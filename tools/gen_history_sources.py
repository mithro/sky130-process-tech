#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Generate ``docs/history/sources.md``, the history section's source inventory.

The inventory lists every source cited on the ``docs/history/`` pages, one
entry per footnote label, in the layout of ``docs/references/public-sources.md``:
an anchor line ``(hsrc-<label>)=``, then ``**LABEL** —`` and the citation,
then the pages that cite it. It is built from the pages' own footnote
definitions, so it cannot drift from them. A label that two pages define
with different text is an error: a source keeps one citation across the
section.

Run ``uv run tools/gen_history_sources.py`` to write the file and
``--check`` to fail if it is out of date (used by the hosted build).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HISTORY = ROOT / "docs" / "history"
OUT = HISTORY / "sources.md"
DEF_START = re.compile(r"^\[\^([A-Za-z0-9][A-Za-z0-9_-]*)\]:\s?(.*)$")
LABEL_RE = re.compile(r"^\(([a-z0-9-]+)\)=\s*$", re.M)
FLAG_RE = re.compile(r"Shown as in force; estimated expiry|Status shown as unknown; estimated expiry")

HEADER = """(history-sources)=
# Sources for the Cypress history

Every source cited in this section, with the full citation and the pages that cite it. The list is
generated from the pages' footnotes by `tools/gen_history_sources.py`; edit the page, not this file.
The SKY130 reference keeps its own list, {ref}`references-index`.
"""


def footnotes(text: str) -> dict[str, str]:
    """label -> definition text (continuation lines joined by single spaces)."""
    defs: dict[str, str] = {}
    current: str | None = None
    for line in text.splitlines():
        m = DEF_START.match(line)
        if m:
            current = m.group(1)
            defs[current] = m.group(2).strip()
        elif current and line.startswith("    ") and line.strip():
            defs[current] += " " + line.strip()
        else:
            current = None
    return defs


def build() -> tuple[str, list[str]]:
    errors: list[str] = []
    entries: dict[str, str] = {}
    used_on: dict[str, list[str]] = {}
    for page in sorted(HISTORY.glob("*.md")):
        if page == OUT:
            continue
        text = page.read_text(encoding="utf-8")
        m = LABEL_RE.search(text)
        ref = m.group(1) if m else None
        if ref is None:
            errors.append(f"{page.relative_to(ROOT)}: no page label")
            continue
        for label, definition in footnotes(text).items():
            if label in entries and entries[label] != definition:
                errors.append(
                    f"[^{label}] is defined differently on {page.relative_to(ROOT)} and on "
                    f"{', '.join(used_on[label])}"
                )
            entries.setdefault(label, definition)
            used_on.setdefault(label, []).append(ref)
    parts = [HEADER]
    restricted: list[str] = []
    for label in sorted(entries):
        pages = ", ".join(f"{{ref}}`{r}`" for r in used_on[label])
        entry = f"(hsrc-{label})=\n**{label.upper()}** — {entries[label]}\nUsed on {pages}.\n"
        # A patent not certainly expired stays behind a collapsed block
        # (tools/check_inforce.py); its footnote carries the flag sentence.
        if FLAG_RE.search(entries[label]):
            restricted.append(entry)
        else:
            parts.append(entry)
    if restricted:
        parts.append(":::{dropdown} Patents shown as in force or of unknown status — open to read\n\n"
                     + "\n".join(restricted) + ":::\n")
    return "\n".join(parts), errors


def main() -> int:
    text, errors = build()
    for e in errors:
        print(e)
    if errors:
        return 1
    if "--check" in sys.argv[1:]:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print(f"{OUT.relative_to(ROOT)} is out of date; run uv run tools/gen_history_sources.py")
            return 1
        print(f"{OUT.relative_to(ROOT)} is up to date")
        return 0
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
