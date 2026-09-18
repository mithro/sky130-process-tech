(machine-vertical-furnace-oxidation)=
# Vertical batch furnace: oxidation

A vertical oxidation furnace is the batch tool a fab uses to grow
thermal oxide on a hundred or more wafers at once: pad and liner
oxides, gate oxides and the thin oxides of a memory stack. The wafers
lie horizontally in a quartz boat that is raised into a vertical quartz
tube inside a resistance heater, and the tube is filled with dry oxygen,
steam or an inert gas according to the recipe. This page describes the
class in general, lists representative 200 mm-era models, and then says
what SkyWater has published about its own furnaces and which SKY130
steps this reference assigns to the class. The oxidation physics
(Deal–Grove kinetics, the thin-oxide regime, oxide charges) is on the
{ref}`category page <category-oxidation>`; the same furnace platform
used for deposition and for anneals has pages of its own
({ref}`machine-vertical-furnace-lpcvd`,
{ref}`machine-vertical-furnace-anneal`).

| | Vertical batch furnace: oxidation |
|---|---|
| What it does | Grows silicon dioxide on a batch of wafers in dry O₂ or steam; "Most thermal oxidation is performed in furnaces, at temperatures between 800 and 1200 °C".[^wiki-thox] |
| Temperature | A vendor rates the heating element of its vertical reactor for "600-1200° C (Up to 1250° C for > 4 Hours)".[^expertech-vtr] |
| Ambients | Dry O₂; steam made by burning hydrogen in oxygen in an external torch;[^pat-torch-drimer] chlorine from "hydrogen chloride or trichloroethylene" added to the oxidant;[^wiki-thox] nitrogen for loading, purging and annealing.[^pat-vf-insulation-tel] |
| Loading ambient | Load locks "purge the wafers with nitrogen before oxidation to limit the growth of native oxide";[^wiki-thox] a Kokusai load lock holds its oxygen concentration "within the range of 1-100 ppm".[^pat-loadlock-kokusai] |
| Wafer handling | Batch: wafers held "horizontally, above and below each other" and loaded "from below";[^wiki-thox] "150 product, test, and filler wafers" per load on the VTR,[^expertech-vtr] "a batch of up to 150" on TEL's ALPHA-8SE i,[^tel-telindy] "up to 200 wafer batches" on Aviza's AVP-8000.[^aviza-avp] |
| 200 mm era | TEL's Alpha-8 series of "diffusion and LP-CVD furnaces" for "sub-0.18 micron design rules";[^tel-alpha8se] Aviza's AVP/RVP, "smallest footprint systems for 150/200mm wafer processing";[^aviza-vert] the SVG-designed VTR, with "over 1000 VTR systems currently in production use";[^expertech-vtr] ASM's A400, with "more than 1000 reactors shipped".[^asm-a400] |
| SkyWater-listed tool | "Furnaces are all made by Aviza": "wet oxidation to 1150C", "dry oxidation to 1150C"[^skw-01] |
| SKY130 steps | 6 steps; see {ref}`SKY130 steps assigned to this class <machine-vertical-furnace-oxidation-steps>` |

## What the machine class is and how it works

A furnace oxidation is simple in principle: silicon, oxidant and heat.
The machine exists to deliver those three uniformly to every wafer in a
batch of more than a hundred, without particles, metals or an
uncontrolled native oxide, and to do it identically run after run.
Wikipedia summarises why the industry moved from horizontal to vertical
tubes: in a horizontal furnace "convection currents inside the tube"
make the top of each upright wafer oxidise thicker than the bottom,
while a vertical furnace holds the wafers flat with the gas "flowing
from top to bottom, significantly damping any thermal convections";
vertical furnaces "use enclosed cabinets with air filtration systems to
prevent dust from reaching the wafers", and "also allow the use of load
locks".[^wiki-thox]

### Tube, heater and boat

The process tube is a quartz cylinder closed at the top and standing
inside a cylindrical resistance heater with several independently
controlled zones. Below it is the loading area. The boat, a quartz or
silicon-carbide rack with slots for the wafers, stands on a pedestal on
a cap that seals the bottom of the tube; an elevator lifts boat and cap
into the tube. Tokyo Electron's patents of the period describe the
arrangement: a substrate holder "mounted on the top of a cap for opening
and closing the bottom opening (furnace throat)" through a heat
insulation structure, so that the wafers sit in "the uniform heat region
in the furnace".[^pat-vf-insulation-tel] The same patent describes the
cycle: the boat is loaded, the tube is evacuated and "an inert gas,
e.g., nitrogen (N₂) gas, is introduced into the process tube … to purge
the interior", the wafers are heated "quickly to a prescribed processing
temperature", and the process gas is admitted.[^pat-vf-insulation-tel]

The boat is more than a rack. Where a wafer rests on a few small
supports its weight concentrates stress there, and "a surface defect
called a slip generated when the wafer is heat treated" can result;
TEL's boat carries each wafer on an annular projection of a ring so that
the load "is dispersed over the entire projection".[^pat-boat-tel] Production
furnaces add throughput features around the tube: Expertech's VTR, the
design "originated by Silicon Valley Group (SVG)", has "a unique
dual-boat design" in which "one boat is in process while the other loads
or reloads", and a "ULPA-filtered Class 1 loading area".[^expertech-vtr]
Aviza described its AVP/RVP furnaces with a "Dual boat feature, fast
temperature ramping and Advanced Temperature Control (ATC)".[^aviza-vert]

### Loading and the native oxide

A wafer that leaves the pre-clean with a bare, hydrogen-terminated
surface regrows a native oxide in air; Morita et al. showed that "the
coexistence of oxygen and water or moisture is required" for that
growth.[^morita-1990] If the boat then enters a hot tube through room
air, a further uncontrolled oxide grows during loading, underneath the
oxide the recipe intends. Furnaces of the 1990s therefore enclosed the
loading area. TEL's transfer chamber below the furnace circulates
filtered gas, and "it is possible that the transfer chamber 3 is in the
form of a load-lock chamber, and the gas streams are nitrogen gas
streams";[^pat-vf-transfer-tel] a Kokusai
design replaces the load-lock atmosphere with inert gas "with oxygen
concentration less than 1 ppm" and can instead meter oxygen back in to
grow a native oxide of "1-2 atomic layers" before the wafers enter a
reaction tube at "approx. 750° C."[^pat-loadlock-kokusai] The
industry-generic recipe on the {ref}`LVGOX <step-047>` page covers the
other half of the same concern: it limits the queue time between the
pre-gate clean and the furnace.

### Dry, wet and chlorinated oxidation

Dry oxidation needs only purified oxygen through the tube. Wet
oxidation needs clean steam, and a production furnace makes it by
burning hydrogen in oxygen. Wikipedia gives the trade-off between the
two: wet oxidation is preferred for thick oxides "because of the higher
growth rate", but "fast oxidation leaves more dangling bonds", so thick
oxides "are usually grown with a long wet oxidation bracketed by short
dry ones (a dry-wet-dry cycle)".[^wiki-thox] Deal and Grove's
linear–parabolic law fits both oxidants "over a wide range of
temperature (700°–1300°C)".[^deal-1965]

The hydrogen is burnt outside the tube. A 1991 patent explains why. In
the earlier "Pyrogenic Internal Torch" the "H₂ ignition in the O₂
environment as well as the torch are inside the process tube", and the
flame disturbs the "+/-0.5° C. temperature stabilization" that "One
typically tight specification for oxide thickness uniformity requires";
moreover "reduced 'thermal budgets' for circuits and operation of
chambers at less than safe-ignition temperatures for hydrogen have
increased demand for H₂ combustion outside the process chamber". The
patent's external torch "provides pure steam for semiconductor
processing" and is designed to be "free from the possibility of unwanted
explosion due to incomplete hydrogen gas consumption".[^pat-torch-drimer] A later torch from the same inventors
is used "both to produce steam and to perform wet or dry dichlorethylene
(DCE) oxidation".[^pat-torch-persys] Yamaha's variant feeds the steam
from "an external gas burner" into the top of the process tube and,
"Until the flame of hydrogen burnt in the external gas burner becomes
stable", admits a dilute gas such as N₂ "so as to suppress the initial
oxidation".[^pat-torch-yamaha] Chlorine is added because "chlorine can
immobilize sodium by forming sodium chloride"; "Its presence also
increases the rate of oxidation".[^wiki-thox]

### Thin oxides, temperature and the post-oxidation anneal

Gate and tunnel oxides of a few nanometres grow in the regime where
"SiO₂ growth in dry oxygen in the thin regime (<500Å) is faster than the
classic description" and the enhancement "is found to decay
exponentially with thickness";[^massoud-1985] a furnace recipe for such
an oxide is therefore calibrated on the tool, and its thickness depends
on the whole temperature history of the load, ramp and cool-down as well
as the soak. Multi-zone heater control, fast ramping and repeatable
loading are what make that history the same for every wafer position and
every run.

The anneal and cool-down ambient also matters. An oxidation recipe
commonly ends with a short in-tube inert anneal, which a fab uses to
lower the fixed oxide charge (typical practice; category
page).[^txt-01] Razouk and Deal found the price of that step: oxides
"annealed and cooled from any oxidation temperature in nitrogen or
argon exhibit large interface state densities as oxidized", but "after
a low temperature hydrogen anneal these densities are lower than those
of comparable oxygen-cooled oxides".[^razouk-1979] The interface is
therefore finished much later by the hydrogen alloy
({ref}`machine-vertical-furnace-anneal`).

## Representative 200 mm-era models

* **SVG Thermco, later Aviza Technology.** The VTR vertical thermal
  reactor, "originated by Silicon Valley Group (SVG)" and now supported
  by Expertech, with "over 1000 VTR systems currently in production use
  worldwide";[^expertech-vtr] the AVP-8000, "a vertical batch furnace
  with a flexible platform for diffusion, oxidation, and LPCVD
  processes" for "150-200mm wafers", listed by dealers under the Aviza,
  SVG and Thermco names;[^aviza-avp] and the AVP/RVP, which Aviza called
  its "third-generation vertical diffusion furnaces".[^aviza-vert] Aviza
  Technology was "Established in October 2003" and traced "its roots back
  to 1962 to the establishment of Thermco, an Orange, California-based
  supplier of heater element assemblies".[^aviza-company]
* **Tokyo Electron.** The Alpha-8 series, "diffusion and LP-CVD
  furnaces" whose Alpha-8SE generation was aimed at devices "that require
  sub-0.18 micron design rules";[^tel-alpha8se] its ALPHA-8SE i
  successor, "Released in 2018", processes "150/200mm wafers in a batch
  of up to 150" for "oxidation/annealing" and CVD, and TEL notes that
  "more than two decades have passed since the release of
  ALPHA-8SE".[^tel-telindy]
* **ASM International.** The A400, whose "original A400™ vertical
  furnace system has a proven track record of more than 1000 reactors
  shipped" and "over 25 years of maturity", with processes including
  "wet oxidation and anneal processes"; the A400 DUO of 2019 continues it
  for "wafer sizes of 200mm and smaller".[^asm-a400][^asm-vf]
* **Kokusai Electric.** A vertical furnace maker whose patents of the
  period cover load-lock oxygen control[^pat-loadlock-kokusai] and the
  tube and boat hardware described on the
  {ref}`LPCVD page <machine-vertical-furnace-lpcvd>`.

The {ref}`category page <category-oxidation>` lists the same vendors
and the rapid thermal oxidation tools that compete with them.

## At SkyWater

### What SkyWater lists

Under "Furnaces/Diffusion/Pre-Clean", in its "Diffusion, Anneal &
Implant" group, SkyWater's *Facilities & Capabilities* page
states:[^skw-01]

> "Furnaces are all made by Aviza"
>
> "wet oxidation to 1150C"
>
> "dry oxidation to 1150C"

and, among the same furnace lines, "Atmospheric selective
oxidation".[^skw-01] Read term by term: both oxidants are available up to
1150 °C, within the heater range a vendor gives for this class of
reactor.[^expertech-vtr] The entry names the vendor only: no model, no
number of tubes, no batch size, and no statement that the furnaces are
vertical; the step pages' reading of them as vertical rests on the
vendor's 200 mm product line.[^aviza-avp][^aviza-vert] "Atmospheric
selective oxidation" is not expanded, and no step page assigns it to a
SKY130 step. The same group lists the pre-furnace clean benches, "DNS
wet bench industry standard HF/SC1/SC2" and "FSI Mercury industry
standard HF/SC1/SC2 rotational",[^skw-01] which the oxidation step pages
name for their pre-cleans ({ref}`category-strip`).

Aviza Technology was established in October 2003,[^aviza-company] and a
year later it sold the manufacturing rights, intellectual property and
inventory of its "'Thermco' Horizontal Furnace (HTR) product line" to
Tetreon Technologies; the release describes those furnaces as
"originally marketed under the 'Thermco' name and later produced by
Silicon Valley Group and ASML", with "an estimated installed base of
over 8,000 processing tubes".[^tetreon-htr-2004] "Made by Aviza"
therefore describes the vendor as SkyWater names it now; whether any of
the furnaces were built under the earlier SVG or Thermco names, and
whether any is horizontal, is not stated.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` the
listing is **strong** for the vendor and for the wet and dry oxidation
capability: it is a SkyWater statement.[^skw-01] The caveats that apply
to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`. For
this class the weak points are the model and configuration: that the
oxidation tubes are vertical AVP/RVP-class furnaces is inferred from the
vendor's product line, which Aviza's own 2005 page describes in one
short paragraph[^aviza-vert] and a used-equipment listing in slightly
more detail (batch size and processes).[^aviza-avp] Nothing public
says how many oxidation tubes there are or which oxide runs in which
tube.

(machine-vertical-furnace-oxidation-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a vertical
oxidation furnace as the tool or one of two options (identical to the
{ref}`machines index <machines-index>` table):

{ref}`BOX <step-002>`, {ref}`LINOX <step-010>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`, {ref}`IOX45 <step-063>`

How the step pages grade the SkyWater tool for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Furnaces are all made by Aviza" (with the process lines quoted
  above)** — *strong:* {ref}`BOX <step-002>`, {ref}`ISONIT <step-003>`; *inference:* {ref}`LINOX <step-010>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`, {ref}`SAGD <step-048>`, {ref}`GATENIT <step-058>`, {ref}`IOX45 <step-063>`, {ref}`SPNIT <step-076>`, {ref}`ALLY1 <step-096>`, {ref}`ALLY <step-170>`; *strong for existence (batch alternative):* {ref}`FILOX <step-011>`, {ref}`POC <step-059>`, {ref}`SPOX <step-080>`; *weak:* {ref}`RTAI <step-034>`, {ref}`TIPRTAD <step-075>`, {ref}`RTAD <step-088>`, {ref}`RTAD2 <step-092>`, {ref}`LINIT <step-104>`; *excluded on thermal grounds (inference):* {ref}`NTSD <step-167>`
* **"Ag Heatpulse 8808 …" instead** — *weak:* {ref}`LINOX <step-010>`,
  {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`,
  {ref}`LVGOX <step-047>`, {ref}`IOX45 <step-063>`; see
  {ref}`machine-rapid-thermal-processor`.

The furnace row covers all three furnace classes, because SkyWater
lists its furnaces as one group; the oxidation steps are
{ref}`BOX <step-002>`, {ref}`LINOX <step-010>`, {ref}`ONO <step-040>`,
{ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>` and
{ref}`IOX45 <step-063>`. The inferences rest on the listed "wet
oxidation to 1150C" and "dry oxidation to 1150C", which no other listed
tool offers as a batch process.[^skw-01]

## Consumables and facilities

The process gases are described on the
{ref}`process gases <material-process-gases>` page.
The gases and quartzware of oxidation are listed in the
{ref}`materials index <materials-index>` and on the
{ref}`category page <category-oxidation>`; what is specific to the
furnace is summarised here. None of the SkyWater sources describes the
fab's furnace gas supply or exhaust. Quartz and silicon-carbide furnace
ware is described on the
{ref}`hardware consumables and abatement <material-hardware-consumables>`
page.

* **Oxidant and carrier gases.** Oxygen; hydrogen for the steam torch;
  nitrogen for purge and anneal; a chlorine source, HCl or
  trichloroethylene,[^wiki-thox] or DCE delivered through the
  torch.[^pat-torch-persys]
* **Steam torch.** Earlier external torches were "constituted by an
  external, purely-thermal (resistive) ignition element, an H₂/O₂ quartz
  injector, a quartz torch chamber, a water-cooled jacket … a safety
  shield and an electronic controller for safety
  interlocks";[^pat-torch-drimer] the quartz parts and the ignition
  element are the parts that wear.
* **Quartzware and boats.** Process tube, boat, pedestal and insulation
  plates; TEL's heat-insulation structure uses "a plurality of thin heat
  insulation plates" under the boat,[^pat-vf-insulation-tel] and boat
  design is a slip-control measure.[^pat-boat-tel]
* **Heater.** The multi-zone heating element, rated "600-1200° C (Up to
  1250° C for > 4 Hours)" on one vendor's reactor;[^expertech-vtr]
  heater assemblies were Thermco's original business.[^aviza-company]
* **Filler and monitor wafers.** A VTR load is "150 product, test, and
  filler wafers";[^expertech-vtr] filler (dummy) wafers keep the gas
  flow and temperature uniform at the ends of the boat, and monitor
  wafers carry the {ref}`ellipsometry measurement <machine-film-thickness-metrology>`.
* **Loading-area gas and filtration.** Nitrogen for a load lock, and
  filters in the transfer chamber, where TEL specifies PTFE filter
  material "which can reduce the amount of impurities scattered from the
  dust removing filter".[^pat-vf-transfer-tel]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's oxidation temperatures, times
and thicknesses are not public.

* **One class, many oxides.** The six steps span a pad oxide, a trench
  liner, the tunnel and blocking oxides of a SONOS stack, a thick and a
  thin gate oxide and a post-etch oxidation. In a batch fab they share a
  small fleet of tubes; which tube runs which recipe, and whether gate
  oxides have dedicated tubes, is not public.
* **Gate oxides in the thin regime.** The {ref}`GOX100 <step-043>` and
  {ref}`LVGOX <step-047>` pages describe oxides of a few nanometres, where
  growth runs faster than the linear–parabolic law predicts;[^massoud-1985]
  the second gate oxidation also thickens the first (category page). The
  furnace's load-lock ambient and ramp are part of the thickness
  budget.[^pat-loadlock-kokusai]
* **The ONO stack in one furnace.** The {ref}`ONO <step-040>` page cites
  a Cypress patent in which the blocking layer is preferably "formed in
  the same processing tool as is both the charge trapping layer(s) … and
  the tunneling layer … without removing the substrate between
  operations",[^pat-03] and SkyWater lists "LPCVD oxide/nitride/oxide"
  among its furnace processes.[^skw-01] The page therefore spans this
  class and the {ref}`LPCVD class <machine-vertical-furnace-lpcvd>`.
* **Furnace or rapid thermal oxidation.** Five of the six pages offer
  single-wafer rapid thermal oxidation — as an equal option for
  {ref}`LVGOX <step-047>` and {ref}`IOX45 <step-063>` and as the
  alternative for {ref}`LINOX <step-010>`, {ref}`ONO <step-040>` and
  {ref}`GOX100 <step-043>` — and grade the SkyWater Heatpulse for it as
  weak.[^skw-01] In-situ steam generation,
  the single-wafer counterpart of wet oxidation, reacts hydrogen and
  oxygen in the chamber (category page);[^txt-09][^yu-1999] the Heatpulse
  entry lists "NH3, Ar, N2, O2" and no
  hydrogen,[^skw-01] so a steam-based single-wafer oxide at SkyWater is
  not supported by the public list (inference).
* **Nitrided oxides.** SkyWater lists "Nitrided gate oxide" as a special
  module without naming a tool;[^skw-01] the furnace lines list no N₂O
  or NO, the ambients of an oxide grown and nitrided in one
  step.[^lai-1998] The possible routes are on the
  {ref}`plasma nitridation page <machine-plasma-nitridation-chamber>`.
* **Post-oxidation anneal.** The typical recipes on the
  {ref}`GOX100 <step-043>` and {ref}`IOX45 <step-063>` pages end the
  oxidation with an inert anneal in the same tube (industry practice;
  SKY130's recipe is not public); SkyWater's furnace list has "Ar anneal to 1150C" and
  "N2 anneal to 1150C".[^skw-01] The ambient of that anneal and of the
  cool-down affects the interface-state density.[^razouk-1979]

## Related pages

* {ref}`category-oxidation` — oxidation kinetics, oxide quality and the
  six oxidation steps of SKY130.
* {ref}`machine-vertical-furnace-lpcvd` and
  {ref}`machine-vertical-furnace-anneal` — the same Aviza furnace group
  used for deposition, anneals and the alloy.
* {ref}`machine-rapid-thermal-processor` — the single-wafer alternative
  and the Heatpulse entry.
* {ref}`machine-plasma-nitridation-chamber` — nitridation of the thin
  gate oxide.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`category-strip` — the pre-furnace cleans on the listed benches.
* {ref}`material-hardware-consumables` — furnace ware, traps and
  abatement.
* {ref}`material-process-gases` — nitrogen, oxygen, hydrogen, argon,
  helium and the oxidation additives, their grades and SkyWater's listed
  gases.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,257,926 A <patent-gp25202080>` — Fast, safe, pyrogenic external torch assembly (1991)
* {ref}`US 5,633,212 A <patent-gp12697185>` — Pyrogenic wet thermal oxidation of semiconductor wafers (1993)
* {ref}`US 5,551,984 A <patent-gp26377048>` — Vertical heat treatment apparatus with a circulation gas passage (1993)
* {ref}`US 5,735,961 A <patent-gp26456233>` — Semiconductor fabricating apparatus, method for controlling oxygen concentration within load-lock chamber and method for generating native oxide (1995)
* {ref}`US 5,709,543 A <patent-gp17268321>` — Vertical heat treatment apparatus (1995)
* {ref}`US 5,820,367 A <patent-gp17432179>` — Boat for heat treatment (1995)
* {ref}`US 6,179,609 B1 <patent-gp26323689>` — Compact external torch assembly for semiconductor processing (1998)

:::{dropdown} 1 family in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 8,093,128 B2 <patent-gp40072804>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the furnace, oxidation
  and pre-clean entries quoted on this page.[^skw-01]
* Aviza Technology, *Company* page (2005) — the company's 2003 formation
  and Thermco origin.[^aviza-company]
* Aviza Technology, *Vertical Processors* page (2005) — the AVP/RVP
  150/200 mm furnaces.[^aviza-vert]
* Tetreon Technologies, press release on Aviza's site (2004) — the sale
  of the Thermco horizontal furnace line and its installed
  base.[^tetreon-htr-2004]
* Moov, *Aviza / SVG / Thermco AVP 8000* listing — the vendor's 200 mm
  vertical furnace and its batch size.[^aviza-avp]
* Expertech, *VTR7000PLUS Thermal Reactor* — the SVG-designed vertical
  reactor, its load and heater range.[^expertech-vtr]
* Tokyo Electron, *TELINDY Series* page — the ALPHA-8SE i and its
  predecessor.[^tel-telindy]
* ASM International, A400 DUO press release (2019) — the A400 installed
  base and processes.[^asm-a400]
* Shimada (Kokusai Electric), US 5,735,961 — load-lock oxygen control
  and native oxide before loading.[^pat-loadlock-kokusai]

### High-level understanding

* Wikipedia, *Thermal oxidation* — furnace oxidation, vertical versus
  horizontal tubes, dry-wet-dry cycles and chlorine.[^wiki-thox]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — oxidation and
  its equipment.[^txt-01]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — the furnace
  as a fab tool.[^txt-07]
* ASM International, *Vertical furnace* — a vendor overview of batch
  oxidation, diffusion and LPCVD.[^asm-vf]
* Semiconductor Online, *Alpha-8SE* — TEL's description of its 200 mm
  furnace generation.[^tel-alpha8se]

### Deep dive

* Deal and Grove, *J. Appl. Phys.* 1965 — the linear–parabolic
  oxidation law for dry and wet oxidants.[^deal-1965]
* Massoud, Plummer and Irene, *J. Electrochem. Soc.* 1985 — growth-rate
  enhancement of thin dry oxides.[^massoud-1985]
* Razouk and Deal, *J. Electrochem. Soc.* 1979 — interface states
  versus oxidation, anneal and cooling ambients.[^razouk-1979]
* Morita et al., *J. Appl. Phys.* 1990 — what native oxide needs to
  grow.[^morita-1990]
* Green et al., *J. Appl. Phys.* 2001 — review of sub-4 nm SiO₂ and
  oxynitride gate dielectrics.[^green-2001]
* Rozé et al., *J. Appl. Phys.* 2017 — dry furnace oxidation compared
  with dry RTO and ISSG.[^roze-2017]
* Yu et al. (TSMC), *Proc. SPIE* 1999 — in-situ steam generation, the
  single-wafer counterpart of wet furnace oxidation.[^yu-1999]
* Lai et al., *Jpn. J. Appl. Phys.* 1998 — N₂O-nitrided gate oxide and
  N₂O poly reoxidation.[^lai-1998]
* Drimer, Glaser and Rowell, US 5,257,926 — an external pyrogenic torch
  for furnace steam.[^pat-torch-drimer]
* Drimer, Mendelovici and Borivker (Persys), US 6,179,609 — a compact
  torch for steam and DCE oxidation.[^pat-torch-persys]
* Yuuki (Yamaha), US 5,633,212 — external-burner wet oxidation with
  suppression of initial oxidation.[^pat-torch-yamaha]
* Shimazu (Tokyo Electron), US 5,709,543 — boat, cap and heat-insulation
  structure of a vertical furnace.[^pat-vf-insulation-tel]
* Tanahashi (Tokyo Electron), US 5,551,984 — gas circulation and
  filtration in the transfer chamber below the furnace.[^pat-vf-transfer-tel]
* Osawa (Tokyo Electron), US 5,820,367 — ring boat supports against
  slip.[^pat-boat-tel]

## Open questions

* How many oxidation tubes SkyWater runs, which models they are, and
  whether they are vertical are not stated; "Furnaces are all made by
  Aviza" gives the vendor only.[^skw-01]
* What "Atmospheric selective oxidation" denotes, and whether any SKY130
  step uses it, is not stated.
* Whether SKY130's gate and tunnel oxides are grown in a furnace or in the
  single-wafer RTP tool is not public; the step pages grade the furnace as
  the inference and the Heatpulse as weak.
* The model list above is incomplete: it covers the SVG/Aviza, Tokyo
  Electron, ASM and Kokusai furnaces for which a public description was
  found, not every vertical furnace of the period.

<!-- footnotes -->

[^wiki-thox]: Wikipedia, *Thermal oxidation*.
    <https://en.wikipedia.org/wiki/Thermal_oxidation>
[^expertech-vtr]: Expertech, *VTR7000PLUS Thermal Reactor | Vertical
    Diffusion Furnaces*, product page, accessed 2026-09-13.
    <https://www.exper-tech.com/products/vertical-thermal-reactor>
[^pat-torch-drimer]: G. Drimer, A. Glaser and D. M. Rowell, *Fast, safe,
    pyrogenic external torch assembly*, US 5,257,926 A, filed 1991-12-17,
    granted 1993-11-02. <https://patents.google.com/patent/US5257926A/en>
[^pat-vf-insulation-tel]: T. Shimazu (Tokyo Electron), *Vertical heat
    treatment apparatus*, US 5,709,543 A, filed 1996-09-04, granted
    1998-01-20. <https://patents.google.com/patent/US5709543A/en>
[^pat-loadlock-kokusai]: M. Shimada (Kokusai Electric), *Semiconductor
    fabricating apparatus, method for controlling oxygen concentration
    within load-lock chamber and method for generating native oxide*,
    US 5,735,961 A, filed 1996-05-16, granted 1998-04-07.
    <https://patents.google.com/patent/US5735961A/en>
[^tel-telindy]: Tokyo Electron, *Deposition TELINDY Series* (product page
    including the ALPHA-8SE i), accessed 2026-09-13.
    <https://www.tel.com/product/telindy.html>
[^aviza-avp]: Moov used-equipment marketplace, *Aviza / SVG / Thermco AVP
    8000* listing, accessed 2026-08-30; re-checked 2026-09-13.
    <https://moov.co/marketplace/furnaces-diffusion/aviza-svg/aviza-asml-svg-watkinsjohnson-avp-8000>
[^tel-alpha8se]: Semiconductor Online, *Thermal Processing Applications —
    Alpha-8SE* (Tokyo Electron America product description), undated,
    accessed 2026-09-13.
    <https://www.semiconductoronline.com/doc/thermal-processing-applications-alpha-8se-0001>
[^aviza-vert]: Aviza Technology, *Vertical Processors*, product page,
    2005; Wayback Machine capture of 2005-11-08.
    <https://web.archive.org/web/20051108133056/http://www.avizatechnology.com/products/vert.htm>
[^asm-a400]: ASM International, *ASM International N.V. launches A400 DUO
    vertical furnace system*, press release, 2019-11-11; Wayback Machine
    capture of 2024-10-14.
    <https://web.archive.org/web/20241014215529/https://www.asm.com/press-releases/asm-international-nv-launches-a400-duo-vertical-furnace-system-1944469>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; furnace, RTA and pre-clean entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^pat-boat-tel]: T. Osawa (Tokyo Electron), *Boat for heat treatment*,
    US 5,820,367 A, filed 1996-09-18, granted 1998-10-13.
    <https://patents.google.com/patent/US5820367A/en>
[^morita-1990]: M. Morita, T. Ohmi, E. Hasegawa, M. Kawakami and
    M. Ohwada, "Growth of native oxide on a silicon surface", *Journal
    of Applied Physics* **68**(3), 1272–1281 (1990).
    <https://doi.org/10.1063/1.347181>
[^pat-vf-transfer-tel]: T. Tanahashi (Tokyo Electron; Tokyo Electron
    Tohoku), *Vertical heat treatment apparatus with a circulation gas
    passage*, US 5,551,984 A, filed 1994-12-05, granted 1996-09-03.
    <https://patents.google.com/patent/US5551984A/en>
[^deal-1965]: B. E. Deal and A. S. Grove, "General Relationship for the
    Thermal Oxidation of Silicon", *Journal of Applied Physics*
    **36**(12), 3770–3778 (1965). <https://doi.org/10.1063/1.1713945>
[^pat-torch-persys]: G. Drimer, L. Mendelovici and N. Borivker (Persys
    Technology), *Compact external torch assembly for semiconductor
    processing*, US 6,179,609 B1, filed 1999-07-02, granted 2001-01-30.
    <https://patents.google.com/patent/US6179609B1/en>
[^pat-torch-yamaha]: T. Yuuki (Yamaha), *Pyrogenic wet thermal oxidation
    of semiconductor wafers*, US 5,633,212 A, filed 1994-07-22, granted
    1997-05-27. <https://patents.google.com/patent/US5633212A/en>
[^massoud-1985]: H. Z. Massoud, J. D. Plummer and E. A. Irene, "Thermal
    Oxidation of Silicon in Dry Oxygen: Growth-Rate Enhancement in the
    Thin Regime. I. Experimental Results", *Journal of The
    Electrochemical Society* **132**(11), 2685–2693 (1985).
    <https://doi.org/10.1149/1.2113648>
[^razouk-1979]: R. R. Razouk and B. E. Deal, "Dependence of Interface
    State Density on Silicon Thermal Oxidation Process Variables",
    *Journal of The Electrochemical Society* **126**(9), 1573–1581
    (1979). <https://doi.org/10.1149/1.2129333>
[^aviza-company]: Aviza Technology, *Company*, web page, 2005; Wayback
    Machine capture of 2005-11-24.
    <https://web.archive.org/web/20051124224446/http://www.avizatechnology.com/company/index.htm>
[^asm-vf]: ASM International, *Vertical furnace*, product page, accessed
    2026-09-13. <https://www.asm.com/our-technology-products/vertical-furnace>
[^tetreon-htr-2004]: Tetreon Technologies (release hosted by Aviza
    Technology), *Tetreon Technologies Acquires Thermco Horizontal
    Furnaces from Aviza Technology*, Business Wire, 2004-11-08; Wayback
    Machine capture of 2005-03-09.
    <https://web.archive.org/web/20050309110126/http://www.avizatechnology.com:80/news/pressrel/110804.htm>
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
    Shown as in force; estimated expiry 2028-10-22 (estimate from public
    records, not legal advice).
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007, ISBN
    978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^yu-1999]: M.-C. Yu, S.-M. Jang, C. H. Diaz, C. H. Yu, S. C. Sun and
    M. S. Liang (TSMC), "Improvement of ultrathin gate oxide by a novel
    rapid thermal oxidation process with in-situ steam generation",
    *Proc. SPIE* **3881**, Microelectronic Device Technology III, 234
    (1999). <https://doi.org/10.1117/12.360557>
[^lai-1998]: C. S. Lai, T. S. Chao, T. F. Lei, C. L. Lee, T. Y. Huang
    and C. Y. Chang, "Improvement of Reliability of Metal-Oxide
    Semiconductor Field-Effect Transistors with N₂O Nitrided Gate Oxide
    and N₂O Polysilicon Gate Reoxidation", *Japanese Journal of Applied
    Physics* **37**(10R), 5507 (1998).
    <https://doi.org/10.1143/JJAP.37.5507>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^green-2001]: M. L. Green, E. P. Gusev, R. Degraeve and E. L.
    Garfunkel, "Ultrathin (<4 nm) SiO₂ and Si–O–N gate dielectric layers
    for silicon microelectronics: Understanding the processing,
    structure, and physical and electrical limits", *Journal of Applied
    Physics* **90**(5), 2057–2121 (2001).
    <https://doi.org/10.1063/1.1385803>
[^roze-2017]: F. Rozé, O. Gourhant, E. Blanquet, F. Bertin, M. Juhel,
    F. Abbate, C. Pribat and R. Duru, "Oxidation kinetics of Si and
    SiGe by dry rapid thermal oxidation, in-situ steam generation
    oxidation and dry furnace oxidation", *Journal of Applied Physics*
    **121**(24), 245308 (2017). <https://doi.org/10.1063/1.4987040>
