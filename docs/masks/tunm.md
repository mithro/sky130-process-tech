(mask-tunm)=
# TUNM — Tunnel Mask

The tunnel mask is the first {term}`reticle` of SKY130's {term}`SONOS`
memory module: on the {ref}`TUNM <step-035>` page's reading, the resist
printed through it at step 35 is opened over the channels of the SONOS
memory transistors and nowhere else, and the same openings serve four
more steps — the anti-reflective-coating etch
{ref}`TUNARCE <step-036>`, the two channel implants
{ref}`PTSI <step-037>` and {ref}`DEPI <step-038>`, and the oxide etch
{ref}`TUNME <step-039>` that clears the silicon for the tunnel oxide.
Its public record is lopsided: the process-steps sheet records a plate
for it on all eight MPW runs, while the public renders of those runs'
tape-out layouts show its drawn layer on one die of MPW-1 and one of
MPW-5 only. This page gathers what public sources say about the mask
itself — its PDK entry and layers, the plates the process-steps sheet
records, what the public renders show, the lithography it needs and the
rules that constrain it. How the step is performed is on the step page;
every mask is indexed on the {ref}`masks index <masks-index>`.

| | TUNM — Tunnel Mask |
|---|---|
| Mask step | {ref}`TUNM <step-035>`, step 35 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Tunnel Mask", `TUNM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `ctunm` mask 20:0, "Tunnel mask"[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `tunm` drawing 80:20, "SONOS device tunnel implant"[^pdk-06] |
| Minimum CD, feature / space | `TUNMCD` 0.41 / `TUNMCDSP` 0.5[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist is opened over the `tunm` windows and remains elsewhere, which with a positive resist would make the plate dark-field with clear windows (inference). |
| Exposure class | i-line, an inference on the step page from the 0.410 µm width rule; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `190`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 1, 0, 0, 0, 1, 0, 0, 0[^mask-renders] |
| Steps that use the pattern | 5 steps; see {ref}`Steps that use this mask <mask-tunm-steps>` |

## What the mask defines

The PDK describes the drawn layer as "SONOS device tunnel implant" and
gives the `tunm` rule set the function line "Defines SONOS
FETs".[^pdk-06][^pdk-periph] The devices are the memory transistors of
the SONOS cells, of which the PDK says: "The SKY130 process currently
supports two SONOS flash memory cells", an "original cell" and a "“star”
cell" whose "cell size is approximately 25% smaller than the original
cell".[^pdk-07] The rules place each window tightly around one memory
gate: `tunm` extends 0.095 beyond the poly-over-diffusion gate (tunm.3),
keeps 0.095 µm from gates outside it (tunm.4), may not be straddled by a
gate (tunm.5), must lie in deep N-well (tunm.6a) and must be enclosed by
`areaid.ce` (tunm.8), the "Memory (SRAM) core cell identifier".[^pdk-periph][^pdk-06]
The {ref}`TUNM <step-035>` page reads the layer description — an
*implant* layer — as the reason this reference places two implants under
the mask, and the {ref}`PTSI <step-037>` page adds the `lvtn` rule set's
function line, "Define regions to block Vt adjust implant for low Vt LV
PMOS/NMOS, SONOS FETs and Native NMOS", as showing that the memory
transistors do not receive the standard NMOS channel
implants.[^pdk-periph]

The PDK's mask generation table, Table F2b, marks the `TUNM` column `C`
("CREATED") in 5 of its 80 device rows: the two "SONOS fet" rows, the
two "NV SONOS fet" rows and the "NV SONOS Diode" row.[^pdk-06] It marks
`-` ("Layer not created for the device") in 44 rows, among them every
1.8 V, 5 V and high-voltage transistor row and the two "Flash npass"
rows, and `+` ("Layer allowed to overlap") in the other 31, among them
the poly and local-interconnect resistors, the capacitors, the inductors
and most diode rows.[^pdk-06] We read the table as tying the plate's
created data to the memory transistor alone: the "Flash npass" select
transistor of the cell does not receive them (our reading of the rows;
the table does not explain its marks).

What the mask does not define is also worth stating. On the step pages'
readings the {term}`ONO` stack is confined to the cells by a separate
mask, {ref}`ONOM <step-041>`; the memory transistor's own tip implant
comes much later, through {ref}`LDNTM <step-071>`; and the deep N-well
that tunm.6a requires is printed at {ref}`DNM <step-007>` ({ref}`mask-dnm`).
How many masks a SONOS module adds is not published for SKY130. A 2011
Cypress and UMC release says that the 65 nm S65 SONOS process "only
requires three additional mask layers to a standard CMOS process", and
gives no count for the 130 nm S8 process;[^cyp-22] Sun et al. describe
another SONOS-based embedded flash, embedded in logic processes from
0.35 µm to 65 nm, for which "only 3 additional non-critical masks are
needed".[^sun-2011] The {ref}`TUNM <step-035>` page reads `TUNM`, `ONOM`
and `LDNTM` as the SONOS masks of SKY130 (inference from the mask table).

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` has one mask-level layer for this mask, `ctunm` with
purpose `mask` at 20:0 ("Tunnel mask"), and no `drawing`, `mask add`,
`mask drop` or `waffle drop` purpose for it; the drawn layer is `tunm`
at 80:20.[^pdk-06] The pairing rests on those names and descriptions, as
for every mask on the {ref}`masks index <masks-index>`; the PDK publishes
no operation that turns `tunm` into the plate. Rule x.15a confines
"Drawn compatible, mask, and waffle-drop layers" to test modules, the
seal ring and the frame, with the exception "FOM/P1M/Metal waffle drop
are allowed inside the die" (flag P),[^pdk-periph] so a design inside
the die draws `tunm`, not `ctunm` (our reading of x.15a).

The PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance
criteria for GDS data", repeats the `tunm` rules with the same values
("0.41 min. width of tunm", "0.672 min. area of tunm") and words tunm.8
as "tunm must be enclosed by COREID".[^pdk-errors] It names a mask-data
layer `TUNMmk` in three generic checks — "off 0.005 grid TUNMmk vertex"
(x.1b), "non-octagonal TUNMmk edge" (x.3a) and "X.15a: layer TUNMmk
allowed inside areaid:mt or inside areaid.sl or inside areaid.ft" — but
it lists no rule for `ctunm` and, unlike most mask layers, no "nikon
cross" check for it.[^pdk-errors] Table C4b of the *Layers Reference*
carries, in its row for `natfet.dg` {124:21}, the comment "Add TUNM for
SONOS channel implants. See SPR 117559, SGL-529", which the PDK does not
explain.[^pdk-06] Apart from `TUNMCD` and `TUNMCDSP` in Table 2, no row
of *Criteria & Assumptions* names the mask or `tunm`.[^pdk-03]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `TUNM` the site renders layer 80:20 (`tunm`)
alone, with no Boolean expression and no fill layer, on all eight runs;
its mask record gives the mask-level layer 20:0 and the note "TUNM =
tunm sized by ctunm.3".[^mask-renders] Neither the periphery rules nor
the Error Messages page contains a rule named `ctunm.3`,[^pdk-periph][^pdk-errors]
and the site gives no source for the note. The render jobs list only the
drawn layer, with no sizing step, so, as the
{ref}`masks index <masks-renders>` reads the site in general, the images
are unsized drawn data. The note and the choice of layer are one public
derivation from the drawn data, not SkyWater's mask-generation recipe;
they agree with the index's pairing, but both start from the same public
PDK files, so the agreement is not independent.

Two dies of the 320 rendered draw `tunm`: MPW-1, frame A4, with 4
shapes, and MPW-5, frame D7, with 16; no die of MPW-2, MPW-3, MPW-4,
MPW-6, MPW-7 or MPW-8 draws the layer.[^mask-renders] The site renders
`ONOM` from the same layer, so its `ONOM` renders show the same two
dies, and it includes 80:20 in its `LVOM` render
({ref}`masks-derivations`).[^mask-renders] The site states the limits of
its images: "These are renders of *drawn* data, not photomask artwork:
reticle pitch, 4x reduction, mirroring and the frame features the fab
adds are not modelled. Empty images are real results - several masks are
used by no project on a given shuttle."[^mask-renders] Its metadata
carries no plate ID, so a render is tied to a plate in the process-steps
sheet only by the acronym `TUNM`, and the MPW-4 renders come from a
different reticle set from the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a `TUNM` plate
as existing on all eight MPW runs, with the plate number `190` on each
and no "Info" note.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab, which
the renders site calls the run's reticle set
({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA190A` |
| MPW-2 | `5CS8007AC` | `S8007AA190A` |
| MPW-3 | `5CS8008AC` | `S8008AA190A` |
| MPW-4 | `5CS8018AC` | `S8018AA190A` |
| MPW-5 | `5CS8011AC` | `S8011AA190A` |
| MPW-6 | `5CS8014AC` | `S8014AA190A` |
| MPW-7 | `5CS8016AC` | `S8016AA190A` |
| MPW-8 | `5CS8017AC` | `S8017AA190A` |

* **Plates on runs with no drawn `tunm`.** A plate is recorded on MPW-2,
  MPW-3, MPW-4, MPW-6, MPW-7 and MPW-8, on which no rendered die draws
  `tunm`, as well as on MPW-1 and MPW-5.[^steps-sheet][^mask-renders]
  Because the renders leave out whatever the fab adds to a plate, they
  cannot show what those six plates carry, and no public source says;
  for MPW-4 the renders and the plates also belong to different reticle
  sets ({ref}`masks-renders`).
* **Plate number.** `190` is higher than the numbers of masks printed
  after it — `LVOM` (step 44) is `125`, `RPM` (step 49) `175` and `NPCM`
  (step 78) `180` — and the sheet does not say what the numbers encode,
  so no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `TUNM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]

## Lithography and pattern transfer

**Exposure class.** The {ref}`TUNM <step-035>` page puts the 0.410 µm
minimum feature at {math}`k_1 \approx 0.67` at the i-line with an
illustrative NA of 0.6 and infers an i-line level; the
{ref}`i-line stepper <machine-i-line-stepper>` page lists it there.
SkyWater lists "ASML I-line stepper" and "ASML I-line scanner" among its
tools but assigns no layer to them.[^skw-01] At the NA 0.48 low end of
ASML's PAS 5500/275D[^asml-pas5500-275d] the same feature has
{math}`k_1 \approx 0.54` (our arithmetic). One Cypress integration
patent, describing its own SONOS channel window, takes the other view
for tight layouts: "because the undercut of window 305 may become very
close to an adjacent logic device, critical layer lithography tools are
employed to reduce misregistration tolerances".[^pat-03] That is the
patent's flow, not a statement about SKY130.

**Mask errors.** Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns";[^wong-1998]
at 365 nm that threshold is about 0.38 µm at NA 0.48 and 0.30 µm at
NA 0.60 (our arithmetic), so the 0.41 µm windows lie just above it.

**Resist.** On the step pages' reading the resist sits on an organic
anti-reflective coating — the separate ARC etch at
{ref}`TUNARCE <step-036>` is the step page's evidence — and is about
1 µm thick, the PDK's generic "Photoresist thickness" being
1.14 µm.[^pdk-03] It has to survive a plasma ARC etch, two implants and
a wet oxide etch before it is removed, and the {ref}`TUNM <step-035>`
page includes a hard bake "to harden the resist for the implants". Baker and Capsuto studied CD
control with an anti-reflective coating on an i-line 0.35 µm
device,[^baker-1996] and Ross et al. stabilised i-line implant resists
with a flood electron beam, reducing shrinkage and CD variation and
eliminating popping.[^ross-1996] SkyWater's resist, ARC and bake are not
public; the consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Pattern transfer.** On the step pages' readings the pattern is used
four times. {ref}`TUNARCE <step-036>` opens the ARC in the windows, on
the {ref}`silicon and polysilicon plasma etcher <machine-plasma-etcher-silicon>`
class; {ref}`PTSI <step-037>` and {ref}`DEPI <step-038>` implant through
them on the {ref}`medium-current implanter <machine-medium-current-implanter>`
class; and {ref}`TUNME <step-039>` removes the oxide in them in dilute HF
or buffered HF on the {ref}`wet bench <machine-wet-bench>` class, with
the resist strip and pre-oxidation clean treated as part of that step.
A Cypress embedded-SONOS patent describes the same sequence: "a patterned
tunnel mask 220 is formed on or overlying the pad oxide 209, ions … are
implanted through a window or opening in the tunnel mask to form a
channel 224 for a NVM transistor 226", and "The tunnel mask can include
a photoresist layer, or a hard mask formed, from a patterned nitride or
silicon-nitride layer".[^pat-04] The isotropic etch widens each window
beyond the resist edge; the integration patent notes that "The isotropic
etch of the screening sacrificial dielectric layer 303 can be expected
to undercut the photoresist 307" and that in its flow "a 0.2 um drawn
size may be downsized to 0.18 um to compensate for an undercut of
0.01 um on a side".[^pat-03] Whether SKY130's `ctunm` data are sized is
not public; the renders' "sized by ctunm.3" note names no source.

**Resist edges.** Ions scattered out of an implant resist edge alter the
threshold of nearby transistors, with shifts "of up to 100 mV … over a
lateral distance on the order of a micrometer" in Hook et al.'s
work;[^hook-2003] the {ref}`TUNM <step-035>` page cites the study for
the 0.095 µm `tunm` clearances. The PDK does not say what those
clearances allow for; we read them as placement margins against the gate
(inference).

**Overlay.** The {ref}`TUNM <step-035>` page reads the mask as aligned to
the trench pattern of {ref}`FOM <step-004>`, and the
{ref}`ONOM <step-041>` page reads the next mask as aligned to this one,
since the ONO island must enclose the window. ASML specifies "≤ 40 nm"
single-machine overlay for the /275D stepper[^asml-pas5500-275d] against
the 0.095 µm of tunm.3 and tunm.4 (our comparison; SkyWater's overlay
budget is not public). van Haren et al. show how alignment-mark
placement accuracy limits layer-to-layer overlay.[^van-haren-2019]

(mask-tunm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `TUNM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`TUNM <step-035>`, {ref}`TUNARCE <step-036>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`TUNME <step-039>`

* {ref}`TUNM <step-035>` — coats the anti-reflective coating and resist,
  exposes and develops the windows.
* {ref}`TUNARCE <step-036>` — etches the anti-reflective coating out of
  the windows, stopping on the oxide beneath.
* {ref}`PTSI <step-037>` — the first implant through the windows, a
  sub-surface punch-through stop on its page's reading.
* {ref}`DEPI <step-038>` — the second implant through the same windows,
  the depletion implant of the memory channel.
* {ref}`TUNME <step-039>` — removes the oxide in the windows; the step
  list used in this reference has no separate strip step, and the step
  page treats the resist strip and pre-oxidation clean as part of this
  etch.

On its step page's reading, the next step, {ref}`ONO <step-040>`, grows
the tunnel oxide on the cleared silicon and forms the oxide–nitride–oxide
stack over the whole wafer after the resist is gone, so it is not listed:
it does not use the `TUNM` resist. The next mask step is
{ref}`ONOM <step-041>`. There is no exception to the rule for this mask.

## Design rules and critical dimensions

The `tunm` rules of the periphery rules, with the `hvi` rule that names
the layer and rule x.15a; flag TC means "Rule not checked for cell name
“\*_tech_CD_top\*”", and flag P "Rule applies to periphery only (outside
areaid.ce). A corresponding core rule may or may not exist.". The unit
column of tunm.3 is blank in the published table.[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| tunm.1 | "Min width of tunm" | 0.410 µm |
| tunm.2 | "Min spacing of tunm to tunm" | 0.500 µm |
| tunm.3 | "Extension of tunm beyond (poly and diff)" | 0.095 |
| tunm.4 | "Min spacing of tunm to (poly and diff) outside tunm" | 0.095 µm |
| tunm.5 | "(poly and diff) may not straddle tunm" | — |
| tunm.6a | "Tunm outside deep n-well is not allowed" (TC) | — |
| tunm.7 | "Min tunm area" | 0.672 µm² |
| tunm.8 | "tunm must be enclosed by areaid.ce" | — |
| hvi.4 | "Hvi must not overlap tunm" | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |

Table 2 of *Criteria & Assumptions* repeats the width and space as
`TUNMCD` 0.41 and `TUNMCDSP` 0.5, and the Error Messages page gives the
same 0.41, 0.5, 0.095 and 0.672.[^pdk-03][^pdk-errors] For the plate,
the smallest features are therefore 0.410 µm windows on 0.500 µm spaces
with an area of at least 0.672 µm²; hvi.4 keeps the windows out of the
thick-oxide regions that {ref}`LVOM <step-044>` works with, on the step
pages' reading. Because tunm.8 confines the windows to `areaid.ce`, whose
internal rules the PDK does not publish, the pitch of the windows inside
a memory array cannot be derived from these rules alone (the
{ref}`TUNM <step-035>` page's reading).

## Related pages

* {ref}`TUNM <step-035>`, {ref}`TUNARCE <step-036>`,
  {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>` and
  {ref}`TUNME <step-039>` — the mask step, the ARC etch, the two
  implants and the oxide etch.
* {ref}`ONO <step-040>` and {ref}`ONOM <step-041>` — the stack grown in
  the windows and the mask that confines it; {ref}`mask-onom` — the ONO
  mask's page.
* {ref}`mask-dnm` — the deep N-well mask; tunm.6a keeps the windows
  inside deep N-well.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the runs whose plates have no drawn shapes.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-medium-current-implanter` and {ref}`machine-wet-bench` —
  the implant and wet-etch classes that use the pattern.
* {ref}`material-lithography-materials` — resists, anti-reflective
  coatings, developer and reticles.
* {ref}`category-lithography`, {ref}`category-implant` and
  {ref}`category-etch` — the mask step, implant and etch categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "Tunnel Mask, TUNM,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `tunm` 80:20,
  `ctunm` 20:0, `areaid.ce`, the Table C4b comment and the `TUNM`
  column of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `TUNMCD`/`TUNMCDSP` and the
  photoresist thickness.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `tunm` rules and function line,
  hvi.4, the `lvtn` function line, x.15a and the flag
  legend.[^pdk-periph]
* SkyWater PDK, *Error Messages* page and `errors.csv` — the `tunm`
  messages and the `TUNMmk` checks.[^pdk-errors]
* SkyWater PDK, *Device Details* — the two SONOS cells.[^pdk-07]
* *S8 / SKY130 Process Steps* sheet — the step, the `TUNM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `TUNM` renders, their layer
  and note, and the per-die shape counts.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the i-line exposure
  tools.[^skw-01]
* ASML, *PAS 5500/275D* data sheet — NA range and single-machine
  overlay of an i-line stepper.[^asml-pas5500-275d]
* Koutny et al. (Cypress), US 8,093,128 — window undercut, window sizing
  and critical-layer lithography in one SONOS integration.[^pat-03]
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — the
  tunnel mask, the implant through it and its removal.[^pat-04]
* Cypress/UMC press release — "three additional mask layers" for the
  S65 process; no count is given for S8.[^cyp-22]

### High-level understanding

* Wikipedia, *SONOS* — the oxide–nitride–oxide memory
  transistor.[^cyp-26]
* Wikipedia, *Photomask* — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wikipedia, *Ion implantation* — masking, range and
  energy.[^wiki-implant]
* Mack, *Fundamental Principles of Optical Lithography* — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* Levinson, *Principles of Lithography* — overlay budgets and the tool
  choice for non-critical levels.[^levinson-2005]

### Deep dive

* Sun et al., ICICDT 2011 — a SONOS-based embedded flash needing "only 3
  additional non-critical masks".[^sun-2011]
* White, Adams and Bu, *IEEE Circuits and Devices* 2000 — a review of
  scaled SONOS.[^pap-01]
* Seo et al. (Samsung), *IEEE JSSC* 2005 — a 130 nm local-SONOS embedded
  flash from another vendor.[^pap-02]
* Kim et al. (Samsung), VLSI 2003 — a manufacturable embedded SONOS
  module.[^pap-03]
* Taniguchi et al., IMW 2023 — SONOS embedded flash on a 130 nm platform
  with three added masks.[^pap-05]
* Jiew, Chien and Yung, NVMTS 2012 — a 2T-SONOS cell for embedded
  flash.[^jiew-2012]
* Ramkumar, Prabhakar and Kapre (Cypress), Semiconductor Digest 2020 —
  the integration cost of embedded SONOS.[^cyp-25]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  size below which it rises.[^wong-1998]
* Baker and Capsuto, *Proc. SPIE* 1996 — CD control with an
  anti-reflective coating on an i-line 0.35 µm device.[^baker-1996]
* Ross et al., *Proc. SPIE* 1996 — electron-beam stabilisation of i-line
  implant resists.[^ross-1996]
* Hook et al., *IEEE TED* 2003 — ions scattered from the resist edge and
  the threshold shifts they cause.[^hook-2003]
* van Haren et al., *Proc. SPIE* 2019 — alignment-mark placement and
  layer-to-layer overlay.[^van-haren-2019]
* ITRS 2001, *Lithography* — mask magnification and the optical mask
  requirements of the 130 nm generation.[^itrs-03]

## Open questions

* The operation that makes the `ctunm` plate data from `tunm`, and
  whether it sizes the windows, is not published; the renders site's
  note names a "ctunm.3" that neither the periphery rules nor the Error
  Messages page contains.[^pdk-periph][^pdk-errors][^mask-renders]
* What the `TUNM` plates of MPW-2, MPW-3, MPW-4, MPW-6, MPW-7 and MPW-8
  carry is not public: no rendered die of those runs draws `tunm`, and
  the renders omit whatever the fab adds.[^steps-sheet][^mask-renders]
* The plate's tone, blank, absorber and magnification, the resist and
  anti-reflective coating, and the exposure tool are not public; the
  i-line reading rests on the 0.410 µm rule.
* The Error Messages page lists no "nikon cross" check for `TUNMmk`,
  and Table C4b's "Add TUNM for SONOS channel implants" comment is not
  explained; the PDK does not say what either
  implies.[^pdk-errors][^pdk-06]
* What the plate number `190` encodes is not stated, and no public source
  lists the `TUNM` plate of the original MPW-4 set
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
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* (including Table C4b,
    purpose layer descriptions, and Table F2b, the mask generation
    table) and `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (all tables),
    SkyWater SKY130 PDK documentation.
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
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_TUNM/`
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
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098 B1,
    granted 2014-08-05. <https://patents.google.com/patent/US8796098B1/en>
[^cyp-22]: Cypress Semiconductor / UMC, *Cypress and UMC Deliver ICs on
    New 65-Nanometer SONOS Embedded Flash Technology*, PR Newswire,
    2011-07-27.
    <https://www.prnewswire.com/news-releases/cypress-and-umc-deliver-ics-on-new-65-nanometer-sonos-embedded-flash-technology-126238008.html>
[^cyp-25]: K. Ramkumar, V. Prabhakar and R. Kapre (Cypress
    Semiconductor), *Scalable SONOS based embedded non-volatile memory
    technology*, Semiconductor Digest, 2020-02.
    <https://sst.semiconductor-digest.com/2020/02/scalable-sonos-based-embedded-non-volatile-memory-technology/>
[^cyp-26]: Wikipedia, *SONOS*. <https://en.wikipedia.org/wiki/SONOS>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^sun-2011]: W.-T. Sun, C.-J. Liu, C.-Y. Lo, Y.-J. Ting, Y.-J. Chen,
    T.-Y. Wu, E.-H. Toh, X.-H. Yuan, K.-L. Low, Q. Han, Y.-S. You,
    Y.-K. Leung and S.-T. Woo, "Low-cost embedded Flash memory
    technology", *2011 IEEE International Conference on IC Design &
    Technology (ICICDT)*, pp. 1–5.
    <https://doi.org/10.1109/ICICDT.2011.5783211>
[^pap-01]: M. H. White, D. A. Adams and J. Bu, "On the go with SONOS",
    *IEEE Circuits and Devices Magazine* **16**(4), 22–31 (2000).
    <https://doi.org/10.1109/101.857747>
[^pap-02]: M.-K. Seo, S.-H. Sim, M.-H. Oh, H.-S. Lee, S.-W. Kim,
    I.-W. Cho, G.-H. Kim and M.-G. Kim (Samsung), "A 130-nm 0.9-V
    66-MHz 8-Mb (256K × 32) local SONOS embedded flash EEPROM", *IEEE
    Journal of Solid-State Circuits* **40**(4), 877–883 (2005).
    <https://doi.org/10.1109/JSSC.2005.845564>
[^pap-03]: J.-H. Kim, I. W. Cho, G. J. Bae, S. S. Kim, K. C. Kim,
    S. H. Kim, K. W. Koh, N. I. Lee, H.-K. Kang, K.-P. Suh, S. T. Kang,
    M. K. Seo, S. H. Lee, M. C. Kim and I. S. Park (Samsung), "Highly
    manufacturable SONOS non-volatile memory for the embedded SoC
    solution", *2003 Symposium on VLSI Technology, Digest of Technical
    Papers*, pp. 31–32. <https://doi.org/10.1109/VLSIT.2003.1221071>
[^pap-05]: Y. Taniguchi et al., "SONOS Embedded Flash IP Using
    Trap-Depth-Controlled SiN Film Enabling Data Retention more than
    10 years at 200°C", *2023 IEEE International Memory Workshop
    (IMW)*, pp. 1–4. <https://doi.org/10.1109/IMW56887.2023.10145990>
[^jiew-2012]: C. B. Jiew, Y. E. Chien and R. T. T. Yung, "Development
    of a robust 2T-SONOS cell for embedded flash application", *2012
    12th Annual Non-Volatile Memory Technology Symposium (NVMTS)*,
    pp. 1–6. <https://doi.org/10.1109/NVMTS.2013.6632849>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
[^baker-1996]: D. C. Baker and E. S. Capsuto, "Critical dimension
    control for i-line 0.35-μm device using a new antireflective
    coating", *Proc. SPIE* **2724**, Advances in Resist Technology and
    Processing XIII, 710 (1996). <https://doi.org/10.1117/12.241869>
[^ross-1996]: M. F. Ross, W. R. Livesay, V. Starov, K. Ostrowski and
    S. Y. Wong, "Photoresist stabilization for ion implant processing",
    *Proc. SPIE* **2724**, 632 (1996).
    <https://doi.org/10.1117/12.241862>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices* **50**(9),
    1946–1951 (2003). <https://doi.org/10.1109/TED.2003.815371>
[^van-haren-2019]: R. J. F. van Haren, S. Steinert, O. Mouraille,
    K. D'havé, L. van Dijk, J. Hermans and D. Beyer, "Wafer alignment
    mark placement accuracy impact on the layer-to-layer overlay
    performance", *Proc. SPIE* **11148**, Photomask Technology 2019, 37
    (2019). <https://doi.org/10.1117/12.2536270>
