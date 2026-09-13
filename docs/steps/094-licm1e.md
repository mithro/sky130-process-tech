(step-094)=
# Step 094 — LICM1E: Local interconnect contact mask etch

| | |
|---|---|
| **Step number** | 94 of 171 |
| **Step code** | `LICM1E` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | MOL — silicide and local interconnect |
| **Previous step** | {ref}`LICM1 <step-093>` |
| **Next step** | {ref}`SACETCH <step-095>` |

## What this step is

`LICM1E` is the contact etch. Through the resist openings of
{ref}`LICM1 <step-093>` it etches 0.17 µm holes[^pdk-periph] down
through the {term}`cap oxide` of {ref}`NCAPOX <step-091>` and the
phosphosilicate glass of {ref}`PSG <step-089>` — together about
0.5 µm, the PDK's "Pre-LI ILD thickness"[^pdk-03] — until each hole
reaches its landing surface: the {ref}`SPOX <step-080>` oxide over
a source/drain or tap, which the etch must also clear, or the bare
poly head inside a {term}`nitride cut` ({ref}`NPCME <step-079>`). The holes
taper — the PDK's "Licon1 etch angle" is 10°[^pdk-03] — from the
0.17 µm drawn opening to a "Standard Licon bottom CD" of
0.08 µm,[^pdk-03] so the aspect ratio at the bottom is about 6:1.
After it the resist is stripped and the wafer cleaned (the
{ref}`SACETCH <step-095>` and the head of {ref}`ALLY1 <step-096>`,
on our reading), and the holes are lined, silicided and filled.

Three landing surfaces make this etch unusual. A diffusion or tap
contact lands on silicon between two nitride {term}`spacers <spacer>` and, where the
0.055 µm licon.11 margin[^pdk-periph] is used up by {term}`overlay`, on the
spacer and the nitride cap of the adjacent gate; the etch therefore
needs {term}`selectivity` to nitride as well as to silicon. A poly
contact lands on poly that the nitride cut has already exposed
(licon.15, licon.18[^pdk-periph]), so there is no nitride to open at
the bottom — that is the point of doing the cut first, as the
{ref}`NPCM <step-078>` page argues from the scheme Tang et al. used
for a TiN {term}`local interconnect`.[^tang-1985] And every hole passes
through two chemically different oxides, cap and {term}`PSG`, whose etch
rates differ, and — if the {ref}`CMPP <step-090>` polish landed on
the gate caps — the holes over poly are shallower than those over
diffusion, so the etch must tolerate different depths on one wafer.

## Step category

`LICM1E` is an {ref}`Etch <category-etch>` step of the *dielectric,
fluorocarbon-chemistry* class — the deepest and narrowest oxide
etch so far in the flow and the first *hole* etch. The category page
sets out the chemistry: fluorocarbons (CF₄, CHF₃, C₄F₈, C₂F₆) with
argon and oxygen, in which fluorine etches oxide as SiF₄ only under
ion bombardment while the carbon forms a polymer on silicon and
nitride that gives the selectivity to the landing surfaces; the
fluorine-to-carbon ratio is the master variable.[^flamm-1981][^winters-1992]
What is specific to this instance is the {term}`aspect ratio` and
the two selectivities at once. The same class recurs at
{ref}`CTME <step-108>` (the `mcon` etch, which lands on the
titanium-nitride local interconnect through its nitride cap) and at
every {term}`via` etch.

## Why this step exists

The contact hole is where the front end meets the wiring; its etch
decides the contact resistance, the junction leakage and the yield
of every transistor. The specific requirements:

* **Vertical, tapered profile.** The 10° taper[^pdk-03] is
  deliberate: it widens the mouth of the hole for the ionised-metal
  {term}`liner` ({ref}`TI/TIN1 <step-097>`) and the {term}`CVD` tungsten fill
  ({ref}`WDEP <step-099>`), and a controlled taper is how a 0.17 µm
  drawn contact becomes a 0.08 µm bottom. Oehrlein and Kurogi
  review the sidewall chemistry that sets the profile.[^oehrlein-1998]
* **Aspect-ratio-dependent etching.** Narrow, deep holes etch more
  slowly than wide ones ({term}`ARDE`, "RIE lag") because ions and
  neutrals reach the bottom less easily; Gottscho, Jurgensen and
  Vitkavage set out the mechanisms,[^gottscho-1992] Joubert, Oehrlein
  and Surendra modelled {term}`RIE` lag for contact holes in a
  high-density fluorocarbon plasma,[^joubert-1994] and Doemling,
  Rueger and Oehrlein observed the *inverse* lag that appears when
  polymer deposition dominates.[^doemling-1996] Because the licons
  are all the same size (licon.3[^pdk-periph]), the lag is the same
  for every hole — one reason the rule exists.
* **Selectivity and etch stop.** Fluorocarbon films on the etched
  surface are what make oxide etch faster than nitride and silicon:
  Oehrlein et al. and Rueger et al. established the steady-state
  film picture,[^oehrlein-1994-ii][^rueger-1997] Standaert et al.
  the mechanism of etching through a thick film,[^standaert-1998]
  and Schaepkens et al. the SiO₂-to-Si₃N₄ selectivity mechanism
  specifically.[^schaepkens-1999] Too much polymer and the hole
  stops before it reaches bottom ("etch stop"); too little and the
  spacer, the gate cap and the silicon are attacked.
* **Damage and charging.** The {term}`over-etch` on the silicon is the most
  damaging plasma exposure the junctions receive: Fonash reviews
  the damage and contamination dry etching leaves,[^fonash-1990]
  Oehrlein the silicon damage specifically,[^oehrlein-1989] and
  Cacciato et al. describe charging damage during a contact etch
  when the etch reaches a conductive borderless nitride[^cacciato-2003]
  — the electron-shading mechanism Hashimoto identified.[^hashimoto-1994]
  What this etch leaves on the silicon is what the
  {ref}`SACETCH <step-095>` and {ref}`ALLY1 <step-096>` steps then
  have to remove or heal (inference from their position).

Without `LICM1E` there would be no path from the local interconnect
to any transistor.

## How it is typically performed

An industry-generic contact etch for a 200 mm, 130 nm-era fab
(SKY130's recipe is not public):

1. **Chamber.** Single-wafer high-density or medium-density
   dielectric etcher — a dual-frequency capacitive reactor (Lam
   Exelan class[^lam-exelan][^lam-10k]) or an inductively coupled
   one (Applied Materials DPS class[^pat-dps-amat]) — with
   independent source and bias power, helium backside cooling and
   optical emission {term}`endpoint` ({ref}`category-etch`).
2. **BARC open.** A short O₂/N₂ or CF₄-based step opens the
   anti-reflective coating under the resist.
3. **Main etch.** C₄F₈ or CHF₃/CF₄ with Ar and a little O₂ at tens of
   mTorr and high bias, tuned to a polymerising regime for
   selectivity;[^oehrlein-1994-ii][^rueger-1997] etch rates of a few
   hundred nanometres per minute and oxide : nitride selectivities of
   order 10 : 1 are typical of the era (category page[^nojiri-2015]).
   SkyWater lists CF₄ and CHF₃ on its AMAT DPS II.[^skw-01]
4. **Endpoint and over-etch.** Optical emission (CO at 483 nm
   rises while oxide is etched and falls as the holes clear; the
   double-endpoint scheme of the Tokyo Electron
   patent[^pat-cn-tel] is one way to detect it through the
   small open area) followed by a timed over-etch that clears the
   {ref}`SPOX <step-080>` oxide at the bottom of the diffusion
   contacts and the shallower poly contacts' residue without
   trenching the silicon or breaching the spacers.
5. **Post-etch treatment.** An in-situ O₂ or H₂/N₂ plasma removes
   the fluorocarbon polymer from the hole walls (the step SkyWater's
   "Mattson Aspen2, RF plasma, O2, CF4, H2>N2" or "Gasonic PEP"
   ashers could also perform[^skw-01]); the resist itself is
   stripped and the wafer wet-cleaned — this reference treats the
   strip as part of this step or of {ref}`SACETCH <step-095>`.
6. **Metrology.** Contact {term}`CD` top and bottom by {term}`CD-SEM`; cross-section
   SEM for profile, taper and residue during development; electrical
   contact-chain resistance at {ref}`category-test` structures
   afterwards.

## Machines typically used

* **Dielectric etcher**, 200 mm: Lam 4520XLE/Exelan,[^lam-exelan]
  Applied Materials MxP/eMax and DPS (dielectric
  configurations),[^amat-1997] TEL DRM/Unity, Lam {term}`TCP` 9100
  ({ref}`category-etch`).
* **Optical emission endpoint** system on the etcher.
* **Cross-section SEM**, **CD-SEM**.

## Machines likely used at SkyWater

* **AMAT DPS II.** SkyWater lists "AMAT DPSII, HBR, Cl2, NF3, CF4,
  CHF3, O2 – gate, trench, W/WN".[^skw-01] Strength: **strong** for
  the tool and for a CF₄/CHF₃/O₂ gas set; assignment to the contact
  etch is an **inference** — the list names gate, trench and
  tungsten applications but no dedicated dielectric etcher, which is
  itself an open question (below).
* **Lam 9400 TCP** ("poly/nitride, HBr, CF4, SF6, O2"[^skw-01]) and
  **Lam 4400** ("HBr, Cl2, C2F6, CF4, SF6, O2"[^skw-01]) carry
  fluorocarbon gases and could etch oxide. Strength: medium/weak.
* **Lam Exelan.** No public source places an Exelan at SkyWater; it
  appears here only as the era's typical dielectric etcher, a line
  Lam's own 10-K lists.[^lam-10k]
* Resist strip and polymer removal: **Mattson Aspen2, Gasonics PEP,
  Iridia** ashers;[^skw-01] wet clean: **DNS wet bench, FSI Mercury,
  Akrion Gamma**.[^skw-01] Strength: strong for existence.

## Resources required

* **C₄F₈, CHF₃, CF₄, Ar, O₂** (and possibly **C₂F₆** or **CO**) —
  industry practice;[^nojiri-2015] SkyWater lists CF₄, CHF₃, C₂F₆
  and O₂ on its etchers.[^skw-01]
* **Helium** backside cooling; **NF₃/O₂** chamber clean.
* **O₂, N₂, H₂/N₂** for the post-etch polymer removal and
  strip.[^skw-01]
* **Chamber consumables** — silicon or quartz rings, liners,
  electrodes; **monitor wafers** with blanket oxide and nitride for
  rate and selectivity checks.[^semi-m8]
* Gas suppliers named by SkyWater: Air Products, Praxair.[^sec-01]

## Related steps and cross-references

* Previous: {ref}`LICM1 <step-093>` (the resist pattern). Next:
  {ref}`SACETCH <step-095>`, then {ref}`ALLY1 <step-096>` and the
  liner {ref}`TI/TIN1 <step-097>`.
* The films etched: {ref}`NCAPOX <step-091>`, {ref}`PSG <step-089>`,
  {ref}`SPOX <step-080>`. The nitride the etch must not breach:
  {ref}`SPNIT <step-076>`/{ref}`SPE <step-077>` spacers,
  {ref}`GATENIT <step-058>` caps.
* The cut that removed nitride from under the poly contacts:
  {ref}`NPCM <step-078>`, {ref}`NPCME <step-079>`.
* The next dielectric hole etch: {ref}`CTME <step-108>`.
* Category page: {ref}`Etch <category-etch>`.

## References

### Cross-check

* SkyWater PDK, *Criteria & Assumptions* — "Pre-LI ILD thickness"
  0.5 µm; "Licon1 etch angle" 10°; "Standard Licon bottom CD"
  0.08 µm; "min. etch and fill capability … licon" 0.15 µm.[^pdk-03]
* SkyWater PDK, *Periphery rules* — licon.1, licon.3, licon.11,
  licon.15, licon.18.[^pdk-periph]
* SkyWater, *Facilities & Capabilities* — AMAT DPS II, Lam 9400,
  Lam 4400 gas sets; ashers; wet benches.[^skw-01]
* Applied Materials, 1997 Annual Report — DPS and MxP
  etchers.[^amat-1997]
* Lam Research, Exelan press release and Form 10-K.[^lam-exelan][^lam-10k]
* SkyWater, Form S-1 — gas suppliers.[^sec-01]

### High-level understanding

* Wikipedia, *Reactive-ion etching*.[^wiki-rie]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  oxide etching.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — contact and
  via etching at deep-submicron nodes.[^txt-05]
* Nojiri, *Dry Etching Technology for Semiconductors* — oxide etch
  chemistry and equipment.[^nojiri-2015]

### Deep dive

* Flamm and Donnelly, *Plasma Chem. Plasma Process.* 1981 — the
  design of plasma etchants.[^flamm-1981]
* Winters and Coburn, *Surf. Sci. Rep.* 1992 — surface science of
  etching reactions.[^winters-1992]
* Oehrlein et al., *JVST A* 1994, and Rueger et al., *JVST A* 1997 —
  fluorocarbon films in high-density oxide etching.[^oehrlein-1994-ii][^rueger-1997]
* Standaert et al., *JVST A* 1998 — etching through a thick
  steady-state fluorocarbon layer.[^standaert-1998]
* Schaepkens et al., *JVST A* 1999 — the SiO₂-to-Si₃N₄ selectivity
  mechanism.[^schaepkens-1999]
* Joubert, Oehrlein and Surendra, *JVST A* 1994 — RIE-lag model for
  contact holes.[^joubert-1994]
* Doemling, Rueger and Oehrlein, *Appl. Phys. Lett.* 1996 — inverse
  RIE lag.[^doemling-1996]
* Gottscho, Jurgensen and Vitkavage, *JVST B* 1992 — microscopic
  uniformity and ARDE.[^gottscho-1992]
* Oehrlein and Kurogi, *Mater. Sci. Eng. R* 1998 — sidewall
  chemistry and profile control.[^oehrlein-1998]
* Fonash, *J. Electrochem. Soc.* 1990, and Oehrlein, *Mater. Sci.
  Eng. B* 1989 — etch damage and contamination.[^fonash-1990][^oehrlein-1989]
* Cacciato et al., P2ID 2003, and Hashimoto, *JJAP* 1994 — charging
  damage during contact etch; electron shading.[^cacciato-2003][^hashimoto-1994]
* Yin et al. (Applied Materials), US 5,540,824 — the DPS
  reactor.[^pat-dps-amat]
* Tokyo Electron, US 6,376,262 — double endpoint detection for
  layered stacks.[^pat-cn-tel]
* Tang et al. (TI), IEDM 1985 — the local-interconnect scheme in
  which nitride over poly is removed only at contact sites.[^tang-1985]

## Open questions

* The etch chemistry, tool, endpoint and over-etch are not public;
  SkyWater's list names no dedicated dielectric etcher, so which
  tool performs the contact etch is an open question.
* Whether the resist strip and post-etch clean are done in this
  step, in {ref}`SACETCH <step-095>`, or separately is not stated
  publicly.
* The oxide thickness at the bottom of the diffusion contacts
  ({ref}`SPOX <step-080>` plus any {ref}`IOX45 <step-063>` residue)
  that the over-etch must clear is not public.
* Whether the holes over poly are shallower than those over
  diffusion (the {ref}`CMPP <step-090>` cap-stop reading) is not
  public.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report*.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^lam-exelan]: Lam Research, *Lam Research Corporation Advances
    Dielectric Etch Capabilities With Launch Of Exelan High
    Performance*, press release, 2001-07-09.
    <https://newsroom.lamresearch.com/2001-07-09-Lam-Research-Corporation-Advances-Dielectric-Etch-Capabilities-With-Launch-Of-Exelan-R-High-Performance>
[^lam-10k]: Lam Research Corporation, Form 10-K for the fiscal year
    ended 2003-06-29 (product line: TCP 9400PTX/DFM, 2300, Exelan).
    <https://www.sec.gov/Archives/edgar/data/707549/000089161803004913/f93126e10vk.htm>
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^nojiri-2015]: K. Nojiri, *Dry Etching Technology for Semiconductors*,
    Springer, 2015. <https://doi.org/10.1007/978-3-319-10295-5>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^flamm-1981]: D. L. Flamm and V. M. Donnelly, "The design of plasma
    etchants", *Plasma Chemistry and Plasma Processing* **1**(4),
    317–363 (1981). <https://doi.org/10.1007/BF00565992>
[^winters-1992]: H. F. Winters and J. W. Coburn, "Surface science
    aspects of etching reactions", *Surface Science Reports*
    **14**(4–6), 162–269 (1992).
    <https://doi.org/10.1016/0167-5729(92)90009-Z>
[^oehrlein-1994-ii]: G. S. Oehrlein, Y. Zhang, D. Vender and
    O. Joubert, "Fluorocarbon high-density plasmas. II. Silicon dioxide
    and silicon etching using CF₄ and CHF₃", *Journal of Vacuum Science
    & Technology A* **12**(2), 333–344 (1994).
    <https://doi.org/10.1116/1.578877>
[^rueger-1997]: N. R. Rueger, J. J. Beulens, M. Schaepkens,
    M. F. Doemling, J. M. Mirza, T. E. F. M. Standaert and
    G. S. Oehrlein, "Role of steady state fluorocarbon films in the
    etching of silicon dioxide using CHF₃ in an inductively coupled
    plasma reactor", *Journal of Vacuum Science & Technology A*
    **15**(4), 1881–1889 (1997). <https://doi.org/10.1116/1.580655>
[^standaert-1998]: T. E. F. M. Standaert, M. Schaepkens, N. R. Rueger,
    P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "High density
    fluorocarbon etching of silicon in an inductively coupled plasma:
    Mechanism of etching through a thick steady state fluorocarbon
    layer", *Journal of Vacuum Science & Technology A* **16**(1),
    239–249 (1998). <https://doi.org/10.1116/1.580978>
[^schaepkens-1999]: M. Schaepkens, T. E. F. M. Standaert, N. R. Rueger,
    P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "Study of the
    SiO₂-to-Si₃N₄ etch selectivity mechanism in inductively coupled
    fluorocarbon plasmas and a comparison with the SiO₂-to-Si
    mechanism", *Journal of Vacuum Science & Technology A* **17**(1),
    26–37 (1999). <https://doi.org/10.1116/1.582108>
[^joubert-1994]: O. Joubert, G. S. Oehrlein and M. Surendra,
    "Fluorocarbon high density plasma. VI. Reactive ion etching lag
    model for contact hole silicon dioxide etching in an electron
    cyclotron resonance plasma", *Journal of Vacuum Science &
    Technology A* **12**(3), 665–670 (1994).
    <https://doi.org/10.1116/1.578850>
[^doemling-1996]: M. F. Doemling, N. R. Rueger and G. S. Oehrlein,
    "Observation of inverse reactive ion etching lag for silicon
    dioxide etching in inductively coupled plasmas", *Applied Physics
    Letters* **68**(1), 10–12 (1996). <https://doi.org/10.1063/1.116772>
[^gottscho-1992]: R. A. Gottscho, C. W. Jurgensen and D. J. Vitkavage,
    "Microscopic uniformity in plasma etching", *Journal of Vacuum
    Science & Technology B* **10**(5), 2133–2147 (1992).
    <https://doi.org/10.1116/1.586180>
[^oehrlein-1998]: G. S. Oehrlein and Y. Kurogi, "Sidewall surface
    chemistry in directional etching processes", *Materials Science and
    Engineering: R* **24**(4), 153–183 (1998).
    <https://doi.org/10.1016/S0927-796X(98)00016-3>
[^fonash-1990]: S. J. Fonash, "An Overview of Dry Etching Damage and
    Contamination Effects", *Journal of The Electrochemical Society*
    **137**(12), 3885–3892 (1990). <https://doi.org/10.1149/1.2086322>
[^oehrlein-1989]: G. S. Oehrlein, "Dry etching damage of silicon: A
    review", *Materials Science and Engineering: B* **4**(1–4), 441–450
    (1989). <https://doi.org/10.1016/0921-5107(89)90284-5>
[^cacciato-2003]: A. Cacciato, A. Scarpa, S. Evseev and M. Diekema,
    "Charging damage during contact etch triggered by increased
    borderless nitride conductivity", *Proc. 2003 8th International
    Symposium on Plasma- and Process-Induced Damage*, pp. 20–23.
    <https://doi.org/10.1109/PPID.2003.1199721>
[^hashimoto-1994]: K. Hashimoto, "Charge Damage Caused by Electron
    Shading Effect", *Japanese Journal of Applied Physics* **33**(10R),
    6013 (1994). <https://doi.org/10.1143/JJAP.33.6013>
[^pat-dps-amat]: G. Z. Yin, H. Hanawa, D. X. Ma and D. Olgado (Applied
    Materials), *Plasma reactor with multi-section RF coil and isolated
    conducting lid*, US 5,540,824 A, granted 1996-07-30.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5540824>
[^pat-cn-tel]: Tokyo Electron Ltd., *Method of forming a semiconductor
    device using double endpoint detection*, US 6,376,262 B1, granted
    2002-04-23 (CN emission at 387 nm as the nitride etch endpoint
    signal). <https://patents.google.com/patent/US6376262B1/en>
[^tang-1985]: T. E. Tang, C.-C. Wei, R. A. Haken, T. C. Holloway,
    C.-F. Wan and M. A. Douglas, "VLSI local interconnect level using
    titanium nitride", *IEDM 1985 Technical Digest*, pp. 590–593.
    <https://doi.org/10.1109/IEDM.1985.191041>
