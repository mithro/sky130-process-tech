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
receive p-well drain-extended implants" (PDK-06) — of the 20 V
devices. Together with {ref}`PWDEI2 <step-032>` it builds a *lightly
doped P-well* that serves as the drift (drain-extension) region of the
20 V PMOS and, we infer, as the low-doped body of the 20 V NMOS whose
standard P-well was blocked at {ref}`PWBM <step-026>`. The code reads
as "P-well drain-extended implant 1"; the "1"/"2" numbering tells us
the well is a chained, two-energy implant like the main wells
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
depletes before the gate oxide or the channel junction breaks down:
"a very lightly doped extension region adjacent to the drain that
depletes at high drain voltages" (PAT-DEMOS-TI). The trade is
one-dimensional physics — the lower the doping, the wider the
depletion region and the higher the breakdown voltage, but the higher
the on-resistance — and it is set by implantation: in LDMOS-type
devices "the drift region of this power MOSFET is fabricated using up
to three ion implantation sequences in order to achieve the
appropriate doping profile needed to withstand high electric fields"
(WIKI-LDMOS). SKY130's 20 V devices are modelled to V_DS = ±22 V with
the same 5.5 V gate rating as the 5 V devices (PDK-07), on a 110 Å
gate oxide (PDK-HV); that combination is only possible with a drift
region far more lightly doped than the 4 × 10¹⁷ cm⁻³ standard P-well
(PDK-03).

Texas Instruments' DE devices for a 0.18 µm logic process (MITROS-2001) used the existing wells as drift regions; the companion patent gives boron "at doses of 2×10¹² cm² to 7×10¹³ cm² at energies of about 40 keV" for the p-type well and "phosphorous species at about 8×10¹² cm² to 7×10¹³ cm² at an energy of about 150 keV" for the n-type one (PAT-DEMOS-TI); SKY130 does the same for
its 16 V devices ("drain extentions (DE) fabricated by lightly doped
Nwells and Pwells", PDK-HV) but adds a dedicated, lighter P-well for
the 20 V family. Without `PWDEI1`/`PWDEI2` there would be no 20 V
PMOS drift region and the `nfet_20v0`/`pfet_20v0` devices, the
"20+V" of SkyWater's platform description (SKW-02), could not be
made.

## How it is typically performed

An industry-generic drain-extension well implant for a 200 mm,
130 nm-era fab. SKY130's values are not public; the figures are
illustrative.

* **Species.** Boron (¹¹B⁺) from BF₃ (WIKI-IMPLANT). The layer name
  ("p-well drain-extended") fixes the polarity.
* **Energy.** A drift region wants a graded profile that is deepest
  near the drain contact; a deep member at a few hundred keV and a
  shallower one give the grading, the same architecture as the main
  wells (PAT-WELL-IBM, PAT-WELL-HYNIX) but at lower dose. The TI
  example uses 40 keV for a shallow p-type drift (PAT-DEMOS-TI); a
  deeper, higher-voltage design would go higher.
* **Dose.** Light — of order 10¹² cm⁻² per implant — so that the drift
  region fully depletes at 20 V. The TI range of 2 × 10¹²–7 × 10¹³ cm⁻²
  (PAT-DEMOS-TI) is for 5–12 V-class devices; a 20 V design at a
  fixed drift length would sit at or below its lower end
  (inference; TXT-04 on RESURF-type design).
* **Tilt and twist.** 7° with twist (WIKI-IMPLANT); the drift region
  is long, so tilt shadowing at the resist edge is a small fraction
  of it.
* **Wafer handling and anneal.** As for {ref}`PWI <step-027>`;
  activation at {ref}`RTAI <step-034>`, after which the lightly doped
  well sees the remaining front-end thermal budget.
* **Monitoring.** Sheet resistance on monitor wafers; the drift
  region's sheet resistance is one of the device's key parameters.

## Machines typically used

* **High-energy batch implanter** (Axcelis GSD/HE, Varian VIISta
  3000) or **medium-current implanter** (Axcelis 8250HT "3keV to
  750keV", AXCELIS-8250) depending on energy; a light-dose,
  moderate-energy boron implant is natural work for the
  medium-current tool (category page).
* **Four-point probe** metrology.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current** ("B11, BF2, As … 1e11 to 1e14",
  SKW-01): boron and the dose window match a light drift-well
  implant. Strength: **strong** for the tool; assignment is an
  **inference**.
* **Axcelis GSD** ("B11 … 10-3000kev", SKW-01) if the energy is above
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

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30.
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **SKW-02** — SkyWater Technology, *Mixed-Signal CMOS & ROIC* ("20+V,
  Drain-Extended CMOS (16V)").
  <https://www.skywatertechnology.com/cmos/>
* **PDK-06** — SkyWater PDK Authors, `gds_layers.csv` (`pwde` 124:20).
  <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
* **PDK-07** — SkyWater PDK Authors, *Device Details* (20 V devices,
  operating voltages).
  <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
* **PDK-HV** — SkyWater PDK Authors, *High Voltage Methodology*.
  <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
* **PDK-03** — SkyWater PDK Authors, *Criteria & Assumptions* (P-well
  peak concentration).
  <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
* **AXCELIS-8250** — Semiconductor Online, *8250HT Medium Current Ion
  Implanter*.
  <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>

### High-level understanding

* **WIKI-LDMOS** — Wikipedia, *LDMOS*.
  <https://en.wikipedia.org/wiki/LDMOS>
* **WIKI-IMPLANT** — Wikipedia, *Ion implantation*.
  <https://en.wikipedia.org/wiki/Ion_implantation>
* **TXT-04** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3*,
  Lattice Press, 1995, ISBN 978-0-9616721-5-7 (drain engineering,
  high-voltage MOS).
  <https://openlibrary.org/isbn/9780961672157>

### Deep dive

* **PAT-DEMOS-TI** — J. C. Mitros (TI), US 6,660,603 B2, granted
  2003-12-09 (DE definition; p-type drift boron 40 keV,
  2 × 10¹²–7 × 10¹³ cm⁻²).
  <https://patents.google.com/patent/US6660603B2/en>
* **PAT-DEMOS-TI2** — P. R. Chidambaram (TI), US 2006/0006461 A1,
  published 2006-01-12.
  <https://patents.google.com/patent/US20060006461A1/en>
* **MITROS-2001** — J. C. Mitros et al., *IEEE Trans. Electron
  Devices*, vol. 48, pp. 1751–1755, 2001, DOI 10.1109/16.936703.
* **MAI-2011** — A. Mai and H. Rücker, *Solid-State Electronics*,
  pp. 45–50, 2011, DOI 10.1016/j.sse.2011.06.034.
* **PAT-WELL-IBM** — US 6,667,205 B2 (IBM), granted 2003-12-23.
  <https://patents.google.com/patent/US6667205B2/en>
* **PAT-WELL-HYNIX** — US 6,455,402 B2 (Hyundai/Hynix), granted
  2002-09-24.
  <https://patents.google.com/patent/US6455402B2/en>

## Open questions

* The species is inferred from the layer name; energy and dose are
  not public.
* Whether the `pwde` well is the drift region of the 20 V PMOS, the
  body of the 20 V NMOS, or both, is inferred from the rule geometry.
* Whether `PWDEI1` is the deeper or the shallower member of the pair
  is unknown.
