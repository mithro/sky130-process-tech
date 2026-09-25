# Progress — rd-figures-s8 (W1c: emulator improvements, then series S8: contact and metal 1, steps 107–117)

Status: **complete** (part 1 emulator, part 2 series S8, 11 figures); awaiting review.

## Part 1 — emulator improvements before the metal levels

The three items of `progress-rd-figures-s7.md`, "For the generator before S8", and review
rd-figures-s7 M3 and its rulings on the terraced PSG and the corner-filling liner.

### What changed in `tools/gen_figures.py` (each with a selftest)

* **Conformal deposition grows normal to the surface.** A blanket `deposit` (no `only_on`,
  no `fill_to`, no flat-topped `where`) now takes the upper envelope of a disc of radius `t`
  rolled over the surface (`_dilate_round`) instead of a square window. A film has its own
  thickness on a sloped wall, every outer corner is rounded, and a hole's bottom stays open
  until the hole closes. Selftest: a 5 u film in a 10° tapered hole is 5 u at the bottom
  centre, its face is 5 u from the wall at mid-height (±1.5; a square element is 5 u off), and
  its top at 45° from the top corner is 40 + 5/√2 (a square element gives 45).
  Thermal growth (`only_on`) is unchanged: it was not part of the ruling and it is drawn at the
  minimum film anyway.
* **Gap-fill profile** `profile: gapfill` (new `deposit` field; `facet_deg`, default 45, and
  `smooth`, a flow length, go with it only; lint for unknown values). The film grows `t` up from
  every surface (bottom-up fill), adds nothing on a vertical wall, rises over a raised line in
  facets from its edges (flat over a wide line, peaked over a narrow one), and where the fill
  between lines rises above a low line the two merge (the opening of `tops + t` by a cone).
  Every point keeps at least 2 u. Selftest: narrow line peak `H + w/2`, wide line `H + t` with a
  facet 4 u from its edge, nothing on the wall beside a line, `t` on open ground; a flowed
  (`smooth`) film stays between 2 u and `t`.
* **Straight tapered walls at full-slice scale.** A film whose top falls steeply at the end of
  its run (a tapered etch cutting it to nothing) now ends on the wall's line instead of dropping
  vertically at the column boundary, and where a flat top meets the wall between two samples
  the corner is put back (`_corners`). Selftest: a 10° wall through four stacked films has every
  polygon vertex within 0.05 u of the wall line (0.32 u before; the test fails with the change
  switched off).
* `docs/plans/figure-authoring.md` documents `profile` and the straight walls.

### Series and caption changes

* `series-mol.yaml`: PSG (089) is `profile: gapfill` (the PSG page's HDP-CVD reading); header
  updated. NILD2 stays conformal (the 105 page leaves HDP or PECVD TEOS open).
* Captions and alt texts that described the old artefacts were rewritten, and their blocks
  re-pasted on the pages (`check_preserved`: 0 undeclared differences on the 7 pages):
  * 089: "broad terraces" → a gap-filling profile, "only illustrates such a deposit"; alt text.
  * 090 alt: "stepped top" → "faceted top".
  * 097: the liner no longer fills the bottom corners (caption and alt).
  * 099 alt: the tungsten blanket has a shallow dip over the hole.
  * 105: no longer "drawn with a flat top" (shallow dips over the gaps); 106 alt "nearly flat".
  * 077 (spacer etch-back): "flat top" → "rounded top … as a conformal film leaves it when its
    own thickness is etched straight down".

### What changed per series (all 440 files rebuilt; lint clean; `--check` 0 problems)

| Series | Figures changed | What the reader sees |
|---|---|---|
| S1 isolation (001–013) | none | Byte-identical: flat blanket films, `only_on` liner, `fill_to` oxide; the trench is a single silicon run |
| S2 wells (014–034) | none | Byte-identical (no conformal film over topography) |
| S3 SONOS (035–042) | all 8 | The ONO films and the resist over the field-oxide step have rounded outer corners |
| S4 gate oxides (043–047) | none | Byte-identical |
| S5 poly (048–063) | 15 of 16 (063 unchanged) | Gate film, caps and re-oxidation over the field-oxide step: rounded shoulders instead of square ones; stacks otherwise unchanged |
| S6 tips/spacers/S-D (064–088) | 065, 066, 068–070, 075–088 | Spacer nitride deposited with rounded corners; after the etch-back the spacer has the classic rounded top (077's caption updated); spacer oxide rounded; some corners of etched films put back |
| S7 MOL (089–106) | all 18 | PSG faceted (bottom-up fill, peaks over the stacks) instead of terraces; contact walls exact; liner of even thickness with an open, rounded bottom; tungsten blanket with a dimple over each hole; NILD2 with shallow dips over the gaps instead of a flat top |

QA: 16 figures harnessed (iso-006, wells-018 as unchanged controls; sonos-040, poly-048, poly-062,
sd-076, sd-077, sd-080, sd-086, mol-089, 090, 094, 097, 098, 100, 105) and shot at desktop and
400 px in light and dark; every tile opened. Also looked at sd-078, sd-079, mol-099, 102, 104, 106,
sonos-042, poly-059 in light desktop. No label, leader or highlight regression seen; the lint
reported nothing.

## Part 2 — series S8 "Contact and metal 1" (steps 107–117)

### What was done

* **Series** `data/figures/series-metal1.yaml`: ops 002–106 copied verbatim from `series-mol.yaml`
  (same ids and label text, the new PSG `profile: gapfill` included), so the wafer at step 106 is
  the S7 end state; then the module. The header records every choice.
* **11 specs** `data/figures/m1-107-ctm1.yaml` … `m1-117-ncapox3.yaml`, SVGs, paste blocks, each
  block pasted after the first paragraph of "What this step is" (no page in 107–117 has a
  `{dropdown}` there). `git diff main -- docs/steps/1{07..17}*`: 8 lines added per page, 0 deleted;
  `check_preserved`: 0 LOST, only ADDED (the blocks' own numbers, quotes, hedges, markers, ids).
* **Generator** (with a selftest each): a negative `crop_depth` is allowed only in a close-up and
  only if the caption says the lower part of the slice is cut off (lint; documented in
  figure-authoring.md). Needed because the metal contact sits 94 u up in the series: a 2.7×
  close-up of it with the substrate would be over the 800 u height budget.
* Label notes avoid step codes with digits (TIN2, WDEP2, NILD3 …): the number lint reads any digit
  outside "step NNN" as a number. Notes say "deposited at step 109" etc.

### Geometry and reading choices (all declared in the captions)

* **Contacts (107, 108).** Two windows, over the left and the right local-interconnect pads, each
  above the local-contact plug below (x 28–52 and 192–216, illustrative); the middle pad has none.
  CTME etches the NILD2 oxide and the LINT nitride to the TiN (the page's reading: stop on the
  nitride, then open it) and strips the resist in the step (the page treats the strip as part of
  it). Walls tapered at 19.5° (review H1; 12° before), bottom about half the top: drawn tapered because the CTM1/CTME pages
  read the PDK's 0.09 µm "Standard contact bottom CD" against the 0.170 µm square as a markedly
  tapered hole; the angle is not public (caption says so). The hole is only 17 u deep in the series
  (NILD2 12 u + LINT 5 u over the pads, fixed by S7's end state), so its aspect ratio is well below
  the page's ~2:1; not to scale.
* **Liner, fill, polish (109–111)** as close-ups of the right-hand contact, window x 170–268
  (≈2.7×), `crop_depth: -130` (cut off at about 48 u of series height; declared). TiN liner 5 u
  conformal (the barrier colour, the same as the TiN local interconnect it lands on: TiN-on-TiN, as
  the TIN2 page reads it; said so); tungsten 12 u conformal, closing the lined hole with a shallow
  dimple; WCMP2 polishes to the NILD2 top (94 u): flush plug, liner off the field.
* **Metal-1 stack (112)**, close-up, three films in one step: bottom 5 u, aluminium–copper 18 u,
  cap 5 u. **The bottom and the cap are not identified**: both are drawn in the barrier colour and
  labelled "Bottom film / Ti, or Ti/TiN — see the overview" and "Cap film / TiW or Ti/TiN — see the
  overview", basis `inferred`. The caption quotes both public stacks with their keys
  (cyp-qtp-113005, cyp-qtp-123907), says which one SKY130 uses is not public and that the figure
  does not choose, and gives the PDK's 0.36 µm for metal 1 (pdk-04). The aluminium label is
  "Aluminium alloy / aluminium–copper, the conductor; step 112" ("Aluminium–copper" as a title is
  one unbreakable word too wide for the label column).
* **Metal 1 pattern and etch (113, 114).** Three resist lines: one over each contact, enclosing it
  (m1.4), and one over the middle; the right-hand one runs on past the slice edge (so its label
  leader is a straight run and no oxide sliver is left at the edge). Etch removes the whole stack,
  stopping on the NILD2 and the plug tops, vertical walls (profile not drawn to scale); resist
  stripped in the step (the MM1E page). Cap film labelled in both, bottom film unlabelled at
  full-slice scale (declared).
* **NILD3 (115)** `profile: gapfill`, `smooth: 16`, 44 u: bottom-up fill, faceted peaks over the
  lines, softened. The page leaves HDP-CVD or PECVD TEOS open, and the CMPM page describes the
  surface as the metal step "reproduced, softened"; the caption says the drawn profile only
  illustrates a gap-filling deposit. NILD3_C (0.030 µm, liner/cap/neither not public) not drawn,
  said so. **CMPM (116)** flat at 132 u (10 u over the metal; removal not public). **NCAPOX3 (117)**
  8 u flat.
* **Labels hidden** (each declared in its caption): all front-end films and doped regions, the S7
  plugs, silicide, liner and glass throughout; the local interconnect (107, 108: a riser from it
  would cross the resist or read as a contact); the LI nitride cap and NILD2 from 113 on where the
  leaders would pair; the new liner under the tungsten (110 after, 111); NILD2 in 112 after and 114
  before.

### Per-figure record

Every figure: built with no LINT line, `--check` clean, harness shot at desktop and 400 px in light
and dark, every tile opened (round r2 all eleven; round r3 after the 111/112 changes, all dark and
phone tiles plus the light desktop tiles with 109–113). Checked: labels readable at 400 px and beside
their layers, no leader through a film or along an edge, no label below its drawing, highlight on the
changed surface only, dark boundaries visible, panels aligned, picture agreeing with the lead.

| Figure | View | Notes / compromises |
|---|---|---|
| 107 CTM1 | full | Windows illustrative; ct.1 0.170 µm, ct.4 (pdk-periph); LI label hidden (riser would cross the resist) |
| 108 CTME | full | Callout "Metal-contact hole / a 0.170 µm square in the PDK's rules" (pdk-periph); 0.09 µm "Standard contact bottom CD" (pdk-03), about 0.34 µm (pdk-04, our reading) in the caption; taper declared |
| 109 TIN2 | close-up, cut off | Of the order of 10–30 nm (txt-05, industry-typical); 0.09 µm bottom (pdk-03); IMP reading and TiN-on-TiN attributed to the page |
| 110 WDEP2 | close-up, cut off | "a few hundred nanometres" (txt-05); nucleation layer and seam not drawn |
| 111 WCMP2 | close-up, cut off | 0.17 µm tungsten squares (pdk-periph); slurry choice not public; recess/erosion not drawn; plug label rises from the plug (route auto) |
| 112 TIAL6 | close-up, cut off | Both stacks quoted verbatim, none chosen; 0.36 µm (pdk-04); bottom and cap labelled with both readings, `inferred` |
| 113 MM1 | full | m1.1, m1.2 0.140 µm, m1.4 0.030 µm (pdk-periph); layout illustrative |
| 114 MM1E | full | 0.140 µm (pdk-periph); vertical walls; the page defines no pdk-04 key, so no 0.36 µm in this caption |
| 115 NILD3 | full | "NILD3" permittivity 4.5, NILD3_C 0.030 µm (pdk-04); profile illustrative |
| 116 CMPM | full | 0.27 µm via-1 height (pdk-04); removal not public; pattern-density steps not drawn |
| 117 NCAPOX3 | full | 0.27 µm (pdk-04); cap of the order of 0.05–0.15 µm (txt-05, industry-typical); the cap setting the final thickness is the page's inference |

Built pages 108, 112, 114 and 115 shot at 1280 and 400 px: the figure follows the lead paragraph,
the caption's footnote markers render and link, prose follows.

### Gates

`check_steps`, `check_refs`, `check_machines`, `check_materials`, `check_masks`, `check_papers`,
`check_patents`, `check_filings`, `check_inforce`: rc 0. `gen_papers`, `gen_patents`, `gen_filings`,
`gen_index_links`, `gen_steps`, `gen_step_tables` `--check`: rc 0. `gen_figures --check`: 484 files,
0 problems; `--selftest` OK; `palette` 0 confusable pairs. `sphinx-build -W`: rc 0. No figure cites a
patent key; no spec text carries patent wording (the S8 pages' patent keys — pat-imp-amat,
pat-tiw-hitachi and others — are not used).

### Page points for the readability batch (page prose not changed)

* **112 lead vs the owner's rule for figures.** The TIAL6 page "describes the Ti/Al–Cu/TiW stack
  because the PDK's thickness matches it" (marked an inference) and its recipe gives "Cap, 300 Å" on
  that reading; the figure, per the undecided-stack rule, draws neither and labels both. 113's lead
  likewise opens with the TiW stack ("per the 2013 Cypress report …") before the TiN alternative.
* **114 cites no source for 0.36 µm.** "the spaces it opens — 0.14 µm wide and 0.36 µm deep" has
  no marker and the page defines no `pdk-04`; the number is pdk-04's metal-1 thickness.
* **Hole aspect ratio.** 107/108 give about 0.34 µm deep for a 0.17 µm hole (about 2:1); the drawing
  inherits S7's thin NILD2 and cannot show it (declared "not to scale").
* **"Standard contact bottom CD" sits in the PDK's laser-fuse table** (108 says so); 107–110 all
  read it as the general mcon bottom. Not a contradiction, but the whole taper reading rests on it.

### For the generator (not done here)

* The number lint counts the digit in a step code ("NILD3", "TIN2", "metal-1") as a number; S9's
  via levels will hit it on every label. Exempting all-caps step codes from the sheet (or
  hyphenated level names) would let notes name them.

## Review round (tmp review rd-figures-s8: approve with fixes, both parts)

* **M1** 089 caption: "lowest over the 5 V area on the left" dropped (no longer true). This removes
  one "5" from the figure's own caption (`check_preserved --base` merge-base: LOST '5' on 089, in
  the figure block only).
* **M2** 099 alt: "a V-shaped notch over the hole reaching most of the way down to the liner"; the
  caption says the deep notch comes from the drawn thickness, not from the page.
* **M3 (generator)** new token `max-film-traverse` (24 u): a right-hand leader may not run more than
  24 u inside ONE other film. The route chooser sends such a label over the surface
  (`_film_run`), and lint 18 refuses it (selftest: 30 u refused, 20 u accepted). Measured on all
  figures first: only poly-054/055/057/058 (resistor body through the gate film's rounded
  shoulder, 35 u) exceeded 19 u; they now rise over the surface as on main. 058 was the same
  regression, not listed in the review.
* **Number lint**: `IDENT_RE` as the review gives it; step and level codes (NILD3, TIN2, NILD3_C)
  are identifiers. Selftests: "polished at NILD3" needs no cite; "NILD3_C, 0.030 µm" and "TIN2
  liner, 20 nm" still do; a `reading` note "NILD3" does not trigger "not public first".
* **H1** CTME taper 19.5°: 12 u floor under the 24 u mouth, "bottom about half the top" is now
  true; series header corrected.
* **M5** 108 is now a close-up of the right-hand contact (the full-slice hole was about 5 px at
  400 px); 108, 109, 110 captions: "The hole is drawn much shallower than it is: … about 0.34 µm
  deep,[^pdk-04] about twice its width."
* **M6 (generator)** a cut close-up (negative `crop_depth`) draws a zigzag break along the bottom of
  the drawing, adds "; the lower part of the slice is not drawn" to its close-up line, and drops
  any film showing less than 2 u above the cut; the lint now asks for the exact phrase "the lower
  part of the slice is cut off" (selftest: "the resist is cut off" is refused). The label-column
  extension that could show more substrate is off for a cut figure.
* **M4, L2, L3** 112 caption: the page's TiW choice explained as the review words it (3 600 Å
  [cyp-qtp-113005] against 0.36 µm [pdk-04], "an inference"); "the colour the figure conventions
  use for every Ti, TiN and TiW film"; "records the change and gives the new metal 1 as".
  113, 114: "the page's text opens with the TiW stack of the 2013 report, and the figure, like
  the overview, draws neither".
* **M7** `anchor_y` 108 on the aluminium (mid-film): its dot is off the bottom film in 112–117.
  113 hides the NILD2 label in both panels (its leader paired with the aluminium's), declared.
* **L1** "Ti or Ti/TiN"; **L4** the cap keeps its note in the lower panels of 113 and 114.
* **114 and pdk-04**: page 114 cites the stack diagram under no key, so no citation was added; the
  figure carries no 0.36 µm. For the readability batch: "0.14 µm wide and 0.36 µm deep" on 114
  has no marker, and the source would need a footnote definition (pdk-04, already in the inventory).
* QA: all 11 S8 figures, poly-054/055/057/058 and mol-099 re-shot at desktop and 400 px in light
  and dark, every tile opened; built pages 108 and 112 at 1280 and 400 px.
