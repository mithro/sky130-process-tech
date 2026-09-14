(mask-nsm)=
# NSM — Nitride Seal Mask

The nitride seal mask is the {term}`reticle` of the one opening in
SKY130's step list that is etched after the last metal and before the
passivation nitride: on the {ref}`NSM <step-165>` page's reading, the
resist printed through it at step 165 is opened in a ring at least 3 µm
wide along the edge of every die, the {ref}`NSME <step-166>` etch cuts
the dielectric there, and the nitride of {ref}`NTSD <step-167>` then
lines the opening. The PDK names the mask and its layer but describes
its function only as "Defines Nitride Seal Mask (FIXME)", so what the
opening is for, and how deep it goes, are readings of the step pages. Its
plate record has one anomaly: the process-steps sheet gives the MPW-6
plate a number different from that of the other seven runs. This page
gathers what public sources say about the mask itself — its PDK entry and
layers, the plates the process-steps sheet records for the MPW runs,
what the public renders of those runs show, the lithography it needs and
the rules that constrain it. How the step is performed is on the step
page; every mask is indexed on the {ref}`masks index <masks-index>`.

| | NSM — Nitride Seal Mask |
|---|---|
| Mask step | {ref}`NSM <step-165>`, step 165 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Nitride Seal Mask", `NSM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cnsm` mask 22:0, "Nitride seal mask"[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `nsm` drawing 61:20, "Nitride seal mask"[^pdk-06] |
| Minimum CD, feature / space | `NSMCD` 3 / `NSMCDSP` 4[^pdk-03] |
| Polarity and tone | Not published; the PDK's `cnsm.nikon` checks name a polarity but not the plate's tone. On the step page's reading the resist is opened where `nsm` is drawn, which with a positive resist would make the plate dark-field with a clear ring (inference). |
| Exposure class | i-line, an inference on the step page from the 3 µm and 4 µm rules; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `007`; MPW-6: `616`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 39, 40, 40, 40, 40, 40, 40, 40[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-nsm-steps>` |

## What the mask defines

The PDK names the mask three times — "Nitride Seal Mask, NSM" in
`masks.csv`, "Nitride seal mask" for both `cnsm` and `nsm` in
`gds_layers.csv`, and the function line of the `nsm` rule set, "Defines
Nitride Seal Mask (FIXME)" — and describes it nowhere.[^pdk-05][^pdk-06][^pdk-periph]
The rules place the layer. Its minimum width is 3.000 µm (nsm.1) and
spacing 4.000 µm (nsm.2); an `NSM_keepout`, which Table C3 of the
*Layers Reference* defines as "nsm.dg OR nsm.mk", must be 1.000 µm from
diffusion, tap, poly, local interconnect, metals 1 to 5 and their mask
layers, with cells named "nikon\*" and the "diff ring inside
areaid.sl" exempted (nsm.3); and the same device and wiring layers must
be enclosed by the frame boundary `areaid.ft` by 3.000 µm and kept
3.000 µm from the die area `areaid.dt` (nsm.3a,
nsm.3b).[^pdk-periph][^pdk-06] Table 7 of *Criteria & Assumptions* gives
the two keep-outs as criteria, "Keepout of active, poly, li and metal to
NSM (TCS-2253)" of 1 (`NSMKeepout`) and "3 um keepout of active, poly, li
and metal to areaid.dt/areaid.ft (TCS-2253)" of 3 (`NSMKeepout_3um`), in
its column headed "space".[^pdk-03] Table C4b describes `areaid.dt` as
"Location of the die within the frame used in frame builder generation to
create blanking for die and other drop-ins. Also used in cldrc/drc for
rules in frame to die edge (waffles, nsm, metals etc)".[^pdk-06]

The {ref}`NSM <step-165>` page reads the published seal-ring cell
`advSeal_6um_gen` of Efabless's caravel repository, which draws a 6 µm
`areaid.sl` band and inside it a 5 µm `nsm` band over four 0.3 µm
diffusion rings, with no poly, local interconnect or metal
rings.[^caravel-sealring] From the rules and that layout it reads `NSM`
as a continuous ring-shaped opening along the die edge, in a band whose
only drawn device layer is the seal ring's diffusion, and the purpose of
the opening as a path for the passivation nitride to seal the edge of
the dielectric stack; the {ref}`NSME <step-166>` page describes a deep
etch towards the seal ring's silicon and a stop on the local-interconnect
nitride as two readings, and leaves the depth open (inferences on those
pages). The step pages compare the construction with a GlobalFoundries
patent on chip edge seals etched through the dielectrics, a Siemens and
IBM patent on crack stops in the dicing channel and a Zeevo seal-ring
patent that shows a moisture path through a passivation
oxide;[^pat-edgeseal-gf][^pat-crackstop-ibm][^pat-sealring-zeevo]
Comizzoli et al. reviewed the corrosion of electronic materials and
devices,[^comizzoli-1986] and Peck gave a model for correlating
humidity tests.[^peck-1986] Gambino et al. name the edge seal ring as
one source of noise coupling between RF devices and propose a segmented
guard ring, which they demonstrate "is reliable for a 0.18 μm RF
technology".[^gambino-2014]

The PDK's general rules add what a seal ring is allowed to be: `areaid.sl`
"must not overlap tap, poly, li1 and metX" (x.23c), and "areaid:sl must
not overlap li1 and metX for pcell "advSeal_6um"" (x.23e); the
""advSeal_6um" pcell must overlap diff" (x.26); and "Lower left corner of
the seal ring should be at origin i.e (0,0)" (x.19).[^pdk-periph] Table
F2b, the mask generation table, has no `NSM` column, and Table F4 of the
*Summary of Key Periphery Rules* no `nsm` row, so the PDK ties the mask to
no device.[^pdk-06][^pdk-summary] The mask does not define the films it
opens ({ref}`NFUSOX <step-164>` and, on the deep reading, the inter-level
dielectrics beneath), the nitride that lines the opening
({ref}`NTSD <step-167>`) or the pad openings cut after it
({ref}`PDM <step-168>`, {ref}`mask-pdm`).

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` has one mask-level layer for this mask, `cnsm` with
purpose `mask` at 22:0 ("Nitride seal mask"), and no `drawing`, `mask
add`, `mask drop` or `waffle drop` purpose; layer number 22 also carries
the `cfom` drawing, mask add, mask drop and waffle drop purposes and the
`fom` dummy purpose ({ref}`masks-index`). The drawn layer is `nsm` at
61:20.[^pdk-06] The pairing rests on the identical descriptions, as on the
{ref}`masks index <masks-index>`, and the PDK publishes no operation that
turns `nsm` into the plate. Rule x.15a confines "Drawn compatible, mask,
and waffle-drop layers" to test modules, the space "inside areaid:sl
(i.e., between the outer and inner areaid:sl edges, but not in the die)"
and the frame (flag P),[^pdk-periph] so `cnsm` shapes may sit in the seal
ring itself, and a design draws `nsm` (our reading of x.15a); with no add
or drop purpose, rule x.9's "serifs" have no `cnsm` layer to sit on; the
first x.9 row exempts the seal-ring cell's `cfom` mask-drop shapes and
0.3 µm die-edge diffusion rings, the rings the caravel cell draws under
its `nsm` band (our reading).

The PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance criteria
for GDS data", repeats nsm.1 and nsm.2 ("3 min. width of nsm", "4 min.
spacing/notch of nsm") and expands nsm.3 into a pair of checks per layer,
for example "1 min. spacing of met5_not_NSM3_exempt & nsm OR NSMmk" and
"met5_not_NSM3_exempt must not overlap nsm OR NSMmk", and nsm.3a and nsm.3b
into checks against "frameBndr" and "dieCut".[^pdk-errors] It also checks
"2 min. spacing of moduleCutAREA & q0nsmnotBuildSpace" (x.12a), "nsm
drawn layer cannot straddle areaid:ModuleCut" (scribe.7) and "6 min.
width of SEALID" (x.28, which the periphery rules give as "N/A"), and it
names a mask-data layer `NSMmk` in the grid, octagonal-edge and x.15a
checks and in two checks named `cnsm.nikon`, "NSMmk in the nikon cross
has the wrong polarity" and "NSMmk is missing from the nikon cross in the
layout".[^pdk-errors][^pdk-periph] The page does not say what the "nikon
cross" is. In the caravel seal-ring cell a sub-cell named
`nikon_sealring_shape`, placed in each corner, draws inside a 4 µm square
a cross of three rectangles, 2.4 µm across with 0.5 µm arms, on `cnsm`
22:0 and 23 other mask-level layers, and the square, with its corners
cut at 45°, less the cross on seven more, among them `cpdm` 37:0 (our reading of the GDS
file).[^caravel-sealring] We read that sub-cell as a "nikon cross" of the
kind the checks name (inference from the names); the exemption of cells
named "nikon\*" in nsm.3 fits that reading. None of this states the tone
of the plate ({ref}`mask-mm5`).

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `NSM` the site renders layer 61:20 (`nsm`)
alone, with no Boolean expression, no fill layer, no info text and no
note, on all eight runs; its mask record gives the mask-level layer
22:0.[^mask-renders] The layer is the one this reference pairs with the
mask; both choices derive from the same public files, so the agreement is
no independent confirmation, and the site's choice is one public
derivation from the drawn data, not SkyWater's mask-generation recipe
({ref}`masks-derivations`). The sheet's "Run Mask IDs" row for `NSM` has
no "Info" note.[^steps-sheet]

The die count is not a count of designs. On MPW-1, 39 dies carry `nsm`
shapes and one (frame D4) carries none; on the other seven runs all 40
do. Every die that carries any carries exactly 36
shapes.[^mask-renders] We read the 36 shapes as a layout common to the
dies rather than to the projects (inference), as the
{ref}`DNM mask page <mask-dnm>` reads its repeated counts; the site does
not say what they are. The number equals our count of polygons on
`nsm` 61:20 in the caravel seal-ring cell, nine in each of its four
corner sub-cells,[^caravel-sealring] which fits, but does not show, a
seal ring common to the dies (our comparison). The `nikon_sealring_shape`
crosses sit on 22:0, which the site does not render. The site states the
limits of its images: "These are renders of *drawn* data, not photomask
artwork: reticle pitch, 4x reduction, mirroring and the frame features
the fab adds are not modelled."[^mask-renders] The frame outside the
dies, where nsm.3a and nsm.3b act, is therefore not shown. Its metadata
carries no plate ID, so a render is tied to a plate in the sheet only by
the acronym `NSM`, and the MPW-4 renders come from a different reticle set
from the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `NSM` plate as
existing on all eight MPW runs, with the plate number `007` on seven of
them and `616` on MPW-6.[^steps-sheet] The plate IDs below are the
sheet's; the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA007A` |
| MPW-2 | `5CS8007AC` | `S8007AA007A` |
| MPW-3 | `5CS8008AC` | `S8008AA007A` |
| MPW-4 | `5CS8018AC` | `S8018AA007A` |
| MPW-5 | `5CS8011AC` | `S8011AA007A` |
| MPW-6 | `5CS8014AC` | `S8014AA616A` |
| MPW-7 | `5CS8016AC` | `S8016AA007A` |
| MPW-8 | `5CS8017AC` | `S8017AA007A` |

* **MPW-6.** The MPW-6 plate ID is `S8014AA616A`, where every other run
  has `007`; the sheet does not explain the difference. `616` is higher
  than any other plate number in the tab and `007` lower, and no other
  mask has more than one number ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
  The MPW-6 renders show the same 36 `nsm` shapes on all 40 dies as the
  other runs do,[^mask-renders] but they show the drawn layouts, not the
  plate.
* **Plate number.** The sheet does not say what `007` or `616` encodes.
  `NSM` (step 165) is `007`, below `NWM` (step 17) `010` and `FOM` (step
  4) `020`, so the numbers do not follow process order, and no process
  position is read from them
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type.** The sheet's "Sheet4" tab gives no type for
  `NSM`.[^steps-sheet] 4× is the ITRS 2001 mask magnification for the
  130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`NSM <step-165>` page gives
{math}`k_1 = 3 \times 0.6 / 0.365 \approx 4.9` on an i-line tool with an
assumed NA of 0.6, "far above any resolution limit", and infers an i-line
exposure, quoting ASML's statement that older systems "migrate to the
lithography of choice for less critical layers";[^asml-30] the
{ref}`i-line stepper <machine-i-line-stepper>` page lists it there.
SkyWater lists "ASML I-line stepper" and "ASML I-line scanner" but
assigns no layer to them.[^skw-01]

**The plate.** Wong et al. found that the mask error factor "is unity for
large features, but increases rapidly when the critical dimension (CD) is
less than 0.5 (lambda) /NA for line-space patterns";[^wong-1998] at
365 nm and NA 0.6 that is about 0.30 µm (our arithmetic), a tenth of the
3 µm ring, so plate CD errors would print at their own size (inference).
At 4× a 3 µm ring is 12 µm wide on the plate (our arithmetic), a feature
within reach of the laser writers and wet-etched chrome that the CAPM
and VIM4 mask pages discuss: a laser writer of the ALTA family addressed
"the needs of maskmakers in the 180 nm and 150 nm technology
nodes",[^morgante-2000] and chrome masks "have traditionally been wet
etched".[^buck-1994] On the {ref}`NSME <step-166>` page's estimate the
ring is about 0.5 % of a die, so on the dark-field reading the plate is
almost entirely chrome (inference). Hochmuth, Ruhl and Coleman found that
with chrome dry etch "the deviation of the CD from the target value is a
function of the chrome loading on the plate";[^hochmuth-1999] whether
that applies to this plate is not public.

**Resist.** The {ref}`NSM <step-165>` page reads a positive DNQ/novolac
i-line resist, the chemistry of Dammel's text,[^dammel-1993] thick enough
to cover the 1.26 µm metal-5 steps[^pdk-04] and to survive a dielectric
etch that may be several micrometres deep, and cites a TSMC patent on
etching fuse windows through a passivation and several inter-metal
dielectrics.[^pat-fusewin-tsmc] The resist is coated over the thin
{ref}`NFUSOX <step-164>` oxide and the full metal-5 topography, so coating
uniformity and swing effects over topography matter (the step page's
reading). SkyWater's resist is not public; the consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Pattern transfer.** On the step pages' readings the resist pattern is
transferred by {ref}`NSME <step-166>`, a fluorocarbon dielectric etch of
unknown depth on the
{ref}`dielectric plasma etcher <machine-plasma-etcher-dielectric>` class,
with the resist strip and clean treated as part of that step. The open
area is small, which the NSME page reads as making optical-emission
endpoint weak; Wodecki describes endpoint detection on low-open-area
dielectric etches.[^wodecki-1999]

**Overlay.** The 1.000 µm keep-out of nsm.3 is, on the
{ref}`NSM <step-165>` page's reading, the alignment budget, and it reads
the alignment as to the metal-5 or earlier frame marks; the PDK does not
say what the keep-out allows for.[^pdk-periph]

(mask-nsm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `NSM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`NSM <step-165>`, {ref}`NSME <step-166>`

* {ref}`NSM <step-165>` — coats, exposes and develops the resist.
* {ref}`NSME <step-166>` — etches the ring opening through the resist;
  the step list used in this reference has no separate strip step, and
  the step page treats the resist strip and post-etch clean as part of
  the etch.

On its step page's reading, the next step, {ref}`NTSD <step-167>`,
deposits the passivation nitride over the whole wafer and into the ring
opening after the resist is gone. The next mask step is
{ref}`PDM <step-168>`. The rule needs no exception for this mask.

## Design rules and critical dimensions

The `nsm` rules of the periphery rules and the general rules on the seal
ring and on mask data. Flag AL means "Rules applicable only to Al BE
flows", P "Rule applies to periphery only (outside areaid.ce). A
corresponding core rule may or may not exist." and NC "Rule not checked by
DRC. It should be used as a guideline only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| nsm.1 | "Min. width of nsm" | 3.000 µm |
| nsm.2 | "Min. spacing of nsm to nsm" | 4.000 µm |
| nsm.3 | "Min spacing, no overlap, between NSM_keepout to diff.dg, tap.dg, fom.dy, cfom.dg, cfom.mk, poly.dg, p1m.mk, li1.dg, cli1m.mk, metX.dg (X=1 to 5) and cmmX.mk (X=1 to 5). Exempt the following from the check: (a) cell name "nikon\*" and (b) diff ring inside areaid.sl" (AL) | 1.000 µm |
| nsm.3a | "Min enclosure of diff.dg, tap.dg, fom.dy, cfom.dg, cfom.mk, poly.dg, p1m.mk, li1.dg, cli1m.mk, metX.dg (X=1 to 5) and cmmX.mk (X=1 to 5) by areaid.ft. Exempt the following from the check: (a) cell name "s8Fab_crntic\*"  (b)  blankings in the frame (rule uses areaid.dt for exemption)" | 3.000 µm |
| nsm.3b | "Min spacing between areaid.dt to diff.dg, tap.dg, fom.dy, cfom.dg, cfom.mk, poly.dg, p1m.mk, li1.dg, cli1m.mk, metX.dg (X=1 to 5) and cmmX.mk (X=1 to 5). Exempt the following from the check: (a) blankings in the frame (rule uses areaid.dt for exemption)" | 3.000 µm |
| x.1b | "Data for SKY130 layout and mask on all layers except those mentioned in 1a must be on a grid of mm (except inside Seal ring)" | 0.005 (unit "mm") |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.9 (first row) | "Shapes on maskAdd or maskDrop layers ("serifs") are allowed in core only. Exempted are: […] cfom md/mp inside "advSeal_6um\* OR cuPillarAdvSeal_6um\*" pcell […] diff rings around the die at min total L>1000 um and W=0.3 um, and PMM/PDMM inside areaid:sl" | — |
| x.9 (second row) | "Shapes on maskAdd or maskDrop layers ("serifs") are allowed in core only. PMM/PDMM inside areaid:sl are excluded." | N/A |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), or inside areaid:sl (i.e., between the outer and inner areaid:sl edges, but not in the die) or inside areaid:ft (i.e., frame, blankings). Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
| x.19 | "Lower left corner of the seal ring should be at origin i.e (0,0)" | — |
| x.23c | "areaid.sl must not overlap tap, poly, li1 and metX" | — |
| x.23e | "areaid:sl must not overlap li1 and metX for pcell "advSeal_6um"" | N/A |
| x.26 | ""advSeal_6um" pcell must overlap diff" | — |
| x.28 | "Min width of areaid.sl" | N/A |

Table 2 of *Criteria & Assumptions* repeats the width and space as
`NSMCD` 3 and `NSMCDSP` 4, and Table 7 gives `NSMKeepout` 1 and
`NSMKeepout_3um` 3, in its column headed "space", and a "Minimum scribe
width" of 50 (`scribew`) in its column headed "CD"; Table 4's "Minimum
Space and Overlap" block, headed "Value (um)", gives a "Bowing of
rectangular contact (per edge) -- seal ring sizing" of 0.015
(`TBOWINGSEAL`).[^pdk-03] The Error Messages page gives the seal-ring
identifier a width of 6 (x.28), where the periphery rules print
"N/A".[^pdk-errors][^pdk-periph] For the plate the decisive figures are a
3.000 µm minimum ring on 4.000 µm spaces, a 7 µm pitch (our arithmetic
from nsm.1 and nsm.2), kept 1.000 µm from all wiring.

## Related pages

* {ref}`NSM <step-165>` and {ref}`NSME <step-166>` — the mask step and
  the ring etch; {ref}`NFUSOX <step-164>` — the oxide it is printed on;
  {ref}`NTSD <step-167>` — the nitride that lines the opening.
* {ref}`mask-mm5` — the metal mask printed before it, whose `cmm5.nikon`
  checks match this mask's; {ref}`mask-pdm` — the pad mask printed after
  the nitride; {ref}`mask-dnm` — the repeated-count reading of the
  renders.
* {ref}`masks-index` — every mask's PDK entry, plates and renders, and the
  plate-number anomaly of MPW-6.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-plasma-etcher-dielectric` — the etch class that
  transfers the pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography` and {ref}`category-etch` — the mask step
  and etch categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "Nitride Seal Mask, NSM,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `nsm` 61:20,
  `cnsm` 22:0, Table C3's `NSM_keepout`, Table C4b's `areaid.dt` and the
  columns of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `NSMCD`/`NSMCDSP`,
  `NSMKeepout`, `NSMKeepout_3um`, `scribew` and `TBOWINGSEAL`.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `nsm` rules and function line,
  x.1b, x.7, x.9, x.15a, x.19, x.23c, x.23e, x.26, x.28 and the flag
  legend.[^pdk-periph]
* SkyWater PDK, *Error Messages* page — the `nsm`, seal-ring, scribe and
  `cnsm.nikon` checks.[^pdk-errors]
* SkyWater PDK, *Summary of Key Periphery Rules* — Table F4.[^pdk-summary]
* SkyWater PDK, *Process stack diagram* — the metal-5 topography.[^pdk-04]
* Efabless, caravel `advSeal_6um_gen` seal-ring GDS — the `nsm` band, its
  polygons and the `nikon_sealring_shape` sub-cell.[^caravel-sealring]
* *S8 / SKY130 Process Steps* sheet — the step, the `NSM` plates of MPW-1
  to MPW-8 and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `NSM` renders, their layer
  and the per-die shape counts.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the i-line exposure
  tools.[^skw-01]
* ASML, *Three decades of PAS 5500* — older exposure tools moving to less
  critical layers.[^asml-30]

### High-level understanding

* Wikipedia, *Photomask* — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wikipedia, *Photolithography* — i-line exposure.[^wiki-litho]
* Mack, *Fundamental Principles of Optical Lithography* — coating over
  topography and swing curves.[^mack-2007]
* Levinson, *Principles of Lithography* — chapters on masks and reticles
  and on overlay.[^levinson-2005]

### Deep dive

* Gambino et al., IITC 2014 — the reliability of a segmented edge
  seal ring in a 0.18 µm RF technology.[^gambino-2014]
* Stamper, McGahay and He (GlobalFoundries), US 10,062,748 — segmented
  guard rings and chip edge seals.[^pat-edgeseal-gf]
* Mitwalsky and Chen (Siemens and IBM), US 5,789,302 — crack
  stops.[^pat-crackstop-ibm]
* Bothra, McKay and Jhota (Zeevo), US 6,492,716 — a seal-ring structure
  for mixed-signal ICs.[^pat-sealring-zeevo]
* Ying and Hung (TSMC), US 6,300,252 — etching fuse windows through the
  back-end dielectrics.[^pat-fusewin-tsmc]
* Comizzoli et al., *Science* 1986 — corrosion of electronic materials and
  devices.[^comizzoli-1986]
* Peck, IRPS 1986 — a model for humidity-test correlation.[^peck-1986]
* Wodecki, *Proc. SPIE* 1999 — endpoint detection at low open
  area.[^wodecki-1999]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  feature size above which it is unity.[^wong-1998]
* Hochmuth, Ruhl and Coleman, *Proc. SPIE* 1999 — plate CD against chrome
  loading.[^hochmuth-1999]
* Morgante and Hamaker, *Proc. SPIE* 2000 — a laser reticle writer and the
  mask nodes it served.[^morgante-2000]
* Buck and Grenon, *Proc. SPIE* 1994 — wet against dry chrome etching of
  masks.[^buck-1994]
* Dammel, *Diazonaphthoquinone-based Resists* — the i-line resist
  chemistry.[^dammel-1993]

## Open questions

* The PDK names `nsm` but does not describe it ("FIXME" in the rule
  table); the reading of the opening as a die-edge path for the
  passivation nitride, and its depth, are inferences of the step
  pages.[^pdk-periph]
* Why the MPW-6 plate is numbered `616` where the other seven runs have
  `007`, and what either number encodes, is not stated.[^steps-sheet]
* The PDK does not describe the "nikon cross"; reading the caravel
  seal-ring sub-cell as that cross, and the 36 `nsm` shapes of the renders
  as a seal ring common to the dies, are
  inferences.[^pdk-errors][^caravel-sealring][^mask-renders]
* The renders do not show the frame, so what the plates carry outside the
  dies, where nsm.3a and nsm.3b act, is not public; MPW-1 frame D4 draws
  no `nsm`.[^mask-renders]
* The exposure tool, the plate's type, tone and CD specification, and the
  resist and its thickness are not public; no public source lists the
  `NSM` plate of the original MPW-4 set `5CS8010AC`.[^mask-renders]

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
    (Table F4), SkyWater SKY130 PDK documentation, retrieved 2026-09-14.
    <https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^caravel-sealring]: Efabless Corporation, *caravel* repository,
    `gds/advSeal_6um_gen.gds.gz` (seal-ring cell for SKY130 shuttle
    designs), retrieved 2026-09-14.
    <https://github.com/efabless/caravel/blob/main/gds/advSeal_6um_gen.gds.gz>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_NSM/`
    directory with its page, `job.json` and per-die slot JSON files,
    retrieved 2026-09-14. Rendered from the public shuttle repositories
    under <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
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
[^gambino-2014]: J. P. Gambino, R. S. Graf, J. C. Malinowski, A. R. Cote,
    W. H. Guthrie, K. M. Watson, P. F. Chapman, K. K. Sims, M. D. Levy,
    T. Aoki, G. A. Mason and M. D. Jaffe, "Reliability of segmented edge
    seal ring for RF devices", *2014 IEEE International Interconnect
    Technology Conference / Advanced Metallization Conference (IITC/AMC)*,
    pp. 367–370. <https://doi.org/10.1109/IITC.2014.6831836>
[^pat-edgeseal-gf]: A. K. Stamper, V. J. McGahay and Z.-X. He
    (GlobalFoundries), *Segmented guard-ring and chip edge seals*,
    US 10,062,748 B1, filed 2017-02-27, granted 2018-08-28.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10062748>
[^pat-crackstop-ibm]: A. R. Mitwalsky and T.-C. Chen (Siemens
    Aktiengesellschaft / International Business Machines), *Crack stops*,
    US 5,789,302 A, filed 1997-03-24, granted 1998-08-04.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5789302>
[^pat-sealring-zeevo]: S. Bothra, T. G. McKay and R. Jhota (Zeevo),
    *Seal ring structure for IC containing integrated digital/RF/analog
    circuits and functions*, US 6,492,716 B1, filed 2001-04-30, granted
    2002-12-10.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6492716>
[^pat-fusewin-tsmc]: S. Ying and S.-C. Hung (Taiwan Semiconductor
    Manufacturing Co.), *Method for etching fuse windows in IC devices
    and devices made*, US 6,300,252 B1, filed 1999-10-01, granted
    2001-10-09.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6300252>
[^comizzoli-1986]: R. B. Comizzoli, R. P. Frankenthal, P. C. Milner and
    J. D. Sinclair, "Corrosion of Electronic Materials and Devices",
    *Science* **234**(4774), 340–345 (1986).
    <https://doi.org/10.1126/science.234.4774.340>
[^peck-1986]: D. S. Peck, "Comprehensive Model for Humidity Testing
    Correlation", *24th International Reliability Physics Symposium*
    (1986), pp. 44–50. <https://doi.org/10.1109/IRPS.1986.362110>
[^wodecki-1999]: N. Wodecki, "Low open area multilayered dielectric
    film etch endpoint detection using EndPoint Plus", *Proc. SPIE*
    **3882**, Process, Equipment, and Materials Control in Integrated
    Circuit Manufacturing V, 231 (1999).
    <https://doi.org/10.1117/12.361313>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**,
    Optical Microlithography XI, 106 (1998).
    <https://doi.org/10.1117/12.310718>
[^hochmuth-1999]: J. Hochmuth, G. G. Ruhl and T. P. Coleman, "Control
    methodology of off-target for varying pattern densities with chrome
    dry etch", *Proc. SPIE* **3873**, 19th Annual Symposium on Photomask
    Technology, 297 (1999). <https://doi.org/10.1117/12.373324>
[^morgante-2000]: C. G. Morgante and H. C. Hamaker, "ALTA 3700:
    extending the application space of the ALTA 3500 laser reticle
    writer", *Proc. SPIE* **4066**, 613 (2000).
    <https://doi.org/10.1117/12.392079>
[^buck-1994]: P. D. Buck and B. J. Grenon, "Comparison of wet and dry
    chrome etching with the CORE-2564", *Proc. SPIE* **2087**, 42–49
    (1994). <https://doi.org/10.1117/12.167247>
[^dammel-1993]: R. R. Dammel, *Diazonaphthoquinone-based Resists*, SPIE
    Tutorial Texts TT11, SPIE Press, 1993.
    <https://doi.org/10.1117/3.2265072>
