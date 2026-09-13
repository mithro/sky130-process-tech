(material-process-gases)=
# Process gases

Process gases are the bulk and near-bulk gases that run through almost
every tool of a fab: nitrogen for purging, venting and drying; oxygen
and hydrogen for oxidation and steam; argon and helium as sputter gas,
plasma diluent and backside coolant; and a few oxidation additives —
hydrogen chloride or dichloroethylene for chlorine, nitrous oxide or
nitric oxide for nitrogen, and water vapour for ashing and corrosion
passivation. Unlike the toxic hydrides and fluorides of the
{ref}`dopant <material-dopant-sources>`, {ref}`precursor
<material-precursors>` and {ref}`etch <material-etch-gases>` classes,
most of them are inert, oxidising or flammable rather than poisonous, and
they are used in far larger volumes. This page describes the class in
general, lists representative gases and the purity grades they are
bought to, and then says what SkyWater has published about process gases
at its fab and which SKY130 steps name them. The oxidation chemistry is
on the {ref}`oxidation category page <category-oxidation>`, and the
tools that use most of these gases are the
{ref}`oxidation furnace <machine-vertical-furnace-oxidation>`, the
{ref}`rapid thermal processor <machine-rapid-thermal-processor>`, the
{ref}`PVD cluster tool <machine-pvd-cluster-tool>` and the
{ref}`asher <machine-downstream-plasma-asher>`.

| | Process gases |
|---|---|
| What they do | Purge and blanket tools, oxidise silicon, carry and dilute reactive gases, sputter and cool; thermal oxidation "may use either water vapor (usually UHP steam) or molecular oxygen as the oxidant".[^wiki-thox] |
| Gases in the SKY130 steps | Nitrogen, oxygen, hydrogen, argon, helium; water vapour; HCl or trans-1,2-dichloroethylene; N₂O or NO (step-page readings). |
| Grades | SEMI C3 and its successors specify gases "used in the manufacture and processing of semiconductors";[^semi-c3] SEMI C59 covers "all grades of nitrogen used in the semiconductor industry".[^semi-c59] |
| Supply | "High purity oxygen, nitrogen, and argon, used for semiconductor device fabrication, require cryogenic distillation";[^wiki-air-separation] one supplier's on-site plants deliver N₂ and O₂ "with less than 1 part per billion (ppb) impurities".[^linde-eng-electronics] |
| Hazards | Hydrogen "forms explosive mixtures with air in concentrations from 4%–74%";[^wiki-hydrogen] nitrogen "presents an asphyxiation hazard" in an enclosed space;[^wiki-nitrogen] NIOSH gives an IDLH of 50 ppm for hydrogen chloride and 100 ppm for nitric oxide.[^niosh-hcl][^niosh-no] |
| SkyWater evidence | "wet oxidation to 1150C", "dry oxidation to 1150C", "Ar anneal to 1150C", "N2 anneal to 1150C", "H2 and forming gas alloy", "Ag Heatpulse 8808 NH3, Ar, N2, O2";[^skw-01] "high-purity compressed gases";[^sec-01][^sec-02] N₂O emissions reported to the EPA for the Bloomington fab[^epa-ghgrp-skywater] |
| SKY130 steps | 148 steps; see {ref}`SKY130 steps that use this class <material-process-gases-steps>` |

## What the class is and what it does

Most process gases do not end up in the wafer. Nitrogen and argon keep
air and moisture out of chambers, carry reactive gases to the wafer and
fill the chamber when it is vented; helium carries heat from the wafer to
a cooled chuck; oxygen, hydrogen and the oxidation additives react with
silicon to grow oxide. What the class shares is the requirement that
nothing else comes with the gas: moisture, oxygen, hydrocarbons and
particles in a purge or carrier gas reach every wafer the tool
processes. Ohmi's programme of "ultraclean technology" named an
"ultraclean processing environment" among its three
principles,[^ohmi-1993] and SEMI's gas specifications were written so
that "The function of the specifications is to establish desired
standards of quality".[^semi-c3]

### Nitrogen

Nitrogen is the fab's universal inert gas. "Nitrogen gas is an
industrial gas produced by the fractional distillation of liquid air, or
by mechanical means using gaseous air (pressurised reverse osmosis
membrane or pressure swing adsorption)".[^wiki-nitrogen] It purges
furnace tubes, load locks and gas lines, vents vacuum chambers, dries
wafers after wet processing and blankets wafers in transfer (industry
practice); vertical
furnaces "allow the use of load locks to purge the wafers with nitrogen
before oxidation to limit the growth of native oxide on the Si
surface".[^wiki-thox] It is also a reactant: added to argon in a
titanium sputtering chamber it makes titanium nitride, a process whose
hysteresis Berg and Nyberg model,[^berg-2005] and it is the carrier of
{term}`forming gas`, which in typical formulations of "5% H2 in N2" is
"not explosive".[^wiki-fg]

### Oxygen and hydrogen

Dry oxidation uses oxygen; wet oxidation uses steam, which production
furnaces make by burning hydrogen in oxygen in a torch ahead of the tube
({ref}`category-oxidation`). Deal and Grove's model describes the growth
in both oxidants.[^deal-1965] Wet oxidation "is preferred to dry oxidation
for growing thick oxides, because of the higher growth rate", and thick
oxides are often grown "with a long wet oxidation bracketed by short dry
ones".[^wiki-thox] Hydrogen and oxygen can also react at the wafer in a
rapid thermal chamber, in-situ steam generation ({term}`ISSG`), which Yu
et al. applied to ultrathin gate oxide.[^yu-1999] Oxygen is also the
reactive gas of resist ashing, where "Oxygen or fluorine are the most
common reactive species",[^wiki-ash] and the oxidant of silane and TEOS
oxides in {term}`HDP-CVD` and {term}`PECVD`. Hydrogen further reduces
tungsten hexafluoride in the tungsten fill ({ref}`category-deposition`)
and is a co-gas in implanter ion sources, where "Hydrogen or hydrogen
with xenon, krypton or argon may be added to the plasma to delay the
degradation of tungsten components due to the halogen
cycle".[^wiki-implant]

### Argon and helium

Argon is the sputter gas: "Argon gas is also commonly used for sputter
deposition of thin films as in microelectronics and for wafer cleaning in
microfabrication".[^wiki-argon] It also dilutes etch and HDP plasmas and
serves as an inert anneal ambient. It is "readily obtained as a byproduct
of cryogenic air separation in the production of liquid oxygen and liquid
nitrogen".[^wiki-argon] Helium is used for its high thermal
conductivity and inertness: as the backside gas between a wafer and an
{term}`electrostatic chuck`, and as a carrier and diluent in CVD.
Goodman describes how "Electrostatic chucks (ESCs) are used in the
semiconductor industry to clamp wafers to a pedestal and combined with
back side gas (BSG) cooling to control temperature during processing",
and models the backside pressure a bowed wafer can hold.[^goodman-2008]
Unlike the air gases, helium "is extracted by fractional distillation
from natural gas, which can contain as much as 7% helium", and its
market has swung between "renowned shortages" and
over-supply.[^wiki-helium]

### Chlorine additions: HCl and DCE

A few per cent of a chlorine source in a dry oxidation getters mobile
ions ({term}`gettering`): "The oxidizing ambient may also contain several percent of
hydrochloric acid (HCl)", and "The chlorine neutralizes metal ions that
may occur in the oxide".[^wiki-thox] Kriegler, Cheng and Colton found
that "The addition of a few mole per cent of HCl or Cl 2 to the oxidizing
atmosphere has been found to significantly improve the electrical
stability of dry‐grown SiO 2 films", that the oxidation rate "is
considerably increased", and that HCl in dry oxygen was "very effective
for the “cleaning” of quartz furnace tubes".[^kriegler-1972] Chlorine
"is often introduced by adding hydrogen chloride or trichloroethylene to
the oxidizing medium";[^wiki-thox] Yoneda et al. qualified "trans 1,2‐dichloroethylene added
oxidation as a substitution for 1,1,1‐trichloroethane", with "lower ozone
depletion potential", and recommended a concentration of "5 w/o" on cost
and performance.[^yoneda-1995] A Persys Technology patent describes one
external torch that can provide "oxygen for steam production, and DCE and
oxygen for HCl production".[^pat-torch-persys]

### Nitrous oxide and nitric oxide

N₂O and NO put nitrogen into a growing oxide. "At elevated temperatures,
nitrous oxide is a powerful oxidiser similar to molecular
oxygen".[^wiki-n2o] Hwang et al. grew "high quality ultrathin (∼60 Å)
gate dielectrics using N2O (nitrous oxide) gas" by rapid thermal
oxidation, and found "a nitrogen-rich layer at the Si/SiO2
interface";[^hwang-1990] their later model explained the resistance of
such films to boron penetration.[^hwang-1991] In a furnace, Tobin et al.
showed that "for a 950 °C oxynitridation process, N2O decomposes into N2,
O2, and NO before reaching the wafer load", and that the nitrogen
concentration follows the NO concentration;[^tobin-1994] Okada et al.
then grew gate oxynitride in NO directly and found that "Much lower
thermal budget is required for an NO process than for an N/sub 2/O
process".[^okada-1994] Kuehne et al. applied NO to rapid thermal
nitridation of thin gate oxides.[^kuehne-1997] N₂O is also the usual
oxidant of silane-based PECVD oxide and, with ammonia, of oxynitride
({ref}`category-deposition`). Nitric oxide is classed as "Very toxic,
corrosive, oxidizer".[^wiki-no]

### Water vapour

Water vapour appears in two places in a 130 nm-era flow. Added to an
oxygen downstream plasma, it helps remove resist, and Fujimura et al.
described a "Sodium contamination free ashing process using O₂+H₂O
plasma downstream".[^fujimura-1994] After chlorine-based metal etching,
a water-vapour or oxygen plasma treatment is used to passivate the
aluminium–copper lines before they meet air (industry practice). The
reason is corrosion: Lee, Eldridge and Schwartz found that "Aluminum and
Al-Cu conductor lines etched with a Cl containing plasma in low-pressure
diode systems corroded rapidly upon atmospheric exposure", with copper
enrichment among the causes for the alloys.[^lee-1981-corrosion]

## Representative materials and grades

Process gases are bought to purity grades that limit moisture, oxygen,
hydrocarbons, metals and particles, delivered either in bulk (liquid
tanks, pipelines or on-site plants) or in cylinders. SEMI's gas
specifications start from SEMI C3, "originally published in 1981",
whose specifications are "intended to serve for gases to be used in the
manufacture and processing of semiconductors and advanced electronic
devices and circuits";[^semi-c3] later documents gather the grades of
one gas. The listings below describe standards and supplier catalogues,
not what SkyWater buys; the purity of SKY130's gases is not public.

* **Nitrogen.** SEMI C59 provides "a series of specifications for
  different grades of nitrogen (N2)" and covers "all grades of nitrogen
  used in the semiconductor industry".[^semi-c59] Linde Engineering
  states that its SPECTRA on-site plants "deliver ultra-pure gaseous and
  liquid N2 and O2 with less than 1 part per billion (ppb) impurities",
  while its NITRON E plants suit "customers with less exacting purity
  requirements (100 ppb)".[^linde-eng-electronics]
* **Oxygen.** SEMI C54 "provides a series of specifications for
  different grades of oxygen (O2)" and cites among its references a
  "Standard for Oxygen (O2), Bulk, 99.9998% Quality".[^semi-c54]
* **Hydrogen.** SEMI C58 "covers requirements for two grades of hydrogen
  used in the semiconductor industry".[^semi-c58] Linde notes that
  "High-purity hydrogen (H2) is often supplied in liquid form for
  low-volume electronics applications".[^linde-eng-electronics]
* **Argon.** Co-produced with nitrogen and oxygen by cryogenic air
  separation;[^wiki-argon] Linde lists "ultra-high-purity nitrogen (N₂),
  oxygen (O₂), argon (Ar), hydrogen (H₂), helium (He), and carbon dioxide
  (CO₂)" among the bulk gases it supplies to wafer fabs.[^linde-semi]
* **Helium.** SEMI C3.20 provides "specifications for helium (He) that is
  used in the semiconductor industry".[^semi-c3-20]
* **HCl and DCE.** Anhydrous hydrogen chloride "Shipped as a liquefied
  compressed gas";[^niosh-hcl] trans-1,2-dichloroethylene is a liquid
  with "applications including electronics cleaning, precision cleaning,
  and certain metal cleaning applications",[^wiki-dce] delivered to a
  furnace as vapour (industry practice); Yoneda et al. added it to gate
  oxidation.[^yoneda-1995]
* **N₂O and NO.** Nitrous oxide in cylinders; nitric oxide, a "Colorless
  gas" "Shipped as a nonliquefied compressed gas".[^niosh-no]
* **Water vapour.** Generated at the tool from ultrapure water or, in a
  furnace, by burning hydrogen in oxygen ({ref}`category-oxidation`).

## At SkyWater

### What SkyWater's filings and pages list

SkyWater's *Facilities & Capabilities* page names process gases on its
furnace, RTA and asher entries. Under "Furnaces/Diffusion/Pre-Clean"
and "RTA":[^skw-01]

> "Furnaces are all made by Aviza" · "wet oxidation to 1150C" · "dry
> oxidation to 1150C" · "Ar anneal to 1150C" · "N2 anneal to 1150C" ·
> "H2 and forming gas alloy"
>
> "Ag Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C"

and under "Resist removal/cleans" and "Poly/Silicon Etch":[^skw-01]

> "Gasonic PEP, remote microwave plasma, N2, O2, 120C – 270C"
>
> "Iridia RF microwave, N2, O2, H2, CF4, NH3, H2/N2, 40C-270C"
>
> "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to 250C"
>
> "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2" · "Lam 9400 TCP,
> poly/nitride, HBr, CF4, SF6, O2" · "Lam 4400, HBr, Cl2, C2F6, CF4,
> SF6, O2"

Read term by term, the page names nitrogen, oxygen, argon and hydrogen,
and implies steam for "wet oxidation"; it names no helium, no chlorine
source, no N₂O or NO and no water vapour, and it lists "Nitrided gate
oxide" among its special modules without a gas.[^skw-01] It gives no
gases for its PVD, CVD or metal-etch tools, where the step pages read
argon, nitrogen, helium and oxygen as typical.

SkyWater's registration statement of 2021 and its annual report for
fiscal 2023 describe the raw materials as including "high-purity
compressed gases" and name gas suppliers:[^sec-01][^sec-02]

| Filing | Gas suppliers as named |
|--------|------------------------|
| S-1 (2021)[^sec-01] | "Air Products & Chemicals, Inc. (bulk and specialty gases, chemicals)"; "Praxair, Inc. (bulk and specialty gases)" |
| 10-K for fiscal 2023[^sec-02] | "Linde, Inc. (bulk and specialty gases)"; "Airgas USA LLC (specialty gases)"; "EMD Performance Materials Corp (Versum) (specialty chemicals and gases)" |

Neither filing says which gases, grades or delivery modes each supplier
provides. Wikipedia records that Praxair "merged with Linde AG to form
Linde plc" in 2018,[^wiki-praxair] that Airgas is "an Air Liquide
company",[^wiki-airgas] and that Air Products completed the spin-off of
Versum Materials in 2016, which the Merck Group acquired in
2019;[^wiki-versum] none of these articles names the "Linde, Inc." or
"EMD Performance Materials Corp" of the filing or SkyWater. Linde's
product pages quoted above describe its catalogue, not SkyWater's
purchases.[^linde-semi][^linde-eng-electronics]

One further public record bears on this class. The U.S. Environmental
Protection Agency's Greenhouse Gas Reporting Program lists facility
1000354 at 2401 E. 86th St., Bloomington, Minnesota — named "SKYWATER
TECHNOLOGY FOUNDRY INC" in the records for 2010–2013 and "SKYWATER
TECHNOLOGY INC" from 2014 — reporting under subparts C and I in each
year from 2011 to 2023, with "CYPRESS SEMICONDUCTOR CORP (100%)" as
parent company in the years to 2016; its
subpart I entries include N₂O emissions in every one of those
years.[^epa-ghgrp-skywater] Subpart I is the electronics-manufacturing
category, under which facilities report "N2O emissions from CVD and other
production processes".[^epa-ghgrp-subpart-i] We read this as evidence
that nitrous oxide is used at the fab; the public tables do not say in
which process.

### Strength of the evidence

The furnace, RTA and asher entries are SkyWater statements and rank as
**strong** evidence, on the scale of the
{ref}`machines index <machines-reading-evidence>`, that oxygen, steam
(by an unstated method), argon, nitrogen and hydrogen are used at the
fab; that the steam is pyrogenic is industry practice, not a SkyWater
statement. As for the tools, the list describes the whole fab in the 2020s and ties no gas
to a step.[^skw-01] The EPA record is a regulatory filing about the
Bloomington facility and is strong for the use of N₂O somewhere in its
processes, weak for any SKY130 step.[^epa-ghgrp-skywater] The supplier
statements are strong as statements but name no gas, and the suppliers
changed between the 2021 and 2023 filings.[^sec-01][^sec-02] Helium,
HCl or DCE, NO and water vapour appear in no SkyWater source cited here;
their use in SKY130 steps is industry practice that the step pages
supply.

(material-process-gases-steps)=
### SKY130 steps that use this class

This page covers the rows of the {ref}`materials index <materials-table>`
listed below by key; the steps are those whose *Resources required* section
names one of them (the union of the rows' *Steps* cells). Forming gas,
which the step pages name for ashes and alloys, belongs to the anneal
ambients row; ammonia belongs to the {ref}`precursors
<material-precursors>` page, and the argon, xenon or hydrogen support
gases of the implanters to the ion-source row of the
{ref}`dopant sources <material-dopant-sources>` page.

Materials index rows covered:

* `n2` — nitrogen
* `o2` — oxygen
* `h2` — hydrogen
* `ar` — argon
* `he` — helium
* `water-vapour` — water vapour
* `hcl-dce` — HCl or trans-1,2-dichloroethylene
* `n2o-no` — nitrous oxide and nitric oxide

Steps:

{ref}`SMAT <step-001>`, {ref}`BOX <step-002>`, {ref}`ISONIT <step-003>`, {ref}`STINITE <step-005>`, {ref}`STIE <step-006>`, {ref}`DNI <step-008>`, {ref}`DNIS <step-009>`, {ref}`LINOX <step-010>`, {ref}`FILOX <step-011>`, {ref}`NS19 <step-013>`, {ref}`LVTNM <step-014>`, {ref}`LVTNI <step-015>`, {ref}`LVTNIS <step-016>`, {ref}`NWM <step-017>`, {ref}`NWI <step-018>`, {ref}`LVTPIS <step-021>`, {ref}`HVTPM <step-022>`, {ref}`PCHIS <step-025>`, {ref}`PWBM <step-026>`, {ref}`PWIS <step-029>`, {ref}`PWDEM <step-030>`, {ref}`PWDEIS <step-033>`, {ref}`RTAI <step-034>`, {ref}`TUNM <step-035>`, {ref}`TUNARCE <step-036>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`TUNME <step-039>`, {ref}`ONO <step-040>`, {ref}`ONOM <step-041>`, {ref}`ONOME <step-042>`, {ref}`GOX100 <step-043>`, {ref}`LVOM <step-044>`, {ref}`NCHI <step-045>`, {ref}`GOXETCH <step-046>`, {ref}`LVGOX <step-047>`, {ref}`SAGD <step-048>`, {ref}`RPM <step-049>`, {ref}`P1I <step-050>`, {ref}`P1IS <step-051>`, {ref}`RRPM <step-052>`, {ref}`PRI <step-053>`, {ref}`PRIS <step-054>`, {ref}`URPM <step-055>`, {ref}`UPRI <step-056>`, {ref}`UPRIS <step-057>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`BFR <step-060>`, {ref}`P1M <step-061>`, {ref}`P1ME <step-062>`, {ref}`IOX45 <step-063>`, {ref}`NTM <step-064>`, {ref}`ASTI <step-065>`, {ref}`BHI <step-066>`, {ref}`ASTIS <step-067>`, {ref}`HVNTM <step-068>`, {ref}`HVASTI <step-069>`, {ref}`HVASTIS <step-070>`, {ref}`LDNTM <step-071>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`, {ref}`LDASTIS <step-074>`, {ref}`TIPRTAD <step-075>`, {ref}`SPNIT <step-076>`, {ref}`SPE <step-077>`, {ref}`NPCM <step-078>`, {ref}`NPCME <step-079>`, {ref}`SPOX <step-080>`, {ref}`PSDM <step-081>`, {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`PDIS <step-084>`, {ref}`NSDM <step-085>`, {ref}`NSDI <step-086>`, {ref}`NSDIS <step-087>`, {ref}`RTAD <step-088>`, {ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`, {ref}`RTAD2 <step-092>`, {ref}`LICM1 <step-093>`, {ref}`LICM1E <step-094>`, {ref}`SACETCH <step-095>`, {ref}`ALLY1 <step-096>`, {ref}`TI/TIN1 <step-097>`, {ref}`CSIL <step-098>`, {ref}`WDEP <step-099>`, {ref}`LITIN <step-101>`, {ref}`LI1M <step-102>`, {ref}`LI1ME <step-103>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`CTM1 <step-107>`, {ref}`CTME <step-108>`, {ref}`TIN2 <step-109>`, {ref}`WDEP2 <step-110>`, {ref}`TIAL6 <step-112>`, {ref}`MM1 <step-113>`, {ref}`MM1E <step-114>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`VIM <step-118>`, {ref}`VIME <step-119>`, {ref}`TIN3 <step-120>`, {ref}`WDEP3 <step-121>`, {ref}`TIAL12 <step-123>`, {ref}`MM2 <step-124>`, {ref}`MM2E <step-125>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`VIM2 <step-129>`, {ref}`VIM2E <step-130>`, {ref}`TIN4 <step-131>`, {ref}`WDEP4 <step-132>`, {ref}`WTIAL3 <step-134>`, {ref}`CAPILD <step-135>`, {ref}`CAPTIW1 <step-136>`, {ref}`CAPM <step-137>`, {ref}`CAPME <step-138>`, {ref}`MM3 <step-139>`, {ref}`MM3E <step-140>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`VIM3 <step-144>`, {ref}`VIM3E <step-145>`, {ref}`TIN5 <step-146>`, {ref}`WDEP5 <step-147>`, {ref}`WTIAL4 <step-149>`, {ref}`CAPILD2 <step-150>`, {ref}`CAPTIW2 <step-151>`, {ref}`CAP2M <step-152>`, {ref}`CAP2ME <step-153>`, {ref}`MM4 <step-154>`, {ref}`MM4E <step-155>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`VIM4 <step-159>`, {ref}`VIM4E <step-160>`, {ref}`WTIAL5 <step-161>`, {ref}`MM5 <step-162>`, {ref}`MM5E <step-163>`, {ref}`NFUSOX <step-164>`, {ref}`NSM <step-165>`, {ref}`NSME <step-166>`, {ref}`NTSD <step-167>`, {ref}`PDM <step-168>`, {ref}`PDME <step-169>`, {ref}`ALLY <step-170>`

The steps fall into groups, as the index rows describe them:

* **Nitrogen almost everywhere.** 142 steps name nitrogen, for purging,
  venting and drying, for reactive TiN sputtering, and as an ash or
  diluent gas; the 29 that do not are twelve CMP steps, ten implants, two
  mask steps, four HDP depositions and the electrical test.
* **Oxidations and anneals.** Oxygen at {ref}`BOX <step-002>`,
  {ref}`LINOX <step-010>`, {ref}`ONO <step-040>`,
  {ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>` and
  {ref}`IOX45 <step-063>`, with hydrogen (steam or radical oxidation),
  the chlorine additions or N₂O or NO at various of them (see the rows);
  argon and nitrogen as the likely RTA ambients
  at {ref}`RTAI <step-034>`, {ref}`TIPRTAD <step-075>`,
  {ref}`RTAD <step-088>`, {ref}`RTAD2 <step-092>` and
  {ref}`CSIL <step-098>` (inference on those pages).
* **Plasma tools.** Oxygen, argon and helium in the etches, ashes and
  CVD steps; N₂O as the oxidant of the silane oxide route of the cap
  oxides and of the capacitor oxynitride at {ref}`CAPILD <step-135>` and
  {ref}`CAPILD2 <step-150>`; water vapour at three implant strips and
  the local-interconnect and metal etches.
* **Sputtering and tungsten fill.** Argon and nitrogen at the PVD steps;
  hydrogen, argon and nitrogen at the tungsten fills.

## Supply, handling, safety and facilities

None of the SkyWater sources cited here describes the fab's gas yard,
distribution, purification or monitoring; the points below are industry
practice, standards and supplier statements.

* **Bulk supply.** Nitrogen, oxygen and argon come from air separation,
  which for semiconductor purity requires "cryogenic
  distillation";[^wiki-air-separation] a supplier offers either on-site
  plants or delivery "by road tanker or ISO container for storage on your
  site".[^linde-eng-electronics] Helium comes from natural gas and is
  subject to supply swings.[^wiki-helium]
* **Purity at the point of use.** Grades are specified by standards such
  as SEMI C59 and C54;[^semi-c59][^semi-c54] what reaches the wafer also
  depends on the piping and valves between (industry practice), part of
  the "ultraclean processing environment" of Ohmi's
  programme.[^ohmi-1993]
* **Asphyxiation.** Nitrogen, argon and helium displace oxygen; argon
  "is 38% more dense than air and therefore considered a dangerous
  asphyxiant in closed areas".[^wiki-argon] Liquid-nitrogen and bulk-gas
  rooms are monitored for low oxygen (industry practice).
* **Oxidisers and flammables.** Oxygen is rated "nonhazardous to health,
  nonflammable, and nonreactive, but an oxidizer";[^wiki-oxygen] hydrogen
  forms explosive mixtures with air over a wide range,[^wiki-hydrogen]
  and the {ref}`ALLY1 <step-096>` and {ref}`ALLY <step-170>` pages list a
  "hydrogen-rated gas panel with leak detection and purge interlocks" for
  the alloy furnace.
* **Toxic additives.** NIOSH lists hydrogen chloride with an IDLH of
  "50 ppm" and a ceiling REL of "5 ppm",[^niosh-hcl] and nitric oxide
  with an IDLH of "100 ppm" and a REL of "TWA 25 ppm";[^niosh-no]
  both are kept in monitored gas cabinets with scrubbed exhaust (industry
  practice).
* **Emissions reporting.** Facilities in the EPA's electronics category
  report "N2O emissions from CVD and other production processes" and
  "Controlled emissions of GHGs from abatement systems, if
  applicable";[^epa-ghgrp-subpart-i] SkyWater's Bloomington facility
  appears in that programme.[^epa-ghgrp-skywater]

## Process-integration notes for SKY130

These notes connect the class to the step pages; they add no SKY130
conditions of their own. SKY130's gas flows, ambients and purities are
not public.

* **Chlorine in the gate oxides.** The {ref}`LINOX <step-010>`,
  {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`,
  {ref}`LVGOX <step-047>` and {ref}`IOX45 <step-063>` pages name HCl or
  DCE as an optional chlorine source; the benefit is the ion gettering
  and tube cleaning Kriegler et al. measured,[^kriegler-1972] and the
  choice of DCE over trichloroethane follows the ozone-layer argument of
  Yoneda et al.[^yoneda-1995] SkyWater lists no chlorine source.[^skw-01]
* **A nitrided gate oxide without a named gas.** SkyWater lists
  "Nitrided gate oxide" as a special module and an RTA with "NH3, Ar, N2,
  O2",[^skw-01] and reports N₂O emissions for the
  fab;[^epa-ghgrp-skywater] the {ref}`LVGOX <step-047>` page reads the
  nitridation route as open among NH₃, N₂O or NO and plasma nitrogen.
  An N₂O furnace process delivers its nitrogen through the NO it forms in
  the tube,[^tobin-1994] and an NO process needs less thermal
  budget,[^okada-1994] which matters for the {ref}`ONO <step-040>` stack
  that sees the same heat (our reading).
* **N₂O in the dielectrics.** The cap-oxide pages
  ({ref}`NCAPOX <step-091>` to {ref}`NCAPOX6 <step-158>`,
  {ref}`NFUSOX <step-164>`), {ref}`POC <step-059>` and
  {ref}`SPOX <step-080>` name silane and N₂O as the alternative to TEOS
  and oxygen, and the capacitor dielectric pages
  ({ref}`CAPILD <step-135>`, {ref}`CAPILD2 <step-150>`) name N₂O with
  silane and ammonia for oxynitride. SkyWater's "PECVD silane
  oxide/nitride/oxynitride, C1" entry names no oxidant.[^skw-01]
* **Water vapour against corrosion.** The metal-etch pages
  ({ref}`MM1E <step-114>` to {ref}`MM5E <step-163>`) and
  {ref}`LI1ME <step-103>` name H₂O vapour or O₂/CF₄ for passivation after
  chlorine etching, which corrodes Al–Cu lines left
  unprotected;[^lee-1981-corrosion] the {ref}`PRIS <step-054>`,
  {ref}`PDIS <step-084>` and {ref}`NSDIS <step-087>` pages name water
  vapour as a possible ash addition after high-dose
  implants.[^fujimura-1994] SkyWater lists no water vapour on any
  asher.[^skw-01]
* **Anneal ambients.** The RTA pages read nitrogen and argon as the
  likely ambient because SkyWater lists the Heatpulse's gases but no
  ambient;[^skw-01] the {term}`forming gas` of the alloys belongs to the
  anneal ambients row of the {ref}`materials index <materials-table>`.
* **Helium behind the wafer.** Every etch, HDP and implant page that
  names helium does so for backside cooling or as a carrier or diluent; its pressure
  under the wafer is limited by chucking force and wafer
  bow,[^goodman-2008] and no SkyWater source names helium.

## Related pages

* {ref}`category-oxidation` — dry, wet and chlorinated oxidation and
  nitrided oxides.
* {ref}`machine-vertical-furnace-oxidation`,
  {ref}`machine-rapid-thermal-processor` and
  {ref}`machine-plasma-nitridation-chamber` — the tools that oxidise and
  nitride with these gases.
* {ref}`machine-pvd-cluster-tool` and {ref}`machine-downstream-plasma-asher`
  — argon and nitrogen for sputtering; oxygen, nitrogen and water vapour
  for ashing.
* {ref}`material-dopant-sources`, {ref}`material-precursors` and
  {ref}`material-etch-gases` — the toxic and reactive gas classes.
* {ref}`materials-index` — all consumable classes, including forming
  gas.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the furnace, RTA,
  asher and etcher entries quoted on this page.[^skw-01]
* SkyWater Technology, Form S-1 (2021) and Form 10-K for fiscal 2023 —
  the raw-materials paragraphs and gas suppliers.[^sec-01][^sec-02]
* U.S. EPA, Greenhouse Gas Reporting Program data for SkyWater's
  Bloomington facility, and the subpart I information sheet — N₂O
  reporting at the fab and what the category
  covers.[^epa-ghgrp-skywater][^epa-ghgrp-subpart-i]
* SEMI C3, C59, C54, C58 and C3.20 — gas specifications for the
  semiconductor
  industry.[^semi-c3][^semi-c59][^semi-c54][^semi-c58][^semi-c3-20]
* NIOSH, *Pocket Guide to Chemical Hazards* — exposure limits for
  hydrogen chloride and nitric oxide.[^niosh-hcl][^niosh-no]
* Linde, *Gases for semiconductors* and Linde Engineering, *Serving the
  Electronics Industry* — current bulk-gas supply and on-site plant
  statements.[^linde-semi][^linde-eng-electronics]

### High-level understanding

* Wikipedia, *Nitrogen*, *Oxygen*, *Hydrogen*, *Argon* and *Helium* —
  production, uses and hazards of the bulk
  gases.[^wiki-nitrogen][^wiki-oxygen][^wiki-hydrogen][^wiki-argon][^wiki-helium]
* Wikipedia, *Air separation* — how nitrogen, oxygen and argon are
  made.[^wiki-air-separation]
* Wikipedia, *Thermal oxidation*, *Forming gas* and *Plasma ashing* —
  wet, dry and chlorinated oxidation, forming gas and
  ashing.[^wiki-thox][^wiki-fg][^wiki-ash]
* Wikipedia, *Nitrous oxide*, *Nitric oxide* and
  *1,2-Dichloroethylene* — the oxidation
  additives.[^wiki-n2o][^wiki-no][^wiki-dce]
* Wikipedia, *Praxair*, *Airgas* and *Versum Materials* — the corporate
  histories behind the filings' supplier
  names.[^wiki-praxair][^wiki-airgas][^wiki-versum]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — oxidation and
  thin-film processes.[^txt-01]

### Deep dive

* Deal and Grove, *JAP* 1965 — the growth model for dry and wet
  oxidation.[^deal-1965]
* Kriegler, Cheng and Colton, *JES* 1972 — HCl and Cl₂ in dry
  oxidation.[^kriegler-1972]
* Yoneda et al., *JES* 1995 — trans-1,2-dichloroethylene in place of
  trichloroethane.[^yoneda-1995]
* Hwang et al., *APL* 1990 — ultrathin oxynitride grown in
  N₂O.[^hwang-1990]
* Hwang et al., *APL* 1991 — boron penetration through N₂O
  oxynitride.[^hwang-1991]
* Tobin et al., *JAP* 1994 — the role of NO in N₂O furnace
  oxynitridation.[^tobin-1994]
* Okada et al., *IEEE TED* 1994 — gate oxynitride grown in
  NO.[^okada-1994]
* Kuehne et al., MRS 1997 — rapid thermal nitridation in
  NO.[^kuehne-1997]
* Green et al., *JAP* 2001 — a review of ultrathin oxide and oxynitride
  gate dielectrics.[^green-2001]
* Yu et al., *Proc. SPIE* 1999 — in-situ steam generation for gate
  oxide.[^yu-1999]
* Fujimura et al., *JVST B* 1994 — O₂/H₂O downstream
  ashing.[^fujimura-1994]
* Lee, Eldridge and Schwartz, *JAP* 1981 — corrosion of Al and Al–Cu
  after chlorine reactive ion etching.[^lee-1981-corrosion]
* Berg and Nyberg, *Thin Solid Films* 2005 — reactive sputtering with
  nitrogen.[^berg-2005]
* Goodman, *JAP* 2008 — electrostatic chucking and backside gas
  cooling.[^goodman-2008]
* Ohmi, *Proc. IEEE* 1993 — ultraclean processing for ULSI.[^ohmi-1993]
* Drimer, Mendelovici and Borivker (Persys Technology), US 6,179,609 —
  an external steam and chlorination torch.[^pat-torch-persys]

## Open questions

* Which gases, grades and delivery modes (on-site plant, liquid bulk or
  cylinder) SkyWater uses, and which supplier provides each, are not
  stated.[^sec-01][^sec-02]
* Whether the "Linde, Inc." of the 2023 report is the former "Praxair,
  Inc." of the 2021 registration statement, and what "EMD Performance
  Materials Corp (Versum)" supplies, are not stated by the sources cited
  here.[^wiki-praxair][^wiki-versum]
* Whether SKY130 oxidations use a chlorine source, and whether it is HCl
  or DCE, is not public.[^skw-01]
* Which gas nitrides SkyWater's "Nitrided gate oxide", and which process
  accounts for the N₂O the facility reports, are not
  public.[^skw-01][^epa-ghgrp-skywater]
* Whether water vapour is used in any SkyWater asher or metal etcher is
  not stated.[^skw-01]

<!-- footnotes -->

[^wiki-thox]: Wikipedia, *Thermal oxidation*.
    <https://en.wikipedia.org/wiki/Thermal_oxidation>
[^semi-c3]: SEMI, *SEMI C3 — Specification for Gases*, SEMI Standards
    store listing (revision C3-0317), accessed 2026-09-13.
    <https://store-us.semi.org/products/c00300-semi-c3-specification-for-gases>
[^semi-c59]: SEMI, *SEMI C59 — Specification for Nitrogen*, SEMI
    Standards store listing (revision C59-0317), accessed 2026-09-13.
    <https://store-us.semi.org/products/c05900-semi-c59-specification-for-nitrogen>
[^wiki-air-separation]: Wikipedia, *Air separation*.
    <https://en.wikipedia.org/wiki/Air_separation>
[^linde-eng-electronics]: Linde Engineering, *Serving the Electronics
    Industry Worldwide*, industry page, accessed 2026-09-13.
    <https://www.linde-engineering.com/industries/electronics>
[^wiki-hydrogen]: Wikipedia, *Hydrogen*.
    <https://en.wikipedia.org/wiki/Hydrogen>
[^wiki-nitrogen]: Wikipedia, *Nitrogen*.
    <https://en.wikipedia.org/wiki/Nitrogen>
[^niosh-hcl]: National Institute for Occupational Safety and Health,
    *NIOSH Pocket Guide to Chemical Hazards: Hydrogen chloride*, CDC;
    read from the Wayback Machine capture of 2025-12-29.
    <https://www.cdc.gov/niosh/npg/npgd0332.html>
    <https://web.archive.org/web/20251229130832/https://www.cdc.gov/niosh/npg/npgd0332.html>
[^niosh-no]: National Institute for Occupational Safety and Health,
    *NIOSH Pocket Guide to Chemical Hazards: Nitric oxide*, CDC; read
    from the Wayback Machine capture of 2025-12-07.
    <https://www.cdc.gov/niosh/npg/npgd0448.html>
    <https://web.archive.org/web/20251207003006/https://www.cdc.gov/niosh/npg/npgd0448.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; furnace, RTA, resist removal and poly/silicon etch
    entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing"; read from a Wayback Machine copy on
    2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; "Raw materials" paragraph; read from a Wayback Machine
    copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^epa-ghgrp-skywater]: U.S. Environmental Protection Agency, Greenhouse
    Gas Reporting Program, Envirofacts tables `PUB_DIM_FACILITY` and
    `PUB_FACTS_SUBP_GHG_EMISSION` for facility ID 1000354 (Bloomington,
    Minnesota; "SKYWATER TECHNOLOGY FOUNDRY INC" for 2010–2013 and
    "SKYWATER TECHNOLOGY INC" from 2014), reporting years 2010–2023,
    retrieved 2026-09-13.
    <https://data.epa.gov/efservice/PUB_DIM_FACILITY/FACILITY_ID/1000354/JSON>
    <https://data.epa.gov/efservice/PUB_FACTS_SUBP_GHG_EMISSION/FACILITY_ID/1000354/SUB_PART_ID/43/JSON>
[^ohmi-1993]: T. Ohmi, "ULSI reliability through ultraclean
    processing", *Proceedings of the IEEE* **81**(5), 716–729 (1993).
    <https://doi.org/10.1109/5.220903>
[^berg-2005]: S. Berg and T. Nyberg, "Fundamental understanding and
    modeling of reactive sputtering processes", *Thin Solid Films*
    **476**(2), 215–230 (2005).
    <https://doi.org/10.1016/j.tsf.2004.10.051>
[^wiki-fg]: Wikipedia, *Forming gas*.
    <https://en.wikipedia.org/wiki/Forming_gas>
[^deal-1965]: B. E. Deal and A. S. Grove, "General Relationship for the
    Thermal Oxidation of Silicon", *Journal of Applied Physics*
    **36**(12), 3770–3778 (1965). <https://doi.org/10.1063/1.1713945>
[^yu-1999]: M.-C. Yu, S.-M. Jang, C. H. Diaz, C. H. Yu, S. C. Sun and
    M. S. Liang (TSMC), "Improvement of ultrathin gate oxide by a novel
    rapid thermal oxidation process with in-situ steam generation",
    *Proc. SPIE* **3881**, Microelectronic Device Technology III, 234
    (1999). <https://doi.org/10.1117/12.360557>
[^wiki-ash]: Wikipedia, *Plasma ashing*.
    <https://en.wikipedia.org/wiki/Plasma_ashing>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-argon]: Wikipedia, *Argon*.
    <https://en.wikipedia.org/wiki/Argon>
[^goodman-2008]: D. L. Goodman, "Effect of wafer bow on electrostatic
    chucking and back side gas cooling", *Journal of Applied Physics*
    **104**(12), 124902 (2008). <https://doi.org/10.1063/1.3043843>
[^wiki-helium]: Wikipedia, *Helium*.
    <https://en.wikipedia.org/wiki/Helium>
[^kriegler-1972]: R. J. Kriegler, Y. C. Cheng and D. R. Colton, "The
    Effect of HCl and Cl₂ on the Thermal Oxidation of Silicon",
    *Journal of The Electrochemical Society* **119**(3), 388 (1972).
    <https://doi.org/10.1149/1.2404208>
[^yoneda-1995]: K. Yoneda, K. Hagiwara, H. Oishi and Y. Todokoro, "The
    Dielectric Breakdown Characteristics of Thin Silicon Dioxide
    Prepared by trans-1,2-Dichloroethylene Added Oxidation", *Journal of
    The Electrochemical Society* **142**(12), 4304–4309 (1995).
    <https://doi.org/10.1149/1.2048502>
[^pat-torch-persys]: G. Drimer, L. Mendelovici and N. Borivker (Persys
    Technology), *Compact external torch assembly for semiconductor
    processing*, US 6,179,609 B1, filed 1999-07-02, granted 2001-01-30.
    <https://patents.google.com/patent/US6179609B1/en>
[^wiki-n2o]: Wikipedia, *Nitrous oxide*.
    <https://en.wikipedia.org/wiki/Nitrous_oxide>
[^hwang-1990]: H. Hwang, W. Ting, B. Maiti, D.-L. Kwong and J. Lee,
    "Electrical characteristics of ultrathin oxynitride gate dielectric
    prepared by rapid thermal oxidation of Si in N₂O", *Applied Physics
    Letters* **57**(10), 1010–1011 (1990).
    <https://doi.org/10.1063/1.103550>
[^hwang-1991]: H. Hwang, W. Ting, D.-L. Kwong and J. Lee, "A physical
    model for boron penetration through an oxynitride gate dielectric
    prepared by rapid thermal processing in N₂O", *Applied Physics
    Letters* **59**(13), 1581–1582 (1991).
    <https://doi.org/10.1063/1.106290>
[^tobin-1994]: P. J. Tobin, Y. Okada, S. A. Ajuria, V. Lakhotia, W. A.
    Feil and R. I. Hegde, "Furnace formation of silicon oxynitride thin
    dielectrics in nitrous oxide (N₂O): The role of nitric oxide (NO)",
    *Journal of Applied Physics* **75**(3), 1811–1817 (1994).
    <https://doi.org/10.1063/1.356374>
[^okada-1994]: Y. Okada, P. J. Tobin, K. G. Reid, R. I. Hegde, B. Maiti
    and S. A. Ajuria, "Furnace grown gate oxynitride using nitric oxide
    (NO)", *IEEE Transactions on Electron Devices* **41**(9), 1608–1613
    (1994). <https://doi.org/10.1109/16.310113>
[^kuehne-1997]: J. Kuehne, S. Hattangady, J. Piccirillo, G. C. Xing,
    G. E. Miner and D. Lopes, "Nitric Oxide Rapid Thermal Nitridation
    of Thin Gate Oxides", *MRS Proceedings* **470**, 381 (1997).
    <https://doi.org/10.1557/PROC-470-381>
[^wiki-no]: Wikipedia, *Nitric oxide*.
    <https://en.wikipedia.org/wiki/Nitric_oxide>
[^fujimura-1994]: S. Fujimura, M. T. Suzuki, K. Shinagawa and M.
    Nakamura, "Sodium contamination free ashing process using O₂+H₂O
    plasma downstream", *Journal of Vacuum Science & Technology B*
    **12**(4), 2409–2413 (1994). <https://doi.org/10.1116/1.587773>
[^lee-1981-corrosion]: W.-Y. Lee, J. M. Eldridge and G. C. Schwartz,
    "Reactive ion etching induced corrosion of Al and Al-Cu films",
    *Journal of Applied Physics* **52**(4), 2994–2999 (1981).
    <https://doi.org/10.1063/1.329043>
[^semi-c54]: SEMI, *SEMI C54 — Specification for Oxygen (O2)*, SEMI
    Standards store listing (revision C54-0624), accessed 2026-09-13.
    <https://store-us.semi.org/products/c05400-semi-c54-specification-for-oxygen>
[^semi-c58]: SEMI, *SEMI C58 — Specification for Hydrogen*, SEMI
    Standards store listing (revision C58-1116), accessed 2026-09-13.
    <https://store-us.semi.org/products/c05800-semi-c58-specification-for-hydrogen>
[^linde-semi]: Linde, *Supporting digitalization with gases for
    semiconductors*, industry page (Linde US), accessed 2026-09-13.
    <https://www.lindeus.com/industries/electronics/semiconductors>
[^semi-c3-20]: SEMI, *SEMI C3.20 — Specification for Helium (He), in
    Cylinders, 99.9995%*, SEMI Standards store listing (revision
    C3.20-0414 (Reapproved 0319)E), accessed 2026-09-13.
    <https://store-us.semi.org/products/c00320-semi-c3-20-specification-for-helium-he-in-cylinders-99-9995>
[^wiki-dce]: Wikipedia, *1,2-Dichloroethylene*.
    <https://en.wikipedia.org/wiki/1,2-Dichloroethylene>
[^wiki-praxair]: Wikipedia, *Praxair*.
    <https://en.wikipedia.org/wiki/Praxair>
[^wiki-airgas]: Wikipedia, *Airgas*.
    <https://en.wikipedia.org/wiki/Airgas>
[^wiki-versum]: Wikipedia, *Versum Materials*.
    <https://en.wikipedia.org/wiki/Versum_Materials>
[^epa-ghgrp-subpart-i]: U.S. Environmental Protection Agency,
    *Electronics Manufacturing: Subpart I, Greenhouse Gas Reporting
    Program*, information sheet, December 2024, accessed 2026-09-13.
    <https://www.epa.gov/system/files/documents/2024-04/i_electronics_infosheet_2024.pdf>
[^wiki-oxygen]: Wikipedia, *Oxygen*.
    <https://en.wikipedia.org/wiki/Oxygen>
[^green-2001]: M. L. Green, E. P. Gusev, R. Degraeve and E. L.
    Garfunkel, "Ultrathin (<4 nm) SiO₂ and Si–O–N gate dielectric layers
    for silicon microelectronics: Understanding the processing,
    structure, and physical and electrical limits", *Journal of Applied
    Physics* **90**(5), 2057–2121 (2001).
    <https://doi.org/10.1063/1.1385803>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
