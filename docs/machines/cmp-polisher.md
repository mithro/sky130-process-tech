(machine-cmp-polisher)=
# CMP polisher

A {term}`CMP` polisher is the machine a fab uses to make a wafer flat
again after a deposition: it presses the wafer face down onto a
rotating or moving polishing pad wetted with slurry, removes the high
points of the film faster than the low ones, and stops at a target
thickness or on a harder layer underneath. Typical 200 mm tools of the
130 nm era carried each wafer across more than one platen, detected the
endpoint in situ and, increasingly, cleaned the wafer on board so that it
entered and left dry (see the models below).
This page describes the class in general, lists representative
200 mm-era models, and then says what SkyWater has published about its
own tool of this class and which SKY130 steps this reference assigns to
it. The polishing physics, slurries and the kinds of polish in the flow
are on the {ref}`category page <category-cmp>`; the clean after each
polish is on the {ref}`post-CMP cleaner page <machine-post-cmp-cleaner>`.

| | CMP polisher |
|---|---|
| What it does | Planarises films by polishing: "The carrier provides a controllable load, i.e., pressure, on the substrate to press it against the polishing pad", while "A polishing slurry, including an abrasive and at least one chemically-reactive agent" is spread over the pad.[^pat-carrier-amat] |
| Removal rate | "The polishing rate depends upon the force pressing the substrate against the pad";[^pat-carrier-amat] rate proportional to pressure and velocity in Preston's law, with a "nonlinear down pressure dependence" in Luo and Dornfeld's model.[^preston-1927][^luo-2001] |
| Architecture | Rotary multi-platen: "Multiple wafer heads, at least one greater in number than the number of polishing stations", suspended from a carousel;[^pat-cmp-mirra] linear: "a moving belt is used to linearly move the pad across the wafer surface".[^pat-linear-lam] |
| Pad | "porous polymeric materials with a pore size between 30 and 50 μm", which "must be regularly reconditioned";[^wiki-cmp] each station of Applied's carousel patent has "a pad conditioner to recondition the polishing pad so that it retains a high polishing rate".[^pat-cmp-mirra] |
| Endpoint | Reflectance through "a window embedded within the polishing table";[^pat-cmp-endpoint-ibm] a "substantially transparent polyurethane plug" in the pad.[^pat-cmp-window] |
| 200 mm era | Applied Materials Mirra, announced December 1995, "three-station, four polishing head design";[^amat-1997] IPEC-Planar AVANTI 472, "single wafer, two-step polishing for wafers up to 200mm";[^ipec-472-1997] Strasbaugh 6DS-SP;[^strasbaugh-6ds-1999] Lam Teres.[^pat-linear-lam] |
| SkyWater-listed tool | "AMAT Mirra CMP": "oxide", "nitride", "niobium", "aluminum", "tungsten", "high selectivity tungsten", "copper"; "On board metrology with feed forward and backward"[^skw-01] |
| SKY130 steps | 12 steps; see {ref}`SKY130 steps assigned to this class <machine-cmp-polisher-steps>` |

## What the machine class is and how it works

A CMP polisher has a few basic elements. Wikipedia's description of
typical tools is of
"rotating an extremely flat plate which is covered by a pad", with the
wafer "mounted upside-down in a carrier/spindle on a backing film" and
"The retaining ring" keeping it "in the correct horizontal position"; a
slurry supply "deposits the slurry on the pad", plate and carrier
rotate, the carrier oscillates, and "A downward pressure/down force is
applied to the carrier".[^wiki-cmp] An Applied Materials patent states
the design goal: the rate, finish and flatness "are determined by the
pad and slurry combination, the relative speed between the substrate
and pad, and the force pressing the substrate against the pad", and the
machine "should have a carrier head which applies a substantially
uniform load across the substrate".[^pat-carrier-amat] What makes a
machine a production polisher is how well it holds those conditions
from wafer to wafer — pad condition, slurry delivery, carrier pressure
profile — and how it knows when to stop.

### Removal: pressure, velocity and chemistry

Preston's law for glass polishing makes the removal rate proportional to
pressure and velocity ({ref}`category-cmp`).[^preston-1927] Production
polishes depart from it. Luo and Dornfeld modelled removal as the number
of active abrasives times the volume each removes, and found that "the
nonlinear down pressure dependence of material removal rate is related
to a probability density function of the abrasive size and the elastic
deformation of the pad".[^luo-2001] Runnels and Eyman showed "that
hydroplaning is possible for standard CMP processes", with wafer
curvature, slurry viscosity and rotation speed setting the fluid-film
thickness.[^runnels-1994] For tungsten, Stein et al. found that "the
polish rate data fit a multiterm regression model better than the
empirical Preston equation", and that the process temperature rose with
alumina concentration mostly because of "increased shaft
work".[^stein-1999] Nanz and Camilletti's review concluded that "as yet
no model describes the entire available process".[^nanz-1995] The
chemistry of oxide and tungsten polishing — hydrated oxide surfaces,
oxidised tungsten — is on the category page.[^rev-02]

### Platen, pad and conditioning

The pad is a consumable that the machine must keep in a steady state.
Wikipedia notes that pads "should be rigid in order to uniformly polish
the wafer surface", that "real pads are often just stacks of soft and
hard materials that conform to wafer topography to some extent", and
that because they are consumed "they must be regularly
reconditioned".[^wiki-cmp] Conditioners are built into the tool: every
polishing station of Applied's carousel patent, whose three-station,
four-head layout matches the Mirra (our reading; the patent does not
name the Mirra), carries one,[^pat-cmp-mirra][^amat-1997] and
IPEC's AVANTI 472 used an APP1000 conditioner whose "Pad profiling"
"reduces removal rate variation from wafer to wafer, improves within
wafer non-uniformity and extends pad life".[^ipec-472-1997] The same
tool listed "Closed loop platen temperature control", "Enhanced slurry
pump capacity up to 1000 ml/min" and "Material compatibility for medium
and low pH slurries (2 - 12)".[^ipec-472-1997]

### Carrier head and uniformity

The carrier sets the pressure profile across the wafer. The Applied
patent explains why: "If the carrier head applies a non-uniform load
… then the high pressure regions will be polished faster than the low
pressure regions", and its answer is a head with "a flexible membrane"
that "extends beneath the base to define a chamber", held in "a
retaining ring connected to the base and surrounding the flexible
membrane".[^pat-carrier-amat] Applied announced a new head for the
Mirra in June 1997, the "Titan Head", "minimizing effects at the edge of
the wafer, thus allowing better uniformity and a higher degree of
planarity".[^amat-1997] Wikipedia adds that on a bowed wafer "the
pressure will be greater on the edges than it would on the center",
which backside pressure can equalise.[^wiki-cmp] Later heads divided the
pressure into zones: SpeedFam-IPEC's Momentum carrier offered "zonal
control and edge-tuning capability".[^speedfam-ipec-2001]

### Machine architectures

The polishers of the period used four arrangements.

* **Rotary, multi-platen carousel.** In the Mirra patent the heads hang
  from a carousel that "provides circumferential positioning of the heads
  relative to the polishing pads". One head sits over "a transfer and
  washing station" while the others polish, so that loading and washing
  "can be performed concurrently with wafer polishing", and "The multiple
  polishing pads can
  be used to sequentially polish a wafer held in a wafer head in a step of
  multiple steps".[^pat-cmp-mirra]
* **Rotary, one or two heads.** The AVANTI 472 polished one wafer at a
  time with a "Two platen process for post polish buff";[^ipec-472-1997]
  Strasbaugh's 6DS-SP had "oscillating dual polishing spindles" and
  processed "two wafers simultaneously".[^strasbaugh-6ds-1999]
* **Linear.** A Lam patent describes the linear polisher, in which "a
  moving belt is used to linearly move the pad across the wafer surface.
  The wafer is still rotated for averaging out the local variations, but
  the global planarity is improved over CMP tools using rotating pads";
  "An example of a linear polisher is the TERES polisher available from
  Lam Research Corporation", which also uses a fluid platen under the
  belt.[^pat-linear-lam]
* **Orbital.** SpeedFam-IPEC's AvantGaard 676 used "a unique orbital
  polishing technique"; its Momentum "combines the benefits of the
  previous rotational and orbital platforms", with "four independent
  wafer-polishing platens" and "orbiting platen motion" combined with
  oscillation.[^speedfam-ipec-2001]

### Endpoint and integrated metrology

A stop-layer or metal polish can detect the change of material; an
oxide polish without a stop cannot, and Wikipedia notes that "a lack of
end points requires blind polishing".[^wiki-cmp] Optical endpoint looks
at the wafer through the rotating table: IBM's patent puts "a window
embedded within the polishing table", with a reflectance measurement in
which "a prescribed change in the in-situ reflectance corresponds to a
prescribed condition of the polishing process";[^pat-cmp-endpoint-ibm]
Applied's puts "A substantially transparent polyurethane plug" in an
aperture through the pad.[^pat-cmp-window] Bibby and Holland's
"Endpoint detection for CMP" (1998) covers the subject.[^bibby-1998] By 2001 tools also
measured film thickness on board: SpeedFam-IPEC's Momentum fed
integrated-metrology data to "predictive modeling software" that
changes "the process for subsequent wafer polishes".[^speedfam-ipec-2001]
Because polish rate depends on the layout, Stine et al. designed test
masks to model it and found "pattern density is a strongly dominant
factor".[^stine-1998]

### Scratches and dry-in/dry-out

A polisher also makes defects. Kwon, Ramachandran and Park review
scratching in CMP, its dependence on process conditions and consumables,
and the use of filtration and water jet spraying to reduce
it.[^kwon-2013] In a tungsten damascene sequence, "μ-scratches" in the
oxide "are filled with tungsten during the CMP process" and "can short
the intended patterned circuitry"; Ollendorf, Cabral and Fuller removed
the metal from them with a plasma clean after the
polish.[^ollendorf-2004] Slurry must not dry on the wafer: Lam described
integrating the cleaner with the polisher as "eliminating the damage
that can occur if polishing slurry dries on a wafer",[^lam-integra-1999]
and Applied's Mirra Mesa of 1999 "combines state-of-the-art wafer
polishing and cleaning capabilities on a single system" to give
"dry-in/dry-out CMP processing".[^amat-mesa-1999]

## Representative 200 mm-era models

* **Applied Materials.** The Mirra, whose entry into CMP Applied dated
  to December 1995, with "a unique three-station, four polishing head
  design that permits continuous processing of several wafers
  simultaneously", and the Titan Head of 1997;[^amat-1997] Applied
  reported its 500th Mirra in February 2000 and said the Mirra accounted
  for "the industry's largest installed base of multi-platen CMP
  tools".[^amat-mirra-500-2000] The Mirra Mesa of 1999 added the Mesa
  cleaner.[^amat-mesa-1999] A Chip History Center article calls the
  Mirra "the first CMP system that successfully integrated endpoint
  detection and integrated cleaning"; Applied's own releases introduce
  its integrated Mesa cleaner, "specifically developed for the Mirra",
  with the Mirra Mesa of 1999, and the article's
  "Announced in 1997" differs from both Applied's December 1995 and the
  article's own "Relevant Date" of
  1995-06-30.[^chiphistory-mirra][^amat-1997][^amat-mesa-1999]
* **IPEC-Planar / SpeedFam-IPEC.** The AVANTI 472, "IPEC-Planar's third
  generation Chemical Mechanical Planarization (CMP) product", for
  "both oxide and metal planarization processes";[^ipec-472-1997] the
  AvantGaard 676, with "Multiple wafer polishing modules (4)" and
  "Integrated post CMP spray box cleaning";[^ipec-676-1997] and, by 2001,
  the Auriga family and the Momentum, the latter for "the 0.18 micron and
  0.13 micron design node requirements".[^speedfam-ipec-2001]
* **Strasbaugh.** The 6DS-SP dual-spindle production planarizer, with
  optional "Dual polishing tables for 2-step processes" and "Double-sided,
  post-CMP scrubber integration";[^strasbaugh-6ds-1999] the 6EC, which
  Strasbaugh called a "Laboratory Planarizer" for "CMP research and
  small quantity production of wafers".[^strasbaugh-6ec-1999]
* **Lam Research.** The Teres linear polisher,[^pat-linear-lam] shipped
  with Lam's Synergy Integra cleaner.[^lam-clean-1000-2001]
* **Ebara.** The step pages name the EPO-222 and F-REX; Ebara now offers
  the F-REX200M2, which "polishes 200 mm wafers with high k-materials and
  aluminium layers".[^ebara-frex] No 200 mm-era Ebara description was
  retrieved for this page.

## At SkyWater

### What SkyWater lists

Under "CMP", SkyWater's *Facilities & Capabilities* page lists one
polisher, with its processes as dashed sub-entries, followed by three
lines without a dash:[^skw-01]

> "AMAT Mirra CMP"
> – "oxide" – "nitride" – "niobium" – "aluminum" – "tungsten" – "high
> selectivity tungsten" – "copper"
>
> "Track ammonia clean"
> "IPA clean"
> "On board metrology with feed forward and backward"

Read term by term: an Applied Materials Mirra, with polishes for oxide
and tungsten — the films of the SKY130 polishes on the step pages'
readings — and for nitride, the stop layer of two of them on those readings; and
for niobium, aluminium and copper, which no SKY130 step page reads as a
polish; the page describes the Minnesota site as
"Recently expanded in 2020 to enable additional capacity and Cu back end
of line".[^skw-01] "high selectivity tungsten" is not explained. The
step pages and the {ref}`machines index <machines-index>` read the three
undashed lines as part of the Mirra entry; the page does not say which
tool performs "Track ammonia clean" or "IPA clean", or whether the
Mirra is a Mirra Mesa with an integrated cleaner. "On board metrology
with feed forward and backward" resembles the integrated metrology
described above, but no model is given. The
page gives no pad, slurry, conditioner or head, and the S-1's list of
raw-material suppliers names no slurry or pad supplier.[^skw-01][^sec-01]

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` the
listing is **strong** for an Applied Mirra and its oxide, nitride and
tungsten processes: it is a SkyWater statement.[^skw-01] Whether the
tool is a Mirra or a Mirra Mesa, how many there are, and which
tungsten process runs a given level are not stated. The caveats that
apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`.

(machine-cmp-polisher-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a CMP polisher
(identical to the {ref}`machines index <machines-index>` table):

{ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>`

<!-- step-tables:begin (generated by tools/gen_step_tables.py; do not edit) -->
:::{table} The 12 steps above: number, code and name
:widths: 10 16 74

| Step | Code | Name |
|---:|:---|:---|
| 12 | {ref}`CMPNIT <step-012>` | CMP over nitride |
| 90 | {ref}`CMPP <step-090>` | CMP over poly |
| 100 | {ref}`WCMPLI <step-100>` | W CMP for local interconnect |
| 106 | {ref}`CMPL <step-106>` | CMP polish over local interconnect |
| 111 | {ref}`WCMP2 <step-111>` | W CMP for metal contact |
| 116 | {ref}`CMPM <step-116>` | CMP over metal1 |
| 122 | {ref}`WCMP3 <step-122>` | W CMP for via1 |
| 127 | {ref}`CMPM2 <step-127>` | CMP over metal2 |
| 133 | {ref}`WCMP4 <step-133>` | W CMP for via2 |
| 142 | {ref}`CMPM3 <step-142>` | CMP over metal3 |
| 148 | {ref}`WCMP5 <step-148>` | W CMP for via3 |
| 157 | {ref}`CMPM4 <step-157>` | CMP over metal4 |
:::
<!-- step-tables:end -->

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"AMAT Mirra CMP"** — *inference from the film:* {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`CMPL <step-106>`, {ref}`CMPM <step-116>`, {ref}`CMPM2 <step-127>`, {ref}`CMPM3 <step-142>`, {ref}`CMPM4 <step-157>`; *inference from the film; which of the two tungsten processes not public:* {ref}`WCMPLI <step-100>`, {ref}`WCMP2 <step-111>`, {ref}`WCMP3 <step-122>`, {ref}`WCMP4 <step-133>`, {ref}`WCMP5 <step-148>`

Every page grades the tool strong and its assignment to the step an
inference from the listed film; SkyWater names no other polisher, so no
page weighs an alternative.[^skw-01]

## Consumables and facilities

The slurries, pads and cleaning chemicals are listed in the
{ref}`materials index <materials-index>` and described on the
{ref}`category page <category-cmp>`; what is specific to the polisher is
summarised here. None of the SkyWater sources describes the fab's
slurry distribution or waste treatment. Slurries, pads, conditioners,
carrier parts and post-CMP clean chemistry are described on the
{ref}`CMP consumables <material-cmp-consumables>` page. Ultrapure water,
its standards and its quality parameters are described on the
{ref}`ultrapure water <material-ultrapure-water>` page.

* **Slurries.** Silica or ceria slurries for oxide and STI, and
  oxidiser-bearing slurries for tungsten ({ref}`category-cmp`), such as
  the composition of an oxidiser and a catalyst "having multiple oxidation
  states" in a Cabot patent;[^pat-cmp-cabot] the AVANTI 472 pumped up to
  1000 ml/min and accepted slurries of pH 2 to 12.[^ipec-472-1997] Which
  slurries SkyWater uses is not public.
* **Pads and conditioners.** Stacked porous polymer pads, reconditioned
  in use;[^wiki-cmp] pads with a transparent window for optical
  endpoint;[^pat-cmp-window] diamond or other conditioner discs
  ({ref}`category-cmp`).
* **Heads.** Membranes, retaining rings and backing films wear and are
  replaced (industry practice).
* **Water and drains.** Ultrapure water for rinsing and for the transfer
  and washing stations,[^pat-cmp-mirra] and slurry-laden waste streams
  (industry practice).

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's polish recipes, slurries and
removal targets are not public; which films lie under each polish and
where each stops are this reference's readings, set out on the category
page and the step pages.

* **Three kinds of polish on one tool type.** On this reference's
  readings, {ref}`CMPNIT <step-012>` polishes the trench fill to the
  nitride, {ref}`CMPP <step-090>` the PSG over the poly (on a nitride-cap
  stop, in that page's reading), {ref}`CMPL <step-106>` and
  {ref}`CMPM <step-116>` to {ref}`CMPM4 <step-157>` the inter-level oxides
  to a remaining thickness, and {ref}`WCMPLI <step-100>` and
  {ref}`WCMP2 <step-111>` to {ref}`WCMP5 <step-148>` the tungsten
  overburden ({ref}`category-cmp`). SkyWater's list covers all three film
  types.[^skw-01]
* **Stopping without a stop layer.** On the step pages' readings the
  inter-level oxide polishes have no material change to detect,[^wiki-cmp] so they depend on timed
  removal or in-situ thickness measurement; the
  {ref}`CMPM <step-116>` page describes both, and SkyWater's "On board
  metrology with feed forward and backward" is the kind of capability
  that serves them (our reading).[^skw-01]
* **Two tungsten processes.** SkyWater lists "tungsten" and "high
  selectivity tungsten"; the tungsten polish pages say which one runs at
  each plug level is not public.[^skw-01] The tungsten polish outline on
  the {ref}`WCMPLI <step-100>` page keeps tungsten and oxide slurries on
  separate platens or heads (industry practice).
* **Pattern density.** Removal depends strongly on pattern
  density,[^stine-1998] which the {ref}`CMPM <step-116>` page connects to
  the density-based fill rules of design-rule decks.
* **Scratches over plugs.** At the plug levels a scratch in the oxide
  that fills with tungsten can short neighbouring
  lines;[^ollendorf-2004] the {ref}`WCMPLI <step-100>` page lists
  optical inspection for residual tungsten among its monitors.
* **The clean that follows.** The step pages' outlines follow each polish
  with a post-CMP clean, which must come before the slurry
  dries;[^lam-integra-1999] the CMP pages find no
  brush scrubber on SkyWater's list and name the single-wafer SEZ tools
  instead ({ref}`machine-post-cmp-cleaner`,
  {ref}`machine-single-wafer-spin-processor`).

## Related pages

* {ref}`category-cmp` — polishing physics, slurries, pads and the polishes
  of SKY130.
* {ref}`machine-post-cmp-cleaner` — the brush scrubbers and integrated
  cleaners that follow the polish.
* {ref}`machine-single-wafer-spin-processor` — the listed single-wafer
  tools the CMP pages name for the post-CMP clean.
* {ref}`machine-hdp-cvd` and {ref}`machine-pecvd` — the oxides the polisher
  planarises.
* {ref}`machine-tungsten-cvd` — the tungsten fill whose overburden the
  polisher removes.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — slurries, pads and cleaning chemicals.
* {ref}`material-cmp-consumables` — slurries, pads, conditioners and
  post-CMP clean chemistry.
* {ref}`material-ultrapure-water` — rinse water, its standards and
  quality.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

**Related patents.** 14 families concern this page (5 unknown, 9 expired).

See {ref}`patents-by-module` for the full, grouped list (families still in force or of unknown status are collapsed there too).

**Related papers.**

* {ref}`paper-smith-2006a` — Eugene Smith and Russell Elias, ISSM 2006 (affiliation inference)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater Technology, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the "AMAT Mirra CMP"
  entry, its processes and the lines that follow it.[^skw-01]
* [SkyWater Technology, Form S-1 (2021)](<https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>) — the raw-material suppliers, none
  for slurry or pads.[^sec-01]
* [Applied Materials, *1997 Annual Report*](<https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>) — the Mirra's announcement,
  architecture and Titan Head.[^amat-1997]
* [Applied Materials, 500th Mirra press release (2000)](<https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-ships-500th-mirra-cmp-system-success-mirra/>) — the installed base
  and the Mesa and metrology additions.[^amat-mirra-500-2000]
* [Applied Materials, Mirra Mesa press release (1999)](<https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-new-mirra-mesa-system-address-market>) — polishing and
  cleaning on one dry-in/dry-out system.[^amat-mesa-1999]
* [IPEC-Planar, *AVANTI 472* (1997 capture)](<https://web.archive.org/web/19970626104141/http://www.ipec.com:80/planar/472.html>) — a single-wafer, two-platen
  200 mm polisher and its conditioner and slurry system.[^ipec-472-1997]
* [IPEC-Planar, *AvantGaard 676 Highlights* (1997 capture)](<https://web.archive.org/web/19970626104827/http://www.ipec.com:80/planar/676-spec.html>) — a four-module
  polisher with integrated spray-box cleaning.[^ipec-676-1997]
* [SpeedFam-IPEC, *CMP Products* (2001 capture)](<https://web.archive.org/web/20010412141846/http://www.ipec.com:80/cmp/products.htm>) — the Momentum, Auriga and
  AvantGaard 776, zonal carriers, endpoint and integrated
  cleaners.[^speedfam-ipec-2001]
* Strasbaugh, [*6DS-SP Series Planarizers*](<https://web.archive.org/web/19990210100559/http://www.strasbaugh.com:80/cmp1.htm>) and [*Model 6EC*](<https://web.archive.org/web/19990210113246/http://www.strasbaugh.com:80/cmp2.htm>) (1999
  captures) — a dual-spindle production polisher and a laboratory
  one.[^strasbaugh-6ds-1999][^strasbaugh-6ec-1999]
* [Lam Research, 1,000th post-CMP clean system press release (2001)](<https://investor.lamresearch.com/2001-02-14-Lam-Research-Ships-1,000th-Post-CMP-Clean-System-To-Philips>) — a
  Synergy Integra cleaner on a Teres polisher.[^lam-clean-1000-2001]
* [EBARA Precision Machinery Europe, *CMP Tools*](<https://www.ebara-pm.eu/systems/cmp-tools/>) — the
  F-REX200M2.[^ebara-frex]

### High-level understanding

* [Wikipedia, *Chemical-mechanical polishing*](<https://en.wikipedia.org/wiki/Chemical-mechanical_polishing>) — the tool, pad, carrier,
  retaining ring and endpoint problem.[^wiki-cmp]
* [Chip History Center, *The Mirra CMP System*](<https://www.chiphistory.org/142-applied-materials-the-mirra-cmp-system>) — the Mirra in the history
  of CMP equipment.[^chiphistory-mirra]
* [Steigerwald, Murarka and Gutmann, *Chemical Mechanical Planarization of
  Microelectronic Materials*](<https://doi.org/10.1002/9783527617746>) — the standard monograph.[^steigerwald-1997]
* [Oliver (ed.), *Chemical-Mechanical Planarization of Semiconductor
  Materials*](<https://doi.org/10.1007/978-3-662-06234-0>) — chapters on oxide, tungsten and STI CMP, pads and
  slurries.[^oliver-2004]
* [Krishnan, Nalaskowski and Cook, *Chem. Rev.* 2010](<https://doi.org/10.1021/cr900170z>) — slurry chemistry and
  mechanisms.[^rev-02]

### Deep dive

* [Tolles et al. (Applied Materials), US 5,738,574](<https://patents.google.com/patent/US5738574A/en>) — a carousel
  multi-platen polisher whose layout matches the Mirra's.[^pat-cmp-mirra]
* [Zuniga et al. (Applied Materials), US 6,183,354](<https://patents.google.com/patent/US6183354B1/en>) — a flexible-membrane
  carrier head for uniform load.[^pat-carrier-amat]
* [Pant et al. (Lam Research), US 6,425,812](<https://patents.google.com/patent/US6425812B1/en>) — a polishing head for a linear
  polisher, with the Teres as example.[^pat-linear-lam]
* [Lustig, Saenger and Tong (IBM), US 5,433,651](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5433651>) — in-situ reflectance
  endpoint through a window in the table.[^pat-cmp-endpoint-ibm]
* [Birang, Gleason and Guthrie (Applied Materials), US 5,893,796](<https://patents.google.com/patent/US5893796A/en>) — a
  transparent window in the polishing pad.[^pat-cmp-window]
* Preston, *J. Soc. Glass Technol.* 1927 — the removal-rate law (no online
  copy is known).[^preston-1927]
* [Luo and Dornfeld, *IEEE TSM* 2001](<https://doi.org/10.1109/66.920723>) — an abrasive-contact model of
  removal rate.[^luo-2001]
* [Runnels and Eyman, *JES* 1994](<https://doi.org/10.1149/1.2054985>) — hydroplaning of the wafer on the
  pad.[^runnels-1994]
* [Stein, Hetherington and Cecchi, *JES* 1999](<https://doi.org/10.1149/1.1391617>) — tungsten polish rate and
  temperature against slurry and machine settings.[^stein-1999]
* [Nanz and Camilletti, *IEEE TSM* 1995](<https://doi.org/10.1109/66.475179>) — a review of CMP
  models.[^nanz-1995]
* [Stine et al., *IEEE TSM* 1998](<https://doi.org/10.1109/66.661292>) — test masks and pattern-density models of
  oxide CMP.[^stine-1998]
* [Bibby and Holland, *J. Electron. Mater.* 1998](<https://doi.org/10.1007/s11664-998-0140-1>) — endpoint detection for
  CMP.[^bibby-1998]
* [Kwon, Ramachandran and Park, *Friction* 2013](<https://doi.org/10.1007/s40544-013-0026-y>) — scratch formation in CMP
  and its reduction.[^kwon-2013]
* [Ollendorf, Cabral and Fuller, ASMC 2004](<https://doi.org/10.1109/ASMC.2004.1309523>) — tungsten-filled microscratches
  and a post-CMP plasma clean.[^ollendorf-2004]
* [Zantye, Kumar and Sikder, *Mater. Sci. Eng. R* 2004](<https://doi.org/10.1016/j.mser.2004.06.002>) — a long review of
  CMP for microelectronics.[^zantye-2004]

## Open questions

* Whether SkyWater's Mirra is a Mirra or a Mirra Mesa, how many polishers
  there are, and which tool performs "Track ammonia clean" and "IPA
  clean", are not stated.[^skw-01]
* What "high selectivity tungsten" denotes, and which tungsten process
  runs at each SKY130 plug level, are not public.
* SkyWater's slurries, pads, conditioners and endpoint methods for the
  SKY130 polishes are not public.
* The model list above is incomplete: it covers the Applied, IPEC and
  SpeedFam-IPEC, Strasbaugh, Lam and Ebara tools for which a public
  description was found, not every 200 mm polisher of the period.

<!-- footnotes -->

[^pat-carrier-amat]: S. M. Zuniga, M. Birang, H. Chen and S.-H. Ko
    (Applied Materials), *Carrier head with a flexible membrane for a
    chemical mechanical polishing system*, US 6,183,354 B1, filed
    1997-05-21, granted 2001-02-06.
    <https://patents.google.com/patent/US6183354B1/en>
[^preston-1927]: F. W. Preston, "The theory and design of plate glass
    polishing machines", *Journal of the Society of Glass Technology*
    **11**, 214–256 (1927).
[^luo-2001]: J. Luo and D. A. Dornfeld, "Material removal mechanism in
    chemical mechanical polishing: theory and modeling", *IEEE
    Transactions on Semiconductor Manufacturing* **14**(2), 112–133
    (2001). <https://doi.org/10.1109/66.920723>
[^pat-cmp-mirra]: R. D. Tolles, N. Shendon, S. Somekh, I. Perlov, E.
    Gantvarg and H. Q. Lee (Applied Materials), *Continuous processing
    system for chemical mechanical polishing*, US 5,738,574 A, granted
    1998-04-14. <https://patents.google.com/patent/US5738574A/en>
[^pat-linear-lam]: A. K. Pant, D. W. Young, G. Travis, K. Volodarsky, A.
    Nagengast et al. (Lam Research), *Polishing head for chemical
    mechanical polishing using linear planarization technology*, US
    6,425,812 B1, filed 1999-12-30, granted 2002-07-30.
    <https://patents.google.com/patent/US6425812B1/en>
[^wiki-cmp]: Wikipedia, *Chemical-mechanical polishing*.
    <https://en.wikipedia.org/wiki/Chemical-mechanical_polishing>
[^pat-cmp-endpoint-ibm]: N. E. Lustig, K. L. Saenger and H.-M. Tong
    (IBM), *In-situ endpoint detection and process monitoring method and
    apparatus for chemical-mechanical polishing*, US 5,433,651 A, granted
    1995-07-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5433651>
[^pat-cmp-window]: M. Birang, A. Gleason and W. L. Guthrie (Applied
    Materials), *Forming a transparent window in a polishing pad for a
    chemical mechanical polishing apparatus*, US 5,893,796 A, granted
    1999-04-13. <https://patents.google.com/patent/US5893796A/en>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report* (Form 10-K
    for the fiscal year ended 1997-10-26).
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^ipec-472-1997]: IPEC-Planar, *AVANTI 472*, product page; Wayback
    Machine capture of 1997-06-26.
    <https://web.archive.org/web/19970626104141/http://www.ipec.com:80/planar/472.html>
[^strasbaugh-6ds-1999]: Strasbaugh, *The 6DS-SP Series Planarizers*,
    product page; Wayback Machine capture of 1999-02-10.
    <https://web.archive.org/web/19990210100559/http://www.strasbaugh.com:80/cmp1.htm>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; CMP entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^stein-1999]: D. Stein, D. L. Hetherington and J. L. Cecchi,
    "Investigation of the Kinetics of Tungsten Chemical Mechanical
    Polishing in Potassium Iodate-Based Slurries: I. Role of Alumina and
    Potassium Iodate", *Journal of The Electrochemical Society*
    **146**(1), 376–381 (1999). <https://doi.org/10.1149/1.1391617>
[^runnels-1994]: S. R. Runnels and L. M. Eyman, "Tribology Analysis of
    Chemical-Mechanical Polishing", *Journal of The Electrochemical
    Society* **141**(6), 1698–1701 (1994).
    <https://doi.org/10.1149/1.2054985>
[^nanz-1995]: G. Nanz and L. E. Camilletti, "Modeling of
    chemical-mechanical polishing: a review", *IEEE Transactions on
    Semiconductor Manufacturing* **8**(4), 382–389 (1995).
    <https://doi.org/10.1109/66.475179>
[^rev-02]: M. Krishnan, J. W. Nalaskowski and L. M. Cook, "Chemical
    Mechanical Planarization: Slurry Chemistry, Materials, and
    Mechanisms", *Chemical Reviews* **110**(1), 178–204 (2010).
    <https://doi.org/10.1021/cr900170z>
[^speedfam-ipec-2001]: SpeedFam-IPEC CMP Group, *Products* (Momentum,
    Auriga, AvantGaard), product page; Wayback Machine capture of
    2001-04-12.
    <https://web.archive.org/web/20010412141846/http://www.ipec.com:80/cmp/products.htm>
[^bibby-1998]: T. Bibby and K. Holland, "Endpoint detection for CMP",
    *Journal of Electronic Materials* **27**(10), 1073–1081 (1998).
    <https://doi.org/10.1007/s11664-998-0140-1>
[^stine-1998]: B. E. Stine, D. O. Ouma, R. R. Divecha, D. S. Boning, J.
    E. Chung, D. L. Hetherington, C. R. Harwood, O. S. Nakagawa and
    S.-Y. Oh, "Rapid characterization and modeling of pattern-dependent
    variation in chemical-mechanical polishing", *IEEE Transactions on
    Semiconductor Manufacturing* **11**(1), 129–140 (1998).
    <https://doi.org/10.1109/66.661292>
[^kwon-2013]: T.-Y. Kwon, M. Ramachandran and J.-G. Park, "Scratch
    formation and its mechanism in chemical mechanical planarization
    (CMP)", *Friction* **1**(4), 279–305 (2013).
    <https://doi.org/10.1007/s40544-013-0026-y>
[^ollendorf-2004]: H. Ollendorf, S. Cabral and R. Fuller, "Reduction of
    CMP μ-scratch induced metal shorts by introduction of a post CMP
    tungsten plasma clean process in a high volume DRAM manufacturing
    environment", *2004 IEEE/SEMI Advanced Semiconductor Manufacturing
    Conference and Workshop*, pp. 1–4.
    <https://doi.org/10.1109/ASMC.2004.1309523>
[^lam-integra-1999]: Lam Research, *Lam Research Corporation Ships 100th
    Synergy Integra Integrated CMP Cleaning System*, press release,
    1999-06-17, accessed 2026-09-13.
    <https://newsroom.lamresearch.com/1999-06-17-Lam-Research-Corporation-Ships-100th-Synergy-IntegraTM-Integrated-CMP-Cleaning-System>
[^amat-mesa-1999]: Applied Materials, *Applied Materials Announces New
    Mirra Mesa System to Address Market Demand for Integrated CMP
    Solutions*, press release, 1999-06-10, accessed 2026-09-13.
    <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-new-mirra-mesa-system-address-market>
[^amat-mirra-500-2000]: Applied Materials, *Applied Materials Ships 500th
    Mirra CMP System*, press release, 2000-02-22, accessed 2026-09-13.
    <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-ships-500th-mirra-cmp-system-success-mirra/>
[^chiphistory-mirra]: Chip History Center, *The Mirra CMP System by
    Applied Materials*.
    <https://www.chiphistory.org/142-applied-materials-the-mirra-cmp-system>
[^ipec-676-1997]: IPEC-Planar, *IPEC AvantGaard 676 Highlights*, product
    page; Wayback Machine capture of 1997-06-26.
    <https://web.archive.org/web/19970626104827/http://www.ipec.com:80/planar/676-spec.html>
[^strasbaugh-6ec-1999]: Strasbaugh, *The Model 6EC Laboratory
    Planarizer*, product page; Wayback Machine capture of 1999-02-10.
    <https://web.archive.org/web/19990210113246/http://www.strasbaugh.com:80/cmp2.htm>
[^lam-clean-1000-2001]: Lam Research, *Lam Research Ships 1,000th
    Post-CMP Clean System To Philips*, press release, 2001-02-14,
    accessed 2026-09-13.
    <https://investor.lamresearch.com/2001-02-14-Lam-Research-Ships-1,000th-Post-CMP-Clean-System-To-Philips>
[^ebara-frex]: EBARA Precision Machinery Europe, *CMP Tools*
    (F-REX200M2), accessed 2026-09-13.
    <https://www.ebara-pm.eu/systems/cmp-tools/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22; "Raw materials." paragraph re-read from the Wayback
    Machine capture of 2021-04-13 on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^pat-cmp-cabot]: Cabot Corporation, *Composition and slurry useful for
    metal CMP*, US 5,958,288 A, filed 1996-11-26, granted 1999-09-28.
    <https://patents.google.com/patent/US5958288A/en>
[^steigerwald-1997]: J. M. Steigerwald, S. P. Murarka and R. J. Gutmann,
    *Chemical Mechanical Planarization of Microelectronic Materials*,
    Wiley, 1997, ISBN 978-0-471-13827-6.
    <https://doi.org/10.1002/9783527617746>
[^oliver-2004]: M. R. Oliver (ed.), *Chemical-Mechanical Planarization of
    Semiconductor Materials*, Springer Series in Materials Science 69,
    Springer, 2004, ISBN 978-3-540-43181-9.
    <https://doi.org/10.1007/978-3-662-06234-0>
[^zantye-2004]: P. B. Zantye, A. Kumar and A. K. Sikder, "Chemical
    mechanical planarization for microelectronics applications",
    *Materials Science and Engineering: R* **45**(3–6), 89–220 (2004).
    <https://doi.org/10.1016/j.mser.2004.06.002>
