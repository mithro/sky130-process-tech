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
* the steps paragraph (the first paragraph under that heading that links
  a step and is not a bullet list) links exactly the union of the steps
  in the claimed rows' Steps cells ("all except" cells count as the
  complement over the 171 steps).

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
ALL_STEPS = {f"step-{n:03d}" for n in range(1, 172)}
STEP_RE = re.compile(r"<(step-\d{3})>`")
FOOTNOTE_RE = re.compile(r"\[\^[A-Za-z0-9_-]+\]")


def norm(text: str) -> str:
    """Remove footnote references and collapse white space."""
    return " ".join(FOOTNOTE_RE.sub("", text).split())


def sections(text: str, level: str) -> dict[str, str]:
    """Map each heading of the given level (``##`` or ``###``) to its body."""
    parts = re.split(rf"^{level} (.+)$", text, flags=re.MULTILINE)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}


def cell_steps(cell: str) -> set[str]:
    steps = set(STEP_RE.findall(cell))
    return ALL_STEPS - steps if cell.strip().startswith("all except") else steps


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


def check(page: Path, rows: dict[str, tuple[str, str]],
          owners: dict[str, list[str]]) -> list[str]:
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
        return problems + [f"no bullet list after '{ROWS_INTRO}'"]
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

    paragraph = next((p for p in steps_body.split("\n\n") if STEP_RE.search(p)
                      and not re.match(r"\*\s", p.lstrip())), "")
    got = set(STEP_RE.findall(paragraph))
    if got != want:
        problems.append(
            f"steps: page only {sorted(got - want)}, rows only {sorted(want - got)}"
        )
    return problems


def main() -> int:
    materials = Path(sys.argv[1]) if len(sys.argv) > 1 else MATERIALS
    rows = index_rows(materials)
    pages = sorted(p for p in materials.glob("*.md") if p.name != "index.md")
    owners: dict[str, list[str]] = {}
    bad = 0
    for page in pages:
        for problem in check(page, rows, owners):
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
