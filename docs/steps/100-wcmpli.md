(step-100)=
# Step 100 — WCMPLI: W CMP for local interconnect

| | |
|---|---|
| **Step number** | 100 of 171[^steps-sheet] |
| **Step code** | `WCMPLI` |
| **Category** | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| **Phase** | {term}`MOL` — silicide and local interconnect |
| **Previous step** | {ref}`WDEP <step-099>` |
| **Next step** | {ref}`LITIN <step-101>` |

## What this step is

`WCMPLI` — tungsten {term}`CMP` for the {term}`local interconnect` — removes the
blanket tungsten of {ref}`WDEP <step-099>` and the Ti/TiN {term}`liner` of
{ref}`TI/TIN1 <step-097>` from the field, leaving tungsten only
inside the contact holes. The wafer is polished face-down in an
acidic, oxidising slurry (industry-typical) until the oxide of
{ref}`NCAPOX <step-091>` is exposed everywhere and every `licon1` is
an isolated
{term}`W plug` flush with the dielectric. The surface that results —
planar oxide studded with tungsten discs — is the surface on which
the titanium-nitride local interconnect ({ref}`LITIN <step-101>`) is
deposited and patterned; the later tungsten polishes {ref}`WCMP2 <step-111>` to
{ref}`WCMP5 <step-148>` do the same for the contact and {term}`via` plugs
under each metal level.

The PDK does not describe the polish, but its consequences are in
the rules: the local interconnect must enclose a licon by 0.080 µm
on one of two adjacent sides (li.5),[^pdk-periph] and "Licon1 must
overlap li1" (licon.4),[^pdk-periph] which is the layout expression
of the requirement that every plug be fully covered by the film that
lands on it. SkyWater's capability list names "AMAT Mirra CMP" with
"tungsten" and "high selectivity tungsten" among its
processes.[^skw-01]

## Step category

`WCMPLI` is a {ref}`Chemical-mechanical planarisation <category-cmp>`
step of the *tungsten* type, which the category page contrasts with
the {term}`STI` and oxide polishes: the film removed is tungsten and its
Ti/TiN liner, the stop is the inter-level oxide, the slurry is
alumina or silica with an oxidiser at pH 2–4, and the failure modes
are {term}`plug recess`, oxide {term}`erosion` in dense arrays, tungsten "coring"
and corrosion. It is the first metal polish in the flow. What is
specific to this instance is what lies under the oxide it stops on:
on the cap-stop reading of {ref}`CMPP <step-090>`, only the {term}`cap oxide`
separates the polish from the gate caps, so erosion here is erosion
of the dielectric that insulates the local interconnect from the
gates, and the per-plug recess it leaves is what the 0.1 µm-thick
TiN film[^pdk-04] must step down into.

## Why this step exists

The blanket tungsten is a short circuit across the whole wafer; it
has to go. The choice of polish over the older plasma etch-back, and
the demands on it:

* **Etch-back versus polish.** Kaanta et al.'s original tungsten-stud
  scheme used planarisation,[^kaanta-1987] and Kaufman et al. at IBM
  showed in 1991 how tungsten can be polished by a cycle of chemical
  oxidation and mechanical abrasion — the oxidiser forms a thin WO₃
  that the abrasive removes, so that the polish is self-limiting on
  the oxide, where nothing oxidises.[^kaufman-1991] A fluorine
  etch-back (SF₆/Ar) leaves plug recess wherever the etch reaches
  the seam and cannot planarise; CMP does both jobs.
* **Chemistry.** Krishnan, Nalaskowski and Cook review the slurry
  chemistry;[^rev-02] Stein, Hetherington and Cecchi worked out the
  kinetics in potassium-iodate slurries,[^stein-1999] Elbel et al.
  the tungsten polish generally,[^elbel-1998] and Bielmann et al.
  the effect of abrasive particle size.[^bielmann-1999] The
  oxidiser (H₂O₂, Fe(NO₃)₃, KIO₃) and pH set the tungsten rate; the
  abrasive and pad set the oxide rate; their ratio is the
  {term}`selectivity` that decides how much oxide is lost in the
  over-polish.
* **Plug recess and erosion.** The tungsten in a plug polishes
  faster than the surrounding oxide once the field clears, so plugs
  recess; dense plug arrays erode the oxide around them. Both
  translate into topography under the local interconnect and into
  higher, more variable contact resistance; Wang et al. characterise
  an integrated tungsten CMP for plugs,[^wang-2002-wcmp] and Lee et
  al. optimised a plug polish across consumables.[^lee-2001-wcmp]
  The "high selectivity tungsten" process SkyWater lists[^skw-01] is,
  we infer, a slurry that stops sharply on oxide to limit exactly
  these effects.
* **Endpoint.** Because the tungsten is opaque and the oxide is not,
  and because the motor torque changes as the metal clears, tungsten
  CMP is one of the easier polishes to {term}`endpoint`: Sue, Lültzen and
  Gonzales describe tungsten CMP endpoint detection,[^sue-1999] and
  Bibby and Holland's 1998 paper, by its abstract, discusses "many of
  the approaches that have been published".[^bibby-1998] The over-polish
  after endpoint is what removes the liner and the last tungsten
  residue ("coring" — tungsten pulled from plug seams — is one
  defect of too little; recess of too much).
* **Corrosion and cleaning.** Tungsten and its liner form a galvanic
  couple in the slurry, and slurry residue corrodes the plugs; the
  {term}`post-CMP clean` is part of the step.

Without `WCMPLI` the local interconnect could not be patterned — it
would be deposited on a continuous sheet of tungsten.

## How it is typically performed

An industry-generic tungsten plug polish for a 200 mm, 130 nm-era
fab (SKY130's recipe is not public):

1. **Tool.** Rotary multi-platen polisher with a dedicated tungsten
   head or platen (tungsten and oxide slurries are not mixed),
   polyurethane pads, diamond conditioner, multi-zone carrier head
   (category page; the Mirra architecture[^pat-cmp-mirra]).
2. **Slurry.** Alumina or silica abrasive with an oxidiser —
   hydrogen peroxide, ferric nitrate or potassium iodate — at pH 2–4
   (typical industry chemistry[^rev-02][^stein-1999]); the tungsten
   removal rate follows the {term}`Preston equation` in pressure and
   velocity to first order.[^preston-1927]
3. **Recipe.** A first platen removes the bulk tungsten at high
   rate; a second clears the field, detects endpoint and removes the
   Ti/TiN liner (which polishes more slowly than tungsten and
   sometimes needs its own slurry); an over-polish sized to the
   liner thickness plus margin; a final buff on a soft pad with
   dilute slurry or DI water.
4. **Endpoint.** Motor-current or optical detection of the
   tungsten-to-oxide transition;[^sue-1999][^bibby-1998] the
   in-situ pad-window method of the Applied Materials
   patent[^pat-cmp-window] or the platen-window method of IBM's.[^pat-cmp-endpoint-ibm]
5. **Post-CMP clean.** Double-sided brush scrub with a
   corrosion-inhibiting chemistry (dilute NH₄OH or citric acid),
   sometimes a dilute-HF touch to lift slurry particles from the
   oxide, spin-rinse-dry; tungsten corrosion is checked by
   inspection (category page).
6. **Metrology.** Remaining oxide thickness on field test pads;
   plug recess and erosion by profilometry or AFM on plug arrays;
   residual tungsten by optical inspection and unpatterned defect
   scan; contact-chain resistance ({ref}`category-test`).

## Machines typically used

* **{ref}`Rotary multi-platen CMP polisher <machine-cmp-polisher>`**, 200 mm: Applied Materials Mirra and Mirra
  Mesa,[^amat-1997][^chiphistory-mirra][^amat-mesa-1999] Ebara F-REX,[^ebara-frex]
  SpeedFam-IPEC Avanti 472, Strasbaugh 6DS-SP (category page).
* **{ref}`Post-CMP brush scrubber <machine-post-cmp-cleaner>`** (OnTrak/Lam DSS-200, Applied Mesa
  integrated cleaner).
* **{ref}`Optical film-thickness mapper <machine-film-thickness-metrology>`**; **{ref}`profilometer/AFM <machine-cross-section-sem-profilers>`**;
  **{ref}`unpatterned defect inspection <machine-defect-inspection>`**.

## Machines likely used at SkyWater

* **Applied Materials Mirra CMP, tungsten.** SkyWater lists "AMAT
  Mirra CMP" with "tungsten" and "high selectivity tungsten" among
  its processes.[^skw-01] Strength: **strong** for the tool and its
  tungsten polishes (SkyWater statement); assignment to this step is
  an **inference** from the film, since the list names no steps (a
  tungsten polish has no other purpose in this flow than the plug
  levels); which of the two tungsten processes runs this step is not
  public.
* **Post-CMP cleaning.** SkyWater lists the "SEZ223, Davinci"
  single-wafer tools with HF and DSP+HF chemistries, and the Mirra
  entry also lists "Track ammonia clean" and "IPA clean";[^skw-01] a
  brush scrubber is not named on any public page (open question).
* **Defect inspection — KLA AIT / SP1**, our reading of "AIT" and "SP1"
  in a SkyWater job posting's "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
  Strength: medium.

## Resources required

* **{ref}`Tungsten slurry <material-cmp-consumables>`** — alumina or silica with H₂O₂ ({ref}`wet chemicals <material-wet-chemicals>`), Fe(NO₃)₃ or
  KIO₃ oxidiser (typical industry chemistry[^rev-02][^stein-1999]).
* **Polishing pads** (stacked polyurethane, IC1000/Suba IV class), **diamond
  conditioners**, **carrier films, membranes and retaining
  rings**.[^steigerwald-1997]
* **{ref}`DI water <material-ultrapure-water>`** in quantity; **dilute NH₄OH** or **TMAH**,[^jolley-1998]
  possibly **citric acid** or **dilute HF** (category page), for the
  post-CMP clean; **PVA brushes**.
* **{ref}`Monitor wafers <material-substrates>`** with blanket tungsten and oxide for rate and
  selectivity checks.[^semi-m8]
* Chemical suppliers named in SkyWater's 2021 S-1: KMG
  Chemicals.[^sec-01]

## Related steps and cross-references

* Previous: {ref}`WDEP <step-099>` (the blanket tungsten). Next:
  {ref}`LITIN <step-101>` (the TiN film deposited on the polished
  plugs), then {ref}`LI1M <step-102>` and {ref}`LI1ME <step-103>`.
* The liner removed from the field: {ref}`TI/TIN1 <step-097>`; the
  oxide the polish stops on: {ref}`NCAPOX <step-091>`.
* The earlier polish that set the surface: {ref}`CMPP <step-090>`;
  the STI polish: {ref}`CMPNIT <step-012>`.
* Later tungsten polishes: {ref}`WCMP2 <step-111>`,
  {ref}`WCMP3 <step-122>`, {ref}`WCMP4 <step-133>`,
  {ref}`WCMP5 <step-148>`.
* Category page: {ref}`Chemical-mechanical planarisation <category-cmp>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

**Related patents.**

* {ref}`In-situ endpoint detection and process monitoring method and apparatus for chemical-mechanical polishing <patent-gp22631367>` — US 5,433,651 A (1993)
* {ref}`Forming a transparent window in a polishing pad for a chemical mechanical polishing apparatus <patent-gp24770421>` — US 5,893,796 A (1995)
* {ref}`Continuous processing system for chemical mechanical polishing <patent-gp24192580>` — US 5,738,574 A (1995)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — "AMAT Mirra CMP":
  "tungsten", "high selectivity tungsten"; SEZ/Da Vinci
  cleaners.[^skw-01]
* SkyWater PDK, *Periphery rules* — licon.4, li.5.[^pdk-periph]
* SkyWater PDK, process stack diagram — `li` 0.1 µm.[^pdk-04]
* Applied Materials, 1997 Annual Report; Chip History Center on the
  Mirra.[^amat-1997][^chiphistory-mirra]
* SkyWater, Form S-1 — chemical suppliers.[^sec-01]
* LinkedIn, SkyWater *Defect Technician 2* posting — inspection
  tools.[^job-06]

### High-level understanding

* Wikipedia, *Chemical-mechanical polishing* — tungsten among the
  polished materials.[^wiki-cmp]
* Steigerwald, Murarka and Gutmann, *Chemical Mechanical
  Planarization of Microelectronic Materials* — the tungsten
  chapter.[^steigerwald-1997]
* Zantye, Kumar and Sikder, *Mater. Sci. Eng. R* 2004 — a long
  review of CMP including metal polishes.[^zantye-2004]

### Deep dive

* Jolley, *Solid State Phenomena* 1998 — TMAH as a post-tungsten-CMP
  clean.[^jolley-1998]
* Kaufman et al. (IBM), *J. Electrochem. Soc.* 1991 — tungsten CMP
  by oxidation and abrasion, the founding paper.[^kaufman-1991]
* Kaanta et al. (IBM), IEDM 1987 — tungsten studs and
  planarisation.[^kaanta-1987]
* Krishnan, Nalaskowski and Cook, *Chem. Rev.* 2010 — slurry
  chemistry for tungsten CMP.[^rev-02]
* Stein, Hetherington and Cecchi, *J. Electrochem. Soc.* 1999 —
  kinetics of tungsten CMP in iodate slurries.[^stein-1999]
* Elbel et al., *J. Electrochem. Soc.* 1998 — tungsten chemical
  mechanical polishing.[^elbel-1998]
* Bielmann et al., *Electrochem. Solid-State Lett.* 1999 — particle
  size in tungsten CMP.[^bielmann-1999]
* Wang et al., *JJAP* 2002 — integrated tungsten CMP for via
  plugs.[^wang-2002-wcmp]
* Lee et al., *J. Mater. Sci.: Mater. Electron.* 2001 — plug CMP
  optimisation across consumables.[^lee-2001-wcmp]
* Sue, Lültzen and Gonzales, *MRS Proc.* 1999 — tungsten CMP
  endpoint detection.[^sue-1999]
* Bibby and Holland, *J. Electron. Mater.* 1998 — endpoint
  methods.[^bibby-1998]
* Preston, *J. Soc. Glass Technol.* 1927 — the removal-rate
  law.[^preston-1927]
* Tolles et al., Birang et al. and Lustig et al. — Mirra
  architecture, pad window and in-situ endpoint
  patents.[^pat-cmp-mirra][^pat-cmp-window][^pat-cmp-endpoint-ibm]
* Oliver (ed.), *Chemical-Mechanical Planarization of Semiconductor
  Materials* — metal CMP and post-CMP cleaning chapters.[^oliver-2004]

## Open questions

* The slurry (abrasive, oxidiser), the liner-removal strategy, the
  endpoint method and the over-polish are not public.
* What SkyWater's "high selectivity tungsten" process is, and
  whether it is used here, is not public.
* The plug recess and oxide erosion the polish leaves, which the
  0.1 µm local interconnect must cover, are not public.
* Whether SkyWater uses a brush scrubber, and which, is not stated
  on any public page.

<!-- footnotes -->
[^amat-mesa-1999]: Applied Materials, *Applied Materials Announces New
    Mirra Mesa System to Address Market Demand for Integrated CMP
    Solutions*, press release, 1999-06-10, accessed 2026-09-13.
    <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-new-mirra-mesa-system-address-market>

[^jolley-1998]: M. Jolley, "Applications of Tetramethylammoninium
    Hydroxide (TMAH) as a Post Tungsten CMP Cleaning Mixture", *Solid
    State Phenomena* **65–66**, 105–108 (1998).
    <https://doi.org/10.4028/www.scientific.net/SSP.65-66.105>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram). <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^job-06]: LinkedIn, *SkyWater Technology hiring Defect Technician 2 in
    Bloomington, MN* (job posting), retrieved 2026-09-19.
    <https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report*.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^chiphistory-mirra]: Chip History Center, *The Mirra CMP System by
    Applied Materials*.
    <https://www.chiphistory.org/142-applied-materials-the-mirra-cmp-system>
[^ebara-frex]: EBARA Precision Machinery Europe, *CMP Tools*
    (F-REX200M2). <https://www.ebara-pm.eu/systems/cmp-tools/>
[^wiki-cmp]: Wikipedia, *Chemical-mechanical polishing*.
    <https://en.wikipedia.org/wiki/Chemical-mechanical_polishing>
[^steigerwald-1997]: J. M. Steigerwald, S. P. Murarka and R. J. Gutmann,
    *Chemical Mechanical Planarization of Microelectronic Materials*,
    Wiley, 1997, ISBN 978-0-471-13827-6.
    <https://doi.org/10.1002/9783527617746>
[^zantye-2004]: P. B. Zantye, A. Kumar and A. K. Sikder, "Chemical
    mechanical planarization for microelectronics applications",
    *Materials Science and Engineering: R* **45**(3–6), 89–220 (2004).
    <https://doi.org/10.1016/j.mser.2004.06.002>
[^oliver-2004]: M. R. Oliver (ed.), *Chemical-Mechanical Planarization
    of Semiconductor Materials*, Springer Series in Materials Science
    69, Springer, 2004, ISBN 978-3-540-43181-9.
    <https://doi.org/10.1007/978-3-662-06234-0>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^kaufman-1991]: F. B. Kaufman, D. B. Thompson, R. E. Broadie, M. A.
    Jaso et al., "Chemical-Mechanical Polishing for Fabricating
    Patterned W Metal Features as Chip Interconnects", *Journal of The
    Electrochemical Society* **138**(11), 3460–3465 (1991).
    <https://doi.org/10.1149/1.2085434>
[^kaanta-1987]: C. Kaanta, W. Cote, J. Cronin, K. Holland et al.,
    "Submicron wiring technology with tungsten and planarization", *IEDM
    1987 Technical Digest*, pp. 209–212.
    <https://doi.org/10.1109/IEDM.1987.191389>
[^rev-02]: M. Krishnan, J. W. Nalaskowski and L. M. Cook, "Chemical
    Mechanical Planarization: Slurry Chemistry, Materials, and
    Mechanisms", *Chemical Reviews* **110**(1), 178–204 (2010).
    <https://doi.org/10.1021/cr900170z>
[^stein-1999]: D. Stein, D. L. Hetherington and J. L. Cecchi,
    "Investigation of the Kinetics of Tungsten Chemical Mechanical
    Polishing in Potassium Iodate-Based Slurries: I. Role of Alumina and
    Potassium Iodate", *Journal of The Electrochemical Society*
    **146**(1), 376–381 (1999). <https://doi.org/10.1149/1.1391617>
[^elbel-1998]: N. Elbel, B. Neureither, B. Ebersberger and P. Lahnor,
    "Tungsten Chemical Mechanical Polishing", *Journal of The
    Electrochemical Society* **145**(5), 1659–1664 (1998).
    <https://doi.org/10.1149/1.1838533>
[^bielmann-1999]: M. Bielmann et al., "Effect of Particle Size during
    Tungsten Chemical Mechanical Polishing", *Electrochemical and
    Solid-State Letters* **2**(8), 401 (1999).
    <https://doi.org/10.1149/1.1390851>
[^wang-2002-wcmp]: C.-K. Wang, H.-S. Wu, N.-T. Ou and H.-C. Cheng,
    "Integrated Tungsten Chemical Mechanical Polishing Process
    Characterization for Via Plug Interconnection in Ultralarge Scale
    Integrated Circuits", *Japanese Journal of Applied Physics*
    **41**(8R), 5120–5124 (2002). <https://doi.org/10.1143/JJAP.41.5120>
[^lee-2001-wcmp]: W.-S. Lee, S.-Y. Kim, Y.-J. Seo and J.-K. Lee, "An
    optimization of tungsten plug chemical mechanical polishing (CMP)
    using different consumables", *Journal of Materials Science:
    Materials in Electronics* **12**(1), 63–68 (2001).
    <https://doi.org/10.1023/A:1011276830620>
[^sue-1999]: L. Sue, J. Lültzen and S. Gonzales, "Tungsten Chemical
    Mechanical Polishing Endpoint Detection", *MRS Proceedings* **566**,
    109 (1999). <https://doi.org/10.1557/PROC-566-109>
[^bibby-1998]: T. Bibby and K. Holland, "Endpoint detection for CMP",
    *Journal of Electronic Materials* **27**(10), 1073–1081 (1998).
    <https://doi.org/10.1007/s11664-998-0140-1>
[^preston-1927]: F. W. Preston, "The theory and design of plate glass
    polishing machines", *Journal of the Society of Glass Technology*
    **11**, 214–256 (1927). No DOI or online copy of the article
    itself is public; library record for the volume:
    <https://books.google.com/books/about/Journal_of_the_Society_of_Glass_Technolo.html?id=3CTyAAAAMAAJ>
[^pat-cmp-mirra]: R. D. Tolles, N. Shendon, S. Somekh, I. Perlov,
    E. Gantvarg and H. Q. Lee (Applied Materials), *Continuous
    processing system for chemical mechanical polishing*,
    US 5,738,574 A, granted 1998-04-14.
    <https://patents.google.com/patent/US5738574A/en>
[^pat-cmp-window]: M. Birang, A. Gleason and W. L. Guthrie (Applied
    Materials), *Forming a transparent window in a polishing pad for a
    chemical mechanical polishing apparatus*, US 5,893,796 A, granted
    1999-04-13. <https://patents.google.com/patent/US5893796A/en>
[^pat-cmp-endpoint-ibm]: N. E. Lustig, K. L. Saenger and H.-M. Tong
    (IBM), *In-situ endpoint detection and process monitoring method and
    apparatus for chemical-mechanical polishing*, US 5,433,651 A,
    granted 1995-07-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5433651>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
