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
Everything in this inventory is publicly available. Where a public
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

## 5. Cypress Semiconductor, "Fab 4" and the S8 process

### 5.1 Fab history: Control Data → VTC → Cypress Fab 4 → SkyWater

**CYP-01** — Cypress Semiconductor, *"Cypress Closes Sale of Minnesota
Wafer Fabrication Facility"*, PR Newswire, 2017-03-01.
<https://www.prnewswire.com/news-releases/cypress-closes-sale-of-minnesota-wafer-fabrication-facility-300416287.html>.
Sale of "Fab 4 in Bloomington, Minnesota" for $30 M to SkyWater
Technology Foundry (Oxbow Industries); wafer-supply agreement. Tier:
cross-check.

**CYP-02** — Alex Van Abbema, Star Tribune, *"Twin Cities tech
executives form new company, buy Cypress chip plant in Bloomington"*,
2017-03-31.
<https://www.startribune.com/twin-cities-tech-executives-form-new-company-buy-cypress-chip-plant-in-bloomington/417672063>.
"The plant, built in the 1980s by Control Data, has 80,000 square feet
of clean-room space and chiefly makes wafers that are 200 millimeters
in diameter. Cypress produced about 17,000 wafers a month at the
plant"; Cypress "bought the plant from Control Data Corp. in January
1991 for $14.7 million"; about 400 employees. Includes an aerial
photograph of the plant. (Page is rate-limited; retrieved with a
browser.) Tier: cross-check.

**CYP-03** — Evan Ramstad, Star Tribune, *"Why computer-chip factories
from the 1980s are still going strong in Bloomington"*, 2019-06-09.
<https://www.startribune.com/why-computer-chip-factories-from-the-1980s-are-still-going-strong-in-bloomington/510984342>.
Fab tour report: Control Data's chip division (1970) → VTC Inc. (1982),
which "added the plant that is now SkyWater's … at 2401 E. 86th St.";
Control Data bought the plants back in the late 1980s and sold this
one to Cypress; "under Cypress, the size of the cleanroom at SkyWater's
plant more than doubled"; wafers go through "about 165 steps or
processes over about four weeks"; 200 mm wafers; the SkyTech Center
(carbon-nanotube deposition) lab. Tier: high-level.

**CYP-04** — Evan Ramstad, Star Tribune, *"SkyWater, Minnesota's
biggest chip plant, is getting even bigger with a third clean room"*,
2019-10-22.
<https://www.startribune.com/skywater-minnesota-s-biggest-chip-plant-is-getting-even-bigger-with-a-third-clean-room/563565242>.
Third cleanroom (first physical expansion since the 1995 second
cleanroom "that doubled the size of the plant, which was built in the
early 1980s"); "New tools and equipment have been installed several
times since then"; about 500 employees; copper interconnect capability
and the 90 nm limit of the existing cleanrooms. Tier: high-level.

**CYP-05** — ATREG, *"For sale: Cypress operational 200mm fab,
Bloomington, USA"*, 2015-10-01.
<https://atreg.com/for-sale-cypress-operational-200mm-fab-bloomington-usa/>.
Fab-broker listing: "cleanroom facility spanning approx. 80,000 sq.
ft.", "a fully integrated tool line capable of producing approx. 16,700
wafers / month (350nm to 90nm)", "Wide range of 416 tools", DMEA
Category 1A Trusted, 14.7-acre site, option to license process IP.
Tier: cross-check (tool count and capacity in 2015).

**CYP-06** — Cypress Semiconductor, Product Information Notification
PIN152804, *"Qualification of GlobalWafer Silicon Wafers for 250nm,
130nm and 90nm Technology Products at Cypress Fab 4"*, 2015-07-12
(copy hosted by Future Electronics).
<https://media.futureelectronics.com/PCN/45887_SPCN.PDF>. Names the
process families run at Fab 4: "250nm R7, 130nm C8/R8/S8/L8 and 90nm
C9/R9/R95 technology products at Cypress Fab 4 in Bloomington,
Minnesota" — the clearest public statement that **S8 was a Fab 4
process** — and the starting-wafer supplier qualification. Tier:
cross-check.

**CYP-07** — Cypress Semiconductor Corp., Form 10-Q/A for Q1 2003.
<https://www.sec.gov/Archives/edgar/data/0000791915/000120677403000508/d12840.htm>.
"Cypress's technologically advanced, eight-inch wafer production
facility located in Minnesota ("Fab 4")"; "During Q1 2003 we continued
ramping our latest 0.13-micron technology in manufacturing. We are
simultaneously transferring our 90 nanometer technology from our
eight-inch R&D facility in San Jose, California ("Fab 1") to our
eight-inch manufacturing facility in Minnesota ("Fab 4")". Dates the
0.13 µm ramp at Fab 4. Tier: cross-check.

**CYP-08** — Cypress Semiconductor Corp., 2004 Annual Report (10-K
wrap), 2005.
<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2004.pdf>.
"Our 90-nanometer technology is now in production at our Minnesota
facility"; fabs "utilize our proprietary 90-nanometer and 0.13 through
0.8-micron CMOS, 0.25 and 0.8-micron BiCMOS, and 0.35-micron Silicon
Nitride Oxide Silicon ("SONOS") processes"; "transition to more
advanced process technologies in our facility in Bloomington,
Minnesota including our 90-nanometer and 0.13-micron CMOS process
technologies"; image sensors made "in Cypress's Fab 4 wafer
fabrication plant"; "our existing 200mm wafers". Tier: cross-check.

**CYP-09** — Cypress Semiconductor Corp., Form 10-K for fiscal 2007,
filed 2008.
<https://www.sec.gov/Archives/edgar/data/791915/000104746908002122/a2182468z10-k.htm>.
Plan to exit the Texas fab and "transfer production to its more
cost-competitive facility in Minnesota"; Bloomington property 278,000
sq ft; transfer of "its 0.13-micron SRAM and LOGIC processes" to Grace
Semiconductor (2007) and of the 0.35 µm SONOS process (2006). Tier:
cross-check.

**CYP-10** — Cypress Semiconductor Corp., Form 10-K for fiscal 2016,
filed 2017.
<https://www.sec.gov/Archives/edgar/data/791915/000079191517000007/cy-01012017x10xk.htm>.
Bloomington property 337,000 sq ft; sale completed 2017-03-01; $37.2 M
impairment. Tier: cross-check.

**CYP-11** — FundingUniverse, *"History of Cypress Semiconductor
Corporation"*.
<https://www.fundinguniverse.com/company-histories/cypress-semiconductor-corporation-history/>.
"At the end of 1990, the company bought its Bloomington, Minnesota,
wafer fab from Control Data VTC, paying just $14.7 million"; 1998
restructuring keeping SRAM at "Fab 4 in Minnesota, where it was
developing a 0.35-micron process". Tier: high-level.

**CYP-12** — Twin Cities Business, *"Minnesota's Silicon Touch"*,
2011-06-01. <https://tcbmag.com/minnesotas-silicon-touch-june-2011/>.
Cypress era: purchase from Control Data's VTC unit for $14.7 M;
TrueTouch products made in Bloomington. Tier: high-level.

**CYP-13** — Wikipedia, *"Cypress Semiconductor"* and *"Control Data
Corporation"*.
<https://en.wikipedia.org/wiki/Cypress_Semiconductor>,
<https://en.wikipedia.org/wiki/Control_Data_Corporation> ("CDC spun
off VTC, a chip maker"). Tier: high-level.

**CYP-14** — AnySilicon, *"A Brief History of SkyWater Technology"*.
<https://anysilicon.com/a-brief-history-of-skywater-technology/>.
Tier: high-level.

**CYP-15** — Jon Y (Asianometry), *"SkyWater Technologies: America's
Semiconductor Foundry"*, 2021-07-28.
<https://www.asianometry.com/p/skywater-technologies-americas-semiconductor>.
80,000 sq ft, Cypress 1991–2017, "upgraded from 130nm/90nm to 65nm",
"12,000 200-mm wafers a month … assuming 30 mask layers", 2019 DoD
contract funded the third cleanroom and copper. Tier: high-level.

**CYP-16** — Austin Lyons (Chipstrat), *"Understanding SkyWater"*,
2025-11-15. <https://www.chipstrat.com/p/understanding-skywater>.
Includes the 1991 acquisition terms ("$26.5m semiconductor facility,
land and some equipment for $11.5m and … leased manufacturing
equipment which costs $32m for just $3.2m", citing TechMonitor) and
"The Minnesota fab is a 200mm fab at 90nm+ geometries". Tier:
high-level.

### 5.2 The S8 130 nm SONOS process in Cypress's own words

**CYP-20** — Electronics Weekly, *"Cypress 4-Mbit non-volatile static
random access memory"*, 2007-10-18.
<https://www.electronicsweekly.com/news/products/memory-products/cypress-4-mbit-non-volatile-static-random-access-memory-2007-10/>.
"The new 4-Mbit nvSRAMs are the first manufactured on Cypress's S8(tm)
0.13-micron SONOS (Silicon Oxide Nitride Oxide Silicon) embedded
nonvolatile memory technology". Tier: cross-check (S8 name).

**CYP-21** — Tech Monitor, *"Cypress expands non-volatile SRAM
portfolio"*, 2009-10-07.
<https://www.techmonitor.ai/technology/data/cypress_expands_non_volatile_sram_portfolio_081009>.
"its nvSRAMs are manufactured on S8 0.13-micron SONOS … embedded
non-volatile memory technology". Tier: high-level.

**CYP-22** — Cypress / UMC, *"Cypress and UMC Deliver ICs on New
65-Nanometer SONOS Embedded Flash Technology"*, PR Newswire,
2011-07-27.
<https://www.prnewswire.com/news-releases/cypress-and-umc-deliver-ics-on-new-65-nanometer-sonos-embedded-flash-technology-126238008.html>.
Compares S65 with "the current 130-nanometer S8 process" and states
the SONOS module "only requires three additional mask layers to a
standard CMOS process". Tier: cross-check.

**CYP-23** — Cypress, *"Cypress Signs Innopower to Enable SONOS-Based
Embedded Flash Solutions for 130-nm and 65-nm Technology Nodes"*,
2011-02-17 (verified copy at Design & Reuse; the Business Wire
original timed out).
<https://www.design-reuse.com/news/25684/65-nm-sonos-embedded-nonvolatile-memory-ip.html>.
"has been shipping in high volumes at 130-nm at several foundries".
Tier: high-level.

**CYP-24** — Krishnaswamy Ramkumar (Cypress), *"Cypress SONOS — A
Scalable Embedded Flash Technology"*, ChipEstimate.com technical
article, 2008-10-21.
<https://www.chipestimate.com/Cypress-SONOS-A-Scalable-Embedded-Flash-Technology/Cypress-Semiconductor/Technical-Article/2008/10/21>.
SONOS module "can easily be embedded into a logic process flow … with
the addition of three to five masking layers"; retention "20 years
after 100K cycles". Tier: high-level.

**CYP-25** — K. Ramkumar, V. Prabhakar and R. Kapre (Cypress
Semiconductor), *"Scalable SONOS based embedded non-volatile memory
technology"*, Semiconductor Digest, 2020-02.
<https://sst.semiconductor-digest.com/2020/02/scalable-sonos-based-embedded-non-volatile-memory-technology/>.
Integration cost (extra masks), cell-size scaling from 130 nm to
28 nm, channel engineering with indium. Tier: deep dive.

**CYP-26** — Wikipedia, *"SONOS"*. <https://en.wikipedia.org/wiki/SONOS>.
Notes Cypress as a SONOS supplier (IP licensing from 2011) and gives
typical ONO thicknesses ("2 nm thick oxide lower layer, a 5 nm thick
silicon nitride middle layer, and a 5–10 nm oxide upper layer"). Tier:
high-level.

### 5.3 Cypress patents on the SONOS module and its integration

All four are assigned to Cypress Semiconductor Corporation at grant
(later reassigned to Longitude Flash Memory Solutions / Monterey
Research). They are the best public description of the ONO deposition
recipe and of where the SONOS module sits in a 130 nm logic flow.

**PAT-01** — US 6,969,689 B1, *"Method of manufacturing an
oxide-nitride-oxide (ONO) dielectric for SONOS-type devices"*,
K. Ramkumar, M. Rathor, B. Parameshwaran, L. Lancaster; filed
2002-06-28, granted 2005-11-29.
<https://patents.google.com/patent/US6969689B1/en>. Tunnel oxide
"less than about 25 Å", charge-storing nitride "less than about 200 Å
… preferably less than about 100 Å", top oxide "less than about 50 Å";
all three layers formed in one furnace window of "about 700° C. to
about 875° C." using NH₃, dichlorosilane and N₂O by LPCVD. Tier:
deep dive.

**PAT-02** — US 2009/0179253 A1, *"Oxide-nitride-oxide stack having
multiple oxynitride layers"*, S. Levy, K. Ramkumar, F. Jenne, S. Geha;
filed 2007-06-13, published 2009-07-16.
<https://patents.google.com/patent/US20090179253A1/en>. Tunnel oxide
"from about 15 Å to about 22 Å", multi-layer charge-trapping layer
"about 70 Å to about 150 Å", blocking oxide "about 30 Å to about 70 Å";
LPCVD at 700–850 °C, 5–500 mTorr, N₂O/NH₃ and DCS/NH₃ gas ratios.
Tier: deep dive.

**PAT-03** — US 8,093,128 B2, *"Integration of non-volatile charge trap
memory devices and logic CMOS devices"*, W. Koutny et al. (Cypress);
filed 2008-05-22, granted 2012-01-10.
<https://patents.google.com/patent/US8093128B2/en>. Order of the SONOS
module relative to the logic well/channel implants, gate oxidation at
"800° C. and 900° C.", nitridation at "900-1100° C.", blocking oxide
3.0–5.0 nm. Tier: deep dive.

**PAT-04** — US 8,796,098 B1, *"Embedded SONOS based memory cells"*,
K. Ramkumar, I. Kouznetsov, V. Prabhakar (Cypress); filed 2013-09-04,
granted 2014-08-05.
<https://patents.google.com/patent/US8796098B1/en>. Pad oxide 10–20 nm,
tunnel dielectric 1.0–4.0 nm, oxynitride charge-trapping layers
2.0–5.0 nm, blocking oxide ~3–4.5 nm, HV gate oxide 5–7 nm, LV gate
oxide 1–3 nm, indium channel doping. Tier: deep dive.

*Searches for Cypress patents specifically on STI, TiN local
interconnect, poly resistors or TiW/AlCu metallisation returned only
generic results; none is listed here.*

### 5.4 SONOS papers (non-Cypress) useful for the 130 nm node

**PAP-01** — M. H. White, D. A. Adams and J. Bu, *"On the go with
SONOS"*, IEEE Circuits and Devices Magazine, vol. 16, no. 4, pp. 22–31,
2000-07, DOI 10.1109/101.857747.
<https://ieeexplore.ieee.org/document/857747/>. Classic review of
scaled SONOS. Tier: deep dive.

**PAP-02** — M.-K. Seo et al. (Samsung), *"A 130-nm 0.9-V 66-MHz 8-Mb
(256K × 32) local SONOS embedded flash EEPROM"*, IEEE Journal of
Solid-State Circuits, vol. 40, no. 4, pp. 877–883, 2005-04,
DOI 10.1109/JSSC.2005.845564.
<https://ieeexplore.ieee.org/document/1424218/>. A 0.13 µm
logic-compatible SONOS embedded flash from another vendor; cell size
and P/E conditions for comparison. Tier: deep dive.

**PAP-03** — Y. Kim et al. (Samsung), *"Highly manufacturable SONOS
non-volatile memory for the embedded SoC solution"*, 2003 Symposium on
VLSI Technology, pp. 31–32, DOI 10.1109/VLSIT.2003.1221071. Tier: deep
dive.

**PAP-04** — Wang et al., *"A million cycle 0.13um 1Mb embedded SONOS
Flash memory using Successive Approximated Read Calibration"*, IEEE
CICC 2008, pp. 427–430, DOI 10.1109/CICC.2008.4672111. Tier: deep dive.

**PAP-05** — Taniguchi et al., *"SONOS Embedded Flash IP Using
Trap-Depth-Controlled SiN Film Enabling Data Retention more than 10
years at 200°C"*, 2023 IEEE International Memory Workshop, DOI
10.1109/IMW56887.2023.10145990.
<https://ieeexplore.ieee.org/document/10145990/>. SONOS on a 130 nm BCD
platform with three added masks. Tier: deep dive.

(IEEE Xplore pages return a JavaScript challenge to automated fetches;
the bibliographic data above were verified through the Crossref
metadata API for each DOI.)

## 6. Trade press and analyst coverage of the Bloomington fab

**PRESS-01** — Joanne Itow (Semico Research), *"A Different Foundry
Model"*, Semiconductor Engineering, 2019-10-17.
<https://semiengineering.com/skywater-the-right-foundry-at-the-right-time/>.
"Today SkyWater is running an all-aluminum 90nm process"; "It does not
even run 300mm wafers"; SkyTech Center for customer-dedicated tools;
DMEA accreditation. Tier: high-level.

**PRESS-02** — Mark LaPedus, *"200mm Fab Crunch"*, Semiconductor
Engineering, 2018-05-21.
<https://semiengineering.com/200mm-fab-crunch/> (PDF copy hosted by
SkyWater:
<https://www.skywatertechnology.com/wp-content/uploads/2018/05/200mm-Fab-Crunch-Semi-Engineering-180521.pdf>).
"SkyWater has one 200mm fab with 0.35-micron, 90nm and other
processes"; context on the used-200 mm-equipment shortage that shapes
what tools such fabs can buy. Tier: high-level.

**PRESS-03** — Willy Shih, Forbes, *"Inside SkyWater Technology's
Domestic Semiconductor Foundry"*, 2020-10-28.
<https://www.forbes.com/sites/willyshih/2020/10/28/skywater-technology-and-domestic-production-of-semiconductors/>.
"SkyWater is still using 200 mm wafers"; 90 nm production, move to
65 nm; two fab photographs. Tier: high-level.

**PRESS-04** — Samuel K. Moore, IEEE Spectrum, *"U.S. Invests in Fabs
That Make Radiation-Hardened Chips"*, 2019-10-29.
<https://spectrum.ieee.org/us-invests-in-radiationhardenedchip-fabs>.
5,500 m² expansion, copper interconnect "to support node scaling to
65 nm and 45 nm". Tier: high-level.

**PRESS-05** — Samuel K. Moore, IEEE Spectrum, *"The Foundry at the
Heart of DARPA's Plan to Let Old Fabs Beat New Ones"*, 2018-08-06.
<https://spectrum.ieee.org/the-foundry-at-the-heart-of-darpas-plan-to-let-old-fabs-beat-new-ones>.
"a lot of the government work is done around 90 nm"; 200 mm wafers;
carbon-nanotube handling protocols. Tier: high-level.

**PRESS-06** — Electronics Weekly (David Manners), *"US DoD invests
$170m in SkyWater fab"*, 2019-10-22.
<https://www.electronicsweekly.com/news/business/us-dod-invests-170m-skywater-fab-2019-10/>.
"operates an old 200mm Cypress fab in Bloomington". Tier: high-level.

**PRESS-07** — Semiconductor Digest, *"US Department of Defense to
Invest up to $170M in SkyWater's Domestic Technology Foundry"*,
2019-10.
<https://www.semiconductor-digest.com/us-department-of-defense-to-invest-up-to-170m-in-skywaters-domestic-technology-foundry/>.
Tier: high-level.

**PRESS-08** — Cleanroom Technology, *"SkyWater to expand
microelectronics production with government contract"*, 2019-10-22.
<https://www.cleanroomtechnology.com/news/article_page/Skywater_to_expand_microelectronics_production_with_government_contract/159234>.
Quotes "8,000 sqft of new cleanroom area" (SKW-11 says up to
15,000 sq ft; GOV-03/GOV-04 give 8,400–13,000 sq ft built). Tier:
high-level.

**PRESS-09** — Evertiq, *"SkyWater expands in Florida – assumes
operation of 200mm fab"*, 2021-01-27. <https://evertiq.com/news/49475>.
Mentions the October 2020 ribbon-cutting for the Bloomington
expansion. Tier: high-level.

**PRESS-10** — Semiconductor Today, *"SkyWater investing $56m in
capacity expansion and 200mm GaN foundry"*, 2021-07-27.
<https://www.semiconductor-today.com/news_items/2021/jul/skywater-270721.shtml>.
Tier: high-level.

**PRESS-11** — Chipstrat, Asianometry, AnySilicon, Star Tribune — see
CYP-02, CYP-03, CYP-04, CYP-14, CYP-15, CYP-16 above.

*Not retrievable:* EE Times, *"Cypress Sells Minnesota Fab for $30
Million"* (2017-03) and EDN's Cypress SONOS licensing articles timed
out or refused every fetch and are therefore not listed with URLs;
the Klobuchar and Minnesota DEED press pages (2021, 2024) returned
HTTP 403 / a CAPTCHA. No public fab-tour photo essay with tool counts
was found beyond the photographs in CYP-02, CYP-03 and PRESS-03.

## 7. Teardowns, die photographs and cross-sections of SKY130 silicon

**TD-01** — ZeptoBars, *"TT04 – looking inside TinyTapeout 4 (GDS
included): weekend die-shot"*, 2024-07-11.
<https://zeptobars.com/en/read/tt04-tinytapeout-silicon-inside-gds-sky130>.
Optical die photographs of a Tiny Tapeout 4 chip (SKY130, MPW,
5256 µm × 3662 µm die) before and after HF removal of the glass and
metal layers, down to the STI pattern, with side-by-side GDS overlays.
Useful for checking layer geometry and the visual appearance of
metal 5 fill, but there are no measured thicknesses. Tier: cross-check
(layout ↔ silicon), high-level for the stack.

**TD-02** — Matt Venn (Zero to ASIC), *"Looking inside an open source
ASIC with Zeptobars"*, 2024-08-03 (interview and video).
<https://www.zerotoasiccourse.com/post/interview_with_zeptobars/>,
<https://www.youtube.com/watch?v=zUv6sdxOaFE>. Describes the
decapsulation and de-layering method used for TD-01. Tier: high-level.

**TD-03** — Tiny Tapeout, *"Tiny Tapeout 4"* chip page.
<https://tinytapeout.com/chips/tt04/>. Identifies the design and
shuttle whose silicon was imaged in TD-01. Tier: high-level.

**TD-04** — The Amp Hour, episode 616, *"Open Source Tapeout with
Matthew Venn"*.
<https://theamphour.com/616-open-source-tapeout-with-matthew-venn/>.
Background on the open MPW programme that produced the imaged chips.
Tier: high-level.

*Not found.* No public SEM/FIB cross-section of a SKY130 or Cypress S8
die with measured film thicknesses was located (searches covered
siliconpr0n.org, TechInsights/Chipworks teasers, arXiv and IEEE). The
siliconpr0n archive page for a Cypress PSoC 4 part
(`azonenberg:cypress:cy8c4245axi`) exists but sits behind a bot
challenge and could not be read, so it is not listed with a URL. For
now the PDK stack diagram (PDK-04) and the Edwards slides (ANN-16)
remain the only public statements of film thicknesses.

## 8. General 130 nm-era process integration references

These are the references every step page can lean on for "how it is
typically performed" and for typical numeric values. Library records
are cited so that the edition can be identified unambiguously.

### 8.1 Textbooks

**TXT-01** — J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
Technology: Fundamentals, Practice and Modeling*, Prentice Hall, 2000,
ISBN 978-0-13-085037-9.
<https://openlibrary.org/isbn/9780130850379>. Oxidation, diffusion,
implantation, thin films, etch and back-end with models; the standard
graduate text for this era. Tier: high-level.

**TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
ISBN 978-0-9616721-6-4.
<https://openlibrary.org/isbn/9780961672164>. Unit processes (wafer
cleaning, oxidation, LPCVD/PECVD, sputtering, lithography, plasma
etch, implantation). Tier: high-level.

**TXT-03** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 2:
Process Integration*, Lattice Press, 1990, ISBN 978-0-9616721-4-0.
<https://openlibrary.org/isbn/9780961672140>. Isolation, wells,
contacts, multilevel metal, passivation. Tier: high-level.

**TXT-04** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
<https://openlibrary.org/isbn/9780961672157>. LDD/extension, halo,
hot-carrier and gate-oxide engineering. Tier: high-level.

**TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
Deep-Submicron Process Technology*, Lattice Press, 2002,
ISBN 978-0-9616721-7-1.
<https://openlibrary.org/isbn/9780961672171>. STI, CMP, W plugs, salicide,
DUV lithography, RTP — written for exactly the 0.25–0.13 µm
generations. Tier: high-level.

**TXT-06** — S. M. Sze (ed.), *VLSI Technology*, 2nd ed., McGraw-Hill,
1988, ISBN 978-0-07-062735-2.
<https://openlibrary.org/isbn/9780070627352>. Tier: high-level.

**TXT-07** — M. Quirk and J. Serda, *Semiconductor Manufacturing
Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
<https://openlibrary.org/isbn/9780130815200>. Fab-floor view of each
tool class, written around a 200 mm, 0.18 µm-era fab. Tier: high-level.

**TXT-08** — H. Xiao, *Introduction to Semiconductor Manufacturing
Technology*, 2nd ed., SPIE Press, 2012, ISBN 978-0-8194-9092-6.
<https://openlibrary.org/isbn/9780819490926>; publisher page
<https://spie.org/Publications/Book/924283>. Tier: high-level.

**TXT-09** — Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
Manufacturing Technology*, 2nd ed., CRC Press, 2007,
ISBN 978-1-57444-675-3.
<https://openlibrary.org/isbn/9781574446753>. Chapter-per-process
reference with equipment detail. Tier: high-level.

**TXT-10** — R. B. Fair (ed.), *Rapid Thermal Processing: Science and
Technology*, Academic Press, 1993, ISBN 978-0-12-247690-7.
<https://openlibrary.org/isbn/9780122476907>. Tier: deep dive.

### 8.2 ITRS roadmaps (2001 and 2003 editions)

Semiconductor Industry Association archive pages:
<https://www.semiconductors.org/resources/2001-international-technology-roadmap-for-semiconductors-itrs/>
and
<https://www.semiconductors.org/resources/2003-international-technology-roadmap-for-semiconductors-itrs/>.
The chapters most useful for a 130 nm flow (all verified PDFs):

**ITRS-01** — ITRS 2001, *Front End Processes*.
<https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>.
Starting material, STI, gate stack, junctions, contacts. Tier: deep dive.

**ITRS-02** — ITRS 2001, *Interconnect*.
<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Interconnect.pdf>.
Al versus Cu, dielectric k, via/metal dimensions by node. Tier: deep dive.

**ITRS-03** — ITRS 2001, *Lithography*.
<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>.
Exposure tools and wavelengths (i-line, 248 nm, 193 nm) by node. Tier:
deep dive.

**ITRS-04** — ITRS 2001, *Process Integration, Devices, and Structures*.
<https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>.
Gate length, oxide thickness, junction depth targets. Tier: deep dive.

**ITRS-05** — ITRS 2003, *Front End Processes*, *Interconnect*,
*Lithography* and *PIDS* chapters.
<https://www.semiconductors.org/wp-content/uploads/2018/08/FEP2003.pdf>,
<https://www.semiconductors.org/wp-content/uploads/2018/08/Interconnect2003.pdf>,
<https://www.semiconductors.org/wp-content/uploads/2018/08/Litho2003.pdf>,
<https://www.semiconductors.org/wp-content/uploads/2018/08/PIDS2003.pdf>.
Tier: deep dive.

### 8.3 Review papers (DOIs verified through Crossref)

**REV-01** — M. Nandakumar, A. Chatterjee, S. Sridhar, K. Joyner,
M. Rodder and I.-C. Chen, *"Shallow trench isolation for advanced ULSI
CMOS technologies"*, IEDM 1998 Technical Digest, pp. 133–136,
DOI 10.1109/IEDM.1998.746297. STI flow: trench definition, corner
rounding, gap fill, planarisation, well implants. Tier: deep dive.

**REV-02** — M. Krishnan, J. W. Nalaskowski and L. M. Cook, *"Chemical
Mechanical Planarization: Slurry Chemistry, Materials, and
Mechanisms"*, Chemical Reviews, vol. 110, no. 1, pp. 178–204, 2010,
DOI 10.1021/cr900170z. Oxide, tungsten and copper CMP chemistry. Tier:
deep dive.

**REV-03** — E. K. Broadbent and C. L. Ramiller, *"Selective Low
Pressure Chemical Vapor Deposition of Tungsten"*, Journal of The
Electrochemical Society, vol. 131, no. 6, pp. 1427–1433, 1984,
DOI 10.1149/1.2115864.
<https://iopscience.iop.org/article/10.1149/1.2115864>. Foundational
WF₆/H₂ and WF₆/SiH₄ kinetics behind W plug fill. Tier: deep dive.

**REV-04** — S.-L. Zhang and M. Östling, *"Metal Silicides in CMOS
Technology: Past, Present, and Future Trends"*, Critical Reviews in
Solid State and Materials Sciences, vol. 28, no. 1, pp. 1–129, 2003,
DOI 10.1080/10408430390802431. TiSi₂, CoSi₂ and NiSi salicide. Tier:
deep dive.

**REV-05** — E. C. Jones and E. Ishida, *"Shallow junction doping
technologies for ULSI"*, Materials Science and Engineering: R, vol. 24,
no. 1–2, pp. 1–80, 1998, DOI 10.1016/S0927-796X(98)00013-8. Low-energy
implantation, transient-enhanced diffusion, extension/halo formation
and RTA. Tier: deep dive.

**REV-06** — M. H. White, D. A. Adams and J. Bu, *"On the go with
SONOS"* — see PAP-01. Tier: deep dive.

### 8.4 Encyclopaedia articles (high-level entry points)

All verified on 2026-08-30:

* *Shallow trench isolation* — <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
* *Chemical-mechanical polishing* — <https://en.wikipedia.org/wiki/Chemical-mechanical_polishing>
* *Rapid thermal processing* — <https://en.wikipedia.org/wiki/Rapid_thermal_processing>
* *Ion implantation* — <https://en.wikipedia.org/wiki/Ion_implantation>
* *Photolithography* (g/h/i-line and KrF/ArF wavelengths) — <https://en.wikipedia.org/wiki/Photolithography>
* *Reactive-ion etching* — <https://en.wikipedia.org/wiki/Reactive-ion_etching>
* *Chemical vapor deposition* (LPCVD, PECVD) — <https://en.wikipedia.org/wiki/Chemical_vapor_deposition>
* *Sputter deposition* — <https://en.wikipedia.org/wiki/Sputter_deposition>
* *Salicide* — <https://en.wikipedia.org/wiki/Salicide>
* *Front end of line* — <https://en.wikipedia.org/wiki/Front_end_of_line>
* *Back end of line* — <https://en.wikipedia.org/wiki/Back_end_of_line>
* *SONOS* — see CYP-26
* *130 nm process* — see ANN-17
