(machines-index)=
# Machines

This page indexes the manufacturing equipment named on the step pages of
this reference. It groups the equipment into machine classes, says what
each class does in the SKY130 flow, quotes what SkyWater has published
about its own tools of that class, and lists the steps that use it. It
is compiled from the two machine sections that every step page carries,
"Machines typically used" and "Machines likely used at SkyWater", read
on all 171 pages; it adds no evidence of its own.

## Equipment classes in a 200 mm, 130 nm fab

A fab of this kind does not have one tool per step. SkyWater's S-1
registration statement says that the Bloomington fab "can produce up to
156,000 wafers per year (depending on the product mix) and has at least
522 well-maintained fab and sort tools",[^sec-01] and its annual report
for 2023 that "CMOS process flows for a number of different node
dimensions are offered ranging from 90 nm—350 nm" in the same 200 mm
fab.[^sec-02] The 171 steps of SKY130 therefore share tools with one
another and with other flows, and the step pages describe equipment by
class. The classes follow the unit processes of the category pages:

* **Thermal processing** — batch vertical furnaces, used for oxidation,
  LPCVD, anneals and the hydrogen alloy, and single-wafer rapid thermal
  processors ({ref}`category-oxidation`, {ref}`category-anneal`).
* **Thin-film deposition** — single-wafer PECVD and HDP-CVD systems for
  dielectrics, CVD reactors for tungsten and PVD (sputtering) cluster
  tools for the metals ({ref}`category-deposition`).
* **Lithography** — i-line and DUV exposure tools, the coat/develop
  tracks linked to them, and CD and overlay metrology
  ({ref}`category-lithography`).
* **Etch** — plasma etchers specialised by the material they remove
  (silicon and polysilicon, dielectrics, metals) and wet etching
  ({ref}`category-etch`).
* **Ion implantation** — medium-current, high-current and high-energy
  implanters, distinguished by the doses and energies they deliver
  ({ref}`category-implant`).
* **Resist strip and clean** — plasma ashers, batch wet benches and
  spray processors, and single-wafer spin processors
  ({ref}`category-strip`).
* **Planarisation** — CMP polishers and post-CMP cleaners
  ({ref}`category-cmp`).
* **Metrology, inspection and test** — film, sheet-resistance, CD,
  overlay and defect measurements in line, and the parametric tester
  and prober at the end of the flow ({ref}`category-test`); incoming
  wafer inspection belongs with the starting material
  ({ref}`category-substrate`).

## What SkyWater has published about its tools

The public basis for naming SkyWater's tools is narrow, and almost all
of it is one page.

* **The *Facilities & Capabilities* page.** Under the heading "SkyWater
  Process Integration Tools & Capabilities" SkyWater lists its tools by
  area — "Lithography", "Photo Metrology", "Film Deposition", "Etch",
  "Resist removal/cleans", "Diffusion, Anneal & Implant", "CMP" and
  "Wafer Sort/Test", among others — usually with a vendor, often with a
  model, and often with the gases, films, species, dose ranges or
  temperatures of the tool: "Axcelis GSD Hi dose B11, BF2, P, As
  2-180kev, 5e12 to 5e16, tilt/twist", for example, or "Furnaces are
  all made by Aviza".[^skw-01] Some entries give only a vendor and a
  chamber list ("AMAT PVD Metal") or an abbreviation ("PECVD TEOS, C2
  and Producer"), and no entry names a process step.[^skw-01] The page
  describes the Minnesota site as "Recently expanded in 2020 to enable
  additional capacity and Cu back end of line", with "90 nm + feature
  geometries", and its list includes tools that no step page assigns to
  SKY130, such as "ASML 193nm twin stage scanner – sub 65nm CD" and
  "AMAT Raider single wafer Cu plating".[^skw-01] A listed tool
  therefore shows what is on the floor now, not what built the first S8
  wafers at Cypress; the {ref}`public-sources inventory
  <references-public-sources>` makes the same caveat. The step pages
  quote the page as accessed on 2026-08-30; the tool names quoted on
  this page were checked against it again on 2026-09-13.
* **A maintenance-technician profile.** SkyWater's *A Day in the Life
  of a SkyWater Maintenance Technician* has photo captions naming "a
  Novellus high density plasma tool" and "a SEZ etcher tool", and
  mentions troubleshooting "complex equipment, like an
  implanter".[^skw-07]
* **A job posting.** A *Defect Technician 2* posting retrieved on
  2026-08-30 asks for "General operation of semiconductor defect
  metrology tools: SEM/AIT/KLA/SP1/EV300/1X", which the step pages read
  as KLA-Tencor AIT (patterned-wafer) and SP1 (unpatterned-wafer)
  inspection.[^job-01]
* **SEC filings.** The S-1 names suppliers of raw materials — among them
  "GlobalWafers Singapore Pte. Ltd. (silicon wafers)", "Honeywell
  Electronic Materials, Inc. (metal sputter targets)", "Tokyo Ohka Kogyo
  America, Inc. (photoresist)" and "Air Products & Chemicals, Inc.,
  Moses Lake (developer)" — and the step pages cite it for wafers,
  targets and resist.[^sec-01] Neither the S-1 nor the 2023 annual
  report names a process-tool vendor as a supplier; the only
  equipment-company name in the S-1 appears in a director's
  biography.[^sec-01][^sec-02] The annual report records one change to
  the tool set: "In 2020, we added deep-trench etching
  capability".[^sec-02]

## "Typically used" and "likely used at SkyWater"

Every step page separates two questions, and this page keeps them
apart.

* **Machines typically used** names the tool classes, with
  representative 130 nm-era models from any vendor, that a 200 mm fab
  of this vintage would use for the step. These are industry
  statements, sourced to textbooks, vendor documents, patents and
  papers; they say nothing about SkyWater. The *Steps* column of the
  main table below is built from these sections.
* **Machines likely used at SkyWater** names only tools for which there
  is public evidence at SkyWater, with the strength of that evidence.
  The inventory's scale is: **strong**, a SkyWater or tool-vendor
  statement; **medium**, a SkyWater job posting or an interview with a
  named SkyWater employee; **weak**, indirect evidence
  ({ref}`references-public-sources`, section 9). Because SkyWater's
  list never names a step, the step pages also grade a second question
  — whether the tool runs *this* step. The usual wording is "strong for
  the tool; **inference** for the assignment"; where a page weighs
  several candidate tools, it grades the assignment itself as medium
  or weak, and where it grades only the tool it writes "strong for
  existence". An assignment graded this way is this reference's
  reading, not a SkyWater statement. The second table below is built
  from these sections.

## Machine classes and the steps that use them

In the table:

* **Machine class** links to the category page that describes the
  class and its physics.
* **What it does in SKY130** summarises the step pages; the films and
  purposes are as the step pages describe them, including the readings
  they mark as inferences.
* **Tools SkyWater lists publicly** quotes the capabilities page exactly
  (sub-entries after a colon or in parentheses), or the profile or
  posting where
  marked; these are the entries the step pages quote. A listed tool is
  not evidence that a particular step runs on it; the second table
  gives the step pages' assignments.
* **Steps** gives, by code, the steps whose "Machines typically used"
  section names the class as the process tool or as one of two options,
  and after *alternative:* the steps where it is named only as an
  alternative or fallback. For supporting equipment (the resist track,
  cleans after etches and strips, metrology) it gives step numbers,
  with runs of three or more consecutive steps written as ranges.

A script check of the process-tool entries (all rows except the track,
the post-CMP cleaner and the metrology rows, and without the "also"
lists) finds all 171 steps in at
least one row, and 24 steps in two, where a page offers two tool
classes as equal options.

| Machine class | What it does in SKY130 | Tools SkyWater lists publicly | Steps |
|---------------|------------------------|-------------------------------|-------|
| {ref}`Starting material <category-substrate>`: incoming inspection, marking and sorting | Crystal growth, slicing and polishing are done at the wafer vendor; in the fab the SMAT page lists a surface scanner, a laser marker, a wafer sorter and a batch wet bench for the incoming wafers. | "Scribe: Lumonics Superclean"[^skw-01] | {ref}`SMAT <step-001>` |
| {ref}`Vertical batch furnace <category-oxidation>`: oxidation | Thermal oxides: the pad (base) oxide, the trench liner, the oxides of the ONO sequence, the thick and thin gate oxides and the oxidation after the gate etch. | "Furnaces are all made by Aviza": "wet oxidation to 1150C", "dry oxidation to 1150C"[^skw-01] | {ref}`BOX <step-002>`, {ref}`LINOX <step-010>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`, {ref}`IOX45 <step-063>` |
| {ref}`Vertical batch furnace <category-deposition>`: LPCVD | Isolation nitride, the ONO nitride, the amorphous-silicon gate film and the spacer nitride; one of two options for the gate nitride and the oxide cap; the batch alternative for the spacer oxide and the local-interconnect nitride cap. | "LPCVD nitride, with NH3 and also DH3", "LPCVD polysilicon (undoped), both amorphous and crystalline", "LPCVD silane oxide", "LPCVD oxide/nitride/oxide", "LPCVD BTBAS low temp nitride" (Aviza)[^skw-01] | {ref}`ISONIT <step-003>`, {ref}`ONO <step-040>`, {ref}`SAGD <step-048>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`SPNIT <step-076>`; *alternative:* {ref}`SPOX <step-080>`, {ref}`LINIT <step-104>` |
| {ref}`Vertical batch furnace <category-anneal>`: anneal and alloy | The hydrogen or forming-gas alloy anneals; the batch alternative for the pre-gate implant anneal and for densifying the fill oxide. | "Ar anneal to 1150C", "N2 anneal to 1150C", "H2 and forming gas alloy" (Aviza)[^skw-01] | {ref}`ALLY1 <step-096>`, {ref}`ALLY <step-170>`; *alternative:* {ref}`FILOX <step-011>`, {ref}`RTAI <step-034>` |
| {ref}`Rapid thermal processor <category-anneal>` (RTA, RTO) | Single-wafer lamp-heated anneals: the pre-gate implant anneal, tip and source/drain activation and contact silicidation; one of two routes for the thin gate oxide and the post-gate-etch oxidation; the single-wafer alternative for the liner, ONO and thick gate oxidations, densification and alloy. | "Ag Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C"[^skw-01] | {ref}`RTAI <step-034>`, {ref}`LVGOX <step-047>`, {ref}`IOX45 <step-063>`, {ref}`TIPRTAD <step-075>`, {ref}`RTAD <step-088>`, {ref}`RTAD2 <step-092>`, {ref}`CSIL <step-098>`; *alternative:* {ref}`LINOX <step-010>`, {ref}`FILOX <step-011>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`ALLY1 <step-096>`, {ref}`ALLY <step-170>` |
| {ref}`Plasma nitridation chamber <category-oxidation>` | Nitridation of the thin gate oxide, if it is plasma-nitrided. | None named; SkyWater lists "Nitrided gate oxide" as a special module without a tool[^skw-01] | *alternative:* {ref}`LVGOX <step-047>` |
| {ref}`PECVD <category-deposition>` (and SACVD) | Low-temperature oxides, nitrides and oxynitrides: gate nitride and oxide cap (one of two options), spacer oxide, the cap oxides, the local-interconnect nitride cap, the ILD overburden option, the MiM capacitor dielectrics, the fuse oxide and the passivation nitride; TEOS-based doped oxide as a PSG option. | "Lam/Novellus/AMAT": "PECVD TEOS, C2 and Producer" ("low temp options"), "PECVD silane oxide/nitride/oxynitride, C1" ("low temp, range of R.I. options"), "PECVD nitride C1"[^skw-01] | {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`SPOX <step-080>`, {ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`CAPILD <step-135>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`CAPILD2 <step-150>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`NFUSOX <step-164>`, {ref}`NTSD <step-167>`; *alternative:* {ref}`SPNIT <step-076>` |
| {ref}`HDP-CVD <category-deposition>` | Gap fill: the shallow-trench fill oxide, the phosphorus-doped pre-metal dielectric and the inter-level oxides between local interconnect and metal 4. | "Lam/Novellus High Density Plasma (HDP) doped and phos doped with sputter etch" ("high aspect (5:1) fill capability")[^skw-01]; a caption naming "a Novellus high density plasma tool"[^skw-07] | {ref}`FILOX <step-011>`, {ref}`PSG <step-089>`, {ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`, {ref}`NILD4 <step-126>`, {ref}`NILD5 <step-141>`, {ref}`NILD6 <step-156>` |
| {ref}`Tungsten CVD <category-deposition>` | Blanket tungsten fill of the local-interconnect contacts, the metal contacts and vias 1–3, polished back afterwards. | "Lam/Novellus PECVD Tungsten" ("plug fill", "PNL option for high aspect ratio (up to 10:1)")[^skw-01] | {ref}`WDEP <step-099>`, {ref}`WDEP2 <step-110>`, {ref}`WDEP3 <step-121>`, {ref}`WDEP4 <step-132>`, {ref}`WDEP5 <step-147>` |
| {ref}`PVD (sputtering) cluster tool <category-deposition>` | The Ti/TiN contact liner and IMP TiN via liners, the TiN local interconnect, the Ti/Al–Cu/TiW metal stacks and the TiW capacitor top plates. | "AMAT PVD Metal": "Sputter etch, degas", "Aluminum both pure and Cu doped", "TiW", "ESC TiN", "Imp TiN", "Collimated Ti", "WN", "Cobalt", "Niobium", "SiO2"[^skw-01] | {ref}`TI/TIN1 <step-097>`, {ref}`LITIN <step-101>`, {ref}`TIN2 <step-109>`, {ref}`TIAL6 <step-112>`, {ref}`TIN3 <step-120>`, {ref}`TIAL12 <step-123>`, {ref}`TIN4 <step-131>`, {ref}`WTIAL3 <step-134>`, {ref}`CAPTIW1 <step-136>`, {ref}`TIN5 <step-146>`, {ref}`WTIAL4 <step-149>`, {ref}`CAPTIW2 <step-151>`, {ref}`WTIAL5 <step-161>` |
| {ref}`i-line stepper or scanner <category-lithography>` | Exposure of the non-critical levels: implant blocks, the memory, oxide and resistor masks, the capacitor masks, via 4, metal 5, the nitride seal and the pad mask; either class for metals 3 and 4. | "ASML I-line stepper", "ASML I-line scanner"[^skw-01] | {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>`; *alternative:* {ref}`FOM <step-004>`, {ref}`NPCM <step-078>` |
| {ref}`DUV (KrF, 248 nm) stepper or scanner <category-lithography>` | Exposure of the critical levels: active, poly gate, nitride poly cut, local-interconnect contact and local interconnect, metal contact, metals 1–2 and vias 1–3; either class for metals 3 and 4. | "ASML DUV stepper", "ASML DUV scanner"; also "ASML 193nm single stage scanner – 90nm CD" and "ASML 193nm twin stage scanner – sub 65nm CD"[^skw-01] | {ref}`FOM <step-004>`, {ref}`P1M <step-061>`, {ref}`NPCM <step-078>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`MM4 <step-154>`; *alternative:* {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>` |
| {ref}`Coat/develop track <category-lithography>` | Resist coat, bake and develop, linked to the exposure tool. | "DNS 80B track", "Sokudo RF3 track", "TEL ProZ Lithius track"[^skw-01] | all 36 mask steps, {ref}`FOM <step-004>` to {ref}`PDM <step-168>` ({ref}`masks-index`) |
| {ref}`CD-SEM and overlay metrology <category-lithography>` | Linewidth after develop and after etch; layer-to-layer registration. | "AMAT Verity (multiple versions) CD", "AMAT VeraSEM", "KLA 5200/5300/Archer overlay"[^skw-01] | *overlay:* all 36 mask steps; *CD-SEM:* {ref}`004 <step-004>`–{ref}`006 <step-006>`, {ref}`014 <step-014>`, {ref}`022 <step-022>`, {ref}`035 <step-035>`, {ref}`036 <step-036>`, {ref}`041 <step-041>`, {ref}`044 <step-044>`, {ref}`049 <step-049>`, {ref}`061 <step-061>`, {ref}`062 <step-062>`, {ref}`064 <step-064>`, {ref}`068 <step-068>`, {ref}`071 <step-071>`, {ref}`078 <step-078>`, {ref}`081 <step-081>`, {ref}`085 <step-085>`, {ref}`093 <step-093>`, {ref}`094 <step-094>`, {ref}`102 <step-102>`, {ref}`103 <step-103>`, {ref}`107 <step-107>`, {ref}`108 <step-108>`, {ref}`113 <step-113>`, {ref}`114 <step-114>`, {ref}`118 <step-118>`, {ref}`119 <step-119>`, {ref}`124 <step-124>`, {ref}`125 <step-125>`, {ref}`129 <step-129>`, {ref}`130 <step-130>`, {ref}`137 <step-137>`–{ref}`140 <step-140>`, {ref}`144 <step-144>`, {ref}`145 <step-145>`, {ref}`152 <step-152>`–{ref}`155 <step-155>`, {ref}`159 <step-159>`, {ref}`160 <step-160>`, {ref}`162 <step-162>`, {ref}`163 <step-163>` |
| {ref}`Plasma etcher <category-etch>`: silicon and polysilicon | High-density etching of the shallow trenches, the tunnel-mask ARC, the ONO stack (one of two options) and the poly gate. | Under "Poly/Silicon Etch": "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2" ("gate, trench, W/WN"), "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6, O2", "Lam 4400, HBr, Cl2, C2F6, CF4, SF6, O2"[^skw-01] | {ref}`STIE <step-006>`, {ref}`TUNARCE <step-036>`, {ref}`ONOME <step-042>`, {ref}`P1ME <step-062>` |
| {ref}`Plasma etcher <category-etch>`: dielectric and nitride | Etching of the isolation nitride, the spacer nitride, the nitride poly cut, the contact and via holes, the ONO stack (one of two options), the nitride seal and the pad opening; an option for an inorganic tunnel-mask ARC. | None: the contact, via, seal and pad etch pages state that no dielectric etcher is named[^skw-01] and weigh the three poly/silicon etchers above instead (second table) | {ref}`STINITE <step-005>`, {ref}`ONOME <step-042>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`LICM1E <step-094>`, {ref}`CTME <step-108>`, {ref}`VIME <step-119>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`, {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>`; *alternative:* {ref}`TUNARCE <step-036>` |
| {ref}`Plasma etcher <category-etch>`: metal | Etching of the TiN local interconnect, the metal 1–5 stacks and the TiW capacitor top plates. | Under "Metal Etch": "Lam 9600, Al, TiW, TiN, Pt", "Lam 2300 Versys, Al, TiW, TiN, Nb, Pt"[^skw-01] | {ref}`LI1ME <step-103>`, {ref}`MM1E <step-114>`, {ref}`MM2E <step-125>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`MM5E <step-163>` |
| {ref}`Resist asher <category-strip>` | Removal of implanted resist after the implant masks, and of resist after etches. | "Gasonic PEP, remote microwave plasma, N2, O2, 120C – 270C", "Iridia RF microwave, N2, O2, H2, CF4, NH3, H2/N2, 40C-270C", "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to 250C"[^skw-01] | {ref}`DNIS <step-009>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`; *alternative:* {ref}`TUNARCE <step-036>`; *also for the strip after an etch:* {ref}`006 <step-006>`, {ref}`039 <step-039>`, {ref}`042 <step-042>`, {ref}`046 <step-046>`, {ref}`062 <step-062>`, {ref}`079 <step-079>`, {ref}`095 <step-095>`, {ref}`103 <step-103>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`130 <step-130>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`145 <step-145>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`160 <step-160>`, {ref}`163 <step-163>`, {ref}`166 <step-166>`, {ref}`169 <step-169>` |
| {ref}`Wet bench and spray processor <category-strip>` | Hot-phosphoric nitride strip; HF or BOE etches of the tunnel windows and the thick gate oxide and the sacrificial etch; SPM, SC-1 and SC-2 cleans; solvent strips. | "Akrion Gamma Batch Wet Bench" ("Sulfuric, SC1, phosphoric, BOE, spin or IPA dry"), "DNS wet bench industry standard HF/SC1/SC2" ("dilute HF-last with IPA dry"), "FSI Mercury industry standard HF/SC1/SC2 rotational", "Batch Rotational" ("EKS265, EKC270 solvents, CO2 injected DI")[^skw-01] | {ref}`NS19 <step-013>`, {ref}`TUNME <step-039>`, {ref}`GOXETCH <step-046>`, {ref}`SACETCH <step-095>`; *also for a clean or strip:* {ref}`001 <step-001>`, {ref}`002 <step-002>`, {ref}`006 <step-006>`, {ref}`009 <step-009>`, {ref}`010 <step-010>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`025 <step-025>`, {ref}`029 <step-029>`, {ref}`033 <step-033>`, {ref}`042 <step-042>`, {ref}`051 <step-051>`, {ref}`054 <step-054>`, {ref}`057 <step-057>`, {ref}`062 <step-062>`, {ref}`067 <step-067>`, {ref}`070 <step-070>`, {ref}`074 <step-074>`, {ref}`079 <step-079>`, {ref}`084 <step-084>`, {ref}`087 <step-087>`, {ref}`103 <step-103>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`130 <step-130>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`145 <step-145>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`160 <step-160>`, {ref}`163 <step-163>`, {ref}`166 <step-166>`, {ref}`169 <step-169>` |
| {ref}`Single-wafer spin processor <category-etch>` | Backside film removal; an option for the HF etches and for cleans; the post-CMP clean candidate on the CMP pages. | "Single Wafer": "SEZ223, Davinci, HF, DSP+HF, titration controlled"[^skw-01]; a caption naming "a SEZ etcher tool"[^skw-07] | {ref}`TUNME <step-039>`, {ref}`GOXETCH <step-046>`, {ref}`BFR <step-060>`, {ref}`SACETCH <step-095>`; *also for a clean:* {ref}`012 <step-012>`, {ref}`108 <step-108>`, {ref}`111 <step-111>`, {ref}`116 <step-116>`, {ref}`119 <step-119>`, {ref}`122 <step-122>`, {ref}`127 <step-127>`, {ref}`130 <step-130>`, {ref}`133 <step-133>`, {ref}`142 <step-142>`, {ref}`145 <step-145>`, {ref}`148 <step-148>`, {ref}`157 <step-157>` |
| {ref}`Medium-current ion implanter <category-implant>` | Low- and medium-dose implants, with tilt: channel and threshold implants, punch-through and depletion implants, drift-well implants, resistor implants, tips and halos. | "Axcelis 8250 Mid current B11, BF2, As, ESC chuck, E shower, 1e11 to 1e14, 0-60 deg tilt"[^skw-01] | {ref}`LVTNI <step-015>`, {ref}`NWI2 <step-019>`, {ref}`LVTPI <step-020>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`PWI2 <step-028>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`NCHI <step-045>`, {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`, {ref}`ASTI <step-065>`, {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`, {ref}`2PSDI <step-083>`; *alternative:* {ref}`NWI <step-018>` |
| {ref}`High-current ion implanter <category-implant>` | High-dose implants: poly gate doping, the arsenic tip and the source/drain implants; one option for the resistor and lightly doped tip implants. | "Axcelis GSD Hi dose B11, BF2, P, As 2-180kev, 5e12 to 5e16, tilt/twist"[^skw-01] | {ref}`P1I <step-050>`, {ref}`PRI <step-053>`, {ref}`ASTI <step-065>`, {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`; *alternative:* {ref}`LDASTI <step-072>` |
| {ref}`High-energy ion implanter <category-implant>` | Deep implants: the deep N-well, N-well and P-well implants and (one of two options) the drift-well implants. | "Axcelis GSD High current/energy B11, BF2, P, As, 10-3000kev, 1e11 to 5e15, tilt/twist"[^skw-01] | {ref}`DNI <step-008>`, {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`; *alternative:* {ref}`LVTPI <step-020>` |
| {ref}`CMP polisher <category-cmp>` | Planarisation of the trench fill to the nitride, the PSG over the poly and the inter-level oxides over local interconnect and metals 1–4; removal of the tungsten overburden at the contact and via levels. | "AMAT Mirra CMP": "oxide", "nitride", "niobium", "aluminum", "tungsten", "high selectivity tungsten", "copper"; "On board metrology with feed forward and backward"[^skw-01] | {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>` |
| {ref}`Post-CMP cleaner <category-cmp>` | Brush-scrub and chemical clean of slurry residue after each polish. | No brush scrubber named; the CMP pages point to "SEZ223, Davinci", and the Mirra entry lists "Track ammonia clean" and "IPA clean"[^skw-01] | {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>` |
| {ref}`Defect and particle inspection <category-test>` | Unpatterned-wafer particle scans and patterned-wafer defect inspection. | None on the capabilities page; a job posting reads "SEM/AIT/KLA/SP1/EV300/1X"[^job-01] | {ref}`001 <step-001>`, {ref}`005 <step-005>`, {ref}`009 <step-009>`, {ref}`013 <step-013>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`025 <step-025>`, {ref}`029 <step-029>`, {ref}`033 <step-033>`, {ref}`035 <step-035>`, {ref}`042 <step-042>`, {ref}`046 <step-046>`, {ref}`051 <step-051>`, {ref}`054 <step-054>`, {ref}`057 <step-057>`, {ref}`060 <step-060>`, {ref}`061 <step-061>`, {ref}`067 <step-067>`, {ref}`070 <step-070>`, {ref}`074 <step-074>`, {ref}`082 <step-082>`, {ref}`084 <step-084>`, {ref}`086 <step-086>`, {ref}`087 <step-087>`, {ref}`090 <step-090>`, {ref}`091 <step-091>`, {ref}`095 <step-095>`, {ref}`100 <step-100>`, {ref}`106 <step-106>`, {ref}`107 <step-107>`, {ref}`110 <step-110>`, {ref}`111 <step-111>`, {ref}`113 <step-113>`, {ref}`116 <step-116>`–{ref}`118 <step-118>`, {ref}`121 <step-121>`, {ref}`122 <step-122>`, {ref}`124 <step-124>`, {ref}`127 <step-127>`–{ref}`129 <step-129>`, {ref}`132 <step-132>`, {ref}`133 <step-133>`, {ref}`137 <step-137>`, {ref}`139 <step-139>`, {ref}`142 <step-142>`–{ref}`144 <step-144>`, {ref}`147 <step-147>`, {ref}`148 <step-148>`, {ref}`152 <step-152>`, {ref}`154 <step-154>`, {ref}`157 <step-157>`, {ref}`159 <step-159>`, {ref}`162 <step-162>`, {ref}`164 <step-164>`, {ref}`165 <step-165>`, {ref}`167 <step-167>`–{ref}`169 <step-169>` |
| {ref}`Film thickness and stress metrology <category-deposition>` | Ellipsometers, reflectometers, FTIR and XRF gauges, and wafer-bow stress gauges on product or monitor wafers. | None named apart from the Mirra's "On board metrology"[^skw-01] | {ref}`002 <step-002>`, {ref}`003 <step-003>`, {ref}`010 <step-010>`–{ref}`013 <step-013>`, {ref}`039 <step-039>`, {ref}`040 <step-040>`, {ref}`043 <step-043>`, {ref}`046 <step-046>`–{ref}`048 <step-048>`, {ref}`058 <step-058>`, {ref}`059 <step-059>`, {ref}`063 <step-063>`, {ref}`076 <step-076>`, {ref}`077 <step-077>`, {ref}`080 <step-080>`, {ref}`089 <step-089>`–{ref}`092 <step-092>`, {ref}`095 <step-095>`, {ref}`097 <step-097>`, {ref}`099 <step-099>`–{ref}`101 <step-101>`, {ref}`104 <step-104>`–{ref}`106 <step-106>`, {ref}`109 <step-109>`–{ref}`112 <step-112>`, {ref}`115 <step-115>`–{ref}`117 <step-117>`, {ref}`120 <step-120>`–{ref}`123 <step-123>`, {ref}`126 <step-126>`–{ref}`128 <step-128>`, {ref}`131 <step-131>`–{ref}`136 <step-136>`, {ref}`138 <step-138>`, {ref}`141 <step-141>`–{ref}`143 <step-143>`, {ref}`146 <step-146>`–{ref}`151 <step-151>`, {ref}`153 <step-153>`, {ref}`156 <step-156>`–{ref}`158 <step-158>`, {ref}`161 <step-161>`, {ref}`164 <step-164>`, {ref}`167 <step-167>` |
| {ref}`Sheet-resistance and dose metrology <category-implant>` | Four-point probe and thermal-wave (modulated reflectance) monitors. | None named | {ref}`008 <step-008>`, {ref}`015 <step-015>`, {ref}`018 <step-018>`–{ref}`020 <step-020>`, {ref}`023 <step-023>`, {ref}`024 <step-024>`, {ref}`027 <step-027>`, {ref}`028 <step-028>`, {ref}`031 <step-031>`, {ref}`032 <step-032>`, {ref}`034 <step-034>`, {ref}`037 <step-037>`, {ref}`038 <step-038>`, {ref}`045 <step-045>`, {ref}`050 <step-050>`, {ref}`053 <step-053>`, {ref}`056 <step-056>`, {ref}`065 <step-065>`, {ref}`066 <step-066>`, {ref}`069 <step-069>`, {ref}`072 <step-072>`, {ref}`073 <step-073>`, {ref}`075 <step-075>`, {ref}`082 <step-082>`, {ref}`083 <step-083>`, {ref}`086 <step-086>`, {ref}`088 <step-088>`, {ref}`092 <step-092>`, {ref}`097 <step-097>`–{ref}`099 <step-099>`, {ref}`101 <step-101>`, {ref}`109 <step-109>`, {ref}`110 <step-110>`, {ref}`112 <step-112>`, {ref}`120 <step-120>`, {ref}`121 <step-121>`, {ref}`123 <step-123>`, {ref}`131 <step-131>`, {ref}`132 <step-132>`, {ref}`134 <step-134>`, {ref}`136 <step-136>`, {ref}`146 <step-146>`, {ref}`147 <step-147>`, {ref}`149 <step-149>`, {ref}`151 <step-151>`, {ref}`161 <step-161>` |
| {ref}`Cross-section SEM and profilers <category-etch>` | Trench, spacer, gap-fill and etch profiles; step height and dishing after CMP. | None assigned by a step page; the physical-analysis list includes "FEI Dual Beam FIB/SEM" and "Hitachi S-4800"[^skw-01] | *cross-section SEM:* {ref}`006 <step-006>`, {ref}`010 <step-010>`, {ref}`011 <step-011>`, {ref}`062 <step-062>`, {ref}`077 <step-077>`, {ref}`079 <step-079>`, {ref}`089 <step-089>`, {ref}`094 <step-094>`, {ref}`103 <step-103>`, {ref}`105 <step-105>`, {ref}`108 <step-108>`–{ref}`110 <step-110>`, {ref}`114 <step-114>`, {ref}`115 <step-115>`, {ref}`119 <step-119>`–{ref}`121 <step-121>`, {ref}`125 <step-125>`, {ref}`126 <step-126>`, {ref}`130 <step-130>`–{ref}`132 <step-132>`, {ref}`140 <step-140>`, {ref}`141 <step-141>`, {ref}`145 <step-145>`–{ref}`147 <step-147>`, {ref}`155 <step-155>`, {ref}`156 <step-156>`, {ref}`160 <step-160>`, {ref}`161 <step-161>`, {ref}`163 <step-163>`, {ref}`166 <step-166>`; *profiler or AFM:* {ref}`012 <step-012>`, {ref}`090 <step-090>`, {ref}`100 <step-100>`, {ref}`106 <step-106>`, {ref}`111 <step-111>`, {ref}`122 <step-122>`, {ref}`133 <step-133>`, {ref}`148 <step-148>` |
| {ref}`Parametric tester and prober <category-test>` | Electrical test of the scribe-line structures at the end of the flow; C–V, leakage and chain structures as electrical monitors. | "HP 4062UX" ("DC, capacitance, pulse generator, frequency counter"), "Engineering manual Probe Station"; no production prober[^skw-01] | {ref}`HPETEST <step-171>`; *electrical monitor named:* {ref}`040 <step-040>`, {ref}`043 <step-043>`, {ref}`047 <step-047>`, {ref}`063 <step-063>`, {ref}`096 <step-096>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`130 <step-130>`, {ref}`135 <step-135>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`145 <step-145>`, {ref}`150 <step-150>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`160 <step-160>`, {ref}`163 <step-163>`, {ref}`170 <step-170>` |

Notes on the table:

* **Two lithography rows for one vendor.** SkyWater's list says "DUV",
  not a wavelength; the step pages read "ASML DUV stepper" and "ASML DUV
  scanner" as 248 nm (KrF) tools and set the two 193 nm scanners aside
  as later additions, which the {ref}`P1M <step-061>` page says "are not
  evidence for how the 130 nm gate was, or is, printed".
* **The dielectric etch row has no SkyWater tool.** SkyWater lists its
  plasma etchers under "Metal Etch" and "Poly/Silicon Etch" only.[^skw-01]
  The local-interconnect contact, contact, via and nitride-seal etch
  pages say that no dielectric etcher is named and, like the pad etch
  page, grade one or more of the three poly/silicon etchers as
  candidates; the second table gives the grades.
* **Classes with no named SkyWater tool.** The "typically used" sections
  name a post-CMP brush scrubber, a production wafer prober, a plasma
  nitridation chamber, film-thickness, stress and sheet-resistance
  gauges and cross-section SEMs; apart from the Mirra's "On board
  metrology", the capabilities page names none of these.[^skw-01] The CMP pages record the missing brush
  scrubber as an open question, and the {ref}`HPETEST <step-171>` page
  notes that no production prober is named.
* **Listed entries no step page assigns.** The capabilities page also
  lists "Atomic Layer Deposition", "AMAT Raider single wafer Cu
  plating", "Atmospheric selective oxidation", "Polyimide cure", "IPA
  clean" (under CMP), "Reticle storage/handler/defect inspection", the
  special modules other than the three in the second table, and a
  "Physical Analysis" group.[^skw-01] None of the 171 step pages assigns
  these to a SKY130 step; the {ref}`NTSD <step-167>` page mentions
  "Polyimide cure" only in asking whether a polyimide is applied.

<!-- footnotes -->

[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023, filed
    2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; tool names re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^skw-07]: SkyWater Technology, *A Day in the Life of a SkyWater Maintenance
    Technician*, 2023-12-14.
    <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
[^job-01]: Indeed, *Skywater Technology Foundry Jobs, Employment in
    Bloomington, MN* (listing page; Defect Technician 2 posting), retrieved
    2026-08-30; listings expire.
    <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
