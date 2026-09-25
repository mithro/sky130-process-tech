#!/usr/bin/env python3
"""Check that a readability edit preserved every fact, number, quotation,
hedge and citation on a page (docs/plans/readability-plan.md W0;
docs/plans/readability/report-A.md, "Acceptance check, every page";
report-B.md section 3 item 4).

Compares each page under ``docs/`` (outside ``docs/plans``) between a base
git revision and the working tree, and reports, per page, anything **LOST**
or **ADDED** in nine categories:

1. ``markers`` — the multiset of footnote markers (``[^label]``) in the
   body, and ``footnotes`` — the set of footnote definitions, each with its
   full (whitespace-normalised) text.
2. ``numbers`` — the multiset of numeric tokens: digits with decimal
   points, thin-space/normal-space/comma thousands separators, ``x10``
   exponents and Unicode superscripts, signs and ranges. Only whitespace is
   normalised; nothing else about a number is touched or interpreted.
   Digits that are part of an identifier (see 9) are masked out first, so
   "SKY130" does not count as the number 130, and so is a leading ordered-
   list marker ("3. "), so a numbered item's own "3." is never the number 3.
3. ``number_order`` — per table row, list item or (heuristically split)
   sentence that contains two or more numbers, the *ordered* tuple of
   those numbers. ``numbers`` alone is a multiset and cannot tell
   "6 of 171" from "171 of 6" apart — both are the same two numbers;
   comparing the order within the unit that holds them both catches that
   swap. It cannot catch a swap *between* two units (a number moved from
   one table row or claim to another): see ``extract_number_order``'s
   docstring and "Checking a readability edit" in agent-briefs.md for
   that and other limitations. A LOST tuple is always an error *unless*
   ``--allow-regrouped`` is given and ``check_regrouped`` finds it is a
   clean regroup of the same digits (review T1) — the deliberate result of
   R-TABLE/R-DERIVATION/R-LIST turning one dense unit into several.
4. ``quotes`` — the multiset of quoted strings (straight ``"..."`` and
   curly “...”), matched against the whitespace-*flattened* page so a
   quotation that spans a hard-wrapped source line is still seen as one
   run, then whitespace-normalised for comparison like everything else.
5. ``refs`` — the multiset of ``{ref}``/``{term}``/``{doc}`` targets, and
   ``urls`` — the multiset of URLs written anywhere on the page.
6. ``hedges`` — counts of the hedge phrases in HEDGES below (e.g. "about",
   "typical", "our reading", "~"), matched against the same whitespace-
   flattened text as quotes, for the same reason (a hedge phrase can span a
   hard-wrapped source line too).
7. The text inside every ``{dropdown}`` block, which must be unchanged
   apart from whitespace and list/table markup, unless
   ``--allow-dropdown-edits`` is given. This is not one of the nine
   categories above and has no ``--allow-added`` equivalent: a dropdown
   either passes unedited, or the whole check is disabled for the run.
8. ``identifiers`` — the multiset of whole identifier tokens ("SKY130",
   "EV300", "SC-1", `` `pfet_01v8` ``, "1X") that ``numbers`` masks out
   before counting, tracked separately as whole tokens so a change like
   "SKY130" -> "SKY 130" is still caught, just not as a number.

A **loss** in any category is always an error. An **addition** is an error
unless its category is named in ``--allow-added`` (comma-separated); every
addition is printed either way (a declared one tagged "(declared)"), so
the coordinator can see what changed even when it was permitted. Exit
status is 1 if any undeclared difference (a loss, or an addition outside
``--allow-added``, or a changed dropdown) was found on any checked page.

**This check is necessary, not sufficient.** It cannot see a number moved
between two table cells or two claims (only reordered *within* one unit,
via ``number_order``), a footnote marker moved from one claim to another
where both claims already cite something, or new prose added that
introduces no number, quotation, marker or hedge at all — all multisets
and per-unit comparisons by construction, with no notion of "the same
claim" across a move. A page with zero reported lines is not proof the
edit is safe: the reviewer still reads the diff itself, the way
report-B.md section 3 item 4 originally asked. Any ``--allow-added``
category used on a page should be named, with the reason, in the branch's
progress file, since it is exactly where an unnoticed bad addition (a
"weaker model completing a table" with an invented figure) can hide.

Usage::

    uv run python tools/check_preserved.py [--base main] \\
        [--allow-added markers,footnotes,numbers,number_order,quotes,refs,urls,hedges,identifiers] \\
        [--allow-dropdown-edits] [--allow-regrouped] [paths ...]

With no ``paths``, every ``docs/**/*.md`` file outside ``docs/plans`` that
differs between ``--base`` and the working tree (tracked changes and new,
not-yet-committed files alike) is checked. A file passed explicitly is
always checked, whether or not it differs from ``--base``. A page that does
not exist at ``--base`` (a genuinely new page) is reported and skipped: it
has nothing to compare against.

Run ``uv run python tools/check_preserved.py --selftest`` to run the
built-in self-tests (touches no files, needs no git history):
paragraph splits, a sentence moved between sections, a re-wrapped
paragraph whose quotation now crosses a different line break, a re-wrapped
paragraph whose hedge now crosses a different line break, prose turned
into a table with the same values, "SKY130"/"SC-1"/"1X"/a numbered-item
marker never counting as numbers, and (with ``--allow-regrouped``) a
prose sentence turned into a table all pass; a dropped footnote marker, a
changed number, two numbers swapped in place ("6 of 171" to "171 of 6"),
a dropped hedge, an altered quotation (including one that spans a source
line break), an identifier changed ("SKY130" to "SKY 130"), the same
table split *without* ``--allow-regrouped``, a regroup with a genuinely
missing number even *with* ``--allow-regrouped``, and text moved out of a
dropdown all fail.
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
BRACKETED_URL_RE = re.compile(r"<(https?://[^<>\s]+)>")
QUOTE_RE = re.compile(r'"([^"\n]{1,400})"|“([^”\n]{1,400})”')

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
# Hyphen and en-dash join two numbers into one range/exponent token
# ("3000–4000", "0.25-0.13"); an em-dash is never a numeric-range
# separator in this house style (citation-style.md: it is the reading-list
# head/annotation punctuation, "* head — annotation", and the general
# prose dash) -- excluding it stops a number that merely sits right
# before a bullet's " — " from being chained with the next number in the
# annotation into one combined token (W0c: linking the head inserts
# "](<...>)" between the two, which un-chains them and would otherwise
# read as a LOST/ADDED pair even though neither number's value changed).
_DASH = r"\s?[-–]\s?"
NUMBER_RE = re.compile(rf"{_CORE}(?:{_DASH}{_CORE})*")
SUP_STANDALONE_RE = re.compile(rf"{_SUP_CLASS}+")

# Identifier tokens whose digits are not measurements (review T2, finding D6):
# "SKY130", "EV300", "SC-1", "pfet_01v8", "P316", "C8" (from "C8/R8/S8/L8"),
# and a bare digit-run immediately followed by a single uppercase letter with
# nothing word-like after it ("1X" from "EV300/1X", the placeholder "00N" in
# "mpw-00N.html"). The second branch is deliberately narrow (uppercase only,
# nothing following) so it does not eat a real measurement: this project's
# house style always puts a space before a unit ("5 V", "130 nm"), so a
# genuine number is never directly followed by a bare uppercase letter with
# no space — checked against every step page (`grep -onE '[0-9]+[A-Z]\b'`),
# which found exactly one hit, the "00N" placeholder above, not a number.
IDENT_RE = re.compile(
    r"(?<![\w.])(?:[A-Za-z_][A-Za-z_]*[-/]?\d[\w-]*|\d+[A-Z](?![\w-]))"
)
# A leading ordered-list marker ("3. ", "12) "): NUMBER_RE has no notion of
# markup, so a numbered list's own "3." was being counted as the number 3
# (review T2: found on 004-fom.md, where an R-PARA split changed a numbered
# item's position). Masked before number extraction only, never before the
# list/table structure detection in extract_number_order (which needs the
# marker to know a new item started).
#
# Deliberately narrow: no leading whitespace allowed, and at most two
# digits. A genuine top-level ordered-list marker in this repository always
# starts at column 0 with 1-2 digits (checked: every `docs/steps/*.md` page
# in this batch; grep found zero indented numbered items). Without the
# column-0 restriction, a wrapped continuation line that happens to *start*
# with a real number — "...suppliers.\n    2015. Cypress issued..." wraps
# the year "2015." onto its own indented line — is indistinguishable from a
# genuine marker and would wrongly swallow a real number (found while
# testing this fix, against docs/steps/001-smat.md: an indented "2015."
# line was masked, LOSING the number 2015). The 1-2 digit limit is the same
# safety margin: no page in the site nests a nested numbered nested list
# past a two-digit item count, but a four-digit year ("2015") must never be
# treated as a marker regardless of indentation.
_LEADING_LIST_MARKER_RE = re.compile(r"^\d{1,2}[.)]\s+", re.MULTILINE)

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

CATEGORIES = [
    "markers", "footnotes", "numbers", "quotes", "refs", "urls", "hedges",
    "number_order", "identifiers",
]

# A line that opens a list item ("* ", "- ", "1. ") or a table row ("| ").
_LIST_ITEM_RE = re.compile(r"^(?:[*-]|\d+[.)])\s+")
_TABLE_ROW_RE = re.compile(r"^\|")
# A rough sentence boundary: end punctuation followed by a capital, a
# digit, or an opening quote. Heuristic only — see extract_number_order.
_SENTENCE_SPLIT_RE = re.compile(r'(?<=[.!?])\s+(?=[A-Z0-9"“])')


def normalize_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def role_target(content: str) -> str:
    content = content.strip()
    m = re.search(r"<([^<>]+)>\s*$", content)
    if m:
        return m.group(1).strip()
    return content


def _number_token_spans(text: str) -> list[tuple[int, int, str]]:
    spans: list[tuple[int, int, str]] = []
    for m in NUMBER_RE.finditer(text):
        spans.append((m.start(), m.end(), m.group(0)))
    for m in SUP_STANDALONE_RE.finditer(text):
        if not any(m.start() < e and m.end() > s for s, e, _ in spans):
            spans.append((m.start(), m.end(), m.group(0)))
    spans.sort(key=lambda t: t[0])
    return spans


def _number_tokens_ordered(text: str) -> list[str]:
    """Numeric tokens in ``text``, left to right, whitespace-normalised."""
    return [normalize_ws(t) for _, _, t in _number_token_spans(text) if normalize_ws(t)]


def extract_numbers(text: str) -> Counter:
    return Counter(_number_tokens_ordered(text))


def extract_number_order(text: str) -> tuple[Counter, dict[tuple[str, ...], list[str]]]:
    """Counter of ordered numeric-token tuples, one per "unit" (a table
    row, a list item, or a rough sentence) that carries two or more
    numbers; and, alongside it, up to three short samples of the source
    text that produced each tuple (review T1: printed next to a
    ``--allow-regrouped`` warning so the reviewer can read the actual
    pairing, not just the digits).

    This is the check report-B.md section 3 item 4 and the coordinator's
    2026-09-20 follow-up review both asked for: the plain multiset in
    ``numbers`` cannot tell "6 of 171" from "171 of 6" apart, because it
    is the same two numbers either way. Comparing the ordered sequence
    *within a unit that already held both numbers* catches exactly that
    swap, at the cost of two things worth knowing:

    * **Sentence and list-item boundaries are found heuristically**
      (a regex on end punctuation, or a leading list/table marker), not
      parsed. An unusual sentence may be split wrongly; this only
      widens or narrows what counts as "together", it does not stop the
      table-row case from working.
    * **It cannot see a swap *between* two units** — two numbers
      exchanged between adjacent table rows, or a marker moved from one
      claim to the next, produce no ordered-tuple difference at all,
      because each unit's own internal order is unchanged. Nor can it
      see prose added that introduces no number. Report-B.md section 3
      item 4's actual worry ("a weaker model completing a table") is
      only partly covered: a same-row transposition is caught; a
      cross-row substitution is not. The reviewer still reads the diff;
      see "Checking a readability edit" in agent-briefs.md.
    """
    tuples: list[tuple[str, ...]] = []
    samples: dict[tuple[str, ...], list[str]] = {}
    paragraph: list[str] = []

    def add_unit(unit_text: str) -> None:
        nums = _number_tokens_ordered(unit_text)
        if len(nums) >= 2:
            key = tuple(nums)
            tuples.append(key)
            bucket = samples.setdefault(key, [])
            if len(bucket) < 3:
                bucket.append(normalize_ws(unit_text)[:160])

    def add_prose(text_block: str) -> None:
        # A leading ordered-list marker ("3. ") is not part of the prose;
        # strip the one at the very start of this unit (there is at most
        # one — a table row never reaches here) before splitting into
        # sentences, so a numbered item's own marker digit is never
        # counted as part of its first sentence's number tuple (T2).
        text_block = _LEADING_LIST_MARKER_RE.sub(" ", text_block.strip(), count=1)
        # A list item can itself hold several sentences (e.g. a reading-
        # list bullet); split it the same way a paragraph is, so a
        # number in one sentence is not lumped together with a number
        # in the next merely because they share one bullet.
        for sentence in _SENTENCE_SPLIT_RE.split(text_block.strip()):
            add_unit(sentence)

    def flush_paragraph() -> None:
        if not paragraph:
            return
        para = " ".join(paragraph)
        paragraph.clear()
        add_prose(para)

    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if _TABLE_ROW_RE.match(stripped):
            flush_paragraph()
            add_unit(line)
            i += 1
            continue
        if _LIST_ITEM_RE.match(stripped):
            flush_paragraph()
            item_lines = [line]
            i += 1
            while (
                i < len(lines)
                and lines[i].strip()
                and not _LIST_ITEM_RE.match(lines[i].strip())
                and not _TABLE_ROW_RE.match(lines[i].strip())
            ):
                item_lines.append(lines[i])
                i += 1
            add_prose(" ".join(item_lines))
            continue
        if not stripped:
            flush_paragraph()
            i += 1
            continue
        paragraph.append(line)
        i += 1
    flush_paragraph()
    return Counter(tuples), samples


def extract_quotes(text: str) -> Counter:
    out = []
    for m in QUOTE_RE.finditer(text):
        inner = m.group(1) if m.group(1) is not None else m.group(2)
        out.append(normalize_ws(inner))
    return Counter(q for q in out if q)


def extract_hedges(text: str) -> Counter:
    # Note (review T3): "typical" also matches inside "industry-typical", so
    # a page using the latter counts both phrases once each for the same
    # words. Harmless — the same double-count happens identically on both
    # sides of a diff, so it never causes a false LOST or ADDED — and left
    # alone rather than adding a phrase-priority rule that would complicate
    # this for no behavioural gain.
    c: Counter = Counter()
    for phrase, pat in HEDGE_PATTERNS:
        n = len(pat.findall(text))
        if n:
            c[phrase] = n
    return c


def extract_urls_masked(text: str) -> tuple[Counter, str]:
    """Return (URL counts, ``text`` with every URL masked to one space).

    House style (``docs/plans/citation-style.md``) wraps a citation URL
    in angle brackets (``<https://...>``); that delimiter is unambiguous
    and is tried first, taking the *whole* interior, parentheses
    included -- a bare punctuation-trimming regex would otherwise
    truncate a pre-2000 Elsevier DOI
    (``https://doi.org/10.1016/0040-6090(89)90102-8``) or a Wikipedia
    title with a literal ``(`` at the first ``)``, and the truncated
    remainder (``)90102-8``) can then be misread as a "new" number by
    ``extract_numbers`` (see ``tools/check_links.py``, which solves the
    same problem the same way). Whatever text is left is masked with the
    old bare-URL regex, in case a page ever strays from house style.
    """
    counts: Counter = Counter()
    spans: list[tuple[int, int]] = []
    for m in BRACKETED_URL_RE.finditer(text):
        counts[m.group(1)] += 1
        spans.append((m.start(), m.end()))
    if spans:
        chars = list(text)
        for s, e in spans:
            for i in range(s, e):
                chars[i] = " "
        text = "".join(chars)
    for u in URL_RE.findall(text):
        counts[u] += 1
    text = URL_RE.sub(" ", text)
    return counts, text


def extract_all(text: str) -> tuple[dict[str, Counter], dict[tuple[str, ...], list[str]]]:
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
    urls, masked = extract_urls_masked(masked)
    masked = MARKER_RE.sub(" ", masked)

    # Flatten before matching (review finding H1): the repository's
    # markdown is hard-wrapped, so a quotation frequently spans a source
    # line break. QUOTE_RE forbids "\n" inside a match, so applied to the
    # raw text it silently misses every such quotation (measured: ~29% of
    # all quotations on this repository's pages) — invisible to a wording
    # change inside one, and it flags a false LOST/ADDED pair whenever a
    # harmless re-wrap moves where a quotation happens to cross a line.
    # Flattening first (as the hand recipe in readability-guide.md §7
    # already does) fixes both: a wrapped quotation is matched as one
    # run, and re-wrapping it changes no character of that run.
    quotes = extract_quotes(normalize_ws(masked))
    # Same flattening for hedges (review T3/D7): "our extraction" re-wrapped
    # across a source line break (one word ending a line, the next starting
    # the following one) used to be invisible to `\b our extraction \b`,
    # which matches literal text, not markdown-soft-wrapped text — a false
    # LOST hedge with no content change at all. Fixed the same way as quotes.
    hedges = extract_hedges(normalize_ws(masked))

    # Mask identifier tokens — "SKY130", "EV300", "SC-1", "pfet_01v8", "1X"
    # — before extracting numbers, so a digit that is part of a name is
    # never counted as a measurement (review T2/D6). This must not touch
    # the `masked` text used above for quotes/hedges: masking would blank
    # out an identifier that happens to sit inside a quotation, corrupting
    # the very wording being checked.
    identifiers: Counter = Counter()

    def _ident_sub(m: re.Match) -> str:
        identifiers[m.group(0)] += 1
        return " "

    masked_for_numbers = IDENT_RE.sub(_ident_sub, masked)
    numbers = extract_numbers(_LEADING_LIST_MARKER_RE.sub(" ", masked_for_numbers))
    number_order, number_order_samples = extract_number_order(masked_for_numbers)
    footnotes = Counter(f"[^{label}]: {text}" for label, text in defs.items())

    return {
        "markers": markers,
        "footnotes": footnotes,
        "numbers": numbers,
        "quotes": quotes,
        "refs": refs,
        "urls": urls,
        "hedges": hedges,
        "number_order": number_order,
        "identifiers": identifiers,
    }, number_order_samples


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


# A near-URL or a whole footnote definition truncated at 100 characters
# often differs only after the cut, making the two printed lines look
# identical (review finding L10); those categories get a longer limit.
_DISPLAY_LIMIT = {"footnotes": 300, "urls": 300}


def format_counter(c: Counter, limit: int = 100) -> str:
    def short(s: str) -> str:
        return s if len(s) <= limit else s[: limit - 1] + "…"

    parts = []
    for item in sorted(c):
        n = c[item]
        parts.append(f"{short(item)!r}×{n}" if n > 1 else f"{short(item)!r}")
    return "; ".join(parts)


def _is_subsequence(sub: tuple[str, ...], full: tuple[str, ...]) -> bool:
    it = iter(full)
    for x in sub:
        for y in it:
            if y == x:
                break
        else:
            return False
    return True


def _flatten(tuples_counter: Counter) -> Counter:
    flat: Counter = Counter()
    for t, n in tuples_counter.items():
        for v in t:
            flat[v] += n
    return flat


def check_regrouped(
    lost_no: Counter,
    added_no: Counter,
    old_numbers: Counter,
    new_numbers: Counter,
    numbers_allowed: bool,
    old_samples: dict[tuple[str, ...], list[str]],
    new_samples: dict[tuple[str, ...], list[str]],
) -> tuple[bool, list[str]]:
    """``--allow-regrouped`` (review T1): downgrade a ``number_order`` LOST
    to a warning when all four hold:

    (a) ``numbers`` itself has no LOST — nothing actually disappeared, only
        the grouping changed;
    (b) the flattened multiset of numbers across the LOST tuples equals
        that of the ADDED tuples, once numbers separately declared with
        ``--allow-added numbers`` are removed from the ADDED side (a
        deliberate new number — an "At a glance" box repeating one — is
        not required to also balance the regrouping arithmetic);
    (c) every ADDED tuple is an ordered subsequence of some one LOST
        tuple. This is what actually catches a same-unit transposition; it
        cannot catch a *wrong* "respectively" pairing, because both the
        right and the wrong pairing are equally valid subsequences of the
        same lost tuple — that is what (d) is for;
    (d) print each LOST unit's source text next to the ADDED units that,
        per (c), cover it, so the reviewer reads the actual pairing rather
        than trusting the digits alone.

    Returns ``(all four hold, extra message lines including the (d)
    printout)``. When any of (a)-(c) fails, the extra lines say which.
    """
    lines: list[str] = []
    if old_numbers - new_numbers:
        return False, ["condition (a) failed: `numbers` itself lost a value"]
    declared_added_numbers = (new_numbers - old_numbers) if numbers_allowed else Counter()
    lost_flat = _flatten(lost_no)
    added_flat = _flatten(added_no) - declared_added_numbers
    if lost_flat != added_flat:
        return False, [
            "condition (b) failed: flattened numbers differ - lost "
            f"{dict(lost_flat)} vs added (after declared) {dict(added_flat)}"
        ]
    lost_units = list(lost_no)
    for added_tuple in added_no:
        if not any(_is_subsequence(added_tuple, t) for t in lost_units):
            return False, [
                f"condition (c) failed: added tuple {added_tuple} is not an "
                "ordered subsequence of any lost tuple"
            ]
    for lost_tuple in lost_units:
        covering = [t for t in added_no if _is_subsequence(t, lost_tuple)]
        lines.append(f"regrouped: {lost_tuple} -> {covering}")
        for sample in old_samples.get(lost_tuple, [])[:1]:
            lines.append(f"    was: {sample!r}")
        for t in covering:
            for sample in new_samples.get(t, [])[:1]:
                lines.append(f"    now {t}: {sample!r}")
    return True, lines


def diff_page(
    old_text: str,
    new_text: str,
    allowed: frozenset[str] = frozenset(),
    allow_dropdown_edits: bool = False,
    allow_regrouped: bool = False,
) -> list[tuple[bool, str]]:
    """Return (is_failure, message) pairs; does not print anything."""
    results: list[tuple[bool, str]] = []
    old, old_samples = extract_all(old_text)
    new, new_samples = extract_all(new_text)
    for cat in CATEGORIES:
        lost = old[cat] - new[cat]
        added = new[cat] - old[cat]
        limit = _DISPLAY_LIMIT.get(cat, 100)
        if cat == "number_order" and allow_regrouped and lost:
            ok, extra = check_regrouped(
                lost, added, old["numbers"], new["numbers"],
                "numbers" in allowed, old_samples, new_samples,
            )
            if ok:
                results.append(
                    (False, f"REGROUPED (--allow-regrouped) number_order: "
                            f"{format_counter(lost, limit)} -> {format_counter(added, limit)}")
                )
                for line in extra:
                    results.append((False, line))
                continue
            results.append((True, f"LOST number_order (not a clean regroup): {format_counter(lost, limit)}"))
            for line in extra:
                results.append((True, line))
            if added:
                is_fail = cat not in allowed
                tag = "ADDED" if is_fail else "ADDED (declared)"
                results.append((is_fail, f"{tag} {cat}: {format_counter(added, limit)}"))
            continue
        if lost:
            results.append((True, f"LOST {cat}: {format_counter(lost, limit)}"))
        if added:
            is_fail = cat not in allowed
            tag = "ADDED" if is_fail else "ADDED (declared)"
            results.append((is_fail, f"{tag} {cat}: {format_counter(added, limit)}"))
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
        "a re-wrapped paragraph whose quotation crosses a different line break",
        "# P\n\nA source says \"first line\nsecond line\" here.[^a]\n\n"
        "[^a]: Source. <https://example.com/a>\n",
        "# P\n\nA source says \"first\nline second line\" here.[^a]\n\n"
        "[^a]: Source. <https://example.com/a>\n",
        True,
    )
    case(
        "a reading-list head linked to a DOI URL with a literal parenthesis "
        "does not leak digits into 'numbers' (W0c)",
        "# P\n\n## References\n\n### Deep dive\n\n"
        "* Turban et al., *Thin Solid Films* 1989 — tungsten etching.[^a]\n"
        "\n[^a]: Turban et al., *Thin Solid Films*. "
        "<https://doi.org/10.1016/0040-6090(89)90102-8>\n",
        "# P\n\n## References\n\n### Deep dive\n\n"
        "* [Turban et al., *Thin Solid Films*](<https://doi.org/10.1016/0040-6090(89)90102-8>)"
        " 1989 — tungsten etching.[^a]\n"
        "\n[^a]: Turban et al., *Thin Solid Films*. "
        "<https://doi.org/10.1016/0040-6090(89)90102-8>\n",
        True,
        allowed=frozenset({"urls"}),
    )
    case(
        "linking a bullet head does not un-chain a number 'joined' to the "
        "annotation's number across the bullet's em-dash (W0c)",
        "# P\n\n## References\n\n### Deep dive\n\n"
        "* Oh (Hynix), US 6,576,405 — 3.4-4.2 MeV phosphorus.[^a]\n"
        "\n[^a]: Oh. <https://patents.google.com/patent/US6576405B2>\n",
        "# P\n\n## References\n\n### Deep dive\n\n"
        "* [Oh (Hynix), US 6,576,405](<https://patents.google.com/patent/US6576405B2>)"
        " — 3.4-4.2 MeV phosphorus.[^a]\n"
        "\n[^a]: Oh. <https://patents.google.com/patent/US6576405B2>\n",
        True,
        allowed=frozenset({"urls"}),
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
    case(
        "a re-wrapped paragraph whose hedge crosses a different line break (T3)",
        "# P\n\nA value (our\nextraction from data).[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        "# P\n\nA value (our extraction\nfrom data).[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        True,
    )

    # -- T1: --allow-regrouped -------------------------------------------
    _regroup_old = (
        "# P\n\nThe values are 5 and 6, or 7 and 8.[^a]\n"
        "\n[^a]: Source. <https://example.com/a>\n"
    )
    _regroup_new = (
        "# P\n\n| A | B |\n|---|---|\n| 5 | 6 |\n| 7 | 8[^a] |\n"
        "\n[^a]: Source. <https://example.com/a>\n"
    )
    case(
        "a clean regroup is a warning, not a failure, with --allow-regrouped",
        _regroup_old, _regroup_new, True, allow_regrouped=True,
    )
    case(
        "the same regroup fails without --allow-regrouped",
        _regroup_old, _regroup_new, False,
    )
    case(
        "a regroup that actually drops a number still fails, even with --allow-regrouped",
        _regroup_old,
        "# P\n\n| A | B |\n|---|---|\n| 5 | 6 |\n| 7 | 9[^a] |\n"
        "\n[^a]: Source. <https://example.com/a>\n",
        False,
        allow_regrouped=True,
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
        "a changed word inside a quotation that spans a source line break",
        "# P\n\nA source says \"a depth d1 within a range\nof, for example, 3000-4000 Å\".[^a]\n\n"
        "[^a]: Source. <https://example.com/a>\n",
        "# P\n\nA source says \"a depth d1 within a range\nof, for instance, 3000-4000 Å\".[^a]\n\n"
        "[^a]: Source. <https://example.com/a>\n",
        False,
    )
    case(
        "two numbers swapped in place",
        "# P\n\n| Step number | 6 of 171[^a] |\n\n[^a]: Source. <https://example.com/a>\n",
        "# P\n\n| Step number | 171 of 6[^a] |\n\n[^a]: Source. <https://example.com/a>\n",
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
    case(
        "an identifier changed is still caught (T2/D6: SKY130 -> SKY 130)",
        "# P\n\nBuilt for SKY130.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        "# P\n\nBuilt for SKY 130.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        False,
    )

    # -- T2: identifiers are masked before numbers are counted, and a
    # numbered list's own marker is not a number. Checked directly against
    # extract_all rather than through diff_page, since these are single-
    # text assertions, not before/after comparisons.
    def assert_no_numbers(name: str, body: str) -> None:
        extracted, _ = extract_all(f"# P\n\n{body}\n")
        if extracted["numbers"]:
            problems.append(f"{name}: expected no numbers, got {dict(extracted['numbers'])}")

    def assert_has_number(name: str, body: str, expected: str) -> None:
        extracted, _ = extract_all(f"# P\n\n{body}\n")
        if extracted["numbers"].get(expected, 0) < 1:
            problems.append(f"{name}: expected {expected!r} in {dict(extracted['numbers'])}")

    for token in ("SKY130", "SC-1", "`nfet_01v8`", "1X"):
        assert_no_numbers(f"identifier {token!r} yields no number", f"Built with {token} here.")
    assert_no_numbers("C8/R8/S8/L8 yields no numbers", "Covers the C8/R8/S8/L8 families.")
    assert_no_numbers(
        "a numbered-item marker yields no number",
        "2. **Step.** No digits appear in this sentence at all.",
    )
    assert_has_number("0.18µm still yields 0.18", "The gap is 0.18µm wide.", "0.18")

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
    ap.add_argument(
        "--allow-regrouped",
        action="store_true",
        help=(
            "downgrade a number_order LOST to a warning when it is a clean regroup of the "
            "same digits (review T1); see check_regrouped's docstring for the four conditions"
        ),
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
        try:
            rel = page.relative_to(ROOT).as_posix()
        except ValueError:
            print(f"{page}: not inside the repository ({ROOT}); skipped", file=sys.stderr)
            bad += 1
            continue
        old_text = get_base_text(args.base, rel)
        if old_text is None:
            print(f"{rel}: new file (not present at {args.base}); skipped")
            continue
        new_text = page.read_text()
        checked += 1
        results = diff_page(old_text, new_text, allowed, args.allow_dropdown_edits, args.allow_regrouped)
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
