# Progress — topic/p4-014-034 (Phase 4 fixes, steps 014–034)

Applying `tmp/p4/review-014-034.md` (23 findings: 0 High, 9 Medium, 14 Low).
Each finding was independently verified against the cited public source (or
by redoing the arithmetic/cross-page check) before being fixed; all 23 were
confirmed correct, so none are declined.

| id | severity | status | note |
|---|---|---|---|
| 014-M1 | Medium | fixed | BARC wavelength-ratio claim was wrong (380/365=1.04, not >2×; the 0.76 µm pitch is 2.08×). Wikipedia's cited BARC passage doesn't state a ratio criterion either. Reused step 022's correct wording. |
| 014-L1 | Low | fixed | Added the LVTNM mask-derivation cross-reference to Open questions (verified against `docs/masks/index.md`/`docs/masks/lvtnm.md`). |
| 015-L1 | Low | fixed | LSI patent (US 5,963,801, text confirmed): "50 and 100 keV" is real but the implant is post-well-anneal through a fresh 200–500 Å sacrificial oxide, not "tens of keV" through a pad oxide. Reworded and added the placement caveat. |
| 016-M1 | Medium | fixed | Steps 018/019/020 = three implants (NWI, NWI2, LVTPI), not four. Fixed the count. |
| 017-M1 | Medium | fixed | Periphery dnwell.2/dnwell.3 = 3.000/6.300 µm (confirmed in `pdk-periphery.txt`) are stricter than nwell.1/nwell.2a 0.840/1.270 µm; NWM's rules are not the loosest front-end layer, only among the loosest. |
| 018-M1 | Medium | fixed | IBM US 6,667,205 quote (text confirmed) was truncated, dropping "of the parasitic device formed by the Well" and inverting the sense; restored and moved to the Latch-up bullet. |
| 018-M2 | Medium | fixed | UMC US 5,393,679 (text confirmed) never mentions an implanter class; reworded the "medium-current tool" claim as our own reading, in body text and Deep dive. |
| 018-L1 | Low | fixed | Test-tile module adjacency ("beside") was wrong: confirmed in `testtile-pads.csv` that the isolation module (7018), Nwell-Psub diode (5208) and n-well resistor row are in different modules, not adjacent. |
| 019-L1 | Low | fixed | Same UMC misattribution as 018-M2, fixed in the Deep dive entry. |
| 020-M1 | Medium | fixed | Unsourced −1.2 V estimate; attached the page's existing [^taur-2009] textbook citation and said what is estimated. |
| 020-L1 | Low | fixed | IBM US 6,667,205 (text confirmed): the 50 keV implant is "low dose implant 16A", the shallowest N-well member; reworded to cite the actual supporting sentence ("a further optional implant to more precisely control dopant levels"). |
| 020-L2 | Low | fixed | Cross-page conflict X2 (HVTPM opening reading): added a hedge sentence and an Open questions entry pointing to step 022's second reading. |
| 021-M1 | Medium | fixed | Cross-checked against `docs/steps/007-dnm.md` (same 2–3 µm resist class) and `docs/steps/008-dni.md` (higher-energy DNI implant); the "thickest so far" / "longest cumulative time" claims didn't hold. Replaced with "as thick as any" and the number-of-implants argument. |
| 021-L1 | Low | fixed | Cumulative-ion-time claim marked as an inference, tied to the implant count rather than an unsupported dose/time claim. |
| 023-M1 | Medium | fixed | chvtpm.3 rule (confirmed in `errors.csv`) and render expression (confirmed in `docs/masks/index.md`) support step 022's second reading; added the hedge and an Open questions entry to step 023. |
| 024-L1 | Low | fixed | Part of X2; added the scoping sentence to "Why this step exists". |
| 025-L1 | Low | fixed | Reworded so the industry-typical 200–270 °C figure no longer reads as corroborated by SkyWater's published asher ranges. |
| 026-L1 | Low | fixed | pwde (gds_layers.csv 124:20) vs pwdem.dg (periphery rule text, confirmed in `pdk-periphery.txt`) naming mismatch recorded on both step 026 and step 030 (X5). |
| 027-L1 | Low | fixed (no edit) | Evidence note only — reviewer's own conclusion is "no change required" (US 7,605,041 confirmed image-only scan: only the bibliographic first page extracts). Verified and left as-is. |
| 028-L1 | Low | fixed | LSI US 5,963,801 (text confirmed): punch-through barrier 24 is formed "in the n-Well 18" (100/70/50 keV chain), a counter-doped PMOS barrier, not a P-well example; corrected the polarity note. |
| 030-L1 | Low | fixed | PDK hv.html (confirmed): 11V/16V NMOS vs 10V/16V PMOS, not "10/16 V" for both. Also added the pwde/pwdem naming note (X5, paired with 026-L1). |
| 034-M1 | Medium | fixed | SemiStar `ag8108.txt` (confirmed): the 8108 section's ±5 °C uniformity spec is over an 8-inch (200 mm) wafer; "150 mm" belongs to the 4100 section. Fixed and added the 4100's own wafer size for contrast. |
| 034-L1 | Low | fixed | Hynix US 6,455,402 (text confirmed) quote dropped "or CVD (Chemical Vapor Deposition) method"; restored with an ellipsis. |

## Checkers and build

All run from the worktree in the foreground before finishing:
`check_steps.py`, `check_refs.py`, `check_machines.py`,
`check_materials.py`, `check_masks.py`, `check_papers.py`,
`gen_papers.py --check`, and `sphinx-build -W -q -b html`.
