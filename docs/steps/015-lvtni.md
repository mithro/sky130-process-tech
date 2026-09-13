(step-015)=
# Step 015 — LVTNI: Low Vt NMOS implantation

| | |
|---|---|
| **Step number** | 15 of 171[^steps-sheet] |
| **Step code** | `LVTNI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`LVTNM <step-014>` |
| **Next step** | {ref}`LVTNIS <step-016>` |

## What this step is

`LVTNI` is a channel-type ion implant performed through the resist
windows opened at {ref}`LVTNM <step-014>`. It is the first implant of
the well and channel module and — unusually — it is placed *before* the
N-well and P-well implants that follow at
{ref}`NWI <step-018>`/{ref}`NWI2 <step-019>` and
{ref}`PWI <step-027>`/{ref}`PWI2 <step-028>`. Its job is to set the
difference in threshold voltage between the low-Vt N-channel devices of
the PDK and the standard ones. The dopant enters the active silicon
through what we infer to be the pad oxide left by
{ref}`NS19 <step-013>`, acting as the {term}`screen oxide` (see the open
question there); a Cypress {term}`SONOS` patent from the same lineage describes
exactly this arrangement, with "dopants … implanted into substrate 204
through the pad oxide 209" of "about 10 nanometers (nm) to about
20 nm".[^pat-04]

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
region: in the standard body-effect expression the parameter γ contains
the doping concentration N_A,[^wiki-vt] and multi-threshold CMOS is
built by "altering the concentration of dopant atoms in the channel
region beneath the gate oxide".[^wiki-mtcmos] The 1.8 V NMOS family of
SKY130 comprises `nfet_01v8` and `nfet_01v8_lvt`;[^pdk-07] `LVTNI`,
together with the N-channel implant {ref}`NCHI <step-045>` that all
1.8 V devices receive under the low-voltage oxide mask, is what
separates the two. The same mask serves `pfet_01v8_lvt`, the native NMOS
devices and the SONOS cells,[^pdk-periph] so this step (or its absence)
also underlies the zero-Vt-class devices whose value to analogue
designers is a threshold near 0 V.

The trade is leakage: "Typical high Vth devices reduce static leakage by
10 times compared with low Vth devices".[^wiki-mtcmos] A process without
`LVTNI` would still make working logic, but only at one threshold.

## How it is typically performed

An industry-generic threshold-adjust implant for a 200 mm, 130 nm-era
fab. The SKY130 species, energy and dose are not public; the values
below are typical or taken from contemporaneous patents.

* **Species.** For an implant that *raises* an NMOS threshold the
  species is p-type: boron (¹¹B⁺), BF₂⁺ for a shallower boron placement
  (only 11/49 of the beam energy is carried by the boron atom; category
  page), or indium, a heavy p-type dopant used for steep retrograde
  channels.[^shahidi-1993][^huang-2000] Cypress's own patents describe
  BF₂ "at an energy of from about 10 to about 100 kilo-electron volts
  (keV), and a dose of from about 1e12 cm⁻² to about 1e14 cm⁻² to form
  an N-type MOS (NMOS) transistor" channel, and an indium-doped channel
  "implanted with Indium (In) at an energy of from about 50 to about 500
  kilo-electron volts (keV), and a dose of from about 5e11 … to about
  5e12 cm⁻²" for the memory transistor;[^pat-04] a 2020 Cypress article
  describes "use of deeper channel implants with heavier species such as
  Indium" for the SONOS cell.[^cyp-25] For an implant that *lowers* the
  threshold by counter-doping, the species is n-type — arsenic or
  phosphorus — at similar doses.[^pat-vt-rrr]
* **Energy and dose.** Tens of keV and 10¹²–10¹³ cm⁻²: an LSI Logic
  patent has the threshold-adjust boron "implanted through the
  sacrificial gate oxide in doses between 1×10¹² and 1×10¹³ atoms/cm² …
  at implant energies between 50 and 100 keV";[^pat-vt-lsi] an AMD
  patent gives "approximately 10-20 KeV for boron or 45-90 KeV for BF₂
  at a concentration of about 1.0 to 2.5×10¹³ ions/cm²" for a channel
  implant.[^pat-vt-amd]
* **Tilt and twist.** A few degrees of tilt with twist to suppress
  {term}`channelling` — "most implantation is carried out a few degrees
  off-axis";[^wiki-implant] the PDK's assumptions table records 7° as
  the angle for tip implants,[^pdk-03] which is also the textbook
  convention for channel implants.[^txt-02]
* **Screen oxide.** The 10–20 nm pad oxide[^pat-04] randomises the beam
  and keeps sputtered resist off the silicon.
* **Charge control and wafer cooling.** Electron shower and cooled
  electrostatic chuck — both features SkyWater lists for its
  medium-current tool ("ESC chuck, E shower").[^skw-01]
* **Anneal.** None here; activation waits for {ref}`RTAI <step-034>`,
  after all well implants.
* **Monitoring.** Modulated-reflectance (Therma-Wave) on product or
  monitor wafers, since the dose is too low for {term}`sheet resistance` to be a
  sensitive check (category page).

## Machines typically used

* **Medium-current implanter**, 200 mm, serial end station with
  tilt/twist: Axcelis (Eaton) NV-8250/8250HT, Varian E220/E500,
  Nissin[^txt-09] (category page). The Eaton 8250HT is described as
  covering "3keV to 750keV" with beam currents "between 4µA and
  3,500µA".[^axcelis-8250]
* **Therma-Wave** modulated-reflectance monitor; {term}`four-point probe` on
  monitor wafers after a monitor anneal.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current implanter.** SkyWater's facilities page
  lists "Axcelis 8250 Mid current B11, BF2, As, ESC chuck, E shower,
  1e11 to 1e14, 0-60 deg tilt".[^skw-01] The species (B, BF₂, As), the
  dose window (10¹¹–10¹⁴ cm⁻²) and the tilt capability are exactly those
  of a threshold-adjust implant. Strength: **strong** for the tool;
  assignment to `LVTNI` is an **inference** from capability.
* **Axcelis GSD**[^skw-01] could equally run a keV boron implant, but a
  batch high-current/high-energy tool is normally reserved for wells and
  source/drains. Strength: strong for existence, weak for assignment.
* A SkyWater maintenance profile mentions implanter robotics and vacuum
  work[^skw-07] — corroboration that implanters are maintained in house,
  not tool evidence.

## Resources required

* **Boron trifluoride (BF₃)** as the source gas for B⁺ and
  BF₂⁺[^wiki-implant] (category page); **arsine (AsH₃)** or **phosphine
  (PH₃)** if the implant is n-type; **solid indium** in a vaporiser oven
  if indium is used (category page).
* **Source support gases** (argon, xenon, hydrogen); **liquid nitrogen /
  cryopump** consumables; high-purity nitrogen vent gas.
* **Ion-source consumables** (filaments or cathodes, arc-chamber liners,
  extraction electrodes).
* **Wafer-cooling** water and backside gas; **monitor wafers**.
* SkyWater's filings name Air Products, Praxair, Linde and Airgas among
  its gas suppliers without tying them to a step.[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`LVTNM <step-014>` (the mask); next:
  {ref}`LVTNIS <step-016>` (strip).
* Threshold-setting companions: {ref}`LVTPI <step-020>` (PMOS, under
  the N-well mask), {ref}`PCHI <step-023>`/{ref}`PNCHI <step-024>`
  (high-Vt PMOS) and {ref}`NCHI <step-045>` (N-channel, under the
  low-voltage oxide mask).
* Activated at {ref}`RTAI <step-034>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — Axcelis 8250 "Mid current B11,
  BF2, As, ESC chuck, E shower, 1e11 to 1e14, 0-60 deg tilt".[^skw-01]
* SkyWater, *A Day in the Life of a SkyWater Maintenance Technician* —
  implanters are maintained in house.[^skw-07]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]
* SkyWater PDK, *Periphery rules* — `lvtn` function text.[^pdk-periph]
* SkyWater PDK, *Device Details* — `nfet_01v8`, `nfet_01v8_lvt`; native
  devices "blocking out all VT implants".[^pdk-07]
* SkyWater PDK, *Criteria & Assumptions* — implant angles
  table.[^pdk-03]
* Ramkumar et al. (Cypress), US 8,796,098 — pad oxide 10–20 nm; BF₂
  10–100 keV, 1e12–1e14 cm⁻²; indium 50–500 keV.[^pat-04]
* Semiconductor Online, *8250HT Medium Current Ion Implanter* — Eaton
  Semiconductor Equipment Operations product description; 3–750 keV,
  4–3500 µA.[^axcelis-8250]

### High-level understanding

* Wikipedia, *Ion implantation* — energies, sources, channelling and
  tilt in one page.[^wiki-implant]
* Wikipedia, *Threshold voltage* — body-effect parameter containing
  N_A.[^wiki-vt]
* Wikipedia, *Multi-threshold CMOS* — why several thresholds are offered
  and how they are set.[^wiki-mtcmos]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — ch. 8 ("Ion
  Implantation").[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography, resist stripping, wafer cleaning and implantation
  chapters.[^txt-02]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — implanter classes.[^txt-09]
* Ramkumar, Prabhakar and Kapre (Cypress), *Scalable SONOS based
  embedded non-volatile memory technology* — indium channel
  engineering.[^cyp-25]

### Deep dive

* Helm and Zhou (Round Rock Research), US 2011/0006372 — arsenic and
  BF₂/indium {term}`Vt` adjusts; counter-doped low-Vt channel.[^pat-vt-rrr]
* Aronowitz, Khan and Kimball (LSI Logic), US 5,963,801 — Vt-adjust
  boron 1e12–1e13 cm⁻² at 50–100 keV.[^pat-vt-lsi]
* Krivokapic and Milic (AMD), US 6,238,982 — channel implant
  energies/doses.[^pat-vt-amd]
* Shahidi et al. (IBM), *IEEE EDL* 1993 — indium channel implants for
  steep retrograde NMOS channels.[^shahidi-1993]
* Huang et al., *IEEE TED* 2000 — an 80 nm DTMOS with an indium
  super-steep retrograde channel.[^huang-2000]
* MacPherson, *Appl. Phys. Lett.* 1971 — the original demonstration of
  setting a MOS threshold by ion implantation.[^macpherson-1971]
* Peressini and Johnson, IEDM 1973 — early NMOS threshold adjustment by
  implantation with dose-versus-threshold data.[^peressini-1973]
* Taur et al., *Proc. IEEE* 1997 — super-steep retrograde channels and
  multiple thresholds at the 0.1 µm node.[^taur-1997]
* Rafferty et al. (AT&T), IEDM 1993 — how implant damage and the anneal
  reshape the channel profile (the reverse short-channel
  effect).[^rafferty-1993]
* Smith, Rosencwaig and Willenborg, *Appl. Phys. Lett.* 1985 — the
  thermal-wave monitor that checks light channel implants where sheet
  resistance cannot.[^smith-1985]
* Current, *J. Vac. Sci. Technol. A* 1996 — what a production
  medium-current implanter looks like inside.[^current-1996]

## Open questions

* The species, energy, dose and tilt of `LVTNI` are not public; so is
  its polarity (p-type baseline implant that low-Vt devices skip, or
  n-type counter-dope into low-Vt devices).
* Why this channel implant precedes the well implants — rather than
  following them as in most published flows — is not documented; a
  plausible reason is simply that it shares the full
  {ref}`RTAI <step-034>` anneal with the wells either way.
* Whether the pad oxide from {ref}`BOX <step-002>` is still present
  as the screen oxide (see the open question on
  {ref}`NS19 <step-013>`) is inferred, not stated.

<!-- footnotes -->

[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
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
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
