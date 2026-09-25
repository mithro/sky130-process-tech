# Progress — rd-preserved2 (tools/check_preserved.py gap fixes)

Branch: topic/rd-preserved2. Task: fix three `check_preserved.py` gaps found while
editing `docs/overview/index.md` on topic/rd-overview (see
`docs/plans/progress-rd-overview.md` on that branch), plus two more findings that
arrived mid-task from the coordinator:

1. A numbered bold run-in label immediately followed by `**` defeats the
   sentence-split regex (false `number_order` LOST on R-H3).
2. `extract_number_order`/`extract_numbers`/identifiers have no fence-skipping:
   `:::{table}`/`:widths:` directive lines are read as prose (undeclarable
   `number_order` ADDED on R-CAPTION).
3. A numeric prose sequence regrouped into one-number-per-row/item table/list
   rows is an unconditional, undeclarable `number_order` LOST.
4. (mid-task, from the rd-overview reviewer, section C) `_GROUPED` misreads
   "Q4 2020" as tokens "4 202" + "0" (no right boundary on the thousands-space
   separator).
5. (mid-task, from the rd-site reviewer, finding L5) `ROLE_RE` runs through an
   inline code span's own backtick and fabricates a fake `{term}`/{ref}` match
   when a role is shown as a literal code example.

The rd-overview reviewer wrote and tested a prototype fix for 1-4 at
`.worktrees/rd-overview/tmp/rev/cp/check_preserved_fixes.diff` (section C of
`tmp/reviews/rd-overview.md`). That prototype is against an OLDER tool version
(pre-`--allow-regrouped`/T1-T3/inch-mark commits already on `main`). Reconciling:
kept `main`'s existing `--allow-regrouped` flag-gated architecture (the task asks
for behaviour "accepted under --allow-regrouped", not always-on), but adopted the
reviewer's much simpler mechanism for gap 3 (a flat left-to-right number "stream"
per page; a LOST tuple that still appears as a contiguous run in the new stream is
a clean regroup) in place of my own draft per-unit-subsequence design, since it
already handles the one-number-per-row case directly and is proven against the
real page. Adopted the reviewer's C1/C2/C4 regexes near-verbatim.

## Status: implementing

See the commits for what landed; this file is updated as each piece completes.
