# Progress — rd-theme (W0a theme, W0b check_preserved.py)

## Done

* `docs/_static/custom.css` — footnote back-reference wrap fix (report-C C2),
  footnote popover card styling, top-aligned/zebra/sticky-header tables,
  narrow-screen smaller table font + sticky first column inside furo's
  `.table-wrapper`, no-wrap quick-facts first-column labels, 44em prose
  measure (tables/code/figures/admonitions excluded), "Sources cited on
  this page" label, left-aligned small figure captions, bold glossary
  terms. Furo CSS variables only (no separate dark-mode block needed).
* `docs/_static/footnote-popover.js` — hover/focus/first-tap popover card
  for footnote markers, reading the existing `<aside class="footnote">`
  definitions; Esc/click-away closes; second tap on touch follows the
  link. No dependency.
* `docs/conf.py` — registered `custom.css` (html_css_files),
  `footnote-popover.js` (html_js_files), and
  `navigation_with_keys: True` in `html_theme_options`.
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

* Nothing outstanding for W0a/W0b. Push branch.
