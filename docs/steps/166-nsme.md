(step-166)=
# Step 166 — NSME: Nitride seal mask etch

| | |
|---|---|
| **Step number** | 166 of 171[^steps-sheet] |
| **Step code** | `NSME` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | BEOL — passivation, pads, alloy, test |
| **Previous step** | {ref}`NSM <step-165>` |
| **Next step** | {ref}`NTSD <step-167>` |

## What this step is

`NSME` etches the opening defined by the `nsm` resist pattern of
{ref}`NSM <step-165>`: a ring, at least 3 µm wide (nsm.1[^pdk-periph]),
along the edge of every die, in a band that the design rules keep at
least 1 µm clear of all diffusion, poly, local interconnect and
metal except the seal ring's own diffusion rings (nsm.3[^pdk-periph]).
The resist is then stripped; this reference treats the strip and
post-etch clean as part of this step. The wafer next receives the
passivation nitride of {ref}`NTSD <step-167>`, which, on our reading,
lines the opening.

What the etch removes is not public. Its first film is the thin
passivation oxide of {ref}`NFUSOX <step-164>` (0.09 µm "TOPOX" on the
PDK's stack diagram[^pdk-04]). Below that, in a region with no wiring,
lie only dielectrics: on the diagram, the inter-level dielectrics NILD6
to NILD2 with the thin NILD3_C and NILD4_C layers, the thin nitride
over the local-interconnect level, which the diagram labels "LINT
K=7.3" (0.075 µm) and the step list calls {ref}`LINIT <step-104>`, the "PSG
K=3.9" pre-metal glass and the field oxide, the bottom of metal 5
carrying the level 5.3711 µm, measured from a datum the drawing does
not state (this reference reads it as the trench floor,
{ref}`STIE <step-006>`).[^pdk-04] In the seal-ring cell
used on Efabless's Caravel shuttle designs the `nsm` band is 5 µm wide
and overlies four 0.3 µm diffusion rings.[^caravel-sealring] The step
list used in this reference does not say how deep `NSME` goes; we
describe two readings (inference):

* **A deep seal etch.** The opening is cut through the inter-level
  oxides — and possibly the LINIT nitride and PSG — towards the silicon
  of the seal ring, so that the passivation nitride deposited next forms
  a continuous wall from the top of the die down into the dielectric
  stack. This is the construction of a GlobalFoundries edge-seal patent,
  whose seal is "formed through the low-k dielectric material to at
  least a substrate" and covered by passivation.[^pat-edgeseal-gf] The
  exemption of the seal ring's diffusion ring from the `nsm` keepout
  (nsm.3[^pdk-periph]) is consistent with an opening that reaches it.
* **A stop on the LINIT nitride.** The oxide etch lands on the 0.075 µm
  local-interconnect nitride,[^pdk-04] so that the top passivation
  nitride joins a nitride that already covers the front end, closing the
  inter-metal oxides inside nitride. A fluorocarbon oxide etch selective
  to nitride makes such a stop possible (Schaepkens et al. studied the
  mechanism[^schaepkens-1999]).

On either of these deeper readings the opening is several micrometres
deep and 3–5 µm wide, an
{term}`aspect ratio` of order 1–2 (our arithmetic), and occupies a very
small fraction of the wafer: a 5 µm band around the 3.6 mm × 5.2 mm
Caravel seal ring[^caravel-sealring] is about 0.09 mm² of an 18.7 mm²
die, some 0.5 % (our arithmetic).

## Step category

`NSME` is an {ref}`Etch <category-etch>` step of the *dielectric,
fluorocarbon-chemistry* class — the category page's "Silicon dioxide"
entry, applied not to a contact or via hole but to a wide, deep ring;
on the reading given here nitride is at most a thin layer to break
through or stop on. What is specific to this instance is the depth of the
dielectric column, the absence of any conductor to land on, the tiny
open area, and the timing: it is the only dielectric etch in the flow
made after metal 5 and before the passivation nitride, so the resist and
the etch must not attack the thin oxide over the metal-5 lines and pads
beside the ring.

## Why this step exists

* **To give the nitride a path down.** A passivation nitride laid only
  on the top surface leaves the inter-level oxides as a continuous
  lateral path from the saw-cut edge to the circuit. An opening through
  them, lined by nitride, interrupts that path; the moisture and ionic
  contamination it blocks are the drivers of corrosion Comizzoli et al.
  reviewed,[^comizzoli-1986] and a seal-ring patent, while calling the
  passivation nitride "a very good barrier of moisture and ionic
  contamination", shows "a moisture path … through the passivation
  oxide" beneath it at the die periphery.[^pat-sealring-zeevo] Even an
  opening through only the thin passivation oxide would let the nitride
  close that path — the patent's own moisture-path area is the die
  perimeter times a "bottle neck width … typically in the range of 0.5
  to 1.0 µm", which we read as the thickness of that
  oxide.[^pat-sealring-zeevo] That
  this is the purpose of
  SKY130's `nsm` ring is our inference ({ref}`NSM <step-165>`).
* **A {term}`crack stop`.** A trench through the dielectric along the saw line
  interrupts crack propagation from dicing, the function a Siemens and IBM patent
  obtains from "discontinuities in the thickness of the dielectric
  layer" near the edges of the active regions (inference for
  SKY130).[^pat-crackstop-ibm]
* **Before the nitride, not after.** The opening must exist when
  {ref}`NTSD <step-167>` is deposited, or the nitride could not line
  it; the pad opening ({ref}`PDME <step-169>`) comes after the nitride
  because it must cut the nitride over the pads.

## How it is typically performed

An industry-generic deep dielectric window etch over a finished
aluminium back end for a 200 mm, 130 nm-era fab (SKY130's recipe is not
public):

1. **Chamber.** A capacitively or inductively coupled dielectric etcher
   with a cooled chuck and helium backside cooling — Lam's
   Exelan[^lam-exelan][^lam-10k] or its predecessors, Applied Materials
   MxP/eMax-class chambers, TEL Unity.
2. **Main etch.** A fluorocarbon plasma (C₄F₈, C₂F₆, CF₄ and/or CHF₃
   with Ar and O₂) that etches silicon dioxide as SiF₄ under ion
   bombardment while depositing a fluorocarbon film on resist, nitride
   and silicon; the fluorine-to-carbon ratio sets rate and
   {term}`selectivity`.[^flamm-1981][^oehrlein-1994b][^winters-1992]
   Perry et al. measured oxide etch rates and selectivity to photoresist
   in a high-density C₂F₆ plasma[^perry-2001] — the ratio that decides
   whether the resist of {ref}`NSM <step-165>` survives a deep etch; a
   TSMC fuse-window patent etches through a passivation and several
   inter-metal dielectrics in two steps, the second with "a high
   selectivity to the silicon nitride etch stop layer".[^pat-fusewin-tsmc]
3. **Nitride layers.** If the etch is to pass the LINIT nitride, a less
   polymerising, more oxygen- or fluorine-rich step breaks through it;
   Kastenmeier et al. measured nitride and oxide rates in CF₄/O₂/N₂ in a
   downstream reactor and found that small N₂ additions raise the
   nitride rate sevenfold while leaving the oxide rate unchanged, the
   chemical contrast such a step exploits.[^kastenmeier-1996] If it is to
   stop on it, a polymerising chemistry with high oxide-to-nitride
   selectivity is used.[^schaepkens-1999]
4. **{term}`Endpoint <endpoint>`.** The open area is about 0.5 % (our
   estimate above), where the emission change at endpoint is small;
   narrow-band systems were nonetheless demonstrated on 200 mm
   dielectric etchers at under 3 % open area.[^wodecki-1999] Whether
   SKY130 endpoints this etch or runs it timed with an
   {term}`over-etch` on monitor calibration is not public.
5. **Strip and clean.** Downstream O₂/N₂ {term}`ash` on the GaSonics,
   Iridia or Mattson strippers SkyWater lists, then a solvent polymer
   clean compatible with the exposed oxide and the aluminium beneath
   the thin oxide elsewhere ("EKS265, EKC270 solvents"[^skw-01]).
6. **Metrology.** Opening width and profile by optical microscope and
   cross-section SEM on monitors; residual oxide and nitride at the
   bottom; particles.

## Machines typically used

* **{ref}`Dielectric etcher <machine-plasma-etcher-dielectric>`**, 200 mm: Lam Exelan,[^lam-exelan] Applied
  Materials MxP/eMax, TEL Unity ({ref}`category-etch`).
* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`**; **{ref}`solvent wet bench <machine-wet-bench>`**.
* **Optical microscope**, **{ref}`cross-section SEM <machine-cross-section-sem-profilers>`**.

## Machines likely used at SkyWater

* **No dielectric etcher is named on SkyWater's public list.** It gives,
  under poly/silicon etch, "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2",
  "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6, O2" and "Lam 4400, HBr,
  Cl2, C2F6, CF4, SF6, O2".[^skw-01] All three carry fluorine-bearing
  gases that can etch oxide; strength: **weak** for assignment of any
  of them to this etch.
* **Lam Exelan.** No public source places one at SkyWater; it appears
  here as the era's typical dielectric etcher.[^lam-exelan]
* **Strip and clean — GaSonics PEP, Iridia, Mattson Aspen II; batch
  rotational tools with "EKS265, EKC270 solvents".**[^skw-01] Strength:
  strong for existence; assignment is an inference.

## Resources required

* **{ref}`C₄F₈ <material-etch-gases>`, C₂F₆, CHF₃, CF₄**, **{ref}`Ar <material-process-gases>`**, **O₂** (and possibly CO or N₂)
  for the oxide etch (industry practice;[^nojiri-2015] SkyWater lists
  CF₄, CHF₃, C₂F₆ and O₂ on its etchers[^skw-01]); **He** backside
  cooling.
* **O₂/N₂** (and {ref}`forming gas <material-anneal-ambients>`) for the ash;[^skw-01] CF₄, listed on the
  Iridia and Mattson ashers,[^skw-01] would etch the oxide the ash exposes —
  the thin passivation oxide over metal 5 and the walls of the ring — and
  would, we infer, be left out. **Amine or semi-aqueous solvent**
  ({ref}`wet chemicals <material-wet-chemicals>`; EKC265/EKC270 class; SkyWater lists "EKS265, EKC270
  solvents"[^skw-01]) and {ref}`DI water <material-ultrapure-water>` for the post-etch clean.
* **{ref}`Chamber consumables <material-hardware-consumables>`** (focus rings, electrodes); **fluorocarbon
  abatement**; **{ref}`monitor wafers <material-substrates>`** with a full dielectric stack.

## Related steps and cross-references

* Previous: {ref}`NSM <step-165>` (the mask). Next:
  {ref}`NTSD <step-167>` (the passivation nitride that lines the
  opening, on our reading).
* The films it cuts, on our reading: {ref}`NFUSOX <step-164>`, the
  inter-level oxides {ref}`NILD2 <step-105>` to
  {ref}`NILD6 <step-156>`, the nitride {ref}`LINIT <step-104>`, the
  glass {ref}`PSG <step-089>`.
* The other window etch through the passivation: {ref}`PDME <step-169>`.
* Other oxide etches: {ref}`CTME <step-108>`, {ref}`VIM3E <step-145>`.
* Category page: {ref}`Etch <category-etch>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,789,302 A <patent-gp25239372>` — Crack stops (1997)
* {ref}`US 6,300,252 B1 <patent-gp23626242>` — Method for etching fuse windows in IC devices and devices made (1999)
* {ref}`US 6,492,716 B1 <patent-gp25297601>` — Seal ring structure for IC containing integrated digital/RF/analog circuits and functions (2001)

:::{dropdown} 1 family in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 10,062,748 B1 <patent-gp63208306>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, *Periphery rules* — nsm.1–nsm.3b.[^pdk-periph]
* SkyWater PDK, *Process stack diagram* — TOPOX, NILD2–NILD6, LINT,
  PSG and FOX; metal-5 level 5.3711 µm.[^pdk-04]
* Efabless, Caravel `advSeal_6um_gen` seal-ring GDS — the 5 µm `nsm`
  band over diffusion rings.[^caravel-sealring]
* SkyWater, *Facilities & Capabilities* — etchers and their gases;
  strippers and solvents.[^skw-01]
* Lam Research, Exelan press release and Form 10-K (2003).[^lam-exelan][^lam-10k]

### High-level understanding

* Wikipedia, *Reactive-ion etching*, *Dry etching*.[^wiki-rie][^wiki-dry-etch]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — plasma etching
  of dielectrics.[^txt-01]
* Nojiri, *Dry Etching Technology for Semiconductors* — oxide etch
  chemistry and equipment.[^nojiri-2015]

### Deep dive

* Flamm and Donnelly, *Plasma Chem. Plasma Process.* 1981 — the design
  of plasma etchants and the fluorine-to-carbon ratio.[^flamm-1981]
* Winters and Coburn, *Surf. Sci. Rep.* 1992 — surface science of
  etching reactions.[^winters-1992]
* Oehrlein et al., *JVST A* 1994 — silicon dioxide and silicon etching
  in CF₄ and CHF₃ high-density plasmas.[^oehrlein-1994b]
* Perry et al., *JVST A* 2001 — oxide etch rates and selectivity to
  photoresist in a C₂F₆ plasma.[^perry-2001]
* Schaepkens et al., *JVST A* 1999 — the SiO₂-to-Si₃N₄ selectivity
  mechanism, for a stop on the LINIT nitride.[^schaepkens-1999]
* Kastenmeier et al., *JVST A* 1996 — nitride and oxide etch rates in a
  downstream CF₄/O₂/N₂ reactor, for the chemical contrast a breakthrough
  step exploits.[^kastenmeier-1996]
* Wodecki, SPIE 1999 — endpoint detection demonstrated at low open
  area.[^wodecki-1999]
* Stamper, McGahay and He (GlobalFoundries), US 10,062,748 — an edge seal
  etched through the dielectrics.[^pat-edgeseal-gf]
* Mitwalsky and Chen (Siemens and IBM), US 5,789,302 — dielectric discontinuities as
  dicing crack stops.[^pat-crackstop-ibm]
* Ying and Hung (TSMC), US 6,300,252 — a two-step window etch through a
  passivation and inter-metal dielectrics.[^pat-fusewin-tsmc]
* Comizzoli et al., *Science* 1986 — corrosion of electronic devices by
  moisture and ions.[^comizzoli-1986]

## Open questions

* How deep the etch goes — through the thin TOPOX only, to the LINIT
  nitride, or to the silicon of the seal ring — and whether it passes
  any nitride, are not public.
* The chemistry, endpoint and tool are not public.
* This page treats the resist strip and clean as part of the etch.

<!-- footnotes -->

[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^caravel-sealring]: Efabless Corporation, *caravel* repository,
    `gds/advSeal_6um_gen.gds.gz` (seal-ring cell for SKY130 shuttle
    designs), retrieved 2026-09-14.
    <https://github.com/efabless/caravel/blob/main/gds/advSeal_6um_gen.gds.gz>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^lam-exelan]: Lam Research, *Lam Research Corporation Advances
    Dielectric Etch Capabilities With Launch Of Exelan High
    Performance*, press release, 2001-07-09.
    <https://newsroom.lamresearch.com/2001-07-09-Lam-Research-Corporation-Advances-Dielectric-Etch-Capabilities-With-Launch-Of-Exelan-R-High-Performance>
[^lam-10k]: Lam Research Corporation, Form 10-K for the fiscal year
    ended 2003-06-29 (product line: TCP 9400PTX/DFM, 2300, Exelan).
    <https://www.sec.gov/Archives/edgar/data/707549/000089161803004913/f93126e10vk.htm>
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^wiki-dry-etch]: Wikipedia, *Dry etching*.
    <https://en.wikipedia.org/wiki/Dry_etching>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^nojiri-2015]: K. Nojiri, *Dry Etching Technology for Semiconductors*,
    Springer, 2015. <https://doi.org/10.1007/978-3-319-10295-5>
[^flamm-1981]: D. L. Flamm and V. M. Donnelly, "The design of plasma
    etchants", *Plasma Chemistry and Plasma Processing* **1**(4),
    317–363 (1981). <https://doi.org/10.1007/BF00565992>
[^winters-1992]: H. F. Winters and J. W. Coburn, "Surface science
    aspects of etching reactions", *Surface Science Reports*
    **14**(4–6), 162–269 (1992).
    <https://doi.org/10.1016/0167-5729(92)90009-Z>
[^oehrlein-1994b]: G. S. Oehrlein, Y. Zhang, D. Vender and O. Joubert,
    "Fluorocarbon high-density plasmas. II. Silicon dioxide and silicon
    etching using CF₄ and CHF₃", *Journal of Vacuum Science &
    Technology A* **12**(2), 333–344 (1994).
    <https://doi.org/10.1116/1.578877>
[^perry-2001]: W. L. Perry, K. Waters, M. Barela and H. M. Anderson,
    "Oxide etch behavior in a high-density, low-pressure, inductively
    coupled C₂F₆ plasma: Etch rates, selectivity to photoresist, plasma
    parameters, and CFx radical densities", *Journal of Vacuum Science
    & Technology A* **19**(5), 2272–2281 (2001).
    <https://doi.org/10.1116/1.1382874>
[^schaepkens-1999]: M. Schaepkens, T. E. F. M. Standaert, N. R. Rueger,
    P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "Study of the
    SiO₂-to-Si₃N₄ etch selectivity mechanism in inductively coupled
    fluorocarbon plasmas and a comparison with the SiO₂-to-Si
    mechanism", *Journal of Vacuum Science & Technology A* **17**(1),
    26–37 (1999). <https://doi.org/10.1116/1.582108>
[^kastenmeier-1996]: B. E. E. Kastenmeier, P. J. Matsuo, J. J. Beulens
    and G. S. Oehrlein, "Chemical dry etching of silicon nitride and
    silicon dioxide using CF₄/O₂/N₂ gas mixtures", *Journal of Vacuum
    Science & Technology A* **14**(5), 2802–2813 (1996).
    <https://doi.org/10.1116/1.580203>
[^wodecki-1999]: N. Wodecki, "Low open area multilayered dielectric
    film etch endpoint detection using EndPoint Plus", *Proc. SPIE*
    **3882**, Process, Equipment, and Materials Control in Integrated
    Circuit Manufacturing V, 231 (1999).
    <https://doi.org/10.1117/12.361313>
[^comizzoli-1986]: R. B. Comizzoli, R. P. Frankenthal, P. C. Milner and
    J. D. Sinclair, "Corrosion of Electronic Materials and Devices",
    *Science* **234**(4774), 340–345 (1986).
    <https://doi.org/10.1126/science.234.4774.340>
[^pat-edgeseal-gf]: A. K. Stamper, V. J. McGahay and Z.-X. He
    (GlobalFoundries), *Segmented guard-ring and chip edge seals*,
    US 10,062,748 B1, filed 2017-02-27, granted 2018-08-28.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10062748>
    Shown as in force; estimated expiry 2038-02-27 (estimate from public
    records, not legal advice).
[^pat-crackstop-ibm]: A. R. Mitwalsky and T.-C. Chen (Siemens
    Aktiengesellschaft / International Business Machines), *Crack stops*,
    US 5,789,302 A, filed 1997-03-24, granted 1998-08-04.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5789302>
[^pat-sealring-zeevo]: S. Bothra, T. G. McKay and R. Jhota (Zeevo),
    *Seal ring structure for IC containing integrated digital/RF/analog
    circuits and functions*, US 6,492,716 B1, filed 2001-04-30, granted
    2002-12-10.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6492716>
[^pat-fusewin-tsmc]: S. Ying and S.-C. Hung (Taiwan Semiconductor
    Manufacturing Co.), *Method for etching fuse windows in IC devices
    and devices made*, US 6,300,252 B1, filed 1999-10-01, granted
    2001-10-09.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6300252>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
