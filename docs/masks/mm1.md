(mask-mm1)=
# MM1 — Metal 1

The metal-1 mask is the {term}`reticle` that draws SKY130's first
aluminium wiring level: on the {ref}`MM1 <step-113>` page's reading, the
resist printed through it at step 113 stays wherever `met1` is drawn,
and the {ref}`MM1E <step-114>` etch removes the metal stack everywhere
else. With 0.14 µm lines on 0.14 µm spaces it is, with metal 2, the
tightest line pattern of the back end, the step pages read it as a
critical KrF level, and it is one of the four masks whose "mask data" rule x.1a
names for its 0.001 grid. It is also one of the levels on which the PDK
allows waffle-drop shapes inside the die. This page gathers what public
sources say
about the mask itself — its PDK entry and layers, the plates the
process-steps sheet records for the MPW runs, what the public renders of
those runs show, the lithography it needs and the rules that constrain
it. How the step is performed is on the step page; every mask is indexed
on the {ref}`masks index <masks-index>`.

| | MM1 — Metal 1 |
|---|---|
| Mask step | {ref}`MM1 <step-113>`, step 113 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Metal 1", `MM1`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cmm1` mask 36:0, "Metal 1 mask"; waffle drop 62:24[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `met1` drawing 68:20, "Metal 1"[^pdk-06] |
| Minimum CD, feature / space | `MM1CD` 0.14 / `MM1CDSP` 0.14[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist remains where `met1` is drawn, which with a positive resist would make the plate clear-field (inference). |
| Exposure class | KrF (248 nm) with resolution enhancement, an inference on the step page from the 0.14 µm rules and the exposure options ITRS 2001 lists for the 130 nm node; no public source names the tool ({ref}`machine-duv-krf-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all except MPW-5[^steps-sheet] |
| Plate no. | `450`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-mm1-steps>` |

## What the mask defines

The periphery rules give the function of the `m1` rule set as "Defines
first level of metal interconnects, buses etc;", and the PDK's Table F4
shows metal 1 joined to `li1` by "Mcon" and to metal 2 by
"Via".[^pdk-periph][^pdk-summary] The mask therefore carries lines at
the 0.140 µm minimum width and space (m1.1, m1.2), the landing pads that
enclose the contacts below by 0.030 µm (m1.4) and the vias above by
0.055 µm (via.4a), wide "huge_met1" features that need 0.280 µm of space
(m1.3a, m1.3b), and, on our reading of the waffle-drop rules below, dummy fill; its
smallest drawn island is 0.083 µm² (m1.6) and its smallest hole
0.140 µm² (m1.7).[^pdk-periph] The PDK's extraction table gives metal 1
a sheet resistance of 125 in a column headed "Resistivity
(mohms/sq)",[^pdk-08] so the printed line width is directly a resistance
(the {ref}`MM1 <step-113>` page's reading).

The PDK's mask generation table, Table F2b, marks the `MM1` column `C`
("CREATED") in two of its 80 device rows — "VPP" and "VPP (with met3
shield)" — and `+`, "Layer allowed to
overlap", in the other 78.[^pdk-06] We read this as metal 1 being part
of every device's wiring and a structural part of the VPP capacitors
only; the table does not explain its marks.

The mask does not define the metal stack it patterns, which
{ref}`TIAL6 <step-112>` deposits, the contacts beneath it
({ref}`mask-ctm1`) or the vias above it (`VIM`), and on the step pages'
readings the dielectric that fills its spaces is deposited afterwards by
{ref}`NILD3 <step-115>` and polished by {ref}`CMPM <step-116>`.

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives the mask-level layer `cmm1` two purposes: `mask`
at 36:0 ("Metal 1 mask") and `waffle drop` at 62:24, on a different
layer number and without a description; the drawn layer is `met1` at
68:20.[^pdk-06] The pairing rests on those names and descriptions, as on
the {ref}`masks index <masks-index>`, and the PDK publishes no operation
from `met1` to the plate. Rule x.15a confines "Drawn compatible, mask,
and waffle-drop layers" to test modules, seal ring and frame, "Exception:
FOM/P1M/Metal waffle drop are allowed inside the die" (flag P, periphery
only),[^pdk-periph] so a die may carry `cmm1` waffle-drop shapes as well
as `met1` (our reading); with no add or drop purpose, rule x.9's
"serifs" have no `cmm1` layer to sit on. The rule set's first entry,
flagged RC, spells out the fill check: it flags a 700 × 700 window
"covered by cmm1 waffleDrop" when the metal pattern density of the same
window is below a limit that falls from 70 % for a fully covered window
to 30 % for one 30–40 % covered.[^pdk-periph] The PDK does not say
whether a waffle-drop shape places fill or keeps it out; the
{ref}`FOM <step-004>` page reads the "waffles" as dummy fill for
{term}`pattern density`.

Two further rules name this mask's data. Rule x.1a puts the "mask data
for p1m, met1, via, met2" on a grid of 0.001, against 0.005 for "all
layers except those mentioned in 1a" (x.1b), both printed with the unit
"mm";[^pdk-periph] reading the unit as µm (our reading, since a 1 mm or
5 mm grid could not carry 0.14 µm lines), a 1 nm wafer grid is a 4 nm
grid on a 4× plate (our arithmetic). ITRS 2001 defines its "Mask design
grid" as "Wafer design grid times the mask magnification" and lists 8 nm
for 2001 and 4 nm for 2003.[^itrs-03] Samuels, Maurer and Farrell
examined how fine a correction OPC can realistically give and "how fine a
grid size is needed in the manufacture of the mask";[^samuels-1995] that
the finer grid serves a correction is our reading, not the PDK's. Rule
nsm.3 lists "metX.dg (X=1 to 5) and cmmX.mk (X=1 to 5)" among the layers
kept 1.000 µm from the nitride-seal keep-out (flag AL).[^pdk-periph]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `MM1` the site renders layer 68:20 (`met1`)
together with 36:28, which it lists as a fill layer, with no Boolean
expression and no note, on all eight runs; its mask record gives the
mask-level layer 36:0 and the info text "Metal 1".[^mask-renders] Layer
36:28 is not in `gds_layers.csv`, whose `cmm1` waffle-drop purpose is
62:24,[^pdk-06] so the site's choice of it is one public reading of the
tape-out files, not a PDK definition, and like the site's other layer
choices it is not SkyWater's mask-generation recipe
({ref}`masks-derivations`). The info text is identical to the "Info" note
of the `MM1` row in the process-steps sheet, so neither is cited as
corroborating the other
({ref}`masks-renders-sheet-notes`).[^steps-sheet][^mask-renders]

Every rendered die of every run carries shapes on these layers — at
least 9 266 129 on each die, fill included[^mask-renders] — so the count
of 40 dies says only that every layout has metal 1. For MPW-5 the
renders show shapes on all 40 dies although the sheet records no `MM1`
plate for that run, which fits the masks index's reading of the gap as
one in the record, but the renders show the drawn layouts, not the plates
({ref}`masks-mpw-runs`).[^mask-renders][^steps-sheet] The site states the
limits of its images: "These are renders of *drawn* data, not photomask
artwork: reticle pitch, 4x reduction, mirroring and the frame features
the fab adds are not modelled."[^mask-renders] The metadata carries no
plate ID, and the MPW-4 renders come from a different reticle set from
the one whose plates the sheet records ({ref}`masks-mpw-reticle-sets`).

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `MM1` plate
as existing on seven runs, with the plate number `450` on each, and has
no mark or plate ID for MPW-5.[^steps-sheet] The plate IDs below are the
sheet's; the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA450A` |
| MPW-2 | `5CS8007AC` | `S8007AA450A` |
| MPW-3 | `5CS8008AC` | `S8008AA450A` |
| MPW-4 | `5CS8018AC` | `S8018AA450A` |
| MPW-5 | `5CS8011AC` | none recorded |
| MPW-6 | `5CS8014AC` | `S8014AA450A` |
| MPW-7 | `5CS8016AC` | `S8016AA450A` |
| MPW-8 | `5CS8017AC` | `S8017AA450A` |

* **MPW-5.** The sheet records no plates for `CTM1`, `MM1`, `VIM`,
  `VIM4` and `PDM` on MPW-5 and gives no reason. The masks index reports
  what is recorded and does not conclude that the plate was absent from
  MPW-5: it reads a gap in the record as the likelier explanation, since
  every working die needs these masks (inference)
  ({ref}`masks-mpw-runs`).[^steps-sheet]
* **Plate number.** The sheet does not say what `450` encodes. It falls
  between `430` for the sky130B `RRM` mask and `455` for `VIMC`, and
  below `500` for `VIM`; the masks index notes that the renders site's
  `VIMC` note argues from exactly these numbers, but the numbers do not
  follow process order elsewhere, so no process position is read from
  it ({ref}`masks-renders-sheet-notes`).[^steps-sheet]
* **Mask type.** The sheet's "Sheet4" tab gives no type for
  `MM1`.[^steps-sheet] Whether the plate is binary with OPC or a
  phase-shift plate — the options the {ref}`MM1 <step-113>` page
  discusses — is not on public record. 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`MM1 <step-113>` page gives
{math}`k_1 = 0.14 \times 0.70 / 0.248 \approx 0.40` on a KrF lens of NA
0.70, at the "0.4 for production" boundary, and 0.45 at NA 0.80, and
infers a 248 nm level from the rules and from ITRS 2001, which lists
"248 nm + PSM" and "193 nm" as the exposure options for the 130 nm node
and says that "only 248 nm lithography has a mature
infrastructure";[^itrs-03] the {ref}`KrF stepper <machine-duv-krf-stepper>`
page lists it there. SkyWater lists "ASML DUV stepper" and "ASML DUV
scanner" but assigns no layer to them.[^skw-01] Word, Zhu and Sturtevant
put the KrF {math}`k_1` of the 130 nm node at "only approximately 0.35",
where "it becomes essential to apply some form of Resolution Enhancement
Technology", and obtained a process window for all pitches, forbidden
ones included, with sub-resolution assist features and optimised
illumination.[^word-2002] Shiraishi et al.'s illumination technique,
which the step page cites for off-axis illumination, gave 0.35 µm lines
and spaces 2.5 times the depth of focus of conventional illumination in
simulation, and resolved 0.275 µm on an i-line stepper in
experiment.[^shiraishi-1992]

**Mask errors.** Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns", and that
"The MEF of a 0.35 (lambda) /NA isolated line is 1.6 whereas that of a
dense line of the same dimension is 4.3".[^wong-1998] At 248 nm and NA
0.7 the threshold is about 0.18 µm and 0.14 µm is about 0.40 λ/NA (our
arithmetic), so plate CD errors on dense metal-1 lines would print
magnified (inference). Cheng and Neureuther, at 193 nm,
found that "The mask CD errors proved a major contribution to
isolated-dense line CD bias on the wafer".[^cheng-2002] ITRS 2001's
optical mask requirements, which are "for critical layers", ask in 2001
for a mask CD uniformity of 10.4 nm (3σ) on dense lines at 4×
magnification.[^itrs-03] How tightly SkyWater specifies the `MM1` plate
is not public.

**Reflective substrate.** The resist sits on metal. Rocke and Schneegans
note that the "High reflectivity of aluminum alloy layers causes
degradation to occur in photoresist images through reflective light
scattering", and use titanium nitride on top of the aluminium as an
anti-reflection layer;[^rocke-1988] Brunner showed that the swing ratio
scales with the square root of the substrate reflectivity, which an
anti-reflective coating reduces.[^brunner-1991] The step page reads the
refractory cap of {ref}`TIAL6 <step-112>` — TiW or TiN,
{ref}`overview-metal-cap` — as a partial anti-reflective layer
with an organic {term}`BARC` as the usual further step, and a chemically
amplified positive KrF resist; with the resist left where `met1` is
drawn, the plate would be clear-field (inference). None of this is
published. The consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Fill and the polish above.** The fill this mask prints serves the
oxide polish, not the lithography. Kahng and Samadi note that "Post-CMP
wafer topography varies according to pattern density",[^kahng-2008] and
Stine et al. found pattern density "a strongly dominant factor" in
interlevel-dielectric polishing.[^stine-1998] The PDK's "Oxide Bias for
MM1" of 0.6 (`BiasMM1`) sits in Table 4's first block, headed "Material
Thicknesses" with a column headed "Value (um)", not with its "Waffling /
Pattern Density" criteria;[^pdk-03] the {term}`oxide bias` glossary entry
records the step pages' reading of it as a density-related polish
allowance, which the PDK does not state.

**Pattern transfer.** On the step pages' readings the resist pattern is
transferred by {ref}`MM1E <step-114>`, a chlorine etch of the whole metal
stack that stops on the contact-level oxide and the tungsten plugs, on
the {ref}`metal plasma etcher <machine-plasma-etcher-metal>` class, with
passivation, resist strip and clean treated as part of that step.

**Overlay.** Metal 1 must enclose each contact by 0.030 µm (m1.4), which
the {ref}`MM1 <step-113>` page calls "the tightest {term}`overlay` in the
back end", and each via above by 0.055 µm (via.4a).[^pdk-periph]

(mask-mm1-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `MM1` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`MM1 <step-113>`, {ref}`MM1E <step-114>`

* {ref}`MM1 <step-113>` — coats, exposes and develops the resist.
* {ref}`MM1E <step-114>` — etches the metal stack through the resist;
  the step list used in this reference has no separate strip step, and
  the step page treats the passivation, resist strip and wet clean as
  part of the etch.

On its step page's reading, the next step, {ref}`NILD3 <step-115>`,
deposits the inter-level oxide over the etched lines after the resist is
gone, and the next mask step is {ref}`VIM <step-118>`. The rule needs no
exception for this mask; the only departure from a mask–etch–strip
pattern is that the strip has no step of its own.

## Design rules and critical dimensions

The `m1` rules of the periphery rules, with the via enclosures by metal
1, the mask-data rules x.1a, x.1b, x.7 and x.15a, and nsm.3, which names
the `cmm1` mask data. Flag P means "Rule applies to periphery only
(outside areaid.ce). A corresponding core rule may or may not exist.",
AL "Rules applicable only to Al BE flows", CU "Rules applicable only to
Cu BE flows", A "Rule documents a functionality implemented in CL
algorithms and may not be checked by DRC.", RR "Recommended rule at any
IP level", RC "Recommended rule at the chip level, required rule at the
IP level." and NC "Rule not checked by DRC. It should be used as a
guideline only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| m1.- | "Algorithm should flag errors, for met1, if ANY of the following is true: […] An entire 700x700 window is covered by cmm1 waffleDrop, and metX PD < 70% for same window. […]" (RC) | — |
| m1.1 | "Width of metal1" | 0.140 µm |
| m1.2 | "Spacing of metal1 to metal1" | 0.140 µm |
| m1.3a | "Min. spacing of features attached to or extending from huge_met1 for a distance of up to 0.280 µm to metal1 […]" | 0.280 µm |
| m1.3b | "Min. spacing of huge_met1 to metal1 excluding features checked by m1.3a" | 0.280 µm |
| m1.4 | "Mcon must be enclosed by Met1 by at least …(Rule exempted for cell names documented in rule m1.4a)" (P) | 0.030 µm |
| m1.5 | "Mcon must be enclosed by Met1 on one of two adjacent sides by at least …" (P AL) | 0.060 µm |
| m1.6 | "Min metal 1 area" | 0.083 µm² |
| m1.7 | "Min area of metal1 holes" | 0.140 µm² |
| m1.pd.1 | "Min MM1_oxide_Pattern_density" (RR AL) | 0.7 |
| m1.pd.2a | "Rule m1.pd.1 has to be checked by dividing the chip into square regions of width and length equal to …" (A AL) | 700 µm |
| m1.pd.2b | "Rule m1.pd.1 has to be checked by dividing the chip into steps of …" (A AL) | 70 |
| m1.11–m1.15 | Maximum width after slotting, slotting threshold, maximum pattern density, its window and step, and a contact enclosure, for copper flows (CU; m1.11 also NC) | 4.000 µm, 3.200, 0.77, 50.000 µm, 25.000 µm, 0.030 µm |
| via.4a | "0.150 µm Via must be enclosed by Met1 by at least …" | 0.055 µm |
| via.5a | "0.150 µm Via must be enclosed by Met1 on one of two adjacent sides by at least …" | 0.085 µm |
| nsm.3 | "Min spacing, no overlap, between NSM_keepout to […] metX.dg (X=1 to 5) and cmmX.mk (X=1 to 5). […]" (AL) | 1.000 µm |
| x.1a | "p1m.md (OPC), DECA and AMKOR layers (pi1.dg, pmm.dg, rdl.dg, pi2.dg, ubm.dg, bump.dg) and mask data for p1m, met1, via, met2 must be on a grid of mm" | 0.001 (unit "mm") |
| x.1b | "Data for SKY130 layout and mask on all layers except those mentioned in 1a must be on a grid of mm (except inside Seal ring)" | 0.005 (unit "mm") |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |

Table 2 of *Criteria & Assumptions* repeats the width and space as
`MM1CD` 0.14 and `MM1CDSP` 0.14, and gives the same 0.14 and 0.14 for a
"Metal 1 - Cu" row (`MM1_CuCD`, `MM1_CuCDSP`), a copper back end that
SKY130's aluminium flow does not use.[^pdk-03] Table 4 adds the
"min. etch and fill capability for isolation, licon, and met1" of 0.15
(`DEFC`), the "Oxide Bias for MM1" of 0.6 (`BiasMM1`), a "Metal 1
thickness for antenna ratio calculations (S8D\*)" of 0.35 (`Met1Thick`),
and, among its pattern-density criteria, a "Min pattern density for
oxide" of 0.75 (`OxideMinPD`), a "Min MM\* PD range" of 0.3
(`MMPDrange`), a 700 "Size of small PD extraction box for rough
tolerance (um)" (`SMALLPDBOX`) and a "Maximum metal waffle drop pattern
density in the frame" of 0.55 (`PD_FrameWP`); Table 7 gives a "Huge metal
X min. W and L" of 3 (`HugeM`) and "Large waffle size must be divisible
by 4", 7.2 (`waffle_large`).[^pdk-03] For the plate the decisive figures
are 0.140 µm lines on a 0.28 µm pitch (our arithmetic from m1.1 and
m1.2).

## Related pages

* {ref}`MM1 <step-113>` and {ref}`MM1E <step-114>` — the mask step and
  the metal etch; {ref}`TIAL6 <step-112>` — the stack patterned.
* {ref}`mask-ctm1` — the contact mask whose holes metal 1 covers.
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

* SkyWater PDK, *Masks* page and `masks.csv` — "Metal 1, MM1,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `met1` 68:20,
  the `cmm1` purposes and the `MM1` column of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `MM1CD`/`MM1CDSP`,
  `MM1_CuCD`/`MM1_CuCDSP`, `DEFC`, `BiasMM1`, `Met1Thick`, the
  pattern-density criteria, `HugeM` and `waffle_large`.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `m1` rules, via.4a, via.5a,
  nsm.3, x.1a, x.1b, x.7, x.9, x.15a and the flag legend.[^pdk-periph]
* SkyWater PDK, *Summary of Key Periphery Rules* — Table F4.[^pdk-summary]
* SkyWater PDK, *Parasitic Layout Extraction* — the metal-1 sheet
  resistance.[^pdk-08]
* *S8 / SKY130 Process Steps* sheet — the step, the `MM1` plates of
  MPW-1 to MPW-8, the "Info" note and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `MM1` renders, their
  layers and info text, and the per-die shape counts.[^mask-renders]
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
* Shiraishi et al. (Nikon), *Proc. SPIE* 1992 — off-axis illumination
  for dense lines.[^shiraishi-1992]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor of dense
  and isolated lines.[^wong-1998]
* Cheng and Neureuther, *Proc. SPIE* 2002 — mask CD errors in the
  isolated–dense bias and line-end shortening.[^cheng-2002]
* Samuels, Maurer and Farrell, *Proc. SPIE* 1995 — OPC, mask CD
  tolerance and mask grid size.[^samuels-1995]
* Brunner, *Proc. SPIE* 1991 — the swing ratio and anti-reflective
  coatings.[^brunner-1991]
* Rocke and Schneegans, *JVST B* 1988 — titanium nitride as an
  anti-reflection layer on aluminium.[^rocke-1988]
* Kahng and Samadi, *IEEE TCAD* 2008 — a survey of CMP fill
  synthesis.[^kahng-2008]
* Stine et al., *IEEE TSM* 1998 — pattern density as the dominant
  factor in dielectric polishing.[^stine-1998]
* ITRS 2001, *Lithography* — the optical mask requirements, including
  the mask design grid, for critical layers at 130 nm.[^itrs-03]

## Open questions

* The operation that makes the `cmm1` plate data from `met1` and the
  waffle-drop purpose is not published, nor whether a waffle-drop shape
  places fill or keeps it out.[^pdk-06][^pdk-periph]
* The plate's type (binary with OPC, or phase-shift), tone and CD
  specification, the resist and anti-reflective scheme, and the exposure
  tool are not public; the KrF reading rests on the 0.140 µm rules.
* The renders' fill layer 36:28 is not in `gds_layers.csv`, which gives
  the `cmm1` waffle drop as 62:24, so what the site takes it to be rests
  on the site alone.[^mask-renders][^pdk-06]
* The PDK prints the x.1a and x.1b grids with the unit "mm" and does
  not say why the `met1` mask data need the finer one.[^pdk-periph]
* Whether the absent MPW-5 record is a gap in the record or a difference
  in the run is not stated,[^steps-sheet] and no public source lists the `MM1` plate of the
  original MPW-4 set `5CS8010AC`.[^mask-renders]

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
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* (including Table F2b,
    the mask generation table) and `gds_layers.csv`, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 4
    and 7), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-summary]: SkyWater PDK Authors, *Summary of Key Periphery Rules*
    (Table F4), SkyWater SKY130 PDK documentation, retrieved 2026-09-14.
    <https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_MM1/`
    directory with its page, `job.json`, `result.json` and per-die slot
    JSON files, retrieved 2026-09-14. Rendered from the public shuttle
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
[^shiraishi-1992]: N. Shiraishi, S. Hirukawa, Y. Takeuchi and
    N. Magome, "New imaging technique for 64M-DRAM", *Proc. SPIE*
    **1674**, Optical/Laser Microlithography V, 741 (1992).
    <https://doi.org/10.1117/12.130364>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**,
    Optical Microlithography XI, 106 (1998).
    <https://doi.org/10.1117/12.310718>
[^cheng-2002]: M. Cheng and A. R. Neureuther, "Effects of residual
    aberrations on line-end shortening in 193-nm lithography", *Proc.
    SPIE* **4691**, Optical Microlithography XV, 1421 (2002).
    <https://doi.org/10.1117/12.474526>
[^samuels-1995]: D. J. Samuels, W. Maurer and T. R. Farrell, "Good OPC,
    where will this drive mask CD tolerance and mask grid size", *Proc.
    SPIE* **2621**, 15th Annual BACUS Symposium on Photomask Technology
    and Management, 588–596 (1995). <https://doi.org/10.1117/12.228213>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^rocke-1988]: M. Rocke and M. Schneegans, "Titanium nitride for
    antireflection control and hillock suppression on aluminum silicon
    metallization", *Journal of Vacuum Science & Technology B* **6**(4),
    1113–1115 (1988). <https://doi.org/10.1116/1.584306>
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
