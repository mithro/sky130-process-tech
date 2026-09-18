#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Generate the financial filings index pages from ``data/filings.yaml``.

Writes ``docs/references/filings/``:

* ``index.md`` -- scope, a short timeline of the lineage events, counts by
  company/type/year, how to read an entry, the EDGAR access note, a list of
  filings known to exist but not found in a fetchable copy (from the
  dataset's ``known_gaps``), links to the other views and the one full
  entry per filing (under its own label ``filing-<id>``), in date order;
* ``by-company.md`` -- Cypress, SkyWater and Infineon first (the lineage),
  then the acquirer, customers and partners; within a company, by date;
* ``by-year.md`` -- year of filing, newest first;
* ``by-type.md`` -- annual reports, quarterly reports, current reports and
  exhibits, registration statements and prospectuses, proxy statements,
  announcements;
* ``by-relationship.md`` -- one section per relationship tag, grouped as
  Cypress era / SkyWater / Infineon / others, each headed by the tag's
  definition;
* ``audits.md`` -- the auditor's reports found in the records.

The pages are overwritten; do not edit them by hand. Before generating, the
dataset must pass ``tools/check_filings.py``'s offline checks.

``--check`` generates into memory and fails if a committed page differs or
if a page in the directory is not generated.

Run with ``uv run tools/gen_filings.py [--check]``. See
``docs/plans/filings-index-design.md``.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "filings.yaml"
OUT = ROOT / "docs" / "references" / "filings"
HEADER = "<!-- Generated from data/filings.yaml by tools/gen_filings.py; do not edit. -->\n"

sys.path.insert(0, str(ROOT / "tools"))
import check_filings  # noqa: E402

# Company display order: the lineage first, then acquirer, customers, partners.
COMPANY_GROUPS = [
    ("Cypress Semiconductor Corporation (the fab's original owner)", ["cypress"]),
    ("SkyWater Technology, Inc. (bought the fab in 2017)", ["skywater"]),
    ("Infineon Technologies AG (acquired Cypress in 2020, sold Fab 25 in 2025)", ["infineon"]),
    ("IonQ, Inc. (acquirer, 2026)", ["ionq"]),
    ("Customers", ["d-wave"]),
    ("Partners", ["quicklogic", "weebit-nano"]),
    ("Others", ["other"]),
]

DOCTYPE_GROUPS = [
    ("Annual reports", ["annual-report", "annual-report-amendment", "annual-report-to-shareholders"]),
    ("Quarterly and half-year reports", ["quarterly-report", "quarterly-report-amendment", "half-year-report"]),
    ("Current reports and exhibits", ["current-report", "exhibit"]),
    ("Registration statements and prospectuses", ["registration-statement", "prospectus"]),
    ("Proxy statements", ["proxy-statement"]),
    ("Announcements and deregistrations", ["ad-hoc-announcement", "market-announcement", "deregistration"]),
]

REL_GROUPS = [
    ("Cypress era", ["cypress-fab-operations", "cypress-process-technology", "cypress-third-party-foundry",
                     "cypress-fab-sale", "cypress-technology-license", "cypress-foundry-services"]),
    ("SkyWater", ["skywater-fab-history", "skywater-ipo", "skywater-suppliers", "skywater-customers",
                  "oxbow-related-party", "minnesota-fab-investment", "skywater-ionq-merger",
                  "skywater-governance"]),
    ("Infineon", ["infineon-cypress-acquisition", "infineon-fab25-sale", "infineon-wafer-supply"]),
    ("Others", ["supplier-names-skywater", "customer-names-skywater", "partner-names-skywater"]),
]

# The lineage timeline on the index page: (date, headline, record id).
TIMELINE = [
    ("2017-03-01", "Cypress reports the sale of its Minnesota fab (Fab 4, Bloomington) to SkyWater's owners as "
                   "completed during the first quarter of fiscal 2017.",
     "cypress-10-q-2017-05-02"),
    ("2020-04-16", "Infineon completes its acquisition of Cypress Semiconductor.", "cypress-8-k-2020-04-16"),
    ("2021-04-22", "SkyWater Technology files the final prospectus for its initial public offering.",
     "skywater-424b4-2021-04-22"),
    ("2025-06-30", "SkyWater completes the purchase of Infineon's Austin fab (Fab 25).", "skywater-8-k-2025-07-03"),
    ("2026-07-31", "IonQ completes its acquisition of SkyWater Technology.", "skywater-8-k-2026-07-31"),
    ("2026-08-10", "SkyWater deregisters from SEC reporting following the IonQ merger.", "skywater-15-12g-2026-08-10"),
]

IDENT_TEXT = {
    "sec-accession": "SEC accession {value}",
    "ir-filing-id": "investor-relations filing {value}; SEC accession not retrieved",
    "company-document": "document {value}",
    "asx-announcement": "ASX announcement {value}",
}

_ESC = re.compile(r"([\\`*_\[\]<>|#${}])")


def esc(text: object) -> str:
    return _ESC.sub(r"\\\1", " ".join(str(text).split()))


def url(u: str) -> str:
    return u.replace("(", "%28").replace(")", "%29").replace(" ", "%20")


def link(text: str, target: str) -> str:
    return f"[{esc(text)}]({url(target)})"


def plural(n: int, word: str) -> str:
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def page(label: str, title: str, body: list[str]) -> str:
    return HEADER + "\n" + f"({label})=\n# {title}\n\n" + "\n".join(body).rstrip() + "\n"


def rel_label(tag: str) -> str:
    return f"filings-rel-{tag}"


def rel_ref(tag: str) -> str:
    return f"{{ref}}`{esc(check_filings.RELATIONSHIPS[tag])} <{rel_label(tag)}>`"


def identifier_text(r: dict) -> str | None:
    ident = r.get("identifier")
    if not ident:
        return None
    return IDENT_TEXT[ident["scheme"]].format(value=ident["value"])


def links_line(r: dict) -> str:
    urls = r["urls"]
    parts = []
    if urls.get("original"):
        parts.append(link("EDGAR" if "sec.gov" in urls["original"] else "Original", urls["original"]))
    if urls.get("wayback"):
        parts.append(link("Wayback copy", urls["wayback"]))
    if urls.get("ir"):
        parts.append(link("investor-relations copy", urls["ir"]))
    return " · ".join(parts) + "."


def quotes_text(r: dict) -> str:
    return "; ".join(f'"{esc(q["text"])}" ({esc(q["location"])})' for q in r["about"]["quotes"])


def entry_lines(r: dict) -> list[str]:
    ident = identifier_text(r)
    filed_clause = f"filed {r['filed']}" + (f"; {ident}" if ident else "")
    head = f"**{esc(r['company'])} — {esc(r['title'])}** ({filed_clause})."
    out = [f"(filing-{r['id']})=", f"* {head}", f"  {links_line(r)}"]
    # FIL-R1-12: a current report's or exhibit's title carries no period (unlike a
    # 10-K's "fiscal year NNNN" or a 10-Q's "quarter ended ..."), so period.label
    # (e.g. "event of 2022-03-29") would otherwise never reach a page.
    period = r.get("period")
    label = period.get("label") if isinstance(period, dict) else None
    if label and r.get("document_type") in ("current-report", "exhibit"):
        out.append(f"  Period: {esc(label)}.")
    out.append(f"  {esc(r['about']['summary'])} {quotes_text(r)}")
    aud = r.get("auditor_report")
    if aud:
        out.append(f"  Auditor: {esc(aud['firm'])}, {aud['date']}: \"{esc(aud['quote'])}\".")
    rels = " · ".join(rel_ref(t) for t in r["relationships"])
    out.append(f"  Relationships: {rels}.")
    if r.get("inventory_key"):
        out.append(f"  Inventory: {esc(r['inventory_key'])}.")
    if r.get("related_docs"):
        rd = "; ".join(f"{{ref}}`{d['label']}` — {esc(d['reason'])}" for d in r["related_docs"])
        out.append(f"  Related pages: {rd}")
    if r.get("parent"):
        out.append(f"  Amends/filed with: {{ref}}`full entry <filing-{r['parent']}>`.")
    if r.get("notes"):
        out.append(f"  Note: {esc(r['notes'])}")
    out.append("")
    return out


def short_line(r: dict) -> str:
    return (f"* {esc(r['company'])}, {esc(r['form'])}, filed {r['filed']}: {esc(r['title'])} "
            f"({{ref}}`full entry <filing-{r['id']}>`)")


def doctype_group(dt: str) -> str:
    for name, types in DOCTYPE_GROUPS:
        if dt in types:
            return name
    raise SystemExit(f"document_type {dt!r} not covered by DOCTYPE_GROUPS")


def company_keys_in_order() -> list[str]:
    """The company_key values in COMPANY_GROUPS order, asserting every key in
    check_filings.COMPANIES is covered (FIL-R1-09, mirroring doctype_group's and
    gen_by_relationship's own completeness guards)."""
    covered = [k for _, keys in COMPANY_GROUPS for k in keys]
    missing = sorted(set(check_filings.COMPANIES) - set(covered))
    if missing:
        raise SystemExit(f"company_key values not covered by COMPANY_GROUPS: {missing}")
    return covered


def gen_known_gaps(gaps: list[dict]) -> list[str]:
    """FIL-R1-13: a short section on index.md naming filings known to exist (from
    another filing's exhibit index, an inventory entry, or a discovery note) but for
    which no copy could be found or read that is not sec.gov itself, so a reader does
    not have to go looking in docs/plans/ to see what is missing and why."""
    if not gaps:
        return []
    by_company: dict[str, list[dict]] = defaultdict(list)
    for g in gaps:
        by_company[g["company_key"]].append(g)
    body = [
        "## Known gaps",
        "",
        "Filings known to exist -- named in another filing's exhibit index, an",
        "inventory entry already cited elsewhere in this reference, or this",
        "project's own discovery notes -- but for which no copy could be found",
        "or read that is not `sec.gov` itself.",
        "",
    ]
    for key in company_keys_in_order():
        items = by_company.get(key)
        if not items:
            continue
        body.append(f"**{esc(check_filings.COMPANIES[key][0])}**")
        body.append("")
        for g in items:
            body.append(f"* {esc(g['description'])} -- {esc(g['reason'])}")
        body.append("")
    return body


def gen_index(rs: list[dict], gaps: list[dict]) -> str:
    n = len(rs)
    companies = Counter(r["company_key"] for r in rs)
    types = Counter(doctype_group(r["document_type"]) for r in rs)
    years = Counter(r["filed"].year for r in rs)
    by_id = {r["id"]: r for r in rs}
    body = [
        "A catalogue of financial and corporate filings that document the",
        "ownership, business and process lineage of the fab that makes",
        "SKY130: Cypress Semiconductor's Minnesota fab (Fab 4), its 2017 sale",
        "to SkyWater Technology Foundry, SkyWater's life as a public company,",
        "its licence of Cypress process IP (now Infineon's), its 2025 purchase",
        "of Infineon's Austin fab (Fab 25, a former Cypress fab) and its 2026",
        "acquisition by IonQ, together with filings by other companies that",
        "name SkyWater or the Cypress fab. It complements the",
        "{doc}`public sources inventory <../public-sources>`: a filing enters",
        "the inventory only when a page cites it. See",
        "`docs/plans/filings-index-design.md` for the inclusion rules.",
        "",
        f"The index holds {plural(n, 'filing')}.",
        "",
        "## Other views",
        "",
        "* {ref}`filings-by-company`",
        "* {ref}`filings-by-year`",
        "* {ref}`filings-by-type`",
        "* {ref}`filings-by-relationship`",
        "* {ref}`filings-audits`",
        "",
        "```{toctree}",
        ":hidden:",
        "",
        "by-company",
        "by-year",
        "by-type",
        "by-relationship",
        "audits",
        "```",
        "",
        "## Lineage timeline",
        "",
    ]
    for date, headline, rid in TIMELINE:
        body.append(f"* **{date}** — {esc(headline)} See {{ref}}`the filing <filing-{rid}>`.")
    body += [
        "",
        "## How to read an entry",
        "",
        "Each entry gives the filer, the form and what it covers, the filing",
        "date and identifier, links to the copies used, a short summary of",
        "what it says about the SKY130 lineage with one or two verbatim",
        "quotes and their location in the document, the auditor's report when",
        "one was read, the record's relationship tags, its public-sources",
        "inventory key when it has one, and related pages of this reference.",
        "A `Note:` line records a caveat, including a disagreement between",
        "this filing and another public source.",
        "",
        "## EDGAR access note",
        "",
        "`sec.gov` requires a contact address in the HTTP User-Agent header,",
        "which this project's checking tools do not send. Every EDGAR",
        "document below is therefore read from a Wayback Machine capture or a",
        "company investor-relations copy; the `sec.gov` link is kept as the",
        "canonical citation but was not itself fetched by this project.",
        "",
        "## Counts",
        "",
        "By company: " + ", ".join(
            f"{esc(check_filings.COMPANIES[k][0])} ({companies[k]})"
            for k in company_keys_in_order() if companies[k]) + ".",
        "",
        "By type: " + ", ".join(f"{esc(name)} ({types[name]})" for name, _ in DOCTYPE_GROUPS if types[name]) + ".",
        "",
        "By year: " + ", ".join(f"{y} ({years[y]})" for y in sorted(years)) + ".",
        "",
    ]
    body += gen_known_gaps(gaps)
    body += [
        "## All filings",
        "",
        "Sorted by filing date, then id.",
        "",
    ]
    for r in rs:
        body += entry_lines(r)
    return page("filings-index", "Financial and corporate filings index", body)


def gen_by_company(rs: list[dict]) -> str:
    body = [
        "Filings grouped by filer: the lineage companies first (Cypress,",
        "SkyWater, Infineon), then the acquirer, customers and partners.",
        "Within a company, by filing date. Each line links the full entry on",
        "{ref}`filings-index`.",
        "",
    ]
    for heading, keys in COMPANY_GROUPS:
        items = [r for r in rs if r["company_key"] in keys]
        if not items:
            continue
        body += [f"## {esc(heading)}", ""] + [short_line(r) for r in items] + [""]
    return page("filings-by-company", "Filings by company", body)


def gen_by_year(rs: list[dict]) -> str:
    body = [
        "Filings by year of filing, newest first. For most records `filed` is the",
        "EDGAR filing date; for some annual reports to shareholders and German annual",
        "reports it is instead the latest signature or auditor's-report date printed",
        "in the copy (each such record's `Note:` on {ref}`filings-index` says so), so",
        "a handful of records are grouped by that date rather than a true filing date.",
        "",
    ]
    for y in sorted({r["filed"].year for r in rs}, reverse=True):
        items = [r for r in rs if r["filed"].year == y]
        body += [f"(filings-year-{y})=", f"## {y}", ""] + [short_line(r) for r in items] + [""]
    return page("filings-by-year", "Filings by year", body)


def gen_by_type(rs: list[dict]) -> str:
    body = [
        "Filings by type of document. Annual reports repeat their auditor's",
        "name and date; the full audit reports are collected on",
        "{ref}`filings-audits`.",
        "",
    ]
    for heading, types in DOCTYPE_GROUPS:
        items = [r for r in rs if r["document_type"] in types]
        if not items:
            continue
        body += [f"## {esc(heading)}", ""]
        for r in items:
            extra = ""
            aud = r.get("auditor_report")
            if aud:
                extra = f" (auditor: {esc(aud['firm'])}, {aud['date']})"
            body.append(short_line(r) + extra)
        body.append("")
    return page("filings-by-type", "Filings by document type", body)


def gen_by_relationship(rs: list[dict]) -> str:
    body = [
        "Filings grouped by relationship tag; a filing can carry several",
        "tags. Each section is headed by the tag's definition. Each line",
        "links the full entry on {ref}`filings-index`.",
        "",
    ]
    covered = {t for _, tags in REL_GROUPS for t in tags}
    missing = set(check_filings.RELATIONSHIPS) - covered
    if missing:
        raise SystemExit(f"relationship tags not covered by REL_GROUPS: {sorted(missing)}")
    for heading, tags in REL_GROUPS:
        body += [f"## {esc(heading)}", ""]
        for t in tags:
            items = [r for r in rs if t in r["relationships"]]
            body += [f"({rel_label(t)})=", f"### {esc(check_filings.RELATIONSHIPS[t])}", ""]
            if items:
                body += [short_line(r) for r in items] + [""]
            else:
                body += ["No filings yet.", ""]
    return page("filings-by-relationship", "Filings by relationship", body)


def gen_audits(rs: list[dict]) -> str:
    body = [
        "The auditor's reports found in the filings below, in filing order.",
        "",
        "Only the firm, subject and report date are recorded (V-09):",
        "the schema has no field for opinion type, so this page cannot say",
        "whether an opinion was unqualified, dual-dated or carried a",
        "going-concern paragraph -- read the quoted signature block on the",
        "filing's own entry for that.",
        "",
        "| Filing | Firm | Subject | Report date |",
        "|---|---|---|---|",
    ]
    items = [r for r in rs if r.get("auditor_report")]
    for r in items:
        aud = r["auditor_report"]
        body.append(f"| {{ref}}`{esc(r['company'])}, {r['filed']} <filing-{r['id']}>` | {esc(aud['firm'])} | "
                    f"{esc(aud['subject'])} | {aud['date']} |")
    body.append("")
    return page("filings-audits", "Auditor's reports", body)


def generate() -> dict[str, str]:
    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("filings"), list):
        raise SystemExit(f"{DATA}: top level must be a mapping with a 'filings' list")
    rs = data["filings"]
    gaps = data.get("known_gaps") or []
    return {
        "index.md": gen_index(rs, gaps),
        "by-company.md": gen_by_company(rs),
        "by-year.md": gen_by_year(rs),
        "by-type.md": gen_by_type(rs),
        "by-relationship.md": gen_by_relationship(rs),
        "audits.md": gen_audits(rs),
    }


def check_dataset() -> None:
    result = subprocess.run(["uv", "run", "tools/check_filings.py"], cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise SystemExit("data/filings.yaml fails tools/check_filings.py; fix it before generating pages")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="fail if committed pages differ from the generated ones")
    args = ap.parse_args()
    check_dataset()
    pages = generate()
    problems: list[str] = []
    if args.check:
        for name, text in pages.items():
            p = OUT / name
            if not p.exists():
                problems.append(f"{p.relative_to(ROOT)}: missing")
            elif p.read_text(encoding="utf-8") != text:
                problems.append(f"{p.relative_to(ROOT)}: differs from generated output")
        if OUT.is_dir():
            for p in sorted(OUT.iterdir()):
                if p.name not in pages:
                    problems.append(f"{p.relative_to(ROOT)}: not generated by tools/gen_filings.py")
    else:
        OUT.mkdir(parents=True, exist_ok=True)
        for name, text in pages.items():
            (OUT / name).write_text(text, encoding="utf-8")
    for p in problems:
        print(p)
    verb = "checked" if args.check else "written"
    print(f"{plural(len(pages), 'page')} {verb}, {plural(len(problems), 'problem')}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
