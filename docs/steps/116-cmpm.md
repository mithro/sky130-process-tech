(step-116)=
# Step 116 — CMPM: CMP over metal1

| | |
|---|---|
| **Step number** | 116 of 171[^steps-sheet] |
| **Step code** | `CMPM` |
| **Category** | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| **Phase** | {term}`BEOL` — contact and metal 1 |
| **Previous step** | {ref}`NILD3 <step-115>` |
| **Next step** | {ref}`NCAPOX3 <step-117>` |

## What this step is

`CMPM` polishes the inter-level dielectric ({term}`ILD`) flat. The
{ref}`NILD3 <step-115>` oxide arrives following the metal-1
topography — thick over wide lines and dense arrays, thinner over
open field, with the 0.36 µm[^pdk-04] step of the metal reproduced,
softened, at its surface. The wafer is pressed against a pad flooded
with alkaline silica slurry (industry-standard for ILD; SKY130's is
not public) until that topography is gone and a planar oxide surface
remains at a controlled height above the tops of the metal-1 lines.
No material change marks the end: it is an
*oxide-on-oxide* polish stopped by removal amount, not by a stop
layer. The cap of {ref}`NCAPOX3 <step-117>` then restores a fixed
thickness before the via-1 mask ({ref}`VIM <step-118>`) is printed on
it. The finished dielectric above metal 1 is, per the PDK's stack
diagram, the 0.27 µm via-1 height.[^pdk-04]

"CMP over metal1" is the first of the *inter-metal* oxide polishes —
the first above a wiring level; the oxide polishes below it are
{ref}`CMPP <step-090>` and {ref}`CMPL <step-106>`. The same operation
recurs as {ref}`CMPM2 <step-127>`,
{ref}`CMPM3 <step-142>` and {ref}`CMPM4 <step-157>` above each metal
level. SkyWater lists "AMAT Mirra CMP" with "oxide" first among its
applications.[^skw-01] The PDK's design rules are written around
this polish: metal 1 carries a "Min MM1_oxide_Pattern_density" of
0.7 (m1.pd.1) checked in square windows, and a fill algorithm that
flags any 700 µm × 700 µm window covered by `cmm1 waffleDrop` whose
metal density falls below stated levels;[^pdk-periph] the assumptions
table gives an "Oxide Bias for MM1" of 0.6, a "Min pattern density
for oxide" of 0.75, a "Min MM* PD range" of 0.3 and 700 µm and
2 000 µm pattern-density extraction boxes.[^pdk-03]

## Step category

`CMPM` is a {ref}`Chemical-mechanical planarisation <category-cmp>`
step of the *inter-level dielectric* type — the category page's
third row: {term}`PECVD`/HDP oxide, no stop layer, silica slurry at pH
10–11, with thickness non-uniformity, scratches and pattern-density
steps as the failure modes. It is the class of polish IBM invented
{term}`CMP` for — coplanar metal/insulator films[^pat-cmp-ibm-1990] — and
the one whose pattern dependence Stine, Ouma, Boning and their
co-workers turned into the density-based fill rules that every
modern design-rule deck, this PDK's included, now
carries.[^stine-1998][^ouma-2002][^stine-1998-ted] It differs from
the tungsten polish of {ref}`WCMP2 <step-111>` in that nothing tells
the tool to stop, and from the {term}`STI` polish of
{ref}`CMPNIT <step-012>` in that there is no nitride beneath. Because
only one material is removed there is no {term}`dishing` or
{term}`erosion` in the two-material sense of the tungsten polish; the
analogue here is the pattern-density-dependent thinning that leaves a
step in the oxide surface between dense and sparse metal.

## Why this step exists

A subtractive aluminium back end without planarisation accumulates
topography with every level; by metal 2 the steps would exceed the
depth of focus of a 248 nm exposure and the {term}`via` etch would have to
reach metal 1 through wildly different oxide thicknesses. The polish
fixes:

* **Planarity for lithography.** The {ref}`VIM <step-118>` and
  {ref}`MM2 <step-124>` exposures need a surface flat to within
  their depth of focus across the field — a few hundred nanometres
  for a 248 nm scanner[^wiki-litho] printing the PDK's 0.14 µm
  metal and 0.15 µm via {term}`CDs <CD>`[^pdk-03] ({ref}`category-lithography`
  sets out the trade-off). Sivaram et al. modelled the
  removal rate and planarity of interlevel-dielectric CMP,[^sivaram-1992]
  and Boning et al. introduced the statistical metrology of ILD
  thickness variation that quantifies what the polish
  achieves.[^boning-1994][^chang-1995]
* **A uniform via depth.** The via-1 etch of {ref}`VIME <step-119>`
  must clear 0.27 µm of oxide[^pdk-04] over every via while not
  over-etching the metal-1 cap where the oxide is thinner
  ({ref}`overview-metal-cap`); the
  post-polish thickness range over metal 1 is the via etch's
  {term}`over-etch` budget.
* **Pattern-density control.** The polish rate depends on local
  density: oxide over an isolated line is removed faster than oxide
  over a dense array, so the surface after polishing follows the
  metal density on a scale set by the pad's {term}`planarisation length`
  (Ouma et al.[^ouma-2002]). Stine et al. showed how metal-fill
  patterning practices reduce the effect and what they cost in
  capacitance;[^stine-1998-ted] the PDK's `cmm1` waffle-drop fill,
  its 0.7 minimum oxide density and its 700 µm windows[^pdk-periph]
  are that practice in SKY130's rules, and the 2 000 µm box of the
  assumptions table[^pdk-03] is, on our reading, the planarisation
  length the rules were fitted against.
* **Capacitance.** The remaining oxide thickness over metal 1 sets
  the metal-1-to-metal-2 capacitance in the PDK's extraction
  tables;[^pdk-08] Stine et al.'s electrical analysis of fill
  patterns shows how fill and thickness trade.[^stine-1998-ted]

Without `CMPM` the later levels of SKY130 could not be printed or
etched reliably, and the via-1 chain would be open in some places and
shorted in others.

## How it is typically performed

An industry-generic ILD polish for a 200 mm, 130 nm-era fab (SKY130's
recipe is not public):

1. **Tool.** A multi-platen rotary polisher[^pat-cmp-mirra] with a
   stacked pad (hard top layer for planarisation over a soft
   sub-pad), a multi-zone carrier head and diamond conditioning;
   optical thickness {term}`endpoint` through a pad window is available on
   this class of tool.[^pat-cmp-window][^pat-cmp-endpoint-ibm]
2. **Slurry.** Fumed or colloidal silica in KOH or NH₄OH at pH
   10–11 (industry-typical values[^steigerwald-1997][^zantye-2004]);
   Cook's mechanism — hydration of the glass surface and removal of
   the softened layer by the abrasive — is what makes oxide
   polishing chemical as well as mechanical,[^cook-1990] and
   Krishnan, Nalaskowski and Cook review the slurry
   chemistry.[^rev-02]
3. **Recipe.** Removal follows Preston's law, rate proportional to
   pressure and velocity,[^preston-1927][^zantye-2004] modified by the pad's
   fluid-film and contact mechanics.[^runnels-1994] Down-force of a
   few psi and platen speeds of tens of rpm are typical.[^txt-05]
   The first platen removes the bulk and planarises; a second, at
   lower pressure, trims to the target thickness; a buff platen
   removes slurry residue. The target is the remaining oxide over
   the metal-1 top plus an allowance for the cap of
   {ref}`NCAPOX3 <step-117>`, so that the sum reaches the 0.27 µm of
   the PDK.[^pdk-04]
4. **Endpoint.** By removal time calibrated on monitors, or by
   in-situ optical thickness measurement;[^pat-cmp-window] the polish
   must stop *above* the metal — breaking through to the cap
   would scratch and thin the lines — so a generous margin is
   left and the {term}`cap oxide` makes up the thickness.
5. **Post-CMP clean.** Double-sided brush scrub with dilute NH₄OH
   (Philipossian and Sun analyse the brush design for post-ILD-CMP
   scrubbing[^philipossian-2009]), sometimes a dilute HF dip, then
   spin-rinse-dry; Devriendt et al. relate oxide-CMP defects to the
   cleaning strategy,[^devriendt-1998] and Sun, Han and Keswani review
   brush scrubbing.[^sun-2017]
6. **Metrology.** Remaining oxide thickness over metal-1 test pads
   by reflectometry or ellipsometry at many sites; die-level
   thickness maps on density test structures (the method of
   Stine et al.[^stine-1998]); scratch and particle inspection on the
   KLA AIT class (our reading of "AIT" in SkyWater's job posting);[^job-06] via-chain
   resistance later at {term}`e-test`.

## Machines typically used

* **{ref}`Rotary multi-platen CMP polisher <machine-cmp-polisher>`**, 200 mm: Applied Materials
  Mirra,[^pat-cmp-mirra][^chiphistory-mirra] Ebara EPO/F-REX,[^ebara-frex]
  SpeedFam-IPEC, Strasbaugh ({ref}`category-cmp`).
* **{ref}`Post-CMP brush scrubber <machine-post-cmp-cleaner>`** (OnTrak/Lam Synergy, SEZ/Lam Da Vinci).
* **{ref}`Thin-film thickness metrology <machine-film-thickness-metrology>`** (reflectometer, ellipsometer),
  **{ref}`patterned-wafer inspection <machine-defect-inspection>`**.

## Machines likely used at SkyWater

* **Applied Materials Mirra CMP.** SkyWater lists "AMAT Mirra CMP"
  with "oxide" among its applications.[^skw-01] Strength: **strong**
  for the tool and its oxide polish (SkyWater statement); assignment to
  this step is an **inference** from the film, since the list names no
  steps.
* **Post-CMP clean — SEZ 223 / Da Vinci** single-wafer tools, and the
  Mirra entry also lists "Track ammonia clean" and "IPA clean";[^skw-01]
  a "SEZ etcher tool" on the maintenance page.[^skw-07] A brush
  scrubber is not named (open question).
* **Defect inspection — KLA AIT / SP1**, our reading of "AIT" and "SP1"
  in a SkyWater job posting's "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
  Strength: medium.

## Resources required

* **{ref}`Silica-based oxide CMP slurry <material-cmp-consumables>`** (KOH- or NH₄OH-stabilised
  fumed or colloidal silica).[^rev-02][^wiki-cmp]
* **Polishing pads** (stacked polyurethane, IC1000/Suba IV class;
  category page) and **diamond
  conditioners**.[^wiki-cmp]
* **{ref}`DI water <material-ultrapure-water>`**, **dilute NH₄OH** (category page), possibly **dilute
  HF**, for the {term}`post-CMP clean`; **PVA brushes**.
* **Carrier-head consumables** — membranes, retaining rings.
* **Slurry supply and {ref}`waste treatment <material-hardware-consumables>`**.[^txt-07]

## Related steps and cross-references

* Previous: {ref}`NILD3 <step-115>` (the film). Next:
  {ref}`NCAPOX3 <step-117>` (the cap), then {ref}`VIM <step-118>`.
* The topography it removes: {ref}`MM1E <step-114>`; the fill rules
  it imposes: {ref}`MM1 <step-113>`.
* The via etch that depends on its thickness control:
  {ref}`VIME <step-119>`.
* The same polish at higher levels: {ref}`CMPM2 <step-127>`,
  {ref}`CMPM3 <step-142>`, {ref}`CMPM4 <step-157>`; the earlier
  oxide polishes: {ref}`CMPP <step-090>`, {ref}`CMPL <step-106>`; the
  tungsten polish before it: {ref}`WCMP2 <step-111>`.
* Category page: {ref}`Chemical-mechanical planarisation <category-cmp>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Method for producing coplanar multi-level metal/insulator films on a substrate and for forming patterned conductive lines simultaneously with stud vias <patent-gp25155097>` — US 4,789,648 A (1985)
* {ref}`Chem-mech polishing method for producing coplanar metal/insulator films on a substrate <patent-gp25155001>` — US 4,944,836 A (1985)
* {ref}`In-situ endpoint detection and process monitoring method and apparatus for chemical-mechanical polishing <patent-gp22631367>` — US 5,433,651 A (1993)
* {ref}`Forming a transparent window in a polishing pad for a chemical mechanical polishing apparatus <patent-gp24770421>` — US 5,893,796 A (1995)
* {ref}`Continuous processing system for chemical mechanical polishing <patent-gp24192580>` — US 5,738,574 A (1995)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — "AMAT Mirra CMP – oxide";
  SEZ 223 / Da Vinci.[^skw-01]
* [SkyWater, *A Day in the Life of a SkyWater Maintenance Technician*](<https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>) —
  "a SEZ etcher tool".[^skw-07]
* [LinkedIn, SkyWater *Defect Technician 2* posting](<https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>) — inspection
  tools.[^job-06]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — m1.pd.1 (0.7), the `cmm1`
  waffle-drop density check in 700 µm windows.[^pdk-periph]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — "Oxide Bias for MM1" 0.6;
  "Min pattern density for oxide" 0.75; "Min MM* PD range" 0.3;
  700 µm and 2 000 µm extraction boxes.[^pdk-03]
* [SkyWater PDK, *Process stack diagram*](<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>) — `met1` 0.36 µm; via1
  0.27 µm.[^pdk-04]
* [SkyWater PDK, *Parasitic Layout Extraction*](<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>) — the capacitance
  tables.[^pdk-08]

### High-level understanding

* Wikipedia, [*Chemical-mechanical polishing*](<https://en.wikipedia.org/wiki/Chemical-mechanical_polishing>); [*Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) —
  the depth-of-focus relation.[^wiki-cmp][^wiki-litho]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) — ILD CMP.[^txt-05]
* [Quirk and Serda, *Semiconductor Manufacturing Technology*](<https://openlibrary.org/isbn/9780130815200>) — CMP
  tools and consumables.[^txt-07]
* [Chip History Center, *The Mirra CMP System*](<https://www.chiphistory.org/142-applied-materials-the-mirra-cmp-system>).[^chiphistory-mirra]
* [Moon, in *Advances in Chemical Mechanical Planarization*](<https://doi.org/10.1016/B978-0-08-100165-3.00001-2>) — the
  chemical and physical mechanisms of dielectric CMP.[^moon-2016]

### Deep dive

* [Stine et al., *IEEE Trans. Semicond. Manuf.* 1998](<https://doi.org/10.1109/66.661292>) — rapid
  characterisation of pattern-dependent CMP variation.[^stine-1998]
* [Stine et al., *IEEE TED* 1998](<https://doi.org/10.1109/16.661228>) — the physical and electrical effects
  of metal-fill patterning for oxide CMP.[^stine-1998-ted]
* [Ouma et al., *IEEE Trans. Semicond. Manuf.* 2002](<https://doi.org/10.1109/66.999598>) — planarisation
  length and pattern density in oxide CMP.[^ouma-2002]
* Boning et al., SPIE 1994, and Chang et al., IEDM 1995 —
  statistical metrology of ILD thickness variation.[^boning-1994][^chang-1995]
* [Sivaram et al. (SEMATECH), MRS 1992](<https://doi.org/10.1557/PROC-260-53>) — removal-rate and planarity
  models for ILD CMP.[^sivaram-1992]
* [Cook, *J. Non-Cryst. Solids* 1990](<https://doi.org/10.1016/0022-3093(90)90200-6>) — the chemistry of glass
  polishing.[^cook-1990]
* Preston, 1927, and Runnels and Eyman, *J. Electrochem. Soc.* 1994
  — the removal-rate law and the tribology of the wafer–pad
  contact.[^preston-1927][^runnels-1994]
* [Krishnan, Nalaskowski and Cook, *Chem. Rev.* 2010](<https://doi.org/10.1021/cr900170z>) — slurry
  chemistry.[^rev-02]
* [Devriendt et al. (IMEC), *Solid State Phenomena* 1998](<https://doi.org/10.4028/www.scientific.net/SSP.65-66.173>) — oxide-CMP
  defects versus post-CMP cleaning.[^devriendt-1998]
* [Philipossian and Sun, *Electrochem. Solid-State Lett.* 2009](<https://doi.org/10.1149/1.3058994>) — brush
  design for post-ILD-CMP scrubbing.[^philipossian-2009]
* [Sun, Han and Keswani, 2017](<https://doi.org/10.1016/B978-0-323-43157-6.00004-5>) — brush scrubbing reviewed.[^sun-2017]
* Steigerwald, Murarka and Gutmann; Oliver (ed.); Zantye, Kumar and
  Sikder — the CMP texts and review.[^steigerwald-1997][^oliver-2004][^zantye-2004]
* Chow et al. (IBM), US 4,789,648, and Beyer et al. (IBM),
  US 4,944,836 — the coplanar metal/insulator CMP patents.[^pat-cmp-ibm-1988][^pat-cmp-ibm-1990]
* Tolles et al. and Birang et al. (Applied Materials), US 5,738,574
  and US 5,893,796; Lustig et al. (IBM), US 5,433,651 — the Mirra
  platform and in-situ endpoint.[^pat-cmp-mirra][^pat-cmp-window][^pat-cmp-endpoint-ibm]

## Open questions

* The slurry, pad, removal amount, target oxide thickness over
  metal 1 and the endpoint method of `CMPM` are not public.
* How the 0.27 µm via-1 height of the PDK[^pdk-04] is split between
  the polished NILD3 and the {ref}`NCAPOX3 <step-117>` cap is not
  public.
* Whether the 2 000 µm extraction box of the assumptions
  table[^pdk-03] corresponds to the polish's planarisation length is
  an inference.
* The post-CMP cleaning tool is not identified beyond the
  SEZ/Da Vinci single-wafer tools.[^skw-01]

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance and capacitance tables), SkyWater SKY130 PDK
    documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^skw-07]: SkyWater Technology, *A Day in the Life of a SkyWater
    Maintenance Technician*, 2023-12-14.
    <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
[^job-06]: LinkedIn, *SkyWater Technology hiring Defect Technician 2 in
    Bloomington, MN* (job posting), retrieved 2026-09-19.
    <https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>
[^pat-cmp-mirra]: R. D. Tolles, N. Shendon, S. Somekh, I. Perlov,
    E. Gantvarg and H. Q. Lee (Applied Materials), *Continuous
    processing system for chemical mechanical polishing*,
    US 5,738,574 A, granted 1998-04-14.
    <https://patents.google.com/patent/US5738574A/en>
[^pat-cmp-window]: M. Birang, A. Gleason and W. L. Guthrie (Applied
    Materials), *Forming a transparent window in a polishing pad for a
    chemical mechanical polishing apparatus*, US 5,893,796 A, granted
    1999-04-13. <https://patents.google.com/patent/US5893796A/en>
[^pat-cmp-endpoint-ibm]: N. E. Lustig, K. L. Saenger and H.-M. Tong
    (IBM), *In-situ endpoint detection and process monitoring method
    and apparatus for chemical-mechanical polishing*, US 5,433,651 A,
    granted 1995-07-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5433651>
[^pat-cmp-ibm-1988]: M. M. Chow, J. E. Cronin, W. L. Guthrie,
    C. W. Kaanta et al. (IBM), *Method for producing coplanar
    multi-level metal/insulator films on a substrate and for forming
    patterned conductive lines simultaneously with stud vias*,
    US 4,789,648 A, granted 1988-12-06.
    <https://patents.google.com/patent/US4789648A/en>
[^pat-cmp-ibm-1990]: K. D. Beyer et al. (IBM), *Chem-mech polishing
    method for producing coplanar metal/insulator films on a
    substrate*, US 4,944,836 A, filed 1985-10-28, granted 1990-07-31.
    <https://patents.google.com/patent/US4944836A/en>
[^chiphistory-mirra]: Chip History Center, *The Mirra CMP System by
    Applied Materials*.
    <https://www.chiphistory.org/142-applied-materials-the-mirra-cmp-system>
[^ebara-frex]: EBARA Precision Machinery Europe, *CMP Tools*
    (F-REX200M2). <https://www.ebara-pm.eu/systems/cmp-tools/>
[^wiki-cmp]: Wikipedia, *Chemical-mechanical polishing*.
    <https://en.wikipedia.org/wiki/Chemical-mechanical_polishing>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^moon-2016]: Y. Moon, "Chemical and physical mechanisms of dielectric
    chemical mechanical polishing (CMP)", in *Advances in Chemical
    Mechanical Planarization (CMP)*, Woodhead Publishing, 2016,
    pp. 3–26, ISBN 978-0-08-100165-3.
    <https://doi.org/10.1016/B978-0-08-100165-3.00001-2>
[^stine-1998]: B. E. Stine, D. O. Ouma, R. R. Divecha, D. S. Boning,
    J. E. Chung, D. L. Hetherington, C. R. Harwood, O. S. Nakagawa and
    S.-Y. Oh, "Rapid characterization and modeling of pattern-dependent
    variation in chemical-mechanical polishing", *IEEE Transactions on
    Semiconductor Manufacturing* **11**(1), 129–140 (1998).
    <https://doi.org/10.1109/66.661292>
[^stine-1998-ted]: B. E. Stine, D. S. Boning, J. E. Chung,
    L. Camilletti, F. Kruppa, E. R. Equi, W. Loh, S. Prasad,
    M. Muthukrishnan, D. Towery, M. Berman and A. Kapoor, "The physical
    and electrical effects of metal-fill patterning practices for oxide
    chemical-mechanical polishing processes", *IEEE Transactions on
    Electron Devices* **45**(3), 665–679 (1998).
    <https://doi.org/10.1109/16.661228>
[^ouma-2002]: D. O. Ouma, D. S. Boning, J. E. Chung, W. G. Easter,
    V. Saxena, S. Misra and A. Crevasse, "Characterization and modeling
    of oxide chemical-mechanical polishing using planarization length
    and pattern density concepts", *IEEE Transactions on Semiconductor
    Manufacturing* **15**(2), 232–244 (2002).
    <https://doi.org/10.1109/66.999598>
[^boning-1994]: D. S. Boning, T. Maung, J. E. Chung, K.-J. Chang,
    S.-Y. Oh and D. Bartelink, "Statistical metrology for interlevel
    dielectric thickness variation", *Proc. SPIE* **2334**, Advanced
    Microelectronic Manufacturing, 316–327 (1994).
    <https://doi.org/10.1117/12.186764>
[^chang-1995]: E. Chang, B. Stine, T. Maung, R. Divecha, D. Boning,
    J. Chung, K. Chang, G. Ray, D. Bradbury, O. S. Nakagawa, S. Oh and
    D. Bartelink, "Using a statistical metrology framework to identify
    systematic and random sources of die- and wafer-level ILD
    thickness variation in CMP processes", *IEDM 1995 Technical
    Digest*, pp. 499–502. <https://doi.org/10.1109/IEDM.1995.499247>
[^sivaram-1992]: S. Sivaram, R. Tolles, H. Bath, E. Lee and
    R. Leggett, "Chemical Mechanical Polishing of Interlevel
    Dielectrics: Models for Removal Rate and Planarity", *MRS
    Proceedings* **260**, 53 (1992). <https://doi.org/10.1557/PROC-260-53>
[^cook-1990]: L. M. Cook, "Chemical processes in glass polishing",
    *Journal of Non-Crystalline Solids* **120**(1–3), 152–171 (1990).
    <https://doi.org/10.1016/0022-3093(90)90200-6>
[^preston-1927]: F. W. Preston, "The theory and design of plate glass
    polishing machines", *Journal of the Society of Glass Technology*
    **11**, 214–256 (1927). Retrieved in secondary sources only; the
    1927 original is not online.
[^runnels-1994]: S. R. Runnels and L. M. Eyman, "Tribology Analysis of
    Chemical-Mechanical Polishing", *Journal of The Electrochemical
    Society* **141**(6), 1698–1701 (1994).
    <https://doi.org/10.1149/1.2054985>
[^rev-02]: M. Krishnan, J. W. Nalaskowski and L. M. Cook, "Chemical
    Mechanical Planarization: Slurry Chemistry, Materials, and
    Mechanisms", *Chemical Reviews* **110**(1), 178–204 (2010).
    <https://doi.org/10.1021/cr900170z>
[^devriendt-1998]: K. Devriendt, E. Vrancken, N. Heylen, J. Grillaert,
    M. Meuris, M. M. Heyns and Z. C. Lin, "Relation between Oxide-CMP
    Induced Defects and Post-CMP Cleaning Strategies", *Solid State
    Phenomena* **65–66**, 173–176 (1998).
    <https://doi.org/10.4028/www.scientific.net/SSP.65-66.173>
[^philipossian-2009]: A. Philipossian and T. Sun, "Frictional Analysis
    of Various Poly(vinyl alcohol) Brush Roller Designs for
    Post-Interlevel Dielectric CMP Scrubbing Applications",
    *Electrochemical and Solid-State Letters* **12**(3), H84 (2009).
    <https://doi.org/10.1149/1.3058994>
[^sun-2017]: T. Sun, Z. Han and M. Keswani, "Brush Scrubbing for
    Post-CMP Cleaning", in *Developments in Surface Contamination and
    Cleaning, Volume 9*, Elsevier, 2017, pp. 109–133.
    <https://doi.org/10.1016/B978-0-323-43157-6.00004-5>
[^steigerwald-1997]: J. M. Steigerwald, S. P. Murarka and R. J. Gutmann,
    *Chemical Mechanical Planarization of Microelectronic Materials*,
    Wiley, 1997, ISBN 978-0-471-13827-6.
    <https://doi.org/10.1002/9783527617746>
[^oliver-2004]: M. R. Oliver (ed.), *Chemical-Mechanical Planarization
    of Semiconductor Materials*, Springer Series in Materials Science
    69, Springer, 2004, ISBN 978-3-540-43181-9.
    <https://doi.org/10.1007/978-3-662-06234-0>
[^zantye-2004]: P. B. Zantye, A. Kumar and A. K. Sikder, "Chemical
    mechanical planarization for microelectronics applications",
    *Materials Science and Engineering: R* **45**(3–6), 89–220 (2004).
    <https://doi.org/10.1016/j.mser.2004.06.002>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
