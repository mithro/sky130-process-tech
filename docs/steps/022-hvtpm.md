(step-022)=
# Step 022 — HVTPM: High V P-channel implant mask

| | |
|---|---|
| **Step number** | 22 of 171[^steps-sheet] |
| **Step code** | `HVTPM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | {term}`FEOL` — wells and channel implants |
| **Previous step** | {ref}`LVTPIS <step-021>` |
| **Next step** | {ref}`PCHI <step-023>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** opens resist windows for the high-Vt PMOS channel implants
  (`PCHI`, `PNCHI`).
* **Why:** gives SKY130 a third 1.8 V PMOS threshold for low-leakage
  design, since the baseline threshold is set through the N-well mask.
* **Public numbers:** minimum `hvtp` width and spacing 0.380 µm
  (hvtp.1, hvtp.2).[^pdk-periph]
* **Likely SkyWater tool:** ASML i-line stepper or scanner — strong
  (existence); inference (assignment).[^skw-01]
* **Not public:** which reticle-polarity reading is correct (→ Open
  questions).
:::

## What this step is

`HVTPM` prints the *high-Vt P-channel mask*: photoresist is coated on
the cleaned wafer, exposed through the HVTPM {term}`reticle` and developed,
opening windows over the PMOS channels that are to have a raised
threshold. Two implants follow, in the sequence this reference
describes, through
the same resist — the P-channel implant {ref}`PCHI <step-023>` and the
second P-channel implant {ref}`PNCHI <step-024>` (BF₂ on this
reference's reading) — and the resist is
stripped at {ref}`PCHIS <step-025>`.

:::{figure} /_static/figures/wells-022-hvtpm.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step the oxide surface is bare over an N-well on the right. After it a block of photoresist covers the left-hand part of the drawing up to the middle of the trench, and the right-hand active area, with its implanted surface band, lies in an open window.
:width: 560px
:name: fig-wells-022-hvtpm

Before, the bare wafer with its N-well; after, resist over the NMOS side and a window over the PMOS. The PDK's mask table lists "High Vt PCh*, HVTPM".[^pdk-05] The page sets out two readings of the opening — over the drawn `hvtp` devices only, or over most low-voltage N-well outside `lvtn` — and, taking this PMOS as a high-Vt (`hvtp`) device, as the whole slice is read (an NMOS beside a high-Vt PMOS), it lies in the window on either; which matches the plate is not public.[^pdk-errors] The resist edge in the trench is illustrative. The NMOS channel implant and the liner oxide are drawn faded. Not to scale.
:::

### What the public record shows

A note on the name. The step list used in this reference gives the name
"High V P-channel implant mask", which could be read as *high-voltage*.

The PDK is unambiguous that the "V" is a threshold:

* the mask table lists "High Vt PCh*, HVTPM";[^pdk-05]
* the drawn layer `hvtp` (GDS 78:44) is "High-Vt LVPMOS implant" and
  the generated mask `chvtpm` (GDS 97:0) is "High Vt Pch mask", with
  mask add/drop purposes 97:43 and 97:42;[^pdk-06]
* the rule table's function line reads "Define Vt adjust implant
  region for high Vt LV PMOS".[^pdk-periph]

The device it creates is `pfet_01v8_hvt`, the "1.8V high-VT PMOS FET",
and the high-Vt varactor option `cap_var_hvt`.[^pdk-07] The "LV" in the
layer's description makes the point twice: this is a low-voltage
(1.8 V) device with a high threshold, nothing to do with the 5 V or
20 V families.

### Key numbers

The design rules are as coarse as those of `lvtn`:

| Rule[^pdk-periph] | Constrains | Value |
|---|---|---:|
| hvtp.1 | minimum width | 0.380 µm |
| hvtp.2 | minimum spacing | 0.380 µm |
| hvtp.3 | minimum enclosure of a PMOS by `hvtp` | 0.180 µm |
| hvtp.4 | minimum spacing from a PMOS not meant to be high-Vt | 0.180 µm |
| hvtp.5, hvtp.6 | minimum area | 0.265 µm² |
| lvtn.9 | no overlap with `lvtn` | 0.380 µm spacing |

Unlike `lvtn`, whose rule heading says it
*blocks* an implant, `hvtp` is described as the *region that receives*
the implant, so we read the reticle polarity as straightforward: resist
is removed over `hvtp`. That reading is an inference from the layer
description.

One public derivation from the drawn MPW
tape-out layouts, which cites no source, renders it as (`nwell` NOT
`hvi`) NOT `lvtn`, without `hvtp`
({ref}`masks-derivations`).[^mask-renders]

### Competing readings

The PDK's *Error Messages* page lists checks on a layer it calls
`CLHVTPM` but does not define:

| Check[^pdk-errors] | Rule text |
|---|---|
| chvtpm.1 | "0.38 min. width of CLHVTPM" |
| chvtpm.2a | "0.38 min. spacing/notch of CLHVTPM" |
| chvtpm.3 | "0 min. enclosure of ((LVnwell not overlapping Var_channel) NOT lvtn) by CLHVTPM" |
| chvtpm.4 | "0 min. enclosure of ((LVnwell overlapping Var_channel) AND hvtp) by CLHVTPM" |

The
{ref}`HVTPM mask page <mask-hvtpm>` reads `CLHVTPM` as the created
`HVTPM` data (inference from the rule names). On that reading the
openings cover low-voltage N-well that does not overlap a varactor
channel, outside `lvtn`, and `hvtp` within low-voltage N-well that does,
rather than drawn `hvtp` alone.

Openings over `hvtp`, as above, and
openings over most low-voltage N-well are both readings; the PDK does
not say which matches the plate, and the checks state what the created
layer must cover, not the operation that makes it.

## Step category

`HVTPM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *implant-block* type: coarse features, a standard-thickness
resist (the implants behind it are keV channel implants), aligned to
the {term}`STI`/active pattern.

## Why this step exists

SKY130 offers three 1.8 V PMOS thresholds — `pfet_01v8`,
`pfet_01v8_lvt`, `pfet_01v8_hvt`[^pdk-07] — because a high-threshold
device is the tool for cutting standby leakage: "High Vth devices are
used on non-critical paths to reduce static leakage power without
incurring a delay penalty. Typical high Vth devices reduce static
leakage by 10 times compared with low Vth devices".[^wiki-mtcmos] The
2001 ITRS treats "Multiple Vt" as a standard feature of the mixed-
signal and low-power roadmap.[^itrs-04]

In a flow where the baseline
PMOS threshold is set by {ref}`LVTPI <step-020>` through the N-well
mask, a *separate* mask is the only way to give some PMOS a different
channel dose; `HVTPM` is that mask. Without it the PDK's `_hvt` PMOS and
high-Vt varactor would not exist, and low-leakage standard-cell
libraries built on them could not be offered.

The varactor shows what the high-Vt implants change. The device page's
e-test table gives the high-Vt option, at the same size, about twice
the minimum capacitance of the low-Vt one (`VC2_CMIN_5_5` 4.197 pF
against `VC_CMIN_5_5` 2.058 pF) and almost the same maximum (20.37 pF
against 20.26 pF). We read the parameter names, because the table's
descriptions do not match them.[^pdk-07]

Published
capacitance–voltage sweeps of the test tile's two options, which the
pad list maps to `cap_var_lvt` and `cap_var_hvt`, show the same
pattern. For 98 devices of 5 × 5 µm, 4.60 pF against 2.41 pF at −1.8 V, on the
low-capacitance side, and 21.04 pF against 21.14 pF at 1.8 V into
accumulation. This is our extraction from the published
measurements.[^raw-data-passives][^raw-data-testtile-pads]

The same pattern holds for an area capacitance of about 1.66
against 0.80 fF/µm² at −1.8 V, over five sizes (our extraction from
the published measurements; the files record no measurement
frequency, temperature, date or
wafer).[^raw-data-passives][^raw-data-testtile-pads]

A larger
depletion capacitance at the same bias means a thinner depletion
layer, consistent with a higher net donor concentration near the well
surface under the high-Vt implants (inference). The data do not show
how {ref}`PCHI <step-023>` and {ref}`PNCHI <step-024>` divide that
effect.

There is no NMOS equivalent: the PDK's
NMOS come in standard, low-Vt and native flavours only,[^pdk-07] so the
high-Vt option is PMOS-only in SKY130.

## How it is typically performed

*An industry-generic implant-block lithography for a 200 mm, 130 nm-era
fab:*

1. **Track preparation.** {term}`HMDS` prime on the oxide surface.
2. **Resist coat.** A conventional positive resist of roughly 1 µm (the
   PDK's nominal "Photoresist thickness" is 1.14 µm)[^pdk-03] is ample
   for keV channel implants.[^txt-02] No {term}`BARC` is needed for 0.38 µm
   features at i-line (inference).[^wiki-litho]
3. **Exposure.** i-line: {term}`k₁ <k1>` ≈ 0.62 for 0.38 µm at {term}`NA` 0.6,[^wiki-litho]
   well within production margins, and ASML describes older exposure
   tools that "migrate to the lithography of choice for less critical
   layers".[^asml-30] We infer an **i-line layer**.
4. **Alignment** to STI. The 0.180 µm enclosure and spacing rules
   (hvtp.3, hvtp.4) define the {term}`overlay` budget between this mask and the
   active pattern that determines which transistor is which.
5. **Develop** in 2.38 % TMAH[^microchemicals-dev] (0.26 N; our
   arithmetic from TMAH's molar mass of 91.15 g/mol,[^wiki-tmah]
   taking the solution's density as about 1 g/mL); optional hard
   bake or UV cure before the
   implant.[^txt-02]
6. **Metrology.** Overlay to STI; {term}`CD` sampled; after-develop inspection.

## Machines typically used

* **{ref}`i-line <machine-i-line-stepper>` {term}`stepper`**, 200 mm (ASML PAS 5500/100–/275, Nikon NSR-2205i,
  Canon FPA-3000i).[^txt-05]
* **{ref}`Coat/develop track <machine-coat-develop-track>`**; **{ref}`overlay tool <machine-cd-sem-overlay-metrology>`**; **{term}`CD-SEM`** for sampling.

## Machines likely used at SkyWater

* **ASML i-line stepper / scanner**
  - *SkyWater says:* lists it.[^skw-01]
  - *Tool exists:* strong.
  - *Runs this step:* assignment to `HVTPM` is an inference from the
    0.38 µm rules.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius**[^skw-01]
  - *Tool exists:* strong for existence.
* **Overlay — KLA 5200/5300/Archer; CD — AMAT Verity/VeraSEM**[^skw-01]
  - *Tool exists:* strong for existence (SkyWater statement).
  - *Runs this step:* use at this mask is an inference.

## Resources required

* **Positive i-line photoresist** ({ref}`lithography materials <material-lithography-materials>`; ~1 µm); suppliers named in SkyWater's
  2021 S-1: Dow, JSR, Tokyo Ohka Kogyo.[^sec-01]
* **HMDS**, **2.38 % (0.26 N) TMAH developer**,[^microchemicals-dev]
  edge-bead remover, {ref}`DI water <material-ultrapure-water>`, {ref}`nitrogen <material-process-gases>`.
* **The HVTPM reticle** (generated from `chvtpm`).[^pdk-06]

## Related steps and cross-references

* Previous: {ref}`LVTPIS <step-021>`.
* Next: {ref}`PCHI <step-023>` and {ref}`PNCHI <step-024>` through
  this resist; strip at {ref}`PCHIS <step-025>`.
* Same module: the baseline PMOS channel implant is
  {ref}`LVTPI <step-020>`.
* Same category: the low-Vt option is defined by
  {ref}`LVTNM <step-014>` (`lvtn`, which may not overlap `hvtp`).
* Mask: {ref}`HVTPM <mask-hvtpm>` — the mask's layers, plates, renders
  and design rules; the previous mask is {ref}`NWM <step-017>`, the
  next mask {ref}`PWBM <step-026>`.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Multiple threshold voltage semiconductor device fabrication technology <patent-gp23113681>` — US 6,238,982 B1 (1999)
* {ref}`Formation of standard voltage threshold and low voltage threshold mosfet devices <patent-gp29999977>` — US 2011/0006372 A1 (2002)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "High Vt PCh*, HVTPM,
  X".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `hvtp` 78:44
  "High-Vt LVPMOS implant"; `chvtpm` 97:0, 97:43, 97:42.[^pdk-06]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — `hvtp` function text; hvtp.1–hvtp.6;
  lvtn.9.[^pdk-periph]
* SkyWater PDK, [*Error Messages*](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) page and `errors.csv` — the
  `chvtpm.1` to `chvtpm.4` checks on the undefined `CLHVTPM`
  layer.[^pdk-errors]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — `pfet_01v8_hvt`;
  `cap_var_hvt`; the varactor e-test table.[^pdk-07]
* SKY130 raw-data repository — C–V sweeps of the test tile's low- and
  high-Vt varactors and the pad list that names them; the capacitances
  quoted here are our extraction.[^raw-data-passives][^raw-data-testtile-pads]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — photoresist
  thickness.[^pdk-03]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the site tool list.[^skw-01]
* [SkyWater, Form S-1 (2021)](<https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>) — photoresist, gas and chemical
  suppliers.[^sec-01]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — one public derivation of
  the `HVTPM` layer from the drawn MPW tape-out layouts, without
  `hvtp`.[^mask-renders]

### High-level understanding

* [Wikipedia, *Multi-threshold CMOS*](<https://en.wikipedia.org/wiki/Multi-threshold_CMOS>) — why several thresholds are offered
  and how they are set.[^wiki-mtcmos]
* [Wikipedia, *Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) — 365 nm i-line and CD =
  k₁·λ/NA.[^wiki-litho]
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

* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — the exposure options it lists by node for
  critical layers.[^itrs-03]
* [ITRS 2001, *Process Integration, Devices, and Structures*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>) — "Multiple
  Vt".[^itrs-04]
* [Wei et al., DAC 1998](<https://doi.org/10.1109/DAC.1998.724521>) — the circuit-level case for a second PMOS/NMOS
  threshold.[^wei-1998]
* [Hook et al. (IBM), *IEEE TED* 2003](<https://doi.org/10.1109/TED.2003.815371>) — threshold shifts from ions
  scattered at an implant-resist edge, the reason for the `hvtp`
  enclosure rules.[^hook-2003]
* [Sheu et al. (TSMC), *IEEE TED* 2006](<https://doi.org/10.1109/TED.2006.884070>) — a compact model of the well-edge
  proximity effect.[^sheu-2006]
* [Drennan, Kniffin and Locascio, CICC 2006](<https://doi.org/10.1109/CICC.2006.320869>) — designer-side consequences
  of proximity effects for analogue layout.[^drennan-2006]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — k₁ and
  resist-profile fundamentals behind the i-line assignment.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]
* [Helm and Zhou (Round Rock Research), US 2011/0006372](<https://patents.google.com/patent/US20110006372A1/en>) — multiple
  thresholds made with masked Vt-adjust implants.[^pat-vt-rrr]
* [Krivokapic and Milic (AMD), US 6,238,982](<https://patents.google.com/patent/US6238982B1/en>) — multiple thresholds set by
  gate length, with a laterally doped channel implant self-aligned to
  the gate pillars.[^pat-vt-amd]
* [Taur and Ning, *Fundamentals of Modern VLSI Devices*](<https://doi.org/10.1017/CBO9781139195065>) — threshold
  voltage as a function of channel doping, what the extra mask
  buys.[^taur-2009]

## Open questions

* **HVTRM mask.** The PDK mask table also flags "HLow VT PCh Radio*,
  HVTRM" as used in SKY130,[^pdk-05] with a drawn layer `hvtr` (GDS
  18:20, "High-Vt RF transistor implant").[^pdk-06] The PDK does not
  say whether that mask is absent from the baseline flow, folded into
  `HVTPM`, or belongs to an option; this reference describes no
  separate step for it.
* **Reticle polarity.** Whether the plate is opened over drawn `hvtp`,
  as this page reads the layer description, or over low-voltage
  N-well outside `lvtn`, as the {ref}`HVTPM mask page <mask-hvtpm>`
  reads the `chvtpm` checks, is not stated in the PDK.[^pdk-periph] The
  Error Messages page does not define `CLHVTPM`.[^pdk-errors]
* **Resist thickness and exposure tool.** Both are inferred.

<!-- footnotes -->

[^wiki-tmah]: Wikipedia, *Tetramethylammonium hydroxide*.
    <https://en.wikipedia.org/wiki/Tetramethylammonium_hydroxide>
[^microchemicals-dev]: MicroChemicals, *Development of photoresists*,
    application note.
    <https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^wiki-mtcmos]: Wikipedia, *Multi-threshold CMOS*.
    <https://en.wikipedia.org/wiki/Multi-threshold_CMOS>
[^itrs-04]: International Technology Roadmap for Semiconductors, *2001
    Edition: Process Integration, Devices, and Structures*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021, accessed
    2026-09-13. <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wei-1998]: L. Wei, Z. Chen, M. Johnson, K. Roy and V. De, "Design and
    optimization of low voltage high performance dual threshold CMOS
    circuits", *Proceedings of the 35th Design Automation Conference*,
    pp. 489–494 (1998). <https://doi.org/10.1109/DAC.1998.724521>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^sheu-2006]: Y.-M. Sheu, K.-W. Su, S. Tian, S.-J. Yang, C.-C. Wang,
    M.-J. Chen and S. Liu, "Modeling the Well-Edge Proximity Effect in
    Highly Scaled MOSFETs", *IEEE Transactions on Electron Devices*
    **53**(11), 2792–2798 (2006).
    <https://doi.org/10.1109/TED.2006.884070>
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
[^pat-vt-rrr]: M. Helm and X. Zhou (Round Rock Research), *Formation of
    standard voltage threshold and low voltage threshold MOSFET
    devices*, US 2011/0006372 A1, published 2011-01-13 (priority
    2002-07-08). <https://patents.google.com/patent/US20110006372A1/en>
[^pat-vt-amd]: Z. Krivokapic and O. Milic (AMD), *Multiple threshold
    voltage semiconductor device fabrication technology*, US 6,238,982
    B1, granted 2001-05-29.
    <https://patents.google.com/patent/US6238982B1/en>
[^taur-2009]: Y. Taur and T. H. Ning, *Fundamentals of Modern VLSI
    Devices*, 2nd ed., Cambridge University Press, 2009, ISBN
    978-0-521-83294-6. <https://doi.org/10.1017/CBO9781139195065>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md`, `masks.html`, the run pages `mpw-001.html` to
    `mpw-008.html`, and for each run × mask directory the page,
    `job.json`, `result.json` and per-die slot JSON files, retrieved
    2026-09-14. Run pages are `mpw-00N.html`; each render's page is
    `<run>_<mask>/<run>_<mask>.html` (for example
    `mpw-001_TUNM/mpw-001_TUNM.html`). Rendered from the public shuttle
    repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^raw-data-passives]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the poly, diffusion
    and well resistors, MiM capacitors, varactors and bipolar
    transistors of the test tile, IC-CAP `.mdm` files in
    `sky130_fd_pr/cells/unsorted/`, `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells/unsorted>
