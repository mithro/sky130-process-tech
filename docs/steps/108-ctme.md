(step-108)=
# Step 108 — CTME: Metal contact mask etch

| | |
|---|---|
| **Step number** | 108 of 171[^steps-sheet] |
| **Step code** | `CTME` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | BEOL — contact and metal 1 |
| **Previous step** | {ref}`CTM1 <step-107>` |
| **Next step** | {ref}`TIN2 <step-109>` |

## What this step is

`CTME` etches the metal-contact holes. Through the resist openings of
{ref}`CTM1 <step-107>` a fluorocarbon plasma cuts the
{ref}`NILD2 <step-105>` oxide — planarised at {ref}`CMPL <step-106>`
(on our reading) — down to the titanium nitride {term}`local interconnect`,
producing the holes that {ref}`TIN2 <step-109>` will line and
{ref}`WDEP2 <step-110>` will fill to make the `mcon` plug, "Contact
from local interconnect to metal1".[^pdk-06] The resist is stripped
afterwards; this reference treats the strip and post-etch clean as
part of this step.

The public dimensions are those of the mask: a 0.170 µm square
(ct.1) on a 0.190 µm space (ct.2),[^pdk-periph] a "min. etch and fill
capability for mcon" of 0.14 µm, and a "Standard contact bottom CD"
of 0.09 µm in the PDK's laser-fuse table.[^pdk-03] The depth is
about 0.34 µm on our reading of the stack diagram, which puts the
bottom of `li` at 0.9361 µm and the bottom of `met1` at 1.3761 µm,
with 0.1 µm of `li`, 0.075 µm of LINT and 0.265 µm of NILD2 between
them.[^pdk-04] What the etch lands on is,
on our reading, not bare TiN but the "LINT" nitride cap of 0.075 µm
(k 7.3) that the diagram draws over the local interconnect[^pdk-04]
and that {ref}`LINIT <step-104>` deposits — so the etch is an oxide
etch that must first stop on nitride, then open the nitride to reach
the 0.10 µm `li`,[^pdk-04] without punching through it. Where an
`mcon` sits with zero enclosure at the edge of an `li` line
(ct.4),[^pdk-periph] part of the hole floor is the
{ref}`LINIT <step-104>` nitride and the {ref}`NILD2 <step-105>` oxide
that fills the space beside the line (inference); the etch must not
trench there, since a further 0.10 µm[^pdk-04] would take it past the
bottom of `li` into the {ref}`PSG <step-089>` or
{ref}`NCAPOX <step-091>` pre-metal dielectric.

## Step category

`CTME` is an {ref}`Etch <category-etch>` step of the *dielectric,
fluorocarbon* class — the same chemistry family as the trench and
local-contact etches ({ref}`LICM1E <step-094>`) and the {term}`via` etches
above ({ref}`VIME <step-119>`) — with two properties that mark it
out: it is a high-aspect-ratio hole rather than a line, so
{term}`ARDE` and polymer build-up at the bottom govern the recipe;
and its etch stop is a nitride-capped metal, so the {term}`selectivity`
that matters is oxide-to-nitride and then nitride-to-TiN, not
oxide-to-silicon. The category page's summary of fluorocarbon oxide
etching — fluorine removes oxide only under ion bombardment while the
carbon forms a polymer that protects nitride and silicon — is the
mechanism at work.[^flamm-1981][^winters-1992]

## Why this step exists

The contact hole sets the resistance and the reliability of every
connection between a device and the metal system:

* **Contact area.** The PDK's extraction tables give an `mcon`
  152 000 mΩ — 152 Ω — against 15 000 mΩ for a `licon` and 4 500 mΩ
  for a `via` (per-contact reading of the PDK's "Resistivity
  (mohms/sq)" column; see {ref}`CTM1 <step-107>`).[^pdk-08] A
  W-to-TiN interface of 0.09 µm bottom
  {term}`CD`[^pdk-03] has little more than a quarter of the drawn area of the
  0.17 µm top, and the taper the etch leaves, together with the
  interfacial layer the {term}`liner` forms, is on our reading why the number
  is so high. Ohmic contact to TiN is a metal–metal contact, so the
  dominant term is interfacial rather than a Schottky barrier
  ({term}`sheet resistance` and contact resistance are treated in the
  PDK's parasitic tables[^pdk-08]).
* **Etch-stop integrity.** If the etch breaks through the 0.10 µm
  `li`[^pdk-04] the tungsten plug reaches whatever is below — the
  {term}`PSG` over a gate or the {term}`silicide` — and the local-interconnect scheme
  fails; if it under-etches, nitride or polymer remains at the bottom
  and the contact is open or resistive. The etch must therefore have
  an oxide-to-nitride selectivity high enough to stop on 0.075 µm of
  nitride[^pdk-04] with margin for the oxide thickness variation that
  {ref}`CMPL <step-106>` leaves, then a controlled nitride
  breakthrough. Schaepkens et al. worked out how oxide-to-nitride
  selectivity arises in inductively coupled fluorocarbon
  plasmas,[^schaepkens-1999] and Oehrlein's group how the steady-state
  fluorocarbon film governs oxide versus silicon
  etching.[^oehrlein-1994b][^standaert-1998]
* **Profile.** A slight taper helps the liner and the tungsten fill
  ({ref}`TIN2 <step-109>`, {ref}`WDEP2 <step-110>`); bowing or
  undercut leaves voids in the plug. The "Bowing of rectangular
  contact (per edge)" entry of 0.015 µm in the PDK's assumptions
  table[^pdk-03] is a public trace of this concern, framed there for
  seal-ring sizing.
* **Charging.** A contact etch that lands on a conductor connected to
  a gate can inject charge through the gate oxide; Cacciato et al.
  describe charging damage during a contact etch triggered by the
  conductivity of the nitride it lands on.[^cacciato-2003]

Without `CTME` the resist pattern of {ref}`CTM1 <step-107>` would be
stripped without effect and metal 1 would sit on unbroken oxide.

## How it is typically performed

An industry-generic contact etch for a 200 mm, 130 nm-era fab
(SKY130's recipe is not public):

1. **Chamber.** A single-wafer dielectric etcher — a medium-density
   capacitively coupled or a high-density inductively coupled
   reactor with separate bias — with helium backside cooling, a
   cooled {term}`electrostatic chuck` and optical-emission {term}`endpoint`
   ({ref}`category-etch`). Lam launched the Exelan dual-frequency
   dielectric etcher for this generation in 2001.[^lam-exelan]
2. **BARC open.** If an organic {term}`BARC` was used at
   {ref}`CTM1 <step-107>`, a short O₂/N₂ or CF₄-containing step opens
   it through the resist holes.
3. **Main oxide etch.** A polymerising fluorocarbon — C₄F₈ or C₂F₆ or
   CHF₃ with Ar, and a little O₂ or CO to tune the fluorine-to-carbon
   ratio — at a few tens of mTorr and high bias. Fluorine etches oxide
   as SiF₄ only where ions strike; the carbon-rich film that forms on
   nitride slows the etch there, which is the source of
   selectivity;[^flamm-1981][^winters-1992][^schaepkens-1999] Perry et
   al. give etch rates and selectivities for a high-density C₂F₆ oxide
   etch,[^perry-2001] and Oehrlein et al. the CF₄/CHF₃ high-density
   behaviour on oxide and silicon.[^oehrlein-1994b] In a 0.17 µm hole
   the flux of neutrals and ions to the floor is throttled by the
   hole itself — Coburn and Winters' conductance
   argument[^coburn-1989] — so the rate falls with depth
   ({term}`ARDE`), and can under some conditions run the other way,
   the "inverse RIE lag" Doemling et al. observed.[^doemling-1996]
   Gottscho, Jurgensen and Vitkavage review the whole family of
   aspect-ratio and loading effects.[^gottscho-1992]
4. **Endpoint and over-etch.** Contact layers expose a small fraction
   of the wafer (the {term}`loading effect` is small and the emission
   signal weak), which is why endpoint on such layers needs
   specialised detection — Wodecki describes a low-open-area
   multilayer dielectric endpoint method[^wodecki-1999] — or is run
   by time with a monitor. The {term}`over-etch` clears the deepest holes
   while the nitride cap protects the `li`.
5. **Nitride breakthrough.** A short, less polymerising step (CF₄ or
   CHF₃/O₂) removes the LINT nitride from the hole floor (on our
   reading of the stack), with selectivity to the TiN below
   ({ref}`category-etch`); Kastenmeier et al. give the nitride
   chemistry.[^kastenmeier-1996] The bottom CD is set here.
6. **Strip and clean.** Oxygen plasma {term}`ash` — GaSonics, Mattson
   or Iridia class in SkyWater's list[^skw-01] — followed by a solvent
   or semi-aqueous clean (SkyWater lists "EKS265, EKC270 solvents"
   under "Batch Rotational"[^skw-01]; EKC265/EKC270-type amine
   solvents) to remove the fluorocarbon
   polymer from the sidewalls and the metal-oxide residue from the
   TiN floor without attacking the TiN. No HF is used (inference:
   it would widen the hole and etch the exposed oxide).
7. **Metrology.** Top and bottom CD by {term}`CD-SEM`, depth and
   profile by cross-section SEM on monitors, contact-chain resistance
   at {term}`e-test`; the 152 Ω `mcon` of the PDK[^pdk-08] is the kind
   of number such chains give. The published SKY130 {term}`test tile`
   has an "M1-LI1 contacts: mcon = 0.17 um" string of 3600 contacts,
   "M1-LI1-N+" and "M1-LI1-P+" contact strings of 6384 and 6992, and
   "M1-LI contact Kelvin" structures drawn with ".05 LI enclosure" and
   "-.01 LI enclosure".[^raw-data-testtile-pads]

## Machines typically used

* **{ref}`Dielectric etcher <machine-plasma-etcher-dielectric>`**, 200 mm single-wafer: Lam Exelan / 4520XLE,
  Applied Materials eMax / MxP+ / Super-e, TEL DRM / Unity
  ({ref}`category-etch`); high-density alternatives (AMAT IPS, Lam
  {term}`TCP` 9100).
* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`** (GaSonics Aura, Mattson Aspen) and **{ref}`wet bench <machine-wet-bench>` or
  {ref}`single-wafer clean <machine-single-wafer-spin-processor>`** for post-etch residue.
* **{ref}`CD-SEM <machine-cd-sem-overlay-metrology>`**, **{ref}`cross-section SEM <machine-cross-section-sem-profilers>`**, **{ref}`e-test <machine-parametric-tester>`** for contact chains.

## Machines likely used at SkyWater

* **No dielectric etcher is named on SkyWater's public list.** The
  list gives, under poly/silicon etch, "AMAT DPSII, HBR, Cl2, NF3,
  CF4, CHF3, O2", "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6, O2" and
  "Lam 4400, HBr, Cl2, C2F6, CF4, SF6, O2".[^skw-01] All three carry
  fluorine-bearing gases that can etch oxide; strength: **weak** for
  assignment of any of them to the contact etch (the DPS II line is
  labelled "gate, trench, W/WN"[^skw-01]).
* **Lam Exelan.** No public source places an Exelan at SkyWater; it
  appears here only as the era's typical dielectric etcher, a line
  Lam's own 10-K lists,[^lam-10k][^lam-exelan] its dual-frequency
  confined technology aimed at "sub-130 nm geometries" per the 2001
  launch.
* **Strip and clean — GaSonics PEP, Iridia, Mattson Aspen II; Akrion
  Gamma wet bench; batch rotational tools with "EKS265, EKC270
  solvents"; SEZ 223 / Da Vinci.**[^skw-01] Strength: strong for
  existence.

## Resources required

* **{ref}`C₄F₈ <material-etch-gases>`, C₂F₆, CHF₃, CF₄**, **{ref}`Ar <material-process-gases>`**, **O₂** (and possibly CO or N₂)
  for the oxide and nitride etch steps (industry practice;[^nojiri-2015]
  SkyWater lists CF₄, CHF₃, C₂F₆ and O₂ on its etchers[^skw-01]).
* **Helium** for backside cooling; **NF₃** or O₂-based chamber clean.
* **O₂/N₂** (and {ref}`forming gas <material-anneal-ambients>`) for the ash;[^skw-01] CF₄, listed on
  the Iridia and Mattson ashers,[^skw-01] would attack the exposed TiN and
  would, we infer, be left out. **Amine or semi-aqueous solvent**
  ({ref}`wet chemicals <material-wet-chemicals>`; EKC265/EKC270 class; SkyWater lists "EKS265, EKC270
  solvents"[^skw-01]) and {ref}`DI water <material-ultrapure-water>` for the post-etch clean.
* **{ref}`Chamber consumables <material-hardware-consumables>`** (liners, focus and edge rings, electrodes),
  **{ref}`monitor wafers <material-substrates>`** with blanket oxide and nitride for rate and
  selectivity checks.

## Related steps and cross-references

* Previous: {ref}`CTM1 <step-107>` (the mask). Next:
  {ref}`TIN2 <step-109>` (the liner), then {ref}`WDEP2 <step-110>`
  and {ref}`WCMP2 <step-111>`.
* The films it cuts: {ref}`NILD2 <step-105>` (oxide, planarised at
  {ref}`CMPL <step-106>`) and {ref}`LINIT <step-104>` (the nitride
  cap); the layer it stops on: {ref}`LI1M <step-102>` /
  {ref}`LI1ME <step-103>`.
* The analogous hole etches: {ref}`LICM1E <step-094>` below,
  {ref}`VIME <step-119>` above.
* Category page: {ref}`Etch <category-etch>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 4,948,458 A <patent-gp23554962>` — Method and apparatus for producing magnetically-coupled planar plasma (1989)
* {ref}`US 5,540,824 A <patent-gp23061269>` — Plasma reactor with multi-section RF coil and isolated conducting lid (1994)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, *Periphery rules* — ct.1 0.170 µm, ct.2 0.190 µm,
  ct.4 0.000 µm.[^pdk-periph]
* SkyWater PDK, *Criteria & Assumptions* — mcon etch-and-fill
  capability 0.14 µm; "Standard contact bottom CD" 0.09 µm; contact
  bowing 0.015 µm per edge.[^pdk-03]
* SkyWater PDK, *Process stack diagram* — `li` 0.10 µm, LINT 0.075 µm
  (k 7.3), NILD2 0.265 µm.[^pdk-04]
* SkyWater PDK, *Layers Reference* — `mcon` 67:44.[^pdk-06]
* SkyWater PDK, *Parasitic Layout Extraction* — MCON 152 000 mΩ.[^pdk-08]
* SkyWater, *Facilities & Capabilities* — DPS II, Lam 9400 TCP and
  Lam 4400 gas lists; ashers; EKC solvents.[^skw-01]
* Lam Research, Exelan launch (2001) and 10-K (2003).[^lam-exelan][^lam-10k]
* SKY130 raw-data repository, test-tile pad documentation — the mcon
  contact-string and Kelvin structures of the published test
  tile.[^raw-data-testtile-pads]

### High-level understanding

* Wikipedia, *Reactive-ion etching*, *Dry etching*.[^wiki-rie][^wiki-dry-etch]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — the etch
  chapter; contact formation.[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 —
  high-aspect-ratio contact etching.[^txt-05]
* Nojiri, *Dry Etching Technology for Semiconductors* — oxide etch
  chemistry and endpoint.[^nojiri-2015]

### Deep dive

* Flamm and Donnelly, 1981, and Winters and Coburn, 1992 — the
  surface chemistry of fluorocarbon selectivity.[^flamm-1981][^winters-1992]
* Oehrlein, Zhang, Vender and Joubert, *JVST A* 1994 — oxide and
  silicon etching in CF₄/CHF₃ high-density plasmas.[^oehrlein-1994b]
* Standaert et al., *JVST A* 1998 — etching through a thick
  steady-state fluorocarbon layer.[^standaert-1998]
* Schaepkens et al., *JVST A* 1999 — the oxide-to-nitride selectivity
  mechanism in inductively coupled fluorocarbon plasmas.[^schaepkens-1999]
* Perry et al., *JVST A* 2001 — oxide etch rates and selectivity in a
  high-density C₂F₆ plasma.[^perry-2001]
* Coburn and Winters, *Appl. Phys. Lett.* 1989 — conductance limits
  in high-aspect-ratio feature etching.[^coburn-1989]
* Doemling, Rueger and Oehrlein, *Appl. Phys. Lett.* 1996 — inverse
  RIE lag in oxide etching.[^doemling-1996]
* Gottscho, Jurgensen and Vitkavage, *JVST B* 1992 — aspect-ratio and
  loading effects reviewed.[^gottscho-1992]
* Kastenmeier et al., *JVST A* 1996 — nitride and oxide etching in
  CF₄/O₂/N₂, the breakthrough chemistry.[^kastenmeier-1996]
* Wodecki, SPIE 1999 — endpoint detection on low-open-area
  dielectric etches.[^wodecki-1999]
* Cacciato et al., P2ID 2003 — charging damage during a contact etch
  landing on a conductive nitride.[^cacciato-2003]
* Yin et al. (Applied Materials), US 5,540,824 — the multi-section
  coil DPS reactor SkyWater lists.[^pat-dps-amat]
* Ogle (Lam Research), US 4,948,458 — the transformer-coupled plasma
  source.[^pat-tcp-lam]

## Open questions

* The etch chemistry, chamber, endpoint scheme and over-etch of
  `CTME`, and the resulting profile, are not public; the 0.09 µm
  "Standard contact bottom CD"[^pdk-03] is read here as the finished
  bottom size.
* Whether the etch stops on the LINT nitride and opens it in a
  separate step, or etches oxide and nitride in one recipe, is
  inferred from the stack diagram.[^pdk-04]
* Which etcher runs the step is not public; SkyWater's list names no
  dedicated dielectric etcher.[^skw-01]
* This page treats the resist strip and post-etch clean as part of
  the etch step.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
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
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
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
[^perry-2001]: W. L. Perry, K. Waters, M. Barela and H. M. Anderson,
    "Oxide etch behavior in a high-density, low-pressure, inductively
    coupled C₂F₆ plasma: Etch rates, selectivity to photoresist, plasma
    parameters, and CFx radical densities", *Journal of Vacuum Science
    & Technology A* **19**(5), 2272–2281 (2001).
    <https://doi.org/10.1116/1.1382874>
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
[^cacciato-2003]: A. Cacciato, A. Scarpa, S. Evseev and M. Diekema,
    "Charging damage during contact etch triggered by increased
    borderless nitride conductivity", *Proc. 2003 8th International
    Symposium on Plasma- and Process-Induced Damage*, pp. 20–23.
    <https://doi.org/10.1109/PPID.2003.1199721>
[^pat-dps-amat]: G. Z. Yin, H. Hanawa, D. X. Ma and D. Olgado (Applied
    Materials), *Plasma reactor with multi-section RF coil and isolated
    conducting lid*, US 5,540,824 A, granted 1996-07-30.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5540824>
[^pat-tcp-lam]: J. S. Ogle (Lam Research Corporation), *Method and
    apparatus for producing magnetically-coupled planar plasma*, US
    4,948,458 A, granted 1990-08-14.
    <https://patents.google.com/patent/US4948458A/en>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
