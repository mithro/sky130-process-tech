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
  glossary; a static dark-mode test page; a static popover-open test page.

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
