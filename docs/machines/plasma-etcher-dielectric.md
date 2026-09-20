(machine-plasma-etcher-dielectric)=
# Plasma etcher: dielectric and nitride

A dielectric plasma etcher is the single-wafer dry-etch tool a fab uses
to cut holes and windows through silicon dioxide and silicon nitride:
contacts and vias, spacer and hard-mask etches, and the seal-ring and
pad openings at the top of the stack. It runs fluorocarbon chemistries
in which a thin polymer film on every surface decides what etches and
what does not, and in the 200 mm, 130 nm era it was most often a
capacitively coupled reactor — magnetically enhanced or dual-frequency
— rather than the inductive sources of silicon and metal etch. This
page describes the class in general, lists representative 200 mm-era
models, and then says what SkyWater has published about tools of this
class (nothing among its production etchers) and which SKY130 steps
this reference assigns to it. The physics and chemistry of plasma
etching are on the {ref}`category page <category-etch>`.

| | Plasma etcher: dielectric and nitride |
|---|---|
| What it does | Anisotropic etching of SiO₂ and Si₃N₄ in fluorocarbon plasmas, selective to the layer underneath; selective etching of "a SiO2 layer over a Si or Si3N4 underlayer" is "a process of vital importance to modern integrated circuit fabrication technology".[^schaepkens-1999] |
| Plasma source | Capacitive: Lam's Exelan uses "Dual Frequency Confined (DFC) technology";[^lam-exelan] Applied's MxP+ is a "MERIE chamber";[^regis-1997] Lam's Rainbow 45XX is a parallel-plate "plasma/RIE" etcher "mainly for Oxide Etch".[^allwin-rainbow-4500] High-density dielectric etchers were also sold, such as Applied's IPS Centura.[^amat-1997] |
| Chemistry | CF₄, CHF₃ or C₂F₆[^perry-2001] with Ar and O₂; the Rainbow 45XX runs "A contact oxide etch process with high selectivity to polysilicon (Ar/CF4/CHF3)";[^allwin-rainbow-4500] CH₃F/O₂ for nitride over-etch stopping on oxide.[^regis-1997] |
| Selectivity | Set by a steady-state fluorocarbon film: under 1.5 nm on oxide, about 1–4 nm on nitride and about 2–7 nm on silicon in Schaepkens et al.'s inductive plasmas;[^schaepkens-1999] SiO₂-to-Si selectivity of about 15 in CHF₃ against about 5 in CF₄ in Oehrlein et al.'s ECR study.[^oehrlein-1994b] |
| Endpoint | Optical emission; for nitride "a strong peak at 387 nm indicates that CN is present in the plasma";[^pat-endpoint-tel] contact layers need detection of films with "low exposure area (less than 3%)".[^wodecki-1999] |
| 200 mm era | Applied's MxP chambers from 1993, the eMxP+ (mid-1997) and IPS Centura (April 1997);[^amat-1997] Lam's Rainbow 4520[^wodecki-1999] and the "200 mm Alliance-based Exelan High Performance" of 2001.[^lam-exelan] |
| SkyWater-listed tool | None among the production etchers; the contact, via and nitride-seal etch pages weigh the three "Poly/Silicon Etch" tools instead, and a lab "Oxford PlasmaLab RIE deprocessing" tool is listed under "Physical Analysis"[^skw-01] |
| SKY130 steps | 12 steps, plus 1 where the class is an alternative; see {ref}`SKY130 steps assigned to this class <machine-plasma-etcher-dielectric-steps>` |

## What the machine class is and how it works

In a fluorocarbon plasma, oxide etches only where energetic ions strike
({ref}`category-etch`), and the carbon in the feed gas builds a polymer
that the ions must also clear.
Oehrlein et al. found an rf "threshold voltage for etching" of 55 V
for CHF₃ and 35 V for CF₄ at 1 mTorr, below which fluorocarbon film
deposition suppresses the etch.[^oehrlein-1994b] What makes a machine a
*dielectric* etcher is therefore a source that delivers a high ion
energy with a controlled fluorocarbon radical supply, stable wall
conditions, and endpoint detection sensitive enough for small open
areas. Donnelly and Kornblit review the field and its
reactors.[^donnelly-2013]

### Capacitive, magnetically enhanced and dual-frequency sources

The oldest single-wafer dielectric etchers are parallel-plate reactors.
Lam's Rainbow family has "top or/and bottom powered electrode plate,
programmable electrode spacing" and switches "between plasma and RIE
modes"; the 45XX series "is mainly for Oxide Etch", with recipes for
contacts, oxide spacers, etch-back planarisation and "A front-end
nitride etch with high selectivity to polysilicon".[^allwin-rainbow-4500]
Applied Materials raised the plasma density of a capacitive reactor
with a magnetic field: its patent, filed in 1988, describes "A magnetic field
enhanced single wafer plasma etch reactor" with "an
electrically-controlled stepped magnetic field for providing high rate
uniform etching at high pressures", a cooled cathode with a
"thermal conductivity-enhancing gas" between wafer and electrode, and
"in-situ self-cleaning capability".[^pat-merie-amat] Regis et al.
developed a nitride spacer etch "in the Dielectric Etch MxP+ MERIE
chamber" for "both 150 mm and 200 mm" chambers.[^regis-1997]

Dual-frequency reactors separate density from ion energy in a
capacitive geometry. Lam describes the Exelan family's "Dual Frequency
Confined (DFC) technology", in which "Confining the plasma … enables
damage-free processing, allows Clean Mode operation without chamber
wall contamination, and retains a consistent RF path inside the
chamber".[^lam-exelan] High-density sources were used for dielectrics too:
Applied launched the Dielectric Etch IPS Centura in April 1997 as its
"most advanced, high-density plasma system for etching dielectric
films".[^amat-1997] Perry et al. mapped such a regime in an inductive
C₂F₆ plasma, with ion energies of 50–160 eV, oxide etch rates of
0–150 Å/s and selectivity to resist of 1 to 6.[^perry-2001]

### Fluorocarbon films and selectivity

Selectivity in dielectric etching comes from the fluorocarbon film on
the surface. Standaert et al. observed "relatively thick (2–7 nm)
fluorocarbon layers" on silicon during steady-state etching and
modelled the etch as fluorine diffusing through the
layer.[^standaert-1998] Schaepkens et al. extended this to nitride:
oxide carries "a thin fluorocarbon film (<1.5 nm)", silicon about
2–7 nm and nitride "intermediate between the oxide and silicon cases",
about 1–4 nm, and "the substrate etch rate is inversely proportional to
the thickness of this fluorocarbon film"; the differences are "related
to a substrate-specific ability to consume carbon".[^schaepkens-1999]
In an ECR source, Oehrlein et al. found the silicon etch rate "much
lower in CHF₃ than in CF₄", giving SiO₂-to-Si selectivity of about 15
against 5, because the film on silicon was about 5.5 nm thick in CHF₃
and 2.5 nm in CF₄,[^oehrlein-1994b] and showed that the deposition in
high-density discharges "is primarily due to bombardment with low
energy ions".[^oehrlein-1994]

### Nitride etching

Nitride is etched in the same reactors. Regis et al.'s MxP+ spacer process used "A
CHF₃/Ar based main etch" at "800-1700 Å/min" with high selectivity to
silicon, then "A second, CH₃F/O₂ based process step … for overetch past
the endpoint to stop on oxide with minimal oxide loss (<50 Å)".[^regis-1997]
Goss and Thornburg describe the spacer etch as needing "high
selectivity … with a small isotropic component and no plasma
damage".[^goss-1997] Where CH₃F/O₂ spacer etches stop on silicon, Blanc
et al. attribute the high nitride-to-silicon selectivity to "a SiOxFy
passivation layer" and find that the oxidised layer behind the "silicon
recess" "is driven by the ion energy".[^blanc-2013] Downstream
(chemical) etching gives selectivity without ions: adding N₂ to CF₄/O₂
"increases the Si₃N₄ etch rate by a factor of 7, but leaves the SiO₂
etch rate unchanged",[^kastenmeier-1996] O₂ injection into NF₃
enhances the nitride rate,[^kastenmeier-1998] and a remote O₂/N₂
discharge with a little NF₃ reached nitride etch-rate ratios "to
polycrystalline silicon and SiO₂ … approximately 100 and 70".[^kastenmeier-1999]

### High-aspect-ratio holes

Contact and via holes etch more slowly as they deepen. Coburn and
Winters argued that "the conductance can be expected to limit the flow
of the reactive species to the bottom of the feature",[^coburn-1989]
and Gottscho, Jurgensen and Vitkavage distinguish this
"aspect ratio dependent etching (ARDE)" from microloading, narrowing its
causes to ion transport, neutral transport and surface
charging.[^gottscho-1992] The opposite can happen: in an inductive
reactor at 6–20 mTorr, Doemling et al. found "inverse RIE lag … i.e.,
the etch rates increase as the width of the microstructures
decrease".[^doemling-1996] Oehrlein et al. measured a depth loss of
about 10 % as 2.5 µm-deep contact holes narrowed from 1.3 to
0.6 µm.[^oehrlein-1994b] The same resist patterns shade the bottom of
a hole from electrons, which Hashimoto showed charges and damages
gate oxides beneath.[^hashimoto-1994]

### Endpoint on small open areas

Nitride clears with a CN emission signal: in a Tokyo Electron and
National Semiconductor patent, "a strong peak at 387 nm indicates that
CN is present in the plasma, usually indicating that nitride is being
etched", and a double endpoint stops the etch at both interfaces of a
TEOS/nitride/TEOS spacer.[^pat-endpoint-tel] Contact and via layers
expose so little of the wafer that the emission change is small;
Wodecki reports an add-on endpoint system on "a Lam Research
Corporation 200 mm Rainbow 4520 dielectric etch system" that "reliably
detected etch endpoints of low exposure area (less than 3%) dielectric
films".[^wodecki-1999]

## Representative 200 mm-era models

* **Applied Materials.** Dielectric etch on the Precision 5000 from
  1989–1990, the "HDP Dielectric Etch Centura" of 1993, MxP chambers
  from 1993, the eMxP+ in mid-1997 and the Dielectric Etch IPS Centura
  in April 1997;[^amat-1997] the 300 mm "Dielectric Etch eMax 300 and
  Dielectric Etch IPS 300" followed in 2000, for "critical self-aligned
  contacts and bi-level contacts, small-geometry via, spacer and
  hardmask etches".[^amat-300-etch-2000] A magnetic-field-enhanced
  single-wafer reactor is the subject of an Applied patent granted in
  1989.[^pat-merie-amat]
* **Lam Research.** The Rainbow 45XX parallel-plate oxide
  etchers[^allwin-rainbow-4500] including the 200 mm Rainbow
  4520;[^wodecki-1999] the Exelan, whose High Performance version of
  2001 is "200 mm Alliance-based" and "targets sub-130 nm
  geometries";[^lam-exelan] and the 2300 Exelan of 2000, which "brings
  the benefits of the dual frequency confined plasma technology into
  300 mm" for "copper damascene, low k, spacer, contact, via, and in situ
  hardmask open".[^lam-2300-2000]
* **Other vendors.** The step pages also name Tokyo Electron DRM and
  Unity dielectric etchers ({ref}`CTME <step-108>`,
  {ref}`NSME <step-166>`); no vendor description of those models was
  retrieved for this page.

## At SkyWater

### What SkyWater lists

SkyWater's *Facilities & Capabilities* page lists its production plasma
etchers under "Metal Etch" and "Poly/Silicon Etch" only; it names no
dielectric etcher.[^skw-01] Its "Poly/Silicon Etch" entries, quoted in
full on the {ref}`silicon and polysilicon etcher page
<machine-plasma-etcher-silicon>`, carry fluorine gases — "AMAT DPSII,
HBR, Cl2, NF3, CF4, CHF3, O2", "Lam 9400 TCP, poly/nitride, HBr, CF4,
SF6, O2" and "Lam 4400, HBr, Cl2, C2F6, CF4, SF6, O2" — and the 9400
entry names nitride.[^skw-01] Separately, under "Physical Analysis",
the page lists "Oxford PlasmaLab RIE deprocessing", which we read as a
failure-analysis tool rather than a production etcher.[^skw-01]

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>`
there is **no listing** for this class. The three poly/silicon etchers
are strong as SkyWater statements,[^skw-01] but their use for a
dielectric step is this reference's inference, graded on each step
page; the caveats that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`. The
list's silence does not show that no dielectric etcher exists: the S-1
counts "at least 522 well-maintained fab and sort tools" in
Bloomington,[^sec-01] far more than the capabilities page names.

(machine-plasma-etcher-dielectric-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a dielectric or
dielectric/nitride plasma etcher as the tool or one of two options
(identical to the {ref}`machines index <machines-index>` table):

{ref}`STINITE <step-005>`, {ref}`ONOME <step-042>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`LICM1E <step-094>`, {ref}`CTME <step-108>`, {ref}`VIME <step-119>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`, {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>`; *alternative:* {ref}`TUNARCE <step-036>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index. No
dielectric etcher is listed, so the pages weigh the three poly/silicon
etchers:

* **"AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2"** — *inference:* {ref}`STIE <step-006>`, {ref}`TUNARCE <step-036>`, {ref}`P1ME <step-062>`; *medium:* {ref}`STINITE <step-005>`, {ref}`ONOME <step-042>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`LI1ME <step-103>`, {ref}`PDME <step-169>`; *weak:* {ref}`LICM1E <step-094>`, {ref}`CTME <step-108>`, {ref}`VIME <step-119>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`, {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>`
* **"Lam 9400 TCP, poly/nitride, HBr, CF4, SF6, O2"** — *inference:* {ref}`STINITE <step-005>`, {ref}`STIE <step-006>`, {ref}`TUNARCE <step-036>`, {ref}`ONOME <step-042>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`PDME <step-169>`; *medium:* {ref}`P1ME <step-062>`; *weak:* {ref}`LICM1E <step-094>`, {ref}`CTME <step-108>`, {ref}`VIME <step-119>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`, {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>`
* **"Lam 4400, HBr, Cl2, C2F6, CF4, SF6, O2"** — *inference:* {ref}`STIE <step-006>`; *weak:* {ref}`STINITE <step-005>`, {ref}`ONOME <step-042>`, {ref}`P1ME <step-062>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`LICM1E <step-094>`, {ref}`CTME <step-108>`, {ref}`VIME <step-119>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`, {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>`

The grades split the class in two. On the nitride etches and the pad
etch the 9400 is inferred, because its entry is the only one that names
nitride, and the DPS II is medium for its CF₄ and CHF₃; on the oxide
contact, via and seal-ring etches all three are weak, since none is
listed for oxide.[^skw-01] The {ref}`PDME <step-169>` page also names
the two metal etchers as a weak option for removing a TiW cap.

## Consumables and facilities

The etch gases and process gases are described on the
{ref}`etch and chamber-clean gases <material-etch-gases>` and
{ref}`process gases <material-process-gases>` pages.
The etch gases and chamber parts are listed in the
{ref}`materials index <materials-index>`; what is specific to a
dielectric etcher is summarised here. None of the SkyWater sources
describes the fab's gas delivery or abatement. Chamber parts and exhaust
abatement are described on the
{ref}`hardware consumables and abatement <material-hardware-consumables>`
page.

* **Fluorocarbon gases.** CF₄, CHF₃ and C₂F₆, with Ar, O₂ and,
  for nitride over-etch, CH₃F;[^regis-1997][^allwin-rainbow-4500] CHF₃
  "is used in the semiconductor industry in plasma etching of silicon
  oxide and silicon nitride".[^wiki-chf3] Perfluorocarbons are potent
  greenhouse gases: C₂F₆ has "a global warming potential (GWP) of 9200",
  a figure Wikipedia's *Hexafluoroethane* article gives without naming an
  IPCC assessment;[^wiki-c2f6] the table of fifth-assessment values in
  its *Fluorocarbon* article gives 11,100.[^wiki-pfc]
* **Backside cooling.** Helium between wafer and chuck; the Rainbow
  45XX configuration includes a controller "for Helium Backside
  cooling",[^allwin-rainbow-4500] and Applied's MERIE patent a
  "thermal conductivity-enhancing gas" at the wafer.[^pat-merie-amat]
* **Chamber parts and cleans.** Fluorocarbon polymer coats the chamber,
  so parts are cleaned or replaced on schedule; Lam's confined plasma
  "allows Clean Mode operation without chamber wall
  contamination"[^lam-exelan] and Applied's patent provides "Protective
  coatings/layers of materials such as quartz" and in-situ
  self-cleaning.[^pat-merie-amat]
* **Monitor wafers.** Blanket oxide and nitride wafers for rate and
  selectivity, and patterned wafers for hole profile and bottom CD, as
  the contact and via pages describe ({ref}`CTME <step-108>`).

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's etch recipes are not public.

* **Two kinds of step.** The class covers nitride etches and oxide
  etches. The nitride etches stop on thin oxide ({ref}`SPE <step-077>`,
  the nitride of {ref}`ONOME <step-042>`), on polysilicon
  ({ref}`NPCME <step-079>`, which clears the nitride–oxide cap from the
  poly) or on silicon ({ref}`STINITE <step-005>`, which clears the
  nitride and the pad oxide ahead of the trench etch); the oxide etches
  stop on a conductor or on nitride ({ref}`LICM1E <step-094>`,
  {ref}`CTME <step-108>`, the four via etches, {ref}`NSME <step-166>`).
  The nitride etches rely on a CH₃F/O₂ over-etch or a fluorine-lean
  O₂/N₂ downstream chemistry, which can be selective over both oxide
  and silicon,[^regis-1997][^kastenmeier-1999] the oxide etches on the
  thicker fluorocarbon film that nitride and silicon carry.[^schaepkens-1999]
* **Spacer etch without a mask.** The {ref}`SPE <step-077>` page's
  etch-back must clear nitride from flat areas while leaving the
  spacer, and stop on the oxide over the extensions; the over-etch
  step and its oxide loss decide the margin.[^regis-1997][^goss-1997]
* **Contacts and vias.** The contact and via pages describe polymerising
  oxide etches in small holes, where aspect-ratio effects and weak
  endpoint signals set the over-etch.[^gottscho-1992][^wodecki-1999] The
  {ref}`CTME <step-108>` page adds a nitride breakthrough at the hole
  floor, on its reading of the stack.
* **Deep windows over a finished back end.** The seal-ring and pad
  openings ({ref}`NSME <step-166>`, {ref}`PDME <step-169>`) etch through
  thick passivation with a small open area; the NSME page infers a timed
  etch, and both pages use a solvent clean that spares the aluminium.
* **No listed tool.** Because SkyWater lists no dielectric etcher,
  every assignment in this class rests on a tool listed as a
  poly/silicon etcher, and the step pages record which tool runs the contact and via etches as an open
  question.[^skw-01]
* **Strip and clean afterwards.** The fluorocarbon polymer left on hole
  walls is removed by an ash and a solvent or wet clean; the
  {ref}`CTME <step-108>` page names the listed ashers and the "EKS265,
  EKC270 solvents" tool.[^skw-01]

## Related pages

* {ref}`category-etch` — plasma and wet etching physics and the 27
  etch steps of SKY130.
* {ref}`machine-plasma-etcher-silicon` — the three listed poly/silicon
  etchers that the step pages weigh for dielectric steps.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — fluorocarbon gases and chamber materials.
* {ref}`category-deposition` — the oxide and nitride films these etches
  pattern.
* {ref}`material-hardware-consumables` — chamber parts and exhaust
  abatement.
* {ref}`material-etch-gases` — fluorocarbon, fluoride, chlorine and
  bromine etch and chamber-clean gases.
* {ref}`material-process-gases` — nitrogen, oxygen, hydrogen, argon,
  helium and the oxidation additives, their grades and SkyWater's listed
  gases.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

* {ref}`Magnetic field-enhanced plasma etch reactor <patent-gp22680079>` — US 4,842,683 A (1986)
* {ref}`Method of forming a semiconductor device using double endpoint detection <patent-gp25360011>` — US 6,376,262 B1 (2001)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the etch groups
  (no dielectric etcher), the three poly/silicon entries and the
  physical-analysis RIE tool.[^skw-01]
* SkyWater Technology, Form S-1 (2021) — the fab and sort tool count,
  larger than the list of named tools.[^sec-01]
* Applied Materials, 1997 annual report (Form 10-K) — dates of the
  Precision 5000, HDP, MxP, eMxP+ and IPS dielectric etchers.[^amat-1997]
* Applied Materials, 300 mm etch product line press release (2000) —
  the eMax and IPS dielectric etchers and their
  applications.[^amat-300-etch-2000]
* Lam Research, Exelan High Performance press release (2001) — the
  200 mm Exelan and its dual-frequency confined source.[^lam-exelan]
* Lam Research, 2300 Etch Series press release (2000) — the 2300 Exelan
  and its applications.[^lam-2300-2000]
* Allwin21, *Lam Rainbow 45XX Plasma Etcher* — the parallel-plate oxide
  etcher and its contact, spacer and nitride
  recipes.[^allwin-rainbow-4500]
* Cheng et al. (Applied Materials), US 4,842,683 — the
  magnetic-field-enhanced single-wafer etch reactor.[^pat-merie-amat]
* Tokyo Electron and National Semiconductor, US 6,376,262 — the 387 nm
  CN emission line as the nitride endpoint.[^pat-endpoint-tel]

### High-level understanding

* Wikipedia, *Reactive-ion etching* — the capacitive reactor and its
  self-bias.[^wiki-rie]
* Wikipedia, *Fluoroform* and *Hexafluoroethane* — two fluorocarbon
  etch gases and their greenhouse impact.[^wiki-chf3][^wiki-c2f6]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — ch. 10 on
  etching.[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 — dry
  etching of oxide and nitride.[^txt-02]
* Lieberman and Lichtenberg, *Principles of Plasma Discharges and
  Materials Processing* — capacitive, magnetically enhanced and
  inductive sources.[^lieberman-2005]

### Deep dive

* Donnelly and Kornblit, *JVST A* 2013 — a review of plasma etching,
  including silicon dioxide.[^donnelly-2013]
* Oehrlein et al., *JVST A* 1994 (I) — fluorocarbon film deposition in
  CF₄ and CHF₃ high-density plasmas.[^oehrlein-1994]
* Oehrlein et al., *JVST A* 1994 (II) — thresholds, film thickness and
  SiO₂-to-Si selectivity in CF₄ and CHF₃.[^oehrlein-1994b]
* Standaert et al., *JVST A* 1998 — etching through a steady-state
  fluorocarbon layer.[^standaert-1998]
* Schaepkens et al., *JVST A* 1999 — the SiO₂-to-Si₃N₄ selectivity
  mechanism.[^schaepkens-1999]
* Perry et al., *JVST A* 2001 — oxide etch rates, resist selectivity and
  radical densities in an inductive C₂F₆ plasma.[^perry-2001]
* Coburn and Winters, *APL* 1989 — conductance limits in
  high-aspect-ratio features.[^coburn-1989]
* Gottscho, Jurgensen and Vitkavage, *JVST B* 1992 — ARDE and
  microloading.[^gottscho-1992]
* Doemling, Rueger and Oehrlein, *APL* 1996 — inverse RIE lag in oxide
  etching.[^doemling-1996]
* Regis et al., ASMC 1997 — a nitride spacer etch in an MxP+ MERIE
  chamber.[^regis-1997]
* Goss and Thornburg, ASMC 1997 — nitride spacer processing for
  0.35 µm CMOS.[^goss-1997]
* Blanc et al., *JVST B* 2013 — silicon recess in CH₃F/O₂/He spacer
  etching.[^blanc-2013]
* Kastenmeier et al., *JVST A* 1996 — downstream CF₄/O₂/N₂ etching of
  nitride and oxide.[^kastenmeier-1996]
* Kastenmeier et al., *JVST A* 1998 — remote NF₃/O₂ etching of nitride
  and oxide.[^kastenmeier-1998]
* Kastenmeier, Matsuo and Oehrlein, *JVST A* 1999 — highly selective
  nitride removal over silicon and oxide.[^kastenmeier-1999]
* Lee and Chen, *JAP* 1983 — chemical and ion-enhanced components of
  CF₄/O₂ reactive ion etching.[^lee-chen-1983]
* Wodecki, *Proc. SPIE* 1999 — endpoint on low-open-area dielectric
  etches in a Rainbow 4520.[^wodecki-1999]
* Hashimoto, *JJAP* 1994 — electron-shading charge damage through
  high-aspect-ratio openings.[^hashimoto-1994]

## Open questions

* Whether SkyWater runs its contact, via, seal-ring and pad etches on
  the listed poly/silicon etchers or on a dielectric etcher it does not
  list is not public.[^skw-01]
* Which of the three poly/silicon etchers carries the nitride etches is
  not stated; the step pages infer the Lam 9400 TCP from the word
  "nitride".
* The model list above is incomplete: it covers the Applied Materials and
  Lam dielectric etchers for which a public description was found, not
  the Tokyo Electron and other dielectric etchers of the period.

<!-- footnotes -->

[^schaepkens-1999]: M. Schaepkens, T. E. F. M. Standaert, N. R. Rueger,
    P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "Study of the
    SiO₂-to-Si₃N₄ etch selectivity mechanism in inductively coupled
    fluorocarbon plasmas and a comparison with the SiO₂-to-Si
    mechanism", *Journal of Vacuum Science & Technology A* **17**(1),
    26–37 (1999). <https://doi.org/10.1116/1.582108>
[^lam-exelan]: Lam Research, *Lam Research Corporation Advances
    Dielectric Etch Capabilities With Launch Of Exelan High
    Performance*, press release, 2001-07-09.
    <https://newsroom.lamresearch.com/2001-07-09-Lam-Research-Corporation-Advances-Dielectric-Etch-Capabilities-With-Launch-Of-Exelan-R-High-Performance>
[^regis-1997]: J. M. Regis, A. M. Joshi, T. Lill and M. Yu, "Reactive
    ion etch of silicon nitride spacer with high selectivity to oxide",
    *1997 IEEE/SEMI Advanced Semiconductor Manufacturing Conference and
    Workshop (ASMC 97) Proceedings*, pp. 252–256.
    <https://doi.org/10.1109/ASMC.1997.630744>
[^allwin-rainbow-4500]: Allwin21, *Lam Rainbow 45XX Plasma Etcher*
    (reseller product description), accessed 2026-09-13.
    <https://allwin21.com/lam-rainbow-45xx-plasma-etcher/>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report* (Form 10-K
    for the fiscal year ended 1997-10-26).
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^oehrlein-1994b]: G. S. Oehrlein, Y. Zhang, D. Vender and O. Joubert,
    "Fluorocarbon high-density plasmas. II. Silicon dioxide and silicon
    etching using CF₄ and CHF₃", *Journal of Vacuum Science & Technology
    A* **12**(2), 333–344 (1994). <https://doi.org/10.1116/1.578877>
[^pat-endpoint-tel]: D. K. Kempa and S. Hyland (Tokyo Electron and
    National Semiconductor), *Method of forming a semiconductor device
    using double endpoint detection*, US 6,376,262 B1, granted
    2002-04-23. <https://patents.google.com/patent/US6376262B1/en>
[^wodecki-1999]: N. D. Wodecki, "Low open area multilayered dielectric
    film etch endpoint detection using EndPoint Plus", *Proc. SPIE*
    **3882**, Process, Equipment, and Materials Control in Integrated
    Circuit Manufacturing V, 231 (1999).
    <https://doi.org/10.1117/12.361313>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; etch and physical-analysis entries re-checked
    2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^donnelly-2013]: V. M. Donnelly and A. Kornblit, "Plasma etching:
    Yesterday, today, and tomorrow", *Journal of Vacuum Science &
    Technology A* **31**(5), 050825 (2013).
    <https://doi.org/10.1116/1.4819316>
[^pat-merie-amat]: D. Cheng, V. J. Zeitlin, D. L. Andrews, M. Chang, D.
    Maydan, S. Somekh, K. R. Stalder, D. N. Wang, J. M. White and J. Y.
    K. Wong (Applied Materials), *Magnetic field-enhanced plasma etch
    reactor*, US 4,842,683 A, granted 1989-06-27.
    <https://patents.google.com/patent/US4842683A/en>
[^perry-2001]: W. L. Perry, K. Waters, M. Barela and H. M. Anderson,
    "Oxide etch behavior in a high-density, low-pressure, inductively
    coupled C₂F₆ plasma: Etch rates, selectivity to photoresist, plasma
    parameters, and CFx radical densities", *Journal of Vacuum Science &
    Technology A* **19**(5), 2272–2281 (2001).
    <https://doi.org/10.1116/1.1382874>
[^standaert-1998]: T. E. F. M. Standaert, M. Schaepkens, N. R. Rueger,
    P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "High density
    fluorocarbon etching of silicon in an inductively coupled plasma:
    Mechanism of etching through a thick steady state fluorocarbon
    layer", *Journal of Vacuum Science & Technology A* **16**(1),
    239–249 (1998). <https://doi.org/10.1116/1.580978>
[^oehrlein-1994]: G. S. Oehrlein, Y. Zhang, D. Vender and M. Haverlag,
    "Fluorocarbon high-density plasmas. I. Fluorocarbon film deposition
    and etching using CF₄ and CHF₃", *Journal of Vacuum Science &
    Technology A* **12**(2), 323–332 (1994).
    <https://doi.org/10.1116/1.578876>
[^goss-1997]: M. Goss and R. Thornburg, "The challenges of nitride
    spacer processing for a 0.35 μm CMOS technology", *1997 IEEE/SEMI
    Advanced Semiconductor Manufacturing Conference and Workshop (ASMC
    97) Proceedings*, pp. 228–233.
    <https://doi.org/10.1109/ASMC.1997.630740>
[^blanc-2013]: R. Blanc, F. Leverd, T. David and O. Joubert, "Patterning
    of silicon nitride for CMOS gate spacer technology. I. Mechanisms
    involved in the silicon consumption in CH₃F/O₂/He high density
    plasmas", *Journal of Vacuum Science & Technology B* **31**(5),
    051801 (2013). <https://doi.org/10.1116/1.4816466>
[^kastenmeier-1996]: B. E. E. Kastenmeier, P. J. Matsuo, J. J. Beulens
    and G. S. Oehrlein, "Chemical dry etching of silicon nitride and
    silicon dioxide using CF₄/O₂/N₂ gas mixtures", *Journal of Vacuum
    Science & Technology A* **14**(5), 2802–2813 (1996).
    <https://doi.org/10.1116/1.580203>
[^kastenmeier-1998]: B. E. E. Kastenmeier, P. J. Matsuo, G. S. Oehrlein
    and J. G. Langan, "Remote plasma etching of silicon nitride and
    silicon dioxide using NF₃/O₂ gas mixtures", *Journal of Vacuum
    Science & Technology A* **16**(4), 2047–2056 (1998).
    <https://doi.org/10.1116/1.581309>
[^kastenmeier-1999]: B. E. E. Kastenmeier, P. J. Matsuo and G. S.
    Oehrlein, "Highly selective etching of silicon nitride over silicon
    and silicon dioxide", *Journal of Vacuum Science & Technology A*
    **17**(6), 3179–3184 (1999). <https://doi.org/10.1116/1.582097>
[^coburn-1989]: J. W. Coburn and H. F. Winters, "Conductance
    considerations in the reactive ion etching of high aspect ratio
    features", *Applied Physics Letters* **55**(26), 2730–2732 (1989).
    <https://doi.org/10.1063/1.101937>
[^gottscho-1992]: R. A. Gottscho, C. W. Jurgensen and D. J. Vitkavage,
    "Microscopic uniformity in plasma etching", *Journal of Vacuum
    Science & Technology B* **10**(5), 2133–2147 (1992).
    <https://doi.org/10.1116/1.586180>
[^doemling-1996]: M. F. Doemling, N. R. Rueger and G. S. Oehrlein,
    "Observation of inverse reactive ion etching lag for silicon dioxide
    etching in inductively coupled plasmas", *Applied Physics Letters*
    **68**(1), 10–12 (1996). <https://doi.org/10.1063/1.116772>
[^hashimoto-1994]: K. Hashimoto, "Charge Damage Caused by Electron
    Shading Effect", *Japanese Journal of Applied Physics* **33**(10R),
    6013 (1994). <https://doi.org/10.1143/JJAP.33.6013>
[^amat-300-etch-2000]: Applied Materials, *Applied Materials Unveils
    300mm Etch Product Line*, press release, 2000-07-10.
    <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-unveils-300mm-etch-product-line>
[^lam-2300-2000]: Lam Research, *Lam Research Corporation Launches
    Industry's First 200- And 300-Mm Capable Etch Product Line*, press
    release, 2000-11-16.
    <https://newsroom.lamresearch.com/2000-11-16-Lam-Research-Corporation-Launches-Industrys-First-200-And-300-Mm-Capable-Etch-Product-Line>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-chf3]: Wikipedia, *Fluoroform*.
    <https://en.wikipedia.org/wiki/Fluoroform>
[^wiki-c2f6]: Wikipedia, *Hexafluoroethane*.
    <https://en.wikipedia.org/wiki/Hexafluoroethane>
[^wiki-pfc]: Wikipedia, *Fluorocarbon*.
    <https://en.wikipedia.org/wiki/Fluorocarbon>
[^lee-chen-1983]: Y. H. Lee and M.-M. Chen, "Silicon etching mechanism
    and anisotropy in CF₄+O₂ plasma", *Journal of Applied Physics*
    **54**(10), 5966–5973 (1983). <https://doi.org/10.1063/1.331774>
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^lieberman-2005]: M. A. Lieberman and A. J. Lichtenberg, *Principles of
    Plasma Discharges and Materials Processing*, 2nd ed., Wiley, 2005,
    ISBN 978-0-471-72001-0. <https://doi.org/10.1002/0471724254>
