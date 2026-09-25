(mask-vim4)=
# VIM4 — Via4

The via-4 mask is the {term}`reticle` that places every connection
between metal 4 and metal 5, the top metal. On the
{ref}`VIM4 <step-159>` page's reading, the resist printed through it at
step 159 is opened in a 0.8 µm square over every drawn `via4`, and the
{ref}`VIM4E <step-160>` etch cuts the holes through the inter-metal
oxide.

| | VIM4 — Via4 |
|---|---|
| Mask step | {ref}`VIM4 <step-159>`, step 159 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Via4", `VIM4`, marked `X` in `Used in SKY130`; "Pad Via", `VIPDM`, unmarked[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cviam4` mask 58:0, "Via 4 mask"; drawing 117:20[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `via4` drawing 71:44, "Contact from metal 4 to metal 5"[^pdk-06] |
| Minimum CD, feature / space | `VIM4CD` 0.8 / `VIM4CDSP` 0.8[^pdk-03] |
| Polarity and tone | Not published. The holes are opened where `via4` is drawn, which with a positive resist would make the plate dark-field (inference). |
| Exposure class | KrF (248 nm), an inference on the step page from the sheet's mask type, with i-line as the alternative the 0.8 µm geometry allows ({ref}`machine-duv-krf-stepper`) |
| Mask type (process-steps sheet) | `B4-248-BIM-LSR-WET`, read on the masks index as a binary mask for 248 nm exposure and, less certainly, 4×[^steps-sheet] |
| Plates recorded | all except MPW-5[^steps-sheet] |
| Plate no. | `585`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-vim4-steps>` |

:::{seealso}
How the
step is performed is on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.
:::

## What the mask defines

The mask is one of three masks, with vias 2 and 3, for which the public
record gives a coded mask type as well as plate IDs on the MPW runs, and the
only one of the three whose type reads as a binary mask. That type
is the reason the step pages read this coarse level as a 248 nm (KrF)
level rather than an i-line one.

The periphery rules give the function of the layer as "Via4 connects
met4 to met5 in the SKY130P\*/SP8P\* flow", and allow one via size: the
"Min and max L and W of via4" is 0.800 µm (via4.1), and "Only min.
square via4s are allowed except die seal ring" (via4.3).[^pdk-periph]
The mask therefore carries a single feature, a 0.8 µm square, repeated
wherever metal 5 meets metal 4; wide connections are arrays of it
(the {ref}`VIM4 <step-159>` page's reading).

On the step pages' readings
the same holes also land on the top plates of the second
{term}`MiM capacitor` ({ref}`CAP2M <step-152>`); the PDK's cross-section
of the stacked capacitor labels `CAP2M`, "Via4", "M5 (plate 1)" and
"M5 (plate 2)".[^pdk-07]

`masks.csv` has a second entry that could be taken for this level,
"Pad Via, `VIPDM`", which is not marked as used in SKY130 and whose
minimum CD, `VIPDMCD` 1.2 / `VIPDMCDSP` 1.27, does not match the via-4
rules.[^pdk-05][^pdk-03][^pdk-periph] The {ref}`VIM4 <step-159>` page therefore describes the `VIM4`
level. The process-steps sheet records
no `VIPDM` plate on any MPW run, and the renders site's `VIPDM` render
reuses the via-3 layer with the note "pad-via flow, not SKY130"
({ref}`masks-index`).[^steps-sheet][^mask-renders]

The mask defines neither the metal-4 landing pads nor the metal-5 lines
that must enclose each via; those are the {ref}`MM4 <step-154>` and
{ref}`MM5 <step-162>` masks. The PDK's mask generation table, Table F2b,
has no via columns, so it says nothing about which devices create
`VIM4`.[^pdk-06]

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `cviam4` a `mask` purpose at 58:0 ("Via 4 mask")
and a `drawing` purpose at 117:20, a layer number that also carries the
`cmm5` waffle drop at 117:4. The drawn layer is `via4` at 71:44,
"Contact from metal 4 to metal 5".[^pdk-06] The pairing rests on the
names and descriptions, as on the {ref}`masks index <masks-index>`, and
the PDK publishes no operation from `via4` to the plate.

Rule x.15a
confines mask layers to test modules, seal ring and frame, and its
exception names only "FOM/P1M/Metal waffle drop" (flag P, periphery
only).[^pdk-periph] So a design inside the die draws `via4` (our reading
of x.15a, which does not say what applies in the core). One row of rule
x.2 limits via3 and via4 to "n x 90" degrees: "Angles permitted on: via3
and via4. Anchors are exempted."[^pdk-periph]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `VIM4` the site renders layer 71:44 alone, with
no Boolean expression and no fill layer, on all eight runs.[^mask-renders] Its mask
record gives the mask-level layer 58:0 and the info text "Via 4
(M4→M5)".[^mask-renders]

That text is identical to the "Info" note of
the `VIM4` row in the process-steps sheet, one of the level names the
two sources share, so neither is cited as corroborating the other
({ref}`masks-renders-sheet-notes`).[^steps-sheet][^mask-renders] The
choice of layer is one public derivation from the drawn data, not
SkyWater's mask-generation recipe.

Every rendered die of every run carries `via4` shapes — at least
229 196 on each die[^mask-renders] — so the count of 40 dies says
nothing about how many projects use via 4 in particular. For MPW-5 the
renders show shapes on all 40 dies although the sheet records no `VIM4`
plate for that run, which fits the masks index's reading of the gap as
one in the record, but the renders show the drawn layouts, not the
plates ({ref}`masks-mpw-runs`).[^mask-renders][^steps-sheet]

The site
states the limits of its images: "These are renders of *drawn* data,
not photomask artwork: reticle pitch, 4x reduction, mirroring and the
frame features the fab adds are not modelled."[^mask-renders] Its
metadata carries no plate ID, and the MPW-4 renders come from a
different reticle set from the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a `VIM4` plate
as existing on seven runs, with the plate number `585` on each, and has
no mark or plate ID for MPW-5.[^steps-sheet] The plate IDs below are the
sheet's; the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA585A` |
| MPW-2 | `5CS8007AC` | `S8007AA585A` |
| MPW-3 | `5CS8008AC` | `S8008AA585A` |
| MPW-4 | `5CS8018AC` | `S8018AA585A` |
| MPW-5 | `5CS8011AC` | none recorded |
| MPW-6 | `5CS8014AC` | `S8014AA585A` |
| MPW-7 | `5CS8016AC` | `S8016AA585A` |
| MPW-8 | `5CS8017AC` | `S8017AA585A` |

* **MPW-5.** The sheet records no plates for `CTM1`, `MM1`, `VIM`,
  `VIM4` and `PDM` on MPW-5 and gives no reason.[^steps-sheet] The masks index reads
  a gap in the record as likelier than a run without these masks, since
  every working die needs them (inference), and does not conclude that
  the plate was absent ({ref}`masks-mpw-runs`).[^steps-sheet]
* **Plate number.** The sheet does not say what `585` encodes; it falls
  between `580` for `MM4` and `590` for `MM5`, but the numbers do not
  follow process order elsewhere (`CAPM` `572` against `MM3` `570`), so
  no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

### The mask-type record

A tab headed "Sheet4" gives a mask type for three masks only, under the
column heading "Mask type": `F4-248-EAPSM-A43-APRX` for `VIM2` and
`VIM3`, and `B4-248-BIM-LSR-WET` for `VIM4`.[^steps-sheet] A further column, "e-beam
spot size", holds 0.02 for `VIM3` and nothing for the other
two.[^steps-sheet] The tab does not define its codes or say to which
runs they apply.

The masks index reads `BIM` as a binary
(chrome-on-quartz) mask and `248` as the exposure wavelength, because
mask makers and the patent literature use those abbreviations, and reads the digit 4, less certainly, as the
4× reduction ratio.[^photronics-abr] A TSMC
patent is titled [*Method for forming binary intensity masks*](<https://patents.google.com/patent/US6379849B1/en>) and
abbreviates them "BIM".[^pat-bim-tsmc]

The index does not read the last two fields, `LSR` and `WET`. We read
them, less certainly still, as a laser-written plate with a wet-etched
absorber (inference from the abbreviations alone). Both are established
options for a plate whose features are large.

A mask maker describes
laser lithography tools as "a lower-cost solution when ultimate
resolution is less critical", and dry etch as what "ensures pattern
fidelity by minimizing CD loss".[^photronics-abr] Laser reticle writers
of the ALTA family served mask makers at the 180 nm and 150 nm
nodes.[^morgante-2000] Chrome masks "have traditionally been wet
etched in an acidic solution of cerric ammonium nitrate", with an
undercut of about 150 nm per edge that is compensated by sizing the
data,[^buck-1994] whereas dry etch was developed for sub-half-micron
features on the plate.[^flack-1993]

At 4×, a 0.8 µm via is a 3.2 µm
square on the plate (our arithmetic), well above those limits. If the
reading is right, the via-4 plate is the simplest kind a mask shop
makes; the sheet does not say so.

## Lithography and pattern transfer

### Exposure class

On geometry alone the level would print on an
i-line tool: the {ref}`VIM4 <step-159>` page gives
{math}`k_1 \approx 1.3` at 365 nm and NA 0.6. The
step page nevertheless reads it as a KrF level, because a reticle made
for 248 nm points to a 248 nm tool, and gives {math}`k_1 \approx 2.3` on
a lens of NA 0.70. The {ref}`KrF stepper <machine-duv-krf-stepper>` page
lists it there, and the {ref}`i-line stepper <machine-i-line-stepper>`
page as an alternative.

SkyWater lists both "ASML DUV stepper" and
"ASML I-line stepper" but assigns no layer to either.[^skw-01] Why a
0.8 µm level has a reticle recorded for 248 nm is not stated.

### Mask errors and mask type

Wong et al. found that the mask error
factor for contacts rises only when the CD falls below 0.75 λ/NA, and
that attenuated phase-shift masks are about as sensitive to mask CD
error as chrome-on-glass masks.[^wong-1998] At 248 nm and NA 0.70 the
threshold is about 0.27 µm (our arithmetic), a third of the via-4 size,
so the plate's CD errors would print about one to one (inference).

Kim
et al. found the same for contact holes on binary and attenuated
masks — a mask error factor of about one for large features, rising
near the resolution limit — with attenuated masks lower there because
of their positive bias.[^kim-1999] On that evidence the attenuated type
recorded for the 0.2 µm vias 2 and 3 would gain little at 0.8 µm, and a
binary plate would suffice (our reading).

Chen, Wang and Chu describe the
process latitude of an attenuated mask in contact-hole
printing.[^chen-1999-psm] ITRS 2001's optical mask requirements, which
are "for critical layers", ask for a mask CD uniformity of 8.0 nm (3σ)
on contacts and vias in the 130 nm year at 4× magnification.[^itrs-03]
No public source gives the via-4 plate's specification.

### Resist and tone

On the KrF reading the resist is a positive
chemically amplified resist,[^ito-2005] and the plate is dark-field:
clear squares in an opaque field (inference from drawing the holes).
Neither is published. The consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

### Overlay and alignment

Metal 4 must enclose the via by 0.190 µm (via4.4) and
metal 5 by 0.310 µm (m5.3).[^pdk-periph] If via 4 is a KrF level and
metal 5 an i-line level, as the machine pages read them, the metal-5
overlay to via 4 is a matched overlay between classes
({ref}`machine-i-line-stepper`).

### Pattern transfer

On the step pages' readings the holes are etched
at {ref}`VIM4E <step-160>` through the cap oxide and inter-metal oxide,
on the {ref}`dielectric plasma etcher <machine-plasma-etcher-dielectric>`
class, down to the metal-4 cap and the `cap2m` plates. On the step pages' readings the resist is
stripped within that step. The next step, {ref}`WTIAL5 <step-161>`,
deposits the metal-5 stack that the step page reads as filling the
holes.

(mask-vim4-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `VIM4` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`VIM4 <step-159>`, {ref}`VIM4E <step-160>`

* {ref}`VIM4 <step-159>` — coats, exposes and develops the resist.
* {ref}`VIM4E <step-160>` — etches the via holes through the resist;
  the step list used in this reference has no separate strip step, and
  the step page treats the resist strip and clean as part of the etch.

The next step, {ref}`WTIAL5 <step-161>`, deposits metal onto the cleaned
holes, and the next mask step is {ref}`MM5 <step-162>`. Unlike vias 1–3,
no liner, tungsten fill or plug polish follows the etch in the step
list, but none of those would use the resist either; the rule needs no
exception for this mask.

## Design rules and critical dimensions

The `via4` rules of the periphery rules, with the metal-5 enclosure;
flag CU means "Rules applicable only to Cu BE flows" and IR "IR drop
check compering Al database and slotted Cu database for the same product
(2 gds files) must be clean".[^pdk-periph]

:::{table} The `via4` rules, with the metal-5 enclosure, as published

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| via4.1 | "Min and max L and W of via4" | 0.800 µm |
| via4.2 | "Spacing of via4 to via4" | 0.800 µm |
| via4.3 | "Only min. square via4s are allowed except die seal ring where via4s are (Via4 CD)\*L" | 0.8\*L |
| via4.4 | "Via4 must be enclosed by Met4 by at least …" | 0.190 µm |
| via4.irdrop.1 | For 1 to 4 via4s "on the same connector" (CU IR) | 0.0 µm |
| via4.irdrop.2 | For 5 to 10 via4s (CU IR) | 0.2 µm |
| via4.irdrop.3 | For 11 to 100 via4s (CU IR) | 0.5 µm |
| via4.irdrop.4 | For more than 100 via4s (CU IR) | 0.8 µm |
| m5.3 | "via4 must be enclosed by met5 by atleast" | 0.310 µm |
| x.2 | "Angles permitted on: via3 and via4. Anchors are exempted." | n x 90 deg |
:::

Table 2 of *Criteria & Assumptions* repeats the size and space, and gives the unmarked pad via:[^pdk-03]

:::{table} Parameters of *Criteria & Assumptions* for the mask and the unmarked pad via, all from Table 2
| Parameter | Published description | Value |
|---|---|---:|
| `VIM4CD` | size | 0.8 |
| `VIM4CDSP` | space | 0.8 |
| `VIPDMCD` | the unmarked pad via | 1.2 |
| `VIPDMCDSP` | the unmarked pad via | 1.27 |
:::

The irdrop rules, flagged
for copper flows, compare "mcon area pre- and post- Cu conversion" in
their published wording although they are via-4 rules; the PDK does not
explain the wording.[^pdk-periph] For the plate, via4.1 to via4.3 are
what matter: one square size on a pitch of 1.6 µm (our arithmetic from
via4.1 and via4.2).

## Related pages

* **Steps.** {ref}`VIM4 <step-159>` and {ref}`VIM4E <step-160>` — the mask step
  and the via etch; {ref}`WTIAL5 <step-161>` — the metal that follows.
* **Category.** {ref}`category-lithography` and {ref}`category-etch` — the mask step
  and etch categories.
* **Machines.** {ref}`machine-duv-krf-stepper` and {ref}`machine-i-line-stepper` — the
  exposure class the step page assigns and its alternative.
  {ref}`machine-plasma-etcher-dielectric` — the etch class that
  transfers the pattern.
* **Materials.** {ref}`material-lithography-materials` — resists, developer and
  reticles.
* **Masks.** {ref}`mask-mm4` and {ref}`mask-mm5` — the metal masks below and above,
  whose lines must enclose the vias.
* **Indexes.** {ref}`masks-index` — every mask's PDK entry, plates, renders and the
  mask-type record for vias 2–4.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

* {ref}`Method for forming binary intensity masks <patent-gp24795638>` — US 6,379,849 B1 (2000)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Via4, VIM4, X" and the
  unmarked "Pad Via, VIPDM".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `via4` 71:44
  and the `cviam4` purposes.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `VIM4CD`/`VIM4CDSP` and
  `VIPDMCD`/`VIPDMCDSP`.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `via4` rules, m5.3, x.2, x.15a
  and the flag legend.[^pdk-periph]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the `VIM4` plates of
  MPW-1 to MPW-8 and the "Sheet4" mask type.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `VIM4` renders, their layer
  and info text.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the DUV and i-line exposure
  tools.[^skw-01]
* [Photronics, *Advanced Binary Reticle*](<https://www.photronics.com/products/advanced-binary-reticle/>) — binary reticles, laser and
  e-beam writing, dry etch and the EAPSM abbreviation.[^photronics-abr]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — the stacked MiM capacitor
  cross-section with `CAP2M` and via 4.[^pdk-07]

### High-level understanding

* [Wikipedia, *Photomask*](<https://en.wikipedia.org/wiki/Photomask>) — binary and phase-shift masks.[^wiki-mask]
* [Wikipedia, *Via (electronics)*](<https://en.wikipedia.org/wiki/Via_(electronics)>) — what a via is.[^wiki-via]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — imaging of
  contact holes.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on masks and
  reticles, overlay and lithography costs.[^levinson-2005]

### Deep dive

* [Lin and Wang (TSMC), US 6,379,849](<https://patents.google.com/patent/US6379849B1/en>) — forming binary intensity masks,
  the "BIM" of the mask-type code.[^pat-bim-tsmc]
* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor of
  contacts and the size below which it rises.[^wong-1998]
* [Kim et al., *Proc. SPIE* 1999](<https://doi.org/10.1117/12.354400>) — mask CD error for contact holes on
  binary and attenuated phase-shift masks.[^kim-1999]
* [Chen, Wang and Chu, *Proc. SPIE* 1999](<https://doi.org/10.1117/12.354399>) — attenuated phase-shift masks
  for contact holes, the type recorded for vias 2 and
  3.[^chen-1999-psm]
* [Morgante and Hamaker, *Proc. SPIE* 2000](<https://doi.org/10.1117/12.392079>) — a laser reticle writer and
  the mask nodes it served.[^morgante-2000]
* [Buck and Grenon, *Proc. SPIE* 1994](<https://doi.org/10.1117/12.167247>) — wet against dry chrome etching of
  masks, undercut and its compensation.[^buck-1994]
* [Flack, Tokunaga and Edwards, *Proc. SPIE* 1993](<https://doi.org/10.1117/12.142153>) — chrome dry etching
  for sub-half-micron reticle features.[^flack-1993]
* [Rizvi (ed.), *Handbook of Photomask Manufacturing Technology*](<https://doi.org/10.1201/9781420028782>) — laser
  mask writers, conventional optical masks and mask
  processing.[^rizvi-2005]
* [Ito, *Adv. Polym. Sci.* 2005](<https://doi.org/10.1007/b97574>) — the chemically amplified resists of
  248 nm exposure.[^ito-2005]
* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — mask magnification and the optical mask
  requirements for critical layers at 130 nm.[^itrs-03]

## Open questions

* The "Sheet4" codes are not defined in the sheet.

  The binary and 248 nm
  readings rest on common abbreviations, the 4× reading is less certain,
  and the laser-written and wet-etched reading of `LSR` and `WET` less
  certain still. The tab does not say to which runs the type applies or
  what its "e-beam spot size" column, and its unit, mean.[^steps-sheet]
* Why a 0.8 µm via level has a mask type for 248 nm, and whether it is
  exposed on a KrF or an i-line tool, is not public; nor are the tone,
  the resist or the plate's CD specification.
* Whether the absent MPW-5 record is a gap in the record or a difference
  in the run is not stated,[^steps-sheet] and no public source lists the `VIM4` plate of
  the original MPW-4 set `5CS8010AC`.[^mask-renders]
* The PDK publishes no operation from `via4` to the `cviam4` plate data,
  and does not say what the `cviam4` drawing purpose at 117:20 is
  for.[^pdk-06]
* The irdrop rules' "mcon" wording is not explained.[^pdk-periph]

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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Table 2),
    SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (MiM capacitors),
    SkyWater SKY130 PDK documentation, and the `cap_mim` cross-section
    drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/cap_mim/cross-section-cap_mim.svg>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_VIM4/`
    directory with its page, `job.json`, `result.json` and per-die slot
    JSON files, retrieved 2026-09-14. Rendered from the public shuttle
    repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^photronics-abr]: Photronics, Inc., *Advanced Binary Reticle*, product
    page, retrieved 2026-09-13.
    <https://www.photronics.com/products/advanced-binary-reticle/>
[^pat-bim-tsmc]: S.-J. Lin and W.-C. Wang (Taiwan Semiconductor
    Manufacturing Co.), *Method for forming binary intensity masks*,
    US 6,379,849 B1, filed 2000-10-26, granted 2002-04-30.
    <https://patents.google.com/patent/US6379849B1/en>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-via]: Wikipedia, *Via (electronics)*.
    <https://en.wikipedia.org/wiki/Via_(electronics)>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
[^kim-1999]: H.-E. Kim, J.-S. Chun, S. Barnett and J. Shih, "Effect of
    mask critical dimension error for subquarter-micron contact hole",
    *Proc. SPIE* **3679**, 821 (1999).
    <https://doi.org/10.1117/12.354400>
[^chen-1999-psm]: Y.-T. Chen, Y.-C. Wang and R. Chu, "Optimization of
    attenuated phase-shift mask for contact hole printing", *Proc.
    SPIE* **3679**, Optical Microlithography XII, 812 (1999).
    <https://doi.org/10.1117/12.354399>
[^morgante-2000]: C. G. Morgante and H. C. Hamaker, "ALTA 3700:
    extending the application space of the ALTA 3500 laser reticle
    writer", *Proc. SPIE* **4066**, 613 (2000).
    <https://doi.org/10.1117/12.392079>
[^buck-1994]: P. D. Buck and B. J. Grenon, "Comparison of wet and dry
    chrome etching with the CORE-2564", *Proc. SPIE* **2087**, 42–49
    (1994). <https://doi.org/10.1117/12.167247>
[^flack-1993]: W. W. Flack, K. E. Tokunaga and K. D. Edwards, "Chrome
    dry-etching for photomask fabrication", *Proc. SPIE* **1809**, 85
    (1993). <https://doi.org/10.1117/12.142153>
[^rizvi-2005]: S. Rizvi (ed.), *Handbook of Photomask Manufacturing
    Technology*, CRC Press, 2005, ISBN 978-1-4200-2878-2.
    <https://doi.org/10.1201/9781420028782>
[^ito-2005]: H. Ito, "Chemical Amplification Resists for
    Microlithography", *Advances in Polymer Science* **172**, 37–245
    (2005). <https://doi.org/10.1007/b97574>
