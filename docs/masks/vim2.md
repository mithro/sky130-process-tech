(mask-vim2)=
# VIM2 — Via 2-PLM

The via-2 mask is the {term}`reticle` that places every connection
between metal 2 and metal 3: on the {ref}`VIM2 <step-129>` page's
reading, the resist printed through it at step 129 is opened in a
0.2 µm square over every drawn `via2`, and the {ref}`VIM2E <step-130>`
etch cuts the holes through the inter-metal oxide down to the metal-2
lines. It is the first of the two masks whose `masks.csv` entry comes
in three variants, only one of them marked as used in SKY130, and the
first of the three via masks for which the process-steps sheet records
a coded mask type as well as plates; the masks index reads that type as
an embedded {term}`attenuated phase-shift mask <attenuated PSM>` for
248 nm exposure. This page gathers what public sources say about the
mask itself — its PDK entry and layers, the plates and mask type the
process-steps sheet records, what the public renders of the MPW runs
show, the lithography it needs and the rules that constrain it. How the
step is performed is on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | VIM2 — Via 2-PLM |
|---|---|
| Mask step | {ref}`VIM2 <step-129>`, step 129 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Via 2-PLM", `VIM2`, marked `X` in `Used in SKY130`; "Via 2-TNV", `VIM2`, unmarked; "Via 2-S8TM", `VIM2`, unmarked[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cviam2` mask 44:0, "Via 2 mask"[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `via2` drawing 69:44, "Contact from metal 2 to metal 3"[^pdk-06] |
| Minimum CD, feature / space | `VIM2CD` / `VIM2CDSP`: "Via 2-PLM" 0.2 / 0.2; "Via 2-TNV" 0.28 / 0.28; "Via 2-S8TM" 0.8 / 0.8[^pdk-03] |
| Polarity and tone | Not published; the PDK's `cviam2.nikon` checks name a polarity but not the plate's tone. The holes are opened where `via2` is drawn, which with a positive resist would make the plate dark-field (inference). |
| Exposure class | KrF (248 nm), an inference on the step page from the 0.2 µm hole and from the 248 nm mask type the sheet records for the plate; no public source names the tool ({ref}`machine-duv-krf-stepper`) |
| Mask type (process-steps sheet) | `F4-248-EAPSM-A43-APRX`, read on the masks index as an embedded attenuated phase-shift mask for 248 nm exposure and, less certainly, 4×[^steps-sheet] |
| Plates recorded | Via 2-PLM: all eight; Via 2-TNV and Via 2-S8TM: not recorded[^steps-sheet] |
| Plate no. | `560`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-vim2-steps>` |

## What the mask defines

The periphery rules give the function of the `via2` rule set as "Via2
connects met2 to met3 in the SKY130T\*/SKY130P\*/SP8Q/SP8P\* flows and
met2/capm to met3 in the SKY130DI\* flow", and the PDK's Table F4 names
"Via2" as the layer joining metal 3 to metal 2 and to `capm` — the
latter, like the function line's "SKY130DI\*" flow, a construction with
the capacitor under metal 3, not the one the step pages read
here.[^pdk-periph][^pdk-summary] The mask carries one product feature,
a square: "Min and max L and W of via2 (except for rule
via2.1b/1c/1d/1e/1f)" 0.200 µm (via2.1a), with "Only min. square via2s
are allowed except die seal ring […]" (via2.3).[^pdk-periph] Rules via2.1b
to via2.1e allow sets of square sizes — drawn from 0.2, 0.280, 0.8, 1.2
and 1.5 µm — inside `areaid.mt`, which `gds_layers.csv` describes as the
"Location of e-test modules within the frame", and via2.1f "Two sizes
of square Vias allowed outside areaid:mt: 0.8um and 1.2 um"; all five
carry flag AL but no value ("N/A" or blank), and none names a product
flow.[^pdk-periph][^pdk-06] The PDK's *Error Messages* page, which
describes "many of the automated DRC rules that are checked by SkyWater
as part of the acceptance criteria for GDS data", checks only the via2.1d
set, "via size inside module cut must be 0.200, 0.280, 1.200, OR
1.500".[^pdk-errors]
The PDK's extraction table lists "VIA2" at 3410 in a column headed
"Resistivity (mohms/sq)", against 4500 for "VIA";[^pdk-08] the step page
reads these as 3.4 Ω and 4.5 Ω per plug.

The three `masks.csv` entries — "Via 2-TNV", "Via 2-S8TM" and "Via
2-PLM", with only "Via 2-PLM" marked — have three sizes in Table 2 of
*Criteria & Assumptions*, 0.28, 0.8 and 0.2, under the same
variable names.[^pdk-05][^pdk-03] The {ref}`VIM2 <step-129>` page
describes the 0.2 µm PLM via, reads "S8TM" as a thick-metal-3 option
(inference from the assumptions table's thickness entries), reads PLM
as the label of the five-metal P flow (inference from the rule tables'
"SP8P\*/SKY130P\* (PLM) CADflow"), and leaves "TNV" unexplained. Two
tables of the PDK's *Summary of Key Periphery Rules* bear on the
variants: Table F3c, "Back end layers for S8D\* flow", gives via2 a
width and spacing of 0.280 with a metal-2 enclosure of 0.040, and Table
F3d, "Back end layers for S8T\* flow", a width of 0.280, a spacing of
1.200 and an enclosure of 0.190;[^pdk-summary] the F3c width and
spacing equal the "Via 2-TNV" row of Table 2 (our comparison), and
neither summary table has a row for the 0.2 µm via. The
process-steps sheet's "Run Mask IDs" tab lists all three variants and
records plates only for "Via 2-PLM" ({ref}`masks-mpw-runs`).[^steps-sheet]

The mask defines neither the metal-2 lines the vias land on
({ref}`mask-mm2`) nor the metal-3 lines that cover them (`MM3`), nor
the liner and tungsten plug that fill the holes
({ref}`TIN4 <step-131>` to {ref}`WCMP4 <step-133>`), which on the step
pages' readings take the etched hole, not this resist, as their shape.
Several PDK definitions tie `capm` to via 2 — capm.4 "Min enclosure of
via2 by capm", capm.5 "Min spacing between capm and via2", and Table
C3's "Capacitor", "Capm enclosing at least one via2" — but the
{ref}`CAPM <step-137>` and {ref}`VIM3 <step-144>` pages read that
wording as applying to via 3 and metal 3 in the flow described here
(inference), and the {ref}`VIM2 <step-129>` page sets the "met2/capm"
landing of the "SKY130DI\*" flow aside as not relevant to
it.[^pdk-periph][^pdk-06] Table F2b,
the PDK's mask generation table, has no via columns.[^pdk-06]

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `cviam2` a single purpose, `mask` at 44:0 ("Via 2
mask"), on a layer number that also carries the `cnpc` drawing purpose
at 44:20 and the `pwelliso` label at 44:5; the drawn layer is `via2` at
69:44.[^pdk-06] The pairing rests on those names and descriptions, as on
the {ref}`masks index <masks-index>`, and the PDK publishes no operation
from `via2` to the plate. With no add or drop purpose, rule x.9's
"serifs" have no `cviam2` layer to sit on, and rule x.15a confines mask
layers to test modules, seal ring and frame, with the exception that
"FOM/P1M/Metal waffle drop are allowed inside the die" (flag P, periphery
only);[^pdk-periph] a design inside the die therefore draws `via2` (our
reading of x.9 and x.15a). Unlike via 1, via 2 is not among the "mask
data for p1m, met1, via, met2" that rule x.1a puts on a 0.001 grid, so
its data fall under x.1b's 0.005 for "all layers except those mentioned
in 1a", both printed with the unit "mm".[^pdk-periph] One row of rule
x.2 permits only "n x 90" degree angles on, among other layers, "capm,
mcon, via, via2".[^pdk-periph] The *Error Messages* page lists two checks
named `cviam2.nikon`, "VIM2mk in the nikon cross has the wrong polarity"
and "VIM2mk is missing from the nikon cross in the layout";[^pdk-errors]
it does not say what the "nikon cross" is, and we read the checks as
concerning a structure on the mask layer whose data must have the right
polarity (inference from the message wording), not as stating the
plate's tone.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `VIM2` the site renders layer 69:44 (`via2`)
alone, with no Boolean expression and no fill layer, on all eight runs;
its mask record gives the mask-level layer 44:0, the description "Via
2-PLM" with the three variant names, and the info text "Via 2
(M2→M3)".[^mask-renders] The choice of layer is one public derivation
from the drawn data, not SkyWater's mask-generation recipe
({ref}`masks-derivations`). The info text is identical to the "Info"
note of the "Via 2-PLM" row in the process-steps sheet, one of the level
names the two sources share, so neither is cited as corroborating the
other ({ref}`masks-renders-sheet-notes`).[^steps-sheet][^mask-renders]

Every rendered die of every run carries `via2` shapes — at least
705 880 on each die[^mask-renders] — so the count of 40 dies says only
that every layout joins metal 2 to metal 3. The site states the limits
of its images: "These are renders of *drawn* data, not photomask
artwork: reticle pitch, 4x reduction, mirroring and the frame features
the fab adds are not modelled."[^mask-renders] Its metadata carries no
plate ID and names no variant beyond the description, so a render is
tied to a plate in the sheet only by the acronym `VIM2`, and the MPW-4
renders come from a different reticle set from the one whose plates the
sheet records ({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a plate for the
"Via 2-PLM" row as existing on all eight MPW runs, with the plate number
`560` on each.[^steps-sheet] The plate IDs below are the sheet's; the
reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet] The sheet records no
plates for the unmarked "Via 2-TNV" and "Via 2-S8TM"
rows.[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA560A` |
| MPW-2 | `5CS8007AC` | `S8007AA560A` |
| MPW-3 | `5CS8008AC` | `S8008AA560A` |
| MPW-4 | `5CS8018AC` | `S8018AA560A` |
| MPW-5 | `5CS8011AC` | `S8011AA560A` |
| MPW-6 | `5CS8014AC` | `S8014AA560A` |
| MPW-7 | `5CS8016AC` | `S8016AA560A` |
| MPW-8 | `5CS8017AC` | `S8017AA560A` |

* **MPW-5.** Unlike `VIM` and `VIM4`, the via-1 and via-4 masks,
  a `VIM2` plate is recorded for MPW-5; the masks index reads the MPW-5
  gaps of those masks as more likely gaps in the record than in the run
  ({ref}`masks-mpw-runs`).[^steps-sheet]
* **Plate number.** The sheet does not say what `560` encodes. It falls
  between `550` for `MM2` and `570` for `MM3`; from `500` to `590` the via
  and metal numbers rise in step order, but each capacitor mask is
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
`VIM4`.[^steps-sheet] The tab names the mask by its acronym alone, so it
does not say to which of the three `VIM2` variants the type applies; that
it is the "Via 2-PLM" plate, the only one with plates recorded, is our
inference. Nor does it define its codes or say to which runs they apply.
The masks index reads `EAPSM` as an embedded attenuated phase-shift mask
and `248` as the exposure wavelength, because a mask maker uses the
abbreviation — Photronics' product page states "At 248nm and 193nm
wavelengths, our embedded attenuated phase-shift masks (EAPSM) rely on a
wavelength-tuned, 6% transmission MoSiON absorber" — and reads the digit
4, less certainly, as the 4× reduction ratio.[^photronics-abr] That
statement describes the catalogue of one mask maker, not the `VIM2`
plate, whose maker, absorber and transmission the sheet does not give.
We do not read the fields `F`, `A43` and `APRX`; the `VIM4` code has
`B`, `LSR` and `WET` in the same positions.

The attenuated type is the one the literature of the period proposed
for isolated openings. Terasawa et al. suggested that "a halftone
phase-shifting mask is suitable for printing isolated patterns and it
gives wider focus latitude than conventional mask
technology";[^terasawa-1991] Smith et al. presented four candidate
films for the shifter, among them "a molybdenum silicon oxide
composite", each capable of 4–15 % transmission at 193 nm at the
thickness that gives a π phase shift.[^smith-1996] Via 2 is a layer of
isolated and arrayed small squares (via2.1a, via2.3),[^pdk-periph] which
fits that use (our reading); the sheet does not say why the type was
chosen.

## Lithography and pattern transfer

**Exposure class.** The {ref}`VIM2 <step-129>` page gives
{math}`k_1 = 0.20 \times 0.70 / 0.248 \approx 0.56` on a KrF lens of NA
0.70 and about 0.35 on an i-line lens of NA 0.63, and infers a 248 nm
level from the hole size and from the mask type the sheet records; the
{ref}`KrF stepper <machine-duv-krf-stepper>` page lists it there, and the
{ref}`i-line stepper <machine-i-line-stepper>` page puts it among the
steps for which SkyWater's i-line tools are "listed, not assigned". SkyWater lists "ASML DUV
stepper" and "ASML DUV scanner" beside its i-line tools but assigns no
layer to any of them.[^skw-01] ITRS 2001 lists "248 nm + PSM" and
"193 nm" as the exposure options for the 130 nm node,
and names "attenuated shifter and alternating aperture" as the primary
phase-shift mask choices.[^itrs-03]

**Mask errors.** Wong et al. found the mask error factor rising "rapidly
when the critical dimension (CD) is less than […] 0.75 (lambda) /NA for
contacts", and attenuated phase-shift masks behaving like chrome-on-glass
masks;[^wong-1998] at 248 nm and NA 0.7 that threshold is about 0.27 µm
(our arithmetic), above the 0.200 µm via, so plate CD errors would print
magnified (inference). Kim et al. found the factor rising near the
resolution limit, larger for dense than for isolated contacts and smaller
on attenuated masks than on binary ones, because of the attenuated
plates' positive bias.[^kim-1999] ITRS 2001 asks, for its 2001 (130 nm)
column, for a mask CD uniformity of 8.0 nm (3σ) on contacts and vias at 4× magnification,
requirements that are "for critical layers".[^itrs-03] How tightly
SkyWater specifies the `VIM2` plate is not public.

**Side lobes and resist.** Ma and Andersson describe side-lobe printing
as "One major limitation of applying attenuated phase shift mask",
"caused by constructive interference of the first order of diffraction
maximum from nearby features, plus the electrical fields from
semi-transparent materials in the surrounding area";[^ma-andersson-1998]
dense via arrays at the 0.200 µm spacing of via2.2 are the case in
which neighbours contribute most (inference). Chen, Wang and Chu optimised an attenuated mask for
contact-hole printing,[^chen-1999-psm] and Lu et al. selected
contact-hole resists compatible with an attenuated mask at
KrF;[^lu-1999] for holes Yamamoto et al. describe hierarchical optical
proximity correction.[^yamamoto-2000] Whether the `VIM2` data are
corrected, and how, is not public.

**Substrate and tone.** On the step pages' readings the resist sits on
the {ref}`NCAPOX4 <step-128>` cap over 0.42 µm of via-2 oxide, the
height of the PDK's stack diagram,[^pdk-04] above capped metal-2
lines, so the reflection under it changes with the metal pattern.
Brunner showed that the swing ratio scales with the square root of the
substrate reflectivity, which an anti-reflective coating
reduces.[^brunner-1991] The step page reads a positive chemically
amplified KrF resist over an organic {term}`BARC`; with the holes opened
where `via2` is drawn, the plate would be dark-field, and on the
attenuated reading its "dark" field within the pattern would be the
partially transmitting shifter film rather than opaque chrome
(inference); Photronics leaves "The mask fiducials, barcode and titles"
of its attenuated plates "in high-contrast chrome".[^photronics-abr] Neither is
published. The consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Pattern transfer.** On the step pages' readings the holes are etched
at {ref}`VIM2E <step-130>` through the cap oxide and the
{ref}`NILD4 <step-126>` oxide, on the
{ref}`dielectric plasma etcher <machine-plasma-etcher-dielectric>` class,
down to the refractory cap of the metal-2 lines
({ref}`overview-metal-cap`), and the resist is stripped
within that step. Le, Banerjee and McPherson found that via size strongly
affects the electromigration failure-time spread of tungsten-plug vias
for one direction of electron flow with a TiN-capped metallisation, and
not for the other,[^le-1996] one reason the printed size matters (our
reading).

**Overlay.** Metal 2 must enclose the via by 0.040 µm (via2.4) and by
0.085 µm on one of two adjacent sides (via2.5), and metal 3 by 0.065 µm
(m3.4).[^pdk-periph] The {ref}`VIM2 <step-129>` page reads the mask as
aligned to the metal-2 pattern and names the 0.040 µm enclosure as "the
registration that matters".

(mask-vim2-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `VIM2` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`VIM2 <step-129>`, {ref}`VIM2E <step-130>`

* {ref}`VIM2 <step-129>` — coats, exposes and develops the resist.
* {ref}`VIM2E <step-130>` — etches the via holes through the resist;
  the step list used in this reference has no separate strip step, and
  the step page treats the resist strip and post-etch clean as part of
  the etch.

On its step page's reading, the next step, {ref}`TIN4 <step-131>`,
sputters a titanium nitride liner into the cleaned holes after the
resist is gone. The next mask step is {ref}`CAPM <step-137>`. The rule
needs no exception for this mask; the liner, tungsten fill and plug
polish that follow do not use the resist.

## Design rules and critical dimensions

The `via2` rules of the periphery rules, with the metal-3 enclosures of
via 2, the `capm` rules that name via 2 and the mask-data rules x.1b,
x.2, x.7, x.15a and x.18. Flag P means "Rule applies to periphery only
(outside areaid.ce). A corresponding core rule may or may not exist.",
AL "Rules applicable only to Al BE flows", CU "Rules applicable only to
Cu BE flows", IR "IR drop check compering Al database and slotted Cu
database for the same product (2 gds files) must be clean", RR
"Recommended rule at any IP level" and NC "Rule not checked by DRC. It
should be used as a guideline only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| via2.1a | "Min and max L and W of via2 (except for rule via2.1b/1c/1d/1e/1f)" (AL) | 0.200 µm |
| via2.1b | "Three sizes of square Vias allowed inside areaid:mt: 0.280um, 1.2 um and 1.5 um" (AL) | N/A |
| via2.1c | "Two sizes of square Vias allowed inside areaid:mt: 1.2 um and 1.5 um" (AL) | N/A |
| via2.1d | "Four sizes of square Vias allowed inside areaid:mt: 0.2um, 0.280um, 1.2 um and 1.5 um" (AL) | — |
| via2.1e | "Three sizes of square Vias allowed inside areaid:mt: 0.8um, 1.2 um and 1.5 um" (AL) | N/A |
| via2.1f | "Two sizes of square Vias allowed outside areaid:mt: 0.8um and 1.2 um" (AL) | N/A |
| via2.2 | "Spacing of via2 to via2" (AL) | 0.200 µm |
| via2.3 | "Only min. square via2s are allowed except die seal ring where via2s are (Via2 CD)\*L" (AL) | 0.2\*L |
| via2.4 | "Via2 must be enclosed by Met2 by at least …" (AL) | 0.040 µm |
| via2.4a | "Inside areaid.mt, 1.5 µm Via2 must be enclosed by met2 by atleast" | 0.140 µm |
| via2.5 | "Via2 must be enclosed by Met2 on one of two adjacent sides by at least …" (AL) | 0.085 µm |
| via2.11–via2.14 | For copper flows: via size, spacing, row spacing and metal-2 enclosure (CU) | 0.210, 0.180, 0.200, 0.035 µm |
| via2.irdrop.1–4 | For 1 to 2, 3 to 4, 5 to 30 and more than 30 via2's "on the same connector", "mcon area pre- and post- Cu conversion must differ by no more than…" (CU IR) | 0.0, 0.6, 0.79, 0.9 µm |
| m3.4 | "Via2 must be enclosed by Met3 by at least …" (AL) | 0.065 µm |
| m3.5 | "Via2 must be enclosed by Met3 on one of two adjacent sides by at least …" | N/A |
| m3.15 | "Via2 must be enclosed by met3 by at least…" (CU) | 0.060 µm |
| capm.4 | "Min enclosure of via2 by capm" | N/A |
| capm.5 | "Min spacing between capm and via2" | N/A |
| x.1b | "Data for SKY130 layout and mask on all layers except those mentioned in 1a must be on a grid of mm (except inside Seal ring)" | 0.005 (unit "mm") |
| x.2 | "Angles permitted on: tap (except inside areaid.en), poly […], li1(periphery), licon1, capm, mcon, via, via2. Anchors are exempted." | n x 90 deg |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
| x.18 | "Use redundant mcon, via, via2, via3 and via4 […]" (RR) | — |

Table 2 of *Criteria & Assumptions* gives `VIM2CD` and `VIM2CDSP` as 0.2
and 0.2 for "Via 2-PLM", 0.28 and 0.28 for "Via 2-TNV" and 0.8 and 0.8
for "Via 2-S8TM", and 0.21 and 0.18 for a "Via 2-Cu" row (`VIM2_CuCD`,
`VIM2_CuCDSP`), the values of the copper rules via2.11 and via2.12, for a
back end SKY130's aluminium flow does not use.[^pdk-03][^pdk-periph] The
irdrop rules speak of "mcon area" although they are via-2 rules, and
via2.3 gives the seal-ring via width as "0.2\*L"; the PDK explains
neither. For the plate the decisive figures are one 0.200 µm square on a
0.40 µm pitch (our arithmetic from via2.1a and via2.2).

## Related pages

* {ref}`VIM2 <step-129>` and {ref}`VIM2E <step-130>` — the mask step and
  the via etch; {ref}`TIN4 <step-131>` — the liner that follows.
* {ref}`mask-mm2` — the metal-2 mask the vias land on; {ref}`mask-vim`
  and {ref}`mask-vim4` — the via masks one and two levels away.
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

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Via 2-PLM", "Via 2-TNV"
  and "Via 2-S8TM", `VIM2`, with the PLM entry marked.[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `via2` 69:44,
  `cviam2` 44:0, `areaid.mt`, Table C3 and the columns of Table
  F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `VIM2CD`/`VIM2CDSP` for the
  three variants and `VIM2_CuCD`/`VIM2_CuCDSP`.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `via2` rules, m3.4, m3.5, m3.15,
  capm.4, capm.5, x.1a, x.1b, x.2, x.7, x.9, x.15a, x.18 and the flag
  legend.[^pdk-periph]
* [SkyWater PDK, *Summary of Key Periphery Rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>) — Tables F3c, F3d and
  F4.[^pdk-summary]
* [SkyWater PDK, *Error Messages* page](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) — the via2.1d check and the
  `cviam2.nikon` checks.[^pdk-errors]
* [SkyWater PDK, *Process stack diagram*](<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>) — the 0.42 µm via-2
  height.[^pdk-04]
* [SkyWater PDK, *Parasitic Layout Extraction*](<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>) — the via resistance
  table.[^pdk-08]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the `VIM2` plates of
  MPW-1 to MPW-8, the "Info" note and the "Sheet4" mask
  type.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `VIM2` renders, their layer,
  description and info text, and the per-die shape counts.[^mask-renders]
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
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]

### Deep dive

* [Terasawa et al., *Jpn. J. Appl. Phys.* 1991](<https://doi.org/10.1143/JJAP.30.2991>) — halftone
  phase-shifting masks and their focus latitude for isolated
  patterns.[^terasawa-1991]
* [Smith et al., *JVST B* 1996](<https://doi.org/10.1116/1.588655>) — four candidate shifter films for
  attenuated phase-shift masks, characterised at 193 nm.[^smith-1996]
* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor of
  contacts on binary and phase-shift masks.[^wong-1998]
* [Kim et al., *Proc. SPIE* 1999](<https://doi.org/10.1117/12.354400>) — mask CD error for sub-quarter-micron
  contact holes on binary and attenuated masks.[^kim-1999]
* [Ma and Andersson, *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310783>) — the cause of side-lobe printing
  with attenuated plates and a rim-shifter remedy.[^ma-andersson-1998]
* [Chen, Wang and Chu, *Proc. SPIE* 1999](<https://doi.org/10.1117/12.354399>) — optimising an attenuated mask
  for contact holes.[^chen-1999-psm]
* [Lu et al., *Proc. SPIE* 1999](<https://doi.org/10.1117/12.350280>) — contact-hole resists compatible
  with attenuated masks at KrF.[^lu-1999]
* [Yamamoto et al., MNC 2000](<https://doi.org/10.1109/IMNC.2000.872612>) — hierarchical OPC on contact-hole
  layers.[^yamamoto-2000]
* [Brunner, *Proc. SPIE* 1991](<https://doi.org/10.1117/12.46410>) — the swing ratio and anti-reflective
  coatings.[^brunner-1991]
* [Le, Banerjee and McPherson (TI), *Semicond. Sci. Technol.* 1996](<https://doi.org/10.1088/0268-1242/11/6/003>) — via
  size and tungsten-plug via electromigration.[^le-1996]
* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — the exposure options and mask requirements
  it lists for critical layers at 130 nm.[^itrs-03]

## Open questions

* The PDK does not define "TNV", "S8TM" or "PLM", nor say for which
  product flows the via2.1b–via2.1f size sets are written, of which only
  via2.1d is among the published checks; the step page's readings of S8TM
  and PLM are inferences.[^pdk-05][^pdk-periph][^pdk-errors]
* The "Sheet4" codes are not defined in the sheet; the attenuated and
  248 nm readings rest on a mask maker's abbreviation, the 4× reading is
  less certain, and the fields `F`, `A43` and `APRX` are not read. The tab
  does not say to which variant or runs the type applies.[^steps-sheet]
* The plate's maker, shifter film, transmission, tone and CD
  specification, any OPC, the resist and the exposure tool are not
  public; the KrF reading rests on the 0.200 µm rule and the mask type.
* The PDK does not explain why the capm rules and Table C3 name via 2,
  which the step pages read as via 3 in this flow.[^pdk-periph][^pdk-06]
* What the plate number `560` encodes is not stated, and no public source
  lists the `VIM2` plate of the original MPW-4 set
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
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* (including Table C3,
    the device and CAD definitions, and Table F2b, the mask generation
    table) and `gds_layers.csv`, SkyWater SKY130 PDK documentation.
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
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_VIM2/`
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
[^lu-1999]: Z. G. Lu, Y. Cui, A. C. Thomas, S. M. Mansfield et al.,
    "Selection of attenuated phase shift mask compatible contact hole
    resists for KrF optical lithography", *Proc. SPIE* **3678**, Advances
    in Resist Technology and Processing XVI, 923 (1999).
    <https://doi.org/10.1117/12.350280>
[^yamamoto-2000]: K. Yamamoto, S. Kobayashi, T. Uno and T. Kotani,
    "Hierarchical optical proximity correction on contact hole layers",
    *Digest of Papers, Microprocesses and Nanotechnology 2000*,
    pp. 40–41. <https://doi.org/10.1109/IMNC.2000.872612>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^le-1996]: H. A. Le, K. Banerjee and J. W. McPherson, "The dependence of
    W-plug via EM performance on via size", *Semiconductor Science and
    Technology* **11**(6), 858–864 (1996).
    <https://doi.org/10.1088/0268-1242/11/6/003>
