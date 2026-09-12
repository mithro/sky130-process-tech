(step-023)=
# Step 023 — PCHI: P-channel implant

| | |
|---|---|
| **Step number** | 23 of 171 |
| **Step code** | `PCHI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`HVTPM <step-022>` |
| **Next step** | {ref}`PNCHI <step-024>` |

## What this step is

`PCHI` is the first of two channel implants placed through the resist
windows of {ref}`HVTPM <step-022>`, the high-Vt P-channel mask. It adds
dopant to the surface of the N-well under the future gates of the PMOS
transistors drawn with the `hvtp` layer, on top of the baseline PMOS
channel doping that every N-well received at {ref}`LVTPI <step-020>`.
Its companion, {ref}`PNCHI <step-024>`, carries "BF2" in its name in the
step list used in this reference; `PCHI` itself carries no species in
its name. The resist is stripped at {ref}`PCHIS <step-025>`.

The PDK describes the `hvtp` region as the "Vt adjust implant region for
high Vt LV PMOS"[^pdk-periph] and the resulting device as the "1.8V
high-VT PMOS FET", `pfet_01v8_hvt`, modelled for V_DS and V_GS from 0 to
−1.95 V.[^pdk-07] The same implant, applied to a varactor, gives
`cap_var_hvt`, the "high VT PMOS device option".[^pdk-07]

## Step category

`PCHI` is an {ref}`Ion implantation <category-implant>` step of the
*threshold-adjust* class: light dose, tens of keV, medium-current
tool, through the pad/screen oxide (category page). It is the third
threshold implant of the module after {ref}`LVTNI <step-015>` and
{ref}`LVTPI <step-020>`.

## Why this step exists

The threshold of a PMOS in an N-well rises in magnitude with the n-type
doping at the surface of the channel.[^wiki-vt][^wiki-mtcmos] `LVTPI`
sets that doping for the standard PMOS; `PCHI` and `PNCHI` add to it
where a higher |Vt| is wanted. The motive is leakage: "Typical high Vth
devices reduce static leakage by 10 times compared with low Vth
devices",[^wiki-mtcmos] and a 130 nm low-power process needs a high-Vt
option to make standby-current targets in cells that are not
speed-critical.[^itrs-04][^wei-1998] The PDK's inverter-delay tables for
`nfet_01v8`/`pfet_01v8_hvt` combinations[^pdk-07] quantify the speed
that is traded for it.

A second, more physical reason to split the high-Vt adjust into two
implants is profile shaping. A single shallow implant that raises the
surface concentration enough to move the threshold also raises the body
effect and degrades mobility; pairing a deeper implant that controls
short-channel behaviour with a shallower one that sets Vt is the
"retrograde channel" approach that ITRS 2001 tabulates ("Retrograde
channel depth (nm)" 21–30 nm for the 2001 high- performance
node)[^itrs-01] and that Thompson, Packan and Bohr analysed for its
drive-current trade-offs.[^thompson-1996] We infer, without public
confirmation, that `PCHI` and `PNCHI` divide these roles between them.

## How it is typically performed

An industry-generic high-Vt PMOS channel implant for a 200 mm,
130 nm-era fab. SKY130's species, energy and dose are not public.

* **Species.** To raise |Vt| of a surface-channel PMOS the added dopant
  is n-type — arsenic (shallow, slow-diffusing) or phosphorus (deeper
  for a given energy).[^txt-04] The Round Rock/Micron multi-Vt patent
  uses "an implant of Arsenic" for exactly this purpose.[^pat-vt-rrr] An
  indium implant, which is p-type, is used for *NMOS* retrograde
  channels[^shahidi-1993] and is not a candidate here. Arsenic is the
  more plausible species, and is on the public species list of
  SkyWater's medium-current tool.[^skw-01]
* **Energy and dose.** Tens of keV; of order 10¹²–10¹³ cm⁻² (category
  page; the boron-side analogues in an LSI Logic patent are "doses
  between 1×10¹² and 1×10¹³ atoms/cm²" at 50–100 keV[^pat-vt-lsi]). A
  high-Vt adjust is by definition a *small* increment over the baseline,
  so its dose is at the low end of the range — a few 10¹² cm⁻² is
  illustrative.
* **Tilt and twist.** 7° with twist.[^wiki-implant][^txt-02]
* **Screen oxide.** The pad oxide (10–20 nm in the Cypress SONOS
  patent)[^pat-04] randomises the beam and traps recoils.
* **Charge control.** Electron shower on a cooled electrostatic chuck
  (SkyWater lists "ESC chuck, E shower").[^skw-01]
* **Anneal.** None until {ref}`RTAI <step-034>`.
* **Monitoring.** Thermal-wave on product; sheet resistance on monitors
  after a monitor anneal.

## Machines typically used

* **Medium-current implanter** with serial end station: Axcelis (Eaton)
  8250/8250HT ("3keV to 750keV", "between 4µA and
  3,500µA"),[^axcelis-8250] Varian E220/E500, Nissin (category page).
* **Thermal-wave** dose monitor.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current** — "B11, BF2, As, ESC chuck, E shower,
  1e11 to 1e14, 0-60 deg tilt".[^skw-01] Arsenic and the dose window
  match. Strength: **strong** for the tool; assignment is an
  **inference**.
* **Axcelis GSD**[^skw-01] is capable but is the well/source-drain
  workhorse. Strength: strong for existence, weak for assignment.

## Resources required

* **Arsine (AsH₃)** or **phosphine (PH₃)** source gas.[^wiki-implant]
* Support gases, cryopump and ion-source consumables, monitor wafers
  (category page).
* No new resist: the {ref}`HVTPM <step-022>` resist is reused for
  {ref}`PNCHI <step-024>`.

## Related steps and cross-references

* Previous: {ref}`HVTPM <step-022>` (mask); next:
  {ref}`PNCHI <step-024>` (second implant through the same resist),
  then {ref}`PCHIS <step-025>` (strip).
* Baseline PMOS channel: {ref}`LVTPI <step-020>`; low-Vt option via
  {ref}`LVTNM <step-014>`.
* Activated at {ref}`RTAI <step-034>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — the site tool list.[^skw-01]
* SkyWater PDK, *Device Details* — `pfet_01v8_hvt`, `cap_var_hvt`,
  inverter delay tables.[^pdk-07]
* SkyWater PDK, *Periphery rules* — `hvtp` function text.[^pdk-periph]
* Ramkumar et al. (Cypress), US 8,796,098 — pad oxide under the
  implants.[^pat-04]
* Semiconductor Online, *8250HT Medium Current Ion Implanter* — the
  Eaton/Axcelis 8250HT energy and beam-current ranges.[^axcelis-8250]

### High-level understanding

* Wikipedia, *Ion implantation* — energies, sources, channelling and
  tilt in one page.[^wiki-implant]
* Wikipedia, *Threshold voltage* — the body-effect parameter containing
  the channel doping.[^wiki-vt]
* Wikipedia, *Multi-threshold CMOS* — why several thresholds are offered
  and how they are set.[^wiki-mtcmos]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography, resist stripping, wafer cleaning and implantation
  chapters.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — channel
  engineering of submicron PMOS.[^txt-04]

### Deep dive

* ITRS 2001, *Front End Processes* — Table 51 retrograde channel
  depth.[^itrs-01]
* ITRS 2001, *Process Integration, Devices, and Structures* — multiple
  threshold-voltage devices as a roadmap requirement.[^itrs-04]
* Thompson, Packan and Bohr (Intel), VLSI 1996 — drive-current
  trade-offs of super-steep retrograde channels.[^thompson-1996]
* Helm and Zhou (Round Rock Research), US 2011/0006372 — low-Vt NMOS and
  PMOS defined by masked Vt-adjust implants, including a counter-doped
  channel.[^pat-vt-rrr]
* Aronowitz, Khan and Kimball (LSI Logic), US 5,963,801 — Vt-adjust
  boron at 1e12–1e13 cm⁻² and 50–100 keV, chained punch-through
  barriers, a 900 °C furnace anneal.[^pat-vt-lsi]
* Shahidi et al. (IBM), *IEEE EDL* 1993 — indium channel implants for
  steep retrograde NMOS channels.[^shahidi-1993]
* Wei et al., DAC 1998 — the circuit-level case for a second threshold
  voltage.[^wei-1998]
* Taur et al., *Proc. IEEE* 1997 — super-steep retrograde channels and
  multiple thresholds at 0.1 µm.[^taur-1997]
* MacPherson, *Appl. Phys. Lett.* 1971 — the original
  threshold-adjust-by-implantation paper.[^macpherson-1971]
* Rafferty et al. (AT&T), IEDM 1993 — how implant damage and the anneal
  reshape the channel profile.[^rafferty-1993]
* Taur and Ning, *Fundamentals of Modern VLSI Devices* — threshold
  voltage versus channel doping and the mobility and body-effect
  penalties of a heavier channel.[^taur-2009]

## Open questions

* The species (arsenic versus phosphorus), energy and dose of `PCHI`
  are not public.
* How the two implants `PCHI` and `PNCHI` divide the job of raising
  the PMOS threshold — and why one of them is a BF₂ (p-type) implant
  in a module that raises a PMOS threshold — is discussed on the
  {ref}`PNCHI <step-024>` page and remains open.

<!-- footnotes -->

[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^wiki-vt]: Wikipedia, *Threshold voltage*.
    <https://en.wikipedia.org/wiki/Threshold_voltage>
[^wiki-mtcmos]: Wikipedia, *Multi-threshold CMOS*.
    <https://en.wikipedia.org/wiki/Multi-threshold_CMOS>
[^itrs-04]: International Technology Roadmap for Semiconductors, *2001
    Edition: Process Integration, Devices, and Structures*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>
[^wei-1998]: L. Wei, Z. Chen, M. Johnson, K. Roy and V. De, "Design and
    optimization of low voltage high performance dual threshold CMOS
    circuits", *Proc. 35th Design Automation Conference*, pp. 489–494
    (1998). <https://doi.org/10.1109/DAC.1998.724521>
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
