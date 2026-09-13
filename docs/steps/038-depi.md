(step-038)=
# Step 038 — DEPI: Depletion implant

| | |
|---|---|
| **Step number** | 38 of 171[^steps-sheet] |
| **Step code** | `DEPI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — SONOS and gate dielectrics |
| **Previous step** | {ref}`PTSI <step-037>` |
| **Next step** | {ref}`TUNME <step-039>` |

## What this step is

`DEPI` is the second implant through the tunnel-mask windows. Where
{ref}`PTSI <step-037>` put a p-type barrier *under* the memory
transistor's channel, `DEPI` dopes the channel *surface* so that the
{term}`SONOS` transistor is a {term}`depletion-mode` device: one that conducts with zero
volts on its gate and needs a negative gate voltage to turn off. The
PDK's own cross-section of the {term}`2-T <2-T cell>` SONOS cell uses the same term: its
labels include "Depletion Implant" alongside "ONO", "SONOS gate", "NPASS
gate" and "NMOS VT implants".[^pdk-sonos-xs] The implant is confined to
the `tunm` windows (GDS 80:20, "SONOS device tunnel implant"[^pdk-06])
by the resist from {ref}`TUNM <step-035>`, opened at
{ref}`TUNARCE <step-036>`, and passes through the (inferred) pad oxide
like `PTSI`.

For an n-channel transistor a depletion implant is an n-type dose
(arsenic or phosphorus) placed in the top few tens of nanometres of
the channel, enough to over-compensate the p-well and leave a thin
n-type layer that conducts until the gate depletes it — the "buried
channel" of the classic ion-implanted depletion-mode
IGFET.[^edwards-1971] We infer arsenic on the grounds that it gives
the shallowest, best-controlled profile and is among the species
SkyWater lists;[^skw-01] no public source names the species, energy or
dose.

## Step category

`DEPI` is an {ref}`Ion implantation <category-implant>` step of the
*threshold-setting channel implant* class, like {ref}`LVTNI <step-015>`
and {ref}`PCHI <step-023>`: a low-energy, medium-current implant of
order 10¹²–10¹³ cm⁻² (industry-typical).[^txt-01] It differs from every
other channel implant in the flow in sign of purpose — it drives the
threshold *negative* rather than trimming a positive one — and in being
confined to the memory cells.

## Why this step exists

The reason is the way the 2-T cell is read. The PDK's programme/erase
table shows the read condition as 0 V on the {term}`control gate`, +1.1 V on
the drain and +1.8 V on the word line (the {term}`select gate`), and the
threshold measurement likewise at 2.05 µA with the gate at
0 V.[^pdk-07] The memory transistor therefore has to conduct with its
gate *grounded* when erased and be cut off with its gate grounded when
programmed. The {term}`e-test` table gives exactly that: a nominal "SONOS
erased VT" of −2.3 V (specification −3.648 to −0.952 V), a "SONOS
programmed VT" of 1.44 V, and a "program inhibit VT" of
−1.132 V.[^pdk-07] A transistor whose erased threshold is −2.3 V is a
depletion-mode device — "For an N-type FET, enhancement-mode devices
have positive thresholds, and depletion-mode devices have negative
thresholds", and such a device "is normally on at zero gate–source
voltage".[^wiki-depletion]

Trapped charge alone does not put the whole window there. Erasing
removes electrons (or adds holes) to the nitride and shifts the
threshold negative; programming adds electrons and shifts it
positive.[^cyp-25][^cyp-26] The *neutral* threshold — with no net
charge in the nitride — sits between the two, and it is set by the
channel doping under the {term}`ONO`. A depletion implant places that
neutral point near or below zero so that a symmetric ±ΔV window from
{term}`Fowler–Nordheim <Fowler–Nordheim tunnelling>` programming and erase[^cyp-25] straddles the 0 V read
condition with margin on both sides. Scaled-SONOS design papers treat
the channel doping and the neutral threshold as design variables of the
memory window alongside the ONO thicknesses.[^bu-2001][^french-1994]

The price of a depletion-mode memory transistor is that it cannot
isolate itself: an erased, unselected cell would conduct. That is what
the second transistor of the 2-T cell is for — the "NPASS gate" driven
by the word line[^pdk-sonos-xs] — and why the PDK's cell is "a SONOS
Control Gate (CG) in series with a CMOS Select Gate".[^cyp-25] A
failure-analysis paper on "parasitic depletion mode leakage in a memory
select transistor" shows what happens when depletion-mode behaviour
leaks into the select device.[^colvin-2000]

**Relation to the native devices.** SKY130 also offers native NMOS
transistors (`nfet_03v3_nvt`, `nfet_05v0_nvt`) and a 20 V zero-Vt
device. It is tempting to connect them to a "depletion implant", but
the PDK says the opposite: "The native device is constructed by
blocking out all VT implants", and the zero-Vt device "has p-well and
all Vt implants blocked to achieve a zero VT".[^pdk-07] Those devices
are made by *omitting* implants (through the `lvtn` block layer, whose
function is to "block Vt adjust implant for low Vt LV PMOS/NMOS, SONOS
FETs and Native NMOS"[^pdk-periph]), not by adding one. We therefore
infer that `DEPI` is specific to the SONOS cells and plays no part in
the native or zero-Vt transistors; their thresholds are those of
channels without threshold-adjust implants.

Measurements published in the SKY130 raw-data repository are consistent
with that reading. By maximum-transconductance extrapolation of the
drain current at a drain bias of 0.1 V (our extraction from the
published measurements), the `nfet_05v0_nvt` structures have thresholds
of 0.05–0.12 V and the `nfet_03v3_nvt` structures −0.05 to +0.05 V,
against 0.79–0.82 V for two 7/8 µm `nfet_g5v0d10v5` devices; the 20 V
zero-Vt structure on the {term}`test tile` (pad-list name `n20zvtvhv1`;
see {ref}`PWBM <step-026>`) gives −0.12 to
−0.13 V.[^raw-data-hv-mosfets][^raw-data-testtile-pads] None of these
thresholds is strongly negative. The shift of threshold with body bias
tells the devices apart: the body-effect coefficient is about 0.47 √V
for a 10/4 µm `nfet_05v0_nvt`, 0.73 √V for the 7/8 µm `nfet_g5v0d10v5`
and 0.07 √V for the zero-Vt structure (our extraction, body biases of
0, −2.5 and −5 V). With the standard uniform-doping expression and the
thick-oxide capacitance measured on the same tile (see
{ref}`GOX100 <step-043>`), these correspond to effective body dopings
of about 6 × 10¹⁶, 1.5 × 10¹⁷ and 1.4 × 10¹⁵ cm⁻³.[^raw-data-hv-mosfets]
We read this as a native device that keeps a well-doped body under its
channel, and a zero-Vt device whose body is some forty times more
lightly doped, as the PDK's "p-well and all Vt implants blocked"
implies.[^pdk-07] The effective values are averages over the depleted
depth, not doping profiles, and the data say nothing about the implants
themselves.

## How it is typically performed

An industry-generic depletion-mode channel implant for a 200 mm,
130 nm-era memory transistor (SKY130's values are not public):

* **Species.** Arsenic (⁷⁵As⁺, from AsH₃) for a shallow, abrupt
  n-layer; phosphorus is the lighter alternative with a longer tail.
  The original ion-implanted depletion-mode IGFET work established the
  implanted n-layer approach,[^edwards-1971] and Merckel's modelling
  chapter treats the resulting device physics.[^merckel-1977] A
  Round Rock Research patent on multi-threshold devices likewise uses
  "an implant of Arsenic" as a first channel adjustment and a
  "counter-doped channel region".[^pat-vt-rrr]
* **Energy.** Low — tens of keV for arsenic — so that the n-layer is
  confined to the top few tens of nanometres above the `PTSI` barrier;
  the {term}`tunnel oxide` grown at {ref}`ONO <step-040>` consumes about 1 nm
  for a 2 nm oxide of the kind the Cypress patents describe[^pat-04]
  (46 % of the oxide thickness lies below the original
  surface[^wiki-thox]), which the target must allow for.
* **Dose.** Of order 10¹² cm⁻²: enough to swing the threshold by a
  volt or two against the p-well surface doping, in line with
  {term}`threshold-adjust <threshold-adjust implant>` practice[^macpherson-1971] and with the 10¹²–10¹³
  cm⁻² channel-implant range of the era's patents.[^pat-vt-amd]
* **Tilt and twist.** 7° with twist,[^txt-02][^wiki-implant] through
  the (inferred) pad oxide, which randomises the beam and reduces
  {term}`channelling`.
* **Order.** After `PTSI` through the same resist; the order of the
  two implants does not matter physically and is presumably chosen for
  implanter scheduling.
* **Anneal.** By the furnace steps that follow, beginning with the
  tunnel oxidation at {ref}`ONO <step-040>`; arsenic's slow diffusion
  keeps the layer shallow through the ONO and gate-oxide thermal
  budget, which Cypress notes must be kept low after the stack is
  formed.[^cyp-25]
* **Monitoring.** Thermal-wave measurement on product; the cell
  threshold itself is monitored at e-test (the `VTE`/`VTP` parameters
  above[^pdk-07]).

## Machines typically used

* **Medium-current ion implanter**, 200 mm, single-wafer: Axcelis
  (Eaton) 8250 class ("3keV to 750keV"[^axcelis-8250]), Varian
  E220/E500, Applied Materials xR ({ref}`category-implant`).
* **Thermal-wave** metrology.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current implanter** — "B11, BF2, As, ESC
  chuck, E shower, 1e11 to 1e14, 0-60 deg tilt".[^skw-01] Arsenic and
  the dose range match a depletion implant. Strength: **strong** for
  the tool; **inference** for its assignment to `DEPI`.
* **Axcelis GSD implanters** — both GSD entries, "High current/energy"
  and "Hi dose", list "B11, BF2, P, As"[^skw-01] — if phosphorus were
  the species; which entry would serve is not stated. Strength: strong
  for existence; weak for assignment.

## Resources required

* **Arsine (AsH₃)** (or phosphine for phosphorus), delivered in
  sub-atmospheric cylinders with gas-cabinet monitoring
  ({ref}`category-implant`).
* **Source consumables**, **helium** platen cooling, **nitrogen**,
  cryopump regeneration.
* **Monitor wafers**.
* Gas suppliers named in SkyWater's filings: Air Products and Praxair
  (2021 S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`PTSI <step-037>` (sub-surface barrier through the
  same window); mask: {ref}`TUNM <step-035>`.
* Next: {ref}`TUNME <step-039>` removes the (inferred) pad oxide the
  implant went through; {ref}`ONO <step-040>` grows the tunnel oxide on the
  implanted silicon.
* The select transistor of the cell is a standard NMOS whose channel we
  take to have been implanted at {ref}`LVTNI <step-015>` or later; the
  cell's tip implant is {ref}`LDNTM <step-071>`.
* Native devices: see {ref}`LVTNM <step-014>` for the `lvtn` block
  layer.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* SkyWater PDK, `cross-section-sonos-cell.svg` — the labelled
  "Depletion Implant" in the 2-T cell drawing.[^pdk-sonos-xs]
* SkyWater PDK, *Device Details* — read/programme/erase conditions,
  erased and programmed thresholds, native and zero-Vt device
  descriptions.[^pdk-07]
* SkyWater PDK, *Periphery rules* — the `lvtn` block-layer
  function.[^pdk-periph]
* SKY130 raw-data repository — I–V sweeps of the native, zero-Vt and
  5 V NMOS test-tile structures (thresholds and body-effect coefficients
  quoted here are our extraction) and the pad list naming
  them.[^raw-data-hv-mosfets][^raw-data-testtile-pads]
* SkyWater PDK, *Layers Reference* — `tunm` 80:20.[^pdk-06]
* SkyWater, *Facilities & Capabilities* — Axcelis 8250 and GSD species
  and dose ranges.[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]
* Ramkumar, Prabhakar and Kapre (Cypress), Semiconductor Digest — the
  2-T cell and Fowler–Nordheim programming.[^cyp-25]
* Semiconductor Online, *8250HT Medium Current Ion Implanter*.[^axcelis-8250]

### High-level understanding

* Wikipedia, *Depletion and enhancement modes* — the sign of the
  threshold in each mode.[^wiki-depletion]
* Wikipedia, *SONOS* — how trapped charge shifts the
  threshold.[^cyp-26]
* Wikipedia, *Thermal oxidation* — silicon consumed by the tunnel
  oxide.[^wiki-thox]
* Wikipedia, *Ion implantation*.[^wiki-implant]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  implantation.[^txt-02]

### Deep dive

* Edwards and Marr, IEDM 1971 — the ion-implanted depletion-mode
  IGFET.[^edwards-1971]
* Merckel, in *Process and Device Modeling for Integrated Circuit
  Design* (1977) — modelling of ion-implanted depletion-mode
  transistors.[^merckel-1977]
* MacPherson, *Appl. Phys. Lett.* 1971 — threshold adjustment by ion
  implantation, the technique in its original form.[^macpherson-1971]
* Helm and Zhou (Round Rock Research), US 2011/0006372 — arsenic
  channel adjustment and {term}`counter-doped <counter-doping>` channels in a multi-Vt
  flow.[^pat-vt-rrr]
* Krivokapic and Milic (AMD), US 6,238,982 — channel-implant energies
  and doses of the era.[^pat-vt-amd]
* Bu and White, *Solid-State Electronics* 2001 — design considerations
  in scaled SONOS devices, including the memory window.[^bu-2001]
* French and White, *Solid-State Electronics* 1994 — scaling of
  multi-dielectric SONOS structures.[^french-1994]
* White, Adams and Bu, *IEEE Circuits & Devices* 2000 — the SONOS
  review.[^pap-01]
* Colvin and Roy, ISTFA 2000 — parasitic depletion-mode leakage in a
  memory select transistor, the failure the 2-T cell must
  avoid.[^colvin-2000]
* Jiew, Chien and Yung, NVMTS 2012 — a robust 2T-SONOS cell for
  embedded flash.[^jiew-2012]
* Maxim, ESSCIRC 2003 — a circuit built on zero-Vt MOSFETs, showing
  what designers do with near-zero-threshold devices.[^maxim-2003]

## Open questions

* The species, energy and dose of `DEPI` are not public; arsenic at
  tens of keV and ~10¹² cm⁻² is an era-typical inference.
* Whether the "Depletion Implant" label in the PDK drawing denotes a
  single implant or the combined effect of `PTSI` and `DEPI` is not
  stated; we read `DEPI` as the surface, n-type component.
* Whether `DEPI` contributes to any device other than the SONOS
  transistor is inferred (no) from the PDK's description of the native
  and zero-Vt devices as implant-blocked; their measured thresholds of
  about −0.13 to +0.12 V (our extraction) are consistent with that but
  do not exclude a small contribution.[^raw-data-hv-mosfets]
* The programme-inhibit threshold of −1.132 V[^pdk-07] implies a
  partial-erase state whose relation to the channel doping is not
  documented publicly.

<!-- footnotes -->

[^pdk-sonos-xs]: SkyWater PDK Authors, `cross-section-sonos-cell.svg`
    (2-T SONOS cell cross-section drawing), google/skywater-pdk
    repository, `docs/rules/device-details/special_sonosfet/`.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/special_sonosfet/cross-section-sonos-cell.svg>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^edwards-1971]: J. R. Edwards and G. Marr, "Ion-implanted
    depletion-mode IGFET", *1971 International Electron Devices
    Meeting*, p. 156. <https://doi.org/10.1109/IEDM.1971.188465>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^wiki-depletion]: Wikipedia, *Depletion and enhancement modes*.
    <https://en.wikipedia.org/wiki/Depletion_and_enhancement_modes>
[^cyp-25]: K. Ramkumar, V. Prabhakar and R. Kapre (Cypress
    Semiconductor), *Scalable SONOS based embedded non-volatile memory
    technology*, Semiconductor Digest, 2020-02.
    <https://sst.semiconductor-digest.com/2020/02/scalable-sonos-based-embedded-non-volatile-memory-technology/>
[^cyp-26]: Wikipedia, *SONOS*. <https://en.wikipedia.org/wiki/SONOS>
[^bu-2001]: J. Bu and M. H. White, "Design considerations in scaled
    SONOS nonvolatile memory devices", *Solid-State Electronics*
    **45**(1), 113–120 (2001).
    <https://doi.org/10.1016/S0038-1101(00)00232-X>
[^french-1994]: M. L. French and M. H. White, "Scaling of
    multidielectric nonvolatile SONOS memory structures", *Solid-State
    Electronics* **37**(12), 1913–1923 (1994).
    <https://doi.org/10.1016/0038-1101(94)90057-4>
[^colvin-2000]: J. B. Colvin and A. Roy, "Identification and Analysis
    of Parasitic Depletion Mode Leakage in a Memory Select Transistor",
    *ISTFA 2000: Proceedings of the 26th International Symposium for
    Testing and Failure Analysis*, pp. 247–249 (2000).
    <https://doi.org/10.31399/asm.cp.istfa2000p0247>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^merckel-1977]: G. Merckel, "Ion Implanted MOS Transistors — Depletion
    Mode Devices", in *Process and Device Modeling for Integrated
    Circuit Design*, Springer, 1977, pp. 677–688.
    <https://doi.org/10.1007/978-94-011-7583-8_24>
[^pat-vt-rrr]: M. Helm and X. Zhou (Round Rock Research), *Formation of
    standard voltage threshold and low voltage threshold MOSFET
    devices*, US 2011/0006372 A1, published 2011-01-13 (priority
    2002-07-08). <https://patents.google.com/patent/US20110006372A1/en>
[^wiki-thox]: Wikipedia, *Thermal oxidation*.
    <https://en.wikipedia.org/wiki/Thermal_oxidation>
[^macpherson-1971]: M. R. MacPherson, "The adjustment of MOS transistor
    threshold voltage by ion implantation", *Applied Physics Letters*
    **18**(11), 502–504 (1971). <https://doi.org/10.1063/1.1653513>
[^pat-vt-amd]: Z. Krivokapic and O. Milic (AMD), *Multiple threshold
    voltage semiconductor device fabrication technology*, US 6,238,982
    B1, granted 2001-05-29.
    <https://patents.google.com/patent/US6238982B1/en>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion
    Implanter* (Eaton Semiconductor Equipment Operations product
    description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^pap-01]: M. H. White, D. A. Adams and J. Bu, "On the go with SONOS",
    *IEEE Circuits and Devices Magazine* **16**(4), 22–31 (2000).
    <https://doi.org/10.1109/101.857747>
[^jiew-2012]: C. B. Jiew, Y. E. Chien and R. T. T. Yung, "Development
    of a robust 2T-SONOS cell for embedded flash application", *2012
    12th Annual Non-Volatile Memory Technology Symposium (NVMTS)*,
    pp. 1–6. <https://doi.org/10.1109/NVMTS.2013.6632849>
[^maxim-2003]: A. Maxim, "A low voltage, 10-2550MHz, 0.15μ CMOS,
    process and divider modulus independent PLL using zero-VT
    MOSFETs", *Proc. ESSCIRC 2003 — 29th European Solid-State Circuits
    Conference*, pp. 105–108. <https://doi.org/10.1109/ESSCIRC.2003.1257083>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^raw-data-hv-mosfets]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the 5 V, 10/16 V,
    20 V, native, zero-Vt and ESD transistors and the thick-oxide gate
    capacitors, IC-CAP `.mdm` files in `sky130_fd_pr/cells/`
    (`nfet_g5v0d10v5`, `pfet_g5v0d10v5`, `nfet_g5v0d16v0`,
    `pfet_g5v0d16v0`, `nfet_g5v0d20v0`, `pfet_g5v0d20v0`,
    `nfet_03v3_nvt`, `nfet_05v0_nvt`, `nfet_20v0_nvt`, `esd_nfet_01v8`,
    `esd_nfet_g5v0d10v5`), `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
