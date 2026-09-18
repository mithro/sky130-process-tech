# Progress — topic/p4-149-163 (fixer for review-149-163.md)

Source review: `tmp/p4/review-149-163.md`. Working Medium -> Low (no High
findings are in this branch's scope; the sole High, X1, is deferred). Steps
135-148 are another fixer's branch in verification; edits here stay inside
149-163 and shared files are touched minimally.

## Scope exclusion — metal-cap/barrier sweep

Per coordinator instruction, the metal cap/barrier composition item
(section 1 of the review: findings X1, X2, X3, X4, and the whole "metal
cap / barrier composition" section) is NOT this branch's to fix — a
dedicated cross-cutting sweep handles every page at once. Two more findings
depend on the same TiW/TiN-cap-composition question or on how
`[^cyp-qtp-123907]` is read, so they are deferred too: **153-L1** and
**161-L1**. The sentences these concern are left untouched.

## Findings

| id | severity | status | note |
|---|---|---|---|
| X1 | High | deferred | metal-cap/barrier sweep — misattribution of `[^cyp-qtp-123907]` (149-wtial4.md:53-55 etc.) |
| X2 | Medium | deferred | metal-cap/barrier sweep — S8P line of `[^cyp-qtp-123907]` as evidence for metal-5 TiW cap (161-wtial5.md:51-62) |
| X3 | Medium | deferred | metal-cap/barrier sweep — Open questions on metal-4 cap uncertainty (149, 153, 155, 160) |
| X4 | Low | deferred | metal-cap/barrier sweep — 0.845/0.8 and 1.26/1.2 arithmetic argument |
| 149-L1 | Low | fixed | "antenna-rule table" vs *Criteria & Assumptions* naming (149:37, 155:34, 161:31; 163:30 already said "assumptions table") |
| 149-L2 | Low | fixed | Rocke & Schneegans (TiN paper) cited for a TiW cap without saying so (149, 152, 154, 161, 162) — reworded to name TiN and mark the TiW analogy as inference, per the review's wording |
| 149-L3 | Low | fixed | Al-Cu target/Cypress attribution missing footnote (149:161-162) |
| 149-L4 | Low | fixed | Newport Fab/TSMC MiM patents — shared-electrode construction overstated (149:85-87) |
| 150-M1 | Medium | fixed | step-name-as-evidence omission pattern (149:52-53, 150:19-22, 151:29-31); the 161 occurrence (line 51) sits inside the range findings X2/X3 concern (51-62), so left for the metal-cap sweep |
| 150-L1 | Low | fixed | missing pad identifiers for CV extraction (150:68-71) |
| 150-L2 | Low | fixed | Van Huylenbroeck et al. — nitride vs ONO finding misstated (150:168-171) |
| 150-L3 | Low | fixed | Chapple-Sokol miscited for a temperature window (150:203-204) |
| 151-L1 | Low | fixed | via3.1a 0.8 µm square not mentioned (151:51-52, 159:47-48) |
| 151-L2 | Low | fixed | per-contact via count stated as fact, not reading (151:104-108) |
| 151-L3 | Low | fixed | Hartsough citation implies corroboration it can't give (151:36-40, Open questions) |
| 152-L1 | Low | fixed | CD-bias arithmetic convention unstated (152:77-81) |
| 152-L2 | Low | fixed | alignment-target naming inconsistency within page (152:155-158) |
| 153-M1 | Medium | fixed | "every capm plate tied to metal4" overstated vs 155's correct wording (153:81-83) |
| 153-L1 | Low | deferred | metal-cap/barrier sweep — S8TNV-5R quote scope (153:31-33, :221) |
| 153-L2 | Low | fixed | solvent-clean citation placement implies chemistry claim (153:145-151) |
| 154-L1 | Low | fixed | CU-flagged rule range incomplete (154:40-42), verified against cached pdk-periphery.txt (m4.7, m4.11-m4.16) |
| 154-L2 | Low | fixed | uncited/unmarked cap2m-edge overlay claim (154:147-152) |
| 155-M1 | Medium | fixed | collective gas-list phrasing attributes all gases to all tools (155:146-149, 163:134-137); verified quotes against cached skw-facilities.txt |
| 155-L1 | Low | fixed | two Cypress reports of different tech families conflated (155:38-41) |
| 155-L2 | Low | fixed | "via-3/via-4 oxide beneath" misnames the dielectric (155:145-147, 163:128-130) |
| 156-M1 | Medium | fixed | HDP quote dropped "doped and phos doped" qualifier (156:50-53); verified against cached skw-facilities.txt |
| 156-L1 | Low | fixed | "oxide" stated as fact rather than reading (156:19-23) |
| 157-L1 | Low | fixed | SEZ223/Davinci vs "SEZ 223 / Da Vinci" spelling split within page (157:198) |
| 157-L2 | Low | fixed | "industry-standard" slurry claim missing adjacent citation (157:20-21) |
| 157-L3 | Low | fixed | no-plug-polish argument from step-list silence not marked as such (157: Open questions) |
| 158-L1 | Low | fixed | "PECVD TEOS" invents a deposition method not in either report (158:105-110); verified both Cypress PDFs with pdftotext |
| 158-L2 | Low | fixed | 650-750°C LPCVD window not clearly labelled as textbook value (158:116-119) |
| 159-M1 | Medium | fixed | Skelly & Gruenke via-fill analogy ignores non-monotonic 2.8 µm result (159:90-97, 161:73-79); verified abstract via Crossref |
| 159-L1 | Low | fixed | Le, Banerjee & McPherson EM finding is conditional, cited as unconditional (159:137-141); verified abstract via OpenAlex |
| 159-L2 | Low | fixed | via4/via3 resistance-per-area residual left uncomputed (159:47-51), fixed alongside 151-L1 |
| 160-M1 | Medium | fixed, corrected | Bui et al. citation misapplied to a residue claim (160:76-83); own fresh Crossref check found the abstract IS published (contrary to the review's claim), so used its actual content (TiN ARC thickness vs EM lifetime) rather than the review's "not publicly readable" wording — see note below |
| 160-L1 | Low | fixed | EKS265 silently read as "EKC265" without marking the reading (160:200-204) |
| 161-L1 | Low | deferred | metal-cap/barrier sweep — 300 Å TiW analogue is top not lower metal (161:214-215) |
| 161-L2 | Low | declined | Kikuta review cited beyond its published abstract (161:91-93) — the review said no abstract is published; a fresh Crossref fetch (DOI 10.1557/S0883769400045577) returns a full abstract that says reflow sputtering "can simplify device-fabrication processes and achieve high reliability without Al/W interfaces" and that W-CVD has "greater resistivity than Al", directly supporting the page's "avoids Al/W interfaces and the higher resistivity of tungsten"; no change needed |
| 161-L3 | Low | deferred | plural "reports" with a single footnote — line 51-53 sits inside the range finding X2 concerns (51-62); left for the metal-cap sweep |
| 162-M1 | Medium | fixed | S8PIR reading uses 3 of 5 Background features, omits the strongest argument (162:31-44); required by coordinator instruction explicitly; all values verified against cached pdk-background.txt, pdk-antenna.txt, pdk-periphery.txt, pdk-assumptions.txt |
| 162-L1 | Low | fixed | m4.4 probe-pad exemption asymmetry not noted (162:43-44); verified against cached pdk-periphery.txt |
| 162-L2 | Low | fixed | circular step-list-silence reasoning (162:117-124) |
| 163-M1 | Medium | fixed | same as 155-M1, second page (163:134-137) |
| 163-L1 | Low | fixed | via-4 aluminium-fill relationship asserted without explanation (163:186-187, new bullet in Why this step exists) |
| 163-L2 | Low | fixed | 155/163 aluminium etch-rate implied rates inconsistent (155:131-133, 163:119-122) |
| EKC-ATTACH | (site-wide, in range) | fixed | EKC/EKS solvents unattached to "Batch Rotational" entry, within 149-163 (155, 160, 163) — review §0 item, not excluded by coordinator, so checked/fixed here |

### Note on 160-M1

The review said Bui et al. 1994 (`[^bui-1994]`, DOI 10.1557/PROC-338-471)
has "no abstract published (checked at Crossref and OpenAlex)". A fresh
`curl -A "sky130-process-tech docs checker" https://api.crossref.org/works/10.1557/PROC-338-471`
in this branch returns a full publisher abstract. Rather than the
review's proposed fix (drop the citation, or note the content is not
readable), the sentence was rewritten to state what the abstract
actually says: a thinner TiN ARC cap cut Kelvin-via EM lifetime by
about an order of magnitude versus a thicker one, under one current
direction — a finding about cap *thickness*, not etch residue, which
is still not quite what the original sentence claimed (residue
degrading EM performance), so the citation is still corrected, just
with real content instead of a "content not readable" hedge.

## Site-wide items from the review left alone (per coordinator instruction)

| item | status | note |
|---|---|---|
| `[^job-01]` job-listing citation, verbatim quotation | left alone | separate site-wide sweep |
| Mattson Aspen II / Aspen2 spelling split | left alone | separate site-wide sweep |
| "Gasonic PEP" spelling | no action | reviewer confirms this is the correct published string |

## Checks before finishing

- [ ] `uv run python tools/check_steps.py`
- [ ] `uv run python tools/check_refs.py`
- [ ] `uv run python tools/check_machines.py`
- [ ] `uv run python tools/check_materials.py`
- [ ] `uv run python tools/check_masks.py`
- [ ] `uv run python tools/check_papers.py`
- [ ] `uv run python tools/gen_papers.py --check`
- [ ] `uv run sphinx-build -W -q -b html docs tmp/build-topic-p4-149-163`
