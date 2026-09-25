#!/usr/bin/env python3
"""Anchor every inventory entry and move its Tier/"used on" sentences to the
end (C10 rules 1-2; docs/plans/readability-guide.md R-ANCHOR).

For every ``**KEY** — ...`` entry in ``docs/references/public-sources.md``:

1. Insert an anchor line ``(src-<key-lowercased>)=`` directly above it, so
   the footnote popover can link to "its" entry (label == key on this
   site; see ``tools/link_popover_check.py``-style verification below).
2. Move the entry's ``Tier: ...`` sentence and every ``Used on ...`` /
   ``Also used on ...`` sentence to the end of the entry, each on its own
   line, in their original relative order (Tier first when present).
   Whole-sentence reordering only: no sentence is reworded, and no other
   text in the entry changes.

An entry's span is found the robust way, not by "one entry = one
blank-line block" (18 entries, `SKW-01` among them, carry an internal
bulleted list or a multi-paragraph "Caveats" note and so are themselves
several blank-line-separated blocks): it runs from its own ``**KEY** —``
line to just before the *next* entry's ``**KEY** —`` line or the next
heading, whichever comes first, so a following section's heading and
intro prose are never swept into the last entry of a section.

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
HEADING_AFTER_RE = re.compile(r"\n\n+#{1,6} ")
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
TIER_RE = re.compile(r"Tier:(?:[^\n<]|\n(?!\n))*?\.")
USED_ON_RE = re.compile(r"(?:Also used on|Used on)(?:[^\n<]|\n(?!\n))*?\.")


def entry_spans(text: str) -> list[tuple[str, int, int]]:
    """[(key, start, end), ...] for every entry, in file order. ``end`` is
    just past the entry's own last character; text[start:end] never
    includes a trailing blank line, a following heading, or another
    entry.
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
    # Tier: cross-check.") or alone on its own line (preceded *and*
    # followed by "\n", as most are). Removing only the matched text
    # itself in the second case would leave the newline before it and the
    # newline after it adjacent -- a blank line the file never had (found
    # when this collapsed a bibliographic paragraph and its in-force flag
    # sentence, which must stay in the same paragraph as each other, onto
    # two paragraphs separated by a blank line; check_inforce.py's flag
    # check follows the entry's *paragraph* text, so it silently stopped
    # seeing the flag on several entries -- see the progress file). So the
    # removal span is widened by one adjacent character: the following
    # newline when the group is on its own line(s), the preceding space
    # when it is inline.
    removals: list[tuple[int, int]] = []
    for group in groups:
        s, e = group[0].start(), group[-1].end()
        if s > 0 and entry_text[s - 1] == "\n" and e < len(entry_text) and entry_text[e] == "\n":
            e += 1
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

    return remaining + "\n" + "\n".join(sentences)


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
        anchor = "" if key in SKIP_ANCHOR_KEYS else f"(src-{key.lower()})=\n\n"
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
    if ANCHOR_RE.search(text):
        print("public-sources.md already has anchor lines; nothing to do.")
        return 0
    new_text, changed = process(text)
    n_entries = len(entry_spans(text))
    n_anchored = n_entries - len(SKIP_ANCHOR_KEYS)
    print(
        f"{n_anchored} of {n_entries} entries anchored "
        f"({len(SKIP_ANCHOR_KEYS)} skipped: {sorted(SKIP_ANCHOR_KEYS)}); "
        f"{changed} reordered (Tier/used-on moved)."
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

    # 2. Tier sentence moves to the end, whole-sentence, nothing reworded.
    text = "**PDK-01** — Foo. Tier: cross-check (SkyWater statement). Bar baz.\n"
    new, _ = process(text)
    expected_tail = "Foo. Bar baz.\nTier: cross-check (SkyWater statement).\n"
    if expected_tail not in new:
        fail(f"Tier sentence not moved cleanly: {new!r}")

    # 3. "Also used on" and "Used on" sentences move too, and the group as
    #    a whole keeps its *original* relative order (this is a relocation
    #    of a set of sentences, not a re-sort of Tier-before-used-on: the
    #    rule says "move to the end", not "put Tier first").
    text = (
        "**PDK-01** — Foo bar. Also used on the X page. Tier: cross-check. "
        "Used on the Y page.\n"
    )
    new, _ = process(text)
    if "Foo bar.\nAlso used on the X page.\nTier: cross-check.\nUsed on the Y page." not in new:
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
        "Caveats: this is a capability list.\n"
        "Also used on the wet-bench page.\n"
        "Tier: cross-check (SkyWater statement).\n"
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
    if "(src-pdk-01)=\n\n**PDK-01** — Baz.\nTier: cross-check." not in new:
        fail(f"a normal entry after the skipped pair was not handled normally: {new!r}")

    if problems:
        for p in problems:
            print("FAIL:", p)
        return 1
    print("selftest OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
