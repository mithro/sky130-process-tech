(mask-mm3)=
# MM3 — Metal 3-PLM

The metal-3 mask is the {term}`reticle` that draws SKY130's third
aluminium wiring level and, in the same pattern, the bottom plates of
the first {term}`MiM capacitor`. On the {ref}`MM3 <step-139>` page's
reading, the resist printed through it at step 139 stays wherever `met3`
is drawn, and the {ref}`MM3E <step-140>` etch removes the capacitor
dielectric and the metal stack everywhere else.

| | MM3 — Metal 3-PLM |
|---|---|
| Mask step | {ref}`MM3 <step-139>`, step 139 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Metal 3-PLM", `MM3`, marked `X` in `Used in SKY130`; "Metal 3-TLM", `MM3`, unmarked; "Metal 3-S8TM", `MM3`, unmarked[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cmm3` mask 34:0, "Metal 3 mask"; waffle drop 107:24[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `met3` drawing 70:20, "Metal 3"[^pdk-06] |
| Minimum CD, feature / space | `MM3CD` / `MM3CDSP`: "Metal 3-PLM" 0.3 / 0.3; "Metal 3-TLM" 0.36 / 0.36; "Metal 3-S8TM" 0.8 / 0.8[^pdk-03] |
| Polarity and tone | Not published; the PDK's `cmm3.nikon` checks name a polarity but not the plate's tone. On the step page's reading the resist remains where `met3` is drawn, which with a positive resist would make the plate clear-field (inference). |
| Exposure class | i-line or KrF (248 nm): the step page finds either plausible for the 0.3 µm line and leaves the class open; no public source names the tool ({ref}`machine-i-line-stepper`, {ref}`machine-duv-krf-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | Metal 3-PLM: all eight; Metal 3-TLM and Metal 3-S8TM: not recorded[^steps-sheet] |
| Plate no. | `570`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-mm3-steps>` |

:::{seealso}
How the step is performed is on
the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.
:::

## What the mask defines

The mask is the first of the
thick upper metals, with 0.3 µm lines, and the step pages leave open
whether it is printed on an i-line or a KrF tool. Like `VIM2`, it has
three `masks.csv` variants of which only one is marked as used in
SKY130, and the process-steps sheet records plates only for that one.

The periphery rules give the function of the `m3` rule set as "Defines
third level of metal interconnects, buses etc", and the PDK's Table F4
shows metal 3 joined to metal 2 by "Via2" and to metal 4 by "Via3".[^pdk-periph][^pdk-summary] Its
entry joining `capm` to metal 3 by "Via2" is part of the metal-2/via-2
wording discussed below.[^pdk-summary] The mask carries:[^pdk-periph]

* lines at the
  0.300 µm minimum width and space (m3.1, m3.2)
* pads that enclose the
  via-2 plugs below by 0.065 µm (m3.4) and the via-3 plugs above by
  0.060 µm (via3.4)
* wide "huge_met3" features that need 0.400 µm of space
  (m3.3c, m3.3d)
* on our reading of the waffle-drop rules below,
  dummy fill

The mask's smallest island is 0.240 µm² (m3.6).[^pdk-periph] The
PDK's extraction table gives metal 3 a sheet resistance of 47 in a
column headed "Resistivity (mohms/sq)", against 125 for metals 1 and
2,[^pdk-08] and the stack diagram draws `met3` 0.845 µm thick against
0.36 µm for metals 1 and 2.[^pdk-04]

The same pattern makes the capacitors' bottom plates. On the step pages'
readings the metal-3 stack stays blanket through the capacitor module
and every `capm` plate must end up inside a metal-3 shape. The PDK's
cross-section of the stacked capacitor labels the metal under "CAPM" "M3
(plate 1)".[^pdk-07]

Table C3 of the [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) defines
"bottom_plate" as "(capm:dg AND met2:dg) sized by capm.3; Exclude all
capm sharing same metal2 plate".[^pdk-06] Rule capm.3 is a "Minimum enclosure
of capm (top_plate) by met2" with the value "N/A".[^pdk-periph]
The {ref}`MM3 <step-139>` page reads that enclosure for metal 3 (rule
text: met2) in the flow described here.

Table F2b, the mask generation table, marks the `MM3` column `C`
("CREATED") in two of its 80 device rows: "metal fuse_D" and "VPP (with
met3 shield)".[^pdk-06] It marks `+`, "Layer allowed to overlap", in the other
78, including the "MiM" row, whose `C` marks are in the `CAPM` and `MM2`
columns ({ref}`mask-mm2`).[^pdk-06]

One row of rule x.11 reads "Metal fuses are drawn in met3",
with values "N/A", beside rows naming met2 and met4.[^pdk-periph] Table C3 gives the
"fuse_metal" as "met3 for S8TEE\*/S8TNV/S8Q\*/SP8TEE-5R/SP8Q\*; met2 for
S8D\*/S8TM\*, met4 for S8P\*/SP8P\*".[^pdk-06] The note above the fuse rules
reads "For SP8P\*/SKY130P\* (PLM) CADflow use MM4 for Metal
Fuse".[^pdk-periph]

We read the metal-3 fuse as belonging to
flows other than the one this reference follows, whose fuse level the
note puts on `MM4` (inference from the note and Table C3, with PLM read
as that flow's label as on the step page).

**Variants.** The three `masks.csv` entries — "Metal 3-TLM", "Metal
3-S8TM" and "Metal 3-PLM", with only "Metal 3-PLM" marked — have the
sizes 0.36, 0.8 and 0.3 in Table 2 of *Criteria & Assumptions*, under the
same variable names.[^pdk-05][^pdk-03] The {ref}`MM3 <step-139>` page
reads "S8TM" as a 2 µm thick-metal-3 option (inference from the
assumptions table's 2 µm "S8TM\* flow" thickness and the 0.8 µm
`MM3CD`) and PLM as the label of the five-metal P flow (inference), and
gives no reading of "TLM".

Table F3c of the [*Summary of Key Periphery
Rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>), "Back end layers for S8D\* flow", gives metal 3 a width and
spacing of 0.360 and a via-2 enclosure of "0.045 / 0.07".[^pdk-summary] Table F3d,
"Back end layers for S8T\* flow", gives a width and spacing of 2.500 and a via-2
enclosure of 0.310.[^pdk-summary] The F3c values equal the "Metal 3-TLM"
row of Table 2 (our comparison), and neither summary table has a row for
the 0.3 µm metal. The process-steps sheet lists all three variants and
records plates only for "Metal 3-PLM" ({ref}`masks-mpw-runs`).[^steps-sheet]

The mask does not define the metal stack it patterns, which
{ref}`WTIAL3 <step-134>` deposits, the capacitor films on it
({ref}`CAPILD <step-135>`, {ref}`CAPTIW1 <step-136>`,
{ref}`mask-capm`), the via-2 plugs beneath ({ref}`mask-vim2`) or the
via-3 plugs above (`VIM3`). On the step pages' readings the
dielectric that fills its spaces is deposited afterwards by
{ref}`NILD5 <step-141>` and polished by {ref}`CMPM3 <step-142>`.

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives the mask-level layer `cmm3` two purposes: `mask`
at 34:0 ("Metal 3 mask") and `waffle drop` at 107:24, on a different
layer number and without a description.[^pdk-06] The drawn layer is `met3` at
70:20.[^pdk-06] The pairing rests on those names and descriptions, as on
the {ref}`masks index <masks-index>`, and the PDK publishes no operation
from `met3` to the plate.

Rule x.15a confines "Drawn compatible, mask,
and waffle-drop layers" to test modules, seal ring and frame, "Exception:
FOM/P1M/Metal waffle drop are allowed inside the die" (flag P, periphery
only),[^pdk-periph] so a die may carry `cmm3` waffle-drop shapes as well
as `met3` (our reading). With no add or drop purpose, rule x.9's "serifs"
have no `cmm3` layer to sit on.

The rule set's first entry, flagged RC,
flags a 700 × 700 window "covered by cmm3 waffleDrop" when the metal
pattern density of the same window is below a limit that falls from 70 %
for a fully covered window to 30 % for one 30–40 % covered.[^pdk-periph] Rule
m3.pd.1 sets a minimum "MM3_oxide_Pattern_density" of 0.7, checked in
700 µm regions stepped by 70 (m3.pd.2a, m3.pd.2b, flag A).[^pdk-periph]

The PDK does not say whether a waffle-drop shape places fill or keeps it
out; the {ref}`MM3 <step-139>` page reads the `cmm3` fill and the 0.7
density rule as existing for the {ref}`CMPM3 <step-142>` polish.

Metal 3 is not among the "mask data for p1m, met1, via, met2" that rule
x.1a puts on a 0.001 grid, so its data fall under x.1b's 0.005, both
printed with the unit "mm".[^pdk-periph] Table C3 defines "top_metal" as
"met3.dg OR mm3.mk (for S8T\*/SP8TEE-5R); met3.dg OR indm.mk (for S8D\*);
met4.dg OR mm4.mk (for SP8Q/S8Q\*); met5.dg OR mm5.mk (for SP8P\*/S8P\*)",
a notation (`mm3.mk`) that `gds_layers.csv` does not use for the
mask.[^pdk-06] Rule nsm.3 lists "metX.dg (X=1 to 5) and cmmX.mk (X=1 to
5)" among the layers kept 1.000 µm from the nitride-seal keep-out (flag
AL).[^pdk-periph]

The PDK's [*Error Messages*](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) page describes "many
of the automated DRC rules that are checked by SkyWater as part of the
acceptance criteria for GDS data".[^pdk-errors] It lists two checks named `cmm3.nikon`,
"MM3mk in the nikon cross has the wrong polarity" and "MM3mk is missing
from the nikon cross in the layout".[^pdk-errors] It does not say what
the "nikon cross" is, and we read the checks as concerning a structure on
the mask layer whose data must have the right polarity (inference from
the message wording), not as stating the plate's tone.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `MM3` the site renders layer 70:20 (`met3`)
together with 34:28, which it lists as a fill layer, with no Boolean
expression and no note, on all eight runs.[^mask-renders] Its mask record gives the
mask-level layer 34:0, the description "Metal 3-PLM" with the three
variant names, and the info text "Metal 3".[^mask-renders]

Layer 34:28 is
not in `gds_layers.csv`, whose `cmm3` waffle-drop purpose is
107:24,[^pdk-06] so the site's choice of it is one public reading of the
tape-out files, not a PDK definition. Like the site's other layer
choices, it is not SkyWater's mask-generation recipe
({ref}`masks-derivations`).

The info text is identical to the "Info" note
of the "Metal 3-PLM" row in the process-steps sheet, so neither is cited
as corroborating the other
({ref}`masks-renders-sheet-notes`).[^steps-sheet][^mask-renders]

The site
also renders its `INDM` entry, "Inductor-TLM" in `masks.csv`, from the
same `met3` layer, with the note "INDM = met3 (thick-last-metal flow, not
SKY130)"; no plate is recorded for it ({ref}`masks-renders`).[^mask-renders][^pdk-05]

Every rendered die of every run carries shapes on these layers — at
least 3 877 082 on each die, fill included[^mask-renders] — so the count
of 40 dies says only that every layout has metal 3.

The site states the
limits of its images: "These are renders of *drawn* data, not photomask
artwork: reticle pitch, 4x reduction, mirroring and the frame features
the fab adds are not modelled."[^mask-renders] Its metadata carries no
plate ID, so a render is tied to a plate in the sheet only by the acronym
`MM3`, and the MPW-4 renders come from a different reticle set from the
one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a plate for the
"Metal 3-PLM" row as existing on all eight MPW runs, with the plate
number `570` on each.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet] The sheet records no
plates for the unmarked "Metal 3-TLM" and "Metal 3-S8TM"
rows.[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA570A` |
| MPW-2 | `5CS8007AC` | `S8007AA570A` |
| MPW-3 | `5CS8008AC` | `S8008AA570A` |
| MPW-4 | `5CS8018AC` | `S8018AA570A` |
| MPW-5 | `5CS8011AC` | `S8011AA570A` |
| MPW-6 | `5CS8014AC` | `S8014AA570A` |
| MPW-7 | `5CS8016AC` | `S8016AA570A` |
| MPW-8 | `5CS8017AC` | `S8017AA570A` |

* **Plate number.** The sheet does not say what `570` encodes. It falls
  between `560` for `VIM2` and `572` for `CAPM`.

  From `500` to `590` the
  via and metal numbers rise in step order, but each capacitor mask is
  numbered 2 above the metal mask that follows it (our comparison). `MM3` (step 139) is
  `570` against `CAPM` (step 137) `572`, as `MM4` (step 154) is `580`
  against `CAP2M` (step 152) `582` (our comparison). Elsewhere the numbers
  do not follow process order, and no process position is read from
  them ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type.** The sheet's "Sheet4" tab gives no type for
  `MM3`.[^steps-sheet] 4× is the ITRS 2001 mask magnification for the
  130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

### Exposure class

The {ref}`MM3 <step-139>` page gives
{math}`k_1 = 0.30 \times 0.70 / 0.248 \approx 0.85` on a KrF lens of NA
0.70 and {math}`k_1 = 0.30 \times 0.60 / 0.365 \approx 0.49` on an i-line
lens of NA 0.6, finds either class plausible and leaves the choice open,
quoting ASML's statement that older systems "migrate to the lithography
of choice for less critical layers".[^asml-30] The
{ref}`i-line stepper <machine-i-line-stepper>` and
{ref}`KrF stepper <machine-duv-krf-stepper>` pages both list it as "not
public which class (i-line or DUV)".

SkyWater lists "ASML I-line stepper", "ASML I-line
scanner", "ASML DUV stepper" and "ASML DUV scanner" but assigns no layer
to any of them.[^skw-01]

### Mask errors

Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space
patterns".[^wong-1998] That threshold is about 0.18 µm at 248 nm and NA
0.7 but about 0.30 µm at 365 nm and NA 0.6 (our arithmetic), so plate CD
errors on dense metal-3 lines would print at their own size on a KrF tool
and begin to be magnified on an i-line tool (inference).

Hochmuth, Ruhl
and Coleman found that with chrome dry etch "the deviation of the CD from
the target value is a function of the chrome loading on the
plate".[^hochmuth-1999] Whether the `MM3` plate is dry-etched, and how
its loading is handled, is not public. How tightly SkyWater specifies the `MM3` plate is not
public.

### Thick metal, capacitors and the resist

On the step pages' readings
the resist is coated over the 0.845 µm metal-3 stack,[^pdk-04] which
carries the thin capacitor dielectric and, over each capacitor, a plate
island of the order of 0.1 µm high (the {ref}`MM3 <step-139>` page's
reading of {ref}`CAPTIW1 <step-136>`), so it sees two thin-film stacks of
different reflectivity and a step at every plate edge.

Brunner showed
that the swing ratio scales with the square root of the substrate
reflectivity, which an anti-reflective coating reduces.[^brunner-1991]
Rocke and Schneegans used titanium nitride on aluminium as an
anti-reflection layer.[^rocke-1988]

The step page reads an organic
{term}`BARC` that also part-planarises the plate edges and a resist
thicker than at metals 1 and 2, because the thick stack must be etched
before the resist is consumed. With the resist left where `met3` is
drawn, the plate would be clear-field (inference). None of this is
published; the {ref}`MM3E <step-140>` page sets out why the metal
thickness itself is not settled. The consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

### Fill and the polish above

Kahng et al. formulate fill as adding
features so that "feature area densities satisfy prescribed upper and
lower bounds in all windows of given size", including a "fixed-dissection
regime" of predetermined windows,[^kahng-1999] the form of the m3.pd
rules' 700 µm regions stepped by 70.[^pdk-periph] Kahng and Samadi note
that "Post-CMP wafer topography varies according to pattern
density",[^kahng-2008] and Stine et al. found pattern density "a strongly
dominant factor" in interlevel-dielectric polishing.[^stine-1998]

The
PDK's "Oxide Bias for MM3" of 1.15 (`BiasMM3`), against 0.6 for `MM1`
and `MM2`, sits in Table 4's first block, headed "Material Thicknesses"
with a column headed "Value (um)", not with its "Waffling / Pattern
Density" criteria.[^pdk-03] The {term}`oxide bias` glossary entry records
the step pages' reading of it.

### Overlay and alignment

Metal 3 must enclose each via 2 below by 0.065 µm (m3.4)
and each via 3 above by 0.060 µm (via3.4), and by 0.090 µm on one of two
adjacent sides (via3.5); the enclosure of the capacitor plates (capm.3)
has no published value.[^pdk-periph] The {ref}`MM3 <step-139>` page reads
the alignment tree — to via-2 targets under the metal, to the `capm`
pattern, or both — as deciding which enclosure carries the larger error,
and leaves it open.

### Pattern transfer

On the step pages' readings the resist pattern is
transferred by {ref}`MM3E <step-140>`, which first breaks through the
capacitor dielectric outside the plates and then etches the metal stack
in a chlorine chemistry, stopping on the via-2 cap oxide and plug tops,
on the {ref}`metal plasma etcher <machine-plasma-etcher-metal>` class. On the step pages' readings
passivation, resist strip and clean are treated as part of that step.

The Newport Fab patent likewise patterns its bottom-plate metal after the
top plate is defined,[^pat-mim-newportfab] and Ng et al. review MiM
integration in Al–Cu and copper back ends.[^ng-2005] Bohr argued that
interconnect, not the transistor, limits performance,[^bohr-1995] and
Stamper, Fuselier and Tian treated the RC delay of aluminium wiring at
the sub-0.25 µm generation.[^stamper-1998] The step page cites both for
why the upper levels are thick and wide.

(mask-mm3-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `MM3` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`MM3 <step-139>`, {ref}`MM3E <step-140>`

* {ref}`MM3 <step-139>` — coats, exposes and develops the resist.
* {ref}`MM3E <step-140>` — etches the remaining capacitor dielectric and
  the metal stack through the resist; the step list used in this
  reference has no separate strip step, and the step page treats the
  passivation, resist strip and wet clean as part of the etch.

On its step page's reading, the next step, {ref}`NILD5 <step-141>`,
deposits the inter-level oxide between metal 3 and metal 4 over the
etched lines and the capacitors after the resist is gone. The next mask
step is {ref}`VIM3 <step-144>`. The rule needs no exception for this
mask.

## Design rules and critical dimensions

The `m3` rules of the periphery rules, with the via-3 enclosures by metal
3, the capacitor and fuse rules that name metal 3 or its role, and the
mask-data rules x.1b, x.7, x.11 and x.15a.

Flag P means "Rule applies to
periphery only (outside areaid.ce). A corresponding core rule may or may
not exist.", AL "Rules applicable only to Al BE flows", CU "Rules
applicable only to Cu BE flows", A "Rule documents a functionality
implemented in CL algorithms and may not be checked by DRC.", RR
"Recommended rule at any IP level", RC "Recommended rule at the chip
level, required rule at the IP level.", LVS "Rule handled by LVS" and NC
"Rule not checked by DRC. It should be used as a guideline
only."[^pdk-periph]

:::{table} The `m3` rules, the via-3 enclosures by metal 3, the capacitor and fuse rules that name metal 3 or its role, and the mask-data rules, as published

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| m3.- | "Algorithm should flag errors, for met3, if ANY of the following is true: […] An entire 700x700 window is covered by cmm3 waffleDrop, and metX PD < 70% for same window. […]" (RC) | — |
| m3.1 | "Width of metal 3" | 0.300 µm |
| m3.2 | "Spacing of metal 3 to metal 3" | 0.300 µm |
| m3.3a | "Min. spacing of features attached to or extending from huge_met3 for a distance of up to 0.480 um to metal3 (rule not checked over non-huge met3 features)" | N/A |
| m3.3b | "Min. spacing of huge_met3 to metal3 excluding features checked by m3.3a" | N/A |
| m3.3c | "Min. spacing of features attached to or extending from huge_met3 for a distance of up to 0.400 µm to metal3 (rule not checked over non-huge met3 features)" | 0.400 µm |
| m3.3d | "Min. spacing of huge_met3 to metal3 excluding features checked by m3.3a" | 0.400 µm |
| m3.4 | "Via2 must be enclosed by Met3 by at least …" (AL) | 0.065 µm |
| m3.5 | "Via2 must be enclosed by Met3 on one of two adjacent sides by at least …" | N/A |
| m3.5a | "Via2 must be enclosed by Met3 on all sides by at least …(Rule not checked on a layout when it satisfies both rules m3.4 and m3.5)" | N/A |
| m3.6 | "Min area of metal3" | 0.240 µm² |
| m3.7 | "Min area of metal3 holes" (CU) | 0.200 µm² |
| m3.pd.1 | "Min MM3_oxide_Pattern_density" (RR) | 0.7 |
| m3.pd.2a | "Rule m3.pd.1 has to be checked by dividing the chip into square regions of width and length equal to …" (A) | 700 µm |
| m3.pd.2b | "Rule m3.pd.1 has to be checked by dividing the chip into steps of …" (A) | 70 |
| m3.11–m3.15 | Maximum width, slotting threshold, maximum pattern density, its window and step, and a via-2 enclosure, for copper flows (CU) | 4.000 µm, 3.200, 0.77, 50.000 µm, 25.000 µm, 0.060 µm |
| via3.4 | "Via3 must be enclosed by Met3 by at least …" (AL) | 0.060 µm |
| via3.5 | "Via3 must be enclosed by Met3 on one of two adjacent sides by at least …" (AL) | 0.090 µm |
| capm.2b | "Minimum spacing of capacitor bottom_plate to bottom plate" | N/A |
| capm.3 | "Minimum enclosure of capm (top_plate) by met2" | N/A |
| mf.21 | "Min spacing , no overlap, between metal3 and fuse center" | 3.300 µm |
| nsm.3 | "Min spacing, no overlap, between NSM_keepout to […] metX.dg (X=1 to 5) and cmmX.mk (X=1 to 5). […]" (AL) | 1.000 µm |
| x.1b | "Data for SKY130 layout and mask on all layers except those mentioned in 1a must be on a grid of mm (except inside Seal ring)" | 0.005 (unit "mm") |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.11 | "Metal fuses are drawn in met3" (LVS) | N/A |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
:::

Table 2 of *Criteria & Assumptions* gives `MM3CD` and `MM3CDSP` as 0.3
and 0.3 for "Metal 3-PLM", 0.36 and 0.36 for "Metal 3-TLM" and 0.8 and
0.8 for "Metal 3-S8TM".[^pdk-03] It gives 0.3 and 0.3 for a "Metal 3-Cu" row
(`MM3_CuCD`, `MM3_CuCDSP`), a copper back end that SKY130's aluminium
flow does not use.[^pdk-03]

Table 4 adds, in its "Material Thicknesses"
block, the "Oxide Bias for MM3" of 1.15 (`BiasMM3`) and metal-3
thicknesses "for antenna ratio calculation":[^pdk-03]

* 0.8 for "(S8P\*/SP8P\*)"
  (`Met3thick_p`) and "(S8Q/SP8Q)" (`Met3thick_q`)
* 0.85 for "(S8T\* other
  than S8TM\*)" (`Met3_Qthick`)
* 2 for "(S8TM\* flow)" (`Met3_TMthick`)
* 0.8 for "(SP8T flow)" (`Met3_SP8Tthick`)

Its "Waffling / Pattern Density" block has criteria not tied to one
level, among them a "Min MM\* PD range" of 0.3 (`MMPDrange`).[^pdk-03] Table 7
gives a "Huge metal X min. W and L" of 3 (`HugeM`) and "Large waffle size
must be divisible by 4", 7.2 (`waffle_large`), both in its column headed
"CD".[^pdk-03]

For the plate the decisive figures are 0.300 µm lines on a
0.6 µm pitch (our arithmetic from m3.1 and m3.2).

## Related pages

* {ref}`MM3 <step-139>` and {ref}`MM3E <step-140>` — the mask step and
  the metal etch; {ref}`WTIAL3 <step-134>` — the stack patterned.
* **Category.** {ref}`category-lithography`, {ref}`category-etch` and
  {ref}`category-cmp` — the mask step, etch and polish categories.
* **Machines.** {ref}`machine-i-line-stepper` and {ref}`machine-duv-krf-stepper` — the
  two exposure classes the step page leaves open.
  {ref}`machine-plasma-etcher-metal` — the etch class that transfers the
  pattern. {ref}`machine-cd-sem-overlay-metrology` — line CD and overlay
  measurement.
* **Materials.** {ref}`material-lithography-materials` — resists, anti-reflective
  coatings, developer and reticles.
* **Masks.** {ref}`mask-capm` — the capacitor mask whose plates metal 3 must
  enclose; {ref}`mask-vim2` — the via mask whose plugs it covers;
  {ref}`mask-mm2` — the metal mask one level down.
* **Indexes.** {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the tables this page's plate facts are taken from.

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Metal 3-PLM", "Metal
  3-TLM" and "Metal 3-S8TM", `MM3`, with the PLM entry marked, and
  "Inductor-TLM".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `met3` 70:20,
  the `cmm3` purposes, Table C3 and the `MM3` column of Table F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `MM3CD`/`MM3CDSP` for the
  three variants, `MM3_CuCD`/`MM3_CuCDSP`, `BiasMM3`, the metal-3 antenna
  thicknesses, `HugeM` and `waffle_large`.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `m3` rules, via3.4, via3.5,
  capm.2b, capm.3, the fuse note, mf.21, nsm.3, x.1a, x.1b, x.7, x.9,
  x.11, x.15a and the flag legend.[^pdk-periph]
* [SkyWater PDK, *Summary of Key Periphery Rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>) — Tables F3c, F3d and
  F4.[^pdk-summary]
* [SkyWater PDK, *Error Messages* page](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) — the `cmm3.nikon`
  checks.[^pdk-errors]
* [SkyWater PDK, *Process stack diagram*](<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>) — the 0.845 µm `met3`.[^pdk-04]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — the stacked MiM cross-section with "M3
  (plate 1)".[^pdk-07]
* [SkyWater PDK, *Parasitic Layout Extraction*](<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>) — the metal sheet
  resistances.[^pdk-08]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the `MM3` plates of
  MPW-1 to MPW-8, the "Info" note and the mask-type tab.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `MM3` renders, their layers,
  description and info text, the `INDM` render and the per-die shape
  counts.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the i-line and DUV exposure
  tools.[^skw-01]
* [ASML, *Three decades of PAS 5500*](<https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>) — older exposure tools moving to less
  critical layers.[^asml-30]

### High-level understanding

* [Wikipedia, *Photomask*](<https://en.wikipedia.org/wiki/Photomask>) — reticles, absorbers and
  pellicles.[^wiki-mask]
* [Wikipedia, *Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) — i-line and DUV exposure.[^wiki-litho]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]

### Deep dive

* [Kahng et al., *IEEE TCAD* 1999](<https://doi.org/10.1109/43.752928>) — fill synthesis to density bounds in
  fixed windows.[^kahng-1999]
* [Kahng and Samadi, *IEEE TCAD* 2008](<https://doi.org/10.1109/TCAD.2007.907061>) — a survey of CMP fill
  synthesis.[^kahng-2008]
* [Stine et al., *IEEE TSM* 1998](<https://doi.org/10.1109/66.661292>) — pattern density as the dominant factor
  in dielectric polishing.[^stine-1998]
* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor of dense
  lines and the size below which it rises.[^wong-1998]
* [Hochmuth, Ruhl and Coleman, *Proc. SPIE* 1999](<https://doi.org/10.1117/12.373324>) — plate CD against chrome
  loading in dry-etched masks.[^hochmuth-1999]
* [Brunner, *Proc. SPIE* 1991](<https://doi.org/10.1117/12.46410>) — the swing ratio and anti-reflective
  coatings.[^brunner-1991]
* [Rocke and Schneegans, *JVST B* 1988](<https://doi.org/10.1116/1.584306>) — titanium nitride as an
  anti-reflection layer on aluminium.[^rocke-1988]
* [Bohr, IEDM 1995](<https://doi.org/10.1109/IEDM.1995.499187>) — interconnect as the limit on
  performance.[^bohr-1995]
* [Stamper, Fuselier and Tian, IITC 1998](<https://doi.org/10.1109/IITC.1998.704752>) — RC delay of aluminium wiring
  below 0.25 µm.[^stamper-1998]
* [Ng et al., *IEEE TED* 2005](<https://doi.org/10.1109/TED.2005.850642>) — MiM integration in Al–Cu and copper back
  ends.[^ng-2005]
* [Kar-Roy and Racanelli (Newport Fab), US 6,430,028](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6430028>) — the bottom-plate
  metal patterned after the top plate.[^pat-mim-newportfab]

## Open questions

* The PDK does not define "TLM", "S8TM" or "PLM"; the step page's
  readings of S8TM and PLM are inferences, and it gives none of
  TLM.[^pdk-05] The renders site's "thick-last-metal" note on `INDM` is
  one public reading, not the PDK's.[^mask-renders]
* The operation that makes the `cmm3` plate data from `met3` and the
  waffle-drop purpose is not published, nor whether a waffle-drop shape
  places fill or keeps it out; the renders' fill layer 34:28 is not in
  `gds_layers.csv`.[^pdk-06][^pdk-periph][^mask-renders]
* Whether the level is exposed on an i-line or a KrF tool, and the
  plate's type, tone and CD specification, the resist and anti-reflective
  scheme, are not public.
* The capacitor enclosure capm.3 has no published value and names met2;
  the reading for metal 3, and the alignment tree between `CAPM` and
  `MM3`, are the step page's inferences.[^pdk-periph]
* Table F2b's `C` mark for "metal fuse_D" in the `MM3` column and the
  x.11 row for met3 are not tied to a flow; the reading that the fuse
  belongs to other flows rests on Table C3 and the fuse
  note.[^pdk-06][^pdk-periph]
* What the plate number `570` encodes is not stated, and no public source
  lists the `MM3` plate of the original MPW-4 set
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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 4
    and 7), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-summary]: SkyWater PDK Authors, *Summary of Key Periphery Rules*
    (Tables F3c, F3d and F4), SkyWater SKY130 PDK documentation,
    retrieved 2026-09-14.
    <https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (MiM capacitors),
    SkyWater SKY130 PDK documentation, and the `cap_mim` cross-section
    drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/cap_mim/cross-section-cap_mim.svg>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md`, `masks.html` and, for each run, the
    `mpw-00N_MM3/` directory with its page, `job.json`, `result.json` and
    per-die slot JSON files, retrieved 2026-09-14. Rendered from the
    public shuttle repositories under
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
[^kahng-1999]: A. B. Kahng, G. Robins, A. Singh and A. Zelikovsky,
    "Filling algorithms and analyses for layout density control", *IEEE
    Transactions on Computer-Aided Design of Integrated Circuits and
    Systems* **18**(4), 445–462 (1999).
    <https://doi.org/10.1109/43.752928>
[^kahng-2008]: A. B. Kahng and K. Samadi, "CMP Fill Synthesis: A Survey
    of Recent Studies", *IEEE Transactions on Computer-Aided Design of
    Integrated Circuits and Systems* **27**(1), 3–19 (2008).
    <https://doi.org/10.1109/TCAD.2007.907061>
[^stine-1998]: B. E. Stine, D. O. Ouma, R. R. Divecha, D. S. Boning,
    J. E. Chung, D. L. Hetherington, C. R. Harwood, O. S. Nakagawa and
    S.-Y. Oh, "Rapid characterization and modeling of pattern-dependent
    variation in chemical-mechanical polishing", *IEEE Transactions on
    Semiconductor Manufacturing* **11**(1), 129–140 (1998).
    <https://doi.org/10.1109/66.661292>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**,
    Optical Microlithography XI, 106 (1998).
    <https://doi.org/10.1117/12.310718>
[^hochmuth-1999]: J. Hochmuth, G. G. Ruhl and T. P. Coleman, "Control
    methodology of off-target for varying pattern densities with chrome
    dry etch", *Proc. SPIE* **3873**, 19th Annual Symposium on Photomask
    Technology, 297 (1999). <https://doi.org/10.1117/12.373324>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^rocke-1988]: M. Rocke and M. Schneegans, "Titanium nitride for
    antireflection control and hillock suppression on aluminum silicon
    metallization", *Journal of Vacuum Science & Technology B* **6**(4),
    1113–1115 (1988). <https://doi.org/10.1116/1.584306>
[^bohr-1995]: M. T. Bohr, "Interconnect scaling — the real limiter to
    high performance ULSI", *IEDM 1995 Technical Digest*, pp. 241–244.
    <https://doi.org/10.1109/IEDM.1995.499187>
[^stamper-1998]: A. K. Stamper, M. B. Fuselier and X. Tian, "Advanced
    wiring RC delay issues for sub-0.25-micron generation CMOS", *Proc.
    IEEE 1998 International Interconnect Technology Conference (IITC)*,
    pp. 62–64. <https://doi.org/10.1109/IITC.1998.704752>
[^ng-2005]: C. H. Ng, C.-S. Ho, S.-F. S. Chu and S.-C. Sun, "MIM
    Capacitor Integration for Mixed-Signal/RF Applications", *IEEE
    Transactions on Electron Devices* **52**(7), 1399–1409 (2005).
    <https://doi.org/10.1109/TED.2005.850642>
[^pat-mim-newportfab]: A. Kar-Roy and M. Racanelli (Newport Fab, LLC),
    *Method for fabrication of an MIM capacitor and related structure*,
    US 6,430,028 B1, filed 2000-11-22, granted 2002-08-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6430028>
