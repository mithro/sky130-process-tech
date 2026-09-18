(mask-pwbm)=
# PWBM — P-Well Block Mask

The P-well block mask is the {term}`reticle` that, on the step pages'
reading, keeps SKY130's P-well implant out of the places that must not
receive it: the resist printed through it at {ref}`PWBM <step-026>`
remains over the N-wells and over the special 20 V regions drawn as
`pwbm`, the boron well implants {ref}`PWI <step-027>` and
{ref}`PWI2 <step-028>` go into all the silicon it leaves open, and the
resist is stripped at {ref}`PWIS <step-029>`. It is the mask of this
reference whose public record is thinnest and most at odds with itself:
`masks.csv` does not mark it as used, the process-steps sheet records
plates for it on only two of the eight MPW runs, and no rendered die of
any run draws the layer the renders use for it. This page gathers what
public sources say about the mask itself — its PDK entry and layers, the
plates the process-steps sheet records, what the public renders show,
the lithography it needs and the rules that constrain it — and reports
the gaps without drawing conclusions from them. How the step is performed
is on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | PWBM — P-Well Block Mask |
|---|---|
| Mask step | {ref}`PWBM <step-026>`, step 26 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "P-Well Block Mask", `PWBM`, unmarked[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | none[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `pwbm` drawing 19:44, "Regions (in UHVI) blocked from p-well implant (DE MOS devices only)", with `nwell` drawing 64:20, "N-well region" — the pairing with `nwell` is an inference of the step page[^pdk-06] |
| Minimum CD, feature / space | `PWBMCD` 0.84 / `PWBMCDSP` 1.27[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist remains over `nwell` and `pwbm` and is removed elsewhere, which with a positive resist would put the absorber over those regions (inference). |
| Exposure class | i-line, an inference on the step page from the N-well outlines the plate would carry (0.840 µm width, 1.270 µm space); no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | MPW-6 and MPW-8[^steps-sheet] |
| Plate no. | `024`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 0 on every run[^mask-renders] |
| Steps that use the pattern | 4 steps; see {ref}`Steps that use this mask <mask-pwbm-steps>` |

## What the mask defines

The PDK has no drawn P-well layer: `gds_layers.csv` lists `pwell` only
with `resistor`, `label`, `pin` and `cut` purposes, and Table C3 of the
*Layers Reference* defines `pwell` as "NOT nwell (default substrate
area)".[^pdk-06] The drawn layer that carries this mask's name is
`pwbm`, "Regions (in UHVI) blocked from p-well implant (DE MOS devices
only)", whose rule set's function line is "Define p-well
block".[^pdk-06][^pdk-periph] The {ref}`PWBM <step-026>` page puts the
two together and infers a plate generated from `nwell` together with
`pwbm`, so that the P-well goes everywhere except into N-wells and the
20 V regions; the masks index records that pairing as an inference.
Harris's twin-well patent shows the older alternative, a photoresist
patterned to expose the region "adjacent to N-type well
17",[^pat-twin-harris] and Combs's retrograde P-well used a single
high-energy boron implant to form a shallow, low-resistance well with a
self-aligned channel stop.[^combs-1981]

The device that needs the block most visibly is the 20 V zero-Vt NMOS,
which "has p-well and all Vt implants blocked to achieve a zero
VT".[^pdk-07] The PDK's mask generation table, Table F2b, marks the
`PWBM` column `C` ("CREATED") in 6 of its 80 device rows: the five UHV
5/20 V drain-extended rows (NMOS, isolated NMOS, native NMOS, isolated
native NMOS and PMOS) and one of its two "Psub-Deep Nwell Diode"
rows.[^pdk-06] That diode appears again in rule ulvt-.2, "areaid.low_vt
must enclose pwbm.dg for the UHV dnw-psub diode texted
"condiodeHvPsub"", in a rule set whose function is "Identify
dnwdiodehv_Psub(BV~60V)".[^pdk-periph] Table F2b marks `-` for `PWBM`
in every other row, including the standard 1.8 V and 5 V NMOS whose
P-well the block would, on the step page's reading, leave
open.[^pdk-06] The table records created shapes, so on it the plate is
tied to the 20 V devices; it does not mark the N-well regions that the
step page's reading also puts on the plate (our reading of the table).
Tee et al. describe the opposite choice in another process — using the
baseline P-well implant in a high-voltage LDNMOS "to avoid an additional
mask and process step".[^tee-2010]

The SKY130 {term}`test tile`'s pad documentation names one 20 V zero-Vt
structure `n20zvtvhv1`, "w/l=30/5.5; m=2", with the cell name
`s8defet_ccgx_hvn_nw_dnw_native_sti_2p0_nopw_L5p0_W60`;[^raw-data-testtile-pads]
the pad list does not explain the name. The {ref}`PWBM <step-026>`
page's analysis of that structure's published measurements finds an
effective body doping far below the P-well peak.

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` has no mask-level (`c…`) layer for this mask; the drawn
layer is `pwbm` at 19:44, and `nwell` is at 64:20.[^pdk-06] `masks.csv`
lists "P-Well Block Mask, PWBM" with the `Used in SKY130` field
blank,[^pdk-05] which the {ref}`PWBM <step-026>` page treats as a
documentation inconsistency, since the layer, its rules and the 20 V
devices that depend on it exist. Table 2 of *Criteria & Assumptions*
gives `PWBMCD` 0.84 and `PWBMCDSP` 1.27, the same values as `NWMCD` and
`NWMCDSP`;[^pdk-03] we read the match as consistent with a plate whose
smallest features are N-well outlines (inference; the table does not
say so), though `PWDEM`, which the step pages do not pair with `nwell`,
has the same pair, so the values may be a common well-mask minimum. The
periphery rules give no values for `pwbm` ("N/A"),[^pdk-periph] but the
PDK's *Error Messages* page, which describes "many of the automated DRC
rules that are checked by SkyWater as part of the acceptance criteria
for GDS data", gives `pwbm.5` as "0.84 min. spacing of pwbm_holes" and
`rpm.10` as "2 min. spacing of rpmNotXmt & pwbm".[^pdk-errors] The PDK
publishes no operation that combines `nwell` and `pwbm` into a
plate.[^pdk-periph]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `PWBM` the site renders layer 19:44 (`pwbm`)
alone, with no Boolean expression, no fill layer, no mask-level layer
and no note, and records the mask as not used in SKY130.[^mask-renders]
The render has no `nwell` term, unlike the index's and the step page's
pairing ({ref}`masks-derivations`). The choice of layer is one public
derivation from the drawn data, not SkyWater's mask-generation recipe,
and neither source settles which is right.

No rendered die on any of the eight runs draws `pwbm`: every image is
empty, including those of MPW-6 and MPW-8, the two runs for which the
sheet records a plate.[^mask-renders][^steps-sheet] The site says that
"Empty images are real results - several masks are used by no project on
a given shuttle", and states the limits of its images: "These are
renders of *drawn* data, not photomask artwork: reticle pitch, 4x
reduction, mirroring and the frame features the fab adds are not
modelled."[^mask-renders] The renders therefore cannot show what the
MPW-6 and MPW-8 plates carry, and on the step page's reading, in which
the plate also covers N-wells, a render of `pwbm` alone would be empty
even for a plate with shapes (inference). The site's metadata carries no
plate ID, and the MPW-4 renders come from a different reticle set from
the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a `PWBM` plate
as existing on MPW-6 and MPW-8 only, with the plate number `024` on
both, and has no mark or plate ID for the other six runs and no "Info"
note.[^steps-sheet] The plate IDs below are the sheet's; the reticle set
is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | none recorded |
| MPW-2 | `5CS8007AC` | none recorded |
| MPW-3 | `5CS8008AC` | none recorded |
| MPW-4 | `5CS8018AC` | none recorded |
| MPW-5 | `5CS8011AC` | none recorded |
| MPW-6 | `5CS8014AC` | `S8014AA024A` |
| MPW-7 | `5CS8016AC` | none recorded |
| MPW-8 | `5CS8017AC` | `S8017AA024A` |

* **Partial record.** The sheet records `PWBM` plates for MPW-6 and
  MPW-8 only and does not say why the plates for the two P-well masks
  are recorded for only some runs ({ref}`masks-mpw-runs`).[^steps-sheet]
  This page reports what is recorded and does not conclude that the
  mask was absent from the other six runs: the gap may be in the record
  rather than in the runs (inference: on the step pages' reading the
  P-well implants of every wafer go through this mask's resist).
* **No drawn shapes.** No rendered die on any run draws `pwbm`, the
  layer the renders use for this mask, so the renders neither show use
  of the mask on MPW-6 and MPW-8 nor its absence elsewhere, and this
  page does not read the two recorded plates as evidence that any
  project used the 20 V devices.[^mask-renders][^steps-sheet]
* **Plate number.** `024` lies between `020` for `FOM` and `026` for
  `PWDEM`, and a few numbers above `010` for `NWM`; the numbers do not
  follow process order elsewhere, and the sheet does not say what they
  encode, so no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `PWBM`,[^steps-sheet] and no public source gives this
  plate's blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]

## Lithography and pattern transfer

**Exposure class.** The {ref}`PWBM <step-026>` page notes that the
`pwbm` rules carry no minimum width and takes the N-well outlines as the
plate's tightest features — 0.840 µm width and 1.270 µm space, with
{math}`k_1 \approx 1.4` at NA 0.6 — and infers an i-line level; the
{ref}`i-line stepper <machine-i-line-stepper>` page lists it there.
SkyWater lists "ASML I-line stepper" and "ASML I-line scanner" among its
tools but assigns no layer to them.[^skw-01] Wong et al.'s mask error
factor "is unity for large features, but increases rapidly when the
critical dimension (CD) is less than 0.5 (lambda) /NA for line-space
patterns";[^wong-1998] at 365 nm and NA 0.48 that is about 0.38 µm (our
arithmetic), far below these features.

**Resist.** The resist must stop the P-well boron wherever the plate
leaves it. The {ref}`PWBM <step-026>` page reads a resist of roughly
2 µm from published examples. An IBM retrograde-well patent masks its
phosphorus N-well implants of up to 850 keV with resist "typically
1800–2500 nm in thickness", but implants its 550 keV P-well boron
through a 200 nm polysilicon mask, which it says substantially
eliminates boron scattering, and uses a resist of the same thickness
only for its 150 keV and 45 keV boron;[^pat-well-ibm] Hook et al. model a
"2.3 µm-thick pwell mask",[^hook-2003] and a Zilog patent needs at least
3.4 µm for a 600–800 keV P-well.[^pat-resist-zilog] The PDK's P-well
peak at 0.42 µm (Table 3a) implies lower energies than the deepest of
those examples (inference).[^pdk-03] The ion
range that sets the thickness is what SRIM computes,[^ziegler-2010] and
Lee et al. measured the outgassing of thick resists under MeV
implantation.[^lee-1996] SkyWater's resist and its thickness are not
public. The consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Resist edges.** Ions scattered from the resist edge shift the
threshold of transistors near the well boundary, "of up to 100 mV …
over a lateral distance on the order of a micrometer";[^hook-2003] the
{ref}`PWBM <step-026>` page notes that for P-well edges the shift raises
the NMOS threshold. Sheu et al. model the effect.[^sheu-2006]

**Pattern transfer.** Nothing is etched through this resist. On the
step pages' readings the pattern is transferred into the silicon as
dopant by {ref}`PWI <step-027>` and {ref}`PWI2 <step-028>` on the
{ref}`high-energy implanter <machine-high-energy-implanter>` or
{ref}`medium-current implanter <machine-medium-current-implanter>`
class, and the resist is removed at {ref}`PWIS <step-029>` on the
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` and
{ref}`wet bench <machine-wet-bench>` classes. The PDK gives the result:
a "p-well peak concentration" of 4E+017 cm⁻³ at a "p-well peak
coordinate" of 0.42 µm, a "y.char" of 0.13 µm and a "min. p-well width
to guarantee 90 % peak concentr." of 0.33 µm (Table 3a), and a P-well
vertical dimension of 0.75 µm (Table 3b).[^pdk-03] A Hynix twin-well
patent gives a contemporaneous three-energy boron P-well, 350, 150 and
80 keV.[^pat-well-hynix]

**Overlay.** The {ref}`PWBM <step-026>` page reads `PWBM` and
{ref}`NWM <step-017>` as registering to the same trench marks, so that
their mutual overlay sets the N-well/P-well junction, which Table 3b
places 0.034 µm from the drawn edge ("N-w/P-w junction (from drawn
edge)").[^pdk-03] Rubin, Morris and Jasper describe how retrograde-well
implant control sets the narrow n+/p+ isolation.[^rubin-2002] If the
plate carries the N-well outlines, as the step page reads it, the two
well masks print the same edges in opposite tone (our reading).

(mask-pwbm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `PWBM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`PWBM <step-026>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`PWIS <step-029>`

* {ref}`PWBM <step-026>` — coats, exposes and develops the thick block
  resist.
* {ref}`PWI <step-027>` — the high-energy boron P-well implant into the
  open regions.
* {ref}`PWI2 <step-028>` — the second P-well implant, a second energy on
  its page's reading, through the same resist.
* {ref}`PWIS <step-029>` — strips the implanted resist and cleans the
  wafer.

The next step, {ref}`PWDEM <step-030>`, is itself the next mask step:
on its step page's reading it prints the drain-extended P-well mask
that puts a lighter P-well back into part of the regions blocked here.
No step between `PWIS` and it uses the `PWBM` resist, and there is no
exception to the rule for this mask.

## Design rules and critical dimensions

The `pwbm` rules of the periphery rules, with the rules of other layers
that name `pwbm`; the periphery rules give no values ("N/A"), but the
Error Messages page's messages give some (after the table).[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| pwbm.1 | "Min width of pwbm.dg" | N/A |
| pwbm.2 | "Min spacing between two pwbm.dg inside UHVI" | N/A |
| pwbm.3 | "Min enclosure of dnwell:dg by pwbm.dg inside UHVI (exempt pwbm hole inside dnwell)" | N/A |
| pwbm.4 | "dnwell inside UHVI must be enclosed by pwbm (exempt pwbm hole inside dnwell)" | N/A |
| pwbm.5 | "Min Space between two pwbm holes inside UHVI" | N/A |
| pwdem.3 | "Min enclosure of pwdem:dg by pwbm.dg inside UHVI" | N/A |
| uhvi.3.- | "pwbm.dg must be enclosed by UHVI (exempt inside areaid.lw)" | N/A |
| hvdifftap.26 | "Min spacing between pwbm to difftap outside UHVI" | N/A |
| rpm.10 | "Min spacing of rpm to pwbm" | N/A |
| rpm.11 | "rpm should not overlap or straddle pwbm except cells […]" | N/A |
| ulvt-.2 | "areaid.low_vt must enclose pwbm.dg for the UHV dnw-psub diode texted "condiodeHvPsub"" | NA |

The Error Messages page's messages give values for two of these rules:
`pwbm.5`, "0.84 min. spacing of pwbm_holes", and `rpm.10`, "2 min.
spacing of rpmNotXmt & pwbm" (with "rpmNotXmt must not overlap
pwbm").[^pdk-errors] Table 2 of *Criteria & Assumptions* gives `PWBMCD`
0.84 and `PWBMCDSP` 1.27.[^pdk-03] Table 3d gives punch-through spacings
of "p+ in nwell to pwell" 0.05 µm (`PPTS`) and "n+ in pwell to nwell"
0.15 µm (`PNPTS`), and Table 7 a "spacing of p-well outside deep n-well
to deep n-well mask edge" of 0.12 (`NWDNWENCL`) and a "p-well in deep
n-well to p-sub" of 1.2 (`NWDNWOL`).[^pdk-03] The test tile's pad
documentation has "Pwell to Pwell Isolation in DNW" structures at spaces
of 1.40, 1.20, 1.00 and 0.84 µm.[^raw-data-testtile-pads] None of these
is stated as a rule for this mask; for the plate on the step page's
reading, the N-well rules nwell.1 and nwell.2a would set the smallest
features (inference).

## Related pages

* {ref}`PWBM <step-026>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`
  and {ref}`PWIS <step-029>` — the mask step, the two implants and the
  strip.
* {ref}`mask-nwm` — the N-well mask, whose drawn layer the step page
  pairs with this mask.
* {ref}`mask-pwdem` — the drain-extended P-well mask, which puts a
  lighter P-well back into part of the blocked regions.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the partial plate record of the two P-well masks.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-high-energy-implanter` — the implant class that uses
  the pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography` and {ref}`category-implant` — the mask
  step and implant categories.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,247,199 A <patent-gp27357991>` — Process for forming twin well CMOS integrated circuits (1986)
* {ref}`US 6,455,402 B2 <patent-gp19572018>` — Method of forming retrograde doping file in twin well CMOS device (1999)
* {ref}`US 6,576,405 B1 <patent-gp23358573>` — High aspect ratio photolithographic method for high energy implantation (1999)
* {ref}`US 6,667,205 B2 <patent-gp29214361>` — Method of forming retrograde n-well and p-well (2002)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "P-Well Block Mask,
  PWBM" with the `Used in SKY130` field blank.[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `pwbm`,
  `nwell`, the `pwell` definition of Table C3 and the `PWBM` column of
  Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `PWBMCD`/`PWBMCDSP` and the
  P-well profile, junction and spacing criteria.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `pwbm` rules and function line
  and the rules of other layers that name `pwbm`.[^pdk-periph]
* SkyWater PDK, *Error Messages* page and `errors.csv` — the values in
  the `pwbm.5` and `rpm.10` messages.[^pdk-errors]
* SkyWater PDK, *Device Details* — the 20 V zero-Vt NMOS with its P-well
  blocked.[^pdk-07]
* SkyWater PDK Authors, test-tile pad documentation — the 20 V zero-Vt
  structure and the P-well isolation structures.[^raw-data-testtile-pads]
* *S8 / SKY130 Process Steps* sheet — the step and the `PWBM` plates of
  MPW-6 and MPW-8.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the empty `PWBM` renders and
  their layer.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the i-line exposure
  tools.[^skw-01]

### High-level understanding

* Wikipedia, *CMOS* — NMOS on the p-substrate, PMOS in an
  N-well.[^wiki-cmos]
* Wikipedia, *Ion implantation* — masking, range and
  energy.[^wiki-implant]
* Wikipedia, *Photomask* — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  implant masking by resist.[^txt-02]

### Deep dive

* Combs, IEDM 1981 — a retrograde P-well from a single high-energy boron
  implant.[^combs-1981]
* Rung, Dell'Oca and Walker, *IEEE TED* 1981 — the retrograde well and
  the device spacing it allows.[^rung-1981]
* Matlock (Harris), US 5,247,199 — twin wells with a patterned P-well
  implant resist.[^pat-twin-harris]
* Breitwisch, Lam and Slinkman (IBM), US 6,667,205 — retrograde wells
  with resist thickness and boron energies.[^pat-well-ibm]
* Lee and Son (Hynix), US 6,455,402 — a three-energy boron
  P-well.[^pat-well-hynix]
* Tee et al., ICEDSA 2010 — the baseline P-well implant used in a
  high-voltage LDNMOS to avoid an extra mask.[^tee-2010]
* Buffat and Adams (Zilog), US 6,576,405 — resist thickness for MeV
  well implants.[^pat-resist-zilog]
* Hook et al., *IEEE TED* 2003 — ions scattered from the resist edge and
  the threshold shifts they cause.[^hook-2003]
* Sheu et al., *IEEE TED* 2006 — a compact model of the well-edge
  proximity effect.[^sheu-2006]
* Rubin, Morris and Jasper, IIT 2002 — retrograde-well implant control
  and narrow n+/p+ isolation.[^rubin-2002]
* Lee et al., IIT 1996 — thick-resist outgassing during MeV
  implantation.[^lee-1996]
* Ziegler, Ziegler and Biersack, *NIM B* 2010 — SRIM, for the ion range
  in resist.[^ziegler-2010]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  size below which it rises.[^wong-1998]

## Open questions

* `masks.csv` leaves the `Used in SKY130` field blank for `PWBM`
  although the layer, its rules and the 20 V devices that need it
  exist;[^pdk-05][^pdk-06][^pdk-periph] the PDK does not explain the
  blank.
* Whether the plate is generated from `nwell` and `pwbm` together, as the
  step page infers, or from `pwbm` alone, as the renders use it and as
  Table F2b's `C` marks might suggest, is not
  public.[^pdk-06][^mask-renders]
* The sheet records plates for MPW-6 and MPW-8 only and does not say
  why;[^steps-sheet] whether the other runs had a plate is not public,
  and no rendered die draws `pwbm`, so the renders cannot
  tell.[^mask-renders]
* The periphery rules publish no values for `pwbm`; the Error Messages
  page gives 0.84 for the spacing of `pwbm` holes but no minimum width,
  so the plate's minimum features under the `pwbm` part are not fully
  stated.[^pdk-periph][^pdk-errors]
* The plate's tone, blank, absorber and magnification, the resist and
  its thickness, and the exposure tool are not public.
* What the plate number `024` encodes is not stated.[^steps-sheet]

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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 3a,
    3b, 3d and 7), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_PWBM/`
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
[^wiki-cmos]: Wikipedia, *CMOS*. <https://en.wikipedia.org/wiki/CMOS>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^combs-1981]: S. R. Combs, "Scaleable retrograde p-well CMOS
    technology", *1981 International Electron Devices Meeting*,
    pp. 346–349. <https://doi.org/10.1109/IEDM.1981.190084>
[^rung-1981]: R. D. Rung, C. J. Dell'Oca and L. G. Walker, "A
    retrograde p-well for higher density CMOS", *IEEE Transactions on
    Electron Devices* **28**(10), 1115–1119 (1981).
    <https://doi.org/10.1109/T-ED.1981.20498>
[^pat-twin-harris]: D. A. Matlock (Harris Corporation), *Process for
    forming twin well CMOS integrated circuits*, US 5,247,199 A, granted
    1993-09-21. <https://patents.google.com/patent/US5247199A/en>
[^pat-well-ibm]: M. J. Breitwisch, C. H. Lam and J. A. Slinkman (IBM),
    *Method of forming retrograde n-well and p-well*, US 6,667,205 B2,
    granted 2003-12-23. <https://patents.google.com/patent/US6667205B2/en>
[^pat-well-hynix]: J.-H. Lee and J.-H. Son (Hyundai/Hynix), *Method of
    forming retrograde doping profile in twin well CMOS device*,
    US 6,455,402 B2, granted 2002-09-24.
    <https://patents.google.com/patent/US6455402B2/en>
[^tee-2010]: E. K. C. Tee, D. K. Pal, S. H. Tia and Y. H. Hu, "High
    voltage NMOS double hump prevention by using baseline CMOS p-well
    implant", *2010 International Conference on Electronic Devices,
    Systems and Applications*, pp. 289–293.
    <https://doi.org/10.1109/ICEDSA.2010.5503059>
[^pat-resist-zilog]: S. J. Buffat and J. L. Adams (Zilog), *High aspect
    ratio photolithographic method for high energy implantation*, US
    6,576,405 B1, granted 2003-06-10.
    <https://patents.google.com/patent/US6576405B1/en>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices* **50**(9),
    1946–1951 (2003). <https://doi.org/10.1109/TED.2003.815371>
[^sheu-2006]: Y.-M. Sheu, K.-W. Su, S. Tian, S.-J. Yang, C.-C. Wang,
    M.-J. Chen and S. Liu, "Modeling the Well-Edge Proximity Effect in
    Highly Scaled MOSFETs", *IEEE Transactions on Electron Devices*
    **53**(11), 2792–2798 (2006). <https://doi.org/10.1109/TED.2006.884070>
[^rubin-2002]: L. M. Rubin, W. Morris and C. Jasper, "Process control
    issues for retrograde well implants for narrow n+/p+ isolation in
    CMOS", *2002 International Conference on Ion Implantation
    Technology*, pp. 17–20. <https://doi.org/10.1109/IIT.2002.1257927>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^ziegler-2010]: J. F. Ziegler, M. D. Ziegler and J. P. Biersack, "SRIM
    – The stopping and range of ions in matter (2010)", *Nuclear
    Instruments and Methods in Physics Research B* **268**(11–12),
    1818–1823 (2010). <https://doi.org/10.1016/j.nimb.2010.02.091>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
