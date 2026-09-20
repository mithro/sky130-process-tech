(mask-urpm)=
# URPM — Ultra-High Resistor Poly

`URPM` is the last of SKY130's three poly-resistor masks: on the
{ref}`URPM <step-055>` page's reading, the resist printed through it at
step 55 covers the gate film everywhere except windows over the bodies
of the 2000 Ω/sq resistors, the light p-type implant
{ref}`UPRI <step-056>` sets their sheet resistance through those windows,
and the resist is stripped at {ref}`UPRIS <step-057>`, after which the
poly doping of the process is complete. Like {ref}`RRPM <mask-rrpm>`, it
has no entry in the PDK's mask table and no mask-level layer, and the
process-steps sheet records a plate for it on all eight MPW runs. Unlike
`RRPM`, it is rendered: the public renders of the MPW tape-out layouts
show its drawn layer on every die of every run, almost always as a single
shape. This page gathers what public sources say about the mask — its
place in the PDK and the drawn layer the step page pairs it with, the
plates the sheet records, what the renders show, the lithography it needs
and the rules that bound it. How the step is performed is on the step
page; every mask is indexed on the {ref}`masks index <masks-index>`.

| | URPM — Ultra-High Resistor Poly |
|---|---|
| Mask step | {ref}`URPM <step-055>`, step 55 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | not listed; the name is the "Run Mask IDs" tab's "Ultra-High Resistor Poly"[^steps-sheet][^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | none[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `urpm` drawing 79:20, "2000 ohms/square polysilicon resistor implant" — the pairing is an inference of the step page[^pdk-06] |
| Minimum CD, feature / space | none listed[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist is opened over the `urpm` bodies and remains elsewhere, which with a positive resist would make the plate dark-field with clear windows (inference). |
| Exposure class | i-line, an inference on the step page from the relaxed geometry of the `rpm` rules it applies to this layer, with a KrF tool named as the option; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `178`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 3 steps; see {ref}`Steps that use this mask <mask-urpm-steps>` |

## What the mask defines

The device the mask serves is public. The PDK's "P- poly precision
resistors" "have 5 different fixed widths, plus a variable W/L option";
"a separate implant is used to set the sheet resistance to 2000 ohm/sq";
their fixed-value resistors "have the same layout footprints as their P+
poly counterparts"; and "Electrical and e-test specs are still TBD, once
sufficient silicon has been evaluated".[^pdk-07] The extraction table
gives the "UHR poly resistor" 2000000 in a column headed "Resistivity
(mohms/sq)", that is 2000 Ω/sq (our conversion).[^pdk-08] The drawn layer
`urpm` is described as "2000 ohms/square polysilicon resistor
implant".[^pdk-06] The repository README says the process "Has high sheet
rho poly resistor", the *Background* page lists "Poly resistor (`r`)"
among the technology options, and Edwards describes the options as
including "high and ultra-high sheet ρ
resistors".[^pdk-10][^pdk-02][^ann-15]

The step list calls step 55 "Ultra-high resistor poly mask" and does not
explain it;[^steps-sheet] the {ref}`URPM <step-055>` page's reading rests
on the PDK's separate implant and on the drawn layer. It infers that the
reticle is generated from `urpm` in the window tone, and that the `urpm`
bodies were covered at {ref}`RPM <step-049>` and not opened at
{ref}`RRPM <step-052>`, so that {ref}`UPRI <step-056>` is the only implant
they receive; it gives the alternative — one reticle for both resistor
implants — as also consistent with the public sources. Why the film needs
its own mask is, on the step page's reading, the steepness of poly
resistance against doping — Seto found the carrier concentration of
boron-implanted poly "very small at doping levels below 5×10¹⁷/cm³" and
increasing "rapidly as the doping concentration was increased", and
proposed a grain-boundary trapping model for it[^seto-1975] — so the 300 Ω/sq and 2000 Ω/sq films need separately
controlled doses. Brederlow et al. found the low-frequency noise of
integrated poly resistors "much higher than predicted" by common
simulation models and examined its dependence on doping and deposition
technique,[^brederlow-2001] and Tsang et al. traced resistance variation
across banks of high-value poly resistors.[^tsang-2014]

The PDK's own tables do not name the mask. `masks.csv` has no entry for
it;[^pdk-05] `gds_layers.csv` has no mask-level layer for it; Table F2b
has no `URPM` column and no row for the 2000 Ω/sq resistor;[^pdk-06] the
periphery rules have no `urpm` rule set;[^pdk-periph] and Table 2 of
*Criteria & Assumptions* has no row for it.[^pdk-03] The test tile's pad
documentation names the mask: among its "2K ohm/sq" poly resistor
structures it marks four — "W = 0.69, L = 0.345, sq = 0.5", "W= 0.33,
l = 0.33, sq = 1" and a mismatch pair of each size — "(may not work for
routes using URPM mask)", without saying why.[^raw-data-testtile-pads]
The {ref}`URPM <step-055>` page extracts from the published measurements
of the marked structures 1.33–1.43 kΩ at 0.33 µm and one square, 0.59 kΩ
in one module against 2.8–3.1 kΩ in another at 0.69 µm and half a
square, and about 1 950 Ω/sq from the longer resistors of the
family.[^raw-data-passives]

## Drawn layers and derivation

### In the PDK

The drawn layer the step page pairs the mask with is `urpm` at 79:20;
there is no mask-level (`c…`) layer and no drawn layer carrying the
mask's name.[^pdk-06] The PDK's *Error Messages* page, which describes
"many of the automated DRC rules that are checked by SkyWater as part of
the acceptance criteria for GDS data", lists three checks under `urpm`
rule names although the periphery rules have no such rule set: "1.27 min.
width of urpm" (urpm.1a), "0.84 min. spacing/notch of urpm" (urpm.2) and
"0.2 min. enclosure of precResistor by rpm" (urpm.3).[^pdk-errors] The
first two give `urpm` the width and spacing that rules rpm.1a and rpm.2
give `rpm`, which fits the step page's application of the `rpm` geometry
to this layer (our comparison), and the third is worded for `rpm`. The
three checks also sit, in the page's numbering, immediately before the
rpm.3 message, where the rpm.1a and rpm.2 messages the page lacks would
be, so they may equally be the `rpm` checks filed under `urpm` names (our
reading).
Table C3 of the [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) defines the `prec_resistor` of the
rules as "rpm AND (poly overlapping poly.rs) AND psdm", naming `rpm`
and not `urpm`;[^pdk-06] the PDK does not say whether a 2000 Ω/sq
resistor is drawn inside `rpm` as well as `urpm`. It publishes no
operation that turns `urpm` into a plate.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `URPM` the site renders layer 79:20 (`urpm`)
alone, with no Boolean expression and no fill layer, on all eight runs;
its mask record gives no mask-level layer and no note, and leaves its
used-in-SKY130 field empty.[^mask-renders] The layer is the one the step
page pairs with the mask. The choice is one public derivation from the
drawn data, not SkyWater's mask-generation recipe; it agrees with the
index's pairing, but both start from the same public PDK files, so the
agreement is not independent ({ref}`masks-derivations`).

All 40 rendered dies of every run carry `urpm` shapes, but that is not 40
designs using the 2000 Ω/sq resistor: every die carries at least one
shape, and on each run 33 to 38 of the 40 dies carry exactly one — 37,
35, 36, 38, 33, 35, 36 and 37 dies on MPW-1 to MPW-8 in turn; the other
dies of MPW-2, MPW-5 and MPW-6 include two dies with a repeated count of
6, 2 and 2 shapes respectively.[^mask-renders] We read the single shape
as common to the dies rather than to the projects (inference), as the
{ref}`masks index <masks-renders>` does; the site does not say what it
is. The renders also show `urpm` without `rpm` on most dies: no die of
MPW-3 draws `rpm`, and at most five dies of any run do
({ref}`mask-rpm`).[^mask-renders] The site states the limits of its
images: "These are renders of *drawn* data, not photomask artwork:
reticle pitch, 4x reduction, mirroring and the frame features the fab
adds are not modelled."[^mask-renders] Its metadata carries no plate ID,
so a render is tied to a plate in the process-steps sheet only by the
acronym `URPM`, and the MPW-4 renders come from a different reticle set
from the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet has a row "Ultra-High
Resistor Poly, URPM", with the "Used in SKY130" field blank, one of the
five rows it adds to the mask table of `masks.csv`; it marks a `URPM`
plate as existing on all eight MPW runs, with the plate number `178` on
each and no "Info" note.[^steps-sheet][^pdk-05] The plate IDs below are
the sheet's; the reticle set is the heading of the run's columns in the
tab ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA178A` |
| MPW-2 | `5CS8007AC` | `S8007AA178A` |
| MPW-3 | `5CS8008AC` | `S8008AA178A` |
| MPW-4 | `5CS8018AC` | `S8018AA178A` |
| MPW-5 | `5CS8011AC` | `S8011AA178A` |
| MPW-6 | `5CS8014AC` | `S8014AA178A` |
| MPW-7 | `5CS8016AC` | `S8016AA178A` |
| MPW-8 | `5CS8017AC` | `S8017AA178A` |

* **Not in `masks.csv`.** The sheet records plates for three masks that
  `masks.csv` does not list — `RRPM`, `URPM` and `CAP2M` — on all eight
  runs ({ref}`masks-mpw-runs`); neither source explains the
  difference.[^steps-sheet][^pdk-05]
* **Shapes on every die.** Because nearly every die carries one `urpm`
  shape, the renders do not show which runs used the 2000 Ω/sq resistor
  in a design, and this page does not read the plates or the die count
  as evidence of such use ({ref}`masks-renders`).[^mask-renders]
* **Plate number.** `178` follows `175` for `RPM` and `177` for `RRPM`,
  but the plate numbers do not follow process order elsewhere, and the
  sheet does not say what they encode, so no process position or
  grouping is read from it ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `URPM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`, whose plates no public
  source lists ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`URPM <step-055>` page applies the `rpm`
minimum width of 1.270 µm and spacing of 0.840 µm to this layer, reads
the geometry as relaxed and infers an i-line level, with a KrF tool as
the option; the {ref}`i-line stepper <machine-i-line-stepper>` page lists
it there.[^pdk-periph] SkyWater lists "ASML I-line stepper" and "ASML
I-line scanner" among its tools but assigns no layer to them.[^skw-01]
At that geometry Wong et al.'s mask error factor, which "is unity for
large features",[^wong-1998] would leave plate CD errors at about their
own size on the wafer (inference); the step page notes that a mis-sized
window shows up directly as resistor value and matching error.

**Resist.** The {ref}`URPM <step-055>` page reads about 1 µm of positive
i-line resist on the doped gate film — the PDK's generic "Photoresist
thickness" is 1.14 µm[^pdk-03] — through a dark-field reticle with clear
windows over the `urpm` bodies. The {ref}`UPRIS <step-057>` page reads
the implant as the lightest of the module, of order 10¹⁴ cm⁻² or less
(illustrative on the {ref}`UPRI <step-056>` page), leaving a thin crust.
SkyWater's resist is not public; the consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Pattern transfer.** Nothing is etched through this resist. On the step
pages' readings the pattern is transferred into the 2000 Ω/sq bodies as
dopant by {ref}`UPRI <step-056>`, on the
{ref}`medium-current implanter <machine-medium-current-implanter>` class,
and the resist is removed at
{ref}`UPRIS <step-057>` on the
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` and
{ref}`wet bench <machine-wet-bench>` classes, which also serves as the
clean before the gate cap. Wright et al. describe rf-sputtered films of
the Cr–Si–B–SiO₂/Al₂O₃ system that reach 20 kΩ/sq with a temperature
coefficient below 200 ppm/°C, an alternative to poly for high-value
resistors,[^wright-2010] and Chen et al. treat the voltage coefficient
of poly resistors in a high-voltage CMOS technology.[^chen-2000]

**Overlay.** The {ref}`URPM <step-055>` page infers alignment to the
trench marks of {ref}`FOM <step-004>`, like the other two resistor masks,
and notes that since the body is later cut from the poly by
{ref}`P1M <step-061>` the window must enclose the drawn body with overlay
margin on every side. The rules give that margin for `rpm` as 0.200 µm
(rpm.3), and the Error Messages page's urpm.3 message repeats it for
`rpm`;[^pdk-periph][^pdk-errors] no enclosure is published for `urpm`
itself. Hook et al. found that ions scattered out of the edge of an
implant resist are implanted in the silicon near the mask
edge;[^hook-2003] the {ref}`URPM <step-055>` page lists the study for
straggle at resist edges. ASML specifies "≤ 40 nm"
single-machine overlay for the PAS 5500/275D
stepper[^asml-pas5500-275d] (our comparison; SkyWater's budget is not
public).

(mask-urpm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `URPM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`URPM <step-055>`, {ref}`UPRI <step-056>`, {ref}`UPRIS <step-057>`

* {ref}`URPM <step-055>` — coats, exposes and develops the resist field
  with windows over the 2000 Ω/sq bodies.
* {ref}`UPRI <step-056>` — the light p-type implant that sets the
  2000 Ω/sq sheet resistance, through the windows.
* {ref}`UPRIS <step-057>` — strips the implanted resist and cleans the
  film for the gate cap.

On its step page's reading, the next step, {ref}`GATENIT <step-058>`,
deposits a blanket nitride cap on the doped gate film after the resist is
gone. The next mask step is {ref}`P1M <step-061>`. There is no exception
to the rule for this mask.

## Design rules and critical dimensions

The PDK publishes no periphery rules for `urpm`. The rules below are the
`rpm` rules that fix the resistor footprints the P− resistors share, on
the device page's statement, with the P+ ones, and whose width and
spacing the step page applies to this layer; flag P means "Rule applies
to periphery only (outside areaid.ce). A corresponding core rule may or
may not exist.", and the unit column of rpm.3 is blank in the published
table.[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| rpm.1a | "Min width of rpm" | 1.270 µm |
| rpm.1b–1f | "Min/Max prec_resistor width xhrpoly_0p35" and the same for xhrpoly_0p69, 1p41, 2p85 and 5p73 | 0.350, 0.690, 1.410, 2.850, 5.730 µm |
| rpm.2 | "Min spacing of rpm to rpm" | 0.840 µm |
| rpm.3 | "rpm must enclose prec_resistor by atleast" | 0.200 |
| rpm.4 | "prec_resistor must be enclosed by psdm by atleast" | 0.110 µm |
| rpm.5 | "prec_resistor must be enclosed by npc by atleast" | 0.095 µm |
| rpm.8 | "poly must not straddle rpm" | — |
| licon.9 | "Spacing, no overlap, between poly_licon and psdm; In SKY130DIA/SKY130TMA/SKY130PIR-10 flows, the rule is checked only between (poly_licon outside rpm) and psdm" (P) | 0.110 µm |

The Error Messages page's `urpm` checks give 1.27 for the width and 0.84
for the spacing and notch of `urpm`, and 0.2 for the enclosure of the
precision resistor by `rpm`.[^pdk-errors] Table 2 of *Criteria &
Assumptions* has no row for `URPM`.[^pdk-03] In the block of Table 4
headed "Other", whose value column is headed "Value", "Poly resistor
width and spacing to reduce CD variation (um)" is 0.33 (`POLYRCD`) and
0.48 (`POLYRSPC`), and "Precision resistor width to accommodate 6
contacts across" 2.03 (`PRECRESW`); none names the 2000 Ω/sq
resistor.[^pdk-03] If the windows are the `urpm` shapes, the 1.27 width
and 0.84 spacing of the `urpm` checks would set their smallest features
(inference).

## Related pages

* {ref}`URPM <step-055>`, {ref}`UPRI <step-056>` and
  {ref}`UPRIS <step-057>` — the mask step, the resistor implant and the
  strip.
* {ref}`mask-rpm` and {ref}`mask-rrpm` — the other two resistor masks,
  which on the URPM step page's reading cover the `urpm` bodies and leave
  them closed.
* {ref}`mask-p1m` — the poly mask that cuts the resistor bodies.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the masks without a `masks.csv` entry.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-medium-current-implanter` — the implant class that uses
  the pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography` and {ref}`category-implant` — the mask
  step and implant categories.

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — no entry for the
  mask.[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `urpm` 79:20,
  the `prec_resistor` definition and Table F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — the poly and precision
  resistor criteria and the photoresist thickness.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `rpm` rules, licon.9 and the flag
  legend.[^pdk-periph]
* SkyWater PDK, [*Error Messages*](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) page and `errors.csv` — the `urpm`
  checks.[^pdk-errors]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — the P− poly precision
  resistors.[^pdk-07]
* [SkyWater PDK, *Parasitic Layout Extraction*](<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>) — the "UHR poly resistor"
  sheet resistance.[^pdk-08]
* SkyWater PDK, repository README and [*Background*](<https://skywater-pdk.readthedocs.io/en/main/rules/background.html>) — the high sheet-rho
  resistor and the `r` option.[^pdk-10][^pdk-02]
* [SkyWater PDK Authors, test-tile pad documentation](<https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>) — the structures
  marked for "routes using URPM mask".[^raw-data-testtile-pads]
* [SkyWater PDK Authors, measured passive-device data](<https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells/unsorted>) — the measurements
  of the marked structures.[^raw-data-passives]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the "Ultra-High Resistor
  Poly" row and its plates on MPW-1 to MPW-8.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `URPM` renders, their layer
  and the per-die shape counts.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the i-line exposure
  tools.[^skw-01]
* [ASML, *PAS 5500/275D* data sheet](<https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-275d.pdf>) — single-machine overlay of an i-line
  stepper.[^asml-pas5500-275d]

### High-level understanding

* [Edwards (Efabless), WOSET 2020](<https://woset-workshop.github.io/PDFs/2020/a03.pdf>) — the SKY130 process options, including
  "high and ultra-high sheet ρ resistors".[^ann-15]
* [Wikipedia, *Photomask*](<https://en.wikipedia.org/wiki/Photomask>) — reticles, absorbers and
  pellicles.[^wiki-mask]
* [Wikipedia, *Sheet resistance*](<https://en.wikipedia.org/wiki/Sheet_resistance>) — the ohms-per-square
  convention.[^wiki-rs]
* [Kamins, *Polycrystalline Silicon for Integrated Circuits and Displays*](<https://doi.org/10.1007/978-1-4615-5577-3>) —
  doping and electrical properties of poly films.[^kamins-1998]

### Deep dive

* [Seto, *J. Appl. Phys.* 1975](<https://doi.org/10.1063/1.321593>) — grain-boundary trapping and the steep
  dependence of poly resistivity on doping.[^seto-1975]
* [Mandurah, Saraswat and Kamins, *IEEE TED* 1981](<https://doi.org/10.1109/T-ED.1981.20504>) — conduction in poly
  with dopant segregation to the grain boundaries.[^mandurah-1981]
* [Lu et al., *IEEE TED* 1981](<https://doi.org/10.1109/T-ED.1981.20437>) — modelling and optimisation of monolithic
  poly resistors.[^lu-1981]
* [Brederlow et al., *IEEE TED* 2001](<https://doi.org/10.1109/16.925245>) — low-frequency noise of integrated
  poly resistors and its dependence on processing.[^brederlow-2001]
* [Tsang et al., *IEEE TSM* 2014](<https://doi.org/10.1109/TSM.2014.2311375>) — resistance variation across banks of
  high-value poly resistors.[^tsang-2014]
* [Wright et al., *JVST B* 2010](<https://doi.org/10.1116/1.3466531>) — rf-sputtered Cr–Si–B–SiO₂/Al₂O₃
  thin-film resistors reaching 20 kΩ/sq at <200 ppm/°C: the non-poly
  alternative route to a high-sheet-resistance, low-TCR
  film.[^wright-2010]
* [Chen et al., *Solid-State Electron.* 2000](<https://doi.org/10.1016/S0038-1101(00)00138-6>) — the voltage coefficient of
  poly resistors in high-voltage CMOS.[^chen-2000]
* [Upreti and Singh, *Bull. Mater. Sci.* 1991](<https://doi.org/10.1007/BF02823239>) — grain-boundary effects in
  boron-doped poly films.[^upreti-1991]
* [Ashuah, Shauly and Shacham-Diamand, *IEEE TSM* 2009](<https://doi.org/10.1109/TSM.2009.2017655>) — co-implantation
  to improve the TCR of boron-implanted poly resistors.[^ashuah-2009]
* [Hook et al., *IEEE TED* 2003](<https://doi.org/10.1109/TED.2003.815371>) — lateral straggle and the mask proximity
  effect at an implant resist edge.[^hook-2003]
* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor and the
  size below which it rises.[^wong-1998]

## Open questions

* Whether `URPM` is a separate window-tone reticle generated from
  `urpm`, as the step page reads it, or one reticle serves both resistor
  implants, is not published; no PDK table names the
  mask.[^pdk-05][^pdk-06]
* Whether a 2000 Ω/sq resistor is drawn inside `rpm` as well as `urpm`,
  and how the Error Messages page's `urpm` checks relate to the `rpm`
  rules, is not stated.[^pdk-06][^pdk-errors]
* What the single `urpm` shape common to most rendered dies is, and so
  which designs on the runs use the resistor, is not shown by the
  renders.[^mask-renders]
* Why `masks.csv` does not list a mask for which the sheet records plates
  on every run, and what the test tile's "routes using URPM mask" are, is
  not explained.[^pdk-05][^steps-sheet][^raw-data-testtile-pads]
* The plate's tone, blank, absorber and magnification, the resist and the
  exposure tool are not public; the i-line reading rests on the `rpm`
  geometry.
* What the plate number `178` encodes is not stated, and no public source
  lists the `URPM` plate of the original MPW-4 set
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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2 and
    4), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README. <https://github.com/google/skywater-pdk>
[^pdk-02]: SkyWater PDK Authors, *Background*, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/background.html>
[^ann-15]: R. T. Edwards (Efabless), "Google/SkyWater and the Promise of
    the Open PDK", *Workshop on Open-Source EDA Technology (WOSET)
    2020*. <https://woset-workshop.github.io/PDFs/2020/a03.pdf>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^raw-data-passives]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the poly, diffusion
    and well resistors, MiM capacitors, varactors and bipolar
    transistors of the test tile, IC-CAP `.mdm` files in
    `sky130_fd_pr/cells/unsorted/`, `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells/unsorted>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_URPM/` and
    `mpw-00N_RPM/` directories with their pages, `job.json`,
    `result.json` and per-die slot JSON files, retrieved 2026-09-14.
    Rendered from the public shuttle repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^asml-pas5500-275d]: ASML, *PAS 5500/275D High Productivity i-Line
    Stepper*, refurbished systems data sheet, 2019, accessed 2026-09-13.
    <https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-275d.pdf>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-rs]: Wikipedia, *Sheet resistance*.
    <https://en.wikipedia.org/wiki/Sheet_resistance>
[^kamins-1998]: T. Kamins, *Polycrystalline Silicon for Integrated
    Circuits and Displays*, 2nd ed., Kluwer Academic, 1998.
    <https://doi.org/10.1007/978-1-4615-5577-3>
[^seto-1975]: J. Y. W. Seto, "The electrical properties of
    polycrystalline silicon films", *Journal of Applied Physics*
    **46**(12), 5247–5254 (1975). <https://doi.org/10.1063/1.321593>
[^mandurah-1981]: M. M. Mandurah, K. C. Saraswat and T. I. Kamins, "A
    model for conduction in polycrystalline silicon — Part I: Theory",
    *IEEE Transactions on Electron Devices* **28**(10), 1163–1171
    (1981). <https://doi.org/10.1109/T-ED.1981.20504>
[^lu-1981]: N. C.-C. Lu, L. Gerzberg, C.-Y. Lu and J. D. Meindl,
    "Modeling and optimization of monolithic polycrystalline silicon
    resistors", *IEEE Transactions on Electron Devices* **28**(7),
    818–830 (1981). <https://doi.org/10.1109/T-ED.1981.20437>
[^brederlow-2001]: R. Brederlow, W. Weber, C. Dahl,
    D. Schmitt-Landsiedel and R. Thewes, "Low-frequency noise of
    integrated polysilicon resistors", *IEEE Transactions on Electron
    Devices* **48**(6), 1180–1187 (2001).
    <https://doi.org/10.1109/16.925245>
[^tsang-2014]: Y. Tsang, R. Shiono, G. Pfeffer and S. Kwan,
    "Characterization and Understanding of High Valued Polysilicon
    Resistor Resistance Variation Across a Resistor Bank With Parallel
    Resistor Fingers", *IEEE Transactions on Semiconductor
    Manufacturing* **27**(2), 294–300 (2014).
    <https://doi.org/10.1109/TSM.2014.2311375>
[^wright-2010]: S. W. Wright, C. P. Judge, M. J. Lee, D. F. Bowers,
    M. Dunbar and C. D. Wilson, "High sheet resistance, low temperature
    coefficient of resistance resistor films for integrated circuits",
    *Journal of Vacuum Science & Technology B* **28**(4), 834–840
    (2010). <https://doi.org/10.1116/1.3466531>
[^chen-2000]: C.-H. Chen, Y.-K. Fang, M.-H. Kuo, Y.-L. Hsu and
    S.-L. Hsu, "A DC current stress method to improve the voltage
    coefficient of resistance of the polysilicon resistor in high
    voltage CMOS technology", *Solid-State Electronics* **44**(10),
    1743–1746 (2000). <https://doi.org/10.1016/S0038-1101(00)00138-6>
[^upreti-1991]: N. K. Upreti and S. Singh, "Grain boundary effect on
    the electrical properties of boron-doped polysilicon films",
    *Bulletin of Materials Science* **14**(6), 1331–1341 (1991).
    <https://doi.org/10.1007/BF02823239>
[^ashuah-2009]: I. Ashuah, E. N. Shauly and Y. Shacham-Diamand,
    "Improvement of Temperature Coefficient of Resistance by
    Co-Implantation of Argon or Xenon or Fluorine in Boron Implanted
    Polysilicon Resistors", *IEEE Transactions on Semiconductor
    Manufacturing* **22**(2), 305–316 (2009).
    <https://doi.org/10.1109/TSM.2009.2017655>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices* **50**(9),
    1946–1951 (2003). <https://doi.org/10.1109/TED.2003.815371>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
