(category-etch)=
# Etch

## What this class of step does

An etch step removes material selectively: wherever the photoresist
(or a hard mask) is open, the exposed film is eaten away down to a
stopping layer, and wherever it is covered, the film stays. Etching is
how the pattern drawn by lithography ({ref}`category-lithography`) is
transferred into the real materials of the chip — nitride, silicon,
oxide, polysilicon, aluminium, titanium nitride. Some etches have no
mask at all and simply remove a film everywhere (a "blanket" etch or
etch-back) or only from the wafer backside.

Precisely, an etch is characterised by four numbers. Its **rate**
(nm/min) sets the process time; its {term}`selectivity`, the ratio of
the rate on the target film to the rate on the mask and on the
underlying stop layer, sets how much over-etch can be tolerated; its
{term}`anisotropy`, the ratio of vertical to lateral rate, sets how
faithfully the resist width becomes the etched width; and its
**uniformity** across the wafer and between dense and isolated features
sets how much over-etch is *needed*. A 130 nm process uses two families:
plasma ("dry") etching in a vacuum chamber, which can be highly
anisotropic and is used for every patterned film, and wet chemical
etching in aqueous baths, which is isotropic and is used where a film
must be removed cleanly and gently with very high selectivity — the
thin oxides at {ref}`GOXETCH <step-046>` and {ref}`SACETCH <step-095>`,
for example.

In the SKY130 flow there are 27 etch steps: the STI nitride and trench
etches, the SONOS tunnel/ONO stack etches, the gate-oxide wet etch, the
poly gate etch, the spacer etch, a nitride cut, the local-interconnect
contact and line etches, the sacrificial-oxide wet etch before
silicidation, the metal contact etch, the five aluminium metal etches,
four via etches, two MiM capacitor etches, a backside film removal, and
the final nitride-seal and pad etches.

## Physics and engineering background

### How a plasma etches

A reactive-ion etcher holds the wafer on an RF-driven electrode in a
gas at low pressure. "Plasma is initiated in the system by applying a
strong RF electromagnetic field to the wafer platter. The field is
typically set to a frequency of 13.56 Megahertz, applied at a few
hundred watts", and because electrons are far more mobile than ions
the platter charges to "a large negative voltage on the platter,
typically around a few hundred volts", which accelerates positive ions
across the sheath and onto the wafer normal to its surface
([Wikipedia: Reactive-ion etching][wiki-rie]). Pressure "is typically
maintained in a range between a few millitorr and a few hundred
millitorr" ([Wikipedia: Reactive-ion etching][wiki-rie]).

Etching then proceeds by a synergy between chemistry and ion
bombardment. Coburn and Winters showed in 1979 that silicon exposed to
XeF₂ *and* an argon-ion beam etches roughly an order of magnitude faster
than under either alone ([Coburn and Winters 1979][coburn]); the ions
break bonds, clear inhibiting films and volatilise reaction products
only where they strike, which is straight down. Steinbrüchel found that
the ion-enhanced etch yield scales as
{math}`Y \propto \sqrt{E} - \sqrt{E_{th}}` at low ion energies
([Steinbrüchel 1989][steinbruchel]). Anisotropy is therefore obtained
either by making the reaction ion-driven or by passivating the sidewalls
with a polymer or oxide that ions remove from the trench floor but not
from the walls (Flamm and Donnelly [flamm]; Lieberman and Lichtenberg,
ch. 15 [lieberman]).

### Plasma sources

A conventional capacitive RIE couples ion density and ion energy through
the one RF supply. High-density sources decouple them: an inductively
coupled ({term}`ICP`; Lam's {term}`TCP`; Applied's "decoupled plasma
source", DPS) coil generates a dense plasma (typically 10¹¹–10¹² cm⁻³;
Lieberman and Lichtenberg, ch. 12 [lieberman]) at a few millitorr, while
a separate low-frequency bias on the electrostatic
chuck sets the ion energy, so that "the ICP is employed as a high
density source of ions which increases the etch rate" while the bias
controls "the energy of ions bombarding the surface" ([Wikipedia:
Reactive-ion etching][wiki-rie]). Low pressure gives a collisionless
sheath and near-vertical ions; low bias limits damage and improves
selectivity. Dielectric etches, which need polymerising chemistries and
higher ion energies, are mostly done in dual-frequency capacitive
reactors (a high frequency for density, a low frequency for bias) such
as Lam's Exelan and Applied's eMxP+ (Donnelly and Kornblit [donnelly];
Nojiri [nojiri]).

### Chemistries by material

* **Silicon and polysilicon** (STI trench {ref}`STIE <step-006>`, gate
  {ref}`P1ME <step-062>`): HBr/Cl₂ with a little O₂, which forms
  volatile SiBrₓ/SiClₓ while a thin SiOₓBrᵧ sidewall film keeps the
  profile vertical; the O₂ also raises selectivity to the gate oxide
  underneath, and the main etch is followed by a soft-landing and an
  HBr/O₂ over-etch step with selectivity to SiO₂ of the order of 100:1
  so that a 2–4 nm gate oxide survives (Nojiri, ch. 3 [nojiri];
  Plummer, Deal and Griffin, ch. 10). SF₆ "is commonly used for etching
  silicon" where isotropy is acceptable ([Wikipedia: Reactive-ion
  etching][wiki-rie]).
* **Silicon dioxide** (contacts {ref}`CTME <step-108>`, vias
  {ref}`VIME <step-119>`, oxide hard masks): fluorocarbons — CF₄, CHF₃,
  C₄F₈, C₂F₆ — with Ar and O₂. Fluorine etches oxide as SiF₄ only under
  ion bombardment, while the carbon forms a polymer that deposits on
  silicon and nitride, giving selectivity to the underlying silicon or
  to a nitride etch-stop; the fluorine-to-carbon ratio is the master
  variable (Flamm and Donnelly [flamm]; Winters and Coburn [winters]).
  High-aspect-ratio contacts show {term}`ARDE`, etch-stop from
  polymer build-up, and bowing.
* **Silicon nitride** (STI hard mask {ref}`STINITE <step-005>`, spacer
  {ref}`SPE <step-077>`, nitride cut {ref}`NPCME <step-079>`, seal
  {ref}`NSME <step-166>`): CF₄/CHF₃/O₂ or SF₆-based, with the
  fluorocarbon content tuned for selectivity to oxide; the spacer etch
  is an unmasked anisotropic etch-back that leaves nitride only on the
  vertical gate sidewalls and must stop on a thin oxide without
  trenching the silicon (Plummer, Deal and Griffin, ch. 10).
* **Aluminium–copper with Ti/TiN caps** (metal 1–5,
  {ref}`MM1E <step-114>` to {ref}`MM5E <step-163>`): Cl₂/BCl₃ with
  N₂ or CHF₃ for sidewall passivation. AlCl₃ is volatile at room
  temperature, so aluminium etches spontaneously in chlorine and
  anisotropy depends entirely on the passivation film; BCl₃ scavenges
  water and reduces the native Al₂O₃; copper chlorides are not volatile
  and are removed by ion bombardment; and residual chlorine plus
  atmospheric moisture corrodes the lines, so the etch ends with an
  in-situ H₂O or O₂/CF₄ passivation plasma and an immediate rinse
  (Nojiri, ch. 3 [nojiri]; Wolf and Tauber, ch. 16).
* **Ti:W and TiN** (capacitor top plates {ref}`CAPME <step-138>`,
  {ref}`CAP2ME <step-153>`): fluorine (SF₆, CF₄) or chlorine chemistries
  with high selectivity to the oxynitride dielectric beneath.
* **Anti-reflective coatings** ({ref}`TUNARCE <step-036>`): organic
  BARC opens in O₂/N₂ or HBr/O₂; inorganic SiON in CF₄-based plasmas.
* **Tungsten** etch-back (an alternative to CMP for plugs): SF₆/Ar.

### Wet etching

Wet etches are chemical only, so they are isotropic and can be almost
perfectly selective. Silicon dioxide is removed in dilute hydrofluoric
acid or in {term}`BOE`, a mixture of ammonium fluoride and HF whose
buffering gives "a more stable pH; thus, more stable concentrations of
HF and HF₂⁻, and a more stable etch rate"; a 6:1 mixture of 40 % NH₄F
and 49 % HF etches thermally grown oxide "at approximately
2 nanometres per second at 25 degrees Celsius" ([Wikipedia: Buffered
oxide etch][wiki-boe]; [Wikipedia: Hydrofluoric acid][wiki-hf]). Dilute HF is the tool for
stripping the thick gate oxide from the low-voltage active areas
({ref}`GOXETCH <step-046>`) and for the sacrificial-oxide removal
before silicidation ({ref}`SACETCH <step-095>`), because a plasma would
damage the exposed silicon. Silicon nitride is stripped in hot
phosphoric acid (85 % H₃PO₄ at 150–180 °C), with selectivity to oxide
of tens to one — the STI nitride strip {ref}`NS19 <step-013>` is
catalogued under {ref}`category-strip`. Aluminium can be etched in
phosphoric/acetic/nitric mixtures, but not with 130 nm-node fidelity.
Wet etch rates vary with temperature, concentration and bath age, so
baths are monitored with etch-rate test wafers.

### Endpoint, over-etch and loading

Because film thickness and etch rate both vary, production etches are
run to an {term}`endpoint` rather than a fixed time: optical emission
spectroscopy watches a product or reactant line (for example the
387 nm CN band during nitride etch — "a strong peak at 387 nm indicates
that CN is present in the plasma, usually indicating that nitride is
being etched" ([US 6,376,262][cn-patent]) — or the 261 nm AlCl line in
metal etch) and triggers a timed over-etch when it changes; laser
interferometry on a monitoring pad follows the film thickness directly
(Nojiri, ch. 4 [nojiri]). The {term}`loading effect` makes the rate
depend on how much material is exposed, and micro-loading and ARDE
make dense and isolated features etch differently, so the over-etch
must cover the slowest feature while the stop layer survives under the
fastest. Etch bias — the difference between the resist CD and the
etched CD — is deliberately used to trim gates below the printed
dimension: ITRS 2001 lists an MPU/ASIC gate etch bias of 25 nm for the
130 nm node ([ITRS 2001, Front End Processes][itrs2001-fep]).

### Damage and charging

Plasma exposure can charge floating gates and conductors; a long metal
line connected to a small gate collects ion current during metal etch
and can rupture the gate oxide. This is why design rules carry
*antenna* limits, and SKY130's antenna rules are computed from the
published metal thicknesses ([SKY130 PDK, Criteria & Assumptions][pdk-assume]).
Ion bombardment also leaves a few nanometres of damaged, sometimes
amorphised silicon in trench floors and source/drains, which the next
oxidation or clean must remove.

## Typical equipment

* **Silicon and poly etch**: Lam TCP 9400 series (Lam's first TCP
  products were introduced in late 1992; the TCP 9400PTX and 9400DFM
  are the 200 mm silicon-etch variants [lam-10k]; the reactor is
  described in university clean-room guides [snf-9400]); Applied
  Materials Silicon Etch DPS Centura (introduced in 1996 for 0.35 µm
  and below [amat-1997]).
* **Dielectric etch**: Lam 4520XLE and Exelan (the Alliance-based
  "Exelan High Performance" dielectric etcher was launched in July 2001
  [lam-exelan]); Applied Materials MxP and eMxP+ chambers on the
  Precision 5000 and Centura platforms [amat-1997]; TEL Unity
  dielectric etchers.
* **Metal etch**: Lam TCP 9600; Applied Materials Metal Etch DPS
  Centura (1996 [amat-1997]) with integrated passivation and strip
  chambers.
* **Wet etch**: automated wet benches with HF, BOE and hot-phosphoric
  tanks (Akrion GAMA [akrion]; SCP, DNS/Screen and Santa Clara Plastics
  benches); centrifugal spray processors (FSI Mercury); single-wafer
  spin etchers for backside film removal and bevel clean (SEZ, now
  Lam) — the natural tool class for {ref}`BFR <step-060>`.
* **Metrology and inspection**: CD-SEM after etch, cross-section SEM
  for profiles, optical inspection for residues, and etch-rate monitor
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

* J. W. Coburn and H. F. Winters, "Ion- and electron-assisted
  gas-surface chemistry — An important effect in plasma etching",
  *Journal of Applied Physics* **50**, 3189–3196 (1979).
  <https://doi.org/10.1063/1.326355>
* C. Steinbrüchel, "Universal energy dependence of physical and
  ion-enhanced chemical etch yields at low ion energy", *Applied
  Physics Letters* **55**, 1960–1962 (1989).
  <https://doi.org/10.1063/1.102336>
* *ITRS 2001 Edition: Front End Processes* (gate etch bias).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
* SkyWater Technology / Google, "Criteria & Assumptions", *SKY130 PDK
  documentation* (antenna-rule film thicknesses).
  <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
* Lam Research Corporation, Form 10-K for fiscal year ended
  2003-06-29 (product line: TCP 9400PTX/DFM, 2300, Exelan).
  <https://www.sec.gov/Archives/edgar/data/707549/000089161803004913/f93126e10vk.htm>
* Lam Research, "Lam Research Corporation Advances Dielectric Etch
  Capabilities With Launch Of Exelan High Performance", press release,
  2001-07-09. <https://newsroom.lamresearch.com/2001-07-09-Lam-Research-Corporation-Advances-Dielectric-Etch-Capabilities-With-Launch-Of-Exelan-R-High-Performance>
* Stanford Nanofabrication Facility, "Lam Research TCP 9400 Poly
  Etcher". <https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>
* Applied Materials, 1997 Annual Report (DPS, MxP/eMxP+ and HDP
  dielectric etch history).
  <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
* C2MI, "Akrion GAMA acid bench".
  <https://www.c2mi.ca/en/equipement/akrion-gama-acid-bench/>
* US Patent 6,376,262, "Method of forming a semiconductor device using
  double endpoint detection" (Tokyo Electron, granted 2002-04-23; CN
  emission at 387 nm as the nitride etch endpoint signal).
  <https://patents.google.com/patent/US6376262B1/en>

### High-level

* Wikipedia, "Reactive-ion etching".
  <https://en.wikipedia.org/wiki/Reactive-ion_etching>
* Wikipedia, "Plasma etching".
  <https://en.wikipedia.org/wiki/Plasma_etching>
* Wikipedia, "Dry etching". <https://en.wikipedia.org/wiki/Dry_etching>
* Wikipedia, "Etching (microfabrication)".
  <https://en.wikipedia.org/wiki/Etching_(microfabrication)>
* Wikipedia, "Inductively coupled plasma".
  <https://en.wikipedia.org/wiki/Inductively_coupled_plasma>
* Wikipedia, "Buffered oxide etch".
  <https://en.wikipedia.org/wiki/Buffered_oxide_etch>
* Wikipedia, "Hydrofluoric acid".
  <https://en.wikipedia.org/wiki/Hydrofluoric_acid>
* Wikipedia, "Phosphoric acid".
  <https://en.wikipedia.org/wiki/Phosphoric_acid>
* J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
  Technology*, Prentice Hall, 2000, ISBN 978-0-13-085037-9, ch. 10
  ("Etching").
* S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI Era,
  Vol. 1*, 2nd ed., Lattice Press, 2000, ISBN 978-0-9616721-6-4,
  ch. 15–16 ("Wet Processing" and "Dry Etching for VLSI").
* S. A. Campbell, *Fabrication Engineering at the Micro- and
  Nanoscale*, 4th ed., Oxford University Press, 2013,
  ISBN 978-0-19-986122-4, ch. 11.
* H. Xiao, *Introduction to Semiconductor Manufacturing Technology*,
  2nd ed., SPIE Press, 2012, ch. 9. <https://doi.org/10.1117/3.924283>

### Deep dive

* K. Nojiri, *Dry Etching Technology for Semiconductors*, Springer,
  2015. <https://doi.org/10.1007/978-3-319-10295-5>
* V. M. Donnelly and A. Kornblit, "Plasma etching: Yesterday, today,
  and tomorrow", *Journal of Vacuum Science and Technology A* **31**,
  050825 (2013). <https://doi.org/10.1116/1.4819316>
* D. L. Flamm and V. M. Donnelly, "The design of plasma etchants",
  *Plasma Chemistry and Plasma Processing* **1**, 317–363 (1981).
  <https://doi.org/10.1007/BF00565992>
* H. F. Winters and J. W. Coburn, "Surface science aspects of etching
  reactions", *Surface Science Reports* **14**, 162–269 (1992).
  <https://doi.org/10.1016/0167-5729(92)90009-Z>
* J. W. Coburn and H. F. Winters, "Plasma etching — A discussion of
  mechanisms", *Journal of Vacuum Science and Technology* **16**,
  391–403 (1979). <https://doi.org/10.1116/1.569958>
* M. A. Lieberman and A. J. Lichtenberg, *Principles of Plasma
  Discharges and Materials Processing*, 2nd ed., Wiley, 2005.
  <https://doi.org/10.1002/0471724254>

[wiki-rie]: https://en.wikipedia.org/wiki/Reactive-ion_etching
[wiki-boe]: https://en.wikipedia.org/wiki/Buffered_oxide_etch
[wiki-hf]: https://en.wikipedia.org/wiki/Hydrofluoric_acid
[coburn]: https://doi.org/10.1063/1.326355
[steinbruchel]: https://doi.org/10.1063/1.102336
[flamm]: https://doi.org/10.1007/BF00565992
[winters]: https://doi.org/10.1016/0167-5729(92)90009-Z
[lieberman]: https://doi.org/10.1002/0471724254
[donnelly]: https://doi.org/10.1116/1.4819316
[nojiri]: https://doi.org/10.1007/978-3-319-10295-5
[itrs2001-fep]: https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf
[pdk-assume]: https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html
[lam-10k]: https://www.sec.gov/Archives/edgar/data/707549/000089161803004913/f93126e10vk.htm
[lam-exelan]: https://newsroom.lamresearch.com/2001-07-09-Lam-Research-Corporation-Advances-Dielectric-Etch-Capabilities-With-Launch-Of-Exelan-R-High-Performance
[snf-9400]: https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly
[amat-1997]: https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf
[akrion]: https://www.c2mi.ca/en/equipement/akrion-gama-acid-bench/
[cn-patent]: https://patents.google.com/patent/US6376262B1/en
