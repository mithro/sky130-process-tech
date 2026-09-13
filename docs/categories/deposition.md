(category-deposition)=
# Thin-film deposition

## What this class of step does

Deposition steps *add* a layer of material onto the wafer surface,
covering everything that is there. Almost every other step in the flow
either patterns a deposited film, implants through one, or polishes one
back. In a 130 nm aluminium-interconnect process like SKY130, the
deposited films are: silicon nitride ({term}`STI` {term}`hard mask`, gate cap, sidewall
{term}`spacers <spacer>`, etch stops and final passivation); silicon dioxide in several
flavours (STI trench fill, spacer oxide, {term}`PSG`, inter-level
dielectrics and capping oxides); amorphous or polycrystalline silicon
(the gate and resistor layer); titanium and titanium nitride (contact
liners and barriers); tungsten (contact and via plugs); aluminium–copper
alloy (the five wiring levels); titanium–tungsten (anti-reflective caps
and capacitor electrodes); and silicon {term}`oxynitride` (MiM capacitor
dielectric and anti-reflective layers).

Precisely, the films are grown by one of two families of technique.
*Chemical vapour deposition* ({term}`CVD`) feeds gaseous precursors into
a heated, low-pressure chamber, where they react on the surface (and, in
plasma variants, are pre-dissociated by an RF discharge) to leave a
solid film and volatile by-products.[^wiki-cvd] *Physical vapour
deposition* ({term}`PVD`) knocks atoms off a solid target with argon
ions from a magnetron plasma and lets them condense on the
wafer.[^wiki-sputter] The choice between them is set by the material
(metals are sputtered; dielectrics, silicon and tungsten are grown by
CVD), by the temperature the wafer can tolerate at that point in the
flow (typically below about 450 °C once aluminium is present)[^txt-02],
and by how conformally the film must coat holes and steps.

## Physics and engineering background

### Growth regimes and conformality

A CVD reaction proceeds in series: reactant transport through the
boundary layer to the surface, adsorption, surface reaction and
desorption of by-products. At low temperature the surface reaction is
the bottleneck and the rate follows an Arrhenius law, {math}`R \propto
e^{-E_A/kT}`; at high temperature transport limits the rate and it
becomes nearly temperature-independent. Films deposited in the
surface-reaction-limited regime are conformal, because reactants reach
every surface at the same concentration and have time to migrate before
reacting; films deposited in the transport-limited regime are thicker on
exposed corners and thinner in recesses, and can pinch off narrow gaps
leaving voids.[^txt-01][^ohring-2002] Conformality is quantified as
{term}`step coverage`, and the {term}`aspect ratio` of the feature being
coated is the governing parameter. Low sticking coefficients (as in
{term}`LPCVD` {term}`TEOS` oxide and nitride) give the best step
coverage; {term}`PECVD` and PVD films have sticking coefficients near unity and
poor bottom coverage in deep holes.

### LPCVD

Low-pressure CVD runs at 0.1–1 Torr in a hot-wall batch furnace, which
deposits on 100 or more wafers at once with excellent uniformity
because the low pressure makes the gas-phase diffusion length long
compared with the wafer spacing.[^txt-01] The
standard LPCVD films and their typical industry conditions are:

* **Polysilicon or amorphous silicon** from silane, SiH₄ → Si + 2H₂, at
  roughly 580–650 °C. Below about 580 °C the film deposits amorphous and
  crystallises during later anneals, giving a smoother surface and finer
  grain, which helps gate etch and {term}`CD` control; SKY130's gate is
  deposited amorphous ({ref}`SAGD <step-048>`). Phosphine or diborane
  can be co-flowed for in-situ doping, but gates in a dual-work-function
  CMOS process are usually implanted instead.[^wiki-poly][^txt-01]
* **Silicon nitride** from dichlorosilane and ammonia, 3SiH₂Cl₂ + 4NH₃ →
  Si₃N₄ + 6HCl + 6H₂, at roughly 700–800 °C. The film is dense, highly
  conformal and under tensile stress of order 1 GPa, which limits its
  thickness before cracking or wafer bowing.[^wiki-sin][^txt-02] Used
  for the STI polish-stop/hard mask ({ref}`ISONIT <step-003>`), the gate
  cap ({ref}`GATENIT <step-058>`) and the spacer ({ref}`SPNIT
  <step-076>`).
* **TEOS oxide**, Si(OC₂H₅)₄ → SiO₂ + by-products, at roughly 650–750
  °C; and **{term}`HTO`** (high-temperature oxide) from SiH₂Cl₂ + N₂O at 800–900
  °C, both temperatures being typical industry values.[^txt-01][^txt-02]
  Both are conformal and are used for spacers and liners.[^wiki-teos]

### PECVD

Plasma-enhanced CVD uses a 13.56 MHz (often mixed with a low-frequency
component) capacitive discharge to dissociate the precursors so that
deposition proceeds at 250–400 °C, low enough for wafers that already
carry aluminium.[^wiki-pecvd] Typical films:

* **Oxide** from SiH₄ + N₂O, or from TEOS + O₂ (better conformality and
  lower particle count). PECVD TEOS oxide is the workhorse inter-level
  dielectric and capping oxide of an aluminium {term}`BEOL`; the ITRS 2001
  notes that fluorinated versions ("Low κ FSG (κ = 3.7)") had "been in
  production since the 250 nm node".[^itrs-02]
* **Nitride** from SiH₄ + NH₃ + N₂, hydrogen-rich (typically 10–25 at.%
  H)[^txt-02], used as an etch stop and as the final scratch- and
  moisture-resistant passivation ({ref}`NTSD <step-167>`).
* **Silicon oxynitride** SiOₓNᵧ from SiH₄ + N₂O + NH₃, whose
  refractive index can be tuned between oxide and nitride; used as a
  dielectric anti-reflective coating under photoresist and as the
  dielectric of MiM capacitors ({ref}`CAPILD <step-135>`).
* **PSG** by adding PH₃ to an oxide deposition, typically 4–8 wt.% P
  (a typical industry range),[^txt-02] which getters
  sodium and, in older flows, could be reflowed.[^wiki-psg]

The ion bombardment inherent in PECVD lets film stress be tuned from
compressive to tensile by adjusting the low-frequency power, a
freedom LPCVD lacks.[^lieberman-2005]

### HDP-CVD

High-density-plasma CVD combines an inductively coupled SiH₄/O₂/Ar
plasma with an RF bias on the wafer, so that deposition and argon
sputtering occur at once. Sputtering preferentially removes material
from the corners of a gap, which would otherwise close first, so gaps of
aspect ratio around 3:1 fill without voids in a single step. The
deposition-to-sputter ratio is the key recipe knob, and the bias makes
the process hot (wafer temperature is controlled by helium backside
cooling on an electrostatic chuck). {term}`HDP-CVD` oxide is the usual STI fill
at this node and is the likely process behind {ref}`FILOX <step-011>`;
in many aluminium processes it also fills the gaps between metal lines
before a capping oxide and {term}`CMP`.[^txt-01][^txt-09]

### PVD (sputtering)

In magnetron sputtering an argon plasma is confined near the target by
crossed electric and magnetic fields; Ar⁺ ions strike the target and
eject atoms with a few eV of energy that travel line-of-sight to the
wafer.[^wiki-sputter] Because the flux is directional and the sticking
coefficient is about one, step coverage in a contact hole is poor, and
film microstructure follows Thornton's zone model with pressure and
homologous temperature.[^ohring-2002] The metallisation films of an
aluminium BEOL are:

* **Aluminium–copper**, typically Al with 0.5–1 wt.% Cu, sputtered at
  150–400 °C. The copper segregates to grain boundaries and greatly
  improves electromigration lifetime relative to pure
  aluminium.[^wiki-em][^txt-02]
* **Titanium** as an adhesion/contact layer and **titanium nitride** by
  reactive sputtering of Ti in Ar/N₂. A conductive TiN underlayer keeps
  a line open after an Al void forms, and it was on Al stripes over TiN
  that Blech discovered the critical-length ("Blech length")
  effect;[^blech-1976] on top of Al it serves as an anti-reflective
  coating for lithography and as a diffusion barrier.[^wiki-tin]
* **Titanium–tungsten** (Ti:W, "typically composed of 10 wt% of titanium
  and the balance of tungsten"),[^pat-tiw-hitachi] a barrier and
  anti-reflective cap used in some aluminium stacks and as a capacitor
  electrode.
* **Cobalt or titanium** for {term}`salicide` formation
  ({ref}`category-anneal`).

For contact and via liners, ordinary sputtering cannot coat the bottom
of a hole of aspect ratio above about 2:1. Ionised-metal-plasma
({term}`IMP`) PVD adds a secondary RF coil that ionises the sputtered
metal; a wafer bias then draws the ions vertically down the hole, so
bottom coverage rises to tens of per cent. IMP Ti/TiN is the standard
liner under CVD tungsten at this node (see, for example, an Applied
Materials IMP patent),[^txt-09][^pat-imp-amat] and this reference
reads SKY130's contact liner as titanium followed by IMP TiN, with the
titanium route (collimated or ionised) not public
({ref}`TI/TIN1 <step-097>`), and its via liners as IMP TiN
({ref}`TIN2 <step-109>`).

### CVD tungsten

Tungsten plugs are grown from tungsten hexafluoride. A thin nucleation
layer is deposited by silane reduction, 2WF₆ + 3SiH₄ → 2W + 3SiF₄ + 6H₂,
then the bulk fill by hydrogen reduction, WF₆ + 3H₂ → W + 6HF, at
roughly 400–450 °C and a few tens of Torr.[^wiki-wf6][^txt-01] CVD W is
almost perfectly conformal, so it fills contacts from the sidewalls
inward and leaves only a small seam. The TiN liner is essential: WF₆
attacks bare silicon and titanium, and HF by-product would otherwise
etch oxide. The blanket film is then removed from the field by CMP
({ref}`category-cmp`), leaving the {term}`W plug`.

### Film thicknesses in SKY130

The SKY130 PDK's design-rule assumptions page publishes the nominal
thicknesses used for antenna-ratio calculations: poly 0.18 µm, local
interconnect (LI1) 0.1 µm, metal 1 and metal 2 0.35 µm, metal 3 and
metal 4 0.8 µm (2 µm in the thick-metal flow options), metal 5 1.2 µm or
2 µm depending on the flow option, an oxide spacer of 0.05 µm and a
pre-LI {term}`ILD` of 0.5 µm.[^pdk-03] These are the antenna-rule assumptions;
the PDK's process stack diagram labels the same conductors 0.36, 0.845
and 1.26 µm.[^pdk-04] We take these as the approximate deposited (and,
for the dielectrics, post-CMP) targets that the deposition steps below
must hit.

## Typical equipment

* **{ref}`LPCVD furnaces <machine-vertical-furnace-lpcvd>`**: the same vertical batch furnaces as for oxidation,
  fitted with silane, DCS, ammonia and TEOS (bubbler or liquid
  injection) delivery and a vacuum pump train — ASM A400 ("LPCVD
  processes like doped silicon and silicon nitride films"),[^asm-a400]
  TEL Alpha-8, Aviza/Thermco.
* **{ref}`PECVD <machine-pecvd>`**: single-wafer multi-station or multi-chamber cluster tools —
  Novellus Concept One/Concept Two Sequel (Novellus's dielectric line
  comprised "Concept One, Concept One Maxus, Concept Two Sequel, Concept
  Two Dual Sequel, Concept Two Sequel-S"),[^novellus-history] Applied
  Materials Producer ("Twin-Chamber" modules, two single-wafer chambers
  per unit)[^amat-10k] and Centura DxZ.
* **{ref}`HDP-CVD <machine-hdp-cvd>`**: Novellus SPEED (completed in 1995, "a high-density plasma
  system with simpler, more cost-effective solutions for inter-metal
  dielectric films")[^novellus-history] and Applied Materials Ultima
  HDP-CVD Centura, "the industry's first production-ready HDP-CVD
  system".[^amat-1997]
* **{ref}`PVD <machine-pvd-cluster-tool>`**: Applied Materials Endura ("Applied Materials entered the PVD
  market in April 1990 with the Endura PVD system", with Ti/TiN liner
  options for "sub-0.25-micron, high aspect ratio contact and via
  structures" added in 1996),[^amat-1997][^amat-endura] with degas,
  pre-clean, Ti, IMP Ti/TiN, Al–Cu and TiN chambers on one vacuum
  mainframe; Novellus INOVA; earlier Varian and MRC (Materials Research
  Corporation) sputterers.
* **{ref}`CVD tungsten <machine-tungsten-cvd>`**: Novellus Concept Two Altus ("metal solutions
  (Concept One-W, Concept Two-Altus, and Concept Two-Dual
  Altus)")[^novellus-history] and Applied Materials Centura WxZ.
* **Metrology**: {ref}`ellipsometry and reflectometry <machine-film-thickness-metrology>` for dielectric
  thickness; {term}`four-point probe` {term}`sheet resistance` for metals
  ({ref}`machine-sheet-resistance-metrology`); stress gauges (wafer-bow); {ref}`particle counters <machine-defect-inspection>`
  on blanket monitor wafers.

## Typical consumables

* **Silicon precursors**: silane (SiH₄), dichlorosilane (SiH₂Cl₂),
  TEOS (liquid, vaporised).
* **Reactants**: ammonia (NH₃), nitrous oxide (N₂O), oxygen (O₂),
  nitrogen (N₂), hydrogen (H₂), argon (Ar), helium (He, backside
  cooling and dilution).
* **Dopant gases**: phosphine (PH₃) for PSG and doped poly; diborane
  (B₂H₆).
* **Tungsten**: tungsten hexafluoride (WF₆); silane for nucleation;
  H₂.
* **Chamber cleaning**: NF₃ or C₂F₆/O₂ plasma cleans for PECVD and
  HDP chambers; in-situ NF₃ cleans for LPCVD tubes.
* **Sputter targets**: Al–Cu (0.5–1 wt.% Cu), Ti, Ti:W (10 wt.% Ti), Co;
  argon and nitrogen process gases; target lifetime is tracked in kWh.
* **Hardware**: quartz tubes and boats, showerheads, shields and
  clamp rings, electrostatic chucks, and vacuum-pump oil or dry pumps.

## Steps in this category

| Step | Code | Name |
|------|------|------|
| 3 | {ref}`ISONIT <step-003>` | Iso nitride deposition |
| 11 | {ref}`FILOX <step-011>` | Fill oxide deposition |
| 48 | {ref}`SAGD <step-048>` | Single a-Si gate deposition |
| 58 | {ref}`GATENIT <step-058>` | Gate poly nitride deposition |
| 59 | {ref}`POC <step-059>` | Protective oxide cap |
| 76 | {ref}`SPNIT <step-076>` | Spacer nitride deposition |
| 80 | {ref}`SPOX <step-080>` | Spacer oxide deposition |
| 89 | {ref}`PSG <step-089>` | Sacrificial PSG deposition |
| 91 | {ref}`NCAPOX <step-091>` | Cap oxide deposition |
| 97 | {ref}`TI/TIN1 <step-097>` | IMP Ti/TiN deposition |
| 99 | {ref}`WDEP <step-099>` | Blanket CVD W deposition |
| 101 | {ref}`LITIN <step-101>` | TiN deposition |
| 104 | {ref}`LINIT <step-104>` | Nitride cap deposition |
| 105 | {ref}`NILD2 <step-105>` | ILD oxide deposition |
| 109 | {ref}`TIN2 <step-109>` | IMP TiN deposition |
| 110 | {ref}`WDEP2 <step-110>` | Blanket CVD W deposition |
| 112 | {ref}`TIAL6 <step-112>` | CoTi/AlCu/TiW deposition |
| 115 | {ref}`NILD3 <step-115>` | ILD oxide deposition |
| 117 | {ref}`NCAPOX3 <step-117>` | CAPOX deposition |
| 120 | {ref}`TIN3 <step-120>` | IMP TiN deposition |
| 121 | {ref}`WDEP3 <step-121>` | Blanket CVD W deposition |
| 123 | {ref}`TIAL12 <step-123>` | AlCu 2/TiW deposition |
| 126 | {ref}`NILD4 <step-126>` | ILD oxide deposition |
| 128 | {ref}`NCAPOX4 <step-128>` | CAPOX deposition |
| 131 | {ref}`TIN4 <step-131>` | IMP TiN deposition |
| 132 | {ref}`WDEP4 <step-132>` | Blanket CVD W deposition |
| 134 | {ref}`WTIAL3 <step-134>` | AlCu 2/TiW deposition |
| 135 | {ref}`CAPILD <step-135>` | Capacitor ILD oxynitride deposition |
| 136 | {ref}`CAPTIW1 <step-136>` | Capacitor TiW deposition |
| 141 | {ref}`NILD5 <step-141>` | ILD oxide deposition |
| 143 | {ref}`NCAPOX5 <step-143>` | CAPOX deposition |
| 146 | {ref}`TIN5 <step-146>` | IMP TiN deposition |
| 147 | {ref}`WDEP5 <step-147>` | Blanket CVD W deposition |
| 149 | {ref}`WTIAL4 <step-149>` | AlCu 2/TiW deposition |
| 150 | {ref}`CAPILD2 <step-150>` | Capacitor ILD oxynitride deposition |
| 151 | {ref}`CAPTIW2 <step-151>` | Capacitor TiW deposition |
| 156 | {ref}`NILD6 <step-156>` | ILD oxide deposition |
| 158 | {ref}`NCAPOX6 <step-158>` | CAPOX deposition |
| 161 | {ref}`WTIAL5 <step-161>` | AlCu 2/TiW deposition |
| 164 | {ref}`NFUSOX <step-164>` | Fuse oxide deposition |
| 167 | {ref}`NTSD <step-167>` | Nitride topside deposition |

## References

### Cross-check

* SkyWater PDK, *Criteria & Assumptions* — the nominal film
  thicknesses used for antenna calculations.[^pdk-03]
* SkyWater PDK, process stack diagram (`metal_stack.svg`) — conductor
  thicknesses 0.36, 0.845 and 1.26 µm.[^pdk-04]
* ITRS 2001, *Interconnect* — FSG in production since the 250 nm node,
  and the dielectric roadmap.[^itrs-02]
* Blech, *JAP* 1976 — the critical-length effect measured on Al lines
  over TiN.[^blech-1976]
* Applied Materials, *Endura PVD* product page.[^amat-endura]
* Applied Materials, Form 10-K (fiscal 2003) — Centura, Endura and
  Producer platform descriptions.[^amat-10k]
* Encyclopedia.com, *Novellus Systems, Inc.* — the Concept One/Two,
  Sequel, SPEED and Altus product history.[^novellus-history]
* ASM International, A400 DUO press release — the A400's LPCVD
  processes.[^asm-a400]
* Applied Materials, US 6,350,353 — alternating IMP and conventional
  sputtering to improve sidewall coverage.[^pat-imp-amat]
* Hitachi Metals, US 5,160,534 — the 10 wt.% Ti composition of Ti:W
  sputter targets.[^pat-tiw-hitachi]

### High-level understanding

* Wikipedia, *Chemical vapor deposition*.[^wiki-cvd]
* Wikipedia, *Plasma-enhanced chemical vapor deposition*.[^wiki-pecvd]
* Wikipedia, *Sputter deposition*.[^wiki-sputter]
* Wikipedia, *Physical vapor deposition*.[^wiki-pvd]
* Wikipedia, *Polycrystalline silicon*.[^wiki-poly]
* Wikipedia, *Silicon nitride*.[^wiki-sin]
* Wikipedia, *Tetraethyl orthosilicate*.[^wiki-teos]
* Wikipedia, *Phosphosilicate glass*.[^wiki-psg]
* Wikipedia, *Titanium nitride*.[^wiki-tin]
* Wikipedia, *Tungsten hexafluoride*.[^wiki-wf6]
* Wikipedia, *Electromigration*.[^wiki-em]
* Wikipedia, *Thin film*.[^wiki-thinfilm]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — ch. 9 ("Thin
  Film Deposition") and ch. 11 ("Back-End Technology").[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  ch. 6 ("Chemical Vapor Deposition of Amorphous and Polycrystalline
  Films") and ch. 11 ("Aluminum Thin Films and Physical Vapor
  Deposition").[^txt-02]
* Campbell, *Fabrication Engineering at the Micro- and Nanoscale* —
  ch. 12 and 13.[^campbell-2013]
* Xiao, *Introduction to Semiconductor Manufacturing Technology* —
  ch. 10 and 11.[^txt-08]

### Deep dive

* Ohring, *Materials Science of Thin Films* — nucleation, growth
  regimes, step coverage and the structure-zone model.[^ohring-2002]
* Lieberman and Lichtenberg, *Principles of Plasma Discharges and
  Materials Processing* — ch. 16 on plasma-enhanced deposition and
  ion-bombardment control of film stress.[^lieberman-2005]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — chapters on CVD, PVD, HDP-CVD and IMP
  liners.[^txt-09]
* Bohr, IEDM 1995 — why interconnect, not the transistor, limits
  performance, motivating the metallisation stack.[^bohr-1995]
* Broadbent and Ramiller, *JES* 1984 — WF₆/H₂ and WF₆/SiH₄ kinetics
  behind CVD tungsten fill.[^rev-03]
* Kaanta et al. (IBM), IEDM 1987 — the tungsten-stud plus planarisation
  wiring scheme that became the standard plug process.[^kaanta-1987]
* Rossnagel and Hopwood, *JVST B* 1994 — the first ionised-magnetron
  (IMP) metal deposition experiments.[^rossnagel-1994]
* Rossnagel, *JVST B* 1998 — review of collimated and ionised PVD for
  liners and barriers.[^rossnagel-1998]
* Thornton, *JVST* 1974 — the structure-zone diagram for sputtered films
  versus pressure and temperature.[^thornton-1974]
* Raupp, Cale and Hey, *JVST B* 1992 — reaction kinetics of PECVD TEOS
  oxide and their effect on step coverage.[^raupp-1992]
* Adams and Capio, *JES* 1979 — LPCVD oxide deposition, including TEOS
  and doped glasses.[^adams-1979]
* Kamins, *JES* 1980 — structure and properties of LPCVD silicon films
  as a function of deposition temperature.[^kamins-1980]
* Ames, d'Heurle and Horstmann, *IBM J. Res. Dev.* 1970 — the original
  demonstration that copper doping suppresses aluminium
  electromigration.[^ames-1970]
* Nguyen, *IBM J. Res. Dev.* 1999 — review of HDP-CVD dielectrics,
  gap-fill and the deposition-to-sputter ratio.[^nguyen-1999]
* Nishimura et al., *JJAP* 2002 — HDP-CVD gap-fill modelling
  demonstrated on 0.13 µm STI.[^nishimura-2002]
* Novellus, SPEED Max press release — a vendor's description of HDP
  gap-fill knobs (deposition, etch and sputter-to-deposition
  ratio).[^lam-speed]
* Seshan (ed.), *Handbook of Thin-Film Deposition Processes and
  Techniques* — chapter-per-technique reference on CVD, PECVD, PVD and
  their equipment.[^seshan-2002]
* Applied Materials, 1997 Annual Report — Centura and Endura platform
  history.[^amat-1997]
* MIT OpenCourseWare 6.152J — lecture notes on CVD and PVD
  fundamentals.[^ocw-6152]

<!-- footnotes -->

[^wiki-cvd]: Wikipedia, *Chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Chemical_vapor_deposition>
[^wiki-sputter]: Wikipedia, *Sputter deposition*.
    <https://en.wikipedia.org/wiki/Sputter_deposition>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^ohring-2002]: M. Ohring, *Materials Science of Thin Films*, 2nd ed.,
    Academic Press, 2002.
    <https://doi.org/10.1016/B978-0-12-524975-1.X5000-9>
[^wiki-poly]: Wikipedia, *Polycrystalline silicon*.
    <https://en.wikipedia.org/wiki/Polycrystalline_silicon>
[^wiki-sin]: Wikipedia, *Silicon nitride*.
    <https://en.wikipedia.org/wiki/Silicon_nitride>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^wiki-teos]: Wikipedia, *Tetraethyl orthosilicate*.
    <https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^itrs-02]: International Technology Roadmap for Semiconductors, *2001
    Edition: Interconnect*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Interconnect.pdf>
[^wiki-psg]: Wikipedia, *Phosphosilicate glass*.
    <https://en.wikipedia.org/wiki/Phosphosilicate_glass>
[^lieberman-2005]: M. A. Lieberman and A. J. Lichtenberg, *Principles of
    Plasma Discharges and Materials Processing*, 2nd ed., Wiley, 2005,
    ISBN 978-0-471-72001-0. <https://doi.org/10.1002/0471724254>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007,
    ISBN 978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^wiki-em]: Wikipedia, *Electromigration*.
    <https://en.wikipedia.org/wiki/Electromigration>
[^blech-1976]: I. A. Blech, "Electromigration in thin aluminum films on
    titanium nitride", *Journal of Applied Physics* **47**(4), 1203–1208
    (1976). <https://doi.org/10.1063/1.322842>
[^wiki-tin]: Wikipedia, *Titanium nitride*.
    <https://en.wikipedia.org/wiki/Titanium_nitride>
[^pat-tiw-hitachi]: Hitachi Metals, *Titanium-tungsten target material
    for sputtering and manufacturing method therefor*, US 5,160,534 A,
    granted 1992-11-03.
    <https://patents.google.com/patent/US5160534A/en>
[^pat-imp-amat]: P. Gopalraja, S. Edelstein, A. Tepman, P. Ding,
    D. Ghosh and N. Maity (Applied Materials), *Alternate steps of IMP
    and sputtering process to improve sidewall coverage*,
    US 6,350,353 B2, filed 1999-11-24, granted 2002-02-26.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6350353>
[^wiki-wf6]: Wikipedia, *Tungsten hexafluoride*.
    <https://en.wikipedia.org/wiki/Tungsten_hexafluoride>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^asm-a400]: ASM International, *ASM International N.V. launches A400
    DUO vertical furnace system*, press release, 2019-11-11.
    <https://www.asm.com/press-releases/asm-international-nv-launches-a400-duo-vertical-furnace-system-1944469>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.*
    (company history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^amat-10k]: Applied Materials, Inc., Form 10-K for fiscal 2003
    (platform descriptions: Centura, Endura, Endura SL, Producer).
    <https://www.sec.gov/Archives/edgar/data/6951/000089161804000093/f95058e10vk.htm>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report*.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^amat-endura]: Applied Materials, *Endura PVD*, product page.
    <https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html>
[^wiki-pvd]: Wikipedia, *Physical vapor deposition*.
    <https://en.wikipedia.org/wiki/Physical_vapor_deposition>
[^wiki-thinfilm]: Wikipedia, *Thin film*.
    <https://en.wikipedia.org/wiki/Thin_film>
[^campbell-2013]: S. A. Campbell, *Fabrication Engineering at the Micro-
    and Nanoscale*, 4th ed., Oxford University Press, 2013,
    ISBN 978-0-19-986122-4. <https://openlibrary.org/isbn/9780199861224>
[^txt-08]: H. Xiao, *Introduction to Semiconductor Manufacturing
    Technology*, 2nd ed., SPIE Press, 2012, ISBN 978-0-8194-9092-6.
    <https://doi.org/10.1117/3.924283>
[^bohr-1995]: M. T. Bohr, "Interconnect scaling — the real limiter to
    high performance ULSI", *IEDM 1995 Technical Digest*, pp. 241–244.
    <https://doi.org/10.1109/IEDM.1995.499187>
[^rev-03]: E. K. Broadbent and C. L. Ramiller, "Selective Low Pressure
    Chemical Vapor Deposition of Tungsten", *Journal of The
    Electrochemical Society* **131**(6), 1427–1433 (1984).
    <https://doi.org/10.1149/1.2115864>
[^kaanta-1987]: C. Kaanta, W. Cote, J. Cronin, K. Holland et al.,
    "Submicron wiring technology with tungsten and planarization", *IEDM
    1987 Technical Digest*, pp. 209–212.
    <https://doi.org/10.1109/IEDM.1987.191389>
[^rossnagel-1994]: S. M. Rossnagel and J. Hopwood, "Metal ion deposition
    from ionized magnetron sputtering discharge", *Journal of Vacuum
    Science & Technology B* **12**(1), 449–453 (1994).
    <https://doi.org/10.1116/1.587142>
[^rossnagel-1998]: S. M. Rossnagel, "Directional and ionized physical
    vapor deposition for microelectronics applications", *Journal of
    Vacuum Science & Technology B* **16**(5), 2585–2608 (1998).
    <https://doi.org/10.1116/1.590242>
[^thornton-1974]: J. A. Thornton, "Influence of apparatus geometry and
    deposition conditions on the structure and topography of thick
    sputtered coatings", *Journal of Vacuum Science and Technology*
    **11**(4), 666–670 (1974). <https://doi.org/10.1116/1.1312732>
[^raupp-1992]: G. B. Raupp, T. S. Cale and H. P. W. Hey, "The role of
    oxygen excitation and loss in plasma-enhanced deposition of silicon
    dioxide from tetraethylorthosilicate", *Journal of Vacuum Science &
    Technology B* **10**(1), 37–45 (1992).
    <https://doi.org/10.1116/1.586361>
[^adams-1979]: A. C. Adams and C. D. Capio, "The Deposition of Silicon
    Dioxide Films at Reduced Pressure", *Journal of The Electrochemical
    Society* **126**(6), 1042–1046 (1979).
    <https://doi.org/10.1149/1.2129171>
[^kamins-1980]: T. I. Kamins, "Structure and Properties of LPCVD Silicon
    Films", *Journal of The Electrochemical Society* **127**(3), 686–690
    (1980). <https://doi.org/10.1149/1.2129733>
[^ames-1970]: I. Ames, F. M. d'Heurle and R. E. Horstmann, "Reduction of
    Electromigration in Aluminum Films by Copper Doping", *IBM Journal
    of Research and Development* **14**(4), 461–463 (1970).
    <https://doi.org/10.1147/rd.144.0461>
[^nguyen-1999]: S. V. Nguyen, "High-density plasma chemical vapor
    deposition of silicon-based dielectric films for integrated
    circuits", *IBM Journal of Research and Development* **43**(1.2),
    109–126 (1999). <https://doi.org/10.1147/rd.431.0109>
[^nishimura-2002]: H. Nishimura, S. Takagi, M. Fujino and N. Nishi,
    "Gap-Fill Process of Shallow Trench Isolation for 0.13 µm
    Technologies", *Japanese Journal of Applied Physics* **41**, Part 1,
    No. 5A, 2886–2893 (2002). <https://doi.org/10.1143/JJAP.41.2886>
[^lam-speed]: Novellus Systems (Lam Research newsroom), *Novellus' SPEED
    Max HDP-CVD Dielectric Gapfill System Extends STI Application to
    32nm*, press release, 2009-10-05.
    <https://newsroom.lamresearch.com/2009-10-05-NOVELLUS-SPEED-R-MAX-HDP-CVD-DIELECTRIC-GAPFILL-SYSTEM-EXTENDS-STI-APPLICATION-TO-32nm>
[^seshan-2002]: K. Seshan (ed.), *Handbook of Thin-Film Deposition
    Processes and Techniques: Principles, Methods, Equipment and
    Applications*, 2nd ed., Noyes Publications / William Andrew, 2002,
    ISBN 978-0-8155-1442-8. <https://openlibrary.org/isbn/9780815514428>
[^ocw-6152]: MIT OpenCourseWare, *6.152J Micro/Nano Processing
    Technology*, Fall 2005 (lecture notes on lithography, etching,
    deposition and CMP).
    <https://ocw.mit.edu/courses/6-152j-micro-nano-processing-technology-fall-2005/>
