#!/usr/bin/env python3
"""Generate stub step pages and the step index from ``tools/steps.csv``.

Existing step pages are *never* overwritten; only missing pages are
created, so the script is safe to re-run after real content has been
written.  ``docs/steps/index.md`` is always regenerated.

Run with ``uv run tools/gen_steps.py``.
"""

from __future__ import annotations

import csv
import re
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

# Phase boundaries (inclusive step numbers).
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
            phase=step["phase"],
            prev=ref(prev),
            next=ref(nxt),
        )
    )
    return True


def write_index(steps: list[dict]) -> None:
    lines = [
        "(steps-index)=",
        "# Process steps",
        "",
        "The SKY130 flow is documented here as 171 numbered steps, in the",
        "order in which a wafer experiences them. Each step has its own page.",
        "",
        "| # | Code | Step | Category |",
        "|---|------|------|----------|",
    ]
    for s in steps:
        lines.append(
            "| {num} | {{ref}}`{code} <step-{num:03d}>` | {name} | {{ref}}`{cat_title} <category-{cat}>` |".format(
                num=s["number"],
                code=s["code"],
                name=s["name"],
                cat=s["category"],
                cat_title=CATEGORY_TITLES[s["category"]],
            )
        )
    lines += ["", "```{toctree}", ":maxdepth: 1", ":hidden:", ""]
    lines += [s["file"][:-3] for s in steps]
    lines += ["```", ""]
    (STEPS / "index.md").write_text("\n".join(lines))


def main() -> None:
    steps = load_steps()
    STEPS.mkdir(parents=True, exist_ok=True)
    created = 0
    for i, step in enumerate(steps):
        prev = steps[i - 1] if i > 0 else None
        nxt = steps[i + 1] if i + 1 < len(steps) else None
        created += write_stub(step, prev, nxt)
    write_index(steps)
    print(f"{created} stub(s) created, {len(steps)} steps indexed")


if __name__ == "__main__":
    main()
