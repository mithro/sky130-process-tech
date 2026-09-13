#!/usr/bin/env python3
"""Check the machine-class pages against their template and the machines index.

For every ``docs/machines/*.md`` page except ``index.md``:

* the H2 headings are exactly the template's, in order, and the H3
  headings under "At SkyWater" and "References" are exactly the
  template's;
* the steps paragraph under "SKY130 steps assigned to this class" links
  the same steps as the page's row in the main table of
  ``docs/machines/index.md`` (the row whose first cell links the page's
  label), both before and after "*alternative:*".

Exit status is non-zero on any problem.  Run with
``uv run tools/check_machines.py``.
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
STEP_RE = re.compile(r"\{ref\}`[^`<]*<(step-\d{3})>`")
LABEL_RE = re.compile(r"^\((machine-[a-z0-9-]+)\)=$", re.MULTILINE)


def sections(text: str, level: str) -> dict[str, str]:
    """Map each heading of the given level (``##`` or ``###``) to its body."""
    parts = re.split(rf"^{level} (.+)$", text, flags=re.MULTILINE)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}


def step_sets(text: str) -> tuple[set[str], set[str]]:
    """Steps before and after "*alternative:*" in a paragraph or table cell."""
    main, _, alt = text.partition("*alternative:*")
    return set(STEP_RE.findall(main)), set(STEP_RE.findall(alt))


def index_rows() -> dict[str, str]:
    """Map a machine label to the Steps cell of its main-table row."""
    rows = {}
    for line in (MACHINES / "index.md").read_text().splitlines():
        if not line.startswith("| "):
            continue
        cells = line.split(" | ")
        m = re.search(r"<(machine-[a-z0-9-]+)>", cells[0])
        if m and len(cells) == 4:
            rows[m.group(1)] = cells[3]
    return rows


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
    paragraph = next((p for p in steps_body.split("\n\n") if STEP_RE.search(p)
                      and not p.lstrip().startswith("*")), "")
    for name, got, want in zip(("steps", "alternative"), step_sets(paragraph),
                               step_sets(row)):
        if got != want:
            problems.append(
                f"{name}: page only {sorted(got - want)}, index only {sorted(want - got)}"
            )
    return problems


def main() -> int:
    rows = index_rows()
    pages = sorted(p for p in MACHINES.glob("*.md") if p.name != "index.md")
    bad = 0
    for page in pages:
        for problem in check(page, rows):
            bad += 1
            print(f"{page.name}: {problem}")
    print(f"{len(pages)} machine pages checked, {bad} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
