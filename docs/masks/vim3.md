(mask-vim3)=
# VIM3 — Via3-PLM

The via-3 mask is the {term}`reticle` that places every connection
between metal 3 and metal 4, and every contact to the top plates of the
first {term}`MiM capacitor`: on the {ref}`VIM3 <step-144>` page's
reading, the resist printed through it at step 144 is opened in a 0.2 µm
square over every drawn `via3`, and the {ref}`VIM3E <step-145>` etch cuts
the holes through the inter-metal oxide down to two kinds of floor, the
metal-3 lines and the capacitor plates. It is the second of the three via
masks for which the process-steps sheet records a coded mask type, the
same code as via 2's, and the only mask for which the sheet also gives an
"e-beam spot size". This page gathers what public sources say about the
mask itself — its PDK entry and layers, the plates and mask type the
process-steps sheet records, what the public renders of the MPW runs
show, the lithography it needs and the rules that constrain it. How the
step is performed is on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | VIM3 — Via3-PLM |
|---|---|
| Mask step | {ref}`VIM3 <step-144>`, step 144 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Via3-PLM", `VIM3`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cviam3` mask 50:0, "Via 3 mask"; drawing 112:20[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `via3` drawing 70:44, "Contact from metal 3 to metal 4"[^pdk-06] |
| Minimum CD, feature / space | `VIM3CD` 0.2 / `VIM3CDSP` 0.2[^pdk-03] |
| Polarity and tone | Not published; the PDK's `cviam3.nikon` checks name a polarity but not the plate's tone. The holes are opened where `via3` is drawn, which with a positive resist would make the plate dark-field (inference). |
| Exposure class | KrF (248 nm), an inference on the step page from the 0.2 µm hole and from the 248 nm mask type the sheet records for the plate; no public source names the tool ({ref}`machine-duv-krf-stepper`) |
| Mask type (process-steps sheet) | `F4-248-EAPSM-A43-APRX`, read on the masks index as an embedded attenuated phase-shift mask for 248 nm exposure and, less certainly, 4×[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `575`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-vim3-steps>` |

## What the mask defines

The periphery rules give the function of the `via3` rule set as "Via3
connects met3 to met4 in the SKY130Q\*/SKY130P\*/SP8Q/SP8P\* flow", and
the PDK's Table F4 names "Via3" as the layer joining metal 4 to metal
3.[^pdk-periph][^pdk-summary] The mask carries one product feature, a
square: "Min and max L and W of via3 (except for rule via3.1a)" 0.200 µm
(via3.1), with "Only min. square via3s are allowed except die seal ring
[…]" (via3.3); inside `areaid.mt`, the "Location of e-test modules within the
frame", rule via3.1a allows "Two sizes of square via3 allowed inside
areaid.mt: 0.200um and 0.800um",[^pdk-periph][^pdk-06] which the PDK's
*Error Messages* page, a description of "many of the automated DRC rules
that are checked by SkyWater as part of the acceptance criteria for GDS
data", checks as "via size inside module cut must be 0.200 OR
0.800".[^pdk-errors] The PDK's extraction table lists "VIA3" at 3410 in a column headed "Resistivity (mohms/sq)", the same as
"VIA2";[^pdk-08] the step page reads this as 3.4 Ω per plug.

The same holes contact the capacitors. The {ref}`VIM3 <step-144>` page
reads the PDK's cross-section of the stacked capacitor, which labels
"CAPM", "M3 (plate 1)" and "Via3",[^pdk-07] as showing vias
from metal 4 landing on the top plate and on the bottom plate, so that a
via over a plate is shallower than one over bare metal 3 by the plate and
dielectric thicknesses (inference). The `capm` rules that govern the via
name via 2 — capm.4 "Min enclosure of via2 by capm", capm.5 "Min spacing
between capm and via2", capm.8 "Min space, no overlap, between via and
capm", all "N/A" — and the step page reads them for via 3 in the flow
described here (inference).[^pdk-periph] The published SKY130
{term}`test tile` names the structures that exercise the placement: a
"Via-3 array, M4-M3 near CAPM (min via-3 space to CAPM)" with a row
"For Via Shorts, 1120 vias, each in 2x2 arrays inside holes in CAPM", a "Via-3 chain, 5754
via-3, M4-CAPM over M3 (min via enclosure)", a "Kelvin via-3, M4-CAPM
over M3", and, off the capacitors, an "s8p via3 (0.2x0.2) contact chain
(16500 contacts)"; its second large capacitor over metal 4, "Same
capacitor as 4531", notes "Caps have seas of via-3's placed under
M4/CAP2M", so via-3 plugs also lie under some metal-4 bottom plates of
the second capacitor.[^raw-data-testtile-pads]

`masks.csv` lists the via-3 mask once, as "Via3-PLM", with the same PLM
suffix as the marked via-2 and metal-3 variants but without unmarked
siblings.[^pdk-05] The {ref}`VIM3 <step-144>` page reads PLM as the label
of the five-metal P flow (inference) and notes that the assumptions
table's 2 µm metal-4 antenna thickness for "S8Q\*/SP8Q" suggests a
thick-metal-4 variant whose via 3 is not separately listed (inference).
The mask defines neither the metal-3 lines and plates the vias land on
({ref}`mask-mm3`, {ref}`mask-capm`) nor the metal-4 lines that cover them
(`MM4`), nor the liner and tungsten plug that fill the holes
({ref}`TIN5 <step-146>` to {ref}`WCMP5 <step-148>`). Table F2b, the mask
generation table, has no via columns.[^pdk-06]

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `cviam3` a `mask` purpose at 50:0 ("Via 3
mask") and a `drawing` purpose at 112:20, a layer number
that also carries the `cmm4` waffle drop at 112:4; the drawn layer is
`via3` at 70:44, "Contact from metal 3 to metal 4".[^pdk-06] The pairing
rests on the names and descriptions, as on the
{ref}`masks index <masks-index>`, and the PDK publishes no operation from
`via3` to the plate, nor what the `cviam3` drawing purpose is for. Rule
x.15a confines mask layers to test modules, seal ring and frame, and its
exception names only "FOM/P1M/Metal waffle drop" (flag P, periphery
only),[^pdk-periph] so a design inside the die draws `via3` (our reading
of x.15a, which does not say what applies in the core). One row of rule
x.2 limits via3 and via4 to "n x 90" degrees: "Angles permitted on: via3
and via4. Anchors are exempted."; the via-3 data fall under x.1b's 0.005
grid.[^pdk-periph] The [*Error Messages*](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) page lists two checks named
`cviam3.nikon`, "VIM3mk in the nikon cross has the wrong polarity" and
"VIM3mk is missing from the nikon cross in the layout";[^pdk-errors] it
does not say what the "nikon cross" is, and we read the checks as
concerning a structure on the mask layer whose data must have the right
polarity (inference from the message wording), not as stating the
plate's tone.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `VIM3` the site renders layer 70:44 (`via3`)
alone, with no Boolean expression and no fill layer, on all eight runs;
its mask record gives the mask-level layer 50:0, the description
"Via3-PLM" and the info text "Via 3 (M3→M4)".[^mask-renders] The choice
of layer is one public derivation from the drawn data, not SkyWater's
mask-generation recipe ({ref}`masks-derivations`). The info text is
identical to the "Info" note of the `VIM3` row in the process-steps
sheet, one of the level names the two sources share, so neither is cited
as corroborating the other
({ref}`masks-renders-sheet-notes`).[^steps-sheet][^mask-renders] The site
also renders its `VIPDM` entry, "Pad Via" in `masks.csv`, from the same
layer, with the note "VIPDM = via3 (pad-via flow, not SKY130)"; the
masks index finds it matching `VIM3` die by die, and no plate is recorded
for it ({ref}`masks-renders`).[^mask-renders][^pdk-05]

Every rendered die of every run carries `via3` shapes — at least
656 450 on each die[^mask-renders] — so the count of 40 dies says only
that every layout joins metal 3 to metal 4. The site states the limits of
its images: "These are renders of *drawn* data, not photomask artwork:
reticle pitch, 4x reduction, mirroring and the frame features the fab
adds are not modelled."[^mask-renders] Its metadata carries no plate ID,
so a render is tied to a plate in the sheet only by the acronym `VIM3`,
and the MPW-4 renders come from a different reticle set from the one
whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a `VIM3` plate
as existing on all eight MPW runs, with the plate number `575` on
each.[^steps-sheet] The plate IDs below are the sheet's; the reticle set
is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA575A` |
| MPW-2 | `5CS8007AC` | `S8007AA575A` |
| MPW-3 | `5CS8008AC` | `S8008AA575A` |
| MPW-4 | `5CS8018AC` | `S8018AA575A` |
| MPW-5 | `5CS8011AC` | `S8011AA575A` |
| MPW-6 | `5CS8014AC` | `S8014AA575A` |
| MPW-7 | `5CS8016AC` | `S8016AA575A` |
| MPW-8 | `5CS8017AC` | `S8017AA575A` |

* **MPW-5.** As for `VIM2`, and unlike `VIM` and `VIM4`, a `VIM3` plate is
  recorded for MPW-5; the masks index reads the MPW-5 gaps of those masks
  as more likely gaps in the record than in the run
  ({ref}`masks-mpw-runs`).[^steps-sheet]
* **Plate number.** The sheet does not say what `575` encodes. It falls
  between `572` for `CAPM` and `580` for `MM4`; from `500` to `590` the
  via and metal numbers rise in step order, but each capacitor mask is
  numbered 2 above the metal mask that follows it (`CAPM`, step 137, is
  `572` against `MM3`, step 139, `570`), and elsewhere the numbers do not
  follow process order, so no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

### The mask-type record

A tab headed "Sheet4" gives a mask type for three masks only, under the
column heading "Mask type": `F4-248-EAPSM-A43-APRX` for `VIM2` and
`VIM3`, and `B4-248-BIM-LSR-WET` for `VIM4`; a further column, "e-beam
spot size", holds 0.02 for `VIM3` and nothing for `VIM2` or
`VIM4`.[^steps-sheet] The tab does not define its codes, give a unit for
the spot size or say to which runs either applies. The masks index reads
`EAPSM` as an embedded attenuated phase-shift mask and `248` as the
exposure wavelength, from a mask maker's use of the abbreviation —
Photronics' product page states "At 248nm and 193nm wavelengths, our
embedded attenuated phase-shift masks (EAPSM) rely on a wavelength-tuned,
6% transmission MoSiON absorber" — and reads the digit 4, less certainly,
as the 4× reduction ratio.[^photronics-abr] That statement describes one
maker's catalogue, not the `VIM3` plate. As on the
{ref}`VIM2 mask page <mask-vim2>`, we do not read `F`, `A43` or `APRX`.

The spot-size column names a writing parameter, which suggests that the
plate, or its record, concerns an electron-beam mask writer (our reading
of the heading); the value's unit and meaning are not stated, and the
same type code for `VIM2` carries no spot size. Electron-beam pattern
generators served mask shops of this period: Abboud et al. describe the
work needed to meet 180 nm mask requirements on the MEBES writers, with
multipass gray writing and "a data path capable of supporting addressing
to 10 nm",[^abboud-1998] and Kurihara et al. compared e-beam and laser
writers for phase-shift mask manufacturing, including the alignment of
the shifter level to the chrome level.[^kurihara-1993] Neither says
anything about SkyWater's plates.

## Lithography and pattern transfer

**Exposure class.** The {ref}`VIM3 <step-144>` page gives
{math}`k_1 = 0.20 \times 0.70 / 0.248 \approx 0.56` on a KrF lens of NA
0.70 and about 0.35 on an i-line lens of NA 0.63, too low for production
contact holes, and infers a 248 nm level, as at via 2, from the hole size
and from the mask type the sheet records; the
{ref}`KrF stepper <machine-duv-krf-stepper>` page lists it there.
SkyWater lists "ASML DUV stepper" and "ASML DUV scanner" beside its
i-line tools but assigns no layer to any of them.[^skw-01] ITRS 2001
lists "248 nm + PSM" and "193 nm" as the exposure options for the 130 nm
node.[^itrs-03]

**Mask errors and mask type.** Wong et al. found the mask error factor
rising "rapidly when the critical dimension (CD) is less than […] 0.75
(lambda) /NA for contacts";[^wong-1998] at 248 nm and NA 0.7 that is about
0.27 µm (our arithmetic), above the 0.200 µm via, so plate CD errors would
print magnified (inference). Kim et al. found the factor rising near
the resolution limit and smaller on attenuated masks than on binary ones,
because of the attenuated plates' positive bias.[^kim-1999] Terasawa et al.
suggested that "a halftone phase-shifting mask is suitable for printing
isolated patterns",[^terasawa-1991] and Smith et al. presented candidate
shifter films, among them "a molybdenum silicon oxide
composite";[^smith-1996] Ma and Andersson describe the side-lobe printing
that limits attenuated masks,[^ma-andersson-1998] and Chen, Wang and Chu
optimised such a mask for contact holes.[^chen-1999-psm] ITRS 2001 asks,
for its 2001 (130 nm) column, for a mask CD uniformity of 8.0 nm (3σ) on contacts and vias at
4× magnification, requirements that are "for critical
layers".[^itrs-03] How tightly SkyWater specifies the `VIM3` plate is not
public.

**Two floors and the resist.** On the step pages' readings the resist
sits on the {ref}`NCAPOX5 <step-143>` cap over the via-3 oxide, 0.39 µm
above metal 3 on the PDK's stack diagram,[^pdk-04] and sees through it
both the reflective metal-3 lines and the capacitor plates at a different
depth. Brunner showed that the swing ratio scales with the square root of
the substrate reflectivity;[^brunner-1991] the step page reads an organic
{term}`BARC` under a positive chemically amplified KrF resist. With the
holes opened where `via3` is drawn, the plate would be dark-field, its
field within the pattern on the attenuated reading a partially
transmitting film rather than opaque chrome (inference); Photronics
leaves "The mask fiducials, barcode and titles" of its attenuated plates
"in high-contrast chrome".[^photronics-abr]
Neither is published. For holes Yamamoto et al. describe hierarchical
optical proximity correction;[^yamamoto-2000] whether the `VIM3` data are
corrected is not public. The consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Pattern transfer.** On the step pages' readings the holes are etched
at {ref}`VIM3E <step-145>` through the cap and the
{ref}`NILD5 <step-141>` oxide, on the
{ref}`dielectric plasma etcher <machine-plasma-etcher-dielectric>` class,
down to the refractory cap of the metal-3 lines
({ref}`overview-metal-cap`) and to the capacitor plates, and
the resist is stripped within that step. A Freescale patent describes a
via etch that stops on MiM plates and interconnect
together;[^pat-mim-freescale] Le, Banerjee and McPherson found that via
size strongly affects the electromigration failure-time spread of
tungsten-plug vias for one direction of electron flow with a TiN-capped
metallisation, and not for the other.[^le-1996]

**Overlay.** Metal 3 must enclose the via by 0.060 µm (via3.4) and by
0.090 µm on one of two adjacent sides (via3.5), and metal 4 by 0.065 µm
(m4.3); the enclosure of a via by a capacitor plate (capm.4) has no
published value.[^pdk-periph] The {ref}`VIM3 <step-144>` page reads the
mask as aligned to the {ref}`MM3 <step-139>` pattern and names the
0.060 µm metal-3 enclosure and the unpublished plate enclosure as "the
registrations that matter".

(mask-vim3-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `VIM3` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`VIM3 <step-144>`, {ref}`VIM3E <step-145>`

* {ref}`VIM3 <step-144>` — coats, exposes and develops the resist.
* {ref}`VIM3E <step-145>` — etches the via holes through the resist; the
  step list used in this reference has no separate strip step, and the
  step page treats the resist strip and post-etch clean as part of the
  etch.

On its step page's reading, the next step, {ref}`TIN5 <step-146>`,
sputters a titanium nitride liner into the cleaned holes over metal 3 and
over the capacitor plates. The next mask step is
{ref}`CAP2M <step-152>`. The rule needs no exception for this mask; the
liner, tungsten fill, plug polish and the second capacitor's films that
follow do not use the resist.

## Design rules and critical dimensions

The `via3` rules of the periphery rules, with the metal-4 enclosures of
via 3, the `capm` rules the step page reads for via 3 and the mask-data
rules x.1b, x.2, x.7, x.15a and x.18. Flag P means "Rule applies to
periphery only (outside areaid.ce). A corresponding core rule may or may
not exist.", AL "Rules applicable only to Al BE flows", CU "Rules
applicable only to Cu BE flows", IR "IR drop check compering Al database
and slotted Cu database for the same product (2 gds files) must be
clean", RR "Recommended rule at any IP level" and NC "Rule not checked by
DRC. It should be used as a guideline only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| via3.1 | "Min and max L and W of via3 (except for rule via3.1a)" (AL) | 0.200 µm |
| via3.1a | "Two sizes of square via3 allowed inside areaid.mt: 0.200um and 0.800um" (AL) | — |
| via3.2 | "Spacing of via3 to via3" (AL) | 0.200 µm |
| via3.3 | "Only min. square via3s are allowed except die seal ring where via3s are (Via3 CD)\*L" | 0.2\*L |
| via3.4 | "Via3 must be enclosed by Met3 by at least …" (AL) | 0.060 µm |
| via3.5 | "Via3 must be enclosed by Met3 on one of two adjacent sides by at least …" (AL) | 0.090 µm |
| via3.11–via3.14 | For copper flows: via size, spacing ("Min spacing between via2's"), metal-3 enclosure and row spacing (CU) | 0.210, 0.180, 0.055, 0.350 µm |
| via3.irdrop.1–4 | For 1 to 2, 3 to 15, 16 to 30 and more than 30 via3's "on the same connector", "mcon area pre- and post- Cu conversion must differ by no more than…" (CU IR) | 0.0, 0.6, 0.8, 0.9 µm |
| m4.3 | "via3 must be enclosed by met4 by atleast" (AL) | 0.065 µm |
| m4.15 | "Via3 must be enclosed by met4 by at least…" (CU) | 0.060 µm |
| capm.4 | "Min enclosure of via2 by capm" | N/A |
| capm.5 | "Min spacing between capm and via2" | N/A |
| capm.8 | "Min space, no overlap, between via and capm" | N/A |
| x.1b | "Data for SKY130 layout and mask on all layers except those mentioned in 1a must be on a grid of mm (except inside Seal ring)" | 0.005 (unit "mm") |
| x.2 | "Angles permitted on: via3 and via4. Anchors are exempted." | n x 90 deg |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
| x.18 | "Use redundant mcon, via, via2, via3 and via4 […]" (RR) | — |

Table 2 of *Criteria & Assumptions* repeats the size and space as
`VIM3CD` 0.2 and `VIM3CDSP` 0.2 for "Via3-PLM", and gives 0.21 and 0.18
for a "Via3-Cu" row (`VIM3_CuCD`, `VIM3_CuCDSP`), the values of the copper
rules via3.11 and via3.12, for a back end SKY130's aluminium flow does not
use.[^pdk-03][^pdk-periph] The summary Tables F3c and F3d stop at metal 3
and have no via-3 row.[^pdk-summary] Rule via3.12 speaks of "via2's",
and the irdrop rules speak of
"mcon area" although they are via-3 rules; the PDK explains none of
these. For the plate the decisive figures are one 0.200 µm square on a
0.40 µm pitch (our arithmetic from via3.1 and via3.2).

## Related pages

* {ref}`VIM3 <step-144>` and {ref}`VIM3E <step-145>` — the mask step and
  the via etch; {ref}`TIN5 <step-146>` — the liner that follows.
* {ref}`mask-mm3` and {ref}`mask-capm` — the metal-3 lines and capacitor
  plates the vias land on; {ref}`mask-vim2` and {ref}`mask-vim4` — the
  via masks below and above, with the same and a different mask type.
* {ref}`masks-index` — every mask's PDK entry, plates and renders, and
  the mask-type record for vias 2–4.
* {ref}`machine-duv-krf-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-plasma-etcher-dielectric` — the etch class that transfers
  the pattern.
* {ref}`machine-cd-sem-overlay-metrology` — hole CD and overlay
  measurement.
* {ref}`material-lithography-materials` — resists, anti-reflective
  coatings, developer and reticles.
* {ref}`category-lithography` and {ref}`category-etch` — the mask step
  and etch categories.

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Via3-PLM, VIM3, X" and
  "Pad Via, VIPDM".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `via3` 70:44,
  the `cviam3` purposes, `areaid.mt` and the columns of Table
  F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `VIM3CD`/`VIM3CDSP` and
  `VIM3_CuCD`/`VIM3_CuCDSP`.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `via3` rules, m4.3, m4.15,
  capm.4, capm.5, capm.8, x.1b, x.2, x.7, x.15a, x.18 and the flag
  legend.[^pdk-periph]
* [SkyWater PDK, *Summary of Key Periphery Rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>) — Tables F3c, F3d and
  F4.[^pdk-summary]
* [SkyWater PDK, *Error Messages* page](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) — the via3.1a check and the
  `cviam3.nikon` checks.[^pdk-errors]
* [SkyWater PDK, *Process stack diagram*](<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>) — the 0.39 µm via-3
  height.[^pdk-04]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — the stacked MiM cross-section.[^pdk-07]
* [SkyWater PDK, *Parasitic Layout Extraction*](<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>) — the via resistance
  table.[^pdk-08]
* [SkyWater PDK Authors, test-tile pad documentation](<https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>) — the via-3 chains and
  via-to-CAPM structures.[^raw-data-testtile-pads]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the `VIM3` plates of
  MPW-1 to MPW-8, the "Info" note and the "Sheet4" mask type and spot
  size.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `VIM3` and `VIPDM` renders,
  their layer, description and info text, and the per-die shape
  counts.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the DUV and i-line exposure
  tools.[^skw-01]
* [Photronics, *Advanced Binary Reticle*](<https://www.photronics.com/products/advanced-binary-reticle/>) — the EAPSM abbreviation in a
  mask maker's catalogue.[^photronics-abr]

### High-level understanding

* [Wikipedia, *Via (electronics)*](<https://en.wikipedia.org/wiki/Via_(electronics)>) — what a via is.[^wiki-via]
* Wikipedia, [*Photomask*](<https://en.wikipedia.org/wiki/Photomask>) and [*Phase-shift mask*](<https://en.wikipedia.org/wiki/Phase-shift_mask>) — binary and attenuated
  plates.[^wiki-mask][^wiki-psm]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on masks and reticles
  and on overlay.[^levinson-2005]

### Deep dive

* [Abboud et al., *Proc. SPIE* 1998](<https://doi.org/10.1117/12.328815>) — electron-beam pattern generation for
  180 nm masks.[^abboud-1998]
* [Kurihara et al., *Proc. SPIE* 1993](<https://doi.org/10.1117/12.142150>) — e-beam and laser writing for
  phase-shift mask manufacturing.[^kurihara-1993]
* [Terasawa et al., *Jpn. J. Appl. Phys.* 1991](<https://doi.org/10.1143/JJAP.30.2991>) — halftone phase-shifting
  masks for isolated patterns.[^terasawa-1991]
* [Smith et al., *JVST B* 1996](<https://doi.org/10.1116/1.588655>) — four candidate shifter films for
  attenuated phase-shift masks.[^smith-1996]
* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor of
  contacts.[^wong-1998]
* [Kim et al., *Proc. SPIE* 1999](<https://doi.org/10.1117/12.354400>) — mask CD error for contact holes on
  binary and attenuated masks.[^kim-1999]
* [Ma and Andersson, *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310783>) — side-lobe printing with
  attenuated plates.[^ma-andersson-1998]
* [Chen, Wang and Chu, *Proc. SPIE* 1999](<https://doi.org/10.1117/12.354399>) — optimising an attenuated mask
  for contact holes.[^chen-1999-psm]
* [Yamamoto et al., MNC 2000](<https://doi.org/10.1109/IMNC.2000.872612>) — hierarchical OPC on contact-hole
  layers.[^yamamoto-2000]
* [Brunner, *Proc. SPIE* 1991](<https://doi.org/10.1117/12.46410>) — the swing ratio and anti-reflective
  coatings.[^brunner-1991]
* [Roberts and Huffman (Freescale), US 7,375,002](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7375002>) — vias to MiM plates and
  interconnect etched together.[^pat-mim-freescale]
* [Le, Banerjee and McPherson (TI), *Semicond. Sci. Technol.* 1996](<https://doi.org/10.1088/0268-1242/11/6/003>) — via
  size and tungsten-plug via electromigration.[^le-1996]
* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — exposure options and mask requirements for
  critical layers at 130 nm.[^itrs-03]

## Open questions

* The "Sheet4" codes are not defined; the attenuated and 248 nm readings
  rest on a mask maker's abbreviation, the 4× reading is less certain,
  and the fields `F`, `A43` and `APRX` are not read. The unit and meaning
  of the "e-beam spot size" 0.02, and why only `VIM3` has one, are not
  stated.[^steps-sheet]
* The plate's maker, shifter film, tone and CD specification, any OPC,
  the resist and the exposure tool are not public; the KrF reading rests
  on the 0.200 µm rule and the mask type.
* The `capm` rules that govern vias on the plates name via 2 and have no
  published values; the reading for via 3 is the step page's
  inference.[^pdk-periph]
* The PDK does not say what the `cviam3` drawing purpose at 112:20 is
  for.[^pdk-06]
* What the plate number `575` encodes is not stated, and no public source
  lists the `VIM3` plate of the original MPW-4 set
  `5CS8010AC`.[^steps-sheet][^mask-renders]

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tabs "Sheet1" (step number, code and description), "Masks"
    (mask steps with step numbers), "Run Mask IDs" (the mask table set
    against MPW-1 to MPW-8, with "Exists", "Plate ID" and "Info" columns)
    and "Sheet4" (mask types and e-beam spot size), retrieved 2026-09-14.
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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Table 2),
    SkyWater SKY130 PDK documentation.
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
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md`, `masks.html` and, for each run, the
    `mpw-00N_VIM3/` and `mpw-00N_VIPDM/` directories with their pages,
    `job.json`, `result.json` and per-die slot JSON files, retrieved
    2026-09-14. Rendered from the public shuttle repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^photronics-abr]: Photronics, Inc., *Advanced Binary Reticle*, product
    page, retrieved 2026-09-13.
    <https://www.photronics.com/products/advanced-binary-reticle/>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^wiki-via]: Wikipedia, *Via (electronics)*.
    <https://en.wikipedia.org/wiki/Via_(electronics)>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-psm]: Wikipedia, *Phase-shift mask*.
    <https://en.wikipedia.org/wiki/Phase-shift_mask>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^abboud-1998]: F. E. Abboud, C. A. Sauer, M. Vernon, T. P. Coleman,
    R. L. Dean, W. Wang, R. Prior, M. Lu and S. Weaver, "Further advances
    in electron-beam pattern generation technology for 180-nm masks",
    *Proc. SPIE* **3412**, Photomask and X-Ray Mask Technology V, 20
    (1998). <https://doi.org/10.1117/12.328815>
[^kurihara-1993]: M. Kurihara, M. Arai, H. Fujita, H. Moro-oka,
    Y. Takahashi and H. Sano, "Primary processes in e-beam and laser
    lithographies for phase-shift mask manufacturing II", *Proc. SPIE*
    **1809**, 12th Annual BACUS Symposium on Photomask Technology and
    Management, 50 (1993). <https://doi.org/10.1117/12.142150>
[^terasawa-1991]: T. Terasawa, N. Hasegawa, H. Fukuda and S. Katagiri,
    "Imaging Characteristics of Multi-Phase-Shifting and Halftone
    Phase-Shifting Masks", *Japanese Journal of Applied Physics*
    **30**(11S), 2991 (1991). <https://doi.org/10.1143/JJAP.30.2991>
[^smith-1996]: B. W. Smith, S. Butt, Z. Alam, S. Kurinec and R. L. Lane,
    "Attenuated phase shift mask materials for 248 and 193 nm
    lithography", *Journal of Vacuum Science & Technology B* **14**(6),
    3719–3723 (1996). <https://doi.org/10.1116/1.588655>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**,
    Optical Microlithography XI, 106 (1998).
    <https://doi.org/10.1117/12.310718>
[^kim-1999]: H.-E. Kim, J.-S. Chun, S. Barnett and J. Shih, "Effect of
    mask critical dimension error for subquarter-micron contact hole",
    *Proc. SPIE* **3679**, 821 (1999).
    <https://doi.org/10.1117/12.354400>
[^ma-andersson-1998]: Z. M. Ma and A. Andersson, "Preventing sidelobe
    printing in applying attenuated phase-shift reticles", *Proc. SPIE*
    **3334**, Optical Microlithography XI, 543 (1998).
    <https://doi.org/10.1117/12.310783>
[^chen-1999-psm]: Y.-T. Chen, Y.-C. Wang and R. Chu, "Optimization of
    attenuated phase-shift mask for contact hole printing", *Proc.
    SPIE* **3679**, Optical Microlithography XII, 812 (1999).
    <https://doi.org/10.1117/12.354399>
[^yamamoto-2000]: K. Yamamoto, S. Kobayashi, T. Uno and T. Kotani,
    "Hierarchical optical proximity correction on contact hole layers",
    *Digest of Papers, Microprocesses and Nanotechnology 2000*,
    pp. 40–41. <https://doi.org/10.1109/IMNC.2000.872612>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^pat-mim-freescale]: D. R. Roberts and G. L. Huffman (Freescale
    Semiconductor), *MIM capacitor in a semiconductor device and method
    therefor*, US 7,375,002 B2, filed 2005-06-28, granted 2008-05-20.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7375002>
[^le-1996]: H. A. Le, K. Banerjee and J. W. McPherson, "The dependence of
    W-plug via EM performance on via size", *Semiconductor Science and
    Technology* **11**(6), 858–864 (1996).
    <https://doi.org/10.1088/0268-1242/11/6/003>
