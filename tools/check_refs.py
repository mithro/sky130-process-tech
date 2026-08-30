#!/usr/bin/env python3
"""Check footnote citations and reference tiers on written pages.

Rules (see docs/plans/citation-style.md):

* every ``[^label]`` reference has a definition and vice versa;
* no reference-style link definitions (``[label]: url``) remain;
* a written step page has at least 8 Deep dive entries, a category page
  at least 12.

Stub pages (containing "This page is a stub.") are skipped.  Exit status
is non-zero on any violation.  Run with ``uv run tools/check_refs.py``.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

STUB_MARKER = "This page is a stub."
REF_RE = re.compile(r"\[\^([A-Za-z0-9][A-Za-z0-9_-]*)\](?!:)")
DEF_RE = re.compile(r"^\[\^([A-Za-z0-9][A-Za-z0-9_-]*)\]:", re.MULTILINE)
LINKDEF_RE = re.compile(r"^\[(?!\^)[^\]]+\]:\s*\S", re.MULTILINE)
BULLET_RE = re.compile(r"^\* ", re.MULTILINE)

TARGETS = [
    (DOCS / "steps", re.compile(r"^\d{3}-[a-z0-9-]+\.md$"), 8),
    (DOCS / "categories", re.compile(r"^(?!index)[a-z-]+\.md$"), 12),
]


def deep_dive_count(text: str) -> int:
    m = re.search(r"^### Deep dive\n(.*?)(?=^## |^### |\Z)", text, re.S | re.M)
    if not m:
        return -1
    return len(BULLET_RE.findall(m.group(1)))


def check(path: Path, min_deep: int) -> list[str]:
    text = path.read_text()
    problems: list[str] = []
    refs = set(REF_RE.findall(text))
    defs = DEF_RE.findall(text)
    dup = {d for d in defs if defs.count(d) > 1}
    defset = set(defs)
    if dup:
        problems.append(f"duplicate footnote definitions: {sorted(dup)}")
    if refs - defset:
        problems.append(f"undefined footnotes: {sorted(refs - defset)}")
    if defset - refs:
        problems.append(f"unreferenced footnotes: {sorted(defset - refs)}")
    if not refs:
        problems.append("no footnote citations")
    if LINKDEF_RE.search(text):
        problems.append("reference-style link definitions present")
    n = deep_dive_count(text)
    if n < 0:
        problems.append("no '### Deep dive' section")
    elif n < min_deep:
        problems.append(f"Deep dive has {n} entries (minimum {min_deep})")
    return problems


def main() -> int:
    bad = 0
    checked = 0
    for directory, pattern, min_deep in TARGETS:
        for page in sorted(directory.iterdir()):
            if not pattern.match(page.name):
                continue
            if STUB_MARKER in page.read_text():
                continue
            checked += 1
            problems = check(page, min_deep)
            if problems:
                bad += 1
                for p in problems:
                    print(f"{page.relative_to(ROOT)}: {p}")
    print(f"{checked} written pages checked, {bad} with problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
