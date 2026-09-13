(step-170)=
# Step 170 — ALLY: Alloy

| | |
|---|---|
| **Step number** | 170 of 171[^steps-sheet] |
| **Step code** | `ALLY` |
| **Category** | {ref}`Anneal / thermal processing <category-anneal>` |
| **Phase** | BEOL — passivation, pads, alloy, test |
| **Previous step** | {ref}`PDME <step-169>` |
| **Next step** | {ref}`HPETEST <step-171>` |

## What this step is

`ALLY` is the last thermal step of the flow: after the pads have been
opened ({ref}`PDME <step-169>`), the finished wafers are, on our reading, annealed at low temperature in a
hydrogen-bearing ambient and then sent to electrical
test ({ref}`HPETEST <step-171>`). In the industry's vocabulary an
{term}`alloy anneal` (or "sinter") is a furnace anneal in
{term}`forming gas` at typically 350–450 °C[^txt-02] whose purposes are
to passivate the Si/SiO₂ interface traps with hydrogen, to repair
damage left by the plasma steps of the back end, and to sinter the
metal contacts and relieve stress in the interconnect (category
page[^txt-01][^wiki-fg]). SkyWater lists "H2 and forming gas alloy" among
the processes of its furnaces, which "are all made by Aviza",[^skw-01]
but does not say at which points of a flow the process is used. The
step list used in this reference does not give conditions; we read
`ALLY` as the conventional final forming-gas anneal (inference:
textbooks describe a final forming-gas anneal at the end of the process
as standard practice,[^txt-01][^txt-02] and SkyWater lists a furnace
alloy process[^skw-01]). The earlier
{ref}`ALLY1 <step-096>` is discussed on its own page.

What is unusual about this wafer compared with the one at
{ref}`ALLY1 <step-096>` is how much now lies between the ambient and
the transistors: five aluminium levels, tungsten plugs, the local
interconnect nitride, and a passivation of oxide and silicon nitride
("TOPOX" and "TOPNIT" on the PDK's stack diagram,[^pdk-04] 7000–9000 Å
of nitride in Cypress reports for other processes at the same
fab[^cyp-qtp-014807][^cyp-qtp-123907][^cyp-qtp-113005]) that is opened
only over the pads. Hydrogen from the
furnace ambient must reach the gate oxides through that stack, or be
supplied from within it: plasma nitride deposited at 330–350 °C contains
some 20–25 at.% hydrogen, as Lanford and Rand measured.[^lanford-1978]
Which source dominates in SKY130 is not public.

## Step category

`ALLY` is an {ref}`Anneal / thermal processing <category-anneal>` step
of the *alloy / forming-gas* type. As the category page sets out, the
alloy anneal comes last because later plasma exposure would undo the
passivation, and its temperature is capped by the aluminium
metallisation (Plummer, Deal and Griffin and Wolf and Tauber treat the
practice[^txt-01][^txt-02]). Its {term}`thermal budget` is
negligible for dopants and junctions. What it changes is hydrogen
bonding at interfaces and in the dielectrics, the microstructure and
stress of the aluminium lines and the interfaces between aluminium,
TiW and tungsten, and the stress of the passivation nitride. In the
sequence this reference describes it is the only anneal performed on a
wafer with open {term}`bond pads <bond pad>`.

## Why this step exists

The physics of a final forming-gas anneal is well documented; its
conditions in SKY130 are not public.

* **Interface-trap passivation.** Hydrogen ties up the dangling bonds
  at the Si/SiO₂ interface: Reed and Plummer set out the chemistry of
  interface-trap annealing,[^reed-1988] Cartier, Stathis and Buchanan
  the passivation and depassivation of dangling bonds by atomic
  hydrogen,[^cartier-1993] Brower the dissociation kinetics of the
  passivated defects[^brower-1990] and Stesmans the passivation of P_b0
  and P_b1 centres by molecular hydrogen.[^stesmans-1996] Deal's
  terminology names the charges involved.[^deal-1980] The interface-trap
  density affects threshold voltage, subthreshold slope and 1/f noise of
  every transistor the PDK models.
* **Repairing back-end plasma damage.** Every plasma step since the
  gates were formed — contact, via and metal etches, HDP and PECVD
  depositions, the passivation etches — can charge gate oxides through
  the interconnect; Fang and McVittie described the thin-oxide
  damage,[^fang-1992] and Rangan, Krishnan and Ashok showed that hydrogen
  (or deuterium) passivation repairs process-induced
  damage.[^rangan-1998] A final anneal after the last plasma step
  (the pad etch) treats all of it at once.
* **Hot-carrier reliability depends on it.** Lyding, Hess and Kizilyalli
  reported that "replacing hydrogen with deuterium during the final
  wafer sintering process greatly reduces hot electron degradation
  effects", with transistor lifetime improvements "by factors of
  10–50";[^lyding-1996] Kizilyalli et al. applied deuterium anneals to
  manufacturing multilevel metal/dielectric MOS
  systems,[^kizilyalli-1998] and the University of Illinois patent
  describes an example anneal "in an ambient of 10% deuterium in
  nitrogen for a period of about 1 hour" at "about 400° C".[^pat-deuterium-uiuc]
  The isotope effect shows how directly the final sinter's hydrogen sets
  the Si–H bonds at the interface. Whether SKY130 uses hydrogen or
  deuterium is not public; SkyWater lists hydrogen and forming
  gas.[^skw-01]
* **Contacts and interconnect.** The same anneal lowers and stabilises
  contact and via resistance and relaxes the as-deposited stress of the
  aluminium (industry practice;[^txt-02] Learn reviewed the aluminium
  metallisation of the preceding decades[^learn-1976]). It also has
  costs: thermal cycling of
  aluminium under a stiff passivation drives
  {term}`stress-induced voiding` (Yue,
  Funsten and Taylor[^yue-1985]), and PECVD nitride shows an
  irreversible tensile stress change on heating (Hughey and
  Cook[^hughey-2003]).
* **Side-effects that bound the recipe.** Hydrogen can deactivate boron
  acceptors in silicon (Sah, Sun and Tzou;[^sah-1983] Pankove et
  al.[^pankove-1983]) and a hydrogen anneal affects the retention of
  nitride charge-trapping memories (Maes, Usmani and Heyns[^maes-1981]),
  relevant to the {term}`SONOS` cells of {ref}`ONO <step-040>`.

Without `ALLY`, on this reading, the transistors would be tested with
the interface-trap density and plasma damage left by the back end, and
the {ref}`HPETEST <step-171>` parameters would not represent the product.

## How it is typically performed

An industry-generic final alloy anneal for a 200 mm, 130 nm-era fab with
an aluminium back end (SKY130's recipe is not public):

* **Tool and ambient.** Vertical batch furnace with a forming-gas
  supply — "typical forming gas formulations (5% H2 in N2)"[^wiki-fg] —
  or hydrogen diluted at the tool; SkyWater lists "H2 and forming gas
  alloy" on its Aviza furnaces.[^skw-01] The tube is purged of oxygen
  before hydrogen is admitted, so that the exposed aluminium pads are not
  oxidised further (inference).
* **Temperature and time.** 350–450 °C for tens of minutes (typical
  industry values;[^txt-02] category page), below the temperatures at
  which aluminium {term}`hillocks <hillock>` and voids grow rapidly and far below the
  Al–Si eutectic; the University of Illinois example of about 400 °C for
  about 1 hour is of this kind.[^pat-deuterium-uiuc]
* **Sequence.** Load; nitrogen purge; ramp; hydrogen-bearing gas at
  temperature; soak; purge; controlled ramp-down to limit thermal-stress
  cycling of the metal; unload.
* **Single-wafer alternative.** A forming-gas anneal in an RTP chamber
  is possible but uncommon for the final sinter; SkyWater's Heatpulse
  8808 lists "NH3, Ar, N2, O2" but not H₂ or forming gas,[^skw-01] which argues
  for the furnace here (inference).
* **Metrology.** Monitor MOS capacitors for interface-trap density
  (charge pumping or C–V); the transistor, contact-chain and sheet
  resistance parameters measured at {ref}`HPETEST <step-171>`; pad
  appearance.

## Machines typically used

* **Vertical furnace** with forming-gas or hydrogen capability:
  Aviza/SVG/Thermco AVP,[^aviza-avp] ASM A400,[^asm-vf] TEL Alpha-8,
  Kokusai Vertron ({ref}`category-anneal`).
* **Horizontal furnace** (older alloy tubes); **RTP** as the
  single-wafer alternative.
* **C–V / charge-pumping test set** for interface-trap monitors.

## Machines likely used at SkyWater

* **Aviza furnaces, "H2 and forming gas alloy".** SkyWater states that
  "Furnaces are all made by Aviza" and lists "H2 and forming gas alloy"
  among the furnace processes.[^skw-01] Strength: **strong** for the
  existence of a furnace alloy process; the assignment to `ALLY` is an
  **inference** — it is the only anneal listed with H₂ or forming gas
  (the furnaces' "H2 and forming gas alloy").
  Dealer documentation describes the Aviza/SVG AVP-8000 as a vertical
  batch furnace for 150–200 mm wafers.[^aviza-avp]
* **AG Associates Heatpulse 8808** — no H₂ or forming gas among its
  listed gases ("NH3, Ar, N2, O2");[^skw-01]
  weak.

## Resources required

* **Forming gas** (H₂ in N₂; "5% H2 in N2" is the typical formulation
  Wikipedia gives[^wiki-fg]) or **hydrogen** and **nitrogen** supplied
  separately; gas suppliers named by SkyWater's filings.[^sec-01]
* **Quartz tube, boats and baffles**; a hydrogen-rated gas panel with
  leak detection and purge interlocks.
* **Monitor wafers** (SEMI M8 class)[^semi-m8] with MOS capacitors.

## Related steps and cross-references

* Previous: {ref}`PDME <step-169>` (the last plasma step, which opens the
  pads). Next: {ref}`HPETEST <step-171>` (electrical test).
* An earlier anneal: {ref}`ALLY1 <step-096>`.
* The hydrogen-rich passivation nitride over the wafer:
  {ref}`NTSD <step-167>`; the oxide beneath it: {ref}`NFUSOX <step-164>`.
* The memory cells whose nitride hydrogen can affect:
  {ref}`ONO <step-040>`.
* Category page: {ref}`Anneal / thermal processing <category-anneal>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — "Furnaces are all made by
  Aviza"; "H2 and forming gas alloy"; Heatpulse 8808 ambients.[^skw-01]
* SkyWater PDK, *Process stack diagram* — TOPOX and TOPNIT over metal 5.[^pdk-04]
* Cypress, QTP 014807, QTP 123907/132302/132301, QTP 113005 — passivation
  nitride thicknesses at Fab 4.[^cyp-qtp-014807][^cyp-qtp-123907][^cyp-qtp-113005]
* Moov, *Aviza / SVG / Thermco AVP 8000* listing; ASM International,
  *Vertical furnace*.[^aviza-avp][^asm-vf]
* SkyWater, Form S-1 — gas suppliers.[^sec-01]

### High-level understanding

* Wikipedia, *Forming gas*.[^wiki-fg]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — the alloy
  anneal and interface passivation.[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  sinter/alloy practice.[^txt-02]
* Deal, *IEEE TED* 1980 — standard terminology for oxide
  charges.[^deal-1980]

### Deep dive

* Reed and Plummer, *J. Appl. Phys.* 1988 — chemistry of Si–SiO₂
  interface-trap annealing.[^reed-1988]
* Cartier, Stathis and Buchanan, *Appl. Phys. Lett.* 1993 — passivation
  and depassivation of dangling bonds by atomic hydrogen.[^cartier-1993]
* Brower, *Phys. Rev. B* 1990 — dissociation kinetics of
  hydrogen-passivated interface defects.[^brower-1990]
* Stesmans, *Appl. Phys. Lett.* 1996 — passivation of P_b0 and P_b1
  centres by molecular hydrogen.[^stesmans-1996]
* Lyding, Hess and Kizilyalli, *Appl. Phys. Lett.* 1996 — deuterium in
  the final sinter and hot-electron degradation.[^lyding-1996]
* Kizilyalli et al., *IEEE EDL* 1998 — deuterium anneals for
  manufacturing multilevel metal/dielectric MOS systems.[^kizilyalli-1998]
* Lyding and Hess (University of Illinois), US 5,872,387 —
  deuterium-treated devices and example anneal conditions.[^pat-deuterium-uiuc]
* Rangan, Krishnan and Ashok, P2ID 1998, and Fang and McVittie, *IEEE
  EDL* 1992 — plasma damage and its hydrogen passivation.[^rangan-1998][^fang-1992]
* Lanford and Rand, *J. Appl. Phys.* 1978 — hydrogen content of plasma
  nitride, a source within the stack.[^lanford-1978]
* Sah, Sun and Tzou, *Appl. Phys. Lett.* 1983, and Pankove et al., *Phys.
  Rev. Lett.* 1983 — hydrogen deactivation of boron.[^sah-1983][^pankove-1983]
* Maes, Usmani and Heyns, *J. Appl. Phys.* 1981 — hydrogen anneals and
  nitride-memory retention.[^maes-1981]
* Learn, *J. Electrochem. Soc.* 1976 — aluminium metallisation and its
  processing.[^learn-1976]
* Yue, Funsten and Taylor, IRPS 1985, and Hughey and Cook, MRS 2003 —
  stress voiding in aluminium and nitride stress change on
  heating.[^yue-1985][^hughey-2003]

## Open questions

* The ambient (forming gas, hydrogen, or deuterium), temperature and time
  of the final anneal are not public.
* Whether hydrogen reaches the gate oxides from the furnace ambient
  through the openings and the passivation, or mainly from the
  hydrogen-rich passivation nitride, is not public.
* Whether the anneal is a batch furnace process or single-wafer is not
  public; the furnace reading rests on SkyWater's "H2 and forming gas
  alloy" entry.[^skw-01]
* How the SONOS cells' retention and programming window are protected
  against the hydrogen of this anneal is not public.

<!-- footnotes -->

[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
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
[^aviza-avp]: Moov used-equipment marketplace, *Aviza / SVG / Thermco
    AVP 8000* listing, accessed 2026-08-30.
    <https://moov.co/marketplace/furnaces-diffusion/aviza-svg/aviza-asml-svg-watkinsjohnson-avp-8000>
[^asm-vf]: ASM International, *Vertical furnace*, product page.
    <https://www.asm.com/our-technology-products/vertical-furnace>
[^wiki-fg]: Wikipedia, *Forming gas*.
    <https://en.wikipedia.org/wiki/Forming_gas>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^deal-1980]: B. E. Deal, "Standardized terminology for oxide charges
    associated with thermally oxidized silicon", *IEEE Transactions on
    Electron Devices* **27**(3), 606–608 (1980),
    DOI 10.1109/T-ED.1980.19908; published simultaneously in *Journal of
    The Electrochemical Society* **127**(4), 979–981 (1980).
    <https://doi.org/10.1109/T-ED.1980.19908>,
    <https://doi.org/10.1149/1.2129800>
[^reed-1988]: M. L. Reed and J. D. Plummer, "Chemistry of Si-SiO₂
    interface trap annealing", *Journal of Applied Physics* **63**(12),
    5776–5793 (1988). <https://doi.org/10.1063/1.340317>
[^cartier-1993]: E. Cartier, J. H. Stathis and D. A. Buchanan,
    "Passivation and depassivation of silicon dangling bonds at the
    Si/SiO₂ interface by atomic hydrogen", *Applied Physics Letters*
    **63**(11), 1510–1512 (1993). <https://doi.org/10.1063/1.110758>
[^brower-1990]: K. L. Brower, "Dissociation kinetics of
    hydrogen-passivated (111) Si-SiO₂ interface defects", *Physical
    Review B* **42**(6), 3444–3453 (1990).
    <https://doi.org/10.1103/PhysRevB.42.3444>
[^stesmans-1996]: A. Stesmans, "Passivation of P_b0 and P_b1 interface
    defects in thermal (100) Si/SiO₂ with molecular hydrogen", *Applied
    Physics Letters* **68**(15), 2076–2078 (1996).
    <https://doi.org/10.1063/1.116308>
[^fang-1992]: S. Fang and J. P. McVittie, "Thin-oxide damage from gate
    charging during plasma processing", *IEEE Electron Device Letters*
    **13**(5), 288–290 (1992). <https://doi.org/10.1109/55.145056>
[^rangan-1998]: S. Rangan, S. Krishnan and S. Ashok, "Process-induced
    damage — a study of hydrogen and deuterium passivation", *Proc.
    1998 3rd International Symposium on Plasma Process-Induced Damage*,
    pp. 213–216. <https://doi.org/10.1109/PPID.1998.725612>
[^lyding-1996]: J. W. Lyding, K. Hess and I. C. Kizilyalli, "Reduction of
    hot electron degradation in metal oxide semiconductor transistors by
    deuterium processing", *Applied Physics Letters* **68**(18),
    2526–2528 (1996). <https://doi.org/10.1063/1.116172>
[^kizilyalli-1998]: I. C. Kizilyalli, G. C. Abeln, Z. Chen, J. Lee,
    G. Weber, B. Kotzias, S. Chetlur, J. W. Lyding and K. Hess,
    "Improvement of hot carrier reliability with deuterium anneals for
    manufacturing multilevel metal/dielectric MOS systems", *IEEE
    Electron Device Letters* **19**(11), 444–446 (1998).
    <https://doi.org/10.1109/55.728907>
[^pat-deuterium-uiuc]: J. W. Lyding and K. Hess (Board of Trustees of the
    University of Illinois), *Deuterium-treated semiconductor devices*,
    US 5,872,387 A, filed 1996-01-16, granted 1999-02-16.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5872387>
[^lanford-1978]: W. A. Lanford and M. J. Rand, "The hydrogen content of
    plasma-deposited silicon nitride", *Journal of Applied Physics*
    **49**(4), 2473–2477 (1978). <https://doi.org/10.1063/1.325095>
[^sah-1983]: C.-T. Sah, J. Y.-C. Sun and J. J.-T. Tzou, "Deactivation
    of the boron acceptor in silicon by hydrogen", *Applied Physics
    Letters* **43**(2), 204–206 (1983). <https://doi.org/10.1063/1.94287>
[^pankove-1983]: J. I. Pankove, D. E. Carlson, J. E. Berkeyheiser and
    R. O. Wance, "Neutralization of Shallow Acceptor Levels in Silicon
    by Atomic Hydrogen", *Physical Review Letters* **51**(24),
    2224–2225 (1983). <https://doi.org/10.1103/PhysRevLett.51.2224>
[^maes-1981]: H. E. Maes, S. H. Usmani and G. L. Heyns, "Effects of a
    high-temperature hydrogen anneal on the memory retention of
    metal-nitride-oxide-silicon transistors at elevated temperatures",
    *Journal of Applied Physics* **52**(6), 4348–4350 (1981).
    <https://doi.org/10.1063/1.329266>
[^learn-1976]: A. J. Learn, "Evolution and Current Status of Aluminum
    Metallization", *Journal of The Electrochemical Society* **123**(6),
    894–906 (1976). <https://doi.org/10.1149/1.2132964>
[^yue-1985]: J. T. Yue, W. P. Funsten and R. V. Taylor, "Stress
    Induced Voids in Aluminum Interconnects During IC Processing",
    *23rd International Reliability Physics Symposium* (1985),
    pp. 126–137. <https://doi.org/10.1109/IRPS.1985.362087>
[^hughey-2003]: M. P. Hughey and R. F. Cook, "Irreversible Tensile
    Stress Development in PECVD Silicon Nitride Films", *MRS
    Proceedings* **795** (2003). <https://doi.org/10.1557/PROC-795-U1.6>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
