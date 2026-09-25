#!/usr/bin/env python3
"""Link the first prose occurrence of each glossary term on each page (C9,
docs/plans/readability-guide.md R-TERM rule 2).

Per page, for every glossary term (``docs/glossary.md``), find the first
occurrence of that term's exact wording in running prose and wrap it with a
``{term}`` role, so the term becomes a link on its first use. A term already
linked, or that never occurs in unexcluded prose, is left alone. Nothing
about a page's own text changes except the insertion of ``{term}`...`` or
``{term}`...<slug>``` around an existing span of characters.

**Never touches** (R-TERM rule 2 plus the readability guide's Never list):
headings, code spans (and MyST role/link display text -- always
backtick-delimited in this codebase's style), table lines (both header and
data rows -- broader than the rule's "table header row" alone, out of an
abundance of caution: several checkers compare table cells character for
character, see ``docs/plans/readability-guide.md`` section 5), footnote
definitions, ``## References`` (all three reading-tier lists), quoted text
(straight or curly quotes), directive option lines (``:something: value``,
any directive), ``{dropdown}`` and ``{figure}`` blocks in full (the former
per the Never list section 2.5/2.6, the latter because W1a makes figure
blocks generated content), and the generated
``<!-- index-links:begin -->``/``<!-- index-links:end -->`` block.

**Case.** A term written in the glossary with no ASCII lowercase letter is
treated as an acronym and matched with its exact case only (rule: "case-
sensitive for acronyms") -- this is what keeps ``MOL`` from matching the
unit "mol", ``CAR`` from matching the English word "car", etc. Any other
term is matched in its exact glossary case, or with only its first letter
capitalised (a sentence-initial occurrence); no other case-folding is done.

**Plurals.** For every non-acronym term a simple regular plural of the
whole string is also tried (and for an acronym, the string with a bare "s"
appended), written with the explicit ``{term}`\\`plural <singular>\\``` form
per the rule's own example (`` {term}`vias <via>` ``).

**Ambiguous terms are skipped entirely** (rule 3's `via`, `liner`, `TED`,
plus any this script or its reviewer add -- see ``SKIP_TERMS`` below, each
with a one-line reason). An independent review (M1) additionally measured
a wrong-sense rate per term by reading context, and named
``passivation``, ``extension``, ``erosion``, ``notching``, ``reflow`` and
``footing`` (all far above a 1-in-200 bar) plus the step-code collisions
``SPE``/``SPC`` for the same full-skip treatment; see ``SKIP_TERMS``.
Four more terms are usually right but have one specific wrong-sense
*context* the review could name precisely enough to guard instead of
skip outright -- ``ICP`` ("ICP-MS"), ``DUV`` (a vendor's "-series"
product line), ``TCP`` (next to a model number, "Lam 9400 TCP"), and
``overlay`` (used as a verb) -- see ``CONTEXT_SKIP``: a context-guarded
occurrence is not abandoned, just deferred to the term's next
occurrence on the page.

**At most 3 new links per paragraph** (M2): a term whose first occurrence
would be a paragraph's 4th new link is deferred the same way, to its next
occurrence (in a less crowded paragraph), rather than crowding one
paragraph with a run of blue spans.

**A page can opt a term out explicitly** (M4), with an HTML comment
anywhere in the page: ``<!-- link_terms: skip <term> -->``. This is what
keeps a hand-reverted link (one a human or check_preserved.py rejected)
reverted across a later re-run, which would otherwise have no way to
distinguish "deliberately left unlinked" from "the script just hadn't
found it yet" and would silently re-add it.

Run per directory (one commit per directory, per the branch's task) or on
explicit files:

    uv run python tools/link_terms.py --check docs/steps/*.md
    uv run python tools/link_terms.py docs/steps/*.md
    uv run python tools/link_terms.py --report docs/steps/*.md

``--check`` prints, per page, every term it would link and where, and a
site-wide summary; it writes nothing. ``--report`` prints, per proposed
link, the term and a window of surrounding text (for a reviewer to sample
by eye) and also writes nothing. Without either flag it rewrites the
given files in place. ``--selftest`` runs the offline unit tests.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
GLOSSARY = DOCS / "glossary.md"

# ---------------------------------------------------------------------------
# Terms ambiguous enough that a mechanical first-use link would likely land
# on the wrong sense or the wrong word. Report-C names the first three
# (C9); this script's own dry run and the ten-page spot-check added none
# beyond them, but the mechanism (a "why") is here so the branch's coordinator
# or a future run can extend the list without guessing at the reason.
SKIP_TERMS = {
    "via": "used constantly as the ordinary English preposition ('via a mask', "
           "'via the resist'), not only as the glossary noun",
    "liner": "a liner is named for dozens of different films across the site "
             "('trench liner', 'barrier liner', 'via liner'); linking the bare "
             "word to one glossary sense would mislead more often than it helps",
    "TED": "collides with the italic journal-title abbreviation 'IEEE TED' "
           "(Transactions on Electron Devices), which appears in Deep dive "
           "citations and would be wrongly glossed as transient enhanced "
           "diffusion",
    # tools/check_preserved.py's own ROLE_RE masks a whole matched role
    # ("{term}`...`" and its content) to a single space *before* counting
    # numbers, so that a {ref}'s own step number does not get double-counted
    # as if it were prose. Any glossary term that itself contains a digit
    # therefore always reports an unfixable false "LOST numbers" the moment
    # it is wrapped -- check_preserved has no way to declare a loss as
    # expected, only an addition. Found on docs/machines/wet-bench.md
    # (SC-1/SC-2) and docs/categories/anneal.md (C49 TiSi2) during this
    # branch's own dry runs; verified for all seven digit-bearing glossary
    # terms directly against check_preserved.extract_all before skipping
    # them (see the progress file). Every term below is skipped for this
    # one, shared reason.
    "SC-1": "check_preserved's number-in-role masking (see the comment above)",
    "SC-2": "check_preserved's number-in-role masking (see the comment above)",
    "1T1R": "check_preserved's number-in-role masking (see the comment above)",
    "2-T cell": "check_preserved's number-in-role masking (see the comment above)",
    "C49 TiSi₂": "check_preserved's number-in-role masking (see the comment above)",
    "C54 TiSi₂": "check_preserved's number-in-role masking (see the comment above)",
    "k1": "check_preserved's number-in-role masking (see the comment above)",
    # M1 (independent review of this branch): read the context of every
    # link to these terms plus a random 40-link sample plus every link
    # touching a hyphen/slash/word-joiner (97), and found a wrong-sense
    # rate for each of these far above the 1-in-200 bar -- the glossary
    # names one specific sense, but the site plainly uses the plain
    # English word or a same-spelled different technical sense often
    # enough that a first-occurrence link is more often wrong than right.
    # Counts are the review's own (wrong/total links of that term).
    "passivation": "21/55 wrong: sidewall-etch passivation, post-metal-etch "
        "'passivation step', and interface-trap/H passivation are all "
        "common on this site and are not the glossary's final-dielectric "
        "sense (review M1)",
    "extension": "10/21 wrong: 'HV drain extension' (a drift region), "
        "'extension of tunm beyond the gate' (a design-rule sense), and "
        "'spacer extension' all collide with the glossary's S/D tip/LDD "
        "sense (review M1)",
    "erosion": "6/10 wrong: sputter-target racetrack erosion, resist "
        "erosion and spacer erosion are all common; the glossary's sense "
        "is specifically CMP erosion (review M1)",
    "notching": "4/6 wrong: 'reflective notching' (a lithography effect) "
        "and wafer notching during ingot shaping both collide with the "
        "glossary's plasma-etch-notching sense (review M1)",
    "reflow": "4/4 wrong (small sample, but 100%): every occurrence found "
        "was aluminium/metal reflow, not the glossary's doped-glass reflow "
        "sense (review M1)",
    "footing": "the one occurrence found is resist footing, not the "
        "glossary's etch-footing sense (review M1)",
    # Step CODES that are also glossary acronyms: "the SPE page" / "the
    # SPC page" name step-list codes, not the process terms solid-phase
    # epitaxy / statistical process control. A context guard (page-name
    # vs. step-ref use) would work for the one confirmed SPE case, but
    # SPC was flagged only as "check this too" with no confirmed
    # occurrence to build a guard from, so both are skipped outright
    # rather than guessed at (review M1 items 4 and its own "check SPC
    # too").
    "SPE": "collides with the SPE step code ('the SPE page'); review M1",
    "SPC": "collides with the SPC step code, by the same pattern as SPE; "
        "review M1 flagged it for the same treatment",
    # Found in this branch's own 100-link random sample (seed 20260925,
    # matching the review's own seed), taken after every M1 fix above:
    # docs/steps/153-cap2me.md links "punch-through" in "A fluorine-rich
    # punch-through would thin the cap of every metal-4 line" -- an etch
    # chemistry breaking through a film, not the glossary's source/drain
    # leakage sense. 1 wrong of 10 total occurrences of this term
    # (checked all 10, not just the sampled one; the other 9, including
    # several "punch-through spacing" design-rule names, are the correct
    # sense). See the progress file for the full sample and count.
    "punch-through": "1 of 10 occurrences is an etch-chemistry sense "
        "('a fluorine-rich punch-through'), not the glossary's source/"
        "drain leakage sense; found in this branch's own 100-link sample",
}

# M1 (review, fix items 2-3): terms that are usually right but have a
# specific, narrow wrong-sense context the review could name precisely
# enough to guard instead of skipping the whole term. Each entry is a list
# of (side, regex) pairs; if a regex on the named side matches starting
# right at the candidate span's edge, that specific occurrence is
# rejected -- the term is tried again at its next occurrence on the page,
# it is not skipped everywhere the way SKIP_TERMS is.
CONTEXT_SKIP: dict[str, list[tuple[str, re.Pattern]]] = {
    # "ICP-MS" (a mass-spectrometry technique) is not the glossary's ICP
    # plasma source.
    "ICP": [("after", re.compile(r"^-MS\b"))],
    # A vendor's product line ("Brewer Science DUV-series") is a name, not
    # the glossary's exposure-wavelength sense.
    "DUV": [("after", re.compile(r"^-[Ss]eries\b"))],
    # "Lam 9400 TCP" / "TCP 9600(SE)" / "TCP 9100": TCP next to a vendor
    # model number is part of the model name, not the generic
    # transformer-coupled-plasma technology (review M1 item 2's "model
    # number" guard, `\b\d{3,5}\b` within one token of the match).
    "TCP": [
        ("before", re.compile(r"\d{3,5}\s*$")),
        ("after", re.compile(r"^\s*\(?\d{3,5}\b")),
    ],
    # "overlay" as a verb ("must overlay each other", "overlays a level")
    # is not the glossary's registration-error noun. Per review M1 item 3,
    # the simplest safe rule is to keep only the forms that read as a noun
    # (preceded by an article/adjective) and reject a bare verb-shaped use
    # (preceded by "to"/a modal, or immediately followed by a lower-case
    # object with no article).
    "overlay": [
        ("before", re.compile(r"\b(?:to|must|can|will|should|may)\s*$")),
        ("after", re.compile(r"^s?\s+(?:each|a\b|the\b(?!\s+\w+\s*[.,;:])|its\b)")),
    ],
}


def context_rejected(body: str, start: int, end: int, canonical: str) -> bool:
    """True if a CONTEXT_SKIP rule for ``canonical`` matches the text
    immediately before/after this specific occurrence."""
    for side, rx in CONTEXT_SKIP.get(canonical, ()):
        if side == "before":
            if rx.search(body[max(0, start - 20) : start]):
                return True
        else:
            if rx.match(body[end : end + 20]):
                return True
    return False

FRONT_LABEL_RE = re.compile(r"^\([a-z0-9-]+\)=\s*$", re.MULTILINE)
FIRST_DEF_RE = re.compile(r"^\[\^[A-Za-z0-9][A-Za-z0-9_-]*\]:", re.MULTILINE)
# A footnote *marker* (as opposed to its definition, already kept out of
# "body" entirely) is inline text like "[^wiki-stepper]" or "[^pdk-cvd]" --
# many labels are the cited term itself, so without this the term-matching
# regex would find "stepper" or "cvd" *inside the marker's own brackets* and
# mangle it into "[^wiki-{term}`stepper`]" (found in the ten-page
# spot-check, on docs/machines/duv-krf-stepper.md's "[^wiki-stepper]" --
# see the progress file). Masked whole, brackets included.
MARKER_RE = re.compile(r"\[\^[A-Za-z0-9][A-Za-z0-9_-]*\]")
HEADING_RE = re.compile(r"^#{1,6}[ \t].*$", re.MULTILINE)
TABLE_ROW_RE = re.compile(r"^[ \t]*\|.*$", re.MULTILINE)
OPTION_LINE_RE = re.compile(r"^:[A-Za-z][\w-]*:.*$", re.MULTILINE)
FENCE_OPEN_RE = re.compile(r"^(:{3,})\{([a-zA-Z][\w-]*)\}")
FENCE_CLOSE_RE = re.compile(r"^(:{3,})\s*$")
# Triple-backtick fences (` ```{toctree} `, ` ```{math} `, or a plain code
# fence): always masked whole, never just their option lines. A toctree's
# body is bare document paths ("cd-sem-overlay-metrology"), not prose, and
# CODE_SPAN_RE's inline single/double-backtick patterns do not reach past a
# fence's own backticks to protect it -- found when the first real run
# mangled a toctree entry into "cd-sem-{term}`overlay`-metrology" and broke
# the -W build (see the progress file). None of these fences nest with each
# other in this codebase, so a plain open/close toggle (not a counted
# stack) is enough.
BACKTICK_FENCE_LINE_RE = re.compile(r"^```")
REFERENCES_RE = re.compile(r"^## References[ \t]*\n", re.MULTILINE)
NEXT_H2_RE = re.compile(r"^## ", re.MULTILINE)
INDEX_LINKS_RE = re.compile(
    r"<!-- index-links:begin.*?<!-- index-links:end -->", re.DOTALL
)

# Prose in this codebase is hard-wrapped at a fixed column, so a quotation,
# a bold span or a link's own text can carry a single line break in the
# middle of it (a wrap, not a paragraph break). Each of the next four
# patterns therefore allows an interior "\n" as long as it is not itself a
# blank line (paragraph boundary) -- (?:[^X\n]|\n(?!\n)) -- rather than the
# simpler [^X\n]+, which would silently stop at the wrap and leave the rest
# of the quoted/bold/linked span exposed as if it were plain prose (found
# in the ten-page spot-check: an "aspect ratio" inside a wrapped quotation,
# and an "Ash" inside a wrapped bold run-in label, both slipped through the
# first version of this script's QUOTE_RE / BOLD_RE for exactly this
# reason -- see the progress file).
CODE_SPAN_RE = re.compile(r"``(?:[^`\n]|\n(?!\n))+``|`(?:[^`\n]|\n(?!\n))+`")
QUOTE_RE = re.compile(
    r'"(?:[^"\n]|\n(?!\n)){1,400}"|“(?:[^”\n]|\n(?!\n)){1,400}”'
)
LINK_RE = re.compile(r"\[(?:[^\]\n]|\n(?!\n))*\]\((?:[^)\n]|\n(?!\n))*\)")
# Bold spans are excluded too, though the rule does not name them: on this
# site **bold** overwhelmingly marks a tool/model *name* ("**Lam 9400
# TCP**") or a run-in label standing in for a heading ("**Ash** —
# ..."/R-H3), not descriptive prose -- both are exactly the "landed on a
# proper name" failure mode the branch's task calls out to fix by rule,
# found in the ten-page spot-check (see the progress file) on
# "**Lam 9400 TCP**" (a product name, not the generic TCP-chamber
# technology) and "**Ash** — ..." (a bullet's run-in label, not the noun
# "ash").
BOLD_RE = re.compile(r"\*\*(?:[^*\n]|\n(?!\n))+?\*\*")
MASKED_DIRECTIVES = {"dropdown", "figure"}


def split_body_and_defs(text: str) -> tuple[str, int]:
    """Return (body, body_length). Definitions are never scanned."""
    m = FIRST_DEF_RE.search(text)
    end = m.start() if m else len(text)
    return text[:end], end


def excluded_mask(body: str) -> list[bool]:
    """A per-character exclusion mask over ``body`` (True = never linkable)."""
    n = len(body)
    excluded = [False] * n

    def mark(a: int, b: int) -> None:
        for i in range(a, min(b, n)):
            excluded[i] = True

    # Line-oriented exclusions: headings, table rows, option lines.
    for rx in (HEADING_RE, TABLE_ROW_RE, OPTION_LINE_RE):
        for m in rx.finditer(body):
            mark(m.start(), m.end())

    # (label)= lines carry no prose but keep them out of harm's way too.
    for m in FRONT_LABEL_RE.finditer(body):
        mark(m.start(), m.end())

    # The generated index-links block, whole.
    for m in INDEX_LINKS_RE.finditer(body):
        mark(m.start(), m.end())

    # "## References" to the next H2 (or end of body): all three reading
    # tiers and the Deep dive list.
    ref_start = None
    for m in REFERENCES_RE.finditer(body):
        ref_start = m.start()
        nxt = NEXT_H2_RE.search(body, m.end())
        ref_end = nxt.start() if nxt else n
        mark(ref_start, ref_end)

    # {dropdown} / {figure} fences, tracked by a colon-count stack so a
    # differently-nested directive (this branch's own {grid}/{grid-item-card}
    # on the landing page) is not mistaken for one of them; and
    # ```{toctree}``` / ```{math}``` / plain code fences, tracked by a
    # simple open/close toggle (see BACKTICK_FENCE_LINE_RE above).
    stack: list[tuple[int, str, int]] = []  # (colon count, name, line start)
    backtick_fence_start: int | None = None
    pos = 0
    for line in body.split("\n"):
        line_start = pos
        line_end = pos + len(line)
        if backtick_fence_start is not None:
            if BACKTICK_FENCE_LINE_RE.match(line):
                mark(backtick_fence_start, line_end)
                backtick_fence_start = None
        elif BACKTICK_FENCE_LINE_RE.match(line):
            backtick_fence_start = line_start
        else:
            m = FENCE_OPEN_RE.match(line)
            if m:
                stack.append((len(m.group(1)), m.group(2), line_start))
            else:
                m2 = FENCE_CLOSE_RE.match(line)
                if m2 and stack and len(m2.group(1)) == stack[-1][0]:
                    count, name, start = stack.pop()
                    if name in MASKED_DIRECTIVES:
                        mark(start, line_end)
        pos = line_end + 1  # + the newline split() ate
    if backtick_fence_start is not None:
        # An unterminated fence (should not happen in well-formed input):
        # mask to the end of the body rather than leave it exposed.
        mark(backtick_fence_start, n)

    # Code spans, role/link display text (always backtick-delimited here),
    # quoted text, markdown link text+target, bold spans (tool/model names
    # and run-in labels -- see BOLD_RE above), and footnote markers.
    for rx in (CODE_SPAN_RE, QUOTE_RE, LINK_RE, BOLD_RE, MARKER_RE):
        for m in rx.finditer(body):
            mark(m.start(), m.end())

    return excluded


# ---------------------------------------------------------------------------
# Glossary terms.

def load_terms() -> list[str]:
    text = GLOSSARY.read_text()
    terms: list[str] = []
    for m in re.finditer(r"```\{glossary\}\n(.*?)\n```", text, re.S):
        for line in m.group(1).split("\n"):
            if line and not line[0].isspace():
                terms.append(line)
    return terms


def is_acronym(term: str) -> bool:
    return not any(c.islower() for c in term if c.isalpha())


def pluralize(word: str) -> str:
    if word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"
    if len(word) > 1 and word[-1] == "y" and word[-2] not in "aeiouAEIOU":
        return word[:-1] + "ies"
    return word + "s"


def sentence_initial(term: str) -> str | None:
    if term[0].isalpha() and term[0].islower():
        return term[0].upper() + term[1:]
    return None


def variants_for(term: str) -> list[tuple[str, str]]:
    """[(variant text, display form for the {term} role), ...] for one
    glossary term. The display form is the variant text itself (the
    ``{term}`` role's own casing is whatever was actually written on the
    page); the *canonical* target is added by the caller when it differs.
    """
    forms = [term]
    if is_acronym(term):
        forms.append(term + "s")
    else:
        alt = sentence_initial(term)
        if alt:
            forms.append(alt)
        forms.append(pluralize(term))
        if alt:
            forms.append(pluralize(alt))
    # dedupe, keep order
    seen: set[str] = set()
    out = []
    for f in forms:
        if f not in seen:
            seen.add(f)
            out.append(f)
    return [(f, term) for f in out]


LEFT_BOUND = r"(?<![A-Za-z0-9_])"
RIGHT_BOUND = r"(?![A-Za-z0-9_])"


def build_pattern(terms: list[str]) -> tuple[re.Pattern, dict[str, str]]:
    """One alternation over every variant of every non-skipped term, longest
    variant text first so a longer term (``CD-SEM``) is tried, and wins,
    before a shorter one that is a prefix of it (``CD``) at the same spot.
    """
    pairs: list[tuple[str, str]] = []
    for term in terms:
        if term in SKIP_TERMS:
            continue
        pairs.extend(variants_for(term))
    pairs.sort(key=lambda p: len(p[0]), reverse=True)
    variant_to_canonical = dict(pairs)
    alt = "|".join(re.escape(v) for v, _ in pairs)
    pattern = re.compile(f"{LEFT_BOUND}(?:{alt}){RIGHT_BOUND}")
    return pattern, variant_to_canonical


EXISTING_TERM_ROLE_RE = re.compile(r"\{term\}`([^`]+)`")


def preexisting_terms(text: str, known_terms: list[str]) -> set[str]:
    """Canonical terms already linked *anywhere* on the page (any existing
    ``{term}`...``` / ``{term}`...<target>``` use, in the body, a dropdown,
    a table, ``## References`` or a footnote definition -- it does not
    matter where: a term already linked once must not be linked again
    elsewhere). Without this, a page that already spells out
    `` {term}`stepper` `` once would still get a *second*,
    script-added `` {term}`stepper` `` at its next occurrence, because that
    first use sits inside a role's own backticks, which the exclusion mask
    (rightly) treats as "not a candidate site" rather than as "this term is
    already spoken for" (found in the ten-page spot-check, on
    docs/machines/duv-krf-stepper.md, which already linked "stepper" once
    by hand; see the progress file).
    """
    by_lower = {t.lower(): t for t in known_terms}
    found: set[str] = set()
    for m in EXISTING_TERM_ROLE_RE.finditer(text):
        content = m.group(1).strip()
        target_m = re.search(r"<([^<>]+)>\s*$", content)
        target = target_m.group(1).strip() if target_m else content
        canonical = by_lower.get(target.lower())
        if canonical:
            found.add(canonical)
    return found


PARAGRAPH_BREAK_RE = re.compile(r"\n[ \t]*\n")

# M4 (review): an explicit, idempotence-safe opt-out for one term on one
# page, e.g. ``<!-- link_terms: skip post-CMP clean -->`` anywhere in the
# page. Without this, a hand-reverted link (one the branch decided was a
# false positive check_preserved.py or a human reviewer rejected) would be
# silently re-added by the next site-wide run, since the script has no
# other way to tell "this term's first occurrence was deliberately left
# unlinked" apart from "the script itself never found a valid occurrence" --
# indistinguishable to a re-run. The comment form (not a side-table keyed
# by path, the review's own suggestion) keeps the decision next to the
# page it applies to and visible in the diff that added it.
PAGE_SKIP_RE = re.compile(r"<!--\s*link_terms:\s*skip\s+([^-]+?)\s*-->")


def page_skip_terms(text: str, known_terms: list[str]) -> set[str]:
    by_lower = {t.lower(): t for t in known_terms}
    found: set[str] = set()
    for m in PAGE_SKIP_RE.finditer(text):
        canonical = by_lower.get(m.group(1).strip().lower())
        if canonical:
            found.add(canonical)
    return found


def paragraph_starts(body: str) -> list[int]:
    """Start offsets of every paragraph in ``body`` (M2's unit), in order,
    always including 0.
    """
    starts = [0]
    starts.extend(m.end() for m in PARAGRAPH_BREAK_RE.finditer(body))
    return starts


def paragraph_of(starts: list[int], pos: int) -> int:
    lo, hi = 0, len(starts) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if starts[mid] <= pos:
            lo = mid
        else:
            hi = mid - 1
    return lo


def first_uses(
    body: str,
    pattern: re.Pattern,
    variant_to_canonical: dict[str, str],
    preseen: set[str] | None = None,
    page_skip: set[str] | None = None,
    max_per_paragraph: int = 3,
):
    """Yield (start, end, matched_text, canonical_term) for the first
    *accepted* occurrence of each term, left to right, skipping anything
    the exclusion mask covers, a term in ``preseen`` or ``page_skip``, a
    CONTEXT_SKIP-rejected occurrence, or a paragraph that has already
    reached ``max_per_paragraph`` new links this pass (M2) -- each of the
    last two only reject *this* occurrence, so the same term is tried
    again at its next occurrence on the page (which may sit in a less
    crowded paragraph, or a better context, and still count as that
    term's first *accepted* link).
    """
    excluded = excluded_mask(body)
    seen_terms: set[str] = set(preseen or ())
    skip_terms = page_skip or set()
    starts = paragraph_starts(body)
    para_count: dict[int, int] = {}
    for m in pattern.finditer(body):
        start, end = m.start(), m.end()
        if any(excluded[start:end]):
            continue
        matched = m.group(0)
        canonical = variant_to_canonical.get(matched)
        if canonical is None:
            # Should not happen: every alternative in the pattern is a key.
            continue
        if canonical in seen_terms or canonical in skip_terms:
            continue
        if context_rejected(body, start, end, canonical):
            continue
        para = paragraph_of(starts, start)
        if para_count.get(para, 0) >= max_per_paragraph:
            continue
        seen_terms.add(canonical)
        para_count[para] = para_count.get(para, 0) + 1
        yield start, end, matched, canonical


def apply_links(
    body: str,
    pattern: re.Pattern,
    variant_to_canonical: dict[str, str],
    preseen: set[str] | None = None,
    page_skip: set[str] | None = None,
):
    """Return (new_body, [(canonical_term, matched_text, start, end), ...])
    applied in left-to-right order; each accepted span becomes
    ``{term}`text`` when ``text`` is exactly the glossary's own spelling,
    else ``{term}`text <canonical>```.
    """
    spans = list(first_uses(body, pattern, variant_to_canonical, preseen, page_skip))
    if not spans:
        return body, []
    out = []
    cursor = 0
    pieces = []
    for start, end, matched, canonical in spans:
        pieces.append(body[cursor:start])
        if matched == canonical:
            pieces.append(f"{{term}}`{matched}`")
        else:
            pieces.append(f"{{term}}`{matched} <{canonical}>`")
        cursor = end
        out.append((canonical, matched, start, end))
    pieces.append(body[cursor:])
    return "".join(pieces), out


def context_window(body: str, start: int, end: int, width: int = 90) -> str:
    """A normalised-whitespace window of text around [start, end), for
    ``--report`` -- a fixed character window rather than an attempt at
    "the sentence", since this codebase's hard-wrapped source and the
    occasional mid-sentence marker make exact sentence boundaries fragile
    to recover; a window is robust and just as readable for sampling.
    """
    lo = max(0, start - width)
    hi = min(len(body), end + width)
    before = re.sub(r"\s+", " ", body[lo:start]).strip()
    matched = body[start:end]
    after = re.sub(r"\s+", " ", body[end:hi]).strip()
    return f"...{before} [{matched}] {after}..."


def process_file(path: Path, pattern, variant_to_canonical, terms, check: bool, report: bool = False):
    text = path.read_text()
    preseen = preexisting_terms(text, terms)
    skip = page_skip_terms(text, terms)
    body, split_at = split_body_and_defs(text)
    new_body, applied = apply_links(body, pattern, variant_to_canonical, preseen, skip)
    if not applied:
        return []
    if report:
        for canonical, matched, start, end in applied:
            print(f"{path}: {canonical!r} (as {matched!r}): {context_window(body, start, end)}")
    if not check and not report:
        path.write_text(new_body + text[split_at:])
    return applied


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    check = "--check" in argv
    report = "--report" in argv
    paths = [Path(a) for a in argv if not a.startswith("--")]
    if not paths:
        print(
            "usage: link_terms.py [--check | --report] <file.md> ...",
            file=sys.stderr,
        )
        return 2
    terms = load_terms()
    pattern, variant_to_canonical = build_pattern(terms)
    total = 0
    for p in paths:
        applied = process_file(p, pattern, variant_to_canonical, terms, check, report)
        if applied:
            total += len(applied)
            if not report:
                label = "would link" if check else "linked"
                print(f"{p}: {label} {len(applied)} term(s)")
                for canonical, matched, _start, _end in applied:
                    print(f"    {canonical!r} (as {matched!r})")
    if not report:
        action = "would add" if check else "added"
        print(f"{action} {total} term link(s) across {len(paths)} file(s)")
    return 0


# ---------------------------------------------------------------------------

def selftest() -> int:
    problems: list[str] = []

    def fail(msg: str) -> None:
        problems.append(msg)

    def linked_of(text: str, terms: list[str]) -> list[tuple[str, str]]:
        pattern, v2c = build_pattern(terms)
        preseen = preexisting_terms(text, terms)
        skip = page_skip_terms(text, terms)
        body, split_at = split_body_and_defs(text)
        _, applied = apply_links(body, pattern, v2c, preseen, skip)
        return [(canonical, matched) for canonical, matched, _s, _e in applied]

    # 1. A plain first occurrence is linked with the implicit form.
    out = linked_of("The gate stack uses CMP to planarise the surface.\n", ["CMP"])
    if out != [("CMP", "CMP")]:
        fail(f"simple acronym link: {out}")

    # 2. Second occurrence on the same page is not linked again.
    body, split_at = split_body_and_defs(
        "CMP planarises the film. Later, CMP happens again.\n"
    )
    pattern, v2c = build_pattern(["CMP"])
    new_body, applied = apply_links(body, pattern, v2c)
    if new_body.count("{term}") != 1:
        fail(f"first-occurrence-only failed: {new_body!r}")

    # 3. Acronym case sensitivity: lowercase "mol" must not match "MOL".
    out = linked_of("A mol of gas is not the same as the MOL module.\n", ["MOL"])
    if out != [("MOL", "MOL")]:
        fail(f"acronym case-sensitivity failed: {out}")

    # 4. "CAR" (acronym) must not match the English word "car" or "Car".
    out = linked_of("A car is not a chemically amplified resist.\n", ["CAR"])
    if out:
        fail(f"acronym false match on ordinary word: {out}")

    # 5. Sentence-initial capitalisation of a regular (non-acronym) term.
    out = linked_of("Spacer width sets the tip overlap.\n", ["spacer"])
    if out != [("spacer", "Spacer")]:
        fail(f"sentence-initial match failed: {out}")

    # 6. Plural, explicit form.
    body, split_at = split_body_and_defs("Two hard masks pattern the film.\n")
    pattern, v2c = build_pattern(["hard mask"])
    new_body, applied = apply_links(body, pattern, v2c)
    if "{term}`hard masks <hard mask>`" not in new_body:
        fail(f"plural explicit form failed: {new_body!r}")

    # 7. Never inside a heading.
    body, split_at = split_body_and_defs("## The CMP module\n\nCMP removes overburden.\n")
    pattern, v2c = build_pattern(["CMP"])
    new_body, applied = apply_links(body, pattern, v2c)
    if "{term}" not in new_body or "## The CMP module" not in new_body:
        fail(f"heading exclusion failed: {new_body!r}")
    if new_body.count("{term}") != 1:
        fail(f"heading CMP was linked too: {new_body!r}")

    # 8. Never inside a code span.
    out = linked_of("The file `CMP.md` describes CMP.\n", ["CMP"])
    if out != [("CMP", "CMP")]:
        fail(f"code-span exclusion failed: {out}")

    # 9. Never inside a quotation.
    out = linked_of('SkyWater states "the CMP step is proprietary" here.\n', ["CMP"])
    if out:
        fail(f"quotation exclusion failed: {out}")

    # 10. Never inside a table row.
    body, split_at = split_body_and_defs(
        "| Step | Note |\n|---|---|\n| 1 | CMP happens |\n\nCMP is discussed here.\n"
    )
    pattern, v2c = build_pattern(["CMP"])
    new_body, applied = apply_links(body, pattern, v2c)
    if "| CMP happens |" not in new_body:
        fail(f"table exclusion failed: {new_body!r}")
    if new_body.count("{term}") != 1:
        fail(f"table CMP was linked too: {new_body!r}")

    # 11. Never inside "## References".
    body, split_at = split_body_and_defs(
        "CMP planarises.\n\n## References\n\n### Deep dive\n\n* CMP paper.[^a]\n"
    )
    pattern, v2c = build_pattern(["CMP"])
    new_body, applied = apply_links(body, pattern, v2c)
    if new_body.count("{term}") != 1:
        fail(f"References exclusion failed: {new_body!r}")

    # 12. Never inside a footnote definition.
    text = "CMP planarises.\n\n<!-- footnotes -->\n\n[^a]: A note about CMP.\n"
    out = linked_of(text, ["CMP"])
    if out != [("CMP", "CMP")]:
        fail(f"footnote-definition exclusion failed: {out}")

    # 13. Never inside a {dropdown}.
    body, split_at = split_body_and_defs(
        "CMP is used here.\n\n:::{dropdown} Title\nCMP mentioned again inside.\n:::\n"
    )
    pattern, v2c = build_pattern(["CMP"])
    new_body, applied = apply_links(body, pattern, v2c)
    if new_body.count("{term}") != 1:
        fail(f"dropdown exclusion failed: {new_body!r}")

    # 14. Never inside a {figure} block (generated): the CMP mentioned in
    #     its alt text and caption must not be linked; the one after the
    #     block must be.
    body, split_at = split_body_and_defs(
        ":::{figure} /x.svg\n:alt: A CMP diagram\n\nCMP shown above.\n:::\n\nCMP happens.\n"
    )
    pattern, v2c = build_pattern(["CMP"])
    new_body, applied = apply_links(body, pattern, v2c)
    canon_matched = [(c, m) for c, m, _s, _e in applied]
    if canon_matched != [("CMP", "CMP")] or "{term}`CMP` happens" not in new_body:
        fail(f"figure exclusion failed: {new_body!r} / {applied}")

    # 15. A {grid}/{grid-item-card} block (this branch's landing page) is
    #     not masked like a dropdown/figure -- its body prose is still
    #     linkable, but its option lines (":link:", ":link-type:") are not
    #     prose and must never be touched even if they happened to contain
    #     term-shaped text.
    body, split_at = split_body_and_defs(
        "::::{grid} 1 2 3\n:::{grid-item-card} Overview\n:link: overview-index\n"
        ":link-type: ref\n\nCMP is mentioned here.\n:::\n::::\n"
    )
    pattern, v2c = build_pattern(["CMP"])
    new_body, applied = apply_links(body, pattern, v2c)
    if [(c, m) for c, m, _s, _e in applied] != [("CMP", "CMP")]:
        fail(f"grid-item-card body should still be linkable: {applied}")
    if ":link: overview-index" not in new_body or ":link-type: ref" not in new_body:
        fail(f"an option line was altered: {new_body!r}")

    # 16. Never inside the generated index-links block.
    body, split_at = split_body_and_defs(
        "CMP happens.\n\n<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->\n"
        "Related patents: CMP thing.\n<!-- index-links:end -->\n"
    )
    pattern, v2c = build_pattern(["CMP"])
    new_body, applied = apply_links(body, pattern, v2c)
    if new_body.count("{term}") != 1:
        fail(f"index-links exclusion failed: {new_body!r}")

    # 17. Skip-listed ambiguous terms are never linked.
    out = linked_of("A via connects two metal levels.\n", ["via"])
    if out:
        fail(f"skip-list term 'via' was linked: {out}")
    out = linked_of("The bench runs SC-1 and SC-2 in sequence.\n", ["SC-1", "SC-2"])
    if out:
        fail(f"skip-list terms 'SC-1'/'SC-2' were linked: {out}")

    # 17b. Every glossary term that contains a digit must be skip-listed:
    # check_preserved.py's ROLE_RE masks a whole matched role to one space
    # before counting numbers, so wrapping any such term always reports an
    # unfixable false "LOST numbers" (see the comment above SKIP_TERMS).
    # This guards against the glossary later gaining a new digit-bearing
    # term that nobody remembers to add to the list.
    digit_terms = [t for t in load_terms() if any(c.isdigit() for c in t)]
    missing = [t for t in digit_terms if t not in SKIP_TERMS]
    if missing:
        fail(f"digit-bearing glossary term(s) not in SKIP_TERMS: {missing}")

    # 18. Prefix collision: a longer term (CD-SEM) wins over a shorter one
    #     that is one of its prefixes (CD), and CD is still linkable on its
    #     own elsewhere on the same page.
    out = linked_of("A CD-SEM measures CD after etch.\n", ["CD", "CD-SEM"])
    if ("CD-SEM", "CD-SEM") not in out or ("CD", "CD") not in out:
        fail(f"prefix collision handling failed: {out}")

    # 19. Never inside existing link/role text (backtick-delimited).
    out = linked_of("See {ref}`the CMP step <step-116>` for detail.\n", ["CMP"])
    if out:
        fail(f"role-text exclusion failed: {out}")

    # 20. Never inside a markdown link's own bracketed text.
    out = linked_of("See [the CMP page](machines/cmp.md) for detail.\n", ["CMP"])
    if out:
        fail(f"markdown-link exclusion failed: {out}")

    # 21. Never inside bold text (tool/model names, run-in labels): the CMP
    #     inside "**Lam CMP tool**" is not linked; a later, unbolded CMP is.
    out = linked_of(
        "* **Lam CMP tool** does the polish. Later, CMP happens again.\n", ["CMP"]
    )
    if out != [("CMP", "CMP")]:
        fail(f"bold exclusion failed: {out}")

    # 22. A quotation that wraps onto a second line still masks its whole
    #     content (not just up to the wrap).
    out = linked_of(
        'Thung records that the "aspect ratio is increased by 66% from\n'
        '0.18 to 0.13".\n',
        ["aspect ratio"],
    )
    if out:
        fail(f"wrapped-quotation exclusion failed: {out}")

    # 23. A bold span that wraps onto a second line still masks its whole
    #     content.
    out = linked_of(
        "* **Ash tool — a long description that happens to wrap onto\n"
        "  a second line here.**[^a] Later, ash happens again.\n",
        ["ash"],
    )
    if out != [("ash", "ash")]:
        fail(f"wrapped-bold exclusion failed: {out}")

    # 24. Never inside a footnote *marker* whose label happens to contain
    #     the term's own text (e.g. "[^wiki-stepper]"): the marker must
    #     stay byte-identical, and the real prose "stepper" elsewhere on
    #     the line must still be linked.
    out = linked_of(
        "A KrF tool has the same chain as an i-line tool,[^wiki-stepper] and "
        "ASML built both on one stepper body.\n",
        ["stepper"],
    )
    if out != [("stepper", "stepper")]:
        fail(f"footnote-marker exclusion failed: {out}")
    body, split_at = split_body_and_defs(
        "A KrF tool has the same chain as an i-line tool,[^wiki-stepper] and "
        "ASML built both on one stepper body.\n"
    )
    pattern, v2c = build_pattern(["stepper"])
    new_body, applied = apply_links(body, pattern, v2c)
    if "[^wiki-stepper]" not in new_body:
        fail(f"a footnote marker was mangled: {new_body!r}")

    # 25. A term already linked once earlier on the page (inside another
    #     role's own backticks, so invisible to the exclusion mask as "a
    #     term", not just as "excluded text") must not be linked again at
    #     its next occurrence.
    terms = ["stepper"]
    text = (
        "A tool is either a whole-field {term}`stepper` or a scanner. "
        "ASML built both on one stepper body.\n"
    )
    preseen = preexisting_terms(text, terms)
    if preseen != {"stepper"}:
        fail(f"preexisting_terms did not find the existing link: {preseen}")
    pattern, v2c = build_pattern(terms)
    body, split_at = split_body_and_defs(text)
    new_body, applied = apply_links(body, pattern, v2c, preseen)
    if applied:
        fail(f"a term already linked once was linked again: {applied}")

    # 26. The explicit <target> form of an existing link is recognised too,
    # case-insensitively against the glossary's own casing.
    preseen = preexisting_terms("See {term}`CDs <CD>` here.\n", ["CD"])
    if preseen != {"CD"}:
        fail(f"preexisting_terms missed an explicit-target existing link: {preseen}")

    # 27. Never inside a ```{toctree}``` block: a bare document path like
    # "cd-sem-overlay-metrology" must not be mangled into
    # "cd-sem-{term}`overlay`-metrology" (this broke the -W build on
    # docs/machines/index.md; see the progress file). A page's own prose
    # after the fence is still linkable.
    out = linked_of(
        "## Machines\n\n"
        "```{toctree}\n:maxdepth: 1\n\ncd-sem-overlay-metrology\n```\n\n"
        "The overlay budget is discussed below.\n",
        ["overlay"],
    )
    if out != [("overlay", "overlay")]:
        fail(f"toctree exclusion failed: {out}")

    # 28. Never inside a ```{math}``` block.
    out = linked_of(
        "```{math}\noverlay = 1\n```\n\nThe overlay budget is discussed below.\n",
        ["overlay"],
    )
    if out != [("overlay", "overlay")]:
        fail(f"math-fence exclusion failed: {out}")

    # 29. M1: the six full-skip terms found wrong-sense in the review's
    # audit are never linked, no matter how plain the context.
    for term in ("passivation", "extension", "erosion", "notching", "reflow", "footing"):
        out = linked_of(f"The {term} step happens here in the process flow.\n", [term])
        if out:
            fail(f"M1 skip-list term {term!r} was linked anyway: {out}")

    # 30. M1 CONTEXT_SKIP: "ICP-MS" and a DUV product line are rejected in
    # context but the plain technology sense still links normally.
    out = linked_of("Trace metals are measured by ICP-MS on this tool.\n", ["ICP"])
    if out:
        fail(f"ICP-MS context guard failed: {out}")
    out = linked_of("The chamber uses an ICP source for the plasma.\n", ["ICP"])
    if out != [("ICP", "ICP")]:
        fail(f"plain ICP use was wrongly rejected: {out}")
    out = linked_of("The vendor sells a Brewer Science DUV-series coater.\n", ["DUV"])
    if out:
        fail(f"DUV-series context guard failed: {out}")
    out = linked_of("Patterning uses a DUV stepper at 248 nm.\n", ["DUV"])
    if out != [("DUV", "DUV")]:
        fail(f"plain DUV use was wrongly rejected: {out}")

    # 31. M1 CONTEXT_SKIP: TCP next to a vendor model number (either side)
    # is rejected; TCP on its own still links.
    out = linked_of("The fab lists a Lam 9400 TCP etcher on site.\n", ["TCP"])
    if out:
        fail(f"TCP-after-model-number context guard failed: {out}")
    out = linked_of("The fab lists a TCP 9600(SE) etcher on site.\n", ["TCP"])
    if out:
        fail(f"TCP-before-model-number context guard failed: {out}")
    out = linked_of("The chamber is a TCP-type high-density source.\n", ["TCP"])
    if out != [("TCP", "TCP")]:
        fail(f"plain TCP use was wrongly rejected: {out}")

    # 32. M1 CONTEXT_SKIP: "overlay" as a verb is rejected; the noun use
    # still links (and the term is still tried again at its next
    # occurrence rather than abandoned for the page).
    out = linked_of(
        "The two patterns must overlay each other precisely. The overlay "
        "budget is set by the design rules.\n",
        ["overlay"],
    )
    if out != [("overlay", "overlay")]:
        fail(f"overlay verb/noun context guard failed: {out}")

    # 33. M2: at most 3 new links per paragraph; a 4th term's first
    # occurrence in an over-full paragraph is deferred to its next
    # occurrence, in a later paragraph, and still counts as that term's
    # first accepted link.
    text = (
        "One CMP two CVD three PVD four ARC in one crowded paragraph.\n\n"
        "A second paragraph mentions ARC again here.\n"
    )
    body, _ = split_body_and_defs(text)
    pattern, v2c = build_pattern(["CMP", "CVD", "PVD", "ARC"])
    new_body, applied = apply_links(body, pattern, v2c)
    if len(applied) != 4:
        fail(f"expected all 4 terms eventually linked, got: {applied}")
    if "four {term}`ARC` in one crowded" in new_body:
        fail(f"the 4th link in an already-full paragraph was not capped: {new_body!r}")
    if "{term}`ARC` again" not in new_body:
        fail(f"the capped term was not linked at its next (2nd-paragraph) occurrence: {new_body!r}")

    # 34. M4: an explicit page-level skip marker keeps a term unlinked
    # even though nothing else would exclude it -- what lets a
    # hand-reverted link stay reverted across a later re-run instead of
    # silently coming back (the exact bug the review's M4 finding was
    # about).
    text = (
        "<!-- link_terms: skip CMP -->\n\n"
        "The polisher performs CMP on the wafer.\n"
    )
    out = linked_of(text, ["CMP"])
    if out:
        fail(f"page_skip marker did not suppress the term: {out}")
    # A second run over the tool's own (unchanged, since nothing was
    # linked) output is identical -- idempotent.
    pattern, v2c = build_pattern(["CMP"])
    body, split_at = split_body_and_defs(text)
    skip = page_skip_terms(text, ["CMP"])
    once, applied1 = apply_links(body, pattern, v2c, page_skip=skip)
    twice, applied2 = apply_links(once, pattern, v2c, page_skip=skip)
    if once != twice or applied1 or applied2:
        fail(f"page_skip is not idempotent: {once!r} -> {twice!r}")

    # 35. --report prints the term and a context window without writing
    # the file (process_file's own contract: report implies no write).
    import io
    import contextlib

    tmp_terms = ["CMP"]
    tmp_pattern, tmp_v2c = build_pattern(tmp_terms)
    scratch = ROOT / "tmp" / "link_terms_selftest_scratch.md"
    scratch.parent.mkdir(parents=True, exist_ok=True)
    original = "The tool performs CMP on the wafer surface.\n"
    scratch.write_text(original)
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            applied = process_file(scratch, tmp_pattern, tmp_v2c, tmp_terms, False, report=True)
        if not applied or "CMP" not in buf.getvalue() or "[CMP]" not in buf.getvalue():
            fail(f"--report produced no useful output: {buf.getvalue()!r}")
        if scratch.read_text() != original:
            fail("--report wrote to the file; it must be read-only")
    finally:
        scratch.unlink(missing_ok=True)

    if problems:
        for p in problems:
            print("FAIL:", p)
        return 1
    print("selftest OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
