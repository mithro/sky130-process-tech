(step-106)=
# Step 106 — CMPL: CMP polish over local interconnect

| | |
|---|---|
| **Step number** | 106 of 171[^steps-sheet] |
| **Step code** | `CMPL` |
| **Category** | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| **Phase** | MOL — silicide and local interconnect |
| **Previous step** | {ref}`NILD2 <step-105>` |
| **Next step** | {ref}`CTM1 <step-107>` |

## What this step is

`CMPL` — chemical-mechanical polish over the {term}`local interconnect` —
planarises the inter-level oxide of {ref}`NILD2 <step-105>` and sets
its final thickness. The as-deposited oxide copies the 0.1 µm TiN
lines and their 0.075 µm nitride cap[^pdk-04] beneath it, more
strongly over dense {term}`LI` arrays than over open field; the wafer is
polished in an alkaline silica slurry (industry-typical) until that
topography is gone and a controlled thickness of oxide — the PDK's
0.265 µm "NILD2"
between the top of the nitride cap over `li` and the `metal1`
bottom[^pdk-04] — remains
over the local interconnect. It is the last step of the
middle-of-line module: the surface it leaves is the one on which the
`mcon` contacts are printed ({ref}`CTM1 <step-107>`) and etched
({ref}`CTME <step-108>`) and on which metal 1 is deposited. The same
step recurs, as `CMPM`, over every metal level
({ref}`CMPM <step-116>` and later).

Unlike {ref}`CMPP <step-090>`, this polish has no nitride stop and no
"sacrificial" film: it is a fixed-removal oxide planarisation whose
target is a thickness, not a surface. The removal is not public; on
the reading of the {ref}`NILD2 <step-105>` page it is of the order
of a few hundred nanometres, the difference between an as-deposited
oxide thick enough to fill and bury the LI and the 0.265 µm that
remains.

## Step category

`CMPL` is a {ref}`Chemical-mechanical planarisation <category-cmp>`
step of the *oxide (ILD)* type, the class the category page
characterises by fixed removal, a silica/KOH or NH₄OH slurry at pH
10–11 and pattern-density non-uniformity as the main failure mode.
What is specific to this instance is the thinness of the films
involved: the step to be planarised is only about 0.175 µm, the
remaining oxide only 0.265 µm,[^pdk-04] and beneath that oxide lie
the nitride cap and the 0.1 µm TiN — so an over-polish that would be
harmless on a thick {term}`inter-metal dielectric` here reaches the nitride
over dense LI, and an under-polish leaves steps that the 0.17 µm
`mcon` lithography ({ref}`CTM1 <step-107>`; ct.1[^pdk-periph])
cannot tolerate. The polish is therefore controlled to a remaining
thickness with tighter tolerance than the CMPM polishes that follow.

## Why this step exists

The reasons are those of every inter-level polish, sharpened by the
thin films:

* **Planarity for the contact lithography.** The `mcon` layer prints
  0.17 µm holes (ct.1) on a 0.19 µm spacing (ct.2),[^pdk-periph] and
  the {ref}`LICM1 <step-093>` page sets out why holes of that size
  need a deep-UV depth of focus of a few hundred nanometres; the
  oxide over the LI must be flat to a fraction of that. Kaanta et
  al.'s tungsten-stud scheme and Davari et al.'s RIE-plus-CMP
  planarisation are the origins of the polished-ILD contact
  module.[^kaanta-1987][^davari-1989]
* **Uniform contact depth.** Every `mcon` is etched through the same
  oxide thickness to the nitride cap over its LI line; a
  non-uniform oxide would leave some contacts unopened while others
  are over-etched through the nitride into the TiN. The 0.265 µm
  figure[^pdk-04] and the "min. etch and fill capability for mcon"
  of 0.14 µm[^pdk-03] are what the polish delivers to the contact
  etch.
* **Pattern-density control.** Oxide over a dense LI array polishes
  differently from oxide over open field; Stine et al. and Ouma et
  al. modelled the effect,[^stine-1998][^ouma-2002] Daubenspeck et
  al. characterised planarisation over variable densities,[^daubenspeck-1991]
  and the PDK's density criteria — "Min pattern density for oxide"
  0.75 and the density boxes[^pdk-03] — apply to this level as they
  did to {ref}`CMPP <step-090>`; Kahng and Samadi survey the fill
  synthesis that keeps LI-level density within the window.[^kahng-2008]
* **Defectivity.** Scratches and slurry residue from this polish
  become contact and metal-1 defects; the {term}`post-CMP clean` is part of
  the step, and the {ref}`NCAPOX3 <step-117>`-style cap that follows
  a metal-level polish has no counterpart here, so the polished
  surface itself must be clean enough for lithography.

Without `CMPL` the `mcon` lithography would print over LI topography
and the contact etch would face a different depth on every line.

## How it is typically performed

An industry-generic thin-ILD oxide polish for a 200 mm, 130 nm-era
fab (SKY130's recipe is not public):

1. **Tool.** Rotary multi-platen polisher with stacked polyurethane
   pads, diamond conditioner, carrier head with retaining ring and
   multi-zone membrane (category page; the Mirra
   architecture[^pat-cmp-mirra]).
2. **Slurry.** Fumed-silica in KOH or NH₄OH at pH 10–11 (typical
   industry chemistry[^rev-02][^steigerwald-1997]); Cook's chemistry
   of glass polishing[^cook-1990] and the {term}`Preston equation`
   removal law[^preston-1927] with the departures Nanz and Camilletti
   review.[^nanz-1995]
3. **Recipe.** A first platen removes the bulk at high rate; a
   second finishes to the target thickness at lower rate for
   uniformity; a final platen buffs in DI water or dilute slurry.
   Down-force of a few psi and platen speeds of tens of rpm are
   typical.[^txt-05] The removal is small, so the recipe is short
   and its uniformity is set by the head's zone pressures.
4. **Endpoint.** Time plus post-polish thickness measurement — the
   "blind polishing" Wikipedia describes for oxide[^wiki-cmp] —
   supplemented, on tools that have it, by in-situ optical
   thickness monitoring through a pad window;[^pat-cmp-window] Bibby
   and Holland review the options.[^bibby-1998] Run-to-run control
   adjusts the time from the previous lot's measured removal.
5. **Post-CMP clean.** Double-sided brush scrub in dilute NH₄OH,
   spin-rinse-dry; slurry residue must be gone before the wafer
   dries.
6. **Metrology.** Remaining oxide over LI and over field on test
   pads by optical thickness mapping (the 0.265 µm target); step
   height over LI arrays by profilometry; defect scan for scratches;
   `mcon` contact-chain resistance after the next module as the
   electrical proof ({ref}`category-test`).

## Machines typically used

* **Rotary multi-platen CMP polisher**, 200 mm: Applied Materials Mirra and Mirra
  Mesa,[^amat-1997][^chiphistory-mirra] Ebara F-REX,[^ebara-frex]
  SpeedFam-IPEC Avanti 472, Strasbaugh 6EC (category page).
* **Post-CMP brush scrubber** (OnTrak/Lam DSS-200, Applied Mesa
  integrated cleaner).
* **Optical film-thickness mapper**; **stylus profiler**;
  **unpatterned defect inspection**.

## Machines likely used at SkyWater

* **Applied Materials Mirra CMP.** SkyWater lists "AMAT Mirra CMP"
  for oxide among its films.[^skw-01] Strength: **strong** for the
  tool and its oxide polish (SkyWater statement); assignment to this
  step is an **inference** from the film, since the list names no
  steps.
* **Post-CMP cleaning.** SkyWater lists the "SEZ223, Davinci"
  single-wafer tools with HF and DSP+HF chemistries, and the Mirra
  entry also lists "Track ammonia clean" and "IPA clean";[^skw-01] a
  brush scrubber is not named on any public page (open question).
* **Defect inspection — KLA AIT / SP1** per a SkyWater job
  posting.[^job-01] Strength: medium.

## Resources required

* **Oxide slurry** — fumed or colloidal silica in KOH or NH₄OH
  (typical industry chemistry[^rev-02][^steigerwald-1997]).
* **Polishing pads** (IC1000/Suba IV class) and **diamond
  conditioners**; **carrier films, membranes and retaining
  rings**.[^steigerwald-1997]
* **DI water** in quantity; **dilute NH₄OH** for post-CMP cleaning;
  **PVA brushes**.
* **Monitor wafers** with blanket oxide for rate checks.[^semi-m8]
* Chemical suppliers named by SkyWater: KMG Chemicals.[^sec-01]

## Related steps and cross-references

* Previous: {ref}`NILD2 <step-105>` (the film polished). Next:
  {ref}`CTM1 <step-107>` (the metal-1 contact mask), then
  {ref}`CTME <step-108>`.
* The conductors and cap beneath the oxide: {ref}`LITIN <step-101>`,
  {ref}`LI1ME <step-103>`, {ref}`LINIT <step-104>`.
* The earlier oxide polish of the module: {ref}`CMPP <step-090>`;
  the tungsten polish: {ref}`WCMPLI <step-100>`; the {term}`STI` polish:
  {ref}`CMPNIT <step-012>`.
* The later metal-level polishes: {ref}`CMPM <step-116>`,
  {ref}`CMPM2 <step-127>`.
* Category page: {ref}`Chemical-mechanical planarisation <category-cmp>`.

## References

### Cross-check

* SkyWater PDK, process stack diagram — "NILD2" 0.265 µm; `li`
  0.1 µm; LINT 0.075 µm.[^pdk-04]
* SkyWater PDK, *Criteria & Assumptions* — "min. etch and fill
  capability for mcon" 0.14 µm; "Min pattern density for oxide"
  0.75; density boxes.[^pdk-03]
* SkyWater PDK, *Periphery rules* — ct.1 0.170 µm, ct.2 0.190 µm.[^pdk-periph]
* SkyWater, *Facilities & Capabilities* — "AMAT Mirra CMP" and its
  film list; SEZ/Da Vinci cleaners.[^skw-01]
* Applied Materials, 1997 Annual Report — the Mirra product
  line.[^amat-1997]
* SkyWater, Form S-1 — chemical suppliers.[^sec-01]
* Indeed, SkyWater *Defect Technician 2* posting — inspection
  tools.[^job-01]

### High-level understanding

* Wikipedia, *Chemical-mechanical polishing*.[^wiki-cmp]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — dielectric
  CMP.[^txt-05]
* Steigerwald, Murarka and Gutmann, *Chemical Mechanical
  Planarization of Microelectronic Materials*.[^steigerwald-1997]
* Chip History Center, *The Mirra CMP System*.[^chiphistory-mirra]

### Deep dive

* Davari et al. (IBM), IEDM 1989 — RIE plus CMP planarisation of
  the inter-level dielectric.[^davari-1989]
* Daubenspeck et al. (IBM), *J. Electrochem. Soc.* 1991 —
  planarisation over variable pattern densities.[^daubenspeck-1991]
* Kaanta et al. (IBM), IEDM 1987 — tungsten studs on a polished
  dielectric.[^kaanta-1987]
* Preston, *J. Soc. Glass Technol.* 1927, and Nanz and Camilletti,
  *IEEE TSM* 1995 — the removal-rate law and CMP
  models.[^preston-1927][^nanz-1995]
* Cook, *J. Non-Cryst. Solids* 1990 — the chemistry of glass
  polishing.[^cook-1990]
* Krishnan, Nalaskowski and Cook, *Chem. Rev.* 2010 — slurry
  chemistry.[^rev-02]
* Stine et al., *IEEE TSM* 1998, and Ouma et al., *IEEE TSM* 2002 —
  pattern-density models of oxide CMP.[^stine-1998][^ouma-2002]
* Bibby and Holland, *J. Electron. Mater.* 1998 — endpoint detection
  for CMP.[^bibby-1998]
* Kahng and Samadi, *IEEE TCAD* 2008 — dummy-fill synthesis.[^kahng-2008]
* Chow et al. and Beyer et al. (IBM) — the foundational
  metal/insulator CMP patents.[^pat-cmp-ibm-1988][^pat-cmp-ibm-1990]
* Tolles et al. and Birang et al. (Applied Materials) — Mirra
  architecture and pad-window endpoint patents.[^pat-cmp-mirra][^pat-cmp-window]
* Oliver (ed.), *Chemical-Mechanical Planarization of Semiconductor
  Materials* — dielectric CMP and cleaning chapters.[^oliver-2004]

## Open questions

* The removal amount, slurry, {term}`endpoint` method and post-CMP clean are
  not public.
* Whether the 0.265 µm of the stack diagram is the post-polish
  thickness over LI (our reading) or a nominal design value is not
  stated.[^pdk-04]
* Whether SkyWater uses a brush scrubber, and which, is not stated
  on any public page.

<!-- footnotes -->

[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram). <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^job-01]: Indeed, *Skywater Technology Foundry Jobs, Employment in
    Bloomington, MN* (listing page; *Defect Technician 2* posting),
    retrieved 2026-08-30; listings expire.
    <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
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
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^steigerwald-1997]: J. M. Steigerwald, S. P. Murarka and R. J. Gutmann,
    *Chemical Mechanical Planarization of Microelectronic Materials*,
    Wiley, 1997, ISBN 978-0-471-13827-6.
    <https://doi.org/10.1002/9783527617746>
[^oliver-2004]: M. R. Oliver (ed.), *Chemical-Mechanical Planarization
    of Semiconductor Materials*, Springer Series in Materials Science
    69, Springer, 2004, ISBN 978-3-540-43181-9.
    <https://doi.org/10.1007/978-3-662-06234-0>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^davari-1989]: B. Davari, C. W. Koburger, R. Schulz, J. D. Warnock,
    T. Furukawa, M. Jost, Y. Taur, W. G. Schwittek, J. K. DeBrosse,
    M. L. Kerbaugh and J. L. Mauer, "A new planarization technique,
    using a combination of RIE and chemical mechanical polish (CMP)",
    *IEDM 1989 Technical Digest*, pp. 61–64.
    <https://doi.org/10.1109/IEDM.1989.74228>
[^daubenspeck-1991]: T. H. Daubenspeck, J. K. DeBrosse, C. W. Koburger,
    M. Armacost and J. R. Abernathey, "Planarization of ULSI Topography
    over Variable Pattern Densities", *Journal of The Electrochemical
    Society* **138**(2), 506–509 (1991).
    <https://doi.org/10.1149/1.2085619>
[^kaanta-1987]: C. Kaanta, W. Cote, J. Cronin, K. Holland et al.,
    "Submicron wiring technology with tungsten and planarization", *IEDM
    1987 Technical Digest*, pp. 209–212.
    <https://doi.org/10.1109/IEDM.1987.191389>
[^preston-1927]: F. W. Preston, "The theory and design of plate glass
    polishing machines", *Journal of the Society of Glass Technology*
    **11**, 214–256 (1927).
[^nanz-1995]: G. Nanz and L. E. Camilletti, "Modeling of
    chemical-mechanical polishing: a review", *IEEE Transactions on
    Semiconductor Manufacturing* **8**(4), 382–389 (1995).
    <https://doi.org/10.1109/66.475179>
[^cook-1990]: L. M. Cook, "Chemical processes in glass polishing",
    *Journal of Non-Crystalline Solids* **120**(1–3), 152–171 (1990).
    <https://doi.org/10.1016/0022-3093(90)90200-6>
[^rev-02]: M. Krishnan, J. W. Nalaskowski and L. M. Cook, "Chemical
    Mechanical Planarization: Slurry Chemistry, Materials, and
    Mechanisms", *Chemical Reviews* **110**(1), 178–204 (2010).
    <https://doi.org/10.1021/cr900170z>
[^stine-1998]: B. E. Stine, D. O. Ouma, R. R. Divecha, D. S. Boning, J.
    E. Chung, D. L. Hetherington, C. R. Harwood, O. S. Nakagawa and
    S.-Y. Oh, "Rapid characterization and modeling of pattern-dependent
    variation in chemical-mechanical polishing", *IEEE Transactions on
    Semiconductor Manufacturing* **11**(1), 129–140 (1998).
    <https://doi.org/10.1109/66.661292>
[^ouma-2002]: D. O. Ouma, D. S. Boning, J. E. Chung, W. G. Easter et
    al., "Characterization and modeling of oxide chemical-mechanical
    polishing using planarization length and pattern density concepts",
    *IEEE Transactions on Semiconductor Manufacturing* **15**(2),
    232–244 (2002). <https://doi.org/10.1109/66.999598>
[^bibby-1998]: T. Bibby and K. Holland, "Endpoint detection for CMP",
    *Journal of Electronic Materials* **27**(10), 1073–1081 (1998).
    <https://doi.org/10.1007/s11664-998-0140-1>
[^kahng-2008]: A. B. Kahng and K. Samadi, "CMP Fill Synthesis: A Survey
    of Recent Studies", *IEEE Transactions on Computer-Aided Design of
    Integrated Circuits and Systems* **27**(1), 3–19 (2008).
    <https://doi.org/10.1109/TCAD.2007.907061>
[^pat-cmp-ibm-1988]: M. M. Chow, J. E. Cronin, W. L. Guthrie, C. W. Kaanta
    et al. (IBM), *Method for producing coplanar multi-level
    metal/insulator films on a substrate and for forming patterned
    conductive lines simultaneously with stud vias*, US 4,789,648 A,
    granted 1988-12-06.
    <https://patents.google.com/patent/US4789648A/en>
[^pat-cmp-ibm-1990]: K. D. Beyer et al. (IBM), *Chem-mech polishing
    method for producing coplanar metal/insulator films on a substrate*,
    US 4,944,836 A, granted 1990.
    <https://patents.google.com/patent/US4944836A/en>
[^pat-cmp-mirra]: R. D. Tolles, N. Shendon, S. Somekh, I. Perlov,
    E. Gantvarg and H. Q. Lee (Applied Materials), *Continuous
    processing system for chemical mechanical polishing*,
    US 5,738,574 A, granted 1998-04-14.
    <https://patents.google.com/patent/US5738574A/en>
[^pat-cmp-window]: M. Birang, A. Gleason and W. L. Guthrie (Applied
    Materials), *Forming a transparent window in a polishing pad for a
    chemical mechanical polishing apparatus*, US 5,893,796 A, granted
    1999-04-13. <https://patents.google.com/patent/US5893796A/en>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
