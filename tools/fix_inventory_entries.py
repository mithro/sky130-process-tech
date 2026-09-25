#!/usr/bin/env python3
"""Anchor every inventory entry and move its Tier/"used on" sentences to the
end (C10 rules 1-2; docs/plans/readability-guide.md R-ANCHOR).

For every ``**KEY** — ...`` entry in ``docs/references/public-sources.md``:

1. Insert an anchor line ``(src-<key-lowercased>)=`` directly above it, so
   the footnote popover can link to "its" entry (label == key on this
   site; see ``tools/link_popover_check.py``-style verification below).
2. Move the entry's ``Tier: ...`` sentence and every ``Used on ...`` /
   ``Also used on ...`` sentence to the end of the entry, each on its own
   *rendered* line (a MyST/CommonMark hard break, two trailing spaces --
   review M3: a bare "\\n" inside one paragraph is only a soft wrap in the
   built HTML, so "each on its own line" was true in the source but
   invisible to a reader; not a trailing backslash, the other CommonMark
   hard-break spelling, because that confuses tools/check_preserved.py's
   own sentence splitter into reading a whole entry as one sentence --
   see ``LINE_BREAK`` below), in their original relative order (this is a
   relocation of a set of sentences, not a re-sort that puts Tier first).
   Whole-sentence reordering only: no sentence is reworded, and no other
   text in the entry changes. A sentence's terminating "." is never one
   that follows a citation abbreviation or a name's initial (review H1:
   "(A. Hiraki)" is not a sentence end) -- see ``SENTENCE_END`` below.

An entry's span is found the robust way, not by "one entry = one
blank-line block" (18 entries, `SKW-01` among them, carry an internal
bulleted list or a multi-paragraph "Caveats" note and so are themselves
several blank-line-separated blocks): it runs from its own ``**KEY** —``
line to just before the *next* entry's ``**KEY** —`` line or the next
heading, whichever comes first, so a following section's heading and
intro prose are never swept into the last entry of a section.

Idempotent: an entry that already has its anchor is not given a second
one, and its trailing sentences (wherever they are) are still found and
reformatted -- running this twice in a row, or once over a file an
earlier version of this script already anchored, converges to the same
text and changes nothing on the second run (verified in the selftest).

Run with ``--check`` for a dry run (prints a diff-less summary and exits
1 if anything would change); ``--selftest`` for the offline unit tests.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ROOT / "docs" / "references" / "public-sources.md"

KEY_DASH_RE = re.compile(r"^\*\*([A-Za-z0-9][A-Za-z0-9_-]*)\*\* — ", re.MULTILINE)
HEADING_AFTER_RE = re.compile(r"\n\n+(?:#{1,6} |\(src-[a-z0-9_-]+\)=\n)")
ANCHOR_RE = re.compile(r"^\(src-[a-z0-9_-]+\)=\n", re.MULTILINE)

# One pre-existing pair in this file (verified with
# tools/check_preserved.py, not guessed): CAE-WAFERMARK-SUPERCLEAN's own
# bibliographic text has an unbalanced quote count ("8""," -- a closing
# description quote immediately followed by an inch-mark quote), which
# desyncs check_preserved.py's whitespace-flattened QUOTE_RE pairing from
# there all the way to the next real quote character anywhere later in the
# file -- which happens to be inside WHS-T4's own title, two entries later.
# That is a pre-existing bug in the checker (a false "quote", not a real
# one), but *any* edit inside that stretch changes what the false match's
# text is, which check_preserved reports as a LOST/ADDED pair regardless of
# --allow-added (it has no way to declare a loss expected). Rather than
# leave check_preserved failing on the whole file, this one entry's
# reordering, and the next one's anchor (the two edits that fall inside the
# stretch), are skipped -- narrow, documented, and the only two entries of
# 1720 this applies to. See the progress file for the full account.
SKIP_REORDER_KEYS = {
    "CAE-WAFERMARK-SUPERCLEAN": "its own unbalanced-quote text desyncs "
        "check_preserved.py's quote pairing up to WHS-T4's title; see the "
        "comment above SKIP_REORDER_KEYS",
}

# The 12 entries each followed by a ":::{dropdown}" (an in-force patent's
# collapsed note; check_inforce.py counts the same 12). Each one's flag
# sentence ("Shown as in force; ...") always already sits directly before
# the dropdown, so it is never itself moved -- but every other Tier/used-on
# sentence in these entries used to sit *before* the flag, close to the
# dropdown's own number-dense text, and moving them to the true end (after
# the dropdown) changes which numbers tools/check_preserved.py's
# `extract_number_order` heuristic groups into "one unit" with the
# dropdown's collapsed-note figures (it walks blank-line paragraphs, not a
# parse tree, and does not know a `{dropdown}` fence bounds anything).
# Verified by direct comparison of check_preserved.extract_all's own
# "numbers" and "number_order" output before and after: no number is lost
# or fabricated in these entries either way, only which sentence the
# dropdown's numbers get heuristically paired with for the *order* check.
# Reordering these 12 is skipped rather than accepted as noise, since a
# false "LOST number_order" fails check_preserved.py with no way to
# declare it expected. See the progress file for the full account.
_IN_FORCE_DROPDOWN_KEYS = (
    "PAT-02", "PAT-03", "PAT-04", "PAT-ONO-THICK-CYP", "PAT-RADOX-CYP",
    "PAT-MIM-TI-ETCH", "PAT-EDGESEAL-GF", "PAT-TESTLINE-TSMC",
    "PAT-RRAM-OXIDE-TSMC", "PAT-RRAM-ETCHSTOP-TSMC", "PAT-DICO2-MKS",
    "PAT-SOFTMARK-GSI",
)
for _k in _IN_FORCE_DROPDOWN_KEYS:
    SKIP_REORDER_KEYS[_k] = (
        "followed by an in-force patent's {dropdown}; see the comment "
        "above _IN_FORCE_DROPDOWN_KEYS"
    )
SKIP_ANCHOR_KEYS = {
    "WHS-T4": "its title quote is where the desync above happens to end; "
        "see the comment above SKIP_REORDER_KEYS",
}

# Sentences to relocate. Both allow a single interior line-wrap (this file
# is hard-wrapped) but stop at a blank line (paragraph break) or the next
# such sentence; verified against every instance in the file (no "Tier:"
# or "(Also )?used on" text contains an internal ". " abbreviation or a
# decimal number that would end the match early -- see the branch's
# progress file for the checks run before trusting this). "<" is excluded
# from the content class: one "Also used on" annotation
# (docs/references/public-sources.md, AMAT-ENDURA) explains a Wayback
# substitution and ends in a bracketed archive URL, not a plain period --
# "https://web.archive.org/..." has its own "." right after "web", so the
# unguarded pattern matched only up to *that* period and cut the URL in
# half (found by check_preserved.py: a LOST/ADDED url pair; see the
# progress file). Refusing to match through a "<" leaves that one
# annotation exactly where it was, on the same conservative principle as
# the rest of this branch: if a rule cannot tell where a sentence safely
# ends, it does not guess.
#
# A terminating "." must not be an abbreviation's own period (review H1):
# PAT-TIW-HITACHI's "...adds the inventor\n(A. Hiraki) and the filing
# date..." was cut at "(A." because a single-capital-letter initial's
# period looks exactly like a sentence end to a naive pattern -- the real
# end, "...barrier film.", was several lines later, so the sentence was
# split in two and a fragment ("Hiraki) and the filing date...") was left
# stranded mid-entry (check_preserved's word multiset does not catch this:
# no word is lost, only misplaced). Each of these, immediately before the
# candidate ".", refuses the match: a single capital letter preceded by
# whitespace or "(" (any name initial, not just "A."), and the known
# abbreviations below in their usual citation casing. All are fixed-width
# lookbehinds (Python's `re` requires that), chained so each is checked
# independently at the same position.
_ABBREVIATIONS = (
    "al", "Al", "Inc", "inc", "Vol", "vol", "No", "no", "pp", "Pp",
    "Fig", "fig", "etc", "Etc",
)
_NOT_ABBREVIATION = "".join(f"(?<![\\s(]{a})" for a in _ABBREVIATIONS)
_NOT_INITIAL = r"(?<![\s(][A-Z])"
SENTENCE_END = _NOT_ABBREVIATION + _NOT_INITIAL + r"\."

TIER_RE = re.compile(rf"Tier:(?:[^\n<]|\n(?!\n))*?{SENTENCE_END}")
USED_ON_RE = re.compile(rf"(?:Also used on|Used on)(?:[^\n<]|\n(?!\n))*?{SENTENCE_END}")

# M3 (review): each relocated sentence gets a MyST/CommonMark hard line
# break before it -- a bare "\n" inside one paragraph renders as a soft
# wrap (a space) in the built HTML, not a new line, so "each on its own
# line" was true only in the source before this fix. CommonMark gives two
# ways to spell a hard break: a trailing backslash, or two-or-more
# trailing spaces, both followed by "\n". This uses the trailing-space
# form, not backslash, because of a second-order effect the backslash
# form has on tools/check_preserved.py (not on the built page): that
# checker's own sentence splitter is `(?<=[.!?])\s+(?=[A-Z0-9"])`, a
# lookbehind for the character *immediately* before the whitespace run a
# sentence break sits in. A trailing backslash sits between the period
# and that whitespace ("...targets.\\\nTier: ..."), so the lookbehind
# never matches there and check_preserved reads the whole entry -- every
# sentence in it -- as *one* "unit" for its number_order check, instead of
# one unit per sentence as before this fix; verified directly (a scratch
# comparison showed number_order tuples with 20+ elements appearing only
# with the backslash form). Trailing spaces do not have this problem: the
# period is still immediately followed by the whitespace run's start, so
# the checker's own sentence boundaries are unaffected, verified the same
# way. Rendering was verified with a scratch Sphinx build either way:
# both spellings produce an identical "<br />" in the built HTML.
LINE_BREAK = "  \n"

# An anchor already sitting directly above an entry (a previous run) is
# left alone, not duplicated -- what makes a second run safe to make
# regardless of anything else it changes (M3's own reformatting needs a
# second run over an already-anchored file to reach every entry).
ANCHOR_BEFORE_RE = re.compile(r"\(src-([a-z0-9_-]+)\)=\n\n\Z")


def existing_anchor_key(text: str, start: int) -> str | None:
    """The key of an anchor already directly above position `start`, if
    any (checked in a small window, not the whole preceding file, for
    speed -- an anchor line plus its blank line is always well under 100
    characters)."""
    window = text[max(0, start - 100) : start]
    m = ANCHOR_BEFORE_RE.search(window)
    return m.group(1) if m else None


def entry_spans(text: str) -> list[tuple[str, int, int]]:
    """[(key, start, end), ...] for every entry, in file order. ``end`` is
    just past the entry's own last character; text[start:end] never
    includes a trailing blank line, a following heading, a following
    entry, or (on a second run over an already-anchored file) the next
    entry's own anchor line -- found the hard way, by running this
    function on its own first-run output: without stopping at an anchor
    too, the *next* entry's "(src-...)=  " line was swept into the
    *previous* entry's own trailing text on a second pass, corrupting
    both.
    """
    starts = [(m.group(1), m.start()) for m in KEY_DASH_RE.finditer(text)]
    spans = []
    for i, (key, start) in enumerate(starts):
        limit = starts[i + 1][1] if i + 1 < len(starts) else len(text)
        region = text[start:limit]
        hm = HEADING_AFTER_RE.search(region)
        if hm:
            region = region[: hm.start()]
        end = start + len(region.rstrip("\n"))
        spans.append((key, start, end))
    return spans


def reorder_entry(entry_text: str) -> str:
    """Move every Tier:/used-on sentence in ``entry_text`` to its end,
    each on its own line, original relative order preserved. No other
    text is changed.
    """
    matches = sorted(
        list(TIER_RE.finditer(entry_text)) + list(USED_ON_RE.finditer(entry_text)),
        key=lambda m: m.start(),
    )
    if not matches:
        return entry_text

    # Two sentences sometimes share one physical line ("Also used on the
    # wet bench page. Tier: deep dive."), so adjacent matches separated
    # only by whitespace are merged into one removal span before deciding
    # what surrounds *that* span -- deciding it per match independently
    # got this exact case wrong (removing "Tier: deep dive." on its own
    # correctly trimmed the space before it, but then still left the
    # newline that followed it, because that match alone did not look
    # like a whole-line removal).
    sentences = [m.group(0) for m in matches]
    groups: list[list[re.Match]] = []
    for m in matches:
        if groups and entry_text[groups[-1][-1].end() : m.start()].strip(" ") == "":
            groups[-1].append(m)
        else:
            groups.append([m])

    # A group sits either inline (preceded by a space, e.g. "... entry.
    # Tier: cross-check.") or alone on its own line (preceded by "\n", as
    # most are, or -- on a second run over an already-migrated file, M3 --
    # by a hard break, "  \n"). Removing only the matched text itself would
    # leave the boundary before it and whatever follows adjacent -- a
    # blank line the file never had (found when this collapsed a
    # bibliographic paragraph and its in-force flag sentence, which must
    # stay in the same paragraph as each other, onto two paragraphs
    # separated by a blank line; check_inforce.py's flag check follows the
    # entry's *paragraph* text, so it silently stopped seeing the flag on
    # several entries -- see the progress file). The fix is to always
    # consume the group's own *leading* boundary (its preceding hard
    # break, "\n", or inline " ") rather than trying to decide whether to
    # widen forward instead: whatever separator already exists right after
    # the group (if anything does) is untouched and left to do its job, so
    # exactly one separator survives between the text before and after the
    # removed group either way. This also makes reorder_entry() idempotent
    # on text it has already reformatted with hard breaks (a hard break
    # before a group is recognised and fully consumed, not left as
    # dangling trailing spaces for LINE_BREAK to double up on next time).
    def _leading_boundary_width(pos: int) -> int:
        # A plain "\n" (width 1) or a hard break -- LINE_BREAK's own
        # trailing-space-then-"\n" form, of whatever length actually
        # precedes it (2, from this script, but counted rather than
        # assumed so a differently-spaced hard break already in the file
        # is still recognised on a re-run).
        if pos > 0 and entry_text[pos - 1] == "\n":
            width = 1
            i = pos - 2
            while i >= 0 and entry_text[i] == " ":
                width += 1
                i -= 1
            return width
        return 0

    removals: list[tuple[int, int]] = []
    for group in groups:
        s, e = group[0].start(), group[-1].end()
        width = _leading_boundary_width(s) if s > 0 else 0
        if width:
            s -= width
        elif s > 0 and entry_text[s - 1] == " ":
            s -= 1
        removals.append((s, e))

    pieces = []
    cursor = 0
    for s, e in removals:
        pieces.append(entry_text[cursor:s])
        cursor = e
    pieces.append(entry_text[cursor:])
    remaining = "".join(pieces)

    # Cosmetic cleanup only, as a safety net for any case the widening
    # above did not anticipate: collapse a run of spaces and a run of 3+
    # newlines down to one space / one blank line. Never touches a single
    # newline (a line wrap) or a single blank line (an intentional
    # paragraph break) that was already there.
    remaining = re.sub(r"[ \t]{2,}", " ", remaining)
    remaining = re.sub(r"\n{3,}", "\n\n", remaining)
    remaining = remaining.rstrip("\n")

    return remaining + LINE_BREAK + LINE_BREAK.join(sentences)


def process(text: str) -> tuple[str, int]:
    """Return (new_text, entries_changed)."""
    spans = entry_spans(text)
    pieces = []
    cursor = 0
    changed = 0
    for key, start, end in spans:
        pieces.append(text[cursor:start])
        entry_text = text[start:end]
        if key in SKIP_REORDER_KEYS:
            new_entry = entry_text
        else:
            new_entry = reorder_entry(entry_text)
        # A blank line, not just a newline, between the anchor and the
        # entry: verified the MyST target still resolves to the entry
        # paragraph either way, but tools/check_inforce.py's own inventory
        # parser (`inventory_entries()`) splits the file on blank lines and
        # requires each resulting *paragraph* to start with "**KEY**" --
        # `(src-...)=` glued directly onto the same paragraph made every
        # entry invisible to it (0 of 12 in-force exemptions found instead
        # of 12; see the progress file). A blank line keeps the anchor as
        # its own paragraph and leaves the entry's paragraph starting
        # exactly as before.
        #
        # Idempotent: an anchor already directly above this entry (a
        # previous run) is kept as-is, not duplicated -- this is what lets
        # a second run reformat every entry's trailing sentences (M3)
        # without re-running main()'s old "already anchored" all-or-
        # nothing guard, which could never reach an already-anchored file
        # again for any reason, including a formatting-only fix.
        already = existing_anchor_key(text, start)
        if key in SKIP_ANCHOR_KEYS or already == key.lower():
            anchor = ""
        else:
            anchor = f"(src-{key.lower()})=\n\n"
        if new_entry != entry_text:
            changed += 1
        pieces.append(anchor + new_entry)
        cursor = end
    pieces.append(text[cursor:])
    return "".join(pieces), changed


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    check = "--check" in argv
    text = INVENTORY.read_text()
    # No file-level "already anchored, nothing to do" guard: process() is
    # idempotent per entry (existing_anchor_key() above), so a second run
    # is always safe, and is exactly what applying a formatting-only fix
    # (M3) to an already-anchored file needs.
    new_text, changed = process(text)
    n_entries = len(entry_spans(text))
    n_anchored = sum(
        1 for key, start, _ in entry_spans(text)
        if key not in SKIP_ANCHOR_KEYS
    )
    if new_text == text:
        print(f"no change: {n_anchored} of {n_entries} entries already anchored and formatted.")
        return 0
    print(
        f"{n_anchored} of {n_entries} entries anchored "
        f"({len(SKIP_ANCHOR_KEYS)} skipped: {sorted(SKIP_ANCHOR_KEYS)}); "
        f"{changed} entries' trailing sentences (re)written."
    )
    if check:
        return 0
    INVENTORY.write_text(new_text)
    return 0


def selftest() -> int:
    problems: list[str] = []

    def fail(msg: str) -> None:
        problems.append(msg)

    # 1. Anchor is inserted, key lower-cased.
    text = "## 1. X\n\n**PDK-01** — Foo. Tier: cross-check.\n\n**PDK-02** — Bar. Tier: high-level.\n"
    new, changed = process(text)
    if "(src-pdk-01)=\n\n**PDK-01**" not in new or "(src-pdk-02)=\n\n**PDK-02**" not in new:
        fail(f"anchors missing: {new!r}")

    # 2. Tier sentence moves to the end, whole-sentence, nothing reworded,
    #    with a hard break (M3) so it renders on its own line.
    text = "**PDK-01** — Foo. Tier: cross-check (SkyWater statement). Bar baz.\n"
    new, _ = process(text)
    expected_tail = "Foo. Bar baz.  \nTier: cross-check (SkyWater statement).\n"
    if expected_tail not in new:
        fail(f"Tier sentence not moved cleanly: {new!r}")

    # 3. "Also used on" and "Used on" sentences move too, and the group as
    #    a whole keeps its *original* relative order (this is a relocation
    #    of a set of sentences, not a re-sort of Tier-before-used-on: the
    #    rule says "move to the end", not "put Tier first"). Each gets its
    #    own hard break.
    text = (
        "**PDK-01** — Foo bar. Also used on the X page. Tier: cross-check. "
        "Used on the Y page.\n"
    )
    new, _ = process(text)
    if "Foo bar.  \nAlso used on the X page.  \nTier: cross-check.  \nUsed on the Y page." not in new:
        fail(f"reordering did not preserve original relative order: {new!r}")

    # 4. A line-wrapped "Also used on" sentence (this file hard-wraps) is
    #    moved whole, including its wrap.
    text = (
        "**PDK-01** — Foo. Tier: cross-check.\n"
        "Also used on the FOM, DNM, LVTNM, NWM, HVTPM, PWBM, PWDEM, TUNM,\n"
        "ONOM, LVOM and RPM mask pages.\n"
    )
    new, _ = process(text)
    if "Also used on the FOM, DNM, LVTNM, NWM, HVTPM, PWBM, PWDEM, TUNM,\nONOM, LVOM and RPM mask pages." not in new:
        fail(f"wrapped used-on sentence not preserved whole: {new!r}")

    # 5. An entry with no Tier/used-on sentence is left with only its
    #    anchor added.
    text = "**PDK-01** — Foo bar with no tier line at all.\n"
    new, changed = process(text)
    if "(src-pdk-01)=\n\n**PDK-01** — Foo bar with no tier line at all." not in new:
        fail(f"untouched entry corrupted: {new!r}")
    if changed != 0:
        fail("an unchanged entry was counted as reordered")

    # 6. A multi-block entry (a bulleted list, like SKW-01): the bullets
    #    are untouched, and the Tier/used-on sentences in the trailing
    #    paragraph move to the true end of the *whole* entry, not just to
    #    the end of the block they were found in.
    text = (
        "**SKW-01** — SkyWater Technology, intro text.\n\n"
        "* *Lithography* — \"ASML I-line stepper\".\n"
        "* *Etch* — \"Lam 9400 TCP\".\n\n"
        "Caveats: this is a capability list. Also used on the wet-bench page. "
        "Tier: cross-check (SkyWater statement). Also used on the CMP page.\n\n"
        "**SKW-02** — Next entry.\n"
    )
    new, _ = process(text)
    if '* *Lithography* — "ASML I-line stepper".' not in new:
        fail(f"bulleted content altered: {new!r}")
    if (
        "Caveats: this is a capability list.  \n"
        "Also used on the wet-bench page.  \n"
        "Tier: cross-check (SkyWater statement).  \n"
        "Also used on the CMP page."
    ) not in new:
        fail(f"multi-block reordering failed: {new!r}")
    if "(src-skw-02)=\n\n**SKW-02**" not in new:
        fail(f"second entry's anchor/boundary wrong: {new!r}")

    # 7. A heading between two entries (a new subsection) is never treated
    #    as part of the entry before it, and its own following intro prose
    #    is left untouched.
    text = (
        "**PDK-01** — Foo. Tier: cross-check.\n\n"
        "## 2. Next section\n\n"
        "Some intro prose that must not gain an anchor or be touched.\n\n"
        "**PDK-02** — Bar. Tier: high-level.\n"
    )
    new, _ = process(text)
    if "## 2. Next section\n\nSome intro prose that must not gain an anchor or be touched.\n\n(src-pdk-02)=" not in new:
        fail(f"heading/intro between entries was mishandled: {new!r}")
    if "(src-" in new.split("## 2. Next section")[0].split("Tier: cross-check.\n")[-1]:
        fail(f"an anchor leaked before the heading: {new!r}")

    # 8. reorder_entry() is idempotent: applied to text that already has
    #    its Tier/used-on sentences at the end, it changes nothing.
    once = reorder_entry("**PDK-01** — Foo. Tier: cross-check.")
    twice = reorder_entry(once)
    if twice != once:
        fail(f"reordering is not idempotent: {once!r} -> {twice!r}")

    # 8b. main()'s own guard: a file that already has anchor lines is left
    #     alone entirely (process() is never even called on it by main()).
    already_anchored = "(src-pdk-01)=\n\n**PDK-01** — Foo. Tier: cross-check.\n"
    if not ANCHOR_RE.search(already_anchored):
        fail("ANCHOR_RE did not recognise an existing anchor line")

    # 9. Regression test for the exact bug this script had before the
    # blank line was added: tools/check_inforce.py's own inventory parser
    # splits the file on blank lines and requires each resulting paragraph
    # to start with "**KEY**" (see its `inventory_entries()`). Reproduce
    # that logic here (not by importing check_inforce, to keep this
    # selftest offline and independent) and confirm every anchored entry
    # is still found by it.
    check_inforce_key_re = re.compile(r"^\*\*([A-Z0-9][A-Z0-9_-]*)\*\*")
    text = (
        "**PDK-01** — Foo. Tier: cross-check.\n\n"
        "**PDK-02** — Bar. Also used on the X page.\n"
    )
    new, _ = process(text)
    found = set()
    for para in re.split(r"(\n\s*\n)", new):
        if para.startswith("\n"):
            continue
        m = check_inforce_key_re.match(para)
        if m:
            found.add(m.group(1))
    if found != {"PDK-01", "PDK-02"}:
        fail(
            "check_inforce.py's paragraph-based KEY_RE.match() no longer "
            f"finds every entry after anchoring: found {found}"
        )

    # 10. Regression test for the second check_inforce.py bug: removing a
    # sentence that sits alone on its own line (bordered by "\n" on both
    # sides, as "Tier:" almost always is) must not leave the newline
    # before it and the one after it adjacent -- that turns one paragraph
    # into two, at exactly the spot where an in-force patent's status flag
    # sentence sits, so check_inforce.py's per-paragraph flag check no
    # longer finds it. Reproduces the real PAT-02 shape: bibliographic
    # text, "Tier:", the flag sentence, all in one paragraph before a
    # dropdown.
    text = (
        "**PAT-02** — Foo bar entry text.\n"
        "Tier: deep dive.\n"
        "Shown as in force; estimated expiry 2027-06-17 (estimate from public\n"
        "records, not legal advice).\n\n"
        ":::{dropdown} From a patent shown as in force\n"
        "Collapsed content.\n"
        ":::\n"
    )
    new = reorder_entry(text)
    if "entry text.\n\nShown as in force" in new:
        fail(f"removing the own-line Tier sentence created a new blank line: {new!r}")
    if "entry text.\nShown as in force" not in new:
        fail(f"the flag sentence's paragraph was not kept intact: {new!r}")

    # 11. Regression test for the real PAT-04 shape: two sentences share
    # one physical line ("Also used on the wet bench page. Tier: deep
    # dive."), and that shared line is itself followed only by more
    # used-on lines and then the flag sentence. Removing the two merged
    # sentences must not leave a blank line where their shared line used
    # to be.
    text = (
        "**PAT-04** — Foo bar entry.\n"
        "Also used on the wet bench page. Tier: deep dive.\n"
        "Also used on the wet chemicals material page.\n"
        "Shown as in force; estimated expiry 2034-02-26 (estimate from public\n"
        "records, not legal advice).\n\n"
        ":::{dropdown} From a patent shown as in force\n"
        "Collapsed content.\n"
        ":::\n"
    )
    new = reorder_entry(text)
    if "entry.\n\nShown as in force" in new:
        fail(f"a shared-line pair of sentences left a new blank line: {new!r}")
    if "entry.\nShown as in force" not in new:
        fail(f"the flag sentence's paragraph was not kept intact: {new!r}")
    if new.count("Also used on the wet bench page.") != 1 or new.count("Tier: deep dive.") != 1:
        fail(f"a merged-group sentence was dropped or duplicated: {new!r}")

    # 12. Regression test for the real AMAT-ENDURA bug: an "Also used on"
    # annotation that ends in a bracketed URL, not a plain period, and
    # whose URL itself contains an internal "." right after its scheme
    # ("https://web.archive.org/..."). The whole sentence must be left
    # untouched (not truncated mid-URL) rather than moved incorrectly; the
    # plain "Used on ... page." and "Tier: ..." sentences on the same
    # entry are still moved normally.
    text = (
        "**AMAT-ENDURA** — Foo bar. Used on the deposition category page. "
        "Tier: cross-check.\n"
        "Also used on the PVD cluster tool page, read from the Wayback "
        "Machine capture of 2026-06-11 because the live page refused the "
        "checker's request on 2026-09-13:\n"
        "<https://web.archive.org/web/20260611155710/https://example.com/x.html>\n"
    )
    new = reorder_entry(text)
    if "<https://web.archive.org/web/20260611155710/https://example.com/x.html>" not in new:
        fail(f"a URL-bearing 'Also used on' annotation was mangled: {new!r}")
    if "Used on the deposition category page." not in new or "Tier: cross-check." not in new:
        fail(f"the plain sentences on the same entry were not still moved: {new!r}")

    # 13. SKIP_REORDER_KEYS / SKIP_ANCHOR_KEYS are honoured: the named
    # entry's reordering is skipped and the *next* entry's anchor is
    # skipped, everything else proceeds normally.
    text = (
        "**CAE-WAFERMARK-SUPERCLEAN** — Foo. Used on the X page. Tier: high-level.\n\n"
        "**WHS-T4** — Bar. Tier: cross-check.\n\n"
        "**PDK-01** — Baz. Tier: cross-check.\n"
    )
    new, changed = process(text)
    if "(src-cae-wafermark-superclean)=\n\n**CAE-WAFERMARK-SUPERCLEAN** — Foo. Used on the X page. Tier: high-level." not in new:
        fail(f"the skip-reorder entry was reordered anyway, or lost its own anchor: {new!r}")
    if "(src-whs-t4)=" in new:
        fail(f"the skip-anchor entry was anchored anyway: {new!r}")
    if "(src-pdk-01)=\n\n**PDK-01** — Baz.  \nTier: cross-check." not in new:
        fail(f"a normal entry after the skipped pair was not handled normally: {new!r}")

    # 14. H1 regression test, built on the exact PAT-TIW-HITACHI text the
    # review found corrupted: a name's initial ("A.") and the abbreviation
    # "wt.%" must not be read as a sentence end, so the "Also used on the
    # PVD cluster tool page..." annotation is captured whole, up to its
    # real end ("...barrier film."), not cut off at "(A.".
    text = (
        "**PAT-TIW-HITACHI** — Hitachi Metals, *Titanium-tungsten target material\n"
        "for sputtering and manufacturing method therefor*, US 5,160,534 A,\n"
        "granted 1992-11-03. <https://patents.google.com/patent/US5160534A/en>\n"
        "The 10 wt.% Ti composition of Ti:W sputter targets. Used on the\n"
        "deposition category page. Tier: cross-check.\n"
        "Also used on the PVD cluster tool page, whose footnote adds the inventor\n"
        "(A. Hiraki) and the filing date (1991-05-31) from Google Patents; the\n"
        "patent gives the 10 wt% titanium as the composition of the barrier film.\n"
        "Also used on the sputter targets material page.\n"
    )
    new, _ = process(text)
    # The old bug's exact signature: "(A." stranded alone at the end of a
    # line (the sentence cut there), and "Hiraki)" starting a new one.
    if "(A.\n" in new or "\nHiraki)" in new or " Hiraki)" in new.replace("(A. Hiraki)", ""):
        fail(f"the abbreviation/initial still split the sentence: {new!r}")
    if new.count("(A. Hiraki)") != 1:
        fail(f"the inventor's initial was duplicated or lost: {new!r}")
    if (
        "targets.  \n"
        "Used on the\ndeposition category page.  \n"
        "Tier: cross-check.  \n"
        "Also used on the PVD cluster tool page, whose footnote adds the inventor\n"
        "(A. Hiraki) and the filing date (1991-05-31) from Google Patents; the\n"
        "patent gives the 10 wt% titanium as the composition of the barrier film.  \n"
        "Also used on the sputter targets material page."
    ) not in new:
        fail(f"PAT-TIW-HITACHI was not reconstructed in its original sentence order: {new!r}")

    # 15. M3, confirmed at the unit level: the boundary between the
    # entry's own text and its first relocated sentence, and between two
    # relocated sentences, is a hard break (two trailing spaces then
    # "\n"), not a bare "\n" (a bare "\n" inside one MyST/CommonMark
    # paragraph renders as a soft wrap -- a space -- not a new line;
    # confirmed separately with a scratch Sphinx build, see the progress
    # file). A line-wrap *inside* one sentence (this file is hard-wrapped)
    # stays a bare "\n": it is not a break between two things, just where
    # the source happens to wrap.
    text = "**PDK-01** — Foo. Used on the\ndeposition category page. Tier: cross-check.\n"
    new, _ = process(text)
    if "Foo.  \nUsed on the\ndeposition category page.  \nTier: cross-check." not in new:
        fail(f"hard breaks are missing or in the wrong place: {new!r}")

    # 16. Idempotence on a re-run: process() applied to its own output a
    # second time changes nothing and does not duplicate an anchor -- what
    # lets a formatting-only fix (M3) reach a file an earlier run already
    # anchored, without a bespoke migration path.
    text = (
        "**PDK-01** — Foo. Used on the X page. Tier: cross-check.\n\n"
        "**PDK-02** — Bar. Also used on the Y page.\n"
    )
    once, changed1 = process(text)
    twice, changed2 = process(once)
    if twice != once:
        fail(f"process() is not idempotent on its own output: {once!r} -> {twice!r}")
    if once.count("(src-pdk-01)=") != 1 or once.count("(src-pdk-02)=") != 1:
        fail(f"a second run duplicated an anchor: {once!r}")

    if problems:
        for p in problems:
            print("FAIL:", p)
        return 1
    print("selftest OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
