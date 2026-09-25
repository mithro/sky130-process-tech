#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Check the Cypress process-history section (``docs/history/``).

Two groups of rules.

**Pages.** Every ``docs/history/*.md`` page except ``index.md`` and
``sources.md`` is checked with ``check_refs.check()`` exactly as an overview
page is (footnotes defined and used, no reference-style link definitions, a
``### Deep dive`` list of at least 12 entries, the C4 inline-URL invariant),
except that its footnote labels must be keys in the section's own inventory,
``docs/history/sources.md``, not in ``docs/references/public-sources.md``:
the history section is kept separate from the SKY130 reference.
``index.md`` gets the same checks with no Deep-dive minimum.

**Claims matrix.** ``data/history/claims.yaml`` lists the history's factual
claims. Each claim names its page, an ``anchor`` (a phrase that must appear
on that page), the footnote labels that carry it (each must be cited on that
page), and its sources: evidence record ids in ``data/history/*.yaml`` or
``data/{filings,patents,papers}.yaml``, each
with the organisation it comes from (``origin``). The rules:

* every source id exists in an evidence file;
* ``grade: corroborated`` needs sources from at least two different origins;
* ``grade: attributed`` needs at least two sources; the page must name the
  origin in the anchor's paragraph (the claim's ``attribution`` phrase);
* ``grade: single-source`` has one source; the anchor's paragraph must
  carry the tag "(single source)" or the claim's ``hedge`` phrase;
* ``grade: conflict`` needs at least two sources and a paragraph that
  contains the claim's ``hedge`` phrase (how the page states the conflict).

Run ``uv run tools/check_history.py``; ``--selftest`` runs the offline tests.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import check_refs  # noqa: E402

HISTORY = ROOT / "docs" / "history"
INVENTORY = HISTORY / "sources.md"
DATA = ROOT / "data" / "history"
CLAIMS = DATA / "claims.yaml"
MIN_DEEP = 12
GRADES = {"corroborated", "attributed", "single-source", "conflict"}
SINGLE_TAG = "(single source)"


def inventory_keys(text: str) -> set[str]:
    return {k.lower() for k in check_refs.KEY_RE.findall(text)}


def evidence_ids() -> set[str]:
    ids: set[str] = set()
    for path in sorted(DATA.glob("*.yaml")):
        if path == CLAIMS:
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for key in ("documents", "records"):
            for rec in doc.get(key, []) or []:
                if isinstance(rec, dict) and rec.get("id"):
                    ids.add(str(rec["id"]))
    # the site's verified datasets (tools/check_filings.py, check_patents.py,
    # check_papers.py) may also be cited as evidence for a history claim
    for name, key in (("filings.yaml", "filings"), ("patents.yaml", "families"), ("papers.yaml", "papers")):
        path = ROOT / "data" / name
        if not path.exists():
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for rec in (doc if isinstance(doc, list) else doc.get(key, []) or []):
            if isinstance(rec, dict) and rec.get("id"):
                ids.add(str(rec["id"]))
    return ids


def paragraph_of(text: str, anchor: str) -> str | None:
    """The blank-line-delimited block (paragraph, table row or bullet) that
    contains ``anchor``, whitespace-normalised; None if absent."""
    flat_anchor = " ".join(anchor.split())
    for block in re.split(r"\n\s*\n", text):
        flat = " ".join(block.split())
        if flat_anchor in flat:
            if block.lstrip().startswith("|"):
                # a table: narrow to the row that holds the anchor
                for row in block.splitlines():
                    if flat_anchor in " ".join(row.split()):
                        return " ".join(row.split())
            return flat
    return None


def check_claims(claims: list[dict], pages: dict[str, str], ids: set[str]) -> list[str]:
    problems: list[str] = []
    seen: set[str] = set()
    for c in claims:
        cid = c.get("id", "?")
        where = f"claims.yaml:{cid}"
        if cid in seen:
            problems.append(f"{where}: duplicate claim id")
        seen.add(cid)
        grade = c.get("grade")
        if grade not in GRADES:
            problems.append(f"{where}: grade {grade!r} not one of {sorted(GRADES)}")
            continue
        sources = c.get("sources") or []
        for s in sources:
            if not isinstance(s, dict) or not s.get("id") or not s.get("origin"):
                problems.append(f"{where}: each source needs id and origin: {s!r}")
            elif s["id"] not in ids:
                problems.append(f"{where}: source {s['id']!r} is not a record in data/history/")
        origins = {s.get("origin") for s in sources if isinstance(s, dict)}
        page = c.get("page")
        text = pages.get(page)
        if text is None:
            problems.append(f"{where}: page {page!r} not found under docs/history/")
            continue
        para = paragraph_of(text, c.get("anchor", ""))
        if not c.get("anchor") or para is None:
            problems.append(f"{where}: anchor {c.get('anchor')!r} not found on {page}")
            continue
        cited = set(check_refs.REF_RE.findall(text))
        for fn in c.get("footnotes") or []:
            if fn not in cited:
                problems.append(f"{where}: footnote [^{fn}] not cited on {page}")
        if not c.get("footnotes"):
            problems.append(f"{where}: no footnotes listed")
        if grade == "corroborated" and len(origins) < 2:
            problems.append(f"{where}: corroborated needs two different origins, has {sorted(map(str, origins))}")
        if grade in ("attributed", "conflict") and len(sources) < 2:
            problems.append(f"{where}: {grade} needs at least two sources")
        if grade == "attributed":
            phrase = c.get("attribution")
            if not phrase or phrase not in para:
                problems.append(f"{where}: attribution {phrase!r} not in the anchor's paragraph")
        if grade == "single-source":
            if len(sources) != 1:
                problems.append(f"{where}: single-source claim lists {len(sources)} sources")
            hedge = c.get("hedge") or SINGLE_TAG
            if hedge not in para:
                problems.append(f"{where}: {hedge!r} not in the anchor's paragraph")
        if grade == "conflict":
            hedge = c.get("hedge")
            if not hedge or hedge not in para:
                problems.append(f"{where}: conflict hedge {hedge!r} not in the anchor's paragraph")
    return problems


def check_pages(keys: set[str]) -> tuple[dict[str, str], list[str]]:
    pages: dict[str, str] = {}
    problems: list[str] = []
    for page in sorted(HISTORY.glob("*.md")):
        rel = str(page.relative_to(ROOT))
        text = page.read_text(encoding="utf-8")
        pages[rel] = text
        if page.name == "sources.md":
            continue
        min_deep = 0 if page.name == "index.md" else MIN_DEEP
        for p in check_refs.check(page, min_deep, keys):
            if min_deep == 0 and "Deep dive" in p:
                continue
            problems.append(f"{rel}: {p}")
    return pages, problems


def selftest() -> int:
    fails: list[str] = []
    page = (
        "Fab 2 ran S4AD-5 at 0.5 µm.[^a][^b]\n\n"
        "Cypress's reports give 110 Å of gate oxide.[^a][^c]\n\n"
        "The line was 0.35 µm (single source).[^a]\n\n"
        "| Code | Rule |\n|---|---|\n| X1 | 1 µm (single source)[^a] |\n| X2 | 2 µm[^b] |\n\n"
        "[^a]: A. <https://a.example/>\n[^b]: B. <https://b.example/>\n[^c]: C. <https://c.example/>\n"
    )
    pages = {"p.md": page}
    ids = {"r1", "r2", "r3"}
    ok = [
        {"id": "c1", "page": "p.md", "anchor": "Fab 2 ran S4AD-5", "grade": "corroborated", "footnotes": ["a", "b"],
         "sources": [{"id": "r1", "origin": "cypress"}, {"id": "r2", "origin": "eetimes"}]},
        {"id": "c2", "page": "p.md", "anchor": "110 Å of gate oxide", "grade": "attributed", "attribution": "Cypress's reports",
         "footnotes": ["a", "c"], "sources": [{"id": "r1", "origin": "cypress"}, {"id": "r3", "origin": "cypress"}]},
        {"id": "c3", "page": "p.md", "anchor": "0.35 µm", "grade": "single-source", "footnotes": ["a"],
         "sources": [{"id": "r1", "origin": "cypress"}]},
        {"id": "c4", "page": "p.md", "anchor": "| X1 |", "grade": "single-source", "footnotes": ["a"],
         "sources": [{"id": "r1", "origin": "cypress"}]},
    ]
    if (p := check_claims(ok, pages, ids)):
        fails.append(f"valid claims reported: {p}")
    bad = [
        {"id": "b1", "page": "p.md", "anchor": "Fab 2 ran S4AD-5", "grade": "corroborated", "footnotes": ["a"],
         "sources": [{"id": "r1", "origin": "cypress"}, {"id": "r3", "origin": "cypress"}]},
        {"id": "b2", "page": "p.md", "anchor": "| X2 |", "grade": "single-source", "footnotes": ["b"],
         "sources": [{"id": "r2", "origin": "eetimes"}]},
        {"id": "b3", "page": "p.md", "anchor": "not on the page", "grade": "corroborated", "footnotes": ["a"],
         "sources": [{"id": "r1", "origin": "x"}, {"id": "r2", "origin": "y"}]},
        {"id": "b4", "page": "p.md", "anchor": "110 Å", "grade": "attributed", "attribution": "SkyWater's",
         "footnotes": ["a"], "sources": [{"id": "r1", "origin": "cypress"}, {"id": "r9", "origin": "cypress"}]},
        {"id": "b5", "page": "p.md", "anchor": "Fab 2 ran S4AD-5", "grade": "corroborated", "footnotes": ["z"],
         "sources": [{"id": "r1", "origin": "x"}, {"id": "r2", "origin": "y"}]},
    ]
    p = check_claims(bad, pages, ids)
    for cid, needle in [("b1", "two different origins"), ("b2", "(single source)"), ("b3", "not found"),
                        ("b4", "attribution"), ("b4", "r9"), ("b5", "[^z]")]:
        if not any(f":{cid}:" in x and needle in x for x in p):
            fails.append(f"{cid}: expected a problem containing {needle!r}; got {p}")
    for f in fails:
        print("FAIL:", f)
    if not fails:
        print("selftest OK")
    return 1 if fails else 0


def main() -> int:
    if "--selftest" in sys.argv[1:]:
        return selftest()
    if not HISTORY.is_dir():
        print("no docs/history/ yet")
        return 0
    keys = inventory_keys(INVENTORY.read_text(encoding="utf-8")) if INVENTORY.exists() else set()
    pages, problems = check_pages(keys)
    claims = (yaml.safe_load(CLAIMS.read_text(encoding="utf-8")) or {}).get("claims", []) if CLAIMS.exists() else []
    problems += check_claims(claims, pages, evidence_ids())
    for p in problems:
        print(p)
    print(f"{len(pages)} history pages, {len(claims)} claims checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
