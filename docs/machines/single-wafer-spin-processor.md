(machine-single-wafer-spin-processor)=
# Single-wafer spin processor

A single-wafer spin processor is the wet tool a fab uses when a batch
bath is too blunt: it holds one wafer on a rotating chuck inside a
closed chamber, dispenses an etchant or cleaning chemical onto the
spinning surface, spins the liquid off into a collecting ring, rinses
and spins the wafer dry. Because a gas cushion between chuck and wafer
can keep the liquid off the side facing the chuck, the chemistry can be
kept to one side, which makes the class the natural tool for removing films from the back of a wafer
as well as for short HF etches and for cleans after etch or polish.
This page describes the class in general, lists representative
200 mm-era models, and then says what SkyWater has published about its
own tools of this class and which SKY130 steps this reference assigns
to it. Wet etch and clean chemistry is on the
{ref}`etch <category-etch>` and {ref}`strip <category-strip>` category
pages; batch wet tools are on the {ref}`wet bench page
<machine-wet-bench>`.

| | Single-wafer spin processor |
|---|---|
| What it does | Wet etching, film removal and cleaning of one wafer at a time. SEZ introduced its Spin-Processor 223 "for high throughput cleaning and film removal applications", including "backside, bevel/edge and frontside exclusion zone copper decontamination" and "frontside film removal applications".[^sez-223-pr] |
| Wafer holding | A support with an annular nozzle "chargeable with compressed gas for the formation of a gas cushion between the support (1) and the silicon wafer (11), the gas exiting between the wafer (11) and the support (1) preventing passage of treatment fluid onto the underside of the wafer".[^pat-spin-sez] |
| Dispense and spin-off | "the remover is dispensed from above and across the rotating wafer by a moving dispense arm" and "immediately spun off into the process chamber where it can be re-circulated"; a multi-stack chamber separates "several chemical and rinse levels".[^sez-polymer-1999] |
| Chemistries | Dilute HF;[^hattori-1998] HF/HNO₃ for silicon;[^oinoue-2018] an "H2O:H2O2:H2SO4:HF mixture" for backside cleaning;[^broussous-2005] DSP+, a "dilute sulfuric-peroxide-HF mixture" for post-etch residues;[^lee-2012-dsp] solvents.[^sez-polymer-1999] |
| Throughput | The 223 "can process 80 or more wafers per hour and use up to three chemistries";[^sez-223-pr] the four-chamber 8200 up to "200 wafers per hour".[^sez-8200-2001] |
| 200 mm era | SEZ's 223, "a robot that transports 200mm wafers from four cassettes to two identical process chambers",[^sez-223-moov] and its four-chamber 4200 and 8200;[^sez-polymer-1999][^sez-8200-2001] the Da Vinci, first sold in 2004,[^sez-2005] for "200- and 300-mm wafers".[^sez-davinci-2008] |
| SkyWater-listed tool | "Single Wafer": "SEZ223, Davinci, HF, DSP+HF, titration controlled";[^skw-01] a caption naming "a SEZ etcher tool"[^skw-07] |
| SKY130 steps | 4 steps, plus 14 where it runs a clean; see {ref}`SKY130 steps assigned to this class <machine-single-wafer-spin-processor-steps>` |

## What the machine class is and how it works

A batch wet tool moves many wafers through the same liquid; a spin
processor brings fresh liquid to one wafer and throws it off again.
SEZ put the difference in terms of transport and redeposition: its 8200
"eliminates redeposition and cross-contamination because chemicals are
spun off the wafer surface and the wafers are not touched during
transport".[^sez-8200-2001] Gaulhofer et al. of SEZ and EKC contrasted
static immersion tanks, which offer "no mechanical velocity", and spray
batch processors with the spin processor's "rapid exchange of the
chemical on the surface".[^sez-polymer-1999] What makes a machine a
production spin processor is the engineering around that: a chuck that
holds the wafer without contaminating the side not being treated,
dispense and collection that keep several chemicals apart, rinsing and
drying in the same chamber, and chemical supply held at a known
concentration.

### Chuck and one-sided processing

An SEZ patent of 1988 describes the chuck. The wafer rests on "a gas
cushion" formed by compressed gas from an annular nozzle, and "the gas
exiting between the wafer (11) and the support (1)" keeps the treatment
fluid off the underside; the support sits inside "an annular tank"
with "at least two annular ducts", and is lifted, lowered and rotated so
that each fluid runs into its own duct.[^pat-spin-sez] The description
states the aim as treating wafers "without having to protect the other
side of the slice-shaped articles, which is not to be treated, by means
of special measures from attack by the treatment fluid", and explains
that the gas leaving the nozzle blows fluid away from the rim so that it
"cannot pass onto the underside".[^pat-spin-sez] An SEZ application note
draws the practical consequence: the chemical spin etcher "requires no
protection for the device surface" and can remove "multilayer films
including oxide films, poly-Si and nitride films through one
process".[^kinoshita-sez] Later SEZ tools processed both faces at once:
the 8200 was "the first non-contact, single wafer, double sided cleaner
available on the market".[^sez-8200-2001]

### Dispense, spin-off and chamber levels

Chemical reaches the wafer from nozzles or a moving arm and leaves it by
centrifugal force. On a rotating disk an initially uniform liquid layer
stays uniform and irregular layers level out.[^emslie-1958] In the SEZ tool Gaulhofer et
al. describe, the stacked chamber keeps chemical and rinse levels apart,
and "A short high-speed spin-off step of the chemical before water rinse
removes excess chemical from the wafer surface, thus improving the
effectiveness of the DI water rinse and acts as a temporary stop for the
remover". Their post-etch residue cleans on 200 mm wafers ran for "10 to
120 seconds" at "400 to 800 rpm", with a remover flow of "0.8 to 2.0
liter/minute"; for a 30-second process they estimated "only 0.75 liter
of chemical and 0.5 liter of DI-water" per wafer, with the chemical
"re-circulated, filtered and re-used".[^sez-polymer-1999]

### Etching on a spinning wafer

An etch on a spinning wafer need not be uniform across it. For silicon in HF/HNO₃, a mixture that etches by oxidation
followed by dissolution,[^schwartz-1976] Oinoue et al. found that in a
single-spin process "Si etch rate distributions largely differ with
different HF/HNO3 concentrations", while oxide etch-rate distributions
stay similar, and traced the difference to consumption of HF or HNO₃
across the wafer.[^oinoue-2018] Short cycles become practical: Hattori
et al. cleaned wafers by "alternately supplying ozonized water and dilute
HF for only 10 s each onto a rotating silicon wafer through jet
nozzles",[^hattori-1998] and later removed particulate and metallic
contamination "in 20 s" with an ultra-dilute HF and nitrogen spray,
with silicon and oxide losses "below 0.003 and 0.03 nm".[^hattori-2007]
Nitride also etches in HF, by a mechanism that explains the "etch
selectivity between these two materials", nitride and oxide.[^knotter-2001] Dilute HF can
be monitored in line: Kikuyama et al. showed that conductivity "can be used to monitor the etching rate
… very accurately when the etching rate is relatively slow (around
1 Å/min)".[^kikuyama-1994]

### Residue removal and backside cleans

Published cleans of the class use solvents and acids. For residues after
a metal etch, SEZ and EKC used room-temperature semi-aqueous removers on
an SEZ spin processor, on "oxide/titanium/TiN/AlCu metal stack etched by
a LAM TCP9600 etcher", with cleaning times from 10 to 120 seconds and
blanket etch rates below 5 Å/min for AlCu.[^sez-polymer-1999] For
post-etch residues around metals, dilute sulphuric–peroxide with HF (DSP+) "is
currently used for the removal of post etch residues on device surface,
to replace the conventional SPM cleaning".[^lee-2012-dsp] A monitoring
system described by Fraunhofer IMM gives one DSP composition, "3.7 wt%
hydrogen peroxide (H2O2) and 8.5 wt% sulfuric acid (H2SO4) dissolved in
water", and names "150 ppm or 300 ppm" HF for DSP+.[^fraunhofer-dsp] On
the backside, Broussous et al. used an SEZ spin processor and "an
H2O:H2O2:H2SO4:HF mixture" to remove metals "by etching a few angstroms
of the wafer backside, whatever its coating".[^broussous-2005] An SEZ
note on post-CMP cleaning argues that compounds formed between
backside films and metals "are difficult to remove by either the brush
scrubber cleaning or the megasonic cleaning", and that wet etching of
the backside film removes particles and compounds together.[^kinoshita-sez]

### Charging and drying

Mui et al. modelled the surface charging of "a single-wafer wet spin
tool" as "the advection of surface charges from wafer-center to
wafer-edge resulting from the shear flow of the liquid", with charging
potentials that depend on radius, process time and spin
speed.[^mui-2011] The wafer is dried by spinning in the same chamber;
Gaulhofer et al. used "a spin-dry step for 15 seconds" after a DI
rinse.[^sez-polymer-1999]

## Representative 200 mm-era models

* **SEZ,** with headquarters in Villach, Austria.[^sez-8200-2001] The
  Spin-Processor 223, introduced in 1999 with "dual processing chambers
  and a small footprint design";[^sez-223-pr] a used-equipment listing
  describes the 200 mm tool, with options including "Film Removal End
  Point Detection" and applications from "Backside Film Removal" to
  "Oxide Etching" and "Post-CMP-Cleaning".[^sez-223-moov] The four-chamber
  4200, and the 8200 of 2001, "based on the company's Spin-Processor
  4200, with an incorporated double sided cleaning
  system".[^sez-8200-2001] The Da Vinci family, "Having sold the first
  Da Vinci tool in Q2 04";[^sez-2005] SEZ later described it as a
  platform for "back-end-of-line (BEOL) polymer cleaning and backside
  etch and clean" on "200- and 300-mm wafers", "Originally developed to
  address 90-nm technology nodes".[^sez-davinci-2008] In December 2007
  SEZ's board signed an agreement for a Lam Research tender offer, after
  which SEZ was to become "a new division within Lam with capabilities focused around single-wafer
  cleaning technology"; SEZ then had "an installed base of over 1,200
  tools".[^sez-lam-2007]
* **SCREEN (formerly Dainippon Screen).** The SP-2100 spin processor of
  2020, "able to process wafer sizes of up to 200 mm (8")" and equipped
  optionally for metal etching, is a current model of the
  class.[^screen-sp2100]
* **Other vendors.** The {ref}`BFR <step-060>` page also names SCP/Akrion
  spin tools; no vendor description of them was retrieved for this page.

## At SkyWater

### What SkyWater lists

Under "Resist removal/cleans", after the ashers, the Akrion bench and
the "Batch Rotational" solvent tool, SkyWater's *Facilities &
Capabilities* page lists:[^skw-01]

> "Single Wafer"
> – "SEZ223, Davinci, HF, DSP+HF, titration controlled"

Read term by term: we read "SEZ223" as SEZ's Spin-Processor
223;[^sez-223-pr] "Davinci" matches SEZ's Da Vinci
family,[^sez-davinci-2008] though the entry names no vendor for it;
"HF" names the etchant without a concentration; "DSP+HF"
we read as dilute sulphuric–peroxide with HF, the mixture published as
DSP+;[^lee-2012-dsp][^fraunhofer-dsp] and "titration controlled" we read
as chemical concentration held by titration, which the page does not
explain.[^skw-01] The entry does not say how many tools there are,
whether HF and DSP+HF run on both, what wafer size the Da Vinci takes,
or whether either tool has a backside or brush module. SkyWater's
maintenance-technician profile adds a caption in which a technician
"replaces a motor for a robot on a SEZ etcher tool";[^skw-07] the
{ref}`machines index <machines-index>` groups that tool with this class.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` the
listing is **strong** for an SEZ 223, a Da Vinci tool and the two
chemistries: it is a SkyWater statement, and the technician caption is
a second SkyWater statement that an SEZ tool is maintained
there.[^skw-01][^skw-07] The model identifications and the reading of
"DSP+HF" and "titration controlled" are ours. The Da Vinci was first
sold in 2004,[^sez-2005] so that entry at least describes a tool of a
later generation than the 223.
The caveats that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`.

(machine-single-wafer-spin-processor-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a single-wafer spin
processor as the tool or one of two options, then the steps where it
runs a clean (identical to the {ref}`machines index <machines-index>`
table):

{ref}`TUNME <step-039>`, {ref}`GOXETCH <step-046>`, {ref}`BFR <step-060>`, {ref}`SACETCH <step-095>`; *also for a clean:* {ref}`CMPNIT <step-012>`, {ref}`PWDEIS <step-033>`, {ref}`CTME <step-108>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`VIME <step-119>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`VIM2E <step-130>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`VIM3E <step-145>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Single Wafer", "SEZ223, Davinci, HF, DSP+HF, titration controlled"** — *inference (SEZ 223):* {ref}`BFR <step-060>`; *medium:* {ref}`SACETCH <step-095>`; *strong for existence:* {ref}`NS19 <step-013>`, {ref}`TUNME <step-039>`, {ref}`GOXETCH <step-046>`, {ref}`CTME <step-108>`, {ref}`VIME <step-119>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`; *named as the post-CMP clean; no brush scrubber named:* {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>`

Two step pages grade the assignment itself rather than only the tool's
existence: {ref}`BFR <step-060>` (an inference, resting on the SEZ press
release and the used-equipment listing naming film removal and backside
applications for the 223[^sez-223-pr][^sez-223-moov]) and
{ref}`SACETCH <step-095>` ("medium for a contact-hole clean"). The CMP pages name the SEZ tools for the
post-CMP clean because SkyWater names no brush scrubber; that clean is
described on the {ref}`post-CMP cleaner page
<machine-post-cmp-cleaner>`.

## Consumables and facilities

The process gases are described on the
{ref}`process gases <material-process-gases>` page.
The wet chemicals are described on the
{ref}`wet chemicals <material-wet-chemicals>` page and listed in the
{ref}`materials index <materials-index>`; what is specific to a spin processor is summarised
here. None of the SkyWater sources describes the tool's chemical supply
or exhaust. Ultrapure water, its standards and its quality parameters
are described on the {ref}`ultrapure water <material-ultrapure-water>`
page, and the chuck and nozzle consumables and acid waste that the BFR
page names are among the rows of the
{ref}`hardware consumables and abatement <material-hardware-consumables>`
page.

* **Acids and oxidisers.** Dilute HF;[^skw-01][^kikuyama-1994] sulphuric
  acid, hydrogen peroxide and HF for DSP and DSP+, at compositions such
  as those Fraunhofer IMM gives;[^fraunhofer-dsp][^broussous-2005] HF
  and nitric acid for silicon removal on the backside.[^oinoue-2018]
* **Solvents.** Post-etch residue removers of the semi-aqueous kind SEZ
  and EKC tested, recirculated and filtered.[^sez-polymer-1999]
* **Water and gases.** Ultrapure water for rinsing; nitrogen or other
  compressed gas for the chuck's gas cushion[^pat-spin-sez] and for
  purging and drying (industry practice).
* **Chemical control.** Concentration monitoring — conductivity for
  dilute HF,[^kikuyama-1994] optical monitoring for DSP,[^fraunhofer-dsp]
  and SkyWater's unexplained "titration controlled".[^skw-01]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's single-wafer recipes are not
public.

* **Backside film removal.** On the {ref}`BFR <step-060>` page's
  reading, the step strips the furnace films from the back of the wafer
  before the gate mask. The page reads
  the tool as SEZ 223 (inference) and describes a chuck that touches
  only the edge or floats the wafer on a nitrogen cushion, with the front
  protected by gas flow and geometry; the SEZ patent's gas cushion keeps
  the treatment fluid off the side facing the support.[^pat-spin-sez]
* **HF etches over thin oxides.** {ref}`TUNME <step-039>`,
  {ref}`GOXETCH <step-046>` and {ref}`SACETCH <step-095>` offer a
  single-wafer wet tool as one option beside the batch benches; both SEZ
  "HF" and the benches' HF are listed, so the listing does not choose
  between them.[^skw-01] Very dilute HF on a spin tool can clean with
  oxide loss below 0.03 nm;[^hattori-2007] an etch that must clear an
  oxide uses a stronger mix or a longer time (industry practice).
* **Cleans after contact and via etches.** The contact and via etch
  pages ({ref}`CTME <step-108>`, {ref}`VIME <step-119>`,
  {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`) name a wet bench or
  single-wafer clean for post-etch residue. DSP+ was published as a
  replacement for SPM on post-etch residues,[^lee-2012-dsp] and SEZ's
  residue work used an aluminium stack etched on a Lam TCP 9600, a model
  SkyWater also lists;[^sez-polymer-1999][^skw-01] neither source
  concerns SKY130.
* **Post-CMP clean.** Nine of the CMP pages list SEZ/Lam Da Vinci among
  post-CMP brush scrubbers, and all name the SEZ tools as SkyWater's
  candidate. The SEZ 223 listing names "Post-CMP-Cleaning" as an
  application,[^sez-223-moov] and SEZ's note describes backside
  wet-etch cleaning after CMP;[^kinoshita-sez] neither mentions a brush,
  so whether SkyWater's tools scrub the front side is an open question
  (our reading).
* **The pre-anneal clean.** {ref}`PWDEIS <step-033>` offers a
  spray or single-wafer processor as an alternative to the batch bench
  for its RCA clean; the SC-2 of that clean is listed only on the DNS and
  FSI tools ({ref}`machine-wet-bench`).[^skw-01]
* **Charging.** The deionised-water rinse of a spin tool can charge the
  surface of an oxide-covered wafer, depending on radius, time and spin
  speed;[^mui-2011] no step page raises this for SKY130.

## Related pages

* {ref}`category-etch` — wet etching and the single-wafer spin etcher
  for backside film removal.
* {ref}`category-strip` — wet strip and clean chemistry.
* {ref}`machine-wet-bench` — the batch benches and spray processors that
  share the HF and clean steps.
* {ref}`machine-post-cmp-cleaner` — the post-CMP clean that the CMP pages
  assign to this class's listed tools.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — HF, sulphuric acid, peroxide and solvents.
* {ref}`material-wet-chemicals` — the acids, peroxide cleans and solvents,
  their grades and SkyWater's listed chemistries.
* {ref}`material-ultrapure-water` — rinse water, its standards and
  quality.
* {ref}`material-hardware-consumables` — chamber parts and waste
  treatment, including BFR's chuck and nozzle consumables.
* {ref}`material-process-gases` — nitrogen, oxygen, hydrogen, argon,
  helium and the oxidation additives, their grades and SkyWater's listed
  gases.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

* {ref}`Support for slice-shaped articles and device for etching silicon wafers with such a support <patent-gp3543072>` — US 4,903,717 A (1987)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the "Single Wafer"
  entry and its chemistries.[^skw-01]
* SkyWater Technology, *A Day in the Life of a SkyWater Maintenance
  Technician* — the caption naming a SEZ etcher tool.[^skw-07]
* SEZ Group, Spin-Processor 223 press release (1999) — the dual-chamber
  tool, its throughput and applications.[^sez-223-pr]
* Moov, *Lam Research / SEZ SP223* listing — the 200 mm tool's chambers,
  options and applications.[^sez-223-moov]
* SEZ Group, Spin-Processor 8200 press release (2001) — the double-sided
  four-chamber cleaner.[^sez-8200-2001]
* SEZ Group, Da Vinci order press release (2005) — the first Da Vinci
  sales.[^sez-2005]
* SEZ Group, *Da Vinci* product page (2008 capture) — the platform's
  applications and wafer sizes.[^sez-davinci-2008]
* SEZ Group, Lam Research acquisition announcement (2007) — SEZ's
  installed base and its move into Lam.[^sez-lam-2007]
* SCREEN Semiconductor Solutions, SP-2100 launch (2020) — a current
  200 mm spin processor.[^screen-sp2100]
* Fraunhofer IMM, *DSP Cleaning Agent Online Monitoring System* — DSP and
  DSP+ compositions and their monitoring.[^fraunhofer-dsp]

### High-level understanding

* Gaulhofer et al. (SEZ and EKC), *European Semiconductor* 1999 — how a
  single-wafer spin processor dispenses, spins off and recirculates
  chemistry.[^sez-polymer-1999]
* Kinoshita (SEZ), *Post-CMP Cleaning Technique by SEZ* — backside wet
  etching after CMP on a chemical spin etcher.[^kinoshita-sez]
* Kern, ch. 1 of *Handbook of Silicon Wafer Cleaning Technology* — an
  overview of cleaning technology and equipment.[^kern-handbook]
* Wikipedia, *Hydrofluoric acid* — the main etchant of the
  class.[^wiki-hf]

### Deep dive

* Sumnitsch (SEZ), US 4,903,717 — the gas-cushion support and collecting
  tank of the spin etcher.[^pat-spin-sez]
* Emslie, Bonner and Peck, *J. Appl. Phys.* 1958 — the flow of a liquid
  film on a rotating disk.[^emslie-1958]
* Hattori et al., *JES* 1998 — spin cleaning with alternating ozonised
  water and dilute HF.[^hattori-1998]
* Hattori et al., *IEEE TSM* 2007 — single-wafer spin cleaning with
  ultra-dilute HF and nitrogen spray.[^hattori-2007]
* Oinoue et al., *Solid State Phenom.* 2018 — etch-rate distributions of
  HF/HNO₃ silicon etching in a single-spin process.[^oinoue-2018]
* Schwartz and Robbins, *JES* 1976 — the oxidation–dissolution mechanism
  of silicon etching in HF/HNO₃.[^schwartz-1976]
* Kikuyama et al., *JES* 1994 — very dilute HF and conductivity
  monitoring of its etch rate.[^kikuyama-1994]
* Knotter and Denteneer, *JES* 2001 — the etching mechanism of nitride in
  HF solutions.[^knotter-2001]
* Broussous et al., *Solid State Phenom.* 2005 — backside cleaning on
  silicon, nitride and oxide in an SEZ spin processor.[^broussous-2005]
* Lee et al., *Solid State Phenom.* 2012 — DSP+ for post-etch residue
  removal.[^lee-2012-dsp]
* Mui et al., *IEEE TSM* 2011 — a model of wafer surface charging in
  single-wafer wet spin processes.[^mui-2011]
* Reinhardt and Kern (eds.), *Handbook of Silicon Wafer Cleaning
  Technology* — wet cleaning, residue removal and particle
  control.[^reinhardt-2008]

## Open questions

* How many single-wafer tools SkyWater has, which chemistries run on the
  SEZ 223 and which on the Da Vinci, and what "titration controlled"
  denotes, are not stated.[^skw-01]
* Whether either listed tool has a front-side brush or megasonic module,
  and so whether it can serve as the post-CMP scrubber the CMP pages look
  for, is not public.
* Which SKY130 steps, if any, run on the listed tools is not stated; the
  step pages' assignments are inferences from the listed chemistries and
  applications.
* The model list above is incomplete: it covers the SEZ and SCREEN tools
  for which a public description was found, not the SCP, Akrion,
  Semitool and other spin processors of the period.

<!-- footnotes -->

[^sez-223-pr]: SEZ Group, *SEZ Doubles Wafer Processing Capabilities With
    New Dual Chamber Spin-Processing System* (press release, 1999-12-13),
    reproduced by Surface Finishing / VertMarkets.
    <https://www.surfacefinishing.com/doc/sez-doubles-wafer-processing-capabilities-wit-0001>
[^pat-spin-sez]: F. Sumnitsch (SEZ), *Support for slice-shaped articles
    and device for etching silicon wafers with such a support*, US
    4,903,717 A, filed 1988-11-09, granted 1990-02-27.
    <https://patents.google.com/patent/US4903717A/en>
[^sez-polymer-1999]: E. Gaulhofer, H. Kruwinus (SEZ), G. Goebel, E.
    Finson and T. Maw (EKC), "Single-Wafer Polymer Removal for
    0.18-micron to 0.25-micron Technology", *European Semiconductor*,
    April 1999; reprint on the SEZ website, Wayback Machine capture of
    2006-01-17.
    <https://web.archive.org/web/20060117001812/http://www.sez.com:80/NR/rdonlyres/e3nsv7jtmjelajokwc2pivxpcigbahrzmpkjqmcqjbeiv4nzvl7qlr3sxhl7otzjxbrsdw6tls4y3ubhoiijpiwz2qb/polymer_removal_0499.pdf>
[^oinoue-2018]: T. Oinoue, S. Saito, A. Okuyama, Y. Hagimoto and H.
    Iwamoto, "Behavior Analysis of Si Etching Process with HF/HNO3
    Mixture in Single-Spin Wafer Process", *Solid State Phenomena*
    **282**, 83–87 (2018).
    <https://doi.org/10.4028/www.scientific.net/SSP.282.83>
[^broussous-2005]: L. Broussous, P. Besson, M. M. Frank and D. Bourgeat,
    "Single Backside Cleaning on Silicon, Silicon Nitride and Silicon
    Oxide", *Solid State Phenomena* **103–104**, 249–254 (2005).
    <https://doi.org/10.4028/www.scientific.net/SSP.103-104.249>
[^lee-2012-dsp]: H. H. Lee, M. S. Yun, H. W. Lee and J. G. Park,
    "Removing W Polymer Residue from BEOL Structures Using DSP+ (Dilute
    Sulfuric-Peroxide-HF) Mixture – A Case Study", *Solid State
    Phenomena* **195**, 128–131 (2012).
    <https://doi.org/10.4028/www.scientific.net/SSP.195.128>
[^sez-8200-2001]: SEZ Group, *First Double Sided Single Wafer
    Spin-Processor Available for Cleaning Applications*, press release,
    2001-01-31; Wayback Machine capture of 2008-11-20.
    <https://web.archive.org/web/20081120145130/http://www.sez.com/31_Jan_01__First_Double_Sided_Single_Wafer_Spin_Processor_Available_for_Cleaning_Applications.SEZ>
[^sez-223-moov]: Moov used-equipment marketplace, *Lam Research / SEZ
    SP223* listing, accessed 2026-09-13.
    <https://moov.co/marketplace/wet-etch/sez-lam-research/lam-research-sez-sp223>
[^sez-2005]: SEZ Group, *World-Leading Korean Manufacturer Places
    Multi-System Order for SEZ Da Vinci Tools*, press release,
    2005-03-02; Wayback Machine capture of 2009-01-07.
    <https://web.archive.org/web/20090107032902/http://www.sez.com/02_Mar_05__World_Leading_Korean_Manufacturer_Places_Multi_System_Order_for_SEZ_Da_Vinci__Tools.SEZ>
[^sez-davinci-2008]: SEZ Group, *Da Vinci*, product page; Wayback Machine
    capture of 2008-03-22.
    <https://web.archive.org/web/20080322001425/http://www.sez.com:80/Da_Vinci.SEZ>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; resist removal and clean entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^skw-07]: SkyWater Technology, *A Day in the Life of a SkyWater
    Maintenance Technician*, 2023-12-14, re-read 2026-09-13.
    <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
[^kinoshita-sez]: K. Kinoshita (SEZ application department, Sumitomo
    Electronics), *Post-CMP Cleaning Technique by SEZ: Cleaning of
    Backside by Wet Etching*, application article, undated; SEZ website,
    Wayback Machine capture of 2006-01-17.
    <https://web.archive.org/web/20060117013206/http://www.sez.com:80/NR/rdonlyres/e7enpr5qqh5rriqc5rsb2wuafgjsrvoycez2ufodmguu27gfnn2xqfmf4al2ukmo7cfqmdm5dwfkx3lfnkizldcy2nb/postcmp.pdf>
[^emslie-1958]: A. G. Emslie, F. T. Bonner and L. G. Peck, "Flow of a
    viscous liquid on a rotating disk", *Journal of Applied Physics*
    **29**(5), 858–862 (1958). <https://doi.org/10.1063/1.1723300>
[^schwartz-1976]: B. Schwartz and H. Robbins, "Chemical Etching of
    Silicon: IV. Etching Technology", *Journal of The Electrochemical
    Society* **123**(12), 1903–1909 (1976).
    <https://doi.org/10.1149/1.2132721>
[^hattori-1998]: T. Hattori, T. Osaka, A. Okamoto, K. Saga and H.
    Kuniyasu, "Contamination Removal by Single‐Wafer Spin Cleaning with
    Repetitive Use of Ozonized Water and Dilute HF", *Journal of The
    Electrochemical Society* **145**(9), 3278–3284 (1998).
    <https://doi.org/10.1149/1.1838798>
[^hattori-2007]: T. Hattori, H. Hirano, T. Osaka and H. Kuniyasu,
    "Environmentally Benign Single-Wafer Spin Cleaning Using
    Ultra-Diluted HF/Nitrogen Jet Spray Without Causing Structural Damage
    and Material Loss", *IEEE Transactions on Semiconductor Manufacturing*
    **20**(3), 252–258 (2007). <https://doi.org/10.1109/TSM.2007.901845>
[^knotter-2001]: D. M. Knotter and T. J. J. Denteneer, "Etching
    Mechanism of Silicon Nitride in HF-Based Solutions", *Journal of The
    Electrochemical Society* **148**(3), F43 (2001).
    <https://doi.org/10.1149/1.1348262>
[^kikuyama-1994]: H. Kikuyama, M. Waki, M. Miyashita, T. Yabune, N.
    Miki, J. Takano and T. Ohmi, "A Study of the Dissociation State and
    the SiO₂ Etching Reaction for HF Solutions of Extremely Low
    Concentration", *Journal of The Electrochemical Society* **141**(2),
    366–374 (1994). <https://doi.org/10.1149/1.2054733>
[^fraunhofer-dsp]: Fraunhofer Institute for Microengineering and
    Microsystems IMM, *DSP Cleaning Agent Online Monitoring System*,
    product sheet, accessed 2026-09-13.
    <https://www.imm.fraunhofer.de/content/dam/imm/de/documents/PDFs-neu2018/A-und-S/IMM-DSP_Cleaning_Agent_Online_Monitoring_System%20.pdf>
[^mui-2011]: D. Mui, E. H. Lenz, C. Cyterski, K. Venkataraman and M.
    Kawaguchi, "Wafer Surface Charging Model for Single-Wafer Wet-Spin
    Processes", *IEEE Transactions on Semiconductor Manufacturing*
    **24**(4), 552–558 (2011). <https://doi.org/10.1109/TSM.2011.2162346>
[^sez-lam-2007]: SEZ Group, *SEZ Holding Welcomes Planned Acquisition by
    Lam Research*, press release, 2007-12-11; Wayback Machine capture of
    2007-12-13.
    <https://web.archive.org/web/20071213223543/http://www.sez.com:80/11_Dec_07__SEZ_Holding_Welcomes_Planned_Acquisition_by_Lam_Research.SEZ>
[^screen-sp2100]: SCREEN Semiconductor Solutions, *SCREEN Launches New
    Spin Processor for Single Wafer Cleaning*, news release, 2020-06-25,
    accessed 2026-09-13.
    <https://www.screen.co.jp/spe/en/information/spe200625>
[^kern-handbook]: W. Kern, "Overview and Evolution of Silicon Wafer
    Cleaning Technology", ch. 1 in K. A. Reinhardt and W. Kern (eds.),
    *Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
    Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8.
    <https://doi.org/10.1016/b978-081551554-8.50004-5>
[^wiki-hf]: Wikipedia, *Hydrofluoric acid*.
    <https://en.wikipedia.org/wiki/Hydrofluoric_acid>
[^reinhardt-2008]: K. A. Reinhardt and W. Kern (eds.), *Handbook of
    Silicon Wafer Cleaning Technology*, 2nd ed., William Andrew, 2008,
    ISBN 978-0-8155-1554-8. <https://openlibrary.org/isbn/9780815515548>
