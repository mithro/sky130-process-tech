# Progress — rd-theme (W0a theme, W0b check_preserved.py)

## Done

* `docs/_static/custom.css` — footnote back-reference wrap fix (report-C C2),
  footnote popover card styling, top-aligned/zebra tables, a narrow-screen
  smaller table font, no-wrap quick-facts first-column labels, 44em prose
  measure (tables/code/figures/admonitions excluded), "Sources cited on
  this page" label, left-aligned small figure captions, bold glossary
  terms. Furo CSS variables only (no separate dark-mode block needed).
  **Superseded by the review round below:** the sticky table header and
  the narrow-screen sticky first column originally shipped here were
  both dropped (dead code / mutilated prose tables — M1, M2).
* `docs/_static/footnote-popover.js` — hover/focus/first-tap popover card
  for footnote markers, reading the existing `<aside class="footnote">`
  definitions; Esc/click-away closes; second tap on touch follows the
  link. No dependency. **Current behaviour reflects the review-round
  fixes below** (real first-tap/second-tap behaviour, keyboard
  reachability, `position: fixed`).
* `docs/conf.py` — registered `custom.css` (html_css_files) and
  `footnote-popover.js` (html_js_files). `navigation_with_keys` was
  tried and dropped (review M3 — see below).
* `tools/check_preserved.py` (W0b) — before/after preservation checker.
  `--selftest` covers all required pass/fail cases. Spot-checked against
  real pages (006-stie.md, 001-smat.md) with simulated edits (dropped
  marker, changed number, moved dropdown text) — all correctly detected;
  clean on real unedited pages.
* `docs/plans/agent-briefs.md` — added "Checking a readability edit"
  section documenting `check_preserved.py` usage.
* All required checkers, generator `--check`s pass (see below).
* Verified with `tools/shoot.py` screenshots (desktop + 400px phone) of:
  overview/index, steps/006-stie, machines/index, materials/index,
  glossary. Confirmed the overview at 400 px is no longer wider than the
  screen (all tiles exactly 400 px; the 29-backref `pdk-04` footnote wraps
  cleanly) and that the "Sources cited on this page" label, zebra/
  top-aligned/sticky-header tables and no-wrap quick-facts labels render
  as intended.
* Interaction states forced with static copies under `tmp/_build/html/`
  (not committed; `tmp/` is git-ignored):
  * dark mode: a copy of steps/006-stie.html with the inline theme script
    hardcoded to `"dark"` (the normal `localStorage`-reading script would
    otherwise reset any `data-theme` attribute set on `<body>`) — zebra
    rows, links, code spans and borders all follow furo's dark palette
    correctly, confirming the CSS uses only furo variables.
  * popover, table cell: a copy of steps/006-stie.html with a script that
    focuses the `[^steps-sheet]` marker in the quick-facts table — card
    appears beside the marker with live link, clamped to the viewport at
    400 px.
  * popover, open dropdown: a copy of machines/starting-material.html
    with its first in-force `{dropdown}` forced `open` and a script that
    focuses the footnote marker inside it (a footnote cited 5 times on
    that page, to also check the "cited many times" case) — card renders
    correctly beside the marker, not clipped by the dropdown's own box,
    at both widths.
  * Debugging note: a naive `element.focus()` fired directly on the
    `load` event raced headless Chrome's own viewport-settling after
    `--window-size`, once producing an unclamped card width — confirmed
    by instrumentation to be a test-harness artifact (real interactions
    happen long after the viewport is stable), fixed in the test by
    waiting for `window.innerWidth` to stabilise across animation frames
    before focusing. No change was needed to `footnote-popover.js`.

## Review round (2026-09-20, independent review at tmp/reviews/rd-theme.md)

Verdict was "approve with fixes" (H1, M1, M2 required before merge; H2/M4
fixed or the claims dropped; M3 an owner call; rest could follow). Fixed
everything High and Medium, plus every Low except two recorded below.

* **H1 (`check_preserved.py` quotes invisible/false-positive across a
  line break).** Fixed: match quotes against the whitespace-flattened
  text, not the raw text (readability-guide.md §7's hand recipe already
  did this). Cap raised 200→400. Reproduced the reviewer's own two
  examples after the fix: the `for example`→`for instance` change inside
  the multi-line STI-depth quotation on `006-stie.md` is now caught; a
  full re-wrap of the same paragraph at a different width (moving every
  line break, including through that quotation) now passes. Ran the
  checker over every written page against `main` with no edits: 0 pages
  flagged (was the baseline before, still is).
* **H2 (`footnote-popover.js` first tap follows the link).** Fixed by
  tracking tap state in the pointerdown/click handlers themselves
  (`tappedMarker`), independent of `owner` (which a touch device's
  emulated `mouseenter` sets before `click` fires, defeating the old
  `owner !== marker` guard). Hit a second, self-inflicted bug while
  building the verification test: `show()`'s internal `hide()` (closing
  any other open card) also clears `tappedMarker`, so setting the flag
  *before* calling `show()` in the pointerdown handler let that same
  call erase it before the click handler ran. Fixed by setting the flag
  *after* `show()` returns. Verified with a headless test dispatching a
  synthetic pointerdown/mouseenter/pointerup/click sequence twice (then
  a third time) on the same marker: `defaultPrevented` is
  `true, false, true` — open-without-navigating, then follow, then
  fresh again. See commit history for the exact script.
* **M1 (dead sticky table header) / L1 (its grey stub row).** Deleted:
  furo's own `.table-wrapper` is the scroll container on both axes (an
  `overflow-x: auto` box with no explicit `overflow-y` computes
  `overflow-y: auto` too), so it never scrolls vertically and
  `thead th { position: sticky; top: 0 }` never had anything to stick
  to. Its background was the only source of the grey stub row over
  quick-facts tables' blank header cell, so deleting it fixes L1 too.
* **M2 (sticky first column mutilates prose-first-column tables).**
  Dropped rather than scoped: a CSS-only way to tell "short key column"
  (materials/index) from "wrapped prose column" (machines/index,
  masks/index) does not exist without content-aware markup, and adding
  a class to those tables belongs to the generators (W0d/W0e), which
  this branch does not own and must not hand-edit around (content pages
  stay untouched). Kept the narrow-screen smaller font, which helps
  every table and has no such failure mode. Re-screenshotted
  machines/index, materials/index, masks/index and steps/index at
  400 px: plain scrollable tables, no overlapping/corrupted text.
* **M3 (`navigation_with_keys` hijacks arrow keys over wide tables).**
  Dropped, per the review's non-owner option; recorded here as the
  owner-reversible decision report-C C12 anticipated.
* **M4 (popover not reachable/announced).** Fixed: the card is inserted
  right after its marker in DOM order (was appended to `<body>`) so Tab
  reaches its links immediately; the marker carries
  `aria-expanded`/`aria-describedby` while open; `role="tooltip"`; a
  `focusin`/`focusout` pair on the card keeps it open while focus is
  inside it, so Tabbing from the marker into the card's link does not
  close it, and Tab continues past it afterwards (nothing traps focus).
  This forced `.fn-popover` from `position: absolute` to `position:
  fixed` (custom.css): a marker inside a sphinx_design `{dropdown}` now
  has the card as a DOM sibling inside `.sd-card`, which sphinx-design
  gives `position: relative` — that would have become the absolutely
  positioned card's containing block, breaking the viewport-relative
  math. `fixed` is anchored to the viewport regardless, and still
  escapes a `.table-wrapper`'s or `.sd-card`'s own overflow clipping.
  Re-verified the popover-in-a-table-cell and popover-in-an-open-dropdown
  cases from the first round after this change; both still correct at
  both widths.
* **M5 (multiset check is blind to rearrangement; brief oversold it).**
  Added a `number_order` category (also satisfies the coordinator's
  explicit ask): per table row / list item / heuristically-split
  sentence with two or more numbers, compares the left-to-right order,
  catching "6 of 171" → "171 of 6" (added as a `--selftest` case).
  Documented the remaining gap — a number or marker moved *between*
  units, or invented prose with no number at all, is still invisible —
  in both the module docstring and a new paragraph in
  agent-briefs.md's "Checking a readability edit", with the instruction
  that any `--allow-added` category used on a page must be named, with
  the reason, in the branch's progress file.
* **L5 (popover never flips above the marker).** Fixed: flips when
  there is no room below and there is room above.
* **L6 (detached card on an empty definition).** Fixed by checking the
  definition has content *before* creating/assigning `card`, not after.
* **L7 (stale CSS comment about marker wrapping).** Reworded.
* **L3 (zebra rows near-invisible).** Switched to
  `--color-background-hover` for more contrast in both themes.
* **L8/L9/L10 (`check_preserved.py` polish).** Guarded
  `page.relative_to(ROOT)` instead of a raw traceback; declared
  additions now print tagged `(declared)`; `footnotes`/`urls` get a
  300-character display truncation instead of 100 (display only, not
  the matching cap).
* **L2 (44em measure barely bites) — recorded reason, not changed.**
  furo's own `.content` box is already ~46em; a real reduction needs a
  narrower article width (furo's `--content-width`), which is a
  bigger, separate decision than this rule. Left the rule with an
  explanatory comment for whoever makes that call.
* **L4 ("Sources cited on this page" is a `::before`, not a real,
  linkable element) — recorded reason, not changed.** A real heading
  needs a Sphinx/docutils-level transform (the footnote list is
  docutils output inside page content; a `_templates` override cannot
  reach into it), which is out of scope for a CSS/JS-only theme branch.
  Left as is.

## Checker/build results (this branch, working tree)

* `check_steps.py`: 171 pages, 0 missing headings, 0 stale index-links.
* `check_refs.py`: 264 pages, 0 problems.
* `check_machines.py` / `check_materials.py` / `check_masks.py`: 0 problems.
* `check_papers.py` / `check_patents.py` / `check_filings.py` /
  `check_inforce.py`: 0 problems.
* `gen_papers.py` / `gen_patents.py` / `gen_filings.py` /
  `gen_index_links.py` `--check`: 0 problems.
* `uv run sphinx-build -W -q -b html docs tmp/_build/html`: clean (exit 0,
  no warnings).

## Decisions / notes

* Footnote HTML in this Sphinx/docutils version is
  `<aside class="footnote brackets" id="label">` with a
  `<span class="backrefs">`, matching the prototype's assumptions exactly
  (no change needed there).
* Quick-facts no-wrap rule targets any table row whose first cell is a
  lone bold run (`td:first-child:nth-last-child(2) > p:only-child >
  strong:only-child`) rather than a page-specific class, since quick-facts
  tables carry no distinguishing class today.
* Narrow-table breakpoint set at 40em (~640px); comfortably covers the
  400px phone screenshots.
* No factual/arithmetic issues noticed (no content pages touched — theme
  and tooling only, per instructions).

## Left to do

* Nothing outstanding for W0a/W0b against the review. Two Lows kept as
  documented, reversible decisions (L2, L4 — see above); everything
  else High/Medium/Low is fixed. Push branch.
* For whoever owns W0d/W0e: a `:class:` (or generator-emitted class) on
  the machines/materials/masks index tables saying which have a
  short-key first column would let the sticky-first-column idea (M2)
  come back safely, scoped correctly.
