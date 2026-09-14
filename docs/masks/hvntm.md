(mask-hvntm)=
# HVNTM — High Volt. N-tip

The high-voltage N-tip mask is the {term}`reticle` of the second tip
implant of SKY130: on the {ref}`HVNTM <step-068>` page's reading, the
thin resist printed through it at step 68 exposes the high-voltage NMOS
transistors on the thick gate oxide and covers everything else, the
arsenic implant {ref}`HVASTI <step-069>` arrives through the openings at
a steep tilt to form their graded drain {term}`extension`, and the resist
is stripped at {ref}`HVASTIS <step-070>`. It is an implant
{term}`block mask`, and the only mask for which the PDK both states an
operation — the drawn layer "will be OR-ed with the CL" — and publishes a
resist thickness, 0.3 µm, well below the generic figure. Because the beam
arrives at 40°, the resist wall's shadow is as much a design parameter as
the openings themselves. This page gathers what public sources say about
the mask itself — its PDK entry and layers, the plates the process-steps
sheet records for the MPW runs, what the public renders of those runs
show, the lithography it needs and the rules that constrain it. How the
step is performed is on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | HVNTM — High Volt. N-tip |
|---|---|
| Mask step | {ref}`HVNTM <step-068>`, step 68 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "High Volt. N-tip", `HVNTM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `chvntm` mask 39:0, "High voltage N-tip implant mask"; drawing 38:20, without a description[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `hvntm` drawing 125:20, "High voltage N-tip implant"; "OR-ed with the CL" (the `hvntm` rules)[^pdk-06][^pdk-periph] |
| Minimum CD, feature / space | `HVNTMCD` 0.7 / `HVNTMCDSP` 0.7[^pdk-03] |
| Polarity and tone | Not published. The step page reads the resist as opened over the high-voltage NMOS; the drawn layer "Defines tip implants", and the `chvntm` checks keep the created layer over n+ diffusion inside `hvi` and off p+ diffusion and taps, so the data mark the openings (our reading); with a positive resist the plate would be clear over them (inference). |
| Exposure class | i-line, an inference on the step page from the 0.7 µm width and space; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `257`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 3 steps; see {ref}`Steps that use this mask <mask-hvntm-steps>` |

## What the mask defines

The periphery rules head the `hvntm` rule set with its function,
"Defines tip implants for the HV NMOS", and the layer table describes
`hvntm` as "High voltage N-tip implant".[^pdk-periph][^pdk-06] The rules
tie it to the thick-oxide layer `hvi`, "High voltage (5.0V) thick oxide
gate regions": "Hvntm must overlap hvi" (hvntm.10), n+ diffusion inside
`hvi` must be enclosed by it (hvntm.3), and n+ diffusion outside `hvi`,
p+ diffusion and p+ taps must stay 0.185 µm clear (hvntm.4 to
hvntm.6a).[^pdk-periph][^pdk-06] It is kept out of the SRAM core ("Hvntm
must not overlap areaid.ce", hvntm.9) and must enclose an
`ESD_nwell_tap` inside `hvi` (hvntm.7).[^pdk-periph] The
{ref}`HVNTM <step-068>` page reads the devices as the 5 V NMOS family on
the 110 Å oxide, which the PDK's *High Voltage Methodology* page says all
VHV devices share with the "standard 5.0V Vcc devices".[^pdk-hv]

The PDK's mask generation table, Table F2b, marks the `HVNTM` column `C`
("CREATED") in 12 of its 80 device rows: the HV n-diffusion resistor,
the HV varactor, the 5/10.5 V NMOS, the 5 V and 3 V native NMOS, the
16 V drain-extended NMOS, the HV, RF ESD HV, RF ESD deep-N-well and
native n-type diodes, and the HV and HV native ESD NMOS.[^pdk-06] It marks
`-`, "Layer not created for the device", in 46 rows, among them every
1.8 V row, the SONOS and flash pass-gate rows, the 5/10.5 V and 16 V
PMOS and the five UHV 5/20 V drain-extended rows.[^pdk-06] On our reading
the created shapes follow the n-type devices on thick oxide up to the
16 V class, and the table does not say why the UHV NMOS rows are left
out. The two `C` rows for native NMOS match the step page's reading that
the native 5 V device takes this tip.

The step page reads the implant as a large-angle-tilt implanted drain
({term}`LATID`) from the 40° angle: Hori introduced the quarter-micron
LATID transistor for 3.3 V operation and gave the full account of the
technology,[^hori-1989-latid][^hori-1992] Rafí and Campabadal compared
the hot-carrier degradation of LDD and LATID NMOS,[^rafi-2001] and the
lightly doped drain[^ogura-1980] and Takeda et al.'s drain structures
for minimising hot-carrier generation[^takeda-1982] are the older
answers to the degradation Hu et al. modelled.[^hu-1985-hci] A Cypress
patent describes a high-voltage device with self-aligned graded
junctions in a CMOS flow;[^pat-hv-graded-cyp] the step page treats it
as circumstantial evidence of lineage and no more.

What the mask does not define is the thick oxide or the tip's edge. The
`hvi` regions are set at {ref}`LVOM <step-044>` and oxidised at
{ref}`GOX100 <step-043>`, and on the step pages' readings the implant is
self-aligned to the gates of the {ref}`P1M <mask-p1m>` pattern; the
standard tip over the other NMOS is placed by {ref}`mask-ntm`, whose
created data, on that page's reading, cover `hvi` rather than open it.

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `chvntm` a `mask` purpose at 39:0 ("High voltage
N-tip implant mask") and a `drawing` purpose at 38:20, without a
description and with no `mask add` or `mask drop` purpose; the drawn
layer is `hvntm` at 125:20, a layer number it shares with `lvtn`
125:44.[^pdk-06] This is the one mask for which the PDK states an
operation. Rule X.1 of the `hvntm` set reads "Hvntm can be drawn inside
HVI. Drawn layer will be OR-ed with the CL and rechecked for
CLDRC".[^pdk-periph] The PDK does not expand "CL" or "CLDRC"; the
{ref}`HVNTM <step-068>` page reads the reticle as the union of what the
designer draws and a computed layer. Rule x.15a confines mask layers to
test modules, seal ring and frame, with an exception that names only
"FOM/P1M/Metal waffle drop" (flag P),[^pdk-periph] so a design inside the
die draws `hvntm` (our reading of x.15a).

The PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance
criteria for GDS data", lists checks on a layer it calls `CLHVNTM` under
the rule names `chvntm.1` to `chvntm.7`: "0.7 min. width of CLHVNTM",
"0.7 min. spacing/notch of CLHVNTM" (`chvntm.2a`), "0.185 Min Enclosure
of ndiff inside hvi by chvntm" (`chvntm.3`), "CLHVNTM must not overlap
NDIFFnoHV" and "CLHVNTM must not overlap PDIFF_noENID", each with a
0.185 spacing (`chvntm.4`, `chvntm.5`), "CLHVNTM must not overlap ptap"
(`chvntm.6a`), "CLHVNTM must not overlap p+diff along diff butting edge
(ESDnWellTap excluded)" (`chvntm.6b`) and "ESDnWellTapHV must be enclosed
by CLHVNTM" (`chvntm.7`); and two `chvntm.nikon` checks, "HVNTMmk in the
nikon cross has the wrong polarity" and "HVNTMmk is missing from the
nikon cross in the layout".[^pdk-errors] It does not define `CLHVNTM`.
We read it as the created `HVNTM` data, the "CL" of rule X.1, and its
checks as the "CLDRC" there (inference from the names): the checks mirror
the drawn-layer rules hvntm.1 to hvntm.7 on the created layer, and they
describe openings over n+ diffusion in `hvi`, not the operation that makes
them. The same page has its own versions of the drawn-layer rules, in
which X.1 reads "hvntm must be drawn inside hvi" (`hvntm.x.1`) where the
periphery rules say "can be drawn", and a module-cut check, "0.19 min.
spacing of moduleCutAREA & q0hvntmnotBuildSpace" (x.12a).[^pdk-errors]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. `HVNTM` is one of the masks the site's README calls
"fab-derived" and evaluates "as a boolean expression over drawn layers":
on all eight runs the expression is
`125:20 OR ((65:20 AND 93:44 AND 75:20) NOT 81:2)`, which in the layer
names of `gds_layers.csv` is `hvntm` OR ((`diff` AND `nsdm` AND `hvi`)
NOT `areaid.ce`).[^mask-renders][^pdk-06] Its mask record lists the drawn
layer 125:20 and the mask-level layer 39:0, with the note "drawn hvntm
merged with a created part (ndiff AND hvi, outside areaid.ce); only the
drawn part is rendered".[^mask-renders] The note contradicts the
expression, as the {ref}`masks index <masks-derivations>` records: the
expression renders the created part as well. The site gives no source for
either. The expression and note are one public derivation from the drawn
data, not SkyWater's mask-generation recipe; for the index, the created
part is one reading of the PDK's unexpanded "CL".

The created part is consistent in kind with the `chvntm` checks, which
place the created layer over n+ diffusion inside `hvi`, and with the
Table F2b rows above (our comparison).[^pdk-errors][^pdk-06] It differs
in detail: it takes n-type diffusion as `diff` AND `nsdm`, where Table
C3 of the *Layers Reference* defines `N+_diff` as "Diff NOT Nwell", and it
has no sizing, where `chvntm.3` asks for a 0.185 enclosure.[^pdk-06]
Since the site names no source, the agreement may only mean that both
start from the same public PDK pages.

All 40 rendered dies of every run carry shapes, but that is not 40
designs with 5 V NMOS: every die carries at least 11 483 shapes; 14 551
shapes appear on 26 to 33 dies of each of MPW-2 to MPW-8 and 14 560 on 37
dies of MPW-1; 11 483 on two to eight dies of each of MPW-2 to MPW-7; and
on MPW-1 one die accounts for 99 % of the run's shapes.[^mask-renders] We
read the repeated counts as shapes common to the dies rather than to the
projects (inference); the site does not say what they are, and with the
expression they may be created shapes over n+ diffusion in `hvi` as well
as drawn `hvntm`. The site states the limits of its images: "These are
renders of *drawn* data, not photomask artwork: reticle pitch, 4x
reduction, mirroring and the frame features the fab adds are not
modelled."[^mask-renders] Its metadata carries no plate ID, so a render
is tied to a plate in the process-steps sheet only by the acronym
`HVNTM`, and the MPW-4 renders come from a different reticle set from the
one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `HVNTM` plate
as existing on all eight MPW runs, with the plate number `257` on each
and no "Info" note.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA257A` |
| MPW-2 | `5CS8007AC` | `S8007AA257A` |
| MPW-3 | `5CS8008AC` | `S8008AA257A` |
| MPW-4 | `5CS8018AC` | `S8018AA257A` |
| MPW-5 | `5CS8011AC` | `S8011AA257A` |
| MPW-6 | `5CS8014AC` | `S8014AA257A` |
| MPW-7 | `5CS8016AC` | `S8016AA257A` |
| MPW-8 | `5CS8017AC` | `S8017AA257A` |

* **Plate number.** The sheet does not say what `257` encodes. It is two
  above `255` for `NTM`, the tip mask before it, but `LDNTM`, the tip mask
  after it, is `238` and `NSDM` (step 85) is `250`, so the numbers do not
  follow process order and no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `HVNTM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`, whose plates no public
  source lists ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`HVNTM <step-068>` page puts the 0.700 µm
width and space at {math}`k_1 \approx 1.2` on an i-line lens of NA 0.6,
quotes ASML's statement that older exposure tools "migrate to the
lithography of choice for less critical layers",[^asml-30] and infers an
i-line level; the {ref}`i-line stepper <machine-i-line-stepper>` page
lists it there. At the NA 0.48 low end of ASML's
PAS 5500/275D[^asml-pas5500-275d] the same feature has
{math}`k_1 = 0.7 \times 0.48 / 0.365 \approx 0.92` (our arithmetic).
SkyWater lists "ASML I-line stepper" and "ASML I-line scanner" among its
tools but assigns no layer to them.[^skw-01]

**Mask errors.** Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns";[^wong-1998]
at 365 nm and NA 0.48 that threshold is about 0.38 µm (our arithmetic),
about half the `HVNTM` minimum, so a CD error on the plate would be
expected to print at its own size (inference). Table 8 of *Criteria &
Assumptions* nevertheless gives an "Extra CD tol for HVNTM to match Ram7
process" of 0.015 (`HVNTMExtraCdTol`) in its column headed "CD"; the PDK
does not say what "Ram7" is or whether the tolerance applies to the plate
or the wafer.[^pdk-03]

**Resist.** Nothing is etched through this resist; it only has to stop
the arsenic of {ref}`HVASTI <step-069>` wherever the plate leaves it.
Table 4 gives a "Photoresist thickness for HV Tip Implants" of 0.3
(`PrThickImplant`) against the generic "Photoresist thickness" of 1.14
(`PRTHICKN`), both in its column headed "Value (um)".[^pdk-03] The step
page reads the thin film as ample for an LDD-type arsenic implant of tens
of keV, whose projected range in resist-like materials is a few tens of
nanometres, and points to pinholes as the risk a 0.3 µm film carries; the
ion range that sets the margin is what SRIM computes.[^ziegler-2010]
SkyWater's resist and any hardening are not public; the consumables are
on the {ref}`lithography materials <material-lithography-materials>`
page.

**Resist edges and shadowing.** The thin resist exists for the tilt:
Table 3f gives an "Angle for HV tip implant" of 40° (`HvTipAngle`) and a
"Twist angle for HV Tip" of 23° (`HvTipTwist`), Table 4 an "HVNTM
shadowing" of 0.232 (`hvntmShadowing`) and a "Min width of tip implant
opening" of 0.1, and Table 8, in its column headed "CD", a "Photoresist
tilted implant penetration" of 0.02 (`HVPrPenetration`), a "Photoresist
tilted implant blocking distance" of 0.013 (`HVPrBlocking`) and a "Min
size of HVTip" of 0.1 (`HVTipMinSize`).[^pdk-03] The
{ref}`HVNTM <step-068>` page finds them consistent: a 0.3 µm wall
shadows a 40° beam for 0.3 µm × tan 40° ≈ 0.25 µm, which less the 0.02 µm
penetration gives the 0.232 µm allowance. The PDK does not say how the
0.013 blocking distance enters. Chen et al. described ion-beam shadowing
of tilted drain implants by adjacent structures,[^chen-1995] a Taiwan
Semiconductor patent splits tilted LDD implants into several wafer
rotations,[^pat-quad-tsmc] and the {ref}`HVASTI <step-069>` page infers
rotations here; ions scattered out of a resist edge also alter nearby
thresholds, as Hook et al. found for a thick well resist.[^hook-2003]

**Pattern transfer.** On the step pages' readings the pattern is
transferred into the silicon as dopant by {ref}`HVASTI <step-069>` on
the {ref}`medium-current implanter <machine-medium-current-implanter>`
class, reaching under the gate edges of the selected transistors, and
the resist is removed at {ref}`HVASTIS <step-070>` on the
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` and
{ref}`wet bench <machine-wet-bench>` classes. The PDK gives the angles;
the species rests on its general "N Tip (As)" row, and the energy and
dose are not public.[^pdk-03]

**Overlay.** The {ref}`HVNTM <step-068>` page reads the mask as aligned
to poly (inference) and the 0.232 µm shadowing allowance and 0.1 µm
minimum opening as fixing how far a resist edge must stand from a gate;
the 0.185 µm rules against n+ diffusion outside `hvi` and against p+
diffusion (hvntm.4, hvntm.5) set the edges relative to the active
pattern.[^pdk-periph] ASML specifies "≤ 40 nm" single-machine overlay for
the /275D stepper[^asml-pas5500-275d] (our comparison; how SkyWater
budgets the margin is not public).

(mask-hvntm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `HVNTM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`HVNTM <step-068>`, {ref}`HVASTI <step-069>`, {ref}`HVASTIS <step-070>`

* {ref}`HVNTM <step-068>` — coats, exposes and develops the thin resist.
* {ref}`HVASTI <step-069>` — the 40° arsenic implant through the resist
  windows; this reference describes no halo for it.
* {ref}`HVASTIS <step-070>` — strips the thin implanted resist and cleans
  the wafer.

The next step, {ref}`LDNTM <step-071>`, is itself the next mask step: on
its step page's reading it coats the resist for the SONOS tip on the
surface cleaned at `HVASTIS`. No step between `HVASTIS` and it uses the
`HVNTM` resist, and there is no exception to the rule for this mask. On
the step pages' readings the tip placed through this resist is annealed
with the other tips at {ref}`TIPRTAD <step-075>`.

## Design rules and critical dimensions

The `hvntm` rules of the periphery rules, with the precision-resistor
rule that refers to the layer and the mask-data rules x.7 and x.15a; flag
P means "Rule applies to periphery only (outside areaid.ce). A
corresponding core rule may or may not exist.", DE "Rule not checked for
source of Drain Extended device" and NC "Rule not checked by DRC. It
should be used as a guideline only."; the unit column of hvntm.7 is
blank in the published table.[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| hvntm.X.1 | "Hvntm can be drawn inside HVI. Drawn layer will be OR-ed with the CL and rechecked for CLDRC" | — |
| hvntm.1 | "Width of hvntm" (P) | 0.700 µm |
| hvntm.2 | "Spacing of hvntm to hvntm" (P) | 0.700 µm |
| hvntm.3 | "Min. enclosure of (n+_diff inside Hvi) but not overlapping areaid.ce by hvntm" (P) | 0.185 µm |
| hvntm.4 | "Space, no overlap, between n+_diff outside Hvi and hvntm" (P) | 0.185 µm |
| hvntm.5 | "Space, no overlap, between p+_diff  and hvntm" (P, DE) | 0.185 µm |
| hvntm.6a | "Space, no overlap, between p+_tap and hvntm (except along the diff-butting edge)" (P) | 0.185 µm |
| hvntm.6b | "Space, no overlap, between p+_tap and hvntm along the diff-butting edge" (P) | 0.000 µm |
| hvntm.7 | "hvntm must enclose ESD_nwell_tap inside hvi by atleast" (P) | 0.000 |
| hvntm.9 | "Hvntm must not overlap areaid.ce" | — |
| hvntm.10 | "Hvntm must overlap hvi" | — |
| rpm.9 | "Min space, no overlap, between prec_resistor and hvntm" | 0.185 µm |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |

Table 2 of *Criteria & Assumptions* repeats the width and space as
`HVNTMCD` 0.7 and `HVNTMCDSP` 0.7, and the Error Messages page checks the
created layer at the same pair (`chvntm.1`, `chvntm.2a`).[^pdk-03][^pdk-errors]
The other criteria that name the mask or its implant are those quoted
above: Table 3f's 40° tilt and 23° twist; Table 4's "Photoresist
thickness for HV Tip Implants" (0.3), "HVNTM shadowing" (0.232) and "Min
width of tip implant opening" (0.1); and Table 8's "Photoresist tilted
implant penetration" (0.02), "Photoresist tilted implant blocking
distance" (0.013), "Min size of HVTip" (0.1) and "Extra CD tol for HVNTM
to match Ram7 process" (0.015).[^pdk-03] Table 8 also gives an "HV MOSFET
channel length" of 0.5 (`HVPCD`), which the {ref}`HVASTI <step-069>`
page reads as long enough not to need a halo.[^pdk-03] For the plate,
hvntm.1 and hvntm.2 set the smallest features, 0.700 µm lines and
spaces, and the 0.185 µm rules set where its edges fall against the
active pattern.

## Related pages

* {ref}`HVNTM <step-068>`, {ref}`HVASTI <step-069>` and
  {ref}`HVASTIS <step-070>` — the mask step, the tilted implant and the
  strip.
* {ref}`mask-ntm` — the standard tip mask before it;
  {ref}`LDNTM <step-071>` — the SONOS tip mask after it;
  {ref}`TIPRTAD <step-075>` — the anneal of all three tips.
* {ref}`LVOM <step-044>` and {ref}`GOX100 <step-043>` — where the `hvi`
  thick oxide the mask follows is defined and grown.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the derivations the renders use.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-medium-current-implanter` — the implant class that uses
  the pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography` and {ref}`category-implant` — the mask
  step and implant categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "High Volt. N-tip, HVNTM,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `hvntm`, the
  `chvntm` purposes, `hvi`, the Table C3 definitions and the `HVNTM`
  column of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `HVNTMCD`/`HVNTMCDSP`, the HV
  tip angles, the photoresist thicknesses and the shadowing, penetration,
  blocking and HV tip criteria.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `hvntm` rules and function line,
  rpm.9, x.7, x.15a and the flag legend.[^pdk-periph]
* SkyWater PDK, *Error Messages* page and `errors.csv` — the `chvntm`
  checks on `CLHVNTM`, the `hvntm` messages and the "nikon cross"
  checks.[^pdk-errors]
* SkyWater PDK, *High Voltage Methodology* — the 110 Å oxide of the VHV
  and 5 V devices.[^pdk-hv]
* *S8 / SKY130 Process Steps* sheet — the step, the `HVNTM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `HVNTM` expression, note and
  per-die shape counts.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the i-line exposure
  tools.[^skw-01]
* ASML, *PAS 5500/275D* data sheet — NA range and single-machine overlay
  of an i-line stepper.[^asml-pas5500-275d]
* ASML, *Three decades of PAS 5500* — older exposure tools moving to less
  critical layers.[^asml-30]

### High-level understanding

* Wikipedia, *Photomask* — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wikipedia, *Ion implantation* — masking, range and
  energy.[^wiki-implant]
* Wikipedia, *Hot-carrier injection* — the failure mode that graded and
  LATID drains exist to prevent.[^wiki-hci]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — LDD and
  hot-carrier engineering.[^txt-04]
* Mack, *Fundamental Principles of Optical Lithography* — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* Levinson, *Principles of Lithography* — overlay budgets and
  non-critical-layer tool choice.[^levinson-2005]

### Deep dive

* Hori, IEDM 1989 — the quarter-micron LATID transistor for 3.3 V
  operation.[^hori-1989-latid]
* Hori et al., *IEEE TED* 1992 — the full account of large-angle-tilt
  implanted drain technology.[^hori-1992]
* Rafí and Campabadal, *Solid-State Electronics* 2001 — hot-carrier
  degradation of LDD against LATID NMOS.[^rafi-2001]
* Ogura et al. (IBM), *IEEE TED* 1980 — the lightly doped drain-source
  transistor.[^ogura-1980]
* Takeda et al., *IEEE TED* 1982 — drain structures for
  minimising hot-carrier generation.[^takeda-1982]
* Hu et al., *IEEE TED* 1985 — the hot-electron degradation model that
  sets the lifetime target.[^hu-1985-hci]
* Kouznetsov (Cypress), US 6,531,366 — a high-voltage device with
  self-aligned graded junctions in a CMOS flow.[^pat-hv-graded-cyp]
* Lin, Yoo and Liang (TSMC), US 5,372,957 — multiple tilted-angle
  implantation with wafer rotation for LDD devices.[^pat-quad-tsmc]
* Chen et al., *Solid-State Electronics* 1995 — ion-beam shadowing of
  tilted drain implants by adjacent structures.[^chen-1995]
* Hook et al., *IEEE TED* 2003 — ions scattered from the resist edge and
  the threshold shifts they cause.[^hook-2003]
* Ziegler, Ziegler and Biersack, *NIM B* 2010 — SRIM, for the ion range
  in resist.[^ziegler-2010]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  size below which it rises.[^wong-1998]
* ITRS 2001, *Lithography* — mask magnification for the 130 nm
  generation.[^itrs-03]

## Open questions

* What "CL" and "CLDRC" mean, and the operation that makes the created
  part of the plate, are not published; the Error Messages page checks a
  `CLHVNTM` layer it does not define,[^pdk-periph][^pdk-errors] and the
  renders' expression for the created part has no sizing and a note that
  contradicts it.[^mask-renders]
* Why Table F2b creates `HVNTM` shapes for the 16 V drain-extended NMOS
  but not for the UHV 5/20 V rows is not explained, and whether the
  drain-extended devices take the implant on their source side is the
  {ref}`HVASTI <step-069>` page's open question.[^pdk-06]
* How the 0.013 "Photoresist tilted implant blocking distance" enters the
  allowances, what "Ram7" is, and whether the 0.015 CD tolerance refers to
  the plate or the wafer are not stated.[^pdk-03]
* The periphery rules' "Hvntm can be drawn inside HVI" and the Error
  Messages page's "hvntm must be drawn inside hvi" are not reconciled in
  the PDK.[^pdk-periph][^pdk-errors]
* The plate's tone, blank, absorber and magnification, the resist and the
  exposure tool are not public; the i-line reading rests on the 0.700 µm
  rules.
* What the plate number `257` encodes is not stated, and no public source
  lists the `HVNTM` plate of the original MPW-4 set
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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 3f,
    4 and 8), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/08-hv.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_HVNTM/`
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
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021.
    <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-hci]: Wikipedia, *Hot-carrier injection*.
    <https://en.wikipedia.org/wiki/Hot-carrier_injection>
[^txt-04]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
    Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
    <https://openlibrary.org/isbn/9780961672157>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^hori-1989-latid]: T. Hori, "1/4-μm LATID (LArge-Tilt-angle Implanted
    Drain) technology for 3.3-V operation", *IEDM 1989 Technical
    Digest*, pp. 777–780. <https://doi.org/10.1109/IEDM.1989.74169>
[^hori-1992]: T. Hori, J. Hirase, Y. Odake and T. Yasui,
    "Deep-submicrometer large-angle-tilt implanted drain (LATID)
    technology", *IEEE Transactions on Electron Devices* **39**(10),
    2312–2324 (1992). <https://doi.org/10.1109/16.158803>
[^rafi-2001]: J. M. Rafí and F. Campabadal, "Hot-carrier degradation in
    deep-submicrometer nMOSFETs: lightly doped drain vs. large angle tilt
    implanted drain", *Solid-State Electronics* **45**(8), 1391–1401
    (2001). <https://doi.org/10.1016/S0038-1101(01)00004-1>
[^ogura-1980]: S. Ogura, P. J. Tsang, W. W. Walker, D. L. Critchlow and
    J. F. Shepard, "Design and characteristics of the lightly doped
    drain-source (LDD) insulated gate field-effect transistor", *IEEE
    Transactions on Electron Devices* **27**(8), 1359–1367 (1980).
    <https://doi.org/10.1109/T-ED.1980.20040>
[^takeda-1982]: E. Takeda, H. Kume, T. Toyabe and S. Asai,
    "Submicrometer MOSFET structure for minimizing hot-carrier
    generation", *IEEE Transactions on Electron Devices* **29**(4),
    611–618 (1982). <https://doi.org/10.1109/T-ED.1982.20752>
[^hu-1985-hci]: C. Hu, S. C. Tam, F.-C. Hsu, P.-K. Ko, T.-Y. Chan and
    K. W. Terrill, "Hot-electron-induced MOSFET degradation — Model,
    monitor, and improvement", *IEEE Transactions on Electron Devices*
    **32**(2), 375–385 (1985). <https://doi.org/10.1109/T-ED.1985.21952>
[^pat-hv-graded-cyp]: I. Kouznetsov (Cypress Semiconductor), *Method and
    structure for high-voltage device with self-aligned graded
    junctions*, US 6,531,366 B1, granted 2003-03-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6531366>
[^pat-quad-tsmc]: M.-S. Lin, C.-S. Yoo and M.-S. Liang (Taiwan
    Semiconductor Manufacturing Company), *Multiple tilted angle ion
    implantation MOSFET method*, US 5,372,957 A, granted 1994-12-13.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5372957>
[^chen-1995]: H.-S. Chen, C.-S. Teng, L. Moberly and R. Lahri, "Ion beam
    shadowing effect in submicrometer large-angle-tilt implanted drain
    (LATID) MOSFETs", *Solid-State Electronics* **38**(7), 1321–1323
    (1995). <https://doi.org/10.1016/0038-1101(94)00256-F>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices* **50**(9),
    1946–1951 (2003). <https://doi.org/10.1109/TED.2003.815371>
[^ziegler-2010]: J. F. Ziegler, M. D. Ziegler and J. P. Biersack, "SRIM
    – The stopping and range of ions in matter (2010)", *Nuclear
    Instruments and Methods in Physics Research B* **268**(11–12),
    1818–1823 (2010). <https://doi.org/10.1016/j.nimb.2010.02.091>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
