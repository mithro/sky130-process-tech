(machine-downstream-plasma-asher)=
# Downstream plasma asher

A downstream plasma asher is the single-wafer tool a fab uses to burn
photoresist off wafers after it has served as an implant or etch mask.
It generates an oxygen-based plasma away from the wafer and lets only
the neutral reactive species reach it, so that the resist is oxidised
without the ion bombardment and charging that a plasma in contact with
the wafer would bring. It is one of the most heavily used tools in a
fab: a strip follows nearly every masked implant and etch. This
page describes the class in general, lists representative 200 mm-era
models, and then says what SkyWater has published about its own tools
of this class and which SKY130 steps this reference assigns to it. The
chemistry of ashing and of the implant crust is on the
{ref}`strip category page <category-strip>`.

| | Downstream plasma asher |
|---|---|
| What it does | Removes photoresist in a remote plasma: ashing is "the process of removing the photoresist … from an etched wafer" with a reactive species, "Oxygen or fluorine" the most common;[^wiki-ash] downstream removal "generates the plasma gases outside of the process chamber in order to minimize bombardment of the substrate surface".[^snf-strip] |
| Plasma source | Microwave or RF, upstream of the wafer: the GaSonics L3510 runs "0–1200 watts at 2.45 GHz";[^gasonics-l3510] Mattson's Aspen Strip uses "proprietary inductively coupled plasma, or ICP, source technologies";[^mattson-2001] a used GaSonics PEP Iridia module carries both an "Astex Microwave Generator" and an "ENI ACG-5XL RF Generator".[^semistar-iridia] |
| Gases | O₂ and N₂, with forming gas, H₂, CF₄ or water vapour for particular residues; 10 % N₂ doubled both the atomic-oxygen density and the ashing rate in Fujimura et al.'s downstream study.[^fujimura-1990] |
| Wafer temperature | Lamp or platen heated: "Platen Temperature: 100–300°C" on the L3510;[^gasonics-l3510] "150-300" °C (typical) on the Aura 1000, with "Three 1KW lamps".[^gasonics-aura] |
| Wafer handling and throughput | Single wafer or two wafers per chamber: the Aura 1000 is a "single-wafer photoresist asher" at "Up to 90 wph";[^gasonics-aura] on the Aspen II Strip "Each chamber processes two wafers at a time", at 90–130 wafers per hour with one chamber.[^mattson-2001] |
| 200 mm era | GaSonics Aura (the Aura 1000 for 75–150 mm wafers) and L3510 (75–200 mm)[^gasonics-l3510][^gasonics-aura] and PEP Iridia lines, continued by Novellus after it bought GaSonics;[^sst-novellus-spec-2006] Mattson Aspen II Strip.[^mattson-2001] |
| SkyWater-listed tool | Under "Resist removal/cleans": "Gasonic PEP, remote microwave plasma, N2, O2, 120C – 270C", "Iridia RF microwave, N2, O2, H2, CF4, NH3, H2/N2, 40C-270C", "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to 250C"[^skw-01] |
| SKY130 steps | 14 steps, plus 1 where the class is an alternative and 22 where it strips the resist after an etch; see {ref}`SKY130 steps assigned to this class <machine-downstream-plasma-asher-steps>` |

## What the machine class is and how it works

An asher turns resist — a hydrocarbon polymer — into volatile products
with atomic oxygen, which a plasma supplies. "Originally, plasma was
generated in the process chamber, but as the need to get rid of the ions
has increased, many machines now use a downstream plasma configuration,
where plasma is formed remotely and the desired particles are channeled
to the wafer"; neutral atomic oxygen survives the trip better than
charged species, although "a large portion of the active species is
lost to recombination", which heating the wafer partly
offsets.[^wiki-ash] What makes a machine a *downstream* asher is that
separation, together with wafer heating, gas chemistry for residues and
crusts, and an optical endpoint. Lam's microwave stripper for a metal
etcher put the benefit in one phrase: its "down-stream plasma source"
eliminates "the potential for charge-induced damage of thin gate
oxides".[^lam-9600se-stripper-1998]

### Plasma generation

In a microwave asher, gas flows through a dielectric tube in a
microwave cavity. The GaSonics Aura 1000 has two interconnected vacuum chambers
("reaction and stripping"), a microwave plasma generator, mass flow
controllers and "an infrared heat source";[^gasonics-aura] Stanford's Aura description says the mixture
"flows downstream to the process chamber where it reaches a state of
'afterglow,' where it is highly reactive and no longer electrically
active or damaging to the wafer surface".[^snf-aura] Microwave
leakage from the cavity is an engineering problem of its own: a Fusion
Systems patent adds "a microwave trap proximate the opening through
which the plasma tube exits the microwave cavity".[^pat-asher-fusion]
Mattson took the other route, a remote inductively coupled source,
introduced "in 1997 to further extend the capability for removal of
the most difficult residues", and designed "for advanced semiconductor
device manufacturing processes of 0.18 micron and below".[^mattson-2001]
Some tools combine the two: the used PEP Iridia modules in a reseller's
listing each carry a microwave generator and an RF
generator,[^semistar-iridia] and ULVAC's cold strip process runs "an
RIE process and a downstream microwave process" sequentially or
simultaneously.[^pat-strip-ulvac]

### Gas distribution and wafer heating

Below the source, the plasma products are spread over the wafer. An
Axcelis patent flows the downstream plasma "through the baffle plate
assembly" and cools the baffle plates with gas.[^pat-asher-axcelis] The
wafer is heated by lamps or a platen: the L3510 lists "programmable
lamp and platen heating",[^gasonics-l3510] the Aura 1000 "Closed loop
temperature control with RTP technology",[^gasonics-aura] and Stanford's
Aura "Wafers heated by lamps".[^snf-aura] Higher temperature raises the
rate, but on implanted resist it risks popping the crust; Tseng, Chao
and Tsai strip "The implant-hardened surface … at a lower temperature
(<220° C.) to prevent popping problem" and the bulk "at a higher
temperature (>220° C.)".[^pat-strip-mosel]

### Chemistry for residues and crusts

Oxygen alone does not remove everything. Nitrogen added to the oxygen
raises the atomic-oxygen density: "the role of nitrogen as the additive
impurity gas is only to increase oxygen in the plasma".[^fujimura-1990]
Resist that has masked a high-dose implant carbonises; Fujimura et al.
found that "A decrease in the etching rate of the high-dose
ion-implanted resist was caused by carbonization", that residues were
"oxide of the implanted species", and developed a two-step process of
"H₂ RIE and downstream ashing".[^fujimura-1989] Horsky traced an abrupt
change in resist outgassing to amorphisation above a critical dose,
which he put at 4.5 × 10¹⁴ cm⁻² for a 150 kV phosphorus source/drain
implant.[^horsky-1998] Water
vapour protects the gate oxide from the resist's sodium: an O₂ + H₂O
downstream ash left sodium in the oxide "nearly the same as that in the
SiO₂ layer as grown", most effectively at 40–60 % H₂O.[^fujimura-1994]
Fluorine additions attack the substrate as well as the resist: TSMC's patent uses
O₂ with CH₃F or CH₂F₂ for "a photoresist with a carbonized crust" while
"reducing thickness loss in exposed oxide, polysilicon, and silicon
layers compared with conventional methods that employ O₂ and CₘFₙ
gases",[^pat-strip-tsmc] and Kastenmeier et al.'s downstream CF₄/O₂
plasmas etched nitride and oxide.[^kastenmeier-1996] Mattson offered
"a wide range of hydrogen and fluorine chemistries" for cleaning vias
with exposed low-k films;[^mattson-2001] Axcelis patented an
"essentially oxygen free and nitrogen free" chemistry for the
same purpose.[^pat-asher-axcelis]

### Endpoint and over-ash

The strip is run to an optical endpoint and a timed over-ash. The Aura
1000 sequence ends "When end-point detection is reached and overstrip
is achieved", after which the gases are turned off and the chamber
purged.[^gasonics-aura] Wikipedia notes that spectral lines can fall as
the process ends, or rise "as the available reactants are
consumed".[^wiki-ash]

## Representative 200 mm-era models

* **GaSonics International** ("Photoresist removal and wafer cleaning
  processes" among its applications in 2000[^gasonics-2000]). The Aura
  1000 for 75–150 mm wafers, with ">320 systems in production" in a reseller's
  description;[^gasonics-aura] the L3510, "a production-proven downstream
  plasma photoresist ashing system" for 75–200 mm wafers;[^gasonics-l3510]
  and the PEP Iridia line, whose modules pair microwave and RF
  generators.[^semistar-iridia] Solid State Technology reported on
  2000-10-27 that Novellus "is acquiring" GaSonics, "a supplier of dry
  resist removal and surface preparation equipment", in a stock-for-stock
  merger "valued at approximately $347 million";[^sst-gasonics-2000] a
  2006 report refers to "Novellus' 2001 purchase of GaSonics" and
  reports that Novellus had just licensed the Aura 1000/2000LL and L3510 designs to a
  refurbisher while keeping the "Gamma and PEP Iridia lines".[^sst-novellus-spec-2006]
* **Mattson Technology.** The Aspen II Strip and Aspen III Strip on the
  "Aspen II platform" and "Aspen III platform", with ICP sources; Mattson
  wrote that strip "is used in as many as 25 steps during IC production"
  and that its Aspen Strip had "become the number one strip choice in
  Taiwan".[^mattson-2001]
* **Etch-platform strippers.** Lam's microwave stripper option for the
  TCP 9600SE metal etcher[^lam-9600se-stripper-1998] and Applied
  Materials' ASP strip chamber on its metal etch systems.[^amat-300-etch-2000]
* **Other vendors.** The step pages also name Axcelis/Fusion ES and PSK
  ashers ({ref}`DNIS <step-009>`); the Fusion and Axcelis patents above
  describe their technology, but no product description was retrieved for
  this page.

## At SkyWater

### What SkyWater lists

Under "Resist removal/cleans", SkyWater's *Facilities & Capabilities*
page lists three plasma strip tools before its wet benches:[^skw-01]

> "Gasonic PEP, remote microwave plasma, N2, O2, 120C – 270C"
>
> "Iridia RF microwave, N2, O2, H2, CF4, NH3, H2/N2, 40C-270C"
>
> "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to 250C"

Read term by term: the PEP entry is a remote microwave plasma with N₂
and O₂ from 120 °C to 270 °C; the Iridia entry adds H₂, CF₄, NH₃ and
H₂/N₂ and reaches down to 40 °C; the Aspen entry is an RF plasma with O₂,
CF₄ and hydrogen in nitrogen, to 250 °C.[^skw-01] SkyWater spells the
vendor "Gasonic" and writes "Aspen2", which we read as the Aspen II
Strip (an inference from the name); it names no vendor for the
Iridia. A trade report lists the "PEP Iridia" among the GaSonics lines
Novellus kept,[^sst-novellus-spec-2006] so we read the PEP and Iridia
entries as GaSonics tools, possibly of one family; that is an inference.
We read "H2>N2" as hydrogen in nitrogen (forming gas); SkyWater does not
expand it. The "RF microwave" wording matches a used PEP Iridia module
that carries both generator types,[^semistar-iridia] but SkyWater gives
no configuration.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>`
the three listings are **strong**: they are SkyWater
statements.[^skw-01] The caveats that apply to every listed tool are
under {ref}`Reading the SkyWater evidence <machines-reading-evidence>`.
For this class the listings are strong for the gases and temperature
ranges; which tool strips which resist is not stated, and the step
pages' choices rest on those ranges.

(machine-downstream-plasma-asher-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a downstream plasma
asher as the tool or one of two options, then the step where it is an
alternative, then the steps where it strips the resist after an etch
(identical to the {ref}`machines index <machines-index>` table):

{ref}`DNIS <step-009>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`; *alternative:* {ref}`TUNARCE <step-036>`; *also for the strip after an etch:* {ref}`STIE <step-006>`, {ref}`TUNME <step-039>`, {ref}`ONOME <step-042>`, {ref}`GOXETCH <step-046>`, {ref}`P1ME <step-062>`, {ref}`NPCME <step-079>`, {ref}`SACETCH <step-095>`, {ref}`LI1ME <step-103>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`VIM3E <step-145>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`VIM4E <step-160>`, {ref}`MM5E <step-163>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Gasonic PEP …", "Iridia RF microwave …", "Mattson Aspen2 …"** — *inference (which of the three not stated):* {ref}`DNIS <step-009>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`; *inference, the Iridia fitting a crust step best:* {ref}`P1IS <step-051>`, {ref}`ASTIS <step-067>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`; *weak:* {ref}`TUNARCE <step-036>`; *strong (strip after an etch):* {ref}`STIE <step-006>`; *strong for existence (strip after an etch):* {ref}`TUNME <step-039>`, {ref}`ONOME <step-042>`, {ref}`GOXETCH <step-046>`, {ref}`P1ME <step-062>`, {ref}`NPCME <step-079>`, {ref}`LICM1E <step-094>`, {ref}`SACETCH <step-095>`, {ref}`LI1ME <step-103>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`VIM3E <step-145>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`VIM4E <step-160>`, {ref}`MM5E <step-163>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>`

The one choice between the three rests on the listed ranges: the Iridia
entry is the only one with a 40 °C lower limit and the only one
listing NH₃, and it has H₂ and H₂/N₂, the conditions the crust-strip pages want for a cool first
stage.[^skw-01] The {ref}`DNIS <step-009>` and
{ref}`LVTPIS <step-021>` pages describe a crust from MeV well implants
but make no choice; the {ref}`machines index <machines-inconsistencies>`
records the difference.

## Consumables and facilities

The process gases and etch gases are described on the
{ref}`process gases <material-process-gases>` and
{ref}`etch and chamber-clean gases <material-etch-gases>` pages.
The strip gases are listed in the {ref}`materials index
<materials-index>`; what is specific to an asher is summarised here.
None of the SkyWater sources describes the fab's gas delivery or
exhaust. Forming gas as an ash ambient is described on the
{ref}`anneal ambients <material-anneal-ambients>` page.

* **Gases.** O₂ and N₂ for the bulk ash; forming gas, H₂, NH₃ and CF₄ on
  the Iridia and Aspen entries;[^skw-01] a used PEP Iridia module lists
  "CF4, N2, 4 percent H2/N2, O2" among its gas lines.[^semistar-iridia]
  Wikipedia gives N₂/H₂ "where the H₂ portion is 2%" as another ashing
  gas.[^wiki-ash]
* **Microwave and RF parts.** Magnetrons or RF generators, and the quartz
  or ceramic plasma tube: the Aura 1000 offers a "Quartz or Ceramic plasma
  chamber".[^gasonics-aura] Microwave traps keep the energy in the
  cavity.[^pat-asher-fusion]
* **Heating lamps and platens.** The Aura 1000's "Three 1KW lamps"
  and the L3510's lamp and platen heaters are service
  items.[^gasonics-aura][^gasonics-l3510]
* **Wet follow-up.** Most strips end on a
  {ref}`wet bench <machine-wet-bench>`, which removes the inorganic
  residue the ash leaves; Tseng, Chao and Tsai finish with "ammonium
  hydroxide and hydrogen peroxide".[^pat-strip-mosel]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's strip recipes are not public.

* **Fourteen implant strips.** Every implant mask from
  {ref}`DNIS <step-009>` to {ref}`NSDIS <step-087>` ends with a strip
  on this class. The high-dose strips ({ref}`P1IS <step-051>`,
  {ref}`ASTIS <step-067>`, {ref}`PDIS <step-084>`,
  {ref}`NSDIS <step-087>`) face a carbonised crust whose removal needs
  a cool first step or a hydrogen chemistry;[^fujimura-1989][^pat-strip-mosel]
  the pages read the Iridia's 40 °C floor and H₂/N₂ as fitting that
  step.[^skw-01]
* **Crust from deep implants.** The {ref}`DNIS <step-009>` and
  {ref}`LVTPIS <step-021>` pages describe a crust from MeV implants
  through thick resist; implant outgassing studies relate resist
  outgassing to dose, energy, beam current and thickness,[^horsky-1998][^lee-1996] but no
  public source ties a crust thickness to these implants.
* **Fluorine in the ash.** CF₄ in a downstream plasma etches nitride
  and oxide,[^kastenmeier-1996] and the {ref}`LICM1E <step-094>` page
  reads the post-etch polymer clean on the Aspen without its CF₄, which
  would attack the silicon at the contact floor (inference).
* **Strips after etch.** After the masked etches the step pages name
  the three ashers for the resist strip, except after
  {ref}`TUNARCE <step-036>`, whose resist stays on for the
  {ref}`PTSI <step-037>` and {ref}`DEPI <step-038>` implants and the
  {ref}`TUNME <step-039>` wet etch; after a metal etch the strip
  also removes chlorine-bearing polymer, a job that some metal-etch platforms do in an
  integrated downstream chamber.[^lam-9600se-stripper-1998][^amat-300-etch-2000]
* **The organic ARC option.** The {ref}`TUNARCE <step-036>` page names
  a timed, isotropic ash as the alternative to a plasma etch for opening
  a thin organic ARC, and grades the ashers weak for it.
* **Charging and sodium.** Downstream operation avoids charge damage to
  thin gate oxides,[^lam-9600se-stripper-1998] and water-vapour ashing
  keeps sodium from the resist out of them.[^fujimura-1994]

## Related pages

* {ref}`category-strip` — ashing, the implant crust and wet strips, and
  the 15 strip steps of SKY130.
* {ref}`machine-wet-bench` — the wet clean that follows most strips.
* {ref}`category-implant` — the implants whose resist this tool
  removes.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — strip gases.
* {ref}`material-anneal-ambients` — forming gas in anneals and
  ashers.
* {ref}`material-process-gases` — nitrogen, oxygen, hydrogen, argon,
  helium and the oxidation additives, their grades and SkyWater's listed
  gases.
* {ref}`material-etch-gases` — fluorocarbon, fluoride, chlorine and
  bromine etch and chamber-clean gases.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

**Related patents.**

* {ref}`Plasma asher with microwave trap <patent-gp22748832>` — US 5,498,308 A (1994)
* {ref}`Cold processes for cleaning and stripping photoresist from surfaces of semiconductor wafers <patent-gp26794054>` — US 5,795,831 A (1996)
* {ref}`Low temperature dry process for stripping photoresist after high dose ion implantation <patent-gp25102092>` — US 5,811,358 A (1997)
* {ref}`Method of ashing a photoresist <patent-gp33298522>` — US 2004/0214448 A1 (2003)
* {ref}`Apparatus and plasma ashing process for increasing photoresist removal rate <patent-gp35448183>` — US 7,449,416 B2 (2004)

**Related papers.**

* {ref}`paper-grover-2019a` — Sidhant Grover and Philip Thompson, ASMC 2019 (affiliation inference)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the three
  "Resist removal/cleans" plasma entries quoted on this page.[^skw-01]
* SemiStar, *Gasonics L3510 plasma asher* — microwave power, platen
  temperature and wafer range of a GaSonics asher.[^gasonics-l3510]
* Allwin21, *Gasonics Aura 1000 Plasma Asher* — the two-chamber
  microwave design, lamps, temperature range and
  sequence.[^gasonics-aura]
* SemiStar, *Novellus Gasonics PEP Iridia DL Plasma Asher* — the
  generators and gas lines of a PEP Iridia system.[^semistar-iridia]
* Mattson Technology, *The Aspen Strip* (2001) — the Aspen II and III
  Strip platforms, ICP source and chemistries.[^mattson-2001]
* GaSonics International, home page (2000) — the vendor's name and
  applications.[^gasonics-2000]
* Solid State Technology, *Novellus acquires Gasonics* (2000) — the
  acquisition and GaSonics's business.[^sst-gasonics-2000]
* Solid State Technology, *Novellus licenses–not sells–legacy strip
  tools to SPEC* (2006) — the GaSonics product lines, including PEP
  Iridia.[^sst-novellus-spec-2006]
* Kamarehi and Simpson (Fusion Systems), US 5,498,308 — the microwave
  trap of a downstream asher.[^pat-asher-fusion]

### High-level understanding

* Wikipedia, *Plasma ashing* — downstream configuration, recombination,
  descum and implanted resist.[^wiki-ash]
* Stanford Nanofabrication Facility, *Downstream/Remote Plasma Resist
  Removal* — the class in a university fab.[^snf-strip]
* Stanford Nanofabrication Facility, *Gasonics Aura Asher* — the
  afterglow description of a GaSonics tool.[^snf-aura]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — resist
  strip as a fab operation.[^txt-07]

### Deep dive

* Fujimura et al., *JJAP* 1989 — carbonised implanted resist, its
  residues and a two-step strip.[^fujimura-1989]
* Fujimura et al., *JJAP* 1990 — why nitrogen raises the downstream
  ashing rate.[^fujimura-1990]
* Fujimura et al., *JVST B* 1994 — O₂ + H₂O downstream ashing against
  sodium contamination.[^fujimura-1994]
* Horsky, IIT 1998 — resist outgassing and the critical dose for
  amorphisation in implantation.[^horsky-1998]
* Lee et al., IIT 1996 — thick-resist outgassing during MeV
  implantation.[^lee-1996]
* Kastenmeier et al., *JVST A* 1996 — downstream CF₄/O₂/N₂ etching of
  nitride and oxide.[^kastenmeier-1996]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — a two-temperature
  dry strip after high-dose implantation.[^pat-strip-mosel]
* Chan, Chiu and Tao (TSMC), US 2004/0214448 — a CₓHᵧF_z/O₂ ash for the
  carbonised crust.[^pat-strip-tsmc]
* Nakayama et al. (ULVAC), US 5,795,831 — cold RIE and downstream
  microwave stripping.[^pat-strip-ulvac]
* Becknell, Hammar and Ferris (Axcelis), US 7,449,416 — an oxygen- and
  nitrogen-free downstream ash through cooled baffle
  plates.[^pat-asher-axcelis]
* Lam Research, TCP 9600SE microwave stripper announcement (1998) — an
  etch-integrated downstream stripper and its charging and corrosion
  tests.[^lam-9600se-stripper-1998]
* Applied Materials, 300 mm etch product line press release (2000) — the
  ASP-based strip and passivation chamber.[^amat-300-etch-2000]
* Kern, *JES* 1990 — the wet cleaning that follows the
  ash.[^kern-1990]

## Open questions

* Which of SkyWater's three ashers strips which resist is not
  stated;[^skw-01] the step pages' choices are inferences from the
  listed gases and temperatures.
* Whether the "Gasonic PEP" and "Iridia" entries are one GaSonics family
  in two configurations, and what "H2>N2" denotes exactly, are not
  stated.
* The model list above is incomplete: it covers the GaSonics and Mattson
  tools for which a public description was found, not the Axcelis/Fusion,
  PSK and other ashers of the period.

<!-- footnotes -->

[^wiki-ash]: Wikipedia, *Plasma ashing*.
    <https://en.wikipedia.org/wiki/Plasma_ashing>
[^snf-strip]: Stanford Nanofabrication Facility, *Downstream/Remote
    Plasma Resist Removal*, equipment guide.
    <https://snfguide.stanford.edu/guide/equipment/purpose/cleaning/resist-removal/dry-resist-removal/downstreamremote-plasma-resist-removal>
[^gasonics-l3510]: SemiStar Corp., *Gasonics L3510 plasma asher* (tool
    description; platen temperature 100–300 °C).
    <http://www.semistarcorp.com/product/gasonics-l3510-asher/>
[^mattson-2001]: Mattson Technology, *The Aspen Strip*, product page;
    Wayback Machine capture of 2001-12-19.
    <https://web.archive.org/web/20011219013713/http://www.mattson.com/products/aspen_strip.html>
[^semistar-iridia]: SemiStar Corp., *Novellus Gasonics PEP Iridia DL
    Plasma Asher* (used-equipment listing), accessed 2026-09-13.
    <http://www.semistarcorp.com/product/novellus-gasonics-pep-iridia-dl-plasma-asher/>
[^fujimura-1990]: S. Fujimura, K. Shinagawa, M. Nakamura and H. Yano,
    "Additive Nitrogen Effects on Oxygen Plasma Downstream Ashing",
    *Japanese Journal of Applied Physics* **29**(10R), 2165 (1990).
    <https://doi.org/10.1143/JJAP.29.2165>
[^gasonics-aura]: Allwin21, *Gasonics Aura 1000 Plasma Asher*
    (specification summary; temperature 150–300 °C typical).
    <https://allwin21.com/gasonics-aura-1000-plasma-asher-2/>
[^sst-novellus-spec-2006]: Solid State Technology, *Novellus
    licenses–not sells–legacy strip tools to SPEC*, 2006-10-19.
    <https://sst.semiconductor-digest.com/2006/10/novellus-licenses-not-sells-legacy-strip-tools-to-spec/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; resist removal entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^lam-9600se-stripper-1998]: Lam Research Corporation, *Lam Research
    Introduces Microwave Stripper for High-Density Metal Etch System*,
    news item, Semiconductor Online, 1998-01-09.
    <https://www.semiconductoronline.com/doc/lam-research-introduces-microwave-stripper-fo-0001>
[^snf-aura]: Stanford Nanofabrication Facility, *Gasonics Aura Asher
    (gasonics)*, equipment page, accessed 2026-09-13.
    <https://snfguide.stanford.edu/guide/equipment/gasonics-aura-asher-gasonics>
[^pat-asher-fusion]: M. Kamarehi and J. E. Simpson (Fusion Systems),
    *Plasma asher with microwave trap*, US 5,498,308 A, granted
    1996-03-12.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5498308>
[^pat-strip-ulvac]: I. Nakayama et al. (ULVAC Technologies), *Cold
    processes for cleaning and stripping photoresist from surfaces of
    semiconductor wafers*, US 5,795,831 A, granted 1998-08-18.
    <https://patents.google.com/patent/US5795831A/en>
[^pat-asher-axcelis]: A. F. Becknell, P. Hammar and D. Ferris (Axcelis
    Technologies), *Apparatus and plasma ashing process for increasing
    photoresist removal rate*, US 7,449,416 B2, granted 2008-11-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7449416>
[^pat-strip-mosel]: M.-S. Tseng, F.-H. Chao and N.-Y. Tsai (Mosel
    Vitelic), *Low temperature dry process for stripping photoresist
    after high dose ion implantation*, US 5,811,358 A, granted
    1998-09-22. <https://patents.google.com/patent/US5811358A/en>
[^fujimura-1989]: S. Fujimura, J. Konno, K. Hikazutani and H. Yano,
    "Ashing of Ion-Implanted Resist Layer", *Japanese Journal of Applied
    Physics* **28**(10R), 2130 (1989).
    <https://doi.org/10.1143/JJAP.28.2130>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy and
    high current ion implantation", *Proc. 1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
[^fujimura-1994]: S. Fujimura, M. T. Suzuki, K. Shinagawa and M.
    Nakamura, "Sodium contamination free ashing process using O₂+H₂O
    plasma downstream", *Journal of Vacuum Science & Technology B*
    **12**(4), 2409–2413 (1994). <https://doi.org/10.1116/1.587773>
[^pat-strip-tsmc]: B.-W. Chan, Y.-H. Chiu and H.-J. Tao (TSMC), *Method
    of ashing a photoresist*, US 2004/0214448 A1, published 2004-10-28.
    <https://patents.google.com/patent/US20040214448A1/en>
[^kastenmeier-1996]: B. E. E. Kastenmeier, P. J. Matsuo, J. J. Beulens
    and G. S. Oehrlein, "Chemical dry etching of silicon nitride and
    silicon dioxide using CF₄/O₂/N₂ gas mixtures", *Journal of Vacuum
    Science & Technology A* **14**(5), 2802–2813 (1996).
    <https://doi.org/10.1116/1.580203>
[^gasonics-2000]: GaSonics International, home page; Wayback Machine
    capture of 2000-03-01.
    <https://web.archive.org/web/20000301102837/http://www.gasonics.com:80/>
[^sst-gasonics-2000]: Solid State Technology, *Novellus Acquires
    Gasonics*, 2000-10-27.
    <https://sst.semiconductor-digest.com/2000/10/novellus-acquires-gasonics/>
[^amat-300-etch-2000]: Applied Materials, *Applied Materials Unveils
    300mm Etch Product Line*, press release, 2000-07-10.
    <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-unveils-300mm-etch-product-line>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
