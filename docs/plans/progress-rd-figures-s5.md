# Progress — rd-figures-s5 (W1c, series S5: poly gate and poly resistors, steps 048–063)

Status: **complete**, awaiting review. 16 figures, one per step, on `topic/rd-figures-s5`.

## What was done

* `data/figures/series-poly.yaml`: the S5 series. Steps 002–034 are repeated from
  `series-wells.yaml` unchanged (same x layout, same material names), so the two series are one
  geometry.
* 16 figure specs `data/figures/poly-048-sagd.yaml` … `poly-063-iox45.yaml`, their SVGs and paste blocks.
  Each block is inserted after the first paragraph of "What this step is". None of the 16 pages
  has a `{dropdown}` straight after that paragraph, so the placement rule moves nothing.
* Commits: the series file first, then the figures in four groups (048–051, 052–055, 056–059, 060–063).

## The starting-state assumption (for the coordinator to reconcile with S3/S4)

S3/S4 (035–047) are being drawn on another branch. This series writes the result of 035–047 as
one change at step 047:

1. The pad oxide is stripped from both active areas.
2. A 5 u thermal gate oxide (`gox`, LVGOX) is grown on both. The slice is read as a 1.8 V NMOS
   beside a high-Vt 1.8 V PMOS, as in S2, so the GOX100 thick oxide and the ONO islands lie
   outside it.
3. The field oxide is etched down 17 u, from 29 u to 12 u above the silicon. P1M describes the
   gate as printing on a planar surface with only the small field-oxide step. The drawn step is
   still larger than the PDK's 0.07 µm, and no mechanism is drawn.

When S3/S4 merge, replace these three ops with that series' ops for 035–047. The `gox` id is used by the S5
specs (`hide_labels` on 063), so keep that id or rename it in `poly-063-iox45.yaml`.

## Geometry choices

* **Gate line.** x 14–38, over the NMOS active area. It was first drawn at 28–52, but there the
  conformal caps' steps notched the gate stack: the dilation model moves each film's top step
  in by the film thickness. The move fixed it.
* **Resistor body.** x 108–160, on the field oxide. It is a 300 Ω/sq P+ body (`rpm`), so:
  * RPM leaves an island over it (x 100–168, wider for rpm.3);
  * RRPM opens a window there;
  * URPM leaves resist over the whole slice, and UPRI reaches nothing. This follows the S2
    PWDE precedent.
* **Poly doping.** The generator's `dope` overlay clips to single-crystal silicon only, so
  P1I, PRI and UPRI are one-panel `no_drawn_change` figures with the beam. The captions say the
  doping is not drawn and why. On 050 and 053 a `Gate film` label override says the doping
  exists but is not drawn.
  **Tooling request:** a `dope` into `poly` (clipped to a named deposited layer) would let
  these steps show the n⁺ gate and the p-type body. This was not done here: it is a generator
  change.
* **Gate etch.** Three `etch` ops with no depth (cap oxide, nitride, poly, each stopping on the next
  material), so the field oxide under the resistor gaps is never etched. A single depth-limited
  etch would have left stringers where the conformal films are thicker.
* **BFR (060).** Written as an `etch` of depth 0 so that the step has a state of its own. The
  back of the wafer is not drawn. This gives a one-panel no-change figure.
* **IOX45 (063).** A `deposit` with `only_on: [si-sub, oxide-thermal, poly]` grows on the active areas and on the
  gate's poly sidewalls. It does not grow on the capped top. The resistor's sidewalls cannot be
  grown by this op, because the resistor stands on field oxide. They are left out, and the caption
  says so. **Tooling request:** a sidewall-only growth op.
* **Layers hidden or faded.** The wells and channel implants are hidden in every figure
  (`hide_layers`), and the caption says so. No page of the module discusses them. The liner
  oxide is faded, and the caption names it.
* **Labels hidden.** The field oxide is unlabelled wherever it is covered: its "over" leader
  cut a white line through the gate film and ran inside the resist. It is labelled in 048's
  before panel only. The silicon is unlabelled on 061–063, to stay within the six-label budget.
  The captions say so.

## Per-figure checks

All 16 were built with no LINT lines, and `--check` passes (212 files). Each figure was looked at
in the harness in light and dark, at desktop and 400 px. For each one I checked:

* the labels are beside their layers;
* no leader runs through a film;
* the highlight is on the changed surface;
* the dark mode keeps its boundaries;
* the panels line up.

| Figure | Notes / compromises |
|---|---|
| 048 SAGD | Dim "Gate film thickness 0.18 µm" [^pdk-03]. The caption states the starting-state reading and that the one-layer drawing is the page's inference [^pdk-04]. Field oxide labelled in the before panel only |
| 049 RPM | Island wider than the body (rpm.3 [^pdk-periph]). Resist note tagged *inferred* (the page infers that RPM protects the bodies) |
| 050 P1I | One panel. The beam lands everywhere except on the island. The caption gives "N+ doped gate poly" [^pdk-07], says the doping is not drawn and that the tilt is not public |
| 051 P1IS | The chemical oxide left by the clean is not drawn (the caption says so) |
| 052 RRPM | Reverse tone is the page's inference (mask table lists no reverse mask [^pdk-05]) |
| 053 PRI | One panel. The beam reaches the film only in the window. The resistor is read as 300 Ω/sq `res_high_po` [^pdk-07] |
| 054 PRIS | Two doping levels, not drawn |
| 055 URPM | Resist has no window in this slice. The resist note is tagged public ("opens only over the ultra-high-value resistors", the page's statement) |
| 056 UPRI | One panel. The beam is stopped by the resist over the whole slice (PWDE precedent) |
| 057 UPRIS | — |
| 058 GATENIT | Thickness and method not public. The caption repeats "poly cap after SPE" 0.2 µm [^pdk-03] as the page's reading |
| 059 POC | Thinness is inferred. The caps are not drawn in any ratio to each other or to the poly |
| 060 BFR | One panel, front unchanged |
| 061 P1M | Callout "Gate line — 0.150 µm drawn minimum" [^pdk-periph]. The gate resist is drawn thinner than the implant resists (30 u against 38 u), following the page's inference; the caption says so |
| 062 P1ME | Callouts "Gate" and "Resistor body". Vertical walls; gate oxide drawn intact (over-etch loss not public). The caption says the resist-on or hard-mask choice is not public |
| 063 IOX45 | Highlight limited to the active areas and the gate sidewalls. Gate-oxide label hidden in the after panel (its leader ran 21 u along the new oxide's edge); the caption says so |

Built pages 048, 053 and 062 were shot at 1280 px and 400 px. The figure sits after the lead
paragraph with its caption, and prose follows it.

## Gates

`check_steps`, `check_refs`, `check_machines`, `check_materials`, `check_masks`, `check_papers`,
`check_patents`, `check_filings` and `check_inforce` all pass. So do `gen_papers`, `gen_patents`,
`gen_filings`, `gen_index_links` and `gen_figures` `--check`, and `sphinx-build -W`.

`check_preserved.py --base 785e7e4b` reports only the figure blocks' own additions. There are no
deletions in `docs/steps` (insert-only). Note that `main` has moved since the branch point, so run
`check_preserved` against the merge base, not `main`.

## For the readability batch (page-internal points; page prose not changed)

* `048-sagd.md`, first paragraph: "The film is undoped as deposited" is stated as fact. The
  second paragraph calls the same description an inference ("… is the public basis for
  describing `SAGD` as one undoped amorphous layer (inference)"). The figure tags the label
  *inferred*.
* `061-p1m.md` describes the surface under the gate as planar, with only the 0.07 µm field-oxide step.
  The isolation and well figures (S1/S2) draw the field oxide standing well proud at 013–034. The
  step has to come down somewhere in 035–047 (S3/S4 should show where, if any page says so).
* `052-rrpm.md` leaves open whether RRPM opens the `urpm` bodies. `055-urpm.md` uses the
  reading that it does not. Both pages already say so and point at each other; this is noted only
  because the figures follow 055's reading (a single P+ body in the slice makes the question moot
  here).
* `063-iox45.md` says the oxide grows "on every exposed silicon surface". Its step 3 then
  distinguishes the resistor bodies ("less"). Not a contradiction, but the figure cannot draw
  the resistor sidewall oxide (see above).
