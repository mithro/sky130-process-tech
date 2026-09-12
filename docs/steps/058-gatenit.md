(step-058)=
# Step 058 — GATENIT: Gate poly nitride deposition

| | |
|---|---|
| **Step number** | 58 of 171 |
| **Step code** | `GATENIT` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | FEOL — gate and poly resistors |
| **Previous step** | {ref}`UPRIS <step-057>` |
| **Next step** | {ref}`POC <step-059>` |

## What this step is

`GATENIT` deposits a blanket silicon nitride film on top of the doped
gate poly. Together with the oxide cap that follows
({ref}`POC <step-059>`) it completes the gate *stack* — gate oxide,
0.18 µm poly,[^pdk-03] nitride, oxide — that is patterned at
{ref}`P1M <step-061>` and etched at {ref}`P1ME <step-062>`. The
thickness, deposition method and precise purpose of the nitride are
not public; what follows is our inference from the PDK's public
rules.

The most informative public fact is what happens to this film later.
The PDK's mask table lists a "Nitride Poly Cut, NPCM" mask,[^pdk-05]
the drawn layer `npc` (GDS 95:20) is described as "Nitride poly cut
(under licon1 areas)",[^pdk-06] and the rules require every precision
resistor to be enclosed by `npc` by 0.095 µm (rpm.5) and keep `npc`
0.090 µm from any gate (npc.4).[^pdk-periph] In the step list used
here the nitride cut ({ref}`NPCM <step-078>`/{ref}`NPCME <step-079>`)
comes *after* the {term}`spacer` etch ({ref}`SPE <step-077>`) and
before the source/drain masks. We therefore infer that the nitride
deposited here stays on top of the poly through gate etch, spacer
formation and the source/drain implants, and is opened only where the
local-interconnect contacts must reach the poly. The assumptions
table's "poly cap after SPE" of 0.2 µm[^pdk-03] is, on this reading,
the thickness of cap material still standing on the gate after the
spacer etch; the table does not define the term further.

## Step category

`GATENIT` is a {ref}`Thin-film deposition <category-deposition>` step:
a silicon nitride deposited either by furnace {term}`LPCVD` from
dichlorosilane and ammonia or by {term}`PECVD` from silane and ammonia. Both
are on SkyWater's public capability list — "LPCVD nitride" among the
Aviza furnace processes, and "PECVD nitride C1" and "PECVD silane
oxide/nitride/oxynitride, C1" among the PECVD tools[^skw-01] — and no
public source says which is used here. What distinguishes this
nitride from {ref}`ISONIT <step-003>` and {ref}`SPNIT <step-076>` is
that it is deposited on a *doped silicon film* rather than on oxide,
and that its optical properties at the exposure wavelength may matter
as much as its mechanical ones.

## Why this step exists

A nitride cap on a poly gate can serve several purposes, and the
public evidence supports more than one of them:

* **{term}`Hard mask <hard mask>` and anti-reflective layer for the gate
  lithography.** Poly is highly reflective at 248 nm, the wavelength we infer
  for the gate layer ({ref}`P1M <step-061>`), and a gate printed at
  0.15 µm[^pdk-periph] needs reflectivity control. Silicon {term}`oxynitride`
  and nitride films deposited by PECVD were the standard *inorganic*
  anti-reflective layers of the KrF generation: Ogawa et al. demonstrated a
  "complete antireflective layer" of this kind for KrF
  lithography,[^ogawa-1993] Dijkstra and Juffermans showed how to optimise its
  thickness and index,[^dijkstra-1993] Czech et al. used one specifically to
  reduce linewidth variation at the gate-conductor level,[^czech-1993] and He
  et al. describe a production inorganic {term}`ARC` process for
  deep-UV.[^he-1998] Such a layer doubles as a hard mask: Bell and Joubert
  compared gate etches masked by resist and by a hard mask,[^bell-1997] and the
  resist can be stripped before the poly is etched, which improves the profile
  and removes the resist's contribution to line-edge
  roughness.[^desvoivres-2000] Whether SKY130 uses the nitride this way, or
  relies on an organic {term}`BARC` as well, is not public
  ({ref}`P1M <step-061>`).
* **A cap that stays.** Because the nitride is cut only under contacts
  ({ref}`NPCM <step-078>`), the gate poly is sealed during the tip,
  {term}`halo` and source/drain implants. That is consistent with — and, we
  infer, the reason for — doping the gate *before* patterning at
  {ref}`P1I <step-050>`: a capped gate cannot be doped by the
  source/drain implants, as in a conventional dual-gate flow.[^wong-1988]
  A sealed gate also cannot lose dopant or be {term}`counter-doped <counter-doping>`, and its
  top surface is protected from the plasma and wet steps that follow.
* **Resistor protection.** The precision resistors are enclosed by
  `npc` with a defined margin,[^pdk-periph] so their bodies remain
  capped and are contacted only at their ends through the cut; the
  cap is part of what makes the resistor's end resistance
  reproducible.
* **A stop layer.** The step list used in this reference contains a "CMP over
  poly" ({ref}`CMPP <step-090>`) after the sacrificial {term}`PSG` deposition;
  a nitride on top of the poly is the natural polish stop for such a step, as
  the {term}`STI` nitride is for {ref}`CMPNIT <step-012>`. This is an
  inference from the step order only.

Without a cap, the gate would be doped by every later implant, the
gate lithography would print on bare reflective poly, and the
resistor ends would be defined by the contact etch alone.

## How it is typically performed

Two industry-generic routes for a 200 mm, 130 nm-era fab:

* **LPCVD nitride.** Dichlorosilane and ammonia in a hot-wall furnace
  at roughly 700–800 °C and a few hundred mTorr (typical industry
  values, category page[^txt-02][^wiki-sin]); Roenigk and Jensen model
  the reactor,[^roenigk-1987] and Habraken and Kuiper review the film
  properties.[^habraken-1994] The film is stoichiometric, dense, about
  1 GPa tensile[^temple-boyer-1998] and deposits on both sides of the
  wafer — one reason a {term}`backside film removal`
  ({ref}`BFR <step-060>`) follows. The deposition temperature would
  crystallise the amorphous gate film and begin activating its
  dopants, which is not necessarily unwelcome.
* **PECVD nitride.** Silane and ammonia (with N₂) in a single-wafer
  chamber at about 300–400 °C; Smith et al. describe the deposition
  mechanism,[^smith-1990] and Claassen et al. how temperature,
  pressure, gas ratio and RF frequency set the film's composition and
  stress.[^claassen-1985] The film is hydrogen-rich, its stress can be
  tuned from tensile to compressive, and — decisive for the ARC role —
  its refractive index and extinction coefficient at 248 nm can be set
  by the N/Si ratio, which is how "silicon oxime"-type dielectric ARCs
  are made.[^pat-oxime-amd] A PECVD film keeps the poly amorphous and
  coats only the front side.
* **Thickness.** Not public. An ARC is tuned to a few tens of
  nanometres; a hard mask or {term}`CMP` stop is thicker. The PDK's 0.2 µm
  "poly cap after SPE"[^pdk-03] suggests the cap *stack* (nitride plus
  oxide) is of hard-mask thickness, if our reading of that entry is
  right.
* **Metrology.** Thickness and refractive index by spectroscopic
  ellipsometry (for an ARC, also the extinction coefficient at the
  exposure wavelength); stress by wafer bow on monitors; particles.

## Machines typically used

* **Vertical LPCVD furnace** (SVG/Thermco–ASML–Aviza AVP/RVP, Kokusai,
  TEL Alpha-8S, ASM A400) with DCS/NH₃ gas panel, *or*
* **PECVD system** (Novellus Concept One/Two and Sequel, Applied
  Materials Precision 5000 / Centura DxZ / Producer) with SiH₄/NH₃/N₂.
* **Spectroscopic ellipsometer**; **stress gauge**.

## Machines likely used at SkyWater

* **Aviza furnace (LPCVD nitride)** — "Furnaces are all made by
  Aviza", with LPCVD nitride listed.[^skw-01] Strength: strong for
  existence; assignment to this step is an inference.
* **"C1" PECVD system (PECVD nitride)** — SkyWater lists "PECVD nitride
  C1" and "PECVD silane oxide/nitride/oxynitride, C1" among its
  Lam/Novellus/AMAT film tools;[^skw-01] the
  {ref}`public-sources inventory <references-public-sources>` (§9)
  reads "C1" as a Novellus Concept One class tool, which is an
  inference. Strength: strong for the capability; weak for the model.
* Which of the two deposits the gate nitride is not public.

## Resources required

* **Dichlorosilane and ammonia** (LPCVD)[^wiki-sin] or **silane,
  ammonia and nitrogen** (PECVD).[^wiki-pecvd]
* **Nitrogen** purge; **NF₃ or CF₄/O₂** chamber clean for a PECVD tool;
  HCl-tolerant exhaust and ammonium-chloride trap maintenance for a
  nitride furnace.[^txt-02]
* **Quartz ware** (furnace) or **chamber consumables** (PECVD).
* **Monitor wafers.**

## Related steps and cross-references

* Previous: {ref}`UPRIS <step-057>` (the clean the film is deposited
  on). Next: {ref}`POC <step-059>` (the oxide cap on top of it).
* Backside film removed at {ref}`BFR <step-060>`; patterned at
  {ref}`P1M <step-061>`/{ref}`P1ME <step-062>`; cut under contacts at
  {ref}`NPCM <step-078>`/{ref}`NPCME <step-079>`; possible polish stop
  at {ref}`CMPP <step-090>`.
* Other nitrides: {ref}`ISONIT <step-003>` (STI), {ref}`ONO <step-040>`
  ({term}`SONOS`), {ref}`SPNIT <step-076>` (spacer), {ref}`LINIT <step-104>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, *Masks* page — "Nitride Poly Cut, NPCM".[^pdk-05]
* SkyWater PDK, *Layers Reference* — `npc` "Nitride poly cut (under
  licon1 areas)".[^pdk-06]
* SkyWater PDK, *Periphery rules* — npc.1–npc.5, rpm.5.[^pdk-periph]
* SkyWater PDK, *Criteria & Assumptions* — poly 0.18 µm; "poly cap
  after SPE" 0.2 µm.[^pdk-03]
* SkyWater, *Facilities & Capabilities* — LPCVD nitride on Aviza
  furnaces; "PECVD nitride C1".[^skw-01]
* Foote and Gupta (AMD), US 5,710,067 — a silicon-oxynitride-type
  dielectric ARC.[^pat-oxime-amd]

### High-level understanding

* Wikipedia, *Silicon nitride* — LPCVD and PECVD nitride.[^wiki-sin]
* Wikipedia, *Plasma-enhanced chemical vapor deposition*.[^wiki-pecvd]
* Wikipedia, *Anti-reflective coating* — inorganic ARCs.[^wiki-arc]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  {term}`CVD` nitride.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — gate stacks
  and {term}`DUV` reflectivity control.[^txt-05]

### Deep dive

* Ogawa et al., SPIE 1993 — the "complete antireflective layer" for
  KrF lithography, the origin of inorganic DARC.[^ogawa-1993]
* Dijkstra and Juffermans, SPIE 1993 — optimisation of
  anti-reflection layers for deep-UV.[^dijkstra-1993]
* Czech et al., *Microelectron. Eng.* 1993 — linewidth-variation
  reduction at the gate level with a new ARC.[^czech-1993]
* He et al., SPIE 1998 — an inorganic ARC process for deep-UV in
  production.[^he-1998]
* Foote and Gupta (AMD), US 5,710,067 — silicon oxime dielectric ARC
  film.[^pat-oxime-amd]
* Bell and Joubert, *J. Vac. Sci. Technol. B* 1997 — resist- versus
  hard-mask-masked poly gate etching.[^bell-1997]
* Desvoivres, Vallier and Joubert, *J. Vac. Sci. Technol. B* 2000 —
  sub-0.1 µm gate etch with hard masks and its limits.[^desvoivres-2000]
* Wong et al. (IBM), IEDM 1988 — gate doping by source/drain implants,
  the route a capped gate forgoes.[^wong-1988]
* Smith et al., *J. Electrochem. Soc.* 1990 — mechanism of PECVD SiNₓHᵧ
  deposition from NH₃/SiH₄.[^smith-1990]
* Claassen et al., *J. Electrochem. Soc.* 1985 — PECVD nitride
  composition and stress versus deposition conditions.[^claassen-1985]
* Roenigk and Jensen, *J. Electrochem. Soc.* 1987 — LPCVD nitride
  reactor model.[^roenigk-1987]
* Habraken and Kuiper, *Mater. Sci. Eng. R* 1994 — nitride and
  oxynitride film properties.[^habraken-1994]
* Temple-Boyer et al., *J. Vac. Sci. Technol. A* 1998 — residual
  stress of LPCVD nitride.[^temple-boyer-1998]
* Teasdale et al., *Electrochem. Solid-State Lett.* 2001 —
  single-wafer RTCVD nitride, a third route.[^teasdale-2001]
* ITRS 2001, *Lithography* — reflectivity control and hard masks at
  the node.[^itrs-03]

## Open questions

* Whether the gate nitride is LPCVD or PECVD, and its thickness,
  stoichiometry and optical constants, are not public.
* Whether it functions as the anti-reflective layer for
  {ref}`P1M <step-061>`, as a hard mask for {ref}`P1ME <step-062>`, as
  a polish stop for {ref}`CMPP <step-090>`, or as all three, is
  inferred from the step order and the PDK rules, not stated.
* The meaning of the PDK's "poly cap after SPE" (0.2 µm) entry is our
  reading; the table does not define it.
* Whether the gate is ever doped through or around the cap by later
  implants is not public; with a 0.2 µm cap[^pdk-03] and no nitride cut
  over gates (npc.4)[^pdk-periph] we read the gates as keeping the n⁺
  doping of {ref}`P1I <step-050>` on both NMOS and PMOS.

<!-- footnotes -->

[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^pat-oxime-amd]: D. K. Foote and S. Gupta (Advanced Micro Devices),
    *Silicon oxime film*, US 5,710,067 A, filed 1995-06-07, granted
    1998-01-20. <https://patents.google.com/patent/US5710067A/en>
[^wiki-sin]: Wikipedia, *Silicon nitride*.
    <https://en.wikipedia.org/wiki/Silicon_nitride>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^wiki-arc]: Wikipedia, *Anti-reflective coating*.
    <https://en.wikipedia.org/wiki/Anti-reflective_coating>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^ogawa-1993]: T. Ogawa, M. Kimura, T. Gocho, Y. Tomo and T. Tsumori,
    "Practical resolution enhancement effect by new complete
    antireflective layer in KrF excimer laser lithography", *Proc.
    SPIE* **1927**, Optical/Laser Microlithography VI, 263 (1993).
    <https://doi.org/10.1117/12.150431>
[^dijkstra-1993]: H. J. Dijkstra and C. A. H. Juffermans,
    "Optimization of antireflection layers for deep-UV lithography",
    *Proc. SPIE* **1927**, Optical/Laser Microlithography VI, 275
    (1993). <https://doi.org/10.1117/12.150432>
[^czech-1993]: G. Czech, L. Mader, K. H. Küsters, P. Küppers and
    A. Gutmann, "Reduction of linewidth variation for the gate
    conductor level by lithography based on a new antireflective
    layer", *Microelectronic Engineering* **21**(1–4), 51–56 (1993).
    <https://doi.org/10.1016/0167-9317(93)90025-Z>
[^he-1998]: Q. He, W. W. Lee, M. A. Hanratty, D. Rogers, G. Xing,
    A. Singh and E. Zielinski, "Inorganic antireflective coating process
    for deep-UV lithography", *Proc. SPIE* **3334**, Optical
    Microlithography XI, 337 (1998). <https://doi.org/10.1117/12.310763>
[^bell-1997]: F. H. Bell and O. Joubert, "Polysilicon gate etching in
    high density plasmas. V. Comparison between quantitative chemical
    analysis of photoresist and oxide masked polysilicon gates etched in
    HBr/Cl₂/O₂ plasmas", *Journal of Vacuum Science & Technology B*
    **15**(1), 88–97 (1997). <https://doi.org/10.1116/1.589259>
[^desvoivres-2000]: L. Desvoivres, L. Vallier and O. Joubert,
    "Sub-0.1 μm gate etch processes: Towards some limitations of the
    plasma technology?", *Journal of Vacuum Science & Technology B*
    **18**(1), 156–165 (2000). <https://doi.org/10.1116/1.591168>
[^wong-1988]: C. Y. Wong, J. Y. Sun, Y. Taur, C. S. Oh, R. Angelucci
    and B. Davari, "Doping of n⁺ and p⁺ polysilicon in a dual-gate CMOS
    process", *IEDM 1988 Technical Digest*, pp. 238–241.
    <https://doi.org/10.1109/IEDM.1988.32800>
[^smith-1990]: D. L. Smith, A. S. Alimonda, C.-C. Chen, S. E. Ready and
    B. Wacker, "Mechanism of SiNₓHᵧ Deposition from NH₃-SiH₄ Plasma",
    *Journal of The Electrochemical Society* **137**(2), 614–623 (1990).
    <https://doi.org/10.1149/1.2086517>
[^claassen-1985]: W. A. P. Claassen, W. G. J. N. Valkenburg,
    M. F. C. Willemsen and W. M. v. d. Wijgert, "Influence of Deposition
    Temperature, Gas Pressure, Gas Phase Composition, and RF Frequency
    on Composition and Mechanical Stress of Plasma Silicon Nitride
    Layers", *Journal of The Electrochemical Society* **132**(4),
    893–898 (1985). <https://doi.org/10.1149/1.2113980>
[^roenigk-1987]: K. F. Roenigk and K. F. Jensen, "Low Pressure CVD of
    Silicon Nitride", *Journal of The Electrochemical Society*
    **134**(7), 1777–1785 (1987). <https://doi.org/10.1149/1.2100756>
[^habraken-1994]: F. H. P. M. Habraken and A. E. T. Kuiper, "Silicon
    nitride and oxynitride films", *Materials Science and Engineering:
    R: Reports* **12**(3), 123–175 (1994).
    <https://doi.org/10.1016/0927-796X(94)90006-X>
[^temple-boyer-1998]: P. Temple-Boyer, C. Rossi, E. Saint-Etienne and
    E. Scheid, "Residual stress in low pressure chemical vapor
    deposition SiNₓ films deposited from silane and ammonia", *Journal
    of Vacuum Science & Technology A* **16**(4), 2003–2007 (1998).
    <https://doi.org/10.1116/1.581302>
[^teasdale-2001]: D. Teasdale, Y. Senzaki, R. Herring, G. Hoeye,
    L. Page and P. Schubert, "LPCVD of Silicon Nitride from
    Dichlorosilane and Ammonia by Single Wafer Rapid Thermal
    Processing", *Electrochemical and Solid-State Letters* **4**(5),
    F11 (2001). <https://doi.org/10.1149/1.1359056>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
