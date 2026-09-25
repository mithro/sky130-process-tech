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

## Starting state (superseded; see "Review round" below)

The first version assumed its own state at 047. It now continues exactly from `series-gates.yaml`
(S4, merged on main); see below.

## Geometry choices (first version; see "Review round" for what changed)

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

## Review round (tmp review rd-figures-s5: approve with fixes)

Done, in the coordinator's order, one commit each:

* **H1.** The series note on the gate film is neutral. "Undoped as deposited" (inferred) is
  on 048/049 only, and each later panel's labels state the doping the page gives.
* **H3 (generator).** A leader may not run along the accent trace of a highlight: `_edge_run`
  and SVG lint rule 18 count the trace as an edge, and there is a selftest case.
  `edge-clearance` is now 6 u (was 4). Every series was re-linted clean: the only other
  figure that changed is `iso-013-ns19` (one dot moved 1.5 u).
* **Mediums.**
  * The 063 caption now says the oxide is drawn equally thick everywhere although the page
    varies it, and that the bird's beak is not drawn.
  * 048 and 051 now declare their hidden labels.
  * The silicon is labelled on 061–063.
  * 048's dimension is clear of the shoulder.
  * The field-oxide clause reads "the oxide-filled trench in the middle".
* **Ruling (a) (generator).** `dope` takes `host: <film id>`. The overlay fills that film,
  through its whole thickness, only where the film still is, and follows later etches. The
  film's own label goes where no overlay covers it, in both the right and the over route.
  * Lint: a host not deposited earlier in the series, or absent everywhere the overlay is
    made.
  * Two selftests.
  * `sd-n` and `sd-p` are reused over poly, and their legend labels now name that use.
  * S5 draws the n-type gate film (P1I) and the p-type resistor body (PRI). 050 and 053 are
    now two panels.
  * Every caption from 050 on says that the colour marks the type of doping, not a depth
    profile.
* **Ruling (b).** The re-oxidation of the resistor's sidewalls remains a recorded follow-up.
  It needs a `beside:` option on `deposit`.
* **Series start (coordinator decision on H2).** Steps 002–047 are now `series-gates.yaml`'s
  ops verbatim. The only change is the trench oxide's label title, "Field oxide" for "Fill
  oxide", as this module's pages say. The slice is:
  * a 5 V NMOS on the left, keeping the thick `gox`;
  * a 1.8 V NMOS on the right, with `thinox` and NCHI;
  * the P-well under both;
  * field oxide still proud.

  The gate line is now x 236–260 over the 1.8 V area, and the resistor is unchanged on the
  field. 048's caption says the page's nearly planar surface is not drawn, because no page
  says where the step comes down. The figures hide the P-well and NCHI, and the captions say
  so.

Labels hidden to keep leaders honest (each one declared in its caption):
* the thick gate oxide from 049 on (its leader would cross the whole slice);
* the undoped body under the RPM island (050 after, 051 before);
* the p-type body under full resist (055 after, 056, 057 before) and under the P1M line
  (061 after, 062 before);
* the thin gate oxide in 063 after.

The n-type gate film's leader in 062 before and 063 rises through the gate's caps (short).
That compromise is accepted.

Follow-ups: `beside:` for the sidewall oxide (ruling b); a highlight clipped to changed
surfaces (review L1).

## After the rebase onto main (S3/S4 generator rules merged)

The combined generator flagged only the S5 figures. Every other series (iso, wells, sonos,
gates, the history chain, the overview charts) builds byte-identically and lints clean. Two
rules from S3/S4 bit S5:
* labels may sit at most 12 u below their drawing;
* two gutter legs may run side by side for at most 48 u.

Fixes, all in the S5 series and specs (no generator change):
* **Shorter series notes:**
  * "gate implant, step 050";
  * "resistor implant, step 053";
  * "GATENIT, step 058";
  * "POC, step 059";
  * the thin oxide's "LVGOX, step 047", the one label text changed in the ops copied from
    `series-gates.yaml`, noted in the header.

  The dropped words (the PDK quotation, "thickness not public") are all in the captions.
* **Thin gate oxide label** hidden from 051 on (unchanged context). Its captions now say
  "both gate oxides are drawn but not labelled".
* **The n-type film's `anchor_y`** is removed. It is no longer needed now that the thin-oxide
  label is gone.
