# Progress — topic/p4-164-171 (fixer for review-164-171.md)

Source review: `tmp/p4/review-164-171.md`. No High findings in range. Working
Medium -> Low. Steps 135-163 are other fixers' branches (open); edits here
stay inside 164-171 and shared files (overview, categories, inventory) are
touched minimally, except where the review specifically asks for a
164-171-caused overview fix (167-M2, 169-M1).

## Scope exclusion — metal-cap/barrier composition sweep

Per coordinator instruction, the metal cap/barrier composition item (whether
a metal level carries a TiW or TiN cap; how the 2014 Cypress report
QTP 123907 is read) is handled by a dedicated cross-cutting sweep. This
branch does NOT edit the sentences the review lists for that item:
`168-pdm.md:230` (finding 169-L4) and `170-ally.md:57-58` (cross-page
conflict 6, no separate finding id). Both are marked "deferred" below and
left untouched.

## Site-wide items not touched here

* Vendor-name spelling split ("GaSonics"/"Gasonic", "Aspen II"/"Aspen2") —
  site-wide sweep, per brief. Locations noted by the review at
  `166-nsme.md:128,153` and `169-pdme.md:123-124,154`. Left alone.

## Findings

| id | severity | status | note |
|---|---|---|---|
| 164-M1 | Medium | fixed | TOPOX identification stated before its fuse-oxide caveat (164:15-16) |
| 164-M2 | Medium | fixed | Chaudhari 1974 (Pb/Sn hillock model) cited for Al hillocks (164:77-78, 232-234) |
| 164-L1 | Low | fixed | "highly stressed" over-generalises Lanford/Claassen (164:71-72) |
| 164-L2 | Low | fixed | Zeevo quote drops HDP-doping-difficulty reason (164:84-87) |
| 164-L3 | Low | fixed | "compliant layer under a stiff film" unsourced (164:74-76) |
| 164-L4 | Low | fixed | R7FT-3R is 0.18 um tech, not flagged in machines-inference section (164:150-153) |
| 165-M1 | Medium | fixed | TSMC patent has three IMD layers not "three or four" (165:136-139) |
| 165-M2 | Medium | fixed | "5.3711 um above the substrate" contradicts overview's datum note (165:77-78; also fix 166:31-32) |
| 165-L1 | Low | fixed | nsm.3a is enclosure not spacing rule, paraphrase conflates with nsm.3b (165:33-35) |
| 165-L2 | Low | fixed | two different areaid.sl layers (81:1 vs 81:7) not distinguished (165:37-39,263,267-269) |
| 165-L3 | Low | fixed | seal-ring cell reading omits areaid.cr/areaid.cd stress-DRC layers (165:43-46) |
| 165-L4 | Low | fixed | GF "one mask" sentence is about nitride/polyimide film, word dropped (165:100-102) |
| 166-M1 | Medium | open | LINIT/LINT name split never bridged (166:29-30,47-48,179; also 167:48) |
| 166-L1 | Low | open | Kastenmeier 1996 is downstream/remote etch, cited for biased breakthrough step (166:119-121,218-219; also 169:100-102) |
| 166-L2 | Low | open | Wodecki cited for inference his paper argues against (166:124-127,220) |
| 166-L3 | Low | open | hyphenation mismatch inside TSMC patent quotation (166:117-118) |
| 166-L4 | Low | open | unmarked mechanical assertion about nitride closing moisture path (166:84-86) |
| 167-M1 | Medium | open | Vanguard "comparable stack" — oxide 4-8x thicker than PDK value (167:132-135) |
| 167-M2 | Medium | open | NTSD says polyimide "not public" while overview cites SkyWater S130 "Yes" (167:254-256, also body 56-63; overview cross-ref) |
| 167-L1 | Low | open | dual-frequency RF stress-trim practice asserted without a source that states it (167:120-122) |
| 167-L2 | Low | open | 0.7-0.9 um range folds 0.18 um R7FT-3R tech into S8 range without saying so (167:129-131,242-244) |
| 167-L3 | Low | open | Sinha 1978 numbers not used though on point (167:69-71,210-211) |
| 167-L4 | Low | open | "only processing left" overlooks strip folded into PDME (167:20-23) |
| 168-M1 | Medium | open | "same GDS layer number (76:44) as pad" mis-states pad's own layer (168:95-96) |
| 168-L1 | Low | open | areaid.mt rule quoted without its test-chip waiver (168:89-90; also 171:48-50) |
| 168-L2 | Low | open | k1 sentence silently uses space vs 165's feature, no note (168:56-59) |
| 168-L3 | Low | open | "any rework strips resist..." unmarked inference (168:69-70) |
| 168-L4 | Low | declined | reviewer: already correctly marked as inference, "no action strictly required"; apply reviewer's optional strictest wording anyway (168:35-39) |
| 169-M1 | Medium | open | Open-questions passivation range mixes oxide+nitride total vs nitride-only figure (169:241-245; also overview :785-792) |
| 169-L1 | Low | open | Kastenmeier/Wodecki same two caveats as 166-L1/166-L2 (169:100-102,115-118) |
| 169-L2 | Low | open | "hidden and later grow during bonding" over-reads Hunter et al. (169:86-88) |
| 169-L3 | Low | open | "in sequence" wording not precise re category page (169:47-49) |
| 169-L4 | Medium(cap) | deferred | metal-cap sweep — Danzl annotation on 168-pdm.md:230-231 needs cap hedge; DO NOT EDIT (scope exclusion) |
| 170-M1 | Medium | open | Maes et al. 1981 listed as a hazard; paper reports hydrogen anneal *improved* MNOS retention (170:108-112,236-237,254-255) |
| 170-M2 | Medium | open | "below temperatures at which Al hillocks/voids grow rapidly" unsourced and contradicts category page + own text (170:129-133) |
| 170-L1 | Low | open | deuterium 10-50x factor quoted without Kizilyalli's one-level-only caveat (170:85-89) |
| 170-L2 | Low | open | "only anneal listed with H2" true but Iridia/Aspen2 asher H2 entries unmentioned (170:160-162) |
| 170-L3 | Low | open | Al-Si eutectic invoked with no citation (170:132-133) — folded into 170-M2 fix |
| 170-L4 | Low | declined | reviewer: no change required, recorded only for contrast with 164-M1 |
| (n/a) | n/a | deferred | metal-cap sweep — 170-ally.md:57-58 "interfaces between aluminium, TiW and tungsten" unhedged; DO NOT EDIT (scope exclusion, cross-page conflict 6) |
| 171-L1 | Low | open | truncated SONOS e-test quotation ("for both original and star cells" dropped) (171:41-42) |
| 171-L2 | Low | open | "two copies" quotation footnoted to wrong README (171:59-65) |
| 171-L3 | Low | open | README title quoted short (171:63-64) |
| 171-L4 | Low | open | single 7/0.15um structure quoted where two exist, differ 0.012V (171:205-206) |
| 171-L5 | Low | open | notebook quotations footnoted to directory listing, not specific file (171:385-389) |
| 171-L6 | Low | open | Group-code list omits stray `3791956` value (171:382-383) |
| 171-L7 | Low | open | "four Die Row groups" passes over 2 blank rows (271 of 273 assigned) (171:66-67) |

## Checks

Run before finishing: `check_steps.py`, `check_refs.py`, `check_machines.py`,
`check_materials.py`, `check_masks.py`, `check_papers.py`,
`gen_papers.py --check`, `sphinx-build -W`. Not yet run.
