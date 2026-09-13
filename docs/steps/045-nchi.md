(step-045)=
# Step 045 — NCHI: N-channel implant

| | |
|---|---|
| **Step number** | 45 of 171[^steps-sheet] |
| **Step code** | `NCHI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — SONOS and gate dielectrics |
| **Previous step** | {ref}`LVOM <step-044>` |
| **Next step** | {ref}`GOXETCH <step-046>` |

## What this step is

`NCHI` is a channel implant made through the windows that
{ref}`LVOM <step-044>` opened over the low-voltage (1.8 V) regions,
before the thick oxide is stripped from them at
{ref}`GOXETCH <step-046>`. This reference describes it as the baseline
threshold-setting implant of the 1.8 V NMOS (inference from its
place in the sequence this reference describes — under the low-voltage
oxide mask, after the well and
channel module was annealed at {ref}`RTAI <step-034>` — and from the
PDK's device description below): the p-type
dose in the top of the channel that gives `nfet_01v8` its threshold.
The earlier pages of this reference treat it that way: the low-Vt
device `nfet_01v8_lvt` is made by the separate {ref}`LVTNI <step-015>`
implant, and the PDK says its cross-section "is identical to the std
NMOS FET except for the VT adjust implants".[^pdk-07]

The implant passes through the thick gate oxide grown at
{ref}`GOX100 <step-043>` — roughly 10 nm of fresh thermal oxide (the
PDK's 110 Å final value[^pdk-hv] less the later increment) — and through
the resist windows; the 5 V and high-voltage regions are covered. That
the oxide it goes through is about to be etched away is not incidental:
Cypress notes that implanted oxide is degraded and loses more in every
strip,[^pat-03] and an implant placed *before* the oxide strip leaves
the damaged oxide to be discarded rather than kept as a gate dielectric.

No public source gives the species, energy or dose. The Cypress
embedded-SONOS patent describes the equivalent implant in its flow:
"BF₂ can be implanted at an energy of from about 10 to about 100
kilo-electron volts (keV), and a dose of from about 1e12 cm⁻² to about
1e14 cm⁻² to form an N-type MOS (NMOS) transistor".[^pat-04]

## Step category

`NCHI` is an {ref}`Ion implantation <category-implant>` step of the
*{term}`threshold-adjust <threshold-adjust implant>` channel implant* class — low energy, medium current,
of order 10¹²–10¹³ cm⁻² (industry-typical)[^txt-01] — and the last
channel implant of the flow before the gate is deposited at
{ref}`SAGD <step-048>`. It is the N-channel counterpart of
{ref}`LVTPI <step-020>`, which the 1.8 V PMOS received through the
N-well window.

## Why this step exists

A MOSFET's threshold rises with the doping of the channel region
(through the body-effect term in Wikipedia's expression[^wiki-vt]);
multi-threshold CMOS is built "by altering the concentration of dopant
atoms in the channel region beneath the gate oxide".[^wiki-mtcmos]
The P-well of {ref}`PWI <step-027>` sets a background; the retrograde
profile keeps the surface lightly doped on purpose
({ref}`NWI <step-018>`); a dedicated surface implant is what puts the
1.8 V NMOS threshold where the PDK's models say it is. MacPherson
showed in 1971 that ion implantation is the way to adjust MOS
thresholds precisely,[^macpherson-1971] and Peressini and Johnson
applied it to n-channel enhancement devices.[^peressini-1973]

Placing the implant here rather than in the well module has two
consequences worth stating:

* **{term}`Thermal budget <thermal budget>`.** The implant sees only the {ref}`LVGOX <step-047>`
  oxidation and the later RTAs before the gate goes on, so the surface
  profile stays shallow — the same logic Cypress applies to its memory
  channel, keeping "surface dopant concentrations low" by limiting
  thermal budget after the critical steps.[^cyp-25] The
  short-channel behaviour of a 130 nm-era NMOS depends on a steep,
  shallow surface profile.[^taur-1997][^taur-2009]
* **Mask economy.** The low-voltage oxide window already outlines the
  1.8 V regions, so the implant needs no mask of its own — the same
  economy as {ref}`LVTPI <step-020>` under the N-well mask.

The window also exposes the 1.8 V *PMOS* regions. Whether the
generated `clvom` mask excludes N-wells, or whether the PMOS channels
simply tolerate the dose, is not public (see *Open questions*).
Without `NCHI` the 1.8 V NMOS would have the threshold of the bare
P-well surface — close to the native devices, whose {term}`Vt` implants are
deliberately blocked.[^pdk-07]

## How it is typically performed

An industry-generic NMOS threshold implant for a 200 mm, 130 nm-era
fab (SKY130's values are not public):

* **Species.** Boron, as ¹¹B⁺ or BF₂⁺; BF₂⁺ gives a shallower profile
  for the same accelerator voltage because the molecule shares its
  energy, and the fluorine it carries affects boron diffusion during
  the later {term}`RTA`.[^wang-1997] Cypress's flow uses BF₂;[^pat-04] an AMD
  patent of the era gives "approximately 10-20 KeV for boron or
  45-90 KeV for BF₂ at a concentration of about 1.0 to 2.5×10¹³
  ions/cm²".[^pat-vt-amd]
* **Energy.** Tens of keV for BF₂ (10–100 keV in the Cypress
  patent[^pat-04]), set so that the peak lies just under the eventual
  gate oxide after allowing for the ~10 nm {term}`screen oxide`[^pdk-hv] the
  ions must cross — the screen also randomises the beam and reduces
  {term}`channelling`.[^txt-02]
* **Dose.** Of order 10¹²–10¹³ cm⁻²: "1e12 cm⁻² to about 1e14
  cm⁻²"[^pat-04] and 1.0–2.5 × 10¹³ cm⁻²[^pat-vt-amd] in the patents.
* **Tilt and twist.** 7° with twist, the textbook
  convention.[^txt-02][^wiki-implant]
* **Wafer handling.** Single-wafer end station, electrostatic chuck,
  electron-shower neutralisation; the resist carries a light dose.
* **Anneal.** No dedicated anneal — the {ref}`LVGOX <step-047>`
  oxidation and the source/drain RTAs ({ref}`RTAD <step-088>`) activate
  it; {term}`TED` during those steps is part of the profile design
  ({ref}`category-implant`).
* **Monitoring.** Thermal-wave measurement on product;[^smith-1985]
  the {term}`e-test` threshold of `nfet_01v8` is the ultimate monitor.

## Machines typically used

* **Medium-current ion implanter**, 200 mm, single-wafer: Axcelis
  (Eaton) 8250 class ("3keV to 750keV"[^axcelis-8250]), Varian
  E220/E500, Applied Materials xR ({ref}`category-implant`).
* **Thermal-wave** and **four-point-probe** metrology.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current implanter** — "B11, BF2, As, ESC
  chuck, E shower, 1e11 to 1e14, 0-60 deg tilt".[^skw-01] Boron and
  BF₂ at 10¹¹–10¹⁴ cm⁻² is exactly this implant's envelope. Strength:
  **strong** for the tool; **inference** for its assignment to
  `NCHI`.
* **Axcelis GSD implanters** — both GSD entries, "High current/energy"
  and "Hi dose", list "B11, BF2, P, As"[^skw-01] — as the alternative;
  which entry would serve is not stated. Strength: strong for existence;
  weak for assignment.

## Resources required

* **Boron trifluoride (BF₃)** source gas for B⁺ or BF₂⁺
  ({ref}`category-implant`).
* **Source consumables**, **helium** platen cooling, **nitrogen**,
  cryopump regeneration.
* **Monitor wafers**.
* Gas suppliers named in SkyWater's filings: Air Products and Praxair
  (2021 S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`LVOM <step-044>` (the window); next:
  {ref}`GOXETCH <step-046>` (the screen oxide is stripped),
  {ref}`LVGOX <step-047>`.
* Companion channel implants: {ref}`LVTNI <step-015>` (low-Vt NMOS),
  {ref}`LVTPI <step-020>` (1.8 V PMOS), {ref}`PCHI <step-023>` /
  {ref}`PNCHI <step-024>` (high-Vt PMOS), {ref}`PTSI <step-037>` /
  {ref}`DEPI <step-038>` ({term}`SONOS`).
* Wells: {ref}`PWI <step-027>`; anneal of the well module:
  {ref}`RTAI <step-034>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* SkyWater PDK, *Device Details* — `nfet_01v8` versus
  `nfet_01v8_lvt` ("identical … except for the VT adjust implants");
  native devices with Vt implants blocked.[^pdk-07]
* SkyWater, *Facilities & Capabilities* — Axcelis 8250 and GSD species
  and dose ranges.[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — BF₂
  NMOS channel implant energies and doses.[^pat-04]
* Koutny et al. (Cypress), US 8,093,128 — oxide degradation by
  implantation and strips.[^pat-03]
* Semiconductor Online, *8250HT Medium Current Ion Implanter*.[^axcelis-8250]

### High-level understanding

* Wikipedia, *Threshold voltage* and *Multi-threshold CMOS* — how
  channel doping sets Vt.[^wiki-vt][^wiki-mtcmos]
* Wikipedia, *Ion implantation*.[^wiki-implant]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  implantation.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — the submicron
  MOSFET and its channel engineering.[^txt-04]

### Deep dive

* MacPherson, *Appl. Phys. Lett.* 1971 — threshold adjustment by ion
  implantation.[^macpherson-1971]
* Peressini and Johnson, IEDM 1973 — threshold adjustment of n-channel
  enhancement FETs.[^peressini-1973]
* Krivokapic and Milic (AMD), US 6,238,982 — channel-implant energies
  and doses of the era.[^pat-vt-amd]
* Aronowitz, Khan and Kimball (LSI Logic), US 5,963,801 —
  threshold-adjust boron through a sacrificial oxide.[^pat-vt-lsi]
* Wang et al., *J. Electrochem. Soc.* 1997 — fluorine's effect on
  boron diffusion after BF₂ implantation through oxide and RTA.[^wang-1997]
* Taur et al., *Proc. IEEE* 1997 — channel profile requirements as
  gates scale.[^taur-1997]
* Taur and Ning, *Fundamentals of Modern VLSI Devices* — threshold
  versus channel doping and the body effect.[^taur-2009]
* Wei et al., DAC 1998 — the circuit case for multiple
  thresholds.[^wei-1998]
* Hook et al., *IEEE TED* 2003 — threshold shifts near implant-mask
  edges.[^hook-2003]
* Smith, Rosencwaig and Willenborg, *Appl. Phys. Lett.* 1985 — the
  thermal-wave implant monitor.[^smith-1985]

## Open questions

* That `NCHI` is the baseline 1.8 V NMOS threshold implant is an
  inference from its place in the sequence this reference describes
  and from the PDK's VT-adjust
  description;[^pdk-07] no public source describes it directly.
* Species (B or BF₂), energy, dose and tilt are not public.
* Whether the low-voltage oxide window through which it is implanted
  excludes the 1.8 V PMOS regions, or whether those regions receive
  the dose, is not public.
* The label "N-channel implant" used in this reference does not say
  which N-channel implant this is; the reading on this page is an
  inference from its place in the sequence this reference describes.

<!-- footnotes -->

[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
[^wiki-mtcmos]: Wikipedia, *Multi-threshold CMOS*.
    <https://en.wikipedia.org/wiki/Multi-threshold_CMOS>
[^wiki-vt]: Wikipedia, *Threshold voltage*.
    <https://en.wikipedia.org/wiki/Threshold_voltage>
[^macpherson-1971]: M. R. MacPherson, "The adjustment of MOS transistor
    threshold voltage by ion implantation", *Applied Physics Letters*
    **18**(11), 502–504 (1971). <https://doi.org/10.1063/1.1653513>
[^peressini-1973]: P. P. Peressini and W. S. Johnson, "Threshold
    adjustment of N-channel enhancement mode FETs by ion implantation",
    *1973 International Electron Devices Meeting*, pp. 467–468.
    <https://doi.org/10.1109/IEDM.1973.188761>
[^cyp-25]: K. Ramkumar, V. Prabhakar and R. Kapre (Cypress
    Semiconductor), *Scalable SONOS based embedded non-volatile memory
    technology*, Semiconductor Digest, 2020-02.
    <https://sst.semiconductor-digest.com/2020/02/scalable-sonos-based-embedded-non-volatile-memory-technology/>
[^taur-1997]: Y. Taur, D. A. Buchanan, W. Chen, D. J. Frank, K. E.
    Ismail, S.-H. Lo, G. A. Sai-Halasz, R. G. Viswanathan, H.-J. C.
    Wann, S. J. Wind and H.-S. Wong, "CMOS scaling into the nanometer
    regime", *Proceedings of the IEEE* **85**(4), 486–504 (1997).
    <https://doi.org/10.1109/5.573737>
[^taur-2009]: Y. Taur and T. H. Ning, *Fundamentals of Modern VLSI
    Devices*, 2nd ed., Cambridge University Press, 2009, ISBN
    978-0-521-83294-6. <https://doi.org/10.1017/CBO9781139195065>
[^wang-1997]: L. Z. Wang, M. S.-C. Luo, H.-H. Tseng and S. A. Ajuria,
    "The Influence of Fluorine on Boron-Enhanced Diffusion in Silicon
    by BF₂⁺ Implantation Through Oxide during High Temperature Rapid
    Thermal Anneal", *Journal of The Electrochemical Society*
    **144**(11), L298–L301 (1997). <https://doi.org/10.1149/1.1838075>
[^pat-vt-amd]: Z. Krivokapic and O. Milic (AMD), *Multiple threshold
    voltage semiconductor device fabrication technology*, US 6,238,982
    B1, granted 2001-05-29.
    <https://patents.google.com/patent/US6238982B1/en>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^smith-1985]: W. L. Smith, A. Rosencwaig and D. L. Willenborg, "Ion
    implant monitoring with thermal wave technology", *Applied Physics
    Letters* **47**(6), 584–586 (1985).
    <https://doi.org/10.1063/1.96079>
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
[^pat-vt-lsi]: S. Aronowitz, L. Khan and J. Kimball (LSI Logic), *Method
    of forming retrograde well structures and punch-through barriers
    using low energy implants*, US 5,963,801 A, granted 1999-10-05.
    <https://patents.google.com/patent/US5963801A/en>
[^wei-1998]: L. Wei, Z. Chen, M. Johnson, K. Roy and V. De, "Design and
    optimization of low voltage high performance dual threshold CMOS
    circuits", *Proceedings of the 35th Design Automation Conference*,
    pp. 489–494 (1998). <https://doi.org/10.1109/DAC.1998.724521>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
