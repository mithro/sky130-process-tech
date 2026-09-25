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
  contains the claim's ``hedge`` phrase (how the page states the conflict);
* ``grade: inference`` is this reference's reading of other claims; its
  paragraph must carry the claim's ``hedge``, "our reading", "our arithmetic"
  or "our inference".

**Links between footnotes and evidence.** A claim is only as good as the
reader's ability to find its sources, so the footnotes the reader sees and
the evidence records the matrix counts must be the same documents:

* every footnote defined on a history page must point at an evidence
  record: its definition must carry the record's ``url`` or
  ``archive_url`` (for a filing, one of its ``urls``; for a patent family,
  one of its patent numbers);
* in every claim, each source must be one of the documents the claim's
  footnotes point at, and each of the claim's footnotes must point at one
  of its sources. A source the paragraph does not cite, or a footnote no
  source stands behind, is an error.

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
GRADES = {"corroborated", "attributed", "single-source", "conflict", "inference"}
SINGLE_TAG = "(single source)"


def inventory_keys(text: str) -> set[str]:
    return {k.lower() for k in check_refs.KEY_RE.findall(text)}


def evidence_ids() -> dict[str, str]:
    """Evidence record id -> the record's origin (the organisation it comes from).

    Records in ``data/history/*.yaml`` carry a fixed ``origin``. The site's verified datasets
    may also be cited: a filing's origin is its company, a patent family's is the patent record,
    a paper's is the paper itself."""
    ids: dict[str, str] = {}
    for path in sorted(DATA.glob("*.yaml")):
        if path == CLAIMS:
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for key in ("documents", "records"):
            for rec in doc.get(key, []) or []:
                if isinstance(rec, dict) and rec.get("id"):
                    ids[str(rec["id"])] = str(rec.get("origin") or "")
    for name, key in (("filings.yaml", "filings"), ("patents.yaml", "families"), ("papers.yaml", "papers")):
        path = ROOT / "data" / name
        if not path.exists():
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for rec in (doc if isinstance(doc, list) else doc.get(key, []) or []):
            if isinstance(rec, dict) and rec.get("id"):
                origin = {"filings.yaml": str(rec.get("company_key") or "filing"),
                          "patents.yaml": "patent-record", "papers.yaml": f"paper:{rec['id']}"}[name]
                ids[str(rec["id"])] = origin
    return ids


DEF_RE = re.compile(r"(?m)^\[\^([^\]\s]+)\]:(.*(?:\n    .*)*)")
URL_RE = re.compile(r"https?://[^\s<>)\]]+")
PATENT_RE = re.compile(r"\b(US\d{7,8}[AB]\d?)\b", re.I)


def link_keys(text: str) -> set[str]:
    """The documents a piece of text points at: URLs with the scheme and any Wayback prefix
    removed, and US patent numbers."""
    keys: set[str] = set()
    for url in URL_RE.findall(text):
        u = url.strip().rstrip(".,;'\"")
        for _ in range(2):
            u = re.sub(r"^https?://", "", u)
            u = re.sub(r"^web\.archive\.org/web/\d+(?:id_)?/", "", u)
        keys.add(u.rstrip("/").lower())
    keys |= {"patent:" + p.upper() for p in PATENT_RE.findall(text)}
    return keys


def _strings(x: object):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from _strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from _strings(v)


def evidence_links() -> dict[str, set[str]]:
    """Evidence record id -> the documents it is about (see ``link_keys``)."""
    links: dict[str, set[str]] = {}
    for path in sorted(DATA.glob("*.yaml")):
        if path == CLAIMS:
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for key in ("documents", "records"):
            for rec in doc.get(key, []) or []:
                if isinstance(rec, dict) and rec.get("id"):
                    links[str(rec["id"])] = set().union(
                        *(link_keys(str(rec[k])) for k in ("url", "archive_url") if rec.get(k)))
    for name, key in (("filings.yaml", "filings"), ("patents.yaml", "families")):
        path = ROOT / "data" / name
        if not path.exists():
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for rec in (doc if isinstance(doc, list) else doc.get(key, []) or []):
            if not isinstance(rec, dict) or not rec.get("id"):
                continue
            if name == "patents.yaml":
                nums = [rec.get("representative") or ""] + [
                    (m.get("number") or "") if isinstance(m, dict) else str(m) for m in rec.get("members") or []]
                links[str(rec["id"])] = {"patent:" + n.upper() for n in nums if n}
            else:
                links[str(rec["id"])] = set().union(*(link_keys(s) for s in _strings(rec.get("urls"))))
    return links


def footnote_links(pages: dict[str, str]) -> dict[str, set[str]]:
    """Footnote label -> the documents its definitions point at, over all history pages."""
    out: dict[str, set[str]] = {}
    for rel, text in pages.items():
        if rel.endswith("/sources.md"):
            continue
        for m in DEF_RE.finditer(text):
            out.setdefault(m.group(1), set()).update(link_keys(m.group(2)))
    return out


def check_links(claims: list[dict], pages: dict[str, str], links: dict[str, set[str]]) -> list[str]:
    problems: list[str] = []
    labels = footnote_links(pages)
    for label in sorted(labels):
        if not any(labels[label] & keys for keys in links.values()):
            problems.append(f"footnote [^{label}] points at no evidence record in data/history/ or "
                            f"data/{{filings,patents}}.yaml")
    for c in claims:
        where = f"claims.yaml:{c.get('id', '?')}"
        footnotes = c.get("footnotes") or []
        covered: set[str] = set()
        for s in c.get("sources") or []:
            if not isinstance(s, dict) or s.get("id") not in links:
                continue
            hits = [fn for fn in footnotes if labels.get(fn, set()) & links[s["id"]]]
            if not hits:
                problems.append(f"{where}: source {s['id']!r} is not the document of any of the claim's "
                                f"footnotes {footnotes}; cite it in the paragraph or drop it")
            covered.update(hits)
        for fn in footnotes:
            if fn in labels and fn not in covered:
                problems.append(f"{where}: footnote [^{fn}] has no source in the claim; add its evidence record")
    return problems


ITEM_RE = re.compile(r"^\s*(?:[*-]|\d+\.)\s")


def blocks(text: str) -> list[str]:
    """Paragraphs, list items and table rows: the units a hedge or a citation must share with
    the claim it qualifies."""
    out: list[str] = []
    for block in re.split(r"\n\s*\n", text):
        lines = block.splitlines()
        if block.lstrip().startswith("|"):
            # a table row is read with its header row
            header = lines[0] if lines else ""
            out += [lines[0]] + [f"{header}\n{ln}" for ln in lines[2:]] if len(lines) > 2 else lines
            continue
        cur: list[str] = []
        for ln in lines:
            if ITEM_RE.match(ln) and cur:
                out.append("\n".join(cur))
                cur = []
            cur.append(ln)
        if cur:
            out.append("\n".join(cur))
    return out


def paragraph_of(text: str, anchor: str) -> str | None:
    """The paragraph, list item or table row that contains ``anchor``, whitespace-normalised;
    None if absent."""
    flat_anchor = " ".join(anchor.split())
    bl = blocks(text)
    for i, block in enumerate(bl):
        flat = " ".join(block.split())
        if flat_anchor in flat:
            if flat.endswith(":"):
                # a lead-in and the list it introduces are one statement
                for nxt in bl[i + 1:]:
                    if not ITEM_RE.match(nxt):
                        break
                    flat += " " + " ".join(nxt.split())
            return flat
    return None


# What may count as an attribution (it must name who says it) and as a single-source or
# conflict hedge (it must say so), so that a phrase such as "See" cannot pass.
ATTRIBUTIONS = ("Cypress", "EE Times", "EDN", "Electronics Weekly", "Semiconductor Digest", "Star Tribune",
                "SkyWater", "Infineon", "Gale", "FundingUniverse", "Connect CRE", "Wikipedia", "patent records")
SINGLE_HEDGES = ("(single source)", "single source", "one report", "one article")
CONFLICT_HEDGES = ("disagree", "conflict", "differ", "not reconciled")
INFERENCE_HEDGES = ("our reading", "our arithmetic", "our inference")


def check_claims(claims: list[dict], pages: dict[str, str], ids: dict[str, str]) -> list[str]:
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
                problems.append(f"{where}: source {s['id']!r} is not an evidence record")
            elif ids[s["id"]] and s["origin"] != ids[s["id"]]:
                problems.append(f"{where}: source {s['id']!r} has origin {ids[s['id']]!r} in the "
                                f"evidence file, not {s['origin']!r}")
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
        footnotes = c.get("footnotes") or []
        if not footnotes:
            problems.append(f"{where}: no footnotes listed")
        in_para = set(check_refs.REF_RE.findall(para))
        for fn in footnotes:
            if fn not in in_para:
                problems.append(f"{where}: footnote [^{fn}] is not cited in the claim's paragraph")
        if grade == "corroborated":
            if len(origins) < 2:
                problems.append(f"{where}: corroborated needs two different origins, has {sorted(map(str, origins))}")
            if len(set(footnotes)) < 2:
                problems.append(f"{where}: corroborated needs two sources cited in the paragraph")
        if grade in ("attributed", "conflict") and len(sources) < 2:
            problems.append(f"{where}: {grade} needs at least two sources")
        if grade == "attributed":
            phrase = c.get("attribution") or ""
            if not phrase or phrase not in para:
                problems.append(f"{where}: attribution {phrase!r} not in the anchor's paragraph")
            elif not any(a.lower() in phrase.lower() for a in ATTRIBUTIONS):
                problems.append(f"{where}: attribution {phrase!r} does not name who says it")
        if grade == "single-source":
            if len(sources) != 1:
                problems.append(f"{where}: single-source claim lists {len(sources)} sources")
            hedge = c.get("hedge") or SINGLE_TAG
            if hedge not in para:
                problems.append(f"{where}: {hedge!r} not in the anchor's paragraph")
            elif not any(h in hedge for h in SINGLE_HEDGES):
                problems.append(f"{where}: hedge {hedge!r} does not say the claim has one source")
        if grade == "conflict":
            hedge = c.get("hedge") or ""
            if not hedge or hedge not in para:
                problems.append(f"{where}: conflict hedge {hedge!r} not in the anchor's paragraph")
            elif not any(h in hedge for h in CONFLICT_HEDGES):
                problems.append(f"{where}: conflict hedge {hedge!r} does not say the sources disagree")
        if grade == "inference":
            hedge = c.get("hedge") or ""
            if not hedge or hedge not in para:
                problems.append(f"{where}: inference hedge {hedge!r} not in the anchor's paragraph")
            elif not any(h in hedge.lower() for h in INFERENCE_HEDGES):
                problems.append(f"{where}: inference hedge {hedge!r} does not mark the claim as our reading")
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
    ids = {"r1": "cypress", "r2": "eetimes", "r3": "cypress"}
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
    bad += [
        {"id": "b6", "page": "p.md", "anchor": "Fab 2 ran S4AD-5", "grade": "corroborated", "footnotes": ["a", "b"],
         "sources": [{"id": "r1", "origin": "cypress"}, {"id": "r2", "origin": "ew"}]},
        {"id": "b7", "page": "p.md", "anchor": "110 Å of gate oxide", "grade": "attributed", "attribution": "give",
         "footnotes": ["a", "c"], "sources": [{"id": "r1", "origin": "cypress"}, {"id": "r3", "origin": "cypress"}]},
    ]
    p = check_claims(bad, pages, ids)
    for cid, needle in [("b1", "two different origins"), ("b2", "(single source)"), ("b3", "not found"),
                        ("b4", "attribution"), ("b4", "r9"), ("b5", "[^z]"),
                        ("b6", "has origin"), ("b7", "does not name")]:
        if not any(f":{cid}:" in x and needle in x for x in p):
            fails.append(f"{cid}: expected a problem containing {needle!r}; got {p}")
    links = {"r1": {"a.example"}, "r2": {"b.example"}, "r3": {"c.example"}}
    if (p := check_links(ok, pages, links)):
        fails.append(f"valid links reported: {p}")
    linkbad = [
        {"id": "l1", "page": "p.md", "anchor": "0.35 µm", "grade": "single-source", "footnotes": ["a"],
         "sources": [{"id": "r3", "origin": "cypress"}]},
        {"id": "l2", "page": "p.md", "anchor": "Fab 2 ran S4AD-5", "grade": "corroborated", "footnotes": ["a", "b"],
         "sources": [{"id": "r1", "origin": "cypress"}]},
    ]
    p = check_links(linkbad, pages, links)
    for cid, needle in [("l1", "'r3' is not the document"), ("l1", "[^a] has no source"), ("l2", "[^b] has no source")]:
        if not any(f":{cid}:" in x and needle in x for x in p):
            fails.append(f"{cid}: expected a link problem containing {needle!r}; got {p}")
    p = check_links([], {"p.md": page + "[^d]: D. <https://d.example/>\n"}, links)
    if not any("[^d] points at no evidence record" in x for x in p):
        fails.append(f"orphan footnote not reported: {p}")
    if link_keys("x <https://web.archive.org/web/2020id_/https://A.example/f/>") != {"a.example/f"}:
        fails.append("link_keys does not strip the Wayback prefix")
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
    problems += check_links(claims, pages, evidence_links())
    for p in problems:
        print(p)
    print(f"{len(pages)} history pages, {len(claims)} claims checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
