# Progress: fixing the paired reviews of steps 001–013 on `topic/p4-001-013`

Source reviews: `tmp/p4/review-001-013-B.md` (primary; 1 High, 7 Medium,
38 Low) and `tmp/p4/review-001-013-A.md` (2 Low only — both duplicates of
findings B already lists, so tracked against B's ids). Work order: High,
then Medium, then Low, one finding or closely-related group per commit.
Status values: open / fixed / declined.

## High

| Finding | Page(s) | Status | Note |
|---|---|---|---|
| 006-H1 | 006-stie, 089-psg, overview/index, materials/index, references/public-sources | fixed | re-derived the arithmetic myself from a fresh fetch of metal_stack.svg's raw coordinates: the two `licon` dimensions (0.6099 over diffusion, 0.4299 over the 0.18 µm field poly), both anchored to the `li`-bottom rung (0.9361), independently give diffusion top = field-oxide top = 0.3262 µm — confirms the review. Rewrote 006-stie.md's "How deep?" paragraph and Open questions (also folds in 006-L1). Fixed overview/index.md:365-366. 089-psg.md, materials/index.md and references/public-sources.md already read the labels the (correct) other way and needed no change (confirmed by re-reading them). Also updated 007-dnm.md's dependent wording (007-L2). |

## Medium

| Finding | Page(s) | Status | Note |
|---|---|---|---|
| 001-M1 | 001-smat | fixed | verified: PDK device-details page distinguishes `nfet_20v0_zvt` (p-well+Vt blocked) from `nfet_20v0_nvt` ("similar to isolated", Vt blocked); raw-data repo has no zvt folder. But `docs/steps/026-pwbm.md` and `docs/references/public-sources.md`'s RAW-DATA-HV-MOSFETS entry already resolve this: the measurement lives in the `nfet_20v0_nvt` folder but its pad geometry (2x30/5.5, `Psub` body) matches the PDK's zvt e-test structure, not nvt's (30/1.0). Fixed 001-smat.md to read it the same way as those two already-correct pages, rather than the reviewer's simpler "must be nvt" fix, which would have put 001-smat.md at odds with 026-pwbm.md and the inventory. |
| 003-M1 | 003-isonit | fixed | verified AmberWave 500-2000 Å = 50-200 nm (already fetched by both reviews and self-consistent with the page's own later quote); lower bound of the stated range didn't match; fixed and tied the 150 nm working figure explicitly to the patent's midpoint |
| 004-M1 | 004-fom | fixed | matched docs/masks/fom.md and docs/masks/index.md, which already mark this pairing "(inference)" |
| 008-M1 | 008-dni | fixed | reworded; the MeV straggle-vs-offset physics claim in the review is standard implant physics, order-of-magnitude plausible, no public SKY130 figure exists so dropped the false-precision framing |
| 009-M1 | 009-dnis | fixed | added the pat-sti-cr citation already used elsewhere on the page for this exact number |
| 011-M1 | 011-filox | fixed | tied the 1.5-2x figure explicitly to the 006/003 working figures instead of restating an inconsistent number |
| 013-M1 | 013-ns19 | declined | reviewer says the 3 A/min silicon rate and the two-sentence quote form can't be confirmed; I fetched the full abstract from OpenAlex's inverted-index (a different independent index than the reviewer used) and it reconstructs verbatim: "...silicon nitride films. The etch rate is 100 A/min. Under the same conditions deposited silicon dioxide had an etch rate of 0-25 A/min depending on the method of preparation, and elemental silicon 3 A/min." This confirms the page's quotation and the 3 A/min figure exactly; no change needed. See commit for the OpenAlex query. |

## Low

| Finding | Page(s) | Status | Note |
|---|---|---|---|
| 001-L1 (review B; = review A 001-L1) | 001-smat, references/public-sources | fixed | tried Wayback Save-Page-Now myself; SEC.gov blocks the Archive's own crawler too (capture failed, "internal error"), matching both reviews' independent finding of no snapshot; added the "(Wayback copy unavailable as of 2026-09-18)" fallback both reviews suggested, in the footnote and the inventory entry |
| 001-L2 | 001-smat | fixed | verified indeed.com returns 403 and has no Wayback snapshot by fetch; added the note |
| 001-L3 | 001-smat, 009-dnis | fixed | verified by fetch: Wikipedia says "75 or 80 °C", not a range; fixed 001-smat.md (both instances) and, since it's in this module's scope, the same wording on 009-dnis.md; 002-box.md only names the baths and needs no change (confirmed) |
| 001-L4 | 001-smat | declined | reviewer's own text calls this "defensible" and offers it as an optional style choice only; leaving as-is |
| 002-L1 | 002-box | fixed | patents.google.com bot-blocked this session; applied review's specific claim-vs-specification wording distinction as given |
| 002-L2 | 002-box, 006-stie | fixed | 006-stie.md side already done in the 006-H1 commit; added the same qualifier here |
| 002-L3 | 002-box | fixed | ties to massoud-1985, already cited on the page for exactly this point |
| 002-L4 | 002-box | fixed | page already partly read this correctly; completed the wording (nitride is doing most of the work, trenches are open) |
| 003-L1 | 003-isonit | fixed | Google Patents fetch of US 2009/0179253 was bot-blocked this session (matches the pattern both reviews report for this host); applied the review's quoted evidence (specific patent-number + verbatim phrase claims) as given, since it is checkable in principle and highly specific |
| 003-L2 | 003-isonit | fixed | marked the FOXSTEP link as our reading, not a documented relation |
| 004-L2 (review B; = review A 004-L1) | 004-fom | fixed | verified Wikipedia's BARC sentence by fetch: confirmed the "45 nm and below" clause is dropped; added the scope note and a 130 nm-era citation |
| 004-L1 (review B) | 004-fom | fixed | added the `cfom` 23:0 mask-level layer, matching masks/fom.md's own ordering |
| 004-L3 | 004-fom | fixed | verified ZeptoBars page by fetch: confirmed "likely" hedge; requoted properly |
| 004-L4 | 004-fom | fixed | added FOMCD/FOMCDSP sentence |
| 004-L5 | 004-fom, masks/index | fixed | masks/index.md:104 says 36 mask steps; "30-odd" -> "35 other" |
| 005-L1 | 005-stinite | fixed | verified by fetch (URL had moved; found via the footnote's own link) — "for selective etching of silicon and polysilicon", no design-intent claim; requoted |
| 005-L2 | 005-stinite | fixed | Thung defines the aspect-ratio formula only; split the citation |
| 005-L3 | 005-stinite | declined | reviewer's own text marks this optional ("strengthens the page") |
| 006-L1 | 006-stie | fixed | folded into the 006-H1 rewrite (ITRS "node on node" sentence dropped, Thung's 66% figure used instead) |
| 006-L2 | 006-stie | open | HDP-void quote clipped/one step removed |
| 006-L3 | 006-stie, 009-dnis | fixed | quoted SkyWater's own spellings ("Gasonic PEP", "Mattson Aspen2") in both places; same commit as 009-L1 |
| 007-L1 | 007-dnm | open | resist thickness: use patent number not book |
| 007-L2 | 007-dnm | fixed | reworded to point at STIE instead of restating a number, as part of the 006-H1 commit |
| 007-L3 | 007-dnm | open | "deliberate trade" overstated |
| 008-L1 | 008-dni | fixed | verified by fetch: prnewswire release is about GSD Ovation (2021), "3 MeV" belongs to GSD/HE Ovation specifically; reworded |
| 008-L2 | 008-dni | fixed | verified by fetch: IEEE Xplore abstract gives non-monotonic Vt-vs-dose with a peak near 1e14, not a simple "keeps dose modest" story; reworded |
| 008-L3 | 008-dni | fixed | added citations already on the page |
| 009-L1 | 009-dnis, 006-stie | fixed | see 006-L3 |
| 009-L2 | 009-dnis | fixed | added orvek-1985/smith-1983, already in the page's Deep dive |
| 010-L1 | 010-linox | open | Lattice figure is thickened 90nm-node liner |
| 010-L2 | 010-linox | open | Spansion/Cypress lineage caveat placement |
| 011-L1 | 011-filox | fixed | verified: iopscience.iop.org bot-blocks the checker's UA (302 to bot-challenge); marked numbers as unverified rather than dropped |
| 011-L2 | 011-filox | fixed | verified by fetch: Wikipedia sentence carries the unsourced-statement category tag; added nguyen-1999 on both uses |
| 011-L3 | 011-filox | fixed | quoted the 10-K's actual IMD-CVD wording so the tool isn't implied to be an STI-fill tool |
| 012-L1 | 012-cmpnit | open | slurry selectivity numbers unverifiable, mark |
| 012-L2 | 012-cmpnit | open | REB quote source describes LOCOS not STI |
| 012-L3 | 012-cmpnit | open | uncited topography figure, tie to FILOX |
| 013-L1 | 013-ns19 | fixed | verified against 058-gatenit.md's own reading; added GATENIT to the list |

## Cross-page conflicts (from B's summary, resolved as part of the above)

X1/X2 -> 006-H1; X3 -> 004-L2; X4 -> 004-M1; X5 -> 004-L5; X6 -> 006-L3/009-L1; X7 -> 003-M1; X8 -> 004-L4.
