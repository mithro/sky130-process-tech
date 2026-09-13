(overview-index)=
# Overview

This section introduces the SKY130 process technology as a whole before
the step-by-step pages. It says where the process came from and what it
offers, explains how this reference is organised and how it marks what
is known and what is inferred, groups the 171 steps into process
modules, walks up a simplified cross-section of the finished wafer,
sets out how the flow divides into front end, middle of line and back
end, and collects the most important questions the public record leaves
open. A companion page describes the optional resistive-memory tier of
the `sky130B` variant.

```{toctree}
:maxdepth: 1

sky130b-reram
```

## What SKY130 is

### A Cypress process in a former Cypress fab

The PDK's *Background* page describes SKY130 as "a mature 180nm-130nm
hybrid technology developed by Cypress Semiconductor that has been used
for many production parts", now "available as a foundry technology
through SkyWater Technology Foundry", and as "the 8th generation SONOS
technology node (130nm)".[^pdk-02] The PDK's *Previous Nomenclature*
page gives the older name: `s8` is "The old Cypress and SkyWater name
for the SKY130 process. It stood for the "8th generation" of the SONOS
technology developed originally by Cypress."[^pdk-previous] Cypress used
the same name in public: a 2007 product announcement calls it "Cypress's
S8(tm) 0.13-micron SONOS (Silicon Oxide Nitride Oxide Silicon) embedded
nonvolatile memory technology",[^cyp-20] and a 2011 release still
referred to "the current 130-nanometer S8™ process".[^cyp-22]

The process was run in Cypress's Fab 4 in Bloomington, Minnesota.
Cypress described Fab 4, where it ramped its 0.13 µm technology in
2003, as an "eight-inch wafer production facility",[^cyp-07] and a 2015
Cypress notice qualified a new wafer supplier "for the 250nm R7, 130nm
C8/R8/S8/L8 and 90nm C9/R9/R95 technology products at Cypress Fab 4 in
Bloomington, Minnesota".[^cyp-06] On 2017-03-01 Cypress announced that it
had sold "the subsidiary that owns its semiconductor wafer fabrication
facility in Bloomington, Minnesota to SkyWater Technology
Foundry",[^cyp-01] and SkyWater described what it had bought as "a 200mm
semiconductor wafer manufacturing facility in Bloomington, Minn.",
"Originally commissioned by Control Data Corporation in the
1980s".[^skw-10] Wikipedia summarises the company's origin the same way:
it "was formed in 2017, when private equity firm Oxbow Industries
acquired Cypress Foundry Solutions".[^wiki-skywater] SkyWater lists "200
mm equipment" for the Minnesota fab,[^skw-01] and its annual report for
2023 says that the same 200 mm fab offers "CMOS process flows for a
number of different node dimensions … ranging from 90 nm—350 nm", so
SKY130 shares the line with other flows.[^sec-02]

SkyWater's own product name for the process is S130: its platform table
lists S130 as "130nm CMOS" on "200mm" wafers,[^skw-02] and SkyWater
describes the open PDK as "known as SKY130 — based on SkyWater's volume
130 nm CMOS technology".[^ann-13] This reference, like its step pages,
treats S130 and SKY130 as the same process (inference from those two
statements; SkyWater does not say that every S130 option is in the open
PDK).

### The open PDK

The open PDK is "a collaboration between Google and SkyWater Technology
Foundry to provide a fully open source Process Design Kit", released
"under the Apache 2.0 license".[^pdk-10] It was announced in a FOSSi
Foundation Dial-Up talk by Tim Ansell of Google, which the foundation
reported on 2020-06-30 as the announcement of "SkyWater PDK, the first
manufacturable, open source process design kit".[^ann-03] Wikipedia's
article on the node records the same event: "In 2020, American
semiconductor company SkyWater Technology, in conjunction with Google
and eFabless, released their 130 nm process design kit as open-source
under the Apache License."[^ann-17] A free shuttle programme followed; the
announcement of November 2020 said that "Each shuttle run will have 40
design slots (seats) and the first run is scheduled to launch in Q4
2020".[^ann-10]

The open PDK is the main public description of the process, and most
of the numbers in this reference come from it: its design rules, its
layer and mask tables, its device pages and electrical specifications,
its extraction tables and its process stack diagram.[^pdk-03][^pdk-04]
It is not a process description — it contains no recipes, and its
thicknesses are drawn or tabulated for design, extraction and antenna
calculations — which is why the step pages read each number for what
it is.

### What the process offers

The PDK repository summarises the technology stack as "Support for
internal 1.8V with 5.0V I/Os (operable at 2.5V)", "1 level of local
interconnect", "5 levels of metal", "Is inductor-capable", "Has high
sheet rho poly resistor", "Optional MiM capacitors", "Includes SONOS
shrunken cell", "Supports 10V regulated supply" and "HV extended-drain
NMOS and PMOS", and adds that SKY130 includes "many normally *optional*
features as standard (features like the local interconnect, SONOS
functionality, MiM capacitors, and more)".[^pdk-10] The *Background*
page lists the stack as "5 levels of metal (`p` - penta)", "Inductor or
Inductor-Capable (`i`)", "Poly resistor (`r`)", "SONOS shrunken cell
(`s`)" and "Supports 10V regulated supply (`10R`)".[^pdk-02]

The PDK's device pages document 1.8 V NMOS and PMOS transistors with
low- and high-threshold variants, native NMOS at 3.0 V and 5.0 V,
"5.0V/10.5V" NMOS and PMOS, a "10V/16V PMOS FET" and an "11V/16V NMOS
FET", 20 V NMOS and PMOS (including native, zero-threshold and isolated
NMOS), an ESD NMOS, diodes, NPN and PNP bipolar transistors, SRAM and
{term}`SONOS` cells, generic and precision ("P+" and "P-") poly resistors,
{term}`MiM capacitors <MiM capacitor>` and vertical parallel-plate
capacitors.[^pdk-07] SkyWater's S130 platform table, re-read on
2026-09-13, gives the same process in foundry terms: metal "5: Al",
local interconnect "1", top metal "1.2 µm", "Mask Steps" "30 – 34",
isolation "STI", gate "Poly", core voltage "1.8V", I/O "3.3V, 5.0V",
high voltage "20+V, Drain-Extended CMOS (16V)", MiM capacitor "Yes",
precision resistors "2000Ω/□ 300Ω/□ (Both P-poly)" and a "Bulk"
substrate.[^skw-02]

Each of these features has a visible cost in the step list, and the
module table below shows where: the two gate-oxide thicknesses need a
mask of their own ({ref}`LVOM <step-044>`); the drain-extended devices
need dedicated well masks ({ref}`PWBM <step-026>`,
{ref}`PWDEM <step-030>`); the SONOS cell needs a tunnel window, an ONO
island and its own tip implant ({ref}`TUNM <step-035>`,
{ref}`ONOM <step-041>`, {ref}`LDNTM <step-071>`); the precision
resistors need three implant masks ({ref}`RPM <step-049>`,
{ref}`RRPM <step-052>`, {ref}`URPM <step-055>`); the local interconnect
needs a contact and a line mask ({ref}`LICM1 <step-093>`,
{ref}`LI1M <step-102>`); and each MiM capacitor needs a plate mask
({ref}`CAPM <step-137>`, {ref}`CAP2M <step-152>`). The step pages also
read three features that set SKY130 apart from a typical 130 nm logic
process of its time, all as inferences from the PDK's numbers: the gates
and diffusions carry no {term}`salicide`, only a silicide at the bottom of
each contact ({ref}`CSIL <step-098>`, from the unsilicided poly and
diffusion sheet resistances[^pdk-08]); the interconnect is
{term}`subtractive <subtractive metallisation>` aluminium with tungsten
plugs rather than copper {term}`damascene` ({ref}`TIAL6 <step-112>`,
{ref}`MM1E <step-114>`); and both NMOS and PMOS gates are n⁺ poly
({ref}`P1I <step-050>`).

### Variants and options

The open-source build scripts distribute the PDK in two variants:
"sky130A = 5-metal backend stack with dual MiM" and "sky130B = 5-metal
backend stack with dual MiM and ReRAM".[^opdks-makefile] The second has
existed "From open_pdks version 1.0.269",[^opdks-readme] and SkyWater's
documentation of the ReRAM device is marked "Initial documentation only
release".[^reram-index] This reference describes `sky130A`; the ReRAM
tier, which is not in the step list, has its own page,
{ref}`overview-sky130b-reram`.

The PDK's older process names show how optional modules were once
named: `s8pfhd`, "The base process. 5 metal layer backend stack, 16V
devices, deep nwell"; `s8phirs`, "The base process plus rdl layer and
rdl metal inductors"; `s8phrc`, "The base process plus dual MiM cap
layers on metal 3 and metal 4"; and `s8pfn-20`, "The base process plus
UHV (ultra-high voltage) implants for 20V device support".[^pdk-previous]
Thicker top metals are documented only in the PDK's tables for flows
other than the one described here. The antenna-calculation table gives
"Metal5 thickness for antenna ratio calculation (S8P\*/SP8P\* with 2um
thick metal)" as 2 µm beside a 1.2 µm entry "with 1.2um thick metal", a
2 µm metal 3 for the "S8TM\* flow" and a 2 µm metal 4 for "S8Q\*/SP8Q";[^pdk-03]
the mask table lists "Metal 3-S8TM" and "Via 2-S8TM" variants without the
"Used in SKY130" mark.[^pdk-05] The step pages read SKY130 as the
1.2 µm-metal-5 flow and the 2 µm entries as belonging to other flows
({ref}`WTIAL3 <step-134>`, {ref}`WTIAL5 <step-161>`; inference), which
agrees with the "1.2 µm" top metal in SkyWater's S130 table.[^skw-02] The
same mask table marks as used in SKY130 three masks for polyimide and
copper redistribution layers that have no step in the step list
({ref}`masks-index`).[^pdk-05]

## How to read this reference

### The step list

The flow is documented as 171 numbered steps, from
{ref}`SMAT <step-001>` (starting material) to
{ref}`HPETEST <step-171>` (electrical test), in the order in which a
wafer experiences them ({ref}`steps-index`). The step numbers, codes,
names and order are those of the public *S8 / SKY130 Process Steps*
sheet.[^steps-sheet] The sheet records what it calls each step and
nothing about how the step is done: a step name is not evidence of a
film, chemistry, tool, dose or temperature, and where a name needs
interpreting the pages say "the step list does not explain …; we read
…" and base the reading on other public sources. Each step is assigned
to one of ten categories; the flow has 41 deposition, 36 lithography,
27 etch, 25 implant, 15 strip, 12 {term}`CMP`, 7 anneal and 6
oxidation steps, one starting-material step and one test step
({ref}`categories-index`). Resist strips that follow an *etch* mask have
no step of their own in the list, and the step pages treat them as part
of the etch ({ref}`category-strip`).

### A step page

Every step page has the same structure. A summary table gives the step
number, code, category, phase ({term}`FEOL`, {term}`MOL` or
{term}`BEOL`, with the module) and links to the previous and next
steps. Then
come:

* **What this step is** — a plain description followed by a precise
  one: what is deposited, patterned, implanted or removed, with the
  public numbers.
* **Step category** — the link to the category page and what is
  particular to this instance.
* **Why this step exists** — the device or integration reason, what
  would go wrong without it and which steps depend on it.
* **How it is typically performed** — an industry-generic recipe
  outline for a 200 mm, 130 nm-era fab, with sources for every
  typical value.
* **Machines typically used** and **Machines likely used at
  SkyWater** — tool classes from any vendor, then only those tools for
  which there is public evidence at SkyWater, with the strength of the
  evidence.
* **Resources required** — gases, chemicals, targets, slurries,
  resists and wafers.
* **Related steps and cross-references**.
* **References** — three annotated reading lists: *Cross-check*
  (primary sources for the page's claims), *High-level understanding*
  and *Deep dive* (at least eight entries).
* **Open questions** — what could not be confirmed publicly.

Full citations are footnotes at the end of each page.

### The cross-cutting pages

* {ref}`categories-index` — one page per unit process (oxidation,
  deposition, lithography, etch, implant, strip, anneal, CMP, substrate,
  test) explaining the physics, equipment and consumables once.
* {ref}`machines-index` — the machine classes named on the step pages,
  what SkyWater has published about its tools, which steps use which
  class, and a list of inconsistencies between pages.
* {ref}`materials-index` — the consumables, mapped to the steps that
  use them.
* {ref}`masks-index` — the 36 mask steps set against the PDK's mask,
  layer and minimum-CD tables.
* {ref}`glossary` — terms and acronyms, linked from the pages on first
  use.
* {ref}`references-index` and the
  {ref}`public-sources inventory <references-public-sources>` — every
  source cited, with a key; the footnote labels on every page are these
  keys in lower case.

### Known, typical and inferred

The pages use a fixed vocabulary to separate kinds of statement.

* **Public fact** — "SkyWater lists …", "the PDK documentation shows
  …", "Cypress's report gives …", with a footnote to the source, and
  quotation marks around the source's words.
* **Typical value** — "typical", "industry-typical" or "era-typical"
  marks a number that describes a 200 mm, 130 nm-era fab in general,
  sourced to a textbook, paper, patent or roadmap; it is not a SkyWater
  number.
* **Inference** — "we infer", "on our reading", "(inference)" and "our
  arithmetic" mark a conclusion drawn from public evidence, with the
  reasoning given on the page.
* **Evidence strength** for tools at SkyWater follows the inventory's
  scale: **strong**, a SkyWater or tool-vendor statement; **medium**, a
  SkyWater job posting or an interview with a named employee; **weak**,
  indirect evidence. Because SkyWater's tool list never names a step,
  the pages grade the tool and its assignment to the step separately,
  typically as "strong for the tool; inference for the assignment"
  ({ref}`machines-index`).

The PDK's process stack diagram, the source of most thicknesses on these
pages, is marked "(Diagram not to scale!)";[^pdk-04] its labels are
quoted as labels, and where they do not add up the pages say so.

<!-- footnotes -->

[^pdk-02]: SkyWater PDK Authors, *Background*, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/background.html>
[^pdk-previous]: SkyWater PDK Authors, *Previous Nomenclature*,
    SkyWater SKY130 PDK documentation, accessed 2026-09-13.
    <https://skywater-pdk.readthedocs.io/en/main/previous.html>
[^cyp-20]: Electronics Weekly, *Cypress 4-Mbit non-volatile static
    random access memory*, 2007-10-18, accessed 2026-09-13.
    <https://www.electronicsweekly.com/news/products/memory-products/cypress-4-mbit-non-volatile-static-random-access-memory-2007-10/>
[^cyp-22]: Cypress Semiconductor / UMC, *Cypress and UMC Deliver ICs on
    New 65-Nanometer SONOS Embedded Flash Technology*, PR Newswire,
    2011-07-27, accessed 2026-09-13.
    <https://www.prnewswire.com/news-releases/cypress-and-umc-deliver-ics-on-new-65-nanometer-sonos-embedded-flash-technology-126238008.html>
[^cyp-07]: Cypress Semiconductor Corp., Form 10-Q/A for Q1 2003.
    <https://www.sec.gov/Archives/edgar/data/0000791915/000120677403000508/d12840.htm>
[^cyp-06]: Cypress Semiconductor, Product Information Notification
    PIN152804, *Qualification of GlobalWafer Silicon Wafers for 250nm,
    130nm and 90nm Technology Products at Cypress Fab 4*, 2015-07-12
    (copy hosted by Future Electronics), accessed 2026-09-13.
    <https://media.futureelectronics.com/PCN/45887_SPCN.PDF>
[^cyp-01]: Cypress Semiconductor, *Cypress Closes Sale of Minnesota Wafer
    Fabrication Facility*, PR Newswire, 2017-03-01, accessed 2026-09-13.
    <https://www.prnewswire.com/news-releases/cypress-closes-sale-of-minnesota-wafer-fabrication-facility-300416287.html>
[^skw-10]: SkyWater Technology, *SkyWater Technology Foundry Acquires
    Twin-Cities Semiconductor Manufacturing Facility from Cypress
    Semiconductor Corporation*, press release, 2017-03-27, accessed
    2026-09-13.
    <https://www.skywatertechnology.com/skywater-technology-foundry-acquires-twin-cities-semiconductor-manufacturing-facility-from-cypress-semiconductor-corporation/>
[^wiki-skywater]: Wikipedia, *SkyWater Technology*, accessed 2026-09-13.
    <https://en.wikipedia.org/wiki/SkyWater_Technology>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^skw-02]: SkyWater Technology, *Mixed-Signal CMOS & ROIC*, platform
    table, accessed 2026-09-13. <https://www.skywatertechnology.com/cmos/>
[^ann-13]: SkyWater Technology, *SKY's the Limit with the SKY130
    Open-Source PDK*, blog, 2023-11-12, accessed 2026-09-13.
    <https://www.skywatertechnology.com/sky130-open-source-pdk/>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README, accessed 2026-09-13. <https://github.com/google/skywater-pdk>
[^ann-03]: P. Wagner (FOSSi Foundation), *Produce your own physical
    chips. For free. In the Open.*, 2020-06-30, accessed 2026-09-13.
    <https://fossi-foundation.org/blog/2020-06-30-skywater-pdk>
[^ann-17]: Wikipedia, *130 nm process*, accessed 2026-09-13.
    <https://en.wikipedia.org/wiki/130_nm_process>
[^ann-10]: Google / SkyWater / Efabless, *Google Partners with SkyWater
    and Efabless to Enable Open Source Manufacturing of Custom ASICs*,
    PR Newswire, 2020-11-12, accessed 2026-09-13.
    <https://www.prnewswire.com/news-releases/google-partners-with-skywater-and-efabless-to-enable-open-source-manufacturing-of-custom-asics-301171870.html>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation (Table 4, `assumptions/04-physical.csv`).
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/04-physical.csv>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^opdks-makefile]: R. T. Edwards et al., *open_pdks*,
    `sky130/Makefile.in`, lines 3–4, commit 1689ac3 (2026-08-27),
    accessed 2026-09-13.
    <https://github.com/RTimothyEdwards/open_pdks/blob/1689ac3f2dc763876eaf967227c7dfe831b031ae/sky130/Makefile.in>
[^opdks-readme]: R. T. Edwards et al., *open_pdks*, `sky130/README`,
    commit 1689ac3, accessed 2026-09-13.
    <https://github.com/RTimothyEdwards/open_pdks/blob/1689ac3f2dc763876eaf967227c7dfe831b031ae/sky130/README>
[^reram-index]: SkyWater PDK Authors, *sky130_fd_pr_reram - SKY130
    ReRAM (SkyWater Provided)*, documentation index page, accessed
    2026-09-13. <https://sky130-fd-pr-reram.readthedocs.io/en/latest/>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    retrieved 2026-09-13; tab "Sheet1" lists the 171 steps (number, code and
    description). <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
