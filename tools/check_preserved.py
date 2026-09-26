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
   A MyST/backtick fence line (``:::{table} Caption``, a bare ``:::``/
   `````` ``` `` close) and a directive option line (``:widths:``,
   ``:width:``, ``:name:``, ``:class:``, ``:align:`` and a few more; not
   ``:alt:``/``:caption:``, which hold real prose) are masked out too
   (review section C finding C2, rd-overview finding 2): layout markup and
   metadata are never content, so an R-CAPTION table's ``:widths:`` values
   never add undeclarable numbers, but the caption/title text itself
   (real, pre-existing prose) is still counted normally.
3. ``number_order`` — per table row, list item, ATX heading, fence
   caption/title or (heuristically split) sentence that contains two or
   more numbers, the *ordered* tuple of those numbers. ``numbers`` alone
   is a multiset and cannot tell "6 of 171" from "171 of 6" apart — both
   are the same two numbers; comparing the order within the unit that
   holds them both catches that swap. It cannot catch a swap *between*
   two units (a number moved from one table row or claim to another):
   see ``extract_number_order``'s docstring and "Checking a readability
   edit" in agent-briefs.md for that and other limitations. A LOST tuple
   is always an error *unless* ``--allow-regrouped`` is given and
   ``check_regrouped`` finds it still occurs, unchanged and in order, as
   a contiguous run in the *other* page's flat numeric-token stream
   (review T1, redesigned per review section C finding C3) — the
   deliberate result of R-TABLE/R-DERIVATION/R-LIST turning one dense
   unit into several, including turning it into several rows/items with
   only *one* number each (rd-overview finding 3), which on its own
   drops every one of those rows/items below the "two or more numbers"
   threshold above and so would otherwise be an unconditional,
   undeclarable loss. A genuine swap — within a unit, between table rows,
   or between list items — breaks the contiguous run and still fails.
4. ``quotes`` — the multiset of quoted strings (straight ``"..."`` and
   curly “...”), matched and paired one PARAGRAPH at a time (split on a
   blank line, then whitespace-*flattened*), so a quotation that spans a
   hard-wrapped source line is still seen as one run, then whitespace-
   normalised for comparison like everything else. A quotation is capped
   at 800 characters (Guide problem 16, raised from 400: a longer
   quotation used to desynchronise the open/close pairing of every later
   quotation on the *whole page*, since matching once ran over the entire
   flattened text; scoping to one paragraph limits any remaining mismatch
   to that paragraph). A paragraph whose own quote-mark count is odd (a
   quotation still over the cap, or a stray unmatched mark) is printed as
   a ``WARN`` naming the page, rather than silently resolved by whatever
   the regex pairs next.
5. ``refs`` — the multiset of ``{ref}``/``{term}``/``{doc}`` targets, and
   ``urls`` — the multiset of URLs written anywhere on the page. A role is
   matched and removed from the text as one atomic unit *before* inline
   code spans are masked (G15/T-new-1, rd-steps-035-047.md and rd-steps-
   014-034.md reviews): the previous order let a role's own closing
   backtick be mistaken for the opening delimiter of whatever unrelated
   code span came next on the same line, swallowing the prose between
   them (a hedge, another role). A role's own closing backtick
   immediately followed by a second backtick is left alone, so a role
   shown as a literal code example is still never misread as a real
   invocation (rd-site review finding L5).
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
9. ``words`` — a case-folded word-multiset of the page's "open text":
   everything outside a ``{dropdown}`` body, a ``{figure}`` fence, a
   generated ``<!-- name:begin -->``...``<!-- name:end -->`` block, and a
   footnote definition. Unlike the eight categories above, this one has
   no notion of a number, quotation, marker, hedge, role or identifier to
   latch onto, so it is the only category that can see an ordinary word
   quietly dropped (rd-steps-064-075.md guide problem 4: a first draft of
   step 074 lost "removing step:" through an overlapping replacement, and
   every other check passed). Always printed (``WORDS LOST``/``WORDS
   ADDED``), never itself a failure, unless ``--strict-words`` is given,
   which fails on a LOST word that is not in the small ``WORDS_STOPLIST``
   of common function words (routine rewording otherwise shifts their
   counts too often to be usable as a strict gate).

A **loss** in categories 1-8 is always an error. An **addition** is an
error unless its category is named in ``--allow-added`` (comma-separated);
every addition is printed either way (a declared one tagged "(declared)"),
so the coordinator can see what changed even when it was permitted.
``--allow-deduplicated`` narrowly downgrades a LOST ``quotes``/``markers``/
``numbers`` item to a warning on a class page (``docs/machines/*.md``,
``docs/materials/*.md`` only) when it disappeared from the quick-facts
table (before the first H2) but is unchanged, and still present, in the
body (rd-materials.md review "D1": R-QUICKFACTS asks writers to delete a
quick-facts cell's copy of a value the body already states, which the
multiset check cannot otherwise tell apart from a real deletion). Exit
status is 1 if any undeclared difference (a loss, an addition outside
``--allow-added``, a changed dropdown, or a ``--strict-words`` failure)
was found on any checked page.

Two further checks are informational only and never affect the exit
status: every "At a glance" admonition bullet's numbers and footnote
markers must recur somewhere in the body below it, and every "*SkyWater
says:*" line must contain a quotation mark or a ``skw-``/``cyp-``
footnote marker; each runs once against the CURRENT page text (not a
before/after diff) and prints a ``WARN`` with the page and line when it
does not.

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
        [--allow-dropdown-edits] [--allow-regrouped] [--allow-deduplicated] \\
        [--strict-words] [paths ...]

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
into a table with the same values, a numbered bold run-in label converted
to a heading (a digit-bearing label immediately followed by ``**`` no
longer fuses with the next sentence), a ``:::{table}`` caption/``:widths:``
pair (the caption's own numbers are kept, the fence and ``:widths:``
line are not), "SKY130"/"SC-1"/"1X"/a numbered-item marker never counting
as numbers, a role shown as a literal inline-code example never counting
as a real role, a bare number directly before a year-like number not
mis-tokenising into a bogus grouped number, a role followed on the same
line by an unrelated inline code span no longer losing the ref or the
hedge between them (G15/T-new-1), a >400-char quotation elsewhere on the
page no longer masking a real wording change in a later quotation (Guide
problem 16), the new hedge words, a quick-facts deletion downgraded by
``--allow-deduplicated`` under its three conditions, a dropped word
reported informationally without failing the run, and (with
``--allow-regrouped``) a prose sentence turned into a table, and a numeric
sequence regrouped into one-number-per-row table or list rows, all pass;
a dropped footnote marker, a changed number, two numbers swapped in place
("6 of 171" to "171 of 6"), a dropped hedge, an altered quotation
(including one that spans a source line break), an identifier changed
("SKY130" to "SKY 130"), the same table split *without*
``--allow-regrouped``, a regroup with a genuinely missing number or a
genuine swap between rows even *with* ``--allow-regrouped``, text moved
out of a dropdown, a quick-facts deletion that is not actually
deduplicated (still present in the body under different terms), and a
dropped content word under ``--strict-words`` all fail. The glance-box
and "*SkyWater says:*" checks, and the plain (non-strict) ``words`` diff,
are exercised too, confirming they warn without failing.
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
# A genuine {ref}/{term}/{doc} role, consumed as one atomic unit and
# removed from the text BEFORE any inline-code-span masking runs (rd-
# steps-035-047.md review section D, "Guide problem 15"; rd-steps-014-
# 034.md review, "T-new-1"). The previous design ran code-span masking
# first and role-matching second: nothing marked a role's own CLOSING
# backtick as already "spent", so the code-span masker was free to treat
# it as a fresh OPENING delimiter for whatever backtick came next later
# on the line, silently swallowing every word of ordinary prose in
# between (a hedge, another role, a citation) into one bogus masked span
# and leaving the role's own target unmatched -- a false LOST ref *and* a
# false LOST hedge from the same edit, and one that came and went with
# harmless re-wrapping (rd-steps-064-075.md guide problem 3), since it
# only fired when the role and the next code span both landed on one
# physical source line. Matching the whole role up front and deleting it
# here removes the characters the bug needed before code-span masking
# ever sees them, so the bug cannot occur regardless of line wrapping.
#
# The trailing negative lookahead ``(?!`)`` -- the role's own closing
# backtick must not be immediately followed by another backtick -- keeps
# this from also swallowing the "role shown as a literal code example"
# case (rd-site review L5, e.g. a glossary intro demonstrating the
# `` `{term}`sense`` `` syntax itself): there the role's closing backtick
# sits right against a second backtick (the start of an enclosing double-
# backtick span), which is the shape of a role *displayed inside* a
# larger code span rather than invoked. Excluding that shape leaves it
# for the ordinary code-span masking below to handle, exactly as before.
ROLE_RE = re.compile(r"\{(?:ref|term|doc)\}`([^`]+)`(?!`)")
URL_RE = re.compile(r"https?://[^\s<>\)\]\"'`]+")
BRACKETED_URL_RE = re.compile(r"<(https?://[^<>\s]+)>")
QUOTE_RE = re.compile(r'"([^"\n]{1,800})"|“([^”\n]{1,800})”')
_PARA_SPLIT_RE = re.compile(r"\n[ \t]*\n")

# An inline code span (`` ``...`` `` or `` `...` ``), run AFTER roles are
# already extracted and removed (see ROLE_RE above): masking here only
# ever sees the ordinary backticks of real code spans, never a role's own
# delimiters, which is what fixes G15/T-new-1. The negative lookbehind
# still refuses to start a span right after a "}" (belt and suspenders:
# harmless now that a genuine role's own opening backtick is always gone
# by this point, but cheap insurance against a malformed role ROLE_RE
# failed to match), and the inner negative lookahead still refuses to let
# a tentative span swallow a role-start sequence, so a stray, unrelated
# code span earlier in the paragraph can never eat into a role ROLE_RE
# also failed to recognise (the literal-example case above) by matching
# all the way to *its* backtick.
_ROLE_START = r"\{(?:ref|term|doc)\}`"
_CODE_SPAN_DOUBLE_RE = re.compile(r"(?<!\})``((?:(?!``).)*?)``")
_CODE_SPAN_SINGLE_RE = re.compile(
    rf"(?<!\}})`((?:(?!{_ROLE_START})[^`\n])*)`"
)


def _mask_inline_code(text: str) -> str:
    text = _CODE_SPAN_DOUBLE_RE.sub(lambda m: m.group(1), text)
    text = _CODE_SPAN_SINGLE_RE.sub(lambda m: m.group(1), text)
    return text

# An inch mark: a straight double quote right after a digit, immediately
# followed (optionally after a closing bracket) by another straight quote,
# as in 8"" or (8")". Left unmasked, QUOTE_RE reads the inch mark as a quote
# delimiter and the pairing then runs off by one for the rest of the page
# (checkers review of rd-steps-001-013, "check_preserved.py quote finding",
# reproduced on docs/machines/starting-material.md:188 and
# docs/machines/single-wafer-spin-processor.md:153). The mechanism is not
# "zero characters between the marks": in (8")", a ")" sits between the two
# marks, so the lookahead allows one optional closing bracket there. The
# digit must follow "(" or "<non-letter><space>", so a nested quotation
# ending in a number ("Fab 4")" is left alone — a bare "8" wide" with no
# second quote nearby is also left alone, since the lookahead requires a
# real closing quote to actually be there.
INCH_RE = re.compile(r'(?:(?<=\(\d)|(?<=[^A-Za-z\s] \d))"(?=[)\]]?")')

_SIGN = r"[+\-−±]"
_SUP_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹"
_SUP_CLASS = rf"[{_SUP_DIGITS}⁻⁺]"
# (?!\d) after each group of 3 stops a bare space from over-running into
# a following, unrelated number: without it "Q4 2020" tokenised as "4 202"
# + "0" (rd-overview reviewer, 2026-09-25 review, section C finding C4) --
# "2020" was read as the start of a thousands-grouped number ("4 202") plus
# a stray trailing "0", because the space between "4" and "2020" is also a
# valid thousands separator and nothing stopped the group from being
# followed by a fourth digit. Real thousands groups ("3 200", "1,940",
# "12,500") are unaffected: each of their groups is followed by whitespace,
# punctuation or end of string, never a fifth digit.
_GROUPED = r"\d{1,3}(?:[,   ]\d{3}(?!\d))+"
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
# "roughly", "of order", "of the order of", "typically", "usually" and
# "likely" are the rd-categories.md review's recommendation (finding D2 /
# the fix round's "For the tool branch" note): without "of order", the
# tool could not see implant.md silently dropping "doses of order
# 10^12-10^13 cm^-2" to the bare range twice over. "light" (as in "light
# doses of order ...", the same finding) is added on the task's own
# instruction, from the same page: it narrows the same approximation the
# same way "of order" does, dropped in the same edit.
HEDGES = [
    "not public", "we infer", "inference", "our reading", "our arithmetic",
    "our extraction", "our estimate", "typical", "industry-typical",
    "industry-generic", "plausibly", "presumably", "probably", "may",
    "might", "about", "approximately", "~", "≈",
    "roughly", "of order", "of the order of", "light", "typically",
    "usually", "likely",
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
# The closing markers `` [*_"”’)\]]* `` between the punctuation and the
# whitespace let the boundary through a closing bold/italic marker, a
# closing quote, a closing bracket, or several of these together (rd-
# overview finding 1 / review C1): a numbered bold run-in label such as
# "**Via 1, metal 2 and via 2.**" was invisible to the old regex, because
# it required `[.!?]` to be *immediately* followed by whitespace, and
# ".**" has "*" in between — the label's digits silently fused with the
# next sentence's into one bogus, inflated `number_order` unit. The
# `[*_(]*` before the capital/digit/quote symmetrically lets the boundary
# through an *opening* marker on the next sentence (e.g. a new bold label).
_SENTENCE_SPLIT_RE = re.compile(r'(?<=[.!?])[*_"”’)\]]*\s+(?=[*_(]*[A-Z0-9"“])')
# An ATX heading ("### Name") is always its own unit and always ends
# whatever paragraph came before it, even with no blank line in between
# (review C1): without this, a bold run-in label converted to a heading
# with no blank line before its body (a workaround some branches used
# specifically to dodge the bug above) reads as one fused unit, same as
# the un-fixed sentence splitter did. With both C1 fixes landed, that
# workaround is unnecessary — a heading may always be followed directly
# by its body with no blank line, or written the normal way with one.
_HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$")
# A fence line: a MyST/backtick directive open (optionally with a caption
# or title after the ``{name}``, e.g. ``:::{table} Caption text.`` or
# ``::::{dropdown} Title``) or a bare close (``:::``/`````` ``). Also
# always its own unit boundary, and never itself prose (review C2): the
# fence markup is layout, not content. A caption/title *argument* after
# the ``{name}`` is real content that pre-existed as ordinary prose before
# the fence was added (e.g. an R-CAPTION table caption), so it is passed
# on to ``add_prose`` as its own unit rather than discarded with the
# fence syntax.
_FENCE_RE = re.compile(r"^(?::{3,}|`{3,})\s*(?:\{[\w-]+\})?\s*(.*)$")
# MyST directive option lines (``:widths: 16 20 28 12 24``, ``:name: ...``)
# inside a fence: layout metadata, never content (review C2). Masked out
# before number/identifier extraction in ``extract_all`` (not here: this
# module-level constant is reused there). Deliberately excludes ``:alt:``
# and ``:caption:``, which hold real, previously-existing prose.
_LAYOUT_OPTION_RE = re.compile(
    r"(?m)^[ \t]*:(?:widths|width|height|scale|align|name|class|"
    r"header-rows|stub-columns|maxdepth|numbered):.*$"
)


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


def extract_number_order(
    text: str,
) -> tuple[Counter, dict[tuple[str, ...], list[str]], list[list[tuple[str, ...]]]]:
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
    # Third result (review rd-steps-118-134 D4, and batch-8 guide problem
    # 3): the page's "blocks" -- a paragraph, a list item, or a table
    # together with the paragraph that leads into it -- each as the list
    # of its units' ordered numeric tokens (units below the 2-number
    # threshold included). check_regrouped uses them to recognise dash or
    # parenthetical material moved, unchanged, to directly after its
    # sentence: same numbers in the same block, only their order changed.
    blocks: list[list[tuple[str, ...]]] = []
    current_block: list[tuple[str, ...]] = []
    last_kind = [""]

    def end_block(kind: str) -> None:
        nonlocal current_block
        if current_block:
            blocks.append(current_block)
        current_block = []
        last_kind[0] = kind

    def add_unit(unit_text: str) -> None:
        nums = _number_tokens_ordered(unit_text)
        current_block.append(tuple(nums))
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
        end_block("paragraph")

    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        hm = _HEADING_RE.match(stripped)
        if hm:
            flush_paragraph()
            add_unit(hm.group(1))
            end_block("heading")
            i += 1
            continue
        fm = _FENCE_RE.match(stripped)
        if fm:
            flush_paragraph()
            if fm.group(1):
                add_prose(fm.group(1))
            end_block("fence")
            i += 1
            continue
        if _TABLE_ROW_RE.match(stripped):
            flush_paragraph()
            # A table and the paragraph that leads into it form one block:
            # take that paragraph back (it was just closed) so a lead-in
            # number moved into a cell, or out of one, is "within the block".
            if last_kind[0] == "paragraph" and blocks:
                current_block = blocks.pop() + current_block
            while i < len(lines) and _TABLE_ROW_RE.match(lines[i].strip()):
                add_unit(lines[i])
                i += 1
            end_block("table")
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
            end_block("item")
            continue
        if not stripped:
            flush_paragraph()
            i += 1
            continue
        paragraph.append(line)
        i += 1
    flush_paragraph()
    end_block("end")
    return Counter(tuples), samples, blocks


def extract_quotes(text: str, page_label: str = "") -> tuple[Counter, list[str]]:
    """Quoted strings in ``text``, matched and paired one PARAGRAPH at a
    time (Guide problem 16, rd-steps-035-047.md review section D; rd-
    steps-014-034.md review). ``QUOTE_RE`` caps a matched quotation at 800
    characters (raised from 400): a real quotation longer than the cap
    used to desynchronise the tool's open/close pairing for every
    following quotation on the *whole page*, since matching ran once over
    the entire flattened text — the regex, unable to find a real closing
    mark within the cap, backtracked onto some quote mark inside the
    quotation's own true (longer) text, then read the quotation's real
    closing mark as the *opening* mark of the next match, and so on,
    which could mask a real wording change anywhere in the shifted zone
    (042-onome.md's 437-character quotation did exactly this). Splitting
    on a blank line first and flattening (whitespace-normalising) each
    paragraph independently, before matching, means a mismatch can now
    span at most one paragraph, and a paragraph whose own quote marks
    still don't pair up (an odd count of them: the shape of a quotation
    still longer than 800 characters, or a stray unmatched mark) is
    reported as a printed ``WARN`` naming the page and the paragraph,
    rather than silently resolved by whatever the regex pairs next.

    Returns ``(quote counts, warning lines)``.
    """
    text = INCH_RE.sub("″", text)  # ″, so QUOTE_RE never pairs it
    counts: Counter = Counter()
    warnings: list[str] = []
    for para in _PARA_SPLIT_RE.split(text):
        flat = normalize_ws(para)
        if not flat:
            continue
        n_marks = len(re.findall(r'["“”]', flat))
        if n_marks % 2:
            warnings.append(
                f"{page_label}: WARN odd number of quote marks ({n_marks}) "
                f"in a paragraph starting {flat[:70]!r}"
            )
        for m in QUOTE_RE.finditer(flat):
            inner = m.group(1) if m.group(1) is not None else m.group(2)
            inner = normalize_ws(inner)
            if inner:
                counts[inner] += 1
    return counts, warnings


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


def extract_all(
    text: str, page_label: str = "",
) -> tuple[dict[str, Counter], dict[tuple[str, ...], list[str]], list[str], list[str]]:
    defs: dict[str, str] = {}
    for label, body in DEF_RE.findall(text):
        defs[label] = normalize_ws(body)
    body_text = DEF_RE.sub("", text)

    # Extract {ref}/{term}/{doc} roles and remove them BEFORE any inline-
    # code masking (G15/T-new-1: see ROLE_RE's comment above). The role's
    # own content is whitespace-flattened before being recorded, so a role
    # target hard-wrapped across a source line break compares the same
    # after a harmless re-wrap as before it (the same reasoning that
    # already flattens quotes/hedges below).
    refs: Counter = Counter()

    def _role_sub(m: re.Match) -> str:
        refs[role_target(normalize_ws(m.group(1)))] += 1
        return " "

    body_text = ROLE_RE.sub(_role_sub, body_text)

    # Strip inline-code backtick delimiters now that roles are already
    # gone (its content is kept): see _mask_inline_code.
    body_text = _mask_inline_code(body_text)

    markers = Counter(MARKER_RE.findall(body_text))

    masked = body_text
    urls, masked = extract_urls_masked(masked)
    masked = MARKER_RE.sub(" ", masked)
    # Layout-only directive options (":widths: 16 20 28 12 24", etc.) are
    # never content (review C2, rd-overview finding 2): masked out here,
    # before quotes/hedges/numbers/identifiers ever see them, so a
    # captioned table's own layout metadata can never be misread as prose.
    masked = _LAYOUT_OPTION_RE.sub(" ", masked)

    # Flatten before matching, per PARAGRAPH (review finding H1; Guide
    # problem 16, rd-steps-035-047.md review section D): the repository's
    # markdown is hard-wrapped, so a quotation frequently spans a source
    # line break. QUOTE_RE forbids "\n" inside a match, so applied to the
    # raw text it silently misses every such quotation (measured: ~29% of
    # all quotations on this repository's pages) — invisible to a wording
    # change inside one, and it flags a false LOST/ADDED pair whenever a
    # harmless re-wrap moves where a quotation happens to cross a line.
    # Flattening fixes both: a wrapped quotation is matched as one run,
    # and re-wrapping it changes no character of that run. Flattening
    # scoped to one paragraph at a time (rather than the whole page)
    # keeps a quotation over the (now 800-char) cap from desynchronising
    # every later quote on the page: a mismatch can now span at most one
    # paragraph, and an odd quote-mark count within it is printed as a
    # WARN rather than silently resolved by whatever the regex happens
    # to pair next.
    quotes, quote_warnings = extract_quotes(masked, page_label)
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
    numbers_stream_text = _LEADING_LIST_MARKER_RE.sub(" ", masked_for_numbers)
    numbers = extract_numbers(numbers_stream_text)
    number_order, number_order_samples, number_blocks = extract_number_order(masked_for_numbers)
    footnotes = Counter(f"[^{label}]: {text}" for label, text in defs.items())
    # The page's numeric tokens, left to right, ignoring all unit
    # boundaries (review C3, rd-overview finding 3): used only by
    # check_regrouped, to recognise a LOST number_order tuple that still
    # occurs, unchanged and in the same order, as a contiguous run
    # somewhere in the *other* page's stream -- i.e. the same numbers were
    # only regrouped into different rows/items/sentences, which is exactly
    # what R-TABLE/R-LIST does to a numeric prose sequence. Computed from
    # the same fully-masked text as `numbers`/`number_order`, so widths
    # and identifiers never enter it.
    stream = _number_tokens_ordered(numbers_stream_text)
    order_context = {"stream": stream, "blocks": number_blocks}

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
    }, number_order_samples, order_context, quote_warnings


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
# --allow-deduplicated (rd-materials.md review, "D1"): R-QUICKFACTS asks a
# writer to delete a quick-facts cell's copy of a value that the body also
# states, once it is checked to be there. The multiset check cannot tell
# that apart from a real deletion by itself, so a blanket "ignore lost
# quotes/markers/numbers" would hide a genuine loss (the review's own H1
# finding, a body clause dropped outright). The patch is narrow instead.

_CLASS_PAGE_RE = re.compile(r"(?:^|/)docs/(?:machines|materials)/[^/]+\.md$")


def is_class_page(page_path: str) -> bool:
    return bool(_CLASS_PAGE_RE.search(page_path.replace("\\", "/")))


def _split_summary(text: str) -> tuple[str, str]:
    """Split ``text`` at the first ATX H2 (``^## ``): (everything before
    it -- the quick-facts table and any short intro above it -- and
    everything from it onward -- the body)."""
    m = re.search(r"^## ", text, re.MULTILINE)
    if not m:
        return text, ""
    return text[: m.start()], text[m.start():]


def check_deduplicated(
    old_text: str, new_text: str, page_path: str,
) -> dict[str, tuple[Counter, Counter, Counter, Counter]]:
    """For a class page (``docs/machines/*.md``, ``docs/materials/*.md``
    only -- condition (c) of the review's patch), the per-half (quick-
    facts summary vs. body) counts of ``quotes``/``markers``/``numbers``
    on both revisions. ``{}`` for any other page, so callers can treat
    "not applicable" and "no losses to excuse" the same way.
    """
    if not is_class_page(page_path):
        return {}
    old_summary, old_body = _split_summary(old_text)
    new_summary, new_body = _split_summary(new_text)
    old_sum_cats = extract_all(old_summary)[0]
    new_sum_cats = extract_all(new_summary)[0]
    old_body_cats = extract_all(old_body)[0]
    new_body_cats = extract_all(new_body)[0]
    return {
        cat: (old_sum_cats[cat], new_sum_cats[cat], old_body_cats[cat], new_body_cats[cat])
        for cat in ("quotes", "markers", "numbers")
    }


def apply_deduplicated(
    cat: str,
    lost: Counter,
    halves: dict[str, tuple[Counter, Counter, Counter, Counter]],
) -> tuple[Counter, list[str]]:
    """Downgrade each item of ``lost`` to a printed ``DEDUPLICATED``
    warning when all three of the review's conditions hold: (a) the
    item's count in the quick-facts summary decreased; (b) its count in
    the body is unchanged, and (c) still >= 1 there. Everything else in
    ``lost`` stays lost (a real, undeclarable loss)."""
    if cat not in halves or not lost:
        return lost, []
    old_sum, new_sum, old_body, new_body = halves[cat]
    still_lost: Counter = Counter()
    info: list[str] = []
    for item, n in lost.items():
        if (
            old_sum[item] > new_sum[item]
            and old_body[item] == new_body[item]
            and new_body[item] >= 1
        ):
            info.append(
                f"DEDUPLICATED (--allow-deduplicated) {cat}: {item!r} removed "
                "from the quick-facts table, unchanged in the body"
            )
        else:
            still_lost[item] = n
    return still_lost, info


# ---------------------------------------------------------------------------
# ``words`` category (rd-steps-064-075.md guide problem 4): none of the nine
# categories above see an ordinary word that carries no number, quotation,
# marker, hedge, role or identifier -- a first draft of 074 lost "removing
# step:" through an overlapping replacement, and every other check passed;
# only an ad hoc word-level diff script caught it. This is a word-multiset
# diff of the page's "open text": everything outside a {dropdown} body, a
# {figure} fence (both generated/managed, never hand-edited prose), a
# generated ``<!-- name:begin -->``...``<!-- name:end -->`` block, and a
# footnote definition. Informational by default (always printed, never
# fails on its own); ``--strict-words`` turns a LOST word that is not in a
# small stop-list of common function words into a failure -- distinctive
# content words like "removing" are not in that list and do fail.

_GENERATED_BLOCK_BEGIN_RE = re.compile(r"^\s*<!--\s*[\w-]+:begin\b")
_GENERATED_BLOCK_END_RE = re.compile(r"^\s*<!--\s*[\w-]+:end\s*-->\s*$")


def _figure_fence_lines(text: str) -> set[int]:
    """1-based line numbers inside a ``{figure}`` fence, the same stack-
    based scan ``check_inforce.dropdown_lines`` uses for ``{dropdown}``,
    just watching for the ``figure`` directive name instead."""
    inside: set[int] = set()
    stack: list[tuple[str, int, bool]] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        if stack and any(is_fig for _, _, is_fig in stack):
            inside.add(lineno)
        m = check_inforce.FENCE_OPEN_RE.match(line)
        if m:
            marker, name = m.group(1), m.group(2)
            is_figure = name == "figure"
            stack.append((marker[0], len(marker), is_figure))
            if is_figure:
                inside.add(lineno)
            continue
        m = check_inforce.FENCE_BARE_RE.match(line)
        if m:
            marker = m.group(1)
            if stack and stack[-1][0] == marker[0] and len(marker) >= stack[-1][1]:
                stack.pop()
    return inside


def open_text_lines(text: str) -> set[int]:
    """1-based line numbers of ``text`` that are "open text" for the
    ``words`` category: outside a ``{dropdown}`` body, a ``{figure}``
    fence, a generated block, and a footnote definition."""
    lines = text.splitlines()
    excluded = check_inforce.dropdown_lines(text) | _figure_fence_lines(text)
    in_generated = False
    for i, line in enumerate(lines, start=1):
        if _GENERATED_BLOCK_BEGIN_RE.match(line):
            in_generated = True
        if in_generated:
            excluded.add(i)
        if _GENERATED_BLOCK_END_RE.match(line):
            in_generated = False
    for m in DEF_RE.finditer(text):
        start_line = text.count("\n", 0, m.start()) + 1
        end_line = text.count("\n", 0, m.end()) + 1
        excluded.update(range(start_line, end_line + 1))
    return {ln for ln in range(1, len(lines) + 1) if ln not in excluded}


def _mask_prose(text: str) -> str:
    """Roles, inline code, URLs, footnote markers and layout-option lines
    stripped -- the same masking ``extract_all`` applies, as a standalone
    helper for text that is not a whole page (``extract_words`` runs it on
    a filtered subset of the page's lines, so it cannot reuse
    ``extract_all``'s own line-numbered ``body_text`` directly)."""
    text = ROLE_RE.sub(" ", text)
    text = _mask_inline_code(text)
    text = MARKER_RE.sub(" ", text)
    _, text = extract_urls_masked(text)
    text = _LAYOUT_OPTION_RE.sub(" ", text)
    return text


_WORD_RE = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)*")

# A small stop-list of common function words (--strict-words): natural
# rewording -- splitting or joining sentences, adding a subject and verb
# -- constantly shifts their counts by one or two with no content lost, so
# strict mode would otherwise be unusable. A distinctive content word
# (e.g. "removing") is deliberately not in this list.
WORDS_STOPLIST = frozenset({
    "a", "an", "the", "and", "or", "but", "nor", "so", "yet", "of", "to",
    "in", "on", "at", "by", "for", "with", "as", "is", "are", "was",
    "were", "be", "been", "being", "it", "its", "this", "that", "these",
    "those", "which", "who", "whom", "whose", "not", "no", "do", "does",
    "did", "has", "have", "had", "can", "will", "would", "could",
    "should", "into", "onto", "than", "then", "also", "each", "any",
    "all", "some", "one", "two", "three", "such", "if", "when", "while",
    "because", "thus", "there", "here",
})


def extract_words(text: str) -> Counter:
    """Case-folded word-multiset of ``text``'s open text (see
    ``open_text_lines``)."""
    lines = text.splitlines()
    keep = open_text_lines(text)
    kept_lines = [lines[i - 1] for i in sorted(keep) if 1 <= i <= len(lines)]
    open_text = _mask_prose("\n".join(kept_lines))
    return Counter(w.lower() for w in _WORD_RE.findall(open_text))


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


def _contiguous(t: tuple[str, ...], stream: list[str]) -> bool:
    """Whether ``t`` occurs, in order and with nothing else interleaved,
    somewhere in ``stream`` (a plain sliding-window check)."""
    n = len(t)
    if n == 0 or n > len(stream):
        return False
    return any(tuple(stream[k : k + n]) == t for k in range(len(stream) - n + 1))


def _moved_within_block(
    t: tuple[str, ...],
    src_blocks: list[list[tuple[str, ...]]],
    dst_blocks: list[list[tuple[str, ...]]],
) -> bool:
    """Whether the unit tuple ``t`` of a ``src_blocks`` block reappears in
    ``dst_blocks`` as a block with exactly the same numbers (as a
    multiset) in which no single unit carries ``t``'s numbers -- i.e. the
    numbers stayed together in their paragraph, list item or table but
    the unit was split and its parts reordered (dash or parenthetical
    material moved to directly after its sentence, R-SENTENCE step 1).

    Three guards keep real swaps out. A transposition inside one
    sentence is not excused: the new sentence is then one unit with the
    same multiset as ``t``. A swap between blocks is not excused, because
    the block multisets then differ. And a one-number-per-row regroup
    whose rows changed order (the stream check's own swap case) is not
    excused either: every destination unit with two or more numbers must
    keep them in ``t``'s order (an in-order subsequence of ``t``) or be a
    unit the source block already had, and at least one such multi-number
    unit must exist -- moved dash material always leaves one.

    Seen from the other side (``t`` is a fragment the split produced,
    reported as ADDED), the same move shows as a destination unit that
    holds ``t``'s numbers in order among others: accepted on the same
    block-multiset condition.
    """
    t_multiset = Counter(t)

    def in_order(part: tuple[str, ...], whole: tuple[str, ...]) -> bool:
        k = 0
        for n in part:
            k = next((j for j in range(k, len(whole)) if whole[j] == n), -1) + 1
            if k == 0:
                return False
        return True

    for src in src_blocks:
        if t not in src:
            continue
        src_multiset = Counter(n for unit in src for n in unit)
        src_units = set(src)
        for dst in dst_blocks:
            if Counter(n for unit in dst for n in unit) != src_multiset:
                continue
            if any(Counter(unit) == t_multiset for unit in dst):
                continue
            # t was the whole unit: its parts are now separate units, each in order
            multi = [unit for unit in dst if len(unit) >= 2 and unit not in src_units]
            if multi and all(in_order(unit, t) for unit in multi):
                return True
            # t is a fragment: some unit holds all of t's numbers, in order, among others
            if any(len(unit) > len(t) and in_order(t, unit) for unit in dst):
                return True
    return False


def check_regrouped(
    lost_no: Counter,
    added_no: Counter,
    old_stream: list[str],
    new_stream: list[str],
    old_samples: dict[tuple[str, ...], list[str]],
    new_samples: dict[tuple[str, ...], list[str]],
    old_blocks: list[list[tuple[str, ...]]] | None = None,
    new_blocks: list[list[tuple[str, ...]]] | None = None,
) -> tuple[Counter, Counter, list[str]]:
    """``--allow-regrouped`` (review T1, redesigned per review C3 for
    rd-overview finding 3): reclassify a ``number_order`` LOST tuple as an
    informational REGROUPED line, rather than an error, when it still
    occurs — same numbers, same order, nothing interleaved — as a
    contiguous run in the *other* page's flat, left-to-right numeric-token
    stream (``extract_all``'s ``"_stream"``, built after masking widths,
    identifiers, roles etc. away, so only real content numbers are in it).
    Symmetric for an ADDED tuple checked against the old page's stream (a
    table or list collapsed into prose).

    This one check replaces four narrower ones from the first design. It
    directly covers the case that design could not: R-TABLE/R-LIST turning
    one multi-number unit into several rows/items with only *one* number
    each. Each such row/item alone falls below ``extract_number_order``'s
    2-or-more-numbers-per-unit threshold, so *no* per-unit ADDED tuple
    exists at all to "cover" the LOST one — the old design required at
    least one, the stream check does not, because it looks at the page's
    numbers directly rather than at how they happen to be grouped into
    units on the new side.

    A real swap is still caught: transposing two numbers, whether within
    one unit, between adjacent table rows, or between list items, breaks
    contiguity in the stream (the exact sequence no longer appears
    anywhere, in that order, with nothing else run through it), so it
    stays a real, undeclarable LOST/ADDED difference.

    Known limit — not multiplicity-aware: if a tuple's digits occur twice
    in one page and only one copy survives on the other, the survivor
    still satisfies "occurs as a contiguous run", so the loss of the
    second copy is excused too. Rare in practice (it requires the same
    multi-number grouping to appear verbatim twice on one page) and
    already flagged by the plain ``numbers``/``identifiers`` categories if
    the vanished copy's own text otherwise differed; not a substitute for
    the reviewer reading the diff (see the module docstring).

    Returns ``(still-lost, still-added, info lines)``: the LOST/ADDED
    tuples that were *not* explained as a regroup (still errors), and
    human-readable lines reporting what was excused and why.
    """
    lines: list[str] = []
    still_lost: Counter = Counter()
    still_added: Counter = Counter()
    # Second condition (review rd-steps-118-134 D4; batch-8 guide problem
    # 3): the same numbers, in the same block, in a different order, with
    # the unit split -- moved dash or parenthetical material. Still an
    # informational line the reviewer re-pairs by hand.
    old_blocks = old_blocks or []
    new_blocks = new_blocks or []
    for t, c in lost_no.items():
        if _contiguous(t, new_stream):
            lines.append(f"REGROUPED (--allow-regrouped) number_order, was: {t}")
            for sample in old_samples.get(t, [])[:1]:
                lines.append(f"    was: {sample!r}")
        elif _moved_within_block(t, old_blocks, new_blocks):
            lines.append(f"REGROUPED (--allow-regrouped) number_order, moved within its block, was: {t}")
            for sample in old_samples.get(t, [])[:1]:
                lines.append(f"    was: {sample!r}")
        else:
            still_lost[t] = c
    for t, c in added_no.items():
        if _contiguous(t, old_stream):
            lines.append(f"REGROUPED (--allow-regrouped) number_order, now: {t}")
            for sample in new_samples.get(t, [])[:1]:
                lines.append(f"    now: {sample!r}")
        elif _moved_within_block(t, new_blocks, old_blocks):
            lines.append(f"REGROUPED (--allow-regrouped) number_order, moved within its block, now: {t}")
            for sample in new_samples.get(t, [])[:1]:
                lines.append(f"    now: {sample!r}")
        else:
            still_added[t] = c
    return still_lost, still_added, lines


# ---------------------------------------------------------------------------
# Two informational quality checks writers keep failing (task instruction,
# not tied to one review finding): run once against the CURRENT page text,
# not a before/after diff, and always print WARN with page and line; never
# fail the run.

_GLANCE_ADMONITION_RE = re.compile(
    r"^([:]{3,})\{admonition\}[ \t]*At a glance[ \t]*\n(.*?)\n\1[ \t]*$",
    re.MULTILINE | re.DOTALL,
)


def check_glance_recurrence(text: str, page_label: str) -> list[str]:
    """Every "At a glance" bullet's numbers and footnote markers must
    recur somewhere in the body below the box: writers keep trimming the
    box down to a claim the body itself no longer makes (or no longer
    cites)."""
    warns: list[str] = []
    m = _GLANCE_ADMONITION_RE.search(text)
    if not m:
        return warns
    glance_body = m.group(2)
    after_body = DEF_RE.sub("", text[m.end():])
    after_masked = _mask_prose(after_body)
    after_numbers = extract_numbers(IDENT_RE.sub(" ", after_masked))
    after_markers = set(MARKER_RE.findall(after_body))
    glance_start_line = text.count("\n", 0, m.start(2)) + 1
    for offset, line in enumerate(glance_body.splitlines()):
        if not line.strip().startswith("*"):
            continue
        lineno = glance_start_line + offset
        line_masked = _mask_prose(line)
        for tok in extract_numbers(IDENT_RE.sub(" ", line_masked)).elements():
            if after_numbers[tok] < 1:
                warns.append(
                    f"{page_label}:{lineno}: WARN glance number {tok!r} does "
                    "not recur in the body below"
                )
        for mk in MARKER_RE.findall(line):
            if mk not in after_markers:
                warns.append(
                    f"{page_label}:{lineno}: WARN glance marker [^{mk}] does "
                    "not recur in the body below"
                )
    return warns


_SKYWATER_SAYS_RE = re.compile(r"^[ \t]*[-*][ \t]*\*SkyWater says:\*")
_BULLET_START_RE = re.compile(r"^[ \t]*[-*][ \t]")
_SKW_CYP_MARKER_RE = re.compile(r"\[\^(?:skw|cyp)-[A-Za-z0-9_-]+\]")


def check_skywater_says(text: str, page_label: str) -> list[str]:
    """Every "*SkyWater says:*" line (or the bullet it starts, if it
    wraps) must contain a quotation mark or a ``skw-``/``cyp-`` footnote
    marker: writers keep paraphrasing what SkyWater's own page says
    without either quoting it or citing it."""
    warns: list[str] = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not _SKYWATER_SAYS_RE.match(line):
            continue
        block = [line]
        j = i + 1
        while j < len(lines) and lines[j].strip() and not _BULLET_START_RE.match(lines[j]):
            block.append(lines[j])
            j += 1
        joined = " ".join(block)
        has_quote = '"' in joined or "“" in joined or "”" in joined
        has_marker = bool(_SKW_CYP_MARKER_RE.search(joined))
        if not has_quote and not has_marker:
            warns.append(
                f"{page_label}:{i + 1}: WARN '*SkyWater says:*' line has no "
                "quotation mark or skw-/cyp- marker"
            )
    return warns


def diff_page(
    old_text: str,
    new_text: str,
    allowed: frozenset[str] = frozenset(),
    allow_dropdown_edits: bool = False,
    allow_regrouped: bool = False,
    page_path: str = "",
    allow_deduplicated: bool = False,
    strict_words: bool = False,
) -> list[tuple[bool, str]]:
    """Return (is_failure, message) pairs; does not print anything."""
    results: list[tuple[bool, str]] = []
    old, old_samples, old_ctx, old_quote_warnings = extract_all(old_text, f"{page_path} (before)")
    new, new_samples, new_ctx, new_quote_warnings = extract_all(new_text, f"{page_path} (after)")
    for w in old_quote_warnings + new_quote_warnings:
        results.append((False, w))
    dedup_halves = check_deduplicated(old_text, new_text, page_path) if allow_deduplicated else {}
    for cat in CATEGORIES:
        lost = old[cat] - new[cat]
        added = new[cat] - old[cat]
        limit = _DISPLAY_LIMIT.get(cat, 100)
        if cat == "number_order" and allow_regrouped and (lost or added):
            lost, added, extra = check_regrouped(
                lost, added, old_ctx["stream"], new_ctx["stream"], old_samples, new_samples,
                old_ctx["blocks"], new_ctx["blocks"],
            )
            for line in extra:
                results.append((False, line))
        if allow_deduplicated and lost:
            lost, dedup_info = apply_deduplicated(cat, lost, dedup_halves)
            for line in dedup_info:
                results.append((False, line))
        if lost:
            results.append((True, f"LOST {cat}: {format_counter(lost, limit)}"))
        if added:
            is_fail = cat not in allowed
            tag = "ADDED" if is_fail else "ADDED (declared)"
            results.append((is_fail, f"{tag} {cat}: {format_counter(added, limit)}"))
    if not allow_dropdown_edits:
        for msg in compare_dropdowns(old_text, new_text):
            results.append((True, msg))

    # ``words`` (not one of the nine CATEGORIES: it has its own, separate
    # gate, --strict-words, rather than --allow-added).
    old_words = extract_words(old_text)
    new_words = extract_words(new_text)
    lost_words = old_words - new_words
    added_words = new_words - old_words
    if lost_words:
        results.append((False, f"WORDS LOST: {format_counter(lost_words)}"))
    if added_words:
        results.append((False, f"WORDS ADDED: {format_counter(added_words)}"))
    if strict_words and lost_words:
        strict_lost = Counter({w: n for w, n in lost_words.items() if w not in WORDS_STOPLIST})
        if strict_lost:
            results.append((True, f"LOST words (--strict-words): {format_counter(strict_lost)}"))

    # Two informational checks against the CURRENT page only (not a diff).
    for w in check_glance_recurrence(new_text, page_path):
        results.append((False, w))
    for w in check_skywater_says(new_text, page_path):
        results.append((False, w))

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
    case(
        "a numbered bold run-in label immediately followed by ** does not "
        "fuse its digits with the next sentence's, so R-H3 does not report "
        "a false number_order LOST (rd-overview finding 1 / review C1)",
        "# P\n\n**Metal 4, second MiM capacitor, via 4 and metal 5.** The "
        "second capacitor sits on metal 4.[^a]\n\n"
        "[^a]: Source. <https://example.com/a>\n",
        "# P\n\n### Metal 4, second MiM capacitor, via 4 and metal 5\n\n"
        "The second capacitor sits on metal 4.[^a]\n\n"
        "[^a]: Source. <https://example.com/a>\n",
        True,
    )
    case(
        "a :::{table} caption / :widths: pair adds no undeclared numbers "
        "or number_order (rd-overview finding 2 / review C2): the caption "
        "sentence is kept as content, the fence and :widths: line are not",
        "# P\n\nSee the numbers 16 and 20 in the caption below.[^a]\n\n"
        "| Level | Width |\n|---|---|\n| 1 | 16 |\n| 2 | 20 |\n"
        "\n[^a]: Source. <https://example.com/a>\n",
        "# P\n\n:::{table} See the numbers 16 and 20 in the caption below.[^a]\n"
        ":widths: 30 70\n\n"
        "| Level | Width |\n|---|---|\n| 1 | 16 |\n| 2 | 20 |\n:::\n"
        "\n[^a]: Source. <https://example.com/a>\n",
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
    # -- gap 3 (rd-overview finding 3): a numeric prose sequence regrouped
    # into a table/list with only *one* number per row/item. Each row/item
    # alone is below the 2-number tracking threshold, so no per-unit ADDED
    # tuple exists at all -- the original T1 design required one and so
    # rejected this unconditionally; the stream-contiguity redesign (C3)
    # does not need one.
    _regroup_singleton_old = (
        "# P\n\nThe count is 2, 3 and 4 masks per tier.[^a]\n"
        "\n[^a]: Source. <https://example.com/a>\n"
    )
    _regroup_singleton_new = (
        "# P\n\n| Tier | Masks |\n|---|---|\n| A | 2 |\n| B | 3 |\n"
        "| C | 4[^a] |\n\n[^a]: Source. <https://example.com/a>\n"
    )
    case(
        "a numeric prose sequence regrouped into one-number-per-row table "
        "rows is accepted under --allow-regrouped",
        _regroup_singleton_old, _regroup_singleton_new, True, allow_regrouped=True,
    )
    case(
        "the same one-number-per-row regroup still fails without --allow-regrouped",
        _regroup_singleton_old, _regroup_singleton_new, False,
    )
    case(
        "a real swap between rows in a one-number-per-row regroup is still "
        "caught, even with --allow-regrouped",
        _regroup_singleton_old,
        "# P\n\n| Tier | Masks |\n|---|---|\n| A | 3 |\n| B | 2 |\n"
        "| C | 4[^a] |\n\n[^a]: Source. <https://example.com/a>\n",
        False,
        allow_regrouped=True,
    )
    case(
        "the same one-number-per-row regroup as a bulleted list, not a "
        "table, is also accepted under --allow-regrouped",
        _regroup_singleton_old,
        "# P\n\n* Tier A: 2\n* Tier B: 3\n* Tier C: 4[^a]\n"
        "\n[^a]: Source. <https://example.com/a>\n",
        True,
        allow_regrouped=True,
    )

    # -- moved within a block (review rd-steps-118-134 D4) ----------------
    _moved_old = (
        "# P\n\nThe etch clears 0.17 µm -- about 0.08 µm over 0.5 µm at 10 degrees -- "
        "in 40 s.[^a]\n\n[^a]: Source. <https://example.com/a>\n"
    )
    _moved_new = (
        "# P\n\nThe etch clears 0.17 µm in 40 s.[^a] That is about 0.08 µm over "
        "0.5 µm at 10 degrees.\n\n[^a]: Source. <https://example.com/a>\n"
    )
    case(
        "dash material moved to directly after its sentence, same paragraph, is "
        "accepted under --allow-regrouped",
        _moved_old, _moved_new, True, allow_regrouped=True,
    )
    case(
        "the same move still fails without --allow-regrouped",
        _moved_old, _moved_new, False,
    )
    case(
        "a transposition inside one sentence is still caught with --allow-regrouped",
        "# P\n\nThe ratio is 6 of 171 wafers.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        "# P\n\nThe ratio is 171 of 6 wafers.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        False,
        allow_regrouped=True,
    )
    case(
        "dash material moved into a different paragraph is still caught",
        _moved_old + "\nAnother paragraph, 900 °C.\n",
        "# P\n\nThe etch clears 0.17 µm in 40 s.[^a]\n\nAnother paragraph, 900 °C. "
        "That is about 0.08 µm over 0.5 µm at 10 degrees.\n\n[^a]: Source. <https://example.com/a>\n",
        False,
        allow_regrouped=True,
    )
    case(
        "a lead-in number moved into the table it introduces is accepted under --allow-regrouped",
        "# P\n\nThree tiers, 9 masks in all:[^a]\n\n| Tier | Masks |\n|---|---|\n| A | 2 |\n| B | 3 |\n| C | 4 |\n"
        "\n[^a]: Source. <https://example.com/a>\n",
        "# P\n\nThree tiers:[^a]\n\n| Tier | Masks |\n|---|---|\n| A | 2 |\n| B | 3 |\n| C | 4 |\n| All | 9 |\n"
        "\n[^a]: Source. <https://example.com/a>\n",
        True,
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
        "rd-categories.md review finding H: dropping 'of order' and "
        "'light' narrows an approximation and must be caught (reproduced "
        "against main's copy of the tool: previously undetected)",
        "# P\n\nThreshold-adjust uses light doses of order "
        "10e12-10e13 cm-2.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        "# P\n\nThreshold-adjust uses 10e12-10e13 cm-2.[^a]\n\n"
        "[^a]: Source. <https://example.com/a>\n",
        False,
    )
    case(
        "the new hedge words ('roughly', 'of the order of', 'typically', "
        "'usually', 'likely') are each individually tracked",
        "# P\n\nA roughly typical value, of the order of 900 degC, "
        "usually and likely so.[^a]\n\n[^a]: Source. <https://example.com/a>\n",
        "# P\n\nA typical value, 900 degC, so.[^a]\n\n"
        "[^a]: Source. <https://example.com/a>\n",
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
        extracted, _, _, _ = extract_all(f"# P\n\n{body}\n")
        if extracted["numbers"]:
            problems.append(f"{name}: expected no numbers, got {dict(extracted['numbers'])}")

    def assert_has_number(name: str, body: str, expected: str) -> None:
        extracted, _, _, _ = extract_all(f"# P\n\n{body}\n")
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

    def assert_numbers(name: str, body: str, expected: set[str]) -> None:
        extracted, _, _, _ = extract_all(f"# P\n\n{body}\n")
        got = set(extracted["numbers"].elements())
        if got != expected:
            problems.append(f"{name}: expected numbers {expected!r}, got {got!r}")

    # -- C4: a space-grouped number must not over-run into a following,
    # unrelated number. A bare 1-3 digit number directly followed by a
    # space and a 3-or-4-digit number used to tokenise as a bogus grouped
    # number plus a stray leftover digit ("4 2020" -> "4 202" + "0";
    # rd-overview review section C, finding C4, reported as "Q4 2020" --
    # reproduced here without the leading letter, which this repository's
    # own identifier masking (T2, already on main) already protects "Q4"
    # with, unlike the reviewer's prototype tool). A real space-grouped
    # thousands number ("3 200") must still work.
    assert_numbers(
        "a bare number directly followed by a year-like number is not "
        "mis-split into a bogus grouped number (C4: 'Q4 2020' -> "
        "'4 202' + '0')",
        "The value is 4 2020, next to 3 200 wafers.",
        {"4", "2020", "3 200"},
    )

    def assert_refs(name: str, body: str, expected: set[str]) -> None:
        extracted, _, _, _ = extract_all(f"# P\n\n{body}\n")
        got = set(extracted["refs"].elements())
        if got != expected:
            problems.append(f"{name}: expected refs {expected!r}, got {got!r}")

    # -- rd-site review finding L5: ROLE_RE has no notion of inline-code
    # nesting and scans forward for the next backtick regardless, so a
    # role shown as a literal code-span example (documenting the syntax
    # itself, not using it) is misread as a real role invocation.
    assert_refs(
        "a role shown as a literal inline-code example is not read as a "
        "real role invocation (L5: ROLE_RE runs through the code span's "
        "own backtick)",
        "Write a term link by wrapping it as `{term}`sense`` in the source.",
        set(),
    )
    assert_refs(
        "a genuine role still resolves normally after inline-code masking",
        "See {ref}`overview-modules` for details.",
        {"overview-modules"},
    )
    assert_refs(
        "a genuine role right after an unrelated inline code span still "
        "resolves (the code span's own backtick is not consumed into the "
        "role's)",
        "Set `nfet_01v8` then see {ref}`overview-modules` for details.",
        {"overview-modules"},
    )
    assert_refs(
        "a stray unmatched backtick earlier in the paragraph cannot "
        "swallow a later genuine role's own opening backtick",
        "Note the ` odd stray mark, then see {ref}`overview-modules` for "
        "details.",
        {"overview-modules"},
    )

    # -- G15 / T-new-1 (rd-steps-035-047.md review section D; rd-steps-014-
    # 034.md review): a role's own CLOSING backtick, followed later on the
    # same line by an unrelated inline code span, used to be treated as a
    # fresh opening delimiter for that later span, swallowing every word
    # of ordinary prose (a hedge, another role) in between and leaving the
    # role's own target unmatched. Reproduced on the exact three pages the
    # batch-2 progress file named.
    def assert_refs_and_hedges(
        name: str, body: str, expected_refs: set[str], expected_hedges: set[str]
    ) -> None:
        extracted, _, _, _ = extract_all(f"# P\n\n{body}\n")
        got_refs = set(extracted["refs"].elements())
        got_hedges = set(extracted["hedges"].elements())
        if got_refs != expected_refs:
            problems.append(f"{name}: expected refs {expected_refs!r}, got {got_refs!r}")
        if got_hedges != expected_hedges:
            problems.append(f"{name}: expected hedges {expected_hedges!r}, got {got_hedges!r}")

    assert_refs_and_hedges(
        "G15/T-new-1: a role followed on the same line by an unrelated "
        "code span no longer eats the hedged prose between them "
        "(docs/steps/017-nwm.md:227)",
        "{ref}`PWBM <step-026>`, whose reticle, we infer, covers the "
        "`nwell` regions.",
        {"step-026"},
        {"we infer"},
    )
    assert_refs_and_hedges(
        "G15/T-new-1: the same bug, a second role and hedge afterwards "
        "(docs/steps/022-hvtpm.md:227)",
        "{ref}`LVTNM <step-014>` (`lvtn`, which may not overlap `hvtp`).",
        {"step-014"},
        {"may"},
    )
    assert_refs(
        "G15/T-new-1: a {term} role followed by more code-styled text on "
        "the same line (docs/steps/014-lvtnm.md:315)",
        "Whether the reticle opens *over* `lvtn` (and `LVTNI` is a "
        "{term}`counter-doping` implant) or *everywhere except* `lvtn`.",
        {"counter-doping"},
    )

    # -- inch marks (checkers review, "check_preserved.py quote finding"):
    # a straight-quote inch mark right before a real closing quote used to
    # be read as a quote delimiter itself, which mis-paired every
    # quotation after it on the page. Checked directly against
    # extract_quotes/INCH_RE, since these are single-text assertions.
    def assert_quotes(name: str, text: str, expected: set[str]) -> None:
        got = set(extract_quotes(text)[0].elements())
        if got != expected:
            problems.append(f"{name}: expected quotes {expected!r}, got {got!r}")

    assert_quotes(
        'an inch mark inside a quotation ("a, 8"" b "c"")',
        '"a, 8"" b "c"',
        {"a, 8″", "c"},
    )
    assert_quotes(
        'an inch mark behind a closing bracket ("(8")" x "y"")',
        '"(8")" x "y"',
        {"(8″)", "y"},
    )
    if INCH_RE.sub("″", '("Fab 4")"') != '("Fab 4")"':
        problems.append('a nested quotation ending in a number ("Fab 4")" is changed by INCH_RE')
    assert_quotes(
        "a standalone inch-mark measurement outside any quotation is untouched",
        'The die is 8" across, with no quotation anywhere in this sentence.',
        set(),
    )

    # -- Guide problem 16 (rd-steps-035-047.md review section D; rd-steps-
    # 014-034.md review): a quotation over the old 400-char cap used to
    # desynchronise the whole page's quote pairing. Reproduced against
    # main's copy of the tool by hand before this fix (a 479-character
    # quotation, well under the new 800 cap, made a real wording change in
    # a *later*, unrelated quotation invisible -- diff_page reported no
    # failure at all). Cap raised to 800 and matching scoped to one
    # paragraph at a time fixes both.
    _long_quote_filler = ("filler word " * 40).strip()  # 479 chars: > 400, <= 800
    case(
        "a >400-char quotation elsewhere on the page no longer masks a "
        "real wording change in a later quotation (Guide problem 16)",
        f'# P\n\nA source says "{_long_quote_filler}" here.[^a]\n\n'
        'Another source says "original wording" too.[^b]\n\n'
        "[^a]: Source A. <https://example.com/a>\n"
        "[^b]: Source B. <https://example.com/b>\n",
        f'# P\n\nA source says "{_long_quote_filler}" here.[^a]\n\n'
        'Another source says "changed wording" too.[^b]\n\n'
        "[^a]: Source A. <https://example.com/a>\n"
        "[^b]: Source B. <https://example.com/b>\n",
        False,
    )

    def assert_quote_warning(name: str, text: str, expect_substr: str, expect_any: bool) -> None:
        _, warns = extract_quotes(text, "test-page.md")
        found = any(expect_substr in w for w in warns)
        if found != expect_any:
            problems.append(
                f"{name}: expected a warning containing {expect_substr!r}"
                f"{'' if expect_any else ' to be absent'}, got {warns!r}"
            )

    assert_quote_warning(
        "an odd number of quote marks in one paragraph (an unpaired "
        "quotation, e.g. still longer than the cap) is reported as a "
        "WARN naming the page, not silently resolved",
        'A source says "an unterminated quotation with no closing mark '
        "at all here.",
        "odd number of quote marks",
        True,
    )
    assert_quote_warning(
        "a normal, evenly-paired paragraph raises no odd-quote-count warning",
        'A source says "a normal quotation" here.\n\n'
        'Another source says "another normal one" too.',
        "odd number of quote marks",
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

    # -- --allow-deduplicated (rd-materials.md review, "D1") -------------
    _dedup_old = (
        '# Wet chemicals\n\n| | |\n|---|---|\n'
        '| **Example** | SkyWater filings say "some substance".[^skw-01] |\n\n'
        '## Overview\n\n'
        'Elsewhere, the filings say "some substance".[^skw-01] More text.\n\n'
        '[^skw-01]: Source. <https://example.com/a>\n'
    )
    _dedup_new = (
        '# Wet chemicals\n\n| | |\n|---|---|\n'
        '| **Example** | See below.[^skw-01] |\n\n'
        '## Overview\n\n'
        'Elsewhere, the filings say "some substance".[^skw-01] More text.\n\n'
        '[^skw-01]: Source. <https://example.com/a>\n'
    )
    case(
        "a quick-facts cell's copy of a body quotation, deleted, fails "
        "by default",
        _dedup_old, _dedup_new, False, page_path="docs/materials/wet-chemicals.md",
    )
    case(
        "the same deletion is a DEDUPLICATED warning, not a failure, "
        "with --allow-deduplicated on a materials page",
        _dedup_old, _dedup_new, True,
        page_path="docs/materials/wet-chemicals.md", allow_deduplicated=True,
    )
    case(
        "the same deletion still fails with --allow-deduplicated on a "
        "page that is not a class page (condition c)",
        _dedup_old, _dedup_new, False,
        page_path="docs/steps/006-stie.md", allow_deduplicated=True,
    )
    case(
        "a quotation lost from BOTH the quick-facts table and the body "
        "still fails even with --allow-deduplicated (condition b: the "
        "body count must be unchanged)",
        _dedup_old,
        '# Wet chemicals\n\n| | |\n|---|---|\n'
        '| **Example** | See below.[^skw-01] |\n\n'
        '## Overview\n\n'
        'Elsewhere, the filings describe it.[^skw-01] More text.\n\n'
        '[^skw-01]: Source. <https://example.com/a>\n',
        False,
        page_path="docs/materials/wet-chemicals.md", allow_deduplicated=True,
    )

    # -- words category (rd-steps-064-075.md guide problem 4) ------------
    _words_old = (
        "# P\n\nThe process for removing step: strip resist.[^a]\n\n"
        "[^a]: Source. <https://example.com/a>\n"
    )
    _words_new = (
        "# P\n\nThe process for strip resist.[^a]\n\n"
        "[^a]: Source. <https://example.com/a>\n"
    )
    case(
        "a dropped 'removing step:' is informational only by default "
        "(WORDS LOST), and does not fail the run",
        _words_old, _words_new, True,
    )

    def _messages(old: str, new: str, **kw) -> list[str]:
        return [msg for _, msg in diff_page(old, new, **kw)]

    msgs = _messages(_words_old, _words_new)
    if not any("WORDS LOST" in m and "removing" in m for m in msgs):
        problems.append(f"words category: expected a WORDS LOST line naming 'removing', got {msgs!r}")

    case(
        "the same dropped 'removing step:' fails under --strict-words "
        "('removing'/'step' are not in the stop-list)",
        _words_old, _words_new, False, strict_words=True,
    )
    case(
        "--strict-words does not fail on a lost STOP-LIST word alone "
        "(routine rewording constantly shifts common-word counts)",
        "# P\n\nThe the value is stated twice here.[^a]\n\n"
        "[^a]: Source. <https://example.com/a>\n",
        "# P\n\nThe value is stated twice here.[^a]\n\n"
        "[^a]: Source. <https://example.com/a>\n",
        True, strict_words=True,
    )
    case(
        "a word dropped from inside a {dropdown} body never reaches the "
        "words diff (excluded as generated/managed text, not open prose; "
        "--allow-dropdown-edits isolates this from the dropdown-body "
        "check itself)",
        "# P\n\n::::{dropdown} t\nRemoving the old resist here.\n::::\n",
        "# P\n\n::::{dropdown} t\nThe old resist here.\n::::\n",
        True, allow_dropdown_edits=True,
    )
    case(
        "a word dropped from a generated index-links block never reaches "
        "the words diff",
        "# P\n\nBody text.\n\n"
        "<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->\n"
        "Removing related patents here.\n"
        "<!-- index-links:end -->\n",
        "# P\n\nBody text.\n\n"
        "<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->\n"
        "Related patents here.\n"
        "<!-- index-links:end -->\n",
        True,
    )
    case(
        "a word dropped from a {figure} caption never reaches the words "
        "diff",
        "# P\n\n:::{figure} /_static/figures/x.svg\n"
        "Removing the caption word here.\n:::\n",
        "# P\n\n:::{figure} /_static/figures/x.svg\n"
        "The caption word here.\n:::\n",
        True,
    )

    # -- glance-box and "*SkyWater says:*" WARN checks (task instruction) -
    _glance_bad = (
        "# Step 999 -- TEST\n\n"
        "::::{admonition} At a glance\n"
        ":class: at-a-glance\n"
        "* **Does:** a made-up step at 900 degC, see [^skw-01].\n"
        "* **Why:** because.\n"
        "::::\n\n"
        "## What this step is\n\n"
        "This step happens at some temperature.[^skw-01]\n\n"
        "  - *SkyWater says:* runs the process without further detail.\n\n"
        "[^skw-01]: Source. <https://example.com/a>\n"
    )
    case(
        "a glance number/marker not recurring in the body, and a "
        "'*SkyWater says:*' line with neither a quote nor a skw-/cyp- "
        "marker, are printed as WARN but never fail the run",
        _glance_bad, _glance_bad, True,
    )
    glance_msgs = _messages(_glance_bad, _glance_bad)
    if not any("WARN glance number '900'" in m for m in glance_msgs):
        problems.append(f"glance check: expected a WARN for the number 900, got {glance_msgs!r}")
    if not any("SkyWater says" in m and "WARN" in m for m in glance_msgs):
        problems.append(f"SkyWater-says check: expected a WARN line, got {glance_msgs!r}")

    _glance_good = (
        "# Step 999 -- TEST\n\n"
        "::::{admonition} At a glance\n"
        ":class: at-a-glance\n"
        "* **Does:** a made-up step at 900 degC, see [^skw-01].\n"
        "* **Why:** because.\n"
        "::::\n\n"
        "## What this step is\n\n"
        'This step runs at 900 degC, which the facilities page lists as '
        '"the process window".[^skw-01]\n\n'
        "  - *SkyWater says:* \"the process window\".[^skw-01]\n\n"
        "[^skw-01]: Source. <https://example.com/a>\n"
    )
    good_msgs = _messages(_glance_good, _glance_good)
    if any("WARN" in m for m in good_msgs):
        problems.append(
            f"glance/SkyWater-says checks: expected no WARN when the number "
            f"recurs and the SkyWater line is quoted, got {good_msgs!r}"
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
    ap.add_argument(
        "--allow-deduplicated",
        action="store_true",
        help=(
            "on docs/machines/*.md and docs/materials/*.md only: downgrade a LOST in quotes, "
            "markers or numbers to a warning when it disappeared from the quick-facts table "
            "(before the first H2) but is unchanged, and still present, in the body "
            "(rd-materials.md review D1)"
        ),
    )
    ap.add_argument(
        "--strict-words",
        action="store_true",
        help=(
            "fail on any LOST word (the 'words' category) that is not in a small stop-list of "
            "common function words; by default 'words' is informational only (WARN)"
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
        results = diff_page(
            old_text, new_text, allowed, args.allow_dropdown_edits, args.allow_regrouped,
            page_path=rel, allow_deduplicated=args.allow_deduplicated,
            strict_words=args.strict_words,
        )
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
