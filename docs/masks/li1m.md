(mask-li1m)=
# LI1M — Local Intrcnct 1

The local-interconnect mask is the {term}`reticle` that draws SKY130's
lowest wiring level, the {term}`local interconnect` (titanium nitride on
the {ref}`LITIN <step-101>` page's reading) that joins transistors, taps
and poly below metal 1. On the
{ref}`LI1M <step-102>` page's reading, the resist printed through it at
step 102 stays wherever `li1` is drawn and protects the TiN that the
{ref}`LI1ME <step-103>` etch leaves standing as lines and pads.

| | LI1M — Local Intrcnct 1 |
|---|---|
| Mask step | {ref}`LI1M <step-102>`, step 102 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Local Intrcnct 1", `LI1M`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cli1m` mask 56:0, "Local interconnect mask"; drawing 115:44, mask add 115:43, mask drop 115:42[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `li1` drawing 67:20, "Local interconnect"[^pdk-06] |
| Minimum CD, feature / space | `LI1MCD` 0.17 / `LI1MCDSP` 0.17; "Core" 0.14 / 0.14[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist remains where `li1` is drawn, which with a positive resist would make the plate clear-field (inference). |
| Exposure class | KrF (248 nm) with OPC, an inference on the step page from the 0.17 µm and 0.14 µm rules and the PDK's proximity-correction criterion; no public source names the tool ({ref}`machine-duv-krf-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `370`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-li1m-steps>` |

:::{seealso}
How the step is performed is on the step
page; every mask is indexed on the {ref}`masks index <masks-index>`.
:::

## What the mask defines

The mask prints
lines rather than holes, at the same 0.17 µm as the contacts beneath it
and at 0.14 µm in one family of cells, and the PDK publishes a "Li1
proximity correction" criterion for it.

The periphery rules give the function of the `li` rule set as "Defines
local interconnect to diff/tap and poly".[^pdk-periph] The PDK's Table
F4, "Connectivity of Drawn and Mask Layers", shows the level in the
middle of the contact stack: `li1` reaches diff and tap through "Licon1"
and poly through "Licon1 AND Npc", and metal 1 reaches `li1` through
"Mcon".[^pdk-summary] The mask therefore carries three kinds of shape:[^pdk-periph]

* lines that wire devices together inside a cell
* pads that cover the
  contacts below ({ref}`mask-licm1`) and receive the contacts above
* LI resistor bodies, at least 0.290 µm wide (li.7)

In the
TiN local-interconnect process of Tang et al., "the 0.1-µm-thick TiN
layer is patterned and etched to provide local connections between
polysilicon gates and n+ and p+ junctions".[^tang-1987] The PDK's stack
diagram gives SKY130's `li` as 0.10 µm thick.[^pdk-04]

The PDK's mask generation table, Table F2b, marks the `LI1M` column `C`
("CREATED") in three of its 80 device rows: the LI resistor and the two
VPP capacitor rows ("VPP" and "VPP (with met3 shield)").[^pdk-06] It marks `+`, "Layer
allowed to overlap", in 75, and `-`, "Layer not created for the device",
only for the two metal fuses.[^pdk-06]

The narrowest `li` rules belong to
one of those devices: li.1a and li.3a allow 0.140 µm width and space
"inside of cells with name s8rf2_xcmvpp_hd5_\*", against 0.170 µm
elsewhere (li.1, li.3).[^pdk-periph] We read the cell name as a VPP
capacitor cell and Table 2's 0.14 "Core" row as those cells' values
(inference from the matching numbers; the PDK does not link them).

The mask does not define the TiN film it patterns, which
{ref}`LITIN <step-101>` deposits, nor the nitride cap that
{ref}`LINIT <step-104>` lays over the etched lines, on the step pages'
readings. The contacts it covers and the contacts that land on it are
the {ref}`LICM1 <step-093>` and {ref}`CTM1 <step-107>` masks.

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives the mask-level layer `cli1m` four purposes:
`mask` at 56:0 ("Local interconnect mask"), and `drawing` 115:44,
`mask add` 115:43 and `mask drop` 115:42 on a different layer number,
the last three without a description.[^pdk-06] The drawn layer is `li1` at 67:20,
"Local interconnect".[^pdk-06] The pairing rests on those names and
descriptions, as on the {ref}`masks index <masks-index>`, and the PDK
publishes no operation from `li1` to the plate.

Rule x.9 reads "Shapes on
maskAdd or maskDrop layers ("serifs") are allowed in core only", with the
exemptions it lists.[^pdk-periph] Rule x.15a confines "Drawn compatible, mask, and
waffle-drop layers" to test modules, seal ring and frame, with the
exception that "FOM/P1M/Metal waffle drop are allowed inside the die"
(flag P, periphery only).[^pdk-periph] A design inside the die therefore
draws `li1` (our reading of x.9 and x.15a).

The `nsm` rules name the
mask-level shapes directly: nsm.3 sets 1.000 µm between the nitride-seal
keep-out and a list of drawn and mask layers that includes "li1.dg" and
"cli1m.mk".[^pdk-periph] We read ".mk" as the mask purpose; the PDK does
not expand it.

Two criteria tie the plate to a correction of the drawn data. Table 7 of
*Criteria & Assumptions*, "Other criteria and parameters", has a row
"LI1CD add/drop" with 0.01 in its CD column and 0.04 in its space
column, and no variable name, and a row "Li1 proximity correction" with
0.25 in its space column (`LI1PROXSpace`).[^pdk-03] The
{ref}`LI1M <step-102>` page reads the second as public evidence that the
`cli1m` data carry an {term}`OPC` applied to lines closer than 0.25 µm,
and the {ref}`LI1ME <step-103>` page reads the first as the mask sizing
that compensates the {term}`etch bias`; the PDK says neither.

The
`LI1M` data are not among those rule x.1a names for the 0.001 grid
("mask data for p1m, met1, via, met2"), so they fall under x.1b's 0.005
(our reading; both values are printed with the unit "mm").[^pdk-periph]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `LI1M` the site renders layer 67:20 (`li1`)
together with 56:28, which it lists as a fill layer, with no Boolean
expression and no note, on all eight runs.[^mask-renders] Its mask record gives the
mask-level layer 56:0 and the info text "LI (Metal 0)".[^mask-renders]

Layer 56:28 is not in `gds_layers.csv`,[^pdk-06] although it shares its
layer number with the `cli1m` mask purpose 56:0 (our observation), so
the site's choice of it is one public reading of the tape-out files,
not a PDK definition. Like the site's other layer choices, it is not
SkyWater's mask-generation recipe ({ref}`masks-derivations`).

The info
text is identical to the "Info" note of the `LI1M` row in the
process-steps sheet, one of the level names the two sources share, so
neither is cited as corroborating the other
({ref}`masks-renders-sheet-notes`).[^steps-sheet][^mask-renders]

Every rendered die of every run carries shapes on these layers — at
least 3 562 112 on each die, fill included[^mask-renders] — so the count
of 40 dies says only that every layout has local interconnect.

The site
states the limits of its images: "These are renders of *drawn* data, not
photomask artwork: reticle pitch, 4x reduction, mirroring and the frame
features the fab adds are not modelled."[^mask-renders] They therefore
show the drawn lines, not the add/drop sizing or proximity correction the
PDK's criteria imply (inference from that statement). The metadata
carries no plate ID, so a render is tied to a plate in the process-steps
sheet only by the acronym `LI1M`, and the MPW-4 renders come from a
different reticle set from the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `LI1M` plate
as existing on all eight MPW runs, with the plate number `370` on
each.[^steps-sheet] The plate IDs below are the sheet's; the reticle
set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA370A` |
| MPW-2 | `5CS8007AC` | `S8007AA370A` |
| MPW-3 | `5CS8008AC` | `S8008AA370A` |
| MPW-4 | `5CS8018AC` | `S8018AA370A` |
| MPW-5 | `5CS8011AC` | `S8011AA370A` |
| MPW-6 | `5CS8014AC` | `S8014AA370A` |
| MPW-7 | `5CS8016AC` | `S8016AA370A` |
| MPW-8 | `5CS8017AC` | `S8017AA370A` |

* **Plate number.** The sheet does not say what `370` encodes. Its
  neighbours in the tab are `317` for `HVTPM` (step 22) and `400` for
  `CTM1` (step 107), so the numbers do not follow process order, and no
  process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type.** The sheet's "Sheet4" tab gives no type for
  `LI1M`.[^steps-sheet] Whether the plate is binary, with or without
  proximity correction, is not on public record. 4× is the ITRS 2001
  mask magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

### Exposure class

The {ref}`LI1M <step-102>` page puts 0.17 µm lines
and spaces at {math}`k_1 \approx 0.28` on an i-line tool of NA 0.6,
which it excludes, and at {math}`k_1 \approx 0.41–0.48` on a KrF lens of
NA 0.6–0.7, "workable for lines with OPC and, for the 0.14 µm cells,
off-axis illumination", and infers a 248 nm level. The
{ref}`KrF stepper <machine-duv-krf-stepper>` page lists it there.

ITRS
2001 lists "248 nm + PSM" and "193 nm" as the exposure options for the
130 nm node, and says that "only 248 nm lithography has a mature
infrastructure".[^itrs-03] ASML's PAS 5500/750E "achieves 130 nm
resolution while using standard 248 nm light".[^asml-750e] SkyWater
lists "ASML DUV stepper" and "ASML DUV scanner" but assigns no layer to
them.[^skw-01]

### Mask errors

Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns".[^wong-1998] Wong et al. found that
"dense lines and spaces exhibit markedly higher MEF values than isolated
features".[^wong-1998] At 248 nm and NA 0.7 the threshold is about
0.18 µm (our arithmetic), just above the 0.17 µm lines and further above
the 0.14 µm lines of li.1a, so plate CD errors on the dense parts of this
mask would print magnified (inference).

Arthur and Martin carried the
mask error factor, with pitch, OPC and focus, through process windows
and CD budgets to "the impact on reticle procurement
specifications".[^arthur-1999] ITRS 2001's optical mask requirements,
which are "for critical layers", ask in 2001 for a mask CD uniformity of
10.4 nm (3σ) on dense lines and 7.4 nm on isolated MPU gate lines on a
binary mask, at 4× magnification.[^itrs-03] How tightly SkyWater
specifies the `LI1M` plate is not public.

### Proximity and line ends

The PDK's 0.25 "Li1 proximity correction"
space[^pdk-03] fits a correction that treats lines closer than 0.25 µm
differently from wider-spaced ones (the step page's reading). Otto et al.
describe such a rules-based correction, whose "edge rules and corner
rules" bias feature edges and add sub-resolution assist
features.[^otto-1994] Rieger and Stirniman generate behaviour models
that serve as the correction rules.[^rieger-1994] Cobb and Zakhor
made aerial-image calculation fast for the mask perturbations OPC
produces.[^cobb-1995]

Shi et al. showed that the "forbidden pitch" lies
where the fields of neighbouring features interfere destructively with
the main feature's, which illumination design can suppress, with
scattering bars placed for best performance.[^shi-2002]

Line ends matter on a wiring level:
Garofalo et al. found that line-end shortening "reduces the wafer process
latitude and in some cases even eliminates the level-to-level overlay
margin".[^garofalo-1995] The `li` rules need 0.080 µm of LI beyond a
licon on one of two adjacent sides (li.5).[^pdk-periph]

### Substrate and tone

On the step pages' readings the resist is
coated on TiN. Sturtevant et al.
examined DUV resists on substrates including titanium nitride and found a
"substrate contamination" effect "which results in distorted photoresist
profiles at the substrate/resist interface", with organic
anti-reflective films acting "as effective barrier layers in some
cases".[^sturtevant-1994]

He et al. developed a silicon oxynitride ARC
that "can not only function as an ARC layer, but also serve as a
hardmask".[^he-1998] Sekiguchi et al. found the effect of underlayer
reflection on the isolated–dense CD bias significant for a negative
resist and small for a positive one.[^sekiguchi-1998]

The step page reads a chemically
amplified positive KrF resist over an organic or inorganic ARC; with the
resist left where `li1` is drawn, the plate would be clear-field:
opaque lines in a clear field (inference). Neither the resist nor the
tone is published. The consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

### Overlay and alignment

The {ref}`LI1M <step-102>` page reads the mask as aligned to
the contact layer and calls li.5 "the tightest overlay-driven rule on the
layer". Above it, `mcon` needs no enclosure by LI at all (ct.4, 0.000 µm;
Table 4's "Mcon enclosure by Li", 0), but Table 4 also gives a "Minimum
mcon overlap onto LI for reproducible contact resistance" of 0.12
(`TCONOVLP`).[^pdk-periph][^pdk-03]

### Pattern transfer

On the step pages' readings the resist pattern is
transferred by {ref}`LI1ME <step-103>`, a chlorine-based etch of the
0.1 µm TiN that stops on the cap oxide and on any plug top the overlay
leaves uncovered, on the
{ref}`metal plasma etcher <machine-plasma-etcher-metal>` class. On the step pages' readings the
resist is stripped and the wafer cleaned before the nitride cap.

(mask-li1m-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `LI1M` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`LI1M <step-102>`, {ref}`LI1ME <step-103>`

* {ref}`LI1M <step-102>` — coats, exposes and develops the resist.
* {ref}`LI1ME <step-103>` — etches the TiN through the resist; the step
  list used in this reference has no separate strip step, and the step
  page describes the passivation, resist strip and clean as part of the
  etch.

On its step page's reading, the next step, {ref}`LINIT <step-104>`,
deposits a thin nitride over the patterned lines after the resist is
gone, and the next mask step is {ref}`CTM1 <step-107>`. The rule needs
no exception for this mask; the only departure from a mask–etch–strip
pattern is that the strip has no step of its own.

## Design rules and critical dimensions

The `li` rules of the periphery rules, with the rules of other sets that
refer to `li1` or `cli1m` shapes and the mask-data rules x.2, x.7, x.9
and x.15a. The published table prints the `li` rule names with a
trailing ".-" (for example "li.1.-"), shortened here. Flag P means "Rule
applies to periphery only (outside areaid.ce). A corresponding core rule
may or may not exist.", NC "Rule not checked by DRC. It should be used as
a guideline only." and AL "Rules applicable only to Al BE
flows".[^pdk-periph]

:::{table} The `li` rules, the rules of other sets that refer to `li1` or `cli1m` shapes and the mask-data rules, as published

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| li.1 | "Width of LI (except for li.1a)" (P) | 0.170 µm |
| li.1a | "Width of LI inside of cells with name s8rf2_xcmvpp_hd5_\*" (P) | 0.140 µm |
| li.2 | "Max ratio of length to width of LI without licon or mcon" (NC) | 10.000 µm |
| li.3 | "Spacing of LI to LI (except for li.3a)" (P) | 0.170 µm |
| li.3a | "Spacing of LI to LI inside cells with names s8rf2_xcmvpp_hd5_\*" (P) | 0.140 µm |
| li.5 | "Enclosure of licon by one of two adjacent LI sides" (P) | 0.080 µm |
| li.6 | "Min area of LI" (P) | 0.0561 µm² |
| li.7 | "Min LI resistor width (rule exempted within areaid.ed; […])" | 0.290 µm |
| licon.4 | "Licon1 must overlap li1 and (poly or diff or tap)" | — |
| ct.4 | "Mcon must be enclosed by LI by at least …" (P) | 0.000 µm |
| nsm.3 | "Min spacing, no overlap, between NSM_keepout to diff.dg, tap.dg, fom.dy, cfom.dg, cfom.mk, poly.dg, p1m.mk, li1.dg, cli1m.mk, metX.dg (X=1 to 5) and cmmX.mk (X=1 to 5). […]" (AL) | 1.000 µm |
| mf.7 | "Spacing (no overlapping) between fuse center and LI" | 3.300 µm |
| x.2 | "Angles permitted on: tap (except inside areaid.en), poly […], li1(periphery), licon1, capm, mcon, via, via2. Anchors are exempted." | n x 90 deg |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.9 | "Shapes on maskAdd or maskDrop layers ("serifs") are allowed in core only. Exempted are: […]" | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
:::

Table 2 of *Criteria & Assumptions* gives two "Local Intrcnct 1" rows
under the same variable names: a "Core" row with 0.14 and 0.14, and a
row with no label with 0.17 and 0.17, under `LI1MCD` and
`LI1MCDSP`.[^pdk-03]

Table 4 gives the "LI1 thickness for antenna ratio
calculations" as 0.1 (`LiThick`) and a "Li resistor width (to drop one
Licon w/o dogbones)" of 0.29 (`LIRESCD`), the value of li.7.[^pdk-03] Table 7
gives, besides the add/drop and proximity rows, a "Keepout of active,
poly, li and metal to NSM (TCS-2253)" of 1 (`NSMKeepout`), the value of
nsm.3.[^pdk-03]

The summary Table F3c, "Back end layers for S8D\*
flow", repeats li1 width and spacing as
0.170 and 0.170 with 0.000 for its enclosure of licon, noting that "All
enclosures in tables are nominal and do not apply to butting edges or
corners".[^pdk-summary] For the plate the smallest features are the
0.140 µm lines and spaces of the VPP cells (li.1a, li.3a), a 0.28 µm
pitch, and elsewhere 0.170 µm on a 0.34 µm pitch (our arithmetic).

## Related pages

* {ref}`LI1M <step-102>` and {ref}`LI1ME <step-103>` — the mask step and
  the TiN etch; {ref}`LITIN <step-101>` — the film patterned.
* **Category.** {ref}`category-lithography` and {ref}`category-etch` — the mask step
  and etch categories.
* **Machines.** {ref}`machine-duv-krf-stepper` — the exposure class the step page
  assigns. {ref}`machine-plasma-etcher-metal` — the etch class that transfers the
  pattern. {ref}`machine-cd-sem-overlay-metrology` — line CD and overlay
  measurement.
* **Materials.** {ref}`material-lithography-materials` — resists, anti-reflective
  coatings, developer and reticles.
* **Masks.** {ref}`mask-licm1` — the contact mask whose holes this pattern covers.
* **Indexes.** {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the tables this page's plate facts are taken from.

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Local Intrcnct 1, LI1M,
  X".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `li1` 67:20,
  the `cli1m` purposes and the `LI1M` column of Table F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `LI1MCD`/`LI1MCDSP`, "LI1CD
  add/drop", `LI1PROXSpace`, `LiThick`, `LIRESCD`, `NSMKeepout`,
  `TCONOVLP` and "Mcon enclosure by Li".[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `li` rules, licon.4, ct.4,
  nsm.3, mf.7, x.1a, x.1b, x.2, x.7, x.9, x.15a and the flag
  legend.[^pdk-periph]
* [SkyWater PDK, *Process stack diagram*](<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>) — the 0.10 µm `li`.[^pdk-04]
* [SkyWater PDK, *Summary of Key Periphery Rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>) — Tables F3c and
  F4.[^pdk-summary]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the `LI1M` plates of
  MPW-1 to MPW-8, the "Info" note and the mask-type tab.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `LI1M` renders, their
  layers and info text, and the per-die shape counts.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the DUV exposure
  tools.[^skw-01]
* [ASML, PAS 5500/750E press release](<https://www.asml.com/en/news/press-releases/2000/asml-introduces-krf-lithography-scanner-optimized-for>) — a KrF scanner for 130 nm design
  rules.[^asml-750e]

### High-level understanding

* [Wikipedia, *Photomask*](<https://en.wikipedia.org/wiki/Photomask>) — reticles, absorbers and
  pellicles.[^wiki-mask]
* [Wikipedia, *Optical proximity correction*](<https://en.wikipedia.org/wiki/Optical_proximity_correction>) — why mask shapes differ
  from drawn shapes.[^wiki-opc]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]

### Deep dive

* [Otto et al., *Proc. SPIE* 1994](<https://doi.org/10.1117/12.175422>) — rules-based optical proximity
  correction with edge and corner rules and assist
  features.[^otto-1994]
* [Rieger and Stirniman, *Proc. SPIE* 1994](<https://doi.org/10.1117/12.175431>) — behaviour models as
  correction rules.[^rieger-1994]
* [Cobb and Zakhor, *Proc. SPIE* 1995](<https://doi.org/10.1117/12.228208>) — fast aerial-image calculation suited
  to the mask perturbations of OPC.[^cobb-1995]
* [Shi et al., *Proc. SPIE* 2002](<https://doi.org/10.1117/12.473427>) — the forbidden-pitch phenomenon and
  assist-feature placement.[^shi-2002]
* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor of dense
  and isolated lines.[^wong-1998]
* [Arthur and Martin, *Proc. SPIE* 1999](<https://doi.org/10.1117/12.350880>) — mask error factor, CD budgets
  and reticle specifications.[^arthur-1999]
* [Garofalo et al., *Proc. SPIE* 1995](<https://doi.org/10.1117/12.209250>) — line-end shortening and its mask
  compensation.[^garofalo-1995]
* [Sekiguchi et al., *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310764>) — underlayer reflection and the
  optical proximity effect.[^sekiguchi-1998]
* [Sturtevant et al. (IBM), *Proc. SPIE* 1994](<https://doi.org/10.1117/12.175469>) — substrate contamination
  of chemically amplified DUV resists, titanium nitride
  included.[^sturtevant-1994]
* [He et al., *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310763>) — an inorganic ARC that doubles as a hard
  mask.[^he-1998]
* [Tang et al. (TI), *IEEE TED* 1987](<https://doi.org/10.1109/T-ED.1987.22980>) — the TiN local interconnect,
  patterned from a 0.1 µm film.[^tang-1987]
* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — the optical mask requirements for critical
  layers at 130 nm.[^itrs-03]

## Open questions

* The operation that makes the `cli1m` plate data from `li1` and the
  `cli1m` drawing, add and drop purposes is not published; how the
  "LI1CD add/drop" values and the "Li1 proximity correction" space are
  applied is not stated.[^pdk-06][^pdk-03]
* The plate's type, tone and CD specification, the resist and
  anti-reflective scheme, and the exposure tool are not public; the KrF
  reading rests on the 0.17 µm and 0.14 µm rules.
* Table 2's unlabelled 0.17 row and "Core" 0.14 row share variable names,
  and the PDK does not say how the 0.14 values relate to the VPP-cell
  rules li.1a and li.3a.[^pdk-03][^pdk-periph]
* The renders' fill layer 56:28 is not in `gds_layers.csv`, so what the
  site takes it to be rests on the site alone.[^mask-renders][^pdk-06]
* What the plate number `370` encodes is not stated, and no public source
  lists the `LI1M` plate of the original MPW-4 set
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
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-summary]: SkyWater PDK Authors, *Summary of Key Periphery Rules*
    (Tables F3c and F4), SkyWater SKY130 PDK documentation, retrieved
    2026-09-14.
    <https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_LI1M/`
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
[^wiki-opc]: Wikipedia, *Optical proximity correction*.
    <https://en.wikipedia.org/wiki/Optical_proximity_correction>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^otto-1994]: O. W. Otto, J. G. Garofalo, K. K. Low, C.-M. Yuan,
    R. C. Henderson, C. Pierrat, R. L. Kostelak, S. Vaidya and
    P. K. Vasudev, "Automated optical proximity correction: a
    rules-based approach", *Proc. SPIE* **2197**, Optical/Laser
    Microlithography VII, 278–293 (1994).
    <https://doi.org/10.1117/12.175422>
[^rieger-1994]: M. L. Rieger and J. P. Stirniman, "Using behavior
    modeling for proximity correction", *Proc. SPIE* **2197**, 371–376
    (1994). <https://doi.org/10.1117/12.175431>
[^cobb-1995]: N. B. Cobb and A. Zakhor, "Fast sparse aerial-image
    calculation for OPC", *Proc. SPIE* **2621**, 534–545 (1995).
    <https://doi.org/10.1117/12.228208>
[^shi-2002]: X. Shi, S. Hsu, J. F. Chen, C. M. Hsu, R. J. Socha and
    M. V. Dusa, "Understanding the forbidden pitch phenomenon and assist
    feature placement", *Proc. SPIE* **4689**, Metrology, Inspection,
    and Process Control for Microlithography XVI, 985 (2002).
    <https://doi.org/10.1117/12.473427>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**,
    Optical Microlithography XI, 106 (1998).
    <https://doi.org/10.1117/12.310718>
[^arthur-1999]: G. G. Arthur and B. Martin, "Mask error factor and
    critical dimension budgets for sub-half-micron CMOS processes",
    *Proc. SPIE* **3677**, 918 (1999).
    <https://doi.org/10.1117/12.350880>
[^garofalo-1995]: J. G. Garofalo, J. DeMarco, J. Bailey, J. Xiao and
    S. Vaidya, "Reduction of ASIC gate-level line-end shortening by mask
    compensation", *Proc. SPIE* **2440**, 171–183 (1995).
    <https://doi.org/10.1117/12.209250>
[^sekiguchi-1998]: A. Sekiguchi, F. Uesawa, K. Takeuchi and T. Oda,
    "Influence of underlayer reflection on optical proximity effects in
    sub-quarter-micron lithography", *Proc. SPIE* **3334**, Optical
    Microlithography XI, 347 (1998). <https://doi.org/10.1117/12.310764>
[^sturtevant-1994]: J. L. Sturtevant, S. J. Holmes, S. E. Knight,
    D. Poley, P. A. Rabidoux, L. K. Somerville, T. L. McDevitt,
    A. Stamper et al., "Substrate contamination effects in the
    processing of chemically amplified DUV photoresists", *Proc. SPIE*
    **2197**, Optical/Laser Microlithography VII, 770–780 (1994).
    <https://doi.org/10.1117/12.175469>
[^he-1998]: Q. He, W. W. Lee, M. A. Hanratty, D. Rogers, G. Xing,
    A. Singh and E. Zielinski, "Inorganic antireflective coating process
    for deep-UV lithography", *Proc. SPIE* **3334**, Optical
    Microlithography XI, 337 (1998). <https://doi.org/10.1117/12.310763>
[^tang-1987]: T. E. Tang, C.-C. Wei, R. A. Haken, T. C. Holloway,
    L. R. Hite and T. G. W. Blake, "Titanium nitride local interconnect
    technology for VLSI", *IEEE Transactions on Electron Devices*
    **34**(3), 682–688 (1987). <https://doi.org/10.1109/T-ED.1987.22980>
