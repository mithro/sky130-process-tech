# Progress — rd-figures-s10 (W1c, S10 MiM capacitors: steps 135–140 and 150–153)

Branch `topic/rd-figures-s10`. Task: one figure per step for the two MiM capacitor modules
(135–138, 150–153) and the metal-3 pattern that follows the first (139–140), continuing the S9a
series `data/figures/series-beol.yaml`.

## Decisions

* **Where the ops go.** In `series-beol.yaml` itself, as its header and the authoring guide
  planned ("the MiM capacitor steps go between them as plain ops"): plain ops for 135–138 and
  150–153, `use: metal-pattern` for 139–140. One back-end geometry; S9b continues after 153.
* **Two optional template parameters**, both defaulting to the old value (no earlier figure
  changes; `--check` clean before any S10 figure): `metal-pattern.etch_materials` (default
  `[barrier, aluminium]`) so that MM3E also removes the capacitor dielectric left on the metal
  outside the resist, and `via-hole.etch_materials` (default `[oxide-dep]`) so that a via onto a
  metal-3 line etches through that dielectric to the cap.
* **The slice holds a capacitor.** Metal 3 is patterned into a wiring line over the via-2 plug
  (x 14–76) and a capacitor bottom plate (x 100 on, past the edge); the top plate runs from
  x 130 (enclosure 30 u, illustrative; the `capm` enclosure value is not published).
* **Thicknesses.** Dielectric 3 u (`thin_ok`, close-ups only, 2.7×), plate 8 u (thicker than the
  5 u metal cap: the pages read the plate as about 0.1 µm, several times the 300 Å TiW cap of the
  2013 stack, and the dielectric as 18–33 nm; all not public). Captions say they are not drawn
  to scale.
* **CAPME stops on the dielectric** (the 138 and 153 pages' reading); no loss into it is drawn.
* **150–153 drawn now, not left for S9b.** The S9a templates instantiate cleanly for 141–149
  (`imd` for NILD5, `via-hole` and `via-plug` for via 3, `metal-stack` for metal 4), so they
  are in the series as unlabelled context: NILD5 polished to 26 u over the metal-3 tops with
  its cap (0.39 µm against via 2's 0.42 µm and 28 u, pdk-04 on the 141/145 pages), via 3 on
  the wiring line and on the top plate, metal 4 as thick as metal 3 (both 0.845 µm). The
  150–153 close-ups show only x 76–176 above 252 u, so they depend on 141–148 only through
  the metal-4 heights. S9b owns 141–149 and may change them (then rebuild 150–153 and move
  their `crop_depth`). Written in the series header and in `figure-authoring.md` ("Drawing
  the next groups", item 1).
* **Close-ups, not full slices.** The dielectric and the plate are too thin to read at
  full-slice scale; every figure is a 2.68× close-up of the plate edge: window `[66, 166]`
  for 135–140 (the edge of the capacitor and, from 139, the end of the wiring line) and
  `[76, 176]` for 150–153 (the via-3 plug at x 52–72 would leave a sliver at the left of
  `[66, 166]`). Cuts at 172 u (−461) and 252 u (−675): with shallower cuts the label column
  ran below the drawing.
* **Labels.** The dielectric: "not public; read here as a PECVD oxynitride", `inferred`
  (135: "described in this reference as a silicon oxynitride (inference)"; 150: "no public
  source describes SKY130's capacitor dielectric … this reference reads the film as a PECVD
  silicon oxynitride"). The plate: "TiW on this reference's reading", `inferred`. The metal cap
  and bottom film keep the S9a wording ("TiW or Ti/TiN — see the overview", "Ti or TiW — see
  the overview"); a panel override keeps the cap note where the noted-label budget dropped it
  (138, 140, 153). No label carries a number.

## Figures

All ten: lint clean, looked at in the harness at 1280 and 400 px in light and dark.

* **135 CAPILD**: blanket dielectric on the blanket metal 3. Caption: material not named by
  the PDK, the page's inference; thickness not public, 18–33 nm the page's arithmetic
  (pdk-07); drawn thicker in proportion. Aluminium, cap, dielectric labelled; oxides and
  bottom film declared unlabelled.
* **136 CAPTIW1**: blanket plate film. Caption: 5.8 Ω/sq (pdk-07), TiW an inference, ~0.1 µm
  the page's arithmetic, several times the 300 Å TiW cap (cyp-qtp-113005) and the dielectric;
  drawn thicker than cap and dielectric, not to scale. Aluminium unlabelled in the upper panel
  (the label column otherwise ran below the drawing).
* **137 CAPM**: resist block from x 130. Caption: CAPMCD 2 µm, CAPMCDSP 0.84 µm (pdk-03);
  plate position illustrative.
* **138 CAPME**: plate etched outside the resist, stopping on the dielectric; resist stripped.
  Caption: stop vs through-etch not public, the page describes the stop, the PDK schematic
  draws the dielectric only under the plate (pdk-07); no dielectric loss drawn.
* **139 MM3**: resist over the wiring line and over the whole plate, reaching beyond it.
  Caption: m3.1/m3.2 0.300 µm, enclosure value not published (pdk-periph); 0.845 µm (pdk-04).
* **140 MM3E**: dielectric outside the resist, then the stack, etched to the cap oxide;
  bottom plate and line end left. Caption says the dielectric stays on the metal under the
  resist on this drawing, that the page does not discuss it, and that the PDK schematic draws
  it only under the plate. The cap oxide is not labelled (its label ran below the drawing and
  the figure hit 810 u); declared.
* **150 CAPILD2**, **151 CAPTIW2**, **152 CAP2M**, **153 CAP2ME**: the same four figures one
  level up, with each page's own wording (150: the step-list name is not evidence of a
  chemistry, steps-sheet; 151: 5.8 Ω/sq, same as the first plate; 152: no `cap2m` rules,
  geometry read as `capm`'s 2 µm / 0.84 µm, pdk-03, inference; 153: as 138).

Compromises: the dielectric (3 u) is drawn about a third of the plate (8 u) and the plate
about a fifth of the metal (42 u); on the pages' estimates (not public) the dielectric is a
few times thinner than the plate and the plate about an eighth of the metal. The captions say
neither is to scale; none states a drawn ratio. Blanket-film figures (135, 136, 150, 151) are
necessarily just flat bands.

## Checks

`gen_figures.py --check` 592 files, 0 problems (552 before, unchanged); `--selftest` OK;
`palette` 0 pairs; all nine checkers and the four gen `--check`s pass; `sphinx-build -W`
passes; `check_preserved` on the ten pages: ADDED only (80 lines added, 0 deleted). Built
pages 138, 140 and 152 shot at 1280 and 400 px: figure after the lead paragraph, prose after
the caption.

## For the owner / the readability batch (page points, not fixed here)

* The 140 page reads MM3E as removing "whatever remains of the CAPILD dielectric outside the
  capacitor plates", but under the MM3 resist nothing is etched, so on the 138 page's
  stop-on-dielectric reading the dielectric stays on every metal-3 shape (on the bottom plate
  around the top plate and on the wiring). The pages do not say so; the 145 page gives the
  via-3 floors as the metal-3 cap and the top plate, without the dielectric on the cap. The
  140 figure draws what the sequence implies and says the page does not discuss it.
* The 150 and 135 pages word the dielectric differently (135: "described in this reference as
  a silicon oxynitride (inference)"; 150: "no public source describes … the public record does
  not single that material out"); the labels use the common "not public; read here as a PECVD
  oxynitride".

## Left

* Nothing for 135–140, 150–153. S9b: 141–149 and 154–163 (see the guide, item 1).
