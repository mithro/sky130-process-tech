#!/usr/bin/env python3
"""Generate stub step pages and the step index from ``tools/steps.csv``.

Existing step pages are *never* overwritten; only missing pages are
created, so the script is safe to re-run after real content has been
written.  ``docs/steps/index.md`` is always regenerated.

``--check`` fails if the committed ``docs/steps/index.md`` differs from
what this script would write, or if a step page that should exist is
missing.  It never writes anything.  Written step pages themselves are
never compared or touched by ``--check`` (or by a normal run): once a
page exists, its content is the writers' to keep.

Run with ``uv run tools/gen_steps.py [--check]``.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "tools" / "steps.csv"
STEPS = ROOT / "docs" / "steps"

# Step category by explicit assignment.  Codes are matched exactly first,
# then by regular expression in order.  Categories correspond to pages
# under docs/categories/.
EXPLICIT = {
    "SMAT": "substrate",
    "BOX": "oxidation",
    "ISONIT": "deposition",
    "STINITE": "etch",
    "STIE": "etch",
    "LINOX": "oxidation",
    "FILOX": "deposition",
    "CMPNIT": "cmp",
    "NS19": "strip",
    "RTAI": "anneal",
    "TUNARCE": "etch",
    "TUNME": "etch",
    "ONO": "oxidation",
    "ONOME": "etch",
    "GOX100": "oxidation",
    "GOXETCH": "etch",
    "LVGOX": "oxidation",
    "SAGD": "deposition",
    "GATENIT": "deposition",
    "POC": "deposition",
    "BFR": "etch",
    "P1ME": "etch",
    "IOX45": "oxidation",
    "TIPRTAD": "anneal",
    "SPNIT": "deposition",
    "SPE": "etch",
    "NPCME": "etch",
    "SPOX": "deposition",
    "RTAD": "anneal",
    "PSG": "deposition",
    "CMPP": "cmp",
    "NCAPOX": "deposition",
    "RTAD2": "anneal",
    "LICM1E": "etch",
    "SACETCH": "etch",
    "ALLY1": "anneal",
    "TI/TIN1": "deposition",
    "CSIL": "anneal",
    "WDEP": "deposition",
    "WCMPLI": "cmp",
    "LITIN": "deposition",
    "LI1ME": "etch",
    "LINIT": "deposition",
    "NILD2": "deposition",
    "CMPL": "cmp",
    "CTME": "etch",
    "TIN2": "deposition",
    "WDEP2": "deposition",
    "WCMP2": "cmp",
    "TIAL6": "deposition",
    "MM1E": "etch",
    "NILD3": "deposition",
    "CMPM": "cmp",
    "NCAPOX3": "deposition",
    "VIME": "etch",
    "TIN3": "deposition",
    "WDEP3": "deposition",
    "WCMP3": "cmp",
    "TIAL12": "deposition",
    "MM2E": "etch",
    "NILD4": "deposition",
    "CMPM2": "cmp",
    "NCAPOX4": "deposition",
    "VIM2E": "etch",
    "TIN4": "deposition",
    "WDEP4": "deposition",
    "WCMP4": "cmp",
    "WTIAL3": "deposition",
    "CAPILD": "deposition",
    "CAPTIW1": "deposition",
    "CAPME": "etch",
    "MM3E": "etch",
    "NILD5": "deposition",
    "CMPM3": "cmp",
    "NCAPOX5": "deposition",
    "VIM3E": "etch",
    "TIN5": "deposition",
    "WDEP5": "deposition",
    "WCMP5": "cmp",
    "WTIAL4": "deposition",
    "CAPILD2": "deposition",
    "CAPTIW2": "deposition",
    "CAP2ME": "etch",
    "MM4E": "etch",
    "NILD6": "deposition",
    "CMPM4": "cmp",
    "NCAPOX6": "deposition",
    "VIM4E": "etch",
    "WTIAL5": "deposition",
    "MM5E": "etch",
    "NFUSOX": "deposition",
    "NSME": "etch",
    "NTSD": "deposition",
    "PDME": "etch",
    "ALLY": "anneal",
    "HPETEST": "test",
}

PATTERNS = [
    (re.compile(r".*IS$"), "strip"),      # implant resist strip
    (re.compile(r".*M\d?$"), "lithography"),  # mask (MM1, CTM1, LICM1, …)
    (re.compile(r".*I\d?$"), "implant"),   # implant
]

CATEGORY_TITLES = {
    "substrate": "Substrate / starting material",
    "oxidation": "Thermal oxidation",
    "deposition": "Thin-film deposition",
    "lithography": "Photolithography (mask step)",
    "etch": "Etch",
    "implant": "Ion implantation",
    "strip": "Resist strip / clean",
    "anneal": "Anneal / thermal processing",
    "cmp": "Chemical-mechanical planarisation",
    "test": "Electrical test / metrology",
}

# Short category labels for the step index (report-A F17): the link
# target is unchanged (CATEGORY_TITLES / category-<cat>), only the link
# text shown in the index table is shortened.
CATEGORY_SHORT = {
    "substrate": "Substrate",
    "oxidation": "Oxidation",
    "deposition": "Deposition",
    "lithography": "Litho",
    "etch": "Etch",
    "implant": "Implant",
    "strip": "Strip/clean",
    "anneal": "Anneal",
    "cmp": "CMP",
    "test": "Test",
}

# Phase boundaries (inclusive step numbers): used only for the
# quick-facts "Phase" cell on step pages, whose 10-way wording is
# already written on all 171 pages and is presentation content that is
# not re-derived here.
PHASES = [
    (1, 13, "FEOL — isolation"),
    (14, 34, "FEOL — wells and channel implants"),
    (35, 47, "FEOL — SONOS and gate dielectrics"),
    (48, 63, "FEOL — gate and poly resistors"),
    (64, 88, "FEOL — extensions, spacers, source/drain"),
    (89, 106, "MOL — silicide and local interconnect"),
    (107, 117, "BEOL — contact and metal 1"),
    (118, 134, "BEOL — via 1, metal 2, via 2"),
    (135, 163, "BEOL — MiM capacitors, metal 3–5, via 3–4"),
    (164, 171, "BEOL — passivation, pads, alloy, test"),
]

# The 13 modules of the overview's module table (docs/overview/index.md,
# "The flow by module"), used only to group the step index (report-A
# F17, report-C C8). This is a different, coarser grouping than PHASES
# above: PHASES is the 10-way "Phase" wording already written into every
# step page's quick-facts table (presentation content, left alone);
# MODULES reuses the overview's own 13 module names and step ranges so
# the index does not invent a fourth vocabulary. See the progress file
# for the reconciliation note.
MODULES = [
    (1, 13, "Starting material, isolation and deep N-well"),
    (14, 34, "Wells and threshold implants"),
    (35, 42, "SONOS tunnel window and ONO stack"),
    (43, 47, "Gate oxides"),
    (48, 63, "Poly gate and poly resistors"),
    (64, 75, "Tips and halos"),
    (76, 88, "Spacers and source/drain"),
    (89, 106, "Pre-metal dielectric, contact silicide and local interconnect"),
    (107, 117, "Metal contact and metal 1"),
    (118, 134, "Via 1, metal 2 and via 2"),
    (135, 148, "First MiM capacitor, metal 3 and via 3"),
    (149, 163, "Metal 4, second MiM capacitor, via 4 and metal 5"),
    (164, 171, "Passivation, pads, alloy and test"),
]

MACHINES_INDEX = ROOT / "docs" / "machines" / "index.md"
MASKS_INDEX = ROOT / "docs" / "masks" / "index.md"

MACHINES_TABLE_HEADER = "| Machine class | What it does in SKY130 | Tools SkyWater lists publicly | Steps |"
MASKS_TABLE_HEADER = ("| Step | PDK mask (`masks.csv`) | Mask-level layers (`gds_layers.csv`) | "
                      "Drawn layers (`gds_layers.csv`) | Patterns | Minimum CD, feature / space |")

STEP_REF_RE = re.compile(r"\{ref\}`[^`]*<step-(\d{3})>`")
MASK_STEP_CELL_RE = re.compile(r"^\{ref\}`([A-Za-z0-9/]+) <step-(\d{3})>`")
MACHINE_REF_RE = re.compile(r"\{ref\}`[^`]*<machine-[^>]+>`")
ROLE_MARKER_RE = re.compile(r"\*[^*]+:\*")


def _table_rows(text: str, header: str) -> list[str]:
    """Data rows (raw ``| ... |`` lines) of the one Markdown table in
    ``text`` whose header line is exactly ``header``: everything from
    two lines after the header (skipping the ``|---|`` rule) up to the
    first line that is not a table row."""
    lines = text.splitlines()
    try:
        i = lines.index(header)
    except ValueError:
        raise SystemExit(f"gen_steps: table header not found: {header!r}")
    rows = []
    j = i + 2
    while j < len(lines) and lines[j].startswith("|"):
        rows.append(lines[j])
        j += 1
    return rows


def _split_row(row: str) -> list[str]:
    return [c.strip() for c in row.strip().strip("|").split("|")]


def machine_class_map() -> dict[int, str]:
    """Step number -> the {ref} link (text and target) of the machine
    class that "Machine classes and the steps that use them" in the
    machines index assigns as the *main* tool for that step (report-B
    B2, "reverse lookup"). Steps named only after a role marker
    (``*alternative:*``, ``*also …:*``, ``*overlay:*``, ``*CD-SEM:*``)
    are not "main" and are not recorded from that row; the first row
    (in the index's own order) to name a step as main wins. No new
    facts: everything comes from the machines index's own cells."""
    text = MACHINES_INDEX.read_text(encoding="utf-8")
    result: dict[int, str] = {}
    for row in _table_rows(text, MACHINES_TABLE_HEADER):
        cells = _split_row(row)
        class_cell, steps_cell = cells[0], cells[3]
        m = MACHINE_REF_RE.search(class_cell)
        if not m:
            continue
        machine_ref = m.group(0)
        marker = ROLE_MARKER_RE.search(steps_cell)
        main_text = steps_cell[:marker.start()] if marker else steps_cell
        for num_s in STEP_REF_RE.findall(main_text):
            result.setdefault(int(num_s), machine_ref)
    return result


def mask_map() -> dict[int, str]:
    """Step number -> the {ref} link to the mask page whose resist
    pattern the step uses, inverting the masks index's "Mask steps in
    this reference" table (its own "Patterns" column plus the mask step
    itself; report-B B2, "reverse lookup"). No new facts."""
    text = MASKS_INDEX.read_text(encoding="utf-8")
    result: dict[int, str] = {}
    for row in _table_rows(text, MASKS_TABLE_HEADER):
        cells = _split_row(row)
        step_cell, patterns_cell = cells[0], cells[4]
        m = MASK_STEP_CELL_RE.match(step_cell)
        if not m:
            raise SystemExit(f"gen_steps: unexpected mask-index step cell: {step_cell!r}")
        code, num_s = m.group(1), m.group(2)
        mask_ref = "{{ref}}`{code} <mask-{slug}>`".format(code=code, slug=slug(code))
        result[int(num_s)] = mask_ref
        for other_s in STEP_REF_RE.findall(patterns_cell):
            result.setdefault(int(other_s), mask_ref)
    return result


def category_for(code: str) -> str:
    if code in EXPLICIT:
        return EXPLICIT[code]
    for pat, cat in PATTERNS:
        if pat.match(code):
            return cat
    raise SystemExit(f"no category for step code {code!r}")


def phase_for(number: int) -> str:
    for lo, hi, name in PHASES:
        if lo <= number <= hi:
            return name
    raise SystemExit(f"no phase for step {number}")


def phase_with_term(phase: str) -> str:
    """``phase`` with a leading FEOL/MOL/BEOL wrapped as a {term} link
    (report-C C9 rule 1: the glossary defines all three). No checker
    reads the Phase cell, so this only affects the rendered link."""
    for term in ("FEOL", "MOL", "BEOL"):
        if phase.startswith(term):
            return f"{{term}}`{term}`" + phase[len(term):]
    return phase


def module_for(number: int) -> str:
    for lo, hi, name in MODULES:
        if lo <= number <= hi:
            return name
    raise SystemExit(f"no module for step {number}")


def slug(code: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", code.lower()).strip("-")


def filename(number: int, code: str) -> str:
    return f"{number:03d}-{slug(code)}.md"


def load_steps() -> list[dict]:
    with CSV.open(newline="") as fh:
        rows = list(csv.DictReader(fh))
    for row in rows:
        row["number"] = int(row["number"])
        row["category"] = category_for(row["code"])
        row["phase"] = phase_for(row["number"])
        row["file"] = filename(row["number"], row["code"])
    return rows


STUB = """\
(step-{num:03d})=
# Step {num:03d} — {code}: {name}

:::{{warning}}
This page is a stub. Content has not yet been researched and reviewed.
:::

| | |
|---|---|
| **Step number** | {num} of 171 |
| **Step code** | `{code}` |
| **Category** | {{ref}}`{cat_title} <category-{cat}>` |
| **Phase** | {phase} |
| **Previous step** | {prev} |
| **Next step** | {next} |

## What this step is

*To be written.*

## Step category

*To be written.*

## Why this step exists

*To be written.*

## How it is typically performed

*To be written.*

## Machines typically used

*To be written.*

## Machines likely used at SkyWater

*To be written.*

## Resources required

*To be written.*

## Related steps and cross-references

*To be written.*

## References

### Cross-check

*To be written.*

### High-level understanding

*To be written.*

### Deep dive

*To be written.*

## Open questions

*To be written.*
"""


def ref(step: dict | None) -> str:
    if step is None:
        return "—"
    return "{{ref}}`{code} <step-{num:03d}>`".format(code=step["code"], num=step["number"])


def write_stub(step: dict, prev: dict | None, nxt: dict | None) -> bool:
    path = STEPS / step["file"]
    if path.exists():
        return False
    path.write_text(
        STUB.format(
            num=step["number"],
            code=step["code"],
            name=step["name"],
            cat=step["category"],
            cat_title=CATEGORY_TITLES[step["category"]],
            phase=phase_with_term(step["phase"]),
            prev=ref(prev),
            next=ref(nxt),
        )
    )
    return True


INDEX_INTRO = """\
(steps-index)=
# Process steps

The SKY130 flow is documented here as 171 numbered steps, in the
order in which a wafer experiences them. Each step has its own page.
The step numbers and codes are those of the public
*S8 / SKY130 Process Steps* sheet, and the names follow its
descriptions,[^steps-sheet] lightly edited for 20 steps: typing slips
are corrected ("Low Vt NOMOS mask" becomes "Low Vt NMOS mask"),
abbreviations are spelt out, and step 82, which the sheet describes only
by its code "PSDI", is named "P+ source drain implant".
"""

INDEX_FOOTNOTES = """\
<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    retrieved 2026-09-14; tab "Sheet1" lists the 171 steps (number, code and
    description). <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
"""


def index_text(steps: list[dict]) -> str:
    by_number = {s["number"]: s for s in steps}
    machines = machine_class_map()
    masks = mask_map()

    lines = INDEX_INTRO.splitlines()
    lines.append("")
    for lo, hi, module_name in MODULES:
        lines.append(f"## {module_name}")
        lines.append("")
        lines.append("| Step | Code | Name | Category |")
        lines.append("|---:|---|---|---|")
        for num in range(lo, hi + 1):
            s = by_number[num]
            lines.append(
                "| {num} | {{ref}}`{code} <step-{num:03d}>` | {name} | {{ref}}`{cat_short} <category-{cat}>` |".format(
                    num=num,
                    code=s["code"],
                    name=s["name"],
                    cat=s["category"],
                    cat_short=CATEGORY_SHORT[s["category"]],
                )
            )
        # Reverse lookup (report-B B2): a step's machine class and mask,
        # inverted from the machines and masks indexes. Kept as a second
        # table per module rather than two more columns on the table
        # above, which does not fit usefully at 400 px with six columns.
        lines.append("")
        lines.append("| Step | Code | Machine class | Mask |")
        lines.append("|---:|---|---|---|")
        for num in range(lo, hi + 1):
            s = by_number[num]
            lines.append(
                "| {num} | {{ref}}`{code} <step-{num:03d}>` | {machine} | {mask} |".format(
                    num=num,
                    code=s["code"],
                    machine=machines.get(num, "—"),
                    mask=masks.get(num, "—"),
                )
            )
        lines.append("")
    lines += ["```{toctree}", ":maxdepth: 1", ":hidden:", ""]
    for s in steps:
        lines.append(
            "{num:03d} {code} — {name} <{file}>".format(
                num=s["number"], code=s["code"], name=s["name"], file=s["file"][:-3]
            )
        )
    lines += ["```", ""]
    lines += INDEX_FOOTNOTES.splitlines()
    return "\n".join(lines) + "\n"


def write_index(steps: list[dict]) -> None:
    (STEPS / "index.md").write_text(index_text(steps))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                     help="fail if docs/steps/index.md differs from generated, or a step page is missing")
    args = ap.parse_args()

    steps = load_steps()

    if args.check:
        problems = []
        for s in steps:
            if not (STEPS / s["file"]).exists():
                problems.append(f"docs/steps/{s['file']}: missing")
        index_path = STEPS / "index.md"
        expected = index_text(steps)
        if not index_path.exists():
            problems.append("docs/steps/index.md: missing")
        elif index_path.read_text() != expected:
            problems.append("docs/steps/index.md: differs from generated output (run `uv run tools/gen_steps.py`)")
        for p in problems:
            print(p)
        print(f"{len(steps)} steps, {len(problems)} problem(s)")
        return 1 if problems else 0

    STEPS.mkdir(parents=True, exist_ok=True)
    created = 0
    for i, step in enumerate(steps):
        prev = steps[i - 1] if i > 0 else None
        nxt = steps[i + 1] if i + 1 < len(steps) else None
        created += write_stub(step, prev, nxt)
    write_index(steps)
    print(f"{created} stub(s) created, {len(steps)} steps indexed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
