(mask-fom)=
# FOM — Field Oxide

The field-oxide mask is the {term}`reticle` that draws the active
islands of SKY130 — every transistor source, drain and channel, every
well and substrate tap — and, by leaving them out, every isolation
trench between them. On the {ref}`FOM <step-004>` page's reading it is
the first lithography of the flow.

| | FOM — Field Oxide |
|---|---|
| Mask step | {ref}`FOM <step-004>`, step 4 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Field Oxide", `FOM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cfom` mask 23:0, "Field oxide mask"; `cfom` drawing 22:20, mask add 22:21, mask drop 22:22, waffle drop 22:24; `fom` dummy 22:23[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `diff` drawing 65:20, "Active (diffusion) area (type opposite of well/substrate underneath)", and `tap` drawing 65:44, "Active (diffusion) area (type equal to the well/substrate underneath) (i.e., N+ and P+)" — the pairing is an inference of the step page[^pdk-06] |
| Minimum CD, feature / space | `FOMCD` 0.14 / `FOMCDSP` 0.27[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist stays over the drawn active areas, which with a positive resist would put the absorber over `diff` and `tap` and leave the field clear (inference); the step page leaves the tone open. |
| Exposure class | KrF (248 nm), an inference on the step page from the 0.150 µm active width, with i-line as the fallback it names "if the layer were relaxed"; no public source names the tool ({ref}`machine-duv-krf-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `020`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 3 steps; see {ref}`Steps that use this mask <mask-fom-steps>` |

:::{seealso}
How the
step is performed is on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.
:::

## What the mask defines

On the {ref}`FOM <step-004>` page's reading, the resist printed through the mask stays
over the future active areas, {ref}`STINITE <step-005>` opens the
nitride and pad oxide around them and {ref}`STIE <step-006>` cuts the
{term}`STI` trenches into the silicon. Because nothing is on the wafer
before it, the step page also reads it as the level that every later
mask aligns to.

The periphery rules give the function of the `diff` and `tap` rule set
as "Defines active regions and contacts to substrate".[^pdk-periph]
The two drawn layers differ only in doping type relative to the well
beneath: `diff` is active "(type opposite of well/substrate
underneath)", the transistor source and drain, and `tap` "(type equal
to the well/substrate underneath)", the well and substrate
contacts.[^pdk-06] Both are silicon that the trench etch must not
touch, so on the {ref}`FOM <step-004>` page's reading one plate carries
them together, and what separates them later is the source/drain
implant masks, not this one.

The mask therefore sets the drawn
transistor width (difftap.1, 0.150 µm, and the minimum channel width
difftap.2, 0.420 µm, flag P) and the narrowest isolation (difftap.3,
0.270 µm between diff and diff, tap and tap, or non-abutting diff and
tap).[^pdk-periph]

The PDK's mask generation table, Table F2b, marks the `FOM` column:[^pdk-06]

* `C`
  ("CREATED") in 61 of its 80 device rows — the diffusion resistors and
  the isolated P-well resistor, every transistor and varactor, the diodes
  with a diffused junction, the bipolar transistors and the ESD
  transistors
* `+`, "Layer allowed to overlap", in 15 rows: the LI
  resistor, the MiM and VPP capacitors, the three inductors and eight
  diodes formed between wells, deep N-well and substrate

The
four rows marked `-`, "Layer not created for the device", are the n+
and p+ poly resistors and the two metal fuses.[^pdk-06] No other column
of the table has as many `C` marks; on the table's evidence almost every
device of the process has active area on this plate (our grouping and
reading of the table).

The mask also carries shapes that belong to no device. Table C3 of the
*Layers Reference* defines `fom_waffles` as "fom.mk with dimensions (um
x um): 0.5 x 0.5, 1.5 x 1.5, 2.5 x 2.5 and 4.08 x 4.08".[^pdk-06] Rule x.15a,
which confines mask and waffle-drop layers to test modules, seal ring
and frame, makes an exception: "FOM/P1M/Metal waffle drop are allowed
inside the die" (flag P).[^pdk-periph] The
{ref}`FOM <step-004>` page reads the "waffles" as dummy active squares
that keep the {term}`CMP` of {ref}`CMPNIT <step-012>` uniform.

Tian,
Tang and Wong formulated dummy-feature placement for the STI polish,
which removes two materials at different rates and so needs its own
model of how topography follows {term}`pattern density`;[^tian-2002]
Kahng and Samadi survey fill synthesis more generally.[^kahng-2008]

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `cfom` five purposes: `mask` at 23:0 ("Field
oxide mask") and `drawing` 22:20, `mask add` 22:21, `mask drop` 22:22
and `waffle drop` 22:24 on a different layer number; `fom` has a
`dummy` purpose at 22:23 with no description.[^pdk-06] The drawn layers
are `diff` 65:20 and `tap` 65:44, with further `diff` purposes
(`resistor` 65:13, `high voltage` 65:8 and others).[^pdk-06]

The pairing
of `cfom` with `diff` and `tap` is the step page's inference; the PDK
publishes no operation from the drawn layers to the plate. It does name
the plate data in two definitions of Table C3: `fomDmy_keepout_1` is
"(diff.dg OR tap.dg OR poly.dg OR pwell resistor OR pad OR cfom.dg OR
cfom.mk OR PhotoArray OR cp1m.mk)", and `Diecut_pmm` is "areaid.dt NOT
(cfom.wp OR cp1m.wp OR cmm1.wp OR cmm2.wp)".[^pdk-06]

We read the
suffixes `.dg`, `.mk` and `.wp` as the drawing, mask and waffle-drop
purposes (inference from the purpose names; the table does not expand
them), so the fill keep-out is built from the drawn active and the
`cfom` data together.

Rule x.9 confines "Shapes on maskAdd or maskDrop layers ("serifs")" to
the core, and names `cfom` among its exemptions: "cfom md/mp inside
"advSeal_6um\* OR cuPillarAdvSeal_6um\*" pcell".[^pdk-periph] The `cfom`
add and drop purposes are therefore used, at least in those seal-ring
cells (our reading of "md/mp" as mask drop and mask add); the PDK does
not say what they add or remove elsewhere. Table 7 of [*Criteria &
Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) has two sizing rows for an emitter, "pnp_emitter sizing
(S8P GSMC flow)" 0.05 (`PnpEmitterSzGSMC`) and "pnp_emitter sizing
(other flows)" 0.03 (`PnpEmitterSz`), without saying on which layer the
sizing acts.[^pdk-03]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `FOM` the site renders layers 65:20 (`diff`)
and 65:44 (`tap`) together with 23:28, which it lists as a fill layer,
with no Boolean expression, on all eight runs.[^mask-renders] Its mask record gives the
mask-level layer 23:0 and the note "FOM = diff OR tap (OR grown pnp
emitter)".[^mask-renders]

Layer 23:28 is not in
`gds_layers.csv`,[^pdk-06] the render job lists no emitter term, and
the site gives no source for the note. The choice of layers and the
note are one public derivation from the drawn data, not SkyWater's
mask-generation recipe ({ref}`masks-derivations`); they agree with the
step page's pairing, but both start from the same public files, so the
agreement is not independent confirmation.

All 40 rendered dies of every run carry shapes on these layers, and the
count says nothing about how many projects draw active area.[^mask-renders] Every die
carries at least 1 438 841 shapes, and the per-die minimum on each run
lies between 1 438 841 and 1 579 678.[^mask-renders] Unlike the `DNM`
counts, these rarely repeat — no two dies share a count on MPW-1, MPW-4
or MPW-8, and on no run do more than seven dies have a count that
another die shares — so they vary with the projects.

We read the large
minimum as fill and structures that every die of these runs carries,
which the site counts together with the drawn active (inference; the
site does not break the count down by layer).[^mask-renders] On MPW-1
one die accounts for 99 % of the run's `FOM` shapes, so the site's run
totals are not comparable between runs ({ref}`masks-renders`).

The site
states the limits of its images: "These are renders of *drawn* data, not
photomask artwork: reticle pitch, 4x reduction, mirroring and the frame
features the fab adds are not modelled."[^mask-renders] Its metadata
carries no plate ID, so a render is tied to a plate in the process-steps
sheet only by the acronym `FOM`, and the MPW-4 renders come from a
different reticle set from the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a `FOM` plate
as existing on all eight MPW runs, with the plate number `020` on each
and no "Info" note.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab, which
the renders site calls the run's reticle set
({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA020A` |
| MPW-2 | `5CS8007AC` | `S8007AA020A` |
| MPW-3 | `5CS8008AC` | `S8008AA020A` |
| MPW-4 | `5CS8018AC` | `S8018AA020A` |
| MPW-5 | `5CS8011AC` | `S8011AA020A` |
| MPW-6 | `5CS8014AC` | `S8014AA020A` |
| MPW-7 | `5CS8016AC` | `S8016AA020A` |
| MPW-8 | `5CS8017AC` | `S8017AA020A` |

* **Plate number.** `020` is low, but the numbers do not follow process
  order: `NSM` (step 165) is `007` and `NWM` (step 17) `010`, both
  below the first mask of the flow.[^steps-sheet] The sheet does not say what
  they encode, so no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `FOM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber, phase-shift type or reduction ratio; 4× is the ITRS
  2001 mask magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`, whose plates no public
  source lists ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

### Exposure class

The {ref}`FOM <step-004>` page puts the 0.150 µm
active line at {math}`k_1 \approx 0.25` on an i-line lens of NA 0.6 and
at about 0.4 on a KrF lens of NA 0.6–0.7, and infers a 248 nm level,
with i-line as the fallback "if the layer were relaxed". The
{ref}`KrF stepper <machine-duv-krf-stepper>` page lists it there and
the {ref}`i-line stepper <machine-i-line-stepper>` page as an
alternative. ASML's PAS 5500/750E, introduced in 2000, "achieves 130 nm
resolution while using standard 248 nm light".[^asml-750e] SkyWater
lists "ASML DUV stepper" and "ASML DUV scanner" among its tools but
assigns no layer to them.[^skw-01]

### Mask errors

Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns", and that
dark-field spaces are more sensitive than light-field lines.[^wong-1998]

At 248 nm that threshold is about 207 nm at NA 0.6 and 177 nm at NA 0.7
(our arithmetic). The 0.150 µm active line lies below it and the 0.270
µm trench space above it, so on the KrF reading a CD error on the plate
would print enlarged on the narrowest active lines and about one to one
on the trenches (inference).

*Criteria & Assumptions* gives a general
"Min process bias 3s tolerance" of 0.032 (`PHTOL`) and no
active-specific CD tolerance.[^pdk-03] Thung et al. evaluated
"re-designs of the STI layout with Optical Proximity Correction (OPC)
tagging" among the changes that removed defects when 0.13 µm STI was run
on 0.18 µm-generation tools.[^thung-2016] Rules-based correction of the
kind Otto et al. describe[^otto-1994] is one form of proximity
correction, and the PDK does not say whether `FOM` data are corrected.

Unlike P1M, `FOM` is not among the layers of the finer grid rule x.1a,
whose 0.001 ("mm") grid is for "p1m.md (OPC)" and the "mask data for
p1m, met1, via, met2"; x.1b gives 0.005 for all other
layers.[^pdk-periph]

### Pattern density

The plate is also a density map for the polish
that follows. Table 4 of *Criteria & Assumptions* gives:[^pdk-03]

* an "S8 average
  FOM PD (extractions from logic device)" of 0.45 (`FOMPDAVG`)
* a "FOM
  700um box PD tolerance for CMP (SOI8 PCR2) for all technologies" of
  0.15 (`FOM700TOL`)
* extraction boxes of 700 and 2000 (`SMALLPDBOX`,
  `LARGEPDBOX`, both labelled "(um)")
* a "Stepping box shift as a
  percent of box size" of 0.5 (`BOXSHIFT`)

We read these as the
window over which the plate's active density, fill included, is checked
(inference; the table does not say how the check is run). Stine et al.
characterised and modelled such pattern-dependent CMP
variation.[^stine-1998] Gan et al. modelled the polish of a reverse-tone
etchback STI flow, predicting dishing and nitride erosion from pattern
density and step height.[^gan-2001] A TSMC patent places dummy
structures for CMP planarity while limiting the capacitance they
add.[^pat-dummy-tsmc]

`gds_layers.csv` has an `areaid.ww` identifier,
"Waffle window (used to prevent waffle shifting)", and Table C3 defines
the waffling "background" as the "Area where waffling grid is defined,
sized to avoid waffle shift between runs".[^pdk-06]

### Resist and tone

The step page reads a chemically amplified KrF
resist over an organic bottom anti-reflective coating or an inorganic
anti-reflective cap on the nitride, and leaves the choice and the
reticle tone open; neither is published. The consumables are on
the {ref}`lithography materials <material-lithography-materials>` page.

### Overlay and alignment

On the {ref}`FOM <step-004>` page's reading there is no
earlier pattern to align to, and the plate prints the marks that later
levels register to; the step page leaves a separate zero-mark step open.
The implant masks that follow align to the trenches on their step pages'
readings ({ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`), and the poly
mask to the same marks ({ref}`mask-p1m`). Edmark and Ausschnitt
calibrated stepper overlay by aligning to a latent image,[^edmark-1985]
and van Haren et al. show how the placement accuracy of wafer alignment
marks limits layer-to-layer overlay.[^van-haren-2019]

The margins that
depend on the placement of this level are:[^pdk-periph]

* those of the poly rules
  against diffusion — 0.130 of poly beyond diffusion (poly.8) and 0.250 of
  diffusion beyond poly (poly.7), whose unit cells are blank in the
  published table
* those of the implant and well rules against it, such as
  difftap.8's 0.180 µm N-well enclosure of p+ diffusion

The
PDK's *Error Messages* page describes "many of the automated DRC
rules that are checked by SkyWater as part of the acceptance criteria
for GDS data".[^pdk-errors] It lists two checks named `cfom.nikon`, "FOMmk in the nikon
cross has the wrong polarity" and "FOMmk is missing from the nikon cross
in the layout", and the same pair for most other mask
layers.[^pdk-errors]

The page does not say what the "nikon cross" is or
where it sits. We read it as a structure on these mask layers whose mask
data must have the right polarity (inference from the message wording),
which does not settle whether `FOM` carries the zero-level alignment
marks.

### Pattern transfer

On the step pages' readings the resist pattern is
transferred by {ref}`STINITE <step-005>` through any anti-reflective
coating, the isolation nitride and the pad oxide on the
{ref}`dielectric plasma etcher <machine-plasma-etcher-dielectric>`
class, and by {ref}`STIE <step-006>` into the silicon on the
{ref}`silicon and polysilicon plasma etcher <machine-plasma-etcher-silicon>`
class. The {ref}`STIE <step-006>` page treats the resist strip and the
polymer clean as part of the trench etch, and lists where the strip
happens as an open question.

(mask-fom-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `FOM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`FOM <step-004>`, {ref}`STINITE <step-005>`, {ref}`STIE <step-006>`

* {ref}`FOM <step-004>` — coats, exposes and develops the resist.
* {ref}`STINITE <step-005>` — etches the nitride and pad oxide through
  the resist windows, stopping on silicon.
* {ref}`STIE <step-006>` — etches the trenches into the silicon, on its
  page's reading commonly with the resist still on top, and strips the
  resist and cleans the trench; the step list used in this reference has
  no separate strip step.

The next step, {ref}`DNM <step-007>`, is itself the next mask step: on
its step page's reading it coats a new resist on the etched but unfilled
trenches, so the {ref}`STIE <step-006>` page's placement of the strip
inside the trench etch is what closes this mask's steps. The trench is
lined and filled later ({ref}`LINOX <step-010>`,
{ref}`FILOX <step-011>`), after the `DNM` resist has gone. There is no
exception to the rule for this mask.

## Design rules and critical dimensions

The `diff` and `tap` rules of the periphery rules, with the angle and
serif rules that name the layers; flag P means "Rule applies to
periphery only (outside areaid.ce). A corresponding core rule may or
may not exist.", NE "Rule not checked for esd_nwell_tap. There are no
corresponding rule for esd_nwell_tap." and DE "Rule not checked for
source of Drain Extended device".[^pdk-periph]

:::{table} The `diff` and `tap` rules, with the angle and mask-data rules that name the layers, as published; the unit column of difftap.4 and difftap.5 is blank in the published table

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| difftap.1 | "Width of diff or tap" (P) | 0.150 µm |
| difftap.2 | "Minimum channel width (Diff And Poly) except for FETs inside areaid.sc […]" (P) | 0.420 µm |
| difftap.2b | "Minimum channel width (Diff And Poly) for FETs inside areaid.sc" (P) | 0.360 µm |
| difftap.3 | "Spacing of diff to diff, tap to tap, or non-abutting diff to tap" | 0.270 µm |
| difftap.4 | "Min tap bound by one diffusion" | 0.290 |
| difftap.5 | "Min tap bound by two diffusions" (P) | 0.400 |
| difftap.6 | "Diff and tap are not allowed to extend beyond their abutting edge" | — |
| difftap.7 | "Spacing of diff/tap abutting edge to a non-conciding diff or tap edge" (NE) | 0.130 µm |
| difftap.8 | "Enclosure of (p+) diffusion by N-well. Rule exempted inside UHVI." (DE NE P) | 0.180 µm |
| difftap.9 | "Spacing of (n+) diffusion to N-well outside UHVI" (DE NE P) | 0.340 µm |
| difftap.10 | "Enclosure of (n+)  tap by N-well. Rule exempted inside UHVI." (NE P) | 0.180 µm |
| difftap.11 | "Spacing of (p+) tap to  N-well. Rule exempted inside UHVI." | 0.130 µm |
| x.2 | "Angles permitted on: diff except for: […]" | n x 90 deg |
| x.2a | "Analog circuits identified by areaid.analog to use rectangular diff and tap geometries only […]" | — |
| x.2c | "45 degree angles allowed on diff, tap inside UHVI" | — |
| x.9 | "Shapes on maskAdd or maskDrop layers ("serifs") are allowed in core only. Exempted are: […] cfom md/mp inside […] pcell […]" | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
:::

The unit column of difftap.4 and difftap.5 is blank in the published
table.[^pdk-periph] [*Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) gives the following:[^pdk-03]

:::{table} Parameters of *Criteria & Assumptions* for the mask

| Parameter | PDK table | Published description | Value |
|---|---:|---|---:|
| `FOMCD` | 2 | minimum feature | 0.14 |
| `FOMCDSP` | 2 | minimum space | 0.27 |
| `FOMSE` | 7 | "MOSFET width" | 0.135 |
| `FOMSESC` | 7 | "MOSFET width in standard cells" | 0.075 |
| `MINFWR` | 3c | "Min. diff/tap width for reproducible resistivity" | 0.12 µm |
| `SDM3` | 3c | "Min. width to open a strip of tap between two diffs" | 0.34 µm |
| `DEFC` | 4 | "min. etch and fill capability for isolation, licon, and met1" | 0.15 |
:::

The PDK does not
reconcile the Table 2 and Table 7 values with the 0.150 µm of difftap.1, and the smaller values
may describe the printed or etched width rather than the drawn one (our
reading; neither table says). The SKY130 {term}`test tile`'s pad
documentation draws its field-edge gate-oxide capacitors at "FOM w/s =
0.14/0.27", the Table 2 pair, and its high-voltage ones at "FOM w/s =
0.42/0.48".[^raw-data-testtile-pads] For the plate, difftap.1 and
difftap.3 set the smallest features: a 0.150 µm line on a 0.270 µm
space.

## Related pages

* **Steps.** {ref}`FOM <step-004>`, {ref}`STINITE <step-005>` and
  {ref}`STIE <step-006>` — the mask step, the hard-mask etch and the
  trench etch.
  {ref}`CMPNIT <step-012>` — the polish whose uniformity the fill
  shapes serve.
* **Category.** {ref}`category-lithography` and {ref}`category-etch` — the mask step
  and etch categories.
* **Machines.** {ref}`machine-duv-krf-stepper` and {ref}`machine-i-line-stepper` — the
  exposure class the step page assigns and its fallback.
  {ref}`machine-plasma-etcher-dielectric` and
  {ref}`machine-plasma-etcher-silicon` — the etch classes that transfer
  the pattern.
* **Materials.** {ref}`material-lithography-materials` — resists, anti-reflective
  coatings, developer and reticles.
* **Indexes.** {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the tables this page's plate facts are taken from.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

* {ref}`Method for forming dummy structures for improved CMP and reduced capacitance <patent-gp34080863>` — US 6,849,549 B1 (2003)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Field Oxide, FOM,
  X".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `diff`, `tap`,
  the `cfom` purposes, `fom` dummy, `areaid.ww`, the Table C3
  definitions and the `FOM` column of Table F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `FOMCD`/`FOMCDSP`, `FOMSE`,
  `FOMSESC`, the pattern-density criteria and the process-bias
  tolerance.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `difftap` rules, x.1a, x.1b,
  x.2, x.9, x.15a, the poly placement rules and the flag
  legend.[^pdk-periph]
* SkyWater PDK, [*Error Messages*](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) page and `errors.csv` — the
  `cfom.nikon` checks.[^pdk-errors]
* [SkyWater PDK Authors, test-tile pad documentation](<https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>) — the "FOM w/s"
  values of the gate-oxide capacitors.[^raw-data-testtile-pads]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the `FOM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `FOM` renders, their layers
  and note, and the per-die shape counts.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the DUV exposure
  tools.[^skw-01]
* [ASML, PAS 5500/750E press release](<https://www.asml.com/en/news/press-releases/2000/asml-introduces-krf-lithography-scanner-optimized-for>) — a KrF scanner for 130 nm
  resolution.[^asml-750e]

### High-level understanding

* [Wikipedia, *Photomask*](<https://en.wikipedia.org/wiki/Photomask>) — reticles, absorbers and
  pellicles.[^wiki-mask]
* [Wikipedia, *Shallow trench isolation*](<https://en.wikipedia.org/wiki/Shallow_trench_isolation>) — the etch, fill and polish
  that the mask starts.[^wiki-sti]
* [Wikipedia, *Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) — KrF and i-line exposure.[^wiki-litho]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]

### Deep dive

* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor of lines
  and spaces and the size below which it rises.[^wong-1998]
* [Tian, Tang and Wong, *IEEE TCAD* 2002](<https://doi.org/10.1109/43.974138>) — dummy-feature placement for
  the dual-material STI polish.[^tian-2002]
* [Gan et al., *J. Electrochem. Soc.* 2001](<https://doi.org/10.1149/1.1348266>) — a CMP model for
  reverse-tone etchback STI and the pattern-density effects it
  predicts.[^gan-2001]
* [Stine et al., *IEEE TSM* 1998](<https://doi.org/10.1109/66.661292>) — pattern-dependent CMP variation, the
  basis of density rules.[^stine-1998]
* [Kahng and Samadi, *IEEE TCAD* 2008](<https://doi.org/10.1109/TCAD.2007.907061>) — a survey of CMP fill
  synthesis.[^kahng-2008]
* [Chiou and Jang (TSMC), US 6,849,549](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6849549>) — dummy structures for CMP
  planarity with reduced added capacitance.[^pat-dummy-tsmc]
* [Thung et al., *JTEC* 2016](<https://web.archive.org/web/20260411150120/https://jtec.utem.edu.my/jtec/article/view/697>) — 0.13 µm STI on 0.18 µm tools, including
  OPC on the STI layout.[^thung-2016]
* [Otto et al., *Proc. SPIE* 1994](<https://doi.org/10.1117/12.175422>) — rules-based optical proximity
  correction.[^otto-1994]
* [Edmark and Ausschnitt, *Proc. SPIE* 1985](<https://doi.org/10.1117/12.947752>) — stepper overlay
  calibration by aligning to a latent image.[^edmark-1985]
* [van Haren et al., *Proc. SPIE* 2019](<https://doi.org/10.1117/12.2536270>) — how alignment-mark placement
  limits layer-to-layer overlay.[^van-haren-2019]
* [Rizvi (ed.), *Handbook of Photomask Manufacturing Technology*](<https://doi.org/10.1201/9781420028782>) — data
  preparation, mask writing and optical masks.[^rizvi-2005]
* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — mask magnification and the exposure
  options of the 130 nm generation.[^itrs-03]

## Open questions

* The operation that makes the `cfom` plate data from `diff`, `tap` and
  the `cfom` add, drop and waffle-drop purposes is not published, and
  the renders site's "grown pnp emitter" term has no public
  source.[^pdk-06][^mask-renders]
* The PDK does not reconcile Table 2's 0.14 and Table 7's 0.135 and
  0.075 with the 0.150 µm of difftap.1, nor say whether `FOM` data are
  proximity-corrected.[^pdk-03][^pdk-periph]
* The plate's tone, blank, absorber, phase-shift type and
  magnification, the resist and the exposure tool are not public; the
  KrF reading rests on the 0.150 µm rule.
* Whether the plate also carries the zero-level alignment marks, or a
  separate zero-mark step does, is not public, and the Error Messages
  page does not explain its "nikon cross" checks.[^pdk-errors]
* The renders do not say how much of each die's shape count is fill, and
  the fill layer 23:28 is not in
  `gds_layers.csv`.[^mask-renders][^pdk-06]
* What the plate number `020` encodes is not stated, and no public
  source lists the `FOM` plate of the original MPW-4 set
  `5CS8010AC`.[^steps-sheet][^mask-renders]

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tabs "Sheet1" (step number, code and description), "Masks"
    (mask steps with step numbers), "Run Mask IDs" (the mask table set
    against MPW-1 to MPW-8, with "Exists" and "Plate ID" columns per run)
    and "Sheet4" (mask types), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* (including Table C3,
    device, LVS and other CAD definitions, and Table F2b, the mask
    generation table) and `gds_layers.csv`, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 3c,
    4 and 7), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_FOM/`
    directory with its page, `job.json`, `result.json` and per-die slot
    JSON files, retrieved 2026-09-14. Rendered from the public shuttle
    repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^asml-750e]: ASML, *ASML introduces KrF lithography scanner* (PAS
    5500/750E), press release, 2000-04-04.
    <https://www.asml.com/en/news/press-releases/2000/asml-introduces-krf-lithography-scanner-optimized-for>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-sti]: Wikipedia, *Shallow trench isolation*.
    <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
[^tian-2002]: R. Tian, X. Tang and M. D. F. Wong, "Dummy-feature
    placement for chemical-mechanical polishing uniformity in a
    shallow-trench isolation process", *IEEE Transactions on
    Computer-Aided Design of Integrated Circuits and Systems* **21**(1),
    63–71 (2002). <https://doi.org/10.1109/43.974138>
[^gan-2001]: T. Gan, T. Tugbawa, B. Lee, D. S. Boning and S. Jang,
    "Modeling of Reverse Tone Etchback Shallow Trench Isolation Chemical
    Mechanical Polishing", *Journal of The Electrochemical Society*
    **148**(3), G159 (2001). <https://doi.org/10.1149/1.1348266>
[^stine-1998]: B. E. Stine, D. O. Ouma, R. R. Divecha, D. S. Boning,
    J. E. Chung, D. L. Hetherington, C. R. Harwood, O. S. Nakagawa and
    S.-Y. Oh, "Rapid characterization and modeling of pattern-dependent
    variation in chemical-mechanical polishing", *IEEE Transactions on
    Semiconductor Manufacturing* **11**(1), 129–140 (1998).
    <https://doi.org/10.1109/66.661292>
[^kahng-2008]: A. B. Kahng and K. Samadi, "CMP Fill Synthesis: A Survey
    of Recent Studies", *IEEE Transactions on Computer-Aided Design of
    Integrated Circuits and Systems* **27**(1), 3–19 (2008).
    <https://doi.org/10.1109/TCAD.2007.907061>
[^pat-dummy-tsmc]: W.-C. Chiou and S.-M. Jang (Taiwan Semiconductor
    Manufacturing Co.), *Method for forming dummy structures for improved
    CMP and reduced capacitance*, US 6,849,549 B1, filed 2003-12-04,
    granted 2005-02-01.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6849549>
[^thung-2016]: B. J. Thung, K. Ibrahim, N. A. Manap and F. Salehuddin,
    "Challenges for 0.13µm Generation Shallow Trench Isolation on
    0.18µm Equipment Platform", *Journal of Telecommunication,
    Electronic and Computer Engineering* **8**(5), 15–21 (2016).
    <https://web.archive.org/web/20260411150120/https://jtec.utem.edu.my/jtec/article/view/697>
    (Wayback Machine capture of 2026-04-11; original, dead since 2026-09-19:
    `https://jtec.utem.edu.my/jtec/article/view/697`; the PDF link below
    still works directly) (PDF:
    <https://jtec.utem.edu.my/jtec/article/download/697/707/3255>).
[^otto-1994]: O. W. Otto, J. G. Garofalo, K. K. Low, C.-M. Yuan,
    R. C. Henderson, C. Pierrat, R. L. Kostelak, S. Vaidya and
    P. K. Vasudev, "Automated optical proximity correction: a
    rules-based approach", *Proc. SPIE* **2197**, Optical/Laser
    Microlithography VII, 278–293 (1994).
    <https://doi.org/10.1117/12.175422>
[^edmark-1985]: K. W. Edmark and C. P. Ausschnitt, "Stepper Overlay
    Calibration Using Alignment To A Latent Image", *Proc. SPIE*
    **0538**, Optical Microlithography IV, 91 (1985).
    <https://doi.org/10.1117/12.947752>
[^van-haren-2019]: R. J. F. van Haren, S. Steinert, O. Mouraille,
    K. D'havé, L. van Dijk, J. Hermans and D. Beyer, "Wafer alignment
    mark placement accuracy impact on the layer-to-layer overlay
    performance", *Proc. SPIE* **11148**, Photomask Technology 2019, 37
    (2019). <https://doi.org/10.1117/12.2536270>
[^rizvi-2005]: S. Rizvi (ed.), *Handbook of Photomask Manufacturing
    Technology*, CRC Press, 2005, ISBN 978-1-4200-2878-2.
    <https://doi.org/10.1201/9781420028782>
