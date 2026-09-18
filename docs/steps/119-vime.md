(step-119)=
# Step 119 — VIME: Via1 mask etch

| | |
|---|---|
| **Step number** | 119 of 171[^steps-sheet] |
| **Step code** | `VIME` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | BEOL — via 1, metal 2, via 2 |
| **Previous step** | {ref}`VIM <step-118>` |
| **Next step** | {ref}`TIN3 <step-120>` |

## What this step is

`VIME` etches the via-1 holes. Through the 0.15 µm resist openings of
{ref}`VIM <step-118>` a fluorocarbon plasma cuts the
{ref}`NCAPOX3 <step-117>` cap and the {ref}`NILD3 <step-115>` oxide
beneath it — 0.27 µm in all, the via-1 height of the PDK's stack
diagram[^pdk-04] — down to the top of the metal-1 lines, producing the
holes that {ref}`TIN3 <step-120>` will line and {ref}`WDEP3 <step-121>`
will fill to make the `via` plug, "Contact from metal 1 to
metal 2".[^pdk-06] The resist is stripped afterwards; this reference
treats the strip and post-etch clean as part of this step, as at
{ref}`CTME <step-108>`.

What the etch lands on is the difference from the contact etch. The
floor of a `via` is not the nitride-capped titanium-nitride local
interconnect but the top film of the metal-1 stack — on the public
description of the S8 process, 300 Å of titanium–tungsten over
3 200 Å of Al–0.5%Cu[^cyp-qtp-113005] — so the {term}`selectivity`
that matters is oxide-to-TiW, and the failure to avoid is punching
through the cap into the aluminium. The public dimensions are the
mask's: 0.150 µm squares (via.1a) on a 0.170 µm space (via.2), with
metal 1 required to enclose them by only 0.055 µm (via.4a);[^pdk-periph]
the assumptions table adds a "Via1 slope" of 0.02 and a "min. etch
and fill capability for via" of 0.18 µm.[^pdk-03] Where the {term}`overlay`
of {ref}`VIM <step-118>` to {ref}`MM1 <step-113>` uses up that
0.055 µm, part of the hole floor is oxide beside the line
(inference), and the etch must not dig far there. The
{term}`aspect ratio` is about 1.8:1 as drawn, shallower than the
contact's.

## Step category

`VIME` is an {ref}`Etch <category-etch>` step of the *dielectric,
fluorocarbon* class — the category page's "oxide and via etch" family
of C₄F₈, CHF₃, CF₄ and C₂F₆ chemistries — and the first of the four
via etches ({ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`,
{ref}`VIM4E <step-160>` follow). Fluorine removes oxide as SiF₄ only
under ion bombardment, while the carbon of the feed gas forms a
polymer that slows the etch on non-oxide surfaces; that surface
chemistry, worked out by Flamm and Donnelly and by Winters and
Coburn,[^flamm-1981][^winters-1992] is what gives the etch its
selectivity to the stop layer. What is specific to this class within
the flow is that the stop layer is a *metal that fluorine can etch*:
tungsten forms volatile WF₆ in fluorine plasmas — Petri, Henry and
Sadeghi describe the mechanism in SF₆[^petri-1992] — and titanium
forms TiF₄, so the etch must reach the cap in a polymerising,
fluorine-lean regime and stop on time rather than on chemistry alone
(industry practice;[^nojiri-2015] see below).

## Why this step exists

The via hole sets the resistance and reliability of every connection
between metal 1 and metal 2, and the etch decides four things:

* **A clean, complete landing on TiW.** The PDK's `via` is 4 500 mΩ
  (4.5 Ω), thirty times lower than the 152 000 mΩ of an
  `mcon`,[^pdk-08] and on our reading that gap is largely a matter of
  the landing: a narrower, shallower hole ending on a metal cap rather
  than a wider one ending on 0.10 µm of TiN.[^pdk-04] Fluorocarbon
  polymer or oxide left on the floor raises the number; Bui et al.
  showed that the anti-reflective cap a tungsten-plug via lands on
  also sets its electromigration performance.[^bui-1994]
* **Not punching through.** If the 300 Å TiW[^cyp-qtp-113005] is
  consumed by the over-etch, the fluorine reaches the aluminium and
  forms involatile AlF₃ — fluorine does not etch aluminium, which is
  why aluminium is etched in chlorine[^hess-1982] — leaving a
  resistive fluoride at the via bottom and a cap too thin to serve as
  the electromigration shunt and barrier the metal-1 page describes
  ({ref}`TIAL6 <step-112>`). Texas Instruments' patent on a Ti–Al or
  Ti–Al–N etch stop for a "fluorine-bearing" via etch is a public
  statement of the same problem and one answer to it.[^pat-etchstop-ti]
* **Tolerating a partly unlanded via.** With only 0.055 µm of
  enclosure (via.4a),[^pdk-periph] some vias will overhang their line;
  the oxide beside the line then etches on while the cap holds, and
  the trench exposes the aluminium sidewall to the liner and the
  tungsten precursor. The etch's over-etch and the liner's coverage
  are budgeted together for this (inference from the rule).
* **A via that tungsten will fill.** Fluorocarbon residue, moisture or
  outgassing from the dielectric sidewall can stop the tungsten of
  {ref}`WDEP3 <step-121>` nucleating — the "poisoned via" that
  Kobayakawa et al. and Romero et al. traced to outgassing from
  spin-on glass in the early 1990s[^kobayakawa-1991][^romero-1991] and
  that a UMC patent addresses by densifying the exposed dielectric
  before the fill.[^pat-via-poison-umc] Which SKY130 dielectric is at
  risk is not public; the PDK's separately named "NILD3_C" (k 3.5,
  0.030 µm)[^pdk-04] is a candidate if it is a fluorinated film
  ({ref}`NILD3 <step-115>`).

Without `VIME` the resist pattern of {ref}`VIM <step-118>` would be
stripped without effect and metal 2 would sit on unbroken oxide.

## How it is typically performed

An industry-generic via etch for a 200 mm, 130 nm-era fab (SKY130's
recipe is not public); the shared physics is set out at
{ref}`CTME <step-108>` and on the category page.

1. **Chamber.** A single-wafer dielectric etcher — a medium-density
   capacitively coupled or a high-density inductively coupled reactor
   with separate bias, helium backside cooling and optical-emission
   endpoint ({ref}`category-etch`); Lam's Exelan was launched for
   this generation in 2001.[^lam-exelan]
2. **BARC open.** The organic {term}`BARC` of {ref}`VIM <step-118>` is
   opened through the resist holes with a short O₂/N₂ or
   CF₄-containing step.
3. **Main oxide etch.** A polymerising fluorocarbon — C₄F₈, C₂F₆ or
   CHF₃ with argon and a little O₂ or CO — at tens of mTorr and high
   bias.[^oehrlein-1994b][^perry-2001][^standaert-1998] In a 0.15 µm
   hole the conductance of the hole throttles the neutral and ion
   flux to the floor (Coburn and Winters[^coburn-1989]), so the rate
   falls with depth ({term}`ARDE`) or, under some conditions, rises
   (Doemling et al.'s inverse RIE lag[^doemling-1996]); Gottscho,
   Jurgensen and Vitkavage review the family of effects.[^gottscho-1992]
   The 0.27 µm depth[^pdk-04] is modest, but the {term}`loading effect`
   between isolated vias and dense arrays is not.
4. **Endpoint and over-etch.** Via layers expose a small fraction of
   the wafer, so the emission signal is weak — Wodecki describes
   endpoint detection on low-open-area dielectric etches[^wodecki-1999]
   — and the etch is usually run by time from the thickness the cap
   and polish left ({ref}`CMPM <step-116>`, {ref}`NCAPOX3 <step-117>`),
   with an over-etch sized to clear the deepest vias without
   consuming the TiW. The mechanism of oxide-to-nitride selectivity
   Schaepkens et al. describe — a thicker steady-state fluorocarbon
   film on the non-oxide surface[^schaepkens-1999] — is what protects
   the cap, and it fails if the chemistry runs fluorine-rich, since
   TiW then etches as WF₆ and TiF₄.[^petri-1992]
5. **Strip and clean.** Oxygen or O₂/N₂ downstream {term}`ash` —
   GaSonics, Iridia or Mattson class in SkyWater's list[^skw-01] —
   then a solvent or semi-aqueous clean — SkyWater lists "EKS265,
   EKC270 solvents, CO2 injected DI" under "Batch Rotational" in its
   resist-removal and clean list[^skw-01] (EKC265/EKC270-class;
   SkyWater writes "EKS265") — to remove the
   fluorocarbon polymer and the titanium- and tungsten-fluoride
   residue from the via floor without attacking the TiW or the
   exposed aluminium of an unlanded via. No HF is used (inference:
   it would widen the via and attack the fluoride-bearing floor).
6. **Queue time.** Because an open via can absorb moisture from the
   air, the time between clean and {ref}`TIN3 <step-120>` is limited,
   and a degas precedes the liner (industry practice;[^txt-05] the
   poisoned-via literature above is the reason[^kobayakawa-1991]).
7. **Metrology.** Top and bottom CD by {term}`CD-SEM`, profile and
   cap loss by cross-section SEM on monitors, via-chain resistance at
   {term}`e-test`; the PDK's 4.5 Ω `via`[^pdk-08] is the number such
   chains give. The published SKY130 {term}`test tile`'s via-1
   structures are an "M2 to M1 via: 0.15um (3240 vias)" string and
   "M2-M1-LI1-N+" and "M2-M1-LI1-P+" strings of 6992 contacts, each a
   "stacked via on mcon on licon1".[^raw-data-testtile-pads]

## Machines typically used

* **{ref}`Dielectric etcher <machine-plasma-etcher-dielectric>`**, 200 mm single-wafer: Lam Exelan / 4520XLE,
  Applied Materials eMax / MxP+ / Super-e, TEL DRM / Unity
  ({ref}`category-etch`); high-density alternatives (AMAT IPS, Lam
  TCP 9100).
* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`** (GaSonics Aura, Mattson Aspen) and **{ref}`wet bench <machine-wet-bench>` or
  {ref}`single-wafer clean <machine-single-wafer-spin-processor>`** for post-etch residue.
* **{ref}`CD-SEM <machine-cd-sem-overlay-metrology>`**, **{ref}`cross-section SEM <machine-cross-section-sem-profilers>`**, **{ref}`e-test <machine-parametric-tester>`** for via chains.

## Machines likely used at SkyWater

* **No dielectric etcher is named on SkyWater's public list.** The
  list gives, under poly/silicon etch, "AMAT DPSII, HBR, Cl2, NF3,
  CF4, CHF3, O2", "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6, O2" and
  "Lam 4400, HBr, Cl2, C2F6, CF4, SF6, O2".[^skw-01] All three carry
  fluorine-bearing gases that can etch oxide; strength: **weak** for
  assignment of any of them to the via etch.
* **Lam Exelan.** No public source places an Exelan at SkyWater; it
  appears here only as the era's typical dielectric etcher, a line
  Lam's own 10-K lists.[^lam-10k]
* **Strip and clean — GaSonics PEP, Iridia, Mattson Aspen II; Akrion
  Gamma wet bench; batch rotational tools with "EKS265, EKC270
  solvents"; SEZ 223 / Da Vinci.**[^skw-01] Strength: strong for
  existence.

## Resources required

* **{ref}`C₄F₈ <material-etch-gases>`, C₂F₆, CHF₃, CF₄**, **{ref}`Ar <material-process-gases>`**, **O₂** (and possibly CO or N₂)
  for the oxide etch (industry practice;[^nojiri-2015] SkyWater lists
  CF₄, CHF₃, C₂F₆ and O₂ on its etchers[^skw-01]).
* **Helium** for backside cooling; **NF₃** or O₂-based chamber clean.
* **O₂/N₂** (and {ref}`forming gas <material-anneal-ambients>`) for the ash;[^skw-01] CF₄, listed on the
  Iridia and Mattson ashers,[^skw-01] would attack the exposed TiW and
  would, we infer, be left out. **Amine or semi-aqueous solvent**
  ({ref}`wet chemicals <material-wet-chemicals>`; EKC265/EKC270 class; SkyWater lists "EKS265, EKC270
  solvents"[^skw-01]) and {ref}`DI water <material-ultrapure-water>` for the post-etch clean.
* **{ref}`Chamber consumables <material-hardware-consumables>`** (liners, focus and edge rings, electrodes);
  **{ref}`monitor wafers <material-substrates>`** with blanket oxide and TiW for rate and
  selectivity checks.

## Related steps and cross-references

* Previous: {ref}`VIM <step-118>` (the mask). Next:
  {ref}`TIN3 <step-120>` (the liner), then {ref}`WDEP3 <step-121>`
  and {ref}`WCMP3 <step-122>`.
* The films it cuts: {ref}`NCAPOX3 <step-117>` and
  {ref}`NILD3 <step-115>` (polished at {ref}`CMPM <step-116>`); the
  cap it stops on: {ref}`TIAL6 <step-112>`, patterned at
  {ref}`MM1 <step-113>` / {ref}`MM1E <step-114>`.
* The analogous hole etches: {ref}`CTME <step-108>` below,
  {ref}`VIM2E <step-130>` above.
* Category page: {ref}`Etch <category-etch>`.

## References

### Cross-check

* SkyWater PDK, *Periphery rules* — via.1a 0.150 µm, via.2 0.170 µm,
  via.4a 0.055 µm.[^pdk-periph]
* SkyWater PDK, *Criteria & Assumptions* — "Via1 slope" 0.02; via
  etch-and-fill capability 0.18 µm.[^pdk-03]
* SkyWater PDK, *Process stack diagram* — via1 (NILD3) 0.27 µm;
  NILD3_C 0.030 µm, k 3.5.[^pdk-04]
* SkyWater PDK, *Layers Reference* — `via` 68:44.[^pdk-06]
* SkyWater PDK, *Parasitic Layout Extraction* — VIA 4 500 mΩ, MCON
  152 000 mΩ.[^pdk-08]
* Cypress, QTP 113005 — the 300 Å TiW cap the etch stops
  on.[^cyp-qtp-113005]
* SkyWater, *Facilities & Capabilities* — DPS II, Lam 9400 TCP and Lam 4400 gas
  lists; ashers; EKC solvents.[^skw-01]
* Lam Research, Exelan launch (2001) and 10-K (2003).[^lam-exelan][^lam-10k]
* SKY130 raw-data repository, test-tile pad documentation — the via-1
  chain structures of the published test tile.[^raw-data-testtile-pads]

### High-level understanding

* Wikipedia, *Reactive-ion etching*, *Dry etching*, *Via
  (electronics)*.[^wiki-rie][^wiki-dry-etch][^wiki-via]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — the etch
  chapter.[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — via etching
  and multilevel-metal integration.[^txt-05]
* Nojiri, *Dry Etching Technology for Semiconductors* — oxide etch
  chemistry and endpoint.[^nojiri-2015]

### Deep dive

* Flamm and Donnelly, 1981, and Winters and Coburn, 1992 — the
  surface chemistry of fluorocarbon selectivity.[^flamm-1981][^winters-1992]
* Oehrlein, Zhang, Vender and Joubert, *JVST A* 1994 — oxide and
  silicon etching in CF₄/CHF₃ high-density plasmas.[^oehrlein-1994b]
* Standaert et al., *JVST A* 1998 — etching through a thick
  steady-state fluorocarbon layer.[^standaert-1998]
* Schaepkens et al., *JVST A* 1999 — how a fluorocarbon film on the
  stop layer creates selectivity.[^schaepkens-1999]
* Perry et al., *JVST A* 2001 — oxide etch rates and selectivity in a
  high-density C₂F₆ plasma.[^perry-2001]
* Coburn and Winters, *Appl. Phys. Lett.* 1989 — conductance limits
  in high-aspect-ratio feature etching.[^coburn-1989]
* Doemling, Rueger and Oehrlein, *Appl. Phys. Lett.* 1996 — inverse
  RIE lag in oxide etching.[^doemling-1996]
* Gottscho, Jurgensen and Vitkavage, *JVST B* 1992 — aspect-ratio and
  loading effects reviewed.[^gottscho-1992]
* Petri, Henry and Sadeghi, *J. Appl. Phys.* 1992 — tungsten etching
  in fluorine plasmas, the reason TiW is a fragile stop.[^petri-1992]
* Fischl and Hess, *J. Electrochem. Soc.* 1987 — tungsten etching in
  chlorine, for contrast.[^fischl-1987]
* Hess, *Plasma Chem. Plasma Process.* 1982 — why fluorine does not
  etch aluminium.[^hess-1982]
* Wodecki, SPIE 1999 — endpoint detection on low-open-area
  dielectric etches.[^wodecki-1999]
* Bui et al., MRS 1994 — the anti-reflective cap under a tungsten-plug
  via and its electromigration performance.[^bui-1994]
* Kobayakawa et al., VMIC 1991, and Romero et al., *J. Mater. Res.*
  1991 — outgassing from planarising dielectrics, the origin of via
  poisoning.[^kobayakawa-1991][^romero-1991]
* Wu and Lu (UMC), US 6,013,581 — preventing poisoned vias by
  densifying the exposed dielectric.[^pat-via-poison-umc]
* Xing, Cerny and Visokay (TI), US 6,090,697 — an etch stop for a
  fluorine-bearing via etch.[^pat-etchstop-ti]
* Yin et al. (Applied Materials), US 5,540,824, and Ogle (Lam
  Research), US 4,948,458 — the two high-density plasma sources of
  the era.[^pat-dps-amat][^pat-tcp-lam]

## Open questions

* The etch chemistry, chamber, endpoint scheme and over-etch of
  `VIME`, the TiW consumed, and the resulting profile are not public.
* Whether the via etch has a distinct step for the
  {ref}`NCAPOX3 <step-117>` cap and the possible "NILD3_C"
  film,[^pdk-04] or etches the whole 0.27 µm in one recipe, is not
  public.
* Whether SKY130 vias ever land partly off metal 1 in practice, and
  how the etch is budgeted for it, is inferred from the 0.055 µm
  enclosure rule.[^pdk-periph]
* Which etcher runs the step is not public; SkyWater's list names no
  dedicated dielectric etcher.[^skw-01]
* This page treats the resist strip and post-etch clean as part of
  the etch step.

<!-- footnotes -->

[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^cyp-qtp-113005]: Cypress Semiconductor, *Product Qualification
    Plan, QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8
    Technology, CMI (Fab 4)*, document 001-85611 Rev. *A, January
    2013 (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^flamm-1981]: D. L. Flamm and V. M. Donnelly, "The design of plasma
    etchants", *Plasma Chemistry and Plasma Processing* **1**(4),
    317–363 (1981). <https://doi.org/10.1007/BF00565992>
[^winters-1992]: H. F. Winters and J. W. Coburn, "Surface science
    aspects of etching reactions", *Surface Science Reports*
    **14**(4–6), 162–269 (1992).
    <https://doi.org/10.1016/0167-5729(92)90009-Z>
[^petri-1992]: R. Petri, D. Henry and N. Sadeghi, "Tungsten etching
    mechanisms in low-pressure SF₆ plasma", *Journal of Applied Physics*
    **72**(7), 2644–2651 (1992). <https://doi.org/10.1063/1.351565>
[^nojiri-2015]: K. Nojiri, *Dry Etching Technology for Semiconductors*,
    Springer, 2015. <https://doi.org/10.1007/978-3-319-10295-5>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^bui-1994]: N. D. Bui, V. H. Pham, D. D. Forsythe, R. T. Lee and
    J. T. Yue, "Effect of TiN ARC on Electromigration Performance of
    Tungsten Plug Via", *MRS Proceedings* **338** (1994).
    <https://doi.org/10.1557/PROC-338-471>
[^hess-1982]: D. W. Hess, "Plasma etch chemistry of aluminum and
    aluminum alloy films", *Plasma Chemistry and Plasma Processing*
    **2**(2), 141–155 (1982). <https://doi.org/10.1007/BF00633130>
[^pat-etchstop-ti]: G. Xing, G. A. Cerny and M. R. Visokay (Texas
    Instruments), *Etchstop for integrated circuits*, US 6,090,697 A,
    filed 1998-06-26, granted 2000-07-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6090697>
[^kobayakawa-1991]: M. Kobayakawa, A. Arimatsu, F. Yokoyama, N. Hirashita
    and T. Ajioka, "A study of outgassing from spin-on-glass films used
    for planarization", *Proc. Eighth International IEEE VLSI Multilevel
    Interconnection Conference (VMIC 1991)*, pp. 454–456.
    <https://doi.org/10.1109/VMIC.1991.153054>
[^romero-1991]: J. D. Romero, M. Khan, H. Fatemi and J. Turlo,
    "Outgassing behavior of spin-on-glass (SOG)", *Journal of Materials
    Research* **6**(9), 1996–2003 (1991).
    <https://doi.org/10.1557/JMR.1991.1996>
[^pat-via-poison-umc]: K.-L. Wu and H.-B. Lu (United Microelectronics
    Corp.), *Method for preventing poisoned vias and trenches*,
    US 6,013,581 A, filed 1998-10-05, granted 2000-01-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6013581>
[^lam-exelan]: Lam Research, *Lam Research Corporation Advances
    Dielectric Etch Capabilities With Launch Of Exelan High
    Performance*, press release, 2001-07-09.
    <https://newsroom.lamresearch.com/2001-07-09-Lam-Research-Corporation-Advances-Dielectric-Etch-Capabilities-With-Launch-Of-Exelan-R-High-Performance>
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
[^standaert-1998]: T. E. F. M. Standaert, M. Schaepkens, N. R. Rueger,
    P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "High density
    fluorocarbon etching of silicon in an inductively coupled plasma:
    Mechanism of etching through a thick steady state fluorocarbon
    layer", *Journal of Vacuum Science & Technology A* **16**(1),
    239–249 (1998). <https://doi.org/10.1116/1.580978>
[^coburn-1989]: J. W. Coburn and H. F. Winters, "Conductance
    considerations in the reactive ion etching of high aspect ratio
    features", *Applied Physics Letters* **55**(26), 2730–2732 (1989).
    <https://doi.org/10.1063/1.101937>
[^doemling-1996]: M. F. Doemling, N. R. Rueger and G. S. Oehrlein,
    "Observation of inverse reactive ion etching lag for silicon
    dioxide etching in inductively coupled plasmas", *Applied Physics
    Letters* **68**(1), 10–12 (1996). <https://doi.org/10.1063/1.116772>
[^gottscho-1992]: R. A. Gottscho, C. W. Jurgensen and D. J. Vitkavage,
    "Microscopic uniformity in plasma etching", *Journal of Vacuum
    Science & Technology B* **10**(5), 2133–2147 (1992).
    <https://doi.org/10.1116/1.586180>
[^wodecki-1999]: N. Wodecki, "Low open area multilayered dielectric
    film etch endpoint detection using EndPoint Plus", *Proc. SPIE*
    **3882**, Process, Equipment, and Materials Control in Integrated
    Circuit Manufacturing V, 231 (1999).
    <https://doi.org/10.1117/12.361313>
[^schaepkens-1999]: M. Schaepkens, T. E. F. M. Standaert, N. R. Rueger,
    P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "Study of the
    SiO₂-to-Si₃N₄ etch selectivity mechanism in inductively coupled
    fluorocarbon plasmas and a comparison with the SiO₂-to-Si
    mechanism", *Journal of Vacuum Science & Technology A* **17**(1),
    26–37 (1999). <https://doi.org/10.1116/1.582108>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^lam-10k]: Lam Research Corporation, Form 10-K for the fiscal year
    ended 2003-06-29 (product line: TCP 9400PTX/DFM, 2300, Exelan).
    <https://www.sec.gov/Archives/edgar/data/707549/000089161803004913/f93126e10vk.htm>
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^wiki-dry-etch]: Wikipedia, *Dry etching*.
    <https://en.wikipedia.org/wiki/Dry_etching>
[^wiki-via]: Wikipedia, *Via (electronics)*.
    <https://en.wikipedia.org/wiki/Via_(electronics)>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^fischl-1987]: D. S. Fischl and D. W. Hess, "Plasma-Enhanced Etching
    of Tungsten and Tungsten Silicide in Chlorine-Containing
    Discharges", *Journal of The Electrochemical Society* **134**(9),
    2265–2269 (1987). <https://doi.org/10.1149/1.2100868>
[^pat-dps-amat]: G. Z. Yin, H. Hanawa, D. X. Ma and D. Olgado (Applied
    Materials), *Plasma reactor with multi-section RF coil and isolated
    conducting lid*, US 5,540,824 A, granted 1996-07-30.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5540824>
[^pat-tcp-lam]: J. S. Ogle (Lam Research Corporation), *Method and
    apparatus for producing magnetically-coupled planar plasma*,
    US 4,948,458 A, granted 1990-08-14.
    <https://patents.google.com/patent/US4948458A/en>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
