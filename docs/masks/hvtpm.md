(mask-hvtpm)=
# HVTPM — High Vt PCh\*

The high-Vt P-channel mask is the {term}`reticle` of the second
threshold implant of SKY130's 1.8 V PMOS: on the {ref}`HVTPM <step-022>`
page's reading, the resist printed through it at step 22 is opened over
the PMOS channels that are to have a raised threshold, the implants
{ref}`PCHI <step-023>` and {ref}`PNCHI <step-024>` pass through the same
openings, and the resist is stripped at {ref}`PCHIS <step-025>`. The "V"
in its name is a threshold, not a voltage class. The public record
disagrees about what the plate carries: the step page follows the PDK's
description of the drawn layer `hvtp`, while, on our reading, the PDK's
mask generation table, its DRC error messages and one public derivation
from the drawn tape-out data all point to openings over most low-voltage
N-well. This page gathers what public sources say about the mask itself
— its PDK entry and layers, the plates the process-steps sheet records
for the MPW runs, what the public renders of those runs show, the
lithography it needs and the rules that constrain it. How the step is
performed is on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | HVTPM — High Vt PCh\* |
|---|---|
| Mask step | {ref}`HVTPM <step-022>`, step 22 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "High Vt PCh\*", `HVTPM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `chvtpm` mask 97:0, "High Vt Pch mask"; drawing 88:44, mask add 97:43, mask drop 97:42[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `hvtp` drawing 78:44, "High-Vt LVPMOS implant"[^pdk-06] |
| Minimum CD, feature / space | `HVTPMCD` 0.38 / `HVTPMCDSP` 0.38[^pdk-03] |
| Polarity and tone | Not published. The step page reads the resist as removed over `hvtp`, from the layer's description (inference); on our reading, Table F2b's rows, the Error Messages page's `chvtpm` checks and the renders' expression point to a different set of openings (below), and the plate's tone is not public. |
| Exposure class | i-line, an inference on the step page from the 0.38 µm width and space; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `317`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 4 steps; see {ref}`Steps that use this mask <mask-hvtpm-steps>` |

## What the mask defines

The PDK names the layer's purpose three times. `masks.csv` lists "High
Vt PCh\*"; `gds_layers.csv` describes `hvtp` as "High-Vt LVPMOS
implant"; and the rule set's function line reads "Define Vt adjust
implant region for high Vt LV PMOS;".[^pdk-05][^pdk-06][^pdk-periph] The
devices are the "1.8V high-VT PMOS FET", whose cross-section "is
identical to the std PMOS FET except for the VT adjust implants (to
achieve the higher VT)", and the varactor option `cap_var_hvt`, the
"high VT PMOS device option".[^pdk-07] Unlike `lvtn`, whose function
line speaks of blocking an implant, `hvtp` is described as the region
that receives one, and the {ref}`HVTPM <step-022>` page reads the
reticle polarity from that: resist removed over `hvtp`.
The rules tie the layer to the varactor as well as the transistor:
varac.8 requires the varactor channel to be enclosed by `hvtp` by
0.255 µm and varac.3 keeps `hvtp` 0.180 µm from it otherwise.[^pdk-periph]
Andreani and Mattisson compared inversion-mode and accumulation-mode MOS
varactors for tuning CMOS oscillators.[^andreani-2000]

The PDK's mask generation table, Table F2b, reads differently. It marks
the `HVTPM` column `C` ("CREATED") in 15 of its 80 device rows: the two
p-diffusion resistor rows, the standard 1.8 V PMOS rows, the high-Vt
PMOS rows, the `pmos_core` rows, the high-Vt varactor, the `pDiode`,
high-Vt `pDiode` and photodiode rows and the parasitic PNP.[^pdk-06] It
marks `-`, "Layer not created for the device", in, among others, the
rows of the low-Vt PMOS, the low-Vt and HV varactors, the 5/10.5 V,
16 V and 20 V PMOS and the HV p-diffusion resistor, and in every NMOS
row.[^pdk-06] On the table, then, the standard 1.8 V PMOS receives
created `HVTPM` shapes and the low-Vt PMOS does not, and the three
1.8 V PMOS flavours differ in which of the two threshold masks they
receive: the standard PMOS `HVTPM` only, the low-Vt
PMOS `LVTNM` only and the high-Vt PMOS both
({ref}`mask-lvtnm`; our reading of the rows).[^pdk-06] That pattern
is hard to square with a plate opened over drawn `hvtp` alone, and it
fits a plate opened over low-voltage N-well outside the low-Vt devices
(our reading); the table does not say what the implants do, and the
step pages' reading of the implants' species (the
{ref}`PNCHI <step-024>` page reads BF₂) does not by itself decide
between the two.

What the mask does not define is the baseline PMOS threshold: on the
step pages' readings that is set by {ref}`LVTPI <step-020>` through the
N-well resist. Kao and Chandrakasan describe dual-threshold techniques
that keep low-threshold speed while cutting stand-by
leakage,[^kao-2000] and Kizilyalli et al. show that in an n+-poly
buried-channel PMOS the threshold and minimum gate length cannot be
scaled independently because of punch-through[^kizilyalli-1995] — the
kind of trade a second PMOS threshold offers designers a way around (our
reading).

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `chvtpm` a `mask` purpose at 97:0 ("High Vt Pch
mask"), `mask add` 97:43 and `mask drop` 97:42 on the same layer number,
and a `drawing` purpose at 88:44, a layer number it shares with
`conom` 88:0; 97 also carries `cap2m` 97:44.[^pdk-06] The drawn layer is
`hvtp` at 78:44. The PDK publishes no operation from `hvtp` to the
plate. Rule x.9 allows "Shapes on maskAdd or maskDrop layers
("serifs")" in the core only, and x.15a confines mask layers to test
modules, seal ring and frame, with an exception that names only
"FOM/P1M/Metal waffle drop" (flag P).[^pdk-periph] Table C3 of the
*Layers Reference* defines `LVnwell` as "nwell NOT hvi" and
`Var_channel` as "poly AND tap AND (nwell NOT hvi) NOT
areaid.ce";[^pdk-06] it uses neither to define the plate.

The PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance
criteria for GDS data", uses both. It lists four checks on a layer it
calls `CLHVTPM`, under the rule names `chvtpm.1`, `chvtpm.2a`,
`chvtpm.3` and `chvtpm.4`: "0.38
min. width of CLHVTPM", "0.38 min. spacing/notch of CLHVTPM", "0 min.
enclosure of ((LVnwell not overlapping Var_channel) NOT lvtn) by
CLHVTPM" and "0 min. enclosure of ((LVnwell overlapping Var_channel)
AND hvtp) by CLHVTPM"; it also has a check `hvtp.c1`, "Min/Max
enclosure of nwell by hvtp", with no value, and two `chvtpm.nikon`
checks.[^pdk-errors] The page does not define `CLHVTPM`. We read it as
the created `HVTPM` data (inference from the rule names); on that
reading the PDK requires the created layer to cover low-voltage N-well
outside varactor channels and `lvtn`, and `hvtp` where low-voltage
N-well overlaps a varactor channel — openings over most low-voltage
N-well rather than over drawn `hvtp` alone, consistent with the Table
F2b rows above. The checks state what the layer must cover, not the
operation that makes it.

`masks.csv` also marks "HLow VT PCh Radio\*, HVTRM" as used in SKY130,
with a mask-level layer `chvtrm` 98:0 and a drawn layer `hvtr` 18:20,
"High-Vt RF transistor implant", whose one spacing rule to this layer is
"Min spacing between hvtp to hvtr" (hvtr.2), 0.380 µm; the step list
used in this reference has no mask step for it, and the
{ref}`HVTPM <step-022>` page leaves open whether it is absent from the
flow or folded into this mask.[^pdk-05][^pdk-06][^pdk-periph]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. `HVTPM` is one of the masks the site's README
calls "fab-derived" and evaluates "as a boolean expression over drawn
layers": on all eight runs the expression is
`(64:20 NOT 75:20) NOT 125:44`, which in the layer names of
`gds_layers.csv` is (`nwell` NOT `hvi`) NOT `lvtn`, with no `hvtp`
term.[^mask-renders][^pdk-06] Its mask record lists the drawn layer 64:20
and the mask-level layer 97:0, with the note "created over (LV nwell =
nwell NOT hvi) NOT lvtn, plus hvtp only where nwell overlaps a varactor;
the fab algorithm says do NOT OR hvtp in. Rendered as nwell = a
superset".[^mask-renders] The note contradicts the expression twice, as
the {ref}`masks index <masks-derivations>` records: it ends "Rendered as
nwell = a superset", but the expression subtracts `hvi` and `lvtn`; and
it describes a varactor term that the expression does not include. It
refers to a "fab algorithm" without naming any source. The expression
and note are one public derivation from the drawn data, not SkyWater's
mask-generation recipe, and they differ from the index's and the step
page's pairing of the mask with `hvtp`.

The expression's first term is the Boolean the PDK calls `LVnwell`, and
its rows agree with Table F2b's `C` marks above — standard and high-Vt
PMOS in, low-Vt and 5 V PMOS out (our comparison).[^pdk-06][^mask-renders]
The note's wording, "(LV nwell = nwell NOT hvi) NOT lvtn, plus hvtp only
where nwell overlaps a varactor", matches the two enclosure checks of the
Error Messages page, which the expression implements only in part (it
has no varactor term).[^pdk-errors][^mask-renders] Since the site names
no source, the agreement may only mean that both start from the same
public PDK pages; neither source says what the implants
through the openings do, and neither settles which reading matches the
plate. The {ref}`masks index <masks-renders>` also records that the
site's `NCM` render, an expression that includes this one, has the same
die-by-die counts as `HVTPM` on every run.

All 40 rendered dies of every run carry shapes, but that is not 40
designs with high-Vt devices: every die carries at least 1 583 shapes,
the minimum on each run lies between 1 583 (MPW-7 and MPW-8) and 2 200
(MPW-1), and on each run 5 to 20 of the 40 dies carry a count that
another die of the run shares — 2 046 on eight dies of MPW-3 and 1 982
on nine dies of MPW-8.[^mask-renders] We read the repeated counts as
shapes common to the dies rather than to the projects (inference); since
the expression renders most low-voltage N-well, the counts follow N-well
use rather than `hvtp`. The site states the limits of its images: "These
are renders of *drawn* data, not photomask artwork: reticle pitch, 4x
reduction, mirroring and the frame features the fab adds are not
modelled."[^mask-renders] Its metadata carries no plate ID, so a render
is tied to a plate in the process-steps sheet only by the acronym
`HVTPM`, and the MPW-4 renders come from a different reticle set from
the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `HVTPM`
plate as existing on all eight MPW runs, with the plate number `317` on
each and no "Info" note.[^steps-sheet] The plate IDs below are the
sheet's; the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA317A` |
| MPW-2 | `5CS8007AC` | `S8007AA317A` |
| MPW-3 | `5CS8008AC` | `S8008AA317A` |
| MPW-4 | `5CS8018AC` | `S8018AA317A` |
| MPW-5 | `5CS8011AC` | `S8011AA317A` |
| MPW-6 | `5CS8014AC` | `S8014AA317A` |
| MPW-7 | `5CS8016AC` | `S8016AA317A` |
| MPW-8 | `5CS8017AC` | `S8017AA317A` |

* **Plate number.** `317` is higher than the numbers of masks many steps
  later in the flow — `P1M` (step 61) is `210` and `NSDM` (step 85)
  `250` — and it is one of the examples the masks index gives of plate
  numbers that do not follow process order; the sheet does not say what
  they encode, so no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `HVTPM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]
* **No HVTRM plate.** The sheet records no plate for the marked `HVTRM`
  entry on any of MPW-1 to MPW-8 ({ref}`masks-mpw-runs`).[^steps-sheet]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`, whose plates no public
  source lists ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`HVTPM <step-022>` page puts the 0.38 µm
width and space at {math}`k_1 \approx 0.62` on an i-line lens of NA 0.6
and infers an i-line level; the
{ref}`i-line stepper <machine-i-line-stepper>` page lists it there.
SkyWater lists "ASML I-line stepper" and "ASML I-line scanner" among its
tools but assigns no layer to them.[^skw-01] At the NA 0.48 low end of
ASML's PAS 5500/275D[^asml-pas5500-275d] the same feature has
{math}`k_1 \approx 0.50` (our arithmetic).

**Mask errors.** Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns";[^wong-1998]
at 365 nm that threshold is about 0.38 µm at NA 0.48 and 0.30 µm at
NA 0.60 (our arithmetic), so the smallest features lie at or just above
it and a plate CD error would print at about its own size (inference).

**Resist.** Nothing is etched through this resist; it only has to stop
the two channel implants wherever the plate leaves it. The step page
reads a conventional positive resist of roughly 1 µm, citing the PDK's
generic "Photoresist thickness" of 1.14 µm, as ample for keV channel
implants;[^pdk-03] the ion range in resist that sets the margin is what
SRIM computes.[^ziegler-2010] Ross et al. stabilised i-line implant
resists with a flood electron beam, reducing shrinkage and CD variation
and eliminating popping.[^ross-1996] The {ref}`PCHIS <step-025>` page
notes that a BF₂ implant leaves fluorine in the resist crust. SkyWater's
resist and any hardening are not public; the consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Resist edges.** Ions scattered out of an implant resist edge alter
the threshold of nearby transistors, with shifts "of up to 100 mV …
over a lateral distance on the order of a micrometer" in Hook et al.'s
work on well implants;[^hook-2003] Sheu et al. model the effect and
Drennan, Kniffin and Locascio set out its consequences for analogue
layout.[^sheu-2006][^drennan-2006] The PDK does not say whether the
0.180 µm rules hvtp.3 and hvtp.4 allow for it; we read them as placement
margins against the active and gate patterns (inference).

**Pattern transfer.** On the step pages' readings the pattern is
transferred into the N-well surface as dopant by
{ref}`PCHI <step-023>` and {ref}`PNCHI <step-024>` on the
{ref}`medium-current implanter <machine-medium-current-implanter>`
class, and the resist is removed at {ref}`PCHIS <step-025>` on the
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` and
{ref}`wet bench <machine-wet-bench>` classes. The species, energies and
doses are not public; an AMD multi-threshold patent gives a laterally
doped channel implant, made after gate formation with the gate pillars
as a self-aligned mask, of "approximately 10-20 KeV for boron or 45-90
KeV for BF₂ at a concentration of about 1.0 to 2.5×10¹³
ions/cm²"[^pat-vt-amd] — a different placement from the pre-gate
implants read here.

**Overlay.** The {ref}`HVTPM <step-022>` page reads the mask as aligned
to the trench pattern and names the 0.180 µm enclosure of a PMOS by
`hvtp` (hvtp.3) and spacing from other PMOS (hvtp.4) as its overlay
budget against the active pattern.[^pdk-periph] ASML specifies "≤ 40 nm"
single-machine overlay for the /275D stepper[^asml-pas5500-275d] (our
comparison; how SkyWater budgets the margin is not public).

(mask-hvtpm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `HVTPM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`HVTPM <step-022>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`PCHIS <step-025>`

* {ref}`HVTPM <step-022>` — coats, exposes and develops the resist.
* {ref}`PCHI <step-023>` — the first P-channel implant through the
  resist windows.
* {ref}`PNCHI <step-024>` — the second implant through the same resist,
  BF₂ on its page's reading.
* {ref}`PCHIS <step-025>` — strips the implanted resist and cleans the
  wafer.

The next step, {ref}`PWBM <step-026>`, is itself the next mask step: on
its step page's reading it coats the thick P-well block resist on the
cleaned surface. No step between `PCHIS` and it uses the `HVTPM` resist,
and there is no exception to the rule for this mask.

## Design rules and critical dimensions

The `hvtp` rules of the periphery rules, with the `lvtn`, varactor and
`hvtr` rules that refer to the layer; flag P means "Rule applies to
periphery only (outside areaid.ce). A corresponding core rule may or may
not exist.".[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| hvtp.1 | "Min width of hvtp" | 0.380 µm |
| hvtp.2 | "Min spacing between hvtp to hvtp" | 0.380 µm |
| hvtp.3 | "Min enclosure of pfet by hvtp" (P) | 0.180 µm |
| hvtp.4 | "Min spacing between pfet and hvtp" (P) | 0.180 µm |
| hvtp.5 | "Min area of hvtp" | 0.265 µm² |
| hvtp.6 | "Min area of hvtp Holes" | 0.265 µm² |
| lvtn.9 | "Min spacing, no overlap, between lvtn and hvtp" | 0.380 µm |
| varac.3 | "Min spacing between hvtp to Var_channel" | 0.180 µm |
| varac.8 | "Min enclosure of Var_channel by hvtp" | 0.255 µm |
| hvtr.2 | "Min spacing between hvtp to hvtr" | 0.380 µm |

Table 2 of *Criteria & Assumptions* repeats the width and space as
`HVTPMCD` 0.38 and `HVTPMCDSP` 0.38;[^pdk-03] no other criterion of
*Criteria & Assumptions* names `hvtp` or the mask. For a plate opened
over `hvtp`, hvtp.1, hvtp.2 and the area rules set the smallest
features; for a plate that covers low-voltage N-well, as the `chvtpm`
checks describe, the smallest features would also follow the `nwell`,
`hvi` and `lvtn` rules (our reading). The Error Messages page gives the
created layer the same 0.38 width and spacing (`chvtpm.1`,
`chvtpm.2a`).[^pdk-errors]

## Related pages

* {ref}`HVTPM <step-022>`, {ref}`PCHI <step-023>`,
  {ref}`PNCHI <step-024>` and {ref}`PCHIS <step-025>` — the mask step,
  the two implants and the strip.
* {ref}`mask-lvtnm` — the other threshold mask of the module, which the
  high-Vt PMOS rows of Table F2b pair with this one.
* {ref}`mask-nwm` — the N-well mask, whose resist carries the baseline
  PMOS threshold implant.
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

* SkyWater PDK, *Masks* page and `masks.csv` — "High Vt PCh\*, HVTPM, X"
  and "HLow VT PCh Radio\*, HVTRM, X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `hvtp`, the
  `chvtpm` purposes, `hvtr`, the Table C3 definitions and the `HVTPM`
  column of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `HVTPMCD`/`HVTPMCDSP` and the
  photoresist thickness.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `hvtp` rules and function line,
  lvtn.9, varac.3, varac.8, hvtr.2, x.9, x.15a and the flag
  legend.[^pdk-periph]
* SkyWater PDK, *Error Messages* page and `errors.csv` — the `chvtpm`
  checks on `CLHVTPM`, `hvtp.c1` and the "nikon cross"
  checks.[^pdk-errors]
* SkyWater PDK, *Device Details* — the high-Vt PMOS and the high-Vt
  varactor option.[^pdk-07]
* *S8 / SKY130 Process Steps* sheet — the step, the `HVTPM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `HVTPM` expression, note and
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

* Kao and Chandrakasan, *IEEE JSSC* 2000 — dual-threshold techniques
  for low stand-by power at high performance.[^kao-2000]
* Mutoh et al., *IEEE JSSC* 1995 — low- and high-threshold transistors
  in one LSI.[^mutoh-1995]
* Wei et al., DAC 1998 — the circuit-level case for a second threshold
  voltage.[^wei-1998]
* Kizilyalli et al., *IEEE EDL* 1995 — the threshold and gate-length
  trade-off of n+-poly buried-channel PMOS.[^kizilyalli-1995]
* Andreani and Mattisson, *IEEE JSSC* 2000 — inversion- and
  accumulation-mode MOS varactors.[^andreani-2000]
* Krivokapic and Milic (AMD), US 6,238,982 — multiple thresholds set by
  gate length, with a laterally doped channel implant self-aligned to
  the gate pillars.[^pat-vt-amd]
* Helm and Zhou (Round Rock Research), US 2011/0006372 — masked
  Vt-adjust implants for standard and low-Vt devices.[^pat-vt-rrr]
* Taur and Ning, *Fundamentals of Modern VLSI Devices* — threshold
  voltage against channel doping.[^taur-2009]
* Hook et al., *IEEE TED* 2003 — ions scattered from the resist edge and
  the threshold shifts they cause.[^hook-2003]
* Sheu et al., *IEEE TED* 2006 — a compact model of the well-edge
  proximity effect.[^sheu-2006]
* Drennan, Kniffin and Locascio, CICC 2006 — proximity effects and
  analogue layout.[^drennan-2006]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  size below which it rises.[^wong-1998]
* Ross et al., *Proc. SPIE* 1996 — electron-beam stabilisation of i-line
  implant resists.[^ross-1996]
* Ziegler, Ziegler and Biersack, *NIM B* 2010 — SRIM, for the ion range
  in resist.[^ziegler-2010]

## Open questions

* Whether the plate is opened over drawn `hvtp`, as the step page reads
  it, or over low-voltage N-well outside the low-Vt devices, as Table
  F2b's rows, the `chvtpm` checks and the renders' expression suggest,
  is not stated in the PDK;[^pdk-06][^pdk-errors][^mask-renders] the
  Error Messages page does not define `CLHVTPM`, and the renders' note
  contradicts its own expression and names no source for its "fab
  algorithm".
* The operation that makes the `chvtpm` plate data, and what its add,
  drop and drawing purposes contribute, are not published; the
  Error Messages page gives only what the created layer must
  cover.[^pdk-06][^pdk-errors]
* How `PCHI` and `PNCHI` divide the threshold shift, and their species,
  energies and doses, are not public.
* Whether the marked `HVTRM` mask is absent from the baseline flow or
  folded into this one is not stated; the sheet records no `HVTRM`
  plate.[^pdk-05][^steps-sheet]
* The plate's tone, blank, absorber and magnification, the resist and
  the exposure tool are not public; the i-line reading rests on the
  0.380 µm rules.
* What the plate number `317` encodes is not stated, and no public
  source lists the `HVTPM` plate of the original MPW-4 set
  `5CS8010AC`.[^steps-sheet][^mask-renders]

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tabs "Sheet1" (step number, code and description), "Masks"
    (mask steps with step numbers), "Run Mask IDs" (the mask table set
    against MPW-1 to MPW-8, with "Exists" and "Plate ID" columns per run)
    and "Sheet4" (mask types), retrieved 2026-09-13.
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
    directory: `README.md` and, for each run, the `mpw-00N_HVTPM/`
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
[^kao-2000]: J. T. Kao and A. P. Chandrakasan, "Dual-threshold voltage
    techniques for low-power digital circuits", *IEEE Journal of
    Solid-State Circuits* **35**(7), 1009–1018 (2000).
    <https://doi.org/10.1109/4.848210>
[^mutoh-1995]: S. Mutoh, T. Douseki, Y. Matsuya, T. Aoki, S. Shigematsu
    and J. Yamada, "1-V power supply high-speed digital circuit
    technology with multithreshold-voltage CMOS", *IEEE Journal of
    Solid-State Circuits* **30**(8), 847–854 (1995).
    <https://doi.org/10.1109/4.400426>
[^wei-1998]: L. Wei, Z. Chen, M. Johnson, K. Roy and V. De, "Design and
    optimization of low voltage high performance dual threshold CMOS
    circuits", *Proceedings of the 35th Design Automation Conference*,
    pp. 489–494 (1998). <https://doi.org/10.1109/DAC.1998.724521>
[^kizilyalli-1995]: I. C. Kizilyalli, M. M. Rambaud, A. Duncan,
    S. A. Lytle and M. J. Thoma, "Threshold voltage-minimum gate length
    trade-off in buried channel PMOS devices for scaled supply voltage
    CMOS technologies", *IEEE Electron Device Letters* **16**(10),
    457–459 (1995). <https://doi.org/10.1109/55.464816>
[^andreani-2000]: P. Andreani and S. Mattisson, "On the use of MOS
    varactors in RF VCOs", *IEEE Journal of Solid-State Circuits*
    **35**(6), 905–910 (2000). <https://doi.org/10.1109/4.845194>
[^pat-vt-amd]: Z. Krivokapic and O. Milic (Advanced Micro Devices),
    *Multiple threshold voltage semiconductor device fabrication
    technology*, US 6,238,982 B1, granted 2001-05-29.
    <https://patents.google.com/patent/US6238982B1/en>
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
