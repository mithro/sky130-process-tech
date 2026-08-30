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
