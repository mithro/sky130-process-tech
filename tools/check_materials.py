#!/usr/bin/env python3
"""Check the material-class pages against their template and the materials index.

The main table of ``docs/materials/index.md`` (under "## Materials
index") gives every row a key, normally in its first column
(`` `hf` ``); the class-page table under "## How to read the index"
assigns every key to exactly one class page.  The checker verifies:

* **Main table.** Every row has a unique key of lower-case letters,
  digits and hyphens, and its Steps cell starts with "all except" (in
  any letter case) or with a step link.

  Two row shapes are accepted (W0e, report-B B2 — the second is not
  used by the committed index yet; restructuring it is a separate, W3
  change, not this one):

  1. **The current shape.** The first cell is exactly the key
     (`` `hf` ``) and the row's own last cell is the Steps cell.
  2. **A reader-facing first column.** The first cell is a name for
     readers, not the tooling key, as long as the key still appears
     somewhere in the row (``find_key()``): embedded in that same cell
     (`` Nitrogen (`n2`) ``) or, failing that, in another cell. When
     the main table's header's last cell does not mention "steps", the
     table is read as having **no Steps column** at all, and the Steps
     cell is instead read from a **second** table in the same section,
     shaped ``Material | Steps`` and keyed the same way
     (``read_steps_table()``): one row per key, the key found by
     ``find_key()``, the Steps cell its last cell.

     In this shape the Class cell is not read positionally (its column
     is not fixed): the whole row is searched for the
     ``{ref}`... <material-slug>``` link instead, so the class-to-page
     consistency check below still runs. A row naming more than one
     material link this way is possible and is not specially detected;
     see the class-cell check below.

  Either shape's table may be **split into groups under H3s** (review
  M3, report-B B2 table rule 7, ">40 rows: split by group"): every table
  block under "## Materials index" whose header equals the first
  block's is read as more of the same table, wherever it sits, not only
  the first block. In shape 2, every *other* table block is read the
  same way as the second "Material \\| Steps" table (also possibly
  split into groups); a block matching neither header is reported, not
  silently dropped or merged.

  The second table, when present, is checked as strictly as the main
  one (review M1): a row with fewer than two cells, a row with no key,
  a key used twice, and a key that names a material absent from the
  main table are all reported.
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
Run with ``--selftest`` for the offline ``Index`` unit tests, covering
both main-table shapes above (touches no files other than a temporary
directory it creates and removes itself).
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


SEPARATOR_RE = re.compile(r"^\|[-| :]+\|$")


def table_blocks(body: str) -> list[list[list[str]]]:
    """Every Markdown pipe table in ``body``, each as a list of row
    cell-lists (header row included; a separator row such as ``|---|---|``
    stays inside the table but contributes no cell-list of its own)."""
    blocks: list[list[list[str]]] = []
    current: list[list[str]] = []
    for line in body.splitlines():
        if line.startswith("| "):
            current.append(table_cells(line))
        elif line.startswith("|") and SEPARATOR_RE.match(line.strip()):
            continue  # a separator row does not end the table
        elif current:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)
    return blocks


def find_key(cells: list[str]) -> str | None:
    """The tooling key of a materials-index row (W0e, report-B B2).

    The original layout's first cell is exactly the key
    (`` `hf` ``, ``KEY_CELL_RE``); that is tried first and is the only
    thing tried for a first cell shaped that way, so an old-style row is
    read exactly as before. Where the first cell is instead a
    reader-facing name, a backtick key token embedded in it (say,
    `` Nitrogen (`n2`) ``) is used; failing that, every other cell of the
    row is searched the same way, first match wins. Returns ``None`` if
    no cell carries one.
    """
    m = KEY_CELL_RE.match(cells[0])
    if m:
        return m.group(1)
    for cell in cells:
        found = KEYS_RE.findall(cell)
        if found:
            return found[0]
    return None


def read_steps_table(rows: list[list[str]]) -> tuple[dict[str, str], list[str]]:
    """key -> Steps cell, from a second ``Material | Steps``-shaped table
    (W0e, report-B B2), used when the main table has no Steps column.
    The key is found the same way as the main table's (``find_key``); the
    Steps cell is the row's own last cell. ``rows`` excludes the header.

    Also returns problems (review M1: the old code checked none of
    this): a row with fewer than 2 cells or with no key at all, and a key
    used twice (the *last* such row's Steps cell is kept, same as the
    main table's "used twice" handling, but it is now reported)."""
    out: dict[str, str] = {}
    problems: list[str] = []
    for cells in rows:
        if len(cells) < 2:
            problems.append(f"steps-table row has fewer than 2 cells: {cells!r}")
            continue
        key = find_key(cells)
        if key is None:
            problems.append(f"steps-table row without a key: {cells[0]!r}")
            continue
        if key in out:
            problems.append(f"steps-table key {key!r} used twice")
        out[key] = cells[-1]
    return out, problems


def _table_blocks_by_header(blocks: list[list[list[str]]],
                            main_header: list[str]) -> tuple[list[list[str]], list[list[str]], list[str]]:
    """Split ``blocks`` into (main rows, steps-table rows, problems).

    Every block whose header equals ``main_header`` contributes its rows
    to the main rows — not only the first block (review M3: a materials
    index split into groups under H3s, as B2 table rule 7 asks for tables
    over 40 rows, must still be read as one table). Every other block is
    assumed to be part of the second "Material | Steps" table (also
    possibly split into groups the same way); all such blocks must share
    one header, or the extra one is reported rather than silently
    ignored or silently merged.
    """
    main_rows: list[list[str]] = []
    steps_rows: list[list[str]] = []
    steps_header: list[str] | None = None
    problems: list[str] = []
    for header, *rows in blocks:
        if header == main_header:
            main_rows.extend(rows)
            continue
        if steps_header is None:
            steps_header = header
            if "steps" not in (header[-1].lower() if header else ""):
                problems.append(
                    f"second table under '## {TABLE_H2}' has header {header}, "
                    "whose last cell does not mention 'steps'"
                )
        if header != steps_header:
            problems.append(
                f"unexpected table under '## {TABLE_H2}' with header {header}"
            )
            continue
        steps_rows.extend(rows)
    return main_rows, steps_rows, problems


class Index:
    """The main table and the class-page table of ``index.md``."""

    def __init__(self, materials: Path) -> None:
        self.problems: list[str] = []
        body = sections((materials / "index.md").read_text(), "##")

        blocks = table_blocks(body.get(TABLE_H2, ""))
        if not blocks:
            self.problems.append(f"no table found under '## {TABLE_H2}'")
        main_header = blocks[0][0] if blocks else []
        # A Steps column is recognised by its header wording, not its
        # position, so a reader-facing reordering of the other columns
        # (report-B B2) does not itself require this check to change.
        has_steps_column = bool(main_header) and "steps" in main_header[-1].lower()
        main_rows, other_rows, block_problems = _table_blocks_by_header(blocks, main_header)
        self.problems += block_problems
        steps_by_key: dict[str, str] = {}
        if not has_steps_column:
            if other_rows:
                steps_by_key, steps_problems = read_steps_table(other_rows)
                self.problems += steps_problems
            else:
                self.problems.append(
                    f"main table under '## {TABLE_H2}' has no Steps column, and "
                    "there is no second 'Material | Steps' table to read it from"
                )
        elif other_rows:
            self.problems.append(
                f"main table under '## {TABLE_H2}' has a Steps column, but an extra "
                "table block is also present"
            )

        # key -> (Class cell or row text to search for one, Steps cell)
        self.rows: dict[str, tuple[str, str]] = {}
        main_keys: set[str] = set()
        for cells in main_rows:
            key = find_key(cells)
            if key is None:
                self.problems.append(f"main-table row without a key: {cells[0]!r}")
                continue
            main_keys.add(key)
            if key in self.rows:
                self.problems.append(f"main-table key {key!r} used twice")
            if has_steps_column:
                if len(cells) != len(main_header):
                    self.problems.append(
                        f"main-table row {key!r}: {len(cells)} cells, header has "
                        f"{len(main_header)}"
                    )
                    continue
                class_cell, steps_cell = cells[2], cells[-1]
            else:
                class_cell = " | ".join(cells)
                steps_cell = steps_by_key.get(key)
                if steps_cell is None:
                    self.problems.append(
                        f"main-table row {key!r}: no Steps entry in the second table"
                    )
                    continue
            self.rows[key] = (class_cell, steps_cell)
            if not (is_all_except(steps_cell) or steps_cell.startswith("{ref}`")):
                self.problems.append(
                    f"main-table row {key!r}: Steps cell starts with neither "
                    "'all except' nor a step link"
                )

        # Review M1: a steps-table key naming a material absent from the
        # main table (e.g. a typo, or a leftover row for a deleted
        # material) must be reported, not silently ignored.
        for key in sorted(set(steps_by_key) - main_keys):
            self.problems.append(
                f"steps table names key {key!r}, which is not in the main table"
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


OLD_INDEX = """\
(materials-table)=
## Materials index

| Key | Material | Class | Role in SKY130 steps | Public SkyWater evidence | Steps whose Resources section names it |
|---|---|---|---|---|---|
| `n2` | Nitrogen (N2) | {ref}`Bulk gas <material-widgets>` | Purge gas. | typical | {ref}`SMAT <step-001>` |

(how-to-read-the-index)=
## How to read the index

| Consumable class | Page | Rows owned (keys) |
|---|---|---|
| Widgets | {ref}`widgets <material-widgets>` | `n2` |
"""

NEW_INDEX = """\
(materials-table)=
## Materials index

| Material | Class | Role | Public SkyWater evidence |
|---|---|---|---|
| Nitrogen (`n2`) | {ref}`Bulk gas <material-widgets>` | Purge gas. | typical |

| Material | Steps |
|---|---|
| Nitrogen (`n2`) | {ref}`SMAT <step-001>` |

(how-to-read-the-index)=
## How to read the index

| Consumable class | Page | Rows owned (keys) |
|---|---|---|
| Widgets | {ref}`widgets <material-widgets>` | `n2` |
"""


EXTRA_KEY_INDEX = NEW_INDEX.replace(
    "| Nitrogen (`n2`) | {ref}`SMAT <step-001>` |",
    "| Nitrogen (`n2`) | {ref}`SMAT <step-001>` |\n"
    "| Unobtainium (`unob`) | {ref}`SMAT <step-001>` |",
)

DUPLICATE_KEY_INDEX = NEW_INDEX.replace(
    "| Nitrogen (`n2`) | {ref}`SMAT <step-001>` |",
    "| Nitrogen (`n2`) | {ref}`SMAT <step-001>` |\n"
    "| Nitrogen again (`n2`) | {ref}`BOX <step-002>` |",
)

NO_KEY_ROW_INDEX = NEW_INDEX.replace(
    "| Nitrogen (`n2`) | {ref}`SMAT <step-001>` |",
    "| Nitrogen (`n2`) | {ref}`SMAT <step-001>` |\n"
    "| Mystery material | {ref}`BOX <step-002>` |",
)

# Review M3: the main table (old, key-first shape) split into two groups
# under H3s, as report-B B2 table rule 7 ("> 40 rows: split by group")
# asks for -- `main` accepted this; the un-fixed checker did not.
GROUPED_MAIN_INDEX = """\
(materials-table)=
## Materials index

### Group one

| Key | Material | Class | Role in SKY130 steps | Public SkyWater evidence | Steps whose Resources section names it |
|---|---|---|---|---|---|
| `n2` | Nitrogen (N2) | {ref}`Bulk gas <material-widgets>` | Purge gas. | typical | {ref}`SMAT <step-001>` |

### Group two

| Key | Material | Class | Role in SKY130 steps | Public SkyWater evidence | Steps whose Resources section names it |
|---|---|---|---|---|---|
| `o2` | Oxygen (O2) | {ref}`Bulk gas <material-widgets>` | Oxidant. | typical | {ref}`BOX <step-002>` |

(how-to-read-the-index)=
## How to read the index

| Consumable class | Page | Rows owned (keys) |
|---|---|---|
| Widgets | {ref}`widgets <material-widgets>` | `n2`, `o2` |
"""

# The no-Steps-column shape, both tables split into two groups each.
GROUPED_NEW_INDEX = """\
(materials-table)=
## Materials index

### Group one

| Material | Class | Role | Public SkyWater evidence |
|---|---|---|---|
| Nitrogen (`n2`) | {ref}`Bulk gas <material-widgets>` | Purge gas. | typical |

### Group two

| Material | Class | Role | Public SkyWater evidence |
|---|---|---|---|
| Oxygen (`o2`) | {ref}`Bulk gas <material-widgets>` | Oxidant. | typical |

### Steps, group one

| Material | Steps |
|---|---|
| Nitrogen (`n2`) | {ref}`SMAT <step-001>` |

### Steps, group two

| Material | Steps |
|---|---|
| Oxygen (`o2`) | {ref}`BOX <step-002>` |

(how-to-read-the-index)=
## How to read the index

| Consumable class | Page | Rows owned (keys) |
|---|---|---|
| Widgets | {ref}`widgets <material-widgets>` | `n2`, `o2` |
"""


def _write_index_fixture(tmp: Path, name: str, text: str) -> Path:
    materials = tmp / name / "materials"
    materials.mkdir(parents=True)
    (materials / "index.md").write_text(text)
    (materials / "widgets.md").write_text("(material-widgets)=\n# Widgets\n")
    return materials


def selftest() -> int:
    """Offline unit tests for ``Index``'s two main-table shapes (W0e,
    report-B B2). Touches only a temporary directory it creates and
    removes itself."""
    import tempfile

    problems: list[str] = []

    with tempfile.TemporaryDirectory() as tmp_str:
        tmp = Path(tmp_str)

        old_dir = _write_index_fixture(tmp, "old", OLD_INDEX)
        old = Index(old_dir)
        if old.problems:
            problems.append(f"old-layout fixture reported problems: {old.problems}")
        if old.rows.get("n2") != ("{ref}`Bulk gas <material-widgets>`", "{ref}`SMAT <step-001>`"):
            problems.append(f"old-layout row for 'n2': {old.rows.get('n2')!r}")
        if old.owner.get("n2") != "widgets":
            problems.append(f"old-layout owner for 'n2': {old.owner.get('n2')!r}")

        new_dir = _write_index_fixture(tmp, "new", NEW_INDEX)
        new = Index(new_dir)
        if new.problems:
            problems.append(f"new-layout fixture reported problems: {new.problems}")
        if "n2" not in new.rows:
            problems.append(f"new-layout: key 'n2' not found in rows {new.rows!r}")
        else:
            cls, steps = new.rows["n2"]
            if steps != "{ref}`SMAT <step-001>`":
                problems.append(f"new-layout Steps cell for 'n2': {steps!r}")
            if "<material-widgets>" not in cls:
                problems.append(f"new-layout Class text for 'n2' has no material link: {cls!r}")
        if new.owner.get("n2") != "widgets":
            problems.append(f"new-layout owner for 'n2': {new.owner.get('n2')!r}")

        # A main table with no Steps column and no second table is a
        # reported problem, not a silent miss.
        no_second = OLD_INDEX.replace(
            "| Key | Material | Class | Role in SKY130 steps | Public SkyWater evidence | "
            "Steps whose Resources section names it |\n|---|---|---|---|---|---|\n"
            "| `n2` | Nitrogen (N2) | {ref}`Bulk gas <material-widgets>` | Purge gas. | "
            "typical | {ref}`SMAT <step-001>` |",
            "| Material | Class | Role | Public SkyWater evidence |\n|---|---|---|---|\n"
            "| Nitrogen (`n2`) | {ref}`Bulk gas <material-widgets>` | Purge gas. | typical |",
        )
        missing_dir = _write_index_fixture(tmp, "missing", no_second)
        missing = Index(missing_dir)
        if not any("no second" in p or "no Steps entry" in p for p in missing.problems):
            problems.append(
                f"a missing-Steps-table fixture was not reported: {missing.problems}"
            )

        # Review M1: the second table is now checked as strictly as the
        # main one -- an extra key, a duplicated key and a keyless row
        # must all be reported, not pass silently.
        extra_dir = _write_index_fixture(tmp, "extra", EXTRA_KEY_INDEX)
        extra = Index(extra_dir)
        if not any("unob" in p and "not in the main table" in p for p in extra.problems):
            problems.append(f"an extra steps-table key was not reported: {extra.problems}")

        dup_dir = _write_index_fixture(tmp, "dup", DUPLICATE_KEY_INDEX)
        dup = Index(dup_dir)
        if not any("n2" in p and "used twice" in p for p in dup.problems):
            problems.append(f"a duplicated steps-table key was not reported: {dup.problems}")

        nokey_dir = _write_index_fixture(tmp, "nokey", NO_KEY_ROW_INDEX)
        nokey = Index(nokey_dir)
        if not any("without a key" in p for p in nokey.problems):
            problems.append(f"a keyless steps-table row was not reported: {nokey.problems}")

        # Review M3: a main table split into groups under H3s (B2 table
        # rule 7) is read as one table, in both main-table shapes.
        grouped_main_dir = _write_index_fixture(tmp, "grouped-main", GROUPED_MAIN_INDEX)
        grouped_main = Index(grouped_main_dir)
        if grouped_main.problems:
            problems.append(f"grouped main-table fixture reported problems: {grouped_main.problems}")
        if set(grouped_main.rows) != {"n2", "o2"}:
            problems.append(f"grouped main-table fixture: rows {grouped_main.rows!r}")

        grouped_new_dir = _write_index_fixture(tmp, "grouped-new", GROUPED_NEW_INDEX)
        grouped_new = Index(grouped_new_dir)
        if grouped_new.problems:
            problems.append(f"grouped no-Steps-column fixture reported problems: {grouped_new.problems}")
        if set(grouped_new.rows) != {"n2", "o2"}:
            problems.append(f"grouped no-Steps-column fixture: rows {grouped_new.rows!r}")
        elif grouped_new.rows["o2"][1] != "{ref}`BOX <step-002>`":
            problems.append(f"grouped no-Steps-column fixture: 'o2' Steps cell {grouped_new.rows['o2'][1]!r}")

    if problems:
        for p in problems:
            print("SELFTEST FAIL:", p)
        print(f"{len(problems)} selftest problem(s)")
        return 1
    print("selftest OK")
    return 0


def main() -> int:
    if "--selftest" in sys.argv[1:]:
        return selftest()
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
