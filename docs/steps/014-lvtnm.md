(step-014)=
# Step 014 — LVTNM: Low Vt NMOS mask

| | |
|---|---|
| **Step number** | 14 of 171[^steps-sheet] |
| **Step code** | `LVTNM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | {term}`FEOL` — wells and channel implants |
| **Previous step** | {ref}`NS19 <step-013>` |
| **Next step** | {ref}`LVTNI <step-015>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** coats the wafer with resist and opens windows for the
  {ref}`LVTNI <step-015>` implant.
* **Why:** separates the low-Vt (and native/SONOS) channels from the
  standard ones, giving SKY130 its multiple threshold-voltage options.
* **Public numbers:** minimum `lvtn` width and space 0.380 µm (lvtn.1a,
  lvtn.2); minimum enclosure of a gate 0.180 µm
  (lvtn.4b).[^pdk-periph]
* **Likely SkyWater tool:** ASML i-line stepper or scanner — strong
  (existence); inference (assignment).[^skw-01]
* **Not public:** which of the two competing reticle-polarity readings
  is correct (→ Open questions).
:::

## What this step is

`LVTNM` is the third mask of the flow and the first of the well and
channel-implant module. The wafer arriving from {ref}`NS19 <step-013>`
is planar: oxide-filled isolation trenches stand slightly proud of
active islands covered, we infer, only by the thin pad oxide grown at
{ref}`BOX <step-002>` (its fate after {ref}`NS19 <step-013>` is not
public). `LVTNM` coats this surface with photoresist, exposes it through
the *low-Vt N-channel mask* {term}`reticle` and develops it, leaving resist
windows through which the {ref}`LVTNI <step-015>` implant is placed. The
resist is removed at {ref}`LVTNIS <step-016>`.

:::{figure} /_static/figures/wells-014-lvtnm.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step the surface is flat apart from the filled trench, whose oxide stands slightly proud of the thin pad oxide over the two active areas. After it a block of photoresist covers the right-hand active area and the right half of the trench, and the left-hand active area lies in an open window.
:width: 560px
:name: fig-wells-014-lvtnm

Before, the wafer as NS19 leaves it; after, resist over the right of the slice and a window over the left. The PDK's mask table lists "Low Vt Nch*, LVTNM" as used in SKY130.[^pdk-05] Which regions the plate opens is not public (see *Open questions*), so the window is drawn over an NMOS area and the resist over a PMOS area only so that both sides of a resist edge can be seen; no layout is being shown, and the slice is read as an NMOS beside a high-Vt PMOS. The pad oxide is drawn as still in place, which the page infers, and the liner oxide in the trench is drawn faded. Not to scale.
:::

The PDK's mask table lists "Low Vt Nch*, LVTNM" as a mask used in
SKY130.[^pdk-05] The drawn layer is `lvtn` (GDS 125:44, "Low-Vt NMOS
device") and the generated mask layer is `clvtnm` (GDS 25:0, "Low Vt Nch
mask"), which also carries "mask add" (25:43) and "mask drop" (25:42)
purposes.[^pdk-06] The existence of add/drop purposes shows that the
reticle is *derived* from the drawn layer by Boolean operations in the
mask-generation flow rather than being a copy of it.

### Key numbers

The periphery design rules state the layer's function directly: `lvtn`
rules "Define regions to block Vt adjust implant for low Vt LV
PMOS/NMOS, SONOS FETs and Native NMOS".[^pdk-periph] The rule values are
coarse for a 130 nm process:

| Rule[^pdk-periph] | Constrains | Value |
|---|---|---:|
| lvtn.1a | minimum width | 0.380 µm |
| lvtn.2 | minimum space | 0.380 µm |
| lvtn.4b | minimum enclosure of a gate by `lvtn` | 0.180 µm |
| lvtn.3a | minimum spacing to a gate | 0.180 µm |
| lvtn.3b | spacing to a PMOS along the source/drain direction | 0.235 µm |
| lvtn.9 | no overlap with `hvtp` | 0.380 µm spacing |
| lvtn.10 | enclosure by `nwell` when used inside an N-well | 0.380 µm |
| lvtn.13 | minimum area | 0.265 µm² |

A separate poly rule sets the minimum channel length of a PMOS
overlapping `lvtn` at 0.350 µm (poly.1b). This is much longer than the
0.150 µm baseline, which is consistent with a device whose channel
doping has been reduced and which therefore needs more length to
control short-channel effects.[^pdk-periph]

## Step category

`LVTNM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *implant-block* type: the image quality that matters is
placement relative to the active pattern and adequate resist thickness,
not minimum feature size.

It aligns to the {term}`STI`/active pattern printed at
{ref}`FOM <step-004>` and etched at {ref}`STIE <step-006>`, which at
this point is, we infer, the only pattern on the wafer.

## Why this step exists

SKY130 is a multi-threshold process. The device list offers, at 1.8 V, a
standard NMOS (`nfet_01v8`), a low-Vt NMOS (`nfet_01v8_lvt`), a standard
PMOS, a low-Vt PMOS (`pfet_01v8_lvt`) and a high-Vt PMOS
(`pfet_01v8_hvt`), together with native NMOS devices (`nfet_03v3_nvt`,
`nfet_05v0_nvt`) that are "constructed by blocking out all VT
implants".[^pdk-07]

The reason for offering several thresholds is the
familiar speed/leakage trade: "Low Vth devices switch faster, and are
therefore useful on critical delay paths to minimize clock periods. The
penalty is that low Vth devices have substantially higher static leakage
power", and the threshold "is adjusted by altering the concentration of
dopant atoms in the channel region beneath the gate
oxide".[^wiki-mtcmos]

The 2001 ITRS states that "multiple
threshold-voltage and multiple-oxide-thickness devices also need to be
available in order to enable more comprehensive circuit/system-level
power/performance optimization".[^itrs-04]

`LVTNM` is the mask that distinguishes the low-threshold (and, per the
rule text, the native and {term}`SONOS`) channels from the standard ones. The
PDK's `lvtn` rule heading says the layer *blocks* a Vt-adjust implant.

That wording, and the fact that the same layer serves low-Vt NMOS,
low-Vt PMOS and native NMOS, lead us to infer that the physical reticle
is generated so resist *covers* the drawn `lvtn` regions while the
{ref}`LVTNI <step-015>` implant goes into the rest of the wafer. These
are devices whose thresholds could not all be lowered by a single
dopant species implanted *into* them. We infer, alternatively, that
Boolean combinations with `nwell` and other layers produce separate
NMOS and PMOS variants of the opening. Which reading is right is not
public; see *Open questions*.

Without this mask every 1.8 V NMOS would have the same threshold, and
the low-Vt, native and SONOS device options in the PDK would not exist.

The published test-tile measurements show the low-Vt devices of both
polarities with lower thresholds than their standard counterparts. At
7/8 µm we extract 0.432 V for `nfet_01v8_lvt` against 0.534 V for
`nfet_01v8`, and a magnitude of 0.672 V for `pfet_01v8_lvt` against
1.065 V for `pfet_01v8` (maximum-transconductance extrapolation at
|V_DS| = 0.1 V, less half the drain bias; our extraction from the
published measurements). The PMOS shift is thus about four times the
NMOS shift, as between the PDK's e-test nominals (0.399 V and
0.101 V).[^raw-data-lv-mosfets][^pdk-07] Measured thresholds do not
show whether the reticle covers or opens the drawn regions, nor how
many implants produce the two shifts.

## How it is typically performed

*An industry-generic implant-block lithography sequence for a 200 mm,
130 nm-era fab:*

1. **Surface preparation.** Dehydration bake and vapour {term}`HMDS` prime on
   the track; the surface is oxide everywhere (pad oxide on active,
   trench oxide on field), which primes well.
2. **Resist coat.** A single-layer positive resist.

   The {ref}`LVTNI <step-015>` implant is a channel-type implant at
   tens of keV, which a resist of about 1 µm stops with a wide margin
   (industry-typical).[^txt-02] The PDK's own assumptions table gives a
   nominal "Photoresist thickness" of 1.14 µm,[^pdk-03] so we take that
   as the plausible order of thickness. No {term}`BARC` is needed for
   0.38 µm features at i-line (inference).[^wiki-litho]
3. **Exposure.** The 0.380 µm minimum width and space[^pdk-periph] are
   comfortably within reach of an i-line (365 nm) {term}`stepper`.

   At {term}`NA` 0.6 the process factor is {term}`k₁ <k1>` = 0.38 × 0.6
   / 0.365 ≈ 0.62, well above the "0.4 for production"
   level.[^wiki-litho] ASML describes older exposure tools that "migrate
   to the lithography of choice for less critical layers".[^asml-30] We
   therefore infer that `LVTNM` is an **i-line layer**, like the other
   implant-block masks of this module and unlike {ref}`FOM <step-004>`.
4. **Alignment.** To the STI pattern. The tightest coupling of this
   layer is to the *future* gate: the 0.180 µm enclosure of gate by
   `lvtn` (lvtn.4b) means both this mask and the later poly mask must
   register to the same active reference within a fraction of that
   value.
5. **Develop** in aqueous TMAH,[^txt-02] rinse, dry; a hard bake or UV
   cure may follow to stabilise the resist against the implant (industry
   practice).[^txt-02]
6. **Inspection.** {term}`Overlay <overlay>` measured on box-in-box targets against the
   STI layer; {term}`CD` checked loosely; after-develop inspection for defects.

## Machines typically used

* **{ref}`i-line stepper <machine-i-line-stepper>`**, 200 mm: ASML PAS 5500/100–/275 series, Nikon
  NSR-2205i, Canon FPA-3000i[^txt-05] (see the category page).
* **{ref}`Coat/develop track <machine-coat-develop-track>`** linked to the stepper (TEL, DNS/SCREEN,
  SVG/ASML, Sokudo).
* **{ref}`Overlay metrology <machine-cd-sem-overlay-metrology>`** (KLA-Tencor 5xxx/Archer class) and a {term}`CD-SEM` for
  periodic checks.

## Machines likely used at SkyWater

* **ASML i-line stepper / i-line scanner**
  - *SkyWater says:* lists "ASML I-line stepper" and "ASML I-line
    scanner".[^skw-01]
  - *Tool exists:* strong for the existence of the tools.
  - *Runs this step:* the assignment of `LVTNM` to the i-line tools is
    an inference from the 0.380 µm design rules, not a SkyWater
    statement.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius**[^skw-01]
  - *Tool exists:* strong for existence.
  - *Runs this step:* which track serves which exposure tool is not
    public.
* **Overlay — KLA 5200/5300/Archer; CD — AMAT Verity/VeraSEM**[^skw-01]
  - *Tool exists:* strong for existence (SkyWater statement).
  - *Runs this step:* use at this mask is an inference.

## Resources required

* **Positive i-line (DNQ/novolac) photoresist** ({ref}`lithography materials <material-lithography-materials>`), about 1 µm thick
  (inferred above; industry-typical); SkyWater's 2021 S-1 names The Dow
  Chemical Company, JSR Corporation and Tokyo Ohka Kogyo America as
  photoresist suppliers.[^sec-01]
* **HMDS** adhesion promoter; **2.38 % (0.26 N) TMAH developer**, the industry
  standard;[^txt-02] edge-bead remover and rinse solvents; {ref}`DI water <material-ultrapure-water>` and
  {ref}`nitrogen <material-process-gases>`.
* **The LVTNM reticle** — a chrome-on-quartz plate generated from the
  `clvtnm` layer with its add/drop corrections.[^pdk-06]

## Related steps and cross-references

* Previous: {ref}`NS19 <step-013>` (nitride strip; leaves the pad
  oxide that this module's implants pass through).
* Next: {ref}`LVTNI <step-015>` (the implant through this mask), then
  {ref}`LVTNIS <step-016>` (resist strip).
* Same module: the other Vt-flavour mask is {ref}`HVTPM <step-022>`
  (`hvtp`, which must not overlap `lvtn`, rule lvtn.9).
* Compare: {ref}`NCHI <step-045>` — the baseline N-channel
  implant of the 1.8 V devices, placed later under the low-voltage
  oxide mask {ref}`LVOM <step-044>` (a different category, in a
  different module).
* Feeds: all of this module's implants are activated at
  {ref}`RTAI <step-034>`.
* Mask: {ref}`LVTNM <mask-lvtnm>` — the mask's layers, plates, renders
  and design rules; the previous mask is {ref}`DNM <step-007>`, the
  next mask {ref}`NWM <step-017>`.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`High aspect ratio photolithographic method for high energy implantation <patent-gp23358573>` — US 6,576,405 B1 (1999)
* {ref}`Formation of standard voltage threshold and low voltage threshold mosfet devices <patent-gp29999977>` — US 2011/0006372 A1 (2002)
* {ref}`Method of adjusting the threshold voltage of a mosfet <patent-gp32681640>` — US 6,764,890 B1 (2003)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Low Vt Nch*, LVTNM,
  X".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `lvtn` 125:44;
  `clvtnm` 25:0, 25:43, 25:42.[^pdk-06]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — `lvtn` function text; lvtn.1a,
  lvtn.2, lvtn.3a, lvtn.3b, lvtn.4b, lvtn.9, lvtn.10, lvtn.13;
  poly.1b.[^pdk-periph]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — `nfet_01v8_lvt`, `pfet_01v8_lvt`,
  `pfet_01v8_hvt`, native NMOS "constructed by blocking out all VT
  implants".[^pdk-07]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — "Photoresist thickness"
  1.14 µm.[^pdk-03]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — ASML i-line stepper and
  scanner; tracks; overlay and CD tools.[^skw-01]
* [SkyWater, Form S-1 (2021)](<https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>) — photoresist suppliers.[^sec-01]
* [SKY130 raw-data repository, 1.8 V transistor files](<https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>) — low-Vt and
  standard thresholds of both polarities (our
  extraction).[^raw-data-lv-mosfets]

### High-level understanding

* [Wikipedia, *Multi-threshold CMOS*](<https://en.wikipedia.org/wiki/Multi-threshold_CMOS>) — why several thresholds are offered
  and how they are set.[^wiki-mtcmos]
* [Wikipedia, *Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) — 365 nm i-line, CD =
  k₁·λ/NA.[^wiki-litho]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) —
  lithography and implant-masking chapters.[^txt-02]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) — lithography
  tools of the 0.25–0.13 µm generations.[^txt-05]

### Deep dive

* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — the exposure options it lists by node for
  critical layers.[^itrs-03]
* [ITRS 2001, *Process Integration, Devices, and Structures*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>) — "multiple
  threshold-voltage and multiple-oxide-thickness devices".[^itrs-04]
* [Helm and Zhou (Round Rock Research), US 2011/0006372](<https://patents.google.com/patent/US20110006372A1/en>) — an example of
  low-Vt NMOS and PMOS defined by masked Vt-adjust
  implants.[^pat-vt-rrr]
* [Hook et al. (IBM), *IEEE TED* 2003](<https://doi.org/10.1109/TED.2003.815371>) — how ions scattered from an
  implant-resist edge shift the threshold of nearby transistors, the
  reason implant layers carry enclosure rules.[^hook-2003]
* [Sheu et al. (TSMC), *IEEE TED* 2006](<https://doi.org/10.1109/TED.2006.884070>) — a compact model of the well-edge
  proximity effect for layout-dependent threshold shifts.[^sheu-2006]
* [Drennan, Kniffin and Locascio, CICC 2006](<https://doi.org/10.1109/CICC.2006.320869>) — what proximity effects mean
  for analogue designers placing devices near implant
  edges.[^drennan-2006]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — k₁, resist
  profiles and thick-resist imaging, the optics behind the i-line
  assignment.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]
* [Taur and Ning, *Fundamentals of Modern VLSI Devices*](<https://doi.org/10.1017/CBO9781139195065>) — threshold
  voltage as a function of channel doping, the physics a Vt-adjust mask
  exists to exploit.[^taur-2009]
* [Lee et al. (Genus), IIT 1996](<https://doi.org/10.1109/IIT.1996.586180>) — outgassing of thick implant resists
  during implantation, one reason to hard-bake or UV-cure the
  resist.[^lee-1996]
* [Buffat and Adams (Zilog), US 6,576,405](<https://patents.google.com/patent/US6576405B1/en>) — what a resist must do when
  the implant behind it is MeV-class, for contrast with this keV
  layer.[^pat-resist-zilog]

## Open questions

* **Reticle polarity.** The PDK says `lvtn` *blocks* a Vt-adjust
  implant, while this reference describes an implant through the
  `LVTNM` resist ({ref}`LVTNI <step-015>`).

  Whether the reticle opens *over* `lvtn` (and `LVTNI` is a
  {term}`counter-doping` implant) or *everywhere except* `lvtn` (and
  `LVTNI` is the baseline Vt-adjust implant that low-Vt devices skip)
  cannot be settled from public data. The "mask add/drop" purposes show
  only that the reticle is generated, not how. One public derivation
  from the drawn tape-out data renders the plate as `lvtn` OR (`nwell`
  AND (`hvtp` OR `areaid.ce`)), with `lvtn` appearing positively, but
  its note contradicts the expression and it settles nothing; see
  {ref}`LVTNM <mask-lvtnm>` and {ref}`masks-derivations`.[^mask-renders]
* **Reticle count.** Whether separate NMOS and PMOS reticles are
  derived from the one drawn layer, or whether `nfet_01v8_lvt` and
  `pfet_01v8_lvt` share a single physical mask, is not public.
* **Resist and exposure details.** Resist thickness, exposure tool and
  the use of a resist-hardening step are inferred from the design
  rules and general practice.

<!-- footnotes -->

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
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^wiki-mtcmos]: Wikipedia, *Multi-threshold CMOS*.
    <https://en.wikipedia.org/wiki/Multi-threshold_CMOS>
[^itrs-04]: International Technology Roadmap for Semiconductors, *2001
    Edition: Process Integration, Devices, and Structures*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
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
[^pat-vt-rrr]: M. Helm and X. Zhou (Round Rock Research), *Formation of
    standard voltage threshold and low voltage threshold MOSFET
    devices*, US 2011/0006372 A1, published 2011-01-13 (priority
    2002-07-08). <https://patents.google.com/patent/US20110006372A1/en>
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
[^taur-2009]: Y. Taur and T. H. Ning, *Fundamentals of Modern VLSI
    Devices*, 2nd ed., Cambridge University Press, 2009, ISBN
    978-0-521-83294-6. <https://doi.org/10.1017/CBO9781139195065>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^pat-resist-zilog]: S. J. Buffat and J. L. Adams (Zilog), *High aspect
    ratio photolithographic method for high energy implantation*, US
    6,576,405 B1, granted 2003-06-10.
    <https://patents.google.com/patent/US6576405B1/en>
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
[^raw-data-lv-mosfets]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the 1.8 V
    transistors, IC-CAP `.mdm` files in `sky130_fd_pr/cells/`
    (`nfet_01v8`, `nfet_01v8_lvt`, `pfet_01v8`, `pfet_01v8_hvt`,
    `pfet_01v8_lvt`), `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
