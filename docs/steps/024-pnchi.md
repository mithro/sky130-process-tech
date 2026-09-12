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
whose species is public: the step list names it the "P-channel BF2
implant". Boron difluoride (BF₂⁺) is the standard way to put boron
very close to the silicon surface, because the molecular ion breaks up
on impact and "only 11/49 of its energy is carried by the boron atom",
so a beam energy the tool can control well produces a shallow boron
profile (category page; TXT-01, ch. 8). The resist is stripped at
{ref}`PCHIS <step-025>`.

Boron is p-type. In an N-well channel it *counter-dopes* the surface
and, on its own, would lower the magnitude of a PMOS threshold, not
raise it. Its appearance inside the "high Vt LV PMOS" module
(PDK-PERIPH) therefore needs explanation; the possibilities are set
out below, and none of them is confirmed publicly.

## Step category

`PNCHI` is an {ref}`Ion implantation <category-implant>` step of the
*threshold/channel* class — keV, light dose, medium-current tool —
and specifically a shallow BF₂ implant of the kind the category page
describes for placing boron near the surface.

## Why this step exists

The physics of a two-implant channel gives three candidate roles for a
shallow boron dose in a high-Vt PMOS:

1. **Surface compensation in a retrograde channel.** The deeper
   n-type implant of {ref}`PCHI <step-023>` can be made heavier than
   the threshold alone requires, so that it also controls punch-through
   and drain-induced barrier lowering; a shallow BF₂ dose then trims
   the *surface* concentration back to the value that gives the wanted
   |Vt|. The net result is a steeper retrograde profile — high doping
   a few tens of nanometres down, lighter at the surface — which is
   exactly what ITRS 2001's "Retrograde channel depth" of 21–30 nm
   (ITRS-01) and the super-steep-retrograde literature describe
   (THOMPSON-1996). This is our preferred reading.
2. **Buried-channel PMOS.** If the PMOS gate were n⁺ polysilicon, a
   shallow boron layer would be needed in *every* PMOS to bring |Vt|
   into range, and the high-Vt variant would use a *smaller* boron
   dose than the baseline. That would require the baseline PMOS to
   receive its own BF₂ elsewhere, and the step list used in this reference shows no
   such step; we consider it unlikely at 130 nm (TXT-04).
3. **Junction or field engineering under the gate edge.** A light
   boron dose at the channel surface changes the source/drain
   extension junction abruptness and the gate-edge field; some
   high-Vt devices are tuned this way (PAT-VT-RRR describes a
   "boron type of implant such as BF₂, or Indium" as a second Vt
   adjustment applied in combination with an arsenic first
   adjustment).

Whichever applies, the aim is the same: a `pfet_01v8_hvt` with the
higher threshold, lower leakage and acceptable short-channel behaviour
that the PDK models (PDK-07), delivered through a single extra mask.

## How it is typically performed

An industry-generic shallow BF₂ channel implant for a 200 mm,
130 nm-era fab (SKY130 values not public):

* **Species and source.** BF₂⁺ selected by the analysing magnet from a
  boron trifluoride (BF₃) plasma (WIKI-IMPLANT; category page). The
  fluorine co-implanted with the boron is a known side effect: it
  amorphises the surface slightly, which helps suppress channelling,
  and it can retard boron diffusion during the anneal (TXT-01,
  ch. 8).
* **Energy.** Tens of keV of BF₂ energy, corresponding to a boron
  energy of a few keV and a projected range of tens of nanometres.
  Public examples: BF₂ "at an energy of from about 10 to about 100
  kilo-electron volts (keV)" for a channel implant in a Cypress SONOS
  patent (PAT-04); "45-90 KeV for BF₂" in an AMD channel-implant
  example (PAT-VT-AMD).
* **Dose.** Light: "a dose of from about 1e12 cm⁻² to about 1e14
  cm⁻²" in the Cypress example (PAT-04); "about 1.0 to 2.5×10¹³
  ions/cm²" in the AMD example (PAT-VT-AMD). A compensating trim in a
  high-Vt device would sit at the bottom of these ranges (inference).
* **Tilt and twist.** 7° with twist (WIKI-IMPLANT); with BF₂ the
  self-amorphisation makes channelling less of a concern than with
  bare boron.
* **Screen oxide.** Through the pad oxide (PAT-04); a shallow implant
  is sensitive to the oxide's thickness, so the oxide loss in the
  preceding strips matters (see {ref}`LVTPIS <step-021>`).
* **Anneal.** {ref}`RTAI <step-034>`; boron in a shallow layer is the
  dopant most affected by transient enhanced diffusion, which is one
  argument for a rapid rather than a furnace anneal (category page on
  {ref}`anneal <category-anneal>`).

## Machines typically used

* **Medium-current implanter** with BF₂ capability: Axcelis (Eaton)
  8250/8250HT (AXCELIS-8250), Varian E220/E500, Nissin (category
  page).
* **Thermal-wave** dose monitor.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current** — its public species list is
  "B11, BF2, As" with "1e11 to 1e14" dose and "0-60 deg tilt"
  (SKW-01): BF₂ is explicitly available. Strength: **strong** for the
  tool; assignment is an **inference** from capability and from the
  step immediately preceding it ({ref}`PCHI <step-023>`) plausibly
  running on the same tool.
* **Axcelis GSD** lists BF₂ too (SKW-01). Strength: strong for
  existence, weak for assignment.

## Resources required

* **Boron trifluoride (BF₃)** source gas, delivered in sub-atmospheric
  cylinders (WIKI-IMPLANT; category page). Fluorinated species erode
  ion-source parts faster than hydrides, so source-consumable usage
  is higher (AXCELIS-GSD-PAGE notes "source operating costs especially
  with fluorinated species").
* Support gases, cryopump and beam-line consumables, monitor wafers.
* No new resist: the {ref}`HVTPM <step-022>` resist is reused.

## Related steps and cross-references

* Previous: {ref}`PCHI <step-023>`; next: {ref}`PCHIS <step-025>`
  (strip); mask: {ref}`HVTPM <step-022>`.
* Baseline PMOS channel: {ref}`LVTPI <step-020>`.
* The other shallow p-type implants in the flow are the P⁺ source/drain implants (species not given in the step list) {ref}`PSDI <step-082>`/{ref}`2PSDI <step-083>`.
* Activated at {ref}`RTAI <step-034>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 (Axcelis 8250 "B11, BF2, As").
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **PDK-07** — SkyWater PDK Authors, *Device Details*
  (`pfet_01v8_hvt`).
  <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
* **PDK-PERIPH** — SkyWater PDK Authors, *Periphery rules* (`hvtp`:
  "Vt adjust implant region for high Vt LV PMOS").
  <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
* **PAT-04** — K. Ramkumar et al. (Cypress), US 8,796,098 B1, granted
  2014-08-05 (BF₂ 10–100 keV, 1e12–1e14 cm⁻²).
  <https://patents.google.com/patent/US8796098B1/en>
* **AXCELIS-8250** — Semiconductor Online, *8250HT Medium Current Ion
  Implanter*.
  <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
* **AXCELIS-GSD-PAGE** — Axcelis Technologies, *GSD Ovation* product page
  (fluorinated-species source costs).
  <https://www.axcelis.com/products/gsd-ovation/>

### High-level understanding

* **WIKI-IMPLANT** — Wikipedia, *Ion implantation*.
  <https://en.wikipedia.org/wiki/Ion_implantation>
* **TXT-01** — J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon
  VLSI Technology*, Prentice Hall, 2000, ISBN 978-0-13-085037-9, ch. 8
  (BF₂ implantation, fluorine effects).
  <https://openlibrary.org/isbn/9780130850379>
* **TXT-04** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3*,
  Lattice Press, 1995, ISBN 978-0-9616721-5-7.
  <https://openlibrary.org/isbn/9780961672157>

### Deep dive

* **ITRS-01** — ITRS 2001, *Front End Processes* (Table 51 retrograde
  channel depth).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
* **THOMPSON-1996** — S. Thompson, P. Packan and M. Bohr, *1996
  Symposium on VLSI Technology*, pp. 154–155,
  DOI 10.1109/VLSIT.1996.507830.
* **PAT-VT-RRR** — US 2011/0006372 A1 (Round Rock Research), published
  2011-01-13 ("boron type of implant such as BF2, or Indium").
  <https://patents.google.com/patent/US20110006372A1/en>
* **PAT-VT-AMD** — US 6,238,982 B1 (AMD), granted 2001-05-29 (BF₂
  45–90 keV, 1–2.5 × 10¹³ cm⁻²).
  <https://patents.google.com/patent/US6238982B1/en>

## Open questions

* The role of a p-type (BF₂) implant inside the high-Vt PMOS module
  is not explained by any public source; the retrograde-channel
  compensation reading above is our inference.
* Energy, dose and the order of `PCHI`/`PNCHI` relative to each other
  in profile depth are not public.
* The expansion of the acronym `PNCHI` is not public; we use only the
  step list's "P-channel BF2 implant".
