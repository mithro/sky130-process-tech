(machine-vertical-furnace-lpcvd)=
# Vertical batch furnace: LPCVD

A vertical LPCVD furnace is a hot-wall, low-pressure chemical vapour
deposition reactor built on the same vertical batch platform as an
oxidation furnace: a quartz tube inside a multi-zone heater, a boat of
horizontal wafers raised in from below, and a vacuum pump and gas panel
instead of an oxidant supply. It deposits the conformal thermal films of
the front end — silicon nitride, amorphous and polycrystalline silicon,
and deposited oxides — on a hundred or more wafers at once. This page
describes the class in general, lists representative 200 mm-era models,
and then says what SkyWater has published about its own furnaces and
which SKY130 steps this reference assigns to the class. The deposition
physics (growth regimes, conformality, the LPCVD film chemistries) is
on the {ref}`category page <category-deposition>`; the furnace hardware
shared with oxidation is described on the
{ref}`oxidation furnace page <machine-vertical-furnace-oxidation>`.

| | Vertical batch furnace: LPCVD |
|---|---|
| What it does | Deposits films from gases at reduced pressure on a batch of wafers in a hot-wall tube; LPCVD "dominates for multi-wafer furnace tube tools", and "Reduced pressures tend to reduce unwanted gas-phase reactions and improve film uniformity across the wafer".[^wiki-cvd] |
| Pressure | "several hundred m Torr" for a dichlorosilane nitride in a vertical furnace;[^pat-nh4cl-tsmc] "5-500 mTorr" for the oxynitride layers of a Cypress ONO stack "in a batch furnace";[^pat-03] below 1 Torr for TEOS oxide.[^becker-1987] |
| Films and temperatures | Nitride from dichlorosilane and ammonia at about 750–800 °C;[^pat-nh4cl-tsmc] nitride from BTBAS and ammonia "at 550-600°C in a 200 mm vertical batch furnace system";[^gumpher-2004] silicon films "polycrystalline … above 600°C" and amorphous below;[^kamins-1980] TEOS oxide at 650–800 °C.[^becker-1987] |
| By-products | Ammonium chloride from the dichlorosilane–ammonia reaction, "gaseous … typically about 700° C." but "a solid condensate at temperatures below about 125° C."[^pat-nh4cl-vlsi] |
| Wafer handling | Batch: "150 product, test, and filler wafers" in a typical VTR LPCVD load;[^expertech-vtr] "a batch of up to 150" on TEL's ALPHA-8SE i;[^tel-telindy] a boat "supported by a boat elevator and boat pedestal" inside an inner sleeve.[^pat-lpcvd-sony] |
| 200 mm era | TEL's Alpha-8 "diffusion and LP-CVD furnaces"[^tel-alpha8se] and the VCF-615S LP-TEOS furnace;[^pat-lpcvd-sony] Aviza's AVP-8000 for "silicon nitride (stoichiometric and low stress), TEOS, SiH4 and DCS-based SiO2, doped (P, As, B) and un-doped polysilicon";[^aviza-avp] ASM's A400 for "doped silicon and silicon nitride films".[^asm-a400] |
| SkyWater-listed tool | "LPCVD nitride, with NH3 and also DH3", "LPCVD polysilicon (undoped), both amorphous and crystalline", "LPCVD silane oxide", "LPCVD oxide/nitride/oxide", "LPCVD BTBAS low temp nitride" (Aviza)[^skw-01] |
| SKY130 steps | 6 steps, plus 2 where the class is an alternative; see {ref}`SKY130 steps assigned to this class <machine-vertical-furnace-lpcvd-steps>` |

## What the machine class is and how it works

In an LPCVD furnace the wafers, the boat and the tube wall are all at
the deposition temperature, and the film grows wherever the reactant
gases reach a hot surface. At a few hundred millitorr the gases diffuse
quickly between closely stacked wafers, so the deposition is limited by
the surface reaction rather than by gas transport, which is what makes a
batch of wafers only millimetres apart coat uniformly and conformally
(category page).[^txt-01] Roenigk and Jensen's model of a hot-wall
nitride reactor shows the limits of that picture: "in‐wafer film
thickness nonuniformities may be explained by the effect of
diffusion‐limited film growth from highly reactive gas‐phase
intermediates, with simultaneous uniform deposition from less reactive
dichlorosilane".[^roenigk-1987]

### Tube, gas injection and exhaust

An LPCVD tube is usually double. A Kokusai patent describes the
conventional arrangement: "an outer tube with a closed upper end", "An
inner tube … with upper and lower opened ends" inside it, a reactive gas
introduced at the flange, and an exhaust nozzle that "communicates with a
gap defined between the outer tube … and inner tube", so that the gas
rises through the boat inside the inner tube and descends between the
tubes to the pump.[^pat-lpcvd-kokusai] Sony's description of TEL's
VCF-615S LP-TEOS furnace is similar: "a bell-shaped chamber wall into
which is disposed an inner sleeve", "A multi-zone heating element",
"a vacuum pump coupled to the deposition chamber through an exhaust port
… proximate the bottom", and TEOS vapour "injected into the bottom zone
of the chamber".[^pat-lpcvd-sony] Expertech's VTR uses "a double-walled
process tube to eliminate film particle formation near the loading door
for advanced particle control in LPCVD films".[^expertech-vtr]

Where two reactants must not meet too early, the injectors matter. An
NEC vertical LPCVD furnace for oxide has separate annular nozzles for
"silane gas and an oxidizing gas", spaced so that the two "are mixed in a
uniform ratio … without an early reaction".[^pat-lpcvd-nec]

### Depletion along the boat

Reactant is consumed as the gas passes each wafer, so a furnace fed from
one end would deposit less at the far end. The hardware above answers
this with a multi-zone heater,[^pat-lpcvd-sony] placed
injectors[^pat-lpcvd-nec] and boat covers. Kokusai's boat cover
splits the gas into "branched streams, one flowing through the inside of
the boat cover and the other flowing in past the boat cover, whereby the
film deposited on the wafer is improved in uniformity and
homogeneity".[^pat-lpcvd-kokusai] Wafer spacing trades capacity against
uniformity: Becker et al. found "oxide thickness variations of <±5%" for
TEOS "for suitable process conditions (PD ≤500 mTorr, wafer spacing
≥4.7 mm, TD <730 °C …)" and "uniformities of ±2%" on 150 mm wafers "if
the wafer spacing is increased to 10 mm".[^becker-1987] Adding a dopant
gas can upset the balance: phosphine caused "a factor of 25 decay in film
growth rates" in doped poly, with "growth‐rate variations of a factor of
two within a wafer commonly observed",[^meyerson-1984] and in TEOS oxide
"The addition of phosphorus compounds causes the deposition rate to
increase and the thickness uniformity to degrade".[^adams-1979]

### The films

* **Silicon nitride from dichlorosilane.** The standard stoichiometric
  nitride; the reaction produces HCl and, with excess ammonia, ammonium
  chloride (below).[^wiki-sin][^pat-nh4cl-tsmc] LPCVD nitride "contains up
  to 8% hydrogen" and "experiences strong tensile stress, which may crack
  films thicker than 200 nm".[^wiki-sin] Temple-Boyer et al. show, for
  silane–ammonia LPCVD nitride, how stress and composition follow
  temperature, pressure and gas ratio.[^temple-boyer-1998]
* **Low-temperature nitride from BTBAS.** Bis(tertiary-butylamino)silane
  lowers the nitride temperature: Gumpher et al. deposited it "at
  550-600°C in a 200 mm vertical batch furnace system" at "4-30 Å/min"
  with thickness variation "below 2% 1-sigma", and found "Substantial
  carbon and hydrogen incorporation" relative to dichlorosilane
  nitride.[^gumpher-2004] Aviza, in 2004, put the dichlorosilane process
  "above 630 degrees C" and BTBAS "at 570 degrees C or above".[^aviza-satin-2004]
* **Amorphous and polycrystalline silicon from silane.** Kamins found
  that "polycrystalline films are formed above 600°C and are more stable
  than the amorphous films deposited at lower temperatures";[^kamins-1980]
  films whose surfaces are amorphous are "much smoother",[^kinsbron-1983]
  and films "deposited in the amorphous phase and subsequently
  crystallized at 900°–1000°C" are "superior in all investigated material
  aspects".[^harbeke-1984]
* **Deposited oxides.** TEOS oxide at "700°–750°C" with thickness
  uniformity "better than ±1% over a deposition zone capable of holding
  100 wafers" and conformal step coverage;[^adams-1979] silane-based oxide
  and dichlorosilane-based oxide are the other furnace
  chemistries.[^aviza-avp]
* **Stacks.** A furnace that can oxidise and deposit can build an
  oxide–nitride–oxide stack in one load; Cypress forms its oxynitride
  layers from "N₂O, NH₃ and SiH₂Cl₂" "in a batch furnace",[^pat-03] and
  Aviza's 300 mm RVP-300 offered "sequential processing for nitrided
  oxides or composite oxide-nitride stacks".[^aviza-vert]

### By-products, pumping and particles

Every film leaves by-products and deposits on something other than the
wafer. Dichlorosilane nitride is the difficult case. Ammonium chloride
"condenses as a solid in the exhaust pipes and within the exhaust pump",
and the condensate "can back-flow into the processing chamber under
certain circumstances, which can contaminate the chamber and any wafer
within the chamber"; VLSI Technology's trap heats its walls to about
140 °C and collects the salt on a water-cooled surface.[^pat-nh4cl-vlsi]
A TSMC patent describes the same salt "in the form of a fine powder" that
"can easily deposit on any cold surface in the furnace or in the ducting
system", powder that "may be syphoned back into the furnace during a
deposition process if the pressure in the furnace is not carefully
controlled".[^pat-nh4cl-tsmc] Film also builds up on the tube, boat and
injectors. Expertech's double-walled tube is meant "to eliminate film
particle formation near the loading door", and its VTR offers "Easier and
faster process tube maintenance through a mechanized tube removal
system".[^expertech-vtr]

## Representative 200 mm-era models

* **SVG Thermco, later Aviza Technology.** The VTR, which offers
  "within-wafer and wafer-to-wafer uniformity in atmospheric and LPCVD
  processes";[^expertech-vtr] the AVP-8000, whose applications include
  nitride, TEOS and silane- and DCS-based oxides, and doped and undoped
  polysilicon;[^aviza-avp] and the RVP-500, on which Aviza introduced a
  nitride process "at approximately 500 degrees C" in
  2004.[^aviza-satin-2004]
* **Tokyo Electron.** The Alpha-8 series of "diffusion and LP-CVD
  furnaces";[^tel-alpha8se] the ALPHA-8SE i successor runs "chemical vapor
  deposition (CVD) of Si (Poly, a-Si), SiN, and SiO₂ films";[^tel-telindy]
  the VCF-615S LP-TEOS furnace appears in a Sony patent.[^pat-lpcvd-sony]
* **ASM International.** The A400, with "low pressure chemical vapor
  deposition (LPCVD) processes like doped silicon and silicon nitride
  films".[^asm-a400][^asm-vf]
* **Kokusai Electric.** Vertical furnaces with the inner-and-outer-tube
  and boat-cover arrangement of its patents.[^pat-lpcvd-kokusai]

Single-wafer alternatives existed for some films: Teasdale et al.
describe "a single wafer rapid thermal processing (RTP) module for
low-pressure chemical vapor deposition (LPCVD) of silicon
nitride",[^teasdale-2001] and Smith et al. a single-wafer BTBAS nitride
chamber.[^smith-2005] SkyWater lists neither kind of tool.[^skw-01]

## At SkyWater

### What SkyWater lists

Under "Furnaces/Diffusion/Pre-Clean", after "Furnaces are all made by
Aviza", SkyWater's *Facilities & Capabilities* page lists five LPCVD
processes:[^skw-01]

> "LPCVD nitride, with NH3 and also DH3"
>
> "LPCVD polysilicon (undoped), both amorphous and crystalline"
>
> "LPCVD silane oxide"
>
> "LPCVD oxide/nitride/oxide"
>
> "LPCVD BTBAS low temp nitride"

Read term by term: a nitride process using ammonia, a silicon process
that can be run amorphous or crystalline and is undoped, an oxide from
silane, a combined ONO process and a low-temperature BTBAS nitride. The
page does not expand "DH3"; the step pages describe dichlorosilane
nitride but do not read "DH3" as dichlorosilane, and neither does this
page. No TEOS furnace oxide and no in-situ doped silicon are
listed.[^skw-01] The entries give no temperatures, pressures, models or
tube counts, and do not say whether the furnaces are vertical.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` the
listing is **strong** for the vendor and for each of the five
processes: it is a SkyWater statement.[^skw-01] The caveats that apply
to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`, and
the Aviza history and the question of vertical or horizontal tubes are
on the {ref}`oxidation furnace page <machine-vertical-furnace-oxidation>`.
For this class the list is unusually specific — a process named
"oxide/nitride/oxide" and a BTBAS nitride match particular SKY130 films —
but it still names no step, so the grades below are the step pages'
readings of a listed capability.

(machine-vertical-furnace-lpcvd-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a vertical LPCVD
furnace as the tool or one of two options (identical to the
{ref}`machines index <machines-index>` table):

{ref}`ISONIT <step-003>`, {ref}`ONO <step-040>`, {ref}`SAGD <step-048>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`SPNIT <step-076>`; *alternative:* {ref}`SPOX <step-080>`, {ref}`LINIT <step-104>`

How the step pages grade the SkyWater tool for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Furnaces are all made by Aviza" (with the process lines quoted
  above)** — *strong:* {ref}`BOX <step-002>`, {ref}`ISONIT <step-003>`; *inference:* {ref}`LINOX <step-010>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`, {ref}`SAGD <step-048>`, {ref}`GATENIT <step-058>`, {ref}`IOX45 <step-063>`, {ref}`SPNIT <step-076>`, {ref}`ALLY1 <step-096>`, {ref}`ALLY <step-170>`; *strong for existence (batch alternative):* {ref}`FILOX <step-011>`, {ref}`POC <step-059>`, {ref}`SPOX <step-080>`; *weak:* {ref}`RTAI <step-034>`, {ref}`TIPRTAD <step-075>`, {ref}`RTAD <step-088>`, {ref}`RTAD2 <step-092>`, {ref}`LINIT <step-104>`; *excluded on thermal grounds (inference):* {ref}`NTSD <step-167>`
* **The PECVD entries instead** — "PECVD silane
  oxide/nitride/oxynitride, C1" and "PECVD nitride C1": *inference:*
  {ref}`LINIT <step-104>`; *not public which of the candidates:*
  {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`; *strong for
  existence:* {ref}`SPOX <step-080>`; *weak:* {ref}`SPNIT <step-076>`.
  "PECVD TEOS, C2 and Producer": *not public which of the candidates:*
  {ref}`POC <step-059>`; *weak:* {ref}`SPOX <step-080>`. See the
  {ref}`PECVD page <machine-pecvd>`.

The furnace row covers all three furnace classes, because SkyWater
lists its furnaces as one group; the LPCVD steps are those in the
paragraph above. The grades rest on the listed processes: "LPCVD
nitride" for {ref}`ISONIT <step-003>` (strong) and
{ref}`GATENIT <step-058>` (inference), "LPCVD oxide/nitride/oxide" for
{ref}`ONO <step-040>` (inference), "LPCVD polysilicon (undoped), both
amorphous and crystalline" for {ref}`SAGD <step-048>` (inference), "LPCVD
BTBAS low temp nitride" for {ref}`SPNIT <step-076>` (inference) and
{ref}`LINIT <step-104>` (weak), and "LPCVD silane oxide" for
{ref}`POC <step-059>` and {ref}`SPOX <step-080>` (strong for existence,
as the batch alternative).[^skw-01]

## Consumables and facilities

The precursors and process gases are described on the
{ref}`precursors <material-precursors>` and
{ref}`process gases <material-process-gases>` pages.
The precursor gases are listed in the
{ref}`materials index <materials-index>`; what is specific to a batch
LPCVD furnace is summarised here. None of the SkyWater sources describes
the fab's gas delivery, pumps or abatement. Quartz and silicon-carbide
furnace ware is described on the
{ref}`hardware consumables and abatement <material-hardware-consumables>`
page.

* **Precursors.** Dichlorosilane and ammonia for nitride; BTBAS, a
  liquid delivered as vapour, with ammonia for low-temperature
  nitride;[^gumpher-2004] silane for silicon and silane
  oxide;[^kamins-1980] N₂O for oxide and oxynitride layers;[^pat-03] TEOS
  for TEOS oxide where it is used.[^becker-1987] SkyWater names ammonia,
  BTBAS and silane in its process lines.[^skw-01]
* **Vacuum and exhaust.** Dry pumps, heated exhaust lines and traps for
  ammonium chloride, which condenses "at temperatures below about 125°
  C.";[^pat-nh4cl-vlsi] trap capture efficiency "is therefore an important
  factor in the successful deposition of silicon nitride
  films".[^pat-nh4cl-tsmc]
* **Quartzware.** Outer and inner tubes, boats, boat covers and
  injectors;[^pat-lpcvd-kokusai] deposits on them are removed at tube
  cleans, and the cleaned or replaced quartz is the main consumable of the
  class.
* **Filler and monitor wafers.** Fillers at the ends of the boat, and
  monitors for {ref}`thickness, refractive index and stress <machine-film-thickness-metrology>` in each
  load.[^expertech-vtr]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's deposition temperatures,
pressures and thicknesses are not public.

* **Thermal budget decides the nitride chemistry.** The
  {ref}`SPNIT <step-076>` page reads the spacer nitride as a candidate for
  the listed BTBAS process because it follows the tip implants, and a
  dichlorosilane nitride at the temperatures above would add diffusion;
  the {ref}`LINIT <step-104>` page, later still and over TiN local
  interconnect, prefers PECVD and keeps BTBAS as the batch alternative.
  Aviza's own figures put BTBAS at "570 degrees C or above" against
  "above 630 degrees C" for dichlorosilane.[^aviza-satin-2004]
* **An amorphous gate film.** The {ref}`SAGD <step-048>` page describes
  the gate silicon as deposited amorphous and undoped, which matches
  SkyWater's "LPCVD polysilicon (undoped), both amorphous and
  crystalline";[^skw-01] amorphous deposition gives a smoother film that
  recrystallises in later anneals.[^kinsbron-1983][^harbeke-1984]
* **The ONO stack across two classes.** The {ref}`ONO <step-040>` page
  combines oxidation of the tunnel oxide with LPCVD of the trapping
  nitride and possibly the blocking oxide; the SkyWater entry "LPCVD
  oxide/nitride/oxide" is the only list entry named after such a
  stack.[^skw-01]
* **Batch or single-wafer dielectrics.** For the gate nitride and oxide
  cap ({ref}`GATENIT <step-058>`, {ref}`POC <step-059>`) the step pages
  give LPCVD and PECVD as equal options and say which is used is not
  public; for the spacer oxide and the local-interconnect nitride cap
  ({ref}`SPOX <step-080>`, {ref}`LINIT <step-104>`) the furnace is the
  alternative. The deciding factors the pages give are thermal budget and
  conformality.
* **Nitride stress and cracking.** LPCVD nitride's tensile stress limits
  its thickness;[^wiki-sin] the {ref}`ISONIT <step-003>` page uses the
  nitride as the STI polish stop over a pad oxide, whose purpose is to
  cushion that stress (category page).

## Related pages

* {ref}`category-deposition` — LPCVD chemistry and the deposition steps
  of SKY130.
* {ref}`machine-vertical-furnace-oxidation` — the furnace platform, the
  Aviza history and the ONO oxidations.
* {ref}`machine-vertical-furnace-anneal` — the same furnace group used
  for anneals and the alloy.
* {ref}`machine-pecvd` — the single-wafer plasma alternative for the gate
  nitride, oxide cap, spacer oxide and local-interconnect nitride cap.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — the precursor gases and their hazards.
* {ref}`category-etch` — the etches that pattern the furnace nitrides and
  the gate silicon.
* {ref}`material-hardware-consumables` — furnace ware, traps and
  abatement.
* {ref}`material-precursors` — silane, dichlorosilane, TEOS, BTBAS,
  ammonia, SiF₄, ozone and WF₆.
* {ref}`material-process-gases` — nitrogen, oxygen, hydrogen, argon,
  helium and the oxidation additives, their grades and SkyWater's listed
  gases.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the five LPCVD
  entries quoted on this page.[^skw-01]
* Moov, *Aviza / SVG / Thermco AVP 8000* listing — the LPCVD films of the
  vendor's 200 mm furnace.[^aviza-avp]
* Aviza Technology, Satin press release (2004) — the vendor's nitride
  temperatures for dichlorosilane, BTBAS and a new precursor.[^aviza-satin-2004]
* Aviza Technology, *Vertical Processors* page (2005) — sequential oxide
  and nitride processing on its furnaces.[^aviza-vert]
* Expertech, *VTR7000PLUS Thermal Reactor* — LPCVD loads and the
  double-walled tube.[^expertech-vtr]
* Tokyo Electron, *TELINDY Series* page — the ALPHA-8SE i CVD
  films.[^tel-telindy]
* ASM International, A400 DUO press release (2019) — the A400 LPCVD
  processes.[^asm-a400]
* Koutny et al. (Cypress), US 8,093,128 — ONO oxynitride layers in a batch
  furnace.[^pat-03]
* Persyn (Sony), US 5,800,616 — the TEL VCF-615S LP-TEOS furnace and its
  exhaust.[^pat-lpcvd-sony]

### High-level understanding

* Wikipedia, *Chemical vapor deposition* — LPCVD as the furnace-tube
  form of CVD.[^wiki-cvd]
* Wikipedia, *Silicon nitride* — LPCVD nitride chemistry, hydrogen content
  and stress.[^wiki-sin]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — CVD and LPCVD
  films.[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 — CVD of
  nitride, polysilicon and oxide.[^txt-02]
* ASM International, *Vertical furnace* — a vendor overview of batch
  LPCVD.[^asm-vf]
* Semiconductor Online, *Alpha-8SE* — TEL's 200 mm diffusion and LPCVD
  furnace generation.[^tel-alpha8se]

### Deep dive

* Roenigk and Jensen, *J. Electrochem. Soc.* 1987 — a hot-wall reactor
  model for dichlorosilane nitride.[^roenigk-1987]
* Temple-Boyer et al., *JVST A* 1998 — stress and composition of
  silane–ammonia LPCVD nitride.[^temple-boyer-1998]
* Gumpher et al., *J. Electrochem. Soc.* 2004 — BTBAS nitride in a 200 mm
  vertical batch furnace.[^gumpher-2004]
* Smith, Seutter and Iyer, *J. Electrochem. Soc.* 2005 — single-wafer BTBAS
  nitride.[^smith-2005]
* Teasdale et al., *Electrochem. Solid-State Lett.* 2001 — single-wafer
  rapid thermal LPCVD nitride.[^teasdale-2001]
* Kamins, *J. Electrochem. Soc.* 1980 — amorphous and polycrystalline LPCVD
  silicon films.[^kamins-1980]
* Kinsbron, Sternheim and Knoell, *Appl. Phys. Lett.* 1983 — crystallisation
  of amorphous silicon during deposition.[^kinsbron-1983]
* Harbeke et al., *J. Electrochem. Soc.* 1984 — amorphous deposition and
  recrystallisation versus as-deposited poly.[^harbeke-1984]
* Meyerson and Olbricht, *J. Electrochem. Soc.* 1984 — phosphine and
  growth-rate non-uniformity in doped poly.[^meyerson-1984]
* Becker et al., *JVST B* 1987 — low-pressure TEOS oxide and wafer
  spacing.[^becker-1987]
* Adams and Capio, *J. Electrochem. Soc.* 1979 — reduced-pressure TEOS
  oxide in a 100-wafer zone.[^adams-1979]
* Maeda et al. (Kokusai Electric), US 5,902,103 — inner and outer tubes
  and a boat cover for uniformity.[^pat-lpcvd-kokusai]
* Usami (NEC), US 5,503,678 — separate annular injectors for silane and
  oxidant.[^pat-lpcvd-nec]
* Caton et al. (VLSI Technology), US 5,303,558 — a thermal trap for
  ammonium chloride.[^pat-nh4cl-vlsi]
* Lin et al. (TSMC), US 2004/0069224 — a cold trap for a vertical nitride
  furnace.[^pat-nh4cl-tsmc]

## Open questions

* What "DH3" in SkyWater's "LPCVD nitride, with NH3 and also DH3" denotes
  is not stated.[^skw-01]
* Whether the gate nitride and oxide cap ({ref}`GATENIT <step-058>`,
  {ref}`POC <step-059>`) are furnace or PECVD films, and whether the spacer
  nitride uses the BTBAS or the ammonia nitride process, are not public.
* How many LPCVD tubes SkyWater runs, and whether nitride, silicon and
  oxide have dedicated tubes, is not stated.
* The model list above is incomplete: it covers the SVG/Aviza, Tokyo
  Electron, ASM and Kokusai furnaces for which a public description was
  found, not every LPCVD furnace of the period.

<!-- footnotes -->

[^wiki-cvd]: Wikipedia, *Chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Chemical_vapor_deposition>
[^pat-nh4cl-tsmc]: L. Lin, T. Fan, S. Chen, V. Lee and Y.-H. Wu (Taiwan
    Semiconductor Manufacturing Company), *Cold trap for CVD furnace*,
    US 2004/0069224 A1, filed 2002-10-11, published 2004-04-15.
    <https://patents.google.com/patent/US20040069224A1/en>
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
[^becker-1987]: F. S. Becker, D. Pawlik, H. Anzinger and A. Spitzer,
    "Low-pressure deposition of high-quality SiO₂ films by pyrolysis of
    tetraethylorthosilicate", *Journal of Vacuum Science & Technology B*
    **5**(6), 1555–1563 (1987). <https://doi.org/10.1116/1.583673>
[^gumpher-2004]: J. Gumpher, W. Bather, N. Mehta and D. Wedel,
    "Characterization of Low-Temperature Silicon Nitride LPCVD from
    Bis(tertiary-butylamino)silane and Ammonia", *Journal of The
    Electrochemical Society* **151**(5), G353 (2004).
    <https://doi.org/10.1149/1.1690294>
[^kamins-1980]: T. I. Kamins, "Structure and Properties of LPCVD Silicon
    Films", *Journal of The Electrochemical Society* **127**(3), 686–690
    (1980). <https://doi.org/10.1149/1.2129733>
[^pat-nh4cl-vlsi]: O. L. Caton, C. A. Bellows, C. M. Hebert, Jr. and
    S. J. Schaper (VLSI Technology), *Thermal trap for gaseous
    materials*, US 5,303,558 A, filed 1992-07-30, granted 1994-04-19.
    <https://patents.google.com/patent/US5303558A/en>
[^expertech-vtr]: Expertech, *VTR7000PLUS Thermal Reactor | Vertical
    Diffusion Furnaces*, product page, accessed 2026-09-13.
    <https://www.exper-tech.com/products/vertical-thermal-reactor>
[^tel-telindy]: Tokyo Electron, *Deposition TELINDY Series* (product page
    including the ALPHA-8SE i), accessed 2026-09-13.
    <https://www.tel.com/product/telindy.html>
[^pat-lpcvd-sony]: S. C. Persyn (Sony), *Vertical LPCVD furnace with
    reversible manifold collar and method of retrofitting same*,
    US 5,800,616 A, filed 1997-12-15, granted 1998-09-01.
    <https://patents.google.com/patent/US5800616A/en>
[^tel-alpha8se]: Semiconductor Online, *Thermal Processing Applications —
    Alpha-8SE* (Tokyo Electron America product description), undated,
    accessed 2026-09-13.
    <https://www.semiconductoronline.com/doc/thermal-processing-applications-alpha-8se-0001>
[^aviza-avp]: Moov used-equipment marketplace, *Aviza / SVG / Thermco AVP
    8000* listing, accessed 2026-08-30; re-checked 2026-09-13.
    <https://moov.co/marketplace/furnaces-diffusion/aviza-svg/aviza-asml-svg-watkinsjohnson-avp-8000>
[^asm-a400]: ASM International, *ASM International N.V. launches A400 DUO
    vertical furnace system*, press release, 2019-11-11; Wayback Machine
    capture of 2024-10-14.
    <https://web.archive.org/web/20241014215529/https://www.asm.com/press-releases/asm-international-nv-launches-a400-duo-vertical-furnace-system-1944469>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; furnace entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^roenigk-1987]: K. F. Roenigk and K. F. Jensen, "Low Pressure CVD of
    Silicon Nitride", *Journal of The Electrochemical Society*
    **134**(7), 1777–1785 (1987). <https://doi.org/10.1149/1.2100756>
[^pat-lpcvd-kokusai]: K. Maeda, S. Kakizaki, T. Taniyama, H. Yanagawa and
    K. Suzaki (Kokusai Electric), *Vertical furnace of a semiconductor
    manufacturing apparatus and a boat cover thereof*, US 5,902,103 A,
    filed 1996-12-23, granted 1999-05-11.
    <https://patents.google.com/patent/US5902103A/en>
[^pat-lpcvd-nec]: T. Usami (NEC), *Vertical low pressure CVD apparatus
    with an adjustable nozzle*, US 5,503,678 A, filed 1994-11-04, granted
    1996-04-02. <https://patents.google.com/patent/US5503678A/en>
[^meyerson-1984]: B. S. Meyerson and W. Olbricht, "Phosphorus-Doped
    Polycrystalline Silicon via LPCVD: I. Process Characterization",
    *Journal of The Electrochemical Society* **131**(10), 2361–2365
    (1984). <https://doi.org/10.1149/1.2115258>
[^adams-1979]: A. C. Adams and C. D. Capio, "The Deposition of Silicon
    Dioxide Films at Reduced Pressure", *Journal of The Electrochemical
    Society* **126**(6), 1042–1046 (1979).
    <https://doi.org/10.1149/1.2129171>
[^wiki-sin]: Wikipedia, *Silicon nitride*.
    <https://en.wikipedia.org/wiki/Silicon_nitride>
[^temple-boyer-1998]: P. Temple-Boyer, C. Rossi, E. Saint-Etienne and
    E. Scheid, "Residual stress in low pressure chemical vapor
    deposition SiNₓ films deposited from silane and ammonia", *Journal
    of Vacuum Science & Technology A* **16**(4), 2003–2007 (1998).
    <https://doi.org/10.1116/1.581302>
[^aviza-satin-2004]: Aviza Technology, *Aviza Technology Introduces New
    Low Temperature Silicon Nitride Process* ("New Satin Process Aimed at
    Sub-90nm DRAM and Logic IC Manufacturing"), press release, 2004-11-29;
    Wayback Machine capture of 2005-03-09.
    <https://web.archive.org/web/20050309110319/http://www.avizatechnology.com/news/pressrel/113004.htm>
[^kinsbron-1983]: E. Kinsbron, M. Sternheim and R. Knoell,
    "Crystallization of amorphous silicon films during low pressure
    chemical vapor deposition", *Applied Physics Letters* **42**(9),
    835–837 (1983). <https://doi.org/10.1063/1.94080>
[^harbeke-1984]: G. Harbeke, L. Krausbauer, E. F. Steigmeier,
    A. E. Widmer, H. F. Kappert and G. Neugebauer, "Growth and Physical
    Properties of LPCVD Polycrystalline Silicon Films", *Journal of The
    Electrochemical Society* **131**(3), 675–682 (1984).
    <https://doi.org/10.1149/1.2115672>
[^aviza-vert]: Aviza Technology, *Vertical Processors*, product page,
    2005; Wayback Machine capture of 2005-11-08.
    <https://web.archive.org/web/20051108133056/http://www.avizatechnology.com/products/vert.htm>
[^asm-vf]: ASM International, *Vertical furnace*, product page, accessed
    2026-09-13. <https://www.asm.com/our-technology-products/vertical-furnace>
[^teasdale-2001]: D. Teasdale, Y. Senzaki, R. Herring, G. Hoeye,
    L. Page and P. Schubert, "LPCVD of Silicon Nitride from
    Dichlorosilane and Ammonia by Single Wafer Rapid Thermal
    Processing", *Electrochemical and Solid-State Letters* **4**(5),
    F11 (2001). <https://doi.org/10.1149/1.1359056>
[^smith-2005]: J. W. Smith, S. M. Seutter and R. S. Iyer, "Thermal
    Chemical Vapor Deposition of Bis(Tertiary-Butylamino)Silane-based
    Silicon Nitride Thin Films", *Journal of The Electrochemical
    Society* **152**(4), G316 (2005). <https://doi.org/10.1149/1.1870792>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
