(references-public-sources)=
# Public sources inventory

An annotated inventory of publicly available sources about (a) the
SKY130 / Cypress "S8" 130 nm process technology and (b) the manufacturing
equipment and materials at SkyWater Technology's 200 mm fab in
Bloomington, Minnesota. It exists so that every step, machine, material
and mask page can cite a source that anyone can obtain.

Every URL below was fetched and checked on 2026-08-30 unless a note says
otherwise. Each entry records what the source contains that is useful for
documenting process steps, tools or materials, and the tier it belongs
to:

* **Cross-check** — a primary public source that can verify a specific
  claim (PDK documentation, SkyWater statements, regulatory filings,
  patents, vendor data).
* **High-level** — introductory or contextual material (encyclopaedia
  articles, textbooks, trade press, talks).
* **Deep dive** — papers, theses, roadmaps and conference proceedings.

Entries carry a short key (for example `PDK-03`) so that other pages can
refer to them unambiguously.

:::{note}
Nothing in this inventory comes from private material. Where a public
source could not be retrieved (dead link, paywall, bot-blocking), it is
listed under *Unverified leads* at the end of the relevant section and
is **not** counted as a verified source.
:::

## 1. SkyWater open PDK documentation

The open PDK is the single most authoritative public description of the
SKY130 process. Its documentation is generated from the
`google/skywater-pdk` repository and published on Read the Docs.

**PDK-01** — *SkyWater SKY130 PDK documentation* (root).
SkyWater PDK Authors (Google / SkyWater Technology), 2020 onwards.
<https://skywater-pdk.readthedocs.io/>.
Entry point to the design rules, device details, layer and mask lists.
Tier: cross-check.

**PDK-02** — *Background* page.
<https://skywater-pdk.readthedocs.io/en/main/rules/background.html>
(source: <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/background.rst>).
States that "SKY130 is a mature 180nm-130nm hybrid technology developed
by Cypress Semiconductor that has been used for many production parts",
that "the technology is the 8th generation SONOS technology node
(130nm)", and lists the stack options: 5 levels of metal (`p`),
inductor-capable (`i`), poly resistor (`r`), SONOS shrunken cell (`s`)
and 10 V regulated supply (`10R`). This is the public origin of the
"S8" ↔ SKY130 identification. Tier: cross-check.

**PDK-03** — *Criteria & Assumptions* page (contains the process stack
diagram).
<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>.
Gives the minimum feature sizes used to derive the design rules and a
small set of film thicknesses: poly 0.18 µm, field oxide 0.07 µm above
the silicon surface under poly, oxide spacer 0.05 µm, pre-LI ILD
0.5 µm, photoresist 1.14 µm, metal 1 minimum width/space 0.14 µm,
`mcon` bottom CD 0.09 µm, via1 0.15 µm. Tier: cross-check.

**PDK-04** — *Process stack diagram* (`metal_stack.svg` / `metal_stack.ps`).
<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
(embedded in PDK-03). The drawing (XCircuit, "not to scale") is the
most complete public statement of the back-end film stack. It labels
each conductor with a thickness — diffusion 0.12 µm, poly 0.18 µm,
`li` 0.10 µm, `met1` 0.36 µm, `met2` 0.36 µm, `met3` 0.845 µm,
`met4` 0.845 µm, `met5` 1.26 µm — and each dielectric with a name and
relative permittivity: FOX (3.9), PSG (3.9), LINT (7.3), NILD2 (4.05),
NILD3 (4.5), NILD3_C (3.5), NILD4 (4.2), NILD4_C (3.5), NILD5 (4.1),
NILD6 (4.0), TOPOX (3.9), TOPNIT (7.5), PI1 (2.94), IOX (3.9) and
SPNIT (7.5), plus the MiM layers `capm` and `cap2m`. It also gives the
cumulative heights of each metal above the substrate (0.3262, 0.9361,
1.3761, 2.0061, 2.7861, 4.0211, 5.3711 and 11.8834 µm). Tier: cross-check.

**PDK-05** — *Masks* page and `masks.csv`.
<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
<https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>.
Table of mask names and acronyms flagged as used in SKY130 (FOM, DNM,
NWM, HVTPM, LVTNM, HVTRM, NTM, HVNTM, LDNTM, PSDM, NSDM, TUNM, ONOM,
LVOM, RPM, NPCM, P1M, LICM1, LI1M, CTM1, MM1–MM5, VIM, VIM2–VIM4, NSM,
PDM, CU1M, PMM2, …). This is the public basis for the mask index and
for the order of the lithography steps. Tier: cross-check.

**PDK-06** — *Layers Reference* and `gds_layers.csv`.
<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
<https://github.com/google/skywater-pdk/blob/main/docs/rules/gds_layers.csv>.
GDS layer/purpose numbers and the process meaning of each drawn layer
(e.g. `vhvi` "used to identify nodes that operate at 12V nominal (16V
max)"). No thicknesses. Tier: cross-check.

**PDK-07** — *Device Details* pages and per-device cross-section drawings.
<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>;
drawings under
<https://github.com/google/skywater-pdk/tree/main/docs/rules/device-details>
(for example `nfet_01v8/cross-section-nfet_01v8.svg`,
`cap_mim/cross-section-cap_mim.svg`, `nfet_20v0/…`, `npn_05v0/…`).
Lists every device offered (1.8 V, 5 V, 10–20 V FETs, native and
zero-Vt devices, NPN/PNP, SRAM cell, SONOS cell, diodes, poly
resistors, MiM and VPP capacitors) with electrical parameters that
constrain the process: P+ poly resistor 300 Ω/sq at fixed widths
0.35–5.73 µm, P− poly 2000 Ω/sq, MiM 2 fF/µm² area and 0.19 fF/µm
periphery, SONOS programmed/erased Vt 1.44 V / −2.3 V and 100 k cycle
endurance. Tier: cross-check.

**PDK-08** — *Parasitic Layout Extraction* page.
<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
(source: <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/rcx.rst>).
Sheet resistances by layer (as listed: metal 1–2 125 mΩ/sq,
metal 3–4 47 mΩ/sq, metal 5 29 mΩ/sq, poly 48 200 mΩ/sq, XHR poly
319 800 mΩ/sq, local interconnect 12 800 mΩ/sq, N-diffusion
120 000 mΩ/sq, P-diffusion 197 000 mΩ/sq) and contact/via resistances.
Useful for inferring film thicknesses and materials (e.g. the 0.36 µm
and 0.845 µm aluminium metals). Tier: cross-check.

**PDK-09** — *"SKY130 (SkyWater PDK) — Stackup Capacitance Data
[public]"* spreadsheet, linked from PDK-08.
<https://docs.google.com/spreadsheets/d/1N9To-xTiA7FLfQ1SNzWKe-wMckFEXVE9WPkPPjYkaxE/edit#gid=226894802>.
Public Google Sheet with tabs "RCX Model Information", "Metal Layer
Process Variation", "Via Process Variation", "Capacitance Table –
Basic/Extended Data" and "Layer resistances and capacitances". Tier:
cross-check.

**PDK-10** — *google/skywater-pdk* repository README.
<https://github.com/google/skywater-pdk>. Summarises the process
(1.8 V core with 5.0 V I/O, "1 level of local interconnect", "5 levels
of metal", high sheet-rho poly resistor, optional MiM, "SONOS shrunken
cell", 10 V regulated supply, HV extended-drain NMOS/PMOS), Apache 2.0
licence, links to documentation and the announcement list. Tier:
cross-check.

**PDK-11** — *SkyWater SKY130 Process Design Rules* index page.
<https://skywater-pdk.readthedocs.io/en/main/rules.html>. Table of
contents for the rule chapters (Background, Masks, Criteria &
Assumptions, Layers, Periphery rules, HV / VHV methodology, Antenna,
RCX, Device details). Tier: cross-check.

**PDK-12** — *Sky130 Technology Library* (Hammer VLSI documentation).
<https://hammer-vlsi.readthedocs.io/en/latest/Technology/Sky130.html>.
Third-party (UC Berkeley) description of how the open PDK is consumed
by a digital flow; useful only for naming conventions. Tier: high-level.

**PDK-13** — *Sky130 PDK* (UCSC VLSI-DA chip tutorials).
<https://vlsida.github.io/chip-tutorials/sky130.html>. Community
tutorial describing the five routing metals plus local interconnect and
their preferred directions; its numeric claims are secondary and should
be checked against PDK-04 before use. Tier: high-level.

## 2. Google and SkyWater announcements and talks about the open PDK

**ANN-01** — Tim Ansell, *"[FOSSi Dial-Up] Skywater PDK: Fully open
source manufacturable PDK for a 130nm process"*, FOSSi Foundation
Dial-Up talk, 2020-06-30 (video).
<https://www.youtube.com/watch?v=EczW2IWdnOM>. Slides:
<https://docs.google.com/presentation/d/e/2PACX-1vRtwZPc8ykkkgtUkHkoJZrP9jKOo3FYdKqbg-So0ic6_kx7ha1vHnxrWmuxWkTc9GfC8xl0TfEpMLwK/pub>
("google/skywater-pdk – Manufacturable Open Source 130nm PDK").
The launch talk; describes the process options, the Cypress heritage
and the roadmap. Tier: high-level.

**ANN-02** — FOSSi Foundation, *"FOSSi Dial-Up launches with Big Bang:
Production-ready Open Source PDK"*, 2020-06-17.
<https://www.fossi-foundation.org/2020/06/17/fossi-dial-up>; announcement
on the `skywater-pdk-announce` list, 2020-06-26:
<https://groups.google.com/g/skywater-pdk-announce/c/4zBSayPQy4I>.
Tier: high-level.

**ANN-03** — Philipp Wagner (FOSSi Foundation), *"Produce your own
physical chips. For free. In the Open."*, 2020-06-30.
<https://fossi-foundation.org/blog/2020-06-30-skywater-pdk>. Summary of
the talk with links to video and slides. Tier: high-level.

**ANN-04** — OSH Park blog, *"FOSSi Dial-up debuts with open source PDK
talk"*, 2020-06-22.
<https://blog.oshpark.com/2020/06/22/fossi-dial-up-debuts-with-open-source-pdk-talk/>.
Tier: high-level.

**ANN-05** — FOSSi Dial-Up YouTube playlist (2020–2021 talks on the
SKY130 PDK, OpenRAM, OpenROAD, Magic DRC, standard cells).
<https://www.youtube.com/playlist?list=PLUg3wIOWD8yoZCg9XpFSgEgljx6MSdm9L>;
including *"[FOSSi Dial-Up] First Impressions from the Skywater Open
Source PDK Shuttle"* <https://www.youtube.com/watch?v=zVlGynNwZDo>.
Tier: high-level.

**ANN-06** — Antmicro, *"Open Source Process Design Kit from Google,
SkyWater technologies and partners released"*, 2020-06-29.
<https://antmicro.com/blog/2020/06/skywater-open-source-pdk>. Repeats the
process feature list ("1 level of local interconnect, 5 levels of
metal, Inductor-capable, High sheet rho poly resistor, Optional MiM
capacitors … SONOS shrunken cell, Supports 10V regulated supply, HV
extended-drain NMOS and PMOS"). Tier: high-level.

**ANN-07** — Gareth Halfacree, Hackster.io, *"Google, SkyWater Release
Production Dev Kit, Offer Open Hardware Projects Free 130nm
Manufacturing"*, 2020-07-01.
<https://www.hackster.io/news/google-skywater-release-production-dev-kit-offer-open-hardware-projects-free-130nm-manufacturing-eadfefbcda7b>.
Tier: high-level.

**ANN-08** — The Amp Hour, episode 501, *"Discussing the Open Source PDK
with Tim Ansell"*, 2020-07-20.
<https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/>.
Discussion of why a 130 nm node was chosen and what SkyWater allowed to
be published. Tier: high-level.

**ANN-09** — SkyWater Technology, *"Open Source ASICs take a Giant Leap
Forward with the First Ever Open Foundry PDK"*, 2020-06.
<https://www.skywatertechnology.com/open-source-asics-take-a-giant-leap-forward-with-first-ever-open-foundry-pdk/>.
SkyWater's own framing of SKY130 as "130 nm CMOS technology" under
Apache 2.0. Tier: cross-check (for SkyWater statements).

**ANN-10** — Google / SkyWater / Efabless, *"Google Partners with
SkyWater and Efabless to Enable Open Source Manufacturing of Custom
ASICs"*, PR Newswire, 2020-11-12.
<https://www.prnewswire.com/news-releases/google-partners-with-skywater-and-efabless-to-enable-open-source-manufacturing-of-custom-asics-301171870.html>
(also on SkyWater's site:
<https://www.skywatertechnology.com/google-partners-with-skywater-and-efabless-to-enable-open-source-manufacturing-of-custom-asics/>).
First MPW shuttle programme: 40 slots, Q4 2020. Tier: cross-check.

**ANN-11** — SkyWater / Efabless, *"First Google-Sponsored MPW Shuttle
Launched at SkyWater with 40 Open Source Community Submitted Designs"*,
2021-04-06.
<https://skywatertechnology.com/press-releases/first-google-sponsored-mpw-shuttle-launched-at-skywater-with-40-open-source-community-submitted-designs>.
States that SKY130 "offers many normally optional features as
standard — features like the local interconnect, SONOS non-volatile
memory functionality, MiM capacitors and more". Tier: cross-check.

**ANN-12** — Johan Euphrosine and Ethan Mahintorabi (Google), *"SkyWater
and Google expand open source program to new 90nm technology"*, Google
Open Source Blog, 2022-07-28.
<https://opensource.googleblog.com/2022/07/SkyWater-and-Google-expand-open-source-program-to-new-90nm-technology.html>.
Shuttle statistics (six shuttles, 240 designs) and the SKY90-FD FDSOI
announcement; useful context for the fab's 90 nm capability. Tier:
high-level.

**ANN-13** — SkyWater Technology, *"SKY's the Limit with the SKY130
Open-Source PDK"*, 2023-11-12.
<https://www.skywatertechnology.com/sky130-open-source-pdk/>. Describes
SKY130 as "SkyWater's volume 130 nm CMOS technology". Tier: cross-check.

**ANN-14** — SkyWater / Cadence, *"SkyWater Announces Availability of
Cadence Open-Source PDK and Reference Design for SkyWater's 130 nm
Process"*, 2023-11-03.
<https://www.skywatertechnology.com/skywater-announces-availability-of-cadence-open-source-pdk-and-reference-design-for-skywaters-130-nm-process/>.
Tier: high-level.

**ANN-15** — R. Timothy Edwards (Efabless), *"Google/SkyWater and the
Promise of the Open PDK"*, Workshop on Open-Source EDA Technology
(WOSET) 2020.
<https://woset-workshop.github.io/PDFs/2020/a03.pdf>. Includes
"Fig. 1. Process stack of the SkyWater 130nm open process" and states
that the options include "deep n-well, MiM capacitors, high and
ultra-high sheet ρ resistors, and isolated gate flash memory
transistors". Tier: deep dive.

**ANN-16** — Tim Edwards (Efabless), *"Introduction to the SkyWater
PDK — The New Age of Open Source Silicon"*, lecture slides, 2021-10-08
(hosted by UC San Diego, BENG 207).
<https://isn.ucsd.edu/courses/beng207/lectures/Tim_Edwards_2021_slides.pdf>.
Slides "Understanding the SkyWater PDK — Layers / back-end metal stack"
give "5 layers of aluminum metal", local interconnect as "Titanium
Nitride (TiN)", metal thicknesses metal5 1.26 µm, metal4 0.845 µm,
metal3 0.845 µm, metal2 0.36 µm, metal1 0.36 µm, local interconnect
0.1 µm, the MiM `capm`/`cap2m` placement, and the copper
redistribution layer (4.0 µm RDL, 5.25 µm polyimide via). Tier:
high-level (numbers should be cross-checked against PDK-04).

**ANN-17** — Wikipedia, *"130 nm process"*.
<https://en.wikipedia.org/wiki/130_nm_process>. Context for the node
(2000–2001 introduction) and a note on the 2020 SkyWater/Google open
PDK release. Tier: high-level.

**ANN-18** — Wikipedia, *"SkyWater Technology"*.
<https://en.wikipedia.org/wiki/SkyWater_Technology>. Corporate history
with references; states the fab makes chips on "90-nanometer and
130-nanometer process technology on equipment designed to handle
200-millimeter wafers". Tier: high-level.

*Not found.* Searches for dedicated ESSCIRC, ISPD, DAC or VLSI
Symposium presentations by SkyWater staff on the SKY130 process itself
returned only the items above; Crossref lists several 2024 conference
papers that *use* the PDK (e.g. standard-cell characterisation) but
none that describe the process flow.

## 3. SkyWater Technology corporate sources

### 3.1 Website — technology and facility pages

**SKW-01** — SkyWater Technology, *"Facilities & Capabilities"*
(Manufacturing → Facilities & Capabilities), live page, accessed
2026-08-30.
<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>.
**The most valuable single public source for the tool set.** For the
Minnesota fab it states "200 mm equipment", "91,000 sq ft cleanroom
(class 10)", "Capacity: 10,000 30 ML CMOS wafers/month or 50,000 MOSFET
wafers/month", "90 nm + feature geometries", and that the site was
"recently expanded in 2020 to enable additional capacity and Cu back
end of line". The "SkyWater Process Integration Tools & Capabilities"
list then names tools and chemistries by area:

* *Lithography* — "ASML I-line stepper", "ASML I-line scanner", "ASML
  DUV stepper", "ASML DUV scanner", "ASML 193nm single stage scanner –
  90nm CD", "ASML 193nm twin stage scanner – sub 65nm CD"; tracks "DNS
  80B track", "Sokudo RF3 track", "TEL ProZ Lithius track"; max field
  26 mm × 32 mm.
* *Photo metrology* — "AMAT Verity (multiple versions) CD", "AMAT
  VeraSEM", "KLA 5200/5300/Archer overlay".
* *Film deposition* — "Lam/Novellus/AMAT" PECVD TEOS ("C2 and
  Producer"), PECVD silane oxide/nitride/oxynitride ("C1"),
  "Lam/Novellus High Density Plasma (HDP) doped and phos doped with
  sputter etch", "Lam/Novellus PECVD Tungsten – plug fill – PNL option",
  "AMAT PVD Metal" (aluminium pure and Cu-doped, TiW, ESC TiN, IMP TiN,
  collimated Ti, WN, cobalt, niobium), "AMAT Raider single wafer Cu
  plating", ALD (AlN, TiN, SiO₂, Al₂O₃, HfO₂, TiO₂, ZrO₂).
* *Etch* — metal: "Lam 9600, Al, TiW, TiN, Pt" and "Lam 2300 Versys,
  Al, TiW, TiN, Nb, Pt"; poly/silicon: "AMAT DPSII, HBR, Cl2, NF3, CF4,
  CHF3, O2 – gate, trench, W/WN", "Lam 9400 TCP, poly/nitride, HBr,
  CF4, SF6, O2", "Lam 4400, HBr, Cl2, C2F6, CF4, SF6, O2".
* *Resist removal / cleans* — "Gasonic PEP, remote microwave plasma",
  "Iridia RF microwave", "Mattson Aspen2", "Akrion Gamma Batch Wet Bench
  – Sulfuric, SC1, phosphoric, BOE", batch rotational "EKS265, EKC270
  solvents", single wafer "SEZ223, Davinci, HF, DSP+HF".
* *Diffusion / anneal / implant* — "Furnaces are all made by Aviza"
  (wet/dry oxidation to 1150 °C, Ar/N₂ anneal, LPCVD nitride,
  polysilicon, silane oxide, "LPCVD oxide/nitride/oxide", BTBAS
  low-temperature nitride, H₂ and forming-gas alloy); pre-clean "DNS
  wet bench industry standard HF/SC1/SC2", "FSI Mercury"; RTA "Ag
  Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C"; implant "Axcelis 8250
  Mid current B11, BF2, As … 1e11 to 1e14", "Axcelis GSD High
  current/energy B11, BF2, P, As, 10-3000kev, 1e11 to 5e15", "Axcelis
  GSD Hi dose B11, BF2, P, As 2-180kev, 5e12 to 5e16"; scribe
  "Lumonics Superclean".
* *CMP* — "AMAT Mirra CMP" for oxide, nitride, niobium, aluminium,
  tungsten, high-selectivity tungsten and copper.
* *Test* — parametric "HP 4062UX"; sort "Advantest T5365P", "Verigy
  V3308, V4108", "Credence Duo", "Credence LT", "Verigy 93000",
  "Camtek Falcon"; reliability lab "Qualitau".
* *Special modules* — "Nitrided gate oxide", "Ti and Co Silicide", "W
  plug dual damascene", "Cu dual damascene", "Nb damascene", "Photo
  stitching", "Low temp (~200C) back end of line processing".

Caveats: this is a 2020s capability list for the whole fab, so it
includes tools added after the S8 flow was developed (copper plating,
niobium, 193 nm scanners, ALD). Tier: cross-check (SkyWater statement).

**SKW-02** — SkyWater Technology, *"Mixed-Signal CMOS & Read Out IC
(ROIC)"* platform page, accessed 2026-08-30.
<https://www.skywatertechnology.com/cmos/>. Table of platforms: S130 —
"130nm CMOS", "200mm", metal layers "5: Al", local interconnect "1",
core 1.8 V, I/O "3.3V, 5.0V", high voltage "20+V, Drain-Extended CMOS
(16V)", "MiM Capacitor", "Precision Resistor", "Bulk" substrate; S90LN
— 90 nm, 7 Al metals, 2 dual-damascene local interconnect, 4 µm epi;
RH90 — 90 nm FD-SOI. Tier: cross-check.

**SKW-03** — SkyWater Technology, *"RH90: The Next-Generation Stateside
Strategic Rad-Hard by Process Technology"*, 2023-03-14.
<https://www.skywatertechnology.com/rh90-the-next-generation-stateside-strategic-rad-hard-by-process-technology/>.
Context for the 90 nm FDSOI platform that shares the fab. Tier:
high-level.

**SKW-04** — SkyWater Technology, *"Weebit Nano ReRAM IP now available
in SkyWater Technology's S130 process"*, 2023-03-07.
<https://www.skywatertechnology.com/weebit-nano-reram-ip-now-available-in-skywater-technologys-s130-process/>.
Describes S130 as an "automotive-grade, extended temperature,
mixed-signal CMOS platform" used "for billions of devices to-date".
Tier: cross-check.

**SKW-05** — SkyWater Technology, *"Overcoming ASIC Obsolescence"*,
2024-04-08.
<https://www.skywatertechnology.com/overcoming-asic-obsolescence/>.
States "a roadmap for the S130 process that extends 10-15 years".
Tier: high-level.

**SKW-06** — SkyWater Technology, *"A Day in the Life of a SkyWater
Engineer"* (R&D/OPC engineer profile), 2024-09-04.
<https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-engineer/>.
Names "the ASML TWINSCAN lithography tool" and "the game-changing
Multibeam direct-write tool". Tier: cross-check (tool naming).

**SKW-07** — SkyWater Technology, *"A Day in the Life of a SkyWater
Maintenance Technician"*, 2023-12-14.
<https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>.
Names a "Novellus high density plasma tool", the "SEZ etcher tool" and
work on implanter robotics and vacuum systems. Tier: cross-check (tool
naming).

**SKW-08** — SkyWater Technology, *"Maintenance Technician Job
Overview"* and *"Careers & Jobs"* pages.
<https://www.skywatertechnology.com/maintenance-technicians/>,
<https://www.skywatertechnology.com/careers/>. The careers page links
the applicant portal on Dayforce
(<https://jobs.dayforcehcm.com/en-US/skywater/CANDIDATEPORTAL/>); the
maintenance page names no tools. Tier: high-level.

**SKW-09** — SkyWater Technology press-release index.
<https://www.skywatertechnology.com/category/press-releases/>. Tier:
high-level (navigation).

### 3.2 Press releases about the fab, expansions and tools

**SKW-10** — *"SkyWater Technology Foundry Acquires Twin-Cities
Semiconductor Manufacturing Facility from Cypress Semiconductor
Corporation"*, 2017-03-27.
<https://www.skywatertechnology.com/skywater-technology-foundry-acquires-twin-cities-semiconductor-manufacturing-facility-from-cypress-semiconductor-corporation/>.
"200mm semiconductor wafer manufacturing facility in Bloomington",
400 jobs, facility "originally established by Control Data Corporation
in the 1980s", multi-year wafer supply to Cypress. Tier: cross-check.

**SKW-11** — *"US Department of Defense to Invest up to $170M at
SkyWater for Rad-Hard Technology"*, 2019-10-21.
<https://www.skywatertechnology.com/us-department-of-defense-to-invest-up-to-170m-at-skywater-for-rad-hard-technology/>.
"up to 15,000 square feet of new cleanroom area", addition of "copper
dual-damascene interconnect technology", initial phase $80 M, 90 nm
rad-hard capability. (Trade-press copies quote 8,000 sq ft; see
PRESS-08.) Tier: cross-check.

**SKW-12** — *"SkyWater Releases Early Access PDK … for 90 nm Strategic
Rad-Hard by Process Platform"*, 2020-12-02, and *"SkyWater Successfully
Launches MPW Shuttle for 90 nm Strategic Rad-Hard by Process
Platform"*, 2021-07-15.
<https://www.skywatertechnology.com/skywater-releases-early-access-pdk-and-partners-with-trusted-semiconductor-solutions-to-enable-design-kit-for-90-nm-strategic-rad-hard-by-process-platform/>,
<https://www.skywatertechnology.com/press-releases/skywater-successfully-launches-mpw-shuttle-for-90-nm-strategic-rad-hard-by-process-platform/>.
Tier: high-level.

**SKW-13** — *"SkyWater Technology to Strategically Invest $56 Million
in Capacity Expansion and Gallium Nitride Technology"*, 2021-07-26
(Business Wire; verified copy at Semiconductor Today).
<https://www.semiconductor-today.com/news_items/2021/jul/skywater-270721.shtml>.
Capital for Minnesota capacity; no tool names. Tier: high-level.

**SKW-14** — *"SkyWater Announces Enhanced Capabilities with
Multibeam's First in Industry High Productivity Multicolumn E-Beam
Lithography System"*, 2024-07-25.
<https://www.skywatertechnology.com/multibeam-e-beam-lithography-system/>
(also Business Wire:
<https://www.businesswire.com/news/home/20240725367118/en/>).
Multicolumn e-beam (MEBL) tool received for the Minnesota fab, "the
only production lithography tool capable of sub 50 nm geometries on
200 mm wafers", customer access from Q4 2024. Tier: cross-check.

**SKW-15** — *"SkyWater Chosen for Volume U.S. Manufacturing of
Temperature Sensing Chip …"*, 2020-05-26.
<https://www.skywatertechnology.com/skywater-chosen-for-volume-u-s-manufacturing-of-temperature-sensing-chip-for-low-cost-wearable-solution-that-detects-early-stage-symptom-of-covid-19/>.
Describes "SkyWater's 130 nm mixed-signal ASIC process (S130)". Tier:
high-level.

**SKW-16** — SkyWater Technology, *"SkyWater Technology — Presentation
to MN Senate Jobs Committee"*, 2023-01-25 (Minnesota Legislative
Reference Library archive, PDF).
<https://www.lrl.mn.gov/archive/minutes/senate/2023/jobs/20230125/Jobs_20230125_SkyWater-Presentation-to-MN-Senate-Jobs-Committee-25Jan2023.pdf>.
Minnesota site: ">600 employees", "200 mm equipment", "91,000 ft²
Cleanroom (Class 10 + SMIF)", "10,000 30 ML CMOS wafers/month or
50,000 MOSFET wafers/month", "65 nm+ feature geometries", ">$1B
capital investment", "DMEA Cat 1A Trusted since 2010"; a company
timeline from the Cypress era (65 nm qualification, foundry opened to
non-Cypress customers) to 2022. Tier: cross-check.

### 3.3 SEC filings

Searches of the filings below for equipment-vendor names (Applied
Materials, Lam Research, Novellus, ASML, Nikon, Canon, KLA, Axcelis,
Varian, Tokyo Electron, Hitachi, Ebara, SCREEN, Amtech, Kokusai, ASM,
Mattson, Rudolph/Onto, Ultratech, Cymer, Multibeam) found **no
equipment supplier named as a supplier**; the only hits are
biographical (a director on the Axcelis board; the President's earlier
career at Rudolph Technologies). The filings do describe the fab,
capacity, process platforms and raw-material suppliers.

**SEC-01** — SkyWater Technology, Inc., Form S-1 (registration
statement), filed 2021-03-22, and Form S-1/A, filed 2021-04-12.
<https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>,
<https://www.sec.gov/Archives/edgar/data/1819974/000119312521112378/d26688ds1a.htm>
(final prospectus 424B4:
<https://www.sec.gov/Archives/edgar/data/1819974/000119312521126725/d26688d424b4.htm>).
Key statements: "Our Bloomington, Minnesota-based fab can produce up
to 156,000 wafers per year (depending on the product mix) and has at
least 522 well-maintained fab and sort tools"; "Our utilization rate
for 2019 was approximately 68%"; "Our S90 (90 nm gate), S130 (130 nm
gate) and CMOS process flows (greater than 130 nm) are the foundation
of our business"; "the base design IP portfolio for S130 technologies
originating from Cypress (now Infineon) was licensed via a technology
license agreement in 2017"; facilities of "approximately 396,000 square
feet"; raw-material suppliers (GlobalWafers and SEH America wafers,
Honeywell Electronic Materials sputter targets, Air Products and
Praxair gases, KMG Chemicals); "Advantages of 200 millimeter Wafer
Fabs". Note: SEC.gov rejects fetches without a descriptive
`User-Agent`. Tier: cross-check.

**SEC-02** — SkyWater Technology, Inc., Form 10-K for fiscal year
2023, filed 2024.
<https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>.
"In our Minnesota facility's 200 mm fab, CMOS process flows for a number
of different node dimensions are offered ranging from 90 nm—350 nm";
"In 2020, we added deep-trench etching capability"; "the base design IP
portfolio for S130 and S90 technologies originating from Cypress was
licensed via a technology license agreement in 2017"; Minnesota
facilities "approximately 356,000 square feet"; RH90 "uses the
already-proven 90 nm fully depleted silicon-on insulator ("FDSOI")
frontend process licensed from MIT-Lincoln Laboratory"; updated
supplier list (GlobalWafers, SEH America, Honeywell and JX Metals
targets, Linde and Airgas gases, EMD Performance Materials). Tier:
cross-check.

**SEC-03** — SkyWater Technology, Inc., Form 10-K for fiscal year
2025, filed 2026.
<https://www.sec.gov/Archives/edgar/data/1819974/000181997426000009/skyt-20251228.htm>.
"our Minnesota fab was owned and operated by Cypress Semiconductor
Corporation … as a captive manufacturing facility for 26 years"; lists
as exhibit 10.7 the "Process Technology License Agreement, dated as of
March 1, 2017, by and between Cypress Semiconductor Corporation and
Cypress Semiconductor (Minnesota) Inc." and its 2020 amendment; Fab 25
(Austin) acquisition. Tier: cross-check.

**SEC-04** — Investor-relations SEC filings index.
<https://ir.skywatertechnology.com/financials/sec-filings/default.aspx>.
Tier: high-level (navigation).

### 3.4 Government and construction sources about the Minnesota fab

**GOV-01** — NIST CHIPS for America, *"SkyWater Technology
(Minnesota)"*, preliminary memorandum of terms signed 2024-12-06.
<https://www.nist.gov/chips/skywater-technology-minnesota-bloomington>.
"up to $16 million" for "replacing equipment, upgrading the facility's
cleanroom and space and IT systems" to increase "production capacity
of 90nm and 130nm wafers by approximately 30%". Tier: cross-check.

**GOV-02** — Business Facilities, *"SkyWater Technology To Invest
$127M In Minnesota Facility"*, 2024-12-18.
<https://businessfacilities.com/skywater-technology-invests-127m-in-minnesota-facility/>.
$19 M Minnesota Forward Fund, $127 M total project, ~70 jobs. Tier:
high-level.

**GOV-03** — Hunt Electric, *"Skywater Technology Foundry"* project
page. <https://www.huntelec.com/portfolio/skywater/>. "64,500 s.f.
addition … 8,400 s.f. of Class 10 fabrication area and additional
4,500 s.f. of future Class 10 area". Tier: cross-check (cleanroom
size).

**GOV-04** — Alliiance (architects), *"SkyWater Technology"* project
page, 2023-01-23.
<https://alliiance.com/design/science-and-technology/skywater-technology/>.
"64,000 SF building addition … approximately 13,000 SF of Class 10
semiconductor cleanroom fabrication (FAB) space; 4,800 SF of future
FAB cleanroom; and a 15,300 SF sub-fabrication space". Tier:
cross-check (cleanroom size).

**GOV-05** — McGough (contractor), *"SkyWater Technology Foundry"*
project page, 2023-07-20.
<https://www.mcgough.com/portfolio/skywater-technology-foundry/>.
"adding more than 64,000 SF". Tier: high-level.

## 4. SkyWater job postings naming tools

Job-board pages are heavily bot-protected; only the postings below
could actually be retrieved. Posting text changes frequently, so each
entry records the retrieval date.

**JOB-01** — Indeed, *"Skywater Technology Foundry Jobs, Employment in
Bloomington, MN"* (listing page), retrieved 2026-08-30.
<https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>.
The *Defect Technician 2* posting reads "General operation of
semiconductor defect metrology tools: SEM/AIT/KLA/SP1/EV300/1X" —
i.e. KLA-Tencor AIT (patterned-wafer inspection), SP1 (unpatterned
Surfscan) and a Zeiss/Leica EV300-class optical review station. Other
titles on the page (Equipment Maintenance Technician – Metrology,
Senior Metals Process Technician, Development Engineering Senior
Technician) name no tools. Tier: cross-check (medium strength).

**JOB-02** — Indeed, Minnesota-wide and Bloomington listing pages,
retrieved 2026-08-30.
<https://www.indeed.com/q-skywater-technology-foundry-l-minnesota-jobs.html>,
<https://www.indeed.com/q-skywater-technologies-l-bloomington,-mn-jobs.html>.
Same job families; no additional tool names. Tier: high-level.

**JOB-03** — Career.com, *"Plasma Etch Process Development Engineer"*,
SkyWater Technology Foundry, Bloomington MN, posted 2024-08-09 (closed
2024-10-30).
<https://www.career.com/company/skywater-technology-foundry-inc/job/plasma-etch-process-development-engineer/-in-bloomington,mn?jid=83e5f3b7-6fb2-41df-9003-31e8e118e0a8>.
Describes the role ("bringing cutting-edge eight-inch Silicon designs
to life") but names no tools. Tier: high-level.

**JOB-04** — LinkedIn, *"Equipment Maintenance Technician"*, SkyWater
Technology, Austin TX (Fab 25, not Bloomington), retrieved 2026-08-30.
<https://www.linkedin.com/jobs/view/equipment-maintenance-technician-at-skywater-technology-4434999110>.
Names Daifuku AMHS, Kensington and Brooks wafer sorters — recorded
here only to show that SkyWater postings do name vendors; not evidence
for the Minnesota fab. Tier: high-level.

**JOB-05** — SkyWater applicant portal (Dayforce).
<https://jobs.dayforcehcm.com/en-US/skywater/CANDIDATEPORTAL/>. Live
listings; the portal renders client-side and individual postings could
not be captured. Tier: high-level.

### Unverified leads (job boards)

Search-engine snippets of SkyWater Technology Foundry postings on
ZipRecruiter, Indeed and Glassdoor (2023–2026) repeatedly quote
equipment lists such as: "LAM Alliance, LAM 2300 Exelan, TEL Unity
M/ME, AMAT Centura DPS Metal/Poly/SuperE, LAM DaVinci wet etch sinks";
"AMAT Endura/Centura PVD and HTF systems, Producer, SVG/Thermco
horizontal diffusion furnaces/SEMY, Aviza Vertical Furnace, Novellus
Concept One, and FSI Mercury"; "AMAT Centura 5200/5500, Producer, Mirra
Mesa"; "AMAT Mirra and Mirra Mesa"; "Axcelis GSD300E Ion Implanter and
Axcelis Purion Ion Implanters". The pages that carry them
(<https://www.ziprecruiter.com/co/Skywater-Technology-Foundry/Jobs/-in-Bloomington,MN>
and Glassdoor's SkyWater listings) returned HTTP 403 or a geographic
redirect to every automated fetch attempted on 2026-08-30, so the
quotations could not be confirmed against the page. They are
consistent with SKW-01 (Lam, AMAT, Novellus, Aviza, FSI, Axcelis GSD,
Mirra all appear there) but should be treated as **weak** evidence
until a copy of the posting is captured.
