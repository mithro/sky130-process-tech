# Progress — topic/p4-064-075 (Phase 4 fixes, steps 064–075)

Applying `tmp/p4/review-064-075.md` (32 distinct finding ids: 1 High,
9 Medium, 22 Low). Each finding is independently verified against the
cited public source (or by redoing the arithmetic/cross-page check)
before being fixed or declined.

| id | severity | status | note |
|---|---|---|---|
| 065-H1 | High | fixed | Confirmed via itrs-fep.txt: the 2001 column's MPU physical gate length is 65 nm, note [G] gives Xj = 0.55 x physical gate length; applied to SKY130's 0.15 um drawn gate that gives ~80 nm, not the tabulated 27-45 nm. Reworded the Energy bullet. |
| 064-M1 | Medium | fixed | Confirmed pdk-assumptions.txt 915-917: pseudoShadowing has no name/description tying it to NTM, unlike its four tip-named neighbours. Marked the connection as a reading. |
| 065-M1 | Medium | fixed | Confirmed wiki-implant.txt gives no arsenic dose threshold (only a yttrium/sapphire example). Cited the threshold to txt-01/rev-05 as a typical value, kept the quotation on wiki-implant. |
| 065-M2 | Medium | fixed | Confirmed pdk-assumptions.html Table 5 column is headed "Vertical Space", not "lateral"; the reading is supported by the JCTD/LD row but was unmarked. Applied the marked formulation on 065-asti.md (both instances) and 075-tiprtad.md; 064-ntm.md already states it neutrally. |
| 066-M1 | Medium | fixed | Confirmed pdk-assumptions.txt 780-801 publishes only three implant angles (HCIMPA 0, TipAng 7, HvTipAngle 40/HvTipTwist 23); at least four other implant pages in range say their SKY130 angle is not public. Reworded to match. |
| 068-M1 | Medium | fixed | Confirmed via masks/hvntm.md's own Table F2b reading (12 of 80 rows marked C) that the "not public" open question is answered by a source the page already cites. Replaced the open question on 068 and its duplicate on 069 with the table's actual answer. |
| 068-M2 | Medium | fixed | Confirmed Table F2b also marks HVNTM for the 3.3V native NMOS, 16V DE NMOS and HV diodes/resistors/varactors, not just the plain 5V family; fixed the device list on 068 and 069, separating the 16V (created) from the 20V UHV (not created) drain-extended devices. |
| 069-M1 | Medium | fixed | Confirmed pdk-assumptions.txt 798-801 gives only the 23 deg HvTipTwist number with no explanation. Marked the twist's purpose as a reading, keeping the "we infer" clause. |
| 072-M1 | Medium | fixed | Same defect as 065-M1 (wiki-implant has no arsenic dose number); applied the same fix on 072-ldasti.md. |
| 075-M1 | Medium | fixed | Same ITRS node mismatch as 065-H1 (65 nm-gate 2001 column vs SKY130's 0.15 um gate); reworded the Junction position bullet with the same 0.55x rule and ~80 nm figure. |
| 064-L1 | Low | fixed | Confirmed OVGTTH ("poly cap after SPE", 0.2 um) is the thickness after the spacer etch (step 077), 12 steps after NTM; the cap at step 064 must be thicker. Reworded on 064 and 065. |
| 064-L2 | Low | fixed | Confirmed Table F2b marks NTM "C" on PMOS/SONOS/flash/110A NMOS rows and "-" on 1.8V NMOS rows (matches masks/ntm.md's own reading). Added the cross-check sentence. |
| 064-L3 | Low | fixed | Same ITRS node caveat as 065-H1/075-M1, applied to step 064's Why-this-step-exists paragraph. |
| 065-L1 | Low | fixed | Confirmed 088-rtad.md:17 says all three deep S/D implants leave silicon amorphised; named them instead of "one of the two". |
| 065-L2 | Low | fixed | = 064-L1, same text/fix at 065-asti.md's shadowing-arithmetic bullet. |
| 065-L3 | Low | fixed | Confirmed via Crossref that Nobili 1983 (10.1149/1.2119859) has no public abstract/paywalled text; marked the 2e20 threshold as a typical value on txt-01, kept Nobili for the precipitation mechanism. |
| 065-L4 | Low | fixed | Confirmed axcelis-8250.txt is the Semiconductor Online 8250HT page (footnote already says so); SkyWater's own 8250 listing gives no energy range. Reworded to attribute the 3 keV floor to the 8250HT variant only. |
| 066-L1 | Low | fixed | Fetched USPTO grant PDFs for US5795831, US6660603 and US5155336 (200 OK, verified valid PDFs) to add to the shared cache alongside the already-cached US6238982/US5811358/US20040214448/US8093128/US8796098; changed all eight patents.google.com footnote URLs (066,067,068,070,071,072,073,074,075) and their public-sources.md entries to image-ppubs.uspto.gov. |
| 066-L2 | Low | fixed | Confirmed cache has no .mdm files for the W=0.42um L=20/25um geometries and the cited repository listing does not identify well configuration; dropped the unverifiable parenthesis rather than naming a file that isn't in the cache. |
| 066-L3 | Low | fixed | Confirmed axcelis-8250.txt (the 8250HT page) says the 8250 platform serves "indium implants"; reworded so the claim is about SkyWater's published list, not the tool's capability. |
| 067-L1 | Low | fixed | Confirmed wb-US5811358.txt 134 reads "(<220° C.)"; fixed the re-typeset instances on 067 and 070 (074 already had it right). |
| 067-L2 | Low | fixed | Confirmed 062-p1me.md:22,159 strips the gate-etch resist in-situ inside P1ME. Reworded to "first stand-alone resist strip". |
| 067-L3 | Low | fixed | Re-verified: Indeed URL still returns HTTP 403 (2026-09-18) to our own fetch; Wayback availability API and archive.ph show no snapshot (rate-limited/empty). Brought the footnote definitions on 067/070/074 in line with the inventory's existing 403 note; kept the quotation, which is a retrieved-and-dated public page per common rule 2. |
| 068-L1 | Low | fixed | Confirmed pdk-background.txt 316 says only "developed by Cypress Semiconductor", no "S8" name. Removed the unsupported name attribution, kept the lineage claim on pdk-02. |
| 069-L1 | Low | fixed | Confirmed Lee 1996 (Crossref) is titled "Thick photoresist outgassing during MeV implantation", the opposite resist thickness/energy regime from HVASTI's 0.3 um / tens-of-keV. Reworded as a scaling inference. |
| 070-L1 | Low | fixed | = 067-L1, fixed together with the 066-L1/067-L1 patent-URL and typography commit. |
| 070-L2 | Low | fixed | Confirmed PDK gives the 0.02 um value with no explanation of consequence; marked the "damaged through" reading as an inference, matching 068's more careful treatment. |
| 071-L1 | Low | fixed | Confirmed Table F2b (parsed) marks LDNTM on 9 rows including "NV SONOS Diode", matching masks/ldntm.md; added the missing row to 071's list. |
| 071-L2 | Low | fixed | Confirmed pdk-device-details.txt 2749-2757 prints V_S as "-38"; added the reviewer's caveat noting the evident typo and our reading. |
| 073-L1 | Low | open | |
| 073-L2 | Low | open | |
| 075-L1 | Low | open | |
