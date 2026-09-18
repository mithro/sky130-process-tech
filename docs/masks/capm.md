(mask-capm)=
# CAPM — Capacitor MiM

The capacitor mask is the {term}`reticle` that draws the top plates of
SKY130's first {term}`MiM capacitor`: on the {ref}`CAPM <step-137>`
page's reading, the resist printed through it at step 137 stays wherever
`capm` is drawn, on the blanket plate film of
{ref}`CAPTIW1 <step-136>` (TiW, as assumed there), and the
{ref}`CAPME <step-138>` etch removes the film everywhere else. It is a
device mask rather than a wiring, contact or implant mask, and a coarse
one, with a 2 µm minimum feature. Its public record is uneven:
`masks.csv` lists it with the `Used in SKY130` field blank and
`gds_layers.csv` gives it no mask-level layer, yet the process-steps
sheet records a plate on every MPW run, and the public renders show
`capm` shapes on 39 or 40 dies of every run — most of them a single
shape. This page gathers what public sources say about the mask
itself — its PDK entry and layers, the plates the process-steps sheet
records for the MPW runs, what the public renders of those runs show,
the lithography it needs and the rules that constrain it. How the step
is performed is on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | CAPM — Capacitor MiM |
|---|---|
| Mask step | {ref}`CAPM <step-137>`, step 137 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Capacitor MiM", `CAPM`, unmarked[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | none[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `capm` drawing 89:44, "MiM capacitor plate over metal 3"[^pdk-06] |
| Minimum CD, feature / space | `CAPMCD` 2 / `CAPMCDSP` 0.84[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist remains where `capm` is drawn, which with a positive resist would make the plate clear-field (inference). |
| Exposure class | i-line, an inference on the step page from the 2 µm and 0.84 µm rules, with a KrF tool able to print the layer but not needed; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `572`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 39, 40, 40, 40, 40, 40, 40, 40[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-capm-steps>` |

## What the mask defines

The periphery rules give the function of the `capm` rule set as
"Defines MIM capacitor", and publish twelve rules for it — minimum
width, spacings, enclosures, a maximum aspect ratio, a rectangles-only
rule, a no-straddle rule and a maximum area — every one with the value
"N/A".[^pdk-periph] The PDK's *Error Messages* page, which describes "many
of the automated DRC rules that are checked by SkyWater as part of the
acceptance criteria for GDS data", gives one check naming `capm` with a
value, "0.42 min. enclosure of capm by moduleCutAREA" (x.18b), which
gives no plate geometry.[^pdk-errors] The *Device Details* page describes the device the
mask draws: "The MiM capacitor is constructed using a thin dielectric
over metal, followed by a thin conductor layer on top of the dielectric.
There are two possible constructions:" "CAPM over Metal-3" and "CAP2M
over Metal-4", which are "identical" and "may be stacked to maximize total
capacitance"; it gives an area capacitance `CMIMA` of 2 fF/µm² (limits
1.8–2.2), a periphery capacitance `CMIMP` of 0.19 fF/µm (0.11–0.27) and
a "MiM top plate sheet resistance" `RSCAPM` of 5.8 Ω/□
(4.8–6.8).[^pdk-07] The mask therefore sets both terms of the
capacitance: the plate area and its perimeter (the
{ref}`CAPM <step-137>` page's reading of the model form). The PDK's
cross-section of the stacked capacitor labels "CAPM" and "CAPILD" above
a wider "M3 (plate 1)", and a "Via3".[^pdk-07]

The PDK's CAD definitions tie the mask to the via and metal below it.
Table C3 of the *Layers Reference* defines "top_plate" as "capm:dg",
"bottom_plate" as "(capm:dg AND met2:dg) sized by capm.3; Exclude all
capm sharing same metal2 plate", "Capacitor" as "Capm enclosing at least
one via2" and "dummy_capacitor" as "Capm not overlapping via2", and
Table C4b lists a "capm_2t.dg" layer, "MIM caps (2 terminal model)", an
"ID layer for MIMCAP that will be treated as 2T device"; Table F2b, the
mask generation table, marks the `CAPM` column `C` ("CREATED") in the
"MiM" row only, `-` in the two VPP capacitor rows and `+`, "Layer allowed
to overlap", in the other 77; in that row the `MM2` column is also `C`
and the `MM3` column `+` ({ref}`mask-mm2`).[^pdk-06] Table F4 of the *Summary of Key
Periphery Rules* gives "Via2" as the connection between `Capm` and
`Met3`.[^pdk-summary] These definitions and rules capm.3–capm.5 name
metal 2 and via 2, while the layer description, the device page and the
test tile put the plate over metal 3;[^pdk-06][^pdk-07][^raw-data-testtile-pads]
the {ref}`CAPM <step-137>` page reads the rules for metal 3 and via 3
in the flow described here, and the {ref}`CAPILD <step-135>` page
suggests that the metal-2 wording may come from a flow variant with the
capacitor one level lower (both inferences); the function line of the
via-2 rules names a "SKY130DI\*" flow in which via 2 connects "met2/capm
to met3".[^pdk-periph] The test tile's second large capacitor, "Same
capacitor as 4530", notes "Caps have seas of via-2's placed under
M3/CAPM", so via-2 plugs do lie under some metal-3 plates; the step
pages' reading of the capm rules for via 3 does not rest on their
absence.[^raw-data-testtile-pads]

The published SKY130 {term}`test tile` shows what the mask is expected
to print on test structures: a "Large MiM capacitor, CAPM on M3, 11
plates, each 40x40" with "Total expected capacitance 35.5 pF"; a
"Periphery-intensive MiM cap, CAPM on M3. 72 plates each 2x35." and an
"Area-intensive MiM cap, CAPM on M3. 5 plates each 35x35."; "CAPM
linewidth, L/W = 500/2.0" and "CAPM linewidth, L/W = 400/1.0" lines; a
"CAPM sheet rho, L/W = 45/4.5" structure; and "CAPM-CAPM serp/comb" and
"M3-M3 serp/comb structure, M3 is under CAPM at min TDR S =1.2"
structures.[^raw-data-testtile-pads] The 1.0 µm linewidth structure is
half the 2 µm `CAPMCD` (our comparison); the test tile does not say how
it relates to that value. The mask does not define the capacitor dielectric or the
plate film ({ref}`CAPILD <step-135>`, {ref}`CAPTIW1 <step-136>`), the
bottom plates, which on the step pages' readings are cut from metal 3 by
the {ref}`MM3 <step-139>` mask, or the via-3 contacts to the plates
({ref}`VIM3 <step-144>`).

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` lists the drawn layer `capm` at 89:44, "MiM capacitor
plate over metal 3", and no mask-level (`c…`) layer for this mask; no
other entry uses layer number 89.[^pdk-06] The pairing of the mask with
`capm` rests on the name alone, as on the
{ref}`masks index <masks-index>`, and the PDK publishes no operation from
the drawn layer to the plate. With no mask-level layer, rules x.9 and
x.15a have no `CAPM` layer to govern, and a design draws `capm` (our
reading). One row of rule x.2 limits `capm`, among other layers, to "n x
90" degree angles; rule x.22 flags floating "capm" as it does floating
interconnect; and `capm` falls under the 0.005 grid of rule x.1b, not
the 0.001 grid of x.1a.[^pdk-periph] Table 7 of *Criteria & Assumptions*
gives a "MiM Capacitor aspect ration" of 20 (`MiM_AR`) in the column
headed "CD", the only criterion named for the capacitor besides Table
2's `CAPMCD` and `CAPMCDSP`; rule capm.6, "Maximum Aspect Ratio
(Length/Width)", has no value.[^pdk-03][^pdk-periph]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `CAPM` the site renders layer 89:44 (`capm`)
alone, with no Boolean expression and no fill layer, on all eight runs;
its mask record gives the description "Capacitor MiM", no mask-level
layer, no info text and no note, and marks the mask as not used in
SKY130, as `masks.csv` does.[^mask-renders] The layer is the one this
reference pairs with the mask; both choices derive from the same public
files, so the agreement is no independent confirmation, and the site's
choice is one public derivation from the drawn data, not SkyWater's
mask-generation recipe ({ref}`masks-derivations`). The sheet's "Run Mask
IDs" row for `CAPM` has no "Info" note.[^steps-sheet]

The die count is not a count of designs with MiM capacitors. On MPW-1,
39 dies carry `capm` shapes and one (frame D4) carries none; on the other
seven runs all 40 do. The minimum per-die count is one shape, and the
number of dies carrying exactly one shape is 36, 35, 34, 38, 34, 36, 33
and 35 on MPW-1 to MPW-8 in turn; on MPW-3 two further dies carry
exactly two. The other dies carry from 2 to 119 701
shapes.[^mask-renders] We read the single shape as common to the dies
rather than to the projects (inference), as the
{ref}`DNM mask page <mask-dnm>` reads its repeated counts; the site does
not say what it is. The site states the limits of its images: "These are
renders of *drawn* data, not photomask artwork: reticle pitch, 4x
reduction, mirroring and the frame features the fab adds are not
modelled."[^mask-renders] Its metadata carries no plate ID, so a render
is tied to a plate in the sheet only by the acronym `CAPM`, and the
MPW-4 renders come from a different reticle set from the one whose plates
the sheet records ({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a `CAPM` plate
as existing on all eight MPW runs, with the plate number `572` on
each.[^steps-sheet] The plate IDs below are the sheet's; the reticle set
is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA572A` |
| MPW-2 | `5CS8007AC` | `S8007AA572A` |
| MPW-3 | `5CS8008AC` | `S8008AA572A` |
| MPW-4 | `5CS8018AC` | `S8018AA572A` |
| MPW-5 | `5CS8011AC` | `S8011AA572A` |
| MPW-6 | `5CS8014AC` | `S8014AA572A` |
| MPW-7 | `5CS8016AC` | `S8016AA572A` |
| MPW-8 | `5CS8017AC` | `S8017AA572A` |

* **A plate for an unmarked entry.** `masks.csv` leaves the `Used in
  SKY130` field blank for "Capacitor MiM", and the sheet's row repeats
  the blank, yet it records a plate on every run; the masks index lists
  this among the entries the PDK table does not mark
  ({ref}`masks-mpw-runs`).[^pdk-05][^steps-sheet] The plates show that a
  `CAPM` level was recorded for each MPW set, not that every die uses
  it (see the renders above).
* **Plate number.** The sheet does not say what `572` encodes. It falls
  between `570` for `MM3` and `575` for `VIM3`. From `500` to `590` the
  via and metal numbers rise in step order, but each capacitor mask is
  numbered 2 above the metal mask that follows it: `CAPM` (step 137) is
  `572` against `MM3` (step 139) `570`, and `CAP2M` (step 152) `582`
  against `MM4` (step 154) `580` (our comparison).[^steps-sheet]
  Elsewhere the numbers do not follow process order, and no process
  position is read from them
  ({ref}`masks-mpw-reticle-sets`).
* **Mask type.** The sheet's "Sheet4" tab gives no type for
  `CAPM`.[^steps-sheet] The {ref}`CAPM <step-137>` page reads the plate
  as a binary chrome-on-glass mask without OPC; that is not on public
  record. 4× is the ITRS 2001 mask magnification for the 130 nm
  generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`CAPM <step-137>` page gives
{math}`k_1 = 0.84 \times 0.6 / 0.365 \approx 1.4` on an i-line lens of
NA 0.6, "far above the resolution limit", and infers an i-line level
from the rules and from ASML's statement that older systems "migrate to
the lithography of choice for less critical layers";[^asml-30] the
{ref}`i-line stepper <machine-i-line-stepper>` page lists it there.
SkyWater lists "ASML I-line stepper" and "ASML I-line scanner" but
assigns no layer to them.[^skw-01]

**Mask errors and the plate.** Wong et al. found that the mask error
factor "is unity for large features, but increases rapidly when the
critical dimension (CD) is less than 0.5 (lambda) /NA for line-space
patterns";[^wong-1998] at 365 nm and NA 0.6 that is about 0.30 µm (our
arithmetic), far below the 0.84 µm space, so plate CD errors would print
at their own size (inference). At 4× a 2 µm plate is 8 µm on the reticle
(our arithmetic), well within what laser reticle writers and wet-etched
chrome handled (our reading): a laser writer of the ALTA family addressed
"the needs of maskmakers in the 180 nm and 150 nm technology
nodes",[^morgante-2000] and chrome masks "have traditionally been wet
etched", with an undercut compensated by sizing the data.[^buck-1994]
The handbook edited by Rizvi covers both kinds of writer and conventional
optical masks.[^rizvi-2005] None of this is recorded for the `CAPM`
plate.

**Why the plate CD matters.** Because the model adds `CMIMP` per micron
of perimeter to `CMIMA` per square micron,[^pdk-07] a bias on the plate
edge changes the capacitance of small plates most: the step page puts a
0.1 µm bias on a 2 µm plate at 10 %, and on a 40 µm × 40 µm test-tile
plate the same bias changes the area term by about 0.5 % (our
arithmetic, with the bias applied to both dimensions). Shyu, Temes and Krummenacher derived the random errors of
capacitance ratios as functions of the physical dimensions and the
spread of the fabrication parameters, for MOS capacitors;[^shyu-1984]
the test tile's area- and periphery-intensive capacitors, with their
expected capacitances, are the structures from which the
{ref}`CAPME <step-138>` page separates the two
terms.[^raw-data-testtile-pads]

**Reflective substrate.** On the step pages' readings the resist sits on
the plate film over a few tens of nanometres of dielectric (the
{ref}`CAPILD <step-135>` page's estimate) on the capped metal-3
stack. Brunner showed that the swing ratio scales with
the square root of the substrate reflectivity;[^brunner-1991] Rocke and
Schneegans used titanium nitride on aluminium as an anti-reflection
layer.[^rocke-1988] The step page reads an organic {term}`BARC` or dyed
resist and a positive DNQ/novolac i-line resist, the chemistry of
Dammel's text;[^dammel-1993] with the resist left where `capm` is drawn,
the plate would be clear-field (inference). Neither is published. The
consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Pattern transfer.** On the step pages' readings the resist pattern is
transferred by {ref}`CAPME <step-138>`, an etch of the plate film on the
{ref}`metal plasma etcher <machine-plasma-etcher-metal>` class that stops
on, or a little way into, the capacitor dielectric, with the resist strip
treated as part of that step; whether the dielectric is also cut is
left open there. Top-plate-first constructions of this kind appear in
the Newport Fab and Freescale patents, and a damascene bottom plate in
IBM's;[^pat-mim-newportfab][^pat-mim-freescale][^pat-mim-ibm] Ng et al.
review MiM integration in Al–Cu and copper back ends.[^ng-2005]

**Overlay and charging.** On the step pages' reading the plate must lie
inside the metal-3 shape printed later and enclose the via-3 contacts, by
margins the PDK does not publish (capm.3 and capm.4, which name metal 2
and via 2).[^pdk-periph] The {ref}`CAPM <step-137>` page
reads the mask as aligned to the via-2 level under the unpatterned metal,
with {ref}`MM3 <step-139>` aligned to the same marks or to `capm`
(inference). Wang, Ackaert et al. showed that plasma-charging damage of
floating MiM capacitors depends on the antenna areas connected to each
plate,[^wang-2004-mim] so the plate area this mask draws is also one term
in the charging exposure of later plasma steps (the step pages' reading).

(mask-capm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `CAPM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`CAPM <step-137>`, {ref}`CAPME <step-138>`

* {ref}`CAPM <step-137>` — coats, exposes and develops the resist.
* {ref}`CAPME <step-138>` — etches the plate film through the resist;
  the step list used in this reference has no separate strip step, and
  the step page treats the resist strip and post-etch clean as part of
  the etch.

On its step page's reading, the next step, {ref}`MM3 <step-139>`, coats
and exposes a new resist for the metal-3 pattern over the finished
plates, after the `CAPM` resist has been stripped. That step is also the
next mask step. The rule needs no exception for this mask.

## Design rules and critical dimensions

The `capm` rules of the periphery rules and the mask-data rules x.1b,
x.2, x.7, x.15a and x.22 as they bear on `capm`. Flag TC means "Rule not
checked for cell name “\*_tech_CD_top\*”", P "Rule applies to periphery
only (outside areaid.ce). A corresponding core rule may or may not
exist.", RC "Recommended rule at the chip level, required rule at the IP
level." and NC "Rule not checked by DRC. It should be used as a guideline
only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| capm.1 | "Min width of capm" | N/A |
| capm.2a | "Min spacing of capm to capm" | N/A |
| capm.2b | "Minimum spacing of capacitor bottom_plate to bottom plate" | N/A |
| capm.3 | "Minimum enclosure of capm (top_plate) by met2" | N/A |
| capm.4 | "Min enclosure of via2 by capm" | N/A |
| capm.5 | "Min spacing between capm and via2" | N/A |
| capm.6 | "Maximum Aspect Ratio (Length/Width)" | N/A |
| capm.7 | "Only rectangular capacitors are allowed" | N/A |
| capm.8 | "Min space, no overlap, between via and capm" | N/A |
| capm.10 | "capm must not straddle nwell, diff, tap, poly, li1 and met1 (Rule exempted for capm overlapping capm_2t.dg)" (TC) | N/A |
| capm.11 | "Min spacing between capm to (met2 not overlapping capm)" | N/A |
| capm.12 | "Max area of capm (um^2)" | N/A |
| x.1b | "Data for SKY130 layout and mask on all layers except those mentioned in 1a must be on a grid of mm (except inside Seal ring)" | 0.005 (unit "mm") |
| x.2 | "Angles permitted on: tap (except inside areaid.en), poly […], li1(periphery), licon1, capm, mcon, via, via2. Anchors are exempted." | n x 90 deg |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
| x.22 | "No floating interconnects (poly, li1, met1-met5) or capm allowed; […] The following are exempt from x.22 violations: \_techCD\_ , inductor.dg, modulecut, capacitors and s8blerf […]" (RC) | — |

The rule set has no rule numbered capm.9. Table 2 of *Criteria &
Assumptions* gives "Capacitor MiM" a feature size of 2 (`CAPMCD`) and a
space size of 0.84 (`CAPMCDSP`), in a table without a unit column, and
Table 7 the aspect ratio of 20 (`MiM_AR`); no other criterion names the
MiM capacitor or `capm` (Table 10's criteria are for the VPP
capacitor).[^pdk-03] For the plate the decisive published
figures are a 2 µm minimum feature on a 0.84 µm space, a pitch of
2.84 µm (our arithmetic), and a rectangle no more than 20 times as long
as it is wide (our reading of `MiM_AR` with capm.6 and capm.7).

## Related pages

* {ref}`CAPM <step-137>` and {ref}`CAPME <step-138>` — the mask step and
  the plate etch; {ref}`CAPILD <step-135>` and
  {ref}`CAPTIW1 <step-136>` — the dielectric and plate film.
* {ref}`mask-vim2` — the via mask printed before it; {ref}`mask-vim4` —
  the via mask that lands on the second capacitor's plates.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the entries the PDK table does not mark.
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

* SkyWater PDK, *Masks* page and `masks.csv` — "Capacitor MiM, CAPM"
  with the `Used in SKY130` field blank.[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `capm` 89:44,
  Tables C3, C4b and F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `CAPMCD`/`CAPMCDSP` and
  `MiM_AR`.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `capm` rules, the via-2 function
  line, x.1b, x.2, x.7, x.9, x.15a, x.22 and the flag
  legend.[^pdk-periph]
* SkyWater PDK, *Summary of Key Periphery Rules* — Table F4.[^pdk-summary]
* SkyWater PDK, *Error Messages* page — the module-cut check naming
  `capm`.[^pdk-errors]
* SkyWater PDK, *Device Details* — the MiM constructions, `CMIMA`,
  `CMIMP`, `RSCAPM` and the stacked cross-section.[^pdk-07]
* SkyWater PDK Authors, test-tile pad documentation — the `CAPM`
  capacitor, linewidth, sheet-resistance and comb
  structures.[^raw-data-testtile-pads]
* *S8 / SKY130 Process Steps* sheet — the step, the `CAPM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `CAPM` renders, their layer
  and mask record, and the per-die shape counts.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the i-line exposure
  tools.[^skw-01]
* ASML, *Three decades of PAS 5500* — older exposure tools moving to less
  critical layers.[^asml-30]

### High-level understanding

* Wikipedia, *Photomask* — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wikipedia, *Photolithography* — i-line exposure.[^wiki-litho]
* Mack, *Fundamental Principles of Optical Lithography* — imaging of large
  features, swing curves and BARCs.[^mack-2007]
* Levinson, *Principles of Lithography* — chapters on masks and reticles
  and on overlay.[^levinson-2005]

### Deep dive

* Shyu, Temes and Krummenacher, *IEEE JSSC* 1984 — random errors in
  capacitance ratios as functions of physical dimensions and process
  spread.[^shyu-1984]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  feature size above which it is unity.[^wong-1998]
* Morgante and Hamaker, *Proc. SPIE* 2000 — a laser reticle writer and
  the mask nodes it served.[^morgante-2000]
* Buck and Grenon, *Proc. SPIE* 1994 — wet against dry chrome etching of
  masks.[^buck-1994]
* Rizvi (ed.), *Handbook of Photomask Manufacturing Technology* — mask
  writers, conventional optical masks and mask processing.[^rizvi-2005]
* Brunner, *Proc. SPIE* 1991 — swing curves and anti-reflection on
  reflective substrates.[^brunner-1991]
* Rocke and Schneegans, *JVST B* 1988 — titanium nitride as an
  anti-reflection layer on aluminium.[^rocke-1988]
* Dammel, *Diazonaphthoquinone-based Resists* — the i-line resist
  chemistry.[^dammel-1993]
* Ng et al., *IEEE TED* 2005 — MiM integration in Al–Cu and
  copper back ends.[^ng-2005]
* Kar-Roy and Racanelli (Newport Fab), US 6,430,028; Roberts and Huffman
  (Freescale), US 7,375,002; Brabazon et al. (IBM), US 5,708,559 — MiM
  constructions and their mask
  sequences.[^pat-mim-newportfab][^pat-mim-freescale][^pat-mim-ibm]
* Wang, Ackaert et al., *IEEE TED* 2004 — plasma-charging damage of
  floating MiM capacitors and its dependence on antenna
  areas.[^wang-2004-mim]

## Open questions

* `masks.csv` leaves the `Used in SKY130` field blank for "Capacitor
  MiM", and `gds_layers.csv` gives the mask no mask-level layer, while
  the sheet records a plate on every MPW run; the README lists "Optional
  MiM capacitors" and also counts MiM capacitors among the "normally
  *optional* features" included "as standard". The PDK does not explain
  the blank.[^pdk-05][^pdk-06][^pdk-10][^steps-sheet]
* Every `capm` rule value is published as "N/A", and the rules and CAD
  definitions name metal 2 and via 2 for a plate the layer table puts over
  metal 3; the reading for metal 3 and via 3 is an inference.[^pdk-periph][^pdk-06]
* The plate's type, tone and CD specification, the resist and the
  exposure tool are not public; the i-line reading rests on the 2 µm and
  0.84 µm values.
* The renders do not say what the single `capm` shape common to most dies
  is, so how many projects on each shuttle use MiM capacitors is not
  shown; the test tile's 1.0 µm linewidth structure, below `CAPMCD`, is
  not explained.[^mask-renders][^raw-data-testtile-pads]
* What the plate number `572` encodes is not stated, and no public source
  lists the `CAPM` plate of the original MPW-4 set
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
    the device and CAD definitions, Table C4b, the auxiliary layers, and
    Table F2b, the mask generation table) and `gds_layers.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2 and
    7), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-summary]: SkyWater PDK Authors, *Summary of Key Periphery Rules*
    (Table F4), SkyWater SKY130 PDK documentation, retrieved 2026-09-14.
    <https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (MiM capacitors),
    SkyWater SKY130 PDK documentation, and the `cap_mim` cross-section
    drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/cap_mim/cross-section-cap_mim.svg>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README. <https://github.com/google/skywater-pdk>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_CAPM/`
    directory with its page, `job.json`, `result.json` and per-die slot
    JSON files, retrieved 2026-09-14. Rendered from the public shuttle
    repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021, accessed
    2026-09-13. <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
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
[^shyu-1984]: J.-B. Shyu, G. C. Temes and F. Krummenacher, "Random error
    effects in matched MOS capacitors and current sources", *IEEE Journal
    of Solid-State Circuits* **19**(6), 948–956 (1984).
    <https://doi.org/10.1109/JSSC.1984.1052250>
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
[^ng-2005]: C. H. Ng, C.-S. Ho, S.-F. S. Chu and S.-C. Sun, "MIM
    Capacitor Integration for Mixed-Signal/RF Applications", *IEEE
    Transactions on Electron Devices* **52**(7), 1399–1409 (2005).
    <https://doi.org/10.1109/TED.2005.850642>
[^pat-mim-newportfab]: A. Kar-Roy and M. Racanelli (Newport Fab, LLC),
    *Method for fabrication of an MIM capacitor and related structure*,
    US 6,430,028 B1, filed 2000-11-22, granted 2002-08-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6430028>
[^pat-mim-freescale]: D. R. Roberts and G. L. Huffman (Freescale
    Semiconductor), *MIM capacitor in a semiconductor device and method
    therefor*, US 7,375,002 B2, filed 2005-06-28, granted 2008-05-20.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7375002>
[^pat-mim-ibm]: T. J. Brabazon, B. El-Kareh, S. R. Martin, M. J. Rutten
    and C. W. Kaanta (International Business Machines), *Precision
    analog metal-metal capacitor*, US 5,708,559 A, filed 1995-10-27,
    granted 1998-01-13.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5708559>
[^wang-2004-mim]: Z. Wang, J. Ackaert, C. Salm, F. G. Kuper, M. Tack,
    E. De Backer, P. Coppens, L. De Schepper and B. Vlachakis,
    "Plasma-charging damage of floating MIM capacitors", *IEEE
    Transactions on Electron Devices* **51**(6), 1017–1024 (2004).
    <https://doi.org/10.1109/TED.2004.829518>
