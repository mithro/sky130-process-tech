# Progress — rd-guide (docs/plans/readability-guide.md)

Task: write the single executor-facing rule book for the readability phase, consolidated from
`docs/plans/readability/report-A.md` … `report-D.md` and `docs/plans/readability-plan.md`.
No content page, tool or checker was edited on this branch.

## Status: complete

`docs/plans/readability-guide.md`, about 2,150 lines:

* §1 one table of limits for the whole site, with the source of each number and the report conflicts
  resolved (paragraph cap 100, sentence cap 45, markers per paragraph 6, columns per B's budget).
* §2 the Never list: facts, hedges, markers, empty cells, dropdown boundaries, what `check_inforce.py`
  enforces (read from its code), the generated blocks and pages, the mandatory headings per page type,
  `{numref}`, inline URLs, the Deep dive bullet count.
* §3 31 rules (`R-PARA` … `R-FIGURE`), preceded by an index table. Each has a mechanical trigger,
  numbered steps, a real before/after with `file:line`, what must not be touched, a grep or measurement
  recipe that was run on this branch, and whether it is hand, scripted or generator work.
* §4 a section per page type: skeleton, order of rules, page-specific limits, checkers to run.
* §5 the checker contract, per checker, from the code, with the verified failure modes.
* §6 a MyST crib, every form built under `-W` in a scratch project with this project's settings.
* §7 the per-page procedure, §8 the reviewer checklist, §9 the blocked-rule table (W0a–W0f, W1a, owner).

## Verifications done for the guide (not guesses)

* MyST forms built under `-W` (scratch project, this project's `conf.py` settings): `{table}` with
  caption/`:widths:`/`:class:` (with and without a blank line after the options, and with a footnote in
  the caption), table inside a list item, `{admonition}`, `{note}`, `{seealso}` (also inside a list
  item), `{dropdown}` in both fence styles and inside a list item, `{grid}`/`{grid-item-card}` with
  `:link:`/`:link-type: ref`, `{tab-set}`, definition list, `{figure}` with alt/width/name and a caption
  carrying footnotes, footnotes in table cells. `{numref}` fails the build (exit 1).
* `check_materials.py` on a copy of `docs/materials`: passes with the quick-facts table wrapped in
  `:::{table}` + caption, and with the `Steps:` line and its run moved inside a `{dropdown}`.
* `check_machines.py` on a copy of the tree: passes with the run inside a `{dropdown}` and a new steps
  table after it; **fails** with the table before the run. A four-column table with a machine link in
  its first cell placed after the main table of `machines/index.md` silently replaces the checked row
  and the page checks fail.
* `check_masks.py` on a copy: a navigation table inserted before the checked table inside
  `## Mask steps in this reference` gives 76 problems; the same table under its own H2 passes.
* Preservation snippet in §7 tested both ways (unchanged page → `identical`; one marker and one digit
  changed → the loss is named).
* `tools/shoot.py` run against the local build at `--width 400`; tiles read.
* Counts quoted in the guide were re-measured on this branch: 647 unlabelled Open-questions bullets,
  396 "Strength:" uses, 93 hand-written dropdowns on 37 step pages, 107 "collapsed note" pointers on 35,
  38 bold run-ins on step pages outside the generated block, 217 on mask pages, 1,826 inventory
  entries, 206 pages with a generated index-links block, `titlelink_dryrun.py` → `ok: 6200`.

## Notes for the coordinator

* The measurement scripts at `docs/plans/readability/prototypes/measure/measure*.py` resolve the
  repository root as `parents[3]`, which is `docs/plans` at their committed location, so they silently
  measure nothing. The guide gives the copy-three-levels-down recipe; the real fix is one line in each
  script, on whichever branch owns them. `measure_b.py` and `titlelink_dryrun.py` and `gloss.py` resolve
  from the current directory and work from the repository root.
* `tools/gen_steps.py` is stale, as report A F17 says: `write_index()` emits a two-sentence intro and no
  `[^steps-sheet]` footnote, while the committed `docs/steps/index.md` carries a longer intro, the
  marker and the definition. Running it today deletes that citation and **no checker fails**
  (`check_refs.py` does not target `steps/index.md`). It must be fixed before any step-index work.
* Source defect: `docs/steps/160-vim4e.md:86-88` is a list continuation that lost its indentation. It
  renders, but it will trip any mechanical splitter. Not fixed here.
* Report A F15's second half — putting drawing labels such as `0.0` into quotation marks instead of
  backticks — is left out of the guide: it changes quoting, which the Never list forbids. Owner
  decision.
* Report A F12 (shorter in-force dropdown titles) is recorded as an owner decision and marked blocked;
  the guide tells executors to leave the titles alone, per `readability-plan.md` W2.
* Conflicting numbers between reports were resolved in §1 and the resolution is recorded in the table,
  so a later reviewer can see which report each limit came from.

## Checks on this branch

All nine checkers, the four generator `--check`s and `sphinx-build -W` pass (run before and after the
work; this branch touches only `docs/plans/`, which the build excludes and `check_inforce.py` skips).
