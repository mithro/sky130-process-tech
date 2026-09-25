#!/usr/bin/env python3
"""Measure a batch of step pages against the guide's own §1 caps (not the looser
"flag" thresholds `measure.py`'s summary prints): paragraph > 100 words, list item
(outside References) > 60 words, sentence > 45 words, table cell > 25 words.

Promoted from the round-1 review's `tmp/rev/caps.py` (review of `topic/rd-steps-001-013`,
2026-09-25, ruling D9): "measure against §1, not ad-hoc thresholds... after the last page
of a batch, run the measurement over the whole batch again and put the counts at the §1
caps in the progress file." This is that whole-batch re-check, cleaned up to be
self-contained (reuses `measure.py`'s own `clean`/`words`/`blocks`, in this same
directory, instead of a copy in `tmp/`) and to take an explicit page list instead of a
hardcoded 001-013 range, so it works for any batch.

Usage (run from the repository root, or copy this whole directory three levels below the
root first — see readability-guide.md §3, "Running the measurement scripts"):

    python3 docs/plans/readability/prototypes/measure/measure5.py docs/steps/00[1-9]-*.md docs/steps/01[0-3]-*.md
    python3 docs/plans/readability/prototypes/measure/measure5.py docs/steps/*.md   # whole site

With no paths, measures every `docs/steps/*.md`.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from measure import blocks, clean, words  # noqa: E402  (sibling prototype, see docstring)

ROOT = Path(__file__).resolve().parents[3]

_SENT_SPLIT_RE = re.compile(r'(?:(?<=[.!?])|(?<=[.!?]["”)]))\s+(?=[A-Z`*\[“"(])')


def sentences(block_text: str) -> list[str]:
    c = clean(" ".join(block_text.split()))
    return [s for s in _SENT_SPLIT_RE.split(c) if len(s.split()) >= 3]


def measure(paths: list[Path]) -> dict[str, int]:
    totals = {"para": 0, "item": 0, "sentence": 0, "cell": 0}
    for path in paths:
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"<!-- index-links:begin.*?index-links:end -->", "", text, flags=re.S)
        for sec, kind, body, lineno in blocks(text):
            if sec.startswith("References"):
                continue
            w = words(body)
            if kind == "para" and w > 100:
                totals["para"] += 1
                print(f"  PARA {w}w {path.name}:{lineno} [{sec}]")
            if kind == "item" and w > 60:
                totals["item"] += 1
                print(f"  ITEM {w}w {path.name}:{lineno} [{sec}]")
            if kind == "table":
                for row in body.split("\n"):
                    for cell in row.strip().strip("|").split("|"):
                        cw = words(cell)
                        if cw > 25:
                            totals["cell"] += 1
                            print(f"  CELL {cw}w {path.name}:{lineno} [{sec}] {cell.strip()[:60]!r}")
            if kind in ("para", "item"):
                for s in sentences(body):
                    sw = len(s.split())
                    if sw > 45:
                        totals["sentence"] += 1
                        print(f"  SENT {sw}w {path.name}:{lineno} [{sec}] {s[:80]!r}")
    return totals


def main() -> int:
    args = sys.argv[1:]
    if args:
        paths = sorted({p for a in args for p in (ROOT.glob(a) if not Path(a).is_absolute() else [Path(a)])})
        if not paths:
            # Argument may already be a path relative to CWD (shell-expanded globs land here).
            paths = sorted(Path(a) for a in args if Path(a).exists())
    else:
        paths = sorted((ROOT / "docs/steps").glob("*.md"))
    totals = measure(paths)
    print(
        f"{len(paths)} pages: "
        f"paragraphs > 100 words: {totals['para']}; "
        f"list items > 60 words: {totals['item']}; "
        f"sentences > 45 words: {totals['sentence']}; "
        f"table cells > 25 words: {totals['cell']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
