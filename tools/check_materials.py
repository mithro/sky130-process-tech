#!/usr/bin/env python3
"""Check the material-class pages against their template and the materials index.

The main table of ``docs/materials/index.md`` (under "## Materials
index") gives every row a key in its first column (`` `hf` ``); the
class-page table under "## How to read the index" assigns every key to
exactly one class page.  The checker verifies:

* **Main table.** Every row has a unique key of lower-case letters,
  digits and hyphens, and its Steps cell starts with "all except" (in
  any letter case) or with a step link.
* **Class-page table.** Each Page cell is either a link
  ``{ref}`slug <material-slug>``` to a page that exists, or
  `` `slug` (not yet written)`` for a page that does not; each slug
  appears once; every material page is in the table; every main-table
  key is owned by exactly one row, and no unknown key is named.
* **Class cells.** A row owned by a written page has a Class cell that
  links that page's label; a row owned by an unwritten page links no
  material page.

For every ``docs/materials/*.md`` page except ``index.md``:

* the page carries a ``(material-<file stem>)=`` label;
* the H2 headings are exactly the template's, in order, and the H3
  headings under "At SkyWater" and "References" are exactly the
  template's;
* the summary table before the first H2 starts with a "What they do" row
  and ends with a "SkyWater evidence" row and a "SKY130 steps" row that
  reads "N steps; see …", where N is the number of steps in the steps
  paragraph;
* under "SKY130 steps that use this class", the ``* `` bullet list after
  the "Materials index rows covered:" line names, one per bullet and
  first on its line (`` * `key` — short name``), exactly the keys the
  class-page table assigns to the page, with none twice;
* the steps paragraph (the paragraph after the "Steps:" line) links
  exactly the union of the steps in those rows' Steps cells ("all
  except" cells count as the complement over the 171 steps), lists no
  step twice, lists the steps in ascending order, and gives each link
  the step's code (from the title of its page) as its text; the bare
  ``{ref}`step-NNN``` form is accepted too.

Exit status is non-zero on any problem.  Run with
``uv run tools/check_materials.py``; an optional argument names another
``materials`` directory to check (used to test the checker on a copy).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MATERIALS = ROOT / "docs" / "materials"
STEPS = ROOT / "docs" / "steps"

H2 = [
    "What the class is and what it does",
    "Representative materials and grades",
    "At SkyWater",
    "Supply, handling, safety and facilities",
    "Process-integration notes for SKY130",
    "Related pages",
    "References",
    "Open questions",
]
H3 = {
    "At SkyWater": [
        "What SkyWater's filings and pages list",
        "Strength of the evidence",
        "SKY130 steps that use this class",
    ],
    "References": ["Cross-check", "High-level understanding", "Deep dive"],
}
STEPS_H3 = "SKY130 steps that use this class"
TABLE_H2 = "Materials index"
MAPPING_H2 = "How to read the index"
MAPPING_HEADER = "| Consumable class | Page |"
ROWS_INTRO = "Materials index rows covered:"
STEPS_INTRO = "Steps:"
SUMMARY_FIRST = "What they do"
SUMMARY_LAST = ("SkyWater evidence", "SKY130 steps")
ALL_STEPS = {f"step-{n:03d}" for n in range(1, 172)}
# Both {ref}`CODE <step-NNN>` and the bare {ref}`step-NNN` form; group 1 is
# the link text (None for the bare form), group 2 the label.
STEP_RE = re.compile(r"\{ref\}`(?:([^`<]*?)\s*<)?(step-\d{3})>?`")
TITLE_RE = re.compile(r"^# Step (\d{3}) — (.+?):", re.MULTILINE)
KEY = r"[a-z0-9][a-z0-9-]*"
KEY_CELL_RE = re.compile(rf"^`({KEY})`$")
KEYS_RE = re.compile(rf"`({KEY})`")
BULLET_KEY_RE = re.compile(rf"^`({KEY})` — \S")
MATERIAL_LINK_RE = re.compile(r"<material-([a-z0-9-]+)>`")
WRITTEN_RE = re.compile(r"^\{ref\}`[^`<]*<material-([a-z0-9-]+)>`$")
UNWRITTEN_RE = re.compile(rf"^`({KEY})` \(not yet written\)$")
STEP_COUNT_RE = re.compile(r"^(\d+) steps?; see ")


def sections(text: str, level: str) -> dict[str, str]:
    """Map each heading of the given level (``##`` or ``###``) to its body."""
    parts = re.split(rf"^{level} (.+)$", text, flags=re.MULTILINE)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}


def table_cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split(" | ")]


def is_all_except(cell: str) -> bool:
    return cell.strip().lower().startswith("all except")


def cell_steps(cell: str) -> set[str]:
    steps = {label for _, label in STEP_RE.findall(cell)}
    return ALL_STEPS - steps if is_all_except(cell) else steps


def step_codes() -> dict[str, str]:
    """Map ``step-NNN`` to the code in the title of that step's page."""
    codes = {}
    for page in STEPS.glob("[0-9][0-9][0-9]-*.md"):
        m = TITLE_RE.search(page.read_text())
        if m:
            codes[f"step-{m.group(1)}"] = m.group(2).strip()
    return codes


class Index:
    """The main table and the class-page table of ``index.md``."""

    def __init__(self, materials: Path) -> None:
        self.problems: list[str] = []
        body = sections((materials / "index.md").read_text(), "##")
        # key -> (Class cell, Steps cell)
        self.rows: dict[str, tuple[str, str]] = {}
        for line in body.get(TABLE_H2, "").splitlines():
            if not line.startswith("| ") or line.startswith("| Key |"):
                continue
            cells = table_cells(line)
            m = KEY_CELL_RE.match(cells[0])
            if len(cells) != 6 or not m:
                self.problems.append(f"main-table row without a key cell: {cells[0]!r}")
                continue
            key = m.group(1)
            if key in self.rows:
                self.problems.append(f"main-table key {key!r} used twice")
            self.rows[key] = (cells[2], cells[5])
            if not (is_all_except(cells[5]) or cells[5].startswith("{ref}`")):
                self.problems.append(
                    f"main-table row {key!r}: Steps cell starts with neither "
                    "'all except' nor a step link"
                )

        # slug -> (written, keys)
        self.pages: dict[str, tuple[bool, list[str]]] = {}
        in_table = False
        for line in body.get(MAPPING_H2, "").splitlines():
            if line.startswith(MAPPING_HEADER):
                in_table = True
                continue
            if not in_table or line.startswith("|--"):
                continue
            if not line.startswith("| "):
                break
            cells = table_cells(line)
            written, unwritten = WRITTEN_RE.match(cells[1]), UNWRITTEN_RE.match(cells[1])
            if not (written or unwritten) or len(cells) != 3:
                self.problems.append(f"class-page table: cannot read row {line!r}")
                continue
            slug = (written or unwritten).group(1)
            if slug in self.pages:
                self.problems.append(f"class-page table: page {slug!r} listed twice")
            self.pages[slug] = (bool(written), KEYS_RE.findall(cells[2]))
            exists = (materials / f"{slug}.md").exists()
            if written and not exists:
                self.problems.append(f"class-page table links {slug!r}, which has no page")
            if unwritten and exists:
                self.problems.append(
                    f"class-page table calls {slug!r} not yet written, but the page exists"
                )
        if not self.pages:
            self.problems.append(f"no class-page table under '## {MAPPING_H2}'")

        self.owner: dict[str, str] = {}
        for slug, (_, keys) in self.pages.items():
            for key in keys:
                if key not in self.rows:
                    self.problems.append(f"class-page table: {slug!r} names unknown key {key!r}")
                elif key in self.owner:
                    self.problems.append(
                        f"key {key!r} owned by both {self.owner[key]!r} and {slug!r}"
                    )
                else:
                    self.owner[key] = slug
        for key, (cls, _) in self.rows.items():
            slug = self.owner.get(key)
            if slug is None:
                self.problems.append(f"key {key!r} is owned by no class page")
                continue
            links = MATERIAL_LINK_RE.findall(cls)
            want = [slug] if self.pages[slug][0] else []
            if links != want:
                self.problems.append(
                    f"Class cell of {key!r} links {links}, expected {want} "
                    f"(owned by {slug!r})"
                )


def claimed_keys(steps_body: str) -> list[str] | None:
    """The bullets after the rows-covered line, as keys (None if no list)."""
    _, found, rest = steps_body.partition(ROWS_INTRO)
    if not found:
        return None
    bullets = []
    for line in rest.lstrip("\n").splitlines():
        if line.startswith("* "):
            bullets.append(line[2:])
        elif not (line.startswith("  ") and bullets):
            break
    if not bullets:
        return None
    return [m.group(1) if (m := BULLET_KEY_RE.match(b)) else f"?{b}" for b in bullets]


def paragraph_after(body: str, intro: str) -> str | None:
    """The paragraph that follows a line reading exactly ``intro``."""
    m = re.search(rf"^{re.escape(intro)}[ \t]*\n[ \t]*\n(.+?)(?:\n[ \t]*\n|\Z)",
                  body, flags=re.MULTILINE | re.DOTALL)
    return m.group(1) if m else None


def check_summary(text: str, n_steps: int) -> list[str]:
    head = text.split("\n## ", 1)[0]
    lines = [line for line in head.splitlines() if line.startswith("|")]
    rows = [table_cells(line) for line in lines[2:]]
    if len(rows) < 3:
        return ["no summary table before the first H2"]
    problems = []
    names = [r[0] for r in rows]
    if names[0] != SUMMARY_FIRST:
        problems.append(f"summary table starts with {names[0]!r}, not {SUMMARY_FIRST!r}")
    if tuple(names[-2:]) != SUMMARY_LAST:
        problems.append(f"summary table ends with {names[-2:]}, not {list(SUMMARY_LAST)}")
    m = STEP_COUNT_RE.match(rows[-1][1] if len(rows[-1]) > 1 else "")
    if not m:
        problems.append("summary table's last row does not read 'N steps; see …'")
    elif int(m.group(1)) != n_steps:
        problems.append(
            f"summary table gives {m.group(1)} steps, the steps paragraph has {n_steps}"
        )
    return problems


def check_steps_paragraph(paragraph: str, want: set[str],
                          codes: dict[str, str]) -> list[str]:
    problems = []
    links = STEP_RE.findall(paragraph)
    steps = [label for _, label in links]
    got = set(steps)
    if got != want:
        problems.append(
            f"steps: page only {sorted(got - want)}, rows only {sorted(want - got)}"
        )
    twice = sorted({s for s in steps if steps.count(s) > 1})
    if twice:
        problems.append(f"steps: {twice} listed twice")
    if steps != sorted(steps):
        problems.append("steps: not in ascending order")
    for text, label in links:
        if text and label in codes and text != codes[label]:
            problems.append(
                f"steps: link text {text!r} for {label} is not its code {codes[label]!r}"
            )
    return problems


def check(page: Path, index: Index, codes: dict[str, str]) -> list[str]:
    text = page.read_text()
    problems = []
    slug = page.stem
    label = f"material-{slug}"
    if not re.search(rf"^\({re.escape(label)}\)=$", text, flags=re.MULTILINE):
        problems.append(f"no ({label})= label")
    h2 = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
    if h2 != H2:
        problems.append(f"H2 headings {h2} differ from the template")
    body = sections(text, "##")
    for parent, wanted in H3.items():
        h3 = re.findall(r"^### (.+)$", body.get(parent, ""), flags=re.MULTILINE)
        if h3 != wanted:
            problems.append(f"H3 under '{parent}' {h3} differ from {wanted}")
    if not index.pages.get(slug, (False,))[0]:
        problems.append("page is not linked in the class-page table of index.md")

    steps_body = sections(body.get("At SkyWater", ""), "###").get(STEPS_H3, "")
    claimed = claimed_keys(steps_body)
    if claimed is None:
        return problems + [f"no '* ' bullet list after a '{ROWS_INTRO}' line"]
    for bad in (k for k in claimed if k.startswith("?")):
        problems.append(f"covered-row bullet does not start with '`key` — ': {bad[1:]!r}")
    keys = [k for k in claimed if not k.startswith("?")]
    twice = sorted({k for k in keys if keys.count(k) > 1})
    if twice:
        problems.append(f"covered rows {twice} listed twice")
    owned = set(index.pages.get(slug, (False, []))[1])
    if set(keys) != owned:
        problems.append(
            f"covered rows: page only {sorted(set(keys) - owned)}, "
            f"index table only {sorted(owned - set(keys))}"
        )
    want: set[str] = set()
    for key in keys:
        if key in index.rows:
            want |= cell_steps(index.rows[key][1])

    paragraph = paragraph_after(steps_body, STEPS_INTRO)
    if paragraph is None:
        return problems + [f"no paragraph after a '{STEPS_INTRO}' line"]
    problems += check_steps_paragraph(paragraph, want, codes)
    return problems + check_summary(text, len(STEP_RE.findall(paragraph)))


def main() -> int:
    materials = Path(sys.argv[1]) if len(sys.argv) > 1 else MATERIALS
    index = Index(materials)
    codes = step_codes()
    pages = sorted(p for p in materials.glob("*.md") if p.name != "index.md")
    bad = 0
    for problem in index.problems:
        bad += 1
        print(f"index.md: {problem}")
    for page in pages:
        for problem in check(page, index, codes):
            bad += 1
            print(f"{page.name}: {problem}")
    link_problems: list[str] = []
    if materials == MATERIALS:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import gen_index_links
        link_problems = gen_index_links.stale_pages_in("materials")
        for p in link_problems:
            print(p)
    print(f"{len(pages)} material pages checked, {bad} problems, "
          f"{len(link_problems)} with a stale index-links block")
    return 1 if bad or link_problems else 0


if __name__ == "__main__":
    sys.exit(main())
