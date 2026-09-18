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
| 113-H1 | High | open | "Track ammonia clean" (SkyWater capabilities page) misread as litho-track amine filtration; it is under the AMAT Mirra CMP block. |
| 108-M1 | Medium | open | Zero-enclosure mcon floor claim: PSG/NCAPOX is reached only if the etch over-trenches; the floor beside `li` is LINIT nitride + NILD2 oxide. |
| 110-M1 | Medium | open | wiki-wf6 does not print the 2WF6+3SiH4 equation cited beside it. |
| 112-M1 | Medium | open | Resistivity reasoning reversed: 4.0 uOhm-cm is above, not within, the typical Al-0.5%Cu range, and parallel refractory layers should lower not raise apparent resistivity. |
| 114-M1 | Medium | open | OES wavelengths (396 nm, 261 nm) cited only to a source explicitly disclaimed as general. |
| 115-M1 | Medium | open | US 6,914,016 annotated as a deposition/etch sequence; it is a single-step fluorine-assisted HDP recipe above 450 C. |
| 107-L1 | Low | open | ct.3 quotation cut short without ellipsis and drops the 0.170*L value. |
| 107-L2 | Low | open | "152000 mOhm each" — PDK heads the column "Resistivity (mohms/sq)"; per-contact reading not marked. Recurs 108, 109, 110, 111. |
| 107-L3 | Low | open | Category-page cross-reference is circular; add the actual evidence. |
| 108-L1 | Low | open | Lam 10-K uncheckable (SEC 403, no Wayback); pair with the retrievable 2001 press release. |
| 109-L1 | Low | open | AMAT PVD Metal film list omits "SiO2" from the source. Recurs 112. |
| 109-L2 | Low | open | amat-endura 403; needs Wayback URL and 200mm-era framing reattributed. Recurs 112 (conflict 5). |
| 110-L1 | Low | open | "multi-station Altus family" — source doesn't say "multi-station" (that's the Concept One-W). |
| 110-L2 | Low | open | W-plug/electromigration sentence has no citation at all. |
| 110-L3 | Low | open | "qualified down to" is an unmarked reading of the PDK's CEFC value. |
| 111-L1 | declined | open | JOB-01 site-wide sweep item; left alone per coordinator instruction. |
| 111-L2 | Low | open | Same as 107-L2 (per-contact reading); fixed once on 107, pages point back. |
| 112-L1 | Low | open | "excluding top metal" belongs to the S8P row only, not all three technologies. |
| 112-L2 | Low | open | Quotation drops a space before the hyphen in "Al -0.5%Cu". Recurs 113, 114, 123. |
| 112-L3 | Low | open | 10 wt% Ti is the film composition per the patent, not the target's. |
| 112-L4 | Low | open | Stack dated "2013-2014"; the report is dated March 2014 only. |
| 112-L5 | Low | open | pdk-02 never prints "S8"; identification is properly made on the overview page. |
| 113-L1 | Low | open | LI1MCD quoted as 0.14 without noting the table's second (0.17) row. |
| 114-L1 | Low | open | "AlCl3 is volatile at room temperature" overstates (sublimes ~180C; etch chamber vapour pressure is temperature-assisted). |
| 114-L2 | Low | declined | Lam 10-K uncheckable but corroborated by SkyWater's own list; no fix required per review, note only. |
| 114-L3 | Low | open | "tightest pitch of any metal level" overstated — metal 2 ties at 0.28um. Recurs 113 (poly/LI tie too). |
| 115-L1 | Low | open | SkyWater HDP entry's "high aspect (5:1) fill capability" sub-line omitted; strengthens the inference. |
| 115-L2 | Low | open | Footnote-ordering style nit (trikon-10k-1996 out of the PDK->SkyWater->SEC->vendor->wiki->books->papers order). |
| 116-L1 | Low | open | "first of the back-end oxide polishes" inconsistent with the page's own Related-steps list and 111's wording. |
| 116-L2 | Low | open | Preston's law rests on an unretrievable 1927 source alone; add a retrievable secondary citation. |
| 116-L3 | declined | open | JOB-01 site-wide sweep item; left alone per coordinator instruction. |
| 117-L1 | Low | open | "_C" suffix used as inference evidence from a name (Common rule 2). |
| 117-L2 | Low | declined | amat-10k uncheckable but independently documented; no fix required per review, note only. |

Checks to run before finishing (foreground): check_steps.py, check_refs.py,
check_machines.py, check_materials.py, check_masks.py, check_papers.py,
gen_papers.py --check, sphinx-build -W -q -b html.
