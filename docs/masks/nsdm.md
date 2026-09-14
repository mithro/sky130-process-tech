(mask-nsdm)=
# NSDM — N+ Implant

The N+ implant mask is the {term}`reticle` that decides where SKY130's
silicon receives the heavy n-type source/drain dose: on the
{ref}`NSDM <step-085>` page's reading, the resist printed through it at
step 85 is opened over every region drawn in `nsdm` — the NMOS and SONOS
sources and drains, the n+ taps to the N-wells, the NPN emitter and
collector contacts, the PNP base contacts, the N+ diffusion resistors and
the n-type diodes — the implant {ref}`NSDI <step-086>` passes through the
openings, and the resist is stripped at {ref}`NSDIS <step-087>`, the last
clean before the source/drain anneal. It is the second of the two
source/drain implant {term}`block masks <block mask>`, nearly the
complement of {ref}`mask-psdm` across the active area, and the last
implant mask of the front end. Its drawn layer is also one of the three
from which one public derivation builds the created part of the
high-voltage tip mask. This page gathers what public sources say about
the mask itself — its PDK entry and layers, the plates the process-steps
sheet records for the MPW runs, what the public renders of those runs
show, the lithography it needs and the rules that constrain it. How the
step is performed is on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | NSDM — N+ Implant |
|---|---|
| Mask step | {ref}`NSDM <step-085>`, step 85 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "N+ Implant", `NSDM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cnsdm` mask 30:0, "N+ Implant mask"; drawing 29:20, mask add 29:21, mask drop 29:22, without descriptions[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `nsdm` drawing 93:44, "N+ source/drain implant"[^pdk-06] |
| Minimum CD, feature / space | `NSDMCD` 0.38 / `NSDMCDSP` 0.38[^pdk-03] |
| Polarity and tone | Not published. The rule set's function is "Defines opening for N+/P+ implants", and the step page reads the resist windows as lying where `nsdm` is drawn; with a positive resist the plate would be clear over `nsdm` and opaque elsewhere (inference). |
| Exposure class | i-line, an inference on the step page from the 0.380 µm feature and space; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `250`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 3 steps; see {ref}`Steps that use this mask <mask-nsdm-steps>` |

## What the mask defines

The periphery rules give `nsdm` and `psdm` one rule set, "N+/P+
Source/Drain Implants (Nsdm and Psdm)", whose function is "Defines
opening for N+/P+ implants", and the layer table describes `nsdm` as "N+
source/drain implant".[^pdk-periph][^pdk-06] "Diff and tap must be
enclosed by their corresponding implant layers" (nsd.9), by 0.125 µm
except at a butting edge (nsd.5a, nsd.5b), and "Nsdm and psdm cannot
overlap diff/tap regions of opposite doping" (nsd.8); the precision
resistors must keep 0.200 µm from `nsdm` ("Min spacing, no overlap, of
rpm and nsdm", rpm.6), and the source of a drain-extended NMOS must be
enclosed by it (denmos.13).[^pdk-periph] The {ref}`NSDM <step-085>` page
lists the regions inside `nsdm` from the PDK's device pages — NMOS
source/drains of every voltage class, the SONOS cells (an inference from
the device being an n-channel FET), n+ taps, NPN emitter and collector
contacts and PNP base contacts, the N+ diffusion resistor and the
P-well-to-n+ diodes — and the PDK's resistance table gives
"N-diffusion" 120000 in a column headed "Resistivity
(mohms/sq)".[^pdk-07][^pdk-08]

The PDK's mask generation table, Table F2b, marks the `NSDM` column `C`
("CREATED") in 37 of its 80 device rows: the n- and HV n-diffusion
resistors, the seven 1.8 V NMOS rows (standard, low-Vt and core), the
three varactors, the four SONOS rows, every 110 Å NMOS row from the
5/10.5 V device and the flash pass gates to the four UHV 5/20 V NMOS rows,
six n-type and photo diode rows, both parasitic bipolar rows and the
three ESD NMOS.[^pdk-06] It marks `-`, "Layer not created for the
device", in 22 rows, the p-diffusion and p+ poly resistors, the PMOS and
the p-type diodes, and `+` in 21.[^pdk-06] On our reading the created
shapes follow the n-type devices and the varactors, whose taps are n+ in
N-well; the table does not say what the created shapes add to the drawn
layer. The varactor rows are marked `-` in the `PSDM` column and `C` here,
and the parasitic bipolar rows `C` in both ({ref}`mask-psdm`).[^pdk-06]

What the mask does not define is the junction edge next to a gate or the
doping of the precision resistors. On the step pages' readings the
implant is self-aligned to the spacers and joins the tips placed through
{ref}`mask-ntm`, {ref}`mask-hvntm` and {ref}`mask-ldntm`, and the capped
gates receive nothing; rule rpm.6 keeps the resistors, whose heads the
{ref}`PSDM <mask-psdm>` implant dopes through the {ref}`mask-npcm` cuts on
the {ref}`NPCM <step-078>` page's reading, clear of the N+
implant.[^pdk-periph]

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `cnsdm` a `mask` purpose at 30:0 ("N+ Implant
mask") and `drawing` 29:20, `mask add` 29:21 and `mask drop` 29:22 on a
different layer number, the three without descriptions; the drawn layer
is `nsdm` at 93:44.[^pdk-06] The {ref}`NSDM <step-085>` page reads the add
and drop purposes as showing that the reticle is derived from the drawn
layer by Boolean operations; the PDK publishes no such operation. Rule
x.9 allows "Shapes on maskAdd or maskDrop layers ("serifs")" in the core
only, and x.15a confines "Drawn compatible, mask, and waffle-drop layers"
to test modules, seal ring and frame, with an exception that names only
"FOM/P1M/Metal waffle drop" (flag P);[^pdk-periph] a design inside the die
therefore draws `nsdm` (our reading of x.15a). Table C3 of the *Layers
Reference* defines `nsdmHoles` as "Hole( nsdm )" for the hole-area rule
and defines `N+_diff` as "Diff NOT Nwell", not by `nsdm`.[^pdk-06]

The PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance
criteria for GDS data", checks the drawn layer under `nsd` names and
adds core values the periphery rules do not give: "0.29 min. width of
nsdm in COREID" (`nsd.c1b`), "0.29 min. spacing/notch of "nsdm" in core"
(`nsd.c2b`) and "0.13 min. enclosure of n+ tap in core by nsdm"
(`nsd.c5a`), beside "0.38 min. width of nsdm (opposite parallel)"
(`nsd.c1a`) and "0.38 min. spacing/notch of "nsdm" in core"
(`nsd.c2a`).[^pdk-errors] It gives nsd.9 as "ndiff/ntap (source of
extendedDrain fet and gated_npn exempted) must be enclosed by
nsdmZENERID", rpm.6 as "rpm must not overlap nsdm" with a 0.2 spacing,
and lists "NSDMdrop must be enclosed by COREID" and "NSDMadd must be
enclosed by COREID" (x.9), a module-cut check at 0.19 (x.12a) and two
`cnsdm.nikon` checks, "NSDMmk in the nikon cross has the wrong polarity"
and "NSDMmk is missing from the nikon cross in the layout".[^pdk-errors]
It names no created `NSDM` layer. The core tap enclosure, 0.13, differs
from the 0.12 of the P+ counterpart `psd.c5b`
({ref}`mask-psdm`).[^pdk-errors]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `NSDM` the site renders layer 93:44 (`nsdm`)
alone, with no Boolean expression, no fill layer and no note, on all
eight runs; its mask record gives the mask-level layer
30:0.[^mask-renders] That is the index's pairing, and the choice of layer
is one public derivation from the drawn data, not SkyWater's
mask-generation recipe. The same layer appears in the site's `HVNTM`
expression, `125:20 OR ((65:20 AND 93:44 AND 75:20) NOT 81:2)`, where it
stands for n+ diffusion inside `hvi` ({ref}`mask-hvntm`).[^mask-renders]

Every rendered die of every run carries `nsdm` shapes — at least 484 947
on each die; the minimum on each run lies between 484 947 (MPW-5) and
538 673 (MPW-8); on MPW-1 one die accounts for more than 98 % of the
run's shapes; and counts rarely repeat, on at most seven dies of a run
and on none of MPW-1 or MPW-8.[^mask-renders] The count of 40 dies
therefore says only that every layout has n-type diffusion, as a CMOS die
must; we read the large minimum as shapes that every die of these runs
carries rather than as project content (inference; the site does not
say what they are). The site states the limits of its images: "These are
renders of *drawn* data, not photomask artwork: reticle pitch, 4x
reduction, mirroring and the frame features the fab adds are not
modelled."[^mask-renders] Its metadata carries no plate ID, so a render
is tied to a plate in the process-steps sheet only by the acronym `NSDM`,
and the MPW-4 renders come from a different reticle set from the one
whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `NSDM` plate
as existing on all eight MPW runs, with the plate number `250` on each
and no "Info" note.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA250A` |
| MPW-2 | `5CS8007AC` | `S8007AA250A` |
| MPW-3 | `5CS8008AC` | `S8008AA250A` |
| MPW-4 | `5CS8018AC` | `S8018AA250A` |
| MPW-5 | `5CS8011AC` | `S8011AA250A` |
| MPW-6 | `5CS8014AC` | `S8014AA250A` |
| MPW-7 | `5CS8016AC` | `S8016AA250A` |
| MPW-8 | `5CS8017AC` | `S8017AA250A` |

* **Plate number.** The sheet does not say what `250` encodes. It is lower
  than `255` for `NTM` (step 64), `257` for `HVNTM` (step 68) and `260`
  for `PSDM` (step 81), all of which precede it in the flow, and higher
  than `238` for `LDNTM` (step 71), so the numbers do not follow process
  order and no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `NSDM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`, whose plates no public
  source lists ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`NSDM <step-085>` page puts the 0.380 µm
feature and space at {math}`k_1 \approx 0.62` on an i-line stepper of
NA 0.6, quotes ASML's statement that older exposure tools "migrate to
the lithography of choice for less critical layers",[^asml-30] and
infers an i-line level, as for `PSDM`; the
{ref}`i-line stepper <machine-i-line-stepper>` page lists it there. At
the NA 0.48 low end of ASML's PAS 5500/275D[^asml-pas5500-275d] the same
feature has {math}`k_1 \approx 0.50`, and the Error Messages page's 0.29
core width and spacing[^pdk-errors] would be at {math}`k_1 \approx 0.48`
at NA 0.6 (our arithmetic); the step page does not discuss the core
values. SkyWater lists "ASML I-line stepper" and "ASML I-line scanner"
among its tools but assigns no layer to them.[^skw-01]

**Mask errors.** Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns";[^wong-1998]
at 365 nm that threshold is about 0.38 µm at NA 0.48 and 0.30 µm at
NA 0.60 (our arithmetic), so the 0.38 µm periphery features lie at or
above it, while 0.29 µm core features would magnify a plate CD error
(inference).

**Resist.** Nothing is etched through this resist; it must stop the
heavy n-type implant wherever the plate leaves it. The step page reads a
positive i-line resist of about 1 µm, the PDK's generic "Photoresist
thickness" of 1.14 µm, which stops an arsenic source/drain implant of
tens of keV with a wide margin, and argues that the thickness is again
set by coverage over the capped gates and by the resist's endurance under
a dose of the order of 10¹⁵ cm⁻².[^pdk-03] The ion range in resist is
what SRIM computes.[^ziegler-2010] The step page adds that arsenic, a
heavier ion than boron or BF₂, deposits more energy in the resist surface
at the same dose and forms a harder crust, of the kind Fujimura et al.
measured;[^fujimura-1989] Smith treated wafer cooling and resist masking
problems in implantation,[^smith-1983] Romig, Bishop and Rio resist
burning in a high-current implanter,[^romig-1996] Lukaszek, Reno and
Bammi the influence of photoresist on wafer charging during a high-current
arsenic implant,[^lukaszek-1996] Lee et al. and Horsky resist
outgassing,[^lee-1996][^horsky-1998] and Rubin et al. UV
photostabilisation of resist before high-dose implants.[^rubin-2000]
SkyWater's resist, its thickness and any hardening are not public; the
consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Resist edges.** The step page reads the enclosure and spacing values as
reflecting the lateral straggle and mask-proximity effects that Hook et
al. measured[^hook-2003] and Sheu et al. modelled,[^sheu-2006] whose
implications for analogue layout Drennan, Kniffin and Locascio
describe;[^drennan-2006] the PDK does not state their purpose. Table 3f
gives "High current" implants an angle of 0° (`HCIMPA`),[^pdk-03] and
Krieger et al. described the shadowing of a tilted arsenic source/drain
implant by the gate and spacer.[^krieger-1989]

**Pattern transfer.** On the step pages' readings the pattern is
transferred into the silicon, and into the poly contact heads opened by
the nitride cut where `nsdm` covers them, as dopant by
{ref}`NSDI <step-086>` on the
{ref}`high-current implanter <machine-high-current-implanter>` class,
through the thin {ref}`SPOX <step-080>` oxide, and the resist is removed
at {ref}`NSDIS <step-087>` on the
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` and
{ref}`wet bench <machine-wet-bench>` classes. Table 3b gives the result,
an "N+ or P+ S/D (XJ)" with a vertical feature of 0.1 µm and a vertical
space of 0.06 µm (`JCTD` / `LD`); the species, energy and dose are not
public.[^pdk-03]

**Overlay.** The {ref}`NSDM <step-085>` page reads the mask as aligned to
the active pattern for the 0.125 µm diffusion enclosure and, for the
butting edges and the resistor rule, to poly and to the `PSDM`
pattern.[^pdk-periph] At a butting diffusion/tap edge the enclosure is
0.000 µm (nsd.6), so the `NSDM` and `PSDM` plates meet there and their
placement errors add (our reading). ASML specifies "≤ 40 nm"
single-machine overlay for the /275D stepper[^asml-pas5500-275d] (our
comparison; how SkyWater budgets the margin is not public).

(mask-nsdm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `NSDM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`NSDM <step-085>`, {ref}`NSDI <step-086>`, {ref}`NSDIS <step-087>`

* {ref}`NSDM <step-085>` — coats, exposes and develops the resist on the
  surface cleaned at {ref}`PDIS <step-084>`.
* {ref}`NSDI <step-086>` — the heavy n-type source/drain implant through
  the resist windows, self-aligned to the spacers.
* {ref}`NSDIS <step-087>` — strips the implanted resist and, as the last
  strip before the anneal, cleans the wafer for it.

On its step page's reading, the next step, {ref}`RTAD <step-088>`, is the
rapid thermal anneal that activates the source/drain implants with no
resist on the wafer. The next mask step is {ref}`LICM1 <step-093>`, after
the sacrificial PSG, the polish and the cap oxide. There is no exception
to the rule for this mask.

## Design rules and critical dimensions

The `nsdm`/`psdm` rules of the periphery rules, given for `nsdm`, with
the precision-resistor and drain-extended NMOS rules that place `nsdm`
and the mask-data rules x.7, x.9 and x.15a; flag P means "Rule applies to
periphery only (outside areaid.ce). A corresponding core rule may or may
not exist.", DE "Rule not checked for source of Drain Extended device"
and NC "Rule not checked by DRC. It should be used as a guideline
only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| nsd.1 | "Width of nsdm(psdm)" (P) | 0.380 µm |
| nsd.2 | "Spacing of nsdm(psdm) to nsdm(psdm)" (P) | 0.380 µm |
| nsd.3 | "Manual merge if less than minimum" | — |
| nsd.5a | "Enclosure of diff by nsdm(psdm), except for butting edge" | 0.125 µm |
| nsd.5b | "Enclosure of tap by nsdm(psdm), except for butting edge" (P) | 0.125 µm |
| nsd.6 | "Enclosure of diff/tap butting edge by nsdm (psdm)" | 0.000 µm |
| nsd.7 | "Spacing of NSDM/PSDM to opposite implant diff or tap (for non-abutting diff/tap edges)" | 0.130 µm |
| nsd.8 | "Nsdm and psdm cannot overlap diff/tap regions of opposite doping" (DE) | — |
| nsd.9 | "Diff and tap must be enclosed by their corresponding implant layers. Rule exempted for […]" (DE) | — |
| nsd.10a | "Min area of Nsdm" | 0.265 µm² |
| nsd.11 | "Min area of n/psdmHoles" | 0.265 µm² |
| rpm.6 | "Min spacing, no overlap, of rpm and nsdm" | 0.200 µm |
| denmos.13 | "de_nFet_source must be enclosed by nsdm by" | 0.130 µm |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.9 | "Shapes on maskAdd or maskDrop layers ("serifs") are allowed in core only. Exempted are: […]" | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |

The periphery table heads the set "(n/ psd.-)" and numbers its rules
without a layer prefix; the names above are those of the Error Messages
page.[^pdk-periph][^pdk-errors] Table 2 of *Criteria & Assumptions*
repeats the feature and space as `NSDMCD` 0.38 and `NSDMCDSP` 0.38, Table
7 gives "Min Nsdm area" as 0.265 (`MinNsdmArea`) and "Min N/Psdm hole
area" as 0.265 (`MinNPsdmHole`) in its column headed "CD", matching
nsd.10a and nsd.11, and Table 3b's "N+ or P+ S/D (XJ)" (0.1 / 0.06),
"Max (N+ or P+ S/D outdiff.) next to isol. edge" (0.007, `LDST`) and the
same for "6 V reg. devices" (0.05, `LDST5`) describe the junction the
implant forms.[^pdk-03] Table 3d gives punch-through spacings "n+ - n+ or
p+-p+" of 0.23 (`DPTS`) and "n+ in pwell to nwell" of 0.15 (`PNPTS`), and
Table 3e a "Minimum n+ or p+ - nwell spacing to prevent latch-up" of 0.23
(`NPNWLU`).[^pdk-03] Table F3a of the *Summary of Key Periphery Rules*
gives `n/psdm` a width of 0.380, a spacing of 0.380 and "Yes" in the
"Manual" (merge) column, and, in its diff and tap columns, spacings of 0.130 and
enclosures of 0.130, against the 0.125 µm of nsd.5a and nsd.5b (our
reading of the columns; the PDK does not reconcile
them).[^pdk-summary][^pdk-periph] For the plate, nsd.1 and nsd.2 set the
smallest periphery features, 0.380 µm lines and spaces with islands of
0.265 µm², and the Error Messages page's core checks allow 0.29.

## Related pages

* {ref}`NSDM <step-085>`, {ref}`NSDI <step-086>` and
  {ref}`NSDIS <step-087>` — the mask step, the implant and the strip;
  {ref}`RTAD <step-088>` — the anneal that follows.
* {ref}`mask-psdm` — the complementary P+ mask; {ref}`mask-npcm` — the
  nitride cut through which the implant reaches poly heads.
* {ref}`mask-ntm`, {ref}`mask-hvntm` and {ref}`mask-ldntm` — the tip masks
  whose extensions the N+ junction joins.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the tables this page's plate facts are taken from.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-high-current-implanter` — the implant class that uses the
  pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography` and {ref}`category-implant` — the mask
  step and implant categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "N+ Implant, NSDM,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `nsdm`, the
  `cnsdm` purposes, the Table C3 definitions and the `NSDM` and `PSDM`
  columns of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `NSDMCD`/`NSDMCDSP`, the
  junction, punch-through, latch-up, implant-angle and area criteria and
  the photoresist thickness.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `nsdm`/`psdm` rules and function
  line, rpm.6, denmos.13, x.7, x.9, x.15a and the flag
  legend.[^pdk-periph]
* SkyWater PDK, *Summary of Key Periphery Rules* — Table
  F3a.[^pdk-summary]
* SkyWater PDK, *Error Messages* page and `errors.csv` — the `nsd` and
  core checks, the rpm.6 and x.9 messages and the "nikon cross"
  checks.[^pdk-errors]
* SkyWater PDK, *Device Details* — the devices built in N+
  diffusion.[^pdk-07]
* SkyWater PDK, *Parasitic Layout Extraction* — the N-diffusion sheet
  resistance.[^pdk-08]
* *S8 / SKY130 Process Steps* sheet — the step, the `NSDM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `NSDM` renders, their layer,
  the `HVNTM` expression and the per-die shape counts.[^mask-renders]
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
* Wikipedia, *CMOS* — NMOS and PMOS side by side, and why each needs its
  own source/drain implant.[^wiki-cmos]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  implant masking by resist.[^txt-02]
* Mack, *Fundamental Principles of Optical Lithography* — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* Levinson, *Principles of Lithography* — overlay budgets and
  non-critical-layer tool choice.[^levinson-2005]

### Deep dive

* Fujimura et al., *JJAP* 1989 — the crust and popping of implanted
  resist.[^fujimura-1989]
* Lukaszek, Reno and Bammi, IIT 1996 — the influence of photoresist on
  wafer charging during high-current arsenic implants.[^lukaszek-1996]
* Krieger et al., *IEEE TED* 1989 — shadowing of a tilted arsenic
  source/drain implant by gate and spacer.[^krieger-1989]
* Smith, in *Ion Implantation: Equipment and Techniques*, 1983 — wafer
  cooling and resist masking problems in implantation.[^smith-1983]
* Romig, Bishop and Rio, IIT 1996 — resist burning in a high-current
  implanter.[^romig-1996]
* Lee et al., IIT 1996 — thick-resist outgassing during MeV implantation
  and its impact on production.[^lee-1996]
* Horsky, IIT 1998 — resist outgassing in high-energy and high-current
  implanters.[^horsky-1998]
* Rubin et al., IIT 2000 — UV photostabilisation of resist before
  high-dose implants.[^rubin-2000]
* Hook et al., *IEEE TED* 2003 — lateral straggle and the mask-proximity
  effect at a resist edge.[^hook-2003]
* Sheu et al., *IEEE TED* 2006 — a compact model of the well-edge
  proximity effect.[^sheu-2006]
* Drennan, Kniffin and Locascio, CICC 2006 — proximity effects and
  analogue layout.[^drennan-2006]
* Ziegler, Ziegler and Biersack, *NIM B* 2010 — SRIM, for the ion range
  in resist.[^ziegler-2010]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  size below which it rises.[^wong-1998]
* ITRS 2001, *Lithography* — mask magnification for the 130 nm
  generation.[^itrs-03]

## Open questions

* The operation that makes the `cnsdm` plate data from `nsdm` and its
  drawing, add and drop purposes is not published, nor what the created
  shapes of Table F2b add to the drawn layer.[^pdk-06]
* That the SONOS cells receive this implant is the step page's inference
  from the device type; Table F2b's `C` marks in the SONOS rows fit it but
  do not say what the created shapes are.[^pdk-06]
* Table F3a's 0.130 enclosures of diffusion and tap and the periphery
  rules' 0.125 µm are not reconciled, and the Error Messages page's 0.29
  core width and spacing and 0.13 core tap enclosure have no counterpart
  in the periphery rules.[^pdk-summary][^pdk-periph][^pdk-errors]
* The implant species, energy and dose, the plate's tone, blank, absorber
  and magnification, the resist and its thickness, and the exposure tool
  are not public; the i-line reading rests on the 0.380 µm rules.
* What the plate number `250` encodes is not stated, and no public source
  lists the `NSDM` plate of the original MPW-4 set
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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 3b,
    3d, 3e, 3f and 7), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/07-other.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-summary]: SkyWater PDK Authors, *Summary of Key Periphery Rules*
    (Table F3a), SkyWater SKY130 PDK documentation, retrieved 2026-09-14.
    <https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/summary/table-f3a-font-end-low-voltage.csv>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_NSDM/` and
    `mpw-00N_HVNTM/` directories with their pages, `job.json`,
    `result.json` and per-die slot JSON files, retrieved 2026-09-14.
    Rendered from the public shuttle repositories under
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
[^wiki-cmos]: Wikipedia, *CMOS*. <https://en.wikipedia.org/wiki/CMOS>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^fujimura-1989]: S. Fujimura, J. Konno, K. Hikazutani and H. Yano,
    "Ashing of Ion-Implanted Resist Layer", *Japanese Journal of Applied
    Physics* **28**(10R), 2130 (1989). <https://doi.org/10.1143/JJAP.28.2130>
[^lukaszek-1996]: W. Lukaszek, S. Reno and R. Bammi, "Influence of
    photoresist on wafer charging during high current arsenic implant",
    *Proc. 11th International Conference on Ion Implantation Technology*
    (1996), pp. 89–92. <https://doi.org/10.1109/IIT.1996.586135>
[^krieger-1989]: G. Krieger, G. Spadini, P. Cuevas and J. Schuur,
    "Shadowing effects due to tilted arsenic source/drain implant", *IEEE
    Transactions on Electron Devices* **36**(11), 2458–2461 (1989).
    <https://doi.org/10.1109/16.43667>
[^smith-1983]: T. C. Smith, "Wafer Cooling and Photoresist Masking
    Problems in Ion Implantation", in *Ion Implantation: Equipment and
    Techniques*, Springer Series in Electrophysics, Springer, 1983,
    pp. 196–213. <https://doi.org/10.1007/978-3-642-69156-0_25>
[^romig-1996]: T. Romig, M. Bishop and V. Rio, "Exploration and
    prevention of photo resist burning in a high current ion implanter",
    *Proc. 11th International Conference on Ion Implantation Technology*
    (1996), pp. 190–193. <https://doi.org/10.1109/IIT.1996.586181>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy
    and high current ion implantation", *1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
[^rubin-2000]: L. Rubin, D. Whiteside, C. Norton, A. Stevenson and
    C. Ukah, "Improved photoresist integrity by UV photostabilization for
    high dose, high energy ion implants", *Proc. 2000 International
    Conference on Ion Implantation Technology*, pp. 817–820.
    <https://doi.org/10.1109/IIT.2000.924279>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices* **50**(9),
    1946–1951 (2003). <https://doi.org/10.1109/TED.2003.815371>
[^sheu-2006]: Y.-M. Sheu, K.-W. Su, S. Tian, S.-J. Yang, C.-C. Wang,
    M.-J. Chen and S. Liu, "Modeling the Well-Edge Proximity Effect in
    Highly Scaled MOSFETs", *IEEE Transactions on Electron Devices*
    **53**(11), 2792–2798 (2006). <https://doi.org/10.1109/TED.2006.884070>
[^drennan-2006]: P. G. Drennan, M. Kniffin and D. Locascio,
    "Implications of Proximity Effects for Analog Design", *IEEE Custom
    Integrated Circuits Conference 2006*, pp. 169–176.
    <https://doi.org/10.1109/CICC.2006.320869>
[^ziegler-2010]: J. F. Ziegler, M. D. Ziegler and J. P. Biersack, "SRIM
    – The stopping and range of ions in matter (2010)", *Nuclear
    Instruments and Methods in Physics Research B* **268**(11–12),
    1818–1823 (2010). <https://doi.org/10.1016/j.nimb.2010.02.091>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
