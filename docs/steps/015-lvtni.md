(step-015)=
# Step 015 — LVTNI: Low Vt NMOS implantation

| | |
|---|---|
| **Step number** | 15 of 171[^steps-sheet] |
| **Step code** | `LVTNI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | {term}`FEOL` — wells and channel implants |
| **Previous step** | {ref}`LVTNM <step-014>` |
| **Next step** | {ref}`LVTNIS <step-016>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** implants the low-Vt channel dopant through the
  {ref}`LVTNM <step-014>` resist windows.
* **Why:** sets the threshold-voltage difference between low-Vt and
  standard NMOS (and, via the shared mask, PMOS/native/SONOS
  channels).
* **Public numbers:** measured threshold 0.432 V (`nfet_01v8_lvt`)
  against 0.534 V (`nfet_01v8`) at 7/8 µm (our
  extraction).[^raw-data-lv-mosfets]
* **Likely SkyWater tool:** Axcelis 8250 medium-current implanter —
  strong (tool); inference (assignment).[^skw-01]
* **Not public:** the actual species, energy, dose and reticle
  polarity (→ Open questions).
:::

## What this step is

`LVTNI` is a channel-type ion implant performed through the resist
windows opened at {ref}`LVTNM <step-014>`. It is the first implant of
the well and channel module and — unusually — it is placed *before* the
N-well and P-well implants that follow at
{ref}`NWI <step-018>`/{ref}`NWI2 <step-019>` and
{ref}`PWI <step-027>`/{ref}`PWI2 <step-028>`. Its job is to set the
difference in threshold voltage between the low-Vt N-channel devices of
the PDK and the standard ones.

The dopant enters the active silicon
through what we infer to be the pad oxide left by
{ref}`NS19 <step-013>`, acting as the {term}`screen oxide` (see the open
question there). A Cypress {term}`SONOS` patent from the same lineage,
which may still be in force, describes exactly this arrangement, in the
collapsed note below.

:::{dropdown} From a patent shown as in force (US 8,796,098; estimated expiry 2034-02-26) — open to read
The Cypress {term}`SONOS` patent has "dopants … implanted into substrate
204 through the pad oxide 209" of "about 10 nanometers (nm) to about
20 nm".[^pat-04]
:::

:::{figure} /_static/figures/wells-015-lvtni.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step photoresist covers the right-hand part of the drawing and the left-hand active area lies in a window. After it arrows come straight down into the window, and a hatched band just under the surface of the left-hand active silicon marks the implanted dopant; the silicon under the resist is untouched.
:width: 560px
:name: fig-wells-015-lvtni

Before, the LVTNM window; after, the implanted dose as the NMOS channel implant, a thin band in the active silicon under the window. The band is hatched, with no colour of its own, because its type is not public: the PDK describes `lvtn` as blocking a Vt-adjust implant,[^pdk-periph] and the page weighs a p-type implant that low-Vt channels skip, which it favours, against an n-type counter-dope into the low-Vt channels only. The window is on the NMOS side as drawn at LVTNM, which is illustrative; the slice is read as an NMOS beside a high-Vt PMOS. The band is drawn only in the active silicon, under the oxide the page infers to be the pad oxide, and its depth is not public; the arrows are drawn vertical because the tilt is not public. The liner oxide is drawn faded. Not to scale.
:::

Which regions receive the implant depends on the {term}`reticle` polarity
discussed on the {ref}`LVTNM <step-014>` page. The PDK describes the
drawn `lvtn` layer as defining "regions to block Vt adjust implant for
low Vt LV PMOS/NMOS, SONOS FETs and Native NMOS".[^pdk-periph] Two
readings are possible:

* **Block reading.** `LVTNI` is the baseline NMOS {term}`threshold-adjust <threshold-adjust implant>`
  implant (a p-type species) given to every future NMOS channel *except*
  those drawn as `lvtn`; low-Vt, native and SONOS channels are the ones
  that skip it. This matches the PDK's word "block" and the statement
  that native devices are "constructed by blocking out all VT
  implants".[^pdk-07]
* **{term}`Counter-dope <counter-doping>` reading.** `LVTNI` is an n-type implant delivered
  *only* into `lvtn` regions, which lowers the NMOS threshold by
  partially compensating the p-type channel. A Round Rock/Micron patent
  describes low-Vt devices obtained in this way, with a "counter-doped
  channel region".[^pat-vt-rrr]

Both are consistent with an NMOS threshold being lowered; only the
first is consistent with the same layer also lowering the PMOS
threshold, unless the reticle is derived separately for N-well
regions. We favour the block reading but cannot confirm it.

## Step category

`LVTNI` is an {ref}`Ion implantation <category-implant>` step of the
*threshold-adjust* class: light dose (of order 10¹²–10¹³ cm⁻²), low
energy (tens of keV), placed just under the future gate oxide, from a
medium-current implanter (category page).[^txt-01]

## Why this step exists

The threshold voltage of a MOSFET rises with the doping of the channel
region. In the standard body-effect expression the parameter γ contains
the doping concentration N_A,[^wiki-vt] and multi-threshold CMOS is
built by "altering the concentration of dopant atoms in the channel
region beneath the gate oxide".[^wiki-mtcmos]

The 1.8 V NMOS family of
SKY130 comprises `nfet_01v8` and `nfet_01v8_lvt`;[^pdk-07] `LVTNI`,
together with the N-channel implant {ref}`NCHI <step-045>` that all
1.8 V devices receive under the low-voltage oxide mask, is what
separates the two. The same mask serves `pfet_01v8_lvt`, the native NMOS
devices and the SONOS cells,[^pdk-periph] so this step (or its absence)
also underlies the zero-Vt-class devices whose value to analogue
designers is a threshold near 0 V.

The published test-tile measurements show the size of the separation.
By maximum-transconductance extrapolation at V_DS = 0.1 V, less half
the drain bias, we extract 0.432 V for `nfet_01v8_lvt` against 0.534 V
for `nfet_01v8` at 7/8 µm, and 0.612 V against 0.707 V at 7/0.15 µm.
These are differences of 0.102 V and 0.095 V, against 0.101 V and
0.089 V between the PDK's e-test nominals.

For two 7/0.15 µm structures with the same
source/drain extent (2.5 µm) the low-Vt device carries 3.84 mA against
3.39 mA at V_GS = V_DS = 1.8 V, 13 % more. The PDK's nominal currents
differ by 14 %. In the modules that hold the e-test geometries, however,
the 7/0.15 µm low-Vt device carries 3.30 mA against 3.40 mA (our
extraction from the published measurements; see
{ref}`HPETEST <step-171>`).[^raw-data-lv-mosfets][^raw-data-testtile-pads][^pdk-07]

The low-Vt device also shows the smaller body effect: its threshold
rises by 0.245 V for 1.8 V of reverse body bias at 7/8 µm, against
0.299 V (our extraction).[^raw-data-lv-mosfets] Lower net channel
doping would give that, and both readings above lower the net doping,
so it does not decide between them (inference).[^wiki-vt]

The trade is leakage: "Typical high Vth devices reduce static leakage by
10 times compared with low Vth devices".[^wiki-mtcmos] A process without
`LVTNI` would still make working logic, but only at one threshold.

## How it is typically performed

*An industry-generic threshold-adjust implant for a 200 mm, 130 nm-era
fab. The SKY130 species, energy and dose are not public; the values
below are typical or taken from contemporaneous patents.*

* **Species.** For an implant that *raises* an NMOS threshold the
  species is p-type.

  Options are boron (¹¹B⁺), BF₂⁺ for a shallower boron placement
  (only 11/49 of the beam energy is carried by the boron atom; category
  page), or indium, a heavy p-type dopant used for steep retrograde
  channels.[^shahidi-1993][^huang-2000] Cypress's own patent, which may
  still be in force, gives energies and doses for a BF₂ channel implant
  and for an indium-doped memory-transistor channel; those sentences are
  in the collapsed note below this list. A 2020 Cypress article
  describes "use of deeper channel implants with heavier species such as
  Indium" for the SONOS cell.[^cyp-25]

  For an implant that *lowers* the
  threshold by counter-doping, the species is n-type — arsenic or
  phosphorus — at similar doses.[^pat-vt-rrr]
* **Energy and dose.** Tens of keV — up to about 100 keV in published
  examples — and 10¹²–10¹³ cm⁻².

  An LSI Logic patent has the threshold-adjust boron "implanted through
  the sacrificial gate oxide in doses between 1×10¹² and 1×10¹³
  atoms/cm² … at implant energies between 50 and 100
  keV". That implant is made after the well anneal,
  through a newly grown 200–500 Å sacrificial oxide, not through a pad
  oxide.[^pat-vt-lsi] An AMD patent gives "approximately 10-20 KeV for boron or
  45-90 KeV for BF₂ at a concentration of about 1.0 to 2.5×10¹³
  ions/cm²" for a laterally doped channel implant made after gate
  formation with the gate pillars as a self-aligned mask.[^pat-vt-amd]
  It is a different placement from this pre-gate implant. AMD also
  describes a prior-art threshold adjust implant at "about 5-to-15 KeV
  at a concentration of about 8×10¹² ions/cm²".[^pat-vt-amd]
* **Tilt and twist.** A few degrees of tilt with twist to suppress
  {term}`channelling` — "most implantation is carried out a few degrees
  off-axis";[^wiki-implant] the PDK's assumptions table records 7° as
  the angle for tip implants,[^pdk-03] which is also the textbook
  convention for channel implants.[^txt-02]
* **Screen oxide.** The pad oxide randomises the beam and keeps
  sputtered resist off the silicon; its thickness is the patent figure
  in the collapsed note below this list.
* **Charge control and wafer cooling.** Electron shower and cooled
  electrostatic chuck — both features SkyWater lists for its
  medium-current tool ("ESC chuck, E shower").[^skw-01]
* **Anneal.** None here; activation waits for {ref}`RTAI <step-034>`,
  after all well implants.
* **Monitoring.** Modulated-reflectance (Therma-Wave) on product or
  monitor wafers, since the dose is too low for {term}`sheet resistance` to be a
  sensitive check (category page).

:::{dropdown} From a patent shown as in force (US 8,796,098; estimated expiry 2034-02-26) — open to read
Cypress's own patents describe BF₂ "at an energy of from about 10 to
about 100 kilo-electron volts (keV), and a dose of from about 1e12 cm⁻²
to about 1e14 cm⁻² to form an N-type MOS (NMOS) transistor" channel, and
an indium-doped channel "implanted with Indium (In) at an energy of from
about 50 to about 500 kilo-electron volts (keV), and a dose of from
about 5e11 … to about 5e12 cm⁻²" for the memory transistor; the screen
oxide is the 10–20 nm pad oxide.[^pat-04]
:::

## Machines typically used

* **{ref}`Medium-current implanter <machine-medium-current-implanter>`**, 200 mm, serial end station with
  tilt/twist: Axcelis (Eaton) NV-8250/8250HT, Varian E220/E500,
  Nissin[^txt-09] (category page). The Eaton 8250HT is described as
  covering "3keV to 750keV" with beam currents "between 4µA and
  3,500µA".[^axcelis-8250]
* **{ref}`Therma-Wave <machine-sheet-resistance-metrology>`** modulated-reflectance monitor; {term}`four-point probe` on
  monitor wafers after a monitor anneal.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current implanter**
  - *SkyWater says:* lists "Axcelis 8250 Mid current B11, BF2, As, ESC
    chuck, E shower, 1e11 to 1e14, 0-60 deg tilt".[^skw-01]
  - *Tool exists:* strong.
  - *Runs this step:* assignment to `LVTNI` is an inference from
    capability — the species (B, BF₂, As), the dose window
    (10¹¹–10¹⁴ cm⁻²) and the tilt capability are exactly those of a
    threshold-adjust implant.
* **Axcelis GSD implanters**
  - *SkyWater says:* lists either GSD entry, "High current/energy" or
    "Hi dose".[^skw-01]
  - *Tool exists:* strong for existence.
  - *Runs this step:* weak — either could equally run a keV boron
    implant, but these batch tools are normally reserved for wells and
    source/drains; which entry would serve is not stated.
* A SkyWater maintenance profile mentions implanter robotics and vacuum
  work[^skw-07] — corroboration that implanters are maintained in house,
  not tool evidence.

## Resources required

* **{ref}`Boron trifluoride <material-dopant-sources>` (BF₃)** as the source gas for B⁺ and
  BF₂⁺[^wiki-implant] (category page); **arsine (AsH₃)** or **phosphine
  (PH₃)** if the implant is n-type; **solid indium** in a vaporiser oven
  if indium is used (category page).
* **Source support gases** ({ref}`argon <material-process-gases>`, xenon, hydrogen); **liquid nitrogen /
  cryopump** consumables; high-purity nitrogen vent gas.
* **Ion-source consumables** (filaments or cathodes, arc-chamber liners,
  extraction electrodes).
* **Wafer-cooling** water and backside gas; **{ref}`monitor wafers <material-substrates>`**.
* SkyWater's filings name Air Products and Praxair (2021 S-1) and Linde and
  Airgas (fiscal 2023 10-K) among its gas suppliers without tying them to a
  step.[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`LVTNM <step-014>` (the mask).
* Next: {ref}`LVTNIS <step-016>` (strip).
* Same category: threshold-setting companions —
  {ref}`LVTPI <step-020>` (PMOS, under the N-well mask),
  {ref}`PCHI <step-023>`/{ref}`PNCHI <step-024>` (high-Vt PMOS) and
  {ref}`NCHI <step-045>` (N-channel, under the low-voltage oxide mask).
* Feeds: activated at {ref}`RTAI <step-034>`.
* Category page: {ref}`Ion implantation <category-implant>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Method of forming retrograde well structures and punch-through barriers using low energy implants <patent-gp25087511>` — US 5,963,801 A (1996)
* {ref}`Multiple threshold voltage semiconductor device fabrication technology <patent-gp23113681>` — US 6,238,982 B1 (1999)
* {ref}`Formation of standard voltage threshold and low voltage threshold mosfet devices <patent-gp29999977>` — US 2011/0006372 A1 (2002)

:::{dropdown} 1 family in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 8,796,098 B1 <patent-gp51229009>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — Axcelis 8250 "Mid current B11,
  BF2, As, ESC chuck, E shower, 1e11 to 1e14, 0-60 deg tilt".[^skw-01]
* [SkyWater, *A Day in the Life of a SkyWater Maintenance Technician*](<https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>) —
  implanters are maintained in house.[^skw-07]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — `lvtn` function text.[^pdk-periph]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — `nfet_01v8`, `nfet_01v8_lvt`; native
  devices "blocking out all VT implants".[^pdk-07]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — implant angles
  table.[^pdk-03]
* [Semiconductor Online, *8250HT Medium Current Ion Implanter*](<https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>) — Eaton
  Semiconductor Equipment Operations product description; 3–750 keV,
  4–3500 µA.[^axcelis-8250]
* SKY130 raw-data repository, 1.8 V transistor files and test-tile pad
  documentation — thresholds, currents and body effect of
  `nfet_01v8` and `nfet_01v8_lvt` (our
  extraction).[^raw-data-lv-mosfets][^raw-data-testtile-pads]

:::{dropdown} From a patent shown as in force (US 8,796,098; estimated expiry 2034-02-26) — open to read
* Ramkumar et al. (Cypress), US 8,796,098 — pad oxide 10–20 nm; BF₂
  10–100 keV, 1e12–1e14 cm⁻²; indium 50–500 keV.[^pat-04]
:::

### High-level understanding

* [Wikipedia, *Ion implantation*](<https://en.wikipedia.org/wiki/Ion_implantation>) — energies, sources, channelling and
  tilt in one page.[^wiki-implant]
* [Wikipedia, *Threshold voltage*](<https://en.wikipedia.org/wiki/Threshold_voltage>) — body-effect parameter containing
  N_A.[^wiki-vt]
* [Wikipedia, *Multi-threshold CMOS*](<https://en.wikipedia.org/wiki/Multi-threshold_CMOS>) — why several thresholds are offered
  and how they are set.[^wiki-mtcmos]
* [Plummer, Deal and Griffin, *Silicon VLSI Technology*](<https://openlibrary.org/isbn/9780130850379>) — ch. 8 ("Ion
  Implantation").[^txt-01]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) —
  lithography, resist stripping, wafer cleaning and implantation
  chapters.[^txt-02]
* [Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology*](<https://openlibrary.org/isbn/9781574446753>) — implanter classes.[^txt-09]
* [Ramkumar, Prabhakar and Kapre (Cypress), *Scalable SONOS based
  embedded non-volatile memory technology*](<https://sst.semiconductor-digest.com/2020/02/scalable-sonos-based-embedded-non-volatile-memory-technology/>) — indium channel
  engineering.[^cyp-25]

### Deep dive

* [Helm and Zhou (Round Rock Research), US 2011/0006372](<https://patents.google.com/patent/US20110006372A1/en>) — arsenic and
  BF₂/indium {term}`Vt` adjusts; counter-doped low-Vt channel.[^pat-vt-rrr]
* [Aronowitz, Khan and Kimball (LSI Logic), US 5,963,801](<https://patents.google.com/patent/US5963801A/en>) — Vt-adjust
  boron 1e12–1e13 cm⁻² at 50–100 keV.[^pat-vt-lsi]
* [Krivokapic and Milic (AMD), US 6,238,982](<https://patents.google.com/patent/US6238982B1/en>) — multiple thresholds set by
  gate length, with a laterally doped channel implant self-aligned to
  the gate pillars.[^pat-vt-amd]
* [Shahidi et al. (IBM), *IEEE EDL* 1993](<https://doi.org/10.1109/55.225595>) — indium channel implants for
  steep retrograde NMOS channels.[^shahidi-1993]
* [Huang et al., *IEEE TED* 2000](<https://doi.org/10.1109/16.887025>) — an 80 nm DTMOS with an indium
  super-steep retrograde channel.[^huang-2000]
* [MacPherson, *Appl. Phys. Lett.* 1971](<https://doi.org/10.1063/1.1653513>) — the original demonstration of
  setting a MOS threshold by ion implantation.[^macpherson-1971]
* [Peressini and Johnson, IEDM 1973](<https://doi.org/10.1109/IEDM.1973.188761>) — early NMOS threshold adjustment by
  implantation with dose-versus-threshold data.[^peressini-1973]
* [Taur et al., *Proc. IEEE* 1997](<https://doi.org/10.1109/5.573737>) — super-steep retrograde channels and
  multiple thresholds at the 0.1 µm node.[^taur-1997]
* [Rafferty et al. (AT&T), IEDM 1993](<https://doi.org/10.1109/IEDM.1993.347345>) — how implant damage and the anneal
  reshape the channel profile (the reverse short-channel
  effect).[^rafferty-1993]
* [Smith, Rosencwaig and Willenborg, *Appl. Phys. Lett.* 1985](<https://doi.org/10.1063/1.96079>) — the
  thermal-wave monitor that checks light channel implants where sheet
  resistance cannot.[^smith-1985]
* [Current, *J. Vac. Sci. Technol. A* 1996](<https://doi.org/10.1116/1.580279>) — what a production
  medium-current implanter looks like inside.[^current-1996]

## Open questions

* **Species, energy, dose, tilt and polarity.** The species, energy,
  dose and tilt of `LVTNI` are not public; so is its polarity (p-type
  baseline implant that low-Vt devices skip, or n-type counter-dope
  into low-Vt devices).
* **Implant ordering.** Why this channel implant precedes the well
  implants — rather than following them as in most published flows —
  is not documented; a plausible reason is simply that it shares the
  full {ref}`RTAI <step-034>` anneal with the wells either way.
* **Screen oxide.** Whether the pad oxide from {ref}`BOX <step-002>`
  is still present as the screen oxide (see the open question on
  {ref}`NS19 <step-013>`) is inferred, not stated.

<!-- footnotes -->

[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
    Shown as in force; estimated expiry 2034-02-26 (estimate from public
    records, not legal advice).
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^pat-vt-rrr]: M. Helm and X. Zhou (Round Rock Research), *Formation of
    standard voltage threshold and low voltage threshold MOSFET
    devices*, US 2011/0006372 A1, published 2011-01-13 (priority
    2002-07-08). <https://patents.google.com/patent/US20110006372A1/en>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^wiki-vt]: Wikipedia, *Threshold voltage*.
    <https://en.wikipedia.org/wiki/Threshold_voltage>
[^wiki-mtcmos]: Wikipedia, *Multi-threshold CMOS*.
    <https://en.wikipedia.org/wiki/Multi-threshold_CMOS>
[^shahidi-1993]: G. G. Shahidi, B. Davari, T. J. Bucelot, P. A.
    Ronsheim, P. J. Coane, S. Pollack, C. R. Blair, B. Clark and H. H.
    Hansen, "Indium channel implant for improved short-channel behavior
    of submicrometer NMOSFETs", *IEEE Electron Device Letters*
    **14**(8), 409–411 (1993). <https://doi.org/10.1109/55.225595>
[^huang-2000]: T.-Y. Huang, Y.-J. Lee, T.-S. Chao, C. Chen, C.-Y. Chang
    and S.-J. Chang, "High-performance and high-reliability 80-nm
    gate-length DTMOS with indium super steep retrograde channel", *IEEE
    Transactions on Electron Devices* **47**(12), 2379–2384 (2000).
    <https://doi.org/10.1109/16.887025>
[^cyp-25]: K. Ramkumar, V. Prabhakar and R. Kapre (Cypress
    Semiconductor), *Scalable SONOS based embedded non-volatile memory
    technology*, Semiconductor Digest, 2020-02.
    <https://sst.semiconductor-digest.com/2020/02/scalable-sonos-based-embedded-non-volatile-memory-technology/>
[^pat-vt-lsi]: S. Aronowitz, L. Khan and J. Kimball (LSI Logic), *Method
    of forming retrograde well structures and punch-through barriers
    using low energy implants*, US 5,963,801 A, granted 1999-10-05.
    <https://patents.google.com/patent/US5963801A/en>
[^pat-vt-amd]: Z. Krivokapic and O. Milic (AMD), *Multiple threshold
    voltage semiconductor device fabrication technology*, US 6,238,982
    B1, granted 2001-05-29.
    <https://patents.google.com/patent/US6238982B1/en>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007, ISBN
    978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion
    Implanter* (Eaton Semiconductor Equipment Operations product
    description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^skw-07]: SkyWater Technology, *A Day in the Life of a SkyWater
    Maintenance Technician*, 2023-12-14.
    <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^macpherson-1971]: M. R. MacPherson, "The adjustment of MOS transistor
    threshold voltage by ion implantation", *Applied Physics Letters*
    **18**(11), 502–504 (1971). <https://doi.org/10.1063/1.1653513>
[^peressini-1973]: P. P. Peressini and W. S. Johnson, "Threshold
    adjustment of N-channel enhancement mode FETs by ion implantation",
    *1973 International Electron Devices Meeting*, pp. 467–468.
    <https://doi.org/10.1109/IEDM.1973.188761>
[^taur-1997]: Y. Taur, D. A. Buchanan, W. Chen, D. J. Frank, K. E.
    Ismail, S.-H. Lo, G. A. Sai-Halasz, R. G. Viswanathan, H.-J. C.
    Wann, S. J. Wind and H.-S. Wong, "CMOS scaling into the nanometer
    regime", *Proceedings of the IEEE* **85**(4), 486–504 (1997).
    <https://doi.org/10.1109/5.573737>
[^rafferty-1993]: C. S. Rafferty, H.-H. Vuong, S. A. Eshraghi, M. D.
    Giles, M. R. Pinto and S. J. Hillenius, "Explanation of reverse
    short channel effect by defect gradients", *IEDM 1993 Technical
    Digest*, pp. 311–314. <https://doi.org/10.1109/IEDM.1993.347345>
[^smith-1985]: W. L. Smith, A. Rosencwaig and D. L. Willenborg, "Ion
    implant monitoring with thermal wave technology", *Applied Physics
    Letters* **47**(6), 584–586 (1985).
    <https://doi.org/10.1063/1.96079>
[^current-1996]: M. I. Current, "Ion implantation for silicon device
    manufacturing: A vacuum perspective", *Journal of Vacuum Science &
    Technology A* **14**(3), 1115–1123 (1996).
    <https://doi.org/10.1116/1.580279>
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
