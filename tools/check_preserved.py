#!/usr/bin/env python3
"""Check that a readability edit preserved every fact, number, quotation,
hedge and citation on a page (docs/plans/readability-plan.md W0;
docs/plans/readability/report-A.md, "Acceptance check, every page";
report-B.md section 3 item 4).

Compares each page under ``docs/`` (outside ``docs/plans``) between a base
git revision and the working tree, and reports, per page, anything **LOST**
or **ADDED** in six categories:

1. ``markers`` — the multiset of footnote markers (``[^label]``) in the
   body, and ``footnotes`` — the set of footnote definitions, each with its
   full (whitespace-normalised) text.
2. ``numbers`` — the multiset of numeric tokens: digits with decimal
   points, thin-space/normal-space/comma thousands separators, ``x10``
   exponents and Unicode superscripts, signs and ranges. Only whitespace is
   normalised; nothing else about a number is touched or interpreted.
3. ``quotes`` — the multiset of quoted strings (straight ``"..."`` and
   curly “...”), whitespace-normalised.
4. ``refs`` — the multiset of ``{ref}``/``{term}``/``{doc}`` targets, and
   ``urls`` — the multiset of URLs written anywhere on the page.
5. ``hedges`` — counts of the hedge phrases in HEDGES below (e.g. "about",
   "typical", "our reading", "~").
6. The text inside every ``{dropdown}`` block, which must be unchanged
   apart from whitespace and list/table markup, unless
   ``--allow-dropdown-edits`` is given. This is not one of the seven
   categories above and has no ``--allow-added`` equivalent: a dropdown
   either passes unedited, or the whole check is disabled for the run.

A **loss** in any category is always an error. An **addition** is an error
unless its category is named in ``--allow-added`` (comma-separated); every
addition is printed either way, so the coordinator can see what changed
even when it was declared. Exit status is 1 if any undeclared difference
(a loss, or an addition outside ``--allow-added``, or a changed dropdown)
was found on any checked page.

Usage::

    uv run python tools/check_preserved.py [--base main] \\
        [--allow-added markers,footnotes,numbers,quotes,refs,urls,hedges] \\
        [--allow-dropdown-edits] [paths ...]

With no ``paths``, every ``docs/**/*.md`` file outside ``docs/plans`` that
differs between ``--base`` and the working tree (tracked changes and new,
not-yet-committed files alike) is checked. A file passed explicitly is
always checked, whether or not it differs from ``--base``. A page that does
not exist at ``--base`` (a genuinely new page) is reported and skipped: it
has nothing to compare against.

Run ``uv run python tools/check_preserved.py --selftest`` to run the
built-in self-tests (touches no files, needs no git history):
paragraph splits, a sentence moved between sections, and prose turned into
a table with the same values all pass; a dropped footnote marker, a
changed number, a dropped hedge, an altered quotation and text moved out
of a dropdown all fail.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_inforce  # noqa: E402  (for its {dropdown} fence parser)

# ---------------------------------------------------------------------------
# Extraction patterns.

DEF_RE = re.compile(
    r"^\[\^([A-Za-z0-9][A-Za-z0-9_-]*)\]:(.*?)(?=^\[\^[A-Za-z0-9_-]+\]:|\Z)",
    re.MULTILINE | re.DOTALL,
)
MARKER_RE = re.compile(r"\[\^([A-Za-z0-9][A-Za-z0-9_-]*)\](?!:)")
ROLE_RE = re.compile(r"\{(?:ref|term|doc)\}`([^`]+)`")
URL_RE = re.compile(r"https?://[^\s<>\)\]\"'`]+")
QUOTE_RE = re.compile(r'"([^"\n]{1,200})"|“([^”\n]{1,200})”')

_SIGN = r"[+\-−±]"
_SUP_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹"
_SUP_CLASS = rf"[{_SUP_DIGITS}⁻⁺]"
_GROUPED = r"\d{1,3}(?:[,   ]\d{3})+"
_PLAIN = r"\d+"
_INT = rf"(?:{_GROUPED}|{_PLAIN})"
_DEC = r"(?:\.\d+)?"
_NUM = rf"{_INT}{_DEC}"
_EXP = rf"(?:\s?[×x]\s?10(?:\^-?\d+|{_SUP_CLASS}+))?"
_CORE = rf"{_SIGN}?{_NUM}{_EXP}"
_DASH = r"\s?[-–—]\s?"
NUMBER_RE = re.compile(rf"{_CORE}(?:{_DASH}{_CORE})*")
SUP_STANDALONE_RE = re.compile(rf"{_SUP_CLASS}+")

# Hedge phrases (docs/plans/readability-plan.md W0b / report-A "hedges").
HEDGES = [
    "not public", "we infer", "inference", "our reading", "our arithmetic",
    "our extraction", "our estimate", "typical", "industry-typical",
    "industry-generic", "plausibly", "presumably", "probably", "may",
    "might", "about", "approximately", "~", "≈",
]


def _hedge_pattern(phrase: str) -> re.Pattern:
    if phrase in ("~", "≈"):
        return re.compile(re.escape(phrase))
    return re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)


HEDGE_PATTERNS = [(h, _hedge_pattern(h)) for h in HEDGES]

CATEGORIES = ["markers", "footnotes", "numbers", "quotes", "refs", "urls", "hedges"]


def normalize_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def role_target(content: str) -> str:
    content = content.strip()
    m = re.search(r"<([^<>]+)>\s*$", content)
    if m:
        return m.group(1).strip()
    return content


def extract_numbers(text: str) -> Counter:
    spans: list[tuple[int, int, str]] = []
    for m in NUMBER_RE.finditer(text):
        spans.append((m.start(), m.end(), m.group(0)))
    for m in SUP_STANDALONE_RE.finditer(text):
        if not any(m.start() < e and m.end() > s for s, e, _ in spans):
            spans.append((m.start(), m.end(), m.group(0)))
    return Counter(normalize_ws(t) for _, _, t in spans if normalize_ws(t))


def extract_quotes(text: str) -> Counter:
    out = []
    for m in QUOTE_RE.finditer(text):
        inner = m.group(1) if m.group(1) is not None else m.group(2)
        out.append(normalize_ws(inner))
    return Counter(q for q in out if q)


def extract_hedges(text: str) -> Counter:
    c: Counter = Counter()
    for phrase, pat in HEDGE_PATTERNS:
        n = len(pat.findall(text))
        if n:
            c[phrase] = n
    return c


def extract_all(text: str) -> dict[str, Counter]:
    defs: dict[str, str] = {}
    for label, body in DEF_RE.findall(text):
        defs[label] = normalize_ws(body)
    body_text = DEF_RE.sub("", text)

    markers = Counter(MARKER_RE.findall(body_text))

    refs: Counter = Counter()

    def _role_sub(m: re.Match) -> str:
        refs[role_target(m.group(1))] += 1
        return " "

    masked = ROLE_RE.sub(_role_sub, body_text)
    urls = Counter(URL_RE.findall(masked))
    masked = URL_RE.sub(" ", masked)
    masked = MARKER_RE.sub(" ", masked)

    numbers = extract_numbers(masked)
    quotes = extract_quotes(masked)
    hedges = extract_hedges(masked)
    footnotes = Counter(f"[^{label}]: {text}" for label, text in defs.items())

    return {
        "markers": markers,
        "footnotes": footnotes,
        "numbers": numbers,
        "quotes": quotes,
        "refs": refs,
        "urls": urls,
        "hedges": hedges,
    }


# ---------------------------------------------------------------------------
# {dropdown} block comparison.


def _dropdown_body_text(lines: list[str], body_lines: set[int]) -> str:
    kept = []
    for lineno in sorted(body_lines):
        line = lines[lineno - 1]
        if check_inforce.FENCE_OPEN_RE.match(line) or check_inforce.FENCE_BARE_RE.match(line):
            continue
        if re.match(r"^\s*\|?[\s:|-]+\|?\s*$", line):
            continue  # a table separator row, e.g. "|---|:--|"
        line = line.replace("|", " ")
        line = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line)
        kept.append(line)
    return normalize_ws(" ".join(kept))


def compare_dropdowns(old_text: str, new_text: str) -> list[str]:
    old_blocks = check_inforce.dropdown_blocks(old_text)
    new_blocks = check_inforce.dropdown_blocks(new_text)
    old_lines = old_text.splitlines()
    new_lines = new_text.splitlines()
    problems = []
    if len(old_blocks) != len(new_blocks):
        problems.append(
            f"{{dropdown}} block count changed: {len(old_blocks)} -> {len(new_blocks)}"
        )
    for i in range(min(len(old_blocks), len(new_blocks))):
        _, old_title, old_body = old_blocks[i]
        _, new_title, new_body = new_blocks[i]
        old_norm = _dropdown_body_text(old_lines, old_body)
        new_norm = _dropdown_body_text(new_lines, new_body)
        if old_norm != new_norm:
            problems.append(
                f"{{dropdown}} {i + 1} ({old_title!r}) text changed beyond "
                "whitespace and list/table markup"
            )
    return problems


# ---------------------------------------------------------------------------
# Diffing and reporting.


def format_counter(c: Counter, limit: int = 100) -> str:
    def short(s: str) -> str:
        return s if len(s) <= limit else s[: limit - 1] + "…"

    parts = []
    for item in sorted(c):
        n = c[item]
        parts.append(f"{short(item)!r}×{n}" if n > 1 else f"{short(item)!r}")
    return "; ".join(parts)


def diff_page(
    old_text: str,
    new_text: str,
    allowed: frozenset[str] = frozenset(),
    allow_dropdown_edits: bool = False,
) -> list[tuple[bool, str]]:
    """Return (is_failure, message) pairs; does not print anything."""
    results: list[tuple[bool, str]] = []
    old = extract_all(old_text)
    new = extract_all(new_text)
    for cat in CATEGORIES:
        lost = old[cat] - new[cat]
        added = new[cat] - old[cat]
        if lost:
            results.append((True, f"LOST {cat}: {format_counter(lost)}"))
        if added:
            results.append((cat not in allowed, f"ADDED {cat}: {format_counter(added)}"))
    if not allow_dropdown_edits:
        for msg in compare_dropdowns(old_text, new_text):
            results.append((True, msg))
    return results


# ---------------------------------------------------------------------------
# git plumbing and page discovery.


def get_base_text(base: str, relpath: str) -> str | None:
    proc = subprocess.run(
        ["git", "show", f"{base}:{relpath}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        return None
    return proc.stdout


def find_changed_pages(base: str) -> list[Path]:
    tracked = subprocess.run(
        ["git", "diff", "--name-only", base, "--", "docs"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()
    status = subprocess.run(
        ["git", "status", "--porcelain", "--", "docs"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()
    files = set(tracked)
    for line in status:
        if line.startswith("??"):
            files.add(line[3:].strip())
    pages = []
    for f in sorted(files):
        p = ROOT / f
        if p.suffix != ".md":
            continue
        rel_parts = Path(f).parts
        if len(rel_parts) < 2 or rel_parts[0] != "docs" or rel_parts[1] == "plans":
            continue
        if not p.exists():
            continue  # deleted; nothing in the working tree to compare
        pages.append(p)
    return pages


# ---------------------------------------------------------------------------
# Self-test.


def selftest() -> int:
    problems: list[str] = []

    def case(name: str, old: str, new: str, should_pass: bool, **kw) -> None:
        results = diff_page(old, new, **kw)
        failed = any(is_fail for is_fail, _ in results)
        if should_pass and failed:
            problems.append(f"{name}: expected to pass, but: {results}")
        if not should_pass and not failed:
            problems.append(f"{name}: expected to fail, but nothing was flagged")

    # -- pass cases -----------------------------------------------------
    case(
        "paragraph split",
        "# P\n\nOne sentence here. Another sentence there, with 130 nm.[^a]\n"
        "\n[^a]: A source. <https://example.com/a>\n",
        "# P\n\nOne sentence here.\n\nAnother sentence there, with 130 nm.[^a]\n"
        "\n[^a]: A source. <https://example.com/a>\n",
        True,
    )
    case(
        "sentence moved between sections",
        "# P\n\n## A\n\nFirst sentence.[^a] Second sentence, 900 °C.[^b]\n\n"
        "## B\n\nThird sentence.\n"
        "\n[^a]: Source A. <https://example.com/a>\n"
        "[^b]: Source B. <https://example.com/b>\n",
        "# P\n\n## A\n\nFirst sentence.[^a]\n\n"
        "## B\n\nSecond sentence, 900 °C.[^b] Third sentence.\n"
        "\n[^a]: Source A. <https://example.com/a>\n"
        "[^b]: Source B. <https://example.com/b>\n",
        True,
    )
    case(
        "prose converted to a table with the same values",
        "# P\n\n"
        "* **ASML.** Its first KrF stepper, the PAS 5000/70 of 1991, had "
        'NA 0.42.[^kato-2007] Its scanner had "a resolution of 0.22µm".[^kato-2007]\n'
        "\n[^kato-2007]: Kato, *KrF steppers*. <https://example.com/kato>\n",
        "# P\n\n"
        "| Vendor | Model | Year | Published figures |\n"
        "|---|---|---:|---|\n"
        "| ASML | PAS 5000/70 | 1991 | NA 0.42[^kato-2007] |\n\n"
        'Its scanner had "a resolution of 0.22µm".[^kato-2007]\n'
        "\n[^kato-2007]: Kato, *KrF steppers*. <https://example.com/kato>\n",
        True,
    )

    # -- fail cases -------------------------------------------------------
    case(
        "a dropped footnote marker",
        "# P\n\nA claim.[^a][^b]\n"
        "\n[^a]: Source A. <https://example.com/a>\n[^b]: Source B. <https://example.com/b>\n",
        "# P\n\nA claim.[^a]\n"
        "\n[^a]: Source A. <https://example.com/a>\n[^b]: Source B. <https://example.com/b>\n",
        False,
    )
    case(
        "a changed number",
        "# P\n\nThe overlap is 0.33 µm.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        "# P\n\nThe overlap is 0.35 µm.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        False,
    )
    case(
        "a dropped hedge",
        "# P\n\nThis is about 130 nm thick.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        "# P\n\nThis is 130 nm thick.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        False,
    )
    case(
        "an altered quotation",
        '# P\n\nThe datasheet says "double-hump profile".[^a]\n\n[^a]: Source. <https://example.com/a>\n',
        '# P\n\nThe datasheet says "double hump profile".[^a]\n\n[^a]: Source. <https://example.com/a>\n',
        False,
    )
    case(
        "text moved out of a dropdown",
        "# P\n\n::::{dropdown} 1 family in force\n"
        "US 8,796,098 B1 is in force.\n"
        "::::\n",
        "# P\n\n::::{dropdown} 1 family in force\n"
        "::::\n\nUS 8,796,098 B1 is in force.\n",
        False,
    )

    # -- --allow-added lets a declared addition through, but never a loss -
    case(
        "a declared addition is allowed",
        "# P\n\nOne step.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        "# P\n\nOne step, step 006.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        True,
        allowed=frozenset({"numbers"}),
    )
    case(
        "an undeclared addition still fails",
        "# P\n\nOne step.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        "# P\n\nOne step, step 006.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        False,
    )
    case(
        "a loss is never allowed by --allow-added",
        "# P\n\nA claim, 130 nm and 180 nm.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        "# P\n\nA claim, 130 nm.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        False,
        allowed=frozenset({"numbers"}),
    )
    case(
        "--allow-dropdown-edits disables the dropdown check",
        "# P\n\n::::{dropdown} t\nbody one\n::::\n",
        "# P\n\n::::{dropdown} t\nbody two\n::::\n",
        True,
        allow_dropdown_edits=True,
    )

    if problems:
        for p in problems:
            print("SELFTEST FAIL:", p)
        print(f"{len(problems)} selftest problem(s)")
        return 1
    print("selftest OK")
    return 0


# ---------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__.splitlines()[0], formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--base", default="main", help="git revision to compare against (default: main)")
    ap.add_argument(
        "--allow-added",
        default="",
        help="comma-separated categories where additions are permitted: " + ", ".join(CATEGORIES),
    )
    ap.add_argument(
        "--allow-dropdown-edits",
        action="store_true",
        help="skip the {dropdown} unchanged-text check",
    )
    ap.add_argument("--selftest", action="store_true", help="run the offline self-test and exit")
    ap.add_argument("paths", nargs="*", help="pages to check (default: every changed docs/**/*.md)")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    allowed = frozenset(x.strip() for x in args.allow_added.split(",") if x.strip())
    unknown = allowed - frozenset(CATEGORIES)
    if unknown:
        print(f"unknown --allow-added categories: {sorted(unknown)}", file=sys.stderr)
        return 2

    if args.paths:
        pages = [Path(p).resolve() for p in args.paths]
    else:
        pages = find_changed_pages(args.base)

    checked = 0
    bad = 0
    for page in pages:
        rel = page.relative_to(ROOT).as_posix()
        old_text = get_base_text(args.base, rel)
        if old_text is None:
            print(f"{rel}: new file (not present at {args.base}); skipped")
            continue
        new_text = page.read_text()
        checked += 1
        results = diff_page(old_text, new_text, allowed, args.allow_dropdown_edits)
        page_failed = False
        for is_fail, msg in results:
            print(f"{rel}: {msg}")
            page_failed = page_failed or is_fail
        if page_failed:
            bad += 1

    print(f"{checked} page(s) checked against {args.base}, {bad} with undeclared differences")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
