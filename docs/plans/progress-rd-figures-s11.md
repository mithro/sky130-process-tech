# Progress: rd-figures-s11 (W1c, the last series: S11 passivation and pad, 164–170, and the 171 test chain)

Branch `topic/rd-figures-s11`, from `main` at "S9b figures merged".

## Status

Done. Every step page, 001–171, now has a figure.

* `data/figures/series-passivation.yaml`: `base: series-beol.yaml`, so it continues exactly
  from the S9b end state (after MM5E, 163), plus seven plain ops, 164–170. No earlier series
  or figure changed (`--check`: 700 generated files, 0 problems).
* Figure specs `pass-164-nfusox` … `pass-170-ally` (cross-sections) and `tool-171-hpetest`
  (a `chain`), generated, linted clean, pasted after the first paragraph of "What this step
  is" on each page. `check_preserved.py` on the eight pages: ADDED entries only; `git diff
  --numstat`: 8 added, 0 deleted per page.
* Checkers: check_steps, check_refs, check_machines, check_materials, check_masks,
  check_papers, check_patents, check_filings, check_inforce: 0 problems. gen_papers,
  gen_patents, gen_filings, gen_index_links `--check`: clean. `sphinx-build -W`: exit 0.
* QA: every figure in the harness at 1280 and 400 px, light and dark, every tile looked at;
  built pages 165, 169 and 171 at 1280 and 400 px (figure after the lead, prose after the
  caption).

## Geometry (the series header says the same)

* Scale: metal 5 is 63 u for the PDK's 1.26 µm (50 u/µm), so the passivation is drawn on
  that scale: TOPOX 5 u (0.09 µm would be 4.5 u; 5 u is the minimum film), TOPNIT 27 u
  (0.54 µm). Both conformal (the default profile): one thickness on the sidewall, where the
  diagram gives 0.070 µm and 0.4223 µm. The captions say so.
* The 80 u metal-5 space stays open after both films (16 u left).
* Cut: `crop_depth: -325` for all seven cross-sections, inside the NILD6 oxide over the
  second capacitor plate (the S9b note: between 319 and 330 u). The captions say "the
  drawing starts inside the oxide under metal 5". A cut at 300 u (inside metal 4) was tried
  and rejected: it only moved the label-column lint.
* NSM/NSME (165–166): the `nsm` ring is at least 3 µm wide at the die edge and at least
  1.000 µm from every metal (nsm.1, nsm.3), so it cannot fall in this slice of wiring, and
  how deep NSME goes is not public (three readings on the 166 page). So the NSM resist covers
  the whole slice, NSME is drawn as the strip only, and both captions say the opening is
  outside the slice and not drawn. Report D's "scribe opening" is therefore not drawn: doing
  so would need a die-edge series (seal-ring diffusion, the whole dielectric column) and a
  depth that is not public.
* PDM/PDME (168–169): the left-hand metal-5 shape (x 10–94) stands for a pad (illustrative,
  said in the captions); opening x 26–78, 16 u enclosure each side, films continuing over the
  metal's edge (the "glass cut" of pdk-04). The etch removes nitride and oxide and stops on
  the metal-5 cap film, which is drawn left in place: whether the TiW cap (the page's
  inference) is removed from the pad is not public. The 169 "after" panel marks the opening
  with a callout ("Opened pad — not public whether its cap film stays").
* ALLY (170): `op: anneal`, a one-panel `no_drawn_change` figure.
* Not drawn: the polyimide ("PI1" on pdk-04; whether a lot receives it is not public, said in
  the 167 caption); the thinner passivation beside the metal that the 164/167 pages read in
  the diagram's 0.3777 µm (said in the 167 caption).

## Per figure

| Figure | Checked | Compromises |
|---|---|---|
| 164 NFUSOX | numbers 0.09/0.070/1.26 µm with pdk-04; "an inference" for TOPOX; 0.8:1 drawn space (80 u × 63 u) matches the page's arithmetic | cap oxide and, in the after panel, aluminium unlabelled (said in the caption); TOPOX and the cap oxide share the oxide colour, the highlight marks the new film |
| 165 NSM | nsm.1, nsm.3 (pdk-periph); resist thickness "not public" | the opening is not in the slice (see above) |
| 166 NSME | three depth readings repeated as the page gives them; the thin oxide over the metal untouched, as the page requires | the after panel differs from the before only by the stripped resist |
| 167 NTSD | 0.54/0.4223/1.26 µm (pdk-04); "between 0.54 µm and 0.9 µm" and the three Cypress keys; PECVD as inference | metal cap unlabelled in the after panel (said) |
| 168 PDM | 60 µm × 70 µm, 2.7 µm (pdk-io-gpiov2); `PDMCD` 2 µm (pdk-03); resist thickness not public | pad and opening sizes not to scale (said) |
| 169 PDME | 0.54 + 0.09 over 1.26 µm (pdk-04); thicker Cypress nitride (three keys); TiW cap an inference, removal not public | walls vertical; positions illustrative (said) |
| 170 ALLY | 350–450 °C as the industry's typical range (txt-02); ambient, temperature, time, hydrogen source not public | none |
| 171 chain | blocks in the lead's order: wafer → prober → tester → results; branches: probe card (typical), HP 4062UX (skw-01, inferred), PDK e-test limits (pdk-07, public) | see the generator notes below |

No figure uses a patent key or wording: the in-force GlobalFoundries edge-seal and TSMC
test-line notes on 165–168 and 171 are not drawn from; `check_inforce.py` and the
generator's screen are clean.

## Generator notes (not changed here; for the owner)

* `chain`: when a branch box is taller than its main box, the downward arrow starts below the
  branch box, leaving a gap under the main box (seen before the branch notes were shortened
  to fit). The footer sits 12 u under the last box, which reads tight. Both apply to
  `history-lineage` too.
* The caption-echo lint fires only once the block is in the page (as S9b noted): 169 and
  170 were reworded after pasting.

## Page points (not fixed; content, for the owner)

* 167, 168, 169, 170: "7000–9000 Å" (or "0.7–0.9 µm") for the Cypress nitrides, but the
  S8TNV-5R report gives "7000 +/- 2000A", i.e. 0.5–0.9 µm; the range the pages quote starts
  at its nominal, not its lower limit (167 lead and "How it is typically performed" item 4; 168 "Step
  category"; 169 lead; 170 lead). 169's Open questions says "0.7 ± 0.2 µm" correctly.
* Arithmetic checked and correct: 165 k₁ ≈ 4.9, 168 k₁ ≈ 2.1, 166 0.09 mm² / 18.7 mm² ≈
  0.5 %, 167 78 %, 164 0.8:1, 164 5.3711 + 0.3777 = 11.8834 − 6.1346.

## What report D's remaining families would need

Every step page now has a figure (report D §2 (a) done, with B1 and E1). Left:

* **(d) Machine block-chains (30 machine pages; P2).** The `chain` kind is enough. Each needs:
  the blocks the page's own "What the machine class is and how it works" names, in its order
  (e.g. the high-current implanter's "ion source, extraction, analysing magnet, acceleration,
  scanning, dosimetry and an end station"); one spec per page, id `tool-<machine>`; basis
  `typical` for generic blocks, `public`/`inferred` with `skw-01` only where the page says
  what SkyWater lists; branches only for a side input the text names. Class templates (report
  D: implanters, furnaces, etchers, CVD/PVD, steppers and track, CMP, wet, metrology, tester)
  would be copy-and-edit specs, not generator templates. Placement: after the first paragraph
  of the first H2; `check_machines.py` forbids new headings. `tool-171-hpetest` is the model.
* **(c) C2 mask derivation chains (36 mask pages).** `chain` again: drawn layers → mask layer
  (GDS number, from pdk-06) → plate → resist → the steps that use it, with `inferred` on every
  link the page marks as inference (e.g. `masks/fom.md`). Report D's second mask figure, the
  cross-section after develop, is already on the step page of each mask step and could be
  re-used by id rather than regenerated. C1 (the generic coat → expose → develop → transfer →
  strip chain) is one spec on the lithography category page. C3 (masks along the flow strip)
  needs a `flowmap` option to mark mask steps; the data are in the step list.
* **F7 category sketches (5; P3).** Generic mechanism schematics, all `typical`: lithography
  (resolution/depth of focus), CMP (dishing/erosion), etch (anisotropy/over-etch), deposition
  (conformality), implant (tilt/shadowing). The deposition and etch ones can be `xsection`
  specs on a small generic series (the `profile: conformal|gapfill` and `taper_deg` machinery
  exists); the lithography and implant ones need a new kind or a small schematic series with
  no SKY130 numbers. Each must say "typical" in its caption and carry no SKY130 value.
* **B2, E2, E3.** B2: the module strip as a locator (a `flowmap` option to highlight one
  module). E2: the front-end depth ladder (`stack` kind, but its trench depth is "our
  reading", which the `stack` lint refuses; it needs a non-to-scale variant or to drop that
  row). E3: the two Cypress metal-1 stacks side by side (two `stack` specs, or a side-by-side
  option).
