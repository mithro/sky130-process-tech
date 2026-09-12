(step-031)=
# Step 031 — PWDEI1: PWDEI1 implant

| | |
|---|---|
| **Step number** | 31 of 171 |
| **Step code** | `PWDEI1` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`PWDEM <step-030>` |
| **Next step** | {ref}`PWDEI2 <step-032>` |

## What this step is

`PWDEI1` is the first of two boron implants placed through the
{ref}`PWDEM <step-030>` resist into the `pwde` regions — "Regions to
receive p-well drain-extended implants"[^pdk-06] — of the 20 V devices.
Together with {ref}`PWDEI2 <step-032>` it builds a *lightly doped
P-well* that serves as the drift (drain-extension) region of the 20 V
PMOS and, we infer, as the low-doped body of the 20 V NMOS whose
standard P-well was blocked at {ref}`PWBM <step-026>`. The code reads as
"P-well drain-extended implant 1"; the "1"/"2" numbering tells us the
well is a chained, two-energy implant like the main wells
({ref}`NWI <step-018>`/{ref}`NWI2 <step-019>`,
{ref}`PWI <step-027>`/{ref}`PWI2 <step-028>`). That is our inference
from the names; no public document describes the two implants. The
resist is stripped at {ref}`PWDEIS <step-033>`.

## Step category

`PWDEI1` is an {ref}`Ion implantation <category-implant>` step of the
*well* class, but with a twist: the aim is a doping *lower* than the
standard well, so its dose is at the light end of the well range and
its energy is chosen for the depth the drift region must have.

## Why this step exists

A drain-extended MOSFET holds off voltage in a drift region that
depletes before the gate oxide or the channel junction breaks down: "a
very lightly doped extension region adjacent to the drain that depletes
at high drain voltages".[^pat-demos-ti] The trade is one-dimensional
physics — the lower the doping, the wider the depletion region and the
higher the breakdown voltage, but the higher the on-resistance — and it
is set by implantation: in LDMOS-type devices "the drift region of this
power MOSFET is fabricated using up to three ion implantation sequences
in order to achieve the appropriate doping profile needed to withstand
high electric fields".[^wiki-ldmos] SKY130's 20 V devices are modelled
to V_DS = ±22 V with the same 5.5 V gate rating as the 5 V
devices,[^pdk-07] on a 110 Å gate oxide;[^pdk-hv] that combination is
only possible with a drift region far more lightly doped than the 4 ×
10¹⁷ cm⁻³ standard P-well.[^pdk-03]

Texas Instruments' DE devices for a 0.18 µm logic process[^mitros-2001]
used the existing wells as drift regions; the companion patent gives
boron "at doses of 2×10¹² cm² to 7×10¹³ cm² at energies of about 40 keV"
for the p-type well and "phosphorous species at about 8×10¹² cm² to
7×10¹³ cm² at an energy of about 150 keV" for the n-type
one;[^pat-demos-ti] SKY130 does the same for its 16 V devices ("drain
extentions (DE) fabricated by lightly doped Nwells and Pwells")[^pdk-hv]
but adds a dedicated, lighter P-well for the 20 V family. Without
`PWDEI1`/`PWDEI2` there would be no 20 V PMOS drift region and the
`nfet_20v0`/`pfet_20v0` devices, the "20+V" of SkyWater's platform
description,[^skw-02] could not be made.

## How it is typically performed

An industry-generic drain-extension well implant for a 200 mm,
130 nm-era fab. SKY130's values are not public; the figures are
illustrative.

* **Species.** Boron (¹¹B⁺) from BF₃.[^wiki-implant] The layer name
  ("p-well drain-extended") fixes the polarity.
* **Energy.** A drift region wants a graded profile that is deepest near
  the drain contact; a deep member at a few hundred keV and a shallower
  one give the grading, the same architecture as the main
  wells[^pat-well-ibm][^pat-well-hynix] but at lower dose. The TI
  example uses 40 keV for a shallow p-type drift;[^pat-demos-ti] a
  deeper, higher-voltage design would go higher.
* **Dose.** Light — of order 10¹² cm⁻² per implant — so that the drift
  region fully depletes at 20 V. The TI range of 2 × 10¹²–7 ×
  10¹³ cm⁻²[^pat-demos-ti] is for 5–12 V-class devices; a 20 V design at
  a fixed drift length would sit at or below its lower end (inference;
  see the RESURF-type design discussion in Wolf vol. 3[^txt-04]).
* **Tilt and twist.** 7° with twist;[^wiki-implant] the drift region is
  long, so tilt shadowing at the resist edge is a small fraction of it.
* **Wafer handling and anneal.** As for {ref}`PWI <step-027>`;
  activation at {ref}`RTAI <step-034>`, after which the lightly doped
  well sees the remaining front-end thermal budget.
* **Monitoring.** Sheet resistance on monitor wafers; the drift region's
  sheet resistance is one of the device's key parameters.

## Machines typically used

* **High-energy batch implanter** (Axcelis GSD/HE, Varian VIISta 3000)
  or **medium-current implanter** (Axcelis 8250HT "3keV to
  750keV")[^axcelis-8250] depending on energy; a light-dose,
  moderate-energy boron implant is natural work for the medium-current
  tool (category page).
* **Four-point probe** metrology.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current** ("B11, BF2, As … 1e11 to
  1e14"):[^skw-01] boron and the dose window match a light drift-well
  implant. Strength: **strong** for the tool; assignment is an
  **inference**.
* **Axcelis GSD** ("B11 … 10-3000kev")[^skw-01] if the energy is above
  the 8250's reach. Strength: strong for existence.

## Resources required

* **Boron trifluoride (BF₃)**; support gases; cryopump and source
  consumables; monitor wafers (category page).
* No new resist: the {ref}`PWDEM <step-030>` resist is reused.

## Related steps and cross-references

* Previous: {ref}`PWDEM <step-030>` (mask); next:
  {ref}`PWDEI2 <step-032>`; strip at {ref}`PWDEIS <step-033>`.
* The standard P-well it replaces: {ref}`PWI <step-027>`; the deep
  N-well tub it sits in: {ref}`DNI <step-008>`; the N-well drift
  regions of the DE NMOS: {ref}`NWI <step-018>`.
* Activated at {ref}`RTAI <step-034>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — the site tool list.[^skw-01]
* SkyWater, *Mixed-Signal CMOS & ROIC* platform table — "20+V,
  Drain-Extended CMOS (16V)".[^skw-02]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `pwde`
  124:20.[^pdk-06]
* SkyWater PDK, *Device Details* — 20 V devices, operating
  voltages.[^pdk-07]
* SkyWater PDK, *High Voltage Methodology* — drain extensions
  "fabricated by lightly doped Nwells and Pwells".[^pdk-hv]
* SkyWater PDK, *Criteria & Assumptions* — P-well peak
  concentration.[^pdk-03]
* Semiconductor Online, *8250HT Medium Current Ion Implanter* — the
  Eaton/Axcelis 8250HT energy and beam-current ranges.[^axcelis-8250]

### High-level understanding

* Wikipedia, *LDMOS* — drift regions formed by chained
  implants.[^wiki-ldmos]
* Wikipedia, *Ion implantation* — energies, sources, channelling and
  tilt in one page.[^wiki-implant]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — drain
  engineering, high-voltage MOS.[^txt-04]

### Deep dive

* Mitros (Texas Instruments), US 6,660,603 — DE definition; p-type drift
  boron 40 keV, 2 × 10¹²–7 × 10¹³ cm⁻².[^pat-demos-ti]
* Chidambaram (Texas Instruments), US 2006/0006461 — DE devices "without
  the addition of extra masks or processing steps".[^pat-demos-ti2]
* Mitros et al. (Texas Instruments), *IEEE TED* 2001 — drain-extended
  MOS transistors added to a 0.18 µm logic process.[^mitros-2001]
* Mai and Rücker (IHP), *Solid-State Electronics* 2011 — 10 V
  drain-extended devices in a 0.13 µm technology.[^mai-2011]
* Breitwisch, Lam and Slinkman (IBM), US 6,667,205 — retrograde N-well
  and P-well energies, doses and resist thickness.[^pat-well-ibm]
* Lee and Son (Hyundai/Hynix), US 6,455,402 — chained retrograde
  twin-well implants and a 1000 °C, 10 s RTA.[^pat-well-hynix]
* Appels and Vaes (Philips), IEDM 1979 — the original RESURF paper: the
  physics of a fully depleting drift layer.[^appels-1979]
* Ludikhuize (Philips), ISPSD 2000 — a review of RESURF design rules
  relating drift dose to breakdown.[^ludikhuize-2000]
* Baliga, *Fundamentals of Power Semiconductor Devices* — breakdown,
  drift-region doping and on-resistance trade-offs.[^baliga-2008]
* Efland, Tsai and Pendharkar (Texas Instruments), IEDM 1998 — LDMOS
  integration into logic CMOS from the TI group behind the DE
  devices.[^efland-1998]
* Kwon, Efland, Malhi and Ng (Texas Instruments), US 5,406,110 — a
  RESURF lateral DMOS with an implanted drift region.[^pat-resurf-ti]
* Bourdelle et al. (Agere), *IEEE TED* 2002 — how a MeV well dose trades
  device performance against junction leakage.[^bourdelle-2002]

## Open questions

* The species is inferred from the layer name; energy and dose are
  not public.
* Whether the `pwde` well is the drift region of the 20 V PMOS, the
  body of the 20 V NMOS, or both, is inferred from the rule geometry.
* Whether `PWDEI1` is the deeper or the shallower member of the pair
  is unknown.

<!-- footnotes -->

[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, google/skywater-pdk repository.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pat-demos-ti]: J. C. Mitros (Texas Instruments), *Higher voltage drain
    extended MOS transistors with self-aligned channel and drain
    extensions*, US 6,660,603 B2, granted 2003-12-09.
    <https://patents.google.com/patent/US6660603B2/en>
[^wiki-ldmos]: Wikipedia, *LDMOS*. <https://en.wikipedia.org/wiki/LDMOS>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^mitros-2001]: J. C. Mitros, C.-Y. Tsai, H. Shichijo, M. Kunz, A.
    Morton, D. Goodpaster, D. Mosher and T. R. Efland, "High-voltage
    drain extended MOS transistors for 0.18-µm logic CMOS process",
    *IEEE Transactions on Electron Devices* **48**(8), 1751–1755 (2001).
    <https://doi.org/10.1109/16.936703>
[^skw-02]: SkyWater Technology, *Mixed-Signal CMOS & ROIC*, platform
    table, accessed 2026-08-30.
    <https://www.skywatertechnology.com/cmos/>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^pat-well-ibm]: M. J. Breitwisch, C. H. Lam and J. A. Slinkman (IBM),
    *Method of forming retrograde n-well and p-well*, US 6,667,205 B2,
    granted 2003-12-23.
    <https://patents.google.com/patent/US6667205B2/en>
[^pat-well-hynix]: J.-H. Lee and J.-H. Son (Hyundai/Hynix), *Method of
    forming retrograde doping profile in twin well CMOS device*, US
    6,455,402 B2, granted 2002-09-24.
    <https://patents.google.com/patent/US6455402B2/en>
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion
    Implanter* (Eaton Semiconductor Equipment Operations product
    description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^txt-04]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
    Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
    <https://openlibrary.org/isbn/9780961672157>
[^pat-demos-ti2]: P. R. Chidambaram (Texas Instruments), *Drain extended
    MOS transistors and methods for making the same*, US 2006/0006461
    A1, published 2006-01-12.
    <https://patents.google.com/patent/US20060006461A1/en>
[^mai-2011]: A. Mai and H. Rücker, "Drain-extended MOS transistors
    capable for operation at 10 V and at radio frequencies",
    *Solid-State Electronics* **65–66**, 45–50 (2011).
    <https://doi.org/10.1016/j.sse.2011.06.034>
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
[^bourdelle-2002]: K. K. Bourdelle, S. Chaudhry and J. Chu, "The effect
    of triple well implant dose on performance of NMOS transistors",
    *IEEE Transactions on Electron Devices* **49**(3), 521–524 (2002).
    <https://doi.org/10.1109/16.987125>
