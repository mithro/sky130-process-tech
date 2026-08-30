(step-006)=
# Step 006 — STIE: Shallow trench etch

| | |
|---|---|
| **Step number** | 6 of 171 |
| **Step code** | `STIE` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | FEOL — isolation |
| **Previous step** | {ref}`STINITE <step-005>` |
| **Next step** | {ref}`DNM <step-007>` |

## What this step is

`STIE` (shallow-trench-isolation etch) is the plasma etch that cuts the
isolation trenches into the silicon. Using the patterned nitride/pad-
oxide hard mask from {ref}`STINITE <step-005>` (with the
{ref}`FOM <step-004>` resist still on top, or already removed —
see below), a halogen plasma etches a few hundred nanometres into the
wafer wherever the field is open. The trench walls are made slightly
tapered and the corners are kept free of sharp features so that the
later liner oxidation ({ref}`LINOX <step-010>`) and HDP fill
({ref}`FILOX <step-011>`) can complete the isolation.

Wikipedia summarises STI as "etching a pattern of trenches in the
silicon, depositing one or more dielectric materials (such as silicon
dioxide) to fill the trenches, and removing the excess dielectric"
(WIKI-STI); `STIE` is the first of those three operations.

**How deep?** No SkyWater document gives the SKY130 trench depth. Two
public numbers constrain it. The PDK process-stack drawing places the
top of the field oxide ("FOX K=3.9") at 0.3262 µm on its vertical
scale (PDK-04), and the assumptions page gives the field-oxide step
above the silicon surface under poly as 0.07 µm (PDK-03). If the
drawing's zero is the trench floor — which is our reading of the
diagram, not a documented fact — the trench would be about 0.26 µm
deep. That is in line with era practice: an AmberWave Systems STI
patent (now TSMC-owned) gives "a depth d1 within a range of, for
example, 3000-4000 Å" (PAT-STI-AMBERWAVE),
and the 2001 ITRS notes that STI aspect ratios rise node on node as
spacing shrinks (ITRS-01). With a minimum trench width of 0.27 µm
(PDK-PERIPH, difftap.3) and a nitride of ~150 nm, the fill aspect ratio
(depth + nitride) / width would be about 1.5 : 1 (THUNG-2016 defines
the ratio that way).

## Step category

`STIE` is an {ref}`Etch <category-etch>` step — a single-crystal
silicon etch in HBr/Cl₂/O₂ chemistry. It is the deepest silicon etch
in the baseline flow (the "deep-trench etching capability" that
SkyWater "added" in 2020, SEC-02, is a separate, later capability).
The poly etch at {ref}`P1ME <step-062>` uses the same family of
chemistry on a different film.

## Why this step exists

STI replaced LOCOS at "CMOS process technology nodes of 250 nanometers
and smaller" (WIKI-STI) because a trench gives a planar surface, no
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
  Trench Isolation (STI) wall structure" (THUNG-2016).
* **Top-corner shape** controls the parasitic edge transistor that
  produces the "double-hump" in the sub-threshold characteristic;
  the 2001 ITRS records that manufacturers were "beginning to use etch
  processes, rather than classic thermal processing, to round the top
  corner of the STI trench as a means for alleviating the classic
  transistor double-hump effect" (ITRS-01).
* **Bottom-corner shape** controls stress and dislocation generation
  during the liner oxidation (REV-01).

## How it is typically performed

An industry-generic recipe for a 200 mm, 130 nm-era fab:

1. **Chamber and mask.** High-density (inductively coupled or
   transformer-coupled) plasma etcher with independent bias power, so
   that ion energy and radical flux can be set separately (WIKI-RIE
   describes the hybrid in which "the ICP is employed as a high density
   source of ions … whereas a separate RF bias is applied to the
   substrate"). The resist from {ref}`FOM <step-004>` is commonly left
   on during the silicon etch and stripped afterwards; some fabs strip
   it after the nitride open and etch the silicon with the nitride
   alone to get better corner control (TXT-05).
2. **Breakthrough.** A few seconds of CF₄ or Cl₂ to clear native oxide
   and any pad-oxide residue.
3. **Main etch.** HBr with a smaller flow of Cl₂ and a few percent O₂,
   at a few to a few tens of mTorr. Bromine and chlorine etch silicon;
   the O₂ forms a thin SiOₓBrᵧ passivation on the sidewall that gives
   the controlled taper and protects the nitride mask. The
   HBr/Cl₂/O₂ ratio, pressure and bias set the taper angle and the
   bottom rounding (TXT-05). The etch is *timed* rather than
   endpointed, because there is no interface to detect; depth is
   controlled by rate calibration on monitor wafers.
4. **Corner rounding (optional).** A short isotropic step, or a
   dedicated post-etch treatment, softens the top corner (ITRS-01).
5. **Resist strip and clean.** O₂ plasma ash, then a wet clean to
   remove the bromine-containing sidewall polymer — an STI paper
   notes that after the dry etch a "wet cleaning process is then
   applied to remove the polymer or residue on the side wall of shallow
   trench" (THUNG-2016). In SKY130 the strip is not a listed step;
   it is presumably part of `STIE` or of the following
   {ref}`DNM <step-007>` litho preparation (open question).
6. **Metrology.** Trench depth by cross-section SEM or by an optical
   scatterometry/profilometry monitor; CD by CD-SEM.

SkyWater's capability page lists the exact chemistry on its AMAT
etcher: "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2 – gate, trench, W/WN"
(SKW-01). Applied Materials sold a dedicated "DPS STI Centura"
configuration of this decoupled-plasma-source platform from late
1998 (see open questions).

## Machines typically used

* **High-density silicon etcher**, 200 mm single wafer: Applied
  Materials Centura DPS / DPS II (decoupled plasma source), Lam TCP 9400
  series (transformer-coupled plasma; SNF-9400), TEL DRM/Unity, Hitachi
  M-series microwave ECR etchers.
* **Resist asher** (downstream microwave or RF O₂ plasma).
* **Wet bench** for post-etch polymer removal.
* **Cross-section SEM / CD-SEM** for depth and CD.

## Machines likely used at SkyWater

* **AMAT DPS II.** SKW-01 names the tool, the HBr/Cl₂/O₂ gases and the
  "trench" application. Strength: strong for the tool and its stated
  application; the assignment to this specific step is our inference.
* **Lam 9400 TCP** (SKW-01: "poly/nitride, HBr, CF4, SF6, O2") and
  **Lam 4400** (SKW-01: "HBr, Cl2, C2F6, CF4, SF6, O2") are alternative
  silicon etchers on site. Strength: strong for existence, inference
  for use here.
* **Ash — Gasonics PEP, Mattson Aspen 2** (SKW-01). Strength: strong.
* **Post-etch clean — DNS / FSI Mercury (HF/SC1/SC2) or Akrion Gamma
  (sulphuric, SC1)** (SKW-01). Strength: strong for existence.

## Resources required

* **HBr, Cl₂, O₂** main-etch gases; **CF₄** for breakthrough (SKW-01,
  TXT-05).
* **Helium** backside cooling; **N₂** purge.
* **NF₃ or SF₆/O₂** chamber clean (SKW-01 lists NF₃ on the DPSII).
* **O₂ / N₂ / forming gas** for the ash.
* **SC-1, H₂SO₄/H₂O₂ or dilute HF** for the post-etch clean
  (WIKI-RCA).
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

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 (DPSII "gate, trench"; Lam 9400/4400; ashers;
  wet benches).
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **SEC-02** — SkyWater Technology, Inc., Form 10-K for fiscal 2023
  ("In 2020, we added deep-trench etching capability").
  <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
* **PDK-03** — SkyWater PDK Authors, *Criteria & Assumptions* (field
  oxide 0.07 µm above the silicon surface under poly).
  <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
* **PDK-04** — SkyWater PDK Authors, *Process stack diagram*
  (`metal_stack.svg`; "FOX K=3.9"; 0.3262 µm; "Diagram not to scale!").
  <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
* **PDK-PERIPH** — SkyWater PDK Authors, *Periphery rules* (difftap.3
  = 0.270 µm).
  <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
* **PAT-STI-AMBERWAVE** — M. T. Currie and A. J. Lochtefeld (AmberWave
  Systems Corporation; assigned to Taiwan Semiconductor Manufacturing
  Co. on 2010-01-26), US 6,960,781 B2, *Shallow trench isolation
  process*, granted 2005-11-01 (trench depth 3000–4000 Å).
  <https://patents.google.com/patent/US6960781B2/en>
* **SNF-9400** — Stanford Nanofabrication Facility, *Lam Research TCP
  9400 Poly Etcher* page.
  <https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>

### High-level understanding

* **WIKI-STI** — Wikipedia, *Shallow trench isolation*.
  <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
* **WIKI-RIE** — Wikipedia, *Reactive-ion etching*.
  <https://en.wikipedia.org/wiki/Reactive-ion_etching>
* **WIKI-RCA** — Wikipedia, *RCA clean*.
  <https://en.wikipedia.org/wiki/RCA_clean>
* **TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4*,
  Lattice Press, 2002, ISBN 978-0-9616721-7-1 (STI trench etch,
  HBr/Cl₂/O₂ chemistry, profile control).
  <https://openlibrary.org/isbn/9780961672171>
* **TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the
  VLSI Era, Vol. 1*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4 (plasma etching of silicon).
  <https://openlibrary.org/isbn/9780961672164>

### Deep dive

* **REV-01** — M. Nandakumar et al., "Shallow trench isolation for
  advanced ULSI CMOS technologies", *IEDM 1998*, pp. 133–136,
  DOI 10.1109/IEDM.1998.746297.
* **ITRS-01** — ITRS 2001, *Front End Processes* (etch section on STI
  corner rounding; thermal/thin-film section on trench fill).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
* **THUNG-2016** — B. J. Thung et al., "Challenges for 0.13µm Generation
  Shallow Trench Isolation on 0.18µm Equipment Platform", *JTEC* 8(5),
  2016, pp. 15–21.
  <https://jtec.utem.edu.my/jtec/article/download/697/707/3255>
* **PAT-STI-CR** — U. Kim et al. (Spansion LLC), US 7,439,141 B2,
  *Shallow trench isolation approach for improved STI corner rounding*,
  granted 2008-10-21 — a corner-rounding scheme from a company later
  merged into Cypress; not evidence for the S8 flow itself.
  <https://patents.google.com/patent/US7439141B2/en>

## Open questions

* **Trench depth.** The ~0.26 µm figure is an inference from PDK-04
  and PDK-03 whose datum is not documented; the drawing says
  "not to scale". No measured cross-section of SKY130 STI is public.
* **Where the FOM resist is stripped** — inside `STIE`, or before the
  silicon etch — is not listed as a step and is unknown.
* **Applied Materials' "DPS STI Centura" press release** (dated
  1998-12-14 according to search-engine snippets) could not be fetched
  during writing and is therefore not cited as a verified source.
* Whether SkyWater's DPSII or a Lam tool carries this etch is not
  public.
