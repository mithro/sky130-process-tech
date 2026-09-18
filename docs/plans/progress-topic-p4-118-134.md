# Progress — topic/p4-118-134 (fixer for review-118-134.md)

Source review: `tmp/p4/review-118-134.md`. Working High -> Medium -> Low,
then the three site-wide sweeps the coordinator asked for in this
branch's brief (the "wider" via claim, the wet-bench solvent
attribution, and the step-name-ordinal soft form — grepped across the
whole `docs/` tree, not just 118-134).

## Findings

| id | severity | status | note |
|---|---|---|---|
| 118-H1 | High | fixed | via narrower not wider (118-vim.md:44-49) — commit b4f1068 |
| 120-H1 | High | fixed | via narrower not wider (120-tin3.md:39-43) — commit b4f1068 |
| 118-M1 | Medium | fixed | via resistance presented as measured, not PDK table value (5 sites: 118, 122-wcmp3, 130-vim2e, 133-wcmp4 x2) — commit 64c40dd |
| 119-M1 | Medium | fixed | EKS265/EKC270 solvents misattributed to wet-bench line, not batch-rotational (119-vime, 125-mm2e, 130-vim2e) — commit 5a806bb |
| 122-M1 | Medium | fixed | Common rule 2 soft form: step-code digit "3" used as evidence for ordinal (122-wcmp3.md:24-27) — commit 4904894 |
| 123-M1 | Medium | declined | Blech 1976 TiAl3 shunt misattribution — handled on topic/p4-107-117 (overlap instruction) |
| 118-L1 | Low | fixed | design-rule quotation cut short without [...] (118-vim, 129-vim2) — commit 7b447ff |
| 119-L1 | Low | fixed | UMC patent is dual-damascene remedy, scope not stated (119-vime, 121-wdep3, 130-vim2e, 132-wdep4 + deep-dive bullets; also found+fixed on 145-vim3e, 147-wdep5) — commit 540b5ce |
| 120-L1 | Low | fixed | "lands on aluminium... rather than TiN" contradicts TiN-on-TiW stated 20 lines earlier (120-tin3.md) — commit 1a2a337 |
| 122-L1 | Low | fixed | incomplete grant date on pat-cmp-ibm-1990 footnote (122, 127-cmpm2, 133-wcmp4) — commit 1a2a337; corrected reviewer's proposed date (1988-10-28 does not match the cached record; used 1985-10-28 filed / 1990-07-31 granted, per gp-US4944836-wb.html) |
| 123-L1 | Low | fixed | Cypress film string re-spaced inside quotation marks (123-tial12 x2, 134-wtial3 x2; 118-vim is prose not quoted, no change needed there) — commit 1a2a337 |
| 125-L1 | Low | fixed | PDK metal-layer antenna area is perimeter not plan area (125-mm2e.md) — commit 3ff9b57 |
| 125-L2 | Low | fixed | 261 nm AlCl endpoint wavelength unsupported by cited source (125-mm2e + cross-page categories/etch.md:164) — commit 3ff9b57 |
| 125-L3 | Low | fixed | unsupported "newer" claim about 2300 platform (125-mm2e.md:163-166) — commit 3ff9b57 |
| 126-L1 | Low | fixed | "still calls" wording for a 2009 press release (126-nild4.md:77-78) — commit 0a6b10a |
| 129-L1 | Low | fixed | via2/via resistance "consistent with larger area" ignores depth (129-vim2, 130-vim2e) — commit 0a6b10a |
| 129-L2 | Low | fixed | i-line NA cross-referenced to page that doesn't give it (129-vim2.md:62-64) — commit 0a6b10a |
| 132-L1 | Low | fixed | "near-ideal" overstates PNL patent claim (132-wdep4.md:71-75; also found+fixed the same overstatement on 110-wdep2.md) — commit a13fce1 |

## Site-wide items from the review (NOT this branch's findings)

| item | status | note |
|---|---|---|
| A: `[^job-01]` job-listing citation | left alone | per coordinator instruction — separate site-wide sweep |
| B: GaSonics/Aspen spelling split | left alone | per coordinator instruction — separate site-wide sweep |
| C: `[^amat-endura]` 403 / Wayback copy not in footnote | left alone | tabled by reviewer alongside A/B as a site-wide item, not assigned to this branch; not itemized as a finding by the reviewer |

## Site-wide sweeps required by this branch's brief

The coordinator asked: when the "wider" via claim, the solvent/wet-bench
attribution, or the step-name ordinal soft form recur elsewhere in
`docs/` (e.g. on 135-163), grep the whole tree and fix every occurrence.

| pattern | status | note |
|---|---|---|
| "wider" via/contact-vs-via miscomparison | done | found and fixed one more instance, 119-vime.md:70 (mcon vs via) — commit b4f1068 |
| solvent wrongly attributed to "wet bench" / EKS265/EKC270 | done | found and fixed four more instances outside 118-134: 108-ctme.md, 114-mm1e.md, 138-capme.md, 140-mm3e.md — commit 5a806bb |
| step-name ordinal soft form ("the digit/suffix makes it the Nth") | done | grepped whole docs/ tree beyond 122, no other occurrence found — commit 4904894 |

## Extra recurrences found and fixed beyond the review's listed sites

While applying findings, grepped for each error's exact pattern and
fixed additional occurrences the review didn't list (all same class of
error as the parent finding, not new independent findings):

* "wider" via-vs-contact miscomparison: 119-vime.md:70 (mcon vs via).
* EKS265/EKC270 "wet-bench list" misattribution: 108-ctme.md,
  114-mm1e.md, 138-capme.md, 140-mm3e.md.
* UMC dual-damascene patent scope (119-L1): 145-vim3e.md, 147-wdep5.md.
* "near-ideal" PNL patent overstatement (132-L1): 110-wdep2.md.

## Verifier follow-ups (tmp/p4/verify-118-134.md), applied after rebase

`main` advanced to `8f99ba3` (107-117 merged) while this branch was in
flight; verifier flagged 4 items, all now done:

1. Rebased onto `main`. Conflicts in `110-wdep2.md` (kept both main's
   silane sentence and this branch's "improved step coverage" fix),
   `123-tial12.md` and `134-wtial3.md` (dropped this branch's 123-L1
   paraphrase, kept main's verbatim Cypress quotation from its commit
   `91182ef` — main resolved the same finding the other way and had
   already applied it repo-wide, so its resolution wins).
2. `114-mm1e.md:121-124` — dropped the unsourced "near 261 nm", adopted
   `125-mm2e.md:123-126`'s wording — commit 9be659e.
3. Brought the other six `[^pat-cmp-ibm-1990]` definitions
   (090-cmpp.md, 106-cmpl.md, 111-wcmp2.md, 116-cmpm.md, 148-wcmp5.md,
   categories/cmp.md) and the `references/public-sources.md` inventory
   entry to "filed 1985-10-28, granted 1990-07-31" — commit 2466122.
4. Did not push (coordinator merges the local branch directly after a
   rebase; a push would need `--force`).

Not done: verifier's optional item 5 (dangling-clause tidy at
108-ctme.md/114-mm1e.md) — not in the coordinator's list of required
items for this pass.

## Checkers / build

All run from the worktree in the foreground, all pass:

* `uv run python tools/check_steps.py` — 171 pages, 171 written, 0 stubs, 0 missing headings
* `uv run python tools/check_refs.py` — 264 written pages checked, 0 with problems
* `uv run python tools/check_machines.py` — 30 machine pages checked, 0 problems
* `uv run python tools/check_materials.py` — 12 material pages checked, 0 problems
* `uv run python tools/check_masks.py` — 36 mask pages checked, 0 problems
* `uv run python tools/check_papers.py` — 49 papers checked, 0 problems
* `uv run python tools/gen_papers.py --check` — 8 pages checked, 0 problems
* `uv run sphinx-build -W -q -b html docs tmp/build-topic-p4-118-134` — exit 0, no warnings

Work on this branch is complete: all 18 findings from the review
addressed (17 fixed, 1 declined as handled elsewhere), plus the three
mandatory site-wide sweeps and four incidental recurrences found and
fixed along the way (see above).
