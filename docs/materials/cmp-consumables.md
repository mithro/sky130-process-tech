(material-cmp-consumables)=
# CMP consumables

Chemical-mechanical planarisation ({term}`CMP`) is a process whose
consumables wear out as fast as they are used. A polisher
presses the wafer against a rotating pad flooded with slurry — abrasive
particles in a chemically active liquid — while a diamond disc keeps the
pad surface open and a carrier head holds the wafer through a membrane
and retaining ring; after the polish, brushes and dilute chemistry
remove the slurry before it dries. On the step pages' readings, SKY130
has twelve polishes: seven oxide polishes, among them the STI polish
over nitride and a sacrificial glass polish, and five tungsten polishes
that leave the {term}`W plugs <W plug>`, each consuming slurry, pad,
conditioner and a {term}`post-CMP clean`. This page describes the class
in general, lists representative slurries, pads and cleaning chemistries,
and then says what SkyWater has published about CMP at its fab and which
SKY130 steps name these consumables. The polishing physics is on the
{ref}`CMP category page <category-cmp>`, and the tools on the
{ref}`CMP polisher <machine-cmp-polisher>` and
{ref}`post-CMP cleaner <machine-post-cmp-cleaner>` pages.

| | CMP consumables |
|---|---|
| What they do | Remove and planarise films by combined chemical and mechanical action; CMP "can be thought of as a hybrid of chemical etching and free abrasive polishing".[^wiki-cmp] |
| Slurries | Silica or ceria abrasives for oxide ("The principal industrial application of ceria is for polishing, especially chemical-mechanical planarization");[^wiki-ceria] for tungsten, "an oxidizing agent and at least one catalyst having multiple oxidation states".[^pat-cmp-cabot] |
| Pads and conditioners | Pads "made from porous polymeric materials with a pore size between 30 and 50 μm", which "must be regularly reconditioned";[^wiki-cmp] diamond "shape, size, density and protrusion" of conditioners affect "pad cut rate and wafer removal rate".[^kakireddy-2010] |
| Carrier parts | A flexible membrane, gimbal and retaining ring in the carrier head.[^pat-carrier-amat] |
| Post-CMP clean | Brush scrubbers whose brushes "are constantly flushed with deionized water to inhibit particle buildup";[^pat-scrubber-ontrak] dilute ammonia, HF, citric acid or TMAH ({ref}`category-cmp`).[^jolley-1998] |
| Defects | Large slurry particles and pad debris scratch; in one production fab "A strong correlation was found between defects and the total particle count" of slurry large particles.[^bennett-2014] |
| SkyWater evidence | "AMAT Mirra CMP" with "oxide", "nitride", "tungsten" and "high selectivity tungsten", "Track ammonia clean", "IPA clean";[^skw-01] "CMC Chemicals, Inc. (a subsidiary of Entegris) (process and chemical mechanical polishing chemicals)"[^sec-02] |
| SKY130 steps | 12 steps; see {ref}`SKY130 steps that use this class <material-cmp-consumables-steps>` |

## What the class is and what it does

A CMP process is set as much by its consumables as by its tool. The
slurry supplies the chemistry that softens the surface and the abrasive
that removes it; the pad carries slurry and transmits pressure; the
conditioner restores the pad; the carrier parts set how uniformly the
wafer is loaded; and the post-CMP clean decides what is left behind.
Wikipedia summarises the arrangement: "an abrasive and corrosive chemical
slurry (commonly a colloid) in conjunction with a polishing pad and
retaining ring", with the wafer "held in place by a plastic retaining
ring".[^wiki-cmp] Removal roughly follows Preston's law, rate
proportional to pressure and velocity ({term}`Preston equation`), with a
coefficient that absorbs pad, slurry and film; Luo and Dornfeld model it
as the number of active abrasive particles times the volume each
removes.[^luo-2001] Steigerwald, Murarka and Gutmann's monograph and
Zantye, Kumar and Sikder's review cover the whole class.[^steigerwald-1997][^zantye-2004]

### Oxide slurries

Oxide polishing inherits the chemistry of glass polishing, whose chemical
processes Cook's paper sets out.[^cook-1990] Production oxide slurries use
fumed or colloidal silica in an alkaline, KOH- or ammonia-stabilised
liquid ({ref}`category-cmp`), or ceria, whose mechanism of polishing
silica Hoshino et al. examined.[^hoshino-2001]
Krishnan, Nalaskowski and Cook review the slurry chemistries and
mechanisms.[^rev-02] For the STI polish, the slurry must stop on nitride:
America and Babu showed that nitride removal "occurs through tribological
wear-induced conversion of the nitride to an oxide" and can be
suppressed by additives, proline in particular, with ceria
abrasives.[^america-2004] Kim et al. found that a ceria high-selectivity
slurry reduced the variation of remaining pad nitride and field-oxide
erosion "to ∼150 and ∼400 Å" for 0.18 µm STI, and that scratches, "∼80%
of the total defect", were minimised by in-situ filtering.[^kim-2002-ceria]

### Tungsten slurries

A tungsten slurry must oxidise the metal as well as abrade it. Kaufman et
al. described tungsten CMP for patterned interconnect
features;[^kaufman-1991] Cabot's patent describes "a chemical mechanical
polishing composition comprising an oxidizing agent and at least one
catalyst having multiple oxidation states";[^pat-cmp-cabot] and Stein,
Hetherington and Cecchi, polishing in potassium iodate slurries with
alumina, found the rate "fit a multiterm regression model better than
the empirical Preston equation" and that "the chemical and physical
interactions between the alumina and tungsten surfaces are complex".[^stein-1999]
The step pages list alumina or silica abrasive with hydrogen peroxide,
ferric nitrate or iodate oxidiser as the industry-typical
choice.[^rev-02][^pat-cmp-cabot]

### Pads, conditioners and carrier parts

Pads "are often just stacks of soft and hard materials that conform to
wafer topography to some extent", and "are usually referred to by their
trademark names rather than their chemical or other
properties".[^wiki-cmp] A Rodel patent describes a pad of "a polymeric matrix impregnated with a plurality of
polymeric microelements, each polymeric microelement having a void space
therein", whose work surface "may be continuously regenerated" as it is
abraded.[^pat-pad-rodel] The pad surface glazes, and conditioning cuts it
back: Castillo-Mejia, Kelchner and Beaudoin modelled the asperity layer
and showed that pad morphology improves removal-rate and uniformity
prediction,[^castillo-mejia-2004] and Kakireddy et al. found that
conditioners with uneven diamonds "exhibited high drop in pad cut rate
and wafer removal rate", with diamonds "missing or sheared off" on some
tested conditioners.[^kakireddy-2010] Pads for in-situ optical endpoint
carry a transparent window.[^pat-cmp-window] In the carrier head, an
Applied Materials patent explains why a non-uniform load gives
non-uniform removal and describes a flexible membrane with a retaining
ring;[^pat-carrier-amat] membranes and rings wear and are replaced
(industry practice).

### Post-CMP cleaning

Slurry must not dry on the wafer. OnTrak's scrubber patent aims "to
provide a semiconductor processing device that prevents semiconductor
wafers from drying between processing steps" and states that the brushes of such scrubbers "are constantly flushed
with deionized water to inhibit particle buildup".[^pat-scrubber-ontrak]
Zhang, Raghavan and Weling call CMP "inherently a dirty process" and
classify its defects as "particulate, metallic, organic, and
others";[^zhang-raghavan-1999] Xu et al. showed that brush scrubbing
removes particles by rolling them;[^xu-2004] and Philipossian and Sun
compared the friction of PVA brush-roller designs.[^philipossian-2009]
For tungsten, Jolley studied TMAH as a post-tungsten-CMP clean,[^jolley-1998]
and Ge et al. traced metal-1 bridges to organic particles from a
post-tungsten-contact brush station.[^ge-2006]

## Representative materials and grades

Slurries, pads and cleaning chemistries are proprietary products bought
by name and qualified per process; no SEMI purity standard governs them
as it does bulk chemicals. The supplier statements below describe their
catalogues, not SkyWater's purchases, even where the supplier's parent is
named in SkyWater's filings.

* **Oxide slurries.** Fumed or colloidal silica in KOH or ammonia at pH
  10–11 (typical industry values);[^steigerwald-1997][^zantye-2004]
  the category page names the Cabot Semi-Sperse SS-12 and Klebosol
  classes ({ref}`category-cmp`). Ceria slurries with additives for STI
  selectivity.[^america-2004][^kim-2002-ceria]
* **Tungsten slurries.** Alumina or silica with a peroxide, ferric or
  iodate oxidiser at pH 2–4 (typical industry
  values).[^pat-cmp-cabot][^stein-1999][^steigerwald-1997]
* **Pads.** Stacked polyurethane pads of the IC1000-over-Suba IV class for
  primary polish and soft Politex-type pads for buffing
  ({ref}`category-cmp`). Qnity (the electronics business DuPont planned to
  separate as an independent company[^qnity-story]) lists "IC1000™" among its pads for tungsten, STI
  and oxide polishing and "Politex™" for buff polishing.[^qnity-cmp-pads]
* **Conditioners, brushes and filters.** Entegris states that, with CMC
  Materials, its CMP offering includes "CMP slurries and pads",
  "post-CMP cleaning chemistries and brushes, CMP pad conditioners" and
  liquid filtration.[^entegris-cmc-2022]
* **Post-CMP clean chemistry.** Dilute NH₄OH after oxide polishes; dilute
  HF, citric acid or TMAH after tungsten;[^jolley-1998] integrated
  cleaners used HF in brush modules and heated RCA chemistries in
  megasonic modules.[^amat-mesa-1999] Entegris lists "post chemical
  mechanical planarization (post-CMP) cleaning solutions" that "offer
  excellent corrosion control".[^entegris-post-cmp]

## At SkyWater

### What SkyWater's filings and pages list

Under "CMP", SkyWater's *Facilities & Capabilities* page lists one
polisher and three further lines:[^skw-01]

> "AMAT Mirra CMP"
> – "oxide" – "nitride" – "niobium" – "aluminum" – "tungsten" – "high
> selectivity tungsten" – "copper"
>
> "Track ammonia clean" · "IPA clean" · "On board metrology with feed
> forward and backward"

Read term by term, the entry names oxide, nitride and tungsten polishes,
which imply oxide and tungsten slurries, and a "high selectivity
tungsten" process that the page does not explain; "Track ammonia clean"
names an ammonia chemistry for a clean, which the step pages read as the
post-CMP clean of the Mirra entry. The page names no slurry, pad,
conditioner or brush.[^skw-01] The filings list chemical
suppliers:[^sec-01][^sec-02]

| Filing | Chemical suppliers as named |
|--------|-----------------------------|
| S-1 (2021)[^sec-01] | "KMG Chemicals, Inc. (chemicals)"; "Air Products & Chemicals, Inc. (bulk and specialty gases, chemicals)" |
| 10-K for fiscal 2023[^sec-02] | "CMC Chemicals, Inc. (a subsidiary of Entegris) (process and chemical mechanical polishing chemicals)"; "EMD Performance Materials Corp (Versum) (specialty chemicals and gases)" |

The 10-K entry is the only statement in the sources cited here that names
a supplier of CMP materials, and it names "chemical mechanical polishing chemicals",
not slurries, pads or a product. Entegris states that it acquired CMC
Materials and announced the close of the transaction on
2022-07-06,[^entegris-cmc-2022]
and Wikipedia that CMC Materials was "previously known as Cabot
Microelectronics Corp";[^wiki-entegris] neither names "CMC Chemicals,
Inc." or SkyWater. SkyWater's maintenance-technician profile mentions "a
SEZ etcher tool",[^skw-07] a make that the capabilities page lists under
"Single Wafer" wet processing ("SEZ223"),[^skw-01] which several CMP step pages consider for the
post-CMP clean.

### Strength of the evidence

The Mirra entry and its polishes are SkyWater statements and rank as
**strong** evidence that oxide, nitride and tungsten polishing, and an
ammonia and an IPA clean, exist at the fab, on the scale of the
{ref}`machines index <machines-reading-evidence>`; that they imply silica,
ceria or tungsten slurries is a reading.[^skw-01] The 10-K supplier entry
is strong as a statement that CMP chemicals are bought from CMC Chemicals,
but it names no product and appears only in the fiscal 2023
report.[^sec-02] Pads, conditioners, carrier parts, brushes and the
post-CMP clean chemistry appear in no SkyWater source cited here; the
step pages' descriptions of them are industry practice.

(material-cmp-consumables-steps)=
### SKY130 steps that use this class

This page covers the rows of the {ref}`materials index <materials-table>`
listed below by key; the steps are those whose *Resources required* section
names one of them (the union of the rows' *Steps* cells).

Materials index rows covered:

* `post-cmp-clean` — post-CMP clean chemistry and PVA brushes
* `oxide-slurry` — oxide CMP slurry
* `w-slurry` — tungsten CMP slurry
* `cmp-pads` — CMP pads, conditioners and carrier parts

Steps:

{ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>`

These are the twelve steps of the
{ref}`CMP category <category-cmp>`. On the step pages' readings, the
oxide slurry serves {ref}`CMPNIT <step-012>` (silica or ceria, stopping on
nitride), {ref}`CMPP <step-090>` and {ref}`CMPL <step-106>` and the four
inter-metal oxide polishes; the tungsten slurry serves
{ref}`WCMPLI <step-100>`, the metal-contact polish
{ref}`WCMP2 <step-111>` and the three via polishes; and every step
names pads, conditioners and a post-CMP clean.

## Supply, handling, safety and facilities

None of the SkyWater sources cited here describes slurry distribution,
pad supply or CMP waste treatment; the points below are industry
practice or supplier and literature statements.

* **Slurry distribution and filtration.** Slurry is mixed and circulated
  in a slurry distribution system and filtered at the point of use;
  Bennett and Fury monitored large particles in a production fab's
  distribution loop and at the tool and found defects correlated with
  "the total particle count in the smallest (1.0-1.2μm) particle
  bin".[^bennett-2014] Scratches from agglomerates and large particles are
  reviewed by Kwon, Ramachandran and Park, who cover filtration and water
  jet spraying against them.[^kwon-2013]
* **Consumption.** The category page gives slurry use of a few hundred
  millilitres per wafer per platen and pad life of a few hundred to a
  thousand wafers as typical industry
  figures;[^zantye-2004][^steigerwald-1997] one 200 mm polisher of the
  period pumped slurry at up to 1000 ml/min and accepted slurries of pH 2
  to 12.[^ipec-472-1997]
* **Oxidisers.** Tungsten slurries are mixed with peroxide or ferric
  oxidisers; hydrogen peroxide is described on the
  {ref}`wet chemicals <material-wet-chemicals>` page.
* **Water and waste.** The step pages cite Quirk and Serda for CMP as
  one of a fab's largest water and waste-water users, and the tungsten
  pages for a separate treatment line for metal-laden acidic
  waste;[^txt-07] Lai and Lin treated CMP waste water from semiconductor fabrication by
  electrocoagulation.[^lai-2003] Ultrapure water and waste treatment are
  described on the {ref}`ultrapure water <material-ultrapure-water>` and
  {ref}`hardware consumables and abatement <material-hardware-consumables>`
  pages.
* **Tungsten defects.** Tungsten-filled micro-scratches can short lines;
  Ollendorf, Cabral and Fuller removed them with a post-CMP tungsten
  plasma clean in a DRAM fab.[^ollendorf-2004]

## Process-integration notes for SKY130

These notes connect the class to the step pages; they add no SKY130
conditions of their own. SKY130's slurries, pads and clean recipes are
not public.

* **Selectivity at the STI polish.** The {ref}`CMPNIT <step-012>` page
  describes a silica or ceria slurry stopping on the isolation nitride;
  additive ceria slurries suppress nitride removal[^america-2004] and
  reduce erosion variation,[^kim-2002-ceria] and SkyWater lists a
  "nitride" polish on its Mirra.[^skw-01] Which slurry SKY130 uses is not
  public.
* **Two tungsten processes.** SkyWater lists "tungsten" and "high
  selectivity tungsten";[^skw-01] the five tungsten step pages do not say
  which runs where. A slurry with higher selectivity to oxide would
  reduce oxide erosion in dense plug arrays (the category page's
  failure-mode table), at the risk of plug recess (our reading).
* **Fixed-removal oxide polishes.** The inter-metal polishes stop on no
  layer ({ref}`category-cmp`), so their final thickness depends on pad and
  conditioner state as well as time; pad cut rate and removal rate drift
  as conditioner diamonds wear,[^kakireddy-2010] which is why the step
  pages lean on SkyWater's "On board metrology with feed forward and
  backward".[^skw-01]
* **Ammonia after oxide, acid or TMAH after tungsten.** The oxide pages
  name dilute NH₄OH for the clean, matching SkyWater's "Track ammonia
  clean" (the {ref}`CMPM4 <step-157>` page's reading), and the tungsten
  pages dilute NH₄OH or TMAH, possibly citric acid or dilute
  HF.[^skw-01][^jolley-1998]
* **The STI polish comes before the gate oxides.** In the step order,
  {ref}`CMPNIT <step-012>` is the only polish before
  {ref}`GOX100 <step-043>`; Kim et al. found that in-situ filtering of
  their STI slurry improved the gate-oxide integrity of MOS capacitors
  built afterwards,[^kim-2002-ceria] so STI slurry filtration bears on the
  gate oxides (our reading).

## Related pages

* {ref}`category-cmp` — polishing physics, the SKY130 polishes and their
  failure modes.
* {ref}`machine-cmp-polisher` — the polisher that consumes slurry, pads
  and carrier parts.
* {ref}`machine-post-cmp-cleaner` — brushes and post-CMP clean chemistry.
* {ref}`material-wet-chemicals` — hydrogen peroxide, HF and ammonia as
  bulk chemicals.
* {ref}`material-ultrapure-water` — the water of the polish and clean.
* {ref}`materials-index` — all consumable classes.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,578,362 A <patent-gp25461879>` — Polymeric polishing pad containing hollow polymeric microelements (1992)
* {ref}`US 5,442,828 A <patent-gp25529547>` — Double-sided wafer scrubber with a wet submersing silicon wafer indexer (1992)
* {ref}`US 5,893,796 A <patent-gp24770421>` — Forming a transparent window in a polishing pad for a chemical mechanical polishing apparatus (1995)
* {ref}`US 6,183,354 B1 <patent-gp24997773>` — Carrier head with a flexible membrane for a chemical mechanical polishing system (1996)
* {ref}`US 5,958,288 A <patent-gp25030826>` — Composition and slurry useful for metal CMP (1996)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the "AMAT Mirra CMP"
  entry, its polishes and cleans.[^skw-01]
* SkyWater Technology, Form S-1 (2021) and Form 10-K for fiscal 2023 —
  chemical suppliers, including "CMC Chemicals, Inc.".[^sec-01][^sec-02]
* SkyWater Technology, maintenance-technician profile — the SEZ
  tool.[^skw-07]
* Entegris, *CMC Materials | July 2022* and *Semiconductor Cleaning
  Solutions* — the acquisition and the CMP consumables
  offered.[^entegris-cmc-2022][^entegris-post-cmp]
* Qnity Electronics, *CMP Pads* and *Our story* — current pad lines and
  the company's DuPont origin.[^qnity-cmp-pads][^qnity-story]
* Cabot, US 5,958,288 — an oxidiser-and-catalyst tungsten
  slurry.[^pat-cmp-cabot]
* Applied Materials, Mirra Mesa release — integrated cleaner
  chemistries.[^amat-mesa-1999]

### High-level understanding

* Wikipedia, *Chemical-mechanical polishing*, *Cerium(IV) oxide* and
  *Colloidal silica* — pads, abrasives and slurry
  particles.[^wiki-cmp][^wiki-ceria][^wiki-colloidal-silica]
* Wikipedia, *Entegris* — CMC Materials' acquisition and its former name,
  Cabot Microelectronics.[^wiki-entegris]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — CMP on the
  fab floor, with its water and waste.[^txt-07]
* Oliver (ed.), *Chemical-Mechanical Planarization of Semiconductor
  Materials* — chapters on dielectric and metal CMP and
  cleaning.[^oliver-2004]
* Steigerwald, Murarka and Gutmann, *Chemical Mechanical Planarization of
  Microelectronic Materials* — pads, slurries and process
  control.[^steigerwald-1997]
* IPEC-Planar, *AVANTI 472* — slurry delivery on a 200 mm polisher of
  the period.[^ipec-472-1997]

### Deep dive

* Cook, *J. Non-Cryst. Solids* 1990 — the chemistry of oxide
  polishing.[^cook-1990]
* Kaufman et al., *JES* 1991 — tungsten CMP for interconnect.[^kaufman-1991]
* Stein, Hetherington and Cecchi, *JES* 1999 — tungsten polishing kinetics
  with alumina and iodate.[^stein-1999]
* Hoshino et al., *J. Non-Cryst. Solids* 2001 — how ceria polishes
  silica.[^hoshino-2001]
* America and Babu, *ESSL* 2004 — additives that suppress nitride
  removal.[^america-2004]
* Kim et al., *JVST B* 2002 — a ceria high-selectivity STI slurry in
  0.18 µm CMOS.[^kim-2002-ceria]
* Krishnan, Nalaskowski and Cook, *Chem. Rev.* 2010 — slurry chemistry
  and mechanisms.[^rev-02]
* Zantye, Kumar and Sikder, *Mater. Sci. Eng. R* 2004 — a long review of
  CMP and its consumables.[^zantye-2004]
* Luo and Dornfeld, *IEEE TSM* 2001 — abrasive-contact removal
  model.[^luo-2001]
* Reinhardt et al. (Rodel), US 5,578,362 — the microelement-filled
  polymer pad.[^pat-pad-rodel]
* Castillo-Mejia, Kelchner and Beaudoin, *JES* 2004 — pad surface
  morphology and removal.[^castillo-mejia-2004]
* Kakireddy et al., *ECS Trans.* 2010 — conditioner diamonds, pad cut
  rate and removal rate.[^kakireddy-2010]
* Zuniga et al. (Applied Materials), US 6,183,354 — a membrane carrier
  head.[^pat-carrier-amat]
* Birang, Gleason and Guthrie (Applied Materials), US 5,893,796 — a
  window pad for optical endpoint.[^pat-cmp-window]
* Bennett and Fury, ICPT 2014 — slurry large-particle counts against
  production defects.[^bennett-2014]
* Kwon, Ramachandran and Park, *Friction* 2013 — scratch formation and
  its prevention.[^kwon-2013]
* Lutz (OnTrak), US 5,442,828 — a double-sided scrubber with a wet
  indexer.[^pat-scrubber-ontrak]
* Zhang, Raghavan and Weling, *JVST B* 1999 — CMP defects and post-CMP
  cleaning.[^zhang-raghavan-1999]
* Xu et al., *JVST B* 2004 — particle removal by brush
  scrubbing.[^xu-2004]
* Philipossian and Sun, *ESSL* 2009 — PVA brush roller
  designs.[^philipossian-2009]
* Jolley, *Solid State Phenomena* 1998 — TMAH after tungsten
  CMP.[^jolley-1998]
* Ge et al., ICSICT 2006 — post-tungsten-CMP clean and metal
  bridging.[^ge-2006]
* Ollendorf, Cabral and Fuller, ASMC 2004 — tungsten micro-scratch
  shorts.[^ollendorf-2004]
* Lai and Lin, *Chem. Eng. J.* 2003 — electrocoagulation of CMP waste
  water.[^lai-2003]

## Open questions

* Which slurries, pads, conditioners, brushes and cleaning chemistries
  SKY130's polishes use, and from which suppliers, is not
  public.[^skw-01][^sec-02]
* What "high selectivity tungsten" and "Track ammonia clean" denote, and
  which tool performs the post-CMP clean, are not stated.[^skw-01]
* What CMP materials "CMC Chemicals, Inc." supplies, and whether "KMG
  Chemicals, Inc." in the S-1 is the same business, is not stated by any
  source cited here.[^sec-01][^sec-02][^entegris-cmc-2022]
* How SkyWater distributes slurry and treats CMP waste water is not
  public.

<!-- footnotes -->

[^wiki-cmp]: Wikipedia, *Chemical-mechanical polishing*.
    <https://en.wikipedia.org/wiki/Chemical-mechanical_polishing>
[^wiki-ceria]: Wikipedia, *Cerium(IV) oxide*.
    <https://en.wikipedia.org/wiki/Cerium(IV)_oxide>
[^pat-cmp-cabot]: B. L. Mueller, C. C. Streinz and S. K. Grumbine (Cabot
    Corporation), *Composition and slurry useful for metal CMP*,
    US 5,958,288 A, filed 1996-11-26, granted 1999-09-28.
    <https://patents.google.com/patent/US5958288A/en>
[^kakireddy-2010]: R. Kakireddy, A. Galpin, J. Smith and D. Slutz,
    "Effects of CMP Pad Conditioner Properties and Performance on
    Polishing Pad, Process and Wafer Removal Rate", *ECS Transactions*
    **33**(10), 157–163 (2010). <https://doi.org/10.1149/1.3489056>
[^pat-carrier-amat]: S. M. Zuniga, M. Birang, H. Chen and S.-H. Ko
    (Applied Materials), *Carrier head with a flexible membrane for a
    chemical mechanical polishing system*, US 6,183,354 B1, filed
    1997-05-21, granted 2001-02-06.
    <https://patents.google.com/patent/US6183354B1/en>
[^pat-scrubber-ontrak]: R. A. Lutz (OnTrak Systems), *Double-sided wafer
    scrubber with a wet submersing silicon wafer indexer*, US 5,442,828 A,
    filed 1992-11-30, granted 1995-08-22.
    <https://patents.google.com/patent/US5442828A/en>
[^jolley-1998]: M. E. Jolley, "Applications of Tetramethylammoninium
    Hydroxide (TMAH) as a Post Tungsten CMP Cleaning Mixture", *Solid
    State Phenomena* **65–66**, 105–108 (1998).
    <https://doi.org/10.4028/www.scientific.net/SSP.65-66.105>
[^bennett-2014]: J. Bennett and M. A. Fury, "Correlation of large
    particle count data in CMP slurry with production wafer defects",
    *Proceedings of International Conference on Planarization/CMP
    Technology (ICPT 2014)*, pp. 50–53.
    <https://doi.org/10.1109/ICPT.2014.7017243>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; CMP entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; "Raw materials" paragraph; read from a Wayback Machine
    copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^luo-2001]: J. Luo and D. A. Dornfeld, "Material removal mechanism in
    chemical mechanical polishing: theory and modeling", *IEEE
    Transactions on Semiconductor Manufacturing* **14**(2), 112–133
    (2001). <https://doi.org/10.1109/66.920723>
[^steigerwald-1997]: J. M. Steigerwald, S. P. Murarka and R. J. Gutmann,
    *Chemical Mechanical Planarization of Microelectronic Materials*,
    Wiley, 1997, ISBN 978-0-471-13827-6.
    <https://doi.org/10.1002/9783527617746>
[^zantye-2004]: P. B. Zantye, A. Kumar and A. K. Sikder, "Chemical
    mechanical planarization for microelectronics applications",
    *Materials Science and Engineering: R* **45**(3–6), 89–220 (2004).
    <https://doi.org/10.1016/j.mser.2004.06.002>
[^cook-1990]: L. M. Cook, "Chemical processes in glass polishing",
    *Journal of Non-Crystalline Solids* **120**(1–3), 152–171 (1990).
    <https://doi.org/10.1016/0022-3093(90)90200-6>
[^hoshino-2001]: T. Hoshino, Y. Kurata, Y. Terasaki and K. Susa,
    "Mechanism of polishing of SiO₂ films by CeO₂ particles", *Journal
    of Non-Crystalline Solids* **283**(1–3), 129–136 (2001).
    <https://doi.org/10.1016/S0022-3093(01)00364-7>
[^rev-02]: M. Krishnan, J. W. Nalaskowski and L. M. Cook, "Chemical
    Mechanical Planarization: Slurry Chemistry, Materials, and
    Mechanisms", *Chemical Reviews* **110**(1), 178–204 (2010).
    <https://doi.org/10.1021/cr900170z>
[^america-2004]: W. G. America and S. V. Babu, "Slurry Additive Effects
    on the Suppression of Silicon Nitride Removal during CMP",
    *Electrochemical and Solid-State Letters* **7**(12), G327 (2004).
    <https://doi.org/10.1149/1.1817870>
[^kim-2002-ceria]: S.-D. Kim, I.-S. Hwang, H.-M. Park, J.-K. Rhee and
    C.-W. Nam, "Chemical mechanical polishing of shallow trench isolation
    using the ceria-based high selectivity slurry for sub-0.18 μm
    complementary metal–oxide–semiconductor fabrication", *Journal of
    Vacuum Science & Technology B* **20**(3), 918–923 (2002).
    <https://doi.org/10.1116/1.1475984>
[^kaufman-1991]: F. B. Kaufman, D. B. Thompson, R. E. Broadie, M. A.
    Jaso et al., "Chemical-Mechanical Polishing for Fabricating
    Patterned W Metal Features as Chip Interconnects", *Journal of The
    Electrochemical Society* **138**(11), 3460–3465 (1991).
    <https://doi.org/10.1149/1.2085434>
[^stein-1999]: D. Stein, D. L. Hetherington and J. L. Cecchi,
    "Investigation of the Kinetics of Tungsten Chemical Mechanical
    Polishing in Potassium Iodate-Based Slurries: I. Role of Alumina and
    Potassium Iodate", *Journal of The Electrochemical Society*
    **146**(1), 376–381 (1999). <https://doi.org/10.1149/1.1391617>
[^pat-pad-rodel]: H. F. Reinhardt, J. V. H. Roberts, H. G. McClain, W. D.
    Budinger and E. W. Jensen (Rodel Inc.), *Polymeric polishing pad
    containing hollow polymeric microelements*, US 5,578,362 A, priority
    1992-08-19, granted 1996-11-26.
    <https://patents.google.com/patent/US5578362A/en>
[^castillo-mejia-2004]: D. Castillo-Mejia, J. Kelchner and S. Beaudoin,
    "Polishing Pad Surface Morphology and Chemical Mechanical
    Planarization", *Journal of The Electrochemical Society* **151**(4),
    G271 (2004). <https://doi.org/10.1149/1.1649751>
[^pat-cmp-window]: M. Birang, A. Gleason and W. L. Guthrie (Applied
    Materials), *Forming a transparent window in a polishing pad for a
    chemical mechanical polishing apparatus*, US 5,893,796 A, granted
    1999-04-13. <https://patents.google.com/patent/US5893796A/en>
[^zhang-raghavan-1999]: L. Zhang, S. Raghavan and M. Weling,
    "Minimization of chemical-mechanical planarization (CMP) defects and
    post-CMP cleaning", *Journal of Vacuum Science & Technology B*
    **17**(5), 2248–2255 (1999). <https://doi.org/10.1116/1.590901>
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
[^ge-2006]: D.-W. Ge, B.-C. Qiu, L.-R. Chen, F.-Y. He, J.-N. Liu, C.-X.
    Zhi and X. Cheng, "Optimizing post cleaning of Tungsten contact CMP to
    improve the yield of logic products with copper interconnect", *2006
    8th International Conference on Solid-State and Integrated Circuit
    Technology (ICSICT)*, pp. 351–353.
    <https://doi.org/10.1109/ICSICT.2006.306249>
[^qnity-story]: Qnity Electronics, *Our story*, company page (separation
    from DuPont), accessed 2026-09-13.
    <https://www.qnityelectronics.com/our-story.html>
[^qnity-cmp-pads]: Qnity Electronics, *CMP Pads*, product page, accessed
    2026-09-13. <https://www.qnityelectronics.com/cmp-pads.html>
[^entegris-cmc-2022]: Entegris, Inc., *CMC Materials | July 2022*,
    acquisition information page, accessed 2026-09-13.
    <https://www.entegris.com/en/home/brands/cmc-materials-july-2022.html>
[^amat-mesa-1999]: Applied Materials, *Applied Materials Announces New
    Mirra Mesa System to Address Market Demand for Integrated CMP
    Solutions*, press release, 1999-06-10, accessed 2026-09-13.
    <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-new-mirra-mesa-system-address-market>
[^entegris-post-cmp]: Entegris, Inc., *Semiconductor Cleaning Solutions*
    (post-CMP cleaning solutions), product page, accessed 2026-09-13.
    <https://www.entegris.com/en/home/products/chemistries/specialty-chemicals/post-cmp-cleaning-solutions/semiconductor-cleaning-solutions.html>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing"; read from a Wayback Machine copy on
    2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-entegris]: Wikipedia, *Entegris*.
    <https://en.wikipedia.org/wiki/Entegris>
[^skw-07]: SkyWater Technology, *A Day in the Life of a SkyWater
    Maintenance Technician*, 2023-12-14; caption re-checked 2026-09-13.
    <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
[^kwon-2013]: T.-Y. Kwon, M. Ramachandran and J.-G. Park, "Scratch
    formation and its mechanism in chemical mechanical planarization
    (CMP)", *Friction* **1**(4), 279–305 (2013).
    <https://doi.org/10.1007/s40544-013-0026-y>
[^ipec-472-1997]: IPEC-Planar, *AVANTI 472*, product page; Wayback
    Machine capture of 1997-06-26.
    <https://web.archive.org/web/19970626104141/http://www.ipec.com:80/planar/472.html>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^lai-2003]: C. L. Lai and S. H. Lin, "Electrocoagulation of chemical
    mechanical polishing (CMP) wastewater from semiconductor
    fabrication", *Chemical Engineering Journal* **95**(1–3), 205–211
    (2003). <https://doi.org/10.1016/S1385-8947(03)00106-2>
[^ollendorf-2004]: H. Ollendorf, S. Cabral and R. Fuller, "Reduction of
    CMP μ-scratch induced metal shorts by introduction of a post CMP
    tungsten plasma clean process in a high volume DRAM manufacturing
    environment", *2004 IEEE/SEMI Advanced Semiconductor Manufacturing
    Conference and Workshop*, pp. 1–4.
    <https://doi.org/10.1109/ASMC.2004.1309523>
[^wiki-colloidal-silica]: Wikipedia, *Colloidal silica*.
    <https://en.wikipedia.org/wiki/Colloidal_silica>
[^oliver-2004]: M. R. Oliver (ed.), *Chemical-Mechanical Planarization
    of Semiconductor Materials*, Springer Series in Materials Science
    69, Springer, 2004, ISBN 978-3-540-43181-9.
    <https://doi.org/10.1007/978-3-662-06234-0>
