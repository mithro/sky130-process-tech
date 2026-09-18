# Progress — topic/p4-064-075 (Phase 4 fixes, steps 064–075)

Applying `tmp/p4/review-064-075.md` (32 distinct finding ids: 1 High,
9 Medium, 22 Low). Each finding is independently verified against the
cited public source (or by redoing the arithmetic/cross-page check)
before being fixed or declined.

| id | severity | status | note |
|---|---|---|---|
| 065-H1 | High | fixed | Confirmed via itrs-fep.txt: the 2001 column's MPU physical gate length is 65 nm, note [G] gives Xj = 0.55 x physical gate length; applied to SKY130's 0.15 um drawn gate that gives ~80 nm, not the tabulated 27-45 nm. Reworded the Energy bullet. |
| 064-M1 | Medium | open | |
| 065-M1 | Medium | fixed | Confirmed wiki-implant.txt gives no arsenic dose threshold (only a yttrium/sapphire example). Cited the threshold to txt-01/rev-05 as a typical value, kept the quotation on wiki-implant. |
| 065-M2 | Medium | fixed | Confirmed pdk-assumptions.html Table 5 column is headed "Vertical Space", not "lateral"; the reading is supported by the JCTD/LD row but was unmarked. Applied the marked formulation on 065-asti.md (both instances) and 075-tiprtad.md; 064-ntm.md already states it neutrally. |
| 066-M1 | Medium | open | |
| 068-M1 | Medium | open | |
| 068-M2 | Medium | open | |
| 069-M1 | Medium | open | |
| 072-M1 | Medium | fixed | Same defect as 065-M1 (wiki-implant has no arsenic dose number); applied the same fix on 072-ldasti.md. |
| 075-M1 | Medium | fixed | Same ITRS node mismatch as 065-H1 (65 nm-gate 2001 column vs SKY130's 0.15 um gate); reworded the Junction position bullet with the same 0.55x rule and ~80 nm figure. |
| 064-L1 | Low | open | |
| 064-L2 | Low | open | |
| 064-L3 | Low | open | |
| 065-L1 | Low | open | |
| 065-L2 | Low | open | |
| 065-L3 | Low | open | |
| 065-L4 | Low | open | |
| 066-L1 | Low | open | |
| 066-L2 | Low | open | |
| 066-L3 | Low | open | |
| 067-L1 | Low | open | |
| 067-L2 | Low | open | |
| 067-L3 | Low | open | |
| 068-L1 | Low | open | |
| 069-L1 | Low | open | |
| 070-L1 | Low | open | |
| 070-L2 | Low | open | |
| 071-L1 | Low | open | |
| 071-L2 | Low | open | |
| 073-L1 | Low | open | |
| 073-L2 | Low | open | |
| 075-L1 | Low | open | |
