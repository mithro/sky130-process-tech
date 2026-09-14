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

With ``--online`` it also fetches each record's Wayback or
investor-relations copy (never ``sec.gov``) with the project user agent
and confirms that every quote occurs in the document text (whitespace,
quotation marks and dashes normalised).  Online fetches are paced and
cached under ``tmp/filings-cache/``.

Run with ``uv run tools/check_filings.py [--online] [path]``.  It prints
"N filings checked, M problems"; the exit status is non-zero when a
problem is found.
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


def normalise(t: str) -> str:
    t = unicodedata.normalize("NFKC", t)
    t = t.replace(" ", " ")
    t = re.sub(r"[‘’‚′]", "'", t)
    t = re.sub(r"[“”„″]", '"', t)
    t = re.sub(r"[‐-―−]", "-", t)
    t = t.replace("…", "...")
    # PDF text extraction drops or inserts spaces, so compare without any.
    return re.sub(r"\s+", "", t).lower()


_last = [0.0]


def fetch(url: str) -> bytes:
    if "sec.gov" in url.split("/")[2]:
        raise ValueError("refusing to fetch sec.gov directly")
    CACHE.mkdir(parents=True, exist_ok=True)
    p = CACHE / hashlib.sha1(url.encode()).hexdigest()
    if p.exists():
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


def document_text(b: bytes) -> str:
    if b[:4] == b"%PDF":
        import pypdf

        reader = pypdf.PdfReader(io.BytesIO(b))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    t = b.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return html.unescape(t)


def check_online(r: dict, where: str, problems: list[str]) -> None:
    """Confirm the quotes in the Wayback copy, else in the investor-relations copy."""
    urls = r.get("urls") or {}
    sources = [u for u in (urls.get("wayback"), urls.get("ir")) if u]
    if not sources and urls.get("original") and "sec.gov" not in urls["original"]:
        sources = [urls["original"]]
    quotes = [q.get("text", "") for q in (r.get("about") or {}).get("quotes", [])]
    aud = r.get("auditor_report")
    if isinstance(aud, dict):
        quotes.append(aud.get("quote", ""))
    pending = list(quotes)
    fetched = []
    for source in sources:
        if not pending:
            break
        try:
            text = normalise(document_text(fetch(source)))
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{where}: could not fetch {source}: {exc}")
            continue
        fetched.append(source)
        pending = [q for q in pending if not all(
            normalise(part) in text
            for part in re.split(r"\s*(?:…|\.\.\.|\[…\])\s*", q) if part.strip())]
    if fetched:
        for q in pending:
            problems.append(f"{where}: quote not found in {', '.join(fetched)}: {q[:60]!r}")


def main() -> int:
    args = sys.argv[1:]
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
            check_online(f, where, problems)
    if order != sorted(order):
        problems.append("filings are not sorted by filing date, then id")
    for p in problems:
        print(p)
    print(f"{len(filings)} filings checked, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
