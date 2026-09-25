(step-037)=
# Step 037 — PTSI: Punch-through stop implant

| | |
|---|---|
| **Step number** | 37 of 171[^steps-sheet] |
| **Step code** | `PTSI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | {term}`FEOL` — SONOS and gate dielectrics |
| **Previous step** | {ref}`TUNARCE <step-036>` |
| **Next step** | {ref}`DEPI <step-038>` |

## What this step is

`PTSI` is the first of two implants made through the tunnel-mask windows
into the channel region of the {term}`SONOS` memory transistors. This
reference describes it as a p-type doping peak *below* the surface of
the memory channel — a "punch-through stop" (inference from the
n-channel SONOS cell and from the standard cure for punch-through
described below[^pat-vt-lsi]) — to
keep the depletion region of the drain from reaching the source in a
transistor whose gate is only a few tenths of a micrometre long and
which must withstand several volts on its drain and body during
programme, erase and inhibit operations. The surface doping, which sets
the threshold, is left for the next implant, {ref}`DEPI <step-038>`.

:::{figure} /_static/figures/sonos-037-ptsi.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step photoresist covers the surface except for a window over the right-hand active area, whose bottom is thin oxide. After it arrows come straight down into the window, and a hatched band lies a short way below the silicon surface under the window only; the silicon under the resist is untouched.
:width: 560px
:name: fig-sonos-037-ptsi

Before, the opened tunnel window; after, a beam into the window and, under it only, the implanted dose drawn as a band a short way below the silicon surface. The band sits below the surface because this page describes the implant as a p-type punch-through stop under the memory transistor's channel, which is an inference; it is hatched with no colour of its own, and its depth and profile are not public. The species, energy and dose are not public, and the arrows are drawn vertical because the tilt is not public (7° is only the textbook convention). The oxide the ions pass is drawn as the pad oxide, which the page infers. The fill oxide and the deep N-well are drawn but not labelled, and the liner oxide is drawn faded. Not to scale.
:::

The wafer at this point carries the {ref}`TUNM <step-035>` resist,
opened through its {term}`ARC` at {ref}`TUNARCE <step-036>`, so the implant
enters only the tunnel windows (`tunm`, GDS 80:20, described by the PDK
as "SONOS device tunnel implant"[^pdk-06]) and passes through the screen
oxide there — the pad oxide, we infer, whose thickness in the Cypress
embedded-SONOS flow is in the collapsed note under the recipe list
below. Everywhere else the resist stops it. On
the block reading of that rule preferred on the {ref}`LVTNI <step-015>`
page — the PDK describes `lvtn` as defining "regions to block Vt
adjust implant for low Vt LV PMOS/NMOS, SONOS FETs and Native
NMOS"[^pdk-periph] — the memory transistors skip the standard NMOS
channel implants, and we read `PTSI` and `DEPI` as their replacements
(inference; the alternative counter-dope reading is set out on
{ref}`LVTNI <step-015>`).

No public source gives the species, energy or dose. We describe the
Cypress-published analogue and era-typical values below.

## Step category

`PTSI` is an {ref}`Ion implantation <category-implant>` step of the
*channel engineering* class — the same family as {ref}`LVTNI <step-015>`
and {ref}`PCHI <step-023>` — but of the sub-surface ("punch-through
stopper" or "anti-punch-through") type rather than the surface
{term}`threshold-adjust <threshold-adjust implant>` type: a medium-current implant at tens to a hundred or
so keV, of order 10¹²–10¹³ cm⁻² (industry-typical),[^txt-01] aimed at a
peak beneath the channel.

## Why this step exists

{term}`Punch-through <punch-through>` is the short-channel failure in which the source and
drain depletion regions merge: Wikipedia describes the regime in which
"the depletion regions of the source and drain begin overlapping
underneath the channel", and drain-induced barrier lowering as the
drain "lowering the source–channel barrier".[^wiki-sce] The standard
cure is a doping peak below the channel that stops the drain depletion
region from spreading, without raising the surface doping that sets the
threshold and degrades mobility. An LSI Logic patent describes such a
technique — chained low-energy "punch-through barriers", there formed
with boron in an n-well beneath p-channel transistors and with
energies the patent itself calls "merely exemplary" (100, 70 and
50 keV)[^pat-vt-lsi] — and ITRS 2001 asks for a "Retrograde
channel depth" of 21–30 nm for its 2001 high-performance
device.[^itrs-01]

Three things make the SONOS transistor need its own barrier:

* **It is short.** The PDK's {term}`e-test` parameters are defined on memory
  transistors of drawn W/L 0.45/0.22 µm and 0.35/0.15 µm, for "both
  original and star cells"; the PDK does not say which geometry
  belongs to which cell, and we read 0.35/0.15 µm as the "star" cell
  because the PDK says it "is approximately 25% smaller than the
  original cell" (inference).[^pdk-07] Either way, both are gate
  lengths at or near the process minimum.
* **It sees high voltages.** The PDK's programme and erase table
  applies +6.7 V to the {term}`control gate` with −3.8 V on source, drain and
  body, and −3.8 V on the gate with +6.7 V on the other three
  terminals[^pdk-07] (the published table prints the programme source
  bias as "-38"; we read it as −3.8 V, the mirror of the erase
  condition), and unselected cells on shared lines see partial
  versions of these ("program inhibit" thresholds are also
  specified[^pdk-07]). A logic-style channel would not hold off these
  conditions at 0.22 µm.
* **Its surface must stay lightly doped.** The next implant makes the
  channel {term}`depletion-mode` ({ref}`DEPI <step-038>`), and Cypress's own
  scaling paper stresses "reduction of dopants in the surface of the
  channel" of the control gate and "use of deeper channel implants
  with heavier species such as Indium … so as to keep surface dopant
  concentrations low".[^cyp-25]

Without `PTSI` the erased cell would leak from drain to source and the
programme/erase window would collapse at short channel lengths.

## How it is typically performed

An industry-generic punch-through-stop implant for a 200 mm, 130 nm-era
memory transistor (SKY130's values are not public):

* **Species.** Boron (¹¹B⁺, from BF₃) is the usual p-type barrier
  dopant; indium is the heavier alternative that gives a steeper,
  shallower-tailed profile. The Cypress embedded-SONOS patent, which may
  still be in force, implants the memory-transistor channel with indium
  at an energy and dose given in the collapsed note below this list, and
  the same company's 2020 article recommends "heavier species such as
  Indium" for the control-gate channel.[^cyp-25] Indium's advantage for a retrograde
  channel was shown by Shahidi et al.[^shahidi-1993] and used for
  super-steep retrograde channels at 80 nm.[^huang-2000]
* **Energy.** Chosen to place the peak below the eventual channel,
  typically a few tens of nanometres to about 0.1 µm deep. Published
  logic-era barriers: boron chained at 100, 70 and 50 keV;[^pat-vt-lsi]
  the Cypress indium range is in the collapsed note below. Hori and
  Kurimoto's LATIPS
  device used a large-tilt-angle implant to put the stopper under the
  channel edge only,[^hori-1988] and Lin et al. optimised a
  tilt-implanted stopper in quarter-micron MOSFETs with
  low-concentration wells.[^lin-1997]
* **Dose.** Of order 10¹²–10¹³ cm⁻²; the Cypress patent's indium dose
  (collapsed note below) and the LSI Logic patent's chained boron
  barrier (4 × 10¹² cm⁻² at 100 keV plus 1–3 × 10¹¹ cm⁻² at 70 and
  50 keV)[^pat-vt-lsi] bracket it.
* **Tilt and twist.** 7° with a twist is the textbook convention to
  suppress {term}`channelling`;[^txt-02][^wiki-implant] a large tilt is
  used only when the barrier is meant to be asymmetric.[^hori-1988]
* **Screen.** Through the {term}`screen oxide` — the pad oxide, we infer,
  whose thickness in the Cypress patent is in the collapsed note below
  — which also randomises the beam.
* **Wafer handling.** Single-wafer, electrostatically chucked end
  station with an electron shower for charge neutralisation; the
  resist carries only a light dose here.
* **Anneal.** No dedicated anneal; the implant is, we infer, activated
  by the {term}`ONO` furnace steps ({ref}`ONO <step-040>`) and the gate
  oxidations ({ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`). The
  Cypress integration patent, which may still be in force, says where it
  places the memory-cell formation (collapsed note below), and this
  reference places the memory-cell steps accordingly.
* **Monitoring.** Thermal-wave damage measurement on product,
  {term}`sheet resistance` on monitor wafers ({ref}`category-implant`).

:::{dropdown} From patents shown as in force (US 8,093,128, estimated expiry 2028-10-22; US 8,796,098, estimated expiry 2034-02-26) — open to read
The Cypress embedded-SONOS patent implants the memory-transistor
channel "with Indium (In) at an energy of from about 50 to about 500
kilo-electron volts (keV), and a dose of from about 5e11 … to about
5e12 cm⁻²", through a pad oxide of 10–20 nm.[^pat-04] The Cypress
integration patent places the memory-cell formation "after at least some
of the well and channel implants for the logic MOS transistors are
formed".[^pat-03]
:::

## Machines typically used

* **{ref}`Medium-current ion implanter <machine-medium-current-implanter>`**, 200 mm, single-wafer: Axcelis
  (Eaton) 8250 class, Varian E220/E500, Applied Materials xR
  ({ref}`category-implant`). The 8250HT covers "3keV to 750keV" with
  beam currents "between 4µA and 3,500µA".[^axcelis-8250]
* **{ref}`Thermal-wave <machine-sheet-resistance-metrology>`** and **four-point-probe** metrology.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current implanter.** SkyWater lists "Axcelis
  8250 Mid current B11, BF2, As, ESC chuck, E shower, 1e11 to 1e14,
  0-60 deg tilt".[^skw-01] The species, dose range and tilt range cover
  a boron punch-through stopper. Strength: **strong** for the tool;
  **inference** for its assignment to `PTSI`.
* **Axcelis GSD high-current/high-energy implanter** ("B11, BF2, P,
  As, 10-3000kev, 1e11 to 5e15")[^skw-01] (the entry whose dose range
  starts below the Hi dose entry's 5e12) — could also run it. Strength:
  strong for existence; weak for assignment.
* Indium is *not* among the species SkyWater lists for any
  implanter,[^skw-01] so if SKY130 used indium here it would be on a
  configuration not described publicly (see *Open questions*).

## Resources required

* **{ref}`Boron trifluoride <material-dopant-sources>` (BF₃)** for ¹¹B⁺ or BF₂⁺; solid indium source
  charge if indium is used ({ref}`category-implant`).
* **Source-support gases**, source consumables (filaments, arc-chamber
  liners), high-purity {ref}`nitrogen <material-process-gases>` for venting.
* **Helium** for platen cooling; **liquid nitrogen** or cryopump
  regeneration.
* **{ref}`Monitor wafers <material-substrates>`** for dose control.
* Gas suppliers named in SkyWater's filings: Air Products and Praxair
  (2021 S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`TUNARCE <step-036>` (window cleared through the
  ARC); mask: {ref}`TUNM <step-035>`.
* Next: {ref}`DEPI <step-038>` (the surface implant through the same
  window), then {ref}`TUNME <step-039>`.
* The logic-transistor channels were implanted earlier
  ({ref}`LVTNI <step-015>`, {ref}`PCHI <step-023>`,
  {ref}`PNCHI <step-024>`) and annealed at {ref}`RTAI <step-034>`;
  this implant is annealed by the furnace steps that follow.
* The memory transistor's own tip implant comes later at
  {ref}`LDNTM <step-071>`.
* Category page: {ref}`Ion implantation <category-implant>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Method of forming retrograde well structures and punch-through barriers using low energy implants <patent-gp25087511>` — US 5,963,801 A (1996)

:::{dropdown} 2 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 8,093,128 B2 <patent-gp40072804>` — in force
* {ref}`US 8,796,098 B1 <patent-gp51229009>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater PDK, *Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) — `tunm` 80:20 "SONOS device tunnel
  implant".[^pdk-06]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — `lvtn` blocks the standard {term}`Vt`
  implants from "SONOS FETs".[^pdk-periph]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — SONOS cell W/L, programme/erase
  voltages and thresholds.[^pdk-07]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the Axcelis 8250 and GSD
  species, dose and tilt ranges.[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]
* [Ramkumar, Prabhakar and Kapre (Cypress), Semiconductor Digest](<https://sst.semiconductor-digest.com/2020/02/scalable-sonos-based-embedded-non-volatile-memory-technology/>) —
  deeper, heavier channel implants for the control gate.[^cyp-25]
* [Semiconductor Online, *8250HT Medium Current Ion Implanter*](<https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>) — energy
  and current range of the tool class.[^axcelis-8250]

:::{dropdown} From patents shown as in force (US 8,093,128, estimated expiry 2028-10-22; US 8,796,098, estimated expiry 2034-02-26) — open to read
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — indium
  channel implant energies and doses for the memory transistor; pad
  oxide thickness.[^pat-04]
* Koutny et al. (Cypress), US 8,093,128 — the memory cell formed after
  the logic well and channel implants.[^pat-03]
:::

### High-level understanding

* [Wikipedia, *Short-channel effect*](<https://en.wikipedia.org/wiki/Short-channel_effect>) — depletion-region overlap and
  {term}`DIBL`.[^wiki-sce]
* [Wikipedia, *Ion implantation*](<https://en.wikipedia.org/wiki/Ion_implantation>) — energies, tilt and
  channelling.[^wiki-implant]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 3](<https://openlibrary.org/isbn/9780961672157>) — the submicron
  MOSFET: punch-through and channel engineering.[^txt-04]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) — the
  implantation chapter.[^txt-02]

### Deep dive

* [Aronowitz, Khan and Kimball (LSI Logic), US 5,963,801](<https://patents.google.com/patent/US5963801A/en>) — chained
  low-energy punch-through barriers with explicit energies and
  doses.[^pat-vt-lsi]
* [Hori and Kurimoto, *IEEE EDL* 1988](<https://doi.org/10.1109/55.20422>) — the large-tilt-angle implanted
  punch-through stopper (LATIPS).[^hori-1988]
* [Lin et al., VLSI-TSA 1997](<https://doi.org/10.1109/VTSA.1997.614915>) — optimising a tilt-implanted
  punch-through stopper in quarter-micron MOSFETs.[^lin-1997]
* [Shahidi et al. (IBM), *IEEE EDL* 1993](<https://doi.org/10.1109/55.225595>) — indium channel implants for
  steep retrograde NMOS channels.[^shahidi-1993]
* [Huang et al., *IEEE TED* 2000](<https://doi.org/10.1109/16.887025>) — an indium super-steep retrograde
  channel at 80 nm gate length.[^huang-2000]
* [Chaudhry et al. (Bell Labs), IEDM 1997](<https://doi.org/10.1109/IEDM.1997.650474>) — suppressing the reverse
  short-channel effect with high-energy implantation.[^chaudhry-1997]
* [Taur et al., *Proc. IEEE* 1997](<https://doi.org/10.1109/5.573737>) — why retrograde channels and
  punch-through control matter as gates shrink.[^taur-1997]
* [Taur and Ning, *Fundamentals of Modern VLSI Devices*](<https://doi.org/10.1017/CBO9781139195065>) — the
  short-channel and punch-through physics.[^taur-2009]
* [Hook et al., *IEEE TED* 2003](<https://doi.org/10.1109/TED.2003.815371>) — threshold shifts near implant-mask
  edges, relevant to the 0.095 µm `tunm` clearances.[^hook-2003]
* [ITRS 2001, *Front End Processes*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>) — retrograde channel depth
  targets.[^itrs-01]

:::{dropdown} From a patent shown as in force (US 8,796,098; estimated expiry 2034-02-26) — open to read
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — the
  published channel-engineering recipe for an embedded SONOS
  transistor.[^pat-04]
:::

## Open questions

* The species (boron or indium), energy, dose and tilt of `PTSI` are
  not public; the values above are from a Cypress patent for a later
  node and from era-typical logic patents.
* Indium is absent from SkyWater's public implanter species lists; if
  it is used, the tool configuration is not described publicly. The
  tool class SkyWater lists is nevertheless an indium-capable one:
  Axcelis markets the 8250HT as removing the need for "a dedicated
  implanter for indium processes".[^axcelis-8250]
* Whether `PTSI` is a single implant or a chain of energies is unknown.
* Whether the implant is symmetric (7° tilt) or a large-tilt
  asymmetric stopper of the LATIPS kind is unknown.

<!-- footnotes -->

[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
    Shown as in force; estimated expiry 2034-02-26 (estimate from public
    records, not legal advice).
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^wiki-sce]: Wikipedia, *Short-channel effect*.
    <https://en.wikipedia.org/wiki/Short-channel_effect>
[^pat-vt-lsi]: S. Aronowitz, L. Khan and J. Kimball (LSI Logic), *Method
    of forming retrograde well structures and punch-through barriers
    using low energy implants*, US 5,963,801 A, granted 1999-10-05.
    <https://patents.google.com/patent/US5963801A/en>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^cyp-25]: K. Ramkumar, V. Prabhakar and R. Kapre (Cypress
    Semiconductor), *Scalable SONOS based embedded non-volatile memory
    technology*, Semiconductor Digest, 2020-02.
    <https://sst.semiconductor-digest.com/2020/02/scalable-sonos-based-embedded-non-volatile-memory-technology/>
[^shahidi-1993]: G. G. Shahidi, B. Davari, T. J. Bucelot, P. A.
    Ronsheim, P. J. Coane, S. Pollack, C. R. Blair, B. Clark and H. H.
    Hansen, "Indium channel implant for improved short-channel behavior
    of submicrometer NMOSFETs", *IEEE Electron Device Letters*
    **14**(8), 409–411 (1993). <https://doi.org/10.1109/55.225595>
[^huang-2000]: T.-Y. Huang, Y.-J. Lee, T.-S. Chao, C. Chen, C.-Y. Chang
    and S.-J. Chang, "High-performance and high-reliability 80-nm
    gate-length DTMOS with indium super steep retrograde channel",
    *IEEE Transactions on Electron Devices* **47**(12), 2379–2384
    (2000). <https://doi.org/10.1109/16.887025>
[^hori-1988]: T. Hori and K. Kurimoto, "A new p-channel MOSFET with
    large-tilt-angle implanted punchthrough stopper (LATIPS)", *IEEE
    Electron Device Letters* **9**(12), 641–643 (1988).
    <https://doi.org/10.1109/55.20422>
[^lin-1997]: C.-H. Lin, J.-J. Yang, K. Young and K.-Y. Chiu,
    "Optimization of tilt-implanted punchthrough stopper on
    short-channel behavior in quarter-micron MOSFET with
    low-concentration wells", *Proc. 1997 International Symposium on
    VLSI Technology, Systems, and Applications*, pp. 303–306.
    <https://doi.org/10.1109/VTSA.1997.614915>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
    Shown as in force; estimated expiry 2028-10-22 (estimate from public
    records, not legal advice).
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion
    Implanter* (Eaton Semiconductor Equipment Operations product
    description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^txt-04]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
    Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
    <https://openlibrary.org/isbn/9780961672157>
[^chaudhry-1997]: S. Chaudhry, C. S. Rafferty, W. J. Nagy, Y. F. Chyan,
    M. S. Carroll, A. S. Chen and K. H. Lee, "Suppression of reverse
    short channel effect by high energy implantation", *IEDM 1997
    Technical Digest*, pp. 679–682.
    <https://doi.org/10.1109/IEDM.1997.650474>
[^taur-1997]: Y. Taur, D. A. Buchanan, W. Chen, D. J. Frank, K. E.
    Ismail, S.-H. Lo, G. A. Sai-Halasz, R. G. Viswanathan, H.-J. C.
    Wann, S. J. Wind and H.-S. Wong, "CMOS scaling into the nanometer
    regime", *Proceedings of the IEEE* **85**(4), 486–504 (1997).
    <https://doi.org/10.1109/5.573737>
[^taur-2009]: Y. Taur and T. H. Ning, *Fundamentals of Modern VLSI
    Devices*, 2nd ed., Cambridge University Press, 2009, ISBN
    978-0-521-83294-6. <https://doi.org/10.1017/CBO9781139195065>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
