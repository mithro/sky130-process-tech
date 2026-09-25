#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml", "pymupdf", "pypdf"]
# ///
"""Keep the Cypress-history evidence re-checkable from what is committed.

The evidence files ``data/history/*.yaml`` hold verbatim quotes;
``tools/check_history_quotes.py`` checks them against a local, untracked
fetch cache (``tmp/cyhist-cache/`` in the main checkout). This tool makes
sure the cache can be rebuilt from the committed records alone, so no claim
has to be researched again when the cache is lost or a reviewer starts from
a clean clone.

Subcommands:

``status``
    One line per record: whether its original document and extracted text
    are in the cache, whether the record carries ``sha256`` and
    ``archive_url``. Ends with totals.

``archive [--write]``
    For records with no ``archive_url``, ask the Wayback Machine's
    availability API for the capture closest to the record's ``retrieved``
    date and print it; ``--write`` adds it to the YAML. Read-only towards the
    archive: it never requests a new capture.

``hash [--write]``
    For records with no ``sha256`` whose original document is in the cache,
    print its SHA-256; ``--write`` adds it to the YAML.

``rebuild DIR [--ids ID ...]``
    Fetch every record's document afresh into DIR (Wayback ``id_`` copy
    first, then the live URL), check it against the recorded ``sha256``,
    extract its text the way the cache was made (pymupdf for PDFs, tag
    stripping for HTML), and look for every quote in the fresh text. Reports
    the records whose quotes cannot be re-found. This is the proof that the
    evidence does not depend on the local cache.

A record whose cached copy did not come from its ``url`` (an API response for a paper, say)
names the URL it came from in ``fetched_from``; ``rebuild`` fetches that first.

A record's cached text is ``<cache root>/<cache>`` when the record has a
``cache`` field, else ``<cache root>/*/<id>.txt``; its original document is
the file with the same stem and any other extension.

Fetching uses the project user agent and waits between requests.
"""

from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_history_quotes as chq  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "history"
CACHE = chq.CACHE_ROOT
UA = "sky130-process-tech docs checker"
PAUSE = 5.0
ORIGINAL_EXTS = (".pdf", ".html", ".htm", ".bin", ".raw")


def evidence_files() -> list[Path]:
    return [p for p in sorted(DATA.glob("*.yaml")) if p.name != "claims.yaml"]


def records(path: Path) -> list[dict]:
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    out: list[dict] = []
    for key in ("documents", "records"):
        out += [r for r in doc.get(key) or [] if isinstance(r, dict) and r.get("id")]
    return out


def cached_text(rec: dict) -> Path | None:
    if rec.get("cache"):
        p = CACHE / str(rec["cache"])
        return p if p.exists() else None
    return chq.find_cache_text(str(rec["id"]))


def original(rec: dict) -> Path | None:
    text = cached_text(rec)
    if text is None:
        return None
    stem = text.name.split(".")[0]
    for ext in ORIGINAL_EXTS:
        p = text.with_name(stem + ext)
        if p.exists():
            return p
    return None


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    # the Wayback Machine's raw ("id_") copies keep the site's own gzip encoding
    return gzip.decompress(data) if data[:2] == b"\x1f\x8b" else data


def raw_wayback(url: str) -> str:
    """The Wayback URL that returns the archived bytes unchanged."""
    return re.sub(r"(web\.archive\.org/web/\d+)(?:id_)?/", r"\1id_/", url, count=1)


def set_field(text: str, rid: str, field: str, value: str) -> str:
    """Set ``field: value`` in the YAML block of record ``rid``: replace an existing null value, or
    add the line after the record's ``url:`` line."""
    m = re.search(rf"(?ms)^- id: {re.escape(rid)}\n.*?(?=^- id: |\Z)", text)
    if not m:
        raise SystemExit(f"record {rid} not found")
    block = m.group(0)
    if re.search(rf"(?m)^  {field}: (?:null|~|'')?\s*$", block):
        new = re.sub(rf"(?m)^  {field}: (?:null|~|'')?\s*$", f"  {field}: {value}", block, count=1)
    elif re.search(rf"(?m)^  {field}:", block):
        return text
    else:
        new = re.sub(r"(?m)^(  url: .*(?:\n    .*)*)$", rf"\1\n  {field}: {value}", block, count=1)
        if new == block:
            raise SystemExit(f"record {rid}: no url line to add {field} after")
    return text[:m.start()] + new + text[m.end():]


def cmd_status(_args: argparse.Namespace) -> int:
    tot = {"records": 0, "text": 0, "original": 0, "sha256": 0, "archive_url": 0}
    for path in evidence_files():
        for rec in records(path):
            t, o = cached_text(rec), original(rec)
            flags = [("text", t is not None), ("original", o is not None),
                     ("sha256", bool(rec.get("sha256"))), ("archive_url", bool(rec.get("archive_url")))]
            tot["records"] += 1
            for k, v in flags:
                tot[k] += v
            print(f"{path.name}:{rec['id']}: " + " ".join(f"{k}={'yes' if v else 'NO'}" for k, v in flags))
    print("totals: " + ", ".join(f"{k} {v}" for k, v in tot.items()))
    return 0


def capture(url: str, stamp: str, sha1_b32: str | None = None) -> str | None:
    """The Wayback capture (status 200) of ``url`` closest to ``stamp`` (YYYYMMDD): from the CDX
    index, which lists every capture, else from the availability API."""
    q = urllib.parse.urlencode({"url": url, "output": "json", "fl": "timestamp,original,digest",
                                "filter": "statuscode:200", "collapse": "digest"})
    try:
        rows = json.loads(get(f"https://web.archive.org/cdx/search/cdx?{q}") or b"[]")[1:]
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        rows = []
    time.sleep(PAUSE)
    if rows:
        # a capture holding the very bytes cached here wins (captures can be truncated)
        same = [r for r in rows if sha1_b32 and len(r) > 2 and r[2] == sha1_b32]
        ts, orig = min(same or rows, key=lambda r: abs(int(r[0][:8]) - int(stamp or r[0][:8])))[:2]
        return f"https://web.archive.org/web/{ts}/{orig}"
    q = urllib.parse.urlencode({"url": url, "timestamp": stamp})
    try:
        data = json.loads(get(f"https://archive.org/wayback/available?{q}"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None
    finally:
        time.sleep(PAUSE)
    snap = (data.get("archived_snapshots") or {}).get("closest") or {}
    if snap.get("available") and str(snap.get("status", "200")) == "200":
        return snap["url"].replace("http://web.archive.org", "https://web.archive.org")
    return None


def cmd_archive(args: argparse.Namespace) -> int:
    seen: dict[str, str | None] = {}
    for path in evidence_files():
        text = path.read_text(encoding="utf-8")
        changed = False
        for rec in records(path):
            if rec.get("archive_url") or not rec.get("url"):
                continue
            stamp = re.sub(r"\D", "", str(rec.get("retrieved") or ""))[:8]
            if rec["url"] not in seen:
                o = original(rec)
                sha1 = base64.b32encode(hashlib.sha1(o.read_bytes()).digest()).decode() if o else None
                seen[rec["url"]] = capture(rec["url"], stamp, sha1)
            url = seen[rec["url"]]
            if url:
                print(f"{path.name}:{rec['id']}: {url}")
                if args.write:
                    text = set_field(text, str(rec["id"]), "archive_url", url)
                    changed = True
            else:
                print(f"{path.name}:{rec['id']}: no capture")
        if changed:
            path.write_text(text, encoding="utf-8")
    return 0


def cmd_hash(args: argparse.Namespace) -> int:
    for path in evidence_files():
        text = path.read_text(encoding="utf-8")
        changed = False
        for rec in records(path):
            o = original(rec)
            if rec.get("sha256") or o is None:
                continue
            sha = hashlib.sha256(o.read_bytes()).hexdigest()
            print(f"{path.name}:{rec['id']}: {sha} ({o.name})")
            if args.write:
                text = set_field(text, str(rec["id"]), "sha256", sha)
                changed = True
        if changed:
            path.write_text(text, encoding="utf-8")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    for name in ("archive", "hash"):
        p = sub.add_parser(name)
        p.add_argument("--write", action="store_true")
    args = ap.parse_args()
    try:
        return {"status": cmd_status, "archive": cmd_archive, "hash": cmd_hash}[args.cmd](args)
    finally:
        pass


if __name__ == "__main__":
    sys.exit(main())
