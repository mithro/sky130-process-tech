# Progress — topic/p4-089-106 (Phase 4 fixes, steps 089–106)

Applying `tmp/p4/review-089-106.md` (33 distinct finding ids: 0 High,
12 Medium, 21 Low; 3 of the Medium ids are the repo-wide `[^job-01]`
sweep item, left alone per the coordinator's instructions — a separate
site-wide sweep under Common rule 11 handles it). Each finding is
independently verified against the cited public source (or by redoing
the arithmetic/cross-page check) before being fixed or declined.

| id | severity | status | note |
|---|---|---|---|
| 090-M1 | Medium (job-01) | left alone | Site-wide sweep item per coordinator instructions; not touched. |
| 100-M1 | Medium (job-01) | left alone | Same as 090-M1. |
| 106-M1 | Medium (job-01) | left alone | Same as 090-M1. |
| 089-M1 | Medium | fixed | Confirmed pdk-assumptions.txt: oxide spacer (SpThickn) = 0.05 um, poly 0.18 um + cap 0.2 um = 0.38 um capped gate. 0.38 minus two 0.05 um spacers leaves ~0.28 um narrowed gap against 0.21 um poly.2 pitch -- narrowed aspect ratio is well above 2:1, not "approaches 2:1". Reworded per review's required fix. |
| 092-M1 | Medium | fixed | Confirmed ag-8108.txt: the AG Associates Heatpulse 8800 spec section (line 257-258) gives 100/150 C per second, not the 1-180 C/s the page attributed to the 8800; that figure is the 8108's (line 129). Reported both documents' figures per the brief's disagreement rule. Same fix applied to 098 (098-L3). |
| 092-M2 | Medium | fixed | 700-800C/tens-of-minutes furnace densification carried no citation; attached [^txt-02] (Wolf & Tauber, already used on the page for the same topic at line 58/232) as a typical-value reference. |
| 093-M1 | Medium | fixed | Confirmed pdk-periphery.txt via.1a = 0.150 um (drawn smaller than licon1's 0.17 um), and 107-ctm1.md's 0.09 um mcon bottom CD vs licon's 0.08 um. Reworded the superlative to be about the etched bottom, not the drawn feature. |
| 094-M1 | Medium | fixed | Redid the arithmetic: 10 deg sidewall over 0.5 um ILD closes ~0.18 um (more than the whole 0.17 um opening); the published 0.17->0.08 um narrowing over 0.5 um is ~5 deg. Reworded to state both numbers without claiming they reconcile at the full depth. |
| 094-M2 | Medium | fixed | Confirmed US6376262.txt monitors CN at 387 nm, not CO at 483 nm; the 483 nm CO figure had no citation at all. Cited it to nojiri-2015 as industry practice/typical value and kept the patent citation only for the CN/387 nm claim it actually supports. |
| 096-M1 | Medium | fixed | Confirmed wiki-fg.txt:85 says only "typical forming gas formulations (5% H2 in N2) are not explosive" -- no percentage limit, and H2/N2 mixtures cannot burn without an oxidiser, so "4% flammability limit in nitrogen" was both uncited and not a meaningful quantity. Reworded around the cited 5% figure and the air-exposure risk.
| 103-M1 | Medium | open | |
| 105-M1 | Medium | open | |
| 089-L1 | Low | fixed | Confirmed skw-facilities.txt:109 sub-bullet "high aspect (5:1) fill capability" under the HDP entry (105-nild2.md already quotes it). Added the same quotation to 089. |
| 090-L1 | Low | open | |
| 090-L2 | Low | open | duplicate of 091-L1 (repo-wide pdk-08 parenthetical); tracked there |
| 091-L1 | Low | open | |
| 091-L2 | Low | open | duplicate of 105-L1 |
| 092-L1 | Low | fixed | Confirmed ag-8800.txt lines 44-48 list "Glass re-flow" alongside "Implant annealing" and "Silicide formation and annealing" among the 8800's applications; added "Glass re-flow" to the quoted list. |
| 093-L1 | Low | fixed | Confirmed pdk-periphery.txt:1409-1411 continues the licon.16 quotation with ", including the diff/tap straddling areaid:ce. Rule exempted inside UHVI."; added the elision marker. |
| 093-L2 | Low | fixed | Confirmed pdk-rcx.txt Table 91 heads its column "Resistivity (mohms/sq)"; reworded the 15 Ohm/contact reading as an explicit reading of that column on 093, 098 and 099. |
| 094-L1 | Low | declined | No rename needed: after the 094-M2 fix, pat-cn-tel is used only for the CN/387 nm claim it supports, so the label is consistent (review said no action needed once M2 is fixed). |
| 095-L1 | Low | fixed | Confirmed the two fragments are separate sentences ~120 lines apart in categories/etch.md (:26 general wet-etch statement, :147-148 the SACETCH-specific inference). Split into two separately-quoted sentences. |
| 095-L2 | Low | fixed | Reading 3 leaned on the word "sacrificial" in its own heading; reworded to justify it by the gap in the sequence (resist/BARC removal has no other placed step) instead. |
| 098-L1 | Low | fixed | Unified the two RTA-temperature mentions on 098 (600-700 vs 600-750) at 600-750 (the wider, safer range), same citations. |
| 098-L2 | Low | fixed | Added [^txt-01] (already used site-wide for this figure, e.g. 099-wdep.md) and a cross-reference to step-099 for the 400-450C tungsten deposition temperature. |
| 098-L3 | Low | fixed | Fixed together with 092-M1: dropped the ramp-rate clause on 098 (a silicide soak is not ramp-limited) and kept only the 400-1200C range and "Silicide formation and annealing". |
| 099-L1 | Low | fixed | Confirmed pi-US6635965.txt abstract has no hyphen ("tungsten containing gases"); removed the added hyphen. |
| 100-L1 | Low | open | duplicate of 090-L1 |
| 101-L1 | Low | fixed | Confirmed pdk-assumptions.txt:993-995: LIRESCD ("Li resistor width...", 0.29 um) sits in the Table 4 "Other" physical-criteria section, not the minimum-CD table. Named the correct table and added the matching li.7 periphery value (0.290 um). |
| 103-L1 | Low | open | |
| 103-L2 | Low | open | |
| 105-L1 | Low | open | duplicate of 091-L2; fixed together |
| 106-L1 | Low | open | duplicate of 090-L1 |
