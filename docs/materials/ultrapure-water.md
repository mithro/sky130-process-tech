(material-ultrapure-water)=
# Ultrapure water

Ultrapure water (UPW), deionised (DI) water in fab shorthand, is the
liquid a wafer fab uses most. It rinses every wet clean, etch and strip,
dilutes the acids and bases of the cleaning baths, carries slurry off
polished wafers and flushes their brushes, and rinses developer from
resist. Water that is merely clean for drinking would leave ions,
organics, silica, particles and bacteria on the silicon, so the fab makes
its own water by a chain of filtration, reverse osmosis, degassing,
ultraviolet treatment and ion exchange, and delivers it in a
recirculating loop to the tools. On the step pages' readings, 84 of
SKY130's 171 steps name DI or ultrapure water among their resources: the
wet cleans, etches and strips, the mask steps and the polishes. This page
describes the class in general, lists the standards and quality
parameters water is specified to, and then says what SkyWater has
published about water at its fab and which SKY130 steps name it. The
tools that use most of it are on the
{ref}`wet bench <machine-wet-bench>`,
{ref}`single-wafer spin processor <machine-single-wafer-spin-processor>`,
{ref}`coat-develop track <machine-coat-develop-track>`,
{ref}`CMP polisher <machine-cmp-polisher>` and
{ref}`post-CMP cleaner <machine-post-cmp-cleaner>` pages.

| | Ultrapure water |
|---|---|
| What they do | "UPW is used extensively in the production of semiconductor devices for all wet-processing steps (including wafer rinsing)".[^semi-f63] |
| Quality | UPW "is generally considered to be >18.1 megΩ resistivity and below 1 PPB in ionics (cations, anions, metals), total organic carbon, silica (dissolved and colloidal), particles, and bacteria";[^itrs-2001-yield] advanced UPW is specified at ">18.18 MΩ·cm" and dissolved oxygen "<10 μg/L".[^wiki-upw] |
| Production | Pretreatment, "multiple-pass reverse osmosis", vacuum or membrane degassing, UV, and polishing by "ion exchange beds or electrodeionization".[^wiki-upw] |
| Standards | SEMI F63 (quality) and SEMI F61 (system design);[^semi-f63][^semi-f61] ASTM D5127, whose water types "are defined with respect to device line width".[^astm-d5127] |
| Volumes | "advanced fabrication plants consuming several million gallons of UPW per day";[^wiki-upw] Ohmi's room-temperature clean cut chemical and ultrapure water use to "less than 1% and 5%, respectively".[^ohmi-1996] |
| SkyWater evidence | "Batch Rotational – EKS265, EKC270 solvents, CO2 injected DI"; otherwise water is not listed[^skw-01] |
| SKY130 steps | 84 steps; see {ref}`SKY130 steps that use this class <material-ultrapure-water-steps>` |

## What the class is and what it does

Water touches the wafer after almost every wet process, and what it
leaves behind stays there. The 2001 ITRS names the contaminants that
matter — "ionics (cations, anions, metals), total organic carbon, silica
(dissolved and colloidal), particles, and bacteria" — and notes that
"UPW quality, more than any other critical fluid, can change between"
the point of distribution, the point of connection at the back of the
tool and the point of use in the tool.[^itrs-2001-yield] Libman, Wilcox
and Zerfas list hydrogen peroxide "generated in Ultraviolet treatment"
and dissolved organics "either originating from incoming city water or
introduced by UPW system materials" among the trace contaminants that
threaten advanced manufacturing.[^libman-2015]

### Resistivity, ions and organics

Ions are tracked by resistivity: ASTM D1193 Type I reagent water is
18.2 MΩ·cm at 25 °C,[^wiki-purified-water] and advanced semiconductor UPW
is specified at ">18.18 MΩ·cm".[^wiki-upw] Organics are tracked as total
organic carbon (TOC), "measured by oxidizing organic molecules in the
water to CO2 and measuring the increase in the CO2
concentration";[^wiki-upw] the 2001 ITRS yield table lists "Total oxidizable
carbon" at 1 ppb, falling to below 1 ppb in later
years.[^itrs-2001-yield]

### Dissolved oxygen and native oxide

Oxygen dissolved in rinse water oxidises a freshly etched silicon
surface. Morita et al. found that "The coexistence of oxygen and water or
moisture is required for growth of native oxide both in air and in
ultrapure water at room temperature";[^morita-1990] Li, Balazs and
Anderson showed that "the ambient and the dissolved oxygen concentration
in UPW dramatically affect the growth rate of the native
oxide";[^li-2005] and Yagi et al. built UPW systems with membrane
degassing and catalytic reduction or nitrogen bubbling that supply "10
ppb or less in dissolved oxygen concentration".[^yagi-1992] The ITRS
records that "Some semiconductor manufactures now treat dissolved oxygen
(DO) in this way", as a process variable rather than a
contaminant.[^itrs-2001-yield]

### Particles and filtration

Particles in the final rinse land on the wafer. Gaudet described
point-of-use ultrafiltration of DI rinse water against "colloidal
particles of 0.2 micron and smaller";[^gaudet-1984] the 2001 ITRS notes
that particle counters "are capable of measuring only to 50nm for
UPW";[^itrs-2001-yield] and Nakata, Fukui and Nagai studied particle
adsorption onto silicon in UPW and the effect of carbon
dioxide.[^nakata-2016]

### Carbon dioxide in rinse water

Ultrapure water is highly resistive. An MKS patent that may still be in
force dissolves carbon dioxide in it for cleaning fragile devices, and
says what that does to the water; its wording is in the collapsed note
below. SkyWater lists "CO2 injected DI" on its batch rotational solvent
tool (see *At SkyWater*).[^skw-01]

:::{dropdown} From a patent shown as in force (EP 2 104 648; estimated expiry 2028-05-14) — open to read
An MKS patent dissolves carbon dioxide in ultrapure water for cleaning
fragile devices: "The dissolved CO2 reduces the resistivity of the DI
water to a level that prevents surface charging".[^pat-dico2-mks]
:::

## Representative materials and grades

Ultrapure water is made on site, not bought, so its "grade" is the
specification the fab sets for its UPW system, usually framed by the
standards below. SKY130's water specification is not public.

* **SEMI F63** (F63-1224, current) — a guide that may be used "To
  establish quality expectations for the supplied UPW" and "To set the
  process control parameters for UPW-system operation", written for
  facilities making semiconductors "with line widths of 32 nm and
  smaller", a scope far below 130 nm, and developed with input from the IRDS UPW
  committee.[^semi-f63]
* **SEMI F61** (F61-0521, current) — "the engineering and component
  requirements for a UPW system used in semiconductor manufacturing",
  including hot UPW.[^semi-f61]
* **ASTM D5127** (D5127-13, reapproved 2018) — recommends "the water
  quality required for the electronics and microelectronics industries";
  "The types of ultra-pure water are defined with respect to device line
  width", and the recommendations "apply at the point of
  distribution".[^astm-d5127]
* **ITRS 2001 yield tables** — TOC, bacteria, total silica, particles
  and critical ions and metals for UPW, measured at the point of
  distribution or connection by the methods of its figure 56 (online
  resistivity cells, TOC by resistivity or CO₂, ICP-MS, ion chromatography
  and light scattering).[^itrs-2001-yield]
* **Carbonated DI water** — CO₂-dissolved water for rinsing where charging
  matters; the patent describing it may still be in force, and is in the
  collapsed note below this list.

:::{dropdown} From a patent shown as in force (EP 2 104 648; estimated expiry 2028-05-14) — open to read
Carbonated DI water is the subject of an MKS patent.[^pat-dico2-mks]
:::

## At SkyWater

### What SkyWater's filings and pages list

SkyWater's *Facilities & Capabilities* page mentions water once, under
"Resist removal/cleans":[^skw-01]

> "Batch Rotational – EKS265, EKC270 solvents, CO2 injected DI"

Read term by term, the batch rotational tool rinses with DI water into
which carbon dioxide is injected, which we read as carbonated rinse water
of the kind the MKS patent describes (that patent may still be in force;
it is cited in the collapsed notes above and below); SkyWater does not
explain it. The page describes no UPW plant, water quality or water use,
and no other tool entry mentions water.[^skw-01] SkyWater's filings list
no water supplier among raw materials.[^sec-01][^sec-02] The S-1's
mention of "an advanced water treatment facility" concerns the Center
for NeoVation in Osceola County, Florida, which SkyWater agreed to
operate, not the Minnesota fab.[^sec-01] The S-1 also states that "We
use, generate and discharge hazardous chemicals and waste" and that its
facilities are ISO 14001 certified.[^sec-01]

### Strength of the evidence

The "CO2 injected DI" entry is a SkyWater statement and ranks as
**strong** evidence that carbonated DI water is used on one solvent tool,
on the scale of the {ref}`machines index <machines-reading-evidence>`;
it says nothing of the rest of the fab's water.[^skw-01] That SkyWater
makes and uses ultrapure water on its wet, lithography and CMP tools is
industry practice for any fab of the class, not a SkyWater statement,
and no public source gives SkyWater's water specification, system or
consumption.

(material-ultrapure-water-steps)=
### SKY130 steps that use this class

This page covers the rows of the {ref}`materials index <materials-table>`
listed below by key; the steps are those whose *Resources required* section
names one of them (the union of the rows' *Steps* cells).

Materials index rows covered:

* `upw` — ultrapure (DI) water

Steps:

{ref}`SMAT <step-001>`, {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`DNIS <step-009>`, {ref}`CMPNIT <step-012>`, {ref}`NS19 <step-013>`, {ref}`LVTNM <step-014>`, {ref}`LVTNIS <step-016>`, {ref}`NWM <step-017>`, {ref}`LVTPIS <step-021>`, {ref}`HVTPM <step-022>`, {ref}`PCHIS <step-025>`, {ref}`PWBM <step-026>`, {ref}`PWIS <step-029>`, {ref}`PWDEM <step-030>`, {ref}`PWDEIS <step-033>`, {ref}`TUNM <step-035>`, {ref}`TUNME <step-039>`, {ref}`ONOM <step-041>`, {ref}`ONOME <step-042>`, {ref}`LVOM <step-044>`, {ref}`GOXETCH <step-046>`, {ref}`RPM <step-049>`, {ref}`P1IS <step-051>`, {ref}`RRPM <step-052>`, {ref}`PRIS <step-054>`, {ref}`URPM <step-055>`, {ref}`UPRIS <step-057>`, {ref}`BFR <step-060>`, {ref}`P1M <step-061>`, {ref}`NTM <step-064>`, {ref}`ASTIS <step-067>`, {ref}`HVNTM <step-068>`, {ref}`HVASTIS <step-070>`, {ref}`LDNTM <step-071>`, {ref}`LDASTIS <step-074>`, {ref}`SPE <step-077>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`PDIS <step-084>`, {ref}`NSDM <step-085>`, {ref}`NSDIS <step-087>`, {ref}`CMPP <step-090>`, {ref}`LICM1 <step-093>`, {ref}`SACETCH <step-095>`, {ref}`WCMPLI <step-100>`, {ref}`LI1M <step-102>`, {ref}`CMPL <step-106>`, {ref}`CTM1 <step-107>`, {ref}`CTME <step-108>`, {ref}`WCMP2 <step-111>`, {ref}`MM1 <step-113>`, {ref}`MM1E <step-114>`, {ref}`CMPM <step-116>`, {ref}`VIM <step-118>`, {ref}`VIME <step-119>`, {ref}`WCMP3 <step-122>`, {ref}`MM2 <step-124>`, {ref}`MM2E <step-125>`, {ref}`CMPM2 <step-127>`, {ref}`VIM2 <step-129>`, {ref}`VIM2E <step-130>`, {ref}`WCMP4 <step-133>`, {ref}`CAPM <step-137>`, {ref}`CAPME <step-138>`, {ref}`MM3 <step-139>`, {ref}`MM3E <step-140>`, {ref}`CMPM3 <step-142>`, {ref}`VIM3 <step-144>`, {ref}`VIM3E <step-145>`, {ref}`WCMP5 <step-148>`, {ref}`CAP2M <step-152>`, {ref}`CAP2ME <step-153>`, {ref}`MM4 <step-154>`, {ref}`MM4E <step-155>`, {ref}`CMPM4 <step-157>`, {ref}`VIM4 <step-159>`, {ref}`VIM4E <step-160>`, {ref}`MM5 <step-162>`, {ref}`MM5E <step-163>`, {ref}`NSM <step-165>`, {ref}`NSME <step-166>`, {ref}`PDM <step-168>`, {ref}`PDME <step-169>`

The steps fall into groups, as the step pages' *Resources required*
sections describe them:

* **Wet cleans, etches and strips** — the pre-furnace clean at
  {ref}`SMAT <step-001>`, the implant strips, the nitride strip at
  {ref}`NS19 <step-013>`, the tunnel-window and gate-oxide etches, the
  backside film removal at {ref}`BFR <step-060>` and the post-etch cleans
  of the back end.
* **Mask steps** — the resist coat, develop and rinse of the mask steps,
  where the pages name DI water with the developer and rinse solvents.
* **Polishes** — the twelve CMP steps, where all the pages name DI water
  for the polish and post-CMP clean and four say "in quantity" or "in
  large volumes".

Most furnace, implant, deposition, anneal and test steps name no water;
their resources are gases, targets and hardware.

## Supply, handling, safety and facilities

None of the SkyWater sources cited here describes the fab's UPW plant,
distribution or waste water; the points below are industry practice or
standards and literature statements.

* **Production.** Pretreatment by coagulation, filtration and softening;
  primary treatment by reverse osmosis and degassing; polishing by UV and
  ion exchange or electrodeionization.[^wiki-upw] SEMI F61 covers the
  design and operation of such systems.[^semi-f61]
* **Distribution and monitoring.** Water is monitored online for
  resistivity, TOC, dissolved oxygen and particles and in the laboratory
  for bacteria, silica, ions and metals;[^itrs-2001-yield] quality can
  change between the point of distribution and the point of
  use.[^itrs-2001-yield]
* **Point-of-use treatment.** Final filters at the tool, as Gaudet
  described for rinse water,[^gaudet-1984] and CO₂ injection where rinse
  charging matters[^skw-01] (the MKS patent, which may still be in force,
  is in the collapsed note below this list).
* **Conservation and reclaim.** "A well-implemented recycle program can
  actually improve final water quality by using a cleaner stream for the
  feed".[^itrs-2001-yield] Cartwright described a semiconductor plant
  where "over 90% of the rinse water is purified back to 18 megohm/cm
  quality for reuse" (sic, for megohm·cm);[^cartwright-1985] Ohmi's clean
  reduced chemical and ultrapure water use to "less than 1% and 5%,
  respectively".[^ohmi-1996] Tool makers promote lower DI water use per
  wafer.[^screen-ss3200]
* **Waste water.** Rinse water carries acids, fluoride, solvent and
  slurry to waste treatment; CMP is among the largest water users (the
  CMP step pages' reading of Quirk and Serda).[^txt-07]

:::{dropdown} From a patent shown as in force (EP 2 104 648; estimated expiry 2028-05-14) — open to read
CO₂ injection at the point of use is the subject of an MKS
patent.[^pat-dico2-mks]
:::

## Process-integration notes for SKY130

These notes connect the class to the step pages; they add no SKY130
conditions of their own. SKY130's water specification is not public.

* **HF-last rinses and native oxide.** On their pages' readings, the
  pre-gate cleans at {ref}`GOXETCH <step-046>` and
  {ref}`TUNME <step-039>` end on silicon
  that rinse water can re-oxidise; native oxide grows in ultrapure water
  when oxygen is present,[^morita-1990][^li-2005] so dissolved oxygen in
  the final rinse bears on the gate oxides that follow (our reading).
* **Rinse charging on the back end.** The post-etch solvent cleans of the
  contact, via and metal etches rinse wafers carrying isolated metal and
  thin dielectrics; SkyWater's "CO2 injected DI" on its solvent tool
  matches the use of carbonated water against surface charging[^skw-01]
  (the MKS patent, which may still be in force, is in the collapsed note
  below this list).
* **Developer rinse.** The mask-step pages name DI water beside the TMAH
  developer and rinse solvents; rinsing the developer off with water is
  industry practice ({ref}`material-lithography-materials`).
* **Slurry must not dry.** The CMP pages name DI water for the polish and
  the brush clean, four of them in quantity or in large volumes, which keep the wafer wet until the
  slurry is removed ({ref}`material-cmp-consumables`).[^pat-scrubber-ontrak]
* **Water in the baths.** The RCA cleans, SPM and dilute HF of the wet
  chemicals class are made up with DI water to their working
  concentrations ({ref}`material-wet-chemicals`).[^wiki-rca]

:::{dropdown} From a patent shown as in force (EP 2 104 648; estimated expiry 2028-05-14) — open to read
The carbonated water used against surface charging is the subject of an
MKS patent.[^pat-dico2-mks]
:::

## Related pages

* {ref}`machine-wet-bench` and {ref}`machine-single-wafer-spin-processor` —
  rinses, carbonated DI water and drying.
* {ref}`machine-coat-develop-track` — the develop rinse.
* {ref}`machine-cmp-polisher` and {ref}`machine-post-cmp-cleaner` — water
  for polishing and brush cleaning.
* {ref}`material-wet-chemicals` — the chemicals water dilutes and rinses
  away.
* {ref}`material-cmp-consumables` — slurries and post-CMP cleans.
* {ref}`materials-index` — all consumable classes.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

* {ref}`Double-sided wafer scrubber with a wet submersing silicon wafer indexer <patent-gp25529547>` — US 5,442,828 A (1992)

:::{dropdown} 1 family in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`EP 2 104 648 B1 <patent-gp39203155>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater Technology, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the "CO2 injected DI"
  entry.[^skw-01]
* SkyWater Technology, Form S-1 (2021) and Form 10-K for fiscal 2023 —
  raw materials, the Florida water treatment facility and environmental
  statements.[^sec-01][^sec-02]
* SEMI F63 and SEMI F61 — UPW quality and system
  guides.[^semi-f63][^semi-f61]
* [ASTM D5127](<https://www.astm.org/d5127-13r18.html>) — ultrapure water for the electronics and semiconductor
  industries.[^astm-d5127]
* [ITRS 2001, *Yield Enhancement*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001YieldEnhance.pdf>) — UPW definition, requirements, test
  methods and recycling.[^itrs-2001-yield]

:::{dropdown} From a patent shown as in force (EP 2 104 648; estimated expiry 2028-05-14) — open to read
* Gottschalk et al. (MKS), EP 2 104 648 — carbonated DI water against
  surface charging.[^pat-dico2-mks]
:::

### High-level understanding

* Wikipedia, [*Ultrapure water*](<https://en.wikipedia.org/wiki/Ultrapure_water>) and [*Purified water*](<https://en.wikipedia.org/wiki/Purified_water>) — production,
  specifications and analytical methods.[^wiki-upw][^wiki-purified-water]
* [Quirk and Serda, *Semiconductor Manufacturing Technology*](<https://openlibrary.org/isbn/9780130815200>) — water on the
  fab floor.[^txt-07]
* [Kern, *JES* 1990](<https://doi.org/10.1149/1.2086825>) — the wet cleaning that water rinses.[^kern-1990]
* [SCREEN, SS-3200 release](<https://www.screen.co.jp/spe/en/information/spe241106>) — DI water use per wafer in a 200 mm
  scrubber.[^screen-ss3200]
* [Wikipedia, *RCA clean*](<https://en.wikipedia.org/wiki/RCA_clean>) — water in the peroxide cleans.[^wiki-rca]

### Deep dive

* [Morita et al., *JAP* 1990](<https://doi.org/10.1063/1.347181>) — native-oxide growth in air and ultrapure
  water.[^morita-1990]
* [Li, Balazs and Anderson, *JES* 2005](<https://doi.org/10.1149/1.1946487>) — dissolved oxygen in UPW and
  initial native-oxide growth.[^li-2005]
* [Yagi et al., *IEEE TSM* 1992](<https://doi.org/10.1109/66.136273>) — low-dissolved-oxygen UPW
  systems.[^yagi-1992]
* [Ohmi, *JES* 1996](<https://doi.org/10.1149/1.1837133>) — a room-temperature clean with less water.[^ohmi-1996]
* [Gaudet, ASTM *Semiconductor Processing* 1984](<https://doi.org/10.1520/STP32652S>) — point-of-use ultrafiltration of rinse
  water.[^gaudet-1984]
* [Cartwright, *Water Sci. Technol.* 1985](<https://doi.org/10.2166/wst.1985.0141>) — rinse-water reclamation in a
  semiconductor plant.[^cartwright-1985]
* [Libman, Wilcox and Zerfas, *ECS Trans.* 2015](<https://doi.org/10.1149/06908.0017ecst>) — UPW challenges for
  advanced manufacturing.[^libman-2015]
* [Nakata, Fukui and Nagai, ISSM 2016](<https://doi.org/10.1109/ISSM.2016.7934544>) — particle adsorption onto silicon in
  UPW.[^nakata-2016]
* [Leenaars, Huethorst and van Oekel, *Langmuir* 1990](<https://doi.org/10.1021/la00101a014>) — Marangoni drying
  after the rinse.[^leenaars-1990]
* [Busnaina, Kashkoush and Gale, *JES* 1995](<https://doi.org/10.1149/1.2050096>) — megasonic cleaning in DI
  water and SC-1.[^busnaina-1995]
* [Lutz (OnTrak), US 5,442,828](<https://patents.google.com/patent/US5442828A/en>) — water-flushed brushes and a wet
  indexer.[^pat-scrubber-ontrak]
* [SEMI F63](<https://store-us.semi.org/products/f06300-semi-f63-guide-for-ultrapure-water-used-in-semiconductor-processing>) — the UPW quality guide, with its IRDS basis.[^semi-f63]

## Open questions

* SkyWater's UPW system, water specification, consumption and reclaim are
  not described in any public source.[^skw-01][^sec-01]
* What "CO2 injected DI" is used for, and whether carbonated water is used
  on other tools, is not stated.[^skw-01]
* Whether SKY130's pre-gate rinses use degassed water is not public.

<!-- footnotes -->

[^semi-f63]: SEMI, *SEMI F63 — Guide for Ultrapure Water Used in
    Semiconductor Processing*, SEMI Standards store listing (revision
    F63-1224, current), accessed 2026-09-13.
    <https://store-us.semi.org/products/f06300-semi-f63-guide-for-ultrapure-water-used-in-semiconductor-processing>
[^itrs-2001-yield]: International Technology Roadmap for
    Semiconductors, *2001 Edition: Yield Enhancement*, "Ultrapure Water"
    and figure 56.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001YieldEnhance.pdf>
[^wiki-upw]: Wikipedia, *Ultrapure water*.
    <https://en.wikipedia.org/wiki/Ultrapure_water>
[^semi-f61]: SEMI, *SEMI F61 — Guide to Design and Operation of a
    Semiconductor Ultrapure Water System*, SEMI Standards store listing
    (revision F61-0521, current), accessed 2026-09-13.
    <https://store-us.semi.org/products/f06100-semi-f61-guide-to-design-and-operation-of-a-semiconductor-ultrapure-water-system>
[^astm-d5127]: ASTM International, *D5127-13(2018) Standard Guide for
    Ultra-Pure Water Used in the Electronics and Semiconductor
    Industries* (active), catalogue page; read from the Wayback Machine
    capture of 2024-09-17.
    <https://www.astm.org/d5127-13r18.html>
    <https://web.archive.org/web/20240917021043/https://www.astm.org/d5127-13r18.html>
[^ohmi-1996]: T. Ohmi, "Total Room Temperature Wet Cleaning for Si
    Substrate Surface", *Journal of The Electrochemical Society*
    **143**(9), 2957–2964 (1996). <https://doi.org/10.1149/1.1837133>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; resist-removal entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^libman-2015]: S. Libman, D. Wilcox and B. Zerfas, "Ultrapure Water for
    Advance Semiconductor Manufacturing: Challenges and Opportunities",
    *ECS Transactions* **69**(8), 17–28 (2015).
    <https://doi.org/10.1149/06908.0017ecst>
[^wiki-purified-water]: Wikipedia, *Purified water* (table of water
    quality standards).
    <https://en.wikipedia.org/wiki/Purified_water>
[^morita-1990]: M. Morita, T. Ohmi, E. Hasegawa, M. Kawakami and
    M. Ohwada, "Growth of native oxide on a silicon surface", *Journal
    of Applied Physics* **68**(3), 1272–1281 (1990).
    <https://doi.org/10.1063/1.347181>
[^li-2005]: F. Li, M. K. Balazs and S. Anderson, "Effects of Ambient and
    Dissolved Oxygen Concentration in Ultrapure Water on Initial Growth
    of Native Oxide on a Silicon (100) Surface", *Journal of The
    Electrochemical Society* **152**(8), G669 (2005).
    <https://doi.org/10.1149/1.1946487>
[^yagi-1992]: Y. Yagi, T. Imaoka, Y. Kasama and T. Ohmi, "Advanced
    ultrapure water systems with low dissolved oxygen for native oxide
    free wafer processing", *IEEE Transactions on Semiconductor
    Manufacturing* **5**(2), 121–127 (1992).
    <https://doi.org/10.1109/66.136273>
[^gaudet-1984]: P. W. Gaudet, "Point-Of-Use Ultrafiltration of Deionized
    Rinse Water and Effects on Microelectronics Device Quality", in
    *Semiconductor Processing*, ASTM International, 1984,
    ISBN 978-0-8031-0403-7, pp. 184–197. <https://doi.org/10.1520/STP32652S>
[^nakata-2016]: K. Nakata, T. Fukui and T. Nagai, "Particle adsorption
    onto Si wafers in ultrapure water; its mechanism and effect of carbon
    dioxide", *2016 International Symposium on Semiconductor
    Manufacturing (ISSM)*, pp. 1–4.
    <https://doi.org/10.1109/ISSM.2016.7934544>
[^pat-dico2-mks]: C. Gottschalk, U. Brammer, J. Lohr and J. Seiwert (MKS
    Instruments), *System and method for carbonation of deionized
    water*, EP 2 104 648 B1, granted 2013-04-17.
    <https://patents.google.com/patent/EP2104648B1/en>
    Shown as in force; estimated expiry 2028-05-14 (estimate from public
    records, not legal advice).
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; the corporate-structure and lease
    passages on the Florida Center for NeoVation, the "Raw materials."
    run-in paragraph and "Environmental, Safety and Quality Matters";
    read from a Wayback Machine copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; "Raw materials" paragraph; read from a Wayback Machine
    copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^cartwright-1985]: P. S. Cartwright, "Total Effluent Treatment and Rinse
    Water Reclamation in a Semiconductor Device Manufacturing Facility",
    *Water Science and Technology* **17**(2–3), 325–336 (1985).
    <https://doi.org/10.2166/wst.1985.0141>
[^screen-ss3200]: SCREEN Semiconductor Solutions, *Launch of 200mm Wafer
    Cleaning System — New SS-3200 for 200mm expands SCREEN SPE's
    world-leading spin scrubber lineup*, news release, 2024-11-06,
    accessed 2026-09-13.
    <https://www.screen.co.jp/spe/en/information/spe241106>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^pat-scrubber-ontrak]: R. A. Lutz (OnTrak Systems), *Double-sided wafer
    scrubber with a wet submersing silicon wafer indexer*, US 5,442,828 A,
    filed 1992-11-30, granted 1995-08-22.
    <https://patents.google.com/patent/US5442828A/en>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^leenaars-1990]: A. F. M. Leenaars, J. A. M. Huethorst and J. J. van
    Oekel, "Marangoni drying: A new extremely clean drying process",
    *Langmuir* **6**(11), 1701–1703 (1990).
    <https://doi.org/10.1021/la00101a014>
[^busnaina-1995]: A. A. Busnaina, I. I. Kashkoush and G. W. Gale, "An
    Experimental Study of Megasonic Cleaning of Silicon Wafers", *Journal
    of The Electrochemical Society* **142**(8), 2812–2817 (1995).
    <https://doi.org/10.1149/1.2050096>
