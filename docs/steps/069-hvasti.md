(step-069)=
# Step 069 — HVASTI: HV As N-tip implant

| | |
|---|---|
| **Step number** | 69 of 171[^steps-sheet] |
| **Step code** | `HVASTI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | {term}`FEOL` — extensions, spacers, source/drain |
| **Previous step** | {ref}`HVNTM <step-068>` |
| **Next step** | {ref}`HVASTIS <step-070>` |

## What this step is

`HVASTI` is the arsenic implant that forms the drain {term}`extension` of the
high-voltage (5 V-class) NMOS transistors. Through the thin resist
windows opened at {ref}`HVNTM <step-068>`, and through the {term}`screen oxide`
inferred at {ref}`IOX45 <step-063>`, arsenic ions strike the wafer at a
steep angle — the PDK's assumptions page gives "Angle for HV tip
implant" 40° and "Twist angle for HV Tip" 23°[^pdk-03] — so that the
implanted region reaches *under* the edge of the polysilicon gate
rather than stopping at it. After {ref}`TIPRTAD <step-075>` the result
is a lightly doped, graded n⁻ region overlapped by the gate on both
sides of the channel: the *large-angle-tilt implanted drain* ({term}`LATID`) of
Hori,[^hori-1989-latid][^hori-1992] the modern descendant of the lightly
doped drain.[^ogura-1980]

The PDK gives arsenic as its N-tip species in general ("N Tip
(As)"),[^pdk-03] and this reference describes the step as an arsenic
implant on that basis. Energy and dose are not public. Unlike the
1.8 V tip, this reference describes no {term}`halo` for this device
before its strip {ref}`HVASTIS <step-070>`: a 0.5 µm "HV MOSFET
channel length"[^pdk-03] is long enough not to need one (inference).

## Step category

`HVASTI` is an {ref}`Ion implantation <category-implant>` step of the
*{term}`LDD`* class: a moderate dose — of order 10¹³ cm⁻² is typical of an LDD
for a 3.3–5 V transistor[^txt-04] — at tens of keV, delivered at a
large tilt with wafer rotation. It is the flow's most steeply tilted
implant, and the one whose geometry the PDK documents most completely
(resist thickness, angle, twist, {term}`shadowing`, penetration).[^pdk-03]

## Why this step exists

At 5.5 V on the drain, an abrupt, heavily doped tip of the
{ref}`ASTI <step-065>` kind would concentrate the lateral field at the
gate edge and inject hot electrons into the gate oxide — the
degradation mechanism Hu and co-workers modelled, monitored and showed
how to reduce by drain engineering.[^hu-1985-hci] The LDD spreads the
field over a lightly doped region;[^ogura-1980][^ogura-1981] Takeda's
group compared drain structures for minimum hot-carrier
generation;[^takeda-1982] and Hori's LATID improved on the LDD by
implanting the n⁻ region at a large tilt so that it lies *under* the
gate, where the gate field keeps it conductive, instead of under the
{term}`spacer`, where an un-gated n⁻ region adds series resistance and can
itself be damaged by hot carriers.[^hori-1992] Rafí and Campabadal's
direct comparison of LDD and LATID NMOS shows the reliability
difference.[^rafi-2001] King et al. showed how the spacer over the n⁻
region sets the worst-case stress condition.[^king-2000]

The PDK's 40° angle[^pdk-03] is therefore the strongest public hint
about the nature of the SKY130 5 V NMOS: not a plain LDD but a
gate-overlapped, tilt-implanted drain. The PDK's Table F2b marks
`HVNTM` "created" for `nfet_g5v0d10v5`, the ESD NMOS built on it, the
5 V and 3.3 V native NMOS, the 16 V drain-extended NMOS, four HV
diodes, an HV n-diffusion resistor and an HV varactor,[^pdk-06] so this is where those
devices' n-type extension is defined, all on the 110 Å
oxide;[^pdk-hv] how the implant is placed relative to a drain-extended
device's drift well is not stated. The
20 V {term}`drain-extended <DEMOS>` NMOS uses an N-well {term}`drift region` as its drain
extension[^pdk-hv][^mitros-2001] and Table F2b marks it "-" ("Layer not
created for the device"), so it does not take this tip.

Without `HVASTI`, the 5 V NMOS would be either unreliable (with the
1.8 V tip) or non-functional (with an undoped gap under the spacer
between channel and n⁺ drain).

## How it is typically performed

An industry-generic large-tilt LDD implant for a 200 mm, 130 nm-era
fab (SKY130's energy and dose are not public):

* **Species and source.** ⁷⁵As⁺ from arsine or solid
  arsenic.[^wiki-implant][^wiki-ash3] The original LDD used
  phosphorus;[^ogura-1980] arsenic's lower diffusivity[^rev-05] keeps a
  0.5 µm channel[^pdk-03] from shortening during the later anneals and
  gives a better-defined overlap, at the price of a less graded
  profile.
* **Energy and dose.** Tens of keV and of order 10¹³ cm⁻²
  (typical);[^txt-04][^txt-01] the dose sets the n⁻ {term}`sheet resistance`
  and hence the trade between hot-carrier margin and on-resistance,
  and the energy sets how far the tilted beam reaches under the gate.
  The PDK's "N+ or P+ S/D (XJ)" of 0.1 µm[^pdk-03] bounds the depth the
  later n⁺ junction will reach; the LDD is shallower.
* **Tilt, twist and rotation.** 40° tilt with a 23° twist.[^pdk-03] We
  read the twist as rotating the beam's plane of incidence away from
  the wafer's low-index channelling directions and away from the gate
  edges: with gates on a Manhattan grid, a beam twisted 23° from the
  flat has a component along both gate orientations, so neither is
  fully shadowed (inference; the PDK publishes the angle and no
  explanation[^pdk-03]). We further
  infer that the implant is split into rotations so that source and
  drain, and gates running in both directions, are implanted
  symmetrically.[^pat-quad-tsmc] The lateral reach under the gate is
  set by the tilt and the screen oxide; the resist and the neighbouring
  gates shadow the beam — the PDK's "HVNTM shadowing" of 0.232 µm and
  "Photoresist tilted implant blocking distance" of 0.013 µm[^pdk-03]
  are the mask generator's allowances for this, and Chen et al.
  measured the device consequences of such shadowing in LATID
  transistors.[^chen-1995]
* **Resist.** Only 0.3 µm thick,[^pdk-03] so that the wall casts a
  short shadow; the PDK's 0.02 µm "Photoresist tilted implant
  penetration"[^pdk-03] allows for ions that pass through the resist
  edge. Outgassing scales with the volume of resist exposed to the
  beam — Lee and co-workers characterised it for thick resist under MeV
  implantation[^lee-1996] — so a 0.3 µm film outgasses less than the
  standard 1.14 µm one[^pdk-03] (inference); charging is likewise reduced with
  less resist volume, but an electron shower and electrostatic chuck ("ESC
  chuck, E shower" on SkyWater's medium-current tool) are, we infer,
  still used;[^skw-01] platen cooling is industry practice.
* **Anneal.** None here; activation at {ref}`TIPRTAD <step-075>`.
* **Monitoring.** Thermal-wave measurement on monitor
  wafers;[^smith-1985] tilt-angle verification is the specific control
  item for a 40° implant.

## Machines typically used

* **{ref}`Medium-current ion implanter <machine-medium-current-implanter>`**, 200 mm, single-wafer with a
  tilting, rotating platen: Axcelis (Eaton) 8250 class, Varian
  E220/E500 and VIISta 810, Applied Materials xR LEAP
  ({ref}`category-implant`). The 8250HT covers "3keV to 750keV" with
  beam currents "between 4µA and 3,500µA".[^axcelis-8250]
* **{ref}`Thermal-wave <machine-sheet-resistance-metrology>`** metrology.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current implanter.** SkyWater lists "Axcelis
  8250 Mid current B11, BF2, As, ESC chuck, E shower, 1e11 to 1e14,
  0-60 deg tilt".[^skw-01] Arsenic, a dose window that contains an LDD
  dose, and a tilt range that reaches 60° — the published 40° HV tip
  angle[^pdk-03] fits inside it. Strength: **strong** for the tool and
  its tilt range; **inference** for the assignment, because it is the
  only listed tool with a *stated* tilt range, and that range covers
  40°.
* **Axcelis GSD implanters (high-current/high-energy and high-dose)**
  ("10-3000kev, 1e11 to 5e15, tilt/twist" and "2-180kev, 5e12 to 5e16,
  tilt/twist")[^skw-01] — batch tools listed with tilt and twist capability
  but with no stated tilt range. Strength: strong for existence; weak for
  assignment.

## Resources required

* **{ref}`Arsine <material-dopant-sources>` (AsH₃)** or a **solid arsenic** source
  charge;[^wiki-implant][^wiki-ash3] gas-cabinet monitoring for the
  toxic gas.
* **Source-support gases**, source consumables, high-purity
  **{ref}`nitrogen <material-process-gases>`** for venting.
* **Helium** for platen cooling; **liquid nitrogen** or cryopump
  regeneration.
* **{ref}`Monitor wafers <material-substrates>`** for thermal-wave and tilt control.
* Gas suppliers named in SkyWater's filings: Air Products and Praxair
  (2021 S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`HVNTM <step-068>` (the thin resist mask); screen
  oxide: {ref}`IOX45 <step-063>`.
* Next: {ref}`HVASTIS <step-070>` (strip).
* The other tips: {ref}`ASTI <step-065>` (1.8 V NMOS),
  {ref}`LDASTI <step-072>` ({term}`SONOS` transistors); the 1.8 V halo:
  {ref}`BHI <step-066>`.
* The thick gate oxide of these devices: {ref}`GOX100 <step-043>`,
  {ref}`LVOM <step-044>`; the drain-extended devices' drift wells:
  {ref}`NWI <step-018>`, {ref}`PWDEM <step-030>`.
* Activation: {ref}`TIPRTAD <step-075>`; spacer:
  {ref}`SPNIT <step-076>`; deep n⁺ junction: {ref}`NSDI <step-086>`.
* Category page: {ref}`Ion implantation <category-implant>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Multiple tilted angle ion implantation MOSFET method <patent-gp22246938>` — US 5,372,957 A (1993)
* {ref}`Method and structure for a single-sided non-self-aligned transistor <patent-gp26739424>` — US 6,586,806 B1 (1997)
* {ref}`Method and structure for high-voltage device with self-aligned graded junctions <patent-gp25418952>` — US 6,531,366 B1 (2001)

:::{dropdown} 2 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 9,111,985 B1 <patent-gp53786102>` — unknown
* {ref}`US 7,936,023 B1 <patent-gp43903297>` — unknown
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, *Criteria & Assumptions* — 40° HV tip angle, 23°
  twist, 0.3 µm HV-tip resist, 0.232 µm shadowing, 0.02 µm penetration,
  0.013 µm blocking distance, 0.5 µm HV MOSFET channel length, "N Tip
  (As)".[^pdk-03]
* SkyWater PDK, *Device Details* — the 5 V NMOS family and the 0.9 µm
  minimum gate length of the native 5 V NMOS.[^pdk-07]
* SkyWater PDK, *High Voltage Methodology* — 110 Å oxide; N-well drain
  extensions for the VHV devices.[^pdk-hv]
* SkyWater, *Facilities & Capabilities* — the Axcelis 8250's arsenic,
  dose and "0-60 deg tilt".[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]
* Semiconductor Online, *8250HT Medium Current Ion Implanter* — the
  tool class.[^axcelis-8250]

### High-level understanding

* Wikipedia, *Hot-carrier injection* — the failure mode.[^wiki-hci]
* Wikipedia, *Ion implantation* — tilt, {term}`channelling`, sources.[^wiki-implant]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — LDD, LATID
  and hot-carrier design.[^txt-04]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — implantation
  and junction formation.[^txt-01]
* Jones and Ishida, *Mater. Sci. Eng. R* 1998 — dopant behaviour in
  shallow junctions.[^rev-05]

### Deep dive

* Hori (Matsushita), IEDM 1989 — the LATID transistor.[^hori-1989-latid]
* Hori et al. (Matsushita), *IEEE TED* 1992 — LATID technology in
  full: tilt, dose, overlap and reliability.[^hori-1992]
* Ogura et al. (IBM), *IEEE TED* 1980 — the LDD.[^ogura-1980]
* Ogura et al. (IBM), IEDM 1981 — elimination of hot-electron gate
  current by the LDD structure.[^ogura-1981]
* Takeda et al. (Hitachi), *IEEE TED* 1982 — drain structures for
  minimum hot-carrier generation.[^takeda-1982]
* Hu et al. (Berkeley), *IEEE TED* 1985 — the hot-electron lifetime
  model.[^hu-1985-hci]
* Rafí and Campabadal, *Solid-State Electronics* 2001 — LDD versus
  LATID hot-carrier degradation.[^rafi-2001]
* King, Lacoe and Wang-Ratkovic, IRPS 2000 — spacer oxide and
  worst-case stress in LDD NMOS.[^king-2000]
* Chen et al., *Solid-State Electronics* 1995 — beam shadowing in
  LATID MOSFETs.[^chen-1995]
* Mitros et al. (TI), *IEEE TED* 2001 — the drain-extended
  alternative.[^mitros-2001]
* Kouznetsov (Cypress), US 6,531,366 — self-aligned {term}`graded junctions <graded junction>`
  for a high-voltage device.[^pat-hv-graded-cyp]
* Lin, Yoo and Liang (TSMC), US 5,372,957 — multiple tilted-angle
  implantation with rotation.[^pat-quad-tsmc]
* Lee et al. (Genus), IIT 1996 — resist outgassing under
  implantation.[^lee-1996]
* Smith, Rosencwaig and Willenborg, *Appl. Phys. Lett.* 1985 — the
  thermal-wave monitor.[^smith-1985]

## Open questions

* The HV tip energy and dose are not public; the LDD-typical values
  above are from textbooks.
* The number of rotations at 40°/23°, and whether the twist is fixed or
  alternated between rotations, is not public.
* Table F2b marks `HVNTM` "C (CREATED)" on the 5/10.5 V NMOS, the 5 V
  and 3 V native NMOS, the 16 V drain-extended NMOS, the HV and HV
  native ESD NMOS, the HV n-diffusion resistor, the HV varactor and
  four n-type diodes, and "-" ("Layer not created for the device") on
  every PMOS row and on all five UHV 5/20 V rows;[^pdk-06] see the
  {ref}`HVNTM mask page <mask-hvntm>`. What the table does not say is
  why the 20 V devices are excluded, or on which side of a
  drain-extended device the implant lands.
* Whether the 5 V PMOS has a corresponding tilted p-tip — the PDK's
  "HVPTM shadowing" parameter[^pdk-03] suggests one was at least
  contemplated, and its *High Voltage Methodology* page says hv
  p-channel devices "get the extra junction grading implant into the
  ringed gate with the HVPDM mask",[^pdk-hv] a mask name absent from
  the PDK's `masks.csv`[^pdk-05] — is not stated publicly; this
  reference describes none.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* (including Table
    F2b, the mask generation table) and `gds_layers.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
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
[^wiki-hci]: Wikipedia, *Hot-carrier injection*.
    <https://en.wikipedia.org/wiki/Hot-carrier_injection>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-ash3]: Wikipedia, *Arsine*. <https://en.wikipedia.org/wiki/Arsine>
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
[^hori-1989-latid]: T. Hori, "1/4-μm LATID (LArge-Tilt-angle Implanted
    Drain) technology for 3.3-V operation", *IEDM 1989 Technical
    Digest*, pp. 777–780. <https://doi.org/10.1109/IEDM.1989.74169>
[^hori-1992]: T. Hori, J. Hirase, Y. Odake and T. Yasui,
    "Deep-submicrometer large-angle-tilt implanted drain (LATID)
    technology", *IEEE Transactions on Electron Devices* **39**(10),
    2312–2324 (1992). <https://doi.org/10.1109/16.158803>
[^ogura-1980]: S. Ogura, P. J. Tsang, W. W. Walker, D. L. Critchlow and
    J. F. Shepard, "Design and characteristics of the lightly doped
    drain-source (LDD) insulated gate field-effect transistor", *IEEE
    Transactions on Electron Devices* **27**(8), 1359–1367 (1980).
    <https://doi.org/10.1109/T-ED.1980.20040>
[^ogura-1981]: S. Ogura, P. J. Tsang, W. W. Walker, D. L. Critchlow and
    J. F. Shepard, "Elimination of hot electron gate current by the
    lightly doped drain-source structure", *IEDM 1981 Technical
    Digest*, pp. 651–654. <https://doi.org/10.1109/IEDM.1981.190171>
[^takeda-1982]: E. Takeda, H. Kume, T. Toyabe and S. Asai,
    "Submicrometer MOSFET structure for minimizing hot-carrier
    generation", *IEEE Transactions on Electron Devices* **29**(4),
    611–618 (1982). <https://doi.org/10.1109/T-ED.1982.20752>
[^hu-1985-hci]: C. Hu, S. C. Tam, F.-C. Hsu, P.-K. Ko, T.-Y. Chan and K. W.
    Terrill, "Hot-electron-induced MOSFET degradation — Model, monitor,
    and improvement", *IEEE Transactions on Electron Devices* **32**(2),
    375–385 (1985). <https://doi.org/10.1109/T-ED.1985.21952>
[^rafi-2001]: J. M. Rafí and F. Campabadal, "Hot-carrier degradation in
    deep-submicrometer nMOSFETs: lightly doped drain vs. large angle
    tilt implanted drain", *Solid-State Electronics* **45**(8),
    1391–1401 (2001). <https://doi.org/10.1016/S0038-1101(01)00004-1>
[^king-2000]: E. E. King, R. C. Lacoe and J. Wang-Ratkovic, "The role
    of the spacer oxide in determining worst-case hot-carrier stress
    conditions for NMOS LDD devices", *Proc. 2000 IEEE International
    Reliability Physics Symposium*, pp. 83–92.
    <https://doi.org/10.1109/RELPHY.2000.843895>
[^chen-1995]: H.-S. Chen, C.-S. Teng, L. Moberly and R. Lahri, "Ion beam
    shadowing effect in submicrometer large-angle-tilt implanted drain
    (LATID) MOSFETs", *Solid-State Electronics* **38**(7), 1321–1323
    (1995). <https://doi.org/10.1016/0038-1101(94)00256-F>
[^mitros-2001]: J. C. Mitros, C.-Y. Tsai, H. Shichijo, M. Kunz, A.
    Morton, D. Goodpaster, D. Mosher and T. R. Efland, "High-voltage
    drain extended MOS transistors for 0.18-µm logic CMOS process",
    *IEEE Transactions on Electron Devices* **48**(8), 1751–1755 (2001).
    <https://doi.org/10.1109/16.936703>
[^pat-hv-graded-cyp]: I. Kouznetsov (Cypress Semiconductor), *Method
    and structure for high-voltage device with self-aligned graded
    junctions*, US 6,531,366 B1, granted 2003-03-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6531366>
[^pat-quad-tsmc]: M.-S. Lin, C.-S. Yoo and M.-S. Liang (Taiwan
    Semiconductor Manufacturing Company), *Multiple tilted angle ion
    implantation MOSFET method*, US 5,372,957 A, granted 1994-12-13.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5372957>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^smith-1985]: W. L. Smith, A. Rosencwaig and D. L. Willenborg, "Ion
    implant monitoring with thermal wave technology", *Applied Physics
    Letters* **47**(6), 584–586 (1985).
    <https://doi.org/10.1063/1.96079>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
