(material-sputter-targets)=
# Sputter targets

A sputter target is the block of metal that a physical vapour deposition
({term}`PVD`) chamber erodes to coat the wafer: argon ions from a plasma
strike it, and the atoms they knock out condense as a film. Each chamber
holds one target, usually bonded to a cooled backing plate, and erodes
it wafer by wafer until it is replaced. On the step pages' readings,
SKY130's metal back end is sputtered from three targets: titanium, which
with nitrogen in the chamber also gives titanium nitride;
aluminium–copper for the wiring; and titanium–tungsten for the stack caps
and the capacitor plates. SkyWater lists films of all three
metals;[^skw-01] which cap SKY130 lots use is not public (see the
process-integration notes below). This page describes the class in general, lists
representative targets and the purities and structures they are made to,
and then says what SkyWater has published about targets and sputtered
films at its fab and which SKY130 steps name them. The sputtering tool is
on the {ref}`PVD cluster tool page <machine-pvd-cluster-tool>` and the
film physics on the {ref}`deposition category page <category-deposition>`.

| | Sputter targets |
|---|---|
| What they do | Supply the atoms of a sputtered film: "A sputtering target is the object of the ion bombardment when sputtering takes place."[^jx-sputtering] |
| Materials in the SKY130 steps | Titanium (also sputtered {term}`reactively <reactive sputtering>` to TiN), aluminium–copper, titanium–tungsten (step-page readings); a report by Cypress, which ran the fab before SkyWater,[^sec-01] gives "Metal 1: 100A Ti / 3200A Al -0.5%Cu / 300A TiW".[^cyp-qtp-113005] |
| Purity | Titanium "4N5 (Ti 99.995% or above) 5N 5N5";[^jx-semi-targets] Al–Cu and Al–Si–Cu "99.99% (4N)-99.9995% (5N5)".[^solstice-targets] |
| Microstructure | Grain size and "crystallographic orientation and surface relief affect the I–V characteristics" of aluminium targets.[^leybovich-1993] |
| Construction | Monolithic or bonded to a backing plate; "The bond between sputtering target and its supporting backing plate is a critical reliability element in a sputter deposition system".[^astm-f1512] |
| Wear and defects | A "'racetrack' erosion profile may appear on the surface of the target";[^wiki-sputter] "Arcing during sputtering is a significant cause of defect generation".[^wickersham-2001] |
| SkyWater evidence | "AMAT PVD Metal": "Aluminum both pure and Cu doped", "TiW", "ESC TiN", "Imp TiN", "Collimated Ti";[^skw-01] "high-purity metals for film deposition processes"; Honeywell and JX Metals as target suppliers[^sec-01][^sec-02] |
| SKY130 steps | 13 steps; see {ref}`SKY130 steps that use this class <material-sputter-targets-steps>` |

## What the class is and what it does

In a sputtering chamber "a sputtering target is bombarded with argon
ions. This causes atoms or molecules to be emitted from the sputtering
target", and "The atoms or molecules are deposited and form a thin film
on the substrate".[^jx-sputtering] In a magnetron the plasma is held
close to the target, so erosion is uneven: "As the target material is
depleted, a 'racetrack' erosion profile may appear on the surface of the
target".[^wiki-sputter] The target sets what the film contains and much
of what goes wrong with it: impurities and inclusions become particles
and defects, the grain structure changes the discharge and the film's
uniformity over the target's life, and the bond to the backing plate
decides whether the target stays cool and attached. What makes a target
more than a block of pure metal is this engineering of purity, grain
structure, shape and bond. Thornton's structure-zone study relates the
deposition conditions a chamber sets to the film that
grows.[^thornton-1974]

### Titanium and reactive titanium nitride

A titanium supplier describes its targets as "widely used in places where
titanium is necessary in semiconductors, such as barrier layers for Al
interconnects, and hard masks".[^jx-semi-targets] Titanium nitride is
made from the same target by adding nitrogen: "Reactive gases can also be
used to sputter compounds. The compound can be formed on the target
surface, in-flight or on the substrate depending on the process
parameters", and "the wide majority of reactive-based sputtering
processes are characterized by an hysteresis-like
behavior".[^wiki-sputter] Berg and Nyberg model such
processes.[^berg-2005] In an ionised chamber the nitrogen reaching the
bottom of a hole matters as well; Mao and Hopwood's model predicts
"nitrogen deficient films at the bottom of trenches under metal-mode
deposition conditions".[^mao-2004] Titanium for contacts is also
sputtered through a collimator, which captures the off-normal flux; in
Rossnagel et al.'s lift-off system, "Atoms whose trajectory is more than
5° from normal are deposited on the inner surfaces of the
collimators".[^rossnagel-1991] Ionised-metal-plasma
chambers add a coil of the target metal inside the chamber; one supplier
states that in Applied Materials' 200 mm and 300 mm equipment "coils and
parts sets of the same material as the target are used inside the
chamber",[^jx-semi-targets] and an Applied Materials patent pastes the
coil with target material so that metal sputtered from it "will not
contaminate the film".[^pat-imp-coil-amat]

### Aluminium–copper

Aluminium wiring is sputtered from aluminium alloyed with a little
copper. Ames, d'Heurle and Horstmann found "that the lifetime of aluminum
films subjected to high current densities at elevated temperatures can
be increased by the addition of copper".[^ames-1970] The copper forms
precipitates, and target makers control them: one supplier lists Al–Cu
targets with no precipitates in a monolithic, fine-grained design, and
precipitates below 5 microns in a standard diffusion-bonded
design.[^solstice-targets] The target's grain structure affects the
discharge: Leybovich and Kuniya compared aluminium single crystals, some
machined to mimic grain relief, with "three polycrystalline Al-1 wt % Cu
targets with grain sizes of 0.25, 0.95, and 5.5 mm". The single crystals
showed "that both crystallographic orientation and surface relief affect
the I–V characteristics", and among the polycrystalline targets the
lowest target voltage came with the least (111) orientation and the
0.95 mm grain size.[^leybovich-1993] A Praxair patent describes aluminium
alloy targets with "a grain orientation ratio of at least 35 percent
(200) orientation" and "a grain size of less than 5 μm" that stay
"stable during sputtering".[^pat-target-texture-praxair] Inclusions
cause arcs: Wickersham et al. found that "The critical size for an Al2O3
inclusion in an aluminum-sputtering target in an argon plasma is 440±160
μm", above which inclusions "readily induce arcing and macroparticle
ejection".[^wickersham-2001]

### Titanium–tungsten

Titanium–tungsten films of the period were "typically composed of 10 wt%
of titanium and the balance of tungsten" and "often used as a barrier
metal layer", sputtered from pressed powder targets.[^pat-tiw-hitachi]
Nicolet's review surveys diffusion barriers in thin films.[^nicolet-1978]
Because the two metals sputter at different rates, a TiW target can shed
particles: the Hitachi Metals patent explains that "titanium having a
light atomic weight is selectively sputtered, and tungsten grains, which
are close to or contained inside the large titanium grains are scattered
from the target material in the form of large diameter particles", and
describes a structure with a Ti–W alloy phase to prevent
it.[^pat-tiw-hitachi] Waterman, Dunlop and Brat compared TiW targets made
three ways and found "that the target manufacturing technique and the
material purity have a significant impact on the defect density of the
deposited films".[^waterman-1990]

### Bonding, backing plates and end of life

Most targets are joined to a backing plate that carries cooling water
and mounts the target in the chamber. ASTM's practice for inspecting the
joint explains that "A bond must have high thermal conductivity to
provide adequate target cooling during sputtering", must withstand "the
shear stresses caused by differential thermal expansion between target
and backing plate", and that "An inadequate bond may fail in service,
potentially causing catastrophic separation of the target from the
backing plate".[^astm-f1512] Target makers patent their bonds: a
Materials Research Corporation and Sony patent roughens a bonding surface
and then heats and presses the assembly "so as to bond the bonding
surfaces";[^pat-target-bond-mrc] a Japan Energy patent claims a
"solid-phase bonded interface accompanied with no appreciable thermal
diffusion layer", with a "bonded area percentage of 100%" and the
target's "microstructure and crystal orientation" kept
intact.[^pat-target-bond-japanenergy] Erosion decides how much of a
target can be used: a Genus patent shapes the back of the target to
conform "substantially in shape to the eroded surface at
end-of-life".[^pat-target-profile-genus]

## Representative materials and grades

Targets are sold to a customer's or tool maker's specification of
purity, composition, grain size, bond and dimensions; ASTM's withdrawn
specification for titanium targets (for through-silicon vias) lists
"purity, grain size, inner quality, bonding, dimension, and appearance"
among its requirements.[^astm-f3166] The examples below are current
supplier statements, not the targets SkyWater buys.

* **Titanium.** JX Advanced Metals offers "4N5 (Ti 99.995% or above) 5N
  5N5" titanium, with "SFG (Super Fine Grain)" and "SR (Sputter Ready)
  Finish" as standard "To minimize particle levels and shorten burn-in
  time";[^jx-semi-targets] Solstice lists titanium at 4N5, 5N and 5N5 in
  monolithic and diffusion-bonded designs.[^solstice-targets]
* **Aluminium–copper.** Solstice lists "AlCu" and "AlSiCu" at "99.99%
  (4N)-99.9995% (5N5)" purity, in monolithic and diffusion-bonded
  designs, and notes that "Al alloy composition can be tuned to customer
  request".[^solstice-targets] The Cypress reports for the fab (see
  *At SkyWater*) give the alloy as "Al-0.5%Cu" and "Al 0.5%
  Cu".[^sec-01][^cyp-qtp-113005][^cyp-qtp-123907]
* **Titanium–tungsten.** Powder-metallurgy WTi at "3N~4N8" purity and
  density "Above 99%", with diffusion, "Nano" or indium
  bonding;[^solstice-targets] 10 wt.% titanium in the Hitachi Metals
  patent.[^pat-tiw-hitachi]
* **Coils and process kits.** Titanium coils "that support ion metal plasma
  sputtering technology for PVD processing" at 4N5 and 5N purity for
  200 mm and 300 mm chambers;[^solstice-targets] JX supplies titanium
  "200 mm parts sets (coils, pins, caps)" as "an officially authorized
  supplier" for Applied Materials.[^jx-semi-targets] Applied Materials
  called the planar target and coil of its IMP chamber "low cost
  consumable items".[^amat-ism-2000]

## At SkyWater

### What SkyWater's filings and pages list

Under "Film Deposition", SkyWater's *Facilities & Capabilities* page
lists one PVD tool and its films:[^skw-01]

> "AMAT PVD Metal"
>
> "Sputter etch, degas" · "Aluminum both pure and Cu doped" · "TiW" ·
> "ESC TiN" · "Imp TiN" · "Collimated Ti" · "WN" · "Cobalt" · "Niobium" ·
> "SiO2"

and its metal etchers as "Lam 9600, Al, TiW, TiN, Pt" and "Lam 2300
Versys, Al, TiW, TiN, Nb, Pt".[^skw-01] Read term by term, the PVD entry
implies targets of aluminium with and without copper, titanium–tungsten,
titanium (for "Collimated Ti" and, with nitrogen, the two TiN entries),
and, for films no SKY130 step uses, cobalt, niobium and a tungsten or
tungsten nitride source; whether "SiO2" is sputtered from an oxide
target is not stated. These are our readings of film names; the page
names no target. The filings describe the raw materials as including
"high-purity metals for film deposition processes" and name target
suppliers:[^sec-01][^sec-02]

| Filing | Sputter-target suppliers as named |
|--------|-----------------------------------|
| S-1 (2021)[^sec-01] | "Honeywell Electronic Materials, Inc. (metal sputter targets)" |
| 10-K for fiscal 2023[^sec-02] | "Honeywell Electronic Materials, Inc. (metal sputtering targets)"; "JX Metals USA, Inc. (metal sputtering targets)" |

Neither filing names a metal. Solstice Advanced Materials states that it
"was created through the spin-off of the former Advanced Materials
business of Honeywell International Inc.", completed on 2025-10-30, a
business that worked on "electronic materials";[^solstice-history] its
current brochure offers the titanium, aluminium alloy and WTi targets
listed above.[^solstice-targets] The Solstice pages do not name
Honeywell Electronic Materials, Inc., and neither Solstice nor JX names
SkyWater. For the films themselves, SkyWater's S-1 states that "Before
we began independent operations, our fab was owned and operated by
Cypress Semiconductor Corporation, or Cypress, as a captive
manufacturing facility for 20 years",[^sec-01] and Cypress's documents
name that fab "Cypress Minnesota" and "CMI (Fab 4)".[^cyp-pin145273][^cyp-qtp-113005] A 2013 Cypress
qualification report for an S8 product from the fab gives "Metal 1: 100A Ti / 3200A
Al -0.5%Cu / 300A TiW",[^cyp-qtp-113005] and a 2014 notification
announced aligning "our internal Cypress Minnesota process, Titanium
Tungsten (TiW) based metal stack, with the industry-wide Best Known Method
Titanium Nitride (TiN) based metal stack", with a qualified stack of
"150A Ti/250A TiN/3200A Al 0.5% Cu/90A Ti/500A TiN".[^cyp-pin145273][^cyp-qtp-123907]
Edwards's PDK lecture names the local interconnect "Titanium Nitride
(TiN)".[^ann-16]

### Strength of the evidence

The PVD entries are SkyWater statements and rank as **strong** evidence
that aluminium–copper, TiW, TiN and collimated titanium films are
deposited at the fab, on the scale of the
{ref}`machines index <machines-reading-evidence>`; that they imply
titanium, Al–Cu and TiW targets is a reading, though a direct one.[^skw-01]
The supplier statements are strong as statements but name no metal and
no chamber, and the second supplier appears only in the 2023
report.[^sec-01][^sec-02] The Cypress documents are public reports on
products made at the same fab, so they are strong for those products'
stacks in 2013 and 2014 but do not show which stack or target set SKY130
lots use.[^cyp-qtp-113005][^cyp-pin145273] Target purities, grain sizes
and bonds at SkyWater are not public; the supplier figures above describe
current products in general.

(material-sputter-targets-steps)=
### SKY130 steps that use this class

This page covers the rows of the {ref}`materials index <materials-table>`
listed below by key; the steps are those whose *Resources required* section
names one of them (the union of the rows' *Steps* cells).

Materials index rows covered:

* `ti-target` — titanium sputter targets
* `alcu-target` — aluminium–copper sputter targets
* `tiw-target` — titanium–tungsten sputter targets

Steps:

{ref}`TI/TIN1 <step-097>`, {ref}`LITIN <step-101>`, {ref}`TIN2 <step-109>`, {ref}`TIAL6 <step-112>`, {ref}`TIN3 <step-120>`, {ref}`TIAL12 <step-123>`, {ref}`TIN4 <step-131>`, {ref}`WTIAL3 <step-134>`, {ref}`CAPTIW1 <step-136>`, {ref}`TIN5 <step-146>`, {ref}`WTIAL4 <step-149>`, {ref}`CAPTIW2 <step-151>`, {ref}`WTIAL5 <step-161>`

These are the same thirteen steps the
{ref}`PVD cluster tool page <machine-pvd-cluster-tool>` assigns to its
class. On the step pages' readings, titanium serves the contact liner,
the TiN via liners, the TiN local interconnect and the underlayer of the
metal stacks; aluminium–copper the five metal stacks; and TiW the two
capacitor top plates and, on the reading the step pages take, the stack
caps. Whether the stack caps need a Ti:W target at all, or a titanium
target sputtered reactively to TiN, turns on the unresolved question set
out under {ref}`overview-metal-cap`.

## Supply, handling, safety and facilities

None of the SkyWater sources cited here describes target logistics,
chamber maintenance or target reclaim; the points below are supplier
statements or industry practice.

* **Changes and burn-in.** A new target is conditioned before product
  wafers; a supplier offers finishes "To minimize particle levels and
  shorten burn-in time".[^jx-semi-targets] Target life is set by erosion
  through the racetrack.[^wiki-sputter][^pat-target-profile-genus]
* **Bonds and cooling.** The bond carries the heat of sputtering to the
  cooled backing plate, and bonds are inspected ultrasonically; ASTM
  F1512 standardised that inspection until its withdrawal in
  2020.[^astm-f1512]
* **Process kits.** Collimators collect the off-normal metal
  flux,[^rossnagel-1991] coils are made of the target
  metal[^jx-semi-targets] and pasted with it,[^pat-imp-coil-amat] and
  shields, coils and collimators are replaced on a schedule tied to
  target life (industry practice).
* **Particles and arcs.** Inclusions and poorly made powder targets
  raise defect densities on the wafer,[^wickersham-2001][^waterman-1990]
  which the fab watches on monitor wafers
  ({ref}`machine-defect-inspection`).
* **Supply.** Target makers describe control of the chain from refined
  metal to finished target; JX states that for titanium "the Group has a
  full supply chain from raw material to target".[^jx-semi-targets]
  SkyWater's 2023 annual report names two target
  suppliers.[^sec-02]

## Process-integration notes for SKY130

These notes connect the class to the step pages; they add no SKY130
conditions of their own. SKY130's target materials, purities and
sputtering recipes are not public.

* **One titanium target, several films.** On the step pages' readings
  the contact liner ({ref}`TI/TIN1 <step-097>`), the via liners
  ({ref}`TIN2 <step-109>` to {ref}`TIN5 <step-146>`), the local
  interconnect ({ref}`LITIN <step-101>`) and the stack underlayers all
  draw on titanium targets, reactively for TiN; SkyWater lists
  "Collimated Ti", "Imp TiN" and "ESC TiN" as separate entries, which the
  pages read as separate chambers.[^skw-01] The nitrogen content of IMP
  TiN at the bottom of a hole depends on the deposition
  mode.[^mao-2004]
* **TiW or TiN stack.** The step pages describe the Ti/Al–Cu/TiW stack of
  the 2013 report; after the 2014 change a TiN-capped stack would use
  titanium targets and nitrogen where the older stack used a Ti:W target
  (our reading).[^cyp-qtp-113005][^cyp-pin145273] Which stack SKY130
  lots use is not public: the evidence on both sides is set out under
  {ref}`overview-metal-cap`. The choice changes how much Ti:W target is
  consumed and how much titanium, but not the set of targets the fab
  must hold, since the MiM plates need Ti:W on the step pages' reading
  either way.
* **The capacitor plates.** {ref}`CAPTIW1 <step-136>` and
  {ref}`CAPTIW2 <step-151>` read the MiM top plate, "a thin conductor
  layer on top of the dielectric",[^pdk-07] as TiW on SkyWater's "TiW"
  entry (inference);[^skw-01] TiW particles from the target would land
  directly on the capacitor dielectric, which is why the target's
  particle performance matters there (our
  reading).[^pat-tiw-hitachi][^waterman-1990]
* **Thick aluminium.** Metal 5 is drawn 1.26 µm thick against 0.36 µm
  for metals 1 and 2;[^pdk-04] the {ref}`WTIAL5 <step-161>` page notes
  that it consumes more Al–Cu target per wafer than any other level (its
  arithmetic from the thicknesses).
* **Copper in the wiring.** The copper that the alloy targets carry is
  there for electromigration lifetime;[^ames-1970][^wiki-em] the
  resulting aluminium–copper lines must then be protected from corrosion
  after the chlorine-based metal etches, as the
  {ref}`metal etcher page <machine-plasma-etcher-metal>` describes.

## Related pages

* {ref}`machine-pvd-cluster-tool` — the chambers the targets are mounted
  in.
* {ref}`category-deposition` — sputtering physics and the deposition
  steps.
* {ref}`machine-plasma-etcher-metal` — the etchers that pattern the
  sputtered stacks.
* {ref}`materials-index` — all consumable classes, including the argon
  and nitrogen of the sputtering chambers.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the "AMAT PVD Metal"
  and metal-etch entries.[^skw-01]
* SkyWater Technology, Form S-1 (2021) and Form 10-K for fiscal 2023 —
  the raw-materials paragraphs and sputter-target
  suppliers.[^sec-01][^sec-02]
* Cypress Semiconductor, QTP 113005, QTP 123907 and PIN145273 — the S8
  metal stacks and the 2014 change from TiW to
  TiN.[^cyp-qtp-113005][^cyp-qtp-123907][^cyp-pin145273]
* SkyWater PDK Authors, `metal_stack.svg` and *Device Details*; Edwards,
  PDK lecture — conductor thicknesses, the MiM top plate and the TiN
  local interconnect.[^pdk-04][^pdk-07][^ann-16]
* Solstice Advanced Materials, *PVD Sputtering Targets and Coil Sets* and
  *History and Brand Transition* — current target specifications and the
  Honeywell spin-off.[^solstice-targets][^solstice-history]
* JX Advanced Metals, *Sputtering Target (PVD) for Semiconductor* and
  *What Is Sputtering?* — titanium targets, coils and parts
  sets.[^jx-semi-targets][^jx-sputtering]
* Applied Materials, *Interconnect Systems & Modules* (product page,
  Wayback capture of 2000-08-15) — the IMP
  chamber's target and coil as consumables.[^amat-ism-2000]

### High-level understanding

* Wikipedia, *Sputter deposition* and *Physical vapor deposition* —
  magnetrons, targets, erosion and reactive
  sputtering.[^wiki-sputter][^wiki-pvd]
* Wikipedia, *Titanium nitride* and *Electromigration* — the liner film
  and the reason for copper in aluminium.[^wiki-tin][^wiki-em]
* Ohring, *Materials Science of Thin Films* — sputtering and film
  growth.[^ohring-2002]
* Seshan (ed.), *Handbook of Thin-Film Deposition Processes and
  Techniques* — sputtering equipment and targets.[^seshan-2002]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  aluminium films and PVD.[^txt-02]

### Deep dive

* Thornton, *JVST* 1974 — the structure-zone model for sputtered
  coatings.[^thornton-1974]
* Ames, d'Heurle and Horstmann, *IBM J. Res. Dev.* 1970 — copper doping
  against electromigration in aluminium.[^ames-1970]
* Nicolet, *Thin Solid Films* 1978 — diffusion barriers in thin
  films.[^nicolet-1978]
* Waterman, Dunlop and Brat, VMIC 1990 — TiW target manufacture, purity
  and film defects.[^waterman-1990]
* Rossnagel et al., *JVST A* 1991 — collimated magnetron
  sputtering.[^rossnagel-1991]
* Leybovich and Kuniya, *JVST A* 1993 — target grain relief and
  orientation against discharge characteristics.[^leybovich-1993]
* Wickersham et al., *JVST A* 2001 — the inclusion size that makes
  aluminium targets arc.[^wickersham-2001]
* Mao and Hopwood, *JAP* 2004 — ionised deposition of TiN.[^mao-2004]
* Berg and Nyberg, *Thin Solid Films* 2005 — reactive sputtering
  processes.[^berg-2005]
* Hiraki (Hitachi Metals), US 5,160,534 — TiW target structure against
  particles.[^pat-tiw-hitachi]
* Perry, Gilman and Van den Sype (Praxair), US 6,605,199 — textured
  fine-grained aluminium alloy targets.[^pat-target-texture-praxair]
* Hunt and Gilman (Materials Research Corp. and Sony), US 5,836,506 —
  a pressed and heated target–backing plate bond.[^pat-target-bond-mrc]
* Ohhashi et al. (Japan Energy), US 5,693,203 — solid-phase bonding that
  preserves target microstructure.[^pat-target-bond-japanenergy]
* Boys (Genus), US 5,215,639 — a target profiled to its end-of-life
  erosion.[^pat-target-profile-genus]
* Ngan (Applied Materials), US 5,707,498 — pasting the IMP coil with
  target material.[^pat-imp-coil-amat]
* ASTM F1512 — ultrasonic evaluation of target–backing plate
  bonds.[^astm-f1512]
* ASTM F3166 — a specification for high-purity titanium
  targets.[^astm-f3166]

## Open questions

* Which metals, alloys, purities and suppliers SkyWater's targets are,
  and whether the Cypress "Al-0.5%Cu" alloy is still used, are not
  stated.[^skw-01][^sec-01][^sec-02]
* Whether SKY130 lots use the TiW-capped or the TiN-capped metal stack,
  and so whether TiW targets serve anything besides the capacitor plates,
  is not public;[^cyp-pin145273] see
  {ref}`overview-metal-cap`.
* What "ESC" and "Imp" denote on SkyWater's TiN entries, and whether
  they are separate titanium-target chambers, is not stated.[^skw-01]
* Whether "Honeywell Electronic Materials, Inc." in SkyWater's filings
  is now part of Solstice Advanced Materials is not stated by either
  company's pages cited here.[^sec-02][^solstice-history]

<!-- footnotes -->

[^jx-sputtering]: JX Advanced Metals Corporation, *What Is Sputtering?*,
    sputtering targets page, accessed 2026-09-13.
    <https://www.jx-nmm.com/english/products/sputtering/about_sputtering.html>
[^cyp-qtp-113005]: Cypress Semiconductor, *Product Qualification Plan,
    QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8
    Technology, CMI (Fab 4)*, document 001-85611 Rev. *A, January 2013
    (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^jx-semi-targets]: JX Advanced Metals Corporation, *Sputtering Target
    (PVD) for Semiconductor*, product page, accessed 2026-09-13.
    <https://www.jx-nmm.com/english/products/sputtering/semiconductor_st/>
[^solstice-targets]: Solstice Advanced Materials, *PVD Sputtering
    Targets and Coil Sets*, brochure 7610006-esm-sls-sputtering-targets
    (08/26), accessed 2026-09-13.
    <https://www.solstice.com/content/dam/advancedmaterials/solstice/events/semicon-tw-2026/sputtering-targets.pdf>
[^leybovich-1993]: A. Leybovich and T. Kuniya, "Effects of aluminum
    sputtering target surface grain relief and crystallographic
    orientation on sputtering I–V characteristics", *Journal of Vacuum
    Science & Technology A* **11**(4), 1553–1557 (1993).
    <https://doi.org/10.1116/1.578504>
[^astm-f1512]: ASTM International, *F1512-94(2011) Standard Practice for
    Ultrasonic C-Scan Bond Evaluation of Sputtering Target-Backing Plate
    Assemblies* (withdrawn 2020), catalogue page; read from the Wayback
    Machine capture of 2025-01-14.
    <https://www.astm.org/f1512-94r11.html>
    <https://web.archive.org/web/20250114231553/https://www.astm.org/f1512-94r11.html>
[^wiki-sputter]: Wikipedia, *Sputter deposition*.
    <https://en.wikipedia.org/wiki/Sputter_deposition>
[^wickersham-2001]: C. E. Wickersham, J. E. Poole, A. Leybovich and L.
    Zhu, "Measurements of the critical inclusion size for arcing and
    macroparticle ejection from aluminum sputtering targets", *Journal of
    Vacuum Science & Technology A* **19**(6), 2767–2772 (2001).
    <https://doi.org/10.1116/1.1403719>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; film deposition and metal etch entries re-checked
    2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; the "Business" overview and the "Raw
    materials." run-in paragraph under "Manufacturing"; read from a
    Wayback Machine copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; "Raw materials" paragraph; read from a Wayback Machine
    copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^thornton-1974]: J. A. Thornton, "Influence of apparatus geometry and
    deposition conditions on the structure and topography of thick
    sputtered coatings", *Journal of Vacuum Science and Technology*
    **11**(4), 666–670 (1974). <https://doi.org/10.1116/1.1312732>
[^berg-2005]: S. Berg and T. Nyberg, "Fundamental understanding and
    modeling of reactive sputtering processes", *Thin Solid Films*
    **476**(2), 215–230 (2005). <https://doi.org/10.1016/j.tsf.2004.10.051>
[^mao-2004]: D. Mao and J. Hopwood, "Ionized physical vapor deposition of
    titanium nitride: A deposition model", *Journal of Applied Physics*
    **96**(1), 820–828 (2004). <https://doi.org/10.1063/1.1753663>
[^rossnagel-1991]: S. M. Rossnagel, D. Mikalsen, H. Kinoshita and J. J.
    Cuomo, "Collimated magnetron sputter deposition", *Journal of Vacuum
    Science & Technology A* **9**(2), 261–265 (1991).
    <https://doi.org/10.1116/1.577531>
[^pat-imp-coil-amat]: K. K.-T. Ngan (Applied Materials), *Avoiding
    contamination from induction coil in ionized sputtering*,
    US 5,707,498 A, filed 1996-07-12, granted 1998-01-13.
    <https://patents.google.com/patent/US5707498A/en>
[^ames-1970]: I. Ames, F. M. d'Heurle and R. E. Horstmann, "Reduction of
    Electromigration in Aluminum Films by Copper Doping", *IBM Journal
    of Research and Development* **14**(4), 461–463 (1970).
    <https://doi.org/10.1147/rd.144.0461>
[^pat-target-texture-praxair]: A. C. Perry, P. S. Gilman and J. Van den
    Sype (Praxair S.T. Technology), *Textured-metastable aluminum alloy
    sputter targets and method of manufacture*, US 6,605,199 B2, filed
    2001-11-14, granted 2003-08-12.
    <https://patents.google.com/patent/US6605199B2/en>
[^pat-tiw-hitachi]: A. Hiraki (Hitachi Metals), *Titanium-tungsten
    target material for sputtering and manufacturing method therefor*,
    US 5,160,534 A, filed 1991-05-31, granted 1992-11-03.
    <https://patents.google.com/patent/US5160534A/en>
[^nicolet-1978]: M.-A. Nicolet, "Diffusion barriers in thin films",
    *Thin Solid Films* **52**(3), 415–443 (1978).
    <https://doi.org/10.1016/0040-6090(78)90184-0>
[^waterman-1990]: E. Waterman, J. Dunlop and T. Brat, "Tungsten-titanium
    sputtering target processing effects on particle generation and thin
    film properties for VLSI applications", *Proc. Seventh International
    IEEE VLSI Multilevel Interconnection Conference (VMIC 1990)*,
    pp. 329–331. <https://doi.org/10.1109/VMIC.1990.127887>
[^pat-target-bond-mrc]: T. J. Hunt and P. S. Gilman (Materials Research
    Corp. and Sony Corp.), *Sputter target/backing plate assembly and
    method of making same*, US 5,836,506 A, filed 1995-04-21, granted
    1998-11-17. <https://patents.google.com/patent/US5836506A/en>
[^pat-target-bond-japanenergy]: T. Ohhashi, H. Fukuyo, I. Sawamura, K.
    Nakamura, A. Fukushima and M. Nagasawa (Japan Energy Corp.),
    *Sputtering target assembly having solid-phase bonded interface*,
    US 5,693,203 A, priority 1992-09-29, granted 1997-12-02.
    <https://patents.google.com/patent/US5693203A/en>
[^pat-target-profile-genus]: D. R. Boys (Genus), *Composite sputtering
    target structures and process for producing such structures*,
    US 5,215,639 A, priority 1984-10-09, granted 1993-06-01.
    <https://patents.google.com/patent/US5215639A/en>
[^astm-f3166]: ASTM International, *F3166-16 Standard Specification for
    High-Purity Titanium Sputtering Target Used for Through-Silicon Vias
    (TSV) Metallization* (withdrawn 2023), catalogue page; read from the
    Wayback Machine capture of 2025-01-17.
    <https://www.astm.org/f3166-16.html>
    <https://web.archive.org/web/20250117070227/https://www.astm.org/f3166-16.html>
[^cyp-qtp-123907]: Cypress Semiconductor, *Fab Process Qualification
    Report, QTP# 123907, 132302, 132301: Metal Stack Change, S8
    Technology, Fab 4 CMI*, document 001-91369 Rev. **, March 2014
    (copy hosted by Tokyo Electron Device as the attachment to
    Cypress Product Information Notification PIN145273, 2014-03-13,
    which states the report is attached and available from
    cypress.com; <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>).
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/145273-Qualification_Report.pdf>
[^amat-ism-2000]: Applied Materials, *Interconnect Systems & Modules*
    (liner/barrier and tungsten CVD systems), product page; Wayback
    Machine capture of 2000-08-15.
    <https://web.archive.org/web/20000815075033/http://www.appliedmaterials.com:80/products/ism_liner.html>
[^solstice-history]: Solstice Advanced Materials, *Solstice Advanced
    Materials: History and Brand Transition*, company page, accessed
    2026-09-13.
    <https://www.solstice.com/us/en/about-us/solstice-advanced-materials-history-and-brand-transition>
[^cyp-pin145273]: Cypress Semiconductor, *Product Information
    Notification PIN145273: Improvement of Cypress Minnesota
    Back-End-of-Line Integration for 130nm SONOS Product Families*,
    document 001-11741 Rev. *H, 2014-03-13 (copy hosted by Tokyo
    Electron Device).
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>
[^ann-16]: T. Edwards (Efabless), *Introduction to the SkyWater PDK —
    The New Age of Open Source Silicon*, lecture slides, 2021-10-08
    (UC San Diego BENG 207).
    <https://isn.ucsd.edu/courses/beng207/lectures/Tim_Edwards_2021_slides.pdf>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, section "MiM capacitors".
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^wiki-em]: Wikipedia, *Electromigration*.
    <https://en.wikipedia.org/wiki/Electromigration>
[^wiki-pvd]: Wikipedia, *Physical vapor deposition*.
    <https://en.wikipedia.org/wiki/Physical_vapor_deposition>
[^wiki-tin]: Wikipedia, *Titanium nitride*.
    <https://en.wikipedia.org/wiki/Titanium_nitride>
[^ohring-2002]: M. Ohring, *Materials Science of Thin Films*, 2nd ed.,
    Academic Press, 2002.
    <https://doi.org/10.1016/B978-0-12-524975-1.X5000-9>
[^seshan-2002]: K. Seshan (ed.), *Handbook of Thin-Film Deposition
    Processes and Techniques: Principles, Methods, Equipment and
    Applications*, 2nd ed., Noyes Publications / William Andrew, 2002,
    ISBN 978-0-8155-1442-8. <https://openlibrary.org/isbn/9780815514428>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
