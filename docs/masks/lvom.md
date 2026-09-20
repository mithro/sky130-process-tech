(mask-lvom)=
# LVOM — Low Voltage Oxide

The low-voltage oxide mask is the {term}`reticle` of SKY130's
{term}`dual gate oxide`: on the {ref}`LVOM <step-044>` page's reading,
the resist printed through it at step 44 is opened over the 1.8 V
transistors and kept over the 5 V, high-voltage and memory devices, the
1.8 V NMOS channel implant {ref}`NCHI <step-045>` goes through the
openings, and {ref}`GOXETCH <step-046>` strips the thick gate oxide in
them so that the thin oxide can be grown at {ref}`LVGOX <step-047>`.
Designers do not draw this mask; they draw its thick-oxide counterpart
`hvi`, and the public record describes the plate from both sides: the
step page reads it as everything outside `hvi`, while, on our reading,
the PDK's mask generation table and one public derivation from the drawn
tape-out data describe its data as the thick-oxide and SONOS regions.
This page gathers what public sources say about the mask itself — its
PDK entry and layers, the plates the process-steps sheet records for the
MPW runs, what the public renders of those runs show, the lithography it
needs and the rules that constrain it. How the step is performed is on
the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | LVOM — Low Voltage Oxide |
|---|---|
| Mask step | {ref}`LVOM <step-044>`, step 44 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Low Voltage Oxide", `LVOM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `clvom` mask 46:0, "Low Voltage oxide mask"; drawing 45:20, with no description[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | no drawn `lvom` layer; the complement of `hvi` drawing 75:20, "High voltage (5.0V) thick oxide gate regions" — an inference of the step page[^pdk-06] |
| Minimum CD, feature / space | `LVOMCD` 0.6 / `LVOMCDSPCSMC` 0.7[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist is opened outside `hvi` and remains over it, which with a positive resist would put the absorber over the thick-oxide regions (inference); on our reading, Table F2b's rows and the renders' layers describe the plate's data as those regions (below), which fits either tone. |
| Exposure class | i-line, an inference on the step page from the 0.600 µm `hvi` width rule; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `125`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 3 steps; see {ref}`Steps that use this mask <mask-lvom-steps>` |

## What the mask defines

The mask divides the wafer between the two gate oxides. The PDK gives
the thick one: "All high voltage devices use 110A gate oxide thickness
just like low voltage (0 to Vcc) devices" and "All VHV devices use 110A
gate oxide thickness just like standard 5.0V Vcc devices";[^pdk-hv] the
public SPICE models carry an electrical oxide thickness (`toxe`) of
4.148 nm for `nfet_01v8` and 11.6 nm for
`nfet_g5v0d10v5`.[^pdk-model-nfet01v8][^pdk-model-nfet5v] The drawn layer
that marks the thick oxide is `hvi`, "High voltage (5.0V) thick oxide
gate regions", whose rule set's function line is "Defines thick oxide
for high voltage devices"; the `hvnwell` rule set adds that "All nwell
connected to voltages greater than 1.8V must be enclosed by
hvi".[^pdk-06][^pdk-periph] The {ref}`LVOM <step-044>` page reads the
mask as essentially NOT `hvi`, opened over everything outside the drawn
thick-oxide regions, and the masks index records that pairing as an
inference.

The PDK's mask generation table, Table F2b, reads from the other side.
It marks the `LVOM` column `C` ("CREATED") in 30 of its 80 device rows:
the HV n and p diffusion resistors, the "HV varactor (floating gate)",
the four SONOS transistor rows, all 13 rows of its "110A CMOS" group (the
5/10.5 V and native devices, the two "Flash npass" rows, and the 16 V
and 20 V drain-extended devices), seven diode rows (the HV, RF ESD,
native and NV SONOS diode rows) and the three HV ESD transistor
rows.[^pdk-06]
It marks `-` ("Layer not created for the device") in 28 rows, among
them every row of its "32 A CMOS" group except the HV varactor — the
1.8 V transistors, the core devices and the low- and high-Vt
varactors — and the LV ESD transistor, and `+` in the other
22.[^pdk-06] On the table, then, the created `LVOM` data belong to the
thick-oxide devices and to the memory transistors, not to the 1.8 V
devices (our reading of the rows; the table does not say what the data
are or in which tone they are written). Read with the step page, the
same plate could carry those regions as its opaque part (inference).

The SONOS rows matter for the resist. Rule hvi.4, "Hvi must not overlap
tunm", keeps the memory windows outside `hvi`,[^pdk-periph] so a plate
that was only NOT `hvi` would open the resist over the ONO islands. The
{ref}`LVOM <step-044>` page leaves open how the mask treats the islands
and infers from a Cypress patent that may still be in force that the
resist protects them; the patent's wording is in the collapsed note
below this paragraph. Table
F2b's `C` marks in the SONOS rows fit that inference (our reading). Diaz
et al. describe the same kind of division in a 0.18 µm logic technology,
where "Robust dual-gate oxides were developed to support 1.5-2 V core
logic as well as 3.3 V periphery (I/O) circuitry",[^diaz-1999] and Togo,
Noda and Tanigawa describe multiple-thickness gate oxides for
logic-embedded DRAM.[^togo-1998]

:::{dropdown} From a patent shown as in force (US 8,093,128; estimated expiry 2028-10-22) — open to read
The Cypress patent says that "while the photoresist layer 318 protects
the ONO charge trapping dielectric stack 306 a clean which would be
detrimental to the ONO charge trapping dielectric stack 306 if it were
not protected by the photoresist layer 318 may be performed at this
time".[^pat-03]
:::

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives the mask-level layer `clvom` two purposes: `mask`
at 46:0 ("Low Voltage oxide mask") and `drawing` at 45:20, which has no
description; there is no drawn layer named `lvom`, and the drawn
thick-oxide layer is `hvi` at 75:20.[^pdk-06] The PDK publishes no
operation that turns `hvi` into the plate. Table C3 of the *Layers
Reference* defines layers built from `hvi` — `LVnwell` as "nwell NOT
hvi", `Hdiff` as "Diffusion AND Hvi", `HV_nwell` as "(nwell AND hvi) OR
(nwell overlapping areaid.hl)" — but no layer for the plate.[^pdk-06]
Rule x.15a confines "Drawn compatible, mask, and waffle-drop layers" to
test modules, the seal ring and the frame, with the exception
"FOM/P1M/Metal waffle drop are allowed inside the die" (flag
P),[^pdk-periph] so a design inside the die draws `hvi`, not `clvom`
(our reading of x.15a).

The *Summary of Key Periphery Rules* uses the mask's name for the drawn
layer. Its Table F3b, "Front end layers (High Voltage Devices)", has a
row for `hvi` with a width of 0.600, 0.700 under "nwell" "spc", 0.180
under the "diff" and "tap" spacing and enclosure columns, 0.700 under
"lvom" "spc", "X" under "lvom" "enc" and "Yes" for manual merge, and it
has no column headed `hvi`.[^pdk-summary] The 0.700 under "lvom" matches
hvi.2a, "Min spacing of Hvi to Hvi", and the 0.700 under "nwell" matches
hvi.5,[^pdk-periph] so we read the table's "lvom" column as the `hvi`
layer itself (inference). Table 2 of *Criteria & Assumptions* names the
space variable `LVOMCDSPCSMC`, a suffix it does not explain.[^pdk-03]

The PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance
criteria for GDS data", has the generic grid, octagonal-edge and x.15a
checks for both `clvom` and a mask-data layer `LVOMmk`, and a
"nikon cross" check, `clvom.nikon`: "LVOMmk in the nikon cross has the
wrong polarity" and "LVOMmk is missing from the nikon cross in the
layout".[^pdk-errors] It words the `hvi` rules as "0.6 min. width of
hvi_peri", "0.7 min. spacing/notch of hvi_peri", "hvi must not overlap
tunm" and "0.7 min. spacing between non-butting hvi and nwell", and
gives no width or spacing check for `clvom` itself.[^pdk-errors]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `LVOM` the site renders layers 75:20 (`hvi`)
and 80:20 (`tunm`) together, with no Boolean expression and no fill
layer, on all eight runs; its mask record gives the mask-level layer
46:0 and the note "LVOM = hvi OR tunm and the SKY130 layer
sheet".[^mask-renders][^pdk-06] The note does not say which sheet it
means, and the site gives no other source. The layers and note are one
public derivation from the drawn data, not SkyWater's mask-generation
recipe. They differ from the index's and the step page's pairing, as the
{ref}`masks index <masks-derivations>` records: the renders show `hvi`
OR `tunm`, where the step page reads the mask as everything outside
`hvi`; since the renders show drawn shapes, not photomask artwork, the
two may describe the same plate in opposite tone (inference), but the
renders also add `tunm`.

The added `tunm` term and the rows of Table F2b above agree in kind —
thick-oxide devices and SONOS transistors in, 1.8 V devices out (our
comparison).[^pdk-06][^mask-renders] Since the site names no source,
that agreement may only mean that both start from the same public PDK
pages, and neither source says in which tone the plate is written.

All 40 rendered dies of every run carry shapes, but that is not 40
designs with 5 V devices: every die carries at least 40 348 shapes, the
minimum on each run being 40 348 (MPW-2 to MPW-5), 40 349 (MPW-6 and
MPW-7), 40 350 (MPW-8) or 53 374 (MPW-1), and on each run 32 to 36 of
the 40 dies carry a count that another die of the run shares — 53 374
on 36 dies of MPW-1 and 53 298 or 53 299 on 26 to 33 dies of each later
run.[^mask-renders] We read the repeated counts as shapes common to the
dies rather than to the projects (inference); the site does not say what
they are. The site states the limits of its images: "These are renders
of *drawn* data, not photomask artwork: reticle pitch, 4x reduction,
mirroring and the frame features the fab adds are not
modelled."[^mask-renders] Its metadata carries no plate ID, so a render
is tied to a plate in the process-steps sheet only by the acronym
`LVOM`, and the MPW-4 renders come from a different reticle set from the
one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `LVOM` plate
as existing on all eight MPW runs, with the plate number `125` on each
and no "Info" note.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA125A` |
| MPW-2 | `5CS8007AC` | `S8007AA125A` |
| MPW-3 | `5CS8008AC` | `S8008AA125A` |
| MPW-4 | `5CS8018AC` | `S8018AA125A` |
| MPW-5 | `5CS8011AC` | `S8011AA125A` |
| MPW-6 | `5CS8014AC` | `S8014AA125A` |
| MPW-7 | `5CS8016AC` | `S8016AA125A` |
| MPW-8 | `5CS8017AC` | `S8017AA125A` |

* **Plate number.** `125` is lower than the numbers of masks printed
  before it — `DNM` (step 7) is `150` and `TUNM` (step 35) `190` — and
  the sheet does not say what the numbers encode, so no process position
  is read from it ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `LVOM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`, whose plates no public
  source lists ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`LVOM <step-044>` page infers an i-line
exposure from the 0.6 µm `hvi` rule; the
{ref}`i-line stepper <machine-i-line-stepper>` page lists it there.
SkyWater lists "ASML I-line stepper" and "ASML I-line scanner" among its
tools but assigns no layer to them.[^skw-01] At NA 0.48, the low end of
ASML's PAS 5500/275D,[^asml-pas5500-275d] the 0.600 µm width has
{math}`k_1 \approx 0.79` (our arithmetic), and Wong et al.'s mask error
factor, which "increases rapidly when the critical dimension (CD) is less
than 0.5 (lambda) /NA for line-space patterns",[^wong-1998] would stay
near unity down to about 0.38 µm at that NA (our arithmetic).

**Resist.** The resist is coated on the fresh thick gate oxide of
{ref}`GOX100 <step-043>`. The {ref}`LVOM <step-044>` page reads about
1 µm of positive i-line resist, the PDK's generic "Photoresist thickness"
being 1.14 µm,[^pdk-03] thick enough to stop the channel implant and to
survive the wet etch, with no anti-reflective coating assumed, and a
firm hard bake to reduce HF penetration along the resist–oxide
interface; it cites Beverina et al. on the "'Resist / Wet Etch' Couple
for Dual Gate Oxide".[^beverina-2003] SkyWater's resist and bake are not
public; the consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Pattern transfer.** Nothing is etched by plasma through this resist.
On the step pages' readings the pattern is used twice:
{ref}`NCHI <step-045>` implants the 1.8 V NMOS channels through the
openings on the {ref}`medium-current implanter <machine-medium-current-implanter>`
class, and {ref}`GOXETCH <step-046>` removes the thick oxide in them in
dilute or buffered HF on the {ref}`wet bench <machine-wet-bench>` class,
with the resist strip and clean treated as part of that etch. The
Cypress patents, which may still be in force, describe the same mask;
their wording is in the collapsed note below this paragraph. The
{ref}`GOXETCH <step-046>` page names thinning of the thick oxide at
trench-isolation edges and at the mask boundary as a known problem of
such an etch. In a dual-gate-oxide process with shallow trench
isolation, Kim et al. found "severe GOX thinning" from 320 Å in the
active area to 79 Å at the STI top edge, with a dent profile, and
prevented it mainly by a thick sidewall oxide with nitride
pullback;[^kim-2002] Lee et al. characterised the thinning at the STI
edge in the dual-gate-oxide process.[^lee-1999-icvc]

:::{dropdown} From patents shown as in force (US 8,093,128, estimated expiry 2028-10-22; US 8,796,098, estimated expiry 2034-02-26) — open to read
The Cypress patents describe the same mask: "a photoresist layer 318 of
FIG. 3D is deposited and patterned to have an opening 319 formed over a
region of the substrate 302 that is to have the next insulator material
and/or insulator layer thickness",[^pat-03] and "a patterned mask layer
242 … includes at least one opening 244 over a channel 218 in the second
region 208", after which "The thick, first gate oxide 240 is etched in
the exposed regions by using a BOE etch".[^pat-04]
:::

**Overlay.** The {ref}`LVOM <step-044>` page reads the mask as aligned to
the trench pattern, with the thick/thin boundary required to land on
field oxide rather than across an active area. The rules that keep it
there are hvdifftap.21, "Diff or tap cannot straddle Hvi", and the
0.180 µm enclosure of HV diffusion by `hvi` and spacing of other
diffusion from it (hvdifftap.22 and hvdifftap.23);[^pdk-periph] we read
the 0.180 µm as the placement margin within which this mask's edge must
fall (inference). ASML specifies "≤ 40 nm" single-machine overlay for the
/275D stepper[^asml-pas5500-275d] (our comparison; SkyWater's budget is
not public).

(mask-lvom-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `LVOM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`LVOM <step-044>`, {ref}`NCHI <step-045>`, {ref}`GOXETCH <step-046>`

* {ref}`LVOM <step-044>` — coats, exposes and develops the resist on the
  thick gate oxide.
* {ref}`NCHI <step-045>` — the 1.8 V NMOS channel implant through the
  openings, before the oxide it passes through is removed.
* {ref}`GOXETCH <step-046>` — strips the thick oxide in the openings; the
  step list used in this reference has no separate strip step, and the
  step page treats the resist strip and clean as part of the etch.

On its step page's reading, the next step, {ref}`LVGOX <step-047>`, grows
the thin gate oxide on the cleared silicon after the resist is gone. The
next mask step is {ref}`RPM <step-049>`, after {ref}`SAGD <step-048>`,
which deposits the amorphous-silicon gate film on its step page's
reading. There is no exception to the rule for this mask.

## Design rules and critical dimensions

The `hvi` rules of the periphery rules, with the rules of the
high-voltage diffusion, poly and N-well sets that bound `hvi` and rule
x.15a; flag P means "Rule applies to periphery only (outside areaid.ce).
A corresponding core rule may or may not exist.".[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| hvi.1 | "Min width of Hvi" (P) | 0.600 µm |
| hvi.2a | "Min spacing of Hvi to Hvi" (P) | 0.700 µm |
| hvi.2b | "Manual merge if space is below minimum" | — |
| hvi.4 | "Hvi must not overlap tunm" | — |
| hvi.5 | "Min space between hvi and nwell (exclude coincident edges)" | 0.700 µm |
| hvnwell.9 | "(Nwell overlapping hvi) must be enclosed by hvi" | — |
| hvdifftap.21 | "Diff or tap cannot straddle Hvi" (P) | — |
| hvdifftap.22 | "Min enclosure of Hdiff or Htap by Hvi. Rule exempted inside UHVI." (P) | 0.180 µm |
| hvdifftap.23 | "Space between diff or tap outside Hvi and Hvi" (P) | 0.180 µm |
| hvpoly.14 | "(poly and diff) cannot straddle Hvi" | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |

Table 2 of *Criteria & Assumptions* gives `LVOMCD` 0.6 and
`LVOMCDSPCSMC` 0.7, the same values as hvi.1 and hvi.2a, and Table F3b
gives `hvi` the same 0.600 and 0.700.[^pdk-03][^pdk-periph][^pdk-summary]
No other row of *Criteria & Assumptions*, including Table 8, "Criteria
for High Voltage FET", names the mask or `hvi`.[^pdk-03] For the plate,
the smallest features are therefore 0.600 µm thick-oxide regions and
0.700 µm gaps between them, below which hvi.2b calls for a manual merge;
whatever the tone, the edges fall between diffusions, 0.180 µm or more
from any active area.

## Related pages

* {ref}`LVOM <step-044>`, {ref}`NCHI <step-045>` and
  {ref}`GOXETCH <step-046>` — the mask step, the channel implant and the
  oxide etch; {ref}`GOX100 <step-043>` and {ref}`LVGOX <step-047>` — the
  thick and thin gate oxidations.
* {ref}`mask-tunm` and {ref}`mask-onom` — the SONOS masks, whose windows
  hvi.4 keeps outside `hvi` and whose islands the resist protects on the
  step page's reading.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the derivations the renders use.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-medium-current-implanter` and {ref}`machine-wet-bench` —
  the implant and wet-etch classes that use the pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography`, {ref}`category-implant` and
  {ref}`category-oxidation` — the mask step, implant and oxidation
  categories.

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Low Voltage Oxide, LVOM,
  X".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `clvom` 46:0
  and 45:20, `hvi` 75:20, the Table C3 definitions and the `LVOM` column
  of Table F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `LVOMCD`/`LVOMCDSPCSMC` and
  the photoresist thickness.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `hvi`, `hvnwell`, `hvdifftap`
  and `hvpoly` rules and function lines, x.15a and the flag
  legend.[^pdk-periph]
* [SkyWater PDK, *Summary of Key Periphery Rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>) — the `hvi` row of
  Table F3b.[^pdk-summary]
* SkyWater PDK, [*Error Messages*](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) page and `errors.csv` — the `hvi`
  messages and the `clvom` and `LVOMmk` checks.[^pdk-errors]
* [SkyWater PDK, *High Voltage Methodology*](<https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>) — the 110 Å gate oxide of the
  high-voltage devices.[^pdk-hv]
* SkyWater PDK, `nfet_01v8` and `nfet_g5v0d10v5` models — the two
  electrical oxide thicknesses.[^pdk-model-nfet01v8][^pdk-model-nfet5v]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the `LVOM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `LVOM` renders, their
  layers and note, and the per-die shape counts.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the i-line exposure
  tools.[^skw-01]
* [ASML, *PAS 5500/275D* data sheet](<https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-275d.pdf>) — NA range and single-machine
  overlay of an i-line stepper.[^asml-pas5500-275d]

:::{dropdown} From patents shown as in force (US 8,093,128, estimated expiry 2028-10-22; US 8,796,098, estimated expiry 2034-02-26) — open to read
* Koutny et al. (Cypress), US 8,093,128 — the gate-insulator mask that
  protects the ONO stack.[^pat-03]
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — the
  dual-gate-oxide mask and its BOE etch.[^pat-04]
:::

### High-level understanding

* [Wikipedia, *Photomask*](<https://en.wikipedia.org/wiki/Photomask>) — reticles, absorbers and
  pellicles.[^wiki-mask]
* [Wikipedia, *Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) — i-line exposure and
  resolution.[^wiki-litho]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]

### Deep dive

* [Diaz et al., VLSI 1999](<https://doi.org/10.1109/VLSIT.1999.799315>) — dual gate oxides for a 1.5–2 V core
  and 3.3 V I/O in a 0.18 µm logic technology.[^diaz-1999]
* [Togo, Noda and Tanigawa (NEC), IEDM 1998](<https://doi.org/10.1109/IEDM.1998.746371>) — multiple-thickness gate
  oxides for logic-embedded DRAM.[^togo-1998]
* [Beverina et al., *Solid State Phenomena* 2003](<https://doi.org/10.4028/www.scientific.net/SSP.92.235>) — the resist and wet
  etch pairing of a dual-gate-oxide mask.[^beverina-2003]
* [Kim et al., *JJAP* 2002](<https://doi.org/10.1143/JJAP.41.2404>) — gate-oxide thinning at the STI edge in a
  dual-gate-oxide process and its prevention.[^kim-2002]
* [Lee et al., ICVC 1999](<https://doi.org/10.1109/ICVC.1999.820895>) — gate-oxide thinning at the edge of shallow
  trench isolation in the dual-gate-oxide process.[^lee-1999-icvc]
* [Lee, *Electrochem. Solid-State Lett.* 1999](<https://doi.org/10.1149/1.1390957>) — a dual-gate-oxide process
  with improved gate-oxide integrity.[^lee-1999]
* [Kim et al., SSDM 2001](<https://doi.org/10.7567/SSDM.2001.A-6-6>) — an STI scheme compensating corner thinning for
  thick dual gate oxides.[^kim-2001]
* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor and the
  size below which it rises.[^wong-1998]
* [ITRS 2001, *Front End Processes*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>) — the gate-stack requirements of the
  130 nm generation.[^itrs-01]
* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — mask magnification and the optical mask
  requirements of the 130 nm generation.[^itrs-03]

## Open questions

* Whether the plate's data are the complement of `hvi`, as the step page
  reads it, or `hvi` and the SONOS regions in the opposite tone, as Table
  F2b's rows and the renders' layers suggest, is not stated in the
  PDK;[^pdk-06][^mask-renders] the renders' note cites an unnamed "layer
  sheet".
* The operation that makes the `clvom` plate data, what the `clvom`
  drawing purpose 45:20 holds and how the ONO islands are treated are
  not published.[^pdk-06]
* The meaning of the suffix of `LVOMCDSPCSMC`, and of Table F3b's use of
  "lvom" as a column heading, is not stated.[^pdk-03][^pdk-summary]
* The plate's tone, blank, absorber and magnification, the resist and
  its bake, and the exposure tool are not public; the i-line reading
  rests on the 0.600 µm rule.
* What the plate number `125` encodes is not stated, and no public source
  lists the `LVOM` plate of the original MPW-4 set
  `5CS8010AC`.[^steps-sheet][^mask-renders]

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tabs "Sheet1" (step number, code and description), "Masks"
    (mask steps with step numbers), "Run Mask IDs" (the mask table set
    against MPW-1 to MPW-8, with "Exists" and "Plate ID" columns per run)
    and "Sheet4" (mask types), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* (including Table C3,
    device, LVS and other CAD definitions, and Table F2b, the mask
    generation table) and `gds_layers.csv`, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (all tables),
    SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-summary]: SkyWater PDK Authors, *Summary of Key Periphery Rules*
    (Table F3b), SkyWater SKY130 PDK documentation, retrieved 2026-09-14.
    <https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^pdk-model-nfet01v8]: SkyWater PDK Authors,
    `sky130_fd_pr__nfet_01v8__tt.pm3.spice` (typical-corner BSIM4
    model, parameter `toxe`), google/skywater-pdk-libs-sky130_fd_pr
    repository.
    <https://raw.githubusercontent.com/google/skywater-pdk-libs-sky130_fd_pr/main/cells/nfet_01v8/sky130_fd_pr__nfet_01v8__tt.pm3.spice>
[^pdk-model-nfet5v]: SkyWater PDK Authors,
    `sky130_fd_pr__nfet_g5v0d10v5__tt.pm3.spice` (typical-corner BSIM4
    model, parameter `toxe`), google/skywater-pdk-libs-sky130_fd_pr
    repository.
    <https://raw.githubusercontent.com/google/skywater-pdk-libs-sky130_fd_pr/main/cells/nfet_g5v0d10v5/sky130_fd_pr__nfet_g5v0d10v5__tt.pm3.spice>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_LVOM/`
    directory with its page, `job.json`, `result.json` and per-die slot
    JSON files, retrieved 2026-09-14. Rendered from the public shuttle
    repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^asml-pas5500-275d]: ASML, *PAS 5500/275D High Productivity i-Line
    Stepper*, refurbished systems data sheet, 2019, accessed 2026-09-13.
    <https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-275d.pdf>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
    Shown as in force; estimated expiry 2028-10-22 (estimate from public
    records, not legal advice).
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098 B1,
    granted 2014-08-05. <https://patents.google.com/patent/US8796098B1/en>
    Shown as in force; estimated expiry 2034-02-26 (estimate from public
    records, not legal advice).
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
[^diaz-1999]: C. H. Diaz, K. L. Young, J. H. Hsu, J. C. H. Lin,
    C. S. Hou et al., "A 0.18 μm CMOS logic technology with dual gate
    oxide and low-k interconnect for high-performance and low-power
    applications", *1999 Symposium on VLSI Technology, Digest of
    Technical Papers*, pp. 11–12.
    <https://doi.org/10.1109/VLSIT.1999.799315>
[^togo-1998]: M. Togo, K. Noda and T. Tanigawa (NEC),
    "Multiple-thickness gate oxide and dual-gate technologies for
    high-performance logic-embedded DRAMs", *IEDM 1998 Technical
    Digest*, pp. 347–350. <https://doi.org/10.1109/IEDM.1998.746371>
[^beverina-2003]: A. Beverina, I. Guilmeau, J. P. Carrere, N. Emonet,
    F. Guyader, V. Huard, S. Petitdidier and R. Velard, "'Resist / Wet
    Etch' Couple for Dual Gate Oxide", *Solid State Phenomena* **92**,
    235–238 (2003). <https://doi.org/10.4028/www.scientific.net/SSP.92.235>
[^kim-2002]: S.-H. Kim, S.-H. Kim, S.-E. Kim, M.-S. Kim, J.-H. Park,
    E.-S. Kim and J.-T. Kim, "Process Design for Preventing the Gate
    Oxide Thinning in the Integration of Dual Gate Oxide Transistor",
    *Japanese Journal of Applied Physics* **41**(4B), 2404–2409 (2002).
    <https://doi.org/10.1143/JJAP.41.2404>
[^lee-1999-icvc]: S.-W. Lee, I. H. Cho, S. H. Park, H. G. Choi,
    N. G. Kim, J.-K. Kim, S. B. Han and K. Lee, "Gate oxide thinning
    effects at the edge of shallow trench isolation in the dual gate
    oxide process", *ICVC '99: 6th International Conference on VLSI
    and CAD*, pp. 249–252. <https://doi.org/10.1109/ICVC.1999.820895>
[^lee-1999]: S.-W. Lee, "Novel Dual Gate Oxide Process with Improved
    Gate Oxide Integrity Reliability", *Electrochemical and Solid-State
    Letters* **3**(1), 56 (1999). <https://doi.org/10.1149/1.1390957>
[^kim-2001]: S.-H. Kim, S.-H. Kim, S.-E. Kim, M.-S. Kim, J.-H. Park and
    E.-S. Kim, "New STI Scheme to Compensate Gate Oxide Thinning at STI
    Corner Edge for the Devices Using Thick Dual Gate Oxide", *Extended
    Abstracts of the 2001 International Conference on Solid State
    Devices and Materials (SSDM)*, 2001.
    <https://doi.org/10.7567/SSDM.2001.A-6-6>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
