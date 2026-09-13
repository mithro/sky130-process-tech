(step-090)=
# Step 090 — CMPP: CMP over poly

| | |
|---|---|
| **Step number** | 90 of 171[^steps-sheet] |
| **Step code** | `CMPP` |
| **Category** | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| **Phase** | MOL — silicide and local interconnect |
| **Previous step** | {ref}`PSG <step-089>` |
| **Next step** | {ref}`NCAPOX <step-091>` |

## What this step is

`CMPP` — chemical-mechanical polish "over poly" — planarises the
sacrificial phosphosilicate glass of {ref}`PSG <step-089>`. The
as-deposited glass copies the topography beneath it: it stands
roughly 0.4 µm higher over every capped gate line and resistor body
(0.18 µm poly plus the 0.2 µm cap[^pdk-03]) than over the field and
the source/drains, with an HDP film's characteristic peaked profile
over narrow lines. The wafer is pressed against a rotating pad in an
alkaline silica slurry (industry-typical) until those peaks are gone
and the surface is flat to within the depth of focus of the contact
lithography that follows.

How far down the polish goes is the crux of the step, and it is not
public. Two readings are consistent with the PDK. On the first, the
polish is a
*fixed-removal* oxide planarisation that leaves a controlled thickness
of {term}`PSG` above the gate caps. On the second — the one the PDK's
0.2 µm nitride/oxide cap supports and this page follows — the polish
continues until it reaches the tops of the caps over the densest poly
arrays, using the {ref}`GATENIT <step-058>` nitride as a
{term}`CMP` stop in the same way the {ref}`ISONIT <step-003>`
nitride serves {ref}`CMPNIT <step-012>`, and the {term}`cap oxide` of the
next step ({ref}`NCAPOX <step-091>`) then re-buries the exposed caps.
The {ref}`POC <step-059>` and {ref}`IOX45 <step-063>` pages read the
cap as the polish stop; we adopt that reading here and mark it as an
inference. On it, the PDK's "Pre-LI ILD thickness" of 0.5 µm[^pdk-03]
is the cap-plus-cap-oxide-plus-residual-glass thickness between the
poly top and the {term}`local interconnect`, and the 0.4299 µm label that the stack diagram draws from the
field-poly top to the `li` bottom[^pdk-04] is the same interval drawn
not to scale.

## Step category

`CMPP` is a {ref}`Chemical-mechanical planarisation <category-cmp>`
step of the *oxide* type — the first of the inter-level polishes
({ref}`CMPL <step-106>`, {ref}`CMPM <step-116>` and the later
`CMPM*` steps are the others) and the only one whose stop, on our
reading, is a nitride cap rather than a fixed removal. The category
page compares the {term}`STI`, tungsten and oxide polishes; this instance
sits between the first two: it removes a doped oxide like an {term}`ILD`
polish, but it may land on nitride like the STI polish, with the same
{term}`dishing` and {term}`erosion` concerns.

## Why this step exists

Chemical-mechanical polishing entered the {term}`pre-metal dielectric` at
IBM at the end of the 1980s, when Davari et al. showed a planarisation
scheme combining reactive-ion etch-back with CMP[^davari-1989] and
Daubenspeck et al. characterised planarisation over variable pattern
densities;[^daubenspeck-1991] Kaanta et al. had already built a
tungsten-stud wiring scheme on a polished dielectric.[^kaanta-1987]
The reasons it is needed here:

* **Lithography depth of focus.** The contact mask
  ({ref}`LICM1 <step-093>`) prints 0.17 µm holes (licon.1[^pdk-periph])
  and, we infer, needs deep-UV exposure whose usable depth of focus
  is a few hundred nanometres (category page[^levinson-2005]) — less
  than the 0.4 µm step the un-polished glass would carry.
* **Uniform contact depth.** Every `licon1` must reach its landing
  surface — poly head, diffusion or tap — through the same oxide
  thickness, or the {term}`over-etch` on the shallow contacts damages their
  silicon while the deep ones are still closed. A polish whose depth
  is referenced to the gate caps makes the oxide over poly the same
  everywhere.
* **Local interconnect and metal 1 topography.** The
  titanium-nitride local interconnect ({ref}`LITIN <step-101>`) is
  only 0.1 µm thick;[^pdk-04] a film that thin cannot be patterned
  reliably over steps, and the {ref}`CMPL <step-106>` polish that
  follows it has less to do if the surface under it is already flat.

The cost is pattern-density sensitivity. The polish rate over a
region depends on the fraction of raised area under the pad, so wide
open field polishes faster than dense poly arrays; Stine et al.
modelled the effect[^stine-1998] and Ouma et al. reduced it to a
{term}`planarisation length` and {term}`pattern density`,[^ouma-2002] and the PDK's
pattern-density criteria — "Min pattern density for oxide" 0.75, the
FOM waffles and the 700 µm and 2000 µm density boxes[^pdk-03] — are
the design-rule expression of that sensitivity (the survey by Kahng
and Samadi covers fill synthesis[^kahng-2008]). If the polish does
land on the caps, nitride erosion over dense arrays and dishing of
the glass between them are the failure modes the STI polish page
describes, measured early by Yu et al.[^yu-1992]

Without `CMPP` the contact and local-interconnect lithography would
have to print over 0.4 µm steps and the contact etch would face a
different depth on every landing surface.

## How it is typically performed

An industry-generic oxide/{term}`PMD` polish for a 200 mm, 130 nm-era fab
(SKY130's recipe is not public):

1. **Tool.** Rotary multi-platen polisher with stacked polyurethane
   pads, diamond conditioner, carrier head with retaining ring and
   multi-zone membrane (category page; the Mirra
   architecture[^pat-cmp-mirra]).
2. **Slurry.** Fumed-silica in KOH or NH₄OH at pH 10–11, the
   classic oxide slurry, whose chemistry Cook set out for glass
   polishing[^cook-1990] and Krishnan, Nalaskowski and Cook
   review;[^rev-02] the removal rate follows the
   {term}`Preston equation` in pressure and velocity[^preston-1927] to a first
   approximation, with the departures Nanz and Camilletti
   review.[^nanz-1995] Doped glass polishes faster than undoped
   oxide, so the rate is calibrated on PSG monitors.
3. **Recipe.** A first platen removes the bulk at high rate; a second
   finishes to the target — either a timed removal or, on the
   cap-stop reading, a polish onto the nitride with a slurry whose
   oxide : nitride {term}`selectivity` is high enough to stop; a
   final platen buffs in DI water or dilute slurry. Down-force of a
   few psi and platen speeds of tens of rpm are typical.[^txt-05]
4. **Endpoint.** For a fixed removal, time plus post-polish
   thickness measurement (the "blind polishing" Wikipedia
   describes[^wiki-cmp]); for a stop-on-nitride, in-situ optical
   {term}`endpoint` through a pad window[^pat-cmp-window] or motor-current
   detection[^pat-cmp-endpoint-ibm] — Bibby and Holland review the
   options.[^bibby-1998]
5. **Post-CMP clean.** Double-sided brush scrub in dilute NH₄OH,
   spin-rinse-dry; a short dilute-HF touch is common before the next
   deposition. Slurry residue must be gone before the wafer dries.
6. **Metrology.** Remaining oxide over poly and over field on test
   pads by optical thickness mapping; step height and dishing by
   profilometry on density test structures; defect scan for
   scratches.

## Machines typically used

* **Rotary CMP polisher**, 200 mm: Applied Materials Mirra and Mirra
  Mesa,[^amat-1997][^chiphistory-mirra] Ebara F-REX,[^ebara-frex]
  SpeedFam-IPEC Avanti 472, Strasbaugh 6EC (category page).
* **Post-CMP brush scrubber** (OnTrak/Lam DSS-200, Applied Mesa
  integrated cleaner).
* **Optical film-thickness mapper**; **stylus profiler**;
  **unpatterned defect inspection**.

## Machines likely used at SkyWater

* **Applied Materials Mirra CMP.** SkyWater lists "AMAT Mirra CMP"
  for oxide, nitride, niobium, aluminium, tungsten, high-selectivity
  tungsten and copper.[^skw-01] Strength: **strong** for the tool
  and for an oxide/nitride polish capability; assignment to `CMPP`
  is an **inference** (the list names no steps).
* **Post-CMP cleaning.** SkyWater lists the "SEZ223, Davinci"
  single-wafer tools with HF and DSP+HF chemistries;[^skw-01] a
  brush scrubber is not named on any public page (open question).

## Resources required

* **Oxide slurry** — fumed or colloidal silica in KOH or NH₄OH
  (Cabot Semi-Sperse class; typical industry
  chemistry[^rev-02][^steigerwald-1997]); a nitride-selective
  (ceria or additive-silica) slurry if the polish stops on the caps.
* **Polishing pads** (IC1000/Suba IV class) and **diamond
  conditioners**; **carrier films, membranes and retaining
  rings**.[^steigerwald-1997]
* **DI water** in quantity; **dilute NH₄OH**, **dilute HF** for
  post-CMP cleaning; **PVA brushes**.
* **Monitor wafers** with blanket PSG and nitride for rate and
  selectivity checks.[^semi-m8]
* Chemical suppliers named by SkyWater: KMG Chemicals.[^sec-01]

## Related steps and cross-references

* Previous: {ref}`PSG <step-089>` (the film polished). Next:
  {ref}`NCAPOX <step-091>` (the cap oxide over the polished
  surface), then {ref}`RTAD2 <step-092>`.
* The stop, on our reading: {ref}`GATENIT <step-058>` and
  {ref}`POC <step-059>`; the "poly cap after SPE" left by
  {ref}`SPE <step-077>`.
* The STI polish with the same nitride-stop principle:
  {ref}`CMPNIT <step-012>`. Later oxide polishes:
  {ref}`CMPL <step-106>`, {ref}`CMPM <step-116>`.
* The lithography that needs the flat surface:
  {ref}`LICM1 <step-093>`.
* Category page: {ref}`Chemical-mechanical planarisation <category-cmp>`.

## References

### Cross-check

* SkyWater PDK, *Criteria & Assumptions* — "poly cap after SPE"
  0.2 µm; poly 0.18 µm; "Pre-LI ILD thickness" 0.5 µm; "Min pattern
  density for oxide" 0.75; pattern-density boxes.[^pdk-03]
* SkyWater PDK, process stack diagram — PSG labels; `li` 0.1 µm.[^pdk-04]
* SkyWater PDK, *Periphery rules* — licon.1 0.170 µm.[^pdk-periph]
* SkyWater, *Facilities & Capabilities* — "AMAT Mirra CMP" and its
  film list; SEZ/Da Vinci cleaners.[^skw-01]
* Applied Materials, 1997 Annual Report — the Mirra product
  line.[^amat-1997]
* SkyWater, Form S-1 — chemical suppliers.[^sec-01]

### High-level understanding

* Wikipedia, *Chemical-mechanical polishing*.[^wiki-cmp]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — dielectric
  CMP.[^txt-05]
* Steigerwald, Murarka and Gutmann, *Chemical Mechanical
  Planarization of Microelectronic Materials*.[^steigerwald-1997]
* Levinson, *Principles of Lithography* — depth of focus and why
  planarity matters.[^levinson-2005]
* Chip History Center, *The Mirra CMP System*.[^chiphistory-mirra]

### Deep dive

* Davari et al. (IBM), IEDM 1989 — RIE plus CMP planarisation of
  the inter-level dielectric.[^davari-1989]
* Daubenspeck et al. (IBM), *J. Electrochem. Soc.* 1991 —
  planarisation over variable pattern densities.[^daubenspeck-1991]
* Kaanta et al. (IBM), IEDM 1987 — tungsten studs on a planarised
  dielectric, the scheme this module follows.[^kaanta-1987]
* Preston, *J. Soc. Glass Technol.* 1927, and Nanz and Camilletti,
  *IEEE TSM* 1995 — the removal-rate law and a review of CMP
  models.[^preston-1927][^nanz-1995]
* Cook, *J. Non-Cryst. Solids* 1990 — the chemistry of glass
  polishing.[^cook-1990]
* Krishnan, Nalaskowski and Cook, *Chem. Rev.* 2010 — slurry
  chemistry for oxide and tungsten CMP.[^rev-02]
* Stine et al., *IEEE TSM* 1998, and Ouma et al., *IEEE TSM* 2002 —
  pattern-density models of oxide CMP.[^stine-1998][^ouma-2002]
* Yu et al., *Appl. Phys. Lett.* 1992 — dishing in a nitride-stop
  polish.[^yu-1992]
* Bibby and Holland, *J. Electron. Mater.* 1998 — endpoint detection
  for CMP.[^bibby-1998]
* Kahng and Samadi, *IEEE TCAD* 2008 — dummy-fill synthesis, the
  design-side answer to density sensitivity.[^kahng-2008]
* Chow et al. and Beyer et al. (IBM) — the foundational
  metal/insulator CMP patents.[^pat-cmp-ibm-1988][^pat-cmp-ibm-1990]
* Tolles et al., Birang et al. and Lustig et al. — multi-platen
  architecture, pad window and in-situ endpoint
  patents.[^pat-cmp-mirra][^pat-cmp-window][^pat-cmp-endpoint-ibm]
* Oliver (ed.), *Chemical-Mechanical Planarization of Semiconductor
  Materials* — dielectric CMP, endpoint and cleaning
  chapters.[^oliver-2004]

## Open questions

* Whether the polish stops on the gate caps or leaves a controlled
  glass thickness above them is not public; the cap-stop reading is
  our inference from the PDK's 0.2 µm cap entry.
* The slurry, removal amount, endpoint method and {term}`post-CMP clean` are
  not public.
* Whether SkyWater uses a brush scrubber, and which, is not stated on
  any public page.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram). <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
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
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
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
[^yu-1992]: C. Yu, P. C. Fazan, V. K. Mathews and T. T. Doan, "Dishing
    effects in a chemical mechanical polishing planarization process
    for advanced trench isolation", *Applied Physics Letters* **61**(11),
    1344–1346 (1992). <https://doi.org/10.1063/1.107586>
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
    US 4,944,836 A, granted 1990-07-31.
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
[^pat-cmp-endpoint-ibm]: N. E. Lustig, K. L. Saenger and H.-M. Tong
    (IBM), *In-situ endpoint detection and process monitoring method and
    apparatus for chemical-mechanical polishing*, US 5,433,651 A,
    granted 1995-07-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5433651>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
