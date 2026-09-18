(machine-post-cmp-cleaner)=
# Post-CMP cleaner

A post-CMP cleaner is the machine that takes a wafer from the polisher
while it is still wet and removes the slurry, polishing debris and metal
contamination the polish leaves behind: it scrubs both faces with soft
rotating brushes in a dilute chemical, often adds a megasonic bath or a
dilute-HF step, rinses the wafer and spins it dry. In the 200 mm era it
was first a separate double-sided scrubber loaded from a wet cassette
and later a module built into the polisher, so that wafers entered and
left the combined tool dry. This page describes the class in general,
lists representative 200 mm-era models, and then says what SkyWater has
published about tools that could serve this purpose and which SKY130
steps this reference assigns to the class. The chemistry of the
{term}`post-CMP clean` is summarised on the {ref}`CMP category page
<category-cmp>`; the polisher is on the {ref}`CMP polisher page
<machine-cmp-polisher>`.

| | Post-CMP cleaner |
|---|---|
| What it does | Removes slurry and metal contamination after a polish before it dries: "If the slurry is not thereafter completely removed, or if it is allowed to dry, so many defects will occur in the individual circuit dice that the whole wafer may have to be scrapped".[^pat-scrubber-ontrak] |
| Brush scrubbing | "A conventional double-sided scrubber system has two brush stations", a spin station that rinses and dries "without contacting the wafer surfaces", and brushes "constantly flushed with deionized water";[^pat-scrubber-ontrak] "Nylon or PVA may be used" for the brushes.[^pat-scrubber-ontrak] |
| Megasonics | Sound "in the neighborhood of 1 MHz" in a cleaning fluid;[^pat-megasonic-rca] "0.8 to 1.0 MHz" megasonic cleaning removes particles more efficiently in SC-1 than in DI water.[^busnaina-1995] |
| Chemistries | Dilute NH₄OH, dilute HF or other chemistries in the brush and megasonic modules ({ref}`category-cmp`); the Mirra Mesa supported "HF in the brush modules and heated RCA chemistries in the megasonic module";[^amat-mesa-1999] TMAH has been studied for post-tungsten-CMP cleaning.[^jolley-1998] |
| Integration | Standalone scrubbers with a wet input indexer that keeps wafers "submersed in processing solution";[^pat-scrubber-ontrak] integrated "dry in/dry out" cleaners on the polisher.[^lam-integra-1999][^amat-mesa-1999] |
| 200 mm era | OnTrak DSS-200 and DSS-150 double-sided scrubbers;[^pat-scrubber-ontrak] Lam's Synergy Integra, introduced in 1997;[^lam-integra-1999] Applied's Mesa cleaner on the Mirra Mesa (1999);[^amat-mesa-1999] SpeedFam-IPEC's Auriga cleaners.[^speedfam-ipec-2001] |
| SkyWater-listed tool | No brush scrubber named; the CMP pages point to "SEZ223, Davinci", and the Mirra entry lists "Track ammonia clean" and "IPA clean"[^skw-01] |
| SKY130 steps | 12 steps; see {ref}`SKY130 steps assigned to this class <machine-post-cmp-cleaner-steps>` |

## What the machine class is and how it works

Polishing leaves abrasive particles pressed into the surface[^zhang-busnaina-1999]
and slurry chemicals and, after a metal polish, metal on it. Zhang, Raghavan and Weling called CMP "inherently a
dirty process", classed its defects as "particulate, metallic, organic,
and others", and reviewed "General approaches that can be used for
removing contaminants after CMP".[^zhang-raghavan-1999] The cleaner's
task is to remove them before they bond: in Busnaina et al.'s work,
strong particle adhesion "is shown to be caused by chemical reactions
(after initial hydrogen bonding) that take place in the presence of
moisture and long aging time".[^busnaina-2002] What makes a machine a post-CMP
cleaner is keeping the wafer wet from the polisher to the first brush,
scrubbing both faces without scratching, supplying the right chemistry
at each station, and returning a dry wafer (industry
practice).[^pat-scrubber-ontrak]

### Double-sided brush scrubbing

A double-sided scrubber passes the wafer between pairs of rotating
brushes. In OnTrak's patent the wafers are moved "along a wet track" by
spray nozzles, each brush station has "two top and two bottom spray
nozzles" and a scrubbing-solution nozzle, and the brushes "have hollow
cores and are supplied with a flow of deionized water during operation
for continuous rinsing of the brush bristles", which "prevents particle
build-up on the brushes" and keeps the water "flowing thereby preventing
bacteria growth".[^pat-scrubber-ontrak] How the brush removes a particle
has been studied closely. Zhang, Busnaina and Ahmadi concluded that "The
lift force in the hydrodynamic boundary layer is too small to lift
particles off the surface and particles most likely roll off the
surfaces by the drag force plus the contact forces from the pad or brush
asperities".[^zhang-busnaina-1999] Busnaina et al. found that "contact
between the particle and the brush is essential to the removal of
submicron particles", and that "high removal efficiency (low number of
defects) is possible with a high brush pressure and a short cleaning
time".[^busnaina-2002] For nanometre-sized slurry particles, Xu et al.
concluded that "nanosized particles cannot be lifted directly by a
brush", that "rolling should be the main particle-removal mechanism",
and that the brush and wafer run "in a hydrodynamic lubrication
regime".[^xu-2004] The brush surface matters too: Philipossian and Sun
found that "brush design strongly impacts the frictional and
lubrication characteristics of the scrubbing process".[^philipossian-2009]
Sun, Han and Keswani review the field.[^sun-2017]

### Megasonic cleaning

A megasonic module adds sound in the megahertz range to the cleaning
liquid. RCA's patent describes a cleaning fluid in which "a transducer
oscillates at a frequency in the range of between about 0.2 and 5 MHz",
propagating "a beam of ultrasonic energy in a direction substantially
parallel to the surfaces of the articles to be cleaned".[^pat-megasonic-rca]
Busnaina, Kashkoush and Gale measured removal at 862 kHz; "The removal
efficiency is known to be higher in SC1 than in DI water", in both it is
"a function of irradiation time and particle size", and increased power
increased it.[^busnaina-1995] Gale and Busnaina showed "both cavitation and
acoustic streaming as important components of the megasonic
process".[^gale-1999] In Applied's Mesa cleaner "A single-wafer
megasonics bath can be added to ensure particle removal from alignment
marks, very small recessed features and difficult bevel
regions".[^amat-mesa-1999]

### Chemistry after oxide and tungsten polishes

The chemistry follows the polish. The {ref}`category page
<category-cmp>` gives dilute NH₄OH for oxide and dilute HF or citric
acid for tungsten; Applied's Mesa cleaner supported "a variety of
industry standard chemistries including HF in the brush modules and
heated RCA chemistries in the megasonic module",[^amat-mesa-1999] and
SpeedFam-IPEC's dual-station box cleaner "extends the pH range for HF
etching and advanced cleaning".[^speedfam-ipec-2001] Jolley studied
tetramethylammonium hydroxide as a post-tungsten-CMP cleaning
mixture,[^jolley-1998] and Devriendt et al. related oxide-CMP defects to
the cleaning strategy.[^devriendt-1998] In sub-130 nm logic products with copper
interconnect, Ge et al. traced a metal-1 bridging yield loss to organic particles from a
tungsten contact polish and found that "Brush 2 with HF spraying and
closed mechanical scrubbing directly induced the organic surface
particles"; opening that brush and optimising the megasonic tank and
the first brush reduced the defects.[^ge-2006] For scratches that have
filled with tungsten, Ollendorf et al. added a plasma etch after the
polish.[^ollendorf-2004]

### Backside, drying and integration

The back of the wafer picks up slurry as well. An SEZ application note
points out that compounds formed between backside films and metals are
"difficult to remove by either the brush scrubber cleaning or the
megasonic cleaning", and proposes etching the backside film on a
single-wafer chemical spin etcher instead ({ref}`machine-single-wafer-spin-processor`).[^kinoshita-sez]
The last station rinses and dries: OnTrak's scrubber used "A spin
station" that rinses and dries both sides "without contacting the wafer
surfaces".[^pat-scrubber-ontrak] Because slurry must not dry, the
cleaner moved onto the polisher. Lam's Synergy Integra combined "the
polisher and cleaner onto a single platform", "eliminating the damage
that can occur if polishing slurry dries on a wafer",[^lam-integra-1999]
and Applied's Mirra Mesa grips wafers "at the edge" and submerges them
"vertically into the modules where they are cleaned on front and back
sides", with each module requiring "only 30 seconds of process
time".[^amat-mesa-1999]

## Representative 200 mm-era models

* **OnTrak Systems / Lam Research.** The DSS-200 and DSS-150
  double-sided scrubbers, used "for processes as diverse as bare silicon
  cleaning by silicon material suppliers to post chemical-mechanical
  planarization (CMP) for inter-metal dielectric planarization
  cleaning";[^pat-scrubber-ontrak] the Synergy Integra, "Introduced in
  1997", integrated "with six of the leading dry in/dry out CMP system
  suppliers", with more than 750 integrated and standalone OnTrak
  cleaners installed by 1999;[^lam-integra-1999] Lam reported its
  1,000th post-CMP clean system in 2001 and wrote that "All Synergy
  Integra post-CMP clean systems use Double-Sided Scrubbing and Chemical
  Mechanical Cleaning (CMC™) technologies for single-step
  processing".[^lam-clean-1000-2001]
* **Applied Materials.** The Mesa cleaner of the Mirra Mesa, configurable
  with "a single-wafer immersion megasonic module, two double-sided brush
  scrubber stations and a spin rinse dryer".[^amat-mesa-1999]
* **IPEC-Planar / SpeedFam-IPEC.** The AvantGaard 676 with "Integrated
  post CMP spray box cleaning";[^ipec-676-1997] the Auriga C, whose
  integrated cleaner's "Two dual side PVA brush boxes remove particulates using common chemistries",
  with a "Rinse Ring design" and a spin rinse dryer that "supports
  optional megasonic cleaner".[^speedfam-ipec-2001]
* **Strasbaugh.** Cleaning stations on the 6DS-SP polisher, where "A
  de-ionized water spray flushes the wafer surface while a cleaning disk
  buffs the residual slurry and particles off the wafer", and an option
  for "Double-sided, post-CMP scrubber integration".[^strasbaugh-6ds-1999]
* **SCREEN (formerly Dainippon Screen).** Spin scrubbers, "Method in which
  wafers are physically cleaned using soft brushes and DI water"; the
  SS-3200 for 200 mm, launched in 2024, is a current
  model.[^screen-ss3200]
* **Other vendors.** The step pages also name SEZ/Lam Da Vinci among
  post-CMP brush scrubbers; the SEZ sources retrieved for this page
  describe single-wafer spin processing and backside wet etching and do
  not mention a brush ({ref}`machine-single-wafer-spin-processor`).[^sez-davinci-2008][^kinoshita-sez]

## At SkyWater

### What SkyWater lists

SkyWater's *Facilities & Capabilities* page lists no brush scrubber or
megasonic cleaner.[^skw-01] Two groups of entries touch the post-CMP
clean. Under "CMP", after the "AMAT Mirra CMP" entry and its dashed
processes, it lists "Track ammonia clean" and "IPA clean" without a
dash; the step pages and the {ref}`machines index <machines-index>`
read them as part of the Mirra entry.[^skw-01] And under "Resist
removal/cleans" it lists "Single Wafer" with "SEZ223, Davinci, HF,
DSP+HF, titration controlled", described on the
{ref}`single-wafer spin processor page
<machine-single-wafer-spin-processor>`.[^skw-01]

Read term by term: "ammonia clean" names an ammonia chemistry and "IPA
clean" an isopropyl-alcohol step (our reading of the words only); what
"Track" denotes, which films either clean follows, and whether either is
a module of an integrated cleaner on the polisher, are not stated. The page does not say
that the Mirra is a Mirra Mesa. A used-equipment listing gives
"Post-CMP-Cleaning" among the applications of the SEZ 223,[^sez-223-moov]
but SkyWater does not say that its SEZ tools clean wafers after
CMP.[^skw-01]

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>`
there is no listing of this class: the entries above are **strong** for
the existence of the "Track ammonia clean" and "IPA clean" entries and
of the SEZ tools, but none is a SkyWater statement that a given tool
performs the post-CMP clean.[^skw-01] The CMP pages name the SEZ entry for the
clean ({ref}`CMPNIT <step-012>` grades it "strong for existence") and
record the missing brush scrubber as an open question. The caveats that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`.

(machine-post-cmp-cleaner-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a post-CMP cleaner
(identical to the {ref}`machines index <machines-index>` table):

{ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Single Wafer", "SEZ223, Davinci, HF, DSP+HF, titration controlled"**
  (the part of the row that concerns this class) — *named as the post-CMP clean; no brush scrubber named:* {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>`;
  the full row, which also covers HF etches and other cleans, is on the
  machines index and the {ref}`single-wafer spin processor page
  <machine-single-wafer-spin-processor>`.

Every CMP page also quotes the Mirra entry's "Track ammonia clean" and
"IPA clean", without grading them as a cleaner.[^skw-01]

## Consumables and facilities

The cleaning chemicals are listed in the {ref}`materials index
<materials-index>`; what is specific to a post-CMP cleaner is summarised
here. None of the SkyWater sources describes the fab's cleaner
chemistry or brush supply. Brushes and post-CMP clean chemistry are
described on the {ref}`CMP consumables <material-cmp-consumables>` page.
Ultrapure water, its standards and its quality parameters are described
on the {ref}`ultrapure water <material-ultrapure-water>` page.

* **Brushes.** Rotating roller brushes of PVA or nylon, flushed with
  ultrapure water through hollow cores,[^pat-scrubber-ontrak] and
  replaced as they wear or load with particles (industry practice); their
  surface design changes the friction of the scrub.[^philipossian-2009]
* **Chemicals.** Dilute ammonia for oxide polishes and dilute HF or
  organic acids for tungsten ({ref}`category-cmp`); HF and heated RCA
  chemistries in integrated cleaners;[^amat-mesa-1999] SC-1 in megasonic
  baths;[^busnaina-1995] SkyWater lists "Track ammonia clean" and "IPA
  clean" under CMP.[^skw-01]
* **Water.** Ultrapure water for the wet indexer, brush flushing, sprays
  and the final rinse;[^pat-scrubber-ontrak] the SS-3200 for 200 mm is
  promoted as "using less de-ionized (DI) water per
  wafer".[^screen-ss3200]
* **Megasonic power and drying.** Megasonic transducers and
  generators,[^pat-megasonic-rca] and spin rinse dryers.[^amat-mesa-1999]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's post-CMP cleaning sequence and
chemistries are not public.

* **After every polish.** All twelve polish steps
  ({ref}`CMPNIT <step-012>` to {ref}`CMPM4 <step-157>`) name a post-CMP
  brush scrubber in their "Machines typically used" sections, and their
  industry-generic outlines describe a double-sided brush scrub, on
  several pages with a dilute-HF step, then spin-rinse-dry.
* **Oxide and tungsten cleans differ.** The outlines of the oxide polishes
  ({ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`CMPL <step-106>`,
  {ref}`CMPM <step-116>` to {ref}`CMPM4 <step-157>`) scrub in dilute
  NH₄OH; those of the tungsten polishes offer an alternative to dilute
  NH₄OH — citric acid on {ref}`WCMPLI <step-100>`, a TMAH-based chemistry
  on {ref}`WCMP2 <step-111>` to {ref}`WCMP5 <step-148>`, where Jolley
  studied TMAH as a post-tungsten-CMP clean (industry
  practice).[^jolley-1998] Ge et al.'s
  130 nm case shows that a tungsten contact clean can itself add
  defects that bridge the first metal.[^ge-2006]
* **What SkyWater's list allows.** With no brush scrubber listed, the CMP
  pages name the SEZ single-wafer tools; the SEZ 223 is offered secondhand
  for "Post-CMP-Cleaning",[^sez-223-moov] and SEZ's own note describes
  backside wet etching after CMP.[^kinoshita-sez] Whether SkyWater's
  post-CMP clean is a brush module of an integrated Mirra Mesa-type
  cleaner, the listed "Track ammonia clean" and "IPA clean", the SEZ
  tools, or an unlisted scrubber is not public (open question).
* **Before the next lithography and deposition.** A polish is followed by
  a liner or cap deposition or a mask (on the step pages' readings,
  {ref}`WCMPLI <step-100>` is followed by the TiN local interconnect and
  {ref}`CMPM <step-116>` by the cap oxide); particles left on the back after CMP can defocus the next
  exposure on a vacuum chuck.[^kinoshita-sez]

## Related pages

* {ref}`category-cmp` — the post-CMP clean and its chemistry.
* {ref}`machine-cmp-polisher` — the polisher that feeds the cleaner.
* {ref}`machine-single-wafer-spin-processor` — the listed single-wafer
  tools the CMP pages name for the clean.
* {ref}`machine-wet-bench` — batch cleans and megasonic tanks elsewhere in
  the flow.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — cleaning chemicals and ultrapure water.
* {ref}`material-cmp-consumables` — slurries, pads, brushes and
  post-CMP clean chemistry.
* {ref}`material-ultrapure-water` — rinse water, its standards and
  quality.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 3,893,869 A <patent-gp23886506>` — Megasonic cleaning system (1974)
* {ref}`US 5,442,828 A <patent-gp25529547>` — Double-sided wafer scrubber with a wet submersing silicon wafer indexer (1992)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the CMP and
  single-wafer entries and the absence of a brush scrubber.[^skw-01]
* Lutz (OnTrak Systems), US 5,442,828 — the DSS double-sided scrubber, its
  brush stations and wet indexer.[^pat-scrubber-ontrak]
* Lam Research, Synergy Integra press release (1999) — an integrated
  post-CMP cleaner and the installed base of OnTrak
  cleaners.[^lam-integra-1999]
* Lam Research, 1,000th post-CMP clean system press release (2001) —
  double-sided scrubbing and chemical mechanical cleaning on the Synergy
  Integra.[^lam-clean-1000-2001]
* Applied Materials, Mirra Mesa press release (1999) — the Mesa
  cleaner's modules, chemistries and wafer handling.[^amat-mesa-1999]
* IPEC-Planar, *AvantGaard 676 Highlights* (1997 capture) — integrated
  spray-box cleaning.[^ipec-676-1997]
* SpeedFam-IPEC, *CMP Products* (2001 capture) — the Auriga brush-box and
  megasonic cleaners.[^speedfam-ipec-2001]
* Strasbaugh, *6DS-SP Series Planarizers* (1999 capture) — cleaning
  stations and scrubber integration on a polisher.[^strasbaugh-6ds-1999]
* SCREEN Semiconductor Solutions, SS-3200 for 200 mm launch (2024) — a
  current 200 mm spin scrubber.[^screen-ss3200]
* Moov, *Lam Research / SEZ SP223* listing — post-CMP cleaning among the
  223's applications.[^sez-223-moov]

### High-level understanding

* Sun, Han and Keswani, "Brush Scrubbing for Post-CMP Cleaning" (2017) —
  a review chapter.[^sun-2017]
* Kinoshita (SEZ), *Post-CMP Cleaning Technique by SEZ* — backside
  contamination after CMP and wet-etch cleaning.[^kinoshita-sez]
* SEZ Group, *Da Vinci* product page (2008 capture) — the single-wafer
  platform the step pages list among scrubbers.[^sez-davinci-2008]
* Wikipedia, *RCA clean* — the SC-1 chemistry of megasonic
  baths.[^wiki-rca]

### Deep dive

* Zhang, Raghavan and Weling, *JVST B* 1999 — CMP defects and approaches
  to post-CMP cleaning.[^zhang-raghavan-1999]
* Zhang, Busnaina and Ahmadi, *JES* 1999 — particle adhesion in CMP and
  removal by rolling in brush cleaning.[^zhang-busnaina-1999]
* Busnaina et al., *IEEE TSM* 2002 — chemical bonding of particles and
  the need for brush contact.[^busnaina-2002]
* Xu et al., *JVST B* 2004 — removal of nanosized slurry particles by
  brush scrubbing.[^xu-2004]
* Philipossian and Sun, *ESSL* 2009 — brush roller design and friction
  in post-ILD-CMP scrubbing.[^philipossian-2009]
* Busnaina, Kashkoush and Gale, *JES* 1995 — megasonic particle removal in
  DI water and SC-1.[^busnaina-1995]
* Gale and Busnaina, *Particul. Sci. Technol.* 1999 — cavitation and
  acoustic streaming in megasonic cleaning.[^gale-1999]
* Mayer and Shwartzman (RCA), US 3,893,869 — the megasonic cleaning
  system.[^pat-megasonic-rca]
* Jolley, *Solid State Phenom.* 1998 — TMAH as a post-tungsten-CMP
  clean.[^jolley-1998]
* Devriendt et al., *Solid State Phenom.* 1998 — oxide-CMP defects and
  post-CMP cleaning strategies.[^devriendt-1998]
* Ge et al., ICSICT 2006 — a post-tungsten-contact-CMP clean at 130 nm
  and the defects it caused.[^ge-2006]
* Ollendorf, Cabral and Fuller, ASMC 2004 — tungsten-filled microscratches
  after tungsten CMP and a dry plasma clean that removes the metal from
  them.[^ollendorf-2004]

## Open questions

* Which tool performs the post-CMP clean of SKY130 wafers at SkyWater —
  an integrated cleaner on the Mirra, the SEZ single-wafer tools or an
  unlisted scrubber — is not public; no brush scrubber is listed.[^skw-01]
* What "Track ammonia clean" and "IPA clean" denote, and whether they
  belong to the Mirra, are not stated.[^skw-01]
* The chemistries used after the oxide and tungsten polishes of SKY130
  are not public.
* The model list above is incomplete: it covers the OnTrak/Lam, Applied,
  SpeedFam-IPEC, Strasbaugh and SCREEN cleaners for which a public
  description was found, not every post-CMP cleaner of the period.

<!-- footnotes -->

[^pat-scrubber-ontrak]: R. A. Lutz (OnTrak Systems), *Double-sided wafer
    scrubber with a wet submersing silicon wafer indexer*, US 5,442,828 A,
    filed 1992-11-30, granted 1995-08-22.
    <https://patents.google.com/patent/US5442828A/en>
[^pat-megasonic-rca]: A. Mayer and S. Shwartzman (RCA), *Megasonic
    cleaning system*, US 3,893,869 A, granted 1975-07-08.
    <https://patents.google.com/patent/US3893869A/en>
[^busnaina-1995]: A. A. Busnaina, I. I. Kashkoush and G. W. Gale, "An
    Experimental Study of Megasonic Cleaning of Silicon Wafers", *Journal
    of The Electrochemical Society* **142**(8), 2812–2817 (1995).
    <https://doi.org/10.1149/1.2050096>
[^amat-mesa-1999]: Applied Materials, *Applied Materials Announces New
    Mirra Mesa System to Address Market Demand for Integrated CMP
    Solutions*, press release, 1999-06-10, accessed 2026-09-13.
    <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-new-mirra-mesa-system-address-market>
[^jolley-1998]: M. E. Jolley, "Applications of Tetramethylammoninium
    Hydroxide (TMAH) as a Post Tungsten CMP Cleaning Mixture", *Solid
    State Phenomena* **65–66**, 105–108 (1998).
    <https://doi.org/10.4028/www.scientific.net/SSP.65-66.105>
[^lam-integra-1999]: Lam Research, *Lam Research Corporation Ships 100th
    Synergy Integra Integrated CMP Cleaning System*, press release,
    1999-06-17, accessed 2026-09-13.
    <https://newsroom.lamresearch.com/1999-06-17-Lam-Research-Corporation-Ships-100th-Synergy-IntegraTM-Integrated-CMP-Cleaning-System>
[^speedfam-ipec-2001]: SpeedFam-IPEC CMP Group, *Products* (Momentum,
    Auriga, AvantGaard), product page; Wayback Machine capture of
    2001-04-12.
    <https://web.archive.org/web/20010412141846/http://www.ipec.com:80/cmp/products.htm>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; CMP and clean entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^zhang-raghavan-1999]: L. Zhang, S. Raghavan and M. Weling,
    "Minimization of chemical-mechanical planarization (CMP) defects and
    post-CMP cleaning", *Journal of Vacuum Science & Technology B*
    **17**(5), 2248–2255 (1999). <https://doi.org/10.1116/1.590901>
[^busnaina-2002]: A. A. Busnaina, H. Lin, N. Moumen, J.-W. Feng and J.
    Taylor, "Particle adhesion and removal mechanisms in post-CMP cleaning
    processes", *IEEE Transactions on Semiconductor Manufacturing*
    **15**(4), 374–382 (2002). <https://doi.org/10.1109/TSM.2002.804872>
[^zhang-busnaina-1999]: F. Zhang, A. A. Busnaina and G. Ahmadi, "Particle
    Adhesion and Removal in Chemical Mechanical Polishing and Post‐CMP
    Cleaning", *Journal of The Electrochemical Society* **146**(7),
    2665–2669 (1999). <https://doi.org/10.1149/1.1391989>
[^xu-2004]: K. Xu, R. Vos, G. Vereecke, G. Doumen, W. Fyen, P. W. Mertens,
    M. M. Heyns, C. Vinckier and J. Fransaer, "Particle adhesion and
    removal mechanisms during brush scrubber cleaning", *Journal of
    Vacuum Science & Technology B* **22**(6), 2844–2852 (2004).
    <https://doi.org/10.1116/1.1815319>
[^philipossian-2009]: A. Philipossian and T. Sun, "Frictional Analysis of
    Various Poly(vinyl alcohol) Brush Roller Designs for Post-Interlevel
    Dielectric CMP Scrubbing Applications", *Electrochemical and
    Solid-State Letters* **12**(3), H84 (2009).
    <https://doi.org/10.1149/1.3058994>
[^sun-2017]: T. Sun, Z. Han and M. Keswani, "Brush Scrubbing for
    Post-CMP Cleaning", in *Developments in Surface Contamination and
    Cleaning, Volume 9*, Elsevier, 2017, pp. 109–133.
    <https://doi.org/10.1016/B978-0-323-43157-6.00004-5>
[^gale-1999]: G. W. Gale and A. A. Busnaina, "Roles of cavitation and
    acoustic streaming in megasonic cleaning", *Particulate Science and
    Technology* **17**(3), 229–238 (1999).
    <https://doi.org/10.1080/02726359908906815>
[^devriendt-1998]: K. Devriendt, E. Vrancken, N. Heylen, J. Grillaert, M.
    Meuris, M. M. Heyns and Z. C. Lin, "Relation between Oxide-CMP Induced
    Defects and Post-CMP Cleaning Strategies", *Solid State Phenomena*
    **65–66**, 173–176 (1998).
    <https://doi.org/10.4028/www.scientific.net/SSP.65-66.173>
[^ge-2006]: D.-W. Ge, B.-C. Qiu, L.-R. Chen, F.-Y. He, J.-N. Liu, C.-X.
    Zhi and X. Cheng, "Optimizing post cleaning of Tungsten contact CMP to
    improve the yield of logic products with copper interconnect", *2006
    8th International Conference on Solid-State and Integrated Circuit
    Technology (ICSICT)*, pp. 351–353.
    <https://doi.org/10.1109/ICSICT.2006.306249>
[^ollendorf-2004]: H. Ollendorf, S. Cabral and R. Fuller, "Reduction of
    CMP μ-scratch induced metal shorts by introduction of a post CMP
    tungsten plasma clean process in a high volume DRAM manufacturing
    environment", *2004 IEEE/SEMI Advanced Semiconductor Manufacturing
    Conference and Workshop*, pp. 1–4.
    <https://doi.org/10.1109/ASMC.2004.1309523>
[^kinoshita-sez]: K. Kinoshita (SEZ application department, Sumitomo
    Electronics), *Post-CMP Cleaning Technique by SEZ: Cleaning of
    Backside by Wet Etching*, application article, undated; SEZ website,
    Wayback Machine capture of 2006-01-17.
    <https://web.archive.org/web/20060117013206/http://www.sez.com:80/NR/rdonlyres/e7enpr5qqh5rriqc5rsb2wuafgjsrvoycez2ufodmguu27gfnn2xqfmf4al2ukmo7cfqmdm5dwfkx3lfnkizldcy2nb/postcmp.pdf>
[^lam-clean-1000-2001]: Lam Research, *Lam Research Ships 1,000th
    Post-CMP Clean System To Philips*, press release, 2001-02-14,
    accessed 2026-09-13.
    <https://investor.lamresearch.com/2001-02-14-Lam-Research-Ships-1,000th-Post-CMP-Clean-System-To-Philips>
[^ipec-676-1997]: IPEC-Planar, *IPEC AvantGaard 676 Highlights*, product
    page; Wayback Machine capture of 1997-06-26.
    <https://web.archive.org/web/19970626104827/http://www.ipec.com:80/planar/676-spec.html>
[^strasbaugh-6ds-1999]: Strasbaugh, *The 6DS-SP Series Planarizers*,
    product page; Wayback Machine capture of 1999-02-10.
    <https://web.archive.org/web/19990210100559/http://www.strasbaugh.com:80/cmp1.htm>
[^screen-ss3200]: SCREEN Semiconductor Solutions, *Launch of 200mm Wafer
    Cleaning System — New SS-3200 for 200mm expands SCREEN SPE's
    world-leading spin scrubber lineup*, news release, 2024-11-06,
    accessed 2026-09-13.
    <https://www.screen.co.jp/spe/en/information/spe241106>
[^sez-davinci-2008]: SEZ Group, *Da Vinci*, product page; Wayback Machine
    capture of 2008-03-22.
    <https://web.archive.org/web/20080322001425/http://www.sez.com:80/Da_Vinci.SEZ>
[^sez-223-moov]: Moov used-equipment marketplace, *Lam Research / SEZ
    SP223* listing, accessed 2026-09-13.
    <https://moov.co/marketplace/wet-etch/sez-lam-research/lam-research-sez-sp223>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
