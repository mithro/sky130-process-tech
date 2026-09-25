# Progress — rd-figures-s7 (W1c, series S7: pre-metal dielectric, contact, silicide and local interconnect, steps 089–106)

Status: **complete**; review round done, awaiting re-review. 18 figures, one per step, on `topic/rd-figures-s7`.

## What was done

* **Generator** (`tools/gen_figures.py`), each change with a selftest:
  * `XSection.surface_ref`: a doped region with `follow: surface` is measured from the
    original silicon surface where a `react` product (the contact silicide) replaced the top of
    the silicon, so the N⁺ source/drain does not dip under the silicide disc. `react` was
    untested before; the selftest covers the disc (only where the liner touches silicon) and the
    doped band under it.
  * Lint 17 (two similar colours touching): only a *patterned* film has to be 10 u tall for its
    pattern to show. A plain film reads as its own inked colour at any thickness; the old rule
    fired on the 5 u spacer oxide under PSG as soon as the contact etch cut it into short
    pieces (a bounding-box effect).
  * Lint 18 (a leader through other materials / along an edge) counts a polygon only inside its
    own drawing's clip rectangle, as rule 16 already did. In a close-up the substrate polygon runs
    on below the crop into the next panel, and the after-panel over-run of 100 was reported as
    crossing it.
  * No existing SVG changed (`--check`: 440 files, 0 problems).
* **Series** `data/figures/series-mol.yaml`: ops 002–088 copied verbatim from
  `series-tips-sd.yaml` (same ids, same label text), then the module; the header records every
  choice. Materials as `tokens.json` names them: `psg` (dots), `oxide-dep` (cap oxide, NILD2),
  `barrier` (Ti/TiN liner and the TiN local interconnect), `silicide`, `tungsten`, `nitride`
  (LINT), `resist`.
* **18 specs** `data/figures/mol-089-psg.yaml` … `mol-106-cmpl.yaml`, SVGs and paste blocks, each
  block pasted after the first paragraph of "What this step is". No page in 089–106 has a
  `{dropdown}` right after that paragraph.
* Commits: series + generator fix; generator lint fixes; specs in four groups (089–092,
  093–096, 097–100, 101–106); QA round 1; placement (all 18 pages, insert-only); QA round 2
  (106); this file.

## Geometry and reading choices (all declared in the captions)

* **Slice.** Inherited exactly from S6 at step 088: the 5 V NMOS area (no gate), the field oxide
  with the P⁺ resistor read through its contact head (cap cut away at NPCME), the 1.8 V NMOS with
  its gate at x 236–260. P-well and NCHI hidden as in S5/S6.
* **PSG (089)** conformal 46 u: square dilation gives broad terraces, lowest over the 5 V area;
  the real (HDP) profile is not drawn, said so.
* **CMPP (090)** flat at 59 u, the height a nitride-capped poly line on the field oxide would
  have (field-oxide top 29 + poly 20 + nitride 10). The pages read the polish as stopping on the
  caps (inferred). In this slice the resistor head (no cap) stands higher than the capped 1.8 V
  gate, as it does with the PDK's heights, so a polish to the gate caps would cut the resistor;
  the drawn level leaves 5 u of glass over the head and more over the gate. The caption says so.
* **Holes (093–096)**: three, one per landing surface (5 V source/drain, resistor head in the
  nitride cut, 1.8 V source/drain beside the gate); x 20–60, 114–154, 184–224; illustrative
  positions. Walls drawn at the PDK's 10° "Licon1 etch angle"; widths not to scale (the 094 page
  itself says 10°, 0.17 µm and 0.08 µm do not reconcile over 0.5 µm). The diffusion holes clear
  the thin oxides (LICM1E lead: "which the etch must also clear"); the resistor hole is
  shallower. The resist stays on at 094 and is stripped at 095 (LICM1E lead: stripped at
  SACETCH / head of ALLY1, "on our reading"; SACETCH reading 3).
* **Liner (097)** Ti then TiN drawn as one 5 u barrier film; square dilation fills the narrow
  bottom corners of the hole, so the tungsten is narrower than a real plug; said so.
* **Silicide (098)** `react` under the liner, only where the liner touches silicon or poly: a
  disc at each hole bottom and nowhere else, tagged *inferred* (the CSIL page's contact-only
  reading from the PDK's unsilicided sheet resistances). Drawn at the minimum 5 u, sunk into the
  silicon it consumed; the N⁺ region keeps its depth.
* **Tungsten (099)** conformal 16 u (closes the 30 u lined opening); **WCMPLI (100)** flat at the
  cap-oxide top (69 u): flush plugs, liner off the field.
* **LI (101–103)** 8 u TiN, one pad per plug enclosing it (licon.4, li.5), illustrative; the
  pads are the same colour as the liner (both titanium films), said so on 101. LI1ME strips the
  resist in the same step (103 lead: "The resist is stripped afterwards").
* **LINT (104)** conformal 5 u nitride; **NILD2 (105)** conformal 24 u — square dilation merges
  the bumps over pads 42 u apart, so the top is flat except beyond the last pad; the caption says
  how far it copies the step is not drawn. **CMPL (106)** flat at 94 u.
* **Close-ups** 097–100 on x 170–268 (about 2.7×, the generator's footer prints it): the hole
  bottom is 16 u wide in the series, too small for the silicide disc and the liner at full-slice
  scale. The silicon label is hidden in the close-ups (all the silicon in view is under doped
  overlays, so the dot could only land on an overlay).
* **Labels hidden to keep leaders honest** (each declared in its caption): front-end films and
  doped regions except where a page's lead names them (089 before, 092, 093 before, 094, 095);
  the glass and cap oxide from 101 on; the plugs after 101; the liner under the tungsten blanket
  (099 after, 100); the local interconnect under the NILD2 (105 after, 106).
* **Spacer oxide** is drawn, not faded: fading it left white shapes that read as voids beside
  the holes (tried and reverted).

## Per-figure checks

All 18 build with no LINT line; `--check` 440 files, 0 problems. **Every figure was shot in the
harness at desktop and at 400 px in light and in dark, and every tile was opened** (round 2 after
the last spec change; 106 re-shot in all four after its last change). Checked for each: labels
beside their layers and readable at 400 px, no leader through a film or along an edge, no label
below its drawing, the highlight on the changed surface only, dark boundaries visible, panels
aligned, the picture agreeing with the lead above it.

| Figure | View | Notes / compromises |
|---|---|---|
| 089 PSG | full | Terraced top (dilation); "PSG K=3.9" (pdk-04); 0.6–0.9 µm as the page's inference (txt-05); spacer-oxide note shortened to "SPOX, step 080" by override |
| 090 CMPP | full | Polish level explained (see above); 0.5 µm (pdk-03) and 0.4299 µm (pdk-04) cited |
| 091 NCAPOX | full | Flat blanket; 0.2–0.3 µm inferred, not public |
| 092 RTAD2 | full, one panel | Both readings inferred; 0.1 µm junction (pdk-03) |
| 093 LICM1 | full | Three openings, illustrative; licon.1 (pdk-periph); highlight on the resist tops |
| 094 LICM1E | full | Two callouts from above (hole to the poly; contact hole with the 10° angle, pdk-03); resist kept on |
| 095 SACETCH | full | Draws reading 3 (strip), all three readings named; highlight where the resist was |
| 096 ALLY1 | full, one panel | skw-01 "H2 and forming gas alloy" |
| 097 TI/TIN1 | close-up | One film; 10–30 nm typical (koerner-1993); bottom corners filled by the drawing |
| 098 CSIL | close-up | Silicide labelled by a callout from above through the open hole; *inferred*; pdk-08 sheet resistances; no highlight (the disc is buried under the liner, so no surface changed) |
| 099 WDEP | close-up | 0.2–0.3 µm typical (txt-01); seam and nucleation layer not drawn |
| 100 WCMPLI | close-up | Plug flush; recess and erosion not drawn; licon.4, li.5 (pdk-periph) |
| 101 LITIN | full | 0.1 µm (pdk-04) in the label note; same colour as the liner, said so |
| 102 LI1M | full | Pads illustrative; li.5 0.080 µm (pdk-periph) |
| 103 LI1ME | full | Resist stripped in the step; 0.1 µm (pdk-04) |
| 104 LINIT | full | "LINT K=7.3", 0.075 µm (pdk-04) in the label note |
| 105 NILD2 | full | Nearly flat top (dilation), said so; "NILD2 K=4.05" (pdk-04); 0.5–0.7 µm inferred (txt-05) |
| 106 CMPL | full | 0.265 µm over the LI nitride (pdk-04) in the label; post-polish reading in the caption |

Built pages 089, 094, 098 and 104 were shot at 1280 px and 400 px: the figure follows the lead
paragraph, its caption renders with working footnote markers, and prose follows it.

## Gates

`check_steps`, `check_refs`, `check_machines`, `check_materials`, `check_masks`,
`check_papers`, `check_patents`, `check_filings`, `check_inforce`: rc 0. `gen_papers`,
`gen_patents`, `gen_filings`, `gen_index_links`, `gen_steps`, `gen_figures` `--check`: rc 0.
`gen_figures --selftest` OK, `palette` 0. `sphinx-build -W`: rc 0. `check_preserved.py`
(against `main`): only ADDED lines on the 18 pages (the blocks' own numbers, quotes, hedges,
markers and ids); `git diff main -- docs/steps`: 144 lines added, 0 deleted. No figure cites a
patent key.

## For the readability batch (page-internal points; page prose not changed)

* **094 vs 095 on the contact-bottom oxide.** The LICM1E lead says the etch reaches "the SPOX
  oxide over a source/drain or tap, which the etch must also clear", and its recipe step 4 has
  the over-etch clear it. The SACETCH page's reading 1 says that "on the reading of the SPOX and
  LICM1E pages" the plasma etch "is stopped on or in it rather than driven into the silicon".
  The two pages disagree on what LICM1E says; the figures follow LICM1E (cleared at 094).
* **Which caps the polish stops on (089, 090, 091, 100, 103).** With the PDK's heights (field-
  oxide top 0.3262 µm; field poly top 0.3262 + 0.18 = 0.5062 µm; gate cap top on active about
  0.38 µm), a polish that stopped on the caps of gates over active area would cut through every
  poly line on the field oxide. The only cap-stop level consistent with the stack diagram is the
  top of the caps over field poly: 0.5062 + 0.4299 = 0.9361 µm (the `li` bottom) leaves 0.4299 µm
  for the 0.2 µm cap plus about 0.23 µm of cap oxide, which matches NCAPOX's inferred
  0.2–0.3 µm (our arithmetic). The pages say "the tops of the caps over the densest poly arrays"
  (090) and "down to, or close to, the tops of the 0.2 µm gate caps" (089) without saying which;
  and 091, 100 and 103 say that on this reading "only the cap oxide separates" the LI from the
  gate caps, which holds for the caps at the polish level but not for gates on active area, which
  keep about 0.33 µm of PSG over them. The figures draw the field-poly-cap level and say why.
* **094's own reconciliation note** (10° against 0.17 → 0.08 µm over 0.5 µm) is on the page and
  repeated in the caption; nothing to change.
* **101 open question on the 1.0111 µm label** — not used by the figures.

## Follow-ups (not done here)

* Conformal films use square dilation, which gives terraced PSG, a nearly flat NILD2 and liners
  that fill a tapered hole's bottom corners. A round structuring element or a directional
  (per-column) deposit would give truer profiles; it changes every conformal film, so it was not
  done (S6 made the same call for spacers).
* The field-oxide height inherited from S4–S6 (29 u above the 1.8 V surface) drives the polish
  level; any later change to it must re-derive CMPP's level.

## Review round (tmp review rd-figures-s7: approve with fixes)

All items done.

* **H1:** 092 hides the N⁺ label (caption lists the doped regions as unlabelled). **Generator:**
  lint 18 now also measures risers: a leader may not rise more than `max-riser-traverse` (40 u)
  through more than `max-riser-layers` (3) other films, where a vertical line reads as a contact
  or a plug. Thresholds chosen from the existing series: every riser over 40 u on `main` crosses
  at most three layers (a resist block, a fill, or oxide over silicon; the longest, 111 u, is the
  iso liner up through the field oxide), while 092's crossed five. Selftest (stack refused, one
  fill accepted); every figure re-linted clean.
* **M1:** new figure field `routes` (`right | over | top | auto`) overrides a series route;
  097–099 give the liner and tungsten `right` (straight runs), 100 gives the tungsten `auto`
  (right in the blanket panel, over from the plug). **Generator:** an over-route riser keeps
  8 u off both drawing edges; new lint "dot within 3 u of its drawing's edge" (cross-sections
  only; a stack chart's dots sit on its bar by design), selftest. This also moved the dot of
  poly-048/049/050's gate film, which sat on the edge, 8 u in.
* **M2 (one rule, generator):** in a close-up a faded film keeps its own fill inside the dashed
  outline (class `ghost`, CSS emitted only where used); at full-slice scale it stays unfilled.
  Documented in figure-authoring.md and in the conventions page row. Regenerated the S6
  close-ups (065, 066, 069, 075–077, 080, 086, 088), which carry the faded trench liner.
* **M3 (generator):** a close-up emulates its series on a grid finer by the enlargement
  (dx = 0.5 / ceil(zoom)), so tapered walls are straight lines; the S6 close-ups regenerate with
  it (their sloped trench and spacer edges also smooth). Build time for a close-up ~14 s.
* **M4:** 089 before drops the spacer-oxide label; 095 after drops the glass label; both declared.
* **M5:** 091, 100 and 103 captions state the polish-level drawing (glass stays over the gate).
* **M6:** "of the order of" restored on 097 and 099 (099 quotes it, so the caption does not
  echo the lead); "about" dropped from 095's 0.08 µm.
* **Lows:** L1 "p-type poly, resistor head" on 089 and 095, 094 callout "Poly contact hole";
  L2 no "dark" wording (captions and alts say purple / same colour); L3 header says 16 u; L4 as
  L1; L5 104 hides the LI label; L6 098 caption says nothing is traced; L7 the right-hand LI pad
  now runs on over the gate (x 178–250), so NILD2 is flat to the edge (102, 103, 105, 106 texts
  updated); L8 noted below; L9 the silicide note drops "we infer" (the tag says it).
* QA: all 18 re-shot in light and dark at desktop and 400 px after the last change, every tile
  opened, plus the regenerated S6 close-ups 065, 069, 086 and poly-048; built pages 092, 097,
  099 at 1280 and 400 px.

## For the generator before S8 (ruling: acceptable as declared for S7 only)

* **Conformal deposit.** `deposit` dilates with a square element, so a film over a step keeps
  square corners, fills the bottom corners of a tapered hole (097–100: the liner) and merges
  bumps within 2t into terraces (089 PSG, 105 NILD2). It should dilate with a round (or
  chamfered) element of radius t, and, inside a hole, grow normal to each wall, so a liner has
  even thickness on a sloped wall and leaves a rounded, open bottom; vias and plugs of S8/S9 will
  otherwise inherit narrowed plugs.
* **PSG and ILD profiles.** A gap-filling glass should be emulated by a deposit that fills gaps
  up to an aspect ratio and then copies the surface with a smoothing length (HDP: peaked profile
  over narrow lines, flat over wide ones), instead of square dilation's terraces.
* **Etch walls.** With the finer close-up grid, taper walls render straight; a dedicated
  straight-edge polygon for `taper_deg` walls would make full-slice walls exact too.
* **Silicide against tungsten** (review L8): ΔE 2.1/4.2 for deuteranopes, told apart only by
  tungsten's cross-hatch. They never touch in S7 (the liner is between); check it if a later
  plug sits directly on a silicide.
