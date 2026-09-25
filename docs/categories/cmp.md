(category-cmp)=
# Chemical-mechanical planarisation

Chemical-mechanical planarisation ({term}`CMP`) makes the wafer flat
again. Every deposited film copies the topography beneath it, so after
a few layers the surface would become a landscape of hills and valleys
too rough for lithography to focus on and too steep for metal to cover.

| | Chemical-mechanical planarisation |
|---|---|
| What it does | Makes the wafer flat again; the high points are removed faster than the low points until the surface is planar. |
| Steps in SKY130 | 12 |
| Tool classes | {ref}`Polishers <machine-cmp-polisher>`, {ref}`Post-CMP cleaners <machine-post-cmp-cleaner>` |
| Consumable classes | {ref}`CMP consumables <material-cmp-consumables>` |
| Governing relation | Preston's equation |

## What this class of step does

Chemical-mechanical planarisation ({term}`CMP`) makes the wafer flat
again. Every deposited film copies the topography beneath it, so after
a few layers the surface would become a landscape of hills and valleys
too rough for lithography to focus on and too steep for metal to cover.
CMP presses the wafer face-down against a rotating polishing pad
flooded with a slurry of fine abrasive particles in a chemically active
liquid. The high points are removed faster than the low points until the
surface is planar, and the polish is stopped either at a fixed removal
or when a harder underlying "stop" layer is reached.

Precisely, CMP is used in a 130 nm aluminium-interconnect process in
three ways, all of which appear in the flow described in this
reference (the assignments below are this reference's readings; the
step pages give the public basis for each):

* **Dielectric planarisation with a stop layer.** The {term}`STI` trench-fill
  oxide is polished back until the nitride {term}`hard mask` on the active
  areas is exposed ({ref}`CMPNIT <step-012>`); a sacrificial
  {term}`PSG` is polished over the gate-poly caps ({ref}`CMPP <step-090>`);
  and the pre-metal dielectric is planarised over the local interconnect
  ({ref}`CMPL <step-106>`).
* **Metal plug formation.** Blanket {term}`CVD` tungsten is polished off the
  field, leaving tungsten only in the contact and via holes
  ({ref}`WCMPLI <step-100>`, {ref}`WCMP2 <step-111>`,
  {ref}`WCMP3 <step-122>`, {ref}`WCMP4 <step-133>`,
  {ref}`WCMP5 <step-148>`) — the {term}`W plug`.
* **Inter-metal dielectric planarisation** without a stop layer: the
  oxide deposited over each aluminium level is polished to a target
  remaining thickness ({ref}`CMPM <step-116>`, {ref}`CMPM2 <step-127>`,
  {ref}`CMPM3 <step-142>`, {ref}`CMPM4 <step-157>`), so that the next
  via and metal lithography see a flat surface. The SKY130 design
  assumptions give, for example, a pre-LI {term}`ILD` thickness of 0.5 µm.[^pdk-03]

CMP was developed at IBM in the 1980s — the foundational patents
describe a "chem-mech polishing method for producing coplanar
metal/insulator films on a substrate"[^pat-cmp-ibm-1990]
— and became a mainstream production step in the 1990s as interconnect
levels multiplied.[^wiki-cmp]

## Physics and engineering background

### Preston's equation

The empirical law of polishing was written down by {term}`Preston <Preston equation>` for plate
glass in 1927 (Preston 1927, cited below): the removal rate is
proportional to the pressure and to the relative velocity between pad
and wafer,

```{math}
\frac{dh}{dt} = k_p\,P\,v ,
```

where {math}`k_p`, the Preston coefficient, absorbs the properties of
pad, slurry and film. It holds well for oxide polishing over the range
of a few psi and tens of metres per minute used in production (typical
industry values).[^zantye-2004] Deviations from it (a non-zero
pressure threshold, sub-linear velocity dependence) are the subject of
later models such as Luo and Dornfeld's, which treats the removal as the
product of the number of active abrasive particles and the volume each
removes.[^luo-2001][^zantye-2004]

### Chemistry and mechanics

Polishing is neither pure abrasion nor pure etching.

**Oxide chemistry.** For silicon dioxide, Cook showed that the alkaline
slurry (pH 10–11) hydrolyses the oxide surface to a soft silanol-rich
layer, that silica abrasive particles bond to it and tear it away, and
that dissolved silica must be carried off before it
re-deposits.[^cook-1990] The abrasive is "cerium dioxide"[^wiki-cmp] or,
for oxide, colloidal/fumed silica in water with KOH or
NH₄OH.[^cook-1990][^rev-02]

**Tungsten chemistry.** For tungsten, Kaufman and co-workers at IBM
showed that an oxidiser in the slurry (originally potassium
ferricyanide, later hydrogen peroxide or ferric nitrate) forms a thin,
soft WO₃ layer that the abrasive removes, exposing fresh
metal.[^kaufman-1991] The rate is set by oxidation and the
{term}`selectivity` to oxide by the slurry's acidity.[^kaufman-1991]

**The pad.** The pad — a porous polyurethane, "porous polymeric
materials with a pore size between 30 and 50 μm"[^wiki-cmp] — carries
the slurry in its pores, and its asperities transmit the load. It
glazes with use and "must be regularly reconditioned" with a diamond
disc.

### Planarisation, dishing and erosion

A pad is compliant on the scale of the wafer but stiff on the scale of a
feature, so it removes high features first: this is what makes CMP
planarise rather than merely thin. The planarisation length is of the
order of a few millimetres, and within it the removal rate of a feature
depends on the local pattern density — dense regions of raised oxide
polish more slowly than sparse ones.[^steigerwald-1997] The same
compliance causes the two classic defects of a stop-layer or metal
polish:

* **{term}`Dishing <dishing>`** — the recession of a wide soft feature
  (an oxide-filled wide trench, a tungsten pad) below the surrounding
  hard surface.
* **{term}`Erosion <erosion>`** — the thinning of the hard surface
  (oxide between a dense array of plugs, or the STI nitride in dense
  active areas).

Both are reduced by high-selectivity slurries, a short
over-polish, and design rules on feature width and density — which is
why PDKs require metal fill and limit wide
plates.[^zantye-2004][^rev-02]

### Endpoint and process control

The polish is stopped by one of: a fixed time derived from a measured
rate; motor-current or friction {term}`endpoint`, which changes when the pad
reaches a different material (nitride under oxide, oxide under
tungsten); or in-situ optical or eddy-current thickness sensing. A Chip History
Center article calls the Applied Mirra "the first CMP system that
successfully integrated endpoint detection and integrated
cleaning".[^chiphistory-mirra] Applied's own release introduces its
integrated Mesa cleaner, "specifically developed for the Mirra", with the
Mirra Mesa in 1999.[^amat-mesa-1999] Pre-
and post-polish thickness maps from an optical thickness gauge give the
removal and its uniformity, which are put under {term}`SPC`;
within-wafer non-uniformity is tuned with zoned carrier pressures,
retaining rings and pad conditioning.

### Post-CMP cleaning

CMP leaves slurry particles and, for tungsten, metal ions on the
surface; they must be removed before they dry. A post-CMP cleaner uses
rotating polyvinyl-alcohol (PVA) brushes with dilute NH₄OH (for oxide)
or dilute HF or citric acid (for tungsten), megasonic rinsing and a spin
dry, integrated into the polisher so that the wafer never dries between
polish and clean.

### STI, tungsten and oxide polishes compared

The film and stop-layer columns are those typical of the node; SKY130's
own films are this reference's readings, set out with their public
sources on the step pages.

:::{table} The three CMP polishes of the flow, film and stop typical of the node; SKY130's own films are this reference's readings, set out on the step pages

| Polish | Film removed | Stop | Slurry | Failure modes |
|--------|--------------|------|--------|---------------|
| STI ({ref}`CMPNIT <step-012>`) | HDP oxide | Si₃N₄ | silica/KOH, or ceria with surfactant for high oxide:nitride selectivity | nitride erosion, oxide dishing in wide trenches, residual oxide on nitride |
| Tungsten ({ref}`WCMPLI <step-100>` etc.) | W and Ti/TiN liner | ILD oxide | alumina or silica with H₂O₂ or Fe(NO₃)₃, pH 2–4 | plug recess, oxide erosion in dense arrays, W "coring", corrosion |
| ILD ({ref}`CMPM <step-116>` etc.) | PECVD/HDP oxide | none (fixed removal) | fumed silica/KOH or NH₄OH, pH 10–11 | thickness non-uniformity, scratches, pattern-density steps |
:::

The slurry pH values in the table are typical industry
values.[^steigerwald-1997][^zantye-2004]

## Typical equipment

**Polishers.** Applied Materials Mirra ("the Company announced its
entry into the CMP market with the Mirra CMP in December 1995. The
Mirra CMP system features a unique three-station, four polishing head
design")[^amat-1997] and Mirra Mesa with integrated cleaner
(1999);[^amat-mesa-1999] Ebara F-REX 200 (the current F-REX200M2
"polishes 200 mm wafers with high k-materials and aluminium
layers");[^ebara-frex] IPEC/Westech 372 and 472 and the SpeedFam-IPEC
Auriga; Strasbaugh 6DS-SP; Lam Teres.

**Post-CMP cleaners.** OnTrak (later Lam) DSS-200 double-sided brush
scrubbers; Applied Mesa integrated cleaner.

**Metrology.** {ref}`Optical film-thickness mappers <machine-film-thickness-metrology>` (Nanometrics NanoSpec,
Rudolph, KLA-Tencor), {ref}`stylus profilers <machine-cross-section-sem-profilers>` for dishing and step height
(KLA-Tencor HRP), and {ref}`unpatterned-wafer defect inspection <machine-defect-inspection>` (KLA-Tencor
Surfscan) for scratches.

:::{table} The equipment classes above, for scanning; models, dates and quotations are in the paragraphs above

| Tool class | Representative models | Note |
|---|---|---|
| {ref}`Polishers <machine-cmp-polisher>` | Applied Materials Mirra, Mirra Mesa; Ebara F-REX; IPEC/Westech; SpeedFam-IPEC Auriga; Strasbaugh; Lam Teres | see above |
| {ref}`Post-CMP cleaners <machine-post-cmp-cleaner>` | OnTrak (later Lam), Applied Mesa | double-sided brush scrubbers |
| {ref}`Optical film-thickness mappers <machine-film-thickness-metrology>` | Nanometrics NanoSpec, Rudolph, KLA-Tencor | — |
| {ref}`Stylus profilers <machine-cross-section-sem-profilers>` | KLA-Tencor | for dishing and step height |
| {ref}`Unpatterned-wafer defect inspection <machine-defect-inspection>` | KLA-Tencor Surfscan | for scratches |
:::

## Typical consumables

* **{ref}`Slurries <material-cmp-consumables>`**: fumed-silica in KOH (Cabot Semi-Sperse SS-12 class)
  for oxide; colloidal silica (Klebosol class); ceria-based slurries
  for STI with nitride selectivity; alumina or silica plus oxidiser
  (H₂O₂, Fe(NO₃)₃) for tungsten. Slurry is consumed at a few hundred
  millilitres per wafer per platen, a typical industry figure.[^zantye-2004]
* **{ref}`Pads <material-cmp-consumables>`**: stacked polyurethane pads (Rodel IC1000 over Suba IV
  class) for primary polish; soft Politex-type pads for buffing;
  replaced after a few hundred to a thousand wafers, a typical
  industry figure.[^steigerwald-1997]
* **Conditioners**: diamond-grit discs; **carrier films** and retaining
  rings; **brushes** (PVA) for the cleaner.
* **{ref}`Chemicals <material-cmp-consumables>`**: KOH, NH₄OH, dilute HF, citric acid, hydrogen peroxide
  for slurry make-up and post-CMP clean; ultrapure water in quantity.

## Steps in this category

:::{table} The twelve CMP steps of the flow, by step number

| Step | Code | Name | Machine class |
|------|------|------|----------------|
| 12 | {ref}`CMPNIT <step-012>` | CMP over nitride | {ref}`CMP polisher <machine-cmp-polisher>` |
| 90 | {ref}`CMPP <step-090>` | CMP over poly | {ref}`CMP polisher <machine-cmp-polisher>` |
| 100 | {ref}`WCMPLI <step-100>` | W CMP for local interconnect | {ref}`CMP polisher <machine-cmp-polisher>` |
| 106 | {ref}`CMPL <step-106>` | CMP polish over local interconnect | {ref}`CMP polisher <machine-cmp-polisher>` |
| 111 | {ref}`WCMP2 <step-111>` | W CMP for metal contact | {ref}`CMP polisher <machine-cmp-polisher>` |
| 116 | {ref}`CMPM <step-116>` | CMP over metal1 | {ref}`CMP polisher <machine-cmp-polisher>` |
| 122 | {ref}`WCMP3 <step-122>` | W CMP for via1 | {ref}`CMP polisher <machine-cmp-polisher>` |
| 127 | {ref}`CMPM2 <step-127>` | CMP over metal2 | {ref}`CMP polisher <machine-cmp-polisher>` |
| 133 | {ref}`WCMP4 <step-133>` | W CMP for via2 | {ref}`CMP polisher <machine-cmp-polisher>` |
| 142 | {ref}`CMPM3 <step-142>` | CMP over metal3 | {ref}`CMP polisher <machine-cmp-polisher>` |
| 148 | {ref}`WCMP5 <step-148>` | W CMP for via3 | {ref}`CMP polisher <machine-cmp-polisher>` |
| 157 | {ref}`CMPM4 <step-157>` | CMP over metal4 | {ref}`CMP polisher <machine-cmp-polisher>` |
:::

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
## Related patents, papers and filings

24 families concern this page (13 unknown, 11 expired).

See {ref}`patents-by-module` for the full, grouped list (families still in force or of unknown status are collapsed there too).
<!-- index-links:end -->

## References

### Cross-check

* Preston, *J. Soc. Glass Technol.* 1927 — the removal-rate law (no
  online copy is known).[^preston-1927]
* [Cook, *J. Non-Cryst. Solids* 1990](<https://doi.org/10.1016/0022-3093(90)90200-6>) — the chemistry of oxide
  polishing.[^cook-1990]
* [Kaufman et al. (IBM), *JES* 1991](<https://doi.org/10.1149/1.2085434>) — tungsten CMP by oxidation and
  abrasion.[^kaufman-1991]
* [Beyer et al. (IBM), US 4,944,836](<https://patents.google.com/patent/US4944836A/en>) — the foundational
  metal/insulator CMP patent.[^pat-cmp-ibm-1990]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — dielectric
  thicknesses.[^pdk-03]
* [Chip History Center, *The Mirra CMP System*](<https://www.chiphistory.org/142-applied-materials-the-mirra-cmp-system>) — the Mirra in
  historical context (its integrated-cleaning claim is qualified
  above).[^chiphistory-mirra]
* [Applied Materials, 1997 Annual Report](<https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>) — entry into CMP with the
  Mirra.[^amat-1997]
* [EBARA Precision Machinery Europe, *CMP Tools*](<https://www.ebara-pm.eu/systems/cmp-tools/>) —
  F-REX200M2.[^ebara-frex]

### High-level understanding

* [Wikipedia, *Chemical-mechanical polishing*](<https://en.wikipedia.org/wiki/Chemical-mechanical_polishing>) — abrasives, pads and
  conditioning.[^wiki-cmp]
* [Wikipedia, *Shallow trench isolation*](<https://en.wikipedia.org/wiki/Shallow_trench_isolation>).[^wiki-sti]
* [Wikipedia, *Colloidal silica*](<https://en.wikipedia.org/wiki/Colloidal_silica>).[^wiki-colloidal-silica]
* [Wikipedia, *Cerium(IV) oxide*](<https://en.wikipedia.org/wiki/Cerium(IV)_oxide>).[^wiki-ceria]
* [Wikipedia, *Polyurethane*](<https://en.wikipedia.org/wiki/Polyurethane>).[^wiki-polyurethane]
* [Plummer, Deal and Griffin, *Silicon VLSI Technology*](<https://openlibrary.org/isbn/9780130850379>) — ch. 11
  ("Back-End Technology").[^txt-01]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) — ch. 8
  ("Chemical-Mechanical Polishing").[^txt-05]
* [Quirk and Serda, *Semiconductor Manufacturing Technology*](<https://openlibrary.org/isbn/9780130815200>) —
  ch. 18.[^txt-07]
* [Xiao, *Introduction to Semiconductor Manufacturing Technology*](<https://doi.org/10.1117/3.924283>) —
  ch. 12.[^txt-08]

### Deep dive

* [Steigerwald, Murarka and Gutmann, *Chemical Mechanical Planarization
  of Microelectronic Materials*](<https://doi.org/10.1002/9783527617746>) — the standard monograph: pads,
  slurries, pattern effects and consumables.[^steigerwald-1997]
* [Zantye, Kumar and Sikder, *Mater. Sci. Eng. R* 2004](<https://doi.org/10.1016/j.mser.2004.06.002>) — a long review
  of CMP for microelectronics, including Preston deviations and slurry
  consumption.[^zantye-2004]
* [Krishnan, Nalaskowski and Cook, *Chem. Rev.* 2010](<https://doi.org/10.1021/cr900170z>) — oxide, tungsten
  and copper slurry chemistry and mechanisms.[^rev-02]
* [Luo and Dornfeld, *IEEE TSM* 2001](<https://doi.org/10.1109/66.920723>) — the abrasive-contact model of
  material removal.[^luo-2001]
* [Runnels and Eyman, *JES* 1994](<https://doi.org/10.1149/1.2054985>) — a tribology (fluid-film) analysis of
  the wafer–pad contact.[^runnels-1994]
* [Stine et al. (MIT), *IEEE TSM* 1998](<https://doi.org/10.1109/66.661292>) — the pattern-density model and
  the test-mask method for characterising planarisation
  length.[^stine-1998]
* [Ouma et al., *IEEE TSM* 2002](<https://doi.org/10.1109/66.999598>) — characterisation and modelling of
  oxide CMP with planarisation length and density
  concepts.[^ouma-2002]
* [Boyd and Ellul, *JES* 1997](<https://doi.org/10.1149/1.1837687>) — a one-step STI planarisation process by
  CMP.[^boyd-1997]
* [Nandakumar et al. (TI), IEDM 1998](<https://doi.org/10.1109/IEDM.1998.746297>) — STI integration including gap
  fill and planarisation.[^rev-01]
* [Stein, Hetherington and Cecchi (Sandia), *JES* 1999](<https://doi.org/10.1149/1.1391617>) — kinetics of
  tungsten CMP: the roles of alumina abrasive and
  oxidiser.[^stein-1999]
* [Lustig, Saenger and Tong (IBM), US 5,433,651](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5433651>) — in-situ optical
  endpoint detection through a window in the platen.[^pat-cmp-endpoint-ibm]
* [Chow et al. (IBM), US 4,789,648](<https://patents.google.com/patent/US4789648A/en>) — coplanar multi-level
  metal/insulator films by polishing, with lines and stud vias formed
  together.[^pat-cmp-ibm-1988]
* [Oliver (ed.), *Chemical-Mechanical Planarization of Semiconductor
  Materials*](<https://doi.org/10.1007/978-3-662-06234-0>) — chapters on oxide, tungsten and STI CMP, pads and
  slurries.[^oliver-2004]
* [Li (ed.), *Microelectronic Applications of Chemical Mechanical
  Planarization*](<https://doi.org/10.1002/9780470180907>) — including a chapter on STI CMP.[^li-2007]
* [MIT OpenCourseWare 6.152J](<https://ocw.mit.edu/courses/6-152j-micro-nano-processing-technology-fall-2005/>) — lecture notes on the deposition and etch
  steps that CMP planarises (no dedicated CMP lecture).[^ocw-6152]

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pat-cmp-ibm-1990]: K. D. Beyer et al. (IBM), *Chem-mech polishing
    method for producing coplanar metal/insulator films on a substrate*,
    US 4,944,836 A, filed 1985-10-28, granted 1990-07-31.
    <https://patents.google.com/patent/US4944836A/en>
[^wiki-cmp]: Wikipedia, *Chemical-mechanical polishing*.
    <https://en.wikipedia.org/wiki/Chemical-mechanical_polishing>
[^zantye-2004]: P. B. Zantye, A. Kumar and A. K. Sikder, "Chemical
    mechanical planarization for microelectronics applications",
    *Materials Science and Engineering: R* **45**(3–6), 89–220 (2004).
    <https://doi.org/10.1016/j.mser.2004.06.002>
[^luo-2001]: J. Luo and D. A. Dornfeld, "Material removal mechanism in
    chemical mechanical polishing: theory and modeling", *IEEE
    Transactions on Semiconductor Manufacturing* **14**(2), 112–133
    (2001). <https://doi.org/10.1109/66.920723>
[^cook-1990]: L. M. Cook, "Chemical processes in glass polishing",
    *Journal of Non-Crystalline Solids* **120**(1–3), 152–171 (1990).
    <https://doi.org/10.1016/0022-3093(90)90200-6>
[^rev-02]: M. Krishnan, J. W. Nalaskowski and L. M. Cook, "Chemical
    Mechanical Planarization: Slurry Chemistry, Materials, and
    Mechanisms", *Chemical Reviews* **110**(1), 178–204 (2010).
    <https://doi.org/10.1021/cr900170z>
[^kaufman-1991]: F. B. Kaufman, D. B. Thompson, R. E. Broadie, M. A.
    Jaso et al., "Chemical-Mechanical Polishing for Fabricating
    Patterned W Metal Features as Chip Interconnects", *Journal of The
    Electrochemical Society* **138**(11), 3460–3465 (1991).
    <https://doi.org/10.1149/1.2085434>
[^steigerwald-1997]: J. M. Steigerwald, S. P. Murarka and R. J. Gutmann,
    *Chemical Mechanical Planarization of Microelectronic Materials*,
    Wiley, 1997, ISBN 978-0-471-13827-6.
    <https://doi.org/10.1002/9783527617746>
[^chiphistory-mirra]: Chip History Center, *The Mirra CMP System by
    Applied Materials*.
    <https://www.chiphistory.org/142-applied-materials-the-mirra-cmp-system>
[^amat-mesa-1999]: Applied Materials, *Applied Materials Announces New
    Mirra Mesa System to Address Market Demand for Integrated CMP
    Solutions*, press release, 1999-06-10, accessed 2026-09-13.
    <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-new-mirra-mesa-system-address-market>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report*.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^ebara-frex]: EBARA Precision Machinery Europe, *CMP Tools*
    (F-REX200M2). <https://www.ebara-pm.eu/systems/cmp-tools/>
[^preston-1927]: F. W. Preston, "The theory and design of plate glass
    polishing machines", *Journal of the Society of Glass Technology*
    **11**, 214–256 (1927).
[^wiki-sti]: Wikipedia, *Shallow trench isolation*.
    <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
[^wiki-colloidal-silica]: Wikipedia, *Colloidal silica*.
    <https://en.wikipedia.org/wiki/Colloidal_silica>
[^wiki-ceria]: Wikipedia, *Cerium(IV) oxide*.
    <https://en.wikipedia.org/wiki/Cerium(IV)_oxide>
[^wiki-polyurethane]: Wikipedia, *Polyurethane*.
    <https://en.wikipedia.org/wiki/Polyurethane>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^txt-08]: H. Xiao, *Introduction to Semiconductor Manufacturing
    Technology*, 2nd ed., SPIE Press, 2012, ISBN 978-0-8194-9092-6.
    <https://doi.org/10.1117/3.924283>
[^runnels-1994]: S. R. Runnels and L. M. Eyman, "Tribology Analysis of
    Chemical-Mechanical Polishing", *Journal of The Electrochemical
    Society* **141**(6), 1698–1701 (1994).
    <https://doi.org/10.1149/1.2054985>
[^stine-1998]: B. E. Stine, D. O. Ouma, R. R. Divecha, D. S. Boning, J.
    E. Chung, D. L. Hetherington, C. R. Harwood, O. S. Nakagawa and
    S.-Y. Oh, "Rapid characterization and modeling of pattern-dependent
    variation in chemical-mechanical polishing", *IEEE Transactions on
    Semiconductor Manufacturing* **11**(1), 129–140 (1998).
    <https://doi.org/10.1109/66.661292>
[^ouma-2002]: D. O. Ouma, D. S. Boning, J. E. Chung, W. G. Easter et
    al., "Characterization and modeling of oxide chemical-mechanical
    polishing using planarization length and pattern density concepts",
    *IEEE Transactions on Semiconductor Manufacturing* **15**(2),
    232–244 (2002). <https://doi.org/10.1109/66.999598>
[^boyd-1997]: J. M. Boyd and J. P. Ellul, "A One-Step Shallow Trench
    Global Planarization Process Using Chemical Mechanical Polishing",
    *Journal of The Electrochemical Society* **144**(5), 1838–1841
    (1997). <https://doi.org/10.1149/1.1837687>
[^rev-01]: M. Nandakumar, A. Chatterjee, S. Sridhar, K. Joyner,
    M. Rodder and I.-C. Chen, "Shallow trench isolation for advanced
    ULSI CMOS technologies", *IEDM 1998 Technical Digest*, pp. 133–136.
    <https://doi.org/10.1109/IEDM.1998.746297>
[^stein-1999]: D. Stein, D. L. Hetherington and J. L. Cecchi,
    "Investigation of the Kinetics of Tungsten Chemical Mechanical
    Polishing in Potassium Iodate-Based Slurries: I. Role of Alumina and
    Potassium Iodate", *Journal of The Electrochemical Society*
    **146**(1), 376–381 (1999). <https://doi.org/10.1149/1.1391617>
[^pat-cmp-endpoint-ibm]: N. E. Lustig, K. L. Saenger and H.-M. Tong
    (IBM), *In-situ endpoint detection and process monitoring method and
    apparatus for chemical-mechanical polishing*, US 5,433,651 A,
    granted 1995-07-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5433651>
[^pat-cmp-ibm-1988]: M. M. Chow, J. E. Cronin, W. L. Guthrie, C. W. Kaanta
    et al. (IBM), *Method for producing coplanar multi-level
    metal/insulator films on a substrate and for forming patterned
    conductive lines simultaneously with stud vias*, US 4,789,648 A,
    granted 1988-12-06.
    <https://patents.google.com/patent/US4789648A/en>
[^oliver-2004]: M. R. Oliver (ed.), *Chemical-Mechanical Planarization
    of Semiconductor Materials*, Springer Series in Materials Science
    69, Springer, 2004, ISBN 978-3-540-43181-9.
    <https://doi.org/10.1007/978-3-662-06234-0>
[^li-2007]: Y. Li (ed.), *Microelectronic Applications of Chemical
    Mechanical Planarization*, Wiley, 2007.
    <https://doi.org/10.1002/9780470180907>
[^ocw-6152]: MIT OpenCourseWare, *6.152J Micro/Nano Processing
    Technology*, Fall 2005 (lecture notes on lithography, etching,
    deposition and CMP).
    <https://ocw.mit.edu/courses/6-152j-micro-nano-processing-technology-fall-2005/>
