# Progress — topic/p4-048-063 (Phase 4 fixes, steps 048–063)

Applying `tmp/p4/review-048-063.md` (54 distinct finding ids: 1 High,
14 Medium, 39 Low, several ids being the same root cause repeated on
more than one page). Each finding is independently verified against the
cited public source (or by redoing the arithmetic/cross-page check)
before being fixed or declined.

| id | severity | status | note |
|---|---|---|---|
| 061-H1 | High | fixed | Confirmed m1.1/m2.1/li.1a = 0.140 µm < poly.1a 0.150 µm and difftap.1 = 0.150 µm (ties) in periphery rules cache; dropped the false "smallest drawn line" superlative, kept the CD-maps-to-gate-length point. |
| 048-M1 | Medium | fixed | Confirmed 058-gatenit.md leaves LPCVD-vs-PECVD open and 060-bfr.md hedges the same way; 048 stated it as an inference without noting the open question. Fixed the cross-reference. |
| 048-M2 | Medium | fixed | Confirmed via OpenAlex: Voutsas & Hatalis 1992 shows the amorphous/poly boundary depends on deposition rate, not just temperature (as-deposited poly obtained at 530 °C by controlling rate); Kamins/Kinsbron place the conventional boundary near 600 °C. Fixed on 048, and the same oversimplified "<580 °C" claim on overview/index.md and categories/deposition.md (minimal edits, shared files). |
| 049-M1 | Medium | fixed | Confirmed via OpenAlex abstract: Wright 2010 is a sputtered Cr-Si-B-SiO2/Al2O3 thin-film resistor paper, no polysilicon. Annotated Deep dive bullets on 049/053/055 correctly; replaced 053's and 055's in-text sentences. |
| 050-M1 | Medium | fixed | Confirmed via cached facilities text: SkyWater lists 3 implanters (8250 to 1e14, GSD High current/energy to 5e15, GSD Hi dose to 5e16); the page's own Cross-check already said "three Axcelis implanters" while the body claimed the Hi-dose GSD was the only one reaching gate-doping doses. Fixed to name both GSD tools. |
| 051-M1 | Medium | fixed | Checked Wayback (`archive.org/wayback/available`, empty) and archive.today (404, no snapshot) for both job-01 and job-03 URLs on 2026-09-18: neither is retrievable or archived. Removed the quoted strings and the specific tool claim on 051/054/057/060; removed job-03 entirely (051/054/057/060 still use job-01 for other, out-of-scope pages, so its inventory key stays; job-03 became fully unused, so its inventory entry was removed). |
| 052-M1 | Medium | fixed | Confirmed via OpenAlex abstract: Tsang 2014's mechanism is hydrogen diffusing through eroded LPCVD-nitride corners (a bank-position effect), not the implant-mask edge. Fixed in-text and Deep dive on 049/052/055. |
| 053-M1 | Medium | fixed | = 049-M1 |
| 054-M1 | Medium | fixed | = 051-M1 |
| 055-M1 | Medium | fixed | = 049-M1; replaced in-text sentence with Lane & Wrixon's design space, added lane-1989 footnote. |
| 055-M2 | Medium | fixed | = 052-M1 |
| 057-M1 | Medium | fixed | Confirmed via OpenAlex: Temple-Boyer 1998 is a silane/ammonia LPCVD study giving ~600 MPa, not 1 GPa DCS nitride. Reworded on 057/058 to cite it correctly and keep 1 GPa as a typical-industry-value claim. |
| 058-M1 | Medium | fixed | = 057-M1 |
| 062-M1 | Medium | fixed | Confirmed via OpenAlex: Noguchi 1997 measured charging during a metal etch, not the poly etch. Reworded to attribute the measurement correctly and mark the poly-etch link as inference. |
| 062-M2 | Medium | fixed | Confirmed via OpenAlex: both Ogryzlo papers measure the ion-free spontaneous reaction, which the 1990 abstract itself contrasts with in-discharge (plasma) behaviour; a gate etch is strongly ion-assisted (cunge-2002, already cited). Reworded the doping-dependent clearing claim as an inference. |
| 063-M1 | Medium | fixed | Confirmed via OpenAlex: Deal 1980 standardises oxide-charge terminology, does not measure or prescribe an anneal. Kept the anneal step as a typical-industry-practice claim with its own citation. |
| 048-L1 | Low | fixed | Confirmed via cached Moov listing: verbatim "up to 200 wafer batches" (not 100-150); added citation and typical-value label. |
| 048-L2 | Low | fixed | Confirmed via OpenAlex: Iverson & Reif's films were amorphised by implantation and give no wall-clock crystallisation time; reworded with their actual anneal range and growth-velocity caveat. |
| 048-L3 | Low | fixed | Matched 050's "we infer ... unsilicided" phrasing for consistency. |
| 049-L1 | Low | fixed | Confirmed via cached periphery.txt: rpm.6 is "min spacing, no overlap" (0.200 µm), not just "no overlap". |
| 049-L2 | Low | fixed | Confirmed via cached periphery.txt: poly.3 = 0.330 µm, poly.9 = 0.480 µm; added them to the body. |
| 049-L3 | Low | fixed | Moved the SkyWater-specific KLA tool name out of the industry-generic recipe sentence. |
| 050-L1 | Low | fixed | [^axcelis-8250] (no dose spec) dropped from the 1e14 sentence as part of the 050-M1 rewrite; it remains correctly used in Cross-check for the medium-current tool class. |
| 050-L2 | Low | fixed | Confirmed via OpenAlex: Kamins 1972 says poly diffusion is "more rapid" with lower activation energy, no order-of-magnitude figure. Reworded. |
| 050-L3 | Low | fixed | Added the NGNIT e-test cross-reference to 050, pointing at 058's npc-mask reading. |
| 051-L1 | Low | fixed | Confirmed via OpenAlex: Kern 1990 gives no oxide thickness. Reworded as a typical-industry figure. |
| 051-L2 | Low | fixed | Added the missing citation/typical-value label for the SPM temperature. |
| 051-L3 | Low | fixed | Confirmed via OpenAlex: Fujimura 1989's two-step process is H2-RIE-plus-downstream, a different sequence from the cold-then-hot O2 one this page describes (from pat-strip-mosel). Fixed the Deep dive annotation. Shared with 057-L3. |
| 052-L1 | Low | fixed | Noted the 0.33 µm test structures are narrower than the narrowest supported fixed width (rpm.1b) and at the poly.3 minimum, unlike the PDK's 0.35 µm e-test comparator. |
| 053-L1 | Low | fixed | Confirmed via cached CSV: double space after "P+"/"P-" in the module header. Restored the exact spacing with a note. Shared with 056-L2. |
| 053-L2 | Low | fixed | Reworded the Open question so it no longer reads "splits" as evidence of multiple implants (Common rule 2). |
| 054-L1 | Low | fixed | Confirmed via OpenAlex: Fujimura 1991 measures ash rate/activation energy, not crust penetration. Reworded to what it actually measured. |
| 054-L2 | Low | fixed | Cited fujimura-1989's residue finding (oxide of implanted species) instead of an unsourced "removes without difficulty" claim. |
| 055-L1 | Low | fixed | Redid the arithmetic: 2000/300 = 6.67, 2000/319.8 = 6.25, not 7. Fixed both occurrences ("factor of seven" and "seven times higher"). |
| 055-L2 | Low | fixed | Confirmed 052 and 049 leave the question open; softened the "used throughout these pages" overstatement and cross-referenced 052's open question. |
| 055-L3 | Low | fixed | Added Lane & Wrixon's published poly design space to Why this step exists, as a second independent source alongside SkyWater's own documentation. |
| 056-L1 | Low | fixed | Fixed the backwards description ("dose x thickness" -> concentration x thickness), matching 053's correct wording. |
| 056-L2 | Low | fixed | = 053-L1 |
| 056-L3 | Low | fixed | Downloaded all 88 pminus_poly_res half/one-square .mdm files from GitHub and re-ran slope.py myself (script in scratchpad); found the actual outliers (module 6222 pads 1-2/1-3, module 6219 pad 10-12 and its D2 device, module 6222 pad 7-9) spanning 2.2x to 69x, matching the page's "twice to more than sixty times" claim, and named them. |
| 057-L1 | Low | fixed | Checked archive.org: only an index/TOC item for RCA Review vol 31 exists, not the full article text, so did not invent a full-text URL; added a "no DOI, available in print and library archives" note instead, repo-wide (057, wet-bench.md, wet-chemicals.md, categories/strip.md, all citing the same key). |
| 057-L2 | Low | fixed | = 051-M1 |
| 057-L3 | Low | fixed | = 051-L3; also removed fujimura-1989 from the in-text "two-step sequence" sentence, keeping only pat-strip-mosel (the actual source of that sequence). |
| 058-L1 | Low | fixed | Added the PDK's NGNIT e-test corroboration and the Tsang et al. nitride-cap corroboration (with correct mechanism) to What this step is / Resistor protection. |
| 059-L1 | Low | fixed | Confirmed via OpenAlex: Hinsberg 1992 measured N-methylpyrrolidone (an amide), not amines specifically. Reworded to "amines and amides". |
| 059-L2 | Low | fixed | Duplicated the four primary-source citations (sturtevant-1994, dijkstra-1993, he-1998, bell-1996) into Cross-check, per citation-style.md rule 5. |
| 060-L1 | Low | open | |
| 060-L2 | Low | open | |
| 060-L3 | Low | open | |
| 060-M-ref | Low | fixed | = 051-M1; replaced with lederer-2003 (already on page), which names the Surfscan SP1 BSIM explicitly. |
| 061-L1 | Low | open | |
| 061-L2 | Low | open | |
| 061-L3 | Low | open | |
| 062-L1 | Low | fixed | Confirmed cached ITRS FEP table: Gate Etch Bias (2001) = 25.2 nm, not 25. |
| 062-L2 | Low | fixed | Confirmed cached snf-9400.txt: page states the TCP 9400 was "originally used for gate etching with high selectivity to thin gate oxides"; added the quote. |
| 063-L1 | Low | fixed | Copied 002/047's correct dual-journal citation for Deal 1980. |
| 063-L2 | Low | fixed | Confirmed via OpenAlex: Kao et al. measured retardation of curved-surface oxidation, not enhancement. Reworded the bird's-beak sentence. |

## Checkers and build

To run from the worktree in the foreground before finishing:
`check_steps.py`, `check_refs.py`, `check_machines.py`,
`check_materials.py`, `check_masks.py`, `check_papers.py`,
`gen_papers.py --check`, and `sphinx-build -W -q -b html`.
