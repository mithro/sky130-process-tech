(mask-ldntm)=
# LDNTM — Lightly Doped N-tip

The lightly doped N-tip mask is the {term}`reticle` of the third and last
tip implant of SKY130: on the {ref}`LDNTM <step-071>` page's reading, the
resist printed through it at step 71 exposes the {term}`SONOS` memory
transistors and covers everything else, the lightly doped arsenic tip
{ref}`LDASTI <step-072>` and the boron {term}`halo` {ref}`LDBHI <step-073>`
pass through the same openings, and the resist is stripped at
{ref}`LDASTIS <step-074>`. It is an implant {term}`block mask` for the
memory module, and in the public record it is a mask of contrasts: the
process-steps sheet records an `LDNTM` plate on all eight MPW runs, while
the public renders of those runs find its drawn layer on one die of
MPW-1 and one of MPW-5 and on no die of the other six, and the PDK's
periphery rules have no rule set for it while its Error Messages page
checks it as a core layer. This page gathers what public sources say about
the mask itself — its PDK entry and layers, the plates the process-steps
sheet records for the MPW runs, what the public renders of those runs
show, the lithography it needs and the rules that constrain it. How the
step is performed is on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | LDNTM — Lightly Doped N-tip |
|---|---|
| Mask step | {ref}`LDNTM <step-071>`, step 71 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Lightly Doped N-tip", `LDNTM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cldntm` mask 11:0, "Lightly-doped N-tip implant mask"[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `ldntm` drawing 11:44, "N-tip implant on SONOS devices"[^pdk-06] |
| Minimum CD, feature / space | `LDNTMCD` 0.7 / `LDNTMCDSP` 0.7[^pdk-03] |
| Polarity and tone | Not published. The step page reads the resist as opened over the SONOS transistors, where `ldntm` is drawn; with a positive resist the plate would be clear over `ldntm` and opaque elsewhere (inference). |
| Exposure class | i-line, an inference on the step page from the size of the memory-array openings; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `238`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 1, 0, 0, 0, 1, 0, 0, 0[^mask-renders] |
| Steps that use the pattern | 4 steps; see {ref}`Steps that use this mask <mask-ldntm-steps>` |

## What the mask defines

`masks.csv` lists "Lightly Doped N-tip, LDNTM" as used in SKY130, and
`gds_layers.csv` describes the drawn layer `ldntm` as "N-tip implant on
SONOS devices" and the mask-level layer `cldntm` as "Lightly-doped N-tip
implant mask".[^pdk-05][^pdk-06] The devices are the memory cells: "The
SKY130 process currently supports two SONOS flash memory cells", an
"original cell" and a "star" cell about 25 % smaller, and the device page
describes the "2-T SONOS memory cell".[^pdk-07] The {ref}`LDNTM <step-071>`
page reads the lighter tip as serving a transistor whose junctions sit at
several volts during programme, erase and inhibit, where a heavily doped,
abrupt tip would raise the field at the gate edge; the lightly doped
drain of Ogura et al. is the classical answer to that
field,[^ogura-1980] and a Micron patent masks a second, lighter LDD onto
selected transistors to cut junction leakage.[^pat-ldd-micron] White,
Adams and Bu review scaled SONOS memory,[^pap-01] and Eitan et al.'s
NROM, a localised-trapping two-bit cell, is the step page's example of a
cell that exploits the drain-edge injection this one
avoids.[^eitan-2000]

The PDK's mask generation table, Table F2b, marks the `LDNTM` column `C`
("CREATED") in 9 of its 80 device rows: the four SONOS rows, both
`nmos_core NV` rows, both flash pass-gate ("Flash npass") rows and the
"NV SONOS Diode".[^pdk-06] It marks `-`, "Layer not created for the
device", in 39 rows, among them the 1.8 V NMOS and PMOS, the `pmos_core`
rows, the varactors and every 110 Å row other than the flash pass gates,
and `+`, "Layer allowed to overlap", in the remaining 32.[^pdk-06] On our
reading the created shapes follow the non-volatile memory devices,
including a 110 Å pass gate and a core NMOS marked "NV", not the SONOS transistor alone; the table does not say what
the implant through the openings does. The four SONOS rows and the two
flash pass-gate rows are also marked `C` in the `NTM` column
({ref}`mask-ntm`), which on that page's reading places the standard
tip's created data over devices that do not receive it.[^pdk-06]

What the mask does not define is the memory transistor itself. On the
step pages' readings the tunnel window is opened at
{ref}`TUNM <step-035>`, the channel is set by {ref}`PTSI <step-037>` and
{ref}`DEPI <step-038>`, the {term}`ONO` stack is patterned at
{ref}`ONOM <step-041>`, and the tip self-aligns to the gates of the
{ref}`P1M <mask-p1m>` pattern; the source and drain are implanted later
through {ref}`NSDM <step-085>`. Codella and Ogura's halo, which the
{ref}`LDBHI <step-073>` implant provides for these transistors, is the
same pairing of tip and pocket as in the logic flow.[^codella-1985]

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `cldntm` a single purpose, `mask` at 11:0 on the
same layer number as the drawn `ldntm` at 11:44, and no `drawing`,
`mask add`, `mask drop` or `waffle drop` purpose.[^pdk-06] The pairing of
the mask with `ldntm` rests on those names and descriptions, and the PDK
publishes no operation from the drawn layer to the plate. Rule x.15a
confines "Drawn compatible, mask, and waffle-drop layers" to test
modules, seal ring and frame, with an exception that names only
"FOM/P1M/Metal waffle drop" (flag P),[^pdk-periph] so a design draws
`ldntm` (our reading of x.15a). The periphery rules have no `ldntm` rule
set, as the {ref}`LDNTM <step-071>` page notes.[^pdk-periph]

The PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance
criteria for GDS data", does list checks on the layer, all with core
names: `ldntm.c1`, "0.7 min. width of ldntmCore"; `ldntm.c2`, "0.7 min.
spacing/notch of ldntmCore"; `ldntm.c3`, "enclosure of ndiff by ldntm
must be more than  0.180"; `ldntm.c4`, "0.125 min. enclosure of nFet by
ldntmCore"; `ldntm.c5`, "ldntm not allowed outside areaid.ce"; and
`ldntm.c6`, "0.18 min. spacing of ldntmCoreExempt & pdiff".[^pdk-errors]
It also has two `cldntm.nikon` checks ("LDNTMmk in the nikon cross has the
wrong polarity" and "LDNTMmk is missing from the nikon cross in the
layout"), module-cut checks "0.35 min. spacing of moduleCutAREA &
q0ldntmnotBuildSpace" (x.12a) and "0.35 min. enclosure of
q0ldntmnotBuildSpace by moduleCutAREA" (x.12b), "ldntm drawn layer cannot
straddle areaid:ModuleCut" (scribe.7), an x.15a message for `LDNTMmk`,
and, among the `NTM` checks, `cntm.7`, "ldntm must be enclosed by
CLNTM".[^pdk-errors] The page defines none of `ldntmCore`,
`ldntmCoreExempt` or `CLNTM`. On our reading the checks confine the layer
to the core identifier `areaid.ce`, "Memory (SRAM) core cell identifier",
as the tunnel rule tunm.8 confines `tunm` ("tunm must be enclosed by
areaid.ce"), and make it enclose the n-type transistors it serves by
0.125 and their n+ diffusion by more than 0.180 (inference from the check
wording).[^pdk-errors][^pdk-06][^pdk-periph] The checks say what the
layer must enclose, not how the plate data are made.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `LDNTM` the site renders layer 11:44 (`ldntm`)
alone, with no Boolean expression, no fill layer and no note, on all
eight runs; its mask record gives the mask-level layer
11:0.[^mask-renders] That is the index's pairing, and the choice of layer
is one public derivation from the drawn data, not SkyWater's
mask-generation recipe.

The layer is drawn on one die of MPW-1 (frame A4, 4 shapes) and one die of
MPW-5 (frame D7, 42 shapes), and on no die of MPW-2, MPW-3, MPW-4, MPW-6,
MPW-7 or MPW-8.[^mask-renders] The
{ref}`masks index <masks-renders>` records the same two frames for `tunm`,
the layer from which the site renders `TUNM` and `ONOM`. The site states
the limits of its images: "These are renders of *drawn* data, not
photomask artwork: reticle pitch, 4x reduction, mirroring and the frame
features the fab adds are not modelled. Empty images are real results -
several masks are used by no project on a given shuttle."[^mask-renders]
Its metadata carries no plate ID, so a render is tied to a plate in the
process-steps sheet only by the acronym `LDNTM`, and the MPW-4 renders
come from a different reticle set from the one whose plates the sheet
records ({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `LDNTM` plate
as existing on all eight MPW runs, with the plate number `238` on each
and no "Info" note.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA238A` |
| MPW-2 | `5CS8007AC` | `S8007AA238A` |
| MPW-3 | `5CS8008AC` | `S8008AA238A` |
| MPW-4 | `5CS8018AC` | `S8018AA238A` |
| MPW-5 | `5CS8011AC` | `S8011AA238A` |
| MPW-6 | `5CS8014AC` | `S8014AA238A` |
| MPW-7 | `5CS8016AC` | `S8016AA238A` |
| MPW-8 | `5CS8017AC` | `S8017AA238A` |

* **Plates on runs without drawn shapes.** The sheet records an `LDNTM`
  plate on MPW-2, MPW-3, MPW-4, MPW-6, MPW-7 and MPW-8, on which no
  rendered die draws `ldntm`, as it does for `TUNM` and `ONOM`
  ({ref}`masks-renders`).[^steps-sheet][^mask-renders] Because the
  renders leave out whatever the fab adds to a plate, they cannot show
  what those plates carry, and no public source says; for MPW-4 the
  renders and the plates also belong to different reticle sets.
* **Plate number.** The sheet does not say what `238` encodes. It lies
  between `230` for `ONOM` (step 41) and `250` for `NSDM` (step 85), and
  below `255` and `257` for `NTM` and `HVNTM`, the tip masks that precede
  it, so the numbers do not follow process order and no process position
  is read from it ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `LDNTM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`, whose plates no public
  source lists ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`LDNTM <step-071>` page reads the openings
as memory-array sized and "far above i-line resolution", quotes ASML's
statement that older exposure tools "migrate to the lithography of
choice for less critical layers",[^asml-30] and infers an i-line level;
the {ref}`i-line stepper <machine-i-line-stepper>` page lists it there.
Table 2 gives 0.7 for both `LDNTMCD` and `LDNTMCDSP`,[^pdk-03] and at the
NA 0.48 low end of ASML's PAS 5500/275D[^asml-pas5500-275d] a 0.7 µm
feature has {math}`k_1 = 0.7 \times 0.48 / 0.365 \approx 0.92` (our
arithmetic). SkyWater lists "ASML I-line stepper" and "ASML I-line
scanner" among its tools but assigns no layer to them.[^skw-01]

**Mask errors.** Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns";[^wong-1998]
at 365 nm and NA 0.48 that threshold is about 0.38 µm (our arithmetic),
about half the `LDNTM` minimum, so a CD error on the plate would be
expected to print at its own size (inference).

**Resist.** Nothing is etched through this resist; it only has to stop
the tip and halo wherever the plate leaves it. The step page notes that
the PDK publishes a thin resist only "for HV Tip Implants" — 0.3 in
Table 4's column headed "Value (um)" (`PrThickImplant`) — and infers the
standard film of about 1 µm, the generic "Photoresist thickness" of
1.14.[^pdk-03] The {ref}`LDASTI <step-072>` page reads the tip as an
LDD-class dose from the PDK's description of the mask, and the step page
the halo as tens of keV, both stopped with a
wide margin; the ion range in resist that sets the margin is what SRIM
computes.[^ziegler-2010] Ross et al. stabilised i-line implant resists
with a flood electron beam, reducing shrinkage and CD variation and
eliminating popping.[^ross-1996] SkyWater's resist, its thickness and any
hardening are not public; the consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Resist edges and shadowing.** The PDK publishes shadowing allowances
for `NTM` (0.16) and `HVNTM` (0.232) but none for `LDNTM`, and a single
"Angle for tip implant" of 7° that the step page takes to apply to this
tip as well (inference).[^pdk-03] The step page reads the array
boundary as the edge that matters: the resist must stand back from the
outermost gates of a dense array by the tip's shadowing allowance. Chen
et al. described ion-beam shadowing of tilted drain implants by adjacent
structures,[^chen-1995] and Hook et al. the threshold shifts of devices
near a resist edge from ions scattered out of it;[^hook-2003] the
{ref}`LDBHI <step-073>` page notes that the halo's tilt is not public.

**Pattern transfer.** On the step pages' readings the pattern is
transferred into the memory transistors' silicon as dopant by
{ref}`LDASTI <step-072>`, on the
{ref}`medium-current implanter <machine-medium-current-implanter>` class
or, as the alternative, the
{ref}`high-current implanter <machine-high-current-implanter>` class,
and by {ref}`LDBHI <step-073>` on the medium-current class, and the
resist is removed at {ref}`LDASTIS <step-074>` on the
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` and
{ref}`wet bench <machine-wet-bench>` classes. The PDK's "N Tip (As)" row
gives arsenic for N tips in general; the energies, doses, and the halo's
species beyond boron, tilt and rotation are not public.[^pdk-03]

**Overlay.** The {ref}`LDNTM <step-071>` page reads the mask as aligned
to poly. The `ldntm.c4` check's 0.125 enclosure of an n-type transistor
and `ldntm.c6`'s 0.18 spacing to p-type diffusion[^pdk-errors] are the
published distances that the plate's placement must respect (our
reading); ASML specifies "≤ 40 nm" single-machine overlay for the /275D
stepper[^asml-pas5500-275d] (our comparison; how SkyWater budgets the
margin is not public).

(mask-ldntm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `LDNTM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`LDNTM <step-071>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`, {ref}`LDASTIS <step-074>`

* {ref}`LDNTM <step-071>` — coats, exposes and develops the resist.
* {ref}`LDASTI <step-072>` — the lightly doped arsenic tip of the memory
  transistors through the resist windows.
* {ref}`LDBHI <step-073>` — the memory transistors' boron halo through
  the same resist.
* {ref}`LDASTIS <step-074>` — strips the implanted resist and, as the
  last strip before the anneal, cleans the wafer for it.

On its step page's reading, the next step, {ref}`TIPRTAD <step-075>`, is
the rapid thermal anneal that activates all the tips and halos of the
module with no resist on the wafer. The next mask step is
{ref}`NPCM <step-078>`, after the spacer deposition and etch. There is no
exception to the rule for this mask.

## Design rules and critical dimensions

The periphery rules have no `ldntm` rule set. The table gives the rules
that bear on the mask there — the tunnel-layer rule that confines `tunm`
to the core identifier and the mask-data rules x.7 and x.15a — and then,
in its last six rows, the Error Messages page's `ldntm` checks, whose
values are in their wording and which carry no flags; flag P means "Rule applies to periphery only
(outside areaid.ce). A corresponding core rule may or may not exist." and
NC "Rule not checked by DRC. It should be used as a guideline
only."[^pdk-periph][^pdk-errors]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| tunm.8 | "tunm must be enclosed by areaid.ce" | — |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
| ldntm.c1 | "0.7 min. width of ldntmCore" | 0.7 |
| ldntm.c2 | "0.7 min. spacing/notch of ldntmCore" | 0.7 |
| ldntm.c3 | "enclosure of ndiff by ldntm must be more than  0.180" | 0.180 |
| ldntm.c4 | "0.125 min. enclosure of nFet by ldntmCore" | 0.125 |
| ldntm.c5 | "ldntm not allowed outside areaid.ce" | — |
| ldntm.c6 | "0.18 min. spacing of ldntmCoreExempt & pdiff" | 0.18 |

Table 2 of *Criteria & Assumptions* gives `LDNTMCD` 0.7 and `LDNTMCDSP`
0.7, the values of `ldntm.c1` and `ldntm.c2`, and no other criterion
names the mask.[^pdk-03][^pdk-errors] The tip criteria that do not name a
mask are Table 3b's "N Tip (As)" (0.01, `LDNTIP`), Table 3f's 7° "Angle
for tip implant" and Table 4's "Min width of tip implant opening" (0.1)
and "pseudo-shadowing" (0.045); Table 4's "Photoresist thickness for HV
Tip Implants" (0.3, `PrThickImplant`), "NTM shadowing" (0.16,
`ntmShadowing`) and "HVNTM shadowing" (0.232, `hvntmShadowing`) name the
HV tip and the other two tip masks.[^pdk-03] For the plate the published figures are a
0.7 µm feature on a 0.7 µm space.

## Related pages

* {ref}`LDNTM <step-071>`, {ref}`LDASTI <step-072>`,
  {ref}`LDBHI <step-073>` and {ref}`LDASTIS <step-074>` — the mask step,
  the tip and halo implants and the strip.
* {ref}`mask-ntm` and {ref}`mask-hvntm` — the two other tip masks of the
  module; {ref}`TIPRTAD <step-075>` — the anneal of all three tips.
* {ref}`TUNM <step-035>` and {ref}`ONOM <step-041>` — the other memory
  masks, whose layer the renders find on the same two dies.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the runs with plates but no drawn shapes.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-medium-current-implanter` and
  {ref}`machine-high-current-implanter` — the implant classes that use
  the pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography` and {ref}`category-implant` — the mask
  step and implant categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "Lightly Doped N-tip,
  LDNTM, X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `ldntm`,
  `cldntm`, `areaid.ce` and the `LDNTM` and `NTM` columns of Table
  F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `LDNTMCD`/`LDNTMCDSP`, the tip
  criteria and the photoresist thicknesses.[^pdk-03]
* SkyWater PDK, *Periphery rules* — tunm.8, x.7, x.15a and the flag
  legend.[^pdk-periph]
* SkyWater PDK, *Error Messages* page and `errors.csv` — the `ldntm` core
  checks, `cntm.7`, the module-cut and "nikon cross" checks.[^pdk-errors]
* SkyWater PDK, *Device Details* — the two SONOS flash memory cells and
  the 2-T cell.[^pdk-07]
* *S8 / SKY130 Process Steps* sheet — the step, the `LDNTM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `LDNTM` renders, their layer
  and the dies that draw it.[^mask-renders]
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
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — LDD, extension
  and halo engineering.[^txt-04]
* Mack, *Fundamental Principles of Optical Lithography* — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* Levinson, *Principles of Lithography* — overlay budgets and
  non-critical-layer tool choice.[^levinson-2005]

### Deep dive

* White, Adams and Bu, *IEEE Circuits and Devices* 2000 — a review of
  scaled SONOS memory.[^pap-01]
* Eitan et al., *IEEE EDL* 2000 — NROM, the localised charge-trapping
  alternative.[^eitan-2000]
* Ogura et al. (IBM), *IEEE TED* 1980 — the lightly doped drain-source
  transistor.[^ogura-1980]
* Codella and Ogura (IBM), IEDM 1985 — the halo added to the
  LDD.[^codella-1985]
* Tran, McQueen and Kerr (Micron), US 6,759,288 — a second, lighter LDD
  masked onto selected transistors to cut junction
  leakage.[^pat-ldd-micron]
* Gardner, Hause and Fulford (AMD), US 5,793,090 — separate LDD and
  source/drain implant steps for different transistors on one
  chip.[^pat-multi-ldd-amd]
* Chen et al., *Solid-State Electronics* 1995 — ion-beam shadowing of
  tilted drain implants by adjacent structures.[^chen-1995]
* Hook et al., *IEEE TED* 2003 — ions scattered from the resist edge and
  the threshold shifts they cause.[^hook-2003]
* Ross et al., *Proc. SPIE* 1996 — electron-beam stabilisation of i-line
  implant resists.[^ross-1996]
* Ziegler, Ziegler and Biersack, *NIM B* 2010 — SRIM, for the ion range
  in resist.[^ziegler-2010]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  size below which it rises.[^wong-1998]
* ITRS 2001, *Lithography* — mask magnification for the 130 nm
  generation.[^itrs-03]

## Open questions

* No public source says what the `LDNTM` plates of MPW-2, MPW-3, MPW-4,
  MPW-6, MPW-7 and MPW-8 carry, on which no rendered die draws
  `ldntm`,[^steps-sheet][^mask-renders] or whether the fab adds shapes of
  its own to them.
* The periphery rules have no `ldntm` rule set; the Error Messages page
  checks the layer under core names and does not define `ldntmCore` or
  `ldntmCoreExempt`.[^pdk-periph][^pdk-errors]
* Why Table F2b creates `LDNTM` shapes for the flash pass gates and the
  `nmos_core NV` rows, and what the implant does to them, is not
  stated.[^pdk-06]
* The tip's dose, the halo's tilt and the resist thickness are not
  public; the PDK gives no shadowing allowance for this
  mask.[^pdk-03]
* The plate's tone, blank, absorber and magnification and the exposure
  tool are not public; the i-line reading rests on the feature sizes.
* What the plate number `238` encodes is not stated, and no public source
  lists the `LDNTM` plate of the original MPW-4 set
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
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* (including Table F2b,
    the mask generation table) and `gds_layers.csv`, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 3b,
    3f and 4), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (SONOS cells), SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_LDNTM/`
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
[^txt-04]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
    Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
    <https://openlibrary.org/isbn/9780961672157>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^pap-01]: M. H. White, D. A. Adams and J. Bu, "On the go with SONOS",
    *IEEE Circuits and Devices Magazine* **16**(4), 22–31 (2000).
    <https://doi.org/10.1109/101.857747>
[^eitan-2000]: B. Eitan, P. Pavan, I. Bloom, E. Aloni, A. Frommer and
    D. Finzi, "NROM: A novel localized trapping, 2-bit nonvolatile memory
    cell", *IEEE Electron Device Letters* **21**(11), 543–545 (2000).
    <https://doi.org/10.1109/55.877205>
[^ogura-1980]: S. Ogura, P. J. Tsang, W. W. Walker, D. L. Critchlow and
    J. F. Shepard, "Design and characteristics of the lightly doped
    drain-source (LDD) insulated gate field-effect transistor", *IEEE
    Transactions on Electron Devices* **27**(8), 1359–1367 (1980).
    <https://doi.org/10.1109/T-ED.1980.20040>
[^codella-1985]: C. F. Codella and S. Ogura, "Halo doping effects in
    submicron DI-LDD device design", *IEDM 1985 Technical Digest*,
    pp. 230–233. <https://doi.org/10.1109/IEDM.1985.190938>
[^pat-ldd-micron]: L. C. Tran, M. McQueen and R. Kerr (Micron
    Technology), *Double LDD devices for improved DRAM refresh*, US
    6,759,288 B2, granted 2004-07-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6759288>
[^pat-multi-ldd-amd]: M. I. Gardner, F. N. Hause and H. J. Fulford
    (Advanced Micro Devices), *Integrated circuit having multiple LDD
    and/or source/drain implant steps to enhance circuit performance*,
    US 5,793,090 A, granted 1998-08-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5793090>
[^chen-1995]: H.-S. Chen, C.-S. Teng, L. Moberly and R. Lahri, "Ion beam
    shadowing effect in submicrometer large-angle-tilt implanted drain
    (LATID) MOSFETs", *Solid-State Electronics* **38**(7), 1321–1323
    (1995). <https://doi.org/10.1016/0038-1101(94)00256-F>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices* **50**(9),
    1946–1951 (2003). <https://doi.org/10.1109/TED.2003.815371>
[^ross-1996]: M. F. Ross, W. R. Livesay, V. Starov, K. Ostrowski and
    S. Y. Wong, "Photoresist stabilization for ion implant processing",
    *Proc. SPIE* **2724**, 632 (1996).
    <https://doi.org/10.1117/12.241862>
[^ziegler-2010]: J. F. Ziegler, M. D. Ziegler and J. P. Biersack, "SRIM
    – The stopping and range of ions in matter (2010)", *Nuclear
    Instruments and Methods in Physics Research B* **268**(11–12),
    1818–1823 (2010). <https://doi.org/10.1016/j.nimb.2010.02.091>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
