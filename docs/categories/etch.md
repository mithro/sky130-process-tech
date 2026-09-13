(category-etch)=
# Etch

## What this class of step does

An etch step removes material selectively: wherever the photoresist
(or a {term}`hard mask`) is open, the exposed film is eaten away down to a
stopping layer, and wherever it is covered, the film stays. Etching is
how the pattern drawn by lithography ({ref}`category-lithography`) is
transferred into the real materials of the chip — nitride, silicon,
oxide, polysilicon, aluminium, titanium nitride. Some etches have no
mask at all and simply remove a film everywhere (a "blanket" etch or
etch-back) or only from the wafer backside.

Precisely, an etch is characterised by four numbers. Its **rate**
(nm/min) sets the process time; its {term}`selectivity`, the ratio of
the rate on the target film to the rate on the mask and on the
underlying stop layer, sets how much {term}`over-etch` can be tolerated; its
{term}`anisotropy`, the ratio of vertical to lateral rate, sets how
faithfully the resist width becomes the etched width; and its
**uniformity** across the wafer and between dense and isolated features
sets how much over-etch is *needed*. A 130 nm process uses two families:
plasma ("dry") etching in a vacuum chamber, which can be highly
anisotropic and is used for every patterned film, and wet chemical
etching in aqueous baths, which is isotropic and is used where a film
must be removed cleanly and gently with very high selectivity — the thin
oxides at {ref}`GOXETCH <step-046>` and {ref}`SACETCH <step-095>`, for
example, which we infer to be wet etches.

In the SKY130 flow there are 27 etch steps: the {term}`STI` nitride and trench
etches, the {term}`SONOS` tunnel/{term}`ONO` stack etches, the gate-oxide wet etch, the
poly gate etch, the {term}`spacer` etch, a nitride cut, the local-interconnect
contact and line etches, the sacrificial-oxide wet etch before
silicidation, the metal contact etch, the five aluminium metal etches,
four via etches, two MiM capacitor etches, a {term}`backside film removal`, and
the final nitride-seal and pad etches.

## Physics and engineering background

### How a plasma etches

A reactive-ion etcher holds the wafer on an RF-driven electrode in a gas
at low pressure. "Plasma is initiated in the system by applying a strong
RF electromagnetic field to the wafer platter. The field is typically
set to a frequency of 13.56 Megahertz, applied at a few hundred watts",
and because electrons are far more mobile than ions the platter charges
to "a large negative voltage on the platter, typically around a few
hundred volts", which accelerates positive ions across the sheath and
onto the wafer normal to its surface.[^wiki-rie] Pressure "is typically
maintained in a range between a few millitorr and a few hundred
millitorr".[^wiki-rie]

Etching then proceeds by a synergy between chemistry and ion
bombardment. Coburn and Winters showed in 1979 that silicon exposed to
XeF₂ *and* an argon-ion beam etches roughly an order of magnitude faster
than under either alone;[^coburn-1979] the ions break bonds, clear
inhibiting films and volatilise reaction products only where they
strike, which is straight down. Steinbrüchel found that the ion-enhanced
etch yield scales as {math}`Y \propto \sqrt{E} - \sqrt{E_{th}}` at low
ion energies.[^steinbruchel-1989] Anisotropy is therefore obtained
either by making the reaction ion-driven or by passivating the sidewalls
with a polymer or oxide that ions remove from the trench floor but not
from the walls.[^flamm-1981][^lieberman-2005]

### Plasma sources

A conventional capacitive {term}`RIE` couples ion density and ion energy through
the one RF supply. High-density sources decouple them: an inductively
coupled ({term}`ICP`; Lam's {term}`TCP`; Applied's "decoupled plasma
source", DPS) coil generates a dense plasma (typically 10¹¹–10¹²
cm⁻³)[^lieberman-2005] at a few millitorr, while a separate
low-frequency bias on the electrostatic chuck sets the ion energy, so
that "the ICP is employed as a high density source of ions which
increases the etch rate" while the bias controls "the energy of ions
bombarding the surface".[^wiki-rie] Low pressure gives a collisionless
sheath and near-vertical ions; low bias limits damage and improves
selectivity. Dielectric etches, which need polymerising chemistries and
higher ion energies, are mostly done in dual-frequency capacitive
reactors (a high frequency for density, a low frequency for bias) such
as Lam's Exelan and Applied's eMxP+.[^donnelly-2013][^nojiri-2015]

### Chemistries by material

The chemistries below are those typical of the node; SKY130's actual
recipes are not public.

* **Silicon and polysilicon** (STI trench {ref}`STIE <step-006>`, gate
  {ref}`P1ME <step-062>`): HBr/Cl₂ with a little O₂, which forms
  volatile SiBrₓ/SiClₓ while a thin SiOₓBrᵧ sidewall film keeps the
  profile vertical; the O₂ also raises selectivity to the gate oxide
  underneath, and the main etch is followed by a {term}`soft-landing <soft landing>` and an
  HBr/O₂ over-etch step with selectivity to SiO₂ of the order of 100:1
  so that a 2–4 nm gate oxide survives.[^nojiri-2015][^txt-01] SF₆ "is
  commonly used for etching silicon" where isotropy is
  acceptable.[^wiki-rie]
* **Silicon dioxide** (contacts {ref}`CTME <step-108>`, vias {ref}`VIME
  <step-119>`, oxide hard masks, the seal-ring opening
  {ref}`NSME <step-166>` (mainly oxide on the reading of that page)):
  fluorocarbons — CF₄, CHF₃, C₄F₈, C₂F₆
  — with Ar and O₂. Fluorine etches oxide as SiF₄ only under ion
  bombardment, while the carbon forms a polymer that deposits on silicon
  and nitride, giving selectivity to the underlying silicon or to a
  nitride etch-stop; the fluorine-to-carbon ratio is the master
  variable.[^flamm-1981][^winters-1992] High-aspect-ratio contacts show
  {term}`ARDE`, etch-stop from polymer build-up, and bowing.
* **Silicon nitride** (STI hard mask {ref}`STINITE <step-005>`, spacer
  {ref}`SPE <step-077>`, nitride cut {ref}`NPCME <step-079>`, pad
  opening {ref}`PDME <step-169>`): CF₄/CHF₃/O₂ or SF₆-based, with the
  fluorocarbon content tuned for selectivity to oxide; the spacer etch
  is an unmasked anisotropic etch-back that leaves nitride only on the
  vertical gate sidewalls and must stop on a thin oxide without
  trenching the silicon.[^txt-01]
* **Aluminium–copper with Ti/TiN or Ti:W caps** (metal 1–5,
  {ref}`MM1E <step-114>` to {ref}`MM5E <step-163>`; the Cypress S8
  qualification report gives a TiW cap on metals 1–3,[^cyp-qtp-113005]
  and this reference describes SKY130's stacks the same way): Cl₂/BCl₃ with N₂ or CHF₃ for sidewall
  passivation. AlCl₃ is volatile at room temperature, so aluminium
  etches spontaneously in chlorine and anisotropy depends entirely on
  the passivation film; BCl₃ scavenges water and reduces the native
  Al₂O₃; copper chlorides are not volatile and are removed by ion
  bombardment; and residual chlorine plus atmospheric moisture corrodes
  the lines, so the etch ends with an in-situ H₂O or O₂/CF₄ passivation
  plasma and an immediate rinse.[^nojiri-2015][^txt-02]
* **Ti:W and TiN** (capacitor top plates {ref}`CAPME <step-138>`,
  {ref}`CAP2ME <step-153>`): fluorine (SF₆, CF₄) or chlorine chemistries
  with high selectivity to the {term}`oxynitride` dielectric beneath.
* **Anti-reflective coatings** ({ref}`TUNARCE <step-036>`): organic {term}`BARC`
  opens in O₂/N₂ or HBr/O₂; inorganic SiON in CF₄-based plasmas.
* **Tungsten** etch-back (an alternative to {term}`CMP` for plugs): SF₆/Ar.

### Wet etching

Wet etches are chemical only, so they are isotropic and can be almost
perfectly selective. Silicon dioxide is removed in dilute hydrofluoric
acid or in {term}`BOE`, a mixture of ammonium fluoride and HF whose
buffering gives "a more stable pH; thus, more stable concentrations of
HF and HF₂⁻, and a more stable etch rate"; a 6:1 mixture of 40 % NH₄F
and 49 % HF etches thermally grown oxide "at approximately 2 nanometres
per second at 25 degrees Celsius".[^wiki-boe][^wiki-hf] Dilute HF is the
natural tool for, and we infer is used at, stripping the thick gate
oxide from the low-voltage active areas ({ref}`GOXETCH <step-046>`) and
the sacrificial-oxide removal before silicidation
({ref}`SACETCH <step-095>`), because a plasma would damage the exposed
silicon. Silicon nitride is stripped in hot phosphoric acid (85 % H₃PO₄
at 150–180 °C), with selectivity to oxide of tens to one (typical
values;[^vgh-1967] see {ref}`category-strip`) — the STI nitride strip
{ref}`NS19 <step-013>` is catalogued under {ref}`category-strip`.
Aluminium can be etched in phosphoric/acetic/nitric mixtures, but not
with 130 nm-node fidelity. Wet etch rates vary with temperature,
concentration and bath age, so baths are monitored with etch-rate test
wafers.

### Endpoint, over-etch and loading

Because film thickness and etch rate both vary, production etches are
run to an {term}`endpoint` rather than a fixed time: optical emission
spectroscopy watches a product or reactant line (for example the 387 nm
CN band during nitride etch — "a strong peak at 387 nm indicates that CN
is present in the plasma, usually indicating that nitride is being
etched"[^pat-endpoint-tel] — or the 261 nm AlCl line in metal etch) and
triggers a timed over-etch when it changes; laser interferometry on a
monitoring pad follows the film thickness directly.[^nojiri-2015] The
{term}`loading effect` makes the rate depend on how much material is
exposed, and micro-loading and ARDE make dense and isolated features
etch differently, so the over-etch must cover the slowest feature while
the stop layer survives under the fastest. {term}`Etch bias <etch bias>` — the difference
between the resist {term}`CD` and the etched CD — is deliberately used to trim
gates below the printed dimension: ITRS 2001 lists an MPU/ASIC gate etch
bias of 25 nm for the 130 nm node.[^itrs-01]

### Damage and charging

Plasma exposure can charge floating gates and conductors; a long metal
line connected to a small gate collects ion current during metal etch
and can rupture the gate oxide. This is why design rules carry
*antenna* limits, and SKY130's antenna rules are computed from the
published metal thicknesses.[^pdk-03]
Ion bombardment also leaves a few nanometres of damaged, sometimes
amorphised silicon in trench floors and source/drains, which the next
oxidation or clean must remove.

## Typical equipment

* **{ref}`Silicon and poly etch <machine-plasma-etcher-silicon>`**: Lam TCP 9400 series (Lam's first TCP
  products were introduced in late 1992; the TCP 9400PTX and 9400DFM are
  the 200 mm silicon-etch variants;[^lam-10k] the reactor is described
  in university clean-room guides);[^snf-9400] Applied Materials Silicon
  Etch DPS Centura (introduced in 1996 for 0.35 µm and
  below).[^amat-1997]
* **{ref}`Dielectric etch <machine-plasma-etcher-dielectric>`**: Lam 4520XLE and Exelan (the Alliance-based
  "Exelan High Performance" dielectric etcher was launched in July
  2001);[^lam-exelan] Applied Materials MxP and eMxP+ chambers on the
  Precision 5000 and Centura platforms;[^amat-1997] TEL Unity dielectric
  etchers.
* **{ref}`Metal etch <machine-plasma-etcher-metal>`**: Lam TCP 9600; Applied Materials Metal Etch DPS Centura
  (1996)[^amat-1997] with integrated passivation and strip chambers.
* **Wet etch**: automated {ref}`wet benches <machine-wet-bench>` with HF, BOE and hot-phosphoric
  tanks (Akrion GAMA;[^akrion-gama] SCP, DNS/Screen and Santa Clara
  Plastics benches); centrifugal {ref}`spray processors <machine-wet-bench>` (FSI Mercury);
  {ref}`single-wafer spin etchers <machine-single-wafer-spin-processor>` for backside film removal and bevel clean
  (SEZ, now Lam) — the natural tool class for {ref}`BFR <step-060>`.
* **Metrology and inspection**: {term}`CD-SEM` after etch, {ref}`cross-section SEM <machine-cross-section-sem-profilers>` for
  profiles, {ref}`optical inspection <machine-defect-inspection>` for residues, and etch-rate monitor
  wafers.

## Typical consumables

* **Fluorine sources**: CF₄, CHF₃, C₄F₈, C₂F₆, SF₆, NF₃ (chamber clean).
* **Chlorine/bromine sources**: Cl₂, HBr, BCl₃.
* **Additives and carriers**: O₂, N₂, Ar, He (backside cooling), H₂,
  CH₂F₂ and CH₃F for nitride selectivity.
* **Wet chemicals**: 49 % HF and dilute HF, BOE (e.g. 6:1 or 10:1
  NH₄F:HF), 85 % phosphoric acid, nitric acid, ammonium hydroxide and
  hydrogen peroxide for post-etch cleans, isopropanol for drying.
* **Chamber parts**: silicon or quartz focus rings, ceramic (Al₂O₃,
  Y₂O₃-coated) liners, electrostatic chucks, showerheads, and endpoint
  windows, all consumed on a scheduled preventive-maintenance basis.
* **Photoresist and hard-mask films** as the pattern carrier
  ({ref}`category-lithography`, {ref}`category-deposition`).

## Steps in this category

| Step | Code | Name |
|------|------|------|
| 5 | {ref}`STINITE <step-005>` | Shallow trench nitride etch |
| 6 | {ref}`STIE <step-006>` | Shallow trench etch |
| 36 | {ref}`TUNARCE <step-036>` | Tunnel mask ARC etch |
| 39 | {ref}`TUNME <step-039>` | Tunnel mask etch |
| 42 | {ref}`ONOME <step-042>` | ONO mask etch |
| 46 | {ref}`GOXETCH <step-046>` | Low V gate oxide etch |
| 60 | {ref}`BFR <step-060>` | Backside film removal |
| 62 | {ref}`P1ME <step-062>` | Poly mask poly etch |
| 77 | {ref}`SPE <step-077>` | Spacer nitride etch |
| 79 | {ref}`NPCME <step-079>` | Nitride poly cut mask etch |
| 94 | {ref}`LICM1E <step-094>` | Local interconnect contact mask etch |
| 95 | {ref}`SACETCH <step-095>` | Sacrificial etch |
| 103 | {ref}`LI1ME <step-103>` | Local interconnect 1 mask etch |
| 108 | {ref}`CTME <step-108>` | Metal contact mask etch |
| 114 | {ref}`MM1E <step-114>` | Metal1 mask etch |
| 119 | {ref}`VIME <step-119>` | Via1 mask etch |
| 125 | {ref}`MM2E <step-125>` | Metal2 mask etch |
| 130 | {ref}`VIM2E <step-130>` | Via2 mask etch |
| 138 | {ref}`CAPME <step-138>` | Capacitor mask etch |
| 140 | {ref}`MM3E <step-140>` | Metal3 mask etch |
| 145 | {ref}`VIM3E <step-145>` | Via3 mask etch |
| 153 | {ref}`CAP2ME <step-153>` | Capacitor 2 mask etch |
| 155 | {ref}`MM4E <step-155>` | Metal4 mask etch |
| 160 | {ref}`VIM4E <step-160>` | Via4 (pad via) mask etch |
| 163 | {ref}`MM5E <step-163>` | Metal5 mask etch |
| 166 | {ref}`NSME <step-166>` | Nitride seal mask etch |
| 169 | {ref}`PDME <step-169>` | Pad mask etch |

## References

### Cross-check

* Coburn and Winters, *JAP* 1979 — the XeF₂ + Ar⁺ synergy
  experiment.[^coburn-1979]
* Steinbrüchel, *APL* 1989 — the square-root energy dependence of
  ion-enhanced etch yields.[^steinbruchel-1989]
* ITRS 2001, *Front End Processes* — the gate etch bias.[^itrs-01]
* SkyWater PDK, *Criteria & Assumptions* — antenna-rule film
  thicknesses.[^pdk-03]
* Lam Research, Form 10-K (fiscal 2003) — the TCP 9400PTX/DFM, 2300
  and Exelan product line.[^lam-10k]
* Lam Research, Exelan High Performance press release
  (2001).[^lam-exelan]
* Stanford Nanofabrication Facility, *Lam TCP 9400 Poly Etcher* — the
  reactor and its gas set.[^snf-9400]
* Applied Materials, 1997 Annual Report — DPS, MxP/eMxP+ and HDP
  dielectric etch history.[^amat-1997]
* C2MI, *Akrion GAMA acid bench*.[^akrion-gama]
* Tokyo Electron, US 6,376,262 — CN emission at 387 nm as the nitride
  etch endpoint signal.[^pat-endpoint-tel]

### High-level understanding

* Wikipedia, *Reactive-ion etching* — RF frequency, self-bias,
  pressure range and ICP sources.[^wiki-rie]
* Wikipedia, *Plasma etching*.[^wiki-plasma-etch]
* Wikipedia, *Dry etching*.[^wiki-dry-etch]
* Wikipedia, *Etching (microfabrication)*.[^wiki-etching]
* Wikipedia, *Inductively coupled plasma*.[^wiki-icp]
* Wikipedia, *Buffered oxide etch* — BOE composition and
  rate.[^wiki-boe]
* Wikipedia, *Hydrofluoric acid*.[^wiki-hf]
* Wikipedia, *Phosphoric acid*.[^wiki-h3po4]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — ch. 10
  ("Etching").[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  ch. 15–16 ("Wet Processing" and "Dry Etching for VLSI").[^txt-02]
* Campbell, *Fabrication Engineering at the Micro- and Nanoscale* —
  ch. 11.[^campbell-2013]
* Xiao, *Introduction to Semiconductor Manufacturing Technology* —
  ch. 9.[^txt-08]

### Deep dive

* Nojiri, *Dry Etching Technology for Semiconductors* — a
  production-oriented monograph on poly, oxide and metal etch
  chemistries and endpoint.[^nojiri-2015]
* Donnelly and Kornblit, *JVST A* 2013 — a long review of plasma
  etching from its origins to the present.[^donnelly-2013]
* Flamm and Donnelly, *Plasma Chem. Plasma Process.* 1981 — the design
  principles of plasma etchants.[^flamm-1981]
* Winters and Coburn, *Surf. Sci. Rep.* 1992 — surface-science view of
  etching reactions.[^winters-1992]
* Coburn and Winters, *JVST* 1979 — a discussion of plasma etching
  mechanisms.[^coburn-1979b]
* Lieberman and Lichtenberg, *Principles of Plasma Discharges and
  Materials Processing* — ch. 12 (high-density sources) and ch. 15
  (etching).[^lieberman-2005]
* Oehrlein, *Mater. Sci. Eng. B* 1989 — review of dry-etching damage to
  silicon.[^oehrlein-1989]
* Oehrlein and Kurogi, *Mater. Sci. Eng. R* 1998 — sidewall passivation
  chemistry in directional etching.[^oehrlein-1998]
* Oehrlein et al., *JVST A* 1994 — fluorocarbon film deposition and
  etching with CF₄ and CHF₃ in high-density plasmas.[^oehrlein-1994]
* Standaert et al., *JVST A* 1998 — etching through a steady-state
  fluorocarbon layer, the mechanism behind oxide-to-silicon
  selectivity.[^standaert-1998]
* Gottscho, Jurgensen and Vitkavage, *JVST B* 1992 — microscopic
  uniformity: aspect-ratio-dependent etching and its
  causes.[^gottscho-1992]
* Bell and Joubert, *JVST B* 1997 — chemical analysis of HBr/Cl₂/O₂
  gate-etch sidewalls under resist and oxide masks.[^bell-1997]
* Tuda, Shintani and Ootera, *JVST A* 2001 — profile evolution during
  Cl₂/HBr/O₂ high-density poly gate etching.[^tuda-2001]
* Mogab, *JES* 1977 — the loading effect.[^mogab-1977]
* Hashimoto, *JJAP* 1994 — electron-shading charging damage during
  high-density plasma etching.[^hashimoto-1994]
* Poulsen, *JVST* 1977 — an early review of plasma etching in IC
  manufacture, including aluminium.[^poulsen-1977]
* van Gelder and Hauser, *JES* 1967 — hot phosphoric acid etch rates
  of nitride, oxide and silicon.[^vgh-1967]
* Ogle (Lam Research), US 4,948,458 — the planar-coil
  transformer-coupled plasma source behind the TCP
  etchers.[^pat-tcp-lam]
* Yin et al. (Applied Materials), US 5,540,824 — the multi-section RF
  coil and isolated lid of the DPS reactor.[^pat-dps-amat]
* MIT OpenCourseWare 6.152J — lecture notes on plasma and wet
  etching.[^ocw-6152]

<!-- footnotes -->

[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^coburn-1979]: J. W. Coburn and H. F. Winters, "Ion- and
    electron-assisted gas-surface chemistry — An important effect in
    plasma etching", *Journal of Applied Physics* **50**(5), 3189–3196
    (1979). <https://doi.org/10.1063/1.326355>
[^steinbruchel-1989]: C. Steinbrüchel, "Universal energy dependence of
    physical and ion-enhanced chemical etch yields at low ion energy",
    *Applied Physics Letters* **55**(19), 1960–1962 (1989).
    <https://doi.org/10.1063/1.102336>
[^flamm-1981]: D. L. Flamm and V. M. Donnelly, "The design of plasma
    etchants", *Plasma Chemistry and Plasma Processing* **1**(4),
    317–363 (1981). <https://doi.org/10.1007/BF00565992>
[^lieberman-2005]: M. A. Lieberman and A. J. Lichtenberg, *Principles of
    Plasma Discharges and Materials Processing*, 2nd ed., Wiley, 2005,
    ISBN 978-0-471-72001-0. <https://doi.org/10.1002/0471724254>
[^donnelly-2013]: V. M. Donnelly and A. Kornblit, "Plasma etching:
    Yesterday, today, and tomorrow", *Journal of Vacuum Science &
    Technology A* **31**(5), 050825 (2013).
    <https://doi.org/10.1116/1.4819316>
[^nojiri-2015]: K. Nojiri, *Dry Etching Technology for Semiconductors*,
    Springer, 2015. <https://doi.org/10.1007/978-3-319-10295-5>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^winters-1992]: H. F. Winters and J. W. Coburn, "Surface science
    aspects of etching reactions", *Surface Science Reports*
    **14**(4–6), 162–269 (1992).
    <https://doi.org/10.1016/0167-5729(92)90009-Z>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^wiki-boe]: Wikipedia, *Buffered oxide etch*.
    <https://en.wikipedia.org/wiki/Buffered_oxide_etch>
[^wiki-hf]: Wikipedia, *Hydrofluoric acid*.
    <https://en.wikipedia.org/wiki/Hydrofluoric_acid>
[^pat-endpoint-tel]: Tokyo Electron, *Method of forming a semiconductor
    device using double endpoint detection*, US 6,376,262 B1, granted
    2002-04-23 (CN emission at 387 nm as the nitride etch endpoint
    signal). <https://patents.google.com/patent/US6376262B1/en>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^lam-10k]: Lam Research Corporation, Form 10-K for the fiscal year
    ended 2003-06-29 (product line: TCP 9400PTX/DFM, 2300, Exelan).
    <https://www.sec.gov/Archives/edgar/data/707549/000089161803004913/f93126e10vk.htm>
[^snf-9400]: Stanford Nanofabrication Facility, *Lam Research TCP 9400
    Poly Etcher (lampoly)*, equipment page.
    <https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report*.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^lam-exelan]: Lam Research, *Lam Research Corporation Advances
    Dielectric Etch Capabilities With Launch Of Exelan High
    Performance*, press release, 2001-07-09.
    <https://newsroom.lamresearch.com/2001-07-09-Lam-Research-Corporation-Advances-Dielectric-Etch-Capabilities-With-Launch-Of-Exelan-R-High-Performance>
[^akrion-gama]: C2MI, *Akrion GAMA acid bench*, equipment page.
    <https://www.c2mi.ca/en/equipement/akrion-gama-acid-bench/>
[^wiki-plasma-etch]: Wikipedia, *Plasma etching*.
    <https://en.wikipedia.org/wiki/Plasma_etching>
[^wiki-dry-etch]: Wikipedia, *Dry etching*.
    <https://en.wikipedia.org/wiki/Dry_etching>
[^wiki-etching]: Wikipedia, *Etching (microfabrication)*.
    <https://en.wikipedia.org/wiki/Etching_(microfabrication)>
[^wiki-icp]: Wikipedia, *Inductively coupled plasma*.
    <https://en.wikipedia.org/wiki/Inductively_coupled_plasma>
[^wiki-h3po4]: Wikipedia, *Phosphoric acid*.
    <https://en.wikipedia.org/wiki/Phosphoric_acid>
[^campbell-2013]: S. A. Campbell, *Fabrication Engineering at the Micro-
    and Nanoscale*, 4th ed., Oxford University Press, 2013,
    ISBN 978-0-19-986122-4. <https://openlibrary.org/isbn/9780199861224>
[^txt-08]: H. Xiao, *Introduction to Semiconductor Manufacturing
    Technology*, 2nd ed., SPIE Press, 2012, ISBN 978-0-8194-9092-6.
    <https://doi.org/10.1117/3.924283>
[^coburn-1979b]: J. W. Coburn and H. F. Winters, "Plasma etching — A
    discussion of mechanisms", *Journal of Vacuum Science and
    Technology* **16**(2), 391–403 (1979).
    <https://doi.org/10.1116/1.569958>
[^oehrlein-1989]: G. S. Oehrlein, "Dry etching damage of silicon: A
    review", *Materials Science and Engineering: B* **4**(1–4), 441–450
    (1989). <https://doi.org/10.1016/0921-5107(89)90284-5>
[^oehrlein-1998]: G. S. Oehrlein and Y. Kurogi, "Sidewall surface
    chemistry in directional etching processes", *Materials Science and
    Engineering: R* **24**(4), 153–183 (1998).
    <https://doi.org/10.1016/S0927-796X(98)00016-3>
[^oehrlein-1994]: G. S. Oehrlein, Y. Zhang, D. Vender and M. Haverlag,
    "Fluorocarbon high-density plasmas. I. Fluorocarbon film deposition
    and etching using CF₄ and CHF₃", *Journal of Vacuum Science &
    Technology A* **12**(2), 323–332 (1994).
    <https://doi.org/10.1116/1.578876>
[^standaert-1998]: T. E. F. M. Standaert, M. Schaepkens, N. R. Rueger,
    P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "High density
    fluorocarbon etching of silicon in an inductively coupled plasma:
    Mechanism of etching through a thick steady state fluorocarbon
    layer", *Journal of Vacuum Science & Technology A* **16**(1),
    239–249 (1998). <https://doi.org/10.1116/1.580978>
[^gottscho-1992]: R. A. Gottscho, C. W. Jurgensen and D. J. Vitkavage,
    "Microscopic uniformity in plasma etching", *Journal of Vacuum
    Science & Technology B* **10**(5), 2133–2147 (1992).
    <https://doi.org/10.1116/1.586180>
[^bell-1997]: F. H. Bell and O. Joubert, "Polysilicon gate etching in
    high density plasmas. V. Comparison between quantitative chemical
    analysis of photoresist and oxide masked polysilicon gates etched in
    HBr/Cl₂/O₂ plasmas", *Journal of Vacuum Science & Technology B*
    **15**(1), 88–97 (1997). <https://doi.org/10.1116/1.589259>
[^tuda-2001]: M. Tuda, K. Shintani and H. Ootera, "Profile evolution
    during polysilicon gate etching with low-pressure high-density
    Cl₂/HBr/O₂ plasma chemistries", *Journal of Vacuum Science &
    Technology A* **19**(3), 711–717 (2001).
    <https://doi.org/10.1116/1.1365135>
[^mogab-1977]: C. J. Mogab, "The Loading Effect in Plasma Etching",
    *Journal of The Electrochemical Society* **124**(8), 1262–1268
    (1977). <https://doi.org/10.1149/1.2133542>
[^hashimoto-1994]: K. Hashimoto, "Charge Damage Caused by Electron
    Shading Effect", *Japanese Journal of Applied Physics* **33**(10R),
    6013 (1994). <https://doi.org/10.1143/JJAP.33.6013>
[^poulsen-1977]: R. G. Poulsen, "Plasma etching in integrated circuit
    manufacture — A review", *Journal of Vacuum Science and Technology*
    **14**(1), 266–274 (1977). <https://doi.org/10.1116/1.569137>
[^vgh-1967]: W. van Gelder and V. E. Hauser, "The Etching of Silicon
    Nitride in Phosphoric Acid with Silicon Dioxide as a Mask", *Journal
    of The Electrochemical Society* **114**(8), 869 (1967).
    <https://doi.org/10.1149/1.2426757>
[^pat-tcp-lam]: J. S. Ogle (Lam Research Corporation), *Method and
    apparatus for producing magnetically-coupled planar plasma*,
    US 4,948,458 A, granted 1990-08-14.
    <https://patents.google.com/patent/US4948458A/en>
[^pat-dps-amat]: G. Z. Yin, H. Hanawa, D. X. Ma and D. Olgado (Applied
    Materials), *Plasma reactor with multi-section RF coil and isolated
    conducting lid*, US 5,540,824 A, granted 1996-07-30.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5540824>
[^ocw-6152]: MIT OpenCourseWare, *6.152J Micro/Nano Processing
    Technology*, Fall 2005 (lecture notes on lithography, etching,
    deposition and CMP).
    <https://ocw.mit.edu/courses/6-152j-micro-nano-processing-technology-fall-2005/>
[^cyp-qtp-113005]: Cypress Semiconductor, *Product Qualification
    Plan, QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8
    Technology, CMI (Fab 4)*, document 001-85611 Rev. *A, January
    2013 (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
