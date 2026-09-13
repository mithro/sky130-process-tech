(step-032)=
# Step 032 — PWDEI2: PWDEI2 implant

| | |
|---|---|
| **Step number** | 32 of 171[^steps-sheet] |
| **Step code** | `PWDEI2` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`PWDEI1 <step-031>` |
| **Next step** | {ref}`PWDEIS <step-033>` |

## What this step is

`PWDEI2` is the second boron implant into the `pwde` regions of the 20 V
devices, run through the {ref}`PWDEM <step-030>` resist directly after
{ref}`PWDEI1 <step-031>`. It is the last implant of the well and channel
module; only the {ref}`PWDEIS <step-033>` strip and the
{ref}`RTAI <step-034>` anneal remain before the flow moves on to the
{term}`SONOS` module at {ref}`TUNM <step-035>`. As with
{ref}`NWI2 <step-019>` and {ref}`PWI2 <step-028>`, no public document
describes it; we infer, from well-building practice, a
second energy of the same species, completing a two-member chained
profile for the lightly doped {term}`drain-extended <DEMOS>` P-well
(inference).[^txt-01]

## Step category

`PWDEI2` is an {ref}`Ion implantation <category-implant>` step of the
*well* class at light dose; tool class as for
{ref}`PWDEI1 <step-031>`.

## Why this step exists

A {term}`drift region` is not a uniform slab. The classic design has doping that
is heaviest under the drain contact — to keep on-resistance low and to
make an ohmic transition to the n⁺ or p⁺ drain — and lightest next to
the channel, where the peak electric field occurs at the gate edge and
where the region must deplete first; and it needs a defined depth so
that the depletion spreads vertically as well as laterally (a
RESURF-type balance).[^txt-04] Two implants at different energies and
doses are the minimum that can approximate this: Wikipedia's description
of LDMOS drift regions "fabricated using up to three ion implantation
sequences in order to achieve the appropriate doping profile needed to
withstand high electric fields"[^wiki-ldmos] is the general statement.
The 20 V devices of SKY130 are specified with a "Longer drift region"
than the 16 V ones[^pdk-07] and the same 110 Å gate oxide,[^pdk-hv] so
the drift doping and depth are doing all the work of holding off the
extra voltage.

There is also a coupling with the standard wells. Where `pwde` sits
inside a deep-N-well tub (pwdem.5),[^pdk-periph] the lightly doped
P-well must reach down to, but not merge into, the buried N-type floor
from {ref}`DNI <step-008>`; we infer that the deeper member of the pair
sets that junction.

## How it is typically performed

An industry-generic second drift-well implant for a 200 mm,
130 nm-era fab (illustrative values only):

* **Species.** Boron (¹¹B⁺) from BF₃.[^wiki-implant]
* **Energy.** Different from `PWDEI1` — one member at a few hundred keV
  to set depth, one at tens of keV to set the surface/contact region, in
  the pattern of chained wells.[^pat-well-ibm][^pat-well-hynix] Which
  member `PWDEI2` is, is not public.
* **Dose.** Of order 10¹² cm⁻²; the Texas Instruments DE patent's 2 ×
  10¹²–7 × 10¹³ cm⁻² for a 5–12 V-class p-type drift
  region[^pat-demos-ti] is an upper bound for a 20 V design (inference).
* **Tilt and twist.** 7° with twist.[^wiki-implant]
* **Sequence.** Back-to-back with `PWDEI1` on the same tool if the
  energies allow.
* **Anneal.** {ref}`RTAI <step-034>`, plus the remaining front-end
  {term}`thermal budget` — a lightly doped, deep well is the profile least
  affected by the later short anneals (category page on
  {ref}`anneal <category-anneal>`).

## Machines typically used

* **{ref}`Medium-current implanter <machine-medium-current-implanter>`** (Axcelis 8250HT "3keV to
  750keV"[^axcelis-8250]; Varian E500) for light doses at moderate
  energy, or a **{ref}`high-energy batch implanter <machine-high-energy-implanter>`** (Axcelis GSD/HE) for the
  deep member.
* **{term}`Four-point probe <four-point probe>`** {ref}`metrology <machine-sheet-resistance-metrology>` on monitor wafers.

## Machines likely used at SkyWater

* **Axcelis 8250** ("B11, BF2, As … 1e11 to 1e14, 0-60 deg
  tilt").[^skw-01] Strength: **strong** for the tool; assignment is an
  **inference**.
* **Axcelis GSD high-current/high-energy implanter** ("B11 …
  10-3000kev").[^skw-01] Strength: strong for existence, weak for
  assignment.

## Resources required

* **{ref}`Boron trifluoride <material-dopant-sources>` (BF₃)**; support gases; cryopump and source
  consumables; {ref}`monitor wafers <material-substrates>` (category page).
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

* SkyWater, *Facilities & Capabilities* — the site tool list.[^skw-01]
* SkyWater PDK, *Device Details* — 20 V devices: "Longer drift
  region".[^pdk-07]
* SkyWater PDK, *High Voltage Methodology* — 110 Å gate oxide on VHV
  devices.[^pdk-hv]
* SkyWater PDK, *Periphery rules* — pwdem.5, pwdem.6.[^pdk-periph]
* Semiconductor Online, *8250HT Medium Current Ion Implanter* — the
  Eaton/Axcelis 8250HT energy and beam-current ranges.[^axcelis-8250]

### High-level understanding

* Wikipedia, *LDMOS* — drift regions formed by chained
  implants.[^wiki-ldmos]
* Wikipedia, *Ion implantation* — energies, sources, {term}`channelling` and
  tilt in one page.[^wiki-implant]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — ch. 2 (CMOS
  well formation) and ch. 8 (ion implantation).[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — channel
  engineering, surface- versus {term}`buried-channel PMOS`, high-voltage
  MOS.[^txt-04]

### Deep dive

* Mitros (Texas Instruments), US 6,660,603 — drain-extended MOS built on
  the existing wells, with drift-well doses and energies.[^pat-demos-ti]
* Mitros et al. (Texas Instruments), *IEEE TED* 2001 — drain-extended
  MOS transistors added to a 0.18 µm logic process.[^mitros-2001]
* Mai and Rücker (IHP), *Solid-State Electronics* 2011 — 10 V
  drain-extended devices in a 0.13 µm technology.[^mai-2011]
* Breitwisch, Lam and Slinkman (IBM), US 6,667,205 — {term}`retrograde N-well <retrograde well>`
  and P-well energies, doses and resist thickness.[^pat-well-ibm]
* Lee and Son (Hyundai/Hynix), US 6,455,402 — chained retrograde
  twin-well implants and a 1000 °C, 10 s {term}`RTA`.[^pat-well-hynix]
* Appels and Vaes (Philips), IEDM 1979 — the original RESURF paper:
  vertical and lateral depletion of a thin drift layer.[^appels-1979]
* Ludikhuize (Philips), ISPSD 2000 — a review of RESURF design rules for
  graded drift regions.[^ludikhuize-2000]
* Baliga, *Fundamentals of Power Semiconductor Devices* — breakdown,
  drift-region doping and on-resistance trade-offs.[^baliga-2008]
* Efland, Tsai and Pendharkar (Texas Instruments), IEDM 1998 — LDMOS
  integration into logic CMOS from the TI group behind the DE
  devices.[^efland-1998]
* Kwon, Efland, Malhi and Ng (Texas Instruments), US 5,406,110 — a
  RESURF lateral DMOS with an implanted drift region.[^pat-resurf-ti]
* Chidambaram (Texas Instruments), US 2006/0006461 — drain-extended MOS
  made with the existing process layers.[^pat-demos-ti2]
* Oh (Hynix), US 6,806,133 — a triple-well recipe showing how a P-well
  is placed above a deep N-well floor.[^pat-dnw-hynix]

## Open questions

* Energy, dose and the depth ordering of `PWDEI1`/`PWDEI2` are not
  public; that they form a chained pair is our inference (see
  {ref}`PWDEI1 <step-031>`).
* Whether the `pwde` well also carries a threshold-setting component
  for the 20 V NMOS channel, or whether that comes from later channel
  implants, is unknown.

<!-- footnotes -->

[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-04]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
    Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
    <https://openlibrary.org/isbn/9780961672157>
[^wiki-ldmos]: Wikipedia, *LDMOS*. <https://en.wikipedia.org/wiki/LDMOS>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
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
[^pat-demos-ti]: J. C. Mitros (Texas Instruments), *Higher voltage drain
    extended MOS transistors with self-aligned channel and drain
    extensions*, US 6,660,603 B2, granted 2003-12-09.
    <https://patents.google.com/patent/US6660603B2/en>
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion
    Implanter* (Eaton Semiconductor Equipment Operations product
    description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^mitros-2001]: J. C. Mitros, C.-Y. Tsai, H. Shichijo, M. Kunz, A.
    Morton, D. Goodpaster, D. Mosher and T. R. Efland, "High-voltage
    drain extended MOS transistors for 0.18-µm logic CMOS process",
    *IEEE Transactions on Electron Devices* **48**(8), 1751–1755 (2001).
    <https://doi.org/10.1109/16.936703>
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
[^pat-demos-ti2]: P. R. Chidambaram (Texas Instruments), *Drain extended
    MOS transistors and methods for making the same*, US 2006/0006461
    A1, published 2006-01-12.
    <https://patents.google.com/patent/US20060006461A1/en>
[^pat-dnw-hynix]: J.-G. Oh (Hynix Semiconductor), *Method for
    fabricating semiconductor device with triple well structure*, US
    6,806,133 B2, granted 2004-10-19.
    <https://patents.google.com/patent/US6806133B2/en>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
