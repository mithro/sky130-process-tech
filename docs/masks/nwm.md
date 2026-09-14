(mask-nwm)=
# NWM — N-Well\*

The N-well mask is the {term}`reticle` that decides where SKY130's
silicon is N-type: on the {ref}`NWM <step-017>` page's reading, the thick
resist printed through it at step 17 is opened over every future N-well —
the body of every PMOS, the ring that closes each deep-N-well tub, the
drift regions of the drain-extended NMOS — and three implants pass
through the same openings, the MeV well pair {ref}`NWI <step-018>` and
{ref}`NWI2 <step-019>` and the P-channel threshold implant
{ref}`LVTPI <step-020>`, before the strip at {ref}`LVTPIS <step-021>`.
It is an implant {term}`block mask`, and its drawn layer is also the one
the PDK's layout definitions use to tell PMOS from NMOS. This
page gathers what public sources say about the mask itself — its PDK
entry and layers, the plates the process-steps sheet records for the MPW
runs, what the public renders of those runs show, the lithography it
needs and the rules that constrain it. How the step is performed is on
the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | NWM — N-Well\* |
|---|---|
| Mask step | {ref}`NWM <step-017>`, step 17 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "N-Well\*", `NWM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cnwm` mask 21:0, "Nwell mask"[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `nwell` drawing 64:20, "N-well region"[^pdk-06] |
| Minimum CD, feature / space | `NWMCD` 0.84 / `NWMCDSP` 1.27[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist is opened where `nwell` is drawn, which with a positive resist would make the plate clear over `nwell` and opaque elsewhere (inference). |
| Exposure class | i-line, an inference on the step page from the 0.84 µm width and the thick implant resist; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `010`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 5 steps; see {ref}`Steps that use this mask <mask-nwm-steps>` |

## What the mask defines

The periphery rules give the function of the layer as "Define nwell
implant regions".[^pdk-periph] The {ref}`NWM <step-017>` page lists what
those regions are for, from the PDK: the body of every PMOS and varactor;
the side wall of the deep-N-well tub, since rule nwell.5 requires "Deep
nwell must be enclosed by nwell"; the drain extension of the
high-voltage NMOS, which the PDK's high-voltage methodology says is
"fabricated by lightly doped Nwells" and P-wells; and the base of the
PNP and the collector contact of the NPN.[^pdk-periph][^pdk-hv][^pdk-07]
A Texas Instruments patent describes the same use of "the n-well region
… as the lightly doped drain extension region".[^pat-demos-ti]

The drawn layer is also what the PDK's device extraction reads. Table
C3 of the *Layers Reference* defines `pfet` as "Gate AND nwell" and
`nfet` as "Gate NOT nwell", `P+_diff` as "Diff AND Nwell" and `N+_diff`
as "Diff NOT Nwell", `pwell` as "NOT nwell (default substrate area)",
`iso_pwell` as "(NOT nwell) AND dnwell" and `LVnwell` as "nwell NOT
hvi".[^pdk-06] There is no drawn P-well: in the layout, everything
outside `nwell` is P-well by definition, which is why the
{ref}`PWBM <step-026>` page pairs the P-well block mask with `nwell`
(the masks index marks that pairing as an inference).

The PDK's mask generation table, Table F2b, marks the `NWM` column `C`
("CREATED") in 34 of its 80 device rows: the three p-diffusion
resistors, the seven 1.8 V PMOS rows (standard, low-Vt, high-Vt and
core), the three varactors, the 5/10.5 V PMOS, the 16 V drain-extended
NMOS and PMOS, all five 20 V drain-extended rows, ten diode rows, both
bipolar transistors and the HV PMOS ESD transistor.[^pdk-06] It marks
`-` in the 1.8 V and 5/10.5 V NMOS rows, and `C` in the 16 V and 20 V
drain-extended NMOS rows,[^pdk-06] which fits the drain-extension use
the step page describes (our reading of the table). Rung, Dell'Oca and
Walker introduced the retrograde well — a deep implant with a brief
anneal, which allowed a much shallower well and closer n- and p-channel
spacing — in 1981,[^rung-1981] and Martin and Chen optimised a
high-energy implanted N-well for 1 µm CMOS.[^martin-1986]

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` has one mask-level layer for this mask, `cnwm` with
purpose `mask` at 21:0 ("Nwell mask"), and no `drawing`, `mask add`,
`mask drop` or `waffle drop` purpose; the drawn layer is `nwell` at
64:20, "N-well region".[^pdk-06] The PDK publishes no operation from
`nwell` to the plate, and rule x.15a confines mask layers to test
modules, seal ring and frame, with an exception that names only
"FOM/P1M/Metal waffle drop" (flag P),[^pdk-periph] so a design inside
the die draws `nwell` (our reading of x.15a).

Several published criteria say that the plate is not the drawn layer
unchanged, without giving the whole operation. Table 7 of *Criteria &
Assumptions* gives a "Serif added to nwell convex corner (SXX-572, 573)"
of 0.22 (`NwellCvxSerif`), a "Serif added to nwell concave corner
(SXX-572, 573)" of 0.12 (`NwellCveSerif`) and an "NWM extension beyond
nwell edge straddling de_nFet_source (for GSMC; QZM-133)" of 0.075
(`NvhvNwellExt`).[^pdk-03] Table C3 defines `nwell_all` as "nwell OR
extension of cnwm beyond nwell edge straddling de_nFet_source by
cnwm.3f (45 degree edges are retained for the NVHV device nwell); Rule
cnwm.3f applies only to GSMC flows", and its `nwellDnwellHoles` and
`photoArray` definitions say that the "Die+frame utility will use the
mask data of nwell and dnwell".[^pdk-06] So the PDK names a rule
`cnwm.3f` and speaks of "mask data of nwell", but the periphery rules
contain no `cnwm` rule set,[^pdk-periph] and the serif and extension
rows name other flows and references that the PDK does not explain. We
read the serifs as corner corrections added to the drawn outline and
the extension as flow-specific (inference from the row wording).

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `NWM` the site renders layer 64:20 alone, with
no Boolean expression and no fill layer, on all eight runs; its mask
record gives the mask-level layer 21:0 and the note "NWM = nwell sized
(cnwm.3a outside hvi / 3b inside), with DEPMOS/pwell-resistor
exemptions".[^mask-renders] The periphery rules have no `cnwm.3a` or
`cnwm.3b`, the only `cnwm` rule the PDK names being Table C3's
`cnwm.3f`,[^pdk-periph][^pdk-06] and the site gives no source for the
note. The render job lists only the drawn layer, with no sizing step,
so, as the {ref}`masks index <masks-renders>` reads the site in general,
the images are unsized drawn data. The note and the choice of layer are
one public derivation from the drawn data, not SkyWater's
mask-generation recipe.

All 40 rendered dies of every run carry `nwell` shapes, but that says
nothing about how many designs use PMOS in particular: every die carries
at least 352 206 shapes, the minimum on each run lies between 352 206
(MPW-5) and 463 378 (MPW-8), and on MPW-1 one die accounts for 99 % of
the run's shapes.[^mask-renders] Counts rarely repeat — on no run do
more than nine dies have a count that another die shares — so we read
the large minimum as `nwell` shapes that every die of these runs
carries, such as those of shared circuitry, rather than as project
content (inference; the site does not say what they are). The site
states the limits of its images: "These are renders of *drawn* data,
not photomask artwork: reticle pitch, 4x reduction, mirroring and the
frame features the fab adds are not modelled."[^mask-renders] Its
metadata carries no plate ID, so a render is tied to a plate in the
process-steps sheet only by the acronym `NWM`, and the MPW-4 renders
come from a different reticle set from the one whose plates the sheet
records ({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `NWM` plate
as existing on all eight MPW runs, with the plate number `010` on each
and no "Info" note.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA010A` |
| MPW-2 | `5CS8007AC` | `S8007AA010A` |
| MPW-3 | `5CS8008AC` | `S8008AA010A` |
| MPW-4 | `5CS8018AC` | `S8018AA010A` |
| MPW-5 | `5CS8011AC` | `S8011AA010A` |
| MPW-6 | `5CS8014AC` | `S8014AA010A` |
| MPW-7 | `5CS8016AC` | `S8016AA010A` |
| MPW-8 | `5CS8017AC` | `S8017AA010A` |

* **Plate number.** `010` is the second-lowest plate number in the tab,
  after `NSM` (`007`), and lower than `FOM` (`020`) and `DNM` (`150`),
  which precede this mask in the flow; the sheet does not say what the
  numbers encode, so no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `NWM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`, whose plates no public
  source lists ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`NWM <step-017>` page puts the 0.84 µm
minimum width at {math}`k_1 \approx 1.4` on an i-line lens of NA 0.6,
notes that chemically amplified DUV resists are seldom made as thick as
this level needs, and infers an i-line level; the
{ref}`i-line stepper <machine-i-line-stepper>` page lists it there.
SkyWater lists "ASML I-line stepper" and "ASML I-line scanner" among its
tools but assigns no layer to them.[^skw-01] At the NA 0.48 low end of
ASML's PAS 5500/275D[^asml-pas5500-275d] the same width has
{math}`k_1 = 0.84 \times 0.48 / 0.365 \approx 1.1` (our arithmetic).

**Mask errors.** Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns";[^wong-1998]
at 365 nm and NA 0.48 that threshold is about 0.38 µm (our arithmetic),
under half the `NWM` minimum, so a CD error on the plate would be
expected to print at its own size (inference). The demands of this mask
fall on its resist and its placement.

**Resist.** The resist must stop the MeV well implants wherever the
plate leaves it. The {ref}`NWM <step-017>` page reads a 2–3 µm-class
thick i-line resist, from published examples: an IBM patent uses a
photoresist "typically 1800–2500 nm in thickness" for phosphorus
implants up to 850 keV,[^pat-well-ibm] and a Zilog patent needs
"minimum thicknesses of 3.4 µm" for a 1.3–1.5 MeV phosphorus
N-well.[^pat-resist-zilog] The ion range in resist that sets the
thickness is what SRIM computes.[^ziegler-2010] Thick resist under MeV
ions outgasses — Lee et al. measured the effect and the dose shift it
causes[^lee-1996] — and Ross et al. stabilised i-line implant resists
with a flood electron beam, reducing shrinkage and CD variation and
eliminating popping.[^ross-1996] Tsukamoto et al. review high-energy
implantation for ULSI, including masking.[^tsukamoto-1991] SkyWater's
resist, its thickness and any hardening are not public; the PDK's
generic "Photoresist thickness" is 1.14 µm,[^pdk-03] which the step page
does not take as this level's resist. The consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Resist edges.** A thick implant resist also scatters ions: "Some of
the ions scattered out of the edge of the photoresist are implanted in
the silicon surface near the mask edge, altering the threshold voltage
of those devices", with shifts "of up to 100 mV … over a lateral
distance on the order of a micrometer".[^hook-2003] Sheu et al. model
this well-edge proximity effect.[^sheu-2006] The
{ref}`NWM <step-017>` page reads rules such as lvtn.10, the 0.380 µm
enclosure of `lvtn` by `nwell`, as the kind of layout guard that
follows;[^pdk-periph] the PDK does not state the purpose of any `nwell`
spacing.

**Pattern transfer.** Nothing is etched through this resist. On the step
pages' readings the pattern is transferred into the silicon as dopant by
the {ref}`NWI <step-018>` and {ref}`NWI2 <step-019>` implants on the
{ref}`high-energy implanter <machine-high-energy-implanter>` class and
by {ref}`LVTPI <step-020>` on the
{ref}`medium-current implanter <machine-medium-current-implanter>`
class, and the resist is removed at {ref}`LVTPIS <step-021>`, which that
page calls the hardest strip of the module, on the
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` and
{ref}`wet bench <machine-wet-bench>` classes. The PDK gives the result
rather than the conditions: an "n-well peak concentration" of
6.00E+017 cm⁻³ over a "background concentration" of 8.00E+14 cm⁻³, a
baseline N-well vertical dimension of 1.1 µm and a "min n-well width to
guarantee 90 % peak concentr." of 0.55 µm (Tables 3a and 3b).[^pdk-03]
Morris and Rubin set out the technical and economic case for retrograde
wells and channel implants of this kind.[^morris-2000]

**Overlay.** The {ref}`NWM <step-017>` page reads the mask as aligned to
the trench pattern of {ref}`FOM <step-004>`, and points to Table 3b's
"N-w/P-w junction (from drawn edge)" of 0.034 µm and Table 3e's
"Minimum n+ or p+ - nwell spacing to prevent latch-up" of 0.23 µm as
showing how tightly the well edge is budgeted.[^pdk-03] The placement
rules against active are 0.180 µm of `nwell` around p+ diffusion
(difftap.8) and n+ tap (difftap.10) and 0.340 µm from n+ diffusion
(difftap.9),[^pdk-periph] against the "≤ 40 nm" single-machine overlay
ASML specifies for the /275D stepper[^asml-pas5500-275d] (our
comparison; the rules must also absorb the lateral spread of the MeV
implants, which is not published). Rubin, Morris and Jasper describe
how retrograde-well implant control sets the narrow n+/p+
isolation.[^rubin-2002]

(mask-nwm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `NWM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`NWM <step-017>`, {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`, {ref}`LVTPI <step-020>`, {ref}`LVTPIS <step-021>`

* {ref}`NWM <step-017>` — coats, exposes and develops the thick resist.
* {ref}`NWI <step-018>` — the high-energy N-type well implant through
  the resist windows.
* {ref}`NWI2 <step-019>` — the second N-well implant, a second energy on
  its page's reading, through the same resist.
* {ref}`LVTPI <step-020>` — the low-energy P-channel threshold implant,
  which on the step pages' reading also goes through the N-well resist.
* {ref}`LVTPIS <step-021>` — strips the resist after all three implants
  and cleans the wafer.

The next step, {ref}`HVTPM <step-022>`, is itself the next mask step:
on its step page's reading it coats a new resist for the high-Vt PMOS
implants on the cleaned surface. The one point that needs stating is
{ref}`LVTPI <step-020>`: it is a channel implant rather than a well
implant, and the step list names the strip after it, but the step pages
read it as using the `NWM` resist — the arrangement of an IBM
retrograde-well patent cited there[^pat-well-ibm] — and no public
document says so. On that reading the rule needs no exception for this
mask.

## Design rules and critical dimensions

The `nwell` rules of the periphery rules, with the diffusion and
high-voltage rules that place other layers against it; flag TC means
"Rule not checked for cell name “\*_tech_CD_top\*”", P "Rule applies to
periphery only (outside areaid.ce). A corresponding core rule may or may
not exist.", NE "Rule not checked for esd_nwell_tap. There are no
corresponding rule for esd_nwell_tap." and DE "Rule not checked for
source of Drain Extended device".[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| nwell.1 | "Width of nwell" | 0.840 µm |
| nwell.2a | "Spacing between two n-wells" | 1.270 µm |
| nwell.2b | "Manual merge wells if less than minimum" | — |
| nwell.4 | "All n-wells will contain metal-contacted tap  (rule checks only for licon on tap) […]" | — |
| nwell.5 | "Deep nwell must be enclosed by nwell by atleast... […]" (TC) | 0.400 µm |
| nwell.5a | "min enclosure of nwell by dnwell inside UHVI" | N/A |
| nwell.5b | "nwell inside UHVI must not be on the same net as nwell outside UHVI" | N/A |
| nwell.6 | "Min enclosure of nwell hole by deep nwell outside UHVI" (TC) | 1.030 µm |
| nwell.7 | "Min spacing between nwell and deep nwell on separate nets […]" (TC) | 4.500 µm |
| difftap.8 | "Enclosure of (p+) diffusion by N-well. Rule exempted inside UHVI." (DE NE P) | 0.180 µm |
| difftap.9 | "Spacing of (n+) diffusion to N-well outside UHVI" (DE NE P) | 0.340 µm |
| difftap.10 | "Enclosure of (n+)  tap by N-well. Rule exempted inside UHVI." (NE P) | 0.180 µm |
| difftap.11 | "Spacing of (p+) tap to  N-well. Rule exempted inside UHVI." | 0.130 µm |
| lvtn.10 | "Min enclosure of lvtn by (nwell not overlapping Var_channel) (exclude coincident edges)" | 0.380 µm |
| hvi.5 | "Min space between hvi and nwell (exclude coincident edges)" | 0.700 µm |
| hvnwell.8 | "Min space between HV_nwell  and any nwell on different nets" | 2.000 µm |
| hv.nwell.1 | "Min spacing of nwell tagged with text "shv_nwell" to any nwell on different nets" | 2.500 µm |
| denmos.12 | "Min spacing between nwells overlapping de_nFET_drain" | 2.400 µm |

Table 2 of *Criteria & Assumptions* repeats the width and space as
`NWMCD` 0.84 and `NWMCDSP` 1.27; Table 3d gives a punch-through spacing
for "n-well - n-well" of 0.835 µm (`NWPTS`), below the 1.270 µm of
nwell.2a; Table 3e gives a "Min n-well enclos. of tap to ensure bkdwn
N-w/P-w before N+/P-w (ESD)" of 0.04 µm (`XNWESD`); Table 7 gives an
"Enclosure of tap by nwell for pwell res" of 0.22 (`PTAP_NWL_SP`); and
Table 8 a "Min HVNwell to any nwell space" of 2 (`HVNwell_Nwell_SP`),
the value of hvnwell.8.[^pdk-03][^pdk-periph] The SKY130
{term}`test tile`'s pad documentation has a "High Voltage Nwell to Nwell
Isolation" module whose spacings are 2.00, 2.50, 1.50, 1.27 and
1.00 µm:[^raw-data-testtile-pads] the 1.27 µm of nwell.2a, the 2.00 µm
and 2.50 µm of the two high-voltage spacings, and two values between or
below them (our comparison). For the plate, nwell.1 and
nwell.2a set the smallest features: a 0.84 µm line on a 1.27 µm space.

## Related pages

* {ref}`NWM <step-017>`, {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`,
  {ref}`LVTPI <step-020>` and {ref}`LVTPIS <step-021>` — the mask step,
  the three implants and the strip.
* {ref}`mask-dnm` — the deep N-well mask whose tubs the N-well ring
  closes.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the tables this page's plate facts are taken from.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-high-energy-implanter` and
  {ref}`machine-medium-current-implanter` — the implant classes that use
  the pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography` and {ref}`category-implant` — the mask
  step and implant categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "N-Well\*, NWM,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `nwell`,
  `cnwm`, the Table C3 definitions and the `NWM` column of Table
  F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `NWMCD`/`NWMCDSP`, the N-well
  profile, junction, punch-through and latch-up criteria, the serif and
  extension rows and the photoresist thickness.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `nwell` rules, the diffusion and
  high-voltage rules against N-well, x.15a and the flag
  legend.[^pdk-periph]
* SkyWater PDK, *Device Details* and *High Voltage Methodology* — the
  devices built in N-well and the drain extensions made of
  it.[^pdk-07][^pdk-hv]
* SkyWater PDK Authors, test-tile pad documentation — the N-well
  isolation spacings.[^raw-data-testtile-pads]
* *S8 / SKY130 Process Steps* sheet — the step, the `NWM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `NWM` renders, their layer
  and note, and the per-die shape counts.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the i-line exposure
  tools.[^skw-01]
* ASML, *PAS 5500/275D* data sheet — NA range and single-machine
  overlay of an i-line stepper.[^asml-pas5500-275d]

### High-level understanding

* Wikipedia, *CMOS* — NMOS on the p-substrate, PMOS in an
  N-well.[^wiki-cmos]
* Wikipedia, *Latch-up* — the parasitic path through the
  wells.[^wiki-latchup]
* Wikipedia, *Ion implantation* — masking, range and
  energy.[^wiki-implant]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  implant masking by resist.[^txt-02]
* Levinson, *Principles of Lithography* — chapters on photoresists,
  masks and reticles, and overlay.[^levinson-2005]

### Deep dive

* Rung, Dell'Oca and Walker, *IEEE TED* 1981 — the retrograde well made
  by a deep implant and a brief anneal.[^rung-1981]
* Martin and Chen, *IEEE JSSC* 1986 — optimising a high-energy
  implanted N-well for 1 µm CMOS.[^martin-1986]
* Stolmeijer, *IEEE TED* 1986 — a twin-well CMOS process built with
  high-energy implants.[^stolmeijer-1986]
* Breitwisch, Lam and Slinkman (IBM), US 6,667,205 — retrograde N- and
  P-wells with the resist thickness and implant energies.[^pat-well-ibm]
* Buffat and Adams (Zilog), US 6,576,405 — resist thickness for MeV well
  implants.[^pat-resist-zilog]
* Mitros (Texas Instruments), US 6,660,603 — the N-well as a drain
  extension.[^pat-demos-ti]
* Hook et al., *IEEE TED* 2003 — ions scattered from the resist edge and
  the threshold shifts they cause.[^hook-2003]
* Sheu et al., *IEEE TED* 2006 — a compact model of the well-edge
  proximity effect.[^sheu-2006]
* Lee et al., IIT 1996 — thick-resist outgassing during MeV
  implantation.[^lee-1996]
* Ross et al., *Proc. SPIE* 1996 — electron-beam stabilisation of i-line
  implant resists.[^ross-1996]
* Morris and Rubin, IIT 2000 — technical and economic considerations for
  retrograde well and channel implants.[^morris-2000]
* Rubin, Morris and Jasper, IIT 2002 — retrograde-well implant control
  and narrow n+/p+ isolation.[^rubin-2002]
* Tsukamoto et al., *NIM B* 1991 — a review of high-energy implantation
  for ULSI.[^tsukamoto-1991]
* Ziegler, Ziegler and Biersack, *NIM B* 2010 — SRIM, for the ion range
  in resist.[^ziegler-2010]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  size below which it rises.[^wong-1998]

## Open questions

* The operation that makes the `cnwm` plate data from `nwell` is not
  published. Table 7's serif and extension rows and Table C3's
  `cnwm.3f` show that it is not a copy,[^pdk-03][^pdk-06] and the renders
  site's note names `cnwm.3a` and `cnwm.3b` rules that the periphery
  rules do not contain.[^pdk-periph][^mask-renders]
* That `NWI`, `NWI2` and `LVTPI` share this resist is the step pages'
  reading; no public document says so.
* The plate's tone, blank, absorber and magnification, the resist and
  its thickness, and the exposure tool are not public; the i-line
  reading rests on the 0.84 µm rule and the implant energies the step
  pages infer.
* Table 3d's 0.835 µm N-well punch-through spacing and rule nwell.2a's
  1.270 µm are not reconciled in the PDK.[^pdk-03][^pdk-periph]
* The renders do not say what the `nwell` shapes common to the dies of
  a run are.[^mask-renders]
* What the plate number `010` encodes is not stated, and no public
  source lists the `NWM` plate of the original MPW-4 set
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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 3a,
    3b, 3d, 3e, 7 and 8), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_NWM/`
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
[^wiki-cmos]: Wikipedia, *CMOS*. <https://en.wikipedia.org/wiki/CMOS>
[^wiki-latchup]: Wikipedia, *Latch-up*.
    <https://en.wikipedia.org/wiki/Latch-up>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^rung-1981]: R. D. Rung, C. J. Dell'Oca and L. G. Walker, "A
    retrograde p-well for higher density CMOS", *IEEE Transactions on
    Electron Devices* **28**(10), 1115–1119 (1981).
    <https://doi.org/10.1109/T-ED.1981.20498>
[^martin-1986]: R. A. Martin and J. Y.-T. Chen, "Optimized retrograde
    N-well for 1-μm CMOS technology", *IEEE Journal of Solid-State
    Circuits* **21**(2), 286–292 (1986).
    <https://doi.org/10.1109/JSSC.1986.1052516>
[^stolmeijer-1986]: A. Stolmeijer, "A twin-well CMOS process employing
    high-energy ion implantation", *IEEE Transactions on Electron
    Devices* **33**(4), 450–457 (1986).
    <https://doi.org/10.1109/T-ED.1986.22511>
[^pat-well-ibm]: M. J. Breitwisch, C. H. Lam and J. A. Slinkman (IBM),
    *Method of forming retrograde n-well and p-well*, US 6,667,205 B2,
    granted 2003-12-23. <https://patents.google.com/patent/US6667205B2/en>
[^pat-resist-zilog]: S. J. Buffat and J. L. Adams (Zilog), *High aspect
    ratio photolithographic method for high energy implantation*, US
    6,576,405 B1, granted 2003-06-10.
    <https://patents.google.com/patent/US6576405B1/en>
[^pat-demos-ti]: J. C. Mitros (Texas Instruments), *Higher voltage drain
    extended MOS transistors with self-aligned channel and drain
    extensions*, US 6,660,603 B2, granted 2003-12-09.
    <https://patents.google.com/patent/US6660603B2/en>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices* **50**(9),
    1946–1951 (2003). <https://doi.org/10.1109/TED.2003.815371>
[^sheu-2006]: Y.-M. Sheu, K.-W. Su, S. Tian, S.-J. Yang, C.-C. Wang,
    M.-J. Chen and S. Liu, "Modeling the Well-Edge Proximity Effect in
    Highly Scaled MOSFETs", *IEEE Transactions on Electron Devices*
    **53**(11), 2792–2798 (2006). <https://doi.org/10.1109/TED.2006.884070>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^ross-1996]: M. F. Ross, W. R. Livesay, V. Starov, K. Ostrowski and
    S. Y. Wong, "Photoresist stabilization for ion implant processing",
    *Proc. SPIE* **2724**, 632 (1996).
    <https://doi.org/10.1117/12.241862>
[^morris-2000]: W. Morris and L. Rubin, "Technical and economic
    considerations for retrograde well and channel implants", *2000
    International Conference on Ion Implantation Technology*,
    pp. 73–76. <https://doi.org/10.1109/IIT.2000.924093>
[^rubin-2002]: L. M. Rubin, W. Morris and C. Jasper, "Process control
    issues for retrograde well implants for narrow n+/p+ isolation in
    CMOS", *2002 International Conference on Ion Implantation
    Technology*, pp. 17–20. <https://doi.org/10.1109/IIT.2002.1257927>
[^tsukamoto-1991]: K. Tsukamoto, S. Komori, T. Kuroi and Y. Akasaka,
    "High-energy ion implantation for ULSI", *Nuclear Instruments and
    Methods in Physics Research B* **59–60**, 584–591 (1991).
    <https://doi.org/10.1016/0168-583X(91)95283-J>
[^ziegler-2010]: J. F. Ziegler, M. D. Ziegler and J. P. Biersack, "SRIM
    – The stopping and range of ions in matter (2010)", *Nuclear
    Instruments and Methods in Physics Research B* **268**(11–12),
    1818–1823 (2010). <https://doi.org/10.1016/j.nimb.2010.02.091>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
