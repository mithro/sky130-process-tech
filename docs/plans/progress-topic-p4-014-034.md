# Progress — topic/p4-014-034 (Phase 4 fixes, steps 014–034)

Applying `tmp/p4/review-014-034.md` (23 findings: 0 High, 9 Medium, 14 Low).
Each finding is independently verified against the cited public source (or by
redoing the arithmetic/cross-page check) before being fixed.

| id | severity | status | note |
|---|---|---|---|
| 014-M1 | Medium | open | BARC wavelength-ratio claim: verified wrong (380/365=1.04, not >2×; pitch 2.08× is). Wikipedia cited source doesn't support the ratio criterion. |
| 014-L1 | Low | open | Open-questions cross-ref to LVTNM mask-derivation missing. |
| 015-L1 | Low | open | LSI patent (US 5,963,801) quote verified: "50 and 100 keV" is real but implant is post-well-anneal through fresh sacrificial oxide, not "tens of keV"/pad oxide. |
| 016-M1 | Medium | open | Steps 018/019/020 = three implants (NWI, NWI2, LVTPI), not four. Verified by count. |
| 017-M1 | Medium | open | Periphery dnwell.2/dnwell.3 = 3.000/6.300 µm verified stricter than nwell.1/nwell.2a 0.840/1.270 µm claimed as "loosest". |
| 018-M1 | Medium | open | IBM US 6,667,205 quote verified truncated: drops "of the parasitic device formed by the Well", inverting the sense. |
| 018-M2 | Medium | open | UMC US 5,393,679 verified to never mention implanter class ("implanter"/"medium current"/"machine"/"equipment" all absent). |
| 018-L1 | Low | open | Test-tile module adjacency ("beside") to be verified against testtile-pads.csv module numbers. |
| 019-L1 | Low | open | Same UMC misattribution as 018-M2 (Deep dive annotation). |
| 020-M1 | Medium | open | Unsourced -1.2 V estimate; page already cites [^taur-2009] for gate work-function topic. |
| 020-L1 | Low | open | IBM US 6,667,205 verified: 50 keV implant is "low dose implant 16A", shallowest N-well member; the "more precisely control" sentence is the one that supports a channel/threshold reading. |
| 020-L2 | Low | open | Cross-page conflict X2 (HVTPM opening reading) — add pointer to step 022's alternative reading. |
| 021-M1 | Medium | open | Cross-check against 007-dnm.md / 008-dni.md resist thickness and implant energy pending. |
| 021-L1 | Low | open | Cumulative-ion-time claim needs inference marking. |
| 023-M1 | Medium | open | chvtpm.3 rule and render expression verified in errors.csv/masks index; add alternative-reading text. |
| 024-L1 | Low | open | Part of X2; add hedging sentence. |
| 025-L1 | Low | open | Reword to avoid implying the 200-270 °C book figure is corroborated by SkyWater's asher ranges. |
| 026-L1 | Low | open | pwde (gds_layers.csv 124:20) vs pwdem.dg (periphery rule text) naming mismatch verified in periphery.txt. |
| 027-L1 | Low | open | Evidence note only; reviewer says no change required (US 7,605,041 image-only scan, unverifiable). |
| 028-L1 | Low | open | LSI US 5,963,801 verified: punch-through barrier 24 formed "in the n-Well 18" (100/70/50 keV chain), not a P-well example. |
| 030-L1 | Low | open | PDK hv.html verified: 11V/16V NMOS vs 10V/16V PMOS, not "10/16 V" for both. |
| 034-M1 | Medium | open | SemiStar ag8108 PDF verified: 8108 section uniformity spec is over an 8-inch (200 mm) wafer; "150 mm" belongs to the 4100 section. |
| 034-L1 | Low | open | Hynix US 6,455,402 verified: quote drops "or CVD (Chemical Vapor Deposition) method". |

Checkers and `-W` build to run before finishing.
