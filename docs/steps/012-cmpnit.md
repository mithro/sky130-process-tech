(step-012)=
# Step 012 — CMPNIT: CMP over nitride

| | |
|---|---|
| **Step number** | 12 of 171[^steps-sheet] |
| **Step code** | `CMPNIT` |
| **Category** | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| **Phase** | FEOL — isolation |
| **Previous step** | {ref}`FILOX <step-011>` |
| **Next step** | {ref}`NS19 <step-013>` |

## What this step is

`CMPNIT` (chemical-mechanical polish, stopping on nitride) removes the
fill oxide from {ref}`FILOX <step-011>` everywhere *except* inside the
trenches. The wafer is pressed face-down against a rotating polishing
pad flooded with abrasive slurry until the oxide over the active
areas is gone and the polish lands on the nitride from
{ref}`ISONIT <step-003>`, which polishes far more slowly. What is left
is a planar surface of nitride islands (future active areas) and
oxide-filled trenches (future field oxide), level with one another.

This is the step that gives {term}`STI` its defining advantage over {term}`LOCOS` —
a flat surface — and Wikipedia's STI outline lists it as "Chemical-
mechanical polishing of the oxide" followed by "Removal of the
protective nitride".[^wiki-sti] Because the oxide is later recessed
slightly during the nitride/pad-oxide removal and subsequent cleans,
the final field-oxide step above the active silicon is small — 0.07 µm
under poly in the PDK's assumptions.[^pdk-03]

## Step category

`CMPNIT` is a {ref}`Chemical-mechanical planarisation <category-cmp>`
step — an oxide polish with a nitride stop. The later polishes in the
flow ({ref}`CMPP <step-090>` over poly, {ref}`CMPL <step-106>`,
{ref}`CMPM <step-116>` over metal levels, and the tungsten polishes
{ref}`WCMPLI <step-100>`, {ref}`WCMP2 <step-111>`) planarise
interlevel dielectrics or clear metal; only this one uses a nitride
stop and only this one determines the height of the silicon islands.

## Why this step exists

Without planarisation the STI module would leave the whole fill
thickness ({ref}`FILOX <step-011>`) of oxide topography over every
active area, which no lithography or gate etch could handle. Beyond
simply flattening, the polish controls:

* **Active-area nitride thickness after polish**, which sets how much
  oxide is left standing above the silicon once the nitride is
  stripped at {ref}`NS19 <step-013>`.
* **{term}`Dishing <dishing>`** of the oxide in wide trenches and **{term}`erosion`** of the
  nitride in dense active regions. Dishing lowers the field oxide
  below the active surface locally and produces divots at active edges;
  erosion thins the nitride and the silicon beneath it. Both are
  pattern-density effects, and they are the reason wide field regions
  are filled with dummy active "waffles" (the PDK's "fom_waffles" of
  0.5–4.08 µm[^pdk-06]) and the reason some flows once used a
  reverse-mask etch-back before the polish.[^rev-01][^txt-05]
* **Defectivity** — scratches and residual slurry particles at this
  step become gate-oxide and poly defects.

## How it is typically performed

An industry-generic STI polish for a 200 mm, 130 nm-era fab:

1. **Tool.** Rotary multi-platen polisher with polyurethane pads; the
   pads "should be rigid in order to uniformly polish the wafer
   surface" and, being consumed, "must be regularly reconditioned"
   with a diamond conditioner.[^wiki-cmp] Wafers are held in a carrier
   head with a retaining ring and, on 200 mm-era tools, a multi-zone
   pressure membrane.
2. **Slurry.** Two options, both in production use at the 130 nm
   node:[^rev-02]
   * *Fumed or colloidal silica* in an alkaline (KOH or NH₄OH)
     solution — the classic oxide slurry, with oxide : nitride
     {term}`selectivity` of only about 3–4 : 1 (from the review's body,
     which is paywalled), which needs {term}`endpoint` control or
     a reverse-mask scheme to avoid over-polishing the nitride.
   * *Ceria (CeO₂)* with surfactant additives — Wikipedia's general
     description of {term}`CMP` names cerium dioxide as a typical
     abrasive[^wiki-cmp] —
     giving oxide : nitride selectivity of tens to one (from the
     review's body, which is paywalled) and a self-stopping polish, the
     "direct STI" approach that removed the reverse mask.
3. **Recipe.** A first platen removes the bulk oxide at high rate; a
   second platen with the selective slurry clears the oxide over the
   active areas and stops on nitride; a final platen buffs with
   DI water or a dilute slurry to remove particles. Down-force of a few
   psi and platen speeds of tens of rpm are typical.[^txt-05]
4. **Endpoint.** Motor-current or optical (in-situ reflectometry)
   endpoint detects the transition from oxide to nitride; Wikipedia
   remarks that without endpoint "a lack of end points requires blind
   polishing".[^wiki-cmp] The remaining nitride thickness is checked
   post-polish by optical metrology.
5. **Post-CMP clean.** Double-sided brush scrub with dilute NH₄OH or
   surfactant, sometimes with a dilute HF step, then spin-rinse-dry —
   slurry residue must be removed before the wafer dries.
6. **Metrology.** Nitride and trench-oxide thickness maps; dishing and
   erosion by profilometry or AFM on test structures; defect scan.

SkyWater's capability page lists "AMAT Mirra CMP – oxide – nitride –
niobium – aluminum – tungsten …"[^skw-01] — an oxide/nitride-capable
polisher, which is what this step needs.

## Machines typically used

* **{ref}`Rotary multi-platen CMP polisher <machine-cmp-polisher>`**, 200 mm: Applied Materials Mirra (the
  200 mm-era multi-platen standard; SkyWater lists it for oxide and
  nitride[^skw-01]), Ebara EPO-222/EPO-300, Strasbaugh 6DS-SP,
  SpeedFam-IPEC Avanti 472, Lam Teres.
* **{ref}`Post-CMP brush scrubber <machine-post-cmp-cleaner>`** (OnTrak/Lam Synergy, SEZ/Lam Da Vinci).
* **{ref}`Film-thickness metrology <machine-film-thickness-metrology>`** (Nanometrics, KLA-Tencor, Rudolph)
  and **{ref}`profilometer/AFM <machine-cross-section-sem-profilers>`**.

## Machines likely used at SkyWater

* **Applied Materials Mirra CMP.** SkyWater names it and lists oxide
  and nitride among its applications.[^skw-01] Strength: **strong**
  for the tool and its oxide and nitride polishes (SkyWater statement);
  assignment to this step is an **inference** from the film, since the
  list names no steps.
* **Post-CMP clean** — SkyWater lists the "SEZ223, Davinci"
  single-wafer tools (HF, DSP+HF), and the Mirra entry also lists
  "Track ammonia clean" and "IPA clean";[^skw-01] the technician profile
  mentions "a SEZ etcher tool".[^skw-07] Strength: strong for
  existence; a brush scrubber is not named on any public page (open
  question).
* **Defect inspection — KLA AIT / SP1**, our reading of "AIT" and "SP1"
  in a SkyWater job posting's "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
  Strength: medium.

## Resources required

* **{ref}`Slurry <material-cmp-consumables>`** — silica-based or ceria-based STI
  slurry.[^rev-02][^wiki-cmp]
* **Polishing pads** (stacked polyurethane, IC1000/Suba IV class;
  category page) and **pad conditioners** (diamond discs).[^wiki-cmp]
* **{ref}`DI water <material-ultrapure-water>`** in large volumes; **dilute NH₄OH** (category page) or a
  **surfactant**, as the recipe outline above gives for this
  ceria-capable polish, possibly **dilute HF**, for the post-CMP clean;
  **PVA brushes**.
* **Carrier-head consumables** — membranes, retaining rings.
* **Slurry supply and {ref}`waste treatment <material-hardware-consumables>`** — CMP is one of the largest
  water and waste-water consumers in the fab.[^txt-07]

## Related steps and cross-references

* Previous: {ref}`FILOX <step-011>` (film being polished).
* Next: {ref}`NS19 <step-013>` (nitride strip that exposes the active
  silicon and leaves the oxide standing).
* Nitride stop from {ref}`ISONIT <step-003>`; pattern-density
  "waffles" from {ref}`FOM <step-004>`.
* Other CMP steps: {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`,
  {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`,
  {ref}`CMPM <step-116>`.
* Category page: {ref}`Chemical-mechanical planarisation <category-cmp>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,893,796 A <patent-gp24770421>` — Forming a transparent window in a polishing pad for a chemical mechanical polishing apparatus (1995)
* {ref}`US 5,738,574 A <patent-gp24192580>` — Continuous processing system for chemical mechanical polishing (1995)
* {ref}`US 6,593,208 B1 <patent-gp25130177>` — Method of uniform polish in shallow trench isolation process (2001)
* {ref}`US 7,439,141 B2 <patent-gp26708682>` — Shallow trench isolation approach for improved STI corner rounding (2001)
* {ref}`US 6,960,781 B2 <patent-gp32990685>` — Shallow trench isolation process (2003)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — "AMAT Mirra CMP – oxide –
  nitride – niobium – aluminum – tungsten …"; SEZ 223 /
  Da Vinci.[^skw-01]
* SkyWater, *A Day in the Life of a SkyWater Maintenance Technician* —
  "a SEZ etcher tool".[^skw-07]
* SkyWater PDK, *Criteria & Assumptions* — field oxide 0.07 µm above
  silicon under poly.[^pdk-03]
* SkyWater PDK, *Layers Reference* — "fom_waffles".[^pdk-06]
* Currie and Lochtefeld (AmberWave), US 6,960,781 —
  "chemical-mechanical polishing (CMP), using the silicon nitride layer
  over the active area as a stop layer".[^pat-sti-amberwave]
* Kim et al. (Spansion), US 7,439,141 — isolation oxide "polished back
  … approximately level with the nitride mask".[^pat-sti-cr]
* LinkedIn, SkyWater *Defect Technician 2* posting — inspection
  tools.[^job-06]

### High-level understanding

* Wikipedia, *Chemical-mechanical polishing* — pads, conditioners,
  abrasives and endpoint.[^wiki-cmp]
* Wikipedia, *Shallow trench isolation* — the polish and nitride
  removal steps.[^wiki-sti]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — the CMP
  chapter; STI CMP.[^txt-05]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — CMP
  tools and consumables.[^txt-07]

### Deep dive

* Krishnan, Nalaskowski and Cook, *Chem. Rev.* 2010 — slurry chemistry,
  materials and mechanisms, including silica and ceria slurries for
  oxide/STI.[^rev-02]
* Nandakumar et al., IEDM 1998 — STI planarisation in the STI
  review.[^rev-01]
* Thung et al., *JTEC* 2016 — CMP in a 0.13 µm STI module on
  0.18 µm-generation tools.[^thung-2016]
* Cook, *J. Non-Cryst. Solids* 1990 — the chemical mechanism of glass
  (oxide) polishing that oxide CMP inherits.[^cook-1990]
* Hoshino et al., *J. Non-Cryst. Solids* 2001 — the mechanism by which
  ceria particles polish SiO₂.[^hoshino-2001]
* Manivannan, Victoria and Ramanathan, *Thin Solid Films* 2010 — the
  mechanism of high oxide-to-nitride selectivity in ceria STI
  slurries.[^manivannan-2010]
* America and Babu, *Electrochem. Solid-State Lett.* 2004 — slurry
  additives that suppress silicon nitride removal, i.e. how a
  self-stopping STI slurry is made.[^america-2004]
* Bu and Moudgil, MRS 2005 — a colloidal-silica route to a
  high-selectivity STI slurry, the alternative to ceria.[^bu-2005]
* Yu, Fazan, Mathews and Doan (Micron), *Appl. Phys. Lett.* 1992 —
  dishing effects in CMP planarisation for trench isolation, measured
  early.[^yu-1992]
* Stine et al., *IEEE Trans. Semicond. Manuf.* 1998 — rapid
  characterisation and modelling of pattern-dependent CMP variation,
  the basis of density-based fill rules.[^stine-1998]
* Chang, *Microelectron. Eng.* 2005 — a dishing model specific to the
  STI CMP process.[^chang-2005]
* Steigerwald, Murarka and Gutmann, *Chemical Mechanical Planarization
  of Microelectronic Materials* — the standard CMP textbook: {term}`Preston <Preston equation>`'s
  law, pads, slurries and process control.[^steigerwald-1997]
* Oliver (ed.), *Chemical-Mechanical Planarization of Semiconductor
  Materials* — chapter-level treatments of dielectric CMP, endpoint and
  post-CMP cleaning.[^oliver-2004]
* Tolles et al. (Applied Materials), US 5,738,574 — the multi-platen
  "continuous processing" CMP architecture of the Mirra
  family.[^pat-cmp-mirra]
* Birang, Gleason and Guthrie (Applied Materials), US 5,893,796 — a
  transparent window in the pad for in-situ optical endpoint
  detection.[^pat-cmp-window]
* Sun, Han and Keswani, *Developments in Surface Contamination and
  Cleaning* 2017 — brush scrubbing for post-CMP cleaning.[^sun-2017]

## Open questions

* Whether SKY130 uses a silica or a ceria (high-selectivity) slurry,
  and whether a reverse-mask etch-back was ever part of the S8 flow,
  is not public.
* The target post-polish nitride thickness and the allowed dishing /
  erosion are not public.
* The post-CMP cleaning tool is not identified on any public SkyWater
  page.
* Applied Materials' own Mirra product pages could not be retrieved
  during writing (HTTP 403), so no vendor description of the tool is
  cited; SkyWater's capability page is the only source used for
  it.[^skw-01]

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^job-06]: LinkedIn, *SkyWater Technology hiring Defect Technician 2 in
    Bloomington, MN* (job posting), retrieved 2026-09-19.
    <https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>
[^skw-07]: SkyWater Technology, *A Day in the Life of a SkyWater
    Maintenance Technician*, 2023-12-14. <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pat-sti-amberwave]: M. T. Currie and A. J. Lochtefeld (AmberWave
    Systems Corporation; assigned to Taiwan Semiconductor Manufacturing
    Co. on 2010-01-26), *Shallow trench isolation process*,
    US 6,960,781 B2, granted 2005-11-01.
    <https://patents.google.com/patent/US6960781B2/en>
[^pat-sti-cr]: U. Kim, Y. Sun, M. S. Chang et al. (Spansion LLC; later
    Cypress Semiconductor / Infineon), *Shallow trench isolation
    approach for improved STI corner rounding*, US 7,439,141 B2,
    priority 2001-12-27, granted 2008-10-21.
    <https://patents.google.com/patent/US7439141B2/en>
[^wiki-cmp]: Wikipedia, *Chemical-mechanical polishing*.
    <https://en.wikipedia.org/wiki/Chemical-mechanical_polishing>
[^wiki-sti]: Wikipedia, *Shallow trench isolation*.
    <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^rev-02]: M. Krishnan, J. W. Nalaskowski and L. M. Cook, "Chemical
    Mechanical Planarization: Slurry Chemistry, Materials, and
    Mechanisms", *Chemical Reviews* **110**(1), 178–204 (2010).
    <https://doi.org/10.1021/cr900170z>
[^rev-01]: M. Nandakumar, A. Chatterjee, S. Sridhar, K. Joyner,
    M. Rodder and I.-C. Chen, "Shallow trench isolation for advanced
    ULSI CMOS technologies", *IEDM 1998 Technical Digest*, pp. 133–136.
    <https://doi.org/10.1109/IEDM.1998.746297>
[^thung-2016]: B. J. Thung, K. Ibrahim, N. A. Manap and F. Salehuddin,
    "Challenges for 0.13µm Generation Shallow Trench Isolation on
    0.18µm Equipment Platform", *Journal of Telecommunication,
    Electronic and Computer Engineering* **8**(5), 15–21 (2016).
    <https://jtec.utem.edu.my/jtec/article/view/697> (times out as of
    2026-09-19, both this User-Agent and a browser one; a Wayback
    Machine copy from 2026-04-11 confirms it was up; the PDF link
    below still works directly) (PDF:
    <https://jtec.utem.edu.my/jtec/article/download/697/707/3255>).
[^cook-1990]: L. M. Cook, "Chemical processes in glass polishing",
    *Journal of Non-Crystalline Solids* **120**(1–3), 152–171 (1990).
    <https://doi.org/10.1016/0022-3093(90)90200-6>
[^hoshino-2001]: T. Hoshino, Y. Kurata, Y. Terasaki and K. Susa,
    "Mechanism of polishing of SiO₂ films by CeO₂ particles", *Journal
    of Non-Crystalline Solids* **283**(1–3), 129–136 (2001).
    <https://doi.org/10.1016/S0022-3093(01)00364-7>
[^manivannan-2010]: R. Manivannan, S. Noyel Victoria and S. Ramanathan,
    "Mechanism of high selectivity in ceria based shallow trench
    isolation chemical mechanical polishing slurries", *Thin Solid
    Films* **518**(20), 5737–5740 (2010).
    <https://doi.org/10.1016/j.tsf.2010.05.072>
[^america-2004]: W. G. America and S. V. Babu, "Slurry Additive Effects
    on the Suppression of Silicon Nitride Removal during CMP",
    *Electrochemical and Solid-State Letters* **7**(12), G327 (2004).
    <https://doi.org/10.1149/1.1817870>
[^bu-2005]: K.-H. Bu and B. M. Moudgil, "Colloidal Silica based High
    Selectivity Shallow Trench Isolation (STI) Chemical Mechanical
    Polishing (CMP) Slurry", *MRS Proceedings* **867**, W8.5 (2005).
    <https://doi.org/10.1557/PROC-867-W8.5>
[^yu-1992]: C. Yu, P. C. Fazan, V. K. Mathews and T. T. Doan, "Dishing
    effects in a chemical mechanical polishing planarization process
    for advanced trench isolation", *Applied Physics Letters* **61**(11),
    1344–1346 (1992). <https://doi.org/10.1063/1.107586>
[^stine-1998]: B. E. Stine, D. O. Ouma, R. R. Divecha, D. S. Boning,
    J. E. Chung, D. L. Hetherington, C. R. Harwood, O. S. Nakagawa and
    S.-Y. Oh, "Rapid characterization and modeling of pattern-dependent
    variation in chemical-mechanical polishing", *IEEE Transactions on
    Semiconductor Manufacturing* **11**(1), 129–140 (1998).
    <https://doi.org/10.1109/66.661292>
[^chang-2005]: S.-H. Chang, "A dishing model for STI CMP process",
    *Microelectronic Engineering* **82**(2), 136–142 (2005).
    <https://doi.org/10.1016/j.mee.2005.07.002>
[^steigerwald-1997]: J. M. Steigerwald, S. P. Murarka and R. J. Gutmann,
    *Chemical Mechanical Planarization of Microelectronic Materials*,
    Wiley, 1997, ISBN 978-0-471-13827-6.
    <https://doi.org/10.1002/9783527617746>
[^oliver-2004]: M. R. Oliver (ed.), *Chemical-Mechanical Planarization
    of Semiconductor Materials*, Springer Series in Materials Science
    69, Springer, 2004, ISBN 978-3-540-43181-9.
    <https://doi.org/10.1007/978-3-662-06234-0>
[^pat-cmp-mirra]: R. D. Tolles, N. Shendon, S. Somekh, I. Perlov,
    E. Gantvarg and H. Q. Lee (Applied Materials), *Continuous
    processing system for chemical mechanical polishing*,
    US 5,738,574 A, granted 1998-04-14.
    <https://patents.google.com/patent/US5738574A/en>
[^pat-cmp-window]: M. Birang, A. Gleason and W. L. Guthrie (Applied
    Materials), *Forming a transparent window in a polishing pad for a
    chemical mechanical polishing apparatus*, US 5,893,796 A, granted
    1999-04-13. <https://patents.google.com/patent/US5893796A/en>
[^sun-2017]: T. Sun, Z. Han and M. Keswani, "Brush Scrubbing for
    Post-CMP Cleaning", in *Developments in Surface Contamination and
    Cleaning, Volume 9*, Elsevier, 2017, pp. 109–133.
    <https://doi.org/10.1016/B978-0-323-43157-6.00004-5>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
