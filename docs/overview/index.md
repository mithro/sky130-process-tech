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
the same name in public: a 2007 Electronics Weekly article calls it "Cypress's
S8(tm) 0.13-micron SONOS (Silicon Oxide Nitride Oxide Silicon) embedded
nonvolatile memory technology",[^cyp-20] and a 2011 release still
referred to "the current 130-nanometer S8™ process".[^cyp-22]

The process was run in Cypress's Fab 4 in Bloomington, Minnesota.
Cypress described Fab 4, where it was ramping its 0.13 µm technology in
early 2003, as an "eight-inch wafer production facility",[^cyp-07] and a 2015
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

Measured silicon data are published too, in a separate raw-data
repository: current–voltage and capacitance–voltage measurements
"collected under contract by CoolCAD
Electronics LLC using the manufacturing test tile created by
SkyWater",[^raw-data-readme] and the pad documentation of that
{term}`test tile`, whose 273 modules name contact and via chains,
resistors, capacitors and transistors layer by layer and are quoted on
the step pages as public examples of e-test-type structures; the
repository does not say they are the structures measured at
{ref}`HPETEST <step-171>`.[^raw-data-testtile-pads] Among the
measured files are sweeps of the 5 V, 16 V and 20 V transistors, the
native and zero-threshold NMOS, the ESD NMOS and the thick-oxide
gate capacitors. Thresholds, resistances, body-effect coefficients and
oxide capacitance extracted from them are quoted on the step pages for
the substrate ({ref}`SMAT <step-001>`), the gate oxide
({ref}`GOX100 <step-043>`), the P-well block, drain-extended wells and
depletion implant ({ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`,
{ref}`DEPI <step-038>`) and electrical test ({ref}`HPETEST <step-171>`), each marked as our
extraction rather than a published value; the files record no
temperature, date or wafer.[^raw-data-hv-mosfets] The files for the five
1.8 V transistor types (standard, low-Vt and high-Vt) are used the same
way: measured thresholds, drain currents and body effect are quoted
beside the e-test values at {ref}`HPETEST <step-171>`, on the
threshold-implant pages ({ref}`LVTNM <step-014>`,
{ref}`LVTNI <step-015>`, {ref}`LVTPI <step-020>`,
{ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`,
{ref}`NCHI <step-045>`), for the gate-length dependence at
{ref}`BHI <step-066>`, for deep N-well at {ref}`DNI <step-008>` and for
the source/drain diffusion extent at {ref}`FILOX <step-011>`; they bear
on the pages' readings of those steps but give no implant doses or
depths.[^raw-data-lv-mosfets] The files for the tile's resistors, MiM
capacitors, varactors and bipolar transistors are used in the same
way. In our extraction from the published measurements the P+ precision
poly resistors come out at about 310 Ω/sq ({ref}`PRI <step-053>`), the
P− ones at about 1 940–1 970 Ω/sq ({ref}`UPRI <step-056>`) and the
first MiM capacitor at 1.87 fF/µm² ({ref}`CAPILD <step-135>`); diffusion
and well resistors, the second MiM capacitor, the varactors and the NPN
are quoted at {ref}`PSDI <step-082>`, {ref}`NSDI <step-086>`,
{ref}`DNM <step-007>`, {ref}`DNI <step-008>`, {ref}`NWI <step-018>`,
{ref}`PWI <step-027>`, {ref}`CAPILD2 <step-150>`,
{ref}`HVTPM <step-022>` and {ref}`LVGOX <step-047>`. These files too
record no temperature, date or wafer.[^raw-data-passives]

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

The PDK's device pages document 1.8 V NMOS and PMOS transistors,
low-threshold NMOS and PMOS and a high-threshold PMOS, 1.8 V
accumulation-mode varactors, native NMOS at 3.0 V and 5.0 V,
"5.0V/10.5V" NMOS and PMOS, a "10V/16V PMOS FET" and an "11V/16V NMOS
FET", 20 V NMOS and PMOS (including native, zero-threshold and isolated
NMOS), an ESD NMOS, diodes, NPN and PNP bipolar transistors, SRAM and
{term}`SONOS` cells, generic and precision ("P+" and "P-") {term}`poly resistors <poly resistor>`,
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
mask of their own ({ref}`LVOM <step-044>`); the {term}`drain-extended <DEMOS>` devices
need their own P-well mask and blocked regions in the P-well block mask
({ref}`PWDEM <step-030>`, {ref}`PWBM <step-026>`); the SONOS cell needs a tunnel window, an ONO
island and its own tip implant ({ref}`TUNM <step-035>`,
{ref}`ONOM <step-041>`, {ref}`LDNTM <step-071>`); the precision
resistors need three implant masks ({ref}`RPM <step-049>`,
{ref}`RRPM <step-052>`, {ref}`URPM <step-055>`); the local interconnect
needs a contact and a line mask ({ref}`LICM1 <step-093>`,
{ref}`LI1M <step-102>`); and each MiM capacitor needs a plate mask
({ref}`CAPM <step-137>`, {ref}`CAP2M <step-152>`). These pairings
rest on the PDK's descriptions of the corresponding layers, as set out on
each step page. Three further features differ from the copper, salicided
processes of leading-edge 130 nm logic (our characterisation). Its interconnect is aluminium ("5:
Al"[^skw-02]), which the step pages describe as patterned
{term}`subtractively <subtractive metallisation>` over tungsten plugs
rather than as copper {term}`damascene` ({ref}`TIAL6 <step-112>`,
{ref}`MM1E <step-114>`). Its gates and diffusions carry, on the step
pages' reading of the unsilicided poly and diffusion
{term}`sheet resistances <sheet resistance>`,[^pdk-08] no
{term}`salicide`, only a {term}`silicide` at the bottom
of each contact ({ref}`CSIL <step-098>`; inference). And both its NMOS
and PMOS gates are, on the reading of the {ref}`P1I <step-050>` page,
n⁺ poly (inference).

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
The PDK documents thicker top metals only in entries labelled with other
flow names. The antenna-calculation table gives
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
steps. Then come:

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

(overview-modules)=
## The flow by module

The 171 steps fall into thirteen process modules, each ending where
one structure of the device is complete. The module boundaries follow
the phases printed in each step page's summary table, with three of
them split where the flow changes subject (SONOS stack and gate
oxides; tips and spacers; the first and second MiM capacitor levels).
The mask counts are the lithography steps of the step list in each
module, as listed on the {ref}`masks-index`; all thirteen add up to 171
steps and 36 masks.

| Module | Steps | Number of steps | Mask steps | Key public facts |
|--------|-------|-----------------|------------|------------------|
| Starting material, isolation and deep N-well | {ref}`SMAT <step-001>` – {ref}`NS19 <step-013>` | 13 | 2 (`FOM`, `DNM`) | "Bulk" substrate;[^skw-02] "FOX K=3.9" field oxide, top at 0.3262 µm on the stack diagram,[^pdk-04] 0.07 µm above the silicon under poly[^pdk-03] |
| Wells and threshold implants | {ref}`LVTNM <step-014>` – {ref}`RTAI <step-034>` | 21 | 5 (`LVTNM`, `NWM`, `HVTPM`, `PWBM`, `PWDEM`) | ten implants and one anneal; N-well peak 6.0 × 10¹⁷ cm⁻³ and baseline vertical dimension 1.1 µm, P-well peak 4 × 10¹⁷ cm⁻³ at 0.42 µm;[^pdk-03] `PWBM` and `PWDEM` not marked as used in SKY130[^pdk-05] |
| SONOS tunnel window and ONO stack | {ref}`TUNM <step-035>` – {ref}`ONOME <step-042>` | 8 | 2 (`TUNM`, `ONOM`) | ONO thicknesses not public, bounded by Cypress patents;[^pat-01][^pat-02] programmed and erased thresholds 1.44 V and −2.3 V (0.45/0.22 cell) in the e-test table[^pdk-07] |
| Gate oxides | {ref}`GOX100 <step-043>` – {ref}`LVGOX <step-047>` | 5 | 1 (`LVOM`) | high-voltage devices "use 110A gate oxide thickness";[^pdk-hv] model `toxe` 4.148 nm (1.8 V) and 11.6 nm (5 V)[^pdk-model-nfet01v8][^pdk-model-nfet5v] |
| Poly gate and poly resistors | {ref}`SAGD <step-048>` – {ref}`IOX45 <step-063>` | 16 | 4 (`RPM`, `RRPM`, `URPM`, `P1M`) | poly 0.18 µm;[^pdk-03][^pdk-04] gate poly 48.2 Ω/sq;[^pdk-08] 300 Ω/sq and 2000 Ω/sq precision resistors;[^pdk-07] poly width 0.150 µm, space 0.210 µm;[^pdk-periph] "poly cap after SPE" 0.2 µm[^pdk-03] |
| Tips and halos | {ref}`NTM <step-064>` – {ref}`TIPRTAD <step-075>` | 12 | 3 (`NTM`, `HVNTM`, `LDNTM`) | "N Tip (As)"; tip implant angle 7°, HV tip 40° with 23° twist;[^pdk-03] no P-tip mask in the mask table[^pdk-05] |
| Spacers and source/drain | {ref}`SPNIT <step-076>` – {ref}`RTAD <step-088>` | 13 | 3 (`NPCM`, `PSDM`, `NSDM`) | "SPNIT K=7.5";[^pdk-04] "oxide spacer" 0.05 µm, "N+ or P+ S/D (XJ)" 0.1 µm;[^pdk-03] N- and P-diffusion 120 Ω/sq and 197 Ω/sq[^pdk-08] |
| Pre-metal dielectric, contact silicide and local interconnect | {ref}`PSG <step-089>` – {ref}`CMPL <step-106>` | 18 | 2 (`LICM1`, `LI1M`) | "PSG K=3.9", 0.6099 µm from the field-oxide top to the `li` bottom and 0.4299 µm from the field-poly top to the `li` bottom;[^pdk-04] "Pre-LI ILD thickness" 0.5 µm;[^pdk-03] `li` 0.1 µm,[^pdk-04] 12.8 Ω/sq;[^pdk-08] "LINT K=7.3" 0.075 µm and "NILD2 K=4.05" 0.265 µm[^pdk-04] |
| Metal contact and metal 1 | {ref}`CTM1 <step-107>` – {ref}`NCAPOX3 <step-117>` | 11 | 2 (`CTM1`, `MM1`) | `mcon` 0.170 µm square;[^pdk-periph] S8 metal 1 "100A Ti / 3200A Al -0.5%Cu / 300A TiW";[^cyp-qtp-113005] `met1` 0.36 µm;[^pdk-04] 125 mΩ/sq[^pdk-08] |
| Via 1, metal 2 and via 2 | {ref}`VIM <step-118>` – {ref}`WTIAL3 <step-134>` | 17 | 3 (`VIM`, `MM2`, `VIM2`) | via 0.150 µm and via 2 0.200 µm squares;[^pdk-periph] via heights 0.27 µm and 0.42 µm, `met2` 0.36 µm[^pdk-04] |
| First MiM capacitor, metal 3 and via 3 | {ref}`CAPILD <step-135>` – {ref}`WCMP5 <step-148>` | 14 | 3 (`CAPM`, `MM3`, `VIM3`) | 2 fF/µm², top plate 5.8 Ω/sq;[^pdk-07] `met3` 0.845 µm and via-3 height 0.39 µm;[^pdk-04] 47 mΩ/sq;[^pdk-08] `CAPM` not marked as used in SKY130[^pdk-05] |
| Metal 4, second MiM capacitor, via 4 and metal 5 | {ref}`WTIAL4 <step-149>` – {ref}`MM5E <step-163>` | 15 | 4 (`CAP2M`, `MM4`, `VIM4`, `MM5`) | `met4` 0.845 µm, via-4 height 0.505 µm, `met5` 1.26 µm;[^pdk-04] via 4 0.800 µm square, metal 5 1.600 µm width and space;[^pdk-periph] no tungsten-plug steps after via 4[^steps-sheet] |
| Passivation, pads, alloy and test | {ref}`NFUSOX <step-164>` – {ref}`HPETEST <step-171>` | 8 | 2 (`NSM`, `PDM`) | "TOPOX K=3.9" 0.09 µm and "TOPNIT K=7.5" 0.54 µm;[^pdk-04] `pad` "Passivation cut (opening over pads)";[^pdk-06] e-test against "EDR (e-test)" specifications[^pdk-07] |

The narrative below walks through the modules. Numbers already in the
table are not repeated. The order of the steps is the step list's;
wherever a description goes further — naming a film, a species or the
purpose of a step — it is the reading of the step page linked, which
gives its public basis and marks what is inferred.

**Starting material, isolation and deep N-well.** The wafer enters as
bare p-type silicon — the stack diagram labels the bottom
"p-substrate"[^pdk-04] — and the first module builds
{term}`shallow trench isolation <STI>`: a pad oxide and a nitride
{term}`hard mask` ({ref}`BOX <step-002>`, {ref}`ISONIT <step-003>`), the
first mask ({ref}`FOM <step-004>`, which on this reference's reading
also prints the alignment marks for later levels), a nitride etch and a
silicon trench etch, a liner oxidation, an oxide fill, a polish that
stops on the nitride, and the nitride strip ({ref}`STINITE <step-005>`
to {ref}`NS19 <step-013>`). The step list places the deep N-well mask,
implant and strip ({ref}`DNM <step-007>` to {ref}`DNIS <step-009>`)
between the trench etch and the liner oxidation. On the {ref}`DNM <step-007>`
page's reading, the implant therefore enters through open trenches and is
driven by the heat of the isolation module (inference); that page also sets
out why that order may have been
chosen, as inferences. No trench depth is public; the {ref}`STIE <step-006>`
page reads the stack diagram as consistent with roughly 0.3 µm and
explains why the drawing cannot fix it.

**Wells and threshold implants.** Five masks carry ten implants. The
module opens with the low-threshold NMOS implant
({ref}`LVTNM <step-014>`, {ref}`LVTNI <step-015>`), then prints the
N-well, through whose resist this reference describes two well implants
and the PMOS channel implant ({ref}`NWM <step-017>` to
{ref}`LVTPIS <step-021>`), the high-threshold PMOS pair
({ref}`HVTPM <step-022>` to {ref}`PCHIS <step-025>`), the P-well, set by
a {term}`block mask` (the PDK has no drawn P-well layer)
({ref}`PWBM <step-026>` to {ref}`PWIS <step-029>`), and the lightly
doped P-well of the 20 V drain-extended devices
({ref}`PWDEM <step-030>` to {ref}`PWDEIS <step-033>`). A single anneal,
{ref}`RTAI <step-034>`, read on its page as activating all ten, comes
before any gate dielectric is grown. The PDK publishes the resulting well profiles, not the implants,
so the two-implant wells are read as chained {term}`retrograde wells
<retrograde well>` (inference).

**SONOS tunnel window and ONO stack.** The tunnel mask opens windows
over the channels of the memory transistors ({ref}`TUNM <step-035>`);
two implants set their channel doping ({ref}`PTSI <step-037>`,
{ref}`DEPI <step-038>`), the oxide in the windows is removed
({ref}`TUNME <step-039>`), and the {term}`ONO` stack of tunnel oxide,
{term}`charge-trapping layer` and {term}`blocking oxide` is formed over
the whole wafer ({ref}`ONO <step-040>`) and then removed from everything
except the memory cells ({ref}`ONOM <step-041>`,
{ref}`ONOME <step-042>`). The module comes before the logic gate
oxides, the order of Cypress's integration patent, in which the logic
gate oxidation has "the advantage of additionally serving to reoxidize
the ONO charge trapping dielectric stack".[^pat-03]

**Gate oxides.** SKY130 is a {term}`dual gate oxide` process. The thick
oxide is grown over every active area ({ref}`GOX100 <step-043>`); the
low-voltage oxide mask opens the 1.8 V regions ({ref}`LVOM <step-044>`),
the 1.8 V NMOS channel implant, on this reference's reading, goes in
through the thick oxide ({ref}`NCHI <step-045>`) and the oxide is stripped there
({ref}`GOXETCH <step-046>`); the thin oxide is then grown, on the {ref}`LVGOX <step-047>` page's reading
thickening the thick oxide slightly at the same time.
SkyWater lists "Nitrided gate oxide" among its special
modules;[^skw-01] whether SKY130 uses it is not stated.

**Poly gate and poly resistors.** One silicon film, read on the {ref}`SAGD <step-048>`
page as undoped amorphous silicon (inference), is deposited and doped *before* it is patterned:
an n-type gate implant everywhere except the resistor bodies
({ref}`RPM <step-049>`, {ref}`P1I <step-050>`), then p-type implants
into the 300 Ω/sq and 2000 Ω/sq resistor bodies through two further
masks ({ref}`RRPM <step-052>` to {ref}`UPRIS <step-057>`). The film is
capped with nitride and oxide ({ref}`GATENIT <step-058>`,
{ref}`POC <step-059>`), the wafer backside is cleared
({ref}`BFR <step-060>`), the gate is printed and etched
({ref}`P1M <step-061>`, {ref}`P1ME <step-062>`) and the poly is
re-oxidised ({ref}`IOX45 <step-063>`). The PDK describes the generic
poly as "N+ doped gate poly",[^pdk-07] which, with the absence of any
P⁺ poly mask, is the basis for reading SKY130 as a
{term}`single-work-function gate <single-work-function gate>` process
(inference, {ref}`P1I <step-050>`).

**Tips and halos.** Three masks each open one transistor family for its
source/drain {term}`extension`: the 1.8 V NMOS, with an arsenic tip and a
boron {term}`halo` ({ref}`NTM <step-064>` to {ref}`ASTIS <step-067>`);
the 5 V-class NMOS, with a steeply tilted arsenic tip
({ref}`HVNTM <step-068>` to {ref}`HVASTIS <step-070>`); and the SONOS
memory transistors, with a lightly doped tip and a halo
({ref}`LDNTM <step-071>` to {ref}`LDASTIS <step-074>`). An anneal, read as a
{term}`rapid thermal anneal <RTA>`, then activates all five implants
({ref}`TIPRTAD <step-075>`; inference). The step
list has no P-tip mask or implant; where the PMOS extension is formed is
one of the open questions below.

**Spacers and source/drain.** A nitride film is deposited and etched
back into {term}`spacers <spacer>` ({ref}`SPNIT <step-076>`,
{ref}`SPE <step-077>`); the gate cap is opened where contacts will land
on poly ({ref}`NPCM <step-078>`, {ref}`NPCME <step-079>`, the
{term}`nitride cut`); an oxide is deposited, read as the PDK's "oxide
spacer" ({ref}`SPOX <step-080>`); the P⁺ source/drain mask carries, on this
reference's reading, two implants and the N⁺ mask one ({ref}`PSDM <step-081>` to
{ref}`NSDIS <step-087>`); and an anneal read as a rapid thermal activation follows
({ref}`RTAD <step-088>`). Here the front end, as this reference divides
the flow, ends.

**Pre-metal dielectric, contact silicide and local interconnect.** This
is the {term}`MOL` of this reference. A
{term}`phosphosilicate glass <PSG>` is
deposited, polished and capped ({ref}`PSG <step-089>` to
{ref}`NCAPOX <step-091>`) and annealed a second time
({ref}`RTAD2 <step-092>`). The local-interconnect contacts are printed
and etched ({ref}`LICM1 <step-093>`, {ref}`LICM1E <step-094>`), cleaned
and annealed ({ref}`SACETCH <step-095>`, {ref}`ALLY1 <step-096>`), lined
with Ti/TiN and silicided at their bottoms ({ref}`TI/TIN1 <step-097>`,
{ref}`CSIL <step-098>`), and filled with tungsten that is polished back
into {term}`plugs <W plug>` ({ref}`WDEP <step-099>`,
{ref}`WCMPLI <step-100>`). A titanium-nitride film is deposited and
patterned into the {term}`local interconnect` ({ref}`LITIN <step-101>`
to {ref}`LI1ME <step-103>`), sealed with nitride
({ref}`LINIT <step-104>`) and buried in an oxide that is polished to
thickness ({ref}`NILD2 <step-105>`, {ref}`CMPL <step-106>`). The step
list does not explain the purposes of the second anneal, the
"sacrificial" etch or the alloy before metal; the step pages give
readings.

**Metal contact and metal 1.** The first back-end level repeats a
pattern that recurs up the stack. Contact holes are printed, etched,
lined with TiN, filled with tungsten and polished ({ref}`CTM1 <step-107>`
to {ref}`WCMP2 <step-111>`); the metal stack is sputtered, printed and
etched ({ref}`TIAL6 <step-112>` to {ref}`MM1E <step-114>`); and the
{term}`inter-metal dielectric` is deposited, polished and capped
({ref}`NILD3 <step-115>` to {ref}`NCAPOX3 <step-117>`). Cypress reports
for the S8 technologies at the same fab describe a Ti/Al–Cu/TiW stack
and its later change "from Ti/AlCu/TiW to
Ti/TiN/AlCu/Ti/TiN";[^cyp-qtp-113005][^cyp-qtp-123907] which of the two
SKY130 carries at any level is not public, and the evidence is set out
under {ref}`overview-metal-cap`.

**Via 1, metal 2 and via 2.** Via 1 and via 2 each take the five steps
of mask, etch, TiN liner, tungsten fill and tungsten polish
({ref}`VIM <step-118>` to {ref}`WCMP3 <step-122>`,
{ref}`VIM2 <step-129>` to {ref}`WCMP4 <step-133>`), and metal 2 the
same deposition, mask, etch, dielectric, polish and cap sequence as
metal 1 ({ref}`TIAL12 <step-123>` to {ref}`NCAPOX4 <step-128>`). The
module ends with the deposition of the metal-3 stack
({ref}`WTIAL3 <step-134>`), which stays unpatterned while the first
capacitor is built on it.

**First MiM capacitor, metal 3 and via 3.** The PDK describes the
capacitor as "constructed using a thin dielectric over metal, followed
by a thin conductor layer on top of the dielectric".[^pdk-07] The
dielectric and the top-plate film are deposited on the blanket metal 3
({ref}`CAPILD <step-135>`, {ref}`CAPTIW1 <step-136>`), the plates are
printed and etched ({ref}`CAPM <step-137>`, {ref}`CAPME <step-138>`), and
only then is metal 3 patterned, cutting the bottom plates with the
wiring ({ref}`MM3 <step-139>`, {ref}`MM3E <step-140>`). The dielectric's
material and thickness and the plate's material are not public; the
step pages read a {term}`PECVD` {term}`oxynitride` and a TiW plate (inference). The
dielectric, polish, cap and via-3 module follow
({ref}`NILD5 <step-141>` to {ref}`WCMP5 <step-148>`), with vias landing
both on metal 3 and on capacitor plates.

**Metal 4, second MiM capacitor, via 4 and metal 5.** The second
capacitor repeats the first on metal 4 ({ref}`WTIAL4 <step-149>` to
{ref}`MM4E <step-155>`); the PDK says "The constructions are identical,
and the capacitors may be stacked to maximize total
capacitance".[^pdk-07] After the via-4 dielectric
({ref}`NILD6 <step-156>` to {ref}`NCAPOX6 <step-158>`) the step list
goes straight from the via-4 mask and etch ({ref}`VIM4 <step-159>`,
{ref}`VIM4E <step-160>`) to the metal-5 stack
({ref}`WTIAL5 <step-161>`), with no liner, tungsten or polish steps in
between;[^steps-sheet] the step pages read the 0.8 µm vias as filled
by the metal-5 aluminium (inference). Metal 5 is then printed and
etched ({ref}`MM5 <step-162>`, {ref}`MM5E <step-163>`).

**Passivation, pads, alloy and test.** A thin oxide is deposited over
metal 5 ({ref}`NFUSOX <step-164>`, read as the diagram's TOPOX), a ring
along each die edge is opened ({ref}`NSM <step-165>`,
{ref}`NSME <step-166>`, read as a {term}`seal-ring <seal ring>` opening for the nitride), the
passivation nitride is deposited ({ref}`NTSD <step-167>`), the pads are
opened ({ref}`PDM <step-168>`, {ref}`PDME <step-169>`), the wafer
receives a final {term}`alloy anneal` ({ref}`ALLY <step-170>`) and the
{term}`e-test` structures are measured ({ref}`HPETEST <step-171>`).

(overview-metal-cap)=
## The metal cap and barrier question

Every aluminium level of this flow is described on its step page as a
sandwich: a thin refractory film under the aluminium–copper alloy, and a
thin refractory film over it. The under-layer is a diffusion barrier and
a wetting layer over the plug and via floors; the over-layer, the
{term}`cap <anti-reflective cap>`, is the {term}`ARC` for the metal
lithography, the {term}`hillock` suppressor, and — at every level but
the top — the film that the via etch above it lands on. Which refractory
films these are is not public for SKY130, and two different answers are
on the public record for the fab that runs it. This section sets both
out; the pages that depend on the choice link here rather than repeating
the argument.

### The two stacks

**The TiW stack.** A January 2013 Cypress qualification plan for a 64 K
serial nvSRAM family describes the technology as "S8TNV-5R", the fab as
"Cypress Semiconductor -- Bloomington, MN", the wafer process as
"Fab4 / S8TNV-5" and the design rule as "S8TNV-5R/0.13m", and gives
"Metal 1: 100A Ti / 3200A Al -0.5%Cu / 300A TiW", the same for metal 2,
and "Metal 3: 150A Ti / 7200A Al -0.5%Cu / 300A TiW".[^cyp-qtp-113005]
Two reports for older technologies at the same fab show the sandwich's
lineage: a 0.18 µm
derivative with "Metal 1: 150Å Ti / 4,200Å Al / 300Å TiW" and
"Metal 3: 150Å Ti / 8,000Å Al / 300Å TiW",[^cyp-qtp-014807] and a 0.42 µm
process with "TiW, AlCu, TiW / 500A, 6000A, 300A".[^cyp-qtp-030204]

**The TiN stack.** A March 2014 Cypress report records three
qualifications at the same fab, all of them changes away from that
sandwich:[^cyp-qtp-123907]

> 123907 Qualification of S8DI Technology Metal Stack Change from
> Ti/AlCu/TiW to Ti/TiN/AlCu/Ti/TiN in CMI Fab 4 — June 2013
>
> 132302 Qualification of S8TNV Technology Metal Stack Change from
> Ti/AlCu/TiW to Ti/TiN/AlCu/Ti/TiN in CMI Fab 4 — July 2013
>
> 132301 Qualification of S8P Metal Stack Change from Ti/AlCu/TiW to
> Ti/TiN/ALCu/Ti/TiN, excluding top metal layers — Feb 2014

The report's only process description is the S8DI one ("Die Fab Line
ID/Wafer Process ID: S8DIN-5R", "1P3M, 0.15 um"), and it gives
"Metal 1: 150A Ti/250A TiN/3200A Al 0.5% Cu/90A Ti/500A TiN", the same
for metal 2, and "Metal 3: 500A TiW/21,250A Al 0.5% Cu/300A
TiW".[^cyp-qtp-123907] The customer notification that carries the report
puts the change in plain words: it "aligns our internal Cypress
Minnesota process, Titanium Tungsten (TiW) based metal stack, with the
industry-wide Best Known Method Titanium Nitride (TiN) based metal
stack", for the "130nm SONOS Product Families", effective from its date
of 2014-03-13, and says the integration "is tuned to ensure that there
are no electrical changes".[^cyp-pin145273]

Three things follow from the reports themselves.

* The 2013 report describes **S8TNV-5R**, a three-metal 0.13 µm sibling
  of S8P, and not S8P — and that technology's own stack was qualified
  away from TiW in July 2013, six months after the report was
  issued.[^cyp-qtp-113005][^cyp-qtp-123907] It is a description of the
  fab's metallisation as it stood before the change, not of SKY130's.
* The only line in the public record that speaks about **S8P** — the
  family this reference reads SKY130 as, since the PDK's *Background*
  page lists "5 levels of metal (p - penta)" and its via-3 rules are
  headed "Via3 connects met3 to met4 in the
  SKY130Q\*/SKY130P\*/SP8Q/SP8P\* flow"[^pdk-02][^pdk-periph] — says
  that its metal stack changed in February 2014, six years before the
  first SKY130 MPW wafers, with an exclusion for "top metal
  layers".[^cyp-qtp-123907]
* The one worked example of that exclusion, in the same document, is
  S8DI's metal 3: the two thin levels take the five-film TiN stack while
  the 2.125 µm top level keeps TiW **both** under and over the
  aluminium.[^cyp-qtp-123907] Note also that the aluminium is 3 200 Å in
  the 2013 S8TNV-5R metal-1 recipe and in the 2014 S8DI one, so across
  the two reports the film total differs — 3 600 Å against 4 190 Å (our
  arithmetic) — while the conductor thickness does not; that is what
  "no electrical changes"[^cyp-pin145273] would require. The 2014 report
  does not print S8DI's pre-change stack, so this is a comparison across
  two technologies and not a before-and-after within
  one.[^cyp-qtp-113005][^cyp-qtp-123907] Note further that the S8DI
  qualification line carries **no** exclusion clause — it reads simply
  "Qualification of S8DI Technology Metal Stack Change from Ti/AlCu/TiW
  to Ti/TiN/AlCu/Ti/TiN in CMI Fab 4" — and yet that technology's top
  metal still stands at "500A TiW/21,250A Al 0.5% Cu/300A
  TiW".[^cyp-qtp-123907] Keeping TiW on a thick top level was therefore
  the fab's practice even where the wording of the qualification does
  not say so. That cuts both ways for this reference, and strengthens
  both of its readings: it makes it more likely that the S8P exclusion
  does mean the top level kept TiW, and more likely that the thin levels
  genuinely moved (inference).

### Which levels are "top metal layers"

Nothing public says. "Layers" is plural, and two readings survive:

* it is plural because the sentence covers several S8P sub-flows — the
  PDK's assumptions table gives both a 1.2 µm and a 2 µm metal 5 for
  S8P\*/SP8P\*[^pdk-03] — each with one top level, in which case only
  metal 5 kept TiW and metals 1 to 4 moved to the TiN stack; or
* it is plural because more than one level of a five-metal flow is
  excluded, in which case the thick upper levels kept TiW as S8DI's did.

On this reference's reading of SKY130 as a five-metal S8P flow, metal 3
and metal 4 are **not** top metal layers: a via connects each of them to
a metal level above.[^pdk-periph]

### What the PDK's own numbers do and do not settle

The PDK never names a metal film. Its *Background*, *Criteria &
Assumptions*, *Masks*, *Layers Reference*, *Device Details*, *Parasitic
Layout Extraction*, periphery and high-voltage documents, its
`gds_layers.csv` and `masks.csv` and its process stack diagram carry no
occurrence of titanium, tungsten, nitride, aluminium, "barrier", "ARC"
or "anti-reflective" in any metal-stack
context.[^pdk-02][^pdk-03][^pdk-05][^pdk-06][^pdk-07][^pdk-08][^pdk-periph][^pdk-hv][^pdk-04]
What it publishes are thicknesses, and two of them are suggestive.

* **The totals.** The stack diagram labels `metal1` and `metal2`
  0.36 µm.[^pdk-04] The 2013 Ti/Al–Cu/TiW recipe sums to exactly
  3 600 Å; the 2014 Ti/TiN/AlCu/Ti/TiN recipe sums to 4 190 Å (our
  arithmetic).[^cyp-qtp-113005][^cyp-qtp-123907] Likewise `metal3` and
  `metal4` are 0.845 µm,[^pdk-04] which is exactly the 8 450 Å of the
  0.18 µm Fab 4 derivative's "150Å Ti / 8,000Å Al / 300Å TiW" metal
  3.[^cyp-qtp-014807]
* **The differences.** The assumptions table's "thickness for antenna
  ratio calculation" is 0.8 µm for metal 3 and for metal 4 in the
  S8P\*/SP8P\* flows,[^pdk-03] against the diagram's 0.845 µm — a
  difference of 450 Å, exactly the 150 Å of titanium plus 300 Å of TiW
  that clad those Cypress stacks.[^cyp-qtp-014807] The 2014 stack's
  cladding is 150 + 250 + 90 + 500 = 990 Å, more than twice as much, and
  cannot be reconciled with a 450 Å difference at any aluminium
  thickness (our arithmetic).[^cyp-qtp-123907]

Both are inferences, and both carry counter-checks that this reference
records rather than suppresses. The obvious objection to the second —
that 0.8 is only 0.845 rounded — is answerable from the same table, which
writes "Metal 3 thickness for antenna ratio calculations (S8T\* other
than S8TM\*)" as 0.85 and is therefore capable of two decimals.[^pdk-03]
Against that, the same table's "Metal 1 thickness for antenna ratio
calculations (S8D\*)" of 0.35 µm, set against a 0.36 µm metal 1, leaves
only 100 Å, which fits no titanium-plus-cap cladding; so "antenna
thickness = the aluminium alone" is not a uniform rule, and that entry is
flagged for S8D\* flows rather than S8P\*.[^pdk-03][^pdk-04] Metal 5's
1.26 µm against a 1.2 µm antenna thickness leaves 600 Å, which matches
neither published cladding — S8DI's top metal is clad 500 + 300 =
800 Å (our arithmetic).[^pdk-03][^pdk-04][^cyp-qtp-123907]

A stronger objection runs the other way. That same 0.85 entry, read
against the 2013 report's S8TNV-5R metal 3 of 150 Å Ti + 7 200 Å Al +
300 Å TiW = 7 650 Å (our arithmetic), *exceeds* that stack's whole
thickness by about a tenth — on the reading, itself ours, that S8TNV
falls under "S8T\*".[^pdk-03][^cyp-qtp-113005] An antenna entry larger
than the film it describes is not derived from film thicknesses at all,
so the 450 Å coincidence at metals 3 and 4 may be exactly that. It is
recorded here as the strongest argument against the inference this
section draws from it.

What the PDK's electrical numbers do **not** do is discriminate. The
published sheet resistances — 125 mΩ/sq at metals 1 and 2, 47 mΩ/sq at
metals 3 and 4 and 29 mΩ/sq at metal 5[^pdk-08] — are set by the
aluminium, which is 3 200 Å in both the 2013 and the 2014
stack.[^cyp-qtp-113005][^cyp-qtp-123907] The claddings conduct in
parallel with it, but weakly: at 50–200 µΩ·cm for a refractory film
(typical industry values[^txt-02]), 300 Å of TiW lowers a 0.125 Ω/sq
sheet by 0.2–0.7 % and the 990 Å of the 2014 cladding by 0.6–2.4 %, so
the two differ from each other by 0.4–1.7 % (our arithmetic) — smaller
than the discrepancy in the aluminium's own resistivity that
{ref}`TIAL6 <step-112>` records, where 125 mΩ/sq over 3 200 Å implies
about 4.0 µΩ·cm against the ≈3 µΩ·cm typical of sputtered
Al–0.5%Cu.[^pdk-08][^txt-02] Neither does
SkyWater's capability list discriminate: its {term}`PVD` films include
"Aluminum both pure and Cu doped", "TiW", "ESC TiN", "Imp TiN" and
"Collimated Ti", and both metal etchers are qualified for "Al, TiW,
TiN",[^skw-01] so the fab as publicly described can build and etch either
stack. The one public SKY130 talk that names titanium nitride names it as
the {term}`local interconnect`, not as a metal cap.[^ann-16]

The step list is not evidence either way. It carries "TiW" in the name
of every aluminium deposition and of both capacitor-plate depositions,
and describes step 149 as "Al Cu 2/TiW deposition".[^steps-sheet] Under
this reference's own rule a step name is evidence of what the sheet
calls the step, not of the films it deposits, so those names are not
counted here; {ref}`WTIAL4 <step-149>` sets the point out for its own
step.

(overview-metal-cap-reading)=
### The reading used in this reference

| Level | What the step pages describe | Basis and confidence |
|---|---|---|
| Metal 1, metal 2 | Both stacks; the recipes are written for the TiW one | Genuinely undecided. The 2014 change is positive evidence about the fab's own 130 nm stack and no published exclusion covers the thin levels; against that, the diagram's 0.36 µm matches the TiW sum exactly and not the TiN sum. **Low confidence either way** |
| Metal 3, metal 4 | Both stacks; the recipes are written for the TiW one | Undecided. The 450 Å difference favours a two-film cladding, with the counter-checks above; but metals 3 and 4 are not top metal on this reference's reading, so the February 2014 exclusion need not reach them. **Low confidence** |
| Metal 5 | A TiW-capped stack | On the reading that SKY130's metal 5 is a "top metal layer", the February 2014 change did not touch it, and the worked example in the same report keeps TiW above and below a thick top metal.[^cyp-qtp-123907] **Moderate confidence** |

Where a statement is true of either stack — that the cap is a refractory
film, that it is an anti-reflective surface, that the via etch must land
on it without punching through, that the metal etch has to break through
it before reaching the aluminium — the step pages say so without naming a
film. Where the choice changes the answer, both cases are given. These
are the places where it changes the answer.

* **What the capacitor-plate etch can stop on.** The MiM top plate sits
  on a thin dielectric on the unpatterned metal below. If that metal's
  cap is the same refractory film as the plate, an etch that cleared the
  dielectric would have no selective layer left to stop on; if the cap
  and the plate are different films, a through-etch has a stop — which is
  what the Philips process does, where "the etch is controlled to stop in
  the TiN ARC film that coats the M5 layer and forms the bottom
  electrode"[^pat-mim-philips] ({ref}`CAPME <step-138>`,
  {ref}`CAP2ME <step-153>`).
* **The via landing layer.** Vias 1 to 4 land on the cap of the metal
  below. Both films etch in fluorine to volatile fluorides, so a
  fluorine-rich over-etch thins either; but it is a TiN floor that the
  contemporaneous patents describe and measure. Texas Instruments'
  etch-stop patent says that "TiN may be used as the via etch stop and
  ARC layer over the interconnect conductor or the top electrode in
  memory cells, but its etch selectivity to oxide is only 30:1", and
  measures 28.4:1 for an Ar/CF₄/CHF₃ etch; nothing public gives the
  corresponding figure for TiW.[^pat-etchstop-ti] So on a TiN cap the
  margin is the one that patent calls insufficient for long over-etches,
  and on a TiW cap it is not public at all ({ref}`VIME <step-119>`,
  {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`,
  {ref}`VIM4E <step-160>`).
* **The metal-etch breakthrough.** A chlorine-based aluminium etch must
  first open the cap. Liu and Kuo etched TiW in CF₄/O₂, CF₄/Cl₂ and
  CF₄/HCl and report that "Both F and Cl are effective etchants for the
  titanium tungsten film";[^liu-2007-tiw] Min et al. characterise TiN
  removal in a Cl₂/Ar plasma.[^min-2008] (The selectivity figures the
  two literatures publish are not directly comparable — TiW against
  nitride in a CF₄-based plasma, TiN against oxide in a
  chlorine-majority one — so they bear on the chemistry, not on which
  cap is present.) Either cap can therefore be
  opened on the same etcher, but a TiW cap is usually opened with a
  fluorine step and a TiN cap can be cleared in the chlorine chemistry
  that follows it ({ref}`MM1E <step-114>`, {ref}`MM3E <step-140>`,
  {ref}`MM5E <step-163>`).
* **Anti-reflective behaviour.** Both films are used as ARCs on
  aluminium at 365 nm and at 248 nm and neither is as good as an organic
  {term}`BARC`; their optical constants differ, so the resist thickness
  at the swing-curve minimum differs ({ref}`MM1 <step-113>`,
  {ref}`MM4 <step-154>`).
* **Which targets and gases the fab needs.** A TiW cap needs a Ti:W
  target and a fluorine-bearing breakthrough; a Ti/TiN stack needs a
  titanium target and nitrogen for reactive sputtering. SkyWater lists
  both kinds of film,[^skw-01] so its public capability list settles
  nothing ({ref}`sputter targets <material-sputter-targets>`,
  {ref}`etch gases <material-etch-gases>`).
* **Thickness arithmetic.** Any sum that uses "300 Å of TiW" as the cap
  — a via over-etch budget, a breakthrough time, a pad-etch depth — is a
  sum over the 2013 stack, not over the 2014 one, whose cap is 500 Å of
  TiN over 90 Å of titanium.[^cyp-qtp-123907]

### What would settle it

A public SKY130 or S8P process description that names the metal films; a
SkyWater or Cypress document that says which levels of a five-metal S8P
flow the February 2014 exclusion covers; a published cross-section or
materials analysis of a SKY130 die; or a PDK release that adds film
materials to the process stack diagram. None of these is public.

(overview-cross-section)=
## A simplified cross-section

The most complete public drawing of the SKY130 stack is the PDK's
process stack diagram.[^pdk-04] It is marked "(Diagram not to scale!)" and labels
each conductor with a thickness, each dielectric with a name and a
relative permittivity ("K"), some dielectric intervals with a height,
and some interfaces with a level above the diagram's zero, whose datum
the drawing does not state (the {ref}`STIE <step-006>` page reads it as
the trench floor). Reading it from the bottom up, with the step pages:

* **Silicon.** A p-type bulk wafer ("p-substrate" on the
  diagram[^pdk-04]) carries the N-wells, P-wells and deep N-wells of the
  well module and the shallow source/drain junctions, 0.1 µm deep in the
  PDK's assumptions.[^pdk-03] The field between active areas is the STI
  oxide, "FOX K=3.9", which stands 0.07 µm above the silicon under
  poly.[^pdk-04][^pdk-03]
* **Transistors.** On the active silicon lie the gate oxides (and, in
  the memory cells, the ONO stack, which the diagram does not draw), the
  0.18 µm poly gate with its nitride/oxide cap, and the sidewall
  spacers, labelled "SPNIT K=7.5".[^pdk-04]
* **Middle of line.** A phosphosilicate glass ("PSG K=3.9") buries the
  transistors; tungsten-filled `licon` contacts pass through it to the
  titanium-nitride local interconnect `li`, which is capped by the
  "LINT K=7.3" nitride and buried in "NILD2 K=4.05".[^pdk-04]
* **Back end.** Five aluminium levels alternate with oxide dielectrics
  "NILD3" to "NILD6", with tungsten plugs (`mcon`, `via1`–`via3`) and the
  wider via 4 between them; the two capacitor plates `capm` and `cap2m`
  sit in the dielectric above metal 3 and metal 4.[^pdk-04]
* **Passivation.** A thin "TOPOX K=3.9" oxide and a thicker "TOPNIT
  K=7.5" nitride cover metal 5, with a "glass cut" over the pad, and a
  polyimide "PI1 K=2.94" is drawn on top.[^pdk-04] The step list has no
  polyimide step, although SkyWater's S130 table gives polyimide
  "Yes".[^skw-02]

The table lists the levels bottom to top with the thicknesses and
heights the step pages quote. Dielectric heights are the diagram's
labels for the intervals between conductors, not deposited thicknesses;
where no number is given, none is public.

| Level (bottom to top) | PDK name or description | Thickness quoted | Level on the diagram (µm) | Built at |
|-----------------------|-------------------------|------------------|---------------------------|----------|
| Substrate and wells | "p-substrate";[^pdk-04] "Bulk"[^skw-02] | N-well baseline vertical dimension 1.1 µm; P-well 0.75 µm; S/D junction 0.1 µm[^pdk-03] | — | {ref}`SMAT <step-001>`; {ref}`LVTNM <step-014>` – {ref}`RTAI <step-034>`; {ref}`PSDM <step-081>` – {ref}`RTAD <step-088>` |
| Field oxide | "FOX K=3.9"[^pdk-04] | 0.07 µm above the silicon under poly[^pdk-03] | top 0.3262[^pdk-04] | {ref}`BOX <step-002>` – {ref}`NS19 <step-013>` |
| Gate dielectrics | thin and thick gate oxide; ONO in SONOS cells | 110 Å (5 V and high-voltage devices);[^pdk-hv] model `toxe` 4.148 nm (1.8 V) and 11.6 nm (5 V);[^pdk-model-nfet01v8][^pdk-model-nfet5v] ONO not public | — | {ref}`ONO <step-040>`; {ref}`GOX100 <step-043>` – {ref}`LVGOX <step-047>` |
| Gate and resistor poly | "polysilicon"[^pdk-04] | 0.18 µm[^pdk-03][^pdk-04] | — | {ref}`SAGD <step-048>` – {ref}`P1ME <step-062>` |
| Gate cap and spacers | "SPNIT K=7.5"[^pdk-04] | "poly cap after SPE" 0.2 µm; "oxide spacer" 0.05 µm[^pdk-03] | — | {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`; {ref}`SPNIT <step-076>` – {ref}`SPOX <step-080>` |
| Pre-metal dielectric | "PSG K=3.9"[^pdk-04] | 0.6099 µm from the field-oxide top to the `li` bottom and 0.4299 µm from the field-poly top to the `li` bottom;[^pdk-04] "Pre-LI ILD thickness" 0.5 µm[^pdk-03] | — | {ref}`PSG <step-089>` – {ref}`NCAPOX <step-091>` |
| Local interconnect | `li` (TiN[^ann-16]) | 0.1 µm[^pdk-04][^pdk-03] | bottom 0.9361[^pdk-04] | {ref}`LITIN <step-101>` – {ref}`LI1ME <step-103>` |
| Local-interconnect cap | "LINT K=7.3"[^pdk-04] | 0.075 µm[^pdk-04] | 1.0111, read as its top beside `li` (see below)[^pdk-04] | {ref}`LINIT <step-104>` |
| Dielectric to metal 1 (`mcon`) | "NILD2 K=4.05"[^pdk-04] | 0.265 µm[^pdk-04] | — | {ref}`NILD2 <step-105>` – {ref}`WCMP2 <step-111>` |
| Metal 1 | `metal1` | 0.36 µm[^pdk-04] | bottom 1.3761[^pdk-04] | {ref}`TIAL6 <step-112>` – {ref}`MM1E <step-114>` |
| Via 1 | "NILD3 K=4.5", "NILD3_C K=3.5"[^pdk-04] | via 0.27 µm; NILD3_C 0.030 µm[^pdk-04] | — | {ref}`NILD3 <step-115>` – {ref}`WCMP3 <step-122>` |
| Metal 2 | `metal2` | 0.36 µm[^pdk-04] | bottom 2.0061[^pdk-04] | {ref}`TIAL12 <step-123>` – {ref}`MM2E <step-125>` |
| Via 2 | "NILD4 K=4.2", "NILD4_C K=3.5"[^pdk-04] | via 0.42 µm; NILD4_C 0.030 µm[^pdk-04] | — | {ref}`NILD4 <step-126>` – {ref}`WCMP4 <step-133>` |
| Metal 3 | `metal3` | 0.845 µm[^pdk-04] | bottom 2.7861[^pdk-04] | {ref}`WTIAL3 <step-134>`, {ref}`MM3 <step-139>`, {ref}`MM3E <step-140>` |
| First MiM capacitor | `capm`[^pdk-04] | not labelled;[^pdk-04] 2 fF/µm²[^pdk-07] | — | {ref}`CAPILD <step-135>` – {ref}`CAPME <step-138>` |
| Via 3 | "NILD5 K=4.1"[^pdk-04] | via 0.39 µm[^pdk-04] | — | {ref}`NILD5 <step-141>` – {ref}`WCMP5 <step-148>` |
| Metal 4 | `metal4` | 0.845 µm[^pdk-04] | bottom 4.0211[^pdk-04] | {ref}`WTIAL4 <step-149>`, {ref}`MM4 <step-154>`, {ref}`MM4E <step-155>` |
| Second MiM capacitor | `cap2m`[^pdk-04] | not labelled;[^pdk-04] 2 fF/µm²[^pdk-07] | — | {ref}`CAPILD2 <step-150>` – {ref}`CAP2ME <step-153>` |
| Via 4 | "NILD6 K=4.0"[^pdk-04] | via 0.505 µm[^pdk-04] | — | {ref}`NILD6 <step-156>` – {ref}`VIM4E <step-160>` |
| Metal 5 | `metal5` | 1.26 µm[^pdk-04] | bottom 5.3711[^pdk-04] | {ref}`WTIAL5 <step-161>` – {ref}`MM5E <step-163>` |
| Passivation oxide | "TOPOX K=3.9"[^pdk-04] | 0.09 µm on the metal, 0.070 µm on its sidewall[^pdk-04] | — | {ref}`NFUSOX <step-164>` |
| Passivation nitride | "TOPNIT K=7.5"[^pdk-04] | 0.54 µm on the metal, 0.4223 µm on its sidewall[^pdk-04] | — | {ref}`NTSD <step-167>` |
| Polyimide | "PI1 K=2.94"[^pdk-04] | — | top 11.8834[^pdk-04] | no step in the step list |

Most of the labels are consistent with one another. From metal 1
upwards each metal bottom equals the one below plus that metal's
thickness plus the via height (1.3761 + 0.36 + 0.27 = 2.0061 µm, and so
on to 4.0211 + 0.845 + 0.505 = 5.3711 µm), and the PSG labels equal the
distance from the field-oxide top to the `li` bottom (0.9361 − 0.3262 =
0.6099 µm) and that distance less the 0.18 µm poly (0.4299 µm) (our
arithmetic from the labels[^pdk-04]). Below metal 1 the labels add up
too: the `li` bottom (0.9361 µm) plus the 0.1 µm `li`, the 0.075 µm LINT
and the 0.265 µm NILD2 gives exactly the 1.3761 µm metal-1 bottom (our
arithmetic from the labels[^pdk-04]). One label does not fit that
reading. The 1.0111 µm level is 0.075 µm above the `li` bottom, not
0.1 µm; the diagram, being not to scale, draws the top of `li` and the
top of the LINT on the glass beside it at the same height, and the
label's leader line runs to the LINT rather than to `li`. We therefore
read 1.0111 µm as the top of the LINT beside `li` (0.9361 + 0.075 µm),
which fits every other label and leaves 0.34 µm from the `li` top to
metal 1 (our reading of the drawing[^pdk-04]; the
{ref}`LITIN <step-101>`, {ref}`NILD2 <step-105>`, {ref}`CTM1 <step-107>`
and {ref}`CTME <step-108>` pages follow it). The public values for some films also disagree with other public
sources; those differences are among the open questions below.

(overview-phases)=
## Front end, middle of line and back end

Every step page's summary table gives the step a phase and a module
name. The boundaries are this reference's, drawn where the kind of work
changes:

| Phase | Steps | Number of steps | Modules as named on the step pages |
|-------|-------|-----------------|------------------------------------|
| {term}`FEOL` | {ref}`SMAT <step-001>` – {ref}`RTAD <step-088>` | 88 | isolation; wells and channel implants; SONOS and gate dielectrics; gate and poly resistors; extensions, spacers, source/drain |
| {term}`MOL` | {ref}`PSG <step-089>` – {ref}`CMPL <step-106>` | 18 | silicide and local interconnect |
| {term}`BEOL` | {ref}`CTM1 <step-107>` – {ref}`HPETEST <step-171>` | 65 | contact and metal 1; via 1, metal 2, via 2; MiM capacitors, metal 3–5, via 3–4; passivation, pads, alloy, test |

The front end ends with the last source/drain anneal, when every
junction is in place. The middle of line runs from the pre-metal glass
to the polished dielectric over the local interconnect, so it contains
the first contacts (`licon`) and the local interconnect itself. The back
end starts with the metal-contact mask and, in this reference, includes
the passivation, the final alloy and electrical test. Two consequences
of these choices are worth knowing when comparing with other sources:
in common usage the back end runs from the first contact through the
final passivation, whereas this reference counts the first contact
level as middle of line; and general descriptions place wafer testing
after the back end, whereas this reference files
{ref}`HPETEST <step-171>` under BEOL. The {ref}`glossary` and the
{ref}`test category page <category-test>` state both. The deposition of the metal-3 stack,
{ref}`WTIAL3 <step-134>`, is also filed with via 2 rather than with the
capacitor and metal-3 steps that follow it.

### Thermal budget

The order of a CMOS flow is set largely by {term}`thermal budget`: once a
junction or film is in place, every later step must stay within what it
tolerates, so the hottest steps broadly come first and the flow cools
as it goes. The step list gives no temperatures, and SKY130's are not public;
the values below are typical ones from the category pages and their
sources, in the order in which the thermal steps occur.

1. **Isolation.** The pad and liner oxidations ({ref}`BOX <step-002>`,
   {ref}`LINOX <step-010>`) and the nitride hard mask
   ({ref}`ISONIT <step-003>`) are read on their step pages as furnace steps: thermal oxidation runs
   at 800–1200 °C[^wiki-thox] and {term}`LPCVD` nitride at roughly
   700–800 °C (typical value),[^txt-02] a tube-furnace process that
   Wikipedia describes as working "at rather high
   temperature".[^wiki-sin] On the
   {ref}`DNM <step-007>` page's reading, this heat also drives the deep
   N-well implanted just before the liner oxidation.
2. **Well anneal.** {ref}`RTAI <step-034>` activates the ten well and
   channel implants at once; the step page reads it as a rapid thermal
   anneal, for which seconds at 1000–1100 °C is typical.[^stolk-1997]
3. **SONOS stack.** One embodiment of a Cypress ONO patent forms all
   three layers at temperatures "from about 700° C. to about 875° C."
   ({ref}`ONO <step-040>`).[^pat-01]
4. **Gate oxides.** Gate oxides of this era are typically grown dry at
   750–950 °C ({ref}`GOX100 <step-043>`,
   {ref}`LVGOX <step-047>`);[^txt-01] in Cypress's integration patent the
   logic gate oxidation also re-oxidises the ONO.[^pat-03]
5. **Gate film.** Silicon deposited at low temperature and at a rate
   above the critical value is amorphous (typical value; the
   amorphous/polycrystalline boundary depends on rate as well as
   temperature);[^voutsas-1992] the
   {ref}`SAGD <step-048>` page reads
   SKY130's gate film as amorphous from SkyWater's "LPCVD polysilicon
   (undoped), both amorphous and crystalline"[^skw-01] (inference); the caps and the post-etch re-oxidation
   ({ref}`GATENIT <step-058>`, {ref}`POC <step-059>`,
   {ref}`IOX45 <step-063>`) follow, at conditions that are not public.
6. **Junction anneals.** Rapid thermal anneals follow the tip and
   source/drain implants ({ref}`TIPRTAD <step-075>`,
   {ref}`RTAD <step-088>`), and a second one follows the polished glass
   ({ref}`RTAD2 <step-092>`, whose two possible purposes — a final
   source/drain anneal or a dielectric anneal — the step page
   discusses as inferences); a soak of
   1000–1050 °C for a few seconds, or a spike, is the typical 130 nm-era
   choice.[^txt-05][^txt-10] After them the junctions — 0.1 µm deep in
   the PDK's assumptions[^pdk-03] — must not move, and every later step
   is cooler (inference from the order).
7. **Contact module.** An anneal that the step page reads as a
   hydrogen-bearing alloy anneal, typically 350–450 °C,[^txt-02] precedes
   the contact liner ({ref}`ALLY1 <step-096>`), and the anneal read as the
   contact silicidation follows it ({ref}`CSIL <step-098>`); titanium disilicide is typically formed by a
   first anneal at roughly 600–700 °C and converted to its
   low-resistance phase at roughly 800–900 °C.[^maex-1993] How SKY130's
   silicidation is done is not public.
8. **Back end.** Once aluminium is on the wafer, from
   {ref}`TIAL6 <step-112>` onwards, depositions typically stay below
   about 450 °C;[^txt-02] tungsten CVD for the plugs runs at roughly
   400–450 °C (typical value),[^txt-01] the low end of the "300 and
   800 °C" that Wikipedia gives for hydrogen reduction of
   WF₆.[^wiki-wf6] The oxide, nitride and
   capacitor films of the back end are described on their step pages as
   low-temperature plasma depositions (inference).
9. **Final alloy.** The last heat is the alloy anneal
   ({ref}`ALLY <step-170>`), read as a {term}`forming-gas <forming gas>` anneal, typically
   350–450 °C.[^txt-02] In the
   `sky130B` variant every thermal step after the ReRAM stack is also
   seen by its 5 nm switching oxide (0.005 µm in the ReRAM tech file,
   {ref}`overview-sky130b-reram`).

(overview-open-questions)=
## Key open questions

Every step page ends with what it could not confirm. The questions
below are those that affect several steps or the picture of the process
as a whole; each links to the pages where the evidence is set out.
Across the whole flow, no implant species, energy or dose beyond the
PDK's tables, and no deposition, etch or anneal condition of SKY130 is
public.

* **PMOS gate doping.** The PDK calls the generic poly "N+ doped gate
  poly",[^pdk-07] its mask table has no separate P⁺ poly
  mask,[^pdk-05] and its rules keep the nitride cut away from
  gates.[^pdk-periph] The step pages therefore read both NMOS and PMOS
  gates as n⁺ poly, with a {term}`counter-doped <counter-doping>` PMOS channel; no public source
  says so ({ref}`P1I <step-050>`, {ref}`LVTPI <step-020>`,
  {ref}`PNCHI <step-024>`).
* **PMOS source/drain extension.** The mask table has only N-tip
  masks,[^pdk-05] yet the PDK's PMOS cross-section shows P− extensions,[^pdk-07]
  its assumptions list an "HVPTM shadowing" of 0.089 µm[^pdk-03] and its
  high-voltage page says hv p-channel devices "get the extra junction
  grading implant into the ringed gate with the HVPDM mask".[^pdk-hv]
  Where the PMOS extension is formed — by the second P⁺ implant, by
  diffusion under the spacer or by a step not in the list — is open
  ({ref}`NTM <step-064>`, {ref}`PSDI <step-082>`,
  {ref}`2PSDI <step-083>`).
* **Fate of the pad oxide.** Whether the pad oxide of
  {ref}`BOX <step-002>` survives the nitride strip as the screen oxide
  for the well implants, and where it is finally removed, is not public;
  the step list contains no separate sacrificial oxidation before the
  gate oxides, and the pages from {ref}`NS19 <step-013>` to
  {ref}`GOXETCH <step-046>` depend on the answer
  ({ref}`TUNME <step-039>`, {ref}`ONOME <step-042>`).
* **Three unexplained middle-of-line steps and the silicide.** The step
  list does not explain the second source/drain anneal after the glass
  is polished, the "sacrificial" etch after the contact etch, or an alloy
  anneal before any metal is on the wafer; the step pages give readings
  ({ref}`RTAD2 <step-092>`, {ref}`SACETCH <step-095>`,
  {ref}`ALLY1 <step-096>`). That the only silicide is at the contact
  bottoms is itself an inference from the PDK's sheet
  resistances ({ref}`CSIL <step-098>`).
* **Metal cap and barrier composition.** Cypress reports for the S8
  technologies at the same fab describe a Ti/Al–Cu/TiW stack and a
  change "from Ti/AlCu/TiW to Ti/TiN/AlCu/Ti/TiN" qualified in
  2013–2014, for S8P "excluding top metal
  layers";[^cyp-qtp-113005][^cyp-qtp-123907] which stack SKY130 lots
  receive at any level is not public, nor is it public which levels of a
  five-metal S8P flow the exclusion covers. The whole of the evidence,
  the reading taken at each level and the statements that depend on it
  are set out under {ref}`overview-metal-cap`
  ({ref}`TIAL6 <step-112>`, {ref}`WTIAL3 <step-134>`,
  {ref}`WTIAL4 <step-149>`, {ref}`WTIAL5 <step-161>`).
* **Metal-3 and metal-4 thickness.** The stack diagram labels both
  0.845 µm;[^pdk-04] the antenna table gives 0.8 µm for the S8P flows and
  0.85 µm for "S8T\* other than S8TM\*";[^pdk-03] Cypress's S8TNV report
  gives "Metal 3: 150A Ti / 7200A Al -0.5%Cu / 300A TiW", which sums to
  0.765 µm;[^cyp-qtp-113005] and a 0.18 µm Fab 4 derivative's
  "150Å Ti / 8,000Å Al / 300Å TiW" metal 3 sums to exactly
  0.845 µm[^cyp-qtp-014807] (our arithmetic). The difference is not
  resolved ({ref}`MM3E <step-140>`, {ref}`MM4E <step-155>`).
* **Metal-5 thickness and via-4 fill.** Metal 5 is 1.26 µm on the stack
  diagram and in Edwards's slides,[^pdk-04][^ann-16] 1.2 µm or 2 µm by
  flow in the antenna table,[^pdk-03] and "1.2 µm" as top metal in
  SkyWater's S130 table.[^skw-02] No liner, tungsten or polish step
  follows the via-4 etch in the step list,[^steps-sheet] so the step
  pages read the 0.8 µm vias as filled by the metal-5 aluminium; no
  public source says how they are filled ({ref}`VIM4 <step-159>`,
  {ref}`WTIAL5 <step-161>`, {ref}`MM5E <step-163>`).
* **MiM capacitors.** The dielectric's material and thickness, the
  top-plate material and whether the plate etch stops on the dielectric
  are not public. The PDK is not self-consistent about the capacitors'
  level: its device page, layer table and stack diagram put `capm` over
  metal 3,[^pdk-07][^pdk-06][^pdk-04] while its `capm` rules and
  extraction entries name metal 2 and via 2,[^pdk-periph][^pdk-08] and
  `cap2m` has no rules and no mask-table entry.[^pdk-periph][^pdk-05]
  The test tile's pad documentation describes "CAPM on M3" and "CAP2M
  over M4" MiM capacitors with via-3 and via-4 chains to the
  plates,[^raw-data-testtile-pads] which agrees with the device page; see
  {ref}`CAPILD <step-135>`, {ref}`CAPME <step-138>` and
  {ref}`CAPILD2 <step-150>`.
* **Passivation thickness.** The stack diagram gives 0.09 µm of TOPOX
  and 0.54 µm of TOPNIT, 0.63 µm together;[^pdk-04] the two Cypress
  reports that give both films report 1.0 µm (1000 Å TEOS plus 9000 Å
  nitride) for the S8DI variant of S8 and, at the same fab, the 0.18 µm
  R7FT-3R technology,[^cyp-qtp-123907][^cyp-qtp-014807] and a third
  report gives 0.7 ± 0.2 µm of nitride with no oxide stated for the
  S8TNV-5R variant.[^cyp-qtp-113005] Which applies to SKY130 is
  not public, and with it the thickness the pad etch must clear
  ({ref}`NTSD <step-167>`, {ref}`PDME <step-169>`); how deep the
  nitride-seal opening goes is not public either
  ({ref}`NSME <step-166>`).
* **Stack-diagram intervals.** Besides the 1.0111 µm label described
  {ref}`above <overview-cross-section>`, what the
  thin "NILD3_C" and "NILD4_C" films represent, and why the finished
  dielectric above metal 2 is thicker than that above metal 1, are not
  public ({ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`,
  {ref}`NILD4 <step-126>`). No trench depth is public either
  ({ref}`STIE <step-006>`).
* **Masks and options.** The step list has 36 mask steps. The PDK's
  mask table marks 34 masks as used in SKY130, four of which (`HVTRM`,
  `PBO`, `CU1M`, `PMM2`) have no step, leaves `PWBM`, `PWDEM` and `CAPM`
  unmarked, and does not list `RRPM`, `URPM` or `CAP2M`
  ({ref}`masks-index`);[^pdk-05] SkyWater's S130 table gives "30 – 34"
  mask steps and gives inductor "No", where the PDK README says the
  process "Is inductor-capable".[^skw-02][^pdk-10] Which optional masks
  — MiM capacitors, drain-extended wells, ultra-high-value resistors —
  are run on a given lot is not public.

## References

### Cross-check

* SkyWater PDK, *Background* and *Previous Nomenclature* — the Cypress
  origin, "8th generation SONOS", the `s8` name and the older flow
  names.[^pdk-02][^pdk-previous]
* SkyWater PDK, repository README — the technology-stack summary and the
  licence.[^pdk-10]
* SKY130 raw-data repository, README and test-tile pad documentation —
  the CoolCAD measurements and the 273 test modules, including the MiM
  capacitor structures; the transistor, gate-capacitor, passive-device,
  varactor and bipolar files from which our extracted values
  come.[^raw-data-readme][^raw-data-testtile-pads][^raw-data-hv-mosfets][^raw-data-lv-mosfets][^raw-data-passives]
* SkyWater PDK, *Criteria & Assumptions* — poly, cap, spacer and pre-LI
  dielectric thicknesses, well and junction depths, implant angles and
  the antenna thicknesses by flow.[^pdk-03]
* SkyWater PDK, process stack diagram — every label of the
  cross-section.[^pdk-04]
* SkyWater PDK, *Masks*, *Layers Reference* and *Periphery rules* — the
  mask marks, layer descriptions and design rules behind the module
  table.[^pdk-05][^pdk-06][^pdk-periph]
* SkyWater PDK, *Device Details*, *High Voltage Methodology*, *Parasitic
  Layout Extraction* and SPICE models — the device list, capacitor and
  resistor values, gate-oxide thickness, sheet resistances and
  `toxe`.[^pdk-07][^pdk-hv][^pdk-08][^pdk-model-nfet01v8][^pdk-model-nfet5v]
* *S8 / SKY130 Process Steps* sheet — the 171 steps, their codes, names
  and order.[^steps-sheet]
* open_pdks `Makefile.in` and `README`, and the `sky130_fd_pr_reram`
  documentation index — the `sky130A` and `sky130B`
  variants.[^opdks-makefile][^opdks-readme][^reram-index]
* SkyWater, *Facilities & Capabilities* and the S130 platform table —
  the fab's equipment and the S130 platform data.[^skw-01][^skw-02]
* Cypress, 10-Q/A for Q1 2003 and PIN152804 — Fab 4 as Cypress's
  eight-inch 0.13 µm fab and S8 as a Fab 4 technology.[^cyp-07][^cyp-06]
* Cypress, sale announcement, and SkyWater, acquisition release — the
  change of ownership of the fab in 2017.[^cyp-01][^skw-10]
* Electronics Weekly (2007) and Cypress/UMC (2011) — Cypress's public use
  of the S8 name for its 0.13 µm SONOS process.[^cyp-20][^cyp-22]
* Cypress qualification reports QTP 113005, 123907 and 014807 — metal
  and passivation stacks of S8 and another technology at Fab
  4.[^cyp-qtp-113005][^cyp-qtp-123907][^cyp-qtp-014807]
* SkyWater, Form 10-K for 2023 — the other flows run in the same
  fab.[^sec-02]
* Google, SkyWater and Efabless shuttle announcement (2020) and
  SkyWater's SKY130 article (2023) — the open shuttle programme and
  SKY130 as SkyWater's volume 130 nm technology.[^ann-10][^ann-13]

### High-level understanding

* Wikipedia, *SkyWater Technology* and *130 nm process* — the company's
  origin and the 2020 open-source release.[^wiki-skywater][^ann-17]
* FOSSi Foundation, announcement of the open PDK (2020) — how the
  release was presented to the open-hardware community.[^ann-03]
* Edwards, *Introduction to the SkyWater PDK* (2021) — lecture slides on
  the layers and metal stack from a designer's point of view.[^ann-16]
* Wikipedia, *SONOS* and *Shallow trench isolation* — the memory cell and
  the isolation module in outline.[^cyp-26][^wiki-sti]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — the unit
  processes of a CMOS flow, with models.[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 — unit
  processes and their typical conditions.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 2 — process
  integration: isolation, wells, contacts, multilevel metal and
  passivation.[^txt-03]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — deep-submicron
  STI, CMP, tungsten plugs, silicides and RTP.[^txt-05]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — the
  fab-floor view of each tool class and the flow as a
  whole.[^txt-07]

### Deep dive

* ITRS 2001, *Front End Processes* — starting-material, isolation,
  gate-stack and junction targets for the 130 nm generation.[^itrs-01]
* ITRS 2001, *Process Integration, Devices, and Structures* — the
  transistor and gate-oxide targets SKY130's 1.8 V and 5 V devices can be
  compared with.[^itrs-04]
* ITRS 2001, *Interconnect* — aluminium and copper back ends and via and
  metal dimensions by node.[^itrs-02]
* Nandakumar et al., IEDM 1998 — the STI flow of
  trench, corner rounding, fill and planarisation.[^rev-01]
* Deal and Grove, *J. Appl. Phys.* 1965 — the kinetics behind every
  thermal oxidation in the flow.[^deal-1965]
* White, Adams and Bu, *IEEE Circuits and Devices* 2000 — a review of
  scaled SONOS memory.[^pap-01]
* Ramkumar et al. (Cypress), US 6,969,689 — ONO layers formed in one
  reaction chamber, with thickness and temperature ranges from several
  embodiments.[^pat-01]
* Koutny et al. (Cypress), US 8,093,128 — where a SONOS module sits
  relative to the logic wells and gate oxides.[^pat-03]
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — an
  embedded-SONOS flow with pad oxide, tunnel mask and dual gate
  oxides.[^pat-04]
* Ramkumar, Prabhakar and Kapre (Cypress), *Semiconductor Digest*
  2020 — SONOS integration cost and scaling from the 130 nm
  generation.[^cyp-25]
* Jones and Ishida, *Mater. Sci. Eng. R* 1998 — shallow-junction doping,
  extensions, halos and rapid thermal annealing.[^rev-05]
* Hori, IEDM 1989 — the large-tilt-angle implanted drain
  ({term}`LATID`), the
  construction read for SKY130's high-voltage tip.[^hori-1989-latid]
* Stolk et al., *J. Appl. Phys.* 1997 — transient enhanced diffusion,
  the reason junction anneals are short.[^stolk-1997]
* Fair (ed.), *Rapid Thermal Processing* — junction formation by rapid
  thermal annealing.[^txt-10]
* Maex, *Mater. Sci. Eng. R* 1993 — titanium and cobalt silicide
  formation.[^maex-1993]
* Zhang and Östling, *Crit. Rev. Solid State Mater. Sci.* 2003 — metal
  silicides in CMOS from titanium to nickel.[^rev-04]
* Broadbent and Ramiller, *J. Electrochem. Soc.* 1984 — the WF₆
  chemistry behind tungsten plug fill.[^rev-03]
* Rossnagel and Hopwood, *Appl. Phys. Lett.* 1993 — ionised sputter
  deposition for contact and via liners.[^rossnagel-1993]
* Krishnan, Nalaskowski and Cook, *Chem. Rev.* 2010 — slurry chemistry
  and mechanisms of oxide and tungsten CMP.[^rev-02]
* Kar-Roy et al., IITC 1999 — PECVD-nitride MiM capacitors in
  an aluminium back end.[^kar-roy-1999]
* Edwards (Efabless), WOSET 2020 — the open PDK, its process stack and
  its options, by the author of open_pdks.[^ann-15]

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
    SKY130 PDK documentation (Tables 3a, 3b, 3f and 4,
    `assumptions/04-physical.csv`).
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
[^pat-01]: K. Ramkumar, M. Rathor, B. Parameshwaran and L. Lancaster
    (Cypress Semiconductor), *Method of manufacturing an
    oxide-nitride-oxide (ONO) dielectric for SONOS-type devices*,
    US 6,969,689 B1, granted 2005-11-29.
    <https://patents.google.com/patent/US6969689B1/en>
[^pat-02]: S. Levy, K. Ramkumar, F. Jenne and S. Geha (Cypress
    Semiconductor), *Oxide-nitride-oxide stack having multiple
    oxynitride layers*, US 2009/0179253 A1, published 2009-07-16.
    <https://patents.google.com/patent/US20090179253A1/en>
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^pdk-model-nfet01v8]: SkyWater PDK Authors,
    `sky130_fd_pr__nfet_01v8__tt.pm3.spice` (typical-corner BSIM4
    model, parameter `toxe`), google/skywater-pdk-libs-sky130_fd_pr
    repository.
    <https://raw.githubusercontent.com/google/skywater-pdk-libs-sky130_fd_pr/main/cells/nfet_01v8/sky130_fd_pr__nfet_01v8__tt.pm3.spice>
[^pdk-model-nfet5v]: SkyWater PDK Authors,
    `sky130_fd_pr__nfet_g5v0d10v5__tt.pm3.spice` (typical-corner BSIM4
    model, parameter `toxe`), google/skywater-pdk-libs-sky130_fd_pr
    repository.
    <https://raw.githubusercontent.com/google/skywater-pdk-libs-sky130_fd_pr/main/cells/nfet_g5v0d10v5/sky130_fd_pr__nfet_g5v0d10v5__tt.pm3.spice>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^cyp-qtp-113005]: Cypress Semiconductor, *Product Qualification
    Plan, QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8
    Technology, CMI (Fab 4)*, document 001-85611 Rev. *A, January
    2013 (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^cyp-qtp-123907]: Cypress Semiconductor, *Fab Process Qualification
    Report, QTP# 123907, 132302, 132301: Metal Stack Change, S8
    Technology, Fab 4 CMI*, document 001-91369 Rev. **, March 2014
    (copy hosted by Tokyo Electron Device as the attachment to
    Cypress Product Information Notification PIN145273, 2014-03-13,
    which states the report is attached and available from
    cypress.com; <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>).
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/145273-Qualification_Report.pdf>
[^wiki-thox]: Wikipedia, *Thermal oxidation*.
    <https://en.wikipedia.org/wiki/Thermal_oxidation>
[^wiki-sin]: Wikipedia, *Silicon nitride*.
    <https://en.wikipedia.org/wiki/Silicon_nitride>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^stolk-1997]: P. A. Stolk, H.-J. Gossmann, D. J. Eaglesham, D. C.
    Jacobson, C. S. Rafferty, G. H. Gilmer, M. Jaraíz, J. M. Poate, H.
    S. Luftman and T. E. Haynes, "Physical mechanisms of transient
    enhanced dopant diffusion in ion-implanted silicon", *Journal of
    Applied Physics* **81**(9), 6031–6050 (1997).
    <https://doi.org/10.1063/1.364452>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^voutsas-1992]: A. T. Voutsas and M. K. Hatalis, "Structure of
    As-Deposited LPCVD Silicon Films at Low Deposition Temperatures and
    Pressures", *Journal of The Electrochemical Society* **139**(9),
    2659–2665 (1992). <https://doi.org/10.1149/1.2221280>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^txt-10]: R. B. Fair (ed.), *Rapid Thermal Processing: Science and
    Technology*, Academic Press, 1993, ISBN 978-0-12-247690-7; R. B.
    Fair, "Junction Formation in Silicon by Rapid Thermal Annealing",
    pp. 169–226. <https://doi.org/10.1016/b978-0-12-247690-7.50009-3>
[^maex-1993]: K. Maex, "Silicides for integrated circuits: TiSi₂ and
    CoSi₂", *Materials Science and Engineering: R* **11**(2–3), vii–153
    (1993). <https://doi.org/10.1016/0927-796X(93)90001-J>
[^wiki-wf6]: Wikipedia, *Tungsten hexafluoride*.
    <https://en.wikipedia.org/wiki/Tungsten_hexafluoride>
[^ann-16]: T. Edwards (Efabless), *Introduction to the SkyWater PDK —
    The New Age of Open Source Silicon*, lecture slides, 2021-10-08
    (UC San Diego BENG 207).
    <https://isn.ucsd.edu/courses/beng207/lectures/Tim_Edwards_2021_slides.pdf>
[^cyp-qtp-014807]: Cypress Semiconductor, *Technology Derivative
    Qualification Report, QTP# 014807 Version 2.0: Technology
    Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM*, June 2005
    (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
[^cyp-pin145273]: Cypress Semiconductor, *Product Information
    Notification PIN145273: Improvement of Cypress Minnesota
    Back-End-of-Line Integration for 130nm SONOS Product Families*,
    document 001-11741 Rev. *H, 2014-03-13 (copy hosted by Tokyo
    Electron Device). <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>
[^cyp-qtp-030204]: Cypress Semiconductor, *Automotive Product
    Qualification Report, QTP# 030204: 256K Static RAM Automotive
    Devices, RAM42HA Technology, Fab 4*, document 001-88023 Rev. **,
    June 2013 (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030204-256k-static-ram-automotive-devices-ram42ha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714980870ac1>
[^pat-mim-philips]: M. C. Olewine and K. F. Saiz (Koninklijke Philips
    Electronics), *Metal-insulator-metal (MIM) capacitor structure and
    methods of fabricating same*, US 6,717,193 B2, filed 2001-10-09,
    granted 2004-04-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6717193>
[^pat-etchstop-ti]: G. Xing, G. A. Cerny and M. R. Visokay (Texas
    Instruments), *Etchstop for integrated circuits*, US 6,090,697 A,
    filed 1998-06-26, granted 2000-07-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6090697>
[^liu-2007-tiw]: G. Liu and Y. Kuo, "Reactive Ion Etching of Titanium
    Tungsten Thin Films", *Journal of The Electrochemical Society*
    **154**(7), H653 (2007). <https://doi.org/10.1149/1.2737631>
[^min-2008]: S. R. Min, H. N. Cho, Y. L. Li, S. K. Lim, S. P. Choi and
    C. W. Chung, "Inductively coupled plasma reactive ion etching of
    titanium nitride thin films in a Cl₂/Ar plasma", *Journal of
    Industrial and Engineering Chemistry* **14**(3), 297–302 (2008).
    <https://doi.org/10.1016/j.jiec.2008.01.001>
[^cyp-26]: Wikipedia, *SONOS*. <https://en.wikipedia.org/wiki/SONOS>
[^wiki-sti]: Wikipedia, *Shallow trench isolation*.
    <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
[^txt-03]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 2:
    Process Integration*, Lattice Press, 1990, ISBN 978-0-9616721-4-0.
    <https://openlibrary.org/isbn/9780961672140>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^itrs-04]: International Technology Roadmap for Semiconductors, *2001
    Edition: Process Integration, Devices, and Structures*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>
[^itrs-02]: International Technology Roadmap for Semiconductors, *2001
    Edition: Interconnect*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Interconnect.pdf>
[^rev-01]: M. Nandakumar, A. Chatterjee, S. Sridhar, K. Joyner,
    M. Rodder and I.-C. Chen, "Shallow trench isolation for advanced
    ULSI CMOS technologies", *IEDM 1998 Technical Digest*, pp. 133–136.
    <https://doi.org/10.1109/IEDM.1998.746297>
[^rev-02]: M. Krishnan, J. W. Nalaskowski and L. M. Cook, "Chemical
    Mechanical Planarization: Slurry Chemistry, Materials, and
    Mechanisms", *Chemical Reviews* **110**(1), 178–204 (2010).
    <https://doi.org/10.1021/cr900170z>
[^rev-03]: E. K. Broadbent and C. L. Ramiller, "Selective Low Pressure
    Chemical Vapor Deposition of Tungsten", *Journal of The
    Electrochemical Society* **131**(6), 1427–1433 (1984).
    <https://doi.org/10.1149/1.2115864>
[^rev-04]: S.-L. Zhang and M. Östling, "Metal Silicides in CMOS
    Technology: Past, Present, and Future Trends", *Critical Reviews in
    Solid State and Materials Sciences* **28**(1), 1–129 (2003).
    <https://doi.org/10.1080/10408430390802431>
[^rev-05]: E. C. Jones and E. Ishida, "Shallow junction doping
    technologies for ULSI", *Materials Science and Engineering: R*
    **24**(1–2), 1–80 (1998).
    <https://doi.org/10.1016/S0927-796X(98)00013-8>
[^deal-1965]: B. E. Deal and A. S. Grove, "General Relationship for the
    Thermal Oxidation of Silicon", *Journal of Applied Physics*
    **36**(12), 3770–3778 (1965). <https://doi.org/10.1063/1.1713945>
[^pap-01]: M. H. White, D. A. Adams and J. Bu, "On the go with SONOS",
    *IEEE Circuits and Devices Magazine* **16**(4), 22–31 (2000).
    <https://doi.org/10.1109/101.857747>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098 B1,
    granted 2014-08-05. <https://patents.google.com/patent/US8796098B1/en>
[^cyp-25]: K. Ramkumar, V. Prabhakar and R. Kapre (Cypress
    Semiconductor), *Scalable SONOS based embedded non-volatile memory
    technology*, Semiconductor Digest, 2020-02.
    <https://sst.semiconductor-digest.com/2020/02/scalable-sonos-based-embedded-non-volatile-memory-technology/>
[^hori-1989-latid]: T. Hori, "1/4-μm LATID (LArge-Tilt-angle Implanted
    Drain) technology for 3.3-V operation", *IEDM 1989 Technical
    Digest*, pp. 777–780. <https://doi.org/10.1109/IEDM.1989.74169>
[^rossnagel-1993]: S. M. Rossnagel and J. Hopwood, "Magnetron sputter
    deposition with high levels of metal ionization", *Applied Physics
    Letters* **63**(24), 3285–3287 (1993).
    <https://doi.org/10.1063/1.110176>
[^kar-roy-1999]: A. Kar-Roy, C. Hu, M. Racanelli, C. A. Compton,
    P. Kempf, G. Jolly, P. N. Sherman, J. Zheng, Z. Zhang and A. Yin,
    "High density metal insulator metal capacitors using PECVD nitride
    for mixed signal and RF circuits", *Proc. IEEE 1999 International
    Interconnect Technology Conference (IITC)*, pp. 245–247.
    <https://doi.org/10.1109/IITC.1999.787134>
[^ann-15]: R. T. Edwards (Efabless), "Google/SkyWater and the Promise of
    the Open PDK", *Workshop on Open-Source EDA Technology (WOSET)
    2020*. <https://woset-workshop.github.io/PDFs/2020/a03.pdf>
[^raw-data-readme]: SkyWater PDK Authors, *sky130-raw-data - Raw data
    collected about the SKY130 process technology*, `README.rst`,
    `google/skywater-pdk-sky130-raw-data` repository, 2022, retrieved
    2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/README.rst>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^raw-data-hv-mosfets]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the 5 V, 10/16 V and
    20 V transistors, the native, zero-Vt and ESD NMOS and the thick-oxide
    gate capacitors, IC-CAP `.mdm` files in `sky130_fd_pr/cells/`
    (`nfet_g5v0d10v5`, `pfet_g5v0d10v5`, `nfet_g5v0d16v0`,
    `pfet_g5v0d16v0`, `nfet_g5v0d20v0`, `pfet_g5v0d20v0`,
    `nfet_03v3_nvt`, `nfet_05v0_nvt`, `nfet_20v0_nvt`, `esd_nfet_01v8`,
    `esd_nfet_g5v0d10v5`), `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
[^raw-data-lv-mosfets]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the 1.8 V
    transistors, IC-CAP `.mdm` files in `sky130_fd_pr/cells/`
    (`nfet_01v8`, `nfet_01v8_lvt`, `pfet_01v8`, `pfet_01v8_hvt`,
    `pfet_01v8_lvt`), `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
[^raw-data-passives]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the poly, diffusion
    and well resistors, MiM capacitors, varactors and bipolar
    transistors of the test tile, IC-CAP `.mdm` files in
    `sky130_fd_pr/cells/unsorted/`, `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells/unsorted>
