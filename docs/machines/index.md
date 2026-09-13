(machines-index)=
# Machines

This page indexes the manufacturing equipment named on the step pages of
this reference. It groups the equipment into machine classes, says what
each class does in the SKY130 flow, quotes what SkyWater has published
about its own tools of that class, and lists the steps that use it. It
is compiled from the two machine sections that every step page carries,
"Machines typically used" and "Machines likely used at SkyWater", read
on all 171 pages; it adds no evidence of its own about SkyWater's
tools. Where the step pages
differ from each other or from the sources they quote, the differences
are listed under
{ref}`Open questions and inconsistencies <machines-inconsistencies>`
rather than resolved here.

## Equipment classes in a 200 mm, 130 nm fab

A fab of this kind does not have one tool per step. SkyWater's S-1
registration statement says that the Bloomington fab "can produce up to
156,000 wafers per year (depending on the product mix) and has at least
522 well-maintained fab and sort tools",[^sec-01] and its annual report
for 2023 that "CMOS process flows for a number of different node
dimensions are offered ranging from 90 nm—350 nm" in the same 200 mm
fab.[^sec-02] The 171 steps of SKY130[^steps-sheet] therefore share tools with one
another and with other flows, and the step pages describe equipment by
class. The classes follow the unit processes of the category pages:

* **Thermal processing** — batch vertical furnaces, used for oxidation,
  {term}`LPCVD`, anneals and the hydrogen alloy, and single-wafer rapid
  thermal ({term}`RTP`) processors ({ref}`category-oxidation`, {ref}`category-anneal`).
* **Thin-film deposition** — single-wafer {term}`PECVD` and {term}`HDP-CVD`
  systems for dielectrics, CVD reactors for tungsten and {term}`PVD`
  (sputtering) cluster
  tools for the metals ({ref}`category-deposition`).
* **Lithography** — i-line and {term}`DUV` exposure tools
  ({term}`steppers <stepper>` and scanners), the coat/develop
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
* **Planarisation** — {term}`CMP` polishers and post-CMP cleaners
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
  Novellus high density plasma tool" and "a SEZ etcher tool" (the
  second in a longer caption: "In the photo above, he replaces a motor
  for a robot on a SEZ etcher tool"), and a third about troubleshooting
  "complex equipment, like an implanter".[^skw-07]
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
  report names a process-tool vendor as a supplier;[^sec-01][^sec-02]
  the semiconductor-equipment company names in the S-1 (Axcelis
  Technologies, "a semiconductor capital equipment company"; Rudolph
  Technologies, Nanometrics and Onto Innovation) appear only in executive
  and director biographies.[^sec-01] The annual report records one change to
  the tool set: "In 2020, we added deep-trench etching
  capability".[^sec-02]

## "Machines typically used" and "Machines likely used at SkyWater"

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
  the tool; inference for the assignment" or a close variant; where a
  page weighs several candidate tools, it grades the assignment itself
  as medium or weak, and where it grades only the tool it writes
  "strong for existence". An assignment graded this way is this reference's
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
  posting where marked; these are the entries the step pages quote. A listed tool is
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
lists) finds all 171 steps in at least one row, and, outside the
*alternative:* lists, 25 steps in two, where a page offers two tool
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
| {ref}`Tungsten CVD <category-deposition>` | Blanket tungsten fill of the local-interconnect contacts, the metal contacts and vias 1–3, polished back afterwards. | "Lam/Novellus PECVD Tungsten" ("plug fill", "{term}`PNL` option for high aspect ratio (up to 10:1)")[^skw-01] | {ref}`WDEP <step-099>`, {ref}`WDEP2 <step-110>`, {ref}`WDEP3 <step-121>`, {ref}`WDEP4 <step-132>`, {ref}`WDEP5 <step-147>` |
| {ref}`PVD (sputtering) cluster tool <category-deposition>` | The Ti/TiN contact liner and {term}`IMP` TiN via liners, the TiN local interconnect, the Ti/Al–Cu/TiW metal stacks and the TiW capacitor top plates. | "AMAT PVD Metal": "Sputter etch, degas", "Aluminum both pure and Cu doped", "TiW", "{term}`ESC` TiN", "Imp TiN", "Collimated Ti", "WN", "Cobalt", "Niobium", "SiO2"[^skw-01] | {ref}`TI/TIN1 <step-097>`, {ref}`LITIN <step-101>`, {ref}`TIN2 <step-109>`, {ref}`TIAL6 <step-112>`, {ref}`TIN3 <step-120>`, {ref}`TIAL12 <step-123>`, {ref}`TIN4 <step-131>`, {ref}`WTIAL3 <step-134>`, {ref}`CAPTIW1 <step-136>`, {ref}`TIN5 <step-146>`, {ref}`WTIAL4 <step-149>`, {ref}`CAPTIW2 <step-151>`, {ref}`WTIAL5 <step-161>` |
| {ref}`i-line stepper or scanner <category-lithography>` | Exposure of the non-critical levels: implant blocks, the memory, oxide and resistor masks, the capacitor masks, via 4, metal 5, the nitride seal and the pad mask; either class for metals 3 and 4. | "ASML I-line stepper", "ASML I-line scanner"[^skw-01] | {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>`; *alternative:* {ref}`FOM <step-004>`, {ref}`NPCM <step-078>` |
| {ref}`DUV (KrF, 248 nm) stepper or scanner <category-lithography>` | Exposure of the critical levels: active, poly gate, nitride poly cut, local-interconnect contact and local interconnect, metal contact, metals 1–2 and vias 1–3; either class for metals 3 and 4. | "ASML DUV stepper", "ASML DUV scanner"; also "ASML 193nm single stage scanner – 90nm CD" and "ASML 193nm twin stage scanner – sub 65nm CD"[^skw-01] | {ref}`FOM <step-004>`, {ref}`P1M <step-061>`, {ref}`NPCM <step-078>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`MM4 <step-154>`; *alternative:* {ref}`DNM <step-007>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>` |
| {ref}`Coat/develop track <category-lithography>` | Resist coat, bake and develop, linked to the exposure tool. | "DNS 80B track", "Sokudo RF3 track", "TEL ProZ Lithius track"[^skw-01] | all 36 mask steps, {ref}`FOM <step-004>` to {ref}`PDM <step-168>` ({ref}`masks-index`) |
| {ref}`CD-SEM and overlay metrology <category-lithography>` | Linewidth after develop and after etch ({term}`CD-SEM`); layer-to-layer registration. | "AMAT Verity (multiple versions) CD", "AMAT VeraSEM", "KLA 5200/5300/Archer overlay"[^skw-01] | *overlay:* all 36 mask steps; *CD-SEM:* {ref}`004 <step-004>`–{ref}`007 <step-007>`, {ref}`014 <step-014>`, {ref}`017 <step-017>`, {ref}`022 <step-022>`, {ref}`026 <step-026>`, {ref}`030 <step-030>`, {ref}`035 <step-035>`, {ref}`036 <step-036>`, {ref}`041 <step-041>`, {ref}`044 <step-044>`, {ref}`049 <step-049>`, {ref}`052 <step-052>`, {ref}`055 <step-055>`, {ref}`061 <step-061>`, {ref}`062 <step-062>`, {ref}`064 <step-064>`, {ref}`068 <step-068>`, {ref}`071 <step-071>`, {ref}`078 <step-078>`, {ref}`081 <step-081>`, {ref}`085 <step-085>`, {ref}`093 <step-093>`, {ref}`094 <step-094>`, {ref}`102 <step-102>`, {ref}`103 <step-103>`, {ref}`107 <step-107>`, {ref}`108 <step-108>`, {ref}`113 <step-113>`, {ref}`114 <step-114>`, {ref}`118 <step-118>`, {ref}`119 <step-119>`, {ref}`124 <step-124>`, {ref}`125 <step-125>`, {ref}`129 <step-129>`, {ref}`130 <step-130>`, {ref}`137 <step-137>`–{ref}`140 <step-140>`, {ref}`144 <step-144>`, {ref}`145 <step-145>`, {ref}`152 <step-152>`–{ref}`155 <step-155>`, {ref}`159 <step-159>`, {ref}`160 <step-160>`, {ref}`162 <step-162>`, {ref}`163 <step-163>`, {ref}`165 <step-165>`, {ref}`168 <step-168>` |
| {ref}`Plasma etcher <category-etch>`: silicon and polysilicon | High-density etching of the shallow trenches, the tunnel-mask ARC, the ONO stack (one of two options) and the poly gate. | Under "Poly/Silicon Etch": "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2" ("gate, trench, W/WN"), "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6, O2", "Lam 4400, HBr, Cl2, C2F6, CF4, SF6, O2"[^skw-01] | {ref}`STIE <step-006>`, {ref}`TUNARCE <step-036>`, {ref}`ONOME <step-042>`, {ref}`P1ME <step-062>` |
| {ref}`Plasma etcher <category-etch>`: dielectric and nitride | Etching of the isolation nitride, the spacer nitride, the nitride poly cut, the contact and via holes, the ONO stack (one of two options), the nitride seal and the pad opening; an option for an inorganic tunnel-mask ARC. | None: the local-interconnect contact, contact, via and nitride-seal etch pages state that no dielectric etcher is named[^skw-01] and, like the pad etch page, weigh the three poly/silicon etchers above instead (second table) | {ref}`STINITE <step-005>`, {ref}`ONOME <step-042>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`LICM1E <step-094>`, {ref}`CTME <step-108>`, {ref}`VIME <step-119>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`, {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>`; *alternative:* {ref}`TUNARCE <step-036>` |
| {ref}`Plasma etcher <category-etch>`: metal | Etching of the TiN local interconnect, the metal 1–5 stacks and the TiW capacitor top plates. | Under "Metal Etch": "Lam 9600, Al, TiW, TiN, Pt", "Lam 2300 Versys, Al, TiW, TiN, Nb, Pt"[^skw-01] | {ref}`LI1ME <step-103>`, {ref}`MM1E <step-114>`, {ref}`MM2E <step-125>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`MM5E <step-163>` |
| {ref}`Downstream plasma asher <category-strip>` | Removal of implanted resist after the implant masks, and of resist after etches. | "Gasonic PEP, remote microwave plasma, N2, O2, 120C – 270C", "Iridia RF microwave, N2, O2, H2, CF4, NH3, H2/N2, 40C-270C", "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to 250C"[^skw-01] | {ref}`DNIS <step-009>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`; *alternative:* {ref}`TUNARCE <step-036>`; *also for the strip after an etch:* {ref}`006 <step-006>`, {ref}`039 <step-039>`, {ref}`042 <step-042>`, {ref}`046 <step-046>`, {ref}`062 <step-062>`, {ref}`079 <step-079>`, {ref}`095 <step-095>`, {ref}`103 <step-103>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`130 <step-130>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`145 <step-145>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`160 <step-160>`, {ref}`163 <step-163>`, {ref}`166 <step-166>`, {ref}`169 <step-169>` |
| {ref}`Wet bench and spray processor <category-strip>` | Hot-phosphoric nitride strip; HF or BOE etches of the tunnel windows and the thick gate oxide and the sacrificial etch; SPM, SC-1 and SC-2 cleans; solvent strips. | "Akrion Gamma Batch Wet Bench" ("Sulfuric, SC1, phosphoric, BOE, spin or IPA dry"), "DNS wet bench industry standard HF/SC1/SC2" ("dilute HF-last with IPA dry"), "FSI Mercury industry standard HF/SC1/SC2 rotational", "Batch Rotational" ("EKS265, EKC270 solvents, CO2 injected DI")[^skw-01] | {ref}`NS19 <step-013>`, {ref}`TUNME <step-039>`, {ref}`GOXETCH <step-046>`, {ref}`SACETCH <step-095>`; *also for a clean or strip:* {ref}`001 <step-001>`, {ref}`002 <step-002>`, {ref}`006 <step-006>`, {ref}`009 <step-009>`, {ref}`010 <step-010>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`025 <step-025>`, {ref}`029 <step-029>`, {ref}`033 <step-033>`, {ref}`042 <step-042>`, {ref}`051 <step-051>`, {ref}`054 <step-054>`, {ref}`057 <step-057>`, {ref}`062 <step-062>`, {ref}`067 <step-067>`, {ref}`070 <step-070>`, {ref}`074 <step-074>`, {ref}`079 <step-079>`, {ref}`084 <step-084>`, {ref}`087 <step-087>`, {ref}`103 <step-103>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`130 <step-130>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`145 <step-145>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`160 <step-160>`, {ref}`163 <step-163>`, {ref}`166 <step-166>`, {ref}`169 <step-169>` |
| {ref}`Single-wafer spin processor <category-etch>` | Backside film removal; an option for the HF etches and for cleans; the post-CMP clean candidate on the CMP pages. | "Single Wafer": "SEZ223, Davinci, HF, DSP+HF, titration controlled"[^skw-01]; a caption naming "a SEZ etcher tool"[^skw-07] | {ref}`TUNME <step-039>`, {ref}`GOXETCH <step-046>`, {ref}`BFR <step-060>`, {ref}`SACETCH <step-095>`; *also for a clean:* {ref}`012 <step-012>`, {ref}`033 <step-033>`, {ref}`108 <step-108>`, {ref}`111 <step-111>`, {ref}`116 <step-116>`, {ref}`119 <step-119>`, {ref}`122 <step-122>`, {ref}`127 <step-127>`, {ref}`130 <step-130>`, {ref}`133 <step-133>`, {ref}`142 <step-142>`, {ref}`145 <step-145>`, {ref}`148 <step-148>`, {ref}`157 <step-157>` |
| {ref}`Medium-current ion implanter <category-implant>` | Low- and medium-dose implants, with tilt: channel and threshold implants, punch-through and depletion implants, drift-well implants, resistor implants, tips and halos. | "Axcelis 8250 Mid current B11, BF2, As, ESC chuck, E shower, 1e11 to 1e14, 0-60 deg tilt"[^skw-01] | {ref}`LVTNI <step-015>`, {ref}`NWI2 <step-019>`, {ref}`LVTPI <step-020>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`NCHI <step-045>`, {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`, {ref}`ASTI <step-065>`, {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`, {ref}`2PSDI <step-083>`; *alternative:* {ref}`NWI <step-018>` |
| {ref}`High-current ion implanter <category-implant>` | High-dose implants: poly gate doping, the arsenic tip and the source/drain implants; one option for the resistor and lightly doped tip implants. | "Axcelis GSD Hi dose B11, BF2, P, As 2-180kev, 5e12 to 5e16, tilt/twist"[^skw-01] | {ref}`P1I <step-050>`, {ref}`PRI <step-053>`, {ref}`ASTI <step-065>`, {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`; *alternative:* {ref}`LDASTI <step-072>` |
| {ref}`High-energy ion implanter <category-implant>` | Deep implants: the deep N-well, N-well and P-well implants and (one of two options) the drift-well implants. | "Axcelis GSD High current/energy B11, BF2, P, As, 10-3000kev, 1e11 to 5e15, tilt/twist"[^skw-01] | {ref}`DNI <step-008>`, {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`; *alternative:* {ref}`LVTPI <step-020>` |
| {ref}`CMP polisher <category-cmp>` | Planarisation of the trench fill to the nitride, the PSG over the poly and the inter-level oxides over local interconnect and metals 1–4; removal of the tungsten overburden at the contact and via levels. | "AMAT Mirra CMP": "oxide", "nitride", "niobium", "aluminum", "tungsten", "high selectivity tungsten", "copper"; "On board metrology with feed forward and backward"[^skw-01] | {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>` |
| {ref}`Post-CMP cleaner <category-cmp>` | Brush-scrub and chemical clean of slurry residue after each polish. | No brush scrubber named; the CMP pages point to "SEZ223, Davinci", and the Mirra entry lists "Track ammonia clean" and "IPA clean"[^skw-01] | {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>` |
| {ref}`Defect and particle inspection <category-test>` | Unpatterned-wafer particle scans and patterned-wafer defect inspection. | None on the capabilities page; a job posting reads "SEM/AIT/KLA/SP1/EV300/1X"[^job-01] | {ref}`001 <step-001>`, {ref}`005 <step-005>`, {ref}`009 <step-009>`, {ref}`013 <step-013>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`025 <step-025>`, {ref}`029 <step-029>`, {ref}`033 <step-033>`, {ref}`035 <step-035>`, {ref}`039 <step-039>`, {ref}`042 <step-042>`, {ref}`046 <step-046>`, {ref}`048 <step-048>`, {ref}`051 <step-051>`, {ref}`054 <step-054>`, {ref}`057 <step-057>`, {ref}`060 <step-060>`, {ref}`061 <step-061>`, {ref}`067 <step-067>`, {ref}`070 <step-070>`, {ref}`074 <step-074>`, {ref}`082 <step-082>`, {ref}`084 <step-084>`, {ref}`086 <step-086>`, {ref}`087 <step-087>`, {ref}`090 <step-090>`, {ref}`091 <step-091>`, {ref}`095 <step-095>`, {ref}`100 <step-100>`, {ref}`106 <step-106>`, {ref}`107 <step-107>`, {ref}`110 <step-110>`, {ref}`111 <step-111>`, {ref}`113 <step-113>`, {ref}`116 <step-116>`–{ref}`118 <step-118>`, {ref}`121 <step-121>`, {ref}`122 <step-122>`, {ref}`124 <step-124>`, {ref}`127 <step-127>`–{ref}`129 <step-129>`, {ref}`132 <step-132>`, {ref}`133 <step-133>`, {ref}`137 <step-137>`, {ref}`139 <step-139>`, {ref}`142 <step-142>`–{ref}`144 <step-144>`, {ref}`147 <step-147>`, {ref}`148 <step-148>`, {ref}`152 <step-152>`, {ref}`154 <step-154>`, {ref}`157 <step-157>`–{ref}`159 <step-159>`, {ref}`162 <step-162>`, {ref}`164 <step-164>`, {ref}`165 <step-165>`, {ref}`167 <step-167>`–{ref}`169 <step-169>` |
| {ref}`Film thickness and stress metrology <category-deposition>` | Ellipsometers, reflectometers, FTIR and XRF gauges, and wafer-bow stress gauges on product or monitor wafers. | None named apart from the Mirra's "On board metrology"[^skw-01] | {ref}`002 <step-002>`, {ref}`003 <step-003>`, {ref}`010 <step-010>`–{ref}`013 <step-013>`, {ref}`039 <step-039>`, {ref}`040 <step-040>`, {ref}`043 <step-043>`, {ref}`046 <step-046>`–{ref}`048 <step-048>`, {ref}`058 <step-058>`, {ref}`059 <step-059>`, {ref}`063 <step-063>`, {ref}`076 <step-076>`, {ref}`077 <step-077>`, {ref}`080 <step-080>`, {ref}`089 <step-089>`–{ref}`092 <step-092>`, {ref}`095 <step-095>`, {ref}`097 <step-097>`, {ref}`099 <step-099>`–{ref}`101 <step-101>`, {ref}`104 <step-104>`–{ref}`106 <step-106>`, {ref}`109 <step-109>`–{ref}`112 <step-112>`, {ref}`115 <step-115>`–{ref}`117 <step-117>`, {ref}`120 <step-120>`–{ref}`123 <step-123>`, {ref}`126 <step-126>`–{ref}`128 <step-128>`, {ref}`131 <step-131>`–{ref}`136 <step-136>`, {ref}`138 <step-138>`, {ref}`141 <step-141>`–{ref}`143 <step-143>`, {ref}`146 <step-146>`–{ref}`151 <step-151>`, {ref}`153 <step-153>`, {ref}`156 <step-156>`–{ref}`158 <step-158>`, {ref}`161 <step-161>`, {ref}`164 <step-164>`, {ref}`167 <step-167>` |
| {ref}`Sheet-resistance and dose metrology <category-implant>` | Four-point probe and thermal-wave (modulated reflectance) monitors. | None named | {ref}`008 <step-008>`, {ref}`015 <step-015>`, {ref}`018 <step-018>`–{ref}`020 <step-020>`, {ref}`023 <step-023>`, {ref}`024 <step-024>`, {ref}`027 <step-027>`, {ref}`028 <step-028>`, {ref}`031 <step-031>`, {ref}`032 <step-032>`, {ref}`034 <step-034>`, {ref}`037 <step-037>`, {ref}`038 <step-038>`, {ref}`045 <step-045>`, {ref}`050 <step-050>`, {ref}`053 <step-053>`, {ref}`056 <step-056>`, {ref}`065 <step-065>`, {ref}`066 <step-066>`, {ref}`069 <step-069>`, {ref}`072 <step-072>`, {ref}`073 <step-073>`, {ref}`075 <step-075>`, {ref}`082 <step-082>`, {ref}`083 <step-083>`, {ref}`086 <step-086>`, {ref}`088 <step-088>`, {ref}`092 <step-092>`, {ref}`097 <step-097>`–{ref}`099 <step-099>`, {ref}`101 <step-101>`, {ref}`109 <step-109>`, {ref}`110 <step-110>`, {ref}`112 <step-112>`, {ref}`120 <step-120>`, {ref}`121 <step-121>`, {ref}`123 <step-123>`, {ref}`131 <step-131>`, {ref}`132 <step-132>`, {ref}`134 <step-134>`, {ref}`136 <step-136>`, {ref}`146 <step-146>`, {ref}`147 <step-147>`, {ref}`149 <step-149>`, {ref}`151 <step-151>`, {ref}`161 <step-161>` |
| {ref}`Cross-section SEM and profilers <category-etch>` | Trench, spacer, gap-fill and etch profiles; step height and dishing after CMP. | None assigned by a step page; the physical-analysis list includes "FEI Dual Beam FIB/SEM" and "Hitachi S-4800"[^skw-01] | *cross-section SEM:* {ref}`006 <step-006>`, {ref}`010 <step-010>`, {ref}`011 <step-011>`, {ref}`062 <step-062>`, {ref}`076 <step-076>`, {ref}`077 <step-077>`, {ref}`079 <step-079>`, {ref}`089 <step-089>`, {ref}`094 <step-094>`, {ref}`097 <step-097>`, {ref}`099 <step-099>`, {ref}`103 <step-103>`–{ref}`105 <step-105>`, {ref}`108 <step-108>`–{ref}`110 <step-110>`, {ref}`114 <step-114>`, {ref}`115 <step-115>`, {ref}`119 <step-119>`–{ref}`121 <step-121>`, {ref}`125 <step-125>`, {ref}`126 <step-126>`, {ref}`130 <step-130>`–{ref}`132 <step-132>`, {ref}`140 <step-140>`, {ref}`141 <step-141>`, {ref}`145 <step-145>`–{ref}`147 <step-147>`, {ref}`155 <step-155>`, {ref}`156 <step-156>`, {ref}`160 <step-160>`, {ref}`161 <step-161>`, {ref}`163 <step-163>`, {ref}`166 <step-166>`; *profiler or AFM:* {ref}`012 <step-012>`, {ref}`090 <step-090>`, {ref}`100 <step-100>`, {ref}`106 <step-106>`, {ref}`111 <step-111>`, {ref}`122 <step-122>`, {ref}`133 <step-133>`, {ref}`148 <step-148>` |
| {ref}`Parametric tester and prober <category-test>` | Electrical test of the scribe-line structures at the end of the flow; C–V, leakage and chain structures as electrical monitors. | "HP 4062UX" ("DC, capacitance, pulse generator, frequency counter"), "Engineering manual Probe Station"; no production prober[^skw-01] | {ref}`HPETEST <step-171>`; *electrical monitor named:* {ref}`040 <step-040>`, {ref}`043 <step-043>`, {ref}`047 <step-047>`, {ref}`063 <step-063>`, {ref}`096 <step-096>`, {ref}`098 <step-098>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`130 <step-130>`, {ref}`135 <step-135>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`145 <step-145>`, {ref}`150 <step-150>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`160 <step-160>`, {ref}`163 <step-163>`, {ref}`170 <step-170>` |

Notes on the table:

* **Two lithography rows for one vendor.** SkyWater's list says "DUV",
  not a wavelength;[^skw-01] the step pages read "ASML DUV stepper" and
  "ASML DUV scanner" as 248 nm (KrF) tools, and the
  {ref}`P1M <step-061>` page sets the two 193 nm scanners aside as later
  additions that "are not evidence for how the 130 nm gate was, or is,
  printed". The DUV row's *alternative:* list takes the i-line mask
  pages that offer a KrF tool as another way to print the layer
  ({ref}`DNM <step-007>`: "a KrF tool could equally print it"), not
  those that say a KrF tool could print it but "is not needed"
  ({ref}`NWM <step-017>`, {ref}`CAPM <step-137>`).
* **The dielectric etch row has no SkyWater tool.** SkyWater lists its
  production plasma etchers under "Metal Etch" and "Poly/Silicon Etch"
  only; its "Physical Analysis" group adds an "Oxford PlasmaLab RIE
  deprocessing" tool.[^skw-01]
  The local-interconnect contact, contact, via and nitride-seal etch
  pages say that no dielectric etcher is named and, like the pad etch
  page, grade the three poly/silicon etchers as
  candidates; the second table gives the grades.
* **Classes with no named SkyWater tool.** The "typically used" sections
  name a post-CMP brush scrubber, a production wafer prober, a plasma
  nitridation chamber, film-thickness, stress and sheet-resistance
  gauges, a single-wafer poly deposition chamber
  ({ref}`SAGD <step-048>`), a horizontal alloy furnace
  ({ref}`ALLY <step-170>`) and surface-analysis and bond-pull tools
  ({ref}`PDME <step-169>`); the last three have no row above. Apart from
  the Mirra's "On board metrology", the capabilities page names no tool
  of these classes, and its "Furnaces are all made by Aviza" does not
  say whether any furnace is horizontal.[^skw-01] It does list SEMs
  under "Physical Analysis" ("FEI Dual Beam FIB/SEM", "Hitachi
  S-4800"), but no step page assigns them the cross-sections that the
  "typically used" sections call for.[^skw-01] The
  CMP pages record the missing brush scrubber as an open question, and
  the {ref}`HPETEST <step-171>` page notes that no production prober is
  named.
* **Listed entries no step page assigns.** The capabilities page also
  lists "Atomic Layer Deposition", "AMAT Raider single wafer Cu
  plating", "Atmospheric selective oxidation", "Polyimide cure", "IPA
  clean" (under CMP), "Reticle storage/handler/defect inspection", the
  special modules other than the three in the second table, and a
  "Physical Analysis" group.[^skw-01] None of the 171 step pages assigns
  these to a SKY130 step; the {ref}`NTSD <step-167>` page mentions
  "Polyimide cure" only in asking whether a polyimide is applied.

## SkyWater's listed tools and the steps assigned to them

This table turns the main table round. For each tool, or group of tools
that the step pages quote together, it lists the steps whose "Machines
likely used at SkyWater" section names the tool, grouped by the words
the page uses for the *assignment* of the step to the tool:

* *inference* — the page names the tool as the likely one and marks the
  assignment an inference ("strong for the tool; inference for the
  assignment", or equivalent);
* *strong* — the page grades the entry strong without qualifying the
  assignment;
* *medium*, *medium/weak*, *weak-to-medium*, *weak* — the page grades
  the assignment itself, usually because it weighs several candidate
  tools;
* *strong for existence* — the page grades only the tool, typically for
  an alternative or for a clean or strip after the main operation;
* other wording is quoted or paraphrased as the page gives it.

The second column gives the source and strength of the listing itself
on the inventory's scale. The tool names are as SkyWater writes them;
"…" shortens an entry quoted in full in the main table. Steps that name
a tool only in passing (for example a metal etcher named as
corroboration on a deposition page) are listed with that wording.

| Tool as SkyWater lists it | Source; strength of the listing | Steps whose pages assign it, by the page's wording |
|---------------------------|-----------------------------------|----------------------------------------------------|
| "ASML I-line stepper", "ASML I-line scanner" | strong[^skw-01] | *inference:* {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`CAPM <step-137>`, {ref}`CAP2M <step-152>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>`; *not public which class (i-line or DUV):* {ref}`MM3 <step-139>`, {ref}`MM4 <step-154>`; *listed, not assigned:* {ref}`FOM <step-004>`, {ref}`VIM2 <step-129>` |
| "ASML DUV stepper", "ASML DUV scanner" | strong[^skw-01] | *inference:* {ref}`FOM <step-004>`, {ref}`P1M <step-061>`, {ref}`NPCM <step-078>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`VIM3 <step-144>`; *not public which class (i-line or DUV):* {ref}`MM3 <step-139>`, {ref}`MM4 <step-154>` |
| "ASML 193nm single stage scanner – 90nm CD", "ASML 193nm twin stage scanner – sub 65nm CD" | strong[^skw-01] | *not evidence for the 130 nm gate (a later addition):* {ref}`P1M <step-061>` |
| "DNS 80B track", "Sokudo RF3 track", "TEL ProZ Lithius track" | strong[^skw-01] | *strong, or strong for existence (some pages add that which track serves which exposure tool is not public):* {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`P1M <step-061>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>` |
| "AMAT Verity (multiple versions) CD", "AMAT VeraSEM" | strong[^skw-01] | *strong:* {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`P1ME <step-062>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`; *strong for existence; that the gate level is measured on them is an inference:* {ref}`P1M <step-061>`; *strong for existence:* {ref}`NSM <step-165>`, {ref}`PDM <step-168>` |
| "KLA 5200/5300/Archer overlay" | strong[^skw-01] | *strong:* {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`; *strong for existence; that the gate level is measured on them is an inference:* {ref}`P1M <step-061>`; *strong for existence:* {ref}`NSM <step-165>`, {ref}`PDM <step-168>` |
| "SEM/AIT/KLA/SP1/EV300/1X" (read as KLA-Tencor AIT and SP1) | medium[^job-01] | *medium:* {ref}`SMAT <step-001>`, {ref}`DNIS <step-009>`, {ref}`CMPNIT <step-012>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`TUNM <step-035>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`BFR <step-060>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>` |
| "Furnaces are all made by Aviza" (with the process lines quoted above) | strong[^skw-01] | *strong:* {ref}`BOX <step-002>`, {ref}`ISONIT <step-003>`; *inference:* {ref}`LINOX <step-010>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`, {ref}`SAGD <step-048>`, {ref}`GATENIT <step-058>`, {ref}`IOX45 <step-063>`, {ref}`SPNIT <step-076>`, {ref}`ALLY1 <step-096>`, {ref}`ALLY <step-170>`; *strong for existence (batch alternative):* {ref}`FILOX <step-011>`, {ref}`POC <step-059>`, {ref}`SPOX <step-080>`; *weak:* {ref}`RTAI <step-034>`, {ref}`TIPRTAD <step-075>`, {ref}`RTAD <step-088>`, {ref}`RTAD2 <step-092>`, {ref}`LINIT <step-104>`; *excluded on thermal grounds (inference):* {ref}`NTSD <step-167>` |
| "Ag Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C" | strong[^skw-01] | *inference:* {ref}`RTAI <step-034>`, {ref}`TIPRTAD <step-075>`, {ref}`RTAD <step-088>`, {ref}`RTAD2 <step-092>`, {ref}`CSIL <step-098>`; *weak:* {ref}`LINOX <step-010>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`, {ref}`IOX45 <step-063>`, {ref}`ALLY1 <step-096>`, {ref}`ALLY <step-170>` |
| "PECVD TEOS, C2 and Producer" | strong (models inferred)[^skw-01] | *inference:* {ref}`NCAPOX <step-091>`, {ref}`NCAPOX3 <step-117>`, {ref}`NCAPOX4 <step-128>`, {ref}`NCAPOX5 <step-143>`, {ref}`NCAPOX6 <step-158>`, {ref}`NFUSOX <step-164>`; *medium (as the whole film):* {ref}`NILD2 <step-105>`; *medium (as the liner or overburden):* {ref}`NILD3 <step-115>`, {ref}`NILD4 <step-126>`, {ref}`NILD5 <step-141>`, {ref}`NILD6 <step-156>`; *not public which of the candidates:* {ref}`POC <step-059>`; *weak:* {ref}`SPOX <step-080>`, {ref}`PSG <step-089>`, {ref}`CAPILD <step-135>`, {ref}`CAPILD2 <step-150>` |
| "PECVD silane oxide/nitride/oxynitride, C1", "PECVD nitride C1" | strong (model inferred)[^skw-01] | *inference:* {ref}`LINIT <step-104>`, {ref}`CAPILD <step-135>`, {ref}`CAPILD2 <step-150>`, {ref}`NTSD <step-167>`; *medium:* {ref}`NCAPOX <step-091>`, {ref}`NCAPOX3 <step-117>`, {ref}`NCAPOX4 <step-128>`, {ref}`NCAPOX5 <step-143>`, {ref}`NCAPOX6 <step-158>`, {ref}`NFUSOX <step-164>`; *not public which of the candidates:* {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`; *strong for existence:* {ref}`SPOX <step-080>`; *weak:* {ref}`SPNIT <step-076>`, {ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`, {ref}`NILD4 <step-126>`, {ref}`NILD5 <step-141>`, {ref}`NILD6 <step-156>` |
| "Lam/Novellus High Density Plasma (HDP) doped and phos doped with sputter etch" | strong[^skw-01][^skw-07] | *strong (two SkyWater statements):* {ref}`FILOX <step-011>`; *inference:* {ref}`PSG <step-089>`, {ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`, {ref}`NILD4 <step-126>`, {ref}`NILD5 <step-141>`, {ref}`NILD6 <step-156>` |
| "Lam/Novellus PECVD Tungsten" | strong (model inferred)[^skw-01] | *inference:* {ref}`WDEP <step-099>`, {ref}`WDEP2 <step-110>`, {ref}`WDEP3 <step-121>`, {ref}`WDEP4 <step-132>`, {ref}`WDEP5 <step-147>` |
| "AMAT PVD Metal" | strong for vendor and films (platform inferred)[^skw-01] | *inference: "Imp TiN" and "Collimated Ti":* {ref}`TI/TIN1 <step-097>`; *inference: "ESC TiN":* {ref}`LITIN <step-101>`; *inference: "Imp TiN":* {ref}`TIN2 <step-109>`, {ref}`TIN3 <step-120>`, {ref}`TIN4 <step-131>`, {ref}`TIN5 <step-146>`; *inference: aluminium, "TiW" and the underlayer:* {ref}`TIAL6 <step-112>`, {ref}`TIAL12 <step-123>`, {ref}`WTIAL3 <step-134>`, {ref}`WTIAL4 <step-149>`, {ref}`WTIAL5 <step-161>`; *inference: "TiW":* {ref}`CAPTIW1 <step-136>`, {ref}`CAPTIW2 <step-151>` |
| "Lam 9600, Al, TiW, TiN, Pt", "Lam 2300 Versys, Al, TiW, TiN, Nb, Pt" | strong[^skw-01] | *inference:* {ref}`LI1ME <step-103>`; *not public which of the two (the page leans to one, by inference):* {ref}`MM1E <step-114>`, {ref}`MM2E <step-125>`, {ref}`MM3E <step-140>`; *not public which of the two:* {ref}`CAPME <step-138>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`MM5E <step-163>`; *weak:* {ref}`PDME <step-169>`; *named as corroboration only:* {ref}`TIAL6 <step-112>`, {ref}`TIAL12 <step-123>`, {ref}`WTIAL3 <step-134>`, {ref}`CAPTIW1 <step-136>`, {ref}`WTIAL4 <step-149>`, {ref}`CAPTIW2 <step-151>`, {ref}`WTIAL5 <step-161>` |
| "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2" | strong[^skw-01] | *inference:* {ref}`STIE <step-006>`, {ref}`TUNARCE <step-036>`, {ref}`P1ME <step-062>`; *medium:* {ref}`STINITE <step-005>`, {ref}`ONOME <step-042>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`LI1ME <step-103>`; *weak:* {ref}`LICM1E <step-094>`, {ref}`CTME <step-108>`, {ref}`VIME <step-119>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`, {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>` |
| "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6, O2" | strong[^skw-01] | *inference:* {ref}`STINITE <step-005>`, {ref}`STIE <step-006>`, {ref}`TUNARCE <step-036>`, {ref}`ONOME <step-042>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`; *medium:* {ref}`P1ME <step-062>`, {ref}`PDME <step-169>`; *weak:* {ref}`LICM1E <step-094>`, {ref}`CTME <step-108>`, {ref}`VIME <step-119>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`, {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>` |
| "Lam 4400, HBr, Cl2, C2F6, CF4, SF6, O2" | strong[^skw-01] | *inference:* {ref}`STIE <step-006>`; *weak:* {ref}`STINITE <step-005>`, {ref}`ONOME <step-042>`, {ref}`P1ME <step-062>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`LICM1E <step-094>`, {ref}`CTME <step-108>`, {ref}`VIME <step-119>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`, {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>` |
| "Gasonic PEP …", "Iridia RF microwave …", "Mattson Aspen2 …" | strong[^skw-01] | *inference (which of the three not stated):* {ref}`DNIS <step-009>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`; *inference, the Iridia fitting a crust step best:* {ref}`P1IS <step-051>`, {ref}`ASTIS <step-067>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`; *weak:* {ref}`TUNARCE <step-036>`; *strong (strip after an etch):* {ref}`STIE <step-006>`; *strong for existence (strip after an etch):* {ref}`TUNME <step-039>`, {ref}`ONOME <step-042>`, {ref}`GOXETCH <step-046>`, {ref}`P1ME <step-062>`, {ref}`NPCME <step-079>`, {ref}`LICM1E <step-094>`, {ref}`SACETCH <step-095>`, {ref}`LI1ME <step-103>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`VIM3E <step-145>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`VIM4E <step-160>`, {ref}`MM5E <step-163>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>` |
| "Akrion Gamma Batch Wet Bench" | strong[^skw-01] | *strong ("the only phosphoric tank listed"):* {ref}`NS19 <step-013>`; *inference:* {ref}`DNIS <step-009>`, {ref}`TUNME <step-039>`, {ref}`GOXETCH <step-046>`; *strong for existence:* {ref}`STIE <step-006>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`ONOME <step-042>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`P1ME <step-062>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`LICM1E <step-094>`, {ref}`SACETCH <step-095>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>` |
| "DNS wet bench industry standard HF/SC1/SC2", "FSI Mercury industry standard HF/SC1/SC2 rotational" | strong[^skw-01] | *inference (the pre-furnace or pre-anneal clean; SC-2 is listed only for these two benches):* {ref}`SMAT <step-001>`, {ref}`BOX <step-002>`, {ref}`DNIS <step-009>`, {ref}`LINOX <step-010>`, {ref}`PWDEIS <step-033>`, {ref}`LDASTIS <step-074>`, {ref}`NSDIS <step-087>`; *inference:* {ref}`SACETCH <step-095>`; *inference for the DNS bench, strong for existence for FSI Mercury:* {ref}`TUNME <step-039>`, {ref}`GOXETCH <step-046>`; *strong for existence:* {ref}`STIE <step-006>`, {ref}`NS19 <step-013>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`P1ME <step-062>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`PDIS <step-084>`, {ref}`LICM1E <step-094>` |
| "Batch Rotational", "EKS265, EKC270 solvents" | strong[^skw-01] | *strong for existence (some pages add that the assignment is an inference):* {ref}`SACETCH <step-095>`, {ref}`LI1ME <step-103>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`VIM3E <step-145>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`VIM4E <step-160>`, {ref}`MM5E <step-163>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>` |
| "Single Wafer", "SEZ223, Davinci, HF, DSP+HF, titration controlled" | strong[^skw-01][^skw-07] | *inference (SEZ 223):* {ref}`BFR <step-060>`; *medium:* {ref}`SACETCH <step-095>`; *strong for existence:* {ref}`NS19 <step-013>`, {ref}`TUNME <step-039>`, {ref}`GOXETCH <step-046>`, {ref}`CTME <step-108>`, {ref}`VIME <step-119>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`; *named as the post-CMP clean; no brush scrubber named:* {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>` |
| "Axcelis 8250 Mid current …" | strong[^skw-01] | *inference:* {ref}`LVTNI <step-015>`, {ref}`LVTPI <step-020>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`NCHI <step-045>`, {ref}`UPRI <step-056>`, {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`, {ref}`2PSDI <step-083>`; *not stated which of two:* {ref}`PRI <step-053>`; *weak:* {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`ASTI <step-065>`; *strong for existence; unlikely, no phosphorus:* {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`; *named only as below the required dose:* {ref}`P1I <step-050>`, {ref}`PSDI <step-082>`, {ref}`NSDI <step-086>` |
| "Axcelis GSD High current/energy …" | strong[^skw-01] | *inference:* {ref}`DNI <step-008>`, {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`ASTI <step-065>`; *strong for existence:* {ref}`LVTPI <step-020>`, {ref}`PWDEI1 <step-031>`, {ref}`PSDI <step-082>`, {ref}`NSDI <step-086>`; *weak:* {ref}`PWDEI2 <step-032>`, {ref}`PTSI <step-037>`, {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>` |
| "Axcelis GSD Hi dose …" | strong[^skw-01] | *inference:* {ref}`P1I <step-050>`, {ref}`ASTI <step-065>`, {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`; *not stated which of two:* {ref}`PRI <step-053>`; *the alternative (no grade):* {ref}`UPRI <step-056>`; *weak:* {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>` |
| "Axcelis GSD High current/energy …" or "Axcelis GSD Hi dose …", either entry | strong[^skw-01] | *weak (which entry would serve not stated):* {ref}`LVTNI <step-015>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`DEPI <step-038>`, {ref}`NCHI <step-045>` |
| "AMAT Mirra CMP" | strong[^skw-01] | *inference from the film:* {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`CMPL <step-106>`, {ref}`CMPM <step-116>`, {ref}`CMPM2 <step-127>`, {ref}`CMPM3 <step-142>`, {ref}`CMPM4 <step-157>`; *inference from the film; which of the two tungsten processes not public:* {ref}`WCMPLI <step-100>`, {ref}`WCMP2 <step-111>`, {ref}`WCMP3 <step-122>`, {ref}`WCMP4 <step-133>`, {ref}`WCMP5 <step-148>` |
| "HP 4062UX" | strong[^skw-01] | *inference:* {ref}`CAPILD2 <step-150>`, {ref}`HPETEST <step-171>` |
| "Engineering manual Probe Station"; sort and reliability-lab tools | strong[^skw-01] | *named; no production prober, and the sort and reliability tools serve other purposes (inference):* {ref}`HPETEST <step-171>` |
| "Scribe: Lumonics Superclean" | strong[^skw-01] | *strong; the step is not stated:* {ref}`SMAT <step-001>` |
| Special modules "Nitrided gate oxide", "Ti and Co Silicide", "W plug dual damascene" | strong for the capability[^skw-01] | *inference for use in SKY130 (nitrided oxide):* {ref}`LVGOX <step-047>`, {ref}`IOX45 <step-063>`; *strong for the capability (silicide, W plug):* {ref}`CSIL <step-098>`, {ref}`WDEP <step-099>` |

Notes on the table:

* **Where the assignments are graded above an inference.** Only a few
  entries grade a step's tool as *strong* without qualifying the
  assignment: the Aviza furnaces for {ref}`BOX <step-002>` and
  {ref}`ISONIT <step-003>`, the Akrion bench for {ref}`NS19 <step-013>`
  (because it is "the only phosphoric tank listed") and the HDP system
  for {ref}`FILOX <step-011>`; the overlay and CD metrology entries on
  most mask pages are also graded *strong*. Everywhere else the step's
  tool is this reference's inference from the tool's listed capability.
* **Where the grades are weakest.** The *weak* grades fall mainly on
  alternatives: the second implanter on the implant pages, the batch or
  single-wafer tool on the oxidation and anneal pages, the other PECVD
  process on the dielectric-deposition pages, and the poly/silicon
  etchers on the contact, via, nitride-seal and pad etch pages, for which
  SkyWater lists no dielectric etcher.[^skw-01]
* **What the capability entries decide.** Some assignments follow from
  a capability that only one listed tool has: an energy range to
  "3000kev" only on the "Axcelis GSD High current/energy" entry, doses
  above "1e14" only on the two GSD entries (the 8250 entry, which also
  lacks phosphorus, stops at "1e14"), the only anneal listed with H₂ or
  forming gas, the furnaces' "H2 and forming gas alloy", "phosphoric" only on the
  Akrion bench, and, among the etchers, TiN only on the two metal
  etchers.[^skw-01] The pages that rely on these say so; the list itself
  still names no step.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — every SkyWater tool
  name, chemistry, dose range and capability quoted on this
  page.[^skw-01]
* SkyWater Technology, *A Day in the Life of a SkyWater Maintenance
  Technician* — the captions naming a Novellus high density plasma tool
  and a SEZ etcher tool.[^skw-07]
* Indeed, SkyWater *Defect Technician 2* posting — the defect-metrology
  tool list read as KLA-Tencor AIT and SP1.[^job-01]
* SkyWater Technology, Form S-1 (2021) — tool count, capacity and
  raw-material suppliers; no process-tool supplier named.[^sec-01]
* SkyWater Technology, Form 10-K for 2023 — the 90–350 nm flows in the
  Minnesota fab and the 2020 deep-trench etch addition.[^sec-02]
* Lam Research, Form 10-K for fiscal 2003 — the {term}`TCP` 9400, 2300 and
  Exelan product lines named on the etch pages.[^lam-10k]
* Axcelis Technologies, *GSD Ovation* product page — the GSD
  high-current and high-energy batch implanter family.[^axcelis-gsd-page]
* Applied Materials, *Endura PVD* product page — the platform the PVD
  pages read "AMAT PVD Metal" as.[^amat-endura]

### High-level understanding

* Quirk and Serda, *Semiconductor Manufacturing Technology* — a
  fab-floor view of each tool class, written around a 200 mm fab of the
  period.[^txt-07]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 — the
  unit processes the tool classes perform.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — STI, CMP,
  tungsten plugs, DUV lithography and RTP for the 0.25–0.13 µm
  generations.[^txt-05]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — chapter-per-process reference with equipment
  detail.[^txt-09]
* Encyclopedia.com, *Novellus Systems, Inc.* — the history of the
  Concept One and Two, Sequel, SPEED and Altus product lines the
  deposition pages refer to.[^novellus-history]
* Wikipedia, *Axcelis Technologies* and *KLA Corporation* — the
  implanter and inspection vendors behind several listed
  tools.[^wiki-axcelis][^wiki-kla]

### Deep dive

* Gronet and Gibbons (Applied Materials), US 5,155,336 — the
  lamp-heated rapid thermal processing chamber.[^pat-rtp-amat]
* Nulman, Krusius and Gat, *IEEE EDL* 1985 — rapid thermal oxidation of
  thin gate dielectrics, the single-wafer alternative to the
  furnace.[^nulman-1985]
* SemiStar, *AG Associates Heatpulse 8800 / 8808* — reseller
  specification of the RTP family SkyWater lists.[^ag-8800]
* Moov, *Aviza / SVG / Thermco AVP 8000* listing — the vendor's 200 mm
  vertical batch furnace.[^aviza-avp]
* Tan, Li and Zygmunt (Applied Materials), US 6,914,016 — HDP-CVD gap
  fill of high-aspect-ratio gaps.[^pat-hdp-amat]
* Lee and Collins (Novellus), US 6,635,965 — the pulsed nucleation
  layer behind SkyWater's "PNL option".[^pat-pnl-novellus]
* Gopalraja et al. (Applied Materials), US 6,350,353 — ionised-metal
  plasma (IMP) sputtering for liner step coverage.[^pat-imp-amat]
* Lai et al. (Novellus), US 6,179,973 — the hollow-cathode-magnetron
  ionised PVD source, the Novellus counterpart to IMP.[^pat-hcm-novellus]
* ASML, PAS 5500/750E press release, 2000 — a KrF step-and-scan system
  aimed at 130 nm.[^asml-750e]
* Tokyo Electron, *Coater/Developer ACT Series* — the track class linked
  to the exposure tools.[^tel-act]
* GCE Market, *KLA-Tencor 8100XP CD-SEM* — specification of a CD-SEM of
  the period.[^gce-kla8100]
* Ogle (Lam Research), US 4,948,458 — the transformer-coupled planar
  plasma source of the TCP etchers.[^pat-tcp-lam]
* Yin et al. (Applied Materials), US 5,540,824 — the decoupled-source
  plasma reactor of the DPS etchers.[^pat-dps-amat]
* Stanford Nanofabrication Facility, *Lam Research TCP 9400 Poly
  Etcher* — a university guide to the etcher SkyWater lists.[^snf-9400]
* Lam Research, Exelan High Performance press release, 2001 — the
  dielectric etcher class the contact and via pages cite.[^lam-exelan]
* Kamarehi and Simpson (Fusion Systems), US 5,498,308 — the microwave
  downstream asher.[^pat-asher-fusion]
* Kern, *J. Electrochem. Soc.* 1990 — the evolution of wafer cleaning
  that the wet benches carry out.[^kern-1990]
* SEZ, Spin-Processor 223 press release, 1999 — a dual-chamber spin
  processor for cleaning and film removal.[^sez-223-pr]
* Current, *J. Vac. Sci. Technol. A* 1996 — production ion implanters
  from a vacuum perspective.[^current-1996]
* Semiconductor Online, *8250HT Medium Current Ion Implanter* — the
  energy and beam-current range of the medium-current class.[^axcelis-8250]
* Mezack et al., IIT 2000 — a single-wafer high-current implanter of the
  period.[^mezack-2000]
* Tolles et al. (Applied Materials), US 5,738,574 — the continuous
  multi-station CMP system of the Mirra.[^pat-cmp-mirra]
* Keithley Instruments, *Series S600 Parametric Test Systems* — the
  parametric tester class used for electrical test.[^keithley-s600]
* ITRS 2001, *Lithography* — the roadmap the mask pages use to allocate
  layers to i-line and DUV exposure.[^itrs-03]

(machines-inconsistencies)=
## Open questions and inconsistencies

The items below were found while extracting the machine sections of all
171 step pages and comparing the tool names they quote with SkyWater's
capabilities page and maintenance-technician profile, both re-read on
2026-09-13.[^skw-01][^skw-07] Items that two consistency passes over the
step pages on 2026-09-13 resolved have been removed from this list.

### How tool names are written

After those passes the step pages quote both SkyWater pages as written
and, outside quotation marks, write each tool name in one form. Where
the vendor's own name identifies the product, the pages use it:
GaSonics, as the company styled itself;[^gasonics-2000] Mattson Aspen
II, the platform name Mattson used;[^mattson-2001] SEZ 223, SEZ's
"Spin-Processor 223";[^sez-223-pr] Da Vinci, SEZ's spelling for its
single-wafer cleaning tools;[^sez-2005] and AG Associates Heatpulse
8808, as the reseller documentation names the family.[^ag-8800] The
solvents are written EKC265/EKC270; whether SkyWater's "EKS265" is the
same product is not stated.[^skw-01] The track is written "TEL ProZ
Lithius", SkyWater's word order without a slash: TEL describes its
LITHIUS Pro Z as a 300 mm coater/developer for the 10 nm
node,[^tel-lithius] so this reference does not identify the 200 mm
fab's track with that model. SkyWater's two GSD entries are written
"Axcelis GSD high-current/high-energy implanter" and "Axcelis GSD
high-dose implanter"; a page that offers a GSD implanter as an
alternative without choosing between them says so.[^skw-01]

The "typically used" sections write the resist asher class as
"Downstream plasma asher", the KrF exposure class as "DUV (KrF, 248 nm)
stepper or scanner" and the polisher as "Rotary multi-platen CMP
polisher". One pair of names is kept on purpose: the oxide contact, via
and seal-ring etches name a "Dielectric etcher" (Exelan- or MxP-class
tools), while the nitride etches ({ref}`STINITE <step-005>`,
{ref}`SPE <step-077>`, {ref}`NPCME <step-079>`) and the pad etch
({ref}`PDME <step-169>`) name a "Dielectric/nitride plasma etcher",
because their representative models include the Lam TCP 9400
poly/nitride class.

### Different tools or grades for analogous steps

The passes applied one treatment to each group of analogous steps: the
three poly/silicon etchers graded alike on the contact, via and
seal-ring etches (weak) and on the nitride etches (the Lam 9400 TCP
inferred, the DPS II medium, the Lam 4400 weak); the "C1" oxide medium
on every cap oxide; the HDP note, a medium TEOS grade and a weak "C1"
liner on every inter-level oxide; the technician profile graded as a
SkyWater statement; one Mirra wording, AIT/SP1 inspection and the
"Track ammonia clean" and "IPA clean" entries on every CMP page;
*inference* or *weak* on the tilted implants; bench and asher
assignments graded as inferences on the cleans; and CD metrology on
every mask page. The differences that remain rest on a reason the pages
state:

* **The pad etch.** {ref}`PDME <step-169>` grades the Lam 9400 TCP
  "medium", above the weak grade of the contact and via etches, because
  it removes mainly passivation nitride and the 9400 is the one listed
  etcher whose entry names nitride.[^skw-01]
* **Inter-level oxides.** The TEOS grade is medium on all five, but on
  {ref}`NILD2 <step-105>` for the whole film (a 1:1 gap) and on
  {ref}`NILD3 <step-115>` to {ref}`NILD6 <step-156>` for the liner or
  overburden only, since those gaps would need a
  deposition–etch–deposition TEOS fill.
* **Ashers after crusted implants.** {ref}`P1IS <step-051>`,
  {ref}`ASTIS <step-067>`, {ref}`PDIS <step-084>` and
  {ref}`NSDIS <step-087>` single out the Iridia's hydrogen chemistry and
  40 °C floor for the crust of a high-dose implant; the other implant
  strips, after the pages' lighter implants, make no choice. {ref}`DNIS <step-009>` and
  {ref}`LVTPIS <step-021>` describe a thick crust from MeV well implants
  at modest dose and also make no choice; whether that crust calls for
  the same reading is left open, since no public source ties a crust
  thickness to these implants.
* **Strength of the metrology listings.** Most mask pages grade the
  overlay and CD tools "strong", while {ref}`P1M <step-061>`,
  {ref}`NSM <step-165>` and {ref}`PDM <step-168>` write "strong for
  existence"; the evidence is the same list entry, and the stricter
  wording is the one the scale supports, but aligning all 36 mask pages
  was left for a later pass.

### Open questions

* **"PECVD Tungsten".** SkyWater lists "Lam/Novellus PECVD
  Tungsten";[^skw-01] the five tungsten-fill pages quote the entry,
  describe a WF₆-based blanket CVD (reading pulsed nucleation from the
  "PNL option") and read the word "PECVD" as a label for the tungsten
  CVD tool rather than evidence of a plasma-assisted deposition. The
  capabilities page does not explain it.
* **The dielectric etcher.** No dielectric etcher appears among the
  process tools on the capabilities page (its "Physical Analysis" group
  lists an "Oxford PlasmaLab RIE deprocessing" tool);[^skw-01] whether the contact, via, nitride-seal and
  pad etches run on the listed poly/silicon etchers or on a tool the
  page does not list is not public.
* **Models behind generic entries.** "C1", "C2 and Producer", "AMAT PVD
  Metal", the Lam/Novellus HDP and the "PECVD Tungsten" system are read
  on the step pages as Novellus Concept One and Concept Two, an Applied
  Materials Producer, an Endura-class PVD platform, a SPEED-class HDP
  system and an Altus-class tungsten system; SkyWater states none of
  these models.[^skw-01]
* **Which exposure class and which track.** Whether metal 3 and metal 4
  are printed on i-line or DUV tools, and which of the three tracks
  serves which exposure tool, are not public.
* **The two GSD entries.** Whether "Axcelis GSD High current/energy" and
  "Axcelis GSD Hi dose" are two machines or two configurations is not
  stated;[^skw-01] several implant pages depend on which entry reaches
  which dose and energy.
* **Tools with no named SkyWater model.** No post-CMP brush scrubber,
  production wafer prober, plasma nitridation chamber or in-line
  film-thickness, stress or sheet-resistance gauge is named in any
  public SkyWater source the step pages found.
* **Age of the list.** The capabilities page is a current list for a
  fab that also runs 90 nm and other flows and was expanded in
  2020;[^skw-01][^sec-02] which of the listed tools, if any, were used
  when the S8 process was set up at Cypress is not public.

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    retrieved 2026-09-13; tab "Sheet1" lists the 171 steps (number, code and
    description). <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
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
[^lam-10k]: Lam Research Corporation, Form 10-K for the fiscal year ended
    2003-06-29 (product line: TCP 9400PTX/DFM, 2300, Exelan).
    <https://www.sec.gov/Archives/edgar/data/707549/000089161803004913/f93126e10vk.htm>
[^axcelis-gsd-page]: Axcelis Technologies, *GSD Ovation — High Current &
    High Energy Batch Ion Implanters*, product page, accessed 2026-08-30.
    <https://www.axcelis.com/products/gsd-ovation/>
[^amat-endura]: Applied Materials, *Endura PVD*, product page.
    <https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing Technology*,
    Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI Era,
    Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4: Deep-Submicron
    Process Technology*, Lattice Press, 2002, ISBN 978-0-9616721-7-1.
    <https://openlibrary.org/isbn/9780961672171>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007, ISBN
    978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.* (company
    history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^wiki-axcelis]: Wikipedia, *Axcelis Technologies*.
    <https://en.wikipedia.org/wiki/Axcelis_Technologies>
[^wiki-kla]: Wikipedia, *KLA Corporation*.
    <https://en.wikipedia.org/wiki/KLA_Corporation>
[^pat-rtp-amat]: C. M. Gronet and J. F. Gibbons (Applied Materials), *Rapid
    thermal heating apparatus and method*, US 5,155,336 A, granted
    1992-10-13. <https://patents.google.com/patent/US5155336A/en>
[^nulman-1985]: J. Nulman, J. P. Krusius and A. Gat, "Rapid thermal
    processing of thin gate dielectrics. Oxidation of silicon", *IEEE
    Electron Device Letters* **6**(5), 205–207 (1985).
    <https://doi.org/10.1109/EDL.1985.26099>
[^ag-8800]: SemiStar Corp., *AG Associates Heatpulse 8800 / 8808 Rapid
    Thermal Processing* (reseller specification page), accessed 2026-08-30.
    <https://www.semistarcorp.com/product/ag-associates-heatpulse-8800-8808/>
[^aviza-avp]: Moov used-equipment marketplace, *Aviza / SVG / Thermco AVP
    8000* listing, accessed 2026-08-30.
    <https://moov.co/marketplace/furnaces-diffusion/aviza-svg/aviza-asml-svg-watkinsjohnson-avp-8000>
[^pat-hdp-amat]: Z. Tan, D. Li and W. Zygmunt (Applied Materials), *HDP-CVD
    deposition process for filling high aspect ratio gaps*, US 6,914,016 B2,
    granted 2005-07-05. <https://patents.google.com/patent/US6914016B2/en>
[^pat-pnl-novellus]: S.-H. Lee and J. Collins (Novellus Systems), *Method
    for producing ultra-thin tungsten layers with improved step coverage*,
    US 6,635,965 B1, filed 2001-10-09, granted 2003-10-21.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6635965>
[^pat-imp-amat]: P. Gopalraja, S. Edelstein, A. Tepman, P. Ding, D. Ghosh
    and N. Maity (Applied Materials), *Alternate steps of IMP and sputtering
    process to improve sidewall coverage*, US 6,350,353 B2, filed
    1999-11-24, granted 2002-02-26.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6350353>
[^pat-hcm-novellus]: K. F. Lai et al. (Novellus Systems), *Apparatus and
    method for controlling plasma uniformity across a substrate*, US
    6,179,973 B1, filed 1999-06-30, granted 2001-01-30.
    <https://patents.google.com/patent/US6179973B1/en>
[^asml-750e]: ASML, *ASML introduces KrF lithography scanner* (PAS
    5500/750E), press release, 2000-04-04.
    <https://www.asml.com/en/news/press-releases/2000/asml-introduces-krf-lithography-scanner-optimized-for>
[^tel-act]: Tokyo Electron, *Coater/Developer ACT Series*, product page.
    <https://www.tel.com/product/act.html>
[^gce-kla8100]: GCE Market, *KLA-Tencor 8100XP CD-SEM* (specification
    summary).
    <https://www.gcemarket.com/gce/gce.nsf/products/kla-tencor-8100xp-cd-sem-7expup>
[^pat-tcp-lam]: J. S. Ogle (Lam Research Corporation), *Method and apparatus
    for producing magnetically-coupled planar plasma*, US 4,948,458 A,
    granted 1990-08-14. <https://patents.google.com/patent/US4948458A/en>
[^pat-dps-amat]: G. Z. Yin, H. Hanawa, D. X. Ma and D. Olgado (Applied
    Materials), *Plasma reactor with multi-section RF coil and isolated
    conducting lid*, US 5,540,824 A, granted 1996-07-30.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5540824>
[^snf-9400]: Stanford Nanofabrication Facility, *Lam Research TCP 9400 Poly
    Etcher (lampoly)*, equipment page.
    <https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>
[^lam-exelan]: Lam Research, *Lam Research Corporation Advances Dielectric
    Etch Capabilities With Launch Of Exelan High Performance*, press
    release, 2001-07-09.
    <https://newsroom.lamresearch.com/2001-07-09-Lam-Research-Corporation-Advances-Dielectric-Etch-Capabilities-With-Launch-Of-Exelan-R-High-Performance>
[^pat-asher-fusion]: M. Kamarehi and J. E. Simpson (Fusion Systems), *Plasma
    asher with microwave trap*, US 5,498,308 A, granted 1996-03-12.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5498308>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning Technology",
    *Journal of The Electrochemical Society* **137**(6), 1887–1892 (1990).
    <https://doi.org/10.1149/1.2086825>
[^sez-223-pr]: SEZ Group, *SEZ Doubles Wafer Processing Capabilities With
    New Dual Chamber Spin-Processing System* (press release, 1999-12-13),
    reproduced by Surface Finishing / VertMarkets.
    <https://www.surfacefinishing.com/doc/sez-doubles-wafer-processing-capabilities-wit-0001>
[^sez-2005]: SEZ Group, *World-Leading Korean Manufacturer Places
    Multi-System Order for SEZ Da Vinci Tools*, press release,
    2005-03-02; Wayback Machine capture of 2009-01-07.
    <https://web.archive.org/web/20090107032902/http://www.sez.com/02_Mar_05__World_Leading_Korean_Manufacturer_Places_Multi_System_Order_for_SEZ_Da_Vinci__Tools.SEZ>
[^gasonics-2000]: GaSonics International, home page; Wayback Machine
    capture of 2000-03-01.
    <https://web.archive.org/web/20000301102837/http://www.gasonics.com:80/>
[^mattson-2001]: Mattson Technology, *The Aspen Strip*, product page;
    Wayback Machine capture of 2001-12-19.
    <https://web.archive.org/web/20011219013713/http://www.mattson.com/products/aspen_strip.html>
[^tel-lithius]: Tokyo Electron, *Coater/Developer LITHIUS Series*,
    product page, accessed 2026-09-13.
    <https://www.tel.com/product/lithius.html>
[^current-1996]: M. I. Current, "Ion implantation for silicon device
    manufacturing: A vacuum perspective", *Journal of Vacuum Science &
    Technology A* **14**(3), 1115–1123 (1996).
    <https://doi.org/10.1116/1.580279>
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion Implanter*
    (Eaton Semiconductor Equipment Operations product description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^mezack-2000]: G. Mezack, T. Callahan, S. Mehta and U. Jeong, "Advantages
    of the Varian VIISta single wafer high current ion implanter for
    advanced device fabrication", *Proc. 2000 International Conference on
    Ion Implantation Technology*, pp. 431–434.
    <https://doi.org/10.1109/IIT.2000.924180>
[^pat-cmp-mirra]: R. D. Tolles, N. Shendon, S. Somekh, I. Perlov, E.
    Gantvarg and H. Q. Lee (Applied Materials), *Continuous processing
    system for chemical mechanical polishing*, US 5,738,574 A, granted
    1998-04-14. <https://patents.google.com/patent/US5738574A/en>
[^keithley-s600]: Keithley Instruments, *Series S600 Parametric Test
    Systems*, data sheet.
    <https://download.tek.com/datasheet/SeriesS600_DataSht.pdf>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
