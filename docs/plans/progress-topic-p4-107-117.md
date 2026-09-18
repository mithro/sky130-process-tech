# Progress — topic/p4-107-117 (Phase 4 fixes, steps 107–117)

Applying `tmp/p4/review-107-117.md` (35 finding ids: 3 High, 5 Medium,
27 Low, plus two site-wide items tabled but not itemised — the
`[^job-01]` job-listing citation and the GaSonics/Aspen vendor-spelling
split — both left untouched per the coordinator's instructions, as
separate site-wide sweeps). Each finding is independently re-verified
against the cited public source (PDK cache, Crossref/OpenAlex, cached
patent/vendor pages) or by redoing the arithmetic before being fixed or
declined. Where a misattribution (110-H1, 112-H1) recurs outside this
page range, `docs/` is grepped for the citation key and every
occurrence is checked and fixed if needed.

| id | severity | status | note |
|---|---|---|---|
| 110-H1 | High | fixed | Confirmed via OpenAlex abstract (10.1149/1.2115864, cached tmp/p4/fetch/openalex-broadbent-1984.json): paper is WF6/H2 + WF6/Si kinetics for the *selective* process, not WF6/SiH4 blanket. Fixed 110-wdep2.md (body + Deep dive) and the same misattribution recurring at categories/deposition.md Deep dive. Other rev-03 citations in docs/ (overview/index.md, machines/tungsten-cvd.md, steps 099/121/132/147) already describe it correctly (generic "WF6 chemistry"/"hydrogen and silicon reduction") and needed no change. |
| 112-H1 | High | fixed | Confirmed via OpenAlex abstract (10.1063/1.322842, cached tmp/p4/fetch/openalex-blech-1976.json): the paper measures the electromigration threshold current density / critical length on Al over TiN; it does not describe a TiAl3 conductive shunt. Fixed 112-tial6.md body text (attributed the shunt/redundancy claim to domenicucci-1996 as industry practice, kept blech-1976 only for the critical-length claim; the page's Deep dive bullet was already correct). Same misattribution recurred at 123-tial12.md:90-93 (fixed the same way) and categories/deposition.md (reworded to drop the "keeps a line open" shunt framing from the blech-1976 sentence). 101-litin.md, 134-wtial3.md, 149-wtial4.md and the rest of 112/123's own citations already describe Blech correctly (critical length / threshold current) and needed no change. |
| 113-H1 | High | fixed | Confirmed via tmp/p4/fetch/skw-facilities.txt:181: the page's only "ammonia" mention is "Track ammonia clean" inside the AMAT Mirra CMP block (lines 170-182), not the lithography track section (lines 91-93 list only DNS 80B/Sokudo RF3/TEL ProZ Lithius, no filtration claim). Fixed 113-mm1.md, and grepped docs/ for the same "track's ammonia-filtered environment[^skw-01]" misattribution, which recurs verbatim on three parallel mask pages outside this range (118-vim.md, 124-mm2.md, 129-vim2.md, all citing skw-01 for the same unsupported claim) — fixed all three the same way, per the coordinator's note that this misattribution pattern may recur on 118-163. The machine pages that discuss airborne-amine filtration (duv-krf-stepper.md, coat-develop-track.md) already cite macdonald-1991/nikon-s204b/tel-act correctly and needed no change. |
| 108-M1 | Medium | fixed | Confirmed 105-nild2.md:15-20 (NILD2 fills the 0.17um li-li gaps) and pdk-04 (li at 0.9361um, met1 bottom 1.3761um): a zero-enclosure mcon floor beside `li` sits on LINIT nitride + NILD2 oxide; PSG/NCAPOX is a further 0.10um down and is reached only by over-trenching. Reworded per review's fix. |
| 110-M1 | Medium | fixed | Confirmed tmp/p4/fetch/wiki-wf6.html: the "Silane and germane" section is qualitative only (no equation); dropped wiki-wf6 from the 2WF6+3SiH4 equation (kept txt-01) and moved it to the "silane commonly used to create a thin nucleation layer" statement it does support. |
| 112-M1 | Medium | fixed | Redid the arithmetic (0.125 ohm/sq x 0.32um = 4.0 uOhm-cm) and confirmed sputtered Al-0.5%Cu is typically ~3 uOhm-cm and that Ti/TiW conduct in parallel (lowering, not raising, apparent resistivity) -- the original reasoning had both points backwards. Reworded per review's fix. |
| 114-M1 | Medium | fixed | Confirmed nojiri-2015 is already used elsewhere on the page (dry-etch textbook, industry-typical per rule 3); attached it to the two OES wavelengths in place of the bawolek-1987 citation that was explicitly disclaimed as general. |
| 115-M1 | Medium | fixed | Confirmed tmp/patent-cache/US6914016B2.html abstract: single-step fluorine-assisted HDP deposition above 450C, fluorine <1 at.%, not a deposition/etch sequence (that is US 6,030,881/pat-hdp-novellus, whose abstract does say "a sequence of deposition and etch"). Reworded both Deep dive bullets per review's fix; body citations at lines 74/120 already correct, left alone. |
| 107-L1 | Low | fixed | Confirmed pdk-periphery.txt:1484 continues ct.3 with "…die seal ring where mcons are…" and value "0.170*L". Added the elision marker and value per review's fix. |
| 107-L2 | Low | fixed | Confirmed pdk-rcx.txt:654 heads the column "Resistivity (mohms/sq)" for every row. Added the parenthetical on 107 and a pointing-back cross-reference on 108, 109, 110 and 111 (same fix as 111-L2). |
| 107-L3 | Low | fixed | Confirmed categories/lithography.md:85-88 attributes the reading back to this page (round trip, no external evidence). Reworded per review's fix, naming the actual evidence (0.17/0.19um rules, ITRS 2001). |
| 108-L1 | Low | fixed | Lam 10-K stays uncheckable (SEC 403, no contact address permitted, no Wayback copy) but is now paired with the retrievable lam-exelan 2001 press release already cited elsewhere on the page. |
| 109-L1 | Low | fixed | Confirmed skw-facilities.txt:113-123 lists a further film "SiO2" after "Niobium" under the same heading. Appended it to the quoted lists on 109 and 112. |
| 109-L2 | Low | fixed | Confirmed the live page 403s (curl -A) and the Wayback capture (20260916190905) returns 200. Added the Wayback URL to the footnote on 109 and 112, and reworded both "200 mm-era" framings as an explicit reading since the source itself does not date the platform. |
| 110-L1 | Low | fixed | Confirmed novellus-history.html: "the company combined the modular architecture of the Concept Two and the tungsten CVD process chamber, resulting in ... Concept Two-ALTUS" -- no "multi-station"; that six-wafer-chamber description belongs to Concept One-W. Reworded per review's fix. |
| 110-L2 | Low | fixed | Added [^domenicucci-1996] (Ti-AlCu-Ti lifetimes over two-level W stud structures, already the citation used for the same literature on 112/123) with the footnote definition added to the page. |
| 110-L3 | Low | fixed | The PDK gives CEFC/0.14um with no explanation of "qualified down to"; marked the reading explicitly per review's fix. |
| 111-L1 | Low | declined | JOB-01 (indeed.com job listing, 403 live, no Wayback) site-wide sweep item; left alone per the coordinator's explicit instruction (separate sweep). |
| 111-L2 | Low | fixed | Same as 107-L2; added the same pointing-back cross-reference here. |
| 112-L1 | Low | fixed | Reworded to say only the S8P entry reads "excluding top metal layers" and to add the report's own metal-3 line ("500A TiW/21,250A Al 0.5% Cu/300A TiW") as the better evidence, per review. |
| 112-L2 | Low | fixed | Confirmed the recurring verbatim quotation drops a space before the hyphen. Fixed the two verbatim occurrences (112-tial6.md:36,248 and 123-tial12.md:27); 113-mm1.md and 114-mm1e.md already paraphrase without quotation marks and needed no change. |
| 112-L3 | Low | fixed | Confirmed US 5,160,534 states 10 wt% Ti for the deposited film, while its worked target example is "10.36 wt% of hydrogenated titanium" with a three-phase structure. Reworded all three occurrences on 112-tial6.md (lines ~131, 179, 214) to attribute 10 wt% to the film, not the target. |
| 112-L4 | Low | fixed | Confirmed qtp123907.pdf XMP metadata: CreateDate 2014-03-11. Changed "qualified in 2013-2014" to "qualified in 2014". |
| 112-L5 | Low | fixed | Confirmed pdk-background.txt never prints "S8" (it says "8th generation SONOS technology node"); the identification is made via pdk-previous's glossary entry and cyp-22 on the overview page. Cited pdk-previous and cyp-22 here too, with a pointer to the overview. |
| 113-L1 | Low | fixed | Confirmed pdk-assumptions.txt:475-485 has two LI1MCD/LI1MCDSP rows (Core 0.14/0.14, and 0.17/0.17). Added the missing second row per review's fix. |
| 114-L1 | Low | fixed | AlCl3 sublimes at ~180C at atmospheric pressure; reworded to "volatile enough at the modest wafer temperatures of an etch chamber" per review's fix. |
| 114-L2 | Low | declined | Lam 10-K uncheckable but corroborated by SkyWater's own list; no fix required per review, note only. |
| 114-L3 | Low | fixed | Confirmed pdk-periphery.txt:1850-1856: m2.1/m2.2 (metal 2 width/spacing) are also 0.140/0.140um, tying metal 1's pitch. Reworded 114 to say "tied with metal 2" and 113 to say "tied with metal 2, poly and the core local interconnect", per review's fix. |
| 115-L1 | Low | open | SkyWater HDP entry's "high aspect (5:1) fill capability" sub-line omitted; strengthens the inference. |
| 115-L2 | Low | open | Footnote-ordering style nit (trikon-10k-1996 out of the PDK->SkyWater->SEC->vendor->wiki->books->papers order). |
| 116-L1 | Low | open | "first of the back-end oxide polishes" inconsistent with the page's own Related-steps list and 111's wording. |
| 116-L2 | Low | open | Preston's law rests on an unretrievable 1927 source alone; add a retrievable secondary citation. |
| 116-L3 | Low | declined | Same JOB-01 site-wide sweep item as 111-L1; left alone per the coordinator's explicit instruction. |
| 117-L1 | Low | open | "_C" suffix used as inference evidence from a name (Common rule 2). |
| 117-L2 | Low | declined | amat-10k uncheckable but independently documented; no fix required per review, note only. |

Checks to run before finishing (foreground): check_steps.py, check_refs.py,
check_machines.py, check_materials.py, check_masks.py, check_papers.py,
gen_papers.py --check, sphinx-build -W -q -b html.
