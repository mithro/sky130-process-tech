#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Generate ``docs/history/stackups.md`` and ``products.md`` from ``data/history/qtp.yaml``.

Every Cypress qualification report in the evidence file that prints a
"Technology/Fab Process Description" block becomes one row of a summary
table (grouped by the design rule the report prints) and one film-by-film
table. Values are copied as the report prints them; the only computed
number is each metal layer's total thickness, the sum of its films,
marked "our arithmetic".

The footnote for a report is ``qtp_footnote(record)``; other history pages
cite the same reports with exactly this text (``tools/gen_history_sources.py``
refuses a label defined two ways).

``uv run tools/gen_history_stackups.py`` writes the page; ``--check`` fails
if it is out of date; ``--sync`` rewrites the ``[^qtp-…]`` footnotes of the
other history pages to the canonical text.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from decimal import ROUND_HALF_UP, Decimal

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "history" / "qtp.yaml"
OUT = ROOT / "docs" / "history" / "stackups.md"
PRODUCTS = ROOT / "docs" / "history" / "products.md"

# Printed-value clean-up for display only: the notes the evidence file adds
# in parentheses ("(printed with the micron sign dropped ...)") are not part
# of the printed value.
NOTE_RE = re.compile(r"\s*\((?:printed|the printed|decoded|as printed|value truncated)[^)]*\)")
# A film thickness: a number with "Å"/"A", or with "K" (kÅ) followed by a unit or a material
# name ("6K Al", ".5KAlCu", "1.2K Å"). "0.5% Cu" and "-5%Cu" are compositions, not thicknesses.
THICK_RE = re.compile(r"(\d[\d,]*(?:\.\d+)?|\.\d+)\s*(?:(K)\s*(?:Å|A\b)?(?=\s*[A-Za-zÅ])|(K)?\s*(?:Å|A(?=[/\s,;]|$)))")

MONTHS = {"Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April", "Jun": "June",
          "Jul": "July", "Aug": "August", "Sep": "September", "Sept": "September", "Oct": "October",
          "Nov": "November", "Dec": "December"}

# Title misprints that the evidence notes identify, folded into the process they name.
ALIASES = {"R7FTW-3R": "R7FT-3R"}

GROUPS = [
    ("0.65 µm", 0.6, 0.7),
    ("0.5 µm", 0.45, 0.55),
    ("0.42 µm and 0.35 µm", 0.33, 0.45),
    ("0.25 µm", 0.24, 0.26),
    ("0.21 µm to 0.15 µm", 0.145, 0.22),
    ("0.13 µm", 0.12, 0.135),
    ("90 nm", 0.085, 0.095),
]


def label(rec: dict) -> str:
    return rec["id"].lower()


def qtp_footnote(rec: dict) -> str:
    """The one canonical footnote definition for a report (continuation
    lines indented four spaces, as citation-style.md asks)."""
    kind = {"QTP": "Product Qualification Report"}.get(rec.get("doc_type", "QTP"), rec.get("doc_type", "report"))
    title = " ".join(str(rec.get("title", "")).split()).replace("*", "\\*")
    printed = str(rec.get("date_printed") or "")
    for short, full in MONTHS.items():
        printed = re.sub(rf"^{short}\b\.?", full, printed)
    when = f", {printed}" if printed else ""
    if rec.get("archive_url"):
        # the cypress.com original is gone; cite the Wayback Machine copy
        return (f"[^{label(rec)}]: Cypress Semiconductor, {kind} QTP {rec.get('number', '')}: *{title}*{when};\n"
                f"    Wayback Machine copy of the cypress.com download.\n    <{rec['archive_url']}>")
    return (f"[^{label(rec)}]: Cypress Semiconductor, {kind} QTP {rec.get('number', '')}: *{title}*{when}.\n"
            f"    <{rec['url']}>")


def link(rec: dict) -> str:
    return rec.get("archive_url") or rec["url"]


def clean(v) -> str:
    return NOTE_RE.sub("", " ".join(str(v).split())) if v is not None else ""


def rule_um(pd: dict) -> float | None:
    text = clean(pd.get("design_rule", ""))
    if text.lower().startswith("not printed"):
        return None
    m = re.search(r"(\d+)\s*nm", text)
    if m:
        return int(m.group(1)) / 1000
    if not re.search(r"(?:µm|um|u\b|m\b|micron|µM|UM)", text, re.I):
        return None
    m = re.search(r"(\d*\.\d+)", text)  # a range such as "0.21 – 0.35 µm" gives its lower bound
    return float(m.group(1)) if m else None


def layers(pd: dict) -> list[tuple[str, str]]:
    comp = clean(pd.get("metal_composition", ""))
    parts = re.split(r";\s*(?=(?:Metal|M)\s*\d)", comp)
    out = []
    for p in parts:
        m = re.match(r"(?:Metal|M)\s*([\d,\s]+?)\s*:\s*(.*)", p.strip())
        if m:
            # "Metal 1,2: ..." gives the same films for two layers
            for n in re.findall(r"\d+", m.group(1)):
                out.append((f"Metal {n}", m.group(2).strip()))
    return out


def total(films: str) -> str:
    """Sum of every film thickness printed for one layer, in µm to 0.001 µm (half up), or "—"
    when no thickness is printed. Works for "500Å Ti/6,000Å Al/1,200Å TiW", for
    "Ti/TiW/Al-Si/TiW, 500A/1200A/6000A/1200A" and for "6K Al, 1200A TiW" alike."""
    angstrom = Decimal(0)
    found = False
    for m in THICK_RE.finditer(films):
        v = Decimal(m.group(1).replace(",", ""))
        angstrom += v * (1000 if (m.group(2) or m.group(3)) else 1)
        found = True
    if not found:
        return "—"
    um = (angstrom / Decimal(10000)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
    note = " (implausibly thin; probably misprinted)" if um < Decimal("0.1") else ""
    return f"{um} µm{note}"


def rule_text(pd: dict) -> str:
    """The printed design rule; the evidence file's note is dropped, but a missing micron sign is
    said, so that "0.5 m" does not read as metres."""
    raw = str(pd.get("design_rule", ""))
    shown = cell(raw)
    if re.search(r"Private-Use-Area glyph", raw):
        shown += " (the report prints µ with a non-standard font glyph)"
    elif re.search(r"micron sign", raw):
        shown += " (the µ is not printed in the report)"
    return shown


def cell(v) -> str:
    return clean(v).replace("|", "\\|") or "—"


def earliest(rec: dict) -> str:
    rows = rec.get("qualification_history") or []
    for r in rows:
        if r.get("date"):
            return f"{r['date']} (QTP {r.get('number')})"
    return "the history table gives no dates" if rows else "no history table"


def build() -> str:
    docs = yaml.safe_load(DATA.read_text(encoding="utf-8"))["documents"]
    usable = [d for d in docs if isinstance(d.get("process_description"), dict)
              and rule_um(d["process_description"]) is not None and layers(d["process_description"])]
    used: list[dict] = []
    out: list[str] = []
    out.append("""(history-stackups)=
# Stackups before S8, as the reports print them

Cypress's qualification reports each carry a "Technology/Fab Process Description": the number of metal
layers, the films of each layer, the passivation, the design rule and the gate oxide. This page copies
those blocks for every report in the evidence file that prints them, so the processes can be compared
with each other and with S8. The page is generated from `data/history/qtp.yaml` by
`tools/gen_history_stackups.py`; edit the evidence, not this page.

## How to read the tables

* **As printed.** Every value is copied from one report, spelling and units included ("A" for Å,
  "Si2N4", "TeOs"). Where two reports on one process disagree, both appear.
* **Our arithmetic.** The "Layer total" column adds up the films of one metal layer. It is not printed in
  the reports.
* **What is missing.** The reports give no inter-metal dielectric thicknesses, no via or contact
  materials and no well or implant data, so the stack cannot be drawn to scale from them.
* **Reissues.** Some reports are reissues with the process block replaced by "Proprietary"; those are
  left out here. See {ref}`history-fabs` for how reissues rename sites.
""")
    out.append("## Summary by design rule\n")
    for name, lo, hi in GROUPS:
        rows = [d for d in usable if lo <= rule_um(d["process_description"]) <= hi]
        if not rows:
            continue
        rows.sort(key=lambda d: (str((d.get("technology_codes") or [""])[0]), d["id"]))
        out.append(f"### {name}\n")
        out.append("| Code | Fab as printed | Metal layers | Gate oxide | Report |")
        out.append("|---|---|---|---|---|")
        for d in rows:
            pd = d["process_description"]
            out.append(f"| {cell((d.get('technology_codes') or ['—'])[0])} | {cell(pd.get('fab_location'))} | "
                       f"{cell(pd.get('number_of_metal_layers'))} | {cell(pd.get('gate_oxide'))} | "
                       f"QTP {d.get('number')}[^{label(d)}] |")
            used.append(d)
        out.append("")
    out.append("## Film by film\n")
    out.append("Each table gives one report's metal layers and passivation, with its design rule and the "
               "earliest dated row of its qualification history.\n")
    for d in sorted(used, key=lambda d: (-rule_um(d["process_description"]), d["id"])):
        pd = d["process_description"]
        out.append(f"### QTP {d.get('number')}: {cell(pd.get('die_fab_line_id'))}\n")
        out.append(f"*{cell(d.get('title'))}.* Design rule: {rule_text(pd)}. "
                   f"Earliest dated history row: {earliest(d)}.[^{label(d)}]\n")
        out.append("| Layer | Films as printed | Layer total (our arithmetic) |")
        out.append("|---|---|---|")
        for lname, films in layers(pd):
            out.append(f"| {lname} | {cell(films)} | {total(films)} |")
        out.append(f"| Passivation | {cell(pd.get('passivation'))} | — |")
        n = pd.get("number_of_metal_layers")
        if isinstance(n, int) and n != len(layers(pd)):
            out.append(f"\nThe report gives {n} metal layers but lists films for {len(layers(pd))}.")
        out.append("")
    out.append("## References\n")
    out.append("### Cross-check\n")
    out.append("* {ref}`history-fabs` — which fab ran each process, from annual reports and the press.\n")
    out.append("### Deep dive\n")
    for d in sorted({x["id"]: x for x in used}.values(), key=lambda x: x["id"]):
        out.append(f"* [Cypress, QTP {d.get('number')}](<{link(d)}>) — {cell(d.get('title'))}.[^{label(d)}]")
    out.append("\n<!-- footnotes -->\n")
    for d in sorted({x["id"]: x for x in used}.values(), key=lambda x: x["id"]):
        out.append(qtp_footnote(d))
    return "\n".join(out) + "\n"


def sync_footnotes() -> int:
    """Rewrite every [^qtp-...] definition on the other history pages to the
    canonical text, so that gen_history_sources.py sees one definition."""
    docs = {d["id"].lower(): d for d in yaml.safe_load(DATA.read_text(encoding="utf-8"))["documents"]}
    changed = 0
    for page in sorted(OUT.parent.glob("*.md")):
        if page in (OUT, PRODUCTS, OUT.parent / "sources.md"):
            continue
        text = page.read_text(encoding="utf-8")
        def repl(m: re.Match) -> str:
            rec = docs.get(m.group(1))
            return qtp_footnote(rec) + "\n" if rec else m.group(0)
        new = re.sub(r"^\[\^(qtp-[a-z0-9]+)\]:.*\n(?:    .*\n)*", repl, text, flags=re.M)
        if new != text:
            page.write_text(new, encoding="utf-8")
            changed += 1
            print(f"synced qtp footnotes on {page.relative_to(ROOT)}")
    return changed


def build_products() -> str:
    """One row per process code: the fabs and the products the reports name."""
    docs = yaml.safe_load(DATA.read_text(encoding="utf-8"))["documents"]
    rows: dict[str, dict] = {}
    for d in docs:
        codes = d.get("technology_codes") or []
        prods = [str(p) for p in (d.get("products") or []) if str(p).strip()]
        if not codes or not prods:
            continue
        code = ALIASES.get(str(codes[0]), str(codes[0]))
        if len(codes) > 3:
            code = "several foundry processes (one summary report)"
        pd = d.get("process_description") if isinstance(d.get("process_description"), dict) else {}
        r = rows.setdefault(code, {"fabs": [], "products": [], "docs": [], "rules": []})
        fab = clean(pd.get("fab_location") or d.get("fab") or "")
        if fab and fab not in r["fabs"]:
            r["fabs"].append(fab)
        for p_ in prods:
            if p_ not in r["products"]:
                r["products"].append(p_)
        r["docs"].append(d)
        if pd and rule_um(pd) is not None:
            r["rules"].append(rule_um(pd))
    for r in rows.values():
        # the design rule most reports print (a lone misprint does not move a process)
        r["rule"] = max(set(r["rules"]), key=lambda v: (r["rules"].count(v), -v)) if r["rules"] else None
    out = ["""(history-products)=
# What was made on each process

The products that Cypress's qualification reports name for each process before S8, with the fabs the
reports give. A report names only the products it qualifies, so these lists are examples, not
complete product lines. The page is generated from `data/history/qtp.yaml` by
`tools/gen_history_stackups.py`; edit the evidence, not this page. The processes themselves are
described on {ref}`history-technologies`.
""", "## Products by process\n"]
    def key(item):
        code, r = item
        return (-(r["rule"] or 0), code)
    used: list[dict] = []
    for name, lo, hi in GROUPS + [("Design rule not printed", -1, 0)]:
        group = [(c, r) for c, r in sorted(rows.items(), key=key)
                 if (r["rule"] is None and lo < 0) or (r["rule"] is not None and lo <= r["rule"] <= hi)]
        if not group:
            continue
        out.append(f"### {name}\n")
        out.append("| Process | Fab as printed | Products named in the reports | Reports |")
        out.append("|---|---|---|---|")
        for code, r in group:
            prods = r["products"]
            shown = ", ".join(prods[:10]) + (f" and {len(prods) - 10} more" if len(prods) > 10 else "")
            reps = "".join(f"[^{label(d)}]" for d in r["docs"])
            out.append(f"| {cell(code)} | {cell('; '.join(r['fabs'][:3]))} | {cell(shown)} | "
                       f"{len(r['docs'])}{reps} |")
            used += r["docs"]
        out.append("")
    uniq = sorted({d["id"]: d for d in used}.values(), key=lambda d: d["id"])
    out.append("## References\n")
    out.append("### Cross-check\n")
    out.append("* {ref}`history-stackups` — the same reports' process descriptions.\n")
    out.append("### Deep dive\n")
    for d in uniq:
        out.append(f"* [Cypress, QTP {d.get('number')}](<{link(d)}>) — {cell(d.get('title'))}.[^{label(d)}]")
    out.append("\n<!-- footnotes -->\n")
    for d in uniq:
        out.append(qtp_footnote(d))
    return "\n".join(out) + "\n"


def main() -> int:
    if "--sync" in sys.argv[1:]:
        sync_footnotes()
        return 0
    bad = 0
    for path, text in ((OUT, build()), (PRODUCTS, build_products())):
        if "--check" in sys.argv[1:]:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                print(f"{path.relative_to(ROOT)} is out of date; run uv run tools/gen_history_stackups.py")
                bad = 1
            else:
                print(f"{path.relative_to(ROOT)} is up to date")
            continue
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")
    return bad


if __name__ == "__main__":
    sys.exit(main())
