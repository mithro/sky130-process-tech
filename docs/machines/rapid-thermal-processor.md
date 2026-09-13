(machine-rapid-thermal-processor)=
# Rapid thermal processor (RTA, RTO)

A rapid thermal processor heats one wafer at a time with banks of
lamps, taking it to anneal or oxidation temperature in seconds, holding
it there for seconds to minutes and cooling it again, in a controlled
gas ambient. A 130 nm fab uses it wherever a furnace's long thermal
cycle would move dopants too far: implant activation, silicide
formation, and thin oxides and nitridations. This page describes the
class in general, lists representative 200 mm-era models, and then says
what SkyWater has published about its own tool of this class and which
SKY130 steps this reference assigns to it. The anneal physics
(activation, transient enhanced diffusion, silicidation) is on the
{ref}`anneal category page <category-anneal>`, and rapid thermal
oxidation on the {ref}`oxidation category page <category-oxidation>`.

| | Rapid thermal processor |
|---|---|
| What it does | Heats a single wafer "to temperatures exceeding 1,000°C for not more than a few seconds" with "high intensity lamps or lasers", for "dopant activation, thermal oxidation, metal reflow and chemical vapor deposition".[^wiki-rtp] |
| Temperature and time | "Recommended steady-state temperature range: 400 – 1200°C" and "Steady-state duration: 1 – 600 seconds per step" for the Heatpulse 8800;[^ag-8800] Applied Materials described RTP as heating "for a short period of time, usually less than 15 seconds".[^amat-1997] |
| Ramp rate | "up to 100°C per second with Ceramic Shield; up to 150°C per second without" in the 8800 section of the reseller's PDF;[^ag-8108] the reseller's 8800/8808 web page gives "Programmable, 1 – 180°C per second", the same text as the PDF's 8108 section.[^ag-8800][^ag-8108] |
| Heating and measurement | Tungsten-halogen lamps "in 2 banks of 14 lamps each, 1 bank above and the other below the process chamber", "10-zone lamp control", "Pyrometer or thermocouple sensing";[^ag-8800] lamps "disposed in a plurality of light pipes" with a "liquid cooled window" in Applied Materials' design.[^pat-rtp-amat] |
| Uniformity | ±3 °C across an 8-inch wafer at 1150 °C in the PDF's 8800 section, ±5 °C in its 8108 section and on the web page;[^ag-8108][^ag-8800] "at 1150° C. the center to edge temperature difference on a four inch silicon wafer of approximately 5° C. can induce dislocation formation and slip".[^pat-rtp-amat] |
| Wafer handling | Single wafer from cassettes, "approximately 80 wafers per hour (in a null cycle) without flat-finder" on the Heatpulse 8800, with wafer sizes of "5 inches, 6 inches, and 8 inches".[^ag-8800] |
| 200 mm era | AG Associates Heatpulse 8108 and 8800, later sold by STEAG, Mattson and Metron;[^mattson-metron-2002] Applied Materials' RTP Centura (1995) and RTP XE Centura (1997);[^amat-1997] "15 RTP equipment manufacturers" surveyed in 1990.[^roozeboom-1990] |
| SkyWater-listed tool | "Ag Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C"[^skw-01] |
| SKY130 steps | 7 steps, plus 6 where the class is an alternative; see {ref}`SKY130 steps assigned to this class <machine-rapid-thermal-processor-steps>` |

## What the machine class is and how it works

Short-time annealing began with arc lamps, resistance heaters, lasers
and electron beams; Sedgwick classified the regimes by duration and
noted that in the "isothermal" regime of seconds "the dopant can be
activated, and amorphous silicon regrown epitaxially with little dopant
diffusion".[^sedgwick-1983] The production RTP tool settled on
tungsten-halogen lamps. Roozeboom and Parekh's 1990 review covers "the
basic system characteristics, the fundamental physics involved, and the
techniques for temperature measurement and control", and summarises "the
options currently available for 15 RTP equipment
manufacturers".[^roozeboom-1990] Wikipedia names the compromise the class
makes: "To achieve short annealing times and quick throughput, sacrifices
are made in temperature and process uniformity, temperature measurement
and control, and wafer stress".[^wiki-rtp]

### Lamps, chamber and cooling

Two chamber designs dominated the 200 mm era. In the AG Associates
Heatpulse, the wafer sits in a quartz isolation tube between two lamp
banks: "Lamps arranged in 2 banks of 14 lamps each, 1 bank above and the
other below the process chamber", with the "upper and lower lamps … at
right angles to each other for optimization of temperature control" and
"10-zone lamp control"; "To provide cold-wall processing, water is
circulated through the process-chamber walls. The quartz isolation tube
is cooled with nitrogen or compressed air."[^ag-8800] Plasma-Therm, which
now supplies the line, describes "two arrays of tungsten lamps" and rapid
cooling "through a cold-wall type heat exchanger".[^plasmatherm-ag]

In Applied Materials' design, patented by Gronet and Gibbons, "lamps are
disposed in a plurality of light pipes arranged to illuminate and supply
heat to a substrate", "The light pipes are positioned so that the
illumination patterns overlap", and "A liquid cooled window cooperates
with the light pipes to transmit energy to a wafer disposed in an
evacuated chamber".[^pat-rtp-amat] The patent contrasts this with the
"prior art flood type rapid thermal heating apparatus", which "does not
provide adequate spatial control of temperature", and supports the wafer
at its edge on a support that is magnetically rotated.[^pat-rtp-amat] An
earlier Tamarack patent encloses the lamps in "An integrating light pipe,
very preferably a kaleidoscope" to heat the workpiece "from both sides
uniformly and efficiently".[^pat-rtp-tamarack]

### Temperature measurement

The wafer is never in equilibrium with the chamber, so its temperature
must be measured on the wafer itself; Wikipedia describes "in situ
pyrometry to effect real time control".[^wiki-rtp] A pyrometer reads the
wafer's thermal radiation, and the reading depends on the wafer's
emissivity: "a variation in the wafer's surface emissivity can result in
an error in the inferred temperature", and during deposition "the
emissivity is a function of the film type and thickness".[^sorrell-1993]
Chen et al. measured the corrections needed for lightpipe radiation
thermometers on a 200 mm wafer in the NIST RTP test bed, using "test
wafers instrumented with thin-film thermocouples".[^chen-2002-rtp] Patterns
on the wafer matter too: Hebb and Jensen found that "pattern effects are
an important consideration for rapid thermal processes".[^hebb-1996] The
Heatpulse offers "Pyrometer or thermocouple sensing (with DTC option)"
and specifies its "ERP temperature accuracy" "when calibrated against an
instrumented thermocouple wafer (ITC)".[^ag-8800] In Applied Materials'
design "Many pyrometers can be used to sample many areas of the wafers",
and the power to groups of lamps near each pyrometer is controlled
separately.[^pat-rtp-amat]

### Uniformity, stress and slip

A uniformly irradiated wafer loses more heat at its edge, and the
resulting gradient is a mechanical as well as a process problem. Deaton
and Massoud describe how "radiative losses from the edge of silicon
wafers which are heated by uniform irradiation create a radial
temperature gradient" that "induces a stress distribution which is
compressive at the center and tensile towards the edge", largest along
"the slip directions on slip planes".[^deaton-1991] Gronet and Gibbons give
the scale: "at 1150° C. the center to edge temperature difference on a
four inch silicon wafer of approximately 5° C. can induce dislocation
formation and slip".[^pat-rtp-amat] Multi-zone control is the answer;
Schaper et al. demonstrated model-based multivariable control with
"less than ±1°C average nonuniformity during steady state".[^schaper-1994]
Cooling is limited for the same reason: "During cooling wafer
temperatures must be brought down slowly to prevent dislocations and
wafer breakage due to thermal shock".[^wiki-rtp]

### Ambient control

Because each wafer is heated alone in a small chamber, the ambient can be
switched between steps, and its purity is critical for metals. Plasma-Therm
explains that "During metal RTD steps, any oxygen present in the chamber
may oxidize the metal", and offers for the Heatpulse "a nitrogen (N₂)
curtain, which reduces the introduction of contaminants and oxygen into the
processing chamber" and "an in-situ oxygen monitor" that detects "oxygen
levels as low as 10 parts per million (PPM)".[^plasmatherm-ag]

### What the class does

* **Implant anneals.** The first listed Heatpulse application after
  dielectric growth is "Implant annealing".[^ag-8800] RTA limits the
  diffusion driven by the implant damage, the "transient enhanced
  diffusion (TED) during annealing which arises from the excess
  interstitials generated by the implant" (category page).[^stolk-1997]
* **Silicide formation.** "Silicide formation and annealing" and "Contact
  alloying" are listed Heatpulse applications,[^ag-8800] and its
  specification allows "no more than 1.5 percent increase to uniformity
  during the first anneal at 650 – 700°C" of a titanium silicidation.[^ag-8108]
* **Rapid thermal oxidation and nitridation.** Nulman, Krusius and Gat
  grew 40–130 Å oxides "in a controlled oxygen ambient with the heating
  provided by tungsten-halogen lamps" at 1150 °C in 5–30 s, with
  "characteristics equal to or better than furnace grown
  oxides";[^nulman-1985] Hori et al. prepared "reoxidized nitrided oxide
  films" entirely by rapid thermal processing;[^hori-1989] Hwang et al.
  showed that oxynitrides grown by RTP in N₂O "show excellent diffusion
  barrier properties" to boron.[^hwang-1991] In 1997 Applied Materials
  added a nitric oxide process that "incorporates nitrogen into the gate
  oxide with a reduced thermal budget" compared with "traditional
  batch-type furnaces".[^amat-1997]
* **In-situ steam generation and deposition.** A reduced-pressure chamber
  can react hydrogen and oxygen at the wafer to grow oxide in "in-situ
  generated steam" (category page);[^txt-09][^yu-1999] a
  hot-wall single-wafer module can deposit nitride by LPCVD.[^teasdale-2001]
  Neither needs to be available on a given tool.

## Representative 200 mm-era models

* **AG Associates, then STEAG, Mattson and Metron.** The Heatpulse 4100,
  8108 and 8800 families, whose reseller documentation gives the
  specifications quoted on this page.[^ag-8800][^ag-8108] In 2002 Mattson
  Technology sold "the AG Associates rapid thermal processing (RTP) product
  line, which Mattson obtained through its acquisition last year of the
  semiconductor division of STEAG Electronic Systems AG", to Metron
  Technology, which took "exclusive ownership of the 4000 and 8000 series
  RTP product line"; Mattson kept its "2000 and 3000 series RTP
  products".[^mattson-metron-2002] Plasma-Therm now offers "the AG Heatpulse
  8800/8108 RTP line (formerly of OEM Group)".[^plasmatherm-ag]
* **Applied Materials.** The RTP Centura, with which the company "entered
  the fast-growing RTP market in 1995", and the RTP XE Centura, "its first
  major system enhancement", launched in 1997.[^amat-1997] The lamp and
  light-pipe design is the Gronet and Gibbons patent.[^pat-rtp-amat] Its
  April 1997 RTP patent suit named AST Elektronik (spelled "AST
  Electronik" in the report) and AG Associates.[^amat-1997]
* **Others.** Roozeboom and Parekh's review lists fifteen manufacturers of
  1990,[^roozeboom-1990] and the {ref}`anneal category page
  <category-anneal>` names the Kokusai and TEL tools of the 130 nm era.

## At SkyWater

### What SkyWater lists

Under "RTA", in its "Diffusion, Anneal & Implant" group, SkyWater's
*Facilities & Capabilities* page lists one tool:[^skw-01]

> "Ag Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C"

Read term by term: an AG Associates Heatpulse, model 8808, with ammonia,
argon, nitrogen and oxygen, to 1200 °C. There is no hydrogen or forming
gas, no N₂O or NO, and no ramp rate or wafer size. "8808" does not appear
in the reseller's specification PDF, which covers the 4100, 8108, 8800
and 8800i; the reseller's web page treats "Heatpulse 8800 8808" as one
product, and its "400 – 1200°C" range matches SkyWater's "up to
1200C".[^ag-8800][^ag-8108] The page also lists the special modules
"Ti and Co Silicide" and "Nitrided gate oxide" without naming a
tool.[^skw-01]

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` this
listing is **strong**: it is a SkyWater statement.[^skw-01] The caveats
that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`. For
this class the listing is specific about the model family but the
specifications behind it are not SkyWater's: the ramp rates, uniformity
and throughput quoted for the 8800 come from a reseller, whose web page
repeats the 8108 figures of its own PDF,[^ag-8800][^ag-8108] and none of
them describes SkyWater's configuration. It is also the only rapid thermal
tool listed, so every RTA step page assigns its anneal to it by
elimination, as an inference.

(machine-rapid-thermal-processor-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a rapid thermal
processor as the tool or one of two options (identical to the
{ref}`machines index <machines-index>` table):

{ref}`RTAI <step-034>`, {ref}`LVGOX <step-047>`, {ref}`IOX45 <step-063>`, {ref}`TIPRTAD <step-075>`, {ref}`RTAD <step-088>`, {ref}`RTAD2 <step-092>`, {ref}`CSIL <step-098>`; *alternative:* {ref}`LINOX <step-010>`, {ref}`FILOX <step-011>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`ALLY1 <step-096>`, {ref}`ALLY <step-170>`

How the step pages grade the SkyWater tool for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Ag Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C"** — *inference:* {ref}`RTAI <step-034>`, {ref}`TIPRTAD <step-075>`, {ref}`RTAD <step-088>`, {ref}`RTAD2 <step-092>`, {ref}`CSIL <step-098>`; *weak:* {ref}`LINOX <step-010>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`, {ref}`IOX45 <step-063>`, {ref}`ALLY1 <step-096>`, {ref}`ALLY <step-170>`
* **The Aviza furnaces instead** — *inference:* {ref}`LINOX <step-010>`,
  {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`,
  {ref}`LVGOX <step-047>`, {ref}`IOX45 <step-063>`,
  {ref}`ALLY1 <step-096>`, {ref}`ALLY <step-170>`; *strong for existence
  (batch alternative):* {ref}`FILOX <step-011>`; *weak:*
  {ref}`RTAI <step-034>`, {ref}`TIPRTAD <step-075>`,
  {ref}`RTAD <step-088>`, {ref}`RTAD2 <step-092>`; see
  {ref}`machine-vertical-furnace-oxidation` and
  {ref}`machine-vertical-furnace-anneal`.
* **Special modules "Nitrided gate oxide", "Ti and Co Silicide", "W plug
  dual damascene"** — *inference for use in SKY130 (nitrided oxide):* {ref}`LVGOX <step-047>`, {ref}`IOX45 <step-063>`; *strong for the capability (silicide, W plug):* {ref}`CSIL <step-098>`, {ref}`WDEP <step-099>`

The inferences for the anneals rest on the Heatpulse being the only RTA
on the list, with the inert ambients and temperature an activation
anneal needs; the weak grades for the oxidations reflect that nothing
public says whether those oxides are grown in a furnace or in the RTP
chamber, and for the alloys that the entry lists no hydrogen.[^skw-01]
The {ref}`LVGOX <step-047>` and {ref}`IOX45 <step-063>` pages give the
furnace and the RTP tool as equal options in "Machines typically used"
but grade the Heatpulse as weak.

## Consumables and facilities

The gases are listed in the {ref}`materials index <materials-index>`;
what is specific to a lamp-heated RTP tool is summarised here. None of
the SkyWater sources describes the fab's RTP facilities.

* **Process gases.** SkyWater's entry lists NH₃, Ar, N₂ and O₂;[^skw-01] the
  Heatpulse gas box has mass-flow-controlled lines,[^ag-8800] and an
  optional nitrogen curtain uses "a dedicated mass flow
  controller".[^plasmatherm-ag]
* **Lamps and quartz.** Tungsten-halogen lamps and the quartz isolation
  tube;[^ag-8800] the reseller's spare-parts and service list for the AG
  Associates tools reads "Quartzware, Equipe PRI
  Robot/Controller/Pre-Aligner, Pyrometer,Chambers,PCBs".[^ag-8800]
* **Cooling.** Water "circulated through the process-chamber walls";[^ag-8800]
  "Tube Cooling CDA or Utility N2" at a minimum of "35 SCFM" and cooling
  water at a typical "4.0 GPM" for the 8800.[^ag-8108]
* **Exhaust.** "Gas Box Exhaust", "Cooling Exhaust", "Scavenger Hood
  Exhaust" and a "Process Gas Exhaust (Scrubber)" connection for the
  8800.[^ag-8108]
* **Calibration wafers.** Instrumented thermocouple wafers for the
  temperature calibration the specifications assume,[^ag-8800] and monitor
  wafers for sheet resistance or oxide thickness after each qualification.

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's anneal temperatures and times are
not public.

* **Activation after each implant module.** The pre-gate anneal
  ({ref}`RTAI <step-034>`), the tip anneal ({ref}`TIPRTAD <step-075>`) and
  the two source/drain anneals ({ref}`RTAD <step-088>`,
  {ref}`RTAD2 <step-092>`) are assigned to the Heatpulse as inferences.
  Each later anneal adds to the diffusion of every earlier implant, which
  is why they are short;[^stolk-1997] the Heatpulse's "1 – 600 seconds per
  step" and programmable ramps cover soak anneals of that
  kind.[^ag-8800]
* **Silicide in oxygen-free ambient.** The {ref}`CSIL <step-098>` page
  assigns contact silicidation to the Heatpulse and reads the metal from
  the PDK numbers; SkyWater lists "Ti and Co Silicide" as a special
  module.[^skw-01] Oxygen in the chamber oxidises the metal before it
  reacts,[^plasmatherm-ag] so nitrogen or argon purity and the load-door
  curtain matter more than for an implant anneal.
* **Ammonia and the nitrided oxide.** The NH₃ line is the only
  nitriding gas on the Heatpulse entry, and the {ref}`LVGOX <step-047>`
  page calls it "the one public hint" of how the "Nitrided gate oxide"
  module might be run. Heating an oxide in ammonia converts its surface
  "directly to silicon nitride or oxynitride", with graded films "At
  temperatures above 900°C",[^ito-1980] and rapid reoxidation of a nitrided
  oxide improves its charge trapping "by the reducing of hydrogen
  concentration".[^hori-1989] Whether SKY130
  uses this, a plasma nitridation or no nitridation is not public
  ({ref}`machine-plasma-nitridation-chamber`).
* **No hydrogen, no steam.** The entry lists no H₂, so in-situ steam
  generation and forming-gas anneals are not supported by the public
  list; the alloy steps are assigned to the furnaces for that reason.[^skw-01]
* **Slip at high temperature.** Edge-to-centre gradients at
  1150 °C can induce slip,[^pat-rtp-amat] and slip generation was
  "frequently observed in wafers processed above 1050°C" in a single-wafer
  furnace study of 200 mm wafers.[^yoo-2002] SkyWater's entry stops at
  "1200C";[^skw-01] how close SKY130's anneals come to the slip regime is
  not public.

## Related pages

* {ref}`category-anneal` — activation, TED, silicidation and the seven
  thermal steps of SKY130.
* {ref}`category-oxidation` — rapid thermal oxidation and ISSG against
  the furnace.
* {ref}`machine-vertical-furnace-oxidation` and
  {ref}`machine-vertical-furnace-anneal` — the batch alternatives.
* {ref}`machine-plasma-nitridation-chamber` — the plasma route to a
  nitrided gate oxide.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`category-test` — the sheet-resistance and electrical monitors of
  the anneals.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the Heatpulse entry
  and the special modules quoted on this page.[^skw-01]
* SemiStar, *AG Associates Heatpulse 8800 / 8808* — the reseller's
  description and applications, with a specification that repeats the
  PDF's 8108 section.[^ag-8800]
* SemiStar, *Heatpulse 4100 / 8108 / 8800 / 8800i Specifications* — the
  reseller PDF's per-model specifications and facilities.[^ag-8108]
* Plasma-Therm, *Product Spotlight: AG Heatpulse 8800 / 8108 RTP* — the
  current supplier's description and options.[^plasmatherm-ag]
* Mattson Technology and Metron Technology, press release (2002) — the
  ownership of the AG Associates product line.[^mattson-metron-2002]
* Applied Materials, *1997 Annual Report* — the RTP Centura, RTP XE
  Centura and the nitric oxide process.[^amat-1997]
* Gronet and Gibbons (Applied Materials), US 5,155,336 — the light-pipe
  lamphead, multi-pyrometer control and slip.[^pat-rtp-amat]

### High-level understanding

* Wikipedia, *Rapid thermal processing* — the class, its uses and its
  compromises.[^wiki-rtp]
* Fair (ed.), *Rapid Thermal Processing: Science and Technology* — the
  standard book on the technique.[^txt-10]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — annealing,
  diffusion and RTP in context.[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — RTP in
  deep-submicron flows.[^txt-05]

### Deep dive

* Roozeboom and Parekh, *JVST B* 1990 — RTP systems and temperature
  control, with fifteen equipment makers.[^roozeboom-1990]
* Sedgwick, *J. Electrochem. Soc.* 1983 — short-time annealing regimes and
  energy sources.[^sedgwick-1983]
* Nulman, Krusius and Gat, *IEEE EDL* 1985 — rapid thermal oxidation of
  thin gate dielectrics.[^nulman-1985]
* Hori, Iwasaki and Tsuji, *IEEE TED* 1989 — reoxidised nitrided oxides
  made by RTP.[^hori-1989]
* Hwang et al., *Appl. Phys. Lett.* 1991 — RTP N₂O oxynitride as a boron
  barrier.[^hwang-1991]
* Ito, Nozaki and Ishikawa, *J. Electrochem. Soc.* 1980 — thermal
  nitridation of oxide in ammonia.[^ito-1980]
* Sorrell and Gyurcsik, *IEEE TSM* 1993 — emissivity correction in
  pyrometer control.[^sorrell-1993]
* Chen et al., RTP 2002 — emissivity effects on lightpipe thermometry at
  NIST.[^chen-2002-rtp]
* Hebb and Jensen, *J. Electrochem. Soc.* 1996 — pattern effects on
  temperature uniformity.[^hebb-1996]
* Schaper et al., *J. Electrochem. Soc.* 1994 — modelling and multizone
  control of RTP systems.[^schaper-1994]
* Deaton and Massoud, *J. Appl. Phys.* 1991 — thermal stress in rapid
  thermal oxidation.[^deaton-1991]
* Yoo et al., *Jpn. J. Appl. Phys.* 2002 — slip in 200 mm and 300 mm
  wafers during high-temperature single-wafer processing.[^yoo-2002]
* Stolk et al., *J. Appl. Phys.* 1997 — transient enhanced diffusion, the
  reason for short anneals.[^stolk-1997]
* Yu et al. (TSMC), *Proc. SPIE* 1999 — in-situ steam generation for
  ultrathin gate oxide.[^yu-1999]
* Teasdale et al., *Electrochem. Solid-State Lett.* 2001 — single-wafer
  rapid thermal LPCVD nitride.[^teasdale-2001]
* Sheets (Tamarack Scientific), US 4,649,261 — an early integrating
  light-pipe heater.[^pat-rtp-tamarack]

## Open questions

* Whether SkyWater's "Ag Heatpulse 8808" differs from the 8800, and its
  ramp rate, uniformity and wafer handling, are not stated; the reseller's
  web page for the "8800 8808" repeats the PDF's 8108 specifications, not
  its 8800 ones.[^ag-8800][^ag-8108]
* Whether SKY130's thin gate oxide and post-gate-etch oxidation run on the
  Heatpulse or in a furnace, and whether the NH₃ line is used for gate-oxide
  nitridation, are not public.
* How many Heatpulse chambers SkyWater runs, and whether silicide and
  implant anneals share a chamber, is not stated.
* The model list above is incomplete: it covers the AG Associates and
  Applied Materials tools for which a public description was found, not
  every RTP tool of the period; AST Elektronik's tools and Mattson's own
  2000 and 3000 series are named but not described.

<!-- footnotes -->

[^wiki-rtp]: Wikipedia, *Rapid thermal processing*.
    <https://en.wikipedia.org/wiki/Rapid_thermal_processing>
[^ag-8800]: SemiStar Corp., *AG Associates Heatpulse 8800 / 8808 Rapid
    Thermal Processing* (reseller specification page), accessed
    2026-08-30; re-checked 2026-09-13.
    <https://www.semistarcorp.com/product/ag-associates-heatpulse-8800-8808/>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report*.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^ag-8108]: SemiStar Corp., *AG Associates Heatpulse 4100 / 8108 / 8800
    / 8800i Specifications* (reseller PDF; operating specifications and
    facilities for each model), accessed 2026-08-30; re-checked
    2026-09-13.
    <https://www.semistarcorp.com/wp-content/uploads/2025/12/AG-Associates-Heatpulse-4100-8108-8800-8800i-Specifications-Rapid-Thermal-Processor.pdf>
[^pat-rtp-amat]: C. M. Gronet and J. F. Gibbons (Applied Materials),
    *Rapid thermal heating apparatus and method*, US 5,155,336 A,
    granted 1992-10-13.
    <https://patents.google.com/patent/US5155336A/en>
[^mattson-metron-2002]: Mattson Technology, Inc. and Metron Technology
    N.V., *Mattson Technology Inc. and Metron Technology N.V. Announce the
    Sale of Mattson's AG Associates RTP Product Line to Metron*, press
    release, 2002-02-27; Wayback Machine capture of 2003-07-13.
    <https://web.archive.org/web/20030713065644/http://mattson.com/news/pr020227.html>
[^roozeboom-1990]: F. Roozeboom and N. Parekh, "Rapid thermal processing
    systems: A review with emphasis on temperature control", *Journal of
    Vacuum Science & Technology B* **8**(6), 1249–1259 (1990).
    <https://doi.org/10.1116/1.584902>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; RTA entry and special modules re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sedgwick-1983]: T. O. Sedgwick, "Short Time Annealing", *Journal of
    The Electrochemical Society* **130**(2), 484–493 (1983).
    <https://doi.org/10.1149/1.2119736>
[^plasmatherm-ag]: Plasma-Therm, *Product Spotlight: AG Heatpulse 8800 /
    8108 RTP*, blog post, 2021-09-09.
    <https://blog.plasmatherm.com/product-spotlight-ag-heatpulse-8800-8108-rtp>
[^pat-rtp-tamarack]: R. E. Sheets (Tamarack Scientific), *Apparatus for
    heating semiconductor wafers in order to achieve annealing, silicide
    formation, reflow of glass passivation layers, etc.*, US 4,649,261
    A, granted 1987-03-10.
    <https://patents.google.com/patent/US4649261A/en>
[^sorrell-1993]: F. Y. Sorrell and R. S. Gyurcsik, "Model-based
    emissivity correction in pyrometer temperature control of rapid
    thermal processing systems", *IEEE Transactions on Semiconductor
    Manufacturing* **6**(3), 273–276 (1993).
    <https://doi.org/10.1109/66.238178>
[^chen-2002-rtp]: D. Chen, D. DeWitt, B. Tsai, K. Kreider and W. Kimes,
    "Effects of wafer emissivity on rapid thermal processing
    temperature measurement", *Proc. 10th IEEE International Conference
    on Advanced Thermal Processing of Semiconductors (RTP 2002)*,
    pp. 59–67. <https://doi.org/10.1109/RTP.2002.1039440>
[^hebb-1996]: J. P. Hebb and K. F. Jensen, "The Effect of Multilayer
    Patterns on Temperature Uniformity during Rapid Thermal Processing",
    *Journal of The Electrochemical Society* **143**(3), 1142–1151
    (1996). <https://doi.org/10.1149/1.1836598>
[^deaton-1991]: R. Deaton and H. Z. Massoud, "Effect of thermally induced
    stresses on the rapid-thermal oxidation of silicon", *Journal of
    Applied Physics* **70**(7), 3588–3592 (1991).
    <https://doi.org/10.1063/1.349254>
[^schaper-1994]: C. D. Schaper, M. M. Moslehi, K. C. Saraswat and
    T. Kailath, "Modeling, Identification, and Control of Rapid Thermal
    Processing Systems", *Journal of The Electrochemical Society*
    **141**(11), 3200–3209 (1994). <https://doi.org/10.1149/1.2059302>
[^stolk-1997]: P. A. Stolk, H.-J. Gossmann, D. J. Eaglesham, D. C.
    Jacobson, C. S. Rafferty, G. H. Gilmer, M. Jaraíz, J. M. Poate, H.
    S. Luftman and T. E. Haynes, "Physical mechanisms of transient
    enhanced dopant diffusion in ion-implanted silicon", *Journal of
    Applied Physics* **81**(9), 6031–6050 (1997).
    <https://doi.org/10.1063/1.364452>
[^nulman-1985]: J. Nulman, J. P. Krusius and A. Gat, "Rapid thermal
    processing of thin gate dielectrics. Oxidation of silicon", *IEEE
    Electron Device Letters* **6**(5), 205–207 (1985).
    <https://doi.org/10.1109/EDL.1985.26099>
[^hori-1989]: T. Hori, H. Iwasaki and K. Tsuji, "Electrical and physical
    properties of ultrathin reoxidized nitrided oxides prepared by rapid
    thermal processing", *IEEE Transactions on Electron Devices*
    **36**(2), 340–350 (1989). <https://doi.org/10.1109/16.19935>
[^hwang-1991]: H. Hwang, W. Ting, D.-L. Kwong and J. Lee, "A physical
    model for boron penetration through an oxynitride gate dielectric
    prepared by rapid thermal processing in N₂O", *Applied Physics
    Letters* **59**(13), 1581–1582 (1991).
    <https://doi.org/10.1063/1.106290>
[^yu-1999]: M.-C. Yu, S.-M. Jang, C. H. Diaz, C. H. Yu, S. C. Sun and
    M. S. Liang (TSMC), "Improvement of ultrathin gate oxide by a novel
    rapid thermal oxidation process with in-situ steam generation",
    *Proc. SPIE* **3881**, Microelectronic Device Technology III, 234
    (1999). <https://doi.org/10.1117/12.360557>
[^teasdale-2001]: D. Teasdale, Y. Senzaki, R. Herring, G. Hoeye,
    L. Page and P. Schubert, "LPCVD of Silicon Nitride from
    Dichlorosilane and Ammonia by Single Wafer Rapid Thermal
    Processing", *Electrochemical and Solid-State Letters* **4**(5),
    F11 (2001). <https://doi.org/10.1149/1.1359056>
[^ito-1980]: T. Ito, T. Nozaki and H. Ishikawa, "Direct Thermal
    Nitridation of Silicon Dioxide Films in Anhydrous Ammonia Gas",
    *Journal of The Electrochemical Society* **127**(9), 2053–2057
    (1980). <https://doi.org/10.1149/1.2130065>
[^yoo-2002]: W. S. Yoo, T. Fukada, I. Yokoyama, K. Kang and
    N. Takahashi, "Thermal Behavior of Large-Diameter Silicon Wafers
    during High-Temperature Rapid Thermal Processing in Single Wafer
    Furnace", *Japanese Journal of Applied Physics* **41**(7A),
    4442–4449 (2002). <https://doi.org/10.1143/JJAP.41.4442>
[^txt-10]: R. B. Fair (ed.), *Rapid Thermal Processing: Science and
    Technology*, Academic Press, 1993, ISBN 978-0-12-247690-7.
    <https://openlibrary.org/isbn/9780122476907>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007, ISBN
    978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
