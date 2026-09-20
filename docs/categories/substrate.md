(category-substrate)=
# Substrate / starting material

## What this class of step does

Every wafer that enters the fab begins as a bare, polished disc of
single-crystal silicon bought from a wafer vendor. The "starting
material" step is not a process performed in the fab so much as a
*specification*: it fixes the diameter, thickness, crystal orientation,
doping type and resistivity, oxygen content, flatness and cleanliness
of the silicon on which every later step depends. Once the wafer lot is
released into the line, nothing can change the bulk properties of the
substrate, so the choice is made once, at process design time, and then
audited on every incoming lot.

More precisely, a starting-material specification for a 130 nm-era
CMOS process on 200 mm wafers defines:

* **Diameter and thickness.** 200 mm wafers are 725 µm thick and were
  introduced in 1992; wafers of 200 mm and above carry a single small
  notch, rather than flats, to indicate crystal
  orientation.[^wiki-wafer] The ITRS 2001 front-end-processes chapter
  notes that "200 mm will still be prevalent through the 130 nm node"
  even though 300 mm was then being phased in.[^itrs-01]
* **Crystal orientation.** Orientation is given by the Miller index,
  "(100) or (111) faces being the most common for silicon";[^wiki-wafer]
  CMOS uses (100) because it gives the lowest density of interface
  states at the Si/SiO₂ interface and therefore the best gate
  oxide.[^txt-01]
* **Doping type and resistivity.** Wafers carry "an initial impurity
  doping concentration between 10¹³ and 10¹⁶ atoms per cm³ of boron,
  phosphorus, arsenic, or antimony".[^wiki-wafer] Bulk CMOS processes
  use lightly boron-doped p-type material, typically in the 1–20 Ω·cm
  range, or a lightly doped p-type {term}`epitaxial layer` on a heavily
  doped p⁺ substrate (a "p/p⁺ epi" wafer) to suppress
  latch-up.[^txt-01][^txt-02]
* **Oxygen and gettering.** {term}`CZ` silicon contains dissolved
  interstitial oxygen from the quartz crucible, typically of order
  10¹⁷–10¹⁸ cm⁻³, which can be precipitated deliberately during the
  early high-temperature steps to form an internal {term}`gettering`
  sink beneath a defect-free "denuded zone" at the surface.[^txt-01]
* **Surface quality.** Site flatness, particle counts, surface metal
  contamination and bulk iron are the key incoming-quality metrics; the
  ITRS 2001 starting-materials table (Table 49a) tabulates their targets
  node by node.[^itrs-01]

The formal definitions of all these parameters are in SEMI M1,
*Specification for Polished Single Crystal Silicon Wafers*,[^semi-m1]
with SEMI M62 covering epitaxial wafers[^semi-m62] and SEMI M8 covering
the cheaper test wafers used for tool monitoring.[^semi-m8]

The SKY130 documentation shows a layer set with an n-well, a deep
n-well and p-substrate contacts and states that the process runs on
200 mm wafers; from this we infer that the starting material is a
p-type 200 mm wafer, as is normal for a twin-well bulk CMOS process,
but the resistivity and whether an epitaxial layer is used are not
stated publicly.[^pdk-01]

## Physics and engineering background

### Crystal growth

Almost all IC wafers are cut from boules grown by the Czochralski
method, in which a seed crystal is dipped into molten silicon (melting
point 1414 °C)[^wiki-si] held in a quartz crucible and slowly withdrawn
while rotating, so that the melt freezes onto the seed as one continuous
crystal.[^wiki-cz] The dopant is added to the melt; because the
segregation coefficient of most dopants is less than one, the crystal
grows progressively more heavily doped from seed to tail, and the
resistivity is specified as a range rather than a single value.[^txt-01]
Float-zone growth, which avoids the crucible and gives much lower
oxygen, is used for power and detector devices but is not economical at
200 mm for CMOS.[^wiki-fz]

The boule "is then sliced with a wafer saw (a type of wire saw),
machined to improve flatness, chemically etched to remove crystal damage
from machining steps and finally polished to form wafers";[^wiki-wafer]
in full, the sequence is grinding to diameter, notching, slicing,
lapping, edge rounding, etching, single-side {term}`CMP` to a mirror
finish with sub-nanometre roughness, cleaning and
packing.[^txt-01][^txt-02]

### Orientation, dopant and resistivity

The (100) surface has the lowest interface-trap density after oxidation,
which is why it displaced (111) for MOS devices; the notch on a 200 mm
wafer lies along a ⟨110⟩ direction so that the die edges, and therefore
the cleave planes, are aligned with the crystal.[^txt-01] Boron is the
p-type dopant of choice because it has a high solid solubility and a
segregation coefficient close to 0.8, giving a uniform axial profile;
the resistivity is chosen as a compromise between latch-up immunity and
well-implant dose (a lightly doped substrate is simply overwritten by
the well implants of {ref}`category-implant`).

### Epitaxial wafers

A p/p⁺ epitaxial wafer has a few micrometres of lightly doped silicon
grown by {term}`CVD` from a chlorosilane (SiHCl₃ or SiH₂Cl₂) at
1000–1150 °C on a heavily boron-doped (≈0.01 Ω·cm) substrate. The
heavily doped bulk shorts out the parasitic p-n-p-n thyristor that
causes latch-up and also getters metals, at the cost of a more expensive
wafer and a need to control autodoping and up-diffusion of boron from
the substrate during later hot steps.[^txt-01][^txt-02] Many 130 nm-era
logic processes used epi wafers, and many did not; publicly, SKY130 does
not say which.

### Oxygen, precipitates and gettering

Interstitial oxygen in CZ silicon is supersaturated at device processing
temperatures. A high-temperature step drives oxygen out of the surface
region (out-diffusion), a low-temperature step nucleates precipitates in
the bulk, and subsequent hot steps grow them. The resulting SiO₂
precipitates and their associated dislocation loops trap fast-diffusing
metals such as Fe, Cu and Ni far from the transistors ("intrinsic
gettering"), while the denuded zone near the surface stays defect-free.
Because the {term}`thermal budget` of a 130 nm process is small, wafer vendors
increasingly supply material whose precipitation behaviour has been
pre-set by the crystal-growth conditions.[^txt-01][^itrs-01] Backside
damage or polysilicon films provide alternative "extrinsic"
gettering.[^txt-01]

### Flatness and particles

Site flatness matters because a scanner's depth of focus at the 130 nm
node is only a few hundred nanometres (see {ref}`category-lithography`).
ITRS 2001 states that "for the 130 nm technology node to the end of
optical lithography, scanners will be utilized with rectangular fields
(nominally 25 mm x 32 mm for 4X scanners)" and that the site-flatness
metric should match that field.[^itrs-01] Incoming inspection therefore
measures flatness site by site, counts localised light scatterers
(particles and crystal-originated pits) with a laser surface scanner,
and checks surface metals.

## Typical equipment

The substrate category has no process tool in the fab itself; the
"equipment" is at the wafer vendor and in incoming quality control:

* **Crystal pullers** (CZ furnaces) and **wire saws**, **lappers**,
  **edge grinders** and **polishers** at the wafer maker. The major 200
  mm suppliers of the era were Shin-Etsu Handotai, SUMCO (formed from
  Sumitomo and Mitsubishi Materials silicon), MEMC (later SunEdison and
  now part of GlobalWafers), Wacker
  Siltronic.[^wiki-seh][^wiki-sumco][^wiki-memc][^wiki-siltronic][^wiki-gw]
* **Epitaxial reactors** if epi wafers are specified: single-wafer
  lamp-heated reactors such as the ASM Epsilon series and the Applied
  Materials Centura Epi, or the older batch barrel
  reactors.[^wiki-asm][^wiki-amat]
* **{ref}`Incoming inspection <machine-starting-material>`**: {ref}`laser surface scanners <machine-defect-inspection>`
  (KLA-Tencor Surfscan family), capacitive flatness gauges (ADE),
  {ref}`four-point-probe resistivity mapping <machine-sheet-resistance-metrology>`,
  and FTIR for oxygen content.[^wiki-kla]

## Typical consumables

* Polished prime wafers to SEMI M1;[^semi-m1] epitaxial
  wafers to SEMI M62.[^semi-m62]
* Test and monitor wafers to SEMI M8,[^semi-m8] and
  reclaimed wafers to SEMI M38 for non-critical tool monitoring.
* Wafer carriers (open cassettes or SMIF pods at 200 mm), which must
  not shed particles or outgas.

## Steps in this category

| Step | Code | Name |
|------|------|------|
| 1 | {ref}`SMAT <step-001>` | Starting material |

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
## Related patents, papers and filings

* {ref}`Ideal oxygen precipitating silicon wafers and oxygen out-diffusion-less process therefor <patent-gp25194044>` — US 5,994,761 A (1997)
<!-- index-links:end -->

## References

### Cross-check

* [SEMI M1](<https://store-us.semi.org/products/m00100-semi-m1-specification-for-polished-single-crystal-silicon-wafers>) — the specification that defines every parameter of a
  polished prime wafer.[^semi-m1]
* [SEMI M8](<https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>) — the looser specification for polished test
  wafers.[^semi-m8]
* [SEMI M62](<https://store-us.semi.org/products/m06200-semi-m62-specification-for-silicon-epitaxial-wafers>) — the specification for epitaxial wafers.[^semi-m62]
* [ITRS 2001, *Front End Processes*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>) — Table 49a, starting-material
  targets node by node, and the scanner field-size note.[^itrs-01]
* [SkyWater PDK documentation](<https://skywater-pdk.readthedocs.io/en/main/>) — the layer set and 200 mm wafer
  statement from which the substrate type is inferred.[^pdk-01]

### High-level understanding

* [Wikipedia, *Wafer (electronics)*](<https://en.wikipedia.org/wiki/Wafer_(electronics)>) — diameters, thickness, notch,
  orientation and doping ranges.[^wiki-wafer]
* [Wikipedia, *Czochralski method*](<https://en.wikipedia.org/wiki/Czochralski_method>).[^wiki-cz]
* [Wikipedia, *Silicon*](<https://en.wikipedia.org/wiki/Silicon>) — the melting point.[^wiki-si]
* [Wikipedia, *Float-zone silicon*](<https://en.wikipedia.org/wiki/Float-zone_silicon>).[^wiki-fz]
* [Wikipedia, *Monocrystalline silicon*](<https://en.wikipedia.org/wiki/Monocrystalline_silicon>).[^wiki-monosi]
* [Wikipedia, *Miller index*](<https://en.wikipedia.org/wiki/Miller_index>).[^wiki-miller]
* [Wikipedia, *Epitaxy*](<https://en.wikipedia.org/wiki/Epitaxy>).[^wiki-epitaxy]
* [Wikipedia, *Latch-up*](<https://en.wikipedia.org/wiki/Latch-up>).[^wiki-latchup]
* [Wikipedia, *SkyWater Technology*](<https://en.wikipedia.org/wiki/SkyWater_Technology>) — fab history and 200 mm
  capacity.[^wiki-skywater]
* [Plummer, Deal and Griffin, *Silicon VLSI Technology*](<https://openlibrary.org/isbn/9780130850379>) — ch. 3
  ("Crystal Growth, Wafer Fabrication and Basic Properties of Silicon
  Wafers") and ch. 4 ("Semiconductor Manufacturing — Clean Rooms, Wafer
  Cleaning and Gettering").[^txt-01]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) —
  ch. 1 ("Silicon: Single Crystal Growth and Wafer Preparation") and
  ch. 5 ("Silicon Epitaxial Growth").[^txt-02]
* [Quirk and Serda, *Semiconductor Manufacturing Technology*](<https://openlibrary.org/isbn/9780130815200>) —
  ch. 4.[^txt-07]
* [Xiao, *Introduction to Semiconductor Manufacturing Technology*](<https://doi.org/10.1117/3.924283>) —
  ch. 4.[^txt-08]

### Deep dive

* [Zulehner, *J. Cryst. Growth* 1983](<https://doi.org/10.1016/0022-0248(83)90051-9>) — a wafer-maker's review of
  Czochralski silicon growth: pulling, oxygen and carbon incorporation,
  dopant segregation.[^zulehner-1983]
* [Dash, *JAP* 1959](<https://doi.org/10.1063/1.1702390>) — the "Dash neck" technique that gives
  dislocation-free CZ crystals.[^dash-1959]
* [Shimura, *Semiconductor Silicon Crystal Technology*](<https://openlibrary.org/isbn/9780126400458>) — the standard
  monograph on crystal growth, wafer preparation, oxygen and defect
  characterisation.[^shimura-1989]
* [Voronkov, *J. Cryst. Growth* 1982](<https://doi.org/10.1016/0022-0248(82)90386-4>) — the v/G theory of vacancy- versus
  interstitial-rich growth that governs grown-in defects.[^voronkov-1982]
* [Falster and Voronkov, *Mater. Sci. Eng. B* 2000](<https://doi.org/10.1016/S0921-5107(99)00439-0>) — engineering of
  intrinsic point defects in crystals and wafers, the basis of
  "perfect silicon" and controlled precipitation.[^falster-2000]
* [Ryuta et al., *JJAP* 1990](<https://doi.org/10.1143/JJAP.29.L1947>) — the discovery of crystal-originated pits
  (COPs) revealed by {term}`SC-1` cleaning.[^ryuta-1990]
* [Borghesi et al., *JAP* 1995](<https://doi.org/10.1063/1.359479>) — a long review of oxygen precipitation in
  silicon.[^borghesi-1995]
* [Myers, Seibt and Schröter, *JAP* 2000](<https://doi.org/10.1063/1.1289273>) — review of the mechanisms of
  transition-metal gettering.[^myers-2000]
* [Kang and Schroder, *JAP* 1989](<https://doi.org/10.1063/1.342714>) — phosphorus-diffusion, argon-implant
  and nickel-film gettering experiments (oxidation does not getter), and
  a segregation model.[^kang-1989]
* [Falster et al. (MEMC), US 5,994,761](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5994761>) — the "magic denuded zone"
  rapid-thermal treatment that sets precipitation behaviour without an
  oxygen out-diffusion anneal.[^pat-mdz-memc]
* [Srinivasan, *JES* 1980](<https://doi.org/10.1149/1.2129895>) — autodoping during silicon epitaxy, the
  main process problem of p/p⁺ epi wafers.[^srinivasan-1980]
* [Troutman, *Latchup in CMOS Technology*](<https://doi.org/10.1007/978-1-4757-1887-4>) — the monograph on the
  parasitic thyristor and the substrate choices that tame
  it.[^troutman-1986]
* [Bean, *IEEE TED* 1978](<https://doi.org/10.1109/T-ED.1978.19250>) — crystal-plane behaviour of silicon in
  anisotropic etching.[^bean-1978]
* [Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology*](<https://openlibrary.org/isbn/9781574446753>) — ch. 1–3 on silicon materials.[^txt-09]
* [MIT OpenCourseWare 6.774](<https://ocw.mit.edu/courses/6-774-physics-of-microfabrication-front-end-processing-fall-2004/>) — lecture notes on crystal growth, point
  defects and gettering.[^ocw-6774]

<!-- footnotes -->

[^wiki-wafer]: Wikipedia, *Wafer (electronics)*.
    <https://en.wikipedia.org/wiki/Wafer_(electronics)>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^semi-m1]: SEMI, *SEMI M1 — Specification for Polished Single Crystal
    Silicon Wafers*, SEMI Standards store listing, accessed
    2026-09-18.
    <https://store-us.semi.org/products/m00100-semi-m1-specification-for-polished-single-crystal-silicon-wafers>
[^semi-m62]: SEMI M62, *Specification for Silicon Epitaxial Wafers*,
    SEMI.
    <https://store-us.semi.org/products/m06200-semi-m62-specification-for-silicon-epitaxial-wafers>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^pdk-01]: SkyWater PDK Authors, *SkyWater SKY130 PDK documentation*.
    <https://skywater-pdk.readthedocs.io/en/main/>
[^wiki-si]: Wikipedia, *Silicon*. <https://en.wikipedia.org/wiki/Silicon>
[^wiki-cz]: Wikipedia, *Czochralski method*.
    <https://en.wikipedia.org/wiki/Czochralski_method>
[^wiki-fz]: Wikipedia, *Float-zone silicon*.
    <https://en.wikipedia.org/wiki/Float-zone_silicon>
[^wiki-seh]: Wikipedia, *Shin-Etsu Chemical*.
    <https://en.wikipedia.org/wiki/Shin-Etsu_Chemical>
[^wiki-sumco]: Wikipedia, *SUMCO*. <https://en.wikipedia.org/wiki/SUMCO>
[^wiki-memc]: Wikipedia, *MEMC Electronic Materials*.
    <https://en.wikipedia.org/wiki/MEMC_Electronic_Materials>
[^wiki-siltronic]: Wikipedia, *Siltronic*.
    <https://en.wikipedia.org/wiki/Siltronic>
[^wiki-gw]: Wikipedia, *GlobalWafers*.
    <https://en.wikipedia.org/wiki/GlobalWafers>
[^wiki-asm]: Wikipedia, *ASM International*.
    <https://en.wikipedia.org/wiki/ASM_International>
[^wiki-amat]: Wikipedia, *Applied Materials*.
    <https://en.wikipedia.org/wiki/Applied_Materials>
[^wiki-kla]: Wikipedia, *KLA Corporation*.
    <https://en.wikipedia.org/wiki/KLA_Corporation>
[^wiki-monosi]: Wikipedia, *Monocrystalline silicon*.
    <https://en.wikipedia.org/wiki/Monocrystalline_silicon>
[^wiki-miller]: Wikipedia, *Miller index*.
    <https://en.wikipedia.org/wiki/Miller_index>
[^wiki-epitaxy]: Wikipedia, *Epitaxy*.
    <https://en.wikipedia.org/wiki/Epitaxy>
[^wiki-latchup]: Wikipedia, *Latch-up*.
    <https://en.wikipedia.org/wiki/Latch-up>
[^wiki-skywater]: Wikipedia, *SkyWater Technology*.
    <https://en.wikipedia.org/wiki/SkyWater_Technology>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^txt-08]: H. Xiao, *Introduction to Semiconductor Manufacturing
    Technology*, 2nd ed., SPIE Press, 2012, ISBN 978-0-8194-9092-6.
    <https://doi.org/10.1117/3.924283>
[^zulehner-1983]: W. Zulehner, "Czochralski growth of silicon", *Journal
    of Crystal Growth* **65**(1–3), 189–213 (1983).
    <https://doi.org/10.1016/0022-0248(83)90051-9>
[^dash-1959]: W. C. Dash, "Growth of Silicon Crystals Free from
    Dislocations", *Journal of Applied Physics* **30**(4), 459–474
    (1959). <https://doi.org/10.1063/1.1702390>
[^shimura-1989]: F. Shimura, *Semiconductor Silicon Crystal Technology*,
    Academic Press, 1989, ISBN 978-0-12-640045-8.
    <https://openlibrary.org/isbn/9780126400458>
[^voronkov-1982]: V. V. Voronkov, "The mechanism of swirl defects
    formation in silicon", *Journal of Crystal Growth* **59**(3),
    625–643 (1982). <https://doi.org/10.1016/0022-0248(82)90386-4>
[^falster-2000]: R. Falster and V. V. Voronkov, "The engineering of
    intrinsic point defects in silicon wafers and crystals", *Materials
    Science and Engineering: B* **73**(1–3), 87–94 (2000).
    <https://doi.org/10.1016/S0921-5107(99)00439-0>
[^ryuta-1990]: J. Ryuta, E. Morita, T. Tanaka and Y. Shimanuki,
    "Crystal-Originated Singularities on Si Wafer Surface after SC1
    Cleaning", *Japanese Journal of Applied Physics* **29**(11A), L1947
    (1990). <https://doi.org/10.1143/JJAP.29.L1947>
[^borghesi-1995]: A. Borghesi, B. Pivac, A. Sassella and A. Stella,
    "Oxygen precipitation in silicon", *Journal of Applied Physics*
    **77**(9), 4169–4244 (1995). <https://doi.org/10.1063/1.359479>
[^myers-2000]: S. M. Myers, M. Seibt and W. Schröter, "Mechanisms of
    transition-metal gettering in silicon", *Journal of Applied Physics*
    **88**(7), 3795–3819 (2000). <https://doi.org/10.1063/1.1289273>
[^kang-1989]: J. S. Kang and D. K. Schroder, "Gettering in silicon",
    *Journal of Applied Physics* **65**(8), 2974–2985 (1989).
    <https://doi.org/10.1063/1.342714>
[^pat-mdz-memc]: R. Falster, M. Cornara, D. Gambaro and M. Olmo (MEMC
    Electronic Materials), *Ideal oxygen precipitating silicon wafers
    and oxygen out-diffusion-less process therefor*, US 5,994,761 A,
    granted 1999-11-30.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5994761>
[^srinivasan-1980]: G. R. Srinivasan, "Autodoping Effects in Silicon
    Epitaxy", *Journal of The Electrochemical Society* **127**(6),
    1334–1342 (1980). <https://doi.org/10.1149/1.2129895>
[^troutman-1986]: R. R. Troutman, *Latchup in CMOS Technology: The
    Problem and Its Cure*, Kluwer Academic Publishers, 1986,
    ISBN 978-0-89838-215-7. <https://doi.org/10.1007/978-1-4757-1887-4>
[^bean-1978]: K. E. Bean, "Anisotropic etching of silicon", *IEEE
    Transactions on Electron Devices* **25**(10), 1185–1193 (1978).
    <https://doi.org/10.1109/T-ED.1978.19250>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007,
    ISBN 978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^ocw-6774]: MIT OpenCourseWare, *6.774 Physics of Microfabrication:
    Front End Processing*, Fall 2004 (lecture notes on oxidation,
    diffusion, implantation and annealing).
    <https://ocw.mit.edu/courses/6-774-physics-of-microfabrication-front-end-processing-fall-2004/>
