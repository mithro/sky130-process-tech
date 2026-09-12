(step-032)=
# Step 032 — PWDEI2: PWDEI2 implant

| | |
|---|---|
| **Step number** | 32 of 171 |
| **Step code** | `PWDEI2` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`PWDEI1 <step-031>` |
| **Next step** | {ref}`PWDEIS <step-033>` |

## What this step is

`PWDEI2` is the second boron implant into the `pwde` regions of the
20 V devices, run through the {ref}`PWDEM <step-030>` resist directly
after {ref}`PWDEI1 <step-031>`. It is the last implant of the well and
channel module; only the {ref}`PWDEIS <step-033>` strip and the
{ref}`RTAI <step-034>` anneal remain before the flow moves on to the
SONOS module at {ref}`TUNM <step-035>`. As with the other "2" implants
of the module, its name is the only public description; we infer a
second energy of the same species, completing a two-member chained
profile for the lightly doped drain-extended P-well (inference;
TXT-01, ch. 2).

## Step category

`PWDEI2` is an {ref}`Ion implantation <category-implant>` step of the
*well* class at light dose; tool class as for
{ref}`PWDEI1 <step-031>`.

## Why this step exists

A drift region is not a uniform slab. The classic design has doping
that is heaviest under the drain contact — to keep on-resistance low
and to make an ohmic transition to the n⁺ or p⁺ drain — and lightest
next to the channel, where the peak electric field occurs at the gate
edge and where the region must deplete first; and it needs a defined
depth so that the depletion spreads vertically as well as laterally
(a RESURF-type balance; TXT-04). Two implants at different energies
and doses are the minimum that can approximate this: Wikipedia's
description of LDMOS drift regions "fabricated using up to three ion
implantation sequences in order to achieve the appropriate doping
profile needed to withstand high electric fields" (WIKI-LDMOS) is the
general statement. The 20 V devices of SKY130 are specified with a
"Longer drift region" than the 16 V ones (PDK-07) and the same
110 Å gate oxide (PDK-HV), so the drift doping and depth are doing
all the work of holding off the extra voltage.

There is also a coupling with the standard wells. Where `pwde` sits
inside a deep-N-well tub (pwdem.5, PDK-PERIPH), the lightly doped
P-well must reach down to, but not merge into, the buried N-type
floor from {ref}`DNI <step-008>`; the deeper member of the pair sets
that junction.

## How it is typically performed

An industry-generic second drift-well implant for a 200 mm,
130 nm-era fab (illustrative values only):

* **Species.** Boron (¹¹B⁺) from BF₃ (WIKI-IMPLANT).
* **Energy.** Different from `PWDEI1` — one member at a few hundred
  keV to set depth, one at tens of keV to set the surface/contact
  region, in the pattern of chained wells (PAT-WELL-IBM,
  PAT-WELL-HYNIX). Which member `PWDEI2` is, is not public.
* **Dose.** Of order 10¹² cm⁻²; the Texas Instruments DE patent's
  2 × 10¹²–7 × 10¹³ cm⁻² for a 5–12 V-class p-type drift region
  (PAT-DEMOS-TI) is an upper bound for a 20 V design (inference).
* **Tilt and twist.** 7° with twist (WIKI-IMPLANT).
* **Sequence.** Back-to-back with `PWDEI1` on the same tool if the
  energies allow.
* **Anneal.** {ref}`RTAI <step-034>`, plus the remaining front-end
  thermal budget — a lightly doped, deep well is the profile least
  affected by the later short anneals (category page on
  {ref}`anneal <category-anneal>`).

## Machines typically used

* **Medium-current implanter** (Axcelis 8250HT "3keV to 750keV",
  AXCELIS-8250; Varian E500) for light doses at moderate energy, or
  a **high-energy batch implanter** (Axcelis GSD/HE) for the deep
  member.
* **Four-point probe** metrology on monitor wafers.

## Machines likely used at SkyWater

* **Axcelis 8250** ("B11, BF2, As … 1e11 to 1e14, 0-60 deg tilt",
  SKW-01). Strength: **strong** for the tool; assignment is an
  **inference**.
* **Axcelis GSD** ("B11 … 10-3000kev", SKW-01). Strength: strong for
  existence, weak for assignment.

## Resources required

* **Boron trifluoride (BF₃)**; support gases; cryopump and source
  consumables; monitor wafers (category page).
* No new resist: the {ref}`PWDEM <step-030>` resist is reused.

## Related steps and cross-references

* Previous: {ref}`PWDEI1 <step-031>`; next: {ref}`PWDEIS <step-033>`
  (strip); mask: {ref}`PWDEM <step-030>`.
* The main-well pairs: {ref}`NWI <step-018>`/{ref}`NWI2 <step-019>`,
  {ref}`PWI <step-027>`/{ref}`PWI2 <step-028>`.
* Activated at {ref}`RTAI <step-034>`; the gate oxide of the 20 V
  devices is grown at {ref}`GOX100 <step-043>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30.
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **PDK-07** — SkyWater PDK Authors, *Device Details* (20 V devices:
  "Longer drift region").
  <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
* **PDK-HV** — SkyWater PDK Authors, *High Voltage Methodology* (110 Å
  gate oxide on VHV devices).
  <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
* **PDK-PERIPH** — SkyWater PDK Authors, *Periphery rules* (pwdem.5,
  pwdem.6).
  <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
* **AXCELIS-8250** — Semiconductor Online, *8250HT Medium Current Ion
  Implanter*.
  <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>

### High-level understanding

* **WIKI-LDMOS** — Wikipedia, *LDMOS*.
  <https://en.wikipedia.org/wiki/LDMOS>
* **WIKI-IMPLANT** — Wikipedia, *Ion implantation*.
  <https://en.wikipedia.org/wiki/Ion_implantation>
* **TXT-01** — J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon
  VLSI Technology*, Prentice Hall, 2000, ISBN 978-0-13-085037-9,
  ch. 2 and ch. 8.
  <https://openlibrary.org/isbn/9780130850379>
* **TXT-04** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3*,
  Lattice Press, 1995, ISBN 978-0-9616721-5-7.
  <https://openlibrary.org/isbn/9780961672157>

### Deep dive

* **PAT-DEMOS-TI** — J. C. Mitros (TI), US 6,660,603 B2, granted
  2003-12-09.
  <https://patents.google.com/patent/US6660603B2/en>
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

* Energy, dose and the depth ordering of `PWDEI1`/`PWDEI2` are not
  public; that they form a chained pair is inferred from the names.
* Whether the `pwde` well also carries a threshold-setting component
  for the 20 V NMOS channel, or whether that comes from later channel
  implants, is unknown.
