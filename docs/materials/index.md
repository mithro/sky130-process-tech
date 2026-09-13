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
{ref}`category pages <categories-index>`.

## Consumable classes in a 200 mm, 130 nm fab

The classes below are those of a 200 mm fab of the 130 nm
generation[^txt-07][^txt-02] as the category pages of this reference
describe them; the main table assigns every material to one of them.

* **Substrates and test wafers.** Polished prime wafers are ordered
  to SEMI M1[^semi-m1] and test and monitor wafers to SEMI
  M8[^semi-m8] ({ref}`category-substrate`).
* **Process gases.** Bulk nitrogen, oxygen, hydrogen, argon and
  helium; oxidation and nitridation additives (HCl or DCE, N₂O, NO,
  NH₃) ({ref}`category-oxidation`).
* **Dopant gases and implant sources.** Boron trifluoride, phosphine
  and arsine in cylinders, solid sources in vaporiser ovens, and the
  ion-source parts they wear out ({ref}`category-implant`). Phosphine
  also dopes the pre-metal glass.
* **Precursors.** Silane, dichlorosilane, TEOS and BTBAS for the
  silicon-based films and tungsten hexafluoride for the tungsten plugs
  ({ref}`category-deposition`). The flow described here has no
  atomic-layer-deposition step; SkyWater lists an ALD capability,
  "Atomic Layer Deposition" with "Oxides: SiO2, Al2O3, HfO2, TiO2,
  ZrO2",[^skw-01] and the {ref}`sky130B ReRAM <overview-sky130b-reram>`
  module is where ALD precursors enter (see *The sky130B ReRAM module*
  below).
* **Etch and chamber-clean gases.** CF₄, CHF₃, C₂F₆, C₄F₈, SF₆, NF₃,
  Cl₂, BCl₃ and HBr, with O₂, N₂, Ar and He as additives and backside
  coolant ({ref}`category-etch`).
* **Wet chemicals.** HF and buffered oxide etch (BOE); the RCA
  cleans SC-1 and SC-2;[^wiki-rca] sulphuric acid–hydrogen peroxide
  mixtures (SPM, piranha);[^wiki-piranha] hot phosphoric acid for
  nitride;[^vgh-1967] HF/HNO₃ for silicon;[^schwartz-1976] isopropanol
  for drying; and amine or semi-aqueous post-etch residue removers of
  the EKC type ({ref}`category-strip`).
* **Lithography materials.** Positive i-line and KrF resists, bottom
  anti-reflective coatings (BARC), HMDS, tetramethylammonium hydroxide
  (TMAH) developer,[^wiki-tmah] edge-bead solvents, reticles and the
  light-source consumables of the exposure tools
  ({ref}`category-lithography`, {ref}`masks-index`).
* **Sputter targets.** Titanium (also sputtered reactively to TiN),
  aluminium–copper and titanium–tungsten ({ref}`category-deposition`).
* **CMP consumables.** Oxide and tungsten slurries, pads,
  conditioners, carrier parts and post-CMP clean chemistry
  ({ref}`category-cmp`).
* **Anneal ambients.** Nitrogen and argon, controlled oxygen
  additions, ammonia, and forming gas (hydrogen in nitrogen) for the
  alloy anneals ({ref}`category-anneal`).
* **Ultrapure water.** Rinses, dilution and polishing; CMP alone is
  one of a fab's largest water and waste-water users.[^txt-07]
* **Hardware consumables and abatement.** Quartz furnace ware,
  chamber kits, lamps, probe cards, exhaust abatement and waste
  treatment ({ref}`category-test`).

## The public basis for SkyWater-specific materials

Three kinds of public source say something about the materials at
SkyWater's Bloomington fab. None of them ties a material to a step.

**SkyWater's capability list.** SkyWater's *Facilities &
Capabilities* page lists, tool by tool, some of the gases, chemistries
and films each tool is set up for.[^skw-01] It is the only source that
names process chemistries at the fab. It lists gases for the ashers,
the rapid thermal anneal (RTA) tool and the poly/silicon etchers —
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
sputtering tools, the plasma CVD tools or the tungsten CVD tool. The
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
stacks and the TEOS/nitride passivation[^cyp-qtp-113005][^cyp-qtp-123907][^cyp-qtp-014807]
— and the PDK documentation gives thicknesses and permittivities for
the SKY130 stack.[^pdk-03][^pdk-04] These are the sources of the
films table below.

## How to read the index

* **Typical and SkyWater-evidenced materials.** The *Role* column
  gives what the step pages describe, which is in most cases
  industry-typical practice for a 200 mm, 130 nm fab. The *Public
  SkyWater evidence* column quotes the capability list, a filing or a
  qualification report where one names the material, or the
  capability it serves, and otherwise reads *typical (not listed)*. A
  quotation shows that a material or capability exists at the fab; it
  does not show that a given SKY130 step uses it.
* **Steps column.** A step is listed when the *Resources required*
  section of its page names the material (or, for an implant, names
  its source-support gases or source consumables). The list was
  compiled by a script and checked by reading each section; it follows
  the resources sections even where a page's recipe outline mentions
  more. Steps are given by number; the {ref}`steps-index` gives their
  codes. *All except* lists the steps whose resources section does not
  name the material.
* **Coverage.** Each of the 171 steps of the step list[^steps-sheet]
  has a page with a non-empty *Resources required* section, and each
  appears in at least one row.

(materials-table)=
## Materials index
| Material | Class | Role in SKY130 steps | Public SkyWater evidence | Steps whose Resources section names it |
|----------|-------|----------------------|--------------------------|----------------------------------------|
| Silicon wafers, 200 mm, p-type, polished bulk | Substrate | Starting material of the flow. | "200 mm equipment";[^skw-01] suppliers in both filings (table above).[^sec-01][^sec-02] | {ref}`001 <step-001>` |
| Test and monitor wafers (SEMI M8 class) | Substrate | Thickness, sheet-resistance, particle, rate and selectivity monitors; RTP thermocouple wafers; CD, overlay and tester reference wafers. | typical (not listed) | {ref}`002 <step-002>`, {ref}`003 <step-003>`, {ref}`006 <step-006>`, {ref}`008 <step-008>`, {ref}`010 <step-010>`, {ref}`015 <step-015>`, {ref}`018 <step-018>`, {ref}`019 <step-019>`, {ref}`020 <step-020>`, {ref}`023 <step-023>`, {ref}`024 <step-024>`, {ref}`027 <step-027>`, {ref}`028 <step-028>`, {ref}`031 <step-031>`, {ref}`032 <step-032>`, {ref}`034 <step-034>`, {ref}`037 <step-037>`, {ref}`038 <step-038>`, {ref}`040 <step-040>`, {ref}`043 <step-043>`, {ref}`045 <step-045>`, {ref}`047 <step-047>`, {ref}`048 <step-048>`, {ref}`050 <step-050>`, {ref}`053 <step-053>`, {ref}`056 <step-056>`, {ref}`058 <step-058>`, {ref}`059 <step-059>`, {ref}`060 <step-060>`, {ref}`061 <step-061>`, {ref}`062 <step-062>`, {ref}`063 <step-063>`, {ref}`065 <step-065>`, {ref}`066 <step-066>`, {ref}`069 <step-069>`, {ref}`072 <step-072>`, {ref}`073 <step-073>`, {ref}`075 <step-075>`, {ref}`076 <step-076>`, {ref}`077 <step-077>`, {ref}`079 <step-079>`, {ref}`080 <step-080>`, {ref}`082 <step-082>`, {ref}`083 <step-083>`, {ref}`086 <step-086>`, {ref}`088 <step-088>`, {ref}`089 <step-089>`, {ref}`090 <step-090>`, {ref}`091 <step-091>`, {ref}`092 <step-092>`, {ref}`094 <step-094>`, {ref}`095 <step-095>`, {ref}`096 <step-096>`, {ref}`097 <step-097>`, {ref}`098 <step-098>`, {ref}`099 <step-099>`, {ref}`100 <step-100>`, {ref}`101 <step-101>`, {ref}`103 <step-103>`, {ref}`104 <step-104>`, {ref}`105 <step-105>`, {ref}`106 <step-106>`, {ref}`108 <step-108>`, {ref}`109 <step-109>`, {ref}`110 <step-110>`, {ref}`112 <step-112>`, {ref}`114 <step-114>`, {ref}`115 <step-115>`, {ref}`117 <step-117>`, {ref}`119 <step-119>`, {ref}`120 <step-120>`, {ref}`121 <step-121>`, {ref}`123 <step-123>`, {ref}`125 <step-125>`, {ref}`126 <step-126>`, {ref}`128 <step-128>`, {ref}`130 <step-130>`, {ref}`131 <step-131>`, {ref}`132 <step-132>`, {ref}`134 <step-134>`, {ref}`135 <step-135>`, {ref}`136 <step-136>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`141 <step-141>`, {ref}`143 <step-143>`, {ref}`145 <step-145>`, {ref}`146 <step-146>`, {ref}`147 <step-147>`, {ref}`149 <step-149>`, {ref}`150 <step-150>`, {ref}`151 <step-151>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`156 <step-156>`, {ref}`158 <step-158>`, {ref}`160 <step-160>`, {ref}`161 <step-161>`, {ref}`163 <step-163>`, {ref}`164 <step-164>`, {ref}`166 <step-166>`, {ref}`167 <step-167>`, {ref}`169 <step-169>`, {ref}`170 <step-170>`, {ref}`171 <step-171>` |
| Nitrogen (N₂) | Bulk gas; anneal ambient | Purge, drying and vent gas; anneal ambient; ash gas; reactive gas for TiN; etch and CVD diluent; CDA/N₂ lamp cooling. | "N2 anneal to 1150C"; "Ag Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C"; N2 on the Gasonic and Iridia asher entries.[^skw-01] | all except {ref}`004 <step-004>`, {ref}`007 <step-007>`, {ref}`012 <step-012>`, {ref}`019 <step-019>`, {ref}`020 <step-020>`, {ref}`023 <step-023>`, {ref}`024 <step-024>`, {ref}`027 <step-027>`, {ref}`028 <step-028>`, {ref}`031 <step-031>`, {ref}`032 <step-032>`, {ref}`053 <step-053>`, {ref}`056 <step-056>`, {ref}`089 <step-089>`, {ref}`090 <step-090>`, {ref}`091 <step-091>`, {ref}`100 <step-100>`, {ref}`105 <step-105>`, {ref}`106 <step-106>`, {ref}`111 <step-111>`, {ref}`116 <step-116>`, {ref}`122 <step-122>`, {ref}`127 <step-127>`, {ref}`133 <step-133>`, {ref}`141 <step-141>`, {ref}`142 <step-142>`, {ref}`148 <step-148>`, {ref}`156 <step-156>`, {ref}`157 <step-157>`, {ref}`171 <step-171>` |
| Oxygen (O₂) | Bulk gas; oxidant | Dry oxidation and pyrogenic steam; ash; etch additive; oxidant for HDP and PECVD oxides; minor RTA addition. | "dry oxidation to 1150C"; "wet oxidation to 1150C"; O2 in the Heatpulse, asher and all three poly/silicon etcher entries.[^skw-01] | {ref}`002 <step-002>`, {ref}`005 <step-005>`, {ref}`006 <step-006>`, {ref}`009 <step-009>`, {ref}`010 <step-010>`, {ref}`011 <step-011>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`025 <step-025>`, {ref}`029 <step-029>`, {ref}`033 <step-033>`, {ref}`034 <step-034>`, {ref}`036 <step-036>`, {ref}`039 <step-039>`, {ref}`040 <step-040>`, {ref}`042 <step-042>`, {ref}`043 <step-043>`, {ref}`046 <step-046>`, {ref}`047 <step-047>`, {ref}`051 <step-051>`, {ref}`054 <step-054>`, {ref}`057 <step-057>`, {ref}`058 <step-058>`, {ref}`059 <step-059>`, {ref}`062 <step-062>`, {ref}`063 <step-063>`, {ref}`067 <step-067>`, {ref}`070 <step-070>`, {ref}`074 <step-074>`, {ref}`075 <step-075>`, {ref}`076 <step-076>`, {ref}`077 <step-077>`, {ref}`079 <step-079>`, {ref}`080 <step-080>`, {ref}`084 <step-084>`, {ref}`087 <step-087>`, {ref}`088 <step-088>`, {ref}`089 <step-089>`, {ref}`091 <step-091>`, {ref}`094 <step-094>`, {ref}`095 <step-095>`, {ref}`103 <step-103>`, {ref}`104 <step-104>`, {ref}`105 <step-105>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`115 <step-115>`, {ref}`117 <step-117>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`126 <step-126>`, {ref}`128 <step-128>`, {ref}`130 <step-130>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`141 <step-141>`, {ref}`143 <step-143>`, {ref}`145 <step-145>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`156 <step-156>`, {ref}`158 <step-158>`, {ref}`160 <step-160>`, {ref}`163 <step-163>`, {ref}`164 <step-164>`, {ref}`166 <step-166>`, {ref}`169 <step-169>` |
| Hydrogen (H₂) | Bulk gas; reductant | Pyrogenic or radical oxidation; bulk reduction of WF₆; alloy anneal; implant-source co-gas; possible PVD pre-clean. | "H2 and forming gas alloy"; "Iridia RF microwave, N2, O2, H2, CF4, NH3, H2/N2, 40C-270C".[^skw-01] | {ref}`002 <step-002>`, {ref}`008 <step-008>`, {ref}`010 <step-010>`, {ref}`015 <step-015>`, {ref}`040 <step-040>`, {ref}`043 <step-043>`, {ref}`096 <step-096>`, {ref}`099 <step-099>`, {ref}`109 <step-109>`, {ref}`110 <step-110>`, {ref}`120 <step-120>`, {ref}`121 <step-121>`, {ref}`131 <step-131>`, {ref}`132 <step-132>`, {ref}`146 <step-146>`, {ref}`147 <step-147>`, {ref}`170 <step-170>` |
| Forming gas (H₂ in N₂) | Anneal and ash ambient | Implant-crust and post-etch ash; alloy anneals at {ref}`ALLY1 <step-096>` and {ref}`ALLY <step-170>` ("5% H2 in N2" is the typical formulation[^wiki-fg]). | "H2 and forming gas alloy"; Iridia "H2/N2"; "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to 250C".[^skw-01] | {ref}`006 <step-006>`, {ref}`009 <step-009>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`025 <step-025>`, {ref}`029 <step-029>`, {ref}`033 <step-033>`, {ref}`039 <step-039>`, {ref}`042 <step-042>`, {ref}`046 <step-046>`, {ref}`051 <step-051>`, {ref}`054 <step-054>`, {ref}`057 <step-057>`, {ref}`062 <step-062>`, {ref}`067 <step-067>`, {ref}`070 <step-070>`, {ref}`074 <step-074>`, {ref}`079 <step-079>`, {ref}`084 <step-084>`, {ref}`087 <step-087>`, {ref}`094 <step-094>`, {ref}`095 <step-095>`, {ref}`096 <step-096>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`130 <step-130>`, {ref}`170 <step-170>` |
| Argon (Ar) | Bulk gas; anneal ambient | Sputter gas and sputter-etch pre-clean; HDP-CVD; etch diluent; RTA and furnace ambient; implant-source support gas. | "Ar anneal to 1150C"; Ar in the Heatpulse entry.[^skw-01] | {ref}`005 <step-005>`, {ref}`008 <step-008>`, {ref}`011 <step-011>`, {ref}`015 <step-015>`, {ref}`034 <step-034>`, {ref}`036 <step-036>`, {ref}`042 <step-042>`, {ref}`043 <step-043>`, {ref}`047 <step-047>`, {ref}`059 <step-059>`, {ref}`062 <step-062>`, {ref}`063 <step-063>`, {ref}`065 <step-065>`, {ref}`075 <step-075>`, {ref}`077 <step-077>`, {ref}`079 <step-079>`, {ref}`082 <step-082>`, {ref}`083 <step-083>`, {ref}`086 <step-086>`, {ref}`088 <step-088>`, {ref}`089 <step-089>`, {ref}`091 <step-091>`, {ref}`092 <step-092>`, {ref}`094 <step-094>`, {ref}`097 <step-097>`, {ref}`098 <step-098>`, {ref}`099 <step-099>`, {ref}`101 <step-101>`, {ref}`103 <step-103>`, {ref}`104 <step-104>`, {ref}`105 <step-105>`, {ref}`108 <step-108>`, {ref}`109 <step-109>`, {ref}`110 <step-110>`, {ref}`112 <step-112>`, {ref}`114 <step-114>`, {ref}`115 <step-115>`, {ref}`119 <step-119>`, {ref}`120 <step-120>`, {ref}`121 <step-121>`, {ref}`123 <step-123>`, {ref}`125 <step-125>`, {ref}`126 <step-126>`, {ref}`130 <step-130>`, {ref}`131 <step-131>`, {ref}`132 <step-132>`, {ref}`134 <step-134>`, {ref}`136 <step-136>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`141 <step-141>`, {ref}`145 <step-145>`, {ref}`146 <step-146>`, {ref}`147 <step-147>`, {ref}`149 <step-149>`, {ref}`151 <step-151>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`156 <step-156>`, {ref}`160 <step-160>`, {ref}`161 <step-161>`, {ref}`163 <step-163>`, {ref}`166 <step-166>`, {ref}`169 <step-169>` |
| Helium (He) | Bulk gas | Backside wafer cooling in etch, CVD, PVD and implant tools; TEOS carrier and CVD diluent. | typical (not listed) | {ref}`005 <step-005>`, {ref}`006 <step-006>`, {ref}`008 <step-008>`, {ref}`011 <step-011>`, {ref}`036 <step-036>`, {ref}`037 <step-037>`, {ref}`038 <step-038>`, {ref}`042 <step-042>`, {ref}`045 <step-045>`, {ref}`050 <step-050>`, {ref}`053 <step-053>`, {ref}`056 <step-056>`, {ref}`059 <step-059>`, {ref}`062 <step-062>`, {ref}`065 <step-065>`, {ref}`066 <step-066>`, {ref}`069 <step-069>`, {ref}`072 <step-072>`, {ref}`073 <step-073>`, {ref}`077 <step-077>`, {ref}`079 <step-079>`, {ref}`080 <step-080>`, {ref}`083 <step-083>`, {ref}`089 <step-089>`, {ref}`091 <step-091>`, {ref}`094 <step-094>`, {ref}`097 <step-097>`, {ref}`101 <step-101>`, {ref}`103 <step-103>`, {ref}`104 <step-104>`, {ref}`105 <step-105>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`115 <step-115>`, {ref}`117 <step-117>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`126 <step-126>`, {ref}`128 <step-128>`, {ref}`130 <step-130>`, {ref}`135 <step-135>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`141 <step-141>`, {ref}`143 <step-143>`, {ref}`145 <step-145>`, {ref}`150 <step-150>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`156 <step-156>`, {ref}`158 <step-158>`, {ref}`160 <step-160>`, {ref}`163 <step-163>`, {ref}`164 <step-164>`, {ref}`166 <step-166>`, {ref}`169 <step-169>` |
| Water vapour (H₂O) | Ash and passivation additive | Ash additive after high-dose implants ({ref}`PRIS <step-054>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`); post-etch corrosion passivation of Al–Cu and TiN. | typical (not listed) | {ref}`054 <step-054>`, {ref}`084 <step-084>`, {ref}`087 <step-087>`, {ref}`103 <step-103>`, {ref}`114 <step-114>`, {ref}`125 <step-125>`, {ref}`140 <step-140>`, {ref}`155 <step-155>`, {ref}`163 <step-163>` |
| HCl or trans-1,2-dichloroethylene (DCE) | Oxidation additive | Chlorine source for gettering in furnace oxidations. | typical (not listed) | {ref}`010 <step-010>`, {ref}`040 <step-040>`, {ref}`043 <step-043>`, {ref}`047 <step-047>`, {ref}`063 <step-063>` |
| Nitrous oxide (N₂O), nitric oxide (NO) | Oxidant; nitriding gas | Nitrided or oxynitride gate and liner oxides; ONO oxynitride layers; oxidant for PECVD silane oxide and oxynitride. | Gases not named; the list has "Nitrided gate oxide" and "PECVD silane oxide/nitride/oxynitride, C1".[^skw-01] | {ref}`010 <step-010>`, {ref}`040 <step-040>`, {ref}`047 <step-047>`, {ref}`059 <step-059>`, {ref}`063 <step-063>`, {ref}`080 <step-080>`, {ref}`091 <step-091>`, {ref}`117 <step-117>`, {ref}`128 <step-128>`, {ref}`135 <step-135>`, {ref}`143 <step-143>`, {ref}`150 <step-150>`, {ref}`158 <step-158>`, {ref}`164 <step-164>` |
| Ammonia (NH₃) | Precursor; nitriding gas | LPCVD, BTBAS and PECVD nitride; PECVD oxynitride; oxide nitridation; possible ash additive. | "LPCVD nitride, with NH3 and also DH3"; NH3 in the Heatpulse and Iridia entries.[^skw-01] | {ref}`003 <step-003>`, {ref}`010 <step-010>`, {ref}`040 <step-040>`, {ref}`047 <step-047>`, {ref}`058 <step-058>`, {ref}`076 <step-076>`, {ref}`084 <step-084>`, {ref}`087 <step-087>`, {ref}`104 <step-104>`, {ref}`135 <step-135>`, {ref}`150 <step-150>`, {ref}`167 <step-167>` |
| Silane (SiH₄) | Precursor | HDP-CVD oxide and PSG; PECVD oxide, nitride and oxynitride; LPCVD amorphous-silicon gate; tungsten nucleation. | Precursor not named; "PECVD silane oxide/nitride/oxynitride, C1", "LPCVD silane oxide", "LPCVD polysilicon (undoped), both amorphous and crystalline".[^skw-01] | {ref}`011 <step-011>`, {ref}`048 <step-048>`, {ref}`058 <step-058>`, {ref}`059 <step-059>`, {ref}`076 <step-076>`, {ref}`080 <step-080>`, {ref}`089 <step-089>`, {ref}`091 <step-091>`, {ref}`099 <step-099>`, {ref}`104 <step-104>`, {ref}`105 <step-105>`, {ref}`110 <step-110>`, {ref}`115 <step-115>`, {ref}`117 <step-117>`, {ref}`121 <step-121>`, {ref}`126 <step-126>`, {ref}`128 <step-128>`, {ref}`132 <step-132>`, {ref}`135 <step-135>`, {ref}`141 <step-141>`, {ref}`143 <step-143>`, {ref}`147 <step-147>`, {ref}`150 <step-150>`, {ref}`156 <step-156>`, {ref}`158 <step-158>`, {ref}`164 <step-164>`, {ref}`167 <step-167>` |
| Dichlorosilane (SiH₂Cl₂) | Precursor | LPCVD nitride (isolation, gate cap, spacer options); ONO trapping layer. | Not named; the LPCVD nitride entry reads "with NH3 and also DH3" and the list has "LPCVD oxide/nitride/oxide".[^skw-01] | {ref}`003 <step-003>`, {ref}`040 <step-040>`, {ref}`058 <step-058>`, {ref}`076 <step-076>` |
| TEOS (tetraethyl orthosilicate) | Precursor (liquid) | PECVD cap, spacer, inter-level and fuse oxides; TEOS route for PSG. | "PECVD TEOS, C2 and Producer" with "low temp options";[^skw-01] a 2005 Cypress Fab 4 report gives the passivation as "1000Å TEOS / 9000Å PECVD Nitride".[^cyp-qtp-014807] | {ref}`059 <step-059>`, {ref}`080 <step-080>`, {ref}`089 <step-089>`, {ref}`091 <step-091>`, {ref}`105 <step-105>`, {ref}`115 <step-115>`, {ref}`117 <step-117>`, {ref}`126 <step-126>`, {ref}`128 <step-128>`, {ref}`141 <step-141>`, {ref}`143 <step-143>`, {ref}`156 <step-156>`, {ref}`158 <step-158>`, {ref}`164 <step-164>` |
| BTBAS (bis(tertiary-butylamino)silane) | Precursor (liquid) | Low-temperature LPCVD nitride option for the spacer and the local-interconnect cap. | "LPCVD BTBAS low temp nitride".[^skw-01] | {ref}`076 <step-076>`, {ref}`104 <step-104>` |
| Silicon tetrafluoride (SiF₄) | Precursor | Fluorinated oxide option for the metal-1/metal-2 and metal-2/metal-3 dielectrics. | typical (not listed) | {ref}`115 <step-115>`, {ref}`126 <step-126>` |
| Tungsten hexafluoride (WF₆), with SiH₄ or B₂H₆ nucleation | Precursor | CVD tungsten plugs in the local-interconnect and metal contacts and in vias 1–3. | Precursor not named; "Lam/Novellus PECVD Tungsten" with "plug fill" and "PNL option for high aspect ratio (up to 10:1)".[^skw-01] | {ref}`099 <step-099>`, {ref}`110 <step-110>`, {ref}`121 <step-121>`, {ref}`132 <step-132>`, {ref}`147 <step-147>` |
| Phosphine (PH₃), solid phosphorus; TMPO | Dopant source | Phosphorus implants (deep N-well, N-well, poly, source/drain options); phosphorus for HDP or TEOS PSG. | Species "P" on both GSD implanters ("B11, BF2, P, As"); "Lam/Novellus High Density Plasma (HDP) doped and phos doped with sputter etch".[^skw-01] | {ref}`008 <step-008>`, {ref}`015 <step-015>`, {ref}`018 <step-018>`, {ref}`019 <step-019>`, {ref}`020 <step-020>`, {ref}`023 <step-023>`, {ref}`038 <step-038>`, {ref}`050 <step-050>`, {ref}`086 <step-086>`, {ref}`089 <step-089>` |
| Boron trifluoride (BF₃), solid boron | Dopant source | B⁺ and BF₂⁺ for wells, threshold adjusts, halos, resistor and P+ source/drain implants. | Species "B11, BF2" on all three implanter entries, e.g. "Axcelis 8250 Mid current B11, BF2, As, ESC chuck, E shower, 1e11 to 1e14, 0-60 deg tilt".[^skw-01] | {ref}`015 <step-015>`, {ref}`020 <step-020>`, {ref}`024 <step-024>`, {ref}`027 <step-027>`, {ref}`028 <step-028>`, {ref}`031 <step-031>`, {ref}`032 <step-032>`, {ref}`037 <step-037>`, {ref}`045 <step-045>`, {ref}`053 <step-053>`, {ref}`056 <step-056>`, {ref}`066 <step-066>`, {ref}`073 <step-073>`, {ref}`082 <step-082>`, {ref}`083 <step-083>` |
| Arsine (AsH₃), solid arsenic | Dopant source | Arsenic for tips, depletion and threshold options, poly and N+ source/drain implants. | Species "As" on all three implanter entries.[^skw-01] | {ref}`015 <step-015>`, {ref}`020 <step-020>`, {ref}`023 <step-023>`, {ref}`038 <step-038>`, {ref}`050 <step-050>`, {ref}`065 <step-065>`, {ref}`069 <step-069>`, {ref}`072 <step-072>`, {ref}`086 <step-086>` |
| Indium (solid source) | Dopant source | Alternative heavy p-type species discussed for threshold and punch-through implants. | Not listed; no implanter entry names indium.[^skw-01] | {ref}`015 <step-015>`, {ref}`037 <step-037>` |
| Ion-source and beam-line consumables: Ar, Xe or H₂ support gases, filaments or cathodes, arc-chamber liners, electrodes, disc pads, flood-gun parts, LN₂ for cryopumps | Hardware; support gas | Consumed by every implant; fluorinated species wear sources faster (Axcelis notes "source operating costs especially with fluorinated species"[^axcelis-gsd-page]). | typical (not listed) | {ref}`008 <step-008>`, {ref}`015 <step-015>`, {ref}`018 <step-018>`, {ref}`019 <step-019>`, {ref}`020 <step-020>`, {ref}`023 <step-023>`, {ref}`024 <step-024>`, {ref}`027 <step-027>`, {ref}`028 <step-028>`, {ref}`031 <step-031>`, {ref}`032 <step-032>`, {ref}`037 <step-037>`, {ref}`038 <step-038>`, {ref}`045 <step-045>`, {ref}`050 <step-050>`, {ref}`053 <step-053>`, {ref}`056 <step-056>`, {ref}`065 <step-065>`, {ref}`066 <step-066>`, {ref}`069 <step-069>`, {ref}`072 <step-072>`, {ref}`073 <step-073>`, {ref}`082 <step-082>`, {ref}`083 <step-083>`, {ref}`086 <step-086>` |
| Carbon tetrafluoride (CF₄) | Etch gas; clean gas | Nitride and oxide etch, breakthrough and cap-open steps; ash additive; CF₄/O₂ PECVD chamber clean. | CF4 on "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2", "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6, O2", "Lam 4400, HBr, Cl2, C2F6, CF4, SF6, O2" and the Iridia and Mattson ashers.[^skw-01] | {ref}`005 <step-005>`, {ref}`006 <step-006>`, {ref}`009 <step-009>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`036 <step-036>`, {ref}`042 <step-042>`, {ref}`058 <step-058>`, {ref}`059 <step-059>`, {ref}`062 <step-062>`, {ref}`067 <step-067>`, {ref}`070 <step-070>`, {ref}`074 <step-074>`, {ref}`076 <step-076>`, {ref}`077 <step-077>`, {ref}`079 <step-079>`, {ref}`080 <step-080>`, {ref}`094 <step-094>`, {ref}`103 <step-103>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`130 <step-130>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`145 <step-145>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`160 <step-160>`, {ref}`163 <step-163>`, {ref}`166 <step-166>`, {ref}`169 <step-169>` |
| Trifluoromethane (CHF₃) | Etch gas | Oxide and nitride etch, ARC open, sidewall passivation in metal etch. | CHF3 on the DPSII entry only.[^skw-01] | {ref}`005 <step-005>`, {ref}`036 <step-036>`, {ref}`042 <step-042>`, {ref}`062 <step-062>`, {ref}`077 <step-077>`, {ref}`079 <step-079>`, {ref}`094 <step-094>`, {ref}`103 <step-103>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`130 <step-130>`, {ref}`140 <step-140>`, {ref}`145 <step-145>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`160 <step-160>`, {ref}`163 <step-163>`, {ref}`166 <step-166>`, {ref}`169 <step-169>` |
| Hexafluoroethane (C₂F₆) | Etch gas | Contact, via and seal-ring oxide etches. | C2F6 on the Lam 4400 entry only.[^skw-01] | {ref}`094 <step-094>`, {ref}`108 <step-108>`, {ref}`119 <step-119>`, {ref}`130 <step-130>`, {ref}`145 <step-145>`, {ref}`160 <step-160>`, {ref}`166 <step-166>` |
| C₄F₈, CO, CH₃F, CH₂F₂, CH₄ | Etch additive | Polymerising, selectivity and passivation additives: C₄F₈ and CO in contact and via etches; CH₃F or CH₂F₂ for nitride selectivity; CH₄ in metal etch. | typical (not listed) | {ref}`077 <step-077>`, {ref}`094 <step-094>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`130 <step-130>`, {ref}`145 <step-145>`, {ref}`153 <step-153>`, {ref}`160 <step-160>`, {ref}`166 <step-166>` |
| Sulphur hexafluoride (SF₆) | Etch gas; clean gas | Nitride, TiN, TiW and pad etches; SF₆/O₂ chamber clean. | SF6 on the Lam 9400 and Lam 4400 entries.[^skw-01] | {ref}`005 <step-005>`, {ref}`006 <step-006>`, {ref}`042 <step-042>`, {ref}`062 <step-062>`, {ref}`077 <step-077>`, {ref}`103 <step-103>`, {ref}`114 <step-114>`, {ref}`125 <step-125>`, {ref}`138 <step-138>`, {ref}`169 <step-169>` |
| Nitrogen trifluoride (NF₃) | Clean gas; etch gas | Remote- or in-situ-plasma clean of HDP, PECVD and tungsten CVD chambers and etchers; nitride-tube clean option. | NF3 on the DPSII entry.[^skw-01] | {ref}`003 <step-003>`, {ref}`005 <step-005>`, {ref}`006 <step-006>`, {ref}`011 <step-011>`, {ref}`058 <step-058>`, {ref}`059 <step-059>`, {ref}`062 <step-062>`, {ref}`076 <step-076>`, {ref}`077 <step-077>`, {ref}`079 <step-079>`, {ref}`080 <step-080>`, {ref}`089 <step-089>`, {ref}`091 <step-091>`, {ref}`094 <step-094>`, {ref}`099 <step-099>`, {ref}`103 <step-103>`, {ref}`104 <step-104>`, {ref}`105 <step-105>`, {ref}`108 <step-108>`, {ref}`110 <step-110>`, {ref}`115 <step-115>`, {ref}`117 <step-117>`, {ref}`119 <step-119>`, {ref}`121 <step-121>`, {ref}`126 <step-126>`, {ref}`128 <step-128>`, {ref}`130 <step-130>`, {ref}`132 <step-132>`, {ref}`135 <step-135>`, {ref}`141 <step-141>`, {ref}`143 <step-143>`, {ref}`145 <step-145>`, {ref}`147 <step-147>`, {ref}`150 <step-150>`, {ref}`156 <step-156>`, {ref}`158 <step-158>`, {ref}`160 <step-160>`, {ref}`164 <step-164>`, {ref}`167 <step-167>` |
| Hydrogen bromide (HBr), Br₂ | Etch gas | Silicon trench and gate etches; organic ARC open; bromine option for the second MiM plate etch. | "HBR" on the DPSII entry; "HBr" on the Lam 9400 and 4400 entries.[^skw-01] | {ref}`006 <step-006>`, {ref}`036 <step-036>`, {ref}`042 <step-042>`, {ref}`062 <step-062>`, {ref}`153 <step-153>` |
| Chlorine (Cl₂) | Etch gas | Trench and gate etches; Al–Cu, TiN and TiW metal etches. | Cl2 on the DPSII and Lam 4400 entries; the metal etchers are listed without gases ("Lam 9600, Al, TiW, TiN, Pt").[^skw-01] | {ref}`006 <step-006>`, {ref}`062 <step-062>`, {ref}`103 <step-103>`, {ref}`114 <step-114>`, {ref}`125 <step-125>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`163 <step-163>` |
| Boron trichloride (BCl₃) | Etch gas | Al–Cu and TiN etches; MiM plate etch. | typical (not listed) | {ref}`103 <step-103>`, {ref}`114 <step-114>`, {ref}`125 <step-125>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`155 <step-155>`, {ref}`163 <step-163>` |
| Hydrofluoric acid (49 % and dilute HF) | Wet chemical | Native-oxide strip and HF-last pre-clean; tunnel-window and gate-oxide etches; nitride-strip breakthrough; backside film removal; pre-metal contact clean. | "DNS wet bench industry standard HF/SC1/SC2" with "dilute HF-last with IPA dry"; "SEZ223, Davinci, HF, DSP+HF, titration controlled".[^skw-01] | {ref}`001 <step-001>`, {ref}`002 <step-002>`, {ref}`003 <step-003>`, {ref}`006 <step-006>`, {ref}`010 <step-010>`, {ref}`013 <step-013>`, {ref}`033 <step-033>`, {ref}`039 <step-039>`, {ref}`042 <step-042>`, {ref}`046 <step-046>`, {ref}`060 <step-060>`, {ref}`095 <step-095>` |
| Buffered oxide etch (NH₄F/HF), with surfactant | Wet chemical | Tunnel-window and thick-gate-oxide etches; ONO bottom-oxide clear; pre-clean and sacrificial-etch alternatives. | "Akrion Gamma Batch Wet Bench": "Sulfuric, SC1, phosphoric, BOE, spin or IPA dry".[^skw-01] | {ref}`039 <step-039>`, {ref}`042 <step-042>`, {ref}`043 <step-043>`, {ref}`046 <step-046>`, {ref}`095 <step-095>` |
| SC-1 (NH₄OH + H₂O₂ + H₂O) | Wet chemical | Particle and organic clean in pre-furnace, post-strip and post-etch sequences. | "SC1" on the Akrion, DNS and FSI Mercury entries.[^skw-01] | {ref}`001 <step-001>`, {ref}`002 <step-002>`, {ref}`006 <step-006>`, {ref}`009 <step-009>`, {ref}`010 <step-010>`, {ref}`013 <step-013>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`025 <step-025>`, {ref}`029 <step-029>`, {ref}`033 <step-033>`, {ref}`039 <step-039>`, {ref}`043 <step-043>`, {ref}`046 <step-046>`, {ref}`051 <step-051>`, {ref}`054 <step-054>`, {ref}`057 <step-057>`, {ref}`062 <step-062>`, {ref}`067 <step-067>`, {ref}`070 <step-070>`, {ref}`074 <step-074>`, {ref}`077 <step-077>`, {ref}`079 <step-079>`, {ref}`084 <step-084>`, {ref}`087 <step-087>`, {ref}`095 <step-095>` |
| SC-2 (HCl + H₂O₂ + H₂O) | Wet chemical | Metal-ion clean before furnace steps and anneals. | "SC2" only on the DNS and FSI Mercury entries ("HF/SC1/SC2").[^skw-01] | {ref}`001 <step-001>`, {ref}`002 <step-002>`, {ref}`009 <step-009>`, {ref}`010 <step-010>`, {ref}`013 <step-013>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`025 <step-025>`, {ref}`029 <step-029>`, {ref}`033 <step-033>`, {ref}`039 <step-039>`, {ref}`043 <step-043>`, {ref}`046 <step-046>`, {ref}`057 <step-057>`, {ref}`067 <step-067>`, {ref}`074 <step-074>`, {ref}`084 <step-084>`, {ref}`087 <step-087>` |
| SPM, piranha (H₂SO₄ + H₂O₂) | Wet chemical | Wet resist strip after the ash; post-etch organic clean. | "Sulfuric" on the Akrion entry.[^skw-01] | {ref}`006 <step-006>`, {ref}`009 <step-009>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`025 <step-025>`, {ref}`029 <step-029>`, {ref}`033 <step-033>`, {ref}`039 <step-039>`, {ref}`042 <step-042>`, {ref}`046 <step-046>`, {ref}`051 <step-051>`, {ref}`054 <step-054>`, {ref}`057 <step-057>`, {ref}`062 <step-062>`, {ref}`067 <step-067>`, {ref}`070 <step-070>`, {ref}`074 <step-074>`, {ref}`079 <step-079>`, {ref}`084 <step-084>`, {ref}`087 <step-087>`, {ref}`095 <step-095>` |
| Hot phosphoric acid (H₃PO₄, 85 %) | Wet chemical | Isolation-nitride strip at {ref}`NS19 <step-013>`; all-wet alternative for the ONO nitride. | "phosphoric" on the Akrion entry.[^skw-01] | {ref}`013 <step-013>`, {ref}`042 <step-042>` |
| Hydrogen peroxide (H₂O₂, 30 %) | Wet chemical; oxidiser | Component of SC-1, SC-2 and SPM; tungsten-slurry oxidiser; possible wet removal of the TiW pad cap. | Not listed separately; SC-1 and SC-2[^wiki-rca] and SPM[^wiki-piranha] contain it. | {ref}`001 <step-001>`, {ref}`002 <step-002>`, {ref}`006 <step-006>`, {ref}`009 <step-009>`, {ref}`013 <step-013>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`025 <step-025>`, {ref}`029 <step-029>`, {ref}`033 <step-033>`, {ref}`039 <step-039>`, {ref}`046 <step-046>`, {ref}`051 <step-051>`, {ref}`054 <step-054>`, {ref}`057 <step-057>`, {ref}`062 <step-062>`, {ref}`067 <step-067>`, {ref}`070 <step-070>`, {ref}`074 <step-074>`, {ref}`077 <step-077>`, {ref}`079 <step-079>`, {ref}`084 <step-084>`, {ref}`087 <step-087>`, {ref}`095 <step-095>`, {ref}`100 <step-100>`, {ref}`111 <step-111>`, {ref}`122 <step-122>`, {ref}`133 <step-133>`, {ref}`148 <step-148>`, {ref}`169 <step-169>` |
| Nitric acid (HF/HNO₃); titration reagents | Wet chemical | Isotropic silicon etch in backside film removal; bath-concentration control. | Nitric acid not named; "SEZ223, Davinci, HF, DSP+HF, titration controlled".[^skw-01] | {ref}`060 <step-060>` |
| Ozone and ozonated water (O₃) | Wet chemical; oxidant | Ozonated-water pre-clean options; O₂/O₃ for the TEOS PSG route. | typical (not listed) | {ref}`039 <step-039>`, {ref}`043 <step-043>`, {ref}`089 <step-089>` |
| Isopropanol (IPA) | Solvent | Drying after wet benches and strips. | "spin or IPA dry" (Akrion); "dilute HF-last with IPA dry" (DNS); "IPA clean" (Mirra CMP).[^skw-01] | {ref}`009 <step-009>`, {ref}`013 <step-013>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`025 <step-025>`, {ref}`029 <step-029>`, {ref}`033 <step-033>`, {ref}`039 <step-039>`, {ref}`042 <step-042>`, {ref}`046 <step-046>`, {ref}`051 <step-051>`, {ref}`054 <step-054>`, {ref}`057 <step-057>`, {ref}`067 <step-067>`, {ref}`070 <step-070>`, {ref}`074 <step-074>`, {ref}`084 <step-084>`, {ref}`087 <step-087>`, {ref}`095 <step-095>` |
| Amine or semi-aqueous post-etch residue removers (EKC265/EKC270 class) | Solvent | Polymer and residue removal after contact, via, local-interconnect, metal, capacitor, seal-ring and pad etches, and in the sacrificial etch. | "Batch Rotational": "EKS265, EKC270 solvents, CO2 injected DI".[^skw-01] | {ref}`095 <step-095>`, {ref}`103 <step-103>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`130 <step-130>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`145 <step-145>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`160 <step-160>`, {ref}`163 <step-163>`, {ref}`166 <step-166>`, {ref}`169 <step-169>` |
| Post-CMP clean chemistry: dilute NH₄OH or TMAH, dilute HF, citric acid, surfactant; PVA brushes | Wet chemical; CMP consumable | Removal of slurry particles and metal contamination after oxide and tungsten polishes. | "AMAT Mirra CMP" with "Track ammonia clean" and "IPA clean";[^skw-01] the FY2023 10-K names "CMC Chemicals, Inc. (a subsidiary of Entegris) (process and chemical mechanical polishing chemicals)".[^sec-02] | {ref}`012 <step-012>`, {ref}`090 <step-090>`, {ref}`100 <step-100>`, {ref}`106 <step-106>`, {ref}`111 <step-111>`, {ref}`116 <step-116>`, {ref}`122 <step-122>`, {ref}`127 <step-127>`, {ref}`133 <step-133>`, {ref}`142 <step-142>`, {ref}`148 <step-148>`, {ref}`157 <step-157>` |
| Ultrapure (DI) water | Utility | Rinses, dilution of wet chemicals, CMP and post-CMP cleaning, developer rinse. | "CO2 injected DI" (batch rotational solvent tool); otherwise not listed.[^skw-01] | {ref}`001 <step-001>`, {ref}`004 <step-004>`, {ref}`007 <step-007>`, {ref}`009 <step-009>`, {ref}`012 <step-012>`, {ref}`013 <step-013>`, {ref}`014 <step-014>`, {ref}`016 <step-016>`, {ref}`017 <step-017>`, {ref}`021 <step-021>`, {ref}`022 <step-022>`, {ref}`025 <step-025>`, {ref}`026 <step-026>`, {ref}`029 <step-029>`, {ref}`030 <step-030>`, {ref}`033 <step-033>`, {ref}`035 <step-035>`, {ref}`039 <step-039>`, {ref}`041 <step-041>`, {ref}`042 <step-042>`, {ref}`044 <step-044>`, {ref}`046 <step-046>`, {ref}`049 <step-049>`, {ref}`051 <step-051>`, {ref}`052 <step-052>`, {ref}`054 <step-054>`, {ref}`055 <step-055>`, {ref}`057 <step-057>`, {ref}`060 <step-060>`, {ref}`061 <step-061>`, {ref}`064 <step-064>`, {ref}`067 <step-067>`, {ref}`068 <step-068>`, {ref}`070 <step-070>`, {ref}`071 <step-071>`, {ref}`074 <step-074>`, {ref}`077 <step-077>`, {ref}`078 <step-078>`, {ref}`081 <step-081>`, {ref}`084 <step-084>`, {ref}`085 <step-085>`, {ref}`087 <step-087>`, {ref}`090 <step-090>`, {ref}`093 <step-093>`, {ref}`095 <step-095>`, {ref}`100 <step-100>`, {ref}`102 <step-102>`, {ref}`106 <step-106>`, {ref}`107 <step-107>`, {ref}`108 <step-108>`, {ref}`111 <step-111>`, {ref}`113 <step-113>`, {ref}`114 <step-114>`, {ref}`116 <step-116>`, {ref}`118 <step-118>`, {ref}`119 <step-119>`, {ref}`122 <step-122>`, {ref}`124 <step-124>`, {ref}`125 <step-125>`, {ref}`127 <step-127>`, {ref}`129 <step-129>`, {ref}`130 <step-130>`, {ref}`133 <step-133>`, {ref}`137 <step-137>`, {ref}`138 <step-138>`, {ref}`139 <step-139>`, {ref}`140 <step-140>`, {ref}`142 <step-142>`, {ref}`144 <step-144>`, {ref}`145 <step-145>`, {ref}`148 <step-148>`, {ref}`152 <step-152>`, {ref}`153 <step-153>`, {ref}`154 <step-154>`, {ref}`155 <step-155>`, {ref}`157 <step-157>`, {ref}`159 <step-159>`, {ref}`160 <step-160>`, {ref}`162 <step-162>`, {ref}`163 <step-163>`, {ref}`165 <step-165>`, {ref}`166 <step-166>`, {ref}`168 <step-168>`, {ref}`169 <step-169>` |
| i-line positive photoresist (DNQ/novolak), including thick implant resist | Lithography | Implant block masks, relaxed etch masks and thick top levels. | "ASML I-line stepper", "ASML I-line scanner";[^skw-01] resist suppliers in both filings (table above).[^sec-01][^sec-02] | {ref}`004 <step-004>`, {ref}`007 <step-007>`, {ref}`014 <step-014>`, {ref}`017 <step-017>`, {ref}`022 <step-022>`, {ref}`026 <step-026>`, {ref}`030 <step-030>`, {ref}`035 <step-035>`, {ref}`041 <step-041>`, {ref}`044 <step-044>`, {ref}`049 <step-049>`, {ref}`052 <step-052>`, {ref}`055 <step-055>`, {ref}`064 <step-064>`, {ref}`068 <step-068>`, {ref}`071 <step-071>`, {ref}`078 <step-078>`, {ref}`081 <step-081>`, {ref}`085 <step-085>`, {ref}`137 <step-137>`, {ref}`139 <step-139>`, {ref}`152 <step-152>`, {ref}`154 <step-154>`, {ref}`159 <step-159>`, {ref}`162 <step-162>`, {ref}`165 <step-165>`, {ref}`168 <step-168>` |
| KrF (248 nm) chemically amplified positive photoresist | Lithography | Critical levels: active, poly, nitride cut, local-interconnect contact and line, contact, metals 1–4, vias 1–3 (per step-page readings). | "ASML DUV stepper", "ASML DUV scanner";[^skw-01] resist suppliers in both filings (table above).[^sec-01][^sec-02] | {ref}`004 <step-004>`, {ref}`061 <step-061>`, {ref}`078 <step-078>`, {ref}`093 <step-093>`, {ref}`102 <step-102>`, {ref}`107 <step-107>`, {ref}`113 <step-113>`, {ref}`118 <step-118>`, {ref}`124 <step-124>`, {ref}`129 <step-129>`, {ref}`139 <step-139>`, {ref}`144 <step-144>`, {ref}`154 <step-154>` |
| Organic BARC, inorganic ARC or dyed resist | Lithography | Reflectivity control on DUV levels and over metal; the ARC opened at {ref}`TUNARCE <step-036>`. | typical (not listed) | {ref}`004 <step-004>`, {ref}`035 <step-035>`, {ref}`036 <step-036>`, {ref}`041 <step-041>`, {ref}`061 <step-061>`, {ref}`078 <step-078>`, {ref}`093 <step-093>`, {ref}`102 <step-102>`, {ref}`107 <step-107>`, {ref}`113 <step-113>`, {ref}`118 <step-118>`, {ref}`124 <step-124>`, {ref}`129 <step-129>`, {ref}`137 <step-137>`, {ref}`139 <step-139>`, {ref}`144 <step-144>`, {ref}`152 <step-152>`, {ref}`154 <step-154>`, {ref}`159 <step-159>`, {ref}`162 <step-162>` |
| HMDS adhesion promoter | Lithography | Vapour prime before resist coat. | typical (not listed) | {ref}`004 <step-004>`, {ref}`007 <step-007>`, {ref}`014 <step-014>`, {ref}`017 <step-017>`, {ref}`022 <step-022>`, {ref}`026 <step-026>`, {ref}`030 <step-030>`, {ref}`035 <step-035>`, {ref}`041 <step-041>`, {ref}`044 <step-044>`, {ref}`049 <step-049>`, {ref}`052 <step-052>`, {ref}`055 <step-055>`, {ref}`061 <step-061>`, {ref}`064 <step-064>`, {ref}`068 <step-068>`, {ref}`071 <step-071>`, {ref}`078 <step-078>`, {ref}`081 <step-081>`, {ref}`085 <step-085>`, {ref}`093 <step-093>`, {ref}`102 <step-102>`, {ref}`107 <step-107>`, {ref}`118 <step-118>`, {ref}`129 <step-129>`, {ref}`144 <step-144>`, {ref}`159 <step-159>`, {ref}`165 <step-165>`, {ref}`168 <step-168>` |
| TMAH developer, 2.38 wt.% (0.26 N) | Lithography | Aqueous development of positive resist. | S-1: "Air Products & Chemicals, Inc., Moses Lake (developer)";[^sec-01] FY2023 10-K: "Moses Lake Industries Inc. (developer)".[^sec-02] | {ref}`004 <step-004>`, {ref}`007 <step-007>`, {ref}`014 <step-014>`, {ref}`017 <step-017>`, {ref}`022 <step-022>`, {ref}`026 <step-026>`, {ref}`030 <step-030>`, {ref}`035 <step-035>`, {ref}`041 <step-041>`, {ref}`044 <step-044>`, {ref}`049 <step-049>`, {ref}`052 <step-052>`, {ref}`055 <step-055>`, {ref}`061 <step-061>`, {ref}`064 <step-064>`, {ref}`068 <step-068>`, {ref}`071 <step-071>`, {ref}`078 <step-078>`, {ref}`081 <step-081>`, {ref}`085 <step-085>`, {ref}`093 <step-093>`, {ref}`102 <step-102>`, {ref}`107 <step-107>`, {ref}`113 <step-113>`, {ref}`118 <step-118>`, {ref}`124 <step-124>`, {ref}`129 <step-129>`, {ref}`137 <step-137>`, {ref}`139 <step-139>`, {ref}`144 <step-144>`, {ref}`152 <step-152>`, {ref}`154 <step-154>`, {ref}`159 <step-159>`, {ref}`162 <step-162>`, {ref}`165 <step-165>`, {ref}`168 <step-168>` |
| Edge-bead remover and rinse solvents (PGMEA, ethyl lactate, cyclohexanone) | Solvent; lithography | Edge-bead removal, back-rinse and rework. | typical (not listed) | {ref}`004 <step-004>`, {ref}`007 <step-007>`, {ref}`014 <step-014>`, {ref}`017 <step-017>`, {ref}`022 <step-022>`, {ref}`026 <step-026>`, {ref}`030 <step-030>`, {ref}`035 <step-035>`, {ref}`041 <step-041>`, {ref}`044 <step-044>`, {ref}`049 <step-049>`, {ref}`052 <step-052>`, {ref}`055 <step-055>`, {ref}`061 <step-061>`, {ref}`064 <step-064>`, {ref}`068 <step-068>`, {ref}`071 <step-071>`, {ref}`078 <step-078>`, {ref}`081 <step-081>`, {ref}`085 <step-085>`, {ref}`093 <step-093>`, {ref}`102 <step-102>`, {ref}`107 <step-107>`, {ref}`113 <step-113>`, {ref}`118 <step-118>`, {ref}`124 <step-124>`, {ref}`129 <step-129>`, {ref}`137 <step-137>`, {ref}`139 <step-139>`, {ref}`144 <step-144>`, {ref}`152 <step-152>`, {ref}`154 <step-154>`, {ref}`159 <step-159>`, {ref}`162 <step-162>`, {ref}`165 <step-165>`, {ref}`168 <step-168>` |
| Reticles (chrome on quartz, with pellicles; SEMI P1 blanks) | Lithography | One per mask step; see {ref}`masks-index`. | "Mask GDS to reticle"; "Reticle storage/handler/defect inspection".[^skw-01] | {ref}`004 <step-004>`, {ref}`007 <step-007>`, {ref}`014 <step-014>`, {ref}`017 <step-017>`, {ref}`022 <step-022>`, {ref}`026 <step-026>`, {ref}`030 <step-030>`, {ref}`035 <step-035>`, {ref}`041 <step-041>`, {ref}`044 <step-044>`, {ref}`049 <step-049>`, {ref}`052 <step-052>`, {ref}`055 <step-055>`, {ref}`061 <step-061>`, {ref}`064 <step-064>`, {ref}`068 <step-068>`, {ref}`071 <step-071>`, {ref}`078 <step-078>`, {ref}`081 <step-081>`, {ref}`085 <step-085>`, {ref}`093 <step-093>`, {ref}`102 <step-102>`, {ref}`107 <step-107>`, {ref}`113 <step-113>`, {ref}`118 <step-118>`, {ref}`124 <step-124>`, {ref}`129 <step-129>`, {ref}`137 <step-137>`, {ref}`139 <step-139>`, {ref}`144 <step-144>`, {ref}`152 <step-152>`, {ref}`154 <step-154>`, {ref}`159 <step-159>`, {ref}`162 <step-162>`, {ref}`165 <step-165>`, {ref}`168 <step-168>` |
| Exposure-tool consumables: KrF laser gas (Kr, F₂/Ne), mercury lamps | Lithography hardware | Light sources of the DUV and i-line tools. | typical (not listed) | {ref}`061 <step-061>`, {ref}`107 <step-107>`, {ref}`113 <step-113>`, {ref}`118 <step-118>`, {ref}`124 <step-124>`, {ref}`129 <step-129>`, {ref}`137 <step-137>`, {ref}`139 <step-139>`, {ref}`144 <step-144>`, {ref}`152 <step-152>`, {ref}`154 <step-154>`, {ref}`159 <step-159>`, {ref}`162 <step-162>`, {ref}`165 <step-165>`, {ref}`168 <step-168>` |
| Titanium sputter targets (Ti; reactive TiN) | Sputter target | Contact Ti/TiN liner; TiN local interconnect; TiN via liners; Ti underlayer of the metal stacks. | "Collimated Ti", "ESC TiN", "Imp TiN" under "AMAT PVD Metal";[^skw-01] S-1: "Honeywell Electronic Materials, Inc. (metal sputter targets)";[^sec-01] FY2023 10-K adds "JX Metals USA, Inc. (metal sputtering targets)".[^sec-02] | {ref}`097 <step-097>`, {ref}`101 <step-101>`, {ref}`109 <step-109>`, {ref}`112 <step-112>`, {ref}`120 <step-120>`, {ref}`123 <step-123>`, {ref}`131 <step-131>`, {ref}`134 <step-134>`, {ref}`146 <step-146>`, {ref}`149 <step-149>`, {ref}`161 <step-161>` |
| Aluminium–copper sputter targets (Al–0.5 wt.% Cu) | Sputter target | Conductor of metals 1–5. | "Aluminum both pure and Cu doped";[^skw-01] Cypress S8 report: "Metal 1: 100A Ti / 3200A Al-0.5%Cu / 300A TiW".[^cyp-qtp-113005] | {ref}`112 <step-112>`, {ref}`123 <step-123>`, {ref}`134 <step-134>`, {ref}`149 <step-149>`, {ref}`161 <step-161>` |
| Titanium–tungsten sputter targets (Ti:W, 10 wt.% Ti) | Sputter target | Cap of the metal stacks; MiM top plates; possible underlayer of metals 3–5. | "TiW" under "AMAT PVD Metal" and on both metal etchers.[^skw-01] | {ref}`112 <step-112>`, {ref}`123 <step-123>`, {ref}`134 <step-134>`, {ref}`136 <step-136>`, {ref}`149 <step-149>`, {ref}`151 <step-151>`, {ref}`161 <step-161>` |
| Oxide CMP slurry (fumed or colloidal silica in KOH or NH₄OH); ceria or additive slurry for nitride selectivity | CMP consumable | STI, pre-metal-dielectric and inter-level oxide polishes. | "AMAT Mirra CMP" with "oxide" and "nitride";[^skw-01] slurry product not named. | {ref}`012 <step-012>`, {ref}`090 <step-090>`, {ref}`106 <step-106>`, {ref}`116 <step-116>`, {ref}`127 <step-127>`, {ref}`142 <step-142>`, {ref}`157 <step-157>` |
| Tungsten CMP slurry (alumina or silica with H₂O₂, Fe(NO₃)₃ or KIO₃) | CMP consumable | Removal of field tungsten after each plug fill. | "tungsten" and "high selectivity tungsten" under "AMAT Mirra CMP".[^skw-01] | {ref}`100 <step-100>`, {ref}`111 <step-111>`, {ref}`122 <step-122>`, {ref}`133 <step-133>`, {ref}`148 <step-148>` |
| CMP pads, diamond conditioners, carrier films, membranes, retaining rings | CMP consumable | Consumed by every polish. | typical (not listed) | {ref}`012 <step-012>`, {ref}`090 <step-090>`, {ref}`100 <step-100>`, {ref}`106 <step-106>`, {ref}`111 <step-111>`, {ref}`116 <step-116>`, {ref}`122 <step-122>`, {ref}`127 <step-127>`, {ref}`133 <step-133>`, {ref}`142 <step-142>`, {ref}`148 <step-148>`, {ref}`157 <step-157>` |
| Furnace ware: quartz or SiC tubes, boats, baffles, liners | Hardware | Batch oxidation, LPCVD and alloy furnaces. | Tool vendor only: "Furnaces are all made by Aviza".[^skw-01] | {ref}`002 <step-002>`, {ref}`003 <step-003>`, {ref}`010 <step-010>`, {ref}`040 <step-040>`, {ref}`043 <step-043>`, {ref}`047 <step-047>`, {ref}`048 <step-048>`, {ref}`058 <step-058>`, {ref}`059 <step-059>`, {ref}`063 <step-063>`, {ref}`076 <step-076>`, {ref}`080 <step-080>`, {ref}`096 <step-096>`, {ref}`170 <step-170>` |
| Plasma, CVD and PVD chamber parts: focus rings, liners, ESC parts, showerheads, domes, shields, collimators, endpoint windows, spin-chuck nozzles | Hardware | Scheduled replacement on etch, CVD, PVD and single-wafer wet tools. | typical (not listed) | {ref}`005 <step-005>`, {ref}`006 <step-006>`, {ref}`011 <step-011>`, {ref}`036 <step-036>`, {ref}`042 <step-042>`, {ref}`058 <step-058>`, {ref}`059 <step-059>`, {ref}`060 <step-060>`, {ref}`062 <step-062>`, {ref}`063 <step-063>`, {ref}`076 <step-076>`, {ref}`077 <step-077>`, {ref}`079 <step-079>`, {ref}`089 <step-089>`, {ref}`091 <step-091>`, {ref}`094 <step-094>`, {ref}`097 <step-097>`, {ref}`099 <step-099>`, {ref}`101 <step-101>`, {ref}`103 <step-103>`, {ref}`104 <step-104>`, {ref}`105 <step-105>`, {ref}`108 <step-108>`, {ref}`109 <step-109>`, {ref}`110 <step-110>`, {ref}`112 <step-112>`, {ref}`114 <step-114>`, {ref}`115 <step-115>`, {ref}`117 <step-117>`, {ref}`119 <step-119>`, {ref}`120 <step-120>`, {ref}`121 <step-121>`, {ref}`123 <step-123>`, {ref}`125 <step-125>`, {ref}`126 <step-126>`, {ref}`128 <step-128>`, {ref}`130 <step-130>`, {ref}`131 <step-131>`, {ref}`132 <step-132>`, {ref}`134 <step-134>`, {ref}`135 <step-135>`, {ref}`136 <step-136>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`141 <step-141>`, {ref}`143 <step-143>`, {ref}`145 <step-145>`, {ref}`146 <step-146>`, {ref}`147 <step-147>`, {ref}`149 <step-149>`, {ref}`150 <step-150>`, {ref}`151 <step-151>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`156 <step-156>`, {ref}`158 <step-158>`, {ref}`160 <step-160>`, {ref}`161 <step-161>`, {ref}`163 <step-163>`, {ref}`164 <step-164>`, {ref}`166 <step-166>`, {ref}`167 <step-167>`, {ref}`169 <step-169>` |
| RTP consumables: tungsten-halogen lamps, quartz windows, edge rings, pyrometer calibration; cooling water and CDA/N₂ | Hardware; utility | Rapid thermal anneals and silicidation (facility table for the Heatpulse family[^ag-8108]). | typical (not listed) | {ref}`034 <step-034>`, {ref}`063 <step-063>`, {ref}`075 <step-075>`, {ref}`088 <step-088>`, {ref}`092 <step-092>`, {ref}`098 <step-098>` |
| Exhaust abatement and waste treatment: HCl-tolerant exhaust and NH₄Cl traps, scrubbing of arsenic-, chlorine-, fluorine- and HF-bearing exhaust, acid-waste neutralisation, CMP slurry waste; pump oil | Abatement | Handles by-products and spent chemicals (see *Safety and abatement* below). | typical (not listed) | {ref}`003 <step-003>`, {ref}`012 <step-012>`, {ref}`048 <step-048>`, {ref}`051 <step-051>`, {ref}`058 <step-058>`, {ref}`060 <step-060>`, {ref}`067 <step-067>`, {ref}`076 <step-076>`, {ref}`086 <step-086>`, {ref}`087 <step-087>`, {ref}`099 <step-099>`, {ref}`110 <step-110>`, {ref}`111 <step-111>`, {ref}`114 <step-114>`, {ref}`116 <step-116>`, {ref}`121 <step-121>`, {ref}`122 <step-122>`, {ref}`125 <step-125>`, {ref}`127 <step-127>`, {ref}`132 <step-132>`, {ref}`133 <step-133>`, {ref}`140 <step-140>`, {ref}`142 <step-142>`, {ref}`147 <step-147>`, {ref}`148 <step-148>`, {ref}`155 <step-155>`, {ref}`157 <step-157>`, {ref}`163 <step-163>`, {ref}`166 <step-166>`, {ref}`169 <step-169>` |
| Probe cards, needles, tip-cleaning media, calibration standards | Test | Parametric e-test. | "HP 4062UX" with "DC, capacitance, pulse generator, frequency counter"; "Engineering manual Probe Station".[^skw-01] | {ref}`171 <step-171>` |

(materials-reram)=
## The sky130B ReRAM module

The `sky130B` variant of the PDK adds a resistive-memory tier between
metal 1 and metal 2 that is not part of the 171-step list used here;
the {ref}`sky130B ReRAM <overview-sky130b-reram>` page describes it as
a module, and its materials are kept out of the table above for that
reason. SkyWater's documentation for the device states that "a
HfO2-based RRAM layer is fabricated within the BEOL
process";[^reram-background] it does not name the electrodes or the
deposition chemistry. A typical atomic-layer-deposition route for the
hafnium oxide uses HfCl₄ and water,[^pat-rram-oxide-tsmc] and
SkyWater's capability list includes ALD of "HfO2" and of "TiN".[^skw-01]
The ReRAM page notes that the published hafnium-oxide cells it cites
use TiN electrodes, some with a thin Ti or Hf layer next to the oxide;
gives BCl₃/O₂ plasma, fluorine- or argon-based plasmas and dilute HF
as typical etch chemistries; describes silicon oxide and nitride for
encapsulation; and reads the upper vias as using TiN, tungsten and
WF₆ as the base via 1 does (inference on that page).

<!-- footnotes -->

[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^semi-m1]: SEMI, *SEMI M1 — Specification for Polished Single Crystal
    Silicon Wafers*, SEMI Standards store listing.
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
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing". <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; "Raw materials" paragraph.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
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
    retrieved 2026-09-13; tab "Sheet1" lists the 171 steps (number, code and
    description). <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
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
