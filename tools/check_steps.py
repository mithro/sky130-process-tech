#!/usr/bin/env python3
"""Check that every step page has the mandatory section headings.

Also reports pages that still carry the stub warning, so progress can be
tracked.  Exit status is non-zero when a page is missing a heading.

Run with ``uv run tools/check_steps.py``.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STEPS = ROOT / "docs" / "steps"

REQUIRED = [
    "## What this step is",
    "## Step category",
    "## Why this step exists",
    "## How it is typically performed",
    "## Machines typically used",
    "## Machines likely used at SkyWater",
    "## Resources required",
    "## Related steps and cross-references",
    "## References",
    "### Cross-check",
    "### High-level understanding",
    "### Deep dive",
    "## Open questions",
]

STUB_MARKER = "This page is a stub."
PAGE_RE = re.compile(r"^\d{3}-[a-z0-9-]+\.md$")


def main() -> int:
    pages = sorted(p for p in STEPS.iterdir() if PAGE_RE.match(p.name))
    if not pages:
        print("no step pages found", file=sys.stderr)
        return 1
    bad = 0
    stubs = 0
    for page in pages:
        text = page.read_text()
        missing = [h for h in REQUIRED if f"\n{h}\n" not in text]
        if missing:
            bad += 1
            print(f"{page.name}: missing {', '.join(missing)}")
        if STUB_MARKER in text:
            stubs += 1
    print(f"{len(pages)} pages, {len(pages) - stubs} written, {stubs} stubs, {bad} with missing headings")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
