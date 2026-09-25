#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6", "pymupdf"]
# ///
"""Check that every quote in ``data/history/*.yaml`` is verbatim.

The Cypress process-technology history (``docs/plans/cypress-history-plan.md``)
keeps its evidence as YAML files under ``data/history/`` (``qtp.yaml``, and in
future ``corporate.yaml``/``literature.yaml`` from the other two evidence
agents). Each file holds one or more lists of document records; a record that
carries a ``quotes`` list (each item ``{text, location}``) is checked here.

For every such quote this script confirms that ``text`` occurs, verbatim
after whitespace/hyphenation normalisation, in the *cached* extracted text of
that record's document -- never by fetching anything online, since the whole
point of the shared fetch cache (``tmp/cyhist-cache/`` in the *main* checkout,
common to every worktree) is that this check runs offline. A record's cache
file is found by its ``id``: every subdirectory of the cache is searched for
``<id>.txt`` (the ``pdftotext -layout`` extraction saved alongside the PDF).

**The pages' own quotations.** Every phrase in double quotes in the prose of
``docs/history/*.md`` (the generated ``stackups.md``, ``products.md`` and
``sources.md`` excepted) must occur, case- and whitespace-insensitively, in
the cached text of an evidence record that the same paragraph, list item or
table row cites -- or, for a block with no citation of its own, that the
nearest cited block above it in the same section cites. A phrase in an
uncited block (a summary table, say) is accepted when it is found in any
source the page cites. ``…`` splits a quotation into parts that must each be found;
``[…]`` marks an editorial insertion and is ignored. For a PDF, the text is
also re-extracted with pymupdf when the cached layout text interleaves table
columns. The link from a footnote to its record is the one
``tools/check_history.py`` enforces (the record's URL in the footnote).

Usage::

    uv run tools/check_history_quotes.py            # check every data/history/*.yaml and the pages
    uv run tools/check_history_quotes.py --selftest  # run the offline unit tests

Exit status is non-zero if any quote could not be verified or any document's
cache text is missing.
"""

from __future__ import annotations

import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parent
DATA_DIR = ROOT / "data" / "history"


def find_cache_root() -> Path:
    """The shared fetch cache lives at ``tmp/cyhist-cache`` in the *main*
    checkout, not in whichever worktree this script happens to run from
    (agent-briefs.md: "Shared fetch cache: tmp/cyhist-cache/ in the main
    checkout"). ``git rev-parse --git-common-dir`` resolves to the same path
    from any worktree sharing that checkout's .git, so its parent is the main
    checkout root regardless of where this script is invoked from. Falls
    back to ROOT/tmp/cyhist-cache (e.g. outside a worktree, or in a plain
    clone) when git is unavailable or the call fails.
    """
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "--git-common-dir"],
            capture_output=True, text=True, timeout=10, check=True,
        ).stdout.strip()
        common_dir = (ROOT / out).resolve() if not Path(out).is_absolute() else Path(out)
        return common_dir.parent / "tmp" / "cyhist-cache"
    except Exception:
        return ROOT / "tmp" / "cyhist-cache"


CACHE_ROOT = find_cache_root()

# Several PDFs in this corpus embed a Symbol-style font whose micron-sign
# glyph has no ToUnicode entry; pdftotext then emits a Private Use Area
# codepoint instead of U+00B5. Checked byte-for-byte against each PDF's own
# text (not merely assumed): U+F06D in qtp-021507, qtp-061806, qtp-072002,
# qtp-097483 and qtp-113005; U+F0B0 in qtp-024110, qtp-097476 and qtp-098368;
# U+F0B5 in qtp-151005 -- three different codepoints depending on which
# Infineon reissue template embedded the document, all standing in for the
# same "µ" in a "Generic Process Technology/Design Rule (µ-drawn)" field or a
# design-rule value ("0.09µm"). Mapped here, not silently dropped, so a quote
# can still say "µm" and be found verbatim in that document's cache.
PUA_MICRON_SIGNS = {"": "µ", "": "µ", "": "µ"}


def tidy(t: str) -> str:
    """NFKC-normalise (expands ligatures: 'ﬁ' -> 'fi') and map known broken
    micron-sign glyphs, without changing case or removing whitespace. The PUA
    substitution runs *before* NFKC (not after): NFKC's own compatibility
    mapping turns an ordinary U+00B5 MICRO SIGN into U+03BC GREEK SMALL LETTER
    MU, so normalising first and substituting after would leave a
    real-micron-sign quote (through NFKC) and a substituted-PUA-sign quote
    (skipping it) at two different final codepoints for what should compare
    equal."""
    for pua, real in PUA_MICRON_SIGNS.items():
        t = t.replace(pua, real)
    t = unicodedata.normalize("NFKC", t)
    t = t.replace(" ", " ")
    return t


def normalise(t: str) -> str:
    """Whitespace- and hyphenation-insensitive comparison key. PDF text
    extraction inserts or drops spaces and hyphenates words split across a
    justified line break (e.g. "Bloom- ington"), so both whitespace and
    hyphens are stripped entirely before comparing. Case-sensitive: a
    mis-cased "quotation" should not silently pass as verbatim."""
    t = tidy(t)
    return "".join(ch for ch in t if not ch.isspace() and ch not in "-‐‑‒–—")


def find_cache_text(doc_id: str) -> Path | None:
    if not CACHE_ROOT.is_dir():
        return None
    matches = sorted(CACHE_ROOT.glob(f"*/{doc_id}.txt"))
    if not matches:
        matches = sorted(CACHE_ROOT.glob(f"{doc_id}.txt"))
    return matches[0] if matches else None


def iter_quoted_records(doc: object, path_hint: str = ""):
    """Yield (record, path_hint) for every dict in ``doc`` that has a
    ``quotes`` list, recursing into any list or dict value -- so this works
    whether a history file's records sit under ``documents:``, ``filings:``,
    a nested ``about.quotes`` shape, or anything else a sibling evidence file
    (corporate.yaml, literature.yaml) turns out to use."""
    if isinstance(doc, dict):
        if isinstance(doc.get("quotes"), list):
            yield doc, path_hint
        for k, v in doc.items():
            yield from iter_quoted_records(v, f"{path_hint}.{k}" if path_hint else str(k))
    elif isinstance(doc, list):
        for i, item in enumerate(doc):
            yield from iter_quoted_records(item, f"{path_hint}[{i}]")


def check_file(path: Path, problems: list[str], checked: list[str], missing_cache: list[str]) -> None:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    for record, path_hint in iter_quoted_records(data):
        rid = record.get("id") or path_hint
        quotes = record["quotes"]
        if not isinstance(quotes, list) or not quotes:
            # every evidence record must carry at least one verified quotation
            problems.append(f"{path.name}:{rid}: no quotes")
            continue
        cache_file = None
        if record.get("cache"):
            candidate = CACHE_ROOT / str(record["cache"])
            cache_file = candidate if candidate.is_file() else None
        if cache_file is None:
            cache_file = find_cache_text(str(rid))
        if cache_file is None:
            missing_cache.append(f"{path.name}:{rid}: no cached text found under {CACHE_ROOT} (looked for */{rid}.txt)")
            continue
        raw_text = normalise(cache_file.read_text(encoding="utf-8", errors="replace"))
        for i, q in enumerate(quotes):
            if not isinstance(q, dict) or "text" not in q:
                problems.append(f"{path.name}:{rid}: quotes[{i}] is not a {{text, location}} mapping")
                continue
            text = q["text"]
            if not isinstance(text, str) or not text.strip():
                problems.append(f"{path.name}:{rid}: quotes[{i}].text is empty")
                continue
            if not q.get("location"):
                problems.append(f"{path.name}:{rid}: quotes[{i}] has no location")
            needle = normalise(text)
            checked.append(f"{path.name}:{rid}:quotes[{i}]")
            if not needle or needle not in raw_text:
                problems.append(
                    f"{path.name}:{rid}: quotes[{i}].text not found verbatim (normalised) in "
                    f"{cache_file.relative_to(CACHE_ROOT.parent) if CACHE_ROOT in cache_file.parents else cache_file}: "
                    f"{text[:80]!r}"
                )


PAGE_EXEMPT = {"stackups.md", "products.md", "sources.md"}
# The section's own labels, written in quotes on the pages that explain them.
OWN_PHRASES = {"single source", "(single source)", "cypress's reports", "our reading", "our arithmetic"}
QUOTE_MARKS = str.maketrans("", "", "'\"’‘“”")


def page_key(t: str) -> str:
    """Case-insensitive, and blind to quotation marks and apostrophes, whose style differs between a
    source and the page quoting it."""
    return normalise(t.translate(QUOTE_MARKS)).lower()


def page_quotations(block: str) -> list[str]:
    parts = block.split('"')
    return [parts[i] for i in range(1, len(parts) - 1, 2)]


def record_texts() -> dict[str, list[Path]]:
    """Evidence record id -> the files holding its text: the cached text, and the original PDF."""
    out: dict[str, list[Path]] = {}
    for path in sorted(DATA_DIR.glob("*.yaml")):
        if path.name == "claims.yaml":
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for rec, _ in iter_quoted_records(data):
            rid = str(rec.get("id") or "")
            text = CACHE_ROOT / str(rec["cache"]) if rec.get("cache") else find_cache_text(rid)
            if not rid or not text or not Path(text).is_file():
                continue
            files = [Path(text)]
            pdf = Path(text).with_name(Path(text).name.split(".")[0] + ".pdf")
            if pdf.is_file():
                files.append(pdf)
            out[rid] = files
    return out


_TEXT_CACHE: dict[Path, str] = {}


def file_key(path: Path) -> str:
    if path not in _TEXT_CACHE:
        if path.suffix == ".pdf":
            import pymupdf
            with pymupdf.open(path) as doc:
                raw = "\n".join(page.get_text() for page in doc)
        else:
            raw = path.read_text(encoding="utf-8", errors="replace")
        _TEXT_CACHE[path] = page_key(raw)
    return _TEXT_CACHE[path]


def quote_found(quote: str, files: list[Path]) -> bool:
    q = re.sub(r"\[[^\]]*\]", "", quote)
    pieces = [page_key(x) for x in re.split(r"…|\.\.\.", q) if x.strip()]
    return bool(pieces) and any(all(pc in file_key(f) for pc in pieces) for f in files)


def check_page_quotes(problems: list[str]) -> int:
    import check_history as ch  # same directory; the footnote-to-record links it enforces

    pages = {str(p.relative_to(ROOT)): p.read_text(encoding="utf-8") for p in sorted((ROOT / "docs" / "history").glob("*.md"))}
    links = ch.evidence_links()
    labels = ch.footnote_links(pages)
    texts = record_texts()
    count = 0
    for rel, text in pages.items():
        if Path(rel).name in PAGE_EXEMPT:
            continue
        body = text.split("\n## References")[0]
        verified: set[str] = set()
        pending: list[str] = []
        last: set[str] = set()
        for block in ch.blocks(body):
            if block.lstrip().startswith("#"):
                last = set()
                continue
            fns = set(re.findall(r"\[\^([^\]]+)\]", block))
            scope = fns or last
            if fns:
                last = fns
            quotes = [q for q in page_quotations(block) if len(q.strip()) >= 2 and q.strip().lower() not in OWN_PHRASES]
            if not quotes:
                continue
            files = [f for rid, keys in links.items() if rid in texts and any(labels.get(fn, set()) & keys for fn in scope)
                     for f in texts[rid]]
            for q in quotes:
                count += 1
                if files and quote_found(q, files):
                    verified.add(page_key(q))
                elif not scope:
                    pending.append(q)
                else:
                    problems.append(f"{rel}: quotation not found in the cited sources {sorted(scope)}: {q[:80]!r}")
        page_fns = set(re.findall(r"\[\^([^\]]+)\]", body))
        page_files = [f for rid, keys in links.items() if rid in texts and any(labels.get(fn, set()) & keys for fn in page_fns)
                      for f in texts[rid]]
        for q in pending:
            if page_key(q) not in verified and not quote_found(q, page_files):
                problems.append(f"{rel}: quotation in an uncited block, not found in any source the page cites: {q[:80]!r}")
    return count


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()

    if not DATA_DIR.is_dir():
        print(f"no {DATA_DIR} directory found", file=sys.stderr)
        return 1

    files = sorted(DATA_DIR.glob("*.yaml"))
    if not files:
        print(f"no *.yaml files under {DATA_DIR}", file=sys.stderr)
        return 1

    problems: list[str] = []
    checked: list[str] = []
    missing_cache: list[str] = []
    for path in files:
        check_file(path, problems, checked, missing_cache)
    page_count = check_page_quotes(problems)

    for p in problems:
        print(f"PROBLEM: {p}")
    for m in missing_cache:
        print(f"NO CACHE: {m}")

    print(f"\n{len(checked)} quote(s) checked across {len(files)} file(s), and {page_count} quotation(s) "
          f"on the history pages; "
          f"cache root: {CACHE_ROOT}")
    print(f"{len(problems)} problem(s), {len(missing_cache)} record(s) with no cached text.")

    return 1 if (problems or missing_cache) else 0


def selftest() -> int:
    assert normalise("Bloom-\ning ton") == normalise("Blooming ton") == normalise("Bloomington")
    assert normalise("CMOS, Double Metal, 0.09m") == normalise("CMOS, Double Metal, 0.09µm")
    assert normalise("reﬁnement") == normalise("refinement")  # ligature fi
    assert normalise("Fab") != normalise("fab")  # case-sensitive
    assert normalise("Fab 2") == normalise("Fab 2")  # nbsp

    class FakeDict(dict):
        pass

    doc = {"documents": [{"id": "x-1", "quotes": [{"text": "Hello world", "location": "p.1"}]}]}
    found = list(iter_quoted_records(doc))
    assert len(found) == 1 and found[0][0]["id"] == "x-1"

    print("selftest OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
