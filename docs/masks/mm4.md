(mask-mm4)=
# MM4 — Metal 4

The metal-4 mask is the {term}`reticle` that draws SKY130's fourth
aluminium wiring level, the bottom plates of the second
{term}`MiM capacitor` and, on the PDK's fuse note, the metal fuses: on the
{ref}`MM4 <step-154>` page's reading, the resist printed through it at
step 154 stays wherever `met4` is drawn, and the {ref}`MM4E <step-155>`
etch removes the capacitor dielectric and the metal stack everywhere else.
Its lines are metal 3's 0.3 µm, the step pages leave open whether it is
printed on an i-line or a KrF tool, and it is the one metal mask whose
public renders use a layer set that differs from this reference's
pairing, since they leave out the `met4` fuse purpose. This page gathers
what public sources say about the mask itself — its PDK entry and layers,
the plates the process-steps sheet records for the MPW runs, what the
public renders of those runs show, the lithography it needs and the rules
that constrain it. How the step is performed is on the step page; every
mask is indexed on the {ref}`masks index <masks-index>`.

| | MM4 — Metal 4 |
|---|---|
| Mask step | {ref}`MM4 <step-154>`, step 154 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Metal 4", `MM4`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cmm4` mask 51:0, "Metal 4 mask"; waffle drop 112:4[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `met4` drawing 71:20, "Metal 4"; `met4` fuse 71:17, without a description (the metal-fuse note names MM4)[^pdk-06][^pdk-periph] |
| Minimum CD, feature / space | `MM4CD` 0.3 / `MM4CDSP` 0.3[^pdk-03] |
| Polarity and tone | Not published; the PDK's `cmm4.nikon` checks name a polarity but not the plate's tone. On the step page's reading the resist remains where `met4` is drawn, which with a positive resist would make the plate clear-field (inference). |
| Exposure class | i-line or KrF (248 nm): the step page finds either plausible for the 0.3 µm line and leaves the class open; no public source names the tool ({ref}`machine-i-line-stepper`, {ref}`machine-duv-krf-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `580`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-mm4-steps>` |

## What the mask defines

The periphery rules give the function of the `m4` rule set as "Defines
Fourth level of metal interconnects;", and the PDK's Table F4 shows metal
4 joined to metal 3 by "Via3" and to metal 5 by
"Via4".[^pdk-periph][^pdk-summary] The mask carries lines at the
0.300 µm minimum width and space (m4.1, m4.2), pads that enclose the
via-3 plugs below by 0.065 µm (m4.3) and the 0.800 µm via-4 openings
above by 0.190 µm (via4.4), wide "huge_met4" features that need 0.400 µm
of space (m4.5a, m4.5b), and, on our reading of the waffle-drop rules
below, dummy fill; its smallest island is 0.240 µm² (m4.4a), with probe
pads of exactly 1.42 µm × 1.42 µm exempted from the area rule
m4.4.[^pdk-periph] The PDK's extraction table gives metal 4, like metal
3, a sheet resistance of 47 in a column headed "Resistivity
(mohms/sq)",[^pdk-08] and the stack diagram draws `metal4` 0.845 µm
thick.[^pdk-04] A via-4 landing therefore needs a metal-4 pad at least
1.18 µm wide, four times the minimum line (the
{ref}`MM4 <step-154>` page's arithmetic from via4.1 and via4.4).

The same pattern makes the second capacitor's bottom plates. On the step
pages' readings the metal-4 stack stays blanket through the second
capacitor module and every `cap2m` plate must end up inside a metal-4
shape; the PDK's cross-section of the stacked capacitor labels a "M4
(plate 2)" and a "M4 (plate 1)", which the step page reads as the plate
under "CAP2M" and a separate shape linking "M3 (plate 1)" to "M5 (plate
1)".[^pdk-07] The PDK publishes no `cap2m` rules, so the enclosure of the
plates by metal 4 has no value.[^pdk-periph]

**Fuses.** The note above the metal-fuse rules reads "For SKY130D\* and
SKY130TM\* CADflow use MM2 for Metal Fuse" and "For SP8P\*/SKY130P\* (PLM)
CADflow use MM4 for Metal Fuse"; one row of rule x.11 reads "Metal fuses
are drawn in met4" (flag LVS, no value), beside rows naming met2 and
met3.[^pdk-periph] Table C3 of the *Layers Reference* defines "fuse:dg"
as "met2:fe for S8D\*/S8TM\*, met3.fe for S8TEE\*/S8TNV/S8Q\*/SP8TEE-5R/SP8Q\*,
met4.fe for S8P\*/SP8P\*" and "fuse_metal" as "met3 for
S8TEE\*/S8TNV/S8Q\*/SP8TEE-5R/SP8Q\*; met2 for S8D\*/S8TM\*, met4 for
S8P\*/SP8P\*", and `gds_layers.csv` has a `met4` fuse purpose at 71:17
and a `target` drawing layer at 76:44, "Metal fuse target".[^pdk-06] The
fuse rules give a fuse a width of 0.800 µm, "Min. and max width of
fuse" (mf.1), and a length of 7.200 µm (mf.2), on centres 2.760 µm apart
(mf.3), with "Only one fuse per metal line allowed"
(mf.20).[^pdk-periph] SkyWater's published DRC checks name the level:
the PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance criteria
for GDS data", lists "metal4 fuse should be rectangular", "0.8 min. width
of metal4 fuse", "7.2 min. length of metal4 fuse" and "0.83 max extension
of met4 beyond fuse boundary" (mf.5, whose periphery-rule value is printed
without a unit), with target spacings of 2.75 (mf.3) and 3.295 (mf.4)
against the periphery tables' 2.760 and 3.300.[^pdk-errors] The
{ref}`MM4 <step-154>` page reads the fuse links as printed by this mask
with the wiring (inference from the note, supported by the metal-4 fuse
checks), and PLM as the label of the
flow this reference follows (inference). Table F2b, the mask generation
table, has columns for `MM1`, `MM2`, `MM3` and `MM5` but none for `MM4`,
and marks its two "metal fuse" rows `C` in the `MM2` and `MM3`
columns;[^pdk-06] the PDK does not explain the missing column.

Table 5 of *Criteria & Assumptions*, "Laser Fuse Criteria", bears on how
such fuses may be opened. It lists in a column headed
"Value (um)" a "Max. width of a metal fuse line that can be removed
reliably" of 0.8 (`FSW`), the width of mf.1; a "Min. L of met. fuse at
which damage doesn't extend beyond ends" of 6.605 (`FSLE`), below the
7.200 µm of mf.2; a "Nominal effective laser spot diameter" of 3.5
(`LASSPT`); a "Positioning tolerance of laser spot (3 s)" of 0.3
(`LASMA`); and a "Fuse melting radius" of 3.6 (`MELTRAD`); Table 9 gives
an "Enclosure of fuses by polyimide" of 12 (`PimFuseEnc`) and an
"Enclosure of laser targets in the die by polyimide" of 30
(`PimLaserEnc`).[^pdk-03] Table 5 also gives a "Max. extension of met2
beyond fuse boundary" of 0.005 (`FEXT`), which names metal 2, where rule
mf.5 allows 0.830 of fuse metal and the Error Messages page checks "0.83
max extension of met4 beyond fuse boundary".[^pdk-03][^pdk-periph][^pdk-errors]
We read the metal-4 fuses as laser-opened links whose drawn width this
mask fixes (inference from Table 5's title, the equal 0.8 widths, the
laser-target criterion and the mf rules' "target"); Table 5's one
metal-named row is for metal 2, so its criteria may describe a metal-2
fuse flow. Smith et al. described the
laser-programmed redundancy of a 64K DRAM, whose polysilicon links were
blown by laser pulses, "in relation to the target geometry, laser spot
size and targeting accuracy".[^smith-1981]

**Variants and flows.** `masks.csv` lists "Metal 4" once and marks
it.[^pdk-05] Table 2 of *Criteria & Assumptions* gives `MM4CD` and
`MM4CDSP` 0.3 and a separate "Metal 4-Cu" row; Table 4 gives metal-4
thicknesses "for antenna ratio calculation" of 0.8 for "(S8P\*/SP8P\*)"
(`Met4Thick_p`) and 2 for "(S8Q\*/SP8Q)" (`Met4Thick_q`), and Table C3
defines "top_metal" as "met4.dg OR mm4.mk" for "SP8Q/S8Q\*" and "met5.dg
OR mm5.mk" for "SP8P\*/S8P\*".[^pdk-03][^pdk-06] The
{ref}`VIM3 <step-144>` page reads the 2 µm entry as a thick-metal-4
variant (inference). The mask does not define the metal stack it
patterns, which {ref}`WTIAL4 <step-149>` deposits, the second capacitor's
films and plates ({ref}`CAPILD2 <step-150>`, {ref}`CAPTIW2 <step-151>`,
{ref}`mask-cap2m`), the via-3 plugs beneath ({ref}`mask-vim3`) or the via
4 above ({ref}`mask-vim4`); on the step pages' readings the dielectric that
fills its spaces is deposited by {ref}`NILD6 <step-156>` and polished by
{ref}`CMPM4 <step-157>`.

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives the mask-level layer `cmm4` two purposes: `mask`
at 51:0 ("Metal 4 mask") and `waffle drop` at 112:4, on a layer number
that also carries the `cviam3` drawing purpose at 112:20; the drawn layer
is `met4` at 71:20, with a `fuse` purpose at 71:17 among its
others.[^pdk-06] The pairing of the mask with `met4` rests on those names
and descriptions, and that with the fuse purpose on rule x.11 and the
fuse note, as on the {ref}`masks index <masks-index>`; the PDK publishes
no operation from the drawn layers to the plate. Rule x.15a confines
"Drawn compatible, mask, and waffle-drop layers" to test modules, seal
ring and frame, "Exception: FOM/P1M/Metal waffle drop are allowed inside
the die" (flag P, periphery only),[^pdk-periph] so a die may carry `cmm4`
waffle-drop shapes as well as `met4` (our reading); with no add or drop
purpose, rule x.9's "serifs" have no `cmm4` layer to sit on. The rule
set's first entry, flagged RC, flags a 700 × 700 window "covered by cmm4
waffleDrop" when the metal pattern density of the same window is below a
limit that falls from 70 % for a fully covered window to 30 % for one
30–40 % covered, and rule m4.pd.1 sets a minimum
"MM4_oxide_Pattern_density" of 0.7, checked in 700 µm regions stepped by
70 (m4.pd.2a, m4.pd.2b, flag A).[^pdk-periph] The PDK does not say
whether a waffle-drop shape places fill or keeps it out; the
{ref}`MM4 <step-154>` page reads the `cmm4` fill and the 0.7 density rule
as existing for the {ref}`CMPM4 <step-157>` polish. Metal 4 falls under
the 0.005 grid of rule x.1b, and rule nsm.3 lists "metX.dg (X=1 to 5)
and cmmX.mk (X=1 to 5)" among the layers kept 1.000 µm from the
nitride-seal keep-out (flag AL).[^pdk-periph] The *Error Messages* page
lists two checks named `cmm4.nikon`, "MM4mk in the nikon cross has the
wrong polarity" and "MM4mk is missing from the nikon cross in the
layout";[^pdk-errors] it does not say what the "nikon cross" is, and we
read the checks as concerning a structure on the mask layer whose data
must have the right polarity (inference from the message wording), not
as stating the plate's tone.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `MM4` the site renders layers 71:20 (`met4`)
and 51:28, which it lists as a fill layer, with no Boolean expression and
no note, on all eight runs; its mask record gives the mask-level layer
51:0 and the info text "Metal 4".[^mask-renders] That layer set differs
from this reference's pairing: the masks index records the render as
"`met4` and the fill layer 51:28; no fuse purpose", so the images leave
out `met4` fuse 71:17 ({ref}`masks-derivations`).[^mask-renders][^pdk-06]
Layer 51:28 is not in `gds_layers.csv`, whose `cmm4` waffle-drop purpose
is 112:4, so the site's choice of it is one public reading of the
tape-out files, not a PDK definition, and like the site's other layer
choices it is not SkyWater's mask-generation recipe. The info text is
identical to the "Info" note of the `MM4` row in the process-steps sheet,
so neither is cited as corroborating the other
({ref}`masks-renders-sheet-notes`).[^steps-sheet][^mask-renders]

Every rendered die of every run carries shapes on these layers — at least
3 070 106 on each die, fill included[^mask-renders] — so the count of 40
dies says only that every layout has metal 4; because the fuse purpose is
not rendered, the images do not show whether any layout draws a metal-4
fuse. The site states the limits of its images: "These are renders of
*drawn* data, not photomask artwork: reticle pitch, 4x reduction,
mirroring and the frame features the fab adds are not
modelled."[^mask-renders] Its metadata carries no plate ID, so a render is
tied to a plate in the sheet only by the acronym `MM4`, and the MPW-4
renders come from a different reticle set from the one whose plates the
sheet records ({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `MM4` plate
as existing on all eight MPW runs, with the plate number `580` on
each.[^steps-sheet] The plate IDs below are the sheet's; the reticle set
is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA580A` |
| MPW-2 | `5CS8007AC` | `S8007AA580A` |
| MPW-3 | `5CS8008AC` | `S8008AA580A` |
| MPW-4 | `5CS8018AC` | `S8018AA580A` |
| MPW-5 | `5CS8011AC` | `S8011AA580A` |
| MPW-6 | `5CS8014AC` | `S8014AA580A` |
| MPW-7 | `5CS8016AC` | `S8016AA580A` |
| MPW-8 | `5CS8017AC` | `S8017AA580A` |

* **MPW-5.** Unlike `VIM4`, the mask above it, an `MM4` plate is
  recorded for MPW-5; the masks index reads the MPW-5 gap of `VIM4` as
  more likely a gap in the record than in the run
  ({ref}`masks-mpw-runs`).[^steps-sheet]
* **Plate number.** The sheet does not say what `580` encodes. From
  `500` to `590` the via and metal numbers rise in step order, but each
  capacitor mask is numbered 2 above the metal mask that follows it:
  `CAP2M` (step 152) is `582` against `MM4` (step 154) `580`, as `CAPM`
  (step 137) is `572` against `MM3` (step 139) `570` (our comparison).
  Elsewhere the numbers do not follow process order, and no process
  position is read from them
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type.** The sheet's "Sheet4" tab gives no type for
  `MM4`.[^steps-sheet] 4× is the ITRS 2001 mask magnification for the
  130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`MM4 <step-154>` page gives
{math}`k_1 = 0.30 \times 0.70 / 0.248 \approx 0.85` on a KrF lens of NA
0.70 and about 0.49 on an i-line lens of NA 0.6, finds either class
plausible and leaves the choice open, quoting ASML's statement that older
systems "migrate to the lithography of choice for less critical
layers";[^asml-30] the {ref}`i-line stepper <machine-i-line-stepper>` and
{ref}`KrF stepper <machine-duv-krf-stepper>` pages both list it as "not
public which class (i-line or DUV)". SkyWater lists "ASML I-line
stepper", "ASML I-line scanner", "ASML DUV stepper" and "ASML DUV scanner"
but assigns no layer to any of them.[^skw-01]

**Mask errors.** Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space
patterns";[^wong-1998] that threshold is about 0.18 µm at 248 nm and NA
0.7 but about 0.30 µm at 365 nm and NA 0.6 (our arithmetic), so plate CD
errors on dense metal-4 lines would print at their own size on a KrF tool
and begin to be magnified on an i-line tool (inference); the 0.800 µm
fuses are well above either threshold. Hochmuth, Ruhl and Coleman found
that with chrome dry etch "the deviation of the CD from the target value
is a function of the chrome loading on the plate";[^hochmuth-1999]
whether the `MM4` plate is dry-etched is not public.

**Thick metal, capacitors and the resist.** On the step pages' readings
the resist is coated over the 0.845 µm metal-4 stack,[^pdk-04] which
carries the thin capacitor dielectric and, over each second-level
capacitor, a plate island of the order of 0.1 µm high (the
{ref}`MM4 <step-154>` page's reading at {ref}`CAPTIW2 <step-151>`), so it
sees two
thin-film stacks of different reflectivity and a step at every plate
edge. Brunner showed that the swing ratio scales with the square root of
the substrate reflectivity, which an anti-reflective coating
reduces,[^brunner-1991] and Rocke and Schneegans used titanium nitride on
aluminium as an anti-reflection layer.[^rocke-1988] The step page reads
an organic {term}`BARC` and a resist thick enough to survive the etch of
the stack; with the resist left where `met4` is drawn, the plate would be
clear-field (inference). None of this is published. The consumables are
on the {ref}`lithography materials <material-lithography-materials>`
page.

**Fill and the polish above.** Kahng et al. formulate fill as meeting
density bounds "in all windows of given size",[^kahng-1999] the form of
the m4.pd rules; Tian, Wong and Boone added a multiple-layer formulation
of dummy-feature placement "avoiding cumulative effect" across
levels,[^tian-2001] a concern for a fourth level of fill over three
filled levels below (our reading). Kahng and Samadi note that "Post-CMP
wafer topography varies according to pattern density",[^kahng-2008] and
Stine et al. found pattern density "a strongly dominant factor" in
interlevel-dielectric polishing.[^stine-1998] The PDK's "Oxide Bias for
MM4" of 1.15 (`BiasMM4`), the same as `MM3` and against 0.6 for `MM1` and
`MM2`, sits in Table 4's first block, headed "Material Thicknesses" with a
column headed "Value (um)", not with its "Waffling / Pattern Density"
criteria;[^pdk-03] the {term}`oxide bias` glossary entry records the step
pages' reading of it.

**Pattern transfer.** On the step pages' readings the resist pattern is
transferred by {ref}`MM4E <step-155>`, which first breaks through the
capacitor dielectric outside the plates and then etches the metal stack
in a chlorine chemistry, stopping on the via-3 cap oxide and plug tops,
on the {ref}`metal plasma etcher <machine-plasma-etcher-metal>` class,
with passivation, resist strip and clean treated as part of that step.
The Newport Fab patent likewise patterns its bottom-plate metal after the
top plate is defined,[^pat-mim-newportfab] and Ng et al. review MiM
integration in Al–Cu and copper back ends.[^ng-2005] Bohr argued that
interconnect limits performance[^bohr-1995] and Stamper, Fuselier and
Tian treated the RC delay of aluminium wiring below 0.25 µm;[^stamper-1998]
the step page cites both for why the upper levels are thick and wide.

**Overlay.** Metal 4 must enclose each via 3 by 0.065 µm (m4.3) and each
via 4 by 0.190 µm (via4.4); the enclosure of the `cap2m` plates has no
published value, and the fuse rules keep a fuse centre 3.300 µm from
fuse metal, metal 1, local interconnect and metal 2 (mf.4, mf.6, mf.7,
mf.19).[^pdk-periph] The {ref}`MM4 <step-154>` page reads the alignment
tree — to via-3 targets under the metal, to the `cap2m` plates, or
both — as deciding which enclosure carries the larger error, and leaves
it open.

(mask-mm4-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `MM4` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`MM4 <step-154>`, {ref}`MM4E <step-155>`

* {ref}`MM4 <step-154>` — coats, exposes and develops the resist.
* {ref}`MM4E <step-155>` — etches the remaining capacitor dielectric and
  the metal stack through the resist; the step list used in this
  reference has no separate strip step, and the step page treats the
  passivation, resist strip and clean as part of the etch.

On its step page's reading, the next step, {ref}`NILD6 <step-156>`,
deposits the inter-level oxide between metal 4 and metal 5 over the
etched lines and the second-level capacitors after the resist is gone.
The next mask step is {ref}`VIM4 <step-159>`. The rule needs no exception
for this mask.

## Design rules and critical dimensions

The `m4` rules of the periphery rules, with the via-4 enclosure by metal
4, the metal-fuse rules that fix the fuse shape, and the mask-data rules
x.1b, x.7, x.11 and x.15a. Flag P means "Rule applies to periphery only
(outside areaid.ce). A corresponding core rule may or may not exist.", AL
"Rules applicable only to Al BE flows", CU "Rules applicable only to Cu
BE flows", A "Rule documents a functionality implemented in CL algorithms
and may not be checked by DRC.", RR "Recommended rule at any IP level",
RC "Recommended rule at the chip level, required rule at the IP level.",
LVS "Rule handled by LVS" and NC "Rule not checked by DRC. It should be
used as a guideline only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| m4.- | "Algorithm should flag errors, for met4, if ANY of the following is true: […] An entire 700x700 window is covered by cmm4 waffleDrop, and metX PD < 70% for same window. […]" (RC) | — |
| m4.1 | "Min width of met4" | 0.300 µm |
| m4.2 | "Min spacing between two met4" | 0.300 µm |
| m4.3 | "via3 must be enclosed by met4 by atleast" (AL) | 0.065 µm |
| m4.4 | "Min area of met4 (rule exempted for probe pads which are exactly 1.42um by 1.42um)" | N/A |
| m4.4a | "Min area of met4" | 0.240 µm² |
| m4.5a | "Min. spacing of features attached to or extending from huge_met4 for a distance of up to 0.400 µm to metal4 (rule not checked over non-huge met4 features)" | 0.400 µm |
| m4.5b | "Min. spacing of huge_met4 to metal4 excluding features checked by m4.5a" | 0.400 µm |
| m4.7 | "Min area of meta4 holes" (CU) | 0.200 µm² |
| m4.pd.1 | "Min MM4_oxide_Pattern_density" (RR) | 0.7 |
| m4.pd.2a | "Rule m4.pd.1 has to be checked by dividing the chip into square regions of width and length equal to …" (A) | 700 µm |
| m4.pd.2b | "Rule m4.pd.1 has to be checked by dividing the chip into steps of …" (A) | 70 |
| m4.11–m4.16 | Maximum width, slotting threshold, maximum pattern density ("met4 overlapping pdm areas are excluded from the check"), its window and step, a via-3 enclosure and a pad enclosure, for copper flows (CU) | 10.000 µm, 10.000, 0.77, 50.000 µm, 25.000 µm, 0.060 µm, 0.850 µm |
| via4.4 | "Via4 must be enclosed by Met4 by at least …" | 0.190 µm |
| mf.1 | "Min. and max width of fuse" | 0.800 µm |
| mf.2 | "Length of fuse" | 7.200 µm |
| mf.3 | "Spacing between centers of adjacent fuses" | 2.760 µm |
| mf.4 | "Spacing between center of fuse and fuse_metal (fuse shields are exempted)" | 3.300 µm |
| mf.5 | "Max. extension of fuse_metal beyond fuse boundary" | 0.830 |
| mf.20 | "Only one fuse per metal line allowed" | — |
| mf.23 | "Spacing (no overlapping) between fuse center and Metal4" | N/A |
| nsm.3 | "Min spacing, no overlap, between NSM_keepout to […] metX.dg (X=1 to 5) and cmmX.mk (X=1 to 5). […]" (AL) | 1.000 µm |
| x.1b | "Data for SKY130 layout and mask on all layers except those mentioned in 1a must be on a grid of mm (except inside Seal ring)" | 0.005 (unit "mm") |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.11 | "Metal fuses are drawn in met4" (LVS) | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |

The other fuse rules, mf.6 to mf.19, mf.21, mf.22 and mf.24, set the
spacings of a fuse centre to other layers and the size, placement and
spacing of fuse shields and fuse contacts; the Error Messages page gives
their target spacings slightly below the periphery values (for example
3.295 for mf.6, mf.7, mf.19 and mf.24, against 3.300).[^pdk-periph][^pdk-errors]
Rule mf.5 is printed without a unit, and mf.23, the spacing to metal 4, has the
value "N/A" (our reading: the fuse is itself metal 4 in this
flow).[^pdk-periph] Table 2 of *Criteria & Assumptions* gives `MM4CD` and
`MM4CDSP` as 0.3 and 0.3, and the same for a "Metal 4-Cu" row
(`MM4_CuCD`, `MM4_CuCDSP`), a copper back end that SKY130's aluminium
flow does not use; Table 4 adds, in its "Material Thicknesses" block,
the "Oxide Bias for MM4" of 1.15 (`BiasMM4`) and the metal-4 antenna
thicknesses of 0.8 and 2; Table 5 gives the laser-fuse criteria quoted
above; Table 7 a "Huge metal X min. W and L" of 3 (`HugeM`), in its column
headed "CD"; and Table 9 the 12 of polyimide around fuses and the 30
around laser targets.[^pdk-03] For
the plate the decisive figures are 0.300 µm lines on a 0.6 µm pitch (our
arithmetic from m4.1 and m4.2), with 0.800 µm fuse links among them.

## Related pages

* {ref}`MM4 <step-154>` and {ref}`MM4E <step-155>` — the mask step and
  the metal etch; {ref}`WTIAL4 <step-149>` — the stack patterned.
* {ref}`mask-cap2m` — the capacitor mask whose plates metal 4 must
  enclose; {ref}`mask-vim3` and {ref}`mask-vim4` — the via masks below and
  above; {ref}`mask-mm3` and {ref}`mask-mm5` — the metal masks one level
  down and up.
* {ref}`masks-index` — every mask's PDK entry, plates and renders, and the
  derivation table that records the `MM4` render's layers.
* {ref}`machine-i-line-stepper` and {ref}`machine-duv-krf-stepper` — the
  two exposure classes the step page leaves open.
* {ref}`machine-plasma-etcher-metal` — the etch class that transfers the
  pattern.
* {ref}`machine-cd-sem-overlay-metrology` — line CD and overlay
  measurement.
* {ref}`material-lithography-materials` — resists, anti-reflective
  coatings, developer and reticles.
* {ref}`category-lithography`, {ref}`category-etch` and
  {ref}`category-cmp` — the mask step, etch and polish categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "Metal 4, MM4,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `met4` 71:20
  and its fuse purpose, the `cmm4` purposes, `target`, Table C3 and the
  columns of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `MM4CD`/`MM4CDSP`,
  `MM4_CuCD`/`MM4_CuCDSP`, `BiasMM4`, the metal-4 antenna thicknesses, the
  laser-fuse criteria, `HugeM`, `PimFuseEnc` and `PimLaserEnc`.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `m4` rules, via4.4, the fuse note
  and `mf` rules, nsm.3, x.1a, x.1b, x.7, x.9, x.11, x.15a and the flag
  legend.[^pdk-periph]
* SkyWater PDK, *Summary of Key Periphery Rules* — Table F4.[^pdk-summary]
* SkyWater PDK, *Error Messages* page — the metal-4 fuse checks and the
  `cmm4.nikon` checks.[^pdk-errors]
* SkyWater PDK, *Process stack diagram* — the 0.845 µm `metal4`.[^pdk-04]
* SkyWater PDK, *Device Details* — the stacked MiM cross-section with its
  two metal-4 plates.[^pdk-07]
* SkyWater PDK, *Parasitic Layout Extraction* — the metal sheet
  resistances.[^pdk-08]
* *S8 / SKY130 Process Steps* sheet — the step, the `MM4` plates of
  MPW-1 to MPW-8, the "Info" note and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `MM4` renders, their layers
  and info text, and the per-die shape counts.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the i-line and DUV exposure
  tools.[^skw-01]
* ASML, *Three decades of PAS 5500* — older exposure tools moving to less
  critical layers.[^asml-30]

### High-level understanding

* Wikipedia, *Photomask* — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wikipedia, *Photolithography* — i-line and DUV exposure.[^wiki-litho]
* Mack, *Fundamental Principles of Optical Lithography* — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* Levinson, *Principles of Lithography* — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]

### Deep dive

* Smith et al., *IEEE JSSC* 1981 — laser-programmed
  redundancy, link geometry, spot size and targeting.[^smith-1981]
* Tian, Wong and Boone, *IEEE TCAD* 2001 — model-based dummy-feature
  placement over single and multiple layers.[^tian-2001]
* Kahng et al., *IEEE TCAD* 1999 — fill synthesis to density bounds in
  fixed windows.[^kahng-1999]
* Kahng and Samadi, *IEEE TCAD* 2008 — a survey of CMP fill
  synthesis.[^kahng-2008]
* Stine et al., *IEEE TSM* 1998 — pattern density as the dominant factor
  in dielectric polishing.[^stine-1998]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor of dense
  lines and the size below which it rises.[^wong-1998]
* Hochmuth, Ruhl and Coleman, *Proc. SPIE* 1999 — plate CD against chrome
  loading in dry-etched masks.[^hochmuth-1999]
* Brunner, *Proc. SPIE* 1991 — the swing ratio and anti-reflective
  coatings.[^brunner-1991]
* Rocke and Schneegans, *JVST B* 1988 — titanium nitride as an
  anti-reflection layer on aluminium.[^rocke-1988]
* Bohr, IEDM 1995 — interconnect as the limit on performance.[^bohr-1995]
* Stamper, Fuselier and Tian, IITC 1998 — RC delay of aluminium wiring
  below 0.25 µm.[^stamper-1998]
* Ng et al., *IEEE TED* 2005 — MiM integration in Al–Cu and copper back
  ends.[^ng-2005]
* Kar-Roy and Racanelli (Newport Fab), US 6,430,028 — the bottom-plate
  metal patterned after the top plate.[^pat-mim-newportfab]

## Open questions

* The operation that makes the `cmm4` plate data from `met4`, its fuse
  purpose and the waffle-drop purpose is not published, nor whether a
  waffle-drop shape places fill or keeps it out; the renders' fill layer
  51:28 is not in `gds_layers.csv`, and the renders leave out the fuse
  purpose.[^pdk-06][^pdk-periph][^mask-renders]
* Table F2b has no `MM4` column; Table 5 names metal 2 in its `FEXT` row,
  and whether its laser-fuse criteria apply to the metal-4 fuses of the
  PLM flow is not stated; that those fuses are laser-opened links printed
  by this mask is an inference.[^pdk-06][^pdk-03][^pdk-periph] The Error
  Messages page's target spacings differ from the periphery tables by
  0.005 to 0.010 without explanation, and it does not explain its "nikon cross"
  checks.[^pdk-errors]
* Whether the level is exposed on an i-line or a KrF tool, and the
  plate's type, tone and CD specification, the resist and anti-reflective
  scheme, are not public.
* The PDK publishes no enclosure of `cap2m` plates by metal 4, and the
  alignment tree between `CAP2M` and `MM4` is the step page's open
  question.[^pdk-periph]
* What the plate number `580` encodes is not stated, and no public source
  lists the `MM4` plate of the original MPW-4 set
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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 4,
    5, 7 and 9), SkyWater SKY130 PDK documentation.
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
    directory: `README.md` and, for each run, the `mpw-00N_MM4/`
    directory with its page, `job.json`, `result.json` and per-die slot
    JSON files, retrieved 2026-09-14. Rendered from the public shuttle
    repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021.
    <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
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
[^smith-1981]: R. T. Smith, J. D. Chlipala, J. F. M. Bindels, R. G. Nelson,
    F. H. Fischer and T. F. Mantz, "Laser programmable redundancy and
    yield improvement in a 64K DRAM", *IEEE Journal of Solid-State
    Circuits* **16**(5), 506–514 (1981).
    <https://doi.org/10.1109/JSSC.1981.1051630>
[^tian-2001]: R. Tian, M. D. F. Wong and R. Boone, "Model-based dummy
    feature placement for oxide chemical-mechanical polishing
    manufacturability", *IEEE Transactions on Computer-Aided Design of
    Integrated Circuits and Systems* **20**(7), 902–910 (2001).
    <https://doi.org/10.1109/43.931037>
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
