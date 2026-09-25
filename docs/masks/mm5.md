(mask-mm5)=
# MM5 — Metal 5

The metal-5 mask is the {term}`reticle` that draws SKY130's top metal.
On the {ref}`MM5 <step-162>` page's reading, the resist printed through
it at step 162 stays wherever `met5` is drawn — the top-level supply
grid and wide buses, the bond pads that the pad mask later
opens, inductor turns and the landings of every via 4.

| | MM5 — Metal 5 |
|---|---|
| Mask step | {ref}`MM5 <step-162>`, step 162 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Metal 5", `MM5`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cmm5` mask 59:0, "Metal 5 mask"; waffle drop 117:4[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `met5` drawing 72:20, "Metal 5"[^pdk-06] |
| Minimum CD, feature / space | `MM5CD` / `MM5CDSP`: "All flows except S8PF\*/S8PIR\*" 0.8 / 0.8; "S8PF\*/S8PIR\*" 1.6 / 1.6[^pdk-03] |
| Polarity and tone | Not published; the PDK's `cmm5.nikon` checks name a polarity but not the plate's tone. On the step page's reading the resist remains where `met5` is drawn, which with a positive resist would make the plate clear-field (inference). |
| Exposure class | i-line, an inference on the step page from the 1.6 µm rules; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `590`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-mm5-steps>` |

:::{seealso}
How the step is performed is on the step page; every mask is indexed
on the {ref}`masks index <masks-index>`.
:::

## What the mask defines

On the {ref}`MM5 <step-162>` page's reading, the
{ref}`MM5E <step-163>` etch removes the 1.26 µm metal-5 stack everywhere
else. The mask is the coarsest of the five metal masks, with 1.6 µm lines on
the step page's reading of the flow. With metal 2, it is one of the two
masks for which a transcribed plate-case label is public, although the
label is not tied to an MPW run.

The periphery rules give the function of the `m5` rule set as "Defines
Fifth level of metal interconnects;".[^pdk-periph] The PDK's Table F4 shows metal
5 joined to metal 4 by "Via4" and to the copper redistribution layer
`rdl` by "(pad AND pmm) for s8pir/s8pr2-10r flows".[^pdk-summary]

The `m5` rules are four:[^pdk-periph]

* a minimum width and spacing of 1.600 µm (m5.1,
  m5.2)
* an enclosure of via 4 of 0.310 µm (m5.3)
* a minimum area of
  4.000 µm², with probe pads of exactly 1.42 µm × 1.42 µm exempted "For all
  flows except SKY130PIR\*/SKY130PF\*" (m5.4)

Table 2 of
*Criteria & Assumptions* gives two rows for the mask, 0.8 for "All flows
except S8PF\*/S8PIR\*" and 1.6 for "S8PF\*/S8PIR\*".[^pdk-03] The
{ref}`MM5 <step-162>` page reads SKY130 as an S8PIR\* flow, from the
background page's "5 levels of metal (p - penta)", "Inductor or
Inductor-Capable (i)" and "Poly resistor (r)",[^pdk-02] so that both
tables give 1.6 µm and the m5.4 exemption does not apply (inference on
that page).

The published SKY130 {term}`test tile` measures metal 5 at
that width: "S8PIR/PF WM5_Kelvin (Width = 1.6um/ Length = 223.6um)", "s8pir/pf M5
(w=1.6) serp / comb over field" and "top:met5 width:1.600 space:1.600",
among other structures.[^raw-data-testtile-pads]

The extraction table gives metal 5 a sheet resistance of 29 in a column
headed "Resistivity (mohms/sq)", against 47 for metals 3 and 4, and via 4
380,[^pdk-08] and the stack diagram draws `metal5` 1.26 µm
thick.[^pdk-04] Table C3 of the *Layers Reference* defines "top_metal" as
"met5.dg OR mm5.mk (for SP8P\*/S8P\*)" and "bondPad" as "pad:dg OUTSIDE
areaid:ft".[^pdk-06]

The mask therefore draws, on the step page's reading,
the pads that {ref}`PDM <step-168>` opens: the Error Messages page checks "2.7 min.
enclosure of bondpadNormal by met5" (pad.4/4a) (and cupad.3 for pad
openings inside an inductor) and "2.5 min. enclosure
of UTESTPAD by met5" (scribe.17), none of which the periphery rules
list.[^pdk-errors][^pdk-periph] The page describes "many of the automated DRC rules that are checked by SkyWater
as part of the acceptance criteria for GDS data".[^pdk-errors] The {ref}`PDM <step-168>` page reports
the same 2.7 µm margin, per side, in SkyWater's GPIO pad cell
({ref}`mask-pdm`).

Marsh et al. bonded copper wire over probe marks on pads of 0.8 µm and
3 µm aluminium,[^marsh-2016] and Ching and Schroen found that the choice
of pad metallisation, among systems of aluminium and titanium-tungsten
alloy, changed a pad's tolerance of bonding stresses.[^ching-1988] Hess et al. studied pads
with circuitry under them at 0.13 µm.[^hess-2003]

The PDK's mask generation table, Table F2b, has an `MM5` column, marked
`C` ("CREATED") in two of its 80 device rows, "Cu Inductor" and "Balun
Inductor", and `+` ("Layer allowed to overlap") in the other 78; it has
no column for `MM4` or `PDM`.[^pdk-06] We read the two `C` marks as
tying created metal-5 data to the copper-inductor option, whose `rdl`
the periphery rules say "Connects to met5 through the pad opening"
(our reading of the table; the PDK does not explain its
marks).[^pdk-periph] Chu et al. used thick top metal for high-quality
spiral inductors.[^chu-2001]

**Variants and flows.** `masks.csv` lists "Metal 5" once and marks
it.[^pdk-05] Table 4 of [*Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) gives metal-5
thicknesses "for antenna ratio calculation" of 2 for "(S8P\*/SP8P\* with
2um thick metal)" (`Met5Thick_p`) and 1.2 for "(S8P\*/SP8P\* with 1.2um
thick metal)" (`Met5Thickp_12`), in a block headed "Material Thicknesses"
with a column headed "Value (um)".[^pdk-03] The
{ref}`MM5E <step-163>` page reads the 1.2 µm entry as SKY130's
(inference).

The mask does not define the metal stack it patterns,
which {ref}`WTIAL5 <step-161>` deposits, the via-4 holes beneath
({ref}`mask-vim4`), or the passivation openings above
({ref}`mask-nsm`, {ref}`mask-pdm`).

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives the mask-level layer `cmm5` two purposes: `mask`
at 59:0 ("Metal 5 mask") and `waffle drop` at 117:4, on a layer number
that also carries the `cviam4` drawing purpose at 117:20.[^pdk-06] The drawn layer
is `met5` at 72:20, with block, label, net, pin, cut, probe and short
purposes among its others.[^pdk-06] The pairing of the mask with `met5`
rests on those names and descriptions, as on the
{ref}`masks index <masks-index>`. The PDK publishes no operation from the
drawn layer to the plate.

Rule x.15a confines "Drawn compatible, mask,
and waffle-drop layers" to test modules, seal ring and frame, "Exception:
FOM/P1M/Metal waffle drop are allowed inside the die" (flag P),[^pdk-periph]
so a die may carry `cmm5` waffle-drop shapes as well as `met5` (our
reading). With no add or drop purpose, rule x.9's "serifs" have no
`cmm5` layer to sit on.

Unlike metals 1 to 4, metal 5 has no waffle-drop density rule
in the periphery rules.[^pdk-periph] The Error Messages page lists waffle-drop
density checks for metals 1 to 4 (`m1.x.1` to `m4.x.1`) and none for
metal 5.[^pdk-errors] Table 4's "Waffling / Pattern Density"
block, headed "Value", gives a "Min MM\* PD range" of 0.3 (`MMPDrange`)
and a "Maximum metal waffle drop pattern density in the frame" of 0.55
(`PD_FrameWP`), without naming metal 5.[^pdk-03] The
{ref}`MM5 <step-162>` page notes that this reference describes no oxide
polish over metal 5 (its inference for the missing density rule).

The Error Messages page names a mask-data layer `MM5mk` in:[^pdk-errors]

* the generic
  grid, octagonal-edge and x.15a checks ("off 0.005 grid MM5mk vertex",
  "non-octagonal MM5mk edge", "X.15a: layer MM5mk allowed inside areaid:mt
  or inside areaid.sl or inside areaid.ft")
* "Wide mm5mk >= 10.0x10.0um
  within 150.0 of scribe junction" (scribe.5)
* two checks named
  `cmm5.nikon`, "MM5mk in the nikon cross has the wrong polarity" and
  "MM5mk is missing from the nikon cross in the layout"

The page
does not say what the "nikon cross" is. The seal-ring cell
`advSeal_6um_gen` published in Efabless's caravel repository contains, in
each of its four corners, a sub-cell named `nikon_sealring_shape` (our reading
of the GDS file).[^caravel-sealring] The sub-cell
draws inside a 4 µm square a cross of three rectangles, 2.4 µm across
with 0.5 µm arms, on `cmm5` 59:0 and 23 other mask-level layers, and the
square, with its corners cut at 45°, less the cross on seven more, among
them `cpdm` 37:0 (our reading
of the GDS file).[^caravel-sealring]

We read that sub-cell as a "nikon
cross" of the kind the checks name, and the two drawn forms as the
"polarity" they test (inference from the names). Rule nsm.3 exempts cells
named "nikon\*" from the nitride-seal keep-out.[^pdk-periph] None of this
states the tone of the plate.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `MM5` the site renders layers 72:20 (`met5`)
and 59:28, which it lists as a fill layer, with no Boolean expression and
no note, on all eight runs.[^mask-renders] Its mask record gives the mask-level layer
59:0 and the info text "Metal 5".[^mask-renders]

Layer 59:28 is not in
`gds_layers.csv`, whose `cmm5` waffle-drop purpose is 117:4, so the site's
choice of it is one public reading of the tape-out files, not a PDK
definition ({ref}`masks-derivations`).[^pdk-06] Like the site's other layer
choices, it is one public derivation from the drawn data, not SkyWater's
mask-generation recipe.[^mask-renders]

The info text is
identical to the "Info" note of the `MM5` row in the process-steps sheet,
so neither is cited as corroborating the other
({ref}`masks-renders-sheet-notes`).[^steps-sheet][^mask-renders] The
`nikon_sealring_shape` crosses sit on 59:0, which the site does not
render.

Every rendered die of every run carries shapes on these layers — at least
115 443 on each die, fill included[^mask-renders] — so the count of 40
dies says only that every layout has metal 5.

The site states the limits
of its images: "These are renders of *drawn* data, not photomask artwork:
reticle pitch, 4x reduction, mirroring and the frame features the fab
adds are not modelled."[^mask-renders] Its metadata carries no plate ID,
so a render is tied to a plate in the sheet only by the acronym `MM5`,
and the MPW-4 renders come from a different reticle set from the one
whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `MM5` plate
as existing on all eight MPW runs, with the plate number `590` on
each.[^steps-sheet] The plate IDs below are the sheet's; the reticle set
is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA590A` |
| MPW-2 | `5CS8007AC` | `S8007AA590A` |
| MPW-3 | `5CS8008AC` | `S8008AA590A` |
| MPW-4 | `5CS8018AC` | `S8018AA590A` |
| MPW-5 | `5CS8011AC` | `S8011AA590A` |
| MPW-6 | `5CS8014AC` | `S8014AA590A` |
| MPW-7 | `5CS8016AC` | `S8016AA590A` |
| MPW-8 | `5CS8017AC` | `S8017AA590A` |

* **MPW-5.** Unlike `VIM4`, the mask below it, an `MM5` plate is
  recorded for MPW-5; the masks index reads the MPW-5 gap of `VIM4` as
  more likely a gap in the record than in the run
  ({ref}`masks-mpw-runs`).[^steps-sheet]
* **Plate number.** The sheet does not say what `590` encodes.

  It is the
  highest of the via and metal numbers from `500` to `590`, which rise in
  step order apart from the capacitor masks, and `PDM` (step 168) is
  `600`.[^steps-sheet] But `NSM` (step 165), between them, is `007`, and elsewhere the
  numbers do not follow process order, so no process position is read
  from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Plate-case label.** The sheet's "Random Mask Case Label Info" tab
  transcribes a Photronics plate-case label whose part-number field names
  `MM5` and the number 590.

  It gives:[^steps-sheet]

  * the material as a 6 × 6 × 0.25 in
    blank
  * the type as "4X Beam Final"
  * a "Percent Clear" of 58.56
  * a
    "Level" of 14
  * a CD specification for patterns it names "Scribe
    Frame Array / Plot / X" and "Scribe Frame Array / Plot / Y", nominal
    6.52 with tolerances of 0.08 either way, measured at means of 6.5163
    (X) and 6.5388 (Y), in no stated unit

  The tab does not
  tie the label to one of the MPW runs ({ref}`masks-mpw-runs`) or define
  its fields. We read "4X" as the reduction ratio and "Percent Clear" as
  the transmitting share of the plate area (inference from the field
  names alone). On those readings a metal-5 plate that is 58.56 % clear
  would fit the clear-field reading of the quick-facts table, but the
  label may belong to another reticle set (inference).

  Hochmuth, Ruhl
  and Coleman found that with chrome dry etch "the deviation of the CD
  from the target value is a function of the chrome loading on the
  plate".[^hochmuth-1999] Whether the recorded percentage serves that
  purpose is not stated.
* **Mask type.** The sheet's "Sheet4" tab gives no type for
  `MM5`.[^steps-sheet] 4× is the ITRS 2001 mask magnification for the
  130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

### Exposure class

The {ref}`MM5 <step-162>` page gives
{math}`k_1 = 1.6 \times 0.6 / 0.365 \approx 2.6` on an i-line lens of NA
0.6, and about 1.3 for the 0.8 µm of other flows, "far from any
resolution limit", and infers an i-line level, quoting ASML's statement
that older systems "migrate to the lithography of choice for less
critical layers".[^asml-30] The
{ref}`i-line stepper <machine-i-line-stepper>` page lists it there.

SkyWater lists "ASML I-line stepper" and "ASML I-line scanner" but
assigns no layer to them.[^skw-01] If via 4 below is a KrF level, as the
{ref}`VIM4 <step-159>` page infers, this mask overlays a level printed on
another class of tool ({ref}`mask-vim4`).

### Mask errors

Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space
patterns".[^wong-1998] At 365 nm and NA 0.6 that is about 0.30 µm (our
arithmetic), far below the 1.6 µm line, so plate CD errors would print
at their own size (inference). At 4× a 1.6 µm line is 6.4 µm on the plate
(our arithmetic).

### Thick metal and the resist

The step page's point is thickness rather
than resolution: the resist must outlast the etch of a 1.26 µm
stack.[^pdk-04] Krogh et al. followed photoresist erosion in an
aluminium etch plasma by emission spectroscopy.[^krogh-1987] So the
{ref}`MM5 <step-162>` page reads a thicker DNQ/novolac i-line resist than
at the lower metal levels (the chemistry of Dammel's
text[^dammel-1993]) and notes that Allen and Rickard's tapered aluminium
etch need not follow the resist slope.[^allen-1994]

On a reflective metal
the swing ratio scales with the square root of the substrate
reflectivity, as Brunner showed,[^brunner-1991] and Rocke and Schneegans
used titanium nitride on aluminium as an anti-reflection
layer.[^rocke-1988] The step page reads a BARC or dyed resist as a
latitude choice at these sizes. None of this is published for SKY130. The
consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

### Overlay and alignment

Metal 5 must enclose each via 4 by 0.310 µm (m5.3), and,
on the Error Messages page, a normal bond pad ("bondpadNormal") by
2.7.[^pdk-periph][^pdk-errors] The {ref}`MM5 <step-162>` page names the
alignment to the via-4 pattern as the registration that matters.

### Pattern transfer

On the step pages' readings the resist pattern is
transferred by {ref}`MM5E <step-163>`, a chlorine etch of the metal stack
on the {ref}`metal plasma etcher <machine-plasma-etcher-metal>` class that
stops on the {ref}`NCAPOX6 <step-158>` cap oxide. On the step pages' readings passivation, resist
strip and clean are treated as part of that step. The level's pattern density
is low over much of a die on that page's reading; Chang et al. studied
the corrosion and passivation-swelling defects of an ultra-low
pattern-density thick-metal etch.[^chang-2004]

Bohr argued that
interconnect limits performance[^bohr-1995] and Stamper, Fuselier and
Tian treated the RC delay of aluminium wiring below 0.25 µm.[^stamper-1998]
The step page cites both for why the top level is the thickest. The
renders' fill layer suggests that some layouts add metal-5 fill
(inference from the site's layer name); Kahng and Samadi survey fill
synthesis.[^kahng-2008]

(mask-mm5-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `MM5` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`MM5 <step-162>`, {ref}`MM5E <step-163>`

* {ref}`MM5 <step-162>` — coats, exposes and develops the resist.
* {ref}`MM5E <step-163>` — etches the metal-5 stack through the resist;
  the step list used in this reference has no separate strip step, and
  the step page treats the passivation, resist strip and clean as part of
  the etch.

On its step page's reading, the next step, {ref}`NFUSOX <step-164>`,
deposits a thin, blanket oxide over the etched metal-5 lines and pads
after the resist is gone. The next mask step is {ref}`NSM <step-165>`.
The rule needs no exception for this mask.

## Design rules and critical dimensions

The `m5` rules of the periphery rules, with the other rules that name
metal 5 or its mask data.

Flag P means "Rule applies to periphery only
(outside areaid.ce). A corresponding core rule may or may not exist.", AL
"Rules applicable only to Al BE flows", F "Rule intended for Frame only,
not checked inside Die", RC "Recommended rule at the chip level, required
rule at the IP level." and NC "Rule not checked by DRC. It should be used
as a guideline only."[^pdk-periph]

:::{table} The `m5` rules and the other rules that name metal 5 or its mask data, as published

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| m5.1 | "Min width of met5" | 1.600 µm |
| m5.2 | "Min spacing between two met5" | 1.600 µm |
| m5.3 | "via4 must  be enclosed by met5 by atleast" | 0.310 µm |
| m5.4 | "Min area of met5 (For all flows except SKY130PIR\*/SKY130PF\*, the rule is exempted for probe pads which are exactly 1.42um by 1.42um)" | 4.000 µm² |
| pad.3 | "Max area of hugePad NOT top_metal" | 30000 µm² |
| nsm.3 | "Min spacing, no overlap, between NSM_keepout to […] metX.dg (X=1 to 5) and cmmX.mk (X=1 to 5). Exempt the following from the check: (a) cell name "nikon\*" and (b) diff ring inside areaid.sl" (AL) | 1.000 µm |
| nsm.3a | "Min enclosure of […] metX.dg (X=1 to 5) and cmmX.mk (X=1 to 5) by areaid.ft. […]" | 3.000 µm |
| nsm.3b | "Min spacing between areaid.dt to […] metX.dg (X=1 to 5) and cmmX.mk (X=1 to 5). […]" | 3.000 µm |
| x.1b | "Data for SKY130 layout and mask on all layers except those mentioned in 1a must be on a grid of mm (except inside Seal ring)" | 0.005 (unit "mm") |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.9 (first row) | "Shapes on maskAdd or maskDrop layers ("serifs") are allowed in core only. Exempted are: […] cfom md/mp inside "advSeal_6um\* OR cuPillarAdvSeal_6um\*" pcell […] diff rings around the die at min total L>1000 um and W=0.3 um, and PMM/PDMM inside areaid:sl" | — |
| x.9 (second row) | "Shapes on maskAdd or maskDrop layers ("serifs") are allowed in core only. PMM/PDMM inside areaid:sl are excluded." | N/A |
| x.12d | "Spacing of areaid.mt to huge_metX (Exempt met5.dg)" (F) | — |
| x.12e | "Enclosure of huge_metX by areaid.mt (Exempt met5.dg)" (F) | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
| x.22 | "No floating interconnects (poly, li1, met1-met5) or capm allowed; […]" (RC) | — |
| x.23c | "areaid.sl must not overlap tap, poly, li1 and metX" | — |
:::

The Error Messages page repeats m5.1 to m5.4 with the same values ("1.6
min. width of met5", "1.6 min. spacing/notch of met5", "0.31 min.
enclosure of via4 by met5", "4 min. area of met5").[^pdk-errors] It adds checks the
periphery rules do not list:[^pdk-errors]

* the bond-pad enclosure of 2.7 (pad.4/4a)
* a
  "1.6 min. spacing of met5 & met5Block" (metblk.1)
* "0.8 min. spacing of
  moduleCutAREA & q0met5notBuildSpace" (x.12a)
* "2.50um min. enclosure of
  Etest pad by met5" (scribe.13)
* "3.295 min. spacing of target & met5"
  (mf.24)

Table 2 of *Criteria & Assumptions* gives `MM5CD`
and `MM5CDSP` as 0.8 and 0.8 for "All flows except S8PF\*/S8PIR\*" and
1.6 and 1.6 for "S8PF\*/S8PIR\*".[^pdk-03] Table 4 adds, in its "Material
Thicknesses" block, the metal-5 antenna thicknesses of 2 and 1.2 and, in
its "Waffling / Pattern Density" block, the 0.3 of `MMPDrange`.[^pdk-03] Table 7 gives a
"Huge metal X min. W and L" of 3 (`HugeM`) in its column headed "CD".[^pdk-03]
Table 9, "Criteria for polyimide manufacturability", gives a "Min/Max enclosure
of pad.dg inside M5RDL by pmm" of 0 (`pmmM5RDLpadEnc`).[^pdk-03]

For the
plate the decisive figures are 1.600 µm lines on a 3.2 µm pitch (our
arithmetic from m5.1 and m5.2), with pads tens of micrometres wide among
them.

## Related pages

* **Steps.** {ref}`MM5 <step-162>` and {ref}`MM5E <step-163>` — the mask step and
  the metal etch; {ref}`WTIAL5 <step-161>` — the stack patterned.
* **Category.** {ref}`category-lithography` and {ref}`category-etch` — the mask step and
  etch categories.
* **Machines.** {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns. {ref}`machine-plasma-etcher-metal` — the etch class that transfers the
  pattern. {ref}`machine-cd-sem-overlay-metrology` — line CD and overlay
  measurement.
* **Materials.** {ref}`material-lithography-materials` — resists, anti-reflective
  coatings, developer and reticles.
* **Masks.** {ref}`mask-vim4` — the via mask below; {ref}`mask-mm4` — the metal mask
  one level down; {ref}`mask-nsm` and {ref}`mask-pdm` — the two masks
  printed over this level.
* **Indexes.** {ref}`masks-index` — every mask's PDK entry, plates and renders, and the
  plate-case labels.

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Metal 5, MM5,
  X".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `met5` 72:20,
  the `cmm5` purposes, Table C3's "top_metal" and "bondPad" and the `MM5`
  column of Table F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `MM5CD`/`MM5CDSP`, the metal-5
  antenna thicknesses, `MMPDrange`, `PD_FrameWP`, `HugeM` and
  `pmmM5RDLpadEnc`.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `m5` rules, pad.3, nsm.3–nsm.3b,
  x.1b, x.7, x.9, x.12d, x.12e, x.15a, x.22, x.23c and the flag
  legend.[^pdk-periph]
* [SkyWater PDK, *Error Messages* page](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) — the `m5`, pad, cupad.3, scribe and
  `cmm5.nikon` checks.[^pdk-errors]
* [SkyWater PDK, *Summary of Key Periphery Rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>) — Table F4.[^pdk-summary]
* [SkyWater PDK, *Background*](<https://skywater-pdk.readthedocs.io/en/main/rules/background.html>) — the flow letters.[^pdk-02]
* [SkyWater PDK, *Process stack diagram*](<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>) — the 1.26 µm `metal5`.[^pdk-04]
* [SkyWater PDK, *Parasitic Layout Extraction*](<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>) — the metal-5 and via-4
  resistances.[^pdk-08]
* [SkyWater PDK Authors, test-tile pad documentation](<https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>) — the 1.6 µm metal-5
  structures.[^raw-data-testtile-pads]
* Efabless, caravel `advSeal_6um_gen` seal-ring GDS — the
  `nikon_sealring_shape` sub-cell.[^caravel-sealring]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the `MM5` plates of MPW-1
  to MPW-8, the "Info" note, the plate-case label and the mask-type
  tab.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `MM5` renders, their layers
  and info text, and the per-die shape counts.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the i-line exposure
  tools.[^skw-01]
* [ASML, *Three decades of PAS 5500*](<https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>) — older exposure tools moving to less
  critical layers.[^asml-30]

### High-level understanding

* [Wikipedia, *Photomask*](<https://en.wikipedia.org/wiki/Photomask>) — reticles, absorbers and
  pellicles.[^wiki-mask]
* [Wikipedia, *Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) — i-line exposure.[^wiki-litho]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — imaging, focus
  and thick resists.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on masks and reticles
  and on overlay.[^levinson-2005]

### Deep dive

* [Ching and Schroen, IRPS 1988](<https://doi.org/10.1109/IRPS.1988.362201>) — oxides under bond pads and the choice of
  metallisation.[^ching-1988]
* [Marsh et al., ECTC 2016](<https://doi.org/10.1109/ECTC.2016.382>) — copper ball bonds over probe marks on pads of
  two aluminium thicknesses.[^marsh-2016]
* [Hess et al., ECTC 2003](<https://doi.org/10.1109/ECTC.2003.1216469>) — bond-over-active pad structures for 0.13 µm
  CMOS.[^hess-2003]
* [Chu et al., VLSI-TSA 2001](<https://doi.org/10.1109/VTSA.2001.934506>) — thick top metal for high-quality spiral
  inductors.[^chu-2001]
* [Krogh et al., *J. Electrochem. Soc.* 1987](<https://doi.org/10.1149/1.2100816>) — photoresist erosion in an
  aluminium etch plasma.[^krogh-1987]
* [Allen and Rickard, *JVST A* 1994](<https://doi.org/10.1116/1.579306>) — a tapered aluminium interconnect
  etch.[^allen-1994]
* [Chang et al., SMTW 2004](<https://doi.org/10.1109/SMTW.2004.1393753>) — defects of an ultra-low pattern-density
  thick-metal etch.[^chang-2004]
* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor and the
  feature size above which it is unity.[^wong-1998]
* [Hochmuth, Ruhl and Coleman, *Proc. SPIE* 1999](<https://doi.org/10.1117/12.373324>) — plate CD against chrome
  loading in dry-etched masks.[^hochmuth-1999]
* [Brunner, *Proc. SPIE* 1991](<https://doi.org/10.1117/12.46410>) — the swing ratio on reflective
  substrates.[^brunner-1991]
* [Rocke and Schneegans, *JVST B* 1988](<https://doi.org/10.1116/1.584306>) — titanium nitride as an
  anti-reflection layer on aluminium.[^rocke-1988]
* [Dammel, *Diazonaphthoquinone-based Resists*](<https://doi.org/10.1117/3.2265072>) — the i-line resist
  chemistry.[^dammel-1993]
* Bohr, IEDM 1995, and Stamper, Fuselier and Tian, IITC 1998 — why the top
  aluminium level is thick and wide.[^bohr-1995][^stamper-1998]
* [Kahng and Samadi, *IEEE TCAD* 2008](<https://doi.org/10.1109/TCAD.2007.907061>) — a survey of CMP fill
  synthesis.[^kahng-2008]

## Open questions

* The operation that makes the `cmm5` plate data from `met5` and its
  waffle-drop purpose is not published; the renders' fill layer 59:28 is
  not in `gds_layers.csv`, and neither the periphery rules nor the Error
  Messages page gives a metal-5 density rule.[^pdk-06][^pdk-periph][^pdk-errors][^mask-renders]
* That SKY130 is an S8PIR\* flow, so that the 1.6 µm row of Table 2
  applies, is the step page's reading; neither table names SKY130's
  flow.[^pdk-03][^pdk-02]
* The PDK does not describe the "nikon cross" or say which form a mask
  layer should take in it; reading the caravel seal-ring sub-cell as that
  cross is an inference.[^pdk-errors][^caravel-sealring]
* Whether the level is exposed on an i-line tool, and the plate's type,
  tone and CD specification, the resist and its thickness, are not
  public.
* The plate-case label is not tied to an MPW run, and its fields are not
  defined; what the plate number `590` encodes is not stated, and no
  public source lists the `MM5` plate of the original MPW-4 set
  `5CS8010AC`.[^steps-sheet][^mask-renders]

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tabs "Sheet1" (step number, code and description), "Masks"
    (mask steps with step numbers), "Run Mask IDs" (the mask table set
    against MPW-1 to MPW-8, with "Exists", "Plate ID" and "Info" columns),
    "Sheet4" (mask types) and "Random Mask Case Label Info" (plate-case
    labels), retrieved 2026-09-14.
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
    7 and 9), SkyWater SKY130 PDK documentation.
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
[^pdk-02]: SkyWater PDK Authors, *Background*, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/background.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^caravel-sealring]: Efabless Corporation, *caravel* repository,
    `gds/advSeal_6um_gen.gds.gz` (seal-ring cell for SKY130 shuttle
    designs), retrieved 2026-09-14.
    <https://github.com/efabless/caravel/blob/main/gds/advSeal_6um_gen.gds.gz>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_MM5/`
    directory with its page, `job.json` and per-die slot JSON files,
    retrieved 2026-09-14. Rendered from the public shuttle repositories
    under <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
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
[^ching-1988]: T. B. Ching and W. H. Schroen, "Bond Pad Structure
    Reliability", *26th International Reliability Physics Symposium*
    (1988), pp. 64–70. <https://doi.org/10.1109/IRPS.1988.362201>
[^marsh-2016]: J. Marsh, A. Doutre, K. Syndergaard, P. Brown, K. I. Hoo,
    E. De Jesus and S. Hunter, "Copper Ball Bond over a Variety of Probe
    Marks in Two Pad Aluminum Thicknesses", *2016 IEEE 66th Electronic
    Components and Technology Conference (ECTC)*, pp. 2228–2232.
    <https://doi.org/10.1109/ECTC.2016.382>
[^hess-2003]: K. J. Hess, S. H. Downey, G. B. Halt, T. Lee, L. L. Mercado,
    J. W. Miter, W. C. Ng and D. G. Wontor, "Reliability of bond over
    active pad structures for 0.13-μm CMOS technology", *53rd Electronic
    Components and Technology Conference (ECTC 2003)*, pp. 1344–1349.
    <https://doi.org/10.1109/ECTC.2003.1216469>
[^chu-2001]: S.-F. Chu, K. W. Chew, W. B. Loh, Y. M. Wang, B. G. Onn,
    Y. Ju, J. Zhang and K. Shao, "High quality factor silicon-integrated
    spiral inductors achieved by using thick top metal with different
    passivation schemes", *2001 International Symposium on VLSI
    Technology, Systems, and Applications (VLSI-TSA)*, pp. 154–157.
    <https://doi.org/10.1109/VTSA.2001.934506>
[^krogh-1987]: O. Krogh, H. Slomowitz, Y. Melaku and H.-O. Blom,
    "Spectroscopic Diagnostics of Photoresist Erosion in an Aluminum Etch
    Plasma", *Journal of The Electrochemical Society* **134**(8),
    2045–2048 (1987). <https://doi.org/10.1149/1.2100816>
[^allen-1994]: L. R. Allen and R. Rickard, "Tapered aluminum
    interconnect etch", *Journal of Vacuum Science & Technology A*
    **12**(4), 1265–1268 (1994). <https://doi.org/10.1116/1.579306>
[^chang-2004]: F.-Y. Chang, H.-C. Huang, S.-H. Yang and S. W. Kuo, "Metal
    corrosion and passivation swelling defect study of ultra low pattern
    density thick metal etch process", *2004 Semiconductor Manufacturing
    Technology Workshop Proceedings*, pp. 153–155.
    <https://doi.org/10.1109/SMTW.2004.1393753>
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
[^dammel-1993]: R. R. Dammel, *Diazonaphthoquinone-based Resists*, SPIE
    Tutorial Texts TT11, SPIE Press, 1993.
    <https://doi.org/10.1117/3.2265072>
[^bohr-1995]: M. T. Bohr, "Interconnect scaling — the real limiter to
    high performance ULSI", *IEDM 1995 Technical Digest*, pp. 241–244.
    <https://doi.org/10.1109/IEDM.1995.499187>
[^stamper-1998]: A. K. Stamper, M. B. Fuselier and X. Tian, "Advanced
    wiring RC delay issues for sub-0.25-micron generation CMOS", *Proc.
    IEEE 1998 International Interconnect Technology Conference (IITC)*,
    pp. 62–64. <https://doi.org/10.1109/IITC.1998.704752>
[^kahng-2008]: A. B. Kahng and K. Samadi, "CMP Fill Synthesis: A Survey
    of Recent Studies", *IEEE Transactions on Computer-Aided Design of
    Integrated Circuits and Systems* **27**(1), 3–19 (2008).
    <https://doi.org/10.1109/TCAD.2007.907061>
