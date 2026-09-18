(material-substrates)=
# Substrates and test wafers

A fab buys its silicon. The wafers that become products arrive from a
wafer maker as polished discs cut from a single crystal, made to a
written specification of diameter, thickness, doping, orientation and
surface quality; the wafers that carry no product — monitor, test,
filler and reference wafers — arrive by the same route, made to looser
specifications or reclaimed from earlier use. On the step pages'
readings, SKY130 starts on a 200 mm, p-type, polished bulk wafer, and
most of its process steps consume test wafers of one kind or another
for thickness, sheet-resistance, particle, rate and calibration checks.
This page describes the class in general, lists representative wafer
grades and the standards they are ordered to, and then says what
SkyWater has published about its wafers and which SKY130 steps name
them. The wafer specification and crystal physics are on the
{ref}`substrate category page <category-substrate>`, and the incoming
inspection, marking and sorting tools on the
{ref}`starting-material machine page <machine-starting-material>`.

| | Substrates and test wafers |
|---|---|
| What they do | Prime wafers carry the product; SEMI M1 exists because "To permit common processing equipment to be used in multiple device fabrication lines, it is essential for the wafer dimensions to be standardized".[^semi-m1] Test and monitor wafers serve "testing and controlling semiconductor fabrication lines and processes".[^gw-products] |
| Prime wafers | Czochralski silicon; 200 mm wafers are "725 μm" thick and "use a single small notch to convey wafer orientation";[^wiki-wafer] polished-wafer resistivities for CMOS have ranged up to "around 30 ohm-cm".[^gw-products] |
| Test wafers | SEMI M8 "covers dimensional and crystallographic properties of monocrystalline virgin silicon test wafers";[^semi-m8] SEMI M24 premium wafers for "particle counting, metal contamination monitoring, and measuring pattern resolution";[^semi-m24] SEMI M38 reclaimed wafers.[^semi-m38] |
| Cost and reuse | Manufacturers "spend millions of dollars annually on the purchase of test wafers"; many "use reclaim to polish off the top surface of the test wafer".[^popovich-1997] |
| SkyWater evidence | "200 mm equipment";[^skw-01] S130 "200mm" and "Bulk";[^skw-02] "silicon wafers" among raw materials, with GlobalWafers and SEH America as suppliers[^sec-01][^sec-02] |
| SKY130 steps | 106 steps; see {ref}`SKY130 steps that use this class <material-substrates-steps>` |

## What the class is and what it does

The wafer is the one material that every step acts on. It is bought, not
made: the crystal is grown, sliced, lapped, etched and polished at the
wafer maker, and what the fab controls is the order it places and the
inspection it runs on receipt ({ref}`category-substrate`,
{ref}`machine-starting-material`). The SEMI M1 specification explains
why the order is standardised: "Single crystal silicon wafers are
utilized for essentially all integrated circuits", and as dimensions
shrink "it has become of interest to standardize additional properties
of the wafers"; its scope is "ordering information and certain
requirements for high-purity (electronic grade), single crystal polished
silicon wafers".[^semi-m1] Kao and Chung's textbook describes the
shaping of the wafer from ingot to polished surface.[^kao-2021]

### Prime wafers

Nearly all CMOS wafers are Czochralski (CZ) silicon; Zulehner reviewed
the growth from the wafer maker's side[^zulehner-1983] and Shimura's
monograph covers the crystal, its oxygen and its
defects.[^shimura-1989] The 200 mm wafer, introduced in 1992, is
"725 μm" thick, and "Wafers of 200 mm diameter and above use a single
small notch to convey wafer orientation, with no visual indication of
doping type".[^wiki-wafer] Two properties of the crystal matter to the
process beyond its doping. Oxygen from the crucible precipitates during
the hot steps.[^borghesi-1995] A MEMC patent's background states that
precipitates in the bulk "are capable of trapping undesired metal
impurities", which it calls "internal or intrinsic gettering", and the
patent describes wafers whose precipitation behaviour is set by a rapid
thermal treatment at the wafer maker;[^pat-mdz-memc] GlobalWafers, which
acquired SunEdison Semiconductor in 2016,[^wiki-gw] offers a "Starting
polished wafer with built-in denuding and nucleation that does not rely
on long thermal treatments in the IC fab process".[^gw-products] And
voids from crystal growth open as pits: Ryuta et al. showed that SC-1
cleaning reveals "crystal-originated singularities" that laser counters
see as particles, presuming their origin to be "some kind of defect in
the melt-grown crystals";[^ryuta-1990] Miyazaki et al. concluded that
the original COP in a crystal is "an octahedral void";[^miyazaki-1997]
and Ishii et al. found that pair pits of this kind caused gate-oxide
failure at oxide thicknesses around 10 nm.[^ishii-1996] Falster and
Voronkov describe how growth conditions
control these point defects.[^falster-2000]

### Epitaxial and other substrates

The alternative to a polished wafer for logic was a lightly doped
epitaxial layer on a heavily doped substrate; SEMI M62 specifies
epitaxial wafers.[^semi-m62] The 2001 ITRS contrasts "lower cost Cz
polished wafers" with "more costly epitaxial wafers" and adds that the
latch-up advantage of epi "may no longer be as critical due to the
implementation of shallow trench isolation (STI)".[^itrs-01] One wafer
maker notes that CMOS substrate resistivities "have typically spanned
from a low of about 5 mohm-cm on heavily doped epi substrates to a high
of around 30 ohm-cm on polished wafers".[^gw-products]

### Test, monitor, filler and reference wafers

A fab runs far more wafers than it sells. Monitor wafers go through a
step beside or instead of product to give a measurement the patterned
product cannot: film thickness on a blanket film, sheet resistance of an
implant into bare silicon, particles added by a tool, an etch rate or a
selectivity. GlobalWafers states that "Although monitor wafers are
substantially the same as prime polished wafers with respect to
cleanliness, and in some cases flatness, other specifications are
generally less rigorous".[^gw-products] SEMI M8 covers "virgin test
wafers in all standard wafer diameters", in "two classes of larger
diameter test wafers (from 150 mm)", but "does not cover test wafers
intended for applications placing higher demands on silicon wafers, such
as particle counting, measuring resolution in a photolithography
process, or monitoring metallic contamination", for which it refers to
SEMI M24.[^semi-m8] Batch furnaces also take filler (dummy) wafers at
the ends of the load: one vertical reactor holds "150 product, test, and
filler wafers",[^expertech-vtr] and a silicon-carbide supplier notes that
"It is still common for silicon dummy wafers to be made from reclaimed
Si material".[^entegris-supersic] Some test wafers are instruments:
Chen et al. used "test wafers instrumented with thin-film thermocouples"
to study temperature measurement in a 200 mm rapid thermal
chamber.[^chen-2002-rtp]

Test wafers are managed as a stock. Popovich, Chilton and Kilgore
described Motorola's tracking system for test wafers that "are used to
qualify tools, monitor processes, and develop new process techniques",
reused internally before reclaim;[^popovich-1997] Ozelkan and
Cakanyildirim modelled the purchase, downgrading and holding of test
wafers, whose "yearly TW costs add up to several million dollars for a
typical semiconductor fab";[^ozelkan-2006] and Watanabe et al. reported
that a DRAM fab cut "the ratio of monitor wafer to wafer start" from
"1.5 (1993) to 0.5 (1999)" by reclaim, recycling and fewer
measurements.[^watanabe-1999]

## Representative materials and grades

Wafers are ordered to a specification agreed with the wafer maker, which
the SEMI standards frame; the grades below are the standards and current
supplier statements. The supplier statements describe the suppliers'
catalogues, not the wafers SkyWater buys, although both suppliers are
named in SkyWater's filings (see *At SkyWater*).

* **Prime polished wafers.** SEMI M1 (current revision M1-0924) gives
  "Standardized dimensional requirements" for "a large number of
  categories of standardized polished wafers".[^semi-m1] SEH America
  states that its polished wafers "can be produced in orientations
  <100>, <111>, and <110>" with boron or phosphorus for all diameters,
  and that its 200 mm range includes "standard CZ polished wafers, COP
  free polished wafers, epi wafers of all types, argon annealed
  wafers".[^seh-products] GlobalWafers calls its principal product "the
  prime polished wafer".[^gw-products]
* **Annealed and gettering wafers.** Argon-annealed wafers with a
  "COP-free surface zone" and an oxygen-denuded zone;[^gw-products]
  SEH uses "nitrogen doping in the CZ crystal and optimized annealing
  recipes".[^seh-products]
* **Epitaxial wafers.** "P/P-, P/P+, N/N-, and N/N+ wafers" in SEH's
  list;[^seh-products] SEMI M62.[^semi-m62]
* **Virgin test wafers.** SEMI M8 (M8-0312, reapproved 1023, current),
  with classes by diameter;[^semi-m8] GlobalWafers' "Test and Monitor
  Wafers".[^gw-products]
* **Premium wafers.** SEMI M24 (M24-0612, inactive) for particle
  counting, metal contamination and lithography resolution, with
  "tighter specification values in some specific items for the specific
  usage".[^semi-m24]
* **Reclaimed wafers.** SEMI M38 (M38-0312, reapproved 1023, current)
  "divides reclaimed wafers into four application categories:
  Mechanical, Furnace, Particle, and Lithography" and includes
  requirements for "devices in the 180 and 130 nm technology
  generations".[^semi-m38]
* **Non-silicon dummy wafers.** Silicon-carbide dummy and baffle wafers
  for furnaces, which "can be cleaned and reused indefinitely in LPCVD
  or diffusion processes", including a 200 mm size of "0.724 mm"
  thickness.[^entegris-supersic]

## At SkyWater

### What SkyWater's filings and pages list

SkyWater's *Facilities & Capabilities* page describes the Minnesota fab
as having "200 mm equipment" and, under "Other Services", lists "High
resistivity, red phos low resistivity and Silison on Insulator
processing" (sic).[^skw-01] Its CMOS platform table gives the S130
platform a "200mm" wafer size and "Bulk" substrates, against "4 µm EPI"
for S90LN and "FD SOI" for RH90.[^skw-02] Neither page gives a
resistivity, orientation, oxygen specification or wafer grade, and
neither mentions test, monitor or reclaimed wafers.

Both of SkyWater's filings list "silicon wafers" first among the raw
materials, and name wafer suppliers:[^sec-01][^sec-02]

| Filing | Silicon-wafer suppliers as named |
|--------|----------------------------------|
| S-1 (2021)[^sec-01] | "GlobalWafers Singapore Pte. Ltd. (silicon wafers)"; "SEH America, subsidiary of Shin-Etsu Handotai, Ltd. (silicon wafers)" |
| 10-K for fiscal 2023[^sec-02] | "Globalwafers Co. LTD."; "SEH America Inc, subsidiary of Shin-Etsu Handotai, Ltd." |

Neither filing names a wafer type, grade or diameter, or says whether
the suppliers provide prime, test or reclaimed wafers. The S-1's risk
factors add that "The raw materials used to manufacture our products are
subject to availability constraints and price volatility".[^sec-01] For
the fab's history, the S-1 states that before independent operations
"our fab was owned and operated by Cypress Semiconductor Corporation, or
Cypress, as a captive manufacturing facility for 20 years".[^sec-01]
Cypress's 2015 notice PIN152804 qualified "GlobalWafer Silicon Wafers"
for "130nm C8/R8/S8/L8" products at Fab 4, to be used "in addition to
wafers from other qualified suppliers".[^cyp-06] The PDK labels the
bottom of the process stack "p-substrate",[^pdk-04] and the
{ref}`SMAT <step-001>` page reads the SKY130 wafer from these sources as
a 200 mm, p-type, polished bulk wafer.

### Strength of the evidence

The "200 mm equipment", "200mm" and "Bulk" statements are SkyWater's
own and rank as **strong** on the scale of the
{ref}`machines index <machines-reading-evidence>`, though the platform
table was written long after the S8 flow was developed.[^skw-01][^skw-02]
The supplier lists are strong as statements but name no product, and the
statements quoted from GlobalWafers' and SEH America's pages describe
their catalogues, not SkyWater's purchases.[^sec-01][^sec-02][^gw-products][^seh-products]
The Cypress notice is strong for a supplier added to the S8 family at
the same fab in 2015 and silent on the wafer specification.[^cyp-06]
Nothing public describes SkyWater's test, monitor, filler or reclaimed
wafers; every use of them on this page is the step pages' reading of
industry practice.

(material-substrates-steps)=
### SKY130 steps that use this class

This page covers the rows of the {ref}`materials index <materials-table>`
listed below by key; the steps are those whose *Resources required* section
names one of them (the union of the rows' *Steps* cells).

Materials index rows covered:

* `si-wafers` — silicon wafers, 200 mm, p-type, polished bulk
* `test-wafers` — test and monitor wafers

Steps:

{ref}`SMAT <step-001>`, {ref}`BOX <step-002>`, {ref}`ISONIT <step-003>`, {ref}`STIE <step-006>`, {ref}`DNI <step-008>`, {ref}`LINOX <step-010>`, {ref}`LVTNI <step-015>`, {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`, {ref}`LVTPI <step-020>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`, {ref}`RTAI <step-034>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`NCHI <step-045>`, {ref}`LVGOX <step-047>`, {ref}`SAGD <step-048>`, {ref}`P1I <step-050>`, {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`BFR <step-060>`, {ref}`P1M <step-061>`, {ref}`P1ME <step-062>`, {ref}`IOX45 <step-063>`, {ref}`ASTI <step-065>`, {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`, {ref}`TIPRTAD <step-075>`, {ref}`SPNIT <step-076>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`SPOX <step-080>`, {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`, {ref}`RTAD <step-088>`, {ref}`PSG <step-089>`, {ref}`CMPP <step-090>`, {ref}`NCAPOX <step-091>`, {ref}`RTAD2 <step-092>`, {ref}`LICM1E <step-094>`, {ref}`SACETCH <step-095>`, {ref}`ALLY1 <step-096>`, {ref}`TI/TIN1 <step-097>`, {ref}`CSIL <step-098>`, {ref}`WDEP <step-099>`, {ref}`WCMPLI <step-100>`, {ref}`LITIN <step-101>`, {ref}`LI1ME <step-103>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`CMPL <step-106>`, {ref}`CTME <step-108>`, {ref}`TIN2 <step-109>`, {ref}`WDEP2 <step-110>`, {ref}`TIAL6 <step-112>`, {ref}`MM1E <step-114>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`VIME <step-119>`, {ref}`TIN3 <step-120>`, {ref}`WDEP3 <step-121>`, {ref}`TIAL12 <step-123>`, {ref}`MM2E <step-125>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`VIM2E <step-130>`, {ref}`TIN4 <step-131>`, {ref}`WDEP4 <step-132>`, {ref}`WTIAL3 <step-134>`, {ref}`CAPILD <step-135>`, {ref}`CAPTIW1 <step-136>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`VIM3E <step-145>`, {ref}`TIN5 <step-146>`, {ref}`WDEP5 <step-147>`, {ref}`WTIAL4 <step-149>`, {ref}`CAPILD2 <step-150>`, {ref}`CAPTIW2 <step-151>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`VIM4E <step-160>`, {ref}`WTIAL5 <step-161>`, {ref}`MM5E <step-163>`, {ref}`NFUSOX <step-164>`, {ref}`NSME <step-166>`, {ref}`NTSD <step-167>`, {ref}`PDME <step-169>`, {ref}`ALLY <step-170>`, {ref}`HPETEST <step-171>`

The steps fall into groups, as the step pages' *Resources required*
sections describe them:

* **The product wafer** — only {ref}`SMAT <step-001>` names the starting
  wafer itself.
* **Monitor wafers** at the furnace, implant, deposition, etch, strip and
  polish steps, for thickness, sheet resistance, particles, rates and
  selectivities; the implant pages add thermal-wave dose and tilt
  control ({ref}`ASTI <step-065>`, {ref}`BHI <step-066>`,
  {ref}`HVASTI <step-069>`), and the two alloy anneals name MOS
  capacitors on their monitors ({ref}`ALLY1 <step-096>`,
  {ref}`ALLY <step-170>`).
* **Calibration and reference wafers** — thermocouple wafers for the
  rapid thermal steps ({ref}`RTAI <step-034>`,
  {ref}`TIPRTAD <step-075>`, {ref}`RTAD <step-088>`,
  {ref}`RTAD2 <step-092>`, {ref}`CSIL <step-098>`); CD-SEM and overlay
  reference wafers at {ref}`P1M <step-061>`; and reference wafers for
  tester correlation at {ref}`HPETEST <step-171>`.

## Supply, handling, safety and facilities

None of the SkyWater sources cited here describes the fab's wafer
logistics, test-wafer stock or reclaim; the points below are industry
practice or supplier and standards statements.

* **Ordering and identity.** Wafers are ordered against SEMI M1 or M8
  categories[^semi-m1][^semi-m8] and marked to SEMI M12, whose mark
  "links the properties of the wafer stored in an appropriate database
  system to each individual wafer",[^semi-m12] or to SEMI M13, whose code
  includes "the origin, approximate resistivity, dopant species, and
  crystal growth orientation";[^semi-m13] the
  marking and sorting tools are on the
  {ref}`starting-material page <machine-starting-material>`.
* **Supply.** Wafers come from a few large makers; SkyWater's filings
  name two,[^sec-01][^sec-02] and GlobalWafers says it serves "100% of
  the top 25 customers in the semiconductor industry".[^gw-home] The S-1
  warns that "availability concerns with respect to some of our essential
  materials, tools and maintenance parts could also prompt a lengthy and
  expensive search for alternative sources which would necessitate
  requalification cycles and production delays".[^sec-01]
* **Test-wafer stock and reclaim.** Used test wafers are downgraded to
  less demanding uses, reclaimed by polishing, or scrapped; automated
  tracking and sorting cut the cost.[^popovich-1997][^ozelkan-2006][^faruqi-2008]
  Reclaim can be external or in-house: Dong et al. describe Micron's
  in-house process, whose CMP and wet steps met "the global reclaim
  specifications".[^dong-2024] SEMI M38 warns buyers to "exercise caution
  when sourcing materials with unknown thermal histories, unknown bulk
  contamination, or unknown deposits".[^semi-m38]
* **Contamination control.** Test wafers must not carry metals or films
  from one tool to another; Popovich et al. list "the potential for
  contamination and tool downtime if the wrong used test wafers are
  processed in the wrong tool".[^popovich-1997]
* **Handling.** Wafers travel in 25-slot cassettes or pods and are
  handled by edge (industry practice; {ref}`category-substrate`). Wafer
  handling carries no chemical hazard of its own.

## Process-integration notes for SKY130

These notes connect the class to the step pages; they add no SKY130
conditions of their own. SKY130's wafer specification and monitor plans
are not public.

* **Bulk wafer, no epitaxial layer.** The {ref}`SMAT <step-001>` page reads
  S130's "Bulk" substrate[^skw-02] as a polished CZ wafer, notes that the
  Cypress SONOS patent allows a bulk wafer or one with an epitaxial
  layer,[^pat-04] and leaves open whether the original S8 wafer was
  epitaxial. The step pages rely on STI, retrograde wells and the optional
  deep N-well for latch-up control, the combination the ITRS says reduces
  the need for epi.[^itrs-01]
* **Substrate doping.** No resistivity is published. The SMAT page gives
  two indirect figures: the PDK's n-well "background concentration" of
  8 × 10¹⁴ cm⁻³ in the design assumptions,[^pdk-03] and an effective
  body doping of about 1.4 × 10¹⁵ cm⁻³ that it extracts from SkyWater's
  test-tile data for the 20 V zero-Vt NMOS;[^raw-data-hv-mosfets]
  neither is a wafer specification.
* **Gettering and thermal budget.** The flow's hot front-end steps
  ({ref}`BOX <step-002>`, {ref}`LINOX <step-010>`, the well anneals) are
  where oxygen precipitates would nucleate and grow;[^borghesi-1995]
  whether SKY130 relies on the wafer's own precipitation or on a
  pre-engineered wafer is not public.
* **Crystal pits and the gate oxides.** Pair-pit COPs caused failures in
  gate oxides around 10 nm thick,[^ishii-1996] and COPs were the main
  cause of GOI failure in Miyazaki et al.'s capacitors,[^miyazaki-1997]
  10 nm being the range of the thick gate oxide of
  {ref}`GOX100 <step-043>` on that page's reading, so the incoming
  wafer's defect grade bears on gate-oxide yield (our reading).
* **Monitors as a hidden consumable.** On the step pages' readings, most
  of the flow's 171 steps name a monitor or reference wafer; at the ratios
  Watanabe et al. report for a DRAM fab, 1.5 to 0.5 monitor wafers per
  wafer start,[^watanabe-1999] test wafers can be a large share of
  silicon bought (our comparison; SkyWater's ratio is not public).
* **Product wafers as their own monitors.** The e-test at
  {ref}`HPETEST <step-171>` measures structures on product wafers; the
  public SKY130 test tile "consists of a grid of probe
  points",[^raw-data-testtile-prop] and it and monitor wafers answer
  different questions (the step page's reading).

## Related pages

* {ref}`category-substrate` — the wafer specification, crystal growth and
  the vendor's equipment.
* {ref}`machine-starting-material` — incoming inspection, marking and
  sorting.
* {ref}`machine-sheet-resistance-metrology` and
  {ref}`machine-film-thickness-metrology` — the gauges that measure most
  monitor wafers.
* {ref}`machine-defect-inspection` — particle monitors on bare wafers.
* {ref}`materials-index` — all consumable classes.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,994,761 A <patent-gp25194044>` — Ideal oxygen precipitating silicon wafers and oxygen out-diffusion-less process therefor (1997)

:::{dropdown} 1 family in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 8,796,098 B1 <patent-gp51229009>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* and the CMOS platform
  table — "200 mm equipment", the substrate services, and S130's "200mm"
  and "Bulk".[^skw-01][^skw-02]
* SkyWater Technology, Form S-1 (2021) and Form 10-K for fiscal 2023 —
  the raw-materials paragraphs, wafer suppliers and supply risk.[^sec-01][^sec-02]
* Cypress Semiconductor, PIN152804 (2015) — GlobalWafers qualified for S8
  at Fab 4.[^cyp-06]
* SkyWater PDK, process stack diagram and *Criteria & Assumptions* — the
  "p-substrate" label and the background concentration.[^pdk-04][^pdk-03]
* SEMI M1, M8, M24, M38 and M62 — prime, test, premium, reclaimed and
  epitaxial wafers.[^semi-m1][^semi-m8][^semi-m24][^semi-m38][^semi-m62]
* SEMI M12 and M13 — wafer marking.[^semi-m12][^semi-m13]
* GlobalWafers, *Products* and home page; SEH America, *Products* —
  current wafer catalogues.[^gw-products][^gw-home][^seh-products]
* Entegris, *SUPERSiC Silicon Carbide* brochure — silicon-carbide dummy
  wafers and reclaimed silicon dummies.[^entegris-supersic]
* SkyWater PDK Authors, raw-data repository — the test tile and the
  transistor data the SMAT page uses.[^raw-data-testtile-prop][^raw-data-hv-mosfets]

### High-level understanding

* Wikipedia, *Wafer (electronics)* and *GlobalWafers* — wafer sizes,
  thicknesses and notches; the supplier's history.[^wiki-wafer][^wiki-gw]
* Kao and Chung, *Wafer Manufacturing* — slicing, lapping and polishing
  of silicon wafers.[^kao-2021]
* Shimura, *Semiconductor Silicon Crystal Technology* — the crystal and
  its defects.[^shimura-1989]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — wafer
  preparation and gettering.[^txt-01]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — wafers and
  incoming inspection on the fab floor.[^txt-07]

### Deep dive

* Zulehner, *J. Cryst. Growth* 1983 — Czochralski growth of
  silicon.[^zulehner-1983]
* Falster and Voronkov, *Mater. Sci. Eng. B* 2000 — engineering point
  defects in crystals and wafers.[^falster-2000]
* Ryuta et al., *JJAP* 1990 — crystal-originated pits revealed by
  SC-1.[^ryuta-1990]
* Ishii et al., *JJAP* 1996 — pair pits and gate-oxide
  failure.[^ishii-1996]
* Miyazaki et al., *JJAP* 1997 — COP microstructure and gate-oxide
  integrity.[^miyazaki-1997]
* Borghesi et al., *JAP* 1995 — oxygen precipitation in
  silicon.[^borghesi-1995]
* Kang and Schroder, *JAP* 1989 — experiments and a segregation model
  for phosphorus-diffusion and other extrinsic gettering.[^kang-1989]
* Falster et al. (MEMC), US 5,994,761 — wafers with pre-set oxygen
  precipitation.[^pat-mdz-memc]
* ITRS 2001, *Front End Processes* — starting-material targets and the
  polished-versus-epi trade.[^itrs-01]
* Popovich, Chilton and Kilgore, ASMC 1997 — a test-wafer inventory and
  reuse system.[^popovich-1997]
* Watanabe et al., ISSM 1999 — cutting monitor wafers per wafer start in
  a DRAM fab.[^watanabe-1999]
* Ozelkan and Cakanyildirim, *IEEE TSM* 2006 — a network model of
  test-wafer purchase and downgrading.[^ozelkan-2006]
* Faruqi et al., ASMC 2008 — automated test-wafer management and
  sorting.[^faruqi-2008]
* Dong et al., ASMC 2024 — in-house test-wafer reclaim.[^dong-2024]
* Chen et al., RTP 2002 — thin-film-thermocouple test wafers in a 200 mm
  RTP test bed.[^chen-2002-rtp]

## Open questions

* The SKY130 wafer's resistivity, orientation, oxygen content, grade and
  supplier, and whether the original S8 wafer was epitaxial, are not
  public.[^skw-02][^cyp-06]
* Whether GlobalWafers and SEH America supply test or reclaimed wafers as
  well as prime wafers, and which of GlobalWafers' and SEH's product
  lines SkyWater buys, is not stated.[^sec-01][^sec-02]
* SkyWater's use of test, monitor, filler and reference wafers — their
  grades, reuse and reclaim — is not described in any public source; the
  step pages' monitor wafers are industry practice.
* What wafers SkyWater's "High resistivity, red phos low resistivity and
  Silison on Insulator processing" service uses is not stated, and it is
  not tied to SKY130.[^skw-01]

<!-- footnotes -->

[^semi-m1]: SEMI, *SEMI M1 — Specification for Polished Single Crystal
    Silicon Wafers*, SEMI Standards store listing (revision M1-0924,
    current), accessed 2026-09-18.
    <https://store-us.semi.org/products/m00100-semi-m1-specification-for-polished-single-crystal-silicon-wafers>
[^gw-products]: GlobalWafers, *Products*, product page (polished,
    annealed, test and monitor, epitaxial and high-resistivity wafers),
    accessed 2026-09-13. <https://www.gw-semi.com/products/>
[^wiki-wafer]: Wikipedia, *Wafer (electronics)*.
    <https://en.wikipedia.org/wiki/Wafer_(electronics)>
[^semi-m8]: SEMI, *SEMI M8 — Specification for Polished Monocrystalline
    Silicon Test Wafers*, SEMI Standards store listing (revision
    M8-0312, reapproved 1023, current), accessed 2026-09-13.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^semi-m24]: SEMI, *SEMI M24 — Specification for Polished
    Monocrystalline Silicon Premium Wafers*, SEMI Standards store listing
    (revision M24-0612, inactive), accessed 2026-09-13.
    <https://store-us.semi.org/products/m02400-semi-m24-specification-for-polished-monocrystalline-silicon-premium-wafers>
[^semi-m38]: SEMI, *SEMI M38 — Specification for Polished Reclaimed
    Silicon Wafers*, SEMI Standards store listing (revision M38-0312,
    reapproved 1023, current), accessed 2026-09-13.
    <https://store-us.semi.org/products/m03800-semi-m38-specification-for-polished-reclaimed-silicon-wafers>
[^popovich-1997]: S. B. Popovich, S. R. Chilton and B. Kilgore,
    "Implementation of a test wafer inventory tracking system to increase
    efficiency in monitor wafer usage", *1997 IEEE/SEMI Advanced
    Semiconductor Manufacturing Conference and Workshop (ASMC 97)*,
    pp. 440–443. <https://doi.org/10.1109/ASMC.1997.630777>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; Minnesota facility and "Other Services" entries re-checked
    2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^skw-02]: SkyWater Technology, *Mixed-Signal CMOS & ROIC*, platform
    table, accessed 2026-09-13. <https://www.skywatertechnology.com/cmos/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; the "Business" overview, the risk
    factors and the "Raw materials." run-in paragraph under
    "Manufacturing"; read from a Wayback Machine copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; "Raw materials" paragraph; read from a Wayback Machine
    copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^kao-2021]: I. Kao and C. Chung, *Wafer Manufacturing: Shaping of
    Single Crystal Silicon Wafers*, Wiley, 2021,
    ISBN 978-0-470-06121-3. <https://doi.org/10.1002/9781118696224>
[^zulehner-1983]: W. Zulehner, "Czochralski growth of silicon", *Journal
    of Crystal Growth* **65**(1–3), 189–213 (1983).
    <https://doi.org/10.1016/0022-0248(83)90051-9>
[^shimura-1989]: F. Shimura, *Semiconductor Silicon Crystal Technology*,
    Academic Press, 1989, ISBN 978-0-12-640045-8.
    <https://openlibrary.org/isbn/9780126400458>
[^borghesi-1995]: A. Borghesi, B. Pivac, A. Sassella and A. Stella,
    "Oxygen precipitation in silicon", *Journal of Applied Physics*
    **77**(9), 4169–4244 (1995). <https://doi.org/10.1063/1.359479>
[^kang-1989]: J. S. Kang and D. K. Schroder, "Gettering in silicon",
    *Journal of Applied Physics* **65**(8), 2974–2985 (1989).
    <https://doi.org/10.1063/1.342714>
[^pat-mdz-memc]: R. Falster, M. Cornara, D. Gambaro and M. Olmo (MEMC
    Electronic Materials), *Ideal oxygen precipitating silicon wafers
    and oxygen out-diffusion-less process therefor*, US 5,994,761 A,
    granted 1999-11-30.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5994761>
[^wiki-gw]: Wikipedia, *GlobalWafers*.
    <https://en.wikipedia.org/wiki/GlobalWafers>
[^ryuta-1990]: J. Ryuta, E. Morita, T. Tanaka and Y. Shimanuki,
    "Crystal-Originated Singularities on Si Wafer Surface after SC1
    Cleaning", *Japanese Journal of Applied Physics* **29**(11A), L1947
    (1990). <https://doi.org/10.1143/JJAP.29.L1947>
[^ishii-1996]: H. Ishii, S. Shiratake, K. Oka, K. Motonami, T. Koyama and
    J. Izumitani, "Direct Observation of Crystal-Originated Particles on
    Czochralski-Grown Silicon Wafer Surface and Effect on Gate Oxide
    Reliability", *Japanese Journal of Applied Physics* **35**(11A),
    L1385 (1996). <https://doi.org/10.1143/JJAP.35.L1385>
[^falster-2000]: R. Falster and V. V. Voronkov, "The engineering of
    intrinsic point defects in silicon wafers and crystals", *Materials
    Science and Engineering: B* **73**(1–3), 87–94 (2000).
    <https://doi.org/10.1016/S0921-5107(99)00439-0>
[^semi-m62]: SEMI, *SEMI M62 — Specification for Silicon Epitaxial
    Wafers*, SEMI Standards store listing (revision M62-1125, current),
    accessed 2026-09-13.
    <https://store-us.semi.org/products/m06200-semi-m62-specification-for-silicon-epitaxial-wafers>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^expertech-vtr]: Expertech, *VTR7000PLUS Thermal Reactor | Vertical
    Diffusion Furnaces*, product page, accessed 2026-09-13.
    <https://www.exper-tech.com/products/vertical-thermal-reactor>
[^entegris-supersic]: Entegris, Inc., *SUPERSiC® Silicon Carbide:
    Products for semiconductor front end processes*, brochure 6116,
    accessed 2026-09-13.
    <https://www.entegris.com/content/dam/shared-product-assets/specialty-shared/brochure-supersic-semiconductor-front-end-6116.pdf>
[^chen-2002-rtp]: D. Chen, D. DeWitt, B. Tsai, K. Kreider and W. Kimes,
    "Effects of wafer emissivity on rapid thermal processing
    temperature measurement", *Proc. 10th IEEE International Conference
    on Advanced Thermal Processing of Semiconductors (RTP 2002)*,
    pp. 59–67. <https://doi.org/10.1109/RTP.2002.1039440>
[^ozelkan-2006]: E. C. Ozelkan and M. Cakanyildirim, "Test Wafer
    Management for Semiconductor Manufacturing", *IEEE Transactions on
    Semiconductor Manufacturing* **19**(2), 241–251 (2006).
    <https://doi.org/10.1109/TSM.2006.873401>
[^watanabe-1999]: A. Watanabe, T. Kobayashi, T. Egi and T. Yoshida,
    "Continuous and independent monitor wafer reduction in DRAM fab",
    *1999 IEEE International Symposium on Semiconductor Manufacturing
    (ISSM)*, pp. 303–306. <https://doi.org/10.1109/ISSM.1999.808796>
[^seh-products]: SEH America, *Products*, product page, accessed
    2026-09-13. <https://sehamerica.com/products/>
[^cyp-06]: Cypress Semiconductor, Product Information Notification
    PIN152804, *Qualification of GlobalWafer Silicon Wafers for 250nm,
    130nm and 90nm Technology Products at Cypress Fab 4*, 2015-07-12
    (copy hosted by Future Electronics).
    <https://media.futureelectronics.com/PCN/45887_SPCN.PDF>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^semi-m12]: SEMI, *SEMI M12 — Specification for Serial Alphanumeric
    Marking of Silicon Wafers*, SEMI Standards store listing (revision
    M12-0523, current), accessed 2026-09-13.
    <https://store-us.semi.org/products/m01200-semi-m12-specification-for-serial-alphanumeric-marking-of-the-front-surface-of-wafers>
[^semi-m13]: SEMI, *SEMI M13 — Specification for Alphanumeric Marking of
    Silicon Wafers*, SEMI Standards store listing (revision M13-0523,
    current), accessed 2026-09-13.
    <https://store-us.semi.org/products/m01300-semi-m13-specification-for-alphanumeric-marking-of-silicon-wafers>
[^gw-home]: GlobalWafers, *Silicon Wafer Manufacturing*, home page,
    accessed 2026-09-13. <https://www.gw-semi.com/>
[^faruqi-2008]: A. Faruqi, R. Goss, D. Adhikari and T. Kowtsch, "Test
    Wafer Management and Automated Wafer Sorting", *2008 IEEE/SEMI
    Advanced Semiconductor Manufacturing Conference (ASMC)*,
    pp. 322–326. <https://doi.org/10.1109/ASMC.2008.4529062>
[^dong-2024]: X. Dong, S. Mukherjee, M. Asokan, Y. Yang and V. Duvvuru,
    "In-house Test Wafer Reclaim for Fab Cost and Wastage Reduction",
    *2024 35th Annual SEMI Advanced Semiconductor Manufacturing Conference
    (ASMC)*, pp. 1–7. <https://doi.org/10.1109/ASMC61125.2024.10545463>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
    Shown as in force; estimated expiry 2034-02-26 (estimate from public
    records, not legal advice).
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^raw-data-hv-mosfets]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the 5 V, 10/16 V and
    20 V transistors, the native, zero-Vt and ESD NMOS and the thick-oxide
    gate capacitors, IC-CAP `.mdm` files in `sky130_fd_pr/cells/`,
    `google/skywater-pdk-sky130-raw-data` repository, 2022, retrieved
    2026-09-13; values quoted from them are our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
[^miyazaki-1997]: M. Miyazaki, S. Miyazaki, T. Kitamura, Y. Yanase, T.
    Ochiai and H. Tsuya, "Influence of Crystal-Originated 'Particle'
    Microstructure on Silicon Wafers on Gate Oxide Integrity", *Japanese
    Journal of Applied Physics* **36**(10R), 6187 (1997).
    <https://doi.org/10.1143/JJAP.36.6187>
[^raw-data-testtile-prop]: SkyWater PDK Authors, *SkyWater 130nm
    Proprietary Manufacturing Test Tile*,
    `docs/sky130-testtile-proprietary/README.rst`,
    `google/skywater-pdk-sky130-raw-data` repository, 2022, retrieved
    2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/README.rst>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
