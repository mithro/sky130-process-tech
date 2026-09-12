(step-024)=
# Step 024 — PNCHI: P-channel BF2 implant

| | |
|---|---|
| **Step number** | 24 of 171 |
| **Step code** | `PNCHI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`PCHI <step-023>` |
| **Next step** | {ref}`PCHIS <step-025>` |

## What this step is

`PNCHI` is the second implant through the high-Vt P-channel resist of
{ref}`HVTPM <step-022>`, following {ref}`PCHI <step-023>` without a
strip in between. It is the one implant in the well and channel module
whose name carries a species: the step list used in this reference names
it "P-channel BF2 implant". No public document confirms the species.
Boron difluoride (BF₂⁺) is the standard way to put boron very close to
the silicon surface, because the molecular ion breaks up on impact and
"only 11/49 of its energy is carried by the boron atom", so a beam
energy the tool can control well produces a shallow boron profile
(category page).[^txt-01] The resist is stripped at
{ref}`PCHIS <step-025>`.

Boron is p-type. In an N-well channel it *counter-dopes* the surface
and, on its own, would lower the magnitude of a PMOS threshold, not
raise it. Its appearance inside the "high Vt LV PMOS"
module[^pdk-periph] therefore needs explanation; the possibilities are
set out below, and none of them is confirmed publicly.

## Step category

`PNCHI` is an {ref}`Ion implantation <category-implant>` step of the
*threshold/channel* class — keV, light dose, medium-current tool —
and specifically a shallow BF₂ implant of the kind the category page
describes for placing boron near the surface.

## Why this step exists

The physics of a two-implant channel gives three candidate roles for a
shallow boron dose in a high-Vt PMOS:

1. **Surface compensation in a retrograde channel.** The deeper n-type
   implant of {ref}`PCHI <step-023>` can be made heavier than the
   threshold alone requires, so that it also controls punch-through and
   drain-induced barrier lowering; a shallow BF₂ dose then trims the
   *surface* concentration back to the value that gives the wanted |Vt|.
   The net result is a steeper retrograde profile — high doping a few
   tens of nanometres down, lighter at the surface — which is exactly
   what ITRS 2001's "Retrograde channel depth" of 21–30 nm[^itrs-01] and
   the super-steep-retrograde literature describe.[^thompson-1996] This
   is our preferred reading.
2. **Buried-channel PMOS.** If the PMOS gate were n⁺ polysilicon, a
   shallow boron layer would be needed in *every* PMOS to bring |Vt|
   into range, and the high-Vt variant would use a *smaller* boron dose
   than the baseline. That would require the baseline PMOS to receive
   its own BF₂ elsewhere, and the step list used in this reference
   contains no such step; we consider it unlikely at 130 nm.[^txt-04]
3. **Junction or field engineering under the gate edge.** A light boron
   dose at the channel surface changes the source/drain extension
   junction abruptness and the gate-edge field; some high-Vt devices are
   tuned this way (the Round Rock/Micron patent describes a "boron type
   of implant such as BF₂, or Indium" as a second Vt adjustment applied
   in combination with an arsenic first adjustment).[^pat-vt-rrr]

Whichever applies, the aim is the same: a `pfet_01v8_hvt` with the
higher threshold, lower leakage and acceptable short-channel behaviour
that the PDK models,[^pdk-07] delivered through a single extra mask.

## How it is typically performed

An industry-generic shallow BF₂ channel implant for a 200 mm,
130 nm-era fab (SKY130 values not public):

* **Species and source.** BF₂⁺ selected by the analysing magnet from a
  boron trifluoride (BF₃) plasma[^wiki-implant] (category page). The
  fluorine co-implanted with the boron is a known side effect: it
  amorphises the surface slightly, which helps suppress channelling, and
  it can retard boron diffusion during the anneal.[^txt-01]
* **Energy.** Tens of keV of BF₂ energy, corresponding to a boron energy
  of a few keV and a projected range of tens of nanometres. Public
  examples: BF₂ "at an energy of from about 10 to about 100
  kilo-electron volts (keV)" for a channel implant in a Cypress SONOS
  patent;[^pat-04] "45-90 KeV for BF₂" in an AMD channel-implant
  example.[^pat-vt-amd]
* **Dose.** Light: "a dose of from about 1e12 cm⁻² to about 1e14 cm⁻²"
  in the Cypress example;[^pat-04] "about 1.0 to 2.5×10¹³ ions/cm²" in
  the AMD example.[^pat-vt-amd] A compensating trim in a high-Vt device
  would sit at the bottom of these ranges (inference).
* **Tilt and twist.** 7° with twist;[^wiki-implant] with BF₂ the
  self-amorphisation makes channelling less of a concern than with bare
  boron.
* **Screen oxide.** Through the pad oxide;[^pat-04] a shallow implant is
  sensitive to the oxide's thickness, so the oxide loss in the preceding
  strips matters (see {ref}`LVTPIS <step-021>`).
* **Anneal.** {ref}`RTAI <step-034>`; boron in a shallow layer is the
  dopant most affected by transient enhanced diffusion, which is one
  argument for a rapid rather than a furnace anneal (category page on
  {ref}`anneal <category-anneal>`).

## Machines typically used

* **Medium-current implanter** with BF₂ capability: Axcelis (Eaton)
  8250/8250HT,[^axcelis-8250] Varian E220/E500, Nissin (category page).
* **Thermal-wave** dose monitor.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current** — its public species list is "B11,
  BF2, As" with "1e11 to 1e14" dose and "0-60 deg tilt":[^skw-01] BF₂ is
  explicitly available. Strength: **strong** for the tool; assignment is
  an **inference** from capability and from the step immediately
  preceding it ({ref}`PCHI <step-023>`) plausibly running on the same
  tool.
* **Axcelis GSD** lists BF₂ too.[^skw-01] Strength: strong for
  existence, weak for assignment.

## Resources required

* **Boron trifluoride (BF₃)** source gas, delivered in sub-atmospheric
  cylinders[^wiki-implant] (category page). Fluorinated species erode
  ion-source parts faster than hydrides, so source-consumable usage is
  higher (Axcelis's GSD page notes "source operating costs especially
  with fluorinated species").[^axcelis-gsd-page]
* Support gases, cryopump and beam-line consumables, monitor wafers.
* No new resist: the {ref}`HVTPM <step-022>` resist is reused.

## Related steps and cross-references

* Previous: {ref}`PCHI <step-023>`; next: {ref}`PCHIS <step-025>`
  (strip); mask: {ref}`HVTPM <step-022>`.
* Baseline PMOS channel: {ref}`LVTPI <step-020>`.
* The other shallow p-type implants in the flow are the P⁺ source/drain
  implants (species not given in the step list used in this reference)
  {ref}`PSDI <step-082>`/{ref}`2PSDI <step-083>`.
* Activated at {ref}`RTAI <step-034>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — Axcelis 8250 "B11, BF2,
  As".[^skw-01]
* SkyWater PDK, *Device Details* — `pfet_01v8_hvt`.[^pdk-07]
* SkyWater PDK, *Periphery rules* — `hvtp`: "Vt adjust implant region
  for high Vt LV PMOS".[^pdk-periph]
* Ramkumar et al. (Cypress), US 8,796,098 — BF₂ 10–100 keV,
  1e12–1e14 cm⁻².[^pat-04]
* Semiconductor Online, *8250HT Medium Current Ion Implanter* — the
  Eaton/Axcelis 8250HT energy and beam-current ranges.[^axcelis-8250]
* Axcelis, *GSD Ovation* product page — fluorinated-species source
  costs.[^axcelis-gsd-page]

### High-level understanding

* Wikipedia, *Ion implantation* — energies, sources, channelling and
  tilt in one page.[^wiki-implant]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — BF₂
  implantation, fluorine effects.[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — channel
  engineering, surface- versus buried-channel PMOS, high-voltage
  MOS.[^txt-04]

### Deep dive

* ITRS 2001, *Front End Processes* — Table 51 retrograde channel
  depth.[^itrs-01]
* Thompson, Packan and Bohr (Intel), VLSI 1996 — drive-current
  trade-offs of super-steep retrograde channels.[^thompson-1996]
* Helm and Zhou (Round Rock Research), US 2011/0006372 — "boron type of
  implant such as BF2, or Indium".[^pat-vt-rrr]
* Krivokapic and Milic (AMD), US 6,238,982 — BF₂ 45–90 keV, 1–2.5 ×
  10¹³ cm⁻².[^pat-vt-amd]
* Wang et al., *J. Electrochem. Soc.* 1997 — fluorine's effect on boron
  diffusion after BF₂ implantation through oxide and RTA, directly
  relevant to a BF₂ channel implant annealed at RTAI.[^wang-1997]
* Taur et al., *Proc. IEEE* 1997 — super-steep retrograde channels at
  0.1 µm, the profile a surface compensation implant helps
  create.[^taur-1997]
* MacPherson, *Appl. Phys. Lett.* 1971 — the original
  threshold-adjust-by-implantation paper.[^macpherson-1971]
* Rafferty et al. (AT&T), IEDM 1993 — how implant damage and the anneal
  reshape shallow channel doping.[^rafferty-1993]
* Huang et al., *IEEE TED* 2000 — an indium super-steep retrograde
  channel, an alternative to shallow boron for profile
  shaping.[^huang-2000]
* Shahidi et al. (IBM), *IEEE EDL* 1993 — indium channel implants for
  steep retrograde NMOS channels.[^shahidi-1993]
* Aronowitz, Khan and Kimball (LSI Logic), US 5,963,801 — Vt-adjust and
  punch-through implants placed through a sacrificial
  oxide.[^pat-vt-lsi]

## Open questions

* The role of a p-type (BF₂) implant inside the high-Vt PMOS module
  is not explained by any public source; the retrograde-channel
  compensation reading above is our inference.
* Energy, dose and the order of `PCHI`/`PNCHI` relative to each other
  in profile depth are not public.
* The expansion of the acronym `PNCHI` is not known; we use only the
  name "P-channel BF2 implant" from the step list used in this
  reference.

<!-- footnotes -->

[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
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
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
[^pat-vt-amd]: Z. Krivokapic and O. Milic (AMD), *Multiple threshold
    voltage semiconductor device fabrication technology*, US 6,238,982
    B1, granted 2001-05-29.
    <https://patents.google.com/patent/US6238982B1/en>
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion
    Implanter* (Eaton Semiconductor Equipment Operations product
    description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^axcelis-gsd-page]: Axcelis Technologies, *GSD Ovation — High Current &
    High Energy Batch Ion Implanters*, product page, accessed
    2026-08-30. <https://www.axcelis.com/products/gsd-ovation/>
[^pat-vt-rrr]: M. Helm and X. Zhou (Round Rock Research), *Formation of
    standard voltage threshold and low voltage threshold MOSFET
    devices*, US 2011/0006372 A1, published 2011-01-13 (priority
    2002-07-08). <https://patents.google.com/patent/US20110006372A1/en>
[^wang-1997]: L. Z. Wang, M. S.-C. Luo, H.-H. Tseng and S. A. Ajuria,
    "The Influence of Fluorine on Boron-Enhanced Diffusion in Silicon by
    BF₂⁺ Implantation Through Oxide during High Temperature Rapid
    Thermal Anneal", *Journal of The Electrochemical Society*
    **144**(11), L298–L301 (1997). <https://doi.org/10.1149/1.1838075>
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
[^huang-2000]: T.-Y. Huang, Y.-J. Lee, T.-S. Chao, C. Chen, C.-Y. Chang
    and S.-J. Chang, "High-performance and high-reliability 80-nm
    gate-length DTMOS with indium super steep retrograde channel", *IEEE
    Transactions on Electron Devices* **47**(12), 2379–2384 (2000).
    <https://doi.org/10.1109/16.887025>
[^shahidi-1993]: G. G. Shahidi, B. Davari, T. J. Bucelot, P. A.
    Ronsheim, P. J. Coane, S. Pollack, C. R. Blair, B. Clark and H. H.
    Hansen, "Indium channel implant for improved short-channel behavior
    of submicrometer NMOSFETs", *IEEE Electron Device Letters*
    **14**(8), 409–411 (1993). <https://doi.org/10.1109/55.225595>
[^pat-vt-lsi]: S. Aronowitz, L. Khan and J. Kimball (LSI Logic), *Method
    of forming retrograde well structures and punch-through barriers
    using low energy implants*, US 5,963,801 A, granted 1999-10-05.
    <https://patents.google.com/patent/US5963801A/en>
