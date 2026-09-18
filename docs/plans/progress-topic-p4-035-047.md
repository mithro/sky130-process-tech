# Progress: fixing the Phase 4 final review (steps 035-047) on `topic/p4-035-047`

Source: `tmp/p4/review-035-047.md` (independent sub-agent review, not
tracked in the repository). Work High first, then Medium, then Low.
Each finding is verified against the public source (fetch cache under
`tmp/p4/fetch/`, reused where already present) or by redoing the
arithmetic before being fixed or declined.

| Finding | Page(s) | Status | Note |
|---|---|---|---|
| 038-H1 | 038-depi.md | fixed | PDK "VT meas" row misread — gate is swept, not held at 0 V; verified against `pdk-device-details.txt` (V_G swept, V_D +1.1, V_B 0, V_S 0, V_WL +1.8) |
| 035-M1 | 035-tunm.md | fixed | Cypress quotation put inside a PDK attribution |
| 036-M1 | 036-tunarce.md | fixed | replaced uncited "few nm resist loss" with the ARC-thickness+overetch statement the page's own Selectivity section already supports |
| 036-M2 | 036-tunarce.md | fixed | widened to "tens to several hundred keV", citing PTSI/DEPI |
| 037-M1 | 037-ptsi.md | fixed | original/star cell W/L pairing stated as fact |
| 037-M2 | 037-ptsi.md | fixed | `lvtn` block reading overstated vs step 015 |
| 038-M1 | 038-depi.md | fixed | 20 V zero-Vt structure identification untraced |
| 038-M2 | 038-depi.md | fixed | arsenic inference not carried into later bullets |
| 040-M1 | 040-ono.md, 039-tunme.md | fixed | 1.5-3 nm tunnel oxide misattributed to pat-04 |
| 040-M2 | 040-ono.md | fixed | "thinnest oxide in the flow" asserted, not shown |
| 041-M1 | 041-onom.md | fixed | ONOM-from-tunm-by-oversizing inference overstated |
| 041-M2 | 041-onom.md | fixed | overlay-to-TUNM inference stated with mixed hedging |
| 042-M1 | 042-onome.md | fixed | 7-15 nm trapping layer merges two different quantities |
| 043-M1 | 043-gox100.md | fixed | ONO-first ordering rationale not given |
| 043-M2 | 043-gox100.md | fixed | "somewhat thinner than 11 nm" left unquantified |
| 044-M1 | 044-lvom.md | fixed | NOT-hvi inference marked once, used as fact elsewhere |
| 045-M1 | 045-nchi.md | fixed | 7 deg tilt asserted; cited analogue specifies zero tilt |
| 045-M2 | 045-nchi.md | fixed | "last channel implant" claim too strong |
| 046-M1 | 046-goxetch.md | fixed | category-page quote drops its inference marker |
| 047-M1 | 047-lvgox.md | fixed | nitridation inference marked once, used as fact elsewhere |
| 047-M2 | 047-lvgox.md | fixed | two overstated claims about oxidation control |
| 035-L1 | 035-tunm.md | fixed | quotation capitalisation |
| 035-L2 | 035-tunm.md | fixed | 5V regions are hvi, drawn complement at LVOM; re-fixed per verifier to mark the NOT-hvi complement reading as an inference (044-M1), not fact |
| 035-L3 | 035-tunm.md | fixed | tunm.3 unit not given by the table |
| 035-L4 | 035-tunm.md | fixed | job-01 no longer retrievable |
| 036-L2 | 036-tunarce.md | fixed | resolved as a side effect of the 036-M1 fix (the unsupported figure is gone) |
| 037-L1 | 037-ptsi.md | fixed | US 5,963,801 context (n-well, "merely exemplary") |
| 037-L2 | 037-ptsi.md | fixed | Axcelis indium cross-validation addition |
| 037-L3 | 037-ptsi.md, 039-tunme.md, 040-ono.md | fixed | silent typo correction in PDK table (-38 -> -3.8) |
| 038-L1 | 038-depi.md | fixed | nfet_05v0_nvt range 0.01 V narrow |
| 038-L2 | 038-depi.md | fixed | "2 nm oxide" narrower than patent range |
| 038-L3 | 038-depi.md | fixed | quotation capitalisation |
| 038-L4 | 038-depi.md | fixed | dead Springer chapter page behind live DOI |
| 039-L1 | 039-tunme.md | fixed | HF-last qualification vs later ONO precleans |
| 039-L2 | 039-tunme.md | fixed | category-page quote splices two passages |
| 039-L3 | 039-tunme.md | fixed | two numeric statements don't follow from pat-04 |
| 040-L1 | 040-ono.md | fixed | dropped word "oxide" in quotation |
| 040-L2 | 040-ono.md | fixed | pat-radox-cyp embodiment is polysilicon-channel |
| 040-L3 | 040-ono.md | fixed | furnace capability line oversold as "decisive" |
| 041-L1 | 041-onom.md | fixed | ARC-etch question left in confusing order |
| 042-L1 | 042-onome.md | fixed | DPS II suffix fixed; SNF gas list fix reverted per verifier — the Stanford page's gas list does include tetrafluoromethane, our first pass misread the cache and introduced a regression |
| 043-L1 | 043-gox100.md | fixed | dropped word "oxide" (same as 040-L1) |
| 043-L2 | 043-gox100.md | fixed | "5.0V I/O" quoted differently than step 044 |
| 044-L1 | 044-lvom.md, 045-nchi.md, 046-goxetch.md | fixed | "~10 nm" cited to finished-thickness source |
| 044-L2 | 044-lvom.md | fixed | beverina-2003 used beyond abstract |
| 045-L1 | 045-nchi.md | fixed | AMD quotation drops "zero tilt" clause (same as 045-M1) |
| 045-L2 | 045-nchi.md | fixed | corrected per verifier: "mean of the two published sweeps" was false at 7/0.15 um (5 sweeps exist there); now names the actual modules used (8008, 8392) |
| 046-L1 | 046-goxetch.md, 039-tunme.md | fixed | uncited/wider HF dilution range vs 039 |
| 046-L2 | 046-goxetch.md | fixed | resolved together with 044-L1 | "~10 nm" (same as 044-L1) |
| 047-L1 | 047-lvgox.md | fixed | "the one public hint" overstates evidence |
| 047-L2 | 047-lvgox.md | fixed | raw-data module-to-device mapping not given |

## Declined findings

| Finding | Reason |
|---|---|
| 036-L1 | The repo-wide, already-merged convention (documented at `docs/machines/downstream-plasma-asher.md:162`, "vendor 'Gasonic' ... writes 'Aspen2', which we read as the Aspen II") normalises the vendor's "Aspen2" to "Aspen II" on ~30 already-merged step and machine pages. The quoted gas-list strings on step 036 are exact; only the model name follows this repo-wide normalisation. Changing step 036 alone to the bare "Aspen2" would make it the sole outlier and fail the consistency check (Common rule 3) against every other page. Declined; no change. |
