(step-023)=
# Step 023 — PCHI: P-channel implant

| | |
|---|---|
| **Step number** | 23 of 171[^steps-sheet] |
| **Step code** | `PCHI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | {term}`FEOL` — wells and channel implants |
| **Previous step** | {ref}`HVTPM <step-022>` |
| **Next step** | {ref}`PNCHI <step-024>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** adds a high-Vt channel dose through the `HVTPM` resist, on
  top of the baseline PMOS implant.
* **Why:** raises |Vt| for low-leakage PMOS; split into two implants
  (with `PNCHI`) to shape the channel profile without hurting
  mobility.
* **Public numbers:** measured threshold 1.124 V (`pfet_01v8_hvt`)
  against 1.065 V (`pfet_01v8`) at 7/8 µm (our
  extraction).[^raw-data-lv-mosfets]
* **Likely SkyWater tool:** Axcelis 8250 medium-current — strong
  (tool); inference (assignment).[^skw-01]
* **Not public:** the actual species, energy and dose (→ Open
  questions).
:::

## What this step is

`PCHI` is the first of two channel implants placed through the resist
windows of {ref}`HVTPM <step-022>`, the high-Vt P-channel mask. On this
page's reading it adds dopant to the surface of the N-well under the
future gates of the PMOS transistors drawn with the `hvtp` layer, on
top of the baseline PMOS channel doping that, we infer, every N-well
received at {ref}`LVTPI <step-020>`.

The {ref}`HVTPM <step-022>` page
sets out a second reading of the `chvtpm` checks and of the public
render derivation, under which the opening covers low-voltage N-well
outside `lvtn` and this implant reaches every standard PMOS as well.
Which is right is not public. Its companion, {ref}`PNCHI <step-024>`, is
described in this reference as a BF₂ implant (an inference, set out on
that page); the species of `PCHI` is discussed below. The resist is stripped at
{ref}`PCHIS <step-025>`.

:::{figure} /_static/figures/wells-023-pchi.svg
:alt: One cross-section of the wafer. Resist covers the left-hand part of the drawing and the PMOS active area, with its thin hatched surface band inside the N-well, lies in a window on which arrows come down. The drawing is the same as the state before the step.
:width: 560px
:name: fig-wells-023-pchi

At PCHI a light channel implant goes through the HVTPM window into the PMOS channel area; the drawing is the state at this step, which is the same as before it, the surface band now standing for both of the channel implants it has received. On the page's reading PCHI adds dopant to the PMOS channel, on top of the dose the page infers LVTPI gave it; its species, energy and dose are not public, and no public source gives the depth of either implant, so the drawing does not separate them. The arrows are drawn vertical because the tilt is not public. The fill oxide is drawn but not labelled; the NMOS channel implant and the liner oxide are drawn faded. Not to scale.
:::

The PDK describes the `hvtp` region as the "Vt adjust implant region for
high Vt LV PMOS"[^pdk-periph] and the resulting device as the "1.8V
high-VT PMOS FET", `pfet_01v8_hvt`, modelled for V_DS and V_GS from 0 to
−1.95 V.[^pdk-07] The same implant, applied to a varactor, gives
`cap_var_hvt`, the "high VT PMOS device option".[^pdk-07]

## Step category

`PCHI` is an {ref}`Ion implantation <category-implant>` step of the
*{term}`threshold-adjust <threshold-adjust implant>`* class: light dose, tens of keV, medium-current
tool, through the pad/{term}`screen oxide` (category page). It is the third
threshold implant of the module after {ref}`LVTNI <step-015>` and
{ref}`LVTPI <step-020>`.

## Why this step exists

The threshold of a PMOS in an N-well rises in magnitude with the n-type
doping at the surface of the channel.[^wiki-vt][^wiki-mtcmos] `LVTPI`
sets that doping for the standard PMOS; `PCHI` and `PNCHI` add to it
where a higher |{term}`Vt`| is wanted. The motive is leakage: "Typical high Vth
devices reduce static leakage by 10 times compared with low Vth
devices",[^wiki-mtcmos] and a 130 nm low-power process needs a high-Vt
option to make standby-current targets in cells that are not
speed-critical.[^itrs-04][^wei-1998] The PDK's inverter-delay tables for
`nfet_01v8`/`pfet_01v8_hvt` combinations[^pdk-07] quantify the speed
that is traded for it.

The published test-tile measurements include both devices at the PDK's
e-test geometries. By maximum-transconductance extrapolation at
V_DS = −0.1 V, less half the drain bias, we extract threshold magnitudes
of 1.124 V for `pfet_01v8_hvt` against 1.065 V for `pfet_01v8` at
7/8 µm (+0.059 V) and 0.917 V against 0.798 V at 7/0.15 µm
(+0.119 V).[^raw-data-lv-mosfets]

At 7/0.15 µm the drain current at V_GS = V_DS = −1.8 V falls from
1.28 mA to 0.94 mA (our extraction from the published measurements).
The PDK's e-test nominals differ by +0.057 V and +0.107 V, and their
currents fall from 1.347 mA to 1.003 mA.[^raw-data-lv-mosfets][^pdk-07]

A second, more physical reason to split the high-Vt adjust into two
implants is profile shaping. A single shallow implant that raises the
surface concentration enough to move the threshold also raises the body
effect and degrades mobility.

Pairing a deeper implant that controls
short-channel behaviour with a shallower one that sets Vt is the
"retrograde channel" approach that ITRS 2001 tabulates ("Retrograde
channel depth (nm)" 21–30 nm for the 2001 high- performance
node).[^itrs-01] Thompson, Packan and Bohr analysed the same approach
for its drive-current trade-offs.[^thompson-1996] We infer, without public
confirmation, that `PCHI` and `PNCHI` divide these roles between them.

The high-Vt varactor shows the two implants from another side.
{ref}`HVTPM <step-022>` sets the published capacitance–voltage sweeps
of the test tile's two varactor options, which the pad list maps to
`cap_var_lvt` and `cap_var_hvt`, beside each other.

For 98 devices of
5 × 5 µm the high-Vt option measures 4.60 pF against 2.41 pF at
−1.8 V, on the low-capacitance side, and 21.04 pF against 21.14 pF at
1.8 V, into accumulation. This is our extraction from the published
measurements; the files record no measurement frequency, temperature,
date or wafer.[^raw-data-passives][^raw-data-testtile-pads]

We read the
larger depletion capacitance as a higher net donor concentration near
the well surface under the high-Vt implants taken together. The data
do not show how `PCHI` and `PNCHI` divide it (inference).

## How it is typically performed

*An industry-generic high-Vt PMOS channel implant for a 200 mm,
130 nm-era fab.* SKY130's species, energy and dose are not public.

* **Species.** To raise |Vt| of a surface-channel PMOS the added dopant
  is n-type — arsenic (shallow, slow-diffusing) or phosphorus (deeper
  for a given energy).[^txt-04]

  The Round Rock/Micron multi-Vt patent
  uses "an implant of Arsenic" for exactly this purpose.[^pat-vt-rrr] An
  indium implant, which is p-type, is used for *NMOS* retrograde
  channels[^shahidi-1993] and is not a candidate here. Arsenic is the
  more plausible species, and is on the public species list of
  SkyWater's medium-current tool.[^skw-01]
* **Energy and dose.** Tens of keV; of order 10¹²–10¹³ cm⁻² (category
  page).

  The boron-side analogues in an LSI Logic patent are "doses
  between 1×10¹² and 1×10¹³ atoms/cm²" at 50–100 keV.[^pat-vt-lsi] A
  high-Vt adjust is by definition a *small* increment over the baseline,
  so its dose is at the low end of the range — a few 10¹² cm⁻² is
  illustrative.
* **Tilt and twist.** 7° with twist.[^wiki-implant][^txt-02]
* **Screen oxide.** The pad oxide randomises the beam and traps recoils;
  the thickness the Cypress {term}`SONOS` patent gives it — that patent
  may still be in force — is in the collapsed note below this list.
* **Charge control.** Electron shower on a cooled electrostatic chuck
  (SkyWater lists "ESC chuck, E shower").[^skw-01]
* **Anneal.** None until {ref}`RTAI <step-034>`.
* **Monitoring.** Thermal-wave on product; {term}`sheet resistance` on monitors
  after a monitor anneal.

:::{dropdown} From a patent shown as in force (US 8,796,098; estimated expiry 2034-02-26) — open to read
The Cypress {term}`SONOS` patent gives the pad oxide as
10–20 nm.[^pat-04]
:::

## Machines typically used

* **{ref}`Medium-current implanter <machine-medium-current-implanter>`** with serial end station: Axcelis (Eaton)
  8250/8250HT ("3keV to 750keV", "between 4µA and
  3,500µA"),[^axcelis-8250] Varian E220/E500, Nissin (category page).
* **{ref}`Thermal-wave <machine-sheet-resistance-metrology>`** dose monitor.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current**
  - *SkyWater says:* lists "B11, BF2, As, ESC chuck, E shower, 1e11 to
    1e14, 0-60 deg tilt".[^skw-01]
  - *Tool exists:* strong — arsenic and the dose window match.
  - *Runs this step:* inference.
* **Axcelis GSD implanters**
  - *SkyWater says:* lists either GSD entry, "High current/energy" or
    "Hi dose".[^skw-01]
  - *Tool exists:* strong for existence; is capable, but these are the
    well and source/drain workhorses.
  - *Runs this step:* weak — which entry would serve is not stated.

## Resources required

* **{ref}`Arsine <material-dopant-sources>` (AsH₃)** or **phosphine (PH₃)** source gas.[^wiki-implant]
* Support gases, cryopump and ion-source consumables, {ref}`monitor wafers <material-substrates>`
  (category page).
* No new resist: the {ref}`HVTPM <step-022>` resist is reused for
  {ref}`PNCHI <step-024>`.

## Related steps and cross-references

* Previous: {ref}`HVTPM <step-022>` (mask).
* Next: {ref}`PNCHI <step-024>` (second implant through the same
  resist), then {ref}`PCHIS <step-025>` (strip).
* Same category: baseline PMOS channel — {ref}`LVTPI <step-020>`;
  low-Vt option via {ref}`LVTNM <step-014>`.
* Feeds: activated at {ref}`RTAI <step-034>`.
* Category page: {ref}`Ion implantation <category-implant>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Method of forming retrograde well structures and punch-through barriers using low energy implants <patent-gp25087511>` — US 5,963,801 A (1996)
* {ref}`Formation of standard voltage threshold and low voltage threshold mosfet devices <patent-gp29999977>` — US 2011/0006372 A1 (2002)

:::{dropdown} 1 family in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 8,796,098 B1 <patent-gp51229009>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the site tool list.[^skw-01]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — `pfet_01v8_hvt`, `cap_var_hvt`,
  inverter delay tables.[^pdk-07]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — `hvtp` function text.[^pdk-periph]
* [Semiconductor Online, *8250HT Medium Current Ion Implanter*](<https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>) — the
  Eaton/Axcelis 8250HT energy and beam-current ranges.[^axcelis-8250]
* [SKY130 raw-data repository, 1.8 V transistor files](<https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>) — `pfet_01v8_hvt`
  and `pfet_01v8` thresholds and drain currents side by side (our
  extraction).[^raw-data-lv-mosfets]
* SKY130 raw-data repository, varactor C–V files and test-tile pad
  documentation — the low- and high-Vt varactors and the pad list that
  names them; the capacitances quoted here are our
  extraction.[^raw-data-passives][^raw-data-testtile-pads]

:::{dropdown} From a patent shown as in force (US 8,796,098; estimated expiry 2034-02-26) — open to read
* Ramkumar et al. (Cypress), US 8,796,098 — pad oxide under the
  implants.[^pat-04]
:::

### High-level understanding

* [Wikipedia, *Ion implantation*](<https://en.wikipedia.org/wiki/Ion_implantation>) — energies, sources, {term}`channelling` and
  tilt in one page.[^wiki-implant]
* [Wikipedia, *Threshold voltage*](<https://en.wikipedia.org/wiki/Threshold_voltage>) — the body-effect parameter containing
  the channel doping.[^wiki-vt]
* [Wikipedia, *Multi-threshold CMOS*](<https://en.wikipedia.org/wiki/Multi-threshold_CMOS>) — why several thresholds are offered
  and how they are set.[^wiki-mtcmos]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) —
  lithography, resist stripping, wafer cleaning and implantation
  chapters.[^txt-02]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 3](<https://openlibrary.org/isbn/9780961672157>) — channel
  engineering of submicron PMOS.[^txt-04]

### Deep dive

* [ITRS 2001, *Front End Processes*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>) — Table 51 retrograde channel
  depth.[^itrs-01]
* [ITRS 2001, *Process Integration, Devices, and Structures*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>) — multiple
  threshold-voltage devices as a roadmap requirement.[^itrs-04]
* [Thompson, Packan and Bohr (Intel), VLSI 1996](<https://doi.org/10.1109/VLSIT.1996.507830>) — drive-current
  trade-offs of super-steep retrograde channels.[^thompson-1996]
* [Helm and Zhou (Round Rock Research), US 2011/0006372](<https://patents.google.com/patent/US20110006372A1/en>) — low-Vt NMOS and
  PMOS defined by masked Vt-adjust implants, including a {term}`counter-doped <counter-doping>`
  channel.[^pat-vt-rrr]
* [Aronowitz, Khan and Kimball (LSI Logic), US 5,963,801](<https://patents.google.com/patent/US5963801A/en>) — Vt-adjust
  boron at 1e12–1e13 cm⁻² and 50–100 keV, chained {term}`punch-through`
  barriers, and a well anneal "at approximately 900° C. in a neutral
  ambient such as nitrogen for approximately 30 minutes" (the patent does
  not name the tool).[^pat-vt-lsi]
* [Shahidi et al. (IBM), *IEEE EDL* 1993](<https://doi.org/10.1109/55.225595>) — indium channel implants for
  steep retrograde NMOS channels.[^shahidi-1993]
* [Wei et al., DAC 1998](<https://doi.org/10.1109/DAC.1998.724521>) — the circuit-level case for a second threshold
  voltage.[^wei-1998]
* [Taur et al., *Proc. IEEE* 1997](<https://doi.org/10.1109/5.573737>) — super-steep retrograde channels and
  multiple thresholds at 0.1 µm.[^taur-1997]
* [MacPherson, *Appl. Phys. Lett.* 1971](<https://doi.org/10.1063/1.1653513>) — the original
  threshold-adjust-by-implantation paper.[^macpherson-1971]
* [Rafferty et al. (AT&T), IEDM 1993](<https://doi.org/10.1109/IEDM.1993.347345>) — how implant damage and the anneal
  reshape the channel profile.[^rafferty-1993]
* [Taur and Ning, *Fundamentals of Modern VLSI Devices*](<https://doi.org/10.1017/CBO9781139195065>) — threshold
  voltage versus channel doping and the mobility and body-effect
  penalties of a heavier channel.[^taur-2009]

## Open questions

* **Species, energy and dose.** The species (arsenic versus
  phosphorus), energy and dose of `PCHI` are not public.
* **Division of roles.** How the two implants `PCHI` and `PNCHI`
  divide the job of raising the PMOS threshold is discussed on the
  {ref}`PNCHI <step-024>` page and remains open. The same page
  discusses why one of them is a BF₂ (p-type) implant in a module that
  raises a PMOS threshold.
* **Baseline vs. increment.** Whether `PCHI` reaches only the `hvtp`
  devices or every low-voltage N-well outside `lvtn` — and hence
  whether it is an increment over {ref}`LVTPI <step-020>` or the
  baseline itself — turns on the reading of the `chvtpm` checks
  discussed on {ref}`HVTPM <step-022>`.[^pdk-errors]

<!-- footnotes -->

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
[^wiki-vt]: Wikipedia, *Threshold voltage*.
    <https://en.wikipedia.org/wiki/Threshold_voltage>
[^wiki-mtcmos]: Wikipedia, *Multi-threshold CMOS*.
    <https://en.wikipedia.org/wiki/Multi-threshold_CMOS>
[^itrs-04]: International Technology Roadmap for Semiconductors, *2001
    Edition: Process Integration, Devices, and Structures*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>
[^wei-1998]: L. Wei, Z. Chen, M. Johnson, K. Roy and V. De, "Design and
    optimization of low voltage high performance dual threshold CMOS
    circuits", *Proceedings of the 35th Design Automation Conference*,
    pp. 489–494 (1998). <https://doi.org/10.1109/DAC.1998.724521>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^thompson-1996]: S. E. Thompson, P. A. Packan and M. T. Bohr, "Linear
    versus saturated drive current: tradeoffs in super steep retrograde
    well engineering", *1996 Symposium on VLSI Technology, Digest of
    Technical Papers*, pp. 154–155.
    <https://doi.org/10.1109/VLSIT.1996.507830>
[^txt-04]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
    Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
    <https://openlibrary.org/isbn/9780961672157>
[^pat-vt-rrr]: M. Helm and X. Zhou (Round Rock Research), *Formation of
    standard voltage threshold and low voltage threshold MOSFET
    devices*, US 2011/0006372 A1, published 2011-01-13 (priority
    2002-07-08). <https://patents.google.com/patent/US20110006372A1/en>
[^shahidi-1993]: G. G. Shahidi, B. Davari, T. J. Bucelot, P. A.
    Ronsheim, P. J. Coane, S. Pollack, C. R. Blair, B. Clark and H. H.
    Hansen, "Indium channel implant for improved short-channel behavior
    of submicrometer NMOSFETs", *IEEE Electron Device Letters*
    **14**(8), 409–411 (1993). <https://doi.org/10.1109/55.225595>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
    Shown as in force; estimated expiry 2034-02-26 (estimate from public
    records, not legal advice).
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion
    Implanter* (Eaton Semiconductor Equipment Operations product
    description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^pat-vt-lsi]: S. Aronowitz, L. Khan and J. Kimball (LSI Logic), *Method
    of forming retrograde well structures and punch-through barriers
    using low energy implants*, US 5,963,801 A, granted 1999-10-05.
    <https://patents.google.com/patent/US5963801A/en>
[^taur-1997]: Y. Taur, D. A. Buchanan, W. Chen, D. J. Frank, K. E.
    Ismail, S.-H. Lo, G. A. Sai-Halasz, R. G. Viswanathan, H.-J. C.
    Wann, S. J. Wind and H.-S. Wong, "CMOS scaling into the nanometer
    regime", *Proceedings of the IEEE* **85**(4), 486–504 (1997).
    <https://doi.org/10.1109/5.573737>
[^macpherson-1971]: M. R. MacPherson, "The adjustment of MOS transistor
    threshold voltage by ion implantation", *Applied Physics Letters*
    **18**(11), 502–504 (1971). <https://doi.org/10.1063/1.1653513>
[^rafferty-1993]: C. S. Rafferty, H.-H. Vuong, S. A. Eshraghi, M. D.
    Giles, M. R. Pinto and S. J. Hillenius, "Explanation of reverse
    short channel effect by defect gradients", *IEDM 1993 Technical
    Digest*, pp. 311–314. <https://doi.org/10.1109/IEDM.1993.347345>
[^taur-2009]: Y. Taur and T. H. Ning, *Fundamentals of Modern VLSI
    Devices*, 2nd ed., Cambridge University Press, 2009, ISBN
    978-0-521-83294-6. <https://doi.org/10.1017/CBO9781139195065>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^raw-data-lv-mosfets]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the 1.8 V
    transistors, IC-CAP `.mdm` files in `sky130_fd_pr/cells/`
    (`nfet_01v8`, `nfet_01v8_lvt`, `pfet_01v8`, `pfet_01v8_hvt`,
    `pfet_01v8_lvt`), `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
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
