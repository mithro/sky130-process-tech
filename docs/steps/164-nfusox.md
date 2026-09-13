(step-164)=
# Step 164 — NFUSOX: Fuse oxide deposition

| | |
|---|---|
| **Step number** | 164 of 171 |
| **Step code** | `NFUSOX` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | BEOL — passivation, pads, alloy, test |
| **Previous step** | {ref}`MM5E <step-163>` |
| **Next step** | {ref}`NSM <step-165>` |

## What this step is

`NFUSOX` is the first deposition after the last metal etch: a thin,
blanket, low-temperature oxide laid over the freshly etched metal-5
lines, pads and the {ref}`NCAPOX6 <step-158>` oxide between them. It
opens the *passivation* module — the insulating "glass" that seals the
finished circuit — which continues with the silicon nitride of
{ref}`NTSD <step-167>` and is cut open over the bond pads at
{ref}`PDM <step-168>` / {ref}`PDME <step-169>`.

The PDK's process stack diagram draws exactly such a film. Directly on
`metal5` (1.26 µm thick on the diagram) it shows a thin layer labelled
"TOPOX K=3.9", dimensioned 0.09 µm on the top of the metal and
0.070 µm on its sidewall, and over that a thicker "TOPNIT K=7.5"
nitride dimensioned 0.54 µm on top and 0.4223 µm on the sidewall;
a "glass cut" is drawn through both over the metal, and an optional
polyimide ("PI1 K=2.94") tops the stack.[^pdk-04] The Cypress
qualification reports for other processes at the same Bloomington fab
describe their passivation in the same two-layer form: "1000Å TEOS /
9000Å PECVD Nitride" for the 0.18 µm R7FT-3R derivative in
2005,[^cyp-qtp-014807] and "1000A TEOS/9000A Si3N4" for the S8DI
metal-stack-change report of 2014,[^cyp-qtp-123907] while the 2013
S8TNV-5R report gives only "7000 +/- 2000A Nitride".[^cyp-qtp-113005]
The step list used in this reference does not explain what the oxide
is for; we read `NFUSOX` as the
deposition of the thin undoped oxide the PDK labels TOPOX (inference:
it is the only oxide the diagram draws between metal 5 and the
nitride, and its 0.09 µm matches the 1000 Å TEOS film of the Cypress
reports within the diagram's rounding[^pdk-04][^cyp-qtp-123907]).

The PDK also documents laser-programmable metal fuses. Its layer table
lists `target` (76:44), "Metal fuse target", on the same GDS layer
number as `pad` (76:20, "Passivation cut (opening over
pads)"),[^pdk-06] its periphery rules define metal fuses 0.800 µm wide
and 7.200 µm long (mf.1, mf.2) with the note "For SP8P*/SKY130P* (PLM)
CADflow use MM4 for Metal Fuse",[^pdk-periph] and its assumptions page
has a "Laser Fuse Criteria" table (a nominal effective laser spot
diameter of 3.5 µm, a fuse melting radius of 3.6 µm, a "Melting related
crack size in ILD" of 0.36 µm) and a polyimide rule, "Enclosure of fuses
by polyimide", of 12.[^pdk-03] Whether this oxide plays any part in the
fuse windows is not stated publicly (see *Open questions*).

## Step category

`NFUSOX` is a {ref}`Thin-film deposition <category-deposition>` step
of the *{term}`PECVD` oxide* class, like the cap oxides
{ref}`NCAPOX3 <step-117>` to {ref}`NCAPOX6 <step-158>`. Two things set
it apart. It is deposited not on a polished, flat oxide but directly on
patterned aluminium — 1.26 µm-tall metal-5 lines at 1.600 µm minimum
width and space (m5.1, m5.2[^pdk-periph][^pdk-04]) — so it must cover
tops, sidewalls and the floor between lines (the diagram's separate
top and sidewall dimensions show a conformal film[^pdk-04]). And it is
the first layer of the permanent passivation: no {term}`CMP` follows,
nothing is deposited on it except the nitride, and it stays on the
finished die except where the pad and seal openings are cut. The
metal-5 spaces are wide (an {term}`aspect ratio` of about 0.8:1, our
arithmetic from the PDK values), so {term}`gap fill` is not the
problem it is at {ref}`NILD5 <step-141>`.

## Why this step exists

The physics of an oxide–nitride passivation is well documented; the
reasons for the oxide in SKY130 specifically are inferred.

* **A buffer between aluminium and nitride.** PECVD silicon nitride is
  the moisture and mobile-ion barrier of a plastic-packaged die — Sinha
  et al. described reactive-plasma Si–N films for MOS-LSI
  passivation,[^sinha-1978] and a later seal-ring patent describes the
  passivation nitride over its passivation oxide as "a very good barrier
  of moisture and ionic contamination"[^pat-sealring-zeevo] — but
  it is hydrogen-rich and highly stressed.[^lanford-1978][^claassen-1985]
  A thin oxide between the metal and the nitride separates the
  aluminium from the nitride's deposition chemistry and adds a
  compliant layer under a stiff film; stress in the dielectric over
  aluminium lines drives {term}`stress-induced voiding` (Yue, Funsten
  and Taylor[^yue-1985]) and {term}`hillock` growth
  (Chaudhari[^chaudhari-1974]). That an oxide under the nitride serves
  this purpose in SKY130 is our inference from the stack and the
  industry pattern.[^txt-05]
* **Doped or undoped.** Passivation oxides under nitride have often
  been phosphorus-doped — the seal-ring patent notes that the
  passivation oxide "is usually doped with phosphorous to form
  phosphosilicate glass (PSG) to absorb and hold the moisture", and also
  that in 0.25 and 0.18 µm technologies a passivation oxide "without
  phosphorous has been used and has passed reliability
  tests"[^pat-sealring-zeevo] — but too much phosphorus corrodes
  aluminium, as Paulson and Kirk showed for passivation
  glasses.[^paulson-1974] The R7FT-3R report lists "Free Phosphorus
  contents in top glass layer(%): 0%"[^cyp-qtp-014807] and the PDK gives
  TOPOX the undoped-oxide permittivity of 3.9;[^pdk-04] we read the
  SKY130 film as undoped (inference).
* **An interface for the pad opening.** The pad etch
  ({ref}`PDME <step-169>`) cuts the nitride with fluorine chemistry;
  a known oxide between nitride and metal gives that etch a change in
  emission and rate before the aluminium is reached (industry practice;
  inference for this flow).
* **Controlled dielectric over laser fuses (possible).** Laser
  programmable redundancy, demonstrated by Smith et al. on a 64K
  DRAM,[^smith-1981] depends on the transparent dielectric over the
  link: Scarfone and Chlipala modelled how the films encapsulating a
  link create "important optical interference effects modifying the
  laser flux absorbed" and how the link must build enough pressure
  "to rupture the dielectric above the link".[^scarfone-1986] Fuse
  patents therefore control the oxide left over a fuse — an IBM patent
  gives "<2000 Å" as crack-prone and ">8000 Å" as needing too much
  laser energy,[^pat-fuse-ibm] a Vanguard patent targets "about 0.35
  microns" under a silicon oxide/silicon nitride
  passivation,[^pat-fuse-vanguard] and a TSMC patent opens a shallow
  window in an oxide/nitride blanket so that the remaining oxide "can be
  moderated and controlled within a narrow window".[^pat-fuse-tsmc]
  Whether TOPOX has such a role in SKY130 is not public.

Without this oxide, on our reading, the nitride would be deposited
directly on the aluminium and on the cap oxide, and the pad etch would
have no intermediate layer between nitride and metal.

## How it is typically performed

An industry-generic first passivation oxide over a thick aluminium top
metal in a 200 mm, 130 nm-era fab (SKY130's recipe is not public):

1. **Surface.** The wafer comes from the {ref}`MM5E <step-163>`
   post-etch passivation, strip and polymer clean; the {term}`queue time`
   before deposition is limited so that residual chlorine does not corrode the
   exposed Al–Cu (industry practice[^txt-05]).
2. **Chamber and temperature.** A single-wafer or multi-station PECVD
   reactor at roughly 300–400 °C (industry-typical for films on
   aluminium[^txt-05][^wiki-pecvd]); SkyWater lists "PECVD TEOS, C2 and
   Producer – low temp options" and "PECVD silane
   oxide/nitride/oxynitride, C1 – low temp, range of R.I.
   options".[^skw-01]
3. **Chemistry.** {term}`TEOS`/O₂ plasma oxide — Raupp, Cale and Hey
   analyse its kinetics[^raupp-1992] — or SiH₄/N₂O plasma oxide, whose
   properties depend on RF power as Chapple-Sokol, Tierney and Batey
   measured.[^chapple-sokol-1989] Adams et al. characterised plasma
   oxide composition and hydrogen,[^adams-1981-pecvd] and Lanford and
   Rand found 5.7 at.% hydrogen, all as OH, in a plasma SiO₂ deposited
   at 300 °C.[^lanford-1978] The Cypress reports name TEOS for the
   corresponding film.[^cyp-qtp-123907][^cyp-qtp-014807]
4. **Thickness.** About 0.09–0.1 µm, from the PDK's TOPOX label and the
   1000 Å of the Cypress reports;[^pdk-04][^cyp-qtp-123907] a
   conformal film, somewhat thinner on the sidewalls (0.070 µm on the
   diagram[^pdk-04]).
5. **Film properties and plasma exposure.** A dense, low-hydrogen,
   mildly compressive film; hydrogen evolution on later heating changes
   plasma-oxide stress, as Mani and Saif showed,[^mani-2007] and the
   final {ref}`ALLY <step-170>` anneal will heat it. The deposition
   plasma reaches every metal-5 line and, through the interconnect, the
   gates; Cheung described the charging mechanism of plasma-enhanced
   dielectric deposition.[^cheung-2000]
6. **Metrology.** Thickness and refractive index by ellipsometry on
   monitors; stress by wafer bow; particles. NF₃ chamber clean between
   runs.

## Machines typically used

* **PECVD dielectric system**, 200 mm: Novellus Concept One/Two or
  Sequel,[^novellus-history] Applied Materials Producer or Centura
  DxZ[^amat-10k] ({ref}`category-deposition`).
* **Ellipsometer / reflectometer**, **stress gauge**, **particle
  inspection**.

## Machines likely used at SkyWater

* **PECVD TEOS "C2 and Producer" with "low temp options".**[^skw-01]
  Strength: **strong** for the capability; the assignment of this film
  to the TEOS process is an **inference** from the "TEOS" of the Cypress
  passivation descriptions at the same fab.[^cyp-qtp-123907][^cyp-qtp-014807]
  "C2" as a Novellus Concept Two and "Producer" as an Applied Materials
  Producer are readings of the names,[^novellus-history][^amat-10k] not
  stated by SkyWater.
* **PECVD silane oxide "C1"**[^skw-01] as the alternative (medium); a
  silane oxide and the following nitride could share a chamber type
  (inference).

## Resources required

* **TEOS** (liquid, vaporised) and **oxygen** with **helium**
  carrier,[^wiki-teos] or **silane** and **N₂O** for the silane
  route;[^wiki-pecvd] gas suppliers per SkyWater's filings.[^sec-01]
* **NF₃** for the chamber clean; **nitrogen** purge.
* **Showerhead, heater and liner consumables**; **monitor wafers**.

## Related steps and cross-references

* Previous: {ref}`MM5E <step-163>` (the metal-5 lines and pads it
  covers). Next: {ref}`NSM <step-165>` and {ref}`NSME <step-166>` (the
  seal-ring opening), then {ref}`NTSD <step-167>` (the passivation
  nitride over this oxide).
* The pad opening through this film: {ref}`PDM <step-168>`,
  {ref}`PDME <step-169>`; the anneal that follows the passivation:
  {ref}`ALLY <step-170>`.
* The metal fuses the PDK places in metal 4: {ref}`MM4 <step-154>`.
* The other plasma oxides of the back end: {ref}`NCAPOX3 <step-117>`,
  {ref}`NCAPOX6 <step-158>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, *Process stack diagram* — "TOPOX K=3.9" 0.09 µm (top)
  and 0.070 µm (sidewall); "TOPNIT K=7.5" 0.54 µm and 0.4223 µm;
  "glass cut"; "PI1 K=2.94"; `metal5` 1.26 µm.[^pdk-04]
* SkyWater PDK, *Layers Reference* — `pad` 76:20 "Passivation cut
  (opening over pads)"; `target` 76:44 "Metal fuse target".[^pdk-06]
* SkyWater PDK, *Periphery rules* — m5.1, m5.2; mf.1–mf.24 and the MM4
  metal-fuse note.[^pdk-periph]
* SkyWater PDK, *Criteria & Assumptions* — Laser Fuse Criteria; polyimide
  enclosure of fuses.[^pdk-03]
* Cypress, QTP 014807 (2005) and QTP 123907/132302/132301 (2014) — "1000Å
  TEOS / 9000Å PECVD Nitride", "1000A TEOS/9000A Si3N4"; 0 % free
  phosphorus.[^cyp-qtp-014807][^cyp-qtp-123907]
* Cypress, QTP 113005 (2013) — "7000 +/- 2000A Nitride".[^cyp-qtp-113005]
* SkyWater, *Facilities & Capabilities* — PECVD TEOS and silane oxide
  entries.[^skw-01]
* SkyWater, Form S-1 — gas suppliers.[^sec-01]

### High-level understanding

* Wikipedia, *Plasma-enhanced chemical vapor deposition*, *Tetraethyl
  orthosilicate*.[^wiki-pecvd][^wiki-teos]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — back-end
  dielectrics and passivation.[^txt-05]
* Novellus company history; Applied Materials 10-K — the 200 mm PECVD
  platforms.[^novellus-history][^amat-10k]

### Deep dive

* Sinha et al., *J. Electrochem. Soc.* 1978 —
  reactive-plasma Si–N films for MOS-LSI passivation, the film this
  oxide lies under.[^sinha-1978]
* Lanford and Rand, *J. Appl. Phys.* 1978 — hydrogen in plasma nitride
  and in a plasma oxide deposited at 300 °C.[^lanford-1978]
* Adams et al., *J. Electrochem. Soc.* 1981 — characterisation of
  plasma-deposited silicon dioxide.[^adams-1981-pecvd]
* Raupp, Cale and Hey, *JVST B* 1992 — PECVD TEOS oxide
  kinetics.[^raupp-1992]
* Chapple-Sokol, Tierney and Batey (IBM), MRS 1989 — RF-power dependence
  of PECVD oxide properties.[^chapple-sokol-1989]
* Mani and Saif, *Thin Solid Films* 2007 — stress change from hydrogen
  evolution in plasma oxide.[^mani-2007]
* Yue, Funsten and Taylor, IRPS 1985, and Chaudhari, *J. Appl. Phys.*
  1974 — stress voids and hillocks in aluminium under
  dielectrics.[^yue-1985][^chaudhari-1974]
* Paulson and Kirk, IRPS 1974 — why the glass next to aluminium is
  undoped.[^paulson-1974]
* Smith et al., *IEEE JSSC* 1981 — laser
  programmable redundancy on a 64K DRAM.[^smith-1981]
* Scarfone and Chlipala, *J. Mater. Res.* 1986 — optical interference
  and dielectric rupture in laser link cutting.[^scarfone-1986]
* Lee, Klaasen and Mitwalsky (IBM), US 5,872,390; Tzeng, Chen and Wang
  (Vanguard), US 6,294,474; Yang and Su (TSMC), US 6,835,642 — controlling
  the oxide left over a laser fuse under an oxide/nitride
  passivation.[^pat-fuse-ibm][^pat-fuse-vanguard][^pat-fuse-tsmc]
* Bothra, McKay and Jhota (Zeevo), US 6,492,716 — a seal ring under a
  passivation oxide and nitride.[^pat-sealring-zeevo]
* Cheung, P2ID 2000 — charging during plasma-enhanced dielectric
  deposition.[^cheung-2000]

## Open questions

* The step list used in this reference does not explain the film; that
  it is the PDK's TOPOX is our reading. Its precursor (TEOS or silane),
  thickness and deposition conditions are not public; 0.09 µm is the
  diagram's label[^pdk-04] and 1000 Å the Cypress reports' value for
  other processes.[^cyp-qtp-123907][^cyp-qtp-014807]
* Whether this oxide is involved in laser-fuse windows over the metal-4
  fuses, and how the fuse `target` layer on GDS layer 76[^pdk-06] is
  turned into an opening (with the pad mask or otherwise), is not
  public.
* The Cypress reports disagree on whether an oxide lies under the
  nitride (S8TNV-5R lists nitride only[^cyp-qtp-113005]); which
  description applies to SKY130 lots is not public beyond the PDK
  diagram.
* The stack diagram also dimensions 0.3777 µm beside metal 5;[^pdk-04]
  what film thicknesses that label combines in the field between lines
  is not stated.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^cyp-qtp-113005]: Cypress Semiconductor, *Product Qualification
    Plan, QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8
    Technology, CMI (Fab 4)*, document 001-85611 Rev. *A, January
    2013 (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^cyp-qtp-123907]: Cypress Semiconductor, *Fab Process Qualification
    Report, QTP# 123907, 132302, 132301: Metal Stack Change, S8
    Technology, Fab 4 CMI*, document 001-91369 Rev. **, March 2014
    (copy hosted by Tokyo Electron Device as the attachment to
    Cypress Product Information Notification PIN145273, 2014-03-13,
    which states the report is attached and available from
    cypress.com; <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>).
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/145273-Qualification_Report.pdf>
[^cyp-qtp-014807]: Cypress Semiconductor, *Technology Derivative
    Qualification Report, QTP# 014807 Version 2.0: Technology
    Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM*, June 2005
    (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.*
    (company history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^amat-10k]: Applied Materials, Inc., Form 10-K for fiscal 2003
    (platform descriptions: Centura, Endura, Endura SL, Producer).
    <https://www.sec.gov/Archives/edgar/data/6951/000089161804000093/f95058e10vk.htm>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^wiki-teos]: Wikipedia, *Tetraethyl orthosilicate*.
    <https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^sinha-1978]: A. K. Sinha, H. J. Levinstein, T. E. Smith, G. Quintana
    and S. E. Haszko, "Reactive Plasma Deposited Si-N Films for MOS-LSI
    Passivation", *Journal of The Electrochemical Society* **125**(4),
    601–608 (1978). <https://doi.org/10.1149/1.2131509>
[^lanford-1978]: W. A. Lanford and M. J. Rand, "The hydrogen content of
    plasma-deposited silicon nitride", *Journal of Applied Physics*
    **49**(4), 2473–2477 (1978). <https://doi.org/10.1063/1.325095>
[^claassen-1985]: W. A. P. Claassen, W. G. J. N. Valkenburg,
    M. F. C. Willemsen and W. M. v. d. Wijgert, "Influence of Deposition
    Temperature, Gas Pressure, Gas Phase Composition, and RF Frequency
    on Composition and Mechanical Stress of Plasma Silicon Nitride
    Layers", *Journal of The Electrochemical Society* **132**(4),
    893–898 (1985). <https://doi.org/10.1149/1.2113980>
[^adams-1981-pecvd]: A. C. Adams, F. B. Alexander, C. D. Capio and
    T. E. Smith, "Characterization of Plasma-Deposited Silicon
    Dioxide", *Journal of The Electrochemical Society* **128**(7),
    1545–1551 (1981). <https://doi.org/10.1149/1.2127680>
[^raupp-1992]: G. B. Raupp, T. S. Cale and H. P. W. Hey, "The role of
    oxygen excitation and loss in plasma-enhanced deposition of silicon
    dioxide from tetraethylorthosilicate", *Journal of Vacuum Science &
    Technology B* **10**(1), 37–45 (1992).
    <https://doi.org/10.1116/1.586361>
[^chapple-sokol-1989]: J. D. Chapple-Sokol, E. Tierney and J. Batey,
    "RF Power Dependence of the Material Properties of PECVD Silicon
    Dioxide", *MRS Proceedings* **165** (1989).
    <https://doi.org/10.1557/PROC-165-113>
[^mani-2007]: S. Mani and T. Saif, "Stress development in
    plasma-deposited silicon dioxide thin-films due to hydrogen
    evolution", *Thin Solid Films* **515**(5), 3120–3125 (2007).
    <https://doi.org/10.1016/j.tsf.2006.08.025>
[^yue-1985]: J. T. Yue, W. P. Funsten and R. V. Taylor, "Stress
    Induced Voids in Aluminum Interconnects During IC Processing",
    *23rd International Reliability Physics Symposium* (1985),
    pp. 126–137. <https://doi.org/10.1109/IRPS.1985.362087>
[^chaudhari-1974]: P. Chaudhari, "Hillock growth in thin films",
    *Journal of Applied Physics* **45**(10), 4339–4346 (1974).
    <https://doi.org/10.1063/1.1663054>
[^paulson-1974]: W. M. Paulson and R. W. Kirk, "The Effects of
    Phosphorus-Doped Passivation Glass on the Corrosion of Aluminum",
    *12th International Reliability Physics Symposium* (1974),
    pp. 172–179. <https://doi.org/10.1109/IRPS.1974.362644>
[^cheung-2000]: K. P. Cheung, "On the mechanism of plasma enhanced
    dielectric deposition charging damage", *Proc. 2000 5th
    International Symposium on Plasma Process-Induced Damage (P2ID)*,
    pp. 161–163. <https://doi.org/10.1109/PPID.2000.870658>
[^smith-1981]: R. T. Smith, J. D. Chlipala, J. F. M. Bindels,
    R. G. Nelson, F. H. Fischer and T. F. Mantz, "Laser programmable
    redundancy and yield improvement in a 64K DRAM", *IEEE Journal of
    Solid-State Circuits* **16**(5), 506–514 (1981).
    <https://doi.org/10.1109/JSSC.1981.1051630>
[^scarfone-1986]: L. M. Scarfone and J. D. Chlipala, "Computer
    simulation of target link explosion in laser programmable
    redundancy for silicon memory", *Journal of Materials Research*
    **1**(2), 368–381 (1986). <https://doi.org/10.1557/JMR.1986.0368>
[^pat-fuse-ibm]: P.-I. P. Lee, W. A. Klaasen and A. Mitwalsky
    (International Business Machines), *Fuse window with controlled fuse
    oxide thickness*, US 5,872,390 A, filed 1997-08-14, granted
    1999-02-16. <https://patents.google.com/patent/US5872390A/en>
[^pat-fuse-vanguard]: W.-T. Tzeng, Y.-F. Chen and K.-J. Wang (Vanguard
    International Semiconductor), *Process for controlling oxide
    thickness over a fusible link using transient etch stops*,
    US 6,294,474 B1, filed 1999-10-25, granted 2001-09-25.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6294474>
[^pat-fuse-tsmc]: C.-H. Yang and C.-M. Su (Taiwan Semiconductor
    Manufacturing Co.), *Method of forming a metal fuse on semiconductor
    devices*, US 6,835,642 B2, filed 2002-12-18, granted 2004-12-28.
    <https://patents.google.com/patent/US6835642B2/en>
[^pat-sealring-zeevo]: S. Bothra, T. G. McKay and R. Jhota (Zeevo),
    *Seal ring structure for IC containing integrated digital/RF/analog
    circuits and functions*, US 6,492,716 B1, filed 2001-04-30, granted
    2002-12-10. <https://patents.google.com/patent/US6492716B1/en>
