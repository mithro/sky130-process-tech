(materials-index)=
# Materials and consumables

A wafer fab consumes far more than silicon. Every step of the SKY130
flow draws on gases, liquids, solids and replaceable hardware: the
furnace oxidations use oxygen and hydrogen, the plasma etches use
fluorine- and chlorine-bearing gases, each mask step uses resist and
developer, each metal level uses sputter targets and each polish uses
slurry and pads. This page is an index of those consumables. It
gathers what the step pages of this reference say about the resources
each step needs, sets it against what SkyWater Technology has said in
public about the materials at its Minnesota fab, and lists the films
the flow deposits with the thicknesses the process design kit (PDK)
gives. The physics and typical recipes are on the
{ref}`category pages <categories-index>`, and the tools that consume
these materials are indexed on the {ref}`machines page <machines-index>`.

## Consumable classes in a 200 mm, 130 nm fab

The classes below are those of a 200 mm fab of the 130 nm
generation[^txt-07][^txt-02] as the category pages of this reference
describe them; the main table assigns every material to one of them.

* **{ref}`Substrates and test wafers <material-substrates>`.** Polished prime wafers are ordered
  to SEMI M1[^semi-m1] and test and monitor wafers to SEMI
  M8[^semi-m8] ({ref}`category-substrate`).
* **{ref}`Process gases <material-process-gases>`.** Bulk nitrogen, oxygen, hydrogen, argon and
  helium; oxidation and nitridation additives (HCl or DCE, N₂O, NO,
  NH₃) ({ref}`category-oxidation`).
* **{ref}`Dopant gases and implant sources <material-dopant-sources>`.** Boron trifluoride, phosphine
  and arsine in cylinders, solid sources in vaporiser ovens, and the
  ion-source parts they wear out ({ref}`category-implant`). Phosphine
  also dopes the pre-metal glass.
* **{ref}`Precursors <material-precursors>`.** Silane, dichlorosilane, {term}`TEOS` and BTBAS for the
  silicon-based films, ozone as an oxidant for TEOS, and tungsten
  hexafluoride for the tungsten plugs
  ({ref}`category-deposition`). The flow described here has no
  {term}`atomic-layer-deposition <ALD>` step; SkyWater lists an ALD
  capability,
  "Atomic Layer Deposition" with "Oxides: SiO2, Al2O3, HfO2, TiO2,
  ZrO2",[^skw-01] and the {ref}`sky130B ReRAM <overview-sky130b-reram>`
  module is where ALD precursors enter (see *The sky130B ReRAM module*
  below).
* **{ref}`Etch and chamber-clean gases <material-etch-gases>`.** CF₄, CHF₃, C₂F₆, C₄F₈, SF₆, NF₃,
  Cl₂, BCl₃ and HBr, with O₂, N₂, Ar and He as additives and backside
  coolant ({ref}`category-etch`).
* **{ref}`Wet chemicals <material-wet-chemicals>`.** HF and buffered oxide etch ({term}`BOE`); the
  {term}`RCA cleans <RCA clean>` {term}`SC-1` and
  {term}`SC-2`;[^wiki-rca] sulphuric acid–hydrogen peroxide mixtures
  ({term}`SPM`, piranha);[^wiki-piranha] hot phosphoric acid for
  nitride;[^vgh-1967] HF/HNO₃ for silicon;[^schwartz-1976] isopropanol
  for drying; and amine or semi-aqueous post-etch residue removers of
  the EKC type ({ref}`category-strip`).
* **{ref}`Lithography materials <material-lithography-materials>`.** Positive i-line and KrF resists, bottom
  anti-reflective coatings ({term}`BARC`), {term}`HMDS`,
  tetramethylammonium hydroxide (TMAH) developer,[^wiki-tmah] edge-bead
  solvents, {term}`reticles <reticle>` and the
  light-source consumables of the exposure tools
  ({ref}`category-lithography`, {ref}`masks-index`).
* **{ref}`Sputter targets <material-sputter-targets>`.** Titanium (also
  {term}`sputtered reactively <reactive sputtering>` to TiN),
  aluminium–copper and titanium–tungsten ({ref}`category-deposition`).
* **{ref}`CMP consumables <material-cmp-consumables>`.** Oxide and tungsten slurries, pads,
  conditioners, carrier parts and {term}`post-CMP clean` chemistry
  ({ref}`category-cmp`).
* **{ref}`Anneal ambients <material-anneal-ambients>`.** Nitrogen and argon, controlled oxygen
  additions, ammonia, and {term}`forming gas` (hydrogen in nitrogen)
  for the {term}`alloy anneals <alloy anneal>` ({ref}`category-anneal`).
* **{ref}`Ultrapure water <material-ultrapure-water>`.** Rinses, dilution and polishing; CMP alone is
  one of a fab's largest water and waste-water users.[^txt-07]
* **{ref}`Hardware consumables and abatement <material-hardware-consumables>`.** Quartz furnace ware,
  chamber kits, lamps, probe cards, exhaust abatement and waste
  treatment ({ref}`category-test`).

## The public basis for SkyWater-specific materials

Four kinds of public source say something about the materials at
SkyWater's Bloomington fab. None of them ties a material to a step.

**SkyWater's capability list.** SkyWater's *Facilities &
Capabilities* page lists, tool by tool, some of the gases, chemistries
and films each tool is set up for;[^skw-01] the
{ref}`machines index <machines-index>` lists the steps to which the
step pages assign those tools. It is the only source that names
process chemistries tool by tool. It lists gases for the ashers,
the rapid thermal anneal ({term}`RTA`) tool and the poly/silicon etchers —
for example "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2", "Lam 9400
TCP, poly/nitride, HBr, CF4, SF6, O2" and "Iridia RF microwave, N2,
O2, H2, CF4, NH3, H2/N2, 40C-270C"; chemistries for the wet tools —
"Akrion Gamma Batch Wet Bench" with "Sulfuric, SC1, phosphoric, BOE,
spin or IPA dry", "DNS wet bench industry standard HF/SC1/SC2",
"EKS265, EKC270 solvents, CO2 injected DI" and "SEZ223, Davinci, HF,
DSP+HF, titration controlled"; implant species ("B11, BF2, P, As");
furnace processes ("LPCVD nitride, with NH3 and also DH3", "LPCVD
BTBAS low temp nitride", "H2 and forming gas alloy"); sputtered films
("Aluminum both pure and Cu doped", "TiW", "ESC TiN", "Imp TiN",
"Collimated Ti"); and polish processes ("oxide", "nitride",
"tungsten", "high selectivity tungsten", "Track ammonia
clean").[^skw-01] It gives no gases for the metal etchers, the
sputtering tools or the tungsten {term}`CVD` tool, and for the CVD tools names
only precursors, through its film names ("PECVD TEOS", "PECVD silane
oxide/nitride/oxynitride", "LPCVD BTBAS low temp nitride"). The
{ref}`public-sources inventory <references-public-sources>` notes that
the list describes the whole fab in the 2020s, including tools added
after the S8 flow was developed. The quotations on this page were
checked against the page as retrieved on 2026-09-13.

**SEC filings.** SkyWater's registration statement (S-1, 2021) and its
annual report for fiscal 2023 (10-K) each contain a "Raw materials"
paragraph. Both say that "These raw materials include silicon wafers,
high-purity compressed gases, high-purity metals for film deposition
processes, high-purity acid, base, and cleaning solutions for various
wet processing steps, and semiconductor grade photoresist and
developer for photolithography", and both name principal
suppliers:[^sec-01][^sec-02]

| Material | S-1 (filed 2021)[^sec-01] | 10-K for fiscal 2023[^sec-02] |
|----------|---------------------------|-------------------------------|
| Silicon wafers | "GlobalWafers Singapore Pte. Ltd."; "SEH America, subsidiary of Shin-Etsu Handotai, Ltd." | "Globalwafers Co. LTD."; "SEH America Inc, subsidiary of Shin-Etsu Handotai, Ltd." |
| Sputter targets | "Honeywell Electronic Materials, Inc. (metal sputter targets)" | "Honeywell Electronic Materials, Inc. (metal sputtering targets)"; "JX Metals USA, Inc. (metal sputtering targets)" |
| Gases | "Air Products & Chemicals, Inc. (bulk and specialty gases, chemicals)"; "Praxair, Inc. (bulk and specialty gases)" | "Linde, Inc. (bulk and specialty gases)"; "Airgas USA LLC (specialty gases)"; "EMD Performance Materials Corp (Versum) (specialty chemicals and gases)" |
| Chemicals | "KMG Chemicals, Inc. (chemicals)" (and Air Products, above) | "CMC Chemicals, Inc. (a subsidiary of Entegris) (process and chemical mechanical polishing chemicals)" (and EMD, above) |
| Photoresist | "The Dow Chemical Company (photoresist)"; "JSR Corporation (photoresist)"; "Tokyo Ohka Kogyo America, Inc. (photoresist)" | "Rohm and Haas EM LLC (a subsidiary of DuPont) (photoresist)"; "JSR Micro Inc. (photoresist)"; "FUJIFILM Electronic Materials USA, Inc. (photoresist)"; "Tokyo Ohka Kogyo America, Inc. (photoresist)" |
| Developer | "Air Products & Chemicals, Inc., Moses Lake (developer)" | "Moses Lake Industries Inc. (developer)" |

**Qualification reports and the PDK.** Cypress Semiconductor's
qualification reports for products made at the same fab give the
composition and thickness of some films — the Ti/Al–Cu/TiW metal
stacks, the Ti/TiN/AlCu/Ti/TiN stack that replaced them at the fab in
2013–2014 and the TEOS/nitride
{term}`passivation`[^cyp-qtp-113005][^cyp-qtp-123907][^cyp-qtp-014807]
(which stack SKY130 carries at each level is not public:
{ref}`overview-metal-cap`)
— and the PDK documentation gives thicknesses and permittivities for
the SKY130 stack.[^pdk-03][^pdk-04] These are the sources of the
{ref}`films table <materials-films>` below.

**The EPA greenhouse-gas record.** The U.S. Environmental Protection
Agency's Greenhouse Gas Reporting Program lists the Bloomington facility
(ID 1000354, "SKYWATER TECHNOLOGY FOUNDRY INC" in the records for
2010–2013 and "SKYWATER TECHNOLOGY INC" from 2014; names later applied to years when
the parent company field reads Cypress Semiconductor, to 2016) as
reporting under
subpart I, electronics manufacturing, in each year from 2011 to 2023;
its subpart I entries include N₂O, SF₆ and NF₃ in every one of those
years, alongside perfluorocarbons, hydrofluorocarbons and other
fluorinated gases.[^epa-ghgrp-skywater] The record has three limits.
The two tables cited give CO₂-equivalent totals by gas or gas group, so
the perfluorocarbon and hydrofluorocarbon totals do not show which of
CF₄, C₂F₆, CHF₃ or the other gases of those groups is
emitted.[^epa-ghgrp-skywater] A facility reports each fluorinated gas
"including each input gas and each by-product
gas",[^epa-ghgrp-subpart-i] so a reported emission does not by itself
show that the gas is supplied to a tool. And the cited tables name no tools,
processes, steps or abatement systems.[^epa-ghgrp-skywater] The
{ref}`process gases <material-process-gases>` and
{ref}`etch and chamber-clean gases <material-etch-gases>` pages discuss
what the record shows for their classes.

## How to read the index

* **Typical and SkyWater-evidenced materials.** The *Role* column
  gives what the step pages describe, which is in most cases
  industry-typical practice for a 200 mm, 130 nm fab. The *Public
  SkyWater evidence* column quotes the capability list, a filing or a
  qualification report where one names the material, or the
  capability it serves, adds the EPA greenhouse-gas record for the
  gases it names, and otherwise reads *typical (not listed)*. A
  quotation or record shows that a material or capability exists at
  the fab; it does not show that a given SKY130 step uses it.
* **Steps column.** A step is listed when the *Resources required*
  section of its page names the material (or, for an implant, names
  its source-support gases or source consumables). The list was
  compiled by a script and checked by reading each section; it follows
  the resources sections even where a page's recipe outline mentions
  more. Steps are given by code; the {ref}`steps-index` gives their
  numbers. *All except* lists the steps whose resources section does not
  name the material. Components of the post-CMP clean mixtures (dilute
  HF, NH₄OH, TMAH) are indexed only under *Post-CMP clean chemistry*,
  H₂/N₂ only under forming gas, and liquid nitrogen for cryopumps only
  under the ion-source row; cooling water is indexed only for the {term}`RTP`
  steps, not for the implanters' platen cooling, and wet-bench hardware
  (bath heaters, quartz tanks) is not indexed.
* **Coverage.** Each of the 171 steps of the step list[^steps-sheet]
  has a page with a non-empty *Resources required* section, and each
  appears in at least one row.
* **Keys.** The first column gives each row a short, stable key. Class
  pages name the rows they cover by key, so rewording a cell does not
  break them.
* **Class pages.** Each consumable class above is to have a page of its
  own, describing the class, representative materials and grades, what
  SkyWater lists, the steps that use it, supply and safety, and
  process-integration notes. Every row belongs to exactly one class page,
  the one for the row's primary role, which is the first term of its
  *Class* cell; a second term (such as "anneal ambient" on the nitrogen
  row) names a secondary role, whose page may discuss the row but does
  not list it. The table below assigns every row by key. A row owned by
  a written page has a *Class* cell that links the page, and
  `tools/check_materials.py` checks that each page's list of rows and
  steps matches this index.

| Consumable class | Page | Rows owned (keys) |
|------------------|------|-------------------|
| Substrates and test wafers | {ref}`substrates <material-substrates>` | `si-wafers`, `test-wafers` |
| Process gases | {ref}`process-gases <material-process-gases>` | `n2`, `o2`, `h2`, `ar`, `he`, `water-vapour`, `hcl-dce`, `n2o-no` |
| Dopant gases and implant sources | {ref}`dopant-sources <material-dopant-sources>` | `ph3`, `bf3`, `ash3`, `indium`, `ion-source` |
| Precursors | {ref}`precursors <material-precursors>` | `nh3`, `sih4`, `dcs`, `teos`, `btbas`, `sif4`, `wf6`, `ozone` |
| Etch and chamber-clean gases | {ref}`etch-gases <material-etch-gases>` | `cf4`, `chf3`, `c2f6`, `etch-additives`, `sf6`, `nf3`, `hbr`, `cl2`, `bcl3` |
| Wet chemicals | {ref}`wet-chemicals <material-wet-chemicals>` | `hf`, `boe`, `sc1`, `sc2`, `spm`, `h3po4`, `h2o2`, `hno3`, `ozonated-water`, `ipa`, `residue-removers` |
| Lithography materials | {ref}`lithography-materials <material-lithography-materials>` | `i-line-resist`, `krf-resist`, `arc`, `hmds`, `tmah`, `ebr-solvents`, `reticles`, `exposure-consumables` |
| Sputter targets | {ref}`sputter-targets <material-sputter-targets>` | `ti-target`, `alcu-target`, `tiw-target` |
| CMP consumables | {ref}`cmp-consumables <material-cmp-consumables>` | `post-cmp-clean`, `oxide-slurry`, `w-slurry`, `cmp-pads` |
| Anneal ambients | {ref}`anneal-ambients <material-anneal-ambients>` | `forming-gas` (nitrogen, argon, oxygen and ammonia, also used as anneal ambients, belong to process gases and precursors) |
| Ultrapure water | {ref}`ultrapure-water <material-ultrapure-water>` | `upw` |
| Hardware consumables and abatement | {ref}`hardware-consumables <material-hardware-consumables>` | `furnace-ware`, `chamber-parts`, `rtp-parts`, `abatement`, `probe-cards` |

```{toctree}
:maxdepth: 1

wet-chemicals
lithography-materials
sputter-targets
substrates
cmp-consumables
anneal-ambients
ultrapure-water
hardware-consumables
process-gases
dopant-sources
precursors
etch-gases
```

(materials-table)=
## Materials index
| Key | Material | Class | Role in SKY130 steps | Public SkyWater evidence | Steps whose Resources section names it |
|-----|----------|-------|----------------------|--------------------------|----------------------------------------|
| `si-wafers` | Silicon wafers, 200 mm, p-type, polished bulk | {ref}`Substrate <material-substrates>` | Starting material of the flow. | "200 mm equipment";[^skw-01] suppliers in both filings (table above).[^sec-01][^sec-02] | {ref}`SMAT <step-001>` |
| `test-wafers` | Test and monitor wafers (SEMI M8 class) | {ref}`Substrate <material-substrates>` | Thickness, {term}`sheet-resistance <sheet resistance>`, particle, rate and selectivity monitors; RTP thermocouple wafers; CD, {term}`overlay` and tester reference wafers. | typical (not listed) | {ref}`BOX <step-002>`, {ref}`ISONIT <step-003>`, {ref}`STIE <step-006>`, {ref}`DNI <step-008>`, {ref}`LINOX <step-010>`, {ref}`LVTNI <step-015>`, {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`, {ref}`LVTPI <step-020>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`, {ref}`RTAI <step-034>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`NCHI <step-045>`, {ref}`LVGOX <step-047>`, {ref}`SAGD <step-048>`, {ref}`P1I <step-050>`, {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`BFR <step-060>`, {ref}`P1M <step-061>`, {ref}`P1ME <step-062>`, {ref}`IOX45 <step-063>`, {ref}`ASTI <step-065>`, {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`, {ref}`TIPRTAD <step-075>`, {ref}`SPNIT <step-076>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`SPOX <step-080>`, {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`, {ref}`RTAD <step-088>`, {ref}`PSG <step-089>`, {ref}`CMPP <step-090>`, {ref}`NCAPOX <step-091>`, {ref}`RTAD2 <step-092>`, {ref}`LICM1E <step-094>`, {ref}`SACETCH <step-095>`, {ref}`ALLY1 <step-096>`, {ref}`TI/TIN1 <step-097>`, {ref}`CSIL <step-098>`, {ref}`WDEP <step-099>`, {ref}`WCMPLI <step-100>`, {ref}`LITIN <step-101>`, {ref}`LI1ME <step-103>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`CMPL <step-106>`, {ref}`CTME <step-108>`, {ref}`TIN2 <step-109>`, {ref}`WDEP2 <step-110>`, {ref}`TIAL6 <step-112>`, {ref}`MM1E <step-114>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`VIME <step-119>`, {ref}`TIN3 <step-120>`, {ref}`WDEP3 <step-121>`, {ref}`TIAL12 <step-123>`, {ref}`MM2E <step-125>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`VIM2E <step-130>`, {ref}`TIN4 <step-131>`, {ref}`WDEP4 <step-132>`, {ref}`WTIAL3 <step-134>`, {ref}`CAPILD <step-135>`, {ref}`CAPTIW1 <step-136>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`VIM3E <step-145>`, {ref}`TIN5 <step-146>`, {ref}`WDEP5 <step-147>`, {ref}`WTIAL4 <step-149>`, {ref}`CAPILD2 <step-150>`, {ref}`CAPTIW2 <step-151>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`VIM4E <step-160>`, {ref}`WTIAL5 <step-161>`, {ref}`MM5E <step-163>`, {ref}`NFUSOX <step-164>`, {ref}`NSME <step-166>`, {ref}`NTSD <step-167>`, {ref}`PDME <step-169>`, {ref}`ALLY <step-170>`, {ref}`HPETEST <step-171>` |
| `n2` | Nitrogen (N₂) | {ref}`Bulk gas; anneal ambient <material-process-gases>` | Purge, drying and vent gas; anneal ambient; ash gas; reactive gas for TiN; etch and CVD diluent; CDA/N₂ lamp cooling. | "N2 anneal to 1150C"; "Ag Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C"; N2 on the GaSonics and Iridia asher entries.[^skw-01] | all except {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`CMPNIT <step-012>`, {ref}`NWI2 <step-019>`, {ref}`LVTPI <step-020>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`, {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`, {ref}`PSG <step-089>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`NILD2 <step-105>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`NILD5 <step-141>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`NILD6 <step-156>`, {ref}`CMPM4 <step-157>`, {ref}`HPETEST <step-171>` |
| `o2` | Oxygen (O₂) | {ref}`Bulk gas; oxidant <material-process-gases>` | Dry oxidation and pyrogenic steam; ash; etch additive; oxidant for HDP and {term}`PECVD` oxides; minor RTA addition. | "dry oxidation to 1150C"; "wet oxidation to 1150C"; O2 in the Heatpulse, asher and all three poly/silicon etcher entries.[^skw-01] | {ref}`BOX <step-002>`, {ref}`STINITE <step-005>`, {ref}`STIE <step-006>`, {ref}`DNIS <step-009>`, {ref}`LINOX <step-010>`, {ref}`FILOX <step-011>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`RTAI <step-034>`, {ref}`TUNARCE <step-036>`, {ref}`TUNME <step-039>`, {ref}`ONO <step-040>`, {ref}`ONOME <step-042>`, {ref}`GOX100 <step-043>`, {ref}`GOXETCH <step-046>`, {ref}`LVGOX <step-047>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`P1ME <step-062>`, {ref}`IOX45 <step-063>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`TIPRTAD <step-075>`, {ref}`SPNIT <step-076>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`SPOX <step-080>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`RTAD <step-088>`, {ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`, {ref}`LICM1E <step-094>`, {ref}`SACETCH <step-095>`, {ref}`LI1ME <step-103>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`VIM2E <step-130>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`VIM3E <step-145>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`VIM4E <step-160>`, {ref}`MM5E <step-163>`, {ref}`NFUSOX <step-164>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>` |
| `h2` | Hydrogen (H₂) | {ref}`Bulk gas; reductant <material-process-gases>` | Pyrogenic or {term}`radical oxidation`; bulk reduction of WF₆; alloy anneal; implant-source co-gas; possible {term}`PVD` pre-clean. | "H2 and forming gas alloy"; "Iridia RF microwave, N2, O2, H2, CF4, NH3, H2/N2, 40C-270C".[^skw-01] | {ref}`BOX <step-002>`, {ref}`DNI <step-008>`, {ref}`LINOX <step-010>`, {ref}`LVTNI <step-015>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`ALLY1 <step-096>`, {ref}`WDEP <step-099>`, {ref}`TIN2 <step-109>`, {ref}`WDEP2 <step-110>`, {ref}`TIN3 <step-120>`, {ref}`WDEP3 <step-121>`, {ref}`TIN4 <step-131>`, {ref}`WDEP4 <step-132>`, {ref}`TIN5 <step-146>`, {ref}`WDEP5 <step-147>`, {ref}`ALLY <step-170>` |
| `forming-gas` | Forming gas (H₂ in N₂) | {ref}`Anneal and ash ambient <material-anneal-ambients>` | Implant-crust and post-etch ash; alloy anneals at {ref}`ALLY1 <step-096>` and {ref}`ALLY <step-170>` ("5% H2 in N2" is the typical formulation[^wiki-fg]). | "H2 and forming gas alloy"; Iridia "H2/N2"; "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to 250C".[^skw-01] | {ref}`STIE <step-006>`, {ref}`DNIS <step-009>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`TUNME <step-039>`, {ref}`ONOME <step-042>`, {ref}`GOXETCH <step-046>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`P1ME <step-062>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`NPCME <step-079>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`LICM1E <step-094>`, {ref}`SACETCH <step-095>`, {ref}`ALLY1 <step-096>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`, {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>`, {ref}`ALLY <step-170>` |
| `ar` | Argon (Ar) | {ref}`Bulk gas; anneal ambient <material-process-gases>` | Sputter gas and sputter-etch pre-clean; {term}`HDP-CVD`; etch diluent; RTA and furnace ambient; implant-source support gas. | "Ar anneal to 1150C"; Ar in the Heatpulse entry.[^skw-01] | {ref}`STINITE <step-005>`, {ref}`DNI <step-008>`, {ref}`FILOX <step-011>`, {ref}`LVTNI <step-015>`, {ref}`RTAI <step-034>`, {ref}`TUNARCE <step-036>`, {ref}`ONOME <step-042>`, {ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`, {ref}`POC <step-059>`, {ref}`P1ME <step-062>`, {ref}`IOX45 <step-063>`, {ref}`ASTI <step-065>`, {ref}`TIPRTAD <step-075>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`, {ref}`RTAD <step-088>`, {ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`, {ref}`RTAD2 <step-092>`, {ref}`LICM1E <step-094>`, {ref}`TI/TIN1 <step-097>`, {ref}`CSIL <step-098>`, {ref}`WDEP <step-099>`, {ref}`LITIN <step-101>`, {ref}`LI1ME <step-103>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`CTME <step-108>`, {ref}`TIN2 <step-109>`, {ref}`WDEP2 <step-110>`, {ref}`TIAL6 <step-112>`, {ref}`MM1E <step-114>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`VIME <step-119>`, {ref}`TIN3 <step-120>`, {ref}`WDEP3 <step-121>`, {ref}`TIAL12 <step-123>`, {ref}`MM2E <step-125>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`VIM2E <step-130>`, {ref}`TIN4 <step-131>`, {ref}`WDEP4 <step-132>`, {ref}`WTIAL3 <step-134>`, {ref}`CAPTIW1 <step-136>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`VIM3E <step-145>`, {ref}`TIN5 <step-146>`, {ref}`WDEP5 <step-147>`, {ref}`WTIAL4 <step-149>`, {ref}`CAPTIW2 <step-151>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`VIM4E <step-160>`, {ref}`WTIAL5 <step-161>`, {ref}`MM5E <step-163>`, {ref}`NFUSOX <step-164>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>` |
| `he` | Helium (He) | {ref}`Bulk gas <material-process-gases>` | Backside wafer cooling in etch, CVD, PVD and implant tools; TEOS carrier and CVD diluent. | typical (not listed) | {ref}`STINITE <step-005>`, {ref}`STIE <step-006>`, {ref}`DNI <step-008>`, {ref}`FILOX <step-011>`, {ref}`TUNARCE <step-036>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`ONOME <step-042>`, {ref}`NCHI <step-045>`, {ref}`P1I <step-050>`, {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`, {ref}`POC <step-059>`, {ref}`P1ME <step-062>`, {ref}`ASTI <step-065>`, {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`SPOX <step-080>`, {ref}`2PSDI <step-083>`, {ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`, {ref}`LICM1E <step-094>`, {ref}`TI/TIN1 <step-097>`, {ref}`LITIN <step-101>`, {ref}`LI1ME <step-103>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`VIM2E <step-130>`, {ref}`CAPILD <step-135>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`VIM3E <step-145>`, {ref}`CAPILD2 <step-150>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`VIM4E <step-160>`, {ref}`MM5E <step-163>`, {ref}`NFUSOX <step-164>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>` |
| `water-vapour` | Water vapour (H₂O) | {ref}`Ash and passivation additive <material-process-gases>` | Ash additive after high-dose implants ({ref}`PRIS <step-054>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`); post-etch corrosion passivation of Al–Cu and TiN. | typical (not listed) | {ref}`PRIS <step-054>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`LI1ME <step-103>`, {ref}`MM1E <step-114>`, {ref}`MM2E <step-125>`, {ref}`MM3E <step-140>`, {ref}`MM4E <step-155>`, {ref}`MM5E <step-163>` |
| `hcl-dce` | HCl or trans-1,2-dichloroethylene (DCE) | {ref}`Oxidation additive <material-process-gases>` | Chlorine source for {term}`gettering` in furnace oxidations. | typical (not listed) | {ref}`LINOX <step-010>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`, {ref}`IOX45 <step-063>` |
| `n2o-no` | Nitrous oxide (N₂O), nitric oxide (NO) | {ref}`Oxidant; nitriding gas <material-process-gases>` | Nitrided or {term}`oxynitride` gate and {term}`liner` oxides; {term}`ONO` oxynitride layers; oxidant for PECVD silane oxide and oxynitride. | The capability list names neither gas but has "Nitrided gate oxide" and "PECVD silane oxide/nitride/oxynitride, C1";[^skw-01] N₂O emissions reported to the EPA for the Bloomington facility in each year 2011–2023, process not stated.[^epa-ghgrp-skywater] | {ref}`LINOX <step-010>`, {ref}`ONO <step-040>`, {ref}`LVGOX <step-047>`, {ref}`POC <step-059>`, {ref}`IOX45 <step-063>`, {ref}`SPOX <step-080>`, {ref}`NCAPOX <step-091>`, {ref}`NCAPOX3 <step-117>`, {ref}`NCAPOX4 <step-128>`, {ref}`CAPILD <step-135>`, {ref}`NCAPOX5 <step-143>`, {ref}`CAPILD2 <step-150>`, {ref}`NCAPOX6 <step-158>`, {ref}`NFUSOX <step-164>` |
| `nh3` | Ammonia (NH₃) | {ref}`Precursor; nitriding gas <material-precursors>` | {term}`LPCVD`, BTBAS and PECVD nitride; PECVD oxynitride; oxide nitridation; possible ash additive. | "LPCVD nitride, with NH3 and also DH3"; NH3 in the Heatpulse and Iridia entries.[^skw-01] | {ref}`ISONIT <step-003>`, {ref}`LINOX <step-010>`, {ref}`ONO <step-040>`, {ref}`LVGOX <step-047>`, {ref}`PRIS <step-054>`, {ref}`GATENIT <step-058>`, {ref}`SPNIT <step-076>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`LINIT <step-104>`, {ref}`CAPILD <step-135>`, {ref}`CAPILD2 <step-150>`, {ref}`NTSD <step-167>` |
| `sih4` | Silane (SiH₄) | {ref}`Precursor <material-precursors>` | HDP-CVD oxide and {term}`PSG`; PECVD oxide, nitride and oxynitride; LPCVD amorphous-silicon gate; tungsten {term}`nucleation <nucleation layer>`. | Named only in film names: "PECVD silane oxide/nitride/oxynitride, C1", "LPCVD silane oxide"; the gate film is "LPCVD polysilicon (undoped), both amorphous and crystalline".[^skw-01] | {ref}`FILOX <step-011>`, {ref}`SAGD <step-048>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`SPNIT <step-076>`, {ref}`SPOX <step-080>`, {ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`, {ref}`WDEP <step-099>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`WDEP2 <step-110>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`WDEP3 <step-121>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`WDEP4 <step-132>`, {ref}`CAPILD <step-135>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`WDEP5 <step-147>`, {ref}`CAPILD2 <step-150>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`NFUSOX <step-164>`, {ref}`NTSD <step-167>` |
| `dcs` | Dichlorosilane (SiH₂Cl₂) | {ref}`Precursor <material-precursors>` | LPCVD nitride (isolation, gate cap, {term}`spacer` options); ONO trapping layer. | Not named; the LPCVD nitride entry reads "with NH3 and also DH3" and the list has "LPCVD oxide/nitride/oxide".[^skw-01] | {ref}`ISONIT <step-003>`, {ref}`ONO <step-040>`, {ref}`GATENIT <step-058>`, {ref}`SPNIT <step-076>` |
| `teos` | TEOS (tetraethyl orthosilicate) | {ref}`Precursor (liquid) <material-precursors>` | PECVD cap, spacer, inter-level and fuse oxides; TEOS route for PSG. | "PECVD TEOS, C2 and Producer" with "low temp options";[^skw-01] a 2005 Cypress Fab 4 report gives the passivation as "1000Å TEOS / 9000Å PECVD Nitride".[^cyp-qtp-014807] | {ref}`POC <step-059>`, {ref}`SPOX <step-080>`, {ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`, {ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`NFUSOX <step-164>` |
| `btbas` | BTBAS (bis(tertiary-butylamino)silane) | {ref}`Precursor (liquid) <material-precursors>` | Low-temperature LPCVD nitride option for the spacer and the {term}`local-interconnect <local interconnect>` cap. | "LPCVD BTBAS low temp nitride".[^skw-01] | {ref}`SPNIT <step-076>`, {ref}`LINIT <step-104>` |
| `sif4` | Silicon tetrafluoride (SiF₄) | {ref}`Precursor <material-precursors>` | Fluorinated oxide option for the metal-1/metal-2 and metal-2/metal-3 dielectrics. | typical (not listed) | {ref}`NILD3 <step-115>`, {ref}`NILD4 <step-126>` |
| `wf6` | Tungsten hexafluoride (WF₆), with SiH₄ or B₂H₆ nucleation | {ref}`Precursor <material-precursors>` | CVD tungsten plugs in the local-interconnect and metal contacts and in vias 1–3. | Precursor not named; "Lam/Novellus PECVD Tungsten" with "plug fill" and "PNL option for high aspect ratio (up to 10:1)".[^skw-01] | {ref}`WDEP <step-099>`, {ref}`WDEP2 <step-110>`, {ref}`WDEP3 <step-121>`, {ref}`WDEP4 <step-132>`, {ref}`WDEP5 <step-147>` |
| `ozone` | Ozone (O₃) for TEOS oxide deposition | {ref}`Precursor; oxidant <material-precursors>` | O₂/O₃ oxidant for the TEOS PSG route. | typical (not listed) | {ref}`PSG <step-089>` |
| `ph3` | Phosphine (PH₃), solid phosphorus; TMPO | {ref}`Dopant source <material-dopant-sources>` | Phosphorus implants (deep N-well, N-well, poly and source/drain; the phosphorus option for the threshold, channel and depletion implants); phosphorus for HDP or TEOS PSG. | Species "P" on both GSD implanters ("B11, BF2, P, As"); "Lam/Novellus High Density Plasma (HDP) doped and phos doped with sputter etch".[^skw-01] | {ref}`DNI <step-008>`, {ref}`LVTNI <step-015>`, {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`, {ref}`LVTPI <step-020>`, {ref}`PCHI <step-023>`, {ref}`DEPI <step-038>`, {ref}`P1I <step-050>`, {ref}`NSDI <step-086>`, {ref}`PSG <step-089>` |
| `bf3` | Boron trifluoride (BF₃), solid boron source | {ref}`Dopant source <material-dopant-sources>` | B⁺ and BF₂⁺ for wells, threshold adjusts, halos, resistor and P+ source/drain implants. | Species "B11, BF2" on all three implanter entries, e.g. "Axcelis 8250 Mid current B11, BF2, As, ESC chuck, E shower, 1e11 to 1e14, 0-60 deg tilt".[^skw-01] | {ref}`LVTNI <step-015>`, {ref}`LVTPI <step-020>`, {ref}`PNCHI <step-024>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`, {ref}`PTSI <step-037>`, {ref}`NCHI <step-045>`, {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`, {ref}`BHI <step-066>`, {ref}`LDBHI <step-073>`, {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>` |
| `ash3` | Arsine (AsH₃), solid arsenic | {ref}`Dopant source <material-dopant-sources>` | Arsenic for tips, depletion and threshold options, poly and N+ source/drain implants. | Species "As" on all three implanter entries.[^skw-01] | {ref}`LVTNI <step-015>`, {ref}`LVTPI <step-020>`, {ref}`PCHI <step-023>`, {ref}`DEPI <step-038>`, {ref}`P1I <step-050>`, {ref}`ASTI <step-065>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`NSDI <step-086>` |
| `indium` | Indium (solid source) | {ref}`Dopant source <material-dopant-sources>` | Alternative heavy p-type species discussed for threshold and {term}`punch-through` implants. | Not listed; no implanter entry names indium.[^skw-01] | {ref}`LVTNI <step-015>`, {ref}`PTSI <step-037>` |
| `ion-source` | Ion-source and beam-line consumables: Ar, Xe or H₂ support gases, filaments or cathodes, arc-chamber liners, electrodes, disc pads, flood-gun parts, LN₂ for cryopumps | {ref}`Implant-source hardware; support gas <material-dopant-sources>` | Consumed by every implant; fluorinated species wear sources faster (Axcelis notes "source operating costs especially with fluorinated species"[^axcelis-gsd-page]). | typical (not listed) | {ref}`DNI <step-008>`, {ref}`LVTNI <step-015>`, {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`, {ref}`LVTPI <step-020>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`NCHI <step-045>`, {ref}`P1I <step-050>`, {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`, {ref}`ASTI <step-065>`, {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`, {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>` |
| `cf4` | Carbon tetrafluoride (CF₄) | {ref}`Etch gas; clean gas <material-etch-gases>` | Nitride and oxide etch, breakthrough and cap-open steps; ash additive; CF₄/O₂ PECVD chamber clean. | CF4 on "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2", "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6, O2", "Lam 4400, HBr, Cl2, C2F6, CF4, SF6, O2" and the Iridia and Mattson ashers.[^skw-01] | {ref}`STINITE <step-005>`, {ref}`STIE <step-006>`, {ref}`DNIS <step-009>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`TUNARCE <step-036>`, {ref}`ONOME <step-042>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`P1ME <step-062>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`SPNIT <step-076>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`SPOX <step-080>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`LICM1E <step-094>`, {ref}`LI1ME <step-103>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`VIM3E <step-145>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`VIM4E <step-160>`, {ref}`MM5E <step-163>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>` |
| `chf3` | Trifluoromethane (CHF₃) | {ref}`Etch gas <material-etch-gases>` | Oxide and nitride etch, ARC open, sidewall passivation in metal etch. | CHF3 on the DPSII entry only.[^skw-01] | {ref}`STINITE <step-005>`, {ref}`TUNARCE <step-036>`, {ref}`ONOME <step-042>`, {ref}`P1ME <step-062>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`LICM1E <step-094>`, {ref}`LI1ME <step-103>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`VIM3E <step-145>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`VIM4E <step-160>`, {ref}`MM5E <step-163>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>` |
| `c2f6` | Hexafluoroethane (C₂F₆) | {ref}`Etch gas <material-etch-gases>` | Contact, via and seal-ring oxide etches. | C2F6 on the Lam 4400 entry only.[^skw-01] | {ref}`LICM1E <step-094>`, {ref}`CTME <step-108>`, {ref}`VIME <step-119>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`, {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>` |
| `etch-additives` | C₄F₈, CO, CH₃F, CH₂F₂, CH₄ | {ref}`Etch additive <material-etch-gases>` | Polymerising, selectivity and passivation additives: C₄F₈ and CO in contact and via etches; CH₃F or CH₂F₂ for nitride selectivity; CH₄ in metal etch. | typical (not listed) | {ref}`SPE <step-077>`, {ref}`LICM1E <step-094>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>`, {ref}`CAPME <step-138>`, {ref}`VIM3E <step-145>`, {ref}`CAP2ME <step-153>`, {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>` |
| `sf6` | Sulphur hexafluoride (SF₆) | {ref}`Etch gas; clean gas <material-etch-gases>` | Nitride, TiN, TiW and pad etches; SF₆/O₂ chamber clean. | SF6 on the Lam 9400 and Lam 4400 entries;[^skw-01] SF₆ emissions (input or by-product gas) reported to the EPA for the Bloomington facility, no tool or process stated.[^epa-ghgrp-skywater][^epa-ghgrp-subpart-i] | {ref}`STINITE <step-005>`, {ref}`STIE <step-006>`, {ref}`ONOME <step-042>`, {ref}`P1ME <step-062>`, {ref}`SPE <step-077>`, {ref}`LI1ME <step-103>`, {ref}`MM1E <step-114>`, {ref}`MM2E <step-125>`, {ref}`CAPME <step-138>`, {ref}`CAP2ME <step-153>`, {ref}`PDME <step-169>` |
| `nf3` | Nitrogen trifluoride (NF₃) | {ref}`Clean gas; etch gas <material-etch-gases>` | Remote- or in-situ-plasma clean of HDP, PECVD and tungsten CVD chambers and etchers; nitride-tube clean option. | NF3 on the DPSII entry;[^skw-01] NF₃ emissions (input or by-product gas) reported to the EPA for the Bloomington facility, no tool or process stated.[^epa-ghgrp-skywater][^epa-ghgrp-subpart-i] | {ref}`ISONIT <step-003>`, {ref}`STINITE <step-005>`, {ref}`STIE <step-006>`, {ref}`FILOX <step-011>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`P1ME <step-062>`, {ref}`SPNIT <step-076>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`SPOX <step-080>`, {ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`, {ref}`LICM1E <step-094>`, {ref}`WDEP <step-099>`, {ref}`LI1ME <step-103>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`CTME <step-108>`, {ref}`WDEP2 <step-110>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`VIME <step-119>`, {ref}`WDEP3 <step-121>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`VIM2E <step-130>`, {ref}`WDEP4 <step-132>`, {ref}`CAPILD <step-135>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`VIM3E <step-145>`, {ref}`WDEP5 <step-147>`, {ref}`CAPILD2 <step-150>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`VIM4E <step-160>`, {ref}`NFUSOX <step-164>`, {ref}`NTSD <step-167>` |
| `hbr` | Hydrogen bromide (HBr), Br₂ | {ref}`Etch gas <material-etch-gases>` | Silicon trench and gate etches; organic ARC open; bromine option for the {term}`MiM <MiM capacitor>` plate etches; optional silicon-selective landing step in the ONO etch. | "HBR" on the DPSII entry; "HBr" on the Lam 9400 and 4400 entries.[^skw-01] | {ref}`STIE <step-006>`, {ref}`TUNARCE <step-036>`, {ref}`ONOME <step-042>`, {ref}`P1ME <step-062>`, {ref}`CAPME <step-138>`, {ref}`CAP2ME <step-153>` |
| `cl2` | Chlorine (Cl₂) | {ref}`Etch gas <material-etch-gases>` | Trench and gate etches; Al–Cu, TiN and TiW metal etches. | Cl2 on the DPSII and Lam 4400 entries; the metal etchers are listed without gases ("Lam 9600, Al, TiW, TiN, Pt").[^skw-01] | {ref}`STIE <step-006>`, {ref}`P1ME <step-062>`, {ref}`LI1ME <step-103>`, {ref}`MM1E <step-114>`, {ref}`MM2E <step-125>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`MM5E <step-163>` |
| `bcl3` | Boron trichloride (BCl₃) | {ref}`Etch gas <material-etch-gases>` | Al–Cu and TiN etches; MiM plate etch. | typical (not listed) | {ref}`LI1ME <step-103>`, {ref}`MM1E <step-114>`, {ref}`MM2E <step-125>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`MM5E <step-163>` |
| `hf` | Hydrofluoric acid (49 % and dilute HF) | {ref}`Wet chemical <material-wet-chemicals>` | Native-oxide strip and HF-last pre-clean; tunnel-window and gate-oxide etches; ONO bottom-oxide clear; nitride-strip breakthrough; backside film removal; pre-metal contact clean; nitride-tube clean option; post-etch clean after the trench etch. | "DNS wet bench industry standard HF/SC1/SC2" with "dilute HF-last with IPA dry"; "SEZ223, Davinci, HF, DSP+HF, titration controlled".[^skw-01] | {ref}`SMAT <step-001>`, {ref}`BOX <step-002>`, {ref}`ISONIT <step-003>`, {ref}`STIE <step-006>`, {ref}`LINOX <step-010>`, {ref}`NS19 <step-013>`, {ref}`PWDEIS <step-033>`, {ref}`TUNME <step-039>`, {ref}`ONOME <step-042>`, {ref}`GOXETCH <step-046>`, {ref}`BFR <step-060>`, {ref}`SACETCH <step-095>` |
| `boe` | Buffered oxide etch (NH₄F/HF), with surfactant | {ref}`Wet chemical <material-wet-chemicals>` | Tunnel-window and thick-gate-oxide etches; ONO bottom-oxide clear; pre-clean and sacrificial-etch alternatives. | "Akrion Gamma Batch Wet Bench": "Sulfuric, SC1, phosphoric, BOE, spin or IPA dry".[^skw-01] | {ref}`TUNME <step-039>`, {ref}`ONOME <step-042>`, {ref}`GOX100 <step-043>`, {ref}`GOXETCH <step-046>`, {ref}`SACETCH <step-095>` |
| `sc1` | SC-1 (NH₄OH + H₂O₂ + H₂O) | {ref}`Wet chemical <material-wet-chemicals>` | Particle and organic clean in pre-furnace, post-strip and post-etch sequences. | "SC1" on the Akrion, DNS and FSI Mercury entries.[^skw-01] | {ref}`SMAT <step-001>`, {ref}`BOX <step-002>`, {ref}`STIE <step-006>`, {ref}`DNIS <step-009>`, {ref}`LINOX <step-010>`, {ref}`NS19 <step-013>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`TUNME <step-039>`, {ref}`GOX100 <step-043>`, {ref}`GOXETCH <step-046>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`P1ME <step-062>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`SACETCH <step-095>` |
| `sc2` | SC-2 (HCl + H₂O₂ + H₂O) | {ref}`Wet chemical <material-wet-chemicals>` | Metal-ion clean before furnace steps and anneals. | "SC2" only on the DNS and FSI Mercury entries ("HF/SC1/SC2").[^skw-01] | {ref}`SMAT <step-001>`, {ref}`BOX <step-002>`, {ref}`DNIS <step-009>`, {ref}`LINOX <step-010>`, {ref}`NS19 <step-013>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`TUNME <step-039>`, {ref}`GOX100 <step-043>`, {ref}`GOXETCH <step-046>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>` |
| `spm` | SPM, piranha (H₂SO₄ + H₂O₂) | {ref}`Wet chemical <material-wet-chemicals>` | Wet resist strip after the ash; post-etch organic clean. | "Sulfuric" on the Akrion entry.[^skw-01] | {ref}`STIE <step-006>`, {ref}`DNIS <step-009>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`TUNME <step-039>`, {ref}`ONOME <step-042>`, {ref}`GOXETCH <step-046>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`P1ME <step-062>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`NPCME <step-079>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`SACETCH <step-095>` |
| `h3po4` | Hot phosphoric acid (H₃PO₄, 85 %[^wiki-h3po4]) | {ref}`Wet chemical <material-wet-chemicals>` | Isolation-nitride strip at {ref}`NS19 <step-013>`; all-wet alternative for the ONO nitride. | "phosphoric" on the Akrion entry.[^skw-01] | {ref}`NS19 <step-013>`, {ref}`ONOME <step-042>` |
| `h2o2` | Hydrogen peroxide (H₂O₂, 30 %[^wiki-rca][^wiki-piranha]) | {ref}`Wet chemical; oxidiser <material-wet-chemicals>` | Component of SC-1, SC-2 and SPM; tungsten-slurry oxidiser; possible wet removal of the TiW pad cap. | Not listed separately; SC-1 and SC-2[^wiki-rca] and SPM[^wiki-piranha] contain it. | {ref}`SMAT <step-001>`, {ref}`BOX <step-002>`, {ref}`STIE <step-006>`, {ref}`DNIS <step-009>`, {ref}`NS19 <step-013>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`TUNME <step-039>`, {ref}`GOXETCH <step-046>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`P1ME <step-062>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`SACETCH <step-095>`, {ref}`WCMPLI <step-100>`, {ref}`WCMP2 <step-111>`, {ref}`WCMP3 <step-122>`, {ref}`WCMP4 <step-133>`, {ref}`WCMP5 <step-148>`, {ref}`PDME <step-169>` |
| `hno3` | Nitric acid (HF/HNO₃); titration reagents | {ref}`Wet chemical <material-wet-chemicals>` | Isotropic silicon etch in backside film removal; bath-concentration control. | Nitric acid not named; "SEZ223, Davinci, HF, DSP+HF, titration controlled".[^skw-01] | {ref}`BFR <step-060>` |
| `ozonated-water` | Ozonated water (O₃ in water) | {ref}`Wet chemical; oxidant <material-wet-chemicals>` | Ozonated-water pre-clean options. | typical (not listed) | {ref}`TUNME <step-039>`, {ref}`GOX100 <step-043>` |
| `ipa` | Isopropanol (IPA) | {ref}`Solvent <material-wet-chemicals>` | Drying after wet benches and strips. | "spin or IPA dry" (Akrion); "dilute HF-last with IPA dry" (DNS); "IPA clean" (Mirra CMP).[^skw-01] | {ref}`DNIS <step-009>`, {ref}`NS19 <step-013>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`TUNME <step-039>`, {ref}`ONOME <step-042>`, {ref}`GOXETCH <step-046>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`SACETCH <step-095>` |
| `residue-removers` | Amine or semi-aqueous post-etch residue removers (EKC265/EKC270 class) | {ref}`Solvent <material-wet-chemicals>` | Polymer and residue removal after contact, via, local-interconnect, metal, capacitor, seal-ring and pad etches, and in the sacrificial etch. | "Batch Rotational": "EKS265, EKC270 solvents, CO2 injected DI".[^skw-01] | {ref}`SACETCH <step-095>`, {ref}`LI1ME <step-103>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`VIM3E <step-145>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`VIM4E <step-160>`, {ref}`MM5E <step-163>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>` |
| `post-cmp-clean` | Post-CMP clean chemistry: dilute NH₄OH or TMAH, dilute HF, citric acid, surfactant; PVA brushes | {ref}`CMP consumable; wet chemical <material-cmp-consumables>` | Removal of slurry particles and metal contamination after oxide and tungsten polishes. | "AMAT Mirra CMP" with "Track ammonia clean" and "IPA clean";[^skw-01] the FY2023 10-K names "CMC Chemicals, Inc. (a subsidiary of Entegris) (process and chemical mechanical polishing chemicals)".[^sec-02] | {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>` |
| `upw` | Ultrapure (DI) water | {ref}`Utility <material-ultrapure-water>` | Rinses, dilution of wet chemicals, CMP and post-CMP cleaning, developer rinse. | "CO2 injected DI" (batch rotational solvent tool); otherwise not listed.[^skw-01] | {ref}`SMAT <step-001>`, {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`DNIS <step-009>`, {ref}`CMPNIT <step-012>`, {ref}`NS19 <step-013>`, {ref}`LVTNM <step-014>`, {ref}`LVTNIS <step-016>`, {ref}`NWM <step-017>`, {ref}`LVTPIS <step-021>`, {ref}`HVTPM <step-022>`, {ref}`PCHIS <step-025>`, {ref}`PWBM <step-026>`, {ref}`PWIS <step-029>`, {ref}`PWDEM <step-030>`, {ref}`PWDEIS <step-033>`, {ref}`TUNM <step-035>`, {ref}`TUNME <step-039>`, {ref}`ONOM <step-041>`, {ref}`ONOME <step-042>`, {ref}`LVOM <step-044>`, {ref}`GOXETCH <step-046>`, {ref}`RPM <step-049>`, {ref}`P1IS <step-051>`, {ref}`RRPM <step-052>`, {ref}`PRIS <step-054>`, {ref}`URPM <step-055>`, {ref}`UPRIS <step-057>`, {ref}`BFR <step-060>`, {ref}`P1M <step-061>`, {ref}`NTM <step-064>`, {ref}`ASTIS <step-067>`, {ref}`HVNTM <step-068>`, {ref}`HVASTIS <step-070>`, {ref}`LDNTM <step-071>`, {ref}`LDASTIS <step-074>`, {ref}`SPE <step-077>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`PDIS <step-084>`, {ref}`NSDM <step-085>`, {ref}`NSDIS <step-087>`, {ref}`CMPP <step-090>`, {ref}`LICM1 <step-093>`, {ref}`SACETCH <step-095>`, {ref}`WCMPLI <step-100>`, {ref}`LI1M <step-102>`, {ref}`CMPL <step-106>`, {ref}`CTM1 <step-107>`, {ref}`CTME <step-108>`, {ref}`WCMP2 <step-111>`, {ref}`MM1 <step-113>`, {ref}`MM1E <step-114>`, {ref}`CMPM <step-116>`, {ref}`VIM <step-118>`, {ref}`VIME <step-119>`, {ref}`WCMP3 <step-122>`, {ref}`MM2 <step-124>`, {ref}`MM2E <step-125>`, {ref}`CMPM2 <step-127>`, {ref}`VIM2 <step-129>`, {ref}`VIM2E <step-130>`, {ref}`WCMP4 <step-133>`, {ref}`CAPM <step-137>`, {ref}`CAPME <step-138>`, {ref}`MM3 <step-139>`, {ref}`MM3E <step-140>`, {ref}`CMPM3 <step-142>`, {ref}`VIM3 <step-144>`, {ref}`VIM3E <step-145>`, {ref}`WCMP5 <step-148>`, {ref}`CAP2M <step-152>`, {ref}`CAP2ME <step-153>`, {ref}`MM4 <step-154>`, {ref}`MM4E <step-155>`, {ref}`CMPM4 <step-157>`, {ref}`VIM4 <step-159>`, {ref}`VIM4E <step-160>`, {ref}`MM5 <step-162>`, {ref}`MM5E <step-163>`, {ref}`NSM <step-165>`, {ref}`NSME <step-166>`, {ref}`PDM <step-168>`, {ref}`PDME <step-169>` |
| `i-line-resist` | i-line positive photoresist (DNQ/novolac), including thick implant resist | {ref}`Lithography <material-lithography-materials>` | Implant block masks, relaxed etch masks and thick top levels. | "ASML I-line stepper", "ASML I-line scanner";[^skw-01] resist suppliers in both filings (table above).[^sec-01][^sec-02] | {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`MM5 <step-162>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>` |
| `krf-resist` | KrF (248 nm) chemically amplified positive photoresist | {ref}`Lithography <material-lithography-materials>` | Critical levels: active, poly, {term}`nitride cut`, local-interconnect contact and line, contact, metals 1–4, vias 1–4 (per step-page readings). | "ASML DUV stepper", "ASML DUV scanner";[^skw-01] resist suppliers in both filings (table above).[^sec-01][^sec-02] | {ref}`FOM <step-004>`, {ref}`P1M <step-061>`, {ref}`NPCM <step-078>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>` |
| `arc` | Organic BARC, inorganic ARC or dyed resist | {ref}`Lithography <material-lithography-materials>` | Reflectivity control on DUV levels and over metal; the ARC opened at {ref}`TUNARCE <step-036>`. | typical (not listed) | {ref}`FOM <step-004>`, {ref}`TUNM <step-035>`, {ref}`TUNARCE <step-036>`, {ref}`ONOM <step-041>`, {ref}`P1M <step-061>`, {ref}`NPCM <step-078>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>` |
| `hmds` | HMDS adhesion promoter | {ref}`Lithography <material-lithography-materials>` | Vapour prime before resist coat. | typical (not listed) | {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`P1M <step-061>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`VIM <step-118>`, {ref}`VIM2 <step-129>`, {ref}`VIM3 <step-144>`, {ref}`VIM4 <step-159>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>` |
| `tmah` | TMAH developer, 2.38 %[^microchemicals-dev] (0.26 N; our arithmetic from TMAH's molar mass of 91.15 g/mol,[^wiki-tmah] taking the solution's density as about 1 g/mL) | {ref}`Lithography <material-lithography-materials>` | Aqueous development of positive resist. | S-1: "Air Products & Chemicals, Inc., Moses Lake (developer)";[^sec-01] FY2023 10-K: "Moses Lake Industries Inc. (developer)".[^sec-02] | {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`P1M <step-061>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>` |
| `ebr-solvents` | Edge-bead remover and rinse solvents (PGMEA, ethyl lactate, cyclohexanone) | {ref}`Lithography; solvent <material-lithography-materials>` | Edge-bead removal, back-rinse and rework. | typical (not listed) | {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`P1M <step-061>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>` |
| `reticles` | Reticles (chrome on quartz or embedded attenuated phase-shift, with pellicles; SEMI P1 blanks) | {ref}`Lithography <material-lithography-materials>` | One per mask step; the process-steps sheet records a type for three plates only, which we read as embedded attenuated phase-shift masks for vias 2 and 3 and a binary mask for via 4, all for 248 nm exposure;[^steps-sheet] see {ref}`masks-index`. | "Mask GDS to reticle"; "Reticle storage/handler/defect inspection".[^skw-01] | {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`P1M <step-061>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>` |
| `exposure-consumables` | Exposure-tool consumables: KrF laser gas (Kr, F₂/Ne), mercury lamps | {ref}`Lithography hardware <material-lithography-materials>` | Light sources of the DUV and i-line tools. | typical (not listed) | {ref}`P1M <step-061>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>` |
| `ti-target` | Titanium sputter targets (Ti; reactive TiN) | {ref}`Sputter target <material-sputter-targets>` | Contact Ti/TiN liner; TiN local interconnect; TiN via liners; Ti underlayer of the metal stacks. | "Collimated Ti", "ESC TiN", "Imp TiN" under "AMAT PVD Metal";[^skw-01] S-1: "Honeywell Electronic Materials, Inc. (metal sputter targets)";[^sec-01] FY2023 10-K adds "JX Metals USA, Inc. (metal sputtering targets)".[^sec-02] | {ref}`TI/TIN1 <step-097>`, {ref}`LITIN <step-101>`, {ref}`TIN2 <step-109>`, {ref}`TIAL6 <step-112>`, {ref}`TIN3 <step-120>`, {ref}`TIAL12 <step-123>`, {ref}`TIN4 <step-131>`, {ref}`WTIAL3 <step-134>`, {ref}`TIN5 <step-146>`, {ref}`WTIAL4 <step-149>`, {ref}`WTIAL5 <step-161>` |
| `alcu-target` | Aluminium–copper sputter targets (Al–0.5%Cu) | {ref}`Sputter target <material-sputter-targets>` | Conductor of metals 1–5. | "Aluminum both pure and Cu doped";[^skw-01] Cypress S8 report: "Metal 1: 100A Ti / 3200A Al -0.5%Cu / 300A TiW".[^cyp-qtp-113005] | {ref}`TIAL6 <step-112>`, {ref}`TIAL12 <step-123>`, {ref}`WTIAL3 <step-134>`, {ref}`WTIAL4 <step-149>`, {ref}`WTIAL5 <step-161>` |
| `tiw-target` | Titanium–tungsten sputter targets (Ti:W, 10 wt.% Ti[^pat-tiw-hitachi]) | {ref}`Sputter target <material-sputter-targets>` | MiM top plates; cap of the metal stacks on the step pages' reading ({ref}`overview-metal-cap`); possible underlayer of metals 3–5. | "TiW" under "AMAT PVD Metal" and on both metal etchers.[^skw-01] | {ref}`TIAL6 <step-112>`, {ref}`TIAL12 <step-123>`, {ref}`WTIAL3 <step-134>`, {ref}`CAPTIW1 <step-136>`, {ref}`WTIAL4 <step-149>`, {ref}`CAPTIW2 <step-151>`, {ref}`WTIAL5 <step-161>` |
| `oxide-slurry` | Oxide CMP slurry (fumed or colloidal silica in KOH or NH₄OH); ceria or additive slurry for nitride selectivity | {ref}`CMP consumable <material-cmp-consumables>` | STI, pre-metal-dielectric and inter-level oxide polishes. | "AMAT Mirra CMP" with "oxide" and "nitride";[^skw-01] slurry product not named. | {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`CMPL <step-106>`, {ref}`CMPM <step-116>`, {ref}`CMPM2 <step-127>`, {ref}`CMPM3 <step-142>`, {ref}`CMPM4 <step-157>` |
| `w-slurry` | Tungsten CMP slurry (alumina or silica with H₂O₂, Fe(NO₃)₃ or KIO₃) | {ref}`CMP consumable <material-cmp-consumables>` | Removal of field tungsten after each plug fill. | "tungsten" and "high selectivity tungsten" under "AMAT Mirra CMP".[^skw-01] | {ref}`WCMPLI <step-100>`, {ref}`WCMP2 <step-111>`, {ref}`WCMP3 <step-122>`, {ref}`WCMP4 <step-133>`, {ref}`WCMP5 <step-148>` |
| `cmp-pads` | CMP pads, diamond conditioners, carrier films, membranes, retaining rings | {ref}`CMP consumable <material-cmp-consumables>` | Consumed by every polish. | typical (not listed) | {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>` |
| `furnace-ware` | Furnace ware: quartz or SiC tubes, boats, baffles, liners | {ref}`Hardware <material-hardware-consumables>` | Batch oxidation, LPCVD and alloy furnaces. | Tool vendor only: "Furnaces are all made by Aviza".[^skw-01] | {ref}`BOX <step-002>`, {ref}`ISONIT <step-003>`, {ref}`LINOX <step-010>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`, {ref}`SAGD <step-048>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`IOX45 <step-063>`, {ref}`SPNIT <step-076>`, {ref}`SPOX <step-080>`, {ref}`ALLY1 <step-096>`, {ref}`ALLY <step-170>` |
| `chamber-parts` | Plasma, CVD and PVD chamber parts: focus rings, liners, ESC parts, showerheads, domes, shields, collimators, endpoint windows, spin-chuck nozzles | {ref}`Hardware <material-hardware-consumables>` | Scheduled replacement on etch, CVD, PVD and single-wafer wet tools. | typical (not listed) | {ref}`STINITE <step-005>`, {ref}`STIE <step-006>`, {ref}`FILOX <step-011>`, {ref}`TUNARCE <step-036>`, {ref}`ONOME <step-042>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`BFR <step-060>`, {ref}`P1ME <step-062>`, {ref}`IOX45 <step-063>`, {ref}`SPNIT <step-076>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`, {ref}`LICM1E <step-094>`, {ref}`TI/TIN1 <step-097>`, {ref}`WDEP <step-099>`, {ref}`LITIN <step-101>`, {ref}`LI1ME <step-103>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`CTME <step-108>`, {ref}`TIN2 <step-109>`, {ref}`WDEP2 <step-110>`, {ref}`TIAL6 <step-112>`, {ref}`MM1E <step-114>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`VIME <step-119>`, {ref}`TIN3 <step-120>`, {ref}`WDEP3 <step-121>`, {ref}`TIAL12 <step-123>`, {ref}`MM2E <step-125>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`VIM2E <step-130>`, {ref}`TIN4 <step-131>`, {ref}`WDEP4 <step-132>`, {ref}`WTIAL3 <step-134>`, {ref}`CAPILD <step-135>`, {ref}`CAPTIW1 <step-136>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`VIM3E <step-145>`, {ref}`TIN5 <step-146>`, {ref}`WDEP5 <step-147>`, {ref}`WTIAL4 <step-149>`, {ref}`CAPILD2 <step-150>`, {ref}`CAPTIW2 <step-151>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`VIM4E <step-160>`, {ref}`WTIAL5 <step-161>`, {ref}`MM5E <step-163>`, {ref}`NFUSOX <step-164>`, {ref}`NSME <step-166>`, {ref}`NTSD <step-167>`, {ref}`PDME <step-169>` |
| `rtp-parts` | RTP consumables: tungsten-halogen lamps, quartz windows, edge rings, pyrometer calibration; cooling water and CDA/N₂ | {ref}`Hardware; utility <material-hardware-consumables>` | Rapid thermal anneals and silicidation (facility table for the Heatpulse family[^ag-8108]). | typical (not listed) | {ref}`RTAI <step-034>`, {ref}`IOX45 <step-063>`, {ref}`TIPRTAD <step-075>`, {ref}`RTAD <step-088>`, {ref}`RTAD2 <step-092>`, {ref}`CSIL <step-098>` |
| `abatement` | Exhaust abatement and waste treatment: HCl-tolerant exhaust and NH₄Cl traps, scrubbing of arsenic-, chlorine-, fluorine- and HF-bearing exhaust, acid-waste neutralisation, CMP slurry waste; pump oil | {ref}`Abatement <material-hardware-consumables>` | Handles by-products and spent chemicals (see *Safety and abatement* below). | typical (not listed) | {ref}`ISONIT <step-003>`, {ref}`CMPNIT <step-012>`, {ref}`SAGD <step-048>`, {ref}`P1IS <step-051>`, {ref}`GATENIT <step-058>`, {ref}`BFR <step-060>`, {ref}`ASTIS <step-067>`, {ref}`SPNIT <step-076>`, {ref}`NSDI <step-086>`, {ref}`NSDIS <step-087>`, {ref}`WDEP <step-099>`, {ref}`WDEP2 <step-110>`, {ref}`WCMP2 <step-111>`, {ref}`MM1E <step-114>`, {ref}`CMPM <step-116>`, {ref}`WDEP3 <step-121>`, {ref}`WCMP3 <step-122>`, {ref}`MM2E <step-125>`, {ref}`CMPM2 <step-127>`, {ref}`WDEP4 <step-132>`, {ref}`WCMP4 <step-133>`, {ref}`MM3E <step-140>`, {ref}`CMPM3 <step-142>`, {ref}`WDEP5 <step-147>`, {ref}`WCMP5 <step-148>`, {ref}`MM4E <step-155>`, {ref}`CMPM4 <step-157>`, {ref}`MM5E <step-163>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>` |
| `probe-cards` | Probe cards, needles, tip-cleaning media, calibration standards | {ref}`Test <material-hardware-consumables>` | Parametric {term}`e-test`. | "HP 4062UX" with "DC, capacitance, pulse generator, frequency counter"; "Engineering manual Probe Station".[^skw-01] | {ref}`HPETEST <step-171>` |

(materials-reram)=
## The sky130B ReRAM module

The `sky130B` variant of the PDK adds a resistive-memory tier between
metal 1 and metal 2 that is not part of the 171-step list used here;
the {ref}`sky130B ReRAM <overview-sky130b-reram>` page describes it as
a module, and its materials are kept out of the table above for that
reason. SkyWater's documentation for the device states that "a
HfO2-based RRAM layer is fabricated within the BEOL
process";[^reram-background] it does not name the electrodes or the
deposition chemistry. A TSMC patent that may still be in force gives a
typical atomic-layer-deposition route for the hafnium oxide, in the
collapsed note below this paragraph; SkyWater's capability list includes
ALD of "HfO2" and of "TiN".[^skw-01]
The ReRAM page notes that the published hafnium-oxide cells it cites
use TiN electrodes, some with a thin Ti or Hf layer next to the oxide;
gives BCl₃/O₂ plasma, fluorine- or argon-based plasmas and dilute HF
as typical etch chemistries; describes silicon oxide and nitride for
encapsulation; and reads the upper vias as using TiN, tungsten and
WF₆ as the base via 1 does (inference on that page).

:::{dropdown} From a patent shown as in force (US 9,431,609; estimated expiry 2035-03-31) — open to read
A typical atomic-layer-deposition route for the hafnium oxide uses
HfCl₄ and water.[^pat-rram-oxide-tsmc]
:::

(materials-films)=
## Films and stacks deposited

The table lists every film that a deposition or oxidation step of the
flow leaves on the wafer, in order of first appearance, with the number the PDK
gives for it where there is one. The PDK numbers come from two
sources, which do not always agree: the *Criteria & Assumptions* page
(nominal thicknesses for antenna-ratio calculations and other design
assumptions)[^pdk-03] and the process stack diagram `metal_stack.svg`
(thicknesses, heights and relative permittivities, "Diagram not to
scale!").[^pdk-04] The labels in the first column (such as "NILD3
K=4.5") are the diagram's; the step pages match them to steps. The
fourth column gives other public numbers — patent ranges for comparable
flows, or Cypress qualification reports for products from the same fab
(S8 technology in QTP 113005 and 123907, the R7FT-3R derivative in
QTP 014807) — and the last column summarises the step page's reading,
with its inferences marked there.

| Film (PDK label) | Formed at | PDK thickness or dimension | Other public numbers or composition | Reading on the step pages |
|------------------|-----------|----------------------------|-------------------------------------|---------------------------|
| Pad (base) oxide | {ref}`BOX <step-002>` | none | A Cypress {term}`SONOS` patent that may still be in force; see the collapsed note under this table | Thermal SiO₂ of the order of 10–20 nm (typical) |
| Isolation nitride | {ref}`ISONIT <step-003>` | none | AmberWave STI patent: mask nitride "500-2000 Å"[^pat-sti-amberwave] | LPCVD Si₃N₄ of the order of 50–200 nm from the cited patent;[^pat-sti-amberwave] the step pages use 150 nm as a working figure; removed at {ref}`NS19 <step-013>` |
| Trench liner oxide | {ref}`LINOX <step-010>` | none | Spansion/Cypress-lineage STI patent: liner "to a thickness of approximately 100-300 Å"[^pat-sti-cr] | Thermal SiO₂ of the order of 10–30 nm (typical)[^pat-sti-cr] |
| Field (fill) oxide, "FOX K=3.9" | {ref}`FILOX <step-011>`, polished at {ref}`CMPNIT <step-012>` | Field-oxide top at 0.3262 µm on the diagram's scale;[^pdk-04] "field oxide (above silicon surface) ... underneath poly" 0.07 µm[^pdk-03] | — | HDP-CVD oxide; fill thickness not public |
| ONO stack: {term}`tunnel oxide`, (oxy)nitride, {term}`blocking oxide` | {ref}`ONO <step-040>` | none | Cypress patent embodiments: tunnel dielectric "less than about 25 Å"; top insulating layer "about 100 Å, preferably less than about 50 Å"[^pat-01] | Furnace oxidation and LPCVD from SiH₂Cl₂, NH₃ and N₂O; SKY130 values not public |
| Thick gate oxide | {ref}`GOX100 <step-043>`, thickened at {ref}`LVGOX <step-047>` | "All VHV devices use 110A gate oxide thickness just like standard 5.0V Vcc devices";[^pdk-hv] 5 V NMOS model `toxe` 1.16e-08 (11.6 nm)[^pdk-model-nfet5v] | — | Thermal oxide grown thinner than the finished thickness here, by an amount that is not public |
| Thin gate oxide | {ref}`LVGOX <step-047>` | 1.8 V NMOS model `toxe` 4.148e-09 (4.148 nm)[^pdk-model-nfet01v8] | "Nitrided gate oxide" special module[^skw-01] | Thermal oxide, possibly nitrided |
| Gate silicon ("poly") | {ref}`SAGD <step-048>` | "poly thickness" 0.18 µm;[^pdk-03] 0.18 µm on the diagram[^pdk-04] | "LPCVD polysilicon (undoped), both amorphous and crystalline"[^skw-01] | One undoped LPCVD amorphous-silicon layer, doped by implant |
| Gate nitride cap and oxide cap | {ref}`GATENIT <step-058>`, {ref}`POC <step-059>` | "poly cap after SPE" 0.2 µm[^pdk-03] | — | Nitride under oxide; as-deposited thicknesses not public |
| Re-oxidation (screen) oxide | {ref}`IOX45 <step-063>` | none used on the step page | — | Thin thermal oxide; thickness, ambient and tool not public |
| Spacer nitride, "SPNIT K=7.5" | {ref}`SPNIT <step-076>`, etched at {ref}`SPE <step-077>` | Permittivity 7.5; no thickness[^pdk-04] | "LPCVD BTBAS low temp nitride" is on the capability list[^skw-01] | Conformal nitride; DCS, BTBAS or PECVD route |
| Spacer oxide | {ref}`SPOX <step-080>` | "oxide spacer" 0.05 µm[^pdk-03] | — | Blanket oxide left through the source/drain implants |
| Pre-metal dielectric, "PSG K=3.9", and {term}`cap oxide` | {ref}`PSG <step-089>`, polished at {ref}`CMPP <step-090>`; cap {ref}`NCAPOX <step-091>` | 0.6099 µm and 0.4299 µm labels, matching field-oxide top (0.3262 µm) to `li` bottom (0.9361 µm) and field-poly top to `li` bottom (our arithmetic);[^pdk-04] "Pre-LI ILD thickness" 0.5 µm[^pdk-03] | — | HDP PSG polished close to the gate caps, then an undoped cap of about 0.2–0.3 µm (inferred) |
| Contact liner Ti/TiN (and titanium {term}`silicide`) | {ref}`TI/TIN1 <step-097>`; silicide formed at {ref}`CSIL <step-098>` | none | — | Ti and TiN of the order of 10–30 nm each (typical)[^koerner-1993] |
| Tungsten plugs: `licon1`, `mcon`, `via`, `via2`, `via3` | {ref}`WDEP <step-099>`, {ref}`WDEP2 <step-110>`, {ref}`WDEP3 <step-121>`, {ref}`WDEP4 <step-132>`, {ref}`WDEP5 <step-147>`; polished at {ref}`WCMPLI <step-100>`, {ref}`WCMP2 <step-111>`, {ref}`WCMP3 <step-122>`, {ref}`WCMP4 <step-133>`, {ref}`WCMP5 <step-148>` | Via heights 0.27 µm (via 1), 0.42 µm (via 2), 0.39 µm (via 3)[^pdk-04] | — | Blanket CVD tungsten; deposited thickness not public |
| TiN plug liners | {ref}`TIN2 <step-109>`, {ref}`TIN3 <step-120>`, {ref}`TIN4 <step-131>`, {ref}`TIN5 <step-146>` | none | — | IMP TiN, a few tens of nanometres on the field (typical)[^txt-05][^rossnagel-1998] |
| Local interconnect, `li` | {ref}`LITIN <step-101>` | 0.1 µm;[^pdk-04] "LI1 thickness for antenna ratio calculations" 0.1 µm[^pdk-03] | Efabless lecture: "Titanium Nitride (TiN)"[^ann-16] | Sputtered TiN |
| Local-interconnect nitride, "LINT K=7.3" | {ref}`LINIT <step-104>` | 0.075 µm[^pdk-04] | — | Low-temperature nitride (PECVD or BTBAS) |
| "NILD2 K=4.05" | {ref}`NILD2 <step-105>`, polished at {ref}`CMPL <step-106>` | 0.265 µm between `li` and `metal1`[^pdk-04] | — | HDP or PECVD TEOS oxide, about 0.5–0.7 µm as deposited (inferred) |
| Metal 1 | {ref}`TIAL6 <step-112>` | 0.36 µm;[^pdk-04] 0.35 µm antenna value[^pdk-03] | "Metal 1: 100A Ti / 3200A Al -0.5%Cu / 300A TiW";[^cyp-qtp-113005] 2014 change to "150A Ti/250A TiN/3200A Al 0.5% Cu/90A Ti/500A TiN"[^cyp-qtp-123907] | Ti/Al–Cu/TiW, or the TiN-clad stack ({ref}`overview-metal-cap`) |
| "NILD3 K=4.5" with "NILD3_C K=3.5" (0.030 µm) | {ref}`NILD3 <step-115>`, polished at {ref}`CMPM <step-116>`; cap {ref}`NCAPOX3 <step-117>` | Via-1 height 0.27 µm[^pdk-04] | — | Gap-fill oxide (fluorinated option) and cap |
| Metal 2 | {ref}`TIAL12 <step-123>` | 0.36 µm;[^pdk-04] 0.35 µm antenna value[^pdk-03] | "Metal 2: 100A Ti / 3200A Al -0.5%Cu / 300A TiW"[^cyp-qtp-113005] | As metal 1 |
| "NILD4 K=4.2" with "NILD4_C K=3.5" (0.030 µm) | {ref}`NILD4 <step-126>`, polished at {ref}`CMPM2 <step-127>`; cap {ref}`NCAPOX4 <step-128>` | Via-2 height 0.42 µm[^pdk-04] | — | As NILD3 |
| Metal 3 | {ref}`WTIAL3 <step-134>` | 0.845 µm;[^pdk-04] antenna values 0.85, 0.8 or 2 µm by flow[^pdk-03] | "Metal 3: 150A Ti / 7200A Al -0.5%Cu / 300A TiW";[^cyp-qtp-113005] S8DI "Metal 3: 500A TiW/21,250A Al 0.5% Cu/300A TiW"[^cyp-qtp-123907] | Ti or TiW underlayer, about 0.8 µm Al–Cu, TiW or TiN cap ({ref}`overview-metal-cap`) |
| MiM capacitor dielectric ("CAPILD" on the `cap_mim` cross-section) | {ref}`CAPILD <step-135>`, {ref}`CAPILD2 <step-150>` | No thickness; `CMIMA` and `CMIM2A` 2 fF/µm²[^pdk-07] | "PECVD silane oxide/nitride/oxynitride, C1"[^skw-01] | PECVD oxynitride (inference); 18–33 nm for k = 4–7.5 (arithmetic) |
| MiM top plate, `capm` and `cap2m` | {ref}`CAPTIW1 <step-136>`, {ref}`CAPTIW2 <step-151>` | `RSCAPM` 5.8 Ω/sq and the same for the second plate[^pdk-07] | "TiW"[^skw-01] | TiW of roughly 0.1 µm (inference from sheet resistance) |
| "NILD5 K=4.1" | {ref}`NILD5 <step-141>`, polished at {ref}`CMPM3 <step-142>`; cap {ref}`NCAPOX5 <step-143>` | Via-3 height 0.39 µm[^pdk-04] | — | Gap-fill oxide and cap |
| Metal 4 | {ref}`WTIAL4 <step-149>` | 0.845 µm;[^pdk-04] antenna values 0.8 or 2 µm by flow[^pdk-03] | none | Repeat of metal 3 (inference) |
| "NILD6 K=4.0" | {ref}`NILD6 <step-156>`, polished at {ref}`CMPM4 <step-157>`; cap {ref}`NCAPOX6 <step-158>` | Via-4 height 0.505 µm[^pdk-04] | — | Gap-fill oxide and cap |
| Metal 5 | {ref}`WTIAL5 <step-161>` | 1.26 µm;[^pdk-04] antenna values 1.2 or 2 µm by flow[^pdk-03] | none | Ti or TiW underlayer, about 1.2 µm Al–Cu, TiW cap; also fills via 4 (inference) |
| "TOPOX K=3.9" | {ref}`NFUSOX <step-164>` | 0.09 µm on the metal-5 top, 0.070 µm on its sidewall[^pdk-04] | Fab 4 passivation "1000Å TEOS / 9000Å PECVD Nitride"[^cyp-qtp-014807] and "1000A TEOS/9000A Si3N4"[^cyp-qtp-123907] | Thin undoped oxide |
| "TOPNIT K=7.5" | {ref}`NTSD <step-167>` | 0.54 µm on the metal-5 top, 0.4223 µm on its sidewall[^pdk-04] | As above, and "7000 +/- 2000A Nitride"[^cyp-qtp-113005] | PECVD silicon nitride |
| "PI1 K=2.94" | no step | Drawn over the passivation, no thickness[^pdk-04] | "Polyimide cure" is a furnace entry[^skw-01] | Not part of the step list |

:::{dropdown} From a patent shown as in force (US 8,796,098; estimated expiry 2034-02-26) — open to read
The *Pad (base) oxide* row above: the Cypress {term}`SONOS` patent gives
the pad oxide as "from about 10 nanometers (nm) to about
20 nm".[^pat-04]
:::

## Safety and abatement

Several consumables of the flow are hazardous in ways that shape how
they are delivered and exhausted. Silane is "a colorless, pyrophoric
gas";[^wiki-silane] phosphine is "a highly toxic respiratory
poison";[^wiki-ph3] arsine is described as "flammable, pyrophoric, and
highly toxic";[^wiki-ash3] boron trifluoride is a "pungent,
colourless, and toxic gas" that "is corrosive";[^wiki-bf3] and tungsten hexafluoride is "a toxic,
corrosive, colorless gas".[^wiki-wf6] Typical forming-gas
formulations, by contrast, "are not explosive".[^wiki-fg] The step
pages describe the implant gases as delivered in sub-atmospheric or dilute
cylinders from monitored gas cabinets ({ref}`category-implant`). They
also list the by-products that need abatement: the HCl and ammonium
chloride of dichlorosilane nitride furnaces
({ref}`ISONIT <step-003>`[^txt-02]), the HF and SiF₄ of tungsten CVD
({ref}`WDEP <step-099>`[^txt-09]), arsenic-bearing ash and spent acid
after arsenic implants ({ref}`ASTIS <step-067>`), chlorine from the
metal etches ({ref}`MM1E <step-114>`), fluorocarbons from the
dielectric etches ({ref}`NSME <step-166>`), and the metal-laden slurry
waste of the tungsten polishes ({ref}`WCMP2 <step-111>`[^txt-07]).
None of the SkyWater sources cited here describes the fab's gas
delivery, abatement or waste treatment.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
## Related patents, papers and filings

**Related patents.**

* {ref}`Titanium-tungsten target material for sputtering and manufacturing method therefor <patent-gp27460980>` — US 5,160,534 A (1990)
* {ref}`Composition and slurry useful for metal CMP <patent-gp25030826>` — US 5,958,288 A (1996)
* {ref}`Shallow trench isolation approach for improved STI corner rounding <patent-gp26708682>` — US 7,439,141 B2 (2001)
* {ref}`Method of manufacturing an oxide-nitride-oxide (ONO) dielectric for SONOS-type devices <patent-gp35405131>` — US 6,969,689 B1 (2002)
* {ref}`Shallow trench isolation process <patent-gp32990685>` — US 6,960,781 B2 (2003)

:::{dropdown} 2 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 8,796,098 B1 <patent-gp51229009>` — in force
* {ref}`US 9,431,609 B2 <patent-gp55302792>` — in force
:::

**Related filings.**

* SkyWater Technology, Inc., S-1, filed 2021-03-22: Form S-1 registration statement (initial public offering), Registration No. 333-254580 ({ref}`full entry <filing-skywater-s-1-2021-03-22>`)
* SkyWater Technology, Inc., 424B4, filed 2021-04-22: Final prospectus for the initial public offering of 6,960,000 shares of common stock ({ref}`full entry <filing-skywater-424b4-2021-04-22>`)
* SkyWater Technology, Inc., 10-K, filed 2024-03-15: Annual report on Form 10-K for the fiscal year ended 2023-12-31 ({ref}`full entry <filing-skywater-10-k-2024-03-15>`)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — every gas,
  chemistry, film and polish process quoted in the main table and the
  inconsistency notes.[^skw-01]
* SkyWater Technology, Form S-1 (2021) and Form 10-K for fiscal 2023 —
  the "Raw materials" paragraphs and supplier lists.[^sec-01][^sec-02]
* Cypress Semiconductor qualification reports QTP 113005, 123907 and
  014807 — metal-stack and passivation compositions at the
  fab.[^cyp-qtp-113005][^cyp-qtp-123907][^cyp-qtp-014807]
* SkyWater PDK, *Criteria & Assumptions* and the process stack
  diagram — film thicknesses and dielectric labels.[^pdk-03][^pdk-04]
* SkyWater PDK, *Device Details*, *High Voltage Methodology* and the
  1.8 V and 5 V NMOS models — MiM parameters and gate-oxide
  thicknesses.[^pdk-07][^pdk-hv][^pdk-model-nfet01v8][^pdk-model-nfet5v]
* SkyWater, `sky130_fd_pr_reram` *Background* — the hafnium-oxide
  switching layer of the ReRAM module.[^reram-background]
* The *S8 / SKY130 Process Steps* sheet — the 171 steps indexed
  here.[^steps-sheet]
* Axcelis, *GSD Ovation* product page — source consumable costs with
  fluorinated species.[^axcelis-gsd-page]

### High-level understanding

* Quirk and Serda, *Semiconductor Manufacturing Technology* — the
  fab-floor view of each tool class and its consumables, including
  CMP water and waste.[^txt-07]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  cleaning, CVD, sputtering, lithography and etch chemistry.[^txt-02]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — chapter-per-process detail on chamber cleans and
  exhaust by-products.[^txt-09]
* Wikipedia, *RCA clean* and *Piranha solution* — SC-1, SC-2 and SPM
  compositions.[^wiki-rca][^wiki-piranha]
* Wikipedia, *Tetramethylammonium hydroxide* and *Forming gas* — the
  developer and the alloy ambient.[^wiki-tmah][^wiki-fg]
* Wikipedia, *Silane*, *Phosphine*, *Arsine*, *Boron trifluoride* and
  *Tungsten hexafluoride* — properties and hazards of the main
  precursor and dopant gases.[^wiki-silane][^wiki-ph3][^wiki-ash3][^wiki-bf3][^wiki-wf6]

### Deep dive

* Kern, *J. Electrochem. Soc.* 1990 — how the RCA cleans and their
  successors developed.[^kern-1990]
* Reinhardt and Reidy (eds.), *Handbook of Cleaning in Semiconductor
  Manufacturing* — wet and dry cleaning, including post-implant
  strip.[^reinhardt-2010]
* Visintin, Korzenski and Baum, *J. Electrochem. Soc.* 2006 — liquid
  strippers for high-dose implanted resist.[^visintin-2006]
* Fujimura et al., *JVST B* 1994 — water-vapour addition to downstream
  ashing.[^fujimura-1994]
* van Gelder and Hauser, *J. Electrochem. Soc.* 1967 — hot phosphoric
  acid etching of nitride against oxide.[^vgh-1967]
* Schwartz and Robbins, *J. Electrochem. Soc.* 1976 — HF/HNO₃ etching
  of silicon.[^schwartz-1976]
* Nojiri, *Dry Etching Technology for Semiconductors* — production
  etch chemistries for poly, oxide and metal.[^nojiri-2015]
* Gumpher et al., *J. Electrochem. Soc.* 2004 — low-temperature LPCVD
  nitride from BTBAS and ammonia.[^gumpher-2004]
* Denison, Barbour and Burkhart, *JVST A* 1996 — fluorine-doped oxide
  as an {term}`inter-metal dielectric`.[^denison-1996]
* Berg and Nyberg, *Thin Solid Films* 2005 — reactive sputtering, the
  process that makes TiN from titanium targets.[^berg-2005]
* Hitachi Metals, US 5,160,534 — the 10 wt.% Ti composition of Ti:W
  sputter targets.[^pat-tiw-hitachi]
* Ito, *Advances in Polymer Science* 2005 — chemically amplified KrF
  resists.[^ito-2005]
* Krishnan, Nalaskowski and Cook, *Chemical Reviews* 2010 — oxide and
  tungsten slurry chemistry.[^rev-02]
* Steigerwald, Murarka and Gutmann, *Chemical Mechanical Planarization
  of Microelectronic Materials* — pads, slurries and process
  control.[^steigerwald-1997]
* Zantye, Kumar and Sikder, *Materials Science and Engineering R* 2004
  — a long review of CMP, including slurry consumption.[^zantye-2004]
* Cabot, US 5,958,288 — a peroxide and ferric-catalyst tungsten
  slurry.[^pat-cmp-cabot]
* Jolley, *Solid State Phenomena* 1998 — TMAH as a post-tungsten-CMP
  clean.[^jolley-1998]
* SEMI M1 and SEMI M8 — the specifications for prime and test
  wafers.[^semi-m1][^semi-m8]

(materials-open-questions)=
## Open questions and inconsistencies

The step pages were written separately, and their *Resources
required* sections do not always describe analogous steps in the same
way. Items that two consistency passes over the step pages on
2026-09-13 resolved have been removed: spellings and quotations of
SkyWater's entries, developer strength on the mask pages that describe
development, the metal-etch gas wording, the PSG dimension labels, the
discussion of "PECVD Tungsten", the implant-strip wet cleans and ash
additions, the post-CMP clean chemistry and pad descriptions, the gas
sets of the two MiM plate etches (which the PDK calls "identical"
constructions[^pdk-07]), the contact and via etch gases, ash and
solvent, the reason for leaving out HMDS on MM2 and CAP2M, the
cap-oxide carrier gases, the RTA ambient (SkyWater lists the Heatpulse's
gases, not an ambient[^skw-01]) and the filing and year behind each
supplier statement. The differences below remain.

### Chemistries of analogous steps

* **Metal etches.** The cap breakthrough is "CF₄ or SF₆" at
  {ref}`MM1E <step-114>` and {ref}`MM2E <step-125>`, "CF₄ or CHF₃" at
  {ref}`MM3E <step-140>` and {ref}`MM4E <step-155>`, and "a fluorine-
  or chlorine-bearing mixture" at {ref}`MM5E <step-163>`; the ash is
  "O₂/N₂ and H₂/N₂" on the first two and "O₂/N₂" on the last three; CH₄
  is a possible additive on the first two only. This item was outside
  the scope of the second pass.
* **Ash additions after implants.** All fourteen implant-strip pages now
  name CF₄ as listed on the Iridia and Mattson ashers and left out, but
  for page-specific reasons: the exposed trench silicon and pad oxide at
  {ref}`DNIS <step-009>`, the pad and trench oxide on the well-module
  strips, the silicon gate film at {ref}`P1IS <step-051>`,
  {ref}`PRIS <step-054>` and {ref}`UPRIS <step-057>`, and the screen or
  spacer oxide on the tip and source/drain strips. NH₃ and water vapour
  are named only on the three strips whose recipe outlines discuss
  water-vapour ashing of the crust ({ref}`PRIS <step-054>`,
  {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`); SkyWater lists NH3
  for the Iridia but no water vapour for any asher.[^skw-01]
* **Post-CMP cleans.** The oxide polishes list dilute NH₄OH and possibly
  dilute HF, and the tungsten polishes dilute NH₄OH or TMAH and possibly
  citric acid or dilute HF (the category page's split);
  {ref}`CMPNIT <step-012>` adds the surfactant its recipe outline gives
  for its ceria-capable polish.
* **HMDS on the metal-3 and metal-4 masks.** {ref}`MM3 <step-139>` and
  {ref}`MM4 <step-154>` list an organic BARC without HMDS and give no
  reason. The reason given at {ref}`MM1 <step-113>` and
  {ref}`CAPM <step-137>` — HMDS is not needed on metal — does not
  clearly apply, because on the {ref}`CAPME <step-138>` and
  {ref}`CAP2ME <step-153>` pages' reading the capacitor dielectric
  remains over the metal outside the plates; neither page settles what
  the resist is coated on.
* **Post-etch solvent at the contact etch.** {ref}`LICM1E <step-094>`
  lists no post-etch solvent of its own and points to
  {ref}`SACETCH <step-095>`, which this reference reads as the clean
  after that etch; the index row for the solvents therefore does not
  list 094.

### Supplier statements

* **Different filings, different suppliers.** The step pages now say
  which filing names each supplier: the 2021 S-1 (Air Products, Praxair,
  KMG Chemicals, Honeywell (also in the 10-K), Dow, JSR, Tokyo Ohka
  Kogyo and "Air Products & Chemicals, Inc., Moses Lake (developer)") or
  the fiscal 2023 10-K (Linde, Airgas, EMD Performance Materials, JX
  Metals, "CMC Chemicals, Inc. (a subsidiary of Entegris)", four
  photoresist suppliers and "Moses Lake Industries Inc.
  (developer)").[^sec-01][^sec-02] The pages from {ref}`PSG <step-089>`
  to {ref}`NILD2 <step-105>` other than {ref}`WDEP <step-099>` still
  cite the 2021 S-1 alone for gases, while the gas pages before and
  after them and the five tungsten fills name both filings; the CMP
  pages name KMG Chemicals but not CMC Chemicals; the lithography pages
  name the 2021 S-1's three photoresist suppliers; and the sputter-target
  pages name Honeywell and JX Metals from both filings. These are
  accurate for the filing cited, and neither filing ties a supplier to a
  step.

### Spellings against SkyWater's page

* Quotations keep SkyWater's wording, including "Sulfuric", "HBR" in
  the DPSII entry and "EKS265"; outside quotations the step pages write
  "sulphuric", following this reference's British spelling, "novolac",
  and the tool and solvent names set out on the
  {ref}`machines index <machines-inconsistencies>`. The capabilities
  page does not say whether "EKS265" and "EKC265" are the same
  product.[^skw-01]

### Open questions

* **Entries not explained.** SkyWater's LPCVD nitride entry reads
  "with NH3 and also DH3", and its single-wafer entry lists "DSP+HF";
  the page expands neither, and no step page discusses "DH3".[^skw-01]
  The step pages describe furnace nitride from dichlorosilane and
  ammonia, a precursor the list does not name.
* **"PECVD Tungsten".** SkyWater lists "Lam/Novellus PECVD
  Tungsten";[^skw-01] the step pages describe the plug fill as chemical
  vapour deposition from WF₆ reduced by hydrogen, with a silane or
  diborane nucleation layer. {ref}`WDEP <step-099>` and
  {ref}`WDEP2 <step-110>` to {ref}`WDEP5 <step-147>` read the wording as
  a label for the tungsten CVD tool rather than evidence of a
  plasma-assisted deposition. No public source clarifies it.
* **Listed but unused.** The list names "Cobalt" among the PVD films,
  "Polyimide cure" and "Atmospheric selective oxidation" among the
  furnace processes, and "CO2 injected DI" and "IPA clean" among the
  cleans.[^skw-01] No step page's resources section lists a cobalt
  target, a polyimide or a selective oxidation; the metal-stack and
  TiN-liner PVD pages ({ref}`TIN2 <step-109>`, {ref}`TIAL6 <step-112>`,
  {ref}`TIN3 <step-120>`, {ref}`TIAL12 <step-123>`,
  {ref}`TIN4 <step-131>`, {ref}`WTIAL3 <step-134>`,
  {ref}`TIN5 <step-146>` and {ref}`WTIAL4 <step-149>`) quote the cobalt
  entry, the {ref}`NTSD <step-167>` page mentions the polyimide cure,
  no step page mentions the two cleans, and only {ref}`CMPM4 <step-157>` quotes the Mirra's
  "Track ammonia clean". The PDK stack diagram draws a polyimide, "PI1
  K=2.94", for which the step list has no step.[^pdk-04]
* **Diagram labels without a step reading.** The stack diagram also
  carries an "IOX K=3.9" label and dimensions of 0.006 µm, 0.0431 µm,
  0.121 µm and 5.2523 µm that no step page, including {ref}`IOX45 <step-063>`,
  uses.[^pdk-04]
* **What "doped" means.** SkyWater's HDP entry reads "doped and phos
  doped"; the dopant of the first is not given. The fluorinated-oxide
  option of {ref}`NILD3 <step-115>` and {ref}`NILD4 <step-126>` rests on
  the PDK's "_C" films, not on this entry.[^skw-01]
* **No materials for many tools.** None of the sources cited here
  names the co-reactant or diluent gases of the CVD tools, the gases of
  the metal etchers or sputtering tools, or the furnace gases beyond
  what the process names imply ("LPCVD nitride, with NH3 and also
  DH3", "Ar anneal to 1150C", "N2 anneal to 1150C", "H2 and forming gas
  alloy"), nor any slurry, pad, BARC or resist product or a developer
  concentration. The implanter entries give species ("B11, BF2, P, As")
  but not whether they come from gas or solid sources, and none names
  indium.[^skw-01]
* **Which materials SKY130 uses.** None of the SkyWater sources cited
  here ties a gas, chemical, target or resist to a step, and the capability
  list covers other processes at the fab, including copper, niobium and
  193 nm lithography.[^skw-01] Every *Steps* entry above therefore
  follows the step pages' readings, and every row marked *typical (not
  listed)* is industry practice, not a SkyWater statement.

<!-- footnotes -->

[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^semi-m1]: SEMI, *SEMI M1 — Specification for Polished Single Crystal
    Silicon Wafers*, SEMI Standards store listing, accessed
    2026-09-18.
    <https://store-us.semi.org/products/m00100-semi-m1-specification-for-polished-single-crystal-silicon-wafers>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; quotations re-checked against the page on 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^wiki-piranha]: Wikipedia, *Piranha solution*.
    <https://en.wikipedia.org/wiki/Piranha_solution>
[^wiki-h3po4]: Wikipedia, *Phosphoric acid*.
    <https://en.wikipedia.org/wiki/Phosphoric_acid>
[^vgh-1967]: W. van Gelder and V. E. Hauser, "The Etching of Silicon
    Nitride in Phosphoric Acid with Silicon Dioxide as a Mask", *Journal
    of The Electrochemical Society* **114**(8), 869 (1967).
    <https://doi.org/10.1149/1.2426757>
[^schwartz-1976]: B. Schwartz and H. Robbins, "Chemical Etching of
    Silicon: IV. Etching Technology", *Journal of The Electrochemical
    Society* **123**(12), 1903–1909 (1976).
    <https://doi.org/10.1149/1.2132721>
[^wiki-tmah]: Wikipedia, *Tetramethylammonium hydroxide*.
    <https://en.wikipedia.org/wiki/Tetramethylammonium_hydroxide>
[^microchemicals-dev]: MicroChemicals, *Development of photoresists*,
    application note.
    <https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing". <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; "Raw materials" paragraph.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^epa-ghgrp-skywater]: U.S. Environmental Protection Agency, Greenhouse
    Gas Reporting Program, Envirofacts tables `PUB_DIM_FACILITY` and
    `PUB_FACTS_SUBP_GHG_EMISSION` for facility ID 1000354 (Bloomington,
    Minnesota; "SKYWATER TECHNOLOGY FOUNDRY INC" for 2010–2013 and
    "SKYWATER TECHNOLOGY INC" from 2014), reporting years 2010–2023,
    retrieved 2026-09-13.
    <https://data.epa.gov/efservice/PUB_DIM_FACILITY/FACILITY_ID/1000354/JSON>
    <https://data.epa.gov/efservice/PUB_FACTS_SUBP_GHG_EMISSION/FACILITY_ID/1000354/SUB_PART_ID/43/JSON>
[^epa-ghgrp-subpart-i]: U.S. Environmental Protection Agency,
    *Electronics Manufacturing: Subpart I, Greenhouse Gas Reporting
    Program*, information sheet, December 2024, accessed 2026-09-13.
    <https://www.epa.gov/system/files/documents/2024-04/i_electronics_infosheet_2024.pdf>
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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    retrieved 2026-09-14; tab "Sheet1" lists the 171 steps (number, code and
    description) and tab "Sheet4" gives mask types for three masks.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^wiki-fg]: Wikipedia, *Forming gas*.
    <https://en.wikipedia.org/wiki/Forming_gas>
[^axcelis-gsd-page]: Axcelis Technologies, *GSD Ovation — High Current &
    High Energy Batch Ion Implanters*, product page, accessed
    2026-08-30. <https://www.axcelis.com/products/gsd-ovation/>
[^ag-8108]: SemiStar Corp., *AG Associates Heatpulse 4100 / 8108 / 8800
    / 8800i Specifications* (reseller PDF; operating specifications for
    the Heatpulse 4100 and 8108), accessed 2026-08-30.
    <https://www.semistarcorp.com/wp-content/uploads/2025/12/AG-Associates-Heatpulse-4100-8108-8800-8800i-Specifications-Rapid-Thermal-Processor.pdf>
[^reram-background]: SkyWater PDK Authors, *Background*,
    `sky130_fd_pr_reram` — SKY130 ReRAM (SkyWater Provided)
    documentation, accessed 2026-09-13.
    <https://sky130-fd-pr-reram.readthedocs.io/en/latest/background.html>
[^pat-rram-oxide-tsmc]: T. H. Dang, H.-L. Lin, C.-Y. Tsai, C.-S. Tsai
    and R.-L. Lee (Taiwan Semiconductor Manufacturing Co.), *Oxide film
    scheme for RRAM structure*, US 9,431,609 B2, filed 2014-08-14,
    granted 2016-08-30.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9431609>
    Shown as in force; estimated expiry 2035-03-31 (estimate from public
    records, not legal advice).
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098 B1,
    granted 2014-08-05. <https://patents.google.com/patent/US8796098B1/en>
    Shown as in force; estimated expiry 2034-02-26 (estimate from public
    records, not legal advice).
[^pat-sti-amberwave]: M. T. Currie and A. J. Lochtefeld (AmberWave
    Systems Corporation; assigned to Taiwan Semiconductor Manufacturing
    Co. on 2010-01-26), *Shallow trench isolation process*,
    US 6,960,781 B2, granted 2005-11-01.
    <https://patents.google.com/patent/US6960781B2/en>
[^pat-sti-cr]: U. Kim, Y. Sun, M. S. Chang et al. (Spansion LLC; later
    Cypress Semiconductor / Infineon), *Shallow trench isolation
    approach for improved STI corner rounding*, US 7,439,141 B2,
    priority 2001-12-27, granted 2008-10-21.
    <https://patents.google.com/patent/US7439141B2/en>
[^pat-01]: K. Ramkumar, M. Rathor, B. Parameshwaran and L. Lancaster
    (Cypress Semiconductor), *Method of manufacturing an
    oxide-nitride-oxide (ONO) dielectric for SONOS-type devices*,
    US 6,969,689 B1, granted 2005-11-29.
    <https://patents.google.com/patent/US6969689B1/en>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^pdk-model-nfet5v]: SkyWater PDK Authors,
    `sky130_fd_pr__nfet_g5v0d10v5__tt.pm3.spice` (typical-corner BSIM4
    model, parameter `toxe`), google/skywater-pdk-libs-sky130_fd_pr
    repository.
    <https://raw.githubusercontent.com/google/skywater-pdk-libs-sky130_fd_pr/main/cells/nfet_g5v0d10v5/sky130_fd_pr__nfet_g5v0d10v5__tt.pm3.spice>
[^pdk-model-nfet01v8]: SkyWater PDK Authors,
    `sky130_fd_pr__nfet_01v8__tt.pm3.spice` (typical-corner BSIM4
    model, parameter `toxe`), google/skywater-pdk-libs-sky130_fd_pr
    repository.
    <https://raw.githubusercontent.com/google/skywater-pdk-libs-sky130_fd_pr/main/cells/nfet_01v8/sky130_fd_pr__nfet_01v8__tt.pm3.spice>
[^ann-16]: T. Edwards (Efabless), *Introduction to the SkyWater PDK —
    The New Age of Open Source Silicon*, lecture slides, 2021-10-08
    (UC San Diego BENG 207).
    <https://isn.ucsd.edu/courses/beng207/lectures/Tim_Edwards_2021_slides.pdf>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (MiM capacitors),
    SkyWater SKY130 PDK documentation, and the `cap_mim` cross-section
    drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/cap_mim/cross-section-cap_mim.svg>
[^wiki-silane]: Wikipedia, *Silane*. <https://en.wikipedia.org/wiki/Silane>
[^wiki-ph3]: Wikipedia, *Phosphine*. <https://en.wikipedia.org/wiki/Phosphine>
[^wiki-ash3]: Wikipedia, *Arsine*. <https://en.wikipedia.org/wiki/Arsine>
[^wiki-bf3]: Wikipedia, *Boron trifluoride*.
    <https://en.wikipedia.org/wiki/Boron_trifluoride>
[^wiki-wf6]: Wikipedia, *Tungsten hexafluoride*.
    <https://en.wikipedia.org/wiki/Tungsten_hexafluoride>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007,
    ISBN 978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^reinhardt-2010]: K. A. Reinhardt and R. F. Reidy (eds.), *Handbook of
    Cleaning in Semiconductor Manufacturing: Fundamental and
    Applications*, Wiley, 2010, ISBN 978-0-470-62595-8.
    <https://doi.org/10.1002/9781118071748>
[^visintin-2006]: P. M. Visintin, M. B. Korzenski and T. H. Baum,
    "Liquid Clean Formulations for Stripping High-Dose Ion-Implanted
    Photoresist from Microelectronic Devices", *Journal of The
    Electrochemical Society* **153**(7), G591 (2006).
    <https://doi.org/10.1149/1.2195884>
[^fujimura-1994]: S. Fujimura, M. T. Suzuki, K. Shinagawa and M.
    Nakamura, "Sodium contamination free ashing process using O₂+H₂O
    plasma downstream", *Journal of Vacuum Science & Technology B*
    **12**(4), 2409–2413 (1994). <https://doi.org/10.1116/1.587773>
[^nojiri-2015]: K. Nojiri, *Dry Etching Technology for Semiconductors*,
    Springer, 2015. <https://doi.org/10.1007/978-3-319-10295-5>
[^gumpher-2004]: J. Gumpher, W. Bather, N. Mehta and D. Wedel,
    "Characterization of Low-Temperature Silicon Nitride LPCVD from
    Bis(tertiary-butylamino)silane and Ammonia", *Journal of The
    Electrochemical Society* **151**(5), G353 (2004).
    <https://doi.org/10.1149/1.1690294>
[^denison-1996]: D. R. Denison, J. C. Barbour and J. H. Burkhart, "Low
    dielectric constant, fluorine-doped SiO₂ for intermetal
    dielectric", *Journal of Vacuum Science & Technology A* **14**(3),
    1124–1126 (1996). <https://doi.org/10.1116/1.580280>
[^berg-2005]: S. Berg and T. Nyberg, "Fundamental understanding and
    modeling of reactive sputtering processes", *Thin Solid Films*
    **476**(2), 215–230 (2005).
    <https://doi.org/10.1016/j.tsf.2004.10.051>
[^pat-tiw-hitachi]: Hitachi Metals, *Titanium-tungsten target material
    for sputtering and manufacturing method therefor*, US 5,160,534 A,
    granted 1992-11-03.
    <https://patents.google.com/patent/US5160534A/en>
[^koerner-1993]: H. Koerner, H. P. Erb and H. Melzner, "Evaluation of
    Ti and TiN thicknesses for tungsten plug contact metallization",
    *Applied Surface Science* **73**, 6–13 (1993).
    <https://doi.org/10.1016/0169-4332(93)90139-3>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^rossnagel-1998]: S. M. Rossnagel, "Directional and ionized physical
    vapor deposition for microelectronics applications", *Journal of
    Vacuum Science & Technology B* **16**(5), 2585–2608 (1998).
    <https://doi.org/10.1116/1.590242>
[^ito-2005]: H. Ito, "Chemical Amplification Resists for
    Microlithography", *Advances in Polymer Science* **172**, 37–245
    (2005). <https://doi.org/10.1007/b97574>
[^rev-02]: M. Krishnan, J. W. Nalaskowski and L. M. Cook, "Chemical
    Mechanical Planarization: Slurry Chemistry, Materials, and
    Mechanisms", *Chemical Reviews* **110**(1), 178–204 (2010).
    <https://doi.org/10.1021/cr900170z>
[^steigerwald-1997]: J. M. Steigerwald, S. P. Murarka and R. J. Gutmann,
    *Chemical Mechanical Planarization of Microelectronic Materials*,
    Wiley, 1997, ISBN 978-0-471-13827-6.
    <https://doi.org/10.1002/9783527617746>
[^zantye-2004]: P. B. Zantye, A. Kumar and A. K. Sikder, "Chemical
    mechanical planarization for microelectronics applications",
    *Materials Science and Engineering: R* **45**(3–6), 89–220 (2004).
    <https://doi.org/10.1016/j.mser.2004.06.002>
[^pat-cmp-cabot]: Cabot Corporation, *Composition and slurry useful
    for metal CMP*, US 5,958,288 A, filed 1996-11-26, granted
    1999-09-28. <https://patents.google.com/patent/US5958288A/en>
[^jolley-1998]: M. Jolley, "Applications of Tetramethylammoninium
    Hydroxide (TMAH) as a Post Tungsten CMP Cleaning Mixture", *Solid
    State Phenomena* **65–66**, 105–108 (1998).
    <https://doi.org/10.4028/www.scientific.net/SSP.65-66.105>
