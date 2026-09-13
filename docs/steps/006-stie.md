(step-006)=
# Step 006 — STIE: Shallow trench etch

| | |
|---|---|
| **Step number** | 6 of 171[^steps-sheet] |
| **Step code** | `STIE` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | FEOL — isolation |
| **Previous step** | {ref}`STINITE <step-005>` |
| **Next step** | {ref}`DNM <step-007>` |

## What this step is

`STIE` (shallow-trench-isolation etch) is the plasma etch that cuts the
isolation trenches into the silicon. Using the patterned nitride/pad-
oxide {term}`hard mask` from {ref}`STINITE <step-005>` (with the
{ref}`FOM <step-004>` resist still on top, or already removed —
see below), a halogen plasma etches a few hundred nanometres into the
wafer wherever the field is open. The trench walls are made slightly
tapered and the corners are kept free of sharp features so that the
later liner oxidation ({ref}`LINOX <step-010>`) and HDP fill
({ref}`FILOX <step-011>`) can complete the isolation.

Wikipedia summarises {term}`STI` as "etching a pattern of trenches in the
silicon, depositing one or more dielectric materials (such as silicon
dioxide) to fill the trenches, and removing the excess
dielectric";[^wiki-sti] `STIE` is the first of those three operations.

**How deep?** No SkyWater document gives the SKY130 trench depth. Two
public numbers constrain it. The PDK process-stack drawing places the
top of the field oxide ("FOX K=3.9") at 0.3262 µm on its vertical
scale,[^pdk-04] and the assumptions page gives the field-oxide step
above the silicon surface under poly as 0.07 µm.[^pdk-03] If the
drawing's zero is the trench floor — which is our reading of the
diagram, not a documented fact — the trench would be about 0.26 µm
deep. That is in line with era practice: an AmberWave Systems STI
patent (now TSMC-owned) gives "a depth d1 within a range of, for
example, 3000-4000 Å",[^pat-sti-amberwave] and the 2001 ITRS notes that
STI {term}`aspect ratios <aspect ratio>` rise node on node as spacing shrinks.[^itrs-01] With
a minimum trench width of 0.27 µm (difftap.3)[^pdk-periph] and a
nitride of ~150 nm, the fill aspect ratio (depth + nitride) / width
would be about 1.5 : 1 (Thung et al. define the ratio that
way[^thung-2016]).

## Step category

`STIE` is an {ref}`Etch <category-etch>` step — a single-crystal
silicon etch in HBr/Cl₂/O₂ chemistry. It is the deepest silicon etch
in the baseline flow (the "deep-trench etching capability" that
SkyWater "added" in 2020[^sec-02] is a separate, later capability).
The poly etch at {ref}`P1ME <step-062>` uses the same family of
chemistry on a different film.

## Why this step exists

STI replaced {term}`LOCOS` at "CMOS process technology nodes of 250 nanometers
and smaller"[^wiki-sti] because a trench gives a planar surface, no
bird's-beak encroachment and a much smaller active-to-active pitch. The
trench profile is the single most important geometric input to the
isolation module:

* **Depth** sets the isolation between neighbouring N⁺ and P⁺
  diffusions and the P-well-to-N-well leakage path; too shallow and
  the wells short under the trench, too deep and the fill and the
  polish get harder.
* **Sidewall angle** (typically a few degrees off vertical) lets the
  HDP oxide fill without voids. The 0.13 µm STI paper cited below
  traces a yield loss to "HDP deposition void at the special Shallow
  Trench Isolation (STI) wall structure".[^thung-2016]
* **Top-corner shape** controls the parasitic edge transistor that
  produces the "double-hump" in the sub-threshold characteristic;
  the 2001 ITRS records that manufacturers were "beginning to use etch
  processes, rather than classic thermal processing, to round the top
  corner of the STI trench as a means for alleviating the classic
  transistor double-hump effect".[^itrs-01]
* **Bottom-corner shape** controls stress and dislocation generation
  during the liner oxidation.[^rev-01]

The published SKY130 {term}`test tile` shows structures with which the
result can be checked electrically: field-oxide FETs, mostly 1000 µm wide, whose poly-1 or metal-1
gates cross the isolation between two diffusions ("poly1 gate w/l =
1000/0.17, diff spacing = 0.27"; "(diff spacing =0.48)" for the
high-voltage version), 0.29 µm n⁺ and p⁺ diffusion lines at 0.3 µm
space for "line integrity", and gate-oxide capacitors that are "field-edge intensive"
at "FOM w/s = 0.14/0.27"[^raw-data-testtile-pads] — the minimum width
and space the PDK's CD table gives for the field-oxide mask
(`FOMCD` 0.14 µm, `FOMCDSP` 0.27 µm).[^pdk-03]

## How it is typically performed

An industry-generic recipe for a 200 mm, 130 nm-era fab:

1. **Chamber and mask.** High-density (inductively coupled or
   transformer-coupled) plasma etcher with independent bias power, so
   that ion energy and radical flux can be set separately (Wikipedia
   describes the hybrid in which "the ICP is employed as a high density
   source of ions … whereas a separate RF bias is applied to the
   substrate"[^wiki-rie]). The resist from {ref}`FOM <step-004>` is
   commonly left on during the silicon etch and stripped afterwards;
   some fabs strip it after the nitride open and etch the silicon with
   the nitride alone to get better corner control.[^txt-05]
2. **Breakthrough.** A few seconds of CF₄ or Cl₂ to clear native oxide
   and any pad-oxide residue.
3. **Main etch.** HBr with a smaller flow of Cl₂ and a few percent O₂,
   at a few to a few tens of mTorr. Bromine and chlorine etch silicon;
   the O₂ forms a thin SiOₓBrᵧ passivation on the sidewall that gives
   the controlled taper and protects the nitride mask. The
   HBr/Cl₂/O₂ ratio, pressure and bias set the taper angle and the
   bottom rounding.[^txt-05] The etch is *timed* rather than
   endpointed, because there is no interface to detect; depth is
   controlled by rate calibration on monitor wafers.
4. **Corner rounding (optional).** A short isotropic step, or a
   dedicated post-etch treatment, softens the top corner.[^itrs-01]
5. **Resist strip and clean.** O₂ plasma {term}`ash`, then a wet clean to
   remove the bromine-containing sidewall polymer — an STI paper
   notes that after the dry etch a "wet cleaning process is then
   applied to remove the polymer or residue on the side wall of shallow
   trench".[^thung-2016] This reference treats the strip as part of
   `STIE`; it could equally belong to the preparation for the
   following {ref}`DNM <step-007>` lithography (open question).
6. **Metrology.** Trench depth by cross-section SEM or by an optical
   scatterometry/profilometry monitor; {term}`CD` by {term}`CD-SEM`.

SkyWater's capability page lists the exact chemistry on its AMAT
etcher: "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2 – gate, trench,
W/WN".[^skw-01]

## Machines typically used

* **{ref}`High-density silicon etcher <machine-plasma-etcher-silicon>`**, 200 mm single wafer: Applied
  Materials Centura DPS / DPS II (decoupled plasma source), Lam {term}`TCP` 9400
  series (transformer-coupled plasma[^snf-9400]), TEL DRM/Unity,
  Hitachi M-series microwave ECR etchers.
* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`** (microwave or RF O₂ plasma).
* **{ref}`Wet bench <machine-wet-bench>`** for post-etch polymer removal.
* **{ref}`Cross-section SEM <machine-cross-section-sem-profilers>` / {ref}`CD-SEM <machine-cd-sem-overlay-metrology>`** for depth and CD.

## Machines likely used at SkyWater

* **AMAT DPS II.** SkyWater names the tool, the HBr/Cl₂/O₂ gases and
  the "trench" application.[^skw-01] Strength: strong for the tool and
  its stated application; the assignment to this specific step is our
  inference.
* **Lam 9400 TCP** ("poly/nitride, HBr, CF4, SF6, O2"[^skw-01]) and
  **Lam 4400** ("HBr, Cl2, C2F6, CF4, SF6, O2"[^skw-01]) are
  alternative silicon etchers on site. Strength: strong for existence,
  inference for use here.
* **Ash — GaSonics PEP, Mattson Aspen II.**[^skw-01] Strength: strong.
* **Post-etch clean — DNS / FSI Mercury (HF/SC1/SC2) or Akrion Gamma
  (sulphuric, SC1).**[^skw-01] Strength: strong for existence.

## Resources required

* **HBr, Cl₂, O₂** main-etch gases; **CF₄** for
  breakthrough.[^skw-01][^txt-05]
* **Helium** backside cooling; **N₂** purge.
* **NF₃ or SF₆/O₂** chamber clean (SkyWater lists NF₃ on the
  DPSII[^skw-01]).
* **O₂ / N₂ / {term}`forming gas`** for the ash.
* **{term}`SC-1`, H₂SO₄/H₂O₂ or dilute HF** ({ref}`wet chemicals <material-wet-chemicals>`) for the post-etch
  clean.[^wiki-rca]
* Chamber consumables (ceramic liners, focus rings); monitor wafers
  for depth calibration.

## Related steps and cross-references

* Previous: {ref}`STINITE <step-005>` (hard-mask open).
* Next: {ref}`DNM <step-007>` — unusually, a mask step follows before
  the trench is lined and filled; see the discussion on that page.
* The trench is lined at {ref}`LINOX <step-010>`, filled at
  {ref}`FILOX <step-011>`, planarised at {ref}`CMPNIT <step-012>`.
* Related silicon/poly etches: {ref}`P1ME <step-062>`,
  {ref}`BFR <step-060>`.
* Category page: {ref}`Etch <category-etch>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — DPSII "gate, trench"; Lam
  9400/4400; ashers; wet benches.[^skw-01]
* SkyWater, Form 10-K for fiscal 2023 — "In 2020, we added deep-trench
  etching capability".[^sec-02]
* SkyWater PDK, *Criteria & Assumptions* — field oxide 0.07 µm above
  the silicon surface under poly.[^pdk-03]
* SkyWater PDK, process stack diagram — "FOX K=3.9"; 0.3262 µm;
  "Diagram not to scale!".[^pdk-04]
* SkyWater PDK, *Periphery rules* — difftap.3 = 0.270 µm.[^pdk-periph]
* Currie and Lochtefeld (AmberWave), US 6,960,781 — trench depth
  3000–4000 Å.[^pat-sti-amberwave]
* Stanford Nanofabrication Facility, *Lam Research TCP 9400 Poly
  Etcher* page — the TCP etcher and its gas set.[^snf-9400]
* SKY130 raw-data repository, test-tile pad documentation — the
  field-oxide FET, diffusion-line and field-edge capacitor structures of
  the published test tile.[^raw-data-testtile-pads]

### High-level understanding

* Wikipedia, *Shallow trench isolation* — the three STI operations and
  the LOCOS cross-over node.[^wiki-sti]
* Wikipedia, *Reactive-ion etching* — {term}`ICP` with separate
  bias.[^wiki-rie]
* Wikipedia, *RCA clean* — the post-etch clean chemistry.[^wiki-rca]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — STI trench
  etch, HBr/Cl₂/O₂ chemistry, profile control.[^txt-05]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  plasma etching of silicon.[^txt-02]

### Deep dive

* Nandakumar et al., IEDM 1998 — the STI review: trench profile,
  corner rounding, stress and defects.[^rev-01]
* ITRS 2001, *Front End Processes* — the etch section on STI corner
  rounding and the thin-film section on trench fill.[^itrs-01]
* Thung et al., *JTEC* 2016 — the HDP void at the trench wall, the
  post-etch wet clean and the fill-aspect-ratio
  definition.[^thung-2016]
* Kim et al. (Spansion), US 7,439,141 — a corner-rounding scheme from
  a company later merged into Cypress; not evidence for the S8 flow
  itself.[^pat-sti-cr]
* Bryant, Hänsch and Mii, IEDM 1994 — the device-level case for STI
  over LOCOS and what trench isolation must deliver.[^bryant-1994]
* Chatterjee et al., VLSI 1996 — an STI study for 0.25/0.18 µm CMOS:
  trench depth, corner and stress trade-offs.[^chatterjee-1996]
* Nandakumar et al., IEDM 1997 — STI for sub-0.13 µm CMOS, the node
  this flow belongs to.[^nandakumar-1997]
* Fazan and Mathews (Micron), IEDM 1993 — an early manufacturable
  trench isolation process, showing the etch, fill and polish
  sequence.[^fazan-1993]
* Bestwick and Oehrlein, *J. Vac. Sci. Technol. A* 1990 — reactive-ion
  etching of silicon in bromine-containing plasmas, the chemistry of
  the main etch.[^bestwick-1990]
* Matsuda et al. (Toshiba), IEDM 1998 — a corner-rounding process
  based on silicon micro-structure transformation after the trench
  etch.[^matsuda-1998]
* Watanabe et al., IEDM 1996 — corner-rounded STI to cut stress-induced
  tunnel-oxide leakage in flash memory.[^watanabe-1996]
* Lin et al., *Solid-State Electronics* 1998 — an analytical model of
  the sub-threshold current hump caused by the STI top
  corner.[^lin-1998]
* Bianchi, Bouche and Roux-dit-Buisson, IEDM 2002 — modelling of
  trench-isolation-induced mechanical stress on MOSFET
  performance.[^bianchi-2002]
* Horioka et al. (Toshiba), US 5,258,332 — rounding of trench corner
  portions by fluorine/oxygen chemical dry etching (framed around
  trench capacitors rather than STI), the same technique as step 4
  above.[^pat-corner-toshiba]
* Hon, SJSU master's thesis 2003 — {term}`line-edge roughness <LER>` measurement on
  an STI etch.[^hon-2003]

## Open questions

* **Trench depth.** The ~0.26 µm figure is an inference from the PDK
  stack drawing and assumptions page[^pdk-04][^pdk-03] whose datum is
  not documented; the drawing says "not to scale". No measured
  cross-section of SKY130 STI is public.
* **Where the FOM resist is stripped** — inside `STIE`, or before the
  silicon etch — is not stated publicly.
* Whether SkyWater's DPSII or a Lam tool carries this etch is not
  public.

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository. <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pat-sti-amberwave]: M. T. Currie and A. J. Lochtefeld (AmberWave
    Systems Corporation; assigned to Taiwan Semiconductor Manufacturing
    Co. on 2010-01-26), *Shallow trench isolation process*,
    US 6,960,781 B2, granted 2005-11-01.
    <https://patents.google.com/patent/US6960781B2/en>
[^snf-9400]: Stanford Nanofabrication Facility, *Lam Research TCP 9400
    Poly Etcher (lampoly)*, equipment page.
    <https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>
[^wiki-sti]: Wikipedia, *Shallow trench isolation*.
    <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^wiki-rca]: Wikipedia, *RCA clean*. <https://en.wikipedia.org/wiki/RCA_clean>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^rev-01]: M. Nandakumar, A. Chatterjee, S. Sridhar, K. Joyner,
    M. Rodder and I.-C. Chen, "Shallow trench isolation for advanced
    ULSI CMOS technologies", *IEDM 1998 Technical Digest*, pp. 133–136.
    <https://doi.org/10.1109/IEDM.1998.746297>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^thung-2016]: B. J. Thung, K. Ibrahim, N. A. Manap and F. Salehuddin,
    "Challenges for 0.13µm Generation Shallow Trench Isolation on
    0.18µm Equipment Platform", *Journal of Telecommunication,
    Electronic and Computer Engineering* **8**(5), 15–21 (2016).
    <https://jtec.utem.edu.my/jtec/article/view/697>
[^pat-sti-cr]: U. Kim, Y. Sun, M. S. Chang et al. (Spansion LLC; later
    Cypress Semiconductor / Infineon), *Shallow trench isolation
    approach for improved STI corner rounding*, US 7,439,141 B2,
    priority 2001-12-27, granted 2008-10-21.
    <https://patents.google.com/patent/US7439141B2/en>
[^bryant-1994]: A. Bryant, W. Hänsch and T. Mii, "Characteristics of
    CMOS device isolation for the ULSI age", *Proc. 1994 IEEE
    International Electron Devices Meeting*, pp. 671–674.
    <https://doi.org/10.1109/IEDM.1994.383292>
[^chatterjee-1996]: A. Chatterjee, J. Esquivel, S. Nag, I. Ali,
    D. Rogers, K. Taylor, K. Joyner, M. Mason, D. Mercer,
    A. Amerasekera, T. Houston and I.-C. Chen, "A shallow trench
    isolation study for 0.25/0.18 µm CMOS technologies and beyond",
    *1996 Symposium on VLSI Technology, Digest of Technical Papers*,
    pp. 156–157. <https://doi.org/10.1109/VLSIT.1996.507831>
[^nandakumar-1997]: M. Nandakumar, S. Sridhar, S. Nag, P. Mei,
    D. Rogers, M. Hanratty, A. Amerasekera and I.-C. Chen, "A shallow
    trench isolation for sub-0.13 µm CMOS technologies", *IEDM 1997
    Technical Digest*, pp. 657–660.
    <https://doi.org/10.1109/IEDM.1997.650469>
[^fazan-1993]: P. C. Fazan and V. K. Mathews, "A highly manufacturable
    trench isolation process for deep submicron DRAMs", *Proc. IEEE
    International Electron Devices Meeting 1993*, pp. 57–60.
    <https://doi.org/10.1109/IEDM.1993.347399>
[^bestwick-1990]: T. D. Bestwick and G. S. Oehrlein, "Reactive ion
    etching of silicon using bromine containing plasmas", *Journal of
    Vacuum Science & Technology A* **8**(3), 1696–1701 (1990).
    <https://doi.org/10.1116/1.576832>
[^matsuda-1998]: S. Matsuda, T. Sato, H. Yoshimura, Y. Takegawa,
    A. Sudo, I. Mizushima, Y. Tsunashima and Y. Toyoshima, "Novel
    corner rounding process for shallow trench isolation utilizing MSTS
    (Micro-Structure Transformation of Silicon)", *IEDM 1998 Technical
    Digest*, pp. 137–140. <https://doi.org/10.1109/IEDM.1998.746298>
[^watanabe-1996]: H. Watanabe, K. Shimizu, Y. Takeuchi and S. Aritome,
    "Corner-rounded shallow trench isolation technology to reduce the
    stress-induced tunnel oxide leakage current for highly reliable
    flash memories", *IEDM 1996 Technical Digest*, pp. 833–836.
    <https://doi.org/10.1109/IEDM.1996.554109>
[^lin-1998]: S. C. Lin, J. B. Kuo, K. T. Huang and S. W. Sun,
    "Analytical subthreshold current hump model for deep-submicron
    shallow-trench-isolated CMOS devices", *Solid-State Electronics*
    **42**(10), 1871–1879 (1998).
    <https://doi.org/10.1016/S0038-1101(98)00161-0>
[^bianchi-2002]: R. A. Bianchi, G. Bouche and O. Roux-dit-Buisson,
    "Accurate modeling of trench isolation induced mechanical stress
    effects on MOSFET electrical performance", *IEDM 2002 Technical
    Digest*, pp. 117–120. <https://doi.org/10.1109/IEDM.2002.1175792>
[^pat-corner-toshiba]: K. Horioka, H. Okano and H. Nishino (Toshiba
    Corporation), *Method of manufacturing semiconductor devices
    including rounding of corner portions by etching*, US 5,258,332 A,
    granted 1993-11-02. <https://patents.google.com/patent/US5258332A/en>
[^hon-2003]: B. M. Hon, *Characterization of shallow trench isolation
    etch line edge roughness*, master's thesis, San José State
    University, 2003. <https://doi.org/10.31979/etd.53yx-bwm5>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
