#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Generate the patent index pages from ``data/patents.yaml``.

Writes ``docs/references/patents/``:

* ``index.md`` — scope, the legal caveat, how families and members are
  counted, the relation legend, counts by status, and links to the
  other views;
* ``families.md`` — the canonical entry for every family, in priority
  order, one per label ``patent-gp<google family id>``; the other pages
  link to these entries instead of repeating them;
* ``by-module.md`` — grouped by process module, in process order, using
  the module table on {ref}`overview-modules`, plus separate sections
  for the sky130B ReRAM module, equipment and metrology, materials, and
  process-wide or category pages;
* ``by-assignee.md`` — grouped by original assignee, Cypress
  Semiconductor, SkyWater Technology and Infineon Technologies first;
* ``by-jurisdiction.md`` — one table per country/office, plus a
  family-size table (members per family);
* ``by-date.md`` — by decade of priority date, and a status section
  (expired, in force, unknown).

A family whose ``expired`` is ``false`` or ``unknown`` is written on
``families.md`` as a collapsed ``{dropdown}`` block whose title shows
only the representative's publication number and its status; other
pages then only name and link the family, never repeating its status
or dates outside the collapsed entry.

The pages are overwritten; do not edit them by hand. Before generating,
the dataset must pass ``tools/check_patents.py``.

``--check`` generates into memory and fails if a committed page differs,
or if a page in the directory was not generated.

Run with ``uv run tools/gen_patents.py [--check]``. See
``docs/plans/patent-index-design.md``.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "patents.yaml"
OUT = ROOT / "docs" / "references" / "patents"
HEADER = "<!-- Generated from data/patents.yaml by tools/gen_patents.py; do not edit. -->\n"

sys.path.insert(0, str(ROOT / "tools"))
import check_patents  # noqa: E402

RELATION_NAME = {
    "cited-on-page": "cited on this page",
    "same-lineage-assignee": "same-lineage assignee",
    "technique-class": "technique class",
}
RELATION_TEXT = {
    "cited-on-page": "the page cites a member of this family.",
    "same-lineage-assignee": "the original assignee is in the process lineage (Cypress Semiconductor, "
                              "SkyWater Technology, or Infineon Technologies for patents that came from "
                              "Cypress); this is not evidence that SKY130 uses the technique.",
    "technique-class": "the family describes the class of technique the page covers, without a citation "
                        "on that page.",
}

# Process modules in step order, from the table at (overview-modules)= on
# docs/overview/index.md. Each entry is (slug, heading, first step, last step).
STEP_MODULES = [
    ("substrate-isolation-dnwell", "Starting material, isolation and deep N-well", 1, 13),
    ("wells", "Wells and threshold implants", 14, 34),
    ("sonos", "SONOS tunnel window and ONO stack", 35, 42),
    ("gate-oxides", "Gate oxides", 43, 47),
    ("poly", "Poly gate and poly resistors", 48, 63),
    ("tips-halos", "Tips and halos", 64, 75),
    ("spacers-sd", "Spacers and source/drain", 76, 88),
    ("psg-li", "Pre-metal dielectric, contact silicide and local interconnect", 89, 106),
    ("contact-m1", "Metal contact and metal 1", 107, 117),
    ("via1-m2-via2", "Via 1, metal 2 and via 2", 118, 134),
    ("mim1-m3-via3", "First MiM capacitor, metal 3 and via 3", 135, 148),
    ("m4-mim2-via4-m5", "Metal 4, second MiM capacitor, via 4 and metal 5", 149, 163),
    ("passivation", "Passivation, pads, alloy and test", 164, 171),
]
STEP_RE = re.compile(r"^step-(\d+)$")

JURISDICTIONS = [
    ("US", "United States"), ("EP", "European Patent Office"), ("WO", "WIPO (PCT)"),
    ("JP", "Japan"), ("CN", "China"), ("KR", "South Korea"), ("TW", "Taiwan"),
    ("DE", "Germany"), ("GB", "United Kingdom"), ("FR", "France"),
]
# Other ISO 3166-1 alpha-2 codes seen in the dataset's members, for a
# readable "others" section heading; a code not listed here falls back
# to the bare code (still correct, just less readable).
OTHER_COUNTRY_NAMES = {
    "AT": "Austria", "AU": "Australia", "BE": "Belgium", "BR": "Brazil", "CA": "Canada",
    "CH": "Switzerland", "DK": "Denmark", "ES": "Spain", "FI": "Finland", "GR": "Greece",
    "HK": "Hong Kong", "IE": "Ireland", "IL": "Israel", "IN": "India", "IT": "Italy",
    "LU": "Luxembourg", "MX": "Mexico", "MY": "Malaysia", "NL": "Netherlands",
    "NO": "Norway", "NZ": "New Zealand", "PT": "Portugal", "RU": "Russia",
    "SE": "Sweden", "SG": "Singapore", "YU": "Yugoslavia (historical)", "ZA": "South Africa",
}

_ESC = re.compile(r"([\\`*_\[\]<>|#${}])")


def esc(text: object) -> str:
    return _ESC.sub(r"\\\1", " ".join(str(text).split()))


IRREGULAR_PLURAL = {"family": "families"}


def plural(n: int, word: str) -> str:
    if n == 1:
        return f"{n} {word}"
    return f"{n} {IRREGULAR_PLURAL.get(word, word + 's')}"


def label_of(fam: dict) -> str:
    return f"patent-{fam['id'].lower()}"


def display_pn(m: dict) -> str:
    """Format a member's publication number for display, following the
    conventions ``tools/check_patents.py``'s ``number_forms`` already
    recognises in docs text: comma-grouped for a US granted-patent-style
    number, ``YYYY/NNNNNNN`` for a US 11-digit pre-grant application
    number, space-grouped for a 7-digit EP number, and left as published
    digits (no grouping) for every other jurisdiction, whose numbering
    is not a plain sequential count."""
    cc = m["country"]
    kind = m.get("kind") or ""
    num = m["number"][len(cc):]
    if kind and num.endswith(kind):
        num = num[: -len(kind)]
    if num.isdigit():
        if cc == "US" and len(num) == 11:
            num = f"{num[:4]}/{num[4:]}"
        elif cc == "US":
            num = f"{int(num):,}"
        elif cc == "EP" and len(num) == 7:
            num = f"{num[0]} {num[1:4]} {num[4:]}"
    return f"{cc} {num}" + (f" {kind}" if kind else "")


def rep_member(fam: dict) -> dict:
    return next(m for m in fam["members"] if m["number"] == fam["representative"])


def dropdown_title(fam: dict) -> str:
    pn = display_pn(rep_member(fam))
    status = fam["legal_status"]["status"]
    exp = fam["expiry"]["date"]
    if fam["expired"] is False:
        return f"{pn} — shown as in force; estimated expiry {exp}"
    return f"{pn} — legal status shown as {esc(status)}; expiry not fully bounded from the records " \
           f"retrieved, estimated no later than {exp}"


def status_word(fam: dict) -> str:
    if fam["expired"] is True:
        return "expired"
    if fam["expired"] is False:
        return "in force"
    return "unknown"


def members_table(fam: dict) -> list[str]:
    rows = ["| Number | Type | Publication date | Status | Verified | Links |",
            "|---|---|---|---|---|---|"]
    for m in fam["members"]:
        title = f" \"{esc(m['title'])}\"" if m.get("title") and m["title"] != fam["title"] else ""
        note = f" ({esc(m['note'])})" if m.get("note") else ""
        pn = display_pn(m) + title + note
        typ = m["document_type"].replace("-", " ")
        pub = m.get("publication_date") or "—"
        status = esc(m.get("status")) if m.get("status") else "not shown"
        verified = esc(m["verified"])
        links = f"[Espacenet]({m['links']['espacenet']}) · [Google Patents]({m['links']['google_patents']})"
        for name, u in m["links"].items():
            if name not in ("espacenet", "google_patents"):
                links += f" · [{esc(name)}]({u})"
        rows.append(f"| {esc(pn)} | {esc(typ)} | {pub} | {status} | {verified} | {links} |")
    return rows


def relevance_lines(fam: dict) -> list[str]:
    # L12: several relevance entries often share one relation and reason
    # word-for-word (the same explanation applies to every step of a
    # module, say) — group them onto one bullet with every target linked,
    # in the order each (relation, reason) pair first appears, instead of
    # repeating the sentence once per target.
    groups: dict[tuple[str, str], list[str]] = {}
    for r in fam["relevance"]:
        groups.setdefault((r["relation"], r["reason"]), []).append(r["target"])
    out = []
    for (relation, reason), targets in groups.items():
        refs = ", ".join(f"{{ref}}`{t}`" for t in targets)
        out.append(f"* {refs} — *{RELATION_NAME[relation]}*: {esc(reason)}")
    return out


def family_body(fam: dict) -> list[str]:
    # Each field is its own paragraph: CommonMark folds consecutive text
    # lines with no blank line between them into one paragraph, so every
    # field line is followed by a blank line (M7) rather than joined into
    # a run-on paragraph.
    fields = [f"**Title:** {esc(fam['title'])}"]
    ass = fam["assignees"]
    fields.append("**Assignees:** original " + "; ".join(esc(a) for a in ass["original"])
                  + ("; current " + "; ".join(esc(a) for a in ass["current"]) if ass["current"] else ""))
    if fam.get("inventors"):
        fields.append("**Inventors:** " + "; ".join(esc(i) for i in fam["inventors"]))
    d = fam["dates"]
    dates = f"priority {d['priority']}"
    if d.get("filing"):
        dates += f", filing {d['filing']}"
    if d.get("grant"):
        dates += f", grant {d['grant']}"
    fields.append(f"**Dates:** {dates}")
    fields.append(f"**Legal status (representative):** {esc(fam['legal_status']['status'])} "
                  f"({esc(fam['legal_status']['source'])})")
    fields.append(f"**Estimated expiry:** {fam['expiry']['date'] or 'not bounded'} — {esc(fam['expiry']['basis'])}")
    if fam["family"]["source"] == "Google Patents family ID":
        fields.append(f"**Google Patents family ID:** `{fam['family']['google_family_id']}` "
                      f"(family section of the representative's own record page, linked below)")
    else:
        fields.append(f"**Family ID:** `{fam['family']['google_family_id']}` ({esc(fam['family']['source'])})")
    body: list[str] = []
    for line in fields:
        body += [line, ""]
    body += ["**Members:**", ""] + members_table(fam)
    body += ["", "**Relevance:**", ""] + relevance_lines(fam)
    if fam.get("inventory_keys"):
        body.append("")
        body.append("**Inventory:** " + ", ".join(f"`{k}`" for k in fam["inventory_keys"]))
    body.append("")
    body.append(f"**Discovery:** {', '.join(fam['discovery'])} — {esc(fam.get('discovery_note', ''))}")
    if fam.get("notes"):
        body.append("")
        body.append("**Notes:**")
        for n in fam["notes"]:
            body.append(f"* {esc(n)}")
    body.append("")
    body.append(f"**Verified:** {esc(fam['verified'])}")
    return body


def family_entry(fam: dict) -> list[str]:
    """The canonical entry: a plain heading, or a collapsed dropdown for
    a family that is not shown as expired."""
    label = label_of(fam)
    if fam["expired"] is True:
        out = [f"({label})=", f"## {display_pn(rep_member(fam))} — {esc(fam['title'])}", ""]
        out += family_body(fam)
        out.append("")
        return out
    out = [f":::{{dropdown}} {dropdown_title(fam)}", f":name: {label}", ""]
    out += family_body(fam)
    out.append(":::")
    out.append("")
    return out


def family_link_line(fam: dict) -> str:
    """A one-line reference used on the grouped pages: title and link for an
    expired family, number and status only (no repeated details) otherwise."""
    label = label_of(fam)
    pn = display_pn(rep_member(fam))
    if fam["expired"] is True:
        return f"* {{ref}}`{pn} <{label}>` — {esc(fam['title'])} ({fam['dates']['priority']})"
    return f"* {{ref}}`{pn} <{label}>` — {esc(status_word(fam))}"


def page(label: str, title: str, body: list[str]) -> str:
    return HEADER + "\n" + f"({label})=\n# {title}\n\n" + "\n".join(body).rstrip() + "\n"


CAVEAT = [
    "Statuses, dates and estimated expiries are as shown by the public",
    "databases (Google Patents, using IFI Claims legal-status and expiry",
    "data) on the retrieval date named on this page. They are not a legal",
    "opinion and are not exhaustive: maintenance-fee lapses, terminal",
    "disclaimers, patent term extensions, oppositions, reissues and the",
    "national validations of a European patent are not fully captured. A US",
    "patent lapsed for non-payment of a maintenance fee can be reinstated on",
    "a petition showing the delay was unintentional, within statutory time",
    "limits that depend on which fee was missed (37 CFR 1.378(a)/(c),",
    "Cornell LII, https://www.law.cornell.edu/cfr/text/37/1.378); a family",
    "shown as expired solely on the strength of a fee lapse, while its term",
    "has not otherwise run, says so in its notes.",
    "Before relying on the status of any family, check the linked",
    "official record.",
]


VERIFIED_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")


def scope_and_completeness(fams: list[dict]) -> list[str]:
    """H1 (round-1 review): state plainly how the index was built and that
    it is not a exhaustive worldwide search, instead of leaving the
    landing page reading as if it were."""
    n = len(fams)
    discovery_counts = Counter(d for f in fams for d in f["discovery"])
    seed_only = sum(1 for f in fams if f["discovery"] == ["cited-in-docs"])
    assignees = Counter(a.casefold() for f in fams for a in f["assignees"]["original"])
    cypress = sum(v for k, v in assignees.items() if "cypress" in k)
    skywater = sum(v for k, v in assignees.items() if "skywater" in k)
    infineon = sum(v for k, v in assignees.items() if "infineon" in k)
    def count_families(n: int, label: str) -> str:
        return f"{n} {label} {'family' if n == 1 else 'families'}"

    skywater_clause = "no SkyWater Technology family" if skywater == 0 else f"only {count_families(skywater, 'SkyWater Technology')}"
    return [
        f"This index began as every patent already cited on a docs page ({plural(seed_only, 'family')} "
        "of the total entered this way and no other), then widened by following each seed's Google "
        "Patents family table and citation lists, by a handful of assignee+keyword searches for "
        "specific process modules, and by an `assignee=\"Weebit Nano\"` search once ReRAM was brought "
        "into scope. It is **not** the result of an exhaustive, systematic sweep of every process "
        "module against every lineage assignee: an independent review of this dataset during its "
        "construction found at least a dozen absent Cypress/"
        "Infineon families from just three more searches, named six process modules never searched at "
        f"all, and notes that the index holds {count_families(cypress, 'Cypress Semiconductor')} and "
        f"{count_families(infineon, 'Infineon Technologies')} but {skywater_clause}, though SkyWater is "
        "named in this index's own scope. Treat this index as a starting point for the SKY130/Cypress/"
        "SkyWater/Infineon patent landscape, not as proof that a family absent from it does not exist.",
        "",
        f"Discovery methods recorded across the {plural(n, 'family')}: "
        + "; ".join(f"{plural(v, 'family')} `{k}`" for k, v in
                     sorted(discovery_counts.items(), key=lambda kv: -kv[1]))
        + ". A family can carry more than one method (reached more than one way), so these do not sum "
        "to the family count.",
        "",
        "A systematic assignee sweep of USPTO Patent Public Search on 2026-09-19 (Cypress Semiconductor, "
        "SkyWater Technology, Longitude Flash Memory Solutions, Infineon Technologies LLC, Spansion, "
        "Ramtron, Weebit Nano, restricted to process-module title keywords, run because Google Patents "
        "was unreachable that day) found 211 distinct families: 39 were already in this index and 24 "
        "were added (the ones whose family ID is a USPTO Patent Public Search identifier rather than a "
        "Google Patents one). That leaves **136 identified, in-scope families this index does not yet "
        "contain** -- mostly a large Spansion estate that needs the same per-family lineage reasoning as "
        "the two Spansion families already added, plus a number of Weebit Nano hits not yet triaged "
        "individually. The full sweep, every family's triage decision and the reason for each are "
        "recorded in the repository at `docs/plans/patent-discovery-log.md` (outside the built "
        "site).",
    ]


def gen_index(fams: list[dict], retrieved: str) -> str:
    n = len(fams)
    nmembers = sum(len(f["members"]) for f in fams)
    status = Counter(status_word(f) for f in fams)
    google_fetched = sum(1 for f in fams for m in f["members"] if "record page fetched" in m["verified"])
    ppubs_fetched = sum(1 for f in fams for m in f["members"]
                         if "USPTO Patent Public Search record" in m["verified"])
    fetched = google_fetched + ppubs_fetched
    ppubs_fams = [f for f in fams if f["family"]["source"] != "Google Patents family ID"]
    verified_dates = sorted({
        m2.group(1) for f in fams
        for v in [f["verified"]] + [m["verified"] for m in f["members"]]
        if (m2 := VERIFIED_DATE_RE.match(v))
    })
    when = verified_dates[0] if len(verified_dates) == 1 else f"{verified_dates[0]} to {verified_dates[-1]}"
    listed = nmembers - fetched
    fams_with_listed = [
        f for f in fams
        if any("record page fetched" not in m["verified"]
               and "USPTO Patent Public Search record" not in m["verified"]
               for m in f["members"])
    ]
    fams_listed_expired = [f for f in fams_with_listed if f["expired"] is True]
    fams_listed_not_expired = [f for f in fams_with_listed if f["expired"] is not True]
    listed_in_expired = sum(
        1 for f in fams_listed_expired for m in f["members"]
        if "record page fetched" not in m["verified"]
        and "USPTO Patent Public Search record" not in m["verified"])
    listed_not_expired = listed - listed_in_expired
    ppubs_clause = (
        [f" Separately, {len(ppubs_fams)} of the {plural(n, 'family')} in this index",
         "rest on USPTO Patent Public Search instead of Google Patents, which stayed unreachable while",
         "they were found (see \"PPUBS fallback\" in `docs/plans/patent-index-design.md`); each says so",
         "in its own *Legal status* and *Verified* lines, carries no legal status or adjusted-expiration",
         "date, and enumerates only the single member PPUBS's own search returned, not a complete family.",
         "Its expiry is a term-arithmetic bound, conservative for the collapse decision (a family is not",
         "shown expired unless that bound has already passed with no possible US patent term adjustment)",
         "but not necessarily an upper bound on the true date: PPUBS does not report a term adjustment a",
         "still-collapsed family's real term may already include."]
        if ppubs_fams else []
    )
    fetched_note = (
        [f"record page was fetched; {fetched} of the {nmembers} members have their own record page",
         f"fetched ({google_fetched} from Google Patents, {ppubs_fetched} from USPTO Patent Public",
         "Search).", f"The remaining {listed} are listed in the fetched Google Patents family table of",
         "their representative but were not fetched separately: a",
         "time-budgeted departure from this index's rule of fetching every",
         "member of a family whose earliest priority is on or after",
         "1999-05-29, recorded as an exception in",
         "`docs/plans/patent-index-design.md`'s \"Verification levels\". Each",
         "such row carries its publication number, country, kind and",
         "publication date from the representative's own family table, says",
         "so in its *Verified* column, and shows no status. "
         f"{plural(listed_in_expired, 'member')} of these sit in "
         f"{plural(len(fams_listed_expired), 'family')} already shown expired "
         f"on other grounds; the remaining {plural(listed_not_expired, 'member')}, in "
         f"{plural(len(fams_listed_not_expired), 'family')} **not** shown expired, are each bounded",
         "conservatively (the family's earliest priority date + 21 years)",
         "rather than assumed ended, per the design's rule 3.",
         *ppubs_clause]
        if fetched < nmembers else
        [f"record page was fetched, and so has every one of the {nmembers} members.", *ppubs_clause]
    )
    body = [
        "A worldwide index of patents and published applications related to",
        "the SKY130 process technology and its lineage (Cypress",
        "Semiconductor, SkyWater Technology and Infineon Technologies, and",
        "suppliers' patents that a docs page already cites or that a public",
        "source ties to this process lineage), generated from one curated",
        "dataset, `data/patents.yaml`. The unit of record is the patent",
        "**family as grouped by Google Patents**: its family ID, the",
        "representative record page, and its other publications and",
        "applications (the family's *Publications* and *Also Published As*",
        "tables). This is close to, but not the same as, an EPO DOCDB simple",
        "family or an INPADOC extended family. Each member's Espacenet link",
        "is a search query for its own number, not a direct record link (the",
        "Espacenet web interface does not accept scripted retrieval); Google",
        "Patents' own record page, linked alongside it, is the working",
        "full-text link this index relies on for every member.",
        "",
        f"Records were retrieved {when} (individual records carry their own",
        f"`verified` date). The index holds {plural(n, 'family')} "
        f"({plural(nmembers, 'member')} in total). Every family's representative",
        *fetched_note,
        "",
        "## Legal caveat",
        "",
        *CAVEAT,
        "",
        "## Unexpired and unknown-status families are collapsed",
        "",
        "A family shown as in force, or whose expiry could not be bounded",
        "from the records retrieved (`unknown`), appears on {ref}`patents-families`",
        "as a collapsed block whose title shows only the representative's",
        "publication number and its status; open it to see the rest. A",
        "family shown as expired is written out in full. The grouped pages",
        "below never repeat a collapsed family's status or dates outside the",
        "collapsed entry.",
        "",
        "## Relations",
        "",
        "Each family links to one or more pages of this reference, with a",
        "relation:",
        "",
    ]
    for rel, text in RELATION_TEXT.items():
        body.append(f"* **{RELATION_NAME[rel]}** (`{rel}`) — {text}")
    body += [
        "",
        "## Counts",
        "",
        "| | Families | Members |",
        "|---|---|---|",
        f"| Total | {n} | {nmembers} |",
        f"| Shown as expired | {status['expired']} | "
        f"{sum(len(f['members']) for f in fams if status_word(f) == 'expired')} |",
        f"| Shown as in force | {status['in force']} | "
        f"{sum(len(f['members']) for f in fams if status_word(f) == 'in force')} |",
        f"| Status unknown | {status['unknown']} | "
        f"{sum(len(f['members']) for f in fams if status_word(f) == 'unknown')} |",
        "",
        "## Scope and completeness",
        "",
        *scope_and_completeness(fams),
        "",
        "## Other views",
        "",
        "* {ref}`patents-families` — the canonical entry for every family, in priority-date order.",
        "* {ref}`patents-by-module` — grouped by process module.",
        "* {ref}`patents-by-assignee` — grouped by original assignee.",
        "* {ref}`patents-by-jurisdiction` — grouped by country or office, and by family size.",
        "* {ref}`patents-by-date` — grouped by decade of priority date, and by status.",
        "",
        "```{toctree}",
        ":hidden:",
        "",
        "families",
        "by-module",
        "by-assignee",
        "by-jurisdiction",
        "by-date",
        "```",
    ]
    return page("patents-index", "Patent index", body)


def gen_families(fams: list[dict]) -> str:
    body = [
        "The canonical entry for every family, sorted by priority date. Other",
        "pages of this index link here instead of repeating an entry.",
        "See {ref}`patents-index` for the scope, the legal caveat and how",
        "families and members are counted.",
        "",
    ]
    for f in fams:
        body += family_entry(f)
    return page("patents-families", "Patent families", body)


def module_of(target: str) -> str | None:
    m = STEP_RE.match(target)
    if not m:
        return None
    n = int(m.group(1))
    for slug, _heading, lo, hi in STEP_MODULES:
        if lo <= n <= hi:
            return slug
    return None


def gen_by_module(fams: list[dict]) -> str:
    body = [
        "Families grouped by the process module their relevance targets",
        "belong to, in process order, using the module table at",
        "{ref}`overview-modules`. A family with relevance targets in several",
        "modules appears under each. Targets that are not a single step page",
        "(category, mask, machine, material and overview pages) are grouped",
        "afterwards. A family appears once per group even if several of its",
        "relevance entries point into that group's targets.",
        "",
    ]
    by_slug: dict[str, list[dict]] = defaultdict(list)
    reram, equipment, materials, crosscutting = [], [], [], []
    for f in fams:
        slugs_here = set()
        for r in f["relevance"]:
            t = r["target"]
            slug = module_of(t)
            if slug:
                slugs_here.add(slug)
            elif t == "overview-sky130b-reram":
                slugs_here.add("__reram__")
            elif t.startswith("machine-") or t == "machines-index":
                slugs_here.add("__equipment__")
            elif t.startswith("material-") or t == "materials-index":
                slugs_here.add("__materials__")
            else:
                slugs_here.add("__crosscutting__")
        for slug in slugs_here:
            if slug == "__reram__":
                reram.append(f)
            elif slug == "__equipment__":
                equipment.append(f)
            elif slug == "__materials__":
                materials.append(f)
            elif slug == "__crosscutting__":
                crosscutting.append(f)
            else:
                by_slug[slug].append(f)
    for slug, heading, lo, hi in STEP_MODULES:
        items = by_slug.get(slug, [])
        if not items:
            continue
        body += [f"## {heading}", "", f"Steps {lo}–{hi}.", ""]
        body += [family_link_line(f) for f in sorted(items, key=lambda f: str(f["dates"]["priority"]))]
        body.append("")
    if reram:
        body += ["## sky130B ReRAM module", ""]
        body += [family_link_line(f) for f in sorted(reram, key=lambda f: str(f["dates"]["priority"]))]
        body.append("")
    if equipment:
        body += ["## Equipment and metrology", ""]
        body += [family_link_line(f) for f in sorted(equipment, key=lambda f: str(f["dates"]["priority"]))]
        body.append("")
    if materials:
        body += ["## Materials", ""]
        body += [family_link_line(f) for f in sorted(materials, key=lambda f: str(f["dates"]["priority"]))]
        body.append("")
    if crosscutting:
        body += ["## Process-wide and category pages", "",
                 "Families whose relevance targets are category, mask or overview pages",
                 "that are not specific to one step.", ""]
        body += [family_link_line(f) for f in sorted(crosscutting, key=lambda f: str(f["dates"]["priority"]))]
        body.append("")
    return page("patents-by-module", "Patents by process module", body)


LINEAGE_FIRST = ["cypress semiconductor", "skywater technology", "infineon technologies"]


def assignee_sort_key(name: str) -> tuple:
    n = name.casefold()
    for i, pref in enumerate(LINEAGE_FIRST):
        if pref in n:
            return (0, i, n)
    return (1, 0, n)


def assignee_group_key(name: str) -> str:
    """Comparison key for grouping equivalent assignee spellings that
    differ only by a trailing full stop or by letter case (round-4 N1):
    a non-Google source (PPUBS) does not follow Google Patents' own
    abbreviation conventions ("Corp" vs "Corporation", "Ltd" vs
    "Ltd."), so two spellings of the same company can otherwise split
    into two headings on ``by-assignee.md``."""
    return re.sub(r"\.$", "", name.strip()).casefold()


def assignee_canonical(variants: dict[str, list]) -> str:
    """Pick one display spelling among the raw strings grouped under one
    ``assignee_group_key``: prefer the spelling used by the most
    families, then one that does not end in a full stop, then the
    alphabetically first."""
    return min(variants, key=lambda v: (-len(variants[v]), v.endswith("."), v))


def gen_by_assignee(fams: list[dict]) -> str:
    body = [
        "Families grouped by original assignee, as shown by Google Patents",
        "or, for a PPUBS-sourced family, by USPTO Patent Public Search",
        "(its caveat applies: the lists \"may be inaccurate\"). Two spellings",
        "of one company that differ only by a trailing full stop or by",
        "letter case (a non-Google source's own convention, not Google's)",
        "are grouped under a single heading, in the spelling used by the",
        "most families; the section below on the family's own page still",
        "gives the literal spelling that source shows. Cypress",
        "Semiconductor, SkyWater Technology and Infineon Technologies come",
        "first; a family with several original assignees appears under each.",
        "The current assignee, where different, is shown alongside. Google's",
        "\"original assignee\" is sometimes the entity's current, renamed name",
        "rather than the name on the published document itself (five cases",
        "found by the round-1 review's cross-check against EPO data); a",
        "heading here is not necessarily the name printed on the patent.",
        "",
    ]
    by_key: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for f in fams:
        for a in f["assignees"]["original"]:
            by_key[assignee_group_key(a)][a].append(f)
    for key in sorted(by_key, key=lambda k: assignee_sort_key(assignee_canonical(by_key[k]))):
        variants = by_key[key]
        name = assignee_canonical(variants)
        items = [f for vs in variants.values() for f in vs]
        current_keys = {assignee_group_key(c): c for f in items for c in f["assignees"]["current"]}
        current_keys.pop(key, None)
        currents = sorted(current_keys.values())
        if name == "Individual":
            # L9: Google's placeholder for "no assignee recorded at grant",
            # not a single entity that became several — read as such.
            heading = "No assignee recorded at grant (Google Patents \"Individual\")"
        else:
            heading = esc(name)
            if currents:
                heading += " (now " + ", ".join(esc(c) for c in currents) + ")"
        body += [f"## {heading}", ""]
        body += [family_link_line(f) for f in sorted(items, key=lambda f: str(f["dates"]["priority"]))]
        body.append("")
    return page("patents-by-assignee", "Patents by assignee", body)


def gen_by_jurisdiction(fams: list[dict]) -> str:
    body = [
        "Every member publication of a family shown as expired, plus one",
        "representative row for each other family, grouped by its country",
        "or office, plus a family-size table (members per family). A family",
        "can have members in several jurisdictions and so appears in",
        "several tables. A family shown as in force or unknown is collapsed",
        "on {ref}`patents-families`; here, as on the other grouped pages, it",
        "contributes only its representative's own row (number and status",
        "word), not its full member list — open the collapsed entry for the",
        "rest. Each section's row count below reflects this: it is not a",
        "count of every member publication in that jurisdiction.",
        "",
    ]
    by_cc: dict[str, list[tuple[dict, dict]]] = defaultdict(list)
    for f in fams:
        if f["expired"] is not True:
            rep = rep_member(f)
            by_cc[rep["country"]].append((rep, f))
            continue
        for m in f["members"]:
            by_cc[m["country"]].append((m, f))
    seen_codes = {cc for cc, _ in JURISDICTIONS}
    others = sorted(set(by_cc) - seen_codes)
    for cc, name in JURISDICTIONS + [(c, OTHER_COUNTRY_NAMES.get(c, c)) for c in others]:
        items = by_cc.get(cc)
        if not items:
            continue
        body += [f"## {esc(name)} ({cc})", "",
                 f"{plural(len(items), 'row')}: every member of a family shown as expired, plus "
                 "one representative row for each collapsed family.", "",
                 "| Number | Family | Status |", "|---|---|---|"]
        for m, f in sorted(items, key=lambda x: (str(x[0].get("publication_date") or ""), x[0]["number"])):
            fam_pn = display_pn(rep_member(f))
            if f["expired"] is not True:
                status = esc(status_word(f))
            else:
                status = esc(m.get("status")) if m.get("status") else "not shown"
            body.append(f"| {esc(display_pn(m))} | {{ref}}`{fam_pn} <{label_of(f)}>` | {status} |")
        body.append("")
    sizes = Counter(len(f["members"]) for f in fams)
    body += ["## Family size", "", "Number of members recorded per family.", "",
             "| Members | Families |", "|---|---|"]
    for size in sorted(sizes):
        body.append(f"| {size} | {sizes[size]} |")
    body.append("")
    return page("patents-by-jurisdiction", "Patents by jurisdiction", body)


def decade_of(iso_date: str) -> str:
    y = int(str(iso_date)[:4])
    d = (y // 10) * 10
    return f"{d}s"


def gen_by_date(fams: list[dict]) -> str:
    body = [
        "Families grouped by decade of earliest priority date, oldest",
        "first, and then by status.",
        "",
    ]
    by_decade: dict[str, list[dict]] = defaultdict(list)
    for f in fams:
        by_decade[decade_of(f["dates"]["priority"])].append(f)
    for dec in sorted(by_decade):
        items = by_decade[dec]
        body += [f"## {dec}", ""]
        body += [family_link_line(f) for f in sorted(items, key=lambda f: str(f["dates"]["priority"]))]
        body.append("")
    body += ["## By status", ""]
    for word, heading in (("expired", "Shown as expired"), ("in force", "Shown as in force"),
                          ("unknown", "Status unknown")):
        items = [f for f in fams if status_word(f) == word]
        body += [f"### {heading}", ""]
        body += [family_link_line(f) for f in sorted(items, key=lambda f: str(f["dates"]["priority"]))]
        body.append("")
    return page("patents-by-date", "Patents by date and status", body)


OVERVIEW_MODULE_ROW = re.compile(
    r"^\|\s*(?P<name>[^|]+?)\s*\|\s*\{ref\}`[^<]*<step-(?P<lo>\d+)>`\s*[–-]\s*\{ref\}`[^<]*<step-(?P<hi>\d+)>`")


def check_step_modules() -> None:
    """L8: STEP_MODULES hard-codes the module boundaries and headings from
    the table at {ref}`overview-modules` on docs/overview/index.md; fail
    loudly if that table is ever edited without updating this copy, rather
    than silently drifting out of sync."""
    text = (ROOT / "docs" / "overview" / "index.md").read_text(encoding="utf-8")
    label_at = text.index("(overview-modules)=")
    # the label is immediately followed by its own "## " heading; the
    # table runs from there to the *next* "## " heading.
    heading_at = text.index("\n## ", label_at) + 1
    rest = text[heading_at + 1:]
    end = heading_at + 1 + rest.index("\n## ") if "\n## " in rest else len(text)
    section = text[heading_at:end]
    rows = [OVERVIEW_MODULE_ROW.match(line) for line in section.splitlines()]
    rows = [m for m in rows if m]
    overview = [(m["name"], int(m["lo"]), int(m["hi"])) for m in rows]
    ours = [(heading, lo, hi) for _slug, heading, lo, hi in STEP_MODULES]
    if overview != ours:
        raise SystemExit(
            "tools/gen_patents.py STEP_MODULES no longer matches the module table at "
            "(overview-modules)= on docs/overview/index.md (L8). Overview table:\n"
            + "\n".join(f"  {n!r} {lo}-{hi}" for n, lo, hi in overview)
            + "\nSTEP_MODULES:\n" + "\n".join(f"  {n!r} {lo}-{hi}" for n, lo, hi in ours))


def generate() -> tuple[dict[str, str], str]:
    check_step_modules()
    # check_patents.Loader keeps ISO dates as strings (like the checker does),
    # rather than yaml.safe_load's automatic datetime.date conversion.
    data = yaml.load(DATA.read_text(encoding="utf-8"), Loader=check_patents.Loader)
    if not isinstance(data, dict) or not isinstance(data.get("families"), list):
        raise SystemExit(f"{DATA}: not the expected schema")
    fams = data["families"]
    labels = check_patents.doc_labels()
    inventory = check_patents.inventory_entries()
    page_text: dict[Path, str] = {}
    problems: list[str] = []
    seen_numbers: dict[str, str] = {}
    for f in fams:
        fid = str(f.get("id"))
        for m in f.get("members") or []:
            pn = m.get("number") if isinstance(m, dict) else None
            if pn in seen_numbers and seen_numbers[pn] != fid:
                problems.append(f"{fid}: {pn} also listed in {seen_numbers[pn]}")
            seen_numbers.setdefault(pn, fid)
        check_patents.check_family(f, labels, inventory, page_text, problems)
    if problems:
        print("\n".join(problems))
        raise SystemExit("data/patents.yaml fails tools/check_patents.py; fix it before generating pages")
    fams = sorted(fams, key=lambda f: (str(f["dates"]["priority"]), f["representative"]))
    retrieved = str(data["retrieved"])
    return {
        "index.md": gen_index(fams, retrieved),
        "families.md": gen_families(fams),
        "by-module.md": gen_by_module(fams),
        "by-assignee.md": gen_by_assignee(fams),
        "by-jurisdiction.md": gen_by_jurisdiction(fams),
        "by-date.md": gen_by_date(fams),
    }, retrieved


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="fail if committed pages differ from the generated ones")
    args = ap.parse_args()
    pages, _retrieved = generate()
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
                    problems.append(f"{p.relative_to(ROOT)}: not generated by tools/gen_patents.py")
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
