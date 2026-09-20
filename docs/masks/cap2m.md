(mask-cap2m)=
# CAP2M — Capacitor MiM 2

The second capacitor mask is the {term}`reticle` that draws the top
plates of SKY130's second {term}`MiM capacitor`, the one built over
metal 4: on the {ref}`CAP2M <step-152>` page's reading, the resist
printed through it at step 152 stays wherever `cap2m` is drawn, on the
blanket plate film of {ref}`CAPTIW2 <step-151>`, and the
{ref}`CAP2ME <step-153>` etch removes the film everywhere else. Less is
public about it than about any of its neighbours: `masks.csv` has no
entry for it, the minimum-CD table no row and the periphery rules no rule
set (the PDK's published DRC checks name it only in two module-cut
checks), and the drawn layer `cap2m` is paired with the mask only on the step
page's reading. The process-steps sheet nevertheless lists it, as
"Capacitor MiM 2", with a plate on every MPW run, and the public renders
show `cap2m` shapes on 39 or 40 dies of every run, most of them a single
shape. This page gathers what public sources say about the mask
itself — its PDK entry and layers, the plates the process-steps sheet
records for the MPW runs, what the public renders of those runs show,
the lithography it needs and the rules that constrain it. How the step
is performed is on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | CAP2M — Capacitor MiM 2 |
|---|---|
| Mask step | {ref}`CAP2M <step-152>`, step 152 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | not listed; the name is the "Run Mask IDs" tab's "Capacitor MiM 2"[^pdk-05][^steps-sheet] |
| Mask-level layer (`gds_layers.csv`) | none[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `cap2m` drawing 97:44, "MiM capacitor plate over metal 4" (inference: the step page's pairing, since no `masks.csv` entry names the mask)[^pdk-06] |
| Minimum CD, feature / space | none listed[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist remains where `cap2m` is drawn, which with a positive resist would make the plate clear-field (inference). |
| Exposure class | i-line, an inference on the step page from the `capm` rules applied to a construction the PDK calls identical; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `582`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 39, 40, 40, 40, 40, 40, 40, 40[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-cap2m-steps>` |

## What the mask defines

The PDK names the device the mask draws but not the mask. Its *Device
Details* page lists two constructions of the MiM capacitor, "CAPM over
Metal-3" and "CAP2M over Metal-4", and states that "The constructions are
identical, and the capacitors may be stacked to maximize total
capacitance"; it names the cell `sky130_fd_pr__cap_mim_m4__base` and the
model `sky130_fd_pr__cap_mim_m4`, and gives the second capacitor its own
area capacitance `CMIM2A` of 2 fF/µm² (limits 1.8–2.2) and periphery
capacitance `CMIM2P` of 0.19 fF/µm (0.11–0.27), with a "MiM2 top plate
sheet resistance" of 5.8 Ω/sq (4.8–6.8) listed under the name `RSCAPM`,
the same name as the first capacitor's.[^pdk-07] The mask therefore sets
the plate area and perimeter of the second capacitor (the
{ref}`CAP2M <step-152>` page's reading of the model form). The PDK's
cross-section of the stacked capacitor labels "CAP2M", "M4 (plate 2)",
"Via4" and "M5 (plate 2)", and the process stack diagram includes a
`cap2m` layer, which the step page reads as lying between `metal4` and
`metal5`.[^pdk-07][^pdk-04]

What the PDK does not publish for this mask is as telling. `masks.csv`
has no entry for a second capacitor mask;[^pdk-05] Table 2 of [*Criteria &
Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) has no `cap2m` row;[^pdk-03] the periphery rules have a
`capm` rule set, every value "N/A", and no `cap2m` rule set;[^pdk-periph]
and neither Table F2b, the mask generation table, nor the CAD definitions
of Table C3, which define "top_plate" as "capm:dg", mention
`cap2m`.[^pdk-06] The {ref}`CAP2M <step-152>` page therefore reads the
plate geometry as that of `capm` — a 2 µm minimum width and a 0.84 µm
minimum space — and the mask as a non-critical, large-feature layer
(inference from the "identical" construction).

The published SKY130 {term}`test tile` uses the name `CAP2M` for the
plate: a "Large MiM2 capacitor, CAP2M over M4, 11 plates, each
40x40" with "Total expected capacitance 35.5 pF"; a "Periphery-intensive
MiM2 cap, CAP2M over M4. 72 plates each 2x35. […]" and an "Area-intensive
MiM2 capacitor, CAP2M over M4. 5 plates each 35x35."; "CAP2M linewidth,
L/W = 500/2.0" and "CAP2M linewidth, L/W = 400/1.0" lines; a "CAP2M sheet
rho, L/W = 45/4.5" structure; "CAP2M-CAP2M serp/comb" and "M4-M4
serp/comb structure, M4 is under CAP2M at min TDR S = 1.0" structures; a
"Via-4 chain, 1392 via-4, M5-CAP2M over M4 (min via enclosure)"; and
"CAPM-M3 and CAP2M-M4 capacitors, stacked on top of each other and
connected together. 11 pairs of plates, each 40x40" with "Total expected
capacitance 71 pF".[^raw-data-testtile-pads] The metal-4 comb gives a
"min TDR S" of 1.0 where the metal-3 comb under `CAPM` gives 1.2 (our
comparison); the test tile does not explain the difference. The mask does
not define the dielectric or plate film ({ref}`CAPILD2 <step-150>`,
{ref}`CAPTIW2 <step-151>`), the bottom plates, which on the step pages'
readings are cut from metal 4 by the {ref}`MM4 <step-154>` mask, or the
via-4 contacts ({ref}`mask-vim4`).

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` lists the drawn layer `cap2m` at 97:44, "MiM capacitor
plate over metal 4", on a layer number that also carries the `chvtpm`
mask purpose at 97:0 and its mask-drop and mask-add purposes at 97:42 and
97:43; it has no mask-level (`c…`) layer for a second capacitor
mask.[^pdk-06] With no `masks.csv` entry, the pairing of the step's mask
with `cap2m` is not a match of names but the reading of the step page and
the masks index, which the layer description, the device page's "CAP2M
over Metal-4" and the test tile support.[^pdk-06][^pdk-07][^raw-data-testtile-pads]
No periphery rule names `cap2m`: the row of rule x.2 that limits `capm`
and other layers to "n x 90" degree angles does not list it, and rule
x.22, which flags floating "capm", does not mention it.[^pdk-periph] The
PDK's *Error Messages* page, which describes "many of the automated DRC
rules that are checked by SkyWater as part of the acceptance criteria for
GDS data", does name it, in two module-cut checks, "0.42 min. spacing of
moduleCutAREA & cap2m" (x.18a) and "0.42 min. enclosure of cap2m by
moduleCutAREA" (x.18b), which give no plate geometry; it lists no
"nikon cross" check for either capacitor mask, as it does for the metal
and via masks.[^pdk-errors]
Table 7's "MiM Capacitor aspect ration" of 20 (`MiM_AR`) names no
capacitor; the step page treats it as published for the first and applies
it to the second (inference).[^pdk-03]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `CAP2M` the site renders layer 97:44 (`cap2m`)
alone, with no Boolean expression and no fill layer, on all eight runs;
its mask record gives the description "Capacitor mask", which is the step
list's description of step 152, no mask-level layer, no info text, no
note and no value for use in SKY130.[^mask-renders][^steps-sheet] The
layer is the one this reference pairs with the mask, and the masks index
lists `CAP2M` among the masks for which the renders and its pairings
agree; both derive from the same public files, so the agreement is no
independent confirmation, and the site's choice is one public derivation
from the drawn data, not SkyWater's mask-generation recipe
({ref}`masks-derivations`). The sheet's "Run Mask IDs" row for `CAP2M`
carries the "Info" note "step 152 'Capacitor mask'; plate 582", which
repeats the step list's description and the plate number and adds no
evidence of its own.[^steps-sheet]

The die count is not a count of designs with a second MiM capacitor. On
MPW-1, 39 dies carry `cap2m` shapes, each exactly one, and one die (frame
D4) carries none; on the other seven runs all 40 dies carry shapes, and
the number carrying exactly one is 38, 39, 39, 36, 37, 36 and 36 on MPW-2
to MPW-8 in turn. The other dies carry from 3 to 119 701
shapes.[^mask-renders] We read the single shape as common to the dies
rather than to the projects (inference), as the
{ref}`CAPM mask page <mask-capm>` does for `capm`; the site does not say
what it is. On MPW-1 the same frame, D4, is also the one die with no
`capm` shape, and the one die with 119 701 shapes on MPW-7 (frame B7) and
on MPW-8 (frame B3) carries the same count on `capm` (our comparison).
The site states the limits of its images: "These are renders of *drawn*
data, not photomask artwork: reticle pitch, 4x reduction, mirroring and
the frame features the fab adds are not modelled."[^mask-renders] Its
metadata carries no plate ID, so a render is tied to a plate in the sheet
only by the acronym `CAP2M`, and the MPW-4 renders come from a different
reticle set from the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet has a row "Capacitor
MiM 2, CAP2M", one of five rows that `masks.csv` does not have, and marks
a plate as existing on all eight MPW runs, with the plate number `582` on
each ({ref}`masks-mpw-runs`).[^steps-sheet] The plate IDs below are the
sheet's; the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA582A` |
| MPW-2 | `5CS8007AC` | `S8007AA582A` |
| MPW-3 | `5CS8008AC` | `S8008AA582A` |
| MPW-4 | `5CS8018AC` | `S8018AA582A` |
| MPW-5 | `5CS8011AC` | `S8011AA582A` |
| MPW-6 | `5CS8014AC` | `S8014AA582A` |
| MPW-7 | `5CS8016AC` | `S8016AA582A` |
| MPW-8 | `5CS8017AC` | `S8017AA582A` |

* **A plate without a PDK entry.** The sheet records a `CAP2M` plate on
  every run although `masks.csv` does not list the mask; the plates show
  that a second capacitor level was recorded for each MPW set, not that
  every die uses it (see the renders above).[^steps-sheet][^pdk-05]
* **Plate number.** The sheet does not say what `582` encodes. It falls
  between `580` for `MM4` and `585` for `VIM4`. From `500` to `590` the
  via and metal numbers rise in step order, but each capacitor mask is
  numbered 2 above the metal mask that follows it: `CAP2M` (step 152) is
  `582` against `MM4` (step 154) `580`, as `CAPM` (step 137) is `572`
  against `MM3` (step 139) `570` (our comparison).[^steps-sheet]
  Elsewhere the numbers do not follow process order, and no process
  position is read from them
  ({ref}`masks-mpw-reticle-sets`).
* **Mask type.** The sheet's "Sheet4" tab gives no type for
  `CAP2M`.[^steps-sheet] The {ref}`CAP2M <step-152>` page reads the plate
  as a binary chrome-on-glass mask without OPC; that is not on public
  record.
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`CAP2M <step-152>` page gives
{math}`k_1 = 0.84 \times 0.6 / 0.365 \approx 1.4` for the `capm` space on
an i-line lens of NA 0.6, with the geometry assumed equal to `capm`'s, and
infers an i-line level, quoting ASML's statement that older systems
"migrate to the lithography of choice for less critical
layers";[^asml-30] the {ref}`i-line stepper <machine-i-line-stepper>` page
lists it there. SkyWater lists "ASML I-line stepper" and "ASML I-line
scanner" but assigns no layer to them.[^skw-01]

**Mask errors and the plate.** Wong et al. found that the mask error
factor "is unity for large features, but increases rapidly when the
critical dimension (CD) is less than 0.5 (lambda) /NA for line-space
patterns";[^wong-1998] at 365 nm and NA 0.6 that is about 0.30 µm (our
arithmetic), far below the assumed 0.84 µm space, so plate CD errors
would print at their own size (inference). Plates of this size are well
within what laser reticle writers of the period and wet-etched chrome
handled (our reading): a laser writer of the ALTA family addressed "the
needs of maskmakers in the 180 nm and 150 nm technology
nodes",[^morgante-2000] and chrome masks "have traditionally been wet
etched".[^buck-1994] The handbook edited by Rizvi covers mask writers and
conventional optical masks.[^rizvi-2005] None of this is recorded for the
`CAP2M` plate.

**Stacked plates.** If the layout stacks the two capacitors, as the device
page allows, the `cap2m` plate is drawn over a `capm` plate one level down,
and the PDK's stacked cross-section draws both plates with the same
outline (the step page's reading of the drawing);[^pdk-07] a
misregistration between the two levels would change the area over which
their fields overlap (inference, on the step page). Kar-Roy, Racanelli and
Kempf stack an upper and a lower MiM capacitor between interconnect levels
and join them in parallel,[^pat-mim-stack-newportfab] and Chang, Lee and
Chen cross-connect stacked plates through filled
vias;[^pat-mim-stack-tsmc] Shyu, Temes and Krummenacher derived how random
errors in capacitance ratios depend on the physical dimensions and the
process spread, for MOS capacitors.[^shyu-1984] Ng et al. review MiM
integration in Al–Cu and copper back ends.[^ng-2005]

**Reflective substrate.** On the step pages' readings the resist sits on
a refractory plate film over some 20–30 nm of dielectric (the
{ref}`CAPILD2 <step-150>` page's estimate) on the unpatterned metal-4
stack. Brunner showed that the swing ratio scales with
the square root of the substrate reflectivity;[^brunner-1991] Rocke and
Schneegans used titanium nitride on aluminium as an anti-reflection
layer.[^rocke-1988] The step page reads an organic {term}`BARC` or dyed
resist and a positive DNQ/novolac i-line resist, the chemistry of
Dammel's text;[^dammel-1993] with the resist left where `cap2m` is drawn,
the plate would be clear-field (inference). Neither is published. The
consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Pattern transfer.** On the step pages' readings the resist pattern is
transferred by {ref}`CAP2ME <step-153>`, an etch of the plate film on the
{ref}`metal plasma etcher <machine-plasma-etcher-metal>` class that stops
on, or a little way into, the capacitor dielectric, with the resist strip
treated as part of that step; the step page repeats {ref}`CAPME <step-138>`
one level higher. The Newport Fab patent patterns its top
plate on unpatterned interconnect metal before the bottom
plate.[^pat-mim-newportfab]

**Overlay and charging.** Each plate must lie inside a metal-4 shape
printed later and enclose the via-4 openings that contact it, by margins
the PDK does not publish; the {ref}`CAP2M <step-152>` page reads the mask
as aligned to the via-3 level under the unpatterned metal (inference).
Wang, Ackaert et al. showed that plasma-charging damage of floating MiM
capacitors depends on the antenna areas connected to each
plate,[^wang-2004-mim] which the step page reads as making the plate area
one term in the charging exposure of later plasma steps until via 4
connects it.

(mask-cap2m-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `CAP2M` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`CAP2M <step-152>`, {ref}`CAP2ME <step-153>`

* {ref}`CAP2M <step-152>` — coats, exposes and develops the resist.
* {ref}`CAP2ME <step-153>` — etches the plate film through the resist;
  the step list used in this reference has no separate strip step, and
  the step page treats the resist strip and clean as part of the etch.

On its step page's reading, the next step, {ref}`MM4 <step-154>`, coats
and exposes a new resist for the metal-4 pattern over the finished plates,
after the `CAP2M` resist has been stripped. That step is also the next
mask step. The rule needs no exception for this mask.

## Design rules and critical dimensions

The periphery rules have no `cap2m` rule set, and the only published
checks naming `cap2m` are the two module-cut checks quoted
above.[^pdk-errors] The table gives the rules
that bear on the mask only by analogy or in general: rule capm.7, which
the {ref}`CAP2M <step-152>` page applies to the second capacitor
(inference from the "identical" construction), rule capm.6, whose subject
matches `MiM_AR` (our reading), and the mask-data rules x.7 and x.15a.
Flag P means "Rule applies to periphery only (outside areaid.ce). A
corresponding core rule may or may not exist." and NC "Rule not checked
by DRC. It should be used as a guideline only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| capm.6 | "Maximum Aspect Ratio (Length/Width)" | N/A |
| capm.7 | "Only rectangular capacitors are allowed" | N/A |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |

Table 2 of *Criteria & Assumptions* has no row for the second capacitor;
its "Capacitor MiM" row gives a feature size of 2 (`CAPMCD`) and a space
size of 0.84 (`CAPMCDSP`), which the step page borrows. Table 7 gives the
"MiM Capacitor aspect ration" of 20 (`MiM_AR`) without naming a
capacitor, and no other criterion names `cap2m`.[^pdk-03] For the plate
the only published figures are therefore those borrowed from `capm`: a
2 µm minimum feature on a 0.84 µm space (inference); the test tile's
2.0 µm and 1.0 µm linewidth lines are drawn at, and below, that
width.[^raw-data-testtile-pads]

## Related pages

* {ref}`CAP2M <step-152>` and {ref}`CAP2ME <step-153>` — the mask step and
  the plate etch; {ref}`CAPILD2 <step-150>` and
  {ref}`CAPTIW2 <step-151>` — the dielectric and plate film.
* {ref}`mask-capm` — the first capacitor's mask; {ref}`mask-vim3` — the
  via mask printed before it; {ref}`mask-vim4` — the via mask whose holes
  land on its plates.
* {ref}`masks index <masks-index>` — every mask's PDK entry, plates and
  renders, including the masks `masks.csv` does not list.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-plasma-etcher-metal` — the etch class that transfers the
  pattern.
* {ref}`material-lithography-materials` — resists, anti-reflective
  coatings, developer and reticles.
* {ref}`category-lithography` and {ref}`category-etch` — the mask step
  and etch categories.

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — no entry for a second
  capacitor mask.[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `cap2m` 97:44,
  the layer-97 `chvtpm` purposes, Tables C3 and F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — the "Capacitor MiM" row of
  Table 2 and `MiM_AR`.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `capm` rules, x.2, x.7, x.15a,
  x.22 and the flag legend.[^pdk-periph]
* [SkyWater PDK, *Error Messages* page](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) — the module-cut checks naming
  `cap2m`.[^pdk-errors]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — "CAP2M over Metal-4", `CMIM2A`,
  `CMIM2P`, the MiM2 top-plate resistance and the stacked
  cross-section.[^pdk-07]
* [SkyWater PDK, *Process stack diagram*](<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>) — the `cap2m` layer.[^pdk-04]
* [SkyWater PDK Authors, test-tile pad documentation](<https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>) — the `CAP2M`
  capacitor, linewidth, comb, via-4 and stacked
  structures.[^raw-data-testtile-pads]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the "Capacitor MiM 2" row
  with its plates and "Info" note, and the mask-type tab.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `CAP2M` renders, their layer
  and mask record, and the per-die shape counts.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the i-line exposure
  tools.[^skw-01]
* [ASML, *Three decades of PAS 5500*](<https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>) — older exposure tools moving to less
  critical layers.[^asml-30]
* [SkyWater PDK Authors, repository README](<https://github.com/google/skywater-pdk>) — "Optional MiM capacitors"
  and optional features included "as standard".[^pdk-10]

### High-level understanding

* [Wikipedia, *Photomask*](<https://en.wikipedia.org/wiki/Photomask>) — reticles, absorbers and
  pellicles.[^wiki-mask]
* [Wikipedia, *Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) — i-line exposure.[^wiki-litho]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — imaging of large
  features, swing curves and BARCs.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on masks and reticles
  and on overlay.[^levinson-2005]

### Deep dive

* [Kar-Roy, Racanelli and Kempf (Newport Fab), US 7,078,310](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7078310>) — two stacked
  MiM capacitors joined in parallel.[^pat-mim-stack-newportfab]
* [Chang, Lee and Chen (TSMC), US 7,317,221](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7317221>) — stacked plates
  cross-connected through filled vias.[^pat-mim-stack-tsmc]
* [Kar-Roy and Racanelli (Newport Fab), US 6,430,028](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6430028>) — the top plate
  patterned before the bottom-plate metal.[^pat-mim-newportfab]
* [Shyu, Temes and Krummenacher, *IEEE JSSC* 1984](<https://doi.org/10.1109/JSSC.1984.1052250>) — random errors in
  capacitance ratios as functions of dimensions and process
  spread.[^shyu-1984]
* [Wang, Ackaert et al., *IEEE TED* 2004](<https://doi.org/10.1109/TED.2004.829518>) — plasma-charging damage of
  floating MiM capacitors.[^wang-2004-mim]
* [Ng et al., *IEEE TED* 2005](<https://doi.org/10.1109/TED.2005.850642>) — MiM integration in Al–Cu and copper back
  ends.[^ng-2005]
* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor and the
  feature size above which it is unity.[^wong-1998]
* [Morgante and Hamaker, *Proc. SPIE* 2000](<https://doi.org/10.1117/12.392079>) — a laser reticle writer and the
  mask nodes it served.[^morgante-2000]
* [Buck and Grenon, *Proc. SPIE* 1994](<https://doi.org/10.1117/12.167247>) — wet against dry chrome etching of
  masks.[^buck-1994]
* [Rizvi (ed.), *Handbook of Photomask Manufacturing Technology*](<https://doi.org/10.1201/9781420028782>) — mask
  writers and conventional optical masks.[^rizvi-2005]
* [Brunner, *Proc. SPIE* 1991](<https://doi.org/10.1117/12.46410>) — swing curves and anti-reflection on
  reflective substrates.[^brunner-1991]
* [Rocke and Schneegans, *JVST B* 1988](<https://doi.org/10.1116/1.584306>) — titanium nitride as an
  anti-reflection layer on aluminium.[^rocke-1988]
* [Dammel, *Diazonaphthoquinone-based Resists*](<https://doi.org/10.1117/3.2265072>) — the i-line resist
  chemistry.[^dammel-1993]

## Open questions

* `masks.csv`, the minimum-CD table and the periphery rules have no entry
  or rule set for the second capacitor mask or for `cap2m`, and the
  published checks name `cap2m` only for module cuts;[^pdk-errors] the geometry on this page
  is borrowed from `capm` on the step page's reading of the "identical"
  construction.[^pdk-05][^pdk-03][^pdk-periph][^pdk-07]
* The sheet records a `CAP2M` plate on every MPW run, and the README
  lists "Optional MiM capacitors" but also counts MiM capacitors among the
  "normally optional features" SKY130 includes "as standard"; whether every die or lot uses the
  second capacitor is not public, and the renders do not say what the
  single `cap2m` shape common to most dies is.[^steps-sheet][^pdk-10][^mask-renders]
* The *Device Details* table lists the MiM2 top-plate sheet resistance
  under the first capacitor's name, `RSCAPM`; the PDK does not say whether
  that is a misprint.[^pdk-07]
* The plate's type, tone and CD specification, the resist, the exposure
  tool and the alignment tree between `CAP2M`, `CAPM` and `MM4` are not
  public.
* What the plate number `582` encodes is not stated, and no public source
  lists the `CAP2M` plate of the original MPW-4 set
  `5CS8010AC`.[^steps-sheet][^mask-renders]

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tabs "Sheet1" (step number, code and description), "Masks"
    (mask steps with step numbers), "Run Mask IDs" (the mask table set
    against MPW-1 to MPW-8, with "Exists", "Plate ID" and "Info" columns)
    and "Sheet4" (mask types), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* (including Table C3,
    the device and CAD definitions, and Table F2b, the mask generation
    table) and `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2 and
    7), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (MiM capacitors),
    SkyWater SKY130 PDK documentation, and the `cap_mim` cross-section
    drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/cap_mim/cross-section-cap_mim.svg>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README. <https://github.com/google/skywater-pdk>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_CAP2M/` and
    `mpw-00N_CAPM/` directories with their pages, `job.json`,
    `result.json` and per-die slot JSON files, retrieved 2026-09-14.
    Rendered from the public shuttle repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021, accessed
    2026-09-13. <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^pat-mim-stack-newportfab]: A. Kar-Roy, M. Racanelli and P. Kempf
    (Newport Fab, LLC), *Method for fabricating a high density composite
    MIM capacitor with flexible routing in semiconductor dies*,
    US 7,078,310 B1, filed 2004-05-19, granted 2006-07-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7078310>
[^pat-mim-stack-tsmc]: K.-L. Chang, C.-Y. Lee and C.-H. Chen (Taiwan
    Semiconductor Manufacturing Co.), *High density MIM capacitor
    structure and fabrication process*, US 7,317,221 B2, filed
    2003-12-04, granted 2008-01-08.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7317221>
[^pat-mim-newportfab]: A. Kar-Roy and M. Racanelli (Newport Fab, LLC),
    *Method for fabrication of an MIM capacitor and related structure*,
    US 6,430,028 B1, filed 2000-11-22, granted 2002-08-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6430028>
[^shyu-1984]: J.-B. Shyu, G. C. Temes and F. Krummenacher, "Random error
    effects in matched MOS capacitors and current sources", *IEEE Journal
    of Solid-State Circuits* **19**(6), 948–956 (1984).
    <https://doi.org/10.1109/JSSC.1984.1052250>
[^wang-2004-mim]: Z. Wang, J. Ackaert, C. Salm, F. G. Kuper, M. Tack,
    E. De Backer, P. Coppens, L. De Schepper and B. Vlachakis,
    "Plasma-charging damage of floating MIM capacitors", *IEEE
    Transactions on Electron Devices* **51**(6), 1017–1024 (2004).
    <https://doi.org/10.1109/TED.2004.829518>
[^ng-2005]: C. H. Ng, C.-S. Ho, S.-F. S. Chu and S.-C. Sun, "MIM
    Capacitor Integration for Mixed-Signal/RF Applications", *IEEE
    Transactions on Electron Devices* **52**(7), 1399–1409 (2005).
    <https://doi.org/10.1109/TED.2005.850642>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**,
    Optical Microlithography XI, 106 (1998).
    <https://doi.org/10.1117/12.310718>
[^morgante-2000]: C. G. Morgante and H. C. Hamaker, "ALTA 3700:
    extending the application space of the ALTA 3500 laser reticle
    writer", *Proc. SPIE* **4066**, 613 (2000).
    <https://doi.org/10.1117/12.392079>
[^buck-1994]: P. D. Buck and B. J. Grenon, "Comparison of wet and dry
    chrome etching with the CORE-2564", *Proc. SPIE* **2087**, 42–49
    (1994). <https://doi.org/10.1117/12.167247>
[^rizvi-2005]: S. Rizvi (ed.), *Handbook of Photomask Manufacturing
    Technology*, CRC Press, 2005, ISBN 978-1-4200-2878-2.
    <https://doi.org/10.1201/9781420028782>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^rocke-1988]: M. Rocke and M. Schneegans, "Titanium nitride for
    antireflection control and hillock suppression on aluminum silicon
    metallization", *Journal of Vacuum Science & Technology B* **6**(4),
    1113–1115 (1988). <https://doi.org/10.1116/1.584306>
[^dammel-1993]: R. R. Dammel, *Diazonaphthoquinone-based Resists*, SPIE
    Tutorial Texts TT11, SPIE Press, 1993.
    <https://doi.org/10.1117/3.2265072>
