(step-011)=
# Step 011 — FILOX: Fill oxide deposition

| | |
|---|---|
| **Step number** | 11 of 171[^steps-sheet] |
| **Step code** | `FILOX` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | FEOL — isolation |
| **Previous step** | {ref}`LINOX <step-010>` |
| **Next step** | {ref}`CMPNIT <step-012>` |

## What this step is

`FILOX` (fill oxide) deposits a thick blanket of silicon dioxide over
the whole wafer, filling the lined isolation trenches from
{ref}`LINOX <step-010>` and burying the nitride-covered active areas.
This deposited oxide *is* the field oxide of the finished device: the
PDK's stack drawing labels it "FOX K=3.9",[^pdk-04] and after the
polish at {ref}`CMPNIT <step-012>` and the nitride strip at
{ref}`NS19 <step-013>` it is the dielectric that separates every
transistor from its neighbours and on which the field poly and the
first interconnect run.

The film must be thick enough to fill the deepest trench and still
stand well above the nitride everywhere — typically 1.5–2 × the
(trench + nitride) height, i.e. of the order of 0.5–0.7 µm for a
~0.3 µm trench (era-typical figures[^txt-05]). At the 130 nm node the
deposition method is high-density-plasma chemical vapour deposition
({term}`HDP-CVD`): "High Density Plasma (HDP) and Chemical Vapor Deposition
(CVD) is the industry standard for STI oxide",[^thung-2016] and
Novellus was still calling HDP "the preferred gapfill dielectric
technology for advanced geometries" in 2009.[^lam-speed] The PDK gives
no fill thickness; it gives the *final* field-oxide top at 0.3262 µm on
its stack scale[^pdk-04] and the field-oxide step above the silicon
surface under poly as 0.07 µm.[^pdk-03]

## Step category

`FILOX` is a {ref}`Thin-film deposition <category-deposition>` step —
a plasma {term}`CVD` of undoped silicon oxide. It is the first of many CVD
oxides in the flow; later ones ({ref}`PSG <step-089>`,
{ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`, …) fill gaps
between poly and metal lines and use {term}`PECVD` {term}`TEOS`, {term}`PSG` or HDP as the
topography demands. The isolation fill is distinctive because its gaps
are the narrowest and deepest in the front end and because it is
followed immediately by a polish that stops on nitride.

## Why this step exists

The trench is only an isolation structure once it is full of
insulator. The fill has to be:

* **Void-free.** A seam or void in the trench is opened by later
  etches and cleans and then fills with polysilicon at
  {ref}`SAGD <step-048>`, causing "poly stringer" shorts — precisely
  the 0.13 µm yield-loss mechanism analysed by Thung et al. ("HDP
  deposition void at the special Shallow Trench Isolation (STI) wall
  structure causes poly stringer after poly deposition
  process").[^thung-2016]
* **Dense.** The oxide must survive the many HF-containing cleans that
  follow without etching faster than thermal oxide, or it will recess
  below the active surface and form divots at the active edge.
* **Low in hydrogen and moisture.** HDP oxide from silane is "a nearly
  hydrogen-free film",[^wiki-pecvd] but residual hydrogen and moisture
  remain a concern for the gate oxide grown later.[^txt-05]
* **Uniform in thickness** over dense and isolated patterns, because
  the polish at {ref}`CMPNIT <step-012>` has to clear it everywhere
  without over-polishing the nitride. This is why the FOM layer carries
  fill "waffles" in wide field regions.[^pdk-06]

The filled trench also affects the transistors beside it mechanically:
Bianchi, Bouche and Roux-dit-Buisson model the "mobility variations"
that trench-isolation-induced stress causes "on complex MOSFET
geometries".[^bianchi-2002] The published SKY130 test tile includes
transistors that differ only in how far the source/drain diffusion
extends from the gate (`sa` = `sb`, from 2.5 µm down to
0.265 µm).[^raw-data-testtile-pads] As that extent shortens, the drain
current at |V_GS| = |V_DS| = 1.8 V of a 7/0.15 µm `pfet_01v8` rises
from 0.95 mA to 1.38 mA, while that of a 1/0.15 µm `nfet_01v8_lvt`
falls from 0.536 mA to 0.463 mA and that of a 1/0.15 µm `nfet_01v8`
from 0.450 mA to 0.409 mA (our extraction from the published
measurements; one device at each extent; the `nfet_01v8` values do not
fall at every step). Over the same range the thresholds extracted by
maximum-transconductance extrapolation at |V_DS| = 0.1 V also move: the
PMOS threshold magnitude falls by 0.14 V, and the thresholds
of the low-Vt and standard NMOS rise by 0.04 V and 0.03 V, so the
current changes are not due to mobility alone.[^raw-data-lv-mosfets]
We read the opposite trends as consistent with a stress effect of the
kind Bianchi et al. model (inference); the data do not measure stress,
and other effects of the diffusion extent cannot be excluded.

## How it is typically performed

An industry-generic HDP-CVD {term}`STI` fill for a 200 mm, 130 nm-era fab:

1. **Chamber.** Inductively coupled high-density plasma reactor with an
   RF-biased electrostatic chuck; wafer temperature of a few hundred
   °C set by backside helium and plasma heating.[^txt-05] In a
   high-density plasma "the ion density can be high enough that
   significant sputtering of the deposited film occurs; this sputtering
   can be employed to help planarize the film and fill trenches or
   holes".[^wiki-pecvd]
2. **Chemistry.** Silane, oxygen and argon: "High-density plasma
   deposition of silicon dioxide from silane and oxygen/argon has been
   widely used to create a nearly hydrogen-free film with good
   conformality over complex surfaces".[^wiki-pecvd] Argon (and the
   oxygen ions) provide the simultaneous sputter component; the
   deposition-to-sputter ratio is the key tuning parameter for
   gap-fill[^thung-2016] (the Novellus release speaks of "tailoring the
   deposition, etch, and sputter-to-deposition (S/D)
   ratio"[^lam-speed]). A published 0.13 µm STI gap-fill study (space
   width 0.13 µm, {term}`aspect ratio` 3.9) models the same sputter/deposition
   balance in HDP-CVD.[^nishimura-2002]
3. **Sequence.** A short *in-situ* sputter-clean or a thin protective
   liner deposition at low bias (so that the sputter component does
   not clip the nitride corners and redeposit silicon-rich material on
   the trench sidewall), then the main fill at higher bias, then an
   unbiased cap. Multi-step deposition/etch/deposition sequences are
   used for the tightest gaps.
4. **Post-deposition.** Some fabs densify the HDP oxide in a furnace
   or {term}`RTP` anneal in N₂ at around 900–1000 °C;[^txt-05] others rely on
   the later thermal steps. An anneal here also continues the deep N-well
   ({ref}`DNI <step-008>`) drive.
5. **Metrology.** Thickness and uniformity by optical reflectometry;
   in-trench fill quality by cross-section SEM on sample wafers; wet
   etch rate ratio (against thermal oxide) as a density monitor.

SkyWater lists the capability directly: "Lam/Novellus High Density
Plasma (HDP) doped and phos doped with sputter etch" among its film
deposition tools,[^skw-01] and a SkyWater maintenance technician's
profile refers to "a Novellus high density plasma tool".[^skw-07]

## Machines typically used

* **HDP-CVD reactor**, 200 mm single-wafer, multi-chamber cluster:
  Novellus SPEED, Applied Materials Ultima HDP-CVD (Centura), Lam
  (post-2012 Novellus SPEED Max/NExT), Trikon Planar 200. Novellus'
  SPEED platform was the market's long-running STI fill
  tool.[^lam-speed]
* **{ref}`Furnace <machine-vertical-furnace-anneal>` or {ref}`RTP <machine-rapid-thermal-processor>`** for optional densification.
* **Reflectometer / ellipsometer**; **cross-section SEM**.

## Machines likely used at SkyWater

* **Novellus (now Lam) HDP-CVD.** SkyWater names "Lam/Novellus High
  Density Plasma (HDP)" with sputter etch,[^skw-01] and the technician
  profile names "a Novellus high density plasma tool".[^skw-07]
  Strength: strong (two SkyWater statements). The model (SPEED is the
  Novellus HDP product line) is our inference, not a SkyWater
  statement.
* **Aviza furnace** for any densification anneal.[^skw-01] Strength:
  strong for existence; the existence of a densification step is an
  inference.

## Resources required

* **Silane (SiH₄)** — pyrophoric, delivered through gas
  cabinets.[^wiki-pecvd]
* **Oxygen** and **argon**.[^wiki-pecvd]
* **Helium** for backside cooling; **nitrogen** purge.
* **NF₃** (with argon/oxygen) for the remote-plasma chamber clean —
  the Novellus release refers to the "enlarged remote plasma source"
  that "allows more wafers to be processed between plasma
  cleans".[^lam-speed]
* Chamber consumables — ceramic dome, gas ring, ESC.
* SkyWater's filings name Air Products and Praxair (2021 S-1) and Linde and
  Airgas (fiscal 2023 10-K) as gas suppliers[^sec-01][^sec-02] without tying
  them to a step.

## Related steps and cross-references

* Previous: {ref}`LINOX <step-010>` (liner under the fill).
* Next: {ref}`CMPNIT <step-012>` (polish of this film, stopping on
  the nitride from {ref}`ISONIT <step-003>`).
* Trench geometry from {ref}`STIE <step-006>`; fill "waffles" from
  {ref}`FOM <step-004>`.
* The resulting field oxide appears as FOX in the PDK stack and is the
  surface under field poly at {ref}`P1M <step-061>` and under local
  interconnect at {ref}`LI1M <step-102>`.
* Other gap-fill oxides: {ref}`PSG <step-089>`,
  {ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — "Lam/Novellus High Density
  Plasma (HDP) doped and phos doped with sputter etch".[^skw-01]
* SkyWater, *A Day in the Life of a SkyWater Maintenance Technician* —
  "Novellus high density plasma tool".[^skw-07]
* SkyWater PDK, *Criteria & Assumptions* — field oxide 0.07 µm above
  silicon under poly.[^pdk-03]
* SkyWater PDK, process stack diagram — "FOX K=3.9";
  0.3262 µm.[^pdk-04]
* SkyWater PDK, *Layers Reference* — "fom_waffles".[^pdk-06]
* SkyWater, Form S-1 (2021) — gas suppliers.[^sec-01]
* SkyWater, Form 10-K for fiscal 2023 — updated gas
  suppliers.[^sec-02]
* Novellus / Lam Research, SPEED Max press release — HDP as the
  preferred STI gap-fill technology; S/D ratio; remote plasma
  clean.[^lam-speed]
* SKY130 raw-data repository, 1.8 V transistor files and test-tile pad
  documentation — drain current against source/drain diffusion extent
  (our extraction).[^raw-data-lv-mosfets][^raw-data-testtile-pads]

### High-level understanding

* Wikipedia, *Plasma-enhanced chemical vapor deposition* —
  high-density plasma, sputtering during deposition, SiH₄/O₂/Ar
  oxide.[^wiki-pecvd]
* Wikipedia, *Shallow trench isolation* — the fill step in
  context.[^wiki-sti]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — HDP-CVD and
  STI fill.[^txt-05]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 — CVD
  of SiO₂.[^txt-02]

### Deep dive

* Nishimura et al., *Jpn. J. Appl. Phys.* 2002 — HDP-CVD gap-fill
  modelling (sputter-yield angular dependence and ionic deposition)
  demonstrated on 0.13 µm STI.[^nishimura-2002]
* Thung et al., *JTEC* 2016 — HDP voids, poly stringers and the fill
  aspect ratio on a 0.18 µm-generation tool set.[^thung-2016]
* Nandakumar et al., IEDM 1998 — trench fill and planarisation in the
  STI review.[^rev-01]
* ITRS 2001, *Front End Processes* — thin films for trench fill: "high
  aspect ratio gaps, top and bottom corner profile control".[^itrs-01]
* Nguyen, *IBM J. Res. Dev.* 1999 — a review of HDP-CVD of
  silicon-based dielectrics: reactor design, film properties and
  gap-fill mechanisms.[^nguyen-1999]
* Lee et al., SSDM 1997 — STI characteristics with an HDP-CVD gap-fill
  oxide for deep-submicron CMOS, including device
  results.[^lee-1997]
* Vassiliev, *Electrochem. Solid-State Lett.* 1999 — properties and
  gap-fill capability of HDP-CVD phosphosilicate glass, the doped
  variant SkyWater also lists.[^vassiliev-1999]
* Bianchi, Bouche and Roux-dit-Buisson, IEDM 2002 — how the stress
  from the trench fill changes MOSFET performance.[^bianchi-2002]
* Lindemann, Radecker and Sperlich, ASMC 2007 — selective oxide
  deposition as an alternative STI gap-fill, showing where HDP's
  limits lie.[^lindemann-2007]
* Papasouliotis et al. (Novellus / IBM), US 6,030,881 — a high-throughput
  HDP-CVD process for filling high-aspect-ratio
  structures.[^pat-hdp-novellus]
* Tan, Li and Zygmunt (Applied Materials), US 6,914,016 — a multi-step
  HDP-CVD deposition/etch process for high-aspect-ratio gaps, the
  competing vendor's approach.[^pat-hdp-amat]
* Seshan (ed.), *Handbook of Thin Film Deposition* — the chapter-level
  reference on CVD and HDP-CVD dielectric equipment and
  films.[^seshan-2012]

## Open questions

* The SKY130 fill thickness, deposition temperature, D/S ratio and
  whether a densification anneal follows are not public.
* Whether the fill was HDP from the start of S8 (2003) or whether an
  earlier TEOS/ozone or PECVD fill was used and later replaced is
  unknown; SkyWater's capability page describes the fab
  today.[^skw-01]
* The HDP tool model (SPEED versus another Novellus/Lam HDP product) is
  inferred from the vendor name only.

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^skw-07]: SkyWater Technology, *A Day in the Life of a SkyWater
    Maintenance Technician*, 2023-12-14. <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository. <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^lam-speed]: Novellus Systems (Lam Research newsroom), *Novellus'
    SPEED Max HDP-CVD Dielectric Gapfill System Extends STI Application
    to 32nm*, press release, 2009-10-05.
    <https://newsroom.lamresearch.com/2009-10-05-NOVELLUS-SPEED-R-MAX-HDP-CVD-DIELECTRIC-GAPFILL-SYSTEM-EXTENDS-STI-APPLICATION-TO-32nm>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^wiki-sti]: Wikipedia, *Shallow trench isolation*.
    <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^nishimura-2002]: H. Nishimura, S. Takagi, M. Fujino and N. Nishi,
    "Gap-Fill Process of Shallow Trench Isolation for 0.13 µm
    Technologies", *Japanese Journal of Applied Physics* **41**, Part 1,
    No. 5A, 2886–2893 (2002). <https://doi.org/10.1143/JJAP.41.2886>
[^thung-2016]: B. J. Thung, K. Ibrahim, N. A. Manap and F. Salehuddin,
    "Challenges for 0.13µm Generation Shallow Trench Isolation on
    0.18µm Equipment Platform", *Journal of Telecommunication,
    Electronic and Computer Engineering* **8**(5), 15–21 (2016).
    <https://jtec.utem.edu.my/jtec/article/view/697>
[^rev-01]: M. Nandakumar, A. Chatterjee, S. Sridhar, K. Joyner,
    M. Rodder and I.-C. Chen, "Shallow trench isolation for advanced
    ULSI CMOS technologies", *IEDM 1998 Technical Digest*, pp. 133–136.
    <https://doi.org/10.1109/IEDM.1998.746297>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^nguyen-1999]: S. V. Nguyen, "High-density plasma chemical vapor
    deposition of silicon-based dielectric films for integrated
    circuits", *IBM Journal of Research and Development* **43**(1.2),
    109–126 (1999). <https://doi.org/10.1147/rd.431.0109>
[^lee-1997]: S. Lee, K. Jung, J. Son, S. Chung, M. Chae, J. Kim,
    W. Yang, Y. Lee and J. Hwang, "Shallow Trench Isolation
    Characteristics with High-Density-Plasma (HDP) CVD Gap-Fill Oxide
    for Deep-Submicron CMOS Technologies", *Extended Abstracts of the
    1997 International Conference on Solid State Devices and
    Materials*, C-13-4 (1997). <https://doi.org/10.7567/SSDM.1997.C-13-4>
[^vassiliev-1999]: V. Y. Vassiliev, "Properties and Gap-Fill Capability
    of HPD-CVD Phosphosilicate Glass Films for Subquarter-Micrometer
    ULSI Device Technology", *Electrochemical and Solid-State Letters*
    **3**(2), 80 (1999). <https://doi.org/10.1149/1.1390964>
[^bianchi-2002]: R. A. Bianchi, G. Bouche and O. Roux-dit-Buisson,
    "Accurate modeling of trench isolation induced mechanical stress
    effects on MOSFET electrical performance", *IEDM 2002 Technical
    Digest*, pp. 117–120. <https://doi.org/10.1109/IEDM.2002.1175792>
[^lindemann-2007]: H. M. Lindemann, J. Radecker and H.-P. Sperlich,
    "Selective Oxide (SelOx) Deposition as Unique Gap-Fill Solution for
    Shallow Trench Isolation", *2007 IEEE/SEMI Advanced Semiconductor
    Manufacturing Conference (ASMC)*, pp. 253–258.
    <https://doi.org/10.1109/ASMC.2007.375111>
[^pat-hdp-novellus]: G. D. Papasouliotis, A. B. Chakravarti, R. A. Conti,
    L. Economikos and P. A. Van Cleemput (Novellus Systems /
    International Business Machines), *High throughput chemical vapor
    deposition process capable of filling high aspect ratio
    structures*, US 6,030,881 A, granted 2000-02-29.
    <https://patents.google.com/patent/US6030881A/en>
[^pat-hdp-amat]: Z. Tan, D. Li and W. Zygmunt (Applied Materials),
    *HDP-CVD deposition process for filling high aspect ratio gaps*,
    US 6,914,016 B2, granted 2005-07-05.
    <https://patents.google.com/patent/US6914016B2/en>
[^seshan-2012]: K. Seshan (ed.), *Handbook of Thin Film Deposition*,
    3rd ed., William Andrew, 2012, ISBN 978-1-4377-7873-1.
    <https://openlibrary.org/isbn/9781437778731>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^raw-data-lv-mosfets]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the 1.8 V
    transistors, IC-CAP `.mdm` files in `sky130_fd_pr/cells/`
    (`nfet_01v8`, `nfet_01v8_lvt`, `pfet_01v8`, `pfet_01v8_hvt`,
    `pfet_01v8_lvt`), `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
