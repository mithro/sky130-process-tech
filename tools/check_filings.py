#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6", "pypdf>=4", "cryptography>=42"]
# ///
"""Check the financial and corporate filings dataset ``data/filings.yaml``.

The schema is described in ``docs/plans/filings-index-design.md``.  The
checker verifies, offline:

* **Schema.** Top-level ``schema_version`` (1), ``retrieved`` (a date) and
  ``filings`` (a list).  Every record has the required keys, in order,
  with the right types.
* **Identifiers.** Record ids are unique slugs; an SEC accession number
  has the form ``0001234567-YY-NNNNNN``, appears in one record only (per
  document) and matches the EDGAR folder of the record's ``sec.gov``
  URL; a ``parent`` names an existing record.
* **Dates.** ``filed``, ``period.start``/``period.end`` and the date that
  starts ``verified`` are ISO 8601 dates; a period does not end after
  the filing date unless the record says why (``period.note``).
* **Controlled lists.** ``company_key``, ``document_type``,
  ``jurisdiction``, ``regulator``, ``identifier.scheme``,
  ``relationships``, ``discovery`` and ``related_docs[].relation`` take
  values from the lists below.
* **URLs.** Every URL is ``https``; a Wayback URL has the shape
  ``https://web.archive.org/web/<14 digits>/<original>`` and its
  embedded original matches ``urls.original``; a record whose original is
  on ``sec.gov`` (EDGAR, which demands a contact in the User-Agent) also
  carries a Wayback or investor-relations copy that is not on
  ``sec.gov``; no e-mail address appears anywhere in a record.
* **Quotes.** ``about.quotes`` holds one or two short verbatim quotes
  (at most 400 characters each), each with a ``location``.
* **Cross-references.** Every ``related_docs`` label is defined in
  ``docs/`` as ``(label)=``; a ``cites`` relation requires the page to
  cite the record's inventory key as a footnote; every inventory key
  exists in ``docs/references/public-sources.md``.
* **Known gaps.** The optional top-level ``known_gaps`` list (filings
  known to exist but for which no non-``sec.gov`` copy could be found or
  read) has a ``company_key`` from the controlled list, a
  ``description`` and a ``reason`` ending with a full stop.

With ``--online`` it also fetches each record's Wayback or
investor-relations copy (never ``sec.gov``) with the project user agent
and confirms that every quote occurs in the document text (whitespace,
quotation marks and dashes normalised).  Online fetches are paced and
cached under ``tmp/filings-cache/``; a Wayback capture is cached forever
(its timestamp is in the URL), but any other copy is re-fetched once its
cache entry is more than ``CACHE_MAX_AGE_DAYS`` old (FIL-R1-11).

``location`` is checked (``check_location``) by whichever of these its
text names: an "ITEM N" caption, case-insensitive and with the full
sub-item number for an 8-K ("Item 4.01", not truncated to "Item 4"),
compared with the nearest preceding occurrence of a real Item heading
in the fetched text (a heading is one that starts a line -- a
table-of-contents run of closely-spaced items is dropped first, and an
inline "see Item 1A" cross-reference is excluded because it never
starts a line); a PDF page number ("page 12", checked against that
1-based page of the extracted PDF text); a position ("cover page",
"first page", "first paragraph", "second paragraph"); or, covering most
annual-report, exhibit and press-release locations that are none of the
above, a prose section heading named in the location text (compared
with the nearest preceding occurrence of that heading, again only one
that starts a line). An HTML document is flattened to text with a line
break at every block-level tag boundary (``<p>``, ``<div>``, ``<tr>``,
``<br>``, headings, list items, ...) precisely so a heading in HTML can
be recognised as starting a line the same way a PDF-extracted one does;
without that a heading-based check on an HTML filing always abstained.
A quote is located, for both the Item and the prose-heading checks, on
exactly the same fully normalised text (whitespace and hyphens
stripped, via ``normalise``) that the verbatim check uses -- not a
separate, whitespace-only search -- so a quote that already passed the
verbatim check can never fail to be located merely because of a
mid-word hyphen or line-wrap ``normalise`` already tolerates.

**Known limitation.** The prose-heading check (unlike the Item check,
where "Item N" values are enumerable and ordered) has no way to know
what the *correct* heading for a quote is; it only confirms that the
heading named in ``location`` occurs, heading-like, within
``HEADING_MAX_GAP`` characters and precedes the quote rather than
following it. A location naming the *wrong* heading, when that wrong
heading also happens to precede the quote within range, passes
silently -- this is a real gap, not a bug, and is not caught by any
check here. A location whose correct preceding heading cannot be
determined at all (heading absent, only mid-sentence, or too far away)
is reported as an abstention, never as a silent pass.

A location the checker cannot make sense of at all, or one it cannot
connect to text it can find, is not silently skipped: it is reported as
one line for every ``location`` it could not check (no Item/page/heading
found, the quote not locatable in the fetched copy, or nothing usable
precedes it -- V-13) and appends "P locations not checked" to the
summary, so a clean run never reads as "every location was verified" --
only as "no *checked* location was found wrong".

Run with ``--selftest`` to run the offline unit tests below and exit
(touches no files, makes no network request).
"""

from __future__ import annotations

import datetime as dt
import gzip
import hashlib
import html
import re
import io
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "filings.yaml"
DOCS = ROOT / "docs"
INVENTORY = DOCS / "references" / "public-sources.md"
CACHE = ROOT / "tmp" / "filings-cache"
USER_AGENT = "sky130-process-tech docs checker"

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ACCESSION_RE = re.compile(r"^\d{10}-\d{2}-\d{6}$")
VERIFIED_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}) \S.*$")
WAYBACK_RE = re.compile(r"^https://web\.archive\.org/web/(\d{14})/(https?://.+)$")
LABEL_RE = re.compile(r"^\(([A-Za-z0-9_-]+)\)=", re.M)
KEY_RE = re.compile(r"^\*\*([A-Z0-9][A-Z0-9_-]*)\*\*", re.M)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

# Filers.  "role" is the filer's relation to the SKY130 lineage.
COMPANIES = {
    "cypress": ("Cypress Semiconductor Corporation", "lineage"),
    "skywater": ("SkyWater Technology, Inc.", "lineage"),
    "infineon": ("Infineon Technologies AG", "lineage"),
    "d-wave": ("D-Wave Quantum Inc.", "customer"),
    "quicklogic": ("QuickLogic Corporation", "partner"),
    "weebit-nano": ("Weebit Nano Limited", "partner"),
    "ionq": ("IonQ, Inc.", "acquirer"),
    "other": ("(named in the record)", "other"),
}

DOCUMENT_TYPES = {
    "annual-report": "Annual report (10-K, 20-F, German annual report, ASX annual report)",
    "annual-report-amendment": "Amendment to an annual report (10-K/A)",
    "annual-report-to-shareholders": "Glossy annual report to shareholders wrapping a 10-K",
    "quarterly-report": "Quarterly report (10-Q) or quarterly statement",
    "quarterly-report-amendment": "Amendment to a quarterly report (10-Q/A)",
    "half-year-report": "Half-year financial report",
    "current-report": "Current report (8-K, 8-K/A)",
    "exhibit": "Exhibit filed with another filing",
    "registration-statement": "Registration statement (S-1, S-1/A, S-3, S-4)",
    "prospectus": "Prospectus (424B)",
    "proxy-statement": "Proxy statement (DEF 14A, DEFM14A)",
    "ad-hoc-announcement": "Ad-hoc announcement (Art. 17 MAR)",
    "market-announcement": "Stock-exchange market announcement",
    "deregistration": "Deregistration or termination of registration (15-12B)",
}

JURISDICTIONS = {"US", "DE", "AU"}
REGULATORS = {"SEC", "BaFin", "ASX"}
ID_SCHEMES = {"sec-accession", "ir-filing-id", "company-document", "asx-announcement"}

RELATIONSHIPS = {
    "cypress-fab-operations": "Cypress describes its Minnesota (Bloomington) fab",
    "cypress-process-technology": "Cypress process technologies made or transferred at the fab (0.13 µm, S8, SONOS)",
    "cypress-third-party-foundry": "Cypress selling wafer-line capacity to outside customers before the 2017 sale",
    "cypress-fab-sale": "sale of the Minnesota fab subsidiary to SkyWater's owners (2017)",
    "cypress-technology-license": "the 2017 Process Technology License Agreement and its amendments",
    "cypress-foundry-services": "Cypress (later Infineon) as SkyWater's wafer customer under the foundry services agreement",
    "skywater-fab-history": "SkyWater describes the fab's Cypress origin",
    "skywater-ipo": "SkyWater's 2021 initial public offering",
    "skywater-suppliers": "SkyWater names its suppliers",
    "oxbow-related-party": "Oxbow ownership, management fees and property transactions",
    "minnesota-fab-investment": "investment and government funding for the Minnesota fab",
    "infineon-cypress-acquisition": "Infineon's acquisition of Cypress (2019-2020)",
    "infineon-fab25-sale": "SkyWater's purchase of Infineon's Austin fab (Fab 25)",
    "infineon-wafer-supply": "Infineon as SkyWater's wafer customer (2022 frame agreement, Fab 25 supply agreement)",
    "skywater-customers": "SkyWater names its customers",
    "skywater-ionq-merger": "IonQ's acquisition of SkyWater (2026)",
    "skywater-governance": "SkyWater's auditor appointments, material weaknesses and restatements as a public company",
    "supplier-names-skywater": "a supplier's filing names SkyWater",
    "customer-names-skywater": "a customer's filing names SkyWater",
    "partner-names-skywater": "a technology partner's filing names SkyWater",
}

DISCOVERY = {
    "inventory-seed": "already in docs/references/public-sources.md",
    "edgar-listing-wayback": "a Wayback capture of the filer's EDGAR company filing list",
    "wayback-cdx": "a Wayback CDX listing of captured EDGAR folders or documents",
    "exhibit-index": "the exhibit index or text of another filing in the dataset",
    "ir-archive": "the filer's investor-relations archive",
    "annualreports-com": "annualreports.com archive",
    "news-citation": "public news or a press release citing the filing",
    "web-search": "a web search, followed by fetching the document",
}

RELATIONS = {"cites", "context"}

RECORD_KEYS = [
    ("id", str, False),
    ("company", str, False),
    ("company_key", str, False),
    ("form", str, False),
    ("document_type", str, False),
    ("parent", str, True),
    ("title", str, False),
    ("period", dict, True),
    ("filed", "date", False),
    ("jurisdiction", str, False),
    ("regulator", str, False),
    ("identifier", dict, True),
    ("urls", dict, False),
    ("about", dict, False),
    ("auditor_report", dict, True),
    ("relationships", list, False),
    ("related_docs", list, False),
    ("inventory_key", str, True),
    ("discovery", list, False),
    ("discovery_note", str, False),
    ("verified", str, False),
]
OPTIONAL_KEYS = {"notes"}


def is_date(v) -> bool:
    if isinstance(v, dt.date):
        return True
    if isinstance(v, str) and DATE_RE.match(v):
        try:
            dt.date.fromisoformat(v)
            return True
        except ValueError:
            return False
    return False


def to_date(v) -> dt.date | None:
    if isinstance(v, dt.date):
        return v
    if is_date(v):
        return dt.date.fromisoformat(v)
    return None


def doc_labels() -> dict[str, Path]:
    labels: dict[str, Path] = {}
    for path in DOCS.rglob("*.md"):
        if "_build" in path.parts or "plans" in path.parts:
            continue
        for lab in LABEL_RE.findall(path.read_text()):
            labels[lab] = path
    return labels


def inventory_keys() -> set[str]:
    return set(KEY_RE.findall(INVENTORY.read_text()))


def walk_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from walk_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_strings(v)


def norm_url(u: str) -> str:
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    return u.replace(":80/", "/").rstrip("/")


def check_record(r: dict, where: str, labels: dict[str, Path], keys: set[str],
                 ids: set[str], problems: list[str]) -> None:
    def bad(msg: str) -> None:
        problems.append(f"{where}: {msg}")

    expected = [k for k, _, _ in RECORD_KEYS]
    present = [k for k in r if k not in OPTIONAL_KEYS]
    missing = [k for k in expected if k not in r]
    extra = [k for k in r if k not in expected and k not in OPTIONAL_KEYS]
    if missing:
        bad(f"missing keys {missing}")
    if extra:
        bad(f"unknown keys {extra}")
    if not missing and not extra and present != expected:
        bad("keys out of order (see RECORD_KEYS)")
    for key, typ, nullable in RECORD_KEYS:
        if key not in r:
            continue
        v = r[key]
        if v is None:
            if not nullable:
                bad(f"{key} must not be null")
            continue
        if typ == "date":
            if not is_date(v):
                bad(f"{key} is not an ISO date: {v!r}")
        elif not isinstance(v, typ):
            bad(f"{key} must be {typ.__name__}")
    if "notes" in r and not isinstance(r["notes"], str):
        bad("notes must be a string")

    rid = r.get("id")
    if isinstance(rid, str) and not ID_RE.match(rid):
        bad(f"id is not a lower-case slug: {rid!r}")

    if r.get("company_key") not in COMPANIES:
        bad(f"company_key {r.get('company_key')!r} not in the controlled list")
    if r.get("document_type") not in DOCUMENT_TYPES:
        bad(f"document_type {r.get('document_type')!r} not in the controlled list")
    if r.get("jurisdiction") not in JURISDICTIONS:
        bad(f"jurisdiction {r.get('jurisdiction')!r} not in the controlled list")
    if r.get("regulator") not in REGULATORS:
        bad(f"regulator {r.get('regulator')!r} not in the controlled list")
    parent = r.get("parent")
    if parent is not None and parent not in ids:
        bad(f"parent {parent!r} is not a record id")
    if r.get("document_type") == "exhibit" and parent is None:
        bad("an exhibit needs a parent record")

    filed = to_date(r.get("filed"))
    period = r.get("period")
    if isinstance(period, dict):
        unknown = set(period) - {"label", "start", "end", "note"}
        if unknown:
            bad(f"period has unknown keys {sorted(unknown)}")
        if not isinstance(period.get("label"), str):
            bad("period.label must be a string")
        for k in ("start", "end"):
            if period.get(k) is not None and not is_date(period.get(k)):
                bad(f"period.{k} is not an ISO date")
        s, e = to_date(period.get("start")), to_date(period.get("end"))
        if s and e and s > e:
            bad("period starts after it ends")
        if e and filed and e > filed and not period.get("note"):
            bad("period ends after the filing date without a period.note")

    ident = r.get("identifier")
    accession = None
    if isinstance(ident, dict):
        if set(ident) != {"scheme", "value"}:
            bad("identifier must have exactly scheme and value")
        if ident.get("scheme") not in ID_SCHEMES:
            bad(f"identifier.scheme {ident.get('scheme')!r} not in the controlled list")
        if ident.get("scheme") == "sec-accession":
            accession = ident.get("value")
            if not isinstance(accession, str) or not ACCESSION_RE.match(accession):
                bad(f"accession number malformed: {accession!r}")
    elif r.get("regulator") == "SEC":
        bad("an SEC record needs an identifier")

    urls = r.get("urls")
    if isinstance(urls, dict):
        unknown = set(urls) - {"original", "wayback", "ir"}
        if unknown:
            bad(f"urls has unknown keys {sorted(unknown)}")
        original = urls.get("original")
        wayback = urls.get("wayback")
        ir = urls.get("ir")
        if not isinstance(original, str):
            bad("urls.original must be a URL")
        for name in ("original", "wayback", "ir"):
            u = urls.get(name)
            if u is None:
                continue
            if not isinstance(u, str) or not u.startswith("https://") or " " in u:
                bad(f"urls.{name} is not an https URL: {u!r}")
        if isinstance(wayback, str):
            m = WAYBACK_RE.match(wayback)
            if not m:
                bad(f"urls.wayback has the wrong shape: {wayback!r}")
            elif isinstance(original, str) and norm_url(m.group(2)) != norm_url(original):
                bad("urls.wayback does not embed urls.original")
        if isinstance(ir, str) and "sec.gov" in ir.split("/")[2]:
            bad("urls.ir must not be on sec.gov")
        on_sec = isinstance(original, str) and original.split("/")[2].endswith("sec.gov")
        if on_sec and not (wayback or ir):
            bad("a sec.gov original needs a Wayback or investor-relations copy")
        if on_sec and accession:
            folder = accession.replace("-", "")
            if f"/{folder}/" not in original:
                bad(f"urls.original is not in the EDGAR folder of {accession}")
        if r.get("regulator") == "SEC" and accession and not on_sec:
            bad("an SEC record with an accession number needs the sec.gov document as urls.original")
        if r.get("regulator") == "SEC" and not accession and not (ir or wayback):
            bad("an SEC record without an accession number needs an investor-relations or Wayback copy")
    about = r.get("about")
    if isinstance(about, dict):
        if set(about) != {"summary", "quotes"}:
            bad("about must have exactly summary and quotes")
        if not isinstance(about.get("summary"), str) or len(about.get("summary", "")) < 20:
            bad("about.summary must be a sentence or more")
        quotes = about.get("quotes")
        if not isinstance(quotes, list) or not 1 <= len(quotes) <= 2:
            bad("about.quotes must hold one or two quotes")
        else:
            for i, q in enumerate(quotes):
                if not isinstance(q, dict) or set(q) != {"text", "location"}:
                    bad(f"about.quotes[{i}] must have exactly text and location")
                    continue
                if not isinstance(q["text"], str) or not 10 <= len(q["text"]) <= 400:
                    bad(f"about.quotes[{i}].text must be 10-400 characters")
                if not isinstance(q["location"], str) or not q["location"]:
                    bad(f"about.quotes[{i}].location is empty")

    aud = r.get("auditor_report")
    if isinstance(aud, dict):
        if set(aud) != {"firm", "subject", "date", "quote"}:
            bad("auditor_report must have exactly firm, subject, date and quote")
        elif not is_date(aud.get("date")):
            bad("auditor_report.date is not an ISO date")

    rels = r.get("relationships")
    if isinstance(rels, list):
        if not rels:
            bad("relationships is empty")
        for t in rels:
            if t not in RELATIONSHIPS:
                bad(f"relationship {t!r} not in the controlled list")
        if len(set(rels)) != len(rels):
            bad("duplicate relationship tags")

    disc = r.get("discovery")
    if isinstance(disc, list):
        if not disc:
            bad("discovery is empty")
        for t in disc:
            if t not in DISCOVERY:
                bad(f"discovery method {t!r} not in the controlled list")

    ikey = r.get("inventory_key")
    if ikey is not None and ikey not in keys:
        bad(f"inventory_key {ikey!r} not in public-sources.md")
    if ikey is not None and isinstance(disc, list) and "inventory-seed" not in disc:
        bad("a record with an inventory key lists inventory-seed as a discovery method")

    rd = r.get("related_docs")
    if isinstance(rd, list):
        for i, d in enumerate(rd):
            if not isinstance(d, dict) or set(d) != {"label", "relation", "reason"}:
                bad(f"related_docs[{i}] must have exactly label, relation and reason")
                continue
            lab = d["label"]
            if lab not in labels:
                bad(f"related_docs label {lab!r} is not defined in docs/")
                continue
            if d["relation"] not in RELATIONS:
                bad(f"related_docs[{i}].relation {d['relation']!r} not in {sorted(RELATIONS)}")
            if not isinstance(d["reason"], str) or not d["reason"].endswith(".") \
                    or d["reason"].count(". ") > 0:
                bad(f"related_docs[{i}].reason must be one sentence ending with a full stop")
            if d["relation"] == "cites":
                if ikey is None:
                    bad(f"related_docs[{i}] 'cites' needs an inventory_key")
                elif f"[^{ikey.lower()}]" not in labels[lab].read_text():
                    bad(f"page of {lab!r} does not cite [^{ikey.lower()}]")

    v = r.get("verified")
    if isinstance(v, str):
        m = VERIFIED_RE.match(v)
        if not m or not is_date(m.group(1)):
            bad("verified must be '<ISO date> <source fetched>'")

    for s in walk_strings(r):
        if EMAIL_RE.search(s):
            bad("record contains an e-mail address")
            break


def tidy(t: str) -> str:
    """NFKC-normalise and unify quotes/dashes, without changing case or removing whitespace."""
    t = unicodedata.normalize("NFKC", t)
    t = t.replace(" ", " ")
    t = re.sub(r"[‘’‚′]", "'", t)
    t = re.sub(r'[“”„″]', '"', t)
    t = re.sub(r"[‐-―−]", "-", t)
    t = t.replace("…", "...")
    return t


def normalise(t: str) -> str:
    # PDF text extraction drops or inserts spaces (and hyphenates words split across a
    # justified line break, e.g. "Bloom- ington"), so compare without either.
    # Case-SENSITIVE: FIL-R1-04, a mis-cased quotation must not pass as verbatim.
    return re.sub(r"[\s-]+", "", tidy(t))


def normalise_map(t: str) -> tuple[str, list[int]]:
    """``normalise(t)``, plus a map from each kept character's index in the result
    back to its index in ``tidy(t)`` -- the whitespace/case-preserving text the
    heading and page-position checks work on. A quote is located (``locate_fragment``)
    by searching this fully normalised text, exactly as the verbatim check does,
    then mapping the match back to a ``tidy(t)`` offset -- rather than a separate,
    laxer whitespace-only regex search, which could miss a quote ``normalise``
    finds (e.g. a mid-word hyphen, or a line-wrap hyphen in a different place)."""
    tidied = tidy(t)
    out: list[str] = []
    idx: list[int] = []
    for i, c in enumerate(tidied):
        if c.isspace() or c == "-":
            continue
        out.append(c)
        idx.append(i)
    return "".join(out), idx


def locate_fragment(
    quote_text: str, raw_text: str, where: str, what: str, abstentions: list[str]
) -> int | None:
    """Return the offset into ``raw_text`` (``tidy``-ed, whitespace/case preserved)
    of the quote's first ellipsis-delimited fragment, found on exactly the same
    fully normalised text the verbatim check (``fragments_match_in_order``) uses.
    Appends one abstention and returns ``None`` when the fragment is empty or
    cannot be located at all."""
    first_fragment = re.split(r"\s*(?:…|\.\.\.|\[…\])\s*", quote_text)[0].strip()
    if not first_fragment:
        abstentions.append(f"{where}: quote has no text before its first ellipsis; location not checked")
        return None
    frag = normalise(first_fragment)
    if not frag:
        abstentions.append(f"{where}: quote has no usable text; location not checked")
        return None
    norm_text, idx_map = normalise_map(raw_text)
    idx = norm_text.find(frag)
    if idx == -1:
        abstentions.append(
            f"{where}: quote text not found in the fetched text (even fully normalised); "
            f"{what} not checked: {quote_text[:60]!r}")
        return None
    return idx_map[idx]


def _line_initial(pos: int, text: str) -> bool:
    """True when the character at ``pos`` in ``text`` starts a line (or the text),
    or immediately follows a sentence-terminal period or colon with no line break
    at all. Some PDF extractions run a paragraph's last sentence straight into the
    next heading with no newline whatsoever (e.g. "...other market conditions and
    other factors.Item 4. Controls and Procedures"), which a plain "starts a line"
    test would miss entirely. A genuine cross-reference ("as described under Item
    8") is preceded by a lower-case word and a space, never by punctuation
    touching the match directly, so this does not reopen that hole."""
    if pos == 0:
        return True
    before = text[:pos].rstrip(" \t")
    return before.endswith("\n") or before.endswith(".") or before.endswith(":")


REFERENCE_CUE_RE = re.compile(r"(?:under|see|discussed|described|regarding|pursuant|refer(?:red)?)\s*$", re.I)


def _looks_like_cross_reference(pos: int, text: str) -> bool:
    """True when the ~30 characters immediately before ``pos`` -- crossing a line
    break, since a cross-reference can coincidentally end its own line by an
    ordinary word-wrap -- end with a reference-introducing word ("...these
    factors are discussed under\\nItem 1A.\\nBusiness Segments..."). Such a match
    starts a line only by coincidence: the sentence naming the item continues
    right there, into unrelated heading-shaped text on the next line. A real
    heading is never preceded by "discussed under"/"see"/etc."""
    before = text[max(0, pos - 30):pos].rstrip()
    return bool(REFERENCE_CUE_RE.search(before))


TOC_ENTRY_TAIL_RE = re.compile(r"(?:\.{2,}|\s)\d+\s*$")
TOC_DOT_LEADER_RE = re.compile(r"\.{4,}")
TOC_ENTRY_WINDOW = 250  # characters; long enough to cross one wrapped title line


def _looks_like_toc_entry(m: re.Match, text: str) -> bool:
    """True when the text shortly after this match -- up to TOC_ENTRY_WINDOW
    characters, or a blank-line paragraph break, whichever comes first -- ends
    in a page number or contains a dot leader ("Item 14. Controls and
    Procedures ....... 75", a dot-leader-free "Item 1. Financial Statements 4",
    or a title that itself wraps onto a second line before the dots and page
    number: "ITEM 9.CHANGES IN ... FINANCIAL\\nDISCLOSURES ..... 73"). This is
    the standard shape of a table-of-contents entry regardless of how many
    other entries sit near it, and catches a TOC entry _drop_toc_runs cannot:
    one left isolated (run length under 3) by an intervening "PART II" line, a
    non-Item sub-entry, or its own title wrapping to a second physical line --
    any of which can widen the gap to its neighbours past the run threshold. A
    real section heading's line(s) are just its title, continuing into prose,
    not a leader-and-number, and stop at the first blank-line paragraph break
    checked here, well short of the window."""
    window = text[m.end():m.end() + TOC_ENTRY_WINDOW]
    brk = re.search(r"\n[ \t]*\n", window)
    if brk:
        window = window[:brk.start()]
    if not window.strip():
        return False
    return bool(TOC_DOT_LEADER_RE.search(window)) or bool(TOC_ENTRY_TAIL_RE.search(window.rstrip()))


_last = [0.0]


CACHE_MAX_AGE_DAYS = 90  # FIL-R1-11: re-fetch a non-Wayback copy after this long


def fetch(url: str) -> bytes:
    if "sec.gov" in url.split("/")[2]:
        raise ValueError("refusing to fetch sec.gov directly")
    CACHE.mkdir(parents=True, exist_ok=True)
    p = CACHE / hashlib.sha1(url.encode()).hexdigest()
    is_wayback = WAYBACK_RE.match(url) is not None
    if p.exists():
        # FIL-R1-11: a Wayback capture is an immutable snapshot (its timestamp is
        # already in the URL), so its cache entry never goes stale; an
        # investor-relations or other live company copy can change or disappear, so
        # re-fetch it once its cache entry (the file's own mtime is the "fetch
        # timestamp beside it") is older than CACHE_MAX_AGE_DAYS -- a passing
        # ``--online`` run then means "confirmed live within the last 90 days", not
        # "confirmed live once, arbitrarily long ago".
        age_days = (time.time() - p.stat().st_mtime) / 86400
        if is_wayback or age_days <= CACHE_MAX_AGE_DAYS:
            return p.read_bytes()
    m = WAYBACK_RE.match(url)
    if m:  # raw capture, without the Wayback banner
        url = f"https://web.archive.org/web/{m.group(1)}id_/{m.group(2)}"
    for attempt in range(4):
        wait = 4.0 - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=120) as resp:
                b = resp.read()
            if b[:2] == b"\x1f\x8b":
                b = gzip.decompress(b)
            p.write_bytes(b)
            return b
        except (urllib.error.URLError, TimeoutError) as exc:
            if isinstance(exc, urllib.error.HTTPError) and exc.code == 404:
                raise
            time.sleep(30 * (attempt + 1))
    raise RuntimeError(f"could not fetch {url}")


# Block-level tags: a document flattened by simply blanking every tag (the old
# behaviour) never has a heading start a line, because "<h2>Risk Factors</h2>Some
# text" collapses to "Risk Factors Some text" with nothing between them -- the
# heading check requires a preceding newline, so it silently abstained on every
# HTML filing. Turning each block boundary into a newline first (before the
# generic tag-stripping pass) restores that line structure, the same as a PDF
# extraction naturally has it.
BLOCK_TAG_RE = re.compile(
    r"(?is)</?(?:p|div|tr|table|thead|tbody|tfoot|td|th|li|ul|ol|h[1-6]|section|"
    r"article|header|footer|blockquote|hr|br)\b[^>]*>")


def document_pages(b: bytes) -> list[str] | None:
    """Per-page extracted text for a PDF, else None (task A: "page N" locations need
    to know which page a quote is on; document_text alone joins every page into one
    string). The sole place a PDF is parsed with pypdf, so document_text (below)
    never re-parses it -- a second, redundant pypdf pass through the same bytes."""
    if b[:4] != b"%PDF":
        return None
    import pypdf

    reader = pypdf.PdfReader(io.BytesIO(b))
    return [(page.extract_text() or "") for page in reader.pages]


def document_text(b: bytes, pages: list[str] | None = None) -> str:
    """Whole-document text. For a PDF this only joins pages already extracted by
    document_pages (pass them in to avoid parsing the PDF a second time); for HTML,
    block-level tags become newlines (see BLOCK_TAG_RE) before the remaining tags
    are blanked, so a heading keeps its line boundary."""
    if b[:4] == b"%PDF":
        if pages is None:
            pages = document_pages(b)
        return "\n".join(pages or [])
    t = b.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = BLOCK_TAG_RE.sub("\n", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return html.unescape(t)


# V-11: the body pages of the Cypress FY1999 annual report (annualreports.com file
# NASDAQ_CY_1999.pdf) are set in a subsetted font that pypdf cannot map to Unicode at
# all; instead of dropping the glyph, pypdf names it literally, e.g. "/G4B". This
# particular font's glyph table is a constant offset from the character's WinAnsi
# code -- chr(int(hex, 16) + 29) recovers it -- and a handful of its glyphs (kerning
# artifacts with no visible letter of their own) have no ToUnicode entry and come out
# as a literal ".", "_" pair that decodes to nothing. Keyed by identifier.value so this
# document-specific offset can never be applied to an unrelated filing.
GLYPH_OFFSET_DOCS = {"NASDAQ_CY_1999": 29}


def decode_glyph_font(text: str, offset: int) -> str:
    def sub(m: re.Match) -> str:
        return "".join(chr(int(h, 16) + offset) for h in re.findall(r"/G([0-9A-Fa-f]{2})", m.group(0)))

    text = re.sub(r"(?:/G[0-9A-Fa-f]{2})+", sub, text)
    return text.replace("._", "")


FRAGMENT_MAX_GAP = 4000  # normalised (whitespace-stripped) characters between ellipsis fragments


def fragments_match_in_order(quote: str, text: str) -> bool:
    """True if every ellipsis-separated fragment of ``quote`` occurs in ``text``, in
    order, each starting no more than FRAGMENT_MAX_GAP characters after the previous
    fragment ends (FIL-R1-04: a quote stitched from distant or reordered passages must
    not pass)."""
    parts = [p for p in re.split(r"\s*(?:…|\.\.\.|\[…\])\s*", quote) if p.strip()]
    if not parts:
        return False
    pos = 0
    for part in parts:
        idx = text.find(normalise(part), pos)
        if idx == -1:
            return False
        if pos and idx - pos > FRAGMENT_MAX_GAP:
            return False
        pos = idx + len(normalise(part))
    return True


def location_item_number(location: str) -> str | None:
    """The Item number a ``location`` string names, keeping a sub-item number in
    full (an 8-K's "Item 4.01" must not be truncated to "4" -- doing so made the
    checker unable to tell Item 1.01 from Item 1.02, or 4.01 from 5.02)."""
    m = re.search(r"item\s*(\d+(?:\.\d+)?[a-z]?)", location, re.I)
    return m.group(1).upper() if m else None


# Case-insensitive (modern EDGAR HTML renders "Item 1.01", not "ITEM 1.01" --
# requiring literal caps made every mixed-case document abstain outright) and with
# an optional sub-item number ("4.01", "5.02"), not just a trailing letter ("1A").
# Losing case as a signal of "this is a real heading, not an inline cross-reference"
# means that signal now comes from _line_initial instead: callers only keep a match
# that starts a line.
HEADING_RE = re.compile(r"Item\s+(\d+(?:\.\d+)?[A-Za-z]?)(?:\s*[.:]|(?=\s+[A-Z]))", re.I)
# A caption is either followed by its own punctuation ("Item 1. Business", "ITEM
# 1A. RISK FACTORS") or, common for 8-K items, by no punctuation at all before the
# capitalised title ("Item 4.01 Changes in Registrant's Certifying Accountant") --
# the second alternative is a lookahead so it does not swallow the space before the
# title into the match.


def _item_num(s: str) -> float:
    """A sortable number for an Item value: "1" -> 1, "1A" -> 1.5, "4.01" -> 4.01,
    "5.02" -> 5.02. Used only to detect an ascending run (a table of contents);
    the letter-suffix and decimal-sub-item schemes never collide in EDGAR's own
    numbering, so a shared "add a fraction" encoding is enough for that purpose."""
    m = re.match(r"(\d+)(?:\.(\d+))?([a-z]?)", s.lower())
    whole = int(m.group(1))
    if m.group(2):
        return whole + int(m.group(2)) / (10 ** len(m.group(2)))
    return whole + (0.5 if m.group(3) else 0)


def _drop_toc_runs(matches: list[re.Match]) -> list[re.Match]:
    """A table of contents lists "ITEM 1.", "ITEM 2.", ... in close, ascending
    succession, each entry typically under 150 characters (a short title plus a page
    number); a real section heading does not. Drop any match that is part of such a
    tightly-spaced run of 3 or more, so a TOC near the top of the document is not
    mistaken for the nearest real heading.

    The gap is intentionally tight (200 characters, not a larger figure): Part III of
    a modern 10-K that incorporates everything by reference to the proxy statement
    often has items 10-15 as one-sentence stubs, so their headings can legitimately
    land 400-1800 characters apart -- close enough to look like a run under a looser
    threshold, but far looser than an actual TOC line, whose next entry follows within
    a couple of hundred characters. A 700-character threshold falsely dropped the real
    Item 15 heading on skywater-10-k-2026-03-11's exhibit index (found by --online),
    reporting it as nearest to Item 12 instead; 200 characters keeps the real TOC (all
    gaps under 150 characters in the record checked) while no longer catching that
    run."""
    kept: list[re.Match] = []
    run: list[re.Match] = []

    def flush():
        if len(run) < 3:
            kept.extend(run)
        run.clear()

    prev_end = None
    prev_num = None
    for m in matches:
        num = _item_num(m.group(1))
        in_run = (
            prev_end is not None and m.start() - prev_end < 200
            and prev_num is not None and num > prev_num
        )
        if in_run:
            run.append(m)
        else:
            flush()
            run.append(m)
        prev_end, prev_num = m.end(), num
    flush()
    return kept


def check_item_location(
    quote_text: str, location: str, raw_text: str, where: str, problems: list[str], abstentions: list[str]
) -> None:
    """Best-effort check (FIL-R1-05): if ``location`` names an Item number, and the
    quote can be located (``locate_fragment``, on the same fully normalised text as
    the verbatim check), compare it with the nearest preceding "ITEM N[.NN]" heading.
    A heading must start a line -- this drops both a table-of-contents listing
    (_drop_toc_runs, a tightly-spaced ascending run) and an inline "see Item 1A"
    cross-reference, which HEADING_RE's now-case-insensitive match would otherwise
    treat the same as a real caption. This augments, never replaces, the verbatim
    check above.

    V-13: every case this cannot check records one line in ``abstentions`` (printed
    and counted by ``main``) instead of returning silently, so a clean "0 problems"
    run no longer reads as "every location was verified" when some were not checked
    at all -- that silence is what let V-01's wrong Item number through undetected."""
    def candidates(matches):
        return [
            m for m in matches
            if _line_initial(m.start(), raw_text)
            and not _looks_like_cross_reference(m.start(), raw_text)
            and not _looks_like_toc_entry(m, raw_text)
        ]

    stated = location_item_number(location)
    if not candidates(HEADING_RE.finditer(raw_text)):
        abstentions.append(
            f"{where}: document never renders an \"Item N\" heading in the expected form; "
            f"Item {stated} was not checked")
        return
    offset = locate_fragment(quote_text, raw_text, where, f"Item {stated}", abstentions)
    if offset is None:
        return
    all_matches = candidates(HEADING_RE.finditer(raw_text[:offset]))
    headings = _drop_toc_runs(all_matches)
    if not headings:
        abstentions.append(f"{where}: no Item heading precedes the quote in the fetched text; Item {stated} not checked")
        return
    nearest = headings[-1].group(1).upper()
    if nearest != stated:
        problems.append(
            f"{where}: location says Item {stated} but the quote sits nearest to "
            f"Item {nearest} in the fetched text: {quote_text[:60]!r}")


PAGE_RE = re.compile(r"\bpage\s+(\d+)\b", re.I)
# Locations that name a position rather than a heading or page number.  "cover page"/
# "first page"/"cover page note" are checked against PDF page 1 when the source is a
# PDF, and against the start of the extracted text otherwise (HTML press releases have
# no real pages); "first paragraph"/"second paragraph" are checked against a
# blank-line-delimited paragraph index.
PAGE_ONE_LOCATIONS = {"cover page", "cover page note", "first page"}
PARAGRAPH_LOCATIONS = {"first paragraph": 0, "second paragraph": 1}

GENERIC_HEADING_SEGMENTS = {
    "form 10-k section", "annual report", "part i", "part ii", "part iii", "part iv",
    "form 10-k", "combined management report", "notes to consolidated financial statements",
    "notes to the consolidated financial statements",
    "notes to the condensed consolidated financial statements", "exhibit index",
    "exhibit", "introductory section", "introductory note",
}


def loose_pattern_ci(fragment: str) -> re.Pattern:
    """A case-insensitive regex matching ``fragment`` with runs of whitespace relaxed
    to ``\\s+``, for locating a prose section heading's occurrences in whitespace-
    preserved text, which may be rendered in a different case than the location
    string names it (e.g. small caps, all caps, or title case in the original PDF)."""
    pieces = [re.escape(p) for p in fragment.split()]
    return re.compile(r"\s+".join(pieces), re.I)


def heading_phrase(location: str) -> str | None:
    """The most specific part of a non-Item, non-page location, to search for as a
    prose section heading: the text after the last comma (a location like "Notes to
    the condensed consolidated financial statements, Major Customers and
    Concentration Risk" names its sub-heading there), preferring a trailing
    parenthetical when one is present (e.g. "Exhibit, amendment ... (recitals)" names
    "recitals"), with generic scaffolding segments (GENERIC_HEADING_SEGMENTS) and
    segments under 4 characters skipped. Returns None when no segment qualifies (e.g.
    a bare "Part I")."""
    segments = [p.strip() for p in location.split(",")]
    for seg in reversed(segments):
        if not seg or seg.lower() in GENERIC_HEADING_SEGMENTS or len(seg) < 4:
            continue
        m = re.search(r"\(([^()]{4,})\)\s*$", seg)
        return m.group(1).strip() if m else seg
    return None


def check_heading_location(
    quote_text: str, location: str, raw_text: str, where: str, problems: list[str], abstentions: list[str]
) -> None:
    """Location check for a prose section heading that is not an "ITEM N" caption
    (annual-report sections, exhibit headings, press-release headings). Finds the
    heading phrase (heading_phrase) and the quote's position (locate_fragment, on
    the same fully normalised text the verbatim check uses), then compares it with
    the nearest occurrence of that phrase that actually looks like a heading --
    starting a line (_line_initial), not sitting mid-sentence -- since the same
    words also turn up as an ordinary cross-reference (e.g. "...as described under
    Risk Factors, the Company...", or fy2006's boilerplate "The letter to
    Shareholders and 'MD&A' contain forward-looking statements...", found 55000
    characters after that record's real, differently-worded "FELLOW SHAREHOLDERS:"
    heading -- counting it would have wrongly failed a correct location). A
    heading in an HTML document can only start a line because document_text turns
    block-tag boundaries into newlines first; without that, no HTML heading could
    ever satisfy _line_initial and this check would always abstain on HTML filings.
    Only a heading-like occurrence within HEADING_MAX_GAP characters of the quote
    counts; when the nearest one *follows* the quote instead of preceding it, that
    is a wrong location (e.g. a quote actually in a 10-Q's general "Note 1 --
    Nature of Business" but whose location instead names the "Business
    Combinations" accounting-policy note that follows a paragraph later).

    Known limitation: unlike an Item number, a prose heading is not enumerable, so
    this check has no way to determine which heading actually precedes a given
    quote -- it only confirms that the heading *named in* ``location`` is
    heading-like and precedes the quote within range. A location naming the wrong
    heading, when that wrong heading happens to also precede the quote within
    HEADING_MAX_GAP, passes silently; only a named heading that is absent,
    mid-sentence-only, too far away, or on the wrong side of the quote is caught.
    """
    phrase = heading_phrase(location)
    if not phrase:
        abstentions.append(f"{where}: location {location!r} names no specific heading; not checked")
        return
    offset = locate_fragment(quote_text, raw_text, where, f"heading {phrase!r}", abstentions)
    if offset is None:
        return
    occurrences = [hm.start() for hm in loose_pattern_ci(phrase).finditer(raw_text)]
    if not occurrences:
        abstentions.append(
            f"{where}: heading {phrase!r} (from location {location!r}) not found anywhere "
            f"in the fetched text; not checked")
        return
    heading_like = [o for o in occurrences if _line_initial(o, raw_text)]
    if not heading_like:
        abstentions.append(
            f"{where}: heading {phrase!r} only occurs mid-sentence (e.g. a cross-reference), "
            f"never starting a line, in the fetched text; not checked")
        return
    HEADING_MAX_GAP = 20000  # tidy()-ed, whitespace-preserving characters; prose sections run far longer than a TOC line
    nearest = min(heading_like, key=lambda o: abs(o - offset))
    gap = offset - nearest  # positive: heading precedes the quote; negative: it follows
    if abs(gap) > HEADING_MAX_GAP:
        abstentions.append(
            f"{where}: heading {phrase!r} found but not within {HEADING_MAX_GAP} characters "
            f"of the quote; treated as unverifiable, not checked")
        return
    if gap < 0:
        problems.append(
            f"{where}: location names heading {phrase!r} but the nearest such heading in the "
            f"fetched text follows the quote by {-gap} characters instead of preceding it: "
            f"{quote_text[:60]!r}")


def check_page_location(
    quote_text: str, stated_page: int, pages: list[str] | None, where: str,
    problems: list[str], abstentions: list[str],
) -> None:
    """Location check for a "page N" location: confirms the quote's first fragment
    occurs on the stated 1-based page of the fetched PDF."""
    if pages is None:
        abstentions.append(
            f"{where}: location names page {stated_page} but the fetched copy is not a PDF; not checked")
        return
    first_fragment = re.split(r"\s*(?:…|\.\.\.|\[…\])\s*", quote_text)[0].strip()
    if not first_fragment:
        abstentions.append(f"{where}: quote has no text before its first ellipsis; location not checked")
        return
    frag = normalise(first_fragment[:120])
    found = [i + 1 for i, p in enumerate(pages) if frag and frag in normalise(p)]
    if not found:
        abstentions.append(f"{where}: quote text not found on any PDF page; page {stated_page} not checked")
        return
    if stated_page not in found:
        problems.append(
            f"{where}: location says page {stated_page} but the quote is on page(s) {found} "
            f"of the fetched PDF: {quote_text[:60]!r}")


def check_positional_location(
    quote_text: str, location: str, raw_text: str, pages: list[str] | None, where: str,
    problems: list[str], abstentions: list[str],
) -> None:
    """Location check for "cover page"/"first page"/"cover page note" (checked against
    PDF page 1, or the start of the text when there are no PDF pages) and "first
    paragraph"/"second paragraph" (checked against a blank-line-delimited paragraph
    index)."""
    loc = location.strip().lower()
    first_fragment = re.split(r"\s*(?:…|\.\.\.|\[…\])\s*", quote_text)[0].strip()
    if not first_fragment:
        abstentions.append(f"{where}: quote has no text before its first ellipsis; location not checked")
        return
    frag = normalise(first_fragment[:120])
    if not frag:
        abstentions.append(f"{where}: quote has no usable text; location not checked")
        return
    if loc in PAGE_ONE_LOCATIONS:
        if pages is not None:
            found = [i + 1 for i, p in enumerate(pages) if frag in normalise(p)]
            if not found:
                abstentions.append(f"{where}: quote text not found on any PDF page; {location!r} not checked")
            elif 1 not in found:
                problems.append(
                    f"{where}: location says {location!r} but the quote is on page(s) {found}, "
                    f"not page 1: {quote_text[:60]!r}")
            return
        window = normalise(raw_text)
        idx = window.find(frag)
        if idx == -1:
            abstentions.append(f"{where}: quote text not found in the fetched text; {location!r} not checked")
        elif idx > 4000:
            problems.append(
                f"{where}: location says {location!r} but the quote first occurs {idx} "
                f"normalised characters into the fetched text: {quote_text[:60]!r}")
        return
    idx = PARAGRAPH_LOCATIONS.get(loc)
    if idx is None:
        abstentions.append(f"{where}: location {location!r} not recognised as a position; not checked")
        return
    # A press release's headline and subheadline are their own blank-line-delimited
    # "paragraphs" ahead of the real body text, so a naive index would call the
    # headline "the first paragraph". Keep only paragraphs that read as prose --
    # a lower-case letter immediately followed by ". " and at least 20 more
    # characters of text in the same paragraph (i.e. a real sentence boundary with
    # another sentence or clause following, not just the paragraph ending there).
    # Requiring more text after the period, not merely "a period or the end of the
    # paragraph", matters because a short headline/subheadline can itself contain a
    # sentence-shaped abbreviation ("Companies to Host Joint Webcast Today at 8:30
    # a.m. ET" satisfies "lower-case letter, period, end of paragraph" on its own,
    # which the previous, looser test wrongly counted as prose). Fall back to the
    # unfiltered list if a document happens to have no such paragraph at all,
    # rather than checking nothing.
    all_paras = [p for p in re.split(r"\n\s*\n+", raw_text) if p.strip()]
    prose_re = re.compile(r"[a-z]\.\s+\S.{19,}", re.S)
    paras = [p for p in all_paras if prose_re.search(p)] or all_paras
    matches = [i for i, p in enumerate(paras) if frag in normalise(p)]
    if not matches:
        abstentions.append(f"{where}: quote text not found in any extracted paragraph; {location!r} not checked")
        return
    if idx not in matches:
        problems.append(
            f"{where}: location says {location!r} but the quote is in paragraph(s) "
            f"{[m + 1 for m in matches]} (1-based, headline/subheadline paragraphs excluded) "
            f"of the fetched text: {quote_text[:60]!r}")


def check_location(
    quote_text: str, location: str, raw_text: str, pages: list[str] | None, where: str,
    problems: list[str], abstentions: list[str],
) -> None:
    """Dispatches to the right location check for ``location``'s shape (FIL task A:
    fewer abstentions than the Item-only checker this replaces): an "Item N" caption
    (check_item_location, unchanged), a "page N" reference for a PDF
    (check_page_location), a recognised position such as "cover page" or "second
    paragraph" (check_positional_location), or -- the fallback that now covers most of
    what used to abstain -- a prose section heading named in the location
    (check_heading_location). Only when none of these can make sense of ``location``
    does it abstain outright."""
    if location_item_number(location):
        check_item_location(quote_text, location, raw_text, where, problems, abstentions)
        return
    m = PAGE_RE.search(location)
    if m:
        check_page_location(quote_text, int(m.group(1)), pages, where, problems, abstentions)
        return
    if location.strip().lower() in PAGE_ONE_LOCATIONS or location.strip().lower() in PARAGRAPH_LOCATIONS:
        check_positional_location(quote_text, location, raw_text, pages, where, problems, abstentions)
        return
    check_heading_location(quote_text, location, raw_text, where, problems, abstentions)


def date_variants(d) -> list[str]:
    if not isinstance(d, dt.date):
        return []
    out = [d.isoformat(), d.strftime("%B %-d, %Y") if hasattr(d, "strftime") else ""]
    try:
        out.append(f"{d.strftime('%B')} {d.day}, {d.year}")
        out.append(f"{d.day} {d.strftime('%B')} {d.year}")
    except ValueError:
        pass
    return [v for v in out if v]


def check_metadata(r: dict, raw_text: str, where: str, problems: list[str]) -> None:
    """Best-effort check (FIL-R1-05): the filer's name and the period-end date, in some
    common rendering, should occur somewhere in the fetched text. Silent (not a
    problem) when the text is too different in style to say either way -- this is a
    supplement to, not a replacement for, the verbatim quote check."""
    company = (r.get("company") or "").split()
    if company:
        first = normalise(company[0])
        if len(first) >= 3 and first not in normalise(raw_text):
            problems.append(f"{where}: company name {company[0]!r} not found in the fetched text")
    end = to_date((r.get("period") or {}).get("end"))
    variants = date_variants(end)
    if variants and not any(normalise(v) in normalise(raw_text) for v in variants):
        problems.append(
            f"{where}: period.end {end} not found in the fetched text in any common rendering "
            f"(tried {variants}) -- may be printed only as a fiscal-year label; verify by hand")


def check_online(r: dict, where: str, problems: list[str], abstentions: list[str]) -> None:
    """Confirm the quotes in the Wayback copy, else in the investor-relations copy."""
    urls = r.get("urls") or {}
    sources = [u for u in (urls.get("wayback"), urls.get("ir")) if u]
    if not sources and urls.get("original") and "sec.gov" not in urls["original"]:
        sources = [urls["original"]]
    if not sources:
        problems.append(f"{where}: no fetchable copy (no wayback/ir url, and original is on sec.gov)")
        return
    # The auditor's signature quote has no ``location`` field in the schema (it is not
    # claimed to sit at any particular place in the document), so it is given location
    # ``None`` and check_location is not called for it below -- that is not an
    # abstention, since no location was ever asserted to check.
    quotes = [(q.get("text", ""), q.get("location", "")) for q in (r.get("about") or {}).get("quotes", [])]
    aud = r.get("auditor_report")
    if isinstance(aud, dict):
        quotes.append((aud.get("quote", ""), None))
    pending = list(quotes)
    fetched = []
    raw_texts = []
    for source in sources:
        if not pending:
            break
        try:
            b = fetch(source)
            pages = document_pages(b)
            raw = document_text(b, pages)
            offset = GLYPH_OFFSET_DOCS.get((r.get("identifier") or {}).get("value"))
            if offset is not None:
                raw = decode_glyph_font(raw, offset)
                if pages is not None:
                    pages = [decode_glyph_font(p, offset) for p in pages]
            raw = tidy(raw)
            if pages is not None:
                pages = [tidy(p) for p in pages]
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{where}: could not fetch {source}: {exc}")
            continue
        fetched.append(source)
        raw_texts.append(raw)
        text = normalise(raw)
        still_pending = []
        for q, loc in pending:
            if fragments_match_in_order(q, text):
                if loc is not None:
                    check_location(q, loc, raw, pages, where, problems, abstentions)
            else:
                still_pending.append((q, loc))
        pending = still_pending
    if fetched:
        for q, _loc in pending:
            problems.append(f"{where}: quote not found in {', '.join(fetched)}: {q[:60]!r}")
        if not pending and raw_texts:
            check_metadata(r, "\n".join(raw_texts), where, problems)


def check_known_gaps(gaps, problems: list[str]) -> None:
    """Validate the top-level ``known_gaps`` list (FIL-R1-13): filings known to exist
    but for which no non-sec.gov copy could be found or read. Each entry names the
    company, describes the filing and gives the reason no record was added."""
    if not isinstance(gaps, list):
        problems.append("known_gaps must be a list")
        return
    for i, g in enumerate(gaps):
        where = f"known_gaps[{i}]"
        if not isinstance(g, dict) or set(g) != {"company_key", "description", "reason"}:
            problems.append(f"{where}: must have exactly company_key, description and reason")
            continue
        if g["company_key"] not in COMPANIES:
            problems.append(f"{where}: company_key {g['company_key']!r} not in the controlled list")
        if not isinstance(g["description"], str) or not g["description"]:
            problems.append(f"{where}: description must be a non-empty string")
        if not isinstance(g["reason"], str) or not g["reason"].endswith("."):
            problems.append(f"{where}: reason must be a string ending with a full stop")


# --------------------------------------------------------------------------
# self-test


def selftest() -> int:
    """Offline unit tests for the location-check machinery (FIL task: constructed
    cases for each new behaviour). Touches no files, makes no network request."""
    problems: list[str] = []

    def fail(msg: str) -> None:
        problems.append(msg)

    # 1. Full sub-item numbers are kept, not truncated ("4.01" must not become "4").
    if location_item_number("Item 4.01, Departure of Directors") != "4.01":
        fail("location_item_number truncated a sub-item number")
    if location_item_number("Item 1A, Risk Factors") != "1A":
        fail("location_item_number lost a letter suffix")
    if location_item_number("Item 2") != "2":
        fail("location_item_number failed on a bare item number")

    # 2. HEADING_RE is case-insensitive and captures the full sub-item number.
    ms = list(HEADING_RE.finditer("Item 4.01 Changes in Registrant's Certifying Accountant"))
    if not ms or ms[0].group(1) != "4.01":
        fail(f"HEADING_RE did not capture a mixed-case sub-item caption: {ms}")
    if not HEADING_RE.search("ITEM 1A. RISK FACTORS"):
        fail("HEADING_RE regressed on an all-caps caption")

    # 3. _item_num orders sub-item and letter-suffix values as expected, and
    #    _drop_toc_runs still drops a tightly-spaced ascending run in mixed case.
    if not (_item_num("1") < _item_num("1.01") < _item_num("1.02") < _item_num("2")):
        fail("_item_num does not order sub-item numbers correctly")
    if not (_item_num("7") < _item_num("7A") < _item_num("8")):
        fail("_item_num does not order a letter suffix correctly")
    toc_text = ("Item 1. Business .... 3\nItem 1A. Risk Factors .... 9\n"
                "Item 2. Properties .... 15\n" + ("x" * 5000) +
                "\nItem 1. Business\nSome real body text about the business.")
    toc_matches = [m for m in HEADING_RE.finditer(toc_text) if _line_initial(m.start(), toc_text)]
    kept = _drop_toc_runs(toc_matches)
    if len(kept) != 1 or kept[0].start() < 5000:
        fail(f"_drop_toc_runs did not drop a mixed-case table-of-contents run: {[m.group(0) for m in kept]}")

    # 4. document_text turns HTML block-tag boundaries into newlines, so a heading
    #    embedded in a paragraph flow still starts a line once flattened.
    html_doc = (b"<html><body><h2>Item 1.01 Entry into a Material Definitive "
                b"Agreement</h2><p>The Company entered into an agreement.</p>"
                b"<p>See <a href=\"#\">Item 1A</a> for risk factors.</p></body></html>")
    flat = document_text(html_doc)
    if "\nItem 1.01" not in flat and not flat.lstrip().startswith("Item 1.01"):
        fail(f"document_text did not give the HTML heading a line start: {flat!r}")
    if not any(_line_initial(m.start(), flat) for m in HEADING_RE.finditer(flat)):
        fail("no heading-like Item match survived HTML flattening")

    # 5. locate_fragment finds a quote via the same normalise() the verbatim check
    #    uses, tolerating a mid-word hyphen/line-wrap a whitespace-only search would
    #    not have (this is the fix for the four "quote text not found" abstentions).
    hyphenated = "The wafer reaches a temperature of 125°-\nC during the anneal."
    abst: list[str] = []
    off = locate_fragment("temperature of 125°C during", hyphenated, "w", "test", abst)
    if off is None or abst:
        fail(f"locate_fragment failed on a hyphen/line-wrap the verbatim check tolerates: {abst}")

    # 6. check_item_location: wrong sub-item number fails; correct mixed-case
    #    sub-item passes; a heading that appears only in the table of contents does
    #    not count as the section start (the quote sits right after the table of
    #    contents, well before the document's one real "Item 1" heading, so only
    #    the TOC's own "Item 2" entry is anywhere near it).
    body = ("Item 1. Business\nBody text here.\n\n"
            "Item 4.01 Changes in Registrant's Certifying Accountant\n"
            "The Company dismissed its auditor on May 1.\n\n"
            "Item 5.02 Departure of Directors\n"
            "A director resigned. See Item 4.01 above for the auditor change.")
    quote = "The Company dismissed its auditor on May 1."

    ps, ab = [], []
    check_item_location(quote, "Item 4.01, Changes in Registrant's Certifying Accountant", body, "w", ps, ab)
    if ps or ab:
        fail(f"a correct mixed-case sub-item location was rejected: problems={ps} abstentions={ab}")

    ps, ab = [], []
    check_item_location(quote, "Item 5.02, Departure of Directors", body, "w", ps, ab)
    if not ps:
        fail("a wrong sub-item number (5.02 instead of 4.01) was not caught as a problem")

    toc_doc = ("Item 1. Business .... 3\nItem 1A. Risk Factors .... 8\n"
               "Item 2. Properties .... 15\n"
               "This section discusses our real and personal properties.\n" +
               ("x" * 3000) + "\nItem 1. Business\nBody text.\n")
    ps, ab = [], []
    check_item_location("This section discusses our real and personal properties.",
                         "Item 2, Properties", toc_doc, "w", ps, ab)
    if ps or not ab:
        fail(f"a heading only in the table of contents was wrongly treated as the "
             f"section start: problems={ps} abstentions={ab}")

    # 7. check_heading_location: mirror the mid-sentence case for a prose heading
    #    (not an Item caption): a correct, line-initial heading passes; the same
    #    words occurring only inside a sentence must abstain, not silently pass.
    prose = ("Overview\nThe Company makes semiconductors.\n\n"
             "Risk Factors\nOur business faces several risks.")
    ps, ab = [], []
    check_heading_location("Our business faces several risks.", "Risk Factors", prose, "w", ps, ab)
    if ps or ab:
        fail(f"a correct prose heading location was rejected: problems={ps} abstentions={ab}")
    mid = ("Overview\nThe Company makes semiconductors.\n\n"
           "As noted under Risk Factors, our business faces several risks.")
    ps, ab = [], []
    check_heading_location("our business faces several risks.", "Risk Factors", mid, "w", ps, ab)
    if ps or not ab:
        fail(f"a prose heading only mid-sentence was not abstained on: problems={ps} abstentions={ab}")

    if problems:
        for p in problems:
            print("SELFTEST FAIL:", p)
        print(f"{len(problems)} selftest problem(s)")
        return 1
    print("selftest OK")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if "--selftest" in args:
        return selftest()
    online = "--online" in args
    args = [a for a in args if a != "--online"]
    path = Path(args[0]) if args else DATA
    problems: list[str] = []
    try:
        data = yaml.safe_load(path.read_text())
    except (OSError, yaml.YAMLError) as exc:
        print(f"{path}: {exc}")
        print("0 filings checked, 1 problems")
        return 1
    if not isinstance(data, dict):
        print(f"{path}: not a mapping")
        print("0 filings checked, 1 problems")
        return 1
    if data.get("schema_version") != 1:
        problems.append("schema_version must be 1")
    if not is_date(data.get("retrieved")):
        problems.append("retrieved must be an ISO date")
    filings = data.get("filings")
    if not isinstance(filings, list):
        print("data/filings.yaml: filings must be a list")
        print("0 filings checked, 1 problems")
        return 1
    labels = doc_labels()
    keys = inventory_keys()
    ids = [f.get("id") for f in filings if isinstance(f, dict)]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup:
        problems.append(f"duplicate ids: {dup}")
    seen_docs: dict[tuple, str] = {}
    order = []
    abstentions: list[str] = []
    for n, f in enumerate(filings):
        where = f"filings[{n}] {f.get('id') if isinstance(f, dict) else ''}".strip()
        if not isinstance(f, dict):
            problems.append(f"{where}: not a mapping")
            continue
        check_record(f, where, labels, keys, set(ids), problems)
        ident = f.get("identifier") or {}
        original = (f.get("urls") or {}).get("original")
        k = (ident.get("value"), original)
        if ident.get("value") and k in seen_docs:
            problems.append(f"{where}: same identifier and URL as {seen_docs[k]}")
        seen_docs[k] = f.get("id")
        order.append((str(f.get("filed")), str(f.get("id"))))
        if online:
            check_online(f, where, problems, abstentions)
    if order != sorted(order):
        problems.append("filings are not sorted by filing date, then id")
    if "known_gaps" in data:
        check_known_gaps(data["known_gaps"], problems)
    for p in problems:
        print(p)
    # V-13: report every location abstention (never just swallow it), and count them
    # in the summary, so "0 problems" cannot be misread as "every location was
    # verified" -- it now means only that none of the *checked* locations were wrong.
    for a in abstentions:
        print(a)
    print(f"{len(filings)} filings checked, {len(problems)} problems", end="")
    print(f", {len(abstentions)} locations not checked" if online else "")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
