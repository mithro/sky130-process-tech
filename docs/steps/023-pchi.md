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
windows of {ref}`HVTPM <step-022>`, the high-Vt P-channel mask. It
adds dopant to the surface of the N-well under the future gates of the
PMOS transistors drawn with the `hvtp` layer, on top of the baseline
PMOS channel doping that every N-well received at
{ref}`LVTPI <step-020>`. Its companion, {ref}`PNCHI <step-024>`, is
named in the step list as a BF₂ implant; `PCHI` itself carries no
species in its public name. The resist is stripped at
{ref}`PCHIS <step-025>`.

The PDK describes the `hvtp` region as the "Vt adjust implant region
for high Vt LV PMOS" (PDK-PERIPH) and the resulting device as the
"1.8V high-VT PMOS FET", `pfet_01v8_hvt`, modelled for V_DS and V_GS
from 0 to −1.95 V (PDK-07). The same implant, applied to a varactor,
gives `cap_var_hvt`, the "high VT PMOS device option" (PDK-07).

## Step category

`PCHI` is an {ref}`Ion implantation <category-implant>` step of the
*threshold-adjust* class: light dose, tens of keV, medium-current
tool, through the pad/screen oxide (category page). It is the third
threshold implant of the module after {ref}`LVTNI <step-015>` and
{ref}`LVTPI <step-020>`.

## Why this step exists

The threshold of a PMOS in an N-well rises in magnitude with the
n-type doping at the surface of the channel (WIKI-VT; WIKI-MTCMOS).
`LVTPI` sets that doping for the standard PMOS; `PCHI` and `PNCHI`
add to it where a higher |Vt| is wanted. The motive is leakage:
"Typical high Vth devices reduce static leakage by 10 times compared
with low Vth devices" (WIKI-MTCMOS), and a 130 nm low-power process
needs a high-Vt option to make standby-current targets in cells that
are not speed-critical (ITRS-04; WEI-1998). The PDK's inverter-delay
tables for `nfet_01v8`/`pfet_01v8_hvt` combinations (PDK-07)
quantify the speed that is traded for it.

A second, more physical reason to split the high-Vt adjust into two
implants is profile shaping. A single shallow implant that raises the
surface concentration enough to move the threshold also raises the
body effect and degrades mobility; pairing a deeper implant that
controls short-channel behaviour with a shallower one that sets Vt is
the "retrograde channel" approach that ITRS 2001 tabulates
("Retrograde channel depth (nm)" 21–30 nm for the 2001 high-
performance node, ITRS-01) and that Thompson, Packan and Bohr analysed
for its drive-current trade-offs (THOMPSON-1996). We infer, without
public confirmation, that `PCHI` and `PNCHI` divide these roles
between them.

## How it is typically performed

An industry-generic high-Vt PMOS channel implant for a 200 mm,
130 nm-era fab. SKY130's species, energy and dose are not public.

* **Species.** To raise |Vt| of a surface-channel PMOS the added
  dopant is n-type — arsenic (shallow, slow-diffusing) or phosphorus
  (deeper for a given energy) (TXT-04). The Round Rock/Micron multi-Vt
  patent uses "an implant of Arsenic" for exactly this purpose
  (PAT-VT-RRR). An indium implant, which is p-type, is used for
  *NMOS* retrograde channels (SHAHIDI-1993) and is not a candidate
  here. Arsenic is the more plausible species, and is on the public
  species list of SkyWater's medium-current tool (SKW-01).
* **Energy and dose.** Tens of keV; of order 10¹²–10¹³ cm⁻² (category
  page; the boron-side analogues in PAT-VT-LSI are "doses between
  1×10¹² and 1×10¹³ atoms/cm²" at 50–100 keV). A high-Vt adjust is by
  definition a *small* increment over the baseline, so its dose is at
  the low end of the range — a few 10¹² cm⁻² is illustrative.
* **Tilt and twist.** 7° with twist (WIKI-IMPLANT; TXT-02).
* **Screen oxide.** The pad oxide (10–20 nm in the Cypress SONOS
  patent, PAT-04) randomises the beam and traps recoils.
* **Charge control.** Electron shower on a cooled electrostatic chuck
  (SKW-01 lists "ESC chuck, E shower").
* **Anneal.** None until {ref}`RTAI <step-034>`.
* **Monitoring.** Thermal-wave on product; sheet resistance on
  monitors after a monitor anneal.

## Machines typically used

* **Medium-current implanter** with serial end station: Axcelis
  (Eaton) 8250/8250HT ("3keV to 750keV", "between 4µA and 3,500µA",
  AXCELIS-8250), Varian E220/E500, Nissin (category page).
* **Thermal-wave** dose monitor.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current** — "B11, BF2, As, ESC chuck, E
  shower, 1e11 to 1e14, 0-60 deg tilt" (SKW-01). Arsenic and the dose
  window match. Strength: **strong** for the tool; assignment is an
  **inference**.
* **Axcelis GSD** (SKW-01) is capable but is the well/source-drain
  workhorse. Strength: strong for existence, weak for assignment.

## Resources required

* **Arsine (AsH₃)** or **phosphine (PH₃)** source gas (WIKI-IMPLANT).
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

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30.
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **PDK-07** — SkyWater PDK Authors, *Device Details*
  (`pfet_01v8_hvt`, `cap_var_hvt`, inverter delay tables).
  <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
* **PDK-PERIPH** — SkyWater PDK Authors, *Periphery rules* (`hvtp`
  function text).
  <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
* **PAT-04** — K. Ramkumar et al. (Cypress), US 8,796,098 B1, granted
  2014-08-05 (pad oxide under the implants).
  <https://patents.google.com/patent/US8796098B1/en>
* **AXCELIS-8250** — Semiconductor Online, *8250HT Medium Current Ion
  Implanter*.
  <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>

### High-level understanding

* **WIKI-IMPLANT** — Wikipedia, *Ion implantation*.
  <https://en.wikipedia.org/wiki/Ion_implantation>
* **WIKI-VT** — Wikipedia, *Threshold voltage*.
  <https://en.wikipedia.org/wiki/Threshold_voltage>
* **WIKI-MTCMOS** — Wikipedia, *Multi-threshold CMOS*.
  <https://en.wikipedia.org/wiki/Multi-threshold_CMOS>
* **TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the
  VLSI Era, Vol. 1*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4, ch. 9.
  <https://openlibrary.org/isbn/9780961672164>
* **TXT-04** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3*,
  Lattice Press, 1995, ISBN 978-0-9616721-5-7 (channel engineering of
  submicron PMOS).
  <https://openlibrary.org/isbn/9780961672157>

### Deep dive

* **ITRS-01** — ITRS 2001, *Front End Processes* (Table 51 retrograde
  channel depth).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
* **ITRS-04** — ITRS 2001, *Process Integration, Devices, and
  Structures*.
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>
* **THOMPSON-1996** — S. Thompson, P. Packan and M. Bohr, "Linear
  versus saturated drive current: tradeoffs in super steep retrograde
  well engineering", *1996 Symposium on VLSI Technology, Digest of
  Technical Papers*, pp. 154–155, DOI 10.1109/VLSIT.1996.507830.
* **PAT-VT-RRR** — US 2011/0006372 A1 (Round Rock Research), published
  2011-01-13.
  <https://patents.google.com/patent/US20110006372A1/en>
* **PAT-VT-LSI** — US 5,963,801 A (LSI Logic), granted 1999-10-05.
  <https://patents.google.com/patent/US5963801A/en>
* **SHAHIDI-1993** — G. G. Shahidi et al., *IEEE Electron Device
  Letters*, vol. 14, no. 8, pp. 409–411, 1993, DOI 10.1109/55.225595.
* **WEI-1998** — L. Wei et al., *Proc. 35th DAC*, pp. 489–494, 1998,
  DOI 10.1109/DAC.1998.724521.

## Open questions

* The species (arsenic versus phosphorus), energy and dose of `PCHI`
  are not public.
* How the two implants `PCHI` and `PNCHI` divide the job of raising
  the PMOS threshold — and why one of them is a BF₂ (p-type) implant
  in a module that raises a PMOS threshold — is discussed on the
  {ref}`PNCHI <step-024>` page and remains open.
