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

## Status: done

Commit `3fa15fc9`: all five fixes, docstring, agent-briefs.md "Checking a
readability edit" section. `--selftest` passes (new cases: gap1 heading,
gap2 fence/widths, gap3 singleton-row/list regroup + real-swap-still-caught
+ list variant, C4 "Q4 2020"-shaped case, L5 inline-code-example case + two
regression controls for genuine roles). Verified each of the 5 new cases
fails against the pre-fix `main` tool (copied to `tmp/cp_old_check/`,
scratch, not committed) before landing the fix, confirming the bug is real
and the fix addresses it. The full existing selftest suite (adversarial set:
changed number, dropped marker, altered multi-line quotation, dropped hedge,
swapped numbers in place, swapped table rows, text moved out of a dropdown)
still fails as before -- no regression.

Full check run (rd-common.txt point 7): check_steps/refs/machines/materials/
masks/papers/patents/filings/inforce all 0 problems; gen_papers/gen_patents/
gen_filings/gen_index_links --check all clean; `sphinx-build -W -q -b html`
passes (no content page touched, so this is a pure sanity check).

## Real-page run (as asked)

Made a detached scratch checkout of `topic/rd-overview`'s tip
(`6a3b3abc`, already includes that branch's own M1-M4/L1-L4 review fixes)
under `tmp/scratch/rd-overview-check/` (a nested `git worktree add
--detach`, removed again after use with `git worktree remove`), copied
this branch's fixed `tools/check_preserved.py` into it, and ran:

```
uv run python tools/check_preserved.py --base 0090926f
```

(`0090926f` = `git merge-base main topic/rd-overview`). Only page found
changed: `docs/overview/index.md` (matches the reviewer's own file list).

**Without `--allow-regrouped`:** 5 `number_order` tuples LOST, 5 ADDED
(the derivation/mask-count/PDK-generation paragraphs, now split), plus
`ADDED numbers: '1'`, `ADDED refs` (6, the on-page nav links + the new
`overview-what-sky130-is` label from M3), `ADDED identifiers: 'S8P',
'sky130-is'` (from the redone older-process-names table and the new
label). No fence/`:widths:`-caused additions at all -- fix 2 removed
those before they were ever counted.

**With `--allow-regrouped --allow-added numbers,refs,identifiers`:** all
5 LOST/ADDED `number_order` pairs are reclassified as informational
`REGROUPED` lines (fix 3) -- **`number_order` needs no `--allow-added`
declaration at all**, confirmed by re-running without it in the list:
still "0 with undeclared differences". The only declarations still
needed are `numbers` (the one real new "1" from the `**Metal 1 and
up.**` label), `refs` (the nav links/label), and `identifiers` (the M1-4
follow-up work, unrelated to the three original gaps).

Compared with the original progress file's declaration
(`--allow-added numbers,number_order,refs`), on the now-current page:
**`number_order` is no longer needed** (fixes 1-3 together resolve every
case that forced it: the false heading fusion, the `:widths:` additions,
and the derivation-paragraphs-into-list/table regroups); `identifiers`
is newly needed only because of the M1-4 follow-up work done after the
original declaration was written, not because of anything in this
branch.
