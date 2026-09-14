#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Check the academic paper index dataset ``data/papers.yaml``.

Offline checks (always run):

* the file is a YAML list of mappings with exactly the schema keys, in
  order, and the right value types;
* ids are unique and have the form ``doi:<lower-case DOI>``,
  ``arxiv:<new-style arXiv id>`` or ``web:<slug>``, and agree with the
  ``doi`` and ``arxiv`` fields;
* DOIs, arXiv ids, years and URLs are well formed (``https://`` only);
* no URL points at a host that distributes unauthorised copies
  (Sci-Hub, Anna's Archive, LibGen, Z-Library and similar);
* ``topics`` come from the controlled list below and are not repeated;
* ``related_docs`` labels exist as ``(label)=`` targets under ``docs/``
  and carry a one-sentence reason;
* ``inventory_key`` values exist as ``**KEY**`` entries in
  ``docs/references/public-sources.md``;
* ``verified`` starts with an ISO 8601 date, and every free full-text
  link records the date it was checked;
* a record whose only free copies are preprints is marked paywalled
  unless it has no publisher version (``venue_type`` preprint or a
  workshop/proceedings page).

``--online`` additionally re-fetches every DOI from the Crossref REST
API and every arXiv id from its abs page and compares the titles.  It
sends only the project user agent and never any contact details.

Prints "N papers checked, M problems" and exits non-zero on problems.
Run with ``uv run tools/check_papers.py [--online]``.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "papers.yaml"
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
    "analog-rf": "analog and RF circuits with silicon results",
    "mixed-signal": "data converters and other mixed-signal circuits with silicon results",
    "power-management": "power converters and regulators with silicon results",
    "digital": "digital logic, processors and accelerators with silicon results",
    "memory": "SRAM and other memory macros",
    "sensors": "sensor front ends and sensing systems",
    "quantum": "circuits for quantum computing or quantum devices",
    "security": "hardware security and cryptographic circuits",
    # ecosystem and lineage
    "tooling": "open-source design flows and generators as they relate to the process",
    "education-shuttles": "shuttle programmes and education built on the process",
    "fab-manufacturing": "manufacturing, yield and process control at the Bloomington fab",
    "lineage-s8": "the Cypress S8 / SONOS 130 nm lineage and Cypress-era work at the fab",
}

VENUE_TYPES = {"journal", "magazine", "conference", "workshop", "preprint", "report"}

KEYS = [
    "id", "title", "authors", "year", "venue", "venue_type", "doi", "landing_url", "arxiv",
    "paywalled", "free_full_text", "topics", "institutions", "fabrication", "related_docs",
    "inventory_key", "discovery", "notes", "verified",
]
LINK_KEYS = ["url", "host", "oa_type", "located_via", "checked"]

FORBIDDEN_HOST = re.compile(
    r"(sci-hub|scihub|sci\.hub|annas-archive|annas-blog|libgen|library\.lol|gen\.lib\.rus|"
    r"z-lib|zlibrary|z-library|1lib\.|b-ok\.|booksc\.|singlelogin|bookfi|pdfdrive|"
    r"researchgate\.net/file|dokumen\.pub|vdoc\.pub|epdf\.pub)",
    re.I,
)
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}$")
WEB_ID_RE = re.compile(r"^web:[a-z0-9][a-z0-9-]*$")
DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}) \S")
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
    t = html.unescape(re.sub(r"<[^>]+>", "", t or ""))
    return re.sub(r"[^a-z0-9]", "", t.lower())


def fetch(url: str) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception:  # noqa: BLE001
        return 0, b""


def check_record(i: int, r: object, labels: set[str], inv_keys: set[str], today: dt.date) -> list[str]:
    probs: list[str] = []
    where = f"record {i}"
    if not isinstance(r, dict):
        return [f"{where}: not a mapping"]
    rid = r.get("id")
    where = f"{rid or where}"
    keys = list(r.keys())
    if keys != KEYS:
        missing = [k for k in KEYS if k not in r]
        extra = [k for k in keys if k not in KEYS]
        probs.append(f"{where}: keys differ from schema (missing {missing}, extra {extra}, or out of order)")

    # id and identifiers
    doi = r.get("doi")
    arx = r.get("arxiv")
    if not isinstance(rid, str):
        probs.append(f"{where}: id missing")
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
    if rid and rid.startswith("web:") and doi is not None:
        probs.append(f"{where}: web: records must not have a DOI (use a doi: id)")
    if arx is not None:
        if not isinstance(arx, dict) or set(arx) != {"id", "url"}:
            probs.append(f"{where}: arxiv must be null or {{id, url}}")
        else:
            if not ARXIV_RE.match(str(arx["id"])):
                probs.append(f"{where}: malformed arXiv id {arx['id']!r}")
            if arx["url"] != f"https://arxiv.org/abs/{arx['id']}":
                probs.append(f"{where}: arXiv url must be https://arxiv.org/abs/<id>")

    # scalar fields
    if not isinstance(r.get("title"), str) or not r["title"].strip() or "&amp;" in r["title"] or "&lt;" in r["title"]:
        probs.append(f"{where}: title missing or contains HTML entities")
    authors = r.get("authors")
    if not isinstance(authors, list) or not authors or not all(isinstance(a, str) and a.strip() for a in authors):
        probs.append(f"{where}: authors must be a non-empty list of names")
    elif any("@" in a for a in authors):
        probs.append(f"{where}: authors must not contain e-mail addresses")
    y = r.get("year")
    if not isinstance(y, int) or not 1980 <= y <= today.year:
        probs.append(f"{where}: year {y!r} out of range")
    if not isinstance(r.get("venue"), str) or not r["venue"].strip() or "&amp;" in str(r.get("venue")):
        probs.append(f"{where}: venue missing or contains HTML entities")
    if r.get("venue_type") not in VENUE_TYPES:
        probs.append(f"{where}: venue_type {r.get('venue_type')!r} not in {sorted(VENUE_TYPES)}")
    if not is_url(r.get("landing_url")):
        probs.append(f"{where}: landing_url must be an https URL")
    if not isinstance(r.get("paywalled"), bool):
        probs.append(f"{where}: paywalled must be true or false")

    # free full text
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
        elif urllib.parse.urlparse(link["url"]).netloc.lower() != str(link["host"]).lower():
            probs.append(f"{lw}: host does not match url")
        if not isinstance(link["checked"], str) or not DATE_RE.match(link["checked"]):
            probs.append(f"{lw}: checked must start with an ISO date")
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

    # every URL: forbidden hosts
    urls = [r.get("landing_url"), (arx or {}).get("url") if isinstance(arx, dict) else None]
    urls += [l.get("url") for l in links if isinstance(l, dict)]
    for u in urls:
        if isinstance(u, str) and FORBIDDEN_HOST.search(u):
            probs.append(f"{where}: forbidden host in {u}")
    blob = json.dumps(r, ensure_ascii=False)
    if FORBIDDEN_HOST.search(blob):
        probs.append(f"{where}: forbidden host mentioned in record")
    if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}", blob):
        probs.append(f"{where}: record contains an e-mail address")

    # topics
    topics = r.get("topics")
    if not isinstance(topics, list) or not topics:
        probs.append(f"{where}: topics must be a non-empty list")
    else:
        for t in topics:
            if t not in TOPICS:
                probs.append(f"{where}: topic {t!r} not in the controlled list")
        if len(set(topics)) != len(topics):
            probs.append(f"{where}: repeated topic")

    inst = r.get("institutions")
    if not isinstance(inst, list) or not all(isinstance(x, str) and x.strip() for x in inst):
        probs.append(f"{where}: institutions must be a list of names")

    fab = r.get("fabrication")
    if fab is not None:
        if not isinstance(fab, dict) or list(fab.keys()) != ["statement", "source"] or not all(
            isinstance(v, str) and v.strip() for v in fab.values()
        ):
            probs.append(f"{where}: fabrication must be null or {{statement, source}}")
        elif re.search(r"data\.wafer\.space|process steps|steps sheet|docs\.google\.com", json.dumps(fab), re.I):
            probs.append(f"{where}: fabrication must come from the paper, not the renders site or the sheet")

    rel = r.get("related_docs")
    if not isinstance(rel, list):
        probs.append(f"{where}: related_docs must be a list")
    else:
        for d in rel:
            if not isinstance(d, dict) or list(d.keys()) != ["label", "reason"]:
                probs.append(f"{where}: related_docs entries must be {{label, reason}}")
                continue
            if d["label"] not in labels:
                probs.append(f"{where}: related_docs label {d['label']!r} does not exist under docs/")
            reason = str(d["reason"]).strip()
            if not reason.endswith(".") or len(re.findall(r"[.!?](\s|$)", reason)) != 1:
                probs.append(f"{where}: related_docs reason for {d['label']} must be one sentence")

    key = r.get("inventory_key")
    if key is not None and key not in inv_keys:
        probs.append(f"{where}: inventory_key {key!r} not in public-sources.md")

    disc = r.get("discovery")
    if not isinstance(disc, list) or not disc or not all(isinstance(x, str) and x.strip() for x in disc):
        probs.append(f"{where}: discovery must be a non-empty list")

    notes = r.get("notes")
    if notes is not None and (not isinstance(notes, str) or not notes.strip()):
        probs.append(f"{where}: notes must be null or text")

    ver = r.get("verified")
    m = DATE_RE.match(ver) if isinstance(ver, str) else None
    if not m:
        probs.append(f"{where}: verified must be '<ISO date> <source fetched>'")
    else:
        try:
            if dt.date.fromisoformat(m.group(1)) > today:
                probs.append(f"{where}: verified date in the future")
        except ValueError:
            probs.append(f"{where}: verified date invalid")
    return probs


def online_check(r: dict) -> list[str]:
    probs = []
    rid = r["id"]
    if r.get("doi"):
        st, body = fetch("https://api.crossref.org/works/" + urllib.parse.quote(r["doi"], safe="/()"))
        if st != 200:
            probs.append(f"{rid}: Crossref returned HTTP {st}")
        else:
            t = " ".join(json.loads(body)["message"].get("title") or [])
            if norm_title(html.unescape(t)) != norm_title(r["title"]):
                probs.append(f"{rid}: Crossref title {t!r} differs")
    if isinstance(r.get("arxiv"), dict):
        st, body = fetch(r["arxiv"]["url"])
        m = re.search(rb'<meta name="citation_title" content="([^"]*)"', body)
        if st != 200 or not m:
            probs.append(f"{rid}: arXiv abs page returned HTTP {st}")
        elif rid.startswith("arxiv:") and norm_title(html.unescape(m.group(1).decode())) != norm_title(r["title"]):
            probs.append(f"{rid}: arXiv title differs")
    if rid.startswith("web:"):
        st, body = fetch(r["landing_url"])
        text = html.unescape(re.sub(r"<[^>]+>", " ", body.decode("utf-8", "replace")))
        if st != 200 or norm_title(r["title"]) not in norm_title(text):
            probs.append(f"{rid}: title not found on {r['landing_url']} (HTTP {st})")
    return probs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--online", action="store_true", help="re-verify DOIs and arXiv ids over the network")
    ap.add_argument("--file", type=Path, default=DATA)
    args = ap.parse_args()

    problems: list[str] = []
    try:
        data = yaml.safe_load(args.file.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as e:
        print(f"cannot read {args.file}: {e}")
        print("0 papers checked, 1 problems")
        return 1
    if not isinstance(data, list):
        print("0 papers checked, 1 problems (top level must be a list)")
        return 1
    labels = doc_labels()
    inv_keys = set(INV_KEY_RE.findall(INVENTORY.read_text(encoding="utf-8")))
    today = dt.date.today()
    seen: dict[str, int] = {}
    for i, r in enumerate(data):
        problems += check_record(i, r, labels, inv_keys, today)
        if isinstance(r, dict) and isinstance(r.get("id"), str):
            if r["id"] in seen:
                problems.append(f"{r['id']}: duplicate id (records {seen[r['id']]} and {i})")
            seen.setdefault(r["id"], i)
        if isinstance(r, dict) and isinstance(r.get("doi"), str):
            other = f"doi-field:{r['doi'].lower()}"
            if other in seen and seen[other] != i:
                problems.append(f"{r['id']}: DOI repeated in another record")
            seen.setdefault(other, i)
        if args.online and isinstance(r, dict) and "id" in r:
            problems += online_check(r)
    for p in problems:
        print(p)
    print(f"{len(data)} papers checked, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
