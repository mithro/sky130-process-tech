(mask-rrpm)=
# RRPM — Rev Resistor Protect

`RRPM` is the second of SKY130's three poly-resistor masks and the one
with the thinnest public record: on the {ref}`RRPM <step-052>` page's
reading, the resist printed through it at step 52 covers the gate film
everywhere except windows over the 300 Ω/sq resistor bodies that
{ref}`RPM <step-049>` protected, the p-type resistor implant
{ref}`PRI <step-053>` goes through the windows, and the resist is
stripped at {ref}`PRIS <step-054>`. The PDK's mask table does not list
it and no PDK layer, rule or table column carries its name; the
process-steps sheet records a plate for it on all eight MPW runs; and
the public mask-layer renders have no image of it for any run. One
public document names it: the pad documentation of the SKY130
{term}`test tile`. This page gathers what public sources say about the
mask — its absence from the PDK tables and the layers the step page
derives it from, the plates the sheet records, what the renders do and
do not show, the lithography it needs and the rules that bound it — and
reports the gaps without drawing conclusions from them. How the step is
performed is on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | RRPM — Rev Resistor Protect |
|---|---|
| Mask step | {ref}`RRPM <step-052>`, step 52 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | not listed; the name is the "Run Mask IDs" tab's "Rev Resistor Protect"[^steps-sheet][^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | none[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `rpm` drawing 86:20, "300 ohms/square polysilicon resistor implant", alone or less `urpm` drawing 79:20, "2000 ohms/square polysilicon resistor implant" — an inference of the step page[^pdk-06] |
| Minimum CD, feature / space | none listed[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist is opened over the resistor bodies and remains elsewhere, which with a positive resist would make the plate dark-field with clear windows, the complement of `RPM` (inference). |
| Exposure class | i-line, an inference on the step page from the relaxed geometry it shares with `RPM` (1.27 µm features, 0.84 µm spaces), with a KrF tool named as the option; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `177`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | not rendered[^mask-renders] |
| Steps that use the pattern | 3 steps; see {ref}`Steps that use this mask <mask-rrpm-steps>` |

## What the mask defines

The step list calls step 52 "Rev resistor protect mask" and does not
explain the name;[^steps-sheet] the {ref}`RRPM <step-052>` page reads the
mask as the reverse of {ref}`RPM <step-049>`. Its argument rests on the
PDK's resistors, not on the name. Both precision flavours are p-type
films — "P+ poly precision resistors" at 300 Ω/sq and "P- poly precision
resistors", for which "a separate implant is used to set the sheet
resistance to 2000 ohm/sq" — inside a poly layer whose generic resistor
is "N+ doped gate poly";[^pdk-07] the extraction table gives the
"XHR poly resistor" 319800 and "Poly" 48200 in a column headed
"Resistivity (mohms/sq)" (319.8 Ω/sq and 48.2 Ω/sq, our
conversion).[^pdk-08] Since `RPM` keeps the gate implant out of the
bodies, the p-type resistor implant must reach exactly those bodies, and
the step page infers a second reticle of the opposite tone on the same
drawn layer, `rpm`, derived from `rpm` alone or from `rpm` less `urpm`
depending on whether the 2000 Ω/sq bodies receive this implant as well
as their own. It says that a reverse-tone mask is itself an inference.

The PDK's own tables name no such mask. `masks.csv` lists "Resistor
Protect, RPM" and no reverse mask;[^pdk-05] `gds_layers.csv` has no
mask-level layer for it; Table F2b has no `RRPM` column, and its one row
with a created `RPM` shape is "p+ poly resistor";[^pdk-06] the periphery
rules have no rule set for it;[^pdk-periph] and Table 2 of *Criteria &
Assumptions* has no row for it.[^pdk-03] The PDK's Error Messages page
has no message that names `RRPM`.[^pdk-errors] The step page reads the
absence as consistent with a reticle generated from `rpm` that a
designer never needs to know about (inference).

The test tile's pad documentation is the one public document outside
the sheet that names the mask. Among its "300 ohm/sq P+ POLY RESISTOR"
structures it marks three — "W = 0.69, L = 0.345, sq = 0.5", its
mismatch pair of the same size, and "W = 0.33, L = 0.33, sq = 1" — "(will
not work for any routes using RRPM mask)".[^raw-data-testtile-pads] It
does not say what a route is or why those structures would fail. The
{ref}`RRPM <step-052>` page extracts from the published measurements of
the marked structures 0.49–0.54 kΩ at 0.69 µm and half a square and
0.97 kΩ at 0.33 µm and one square, inside the limits of the PDK's
e-test table for the nearest listed sizes, and notes that the files do
not say which route the measured wafer
followed.[^raw-data-passives][^pdk-07] O'Dwyer and Kennedy compared the
matching of different poly resistor films in one CMOS
process.[^odwyer-2009]

## Drawn layers and derivation

### In the PDK

The drawn layers the step page derives the mask from are `rpm` at 86:20
and `urpm` at 79:20; there is no mask-level (`c…`) layer and no drawn
layer carrying the mask's name.[^pdk-06] The periphery rules define the
`rpm` rule set as "Defines p+ poly resistors" and publish no `urpm` rule
set,[^pdk-periph] and Table C3 of the *Layers Reference* defines
`prec_resistor` as "rpm AND (poly overlapping poly.rs) AND
psdm";[^pdk-06] none of these mentions a second mask. The Error Messages
page lists checks under the rule names urpm.1a, urpm.2 and urpm.3 — "1.27
min. width of urpm", "0.84 min. spacing/notch of urpm" and "0.2 min.
enclosure of precResistor by rpm" — which carry the values of rpm.1a,
rpm.2 and rpm.3 (our comparison) and say nothing about the tone of any
plate.[^pdk-errors][^pdk-periph] The PDK therefore publishes neither the
operation nor the choice between `rpm` and `rpm` less `urpm` that the
step page leaves open.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask, for 42 mask layers. `RRPM` is not among them: the
site has no `RRPM` render directory for any run, and its overview of
every run against every mask has no `RRPM` column; it does not say
why.[^mask-renders] The site's `RPM` render is of `rpm` 86:20 alone, and
its `URPM` render of `urpm` 79:20 alone ({ref}`mask-rpm`,
{ref}`masks-derivations`).[^mask-renders] On the step page's reading the
`RRPM` data would come from those layers, so the `RPM` renders — `rpm`
on 1, 5, 0, 3, 4, 2, 3 and 2 dies of MPW-1 to MPW-8 — are the nearest
public view of what this mask draws (inference); they are one public
derivation from the drawn data, not SkyWater's mask-generation recipe,
and they are not a render of this mask. The site states the limits of
all its images: "These are renders of *drawn* data, not photomask
artwork: reticle pitch, 4x reduction, mirroring and the frame features
the fab adds are not modelled."[^mask-renders]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet has a row "Rev
Resistor Protect, RRPM", with the "Used in SKY130" field blank, one of
the five rows it adds to the mask table of `masks.csv`; it marks an
`RRPM` plate as existing on all eight MPW runs, with the plate number
`177` on each and no "Info" note.[^steps-sheet][^pdk-05] The plate IDs
below are the sheet's; the reticle set is the heading of the run's
columns in the tab ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA177A` |
| MPW-2 | `5CS8007AC` | `S8007AA177A` |
| MPW-3 | `5CS8008AC` | `S8008AA177A` |
| MPW-4 | `5CS8018AC` | `S8018AA177A` |
| MPW-5 | `5CS8011AC` | `S8011AA177A` |
| MPW-6 | `5CS8014AC` | `S8014AA177A` |
| MPW-7 | `5CS8016AC` | `S8016AA177A` |
| MPW-8 | `5CS8017AC` | `S8017AA177A` |

* **Plate recorded, never rendered.** Every run has an `RRPM` plate in
  the sheet and no `RRPM` render on the site
  ({ref}`masks-renders`).[^steps-sheet][^mask-renders] No public source
  shows what any of the eight plates carries, and no rendered die of
  MPW-3 draws `rpm`, the layer the step page derives the mask from; this
  page does not read the plates as evidence that any project on the runs
  used the 300 Ω/sq resistor.
* **Not in `masks.csv`.** The sheet records plates for three masks that
  `masks.csv` does not list — `RRPM`, `URPM` and `CAP2M` — on all eight
  runs ({ref}`masks-mpw-runs`); neither source explains the
  difference.[^steps-sheet][^pdk-05]
* **Plate number.** `177` lies between `175` for `RPM` and `178` for
  `URPM`, but the plate numbers do not follow process order elsewhere,
  and the sheet does not say what they encode, so no process position or
  grouping is read from it ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `RRPM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]

## Lithography and pattern transfer

**Exposure class.** The {ref}`RRPM <step-052>` page gives the mask the
geometry of `RPM` — 1.27 µm features and 0.84 µm spaces, the `RPMCD` and
`RPMCDSP` of Table 2[^pdk-03] — and infers an i-line level, with a KrF
tool as the option; the {ref}`i-line stepper <machine-i-line-stepper>`
page lists it there. SkyWater lists "ASML I-line stepper" and "ASML
I-line scanner" among its tools but assigns no layer to them.[^skw-01]
At that geometry Wong et al.'s mask error factor, which "is unity for
large features",[^wong-1998] would leave plate CD errors at about their
own size on the wafer (inference).

**Resist and tone.** The {ref}`RRPM <step-052>` page reads a positive
i-line resist of about 1 µm on the doped gate film — the PDK's generic
"Photoresist thickness" is 1.14 µm[^pdk-03] — and a mostly chrome plate
whose clear windows are the resistor bodies plus enclosure. It notes that
a continuous field of resist with holes is the easier case for an implant
mask, since resist islands can lift or shift. The {ref}`PRIS <step-054>`
page reads the resist as carrying a continuous implanted crust after a
p-type dose of order 10¹⁴–10¹⁵ cm⁻² (illustrative on the
{ref}`PRI <step-053>` page), the carbonised layer Orvek and Huffman
describe.[^orvek-1985] SkyWater's resist is not public; the consumables
are on the {ref}`lithography materials <material-lithography-materials>`
page.

**Pattern transfer.** Nothing is etched through this resist. On the step
pages' readings the pattern is transferred into the resistor bodies as
dopant by {ref}`PRI <step-053>`, on the
{ref}`high-current implanter <machine-high-current-implanter>` or
{ref}`medium-current implanter <machine-medium-current-implanter>` class,
and the resist is removed at {ref}`PRIS <step-054>` on the
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` class.
The sheet resistance the implant sets is a steep function of dose:
Seto's grain-boundary trapping model shows the resistivity of doped poly
falling by orders of magnitude over a narrow doping range,[^seto-1975]
and Mandurah, Saraswat and Kamins refined it with dopant segregation to
the grain boundaries.[^mandurah-1981]

**Overlay with `RPM`.** The {ref}`RRPM <step-052>` page infers that
`RPM` and `RRPM` both align to the trench marks of {ref}`FOM <step-004>`,
so that their mutual overlay is the sum of two registrations: a gap
between the `RPM` island and the `RRPM` window would leave a strip of
undoped poly, and an overlap a strip doped both n⁺ and p. It reads the
0.200 µm enclosure of the resistor by `rpm` (rpm.3) as the margin that
keeps either strip off the body, and cites Hook et al. for the lateral
straggle that blurs a resist-edge boundary.[^hook-2003][^pdk-periph] The
two dopings behave differently: Chuang et al. found negative
temperature coefficients of the bulk sheet resistance in n⁺ and positive
ones in p⁺ poly resistors,[^chuang-2003] so a mixed strip would not
share the body's behaviour (our reading). ASML specifies "≤ 40 nm"
single-machine overlay for the PAS 5500/275D
stepper[^asml-pas5500-275d] (our comparison; SkyWater's budget is not
public).

(mask-rrpm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `RRPM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`RRPM <step-052>`, {ref}`PRI <step-053>`, {ref}`PRIS <step-054>`

* {ref}`RRPM <step-052>` — coats, exposes and develops the resist field
  with windows over the resistor bodies.
* {ref}`PRI <step-053>` — the p-type implant that sets the 300 Ω/sq
  sheet resistance, through the windows.
* {ref}`PRIS <step-054>` — strips the implanted resist and cleans the
  film for the next mask.

The next step, {ref}`URPM <step-055>`, is itself the next mask step: on
its step page's reading it coats the ultra-high-resistor mask on the
cleaned film and opens windows over the 2000 Ω/sq bodies. No step
between `PRIS` and it uses the `RRPM` resist, and there is no exception
to the rule for this mask.

## Design rules and critical dimensions

The PDK publishes no rules for this mask. The rules below are the `rpm`
rules that fix the bodies and the edge the step page derives the
windows from; flag P means "Rule applies to periphery only (outside
areaid.ce). A corresponding core rule may or may not exist.", and the
unit column of rpm.3 is blank in the published table.[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| rpm.1a | "Min width of rpm" | 1.270 µm |
| rpm.1b–1f | "Min/Max prec_resistor width xhrpoly_0p35" and the same for xhrpoly_0p69, 1p41, 2p85 and 5p73 | 0.350, 0.690, 1.410, 2.850, 5.730 µm |
| rpm.2 | "Min spacing of rpm to rpm" | 0.840 µm |
| rpm.3 | "rpm must enclose prec_resistor by atleast" | 0.200 |
| rpm.4 | "prec_resistor must be enclosed by psdm by atleast" | 0.110 µm |
| rpm.7 | "Min spacing between rpm and poly" | 0.200 µm |
| rpm.8 | "poly must not straddle rpm" | — |
| licon.9 | "Spacing, no overlap, between poly_licon and psdm; In SKY130DIA/SKY130TMA/SKY130PIR-10 flows, the rule is checked only between (poly_licon outside rpm) and psdm" (P) | 0.110 µm |

Table 2 of *Criteria & Assumptions* has no row for `RRPM`; the step page
takes the `RPM` row, `RPMCD` 1.27 and `RPMCDSP` 0.84, for this mask's
geometry.[^pdk-03] In the block of Table 4 headed "Other", whose value
column is headed "Value", "Poly resistor width and spacing to reduce CD
variation (um)" is 0.33 (`POLYRCD`) and 0.48 (`POLYRSPC`), and "Precision
resistor width to accommodate 6 contacts across" 2.03
(`PRECRESW`).[^pdk-03] None of these is stated as a rule for this mask.
If the windows are the `rpm` shapes, as the step page reads it, rpm.1a
and rpm.2 would set their smallest features (inference).

## Related pages

* {ref}`RRPM <step-052>`, {ref}`PRI <step-053>` and
  {ref}`PRIS <step-054>` — the mask step, the resistor implant and the
  strip.
* {ref}`mask-rpm` — the resistor protect mask, whose drawn layer the step
  page derives this mask from and whose islands it complements.
* {ref}`URPM <step-055>` — the ultra-high-resistor mask that follows.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the masks without a `masks.csv` entry and the plate that was
  never rendered.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-high-current-implanter` and
  {ref}`machine-medium-current-implanter` — the implant classes that use
  the pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography` and {ref}`category-implant` — the mask
  step and implant categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "Resistor Protect, RPM"
  and no reverse mask.[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `rpm`, `urpm`,
  the `prec_resistor` definition and Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — the `RPM` row of Table 2, the
  poly and precision resistor criteria and the photoresist
  thickness.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `rpm` rules, licon.9 and the
  flag legend.[^pdk-periph]
* SkyWater PDK, *Error Messages* page and `errors.csv` — the `urpm`
  messages and the absence of any `RRPM` message.[^pdk-errors]
* SkyWater PDK, *Device Details* — the P+ and P− poly precision resistors
  and their e-test table.[^pdk-07]
* SkyWater PDK, *Parasitic Layout Extraction* — the poly and resistor
  sheet resistances.[^pdk-08]
* SkyWater PDK Authors, test-tile pad documentation — the resistor
  structures marked for "routes using RRPM
  mask".[^raw-data-testtile-pads]
* SkyWater PDK Authors, measured passive-device data — the measurements
  of the marked structures.[^raw-data-passives]
* *S8 / SKY130 Process Steps* sheet — the step, the "Rev Resistor
  Protect" row and its plates on MPW-1 to MPW-8.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the absence of an `RRPM`
  render and the `RPM` and `URPM` layers.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the i-line exposure
  tools.[^skw-01]
* ASML, *PAS 5500/275D* data sheet — single-machine overlay of an i-line
  stepper.[^asml-pas5500-275d]

### High-level understanding

* Wikipedia, *Photomask* — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wikipedia, *Ion implantation* — masking, range and
  energy.[^wiki-implant]
* Wikipedia, *Sheet resistance* — the ohms-per-square
  convention.[^wiki-rs]
* Kamins, *Polycrystalline Silicon for Integrated Circuits and Displays* —
  doping and electrical properties of poly films.[^kamins-1998]

### Deep dive

* Seto, *J. Appl. Phys.* 1975 — grain-boundary trapping and the steep
  dependence of poly resistivity on doping.[^seto-1975]
* Mandurah, Saraswat and Kamins, *IEEE TED* 1981 — conduction in poly
  with dopant segregation to the grain boundaries.[^mandurah-1981]
* Lu et al., *IEEE TED* 1981 — modelling and optimisation of monolithic
  poly resistors.[^lu-1981]
* Lane and Wrixon, *IEEE TED* 1989 — the design of thin-film poly
  resistors for analogue ICs.[^lane-1989]
* Chuang et al., *IEEE TED* 2003 — temperature coefficients of n⁺ and p⁺
  poly and diffused resistors.[^chuang-2003]
* O'Dwyer and Kennedy, PRIME 2009 — matching of poly resistor films in a
  CMOS process.[^odwyer-2009]
* Tsang et al., *IEEE TSM* 2014 — resistance variation across banks of
  high-value poly resistors.[^tsang-2014]
* Ashuah, Shauly and Shacham-Diamand, *IEEE TSM* 2009 — co-implantation
  to improve the TCR of boron-implanted poly resistors.[^ashuah-2009]
* Upreti and Singh, *Bull. Mater. Sci.* 1991 — grain-boundary effects in
  boron-doped poly films.[^upreti-1991]
* Orvek and Huffman, *NIM B* 1985 — the carbonised layer on ion-implanted
  resist masks.[^orvek-1985]
* Hook et al., *IEEE TED* 2003 — lateral straggle and the mask proximity
  effect at an implant resist edge.[^hook-2003]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  size below which it rises.[^wong-1998]

## Open questions

* Whether `RRPM` is a reverse-tone reticle generated from `rpm`, as the
  step page infers, and whether it is derived from `rpm` alone or from
  `rpm` less `urpm`, is not published; no PDK table names the
  mask.[^pdk-05][^pdk-06][^pdk-periph]
* Why `masks.csv` does not list a mask for which the sheet records plates
  on every run is not stated in either source.[^pdk-05][^steps-sheet]
* What the test tile's "routes using RRPM mask" are, and why the marked
  structures would not work on them, is not explained.[^raw-data-testtile-pads]
* The renders site has no `RRPM` render and does not say why, so no
  public image of the mask's drawn data exists.[^mask-renders]
* The plate's tone, blank, absorber and magnification, the resist and the
  exposure tool are not public; the i-line reading rests on the `RPM`
  geometry.
* What the plate number `177` encodes is not stated, and no public source
  lists the `RRPM` plate of the original MPW-4 set
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
    directory: `README.md`, `masks.html` and, for each run, the
    `mpw-00N_RPM/` and `mpw-00N_URPM/` directories with their pages,
    `job.json`, `result.json` and per-die slot JSON files; no
    `mpw-00N_RRPM/` directory exists; retrieved 2026-09-14. Rendered from
    the public shuttle repositories under
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
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
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
[^lane-1989]: W. A. Lane and G. T. Wrixon, "The design of thin-film
    polysilicon resistors for analog IC applications", *IEEE
    Transactions on Electron Devices* **36**(4), 738–744 (1989).
    <https://doi.org/10.1109/16.22479>
[^chuang-2003]: H.-M. Chuang, K.-B. Thei, S.-F. Tsai and W.-C. Liu,
    "Temperature-dependent characteristics of polysilicon and diffused
    resistors", *IEEE Transactions on Electron Devices* **50**(5),
    1413–1415 (2003). <https://doi.org/10.1109/TED.2003.813472>
[^odwyer-2009]: T. G. O'Dwyer and M. P. Kennedy, "Comparison of
    resistor matching performance of polysilicon films in a CMOS
    process", *2009 Ph.D. Research in Microelectronics and Electronics
    (PRIME)*, pp. 80–83. <https://doi.org/10.1109/RME.2009.5201322>
[^tsang-2014]: Y. Tsang, R. Shiono, G. Pfeffer and S. Kwan,
    "Characterization and Understanding of High Valued Polysilicon
    Resistor Resistance Variation Across a Resistor Bank With Parallel
    Resistor Fingers", *IEEE Transactions on Semiconductor
    Manufacturing* **27**(2), 294–300 (2014).
    <https://doi.org/10.1109/TSM.2014.2311375>
[^ashuah-2009]: I. Ashuah, E. N. Shauly and Y. Shacham-Diamand,
    "Improvement of Temperature Coefficient of Resistance by
    Co-Implantation of Argon or Xenon or Fluorine in Boron Implanted
    Polysilicon Resistors", *IEEE Transactions on Semiconductor
    Manufacturing* **22**(2), 305–316 (2009).
    <https://doi.org/10.1109/TSM.2009.2017655>
[^upreti-1991]: N. K. Upreti and S. Singh, "Grain boundary effect on
    the electrical properties of boron-doped polysilicon films",
    *Bulletin of Materials Science* **14**(6), 1331–1341 (1991).
    <https://doi.org/10.1007/BF02823239>
[^orvek-1985]: K. J. Orvek and C. Huffman, "Carbonized layer formation
    in ion implanted photoresist masks", *Nuclear Instruments and
    Methods in Physics Research B* **7–8**, 501–506 (1985).
    <https://doi.org/10.1016/0168-583X(85)90421-5>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices* **50**(9),
    1946–1951 (2003). <https://doi.org/10.1109/TED.2003.815371>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
