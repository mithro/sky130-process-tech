(mask-lvtnm)=
# LVTNM — Low Vt Nch\*

The low-Vt N-channel mask is the {term}`reticle` that sorts SKY130's
low-voltage transistors into threshold flavours: on the
{ref}`LVTNM <step-014>` page's reading, the resist printed through it at
step 14 decides where the {ref}`LVTNI <step-015>` channel implant goes,
and is stripped again at {ref}`LVTNIS <step-016>`. It is an implant
{term}`block mask` with coarse rules, and the first mask of the well and
channel module. What makes it unusual is that the public record does not
settle what its openings are: the PDK describes the drawn layer as
blocking an implant, the step pages leave the polarity open, and one
public derivation from the drawn tape-out data adds created shapes to the
drawn layer.
This page gathers what public sources say about the mask itself — its
PDK entry and layers, the plates the process-steps sheet records for the
MPW runs, what the public renders of those runs show, the lithography it
needs and the rules that constrain it. How the step is performed is on
the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | LVTNM — Low Vt Nch\* |
|---|---|
| Mask step | {ref}`LVTNM <step-014>`, step 14 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Low Vt Nch\*", `LVTNM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `clvtnm` mask 25:0, "Low Vt Nch mask"; drawing 25:44, mask add 25:43, mask drop 25:42[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `lvtn` drawing 125:44, "Low-Vt NMOS device"[^pdk-06] |
| Minimum CD, feature / space | `LVTNMCD` 0.38 / `LVTNMCDSP` 0.38[^pdk-03] |
| Polarity and tone | Not published. The step page leaves open whether the resist is opened over `lvtn` (a counter-doping implant) or everywhere except `lvtn` (a baseline implant that low-Vt devices skip), and favours the second; the plate's tone follows from that choice and from the resist, neither public. |
| Exposure class | i-line, an inference on the step page from the 0.380 µm width and space; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `038`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 3 steps; see {ref}`Steps that use this mask <mask-lvtnm-steps>` |

## What the mask defines

The PDK describes the drawn layer in two ways. `gds_layers.csv` calls
`lvtn` "Low-Vt NMOS device",[^pdk-06] but the function line of its rule
set is wider: "Define regions to block Vt adjust implant for low Vt LV
PMOS/NMOS, SONOS FETs and Native NMOS".[^pdk-periph] The device pages
describe the transistors that result in the same terms: the low-VT NMOS
and PMOS cross-sections are "identical to the std NMOS FET" (or PMOS
FET) "except for the VT adjust implants (to achieve the lower VT)", the
3.3 V and 5 V native NMOS are "constructed by blocking out all VT
implants", and the 20 V native NMOS "has all Vt implants blocked to
achieve a very low VT".[^pdk-07] The {ref}`LVTNM <step-014>` page takes
the word "block", and the fact that one layer serves NMOS and PMOS of
opposite channel type, as grounds for favouring a reticle that covers
the drawn `lvtn` regions while {ref}`LVTNI <step-015>` implants the rest;
the {ref}`LVTNI <step-015>` page sets out the counter-doping alternative
and cites a Round Rock patent that obtains low-Vt devices with a
"counter-doped channel region".[^pat-vt-rrr] Neither page settles it.

The PDK's mask generation table, Table F2b, marks the `LVTNM` column
`C` ("CREATED") in 28 of its 80 device rows: the low-Vt 1.8 V NMOS and
PMOS, both high-Vt PMOS rows, both `pmos_core` rows, the low-Vt NMOS
core device, the low-Vt, high-Vt and HV varactors, the four SONOS
rows, the 5 V and 3 V native NMOS, all five UHV 5/20 V drain-extended
rows, six diode rows and the HV native ESD transistor.[^pdk-06] It
marks `-`, "Layer not created for the device", in the standard 1.8 V
NMOS and PMOS rows.[^pdk-06] The high-Vt PMOS and `pmos_core` rows are
not devices the `lvtn` function line names, and on the table the three
1.8 V PMOS flavours differ in which of the two threshold masks they
receive: the standard PMOS `HVTPM` only, the low-Vt PMOS `LVTNM` only
and the high-Vt PMOS both ({ref}`mask-hvtpm`; our reading of the
rows).[^pdk-06] The table does not say what the implants through the
two masks do, so it does not settle the polarity either; on our reading,
it shows that the plate is not the drawn `lvtn` alone.

What the mask does not define is the baseline threshold of the other
devices: on the step pages' readings the P-channel threshold implant
{ref}`LVTPI <step-020>` goes through the N-well resist, the high-Vt
PMOS implants through the {ref}`HVTPM <step-022>` resist and the
N-channel implant {ref}`NCHI <step-045>` through the low-voltage oxide
resist. A multi-threshold process is a circuit designer's tool: Mutoh et
al. combined low-threshold transistors for speed with high-threshold
ones that suppress stand-by leakage in one 0.5 µm LSI.[^mutoh-1995]

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `clvtnm` a `mask` purpose at 25:0 ("Low Vt Nch
mask") and `drawing` 25:44, `mask add` 25:43 and `mask drop` 25:42 on
the same layer number — one of only two mask-level layers whose other
purposes share its number ({ref}`masks-index`).[^pdk-06] The drawn layer
is `lvtn` at 125:44, a layer number it shares with `hvntm` 125:20; the
layer table also has an identifier `areaid.lvt` at 81:108, "Low-Vt
identifier".[^pdk-06] The PDK publishes no operation from `lvtn` to the
plate. The {ref}`LVTNM <step-014>` page reads the add and drop purposes
as showing that the reticle is derived by Boolean operations rather
than copied. Rule x.9 allows "Shapes on maskAdd or maskDrop layers
("serifs")" in the core only, and x.15a confines mask layers to test
modules, seal ring and frame, with an exception that names only
"FOM/P1M/Metal waffle drop" (flag P).[^pdk-periph] A design inside the
die therefore draws `lvtn` (our reading of x.15a, which does not say
what applies in the core).

Two definitions in Table C3 of the *Layers Reference* bear on the
layer: `LVTN_Gate`, "Gate overlapping lvtn", used by rule ncm.5; and
`Var_channel`, "poly AND tap AND (nwell NOT hvi) NOT areaid.ce", used
by rule lvtn.10, which requires `lvtn` to be enclosed by "(nwell not
overlapping Var_channel)".[^pdk-06][^pdk-periph] The `C` marks of Table
F2b in rows that the `lvtn` function line does not name (above) point to
created shapes, but the PDK does not give the operation that makes
them.[^pdk-06]

The PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance
criteria for GDS data", names checks on the mask data that the rule
tables do not: `clvtnm.1`, "0.38 min. width of clvtnm in periphery",
`clvtnm.2`, "0.38 min. spacing/notch of CLLVTNM", and two `clvtnm.nikon`
checks, "LVTNMmk in the nikon cross has the wrong polarity" and
"LVTNMmk is missing from the nikon cross in the layout".[^pdk-errors] It
does not define `CLLVTNM`; we read it as the created `LVTNM` data
(inference from the rule name), so the PDK checks the created layer at
the same 0.38 µm as the drawn one without saying how it is made. The
page's message for lvtn.3b gives "0.19 min spacing of lvtn(peri) to
pfet along S/D direction", against the 0.235 µm of the periphery
rules;[^pdk-errors][^pdk-periph] the PDK does not reconcile the two.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. `LVTNM` is one of the masks the site's README
calls "fab-derived" and evaluates "as a boolean expression over drawn
layers": on all eight runs the expression is
`125:44 OR (64:20 AND (78:44 OR 81:2))`, which in the layer names of
`gds_layers.csv` is `lvtn` OR (`nwell` AND (`hvtp` OR
`areaid.ce`)).[^mask-renders][^pdk-06] Its mask record lists the drawn
layer 125:44 and the mask-level layer 25:0, with the note "drawn lvtn
plus a created part [nwell AND (hvtp OR areaid.ce)] OR (LV nwell over
varactors); only the drawn part is rendered".[^mask-renders] The note
contradicts the expression twice, as the
{ref}`masks index <masks-derivations>` records: the expression renders
the created part, not only the drawn part, and it has no term for the
"(LV nwell over varactors)" the note describes. The site gives no
source for the expression or the note. They are one public derivation
from the drawn data, not SkyWater's mask-generation recipe, and they
differ from the index's pairing of the mask with `lvtn` alone.

The created part is consistent in kind with the Table F2b rows above:
the high-Vt PMOS (`hvtp` inside `nwell`) and `pmos_core` (`areaid.ce`,
"Memory (SRAM) core cell identifier") rows, which the `lvtn` function
line does not name, are marked `C` for `LVTNM` (our
comparison).[^pdk-06][^mask-renders] Since
the site names no source, that agreement may only mean that both start
from the same public table, and it says nothing about the resist
polarity.

All 40 rendered dies of every run carry shapes, but that is not 40
designs with low-Vt devices: every die carries at least 2 194 shapes,
the minimum on each run is 2 194 (MPW-2 to MPW-5), 2 313 (MPW-6 to
MPW-8) or 2 809 (MPW-1), and on each run 6 to 23 of the 40 dies carry
a count that another die of the run shares — 2 194 on five to seven dies
of each of MPW-2 to MPW-5, and 2 973 on nine dies of
MPW-8.[^mask-renders] We read the repeated counts as shapes common to
the dies rather than to the projects (inference); the site does not say
what they are, and with the expression they may include created shapes
as well as drawn `lvtn`. The site states the limits of its images:
"These are renders of *drawn* data, not photomask artwork: reticle
pitch, 4x reduction, mirroring and the frame features the fab adds are
not modelled."[^mask-renders] Its metadata carries no plate ID, so a
render is tied to a plate in the process-steps sheet only by the
acronym `LVTNM`, and the MPW-4 renders come from a different reticle set
from the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `LVTNM`
plate as existing on all eight MPW runs, with the plate number `038` on
each and no "Info" note.[^steps-sheet] The plate IDs below are the
sheet's; the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA038A` |
| MPW-2 | `5CS8007AC` | `S8007AA038A` |
| MPW-3 | `5CS8008AC` | `S8008AA038A` |
| MPW-4 | `5CS8018AC` | `S8018AA038A` |
| MPW-5 | `5CS8011AC` | `S8011AA038A` |
| MPW-6 | `5CS8014AC` | `S8014AA038A` |
| MPW-7 | `5CS8016AC` | `S8016AA038A` |
| MPW-8 | `5CS8017AC` | `S8017AA038A` |

* **Plate number.** The sheet does not say what `038` encodes; it falls
  between `020` for `FOM` and `150` for `DNM`, which precede it in the
  flow, but the numbers do not follow process order elsewhere (`NWM`,
  three steps later, is `010`), so no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `LVTNM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`, whose plates no public
  source lists ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`LVTNM <step-014>` page puts the 0.380 µm
width and space at {math}`k_1 \approx 0.62` on an i-line lens of NA 0.6
and infers an i-line level; the
{ref}`i-line stepper <machine-i-line-stepper>` page lists it there.
SkyWater lists "ASML I-line stepper" and "ASML I-line scanner" among its
tools but assigns no layer to them.[^skw-01] ASML's PAS 5500/275D runs
at NA 0.48–0.60,[^asml-pas5500-275d] at which the same feature has
{math}`k_1 = 0.38 \times 0.48 / 0.365 \approx 0.50` at the low end (our
arithmetic).

**Mask errors.** Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns".[^wong-1998]
At 365 nm that threshold is about 0.38 µm at NA 0.48 and 0.30 µm at
NA 0.60 (our arithmetic), so the smallest `LVTNM` features lie at or
just above it, and a CD error on the plate would print at about its own
size (inference). The rules that matter more are placement rules (below).

**Resist.** Nothing is etched through this resist; it only has to stop
the {ref}`LVTNI <step-015>` implant wherever the plate leaves resist.
The step page reads a positive i-line resist of about 1 µm for a
channel implant of tens of keV, with a wide margin, and cites the PDK's
generic "Photoresist thickness" of 1.14 µm as the order of
thickness;[^pdk-03] the ion range in resist that sets such a margin is
what SRIM computes.[^ziegler-2010] Ross et al. stabilised three i-line
resists for implant with a flood electron beam, which reduced
post-implant shrinkage and CD variation and eliminated popping during
removal.[^ross-1996] SkyWater's resist, its thickness and any hardening
are not public. The consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Resist edges.** Ions also scatter out of the resist edge: "Some of the
ions scattered out of the edge of the photoresist are implanted in the
silicon surface near the mask edge, altering the threshold voltage of
those devices", with shifts "of up to 100 mV … over a lateral distance
on the order of a micrometer", in the words of Hook et al., who model a
thick well resist.[^hook-2003] Sheu et al. model the well-edge proximity
effect,[^sheu-2006] Drennan, Kniffin and Locascio set out what such
effects mean for analogue layout,[^drennan-2006] and Faricelli reviews
the process features that make device behaviour depend on its
neighbourhood.[^faricelli-2010] A channel-implant resist is thinner than
a well resist, and the PDK does not say whether the 0.180 µm spacing of
`lvtn` to a gate (lvtn.3a) allows for such scattering; we read it as
partly a placement margin (inference).

**Pattern transfer.** On the step pages' readings the pattern is
transferred into the silicon as dopant by the {ref}`LVTNI <step-015>`
implant on the
{ref}`medium-current implanter <machine-medium-current-implanter>`
class, through the pad oxide, and the resist is removed at
{ref}`LVTNIS <step-016>` on the
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` and
{ref}`wet bench <machine-wet-bench>` classes. The species, energy and
dose are not public.

**Overlay.** The {ref}`LVTNM <step-014>` page reads the mask as aligned
to the trench pattern of {ref}`FOM <step-004>` and notes that the
0.180 µm enclosure of a gate by `lvtn` (lvtn.4b) couples this level to
the poly mask printed much later.[^pdk-periph] Both register to the
same active pattern on the step pages' readings ({ref}`mask-p1m`), so
the enclosure must absorb the overlay of both against it; ASML
specifies "≤ 40 nm" single-machine overlay for the /275D
stepper[^asml-pas5500-275d] (our comparison; how SkyWater budgets the
margin is not public).

(mask-lvtnm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `LVTNM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`LVTNM <step-014>`, {ref}`LVTNI <step-015>`, {ref}`LVTNIS <step-016>`

* {ref}`LVTNM <step-014>` — coats, exposes and develops the resist.
* {ref}`LVTNI <step-015>` — the channel implant through the resist
  windows, whose species and polarity the step page leaves open.
* {ref}`LVTNIS <step-016>` — strips the implanted resist and cleans the
  wafer.

The next step, {ref}`NWM <step-017>`, is itself the next mask step: on
its step page's reading it coats the thick N-well resist on the cleaned
surface. No step between `LVTNIS` and it uses the `LVTNM` resist, and
there is no exception to the rule for this mask. On the step pages'
readings the implant placed through this resist is annealed with the
rest of the module at {ref}`RTAI <step-034>`.

## Design rules and critical dimensions

The `lvtn` rules of the periphery rules, with the poly and `ncm` rules
that refer to the layer; flag P means "Rule applies to periphery only
(outside areaid.ce). A corresponding core rule may or may not
exist.".[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| lvtn.1a | "Min width of lvtn" | 0.380 µm |
| lvtn.2 | "Min space lvtn to lvtn" | 0.380 µm |
| lvtn.3a | "Min spacing of lvtn to gate. Rule exempted inside UHVI." (P) | 0.180 µm |
| lvtn.3b | "Min spacing of lvtn to pfet along the S/D direction" (P) | 0.235 µm |
| lvtn.4b | "Min enclosure of gate by lvtn. Rule exempted inside UHVI." (P) | 0.180 µm |
| lvtn.9 | "Min spacing, no overlap, between lvtn and hvtp" | 0.380 µm |
| lvtn.10 | "Min enclosure of lvtn by (nwell not overlapping Var_channel) (exclude coincident edges)" | 0.380 µm |
| lvtn.12 | "Min spacing between lvtn and (nwell inside areaid.ce)" | 0.380 µm |
| lvtn.13 | "Min area of lvtn" | 0.265 µm² |
| lvtn.14 | "Min area of lvtn Holes" | 0.265 µm² |
| poly.1b | "Min channel length (poly width) for pfet overlapping lvtn […]" | 0.350 µm |
| ncm.5 | "Min space, no overlap, between ncm and (LVTN_gate) OR (diff containing lvtn)" (P) | 0.230 µm |

Table 2 of *Criteria & Assumptions* repeats the width and space as
`LVTNMCD` 0.38 and `LVTNMCDSP` 0.38, and Table 4 gives a "Channel length
for low Vt PMOS" of 0.35 (`lvtpmos_poly`), matching poly.1b, and a
"Width of the Low Leakage gate on each side of LowVt Pmos connected to
power rails (requirement based on exp data)" of 0.28
(`LvtEnc_forPowerRail`).[^pdk-03][^pdk-periph] The Error Messages page
adds `clvtnm.1` and `clvtnm.2` at 0.38 for the created layer and gives
lvtn.3b as 0.19 (above).[^pdk-errors] For the plate, lvtn.1a, lvtn.2 and
the two area rules set the smallest features — 0.380 µm lines, spaces
and islands of 0.265 µm² — and the gate spacing and enclosure rules set
where its edges may fall relative to the active and poly patterns.

## Related pages

* {ref}`LVTNM <step-014>`, {ref}`LVTNI <step-015>` and
  {ref}`LVTNIS <step-016>` — the mask step, the implant and the strip.
* {ref}`mask-hvtpm` — the other threshold mask of the module,
  which the high-Vt PMOS rows of Table F2b pair with this one.
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

* SkyWater PDK, *Masks* page and `masks.csv` — "Low Vt Nch\*, LVTNM,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `lvtn`, the
  `clvtnm` purposes, `areaid.lvt`, `areaid.ce`, the Table C3 definitions
  and the `LVTNM` column of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `LVTNMCD`/`LVTNMCDSP`,
  `lvtpmos_poly`, `LvtEnc_forPowerRail` and the photoresist
  thickness.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `lvtn` rules and function line,
  poly.1b, ncm.5, x.9, x.15a and the flag legend.[^pdk-periph]
* SkyWater PDK, *Error Messages* page and `errors.csv` — the `clvtnm`
  width, spacing and "nikon cross" checks and the lvtn.3b
  message.[^pdk-errors]
* SkyWater PDK, *Device Details* — the low-Vt and native devices and
  their "VT adjust implants".[^pdk-07]
* *S8 / SKY130 Process Steps* sheet — the step, the `LVTNM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `LVTNM` expression, note and
  per-die shape counts.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the i-line exposure
  tools.[^skw-01]
* ASML, *PAS 5500/275D* data sheet — NA range and single-machine
  overlay of an i-line stepper.[^asml-pas5500-275d]

### High-level understanding

* Wikipedia, *Multi-threshold CMOS* — why several thresholds are offered
  and how they are set.[^wiki-mtcmos]
* Wikipedia, *Photomask* — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wikipedia, *Ion implantation* — masking, range and
  energy.[^wiki-implant]
* Mack, *Fundamental Principles of Optical Lithography* — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* Levinson, *Principles of Lithography* — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]

### Deep dive

* Mutoh et al., *IEEE JSSC* 1995 — low- and high-threshold
  transistors in one LSI, the circuit case for a threshold
  mask.[^mutoh-1995]
* Helm and Zhou (Round Rock Research), US 2011/0006372 — standard and
  low-Vt devices by masked Vt-adjust and counter-doping
  implants.[^pat-vt-rrr]
* Taur and Ning, *Fundamentals of Modern VLSI Devices* — threshold
  voltage against channel doping.[^taur-2009]
* Hook et al., *IEEE TED* 2003 — ions scattered from the resist
  edge and the threshold shifts they cause.[^hook-2003]
* Sheu et al., *IEEE TED* 2006 — a compact model of the
  well-edge proximity effect.[^sheu-2006]
* Drennan, Kniffin and Locascio, CICC 2006 — proximity effects and
  analogue layout.[^drennan-2006]
* Faricelli, CICC 2010 — a review of layout-dependent proximity
  effects and their process causes.[^faricelli-2010]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  size below which it rises.[^wong-1998]
* Ross et al., *Proc. SPIE* 1996 — electron-beam stabilisation of i-line
  implant resists.[^ross-1996]
* Ziegler, Ziegler and Biersack, *NIM B* 2010 — SRIM, for the ion range
  in resist.[^ziegler-2010]
* ITRS 2001, *Lithography* — mask magnification for the 130 nm
  generation.[^itrs-03]

## Open questions

* Whether the plate opens the resist over `lvtn` or over everything
  else, and so whether `LVTNI` is a counter-doping or a baseline
  implant, is not public; the step pages favour the block reading.
* The operation that makes the `clvtnm` plate data is not published.
  Table F2b marks created `LVTNM` shapes in rows the `lvtn` function
  line does not name,[^pdk-06] the Error Messages page checks a created
  layer it does not define,[^pdk-errors] and the renders site renders
  one expression for them whose note contradicts it;[^mask-renders]
  which, if either, matches the plate is not public.
* The plate's tone, blank, absorber and magnification, the resist and
  its thickness, and the exposure tool are not public; the i-line
  reading rests on the 0.380 µm rules.
* The Error Messages page's 0.19 for lvtn.3b and the periphery rules'
  0.235 µm are not reconciled in the PDK.[^pdk-errors][^pdk-periph]
* The renders do not say what the shapes common to many dies of a run
  are, so how many projects on each shuttle use low-Vt or native devices
  is not shown.[^mask-renders]
* What the plate number `038` encodes is not stated, and no public
  source lists the `LVTNM` plate of the original MPW-4 set
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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2 and
    4), SkyWater SKY130 PDK documentation.
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
    directory: `README.md` and, for each run, the `mpw-00N_LVTNM/`
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
[^wiki-mtcmos]: Wikipedia, *Multi-threshold CMOS*.
    <https://en.wikipedia.org/wiki/Multi-threshold_CMOS>
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
[^mutoh-1995]: S. Mutoh, T. Douseki, Y. Matsuya, T. Aoki, S. Shigematsu
    and J. Yamada, "1-V power supply high-speed digital circuit
    technology with multithreshold-voltage CMOS", *IEEE Journal of
    Solid-State Circuits* **30**(8), 847–854 (1995).
    <https://doi.org/10.1109/4.400426>
[^pat-vt-rrr]: M. Helm and X. Zhou (Round Rock Research), *Formation of
    standard voltage threshold and low voltage threshold MOSFET
    devices*, US 2011/0006372 A1, published 2011-01-13.
    <https://patents.google.com/patent/US20110006372A1/en>
[^taur-2009]: Y. Taur and T. H. Ning, *Fundamentals of Modern VLSI
    Devices*, 2nd ed., Cambridge University Press, 2009, ISBN
    978-0-521-83294-6. <https://doi.org/10.1017/CBO9781139195065>
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
[^faricelli-2010]: J. V. Faricelli, "Layout-dependent proximity effects
    in deep nanoscale CMOS", *IEEE Custom Integrated Circuits Conference
    2010*, pp. 1–8. <https://doi.org/10.1109/CICC.2010.5617407>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
[^ross-1996]: M. F. Ross, W. R. Livesay, V. Starov, K. Ostrowski and
    S. Y. Wong, "Photoresist stabilization for ion implant processing",
    *Proc. SPIE* **2724**, 632 (1996).
    <https://doi.org/10.1117/12.241862>
[^ziegler-2010]: J. F. Ziegler, M. D. Ziegler and J. P. Biersack, "SRIM
    – The stopping and range of ions in matter (2010)", *Nuclear
    Instruments and Methods in Physics Research B* **268**(11–12),
    1818–1823 (2010). <https://doi.org/10.1016/j.nimb.2010.02.091>
