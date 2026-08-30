(category-cmp)=
# Chemical-mechanical planarisation

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
three ways, all of which appear in the SKY130 flow:

* **Dielectric planarisation with a stop layer.** The STI trench-fill
  oxide is polished back until the nitride hard mask on the active
  areas is exposed ({ref}`CMPNIT <step-012>`); a sacrificial
  {term}`PSG` is polished over the gate-poly caps ({ref}`CMPP <step-090>`);
  and the pre-metal dielectric is planarised over the local interconnect
  ({ref}`CMPL <step-106>`).
* **Metal plug formation.** Blanket CVD tungsten is polished off the
  field, leaving tungsten only in the contact and via holes
  ({ref}`WCMPLI <step-100>`, {ref}`WCMP2 <step-111>`,
  {ref}`WCMP3 <step-122>`, {ref}`WCMP4 <step-133>`,
  {ref}`WCMP5 <step-148>`) — the {term}`W plug`.
* **Inter-metal dielectric planarisation** without a stop layer: the
  oxide deposited over each aluminium level is polished to a target
  remaining thickness ({ref}`CMPM <step-116>`, {ref}`CMPM2 <step-127>`,
  {ref}`CMPM3 <step-142>`, {ref}`CMPM4 <step-157>`), so that the next
  via and metal lithography see a flat surface. The SKY130 design
  assumptions publish the resulting nominal dielectric thicknesses,
  for example a pre-LI ILD of 0.5 µm ([SKY130 PDK, Criteria &
  Assumptions][pdk-assume]).

CMP was developed at IBM in the 1980s — the foundational patents
describe a "chem-mech polishing method for producing coplanar
metal/insulator films on a substrate" ([Beyer et al., US 4,944,836][beyer])
— and became a mainstream production step in the 1990s as interconnect
levels multiplied ([Wikipedia: Chemical-mechanical polishing][wiki-cmp]).

## Physics and engineering background

### Preston's equation

The empirical law of polishing was written down by Preston for plate
glass in 1927 (Preston 1927, cited below): the removal rate is
proportional to the pressure and to the relative velocity between pad
and wafer,

```{math}
\frac{dh}{dt} = k_p\,P\,v ,
```

where {math}`k_p`, the Preston coefficient, absorbs the properties of
pad, slurry and film. It holds well for oxide polishing over the range
of a few psi and tens of metres per minute used in production, and
deviations from it (a non-zero pressure threshold, sub-linear velocity
dependence) are the subject of later models such as Luo and Dornfeld's,
which treats the removal as the product of the number of active
abrasive particles and the volume each removes ([Luo and Dornfeld
2001][luo]; Zantye, Kumar and Sikder [zantye]).

### Chemistry and mechanics

Polishing is neither pure abrasion nor pure etching. For silicon dioxide,
Cook showed that the alkaline slurry (pH 10–11) hydrolyses the oxide
surface to a soft silanol-rich layer, that silica abrasive particles
bond to it and tear it away, and that dissolved silica must be carried
off before it re-deposits ([Cook 1990][cook]); the slurry is
"cerium dioxide" or colloidal/fumed silica in water with KOH or NH₄OH
([Wikipedia: Chemical-mechanical polishing][wiki-cmp]). For tungsten,
Kaufman and co-workers at IBM showed that an oxidiser in the slurry
(originally potassium ferricyanide, later hydrogen peroxide or ferric
nitrate) forms a thin, soft WO₃ layer that the abrasive removes,
exposing fresh metal, so that the rate is set by oxidation and the
selectivity to oxide by the slurry's acidity ([Kaufman et al.
1991][kaufman]). The pad — a porous polyurethane, "porous polymeric
materials with a pore size between 30 and 50 μm" ([Wikipedia:
Chemical-mechanical polishing][wiki-cmp]) — carries the slurry in its
pores, and its asperities transmit the load; it glazes with use and
"must be regularly reconditioned" with a diamond disc.

### Planarisation, dishing and erosion

A pad is compliant on the scale of the wafer but stiff on the scale of
a feature, so it removes high features first: this is what makes CMP
planarise rather than merely thin. The planarisation length is of the
order of a few millimetres, and within it the removal rate of a
feature depends on the local pattern density — dense regions of raised
oxide polish more slowly than sparse ones (Steigerwald, Murarka and
Gutmann [steigerwald]). The same compliance causes the two classic
defects of a stop-layer or metal polish: {term}`dishing`, the recession
of a wide soft feature (an oxide-filled wide trench, a tungsten pad)
below the surrounding hard surface, and {term}`erosion`, the thinning
of the hard surface (oxide between a dense array of plugs, or the STI
nitride in dense active areas). Both are reduced by high-selectivity
slurries, a short over-polish, and design rules on feature width and
density — which is why PDKs require metal fill and limit wide plates
([Zantye, Kumar and Sikder 2004][zantye]; [Krishnan, Nalaskowski and
Cook 2009][krishnan]).

### Endpoint and process control

The polish is stopped by one of: a fixed time derived from a measured
rate; motor-current or friction endpoint, which changes when the pad
reaches a different material (nitride under oxide, oxide under
tungsten); or in-situ optical or eddy-current thickness sensing. The
Applied Mirra "was the first CMP system that successfully integrated
endpoint detection and integrated cleaning"
([Chip History Center: Mirra][chiphistory]). Pre- and post-polish
thickness maps from an optical thickness gauge give the removal and its
uniformity, which are put under {term}`SPC`; within-wafer
non-uniformity is tuned with zoned carrier pressures, retaining rings
and pad conditioning.

### Post-CMP cleaning

CMP leaves slurry particles and, for tungsten, metal ions on the
surface; they must be removed before they dry. A post-CMP cleaner uses
rotating polyvinyl-alcohol (PVA) brushes with dilute NH₄OH (for oxide)
or dilute HF or citric acid (for tungsten), megasonic rinsing and a spin
dry, integrated into the polisher so that the wafer never dries between
polish and clean ([Chip History Center: Mirra][chiphistory]).

### STI, tungsten and oxide polishes compared

| Polish | Film removed | Stop | Slurry | Failure modes |
|--------|--------------|------|--------|---------------|
| STI ({ref}`CMPNIT <step-012>`) | HDP oxide | Si₃N₄ | silica/KOH, or ceria with surfactant for high oxide:nitride selectivity | nitride erosion, oxide dishing in wide trenches, residual oxide on nitride |
| Tungsten ({ref}`WCMPLI <step-100>` etc.) | W and Ti/TiN liner | ILD oxide | alumina or silica with H₂O₂ or Fe(NO₃)₃, pH 2–4 | plug recess, oxide erosion in dense arrays, W "coring", corrosion |
| ILD ({ref}`CMPM <step-116>` etc.) | PECVD/HDP oxide | none (fixed removal) | fumed silica/KOH or NH₄OH, pH 10–11 | thickness non-uniformity, scratches, pattern-density steps |

## Typical equipment

* **Polishers**: Applied Materials Mirra ("the Company announced its
  entry into the CMP market with the Mirra CMP in December 1995. The
  Mirra CMP system features a unique three-station, four polishing
  head design" [amat-1997]) and Mirra Mesa with integrated cleaner
  ([Chip History Center: Mirra][chiphistory]); Ebara F-REX 200 (the current
  F-REX200M2 "polishes 200 mm wafers with high k-materials and
  aluminium layers" [ebara]); IPEC/Westech 372 and 472 and the
  SpeedFam-IPEC Auriga; Strasbaugh 6DS-SP; Lam Teres.
* **Post-CMP cleaners**: OnTrak (later Lam) DSS-200 double-sided
  brush scrubbers; Applied Mesa integrated cleaner.
* **Metrology**: optical film-thickness mappers (Nanometrics NanoSpec,
  Rudolph, KLA-Tencor), stylus profilers for dishing and step height
  (KLA-Tencor HRP), and unpatterned-wafer defect inspection
  (KLA-Tencor Surfscan) for scratches.

## Typical consumables

* **Slurries**: fumed-silica in KOH (Cabot Semi-Sperse SS-12 class)
  for oxide; colloidal silica (Klebosol class); ceria-based slurries
  for STI with nitride selectivity; alumina or silica plus oxidiser
  (H₂O₂, Fe(NO₃)₃) for tungsten. Slurry is consumed at a few hundred
  millilitres per wafer per platen ([Wikipedia: Colloidal
  silica][wiki-silica]; [Wikipedia: Cerium(IV) oxide][wiki-ceria]).
* **Pads**: stacked polyurethane pads (Rodel IC1000 over Suba IV
  class) for primary polish; soft Politex-type pads for buffing;
  replaced every few hundred to a thousand wafers ([Wikipedia:
  Polyurethane][wiki-pu]).
* **Conditioners**: diamond-grit discs; **carrier films** and retaining
  rings; **brushes** (PVA) for the cleaner.
* **Chemicals**: KOH, NH₄OH, dilute HF, citric acid, hydrogen peroxide
  for slurry make-up and post-CMP clean; ultrapure water in quantity.

## Steps in this category

| Step | Code | Name |
|------|------|------|
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

## References

### Cross-check

* F. W. Preston, "The theory and design of plate glass polishing
  machines", *Journal of the Society of Glass Technology* **11**,
  214–256 (1927).
* L. M. Cook, "Chemical processes in glass polishing", *Journal of
  Non-Crystalline Solids* **120**, 152–171 (1990).
  <https://doi.org/10.1016/0022-3093(90)90200-6>
* F. B. Kaufman et al., "Chemical-Mechanical Polishing for Fabricating
  Patterned W Metal Features as Chip Interconnects", *Journal of the
  Electrochemical Society* **138**, 3460–3465 (1991).
  <https://doi.org/10.1149/1.2085434>
* K. D. Beyer et al., "Chem-mech polishing method for producing
  coplanar metal/insulator films on a substrate", US Patent 4,944,836
  (1990). <https://patents.google.com/patent/US4944836A/en>
* SkyWater Technology / Google, "Criteria & Assumptions", *SKY130 PDK
  documentation* (dielectric thicknesses).
  <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
* Chip History Center, "The Mirra CMP System by Applied Materials".
  <https://www.chiphistory.org/142-applied-materials-the-mirra-cmp-system>
* Applied Materials, 1997 Annual Report (entry into CMP with the
  Mirra). <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
* EBARA Precision Machinery Europe, "CMP Tools" (F-REX200M2).
  <https://www.ebara-pm.eu/systems/cmp-tools/>

### High-level

* Wikipedia, "Chemical-mechanical polishing".
  <https://en.wikipedia.org/wiki/Chemical-mechanical_polishing>
* Wikipedia, "Shallow trench isolation".
  <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
* Wikipedia, "Colloidal silica".
  <https://en.wikipedia.org/wiki/Colloidal_silica>
* Wikipedia, "Cerium(IV) oxide".
  <https://en.wikipedia.org/wiki/Cerium(IV)_oxide>
* Wikipedia, "Polyurethane".
  <https://en.wikipedia.org/wiki/Polyurethane>
* J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
  Technology*, Prentice Hall, 2000, ISBN 978-0-13-085037-9, ch. 11
  ("Back-End Technology").
* S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4: Deep-Submicron
  Process Technology*, Lattice Press, 2002, ISBN 978-0-9616721-7-1,
  ch. 8 ("Chemical-Mechanical Polishing").
* M. Quirk and J. Serda, *Semiconductor Manufacturing Technology*,
  Prentice Hall, 2001, ISBN 978-0-13-081520-0, ch. 18.
* H. Xiao, *Introduction to Semiconductor Manufacturing Technology*,
  2nd ed., SPIE Press, 2012, ch. 12. <https://doi.org/10.1117/3.924283>

### Deep dive

* J. M. Steigerwald, S. P. Murarka and R. J. Gutmann, *Chemical
  Mechanical Planarization of Microelectronic Materials*, Wiley, 1997.
  <https://doi.org/10.1002/9783527617746>
* P. B. Zantye, A. Kumar and A. K. Sikder, "Chemical mechanical
  planarization for microelectronics applications", *Materials Science
  and Engineering R* **45**, 89–220 (2004).
  <https://doi.org/10.1016/j.mser.2004.06.002>
* M. Krishnan, J. W. Nalaskowski and L. M. Cook, "Chemical Mechanical
  Planarization: Slurry Chemistry, Materials, and Mechanisms",
  *Chemical Reviews* **110**, 178–204 (2010).
  <https://doi.org/10.1021/cr900170z>
* J. Luo and D. A. Dornfeld, "Material removal mechanism in chemical
  mechanical polishing: theory and modeling", *IEEE Transactions on
  Semiconductor Manufacturing* **14**(2), 112–133 (2001).
  <https://doi.org/10.1109/66.920723>
* K. D. Beyer et al., "Method for producing coplanar multi-level
  metal/insulator films on a substrate", US Patent 4,789,648 (1988).
  <https://patents.google.com/patent/US4789648A/en>

[wiki-cmp]: https://en.wikipedia.org/wiki/Chemical-mechanical_polishing
[wiki-silica]: https://en.wikipedia.org/wiki/Colloidal_silica
[wiki-ceria]: https://en.wikipedia.org/wiki/Cerium(IV)_oxide
[wiki-pu]: https://en.wikipedia.org/wiki/Polyurethane
[cook]: https://doi.org/10.1016/0022-3093(90)90200-6
[kaufman]: https://doi.org/10.1149/1.2085434
[luo]: https://doi.org/10.1109/66.920723
[zantye]: https://doi.org/10.1016/j.mser.2004.06.002
[krishnan]: https://doi.org/10.1021/cr900170z
[steigerwald]: https://doi.org/10.1002/9783527617746
[beyer]: https://patents.google.com/patent/US4944836A/en
[chiphistory]: https://www.chiphistory.org/142-applied-materials-the-mirra-cmp-system
[amat-1997]: https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf
[ebara]: https://www.ebara-pm.eu/systems/cmp-tools/
[pdk-assume]: https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html
