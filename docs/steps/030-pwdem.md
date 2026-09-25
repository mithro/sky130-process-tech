(step-030)=
# Step 030 — PWDEM: P-well drain extended mask

| | |
|---|---|
| **Step number** | 30 of 171[^steps-sheet] |
| **Step code** | `PWDEM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | {term}`FEOL` — wells and channel implants |
| **Previous step** | {ref}`PWIS <step-029>` |
| **Next step** | {ref}`PWDEI1 <step-031>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** opens resist windows over the 20 V devices for a custom,
  lightly doped P-well, in place of the standard P-well `PWBM` blocked
  there.
* **Why:** the standard P-well is too heavily doped to deplete fully
  at 20 V; the drift region needs a lighter, purpose-built well.
* **Public numbers:** measured 16 V NMOS on-resistance about 470 Ω at
  20 µm width (our extraction).[^raw-data-hv-mosfets]
* **Likely SkyWater tool:** ASML i-line stepper or scanner — strong
  (existence); inference (assignment).[^skw-01]
* **Not public:** whether `pwde` covers the 20 V NMOS body, the PMOS
  drift region, or both (→ Open questions).
:::

## What this step is

`PWDEM` prints the *P-well {term}`drain-extended <DEMOS>` mask*, the last lithography of
the well and channel module. A photoresist (thick, we infer) is coated,
exposed and developed to open windows over the regions of the 20 V
devices that are to receive a purpose-built, lightly doped P-well.

The
two implants {ref}`PWDEI1 <step-031>` and {ref}`PWDEI2 <step-032>`
follow (through the same resist in the sequence this reference
describes), and the
resist is stripped at {ref}`PWDEIS <step-033>`.

:::{figure} /_static/figures/wells-030-pwdem.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step the oxide surface is bare over a P-well on the left and an N-well on the right. After it a thick block of photoresist covers the whole slice: the windows of this mask lie over other devices, not over this pair.
:width: 560px
:name: fig-wells-030-pwdem

Before, the bare wafer over both wells; after, thick resist over the whole slice. This mask opens windows only over parts of the 20 V devices, whose `pwde` regions lie inside a deep-N-well tub;[^pdk-periph] this slice, drawn outside a deep N-well region like the rest of the module, is an ordinary NMOS and PMOS pair and stays covered. The resist thickness is inferred. The PDK's mask table leaves the mask's "Used in SKY130" column blank, which this reference treats as a documentation inconsistency.[^pdk-05] The NMOS channel implant, the PMOS channel implant and the liner oxide are drawn faded. Not to scale.
:::

### What the public record shows

The drawn layer is `pwde` (GDS 124:20), "Regions to receive p-well
drain-extended implants".[^pdk-06] Its rules (pwdem.1–pwdem.6) name the
layer `pwdem`, not `pwde` — the PDK is inconsistent between the drawn
layer's name and its rule set's name for it — but have no public
numeric values.

They fix the geometry:

* `pwde` "must be enclosed by UHVI" (pwdem.4), the 20 V node identifier;
* "pwdem.dg inside UHVI must be enclosed by deep nwell" (pwdem.5), with a
  minimum enclosure by deep N-well (pwdem.6);
* it must be enclosed by the P-well block layer `pwbm`
  (pwdem.3).[^pdk-periph]

The `pwbm` description reads "Regions (in UHVI) blocked from p-well
implant (DE MOS devices only)".[^pdk-06] Read together, the sequence
is: the standard P-well was kept *out* of
the 20 V device area at {ref}`PWBM <step-026>`, and `PWDEM` now puts a
*different* P-well back into part of it, inside a deep-N-well tub.

The PDK's mask table lists "P-Well Drain Extended, PWDEM" but, as for
PWBM, leaves the "Used in SKY130" column blank;[^pdk-05] the layer and
its rules exist,[^pdk-06] so this reference treats the blank as a
documentation inconsistency (see *Open questions*).

## Step category

`PWDEM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *thick-resist implant-block* type, aligned (we infer) to the
{term}`STI` pattern and used only by the high-voltage device family. Its
features are large — the 20 V devices have drawn channel lengths of the
order of a micrometre (the PDK's HV methodology gives 1.055 µm and
1.050 µm for the 16 V VHV NMOS and PMOS[^pdk-hv]) and {term}`drift regions <drift region>`
longer still.[^pdk-07]

## Why this step exists

SKY130 is a multi-voltage process: a 1.8 V core, 5 V I/O, and "HV
extended-drain NMOS and PMOS"[^pdk-10] rated in the PDK at 11/16 V for
the NMOS (`nfet_g5v0d16v0`) and 10/16 V for the PMOS
(`pfet_g5v0d16v0`), and 20 V (`nfet_20v0`, `pfet_20v0`,
`nfet_20v0_iso`, `nfet_20v0_nvt`, `nfet_20v0_zvt`).[^pdk-07] SkyWater's
platform table lists "20+V, Drain-Extended CMOS (16V)" for
S130.[^skw-02]

A drain-extended (DE) MOSFET keeps the thin gate oxide
and short channel of a 5 V transistor but inserts a lightly doped
*drift* region between channel and drain. "Drain extended transistors
differ from regular self aligned polysilicon gate transistors in that
they use a very lightly doped extension region adjacent to the drain
that depletes at high drain voltages".[^pat-demos-ti]

The PDK says the
same for its own devices: "The VHV devices need to be designed with
drain extentions (DE) fabricated by lightly doped Nwells and Pwells
respectively" and "All VHV devices use 110A gate oxide thickness just
like standard 5.0V Vcc devices".[^pdk-hv]

For the 16 V devices the ordinary wells serve, we infer, as the drift
regions;[^pdk-hv] a second TI patent notes that DE devices can be made
"without the addition of extra masks or processing
steps".[^pat-demos-ti2]

For the 20 V devices the standard P-well is too
heavily doped: a drift region must deplete fully at the rated voltage,
which requires a doping and depth that a 4 × 10¹⁷ cm⁻³ well[^pdk-03]
cannot provide. `PWDEM` therefore defines where a lighter, custom P-well
goes — we infer, the drift region of the 20 V PMOS and the body of the
20 V NMOS whose standard P-well was blocked.

This is what makes the 20 V
devices "similar construction to the 11V/16V NMOS FET, with several
differences: Longer drift region, Longer poly gate, Larger W/L, Devices
placed in pairs".[^pdk-07]

The published SKY130 {term}`test tile` includes such devices: "VHV DE
NMOS" and "VHV DE PMOS" transistors with lengths labelled "L=0.7" and
"L=2.2" (NMOS) and "L=0.66" and "L=2.16" (PMOS), and a PMOS listed as
`p20vhv1` with the cell name
"s8tet_s_hvp_pwde_stdnw_sti_1p5_2f_60um_IP_LVS".[^raw-data-testtile-pads]
The `pwde` in that name matches the drawn layer of this
mask;[^pdk-06] the pad list itself does not explain the name.

The measurements of those structures published in the raw-data
repository show the electrical behaviour expected of a lightly doped
drift region in series with the channel, although the drain was swept to
no more than 5 V (10 V on the symmetric 16 V structures). This means
they say nothing about breakdown.

Ten 20 µm-wide `nfet_g5v0d16v0` structures with
a 0.925 µm drawn gate ("L=0.7") have a median resistance of about 470 Ω
at V_GS = 5 V and V_DS = 0.1 V (from the I_D–V_D sweeps), against 119 Ω for a 20/0.5 µm
`nfet_g5v0d10v5`. At V_DS = 2.5 V they carry 62–71 % of their
V_DS = 5 V current, against 95 % for that device and 96 % for a
1/1 µm `nfet_g5v0d10v5`. That device's 3.2 kΩ at the same bias
corresponds to about 160 Ω at 20 µm width.

Their threshold, taken at a constant
current of 100 nA × W/L, moves by 1–6 mV per volt of drain bias, which
a 1/1 µm 5 V device (3.9 mV/V) also shows, against 28 mV/V at 0.5 µm.
This last difference reflects gate length rather than the drift
region. This is our extraction from the published measurements.[^raw-data-hv-mosfets]

The 16 V PMOS behaves
alike (about 725 Ω against 310 Ω at 20 µm width), and the 20 V NMOS and
PMOS structures of modules 4441 and 4442 carry 60–70 % of their
V_DS = 5 V current at 2.5 V.[^raw-data-hv-mosfets]

The thresholds of the
16 V NMOS (0.73–0.79 V by maximum-transconductance extrapolation, less
half the 0.1 V drain bias) are
close to those of a 7/8 µm `nfet_g5v0d10v5` (0.79–0.82 V by
the same fit).

Its body-effect coefficient at
L = 2.425 µm is 0.70–0.72 √V, from a least-squares fit of the threshold
shifts at body biases of −2.5 V and −5 V to the uniform-doping
expression, with the surface potential set by the implied doping. This
is likewise close to that reference device's 0.73 √V by the same fit.
This is consistent
with a 5 V channel to which a drain extension has been added. The data
contain nothing about the implants that form the
extension.[^raw-data-hv-mosfets]

## How it is typically performed

*An industry-generic drain-extension well lithography for a 200 mm,
130 nm-era fab:*

1. **Track preparation.** {term}`HMDS` prime; no {term}`BARC` for micrometre-scale
   features (inference).[^wiki-litho]
2. **Thick resist coat.** The resist must stop the deepest
   drain-extension implant. A DE well is *lighter* than the main well
   but not necessarily shallower — a deep, graded drift region gives the
   best breakdown.

   A 2 µm-class implant resist like that of
   {ref}`PWBM <step-026>` is plausible (inference;[^txt-02] compare
   IBM's 1800–2500 nm resist for 150 keV and 45 keV boron, its 550 keV
   boron going through a 200 nm polysilicon mask[^pat-well-ibm]).
3. **Exposure.** i-line; the layer's features are
   micrometre-scale[^pdk-hv] and its {term}`overlay` requirements are set by the
   drift-region length rather than by a sub-micrometre {term}`CD`. We infer an
   **i-line layer**.
4. **Alignment** to STI. In a DE device the field-oxide length and the
   poly-to-drift overlap are reliability-critical: "Under no
   circumstances the poly/extended drain overlap and field oxide length
   should be changed".[^pdk-hv]

   So the well edge position relative to
   the STI, and later the poly, matters more than for an ordinary well.
5. **Develop, hard bake, inspect.** 2.38 % TMAH[^microchemicals-dev]
   (0.26 N; our arithmetic from TMAH's molar mass of 91.15 g/mol,[^wiki-tmah]
   taking the solution's density as about 1 g/mL)
   develop.

## Machines typically used

* **{ref}`i-line <machine-i-line-stepper>` {term}`stepper`**, 200 mm (ASML PAS 5500/100–/275, Nikon NSR-2205i,
  Canon FPA-3000i).[^txt-05]
* **{ref}`Coat/develop track <machine-coat-develop-track>`** with thick-resist capability; **{ref}`overlay tool <machine-cd-sem-overlay-metrology>`**
  and a {term}`CD-SEM` for periodic checks.

## Machines likely used at SkyWater

* **ASML i-line stepper / scanner**
  - *SkyWater says:* lists it.[^skw-01]
  - *Tool exists:* strong.
  - *Runs this step:* inference from the coarse geometry.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius**[^skw-01]
  - *Tool exists:* strong for existence.
* **Overlay — KLA 5200/5300/Archer; CD — AMAT Verity/VeraSEM**[^skw-01]
  - *Tool exists:* strong for existence (SkyWater statement).
  - *Runs this step:* use at this mask is an inference.

## Resources required

* **Thick positive i-line {ref}`implant resist <material-lithography-materials>`** (inference); suppliers named
  in SkyWater's 2021 S-1: Dow, JSR, Tokyo Ohka Kogyo.[^sec-01]
* **HMDS**, **2.38 % (0.26 N) TMAH developer**,[^microchemicals-dev]
  edge-bead remover, {ref}`DI water <material-ultrapure-water>`, {ref}`nitrogen <material-process-gases>`.
* **The PWDEM {term}`reticle`** (from `pwde`).[^pdk-06]

## Related steps and cross-references

* Previous: {ref}`PWIS <step-029>`.
* Next: {ref}`PWDEI1 <step-031>` and {ref}`PWDEI2 <step-032>` through
  this resist; strip at {ref}`PWDEIS <step-033>`.
* Depends on: the standard P-well blocked from these regions —
  {ref}`PWBM <step-026>`; the deep N-well tub they sit in —
  {ref}`DNM <step-007>`; the N-well drift regions of the DE NMOS —
  {ref}`NWM <step-017>`.
* Mask: {ref}`PWDEM <mask-pwdem>` — the mask's layer, plates, renders
  and design rules; the previous mask is {ref}`PWBM <step-026>`, the
  next mask {ref}`TUNM <step-035>`.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

18 families concern this page (1 in force, 10 unknown, 7 expired).

See {ref}`patents-by-module` for the full, grouped list (families still in force or of unknown status are collapsed there too).
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "P-Well Drain Extended,
  PWDEM".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `pwde` 124:20;
  `pwbm` 19:44; `uhvi` 74:22.[^pdk-06]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — pwdem.1–pwdem.6.[^pdk-periph]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — 20 V NMOS/PMOS, isolated, native and
  zero-Vt 20 V NMOS; 10/16 V devices.[^pdk-07]
* [SkyWater PDK, *High Voltage Methodology*](<https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>) — DE by lightly doped wells;
  110 Å oxide; channel lengths; poly/drift overlap rule.[^pdk-hv]
* [google/skywater-pdk repository README](<https://github.com/google/skywater-pdk>) — "HV extended-drain NMOS and
  PMOS".[^pdk-10]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — P-well peak
  concentration.[^pdk-03]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the site tool list.[^skw-01]
* [SkyWater, *Mixed-Signal CMOS & ROIC* platform table](<https://www.skywatertechnology.com/cmos/>) — "20+V,
  Drain-Extended CMOS (16V)".[^skw-02]
* [SkyWater, Form S-1 (2021)](<https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>) — photoresist, gas and chemical
  suppliers.[^sec-01]
* [SKY130 raw-data repository, test-tile pad documentation](<https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>) — the
  drain-extended transistor structures of the published test
  tile.[^raw-data-testtile-pads]
* [SKY130 raw-data repository, measured data](<https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>) — I–V sweeps of the 5 V,
  16 V and 20 V transistors on the test tile; the resistances, current
  ratios, thresholds and body-effect coefficients quoted here are our
  extraction.[^raw-data-hv-mosfets]

### High-level understanding

* [Wikipedia, *LDMOS*](<https://en.wikipedia.org/wiki/LDMOS>) — drift region formed by implantation.[^wiki-ldmos]
* [Wikipedia, *Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) — 365 nm i-line and CD =
  {term}`k₁ <k1>`·λ/{term}`NA`.[^wiki-litho]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) —
  lithography, resist stripping, wafer cleaning and implantation
  chapters.[^txt-02]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) — lithography
  tools, implanted-resist stripping and {term}`RTP` of the 0.25–0.13 µm
  generations.[^txt-05]
* [MicroChemicals, *Development of photoresists*](<https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>) — practical
  develop-process notes, including the 2.38 % TMAH
  developers.[^microchemicals-dev]

### Deep dive

* [Mitros (Texas Instruments), US 6,660,603](<https://patents.google.com/patent/US6660603B2/en>) — drain-extended MOS built on
  the existing wells, with drift-well doses and energies.[^pat-demos-ti]
* [Chidambaram (Texas Instruments), US 2006/0006461](<https://patents.google.com/patent/US20060006461A1/en>) — DE devices "without
  the addition of extra masks or processing steps".[^pat-demos-ti2]
* [Mitros et al. (Texas Instruments), *IEEE TED* 2001](<https://doi.org/10.1109/16.936703>) — drain-extended
  MOS transistors added to a 0.18 µm logic process.[^mitros-2001]
* [Mai and Rücker (IHP), *Solid-State Electronics* 2011](<https://doi.org/10.1016/j.sse.2011.06.034>) — DE devices in a
  0.13 µm technology.[^mai-2011]
* [Breitwisch, Lam and Slinkman (IBM), US 6,667,205](<https://patents.google.com/patent/US6667205B2/en>) — resist thickness
  for keV-hundreds boron.[^pat-well-ibm]
* [Appels and Vaes (Philips), IEDM 1979](<https://doi.org/10.1109/IEDM.1979.189589>) — the original RESURF paper: why
  a thin, lightly doped layer holds off high voltage.[^appels-1979]
* [Ludikhuize (Philips), ISPSD 2000](<https://doi.org/10.1109/ISPSD.2000.856763>) — a review of RESURF design rules for
  drift regions.[^ludikhuize-2000]
* [Baliga, *Fundamentals of Power Semiconductor Devices*](<https://doi.org/10.1007/978-0-387-47314-7>) — breakdown,
  drift-region doping and on-resistance trade-offs.[^baliga-2008]
* [Efland, Tsai and Pendharkar (Texas Instruments), IEDM 1998](<https://doi.org/10.1109/IEDM.1998.746447>) — LDMOS
  integration into logic CMOS from the TI group behind the DE
  devices.[^efland-1998]
* [Kwon, Efland, Malhi and Ng (Texas Instruments), US 5,406,110](<https://patents.google.com/patent/US5406110A/en>) — a
  RESURF lateral DMOS with an implanted drift region.[^pat-resurf-ti]
* [Buffat and Adams (Zilog), US 6,576,405](<https://patents.google.com/patent/US6576405B1/en>) — thick-resist lithography for
  high-energy implants.[^pat-resist-zilog]
* [Lee et al. (Genus), IIT 1996](<https://doi.org/10.1109/IIT.1996.586180>) — outgassing of thick resists during MeV
  implantation.[^lee-1996]

## Open questions

* **Reticle scope.** Whether `pwde` defines the body of the 20 V NMOS,
  the drift region of the 20 V PMOS, or both, is inferred from the
  rule geometry; the PDK's 20 V cross-section drawings are not
  labelled in text form.

  The
  test-tile pad list names the 20 V PMOS structures
  `s8tet_s_hvp_pwde_stdnw_sti_1p5_2f_60um_IP_LVS` and variants, with
  `pwde` in the name, and the 20 V NMOS structures (for example
  `s8tet_s_hvn_nw_dnw_sti_3p0_IP` and
  `s8tet_s_hvn_iso_nw_dnw_sti_2p0_esd_IP`) without it.[^raw-data-testtile-pads]
  Names need not list every layer, so this supports the PMOS reading
  without settling the NMOS one.
* **Blank "Used in SKY130" entry.** This entry for PWDEM in the PDK
  mask table sits oddly with the existence of the `pwde` layer and its
  rules; we treat it as a documentation inconsistency that cannot be
  resolved publicly.
* **Resist thickness and exposure tool.** Both are inferred.

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
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README. <https://github.com/google/skywater-pdk>
[^skw-02]: SkyWater Technology, *Mixed-Signal CMOS & ROIC*, platform
    table, accessed 2026-09-13.
    <https://www.skywatertechnology.com/cmos/>
[^pat-demos-ti]: J. C. Mitros (Texas Instruments), *Higher voltage drain
    extended MOS transistors with self-aligned channel and drain
    extensions*, US 6,660,603 B2, granted 2003-12-09.
    <https://patents.google.com/patent/US6660603B2/en>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-ldmos]: Wikipedia, *LDMOS*. <https://en.wikipedia.org/wiki/LDMOS>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^pat-demos-ti2]: P. R. Chidambaram (Texas Instruments), *Drain extended
    MOS transistors and methods for making the same*, US 2006/0006461
    A1, published 2006-01-12.
    <https://patents.google.com/patent/US20060006461A1/en>
[^mitros-2001]: J. C. Mitros, C.-Y. Tsai, H. Shichijo, M. Kunz, A.
    Morton, D. Goodpaster, D. Mosher and T. R. Efland, "High-voltage
    drain extended MOS transistors for 0.18-µm logic CMOS process",
    *IEEE Transactions on Electron Devices* **48**(8), 1751–1755 (2001).
    <https://doi.org/10.1109/16.936703>
[^mai-2011]: A. Mai and H. Rücker, "Drain-extended MOS transistors
    capable for operation at 10 V and at radio frequencies",
    *Solid-State Electronics* **65–66**, 45–50 (2011).
    <https://doi.org/10.1016/j.sse.2011.06.034>
[^pat-well-ibm]: M. J. Breitwisch, C. H. Lam and J. A. Slinkman (IBM),
    *Method of forming retrograde n-well and p-well*, US 6,667,205 B2,
    granted 2003-12-23.
    <https://patents.google.com/patent/US6667205B2/en>
[^appels-1979]: J. A. Appels and H. M. J. Vaes, "High voltage thin layer
    devices (RESURF devices)", *1979 International Electron Devices
    Meeting*, pp. 238–241. <https://doi.org/10.1109/IEDM.1979.189589>
[^ludikhuize-2000]: A. W. Ludikhuize, "A review of RESURF technology",
    *Proc. 12th International Symposium on Power Semiconductor Devices &
    ICs* (2000), pp. 11–18. <https://doi.org/10.1109/ISPSD.2000.856763>
[^baliga-2008]: B. J. Baliga, *Fundamentals of Power Semiconductor
    Devices*, Springer, 2008, ISBN 978-0-387-47313-0.
    <https://doi.org/10.1007/978-0-387-47314-7>
[^efland-1998]: T. R. Efland, C.-Y. Tsai and S. Pendharkar, "Lateral
    thinking about power devices (LDMOS)", *IEDM 1998 Technical Digest*,
    pp. 679–682. <https://doi.org/10.1109/IEDM.1998.746447>
[^pat-resurf-ti]: O.-K. Kwon, T. R. Efland, S. Malhi and W. T. Ng (Texas
    Instruments), *Resurf lateral double diffused insulated gate field
    effect transistor*, US 5,406,110 A, granted 1995-04-11.
    <https://patents.google.com/patent/US5406110A/en>
[^pat-resist-zilog]: S. J. Buffat and J. L. Adams (Zilog), *High aspect
    ratio photolithographic method for high energy implantation*, US
    6,576,405 B1, granted 2003-06-10.
    <https://patents.google.com/patent/US6576405B1/en>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
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
