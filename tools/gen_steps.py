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
OVERVIEW_INDEX = ROOT / "docs" / "overview" / "index.md"
OVERVIEW_MODULES_HEADER = "| Module | Steps | Number of steps | Mask steps | Key public facts |"

MACHINES_TABLE_HEADER = "| Machine class | What it does in SKY130 | Tools SkyWater lists publicly | Steps |"
MASKS_TABLE_HEADER = ("| Step | PDK mask (`masks.csv`) | Mask-level layers (`gds_layers.csv`) | "
                      "Drawn layers (`gds_layers.csv`) | Patterns | Minimum CD, feature / space |")

# A single step ref, optionally paired with a second one across an en
# dash to spell a contiguous range ("{ref}`A <step-010>`-{ref}`B
# <step-013>`" means steps 10-13 inclusive; review L2).
STEP_REF_OR_RANGE_RE = re.compile(
    r"\{ref\}`[^`]*<step-(\d{3})>`(?:\s*[–-]\s*\{ref\}`[^`]*<step-(\d{3})>`)?"
)
MASK_STEP_CELL_RE = re.compile(r"^\{ref\}`([A-Za-z0-9/]+) <step-(\d{3})>`")
MACHINE_REF_RE = re.compile(r"\{ref\}`([^`<]+) <(machine-[^>]+)>`")
ROLE_MARKER_RE = re.compile(r"\*[^*]+:\*")

# Rows the machines index's own text excludes when it counts steps with
# two equal main options ("A script check of the process-tool entries
# (all rows except the track, the post-CMP cleaner and the metrology
# rows, ...) finds all 171 steps in at least one row" - docs/machines/
# index.md, "Machine classes and the steps that use them"): supporting
# equipment used to check or handle other steps' work, not a step's own
# process tool. Excluding them from the reverse lookup matches the
# index's own accounting exactly (review M3) and, as a side effect,
# removes every row that uses the "A-B" range shorthand for a long run
# of steps (review M4/L2): the remaining process-tool rows name steps
# individually or in short, genuine either/or ranges only.
#
# "Parametric tester and prober" is deliberately NOT here even though
# the index calls it a metrology tool in prose: unlike the other five,
# its main list names a step it is the process step FOR (electrical
# test, {ref}`HPETEST <step-171>`), not only steps it checks after the
# fact (its "*electrical monitor named:*" list, correctly excluded as
# non-main); dropping it would leave step 171 with no machine class,
# contradicting the index's own "all 171 steps in at least one row".
SUPPORTING_EQUIPMENT_TARGETS = {
    "machine-coat-develop-track",
    "machine-post-cmp-cleaner",
    "machine-cd-sem-overlay-metrology",
    "machine-film-thickness-metrology",
    "machine-sheet-resistance-metrology",
    "machine-cross-section-sem-profilers",
    "machine-defect-inspection",
}


def expand_step_refs(text: str) -> list[int]:
    """Every step number named in ``text`` by a bare {ref} or by an
    en-dash range of two of them (review L2)."""
    nums: list[int] = []
    for m in STEP_REF_OR_RANGE_RE.finditer(text):
        lo = int(m.group(1))
        if m.group(2):
            nums.extend(range(lo, int(m.group(2)) + 1))
        else:
            nums.append(lo)
    return nums


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


def machine_class_map() -> dict[int, list[str]]:
    """Step number -> the {ref} link(s) (text and target) of the machine
    class(es) that "Machine classes and the steps that use them" in the
    machines index assigns as *main* tool for that step (report-B B2,
    "reverse lookup"). Steps named only after a role marker
    (``*alternative:*``, ``*also …:*``, ``*overlay:*``, ``*CD-SEM:*``)
    are not "main" and are not recorded from that row. Supporting
    equipment (the resist track, the post-CMP cleaner, and metrology
    rows) is excluded, matching the machines index's own accounting
    (its "Machine classes and the steps that use them" intro: "all rows
    except the track, the post-CMP cleaner and the metrology rows ...
    finds all 171 steps in at least one row, and ... 25 steps in two,
    where a page offers two tool classes as equal options" — review
    M3/M4/L2). A step named main by two rows keeps both, in the index's
    own row order (caller joins with "or"; review M3). No new facts:
    everything comes from the machines index's own cells."""
    return _machine_class_map_from_text(MACHINES_INDEX.read_text(encoding="utf-8"))


def _machine_class_map_from_text(text: str) -> dict[int, list[str]]:
    """The parsing core of ``machine_class_map()``, taking the machines
    index's own text as a parameter so ``--selftest`` can pin the role-
    marker, exclusion and ambiguous-label rules against a small
    synthetic table instead of the real, large one (review L6)."""
    rows = []
    label_counts: dict[str, int] = {}
    for row in _table_rows(text, MACHINES_TABLE_HEADER):
        cells = _split_row(row)
        class_cell, steps_cell = cells[0], cells[3]
        m = MACHINE_REF_RE.search(class_cell)
        if not m or m.group(2) in SUPPORTING_EQUIPMENT_TARGETS:
            continue
        label = m.group(1)
        label_counts[label] = label_counts.get(label, 0) + 1
        rows.append((m, class_cell, steps_cell))

    result: dict[int, list[str]] = {}
    for m, class_cell, steps_cell in rows:
        label, target = m.group(1), m.group(2)
        if label_counts[label] > 1:
            # Ambiguous base label shared by several rows (e.g. three
            # "Vertical batch furnace" process rows): fold the cell's
            # own qualifier, given after the role, into the link text
            # so the reverse-lookup table can tell them apart (review
            # M4). Rows with a unique label are left exactly as the
            # index writes them.
            after = re.split(r"[;,]", class_cell[m.end():], maxsplit=1)[0]
            qualifier = after.lstrip(": ").strip().rstrip(".")
            label = f"{label}: {qualifier}" if qualifier else label
        machine_ref = f"{{ref}}`{label} <{target}>`"
        marker = ROLE_MARKER_RE.search(steps_cell)
        main_text = steps_cell[:marker.start()] if marker else steps_cell
        for num in expand_step_refs(main_text):
            claims = result.setdefault(num, [])
            if machine_ref not in claims:
                claims.append(machine_ref)
    return result


def mask_map() -> dict[int, str]:
    """Step number -> the {ref} link to the mask page whose resist
    pattern the step uses, inverting the masks index's "Mask steps in
    this reference" table (its own "Patterns" column plus the mask step
    itself; report-B B2, "reverse lookup"). No new facts."""
    return _mask_map_from_text(MASKS_INDEX.read_text(encoding="utf-8"))


def _mask_map_from_text(text: str) -> dict[int, str]:
    """The parsing core of ``mask_map()``, taking the masks index's own
    text as a parameter (review L6, see ``_machine_class_map_from_text``)."""
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
        for other in expand_step_refs(patterns_cell):
            result.setdefault(other, mask_ref)
    return result


def check_modules_match_overview() -> None:
    """Fail loudly if MODULES drifts from the overview's own "The flow by
    module" table (review L1): MODULES is a hand copy of it, made once
    when the step index was grouped, and nothing previously asserted the
    two stay equal."""
    text = OVERVIEW_INDEX.read_text(encoding="utf-8")
    overview: list[tuple[int, int, str]] = []
    for row in _table_rows(text, OVERVIEW_MODULES_HEADER):
        cells = _split_row(row)
        name, steps_cell, count_cell = cells[0], cells[1], cells[2]
        nums = [int(n) for n in re.findall(r"<step-(\d{3})>", steps_cell)]
        if len(nums) != 2:
            raise SystemExit(f"gen_steps: unexpected overview module Steps cell: {steps_cell!r}")
        lo, hi = nums
        if hi - lo + 1 != int(count_cell):
            raise SystemExit(
                f"gen_steps: overview module {name!r} step range {lo}-{hi} "
                f"does not match its own Number of steps {count_cell!r}"
            )
        overview.append((lo, hi, name))
    if overview != MODULES:
        raise SystemExit(
            "gen_steps.MODULES has drifted from docs/overview/index.md's module "
            f"table.\noverview: {overview!r}\nMODULES:  {MODULES!r}"
        )


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
    check_modules_match_overview()
    by_number = {s["number"]: s for s in steps}
    machines = machine_class_map()
    masks = mask_map()

    lines = INDEX_INTRO.splitlines()
    lines.append("")
    # review L5: a lead-in explaining the two-table-per-module layout and
    # what "—" and "or" mean in the second table, so a reader meets the
    # pattern once instead of 13 times unexplained.
    lines.append(
        "Each module below is listed twice: first by name and category, "
        "then by the machine class and mask that the "
        "{ref}`machines index <machines-index>` and "
        "{ref}`masks index <masks-index>` assign to each step. "
        "A dash means neither index names one; \"or\" means the machines "
        "index offers two tool classes as equal options."
    )
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
            machine = " or ".join(machines.get(num, [])) or "—"
            lines.append(
                "| {num} | {{ref}}`{code} <step-{num:03d}>` | {machine} | {mask} |".format(
                    num=num,
                    code=s["code"],
                    machine=machine,
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


# ---------------------------------------------------------------------------
# Self-test (no repository files touched; review L6)
# ---------------------------------------------------------------------------

def selftest() -> int:
    problems: list[str] = []

    # expand_step_refs(): a bare ref, and an en-dash range of two.
    if expand_step_refs("{ref}`FOM <step-004>`") != [4]:
        problems.append("expand_step_refs did not read a bare ref")
    if expand_step_refs("{ref}`A <step-010>`–{ref}`B <step-013>`") != [10, 11, 12, 13]:
        problems.append("expand_step_refs did not expand an en-dash range")
    if expand_step_refs("{ref}`A <step-001>`, {ref}`B <step-003>`") != [1, 3]:
        problems.append("expand_step_refs joined two bare refs into a range")

    # machine_class_map(): role markers, supporting-equipment exclusion,
    # ambiguous-label disambiguation and multi-row "main" claims, all
    # against a small synthetic table rather than the real one.
    machines_text = "\n".join([
        MACHINES_TABLE_HEADER,
        "|---|---|---|---|",
        "| {ref}`Furnace <machine-furnace-ox>`: oxidation | x | y | {ref}`A <step-001>`, {ref}`B <step-002>`; *alternative:* {ref}`C <step-003>` |",
        "| {ref}`Furnace <machine-furnace-lpcvd>`: LPCVD | x | y | {ref}`C <step-003>` |",
        "| {ref}`RTP <machine-rtp>` | x | y | {ref}`C <step-003>` |",
        "| {ref}`Metrology <machine-cd-sem-overlay-metrology>` | x | y | {ref}`A <step-001>`, {ref}`B <step-002>`, {ref}`C <step-003>` |",
    ])
    mm = _machine_class_map_from_text(machines_text)
    if mm.get(1) != ["{ref}`Furnace: oxidation <machine-furnace-ox>`"]:
        problems.append(f"machine_class_map: step 1 main claim wrong: {mm.get(1)!r}")
    if 3 not in mm or set(mm[3]) != {
        "{ref}`Furnace: LPCVD <machine-furnace-lpcvd>`", "{ref}`RTP <machine-rtp>`"
    }:
        problems.append(f"machine_class_map: step 3's two equal main options not both kept: {mm.get(3)!r}")
    if any("machine-cd-sem-overlay-metrology" in r for v in mm.values() for r in v):
        problems.append("machine_class_map: a supporting-equipment (metrology) row was not excluded")
    if any("Furnace <machine" in r for v in mm.values() for r in v):
        problems.append("machine_class_map: an ambiguous label was not disambiguated with its qualifier")

    # mask_map(): the mask step itself plus its Patterns cell map to the
    # mask; a step named in no row's Patterns cell is simply absent
    # (rendered "—" by the caller).
    masks_text = "\n".join([
        MASKS_TABLE_HEADER,
        "|---|---|---|---|---|---|",
        "| {ref}`FOM <step-004>` | x | y | z | {ref}`STINITE <step-005>`, {ref}`STIE <step-006>` | w |",
    ])
    msk = _mask_map_from_text(masks_text)
    want_mask_ref = "{ref}`FOM <mask-fom>`"
    if msk != {4: want_mask_ref, 5: want_mask_ref, 6: want_mask_ref}:
        problems.append(f"mask_map: unexpected result: {msk!r}")
    if 7 in msk:
        problems.append("mask_map: a step named nowhere was assigned a mask")

    if problems:
        for p in problems:
            print("SELFTEST FAIL:", p)
        print(f"{len(problems)} selftest problem(s)")
        return 1
    print("selftest OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                     help="fail if docs/steps/index.md differs from generated, or a step page is missing")
    ap.add_argument("--selftest", action="store_true", help="run the offline self-test and exit; touches no files")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

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
