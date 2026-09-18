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
| 125-L1 | Low | open | PDK metal-layer antenna area is perimeter not plan area (125-mm2e.md) |
| 125-L2 | Low | open | 261 nm AlCl endpoint wavelength unsupported by cited source (125-mm2e + cross-page categories/etch.md:164) |
| 125-L3 | Low | open | unsupported "newer" claim about 2300 platform (125-mm2e.md:163-166) |
| 126-L1 | Low | open | "still calls" wording for a 2009 press release (126-nild4.md:77-78) |
| 129-L1 | Low | open | via2/via resistance "consistent with larger area" ignores depth (129-vim2, 130-vim2e) |
| 129-L2 | Low | open | i-line NA cross-referenced to page that doesn't give it (129-vim2.md:62-64) |
| 132-L1 | Low | open | "near-ideal" overstates PNL patent claim (132-wdep4.md:71-75) |

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

## Checkers / build

Not yet run to completion — will run before finishing per brief step 4.
