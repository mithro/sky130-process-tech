(material-hardware-consumables)=
# Hardware consumables and abatement

Every process tool wears out parts of itself. A furnace consumes its
quartz or silicon-carbide tubes, boats and baffles; a plasma etcher, CVD
chamber or sputtering chamber consumes the rings, liners, domes,
showerheads, shields and chuck surfaces that the plasma or the film
attacks; a rapid thermal processor consumes lamps and quartz windows;
and an electrical tester consumes probe cards and their needles. Behind
the tools, the exhaust and waste of the processes pass through traps,
scrubbers and abatement systems that are themselves maintained and
replaced. On the step pages' readings, 92 of SKY130's 171 steps name
hardware of this kind among their resources. This page describes the
class in general, lists representative parts and abatement methods, and
then says what SkyWater and public regulators have published about them
at the Minnesota fab and which SKY130 steps name them. The tools are on
the {ref}`machines index <machines-index>` pages; the process gases whose
by-products are abated are in the {ref}`materials index <materials-index>`.

| | Hardware consumables and abatement |
|---|---|
| What they do | Hold, heat, confine and contact the wafer, and are worn by doing so; "Fused quartz and silica tubes are needed in the semiconductor industry for the manufacturing of batch processing equipment used in CVD, Diffusion and Annealing tools".[^heraeus-tubes] |
| Furnace ware | Quartz tubes, boats and insulation plates;[^pat-vf-insulation-tel][^pat-boat-tel] silicon-carbide carriers and dummy wafers "impervious to acid attack".[^entegris-supersic] |
| Chamber parts | Domes, liners, rings, showerheads, shields and chucks; wall coatings "cause large and uncontrolled shifts in the etch process".[^joubert-2004] |
| RTP parts | Tungsten-halogen lamps "arranged in 2 banks of 14 lamps each";[^ag-8800] quartzware, cooling water and CDA or nitrogen.[^ag-8108] |
| Abatement | Traps, scrubbers, thermal and plasma abatement; point-of-use plasma abatement converts PFCs "to products that can be scrubbed downstream of the backing pump".[^fiala-1999] |
| Probe cards | Needles "made of tungsten or tungsten/rhenium alloys or advanced palladium based alloys"; "contamination builds up on the tips".[^wiki-probecard] |
| SkyWater evidence | "Furnaces are all made by Aviza"; "Ag Heatpulse 8808"; "HP 4062UX" parametric test; "Engineering manual Probe Station";[^skw-01] "essential materials, tools and maintenance parts";[^sec-01] EPA records of the site's electronics-manufacturing (subpart I) greenhouse-gas reports[^epa-ghgrp-skywater] |
| SKY130 steps | 92 steps; see {ref}`SKY130 steps that use this class <material-hardware-consumables-steps>` |

## What the class is and what it does

These consumables are parts of machines rather than materials that reach
the wafer, but they set what does reach it: particles and metals shed by
worn parts, film thickness drift as a chamber wall coats, temperature
error as a lamp ages, contact resistance as a probe tip loads, and the
emissions a fab is permitted to release. They are replaced on schedules
tied to wafer counts, RF hours or kilowatt-hours, cleaned and requalified,
and bought from tool makers and specialist part suppliers. SkyWater's S-1
names the category among its risks: "availability concerns with respect
to some of our essential materials, tools and maintenance parts could
also prompt a lengthy and expensive search for alternative sources which
would necessitate requalification cycles and production
delays".[^sec-01]

### Furnace ware

A batch furnace holds a column of wafers in a quartz or silicon-carbide
boat inside a process tube. Heraeus Covantics states that fused quartz
and silica tubes "serve as chemically pure reaction chambers, as gas or
liquid inlets or as transportation pipes", and offers grades up to
synthetic silica of "parts per billion class purity".[^heraeus-tubes]
The design of the ware is process-critical: a Tokyo Electron boat
supports wafers on rings so that "a surface defect called a slip
generated when the wafer is heat treated can be eliminated";[^pat-boat-tel]
a Tokyo Electron furnace stands the boat on "thin heat insulation plates"
above the furnace throat;[^pat-vf-insulation-tel] and a Kokusai patent
adds a boat cover inside the inner and outer tubes of an LPCVD furnace
so that the film "is improved in uniformity and
homogeneity".[^pat-lpcvd-kokusai] Sodium diffuses through quartz: Eisele and
Ruthardt described stabilised fused-quartz tubes with reduced sodium
diffusion.[^eisele-1978] Heat also limits the ware's life: Heraeus offers
stabilised tubes for high-temperature use "to reduce the possibility of
sagging at elevated working temperatures",[^heraeus-tubes] and silica
glass can crystallise (devitrify) where it is contaminated — Horii et al.
heated silica glasses in contact with a NaCl grain and found a
crystallised region whose depth grew with the square root of the heating
time.[^horii-2010] Silicon carbide is the alternative: Entegris
describes converted SiC with contamination "typically below 5 ppm" and
states that its dummy wafers "can be cleaned and reused indefinitely in
LPCVD or diffusion processes".[^entegris-supersic] Deposition furnaces
coat their ware with film, which is removed at tube cleans; the step pages
list quartz or silicon-carbide tubes and tube cleaning for the nitride
and silicon furnaces.

### Plasma, CVD and PVD chamber parts

Plasma chambers erode and coat their own walls. Joubert et al. wrote that
layers deposited on reactor walls "cause large and uncontrolled shifts in
the etch process",[^joubert-2004] and Cunge et al. found that in HBr/Cl₂
gate-etch plasmas the walls stay clean without oxygen but grow a silicon
oxychloride layer as oxygen is added.[^cunge-2005] Parts shed
contamination: Bell and Joubert traced sidewall oxide to sputtering of
"the quartz tube of the helicon source";[^bell-1996] Ito et al. found
AlF₃ particles from the "coating material Al2O3 on the etching chamber
wall" and suppressed them by dehydrating the chamber parts;[^ito-2008]
and an Applied Materials HDP-CVD patent attributes sodium to the quartz
dome and alumina nozzles and deposits a seasoning film after each clean
to hold it back.[^pat-seasoning-amat] Coatings resist attack: a patent
by Sun et al. adds "a ceramic-based surface coating, high purity yttrium
oxide coating" on anodised aluminium parts "against fluorine and oxygen
plasma attack".[^pat-yttria] Tool makers design against consumable cost;
Lam's 9600DFM release claimed design advances that "virtually eliminate
the cost of consumables", with a customer reporting a mean time between
cleans of "more than 300 RF hours".[^lam-9600dfm-2001] In sputtering
chambers, collimators capture off-normal metal[^rossnagel-1991] and IMP
coils are pasted with target material;[^pat-imp-coil-amat] shields and
kits are changed with the targets ({ref}`material-sputter-targets`).

### Rapid thermal processing parts

A lamp-heated RTP chamber consumes its light source and its window. The
Heatpulse 8800/8808 page describes "Tungsten halogen lamps and cold
process-chamber walls which allow fast wafer heating and cooling rates",
with lamps "arranged in 2 banks of 14 lamps each";[^ag-8800] the same
reseller's specifications list cooling water, CDA or nitrogen for tube
cooling and exhausts among the facilities.[^ag-8108] Temperature is
sensed by pyrometer or thermocouple,[^ag-8800] and its calibration depends
on the wafer and chamber:
Chen et al. used test wafers with thin-film thermocouples to study how
emissivity affects lightpipe thermometry.[^chen-2002-rtp]

### Exhaust abatement and waste treatment

Process exhaust carries unreacted gases and by-products that must be
trapped, destroyed or scrubbed before release. Some condense: ammonium
chloride from nitride furnaces "forms a solid condensate at temperatures
below about 125° C." in exhaust lines and pumps,[^pat-nh4cl-vlsi] and a
TSMC patent describes it as "a fine powder" that "may be syphoned back
into the furnace".[^pat-nh4cl-tsmc] Fluorinated gases are potent
greenhouse gases — in the IPCC Fourth Assessment Report values that
Wikipedia tabulates, NF₃ has a 100-year global warming potential (GWP)
of 17,200 and C₂F₆ one of 12,200[^wiki-gwp] — and are destroyed by
combustion, electric heating or plasma: Fiala et al.
modelled point-of-use plasma abatement between the turbomolecular and
backing pumps;[^fiala-1999] Hu et al. studied NF₃ decomposition in
point-of-use "wet-thermal-wet abatement" of PECVD chamber
cleaning;[^hu-2018] and Mangyou et al. reported an atmospheric plasma
system treating "up to 80 L/min of CF4 exhaust with 95% of
DRE".[^mangyou-2005] Hydrides can also be taken up at ambient
temperature by solid adsorbents: Hsu et al. found that copper, zinc and
cerium oxides on alumina removed silane with an efficiency above 99.9 %
before breakthrough,[^hsu-2007] and tested copper on sol-gel alumina for
phosphine, which "local scrubbers must immediately abate" because of its
toxicity.[^hsu-2010] Johnson, Ridgeway and Maroulis describe process
changes in CVD cleaning and etch that reduce PFC emissions at
source,[^johnson-2004] and Sherer's book covers point-of-use devices and
the centralised acid and ammonia scrubbers of a fab's exhaust
system.[^sherer-2005]

### Probe cards

A probe card connects the tester to the pads of the structures under
test. "Normally a probe card is inserted into a wafer prober", and cards
are "broadly classified into needle type, vertical type, and MEMS";
needles "are made of tungsten or tungsten/rhenium alloys or advanced
palladium based alloys like PdCuAg", and "contamination builds up on the
tips as a result of successive touchdown events", which harms contact
resistance.[^wiki-probecard] Broz and Rincon measured the contact
resistance of tungsten, tungsten–rhenium, beryllium–copper and alloy
probes on aluminium pads at elevated temperature;[^broz-1999] Roggei and
Seshan addressed "resistance increase between probes and pads during the
probing process" through the fab process;[^roggei-1999] and Electroglas
described how a prober connects the wafer to a parametric or functional
tester through the card.[^electroglas-1999]

## Representative materials and grades

The parts below are sold by tool makers and specialist suppliers to tool
and process specifications; the supplier statements describe their
catalogues, not the parts SkyWater buys.

* **Quartz tubes and ware.** Electrically fused quartz tubes in grades
  from "HSQ®100" to "HSQ®330S", stabilised "HSQ®400" for high temperature,
  and synthetic "HSQ®900" silica.[^heraeus-tubes]
* **Silicon-carbide ware.** Horizontal-furnace carriers, "baffle
  assemblies", "LTO cages" and dummy wafers of converted SiC.[^entegris-supersic]
* **Heaters and insulation.** Multi-zone heaters, rated "600-1200° C (Up
  to 1250° C for > 4 Hours)" on one vertical reactor;[^expertech-vtr]
  insulation plates at the furnace throat.[^pat-vf-insulation-tel]
* **Chamber kits.** Quartz, ceramic, silicon or coated aluminium domes,
  liners, focus and edge rings, showerheads and nozzles, electrostatic
  chucks, shields, coils and collimators, as the machine pages describe
  them;[^pat-hdp-reactor-amat][^pat-yttria][^amat-ism-2000] exclusion
  rings on tungsten CVD pedestals.[^novellus-wcvd-2002]
* **RTP parts.** Tungsten-halogen lamps, quartz isolation tubes or
  windows, and pyrometer and thermocouple calibration
  hardware.[^ag-8800][^chen-2002-rtp]
* **Abatement.** Heated traps for condensable by-products,[^pat-nh4cl-vlsi]
  thermal or plasma point-of-use abatement for fluorinated
  gases,[^hu-2018][^mangyou-2005][^fiala-1999] adsorbent beds for
  hydrides such as silane and phosphine,[^hsu-2007][^hsu-2010] and central
  wet scrubbers.[^sherer-2005]
* **Probe cards and cleaning.** Needle, vertical and MEMS
  cards;[^wiki-probecard] Entegris lists, among CMC Materials' products,
  "Highly engineered cleaning materials for advanced probe cards, test
  socket applications, and chuck-cleaning".[^entegris-cmc-2022]

## At SkyWater

### What SkyWater's filings and pages list

SkyWater's *Facilities & Capabilities* page names tools, not their
parts.[^skw-01] The entries that bear on this class are "Furnaces are all
made by Aviza"; "Ag Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C" under
"RTA"; the etchers, deposition tools and PVD chambers described on the
machine pages; and, under "Wafer Sort/Test":

> "Parametric Test" · "HP 4062UX" · "– DC, capacitance, pulse generator,
> frequency counter" · "– automatic data upload, SPC, analysis,
> disposition" · "Engineering manual Probe Station"

with "Summit 200 Prober/Tester" and "PMC200 Cryo Probe" in the
reliability laboratory and "Cryogenic probing down to 8-Kelvin" under
"Other Services".[^skw-01] The page names no quartzware, chamber kit,
lamp, probe card, trap or abatement system. The S-1 includes "maintenance
parts" among essential items (quoted above), states that "We use,
generate and discharge hazardous chemicals and waste in our research and
development and manufacturing activities", and states that "our
facilities are ISO 14001 certified",[^sec-01] and the annual report for
fiscal 2023 lists "ISO 14001:2015" among the certifications "for our
Minnesota facility".[^sec-02] SkyWater's certifications
page lists for SkyWater Minnesota "ISO14004 Environmental Management
system" among its accreditations.[^skw-certs] SkyWater's maintenance
technician profile describes work on tool robots and "the pneumatic
controls of a vacuum system".[^skw-07]

Two public regulator sources bear on emissions at the Bloomington site.
The EPA's Greenhouse Gas Reporting Program lists the facility at
2401 E. 86th St., Bloomington, as reporting under subparts "C,I" in each
year from 2011 to 2023;[^epa-ghgrp-skywater] subpart I covers electronics
manufacturing, whose reports include "Controlled emissions of GHGs from
abatement systems, if applicable" and an "Inventory and description of
all abatement systems through which fluorinated GHGs or N2O flow at the
facility and for which destruction or removal efficiency is
claimed".[^epa-ghgrp-subpart-i] The Minnesota Pollution Control Agency's
enforcement release of 2025-02-04 on SkyWater's air permit lists, among
its findings, "Taking credit for greenhouse gas emissions control
equipment that was not allowed in permit", and records that SkyWater
"has taken corrective action and has submitted a complete permit
application".[^mpca-2025]

### Strength of the evidence

The tool entries are SkyWater statements and rank as **strong** evidence
for the tools whose parts this page describes, on the scale of the
{ref}`machines index <machines-reading-evidence>`, but they name no
part.[^skw-01] The EPA record is **strong** that the site reported as an
electronics-manufacturing facility under subpart I; the record retrieved
names no abatement system, so that the site claims abatement is not shown
by it.[^epa-ghgrp-skywater][^epa-ghgrp-subpart-i] The MPCA release refers to
greenhouse-gas "emissions control equipment" in a permit context; it
does not say what the equipment is, which gases or tools it serves, or
whether it is in service (our reading).[^mpca-2025] Quartzware, chamber
kits, lamps, probe cards and traps at SkyWater appear in no public source
cited here; their
descriptions on the step pages are industry practice.

(material-hardware-consumables-steps)=
### SKY130 steps that use this class

This page covers the rows of the {ref}`materials index <materials-table>`
listed below by key; the steps are those whose *Resources required* section
names one of them (the union of the rows' *Steps* cells).

Materials index rows covered:

* `furnace-ware` — furnace ware: quartz or SiC tubes, boats, baffles, liners
* `chamber-parts` — plasma, CVD and PVD chamber parts
* `rtp-parts` — RTP consumables: lamps, quartz, edge rings, cooling
* `abatement` — exhaust abatement and waste treatment
* `probe-cards` — probe cards, needles, cleaning media and standards

Steps:

{ref}`BOX <step-002>`, {ref}`ISONIT <step-003>`, {ref}`STINITE <step-005>`, {ref}`STIE <step-006>`, {ref}`LINOX <step-010>`, {ref}`FILOX <step-011>`, {ref}`CMPNIT <step-012>`, {ref}`RTAI <step-034>`, {ref}`TUNARCE <step-036>`, {ref}`ONO <step-040>`, {ref}`ONOME <step-042>`, {ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`, {ref}`SAGD <step-048>`, {ref}`P1IS <step-051>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`BFR <step-060>`, {ref}`P1ME <step-062>`, {ref}`IOX45 <step-063>`, {ref}`ASTIS <step-067>`, {ref}`TIPRTAD <step-075>`, {ref}`SPNIT <step-076>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`SPOX <step-080>`, {ref}`NSDI <step-086>`, {ref}`NSDIS <step-087>`, {ref}`RTAD <step-088>`, {ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`, {ref}`RTAD2 <step-092>`, {ref}`LICM1E <step-094>`, {ref}`ALLY1 <step-096>`, {ref}`TI/TIN1 <step-097>`, {ref}`CSIL <step-098>`, {ref}`WDEP <step-099>`, {ref}`LITIN <step-101>`, {ref}`LI1ME <step-103>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`CTME <step-108>`, {ref}`TIN2 <step-109>`, {ref}`WDEP2 <step-110>`, {ref}`WCMP2 <step-111>`, {ref}`TIAL6 <step-112>`, {ref}`MM1E <step-114>`, {ref}`NILD3 <step-115>`, {ref}`CMPM <step-116>`, {ref}`NCAPOX3 <step-117>`, {ref}`VIME <step-119>`, {ref}`TIN3 <step-120>`, {ref}`WDEP3 <step-121>`, {ref}`WCMP3 <step-122>`, {ref}`TIAL12 <step-123>`, {ref}`MM2E <step-125>`, {ref}`NILD4 <step-126>`, {ref}`CMPM2 <step-127>`, {ref}`NCAPOX4 <step-128>`, {ref}`VIM2E <step-130>`, {ref}`TIN4 <step-131>`, {ref}`WDEP4 <step-132>`, {ref}`WCMP4 <step-133>`, {ref}`WTIAL3 <step-134>`, {ref}`CAPILD <step-135>`, {ref}`CAPTIW1 <step-136>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`NILD5 <step-141>`, {ref}`CMPM3 <step-142>`, {ref}`NCAPOX5 <step-143>`, {ref}`VIM3E <step-145>`, {ref}`TIN5 <step-146>`, {ref}`WDEP5 <step-147>`, {ref}`WCMP5 <step-148>`, {ref}`WTIAL4 <step-149>`, {ref}`CAPILD2 <step-150>`, {ref}`CAPTIW2 <step-151>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`NILD6 <step-156>`, {ref}`CMPM4 <step-157>`, {ref}`NCAPOX6 <step-158>`, {ref}`VIM4E <step-160>`, {ref}`WTIAL5 <step-161>`, {ref}`MM5E <step-163>`, {ref}`NFUSOX <step-164>`, {ref}`NSME <step-166>`, {ref}`NTSD <step-167>`, {ref}`PDME <step-169>`, {ref}`ALLY <step-170>`, {ref}`HPETEST <step-171>`

<!-- step-tables:begin (generated by tools/gen_step_tables.py; do not edit) -->
:::{dropdown} All 92 steps (links)

See the grouped bullets below for what each step's assignment means.
:::
<!-- step-tables:end -->

The steps fall into groups by row, as the step pages' *Resources
required* sections describe them:

* **Furnace ware** — the oxidation, LPCVD and alloy furnace steps, from
  {ref}`BOX <step-002>` to {ref}`ALLY <step-170>`, with
  {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`,
  {ref}`IOX45 <step-063>`, {ref}`SPNIT <step-076>` and
  {ref}`SPOX <step-080>` naming quartz ware as one of two tool options.
* **Chamber parts** — the plasma etches, HDP and PECVD depositions,
  tungsten CVD and PVD steps, and the single-wafer backside removal at
  {ref}`BFR <step-060>`.
* **RTP parts** — the rapid thermal steps {ref}`RTAI <step-034>`,
  {ref}`TIPRTAD <step-075>`, {ref}`RTAD <step-088>`,
  {ref}`RTAD2 <step-092>` and {ref}`CSIL <step-098>`, and the RTP option
  at {ref}`IOX45 <step-063>`.
* **Abatement and waste** — the nitride and silicon furnaces, the
  tungsten depositions and polishes, the chlorine metal etches, the
  fluorine pad and seal-ring etches, the arsenic implant and several
  implant strips, the
  oxide polishes and the backside acid etch.
* **Probe cards** — the e-test at {ref}`HPETEST <step-171>`.

## Supply, handling, safety and facilities

None of the SkyWater sources cited here describes the fab's parts
logistics, cleaning or abatement systems; the points below are industry
practice or supplier, literature and regulator statements.

* **Parts supply and requalification.** Parts come from tool makers and
  specialist suppliers; the S-1 warns that shortages of "maintenance
  parts" would force "requalification cycles and production
  delays".[^sec-01]
* **Cleaning and seasoning.** Chamber cleans and seasoning films restore
  a chamber after maintenance;[^pat-seasoning-amat][^cunge-2005] quartz
  and SiC ware is cleaned in acid, SiC because it is "impervious to acid
  attack".[^entegris-supersic]
* **Traps and pumps.** Heated traps and pump maintenance for condensable
  by-products such as ammonium chloride;[^pat-nh4cl-vlsi][^pat-nh4cl-tsmc]
  the step pages add dry-pump maintenance and exhaust abatement at the
  silane furnace ({ref}`SAGD <step-048>`).
* **Greenhouse-gas reporting.** Electronics facilities that report under
  subpart I report fluorinated-gas and N₂O emissions and describe the
  abatement systems for which they claim destruction or removal
  efficiency;[^epa-ghgrp-subpart-i] the Bloomington facility's records show
  subpart I reports for each year from 2011 to 2023.[^epa-ghgrp-skywater]
* **Probe-card care.** Tips are cleaned to restore contact
  resistance,[^wiki-probecard] and contact resistance varies with probe
  material and temperature.[^broz-1999]

## Process-integration notes for SKY130

These notes connect the class to the step pages; they add no SKY130
conditions of their own. SKY130's parts schedules, abatement and probe
cards are not public.

* **Nitride furnaces and ammonium chloride.** On their pages' readings,
  {ref}`ISONIT <step-003>` and {ref}`ONO <step-040>` deposit nitride from
  dichlorosilane and ammonia, whose ammonium chloride
  loads exhaust lines, pumps and traps;[^pat-nh4cl-vlsi][^pat-nh4cl-tsmc]
  the ISONIT page lists an HCl-tolerant exhaust and tube cleaning, and the
  ONO page quartz ware periodically cleaned of nitride.
* **Chamber walls and gate CD.** On its page's reading, the gate etch at
  {ref}`P1ME <step-062>` runs in HBr/Cl₂/O₂, a chemistry in which wall
  coatings change with oxygen addition;[^cunge-2005] the step page names
  chamber consumables
  and monitor wafers together, since chamber state and CD drift are
  controlled together (our reading).
* **Metal etches and chlorine.** The metal etches from
  {ref}`MM1E <step-114>` to {ref}`MM5E <step-163>` name chlorine abatement
  and chamber parts replaced often; the MM3E and MM5E pages tie the
  replacement rate to metal thickness.
* **Fluorinated cleans.** The HDP, PECVD and tungsten CVD pages name NF₃
  chamber cleans, whose unreacted NF₃ and by-products need
  abatement;[^wiki-nf3][^hu-2018] SkyWater lists NF₃ only on its DPSII
  etcher entry.[^skw-01]
* **RTP calibration.** The five RTP step pages name lamps, quartz and
  thermocouple or pyrometer calibration; lamp and window condition and
  wafer emissivity affect the temperature the recipe
  achieves.[^chen-2002-rtp][^ag-8800]
* **Probing the e-test structures.** The public SKY130 test tile
  "consists of a grid of probe points",[^raw-data-testtile-prop] and the
  replacement open test tile, a Google, NIST and University of Michigan
  OpenFASoC design, documents its own test interface with an image whose
  alternative text is "Probing Card";[^raw-data-testtile-open] neither
  document describes SkyWater's production e-test probe cards. The
  {ref}`HPETEST <step-171>` page names probe cards laid out for the e-test
  modules. SkyWater lists no production prober.[^skw-01]

## Related pages

* {ref}`machine-vertical-furnace-oxidation`,
  {ref}`machine-vertical-furnace-lpcvd` and
  {ref}`machine-vertical-furnace-anneal` — furnace ware.
* {ref}`machine-plasma-etcher-silicon`,
  {ref}`machine-plasma-etcher-dielectric`,
  {ref}`machine-plasma-etcher-metal`, {ref}`machine-pecvd`,
  {ref}`machine-hdp-cvd`, {ref}`machine-tungsten-cvd` and
  {ref}`machine-pvd-cluster-tool` — chamber parts.
* {ref}`machine-rapid-thermal-processor` — lamps and quartz.
* {ref}`machine-parametric-tester` — probe cards.
* {ref}`material-substrates` — monitor, dummy and calibration wafers.
* {ref}`materials-index` — the gases whose exhaust is abated.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

* {ref}`Thermal trap for gaseous materials <patent-gp25448458>` — US 5,303,558 A (1992)
* {ref}`Vertical heat treatment apparatus <patent-gp17268321>` — US 5,709,543 A (1995)
* {ref}`Boat for heat treatment <patent-gp17432179>` — US 5,820,367 A (1995)
* {ref}`Vertical furnace of a semiconductor manufacturing apparatus and a boat cover thereof <patent-gp18429343>` — US 5,902,103 A (1995)
* {ref}`Avoiding contamination from induction coil in ionized sputtering <patent-gp24741421>` — US 5,707,498 A (1996)
* {ref}`Symmetric tunable inductively coupled HDP-CVD reactor <patent-gp24728963>` — US 6,170,428 B1 (1996)
* {ref}`Reduction of mobile ion and metal contamination in HDP-CVD chambers using chamber seasoning film depositions <patent-gp25360177>` — US 6,121,161 A (1997)
* {ref}`Yttrium oxide based surface coating for semiconductor IC processing vacuum chambers <patent-gp32848879>` — US 6,776,873 B1 (2002)
* {ref}`Cold trap for CVD furnace <patent-gp32068901>` — US 2004/0069224 A1 (2002)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater Technology, [*Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) and [*Certifications &
  Policies*](<https://www.skywatertechnology.com/certifications-policies/>) — the tool and test entries and the Minnesota site's
  environmental accreditation.[^skw-01][^skw-certs]
* SkyWater Technology, Form S-1 (2021) and 10-K for fiscal 2023 —
  maintenance parts, hazardous materials and ISO 14001.[^sec-01][^sec-02]
* [SkyWater Technology, maintenance-technician profile](<https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>) — tool maintenance
  work.[^skw-07]
* US EPA, GHGRP facility record and *Subpart I Information Sheet* —
  electronics-manufacturing reporting and abatement
  systems.[^epa-ghgrp-skywater][^epa-ghgrp-subpart-i]
* [Minnesota Pollution Control Agency, 2025 enforcement release](<https://www.pca.state.mn.us/news-and-stories/skywater-technology-fined-more-than-97000-for-air-permit-violations>) — a permit
  finding that mentions greenhouse-gas control equipment.[^mpca-2025]
* Heraeus Covantics, [*Fused Quartz and Silica Tubes*](<https://www.heraeus-covantics.com/products-and-solutions/products-by-shape/tubes/fused-quartz-and-silica-tubes-for-semiconductor-applications>); Entegris,
  [*SUPERSiC*](<https://www.entegris.com/content/dam/shared-product-assets/specialty-shared/brochure-supersic-semiconductor-front-end-6116.pdf>) brochure and [*CMC Materials | July 2022*](<https://www.entegris.com/en/home/brands/cmc-materials-july-2022.html>) — quartz, SiC and
  probe-card cleaning products.[^heraeus-tubes][^entegris-supersic][^entegris-cmc-2022]
* SemiStar, Heatpulse 8800/8808 page and specifications — lamps and
  facilities.[^ag-8800][^ag-8108]
* [Lam Research, TCP 9600DFM release](<https://investor.lamresearch.com/2001-06-18-Lam-Research-Corporation-Takes-Metal-Processing-To-New-Level-With-New-TCP-R-9600DFM>) — consumables cost and time between
  cleans.[^lam-9600dfm-2001]
* SkyWater PDK Authors, raw-data test tiles — the proprietary tile's
  probe points and the open OpenFASoC tile's test-interface image, which
  do not describe SkyWater's production probe
  cards.[^raw-data-testtile-prop][^raw-data-testtile-open]

### High-level understanding

* Wikipedia, [*Probe card*](<https://en.wikipedia.org/wiki/Probe_card>), [*Nitrogen trifluoride*](<https://en.wikipedia.org/wiki/Nitrogen_trifluoride>) and [*Global warming
  potential*](<https://en.wikipedia.org/wiki/Global_warming_potential>) — probe cards, NF₃ chamber cleaning and the greenhouse
  potential of clean and etch gases.[^wiki-probecard][^wiki-nf3][^wiki-gwp]
* [Wikipedia, *ISO 14000 series*](<https://en.wikipedia.org/wiki/ISO_14000_series>) — the environmental-management standards
  and what ISO 14001 and ISO 14004 each cover.[^wiki-iso14000]
* [Sherer, *Semiconductor Industry: Wafer Fab Exhaust Management*](<https://doi.org/10.1201/9781420027198>) —
  point-of-use and central exhaust treatment.[^sherer-2005]
* [Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology*](<https://openlibrary.org/isbn/9781574446753>) — tools, exhaust by-products and facilities.[^txt-09]
* [Expertech, *VTR7000PLUS*](<https://www.exper-tech.com/products/vertical-thermal-reactor>) — a vertical reactor's heater and
  load.[^expertech-vtr]
* [Electroglas, 1999 annual report](<https://web.archive.org/web/20020530031508/http://www.electroglas.com:80/press/pressreleases/reports/1999annual/wafer.htm>) — wafer probing.[^electroglas-1999]

### Deep dive

* [Eisele and Ruthardt, *JES* 1978](<https://doi.org/10.1149/1.2131646>) — stabilised quartz tubes against
  sodium.[^eisele-1978]
* [Horii et al., *J. Ceram. Soc. Japan* 2010](<https://doi.org/10.2109/jcersj2.118.318>) — crystallisation of silica
  glass in contact with NaCl.[^horii-2010]
* [Osawa (Tokyo Electron), US 5,820,367](<https://patents.google.com/patent/US5820367A/en>) — a ring boat against
  slip.[^pat-boat-tel]
* [Shimazu (Tokyo Electron), US 5,709,543](<https://patents.google.com/patent/US5709543A/en>) — furnace-throat
  insulation.[^pat-vf-insulation-tel]
* [Maeda et al. (Kokusai), US 5,902,103](<https://patents.google.com/patent/US5902103A/en>) — LPCVD tubes and a boat
  cover.[^pat-lpcvd-kokusai]
* [Joubert et al., *JVST A* 2004](<https://doi.org/10.1116/1.1697484>) — monitoring chamber-wall
  coatings.[^joubert-2004]
* [Cunge et al., *PSST* 2005](<https://doi.org/10.1088/0963-0252/14/2/S06>) — plasma–wall interactions in gate
  etch.[^cunge-2005]
* [Bell and Joubert, *JVST B* 1996](<https://doi.org/10.1116/1.588758>) — quartz sputtered from a helicon
  source.[^bell-1996]
* [Ito et al., *JJAP* 2008](<https://doi.org/10.1143/JJAP.47.3630>) — AlF₃ particles from chamber
  walls.[^ito-2008]
* [Rossman et al. (Applied Materials), US 6,121,161](<https://patents.google.com/patent/US6121161A/en>) — seasoning films
  against dome and nozzle contamination.[^pat-seasoning-amat]
* [Redeker et al. (Applied Materials), US 6,170,428](<https://patents.google.com/patent/US6170428B1/en>) — an HDP-CVD reactor's
  dome, chuck and clean.[^pat-hdp-reactor-amat]
* [Sun et al., US 6,776,873](<https://patents.google.com/patent/US6776873B1/en>) — yttria coatings on chamber
  parts.[^pat-yttria]
* [Rossnagel et al., *JVST A* 1991](<https://doi.org/10.1116/1.577531>) — collimated sputtering.[^rossnagel-1991]
* [Chen et al., RTP 2002](<https://doi.org/10.1109/RTP.2002.1039440>) — emissivity and RTP temperature
  measurement.[^chen-2002-rtp]
* [Caton et al. (VLSI Technology), US 5,303,558](<https://patents.google.com/patent/US5303558A/en>) — a thermal trap for
  ammonium chloride.[^pat-nh4cl-vlsi]
* [Lin et al. (TSMC), US 2004/0069224](<https://patents.google.com/patent/US20040069224A1/en>) — a cold trap for a CVD
  furnace.[^pat-nh4cl-tsmc]
* [Fiala et al., *JAP* 1999](<https://doi.org/10.1063/1.370711>) — point-of-use plasma abatement of
  PFCs.[^fiala-1999]
* [Hu et al., *IEEE TSM* 2018](<https://doi.org/10.1109/TSM.2018.2808173>) — wet-thermal-wet abatement of
  NF₃.[^hu-2018]
* [Mangyou et al., ISSM 2005](<https://doi.org/10.1109/ISSM.2005.1513352>) — atmospheric plasma PFC
  abatement.[^mangyou-2005]
* Hsu et al., *JAWMA* 2007 and 2010 — metal-oxide and copper adsorbents
  on alumina for silane and phosphine removal.[^hsu-2007][^hsu-2010]
* [Johnson, Ridgeway and Maroulis, *IEEE TSM* 2004](<https://doi.org/10.1109/TSM.2004.835700>) — PFC reduction in CVD
  and etch.[^johnson-2004]
* [Broz and Rincon, ITC 1999](<https://doi.org/10.1109/TEST.1999.805761>) — probe contact resistance at
  temperature.[^broz-1999]
* [Roggei and Seshan, ISSM 1999](<https://doi.org/10.1109/ISSM.1999.808775>) — probe-to-pad contact
  resistance.[^roggei-1999]

## Open questions

* SkyWater's furnace ware, chamber kits, lamps, probe cards and their
  suppliers and schedules are not public.[^skw-01]
* Which abatement systems the Bloomington fab uses, for which gases and
  tools, and what the MPCA meant by "greenhouse gas emissions control
  equipment", are not stated in the sources cited here.[^mpca-2025][^epa-ghgrp-skywater]
* Which prober runs the SKY130 e-test, and what probe cards it uses, is
  not public; SkyWater lists an "Engineering manual Probe Station" with
  its parametric tester.[^skw-01]
* SkyWater's certifications page lists "ISO14004" for Minnesota, while
  the 10-K lists ISO 14001:2015 for the Minnesota
  facility;[^skw-certs][^sec-02] ISO 14004 is the
  implementation-guidelines standard of the series,[^wiki-iso14000] so we
  read the web listing as a slip for ISO 14001 (our inference).

<!-- footnotes -->

[^heraeus-tubes]: Heraeus Covantics, *Fused Quartz and Silica Tubes for
    Semiconductor Applications*, product page, accessed 2026-09-13.
    <https://www.heraeus-covantics.com/products-and-solutions/products-by-shape/tubes/fused-quartz-and-silica-tubes-for-semiconductor-applications>
[^pat-vf-insulation-tel]: T. Shimazu (Tokyo Electron), *Vertical heat
    treatment apparatus*, US 5,709,543 A, filed 1996-09-04, granted
    1998-01-20. <https://patents.google.com/patent/US5709543A/en>
[^pat-boat-tel]: T. Osawa (Tokyo Electron), *Boat for heat treatment*,
    US 5,820,367 A, filed 1996-09-18, granted 1998-10-13.
    <https://patents.google.com/patent/US5820367A/en>
[^entegris-supersic]: Entegris, Inc., *SUPERSiC® Silicon Carbide:
    Products for semiconductor front end processes*, brochure 6116,
    accessed 2026-09-13.
    <https://www.entegris.com/content/dam/shared-product-assets/specialty-shared/brochure-supersic-semiconductor-front-end-6116.pdf>
[^joubert-2004]: O. Joubert, G. Cunge, B. Pelissier, L. Vallier, M.
    Kogelschatz and E. Pargon, "Monitoring chamber walls coating
    deposited during plasma processes: Application to silicon gate etch
    processes", *Journal of Vacuum Science & Technology A* **22**(3),
    553–563 (2004). <https://doi.org/10.1116/1.1697484>
[^ag-8800]: SemiStar Corp., *AG Associates Heatpulse 8800 / 8808 Rapid
    Thermal Processing* (reseller specification page), accessed
    2026-08-30; lamp description re-checked 2026-09-13.
    <https://www.semistarcorp.com/product/ag-associates-heatpulse-8800-8808/>
[^ag-8108]: SemiStar Corp., *AG Associates Heatpulse 4100 / 8108 / 8800
    / 8800i Specifications* (reseller PDF; operating specifications and
    facilities for each model), accessed 2026-08-30; re-checked
    2026-09-13.
    <https://www.semistarcorp.com/wp-content/uploads/2025/12/AG-Associates-Heatpulse-4100-8108-8800-8800i-Specifications-Rapid-Thermal-Processor.pdf>
[^fiala-1999]: A. Fiala, M. Kiehlbauch, S. Mahnovski and D. B. Graves,
    "Model of point-of-use plasma abatement of perfluorinated compounds
    with an inductively coupled plasma", *Journal of Applied Physics*
    **86**(1), 152–162 (1999). <https://doi.org/10.1063/1.370711>
[^wiki-probecard]: Wikipedia, *Probe card*.
    <https://en.wikipedia.org/wiki/Probe_card>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; furnace, RTA, test and other-services entries re-checked
    2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; risk factors on raw materials, tools
    and maintenance parts, and "Environmental, Safety and Quality
    Matters"; read from a Wayback Machine copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; certifications list and "Environmental, Safety and
    Quality Matters"; read from a Wayback Machine copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^wiki-iso14000]: Wikipedia, *ISO 14000 series*, accessed 2026-09-13.
    <https://en.wikipedia.org/wiki/ISO_14000_series>
[^epa-ghgrp-skywater]: US Environmental Protection Agency, Greenhouse Gas
    Reporting Program, Envirofacts `pub_dim_facility` records for
    facility 1000354 ("SKYWATER TECHNOLOGY INC", 2401 E. 86th St.,
    Bloomington, MN), reporting years 2010–2023, retrieved 2026-09-13.
    <https://data.epa.gov/efservice/pub_dim_facility/facility_name/CONTAINING/SKYWATER/JSON>
[^mpca-2025]: Minnesota Pollution Control Agency, *SkyWater Technology
    fined more than $97,000 for violations with their air permit,
    federal regulations and Minnesota rules*, news release, 2025-02-04,
    accessed 2026-09-13.
    <https://www.pca.state.mn.us/news-and-stories/skywater-technology-fined-more-than-97000-for-air-permit-violations>
[^pat-lpcvd-kokusai]: K. Maeda, S. Kakizaki, T. Taniyama, H. Yanagawa and
    K. Suzaki (Kokusai Electric), *Vertical furnace of a semiconductor
    manufacturing apparatus and a boat cover thereof*, US 5,902,103 A,
    filed 1996-12-23, granted 1999-05-11.
    <https://patents.google.com/patent/US5902103A/en>
[^eisele-1978]: K. M. Eisele and R. Ruthardt, "Stabilized Fused-Quartz
    Tubes with Reduced Sodium Diffusion for Semiconductor Device
    Technology", *Journal of The Electrochemical Society* **125**(7),
    1188–1190 (1978). <https://doi.org/10.1149/1.2131646>
[^cunge-2005]: G. Cunge, M. Kogelschatz, O. Joubert and N. Sadeghi,
    "Plasma–wall interactions during silicon etching processes in
    high-density HBr/Cl₂/O₂ plasmas", *Plasma Sources Science and
    Technology* **14**(2), S42–S52 (2005).
    <https://doi.org/10.1088/0963-0252/14/2/S06>
[^bell-1996]: F. H. Bell and O. Joubert, "Polysilicon gate etching in
    high density plasmas. III. X-ray photoelectron spectroscopy
    investigation of sidewall passivation of silicon trenches using an
    oxide hard mask", *Journal of Vacuum Science & Technology B*
    **14**(4), 2493–2499 (1996). <https://doi.org/10.1116/1.588758>
[^ito-2008]: N. Ito, T. Moriya, F. Uesugi, M. Matsumoto, S. Liu and Y.
    Kitayama, "Reduction of Particle Contamination in Plasma-Etching
    Equipment by Dehydration of Chamber Wall", *Japanese Journal of
    Applied Physics* **47**(5R), 3630 (2008).
    <https://doi.org/10.1143/JJAP.47.3630>
[^pat-seasoning-amat]: K. Rossman, T. Sahin, H. M'Saad and R. Nowak
    (Applied Materials), *Reduction of mobile ion and metal contamination
    in HDP-CVD chambers using chamber seasoning film depositions*,
    US 6,121,161 A, filed 1999-01-19, granted 2000-09-19.
    <https://patents.google.com/patent/US6121161A/en>
[^pat-yttria]: J. Y. Sun, S. J. Wu, S. Thach, A. H. Kumar, R. W. Wu,
    H. Wang, Y. Lin and C. C. Stow, *Yttrium oxide based surface coating
    for semiconductor IC processing vacuum chambers*, US 6,776,873 B1,
    filed 2002-02-14, granted 2004-08-17.
    <https://patents.google.com/patent/US6776873B1/en>
[^lam-9600dfm-2001]: Lam Research, *Lam Research Corporation Takes Metal
    Processing To New Level With New TCP 9600DFM*, press release,
    2001-06-18.
    <https://investor.lamresearch.com/2001-06-18-Lam-Research-Corporation-Takes-Metal-Processing-To-New-Level-With-New-TCP-R-9600DFM>
[^rossnagel-1991]: S. M. Rossnagel, D. Mikalsen, H. Kinoshita and J. J.
    Cuomo, "Collimated magnetron sputter deposition", *Journal of Vacuum
    Science & Technology A* **9**(2), 261–265 (1991).
    <https://doi.org/10.1116/1.577531>
[^pat-imp-coil-amat]: K. K.-T. Ngan (Applied Materials), *Avoiding
    contamination from induction coil in ionized sputtering*,
    US 5,707,498 A, filed 1996-07-12, granted 1998-01-13.
    <https://patents.google.com/patent/US5707498A/en>
[^chen-2002-rtp]: D. Chen, D. DeWitt, B. Tsai, K. Kreider and W. Kimes,
    "Effects of wafer emissivity on rapid thermal processing
    temperature measurement", *Proc. 10th IEEE International Conference
    on Advanced Thermal Processing of Semiconductors (RTP 2002)*,
    pp. 59–67. <https://doi.org/10.1109/RTP.2002.1039440>
[^pat-nh4cl-vlsi]: O. L. Caton, C. A. Bellows, C. M. Hebert, Jr. and
    S. J. Schaper (VLSI Technology), *Thermal trap for gaseous
    materials*, US 5,303,558 A, filed 1992-07-30, granted 1994-04-19.
    <https://patents.google.com/patent/US5303558A/en>
[^pat-nh4cl-tsmc]: L. Lin, T. Fan, S. Chen, V. Lee and Y.-H. Wu (Taiwan
    Semiconductor Manufacturing Company), *Cold trap for CVD furnace*,
    US 2004/0069224 A1, filed 2002-10-11, published 2004-04-15.
    <https://patents.google.com/patent/US20040069224A1/en>
[^wiki-nf3]: Wikipedia, *Nitrogen trifluoride*.
    <https://en.wikipedia.org/wiki/Nitrogen_trifluoride>
[^wiki-gwp]: Wikipedia, *Global warming potential*, table "Earlier
    values from 2007" (IPCC Fourth Assessment Report, 100-year values),
    accessed 2026-09-13.
    <https://en.wikipedia.org/wiki/Global_warming_potential>
[^hu-2018]: S.-C. Hu, A. Shiue, W.-T. Tseng and G. Leggett,
    "Perfluorocompound Emissions Control and Kinetic Characteristics in
    Point-of-Use Wet-Thermal-Wet Abatement of Plasma-Enhanced Chemical
    Vapor Deposition Chamber Cleaning", *IEEE Transactions on
    Semiconductor Manufacturing* **31**(2), 302–308 (2018).
    <https://doi.org/10.1109/TSM.2018.2808173>
[^mangyou-2005]: H. Mangyou, N. Watanabe, K. Hattori, T. Watanabe, Y.
    Sugimori, K. Shibuya and S. Hasaka, "High performance atmospheric
    plasma abatement system for PFC reduction", *ISSM 2005, IEEE
    International Symposium on Semiconductor Manufacturing*,
    pp. 263–266. <https://doi.org/10.1109/ISSM.2005.1513352>
[^horii-2010]: N. Horii, M. Kamide, A. Inouye and N. Kuzuu,
    "Crystallization of silica glass upon heating by contact with a NaCl
    crystal grain", *Journal of the Ceramic Society of Japan*
    **118**(1376), 318–320 (2010).
    <https://doi.org/10.2109/jcersj2.118.318>
[^hsu-2007]: J.-N. Hsu, C.-J. Tsai, C. Chiang and S.-N. Li, "Silane
    Removal at Ambient Temperature by Using Alumina-Supported Metal Oxide
    Adsorbents", *Journal of the Air & Waste Management Association*
    **57**(2), 204–210 (2007).
    <https://doi.org/10.1080/10473289.2007.10465309>
[^hsu-2010]: J.-N. Hsu, H. Bai, S.-N. Li and C.-J. Tsai, "Copper Loaded
    on Sol-Gel-Derived Alumina Adsorbents for Phosphine Removal",
    *Journal of the Air & Waste Management Association* **60**(5),
    629–635 (2010). <https://doi.org/10.3155/1047-3289.60.5.629>
[^johnson-2004]: A. D. Johnson, R. G. Ridgeway and P. J. Maroulis,
    "Reduction of PFC emissions to the environment through advances in
    CVD and etch processes", *IEEE Transactions on Semiconductor
    Manufacturing* **17**(4), 491–496 (2004).
    <https://doi.org/10.1109/TSM.2004.835700>
[^sherer-2005]: J. M. Sherer, *Semiconductor Industry: Wafer Fab Exhaust
    Management*, CRC Press, 2005. <https://doi.org/10.1201/9781420027198>
[^broz-1999]: J. J. Broz and R. M. Rincon, "Probe contact resistance
    variations during elevated temperature wafer test", *Proc.
    International Test Conference 1999*, pp. 396–405.
    <https://doi.org/10.1109/TEST.1999.805761>
[^roggei-1999]: A. Roggei and K. Seshan, "Reduction of probe to pad
    contact resistance: technology development targeted for cost
    effectiveness Pentium II(R) processors testing", *1999 IEEE
    International Symposium on Semiconductor Manufacturing (ISSM)*,
    pp. 217–219. <https://doi.org/10.1109/ISSM.1999.808775>
[^electroglas-1999]: Electroglas, *1999 Annual Report*, "Wafer Probing"
    section, web page; Wayback Machine capture of 2002-05-30.
    <https://web.archive.org/web/20020530031508/http://www.electroglas.com:80/press/pressreleases/reports/1999annual/wafer.htm>
[^expertech-vtr]: Expertech, *VTR7000PLUS Thermal Reactor | Vertical
    Diffusion Furnaces*, product page, accessed 2026-09-13.
    <https://www.exper-tech.com/products/vertical-thermal-reactor>
[^pat-hdp-reactor-amat]: F. C. Redeker, F. Moghadam, H. Hanawa,
    T. Ishikawa, D. Maydan, S. Li, B. Lue, R. J. Steger, M. Wong, Y. Wong
    and A. K. Sinha (Applied Materials), *Symmetric tunable inductively
    coupled HDP-CVD reactor*, US 6,170,428 B1, filed 1996-07-15, granted
    2001-01-09. <https://patents.google.com/patent/US6170428B1/en>
[^amat-ism-2000]: Applied Materials, *Interconnect Systems & Modules*
    (liner/barrier and tungsten CVD systems), product page; Wayback
    Machine capture of 2000-08-15.
    <https://web.archive.org/web/20000815075033/http://www.appliedmaterials.com:80/products/ism_liner.html>
[^novellus-wcvd-2002]: Novellus Systems, *Tungsten Product Solutions*
    (metal CVD), product page; Wayback Machine capture of 2002-02-10.
    <https://web.archive.org/web/20020210183923/http://www.novellus.com:80/products/cvd.asp>
[^entegris-cmc-2022]: Entegris, Inc., *CMC Materials | July 2022*,
    acquisition information page, accessed 2026-09-13.
    <https://www.entegris.com/en/home/brands/cmc-materials-july-2022.html>
[^skw-certs]: SkyWater Technology, *Certifications & Policies*, company
    page, accessed 2026-09-13.
    <https://www.skywatertechnology.com/certifications-policies/>
[^skw-07]: SkyWater Technology, *A Day in the Life of a SkyWater
    Maintenance Technician*, 2023-12-14; caption re-checked 2026-09-13.
    <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
[^epa-ghgrp-subpart-i]: US Environmental Protection Agency, *Electronics
    Manufacturing: Subpart I, Greenhouse Gas Reporting Program*,
    information sheet, December 2024, accessed 2026-09-13.
    <https://www.epa.gov/system/files/documents/2024-04/i_electronics_infosheet_2024.pdf>
[^raw-data-testtile-prop]: SkyWater PDK Authors, *SkyWater 130nm
    Proprietary Manufacturing Test Tile*,
    `docs/sky130-testtile-proprietary/README.rst`,
    `google/skywater-pdk-sky130-raw-data` repository, 2022, retrieved
    2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/README.rst>
[^raw-data-testtile-open]: SkyWater PDK Authors, *SkyWater 130nm Open
    Manufacturing Test Tile*, `docs/sky130-testtile-open/README.rst` and
    images, `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-open/README.rst>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007,
    ISBN 978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
