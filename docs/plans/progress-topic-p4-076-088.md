# Progress — topic/p4-076-088 (Phase 4 fixes, steps 076–088)

Applying `tmp/p4/review-076-088.md` (16 distinct finding ids: 1 High,
4 Medium, 11 Low, plus one repository-wide job-listing item under
Common rule 11 left to the site-wide sweep). Each finding is
independently verified against the cited public source (or by redoing
the arithmetic/cross-page check) before being fixed or declined.

| id | severity | status | note |
|---|---|---|---|
| 079-H1 | High | fixed | Confirmed via Crossref abstract of 10.1116/1.582097: Kastenmeier 1999 gets nitride-to-poly selectivity from a remote O2/N2 discharge growing a ~10 nm oxidised layer on the poly, not from "high carbon-to-fluorine ratio" or "O2-lean" RIE chemistry (absent from the paper). Reworded 079-npcme.md's "Stop on poly" bullet to attribute the RIE practice to the category page and describe Kastenmeier's actual downstream-reactor mechanism separately. |
| 076-M1 | Medium | fixed | Confirmed pdk-assumptions.txt 819-821: OVGTTH "poly cap after SPE" = 0.2 um is the thickness that survives the spacer etch at step 077, which is after step 076. Grepped docs/ for the "0.4 um" gate-height phrase: the five later uses (078, 081, 082, 083, 086) are all after step 077 and correct; only 076's two uses (pre-SPE) were wrong. Reworded both on 076-spnit.md to say the cap is "no thinner than" the post-SPE 0.2 um figure. |
| 076-M2 | Medium | fixed | Confirmed via Crossref abstract of 10.1116/1.581302: Temple-Boyer et al. 1998 studies silane/ammonia LPCVD SiNx (not the DCS/ammonia film the bullet describes) and reports ~600 MPa for its lowest-stress condition, not ~1 GPa. Reworded: the ~1 GPa figure now cites wiki-sin/txt-02, matching how the category page sources it, and Temple-Boyer is described accurately as a separate silane/ammonia measurement giving ~600 MPa. |
| 076-M3 | Medium | fixed | Confirmed itrs-fep.txt line ~1460: "Sidewall spacer thickness (nm) extension structure [K] 48-95" for the 2001 technology year, note [K] equates spacer width to contact junction depth; the key itrs-01 is already in the inventory (used on 064-ntm.md for the same table). Appended the cross-check to 076's Thickness bullet with the same "our reading of the roadmap" hedge 064 uses, and added itrs-01 to 076's footnote definitions and Deep dive list. |
| 086-M1 | Medium | fixed | Independently re-fit the raw .mdm sweep (least-squares, through-origin and endpoint methods, all agreeing to <0.01%): 3071.18 ohm / 25.06 sq = 122.55 ohm/sq (file matches text) and 3015.65 ohm / 25.0 sq = 120.63 ohm/sq, not 120.7. Fixed "120.7" to "120.6" on 086-nsdi.md; grepped docs/ for the figure, no other occurrence. |
| 076-L1 | Low | fixed | Confirmed via Crossref (10.1149/1.1690294): no abstract available (IOP paywalled/bot-checked as the review found), title confirms only "Low-Temperature ... LPCVD"; no explicit temperature number. Labelled the 550-600 C range as a typical industry value per the review's proposed wording. |
| 076-L2 | Low | fixed | Confirmed docs/categories/deposition.md gives 250-400 C with wiki-pecvd for PECVD; smith-1990/claassen-1985 have no Crossref abstracts to support 300-400 C. Matched the category page's range and citation. |
| 077-L1 | Low | fixed | Confirmed both DOIs (10.1116/1.580203, 10.1116/1.582097, checked for 079-H1) are downstream/remote-plasma studies, cited inside a bullet describing the ion-driven RIE main etch. Added the review's parenthetical clarifying they describe the chemistry, not the RIE tool used here. |
| 079-L1 | Low | declined | Confirmed skw-facilities.txt reads "Gasonic PEP"/"Mattson Aspen2" and the repo has a real, pre-existing split (38x "GaSonics PEP" vs 34x "Gasonic PEP"; 31x "Aspen2" vs 57x "Aspen II"). Not a factual error on this page (corporate name is GaSonics International); the review itself concludes "no change is strictly required" and asks the coordinator to settle the repo-wide spelling once. Declining a page-local fix that would leave the branch inconsistent with the rest of the site; left for the coordinator's site-wide pass. |
| 080-L1 | Low | fixed | Confirmed via Crossref (10.1116/1.586361): Raupp's abstract gives trends with temperature/pressure/power but no absolute window. Matched the category page's sourced 250-400 C, wiki-pecvd. |
| 080-L2 | Low | fixed | Confirmed page's own reading (lines 14-27): SPOX is deposited over the SPNIT/SPE nitride spacer as an additional composite layer, not a replacement; "instead of nitride" wrongly implied substitution. Reworded to "the extra spacer width added here is oxide rather than more nitride". |
| 082-L1 | Low | fixed | Confirmed via Crossref (10.1063/1.96079): Smith 1985's abstract says "high sensitivity even at low dose", supporting a low-dose use, not a high-dose limitation as unsourced. Reworded as an inference citing Smith (added footnote def + Deep dive entry, already used the same way on 083-2psdi.md). |
| 083-L1 | Low | fixed | Confirmed pdk-assumptions.txt gives PrThickImplant=0.3 and PRTHICKN=1.14 with no stated rationale for either. The causal "which is why" was this reference's own reading, not the PDK's; reworded as "we read ... as a response to that, though the PDK does not say so", matching the mask-page brief's rule on design-rule purposes. |
| 084-L1 | Low | fixed | Confirmed wiki-piranha.txt gives no percentage for the sulfuric acid, only "concentrated sulfuric acid" and "30 wt.% hydrogen peroxide"; 96-98% is unsourced. Fixed 084-pdis.md per the review's wording, and the same unsourced pair on docs/categories/strip.md (the shared strip category page, in my range's citation list) to keep it sourced. Grepped further: 016-lvtnis.md and 067-astis.md have the identical unsourced text but are outside steps 076-088 and outside this review; left untouched as out of scope for this branch. |
| 087-L1 | Low | declined | Confirmed page already does both correctly (verbatim quotations vs normalised prose); the review itself says "no change is needed" here and asks the coordinator to settle the repo-wide spelling split once, same as 079-L1. |
| 088-L1 | Low | fixed | Confirmed docs/categories/anneal.md:58-59 gives the "800-1000 C" statement unquoted with [^gibbons-1972][^txt-01], not as a quotation. Dropped the quotation marks here (txt-01 already defined on this page) so it doesn't read as Gibbons's own words. |
| job-01 (rule 11) | — | left alone | Per coordinator instruction: a separate site-wide sweep under Common rule 11 handles `[^job-01]` everywhere; not touched in this branch. |

## Verifier follow-ups (tmp/p4/verify-076-088.md)

| id | status | note |
|---|---|---|
| verify-1 | fixed | Re-confirmed via Crossref abstract of 10.1116/1.582097: with NF3, Kastenmeier 1999 reports a nitride-to-oxide ratio of ~70, not "not etched at all" (that phrase applies only to the CF4 process, where SiO2 is not etched at all). Fixed 079-npcme.md:131-132 to state both cases correctly. |
| verify-2 | fixed | Fetched the Gumpher 2004 abstract myself via OpenAlex (api.openalex.org/works/doi:10.1149/1.1690294), since Crossref carries none and IOP bot-blocks direct fetches: confirms 550-600 C, 200 mm vertical batch furnace, 4-30 A/min deposition rate. Replaced the "typical industry value" hedge (which also wrongly said the paper's title confirms only "low-temperature") with the sourced figures on 076-spnit.md. |
| verify-3 (084-L1 sweep) | fixed | Coordinator-authorized, out-of-range: applied the same unsourced-96-98%-acid fix to docs/steps/067-astis.md (wiki-piranha already defined there) and docs/steps/016-lvtnis.md (added the wiki-piranha footnote definition; that page previously mis-cited wiki-rca for the SPM claim). Text matches 084-pdis.md's wording exactly. |

## Final status

All 16 findings resolved: 1 High fixed, 4 Medium fixed, 9 Low fixed,
2 Low declined (079-L1, 087-L1 — repo-wide vendor-spelling split,
matching the review's own "no change required" conclusion; left for
the coordinator's site-wide pass). `[^job-01]` left untouched per
instruction. One out-of-range gap noted but not fixed: 016-lvtnis.md
and 067-astis.md carry the same unsourced "96-98%" sulfuric acid
figure as 084-L1 but are outside steps 076-088 and this review.

Checkers run in the foreground from the worktree, all passing:
`check_steps.py` (171 pages, 0 problems), `check_refs.py` (264, 0),
`check_machines.py` (30, 0), `check_materials.py` (12, 0),
`check_masks.py` (36, 0), `check_papers.py` (49, 0),
`gen_papers.py --check` (8, 0), and
`sphinx-build -W -q -b html docs tmp/build-topic-p4-076-088` (clean,
no warnings/errors).

Rebased onto main (2026-09-19) after the verifier's follow-up report;
addressed all three requested items (verify-1, verify-2, verify-3
above); re-ran every checker and the build after rebasing and after
the follow-up fixes — all clean.
