(machine-pvd-cluster-tool)=
# PVD (sputtering) cluster tool

A PVD cluster tool is the vacuum platform a fab uses to sputter the
metal films of the back end: titanium and titanium nitride liners, the
aluminium–copper alloy of the wiring, and refractory caps such as
titanium–tungsten. Several single-wafer chambers — degas, sputter
pre-clean and one chamber per target — sit around robots in a vacuum
that the wafer never leaves between films, so that a stack of three
films is deposited without an oxide forming between them. Within the
class the chambers differ in how they deliver metal into holes: plain
magnetron sputtering, collimated sputtering or ionised metal plasma
({term}`IMP`). This page describes the class in general, lists
representative 200 mm-era models, and then says what SkyWater has
published about its own tool of this class and which SKY130 steps this
reference assigns to it. The film physics is summarised on the
{ref}`category page <category-deposition>`.

| | PVD (sputtering) cluster tool |
|---|---|
| What it does | Deposits metal films by "ejecting material from a 'target' that is a source onto a 'substrate' such as a silicon wafer"; "Sputtering is used extensively in the semiconductor industry to deposit thin films of various materials in integrated circuit processing".[^wiki-sputter] |
| Sources | Magnetrons "that utilize strong electric and magnetic fields to confine charged plasma particles close to the surface of the sputter target";[^wiki-sputter] a "collimating filter" with cells of "length to diameter ratio on the order of 1:1 to 3:1";[^pat-collimator-varian] an RF coil that ionises the sputtered metal, reaching "≳80% at pressures in the 25–35 mTorr range".[^rossnagel-1993] |
| Platform | Applied's Endura, "a modular, two-stage, single-wafer, multi-chamber platform that accommodates both ultra-high vacuum processes like PVD and conventional high vacuum processes like CVD and etch";[^amat-1997] today "up to nine process chambers, including two preclean chambers for native oxide removal".[^amat-endura] |
| Films | Aluminium alloys, titanium, and nitrides by reactive sputtering with "a reactive gas introduced into the sputtering chamber such as oxygen or nitrogen";[^wiki-sputter] Ti/TiN liners[^amat-ism-2000] and aluminium "over tungsten plugs"[^amat-al-slab-2002] on Applied's platforms; SkyWater also lists TiW.[^skw-01] |
| Bottom coverage | "only 20% coverage" for unbiased aluminium in Skelly and Gruenke's vias;[^skelly-1986] "(>40% at 5:1)" for Applied's Vectra IMP with wafer bias.[^amat-ism-2000] |
| 200 mm era | Applied's Endura (April 1990), Endura HP (1993) and VHP (1994), and Ti/TiN liner options from December 1996;[^amat-1997] Novellus's INOVA, from its purchase of "the Thin Film Systems business of Varian Associates".[^novellus-pvd-1998] |
| SkyWater-listed tool | "AMAT PVD Metal": "Sputter etch, degas", "Aluminum both pure and Cu doped", "TiW", "{term}`ESC` TiN", "Imp TiN", "Collimated Ti", "WN", "Cobalt", "Niobium", "SiO2"[^skw-01] |
| SKY130 steps | 13 steps; see {ref}`SKY130 steps assigned to this class <machine-pvd-cluster-tool-steps>` |

## What the machine class is and how it works

In a sputtering chamber argon ions from a plasma strike a metal target
and knock atoms out of it; the atoms cross the chamber and condense on
the wafer. The flux leaves the target in all directions, and the film
grows wherever atoms can see the target, so the bottom of a narrow hole
receives little. A metal back end needs several such films in sequence,
each on a clean surface. What makes a machine a production PVD cluster
tool is therefore the platform as much as the chambers: a vacuum good
enough that titanium and aluminium do not oxidise between chambers, a
degas and sputter pre-clean before the first film, chambers that put
enough metal at the bottom of contacts and vias, and targets, shields
and chucks that can be changed without long downtime.

### Magnetron sputtering

A magnetron traps electrons near the target: "electrons follow helical
paths around magnetic field lines, undergoing more ionizing collisions
with gaseous neutrals near the target surface", which gives "a higher
deposition rate" and lets the plasma "be sustained at a lower
pressure".[^wiki-sputter] Most of what leaves the target is neutral —
"typically only a small fraction of the ejected particles are
ionized—on the order of 1 percent" — and the gas pressure decides
whether atoms fly ballistically or diffuse to the wafer.[^wiki-sputter]
Thornton's structure-zone study of sputtered coatings found
microstructures "generally consistent with the three-zone model", and
"at low argon pressures a broad zone 1–zone 2 transition zone consisting
of densely packed fibrous grains".[^thornton-1974] Ions striking the
wafer also move deposited metal: Skelly and Gruenke planarised
"1.3 μm diam, straight-walled vias 1 μm deep" by bias sputtering
aluminium, where "Unbiased deposition results in only 20%
coverage".[^skelly-1986]

### The cluster platform

Applied Materials' staged-vacuum patent, with a 1989 priority date,
describes the
architecture: "multiple, isolated vacuum stages between the cassette load
lock station and the main vacuum processing chambers", "A vacuum
gradient" so that "a very high degree of vacuum" can be used in the
process chambers "without lengthy pump down times", "Separate robot
chambers" for the load locks and the process chambers, and
"Pre-treatment and post-treatment chambers" in the paths between
them.[^pat-staged-vacuum-amat] In its description a pre-cleaning chamber
prepares wafers "before they enter a high vacuum transfer station", and
a cool-down chamber receives them after processing.[^pat-staged-vacuum-amat]
Applied launched the Endura PVD system in April 1990 as "a modular,
two-stage, single-wafer, multi-chamber platform".[^amat-1997] Its Endura
SL of about 2000 has "dual VHP+ robots for the simultaneous exchange of
four wafers and can accommodate up to six process chambers for high
throughput, greater than 60 wph", with "any chamber in any
position".[^amat-ism-cu-2000]

### Degas and pre-clean

Films in a contact or via must land on a clean surface. SkyWater's list
names "Sputter etch, degas" among its PVD capabilities,[^skw-01] and
today's Endura provides "two preclean chambers for native oxide
removal".[^amat-endura] Applied's liner system of the late 1990s combined
"a PVD Vectra Ion Metal Plasma (IMP) Titanium (Ti) chamber, CVD Titanium
Nitride (TiN) TxZ chamber, and the Preclean II chamber", and "The
sequential processes are performed without a vacuum break, resulting in
superior quality films with no TiOx formation at the
interface".[^amat-ism-2000] A Novellus induction-source patent describes
a pre-clean of this kind: "a gentle, low voltage argon sputter
particularly suitable for the removal of thin oxides and contaminants
prior to the deposition of thin metal films".[^pat-icp-novellus]

### Collimated sputtering

A collimator filters the flux by angle. Varian's patent, with a 1990
priority date, passes sputtered particles "through a collimating filter
having a plurality of transmissive cells with a length to diameter ratio
on the order of 1:1 to 3:1" at a pressure "sufficiently low to prevent
substantial scattering of the particles between the source and the
workpiece".[^pat-collimator-varian] Rossnagel et al. restricted the flux
"to normal incidence ±5°" with "an array of collimating tubes", observed
"Hole filling at aspect ratios up to 3.0", and noted that atoms outside
that angle "are deposited on the inner surfaces of the
collimators".[^rossnagel-1991] Rossnagel's later review judged such
filtered or directional techniques to "suffer from poor efficiency, high
cost, and/or poor scaling".[^rossnagel-1998] Ryan et al. describe the
application to titanium and titanium nitride.[^ryan-1995]

### Ionised metal plasma

Ionised PVD adds a dense plasma between target and wafer. Rossnagel and
Hopwood combined "conventional magnetron sputter deposition with a rf
inductively coupled plasma", "set up by a metal coil immersed in the
plasma"; "By placing a negative bias on the sample, metal ions are then
accelerated across the sample sheath and deposited at normal incidence",
and the ionised fraction "rises to ≳80% at pressures in the 25–35 mTorr
range".[^rossnagel-1993] They scaled the technique "to 300 mm cathodes
and 200 mm wafers" and "demonstrated with Cu, AlCu, and
Ti/TiN".[^rossnagel-1994] Hopwood explains why: sputtered atoms entering
"a moderate pressure (4 Pa), high-density Ar plasma" are "first
thermalized and then ionized", and "over 80% of the metal species are
ionized using I-PVD".[^hopwood-1998] Coverage comes from deposition and
resputtering together: "combination of direct deposition and
trench-bottom resputtering results in good conformality of step
coverages".[^hamaguchi-1996]

Applied Materials' IMP chamber put this into production. Its Vectra IMP
"features a medium density Ion Metal Plasma source created between the
target and the wafer, resulting in a highly directional deposition
profile"; "Wafer bias capability further enhances bottom coverage (>40% at
5:1)"; "The simplicity of the planar target and coil design make them low
cost consumable items"; and
the chamber had been "production proven (>350 chambers to date)" by
2000.[^amat-ism-2000] Applied patents describe cycling the target power
so that sputtering alternates with "reverse sputter" of the wafer to
improve sidewall coverage,[^pat-imp-amat] and "pasting" the induction
coil with target material so that metal sputtered off the coil "will not
contaminate the film".[^pat-imp-coil-amat] Novellus's alternative, the
hollow-cathode magnetron, is "a hollow cathode with a non-planar target"
in which "plasma can be controlled to achieve high ionization levels, good
step coverage, and good process uniformity";[^pat-hcm-novellus] Novellus
wrote that its "HCM Ti/TiN films make an excellent diffusion barrier for
CVD W applications".[^novellus-pvd-2001]

### Reactive titanium nitride

Titanium nitride is sputtered from a titanium target in argon and
nitrogen. Reactive processes "are characterized by an hysteresis-like
behavior", which requires control of the gas partial
pressures;[^wiki-sputter] Berg and Nyberg model that
behaviour.[^berg-2005] In an ionised chamber the nitrogen that reaches
the bottom of a hole matters: Mao and Hopwood's model "depends critically
on the sticking coefficient for nitrogen atoms on TiNx surfaces" and
predicts "nitrogen deficient films at the bottom of trenches under
metal-mode deposition conditions".[^mao-2004]

### Aluminium alloy and via fill

Aluminium–copper is sputtered as the thick wiring film, and its step
coverage rises with wafer temperature: Taylor, Jain and Cale found that
"Step coverage improves with increasing temperature and decreasing
deposition rates".[^taylor-1998] Hot and forced fills went further.
Nishimura et al. achieved "Complete filling of a 0.5 mu m diameter via
hole with an aspect ratio of 1.6" with high-temperature Al–Si–Cu
sputtering over a thin titanium underlayer;[^nishimura-1991] Dirks et
al. explain reflow and forcefill, in which "an additional high stress has
been applied", by stress relaxation.[^dirks-1999] Hot bias sputtering has
a cost: "the electromigration lifetime of bias-sputtered Al films is
inferior to unbiased film".[^hariu-1989] The underlayer matters too:
Pramanik and Jain correlated "breaks in Al step coverage on via
sidewalls" with the grain roughness that the underlayer
produces.[^pramanik-1990] Applied's slab chambers deposit "aluminum over
tungsten plugs in logic and DRAM devices to form metal wiring", and its
ALPS+ fill runs at "low-fill temperatures (<430°C)";[^amat-al-slab-2002]
Novellus offered "MaxFill™ low pressure aluminum plug" fill on the
INOVA.[^novellus-pvd-2001]

## Representative 200 mm-era models

* **Applied Materials.** The Endura (April 1990), the Endura HP and VHP
  of 1993 and 1994, and, from December 1996, Endura HP Metal options for
  "titanium (Ti) and titanium nitride (TiN) liner/barrier films in
  sub-0.25-micron, high aspect ratio contact and via
  structures";[^amat-1997] the Integrated PVD/CVD Liner/Barrier system,
  with "more than 100 systems shipped" by 2000, and the Vectra IMP
  chamber;[^amat-ism-2000] the Endura SL;[^amat-ism-cu-2000] and the
  Self-Ionized Plasma (SIP) Ti/TiN ("TTN") chamber, "used in volume
  production for advanced devices with aspect ratios of
  7:1".[^amat-liner-barrier-2001]
  Applied describes the Endura today as "the most successful
  metallization system in the history of the semiconductor
  industry".[^amat-endura]
* **Novellus Systems.** The INOVA, made possible by "the acquisition of
  the Thin Film Systems business of Varian Associates, Inc.", with
  "Maxfill™ aluminum and superior Ti/Ti-nitride film quality" and a Ti/TiN
  process "in production with Controlled Divergence Technology" before the
  ionised HCM source;[^novellus-pvd-1998] and the 300 mm INOVA xT of
  2000.[^novellus-pvd-2001] Applied's 1997 annual report records patent
  litigation that followed "Novellus' acquisition of the Varian thin film
  PVD business unit".[^amat-1997]
* **Varian.** The collimated deposition patent above is Varian's;[^pat-collimator-varian]
  the step pages also name the Varian M2i ({ref}`TI/TIN1 <step-097>`),
  of which no vendor description was retrieved for this page.
* **Other vendors.** The step pages name MRC Eclipse
  ({ref}`TI/TIN1 <step-097>`), ULVAC and Anelva sputtering systems
  ({ref}`TIAL6 <step-112>`) and Electrotech/Trikon high-pressure fill
  modules ({ref}`WTIAL5 <step-161>`); no vendor description of them was
  retrieved for this page.

## At SkyWater

### What SkyWater lists

Under "Film Deposition", SkyWater's *Facilities & Capabilities* page
lists one PVD tool with ten sub-entries:[^skw-01]

> "AMAT PVD Metal"
>
> "Sputter etch, degas" · "Aluminum both pure and Cu doped" · "TiW" ·
> "ESC TiN" · "Imp TiN" · "Collimated Ti" · "WN" · "Cobalt" · "Niobium" ·
> "SiO2"

Read term by term: pre-clean and degas chambers; aluminium with and
without copper; titanium–tungsten; two titanium nitride processes, one
labelled "ESC" and one "Imp"; collimated titanium; tungsten nitride,
cobalt, niobium and silicon dioxide. The page does not expand "ESC" or
"Imp"; the step pages read them as a TiN chamber with an electrostatic
chuck and an ionised-metal-plasma TiN chamber (our reading). It does not
name the platform, the number of chambers or whether the list is one
tool or several.[^skw-01] SkyWater's filings name its sputter-target
suppliers: "Honeywell Electronic Materials, Inc. (metal sputter targets)"
in the S-1,[^sec-01] and Honeywell and "JX Metals USA, Inc. (metal
sputtering targets)" in the 10-K for 2023.[^sec-02]

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` the
listing is **strong** for the vendor and for each film and chamber type:
it is a SkyWater statement.[^skw-01] The platform is not named; the step
pages read "AMAT PVD Metal" as an Endura-class tool, an inference from
Applied's product line.[^amat-endura] The step grades assign no SKY130
step to the "WN", "Cobalt", "Niobium" or "SiO2" entries, and the capabilities page
also lists "Cu dual damascene" and "Nb damascene" modules that no SKY130
step page uses.[^skw-01] The target suppliers are strong as SkyWater
statements but are not tied to any chamber or film.[^sec-01][^sec-02]
The caveats that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`.

(machine-pvd-cluster-tool-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a PVD cluster tool
as the tool or one of two options (identical to the
{ref}`machines index <machines-index>` table):

{ref}`TI/TIN1 <step-097>`, {ref}`LITIN <step-101>`, {ref}`TIN2 <step-109>`, {ref}`TIAL6 <step-112>`, {ref}`TIN3 <step-120>`, {ref}`TIAL12 <step-123>`, {ref}`TIN4 <step-131>`, {ref}`WTIAL3 <step-134>`, {ref}`CAPTIW1 <step-136>`, {ref}`TIN5 <step-146>`, {ref}`WTIAL4 <step-149>`, {ref}`CAPTIW2 <step-151>`, {ref}`WTIAL5 <step-161>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"AMAT PVD Metal"** — *inference: "Imp TiN" and "Collimated Ti":* {ref}`TI/TIN1 <step-097>`; *inference: "ESC TiN":* {ref}`LITIN <step-101>`; *inference: "Imp TiN":* {ref}`TIN2 <step-109>`, {ref}`TIN3 <step-120>`, {ref}`TIN4 <step-131>`, {ref}`TIN5 <step-146>`; *inference: aluminium, "TiW" and the underlayer:* {ref}`TIAL6 <step-112>`, {ref}`TIAL12 <step-123>`, {ref}`WTIAL3 <step-134>`, {ref}`WTIAL4 <step-149>`, {ref}`WTIAL5 <step-161>`; *inference: "TiW":* {ref}`CAPTIW1 <step-136>`, {ref}`CAPTIW2 <step-151>`
* **The metal etchers as corroboration** — "Lam 9600, Al, TiW, TiN, Pt",
  "Lam 2300 Versys, Al, TiW, TiN, Nb, Pt": *named as corroboration only:*
  {ref}`TIAL6 <step-112>`, {ref}`TIAL12 <step-123>`,
  {ref}`WTIAL3 <step-134>`, {ref}`CAPTIW1 <step-136>`,
  {ref}`WTIAL4 <step-149>`, {ref}`CAPTIW2 <step-151>`,
  {ref}`WTIAL5 <step-161>`; the full grade list is on the
  {ref}`metal etcher page <machine-plasma-etcher-metal>`.

Every assignment is an inference from the listed chamber types: the
step pages match "Imp TiN" to the contact and via liners because of the
holes' aspect ratios, "ESC TiN" to the planar local-interconnect film,
and "TiW" and the aluminium entries to the metal stacks and the capacitor
plates, and grade the vendor and films strong.[^skw-01] Whether the
contact titanium is collimated or ionised is not public; SkyWater's list
names collimation for titanium and IMP for TiN.

## Consumables and facilities

The process gases are described on the
{ref}`process gases <material-process-gases>` page.
The targets are described on the
{ref}`sputter targets <material-sputter-targets>` page; targets and
process gases are listed in the {ref}`materials index
<materials-index>`; what is specific to a PVD cluster tool is summarised
here. None of the SkyWater sources describes the fab's pumps or target
logistics. Chamber parts and exhaust abatement are described on the
{ref}`hardware consumables and abatement <material-hardware-consumables>`
page.

* **Targets.** Titanium, aluminium–copper and TiW targets, one per
  chamber; SkyWater's filings name Honeywell and JX Metals as suppliers
  of "metal sputtering targets".[^sec-02] Magnetron targets erode
  unevenly: "a 'racetrack' erosion profile may appear on the surface of
  the target".[^wiki-sputter] TiW barrier films of the period were
  "typically composed of 10 wt% of titanium and the balance of
  tungsten", sputtered from TiW targets (category
  page).[^pat-tiw-hitachi]
* **Gases.** Argon for sputtering and pre-clean, nitrogen for reactive
  TiN.[^wiki-sputter]
* **Process kits.** Shields and clamp rings (category page), IMP coils
  and collimators, which collect metal that does not reach the wafer and
  are replaced as kits;[^rossnagel-1991][^amat-ism-2000] IMP coils are
  pasted with target material after a number of
  wafers.[^pat-imp-coil-amat]
* **Chucks and heaters.** Electrostatic or heated pedestals, with RF
  bias on IMP chambers;[^amat-ism-2000][^amat-liner-barrier-2001] the
  glossary entry {term}`electrostatic chuck` gives the principle.
* **Monitor wafers.** {ref}`Sheet resistance <machine-sheet-resistance-metrology>`,
  {ref}`thickness (XRF) <machine-film-thickness-metrology>`, reflectivity and stress on blanket wafers, as the step pages' industry-generic outlines
  describe
  ({ref}`TIAL6 <step-112>`).

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's sputtering recipes and most of
its film thicknesses are not public.

* **Liners under tungsten.** The {ref}`TI/TIN1 <step-097>` page reads the
  contact liner as titanium followed by IMP TiN, an inference from SkyWater's
  "Collimated Ti" and "Imp TiN" entries[^skw-01] and from Ti/TiN
  liner/barrier systems of the period such as the Endura with a Vectra
  IMP Ti chamber;[^amat-ism-2000] whether the titanium is collimated, as "Collimated Ti"
  would allow, or ionised is not public. The via-liner pages
  ({ref}`TIN2 <step-109>` to {ref}`TIN5 <step-146>`) read their liners as
  IMP TiN. Each liner is followed by a tungsten fill ({ref}`tungsten CVD page
  <machine-tungsten-cvd>`). Ionised deposition exists to put metal at
  the bottom of such holes.[^rossnagel-1994][^hopwood-1998]
* **The local interconnect.** The PDK draws `li` 0.1 µm thick,[^pdk-04]
  and Edwards's PDK lecture names it "Titanium Nitride (TiN)";[^ann-16]
  the {ref}`LITIN <step-101>` page reads it as sputtered TiN on the
  "ESC TiN" chamber (inference).[^skw-01]
* **The metal stacks.** A 2013 Cypress qualification report for an S8
  variant made in Bloomington gives metals 1 and 2 as 100 Å Ti, 3 200 Å
  Al–0.5%Cu and 300 Å TiW, and metal 3 with 7 200 Å of
  aluminium;[^cyp-qtp-113005] the {ref}`TIAL6 <step-112>` page notes that
  the first sum matches the PDK's 0.36 µm `met1`.[^pdk-04] In 2014 Cypress
  notified customers that it would align "our internal Cypress Minnesota
  process, Titanium Tungsten (TiW) based metal stack, with the
  industry-wide Best Known Method Titanium Nitride (TiN) based metal
  stack";[^cyp-pin145273] which stack SKY130 lots use is not public, and
  the step pages describe the TiW stack (inference). The chambers
  needed differ: the TiW stack needs a Ti:W chamber, the other a
  titanium chamber run reactively in nitrogen, and the 2014 stack has
  five films to the 2013 one's three. The evidence on both sides is set
  out under {ref}`overview-metal-cap`.
* **The capacitor top plates.** The PDK calls the MiM top plate "a thin
  conductor layer on top of the dielectric";[^pdk-07] the
  {ref}`CAPTIW1 <step-136>` and {ref}`CAPTIW2 <step-151>` pages read it
  as TiW on SkyWater's "TiW" entry (inference),[^skw-01] and the
  {ref}`metal etcher page <machine-plasma-etcher-metal>` notes that the
  same evidence would equally allow TiN.
* **The top metal.** Metal 5 is drawn 1.26 µm thick[^pdk-04] and is
  deposited into the via-4 holes ({ref}`WTIAL5 <step-161>`); whether the
  tool fills them hot, under pressure or not at all is not public, and the
  WTIAL5 page names the fill techniques above as possibilities only.
* **One vacuum sequence.** The stack pages read each Ti/Al–Cu/TiW stack
  as deposited without breaking vacuum (our reading), which is what the
  cluster architecture provides.[^pat-staged-vacuum-amat][^amat-ism-2000]

## Related pages

* {ref}`category-deposition` — sputtering physics and the deposition steps
  of SKY130.
* {ref}`machine-tungsten-cvd` — the tungsten fill that follows each
  liner.
* {ref}`machine-plasma-etcher-metal` — the etchers that pattern the
  local interconnect, the stacks and the capacitor plates.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — sputter targets and process gases.
* {ref}`material-sputter-targets` — target materials, purity, bonding
  and suppliers.
* {ref}`material-hardware-consumables` — chamber parts and exhaust
  abatement.
* {ref}`material-process-gases` — nitrogen, oxygen, hydrogen, argon,
  helium and the oxidation additives, their grades and SkyWater's listed
  gases.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

**Related patents.**

* {ref}`Staged-vacuum wafer processing system and method <patent-gp26998663>` — US 5,186,718 A (1989)
* {ref}`Collimated deposition apparatus and method <patent-gp23870722>` — US 5,330,628 A (1990)
* {ref}`Titanium-tungsten target material for sputtering and manufacturing method therefor <patent-gp27460980>` — US 5,160,534 A (1990)
* {ref}`Induction plasma source <patent-gp25518280>` — US 5,346,578 A (1992)
* {ref}`Avoiding contamination from induction coil in ionized sputtering <patent-gp24741421>` — US 5,707,498 A (1996)
* {ref}`Apparatus and method for controlling plasma uniformity across a substrate <patent-gp26812562>` — US 6,179,973 B1 (1999)
* {ref}`Alternate steps of IMP and sputtering process to improve sidewall coverage <patent-gp23783296>` — US 6,350,353 B2 (1999)
* {ref}`Method for forming a metallization structure in an integrated circuit <patent-gp23892778>` — US 6,969,448 B1 (1999)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the "AMAT PVD Metal"
  entry and its sub-entries.[^skw-01]
* SkyWater Technology, Form S-1 (2021) and Form 10-K for 2023 — the
  sputter-target suppliers.[^sec-01][^sec-02]
* Applied Materials, *1997 Annual Report* — the Endura's introduction,
  versions and liner/barrier options.[^amat-1997]
* Applied Materials, *Endura PVD* product page — the platform's chamber
  count and preclean chambers.[^amat-endura]
* Applied Materials, *Interconnect Systems & Modules* pages (2000) — the
  integrated liner/barrier system, the Vectra IMP chamber and the Endura
  SL.[^amat-ism-2000][^amat-ism-cu-2000]
* Applied Materials, *Aluminum Liner/Barrier* (2001) and *Aluminum Slab
  and Fill* (2002) pages — SIP Ti/TiN, aluminium over tungsten plugs and
  ALPS+ fill.[^amat-liner-barrier-2001][^amat-al-slab-2002]
* Novellus Systems, *Metal PVD Solutions* (1998 and 2001 captures) — the
  INOVA, its Varian origin and the HCM source.[^novellus-pvd-1998][^novellus-pvd-2001]
* Tepman et al. (Applied Materials), US 5,186,718 — the staged-vacuum
  multi-chamber platform.[^pat-staged-vacuum-amat]
* Demaray et al. (Varian), US 5,330,628 — collimated deposition.[^pat-collimator-varian]
* Cypress Semiconductor, QTP 113005 and PIN145273 — the S8 metal stack
  and its change from TiW to TiN.[^cyp-qtp-113005][^cyp-pin145273]
* SkyWater PDK Authors, `metal_stack.svg` and *Device Details*; Edwards,
  PDK lecture — the conductor thicknesses, the MiM top plate and the TiN
  local interconnect.[^pdk-04][^pdk-07][^ann-16]

### High-level understanding

* Wikipedia, *Sputter deposition* — magnetrons, reactive sputtering and
  film structure.[^wiki-sputter]
* Wikipedia, *Physical vapor deposition* — the family of PVD
  methods.[^wiki-pvd]
* Wikipedia, *Titanium nitride* — the liner and local-interconnect
  film.[^wiki-tin]
* Ohring, *Materials Science of Thin Films* — sputtering, film growth
  and step coverage.[^ohring-2002]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  aluminium thin films and PVD.[^txt-02]
* Seshan (ed.), *Handbook of Thin-Film Deposition Processes and
  Techniques* — sputtering equipment.[^seshan-2002]

### Deep dive

* Thornton, *JVST* 1974 — the structure-zone model for sputtered
  coatings.[^thornton-1974]
* Skelly and Gruenke, *JVST A* 1986 — bias-sputtered aluminium step
  coverage.[^skelly-1986]
* Rossnagel et al., *JVST A* 1991 — collimated magnetron sputter
  deposition.[^rossnagel-1991]
* Ryan et al., *MRS Bulletin* 1995 — collimated sputtering of Ti and
  TiN.[^ryan-1995]
* Rossnagel and Hopwood, *APL* 1993 — magnetron sputtering with high
  metal ionisation.[^rossnagel-1993]
* Rossnagel and Hopwood, *JVST B* 1994 — metal ion deposition scaled to
  200 mm wafers.[^rossnagel-1994]
* Hamaguchi and Rossnagel, *JVST B* 1996 — liner conformality in ionised
  sputtering.[^hamaguchi-1996]
* Hopwood, *Phys. Plasmas* 1998 — ionised PVD of interconnects.[^hopwood-1998]
* Rossnagel, *JVST B* 1998 — a review of directional and ionised
  PVD.[^rossnagel-1998]
* Mao and Hopwood, *JAP* 2004 — a deposition model for ionised
  TiN.[^mao-2004]
* Berg and Nyberg, *Thin Solid Films* 2005 — reactive sputtering
  processes.[^berg-2005]
* Taylor, Jain and Cale, *JVST A* 1998 — rate and temperature in
  aluminium step coverage.[^taylor-1998]
* Nishimura, Yamada and Ogawa, VMIC 1991 — high-temperature aluminium
  via fill.[^nishimura-1991]
* Hariu et al., IRPS 1989 — electromigration of hot bias-sputtered
  Al–Cu.[^hariu-1989]
* Pramanik and Jain, VMIC 1990 — underlayers and aluminium step
  coverage.[^pramanik-1990]
* Dirks et al., *JAP* 1999 — the mechanism of reflow and forcefill.[^dirks-1999]
* Gopalraja et al. (Applied Materials), US 6,350,353 — alternating IMP
  deposition and resputtering.[^pat-imp-amat]
* Ngan (Applied Materials), US 5,707,498 — pasting the IMP coil against
  contamination.[^pat-imp-coil-amat]
* Lai et al. (Novellus), US 6,179,973 — the hollow-cathode magnetron
  source.[^pat-hcm-novellus]

## Open questions

* Whether "AMAT PVD Metal" is one Endura-class tool or several, and which
  chambers it carries, are not stated.[^skw-01]
* What "ESC" and "Imp" denote on SkyWater's TiN entries is not stated.
* Whether the contact titanium is collimated or ionised, and whether the
  SKY130 metal stacks are the TiW or the TiN version of the Cypress
  stack, are not public; on the second, see
  {ref}`overview-metal-cap`.
* The model list above is incomplete: it covers the Applied Materials,
  Novellus and Varian systems for which a public description was found,
  not the MRC, ULVAC, Anelva, Electrotech and other sputtering systems of
  the period.

<!-- footnotes -->

[^wiki-sputter]: Wikipedia, *Sputter deposition*.
    <https://en.wikipedia.org/wiki/Sputter_deposition>
[^pat-collimator-varian]: R. E. Demaray, V. E. Hoffman, J. C. Helmer,
    Y. H. Park and R. R. Cochran (Varian Associates), *Collimated
    deposition apparatus and method*, US 5,330,628 A, filed 1991-10-23,
    granted 1994-07-19. <https://patents.google.com/patent/US5330628A/en>
[^rossnagel-1993]: S. M. Rossnagel and J. Hopwood, "Magnetron sputter
    deposition with high levels of metal ionization", *Applied Physics
    Letters* **63**(24), 3285–3287 (1993).
    <https://doi.org/10.1063/1.110176>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report* (Form 10-K
    for the fiscal year ended 1997-10-26).
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^amat-endura]: Applied Materials, *Endura PVD*, product page; read from
    the Wayback Machine capture of 2026-06-11.
    <https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html>
    <https://web.archive.org/web/20260611155710/https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html>
[^amat-ism-2000]: Applied Materials, *Interconnect Systems & Modules*
    (liner/barrier and tungsten CVD systems), product page; Wayback
    Machine capture of 2000-08-15.
    <https://web.archive.org/web/20000815075033/http://www.appliedmaterials.com:80/products/ism_liner.html>
[^amat-al-slab-2002]: Applied Materials, *Aluminum Slab and Fill*,
    product page; Wayback Machine capture of 2002-06-25.
    <https://web.archive.org/web/20020625163718/http://www.appliedmaterials.com:80/products/aluminum_slab_and_fill.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; film deposition and special module entries re-checked
    2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^skelly-1986]: D. W. Skelly and L. A. Gruenke, "Significant improvement
    in step coverage using bias sputtered aluminum", *Journal of Vacuum
    Science & Technology A* **4**(3), 457–460 (1986).
    <https://doi.org/10.1116/1.573905>
[^novellus-pvd-1998]: Novellus Systems, *Metal – PVD Solutions*, product
    page; Wayback Machine capture of 1998-06-11.
    <https://web.archive.org/web/19980611202757/http://www.novellus.com:80/products/pvd.htm>
[^thornton-1974]: J. A. Thornton, "Influence of apparatus geometry and
    deposition conditions on the structure and topography of thick
    sputtered coatings", *Journal of Vacuum Science and Technology*
    **11**(4), 666–670 (1974). <https://doi.org/10.1116/1.1312732>
[^pat-staged-vacuum-amat]: A. Tepman, H. Grunes, S. Somekh and D. Maydan
    (Applied Materials), *Staged-vacuum wafer processing system and
    method*, US 5,186,718 A, filed 1991-04-15, granted 1993-02-16.
    <https://patents.google.com/patent/US5186718A/en>
[^amat-ism-cu-2000]: Applied Materials, *Interconnect Systems & Modules*
    (copper and aluminium systems, Endura SL), product page; Wayback
    Machine capture of 2000-08-16.
    <https://web.archive.org/web/20000816055835/http://www.appliedmaterials.com:80/products/ism_coppalum.html>
[^pat-icp-novellus]: J. C. Benzing, E. K. Broadbent and J. K. H. Rough
    (Novellus Systems), *Induction plasma source*, US 5,346,578 A, filed
    1992-11-04, granted 1994-09-13.
    <https://patents.google.com/patent/US5346578A/en>
[^rossnagel-1991]: S. M. Rossnagel, D. Mikalsen, H. Kinoshita and J. J.
    Cuomo, "Collimated magnetron sputter deposition", *Journal of Vacuum
    Science & Technology A* **9**(2), 261–265 (1991).
    <https://doi.org/10.1116/1.577531>
[^rossnagel-1998]: S. M. Rossnagel, "Directional and ionized physical
    vapor deposition for microelectronics applications", *Journal of
    Vacuum Science & Technology B* **16**(5), 2585–2608 (1998).
    <https://doi.org/10.1116/1.590242>
[^ryan-1995]: J. G. Ryan, S. B. Brodsky, T. Katata, M. Honda, N. Shoda
    and H. Aochi, "Collimated Sputtering of Titanium and Titanium Nitride
    Films", *MRS Bulletin* **20**(11), 42–45 (1995).
    <https://doi.org/10.1557/S0883769400045553>
[^rossnagel-1994]: S. M. Rossnagel and J. Hopwood, "Metal ion deposition
    from ionized magnetron sputtering discharge", *Journal of Vacuum
    Science & Technology B* **12**(1), 449–453 (1994).
    <https://doi.org/10.1116/1.587142>
[^hopwood-1998]: J. Hopwood, "Ionized physical vapor deposition of
    integrated circuit interconnects", *Physics of Plasmas* **5**(5),
    1624–1631 (1998). <https://doi.org/10.1063/1.872829>
[^hamaguchi-1996]: S. Hamaguchi and S. M. Rossnagel, "Liner conformality
    in ionized magnetron sputter metal deposition processes", *Journal of
    Vacuum Science & Technology B* **14**(4), 2603–2608 (1996).
    <https://doi.org/10.1116/1.588993>
[^pat-imp-amat]: P. Gopalraja, S. Edelstein, A. Tepman, P. Ding, D. Ghosh
    and N. Maity (Applied Materials), *Alternate steps of IMP and
    sputtering process to improve sidewall coverage*, US 6,350,353 B2,
    filed 1999-11-24, granted 2002-02-26.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6350353>
[^pat-imp-coil-amat]: K. K.-T. Ngan (Applied Materials), *Avoiding
    contamination from induction coil in ionized sputtering*,
    US 5,707,498 A, filed 1996-07-12, granted 1998-01-13.
    <https://patents.google.com/patent/US5707498A/en>
[^pat-hcm-novellus]: K. F. Lai et al. (Novellus Systems), *Apparatus and
    method for controlling plasma uniformity across a substrate*, US
    6,179,973 B1, filed 1999-06-30, granted 2001-01-30.
    <https://patents.google.com/patent/US6179973B1/en>
[^novellus-pvd-2001]: Novellus Systems, *Metal PVD Solutions*, product
    page; Wayback Machine capture of 2001-12-14.
    <https://web.archive.org/web/20011214001648/http://www.novellus.com:80/products/pvd.asp>
[^berg-2005]: S. Berg and T. Nyberg, "Fundamental understanding and
    modeling of reactive sputtering processes", *Thin Solid Films*
    **476**(2), 215–230 (2005). <https://doi.org/10.1016/j.tsf.2004.10.051>
[^mao-2004]: D. Mao and J. Hopwood, "Ionized physical vapor deposition of
    titanium nitride: A deposition model", *Journal of Applied Physics*
    **96**(1), 820–828 (2004). <https://doi.org/10.1063/1.1753663>
[^taylor-1998]: D. S. Taylor, M. K. Jain and T. S. Cale, "Deposition rate
    dependence of step coverage of sputter deposited aluminum-(1.5%)
    copper films", *Journal of Vacuum Science & Technology A* **16**(5),
    3123–3126 (1998). <https://doi.org/10.1116/1.581476>
[^nishimura-1991]: H. Nishimura, T. Yamada and S. Ogawa, "Reliable
    submicron vias using aluminum alloy high temperature sputter
    filling", *Proc. Eighth International IEEE VLSI Multilevel
    Interconnection Conference (VMIC 1991)*, pp. 170–176.
    <https://doi.org/10.1109/VMIC.1991.152982>
[^dirks-1999]: A. G. Dirks, M. N. Webster, P. Turner, P. Rich and D. C.
    Butler, "On the mechanism of aluminum via fill by reflow and forcefill
    as studied by transmission electron microscopy", *Journal of Applied
    Physics* **85**(1), 571–577 (1999). <https://doi.org/10.1063/1.369491>
[^hariu-1989]: T. Hariu, K. Watanabe, M. Inoue, T. Takada and
    H. Tsuchikawa, "The Properties of Al-Cu/Ti Films Sputter Deposited at
    Elevated Temperatures and High DC Bias", *27th International
    Reliability Physics Symposium (IRPS 1989)*, pp. 210–214.
    <https://doi.org/10.1109/IRPS.1989.363388>
[^pramanik-1990]: D. Pramanik and V. Jain, "Effect of underlayer on
    sputtered aluminum grain structure and its correlation with step
    coverage in submicron vias", *Proc. Seventh International IEEE VLSI
    Multilevel Interconnection Conference (VMIC 1990)*, pp. 332–334.
    <https://doi.org/10.1109/VMIC.1990.127888>
[^amat-liner-barrier-2001]: Applied Materials, *Aluminum Liner/Barrier*,
    product page; Wayback Machine capture of 2001-08-07.
    <https://web.archive.org/web/20010807161527/http://www.appliedmaterials.com:80/products/liner_barrier.html>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^pat-tiw-hitachi]: A. Hiraki (Hitachi Metals), *Titanium-tungsten
    target material for sputtering and manufacturing method therefor*,
    US 5,160,534 A, filed 1991-05-31, granted 1992-11-03.
    <https://patents.google.com/patent/US5160534A/en>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^ann-16]: T. Edwards (Efabless), *Introduction to the SkyWater PDK —
    The New Age of Open Source Silicon*, lecture slides, 2021-10-08
    (UC San Diego BENG 207).
    <https://isn.ucsd.edu/courses/beng207/lectures/Tim_Edwards_2021_slides.pdf>
[^cyp-qtp-113005]: Cypress Semiconductor, *Product Qualification Plan,
    QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8
    Technology, CMI (Fab 4)*, document 001-85611 Rev. *A, January 2013
    (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^cyp-pin145273]: Cypress Semiconductor, *Product Information
    Notification PIN145273: Improvement of Cypress Minnesota
    Back-End-of-Line Integration for 130nm SONOS Product Families*,
    document 001-11741 Rev. *H, 2014-03-13 (copy hosted by Tokyo
    Electron Device).
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, section "MiM capacitors".
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^wiki-pvd]: Wikipedia, *Physical vapor deposition*.
    <https://en.wikipedia.org/wiki/Physical_vapor_deposition>
[^wiki-tin]: Wikipedia, *Titanium nitride*.
    <https://en.wikipedia.org/wiki/Titanium_nitride>
[^ohring-2002]: M. Ohring, *Materials Science of Thin Films*, 2nd ed.,
    Academic Press, 2002.
    <https://doi.org/10.1016/B978-0-12-524975-1.X5000-9>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^seshan-2002]: K. Seshan (ed.), *Handbook of Thin-Film Deposition
    Processes and Techniques: Principles, Methods, Equipment and
    Applications*, 2nd ed., Noyes Publications / William Andrew, 2002,
    ISBN 978-0-8155-1442-8. <https://openlibrary.org/isbn/9780815514428>
