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
sputtering tools or the tungsten CVD tool, and for the CVD tools names
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
stacks and the TEOS/nitride passivation[^cyp-qtp-113005][^cyp-qtp-123907][^cyp-qtp-014807]
— and the PDK documentation gives thicknesses and permittivities for
the SKY130 stack.[^pdk-03][^pdk-04] These are the sources of the
{ref}`films table <materials-films>` below.

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
| Silane (SiH₄) | Precursor | HDP-CVD oxide and PSG; PECVD oxide, nitride and oxynitride; LPCVD amorphous-silicon gate; tungsten nucleation. | Named only in film names: "PECVD silane oxide/nitride/oxynitride, C1", "LPCVD silane oxide"; the gate film is "LPCVD polysilicon (undoped), both amorphous and crystalline".[^skw-01] | {ref}`011 <step-011>`, {ref}`048 <step-048>`, {ref}`058 <step-058>`, {ref}`059 <step-059>`, {ref}`076 <step-076>`, {ref}`080 <step-080>`, {ref}`089 <step-089>`, {ref}`091 <step-091>`, {ref}`099 <step-099>`, {ref}`104 <step-104>`, {ref}`105 <step-105>`, {ref}`110 <step-110>`, {ref}`115 <step-115>`, {ref}`117 <step-117>`, {ref}`121 <step-121>`, {ref}`126 <step-126>`, {ref}`128 <step-128>`, {ref}`132 <step-132>`, {ref}`135 <step-135>`, {ref}`141 <step-141>`, {ref}`143 <step-143>`, {ref}`147 <step-147>`, {ref}`150 <step-150>`, {ref}`156 <step-156>`, {ref}`158 <step-158>`, {ref}`164 <step-164>`, {ref}`167 <step-167>` |
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
| Pad (base) oxide | {ref}`BOX <step-002>` | none | Cypress SONOS patent: pad oxide "from about 10 nanometers (nm) to about 20 nm"[^pat-04] | Thermal SiO₂ of the order of 10–20 nm (typical) |
| Isolation nitride | {ref}`ISONIT <step-003>` | none | AmberWave STI patent: mask nitride "500-2000 Å"[^pat-sti-amberwave] | LPCVD Si₃N₄ of the order of 100–200 nm; removed at {ref}`NS19 <step-013>` |
| Trench liner oxide | {ref}`LINOX <step-010>` | none | Spansion/Cypress-lineage STI patent: liner "to a thickness of approximately 100-300 Å"[^pat-sti-cr] | Thermal SiO₂ of the order of 10–30 nm |
| Field (fill) oxide, "FOX K=3.9" | {ref}`FILOX <step-011>`, polished at {ref}`CMPNIT <step-012>` | Field-oxide top at 0.3262 µm on the diagram's scale;[^pdk-04] field-oxide step under poly 0.07 µm[^pdk-03] | — | HDP-CVD oxide; fill thickness not public |
| ONO stack: tunnel oxide, (oxy)nitride, blocking oxide | {ref}`ONO <step-040>` | none | Cypress patent: tunnel oxide "less than about 25 Å", top oxide "less than about 50 Å"[^pat-01] | Furnace oxidation and LPCVD from SiH₂Cl₂, NH₃ and N₂O; SKY130 values not public |
| Thick gate oxide | {ref}`GOX100 <step-043>`, thickened at {ref}`LVGOX <step-047>` | "All VHV devices use 110A gate oxide thickness just like standard 5.0V Vcc devices";[^pdk-hv] 5 V NMOS model `toxe` 1.16e-08 (11.6 nm)[^pdk-model-nfet5v] | — | Thermal oxide grown somewhat thinner than 11 nm here |
| Thin gate oxide | {ref}`LVGOX <step-047>` | 1.8 V NMOS model `toxe` 4.148e-09 (4.148 nm)[^pdk-model-nfet01v8] | "Nitrided gate oxide" special module[^skw-01] | Thermal oxide, possibly nitrided |
| Gate silicon ("poly") | {ref}`SAGD <step-048>` | "poly thickness" 0.18 µm;[^pdk-03] 0.18 µm on the diagram[^pdk-04] | "LPCVD polysilicon (undoped), both amorphous and crystalline"[^skw-01] | One undoped LPCVD amorphous-silicon layer, doped by implant |
| Gate nitride cap and oxide cap | {ref}`GATENIT <step-058>`, {ref}`POC <step-059>` | "poly cap after SPE" 0.2 µm[^pdk-03] | — | Nitride under oxide; as-deposited thicknesses not public |
| Re-oxidation (screen) oxide | {ref}`IOX45 <step-063>` | none used on the step page | — | Thin thermal oxide; thickness, ambient and tool not public |
| Spacer nitride, "SPNIT K=7.5" | {ref}`SPNIT <step-076>`, etched at {ref}`SPE <step-077>` | Permittivity 7.5; no thickness[^pdk-04] | "LPCVD BTBAS low temp nitride" is on the capability list[^skw-01] | Conformal nitride; DCS, BTBAS or PECVD route |
| Spacer oxide | {ref}`SPOX <step-080>` | "oxide spacer" 0.05 µm[^pdk-03] | — | Blanket oxide left through the source/drain implants |
| Pre-metal dielectric, "PSG K=3.9", and cap oxide | {ref}`PSG <step-089>`, polished at {ref}`CMPP <step-090>`; cap {ref}`NCAPOX <step-091>` | 0.6099 µm and 0.4299 µm labels, matching field-oxide top (0.3262 µm) to `li` bottom (0.9361 µm) and field-poly top to `li` bottom (our arithmetic);[^pdk-04] "Pre-LI ILD thickness" 0.5 µm[^pdk-03] | — | HDP PSG polished close to the gate caps, then an undoped cap of about 0.2–0.3 µm (inferred) |
| Contact liner Ti/TiN (and titanium silicide) | {ref}`TI/TIN1 <step-097>`; silicide formed at {ref}`CSIL <step-098>` | none | — | IMP Ti and TiN of the order of 10–30 nm each (typical) |
| Tungsten plugs: `licon1`, `mcon`, `via`, `via2`, `via3` | {ref}`WDEP <step-099>`, {ref}`WDEP2 <step-110>`, {ref}`WDEP3 <step-121>`, {ref}`WDEP4 <step-132>`, {ref}`WDEP5 <step-147>`; polished at {ref}`WCMPLI <step-100>`, {ref}`WCMP2 <step-111>`, {ref}`WCMP3 <step-122>`, {ref}`WCMP4 <step-133>`, {ref}`WCMP5 <step-148>` | Via heights 0.27 µm (via 1), 0.42 µm (via 2), 0.39 µm (via 3)[^pdk-04] | — | Blanket CVD tungsten; deposited thickness not public |
| TiN plug liners | {ref}`TIN2 <step-109>`, {ref}`TIN3 <step-120>`, {ref}`TIN4 <step-131>`, {ref}`TIN5 <step-146>` | none | — | IMP TiN, a few tens of nanometres on the field (typical) |
| Local interconnect, `li` | {ref}`LITIN <step-101>` | 0.1 µm;[^pdk-04] "LI1 thickness for antenna ratio calculations" 0.1 µm[^pdk-03] | Efabless lecture: "Titanium Nitride (TiN)"[^ann-16] | Sputtered TiN |
| Local-interconnect nitride, "LINT K=7.3" | {ref}`LINIT <step-104>` | 0.075 µm[^pdk-04] | — | Low-temperature nitride (PECVD or BTBAS) |
| "NILD2 K=4.05" | {ref}`NILD2 <step-105>`, polished at {ref}`CMPL <step-106>` | 0.265 µm between `li` and `metal1`[^pdk-04] | — | HDP or PECVD TEOS oxide, about 0.5–0.7 µm as deposited (inferred) |
| Metal 1 | {ref}`TIAL6 <step-112>` | 0.36 µm;[^pdk-04] 0.35 µm antenna value[^pdk-03] | "Metal 1: 100A Ti / 3200A Al-0.5%Cu / 300A TiW";[^cyp-qtp-113005] 2014 change to "150A Ti/250A TiN/3200A Al 0.5% Cu/90A Ti/500A TiN"[^cyp-qtp-123907] | Ti/Al–Cu/TiW |
| "NILD3 K=4.5" with "NILD3_C K=3.5" (0.030 µm) | {ref}`NILD3 <step-115>`, polished at {ref}`CMPM <step-116>`; cap {ref}`NCAPOX3 <step-117>` | Via-1 height 0.27 µm[^pdk-04] | — | Gap-fill oxide (fluorinated option) and cap |
| Metal 2 | {ref}`TIAL12 <step-123>` | 0.36 µm;[^pdk-04] 0.35 µm antenna value[^pdk-03] | "Metal 2: 100A Ti / 3200A Al-0.5%Cu / 300A TiW"[^cyp-qtp-113005] | As metal 1 |
| "NILD4 K=4.2" with "NILD4_C K=3.5" (0.030 µm) | {ref}`NILD4 <step-126>`, polished at {ref}`CMPM2 <step-127>`; cap {ref}`NCAPOX4 <step-128>` | Via-2 height 0.42 µm[^pdk-04] | — | As NILD3 |
| Metal 3 | {ref}`WTIAL3 <step-134>` | 0.845 µm;[^pdk-04] antenna values 0.85, 0.8 or 2 µm by flow[^pdk-03] | "Metal 3: 150A Ti / 7200A Al-0.5%Cu / 300A TiW";[^cyp-qtp-113005] S8DI "Metal 3: 500A TiW/21,250A Al 0.5% Cu/300A TiW"[^cyp-qtp-123907] | Ti or TiW underlayer, about 0.8 µm Al–Cu, TiW cap |
| MiM capacitor dielectric ("CAPILD" on the `cap_mim` cross-section) | {ref}`CAPILD <step-135>`, {ref}`CAPILD2 <step-150>` | No thickness; `CMIMA` and `CMIM2A` 2 fF/µm²[^pdk-07] | "PECVD silane oxide/nitride/oxynitride, C1"[^skw-01] | PECVD oxynitride (inference); 18–33 nm for k = 4–7.5 (arithmetic) |
| MiM top plate, `capm` and `cap2m` | {ref}`CAPTIW1 <step-136>`, {ref}`CAPTIW2 <step-151>` | `RSCAPM` 5.8 Ω/sq and the same for the second plate[^pdk-07] | "TiW"[^skw-01] | TiW of roughly 0.1 µm (inference from sheet resistance) |
| "NILD5 K=4.1" | {ref}`NILD5 <step-141>`, polished at {ref}`CMPM3 <step-142>`; cap {ref}`NCAPOX5 <step-143>` | Via-3 height 0.39 µm[^pdk-04] | — | Gap-fill oxide and cap |
| Metal 4 | {ref}`WTIAL4 <step-149>` | 0.845 µm;[^pdk-04] antenna values 0.8 or 2 µm by flow[^pdk-03] | none | Repeat of metal 3 (inference) |
| "NILD6 K=4.0" | {ref}`NILD6 <step-156>`, polished at {ref}`CMPM4 <step-157>`; cap {ref}`NCAPOX6 <step-158>` | Via-4 height 0.505 µm[^pdk-04] | — | Gap-fill oxide and cap |
| Metal 5 | {ref}`WTIAL5 <step-161>` | 1.26 µm;[^pdk-04] antenna values 1.2 or 2 µm by flow[^pdk-03] | none | Ti or TiW underlayer, about 1.2 µm Al–Cu, TiW cap; also fills via 4 (inference) |
| "TOPOX K=3.9" | {ref}`NFUSOX <step-164>` | 0.09 µm on the metal-5 top, 0.070 µm on its sidewall[^pdk-04] | Fab 4 passivation "1000Å TEOS / 9000Å PECVD Nitride"[^cyp-qtp-014807] and "1000A TEOS/9000A Si3N4"[^cyp-qtp-123907] | Thin undoped oxide |
| "TOPNIT K=7.5" | {ref}`NTSD <step-167>` | 0.54 µm on the metal-5 top, 0.4223 µm on its sidewall[^pdk-04] | As above, and "7000 +/- 2000A Nitride"[^cyp-qtp-113005] | PECVD silicon nitride |
| "PI1 K=2.94" | no step | Drawn over the passivation, no thickness[^pdk-04] | "Polyimide cure" is a furnace entry[^skw-01] | Not part of the step list |

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
  as an inter-metal dielectric.[^denison-1996]
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
way. The differences below are recorded as found; this page does not
decide between them, and the step pages are unchanged.

### Chemistries of analogous steps

* **Implant-strip wet cleans.** Eleven of the fourteen implant-strip
  pages list SC-2 (or its hydrochloric acid) after SPM and SC-1
  ({ref}`DNIS <step-009>`,
  {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`,
  {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`,
  {ref}`PWDEIS <step-033>`, {ref}`UPRIS <step-057>`,
  {ref}`ASTIS <step-067>`, {ref}`LDASTIS <step-074>`,
  {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`); three list SPM and
  SC-1 only ({ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`,
  {ref}`HVASTIS <step-070>`). Only {ref}`PWDEIS <step-033>` lists dilute
  HF ("only if the oxide is removed").
* **Ash additions after implants.** A small CF₄ addition is used
  "for some recipes" at {ref}`DNIS <step-009>`; it "would normally be
  omitted" at {ref}`LVTNIS <step-016>`, "is normally omitted" at
  {ref}`LVTPIS <step-021>` and {ref}`ASTIS <step-067>`, and "would be
  omitted, we infer" at {ref}`HVASTIS <step-070>` and
  {ref}`LDASTIS <step-074>`; the other strips' resources sections do
  not mention it, although the recipe outlines of
  {ref}`P1IS <step-051>`, {ref}`PDIS <step-084>` and
  {ref}`NSDIS <step-087>` say CF₄ is avoided or, by inference, left
  out. Water
  vapour appears at {ref}`PRIS <step-054>`, {ref}`PDIS <step-084>` and
  {ref}`NSDIS <step-087>`, and NH₃ at the last two only. SkyWater's
  asher entries list NH3 (Iridia) and CF4 (Iridia, Mattson) but no
  water vapour.[^skw-01]
* **Post-CMP cleans.** For oxide polishes the listed chemistry is
  "dilute NH₄OH / surfactant / dilute HF" ({ref}`CMPNIT <step-012>`),
  "dilute NH₄OH, dilute HF" ({ref}`CMPP <step-090>`), "dilute NH₄OH"
  alone ({ref}`CMPL <step-106>`) and "dilute NH₄OH, possibly dilute
  HF" ({ref}`CMPM <step-116>` to {ref}`CMPM4 <step-157>`). For tungsten
  polishes it is "dilute NH₄OH, citric acid, dilute HF"
  ({ref}`WCMPLI <step-100>`), "dilute NH₄OH or TMAH, possibly dilute
  HF" ({ref}`WCMP2 <step-111>` to {ref}`WCMP4 <step-133>`) and "dilute
  NH₄OH or TMAH" without HF ({ref}`WCMP5 <step-148>`). Pads are
  "IC1000/Suba IV class" on {ref}`CMPP <step-090>`,
  {ref}`WCMPLI <step-100>` and {ref}`CMPL <step-106>`, "polyurethane"
  or "stacked polyurethane" on six other polish pages, and unqualified
  on {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>` and
  {ref}`CMPM4 <step-157>`.
* **The two MiM plate etches.** {ref}`CAPME <step-138>` lists "SF₆ or
  CF₄, Cl₂ and/or BCl₃, Ar or N₂"; {ref}`CAP2ME <step-153>` lists "Cl₂
  or Br₂ (or HBr), a small flow of CHF₃, CF₄ or CH₂F₂, and Ar or He".
  Both pages read the plate as TiW, and the PDK calls the two
  capacitor constructions "identical".[^pdk-07] The two pages also
  quote different subsets of SkyWater's poly/silicon etcher gases
  (Cl₂, CF₄ and SF₆ against Cl₂, HBr, CF₄ and CHF₃).
* **Metal etches.** The cap breakthrough is "CF₄ or SF₆" at
  {ref}`MM1E <step-114>` and {ref}`MM2E <step-125>`, "CF₄ or CHF₃" at
  {ref}`MM3E <step-140>` and {ref}`MM4E <step-155>`, and "a fluorine-
  or chlorine-bearing mixture" at {ref}`MM5E <step-163>`; the ash is
  "O₂/N₂ and H₂/N₂" on the first two and "O₂/N₂" on the last three; CH₄
  is a possible additive on the first two only. {ref}`MM1E <step-114>`
  and {ref}`MM2E <step-125>` say "SkyWater names Cl₂ and CF₄ on its
  etchers", while the metal-3 to metal-5 pages add that "SkyWater lists
  no gases for its metal etchers"; the capability list's metal-etch
  entries ("Lam 9600, Al, TiW, TiN, Pt"; "Lam 2300 Versys, Al, TiW, TiN,
  Nb, Pt") carry no gases.[^skw-01]
* **Contact, via and seal-ring oxide etches.** C₂F₆ is a possible
  addition at {ref}`LICM1E <step-094>` but a listed gas at
  {ref}`CTME <step-108>`, {ref}`VIME <step-119>`,
  {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`,
  {ref}`VIM4E <step-160>` and {ref}`NSME <step-166>`. The optional
  additions are "CO or N₂" on CTME, VIME and VIM2E and "CO" on VIM3E and
  VIM4E. Forming gas or CF₄ in the ash appears on CTME, VIME and VIM2E
  but not on VIM3E, VIM4E or NSME, and {ref}`LICM1E <step-094>` lists no
  post-etch solvent, which the other contact and via etches do.
* **HMDS on BARC levels.** HMDS is listed with a BARC or ARC at
  {ref}`FOM <step-004>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`,
  {ref}`P1M <step-061>`, {ref}`NPCM <step-078>`,
  {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`,
  {ref}`CTM1 <step-107>`, {ref}`VIM <step-118>`,
  {ref}`VIM2 <step-129>`, {ref}`VIM3 <step-144>` and
  {ref}`VIM4 <step-159>`, but not at {ref}`MM1 <step-113>`,
  {ref}`MM2 <step-124>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`,
  {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>` or
  {ref}`MM5 <step-162>`; the MM1, CAPM and MM5 recipe outlines say
  HMDS is not used on metal, while MM2, MM3, CAP2M and MM4 give no
  reason.
* **Developer strength.** Six resources sections give it as
  "2.38 %" ({ref}`FOM <step-004>`, {ref}`TUNM <step-035>`,
  {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`,
  {ref}`RPM <step-049>`, {ref}`P1M <step-061>`), 23 as "0.26 N", and
  seven without a strength. These are two expressions of one solution:
  the {ref}`lithography category page <category-lithography>` gives the
  industry-standard strength as "0.26 N (2.38 wt.%)".
* **Cap-oxide carriers.** The pages give "helium or argon diluent"
  ({ref}`NCAPOX <step-091>`), "helium or nitrogen carrier"
  ({ref}`NCAPOX3 <step-117>`, {ref}`NCAPOX4 <step-128>`) and "helium
  carrier" ({ref}`NCAPOX5 <step-143>`, {ref}`NCAPOX6 <step-158>`,
  {ref}`NFUSOX <step-164>`) for what the pages describe as the same
  kind of film.
* **RTA ambient.** {ref}`RTAI <step-034>`, {ref}`RTAD2 <step-092>` and
  {ref}`CSIL <step-098>` cite SkyWater for nitrogen and argon as the
  process ambient; {ref}`TIPRTAD <step-075>` and {ref}`RTAD <step-088>`
  write "likely ambient; SkyWater's list gives the tool's gases". The
  list gives the tool's gases, "NH3, Ar, N2, O2", and no
  ambient for any step.[^skw-01]

### Supplier statements

* **Developer.** {ref}`P1M <step-061>` says the developer is "supplied
  by Air Products"; other pages say "Air Products per the S-1" or that
  the S-1 "names Air Products (Moses Lake) as a developer supplier".
  The S-1 names "Air Products & Chemicals, Inc., Moses Lake
  (developer)" and the fiscal 2023 10-K "Moses Lake Industries Inc.
  (developer)"; neither ties a developer to a layer.[^sec-01][^sec-02]
* **Dates of supplier lists.** Most front-end pages cite both filings
  for gas suppliers (Air Products, Praxair, Linde, Airgas), while most
  pages from {ref}`PSG <step-089>` onwards cite the S-1 alone (Air
  Products, Praxair). The CMP pages that name a chemical supplier
  ({ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`,
  {ref}`CMPL <step-106>`) name KMG Chemicals from the S-1; none cites
  the 10-K's "CMC Chemicals, Inc. (a subsidiary of Entegris) (process
  and chemical mechanical polishing chemicals)".[^sec-02] The
  lithography pages name the S-1's three photoresist suppliers, not the
  10-K's four. {ref}`TI/TIN1 <step-097>` and {ref}`LITIN <step-101>`
  name Honeywell as the target supplier; the later PVD pages add JX
  Metals from the 10-K.

### Spellings and transcriptions against SkyWater's page

* SkyWater writes "Gasonic PEP"; 31 step pages write "Gasonics PEP"
  (some pages use both forms).
* SkyWater writes "EKS265, EKC270 solvents"; 15 pages quote that, and
  seven describe the chemistry as "EKC265/270" or "EKC265/EKC270"
  class. The page does not say whether "EKS265" and "EKC265" are the
  same product.
* SkyWater writes "Mattson Aspen2", "Davinci" and "TEL ProZ Lithius
  track"; many pages write "Aspen 2", "DaVinci" and "TEL ProZ/Lithius".
* SkyWater writes "HBR" in the DPSII entry and "HBr" elsewhere;
  {ref}`TUNARCE <step-036>` and {ref}`ONOME <step-042>` quote the DPSII
  entry with "HBr".
* SkyWater writes "Sulfuric"; the step pages use "sulphuric" outside
  quotations, following this reference's British spelling. The pages
  themselves use both "novolac" ({ref}`FOM <step-004>`,
  {ref}`DNM <step-007>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`)
  and "novolak" (the other pages and the lithography category page).
* {ref}`DNIS <step-009>` describes the Akrion bench as having "spin
  and IPA drying"; SkyWater writes "spin or IPA dry". Some pages join
  sub-items of the list into one quotation — {ref}`GOX100 <step-043>`
  quotes "Furnaces are all made by Aviza: wet oxidation to 1150C, dry
  oxidation to 1150C", where the page has separate lines and no colon,
  and {ref}`CAP2ME <step-153>` quotes "Batch Rotational (EKS265, EKC270
  solvents …)".[^skw-01]

### Open questions

* **Entries not explained.** SkyWater's LPCVD nitride entry reads
  "with NH3 and also DH3", and its single-wafer entry lists "DSP+HF";
  the page expands neither, and no step page discusses "DH3".[^skw-01]
  The step pages describe furnace nitride from dichlorosilane and
  ammonia, a precursor the list does not name.
* **"PECVD Tungsten".** SkyWater lists "Lam/Novellus PECVD
  Tungsten";[^skw-01] the step pages describe the plug fill as chemical
  vapour deposition from WF₆ reduced by hydrogen, with a silane or
  diborane nucleation layer. {ref}`WDEP2 <step-110>` to
  {ref}`WDEP5 <step-147>` read the wording as a label for the tungsten
  CVD tool rather than evidence of a plasma-assisted deposition;
  {ref}`WDEP <step-099>` quotes it without comment. No public source
  clarifies it.
* **Listed but unused.** The list names "Cobalt" among the PVD films,
  "Polyimide cure" and "Atmospheric selective oxidation" among the
  furnace processes, and "CO2 injected DI" and "IPA clean" among the
  cleans.[^skw-01] No step page's resources section lists a cobalt
  target, a polyimide or a selective oxidation; the
  {ref}`TIAL6 <step-112>` page mentions the cobalt entry and the
  {ref}`NTSD <step-167>` page the polyimide cure, no step page mentions
  the two cleans, and only {ref}`CMPM4 <step-157>` quotes the Mirra's
  "Track ammonia clean". The PDK stack diagram draws a polyimide, "PI1
  K=2.94", for which the step list has no step.[^pdk-04]
* **The PSG dimension labels.** {ref}`PSG <step-089>` describes the
  stack diagram's 0.6099 µm label as the dielectric "over the gate
  region". The diagram gives no region for it; the value equals the
  distance from the field-oxide top (0.3262 µm) to the `li` bottom
  (0.9361 µm), and 0.4299 µm equals the distance from the top of the
  0.18 µm field poly to the `li` bottom (our arithmetic).[^pdk-04]
* **Diagram labels without a step reading.** The stack diagram also
  carries an "IOX K=3.9" label and dimensions of 0.006 µm, 0.0431 µm
  and 0.121 µm that no step page, including {ref}`IOX45 <step-063>`,
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
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098 B1,
    granted 2014-08-05. <https://patents.google.com/patent/US8796098B1/en>
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
[^jolley-1998]: R. Jolley, "Applications of Tetramethylammoninium
    Hydroxide (TMAH) as a Post Tungsten CMP Cleaning Mixture", *Solid
    State Phenomena* **65–66**, 105–108 (1998).
    <https://doi.org/10.4028/www.scientific.net/SSP.65-66.105>
