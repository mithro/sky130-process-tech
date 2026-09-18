(machine-wet-bench)=
# Wet bench and spray processor

A wet bench is the batch tool a fab uses to clean, etch and strip wafers
in liquid chemicals: a line of tanks — sulphuric–peroxide, the RCA
cleans, dilute HF and buffered oxide etch, hot phosphoric acid —
through which a robot carries cassettes or bare wafer batches, ending
in a rinse and a dryer. A spray processor does the same chemistry in a
closed chamber, spinning a batch of wafers in a rotor while nozzles
spray the liquids onto them. Between them these tools run the
pre-furnace cleans, the nitride strip, the wet oxide etches and the
cleans that follow most strips and etches. This page describes the
class in general, lists representative 200 mm-era models, and then says
what SkyWater has published about its own tools of this class and which
SKY130 steps this reference assigns to it. The chemistry of wet
cleaning and etching is on the {ref}`strip <category-strip>` and
{ref}`etch <category-etch>` category pages.

| | Wet bench and spray processor |
|---|---|
| What it does | Batch wet cleaning, etching and stripping. The RCA clean, "a standard set of wafer cleaning steps which need to be performed before high-temperature processing steps", is its core sequence;[^wiki-rca] Kern traces its implementation "from simple immersion to centrifugal spraying, megasonic techniques, and enclosed system processing".[^kern-1990] |
| Chemistries | SPM ("A typical mixture is 3 parts of concentrated sulfuric acid and 1 part of 30 wt. % hydrogen peroxide");[^wiki-piranha] SC-1 and SC-2 "at 75 or 80 °C";[^wiki-rca] HF and BOE (6:1 BOE etches thermal oxide "at approximately 2 nanometres per second at 25 degrees Celsius");[^wiki-boe] hot phosphoric acid; solvents. |
| Hot phosphoric bath | "Refluxed boiling phosphoric acid at 180°C" etches nitride at 100 Å/min against 0–25 Å/min for deposited oxide;[^vgh-1967] water spiking and partial bath replacement keep the selectivity stable over the bath's life.[^liu-2007] |
| Wafer handling | Immersion benches move batches between tanks — SCREEN's WS-820C "for 200 mm wafers with carrier transfer processing" or WS-820L "with carrierless transfer processing", with "up to 13 baths";[^screen-ws820] a centrifugal spray processor holds cassettes "in a rotor within the process chamber" facing spray manifolds.[^pat-spray-semitool] |
| Drying | Spin or IPA-vapour drying — SkyWater lists "spin or IPA dry" on its Akrion bench;[^skw-01] Kern noted "Improvements in wafer drying by use of isopropanol vapor";[^kern-1990] Marangoni drying was published as "A new extremely clean drying process".[^leenaars-1990] |
| 200 mm era | Akrion GAMA (150–300 mm)[^akrion-gama-series] and E200 benches;[^sst-akrion-scp-2007] SCREEN (DNS) WS-820 wet stations;[^screen-ws820] the FSI (now TEL) MERCURY batch spray system for "75mm – 200mm wafers", with "over 1,000 systems installed".[^tel-mercury-2018] |
| SkyWater-listed tool | "Akrion Gamma Batch Wet Bench" ("Sulfuric, SC1, phosphoric, BOE, spin or IPA dry"), "Batch Rotational" ("EKS265, EKC270 solvents, CO2 injected DI"); under "Pre-cleaning", "DNS wet bench industry standard HF/SC1/SC2" ("dilute HF-last with IPA dry") and "FSI Mercury industry standard HF/SC1/SC2 rotational"[^skw-01] |
| SKY130 steps | 4 steps, plus 36 where it runs a clean or strip; see {ref}`SKY130 steps assigned to this class <machine-wet-bench-steps>` |

## What the machine class is and how it works

Wet processing removes films and contaminants by dissolving them, so it
is isotropic and can be very selective, and it cleans without the
damage of a plasma. Kern's review of 1990 records that wafer-cleaning
chemistry "has remained essentially unchanged in the past 25 years and
is based on hot alkaline and acidic hydrogen peroxide solutions", while
the equipment changed around it.[^kern-1990] What makes a machine a
*wet bench* or *spray processor* is the engineering of that equipment:
chemical baths or spray delivery held at controlled concentration and
temperature, transfer between chemicals without contamination, rinsing,
and a dry that leaves no watermarks or particles. Kern's handbook
chapter surveys the whole field.[^kern-handbook]

### Immersion benches

An automated bench is a row of process tanks, rinse tanks and a dryer
served by robots. SCREEN's WS-series stations can be configured "freely,
depending on the application", with "up to 13 baths" and "up to six
transfer robots", "strict chemical management" and "clean drying
units".[^screen-ws820] Akrion describes its GAMA series as a "Batch
immersion process solution for all FEOL and BEOL semiconductor
applications" with "Concentration control and dilute
chemistry";[^akrion-gama-series] a GAMA bench at a Canadian research
centre offers "Dry-in/dry-out automated SMIF pod input/output
operation", "Real time particle monitoring in chemical tanks" and "Real
time chemical analysis and concentration adjustments".[^akrion-gama]
Akrion's E200 bench, as described in 2007, offered configurations "for RCA cleans,
nitride etch, and photoresist strip applications", with rinse tanks
"designed for DI water savings" and dryers that allow "rinsing and
drying in one tank in less than 10 minutes as well as chemical
injection for surface conversion and critical etch in 'true' HF Last
processes".[^sst-akrion-scp-2007] A university bench shows the same
class at small scale: a "Semi-automated wet bench for etching silicon
nitride … using 155C phosphoric acid", whose "baths can hold up to 25
wafers".[^snf-nitride-wet]

### Spray processors

A centrifugal spray processor puts the batch in a closed chamber
instead of moving it between tanks. In a Semitool patent, wafers "are
contained within cassettes … loaded into a rotor" driven by a motor
behind the chamber, and arrays of spray nozzles "are adapted to spray
fluids towards the rotor"; the patent spreads the flow over more,
smaller nozzles "to reduce consumption of liquid process
chemicals".[^pat-spray-semitool] Tokyo Electron, which later took over
FSI's MERCURY line, describes its batch spray systems as tools that
replace "dated ashers, wet bench stations and peripheral rinsing/drying
equipment with a single tool that etches, strips and cleans in one safe,
space-conscious footprint".[^tel-mercury-2018]

### Chemistry control

Wet etch rates depend on concentration and temperature, and baths drift
as they work. In dilute HF, Kikuyama et al. showed that conductivity
"can be used to monitor the etching rate … very accurately when
the etching rate is relatively slow (around 1 Å/min)".[^kikuyama-1994]
Buffering HF with NH₄F gives "a more stable pH; thus, more stable
concentrations of HF and HF₂⁻, and a more stable etch rate".[^wiki-boe]
Nitride also etches in HF, at a rate Deckert found "linear in both [HF]
and [HF₂⁻], but independent of [F⁻]",[^deckert-1978] and Knotter and
Denteneer's mechanism explains "etch selectivity between these two
materials".[^knotter-2001] In hot phosphoric acid,
van Gelder and Hauser found that "An increase in water content increases
the etch rate of silicon nitride and decreases the etch rate of silicon
dioxide", and used a refluxed boiling bath to hold the water
content;[^vgh-1967] in production, Liu et al. controlled it with "a
water concentration monitor and a water spiking apparatus", replaced
part of the bath after each lot to reduce dissolved silicon, and added
sulphuric acid to shorten conditioning.[^liu-2007] Room-temperature
cleaning sequences have been developed to cut the chemical load of the
hot RCA steps: Ohmi's five-step clean reduced chemical and ultrapure
water use to "less than 1% and 5%, respectively".[^ohmi-1996]

### Rinsing, drying and static charge

The last steps decide whether a clean wafer stays clean. Kern recorded
in 1990 that "Improvements in wafer drying by use of isopropanol vapor
or by 'slow-pull' out of hot deionized water are being
investigated";[^kern-1990] Leenaars, Huethorst and van Oekel published
Marangoni drying the same year as "A new extremely clean drying
process".[^leenaars-1990] Drying also affects corrosion: Wai and Ling traced corrosion of Al–Cu lines to
moisture left after a wet polymer clean and prevented it by lengthening
"isopropyl-alcohol (IPA) purge time by 10 secs and wafers lift up time
by 18 secs" in the Marangoni step.[^wai-2017] Rinse water can also leave electrostatic
charge: an MKS Instruments patent dissolves CO₂ in DI water for wet
cleaning "while preventing or reducing damage created by electrostatic
charge", because "The dissolved CO2 reduces the
resistivity of the DI water to a level that prevents surface
charging".[^pat-dico2-mks]

### Solvent strippers

Where acids would attack exposed metal, residues after etching are
removed with amine solvents. An EKC Technology patent describes "A
stripping and cleaning composition for removing resists and etching
residue from substrates containing hydroxylamine and at least one
alkanolamine", with a chelating agent that "provides added stability
and effectiveness".[^pat-ekc-hydroxylamine] Wikipedia describes the
related solvent N-methyl-2-pyrrolidone.[^wiki-nmp]

## Representative 200 mm-era models

* **Akrion.** The GAMA automated wet station, "suitable for various
  cleaning, etching, and stripping applications",[^akrion-gama-series]
  installed as a "GAMA wet processor B" at a research
  centre,[^akrion-gama] and the E200 modular linear wet bench; Akrion
  bought most of the assets of SCP Global Technologies, "a manufacturer
  of batch-immersion tools", in 2006.[^sst-akrion-scp-2007]
* **SCREEN (formerly Dainippon Screen, DNS).** The WS-620C for 150 mm,
  WS-820C and WS-820L for 200 mm wafers, with an optional "low-pressure
  drying unit … to reduce watermarks".[^screen-ws820]
* **FSI International / Tokyo Electron.** The MERCURY batch spray
  cleaning system, "Supporting 75mm – 200mm wafers" and "only recently
  retired as the industry moved towards 300mm and single-wafer cleaning"
  when TEL returned it to production in 2018; TEL handed the line to
  another supplier in 2024.[^tel-mercury-2018]
* **Semitool.** Centrifugal spray processors, as described in its
  patent.[^pat-spray-semitool]
* **Other vendors.** The step pages also name SCP
  ({ref}`PRIS <step-054>`) and Santa Clara Plastics
  ({ref}`NS19 <step-013>`) benches; no separate vendor
  description was retrieved for this page.

## At SkyWater

### What SkyWater lists

SkyWater's *Facilities & Capabilities* page lists wet tools in two
places. Under "Resist removal/cleans", after the plasma ashers:[^skw-01]

> "Akrion Gamma Batch Wet Bench"
> – "Sulfuric, SC1, phosphoric, BOE, spin or IPA dry"
>
> "Batch Rotational"
> – "EKS265, EKC270 solvents, CO2 injected DI"

and under "Pre-cleaning", in the "Furnaces/Diffusion/Pre-Clean" group of
"Diffusion, Anneal & Implant":[^skw-01]

> "DNS wet bench industry standard HF/SC1/SC2"
> "dilute HF-last with IPA dry"
> "FSI Mercury industry standard HF/SC1/SC2 rotational"

Read term by term: the Akrion bench is the only entry with sulphuric
acid, phosphoric acid and BOE; the DNS bench and the FSI Mercury are the
only entries with SC-2; the Batch Rotational tool is a solvent tool with
CO₂-injected rinse water; and the "Single Wafer" entry that follows the
Batch Rotational, "SEZ223, Davinci, HF, DSP+HF, titration controlled",
is a {ref}`single-wafer spin processor <machine-single-wafer-spin-processor>`, a separate class.[^skw-01] SkyWater
gives no model, tank count or vendor for the Batch Rotational tool. We
read "Akrion Gamma" as Akrion's GAMA wet station,[^akrion-gama-series]
"DNS" as Dainippon Screen, now SCREEN,[^screen-ws820] and "rotational"
on the FSI Mercury as a rotating batch spray chamber of the kind the
Semitool patent describes;[^pat-spray-semitool] TEL describes the
MERCURY only as a "batch spray cleaning system".[^tel-mercury-2018]
These are inferences from the names. The step pages write the solvents
EKC265/EKC270; whether SkyWater's "EKS265" is the same product is not
stated.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>`
the four listings are **strong**: they are SkyWater
statements.[^skw-01] The caveats that apply to every listed tool are
under {ref}`Reading the SkyWater evidence <machines-reading-evidence>`.
For this class the chemistry lists do most of the work: "phosphoric"
appears only on the Akrion entry and SC-2 only on the DNS and FSI
entries, and the step pages build their assignments on
that.[^skw-01]

(machine-wet-bench-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a wet bench or
spray processor as the tool or one of two options, then the steps where
it runs a clean or strip around another operation (identical to the
{ref}`machines index <machines-index>` table):

{ref}`NS19 <step-013>`, {ref}`TUNME <step-039>`, {ref}`GOXETCH <step-046>`, {ref}`SACETCH <step-095>`; *also for a clean or strip:* {ref}`001 <step-001>`, {ref}`002 <step-002>`, {ref}`006 <step-006>`, {ref}`009 <step-009>`, {ref}`010 <step-010>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`025 <step-025>`, {ref}`029 <step-029>`, {ref}`033 <step-033>`, {ref}`042 <step-042>`, {ref}`051 <step-051>`, {ref}`054 <step-054>`, {ref}`057 <step-057>`, {ref}`062 <step-062>`, {ref}`067 <step-067>`, {ref}`070 <step-070>`, {ref}`074 <step-074>`, {ref}`079 <step-079>`, {ref}`084 <step-084>`, {ref}`087 <step-087>`, {ref}`103 <step-103>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`130 <step-130>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`145 <step-145>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`160 <step-160>`, {ref}`163 <step-163>`, {ref}`166 <step-166>`, {ref}`169 <step-169>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Akrion Gamma Batch Wet Bench"** — *strong ("the only phosphoric tank listed"):* {ref}`NS19 <step-013>`; *inference:* {ref}`DNIS <step-009>`, {ref}`TUNME <step-039>`, {ref}`GOXETCH <step-046>`; *strong for existence:* {ref}`STIE <step-006>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`ONOME <step-042>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`P1ME <step-062>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`LICM1E <step-094>`, {ref}`SACETCH <step-095>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>`
* **"DNS wet bench industry standard HF/SC1/SC2", "FSI Mercury industry standard HF/SC1/SC2 rotational"** — *inference (the pre-furnace or pre-anneal clean; SC-2 is listed only for these two benches):* {ref}`SMAT <step-001>`, {ref}`BOX <step-002>`, {ref}`DNIS <step-009>`, {ref}`LINOX <step-010>`, {ref}`PWDEIS <step-033>`, {ref}`LDASTIS <step-074>`, {ref}`NSDIS <step-087>`; *inference:* {ref}`SACETCH <step-095>`; *inference for the DNS bench, strong for existence for FSI Mercury:* {ref}`TUNME <step-039>`, {ref}`GOXETCH <step-046>`; *strong for existence:* {ref}`STIE <step-006>`, {ref}`NS19 <step-013>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`P1ME <step-062>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`PDIS <step-084>`, {ref}`LICM1E <step-094>`
* **"Batch Rotational", "EKS265, EKC270 solvents"** — *strong for existence (some pages add that the assignment is an inference):* {ref}`SACETCH <step-095>`, {ref}`LI1ME <step-103>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`VIM3E <step-145>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`VIM4E <step-160>`, {ref}`MM5E <step-163>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>`

The {ref}`NS19 <step-013>` grade is one of the few *strong* assignments
on the machines index, because the Akrion bench is "the only phosphoric
tank listed".[^skw-01] The single-wafer "SEZ223, Davinci" entry, which
several of these pages also name for HF etches and cleans, belongs to
the {ref}`single-wafer spin processor <machine-single-wafer-spin-processor>` class.

## Consumables and facilities

The wet chemicals are described on the
{ref}`wet chemicals <material-wet-chemicals>` page and listed in the
{ref}`materials index <materials-index>`; what is specific to a wet bench is summarised here.
None of the SkyWater sources describes the fab's chemical supply or
waste treatment. Ultrapure water, its standards and its quality
parameters are described on the
{ref}`ultrapure water <material-ultrapure-water>` page.

* **Acids, bases and oxidisers.** Sulphuric acid and hydrogen peroxide
  for SPM; ammonia, hydrochloric acid and peroxide for SC-1 and
  SC-2;[^wiki-rca][^wiki-piranha] 49 % HF, NH₄F for
  BOE;[^wiki-boe][^wiki-hf] and phosphoric acid for the nitride
  bath.[^wiki-h3po4][^vgh-1967] SkyWater lists sulphuric, SC1, SC2, HF,
  phosphoric and BOE across its benches.[^skw-01]
* **Solvents.** Hydroxylamine–alkanolamine strippers of the kind EKC
  Technology patented,[^pat-ekc-hydroxylamine] and IPA for drying; SkyWater
  lists "EKS265, EKC270 solvents" and "IPA dry".[^skw-01]
* **Water and gases.** Ultrapure water in large volumes — Ohmi's
  room-temperature clean was designed partly to cut it[^ohmi-1996] — with
  CO₂ dissolved where charging matters.[^pat-dico2-mks]
* **Bath control.** Concentration monitors, water spiking for the
  phosphoric bath and scheduled bath changes;[^liu-2007][^akrion-gama]
  quartz and fluoropolymer tanks and carriers ({ref}`category-strip`).

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's clean and wet-etch recipes are
not public.

* **The nitride strip.** {ref}`NS19 <step-013>` removes the isolation
  nitride in hot phosphoric acid, where water content sets the
  nitride-to-oxide selectivity;[^vgh-1967][^liu-2007] the page assigns
  it to the Akrion bench as the only phosphoric tank SkyWater
  lists.[^skw-01]
* **Wet oxide etches over thin films.** {ref}`TUNME <step-039>` removes
  the oxide from the tunnel windows (the pad oxide, on that page's
  inference) and {ref}`GOXETCH <step-046>` strips the exposed thick gate
  oxide, both with BOE, the etchant a Cypress embedded-SONOS patent
  names for the two operations, with 20:1 BOE or 50:1 HF among its
  alternatives for the pad oxide;[^pat-04] the
  {ref}`SACETCH <step-095>` page reads its etch, by inference, as a
  dilute-HF dip. At these thicknesses the slow, well-controlled rates of
  dilute HF matter.[^kikuyama-1994][^wiki-boe]
* **Pre-furnace cleans.** The oxidation and anneal pages
  ({ref}`BOX <step-002>`, {ref}`LINOX <step-010>` and the pre-anneal
  cleans of several implant strips) assign the clean to the DNS or FSI
  tools because SC-2, which removes metallic contamination, is listed
  only for them;[^skw-01][^wiki-rca] the DNS entry's "dilute HF-last with
  IPA dry" is the option the {ref}`GOXETCH <step-046>`
  page matches to its HF-last pre-gate clean.[^skw-01]
* **Cleans after implant strips.** The implant-strip pages follow the
  ash with SPM and SC-1 on the Akrion bench to remove the residue that
  ashing leaves;[^skw-01] Fujimura et al. found that residue to be
  mainly "oxide of the implanted species".[^fujimura-1989]
* **Solvent cleans over metal.** After the local-interconnect, metal,
  via, capacitor and pad etches, the pages name the "Batch Rotational"
  solvent tool rather than acid benches, because SPM attacks aluminium
  and TiN ({ref}`category-strip`); corrosion after such cleans depends
  on how well the wafer is dried.[^wai-2017][^pat-ekc-hydroxylamine]
* **Spray or single-wafer alternatives.** Several pages offer the FSI
  Mercury spray tool or the single-wafer SEZ tools for the HF steps; the
  capabilities page names HF on both.[^skw-01]

## Related pages

* {ref}`category-strip` — wet strip and clean chemistry and the nitride
  strip.
* {ref}`category-etch` — wet etching of oxides and nitride.
* {ref}`machine-downstream-plasma-asher` — the ash that precedes most
  wet strips.
* {ref}`machines-index` — all machine classes, including the
  single-wafer spin processor, SkyWater's listed tools and the step
  assignments.
* {ref}`materials-index` — wet chemicals and ultrapure water.
* {ref}`material-wet-chemicals` — the acids, peroxide cleans and solvents,
  their grades and SkyWater's listed chemistries.
* {ref}`material-ultrapure-water` — rinse water, its standards and
  quality.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,334,332 A <patent-gp24443399>` — Cleaning compositions for removing etching residue and method of using (1990)
* {ref}`US 7,305,999 B2 <patent-gp24449421>` — Centrifugal spray processor and retrofit kit (2000)

:::{dropdown} 2 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`EP 2 104 648 B1 <patent-gp39203155>` — in force
* {ref}`US 8,796,098 B1 <patent-gp51229009>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the Akrion, Batch
  Rotational, DNS and FSI Mercury entries quoted on this page.[^skw-01]
* Akrion Technologies, *GAMA Automated Wet Station* — the batch
  immersion design and concentration control.[^akrion-gama-series]
* C2MI, *Akrion GAMA acid bench* — an installed GAMA wet processor and
  its automation.[^akrion-gama]
* Solid State Technology, Akrion E200 sale (2007) — a 200 mm bench's
  configurations, rinse and drying, and Akrion's purchase of
  SCP.[^sst-akrion-scp-2007]
* SCREEN Semiconductor Solutions, *Wet Station WS-620C / WS-820L* — the
  DNS 200 mm wet stations.[^screen-ws820]
* Tokyo Electron, MERCURY MP relaunch (2018) — the batch spray system's
  wafer sizes, installed base and scope.[^tel-mercury-2018]
* Meuchel, Bernt and Henke (Semitool), US 7,305,999 — the centrifugal
  spray processor.[^pat-spray-semitool]
* Gottschalk et al. (MKS Instruments), EP 2 104 648 B1 — CO₂ in DI rinse
  water against surface charging.[^pat-dico2-mks]
* Lee (EKC Technology), US 5,334,332 — hydroxylamine and alkanolamine
  residue removers.[^pat-ekc-hydroxylamine]
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — BOE
  etches of the pad and thick gate oxides, with HF alternatives, in an
  embedded-SONOS flow.[^pat-04]

### High-level understanding

* Wikipedia, *RCA clean* — the SC-1, HF and SC-2 sequence.[^wiki-rca]
* Wikipedia, *Piranha solution* — SPM composition.[^wiki-piranha]
* Wikipedia, *Buffered oxide etch* — BOE composition and
  rate.[^wiki-boe]
* Wikipedia, *Hydrofluoric acid* and *Phosphoric acid* — two bench
  chemicals.[^wiki-hf][^wiki-h3po4]
* Wikipedia, *N-Methyl-2-pyrrolidone* — a resist solvent.[^wiki-nmp]
* Stanford Nanofabrication Facility, *Silicon Nitride Wet Etching* — a
  university hot-phosphoric bench.[^snf-nitride-wet]
* Kern, ch. 1 of *Handbook of Silicon Wafer Cleaning Technology* — an
  overview of cleaning technology.[^kern-handbook]

### Deep dive

* Kern, *JES* 1990 — the evolution of wafer cleaning and its
  equipment.[^kern-1990]
* Kern and Puotinen, *RCA Review* 1970 — the original peroxide
  cleaning solutions.[^kern-1970]
* Ohmi, *JES* 1996 — a room-temperature wet clean with less chemical and
  water use.[^ohmi-1996]
* Reinhardt and Kern (eds.), *Handbook of Silicon Wafer Cleaning
  Technology* — wet cleaning, resist removal and particle
  control.[^reinhardt-2008]
* van Gelder and Hauser, *JES* 1967 — etching nitride in refluxed hot
  phosphoric acid.[^vgh-1967]
* Liu et al., *ECS Trans.* 2007 — keeping the nitride-to-oxide
  selectivity of a production phosphoric bath stable.[^liu-2007]
* Deckert, *JES* 1978 — the rate law for nitride in acidic fluoride
  solutions.[^deckert-1978]
* Knotter and Denteneer, *JES* 2001 — the etching mechanism of nitride in
  HF solutions.[^knotter-2001]
* Kikuyama et al., *JES* 1994 — dissociation and oxide etching in very
  dilute HF.[^kikuyama-1994]
* Lee, *ESSL* 1999 — silicon and oxide etch rates in ammonia–peroxide
  solutions.[^lee-kt-1999]
* Leenaars, Huethorst and van Oekel, *Langmuir* 1990 — Marangoni
  drying.[^leenaars-1990]
* Wai and Ling, ASMC 2017 — corrosion after wet polymer clean and the
  Marangoni dry that prevents it.[^wai-2017]
* Fujimura et al., *JJAP* 1989 — the residues left by ashing implanted
  resist.[^fujimura-1989]

## Open questions

* Which bench or spray tool runs which SKY130 clean, strip or wet etch
  is not stated;[^skw-01] the step pages' assignments are inferences from
  the listed chemistries.
* What the "Batch Rotational" tool is (vendor and model), whether
  "EKS265" is EKC265, and whether "Akrion Gamma" is Akrion's GAMA
  station, are not stated.
* The model list above is incomplete: it covers the Akrion, SCREEN,
  FSI/TEL and Semitool tools for which a public description was found,
  not the SCP, Santa Clara Plastics and other benches of the period.

<!-- footnotes -->

[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^wiki-piranha]: Wikipedia, *Piranha solution*.
    <https://en.wikipedia.org/wiki/Piranha_solution>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
[^wiki-boe]: Wikipedia, *Buffered oxide etch*.
    <https://en.wikipedia.org/wiki/Buffered_oxide_etch>
[^vgh-1967]: W. van Gelder and V. E. Hauser, "The Etching of Silicon
    Nitride in Phosphoric Acid with Silicon Dioxide as a Mask", *Journal
    of The Electrochemical Society* **114**(8), 869 (1967).
    <https://doi.org/10.1149/1.2426757>
[^liu-2007]: L. Liu, I. Kashkoush, G. Chen and C. Murphy, "Maintaining a
    Stable Etch Selectivity between Silicon Nitride and Silicon Dioxide
    in a Hot Phosphoric Acid Bath", *ECS Transactions* **11**(2), 63–70
    (2007). <https://doi.org/10.1149/1.2779363>
[^screen-ws820]: SCREEN Semiconductor Solutions, *Wet Station: WS-620C /
    WS-820L*, product page, accessed 2026-09-13.
    <https://www.screen.co.jp/spe/en/products/ws-620c820l>
[^pat-spray-semitool]: C. Meuchel, M. Bernt and T. Henke (Semitool),
    *Centrifugal spray processor and retrofit kit*, US 7,305,999 B2,
    filed 2002-07-19, granted 2007-12-11.
    <https://patents.google.com/patent/US7305999B2/en>
[^leenaars-1990]: A. F. M. Leenaars, J. A. M. Huethorst and J. J. van
    Oekel, "Marangoni drying: A new extremely clean drying process",
    *Langmuir* **6**(11), 1701–1703 (1990).
    <https://doi.org/10.1021/la00101a014>
[^akrion-gama]: C2MI, *Akrion GAMA acid bench*, equipment page.
    <https://www.c2mi.ca/en/equipement/akrion-gama-acid-bench/>
[^sst-akrion-scp-2007]: Solid State Technology, *Akrion sells "SCP"
    automated wet station for wafer cleaning*, 2007-06-11.
    <https://sst.semiconductor-digest.com/2007/06/akrion-sells-scp-automated-wet-station-for-wafer-cleaning/>
[^tel-mercury-2018]: Tokyo Electron, *TEL announces the relaunch of
    MERCURY MP, a Batch Spray Cleaning System*, news release, 2018-07-10,
    accessed 2026-09-13.
    <https://www.tel.com/news/product/2018/20180710_001.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; resist removal and pre-cleaning entries re-checked
    2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^kern-handbook]: W. Kern, "Overview and Evolution of Silicon Wafer
    Cleaning Technology", ch. 1 in K. A. Reinhardt and W. Kern (eds.),
    *Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
    Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8.
    <https://doi.org/10.1016/b978-081551554-8.50004-5>
[^akrion-gama-series]: Akrion Technologies, *GAMA Automated Wet
    Station*, product page, accessed 2026-09-13.
    <https://www.akriontech.com/product-3>
[^snf-nitride-wet]: Stanford Nanofabrication Facility, *Silicon Nitride
    Wet Etching*, equipment-purpose page.
    <https://snfguide.stanford.edu/guide/equipment/purpose/etching/wet-etching/silicon-nitride-wet-etching>
[^kikuyama-1994]: H. Kikuyama, M. Waki, M. Miyashita, T. Yabune, N.
    Miki, J. Takano and T. Ohmi, "A Study of the Dissociation State and
    the SiO₂ Etching Reaction for HF Solutions of Extremely Low
    Concentration", *Journal of The Electrochemical Society* **141**(2),
    366–374 (1994). <https://doi.org/10.1149/1.2054733>
[^deckert-1978]: C. A. Deckert, "Etching of CVD Si₃N₄ in Acidic Fluoride
    Media", *Journal of The Electrochemical Society* **125**(2), 320–323
    (1978). <https://doi.org/10.1149/1.2131436>
[^knotter-2001]: D. M. Knotter and T. J. J. Denteneer, "Etching
    Mechanism of Silicon Nitride in HF-Based Solutions", *Journal of The
    Electrochemical Society* **148**(3), F43 (2001).
    <https://doi.org/10.1149/1.1348262>
[^ohmi-1996]: T. Ohmi, "Total Room Temperature Wet Cleaning for Si
    Substrate Surface", *Journal of The Electrochemical Society*
    **143**(9), 2957–2964 (1996). <https://doi.org/10.1149/1.1837133>
[^wai-2017]: W. T. Wai and N. C. Ling, "Al-Cu interconnect corrosion
    prevention in post metal etch and wet polymer clean wafers: CFM:
    Contamination free manufacturing", *2017 28th Annual SEMI Advanced
    Semiconductor Manufacturing Conference (ASMC)*, pp. 64–67.
    <https://doi.org/10.1109/ASMC.2017.7969200>
[^pat-dico2-mks]: C. Gottschalk, U. Brammer, J. Lohr and J. Seiwert (MKS
    Instruments), *System and method for carbonation of deionized
    water*, EP 2 104 648 B1, granted 2013-04-17.
    <https://patents.google.com/patent/EP2104648B1/en>
[^pat-ekc-hydroxylamine]: W. M. Lee (EKC Technology), *Cleaning
    compositions for removing etching residue and method of using*,
    US 5,334,332 A, granted 1994-08-02.
    <https://patents.google.com/patent/US5334332A/en>
[^wiki-nmp]: Wikipedia, *N-Methyl-2-pyrrolidone*.
    <https://en.wikipedia.org/wiki/N-Methyl-2-pyrrolidone>
[^wiki-hf]: Wikipedia, *Hydrofluoric acid*.
    <https://en.wikipedia.org/wiki/Hydrofluoric_acid>
[^wiki-h3po4]: Wikipedia, *Phosphoric acid*.
    <https://en.wikipedia.org/wiki/Phosphoric_acid>
[^fujimura-1989]: S. Fujimura, J. Konno, K. Hikazutani and H. Yano,
    "Ashing of Ion-Implanted Resist Layer", *Japanese Journal of Applied
    Physics* **28**(10R), 2130 (1989).
    <https://doi.org/10.1143/JJAP.28.2130>
[^kern-1970]: W. Kern and D. A. Puotinen, "Cleaning solutions based on
    hydrogen peroxide for use in silicon semiconductor technology", *RCA
    Review* **31**, 187–206 (1970). No DOI; *RCA Review* 31 is available
    in print and in library archives.
[^reinhardt-2008]: K. A. Reinhardt and W. Kern (eds.), *Handbook of
    Silicon Wafer Cleaning Technology*, 2nd ed., William Andrew, 2008,
    ISBN 978-0-8155-1554-8. <https://openlibrary.org/isbn/9780815515548>
[^lee-kt-1999]: K. T. Lee, "Etch Rate of Silicon and Silicon Dioxide in
    Ammonia-Peroxide Solutions Measured by Quartz Crystal Microbalance
    Technique", *Electrochemical and Solid-State Letters* **2**(4), 172
    (1999). <https://doi.org/10.1149/1.1390773>
