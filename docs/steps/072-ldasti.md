(step-072)=
# Step 072 — LDASTI: LD ASTI implant

| | |
|---|---|
| **Step number** | 72 of 171 |
| **Step code** | `LDASTI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — extensions, spacers, source/drain |
| **Previous step** | {ref}`LDNTM <step-071>` |
| **Next step** | {ref}`LDBHI <step-073>` |

## What this step is

`LDASTI` is the *lightly doped* arsenic tip implant of the {term}`SONOS`
memory transistors: the counterpart of {ref}`ASTI <step-065>` made
through the {ref}`LDNTM <step-071>` resist, at a dose that is, we
infer, lower than the standard tip's: the PDK calls the mask the
"Lightly-doped N-tip implant mask".[^pdk-06] Arsenic
ions enter the memory cell's active silicon on both sides of each
control-gate line, self-aligned to the polysilicon gate, and form the
shallow n⁻ regions that will connect the memory transistor's channel to
the deep n⁺ source/drain implanted later at {ref}`NSDI <step-086>`.
The boron {term}`halo` {ref}`LDBHI <step-073>` follows through the same resist;
the strip is {ref}`LDASTIS <step-074>`.

The PDK's "N Tip (As)" row gives arsenic;[^pdk-03] energy and dose are
not public. We read the PDK's "lightly-doped" mask description as an
LDD-class dose, of order
10¹³ cm⁻² (typical of an {term}`LDD`),[^txt-04] against the
10¹⁴–10¹⁵ cm⁻² of a logic {term}`extension` (typical).[^txt-01]

## Step category

`LDASTI` is an {ref}`Ion implantation <category-implant>` step of the
*LDD* class: low energy, moderate dose, small tilt — the PDK's 7°
"Angle for tip implant"[^pdk-03] applies, we infer, to this tip as to
the standard one. It is the module's smallest implant by area, since
only the memory array is open.

## Why this step exists

The reasons are set out on the {ref}`LDNTM <step-071>` page: the
SONOS memory transistor's junctions see several volts during programme,
erase and inhibit (the PDK's cell conditions apply +6.7 V and −3.8 V
across gate and source/drain/body),[^pdk-07] so a heavily doped abrupt
tip at the gate edge would leak by band-to-band tunnelling and inject
unwanted charge into the nitride, while a lightly doped, graded
junction keeps the peak field low — the original lightly doped drain
argument.[^ogura-1980] The trade-off is the one Thompson's group
quantified for logic: a lighter, deeper extension gives less
short-channel control and more series resistance.[^thompson-1998] For
a memory transistor read at low current, series resistance is
secondary; short-channel control is restored by the cell's own halo
({ref}`LDBHI <step-073>`) and {term}`punch-through stopper <punch-through>`
({ref}`PTSI <step-037>`).

Arsenic is kept, rather than the phosphorus of the classic LDD,
because its low diffusivity[^rev-05] preserves the graded profile
through the later anneals and keeps the 0.15–0.22 µm channel[^pdk-07]
from shortening; at LDD doses arsenic stays below the concentration
at which it precipitates and deactivates,[^nobili-1983] so its
activation is complete after a short anneal.

Without `LDASTI`, the memory transistors would have an undoped gap
between channel and n⁺ source/drain under the {term}`spacer`, or would have to
take the logic tip with its leakage and disturb penalties.

## How it is typically performed

An industry-generic lightly doped arsenic extension for a 200 mm,
130 nm-era fab (SKY130's values are not public):

* **Species and source.** ⁷⁵As⁺ from arsine or solid
  arsenic.[^wiki-implant][^wiki-ash3]
* **Energy.** A few keV to a few tens of keV (typical);[^txt-01] with a
  lighter dose, a slightly higher energy than the logic tip is often
  used so that the junction is deeper and more graded (LDD
  practice).[^txt-04]
* **Dose.** Of order 10¹³ cm⁻² (typical of an LDD);[^txt-04] below the
  arsenic amorphisation threshold of roughly 10¹⁴–10¹⁵
  cm⁻²,[^wiki-implant] so — unlike {ref}`ASTI <step-065>` — the
  silicon stays crystalline and the implant leaves point-defect damage
  rather than an amorphous layer. That changes what the halo boron
  sees ({ref}`LDBHI <step-073>`) and how much transient enhanced
  diffusion the anneal produces.[^stolk-1997]
* **Screen.** The implant passes through whatever dielectric remains
  over the memory transistor's source/drain after the gate etch — the
  {term}`screen oxide` of {ref}`IOX45 <step-063>` and, if it survived the gate
  etch, part of the {term}`ONO` stack patterned at {ref}`ONOME <step-042>`;
  which is the case is not public (see *Open questions*).
* **Tilt and rotation.** 7° (PDK tip angle),[^pdk-03] with twist; two
  or four rotations, or 0°, for symmetry — not public. In a dense
  array the neighbouring gate lines {term}`shadow <shadowing>` a tilted beam more than in
  logic, which favours a small tilt.[^chen-1995]
* **Charge control and cooling.** Electron shower and electrostatic
  chuck ("ESC chuck, E shower" on SkyWater's medium-current
  tool);[^skw-01] platen cooling is industry practice.
* **Anneal.** None here; activation at {ref}`TIPRTAD <step-075>`.
* **Monitoring.** Thermal-wave measurement on monitor
  wafers;[^smith-1985] at 10¹³ cm⁻² the {term}`sheet resistance` of a monitor
  is measurable but less sensitive.

## Machines typically used

* **Medium-current ion implanter**, 200 mm, single-wafer: Axcelis
  (Eaton) 8250 class, Varian E220/E500, Applied Materials xR
  ({ref}`category-implant`); the 8250HT covers "3keV to 750keV" with
  beam currents "between 4µA and 3,500µA".[^axcelis-8250]
* **High-current implanter** (Axcelis GSD, Varian VIISta 80) as the
  alternative if the dose is at the upper end.
* **Thermal-wave** and **four-point-probe** metrology.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current implanter.** SkyWater lists "Axcelis
  8250 Mid current B11, BF2, As, ESC chuck, E shower, 1e11 to 1e14,
  0-60 deg tilt".[^skw-01] An LDD-class arsenic dose sits inside its
  quoted window, and its 3 keV floor[^axcelis-8250] covers a shallow
  tip. Strength: **strong** for the tool; **medium** for the
  assignment, since a "lightly doped" tip is the one tip whose dose
  plausibly fits the medium-current tool.
* **Axcelis GSD high-current implanters** ("10-3000kev, 1e11 to 5e15,
  tilt/twist" and "2-180kev, 5e12 to 5e16, tilt/twist")[^skw-01] —
  possible; the Hi dose tool's 2 keV floor covers a shallow tip.
  Strength: strong for existence; weak for assignment.

## Resources required

* **Arsine (AsH₃)** or a **solid arsenic** source
  charge;[^wiki-implant][^wiki-ash3] gas-cabinet monitoring.
* **Source-support gases**, source consumables, high-purity
  **nitrogen** for venting.
* **Helium** for platen cooling; **liquid nitrogen** or cryopump
  regeneration.
* **Monitor wafers**.
* Gas suppliers named by SkyWater: Air Products, Praxair, Linde,
  Airgas.[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`LDNTM <step-071>` (the resist mask).
* Next: {ref}`LDBHI <step-073>` (the cell's halo through the same
  resist), then {ref}`LDASTIS <step-074>` (strip).
* The other tips: {ref}`ASTI <step-065>`, {ref}`HVASTI <step-069>`.
* The memory transistor's channel: {ref}`PTSI <step-037>`,
  {ref}`DEPI <step-038>`; its gate stack: {ref}`ONO <step-040>`,
  {ref}`SAGD <step-048>`, {ref}`P1ME <step-062>`.
* Activation: {ref}`TIPRTAD <step-075>`; deep n⁺ junction:
  {ref}`NSDI <step-086>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* SkyWater PDK, *Criteria & Assumptions* — "N Tip (As)", 7° tip
  angle.[^pdk-03]
* SkyWater PDK, *Layers Reference* — `ldntm` "N-tip implant on SONOS
  devices".[^pdk-06]
* SkyWater PDK, *Device Details* — SONOS cell dimensions and
  programme/erase voltages.[^pdk-07]
* SkyWater, *Facilities & Capabilities* — the Axcelis 8250 and GSD
  species, dose and energy ranges.[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]
* Semiconductor Online, *8250HT Medium Current Ion Implanter* — the
  tool class.[^axcelis-8250]

### High-level understanding

* Wikipedia, *Ion implantation* — sources, amorphisation
  threshold.[^wiki-implant]
* Wikipedia, *SONOS* — the cell.[^wiki-sonos]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — implantation
  and junction formation.[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — LDD design and
  doses.[^txt-04]

### Deep dive

* Ogura et al. (IBM), *IEEE TED* 1980 — the lightly doped
  drain.[^ogura-1980]
* Thompson et al. (Intel), VLSI 1998 — the extension depth/doping
  trade-off this implant deliberately takes the other way.[^thompson-1998]
* Jones and Ishida, *Mater. Sci. Eng. R* 1998 — shallow-junction
  doping, arsenic behaviour and {term}`TED`.[^rev-05]
* Nobili et al., *J. Electrochem. Soc.* 1983 — arsenic precipitation
  and deactivation, irrelevant at LDD doses but decisive at logic-tip
  doses.[^nobili-1983]
* Stolk et al. (Bell Labs), *J. Appl. Phys.* 1997 — transient enhanced
  diffusion from sub-amorphising implants.[^stolk-1997]
* White, Adams and Bu, *IEEE Circuits & Devices* 2000 — the SONOS
  cell's operation and reliability.[^pap-01]
* Eitan et al., *IEEE EDL* 2000 — the NROM cell, for contrast on drain
  engineering of charge-trapping memories.[^eitan-2000]
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — the
  embedded SONOS cell with its own implants.[^pat-04]
* Tran, McQueen and Kerr (Micron), US 6,759,288 — a lighter LDD on
  selected transistors to reduce junction leakage.[^pat-ldd-micron]
* Yu (AMD), US 6,521,502 — extension and halo activation by
  {term}`solid-phase epitaxy`, for contrast with a non-amorphising tip.[^pat-spe-amd]
* Chen et al., *Solid-State Electronics* 1995 — shadowing of tilted
  implants by neighbouring gates.[^chen-1995]
* Smith, Rosencwaig and Willenborg, *Appl. Phys. Lett.* 1985 — the
  thermal-wave implant monitor.[^smith-1985]

## Open questions

* The energy and dose of the lightly doped tip, and how much lighter
  than the logic tip it is, are not public.
* What dielectric covers the memory transistor's source/drain at this
  point — screen oxide alone, or remnants of the ONO stack — depends
  on the gate-etch and {ref}`ONOME <step-042>` details, which are not
  public.
* Whether the implant is at 7° with rotations or at 0° is not public.
* Whether the select transistor of the {term}`2-T cell` receives this tip or
  the logic tip is not public.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing". <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion
    Implanter* (Eaton Semiconductor Equipment Operations product
    description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-ash3]: Wikipedia, *Arsine*. <https://en.wikipedia.org/wiki/Arsine>
[^wiki-sonos]: Wikipedia, *SONOS*. <https://en.wikipedia.org/wiki/SONOS>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-04]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
    Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
    <https://openlibrary.org/isbn/9780961672157>
[^rev-05]: E. C. Jones and E. Ishida, "Shallow junction doping
    technologies for ULSI", *Materials Science and Engineering: R*
    **24**(1–2), 1–80 (1998).
    <https://doi.org/10.1016/S0927-796X(98)00013-8>
[^ogura-1980]: S. Ogura, P. J. Tsang, W. W. Walker, D. L. Critchlow and
    J. F. Shepard, "Design and characteristics of the lightly doped
    drain-source (LDD) insulated gate field-effect transistor", *IEEE
    Transactions on Electron Devices* **27**(8), 1359–1367 (1980).
    <https://doi.org/10.1109/T-ED.1980.20040>
[^thompson-1998]: S. Thompson, P. Packan, T. Ghani, M. Stettler,
    M. Alavi, I. Post, S. Tyagi, S. Ahmed, S. Yang and M. Bohr,
    "Source/drain extension scaling for 0.1 μm and below channel length
    MOSFETs", *1998 Symposium on VLSI Technology, Digest of Technical
    Papers*, pp. 132–133. <https://doi.org/10.1109/VLSIT.1998.689229>
[^nobili-1983]: D. Nobili, A. Carabelas, G. Celotti and S. Solmi,
    "Precipitation as the Phenomenon Responsible for the Electrically
    Inactive Arsenic in Silicon", *Journal of The Electrochemical
    Society* **130**(4), 922–928 (1983).
    <https://doi.org/10.1149/1.2119859>
[^stolk-1997]: P. A. Stolk, H.-J. Gossmann, D. J. Eaglesham, D. C.
    Jacobson, C. S. Rafferty, G. H. Gilmer, M. Jaraíz, J. M. Poate, H.
    S. Luftman and T. E. Haynes, "Physical mechanisms of transient
    enhanced dopant diffusion in ion-implanted silicon", *Journal of
    Applied Physics* **81**(9), 6031–6050 (1997).
    <https://doi.org/10.1063/1.364452>
[^pap-01]: M. H. White, D. A. Adams and J. Bu, "On the go with SONOS",
    *IEEE Circuits and Devices Magazine* **16**(4), 22–31 (2000).
    <https://doi.org/10.1109/101.857747>
[^eitan-2000]: B. Eitan, P. Pavan, I. Bloom, E. Aloni, A. Frommer and
    D. Finzi, "NROM: A novel localized trapping, 2-bit nonvolatile
    memory cell", *IEEE Electron Device Letters* **21**(11), 543–545
    (2000). <https://doi.org/10.1109/55.877205>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098 B1,
    granted 2014-08-05. <https://patents.google.com/patent/US8796098B1/en>
[^pat-ldd-micron]: L. C. Tran, M. McQueen and R. Kerr (Micron
    Technology), *Double LDD devices for improved DRAM refresh*, US
    6,759,288 B2, granted 2004-07-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6759288>
[^pat-spe-amd]: B. Yu (Advanced Micro Devices), *Solid phase epitaxy
    activation process for source/drain junction extensions and halo
    regions*, US 6,521,502 B1, granted 2003-02-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6521502>
[^chen-1995]: H.-S. Chen, C.-S. Teng, L. Moberly and R. Lahri, "Ion beam
    shadowing effect in submicrometer large-angle-tilt implanted drain
    (LATID) MOSFETs", *Solid-State Electronics* **38**(7), 1321–1323
    (1995). <https://doi.org/10.1016/0038-1101(94)00256-F>
[^smith-1985]: W. L. Smith, A. Rosencwaig and D. L. Willenborg, "Ion
    implant monitoring with thermal wave technology", *Applied Physics
    Letters* **47**(6), 584–586 (1985).
    <https://doi.org/10.1063/1.96079>
