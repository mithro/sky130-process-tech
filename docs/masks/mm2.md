(mask-mm2)=
# MM2 — Metal 2

The metal-2 mask is the {term}`reticle` that draws SKY130's second
aluminium wiring level: on the {ref}`MM2 <step-124>` page's reading, the
resist printed through it at step 124 stays wherever `met2` is drawn,
and the {ref}`MM2E <step-125>` etch removes the metal stack everywhere
else. Its rules repeat metal 1's 0.14 µm lines and spaces, the step pages
read it as a critical KrF level, and it is one of the four masks whose "mask data" rule
x.1a names for its 0.001 grid. With metal 5, it is also one of
the two masks for which a transcribed plate-case label is public,
although the label is not tied to an MPW run. This page gathers
what public sources say about the mask itself — its PDK entry and
layers, the plates the process-steps sheet records for the MPW runs,
what the public renders of those runs show, the lithography it needs and
the rules that constrain it. How the step is performed is on the step
page; every mask is indexed on the {ref}`masks index <masks-index>`.

| | MM2 — Metal 2 |
|---|---|
| Mask step | {ref}`MM2 <step-124>`, step 124 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Metal 2", `MM2`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cmm2` mask 41:0, "Metal 2 mask"; waffle drop 105:52[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `met2` drawing 69:20, "Metal 2"[^pdk-06] |
| Minimum CD, feature / space | `MM2CD` 0.14 / `MM2CDSP` 0.14[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist remains where `met2` is drawn, which with a positive resist would make the plate clear-field (inference). |
| Exposure class | KrF (248 nm) with resolution enhancement, an inference on the step page from the 0.14 µm rules and the exposure options ITRS 2001 lists for the 130 nm node; no public source names the tool ({ref}`machine-duv-krf-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `550`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-mm2-steps>` |

## What the mask defines

The periphery rules give the function of the `m2` rule set as "Defines
second level of metal interconnects, buses etc", and the PDK's Table F4
shows metal 2 joined to metal 1 by "Via" and to metal 3 by
"Via2".[^pdk-periph][^pdk-summary] The mask carries lines at the
0.140 µm minimum width and space (m2.1, m2.2), pads that enclose the vias
below by 0.055 µm (m2.4) and the via-2 plugs above by 0.040 µm (via2.4),
wide "huge_met2" features that need 0.280 µm of space (m2.3a, m2.3b),
and, on our reading of the waffle-drop rules below, dummy fill; its
smallest island is 0.0676 µm² (m2.6) and its smallest hole 0.140 µm²
(m2.7).[^pdk-periph] The PDK's extraction table gives metal 2 the same
sheet resistance as metal 1, 125 in a column headed "Resistivity
(mohms/sq)".[^pdk-08]

The PDK's mask generation table, Table F2b, marks the `MM2` column `C`
("CREATED") in four of its 80 device rows — "metal fuse_T", "MiM",
"VPP" and "VPP (with met3 shield)" — and `+`, "Layer allowed to
overlap", in the other 76.[^pdk-06] Two of these tie the level to devices
beyond wiring. One row of rule x.11 reads "Metal fuses are drawn in met2",
with values "N/A", beside rows naming met3 and met4, and the fuse rules
keep metal 2 3.300 µm from a fuse centre (mf.19);[^pdk-periph] and the
function line of the via-2 rules names a "SKY130DI\*" flow in which via 2
connects "met2/capm to met3".[^pdk-periph] We read the `C` marks for the
fuse and the MiM capacitor as belonging to flows other than the one this
reference follows, whose `CAPM` capacitor the
{ref}`masks index <masks-index>` places on metal 3 from the test tile's
pad documentation; the PDK does not say which flow a `C` refers to.

The mask does not define the metal stack it patterns, which
{ref}`TIAL12 <step-123>` deposits, the vias beneath it ({ref}`mask-vim`)
or the via-2 plugs above it (`VIM2`), and on the step pages' readings the
dielectric that fills its spaces is deposited afterwards by
{ref}`NILD4 <step-126>` and polished by {ref}`CMPM2 <step-127>`.

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives the mask-level layer `cmm2` two purposes: `mask`
at 41:0 ("Metal 2 mask") and `waffle drop` at 105:52, on a different
layer number and without a description; the drawn layer is `met2` at
69:20.[^pdk-06] The pairing rests on those names and descriptions, as on
the {ref}`masks index <masks-index>`, and the PDK publishes no operation
from `met2` to the plate. Rule x.15a confines "Drawn compatible, mask,
and waffle-drop layers" to test modules, seal ring and frame, "Exception:
FOM/P1M/Metal waffle drop are allowed inside the die" (flag P, periphery
only),[^pdk-periph] so a die may carry `cmm2` waffle-drop shapes as well
as `met2` (our reading); with no add or drop purpose, rule x.9's
"serifs" have no `cmm2` layer to sit on. The rule set's first entry,
flagged RC, flags a 700 × 700 window "covered by cmm2 waffleDrop" when the
metal pattern density of the same window is below a limit that falls
from 70 % for a fully covered window to 30 % for one 30–40 %
covered.[^pdk-periph] The PDK does not say whether a waffle-drop shape
places fill or keeps it out; the {ref}`MM2 <step-124>` page reads the
`cmm2` fill and the 0.7 density rule as existing for the
{ref}`CMPM2 <step-127>` polish.

Rule x.1a puts the "mask data for p1m, met1, via, met2" on a grid of
0.001, against 0.005 for "all layers except those mentioned in 1a"
(x.1b), both printed with the unit "mm".[^pdk-periph] Reading the unit
as µm, a 1 nm wafer grid is a 4 nm grid on a 4× plate (our arithmetic);
Samuels, Maurer and Farrell examined "how fine a grid size is needed in
the manufacture of the mask" once OPC is applied.[^samuels-1995] The PDK
does not say why the metal-2 data need the finer grid. Rule nsm.3 lists
"metX.dg (X=1 to 5) and cmmX.mk (X=1 to 5)" among the layers kept
1.000 µm from the nitride-seal keep-out (flag AL).[^pdk-periph]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `MM2` the site renders layer 69:20 (`met2`)
together with 41:28, which it lists as a fill layer, with no Boolean
expression and no note, on all eight runs; its mask record gives the
mask-level layer 41:0 and the info text "Metal 2".[^mask-renders] Layer
41:28 is not in `gds_layers.csv`, whose `cmm2` waffle-drop purpose is
105:52,[^pdk-06] so the site's choice of it is one public reading of the
tape-out files, not a PDK definition, and like the site's other layer
choices it is not SkyWater's mask-generation recipe
({ref}`masks-derivations`). The info text is identical to the "Info" note
of the `MM2` row in the process-steps sheet, so neither is cited as
corroborating the other
({ref}`masks-renders-sheet-notes`).[^steps-sheet][^mask-renders]

Every rendered die of every run carries shapes on these layers — at
least 9 561 696 on each die, fill included[^mask-renders] — so the count
of 40 dies says only that every layout has metal 2. The site states the
limits of its images: "These are renders of *drawn* data, not photomask
artwork: reticle pitch, 4x reduction, mirroring and the frame features
the fab adds are not modelled."[^mask-renders] The metadata carries no
plate ID, so a render is tied to a plate in the process-steps sheet only
by the acronym `MM2`, and the MPW-4 renders come from a different reticle
set from the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `MM2` plate
as existing on all eight MPW runs, with the plate number `550` on
each.[^steps-sheet] The plate IDs below are the sheet's; the reticle set
is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA550A` |
| MPW-2 | `5CS8007AC` | `S8007AA550A` |
| MPW-3 | `5CS8008AC` | `S8008AA550A` |
| MPW-4 | `5CS8018AC` | `S8018AA550A` |
| MPW-5 | `5CS8011AC` | `S8011AA550A` |
| MPW-6 | `5CS8014AC` | `S8014AA550A` |
| MPW-7 | `5CS8016AC` | `S8016AA550A` |
| MPW-8 | `5CS8017AC` | `S8017AA550A` |

* **MPW-5.** Unlike `CTM1`, `MM1` and `VIM`, the masks just below it, an
  `MM2` plate is recorded for MPW-5; the masks index reads the MPW-5 gaps
  of those masks as more likely gaps in the record than in the run
  ({ref}`masks-mpw-runs`).[^steps-sheet]
* **Plate number.** The sheet does not say what `550` encodes. It falls
  between `500` for `VIM` and `560` for `VIM2`, but the numbers do not
  follow process order elsewhere (`CAPM`, step 137, is `572` against
  `MM3`, step 139, `570`), so no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Plate-case label.** The sheet's "Random Mask Case Label Info" tab
  transcribes a Photronics plate-case label whose part-number field names
  `MM2` and the number 550. It gives the material as a 6 × 6 × 0.25 in
  blank, the type as "4X Beam Final", a "Percent Clear" of 56.64 and a
  "Level" of 4, and a CD specification for patterns it names "Scribe FA DI X
  / LINE / X" and "Scribe FA DI Y / LINE / Y", nominal 0.568 with tolerances of 0.02 either way, measured at means
  of 0.5497 (X) and 0.5588 (Y), in no stated unit.[^steps-sheet] The tab
  does not tie the label to one of the MPW runs ({ref}`masks-mpw-runs`) or
  define its fields; we read "4X" as the reduction ratio and "Percent
  Clear" as the transmitting share of the plate area (inference from the
  field names alone). Hochmuth, Ruhl and Coleman found that with chrome
  dry etch "the deviation of the CD from the target value is a function
  of the chrome loading on the plate", and compensated by dose or develop
  time "based on the pattern loading of a particular mask
  level";[^hochmuth-1999] whether the recorded percentage serves that
  purpose is not stated.
* **Mask type.** The sheet's "Sheet4" tab gives no type for
  `MM2`.[^steps-sheet] 4× is the ITRS 2001 mask magnification for the
  130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`MM2 <step-124>` page gives
{math}`k_1 = 0.14 \times 0.70 / 0.248 \approx 0.40` on a KrF lens of NA
0.70 and 0.45 at NA 0.80, and infers a 248 nm level from the rules and
from ITRS 2001, which lists "248 nm + PSM" and "193 nm" as the exposure
options for the 130 nm node and says that "only 248 nm lithography has a
mature infrastructure";[^itrs-03] the
{ref}`KrF stepper <machine-duv-krf-stepper>` page lists it there.
SkyWater lists "ASML DUV stepper" and "ASML DUV scanner" but assigns no
layer to them.[^skw-01] Word, Zhu and Sturtevant put the KrF
{math}`k_1` of the 130 nm node at "only approximately 0.35" and obtained
a process window for all pitches with assist features and optimised
illumination;[^word-2002] Shi et al. traced the "forbidden pitch" to
destructive interference between the fields of neighbouring features and
the main feature.[^shi-2002] The step page names Shiraishi et al.'s
illumination technique, which gave 0.35 µm lines and spaces 2.5 times the
depth of focus of conventional illumination in
simulation.[^shiraishi-1992]

**Mask errors.** Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns", and that
"dense lines and spaces exhibit markedly higher MEF values than isolated
features";[^wong-1998] at 248 nm and NA 0.7 the threshold is about
0.18 µm (our arithmetic), above the 0.14 µm lines, so plate CD errors on
dense metal-2 lines would print magnified (inference). ITRS 2001's
optical mask requirements, which are "for critical layers", ask in 2001
for a mask CD uniformity of 10.4 nm (3σ) on dense lines at 4×
magnification.[^itrs-03] How tightly SkyWater specifies the `MM2` plate
is not public; the label above records a specification for one scribe
feature only.

**Reflective substrate.** The resist sits on the capped metal stack
({ref}`overview-metal-cap`)
of {ref}`TIAL12 <step-123>` (the step page's reading). Chen, Chen and
Tsou traced notched metal lines to "reflective notching in photo
processing" and used TiN as an anti-reflective layer in a sub-micrometre
process;[^chen-1991-tin] Rocke and Schneegans used titanium nitride on
aluminium for the same purpose;[^rocke-1988] and Brunner showed that the
swing ratio scales with the square root of the substrate reflectivity,
which an anti-reflective coating reduces.[^brunner-1991] The step page
reads a chemically amplified positive KrF resist, probably over an organic
{term}`BARC`; with the resist left where `met2` is drawn, the plate would
be clear-field (inference). Neither is published. The consumables are on
the {ref}`lithography materials <material-lithography-materials>` page.

**Fill and the polish above.** Kahng and Samadi note that "Post-CMP
wafer topography varies according to pattern density",[^kahng-2008] and
Stine et al. found pattern density "a strongly dominant factor" in
interlevel-dielectric polishing.[^stine-1998] The PDK's "Oxide Bias for
MM2" of 0.6 (`BiasMM2`) sits in Table 4's first block, headed "Material
Thicknesses" with a column headed "Value (um)", not with its "Waffling /
Pattern Density" criteria;[^pdk-03] the {term}`oxide bias` glossary entry
records the step pages' reading of it.

**Pattern transfer.** On the step pages' readings the resist pattern is
transferred by {ref}`MM2E <step-125>`, a chlorine etch of the whole
metal stack that stops on the via-1 cap oxide and the via plugs, on the
{ref}`metal plasma etcher <machine-plasma-etcher-metal>` class, with
passivation, resist strip and clean treated as part of that step.

**Overlay.** Metal 2 must enclose each via below by 0.055 µm (m2.4) and
by 0.085 µm on one of two adjacent sides (m2.5), and each via 2 above by
0.040 µm (via2.4).[^pdk-periph] The {ref}`MM2 <step-124>` page reads the
mask as aligned to the via layer and, through it, to metal 1, and leaves
open which layer's targets it uses.

(mask-mm2-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `MM2` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`MM2 <step-124>`, {ref}`MM2E <step-125>`

* {ref}`MM2 <step-124>` — coats, exposes and develops the resist.
* {ref}`MM2E <step-125>` — etches the metal stack through the resist;
  the step list used in this reference has no separate strip step, and
  the step page treats the passivation, resist strip and wet clean as
  part of the etch.

On its step page's reading, the next step, {ref}`NILD4 <step-126>`,
deposits the inter-level oxide between metal 2 and metal 3 over the
etched lines after the resist is gone, and the next mask step is
{ref}`VIM2 <step-129>`. The rule needs no exception for this mask; the
only departure from a mask–etch–strip pattern is that the strip has no
step of its own.

## Design rules and critical dimensions

The `m2` rules of the periphery rules, with the via-2 enclosures by metal
2, the fuse rules that name metal 2, and the mask-data rules x.1a, x.1b,
x.7, x.11 and x.15a. Flag P means "Rule applies to periphery only
(outside areaid.ce). A corresponding core rule may or may not exist.",
AL "Rules applicable only to Al BE flows", CU "Rules applicable only to
Cu BE flows", A "Rule documents a functionality implemented in CL
algorithms and may not be checked by DRC.", RR "Recommended rule at any
IP level", RC "Recommended rule at the chip level, required rule at the
IP level.", LVS "Rule handled by LVS" and NC "Rule not checked by DRC. It
should be used as a guideline only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| m2.- | "Algorithm should flag errors, for met2, if ANY of the following is true: […] An entire 700x700 window is covered by cmm2 waffleDrop, and metX PD < 70% for same window. […]" (RC) | — |
| m2.1 | "Width of metal 2" | 0.140 µm |
| m2.2 | "Spacing of metal 2 to metal 2" | 0.140 µm |
| m2.3a | "Min. spacing of features attached to or extending from huge_met2 for a distance of up to 0.280 µm to metal2 […]" | 0.280 µm |
| m2.3b | "Min. spacing of huge_met2 to metal2 excluding features checked by m2.3a" | 0.280 µm |
| m2.3c | "Min spacing between floating_met2 with AR_met2_A >= 0.05 and AR_met2_B =< 0.032, outside areaid:sc must be greater than" (RR) | 0.145 µm |
| m2.4 | "Via must be enclosed by Met2 by at least …" (P AL) | 0.055 µm |
| m2.5 | "Via must be enclosed by Met2 on one of two adjacent sides by at least …" (AL) | 0.085 µm |
| m2.6 | "Min metal2 area" | 0.0676 µm² |
| m2.7 | "Min area of metal2 holes" | 0.140 µm² |
| m2.pd.1 | "Min MM2_oxide_Pattern_density" (RR) | 0.7 |
| m2.pd.2a | "Rule m2.pd.1 has to be checked by dividing the chip into square regions of width and length equal to …" (A) | 700 µm |
| m2.pd.2b | "Rule m2.pd.1 has to be checked by dividing the chip into steps of …" (A) | 70 |
| m2.11–m2.15 | Maximum width, slotting threshold, maximum pattern density, its window and step, and a via enclosure, for copper flows (CU) | 4.000 µm, 3.200, 0.77, 50.000 µm, 25.000 µm, 0.040 µm |
| via2.4 | "Via2 must be enclosed by Met2 by at least …" (AL) | 0.040 µm |
| via2.4a | "Inside areaid.mt, 1.5 µm Via2 must be enclosed by met2 by atleast" | 0.140 µm |
| via2.5 | "Via2 must be enclosed by Met2 on one of two adjacent sides by at least …" (AL) | 0.085 µm |
| mf.19 | "Spacing (no overlapping) between fuse center and Metal2" | 3.300 µm |
| nsm.3 | "Min spacing, no overlap, between NSM_keepout to […] metX.dg (X=1 to 5) and cmmX.mk (X=1 to 5). […]" (AL) | 1.000 µm |
| x.1a | "p1m.md (OPC), DECA and AMKOR layers (pi1.dg, pmm.dg, rdl.dg, pi2.dg, ubm.dg, bump.dg) and mask data for p1m, met1, via, met2 must be on a grid of mm" | 0.001 (unit "mm") |
| x.1b | "Data for SKY130 layout and mask on all layers except those mentioned in 1a must be on a grid of mm (except inside Seal ring)" | 0.005 (unit "mm") |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.11 | "Metal fuses are drawn in met2" (LVS) | N/A |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |

Table 2 of *Criteria & Assumptions* repeats the width and space as
`MM2CD` 0.14 and `MM2CDSP` 0.14, and gives the same values for a "Metal 2
- Cu" row (`MM2_CuCD`, `MM2_CuCDSP`), a copper back end that SKY130's
aluminium flow does not use.[^pdk-03] Table 4 adds the "Oxide Bias for
MM2" of 0.6 (`BiasMM2`), a "Metal 2 thickness for antenna ratio
calculations (S8D\*)" of 0.35 (`Met2Thick`) and the same 0.35 for
"(SP8T/S8T\*)" (`Met2_Qthick`), and the pattern-density criteria it
shares with metal 1; Table 5, the laser-fuse criteria, gives a "Max.
extension of met2 beyond fuse boundary" of 0.005 (`FEXT`), and Table 7 a
"Huge metal X min. W and L" of 3 (`HugeM`).[^pdk-03] The summary Table F3c, "Back end layers for S8D\*
flow", repeats metal 2 as 0.140 wide on a 0.140 space, enclosing the via by
"0.055 / 0.085" and via 2 by 0.040.[^pdk-summary] For the plate the
decisive figures are 0.140 µm lines on a 0.28 µm pitch (our arithmetic
from m2.1 and m2.2).

## Related pages

* {ref}`MM2 <step-124>` and {ref}`MM2E <step-125>` — the mask step and
  the metal etch; {ref}`TIAL12 <step-123>` — the stack patterned.
* {ref}`mask-vim` — the via mask whose plugs metal 2 covers;
  {ref}`mask-mm1` — the metal mask one level down.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the tables this page's plate facts are taken from.
* {ref}`machine-duv-krf-stepper` — the exposure class the step page
  assigns.
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

* SkyWater PDK, *Masks* page and `masks.csv` — "Metal 2, MM2,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `met2` 69:20,
  the `cmm2` purposes and the `MM2` column of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `MM2CD`/`MM2CDSP`,
  `MM2_CuCD`/`MM2_CuCDSP`, `BiasMM2`, `Met2Thick`, `Met2_Qthick`, `FEXT`
  and `HugeM`.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `m2` rules, via2.4, via2.4a,
  via2.5, the via-2 function line, mf.19, nsm.3, x.1a, x.1b, x.7, x.9,
  x.11, x.15a and the flag legend.[^pdk-periph]
* SkyWater PDK, *Summary of Key Periphery Rules* — Tables F3c and
  F4.[^pdk-summary]
* SkyWater PDK, *Parasitic Layout Extraction* — the metal-2 sheet
  resistance.[^pdk-08]
* *S8 / SKY130 Process Steps* sheet — the step, the `MM2` plates of
  MPW-1 to MPW-8, the "Info" note, the mask-type tab and the plate-case
  label.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `MM2` renders, their layers
  and info text, and the per-die shape counts.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the DUV exposure
  tools.[^skw-01]

### High-level understanding

* Wikipedia, *Photomask* — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wikipedia, *Optical proximity correction* — why mask shapes differ
  from drawn shapes.[^wiki-opc]
* Mack, *Fundamental Principles of Optical Lithography* — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* Levinson, *Principles of Lithography* — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]

### Deep dive

* Word, Zhu and Sturtevant, *Proc. SPIE* 2002 — assist-feature OPC for
  the 130 nm node with KrF and no forbidden pitches.[^word-2002]
* Shi et al., *Proc. SPIE* 2002 — the forbidden-pitch phenomenon and
  assist-feature placement.[^shi-2002]
* Shiraishi et al. (Nikon), *Proc. SPIE* 1992 — an illumination
  technique for dense lines.[^shiraishi-1992]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor of dense
  and isolated lines.[^wong-1998]
* Samuels, Maurer and Farrell, *Proc. SPIE* 1995 — OPC, mask CD
  tolerance and mask grid size.[^samuels-1995]
* Hochmuth, Ruhl and Coleman, *Proc. SPIE* 1999 — plate CD against
  chrome loading in dry-etched masks.[^hochmuth-1999]
* Chen, Chen and Tsou, VMIC 1991 — reflective notching of metal lines
  and a TiN anti-reflective layer.[^chen-1991-tin]
* Rocke and Schneegans, *JVST B* 1988 — titanium nitride as an
  anti-reflection layer on aluminium.[^rocke-1988]
* Brunner, *Proc. SPIE* 1991 — the swing ratio and anti-reflective
  coatings.[^brunner-1991]
* Kahng and Samadi, *IEEE TCAD* 2008 — a survey of CMP fill
  synthesis.[^kahng-2008]
* Stine et al., *IEEE TSM* 1998 — pattern density as the dominant
  factor in dielectric polishing.[^stine-1998]
* ITRS 2001, *Lithography* — the optical mask requirements for critical
  layers at 130 nm.[^itrs-03]

## Open questions

* The operation that makes the `cmm2` plate data from `met2` and the
  waffle-drop purpose is not published, nor whether a waffle-drop shape
  places fill or keeps it out.[^pdk-06][^pdk-periph]
* The plate's type, tone and CD specification, the resist and
  anti-reflective scheme, and the exposure tool are not public; the KrF
  reading rests on the 0.140 µm rules.
* Table F2b's `C` marks for the metal fuse and the MiM capacitor in the
  `MM2` column are not tied to a flow, and the x.11 row for met2 gives
  only "N/A".[^pdk-06][^pdk-periph]
* The plate-case label's fields are not defined, and the label is not
  tied to an MPW run or reticle set.[^steps-sheet]
* The renders' fill layer 41:28 is not in `gds_layers.csv`, which gives
  the `cmm2` waffle drop as 105:52, so what the site takes it to be rests
  on the site alone.[^mask-renders][^pdk-06]
* What the plate number `550` encodes is not stated, and no public source
  lists the `MM2` plate of the original MPW-4 set
  `5CS8010AC`.[^steps-sheet][^mask-renders]

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tabs "Sheet1" (step number, code and description), "Masks"
    (mask steps with step numbers), "Run Mask IDs" (the mask table set
    against MPW-1 to MPW-8, with "Exists", "Plate ID" and "Info" columns),
    "Sheet4" (mask types) and "Random Mask Case Label Info" (plate-case
    labels), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* (including Table F2b,
    the mask generation table) and `gds_layers.csv`, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 4, 5
    and 7), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-summary]: SkyWater PDK Authors, *Summary of Key Periphery Rules*
    (Tables F3c and F4), SkyWater SKY130 PDK documentation, retrieved
    2026-09-13.
    <https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_MM2/`
    directory with its page, `job.json`, `result.json` and per-die slot
    JSON files, retrieved 2026-09-13. Rendered from the public shuttle
    repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-opc]: Wikipedia, *Optical proximity correction*.
    <https://en.wikipedia.org/wiki/Optical_proximity_correction>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^word-2002]: J. C. Word, S. Zhu and J. L. Sturtevant, "Assist feature
    OPC implementation for the 130 nm technology node with KrF and no
    forbidden pitches", *Proc. SPIE* **4691**, Optical Microlithography
    XV, 1139 (2002). <https://doi.org/10.1117/12.474494>
[^shi-2002]: X. Shi, S. Hsu, J. F. Chen, C. M. Hsu, R. J. Socha and
    M. V. Dusa, "Understanding the forbidden pitch phenomenon and assist
    feature placement", *Proc. SPIE* **4689**, Metrology, Inspection,
    and Process Control for Microlithography XVI, 985 (2002).
    <https://doi.org/10.1117/12.473427>
[^shiraishi-1992]: N. Shiraishi, S. Hirukawa, Y. Takeuchi and
    N. Magome, "New imaging technique for 64M-DRAM", *Proc. SPIE*
    **1674**, Optical/Laser Microlithography V, 741 (1992).
    <https://doi.org/10.1117/12.130364>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**,
    Optical Microlithography XI, 106 (1998).
    <https://doi.org/10.1117/12.310718>
[^samuels-1995]: D. J. Samuels, W. Maurer and T. R. Farrell, "Good OPC,
    where will this drive mask CD tolerance and mask grid size", *Proc.
    SPIE* **2621**, 15th Annual BACUS Symposium on Photomask Technology
    and Management, 588–596 (1995). <https://doi.org/10.1117/12.228213>
[^hochmuth-1999]: J. Hochmuth, G. G. Ruhl and T. P. Coleman, "Control
    methodology of off-target for varying pattern densities with chrome
    dry etch", *Proc. SPIE* **3873**, 19th Annual Symposium on Photomask
    Technology, 297 (1999). <https://doi.org/10.1117/12.373324>
[^chen-1991-tin]: S. Chen, C. L. Chen and S. Tsou, "Sputtered TiN
    performance as an anti-reflective coating in backend sub-µm i-line
    lithography process", *Proc. Eighth International IEEE VLSI
    Multilevel Interconnection Conference (VMIC 1991)*, pp. 393–395.
    <https://doi.org/10.1109/VMIC.1991.153035>
[^rocke-1988]: M. Rocke and M. Schneegans, "Titanium nitride for
    antireflection control and hillock suppression on aluminum silicon
    metallization", *Journal of Vacuum Science & Technology B* **6**(4),
    1113–1115 (1988). <https://doi.org/10.1116/1.584306>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
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
