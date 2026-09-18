# Progress — topic/p4-135-148 (fixer, review-135-148.md)

Status legend: open / fixed / declined / deferred (metal-cap sweep,
per coordinator instruction — not this agent's scope).

| Finding | Status | Note |
|---|---|---|
| X1 (High, metal-3 cap TiW vs 2014 S8P report) | deferred | scope exclusion: cross-cutting metal-cap sweep handles this on every page at once; sentences left untouched |
| 135-L1 | fixed | Babcock Deep-dive annotation corrected to frequency dependence/voltage linearity/dispersion |
| 135-L2 | fixed | Kar-Roy Deep-dive annotation: "aluminium" removed from paraphrase, marked as our inference from the date |
| 135-L3 | fixed | split citation: PDK k=7.5 cited for "highest density per thickness", Van Huylenbroeck kept for dispersion |
| (135 open question, part of X3/144-M2) | fixed | added the cross-section's explicit "Via3" label as further support for the metal-3 reading |
| 136-M1 (= X2, also 137-M1) | fixed | corrected: Freescale's MiM is top-plate-first in patterning order only, over a dedicated CMP-planarised bottom electrode, not on the interconnect metal |
| 136-M2 | fixed | TiN top-plate claim re-attributed to the two patents that actually state it (US 6,430,028, US 8,110,414); Kar-Roy/Babcock Deep-dive bullets reworded to what their abstracts actually say |
| 136-L1 | fixed | dropped the uncited "some tens of µΩ·cm" range; kept only the industry-typical 50-100 µΩ·cm with its textbook citation |
| 136-L2 | fixed | "Ta/TaN top electrode" corrected to bottom electrode/diffusion barrier per US 7,250,334 |
| 137-M1 | fixed | see 136-M1 |
| 137-L1 | fixed | enumerated the three spacing rules (capm-via2, via-capm, capm-met2) that were missing from the list of twelve |
| 137-L2 | fixed | corrected capm.3-capm.5 range label: capm.5 is a spacing, not an enclosure |
| 138-M1 (TiW-to-nitride selectivity) | deferred | scope exclusion: depends on which cap the metal-3 line carries |
| 138-M2 (= X1) | deferred | scope exclusion |
| 138-L1 (EKC/wet-bench attribution) | declined | already correct on this branch's base (main); phrase "of the wet-bench list" not present, page already reads "under Batch Rotational" — no action needed |
| 138-L2 | fixed | added `[^pat-mim-ti-etch]` beside `[^hess-1982]` with the patent's own AlF3 sentence quoted |
| 139-M1 (= X1) | deferred | scope exclusion |
| 139-L1 | fixed | distinguished m3.pd.1 (0.7) from the assumptions table's global OxideMinPD (0.75) |
| 139-L2 | fixed | added the fourth "Metal 3-Cu" CD row and its copper-flow attribution |
| 140-M1 (= X1) | deferred | scope exclusion |
| 140-L1 (vendor spelling GaSonics/Aspen; EKC attribution) | declined (spelling) / declined (EKC, already correct) | vendor-spelling split is a separate site-wide sweep per coordinator instruction, left untouched; EKC attribution already correct on this branch's base |
| 140-L2 | fixed | attributed the "begins with a dielectric" claim to "this reference's reading of CAPME" rather than stating it as fact |
| 141-L1 | fixed | distinguished m3.pd.1 (0.7) from OxideMinPD (0.75) here too |
| 141-L2 | fixed | made explicit that the public entry names only doped/phos-doped HDP films, cross-referenced to the open question |
| 142-L1 (`[^job-01]`) | declined | separate site-wide sweep per coordinator instruction; left untouched |
| 142-L2 | fixed | added `[^steps-sheet]` to the quoted step-list description "CMP over metal3" |
| 142-L3 | fixed | added `[^steigerwald-1997][^zantye-2004]` to the uncited "industry-standard for ILD" parenthesis |
| 143-L1 (= part of X3) | fixed | cross-section vias now described as labelled "Via3" |
| 143-L2 | fixed | corrected: PECVD nitride, not the TEOS, is what the reports call PECVD; TEOS-being-plasma is now marked as our inference |
| 144-M1 (also 147-M1) | fixed | Le/Banerjee/McPherson claim corrected to its actual conditional finding (TiN cap, M2->M1 flow only; no dependence with a Ti-bearing cap) |
| 144-M2 (= X3) | fixed | cross-section's explicit "Via3" label added at both open-question locations |
| 144-L1 | fixed | linked the "digit 4" reading to ITRS 2001's stated 4x mask magnification |
| 145-M1 | fixed | removed the "fluorine-bearing" misquotation of US 6,090,697; replaced with the patent's real subject (etch-stop punch-through) and its published 28.4:1 / 228:1 selectivity numbers |
| 145-M2 (= X1) | deferred | scope exclusion |
| 145-L1 | fixed | Schaepkens et al. citation scoped to what it actually measured (SiO2-to-Si3N4/Si), extension to a refractory stop marked as inference |
| 145-L2 | fixed | added a citation-free reword for the TiF4 claim, noting the citation covers only the tungsten half |
| 145-L3 (vendor spelling) | declined | separate site-wide sweep per coordinator instruction |
| 146-M1 (= X1) | deferred | scope exclusion |
| 146-L1 (step-name-derived ordinal) | fixed | reworded to enumerate the four TiN-only liners plus the TI/TIN1 bilayer explicitly, not an ordinal keyed to the step-code digit |
| 146-L2 | fixed | dropped `[^rossnagel-1998]` from the numeric liner-thickness claim, kept on the mechanism sentences |
| 147-M1 (= 144-M1) | fixed | see 144-M1 |
| 147-L1 (Broadbent & Ramiller pattern) | fixed | moved `[^rev-03][^mcconica-1986]` to the hydrogen-reduction clause only; added the nucleation-layer citations already on the page to the first clause |
| 147-L2 | fixed | reworded: the fill-both-holes claim is a geometric consequence, not backed by the paywalled Ireland citation |
| 148-L1 (`[^job-01]`) | declined | separate site-wide sweep per coordinator instruction |
| 148-L2 | fixed | added the published test-tile via-array/via-chain evidence, noted the inference-on-inference structure |
| 148-L3 | declined | reviewer states "none required for accuracy"; left as is |

## Verifier follow-ups (verify-135-148.md)

| Item | Status | Note |
|---|---|---|
| 1. Via3 label attributed to two vias | fixed | confirmed against the cached SVG: exactly one "Via3" text element, on the via that lands on CAPM; corrected 135:338-341, 143:41-42 and :182, 144:117-119 and :300-302 to say the cross-section labels only that via |
| 2. Spliced test-tile quotation | fixed | 148-wcmp5.md:55-57 now quotes the CSV row whole: "Via-3 chain, 5754 via-3, M4-CAPM over M3" |
| 3. Kar-Roy TiN attribution survives at 136:70-71 | fixed | dropped [^kar-roy-1999] from that sentence, consistent with the corrected sentence at 136:106-107 |
| 4. "fluorine-bearing" misquotation survives at 130/160 | fixed | 130-vim2e.md:73 (quoted) and :256, 160-vim4e.md:88 and :255 reworded like 145: quotation removed, patent's real subject (etch-stop punch-through) and selectivity numbers substituted. Note: the identical misquotation also survives at 119-vime.md:82,282, outside the coordinator's four listed locations and outside this branch's assigned range; not touched here, flagged for the coordinator/sweep. |
