#!/usr/bin/env python3
"""Link reading-list bullet heads to their footnote's own URL (W0c).

docs/plans/readability/report-C.md finding C1; docs/plans/readability-guide.md
R-LINKS rule 1 (steps 1-4); docs/plans/citation-style.md rule 5.

Inside ``## References`` only, per bullet under a ``* `` list item. The
*head* is the text before the bullet's annotation; two shapes exist, and
every rule below applies to either:

* **with a dash** — the head is the text before the first `` — ``, the
  tail is the dash, the annotation and the trailing marker(s);
* **without a dash** (review finding H1) — the head is the text before
  the trailing run of markers, the tail is just that marker run.

1. One marker ``[^k]``, and the head has no ``{role}``, ``[`` or
   backtick: wrap the whole head as ``[head](<URL>)``, URL = the first
   ``<URL>`` in the page's own ``[^k]:`` definition (character for
   character; when that definition's first URL is a Wayback capture,
   that is the URL used — the archive-first form is already page
   policy, R-WAYBACK). **Rule 1b**, the no-dash case: the head must also
   end in ``.``; that full stop stays outside the link, immediately
   before the marker.
2. Head has a role or backtick but exactly one ``*italic title*``: link
   only that span. (No no-dash equivalent: not asked for, and no such
   bullet was found on this site.)
3. N markers and exactly N italic titles, in the head, in the same
   order: link title *i* to marker *i*'s URL. **Rule 3b** is the same
   rule for a no-dash head.
4. **Rule 3c** (review finding M2, multi-marker bullets only): when
   rule 3/3b's exact N-for-N match fails, look at each ``*italic
   title*`` in the head in turn and search the *bullet's own markers'
   definitions* (any italic span in each definition's body, whitespace-
   normalised) for that same title. Link a title to its marker only
   when exactly one marker's definition names it, and only when no two
   titles resolve to the same marker (a title with zero or several
   candidate markers, and a marker two titles would both claim, are
   left as they are). This can convert *part* of a bullet — some
   titles linked, others left as plain text next to markers that stay
   plain footnotes — which the other rules never do.
5. Anything else (no marker, marker undefined, ambiguous italics,
   already linked, or a shape rules 1/1b/2/3/3b/3c do not cover): leave
   the bullet untouched.

The marker always stays, unchanged, at the end of the bullet. Nothing
else in the bullet, the annotation after the dash, the number of
bullets, footnote definitions or the generated ``index-links`` block is
touched. A bullet inside a ``{dropdown}`` (an in-force patent note) is
left untouched by this script -- report-C.md and R-LINKS allow
converting it in place, but only "if `tools/check_inforce.py` still
passes" and "if in doubt, leave it": `check_preserved.py` treats any
change to a dropdown's body as a content edit needing a deliberate
`--allow-dropdown-edits`, so converting these by script would need a
per-page review this tool cannot do. Left as a documented hand-finish
candidate (reason ``in-dropdown``).

Idempotent: a bullet whose head already contains a markdown link
(``](<...`` before the dash) is left alone, so running this script
twice makes no further change.

Usage::

    uv run tools/fix_reading_list_links.py [--check] [path ...]
    uv run tools/fix_reading_list_links.py --refresh [--check] [path ...]
    uv run tools/fix_reading_list_links.py --selftest

With no paths, every ``docs/**/*.md`` file outside ``docs/plans`` is
processed. ``--check`` reports what would change (file, counts) without
writing, and exits non-zero if anything would change. Without
``--check``, matching files are rewritten in place and a summary is
printed.

``--refresh`` (review finding H2) is a separate mode: it never links a
new bullet, only re-points a bullet's *already-existing* single link to
its own marker's *current* first URL, for the case a definition's first
URL moves after the link was made (R-WAYBACK: converting a definition to
archive-first form). Only a bullet with exactly one marker and exactly
one existing ``](<URL>)`` link is touched -- a multi-link bullet (rule
3/3b/3c) needs a human to say which link belongs to which marker, so
``--refresh`` leaves it alone. Combine with ``--check`` for a dry run.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_inforce  # noqa: E402  (for its {dropdown} fence parser)

DEF_RE = re.compile(
    r"^\[\^([A-Za-z0-9_-]+)\]:(.*?)(?=^\[\^[A-Za-z0-9_-]+\]:|\Z)", re.M | re.S
)
MARK_RE = re.compile(r"\[\^([A-Za-z0-9_-]+)\]")
URL_RE = re.compile(r"<(https?://[^<>\s]+)>")
REFS_SECTION_RE = re.compile(r"^## References\n(.*?)(?=^## |\Z)", re.S | re.M)
# A single-asterisk italic span: never a run of "**bold**" (an opening or
# closing "*" adjacent to another "*"), and never whitespace directly
# inside the delimiters (CommonMark forbids it, and it is what would
# otherwise let a list bullet's own leading "* " be mistaken for an
# opening delimiter).
ITALIC_RE = re.compile(r"(?<!\*)\*(?![\s*])[^*]+?(?<![\s*])\*(?!\*)")
HEAD_TAIL_RE = re.compile(r"\A(\* .*?)(\s+—\s)", re.S)
# The no-dash shape (H1): everything up to the trailing run of markers is
# the head, the marker run (and any trailing whitespace) is the tail. Only
# tried when HEAD_TAIL_RE has already failed, i.e. there is no " -- "
# anywhere in the bullet.
NODASH_RE = re.compile(r"\A(\* .*?)((?:\[\^[A-Za-z0-9_-]+\])+)(\s*)\Z", re.S)
GENBLOCK_RE = re.compile(
    r"<!-- index-links:begin \(generated by tools/gen_index_links\.py; "
    r"do not edit\) -->.*?<!-- index-links:end -->",
    re.S,
)

REASONS = (
    "ok-rule1",
    "ok-rule1b",
    "ok-rule2",
    "ok-rule3",
    "ok-rule3b",
    "ok-rule3c",
    "ok-refresh",
    "already-linked",
    "in-dropdown",
    "no-dash",
    "no-marker",
    "no-url",
    "role-in-head",
    "multi-marker",
)


def page_urls(text: str) -> dict[str, str]:
    """``{label: first <URL> in that label's own [^label]: definition}``."""
    urls: dict[str, str] = {}
    for lab, body in DEF_RE.findall(text):
        found = URL_RE.findall(body)
        if found:
            urls[lab] = found[0]
    return urls


def page_def_bodies(text: str) -> dict[str, str]:
    """``{label: that label's own [^label]: definition body text}``."""
    return dict(DEF_RE.findall(text))


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _italic_inner_set(text: str) -> set[str]:
    """Every ``*italic*`` span in ``text``, inner text, whitespace-normalised."""
    return {_norm(m.group(0)[1:-1]) for m in ITALIC_RE.finditer(text)}


def rule3c_matches(
    head: str, labs: list[str], urls: dict[str, str], def_bodies: dict[str, str]
) -> list[tuple[re.Match, str]]:
    """Review finding M2. For each italic title in ``head``, find the one
    marker (of ``labs``) whose own definition names that same title. Returns
    the accepted ``(match, label)`` pairs, in head order: a title with zero
    or several candidate markers, or a marker two titles would both claim,
    is excluded from the result entirely.
    """
    per_title: list[tuple[re.Match, list[str]]] = []
    for cand in ITALIC_RE.finditer(head):
        title = _norm(cand.group(0)[1:-1])
        matched = [
            lab
            for lab in labs
            if lab in urls and title in _italic_inner_set(def_bodies.get(lab, ""))
        ]
        per_title.append((cand, matched))
    unique = [(cand, m[0]) for cand, m in per_title if len(m) == 1]
    label_counts: dict[str, int] = {}
    for _, lab in unique:
        label_counts[lab] = label_counts.get(lab, 0) + 1
    return [(cand, lab) for cand, lab in unique if label_counts[lab] == 1]


def _split_head_tail(bullet: str) -> tuple[str, str, bool] | None:
    """Return ``(head, tail, has_dash)``, or ``None`` if the bullet has
    neither a `` -- `` annotation nor a trailing run of markers to anchor
    on. ``tail`` is everything from the head's own boundary onward,
    unchanged by any rule.
    """
    m = HEAD_TAIL_RE.match(bullet)
    if m:
        return m.group(1)[2:], bullet[m.end(1) :], True
    m2 = NODASH_RE.match(bullet)
    if m2:
        return m2.group(1)[2:], m2.group(2) + m2.group(3), False
    return None


def convert_bullet(
    bullet: str, urls: dict[str, str], def_bodies: dict[str, str]
) -> tuple[str | None, str]:
    """Return ``(new_bullet_or_None, reason)`` for one ``* ...`` bullet.

    ``bullet`` is the bullet's own text (starting with ``* ``, no
    trailing blank line). Returns ``None`` with the reason it was left
    alone, or the rewritten bullet text with a reason starting "ok-".
    """
    split = _split_head_tail(bullet)
    if split is None:
        return None, "no-dash"
    head, tail, has_dash = split
    if "](<" in head:
        return None, "already-linked"
    labs = MARK_RE.findall(bullet)
    if not labs:
        return None, "no-marker"

    if len(labs) == 1:
        lab = labs[0]
        if lab not in urls:
            return None, "no-url"
        url = urls[lab]
        if has_dash:
            if "{" in head or "[" in head or "`" in head:
                italics = ITALIC_RE.findall(head)
                if len(italics) != 1 or "{" in italics[0]:
                    return None, "role-in-head"
                new_head = head.replace(italics[0], f"[{italics[0]}](<{url}>)", 1)
                return "* " + new_head + tail, "ok-rule2"
            new_head = f"[{head}](<{url}>)"
            return "* " + new_head + tail, "ok-rule1"
        # Rule 1b (H1): no dash, one marker, no role/bracket/backtick, and
        # the head ends in "." -- link everything but that final ".",
        # which stays outside the link, immediately before the marker.
        if "{" in head or "[" in head or "`" in head or not head.endswith("."):
            return None, "no-dash"
        new_head = f"[{head[:-1]}](<{url}>)."
        return "* " + new_head + tail, "ok-rule1b"

    # Rule 3 / 3b: N markers, N italic titles, same order (with or without
    # a dash -- the reconstruction is identical either way).
    italics = list(ITALIC_RE.finditer(head))
    if len(italics) == len(labs):
        if any(lab not in urls for lab in labs):
            return None, "no-url"
        pieces: list[str] = []
        pos = 0
        for it, lab in zip(italics, labs):
            pieces.append(head[pos : it.start()])
            pieces.append(f"[{it.group(0)}](<{urls[lab]}>)")
            pos = it.end()
        pieces.append(head[pos:])
        new_head = "".join(pieces)
        return "* " + new_head + tail, "ok-rule3" if has_dash else "ok-rule3b"

    # Rule 3c (review finding M2): the exact N-for-N match failed, but an
    # italic title may still be uniquely identifiable from its own
    # marker's definition. Converts part of a bullet, never all of it if
    # rule 3/3b already would have.
    matches = rule3c_matches(head, labs, urls, def_bodies)
    if matches:
        matches = sorted(matches, key=lambda pair: pair[0].start())
        pieces = []
        pos = 0
        for it, lab in matches:
            pieces.append(head[pos : it.start()])
            pieces.append(f"[{it.group(0)}](<{urls[lab]}>)")
            pos = it.end()
        pieces.append(head[pos:])
        new_head = "".join(pieces)
        return "* " + new_head + tail, "ok-rule3c"

    return None, "multi-marker"


EXISTING_LINK_URL_RE = re.compile(r"\]\(<(https?://[^<>\s]+)>\)")


def refresh_bullet(bullet: str, urls: dict[str, str]) -> tuple[str | None, str]:
    """Review finding H2. Re-point a bullet's own link to its marker's
    *current* first URL, when a definition has moved (R-WAYBACK: converting
    a definition to archive-first form changes its first URL after a
    bullet already links the old one).

    Only a bullet with **exactly one marker and exactly one existing
    ``](<URL>)`` link** is touched -- the single shape rules 1, 1b and 2
    ever produce, and the only shape this can update without first having
    to work out which of several links belongs to which of several
    markers. A multi-link bullet (rule 3/3b/3c) is left alone. The
    replacement is always that marker's *own* definition's first URL,
    character for character -- never a URL from any other source.
    """
    labs = MARK_RE.findall(bullet)
    if len(labs) != 1:
        return None, "not-single-marker"
    lab = labs[0]
    if lab not in urls:
        return None, "no-url"
    link_urls = EXISTING_LINK_URL_RE.findall(bullet)
    if len(link_urls) != 1:
        return None, "not-single-link"
    old_url = link_urls[0]
    new_url = urls[lab]
    if old_url == new_url:
        return None, "up-to-date"
    new_bullet = bullet.replace(f"(<{old_url}>)", f"(<{new_url}>)", 1)
    return new_bullet, "ok-refresh"


def refresh_text(text: str) -> tuple[str, dict[str, int]]:
    """Like ``process_text``, but for ``--refresh``: touches only bullets
    under ``## References`` that already have a single link, re-pointing a
    stale URL to its own marker's current first URL. Never creates a new
    link, never touches a dropdown bullet (the same policy as
    ``convert_bullet``), never touches any other page content.
    """
    counts: dict[str, int] = {}
    urls = page_urls(text)
    rm = REFS_SECTION_RE.search(text)
    if not rm:
        return text, counts
    section = rm.group(1)
    dropdown_lines = check_inforce.dropdown_lines(text)
    base_lines = text[: rm.start(1)].count("\n")
    chunks = re.split(r"\n(?=\* )", section)
    out: list[str] = []
    offset = 0
    for idx, chunk in enumerate(chunks):
        if idx > 0:
            offset += 1
        if chunk.startswith("* "):
            bullet, sep, rest = chunk.partition("\n\n")
            abs_line = base_lines + section[:offset].count("\n") + 1
            if abs_line in dropdown_lines:
                new, reason = None, "in-dropdown"
            else:
                new, reason = refresh_bullet(bullet, urls)
            if new is not None:
                counts[reason] = counts.get(reason, 0) + 1
            chunk_out = (new if new is not None else bullet) + sep + rest
        else:
            chunk_out = chunk
        out.append(chunk_out if idx == 0 else "\n" + chunk_out)
        offset += len(chunk)
    new_section = "".join(out)
    new_text = text[: rm.start(1)] + new_section + text[rm.end(1) :]
    return new_text, counts


def process_text(text: str) -> tuple[str, dict[str, int]]:
    """Convert every eligible bullet under ``## References``.

    Returns ``(new_text, counts)`` where ``counts`` maps each reason (see
    ``REASONS``) to how many bullets fell into it. ``new_text`` is
    byte-identical to ``text`` when no bullet is converted.
    """
    counts: dict[str, int] = {}
    urls = page_urls(text)
    def_bodies = page_def_bodies(text)
    rm = REFS_SECTION_RE.search(text)
    if not rm:
        return text, counts
    section = rm.group(1)
    # Defensive: never touch the generated block, though it never sits
    # inside "## References" on this site (checked; it always precedes it).
    if GENBLOCK_RE.search(section):
        raise SystemExit(
            "fix_reading_list_links: found a generated index-links block "
            "inside '## References' -- refusing to touch this page"
        )
    dropdown_lines = check_inforce.dropdown_lines(text)
    base_lines = text[: rm.start(1)].count("\n")
    # Split at the single "\n" that separates two top-level bullets (the
    # prototype's boundary): a tight list has no blank line between
    # bullets, only between the last bullet of a tier and its heading. The
    # delimiter itself (one "\n") is dropped by split and put back below.
    chunks = re.split(r"\n(?=\* )", section)
    out: list[str] = []
    offset = 0
    for idx, chunk in enumerate(chunks):
        if idx > 0:
            offset += 1  # the "\n" delimiter consumed by split, restored
        if chunk.startswith("* "):
            # A bullet's own text ends at the first blank line, if any
            # (the tier heading that may follow it); anything from there
            # on is passed through untouched.
            bullet, sep, rest = chunk.partition("\n\n")
            abs_line = base_lines + section[:offset].count("\n") + 1
            if abs_line in dropdown_lines:
                new, reason = None, "in-dropdown"
            else:
                new, reason = convert_bullet(bullet, urls, def_bodies)
            counts[reason] = counts.get(reason, 0) + 1
            chunk_out = (new if new is not None else bullet) + sep + rest
        else:
            chunk_out = chunk
        out.append(chunk_out if idx == 0 else "\n" + chunk_out)
        offset += len(chunk)
    new_section = "".join(out)
    new_text = text[: rm.start(1)] + new_section + text[rm.end(1) :]
    return new_text, counts


def target_files(paths: list[str]) -> list[Path]:
    if paths:
        return [Path(p).resolve() for p in paths]
    return sorted(
        p
        for p in DOCS.rglob("*.md")
        if "plans" not in p.relative_to(DOCS).parts
        and "references" not in p.relative_to(DOCS).parts
    )


def run(paths: list[str], check: bool, refresh: bool = False) -> int:
    total: dict[str, int] = {}
    changed_files: list[Path] = []
    processor = refresh_text if refresh else process_text
    for path in target_files(paths):
        text = path.read_text(encoding="utf-8")
        new_text, counts = processor(text)
        for k, v in counts.items():
            total[k] = total.get(k, 0) + v
        if new_text != text:
            changed_files.append(path)
            if not check:
                path.write_text(new_text, encoding="utf-8")
    if refresh:
        print(f"{len(changed_files)} files {'would change' if check else 'changed'}")
        print(f"refreshed: {total.get('ok-refresh', 0)}")
        if check:
            for f in changed_files:
                print(f"would change: {f.relative_to(ROOT)}")
            return 1 if changed_files else 0
        return 0
    ok_total = sum(v for k, v in total.items() if k.startswith("ok-"))
    print(f"{len(changed_files)} files {'would change' if check else 'changed'}")
    print(f"converted: {ok_total}  ({', '.join(f'{k}={v}' for k, v in sorted(total.items()) if k.startswith('ok-'))})")
    left = {k: v for k, v in total.items() if not k.startswith("ok-")}
    print(f"left alone: {sum(left.values())}  ({', '.join(f'{k}={v}' for k, v in sorted(left.items()))})")
    if check:
        for f in changed_files:
            print(f"would change: {f.relative_to(ROOT)}")
        return 1 if changed_files else 0
    return 0


# --------------------------------------------------------------------------


def selftest() -> int:
    problems: list[str] = []

    def fail(msg: str) -> None:
        problems.append(msg)

    def refs(bullets: str, defs: str) -> str:
        return f"# T\n\n## References\n\n### Deep dive\n\n{bullets}\n{defs}"

    # Rule 1: plain head, single marker.
    page = refs(
        "* Wikipedia, *Shallow trench isolation* — the three STI operations "
        "and the LOCOS cross-over node.[^wiki-sti]\n",
        "[^wiki-sti]: Wikipedia, *Shallow trench isolation*. "
        "<https://en.wikipedia.org/wiki/Shallow_trench_isolation>\n",
    )
    new, counts = process_text(page)
    if counts.get("ok-rule1") != 1:
        fail(f"rule 1 did not fire: {counts}")
    if "[Wikipedia, *Shallow trench isolation*](<https://en.wikipedia.org/wiki/Shallow_trench_isolation>)" not in new:
        fail(f"rule 1 produced the wrong head: {new!r}")
    if "the LOCOS cross-over node.[^wiki-sti]" not in new:
        fail(f"rule 1 dropped the trailing marker or the annotation: {new!r}")
    # Idempotent.
    new2, counts2 = process_text(new)
    if new2 != new:
        fail("rule 1 output is not idempotent")
    if counts2.get("already-linked") != 1:
        fail(f"the second pass did not recognise the link: {counts2}")

    # Rule 2: role/backtick in head, exactly one italic title.
    page = refs(
        "* SkyWater PDK, {ref}`Periphery rules <mask-periph>`, *Design rule "
        "manual* — the periphery constraints.[^pdk-periph]\n",
        "[^pdk-periph]: SkyWater PDK Authors, *Design rule manual*. "
        "<https://example.com/periph>\n",
    )
    new, counts = process_text(page)
    if counts.get("ok-rule2") != 1:
        fail(f"rule 2 did not fire: {counts}")
    if "[*Design rule manual*](<https://example.com/periph>)" not in new:
        fail(f"rule 2 linked the wrong span: {new!r}")
    if "{ref}`Periphery rules <mask-periph>`" not in new:
        fail("rule 2 touched the {ref} role")

    # Rule 3: N markers, N italic titles, in order.
    page = refs(
        "* Wikipedia, *Silane*, *Tetraethyl orthosilicate* and *Nitrogen "
        "trifluoride* — the precursors and the clean "
        "gas.[^wiki-silane][^wiki-teos][^wiki-nf3]\n",
        "[^wiki-silane]: Wikipedia, *Silane*. <https://en.wikipedia.org/wiki/Silane>\n"
        "[^wiki-teos]: Wikipedia, *Tetraethyl orthosilicate*. "
        "<https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>\n"
        "[^wiki-nf3]: Wikipedia, *Nitrogen trifluoride*. "
        "<https://en.wikipedia.org/wiki/Nitrogen_trifluoride>\n",
    )
    new, counts = process_text(page)
    if counts.get("ok-rule3") != 1:
        fail(f"rule 3 did not fire: {counts}")
    for title, url in (
        ("*Silane*", "https://en.wikipedia.org/wiki/Silane"),
        ("*Tetraethyl orthosilicate*", "https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate"),
        ("*Nitrogen trifluoride*", "https://en.wikipedia.org/wiki/Nitrogen_trifluoride"),
    ):
        if f"[{title}](<{url}>)" not in new:
            fail(f"rule 3 did not link {title} to {url}: {new!r}")
    if "[^wiki-silane][^wiki-teos][^wiki-nf3]" not in new:
        fail("rule 3 disturbed the marker order")

    # Rule 3 across a wrapped line: an italic title split by the text
    # wrapping (docs/machines/pecvd.md:470-471) is still one title.
    page = refs(
        "* Wikipedia, *Silane*, *Tetraethyl orthosilicate* and *Nitrogen\n"
        "  trifluoride* — the precursors and the clean "
        "gas.[^wiki-silane][^wiki-teos][^wiki-nf3]\n",
        "[^wiki-silane]: Wikipedia, *Silane*. <https://en.wikipedia.org/wiki/Silane>\n"
        "[^wiki-teos]: Wikipedia, *Tetraethyl orthosilicate*. "
        "<https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>\n"
        "[^wiki-nf3]: Wikipedia, *Nitrogen trifluoride*. "
        "<https://en.wikipedia.org/wiki/Nitrogen_trifluoride>\n",
    )
    new, counts = process_text(page)
    if counts.get("ok-rule3") != 1:
        fail(f"rule 3 did not fire across a wrapped line: {counts}")
    if "[*Nitrogen\n  trifluoride*](<https://en.wikipedia.org/wiki/Nitrogen_trifluoride>)" not in new:
        fail(f"rule 3 mishandled a title wrapped across a line break: {new!r}")

    # A "**bold**" run in the head is never mistaken for an italic title.
    page = refs(
        "* **Loud Corp** and *Quiet Co* — two vendors.[^loud][^quiet]\n",
        "[^loud]: Loud Corp. <https://example.com/loud>\n"
        "[^quiet]: Quiet Co, *Quiet Co*. <https://example.com/quiet>\n",
    )
    new, counts = process_text(page)
    if counts.get("ok-rule3") == 1:
        fail(f"a bold run was treated as a second italic title: {new!r} {counts}")

    # Rule 3/3b do not fire when the counts differ; rule 3c also does not
    # fire when a title has zero or several matching definitions, or two
    # titles would claim the same marker (leftover: multi-marker).
    page = refs(
        "* Wikipedia, *Silane* and *Xenon* — the "
        "precursors.[^wiki-silane][^wiki-teos][^wiki-nf3]\n",
        "[^wiki-silane]: Wikipedia, *Silane*. <https://en.wikipedia.org/wiki/Silane>\n"
        # Neither *Xenon* nor these definitions' own titles match: teos's
        # def names "Tetraethyl orthosilicate" (not "Xenon"), so *Xenon*
        # has zero candidate markers, and wiki-nf3 has no title in the
        # head naming it at all.
        "[^wiki-teos]: Wikipedia, *Tetraethyl orthosilicate*. "
        "<https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>\n"
        "[^wiki-nf3]: Wikipedia, *Nitrogen trifluoride*. "
        "<https://en.wikipedia.org/wiki/Nitrogen_trifluoride>\n",
    )
    new, counts = process_text(page)
    if counts.get("ok-rule3c") != 1 or "[*Silane*](<https://en.wikipedia.org/wiki/Silane>)" not in new:
        fail(f"rule 3c did not link the one unambiguous title: {new!r} {counts}")
    if "*Xenon*" not in new or "[*Xenon*]" in new:
        fail(f"rule 3c wrongly linked a title with no matching definition: {new!r}")

    # Rule 3c: a marker two titles would both claim is left alone for both
    # (three markers, so rule 3/3b's exact N-for-N match cannot fire on
    # these two italics; both resolve uniquely, but to the *same* marker,
    # whose own definition happens to name both).
    page = refs(
        "* Some Co, *Foo* and *Bar* — two names for one "
        "thing.[^x][^y][^z]\n",
        "[^x]: Some Co, *Foo* and *Bar*. <https://example.com/x>\n"
        "[^y]: Other Co. <https://example.com/y>\n"
        "[^z]: Third Co. <https://example.com/z>\n",
    )
    new, counts = process_text(page)
    if new != page or counts.get("multi-marker") != 1:
        fail(f"an ambiguous multi-marker bullet was changed: {new!r} {counts}")

    # Rule 1b (H1): no dash, one marker, head ends in ".": link everything
    # but the final "."; the "." and the marker stay outside the link.
    page = refs(
        "* Wikipedia, *Furnace anneal*.[^wiki-furnace]\n",
        "[^wiki-furnace]: Wikipedia, *Furnace anneal*. "
        "<https://en.wikipedia.org/wiki/Diffusion_furnace>\n",
    )
    new, counts = process_text(page)
    if counts.get("ok-rule1b") != 1:
        fail(f"rule 1b did not fire: {counts}")
    if ("* [Wikipedia, *Furnace anneal*]"
        "(<https://en.wikipedia.org/wiki/Diffusion_furnace>).[^wiki-furnace]") not in new:
        fail(f"rule 1b produced the wrong bullet: {new!r}")

    # Rule 1b does not fire without a trailing "." (leftover: no-dash).
    page = refs(
        "* Wikipedia, *Silane*[^wiki-silane]\n",
        "[^wiki-silane]: Wikipedia, *Silane*. <https://en.wikipedia.org/wiki/Silane>\n",
    )
    new, counts = process_text(page)
    if new != page or counts.get("no-dash") != 1:
        fail(f"a dashless, dotless bullet was touched: {new!r} {counts}")

    # Rule 1b does not fire on a role/backtick head (leftover: no-dash).
    page = refs(
        "* SkyWater PDK, `gds_layers.csv`.[^pdk-05]\n",
        "[^pdk-05]: SkyWater PDK Authors, *Layers Reference*. "
        "<https://example.com/layers>\n",
    )
    new, counts = process_text(page)
    if new != page or counts.get("no-dash") != 1:
        fail(f"a role-in-head dashless bullet was touched: {new!r} {counts}")

    # Rule 3b (H1): no dash, N trailing markers, N italic titles in order.
    page = refs(
        "* Wikipedia, *Ion implantation*, *Phosphine* and "
        "*Arsine*.[^wiki-implant][^wiki-ph3][^wiki-ash3]\n",
        "[^wiki-implant]: Wikipedia, *Ion implantation*. "
        "<https://en.wikipedia.org/wiki/Ion_implantation>\n"
        "[^wiki-ph3]: Wikipedia, *Phosphine*. <https://en.wikipedia.org/wiki/Phosphine>\n"
        "[^wiki-ash3]: Wikipedia, *Arsine*. <https://en.wikipedia.org/wiki/Arsine>\n",
    )
    new, counts = process_text(page)
    if counts.get("ok-rule3b") != 1:
        fail(f"rule 3b did not fire: {counts}")
    for title, url in (
        ("*Ion implantation*", "https://en.wikipedia.org/wiki/Ion_implantation"),
        ("*Phosphine*", "https://en.wikipedia.org/wiki/Phosphine"),
        ("*Arsine*", "https://en.wikipedia.org/wiki/Arsine"),
    ):
        if f"[{title}](<{url}>)" not in new:
            fail(f"rule 3b did not link {title} to {url}: {new!r}")
    if ").[^wiki-implant][^wiki-ph3][^wiki-ash3]" not in new:
        fail(f"rule 3b disturbed the trailing markers: {new!r}")

    # Leftover: marker with no URL in its own definition.
    page = refs(
        "* Wikipedia, *Silane* — the precursor.[^wiki-silane]\n",
        "[^wiki-silane]: Wikipedia, *Silane* (no URL retrieved).\n",
    )
    new, counts = process_text(page)
    if new != page or counts.get("no-url") != 1:
        fail(f"a urlless-definition bullet was touched: {new!r} {counts}")

    # Never touches the generated index-links block or a bullet outside
    # "## References".
    page = (
        "# T\n\n## Related steps and cross-references\n\n"
        "* Wikipedia, *Foo* — a gloss.[^wiki-foo]\n\n"
        "## References\n\n### Deep dive\n\n"
        "* Wikipedia, *Bar* — a gloss.[^wiki-bar]\n\n"
        "[^wiki-foo]: Wikipedia, *Foo*. <https://en.wikipedia.org/wiki/Foo>\n"
        "[^wiki-bar]: Wikipedia, *Bar*. <https://en.wikipedia.org/wiki/Bar>\n"
    )
    new, counts = process_text(page)
    if "[Wikipedia, *Foo*]" in new:
        fail("a bullet outside '## References' was converted")
    if "[Wikipedia, *Bar*](<https://en.wikipedia.org/wiki/Bar>)" not in new:
        fail("the in-section bullet was not converted")

    # A bullet inside a {dropdown} (an in-force patent note) is left
    # untouched, even though it otherwise matches rule 1.
    page = (
        "# T\n\n## References\n\n### Deep dive\n\n"
        ":::{dropdown} From a patent shown as in force (US 1,234,567; "
        "estimated expiry 2030-01-01) — open to read\n"
        "* Doe (Acme), US 1,234,567 — a gloss.[^pat-doe]\n"
        ":::\n\n"
        "* Wikipedia, *Open* — a gloss.[^wiki-open]\n\n"
        "[^pat-doe]: Doe. <https://patents.google.com/patent/US1234567>\n"
        "[^wiki-open]: Wikipedia, *Open*. <https://en.wikipedia.org/wiki/Open>\n"
    )
    new, counts = process_text(page)
    if counts.get("in-dropdown") != 1:
        fail(f"a dropdown bullet was not recognised: {counts}")
    if "[Doe (Acme), US 1,234,567]" in new:
        fail(f"a bullet inside a dropdown was converted: {new!r}")
    if "[Wikipedia, *Open*](<https://en.wikipedia.org/wiki/Open>)" not in new:
        fail(f"the bullet after the dropdown was not converted: {new!r}")

    # A bullet already converted by hand is left exactly as it is.
    page = refs(
        "* [Wikipedia, *Baz*](<https://en.wikipedia.org/wiki/Baz>) — a "
        "gloss.[^wiki-baz]\n",
        "[^wiki-baz]: Wikipedia, *Baz*. <https://en.wikipedia.org/wiki/Baz>\n",
    )
    new, counts = process_text(page)
    if new != page or counts.get("already-linked") != 1:
        fail(f"an already-linked bullet was not left alone: {new!r} {counts}")

    # --refresh (H2): a bullet's link is re-pointed when its own marker's
    # definition now gives a different first URL (simulating R-WAYBACK:
    # the definition below has moved to an archive-first form, but the
    # bullet above still links the old, now-dead URL).
    page = refs(
        "* [Wikipedia, *Baz*](<https://en.wikipedia.org/wiki/Old>) — a "
        "gloss.[^wiki-baz]\n",
        "[^wiki-baz]: Wikipedia, *Baz*. "
        "<https://web.archive.org/web/20260101000000/https://en.wikipedia.org/wiki/Baz>\n"
        "    (Wayback Machine capture of 2026-01-01; original, dead since "
        "2026-02-01: `https://en.wikipedia.org/wiki/Old`).\n",
    )
    new, counts = refresh_text(page)
    if counts.get("ok-refresh") != 1:
        fail(f"--refresh did not fire on a moved URL: {counts}")
    if ("[Wikipedia, *Baz*]"
        "(<https://web.archive.org/web/20260101000000/https://en.wikipedia.org/wiki/Baz>)"
        ) not in new:
        fail(f"--refresh produced the wrong link: {new!r}")
    if "[^wiki-baz]" not in new:
        fail("--refresh disturbed the marker")

    # --refresh leaves an up-to-date link untouched (and is therefore
    # idempotent: refreshing twice makes no further change).
    new2, counts2 = refresh_text(new)
    if new2 != new or counts2.get("ok-refresh", 0):
        fail(f"--refresh is not idempotent: {counts2}")

    # --refresh never touches a multi-link bullet (rule 3): it cannot know
    # which of several links belongs to which of several markers without
    # redoing that match, so it leaves the whole bullet alone even if one
    # of its markers' definitions has moved.
    page = refs(
        "* Wikipedia, [*Silane*](<https://en.wikipedia.org/wiki/Old-Silane>) "
        "and [*Arsine*](<https://en.wikipedia.org/wiki/Arsine>) — two "
        "gases.[^wiki-silane][^wiki-ash3]\n",
        "[^wiki-silane]: Wikipedia, *Silane*. "
        "<https://en.wikipedia.org/wiki/Silane>\n"
        "[^wiki-ash3]: Wikipedia, *Arsine*. <https://en.wikipedia.org/wiki/Arsine>\n",
    )
    new, counts = refresh_text(page)
    if new != page or counts.get("ok-refresh", 0):
        fail(f"--refresh touched a multi-link bullet: {new!r} {counts}")

    # --refresh never touches a dropdown bullet, and never creates a link
    # where none existed (a bullet --check would still report as a
    # candidate for ordinary conversion is not --refresh's job).
    page = (
        "# T\n\n## References\n\n### Deep dive\n\n"
        ":::{dropdown} From a patent shown as in force (US 1,234,567; "
        "estimated expiry 2030-01-01) — open to read\n"
        "* [Doe (Acme), US 1,234,567](<https://old.example/patent>) — a "
        "gloss.[^pat-doe]\n"
        ":::\n\n"
        "* Wikipedia, *Unlinked* — a gloss.[^wiki-unlinked]\n\n"
        "[^pat-doe]: Doe. <https://patents.google.com/patent/US1234567>\n"
        "[^wiki-unlinked]: Wikipedia, *Unlinked*. "
        "<https://en.wikipedia.org/wiki/Unlinked>\n"
    )
    new, counts = refresh_text(page)
    if new != page or counts.get("ok-refresh", 0):
        fail(f"--refresh touched a dropdown link or an unlinked bullet: "
             f"{new!r} {counts}")

    if problems:
        for p in problems:
            print("FAIL:", p)
        return 1
    print("selftest OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="report only, write nothing")
    ap.add_argument(
        "--refresh",
        action="store_true",
        help=(
            "re-point an already-linked bullet's URL to its own marker's "
            "current first URL (e.g. after R-WAYBACK); never links a new "
            "bullet, combine with --check for a dry run"
        ),
    )
    ap.add_argument("--selftest", action="store_true", help="run offline unit tests")
    ap.add_argument("paths", nargs="*")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    return run(args.paths, args.check, args.refresh)


if __name__ == "__main__":
    sys.exit(main())
