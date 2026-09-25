(material-lithography-materials)=
# Lithography materials

Lithography materials are what a mask step consumes besides light and
time: the photoresist that records the pattern, the anti-reflective
coating and adhesion promoter under it, the developer that dissolves the
exposed resist, the solvents that clean the wafer edge and back, the
reticle that carries the pattern, and the lamps and laser gas of the
exposure tools. A mask step typically uses most of them (industry
practice), and the step pages read each of SKY130's 36 mask steps as
doing so.
This page describes the class in general, lists representative materials
and the grades and standards they are bought to, and then says what
SkyWater has published about lithography materials at its fab and which
SKY130 steps name them. The sequence of a mask step is on the
{ref}`lithography category page <category-lithography>`, the tools on
the {ref}`coat/develop track <machine-coat-develop-track>`,
{ref}`i-line stepper <machine-i-line-stepper>` and
{ref}`DUV stepper <machine-duv-krf-stepper>` pages, and the masks
themselves on the {ref}`masks page <masks-index>`.

| | Lithography materials |
|---|---|
| What they do | "Photoresists are Photo-imageable liquids"; positive-tone types are those "in which only the areas exposed to light are removed by a developing solution".[^jsr-em] |
| Resists | DNQ/novolac, "One very common positive photoresist used with the I, G and H-lines from a mercury-vapor lamp"; for DUV, resists "require the use of chemical amplification to increase the sensitivity to the exposure energy".[^wiki-resist] |
| Under the resist | A "BARC coating (Bottom Anti-Reflectant Coating)";[^wiki-litho] HMDS, "often used as an adhesion promoter for photoresists".[^wiki-hmds] |
| Developer | "usually 0.26N tetramethylammonium hydroxide (TMAH) in water";[^wiki-resist] 2.38 % ready to use;[^microchemicals-dev] SEMI guides a 25 % grade.[^semi-c46] |
| Solvents | PGMEA, "a commonly used solvent" in the semiconductor industry;[^wiki-pgmea] ethyl lactate blends for edge-bead removal.[^pat-ebr-clariant] |
| Reticles | Hard-surface mask substrates to SEMI P1;[^semi-p1] pellicles to SEMI P5;[^semi-p5] a pellicle is "a thin transparent film stretched over a frame that is glued over one side of the photomask".[^wiki-mask] |
| Light sources | KrF excimer lasers at 248 nm;[^wiki-excimer] mercury lamps using "three ultraviolet wavelengths (436, 405 and 365 nm)".[^ushio-uv-lamps] |
| SkyWater evidence | "ASML I-line stepper", "ASML DUV stepper" and scanners, three tracks, "Reticle storage/handler/defect inspection", "Mask GDS to reticle";[^skw-01] "semiconductor grade photoresist and developer for photolithography"[^sec-01][^sec-02] |
| SKY130 steps | 37 steps; see {ref}`SKY130 steps that use this class <material-lithography-materials-steps>` |

## What the class is and what it does

A mask step turns a pattern on a reticle into a pattern of resist on the
wafer. The resist is spun on over a primer or anti-reflective coating,
exposed through the reticle, and developed, leaving openings where the
next etch or implant acts; the resist is then stripped
({ref}`category-lithography`, {ref}`category-strip`). The materials set
what the step can resolve and how reproducibly: the resist's contrast
and sensitivity, the reflectivity under it, the developer's strength and
temperature, and the cleanliness of reticle and air.

### Positive i-line resists: DNQ/novolac

The workhorse resist of mercury-lamp lithography is a novolac resin with
a diazonaphthoquinone (DNQ) photoactive compound. "DNQ inhibits the
dissolution of the novolac resin, but upon exposure to light, the
dissolution rate increases even beyond that of pure novolac", and
"DNQ-novolac resists are developed by dissolution in a basic solution
(usually 0.26N tetramethylammonium hydroxide (TMAH) in
water)".[^wiki-resist][^wiki-dnq] Pacansky and Lyerla showed that the
photochemical decomposition "proceeds via a ketene intermediate to a
photoproduct, the nature of which depends on the reaction conditions",
giving "3-indenecarboxylic acid" under ambient
conditions.[^pacansky-1979] Dill et al. reduced exposure to "three
optical parameters, A, B, and C" and development to "a rate relationship
R(M)", the basis for the process models of the papers that accompanied
it;[^dill-1975] Kim, Oldham and
Neureuther extended the development model "over the full range of
exposure".[^kim-1984] Resist makers tune the resin: a Tokyo Ohka Kogyo
patent combines "two different cresol novolac resins differentiated in
respects of the weight-average molecular weight" with a naphthoquinone
diazide ester for "fine patterning in the manufacture of semiconductor
devices".[^pat-resist-tok] Dammel's tutorial text covers the
chemistry.[^dammel-1993]

### KrF chemically amplified resists

Production resists for DUV "require the use of chemical amplification
to increase the sensitivity to the exposure energy", which "is done in
order to combat the larger absorption at shorter wavelengths": "acids
released by the exposure radiation diffuse during the post-exposure
bake step", and "A single acid molecule can catalyze many such
'deprotection' reactions".[^wiki-resist] Ito and Willson showed resists
in which a photogenerated acid removes the t-butoxycarbonyl protecting
group from a polystyrene to leave poly(hydroxystyrene), and wrote that
"The extremely high sensitivity of these systems is achieved through
chemical amplification".[^ito-1984] The catalyst can be
poisoned: MacDonald et al. found such a resist "severely degraded by
vapor from organic bases" at "as little as 15 parts per billion (ppb)",
and relieved it with "localized air filtration".[^macdonald-1991]
Environmentally stable resists followed. The ESCAP resist of Ito et al.,
a copolymer of 4-hydroxystyrene with t-butyl acrylate, "is extremely
insensitive to the delay effect";[^ito-1994] Huang et al. described a resist "resilient
to airborne base contaminants" that showed "stable resist linewidth with
more than 24 hours delay between exposure and develop".[^huang-1994]
Ito's review covers the family.[^ito-2005]

### Anti-reflective coatings and adhesion promoter

"A BARC coating (Bottom Anti-Reflectant Coating) may be applied before
the photoresist is applied, to avoid reflections from occurring under
the photoresist".[^wiki-litho] Brunner showed why: interference in the
resist film makes the dose swing with thickness, and anti-reflective
coating processes "reduce S as the square root of substrate reflectivity
under the resist".[^brunner-1991] A Brewer Science patent describes the
organic form: "A light absorbing medium to be interposed under
photosensitive layers", with "a polymer vehicle which can penetrate into
small depressions of a substrate" and "a light absorbing
dye".[^pat-arc-brewer] Before coating, the wafer is primed: "The surface
layer of silicon dioxide on the wafer reacts with HMDS to form
tri-methylated silicon-dioxide, a highly water repellent
layer",[^wiki-litho] and "Best results are obtained by applying HMDS
from the gas phase on heated substrates".[^wiki-hmds]

### Developer

Positive resists are developed in aqueous base. "Developers originally
often contained sodium hydroxide (NaOH). However, sodium is considered an
extremely undesirable contaminant in MOSFET fabrication", so
"Metal-ion-free developers such as tetramethylammonium hydroxide (TMAH)
are now used", with the developer's temperature controlled "to within
0.2 °C".[^wiki-litho] A common ready-to-use strength is 2.38 %
TMAH.[^microchemicals-dev] Surfactants are added for puddle
development: Perera found that the developer's surface tension "has to
be lowered, by adding a surfactant, to avoid 'pullback' of the developer
during puddling".[^perera-1989] TMAH is also toxic: "The
tetramethylammonium ion affects nerves and muscles, causing difficulties
in breathing, muscular paralysis and possibly death".[^wiki-tmah]

### Solvents

Resists are cast from organic solvents, and the same solvents clean the
wafer: "In the semiconductor industry, PGMEA is a commonly used
solvent".[^wiki-pgmea] Spin
coating leaves a thick rim: "Edge bead removal (EBR) is carried out,
usually with a nozzle, to remove this extra resist as it could otherwise
cause particulate contamination".[^wiki-litho] A Clariant patent uses
"ethyl lactate and N-methyl pyrollidone" as a remover that "is effective
as both a backside and topside edge bead remover";[^pat-ebr-clariant] a
Samsung patent uses ethyl lactate blends as a thinner both for edge and
backside rinsing and for reworking wafers "having excess coated
photoresist due to an etching failure".[^pat-thinner-samsung]

### Reticles and pellicles

The reticle is a patterned absorber on a quartz plate, bought as a blank
to the SEMI hard-surface substrate specification[^semi-p1] and written
by a mask shop; a mask maker describes "embedded attenuated phase-shift
masks (EAPSM)" that "rely on a wavelength-tuned, 6% transmission MoSiON
absorber" at 248 and 193 nm.[^photronics-abr] It is kept clean by a
pellicle, placed so that "moderate-to-small sized particles that land on
the pellicle will be too far out of focus to print".[^wiki-mask] SEMI P5
"covers the general requirements for pellicles used on photomasks or
reticles in photolithographic exposure systems",[^semi-p5] and Hershel's
1981 paper examined the mask protection problem "with emphasis given to
the relevant optical requirements of pellicles".[^hershel-1981]

### Light-source consumables

The exposure tools consume their light sources. "An excimer laser
typically uses a combination of a noble gas (argon, krypton, or xenon)
and a reactive gas (fluorine or chlorine)", and lithography tools
"mostly use deep ultraviolet (DUV) light from the KrF and ArF excimer
lasers with wavelengths of 248 and 193 nanometers".[^wiki-excimer] Das
and Sandstrom wrote that "The only laser that has been successfully used
in semiconductor manufacturing as a source for lithography is the excimer
laser".[^das-2002] i-line tools use mercury arc lamps; Ushio's
lithography lamps are "developed to effectively utilize three
ultraviolet wavelengths (436, 405 and 365 nm)".[^ushio-uv-lamps]

## Representative materials and grades

Resists, coatings and developers are proprietary formulations sold by
product name; the families below are those the step pages describe.
SKY130's products, thicknesses and bake and develop conditions are not
public, apart from two photoresist thicknesses in the PDK's design
assumptions.[^pdk-03] The supplier product lines quoted below are
current company statements about their catalogues; none says what
SkyWater buys, although Tokyo Ohka Kogyo, JSR and Moses Lake Industries
are among the suppliers SkyWater's filings name.[^sec-01][^sec-02]

* **i-line positive resists.** DNQ/novolac, including thick grades for
  implant masks;[^wiki-resist] Tokyo Ohka Kogyo lists "g/i-Line
  photoresists" among its semiconductor products,[^tok-products] and JSR
  a lineup "compatible with various exposure sources, including EUV
  (MOR), EUV (CAR), ArF, KrF, i-line, and g-line".[^jsr-em]
* **KrF positive resists.** Chemically amplified hydroxystyrene
  resists;[^ito-2005] TOK lists "KrF excimer laser
  photoresists".[^tok-products]
* **Anti-reflective coatings.** Organic dyed polymers of the kind
  Brewer Science patented;[^pat-arc-brewer] JSR sells "underlayers and
  topcoats" as "multilayer materials".[^jsr-em]
* **Adhesion promoter.** HMDS, bis(trimethylsilyl)amine, applied as
  vapour;[^wiki-hmds] TOK lists "Adhesion Enhancing
  Materials".[^tok-products]
* **Developer.** TMAH in water, commonly 2.38 % (0.26 N), with or
  without surfactant;[^microchemicals-dev][^wiki-resist] SEMI C46 is a
  "guide for a grade of 25% tetramethylammonium hydroxide", the
  concentrate,[^semi-c46] and Moses Lake Industries sells TMAH "at
  concentrations of choice (in water) up to 25%, and with or without
  surfactants", with "metallic impurity levels of <1000
  ppt".[^mli-tmah]
* **Edge-bead and rinse solvents.** PGMEA and ethyl lactate
  blends;[^wiki-pgmea][^pat-ebr-clariant][^pat-thinner-samsung] TOK
  lists "Thinners".[^tok-products]
* **Reticles and pellicles.** Chrome or attenuated phase-shift absorbers
  on quartz blanks to SEMI P1, protected by pellicles to SEMI
  P5.[^semi-p1][^semi-p5][^photronics-abr]
* **Exposure-tool consumables.** KrF laser gas, a noble gas with a
  reactive halogen[^wiki-excimer] (krypton with a fluorine–neon premix,
  as the step pages list it), and mercury arc
  lamps.[^ushio-uv-lamps]

## At SkyWater

### What SkyWater's filings and pages list

Under "Lithography", SkyWater's *Facilities & Capabilities* page lists
exposure tools, tracks and reticle handling:[^skw-01]

> "ASML I-line stepper" · "ASML I-line scanner" · "ASML DUV stepper" ·
> "ASML DUV scanner" · "ASML 193nm single stage scanner – 90nm CD" ·
> "ASML 193nm twin stage scanner – sub 65nm CD" · "DNS 80B track" ·
> "Sokudo RF3 track" · "TEL ProZ Lithius track"

and, under "Photo Metrology", "Reticle storage/handler/defect
inspection"; under "Other Services" it lists "Mask GDS to reticle" and
"OPC modeling".[^skw-01] It names no resist, coating, developer or
reticle supplier. Both of SkyWater's filings describe the raw materials
as including "semiconductor grade photoresist and developer for
photolithography" and name suppliers:[^sec-01][^sec-02]

| Filing | Photoresist | Developer |
|--------|-------------|-----------|
| S-1 (2021)[^sec-01] | "The Dow Chemical Company (photoresist)"; "JSR Corporation (photoresist)"; "Tokyo Ohka Kogyo America, Inc. (photoresist)" | "Air Products & Chemicals, Inc., Moses Lake (developer)" |
| 10-K for fiscal 2023[^sec-02] | "Rohm and Haas EM LLC (a subsidiary of DuPont) (photoresist)"; "JSR Micro Inc. (photoresist)"; "FUJIFILM Electronic Materials USA, Inc. (photoresist)"; "Tokyo Ohka Kogyo America, Inc. (photoresist)" | "Moses Lake Industries Inc. (developer)" |

Neither filing names a product or says which resist serves which tool.
Moses Lake Industries describes itself as "Founded in 1984 as a wholly
owned subsidiary of Tama Chemicals" and sells TMAH solutions;[^mli-about][^mli-tmah]
the filings do not say what developer SkyWater buys, and the S-1's
wording, which attaches "Moses Lake" to Air Products, is not explained.
The PDK's design assumptions give a "Photoresist thickness" of 1.14 and
a "Photoresist thickness for HV Tip Implants" of 0.3 (µm),[^pdk-03]
and the process-steps sheet records a mask type for three plates only,
which the {ref}`masks page <masks-index>` reads as embedded attenuated
phase-shift masks for vias 2 and 3 and a binary mask for via
4.[^steps-sheet]

### Strength of the evidence

The exposure tools, tracks and reticle services are SkyWater statements
and rank as **strong** on the scale of the
{ref}`machines index <machines-reading-evidence>`.[^skw-01] The resist
and developer suppliers are strong as statements but tie no product,
chemistry or wavelength to a supplier, and they changed between the
2021 and 2023 filings.[^sec-01][^sec-02] That TMAH is the developer, and
that the resists are DNQ/novolac and chemically amplified families, is
industry practice for the exposure tools SkyWater lists, not a SkyWater
statement; anti-reflective coatings, HMDS, edge-bead solvents and
pellicles appear in no SkyWater source cited here. The PDK thicknesses
are design assumptions, not process specifications.[^pdk-03]

(material-lithography-materials-steps)=
### SKY130 steps that use this class

This page covers the rows of the {ref}`materials index <materials-table>`
listed below by key; the steps are those whose *Resources required* section
names one of them (the union of the rows' *Steps* cells).

Materials index rows covered:

* `i-line-resist` — i-line positive photoresist
* `krf-resist` — KrF chemically amplified positive photoresist
* `arc` — anti-reflective coatings
* `hmds` — HMDS adhesion promoter
* `tmah` — TMAH developer
* `ebr-solvents` — edge-bead remover and rinse solvents
* `reticles` — reticles and pellicles
* `exposure-consumables` — exposure-tool consumables

<!-- step-tables:begin (generated by tools/gen_step_tables.py; do not edit) -->
:::{dropdown} All 37 steps as one line of links (checked against the index)

Steps:

{ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`TUNARCE <step-036>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`P1M <step-061>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>`
:::
<!-- step-tables:end -->

All 36 mask steps name developer, edge-bead solvent and a reticle. The
step list calls the remaining step, {ref}`TUNARCE <step-036>`, a
"Tunnel mask ARC etch" and does not explain it;[^steps-sheet] its step
page reads it as the etch that opens an anti-reflective coating under
the {ref}`TUNM <step-035>` resist. Which
mask steps name i-line or KrF resist, a BARC, HMDS, or laser gas or
lamps follows each step page's reading, as recorded in the index rows.

## Supply, handling, safety and facilities

None of the SkyWater sources cited here describes how the fab stores,
delivers or disposes of lithography materials; the points below are
industry practice or supplier statements.

* **Airborne contamination.** Chemically amplified resists need
  amine-free air, which tracks provide by chemical
  filtration;[^macdonald-1991] PGMEA "is often the most abundant
  airborne, molecular contamination (AMC) in semiconductor cleanrooms,
  due to its evaporation into ambient air".[^wiki-pgmea]
* **Developer supply.** Moses Lake Industries ships TMAH in "1000-liter
  IBC containers, 200-liter drums, and 1-gallon bottles";[^mli-tmah]
  metal-ion-free developer protects gate oxides from
  sodium.[^wiki-litho]
* **Hazards.** TMAH is toxic by its effect on nerves and
  muscles;[^wiki-tmah] the Clariant remover was formulated to have "a
  flash point of greater than 100° F. (38° C.)".[^pat-ebr-clariant]
* **Developer waste.** Wang et al. note that "A large amount of
  developer wastewater containing tetramethylammonium hydroxide (TMAH) is
  discharged from semiconductors and photoelectric industries" and
  recovered TMAH from it by electrodialysis.[^wang-2013-tmah]
* **Reticles.** Reticles are stored, handled and inspected in dedicated
  systems, which SkyWater lists;[^skw-01] pellicles keep particles out of
  focus.[^wiki-mask]
* **Light sources.** Laser gas refills and chamber replacements for the
  KrF lasers, and lamp changes for the i-line tools, are scheduled
  consumables of the exposure tools ({ref}`machine-duv-krf-stepper`,
  {ref}`machine-i-line-stepper`).

## Process-integration notes for SKY130

These notes connect the class to the step pages; they add no SKY130
conditions of their own.

* **Two resist families.** The step pages read the critical levels
  (active, poly, nitride cut, local-interconnect contact and line,
  contact, metals 1–4 and vias 1–4) as KrF levels with chemically
  amplified resist, and the implant blocks, relaxed etch masks and thick
  top levels as i-line levels with DNQ/novolac resist, as the index rows
  record; the {ref}`MM3 <step-139>` and {ref}`MM4 <step-154>` pages
  allow either. The
  chemically amplified levels carry the airborne-amine and delay
  constraints the i-line levels do not.[^macdonald-1991][^huang-1994]
* **Resist thickness.** The PDK assumes 1.14 µm of photoresist in
  general and 0.3 µm for the HV tip implants;[^pdk-03] the
  {ref}`HVNTM <step-068>` page reads the thin film as a thin-viscosity
  i-line resist, and the {ref}`DNM <step-007>` and
  {ref}`MM5 <step-162>` pages read thick grades for the deep-well and
  top-metal masks (inference).
* **Resist as an implant mask.** Resist exposed to high-dose implants
  forms a crust that the strip steps must remove
  ({ref}`category-strip`); Norton et al. compared i-line and DUV resists
  under high-current implantation.[^norton-2000]
* **HMDS on metal.** {ref}`MM1 <step-113>` and {ref}`CAPM <step-137>`
  leave out HMDS, on those pages' reasoning that it is not needed on
  metal, and
  {ref}`MM3 <step-139>` and {ref}`MM4 <step-154>` list an organic BARC
  without HMDS; the {ref}`materials index <materials-open-questions>`
  records that the reason does not clearly apply at the capacitor
  levels.
* **An anti-reflective coating that is etched.** The step list does not
  explain {ref}`TUNARCE <step-036>` beyond its name;[^steps-sheet] its
  step page reads it as opening an ARC under the tunnel-window resist
  before the implants and wet etch that resist serves.
* **Reticle types.** The masks page reads the three plates whose type
  the step list records as attenuated phase-shift masks for vias 2 and 3
  and a binary mask for via 4;[^steps-sheet] the other reticles' types
  are not public ({ref}`masks-index`).

## Related pages

* {ref}`category-lithography` — the sequence of a mask step, resists,
  anti-reflective coatings and developer.
* {ref}`machine-coat-develop-track` — the tool that primes, coats,
  bakes and develops.
* {ref}`machine-i-line-stepper` and {ref}`machine-duv-krf-stepper` — the
  exposure tools and their light sources.
* {ref}`masks-index` — the 36 mask steps and their reticles.
* {ref}`category-strip` — removing the resist after etch or implant.
* {ref}`materials-index` — all consumable classes.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

* {ref}`Anti-reflective coating <patent-gp27029211>` — US 4,910,122 A (1982)
* {ref}`Positive-working naphthoquinone diazide photoresist composition with two cresol novolac resins <patent-gp15976485>` — US 4,731,319 A (1985)
* {ref}`Use of mixtures of ethyl lactate and N-methyl pyrollidone as an edge bead remover for photoresists <patent-gp26689885>` — US 5,814,433 A (1996)
* {ref}`Rework method utilizing thinner for wafers in manufacturing of semiconductor devices <patent-gp26633062>` — US 6,159,646 A (1997)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater Technology, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the lithography,
  photo-metrology and mask-service entries.[^skw-01]
* SkyWater Technology, Form S-1 (2021) and Form 10-K for fiscal 2023 —
  the photoresist and developer suppliers.[^sec-01][^sec-02]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — the two photoresist
  thicknesses.[^pdk-03]
* [The *S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — mask types for three
  plates.[^steps-sheet]
* [Tokyo Ohka Kogyo, *Semiconductor Manufacturing Field*](<https://www.tok.co.jp/eng/products/semiconductor-pre>) — the company's
  resist, developer, thinner and adhesion product lines.[^tok-products]
* [JSR, *About our Electronic Materials Business*](<https://www.jsr.co.jp/jsr_e/products/em/biz/>) — photoresists and
  multilayer materials.[^jsr-em]
* Moses Lake Industries, [*TMAH Aqueous Solutions*](<https://mlindustries.com/products/tmah-aqueous-solutions/>) and [*About MLI*](<https://mlindustries.com/about-mli/>) — TMAH
  concentrations, purity and packaging, and the company's
  ownership.[^mli-tmah][^mli-about]
* [Photronics, *Advanced Binary Reticle*](<https://www.photronics.com/products/advanced-binary-reticle/>) — binary and embedded attenuated
  phase-shift reticles.[^photronics-abr]
* [Ushio, *Super high-pressure UV lamps*](<https://www.ushio.co.jp/en/products/1010.html>) — lithography mercury
  lamps.[^ushio-uv-lamps]

### High-level understanding

* Wikipedia, [*Photoresist*](<https://en.wikipedia.org/wiki/Photoresist>) and [*Diazonaphthoquinone*](<https://en.wikipedia.org/wiki/Diazonaphthoquinone>) — resist types,
  DNQ/novolac and chemical amplification.[^wiki-resist][^wiki-dnq]
* [Wikipedia, *Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) — priming, BARC, edge-bead removal,
  developer and hard bake.[^wiki-litho]
* [Wikipedia, *Anti-reflective coating*](<https://en.wikipedia.org/wiki/Anti-reflective_coating>) — ARCs in
  lithography.[^wiki-arc]
* Wikipedia, [*Bis(trimethylsilyl)amine*](<https://en.wikipedia.org/wiki/Bis(trimethylsilyl)amine>), [*Propylene glycol methyl ether
  acetate*](<https://en.wikipedia.org/wiki/Propylene_glycol_methyl_ether_acetate>) and [*Tetramethylammonium hydroxide*](<https://en.wikipedia.org/wiki/Tetramethylammonium_hydroxide>) — the primer, a casting
  and rinse solvent, and the developer.[^wiki-hmds][^wiki-pgmea][^wiki-tmah]
* Wikipedia, [*Photomask*](<https://en.wikipedia.org/wiki/Photomask>) and [*Excimer laser*](<https://en.wikipedia.org/wiki/Excimer_laser>) — reticles, pellicles and
  KrF lasers.[^wiki-mask][^wiki-excimer]
* [MicroChemicals, *Development of photoresists*](<https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>) — developer types and
  strength.[^microchemicals-dev]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — resist
  chemistry and processing.[^mack-2007]

### Deep dive

* [Dill et al., *IEEE TED* 1975](<https://doi.org/10.1109/T-ED.1975.18159>) — the A, B, C exposure parameters and
  development rate of positive resist.[^dill-1975]
* [Pacansky and Lyerla, *IBM J. Res. Dev.* 1979](<https://doi.org/10.1147/rd.231.0042>) — the photochemistry of
  DNQ in novolac.[^pacansky-1979]
* [Kim, Oldham and Neureuther, *IEEE TED* 1984](<https://doi.org/10.1109/T-ED.1984.21779>) — a development model for
  positive resist.[^kim-1984]
* [Dammel, *Diazonaphthoquinone-based Resists*](<https://doi.org/10.1117/3.2265072>) — i-line resist
  chemistry.[^dammel-1993]
* [Reichmanis and Thompson, *Chem. Rev.* 1989](<https://doi.org/10.1021/cr00096a001>) — polymer materials for
  microlithography.[^reichmanis-1989]
* [Ito and Willson, *ACS Symp. Ser.* 1984](<https://doi.org/10.1021/bk-1984-0242.ch002>) — chemically amplified
  resists.[^ito-1984]
* [MacDonald et al., *Proc. SPIE* 1991](<https://doi.org/10.1117/12.46354>) — airborne amines and chemically
  amplified resist.[^macdonald-1991]
* [Ito et al., *J. Photopolym. Sci. Technol.* 1994](<https://doi.org/10.2494/photopolymer.7.433>) — the environmentally
  stable ESCAP resist.[^ito-1994]
* [Huang et al., *Proc. SPIE* 1994](<https://doi.org/10.1117/12.175370>) — a base-resilient positive DUV
  resist.[^huang-1994]
* [Ito, *Adv. Polym. Sci.* 2005](<https://doi.org/10.1007/b97574>) — a review of chemically amplified
  resists.[^ito-2005]
* [Brunner, *Proc. SPIE* 1991](<https://doi.org/10.1117/12.46410>) — swing curves and anti-reflective
  coatings.[^brunner-1991]
* [Perera, *Proc. SPIE* 1989](<https://doi.org/10.1117/12.953060>) — developer surfactants for puddle
  development.[^perera-1989]
* [Hershel, *Proc. SPIE* 1981](<https://doi.org/10.1117/12.931869>) — the optical requirements of
  pellicles.[^hershel-1981]
* [Das and Sandstrom, *Proc. IEEE* 2002](<https://doi.org/10.1109/JPROC.2002.803665>) — excimer lasers for
  lithography.[^das-2002]
* [Norton et al., IIT 2000](<https://doi.org/10.1109/IIT.2000.924278>) — i-line and DUV resists under high-current
  implantation.[^norton-2000]
* [Wang et al., *Ind. Eng. Chem. Res.* 2013](<https://doi.org/10.1021/ie4023995>) — recovering TMAH from
  developer wastewater.[^wang-2013-tmah]
* [Arnold, Brewer and Punyakumleard (Brewer Science), US 4,910,122](<https://patents.google.com/patent/US4910122A/en>) — a
  dyed anti-reflective coating under resist.[^pat-arc-brewer]
* [Kohara et al. (Tokyo Ohka Kogyo), US 4,731,319](<https://patents.google.com/patent/US4731319A/en>) — a two-novolac DNQ
  resist.[^pat-resist-tok]
* [Nelson and Lehar (Clariant), US 5,814,433](<https://patents.google.com/patent/US5814433A/en>) — an ethyl lactate edge-bead
  remover.[^pat-ebr-clariant]
* [Jeon, Lee and Lee (Samsung), US 6,159,646](<https://patents.google.com/patent/US6159646A/en>) — thinner compositions for
  edge rinse and rework.[^pat-thinner-samsung]
* SEMI P1, SEMI P5 and SEMI C46 — photomask substrates, pellicles and
  25 % TMAH.[^semi-p1][^semi-p5][^semi-c46]

## Open questions

* Which resist, coating, developer and solvent products SKY130 levels
  use, and at what thicknesses and conditions beyond the two PDK
  assumptions, are not public.[^pdk-03]
* Which supplier provides the resists for which exposure tool, and why
  the S-1 attaches "Moses Lake" to Air Products, are not
  stated.[^sec-01][^sec-02]
* Whether SKY130 levels use HMDS, BARC or a top anti-reflective coating
  is not stated by any SkyWater source; the step pages read these from
  industry practice.
* Who writes SkyWater's reticles, and the absorber type of the reticles
  other than the three plates the step list records, are not
  public.[^skw-01][^steps-sheet]

<!-- footnotes -->

[^jsr-em]: JSR Corporation, *About our Electronic Materials Business*,
    business introduction page, accessed 2026-09-13.
    <https://www.jsr.co.jp/jsr_e/products/em/biz/>
[^wiki-resist]: Wikipedia, *Photoresist*.
    <https://en.wikipedia.org/wiki/Photoresist>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^wiki-hmds]: Wikipedia, *Bis(trimethylsilyl)amine* (hexamethyldisilazane).
    <https://en.wikipedia.org/wiki/Bis(trimethylsilyl)amine>
[^microchemicals-dev]: MicroChemicals, *Development of photoresists*,
    application note, accessed 2026-09-13.
    <https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>
[^semi-c46]: SEMI, *SEMI C46 — Guide for 25% Tetramethylammonium
    Hydroxide*, SEMI Standards store listing (revision C46-0812,
    inactive), accessed 2026-09-13.
    <https://store-us.semi.org/products/c04600-semi-c46-guide-for-25-tetramethylammonium-hydroxide>
[^wiki-pgmea]: Wikipedia, *Propylene glycol methyl ether acetate*.
    <https://en.wikipedia.org/wiki/Propylene_glycol_methyl_ether_acetate>
[^pat-ebr-clariant]: W. C. Nelson and O. Lehar (Clariant Finance (BVI)),
    *Use of mixtures of ethyl lactate and N-methyl pyrollidone as an edge
    bead remover for photoresists*, US 5,814,433 A, priority 1996-05-17,
    granted 1998-09-29. <https://patents.google.com/patent/US5814433A/en>
[^semi-p1]: SEMI, *SEMI P1 — Specification for Hard Surface Photomask
    Substrates*, SEMI Standards store listing (revision P1-0708E,
    inactive), accessed 2026-09-13.
    <https://store-us.semi.org/products/p00100-semi-p1-specification-for-hard-surface-photomask-substrates>
[^semi-p5]: SEMI, *SEMI P5 — Specification for Pellicles*, SEMI
    Standards store listing (revision P5-0416, reapproved 1221), accessed
    2026-09-13.
    <https://store-us.semi.org/products/p00500-semi-p5-specification-for-pellicles>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-excimer]: Wikipedia, *Excimer laser*.
    <https://en.wikipedia.org/wiki/Excimer_laser>
[^ushio-uv-lamps]: Ushio Inc., *Super high-pressure UV lamps (500W~35kW)*,
    product page, accessed 2026-09-13.
    <https://www.ushio.co.jp/en/products/1010.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography, photo-metrology and other-services entries
    re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing"; read from a Wayback Machine copy on
    2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; "Raw materials" paragraph; read from a Wayback Machine
    copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^wiki-dnq]: Wikipedia, *Diazonaphthoquinone*.
    <https://en.wikipedia.org/wiki/Diazonaphthoquinone>
[^pacansky-1979]: J. Pacansky and J. R. Lyerla, "Photochemical
    Decomposition Mechanisms for AZ-Type Photoresists", *IBM Journal of
    Research and Development* **23**(1), 42–55 (1979).
    <https://doi.org/10.1147/rd.231.0042>
[^dill-1975]: F. H. Dill, W. P. Hornberger, P. S. Hauge and J. M. Shaw,
    "Characterization of positive photoresist", *IEEE Transactions on
    Electron Devices* **22**(7), 445–452 (1975).
    <https://doi.org/10.1109/T-ED.1975.18159>
[^kim-1984]: D. J. Kim, W. G. Oldham and A. R. Neureuther, "Development
    of positive photoresist", *IEEE Transactions on Electron Devices*
    **31**(12), 1730–1736 (1984). <https://doi.org/10.1109/T-ED.1984.21779>
[^pat-resist-tok]: H. Kohara, H. Tanaka, M. Miyabe, Y. Arai, S. Asaumi
    and T. Nakayama (Tokyo Ohka Kogyo), *Positive-working naphthoquinone
    diazide photoresist composition with two cresol novolac resins*,
    US 4,731,319 A, priority 1985-08-09, granted 1988-03-15.
    <https://patents.google.com/patent/US4731319A/en>
[^dammel-1993]: R. R. Dammel, *Diazonaphthoquinone-based Resists*, SPIE
    Tutorial Texts TT11, SPIE Press, 1993.
    <https://doi.org/10.1117/3.2265072>
[^ito-1984]: H. Ito and C. G. Willson, "Applications of Photoinitiators to
    the Design of Resists for Semiconductor Manufacturing", *ACS Symposium
    Series* **242**, 11–23 (1984).
    <https://doi.org/10.1021/bk-1984-0242.ch002>
[^macdonald-1991]: S. A. MacDonald, N. J. Clecak, H. R. Wendt, C. G.
    Willson, C. D. Snyder, C. J. Knors, N. B. Deyoe, J. G. Maltabes, J. R.
    Morrow, A. E. McGuire and S. J. Holmes, "Airborne chemical contamination
    of a chemically amplified resist", *Proc. SPIE* **1466**, 2–12 (1991).
    <https://doi.org/10.1117/12.46354>
[^ito-1994]: H. Ito, G. Breyta, D. Hofer, R. Sooriyakumaran, K. Petrillo
    and D. Seeger, "Environmentally stable chemical amplification positive
    resist: principle, chemistry, contamination resistance, and
    lithographic feasibility", *Journal of Photopolymer Science and
    Technology* **7**(3), 433–447 (1994).
    <https://doi.org/10.2494/photopolymer.7.433>
[^huang-1994]: W.-S. Huang, R. W. Kwong, A. D. Katnani and M. Khojasteh,
    "Evaluation of a new environmentally stable positive tone chemically
    amplified deep-UV resist", *Proc. SPIE* **2195**, 37 (1994).
    <https://doi.org/10.1117/12.175370>
[^ito-2005]: H. Ito, "Chemical Amplification Resists for
    Microlithography", *Advances in Polymer Science* **172**, 37–245
    (2005). <https://doi.org/10.1007/b97574>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^pat-arc-brewer]: J. W. Arnold, T. L. Brewer and S. Punyakumleard
    (Brewer Science), *Anti-reflective coating*, US 4,910,122 A, priority
    1982-09-30, granted 1990-03-20.
    <https://patents.google.com/patent/US4910122A/en>
[^perera-1989]: T. Perera, "Characteristics of a developer for spray
    puddle develop processes", *Proc. SPIE* **1086**, 470 (1989).
    <https://doi.org/10.1117/12.953060>
[^wiki-tmah]: Wikipedia, *Tetramethylammonium hydroxide*.
    <https://en.wikipedia.org/wiki/Tetramethylammonium_hydroxide>
[^pat-thinner-samsung]: M.-S. Jeon, C.-D. Lee and B.-Y. Lee (Samsung
    Electronics), *Rework method utilizing thinner for wafers in
    manufacturing of semiconductor devices*, US 6,159,646 A, priority
    1997-09-04, granted 2000-12-12.
    <https://patents.google.com/patent/US6159646A/en>
[^photronics-abr]: Photronics, Inc., *Advanced Binary Reticle*, product
    page, retrieved 2026-09-13.
    <https://www.photronics.com/products/advanced-binary-reticle/>
[^hershel-1981]: R. Hershel, "Pellicle Protection Of Integrated Circuit
    (IC) Masks", *Proc. SPIE* **0275**, Semiconductor Microlithography VI,
    23–28 (1981). <https://doi.org/10.1117/12.931869>
[^das-2002]: P. Das and R. L. Sandstrom, "Advances in excimer laser
    technology for sub-0.25-μm lithography", *Proceedings of the IEEE*
    **90**(10), 1637–1652 (2002). <https://doi.org/10.1109/JPROC.2002.803665>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^tok-products]: Tokyo Ohka Kogyo Co., Ltd., *Semiconductor Manufacturing
    Field*, products page, accessed 2026-09-13.
    <https://www.tok.co.jp/eng/products/semiconductor-pre>
[^mli-tmah]: Moses Lake Industries, *TMAH Aqueous Solutions*, product
    page, accessed 2026-09-13.
    <https://mlindustries.com/products/tmah-aqueous-solutions/>
[^mli-about]: Moses Lake Industries, *About MLI*, company page, accessed
    2026-09-13. <https://mlindustries.com/about-mli/>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    retrieved 2026-09-14; tab "Sheet1" lists the 171 steps (number, code and
    description) and tab "Sheet4" gives mask types for three masks.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^wang-2013-tmah]: Y. Wang, Z. Zhang, C. Jiang and T. Xu, "Electrodialysis
    Process for the Recycling and Concentrating of Tetramethylammonium
    Hydroxide (TMAH) from Photoresist Developer Wastewater", *Industrial &
    Engineering Chemistry Research* **52**(51), 18356–18361 (2013).
    <https://doi.org/10.1021/ie4023995>
[^norton-2000]: C. Norton, D. Marshall, M. Ameen, D. Whiteside, J. Hallock
    and A. Becknell, "Photoresist properties during high current
    implantation: an I-line vs. DUV resist comparison", *Proc. 2000
    International Conference on Ion Implantation Technology*, pp. 813–816.
    <https://doi.org/10.1109/IIT.2000.924278>
[^wiki-arc]: Wikipedia, *Anti-reflective coating*.
    <https://en.wikipedia.org/wiki/Anti-reflective_coating>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^reichmanis-1989]: E. Reichmanis and L. F. Thompson, "Polymer
    materials for microlithography", *Chemical Reviews* **89**(6),
    1273–1289 (1989). <https://doi.org/10.1021/cr00096a001>
