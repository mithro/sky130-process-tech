#!/usr/bin/env python3
"""Check the material-class pages against their template and the materials index.

For every ``docs/materials/*.md`` page except ``index.md``:

* the page carries a ``(material-<file stem>)=`` label;
* the H2 headings are exactly the template's, in order, and the H3
  headings under "At SkyWater" and "References" are exactly the
  template's;
* under "SKY130 steps that use this class", the bullet list after
  "Materials index rows covered:" names rows of the main table of
  ``docs/materials/index.md`` (the table under "## Materials index") —
  each bullet is the row's Material cell,
  compared with footnote references removed and white space collapsed;
* no index row is claimed by two pages, and the rows whose Class cell
  links a page's label are exactly the rows that page claims;
* the steps paragraph (the paragraph after the "Steps:" line) links
  exactly the union of the steps in the claimed rows' Steps cells ("all
  except" cells, in any letter case, count as the complement over the
  171 steps), lists no step twice, lists the steps in ascending order,
  and gives each link the step's code (from the title of its page) as
  its text; the bare ``{ref}`step-NNN``` form is accepted too.

Every index Steps cell must start with "all except" or with a step link.

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
ROWS_INTRO = "Materials index rows covered:"
STEPS_INTRO = "Steps:"
ALL_STEPS = {f"step-{n:03d}" for n in range(1, 172)}
# Both {ref}`CODE <step-NNN>` and the bare {ref}`step-NNN` form; group 1 is
# the link text (None for the bare form), group 2 the label.
STEP_RE = re.compile(r"\{ref\}`(?:([^`<]*?)\s*<)?(step-\d{3})>?`")
TITLE_RE = re.compile(r"^# Step (\d{3}) — (.+?):", re.MULTILINE)
FOOTNOTE_RE = re.compile(r"\[\^[A-Za-z0-9_-]+\]")


def norm(text: str) -> str:
    """Remove footnote references and collapse white space."""
    return " ".join(FOOTNOTE_RE.sub("", text).split())


def sections(text: str, level: str) -> dict[str, str]:
    """Map each heading of the given level (``##`` or ``###``) to its body."""
    parts = re.split(rf"^{level} (.+)$", text, flags=re.MULTILINE)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}


def steps_in(text: str) -> list[str]:
    return [label for _, label in STEP_RE.findall(text)]


def is_all_except(cell: str) -> bool:
    return cell.strip().lower().startswith("all except")


def cell_steps(cell: str) -> set[str]:
    steps = set(steps_in(cell))
    return ALL_STEPS - steps if is_all_except(cell) else steps


def step_codes() -> dict[str, str]:
    """Map ``step-NNN`` to the code in the title of that step's page."""
    codes = {}
    for page in STEPS.glob("[0-9][0-9][0-9]-*.md"):
        m = TITLE_RE.search(page.read_text())
        if m:
            codes[f"step-{m.group(1)}"] = m.group(2).strip()
    return codes


def index_rows(materials: Path) -> dict[str, tuple[str, str]]:
    """Map a normalised Material cell to its (Class cell, Steps cell)."""
    rows = {}
    table = sections((materials / "index.md").read_text(), "##").get(TABLE_H2, "")
    for line in table.splitlines():
        if not line.startswith("| "):
            continue
        cells = line.strip().strip("|").split(" | ")
        if len(cells) == 5 and "step-" in cells[4]:
            rows[norm(cells[0])] = (cells[1], cells[4])
    return rows


def claimed_rows(steps_body: str) -> list[str] | None:
    """The bullets after the rows-covered line, each joined onto one line."""
    _, found, rest = steps_body.partition(ROWS_INTRO)
    if not found:
        return None
    bullets: list[str] = []
    for line in rest.lstrip("\n").splitlines():
        if line.startswith("* "):
            bullets.append(line[2:])
        elif line.startswith("  ") and bullets:
            bullets[-1] += " " + line.strip()
        else:
            break
    return [norm(b) for b in bullets]


def paragraph_after(body: str, intro: str) -> str | None:
    """The paragraph that follows a line reading exactly ``intro``."""
    m = re.search(rf"^{re.escape(intro)}[ \t]*\n[ \t]*\n(.+?)(?:\n[ \t]*\n|\Z)",
                  body, flags=re.MULTILINE | re.DOTALL)
    return m.group(1) if m else None


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


def check(page: Path, rows: dict[str, tuple[str, str]],
          owners: dict[str, list[str]], codes: dict[str, str]) -> list[str]:
    text = page.read_text()
    problems = []
    label = f"material-{page.stem}"
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

    steps_body = sections(body.get("At SkyWater", ""), "###").get(STEPS_H3, "")
    claimed = claimed_rows(steps_body)
    if not claimed:
        return problems + [f"no '* ' bullet list after a '{ROWS_INTRO}' line"]
    want: set[str] = set()
    for row in claimed:
        owners.setdefault(row, []).append(page.name)
        if row not in rows:
            problems.append(f"covered row not in the index table: {row!r}")
            continue
        want |= cell_steps(rows[row][1])
        if f"<{label}>" not in rows[row][0]:
            problems.append(f"index Class cell of {row!r} does not link {label}")
    for row, (cls, _) in rows.items():
        if f"<{label}>" in cls and row not in claimed:
            problems.append(f"index row {row!r} links {label} but is not listed")

    paragraph = paragraph_after(steps_body, STEPS_INTRO)
    if paragraph is None:
        return problems + [f"no paragraph after a '{STEPS_INTRO}' line"]
    return problems + check_steps_paragraph(paragraph, want, codes)


def main() -> int:
    materials = Path(sys.argv[1]) if len(sys.argv) > 1 else MATERIALS
    rows = index_rows(materials)
    codes = step_codes()
    pages = sorted(p for p in materials.glob("*.md") if p.name != "index.md")
    owners: dict[str, list[str]] = {}
    bad = 0
    for row, (_, steps_cell) in rows.items():
        if not (is_all_except(steps_cell) or steps_cell.lstrip().startswith("{ref}`")):
            bad += 1
            print(f"index row {row!r}: Steps cell starts with neither 'all except' "
                  "nor a step link")
    for page in pages:
        for problem in check(page, rows, owners, codes):
            bad += 1
            print(f"{page.name}: {problem}")
    for row, names in sorted(owners.items()):
        if len(names) > 1:
            bad += 1
            print(f"index row {row!r} claimed by {', '.join(names)}")
    print(f"{len(pages)} material pages checked, {bad} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
