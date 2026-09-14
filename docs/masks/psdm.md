(mask-psdm)=
# PSDM — P+ Implant

The P+ implant mask is the {term}`reticle` that decides where SKY130's
silicon receives the heavy p-type source/drain dose: on the
{ref}`PSDM <step-081>` page's reading, the resist printed through it at
step 81 is opened over every region drawn in `psdm` — the PMOS sources
and drains, the p+ taps, the PNP emitters and collectors, the P+
diffusion resistors, the p-type diodes and the precision-resistor heads —
the implants {ref}`PSDI <step-082>` and {ref}`2PSDI <step-083>` pass
through the same openings, and the resist is stripped at
{ref}`PDIS <step-084>`. It is the first of the two source/drain implant
{term}`block masks <block mask>` and, with {ref}`NSDM <step-085>`, nearly
the complement of the other across the active area. Its drawn layer
also appears in the PDK's definitions of the precision resistor and the
PNP emitter, and its public record has a quirk: the process-steps sheet
lists the implant step after it among the mask steps, with the mask's own
description. This page gathers what public sources say about the mask
itself — its PDK entry and layers, the plates the process-steps sheet
records for the MPW runs, what the public renders of those runs show, the
lithography it needs and the rules that constrain it. How the step is
performed is on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | PSDM — P+ Implant |
|---|---|
| Mask step | {ref}`PSDM <step-081>`, step 81 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "P+ Implant", `PSDM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cpsdm` mask 32:0, "P+ Implant mask"; drawing 31:20, mask add 31:21, mask drop 31:22, without descriptions[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `psdm` drawing 94:20, "P+ source/drain implant"[^pdk-06] |
| Minimum CD, feature / space | `PSDMCD` 0.38 / `PSDMCDSP` 0.38[^pdk-03] |
| Polarity and tone | Not published. The rule set's function is "Defines opening for N+/P+ implants", and the step page reads the resist as opened where `psdm` is drawn; with a positive resist the plate would be clear over `psdm` and opaque elsewhere (inference). |
| Exposure class | i-line, an inference on the step page from the 0.380 µm width and space; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `260`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 4 steps; see {ref}`Steps that use this mask <mask-psdm-steps>` |

## What the mask defines

The periphery rules give `nsdm` and `psdm` one rule set, "N+/P+
Source/Drain Implants (Nsdm and Psdm)", whose function is "Defines opening for N+/P+
implants", and the layer table describes `psdm` as "P+ source/drain
implant".[^pdk-periph][^pdk-06] The rules tie the layer to the active
pattern: "Diff and tap must be enclosed by their corresponding implant
layers" (psd.9), by 0.125 µm except at a butting edge (psd.5a, psd.5b),
and "Nsdm and psdm cannot overlap diff/tap regions of opposite doping"
(psd.8).[^pdk-periph] The {ref}`PSDM <step-081>` page lists the regions
inside `psdm` from the PDK's device pages — PMOS source/drains, p+ taps,
PNP emitters and collectors and NPN bases, the P+ diffusion resistor,
p-type diodes and the precision poly resistors — and the PDK's
resistance table gives "P-diffusion" 197000 in a column headed
"Resistivity (mohms/sq)".[^pdk-07][^pdk-08] Two of the PDK's layout
definitions use the layer: Table C3 of the *Layers Reference* defines
`prec_resistor` as "rpm AND (poly overlapping poly.rs) AND psdm" and
`pnp_emitter` as "diff AND pnp.dg AND psdm".[^pdk-06]

The PDK's mask generation table, Table F2b, marks the `PSDM` column `C`
("CREATED") in 24 of its 80 device rows: the four p-diffusion and p+
poly resistor rows, the seven 1.8 V PMOS rows, the 5/10.5 V, 16 V and
20 V PMOS, seven p-type diode rows, both parasitic bipolar rows and the
HV PMOS ESD transistor.[^pdk-06] It marks `-`, "Layer not created for the
device", in 35 rows, among them every NMOS, SONOS and varactor row and
the n-type diodes.[^pdk-06] On our reading the created shapes follow the
p-type devices, as the drawn-layer rules do; the table does not say what
the created shapes add to the drawn layer. The two layers of the
source/drain pair are close to complementary: they meet with zero
enclosure at a butting diffusion/tap edge (psd.6) and otherwise keep
0.130 µm from diffusion of the opposite implant (psd.7).[^pdk-periph]

What the mask does not define is the junction edge next to a gate. On
the step pages' readings the implants are self-aligned to the spacers
formed at {ref}`SPE <step-077>`, the gates are capped and receive
nothing, and the poly heads that the implant reaches are those opened by
{ref}`mask-npcm`; the shallow p-type extensions of the PMOS are an open
question on the tip-mask pages ({ref}`mask-ntm`).

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `cpsdm` a `mask` purpose at 32:0 ("P+ Implant
mask") and `drawing` 31:20, `mask add` 31:21 and `mask drop` 31:22 on a
different layer number, the three without descriptions; the drawn layer
is `psdm` at 94:20.[^pdk-06] The {ref}`PSDM <step-081>` page reads the
add and drop purposes as evidence that the reticle is derived by Boolean
operations rather than copied from the drawn layer. The PDK publishes no
such operation. Rule x.9 allows "Shapes on maskAdd or maskDrop layers
("serifs")" in the core only, and x.15a confines "Drawn compatible, mask,
and waffle-drop layers" to test modules, seal ring and frame, with an
exception that names only "FOM/P1M/Metal waffle drop" (flag
P);[^pdk-periph] a design inside the die therefore draws `psdm` (our
reading of x.15a). Table 7 of *Criteria & Assumptions* gives a
"pnp_emitter sizing (S8P GSMC flow)" of 0.05 (`PnpEmitterSzGSMC`) and a
"pnp_emitter sizing (other flows)" of 0.03 (`PnpEmitterSz`), in its
column headed "space", without saying which layer is sized.[^pdk-03]

The PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance
criteria for GDS data", checks the drawn layer under `psd` names and
adds core values the periphery rules do not give: "0.29 min. width of
psdm in COREID" (`psd.c1b`), "0.29 min. spacing/notch of "psdm" in core"
(`psd.c2b`) and "0.12 min. enclosure of p+ tap in core by psdm"
(`psd.c5b`), beside "0.38 min. width of psdm (opposite parallel)"
(`psd.c1a`) and "0.38 min. spacing/notch of "psdm" in core"
(`psd.c2a`).[^pdk-errors] It gives psd.9 as "pdiff/ptap (source of
extendedDrain fet exempted) must be enclosed by psdmZENERID", checks
licon.9 only against poly contacts outside `rpm` ("0.11 min. spacing of
polyLicon1OutRpm & psdm"), and lists "PSDMdrop must be enclosed by
COREID" and "PSDMadd must be enclosed by COREID" (x.9), a module-cut
check at 0.19 (x.12a) and two `cpsdm.nikon` checks, "PSDMmk in the nikon
cross has the wrong polarity" and "PSDMmk is missing from the nikon cross
in the layout".[^pdk-errors] It names no created `PSDM` layer.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `PSDM` the site renders layer 94:20 (`psdm`)
alone, with no Boolean expression and no fill layer, on all eight runs;
its mask record gives the mask-level layer 32:0 and the note "PSDM =
psdm OR grown psdm over pnp emitters".[^mask-renders] The render job has
no sizing step, so, as the {ref}`masks index <masks-renders>` reads the
site in general, the images are unsized drawn `psdm` and do not include
the grown shapes the note describes. The note's operation is of the kind
Table 7's "pnp_emitter sizing" rows and Table C3's `pnp_emitter`
definition suggest (our comparison),[^pdk-03][^pdk-06] but the site gives
no source for it. The note and the choice of layer are one public
derivation from the drawn data, not SkyWater's mask-generation recipe.

The site also renders an image it labels `PSDI`, for step 82, from the
same layer 94:20, with the note "second P+ implant, same drawn layer as
PSDM" and no mask-level layer; its die-by-die shape counts equal those
of `PSDM` on every run, and the masks index does not count it as
evidence of a further plate.[^mask-renders]

Every rendered die of every run carries `psdm` shapes — at least 427 885
on each die; the minimum on each run lies between 427 885 (MPW-5) and
515 813 (MPW-8); on MPW-1 one die accounts for nearly 99 % of the run's
shapes; and counts rarely repeat, on at most seven dies of a run and on
none of MPW-1, MPW-4 or MPW-8.[^mask-renders] The count of 40 dies
therefore says only that every layout has p-type diffusion, as a CMOS
die must; we read the large minimum as shapes that every die of these
runs carries rather than as project content (inference; the site does
not say what they are). The site states the limits of its images:
"These are renders of *drawn* data, not photomask artwork: reticle pitch,
4x reduction, mirroring and the frame features the fab adds are not
modelled."[^mask-renders] Its metadata carries no plate ID, so a render
is tied to a plate in the process-steps sheet only by the acronym `PSDM`,
and the MPW-4 renders come from a different reticle set from the one
whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a `PSDM` plate
as existing on all eight MPW runs, with the plate number `260` on each
and no "Info" note; the tab has no row for `PSDI`.[^steps-sheet] The
plate IDs below are the sheet's; the reticle set is the heading of the
run's columns in the tab ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA260A` |
| MPW-2 | `5CS8007AC` | `S8007AA260A` |
| MPW-3 | `5CS8008AC` | `S8008AA260A` |
| MPW-4 | `5CS8018AC` | `S8018AA260A` |
| MPW-5 | `5CS8011AC` | `S8011AA260A` |
| MPW-6 | `5CS8014AC` | `S8014AA260A` |
| MPW-7 | `5CS8016AC` | `S8016AA260A` |
| MPW-8 | `5CS8017AC` | `S8017AA260A` |

* **Plate number.** The sheet does not say what `260` encodes. It lies
  between `257` for `HVNTM` (step 68) and `265` for `LICM1` (step 93),
  while `NSDM`, the next mask step, is `250`, so the numbers do not
  follow process order and no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `PSDM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`, whose plates no public
  source lists ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`PSDM <step-081>` page puts the 0.380 µm
width and space at {math}`k_1 = 0.38 \times 0.6 / 0.365 \approx 0.62` on
an i-line stepper of NA 0.6, quotes ASML's statement that older exposure
tools "migrate to the lithography of choice for less critical
layers",[^asml-30] and infers an i-line level; the
{ref}`i-line stepper <machine-i-line-stepper>` page lists it there. At
the NA 0.48 low end of ASML's PAS 5500/275D[^asml-pas5500-275d] the same
feature has {math}`k_1 \approx 0.50`, and the Error Messages page's
0.29 core width and spacing[^pdk-errors] would be at
{math}`k_1 \approx 0.48` at NA 0.6 and 0.38 at NA 0.48 (our arithmetic);
the step page does not discuss the core values. SkyWater lists "ASML
I-line stepper" and "ASML I-line scanner" among its tools but assigns no
layer to them.[^skw-01]

**Mask errors.** Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns";[^wong-1998]
at 365 nm that threshold is about 0.38 µm at NA 0.48 and 0.30 µm at
NA 0.60 (our arithmetic), so the 0.38 µm periphery features lie at or
above it and would print a plate CD error at about its own size, while
0.29 µm core features would magnify it (inference).

**Resist.** Nothing is etched through this resist; it must stop the
high-dose p-type implants wherever the plate leaves it. The step page
reads a positive i-line resist of about 1 µm, citing the PDK's generic
"Photoresist thickness" of 1.14 µm, and argues that the thickness is set
less by stopping power than by coverage over the capped gates and by
the resist's endurance under a dose of the order of
10¹⁵ cm⁻².[^pdk-03] The ion range in resist is what SRIM
computes.[^ziegler-2010] Smith treated wafer cooling and resist masking
problems in implantation,[^smith-1983] Romig, Bishop and Rio resist
burning in a high-current implanter,[^romig-1996] Lee et al., Horsky and
Carpenter and Fecteau resist outgassing and its cost to
productivity,[^lee-1996][^horsky-1998][^carpenter-2002] and Rubin et al.
UV photostabilisation of resist before high-dose
implants;[^rubin-2000] Fujimura et al. measured the crust that such a
dose leaves for {ref}`PDIS <step-084>` to remove.[^fujimura-1989]
SkyWater's resist, its thickness and any hardening are not public; the
consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Resist edges.** Ions scattered out of a resist edge implant the
silicon near it — Hook et al. measured the lateral straggle and
mask-proximity effect,[^hook-2003] Sheu et al. modelled the well-edge
version[^sheu-2006] and Drennan, Kniffin and Locascio set out its
meaning for analogue layout[^drennan-2006] — and the step page reads the
0.125–0.130 µm enclosure and spacing rules as reflecting such effects;
the PDK does not state their purpose. Table 3f gives "High current"
implants an angle of 0° (`HCIMPA`),[^pdk-03] and Krieger et al. described
the shadowing of a tilted source/drain implant by the gate and
spacer;[^krieger-1989] the step pages leave the angle of
{ref}`2PSDI <step-083>` open.

**Pattern transfer.** On the step pages' readings the pattern is
transferred into the silicon, and into the poly heads opened by the
nitride cut, as dopant by {ref}`PSDI <step-082>` on the
{ref}`high-current implanter <machine-high-current-implanter>` class and
by {ref}`2PSDI <step-083>` on the high-current or
{ref}`medium-current <machine-medium-current-implanter>` class, through
the thin {ref}`SPOX <step-080>` oxide, and the resist is removed at
{ref}`PDIS <step-084>` on the
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` and
{ref}`wet bench <machine-wet-bench>` classes. Table 3b gives the result,
an "N+ or P+ S/D (XJ)" with a vertical feature of 0.1 µm and a vertical
space of 0.06 µm (`JCTD` / `LD`); the species, energies and doses are not public.[^pdk-03]

**Overlay.** The {ref}`PSDM <step-081>` page reads the mask as aligned
to the active pattern for the 0.125 µm diffusion enclosure and to poly
for the resistor and licon.9 rules.[^pdk-periph] Where `psdm` and `nsdm`
butt at a diffusion/tap edge the enclosure is 0.000 µm (psd.6), so the
two plates' placement errors meet there (our reading). ASML specifies
"≤ 40 nm" single-machine overlay for the /275D
stepper[^asml-pas5500-275d] (our comparison; how SkyWater budgets the
margin is not public).

(mask-psdm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `PSDM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`PSDM <step-081>`, {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`PDIS <step-084>`

* {ref}`PSDM <step-081>` — coats, exposes and develops the resist over the
  spacers, the nitride cut and the {ref}`SPOX <step-080>` oxide.
* {ref}`PSDI <step-082>` — the heavy p-type source/drain implant through
  the resist windows, self-aligned to the spacers.
* {ref}`2PSDI <step-083>` — a second p-type implant, which its page reads
  as made through the same resist; what it is, is not public.
* {ref}`PDIS <step-084>` — strips the implanted resist and cleans the
  wafer without thinning the oxide beneath.

The next step, {ref}`NSDM <step-085>`, is itself the next mask step: on
its step page's reading it coats the N+ resist on the surface cleaned at
`PDIS`. No step between `PDIS` and it uses the `PSDM` resist. The one
point that needs stating is {ref}`PSDI <step-082>`: the sheet's "Masks"
tab lists step 82 among the mask steps with the same description as step
81, "P+ source drain implant mask", and the renders site renders a `PSDI`
image from `psdm`, but the tab "Run Mask IDs" has no plate row for it and
the step pages read it as the implant through the `PSDM`
resist,[^steps-sheet][^mask-renders] so the rule needs no exception for
this mask.

## Design rules and critical dimensions

The `nsdm`/`psdm` rules of the periphery rules, given for `psdm`, with
the contact, precision-resistor and drain-extended PMOS rules that place
`psdm` and the mask-data rules x.7, x.9 and x.15a; flag P means "Rule
applies to periphery only (outside areaid.ce). A corresponding core rule
may or may not exist.", DE "Rule not checked for source of Drain Extended
device" and NC "Rule not checked by DRC. It should be used as a guideline
only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| psd.1 | "Width of nsdm(psdm)" (P) | 0.380 µm |
| psd.2 | "Spacing of nsdm(psdm) to nsdm(psdm)" (P) | 0.380 µm |
| psd.3 | "Manual merge if less than minimum" | — |
| psd.5a | "Enclosure of diff by nsdm(psdm), except for butting edge" | 0.125 µm |
| psd.5b | "Enclosure of tap by nsdm(psdm), except for butting edge" (P) | 0.125 µm |
| psd.6 | "Enclosure of diff/tap butting edge by nsdm (psdm)" | 0.000 µm |
| psd.7 | "Spacing of NSDM/PSDM to opposite implant diff or tap (for non-abutting diff/tap edges)" | 0.130 µm |
| psd.8 | "Nsdm and psdm cannot overlap diff/tap regions of opposite doping" (DE) | — |
| psd.9 | "Diff and tap must be enclosed by their corresponding implant layers. Rule exempted for […]" (DE) | — |
| psd.10b | "Min area of Psdm" | 0.255 µm² |
| psd.11 | "Min area of n/psdmHoles" | 0.265 µm² |
| licon.9 | "Spacing, no overlap, between poly_licon and psdm; In SKY130DIA/SKY130TMA/SKY130PIR-10 flows, the rule is checked only between (poly_licon outside rpm) and psdm" (P) | 0.110 µm |
| rpm.4 | "prec_resistor must be enclosed by psdm by atleast" | 0.110 µm |
| depmos.12 | "de_pFet_source must be enclosed by psdm by" | 0.130 µm |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.9 | "Shapes on maskAdd or maskDrop layers ("serifs") are allowed in core only. Exempted are: […]" | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |

The periphery table heads the set "(n/ psd.-)" and numbers its rules
without a layer prefix; the names above are those of the Error Messages
page.[^pdk-periph][^pdk-errors] Table 2 of *Criteria & Assumptions*
repeats the width and space as `PSDMCD` 0.38 and `PSDMCDSP` 0.38, Table 7
gives "Min Psdm area" as 0.255 (`MinPsdmArea`) and "Min N/Psdm hole area"
as 0.265 (`MinNPsdmHole`) in its column headed "CD", matching psd.10b and
psd.11, and Table 3b's "N+ or P+ S/D (XJ)" (0.1 / 0.06), "Max (N+ or P+
S/D outdiff.) next to isol. edge" (0.007, `LDST`) and the same for "6 V
reg. devices" (0.05, `LDST5`) describe the junction the implant
forms.[^pdk-03] Table 3d gives punch-through spacings "n+ - n+ or p+-p+"
of 0.23 (`DPTS`) and "p+ in nwell to pwell" of 0.05 (`PPTS`), and Table
3e a "Minimum n+ or p+ - nwell spacing to prevent latch-up" of 0.23
(`NPNWLU`) and a "Max. overlap of n-well by p+ tap" of 0.06
(`XNWPTS`).[^pdk-03] Table F3a of the *Summary of Key Periphery Rules*
gives `n/psdm` a width of 0.380, a spacing of 0.380 and "Yes" under
"Manual merge ?", and, in its diff and tap columns, spacings of 0.130 and
enclosures of 0.130, against the 0.125 µm of psd.5a and psd.5b (our
reading of the columns; the PDK does not reconcile
them).[^pdk-summary][^pdk-periph] For the plate, psd.1 and psd.2 set the
smallest periphery features, 0.380 µm lines and spaces with islands of
0.255 µm², and the Error Messages page's core checks allow 0.29.

## Related pages

* {ref}`PSDM <step-081>`, {ref}`PSDI <step-082>`,
  {ref}`2PSDI <step-083>` and {ref}`PDIS <step-084>` — the mask step, the
  two implants and the strip.
* {ref}`NSDM <step-085>` — the complementary N+ mask;
  {ref}`RTAD <step-088>` — the source/drain anneal.
* {ref}`mask-npcm` — the nitride cut through which the implant reaches the
  poly heads; {ref}`mask-ntm` — the tip mask of the same module.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the `PSDI` render and the "Masks" tab.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-high-current-implanter` and
  {ref}`machine-medium-current-implanter` — the implant classes that use
  the pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography` and {ref}`category-implant` — the mask
  step and implant categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "P+ Implant, PSDM,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `psdm`, the
  `cpsdm` purposes, the `prec_resistor` and `pnp_emitter` definitions and
  the `PSDM` column of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `PSDMCD`/`PSDMCDSP`, the
  junction, punch-through, latch-up, implant-angle, area and
  `pnp_emitter` criteria and the photoresist thickness.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `nsdm`/`psdm` rules and function
  line, licon.9, rpm.4, depmos.12, x.7, x.9, x.15a and the flag
  legend.[^pdk-periph]
* SkyWater PDK, *Summary of Key Periphery Rules* — Table
  F3a.[^pdk-summary]
* SkyWater PDK, *Error Messages* page and `errors.csv` — the `psd` and
  core checks, the licon.9 and x.9 messages and the "nikon cross"
  checks.[^pdk-errors]
* SkyWater PDK, *Device Details* — the devices built in P+
  diffusion.[^pdk-07]
* SkyWater PDK, *Parasitic Layout Extraction* — the P-diffusion sheet
  resistance.[^pdk-08]
* *S8 / SKY130 Process Steps* sheet — the step, the `PSDM` plates of
  MPW-1 to MPW-8, the "Masks" tab and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `PSDM` and `PSDI` renders,
  their layer and note, and the per-die shape counts.[^mask-renders]
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

* Hook et al., *IEEE TED* 2003 — lateral straggle and the mask-proximity
  effect at a resist edge.[^hook-2003]
* Sheu et al., *IEEE TED* 2006 — a compact model of the well-edge
  proximity effect.[^sheu-2006]
* Drennan, Kniffin and Locascio, CICC 2006 — proximity effects and
  analogue layout.[^drennan-2006]
* Smith, in *Ion Implantation: Equipment and Techniques*, 1983 — wafer
  cooling and resist masking problems in implantation.[^smith-1983]
* Romig, Bishop and Rio, IIT 1996 — resist burning in a high-current
  implanter.[^romig-1996]
* Lee et al., IIT 1996 — thick-resist outgassing during MeV implantation
  and its impact on production.[^lee-1996]
* Horsky, IIT 1998 — resist outgassing in high-energy and high-current
  implanters.[^horsky-1998]
* Carpenter and Fecteau, IIT 2002 — productivity during high-pressure
  resist outgassing.[^carpenter-2002]
* Rubin et al., IIT 2000 — UV photostabilisation of resist before
  high-dose implants.[^rubin-2000]
* Fujimura et al., *JJAP* 1989 — the crust and popping of implanted
  resist.[^fujimura-1989]
* Krieger et al., *IEEE TED* 1989 — shadowing of a tilted source/drain
  implant by gate and spacer.[^krieger-1989]
* Ziegler, Ziegler and Biersack, *NIM B* 2010 — SRIM, for the ion range
  in resist.[^ziegler-2010]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  size below which it rises.[^wong-1998]
* ITRS 2001, *Lithography* — mask magnification for the 130 nm
  generation.[^itrs-03]

## Open questions

* The operation that makes the `cpsdm` plate data from `psdm` and its
  drawing, add and drop purposes is not published; Table 7's
  `pnp_emitter` sizing rows do not name the layer they size, and the
  renders' note about "grown psdm over pnp emitters" names no
  source.[^pdk-06][^pdk-03][^mask-renders]
* What `2PSDI` implants through this resist is not public.
* Table F3a's 0.130 enclosures of diffusion and tap and the periphery
  rules' 0.125 µm are not reconciled, and the Error Messages page's 0.29
  core width and spacing have no counterpart in the periphery
  rules.[^pdk-summary][^pdk-periph][^pdk-errors]
* The plate's tone, blank, absorber and magnification, the resist and
  its thickness, and the exposure tool are not public; the i-line
  reading rests on the 0.380 µm rules.
* What the plate number `260` encodes is not stated, and no public source
  lists the `PSDM` plate of the original MPW-4 set
  `5CS8010AC`.[^steps-sheet][^mask-renders]

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tabs "Sheet1" (step number, code and description), "Masks"
    (mask steps with step numbers and descriptions), "Run Mask IDs" (the
    mask table set against MPW-1 to MPW-8, with "Exists" and "Plate ID"
    columns per run) and "Sheet4" (mask types), retrieved 2026-09-14.
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
    directory: `README.md` and, for each run, the `mpw-00N_PSDM/` and
    `mpw-00N_PSDI/` directories with their pages, `job.json`,
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
[^carpenter-2002]: N. Carpenter and T. Fecteau, "Process and
    productivity improvements during high pressure photoresist
    outgassing", *Proc. 14th International Conference on Ion Implantation
    Technology* (2002), pp. 507–510.
    <https://doi.org/10.1109/IIT.2002.1258053>
[^rubin-2000]: L. Rubin, D. Whiteside, C. Norton, A. Stevenson and
    C. Ukah, "Improved photoresist integrity by UV photostabilization for
    high dose, high energy ion implants", *Proc. 2000 International
    Conference on Ion Implantation Technology*, pp. 817–820.
    <https://doi.org/10.1109/IIT.2000.924279>
[^fujimura-1989]: S. Fujimura, J. Konno, K. Hikazutani and H. Yano,
    "Ashing of Ion-Implanted Resist Layer", *Japanese Journal of Applied
    Physics* **28**(10R), 2130 (1989). <https://doi.org/10.1143/JJAP.28.2130>
[^krieger-1989]: G. Krieger, G. Spadini, P. Cuevas and J. Schuur,
    "Shadowing effects due to tilted arsenic source/drain implant", *IEEE
    Transactions on Electron Devices* **36**(11), 2458–2461 (1989).
    <https://doi.org/10.1109/16.43667>
[^ziegler-2010]: J. F. Ziegler, M. D. Ziegler and J. P. Biersack, "SRIM
    – The stopping and range of ions in matter (2010)", *Nuclear
    Instruments and Methods in Physics Research B* **268**(11–12),
    1818–1823 (2010). <https://doi.org/10.1016/j.nimb.2010.02.091>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
