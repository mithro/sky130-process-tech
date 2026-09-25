(material-precursors)=
# Precursors

Precursors are the gases and vapours whose atoms become a deposited
film: silane, dichlorosilane, TEOS and BTBAS for silicon, oxide and
nitride; ammonia for the nitrogen of nitride and oxynitride; silicon
tetrafluoride for fluorinated oxide; ozone as an oxidant for TEOS; and
tungsten hexafluoride for the tungsten plugs. They are reactive by
design, and several are pyrophoric, toxic or corrosive. This page
describes the class in general, lists representative precursors and the
standards they are specified to, and then says what SkyWater has
published about the films and precursors at its fab and which SKY130
steps name them. The deposition chemistry is on the
{ref}`deposition category page <category-deposition>`, and the tools on
the {ref}`LPCVD furnace <machine-vertical-furnace-lpcvd>`,
{ref}`PECVD <machine-pecvd>`, {ref}`HDP-CVD <machine-hdp-cvd>` and
{ref}`tungsten CVD <machine-tungsten-cvd>` pages.

| | Precursors |
|---|---|
| What they do | Supply the silicon, nitrogen or tungsten of a film; above 420 °C "silane decomposes into silicon and hydrogen; it can therefore be used in the chemical vapor deposition of silicon".[^wiki-silane] |
| Precursors in the SKY130 steps | Silane, dichlorosilane, TEOS, BTBAS, ammonia, SiF₄, ozone, WF₆ with silane or diborane nucleation (step-page readings). |
| Grades | SEMI C3.55 (bulk silane), C3.12 (ammonia) and C70 (tungsten hexafluoride).[^semi-c3-55][^semi-c3-12][^semi-c70] |
| Delivery | Gases in cylinders or bulk; liquids (TEOS, BTBAS) vaporised at the tool; ozone generated at the tool, since "Ozone is produced in the corona discharge"[^wiki-ozone] (industry practice). |
| Hazards | Silane is "a pyrophoric gas (capable of autoignition at temperatures below 54 °C or 129 °F)";[^wiki-silane] WF₆ is "a toxic, corrosive, colorless gas";[^wiki-wf6] NIOSH gives ammonia an IDLH of "300 ppm".[^niosh-nh3] |
| SkyWater evidence | "PECVD TEOS, C2 and Producer"; "PECVD silane oxide/nitride/oxynitride, C1"; "LPCVD nitride, with NH3 and also DH3"; "LPCVD BTBAS low temp nitride"; "Lam/Novellus PECVD Tungsten";[^skw-01] "high-purity compressed gases"[^sec-01][^sec-02] |
| SKY130 steps | 34 steps; see {ref}`SKY130 steps that use this class <material-precursors-steps>` |

## What the class is and what it does

A chemical vapour deposition ({term}`CVD`) process brings a precursor
to a heated or plasma-activated surface, where it decomposes or reacts
and leaves a solid film; the rest leaves as by-product gas. The precursor
sets the temperature a film can be grown at, what the film contains
besides the wanted elements (hydrogen, carbon, chlorine, fluorine), how
conformally it coats a step, and what the exhaust must handle
({ref}`category-deposition`). Utilisation is often low: "The
plasma-enhanced chemical vapor deposition (PECVD) process is relatively
inefficient at materials utilization with approximately 85% of the silane
being wasted".[^wiki-silane]

### Silane and dichlorosilane

Silane "has one dominant application, as a precursor to elemental
silicon, particularly in the semiconductor industry".[^wiki-silane] In a
furnace it gives amorphous or polycrystalline silicon, whose structure
Kamins related to deposition temperature;[^kamins-1980] with oxygen or
N₂O it gives oxide in HDP and PECVD
tools,[^adams-1981-pecvd][^nguyen-1999] and with ammonia it gives
nitride: Denisse et al. covered "the entire range of compositions from
silicon oxide to silicon nitride" from SiH₄, N₂O and
NH₃.[^denisse-1986]

Its hazard is ignition: silane
"undergoes spontaneous combustion in air, without the need for external
ignition",[^wiki-silane] and Britton's paper on "the unusual combustion
hazards of silane and its chlorides" gives "new experimental data
presented showing the effects of sudden releases into free
air".[^britton-1990]

Dichlorosilane is the chlorinated relative used for
furnace nitride: "In its major use, it is mixed with ammonia (NH3) in
LPCVD chambers to grow silicon nitride in semiconductor
processing".[^wiki-dcs] Roenigk and Jensen modelled that growth in a hot-wall
tube and explained its non-uniformities by "diffusion‐limited film growth
from highly reactive gas‐phase intermediates".[^roenigk-1987] Its
by-product ammonium chloride is "a solid condensate at temperatures below
about 125° C.",[^pat-nh4cl-vlsi] which is why nitride furnaces carry
heated exhaust lines and traps (industry practice).

### Ammonia

Ammonia is the nitrogen source of LPCVD, BTBAS and PECVD nitride and, with
N₂O, of PECVD oxynitride, whose growth and composition Denisse et al.
studied.[^denisse-1986] It also nitrides oxide in an RTA tool and
appears as an asher gas. Ammonia "is regulated in the US as a
non-flammable gas, but it meets the definition of a material that is
toxic by inhalation";[^wiki-ammonia] NIOSH gives an IDLH of "300 ppm" and
a REL of "TWA 25 ppm (18 mg/m3) ST 35 ppm (27 mg/m3)".[^niosh-nh3]

### TEOS and ozone

Tetraethyl orthosilicate is a liquid used "as a precursor to silicon
dioxide in the semiconductor industry", and "At elevated temperatures
(>600 °C), TEOS converts to silicon dioxide";[^wiki-teos] Becker et al.
deposited LPCVD TEOS oxide "at temperatures between 650 and 800
°C".[^becker-1987] In a PECVD chamber the plasma lowers the temperature,
and TEOS oxide conforms to steps better than silane oxide
({ref}`category-deposition`).

Ozone oxidises TEOS without a plasma: Fujino
et al. found that "step coverage of the films changed from isotropic to
flow shape with ozone concentration increase",[^fujino-1990] and later
added "trimethylphosphate for PSG films".[^fujino-1991] Kwok et al.
found ozone–TEOS growth sensitive to the surface beneath
it.[^kwok-1994] Ozone "is among the most powerful oxidising agents known,
far stronger than O2"; "Ozone is produced in the corona
discharge".[^wiki-ozone]

### BTBAS

Bis(tertiary-butylamino)silane is a liquid aminosilane for
low-temperature nitride. Gumpher et al. deposited "silicon nitride from
bis(tertiary-butylamino)silane (BTBAS) and ammonia precursors" at
"550-600°C in a 200 mm vertical batch furnace", and found "Substantial
carbon and hydrogen incorporation" relative to dichlorosilane
nitride.[^gumpher-2004] It avoids the chlorine and ammonium chloride of
the dichlorosilane route (our comparison of the two chemistries).

### Silicon tetrafluoride

SiF₄ puts fluorine into an oxide to lower its permittivity. Denison,
Barbour and Burkhart grew fluorine-doped oxide "from a mixture of SiH4 and
SiF4, O2, and Ar" in a high-density plasma, and found that "The
dielectric constant decreased linearly from 4.0 at zero F to 3.55 at 10.5
at. % F".[^denison-1996] Wikipedia notes that the gas "finds limited use
in microelectronics" and classes it as "toxic, corrosive".[^wiki-sif4]

### Tungsten hexafluoride

"The dominant application of tungsten fluoride is in the semiconductor
industry, where it is widely used for depositing tungsten metal in a
chemical vapor deposition (CVD) process", and "The decomposition is
usually facilitated by mixing WF6 with hydrogen, silane, germane,
diborane, phosphine, and related hydrogen-containing gases".[^wiki-wf6]
McConica and Krishnamani found that without hydrogen "the silicon
reduction results in a 10–40 nm self‐limiting tungsten deposit", and that
the hydrogen reduction "is one‐half order in hydrogen, zero order in
tungsten hexafluoride".[^mcconica-1986] Kleijn et al. modelled transport
in a single-wafer reactor.[^kleijn-1991] The by-product is a hazard: "HF
vapor is very aggressive and etches away most materials".[^wiki-wf6]

Nucleation layers may use diborane, "a highly toxic, colorless, and
pyrophoric gas",[^wiki-diborane] which NIOSH notes is "Usually shipped in
pressurized cylinders diluted with hydrogen, argon, nitrogen, or
helium";[^niosh-diborane] Novellus's pulsed nucleation patent forms the
nucleation film "by alternatively providing to that surface, reducing
gases and tungsten containing gases".[^pat-pnl-novellus]

## Representative materials and grades

Precursors are specified by SEMI and sold by specialty-gas and
electronic-chemical suppliers; liquids are shipped in stainless-steel
ampoules or bulk canisters and vaporised by bubblers or liquid-injection
systems at the tool (industry practice). The statements below describe
standards and general properties, not what SkyWater buys; SKY130's
precursor grades and flows are not public.

:::{table} Representative precursors and grades, as public and current supplier documents describe them
:widths: 20 12 68

| Material | As supplied | Specification |
|---|---|---|
| Silane | — | SEMI C3.55 provides "specifications for silane (SiH4)" and covers "requirements for bulk silane (SiH4) used in the semiconductor industry";[^semi-c3-55] silane is "slightly toxic", with an LC50 for rats of "0.96% (9,600 ppm) over a 4-hour exposure"[^wiki-silane] |
| Dichlorosilane | — | "Dichlorosilane must be ultrapurified and concentrated in order to be used for the manufacturing of semiconducting epitaxial silicon layers"; it "is also very toxic"[^wiki-dcs] |
| Ammonia | — | SEMI C3.12 is a "specification for ammonia (NH3) that is used in the semiconductor industry", first published in 1983 and reapproved in 2022 as C3.12-0116 (Reapproved 0922)[^semi-c3-12] |
| TEOS | — | A liquid precursor to silicon dioxide[^wiki-teos] |
| BTBAS | — | A liquid aminosilane for 550–600 °C LPCVD nitride[^gumpher-2004] |
| Silicon tetrafluoride | — | A "toxic, corrosive" gas[^wiki-sif4] |
| Tungsten hexafluoride | — | SEMI C70 provides "specifications for tungsten hexafluoride (WF6) that are used in the semiconductor industry" (revision C70-0924);[^semi-c70] the gas is "roughly 11 times heavier than air"[^wiki-wf6] |
| Ozone | — | Generated at the tool from oxygen by corona discharge;[^wiki-ozone] Applied's SACVD chamber used "TEOS (tetraethylorthosilicate) and ozone"[^amat-sacvd-2000] |
| Diborane | — | Diluted in hydrogen, argon, nitrogen or helium[^niosh-diborane] |
:::

## At SkyWater

### What SkyWater's filings and pages list

SkyWater's *Facilities & Capabilities* page names deposition processes,
not precursors. Under "Film Deposition":[^skw-01]

> "Lam/Novellus/AMAT" · "PECVD TEOS, C2 and Producer" · "– low temp
> options" · "PECVD silane oxide/nitride/oxynitride, C1" · "– low temp,
> range of R.I. options" · "PECVD nitride C1" · "– high R.I., low temp
> options"
>
> "Lam/Novellus High Density Plasma (HDP) doped and phos doped with
> sputter etch" · "– high aspect (5:1) fill capability"
>
> "Lam/Novellus PECVD Tungsten" · "– plug fill" · "– PNL option for high
> aspect ratio (up to 10:1)"

and under "Furnaces/Diffusion/Pre-Clean":[^skw-01]

> "LPCVD nitride, with NH3 and also DH3" · "LPCVD polysilicon (undoped),
> both amorphous and crystalline" · "LPCVD silane oxide" · "LPCVD
> oxide/nitride/oxide" · "LPCVD BTBAS low temp nitride"

The RTA entry lists "NH3" and the Iridia asher entry "NH3"; the page also
lists atomic layer deposition of "Metals: AIN, TiN" and "Oxides: SiO2,
Al2O3, HfO2, TiO2, ZrO2".[^skw-01] Read term by term, the page names
TEOS, silane, ammonia and BTBAS; it does not name dichlorosilane (it does
not expand "DH3"), SiF₄, ozone, diborane or tungsten hexafluoride, and
its "PECVD Tungsten" wording is read on the step pages as a label for the
tungsten CVD tool.[^skw-01] The filings describe "high-purity compressed
gases" and name gas suppliers, as quoted on the
{ref}`process gases <material-process-gases>` page, without naming any
precursor.[^sec-01][^sec-02]

For the films, SkyWater's S-1 states that "our fab was owned and operated
by Cypress Semiconductor Corporation, or Cypress, as a captive
manufacturing facility for 20 years",[^sec-01] and Cypress's 2017
release on its sale describes "its semiconductor wafer fabrication
facility in Bloomington, Minnesota" and calls it "Fab 4 in
Minnesota";[^cyp-01] a 2005 Cypress report for a "Fab4" product gives its
passivation as "1000Å TEOS / 9000Å PECVD Nitride".[^cyp-qtp-014807]

### Strength of the evidence

The film and process entries are SkyWater statements and rank as
**strong** evidence, on the scale of the
{ref}`machines index <machines-reading-evidence>`, that TEOS, silane,
ammonia and BTBAS chemistries run at the fab, and that tungsten plugs are
filled; they tie no precursor to a step and describe the fab in the
2020s.[^skw-01]

That the tungsten fill uses WF₆, that the furnace nitride
uses dichlorosilane, and that SiF₄ and ozone are available, are
industry practice that the step pages supply, not SkyWater statements.
The Cypress report is strong for the passivation of one product in 2005
and does not show SKY130's films.[^cyp-qtp-014807]

(material-precursors-steps)=
### SKY130 steps that use this class

This page covers the rows of the {ref}`materials index <materials-table>`
listed below by key; the steps are those whose *Resources required* section
names one of them (the union of the rows' *Steps* cells). The oxygen,
N₂O, argon and helium that accompany the precursors belong to the
{ref}`process gases <material-process-gases>` page, and the phosphorus
sources of PSG to the {ref}`dopant sources <material-dopant-sources>`
page.

Materials index rows covered:

* `nh3` — ammonia
* `sih4` — silane
* `dcs` — dichlorosilane
* `teos` — TEOS
* `btbas` — BTBAS
* `sif4` — silicon tetrafluoride
* `wf6` — tungsten hexafluoride with silane or diborane nucleation
* `ozone` — ozone for TEOS oxide deposition

<!-- step-tables:begin (generated by tools/gen_step_tables.py; do not edit) -->
:::{dropdown} All 34 steps as one line of links (checked against the index)

Steps:

{ref}`ISONIT <step-003>`, {ref}`LINOX <step-010>`, {ref}`FILOX <step-011>`, {ref}`ONO <step-040>`, {ref}`LVGOX <step-047>`, {ref}`SAGD <step-048>`, {ref}`PRIS <step-054>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`SPNIT <step-076>`, {ref}`SPOX <step-080>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`, {ref}`WDEP <step-099>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`WDEP2 <step-110>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`WDEP3 <step-121>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`WDEP4 <step-132>`, {ref}`CAPILD <step-135>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`WDEP5 <step-147>`, {ref}`CAPILD2 <step-150>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`NFUSOX <step-164>`, {ref}`NTSD <step-167>`
:::
<!-- step-tables:end -->

The steps fall into groups, as the index rows describe them:

* **Furnace films.** Dichlorosilane and ammonia for the isolation, ONO and
  (on one reading) gate-cap and spacer nitrides at
  {ref}`ISONIT <step-003>`, {ref}`ONO <step-040>`,
  {ref}`GATENIT <step-058>` and {ref}`SPNIT <step-076>`; silane for the
  gate silicon at {ref}`SAGD <step-048>`; BTBAS as the low-temperature
  option at {ref}`SPNIT <step-076>` and {ref}`LINIT <step-104>`.
* **Plasma dielectrics.**
  * Silane for the HDP fills
    ({ref}`FILOX <step-011>`, {ref}`PSG <step-089>`,
    {ref}`NILD2 <step-105>` to {ref}`NILD6 <step-156>`), with SiF₄ as the
    fluorinated option at {ref}`NILD3 <step-115>` and
    {ref}`NILD4 <step-126>`.
  * TEOS or silane for the cap oxides, spacer
    oxide and fuse oxide.
  * Silane and ammonia for the nitrides and the
    capacitor oxynitride at {ref}`CAPILD <step-135>`,
    {ref}`CAPILD2 <step-150>` and {ref}`NTSD <step-167>`.
  * Ozone only for
    the TEOS route of {ref}`PSG <step-089>`.
* **Tungsten.** WF₆ with silane or diborane nucleation at the five
  tungsten fills.
* **Ammonia outside deposition.** As a nitriding option at
  {ref}`LINOX <step-010>` and {ref}`LVGOX <step-047>`, and as a possible
  ash gas at {ref}`PRIS <step-054>`, {ref}`PDIS <step-084>` and
  {ref}`NSDIS <step-087>`, where SkyWater lists NH3 on the Iridia
  asher.[^skw-01]

## Supply, handling, safety and facilities

None of the SkyWater sources cited here describes the fab's gas cabinets,
liquid delivery, exhaust or abatement; the points below are industry
practice, standards and safety data.

* **Pyrophoric gases.** Silane ignites in air;[^wiki-silane] Britton
  measured what happens when it is released suddenly,[^britton-1990] and
  diborane is also pyrophoric.[^wiki-diborane] Such gases are held in
  ventilated gas cabinets, which Wikipedia describes as storage "for
  protection from external fire or from any leak".[^wiki-industrial-gas]
* **Toxic and corrosive gases.** Ammonia's NIOSH IDLH is "300
  ppm";[^niosh-nh3] diborane's is "15 ppm";[^niosh-diborane] WF₆
  "gives HF on contact with water",[^wiki-wf6] and SiF₄ is corrosive and "fatal if
  inhaled".[^wiki-sif4]
* **By-products and exhaust.** Dichlorosilane nitride furnaces make
  ammonium chloride, which condenses below about 125 °C, and trap
  efficiency "is therefore an important factor in the successful
  deposition of silicon nitride films";[^pat-nh4cl-vlsi][^pat-nh4cl-tsmc]
  tungsten CVD exhausts HF.[^wiki-wf6]
* **Ozone.** Ozone damages respiratory tissue "above concentrations of
  about 0.1 ppm";[^wiki-ozone] unused ozone is destroyed at the tool
  exhaust (industry practice), and catalytic decomposition, over
  materials such as "manganese dioxide", is the most widely used
  method.[^wiki-ozone]
* **Chamber cleaning.** Deposition on chamber walls is removed with
  fluorine chemistries, the subject of the
  {ref}`etch and chamber-clean gases <material-etch-gases>` page
  ({ref}`machine-pecvd`).

## Process-integration notes for SKY130

These notes connect the class to the step pages; they add no SKY130
conditions of their own. SKY130's precursors and deposition recipes are
not public.

* **"DH3".** SkyWater's LPCVD nitride entry reads "with NH3 and also
  DH3"; the step pages describe dichlorosilane nitride but do not read
  "DH3" as dichlorosilane, and the
  {ref}`materials index <materials-open-questions>` keeps it
  open.[^skw-01]
* **Thermal budget and the spacer.** The {ref}`SPNIT <step-076>` page
  weighs a dichlorosilane furnace nitride against BTBAS and PECVD
  routes after the tip implants; BTBAS lowers the deposition temperature
  to 550–600 °C at the cost of carbon and hydrogen in the
  film,[^gumpher-2004] and SkyWater lists "LPCVD BTBAS low temp
  nitride".[^skw-01]
* **Silane or TEOS for cap oxides.** The cap-oxide pages offer TEOS with
  oxygen or silane with N₂O; SkyWater lists both "PECVD TEOS" and "PECVD
  silane oxide" entries,[^skw-01] and the Cypress report names TEOS for a
  passivation oxide at the fab.[^cyp-qtp-014807]
* **Fluorinated oxide.** SiF₄ at {ref}`NILD3 <step-115>` and
  {ref}`NILD4 <step-126>` rests on the PDK's "_C" dielectric labels, not
  on a SkyWater entry (see the
  {ref}`materials index <materials-open-questions>`); Denison et al. show
  the permittivity fluorine buys.[^denison-1996]
* **Tungsten nucleation.** The WDEP pages read a silane or diborane
  nucleation followed by hydrogen reduction, and we read SkyWater's "PNL option" as the pulsed nucleation layer that
  Novellus patented, formed "by alternatively providing to that surface,
  reducing gases and tungsten containing gases".[^skw-01][^pat-pnl-novellus]
  Silicon reduction of WF₆ is self-limiting,[^mcconica-1986] and the TiN
  liner protects the silicon and oxide beneath
  ({ref}`category-deposition`).
* **Ozone only as an option.** The {ref}`PSG <step-089>` page reads HDP
  PSG from silane as the likely route and names ozone–TEOS only as the
  alternative, following SkyWater's "phos doped" HDP entry.[^skw-01]

## Related pages

* **Category.** {ref}`category-deposition` — CVD chemistry, films and
  chamber cleaning.
* **Machines.** {ref}`machine-vertical-furnace-lpcvd`, {ref}`machine-pecvd`,
  {ref}`machine-hdp-cvd` and {ref}`machine-tungsten-cvd` — the tools that
  consume these precursors. {ref}`machine-rapid-thermal-processor` —
  ammonia nitridation.
* **Materials.** {ref}`material-process-gases` and
  {ref}`material-dopant-sources` — the oxidants, carriers and phosphorus
  sources used with the precursors. {ref}`material-etch-gases` — the
  NF₃ and fluorocarbon chamber cleans.
* **Indexes.** {ref}`materials-index` — all consumable classes and the
  films table.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

* {ref}`Thermal trap for gaseous materials <patent-gp25448458>` — US 5,303,558 A (1992)
* {ref}`Method for producing ultra-thin tungsten layers with improved step coverage <patent-gp46204269>` — US 6,635,965 B1 (2001)
* {ref}`Cold trap for CVD furnace <patent-gp32068901>` — US 2004/0069224 A1 (2002)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater Technology, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the film deposition,
  furnace, RTA and asher entries.[^skw-01]
* SkyWater Technology, Form S-1 (2021) and Form 10-K for fiscal 2023 —
  compressed gases, gas suppliers and the fab's Cypress
  history.[^sec-01][^sec-02]
* [Cypress Semiconductor, *Cypress Closes Sale of Minnesota Wafer
  Fabrication Facility* (2017)](<https://www.prnewswire.com/news-releases/cypress-closes-sale-of-minnesota-wafer-fabrication-facility-300416287.html>) — the Bloomington fab as Fab 4.[^cyp-01]
* [Cypress Semiconductor, QTP 014807](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>) — a TEOS and PECVD nitride
  passivation at the fab in 2005.[^cyp-qtp-014807]
* SEMI C3.55, C3.12 and C70 — specifications for silane, ammonia and
  tungsten hexafluoride.[^semi-c3-55][^semi-c3-12][^semi-c70]
* NIOSH, *Pocket Guide to Chemical Hazards* — ammonia and
  diborane.[^niosh-nh3][^niosh-diborane]
* [Applied Materials, *SACVD* (Wayback capture of 2000)](<https://web.archive.org/web/20000709131617/http://www.appliedmaterials.com:80/products/sacvd.html>) — TEOS and ozone
  in a sub-atmospheric chamber.[^amat-sacvd-2000]
* [Lee and Collins (Novellus), US 6,635,965](<https://patents.google.com/patent/US6635965B1/en>) — the pulsed nucleation
  layer.[^pat-pnl-novellus]

### High-level understanding

* Wikipedia, [*Silane*](<https://en.wikipedia.org/wiki/Silane>), [*Dichlorosilane*](<https://en.wikipedia.org/wiki/Dichlorosilane>) and [*Ammonia*](<https://en.wikipedia.org/wiki/Ammonia>) — silicon and
  nitrogen precursors.[^wiki-silane][^wiki-dcs][^wiki-ammonia]
* Wikipedia, [*Tetraethyl orthosilicate*](<https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>), [*Ozone*](<https://en.wikipedia.org/wiki/Ozone>) and [*Silicon
  tetrafluoride*](<https://en.wikipedia.org/wiki/Silicon_tetrafluoride>) — oxide precursors.[^wiki-teos][^wiki-ozone][^wiki-sif4]
* Wikipedia, [*Tungsten hexafluoride*](<https://en.wikipedia.org/wiki/Tungsten_hexafluoride>) and [*Diborane*](<https://en.wikipedia.org/wiki/Diborane>) — the tungsten fill
  gases.[^wiki-wf6][^wiki-diborane]
* [Wikipedia, *Industrial gas*](<https://en.wikipedia.org/wiki/Industrial_gas>) — gas cabinets and supply.[^wiki-industrial-gas]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) — CVD
  of silicon, oxide, nitride and tungsten.[^txt-02]

### Deep dive

* [Kamins, *JES* 1980](<https://doi.org/10.1149/1.2129733>) — LPCVD silicon from silane.[^kamins-1980]
* [Roenigk and Jensen, *JES* 1987](<https://doi.org/10.1149/1.2100756>) — LPCVD nitride from dichlorosilane and
  ammonia.[^roenigk-1987]
* [Gumpher et al., *JES* 2004](<https://doi.org/10.1149/1.1690294>) — BTBAS nitride.[^gumpher-2004]
* [Becker et al., *JVST B* 1987](<https://doi.org/10.1116/1.583673>) — LPCVD TEOS oxide.[^becker-1987]
* [Adams et al., *JES* 1981](<https://doi.org/10.1149/1.2127680>) — plasma-deposited oxide.[^adams-1981-pecvd]
* [Denisse et al., *JAP* 1986](<https://doi.org/10.1063/1.337117>) — PECVD oxynitride from silane, N₂O and
  ammonia.[^denisse-1986]
* Fujino et al., *JES* 1990 and 1991 — TEOS–ozone oxide and doped
  glass.[^fujino-1990][^fujino-1991]
* [Kwok et al., *JES* 1994](<https://doi.org/10.1149/1.2055081>) — surface effects in ozone–TEOS gap
  fill.[^kwok-1994]
* [Nguyen, *IBM J. Res. Dev.* 1999](<https://doi.org/10.1147/rd.431.0109>) — HDP-CVD dielectrics.[^nguyen-1999]
* [Denison, Barbour and Burkhart, *JVST A* 1996](<https://doi.org/10.1116/1.580280>) — fluorine-doped oxide
  from SiF₄.[^denison-1996]
* [McConica and Krishnamani, *JES* 1986](<https://doi.org/10.1149/1.2108468>) — WF₆ reduction
  kinetics.[^mcconica-1986]
* [Kleijn et al., *JES* 1991](<https://doi.org/10.1149/1.2085620>) — transport in tungsten LPCVD.[^kleijn-1991]
* [Britton, *Plant/Operations Progress* 1990](<https://doi.org/10.1002/prsb.720090107>) — combustion hazards of
  silane and chlorosilanes.[^britton-1990]
* Caton et al. (VLSI Technology), US 5,303,558, and Lin et al. (TSMC),
  US 2004/0069224 — ammonium chloride traps for nitride
  furnaces.[^pat-nh4cl-vlsi][^pat-nh4cl-tsmc]

## Open questions

* Which precursors, grades and suppliers SkyWater uses, and whether its
  furnace nitride uses dichlorosilane, are not stated; "DH3" is not
  explained.[^skw-01][^sec-01][^sec-02]
* Whether SKY130's inter-metal dielectrics are fluorinated, and so
  whether SiF₄ is used, is not public.[^skw-01]
* Whether the tungsten nucleation uses silane or diborane is not
  stated.[^skw-01]
* Whether ozone–TEOS deposition is used anywhere in SKY130 is not
  public.

<!-- footnotes -->

[^wiki-silane]: Wikipedia, *Silane*. <https://en.wikipedia.org/wiki/Silane>
[^semi-c3-55]: SEMI, *SEMI C3.55 — Specification for Silane (SiH4), Bulk,
    99.994% Quality*, SEMI Standards store listing (revision C3.55-1011
    (Reapproved 0218)), accessed 2026-09-13.
    <https://store-us.semi.org/products/c00355-semi-c3-55-specification-for-silane-sih4-bulk-99-994-quality>
[^semi-c3-12]: SEMI, *SEMI C3.12 — Specification for Ammonia (NH3) in
    Cylinders, 99.998% Quality*, SEMI Standards store listing (revision
    C3.12-0116 (Reapproved 0922)), accessed 2026-09-13.
    <https://store-us.semi.org/products/c00312-semi-c3-12-specification-for-ammonia-nh3-in-cylinders-99-998-quality>
[^semi-c70]: SEMI, *SEMI C70 — Specification for Tungsten Hexafluoride
    (WF6)*, SEMI Standards store listing (revision C70-0924), accessed
    2026-09-13.
    <https://store-us.semi.org/products/c0700-semi-c70-specification-for-tungsten-hexafluoride>
[^wiki-wf6]: Wikipedia, *Tungsten hexafluoride*.
    <https://en.wikipedia.org/wiki/Tungsten_hexafluoride>
[^niosh-nh3]: National Institute for Occupational Safety and Health,
    *NIOSH Pocket Guide to Chemical Hazards: Ammonia*, CDC; read from the
    Wayback Machine capture of 2026-01-08.
    <https://www.cdc.gov/niosh/npg/npgd0028.html>
    <https://web.archive.org/web/20260108051903/https://www.cdc.gov/niosh/npg/npgd0028.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; film deposition, furnace, RTA and asher entries
    re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; the "Business" overview and the "Raw
    materials." run-in paragraph under "Manufacturing"; read from a
    Wayback Machine copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; "Raw materials" paragraph; read from a Wayback Machine
    copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^kamins-1980]: T. I. Kamins, "Structure and Properties of LPCVD Silicon
    Films", *Journal of The Electrochemical Society* **127**(3), 686–690
    (1980). <https://doi.org/10.1149/1.2129733>
[^adams-1981-pecvd]: A. C. Adams, F. B. Alexander, C. D. Capio and
    T. E. Smith, "Characterization of Plasma-Deposited Silicon Dioxide",
    *Journal of The Electrochemical Society* **128**(7), 1545–1551
    (1981). <https://doi.org/10.1149/1.2127680>
[^nguyen-1999]: S. V. Nguyen, "High-density plasma chemical vapor
    deposition of silicon-based dielectric films for integrated
    circuits", *IBM Journal of Research and Development* **43**(1.2),
    109–126 (1999). <https://doi.org/10.1147/rd.431.0109>
[^britton-1990]: L. G. Britton, "Combustion hazards of silane and its
    chlorides", *Plant/Operations Progress* **9**(1), 16–38 (1990).
    <https://doi.org/10.1002/prsb.720090107>
[^wiki-dcs]: Wikipedia, *Dichlorosilane*.
    <https://en.wikipedia.org/wiki/Dichlorosilane>
[^roenigk-1987]: K. F. Roenigk and K. F. Jensen, "Low Pressure CVD of
    Silicon Nitride", *Journal of The Electrochemical Society*
    **134**(7), 1777–1785 (1987). <https://doi.org/10.1149/1.2100756>
[^pat-nh4cl-vlsi]: O. L. Caton, C. A. Bellows, C. M. Hebert, Jr. and
    S. J. Schaper (VLSI Technology), *Thermal trap for gaseous
    materials*, US 5,303,558 A, filed 1992-07-30, granted 1994-04-19.
    <https://patents.google.com/patent/US5303558A/en>
[^denisse-1986]: C. M. M. Denisse, K. Z. Troost, J. B. Oude Elferink,
    F. H. P. M. Habraken, W. F. van der Weg and M. Hendriks,
    "Plasma-enhanced growth and composition of silicon oxynitride films",
    *Journal of Applied Physics* **60**(7), 2536–2542 (1986).
    <https://doi.org/10.1063/1.337117>
[^wiki-ammonia]: Wikipedia, *Ammonia*.
    <https://en.wikipedia.org/wiki/Ammonia>
[^wiki-teos]: Wikipedia, *Tetraethyl orthosilicate*.
    <https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>
[^becker-1987]: F. S. Becker, D. Pawlik, H. Anzinger and A. Spitzer,
    "Low-pressure deposition of high-quality SiO₂ films by pyrolysis of
    tetraethylorthosilicate", *Journal of Vacuum Science & Technology B*
    **5**(6), 1555–1563 (1987). <https://doi.org/10.1116/1.583673>
[^fujino-1990]: K. Fujino, Y. Nishimoto, N. Tokumasu and K. Maeda,
    "Silicon Dioxide Deposition by Atmospheric Pressure and
    Low-Temperature CVD Using TEOS and Ozone", *Journal of The
    Electrochemical Society* **137**(9), 2883–2887 (1990).
    <https://doi.org/10.1149/1.2087093>
[^fujino-1991]: K. Fujino, Y. Nishimoto, N. Tokumasu and K. Maeda,
    "Doped Silicon Oxide Deposition by Atmospheric Pressure and Low
    Temperature Chemical Vapor Deposition Using Tetraethoxysilane and
    Ozone", *Journal of The Electrochemical Society* **138**(10),
    3019–3024 (1991). <https://doi.org/10.1149/1.2085358>
[^kwok-1994]: K. Kwok, E. Yieh, S. Robles and B. C. Nguyen, "Surface
    Related Phenomena in Integrated PECVD/Ozone-TEOS SACVD Processes for
    Sub-Half Micron Gap Fill: Electrostatic Effects", *Journal of The
    Electrochemical Society* **141**(8), 2172–2177 (1994).
    <https://doi.org/10.1149/1.2055081>
[^wiki-ozone]: Wikipedia, *Ozone*. <https://en.wikipedia.org/wiki/Ozone>
[^gumpher-2004]: J. Gumpher, W. Bather, N. Mehta and D. Wedel,
    "Characterization of Low-Temperature Silicon Nitride LPCVD from
    Bis(tertiary-butylamino)silane and Ammonia", *Journal of The
    Electrochemical Society* **151**(5), G353 (2004).
    <https://doi.org/10.1149/1.1690294>
[^denison-1996]: D. R. Denison, J. C. Barbour and J. H. Burkhart, "Low
    dielectric constant, fluorine-doped SiO₂ for intermetal
    dielectric", *Journal of Vacuum Science & Technology A* **14**(3),
    1124–1126 (1996). <https://doi.org/10.1116/1.580280>
[^wiki-sif4]: Wikipedia, *Silicon tetrafluoride*.
    <https://en.wikipedia.org/wiki/Silicon_tetrafluoride>
[^mcconica-1986]: C. M. McConica and K. Krishnamani, "The Kinetics of
    LPCVD Tungsten Deposition in a Single Wafer Reactor", *Journal of The
    Electrochemical Society* **133**(12), 2542–2548 (1986).
    <https://doi.org/10.1149/1.2108468>
[^kleijn-1991]: C. R. Kleijn, C. J. Hoogendoorn, A. Hasper, J. Holleman
    and J. Middelhoek, "Transport Phenomena in Tungsten LPCVD in a
    Single-Wafer Reactor", *Journal of The Electrochemical Society*
    **138**(2), 509–517 (1991). <https://doi.org/10.1149/1.2085620>
[^wiki-diborane]: Wikipedia, *Diborane*.
    <https://en.wikipedia.org/wiki/Diborane>
[^niosh-diborane]: National Institute for Occupational Safety and
    Health, *NIOSH Pocket Guide to Chemical Hazards: Diborane*, CDC; read
    from the Wayback Machine capture of 2026-01-22.
    <https://www.cdc.gov/niosh/npg/npgd0183.html>
    <https://web.archive.org/web/20260122103710/https://www.cdc.gov/niosh/npg/npgd0183.html>
[^pat-pnl-novellus]: S.-H. Lee and J. Collins (Novellus Systems), *Method
    for producing ultra-thin tungsten layers with improved step coverage*,
    US 6,635,965 B1, filed 2001-10-09, granted 2003-10-21.
    <https://patents.google.com/patent/US6635965B1/en>
[^amat-sacvd-2000]: Applied Materials, *SACVD* (Giga-Fill SACVD Centura),
    product page; Wayback Machine capture of 2000-07-09.
    <https://web.archive.org/web/20000709131617/http://www.appliedmaterials.com:80/products/sacvd.html>
[^cyp-01]: Cypress Semiconductor, *Cypress Closes Sale of Minnesota Wafer
    Fabrication Facility*, PR Newswire, 2017-03-01, accessed 2026-09-13.
    <https://www.prnewswire.com/news-releases/cypress-closes-sale-of-minnesota-wafer-fabrication-facility-300416287.html>
[^cyp-qtp-014807]: Cypress Semiconductor, *Technology Derivative
    Qualification Report, QTP# 014807 Version 2.0: Technology
    Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM*, June 2005
    (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
[^wiki-industrial-gas]: Wikipedia, *Industrial gas*.
    <https://en.wikipedia.org/wiki/Industrial_gas>
[^pat-nh4cl-tsmc]: L. Lin, T. Fan, S. Chen, V. Lee and Y.-H. Wu (Taiwan
    Semiconductor Manufacturing Company), *Cold trap for CVD furnace*,
    US 2004/0069224 A1, filed 2002-10-11, published 2004-04-15.
    <https://patents.google.com/patent/US20040069224A1/en>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
