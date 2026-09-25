#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
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

Usage::

    uv run tools/check_history_quotes.py            # check every data/history/*.yaml
    uv run tools/check_history_quotes.py --selftest  # run the offline unit tests

Exit status is non-zero if any quote could not be verified or any document's
cache text is missing.
"""

from __future__ import annotations

import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
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

    for p in problems:
        print(f"PROBLEM: {p}")
    for m in missing_cache:
        print(f"NO CACHE: {m}")

    print(f"\n{len(checked)} quote(s) checked across {len(files)} file(s); "
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
