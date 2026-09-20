(mask-p1m)=
# P1M — Poly 1

The poly mask is the {term}`reticle` that draws every polysilicon shape
of SKY130 in one exposure: on the {ref}`P1M <step-061>` page's reading,
the resist printed through it at step 61 stays wherever poly is to
remain — every transistor gate, poly interconnect, poly resistor body and
{term}`SONOS` gate — and the {ref}`P1ME <step-062>` etch removes the gate
stack everywhere else. Because the etched poly width is the transistor
gate length, this is the mask whose {term}`CD` matters most to device
behaviour, and the step pages read it as a critical KrF level. This page
gathers what public sources say about the mask itself — its PDK entry
and layers, the plates the process-steps sheet records for the MPW runs,
what the public renders of those runs show, the lithography it needs and
the rules that constrain it. How the step is performed is on the step
page; every mask is indexed on the {ref}`masks index <masks-index>`.

| | P1M — Poly 1 |
|---|---|
| Mask step | {ref}`P1M <step-061>`, step 61 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Poly 1", `P1M`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cp1m` mask 28:0, "Poly 1 mask"; mask add 33:43, mask drop 33:42, waffle drop 33:24[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `poly` drawing 66:20, "Polysilicon", with gate 66:9 and resistor 66:13 purposes[^pdk-06] |
| Minimum CD, feature / space | `P1MCD` N/A / `P1MCDSP` 0.14; "Endcap/Gap" `P1G` 0.15 / 0.21[^pdk-03] |
| Polarity and tone | Not published. Poly is drawn where it remains, so with a positive resist the plate would be clear-field (the step page's reading). |
| Exposure class | KrF (248 nm), an inference on the step page from the 0.150 µm poly width; no public source names the tool ({ref}`machine-duv-krf-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `210`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-p1m-steps>` |

## What the mask defines

The periphery rules give the function of the `poly` layer as "Defines
FET gates, interconnects and resistors".[^pdk-periph] The mask therefore
carries three kinds of feature with different demands: gate lines,
whose width is the channel length and whose minimum is 0.150 µm
(poly.1a); poly wiring on the field oxide; and poly resistor bodies, at
least 0.330 µm wide (poly.3).[^pdk-periph] [*Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>)
gives 0.33 and 0.48 as the "Poly resistor width and spacing to reduce CD
variation (um)" (`POLYRCD`, `POLYRSPC`), the same numbers as rules poly.3
and poly.9, so the PDK ties the resistor rules to the CD variation of
this level.[^pdk-03][^pdk-periph]

The PDK's mask generation table, Table F2b, marks the `P1M` column `C`
("CREATED") in 40 of its 80 device rows: the n+ and p+ poly resistors,
the 17 rows of its "32 A CMOS" group (the 1.8 V transistors, core
devices and varactors), the four SONOS rows, the 13 rows of its "110A
CMOS" group (the 5/10.5 V, native, flash pass-gate, 16 V and 20 V
devices) and the four ESD transistor rows.[^pdk-06] The rows it leaves
unmarked are the diffusion, well, local-interconnect and metal-fuse
resistors, the capacitors, inductors, diodes and bipolar
transistors[^pdk-06] — devices without a poly gate or poly body (our
reading of the table).

Two things the mask does not define are worth separating from it. The
gate stack it patterns — gate oxides, poly, nitride cap and oxide cap —
is laid down by earlier steps ({ref}`LVGOX <step-047>`,
{ref}`SAGD <step-048>`, {ref}`GATENIT <step-058>`,
{ref}`POC <step-059>`), and the poly doping that distinguishes gates
from resistor bodies comes from the resistor masks before it
({ref}`RPM <step-049>`, {ref}`RRPM <step-052>`,
{ref}`URPM <step-055>`), on the step pages' readings. On the same
readings, the tip and halo implants take the etched poly, and the
source/drain implants the spacers formed on it, as their edge, not this
resist.

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives the mask-level layer `cp1m` four purposes: `mask`
at 28:0 ("Poly 1 mask"), and `mask add` 33:43, `mask drop` 33:42 and
`waffle drop` 33:24 on a different layer number.[^pdk-06] The drawn
layer is `poly` at 66:20, with `gate` (66:9) and `resistor` (66:13)
purposes among others; the PDK does not publish how these combine into
the plate.[^pdk-06] Two rules show what a designer may place on the mask
layers. Rule x.9: "Shapes on maskAdd or maskDrop layers (“serifs”) are
allowed in core only", and rule x.15a, which confines mask and
waffle-drop layers to test modules, seal ring and frame, makes one
exception: "FOM/P1M/Metal waffle drop are allowed inside the
die" (flag P, periphery only).[^pdk-periph] The {ref}`FOM <step-004>`
page reads the "waffles" as dummy fill for {term}`pattern density`; the PDK does not say whether
a waffle-drop shape places fill or keeps it out, and the purpose name
does not settle it.

The layer table also has `areaid.op` (81:54), "OPC drop. Block automatic
OPC (for fab blocks and lithocal structures)",[^pdk-06] which implies
that automatic {term}`OPC` is applied to some mask data, and rule x.1a
names P1M among the layers it applies to. Rule x.1a reads "p1m.md (OPC),
DECA and AMKOR layers (pi1.dg, pmm.dg, rdl.dg, pi2.dg, ubm.dg, bump.dg)
and mask data for p1m, met1, via, met2 must be on a grid of mm", with the
value 0.001 (unit printed as "mm"), against 0.005 for "all layers except
those mentioned in 1a" (x.1b).[^pdk-periph] We read "(OPC)" and the
finer grid as a sign that the poly mask data are proximity-corrected
(inference); the PDK does not expand "md" or say what the correction
is. [*Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) sets a
"Min process bias 3s tolerance for poly" of 0.02 (`PHP1TOL`), against a
general "Min process bias 3s tolerance" of 0.032 (`PHTOL`),[^pdk-03] so
the PDK assumes tighter bias control for poly than for other layers; it
does not say how the drawn-to-printed bias is set.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `P1M` the site renders layer 66:20 (`poly`)
together with 28:28, which it lists as a fill layer, with no Boolean
expression and no note, on all eight runs; its mask record gives the
mask-level layer 28:0.[^mask-renders] Layer 28:28 is not in
`gds_layers.csv`,[^pdk-06] so the site's
choice of it is one public reading of the tape-out files, not a PDK
definition, and like the site's other layer choices it is not
SkyWater's mask-generation recipe ({ref}`masks-derivations`). Every
rendered die of every run carries shapes on these layers.[^mask-renders]

The images are drawn data: "These are renders of *drawn* data, not
photomask artwork: reticle pitch, 4x reduction, mirroring and the frame
features the fab adds are not modelled."[^mask-renders] They therefore
show the drawn gate widths, not any OPC or bias the plate may carry
(inference from that statement). The metadata carries no plate ID, so a
render is tied to a plate in the process-steps sheet only by the acronym
`P1M`, and the MPW-4 renders come from a different reticle set from the
one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a `P1M` plate
as existing on all eight MPW runs, with the plate number `210` on each
and no "Info" note.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA210A` |
| MPW-2 | `5CS8007AC` | `S8007AA210A` |
| MPW-3 | `5CS8008AC` | `S8008AA210A` |
| MPW-4 | `5CS8018AC` | `S8018AA210A` |
| MPW-5 | `5CS8011AC` | `S8011AA210A` |
| MPW-6 | `5CS8014AC` | `S8014AA210A` |
| MPW-7 | `5CS8016AC` | `S8016AA210A` |
| MPW-8 | `5CS8017AC` | `S8017AA210A` |

* **Plate number.** The sheet does not say what `210` encodes, and the
  plate numbers do not follow process order ({ref}`masks-mpw-reticle-sets`),
  so no process position is read from it.[^steps-sheet]
* **Mask type.** The sheet's "Sheet4" tab gives no type for
  `P1M`.[^steps-sheet] Whether the plate is binary or an
  {term}`attenuated phase-shift mask <attenuated PSM>` — the two options
  the {ref}`P1M <step-061>` page discusses — is not on public record.
  4× is the ITRS 2001 mask magnification for the 130 nm
  generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`P1M <step-061>` page puts the 0.150 µm
line at {math}`k_1 \approx 0.36–0.42` on a KrF lens of NA 0.6–0.7 and at
{math}`k_1 \approx 0.25–0.29` at the i-line, and infers a 248 nm level;
the {ref}`KrF stepper <machine-duv-krf-stepper>` page lists it there.
ASML's PAS 5500/750E, introduced in 2000, "achieves 130 nm resolution
while using standard 248 nm light" with overlay "less than
30 nm".[^asml-750e] SkyWater lists "ASML DUV stepper" and "ASML DUV
scanner" but assigns no layer to them.[^skw-01]

**Mask errors.** At this {math}`k_1` a CD error on the plate prints
larger than it is. Wong et al. found that the mask error factor "is
unity for large features, but increases rapidly when the critical
dimension (CD) is less than 0.5 (lambda) /NA for line-space patterns";
the threshold at 248 nm and NA 0.7 is about 177 nm (our arithmetic),
above the 150 nm gate. They also found dense lines more sensitive than
isolated ones and light-field lines less sensitive than dark-field
spaces.[^wong-1998] Kuijten, Duray and der Kinderen, on an ASML
PAS 5500/300 at 0.25 µm, separated a reticle CD error component of
10 nm (3σ), from 32 nm (3σ) mask CD uniformity and a reticle sensitivity
factor of 1.3, from an exposure-tool component of 8 nm,[^kuijten-1998]
and Arthur and Martin followed the mask error factor through CD budgets
into reticle procurement specifications.[^arthur-1999] ITRS 2001's
optical mask requirements, which are "for critical layers", ask in the
130 nm year for a mask CD uniformity of 7.4 nm (3σ) on isolated MPU gate
lines on a binary mask, at 4× magnification.[^itrs-03] How tightly
SkyWater specifies the `P1M` plate is not public; the PDK's 0.02
`PHP1TOL` and Table 7's "P1M additional CD control" of 0.011
(`P1MCDcontrol`) are the only published poly CD figures, and neither
says what it is measured on (plate or wafer).[^pdk-03]

**Proximity and line ends.** Gate levels suffer line-end shortening,
which "reduces the wafer process latitude and in some cases even
eliminates the level-to-level overlay margin"; Garofalo et al. reduced
it on ASIC gate levels by mask compensation and modified
illumination.[^garofalo-1995] At the 130 nm node Zheng et al. studied
how well one OPC model for the gate line width holds across the field
and across several scanners.[^zheng-2003] Rules-based
OPC,[^otto-1994] the phase-shifting mask[^levenson-1982] and its
attenuated form[^lin-1993] are the techniques the step page names as
likely but unconfirmed for this level; the endcap rule poly.8, 0.130
beyond diffusion,[^pdk-periph] is the margin that line-end shortening
would consume (our reading).

**Resist and tone.** The step page reads a chemically amplified positive
KrF resist over an anti-reflective scheme, and a clear-field plate as
the consequence of drawing poly where it remains; neither the resist nor
the tone is published. The consumables are on the
{ref}`lithography materials <material-lithography-materials>` page and
the coat and develop on the
{ref}`coat/develop track <machine-coat-develop-track>` page.

**Pattern transfer.** On the step pages' readings the resist pattern is
transferred by {ref}`P1ME <step-062>` through the oxide cap, the nitride
cap and the poly, stopping on the gate oxides, on the
{ref}`silicon and polysilicon plasma etcher <machine-plasma-etcher-silicon>`
class, and the resist is stripped within that step. Orshansky, Milor and
Hu characterised spatial intrafield gate-CD variation, which they found
"strongly dependent on the local layout patterns", and proposed a
mask-level correction for it.[^orshansky-2004]

**Overlay.** The step page infers that `P1M` aligns to the STI marks of
{ref}`FOM <step-004>`. The placement margins against active are
0.130 beyond diffusion (poly.8) and 0.250 of diffusion beyond poly
(poly.7), with poly on field kept 0.075 µm from diffusion
(poly.4);[^pdk-periph] on the step pages' readings the tip and halo
implants and the spacers that follow take the etched gate as their
reference. Starikov analysed the accuracy of the overlay
measurements on which such margins rely.[^starikov-1992]

(mask-p1m-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `P1M` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`P1M <step-061>`, {ref}`P1ME <step-062>`

* {ref}`P1M <step-061>` — coats, exposes and develops the resist.
* {ref}`P1ME <step-062>` — etches the gate stack through the resist; the
  step list used in this reference has no separate strip step, and the
  step page treats the resist strip as part of the etch.

On its step page's reading, the next step, {ref}`IOX45 <step-063>`,
grows a thin oxide on the etched poly and exposed silicon after the
resist is gone, and the next mask step is
{ref}`NTM <step-064>`. The only departure from a mask–etch–strip pattern
is that the strip has no step of its own; the rule itself needs no
exception. The later steps that self-align to the gate
({ref}`NTM <step-064>` onwards, {ref}`SPE <step-077>`) use the etched
poly, not this resist, and are not listed.

## Design rules and critical dimensions

The `poly` rules of the periphery rules, with the grid rules x.1a and
x.1b and the poly row of x.2; flag P means "Rule applies to
periphery only (outside areaid.ce). A corresponding core rule may or may
not exist.", and the unit column of poly.7 and poly.8 is blank in the
published table.[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| poly.1a | "Width of poly" | 0.150 µm |
| poly.1b | "Min channel length (poly width) for pfet overlapping lvtn […]" | 0.350 µm |
| poly.2 | "Spacing of poly to poly except for poly.c2 and poly.c3 […]" | 0.210 µm |
| poly.3 | "Min poly resistor width" | 0.330 µm |
| poly.4 | "Spacing of poly on field to diff (parallel edges only)" (P) | 0.075 µm |
| poly.5 | "Spacing of poly on field to tap" (P) | 0.055 µm |
| poly.6 | "Spacing of poly on diff to abutting tap (min source)" (P) | 0.300 µm |
| poly.7 | "Extension of diff beyond poly (min drain)" (P) | 0.250 |
| poly.8 | "Extension of poly beyond diffusion (endcap)" (P) | 0.130 |
| poly.9 | "Poly resistor spacing to poly or spacing (no overlap) to diff/tap" | 0.480 µm |
| poly.10 | "Poly can't overlap inner corners of diff" | — |
| poly.11 | "No 90 deg turns of poly on diff" | — |
| x.1a | "p1m.md (OPC), DECA and AMKOR layers (pi1.dg, pmm.dg, rdl.dg, pi2.dg, ubm.dg, bump.dg) and mask data for p1m, met1, via, met2 must be on a grid of mm" | 0.001 (unit "mm") |
| x.1b | "Data for SKY130 layout and mask on all layers except those mentioned in 1a must be on a grid of mm (except inside Seal ring)" | 0.005 (unit "mm") |
| x.2 | Angles on poly "n x 90" deg, "except for ESD flare gates or gated_npn" | — |

Table 2 of *Criteria & Assumptions* gives two "Poly 1" rows: an
"Endcap/Gap" row with 0.15 and 0.21 under `P1G`, and a row with "N/A"
and 0.14 under `P1MCD` and `P1MCDSP`, which the table does not
explain.[^pdk-03] Table 4 gives the poly thickness as 0.18
(`POLYTH`) and the "Channel length for low Vt PMOS" as 0.35
(`lvtpmos_poly`), matching poly.1b.[^pdk-03][^pdk-periph] Table 7,
"Other criteria and parameters", has a row named for this mask, "P1M
additional CD control", 0.011 (`P1MCDcontrol`), and the same table gives
a "Field oxide etchback after P1ME before implants" of 0.04
(`WFDEL`);[^pdk-03] neither row has a unit or says what the value
applies to. The smallest
feature the plate must resolve is therefore the 0.150 µm gate line on a
0.210 µm space.

## Related pages

* {ref}`P1M <step-061>` and {ref}`P1ME <step-062>` — the mask step and
  the gate etch.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the tables this page's plate facts are taken from.
* {ref}`machine-duv-krf-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-plasma-etcher-silicon` — the etch class that transfers
  the pattern.
* {ref}`machine-cd-sem-overlay-metrology` — gate CD and overlay
  measurement.
* {ref}`material-lithography-materials` — resists, anti-reflective
  coatings, developer and reticles.
* {ref}`category-lithography` and {ref}`category-etch` — the mask step
  and etch categories.

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Poly 1, P1M,
  X".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `poly` and
  its purposes, `cp1m` and its purposes, `areaid.op`, and the `P1M`
  column of Table F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `P1G`, `P1MCD`/`P1MCDSP`,
  `PHP1TOL`, `P1MCDcontrol`, `POLYTH` and the poly resistor CD
  criteria.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `poly` rules, x.1a, x.1b, x.2,
  x.9, x.15a and the flag legend.[^pdk-periph]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the `P1M` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `P1M` renders and their
  layers.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the DUV exposure
  tools.[^skw-01]
* [ASML, PAS 5500/750E press release](<https://www.asml.com/en/news/press-releases/2000/asml-introduces-krf-lithography-scanner-optimized-for>) — a KrF scanner for 130 nm design
  rules.[^asml-750e]

### High-level understanding

* [Wikipedia, *Photomask*](<https://en.wikipedia.org/wiki/Photomask>) — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wikipedia, [*Phase-shift mask*](<https://en.wikipedia.org/wiki/Phase-shift_mask>) and [*Optical proximity correction*](<https://en.wikipedia.org/wiki/Optical_proximity_correction>) —
  why mask shapes differ from drawn shapes.[^wiki-psm][^wiki-opc]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — imaging at
  low {math}`k_1`.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) — deep-submicron
  gate lithography.[^txt-05]

### Deep dive

* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor of lines
  and spaces and the size below which it rises.[^wong-1998]
* [Arthur and Martin, *Proc. SPIE* 1999](<https://doi.org/10.1117/12.350880>) — mask error factor, CD budgets
  and reticle specifications.[^arthur-1999]
* [Kuijten, Duray and der Kinderen, *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310792>) — the reticle's
  share of intrafield CD uniformity on a DUV stepper.[^kuijten-1998]
* [Garofalo et al., *Proc. SPIE* 1995](<https://doi.org/10.1117/12.209250>) — gate-level line-end shortening
  and its mask compensation.[^garofalo-1995]
* [Zheng et al., *Proc. SPIE* 2003](<https://doi.org/10.1117/12.485431>) — optical proximity matching of the
  130 nm gate line width across the field and across
  scanners.[^zheng-2003]
* [Otto et al., *Proc. SPIE* 1994](<https://doi.org/10.1117/12.175422>) — rules-based optical proximity
  correction.[^otto-1994]
* [Levenson, Viswanathan and Simpson, *IEEE TED* 1982](<https://doi.org/10.1109/T-ED.1982.21037>) — the
  phase-shifting mask.[^levenson-1982]
* [Lin, *IEEE Circuits and Devices* 1993](<https://doi.org/10.1109/101.200850>) — alternating and attenuated
  phase-shift masks.[^lin-1993]
* [Orshansky, Milor and Hu, *IEEE TSM* 2004](<https://doi.org/10.1109/TSM.2003.822735>) — intrafield gate-CD
  variability and mask-level correction.[^orshansky-2004]
* [Starikov, *Opt. Eng.* 1992](<https://doi.org/10.1117/12.56172>) — the accuracy of overlay
  measurement.[^starikov-1992]
* [Rizvi (ed.), *Handbook of Photomask Manufacturing Technology*](<https://doi.org/10.1201/9781420028782>) — mask
  writing, advanced optical masks and mask metrology.[^rizvi-2005]
* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — gate CD targets and the optical mask
  requirements for critical layers at 130 nm.[^itrs-03]

## Open questions

* The operation that makes the `cp1m` plate data from `poly` and the
  `cp1m` add, drop and waffle-drop purposes is not published.[^pdk-06]
  Rule x.1a ties P1M to OPC, but the PDK does not describe the
  correction or any bias applied to this mask.[^pdk-periph]
* The plate's type (binary or attenuated phase-shift), tone and CD
  specification, the resist and the exposure tool are not public; the
  KrF reading rests on the 0.150 µm rule.
* Table 2's second "Poly 1" row ("N/A" and 0.14) is not explained, and
  the blank unit column of poly.7 and poly.8 is read as µm by the step
  page.[^pdk-03][^pdk-periph]
* The renders' fill layer 28:28 is not in `gds_layers.csv`, so what the
  site takes it to be rests on the site alone.[^mask-renders][^pdk-06]
* What the plate number `210` encodes is not stated, and no public source
  lists the `P1M` plate of the original MPW-4 set
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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 4
    and 7), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_P1M/`
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
[^wiki-psm]: Wikipedia, *Phase-shift mask*.
    <https://en.wikipedia.org/wiki/Phase-shift_mask>
[^wiki-opc]: Wikipedia, *Optical proximity correction*.
    <https://en.wikipedia.org/wiki/Optical_proximity_correction>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
[^arthur-1999]: G. G. Arthur and B. Martin, "Mask error factor and
    critical dimension budgets for sub-half-micron CMOS processes",
    *Proc. SPIE* **3677**, 918 (1999).
    <https://doi.org/10.1117/12.350880>
[^kuijten-1998]: J. P. Kuijten, F. Duray and T. der Kinderen, "Reticle
    contributions to CD uniformity for 0.25-μm DUV lithography", *Proc.
    SPIE* **3334**, 620 (1998). <https://doi.org/10.1117/12.310792>
[^garofalo-1995]: J. G. Garofalo, J. DeMarco, J. Bailey, J. Xiao and
    S. Vaidya, "Reduction of ASIC gate-level line-end shortening by mask
    compensation", *Proc. SPIE* **2440**, 171–183 (1995).
    <https://doi.org/10.1117/12.209250>
[^zheng-2003]: S. Zheng, G. Zhang, C. Wang and S. F. Detweiler,
    "Characterization of optical proximity matching for 130-nm node gate
    line width", *Proc. SPIE* **5040**, 894 (2003).
    <https://doi.org/10.1117/12.485431>
[^otto-1994]: O. W. Otto, J. G. Garofalo, K. K. Low, C.-M. Yuan,
    R. C. Henderson, C. Pierrat, R. L. Kostelak, S. Vaidya and
    P. K. Vasudev, "Automated optical proximity correction: a
    rules-based approach", *Proc. SPIE* **2197**, Optical/Laser
    Microlithography VII, 278–293 (1994).
    <https://doi.org/10.1117/12.175422>
[^levenson-1982]: M. D. Levenson, N. S. Viswanathan and R. A. Simpson,
    "Improving resolution in photolithography with a phase-shifting
    mask", *IEEE Transactions on Electron Devices* **29**(12),
    1828–1836 (1982). <https://doi.org/10.1109/T-ED.1982.21037>
[^lin-1993]: B. J. Lin, "Phase-shifting masks gain an edge", *IEEE
    Circuits and Devices Magazine* **9**(2), 28–35 (1993).
    <https://doi.org/10.1109/101.200850>
[^orshansky-2004]: M. Orshansky, L. Milor and C. Hu, "Characterization
    of Spatial Intrafield Gate CD Variability, Its Impact on Circuit
    Performance, and Spatial Mask-Level Correction", *IEEE Transactions
    on Semiconductor Manufacturing* **17**(1), 2–11 (2004).
    <https://doi.org/10.1109/TSM.2003.822735>
[^starikov-1992]: A. Starikov, "Accuracy of overlay measurements: tool
    and mark asymmetry effects", *Optical Engineering* **31**(6), 1298
    (1992). <https://doi.org/10.1117/12.56172>
[^rizvi-2005]: S. Rizvi (ed.), *Handbook of Photomask Manufacturing
    Technology*, CRC Press, 2005, ISBN 978-1-4200-2878-2.
    <https://doi.org/10.1201/9781420028782>
