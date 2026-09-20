(step-026)=
# Step 026 — PWBM: P-well block mask

| | |
|---|---|
| **Step number** | 26 of 171[^steps-sheet] |
| **Step code** | `PWBM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | {term}`FEOL` — wells and channel implants |
| **Previous step** | {ref}`PCHIS <step-025>` |
| **Next step** | {ref}`PWI <step-027>` |

## What this step is

`PWBM` prints the *P-well {term}`block mask`*: a photoresist (thick, we infer)
is coated, exposed through the PWBM {term}`reticle` and developed so that resist
*remains* over every region that must not receive the P-well and is
removed everywhere else. The two P-well implants {ref}`PWI <step-027>`
and {ref}`PWI2 <step-028>` follow (through the same openings in the
sequence this reference describes), and the resist is stripped at
{ref}`PWIS <step-029>`. The PDK's name for the mask, "P-Well Block
Mask",[^pdk-05] says how the layer is used: this is a
*block* mask, the negative of the {ref}`NWM <step-017>` N-well mask in
spirit, and the P-well is implanted into all silicon that it does not
cover.

Three pieces of public evidence support that reading. First, the PDK has
no drawn P-well layer: `gds_layers.csv` contains `nwell` as a drawing
layer (64:20) but `pwell` only as label, pin and resistor purposes
(64:59, 122:16, 64:13 …), so a layout defines P-well implicitly as "not
N-well".[^pdk-06] Second, the drawn layer that does exist is `pwbm` (GDS
19:44), described as "Regions (in UHVI) blocked from p-well implant (DE
MOS devices only)";[^pdk-06] its rule table is headed "Function: Define
p-well block".[^pdk-periph] Third, the device that uses it is described
the same way: the 20 V zero-Vt NMOS "has p-well and all Vt implants
blocked to achieve a zero VT".[^pdk-07] We therefore infer that the
physical reticle is generated from `nwell` ∪ `pwbm` (plus any
deep-N-well-related additions), so that the P-well goes everywhere
except into N-wells and into the special 20 V regions.

The PDK's mask table lists "P-Well Block Mask, PWBM" but — unlike `NWM`,
`LVTNM` and `HVTPM` — does *not* tick it as "Used in SKY130".[^pdk-05]
The `pwbm` layer and its rules exist, and the 20 V zero-Vt NMOS
depends on the block,[^pdk-07] so this reference treats the unticked
box as a documentation inconsistency rather than as evidence that the
mask is absent (see *Open questions*).

Measured data are consistent with a zero-Vt device that has no P-well
under its channel. The SKY130 raw-data repository publishes I–V sweeps
of a {term}`test tile` structure that the pad list names `n20zvtvhv1`
("w/l=30/5.5; m=2", cell name
`s8defet_ccgx_hvn_nw_dnw_native_sti_2p0_nopw_L5p0_W60`), whose only body
connection in the pad list is `Psub`;[^raw-data-testtile-pads] the repository
files it under `nfet_20v0_nvt`, but its geometry is that of the PDK's
`nfet_20v0_zvt` e-test structure ("2\* 30/5.5") rather than the
"2\* 30/1.0" listed for `nfet_20v0_nvt`.[^pdk-07] Five instances give a
threshold of −0.12 to −0.13 V by maximum-transconductance extrapolation
at a drain bias of 0.1 V (less half that bias), against an e-test nominal of −0.1224 V, and a
body-effect coefficient of 0.070–0.072 √V from the threshold shift at
substrate biases of −2.5 V and −5 V (our extraction from the published
measurements).[^raw-data-hv-mosfets][^pdk-07] With the standard
uniform-doping expression and the thick-oxide capacitance measured on
the same tile ({ref}`GOX100 <step-043>`), that coefficient corresponds
to an effective body doping of about 1.4 × 10¹⁵ cm⁻³ — far below the
4 × 10¹⁷ cm⁻³ P-well peak and of the same order as the PDK's
8 × 10¹⁴ cm⁻³ background concentration[^pdk-03] — whereas the same
calculation gives about 1.5 × 10¹⁷ cm⁻³ for a 5 V NMOS in the standard
P-well (see {ref}`DEPI <step-038>`).[^raw-data-hv-mosfets] The value is
an average over the depleted depth and says nothing about how the block
was drawn or printed.

The `pwbm` rules (pwbm.1–pwbm.5) have no public numeric values ("N/A")
but describe the geometry: `pwbm` regions live inside the 20 V
identifier `uhvi`; "dnwell inside UHVI must be enclosed by pwbm (exempt
pwbm hole inside dnwell)" (pwbm.4); and the {term}`drain-extended <DEMOS>` implant layer
must be enclosed by `pwbm` ("Min enclosure of pwdem:dg by pwbm.dg
inside UHVI", pwdem.3 — the rule set calls the layer `pwdem`, while
`gds_layers.csv` draws it as `pwde` 124:20).[^pdk-periph][^pdk-06] In words:
inside a 20 V device the standard P-well is kept out of the deep-N-well
tub, and a custom, lighter P-well is put back by
{ref}`PWDEM <step-030>`/{ref}`PWDEI1 <step-031>` where the device needs
it.

## Step category

`PWBM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *thick-resist implant-block* kind. The resist must stop
boron at, we infer, a few hundred keV (see {ref}`PWI <step-027>`); the
pattern is the coarsest in the front end after the deep N-well; and the
layer is, we infer, aligned to the {term}`STI` pattern, as is `NWM`, so that the
two well edges meet in the isolation between NMOS and PMOS.

## Why this step exists

CMOS needs a P-type body for its NMOS: "The N device is manufactured on
a p-type substrate",[^wiki-cmos] but a 130 nm process cannot use the
lightly doped substrate (the PDK lists an 8 × 10¹⁴ cm⁻³ background
concentration among its n-well entries, without calling it the wafer
doping)[^pdk-03] as it comes
— it needs a *{term}`retrograde P-well <retrograde well>`* with a peak of 4 × 10¹⁷ cm⁻³ at 0.42 µm
depth[^pdk-03] for {term}`punch-through`, isolation and latch-up control (see
{ref}`PWI <step-027>`). That implant must be kept out of the N-wells,
where it would compensate the PMOS body, and out of the regions where
the PDK's 20 V devices want either no well (`nfet_20v0_zvt`) or a
lighter, purpose-built one (the drain-extended
devices).[^pdk-07][^pdk-hv] A block mask does both with one lithography.

The alternative used in older generations — a separately drawn P-well
mask, as in the Harris twin-well flow where "an implant blocking
photoresist layer 18" is patterned to expose the region "adjacent to
N-type well 17"[^pat-twin-harris] — needs a second, positively drawn
well layer and cannot by itself define the custom 20 V regions. A drawn
P-well mask would be equivalent to `PWBM` in effect; SKY130 simply chose
to draw the exceptions rather than the wells.

## How it is typically performed

An industry-generic P-well-block lithography for a 200 mm, 130 nm-era
fab:

1. **Track preparation.** {term}`HMDS` prime; no {term}`BARC` for a coarse layer
   (inference).[^wiki-litho]
2. **Thick resist coat.** The resist must stop the deepest P-well boron.
   IBM's retrograde-well patent implants its deepest P-well boron, at
   550 keV, through a 200 nm polysilicon mask to avoid boron scattering,
   and masks its 150 keV and 45 keV boron with a resist "between
   1800-2500 nm";[^pat-well-ibm] Hook's IBM
   study modelled a "2.3 µm-thick pwell mask" against 600 keV
   boron;[^hook-2003] Zilog's 600–800 keV p-well needed at least
   3.4 µm.[^pat-resist-zilog] For a P-well whose peak is at 0.42 µm and
   whose vertical extent is 0.75 µm,[^pdk-03] boron energies are lower
   than those examples and a resist of roughly 2 µm is plausible
   (inference).[^txt-02]
3. **Exposure.** i-line: the `pwbm` rules carry no minimum width, but
   the reticle's tightest features are the N-well outlines (0.840 µm
   width, 1.270 µm space),[^pdk-periph] for which i-line has ample
   margin ({term}`k₁ <k1>` ≈ 1.4 at {term}`NA` 0.6).[^wiki-litho] We infer an **i-line
   layer**.
4. **Alignment** to STI. The N-well/P-well junction is budgeted at
   0.034 µm from the drawn edge,[^pdk-03] so `PWBM` and `NWM` must both
   register to the same STI marks; their mutual {term}`overlay` is what sets the
   well-to-well junction position and hence the n⁺/p⁺ spacing
   rules.[^rubin-2002]
5. **Develop, hard bake, inspect.** 2.38 % TMAH[^microchemicals-dev]
   (0.26 N; our arithmetic from TMAH's molar mass of 91.15 g/mol,[^wiki-tmah]
   taking the solution's density as about 1 g/mL)
   develop; resist hardening for
   the high-energy implant; overlay to STI.

**{term}`Well proximity effect <well proximity effect>`.** As with the N-well, ions scattered from the
resist edge shift the threshold of transistors within about a micrometre
of the well boundary;[^hook-2003][^sheu-2006] for P-well edges the shift
raises NMOS {term}`Vt`.[^hook-2003]

## Machines typically used

* **{ref}`i-line <machine-i-line-stepper>` {term}`stepper`**, 200 mm (ASML PAS 5500/100–/275, Nikon NSR-2205i,
  Canon FPA-3000i).[^txt-05]
* **{ref}`Coat/develop track <machine-coat-develop-track>`** with thick-resist capability.
* **{ref}`Overlay metrology <machine-cd-sem-overlay-metrology>`** and a {term}`CD-SEM` for periodic checks.

## Machines likely used at SkyWater

* **ASML i-line stepper / scanner**.[^skw-01] Strength: **strong** for
  existence; assignment to `PWBM` is an **inference** from the coarse
  rules and thick resist.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius**.[^skw-01] Strength:
  strong for existence.
* **Overlay — KLA 5200/5300/Archer; CD — AMAT Verity/VeraSEM**.[^skw-01]
  Strength: strong for existence (SkyWater statement); use at this
  mask is an inference.

## Resources required

* **Thick positive i-line implant resist** ({ref}`lithography materials <material-lithography-materials>`; ~2 µm class, inference);
  suppliers named in SkyWater's 2021 S-1: Dow, JSR, Tokyo Ohka
  Kogyo.[^sec-01]
* **HMDS**, **2.38 % (0.26 N) TMAH developer**,[^microchemicals-dev]
  edge-bead remover, {ref}`DI water <material-ultrapure-water>`, {ref}`nitrogen <material-process-gases>`.
* **The PWBM reticle**, generated from `nwell` and `pwbm`
  (inference).[^pdk-06]

## Related steps and cross-references

* Previous: {ref}`PCHIS <step-025>`.
* Next: {ref}`PWI <step-027>` and {ref}`PWI2 <step-028>` through this
  resist; strip at {ref}`PWIS <step-029>`.
* Complementary mask: {ref}`NWM <step-017>`. The regions blocked here
  and re-doped later: {ref}`PWDEM <step-030>`.
* The isolated P-well inside the deep N-well tub
  ({ref}`DNM <step-007>`) is formed by this same implant, ringed by
  N-well.
* Previous mask: {ref}`HVTPM <step-022>`; next mask:
  {ref}`PWDEM <step-030>`.
* Mask page: {ref}`PWBM <mask-pwbm>` — the mask's layers, plates,
  renders and design rules.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,247,199 A <patent-gp27357991>` — Process for forming twin well CMOS integrated circuits (1986)
* {ref}`US 6,455,402 B2 <patent-gp19572018>` — Method of forming retrograde doping file in twin well CMOS device (1999)
* {ref}`US 6,576,405 B1 <patent-gp23358573>` — High aspect ratio photolithographic method for high energy implantation (1999)
* {ref}`US 6,667,205 B2 <patent-gp29214361>` — Method of forming retrograde n-well and p-well (2002)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "P-Well Block Mask,
  PWBM" with the "Used in SKY130" column blank.[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `pwbm` 19:44;
  `nwell` 64:20; `pwell` label/pin/resistor purposes only.[^pdk-06]
* SkyWater PDK, *Periphery rules* — pwbm.1–5 "Define p-well block";
  pwdem.3; nwell.1, nwell.2a.[^pdk-periph]
* SkyWater PDK, *Device Details* — `nfet_20v0_zvt`: "p-well and all Vt
  implants blocked".[^pdk-07]
* SkyWater PDK, *Criteria & Assumptions* — P-well peak concentration and
  coordinate, vertical dimension, junction offset.[^pdk-03]
* SKY130 raw-data repository — I–V sweeps of the 20 V zero-Vt test-tile
  structure (threshold, body-effect coefficient and effective doping
  quoted here are our extraction) and the pad-list row that names
  it.[^raw-data-hv-mosfets][^raw-data-testtile-pads]
* SkyWater PDK, *High Voltage Methodology* — drain extensions
  "fabricated by lightly doped Nwells and Pwells".[^pdk-hv]
* SkyWater, *Facilities & Capabilities* — the site tool list.[^skw-01]
* SkyWater, Form S-1 (2021) — photoresist, gas and chemical
  suppliers.[^sec-01]

### High-level understanding

* Wikipedia, *CMOS* — NMOS on the p-substrate, PMOS in an
  N-well.[^wiki-cmos]
* Wikipedia, *Photolithography* — 365 nm i-line and {term}`CD` =
  k₁·λ/NA.[^wiki-litho]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography, resist stripping, wafer cleaning and implantation
  chapters.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 2 — twin-well CMOS,
  well masking options.[^txt-03]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — lithography
  tools, implanted-resist stripping and {term}`RTP` of the 0.25–0.13 µm
  generations.[^txt-05]
* MicroChemicals, *Development of photoresists* — practical
  develop-process notes, including the 2.38 % TMAH
  developers.[^microchemicals-dev]

### Deep dive

* Breitwisch, Lam and Slinkman (IBM), US 6,667,205 — retrograde N-well
  and P-well energies, doses and resist thickness.[^pat-well-ibm]
* Buffat and Adams (Zilog), US 6,576,405 — 3.4–4.2 µm resist for
  1.3–1.5 MeV phosphorus wells.[^pat-resist-zilog]
* Matlock (Harris), US 5,247,199 — a twin-well flow with 500/275/130 keV
  phosphorus and 360/185/55 keV boron chains.[^pat-twin-harris]
* Hook et al. (IBM), *IEEE TED* 2003 — lateral {term}`straggle` from a thick
  well resist and the resulting mask proximity effect.[^hook-2003]
* Sheu et al. (TSMC), *IEEE TED* 2006 — a compact model of the well-edge
  proximity effect.[^sheu-2006]
* Rubin, Morris and Jasper, IIT 2002 — how well-implant control sets the
  n⁺/p⁺ isolation spacing.[^rubin-2002]
* Drennan, Kniffin and Locascio, CICC 2006 — the analogue-design
  consequences of the well proximity effect.[^drennan-2006]
* Mack, *Fundamental Principles of Optical Lithography* — thick-resist
  imaging and k₁ margins behind the i-line choice.[^mack-2007]
* Levinson, *Principles of Lithography* — the chapter on
  overlay.[^levinson-2005]
* Lee et al. (Genus), IIT 1996 — outgassing of thick resists during MeV
  implantation.[^lee-1996]
* Stolmeijer, *IEEE TED* 1986 — a twin-well CMOS process using implants of
  up to 1 MeV, with an N-type isolation well and retrograde
  wells.[^stolmeijer-1986]
* Lee and Son (Hyundai/Hynix), US 6,455,402 — chained retrograde P-well
  implants placed through a resist mask.[^pat-well-hynix]
* Borland, Cho and Kim, IIT 1998 — latch-up with MeV-implanted wells
  under STI, the reason the P-well profile matters.[^borland-1998]

## Open questions

* The PDK mask table leaves the "Used in SKY130" column blank for PWBM
  (and for PWDEM) although the `pwbm`/`pwde` layers and their rules
  exist and the 20 V devices depend on them;[^pdk-07] in
  `masks.csv` these two `pwbm`/`pwde`-backed masks are the only
  well-module masks left blank — DNM, NWM, HVTPM and LVTNM are all
  ticked.[^pdk-05] We treat the blank as a documentation inconsistency.
* That the reticle is derived from `nwell` ∪ `pwbm` is our inference
  from the absence of a drawn P-well layer; the actual Boolean
  generation rules are not public.
* Resist thickness and exposure tool are inferred.

<!-- footnotes -->

[^wiki-tmah]: Wikipedia, *Tetramethylammonium hydroxide*.
    <https://en.wikipedia.org/wiki/Tetramethylammonium_hydroxide>
[^microchemicals-dev]: MicroChemicals, *Development of photoresists*,
    application note.
    <https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^wiki-cmos]: Wikipedia, *CMOS*. <https://en.wikipedia.org/wiki/CMOS>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^pat-twin-harris]: D. A. Matlock (Harris Corporation), *Process for
    forming twin well CMOS integrated circuits*, US 5,247,199 A, granted
    1993-09-21. <https://patents.google.com/patent/US5247199A/en>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^pat-well-ibm]: M. J. Breitwisch, C. H. Lam and J. A. Slinkman (IBM),
    *Method of forming retrograde n-well and p-well*, US 6,667,205 B2,
    granted 2003-12-23.
    <https://patents.google.com/patent/US6667205B2/en>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^pat-resist-zilog]: S. J. Buffat and J. L. Adams (Zilog), *High aspect
    ratio photolithographic method for high energy implantation*, US
    6,576,405 B1, granted 2003-06-10.
    <https://patents.google.com/patent/US6576405B1/en>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^rubin-2002]: L. M. Rubin, W. Morris and C. Jasper, "Process control
    issues for retrograde well implants for narrow n+/p+ isolation in
    CMOS", *Proc. 2002 International Conference on Ion Implantation
    Technology*, pp. 17–20. <https://doi.org/10.1109/IIT.2002.1257927>
[^sheu-2006]: Y.-M. Sheu, K.-W. Su, S. Tian, S.-J. Yang, C.-C. Wang,
    M.-J. Chen and S. Liu, "Modeling the Well-Edge Proximity Effect in
    Highly Scaled MOSFETs", *IEEE Transactions on Electron Devices*
    **53**(11), 2792–2798 (2006).
    <https://doi.org/10.1109/TED.2006.884070>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^txt-03]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 2:
    Process Integration*, Lattice Press, 1990, ISBN 978-0-9616721-4-0.
    <https://openlibrary.org/isbn/9780961672140>
[^drennan-2006]: P. G. Drennan, M. Kniffin and D. Locascio,
    "Implications of Proximity Effects for Analog Design", *Proc. IEEE
    Custom Integrated Circuits Conference 2006*, pp. 169–176.
    <https://doi.org/10.1109/CICC.2006.320869>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007,
    ISBN 978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
    (companion site <https://www.lithoguru.com/textbook/>)
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^stolmeijer-1986]: A. Stolmeijer, "A twin-well CMOS process employing
    high-energy ion implantation", *IEEE Transactions on Electron
    Devices* **33**(4), 450–457 (1986).
    <https://doi.org/10.1109/T-ED.1986.22511>
[^pat-well-hynix]: J.-H. Lee and J.-H. Son (Hyundai/Hynix), *Method of
    forming retrograde doping profile in twin well CMOS device*, US
    6,455,402 B2, granted 2002-09-24.
    <https://patents.google.com/patent/US6455402B2/en>
[^borland-1998]: J. O. Borland, H. T. Cho and J. K. Kim, "LOCOS vs.
    shallow trench isolation latch-up using MeV implantation for well
    formation down to 0.18 μm design rules", *Proc. 1998 International
    Conference on Ion Implantation Technology*, vol. 1, pp. 67–70.
    <https://doi.org/10.1109/IIT.1999.812053>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^raw-data-hv-mosfets]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the 5 V, 10/16 V and
    20 V transistors, the native, zero-Vt and ESD NMOS and the thick-oxide
    gate capacitors, IC-CAP `.mdm` files in `sky130_fd_pr/cells/`
    (`nfet_g5v0d10v5`, `pfet_g5v0d10v5`, `nfet_g5v0d16v0`,
    `pfet_g5v0d16v0`, `nfet_g5v0d20v0`, `pfet_g5v0d20v0`,
    `nfet_03v3_nvt`, `nfet_05v0_nvt`, `nfet_20v0_nvt`, `esd_nfet_01v8`,
    `esd_nfet_g5v0d10v5`), `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
