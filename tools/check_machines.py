#!/usr/bin/env python3
"""Check the machine-class pages against their template and the machines index.

For every ``docs/machines/*.md`` page except ``index.md``:

* the H2 headings are exactly the template's, in order, and the H3
  headings under "At SkyWater" and "References" are exactly the
  template's;
* the steps paragraph under "SKY130 steps assigned to this class" links
  the same steps as the page's row in the main table of
  ``docs/machines/index.md`` (the row whose first cell links the page's
  label and whose **last** cell is the Steps cell, whatever the column
  count between them — W0e, report-B B2), separately for the main list,
  the "*alternative:*" list and the "*also …:*" lists, so a step moved
  between lists is caught; a step listed twice in one list, and
  "*also …:*" marker wording that differs between page and index, are
  reported too.

Exit status is non-zero on any problem.  Run with
``uv run tools/check_machines.py``. Run with ``--selftest`` for the
offline ``index_rows_from_lines`` unit tests (touches no files).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MACHINES = ROOT / "docs" / "machines"

H2 = [
    "What the machine class is and how it works",
    "Representative 200 mm-era models",
    "At SkyWater",
    "Consumables and facilities",
    "Process-integration notes for SKY130",
    "Related pages",
    "References",
    "Open questions",
]
H3 = {
    "At SkyWater": [
        "What SkyWater lists",
        "Strength of the evidence",
        "SKY130 steps assigned to this class",
    ],
    "References": ["Cross-check", "High-level understanding", "Deep dive"],
}
STEPS_H3 = "SKY130 steps assigned to this class"
# Both {ref}`text <step-NNN>` and the bare {ref}`step-NNN` form.
STEP_RE = re.compile(r"\{ref\}`(?:[^`<]*<)?(step-\d{3})>?`")
LABEL_RE = re.compile(r"^\((machine-[a-z0-9-]+)\)=$", re.MULTILINE)
# "*alternative:*" or "*also for a clean:*" (any "*also …:*" wording).
MARKER_RE = re.compile(r"(\*alternative:\*|\*also\b[^*]*:\*)")
LISTS = ("steps", "alternative", "also")


def sections(text: str, level: str) -> dict[str, str]:
    """Map each heading of the given level (``##`` or ``###``) to its body."""
    parts = re.split(rf"^{level} (.+)$", text, flags=re.MULTILINE)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}


def step_lists(text: str) -> tuple[dict[str, list[str]], list[str]]:
    """Main, "*alternative:*" and "*also …:*" steps in a paragraph or cell.

    Each marker starts a new list that runs to the next marker, so the
    lists may appear in any order; several "*also …:*" lists are merged.
    Whitespace is collapsed first, so a marker may wrap across lines.
    Also returns the "*also …:*" marker texts, in order.
    """
    parts = MARKER_RE.split(re.sub(r"\s+", " ", text))
    lists: dict[str, list[str]] = {name: [] for name in LISTS}
    lists["steps"] += STEP_RE.findall(parts[0])
    also_markers = []
    for i in range(1, len(parts), 2):
        name = "alternative" if parts[i].startswith("*alternative") else "also"
        if name == "also":
            also_markers.append(parts[i])
        lists[name] += STEP_RE.findall(parts[i + 1])
    return lists, also_markers


def duplicates(steps: list[str]) -> list[str]:
    return sorted({s for s in steps if steps.count(s) > 1})


def index_rows_from_lines(lines: list[str]) -> dict[str, str]:
    """Map a machine label to the Steps cell of its main-table row.

    A matching line is any ``| `` row whose first cell links a
    ``machine-…`` label; the **last** cell is the Steps cell, whatever
    the column count in between (report-B B2: the index may shrink from
    the current four columns to just ``Machine class | Steps``, moving
    the descriptive columns to cards). At least two cells are required,
    so a one-column line cannot be mistaken for a row. As before, the
    **last** matching line wins, so a differently-shaped table placed
    after the main one can still silently override a checked row —
    see R-INDEX rule 4 in readability-guide.md.
    """
    rows = {}
    for line in lines:
        if not line.startswith("| "):
            continue
        cells = line.split(" | ")
        m = re.search(r"<(machine-[a-z0-9-]+)>", cells[0])
        if m and len(cells) >= 2:
            rows[m.group(1)] = cells[-1]
    return rows


def index_rows() -> dict[str, str]:
    """Map a machine label to the Steps cell of its main-table row."""
    return index_rows_from_lines((MACHINES / "index.md").read_text().splitlines())


def check(page: Path, rows: dict[str, str]) -> list[str]:
    text = page.read_text()
    problems = []
    h2 = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
    if h2 != H2:
        problems.append(f"H2 headings {h2} differ from the template")
    body = sections(text, "##")
    for parent, wanted in H3.items():
        h3 = re.findall(r"^### (.+)$", body.get(parent, ""), flags=re.MULTILINE)
        if h3 != wanted:
            problems.append(f"H3 under '{parent}' {h3} differ from {wanted}")

    label = LABEL_RE.search(text)
    if not label:
        return problems + ["no (machine-…)= label"]
    row = rows.get(label.group(1))
    if row is None:
        return problems + [f"no main-table row links {label.group(1)} in index.md"]
    steps_body = sections(body.get("At SkyWater", ""), "###").get(STEPS_H3, "")
    # The first paragraph that links a step and is not a bullet list (a
    # paragraph may itself start with the emphasis "*alternative:*").
    paragraph = next((p for p in steps_body.split("\n\n") if STEP_RE.search(p)
                      and not re.match(r"\*\s", p.lstrip())), "")
    page_lists, page_markers = step_lists(paragraph)
    row_lists, row_markers = step_lists(row)
    for name in LISTS:
        got, want = set(page_lists[name]), set(row_lists[name])
        if got != want:
            problems.append(
                f"{name}: page only {sorted(got - want)}, index only {sorted(want - got)}"
            )
        for where, steps in (("page", page_lists[name]), ("index", row_lists[name])):
            if duplicates(steps):
                problems.append(f"{name}: {where} lists {duplicates(steps)} twice")
    if page_markers != row_markers:
        problems.append(f"'also' markers differ: page {page_markers}, index {row_markers}")
    return problems


def selftest() -> int:
    """Offline unit tests for ``index_rows_from_lines`` (W0e: the machines
    index may shrink to a two-column ``Machine class | Steps`` table).
    Touches no files."""
    problems: list[str] = []

    # 1. The old, four-column form still works: the last (fourth) cell is
    #    read as the Steps cell, unchanged from before W0e.
    old = [
        "| {ref}`wet bench <machine-wet-bench>` | What it does | Tools | "
        "{ref}`NS19 <step-013>` |"
    ]
    got = index_rows_from_lines(old)
    if got.get("machine-wet-bench") != "{ref}`NS19 <step-013>` |":
        problems.append(f"old 4-column form: {got!r}")

    # 2. The new, two-column form (Machine class | Steps) is read the same
    #    way: first cell links the label, last cell is Steps.
    new = ["| {ref}`wet bench <machine-wet-bench>` | {ref}`NS19 <step-013>` |"]
    got = index_rows_from_lines(new)
    if got.get("machine-wet-bench") != "{ref}`NS19 <step-013>` |":
        problems.append(f"new 2-column form: {got!r}")

    # 3. A shape with columns in between (more than two, fewer than four)
    #    also works: only the position of the first and last cell matters.
    mid = ["| {ref}`wet bench <machine-wet-bench>` | grouping | "
           "{ref}`NS19 <step-013>` |"]
    got = index_rows_from_lines(mid)
    if got.get("machine-wet-bench") != "{ref}`NS19 <step-013>` |":
        problems.append(f"3-column form: {got!r}")

    # 4. A one-column line (no room for a separate Steps cell) is not
    #    mistaken for a row.
    one = ["| {ref}`wet bench <machine-wet-bench>` |"]
    got = index_rows_from_lines(one)
    if got:
        problems.append(f"a one-column line was wrongly read as a row: {got!r}")

    # 5. The last matching line still wins, in both the old and new shapes.
    two_old = [
        "| {ref}`wet bench <machine-wet-bench>` | a | b | {ref}`NS19 <step-013>` |",
        "| {ref}`wet bench <machine-wet-bench>` | a | b | {ref}`FOM <step-004>` |",
    ]
    got = index_rows_from_lines(two_old)
    if got.get("machine-wet-bench") != "{ref}`FOM <step-004>` |":
        problems.append(f"last-line-wins (old shape): {got!r}")
    two_new = [
        "| {ref}`wet bench <machine-wet-bench>` | {ref}`NS19 <step-013>` |",
        "| {ref}`wet bench <machine-wet-bench>` | {ref}`FOM <step-004>` |",
    ]
    got = index_rows_from_lines(two_new)
    if got.get("machine-wet-bench") != "{ref}`FOM <step-004>` |":
        problems.append(f"last-line-wins (new shape): {got!r}")

    # 6. A line whose first cell links no machine label is not a row.
    unrelated = ["| Something else | {ref}`NS19 <step-013>` |"]
    if index_rows_from_lines(unrelated):
        problems.append("a line with no machine link in its first cell was read as a row")

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
    rows = index_rows()
    pages = sorted(p for p in MACHINES.glob("*.md") if p.name != "index.md")
    bad = 0
    for page in pages:
        for problem in check(page, rows):
            bad += 1
            print(f"{page.name}: {problem}")
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import gen_index_links
    link_problems = gen_index_links.stale_pages_in("machines")
    for p in link_problems:
        print(p)
    print(f"{len(pages)} machine pages checked, {bad} problems, "
          f"{len(link_problems)} with a stale index-links block")
    return 1 if bad or link_problems else 0


if __name__ == "__main__":
    sys.exit(main())
