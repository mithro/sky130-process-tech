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
| 093-M1 | Medium | open | |
| 094-M1 | Medium | open | |
| 094-M2 | Medium | open | |
| 096-M1 | Medium | open | |
| 103-M1 | Medium | open | |
| 105-M1 | Medium | open | |
| 089-L1 | Low | fixed | Confirmed skw-facilities.txt:109 sub-bullet "high aspect (5:1) fill capability" under the HDP entry (105-nild2.md already quotes it). Added the same quotation to 089. |
| 090-L1 | Low | open | |
| 090-L2 | Low | open | duplicate of 091-L1 (repo-wide pdk-08 parenthetical); tracked there |
| 091-L1 | Low | open | |
| 091-L2 | Low | open | duplicate of 105-L1 |
| 092-L1 | Low | fixed | Confirmed ag-8800.txt lines 44-48 list "Glass re-flow" alongside "Implant annealing" and "Silicide formation and annealing" among the 8800's applications; added "Glass re-flow" to the quoted list. |
| 093-L1 | Low | open | |
| 093-L2 | Low | open | |
| 094-L1 | Low | open | recorded as no-op pending 094-M2 fix |
| 095-L1 | Low | open | |
| 095-L2 | Low | open | |
| 098-L1 | Low | fixed | Unified the two RTA-temperature mentions on 098 (600-700 vs 600-750) at 600-750 (the wider, safer range), same citations. |
| 098-L2 | Low | fixed | Added [^txt-01] (already used site-wide for this figure, e.g. 099-wdep.md) and a cross-reference to step-099 for the 400-450C tungsten deposition temperature. |
| 098-L3 | Low | fixed | Fixed together with 092-M1: dropped the ramp-rate clause on 098 (a silicide soak is not ramp-limited) and kept only the 400-1200C range and "Silicide formation and annealing". |
| 099-L1 | Low | open | |
| 100-L1 | Low | open | duplicate of 090-L1 |
| 101-L1 | Low | open | |
| 103-L1 | Low | open | |
| 103-L2 | Low | open | |
| 105-L1 | Low | open | duplicate of 091-L2; fixed together |
| 106-L1 | Low | open | duplicate of 090-L1 |
