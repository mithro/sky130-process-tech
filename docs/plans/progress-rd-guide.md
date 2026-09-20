# Progress — rd-guide (docs/plans/readability-guide.md)

Task: write the single executor-facing rule book for the readability phase, consolidated from
`docs/plans/readability/report-A.md` … `report-D.md` and `docs/plans/readability-plan.md`.
No content page, tool or checker is edited on this branch.

## Done

* Read all four reports, `readability-plan.md`, `agent-briefs.md`, `citation-style.md`, and the checkers
  (`check_steps`, `check_refs`, `check_machines`, `check_materials`, `check_masks`, `check_inforce`,
  `gen_index_links`, `gen_steps`, `shoot.py`).
* Baseline: all nine checkers, four generator `--check`s and the `-W` build pass on this branch.
* Guide §1 limits table (conflicting numbers between reports resolved, with the source of each), §2 Never
  list (check_inforce behaviour taken from the code, mandatory headings taken from the checkers).

## Verifications done for the guide (not guesses)

* MyST forms built under `-W` in a scratch project (`tmp/syntax/`) with this project's `conf.py`
  settings: `{table}` with caption/`:widths:`/`:class:`, table inside a list item, `{admonition}`,
  `{note}`, `{seealso}`, `{dropdown}`, `{grid}`/`{grid-item-card}` with `:link:`/`:link-type: ref`,
  `{tab-set}`/`{tab-item}`, definition list, `{figure}` with alt/width/name and a caption carrying
  footnotes, footnotes in table cells. `{numref}` fails the build (warning "numfig is disabled").
* `check_materials.py` on a copy of `docs/materials` (its optional path argument): still passes when the
  quick-facts table is wrapped in `:::{table}` with a caption, and when the "Steps:" line and its link run
  are moved inside a `{dropdown}`.
* `check_machines.py` on a copy of the tree under `tmp/mtest/`: still passes when the step-link run is
  wrapped in a `{dropdown}` and a new steps table is placed *after* it; **fails** with
  "steps: page only [], index only […]" when the new table is placed *before* the run.
* The measurement scripts under `docs/plans/readability/prototypes/measure/` resolve the repository root
  as `Path(__file__).resolve().parents[3]`, which is `docs/plans` at their committed location, so they
  silently measure nothing there. Copy them three levels below the root first (recipe in the guide, §3).

## Left

* Rule sections, page-type sections, checker contract, MyST crib, procedures, reviewer checklist.

## Notes for the coordinator

* `docs/steps/160-vim4e.md:86-88` is a list continuation that lost its indentation (source defect, noted
  by report A at different line numbers). It renders, but it will trip any mechanical splitter.
