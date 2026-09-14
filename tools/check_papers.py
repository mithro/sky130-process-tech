#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Check the academic paper index datasets.

``data/papers.yaml`` holds the included papers and
``data/papers-excluded.yaml`` the papers that were considered and
excluded or held, so that they are not rediscovered and re-argued.
``data/papers-labels.yaml`` is the append-only map of every published
page label to its paper id.

Offline checks (always run):

* both files are YAML lists of mappings with exactly the schema keys, in
  order, and the right value types; the included list is sorted by
  ``(year, title.casefold())``;
* ids are strings of the form ``doi:<lower-case DOI>``, ``arxiv:<new-style
  id>`` or ``web:<slug>``, agree with the ``doi`` and ``arxiv`` fields,
  and are unique across both files; DOIs, arXiv ids and ``label`` values
  are unique;
* labels have the form ``paper-<family>-<year><letter>`` and match the
  record's year; ``title_display`` carries no inline TeX or backticks;
* DOIs, arXiv ids, years and URLs are well formed (``https://`` only);
* no URL or text points at a host that distributes unauthorised or
  scraped copies (Sci-Hub and its successors, Anna's Archive, LibGen,
  Z-Library, ResearchGate, Academia.edu and similar); free full-text
  links must also be on the allowlist of hosts below; no e-mail address,
  ``mailto`` or ``email=`` parameter appears anywhere;
* nothing refers to the mask-renders site, MPW run or frame identifiers
  or the process-steps sheet (fabrication statements come from the paper
  only), and ``fabrication.source`` is one of the enumerated values;
* ``topics`` come from the controlled list and are not repeated;
  ``basis`` is one of the enumerated values; ``institutions`` is non-empty;
* ``related_docs`` labels exist as ``(label)=`` targets under ``docs/``
  and carry a one-sentence reason; ``inventory_key`` values exist in
  ``docs/references/public-sources.md``;
* ``verified``, every link's ``checked`` and every exclusion's
  ``decided`` start with an ISO 8601 date that is not in the future;
* ``paywalled`` agrees with the listed free copies;
* titles, notes, quotes and reasons are single lines;
* every record's label is in the label map with its id, and every label
  in the map is still used by the same paper (a published label may not be
  dropped, renamed or reused; an id correction goes in ``previous_ids``).

``--online`` re-fetches every DOI from the Crossref REST API and compares
title, author family names, year (a record may carry an earlier
conference year), container title, landing URL, volume, issue and pages;
checks arXiv titles (also for DOI records with an arXiv id); checks that
``web:`` titles appear on their proceedings page (a Wayback Machine copy
is accepted); and checks each fabrication quote against the abstract
(OpenAlex or arXiv) or the arXiv HTML full text.  ``--links`` re-fetches
every free full-text link and reports results that differ from the
recorded ``checked`` status.  Both send only the project user agent and
never any contact details, and back off on HTTP 429.

Prints "N papers checked, M problems" and exits non-zero on problems.
Run with ``uv run tools/check_papers.py [--online] [--links]``.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "papers.yaml"
EXCLUDED = ROOT / "data" / "papers-excluded.yaml"
LABELS = ROOT / "data" / "papers-labels.yaml"
DOCS = ROOT / "docs"
INVENTORY = DOCS / "references" / "public-sources.md"
UA = "sky130-process-tech docs checker"

TOPICS = {
    # process, PDK and devices
    "pdk-models": "compact models, parameter extraction and model calibration for the PDK's devices",
    "device-characterisation": "measured behaviour of devices fabricated in the process",
    "test-structures": "test chips, test vehicles and structures for process or device evaluation",
    "reliability": "reliability, yield, harsh-environment operation and wear-out",
    "radiation": "total ionising dose, single-event effects and radiation testing",
    "cryogenic": "operation, measurement or modelling below room temperature",
    "high-temperature": "operation, measurement or modelling at elevated temperature",
    "rram": "resistive RAM devices, arrays and models (sky130B ReRAM and its lineage)",
    "sonos": "SONOS charge-trap memory",
    "floating-gate": "floating-gate devices built in the standard process",
    "beol-integration": "devices or tiers integrated in the back end of line",
    "photonics": "photonic or optoelectronic devices",
    "mems": "MEMS or post-processed mechanical structures",
    # circuits fabricated on the process
    "analog-rf": "analog and RF circuits designed for or fabricated on the process",
    "mixed-signal": "data converters and other mixed-signal circuits designed for or fabricated on the process",
    "power-management": "power converters and regulators designed for or fabricated on the process",
    "digital": "digital logic, processors and accelerators designed for or fabricated on the process",
    "memory": "SRAM and other memory macros",
    "sensors": "sensor front ends and sensing systems",
    "quantum": "circuits for quantum computing or quantum devices",
    "security": "hardware security and cryptographic circuits",
    # ecosystem and lineage
    "tooling": "open-source design flows and generators as they relate to the process",
    "education-shuttles": "papers about a shuttle programme or its educational use",
    "fab-manufacturing": "manufacturing, yield and process control at the Bloomington fab",
    "lineage-s8": "the Cypress S8 / SONOS 130 nm lineage and Cypress-era work at the fab",
}

BASIS = {
    "named-process": "the abstract or full text names SKY130 or the SkyWater 130 nm process or foundry",
    "affiliation-inference": "the process or fab is inferred from SkyWater or Cypress Bloomington author affiliations",
    "lineage-inference": "the process is inferred from public Cypress statements about the S8 lineage",
}
VENUE_TYPES = {"journal", "magazine", "conference", "workshop", "preprint", "report"}
FAB_SOURCES = {"abstract", "full text (HTML)", "full text (PDF)"}
EXCLUSION_STATUS = {"excluded", "held"}

KEYS = [
    "id", "label", "title", "title_display", "authors", "year", "venue", "venue_series", "venue_type",
    "volume", "issue", "pages", "article_number", "doi", "landing_url", "arxiv", "paywalled",
    "free_full_text", "topics", "basis", "institutions", "fabrication", "related_docs", "inventory_key",
    "discovery", "notes", "verified",
]
LINK_KEYS = ["url", "host", "oa_type", "located_via", "checked"]
EXCLUDED_KEYS = ["id", "title", "year", "status", "reason", "decided"]
LABEL_KEYS = ["label", "id", "previous_ids", "published"]

# Hosts accepted for free full-text copies (fails closed on new hosts).
ALLOWED_FREE_HOSTS = {
    "arxiv.org", "www.osti.gov", "osti.gov", "www.ncbi.nlm.nih.gov", "europepmc.org",
    "escholarship.org", "hdl.handle.net", "upcommons.upc.edu", "woset-workshop.github.io",
    "ieeexplore.ieee.org", "dl.acm.org", "www.mdpi.com", "onlinelibrary.wiley.com",
    "ietresearch.onlinelibrary.wiley.com", "iopscience.iop.org", "www.authorea.com",
    "www.techrxiv.org", "web.archive.org",
}
FORBIDDEN_HOST = re.compile(
    r"(sci-hub|scihub|sci\.hub|sci-net|annas-archive|annas-blog|libgen|library\.lol|gen\.lib\.rus|"
    r"z-lib|zlibrary|z-library|1lib\.|b-ok\.|booksc\.|singlelogin|bookfi|pdfdrive|"
    r"researchgate\.net|academia\.edu|dokumen\.pub|vdoc\.pub|epdf\.pub)",
    re.I,
)
PROVENANCE = re.compile(
    r"(data\.wafer\.space|docs\.google\.com|\brenders?\b|\bMPW-\d|\bframe [A-H]\d|\bsheet\b|"
    r"process[- ]steps)",
    re.I,
)
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+(@|%40)[A-Za-z0-9.-]+\.[a-z]{2,}|mailto|[?&]e-?mail=", re.I)
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}$")
WEB_ID_RE = re.compile(r"^web:[a-z0-9][a-z0-9-]*$")
LABEL_ID_RE = re.compile(r"^paper-[a-z0-9-]+-(\d{4})[a-z]$")
DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})( \S|$)")
LABEL_RE = re.compile(r"^\(([A-Za-z0-9_-]+)\)=\s*$", re.MULTILINE)
INV_KEY_RE = re.compile(r"^\*\*([A-Za-z0-9][A-Za-z0-9_-]*)\*\*", re.MULTILINE)


def doc_labels() -> set[str]:
    labels: set[str] = set()
    for p in DOCS.rglob("*.md"):
        if "_build" in p.parts:
            continue
        labels.update(LABEL_RE.findall(p.read_text(encoding="utf-8")))
    return labels


def is_url(u: object) -> bool:
    if not isinstance(u, str):
        return False
    p = urllib.parse.urlparse(u)
    return p.scheme == "https" and bool(p.netloc) and " " not in u


def norm_title(t: str) -> str:
    t = html.unescape(html.unescape(re.sub(r"<[^>]+>", "", t or "")))
    t = "".join(c for c in unicodedata.normalize("NFKD", t) if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", t.lower())


def squash(t: str) -> str:
    t = html.unescape(t or "")
    t = unicodedata.normalize("NFKC", t).replace("‐", "-").replace("–", "-").replace("’", "'")
    return re.sub(r"\s+", "", t)


def date_ok(value: object, today: dt.date) -> bool:
    m = DATE_RE.match(value) if isinstance(value, str) else None
    if not m:
        return False
    try:
        return dt.date.fromisoformat(m.group(1)) <= today
    except ValueError:
        return False


def fetch(url: str) -> tuple[int, bytes]:
    for i in range(5):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and i < 4:
                time.sleep(15 * (i + 1))
                continue
            return e.code, b""
        except Exception:  # noqa: BLE001
            time.sleep(3)
    return 0, b""


def str_or_null(v: object) -> bool:
    return v is None or (isinstance(v, str) and v.strip() != "")


def scan_text(where: str, blob: str) -> list[str]:
    probs = []
    if FORBIDDEN_HOST.search(blob):
        probs.append(f"{where}: forbidden host mentioned in record")
    if EMAIL.search(blob):
        probs.append(f"{where}: record contains an e-mail address or mailto/email parameter")
    m = PROVENANCE.search(blob)
    if m:
        probs.append(f"{where}: refers to the renders site, run/frame ids or the sheet ({m.group(0)!r})")
    return probs


def check_record(i: int, r: object, labels: set[str], inv_keys: set[str], today: dt.date) -> list[str]:
    probs: list[str] = []
    if not isinstance(r, dict):
        return [f"record {i}: not a mapping"]
    rid = r.get("id")
    where = rid if isinstance(rid, str) else f"record {i}"
    if list(r.keys()) != KEYS:
        missing = [k for k in KEYS if k not in r]
        extra = [k for k in r if k not in KEYS]
        probs.append(f"{where}: keys differ from schema (missing {missing}, extra {extra}, or out of order)")

    doi = r.get("doi")
    arx = r.get("arxiv")
    if not isinstance(rid, str):
        probs.append(f"{where}: id must be a string")
        rid = ""
    elif rid.startswith("doi:"):
        if not DOI_RE.match(rid[4:]) or rid[4:] != rid[4:].lower():
            probs.append(f"{where}: malformed DOI id (must be lower case)")
        if not isinstance(doi, str) or doi.lower() != rid[4:]:
            probs.append(f"{where}: doi field does not match id")
    elif rid.startswith("arxiv:"):
        if not ARXIV_RE.match(rid[6:]):
            probs.append(f"{where}: malformed arXiv id")
        if not isinstance(arx, dict) or arx.get("id") != rid[6:]:
            probs.append(f"{where}: arxiv field does not match id")
    elif not WEB_ID_RE.match(rid):
        probs.append(f"{where}: id must start with doi:, arxiv: or web:")
    if doi is not None and (not isinstance(doi, str) or not DOI_RE.match(doi)):
        probs.append(f"{where}: malformed doi {doi!r}")
    if rid.startswith("web:") and doi is not None:
        probs.append(f"{where}: web: records must not have a DOI (use a doi: id)")
    if arx is not None:
        if not isinstance(arx, dict) or set(arx) != {"id", "url"}:
            probs.append(f"{where}: arxiv must be null or {{id, url}}")
        else:
            if not isinstance(arx["id"], str) or not ARXIV_RE.match(arx["id"]):
                probs.append(f"{where}: malformed arXiv id {arx['id']!r}")
            if arx["url"] != f"https://arxiv.org/abs/{arx['id']}":
                probs.append(f"{where}: arXiv url must be https://arxiv.org/abs/<id>")

    label = r.get("label")
    m = LABEL_ID_RE.match(label) if isinstance(label, str) else None
    if not m:
        probs.append(f"{where}: label must be paper-<family>-<year><letter>")
    elif r.get("year") != int(m.group(1)):
        probs.append(f"{where}: label year does not match year")

    title = r.get("title")
    if not isinstance(title, str) or not title.strip() or re.search(r"&(amp|lt|gt|quot);", title):
        probs.append(f"{where}: title missing or contains HTML entities")
    td = r.get("title_display")
    if not isinstance(td, str) or not td.strip() or re.search(r"[$`\\]|&(amp|lt|gt);", td):
        probs.append(f"{where}: title_display missing or contains TeX, backticks or entities")
    authors = r.get("authors")
    if not isinstance(authors, list) or not authors or not all(isinstance(a, str) and a.strip() for a in authors):
        probs.append(f"{where}: authors must be a non-empty list of names")
    y = r.get("year")
    if not isinstance(y, int) or not 1980 <= y <= today.year:
        probs.append(f"{where}: year {y!r} out of range")
    for fld in ("venue", "venue_series"):
        if not isinstance(r.get(fld), str) or not r[fld].strip() or "&amp;" in str(r.get(fld)):
            probs.append(f"{where}: {fld} missing or contains HTML entities")
    if r.get("venue_type") not in VENUE_TYPES:
        probs.append(f"{where}: venue_type {r.get('venue_type')!r} not in {sorted(VENUE_TYPES)}")
    for fld in ("volume", "issue", "pages", "article_number"):
        if not str_or_null(r.get(fld)):
            probs.append(f"{where}: {fld} must be null or a string")
    if not is_url(r.get("landing_url")):
        probs.append(f"{where}: landing_url must be an https URL")
    if not isinstance(r.get("paywalled"), bool):
        probs.append(f"{where}: paywalled must be true or false")

    links = r.get("free_full_text")
    if not isinstance(links, list):
        probs.append(f"{where}: free_full_text must be a list")
        links = []
    for j, link in enumerate(links):
        lw = f"{where}: free_full_text[{j}]"
        if not isinstance(link, dict) or list(link.keys()) != LINK_KEYS:
            probs.append(f"{lw}: keys must be {LINK_KEYS}")
            continue
        if not is_url(link["url"]):
            probs.append(f"{lw}: url must be https")
        else:
            host = urllib.parse.urlparse(link["url"]).netloc.lower()
            if host != str(link["host"]).lower():
                probs.append(f"{lw}: host does not match url")
            if host not in ALLOWED_FREE_HOSTS:
                probs.append(f"{lw}: host {host} is not on the free-copy allowlist")
        if not date_ok(link["checked"], today):
            probs.append(f"{lw}: checked must start with an ISO date not in the future")
        for fld in ("oa_type", "located_via"):
            if not isinstance(link[fld], str) or not link[fld].strip():
                probs.append(f"{lw}: {fld} missing")
    publisher_free = any(
        isinstance(l, dict) and re.match(r"(gold|diamond|hybrid|bronze|conference open-access)", str(l.get("oa_type")))
        for l in links
    )
    if isinstance(r.get("paywalled"), bool) and r.get("venue_type") != "preprint":
        if r["paywalled"] and publisher_free:
            probs.append(f"{where}: paywalled is true but a free publisher version is listed")
        if not r["paywalled"] and not publisher_free:
            probs.append(f"{where}: paywalled is false but no free publisher version is listed")

    urls = [r.get("landing_url"), arx.get("url") if isinstance(arx, dict) else None]
    urls += [l.get("url") for l in links if isinstance(l, dict)]
    for u in urls:
        if isinstance(u, str) and FORBIDDEN_HOST.search(u):
            probs.append(f"{where}: forbidden host in {u}")
    probs += scan_text(where, json.dumps(r, ensure_ascii=False))

    topics = r.get("topics")
    if not isinstance(topics, list) or not topics:
        probs.append(f"{where}: topics must be a non-empty list")
    else:
        for t in topics:
            if t not in TOPICS:
                probs.append(f"{where}: topic {t!r} not in the controlled list")
        if len(set(map(str, topics))) != len(topics):
            probs.append(f"{where}: repeated topic")
    if r.get("basis") not in BASIS:
        probs.append(f"{where}: basis {r.get('basis')!r} not in {sorted(BASIS)}")
    elif r["basis"] != "named-process" and not (isinstance(r.get("notes"), str) and r["notes"].strip()):
        probs.append(f"{where}: an inferred basis needs notes explaining the inference")

    inst = r.get("institutions")
    if not isinstance(inst, list) or not inst or not all(isinstance(x, str) and x.strip() for x in inst):
        probs.append(f"{where}: institutions must be a non-empty list of names")

    fab = r.get("fabrication")
    if fab is not None:
        if not isinstance(fab, dict) or list(fab.keys()) != ["quote", "source"] or not all(
            isinstance(v, str) and v.strip() for v in fab.values()
        ):
            probs.append(f"{where}: fabrication must be null or {{quote, source}}")
        elif fab["source"] not in FAB_SOURCES:
            probs.append(f"{where}: fabrication.source {fab['source']!r} not in {sorted(FAB_SOURCES)}")

    rel = r.get("related_docs")
    if not isinstance(rel, list):
        probs.append(f"{where}: related_docs must be a list")
    else:
        for dd in rel:
            if not isinstance(dd, dict) or list(dd.keys()) != ["label", "reason"]:
                probs.append(f"{where}: related_docs entries must be {{label, reason}}")
                continue
            if dd["label"] not in labels:
                probs.append(f"{where}: related_docs label {dd['label']!r} does not exist under docs/")
            reason = str(dd["reason"]).strip()
            if not reason.endswith(".") or len(re.findall(r"[.!?](\s|$)", reason)) != 1:
                probs.append(f"{where}: related_docs reason for {dd['label']} must be one sentence")

    key = r.get("inventory_key")
    if key is not None and key not in inv_keys:
        probs.append(f"{where}: inventory_key {key!r} not in public-sources.md")
    disc = r.get("discovery")
    if not isinstance(disc, list) or not disc or not all(isinstance(x, str) and x.strip() for x in disc):
        probs.append(f"{where}: discovery must be a non-empty list")
    if not str_or_null(r.get("notes")):
        probs.append(f"{where}: notes must be null or text")
    single_line = [("title", r.get("title")), ("title_display", r.get("title_display")), ("notes", r.get("notes")),
                   ("venue", r.get("venue")), ("verified", r.get("verified"))]
    if isinstance(fab, dict):
        single_line.append(("fabrication.quote", fab.get("quote")))
    for dd in rel if isinstance(rel, list) else []:
        if isinstance(dd, dict):
            single_line.append((f"related_docs reason for {dd.get('label')}", dd.get("reason")))
    for fld, val in single_line:
        if isinstance(val, str) and re.search(r"[\n\r\t]", val):
            probs.append(f"{where}: {fld} must be a single line (no newlines or tabs)")
    if not date_ok(r.get("verified"), today) or len(str(r.get("verified"))) < 12:
        probs.append(f"{where}: verified must be '<ISO date> <source fetched>' with a date not in the future")
    return probs


def check_excluded(i: int, r: object, today: dt.date) -> list[str]:
    if not isinstance(r, dict):
        return [f"excluded record {i}: not a mapping"]
    rid = r.get("id")
    where = f"excluded {rid if isinstance(rid, str) else i}"
    probs = []
    if list(r.keys()) != EXCLUDED_KEYS:
        probs.append(f"{where}: keys must be {EXCLUDED_KEYS}")
    if not isinstance(rid, str) or not (
        (rid.startswith("doi:") and DOI_RE.match(rid[4:]) and rid == rid.lower())
        or (rid.startswith("arxiv:") and ARXIV_RE.match(rid[6:]))
        or WEB_ID_RE.match(rid)
    ):
        probs.append(f"{where}: malformed id")
    if not isinstance(r.get("title"), str) or not r["title"].strip():
        probs.append(f"{where}: title missing")
    if not isinstance(r.get("year"), int):
        probs.append(f"{where}: year must be an integer")
    if r.get("status") not in EXCLUSION_STATUS:
        probs.append(f"{where}: status must be one of {sorted(EXCLUSION_STATUS)}")
    if not isinstance(r.get("reason"), str) or not r["reason"].strip():
        probs.append(f"{where}: reason missing")
    if not date_ok(r.get("decided"), today):
        probs.append(f"{where}: decided must be an ISO date not in the future")
    probs += scan_text(where, json.dumps(r, ensure_ascii=False))
    return probs


def check_labels(entries: object, data: list, excluded: list, today: dt.date) -> list[str]:
    """The label map is append-only: every published label keeps its id for good."""
    if not isinstance(entries, list):
        return [f"{LABELS.name}: top level must be a list"]
    probs: list[str] = []
    records = {r.get("id"): r for r in data if isinstance(r, dict)}
    excluded_ids = {r.get("id") for r in excluded if isinstance(r, dict)}
    seen_labels: set[str] = set()
    seen_ids: dict[str, str] = {}
    for i, e in enumerate(entries):
        where = f"{LABELS.name} entry {i}"
        if not isinstance(e, dict) or list(e.keys()) != LABEL_KEYS:
            probs.append(f"{where}: keys must be {LABEL_KEYS}")
            continue
        lab, pid, prev = e["label"], e["id"], e["previous_ids"]
        if not isinstance(lab, str) or not LABEL_ID_RE.match(lab):
            probs.append(f"{where}: malformed label {lab!r}")
        if not isinstance(prev, list) or not all(isinstance(x, str) for x in prev):
            probs.append(f"{where}: previous_ids must be a list of ids")
            prev = []
        if not date_ok(e["published"], today):
            probs.append(f"{where}: published must be an ISO date not in the future")
        if lab in seen_labels:
            probs.append(f"{where}: label {lab!r} listed twice (labels may never be reused)")
        seen_labels.add(lab)
        for x in [pid, *prev]:
            if x in seen_ids and seen_ids[x] != lab:
                probs.append(f"{where}: id {x!r} already has label {seen_ids[x]!r}")
            seen_ids[x] = lab
        rec = records.get(pid)
        if rec is None:
            probs.append(f"{where}: published label {lab!r} ({pid}) is not in papers.yaml; a published label "
                         f"may not be dropped" + (" (the id is in the exclusions file)" if pid in excluded_ids else ""))
        elif rec.get("label") != lab:
            probs.append(f"{where}: {pid} has label {rec.get('label')!r}, but its published label is {lab!r}")
    for pid, rec in records.items():
        if isinstance(pid, str) and seen_ids.get(pid) != rec.get("label"):
            probs.append(f"{pid}: label {rec.get('label')!r} is not recorded in {LABELS.name}")
    return probs


def abstract_for(r: dict) -> str:
    if r["id"].startswith("arxiv:"):
        st, body = fetch(r["arxiv"]["url"])
        m = re.search(rb'<meta name="citation_abstract" content="([^"]*)"', body)
        return html.unescape(m.group(1).decode()) if m else ""
    st, body = fetch("https://api.openalex.org/works/doi:" + urllib.parse.quote(r["doi"], safe="/()"))
    if st != 200:
        return ""
    inv = json.loads(body).get("abstract_inverted_index") or {}
    return " ".join(w for _, w in sorted((i, w) for w, idx in inv.items() for i in idx))


def quote_in(quote: str, text: str) -> bool:
    hay = squash(text)
    pos = 0
    for part in quote.split("[…]"):
        p = squash(part)
        k = hay.find(p, pos)
        if k < 0:
            return False
        pos = k + len(p)
    return True


def family_names(names: list[str]) -> list[str]:
    return [norm_title(n.split()[-1]) if n.split() else "" for n in names]


def online_check(r: dict) -> list[str]:
    probs = []
    rid = r["id"]
    if r.get("doi"):
        st, body = fetch("https://api.crossref.org/works/" + urllib.parse.quote(r["doi"], safe="/()"))
        if st != 200:
            probs.append(f"{rid}: Crossref returned HTTP {st}")
        else:
            msg = json.loads(body)["message"]
            t = " ".join(msg.get("title") or [])
            if norm_title(t) != norm_title(r["title"]):
                probs.append(f"{rid}: Crossref title {t!r} differs")
            fams = [norm_title(a.get("family") or a.get("name") or "") for a in msg.get("author") or []]
            rec_authors = [norm_title(a) for a in r["authors"]]
            if len(fams) != len(rec_authors) or any(f and f not in ra for f, ra in zip(fams, rec_authors)):
                probs.append(f"{rid}: author family names differ from Crossref")
            years = []
            for fld in ("published-print", "published-online", "published", "issued", "created"):
                dp = ((msg.get(fld) or {}).get("date-parts") or [[None]])[0]
                if dp and dp[0]:
                    years.append(dp[0])
            cont = html.unescape(html.unescape(" ".join(msg.get("container-title") or [])))
            cont_years = [int(x) for x in re.findall(r"\b(19[89]\d|20[0-3]\d)\b", cont)]
            if r["year"] not in years + cont_years:
                probs.append(f"{rid}: year {r['year']} not among Crossref dates {years} or container years")
            if norm_title(cont) != norm_title(r["venue"]):
                probs.append(f"{rid}: container title {cont!r} differs from venue")
            landing = ((msg.get("resource") or {}).get("primary") or {}).get("URL") or ""
            if landing.replace("http://", "https://", 1) != r["landing_url"]:
                probs.append(f"{rid}: landing URL differs from Crossref resource {landing!r}")
            for fld, cfld in (("volume", "volume"), ("issue", "issue"), ("pages", "page"), ("article_number", "article-number")):
                if (msg.get(cfld) or None) != r.get(fld):
                    probs.append(f"{rid}: {fld} {r.get(fld)!r} differs from Crossref {msg.get(cfld)!r}")
    if isinstance(r.get("arxiv"), dict):
        st, body = fetch(r["arxiv"]["url"])
        m = re.search(rb'<meta name="citation_title" content="([^"]*)"', body)
        if st != 200 or not m:
            probs.append(f"{rid}: arXiv abs page returned HTTP {st}")
        elif norm_title(html.unescape(m.group(1).decode())) != norm_title(r["title"]):
            probs.append(f"{rid}: arXiv title differs")
    if rid.startswith("web:"):
        st, body = fetch(r["landing_url"])
        text = html.unescape(re.sub(r"<[^>]+>", " ", body.decode("utf-8", "replace")))
        if st != 200 or norm_title(r["title"]) not in norm_title(text):
            probs.append(f"{rid}: title not found on {r['landing_url']} (HTTP {st})")
        elif any(norm_title(a) not in norm_title(text) for a in r["authors"]):
            probs.append(f"{rid}: an author is not named on {r['landing_url']}")
    fab = r.get("fabrication")
    if isinstance(fab, dict):
        if fab.get("source") == "abstract":
            if not quote_in(fab["quote"], abstract_for(r)):
                probs.append(f"{rid}: fabrication quote not found in the abstract")
        elif fab.get("source") == "full text (HTML)" and isinstance(r.get("arxiv"), dict):
            st, body = fetch(f"https://arxiv.org/html/{r['arxiv']['id']}")
            text = html.unescape(re.sub(r"<[^>]+>", " ", body.decode("utf-8", "replace")))
            if not quote_in(fab["quote"], text):
                probs.append(f"{rid}: fabrication quote not found in the arXiv HTML full text")
    return probs


def links_check(r: dict) -> list[str]:
    probs = []
    for link in r.get("free_full_text") or []:
        st, _ = fetch(link["url"])
        m = re.search(r"HTTP (\d{3})", link.get("checked", ""))
        recorded = int(m.group(1)) if m else None
        ok = lambda s: s is not None and (200 <= s < 400)  # noqa: E731
        if st == 0 or (st >= 400 and st != 403) or (ok(recorded) != ok(st)):
            probs.append(f"{r['id']}: link {link['url']} now HTTP {st} (recorded {recorded})")
    return probs


def load(path: Path) -> tuple[list | None, str | None]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as e:
        return None, f"cannot read {path}: {e}"
    if not isinstance(data, list):
        return None, f"{path}: top level must be a list"
    return data, None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--online", action="store_true", help="re-verify metadata and quotes over the network")
    ap.add_argument("--links", action="store_true", help="re-fetch free full-text links")
    ap.add_argument("--file", type=Path, default=DATA)
    ap.add_argument("--excluded", type=Path, default=EXCLUDED)
    ap.add_argument("--labels", type=Path, default=LABELS)
    args = ap.parse_args()

    data, err = load(args.file)
    if err:
        print(err)
        print("0 papers checked, 1 problem")
        return 1
    excluded, err = load(args.excluded)
    problems: list[str] = []
    if err:
        problems.append(err)
        excluded = []
    labels = doc_labels()
    inv_keys = set(INV_KEY_RE.findall(INVENTORY.read_text(encoding="utf-8")))
    today = dt.date.today()
    seen: dict[str, int] = {}

    def once(kind: str, value: object, i: int, where: str) -> None:
        if not isinstance(value, str):
            return
        k = f"{kind}:{value.lower()}"
        if k in seen:
            problems.append(f"{where}: duplicate {kind} {value!r} (records {seen[k]} and {i})")
        else:
            seen[k] = i

    prev = None
    for i, r in enumerate(data):
        problems += check_record(i, r, labels, inv_keys, today)
        if not isinstance(r, dict):
            continue
        where = r.get("id") if isinstance(r.get("id"), str) else f"record {i}"
        once("id", r.get("id"), i, where)
        once("doi", r.get("doi"), i, where)
        if isinstance(r.get("arxiv"), dict):
            once("arxiv", r["arxiv"].get("id"), i, where)
        once("label", r.get("label"), i, where)
        if isinstance(r.get("year"), int) and isinstance(r.get("title"), str):
            key = (r["year"], r["title"].casefold())
            if prev is not None and key < prev:
                problems.append(f"{where}: out of order (sort by year, then title)")
            prev = key
        if args.online and isinstance(r.get("id"), str):
            problems += online_check(r)
        if args.links:
            problems += links_check(r)
    labels_map, err = load(args.labels)
    problems += [err] if err else check_labels(labels_map, data, excluded, today)
    included_ids = {r.get("id") for r in data if isinstance(r, dict)}
    ex_seen: set[str] = set()
    for i, r in enumerate(excluded):
        problems += check_excluded(i, r, today)
        if isinstance(r, dict) and isinstance(r.get("id"), str):
            if r["id"] in included_ids:
                problems.append(f"excluded {r['id']}: also in {args.file.name}")
            if r["id"] in ex_seen:
                problems.append(f"excluded {r['id']}: duplicate")
            ex_seen.add(r["id"])
    for p in problems:
        print(p)
    noun = "problem" if len(problems) == 1 else "problems"
    print(f"{len(data)} papers checked, {len(problems)} {noun} ({len(excluded)} excluded or held papers checked)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
