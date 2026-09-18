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
| 077-L1 | Low | open | |
| 079-L1 | Low | open | |
| 080-L1 | Low | open | |
| 080-L2 | Low | open | |
| 082-L1 | Low | open | |
| 083-L1 | Low | open | |
| 084-L1 | Low | open | |
| 087-L1 | Low | open | |
| 088-L1 | Low | open | |
| job-01 (rule 11) | — | left alone | Per coordinator instruction: a separate site-wide sweep under Common rule 11 handles `[^job-01]` everywhere; not touched in this branch. |

Checkers/build not yet run to completion; will run before finishing.
