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
refer to them unambiguously. The footnote labels on the step, category,
landing and glossary pages are these keys in lower case (`PDK-03` →
`[^pdk-03]`, `DEAL-1965` → `[^deal-1965]`), so every label used on a
written page has exactly one entry here; the inventory holds 1113
keyed entries as of 2026-09-13, and `tools/check_refs.py` keeps the
page-side labels well formed. Sections 8.4 (keyed Wikipedia entries),
8.8, 8.9, 8.10, 8.11, 8.12, 8.13, 8.14, 8.15, 8.16 and 8.17 were added
to cover the sources the writers of the step, category and overview
pages introduced; a
"Label ↔ key" note marks the few cases where one source has two keys.

:::{note}
Everything in this inventory is publicly available. Where a public
source could not be retrieved (dead link, paywall, bot-blocking), it is
not cited.
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
contact (`mcon`) drawn CD 0.17 µm and "standard contact bottom CD" 0.09 µm, licon bottom CD 0.08 µm, via 0.15 µm. Tier: cross-check.

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
SPNIT (7.5), plus the MiM layers `capm` and `cap2m`. It also labels
the inter-level dielectric / via heights directly: li top to met1
bottom (NILD2) 0.265 µm, via1 (NILD3) 0.27 µm, via2 (NILD4) 0.42 µm,
via3 (NILD5) 0.39 µm, via4 (NILD6) 0.505 µm, LINT 0.075 µm, TOPOX
0.09 µm, TOPNIT 0.54 µm on metal (0.3777 µm from the metal-5 bottom to its top in the field, on our
reading of the drawing), NILD3_C/NILD4_C liners 0.030 µm, PSG
0.6099 µm over the gate and 0.4299 µm over field poly; and levels
above the substrate: FOX top 0.3262, li bottom 0.9361, li top 1.0111,
met1 bottom 1.3761, met2 bottom 2.0061, met3 bottom 2.7861, met4
bottom 4.0211, met5 bottom 5.3711, and PI1 top 11.8834 µm (further
labels 5.2523, 6.1346, 0.4223 and 0.070 µm dimension the
metal5/passivation region). Tier: cross-check.

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
RCX, Device details). The *Antenna Rules* chapter
(<https://skywater-pdk.readthedocs.io/en/main/rules/antenna.html>)
defines the ratio of interconnect area exposed to plasma etch (bottom
areas of licon, mcon, via and via2; perimeter areas of poly, li and
met1–met3) to the connected gate area, layer by layer; step 125 cites
it under this key. Tier: cross-check.

**PDK-PERIPH** — *Periphery rules* page.
<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>.
The numeric design rules by layer. Values used on the step pages:
difftap.1 (width of diff or tap) 0.150 µm; difftap.3 (spacing of diff
to diff, tap to tap, or non-abutting diff to tap) 0.270 µm; dnwell.2
(minimum width of deep N-well) 3.000 µm; dnwell.3 (minimum spacing
between deep N-wells, marked "Rule exempt inside UHVI") 6.300 µm;
dnwell.6 (RF NMOS enclosure by deep N-well); nwell.5 and nwell.6
(enclosure rules between deep N-well and N-well); poly.2 (spacing of
poly to poly) 0.210 µm; licon.2 (spacing of licon to licon) 0.170 µm.
Tier: cross-check.

**PDK-HV** — *High Voltage Methodology* page.
<https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>.
Design methodology for the HV and VHV (drain-extended) devices: "The
VHV devices need to be designed with drain extentions (DE) fabricated
by lightly doped Nwells and Pwells respectively"; "All VHV devices use
110A gate oxide thickness just like standard 5.0V Vcc devices"; drawn
channel lengths of 1.055 µm and 1.050 µm for the 16 V VHV NMOS and
PMOS; "Under no circumstances the poly/extended drain overlap and
field oxide length should be changed". Tier: cross-check.

**PDK-WLCSP** — *WLCSP Rules* page.
<https://skywater-pdk.readthedocs.io/en/main/rules/wlcsp.html>
(tables: <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/wlcsp/amkor.csv>,
<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/wlcsp/deca.csv>).
Two tables of wafer-level chip-scale package rules. The Amkor table
has `pi1`, `rdl`, `pi2`, `ubm` and `bump` rule sets at 400 µm and
500 µm pitch; the DECA table has `cpbo` ("1st polyimide (mask)"),
`rdl`, `cpmm2` ("2nd polyimide"), `ubm` and `bump` rule sets, each with
a function line (for `rdl`, "Re-distribution layer connects the top
metal from the customer to the bumps"). The masks index cites it for
the `PBO`, `CU1M` and `PMM2` entries of PDK-05. Tier: cross-check.

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
Forward with the First Ever Open Foundry PDK"*, 2020-11-16.
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

**STEPS-SHEET** — *[external] S8 / SKY130 Process Steps* (public Google
Sheet), retrieved 2026-09-13.
<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>.
The source of the 171-step list used in this reference (tab "Sheet1":
step number, code and description, `SMAT` to `HPETEST`). Further tabs:
"Masks" (the mask steps with their step numbers); "Run Mask IDs" (the
PDK mask table set against MPW-1 to MPW-8, recording for each run
whether a plate exists for each mask, its plate ID, and notes including
the sky130B ReRAM masks `RRM` and `VIMC`); "SKY130 MPW-3 Mask
Information" (photographs of via-2 and via-3 plates); "Random Mask Case
Label Info" (Photronics plate-case labels: 6 × 6 × 0.25 in blanks, 4×,
CD specifications); and "Sheet4" (mask types, e.g.
`F4-248-EAPSM-A43-APRX` for `VIM2`/`VIM3` and `B4-248-BIM-LSR-WET` for
`VIM4`). Each tab can be exported anonymously as CSV. Used on the
landing page, the steps index, every step page and the mask index.
Tier: cross-check.

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
* *Physical analysis* — "FEI Dual Beam FIB/SEM", "Hitachi S-4800",
  "SELA EM2 Precision Cleave", "Oxford PlasmaLab RIE deprocessing",
  "Allied TechPrep polisher".

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
A photograph caption (re-checked 2026-09-13) reads "Weebit ReRAM bitcell
is shown integrated into the S130 technology between Metal1 and
Metal2"; the module includes "a 256Kb ReRAM array". Tier: cross-check.

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
Names a "Novellus high density plasma tool" and the "SEZ etcher tool";
photo captions show technicians troubleshooting "an implanter" and,
separately, servicing tool robots (robot teach points, "a robot fault
on a Novellus high density plasma tool", "a motor for a robot on a SEZ
etcher tool") and "the pneumatic controls of a vacuum system". Tier:
cross-check (tool naming).

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
400 jobs, facility "Originally commissioned by Control Data Corporation
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
feet"; raw-material suppliers, given in a run-in paragraph headed
"Raw materials." under "Manufacturing" (GlobalWafers Singapore and SEH
America wafers, Honeywell Electronic Materials sputter targets, Air
Products and Praxair gases, KMG Chemicals; photoresist from "The Dow
Chemical Company", "JSR Corporation" and "Tokyo Ohka Kogyo America,
Inc."; developer from Air Products, Moses Lake); "Advantages of 200
millimeter Wafer Fabs". Note: SEC.gov rejects fetches without a
descriptive `User-Agent`. Tier: cross-check.

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

Job-listing sites are heavily bot-protected; only the postings below
could actually be retrieved. Posting text changes frequently, so each
entry records the retrieval date.

**JOB-01** — Indeed, *"Skywater Technology Foundry Jobs, Employment in
Bloomington, MN"* (listing page), retrieved 2026-08-30; listings
expire, and the page refused later automated retrieval (HTTP 403,
2026-09-13).
<https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>.
The *Defect Technician 2* posting reads "General operation of
semiconductor defect metrology tools: SEM/AIT/KLA/SP1/EV300/1X" —
i.e. KLA-Tencor AIT (patterned-wafer inspection), SP1 (unpatterned
Surfscan) and an "EV300" review tool (vendor not stated in the posting). Other
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
2024-10-30), retrieved 2026-08-30.
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

**PAT-STI-CR** — US 7,439,141 B2, *"Shallow trench isolation approach
for improved STI corner rounding"*, U. Kim, Y. Sun, M. S. Chang et al.;
priority date 2001-12-27, assigned to Spansion LLC, granted 2008-10-21.
<https://patents.google.com/patent/US7439141B2/en>. Double liner
oxidation scheme: first liner grown to "approximately 100-300 Å" at
"900-1100 degrees Celsius", second liner "approximately 100-500 Å",
pad-oxide undercut of "approximately 100-300 Å" by HF before the first
liner oxidation, isolation oxide polished back level with the nitride,
nitride then stripped "to expose the pad oxide". This patent
originated at Spansion and came into Cypress's portfolio only through
the 2015 Spansion merger; it is **not** evidence for the S8 flow and is
used on the step pages only for era-typical STI values. Tier: deep
dive.

*Searches for Cypress-originated patents on STI, TiN local
interconnect, poly resistors or TiW/AlCu metallisation returned only
generic results; the one STI patent in Cypress's hands (PAT-STI-CR)
came from Spansion.*

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
* *Thermal oxidation* (Deal–Grove growth, silicon consumption) — <https://en.wikipedia.org/wiki/Thermal_oxidation>
* *Silicon nitride* (LPCVD reaction, hot H₃PO₄ etch, oxidation mask) — <https://en.wikipedia.org/wiki/Silicon_nitride>
* *Plasma-enhanced chemical vapor deposition* (high-density plasma, SiH₄/O₂/Ar oxide) — <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
* *Wafer (electronics)* (200 mm wafer thickness and notch) — <https://en.wikipedia.org/wiki/Wafer_(electronics)>
* *RCA clean* (SC-1 and SC-2) — <https://en.wikipedia.org/wiki/RCA_clean>
* *Multi-threshold CMOS* (why several thresholds are offered; how they are set) — <https://en.wikipedia.org/wiki/Multi-threshold_CMOS>
* *Threshold voltage* (body-effect parameter containing the channel doping) — <https://en.wikipedia.org/wiki/Threshold_voltage>
* *CMOS* (NMOS on the p-substrate, PMOS in an N-well) — <https://en.wikipedia.org/wiki/CMOS>
* *Latch-up* (the parasitic n-p-n-p path through the wells) — <https://en.wikipedia.org/wiki/Latch-up>
* *Plasma ashing* (downstream ashing, implanted-resist problems) — <https://en.wikipedia.org/wiki/Plasma_ashing>
* *LDMOS* (drift regions formed by chained implants) — <https://en.wikipedia.org/wiki/LDMOS>
* *Furnace anneal* (furnace anneals being supplanted by RTA) — <https://en.wikipedia.org/wiki/Diffusion_furnace>
* *SONOS* — see CYP-26
* *130 nm process* — see ANN-17

The pages cite the articles above and a number of others by label.
Every Wikipedia label in use on the pages has a keyed entry here so
that the inventory is complete; the articles are entry points, not
evidence, and are cited only in the *High-level* tier. All were
fetched when the citing page was written or reviewed (2026-08-30 to
2026-09-12).

**WIKI-4T** — Wikipedia, *Four-terminal sensing*.
<https://en.wikipedia.org/wiki/Four-terminal_sensing> Four-terminal
(Kelvin) sensing, the principle behind four-point-probe and Kelvin
contact measurements. Used on the test category page. Tier: high-level.

**WIKI-ADVANTEST** — Wikipedia, *Advantest*.
<https://en.wikipedia.org/wiki/Advantest> Company article on the
test-equipment maker Advantest. Used on the test category page. Tier:
high-level.

**WIKI-AGILENT** — Wikipedia, *Agilent Technologies*.
<https://en.wikipedia.org/wiki/Agilent_Technologies> Company article on
Agilent Technologies, successor to the HP test-and-measurement business
behind the 4062UX tester. Used on the test category page. Tier:
high-level.

**WIKI-AMAT** — Wikipedia, *Applied Materials*.
<https://en.wikipedia.org/wiki/Applied_Materials> Company article on
Applied Materials. Used on the substrate category page. Tier:
high-level.

**WIKI-ANNEALING** — Wikipedia, *Annealing (materials science)*.
<https://en.wikipedia.org/wiki/Annealing_(materials_science)> Annealing
in materials science: recovery, recrystallisation and grain growth. Used
on the anneal category page. Tier: high-level.

**WIKI-ARC** — Wikipedia, *Anti-reflective coating*.
<https://en.wikipedia.org/wiki/Anti-reflective_coating> ARCs in
photolithography, BARC. Used on steps 035 and 036 and the lithography
category page. Tier: high-level.

**WIKI-ARRHENIUS** — Wikipedia, *Arrhenius equation*.
<https://en.wikipedia.org/wiki/Arrhenius_equation> Arrhenius temperature
dependence of rate constants, used for diffusion and etch rates. Used on
the anneal category page. Tier: high-level.

**WIKI-ASH** — Wikipedia, *Plasma ashing*.
<https://en.wikipedia.org/wiki/Plasma_ashing> Downstream ashing and
implanted-resist problems. Used on steps 016, 021, 025, 029 and 033 and
the strip category page. Tier: high-level.

**WIKI-ASH3** — Wikipedia, *Arsine*.
<https://en.wikipedia.org/wiki/Arsine> Arsine, the arsenic source gas
for implanters. Used on the implant category page. Tier: high-level.

**WIKI-ASM** — Wikipedia, *ASM International*.
<https://en.wikipedia.org/wiki/ASM_International> Company article on ASM
International (vertical furnaces, ALD). Used on the substrate category
page. Tier: high-level.

**WIKI-ATE** — Wikipedia, *Automatic test equipment*.
<https://en.wikipedia.org/wiki/Automatic_test_equipment> Automatic test
equipment: what a tester and handler do at wafer sort and final test.
Used on the test category page. Tier: high-level.

**WIKI-AXCELIS** — Wikipedia, *Axcelis Technologies*.
<https://en.wikipedia.org/wiki/Axcelis_Technologies> Company article on
Axcelis Technologies, the former Eaton implanter business. Used on the
implant category page. Tier: high-level.

**WIKI-BF3** — Wikipedia, *Boron trifluoride*.
<https://en.wikipedia.org/wiki/Boron_trifluoride> Boron trifluoride, the
boron source gas for B⁺ and BF₂⁺ implants. Used on the implant category
page. Tier: high-level.

**WIKI-BOE** — Wikipedia, *Buffered oxide etch*.
<https://en.wikipedia.org/wiki/Buffered_oxide_etch> BOE composition and
etch rate. Used on steps 039 and 046 and the etch category page. Tier:
high-level.

**WIKI-CD** — Wikipedia, *Critical dimension*.
<https://en.wikipedia.org/wiki/Critical_dimension> Critical dimension:
the smallest printed feature and how it is measured. Used on the
lithography category page. Tier: high-level.

**WIKI-CERIA** — Wikipedia, *Cerium(IV) oxide*.
<https://en.wikipedia.org/wiki/Cerium(IV)_oxide> Cerium(IV) oxide, the
abrasive in high-selectivity STI slurries. Used on the cmp category
page. Tier: high-level.

**WIKI-CHANNEL** — Wikipedia, *Channelling (physics)*.
<https://en.wikipedia.org/wiki/Channelling_(physics)> Ion channelling
along crystal axes and why implants use tilt and twist. Used on the
implant category page. Tier: high-level.

**WIKI-CMOS** — Wikipedia, *CMOS*. <https://en.wikipedia.org/wiki/CMOS>
NMOS on the p-substrate, PMOS in an N-well. Used on steps 017, 018 and
026. Tier: high-level.

**WIKI-CMP** — Wikipedia, *Chemical-mechanical polishing*.
<https://en.wikipedia.org/wiki/Chemical-mechanical_polishing> Pads,
conditioners, abrasives, endpoint and REB + CMP for STI. Used on step
012 and the cmp category page. Tier: high-level.

**WIKI-COLLOIDAL-SILICA** — Wikipedia, *Colloidal silica*.
<https://en.wikipedia.org/wiki/Colloidal_silica> Colloidal silica, the
abrasive in conventional oxide slurries. Used on the cmp category page.
Tier: high-level.

**WIKI-CTF** — Wikipedia, *Charge trap flash*.
<https://en.wikipedia.org/wiki/Charge_trap_flash> Why trapped charge
tolerates oxide defects. Used on step 040. Tier: high-level.

**WIKI-CVD** — Wikipedia, *Chemical vapor deposition*.
<https://en.wikipedia.org/wiki/Chemical_vapor_deposition> LPCVD in
context. Used on step 003 and the deposition category page. Tier:
high-level.

**WIKI-CZ** — Wikipedia, *Czochralski method*.
<https://en.wikipedia.org/wiki/Czochralski_method> Czochralski crystal
pulling for silicon boules. Used on the substrate category page. Tier:
high-level.

**WIKI-DEPLETION** — Wikipedia, *Depletion and enhancement modes*.
<https://en.wikipedia.org/wiki/Depletion_and_enhancement_modes> The sign
of the threshold in each mode. Used on step 038. Tier: high-level.

**WIKI-DG** — Wikipedia, *Deal–Grove model*.
<https://en.wikipedia.org/wiki/Deal%E2%80%93Grove_model> The
rate-constant table and the thin-oxide caveat. Used on steps 043 and 047
and the oxidation category page. Tier: high-level.

**WIKI-DNQ** — Wikipedia, *Diazonaphthoquinone*.
<https://en.wikipedia.org/wiki/Diazonaphthoquinone> Diazonaphthoquinone,
the photoactive compound of i-line novolak resists. Used on the
lithography category page. Tier: high-level.

**WIKI-DOPANT** — Wikipedia, *Dopant*.
<https://en.wikipedia.org/wiki/Dopant> Dopants in silicon: group III and
V elements and what they do. Used on the implant category page. Tier:
high-level.

**WIKI-DRY-ETCH** — Wikipedia, *Dry etching*.
<https://en.wikipedia.org/wiki/Dry_etching> Dry etching overview: plasma
etching, RIE and ion milling. Used on the etch category page. Tier:
high-level.

**WIKI-EM** — Wikipedia, *Electromigration*.
<https://en.wikipedia.org/wiki/Electromigration> Electromigration in
interconnects and the Al–Cu remedy. Used on the deposition category
page. Tier: high-level.

**WIKI-EPITAXY** — Wikipedia, *Epitaxy*.
<https://en.wikipedia.org/wiki/Epitaxy> Epitaxial growth and its
terminology. Used on the substrate category page. Tier: high-level.

**WIKI-ETCHING** — Wikipedia, *Etching (microfabrication)*.
<https://en.wikipedia.org/wiki/Etching_(microfabrication)> Etching in
microfabrication: wet versus dry, isotropic versus anisotropic. Used on
the etch category page. Tier: high-level.

**WIKI-EXCIMER** — Wikipedia, *Excimer laser*.
<https://en.wikipedia.org/wiki/Excimer_laser> Excimer lasers, the KrF
(248 nm) and ArF (193 nm) sources of DUV steppers. Used on the
lithography category page. Tier: high-level.

**WIKI-FG** — Wikipedia, *Forming gas*.
<https://en.wikipedia.org/wiki/Forming_gas> The 5 % H₂ in N₂ mixture and
interface passivation. Used on the anneal category page. Tier:
high-level.

**WIKI-FICK** — Wikipedia, *Fick's laws of diffusion*.
<https://en.wikipedia.org/wiki/Fick%27s_laws_of_diffusion> Fick's laws,
the basis of diffusion and Deal–Grove modelling. Used on the anneal
category page. Tier: high-level.

**WIKI-FURNACE** — Wikipedia, *Furnace anneal*.
<https://en.wikipedia.org/wiki/Diffusion_furnace> Furnace anneals being
supplanted by RTA. The label keeps the page's *Furnace anneal* wording;
the article is titled *Diffusion furnace*. Used on step 034 and the
anneal category page. Tier: high-level.

**WIKI-FZ** — Wikipedia, *Float-zone silicon*.
<https://en.wikipedia.org/wiki/Float-zone_silicon> Float-zone silicon
and why CZ material is used for CMOS substrates instead. Used on the
substrate category page. Tier: high-level.

**WIKI-GATE-OXIDE** — Wikipedia, *Gate oxide*.
<https://en.wikipedia.org/wiki/Gate_oxide> What the gate oxide does and
withstands. Label ↔ key: the same article is cited as `wiki-gox` on the
oxidation category page. Used on steps 043, 044 and 047. Tier:
high-level.

**WIKI-GOX** — Wikipedia, *Gate oxide*.
<https://en.wikipedia.org/wiki/Gate_oxide> Gate oxide: role, thickness
scaling and leakage. Label ↔ key: the same article is cited as
`wiki-gate-oxide` on steps 043, 044 and 047. Used on the oxidation
category page. Tier: high-level.

**WIKI-GW** — Wikipedia, *GlobalWafers*.
<https://en.wikipedia.org/wiki/GlobalWafers> Company article on
GlobalWafers, a wafer supplier named in SkyWater's Form S-1 (SEC-01).
Used on the substrate category page. Tier: high-level.

**WIKI-H3PO4** — Wikipedia, *Phosphoric acid*.
<https://en.wikipedia.org/wiki/Phosphoric_acid> Phosphoric acid, the hot
nitride-strip chemistry. Used on the etch and strip category pages.
Tier: high-level.

**WIKI-HF** — Wikipedia, *Hydrofluoric acid*.
<https://en.wikipedia.org/wiki/Hydrofluoric_acid> Hydrofluoric acid, the
oxide etchant, and its hazards. Used on the etch and strip category
pages. Tier: high-level.

**WIKI-ICP** — Wikipedia, *Inductively coupled plasma*.
<https://en.wikipedia.org/wiki/Inductively_coupled_plasma> Inductively
coupled plasma, the source type behind TCP and DPS etchers. Used on the
etch category page. Tier: high-level.

**WIKI-IMPLANT** — Wikipedia, *Ion implantation*.
<https://en.wikipedia.org/wiki/Ion_implantation> Energies, ranges,
channelling, amorphisation and implanter classes. Used on steps 007,
008, 015, 018, 019, 020, 023, 024, 027, 028, 031, 032, 037, 038 and 045
and the implant category page. Tier: high-level.

**WIKI-KEITHLEY** — Wikipedia, *Keithley Instruments*.
<https://en.wikipedia.org/wiki/Keithley_Instruments> Company article on
Keithley Instruments (parametric test systems). Used on the test
category page. Tier: high-level.

**WIKI-KLA** — Wikipedia, *KLA Corporation*.
<https://en.wikipedia.org/wiki/KLA_Corporation> The inspection and
metrology vendor. Used on the lithography and substrate category pages.
Tier: high-level.

**WIKI-LATCHUP** — Wikipedia, *Latch-up*.
<https://en.wikipedia.org/wiki/Latch-up> The parasitic n-p-n-p path
through the wells. Used on steps 017, 018 and 027 and the substrate
category page. Tier: high-level.

**WIKI-LDMOS** — Wikipedia, *LDMOS*.
<https://en.wikipedia.org/wiki/LDMOS> Drift regions formed by chained
implants. Used on steps 030, 031 and 032. Tier: high-level.

**WIKI-LITHO** — Wikipedia, *Photolithography*.
<https://en.wikipedia.org/wiki/Photolithography> The process sequence,
the resolution equation and wavelengths. Used on steps 004, 007, 014,
017, 022, 026, 030, 035, 041 and 044 and the lithography category page.
Tier: high-level.

**WIKI-LOCOS** — Wikipedia, *LOCOS*.
<https://en.wikipedia.org/wiki/LOCOS> LOCOS isolation, the predecessor
of STI. Used on the oxidation category page. Tier: high-level.

**WIKI-MASK** — Wikipedia, *Photomask*.
<https://en.wikipedia.org/wiki/Photomask> Photomasks: substrates,
absorber and pellicles. Used on the lithography category page. Tier:
high-level.

**WIKI-MEMC** — Wikipedia, *MEMC Electronic Materials*.
<https://en.wikipedia.org/wiki/MEMC_Electronic_Materials> Company
article on MEMC Electronic Materials, the wafer maker later part of
SunEdison Semiconductor and GlobalWafers. Used on the substrate category
page. Tier: high-level.

**WIKI-MILLER** — Wikipedia, *Miller index*.
<https://en.wikipedia.org/wiki/Miller_index> Miller indices for crystal
planes such as (100). Used on the substrate category page. Tier:
high-level.

**WIKI-MONOSI** — Wikipedia, *Monocrystalline silicon*.
<https://en.wikipedia.org/wiki/Monocrystalline_silicon> Monocrystalline
silicon as the wafer material. Used on the substrate category page.
Tier: high-level.

**WIKI-MTCMOS** — Wikipedia, *Multi-threshold CMOS*.
<https://en.wikipedia.org/wiki/Multi-threshold_CMOS> Why several
thresholds are offered and how they are set. Used on steps 014, 015,
020, 022, 023 and 045. Tier: high-level.

**WIKI-NA** — Wikipedia, *Numerical aperture*.
<https://en.wikipedia.org/wiki/Numerical_aperture> Numerical aperture
and its place in the Rayleigh resolution criterion. Used on the
lithography category page. Tier: high-level.

**WIKI-NMP** — Wikipedia, *N-Methyl-2-pyrrolidone*.
<https://en.wikipedia.org/wiki/N-Methyl-2-pyrrolidone>
N-Methyl-2-pyrrolidone, a solvent-strip chemistry. Used on the strip
category page. Tier: high-level.

**WIKI-OPC** — Wikipedia, *Optical proximity correction*.
<https://en.wikipedia.org/wiki/Optical_proximity_correction> Optical
proximity correction of mask shapes. Used on the lithography category
page. Tier: high-level.

**WIKI-PECVD** — Wikipedia, *Plasma-enhanced chemical vapor deposition*.
<https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
High-density plasma, sputtering during deposition, SiH₄/O₂/Ar oxide.
Used on step 011 and the deposition category page. Tier: high-level.

**WIKI-PH3** — Wikipedia, *Phosphine*.
<https://en.wikipedia.org/wiki/Phosphine> Phosphine, the phosphorus
source gas for implanters. Used on the implant category page. Tier:
high-level.

**WIKI-PIRANHA** — Wikipedia, *Piranha solution*.
<https://en.wikipedia.org/wiki/Piranha_solution> SPM ratios and
temperature. Used on the strip category page. Tier: high-level.

**WIKI-PLASMA-ETCH** — Wikipedia, *Plasma etching*.
<https://en.wikipedia.org/wiki/Plasma_etching> Plasma etching mechanisms
and chemistries. Used on the etch category page. Tier: high-level.

**WIKI-POLY** — Wikipedia, *Polycrystalline silicon*.
<https://en.wikipedia.org/wiki/Polycrystalline_silicon> Polycrystalline
silicon as a gate and resistor material. Used on the deposition category
page. Tier: high-level.

**WIKI-POLYURETHANE** — Wikipedia, *Polyurethane*.
<https://en.wikipedia.org/wiki/Polyurethane> Polyurethane, the CMP pad
material. Used on the cmp category page. Tier: high-level.

**WIKI-PROBECARD** — Wikipedia, *Probe card*.
<https://en.wikipedia.org/wiki/Probe_card> Probe cards for wafer test.
Used on the test category page. Tier: high-level.

**WIKI-PSG** — Wikipedia, *Phosphosilicate glass*.
<https://en.wikipedia.org/wiki/Phosphosilicate_glass> Phosphosilicate
glass, the doped CVD dielectric. Used on the deposition category page.
Tier: high-level.

**WIKI-PSM** — Wikipedia, *Phase-shift mask*.
<https://en.wikipedia.org/wiki/Phase-shift_mask> Phase-shift masks as a
resolution-enhancement technique. Used on the lithography category page.
Tier: high-level.

**WIKI-PVD** — Wikipedia, *Physical vapor deposition*.
<https://en.wikipedia.org/wiki/Physical_vapor_deposition> Physical
vapour deposition overview. Used on the deposition category page. Tier:
high-level.

**WIKI-RC** — Wikipedia, *Contact resistance*.
<https://en.wikipedia.org/wiki/Contact_resistance> Contact resistance
and specific contact resistivity. Used on the test category page. Tier:
high-level.

**WIKI-RCA** — Wikipedia, *RCA clean*.
<https://en.wikipedia.org/wiki/RCA_clean> SC-1 and SC-2 compositions and
temperatures. Used on steps 001, 002, 006, 009, 010, 013, 016, 021, 025,
029, 033, 039 and 046 and the strip category page. Tier: high-level.

**WIKI-RESIST** — Wikipedia, *Photoresist*.
<https://en.wikipedia.org/wiki/Photoresist> Photoresist chemistry, tone
and processing. Used on the lithography and strip category pages. Tier:
high-level.

**WIKI-RET** — Wikipedia, *Resolution enhancement technologies*.
<https://en.wikipedia.org/wiki/Resolution_enhancement_technologies>
Resolution enhancement technologies: OPC, phase-shift masks and off-axis
illumination. Used on the lithography category page. Tier: high-level.

**WIKI-RIE** — Wikipedia, *Reactive-ion etching*.
<https://en.wikipedia.org/wiki/Reactive-ion_etching> RF frequency,
self-bias, pressure range and ICP sources. Used on steps 005, 006, 036
and 042 and the etch category page. Tier: high-level.

**WIKI-RS** — Wikipedia, *Sheet resistance*.
<https://en.wikipedia.org/wiki/Sheet_resistance> Sheet resistance and
the ohms-per-square convention. Used on the test category page. Tier:
high-level.

**WIKI-RTP** — Wikipedia, *Rapid thermal processing*.
<https://en.wikipedia.org/wiki/Rapid_thermal_processing> Lamp heating,
seconds above 1000 °C, in-situ pyrometry. Used on step 034 and the
anneal and oxidation category pages. Tier: high-level.

**WIKI-SALICIDE** — Wikipedia, *Salicide*.
<https://en.wikipedia.org/wiki/Salicide> The two-anneal self-aligned
silicide sequence. Used on the anneal category page. Tier: high-level.

**WIKI-SCE** — Wikipedia, *Short-channel effect*.
<https://en.wikipedia.org/wiki/Short-channel_effect> Depletion-region
overlap and DIBL. Used on step 037. Tier: high-level.

**WIKI-SEH** — Wikipedia, *Shin-Etsu Chemical*.
<https://en.wikipedia.org/wiki/Shin-Etsu_Chemical> Company article on
Shin-Etsu Chemical, parent of the wafer maker Shin-Etsu Handotai. Used
on the substrate category page. Tier: high-level.

**WIKI-SI** — Wikipedia, *Silicon*.
<https://en.wikipedia.org/wiki/Silicon> Silicon's properties, including
the melting point. Used on the substrate category page. Tier:
high-level.

**WIKI-SILTRONIC** — Wikipedia, *Siltronic*.
<https://en.wikipedia.org/wiki/Siltronic> Company article on the wafer
maker Siltronic. Used on the substrate category page. Tier: high-level.

**WIKI-SIN** — Wikipedia, *Silicon nitride*.
<https://en.wikipedia.org/wiki/Silicon_nitride> The LPCVD reaction, hot
H₃PO₄ etch and use as an oxidation mask. Used on steps 003, 013, 040, 042
and 135 and the deposition category page. Tier: high-level.

**WIKI-SKYWATER** — Wikipedia, *SkyWater Technology*.
<https://en.wikipedia.org/wiki/SkyWater_Technology> Fab history and 200
mm capacity. Label ↔ key: the same article as ANN-18. Used on the
substrate category page. Tier: high-level.

**WIKI-SONOS** — Wikipedia, *SONOS*.
<https://en.wikipedia.org/wiki/SONOS> SONOS memory cell structure and
operation. Label ↔ key: the same article as CYP-26; both labels are in
use on the pages. Used on the oxidation category page. Tier: high-level.

**WIKI-SPC** — Wikipedia, *Statistical process control*.
<https://en.wikipedia.org/wiki/Statistical_process_control> Statistical
process control charts and limits. Used on the test category page. Tier:
high-level.

**WIKI-SPUTTER** — Wikipedia, *Sputter deposition*.
<https://en.wikipedia.org/wiki/Sputter_deposition> Sputter deposition:
magnetron sources, targets and step coverage. Used on the deposition
category page. Tier: high-level.

**WIKI-SRIM** — Wikipedia, *Stopping and Range of Ions in Matter*.
<https://en.wikipedia.org/wiki/Stopping_and_Range_of_Ions_in_Matter>
SRIM, the Monte Carlo range and straggle calculator for implants. Used
on the implant category page. Tier: high-level.

**WIKI-STEPPER** — Wikipedia, *Stepper*.
<https://en.wikipedia.org/wiki/Stepper> Steppers and step-and-scan
systems: reduction optics, alignment and overlay. Used on the
lithography category page. Tier: high-level.

**WIKI-STI** — Wikipedia, *Shallow trench isolation*.
<https://en.wikipedia.org/wiki/Shallow_trench_isolation> The three STI
operations and the LOCOS cross-over node. Used on steps 002, 003, 005,
006, 007, 011, 012 and 013 and the cmp and oxidation category pages.
Tier: high-level.

**WIKI-SUMCO** — Wikipedia, *SUMCO*.
<https://en.wikipedia.org/wiki/SUMCO> Company article on the wafer maker
SUMCO. Used on the substrate category page. Tier: high-level.

**WIKI-TEOS** — Wikipedia, *Tetraethyl orthosilicate*.
<https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate> Tetraethyl
orthosilicate, the liquid precursor for CVD oxide. Used on the
deposition category page. Tier: high-level.

**WIKI-TERADYNE** — Wikipedia, *Teradyne*.
<https://en.wikipedia.org/wiki/Teradyne> Company article on the
test-equipment maker Teradyne. Used on the test category page. Tier:
high-level.

**WIKI-TEST** — Wikipedia, *Wafer testing*.
<https://en.wikipedia.org/wiki/Wafer_testing> Parametric versus
functional test and the wafermap. Used on the test category page. Tier:
high-level.

**WIKI-THINFILM** — Wikipedia, *Thin film*.
<https://en.wikipedia.org/wiki/Thin_film> Thin films: deposition methods
and properties. Used on the deposition category page. Tier: high-level.

**WIKI-THOX** — Wikipedia, *Thermal oxidation*.
<https://en.wikipedia.org/wiki/Thermal_oxidation> Reaction, silicon
consumption, chlorine additions and dry–wet–dry cycles. Used on steps
002, 010, 038 and 043 and the oxidation category page. Tier: high-level.

**WIKI-TIN** — Wikipedia, *Titanium nitride*.
<https://en.wikipedia.org/wiki/Titanium_nitride> Titanium nitride as a
barrier and local-interconnect material. Used on the deposition category
page. Tier: high-level.

**WIKI-TISI2** — Wikipedia, *Titanium disilicide*.
<https://en.wikipedia.org/wiki/Titanium_disilicide> Titanium disilicide
and its C49-to-C54 phase transformation. Used on the anneal category
page. Tier: high-level.

**WIKI-TLM** — Wikipedia, *Transfer length method*.
<https://en.wikipedia.org/wiki/Transmission_line_measurement> The
transfer-length (transmission-line) method for contact resistance. The
label keeps the page's *Transfer length method* wording; the article is
titled *Transmission line measurement*. Used on the test category page.
Tier: high-level.

**WIKI-TMAH** — Wikipedia, *Tetramethylammonium hydroxide*.
<https://en.wikipedia.org/wiki/Tetramethylammonium_hydroxide>
Tetramethylammonium hydroxide, the standard aqueous resist developer.
Used on the lithography category page. Tier: high-level.

**WIKI-VARIAN** — Wikipedia, *Varian Semiconductor*.
<https://en.wikipedia.org/wiki/Varian_Semiconductor> Company article on
Varian Semiconductor Equipment (implanters; now part of Applied
Materials). Used on the implant category page. Tier: high-level.

**WIKI-VDP** — Wikipedia, *Van der Pauw method*.
<https://en.wikipedia.org/wiki/Van_der_Pauw_method> The van der Pauw
method for sheet resistance and Hall measurements. Used on the test
category page. Tier: high-level.

**WIKI-VT** — Wikipedia, *Threshold voltage*.
<https://en.wikipedia.org/wiki/Threshold_voltage> The body-effect
parameter containing the channel doping. Used on steps 015, 020, 023 and
045 and the implant and test category pages. Tier: high-level.

**WIKI-WAFER** — Wikipedia, *Wafer (electronics)*.
<https://en.wikipedia.org/wiki/Wafer_(electronics)> Diameters,
thickness, notch, orientation and doping ranges. Used on step 001 and
the substrate category page. Tier: high-level.

**WIKI-WF6** — Wikipedia, *Tungsten hexafluoride*.
<https://en.wikipedia.org/wiki/Tungsten_hexafluoride> Tungsten
hexafluoride, the CVD tungsten precursor. Used on the deposition
category page. Tier: high-level.

### 8.5 Papers and patents used for era-typical isolation-module values

None of these is a SkyWater or Cypress source; the step pages for the
isolation module (steps 001–013) use them for typical numbers and
mechanisms of a 130 nm-era STI and deep N-well module. DOIs were
verified through the Crossref API and patents through Google Patents
on 2026-08-30.

**VGH-1967** — W. van Gelder and V. E. Hauser, *"The Etching of Silicon
Nitride in Phosphoric Acid with Silicon Dioxide as a Mask"*, Journal of
The Electrochemical Society, vol. 114, no. 8, p. 869, 1967,
DOI 10.1149/1.2426757.
<https://iopscience.iop.org/article/10.1149/1.2426757>. Hot phosphoric
acid etch rates of silicon nitride, silicon dioxide and silicon, i.e.
the selectivity behind every wet nitride strip. Tier: deep dive.

**THUNG-2016** — B. J. Thung, K. Ibrahim, N. A. Manap and
F. Salehuddin, *"Challenges for 0.13µm Generation Shallow Trench
Isolation on 0.18µm Equipment Platform"*, Journal of Telecommunication,
Electronic and Computer Engineering (JTEC), vol. 8, no. 5, pp. 15–21,
2016.
<https://jtec.utem.edu.my/jtec/article/view/697> (PDF:
<https://jtec.utem.edu.my/jtec/article/download/697/707/3255>). A
foundry account of running 0.13 µm STI on 0.18 µm-generation tools:
definition of the fill aspect ratio, HDP void / poly-stringer yield
loss, OPC on the STI layout, liner oxidation, post-etch wet clean,
phosphoric-acid nitride strip. The journal page lists the first author
as "Thung Beng Joo" (family name Thung). Tier: deep dive.

**NISHIMURA-2002** — H. Nishimura, S. Takagi, M. Fujino and N. Nishi,
*"Gap-Fill Process of Shallow Trench Isolation for 0.13 µm
Technologies"*, Japanese Journal of Applied Physics, vol. 41, part 1,
no. 5A, pp. 2886–2893, 2002, DOI 10.1143/JJAP.41.2886. HDP-CVD
gap-fill modelling (sputter-yield angular dependence and ionic
deposition) demonstrated on STI "of space width 0.13 µm and aspect
ratio 3.9". Tier: deep dive.

**CHEW-2002** — K. W. Chew, J. Zhang, K. Shao, W. B. Loh and S.-F. Chu,
*"Impact of Deep N-well Implantation on Substrate Noise Coupling and RF
Transistor Performance for Systems-on-a-Chip Integration"*, ESSDERC
2002, pp. 251–254, DOI 10.1109/ESSDERC.2002.194917. Deep N-well as a
substrate-noise isolation structure. Tier: deep dive.

**YANG-2005** — M. T. Yang, D. C. W. Kuo, C. W. Kuo, Y. J. Wang,
P. P. C. Ho, T. J. Yeh and S. Liu, *"Characterization and model of
on-chip flicker noise with deep Nwell (DNW) isolation for 130nm and
beyond SOC"*, ICMTS 2005, pp. 125–129, DOI 10.1109/ICMTS.2005.1452242.
Deep N-well isolation at the 130 nm node. Tier: deep dive.

**KAO-1987** — D.-B. Kao, J. P. McVittie, W. D. Nix and K. C. Saraswat,
*"Two-dimensional thermal oxidation of silicon — I. Experiments"*,
IEEE Transactions on Electron Devices, vol. 34, no. 5, pp. 1008–1017,
1987, DOI 10.1109/T-ED.1987.23037. Oxidation of curved silicon "is
retarded at low temperatures and sharp curvatures, and … the
retardation is more severe on concave than convex structures"
(abstract). Tier: deep dive.

**KAO-1988** — D.-B. Kao, J. P. McVittie, W. D. Nix and K. C. Saraswat,
*"Two-dimensional thermal oxidation of silicon. II. Modeling stress
effects in wet oxides"*, IEEE Transactions on Electron Devices,
vol. 35, no. 1, pp. 25–37, 1988, DOI 10.1109/16.2412. Viscous-stress
model of the corner retardation. Tier: deep dive.

**PAT-STI-AMBERWAVE** — US 6,960,781 B2, *"Shallow trench isolation
process"*, M. T. Currie and A. J. Lochtefeld; original assignee
AmberWave Systems Corporation, granted 2005-11-01; assigned to Taiwan
Semiconductor Manufacturing Co. on 2010-01-26.
<https://patents.google.com/patent/US6960781B2/en>. Pad oxide
"50-200 Å", nitride "500-2000 Å", trench depth "3000-4000 Å", CMP
"using the silicon nitride layer over the active area as a stop
layer", liner oxidation optionally in steam or below 1000 °C. Tier:
deep dive.

**PAT-STI-LATTICE** — US 7,985,656 B1, *"Shallow trench isolation (STI)
with trench liner of increased thickness"*, S. Mehta, S. Logie and
S. Fong (Lattice Semiconductor), granted 2011-07-26.
<https://patents.google.com/patent/US7985656B1/en>. Liner "in the range
of approximately 10 nm to approximately 30 nm" grown by "a high
temperature (for example, in excess of approximately 1000 degrees C.)
oxide growth process". Tier: deep dive.

**PAT-DNW-HYNIX** — US 6,806,133 B2, *"Method for fabricating
semiconductor device with triple well structure"*, J.-G. Oh (Hynix
Semiconductor), granted 2004-10-19.
<https://patents.google.com/patent/US6806133B2/en>. Deep N-well by
³¹P⁺ implantation "with an ion implantation energy of about 0.6 MeV to
about 1.6 MeV" and a dose of "about 5×10¹² ions/cm² to about
1.5×10¹³ ions/cm²", performed after the STI field oxide is formed.
Tier: deep dive.

### 8.6 Vendor, facility and marketplace pages for representative tools

Used to describe tool classes that SKW-01 names only by vendor and
family; none of these pages mentions SkyWater.

**LAM-SPEED** — Novellus Systems (Lam Research newsroom), *"Novellus'
SPEED Max HDP-CVD Dielectric Gapfill System Extends STI Application to
32nm"*, press release, 2009-10-05.
<https://newsroom.lamresearch.com/2009-10-05-NOVELLUS-SPEED-R-MAX-HDP-CVD-DIELECTRIC-GAPFILL-SYSTEM-EXTENDS-STI-APPLICATION-TO-32nm>.
"HDP is still the preferred gapfill dielectric technology for advanced
geometries"; "tailoring the deposition, etch, and sputter-to-deposition
(S/D) ratio"; "enlarged remote plasma source". Tier: cross-check
(vendor statement).

**AXCELIS-GSD** — Axcelis Technologies, *"Axcelis Announces
Introduction Of The 'GSD Ovation' High Current And High Energy Batch
Implanters"*, PR Newswire, 2021-11-02.
<https://www.prnewswire.com/news-releases/axcelis-announces-introduction-of-the-gsd-ovation-high-current-and-high-energy-batch-implanters-301412520.html>.
Calls the GSD series "the industry benchmark for the longest
manufactured and supported batch ion implanter" and names "the GSD/HE
Ovation with energies up to 3 MeV, and the GSD/VHE Ovation with
energies up to 4.9 MeV". Tier: cross-check (vendor statement).

**SNF-9400** — Stanford Nanofabrication Facility, *"Lam Research TCP
9400 Poly Etcher (lampoly)"* equipment page.
<https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>.
"a Transformer Coupled Plasma (TCP) etcher, generates a uniform, high
density plasma for selective etching of silicon and polysilicon"; the
gas list includes chlorine, hydrogen bromide, oxygen and
tetrafluoromethane. Tier: high-level.

**AVIZA-AVP** — Moov used-equipment marketplace, *"Aviza / SVG /
Thermco AVP 8000"* listing.
<https://moov.co/marketplace/furnaces-diffusion/aviza-svg/aviza-asml-svg-watkinsjohnson-avp-8000>.
"The AVP-8000 is a vertical batch furnace with a flexible platform for
diffusion, oxidation, and LPCVD processes … can handle 150-200mm
wafers." A dealer listing rather than a vendor data sheet. Tier:
high-level (weak).

**AXCELIS-GSD-PAGE** — Axcelis Technologies, *"GSD Ovation — High
Current & High Energy Batch Ion Implanters"*, product page, accessed
2026-08-30. <https://www.axcelis.com/products/gsd-ovation/>. Describes
the GSD/HE as a "10 stage LINAC with energies up to 3 MeV" and notes
"source operating costs especially with fluorinated species". Distinct
from the PR Newswire release AXCELIS-GSD. Tier: cross-check (vendor
statement).

**AXCELIS-8250** — Semiconductor Online, *"8250HT Medium Current Ion
Implanter"* (Eaton Semiconductor Equipment Operations product
description).
<https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>.
The 8250HT covers "3keV to 750keV" with beam currents "between 4µA and
3,500µA"; the medium-current class that SKW-01 lists as "Axcelis 8250".
Tier: high-level (vendor description reproduced by a trade site).

**AG-8800** — SemiStar Corp., *"AG Associates Heatpulse 8800 / 8808
Rapid Thermal Processing"* (reseller specification page), accessed
2026-08-30.
<https://www.semistarcorp.com/product/ag-associates-heatpulse-8800-8808/>.
"Recommended steady-state temperature range: 400 – 1200°C", ramp-up
"Programmable, 1 – 180°C per second", "2 banks of 14 lamps" with
"10-zone lamp control", pyrometer or thermocouple sensing, wafer sizes
to 8 inches, "Implant annealing" among the applications. Tier:
high-level (reseller page for the tool SKW-01 lists as "Ag Heatpulse
8808").

**AG-8108** — SemiStar Corp., *"AG Associates Heatpulse 4100 / 8108 /
8800 / 8800i Specifications"* (reseller PDF), accessed 2026-08-30.
<http://www.semistarcorp.com/wp-content/uploads/2025/12/AG-Associates-Heatpulse-4100-8108-8800-8800i-Specifications-Rapid-Thermal-Processor.pdf>.
Although titled for the whole family, the PDF documents the operating
specifications of the Heatpulse 4100: 400–1200 °C, maximum ramp
150 °C/s, ±5 °C uniformity across a 150 mm wafer at 1150 °C, and a
facility table (cooling water, CDA/N₂). Tier: high-level (weak for the
8808 itself).

### 8.7 Well and channel-implant module sources

None of these is a SkyWater or Cypress source; the step pages for the
well and channel-implant module (steps 014–034) use them for typical
numbers, mechanisms and further reading on threshold-adjust implants,
retrograde wells, implant-resist lithography and stripping,
drain-extended devices and the well anneal. DOIs were verified through
the Crossref API on 2026-09-12; patents were verified on Google
Patents by the reviewer of the module (Google Patents refused
automated access from the editing host).

**PAT-VT-RRR** — US 2011/0006372 A1, *"Formation of standard voltage
threshold and low voltage threshold MOSFET devices"*, M. Helm and
X. Zhou (Round Rock Research; priority 2002-07-08), published
2011-01-13.
<https://patents.google.com/patent/US20110006372A1/en>. Low-Vt NMOS
and PMOS defined by masked Vt-adjust implants: "an implant of Arsenic"
as a first adjustment, a "boron type of implant such as BF2, or
Indium" as a second, and a "counter-doped channel region". Tier: deep
dive.

**PAT-VT-LSI** — US 5,963,801 A, *"Method of forming retrograde well
structures and punch-through barriers using low energy implants"*,
S. Aronowitz, L. Khan and J. Kimball (LSI Logic), granted 1999-10-05.
<https://patents.google.com/patent/US5963801A/en>. Threshold-adjust
boron "implanted through the sacrificial gate oxide in doses between
1×10¹² and 1×10¹³ atoms/cm² … at implant energies between 50 and
100 keV"; chained punch-through barriers at 100, 70 and 50 keV; a
furnace anneal at "approximately 900 °C … for approximately 30
minutes". Tier: deep dive.

**PAT-VT-AMD** — US 6,238,982 B1, *"Multiple threshold voltage
semiconductor device fabrication technology"*, Z. Krivokapic and
O. Milic (AMD), granted 2001-05-29.
<https://patents.google.com/patent/US6238982B1/en>. Channel implant
"approximately 10-20 KeV for boron or 45-90 KeV for BF₂ at a
concentration of about 1.0 to 2.5×10¹³ ions/cm²". Tier: deep dive.

**PAT-WELL-IBM** — US 6,667,205 B2, *"Method of forming retrograde
n-well and p-well"*, M. J. Breitwisch, C. H. Lam and J. A. Slinkman
(IBM), granted 2003-12-23.
<https://patents.google.com/patent/US6667205B2/en>. Photoresist
"typically 1800–2500 nm in thickness"; N-well phosphorus 850 keV at
5.2 × 10¹³ cm⁻², 550 keV at 1.25 × 10¹² cm⁻² and 50 keV at
5 × 10¹¹ cm⁻²; P-well boron 550, 150 and 45 keV; "The concentration of
dopant is higher at the bottom of the well and lower at the upper
surface of the well". Tier: deep dive.

**PAT-WELL-HYNIX** — US 6,455,402 B2, *"Method of forming retrograde
doping profile in twin well CMOS device"*, J.-H. Lee and J.-H. Son
(Hyundai/Hynix), granted 2002-09-24.
<https://patents.google.com/patent/US6455402B2/en>. N-well 700 keV at
2.0 × 10¹³ cm⁻² plus 120 keV at 2.0 × 10¹² cm⁻²; P-well 350 keV at
1.5 × 10¹³ cm⁻², 150 keV at 6.0 × 10¹² cm⁻² and 80 keV at
1.0 × 10¹² cm⁻²; "an annealing at 1000 C for 10 sec in an RTA" before
gate oxidation. Tier: deep dive.

**PAT-TWIN-HARRIS** — US 5,247,199 A, *"Process for forming twin well
CMOS integrated circuits"*, D. A. Matlock (Harris Corporation), granted
1993-09-21. <https://patents.google.com/patent/US5247199A/en>. Twin
wells by chained implants — 500/275/130 keV phosphorus and
360/185/55 keV boron — with "an implant blocking photoresist layer 18"
patterned to expose the region "adjacent to N-type well 17". Tier:
deep dive.

**PAT-UMC-DC** — US 5,393,679 A, *"Use of double charge implant to
improve retrograde process PMOS punch through voltage"*, S.-H. Yang
(United Microelectronics), granted 1995-02-28.
<https://patents.google.com/patent/US5393679A/en>. Retrograde well by
"double charge … P++ … at an energy within a range from about 380 keV
to about 400 keV" on a medium-current implanter. Tier: deep dive.

**PAT-RESIST-ZILOG** — US 6,576,405 B1, *"High aspect ratio
photolithographic method for high energy implantation"*, S. J. Buffat
and J. L. Adams (Zilog), granted 2003-06-10.
<https://patents.google.com/patent/US6576405B1/en>. Resist "minimum
thicknesses of 3.4 µm … with the preferred thickness for the resist
between 3.8 µm and 4.2 µm" for a 1.3–1.5 MeV phosphorus N-well and a
600–800 keV boron P-well. Tier: deep dive.

**PAT-DEMOS-TI** — US 6,660,603 B2, *"Higher voltage drain extended
MOS transistors with self-aligned channel and drain extensions"*,
J. C. Mitros (Texas Instruments), granted 2003-12-09.
<https://patents.google.com/patent/US6660603B2/en>. Drain-extended
transistors "use a very lightly doped extension region adjacent to the
drain that depletes at high drain voltages", formed from "the n-well
region … as the lightly doped drain extension region"; boron "at doses
of 2×10¹² cm² to 7×10¹³ cm² at energies of about 40 keV" for the
p-type well and "phosphorous species at about 8×10¹² cm² to
7×10¹³ cm² at an energy of about 150 keV" for the n-type. Tier: deep
dive.

**PAT-DEMOS-TI2** — US 2006/0006461 A1, *"Drain extended MOS
transistors and methods for making the same"*, P. R. Chidambaram
(Texas Instruments), published 2006-01-12.
<https://patents.google.com/patent/US20060006461A1/en>. DE devices
made "without the addition of extra masks or processing steps". Tier:
deep dive.

**PAT-FUJ** — US 7,605,041 B2, *"Semiconductor device and its
manufacture method"*, T. Ema, H. Kojima and T. Anezaki (Fujitsu),
granted 2009-10-20. <https://patents.google.com/patent/US7605041B2/en>.
A 400 keV, 1.5 × 10¹³ cm⁻² boron p-well in a triple-well HV/flash
integration. Tier: deep dive.

**PAT-STRIP-MOSEL** — US 5,811,358 A, *"Low temperature dry process
for stripping photoresist after high dose ion implantation"*,
M.-S. Tseng, F.-H. Chao and N.-Y. Tsai (Mosel Vitelic), granted
1998-09-22. <https://patents.google.com/patent/US5811358A/en>. The
popping mechanism — volatile bulk resist that can "build up pressure
beneath the implant-hardened surface layer" during a conventional
"high temperature (>200° C.) dry ashing" — and a first stage "removed
by oxygen and nitrogen/hydrogen plasma in a low-temperature (<220 °C)
environment". Tier: deep dive.

**PAT-STRIP-TSMC** — US 2004/0214448 A1, *"Method of ashing a
photoresist"*, B.-W. Chan, Y.-H. Chiu and H.-J. Tao (TSMC), published
2004-10-28. <https://patents.google.com/patent/US20040214448A1/en>.
After implantation "the top portion of the photoresist layer is
transformed into a carbonized crust that is difficult to remove because
of its low solubility in wet strippers". Tier: deep dive.

**PAT-STRIP-ULVAC** — US 5,795,831 A, *"Cold processes for cleaning
and stripping photoresist from surfaces of semiconductor wafers"*,
I. Nakayama et al. (ULVAC Technologies), granted 1998-08-18.
<https://patents.google.com/patent/US5795831A/en>. A cold stripping
and cleaning process for implanted resist, an alternative to hot
ashing. Tier: deep dive.

**PAT-RESURF-TI** — US 5,406,110 A, *"Resurf lateral double diffused
insulated gate field effect transistor"*, O.-K. Kwon, T. R. Efland,
S. Malhi and W. T. Ng (Texas Instruments), granted 1995-04-11.
<https://patents.google.com/patent/US5406110A/en>. A RESURF lateral
DMOS with an implanted drift region. Tier: deep dive.

**PAT-RTP-AMAT** — US 5,155,336 A, *"Rapid thermal heating apparatus
and method"*, C. M. Gronet and J. F. Gibbons (Applied Materials),
granted 1992-10-13. <https://patents.google.com/patent/US5155336A/en>.
A lamp-heated single-wafer RTP chamber design. Tier: deep dive.

**PAT-RTP-TAMARACK** — US 4,649,261 A, *"Apparatus for heating
semiconductor wafers in order to achieve annealing, silicide
formation, reflow of glass passivation layers, etc."*, R. E. Sheets
(Tamarack Scientific), granted 1987-03-10.
<https://patents.google.com/patent/US4649261A/en>. An early
lamp-heating apparatus for wafer annealing. Tier: deep dive.

**HOOK-2003** — T. B. Hook, J. Brown, P. Cottrell, E. Adler,
D. Hoyniak, J. Johnson and R. Mann, *"Lateral Ion Implant Straggle and
Mask Proximity Effect"*, IEEE Transactions on Electron Devices,
vol. 50, no. 9, pp. 1946–1951, 2003, DOI 10.1109/TED.2003.815371
(open copy:
<https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>).
"Some of the ions scattered out of the edge of the photoresist are
implanted in the silicon surface near the mask edge, altering the
threshold voltage of those devices", with shifts "of up to 100 mV …
over a lateral distance on the order of a micrometer"; models a
"2.3 µm-thick pwell mask". Tier: deep dive.

**SHEU-2006** — Y.-M. Sheu, K.-W. Su, S. Tian, S.-J. Yang, C.-C. Wang,
M.-J. Chen and S. Liu, *"Modeling the Well-Edge Proximity Effect in
Highly Scaled MOSFETs"*, IEEE Transactions on Electron Devices,
vol. 53, no. 11, pp. 2792–2798, 2006, DOI 10.1109/TED.2006.884070. A
compact model of the well-edge proximity effect. Tier: deep dive.

**DRENNAN-2006** — P. G. Drennan, M. Kniffin and D. Locascio,
*"Implications of Proximity Effects for Analog Design"*, IEEE Custom
Integrated Circuits Conference 2006, pp. 169–176,
DOI 10.1109/CICC.2006.320869. Designer-side consequences of the well
proximity effect. Tier: deep dive.

**MORRIS-2000** — W. Morris and L. Rubin, *"Technical and economic
considerations for retrograde well and channel implants"*, 2000
International Conference on Ion Implantation Technology, pp. 73–76,
DOI 10.1109/IIT.2000.924093. Why MeV retrograde wells replaced diffused
wells, with the cost trade-offs. Tier: deep dive.

**RUBIN-2002** — L. M. Rubin, W. Morris and C. Jasper, *"Process
control issues for retrograde well implants for narrow n+/p+ isolation
in CMOS"*, 2002 International Conference on Ion Implantation
Technology, pp. 17–20, DOI 10.1109/IIT.2002.1257927. How well-implant
control sets the n⁺/p⁺ isolation spacing. Tier: deep dive.

**BORLAND-1998** — J. O. Borland, H. T. Cho and J. K. Kim, *"LOCOS vs.
shallow trench isolation latch-up using MeV implantation for well
formation down to 0.18 μm design rules"*, 1998 International
Conference on Ion Implantation Technology, vol. 1, pp. 67–70,
DOI 10.1109/IIT.1999.812053. Latch-up with MeV-implanted wells under
LOCOS and STI. Tier: deep dive.

**STOLMEIJER-1986** — A. Stolmeijer, *"A twin-well CMOS process
employing high-energy ion implantation"*, IEEE Transactions on Electron
Devices, vol. 33, no. 4, pp. 450–457, 1986, DOI 10.1109/T-ED.1986.22511.
The original twin-well CMOS process built entirely with high-energy
implants. Tier: deep dive.

**STOLMEIJER-1989** — A. Stolmeijer, M. Pitt, H. den Blanken, P. van
der Plas and R. de Werdt, *"Profile engineering for sub-micron CMOS
using high energy ion implantation"*, International Symposium on VLSI
Technology, Systems and Applications 1989, pp. 317–320,
DOI 10.1109/VTSA.1989.68637. Profile engineering of sub-micron CMOS
wells with chained high-energy implants. Tier: deep dive.

**TSUKAMOTO-1991** — K. Tsukamoto, S. Komori, T. Kuroi and Y. Akasaka,
*"High-energy ion implantation for ULSI"*, Nuclear Instruments and
Methods in Physics Research B, vol. 59–60, pp. 584–591, 1991,
DOI 10.1016/0168-583X(91)95283-J. Review of high-energy implantation
for ULSI: retrograde wells, buried layers, masking and damage
annealing. Tier: deep dive.

**BOURDELLE-2002** — K. K. Bourdelle, S. Chaudhry and J. Chu, *"The
effect of triple well implant dose on performance of NMOS
transistors"*, IEEE Transactions on Electron Devices, vol. 49, no. 3,
pp. 521–524, 2002, DOI 10.1109/16.987125. How a 1 MeV phosphorus
triple-well dose affects NMOS performance and diode leakage. Tier:
deep dive.

**SPINELLI-1985** — P. Spinelli, P. Escaron, A. Soubie and M. Bruel,
*"High energy ion implantation for C-MOS isolation n-wells technology:
Problems related to the use of multicharged phosphorous ions in an
industrial context"*, Nuclear Instruments and Methods in Physics
Research B, vol. 6, no. 1–2, pp. 283–286, 1985,
DOI 10.1016/0168-583X(85)90646-9. Multiply charged phosphorus for MeV
n-well implants in production. Tier: deep dive.

**RO-1999** — J.-S. Ro, *"A study of buried layer formation using MeV
ion implantation for the fabrication of ULSI CMOS devices"*, Thin Solid
Films, vol. 349, no. 1–2, pp. 130–134, 1999,
DOI 10.1016/S0040-6090(99)00079-6. Buried-layer formation by MeV
implantation and the leakage caused by threading dislocations. Tier:
deep dive.

**JANG-1998** — Y.-T. Jang, T.-H. Huh and J.-S. Ro, *"A study on the
defects in the fabrication of CMOS retrograde well including a buried
layer using MeV ion implantation"*, 1998 International Conference on
Ion Implantation Technology, vol. 2, pp. 959–962,
DOI 10.1109/IIT.1998.813837. Defect formation in MeV retrograde wells
with buried layers. Tier: deep dive.

**PAT-BILLI-GENUS** — US 5,821,589 A, *"Method for CMOS latch-up
improvement by MeV BILLI (buried implanted layer for lateral
isolation) plus buried layer implantation"*, J. O. Borland (Genus),
granted 1998-10-13. <https://patents.google.com/patent/US5821589A/en>.
The "BILLI" buried-implanted-layer approach to latch-up suppression
with MeV implants. Tier: deep dive.

**CHAUDHRY-1997** — S. Chaudhry, C. S. Rafferty, W. J. Nagy,
Y. F. Chyan, M. S. Carroll, A. S. Chen and K. H. Lee, *"Suppression of
reverse short channel effect by high energy implantation"*, IEDM 1997
Technical Digest, pp. 679–682, DOI 10.1109/IEDM.1997.650474.
Suppressing the reverse short-channel effect with a high-energy well
implant. Tier: deep dive.

**RAFFERTY-1993** — C. S. Rafferty, H.-H. Vuong, S. A. Eshraghi,
M. D. Giles, M. R. Pinto and S. J. Hillenius, *"Explanation of reverse
short channel effect by defect gradients"*, IEDM 1993 Technical
Digest, pp. 311–314, DOI 10.1109/IEDM.1993.347345. How implant damage
plus the anneal reshapes channel doping. Tier: deep dive.

**MACPHERSON-1971** — M. R. MacPherson, *"The adjustment of MOS
transistor threshold voltage by ion implantation"*, Applied Physics
Letters, vol. 18, no. 11, pp. 502–504, 1971, DOI 10.1063/1.1653513.
The original threshold-adjust-by-implantation paper. Tier: deep dive.

**PERESSINI-1973** — P. P. Peressini and W. S. Johnson, *"Threshold
adjustment of N-channel enhancement mode FETs by ion implantation"*,
1973 International Electron Devices Meeting, pp. 467–468,
DOI 10.1109/IEDM.1973.188761. Early NMOS threshold adjustment by
implantation. Tier: deep dive.

**SHAHIDI-1993** — G. G. Shahidi, B. Davari, T. J. Bucelot,
P. A. Ronsheim, P. J. Coane, S. Pollack, C. R. Blair, B. Clark and
H. H. Hansen, *"Indium channel implant for improved short-channel
behavior of submicrometer NMOSFETs"*, IEEE Electron Device Letters,
vol. 14, no. 8, pp. 409–411, 1993, DOI 10.1109/55.225595. Indium
channel implants for steep retrograde NMOS channels. Tier: deep dive.

**HUANG-2000** — T.-Y. Huang, Y.-J. Lee, T.-S. Chao, C. Chen,
C.-Y. Chang and S.-J. Chang, *"High-performance and high-reliability
80-nm gate-length DTMOS with indium super steep retrograde channel"*,
IEEE Transactions on Electron Devices, vol. 47, no. 12, pp. 2379–2384,
2000, DOI 10.1109/16.887025 (Crossref lists T.-Y. Huang as first
author). An 80 nm DTMOS with an indium super-steep retrograde channel.
Tier: deep dive.

**THOMPSON-1996** — S. E. Thompson, P. A. Packan and M. T. Bohr,
*"Linear versus saturated drive current: tradeoffs in super steep
retrograde well engineering"*, 1996 Symposium on VLSI Technology,
Digest of Technical Papers, pp. 154–155, DOI 10.1109/VLSIT.1996.507830.
Drive-current trade-offs of super-steep retrograde channels. Tier:
deep dive.

**TAUR-1997** — Y. Taur, D. A. Buchanan, W. Chen, D. J. Frank,
K. E. Ismail, S.-H. Lo, G. A. Sai-Halasz, R. G. Viswanathan,
H.-J. C. Wann, S. J. Wind and H.-S. Wong, *"CMOS scaling into the
nanometer regime"*, Proceedings of the IEEE, vol. 85, no. 4,
pp. 486–504, 1997, DOI 10.1109/5.573737. Super-steep retrograde
channels and multiple thresholds at 0.1 µm. Tier: deep dive.

**TAUR-2009** — Y. Taur and T. H. Ning, *Fundamentals of Modern VLSI
Devices*, 2nd ed., Cambridge University Press, 2009,
ISBN 978-0-521-83294-6, DOI 10.1017/CBO9781139195065. Threshold voltage
versus channel doping, retrograde channels, body effect. Tier: deep
dive.

**WEI-1998** — L. Wei, Z. Chen, M. Johnson, K. Roy and V. De, *"Design
and optimization of low voltage high performance dual threshold CMOS
circuits"*, Proceedings of the 35th Design Automation Conference,
pp. 489–494, 1998, DOI 10.1109/DAC.1998.724521. The circuit-level case
for a second threshold voltage. Tier: deep dive.

**WANG-1997** — L. Z. Wang, M. S.-C. Luo, H.-H. Tseng and S. A. Ajuria,
*"The Influence of Fluorine on Boron-Enhanced Diffusion in Silicon by
BF₂⁺ Implantation Through Oxide during High Temperature Rapid Thermal
Anneal"*, Journal of The Electrochemical Society, vol. 144, no. 11,
pp. L298–L301, 1997, DOI 10.1149/1.1838075. Fluorine's effect on boron
diffusion after BF₂ implantation through oxide and RTA. Tier: deep
dive.

**SMITH-1985** — W. L. Smith, A. Rosencwaig and D. L. Willenborg,
*"Ion implant monitoring with thermal wave technology"*, Applied
Physics Letters, vol. 47, no. 6, pp. 584–586, 1985,
DOI 10.1063/1.96079. The thermal-wave (modulated-reflectance) implant
monitor. Tier: deep dive.

**CURRENT-1996** — M. I. Current, *"Ion implantation for silicon device
manufacturing: A vacuum perspective"*, Journal of Vacuum Science &
Technology A, vol. 14, no. 3, pp. 1115–1123, 1996,
DOI 10.1116/1.580279. Production-implanter overview: sources, beam
lines, end stations and vacuum. Tier: deep dive.

**MACK-2007** — C. Mack, *Fundamental Principles of Optical
Lithography: The Science of Microfabrication*, Wiley, 2007,
ISBN 978-0-470-01893-4, DOI 10.1002/9780470723876. k₁, resist profiles,
thick-resist imaging. Tier: deep dive.

**LEVINSON-2005** — H. J. Levinson, *Principles of Lithography*, 2nd
ed., SPIE Press, 2005, ISBN 978-0-8194-5660-1, DOI 10.1117/3.601520.
Overlay budgets and non-critical-layer tool choice. Tier: deep dive.

**ROCHE-1985** — D. Roche, J. F. Michaud and M. Bruel, *"Outgassing of
Photoresist During Ion Implantation"*, MRS Proceedings, vol. 45, 1985,
DOI 10.1557/PROC-45-203. Resist outgassing during implantation. Tier:
deep dive.

**LEE-1996** — W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland,
M. Dennon and C. Kozak, *"Thick photoresist outgassing during MeV
implantation (mechanism and impact on production)"*, Proceedings of
the 11th International Conference on Ion Implantation Technology
(1996), pp. 186–189, DOI 10.1109/IIT.1996.586180. Outgassing of thick
resists during MeV implantation. Tier: deep dive.

**HORSKY-1998** — T. N. Horsky, *"Photoresist outgassing in high energy
and high current ion implantation"*, 1998 International Conference on
Ion Implantation Technology, vol. 1, pp. 654–657,
DOI 10.1109/IIT.1999.812201. Resist outgassing in high-energy and
high-current implanters. Tier: deep dive.

**FUJIMURA-1989** — S. Fujimura, J. Konno, K. Hikazutani and H. Yano,
*"Ashing of Ion-Implanted Resist Layer"*, Japanese Journal of Applied
Physics, vol. 28, no. 10R, p. 2130, 1989, DOI 10.1143/JJAP.28.2130. The
crust and popping mechanism of implanted resist, measured. Tier: deep
dive.

**FUJIMURA-1990** — S. Fujimura, K. Shinagawa, M. Nakamura and
H. Yano, *"Additive Nitrogen Effects on Oxygen Plasma Downstream
Ashing"*, Japanese Journal of Applied Physics, vol. 29, no. 10R,
p. 2165, 1990, DOI 10.1143/JJAP.29.2165. Why nitrogen is added to
oxygen in downstream ashing. Tier: deep dive.

**FUJIMURA-1994** — S. Fujimura, M. T. Suzuki, K. Shinagawa and
M. Nakamura, *"Sodium contamination free ashing process using O₂+H₂O
plasma downstream"*, Journal of Vacuum Science & Technology B, vol. 12,
no. 4, pp. 2409–2413, 1994, DOI 10.1116/1.587773. Water-vapour
addition to downstream ashing. Tier: deep dive.

**OHMI-1996** — T. Ohmi, *"Total Room Temperature Wet Cleaning for Si
Substrate Surface"*, Journal of The Electrochemical Society, vol. 143,
no. 9, pp. 2957–2964, 1996, DOI 10.1149/1.1837133. A room-temperature
alternative to the hot RCA sequence. Tier: deep dive.

**KERN-1990** — W. Kern, *"The Evolution of Silicon Wafer Cleaning
Technology"*, Journal of The Electrochemical Society, vol. 137, no. 6,
pp. 1887–1892, 1990, DOI 10.1149/1.2086825. History and chemistry of
the RCA clean. Tier: deep dive.

**KERN-HANDBOOK** — W. Kern, *"Overview and Evolution of Silicon Wafer
Cleaning Technology"*, ch. 1 in K. A. Reinhardt and W. Kern (eds.),
*Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8,
DOI 10.1016/b978-081551554-8.50004-5. Overview chapter on wet-cleaning
chemistry and contamination. Tier: deep dive.

**REINHARDT-2010** — K. A. Reinhardt and R. F. Reidy (eds.), *Handbook
of Cleaning in Semiconductor Manufacturing: Fundamental and
Applications*, Wiley, 2010, ISBN 978-0-470-62595-8,
DOI 10.1002/9781118071748. Modern treatment of wet and dry cleaning,
including post-implant strip. Tier: deep dive.

**MITROS-2001** — J. C. Mitros, C.-Y. Tsai, H. Shichijo, M. Kunz,
A. Morton, D. Goodpaster, D. Mosher and T. R. Efland, *"High-voltage
drain extended MOS transistors for 0.18-µm logic CMOS process"*, IEEE
Transactions on Electron Devices, vol. 48, no. 8, pp. 1751–1755, 2001,
DOI 10.1109/16.936703. Drain-extended MOS transistors added to a
0.18 µm logic process. Tier: deep dive.

**MAI-2011** — A. Mai and H. Rücker, *"Drain-extended MOS transistors
capable for operation at 10 V and at radio frequencies"*, Solid-State
Electronics, vol. 65–66, pp. 45–50, 2011,
DOI 10.1016/j.sse.2011.06.034. 10 V drain-extended devices in a
0.13 µm technology. Tier: deep dive.

**APPELS-1979** — J. A. Appels and H. M. J. Vaes, *"High voltage thin
layer devices (RESURF devices)"*, 1979 International Electron Devices
Meeting, pp. 238–241, DOI 10.1109/IEDM.1979.189589. The original RESURF
paper. Tier: deep dive.

**LUDIKHUIZE-2000** — A. W. Ludikhuize, *"A review of RESURF
technology"*, 12th International Symposium on Power Semiconductor
Devices & ICs (2000), pp. 11–18, DOI 10.1109/ISPSD.2000.856763. Review
of RESURF design rules for drift regions. Tier: deep dive.

**BALIGA-2008** — B. J. Baliga, *Fundamentals of Power Semiconductor
Devices*, Springer, 2008, ISBN 978-0-387-47313-0,
DOI 10.1007/978-0-387-47314-7. Breakdown, drift-region doping and
on-resistance trade-offs. Tier: deep dive.

**EFLAND-1998** — T. R. Efland, C.-Y. Tsai and S. Pendharkar, *"Lateral
thinking about power devices (LDMOS)"*, IEDM 1998 Technical Digest,
pp. 679–682, DOI 10.1109/IEDM.1998.746447. LDMOS integration into logic
CMOS. Tier: deep dive.

**STOLK-1997** — P. A. Stolk, H.-J. Gossmann, D. J. Eaglesham,
D. C. Jacobson, C. S. Rafferty, G. H. Gilmer, M. Jaraíz, J. M. Poate,
H. S. Luftman and T. E. Haynes, *"Physical mechanisms of transient
enhanced dopant diffusion in ion-implanted silicon"*, Journal of
Applied Physics, vol. 81, no. 9, pp. 6031–6050, 1997,
DOI 10.1063/1.364452. The physical mechanisms of transient enhanced
diffusion. Tier: deep dive.

**MICHEL-1987** — A. E. Michel, W. Rausch, P. A. Ronsheim and
R. H. Kastl, *"Rapid annealing and the anomalous diffusion of ion
implanted boron into silicon"*, Applied Physics Letters, vol. 50,
no. 7, pp. 416–418, 1987, DOI 10.1063/1.98160. First report of
anomalous (transient enhanced) boron diffusion under rapid annealing.
Tier: deep dive.

**EAGLESHAM-1994** — D. J. Eaglesham, P. A. Stolk, H.-J. Gossmann and
J. M. Poate, *"Implantation and transient B diffusion in Si: The
source of the interstitials"*, Applied Physics Letters, vol. 65,
no. 18, pp. 2305–2307, 1994, DOI 10.1063/1.112725. The interstitial
source behind transient boron diffusion. Tier: deep dive.

**ROOZEBOOM-1990** — F. Roozeboom and N. Parekh, *"Rapid thermal
processing systems: A review with emphasis on temperature control"*,
Journal of Vacuum Science & Technology B, vol. 8, no. 6,
pp. 1249–1259, 1990, DOI 10.1116/1.584902. Review of RTP systems with
emphasis on temperature control. Tier: deep dive.

**FIORY-2002** — A. T. Fiory, *"Recent developments in rapid thermal
processing"*, Journal of Electronic Materials, vol. 31, no. 10,
pp. 981–987, 2002, DOI 10.1007/s11664-002-0031-9. RTP developments of
the 130 nm era. Tier: deep dive.


**GIBBONS-1972** — J. F. Gibbons, "Ion implantation in semiconductors —
Part II: Damage production and annealing", *Proceedings of the IEEE*
**60**(9), 1062–1096 (1972). <https://doi.org/10.1109/PROC.1972.8854>
Damage production and annealing of implanted layers. Used on step 034
and the anneal and implant category pages. Tier: deep dive.

### 8.8 Isolation-module deep-dive sources

None of these is a SkyWater or Cypress source; the step pages for the
isolation module (steps 001–013: starting material, pad oxide, nitride,
active-area lithography, trench etch, deep N-well, liner, fill, CMP and
nitride strip) use them for era-typical values, mechanisms and further
reading. They complement §8.5, which holds the first sources gathered
for the same module. Every entry was fetched by the writer or reviewer
of the citing page; a random sample was re-checked through Crossref on
2026-09-12.

#### Papers and review articles

**AMERICA-2004** — W. G. America and S. V. Babu, "Slurry Additive
Effects on the Suppression of Silicon Nitride Removal during CMP",
*Electrochemical and Solid-State Letters* **7**(12), G327 (2004).
<https://doi.org/10.1149/1.1817870> Slurry additives that suppress
silicon nitride removal, i.e. how a self-stopping STI slurry is made.
Used on step 012. Tier: deep dive.

**BASSETT-2016** — D. W. Bassett and A. L. P. Rotondaro, "Silica
Formation during Etching of Silicon Nitride in Phosphoric Acid", *Solid
State Phenomena* **255**, 285–290 (2016).
<https://doi.org/10.4028/www.scientific.net/SSP.255.285> Silica
formation during nitride etching in phosphoric acid, the mechanism
behind bath ageing and selectivity drift. Used on step 013. Tier: deep
dive.

**BERGMAN-2009** — E. J. Bergman and J. D. Leonhard, "Novel Methods for
Wet Stripping High Dose Implanted Photoresist Using Sulfur Trioxide",
*Solid State Phenomena* **145–146**, 281–284 (2009).
<https://doi.org/10.4028/www.scientific.net/SSP.145-146.281> Wet
stripping of high-dose implanted resist with sulphur trioxide, a
sulphuric-family alternative to SPM. Used on step 009. Tier: deep dive.

**BESTWICK-1990** — T. D. Bestwick and G. S. Oehrlein, "Reactive ion
etching of silicon using bromine containing plasmas", *Journal of Vacuum
Science & Technology A* **8**(3), 1696–1701 (1990).
<https://doi.org/10.1116/1.576832> Reactive-ion etching of silicon in
bromine-containing plasmas, the chemistry of the main etch. Used on step
006. Tier: deep dive.

**BIANCHI-2002** — R. A. Bianchi, G. Bouche and O. Roux-dit-Buisson,
"Accurate modeling of trench isolation induced mechanical stress effects
on MOSFET electrical performance", *IEDM 2002 Technical Digest*, pp.
117–120. <https://doi.org/10.1109/IEDM.2002.1175792> Modelling of
trench-isolation-induced mechanical stress on MOSFET performance. Used
on steps 006 and 011. Tier: deep dive.

**BORGHESI-1995** — A. Borghesi, B. Pivac, A. Sassella and A. Stella,
"Oxygen precipitation in silicon", *Journal of Applied Physics*
**77**(9), 4169–4244 (1995). <https://doi.org/10.1063/1.359479> A review
of oxygen precipitation in CZ silicon, the basis of internal gettering
and a driver of wafer warpage through the thermal budget. Used on step
001 and the substrate category page. Tier: deep dive.

**BRYANT-1994** — A. Bryant, W. Hänsch and T. Mii, "Characteristics of
CMOS device isolation for the ULSI age", *Proc. 1994 IEEE International
Electron Devices Meeting*, pp. 671–674.
<https://doi.org/10.1109/IEDM.1994.383292> The device-level case for STI
over LOCOS and what trench isolation must deliver. Used on steps 006,
010 and 013. Tier: deep dive.

**BU-2005** — K.-H. Bu and B. M. Moudgil, "Colloidal Silica based High
Selectivity Shallow Trench Isolation (STI) Chemical Mechanical Polishing
(CMP) Slurry", *MRS Proceedings* **867**, W8.5 (2005).
<https://doi.org/10.1557/PROC-867-W8.5> A colloidal-silica route to a
high-selectivity STI slurry, the alternative to ceria. Used on step 012.
Tier: deep dive.

**CHANG-2005** — S.-H. Chang, "A dishing model for STI CMP process",
*Microelectronic Engineering* **82**(2), 136–142 (2005).
<https://doi.org/10.1016/j.mee.2005.07.002> A dishing model specific to
the STI CMP process. Used on step 012. Tier: deep dive.

**CHATTERJEE-1996** — A. Chatterjee, J. Esquivel, S. Nag, I. Ali, D.
Rogers, K. Taylor, K. Joyner, M. Mason, D. Mercer, A. Amerasekera, T.
Houston and I.-C. Chen, "A shallow trench isolation study for 0.25/0.18
µm CMOS technologies and beyond", *1996 Symposium on VLSI Technology,
Digest of Technical Papers*, pp. 156–157.
<https://doi.org/10.1109/VLSIT.1996.507831> An STI integration study for
0.25/0.18 µm CMOS covering the pad-oxide/nitride stack and trench corner
choices. Used on steps 002 and 006. Tier: deep dive.

**COBURN-1979** — J. W. Coburn and H. F. Winters, "Ion- and
electron-assisted gas-surface chemistry — An important effect in plasma
etching", *Journal of Applied Physics* **50**(5), 3189–3196 (1979).
<https://doi.org/10.1063/1.326355> The classic demonstration that ion
bombardment plus reactive gas etches far faster than either alone, the
basis of anisotropic RIE. Used on steps 005, 036 and 042 and the etch
category page. Tier: deep dive.

**COOK-1990** — L. M. Cook, "Chemical processes in glass polishing",
*Journal of Non-Crystalline Solids* **120**(1–3), 152–171 (1990).
<https://doi.org/10.1016/0022-3093(90)90200-6> The chemical mechanism of
glass (oxide) polishing that oxide CMP inherits. Used on step 012 and
the cmp category page. Tier: deep dive.

**DEAL-1965** — B. E. Deal and A. S. Grove, "General Relationship for
the Thermal Oxidation of Silicon", *Journal of Applied Physics*
**36**(12), 3770–3778 (1965). <https://doi.org/10.1063/1.1713945> The
planar oxidation model that the corner results are measured against.
Used on steps 002, 010, 040, 042, 043 and 047 and the oxidation category
page. Tier: deep dive.

**DEAL-1980** — B. E. Deal, "Standardized terminology for oxide charges
associated with thermally oxidized silicon", *IEEE Transactions on
Electron Devices* **27**(3), 606–608 (1980), DOI
10.1109/T-ED.1980.19908; published simultaneously in *Journal of The
Electrochemical Society* **127**(4), 979–981 (1980).
<https://doi.org/10.1109/T-ED.1980.19908>,
<https://doi.org/10.1149/1.2129800> The standard terminology for oxide
charges (fixed, trapped, mobile, interface) used when qualifying any
thermal oxide. Used on steps 002, 043 and 047 and the anneal and
oxidation category pages. Tier: deep dive.

**DECKERT-1978** — C. A. Deckert, "Etching of CVD Si₃N₄ in Acidic
Fluoride Media", *Journal of The Electrochemical Society* **125**(2),
320–323 (1978). <https://doi.org/10.1149/1.2131436> Etching of CVD Si₃N₄
in acidic fluoride media, the older data on the same chemistry. Used on
step 013. Tier: deep dive.

**EDMARK-1985** — K. W. Edmark and C. P. Ausschnitt, "Stepper Overlay
Calibration Using Alignment To A Latent Image", *Proc. SPIE* **0538**,
Optical Microlithography IV, 91 (1985).
<https://doi.org/10.1117/12.947752> Stepper overlay calibration by
aligning to a latent image, an early treatment of stepper
self-calibration relevant to an unaligned first layer. Used on step 004.
Tier: deep dive.

**FALSTER-2000** — R. Falster and V. V. Voronkov, "The engineering of
intrinsic point defects in silicon wafers and crystals", *Materials
Science and Engineering: B* **73**(1–3), 87–94 (2000).
<https://doi.org/10.1016/S0921-5107(99)00439-0> Engineering of intrinsic
point defects in crystals and wafers, the basis of "perfect silicon" and
controlled precipitation. Used on step 001 and the substrate category
page. Tier: deep dive.

**FAZAN-1993** — P. C. Fazan and V. K. Mathews, "A highly manufacturable
trench isolation process for deep submicron DRAMs", *Proc. IEEE
International Electron Devices Meeting 1993*, pp. 57–60.
<https://doi.org/10.1109/IEDM.1993.347399> An early manufacturable
trench isolation process, showing the etch, fill and polish sequence.
Used on step 006. Tier: deep dive.

**FLAMM-1990** — D. L. Flamm, "Mechanisms of silicon etching in
fluorine- and chlorine-containing plasmas", *Pure and Applied Chemistry*
**62**(9), 1709–1720 (1990). <https://doi.org/10.1351/pac199062091709>
Mechanisms of silicon etching in fluorine- and chlorine-containing
plasmas, relevant to the pad-oxide breakthrough and the silicon stop.
Used on step 005. Tier: deep dive.

**FUJIMURA-1991** — S. Fujimura, K. Shinagawa, M. T. Suzuki and M.
Nakamura, "Resist stripping in an O₂+H₂O plasma downstream", *Journal of
Vacuum Science & Technology B* **9**(2), 357–361 (1991).
<https://doi.org/10.1116/1.585575> Resist stripping in an O₂ + H₂O
downstream plasma, a low-damage alternative. Used on step 009. Tier:
deep dive.

**HABRAKEN-1994** — F. H. P. M. Habraken and A. E. T. Kuiper, "Silicon
nitride and oxynitride films", *Materials Science and Engineering: R:
Reports* **12**(3), 123–175 (1994).
<https://doi.org/10.1016/0927-796X(94)90006-X> A review of silicon
nitride and oxynitride films: growth, composition, hydrogen content and
etch behaviour. Used on step 003. Tier: deep dive.

**HOSHINO-2001** — T. Hoshino, Y. Kurata, Y. Terasaki and K. Susa,
"Mechanism of polishing of SiO₂ films by CeO₂ particles", *Journal of
Non-Crystalline Solids* **283**(1–3), 129–136 (2001).
<https://doi.org/10.1016/S0022-3093(01)00364-7> The mechanism by which
ceria particles polish SiO₂. Used on step 012. Tier: deep dive.

**HU-1991** — S. M. Hu, "Stress-related problems in silicon technology",
*Journal of Applied Physics* **70**(6), R53–R80 (1991).
<https://doi.org/10.1063/1.349282> A review of stress-related problems
in silicon technology, including nitride-on-pad-oxide stress and
dislocation generation. Used on steps 002, 003 and 010. Tier: deep dive.

**IRENE-1988** — E. A. Irene, "Models for the oxidation of silicon",
*Critical Reviews in Solid State and Materials Sciences* **14**(2),
175–223 (1988). <https://doi.org/10.1080/10408438808242183> A review of
oxidation models beyond Deal–Grove, including the thin-film and stress
effects. Used on step 002. Tier: deep dive.

**ITO-2005** — H. Ito, "Chemical Amplification Resists for
Microlithography", *Advances in Polymer Science* **172**, 37–245 (2005).
<https://doi.org/10.1007/b97574> A 200-page review of chemically
amplified resists, including KrF poly(hydroxystyrene) systems. Used on
step 004 and the lithography category page. Tier: deep dive.

**KAHNG-2008** — A. B. Kahng and K. Samadi, "CMP Fill Synthesis: A
Survey of Recent Studies", *IEEE Transactions on Computer-Aided Design
of Integrated Circuits and Systems* **27**(1), 3–19 (2008).
<https://doi.org/10.1109/TCAD.2007.907061> A survey of dummy-fill
synthesis for CMP, the design-side view of the FOM "waffles". Used on
step 004. Tier: deep dive.

**KANG-1989** — J. S. Kang and D. K. Schroder, "Gettering in silicon",
*Journal of Applied Physics* **65**(8), 2974–2985 (1989).
<https://doi.org/10.1063/1.342714> A review of gettering mechanisms
(intrinsic and extrinsic) that a bulk-wafer process relies on to keep
metals away from junctions. Used on step 001 and the substrate category
page. Tier: deep dive.

**KASTENMEIER-1999** — B. E. E. Kastenmeier, P. J. Matsuo and G. S.
Oehrlein, "Highly selective etching of silicon nitride over silicon and
silicon dioxide", *Journal of Vacuum Science & Technology A* **17**(6),
3179–3184 (1999). <https://doi.org/10.1116/1.582097> How to etch silicon
nitride selectively over silicon and silicon dioxide in fluorine-based
plasmas. Used on step 005. Tier: deep dive.

**KNOTTER-2001** — D. M. Knotter and T. J. J. Denteneer, "Etching
Mechanism of Silicon Nitride in HF-Based Solutions", *Journal of The
Electrochemical Society* **148**(3), F43 (2001).
<https://doi.org/10.1149/1.1348262> The etching mechanism of silicon
nitride in HF-based solutions, relevant to the pre-strip breakthrough
dip. Used on step 013. Tier: deep dive.

**KOOI-1976** — E. Kooi, J. G. van Lierop and J. A. Appels, "Formation
of Silicon Nitride at a Si–SiO₂ Interface during Local Oxidation of
Silicon and during Heat-Treatment of Oxidized Silicon in NH₃ Gas",
*Journal of The Electrochemical Society* **123**(7), 1117–1120 (1976).
<https://doi.org/10.1149/1.2133008> The "Kooi effect": nitride formed at
the Si/SiO₂ interface at the edge of a nitride mask, the reason
pad-oxide thickness and post-strip treatment matter. Used on steps 002,
003, 010 and 013 and the oxidation category page. Tier: deep dive.

**LEE-1997** — S. Lee, K. Jung, J. Son, S. Chung, M. Chae, J. Kim, W.
Yang, Y. Lee and J. Hwang, "Shallow Trench Isolation Characteristics
with High-Density-Plasma (HDP) CVD Gap-Fill Oxide for Deep-Submicron
CMOS Technologies", *Extended Abstracts of the 1997 International
Conference on Solid State Devices and Materials*, C-13-4 (1997).
<https://doi.org/10.7567/SSDM.1997.C-13-4> STI characteristics with an
HDP-CVD gap-fill oxide for deep-submicron CMOS, including device
results. Used on step 011. Tier: deep dive.

**LIN-1998** — S. C. Lin, J. B. Kuo, K. T. Huang and S. W. Sun,
"Analytical subthreshold current hump model for deep-submicron
shallow-trench-isolated CMOS devices", *Solid-State Electronics*
**42**(10), 1871–1879 (1998).
<https://doi.org/10.1016/S0038-1101(98)00161-0> An analytical model of
the sub-threshold current hump caused by the STI top corner. Used on
step 006. Tier: deep dive.

**LINDEMANN-2007** — H. M. Lindemann, J. Radecker and H.-P. Sperlich,
"Selective Oxide (SelOx) Deposition as Unique Gap-Fill Solution for
Shallow Trench Isolation", *2007 IEEE/SEMI Advanced Semiconductor
Manufacturing Conference (ASMC)*, pp. 253–258.
<https://doi.org/10.1109/ASMC.2007.375111> Selective oxide deposition as
an alternative STI gap-fill, showing where HDP's limits lie. Used on
step 011. Tier: deep dive.

**LIU-2007** — L. Liu, I. Kashkoush, G. Chen and C. Murphy, "Maintaining
a Stable Etch Selectivity between Silicon Nitride and Silicon Dioxide in
a Hot Phosphoric Acid Bath", *ECS Transactions* **11**(2), 63–70 (2007).
<https://doi.org/10.1149/1.2779363> How to keep the nitride : oxide
selectivity stable in a production hot phosphoric bath, from Akrion, the
wet-bench vendor SKW-01 names. Used on step 013. Tier: deep dive.

**LIU-2020** — P. Liu, M. Garcia-Sciveres, T. Heim, A. Krieger and D.
Gnani, "Measured Effectiveness of Deep N-well Substrate Isolation in a
65nm Pixel Readout Chip Prototype", *Nuclear Instruments and Methods in
Physics Research A* (2020); preprint arXiv:1908.06182.
<https://arxiv.org/abs/1908.06182> Quantitative deep N-well isolation
measurements in a 65 nm pixel readout chip, showing which side of the
isolation to put the sensitive circuits. Used on step 008. Tier: deep
dive.

**MANIVANNAN-2010** — R. Manivannan, S. Noyel Victoria and S.
Ramanathan, "Mechanism of high selectivity in ceria based shallow trench
isolation chemical mechanical polishing slurries", *Thin Solid Films*
**518**(20), 5737–5740 (2010).
<https://doi.org/10.1016/j.tsf.2010.05.072> The mechanism of high
oxide-to-nitride selectivity in ceria STI slurries. Used on step 012.
Tier: deep dive.

**MARCUS-1982** — R. B. Marcus and T. T. Sheng, "The Oxidation of Shaped
Silicon Surfaces", *Journal of The Electrochemical Society* **129**(6),
1278–1282 (1982). <https://doi.org/10.1149/1.2124118> The first
systematic study of oxidising shaped (trenched and stepped) silicon
surfaces. Used on step 010. Tier: deep dive.

**MASSOUD-1985** — H. Z. Massoud, J. D. Plummer and E. A. Irene,
"Thermal Oxidation of Silicon in Dry Oxygen: Growth-Rate Enhancement in
the Thin Regime. I. Experimental Results", *Journal of The
Electrochemical Society* **132**(11), 2685–2693 (1985).
<https://doi.org/10.1149/1.2113648> The growth-rate enhancement in the
thin (< 30 nm) dry-oxide regime that a 10–20 nm pad oxide sits in. Used
on steps 002, 040, 043 and 047 and the oxidation category page. Tier:
deep dive.

**MATSUDA-1998** — S. Matsuda, T. Sato, H. Yoshimura, Y. Takegawa, A.
Sudo, I. Mizushima, Y. Tsunashima and Y. Toyoshima, "Novel corner
rounding process for shallow trench isolation utilizing MSTS
(Micro-Structure Transformation of Silicon)", *IEDM 1998 Technical
Digest*, pp. 137–140. <https://doi.org/10.1109/IEDM.1998.746298> A
corner-rounding process based on silicon micro-structure transformation
after the trench etch. Used on steps 006 and 010. Tier: deep dive.

**NANDAKUMAR-1997** — M. Nandakumar, S. Sridhar, S. Nag, P. Mei, D.
Rogers, M. Hanratty, A. Amerasekera and I.-C. Chen, "A shallow trench
isolation for sub-0.13 µm CMOS technologies", *IEDM 1997 Technical
Digest*, pp. 657–660. <https://doi.org/10.1109/IEDM.1997.650469> STI for
sub-0.13 µm CMOS, including the liner and corner engineering. Used on
steps 006 and 010. Tier: deep dive.

**NGUYEN-1999** — S. V. Nguyen, "High-density plasma chemical vapor
deposition of silicon-based dielectric films for integrated circuits",
*IBM Journal of Research and Development* **43**(1.2), 109–126 (1999).
<https://doi.org/10.1147/rd.431.0109> A review of HDP-CVD of
silicon-based dielectrics: reactor design, film properties and gap-fill
mechanisms. Used on step 011 and the deposition category page. Tier:
deep dive.

**OCONNOR-1996** — J. P. O'Connor and N. Tokoro, "End station and beam
line design considerations for photoresist outgassing with high energy
(MeV) ion implantation", *Proc. 11th International Conference on Ion
Implantation Technology (1996)*, pp. 350–354.
<https://doi.org/10.1109/IIT.1996.586285> End-station and beam-line
design to cope with resist outgassing at MeV energies. Used on step 007.
Tier: deep dive.

**OEHRLEIN-1994** — G. S. Oehrlein, Y. Zhang, D. Vender and M. Haverlag,
"Fluorocarbon high-density plasmas. I. Fluorocarbon film deposition and
etching using CF₄ and CHF₃", *Journal of Vacuum Science & Technology A*
**12**(2), 323–332 (1994). <https://doi.org/10.1116/1.578876>
Fluorocarbon high-density plasmas with CF₄ and CHF₃: polymer deposition
versus etching, the mechanism behind sidewall passivation. Used on step
005 and the etch category page. Tier: deep dive.

**OHASHI-2007** — T. Ohashi, T. Kubota and A. Nakajima, "Ar Annealing
for Suppression of Gate Oxide Thinning at Shallow Trench Isolation
Edge", *IEEE Electron Device Letters* **28**(7), 562–564 (2007).
<https://doi.org/10.1109/LED.2007.899328> An argon anneal that
suppresses gate-oxide thinning at the STI edge, a later view of the same
problem. Used on step 010. Tier: deep dive.

**ORVEK-1985** — K. J. Orvek and C. Huffman, "Carbonized layer formation
in ion implanted photoresist masks", *Nuclear Instruments and Methods in
Physics Research B* **7–8**, 501–506 (1985).
<https://doi.org/10.1016/0168-583X(85)90421-5> The carbonised layer that
forms on ion-implanted photoresist, the reason implant strips are hard.
Used on step 009. Tier: deep dive.

**OTTO-1994** — O. W. Otto, J. G. Garofalo, K. K. Low, C.-M. Yuan, R. C.
Henderson, C. Pierrat, R. L. Kostelak, S. Vaidya and P. K. Vasudev,
"Automated optical proximity correction: a rules-based approach", *Proc.
SPIE* **2197**, Optical/Laser Microlithography VII, 278–293 (1994).
<https://doi.org/10.1117/12.175422> An early rules-based optical
proximity correction method of the kind applied to active-layer
reticles. Used on step 004 and the lithography category page. Tier: deep
dive.

**PEEV-1990** — G. Peev, L. Zambov and Y. Yanakiev, "Kinetics of the
chemical reaction between dichlorosilane and ammonia during silicon
nitride film deposition", *Thin Solid Films* **189**(2), 275–282 (1990).
<https://doi.org/10.1016/0040-6090(90)90456-N> The kinetics of the
DCS–NH₃ reaction and how the deposition rate depends on gas ratio,
pressure and temperature. Used on step 003. Tier: deep dive.

**REGIS-1997** — J. M. Regis, A. M. Joshi, T. Lill and M. Yu, "Reactive
ion etch of silicon nitride spacer with high selectivity to oxide",
*1997 IEEE/SEMI Advanced Semiconductor Manufacturing Conference and
Workshop (ASMC 97) Proceedings*, pp. 252–256.
<https://doi.org/10.1109/ASMC.1997.630744> A production RIE recipe for
silicon nitride with high selectivity to oxide, with the process-window
data. Used on steps 005 and 042. Tier: deep dive.

**ROENIGK-1987** — K. F. Roenigk and K. F. Jensen, "Low Pressure CVD of
Silicon Nitride", *Journal of The Electrochemical Society* **134**(7),
1777–1785 (1987). <https://doi.org/10.1149/1.2100756> A reactor model of
LPCVD nitride from DCS/NH₃, explaining thickness uniformity along a
hot-wall tube. Used on step 003. Tier: deep dive.

**RYUTA-1990** — J. Ryuta, E. Morita, T. Tanaka and Y. Shimanuki,
"Crystal-Originated Singularities on Si Wafer Surface after SC1
Cleaning", *Japanese Journal of Applied Physics* **29**(11A), L1947
(1990). <https://doi.org/10.1143/JJAP.29.L1947> The paper that
identified "crystal-originated singularities" (COPs) revealed by SC-1
cleaning, the defect class that gate-oxide yield depends on. Used on
step 001 and the substrate category page. Tier: deep dive.

**STAFFA-1995** — J. Staffa, D. Hwang, B. Luther, J. Ruzyllo and R.
Grant, "Temperature dependence of the etch rate and selectivity of
silicon nitride over silicon dioxide in remote plasma NF₃/Cl₂", *Applied
Physics Letters* **67**(13), 1902–1904 (1995).
<https://doi.org/10.1063/1.114371> Nitride-over-oxide selectivity of a
remote NF₃/Cl₂ plasma, a dry alternative to the hot phosphoric strip.
Used on step 013. Tier: deep dive.

**STINE-1998** — B. E. Stine, D. O. Ouma, R. R. Divecha, D. S. Boning,
J. E. Chung, D. L. Hetherington, C. R. Harwood, O. S. Nakagawa and S.-Y.
Oh, "Rapid characterization and modeling of pattern-dependent variation
in chemical-mechanical polishing", *IEEE Transactions on Semiconductor
Manufacturing* **11**(1), 129–140 (1998).
<https://doi.org/10.1109/66.661292> Rapid characterisation and modelling
of pattern-dependent CMP variation, the basis of density-based fill
rules. Used on step 012 and the cmp category page. Tier: deep dive.

**STONEY-1909** — G. G. Stoney, "The tension of metallic films deposited
by electrolysis", *Proceedings of the Royal Society of London A*
**82**(553), 172–175 (1909). <https://doi.org/10.1098/rspa.1909.0021>
The wafer-curvature relation used to turn a bow measurement into a film
stress. Used on step 003. Tier: deep dive.

**TEASDALE-2001** — D. Teasdale, Y. Senzaki, R. Herring, G. Hoeye, L.
Page and P. Schubert, "LPCVD of Silicon Nitride from Dichlorosilane and
Ammonia by Single Wafer Rapid Thermal Processing", *Electrochemical and
Solid-State Letters* **4**(5), F11 (2001).
<https://doi.org/10.1149/1.1359056> Single-wafer RTCVD of DCS/NH₃
nitride, the alternative to a batch furnace. Used on step 003. Tier:
deep dive.

**TEMPLE-BOYER-1998** — P. Temple-Boyer, C. Rossi, E. Saint-Etienne and
E. Scheid, "Residual stress in low pressure chemical vapor deposition
SiNₓ films deposited from silane and ammonia", *Journal of Vacuum
Science & Technology A* **16**(4), 2003–2007 (1998).
<https://doi.org/10.1116/1.581302> Residual stress in LPCVD SiNₓ as a
function of composition, the reason stoichiometric films are highly
tensile. Used on step 003. Tier: deep dive.

**VAN-HAREN-2019** — R. J. F. van Haren, S. Steinert, O. Mouraille, K.
D'havé, L. van Dijk, J. Hermans and D. Beyer, "Wafer alignment mark
placement accuracy impact on the layer-to-layer overlay performance",
*Proc. SPIE* **11148**, Photomask Technology 2019, 37 (2019).
<https://doi.org/10.1117/12.2536270> How alignment-mark placement
accuracy limits layer-to-layer overlay. Used on steps 004 and 041. Tier:
deep dive.

**VASSILIEV-1999** — V. Y. Vassiliev, "Properties and Gap-Fill
Capability of HPD-CVD Phosphosilicate Glass Films for
Subquarter-Micrometer ULSI Device Technology", *Electrochemical and
Solid-State Letters* **3**(2), 80 (1999).
<https://doi.org/10.1149/1.1390964> Properties and gap-fill capability
of HDP-CVD phosphosilicate glass, the doped variant SkyWater also lists.
Used on step 011. Tier: deep dive.

**VISINTIN-2006** — P. M. Visintin, M. B. Korzenski and T. H. Baum,
"Liquid Clean Formulations for Stripping High-Dose Ion-Implanted
Photoresist from Microelectronic Devices", *Journal of The
Electrochemical Society* **153**(7), G591 (2006).
<https://doi.org/10.1149/1.2195884> Liquid formulations for stripping
high-dose implanted resist when ashing alone is insufficient. Used on
step 009. Tier: deep dive.

**WATANABE-1996** — H. Watanabe, K. Shimizu, Y. Takeuchi and S. Aritome,
"Corner-rounded shallow trench isolation technology to reduce the
stress-induced tunnel oxide leakage current for highly reliable flash
memories", *IEDM 1996 Technical Digest*, pp. 833–836.
<https://doi.org/10.1109/IEDM.1996.554109> Corner-rounded STI to cut
stress-induced tunnel-oxide leakage in flash memory. Used on steps 006
and 010. Tier: deep dive.

**YU-1992** — C. Yu, P. C. Fazan, V. K. Mathews and T. T. Doan, "Dishing
effects in a chemical mechanical polishing planarization process for
advanced trench isolation", *Applied Physics Letters* **61**(11),
1344–1346 (1992). <https://doi.org/10.1063/1.107586> Dishing effects in
CMP planarisation for trench isolation, measured early. Used on step
012. Tier: deep dive.

**ZIEGLER-2010** — J. F. Ziegler, M. D. Ziegler and J. P. Biersack,
"SRIM – The stopping and range of ions in matter (2010)", *Nuclear
Instruments and Methods in Physics Research B* **268**(11–12), 1818–1823
(2010). <https://doi.org/10.1016/j.nimb.2010.02.091> SRIM, the tool used
to compute the ion range in resist that sets the mask thickness. Used on
step 007 and the implant category page. Tier: deep dive.

**ZULEHNER-1983** — W. Zulehner, "Czochralski growth of silicon",
*Journal of Crystal Growth* **65**(1–3), 189–213 (1983).
<https://doi.org/10.1016/0022-0248(83)90051-9> A wafer-maker's review of
Czochralski silicon growth: pulling, oxygen and carbon incorporation,
dopant segregation. Used on step 001 and the substrate category page.
Tier: deep dive.

#### Books and book chapters

**BAWOLEK-1987** — E. J. Bawolek, "Monte Carlo Simulation of Plasma Etch
Emission Endpoint", in *Emerging Semiconductor Technology*, ASTM STP
960, ASTM International, 1987, pp. 190–203.
<https://doi.org/10.1520/STP25751S> A Monte Carlo treatment of
plasma-etch optical-emission endpoint behaviour. Used on step 005. Tier:
deep dive.

**LIEBERMAN-2005** — M. A. Lieberman and A. J. Lichtenberg, *Principles
of Plasma Discharges and Materials Processing*, 2nd ed., Wiley, 2005,
ISBN 978-0-471-72001-0. <https://doi.org/10.1002/0471724254> Ch. 16 on
plasma-enhanced deposition and ion-bombardment control of film stress.
Used on step 005 and the deposition and etch category pages. Tier: deep
dive.

**NICOLLIAN-1982** — E. H. Nicollian and J. R. Brews, *MOS (Metal Oxide
Semiconductor) Physics and Technology*, Wiley, 1982, ISBN
978-0-471-08500-3. <https://openlibrary.org/isbn/9780471085003> The
reference on oxide charges and C–V characterisation of the Si/SiO₂
interface. Used on step 002 and the oxidation category page. Tier: deep
dive.

**OLIVER-2004** — M. R. Oliver (ed.), *Chemical-Mechanical Planarization
of Semiconductor Materials*, Springer Series in Materials Science 69,
Springer, 2004, ISBN 978-3-540-43181-9.
<https://doi.org/10.1007/978-3-662-06234-0> Chapter-level treatments of
dielectric CMP, endpoint and post-CMP cleaning. Used on step 012 and the
cmp category page. Tier: deep dive.

**REINHARDT-2008** — K. A. Reinhardt and W. Kern (eds.), *Handbook of
Silicon Wafer Cleaning Technology*, 2nd ed., William Andrew, 2008, ISBN
978-0-8155-1554-8. <https://openlibrary.org/isbn/9780815515548> The
reference volume on wet and dry cleaning, resist removal and particle
control. Label ↔ key: the handbook whose first chapter is listed
separately as KERN-HANDBOOK. Used on steps 009 and 013. Tier: deep dive.

**SESHAN-2012** — K. Seshan (ed.), *Handbook of Thin Film Deposition*,
3rd ed., William Andrew, 2012, ISBN 978-1-4377-7873-1.
<https://openlibrary.org/isbn/9781437778731> The chapter-level reference
on CVD and HDP-CVD dielectric equipment and films. Used on step 011.
Tier: deep dive.

**SHIMURA-1989** — F. Shimura, *Semiconductor Silicon Crystal
Technology*, Academic Press, 1989, ISBN 978-0-12-640045-8.
<https://openlibrary.org/isbn/9780126400458> The standard monograph on
CZ growth, dopant and oxygen incorporation, and wafer characterisation.
Used on step 001 and the substrate category page. Tier: deep dive.

**SMITH-1983** — T. C. Smith, "Wafer Cooling and Photoresist Masking
Problems in Ion Implantation", in *Ion Implantation: Equipment and
Techniques*, Springer Series in Electrophysics, Springer, 1983, pp.
196–213. <https://doi.org/10.1007/978-3-642-69156-0_25> Wafer cooling
and photoresist masking problems (flow, crust, popping) in implantation.
Used on steps 007 and 009. Tier: deep dive.

**STEIGERWALD-1997** — J. M. Steigerwald, S. P. Murarka and R. J.
Gutmann, *Chemical Mechanical Planarization of Microelectronic
Materials*, Wiley, 1997, ISBN 978-0-471-13827-6.
<https://doi.org/10.1002/9783527617746> The standard CMP textbook:
Preston's law, pads, slurries and process control. Used on step 012 and
the cmp category page. Tier: deep dive.

**SUN-2017** — T. Sun, Z. Han and M. Keswani, "Brush Scrubbing for
Post-CMP Cleaning", in *Developments in Surface Contamination and
Cleaning, Volume 9*, Elsevier, 2017, pp. 109–133.
<https://doi.org/10.1016/B978-0-323-43157-6.00004-5> Brush scrubbing for
post-CMP cleaning. Used on step 012. Tier: deep dive.

**TROUTMAN-1986** — R. R. Troutman, *Latchup in CMOS Technology: The
Problem and Its Cure*, Kluwer Academic Publishers, 1986, ISBN
978-0-89838-215-7. <https://doi.org/10.1007/978-1-4757-1887-4> The
monograph on why substrate resistance matters and how epitaxial
substrates, guard rings and wells suppress latch-up. Used on step 001
and the substrate category page. Tier: deep dive.

#### Theses

**HON-2003** — B. M. Hon, *Characterization of shallow trench isolation
etch line edge roughness*, master's thesis, San José State University,
2003. <https://doi.org/10.31979/etd.53yx-bwm5> Characterisation of
line-edge roughness in an STI etch, a metrology view of the
nitride/trench profile. Used on steps 005 and 006. Tier: deep dive.

#### Patents

**PAT-CMP-MIRRA** — R. D. Tolles, N. Shendon, S. Somekh, I. Perlov, E.
Gantvarg and H. Q. Lee (Applied Materials), *Continuous processing
system for chemical mechanical polishing*, US 5,738,574 A, granted
1998-04-14. <https://patents.google.com/patent/US5738574A/en> The
multi-platen "continuous processing" CMP architecture of the Mirra
family. Used on step 012. Tier: deep dive.

**PAT-CMP-WINDOW** — M. Birang, A. Gleason and W. L. Guthrie (Applied
Materials), *Forming a transparent window in a polishing pad for a
chemical mechanical polishing apparatus*, US 5,893,796 A, granted
1999-04-13. <https://patents.google.com/patent/US5893796A/en> A
transparent window in the pad for in-situ optical endpoint detection.
Used on step 012. Tier: deep dive.

**PAT-CORNER-TOSHIBA** — K. Horioka, H. Okano and H. Nishino (Toshiba
Corporation), *Method of manufacturing semiconductor devices including
rounding of corner portions by etching*, US 5,258,332 A, granted
1993-11-02. <https://patents.google.com/patent/US5258332A/en> Rounding
of trench corner portions by fluorine/oxygen chemical dry etching,
framed around trench capacitors rather than STI. Used on step 006. Tier:
deep dive.

**PAT-HDP-AMAT** — Z. Tan, D. Li and W. Zygmunt (Applied Materials),
*HDP-CVD deposition process for filling high aspect ratio gaps*, US
6,914,016 B2, granted 2005-07-05.
<https://patents.google.com/patent/US6914016B2/en> A multi-step HDP-CVD
deposition/etch process for high-aspect-ratio gaps, the Applied
Materials counterpart to the Novellus approach. Used on step 011. Tier:
deep dive.

**PAT-HDP-NOVELLUS** — G. D. Papasouliotis, A. B. Chakravarti, R. A.
Conti, L. Economikos and P. A. Van Cleemput (Novellus Systems /
International Business Machines), *High throughput chemical vapor
deposition process capable of filling high aspect ratio structures*, US
6,030,881 A, granted 2000-02-29.
<https://patents.google.com/patent/US6030881A/en> A high-throughput
HDP-CVD process for filling high-aspect-ratio structures. Used on step
011. Tier: deep dive.

**PAT-HOTPHOS-TSMC** — C.-C. Huang and S. M. Chen (Taiwan Semiconductor
Manufacturing Co.), *Automated method for monitoring and controlling the
orthophosphoric acid etch rate of silicon nitride insulator layers*, US
5,830,375 A, granted 1998-11-03.
<https://patents.google.com/patent/US5830375A/en> An automated method
for monitoring and controlling the phosphoric-acid etch rate of silicon
nitride, a production-control view. Used on step 013. Tier: deep dive.

**PAT-TCP-LAM** — J. S. Ogle (Lam Research Corporation), *Method and
apparatus for producing magnetically-coupled planar plasma*, US
4,948,458 A, granted 1990-08-14.
<https://patents.google.com/patent/US4948458A/en> The
transformer-coupled planar plasma source behind the Lam TCP 9400 family.
Used on step 005 and the etch category page. Tier: deep dive.

**PAT-WORLEY-2000** — E. R. Worley, *Method of reducing substrate noise
coupling in mixed signal integrated circuits*, US 6,020,614 A, granted
2000-02-01. <https://patents.google.com/patent/US6020614A/en> Reducing
substrate-noise coupling in mixed-signal ICs by tailoring deep implants
between regions. Used on step 008. Tier: deep dive.

#### Standards and roadmaps

**SEMI-M1** — SEMI, *SEMI M1 — Specification for Polished Single Crystal
Silicon Wafers*, SEMI Standards store listing.
<https://store-us.semi.org/products/m00100-semi-m1-specification-for-polished-single-crystal-silicon-wafers>
The industry standard that defines the diameter, thickness, notch,
flatness and resistivity classes a fab orders against. Used on step 001
and the substrate category page. Tier: cross-check.

**SEMI-P1** — SEMI, *SEMI P1 — Specification for Hard Surface Photomask
Substrates*, SEMI Standards store listing.
<https://store-us.semi.org/products/p00100-semi-p1-specification-for-hard-surface-photomask-substrates>
The specification for hard-surface photomask substrates. Used on step
004 and the lithography category page. Tier: deep dive.

#### University and course pages

**SNF-LPCVD** — Stanford Nanofabrication Facility, *Tystar LPCVD Tube
Training*, equipment training page.
<https://snfguide.stanford.edu/guide/equipment/training/tystar-lpcvd-tube-training>
A university facility guide to running a hot-wall LPCVD nitride tube.
Used on step 003. Tier: deep dive.

**SNF-NITRIDE-WET** — Stanford Nanofabrication Facility, *Silicon
Nitride Wet Etching*, equipment-purpose page.
<https://snfguide.stanford.edu/guide/equipment/purpose/etching/wet-etching/silicon-nitride-wet-etching>
A university facility page on the hot phosphoric bath in practice. Used
on step 013. Tier: deep dive.

**SNF-OXIDE** — Stanford Nanofabrication Facility, *Oxide Growth
(furnace)*, processing-technique page.
<https://snfguide.stanford.edu/guide/equipment/processing-technique/annealing-oxidation/oxide-growth-furnace>
A university facility page describing furnace oxidation practice and
recipes. Used on steps 002 and 010. Tier: deep dive.

### 8.9 SONOS and gate-dielectric module sources

None of these is a SkyWater or Cypress source unless marked. The step
pages for the SONOS and gate-dielectric module (steps 035–047: tunnel
oxide lithography and etch, punch-through stop, depletion implant, ONO
deposition, patterning and etch, thick and thin gate oxides, dual-oxide
lithography and etch) use them for era-typical values, mechanisms and
further reading. The Cypress SONOS patents in §5.3 remain the primary
public description of the module itself.

#### Papers and review articles

**BAKER-1996** — D. C. Baker and E. S. Capsuto, "Critical dimension
control for i-line 0.35-μm device using a new antireflective coating",
*Proc. SPIE* **2724**, Advances in Resist Technology and Processing
XIII, 710 (1996). <https://doi.org/10.1117/12.241869> CD control for an
i-line 0.35 µm device using a new anti-reflective coating. Used on steps
035, 036 and 041. Tier: deep dive.

**BEVERINA-2003** — A. Beverina, I. Guilmeau, J. P. Carrere, N. Emonet,
F. Guyader, V. Huard, S. Petitdidier and R. Velard, "'Resist / Wet Etch'
Couple for Dual Gate Oxide", *Solid State Phenomena* **92**, 235–238
(2003). <https://doi.org/10.4028/www.scientific.net/SSP.92.235> The
resist / wet-etch couple for dual gate oxide. Used on steps 044 and 046.
Tier: deep dive.

**BU-2001** — J. Bu and M. H. White, "Design considerations in scaled
SONOS nonvolatile memory devices", *Solid-State Electronics* **45**(1),
113–120 (2001). <https://doi.org/10.1016/S0038-1101(00)00232-X> Design
considerations in scaled SONOS devices, including the memory window.
Used on steps 038 and 040. Tier: deep dive.

**BUCHANAN-1999** — D. A. Buchanan, "Scaling the gate dielectric:
Materials, integration, and reliability", *IBM Journal of Research and
Development* **43**(3), 245–264 (1999).
<https://doi.org/10.1147/rd.433.0245> Scaling the gate dielectric:
materials, integration, reliability. Used on step 047. Tier: deep dive.

**CEROFOLINI-1998** — G. F. Cerofolini, "A study of the ionic route for
hydrogen terminations resulting after SiO₂ etching by concentrated
aqueous solutions of HF", *Applied Surface Science* **133**(1–2),
108–114 (1998). <https://doi.org/10.1016/S0169-4332(98)00182-2> How HF
etching leaves hydrogen-terminated silicon. Used on steps 039 and 046.
Tier: deep dive.

**COLVIN-2000** — J. B. Colvin and A. Roy, "Identification and Analysis
of Parasitic Depletion Mode Leakage in a Memory Select Transistor",
*ISTFA 2000: Proceedings of the 26th International Symposium for Testing
and Failure Analysis*, pp. 247–249 (2000).
<https://doi.org/10.31399/asm.cp.istfa2000p0247> Parasitic
depletion-mode leakage in a memory select transistor, the failure the
2-T cell must avoid. Used on step 038. Tier: deep dive.

**EDWARDS-1971** — J. R. Edwards and G. Marr, "Ion-implanted
depletion-mode IGFET", *1971 International Electron Devices Meeting*, p.
156. <https://doi.org/10.1109/IEDM.1971.188465> The ion-implanted
depletion-mode IGFET. Used on step 038. Tier: deep dive.

**EITAN-2000** — B. Eitan, P. Pavan, I. Bloom, E. Aloni, A. Frommer and
D. Finzi, "NROM: A novel localized trapping, 2-bit nonvolatile memory
cell", *IEEE Electron Device Letters* **21**(11), 543–545 (2000).
<https://doi.org/10.1109/55.877205> NROM, the localised charge-trapping
alternative. Used on step 040. Tier: deep dive.

**FLAMM-1981** — D. L. Flamm and V. M. Donnelly, "The design of plasma
etchants", *Plasma Chemistry and Plasma Processing* **1**(4), 317–363
(1981). <https://doi.org/10.1007/BF00565992> The design of plasma
etchants, including oxygen-based organic etches. Used on steps 036 and
042 and the etch category page. Tier: deep dive.

**FRENCH-1994** — M. L. French and M. H. White, "Scaling of
multidielectric nonvolatile SONOS memory structures", *Solid-State
Electronics* **37**(12), 1913–1923 (1994).
<https://doi.org/10.1016/0038-1101(94)90057-4> Scaling of
multi-dielectric SONOS structures. Used on steps 038 and 040. Tier: deep
dive.

**GREEN-2001** — M. L. Green, E. P. Gusev, R. Degraeve and E. L.
Garfunkel, "Ultrathin (<4 nm) SiO₂ and Si–O–N gate dielectric layers for
silicon microelectronics: Understanding the processing, structure, and
physical and electrical limits", *Journal of Applied Physics* **90**(5),
2057–2121 (2001). <https://doi.org/10.1063/1.1385803> A long review of
sub-4 nm SiO₂ and oxynitride gate dielectrics, their processing,
structure and electrical limits. Used on steps 043 and 047 and the
oxidation category page. Tier: deep dive.

**HATTANGADY-1995** — S. V. Hattangady, H. Niimi and G. Lucovsky,
"Controlled nitrogen incorporation at the gate oxide surface", *Applied
Physics Letters* **66**(25), 3495–3497 (1995).
<https://doi.org/10.1063/1.113775> Controlled nitrogen incorporation at
the gate-oxide surface. Used on step 047. Tier: deep dive.

**HORI-1988** — T. Hori and K. Kurimoto, "A new p-channel MOSFET with
large-tilt-angle implanted punchthrough stopper (LATIPS)", *IEEE
Electron Device Letters* **9**(12), 641–643 (1988).
<https://doi.org/10.1109/55.20422> The large-tilt-angle implanted
punch-through stopper (LATIPS). Used on step 037. Tier: deep dive.

**HORI-1989** — T. Hori, H. Iwasaki and K. Tsuji, "Electrical and
physical properties of ultrathin reoxidized nitrided oxides prepared by
rapid thermal processing", *IEEE Transactions on Electron Devices*
**36**(2), 340–350 (1989). <https://doi.org/10.1109/16.19935> Electrical
and physical properties of RTP reoxidised nitrided oxides. Used on step
047 and the oxidation category page. Tier: deep dive.

**HWANG-1991** — H. Hwang, W. Ting, D.-L. Kwong and J. Lee, "A physical
model for boron penetration through an oxynitride gate dielectric
prepared by rapid thermal processing in N₂O", *Applied Physics Letters*
**59**(13), 1581–1582 (1991). <https://doi.org/10.1063/1.106290> A
physical model of boron penetration through N₂O oxynitride. Used on step
047. Tier: deep dive.

**INUKAI-2000** — T. Inukai and T. Hiramoto, "Suppression of Stand-by
Tunnel Current in Ultra-Thin Gate Oxide MOSFETs by Dual Oxide
Thickness-Multiple Threshold Voltage CMOS (DOT-MTCMOS)", *Japanese
Journal of Applied Physics* **39**(4S), 2287 (2000).
<https://doi.org/10.1143/JJAP.39.2287> Dual oxide thickness / multiple
threshold CMOS for stand-by leakage. Used on step 044. Tier: deep dive.

**ITO-1980** — T. Ito, T. Nozaki and H. Ishikawa, "Direct Thermal
Nitridation of Silicon Dioxide Films in Anhydrous Ammonia Gas", *Journal
of The Electrochemical Society* **127**(9), 2053–2057 (1980).
<https://doi.org/10.1149/1.2130065> Direct thermal nitridation of SiO₂
in ammonia. Used on step 047. Tier: deep dive.

**JIEW-2012** — C. B. Jiew, Y. E. Chien and R. T. T. Yung, "Development
of a robust 2T-SONOS cell for embedded flash application", *2012 12th
Annual Non-Volatile Memory Technology Symposium (NVMTS)*, pp. 1–6.
<https://doi.org/10.1109/NVMTS.2013.6632849> Development of a robust
2T-SONOS cell for embedded flash, the same cell topology as SKY130's.
Used on steps 035, 038 and 041. Tier: deep dive.

**JUDGE-1971** — J. S. Judge, "A Study of the Dissolution of SiO₂ in
Acidic Fluoride Solutions", *Journal of The Electrochemical Society*
**118**(11), 1772 (1971). <https://doi.org/10.1149/1.2407835> The
dissolution kinetics of SiO₂ in acidic fluoride solutions. Used on steps
039 and 046. Tier: deep dive.

**KIKUYAMA-1994** — H. Kikuyama, M. Waki, M. Miyashita, T. Yabune, N.
Miki, J. Takano and T. Ohmi, "A Study of the Dissociation State and the
SiO₂ Etching Reaction for HF Solutions of Extremely Low Concentration",
*Journal of The Electrochemical Society* **141**(2), 366–374 (1994).
<https://doi.org/10.1149/1.2054733> Dissociation state and etching
reaction of extremely dilute HF. Used on steps 039 and 046. Tier: deep
dive.

**KIM-2001** — S.-H. Kim, S.-H. Kim, S.-E. Kim, M.-S. Kim, J.-H. Park
and E.-S. Kim, "New STI Scheme to Compensate Gate Oxide Thinning at STI
Corner Edge for the Devices Using Thick Dual Gate Oxide", *Extended
Abstracts of the 2001 International Conference on Solid State Devices
and Materials (SSDM)*, 2001. <https://doi.org/10.7567/SSDM.2001.A-6-6>
An STI scheme that compensates thinning at the STI corner for thick dual
gate oxides. Used on steps 044 and 046. Tier: deep dive.

**KRAFT-1997** — R. Kraft, T. P. Schneider, W. W. Dostalik and S.
Hattangady, "Surface nitridation of silicon dioxide with a high density
nitrogen plasma", *Journal of Vacuum Science & Technology B* **15**(4),
967–970 (1997). <https://doi.org/10.1116/1.589516> Surface nitridation
of SiO₂ with a high-density nitrogen plasma. Used on step 047. Tier:
deep dive.

**KUEHNE-1997** — J. Kuehne, S. Hattangady, J. Piccirillo, G. C. Xing,
G. E. Miner and D. Lopes, "Nitric Oxide Rapid Thermal Nitridation of
Thin Gate Oxides", *MRS Proceedings* **470**, 381 (1997).
<https://doi.org/10.1557/PROC-470-381> Nitric oxide rapid thermal
nitridation of thin gate oxides. Used on step 047. Tier: deep dive.

**LEE-1999** — S.-W. Lee, "Novel Dual Gate Oxide Process with Improved
Gate Oxide Integrity Reliability", *Electrochemical and Solid-State
Letters* **3**(1), 56 (1999). <https://doi.org/10.1149/1.1390957> A dual
gate oxide process with improved gate-oxide integrity. Used on steps
043, 044 and 046. Tier: deep dive.

**LEE-1999-ICVC** — S.-W. Lee, I. H. Cho, S. H. Park, H. G. Choi, N. G.
Kim, J.-K. Kim, S. B. Han and K. Lee, "Gate oxide thinning effects at
the edge of shallow trench isolation in the dual gate oxide process",
*ICVC '99: 6th International Conference on VLSI and CAD*, pp. 249–252.
<https://doi.org/10.1109/ICVC.1999.820895> Gate oxide thinning at the
STI edge in the dual gate oxide process. Used on steps 043, 044 and 046.
Tier: deep dive.

**LIBSCH-1990** — F. R. Libsch and M. H. White, "Charge transport and
storage of low programming voltage SONOS/MONOS memory devices",
*Solid-State Electronics* **33**(1), 105–126 (1990).
<https://doi.org/10.1016/0038-1101(90)90017-9> Charge transport and
storage in low-voltage SONOS/MONOS devices. Used on step 040. Tier: deep
dive.

**LIN-1997** — C.-H. Lin, J.-J. Yang, K. Young and K.-Y. Chiu,
"Optimization of tilt-implanted punchthrough stopper on short-channel
behavior in quarter-micron MOSFET with low-concentration wells", *Proc.
1997 International Symposium on VLSI Technology, Systems, and
Applications*, pp. 303–306. <https://doi.org/10.1109/VTSA.1997.614915>
Optimising a tilt-implanted punch-through stopper in quarter-micron
MOSFETs. Used on step 037. Tier: deep dive.

**LINLIU-2000** — K. Linliu, M.-R. Kuo and Y.-R. Huang, "Novel polymeric
antireflective coating (PARC) for better uniformity control of critical
dimension", *Proc. SPIE* **4000**, Optical Microlithography XIII, 915
(2000). <https://doi.org/10.1117/12.389087> A polymeric ARC for better
CD uniformity. Used on step 036. Tier: deep dive.

**LO-1997** — S.-H. Lo, D. A. Buchanan, Y. Taur and W. Wang,
"Quantum-mechanical modeling of electron tunneling current from the
inversion layer of ultra-thin-oxide nMOSFET's", *IEEE Electron Device
Letters* **18**(5), 209–211 (1997). <https://doi.org/10.1109/55.568766>
Tunnelling current through ultrathin oxides. Used on step 047. Tier:
deep dive.

**LUE-2005** — H.-T. Lue, S.-Y. Wang, E.-K. Lai, Y.-H. Shih, S.-C. Lai,
L.-W. Yang, K.-C. Chen, K.-Y. Hsieh, R. Liu and C.-Y. Lu, "BE-SONOS: A
bandgap engineered SONOS with excellent performance and reliability",
*IEDM 2005 Technical Digest*, pp. 547–550.
<https://doi.org/10.1109/IEDM.2005.1609404> Bandgap-engineered SONOS,
the multi-layer tunnel dielectric idea. Used on step 040. Tier: deep
dive.

**MA-1998** — T. P. Ma, "Making silicon nitride film a viable gate
dielectric", *IEEE Transactions on Electron Devices* **45**(3), 680–690
(1998). <https://doi.org/10.1109/16.661229> Silicon nitride as a gate
dielectric, the nitrogen-rich end of the spectrum. Used on step 047.
Tier: deep dive.

**MAXIM-2003** — A. Maxim, "A low voltage, 10-2550MHz, 0.15μ CMOS,
process and divider modulus independent PLL using zero-VT MOSFETs",
*Proc. ESSCIRC 2003 — 29th European Solid-State Circuits Conference*,
pp. 105–108. <https://doi.org/10.1109/ESSCIRC.2003.1257083> A circuit
built on zero-Vt MOSFETs, showing what designers do with
near-zero-threshold devices. Used on step 038. Tier: deep dive.

**MONK-1994** — D. J. Monk, D. S. Soane and R. T. Howe, "Hydrofluoric
Acid Etching of Silicon Dioxide Sacrificial Layers: I. Experimental
Observations" and "II. Modeling", *Journal of The Electrochemical
Society* **141**(1), 264–269 and 270–274 (1994).
<https://doi.org/10.1149/1.2054696>, <https://doi.org/10.1149/1.2054697>
HF etching of silicon dioxide, experiments and model. Used on steps 039
and 046. Tier: deep dive.

**NULMAN-1985** — J. Nulman, J. P. Krusius and A. Gat, "Rapid thermal
processing of thin gate dielectrics. Oxidation of silicon", *IEEE
Electron Device Letters* **6**(5), 205–207 (1985).
<https://doi.org/10.1109/EDL.1985.26099> Rapid thermal oxidation of thin
gate dielectrics. Used on steps 043 and 047. Tier: deep dive.

**PFIESTER-1990** — J. R. Pfiester, F. K. Baker, T. C. Mele, H.-H.
Tseng, P. J. Tobin, J. D. Hayden, J. W. Miller, C. D. Gunderson and L.
C. Parrillo, "The effects of boron penetration on p⁺ polysilicon gated
PMOS devices", *IEEE Transactions on Electron Devices* **37**(8),
1842–1851 (1990). <https://doi.org/10.1109/16.57135> Boron penetration
through thin oxides from p⁺ poly gates. Used on step 047. Tier: deep
dive.

**RAMANATHAN-1998** — V. Ramanathan, S. Chen, K. Lai, M. R. Brongo and
N. Samarakone, "Etch integration issues in the development of deep
submicron contacts utilizing DUV resist and organic BARC", *Proc. SPIE*
**3333**, Advances in Resist Technology and Processing XV, 909 (1998).
<https://doi.org/10.1117/12.312473> Etch integration issues with DUV
resist over organic BARC. Used on step 036. Tier: deep dive.

**ROZE-2017** — F. Rozé, O. Gourhant, E. Blanquet, F. Bertin, M. Juhel,
F. Abbate, C. Pribat and R. Duru, "Oxidation kinetics of Si and SiGe by
dry rapid thermal oxidation, in-situ steam generation oxidation and dry
furnace oxidation", *Journal of Applied Physics* **121**(24), 245308
(2017). <https://doi.org/10.1063/1.4987040> Oxidation kinetics of dry
RTO, ISSG and dry furnace oxidation compared. Used on steps 040, 043 and
047. Tier: deep dive.

**STATHIS-2002** — J. H. Stathis, "Reliability limits for the gate
insulator in CMOS technology", *IBM Journal of Research and Development*
**46**(2.3), 265–286 (2002). <https://doi.org/10.1147/rd.462.0265>
Reliability limits of the gate insulator. Used on step 047. Tier: deep
dive.

**STEINBRUCHEL-1989** — C. Steinbrüchel, "Universal energy dependence of
physical and ion-enhanced chemical etch yields at low ion energy",
*Applied Physics Letters* **55**(19), 1960–1962 (1989).
<https://doi.org/10.1063/1.102336> The energy dependence of ion-enhanced
etch yields, governing the low-bias ARC open. Used on step 036 and the
etch category page. Tier: deep dive.

**TOGO-1998** — M. Togo, K. Noda and T. Tanigawa (NEC),
"Multiple-thickness gate oxide and dual-gate technologies for
high-performance logic-embedded DRAMs", *IEDM 1998 Technical Digest*,
pp. 347–350. <https://doi.org/10.1109/IEDM.1998.746371>
Multiple-thickness gate oxide and dual-gate technologies for embedded
DRAM. Used on steps 043 and 044. Tier: deep dive.

**TSENG-1998** — H.-H. Tseng, D. L. O'Meara, P. J. Tobin, V. S. Wang, X.
Guo, R. Hegde, I. Y. Yang, P. Gilbert et al. (Motorola), "Reduced gate
leakage current and boron penetration of 0.18 μm 1.5 V MOSFETs using
integrated RTCVD oxynitride gate dielectric", *IEDM 1998 Technical
Digest*, pp. 793–796. <https://doi.org/10.1109/IEDM.1998.746475> Reduced
leakage and boron penetration with an RTCVD oxynitride at 0.18 µm. Used
on step 047. Tier: deep dive.

**VAN-SCHAIJK-2004** — R. van Schaijk, M. van Duuren, W. Y. Mei, K. van
der Jeugd, A. Rothschild and M. Demand, "Oxide–nitride–oxide layer
optimisation for reliable embedded SONOS memories", *Microelectronic
Engineering* **72**(1–4), 395–398 (2004).
<https://doi.org/10.1016/j.mee.2004.01.021> ONO layer optimisation for
reliable embedded SONOS. Used on step 040. Tier: deep dive.

**WINTERS-1992** — H. F. Winters and J. W. Coburn, "Surface science
aspects of etching reactions", *Surface Science Reports* **14**(4–6),
162–269 (1992). <https://doi.org/10.1016/0167-5729(92)90009-Z>
Surface-science mechanisms of fluorine-based etching. Used on step 042
and the etch category page. Tier: deep dive.

**WRIGHT-1990** — P. J. Wright and K. C. Saraswat, "Thickness
limitations of SiO₂ gate dielectrics for MOS ULSI", *IEEE Transactions
on Electron Devices* **37**(8), 1884–1892 (1990).
<https://doi.org/10.1109/16.57140> Thickness limitations of SiO₂ gate
dielectrics. Used on steps 043 and 047. Tier: deep dive.

**XU-2001** — S. Xu, T. Lill and D. Podlesnik, "Wall-dependent etching
characteristics of organic antireflection coating in O₂+halogen/hydrogen
halide plasma", *Journal of Vacuum Science & Technology A* **19**(6),
2893–2899 (2001). <https://doi.org/10.1116/1.1412655> Wall-dependent
etching of organic ARC in O₂ + halogen / hydrogen halide plasmas. Used
on step 036. Tier: deep dive.

**YANG-2000** — Y. Yang and M. H. White, "Charge retention of scaled
SONOS nonvolatile memory devices at elevated temperatures", *Solid-State
Electronics* **44**(6), 949–958 (2000).
<https://doi.org/10.1016/S0038-1101(00)00012-5> Charge retention of
scaled SONOS at elevated temperature. Used on step 040. Tier: deep dive.

**YU-1999** — M.-C. Yu, S.-M. Jang, C. H. Diaz, C. H. Yu, S. C. Sun and
M. S. Liang (TSMC), "Improvement of ultrathin gate oxide by a novel
rapid thermal oxidation process with in-situ steam generation", *Proc.
SPIE* **3881**, Microelectronic Device Technology III, 234 (1999).
<https://doi.org/10.1117/12.360557> Ultrathin gate oxide grown by
in-situ steam generation in an RTP chamber. Used on steps 040, 043 and
047 and the oxidation category page. Tier: deep dive.

#### Books and book chapters

**BREWER-GILL-2007** — J. E. Brewer and M. Gill (eds.), *Nonvolatile
Memory Technologies with Emphasis on Flash: A Comprehensive Guide to
Understanding and Using NVSM Devices*, Wiley-IEEE Press, 2007.
<https://doi.org/10.1002/9780470181355> The SONOS chapters. Used on step
040. Tier: high-level.

**HORI-1997** — T. Hori, *Gate Dielectrics and MOS ULSIs: Physics,
Technology and Applications*, Springer Series in Electronics and
Photonics, vol. 34, Springer, 1997.
<https://doi.org/10.1007/978-3-642-60856-8> Monograph on nitrided and
reoxidised-nitrided gate oxides. Used on steps 043 and 047 and the
oxidation category page. Tier: deep dive.

**MERCKEL-1977** — G. Merckel, "Ion Implanted MOS Transistors —
Depletion Mode Devices", in *Process and Device Modeling for Integrated
Circuit Design*, Springer, 1977, pp. 677–688.
<https://doi.org/10.1007/978-94-011-7583-8_24> Modelling of
ion-implanted depletion-mode transistors. Used on step 038. Tier: deep
dive.

**NOJIRI-2015** — K. Nojiri, *Dry Etching Technology for
Semiconductors*, Springer, 2015.
<https://doi.org/10.1007/978-3-319-10295-5> A production-oriented
monograph on poly, oxide and metal etch chemistries and endpoint. Used
on steps 036 and 042 and the etch category page. Tier: deep dive.

#### Patents

**PAT-CN-TEL** — Tokyo Electron Ltd., *Method of forming a semiconductor
device using double endpoint detection*, US 6,376,262 B1, granted
2002-04-23. <https://patents.google.com/patent/US6376262B1/en> CN
emission at 387 nm as the nitride etch endpoint. Label ↔ key: the same
patent is cited as `pat-endpoint-tel` on the etch category page
(PAT-ENDPOINT-TEL). Used on step 042. Tier: cross-check.

**PAT-ONO-THICK-CYP** — K. Ramkumar (Cypress Semiconductor), *Method of
integration of ONO stack formation into thick gate oxide CMOS flow*, US
9,824,895 B1, granted 2017-11-21.
<https://patents.google.com/patent/US9824895B1/en> The alternative
ordering with the thick gate oxide before the ONO, and why. Used on step
043. Tier: cross-check.

**PAT-RADOX-CYP** — K. Ramkumar, S. Levy and J. Byun (Cypress
Semiconductor), *Radical oxidation process for fabricating a nonvolatile
charge trap memory device*, US 8,940,645 B2, granted 2015-01-27.
<https://patents.google.com/patent/US8940645B2/en> A radical oxidation
process for the ONO stack with trap-free and trap-dense oxynitride
layers. Used on step 040. Tier: deep dive.

#### SkyWater and PDK sources

**PDK-MODEL-NFET01V8** — SkyWater PDK Authors,
`sky130_fd_pr__nfet_01v8__tt.pm3.spice` (typical-corner BSIM4 model,
parameter `toxe`), google/skywater-pdk-libs-sky130_fd_pr repository.
<https://raw.githubusercontent.com/google/skywater-pdk-libs-sky130_fd_pr/main/cells/nfet_01v8/sky130_fd_pr__nfet_01v8__tt.pm3.spice>
The BSIM4 `toxe` parameter of the 1.8 V NMOS model, a public electrical
oxide thickness. Used on steps 043, 044, 046 and 047. Tier: cross-check.

**PDK-MODEL-NFET5V** — SkyWater PDK Authors,
`sky130_fd_pr__nfet_g5v0d10v5__tt.pm3.spice` (typical-corner BSIM4
model, parameter `toxe`), google/skywater-pdk-libs-sky130_fd_pr
repository.
<https://raw.githubusercontent.com/google/skywater-pdk-libs-sky130_fd_pr/main/cells/nfet_g5v0d10v5/sky130_fd_pr__nfet_g5v0d10v5__tt.pm3.spice>
The BSIM4 `toxe` parameter of the 5 V NMOS model, a public electrical
oxide thickness. Used on steps 043, 044 and 047. Tier: cross-check.

**PDK-SONOS-XS** — SkyWater PDK Authors, `cross-section-sonos-cell.svg`
(2-T SONOS cell cross-section drawing), google/skywater-pdk repository,
`docs/rules/device-details/special_sonosfet/`.
<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/special_sonosfet/cross-section-sonos-cell.svg>
The labelled "Depletion Implant" in the 2-T cell drawing. Used on step
038. Tier: cross-check.

### 8.10 Category-page sources (by category)

Sources cited only on the category pages (`docs/categories/*.md`),
grouped by the category page that introduced them; where a source is
shared between categories it is listed once, under the first, and the
entry names every page that uses it. These pages are process-generic:
none of the sources describes SkyWater unless the entry says so.

#### Substrate

##### Papers and review articles

**BEAN-1978** — K. E. Bean, "Anisotropic etching of silicon", *IEEE
Transactions on Electron Devices* **25**(10), 1185–1193 (1978).
<https://doi.org/10.1109/T-ED.1978.19250> Crystal-plane behaviour of
silicon in anisotropic etching. Used on the substrate category page.
Tier: deep dive.

**DASH-1959** — W. C. Dash, "Growth of Silicon Crystals Free from
Dislocations", *Journal of Applied Physics* **30**(4), 459–474 (1959).
<https://doi.org/10.1063/1.1702390> The "Dash neck" technique that gives
dislocation-free CZ crystals. Used on the substrate category page. Tier:
deep dive.

**MYERS-2000** — S. M. Myers, M. Seibt and W. Schröter, "Mechanisms of
transition-metal gettering in silicon", *Journal of Applied Physics*
**88**(7), 3795–3819 (2000). <https://doi.org/10.1063/1.1289273> Review
of the mechanisms of transition-metal gettering. Used on the substrate
category page. Tier: deep dive.

**SRINIVASAN-1980** — G. R. Srinivasan, "Autodoping Effects in Silicon
Epitaxy", *Journal of The Electrochemical Society* **127**(6), 1334–1342
(1980). <https://doi.org/10.1149/1.2129895> Autodoping during silicon
epitaxy, the main process problem of p/p⁺ epi wafers. Used on the
substrate category page. Tier: deep dive.

**VORONKOV-1982** — V. V. Voronkov, "The mechanism of swirl defects
formation in silicon", *Journal of Crystal Growth* **59**(3), 625–643
(1982). <https://doi.org/10.1016/0022-0248(82)90386-4> The v/G theory of
vacancy- versus interstitial-rich growth that governs grown-in defects.
Used on the substrate category page. Tier: deep dive.

##### Patents

**PAT-MDZ-MEMC** — R. Falster, M. Cornara, D. Gambaro and M. Olmo (MEMC
Electronic Materials), *Ideal oxygen precipitating silicon wafers and
oxygen out-diffusion-less process therefor*, US 5,994,761 A, granted
1999-11-30.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5994761>
The "magic denuded zone" rapid-thermal treatment that sets precipitation
behaviour without an oxygen out-diffusion anneal. Used on the substrate
category page. Tier: deep dive.

##### Standards and roadmaps

**SEMI-M62** — SEMI M62, *Specification for Silicon Epitaxial Wafers*,
SEMI.
<https://store-us.semi.org/products/m06200-semi-m62-specification-for-silicon-epitaxial-wafers>
The specification for epitaxial wafers. Used on the substrate category
page. Tier: cross-check.

**SEMI-M8** — SEMI M8, *Specification for Polished Monocrystalline
Silicon Test Wafers*, SEMI.
<https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
The looser specification for polished test wafers. Used on the substrate
category page. Tier: cross-check.

#### Oxidation

##### Papers and review articles

**HU-1974** — S. M. Hu, "Formation of stacking faults and enhanced
diffusion in the oxidation of silicon", *Journal of Applied Physics*
**45**(4), 1567–1573 (1974). <https://doi.org/10.1063/1.1663459>
Oxidation-induced stacking faults and oxidation-enhanced diffusion from
injected interstitials. Used on the oxidation category page. Tier: deep
dive.

**LIGENZA-1960** — J. R. Ligenza and W. G. Spitzer, "The mechanisms for
silicon oxidation in steam and oxygen", *Journal of Physics and
Chemistry of Solids* **14**, 131–136 (1960).
<https://doi.org/10.1016/0022-3697(60)90219-5> The isotope experiments
showing that the oxidant diffuses through the oxide to react at the
interface. Used on the oxidation category page. Tier: deep dive.

**MASSOUD-1985B** — H. Z. Massoud, J. D. Plummer and E. A. Irene,
"Thermal Oxidation of Silicon in Dry Oxygen: Growth-Rate Enhancement in
the Thin Regime. II. Physical Mechanisms", *Journal of The
Electrochemical Society* **132**(11), 2693–2700 (1985).
<https://doi.org/10.1149/1.2113649> Candidate physical mechanisms for
the thin-regime enhancement. Used on the oxidation category page. Tier:
deep dive.

**MASSOUD-1987** — H. Z. Massoud and J. D. Plummer, "Analytical
relationship for the oxidation of silicon in dry oxygen in the thin-film
regime", *Journal of Applied Physics* **62**(8), 3416–3423 (1987).
<https://doi.org/10.1063/1.339305> The closed-form thin-film oxidation
relationship used by growth calculators. Used on the oxidation category
page. Tier: deep dive.

**NAGAI-2002** — N. Nagai, K. Terada, Y. Muraji, H. Hashimoto et al.,
"Infrared absorption study of rapid thermal oxidation and in situ steam
generation of thin SiO₂ films by gradient etching preparation", *Journal
of Applied Physics* **91**(7), 4747–4750 (2002).
<https://doi.org/10.1063/1.1459097> Infrared study comparing RTO and
ISSG thin oxides. Used on the oxidation category page. Tier: deep dive.

**TAN-1982** — T. Y. Tan and U. Gösele, "Oxidation-enhanced or retarded
diffusion and the growth or shrinkage of oxidation-induced stacking
faults in silicon", *Applied Physics Letters* **40**(7), 616–619 (1982).
<https://doi.org/10.1063/1.93200> Growth and shrinkage of
oxidation-induced stacking faults tied to the interstitial
supersaturation. Used on the oxidation category page. Tier: deep dive.

##### Patents

**PAT-DGOX-AMD** — M. I. Gardner (Advanced Micro Devices), *Dual gate
oxide thickness integrated circuit and process for making same*, US
6,033,943 A, granted 2000-03-07.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6033943>
A dual-gate-oxide process: first oxide, masked strip, second oxidation.
Used on the oxidation category page. Tier: deep dive.

##### Standards and roadmaps

**SEMI-MF576** — SEMI MF576, *Test Method for Measurement of Insulator
Thickness and Refractive Index on Silicon Substrates by Ellipsometry*,
SEMI.
<https://store-us.semi.org/products/mf057600-semi-mf576-test-method-for-measurement-of-insulator-thickness-and-refractive-index-on-silicon-substrates-by-ellipsometry>
The standard ellipsometric test method for insulator thickness and
refractive index on silicon. Used on the oxidation category page. Tier:
deep dive.

##### University and course pages

**BYU-OXCALC** — Brigham Young University Cleanroom, *Oxide Growth
Calculator* (Deal–Grove with thin-oxide correction).
<https://cleanroom.byu.edu/oxidetimecalc> Deal–Grove with the thin-oxide
correction, runnable online. Used on the oxidation category page. Tier:
high-level.

#### Deposition

##### Papers and review articles

**ADAMS-1979** — A. C. Adams and C. D. Capio, "The Deposition of Silicon
Dioxide Films at Reduced Pressure", *Journal of The Electrochemical
Society* **126**(6), 1042–1046 (1979).
<https://doi.org/10.1149/1.2129171> LPCVD oxide deposition, including
TEOS and doped glasses. Used on the deposition category page. Tier: deep
dive.

**AMES-1970** — I. Ames, F. M. d'Heurle and R. E. Horstmann, "Reduction
of Electromigration in Aluminum Films by Copper Doping", *IBM Journal of
Research and Development* **14**(4), 461–463 (1970).
<https://doi.org/10.1147/rd.144.0461> The original demonstration that
copper doping suppresses aluminium electromigration. Used on the
deposition category page. Tier: deep dive.

**BLECH-1976** — I. A. Blech, "Electromigration in thin aluminum films
on titanium nitride", *Journal of Applied Physics* **47**(4), 1203–1208
(1976). <https://doi.org/10.1063/1.322842> The critical-length effect
measured on Al lines over TiN. Used on the deposition category page.
Tier: cross-check.

**BOHR-1995** — M. T. Bohr, "Interconnect scaling — the real limiter to
high performance ULSI", *IEDM 1995 Technical Digest*, pp. 241–244.
<https://doi.org/10.1109/IEDM.1995.499187> Why interconnect, not the
transistor, limits performance, motivating the metallisation stack. Used
on the deposition category page. Tier: deep dive.

**KAANTA-1987** — C. Kaanta, W. Cote, J. Cronin, K. Holland et al.,
"Submicron wiring technology with tungsten and planarization", *IEDM
1987 Technical Digest*, pp. 209–212.
<https://doi.org/10.1109/IEDM.1987.191389> The tungsten-stud plus
planarisation wiring scheme that became the standard plug process. Used
on the deposition category page. Tier: deep dive.

**KAMINS-1980** — T. I. Kamins, "Structure and Properties of LPCVD
Silicon Films", *Journal of The Electrochemical Society* **127**(3),
686–690 (1980). <https://doi.org/10.1149/1.2129733> Structure and
properties of LPCVD silicon films as a function of deposition
temperature. Used on the deposition category page. Tier: deep dive.

**RAUPP-1992** — G. B. Raupp, T. S. Cale and H. P. W. Hey, "The role of
oxygen excitation and loss in plasma-enhanced deposition of silicon
dioxide from tetraethylorthosilicate", *Journal of Vacuum Science &
Technology B* **10**(1), 37–45 (1992).
<https://doi.org/10.1116/1.586361> Reaction kinetics of PECVD TEOS oxide
and their effect on step coverage. Used on the deposition category page.
Tier: deep dive.

**ROSSNAGEL-1994** — S. M. Rossnagel and J. Hopwood, "Metal ion
deposition from ionized magnetron sputtering discharge", *Journal of
Vacuum Science & Technology B* **12**(1), 449–453 (1994).
<https://doi.org/10.1116/1.587142> The first ionised-magnetron (IMP)
metal deposition experiments. Used on the deposition category page.
Tier: deep dive.

**ROSSNAGEL-1998** — S. M. Rossnagel, "Directional and ionized physical
vapor deposition for microelectronics applications", *Journal of Vacuum
Science & Technology B* **16**(5), 2585–2608 (1998).
<https://doi.org/10.1116/1.590242> Review of collimated and ionised PVD
for liners and barriers. Used on the deposition category page. Tier:
deep dive.

**THORNTON-1974** — J. A. Thornton, "Influence of apparatus geometry and
deposition conditions on the structure and topography of thick sputtered
coatings", *Journal of Vacuum Science and Technology* **11**(4), 666–670
(1974). <https://doi.org/10.1116/1.1312732> The structure-zone diagram
for sputtered films versus pressure and temperature. Used on the
deposition category page. Tier: deep dive.

##### Books and book chapters

**OHRING-2002** — M. Ohring, *Materials Science of Thin Films*, 2nd ed.,
Academic Press, 2002.
<https://doi.org/10.1016/B978-0-12-524975-1.X5000-9> Nucleation, growth
regimes, step coverage and the structure-zone model. Used on the
deposition category page. Tier: deep dive.

**SESHAN-2002** — K. Seshan (ed.), *Handbook of Thin-Film Deposition
Processes and Techniques: Principles, Methods, Equipment and
Applications*, 2nd ed., Noyes Publications / William Andrew, 2002, ISBN
978-0-8155-1442-8. <https://openlibrary.org/isbn/9780815514428>
Chapter-per-technique reference on CVD, PECVD, PVD and their equipment.
Used on the deposition category page. Tier: deep dive.

##### Patents

**PAT-IMP-AMAT** — P. Gopalraja, S. Edelstein, A. Tepman, P. Ding, D. Ghosh
and N. Maity (Applied Materials), *Alternate steps of IMP and sputtering
process to improve sidewall coverage*, US 6,350,353 B2, filed 1999-11-24,
granted 2002-02-26.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6350353>
Alternating IMP and conventional sputtering to improve sidewall
coverage. Used on the deposition category page. Tier: cross-check.

**PAT-TIW-HITACHI** — Hitachi Metals, *Titanium-tungsten target material
for sputtering and manufacturing method therefor*, US 5,160,534 A,
granted 1992-11-03. <https://patents.google.com/patent/US5160534A/en>
The 10 wt.% Ti composition of Ti:W sputter targets. Used on the
deposition category page. Tier: cross-check.

##### Vendor, regulatory, marketplace and press pages

**AMAT-10K** — Applied Materials, Inc., Form 10-K for fiscal 2003
(platform descriptions: Centura, Endura, Endura SL, Producer).
<https://www.sec.gov/Archives/edgar/data/6951/000089161804000093/f95058e10vk.htm>
Centura, Endura and Producer platform descriptions. Used on the
deposition category page. Tier: cross-check.

**AMAT-ENDURA** — Applied Materials, *Endura PVD*, product page.
<https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html>
Current product page for the Endura PVD platform (cluster architecture
and chamber types). Used on the deposition category page. Tier:
cross-check.

**ASM-A400** — ASM International, *ASM International N.V. launches A400
DUO vertical furnace system*, press release, 2019-11-11.
<https://www.asm.com/press-releases/asm-international-nv-launches-a400-duo-vertical-furnace-system-1944469>
The A400 furnace's install base and wet-oxidation/anneal use. Used on
the deposition and oxidation category pages. Tier: cross-check.

**NOVELLUS-HISTORY** — Encyclopedia.com, *Novellus Systems, Inc.*
(company history: Concept One/Two, Sequel, SPEED, Altus).
<https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
The Concept One/Two, Sequel, SPEED and Altus product history. Used on
the deposition category page. Tier: cross-check.

#### Lithography

##### Papers and review articles

**BOSSUNG-1977** — J. W. Bossung, "Projection Printing
Characterization", *Proc. SPIE* **100**, 80–85 (1977).
<https://doi.org/10.1117/12.955357> The focus–exposure ("Bossung") plots
used to characterise projection printing. Used on the lithography
category page. Tier: deep dive.

**BRUNING-2007** — J. H. Bruning, "Optical lithography: 40 years and
holding", *Proc. SPIE* **6520**, 652004 (2007).
<https://doi.org/10.1117/12.720631> A history of optical lithography
tools from contact printers to scanners. Used on the lithography
category page. Tier: deep dive.

**BRUNNER-1991** — T. A. Brunner, "Optimization of optical properties of
resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
<https://doi.org/10.1117/12.46410> Optimising resist-stack optical
properties: swing curves and anti-reflective layers. Used on the
lithography category page. Tier: deep dive.

**DAMMEL-1993** — R. R. Dammel, *Diazonaphthoquinone-based Resists*,
SPIE Tutorial Texts TT11, SPIE Press, 1993.
<https://doi.org/10.1117/3.2265072> The SPIE tutorial text on i-line
resist chemistry. Used on the lithography category page. Tier: deep
dive.

**ITO-1983** — H. Ito and C. G. Willson, "Chemical amplification in the
design of dry developing resist materials", *Polymer Engineering &
Science* **23**(18), 1012–1018 (1983).
<https://doi.org/10.1002/pen.760231807> The first chemical amplification
resist paper. Used on the lithography category page. Tier: deep dive.

**ITO-1984** — H. Ito and C. G. Willson, "Applications of
Photoinitiators to the Design of Resists for Semiconductor
Manufacturing", *ACS Symposium Series* **242**, 11–23 (1984).
<https://doi.org/10.1021/bk-1984-0242.ch002> The chemically amplified
resist concept applied to semiconductor manufacturing. Used on the
lithography category page. Tier: deep dive.

**LEVENSON-1982** — M. D. Levenson, N. S. Viswanathan and R. A. Simpson,
"Improving resolution in photolithography with a phase-shifting mask",
*IEEE Transactions on Electron Devices* **29**(12), 1828–1836 (1982).
<https://doi.org/10.1109/T-ED.1982.21037> The original phase-shifting
mask paper. Used on the lithography category page. Tier: deep dive.

**LEVINSON-1987** — H. J. Levinson and W. H. Arnold, "Focus: The
critical parameter for submicron lithography", *Journal of Vacuum
Science & Technology B* **5**(1), 293–298 (1987).
<https://doi.org/10.1116/1.583886> Focus as the critical parameter for
submicron lithography, and its budget. Used on the lithography category
page. Tier: deep dive.

**LIN-1986** — B. J. Lin, "Where Is The Lost Resolution?", *Proc. SPIE*
**633**, 44 (1986). <https://doi.org/10.1117/12.963701> Where the
resolution is lost between the Rayleigh limit and production practice.
Used on the lithography category page. Tier: deep dive.

**LIN-1993** — B. J. Lin, "Phase-shifting masks gain an edge", *IEEE
Circuits and Devices Magazine* **9**(2), 28–35 (1993).
<https://doi.org/10.1109/101.200850> A tutorial on alternating and
attenuated phase-shift masks. Used on the lithography category page.
Tier: deep dive.

**LIN-2002** — B. J. Lin, "The k₃ coefficient in nonparaxial λ/NA
scaling equations for resolution, depth of focus, and immersion
lithography", *Journal of Micro/Nanolithography, MEMS, and MOEMS*
**1**(1), 7–12 (2002). <https://doi.org/10.1117/1.1445798> The k₁ and k₃
coefficients and the nonparaxial scaling equations for resolution and
depth of focus. Used on the lithography category page. Tier: deep dive.

**MACK-1988** — C. A. Mack, "Understanding Focus Effects In
Submicrometer Optical Lithography", *Optical Engineering* **27**(12)
(1988). <https://doi.org/10.1117/12.7978683> Understanding focus effects
in submicrometre optical lithography. Used on the lithography category
page. Tier: deep dive.

**REICHMANIS-1989** — E. Reichmanis and L. F. Thompson, "Polymer
materials for microlithography", *Chemical Reviews* **89**(6), 1273–1289
(1989). <https://doi.org/10.1021/cr00096a001> Polymer materials for
microlithography, DNQ/novolak included. Used on the lithography category
page. Tier: deep dive.

**RIEGER-1994** — M. L. Rieger and J. P. Stirniman, "Using behavior
modeling for proximity correction", *Proc. SPIE* **2197**, 371–376
(1994). <https://doi.org/10.1117/12.175431> Model-based ("behaviour
modelling") proximity correction. Used on the lithography category page.
Tier: deep dive.

**STARIKOV-1992** — A. Starikov, "Accuracy of overlay measurements: tool
and mark asymmetry effects", *Optical Engineering* **31**(6), 1298
(1992). <https://doi.org/10.1117/12.56172> Accuracy of overlay
measurements and tool-induced shift. Used on the lithography category
page. Tier: deep dive.

**TOLPYGO-2014** — S. K. Tolpygo et al., "Fabrication Process and
Properties of Fully-Planarized Deep-Submicron Nb/Al-AlOx/Nb Josephson
Junctions for VLSI Circuits", arXiv:1408.5829 (2014) — describes a Canon
FPA-3000EX4 248 nm stepper with 5× reduction and NA 0.6.
<https://arxiv.org/abs/1408.5829> A Canon FPA-3000EX4 described in use.
Used on the lithography category page. Tier: cross-check.

**WALLRAFF-1999** — G. M. Wallraff and W. D. Hinsberg, "Lithographic
Imaging Techniques for the Formation of Nanoscopic Features", *Chemical
Reviews* **99**(7), 1801–1822 (1999).
<https://doi.org/10.1021/cr980003i> Lithographic imaging techniques and
resist chemistry for sub-quarter-micron features. Used on the
lithography category page. Tier: deep dive.

##### Books and book chapters

**LEVINSON-2019** — H. J. Levinson, *Principles of Lithography*, 4th
ed., SPIE Press, 2019, ISBN 978-1-5106-2760-4.
<https://doi.org/10.1117/3.2525393> Tools, resists, overlay and
metrology in one volume. Used on the lithography category page. Tier:
high-level.

##### Vendor, regulatory, marketplace and press pages

**ASML-30** — ASML, *Three decades of PAS 5500*, 2021.
<https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
ASML's own account of the PAS 5500 platform's three-decade lifetime.
Used on the lithography category page. Tier: cross-check.

**ASML-750E** — ASML, *ASML introduces KrF lithography scanner* (PAS
5500/750E), press release, 2000-04-04.
<https://www.asml.com/en/news/press-releases/2000/asml-introduces-krf-lithography-scanner-optimized-for>
130 nm resolution at 248 nm, NA 0.7, 120 wafers per hour. Used on the
lithography category page. Tier: cross-check.

**ASML-800** — ASML, *ASML introduces new KrF Step & Scan system* (PAS
5500/800), press release, 2001-01-31.
<https://www.asml.com/en/news/press-releases/2001/asml-introduces-new-krf-step-and-scan-system-that-extends>
NA 0.80, 120 nm resolution. Used on the lithography category page. Tier:
cross-check.

**CHIPHISTORY-PAS5500** — Chip History Center, *PAS 5500/400 Step & Scan
Alignment System from ASML*.
<https://www.chiphistory.org/163-asml-pas-5500-400-step-scan-system> The
ASML platform in its historical context. Used on the lithography
category page. Tier: deep dive.

**GCE-KLA8100** — GCE Market, *KLA-Tencor 8100XP CD-SEM* (specification
summary).
<https://www.gcemarket.com/gce/gce.nsf/products/kla-tencor-8100xp-cd-sem-7expup>
Marketplace specification summary for the KLA-Tencor 8100XP CD-SEM
(accelerating voltage and resolution). Used on the lithography category
page. Tier: cross-check.

**MICROCHEMICALS-DEV** — MicroChemicals, *Development of photoresists*,
application note.
<https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>
TMAH developer strength and practice. Used on the lithography category
page. Tier: cross-check.

**NIKON-S204B** — Nikon, *NSR-S204B 248 nm Scanner Exposure System
Overview* (specification summary, reseller copy), attached to the
listing Tara Semiconductor Technology, *Used 2002 NIKON S204 Scanner*
(listing LITV25-01), accessed 2026-09-12.
<https://f.machineryhost.com/fc49306d97602c8ed1be1dfbf0835ead/aa008f2897d7d4a224ff92839b4299e9/SpecSummary_LITV25-01_NSR-S204B.pdf>,
<https://www.tarasemi.com/listings/5223879-used-2002-nikon-s204-scanner>
Field size, NA and wavelength of the NSR-S204B KrF scanner. Used on the
lithography category page. Tier: cross-check.

**SEMIMARKET-S9200** — Legacy Semi, *Hitachi S-9200 CD-SEM* (listing).
<https://www.semimarket.com/item/hitachi-s-9200-cd-sem/42724>
Marketplace listing for the Hitachi S-9200 CD-SEM, a 200 mm-era in-line
CD metrology tool. Used on the lithography category page. Tier:
cross-check.

**TEL-ACT** — Tokyo Electron, *Coater/Developer ACT Series*, product
page. <https://www.tel.com/product/act.html> TEL product page for the
ACT coater/developer family. Used on the lithography category page.
Tier: cross-check.

**TEL-ACT8** — Semiconductor Online, *CLEAN TRACK ACT 8 System for
Spin-On Dielectric (SOD) Applications*.
<https://www.semiconductoronline.com/doc/clean-track-act-8-system-for-spin-on-dielectr-0001>
Introduction date and throughput of the CLEAN TRACK ACT 8. Used on the
lithography category page. Tier: cross-check.

##### University and course pages

**MACK-BASICS** — C. A. Mack, *The Basics of Microlithography*, online
tutorial. <https://www.lithoguru.com/scientist/lithobasics.html> An
online tutorial on the lithography process sequence and its physics.
Used on the lithography category page. Tier: high-level.

**MACK-COURSE** — C. A. Mack, *Online Micro- and Nanofabrication Course*
(CHE323 lecture materials).
<https://www.lithoguru.com/scientist/CHE323/course.html> University
lecture materials (CHE323) covering the whole lithography process. Used
on the lithography category page. Tier: deep dive.

#### Etch

##### Papers and review articles

**BELL-1997** — F. H. Bell and O. Joubert, "Polysilicon gate etching in
high density plasmas. V. Comparison between quantitative chemical
analysis of photoresist and oxide masked polysilicon gates etched in
HBr/Cl₂/O₂ plasmas", *Journal of Vacuum Science & Technology B*
**15**(1), 88–97 (1997). <https://doi.org/10.1116/1.589259> Chemical
analysis of HBr/Cl₂/O₂ gate-etch sidewalls under resist and oxide masks.
Used on the etch category page. Tier: deep dive.

**COBURN-1979B** — J. W. Coburn and H. F. Winters, "Plasma etching — A
discussion of mechanisms", *Journal of Vacuum Science and Technology*
**16**(2), 391–403 (1979). <https://doi.org/10.1116/1.569958> A
discussion of plasma etching mechanisms. Used on the etch category page.
Tier: deep dive.

**DONNELLY-2013** — V. M. Donnelly and A. Kornblit, "Plasma etching:
Yesterday, today, and tomorrow", *Journal of Vacuum Science & Technology
A* **31**(5), 050825 (2013). <https://doi.org/10.1116/1.4819316> A long
review of plasma etching from its origins to the present. Used on the
etch category page. Tier: deep dive.

**GOTTSCHO-1992** — R. A. Gottscho, C. W. Jurgensen and D. J. Vitkavage,
"Microscopic uniformity in plasma etching", *Journal of Vacuum Science &
Technology B* **10**(5), 2133–2147 (1992).
<https://doi.org/10.1116/1.586180> Microscopic uniformity:
aspect-ratio-dependent etching and its causes. Used on the etch category
page. Tier: deep dive.

**HASHIMOTO-1994** — K. Hashimoto, "Charge Damage Caused by Electron
Shading Effect", *Japanese Journal of Applied Physics* **33**(10R), 6013
(1994). <https://doi.org/10.1143/JJAP.33.6013> Electron-shading charging
damage during high-density plasma etching. Used on the etch category
page. Tier: deep dive.

**MOGAB-1977** — C. J. Mogab, "The Loading Effect in Plasma Etching",
*Journal of The Electrochemical Society* **124**(8), 1262–1268 (1977).
<https://doi.org/10.1149/1.2133542> The loading effect. Used on the etch
category page. Tier: deep dive.

**OEHRLEIN-1989** — G. S. Oehrlein, "Dry etching damage of silicon: A
review", *Materials Science and Engineering: B* **4**(1–4), 441–450
(1989). <https://doi.org/10.1016/0921-5107(89)90284-5> Review of
dry-etching damage to silicon. Used on the etch category page. Tier:
deep dive.

**OEHRLEIN-1998** — G. S. Oehrlein and Y. Kurogi, "Sidewall surface
chemistry in directional etching processes", *Materials Science and
Engineering: R* **24**(4), 153–183 (1998).
<https://doi.org/10.1016/S0927-796X(98)00016-3> Sidewall passivation
chemistry in directional etching. Used on the etch category page. Tier:
deep dive.

**POULSEN-1977** — R. G. Poulsen, "Plasma etching in integrated circuit
manufacture — A review", *Journal of Vacuum Science and Technology*
**14**(1), 266–274 (1977). <https://doi.org/10.1116/1.569137> An early
review of plasma etching in IC manufacture, including aluminium. Used on
the etch category page. Tier: deep dive.

**STANDAERT-1998** — T. E. F. M. Standaert, M. Schaepkens, N. R. Rueger,
P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "High density
fluorocarbon etching of silicon in an inductively coupled plasma:
Mechanism of etching through a thick steady state fluorocarbon layer",
*Journal of Vacuum Science & Technology A* **16**(1), 239–249 (1998).
<https://doi.org/10.1116/1.580978> Etching through a steady-state
fluorocarbon layer, the mechanism behind oxide-to-silicon selectivity.
Used on the etch category page. Tier: deep dive.

**TUDA-2001** — M. Tuda, K. Shintani and H. Ootera, "Profile evolution
during polysilicon gate etching with low-pressure high-density
Cl₂/HBr/O₂ plasma chemistries", *Journal of Vacuum Science & Technology
A* **19**(3), 711–717 (2001). <https://doi.org/10.1116/1.1365135>
Profile evolution during Cl₂/HBr/O₂ high-density poly gate etching. Used
on the etch category page. Tier: deep dive.

##### Patents

**PAT-DPS-AMAT** — G. Z. Yin, H. Hanawa, D. X. Ma and D. Olgado (Applied
Materials), *Plasma reactor with multi-section RF coil and isolated
conducting lid*, US 5,540,824 A, granted 1996-07-30.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5540824>
The multi-section RF coil and isolated lid of the DPS reactor. Used on
the etch category page. Tier: deep dive.

**PAT-ENDPOINT-TEL** — Tokyo Electron, *Method of forming a
semiconductor device using double endpoint detection*, US 6,376,262 B1,
granted 2002-04-23 (CN emission at 387 nm as the nitride etch endpoint
signal). <https://patents.google.com/patent/US6376262B1/en> CN emission
at 387 nm as the nitride etch endpoint signal. Label ↔ key: the same
patent is cited as `pat-cn-tel` on step 042 (PAT-CN-TEL). Used on the
etch category page. Tier: cross-check.

##### Vendor, regulatory, marketplace and press pages

**AKRION-GAMA** — C2MI, *Akrion GAMA acid bench*, equipment page.
<https://www.c2mi.ca/en/equipement/akrion-gama-acid-bench/> Facility
equipment page describing an Akrion GAMA automated acid wet bench, the
bench type SKW-01 lists. Used on the etch and strip category pages.
Tier: cross-check.

**LAM-10K** — Lam Research Corporation, Form 10-K for the fiscal year
ended 2003-06-29 (product line: TCP 9400PTX/DFM, 2300, Exelan).
<https://www.sec.gov/Archives/edgar/data/707549/000089161803004913/f93126e10vk.htm>
The TCP 9400PTX/DFM, 2300 and Exelan product line. Used on the etch
category page. Tier: cross-check.

**LAM-EXELAN** — Lam Research, *Lam Research Corporation Advances
Dielectric Etch Capabilities With Launch Of Exelan High Performance*,
press release, 2001-07-09.
<https://newsroom.lamresearch.com/2001-07-09-Lam-Research-Corporation-Advances-Dielectric-Etch-Capabilities-With-Launch-Of-Exelan-R-High-Performance>
Press release launching the Exelan dielectric etcher in 2001. Used on
the etch category page. Tier: cross-check.

#### Strip

##### Papers and review articles

**KERN-1970** — W. Kern and D. A. Puotinen, "Cleaning solutions based on
hydrogen peroxide for use in silicon semiconductor technology", *RCA
Review* **31**, 187–206 (1970). The original SC-1/SC-2 paper. Used on
the strip category page. Tier: cross-check.

##### Patents

**PAT-ASHER-AXCELIS** — A. F. Becknell, P. Hammar and D. Ferris (Axcelis
Technologies), *Apparatus and plasma ashing process for increasing
photoresist removal rate*, US 7,449,416 B2, granted 2008-11-11.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7449416>
An oxygen-free, nitrogen-free ashing chemistry for resist and post-etch
residue removal over low-k dielectrics. Used on the strip category page.
Tier: deep dive.

**PAT-ASHER-FUSION** — M. Kamarehi and J. E. Simpson (Fusion Systems),
*Plasma asher with microwave trap*, US 5,498,308 A, granted 1996-03-12.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5498308>
A downstream microwave asher design. Used on the strip category page.
Tier: deep dive.

##### Vendor, regulatory, marketplace and press pages

**GASONICS-AURA** — Allwin21, *Gasonics Aura 1000 Plasma Asher*
(specification summary; temperature 150–300 °C typical).
<https://allwin21.com/gasonics-aura-1000-plasma-asher-2/> Specification
summary for the Gasonics Aura 1000 downstream asher (150–300 °C
typical). Used on the strip category page. Tier: cross-check.

**GASONICS-L3510** — SemiStar Corp., *Gasonics L3510 plasma asher* (tool
description; platen temperature 100–300 °C).
<http://www.semistarcorp.com/product/gasonics-l3510-asher/> Tool
description for the Gasonics L3510 asher (platen temperature 100–300
°C). Used on the strip category page. Tier: cross-check.

##### University and course pages

**SNF-STRIP** — Stanford Nanofabrication Facility, *Downstream/Remote
Plasma Resist Removal*, equipment guide.
<https://snfguide.stanford.edu/guide/equipment/purpose/cleaning/resist-removal/dry-resist-removal/downstreamremote-plasma-resist-removal>
University equipment guide on downstream/remote-plasma resist removal.
Used on the strip category page. Tier: cross-check.

#### Implant

##### Papers and review articles

**CURRENT-2017** — M. I. Current, "Ion implantation of advanced silicon
devices: Past, present and future", *Materials Science in Semiconductor
Processing* **62**, 13–22 (2017).
<https://doi.org/10.1016/j.mssp.2016.10.045> Implantation for advanced
silicon devices, past to future. Used on the implant category page.
Tier: deep dive.

**DENNARD-1974** — R. H. Dennard, F. H. Gaensslen, H.-N. Yu, V. L.
Rideout, E. Bassous and A. R. LeBlanc, "Design of ion-implanted MOSFET's
with very small physical dimensions", *IEEE Journal of Solid-State
Circuits* **9**(5), 256–268 (1974).
<https://doi.org/10.1109/JSSC.1974.1050511> The scaling rules against
which the measured parameters are judged. Used on the implant and test
category pages. Tier: deep dive.

**GIBBONS-1968** — J. F. Gibbons, "Ion implantation in semiconductors —
Part I: Range distribution theory and experiments", *Proceedings of the
IEEE* **56**(3), 295–319 (1968).
<https://doi.org/10.1109/PROC.1968.6273> Range distributions in
semiconductors. Used on the implant category page. Tier: cross-check.

**LINDHARD-1963** — J. Lindhard, M. Scharff and H. E. Schiøtt, "Range
Concepts and Heavy Ion Ranges", *Matematisk-fysiske Meddelelser, Det
Kongelige Danske Videnskabernes Selskab* **33**(14), 1–42 (1963).
<https://gymarkiv.sdu.dk/MFM/kdvs/mfm%2030-39/mfm-33-14.pdf> The LSS
range theory. Used on the implant category page. Tier: cross-check.

##### Books and book chapters

**RYSSEL-1986** — H. Ryssel and I. Ruge, *Ion Implantation*, Wiley,
1986, ISBN 978-0-471-10311-0.
<https://openlibrary.org/isbn/9780471103110> The classic monograph on
range theory, damage, annealing and equipment. Used on the implant
category page. Tier: deep dive.

##### Theses

**HOESSINGER-2000** — A. Hössinger, *Simulation of Ion Implantation for
ULSI Technology*, PhD thesis, TU Wien, 2000.
<https://www.iue.tuwien.ac.at/phd/hoessinger/> Monte Carlo simulation of
implantation for ULSI technology. Used on the implant category page.
Tier: deep dive.

##### Patents

**PAT-SHOCKLEY** — W. Shockley, *Forming semiconductive devices by ionic
bombardment*, US 2,787,564 A, granted 1957.
<https://patents.google.com/patent/US2787564A/en> The original patent on
forming devices by ion bombardment. Used on the implant category page.
Tier: cross-check.

##### Vendor, regulatory, marketplace and press pages

**SEMIMARKET-VIISTA** — Legacy Semi, *Varian VIISta HC High Current
Implanter* (listing).
<https://www.semimarket.com/item/varian-viista-hc-high-current-implanter/94062>
Marketplace listing for the Varian VIISta HC single-wafer high-current
implanter. Used on the implant category page. Tier: cross-check.

**SRIM** — J. F. Ziegler, *SRIM — The Stopping and Range of Ions in
Matter* (software and documentation). <http://www.srim.org/> The SRIM
software and documentation for implant range and straggle calculations.
Used on the implant category page. Tier: cross-check.

#### Anneal

##### Papers and review articles

**AGARWAL-1999** — A. Agarwal, H.-J. Gossmann and A. T. Fiory, "Effect
of ramp rates during rapid thermal annealing of ion implanted boron for
formation of ultra-shallow junctions", *Journal of Electronic Materials*
**28**(12), 1333–1339 (1999).
<https://doi.org/10.1007/s11664-999-0118-7> The effect of RTA ramp rate
on boron ultra-shallow junctions, the case for spike anneals. Used on
the anneal category page. Tier: deep dive.

**CARTIER-1993** — E. Cartier, J. H. Stathis and D. A. Buchanan,
"Passivation and depassivation of silicon dangling bonds at the Si/SiO₂
interface by atomic hydrogen", *Applied Physics Letters* **63**(11),
1510–1512 (1993). <https://doi.org/10.1063/1.110758> Hydrogen
passivation and depassivation of interface dangling bonds. Used on the
anneal category page. Tier: deep dive.

**CSEPREGI-1978** — L. Csepregi, E. F. Kennedy, J. W. Mayer and T. W.
Sigmon, "Substrate-orientation dependence of the epitaxial regrowth rate
from Si-implanted amorphous Si", *Journal of Applied Physics* **49**(7),
3906–3911 (1978). <https://doi.org/10.1063/1.325397> Solid-phase
epitaxial regrowth rates of amorphised silicon versus orientation. Used
on the anneal category page. Tier: deep dive.

**MAEX-1993** — K. Maex, "Silicides for integrated circuits: TiSi₂ and
CoSi₂", *Materials Science and Engineering: R* **11**(2–3), vii–153
(1993). <https://doi.org/10.1016/0927-796X(93)90001-J> TiSi₂ and CoSi₂
formation, silicon consumption and the narrow-line effect. Used on the
anneal category page. Tier: cross-check.

**MANN-1994** — R. W. Mann and L. A. Clevenger, "The C49 to C54 Phase
Transformation in TiSi₂ Thin Films", *Journal of The Electrochemical
Society* **141**(5), 1347–1350 (1994).
<https://doi.org/10.1149/1.2054921> The C49-to-C54 TiSi₂ phase
transformation and its nucleation limit on narrow lines. Used on the
anneal category page. Tier: deep dive.

**REED-1988** — M. L. Reed and J. D. Plummer, "Chemistry of Si-SiO₂
interface trap annealing", *Journal of Applied Physics* **63**(12),
5776–5793 (1988). <https://doi.org/10.1063/1.340317> The chemistry of
Si/SiO₂ interface-trap annealing in hydrogen. Used on the anneal
category page. Tier: deep dive.

**SEDGWICK-1983** — T. O. Sedgwick, "Short Time Annealing", *Journal of
The Electrochemical Society* **130**(2), 484–493 (1983).
<https://doi.org/10.1149/1.2119736> An early review of short-time
annealing. Used on the anneal category page. Tier: deep dive.

##### Books and book chapters

**CAMPBELL-2013** — S. A. Campbell, *Fabrication Engineering at the
Micro- and Nanoscale*, 4th ed., Oxford University Press, 2013, ISBN
978-0-19-986122-4. <https://openlibrary.org/isbn/9780199861224> Textbook
chapters on thermal processing, implantation, deposition, etching and
lithography. Used on the anneal, deposition, etch, implant, lithography
and oxidation category pages. Tier: high-level.

**MURARKA-1983** — S. P. Murarka, "Formation", in *Silicides for VLSI
Applications*, Academic Press, 1983, pp. 99–131.
<https://doi.org/10.1016/b978-0-08-057056-3.50009-4> Ch. "Formation",
the classic text on silicide reaction kinetics. Used on the anneal
category page. Tier: deep dive.

**OSBURN-1993** — C. M. Osburn, "Silicides", in R. B. Fair (ed.), *Rapid
Thermal Processing: Science and Technology*, Academic Press, 1993, pp.
227–309. <https://doi.org/10.1016/b978-0-12-247690-7.50010-x> Chapter on
silicide formation by rapid thermal processing in Fair's *Rapid Thermal
Processing* (the book is TXT-10). Label ↔ key: this chapter is part of
the book listed as TXT-10. Used on the anneal category page. Tier:
cross-check.

**SZE-2012** — S. M. Sze and M. K. Lee, *Semiconductor Devices: Physics
and Technology*, 3rd ed., Wiley, 2012, ISBN 978-0-470-53794-7.
<https://www.wiley.com/en-us/Semiconductor+Devices%3A+Physics+and+Technology%2C+3rd+Edition-p-9780470537947>
Textbook coverage of oxidation, implantation and MOSFET characteristics
(ch. 6). Used on the anneal, implant, oxidation and test category pages.
Tier: high-level.

##### Vendor, regulatory, marketplace and press pages

**AG-10K** — AG Associates, Inc., Form 10-K for the fiscal year ended
1996-09-30, filed 1996-12-23 (Heatpulse 8108 first shipped October 1992;
125–200 mm).
<https://www.sec.gov/Archives/edgar/data/942124/000089161896003159/0000891618-96-003159.txt>
Heatpulse 8108 first shipped October 1992, 125–200 mm. Used on the
anneal and oxidation category pages. Tier: cross-check.

**AMAT-1997** — Applied Materials, Inc., *1997 Annual Report*.
<https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
Applied Materials' 1997 product line: DPS and MxP/eMxP+ etchers,
HDP-CVD, Mirra CMP and RTP chambers. Used on the anneal, cmp, deposition
and etch category pages. Tier: cross-check.

**AMAT-RTP** — EDN, *Applied dedicates RTP with Vantage*, 2002-09-23
(Applied Materials Radiance/Vantage RTP chambers).
<https://www.edn.com/applied-dedicates-rtp-with-vantage/> The
Radiance/Vantage RTP chamber family. Used on the anneal and oxidation
category pages. Tier: cross-check.

**ASM-VF** — ASM International, *Vertical furnace*, product page.
<https://www.asm.com/our-technology-products/vertical-furnace> ASM
product page for its vertical furnace family (A400/A412). Used on the
anneal and oxidation category pages. Tier: cross-check.

**PLASMATHERM-AG** — Plasma-Therm, *Product Spotlight: AG Heatpulse 8800
/ 8108 RTP*, blog post.
<https://blog.plasmatherm.com/product-spotlight-ag-heatpulse-8800-8108-rtp>
Vendor blog post on the AG Associates Heatpulse 8800 and 8108 RTP
systems, now supported by Plasma-Therm. Used on the anneal and oxidation
category pages. Tier: cross-check.

##### University and course pages

**OCW-6774** — MIT OpenCourseWare, *6.774 Physics of Microfabrication:
Front End Processing*, Fall 2004 (lecture notes on oxidation, diffusion,
implantation and annealing).
<https://ocw.mit.edu/courses/6-774-physics-of-microfabrication-front-end-processing-fall-2004/>
Lecture notes on oxidation, diffusion, implantation, damage and
annealing. Used on the anneal, implant, oxidation and substrate category
pages. Tier: deep dive.

#### CMP

##### Papers and review articles

**BOYD-1997** — J. M. Boyd and J. P. Ellul, "A One-Step Shallow Trench
Global Planarization Process Using Chemical Mechanical Polishing",
*Journal of The Electrochemical Society* **144**(5), 1838–1841 (1997).
<https://doi.org/10.1149/1.1837687> A one-step STI planarisation process
by CMP. Used on the cmp category page. Tier: deep dive.

**KAUFMAN-1991** — F. B. Kaufman, D. B. Thompson, R. E. Broadie, M. A.
Jaso et al., "Chemical-Mechanical Polishing for Fabricating Patterned W
Metal Features as Chip Interconnects", *Journal of The Electrochemical
Society* **138**(11), 3460–3465 (1991).
<https://doi.org/10.1149/1.2085434> Tungsten CMP by oxidation and
abrasion. Used on the cmp category page. Tier: cross-check.

**LUO-2001** — J. Luo and D. A. Dornfeld, "Material removal mechanism in
chemical mechanical polishing: theory and modeling", *IEEE Transactions
on Semiconductor Manufacturing* **14**(2), 112–133 (2001).
<https://doi.org/10.1109/66.920723> The abrasive-contact model of
material removal. Used on the cmp category page. Tier: deep dive.

**OUMA-2002** — D. O. Ouma, D. S. Boning, J. E. Chung, W. G. Easter et
al., "Characterization and modeling of oxide chemical-mechanical
polishing using planarization length and pattern density concepts",
*IEEE Transactions on Semiconductor Manufacturing* **15**(2), 232–244
(2002). <https://doi.org/10.1109/66.999598> Characterisation and
modelling of oxide CMP with planarisation length and density concepts.
Used on the cmp category page. Tier: deep dive.

**PRESTON-1927** — F. W. Preston, "The theory and design of plate glass
polishing machines", *Journal of the Society of Glass Technology*
**11**, 214–256 (1927). The Preston removal-rate law; no online copy is
known. Used on the cmp category page. Tier: cross-check.

**RUNNELS-1994** — S. R. Runnels and L. M. Eyman, "Tribology Analysis of
Chemical-Mechanical Polishing", *Journal of The Electrochemical Society*
**141**(6), 1698–1701 (1994). <https://doi.org/10.1149/1.2054985> A
tribology (fluid-film) analysis of the wafer–pad contact. Used on the
cmp category page. Tier: deep dive.

**STEIN-1999** — D. Stein, D. L. Hetherington and J. L. Cecchi,
"Investigation of the Kinetics of Tungsten Chemical Mechanical Polishing
in Potassium Iodate-Based Slurries: I. Role of Alumina and Potassium
Iodate", *Journal of The Electrochemical Society* **146**(1), 376–381
(1999). <https://doi.org/10.1149/1.1391617> Kinetics of tungsten CMP:
the roles of alumina abrasive and oxidiser. Used on the cmp category
page. Tier: deep dive.

**ZANTYE-2004** — P. B. Zantye, A. Kumar and A. K. Sikder, "Chemical
mechanical planarization for microelectronics applications", *Materials
Science and Engineering: R* **45**(3–6), 89–220 (2004).
<https://doi.org/10.1016/j.mser.2004.06.002> A long review of CMP for
microelectronics, including Preston deviations and slurry consumption.
Used on the cmp category page. Tier: deep dive.

##### Books and book chapters

**LI-2007** — Y. Li (ed.), *Microelectronic Applications of Chemical
Mechanical Planarization*, Wiley, 2007.
<https://doi.org/10.1002/9780470180907> Including a chapter on STI CMP.
Used on the cmp category page. Tier: deep dive.

##### Patents

**PAT-CMP-ENDPOINT-IBM** — N. E. Lustig, K. L. Saenger and H.-M. Tong
(IBM), *In-situ endpoint detection and process monitoring method and
apparatus for chemical-mechanical polishing*, US 5,433,651 A, granted
1995-07-18.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5433651>
In-situ optical endpoint detection through a window in the platen. Used
on the cmp category page. Tier: deep dive.

**PAT-CMP-IBM-1988** — M. M. Chow, J. E. Cronin, W. L. Guthrie, C. W.
Kaanta et al. (IBM), *Method for producing coplanar multi-level
metal/insulator films on a substrate and for forming patterned
conductive lines simultaneously with stud vias*, US 4,789,648 A, granted
1988-12-06. <https://patents.google.com/patent/US4789648A/en> Coplanar
multi-level metal/insulator films by polishing, with lines and stud vias
formed together. Used on the cmp category page. Tier: deep dive.

**PAT-CMP-IBM-1990** — K. D. Beyer et al. (IBM), *Chem-mech polishing
method for producing coplanar metal/insulator films on a substrate*, US
4,944,836 A, granted 1990.
<https://patents.google.com/patent/US4944836A/en> The foundational
metal/insulator CMP patent. Used on the cmp category page. Tier:
cross-check.

##### Vendor, regulatory, marketplace and press pages

**CHIPHISTORY-MIRRA** — Chip History Center, *The Mirra CMP System by
Applied Materials*.
<https://www.chiphistory.org/142-applied-materials-the-mirra-cmp-system>
The Mirra polisher in its historical context: integrated endpoint and
cleaning. Used on the cmp category page. Tier: cross-check.

**EBARA-FREX** — EBARA Precision Machinery Europe, *CMP Tools*
(F-REX200M2). <https://www.ebara-pm.eu/systems/cmp-tools/> The
F-REX200M2 200 mm CMP tool. Used on the cmp category page. Tier:
cross-check.

##### University and course pages

**OCW-6152** — MIT OpenCourseWare, *6.152J Micro/Nano Processing
Technology*, Fall 2005 (lecture notes on lithography, etching,
deposition and CMP).
<https://ocw.mit.edu/courses/6-152j-micro-nano-processing-technology-fall-2005/>
Lecture notes on lithography, resists, etching, deposition and CMP. Used
on the cmp, deposition, etch and lithography category pages. Tier: deep
dive.

#### Test

##### Papers and review articles

**BERGER-1972** — H. H. Berger, "Models for contacts to planar devices",
*Solid-State Electronics* **15**(2), 145–158 (1972).
<https://doi.org/10.1016/0038-1101(72)90048-2> Contact models, the
origin of the transmission-line method. Used on the test category page.
Tier: deep dive.

**BUEHLER-1978** — M. G. Buehler, S. D. Grant and W. R. Thurber, "Bridge
and van der Pauw Sheet Resistors for Characterizing the Line Width of
Conducting Layers", *Journal of The Electrochemical Society* **125**(4),
650–654 (1978). <https://doi.org/10.1149/1.2131517> Bridge and van der
Pauw resistors for line-width (electrical CD) measurement. Used on the
test category page. Tier: deep dive.

**HESS-1999** — C. Hess and L. H. Weiland, "Extraction of wafer-level
defect density distributions to improve yield prediction", *IEEE
Transactions on Semiconductor Manufacturing* **12**(2), 175–183 (1999).
<https://doi.org/10.1109/66.762875> Extracting defect-density
distributions from test structures for yield prediction. Used on the
test category page. Tier: deep dive.

**MALY-1990** — W. Maly, "Computer-aided design for VLSI circuit
manufacturability", *Proceedings of the IEEE* **78**(2), 356–392 (1990).
<https://doi.org/10.1109/5.52217> Design for manufacturability and the
role of test structures. Used on the test category page. Tier: deep
dive.

**ORTIZ-CONDE-2002** — A. Ortiz-Conde, F. J. García Sánchez, J. J. Liou,
A. Cerdeira, M. Estrada and Y. Yue, "A review of recent MOSFET threshold
voltage extraction methods", *Microelectronics Reliability* **42**(4–5),
583–596 (2002). <https://doi.org/10.1016/S0026-2714(02)00027-6> A review
of MOSFET threshold-voltage extraction methods. Used on the test
category page. Tier: deep dive.

**PROCTOR-1983** — S. J. Proctor, L. W. Linholm and J. A. Mazer, "Direct
measurements of interfacial contact resistance, end contact resistance,
and interfacial contact layer uniformity", *IEEE Transactions on
Electron Devices* **30**(11), 1535–1542 (1983).
<https://doi.org/10.1109/T-ED.1983.21334> Kelvin measurement of
interfacial contact resistance and its pitfalls. Used on the test
category page. Tier: deep dive.

**REEVES-1982** — G. K. Reeves and H. B. Harrison, "Obtaining the
specific contact resistance from transmission line model measurements",
*IEEE Electron Device Letters* **3**(5), 111–113 (1982).
<https://doi.org/10.1109/EDL.1982.25502> Extracting specific contact
resistance from TLM ladders. Used on the test category page. Tier: deep
dive.

**SMITS-1958** — F. M. Smits, "Measurement of Sheet Resistivities with
the Four-Point Probe", *Bell System Technical Journal* **37**(3),
711–718 (1958). <https://doi.org/10.1002/j.1538-7305.1958.tb03883.x>
Four-point-probe sheet resistivity and its correction factors. Used on
the test category page. Tier: deep dive.

**STAPPER-1983** — C. H. Stapper, "Modeling of Integrated Circuit Defect
Sensitivities", *IBM Journal of Research and Development* **27**(6),
549–557 (1983). <https://doi.org/10.1147/rd.276.0549> Defect-sensitivity
and critical-area yield modelling. Used on the test category page. Tier:
deep dive.

**VALDES-1954** — L. B. Valdes, "Resistivity Measurements on Germanium
for Transistors", *Proceedings of the IRE* **42**(2), 420–427 (1954).
<https://doi.org/10.1109/JRPROC.1954.274680> The original
four-point-probe resistivity measurement. Used on the test category
page. Tier: deep dive.

**VDP-1958** — L. J. van der Pauw, "A method of measuring specific
resistivity and Hall effect of discs of arbitrary shape", *Philips
Research Reports* **13**, 1–9 (1958); reprinted in S. M. Sze (ed.),
*Semiconductor Devices: Pioneering Papers*, World Scientific, 1991, pp.
174–182. <https://doi.org/10.1142/9789814503464_0017> The theorem behind
the four-contact sheet-resistance structure. Used on the test category
page. Tier: deep dive.

##### Books and book chapters

**CHENG-1999** — Y. Cheng and C. Hu, *MOSFET Modeling & BSIM3 User's
Guide*, Kluwer Academic, 1999. <https://doi.org/10.1007/b117400> How
parametric data become compact-model parameters. Used on the test
category page. Tier: deep dive.

**SCHRODER-2006** — D. K. Schroder, *Semiconductor Material and Device
Characterization*, 3rd ed., Wiley, 2006.
<https://doi.org/10.1002/0471749095> The reference text on resistivity,
contact, C–V and MOSFET measurements. Used on the test category page.
Tier: deep dive.

##### Standards and roadmaps

**ITRS-2001-MET** — International Technology Roadmap for Semiconductors,
*2001 Edition: Metrology*.
<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Met.pdf>
The test-structure and in-line metrology needs. Used on the test
category page. Tier: cross-check.

**ITRS-2001-TEST** — International Technology Roadmap for
Semiconductors, *2001 Edition: Test and Test Equipment*.
<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Test.pdf>
Wafer sort and tester requirements. Used on the test category page.
Tier: cross-check.

**ITRS-2001-YIELD** — International Technology Roadmap for
Semiconductors, *2001 Edition: Yield Enhancement*.
<https://www.semiconductors.org/wp-content/uploads/2018/08/2001YieldEnhance.pdf>
The yield-learning loop. Used on the test category page. Tier:
cross-check.

**SEMI-MF84** — SEMI MF84, *Test Method for Measuring Resistivity of
Silicon Wafers With an In-Line Four-Point Probe*, SEMI.
<https://store-us.semi.org/products/mf008400-semi-mf84-test-method-for-measuring-resistivity-of-silicon-wafers-with-an-in-line-four-point-probe>
The standard four-point-probe resistivity test method. Used on the test
category page. Tier: deep dive.

##### Vendor, regulatory, marketplace and press pages

**BRLTEST-4062** — BRL Test, *4062UX — Keysight / Agilent Parametric
Testers* (listing).
<https://www.brltest.com/index.php?main_page=product_info&products_id=7874>
Used-equipment listing for the HP/Agilent 4062UX parametric tester named
in SKW-01. Used on the test category page. Tier: cross-check.

**KEITHLEY-S600** — Keithley Instruments, *Series S600 Parametric Test
Systems*, data sheet.
<https://download.tek.com/datasheet/SeriesS600_DataSht.pdf> Data sheet
giving the S600 tester's intended uses. Used on the test category page.
Tier: cross-check.

**SEMIONLINE-S600** — Semiconductor Online, *S600 Series Parametric Test
Systems*.
<https://www.semiconductoronline.com/doc/s600-series-parametric-test-systems-0001>
Product description of the Keithley S600 parametric test systems. Used
on the test category page. Tier: cross-check.

### 8.11 Gate, poly-resistor and tip/halo module sources

Sources introduced by the writers of the polysilicon gate module
(steps 048–063) and the tip/halo module (steps 064–075) that had no
entry above. Each label on those pages is the key below in lower case;
the citation is the one given in the page footnote. Grouped by the
sub-module that first cited the source; an entry names every page that
uses it. None of these sources describes SkyWater unless the entry
says so.

#### Polysilicon gate film, gate pre-doping and poly re-oxidation (steps 048, 050 and 063)

**ARORA-1995** — N. D. Arora, E. Rios and C.-L. Huang, "Modeling the
polysilicon depletion effect and its impact on submicrometer CMOS
circuit performance", *IEEE Transactions on Electron Devices* **42**(5),
935–943 (1995). <https://doi.org/10.1109/16.381991> Models of the
poly-depletion effect and its circuit penalty. Used on steps 048 and
050. Tier: deep dive.

**BAUER-1998** — A. J. Bauer, P. Mayer, L. Frey, V. Häublein and H.
Ryssel, "Implantation of nitrogen into polysilicon to suppress boron
penetration through the gate oxide", *Proc. 1998 International
Conference on Ion Implantation Technology*, vol. 1, pp. 30–33.
<https://doi.org/10.1109/IIT.1999.812044> Nitrogen implantation into
poly to suppress boron penetration. Used on step 050. Tier: deep dive.

**CHAN-1987** — T. Y. Chan, A. T. Wu, P. K. Ko and C. Hu, "Effects of
the gate-to-drain/source overlap on MOSFET characteristics", *IEEE
Electron Device Letters* **8**(7), 326–328 (1987).
<https://doi.org/10.1109/EDL.1987.26647> The gate-to-drain overlap and
MOSFET characteristics. Used on step 063. Tier: deep dive.

**CHRISTEL-1981** — L. A. Christel, J. F. Gibbons and S. Mylroie,
"Recoil range distributions in multilayered targets", *Nuclear
Instruments and Methods* **182–183**, 187–198 (1981).
<https://doi.org/10.1016/0029-554X(81)90687-X> Recoil range
distributions in multilayer targets: knock-on through a screen oxide.
Used on step 063. Tier: deep dive.

**CLAASSEN-1982** — W. A. P. Claassen, J. Bloem, W. G. J. N. Valkenburg
and C. H. J. van den Brekel, "The deposition of silicon from silane in a
low-pressure hot-wall system", *Journal of Crystal Growth* **57**(2),
259–266 (1982). <https://doi.org/10.1016/0022-0248(82)90481-X> Silane
deposition kinetics in a low-pressure hot-wall reactor. Used on step
048. Tier: deep dive.

**DOYLE-1993** — B. S. Doyle and A. Philipossian, "p-channel hot-carrier
optimization of RNO gate dielectrics through the reoxidation step",
*IEEE Electron Device Letters* **14**(4), 161–163 (1993).
<https://doi.org/10.1109/55.215164> P-channel hot-carrier optimisation
through the re-oxidation step. Used on step 063. Tier: deep dive.

**HAO-1997** — M.-Y. Hao, D. Nayak and R. Rakkhit, "Impact of boron
penetration at p⁺-poly/gate oxide interface on deep-submicron device
reliability for dual-gate CMOS technologies", *IEEE Electron Device
Letters* **18**(5), 215–217 (1997). <https://doi.org/10.1109/55.568770>
Reliability impact of boron penetration in dual-gate CMOS. Used on step
050. Tier: deep dive.

**HARBEKE-1984** — G. Harbeke, L. Krausbauer, E. F. Steigmeier, A. E.
Widmer, H. F. Kappert and G. Neugebauer, "Growth and Physical Properties
of LPCVD Polycrystalline Silicon Films", *Journal of The Electrochemical
Society* **131**(3), 675–682 (1984). <https://doi.org/10.1149/1.2115672>
Growth and physical properties of LPCVD poly, including the amorphous
regime. Used on step 048. Tier: deep dive.

**HATALIS-1988** — M. K. Hatalis and D. W. Greve, "Large grain
polycrystalline silicon by low-temperature annealing of low-pressure
chemical vapor deposited amorphous silicon films", *Journal of Applied
Physics* **63**(7), 2260–2266 (1988). <https://doi.org/10.1063/1.341065>
Large-grain poly from low-temperature annealing of LPCVD a-Si. Used on
step 048. Tier: deep dive.

**HO-1979** — C. P. Ho and J. D. Plummer, "Si/SiO₂ Interface Oxidation
Kinetics: A Physical Model for the Influence of High Substrate Doping
Levels: I. Theory", *Journal of The Electrochemical Society* **126**(9),
1516–1522 (1979). <https://doi.org/10.1149/1.2129320> The physical model
of oxidation kinetics at high substrate doping. Used on step 063. Tier:
deep dive.

**HU-1985** — G. J. Hu and R. H. Bruce, "Design tradeoffs between
surface and buried-channel FET's", *IEEE Transactions on Electron
Devices* **32**(3), 584–588 (1985).
<https://doi.org/10.1109/T-ED.1985.21981> The design trade-offs between
surface- and buried-channel FETs, i.e. between p⁺ and n⁺ gates on PMOS.
Used on step 050. Tier: deep dive.

**IVERSON-1987** — R. B. Iverson and R. Reif, "Recrystallization of
amorphized polycrystalline silicon films on SiO₂: Temperature dependence
of the crystallization parameters", *Journal of Applied Physics*
**62**(5), 1675–1681 (1987). <https://doi.org/10.1063/1.339591> The
temperature dependence of solid-phase crystallisation kinetics of
silicon films on SiO₂. Used on step 048. Tier: deep dive.

**JOSHI-1992** — A. B. Joshi, G. Q. Lo, D. K. Shih and D.-L. Kwong,
"Effect of rapid thermal reoxidation on the electrical properties of
rapid thermally nitrided thin-gate oxides", *IEEE Transactions on
Electron Devices* **39**(4), 883–892 (1992).
<https://doi.org/10.1109/16.127479> Rapid thermal re-oxidation of
rapidly nitrided thin gate oxides. Used on step 063. Tier: deep dive.

**JOUBERT-1987** — P. Joubert, B. Loisel, Y. Chouan and L. Haji, "The
Effect of Low Pressure on the Structure of LPCVD Polycrystalline Silicon
Films", *Journal of The Electrochemical Society* **134**(10), 2541–2545
(1987). <https://doi.org/10.1149/1.2100239> How deposition pressure
changes the structure of LPCVD poly films. Used on step 048. Tier: deep
dive.

**KAMINS-1972** — T. I. Kamins, J. Manoliu and R. N. Tucker, "Diffusion
of Impurities in Polycrystalline Silicon", *Journal of Applied Physics*
**43**(1), 83–91 (1972). <https://doi.org/10.1063/1.1660842> Dopant
diffusion in poly, the mechanism that spreads the implant through the
film. Used on steps 048, 050 and 056. Tier: deep dive.

**KAMINS-1979** — T. I. Kamins, "Oxidation of Phosphorus-Doped Low
Pressure and Atmospheric Pressure CVD Polycrystalline-Silicon Films",
*Journal of The Electrochemical Society* **126**(5), 838–844 (1979).
<https://doi.org/10.1149/1.2129152> Oxidation of phosphorus-doped LPCVD
and APCVD poly films. Used on step 063. Tier: deep dive.

**KAMINS-1998** — T. Kamins, *Polycrystalline Silicon for Integrated
Circuits and Displays*, 2nd ed., Kluwer Academic, 1998.
<https://doi.org/10.1007/978-1-4615-5577-3> The monograph on deposition,
structure, doping, oxidation and electrical properties of poly films.
Used on steps 048, 050, 053, 055, 056 and 063. Tier: high-level / deep
dive.

**KINSBRON-1983** — E. Kinsbron, M. Sternheim and R. Knoell,
"Crystallization of amorphous silicon films during low pressure chemical
vapor deposition", *Applied Physics Letters* **42**(9), 835–837 (1983).
<https://doi.org/10.1063/1.94080> Crystallisation of a-Si films during
the deposition itself, the hazard that sets the deposition temperature
margin. Used on step 048. Tier: deep dive.

**KODA-1993** — M. Koda, Y. Shida, J. Kawaguchi and Y. Kaneko,
"Improving gate oxide integrity in p⁺ pMOSFET by using large grain size
polysilicon gate", *IEDM 1993 Technical Digest*, pp. 471–474.
<https://doi.org/10.1109/IEDM.1993.347308> Gate-oxide integrity improved
by large-grain poly gates. Used on step 048. Tier: deep dive.

**LAI-1998** — C. S. Lai, T. S. Chao, T. F. Lei, C. L. Lee, T. Y. Huang
and C. Y. Chang, "Improvement of Reliability of Metal-Oxide
Semiconductor Field-Effect Transistors with N₂O Nitrided Gate Oxide and
N₂O Polysilicon Gate Reoxidation", *Japanese Journal of Applied Physics*
**37**(10R), 5507 (1998). <https://doi.org/10.1143/JJAP.37.5507>
Reliability improvement from N₂O polysilicon-gate re-oxidation. Used on
step 063. Tier: deep dive.

**LU-1989** — C.-Y. Lu, J. M. Sung, H. C. Kirsch, S. J. Hillenius, T. E.
Smith and L. Manchanda, "Anomalous C-V characteristics of implanted poly
MOS structure in n⁺/p⁺ dual-gate CMOS technology", *IEEE Electron Device
Letters* **10**(5), 192–194 (1989). <https://doi.org/10.1109/55.31717>
Anomalous C–V of implanted-poly gates in an n⁺/p⁺ dual-gate technology,
showing what incomplete gate doping looks like electrically. Used on
step 050. Tier: deep dive.

**MANDURAH-1981** — M. M. Mandurah, K. C. Saraswat and T. I. Kamins, "A
model for conduction in polycrystalline silicon — Part I: Theory", *IEEE
Transactions on Electron Devices* **28**(10), 1163–1171 (1981).
<https://doi.org/10.1109/T-ED.1981.20504> Grain-boundary trapping and
dopant segregation in doped poly, the model behind poly resistor and
gate doping. Used on steps 048, 050, 052, 053 and 056. Tier: deep dive.

**MEYERSON-1984** — B. S. Meyerson and W. Olbricht, "Phosphorus-Doped
Polycrystalline Silicon via LPCVD: I. Process Characterization",
*Journal of The Electrochemical Society* **131**(10), 2361–2365 (1984).
<https://doi.org/10.1149/1.2115258> In-situ phosphorus doping of LPCVD
poly and its effect on deposition rate, the alternative to an implanted
gate. Used on step 048. Tier: deep dive.

**PAN-1994** — Y. Pan, K. K. Ng and V. Kwong, "Comparison of gate-edge
effects on the hot-carrier induced degradation of LDD N- and P-channel
MOSFETs", *Solid-State Electronics* **37**(1), 77–82 (1994).
<https://doi.org/10.1016/0038-1101(94)90108-2> Gate-edge effects on
hot-carrier degradation of LDD devices. Used on step 063. Tier: deep
dive.

**RIOS-1994** — R. Rios, N. D. Arora and C.-L. Huang, "An analytic
polysilicon depletion effect model for MOSFETs", *IEEE Electron Device
Letters* **15**(4), 129–131 (1994). <https://doi.org/10.1109/55.285407>
Models of the poly-depletion effect and its circuit penalty. Used on
step 050. Tier: deep dive.

**SARASWAT-1982** — K. C. Saraswat and H. Singh, "Thermal Oxidation of
Heavily Phosphorus-Doped Thin Films of Polycrystalline Silicon",
*Journal of The Electrochemical Society* **129**(10), 2321–2326 (1982).
<https://doi.org/10.1149/1.2123503> Oxidation of heavily
phosphorus-doped thin poly films, the n⁺ gate sidewall case. Used on
step 063. Tier: deep dive.

**SCHUEGRAF-1993** — K. F. Schuegraf, C. C. King and C. Hu, "Impact of
polysilicon depletion in thin oxide MOS technology", *1993 International
Symposium on VLSI Technology, Systems, and Applications (VLSI-TSA)*, pp.
86–90. <https://doi.org/10.1109/VTSA.1993.263633> The impact of poly
depletion in thin-oxide MOS technology. Used on step 050. Tier: deep
dive.

**SUNAMI-1978** — H. Sunami, "Thermal Oxidation of Phosphorus-Doped
Polycrystalline Silicon in Wet Oxygen", *Journal of The Electrochemical
Society* **125**(6), 892–897 (1978). <https://doi.org/10.1149/1.2131586>
Thermal oxidation of phosphorus-doped poly in wet oxygen. Used on step
063. Tier: deep dive.

**SUNG-1989** — J. M. Sung, C. Y. Lu, M. L. Chen, S. J. Hillenius, W. S.
Lindenberger, L. Manchanda, T. E. Smith and S. J. Wang, "Fluorine effect
on boron diffusion of p⁺ gate devices (MOSFETs)", *IEDM 1989 Technical
Digest*, pp. 447–450. <https://doi.org/10.1109/IEDM.1989.74318> The
fluorine effect on boron diffusion in p⁺-gate devices. Used on step 050.
Tier: deep dive.

**VOUTSAS-1992** — A. T. Voutsas and M. K. Hatalis, "Structure of
As-Deposited LPCVD Silicon Films at Low Deposition Temperatures and
Pressures", *Journal of The Electrochemical Society* **139**(9),
2659–2665 (1992). <https://doi.org/10.1149/1.2221280> The structure of
as-deposited LPCVD films at low temperature and pressure: where the
amorphous/polycrystalline boundary lies. Used on step 048. Tier: deep
dive.

**WIKI-ASI** — Wikipedia, *Amorphous silicon*.
<https://en.wikipedia.org/wiki/Amorphous_silicon> Amorphous silicon, the
form in which the gate film is deposited. Used on step 048. Tier:
high-level.

**WIKI-POLYDEP** — Wikipedia, *Polysilicon depletion effect*.
<https://en.wikipedia.org/wiki/Polysilicon_depletion_effect> The
polysilicon depletion effect that the gate pre-dope is chosen to
suppress. Used on step 050. Tier: high-level.

**WIKI-SILANE** — Wikipedia, *Silane*.
<https://en.wikipedia.org/wiki/Silane> Silane, the poly deposition
precursor, and its hazards. Used on step 048. Tier: high-level.

**WONG-1988** — C. Y. Wong, J. Y. Sun, Y. Taur, C. S. Oh, R. Angelucci
and B. Davari, "Doping of n⁺ and p⁺ polysilicon in a dual-gate CMOS
process", *IEDM 1988 Technical Digest*, pp. 238–241.
<https://doi.org/10.1109/IEDM.1988.32800> Doping n⁺ and p⁺ poly in a
dual-gate CMOS process, the alternative to a single pre-dope. Used on
steps 050 and 058. Tier: deep dive.

**WU-1993** — S. L. Wu, C. L. Lee and T. F. Lei, "Suppression of boron
penetration into an ultra-thin gate oxide (≤7 nm) by using a
stacked-amorphous-silicon (SAS) film", *IEDM 1993 Technical Digest*, pp.
329–332. <https://doi.org/10.1109/IEDM.1993.347341> The
stacked-amorphous-silicon gate, an alternative to a single poly film.
Used on step 048. Tier: deep dive.

#### Poly resistor implants (steps 049 and 052–056)

**AMEMIYA-1979** — Y. Amemiya, T. Ono and K. Kato, "Electrical trimming
of heavily doped polycrystalline silicon resistors", *IEEE Transactions
on Electron Devices* **26**(11), 1738–1742 (1979).
<https://doi.org/10.1109/T-ED.1979.19679> Electrical trimming of heavily
doped poly resistors. Used on step 049. Tier: deep dive.

**ASHUAH-2009** — I. Ashuah, E. N. Shauly and Y. Shacham-Diamand,
"Improvement of Temperature Coefficient of Resistance by Co-Implantation
of Argon or Xenon or Fluorine in Boron Implanted Polysilicon Resistors",
*IEEE Transactions on Semiconductor Manufacturing* **22**(2), 305–316
(2009). <https://doi.org/10.1109/TSM.2009.2017655> Improving the TCR of
boron-implanted poly resistors by co-implantation, a modern example of
resistor-implant engineering. Used on steps 052, 053 and 056. Tier: deep
dive.

**CHEN-2000** — C.-H. Chen, Y.-K. Fang, M.-H. Kuo, Y.-L. Hsu and S.-L.
Hsu, "A DC current stress method to improve the voltage coefficient of
resistance of the polysilicon resistor in high voltage CMOS technology",
*Solid-State Electronics* **44**(10), 1743–1746 (2000).
<https://doi.org/10.1016/S0038-1101(00)00138-6> The voltage coefficient
of poly resistors in a high-voltage CMOS technology. Used on steps 052,
053, 055 and 056. Tier: deep dive.

**KAMINS-1971** — T. I. Kamins, "Hall Mobility in Chemically Deposited
Polycrystalline Silicon", *Journal of Applied Physics* **42**(11),
4357–4365 (1971). <https://doi.org/10.1063/1.1659780> Hall mobility in
deposited poly, the early data behind the models. Used on step 049.
Tier: deep dive.

**KATO-1996** — K. Kato and T. Ono, "Change in Temperature Coefficient
of Resistance of Heavily Doped Polysilicon Resistors Caused by
Electrical Trimming", *Japanese Journal of Applied Physics* **35**(8R),
4209 (1996). <https://doi.org/10.1143/JJAP.35.4209> The temperature
coefficient of heavily doped poly resistors and how processing changes
it. Used on steps 052 and 055. Tier: deep dive.

**LANE-1989** — W. A. Lane and G. T. Wrixon, "The design of thin-film
polysilicon resistors for analog IC applications", *IEEE Transactions on
Electron Devices* **36**(4), 738–744 (1989).
<https://doi.org/10.1109/16.22479> The design of thin-film poly
resistors for analogue ICs. Used on steps 049, 053 and 056. Tier: deep
dive.

**LU-1981** — N. C.-C. Lu, L. Gerzberg, C.-Y. Lu and J. D. Meindl,
"Modeling and optimization of monolithic polycrystalline silicon
resistors", *IEEE Transactions on Electron Devices* **28**(7), 818–830
(1981). <https://doi.org/10.1109/T-ED.1981.20437> Modelling and
optimisation of monolithic poly resistors: why the doping level sets
everything. Used on steps 049, 053, 055 and 056. Tier: deep dive.

**LU-1982** — N. C.-C. Lu, L. Gerzberg and J. D. Meindl, "Scaling
limitations of monolithic polycrystalline-silicon resistors in VLSI
static RAM's and logic", *IEEE Transactions on Electron Devices*
**29**(4), 682–690 (1982). <https://doi.org/10.1109/T-ED.1982.20762>
Scaling limits of poly resistors in SRAM and logic, including the
end-resistance problem. Used on steps 052 and 055. Tier: deep dive.

**ODWYER-2009** — T. G. O'Dwyer and M. P. Kennedy, "Comparison of
resistor matching performance of polysilicon films in a CMOS process",
*2009 Ph.D. Research in Microelectronics and Electronics (PRIME)*, pp.
80–83. <https://doi.org/10.1109/RME.2009.5201322> Matching performance
of different poly resistor films in a CMOS process. Used on steps 049
and 052. Tier: deep dive.

**SETO-1975** — J. Y. W. Seto, "The electrical properties of
polycrystalline silicon films", *Journal of Applied Physics* **46**(12),
5247–5254 (1975). <https://doi.org/10.1063/1.321593> The grain-boundary
trapping theory of poly conduction that explains the steep dependence of
resistance on dose. Used on steps 049, 052, 053, 055 and 056. Tier: deep
dive.

**TSANG-2014** — Y. Tsang, R. Shiono, G. Pfeffer and S. Kwan,
"Characterization and Understanding of High Valued Polysilicon Resistor
Resistance Variation Across a Resistor Bank With Parallel Resistor
Fingers", *IEEE Transactions on Semiconductor Manufacturing* **27**(2),
294–300 (2014). <https://doi.org/10.1109/TSM.2014.2311375> Resistance
variation across banks of high-value poly resistors, a modern
manufacturing view. Used on steps 049, 052, 055 and 056. Tier: deep
dive.

**UPRETI-1991** — N. K. Upreti and S. Singh, "Grain boundary effect on
the electrical properties of boron-doped polysilicon films", *Bulletin
of Materials Science* **14**(6), 1331–1341 (1991).
<https://doi.org/10.1007/BF02823239> Grain-boundary effects on the
electrical properties of boron-doped poly films. Used on steps 052, 053
and 055. Tier: deep dive.

**WRIGHT-2010** — S. W. Wright, C. P. Judge, M. J. Lee, D. F. Bowers, M.
Dunbar and C. D. Wilson, "High sheet resistance, low temperature
coefficient of resistance resistor films for integrated circuits",
*Journal of Vacuum Science & Technology B* **28**(4), 834–840 (2010).
<https://doi.org/10.1116/1.3466531> High-sheet-resistance, low-TCR
resistor films for ICs. Used on steps 049, 053, 055 and 056. Tier: deep
dive.

#### Resist strips after the poly and tip implants (steps 051, 054, 057, 067, 070 and 074)

**LEE-KT-1999** — K. T. Lee, "Etch Rate of Silicon and Silicon Dioxide
in Ammonia-Peroxide Solutions Measured by Quartz Crystal Microbalance
Technique", *Electrochemical and Solid-State Letters* **2**(4), 172
(1999). <https://doi.org/10.1149/1.1390773> Etch rates of silicon and
SiO₂ in ammonia–peroxide (SC-1) solutions, the constraint on cleaning a
bare poly film. Used on steps 051, 054 and 057. Tier: deep dive.

**PRITCHARD-1998** — D. C. Pritchard, W. Montgomery, J. P. Kimball and
J. A. Albelo, "Photoresist performance evaluation of implant resist
systems", *Proc. SPIE* **3333**, Advances in Resist Technology and
Processing XV, 1337 (1998). <https://doi.org/10.1117/12.312367>
Performance evaluation of implant resist systems, including post-implant
strippability. Used on step 051. Tier: deep dive.

**RUBIN-2000** — L. Rubin, D. Whiteside, C. Norton, A. Stevenson and C.
Ukah, "Improved photoresist integrity by UV photostabilization for high
dose, high energy ion implants", *Proc. 2000 International Conference on
Ion Implantation Technology*, pp. 817–820.
<https://doi.org/10.1109/IIT.2000.924279> UV photostabilisation of
resist before high-dose implants, the implant-side remedy for resist
popping. Used on step 067. Tier: deep dive.

**YEGNASUBRAMANIAN-1992** — S. Yegnasubramanian, C. W. Draper and C. W.
Pearce, "Tem Investigation of Implanted Photoresist Residues Remaining
After Oxygen Plasma Ashing", *MRS Online Proceedings Library* **265**,
295–300 (1992). <https://doi.org/10.1557/PROC-265-295> TEM of the
implanted-resist residues left after oxygen-plasma ashing. Used on step
067. Tier: deep dive.

#### Gate hard mask, ARC, lithography and etch (steps 058, 059, 061 and 062)

**ASENOV-2003** — A. Asenov, S. Kaya and A. R. Brown, "Intrinsic
parameter fluctuations in decananometer MOSFETs introduced by gate line
edge roughness", *IEEE Transactions on Electron Devices* **50**(5),
1254–1260 (2003). <https://doi.org/10.1109/TED.2003.813457> Device
parameter fluctuations caused by gate line-edge roughness. Used on step
061. Tier: deep dive.

**AUSSCHNITT-1999** — C. P. Ausschnitt, "Distinguishing dose from
defocus for in-line lithography control", *Proc. SPIE* **3677**,
Metrology, Inspection, and Process Control for Microlithography XIII,
140 (1999). <https://doi.org/10.1117/12.350800> Separating dose from
defocus for in-line lithography control. Used on step 061. Tier: deep
dive.

**BECKER-1987** — F. S. Becker, D. Pawlik, H. Anzinger and A. Spitzer,
"Low-pressure deposition of high-quality SiO₂ films by pyrolysis of
tetraethylorthosilicate", *Journal of Vacuum Science & Technology B*
**5**(6), 1555–1563 (1987). <https://doi.org/10.1116/1.583673>
Low-pressure TEOS oxide deposition. Used on step 059. Tier: deep dive.

**BELL-1996** — F. H. Bell and O. Joubert, "Polysilicon gate etching in
high density plasmas. III. X-ray photoelectron spectroscopy
investigation of sidewall passivation of silicon trenches using an oxide
hard mask", *Journal of Vacuum Science & Technology B* **14**(4),
2493–2499 (1996). <https://doi.org/10.1116/1.588758> Sidewall
passivation of silicon etched with an oxide hard mask. Used on steps 059
and 062. Tier: deep dive.

**BRUNNER-1997** — T. A. Brunner, "Impact of lens aberrations on optical
lithography", *IBM Journal of Research and Development* **41**(1.2),
57–67 (1997). <https://doi.org/10.1147/rd.411.0057> How lens aberrations
show up as CD errors at low k₁. Used on step 061. Tier: deep dive.

**CHAPPLE-SOKOL-1989** — J. D. Chapple-Sokol, E. Tierney and J. Batey,
"RF Power Dependence of the Material Properties of PECVD Silicon
Dioxide", *MRS Proceedings* **165** (1989).
<https://doi.org/10.1557/PROC-165-113> RF-power dependence of PECVD
oxide properties. Used on step 059. Tier: deep dive.

**CLAASSEN-1985** — W. A. P. Claassen, W. G. J. N. Valkenburg, M. F. C.
Willemsen and W. M. v. d. Wijgert, "Influence of Deposition Temperature,
Gas Pressure, Gas Phase Composition, and RF Frequency on Composition and
Mechanical Stress of Plasma Silicon Nitride Layers", *Journal of The
Electrochemical Society* **132**(4), 893–898 (1985).
<https://doi.org/10.1149/1.2113980> PECVD nitride composition and stress
versus deposition conditions. Used on step 058. Tier: deep dive.

**CUNGE-2002** — G. Cunge, R. L. Inglebert, O. Joubert, L. Vallier and
N. Sadeghi, "Ion flux composition in HBr/Cl₂/O₂ and HBr/Cl₂/O₂/CF₄
chemistries during silicon etching in industrial high-density plasmas",
*Journal of Vacuum Science & Technology B* **20**(5), 2137–2148 (2002).
<https://doi.org/10.1116/1.1511219> Ion flux composition in industrial
HBr/Cl₂/O₂ high-density plasmas. Used on step 062. Tier: deep dive.

**CZECH-1993** — G. Czech, L. Mader, K. H. Küsters, P. Küppers and A.
Gutmann, "Reduction of linewidth variation for the gate conductor level
by lithography based on a new antireflective layer", *Microelectronic
Engineering* **21**(1–4), 51–56 (1993).
<https://doi.org/10.1016/0167-9317(93)90025-Z> Linewidth-variation
reduction at the gate level with a new ARC. Used on step 058. Tier: deep
dive.

**DESVOIVRES-2000** — L. Desvoivres, L. Vallier and O. Joubert, "Sub-0.1
μm gate etch processes: Towards some limitations of the plasma
technology?", *Journal of Vacuum Science & Technology B* **18**(1),
156–165 (2000). <https://doi.org/10.1116/1.591168> Sub-0.1 µm gate etch
and the limits of the technology. Used on steps 058 and 062. Tier: deep
dive.

**DETTER-2003** — X. Detter, R. Palla, I. Thomas-Boutherin, E. Pargon,
G. Cunge, O. Joubert and L. Vallier, "Impact of chemistry on profile
control of resist masked silicon gates etched in high density
halogen-based plasmas", *Journal of Vacuum Science & Technology B*
**21**(5), 2174–2183 (2003). <https://doi.org/10.1116/1.1612932>
Chemistry and profile control of resist-masked gates. Used on step 062.
Tier: deep dive.

**DIJKSTRA-1993** — H. J. Dijkstra and C. A. H. Juffermans,
"Optimization of antireflection layers for deep-UV lithography", *Proc.
SPIE* **1927**, Optical/Laser Microlithography VI, 275 (1993).
<https://doi.org/10.1117/12.150432> Optimisation of anti-reflection
layers for deep-UV. Used on steps 058 and 059. Tier: deep dive.

**GALLATIN-2005** — G. M. Gallatin, "Resist blur and line edge
roughness", *Proc. SPIE* **5754**, Optical Microlithography XVIII, 4
(2005). <https://doi.org/10.1117/12.607233> Resist blur and line-edge
roughness. Used on step 061. Tier: deep dive.

**GOLDFARB-2004** — D. L. Goldfarb, A. P. Mahorowala, G. M. Gallatin, K.
E. Petrillo, K. Temple, M. Angelopoulos, S. Rasgon, H. H. Sawin, S. D.
Allen, M. C. Lawson and R. W. Kwong, "Effect of thin-film imaging on
line edge roughness transfer to underlayers during etch processes",
*Journal of Vacuum Science & Technology B* **22**(2), 647–653 (2004).
<https://doi.org/10.1116/1.1667513> Line-edge roughness transfer from
resist to the underlying layers during etch. Used on step 062. Tier:
deep dive.

**HE-1998** — Q. He, W. W. Lee, M. A. Hanratty, D. Rogers, G. Xing, A.
Singh and E. Zielinski, "Inorganic antireflective coating process for
deep-UV lithography", *Proc. SPIE* **3334**, Optical Microlithography
XI, 337 (1998). <https://doi.org/10.1117/12.310763> An inorganic ARC
process for deep-UV in production. Used on steps 058 and 059. Tier: deep
dive.

**HINSBERG-1992** — W. D. Hinsberg, S. A. MacDonald, N. J. Clecak and C.
D. Snyder, "Quantitation of airborne chemical contamination of
chemically amplified resists using radiochemical analysis", *Proc. SPIE*
**1672**, Advances in Resist Technology and Processing IX, 24 (1992).
<https://doi.org/10.1117/12.59723> Quantitative measurement of airborne
base contamination of chemically amplified resists. Used on step 059.
Tier: deep dive.

**HSU-2004** — L. Hsu, "An optical interference model to analyze
interferometry endpoint signal for process control of polysilicon gate
etch", *2004 Semiconductor Manufacturing Technology Workshop
Proceedings*, pp. 111–114. <https://doi.org/10.1109/SMTW.2004.1393740>
An interferometry endpoint model for poly gate etch process control.
Used on step 062. Tier: deep dive.

**JOUBERT-2003** — O. Joubert, E. Pargon, J. Foucher, X. Detter, G.
Cunge and L. Vallier, "Nanometer scale linewidth control during etching
of polysilicon gates in high-density plasmas", *Microelectronic
Engineering* **69**(2–4), 350–357 (2003).
<https://doi.org/10.1016/S0167-9317(03)00321-6> Nanometre-scale
linewidth control in poly gate etching. Used on step 062. Tier: deep
dive.

**KANG-2007** — S. J. Kang, Y. H. Joung and S. Y. Mun, "New Gate CD
Control Technology Using CF₄ Plasma Treatment Following HBr/O₂ Plasma
Treatment Step in Gate Etch Process Using Organic BARC", *IEEE
Transactions on Semiconductor Manufacturing* **20**(2), 150–153 (2007).
<https://doi.org/10.1109/TSM.2007.895206> Gate CD control by plasma
treatment of an organic BARC in the gate etch. Used on steps 061 and
062. Tier: deep dive.

**KIM-2007** — D.-K. Kim, Y. K. Kim and H. Lee, "A study of the role of
HBr and oxygen on the etch selectivity and the post-etch profile in a
polysilicon/oxide etch using HBr/O₂ based high density plasma for
advanced DRAMs", *Materials Science in Semiconductor Processing*
**10**(1), 41–48 (2007). <https://doi.org/10.1016/j.mssp.2006.08.027>
HBr and O₂ in the poly/oxide selectivity and post-etch profile of an
HBr/O₂ over-etch. Used on step 062. Tier: deep dive.

**KRAFT-1995** — R. Kraft and S. Krishnan, "Gate oxide loss at the
periphery of a metal–oxide–semiconductor field-effect transistor
resulting from a polysilicon gate etch with a helicon etch tool",
*Journal of Vacuum Science & Technology B* **13**(6), 2226–2229 (1995).
<https://doi.org/10.1116/1.588053> Gate oxide loss at the MOSFET
periphery after the poly etch, the damage the poly re-oxidation repairs.
Used on steps 062 and 063. Tier: deep dive.

**KRISHNAN-1995** — S. Krishnan, S. Aur, G. Wilhite and R. Rajgopal,
"High density plasma etch induced damage to thin gate oxide", *IEDM 1995
Technical Digest*, pp. 315–318.
<https://doi.org/10.1109/IEDM.1995.499204> High-density-plasma etch
damage to thin gate oxide. Used on step 062. Tier: deep dive.

**LIN-2000** — Q. Lin, R. Sooriyakumaran and W.-S. Huang, "Toward
controlled resist line-edge roughness: material origin of line-edge
roughness in chemically amplified positive-tone resists", *Proc. SPIE*
**3999**, Advances in Resist Technology and Processing XVII, 230 (2000).
<https://doi.org/10.1117/12.388307> The material origin of line-edge
roughness in CARs. Used on step 061. Tier: deep dive.

**LIN-2001** — C. H. Lin, H. L. Chen and L. A. Wang, "A study on
adhesion and footing issues of HMDSO films as bottom antireflective
coating for deep UV lithographies", *Microelectronic Engineering*
**57–58**, 555–561 (2001).
<https://doi.org/10.1016/S0167-9317(01)00501-9> Adhesion and footing of
a plasma-deposited BARC for deep-UV. Used on step 059. Tier: deep dive.

**MOGAB-1980** — C. J. Mogab and H. J. Levinstein, "Anisotropic plasma
etching of polysilicon", *Journal of Vacuum Science and Technology*
**17**(3), 721–730 (1980). <https://doi.org/10.1116/1.570549>
Anisotropic plasma etching of polysilicon, the classic starting point
for gate etching. Used on step 062. Tier: deep dive.

**MONTGOMERY-2005** — P. K. Montgomery, R. Peters, C. Garza, J. Cobb, B.
Darlington, C. Parker, S. Filipiak and D. Babbitt, "Reduction of line
edge roughness and post resist trim pattern collapse for sub 60 nm gate
patterns using gas-phase resist fluorination", *Proc. SPIE* **5753**,
Advances in Resist Technology and Processing XXII, 1024 (2005).
<https://doi.org/10.1117/12.600785> Line-edge roughness and pattern
collapse after resist trimming for sub-60 nm gates. Used on step 061.
Tier: deep dive.

**NOGUCHI-1997** — K. Noguchi, K. Tokashiki, T. Horiuchi and H.
Miyamoto, "Reliability of thin gate oxide under plasma charging caused
by antenna topography-dependent electron shading effect", *IEDM 1997
Technical Digest*, pp. 441–444.
<https://doi.org/10.1109/IEDM.1997.650419> Thin-oxide reliability under
electron-shading charging during the poly etch. Used on step 062. Tier:
deep dive.

**OGAWA-1993** — T. Ogawa, M. Kimura, T. Gocho, Y. Tomo and T. Tsumori,
"Practical resolution enhancement effect by new complete antireflective
layer in KrF excimer laser lithography", *Proc. SPIE* **1927**,
Optical/Laser Microlithography VI, 263 (1993).
<https://doi.org/10.1117/12.150431> The "complete antireflective layer"
for KrF lithography, the origin of inorganic DARC. Used on step 058.
Tier: deep dive.

**OGRYZLO-1988** — E. A. Ogryzlo, D. L. Flamm, D. E. Ibbotson and J. A.
Mucha, "The etching of doped polycrystalline silicon by molecular
chlorine", *Journal of Applied Physics* **64**(11), 6510–6514 (1988).
<https://doi.org/10.1063/1.342070> Doping dependence of poly and silicon
etch rates in chlorine. Used on step 062. Tier: deep dive.

**OGRYZLO-1990** — E. A. Ogryzlo, D. E. Ibbotson, D. L. Flamm and J. A.
Mucha, "Doping and crystallographic effects in Cl-atom etching of
silicon", *Journal of Applied Physics* **67**(6), 3115–3120 (1990).
<https://doi.org/10.1063/1.345388> Doping dependence of poly and silicon
etch rates in chlorine. Used on step 062. Tier: deep dive.

**ORSHANSKY-2004** — M. Orshansky, L. Milor and C. Hu, "Characterization
of Spatial Intrafield Gate CD Variability, Its Impact on Circuit
Performance, and Spatial Mask-Level Correction", *IEEE Transactions on
Semiconductor Manufacturing* **17**(1), 2–11 (2004).
<https://doi.org/10.1109/TSM.2003.822735> Spatial intrafield gate-CD
variability, its circuit impact and mask-level correction. Used on step
061. Tier: deep dive.

**PAT-OXIME-AMD** — D. K. Foote and S. Gupta (Advanced Micro Devices),
*Silicon oxime film*, US 5,710,067 A, filed 1995-06-07, granted
1998-01-20. <https://patents.google.com/patent/US5710067A/en> A
silicon-oxynitride-type dielectric ARC. Used on step 058. Tier:
cross-check / deep dive.

**SMITH-1990** — D. L. Smith, A. S. Alimonda, C.-C. Chen, S. E. Ready
and B. Wacker, "Mechanism of SiNₓHᵧ Deposition from NH₃-SiH₄ Plasma",
*Journal of The Electrochemical Society* **137**(2), 614–623 (1990).
<https://doi.org/10.1149/1.2086517> Mechanism of PECVD SiNₓHᵧ deposition
from NH₃/SiH₄. Used on step 058. Tier: deep dive.

**STURTEVANT-1994** — J. L. Sturtevant, S. J. Holmes, S. E. Knight, D.
Poley, P. A. Rabidoux, L. K. Somerville, T. L. McDevitt and A. Stamper,
"Substrate contamination effects in the processing of chemically
amplified DUV photoresists", *Proc. SPIE* **2197**, Optical/Laser
Microlithography VII, 770–780 (1994).
<https://doi.org/10.1117/12.175469> Substrate contamination effects on
chemically amplified DUV resists, the case for an inert cap under the
resist. Used on step 059. Tier: deep dive.

**VALLIER-2003** — L. Vallier, J. Foucher, X. Detter, E. Pargon, O.
Joubert, G. Cunge and T. Lill, "Chemical topography analyses of silicon
gates etched in HBr/Cl₂/O₂ and HBr/Cl₂/O₂/CF₄ high density plasmas",
*Journal of Vacuum Science & Technology B* **21**(2), 904–911 (2003).
<https://doi.org/10.1116/1.1563255> Chemical topography of gates etched
in HBr/Cl₂/O₂ and HBr/Cl₂/O₂/CF₄. Used on step 062. Tier: deep dive.

**YOSHINO-1998** — H. Yoshino, T. Itani, S. Hashimoto, M. Yamana, T.
Yoshii and H. Tanabe, "Compatibility of chemically amplified
photoresists with bottom antireflective coatings", *Proc. SPIE*
**3333**, Advances in Resist Technology and Processing XV, 655 (1998).
<https://doi.org/10.1117/12.312459> Compatibility of chemically
amplified resists with bottom anti-reflective coatings. Used on step
059. Tier: deep dive.

**ZHANG-2005** — G. Zhang, M. Terry, S. O'Brien, R. Soper, M. Mason, W.
Kim, C. Wang, S. Hansen, J. Lee and J. Ganeshan, "65nm node gate pattern
using attenuated phase shift mask with off-axis illumination and
sub-resolution assist features", *Proc. SPIE* **5754**, Optical
Microlithography XVIII, 83 (2005). <https://doi.org/10.1117/12.600409>
Attenuated PSM with off-axis illumination and assist features on a later
gate level, showing where the technique went. Used on step 061. Tier:
deep dive.

**ZHANG-2007** — Q. Zhang, K. Poolla and C. J. Spanos, "Across Wafer
Critical Dimension Uniformity Enhancement Through Lithography and Etch
Process Sequence: Concept, Approach, Modeling, and Experiment", *IEEE
Transactions on Semiconductor Manufacturing* **20**(4), 488–505 (2007).
<https://doi.org/10.1109/TSM.2007.907627> Across-wafer CD uniformity
through the lithography and etch sequence. Used on steps 061 and 062.
Tier: deep dive.

#### Backside film removal (step 060)

**BROUSSOUS-2005** — L. Broussous, P. Besson, M. M. Frank and D.
Bourgeat, "Single Backside Cleaning on Silicon, Silicon Nitride and
Silicon Oxide", *Solid State Phenomena* **103–104**, 249–254 (2005).
<https://doi.org/10.4028/www.scientific.net/SSP.103-104.249>
Single-sided backside cleaning of silicon, nitride and oxide in a spin
tool. Used on step 060. Tier: deep dive.

**CARLSON-2006** — A. Carlson and T. Le, "Correlation of wafer backside
defects to photolithography hot spots using advanced macro inspection",
*Proc. SPIE* **6152**, Metrology, Inspection, and Process Control for
Microlithography XX, 61523E (2006). <https://doi.org/10.1117/12.656937>
Correlating backside defects with lithography hot spots. Used on step
060. Tier: deep dive.

**KERN-1978** — W. Kern and C. A. Deckert, "Chemical Etching", in J. L.
Vossen and W. Kern (eds.), *Thin Film Processes*, Academic Press, 1978,
pp. 401–496. <https://doi.org/10.1016/B978-0-12-728250-3.50015-5> The
reference chapter on wet etching of silicon, oxide and nitride. Used on
step 060. Tier: deep dive.

**LEDERER-2003** — K. Lederer, M. Scholze, U. Strohbach, A. Wocko, T.
Reuter and A. Schoenauer, "Wafer backside inspection applications in
lithography", *2003 IEEE/SEMI Advanced Semiconductor Manufacturing
Conference and Workshop*, pp. 1–8.
<https://doi.org/10.1109/ASMC.2003.1194459> Wafer backside inspection
for lithography. Used on step 060. Tier: deep dive.

**LIAUW-1987** — L. Liauw, A. Muray and M. Chen, "Impact Of Wafer
Flatness On Submicron Optical Lithography", *Proc. SPIE* **0772**,
Optical Microlithography VI, 232 (1987).
<https://doi.org/10.1117/12.967055> The impact of wafer flatness on
submicron optical lithography. Used on step 060. Tier: deep dive.

**SCHWARTZ-1976** — B. Schwartz and H. Robbins, "Chemical Etching of
Silicon: IV. Etching Technology", *Journal of The Electrochemical
Society* **123**(12), 1903–1909 (1976).
<https://doi.org/10.1149/1.2132721> HF/HNO₃ etching of silicon: rates,
mechanisms and technology. Used on step 060. Tier: deep dive.

**SEZ-223-MOOV** — Moov used-equipment marketplace, *Lam Research / SEZ
SP223* listing, accessed 2026-09-12.
<https://moov.co/marketplace/wet-etch/sez-lam-research/lam-research-sez-sp223>
Used-equipment listing for a 200 mm SEZ SP223 spin processor that names
backside film removal among its applications (weak evidence). Used on
step 060. Tier: cross-check.

**SEZ-223-PR** — SEZ Group, *SEZ Doubles Wafer Processing Capabilities
With New Dual Chamber Spin-Processing System* (press release,
1999-12-13), reproduced by Surface Finishing / VertMarkets.
<https://www.surfacefinishing.com/doc/sez-doubles-wafer-processing-capabilities-wit-0001>
Press release on the SEZ Spin-Processor 223: dual chambers, throughput,
three chemistries and film-removal applications. Used on step 060. Tier:
cross-check.

**UNE-2000** — A. Une, Y. Kai, M. Mochida, S. Matsui and F. Ohira,
"Influence of wafer chucking on focus margin for resolving fine patterns
in optical lithography", *Microelectronic Engineering* **53**(1–4),
137–140 (2000). <https://doi.org/10.1016/S0167-9317(00)00281-1> How
wafer chucking affects the focus margin for fine patterns. Used on step
060. Tier: deep dive.

**ZHANG-1997** — Y. Zhang, L. Wagner and P. Golbutsov, "Importance of
wafer flatness for CMP and lithography", *Proc. SPIE* **3050**, Optical
Microlithography X, 266 (1997). <https://doi.org/10.1117/12.275916> The
importance of wafer flatness for CMP and lithography. Used on step 060.
Tier: deep dive.

#### Tip, halo and activation (steps 064–075)

**AGARWAL-1998** — A. Agarwal, A. T. Fiory, H.-J. L. Gossmann, C. S.
Rafferty and P. Frisella, "Ultra-shallow junction formation by spike
annealing in a lamp-based or hot-walled rapid thermal annealing system:
effect of ramp-up rate", *Materials Science in Semiconductor Processing*
**1**(3–4), 237–241 (1998).
<https://doi.org/10.1016/S1369-8001(98)00030-4> Spike annealing in lamp
and hot-wall systems and the effect of ramp-up rate. Used on step 075.
Tier: deep dive.

**BUTI-1989** — T. N. Buti, S. Ogura, N. Rovedo, K. Tobimatsu and C. F.
Codella, "Asymmetrical halo source GOLD drain (HS-GOLD) deep sub-half
micron n-MOSFET design for reliability and performance", *IEDM 1989
Technical Digest*, pp. 617–620.
<https://doi.org/10.1109/IEDM.1989.74356> The asymmetric halo-source
device, showing what a one-sided halo does. Used on step 066. Tier: deep
dive.

**CHEN-1995** — H.-S. Chen, C.-S. Teng, L. Moberly and R. Lahri, "Ion
beam shadowing effect in submicrometer large-angle-tilt implanted drain
(LATID) MOSFETs", *Solid-State Electronics* **38**(7), 1321–1323 (1995).
<https://doi.org/10.1016/0038-1101(94)00256-F> Ion-beam shadowing of
tilted drain implants by adjacent structures, the effect behind the
PDK's shadowing allowances. Used on steps 064, 066, 068, 069, 072 and
073. Tier: deep dive.

**CODELLA-1985** — C. F. Codella and S. Ogura, "Halo doping effects in
submicron DI-LDD device design", *IEDM 1985 Technical Digest*, pp.
230–233. <https://doi.org/10.1109/IEDM.1985.190938> The halo added to
the LDD, the origin of the tip/halo pairing. Used on steps 064, 066, 071
and 073. Tier: deep dive.

**HORI-1989-LATID** — T. Hori, "1/4-μm LATID (LArge-Tilt-angle Implanted
Drain) technology for 3.3-V operation", *IEDM 1989 Technical Digest*,
pp. 777–780. <https://doi.org/10.1109/IEDM.1989.74169> The
quarter-micron LATID transistor for 3.3 V operation. Used on steps 068
and 069. Tier: deep dive.

**HORI-1992** — T. Hori, J. Hirase, Y. Odake and T. Yasui,
"Deep-submicrometer large-angle-tilt implanted drain (LATID)
technology", *IEEE Transactions on Electron Devices* **39**(10),
2312–2324 (1992). <https://doi.org/10.1109/16.158803> The full account
of large-angle-tilt implanted drain technology. Used on steps 068 and
069. Tier: deep dive.

**HU-1985-HCI** — C. Hu, S. C. Tam, F.-C. Hsu, P.-K. Ko, T.-Y. Chan and
K. W. Terrill, "Hot-electron-induced MOSFET degradation — Model,
monitor, and improvement", *IEEE Transactions on Electron Devices*
**32**(2), 375–385 (1985). <https://doi.org/10.1109/T-ED.1985.21952> The
hot-electron degradation model that sets the lifetime target. Used on
steps 068 and 069. Tier: deep dive.

**KASNAVI-2000** — R. Kasnavi, P. B. Griffin and J. D. Plummer, "Ultra
low energy arsenic implant limits on sheet resistance and junction
depth", *2000 Symposium on VLSI Technology, Digest of Technical Papers*,
pp. 112–113. <https://doi.org/10.1109/VLSIT.2000.852790> The limits of
ultra-low energy arsenic implants on sheet resistance and junction
depth. Used on step 065. Tier: deep dive.

**KING-2000** — E. E. King, R. C. Lacoe and J. Wang-Ratkovic, "The role
of the spacer oxide in determining worst-case hot-carrier stress
conditions for NMOS LDD devices", *Proc. 2000 IEEE International
Reliability Physics Symposium*, pp. 83–92.
<https://doi.org/10.1109/RELPHY.2000.843895> The role of the spacer
oxide in hot-carrier stress of LDD NMOS. Used on steps 068 and 069.
Tier: deep dive.

**LU-1989-RSCE** — C.-Y. Lu and J. M. Sung, "Reverse short-channel
effects on threshold voltage in submicrometer salicide devices", *IEEE
Electron Device Letters* **10**(10), 446–448 (1989).
<https://doi.org/10.1109/55.43095> The reverse short-channel effect in
submicrometre salicide devices. Used on steps 066 and 073. Tier: deep
dive.

**LUKASZEK-1996** — W. Lukaszek, S. Reno and R. Bammi, "Influence of
photoresist on wafer charging during high current arsenic implant",
*Proc. 11th International Conference on Ion Implantation Technology*
(1996), pp. 89–92. <https://doi.org/10.1109/IIT.1996.586135> Wafer
charging through resist during high-current arsenic implants. Used on
steps 065 and 067. Tier: deep dive.

**MACHALA-1997** — C. Machala, R. Wise, D. Mercer and A. Chatterjee,
"The role of boron segregation and transient enhanced diffusion on
reverse short channel effect", *Proc. SISPAD 1997*, pp. 141–143.
<https://doi.org/10.1109/SISPAD.1997.621357> Boron segregation and TED
in the reverse short-channel effect. Used on steps 066 and 073. Tier:
deep dive.

**NOBILI-1983** — D. Nobili, A. Carabelas, G. Celotti and S. Solmi,
"Precipitation as the Phenomenon Responsible for the Electrically
Inactive Arsenic in Silicon", *Journal of The Electrochemical Society*
**130**(4), 922–928 (1983). <https://doi.org/10.1149/1.2119859> Arsenic
precipitation and deactivation, irrelevant at LDD doses but decisive at
logic-tip doses. Used on steps 065, 072 and 075. Tier: deep dive.

**OGURA-1980** — S. Ogura, P. J. Tsang, W. W. Walker, D. L. Critchlow
and J. F. Shepard, "Design and characteristics of the lightly doped
drain-source (LDD) insulated gate field-effect transistor", *IEEE
Transactions on Electron Devices* **27**(8), 1359–1367 (1980).
<https://doi.org/10.1109/T-ED.1980.20040> The original lightly doped
drain-source transistor, the ancestor of every tip implant. Used on
steps 064, 065, 068, 069, 071 and 072. Tier: deep dive.

**OGURA-1981** — S. Ogura, P. J. Tsang, W. W. Walker, D. L. Critchlow
and J. F. Shepard, "Elimination of hot electron gate current by the
lightly doped drain-source structure", *IEDM 1981 Technical Digest*, pp.
651–654. <https://doi.org/10.1109/IEDM.1981.190171> Elimination of
hot-electron gate current by the LDD structure. Used on step 069. Tier:
deep dive.

**PAT-HALO-AMD-DIFF** — B. Yu (Advanced Micro Devices), *MOSFET with
differential halo implant and annealing strategy*, US 6,630,385 B1,
granted 2003-10-07.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6630385>
Two halo implants with different anneals to shape the pocket. Used on
steps 066 and 073. Tier: deep dive.

**PAT-HALO-AMD-ZERO** — D.-H. Ju and S. Luning (Advanced Micro Devices),
*CMOS processing employing zero degree halo implant for P-channel
transistor*, US 6,232,166 B1, granted 2001-05-15.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6232166>
A zero-degree halo for the PMOS, for contrast with the tilted NMOS halo.
Used on step 066. Tier: deep dive.

**PAT-HALO-CHARTERED** — Y. Pan (Chartered Semiconductor Manufacturing),
*Method of making self-aligned halo process for reducing junction
capacitance*, US 5,595,919 A, granted 1997-01-21.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5595919>
A self-aligned halo process designed to limit the junction-capacitance
penalty. Used on steps 066 and 073. Tier: deep dive.

**PAT-HALO-GOLDSTAR** — H. S. Hwang (Goldstar Electron), *Method for
fabricating LDD transitor utilizing halo implant*, US 5,364,807 A,
granted 1994-11-15.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5364807>
An LDD transistor with a halo punch-through stopper made without extra
masks. Used on steps 066 and 073. Tier: deep dive.

**PAT-HV-GRADED-CYP** — I. Kouznetsov (Cypress Semiconductor), *Method
and structure for high-voltage device with self-aligned graded
junctions*, US 6,531,366 B1, granted 2003-03-11.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6531366>
A high-voltage device with self-aligned graded junctions in a CMOS flow.
Used on steps 068 and 069. Tier: deep dive.

**PAT-LDD-MICRON** — L. C. Tran, M. McQueen and R. Kerr (Micron
Technology), *Double LDD devices for improved DRAM refresh*, US
6,759,288 B2, granted 2004-07-06.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6759288>
A second, lighter LDD masked onto selected transistors to cut junction
leakage. Used on steps 064, 065, 071 and 072. Tier: deep dive.

**PAT-MULTI-LDD-AMD** — M. I. Gardner, F. N. Hause and H. J. Fulford
(Advanced Micro Devices), *Integrated circuit having multiple LDD and/or
source/drain implant steps to enhance circuit performance*, US 5,793,090
A, granted 1998-08-11.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5793090>
Separate LDD and source/drain implant steps for different transistors on
one chip. Used on steps 064, 068 and 071. Tier: deep dive.

**PAT-QUAD-TSMC** — M.-S. Lin, C.-S. Yoo and M.-S. Liang (Taiwan
Semiconductor Manufacturing Company), *Multiple tilted angle ion
implantation MOSFET method*, US 5,372,957 A, granted 1994-12-13.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5372957>
Multiple tilted-angle implantation with wafer rotation for LDD devices.
Used on steps 066, 069 and 073. Tier: deep dive.

**PAT-SPE-AMD** — B. Yu (Advanced Micro Devices), *Solid phase epitaxy
activation process for source/drain junction extensions and halo
regions*, US 6,521,502 B1, granted 2003-02-18.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6521502>
Activating extensions and halos by solid-phase epitaxy at low
temperature, an alternative to spike-anneal activation. Used on steps
065, 066, 072 and 075. Tier: deep dive.

**PAT-SPIKE-AMAT** — B. Ramachandran, R. Jallepally, R. C. Boas, S.
Ramamurthy, A. Al-Bayati, H. Graoui and J. M. Spear (Applied Materials),
*Advances in spike anneal processes for ultra shallow junctions*, US
6,897,131 B2, granted 2005-05-24.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6897131>
Sharpening the spike by faster cool-down. Used on step 075. Tier: deep
dive.

**PAT-SPIKE-AMAT-AMBIENT** — D. Jennings, S. Tallavarjula and R. Thakur
(Applied Materials), *Optimal spike anneal ambient*, US 6,803,297 B2,
granted 2004-10-12.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6803297>
The anneal ambient for spike anneals. Used on step 075. Tier: deep dive.

**PAT-SPIKE-IBM** — K. L. Lee, Y. Zhang, M. Surendra and E. M. Sikorski
(IBM), *Sacrificial polysilicon sidewall process and rapid thermal spike
annealing for advance CMOS fabrication*, US 6,518,136 B2, granted
2003-02-11.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6518136>
Extensions and halos activated by spike annealing to prevent their
diffusion. Used on step 075. Tier: deep dive.

**RAFI-2001** — J. M. Rafí and F. Campabadal, "Hot-carrier degradation
in deep-submicrometer nMOSFETs: lightly doped drain vs. large angle tilt
implanted drain", *Solid-State Electronics* **45**(8), 1391–1401 (2001).
<https://doi.org/10.1016/S0038-1101(01)00004-1> Hot-carrier degradation
of LDD versus LATID NMOS. Used on steps 068 and 069. Tier: deep dive.

**ROUSSEAU-1994** — P. M. Rousseau, P. B. Griffin and J. D. Plummer,
"Electrical deactivation of arsenic as a source of point defects",
*Applied Physics Letters* **65**(5), 578–580 (1994).
<https://doi.org/10.1063/1.112301> Arsenic deactivation as a source of
interstitials that enhance diffusion of neighbouring dopants. Used on
steps 065, 066 and 075. Tier: deep dive.

**SHIN-1999** — H. Shin and S. Lee, "An 0.1-μm asymmetric halo by
large-angle-tilt implant (AHLATI) MOSFET for high performance and
reliability", *IEEE Transactions on Electron Devices* **46**(4), 820–822
(1999). <https://doi.org/10.1109/16.753725> An asymmetric halo by
large-angle tilt implant at 0.1 µm. Used on step 066. Tier: deep dive.

**SHISHIGUCHI-1997** — S. Shishiguchi, A. Mineji, T. Hayashi and S.
Saito, "Boron Implanted Shallow Junction Formation By
High-temperature/Short-time/high-ramping-rate (400 °C/sec) RTA", *1997
Symposium on VLSI Technology, Digest of Technical Papers*, pp. 89–90.
<https://doi.org/10.1109/VLSIT.1997.623709> 400 °C/s RTA for boron
shallow junctions. Used on step 075. Tier: deep dive.

**TAKEDA-1982** — E. Takeda, H. Kume, T. Toyabe and S. Asai,
"Submicrometer MOSFET structure for minimizing hot-carrier generation",
*IEEE Transactions on Electron Devices* **29**(4), 611–618 (1982).
<https://doi.org/10.1109/T-ED.1982.20752> Drain structures for
minimising hot-carrier generation. Used on steps 068 and 069. Tier: deep
dive.

**TAUR-1998** — Y. Taur, C. H. Wann and D. J. Frank, "25 nm CMOS design
considerations", *IEDM 1998 Technical Digest*, pp. 789–792.
<https://doi.org/10.1109/IEDM.1998.746474> Super-halo design: pockets at
the channel ends, light doping in between. Used on steps 066 and 073.
Tier: deep dive.

**THOMPSON-1998** — S. Thompson, P. Packan, T. Ghani, M. Stettler, M.
Alavi, I. Post, S. Tyagi, S. Ahmed, S. Yang and M. Bohr, "Source/drain
extension scaling for 0.1 μm and below channel length MOSFETs", *1998
Symposium on VLSI Technology, Digest of Technical Papers*, pp. 132–133.
<https://doi.org/10.1109/VLSIT.1998.689229> How extension depth and
doping scale with gate length, the reason a 1.8 V tip differs from a 5 V
one. Used on steps 064, 065 and 072. Tier: deep dive.

**WIKI-HCI** — Wikipedia, *Hot-carrier injection*.
<https://en.wikipedia.org/wiki/Hot-carrier_injection> Hot-carrier
injection, the failure mode that graded and LATID drains exist to
prevent. Used on steps 068 and 069. Tier: high-level.

**YONEDA-2002** — K. Yoneda and M. Niwayama, "The drain current
asymmetry of 130 nm MOSFETs due to extension implant shadowing
originated by mechanical angle error in high current implanter",
*Extended Abstracts of the Third International Workshop on Junction
Technology (IWJT 2002)*, pp. 19–22.
<https://doi.org/10.1109/IWJT.2002.1225190> Drain-current asymmetry in
130 nm MOSFETs from extension-implant shadowing caused by an implanter
angle error. Used on steps 064 and 065. Tier: deep dive.

### 8.12 Spacer, source/drain, silicide, local-interconnect and metal-1 module sources

Sources introduced by the writers of the spacer and source/drain module
(steps 076–088), the pre-metal dielectric and local-interconnect module
(steps 089–106) and the metal-contact and metal-1 module (steps 107–117)
that had no entry above. Each label on those pages is the key below in
lower case; the citation is the one given in the page footnote, and the
annotation is taken from the citing page's reading list. Grouped by the
sub-module that first cited the source; an entry names every page that
uses it. Only the Cypress qualification reports and notification under
"Metal-1 stack" describe the Bloomington fab; none of the other sources
describes SkyWater unless the entry says so.

#### Spacer nitride, spacer etch, nitride/poly cut and spacer oxide (steps 076–080)

**CACCIATO-2003** — A. Cacciato, A. Scarpa, S. Evseev and M. Diekema,
"Charging damage during contact etch triggered by increased borderless
nitride conductivity", *Proc. 2003 8th International Symposium on
Plasma- and Process-Induced Damage*, pp. 20–23.
<https://doi.org/10.1109/PPID.2003.1199721> Charging damage when a
contact etch meets a borderless nitride. Used on steps 078, 079, 094,
096, 104 and 108. Tier: deep dive.

**FARHANE-2003** — R. Farhane, F. Salvetti, F. Wacquant, C. Laviron, B.
Froment, A. Muller, A. Pouydebasque and A. Halimaoui, "Investigation of
the dose loss during annealing in nitrogen of shallow-implanted
arsenic", *Proc. 11th IEEE International Conference on Advanced Thermal
Processing of Semiconductors (RTP 2003)*, pp. 173–176.
<https://doi.org/10.1109/RTP.2003.1249144> Arsenic dose loss during
nitrogen anneals. Used on steps 080, 086 and 088. Tier: deep dive.

**GOSS-1997** — M. Goss and R. Thornburg, "The challenges of nitride
spacer processing for a 0.35 μm CMOS technology", *1997 IEEE/SEMI
Advanced Semiconductor Manufacturing Conference and Workshop (ASMC 97)
Proceedings*, pp. 228–233. <https://doi.org/10.1109/ASMC.1997.630740>
Integrating a nitride spacer into a 0.35 µm CMOS technology. Used on
steps 076 and 077. Tier: deep dive.

**GUMPHER-2004** — J. Gumpher, W. Bather, N. Mehta and D. Wedel,
"Characterization of Low-Temperature Silicon Nitride LPCVD from
Bis(tertiary-butylamino)silane and Ammonia", *Journal of The
Electrochemical Society* **151**(5), G353 (2004).
<https://doi.org/10.1149/1.1690294> BTBAS low-temperature LPCVD nitride.
Used on steps 076 and 104. Tier: deep dive.

**HUGHEY-2003** — M. P. Hughey and R. F. Cook, "Irreversible Tensile
Stress Development in PECVD Silicon Nitride Films", *MRS Proceedings*
**795** (2003). <https://doi.org/10.1557/PROC-795-U1.6> Irreversible
stress change in PECVD nitride on heating. Used on steps 076 and 104.
Tier: deep dive.

**HWANG-1996** — H. Hwang, D.-H. Lee and J. M. Hwang, "Effect of Nitride
Sidewall Spacer on Hot Carrier Reliability Characteristics of MOSFET's",
*Extended Abstracts of the 1996 International Conference on Solid State
Devices and Materials*, PC-4-6 (1996).
<https://doi.org/10.7567/SSDM.1996.PC-4-6> Nitride spacer versus
hot-carrier reliability. Used on step 076. Tier: deep dive.

**ITO-2000** — S. Ito, H. Namba, K. Yamaguchi, T. Hirata, K. Ando, S.
Koyama, S. Kuroki, N. Ikezawa, T. Suzuki, T. Saitoh and T. Horiuchi,
"Mechanical stress effect of etch-stop nitride and its impact on deep
submicron transistor design", *IEDM 2000 Technical Digest*, pp. 247–250.
<https://doi.org/10.1109/IEDM.2000.904303> Nitride film stress as a
channel-strain variable. Used on steps 076, 078 and 104. Tier: deep
dive.

**JANAPATY-1998** — V. Janapaty, J.-Y. Tsai and S. Prasad, "Enhanced
hot-carrier-induced degradation of 0.25-μm P-MOSFETs with oxide/nitride
composite spacer compared to those with oxide spacer", *Proc. SPIE*
**3510**, Microelectronic Manufacturing, 225 (1998).
<https://doi.org/10.1117/12.324387> Oxide/nitride composite versus oxide
spacers on 0.25 µm PMOS. Used on steps 076 and 080. Tier: deep dive.

**JOUBERT-1997** — O. Joubert and F. H. Bell, "Polysilicon Gate Etching
in High-Density Plasmas: Comparison Between Oxide Hard Mask and Resist
Mask", *Journal of The Electrochemical Society* **144**(5), 1854–1861
(1997). <https://doi.org/10.1149/1.1837690> Resist and oxide masks over
poly in high-density plasmas. Used on step 079. Tier: deep dive.

**KASTENMEIER-1996** — B. E. E. Kastenmeier, P. J. Matsuo, J. J. Beulens
and G. S. Oehrlein, "Chemical dry etching of silicon nitride and silicon
dioxide using CF₄/O₂/N₂ gas mixtures", *Journal of Vacuum Science &
Technology A* **14**(5), 2802–2813 (1996).
<https://doi.org/10.1116/1.580203> Nitride and oxide etching in
CF₄/O₂/N₂. Used on steps 077, 079 and 108. Tier: deep dive.

**KRIEGER-1989** — G. Krieger, G. Spadini, P. Cuevas and J. Schuur,
"Shadowing effects due to tilted arsenic source/drain implant", *IEEE
Transactions on Electron Devices* **36**(11), 2458–2461 (1989).
<https://doi.org/10.1109/16.43667> Shadowing of a tilted source/drain
implant by the gate and spacer. Used on steps 077, 082, 083 and 086.
Tier: deep dive.

**LEE-CHEN-1983** — Y. H. Lee and M.-M. Chen, "Silicon etching mechanism
and anisotropy in CF₄+O₂ plasma", *Journal of Applied Physics*
**54**(10), 5966–5973 (1983). <https://doi.org/10.1063/1.331774>
Mechanism and anisotropy in CF₄+O₂ plasmas. Used on steps 077 and 079.
Tier: deep dive.

**LIM-1993** — D. Lim, S.-H. Yang, S. Morris and A. F. Tasch, "An
accurate and computationally-efficient model of boron implantation
through screen oxide layers into (100) single-crystal silicon", *IEDM
1993 Technical Digest*, pp. 291–294.
<https://doi.org/10.1109/IEDM.1993.347350> A model of boron implantation
through screen oxide into (100) silicon. Used on steps 080 and 082.
Tier: deep dive.

**MCANDREW-1994** — C. C. McAndrew, G. Zaneski, P. Layman and S. Ayyar,
"Accurate characterization of MOSFET overlap/fringing capacitance for
circuit design", *Proc. 1994 IEEE International Conference on
Microelectronic Test Structures*, pp. 15–20.
<https://doi.org/10.1109/ICMTS.1994.303510> Overlap/fringing capacitance
models in which the spacer's permittivity appears. Used on step 076.
Tier: deep dive.

**MIZUNO-1989** — T. Mizuno, T. Kobori, Y. Saitoh, S. Sawada and T.
Tanaka, "High dielectric LDD spacer technology for high performance
MOSFET using gate-fringing field effects", *IEDM 1989 Technical Digest*,
pp. 613–616. <https://doi.org/10.1109/IEDM.1989.74355> High-permittivity
spacers and the gate-fringing field. Used on step 076. Tier: deep dive.

**NG-1986** — K. K. Ng and W. T. Lynch, "Analysis of the
gate-voltage-dependent series resistance of MOSFET's", *IEEE
Transactions on Electron Devices* **33**(7), 965–972 (1986).
<https://doi.org/10.1109/T-ED.1986.22602> Series resistance of the
un-silicided extension under the spacer, and why it limits scaling. Used
on steps 076, 077, 082 and 086. Tier: deep dive.

**NG-1987** — K. K. Ng and W. T. Lynch, "The impact of intrinsic series
resistance on MOSFET scaling", *IEEE Transactions on Electron Devices*
**34**(3), 503–511 (1987). <https://doi.org/10.1109/T-ED.1987.22956>
Series resistance of the un-silicided extension under the spacer, and
why it limits scaling. Used on step 076. Tier: deep dive.

**OM-1995** — J.-C. Om, M.-S. Jo, H.-S. Park, I.-S. Chung and W.-S. Min,
"Source/drain junction leakage current of LDD NMOSFET with various
spacer materials", *Proc. 1995 International Conference on
Microelectronic Test Structures*, pp. 177–180.
<https://doi.org/10.1109/ICMTS.1995.513968> Junction leakage versus
spacer material. Used on steps 076 and 077. Tier: deep dive.

**PARK-1991** — C. Park, K. M. Klein, A. F. Tasch, R. B. Simonton and G.
E. Lux, "Paradoxical boron profile broadening caused by implantation
through a screen oxide layer", *IEDM 1991 Technical Digest*, pp. 67–70.
<https://doi.org/10.1109/IEDM.1991.235422> Boron profile broadening from
a screen oxide. Used on steps 080 and 082. Tier: deep dive.

**PELLETIER-2008** — B. Pelletier, M. Juhel, C. Trouiller, D. Beucher,
J. Autran and P. Morin, "Boron out-diffusion mechanism in oxide and
nitride CMOS sidewall spacer: Impact of the materials properties",
*Materials Science and Engineering: B* **154–155**, 252–255 (2008).
<https://doi.org/10.1016/j.mseb.2008.09.025> Boron out-diffusion into
oxide and nitride spacers. Used on steps 080 and 088. Tier: deep dive.

**PFIESTER-1988** — J. R. Pfiester, "LDD MOSFETs using disposable
sidewall spacer technology", *IEEE Electron Device Letters* **9**(4),
189–192 (1988). <https://doi.org/10.1109/55.685> Disposable-spacer
alternatives, in which the spacer is removed after the implant. Used on
step 077. Tier: deep dive.

**PFIESTER-1990-EDL** — J. R. Pfiester, L. C. Parrillo, M. Woo, H.
Kawasaki, B. Boeck, E. Travis and C. D. Gunderson, "An advanced 0.5-μm
CMOS disposable TiN LDD/salicide spacer process", *IEEE Electron Device
Letters* **11**(7), 318–320 (1990). <https://doi.org/10.1109/55.56487>
Disposable-spacer alternatives, in which the spacer is removed after the
implant. Used on step 077. Tier: deep dive.

**REINHARDT-1992** — K. A. Reinhardt and F. M. Dumesnil,
"Characterization of silicon damage during LDD oxide spacer etch with
the use of thermal-wave-modulated reflectance", *Proc. SPIE* **1593**,
Dry Etch Technology, 32–46 (1992). <https://doi.org/10.1117/12.56913>
Silicon damage from an LDD spacer etch measured by thermal-wave
reflectance. Used on step 077. Tier: deep dive.

**SAMBONSUGI-1998** — Y. Sambonsugi and T. Sugii, "Hot-carrier
degradation mechanism and promising device design of nMOSFETs with
nitride sidewall spacer", *1998 IEEE International Reliability Physics
Symposium Proceedings*, pp. 184–188.
<https://doi.org/10.1109/RELPHY.1998.670531> Hot-carrier mechanism of
NMOS with nitride spacers. Used on step 076. Tier: deep dive.

**SHIBAHARA-1998** — K. Shibahara, H. Furumoto, K. Egusa, M. Koh and S.
Yokoyama, "Dopant Loss Origins of Low Energy Implanted Arsenic and
Antimony for Ultra Shallow Junction Formation", *MRS Proceedings*
**532** (1998). <https://doi.org/10.1557/PROC-532-23> Origins of dopant
loss for low-energy arsenic and antimony. Used on steps 080 and 086.
Tier: deep dive.

**SHIMAYA-1995** — M. Shimaya, "Water diffusion model for the
enhancement of hot-carrier-induced degradation due to silicon nitride
passivation in submicron MOSFET's", *33rd IEEE International Reliability
Physics Symposium Proceedings* (1995), pp. 292–296.
<https://doi.org/10.1109/RELPHY.1995.513694> Water diffusion through
nitride and hot-carrier degradation. Used on steps 076 and 104. Tier:
deep dive.

**SHIMIZU-2001** — A. Shimizu, K. Hachimine, N. Ohki, H. Ohta, M.
Koguchi, Y. Nonaka, H. Sato and F. Ootsuka, "Local mechanical-stress
control (LMC): a new technique for CMOS-performance enhancement", *IEDM
2001 Technical Digest*, pp. 19.4.1–19.4.4.
<https://doi.org/10.1109/IEDM.2001.979529> Nitride film stress as a
channel-strain variable. Used on steps 076 and 104. Tier: deep dive.

**SHRIVASTAVA-1982** — R. Shrivastava and K. Fitzpatrick, "A simple
model for the overlap capacitance of a VLSI MOS device", *IEEE
Transactions on Electron Devices* **29**(12), 1870–1875 (1982).
<https://doi.org/10.1109/T-ED.1982.21044> Overlap/fringing capacitance
models in which the spacer's permittivity appears. Used on steps 076 and
080. Tier: deep dive.

**SMITH-2005** — J. W. Smith, S. M. Seutter and R. S. Iyer, "Thermal
Chemical Vapor Deposition of Bis(Tertiary-Butylamino)Silane-based
Silicon Nitride Thin Films", *Journal of The Electrochemical Society*
**152**(4), G316 (2005). <https://doi.org/10.1149/1.1870792> BTBAS
low-temperature LPCVD nitride. Used on step 076. Tier: deep dive.

**TANG-1985** — T. E. Tang, C.-C. Wei, R. A. Haken, T. C. Holloway,
C.-F. Wan and M. A. Douglas, "VLSI local interconnect level using
titanium nitride", *IEDM 1985 Technical Digest*, pp. 590–593.
<https://doi.org/10.1109/IEDM.1985.191041> The TiN local-interconnect
scheme in which a nitride over poly is opened only where contacts are
made. Used on steps 078, 079, 094 and 101. Tier: deep dive.

**TANG-1987** — T. E. Tang, C.-C. Wei, R. A. Haken, T. C. Holloway, L.
R. Hite and T. G. W. Blake, "Titanium nitride local interconnect
technology for VLSI", *IEEE Transactions on Electron Devices* **34**(3),
682–688 (1987). <https://doi.org/10.1109/T-ED.1987.22980> The TiN
local-interconnect scheme in which a nitride over poly is opened only
where contacts are made. Used on steps 078, 079, 101, 102 and 103. Tier:
deep dive.

**TSANG-1982** — P. J. Tsang, S. Ogura, W. W. Walker, J. F. Shepard and
D. L. Critchlow, "Fabrication of high-performance LDDFET's with oxide
sidewall-spacer technology", *IEEE Transactions on Electron Devices*
**29**(4), 590–596 (1982). <https://doi.org/10.1109/T-ED.1982.20748> The
oxide sidewall-spacer process: conformal deposition plus anisotropic
etch-back. Used on steps 076, 077, 080, 082 and 086. Tier: deep dive.

**TUDA-2004** — M. Tuda, K. Shintani and J. Tanimura, "Highly Selective
Removal of Residual Deposited Films and Oxide Hard Masks on Polysilicon
Gate Electrodes in Anhydrous HF Gases", *Japanese Journal of Applied
Physics* **43**(3R), 945 (2004). <https://doi.org/10.1143/JJAP.43.945>
Selective removal of hard masks and residues from poly gates. Used on
step 079. Tier: deep dive.


#### Source/drain implant masks, implants, strips and activation anneal (steps 081–088)

**ADACHI-2001** — K. Adachi, K. Ohuchi and Y. Toyoshima, "Combination of
germanium preamorphization and sub-keV boron implantation for
source/drain extension of pMOSFETs", *Extended Abstracts of the Second
International Workshop on Junction Technology* (2001), pp. 35–38.
<https://doi.org/10.1109/IWJT.2001.993821> Ge PAI with sub-keV boron for
PMOS extensions. Used on steps 082 and 083. Tier: deep dive.

**AGARWAL-2000** — A. Agarwal, "Ultra-shallow junction formation using
conventional ion implantation and rapid thermal annealing", *Proc. 2000
International Conference on Ion Implantation Technology*, pp. 293–299.
<https://doi.org/10.1109/IIT.2000.924147> Ultra-shallow junctions by
conventional implantation and RTA. Used on step 088. Tier: deep dive.

**ANGELUCCI-1985** — R. Angelucci, G. Celotti, D. Nobili and S. Solmi,
"Precipitation and Diffusivity of Arsenic in Silicon", *Journal of The
Electrochemical Society* **132**(11), 2726–2730 (1985).
<https://doi.org/10.1149/1.2113654> Arsenic precipitation and
diffusivity. Used on step 086. Tier: deep dive.

**AUGENDRE-2001** — E. Augendre, A. De Keersgieter, S. Kubicek, A.
Redolfi, J. Van Laer and G. Badenes, "Arsenic and Phosphorus
co-Implantation for Deep Submicron CMOS Gate and Source/Drain
Engineering", *Proc. 31st European Solid-State Device Research
Conference (ESSDERC 2001)*, pp. 115–118.
<https://doi.org/10.1109/ESSDERC.2001.195214> As/P co-implantation for
gate and source/drain engineering. Used on steps 083 and 086. Tier: deep
dive.

**BOURDELLE-2000** — K. K. Bourdelle, H.-J. Gossmann, S. Chaudhry and A.
Agarwal, "Comparison of B and BF₂ source/drain extension implants for
PMOS transistors with thin gate oxides", *Proc. 2000 International
Conference on Ion Implantation Technology*, pp. 25–27.
<https://doi.org/10.1109/IIT.2000.924081> B versus BF₂ for PMOS
junctions with thin gate oxides. Used on steps 082 and 083. Tier: deep
dive.

**CAMILLO-CASTILLO-2002** — R. A. Camillo-Castillo, K. S. Jones, M. E.
Law and L. M. Rubin, "Study of the Effects of a Two-Step Anneal on the
End of Range Defects in Silicon", *MRS Proceedings* **717** (2002).
<https://doi.org/10.1557/PROC-717-C1.4> Two-step anneals and
end-of-range defects. Used on steps 088 and 092. Tier: deep dive.

**CARPENTER-2002** — N. Carpenter and T. Fecteau, "Process and
productivity improvements during high pressure photoresist outgassing",
*Proc. 14th International Conference on Ion Implantation Technology*
(2002), pp. 507–510. <https://doi.org/10.1109/IIT.2002.1258053>
Productivity during high-pressure resist outgassing. Used on steps 081
and 084. Tier: deep dive.

**CHEN-2002-RTP** — D. Chen, D. DeWitt, B. Tsai, K. Kreider and W.
Kimes, "Effects of wafer emissivity on rapid thermal processing
temperature measurement", *Proc. 10th IEEE International Conference on
Advanced Thermal Processing of Semiconductors (RTP 2002)*, pp. 59–67.
<https://doi.org/10.1109/RTP.2002.1039440> Temperature control and
emissivity in RTP. Used on steps 088 and 092. Tier: deep dive.

**CURRENT-1996-IIT** — M. I. Current, M. Vella and W. Lukaszek,
"Beam-plasma concepts for wafer charging control during ion
implantation", *Proc. 11th International Conference on Ion Implantation
Technology* (1996), pp. 53–56. <https://doi.org/10.1109/IIT.1996.586119>
Wafer charging and flood-gun control during high-current implants. Used
on step 082. Tier: deep dive.

**CURRENT-1998** — M. I. Current, M. Foad, S. Brown, W. Lukaszek and M.
Vella, "Photoresist effects on wafer charging control: current-voltage
characteristics measured with Charm-2 monitors during high-current As⁺
implantation", *Proc. 1998 International Conference on Ion Implantation
Technology*, vol. 1, pp. 490–493.
<https://doi.org/10.1109/IIT.1999.812159> Charging control during
high-current arsenic implants. Used on step 086. Tier: deep dive.

**DIXON-1996** — W. Dixon, W. Lukaszek and C. Heden,
"Photoresist-enhanced wafer charging during high current ion
implantation", *Proc. 11th International Conference on Ion Implantation
Technology* (1996), pp. 85–88. <https://doi.org/10.1109/IIT.1996.586134>
Resist-enhanced wafer charging during high-current implants. Used on
steps 081, 082 and 083. Tier: deep dive.

**GERRITSEN-2000** — E. Gerritsen, "Spike anneal: RTP processing at
reduced thermal budget with applications to TiSi₂ formation towards
0.1-μm linewidths", *Microelectronic Engineering* **50**(1–4), 147–151
(2000). <https://doi.org/10.1016/S0167-9317(99)00275-0> The spike
anneal. Used on step 088. Tier: deep dive.

**JEON-1989** — Y.-J. Jeon, M. F. Becker and R. M. Walser,
"Concentration Dependence of Arsenic on Solid Phase Epitaxial Regrowth
of Amorphous Silicon", *MRS Proceedings* **157** (1989).
<https://doi.org/10.1557/PROC-157-745> Solid-phase epitaxial regrowth
and its arsenic-concentration dependence. Used on steps 086 and 088.
Tier: deep dive.

**JONES-1996** — M. Jones and F. Sinclair, "Across-wafer channeling
variations on batch implanters: a graphical technique to analyze
spinning disk systems", *Proc. 11th International Conference on Ion
Implantation Technology* (1996), pp. 264–267.
<https://doi.org/10.1109/IIT.1996.586257> Channelling variation across a
spinning-disc batch implanter. Used on steps 082 and 086. Tier: deep
dive.

**JOSSE-2002** — E. Josse, F. Arnaud, F. Wacquant, D. Lenoble, O. Menut
and E. Robilliart, "Spike Anneal Optimization for Digital and Analogue
High Performance 0.13 μm CMOS Platform", *Proc. 32nd European
Solid-State Device Research Conference (ESSDERC 2002)*, pp. 207–210.
<https://doi.org/10.1109/ESSDERC.2002.194906> Source/drain and
spike-anneal optimisation for a 0.13 µm platform. Used on steps 083 and
088. Tier: deep dive.

**LEE-1999-EDL** — H.-D. Lee and Y.-J. Lee, "Arsenic and phosphorus
double ion implanted source/drain junction for 0.25- and sub-0.25-μm
MOSFET technology", *IEEE Electron Device Letters* **20**(1), 42–44
(1999). <https://doi.org/10.1109/55.737568> An As/P double-implanted
source/drain for 0.25 µm, the n-type analogue. Used on steps 083 and
086. Tier: deep dive.

**LIFSHITZ-1985** — N. Lifshitz, "Dependence of the work-function
difference between the polysilicon gate and silicon substrate on the
doping level in polysilicon", *IEEE Transactions on Electron Devices*
**32**(3), 617–621 (1985). <https://doi.org/10.1109/T-ED.1985.21987>
Poly gate work function versus doping. Used on step 082. Tier: deep
dive.

**LUNING-1992** — S. Luning, P. M. Rousseau, P. B. Griffin, P. G. Carey
and J. D. Plummer, "Kinetics of high concentration arsenic deactivation
at moderate to low temperatures", *IEDM 1992 Technical Digest*, pp.
457–460. <https://doi.org/10.1109/IEDM.1992.307400> Kinetics of arsenic
deactivation. Used on steps 086, 088 and 092. Tier: deep dive.

**MATSUDA-2002** — T. Matsuda, S. Shishiguchi and H. Kitajima, "Ultra
Shallow Junction Formation with High Process Controllability Using
Optimized Rapid Thermal Anneal Process", *Japanese Journal of Applied
Physics* **41**(2A), 451–457 (2002).
<https://doi.org/10.1143/JJAP.41.451> An optimised RTA for shallow
junctions. Used on step 088. Tier: deep dive.

**MEHTA-1996** — S. Mehta, B. Axan, S. Walther and S. Felch,
"Investigation of negative charging with plasma flood gun (PFG) during
high current implantation", *Proc. 11th International Conference on Ion
Implantation Technology* (1996), pp. 73–76.
<https://doi.org/10.1109/IIT.1996.586128> Wafer charging and flood-gun
control during high-current implants. Used on steps 082 and 086. Tier:
deep dive.

**MEZACK-2000** — G. Mezack, T. Callahan, S. Mehta and U. Jeong,
"Advantages of the Varian VIISta single wafer high current ion implanter
for advanced device fabrication", *Proc. 2000 International Conference
on Ion Implantation Technology*, pp. 431–434.
<https://doi.org/10.1109/IIT.2000.924180> The single-wafer high-current
implanter alternative. Used on steps 082, 083 and 086. Tier: deep dive.

**OGURA-1982** — S. Ogura, C. F. Codella, N. Rovedo, J. F. Shepard and
J. Riseman, "A half micron MOSFET using double implanted LDD", *IEDM
1982 Technical Digest*, pp. 718–721.
<https://doi.org/10.1109/IEDM.1982.190395> The double-implanted LDD, two
implants to grade one junction. Used on step 083. Tier: deep dive.

**OZTURK-1988** — M. C. Öztürk, J. J. Wortman, C. M. Osburn, A. Ajmera,
G. A. Rozgonyi, E. Frey, W.-K. Chu and C. Lee, "Optimization of the
germanium preamorphization conditions for shallow-junction formation",
*IEEE Transactions on Electron Devices* **35**(5), 659–668 (1988).
<https://doi.org/10.1109/16.2510> Germanium pre-amorphisation for
shallow p⁺ junctions. Used on steps 082 and 083. Tier: deep dive.

**ROMIG-1996** — T. Romig, M. Bishop and V. Rio, "Exploration and
prevention of photo resist burning in a high current ion implanter",
*Proc. 11th International Conference on Ion Implantation Technology*
(1996), pp. 190–193. <https://doi.org/10.1109/IIT.1996.586181> Resist
burning in a high-current implanter. Used on steps 081, 082, 084, 085
and 086. Tier: deep dive.

**ROUSSEAU-1996** — P. M. Rousseau, P. B. Griffin, S. C. Kuehne and J.
D. Plummer, "Enhanced diffusion by electrical deactivation of arsenic
and its implications for bipolar devices", *IEEE Transactions on
Electron Devices* **43**(4), 547–553 (1996).
<https://doi.org/10.1109/16.485536> Arsenic deactivation as an
interstitial source and its device consequences. Used on step 086. Tier:
deep dive.

**SORRELL-1993** — F. Y. Sorrell and R. S. Gyurcsik, "Model-based
emissivity correction in pyrometer temperature control of rapid thermal
processing systems", *IEEE Transactions on Semiconductor Manufacturing*
**6**(3), 273–276 (1993). <https://doi.org/10.1109/66.238178>
Temperature control and emissivity in RTP. Used on steps 088, 092 and
098. Tier: deep dive.

**VANDENABEELE-1998** — P. Vandenabeele and W. Renken, "Model Based
Temperature Control in RTP Yielding ±0.1 °C accuracy on A 1000 °C, 2
second, 100 °C/s Spike Anneal", *MRS Proceedings* **525** (1998).
<https://doi.org/10.1557/PROC-525-109> Temperature control and
emissivity in RTP. Used on steps 088 and 092. Tier: deep dive.


#### Sacrificial PSG, CMP over poly, cap oxide and second anneal (steps 089–092)

**ADAMS-1981** — A. C. Adams and C. D. Capio, "Planarization of
Phosphorus-Doped Silicon Dioxide", *Journal of The Electrochemical
Society* **128**(2), 423–429 (1981). <https://doi.org/10.1149/1.2127434>
Planarisation versus phosphorus content and anneal. Used on step 089.
Tier: deep dive.

**ADAMS-1981-PECVD** — A. C. Adams, F. B. Alexander, C. D. Capio and T.
E. Smith, "Characterization of Plasma-Deposited Silicon Dioxide",
*Journal of The Electrochemical Society* **128**(7), 1545–1551 (1981).
<https://doi.org/10.1149/1.2127680> Characterisation of plasma-deposited
silicon dioxide. Used on steps 091, 092, 096 and 105. Tier: deep dive.

**ALVI-1986** — N. S. Alvi and D. L. Kwong, "Reflow of Phosphosilicate
Glass by Rapid Thermal Annealing", *Journal of The Electrochemical
Society* **133**(12), 2626–2631 (1986).
<https://doi.org/10.1149/1.2108492> Reflow of PSG by rapid thermal
annealing. Used on step 092. Tier: deep dive.

**ARMSTRONG-1974** — W. E. Armstrong and D. L. Tolliver, "A Scanning
Electron Microscope Investigation of Glass Flow in MOS Integrated
Circuit Fabrication", *Journal of The Electrochemical Society*
**121**(2), 307 (1974). <https://doi.org/10.1149/1.2401803> The original
SEM study of PSG flow over MOS topography. Used on step 089. Tier: deep
dive.

**BECKER-ROHL-1987** — F. S. Becker and S. Röhl, "Low Pressure
Deposition of Doped SiO₂ by Pyrolysis of Tetraethylorthosilicate (TEOS):
I. Boron and Phosphorus Doped Films", *Journal of The Electrochemical
Society* **134**(11), 2923–2931 (1987).
<https://doi.org/10.1149/1.2100314> TEOS-based doped oxides by LPCVD.
Used on step 089. Tier: deep dive.

**BIBBY-1998** — T. Bibby and K. Holland, "Endpoint detection for CMP",
*Journal of Electronic Materials* **27**(10), 1073–1081 (1998).
<https://doi.org/10.1007/s11664-998-0140-1> Endpoint detection for CMP.
Used on steps 090, 100 and 106. Tier: deep dive.

**CHEN-2002-PSG** — S. Chen, C.-Y. Fu, S.-M. Jang, C.-H. Yu and M.-S.
Liang, "Plasma damage reduction for high density plasma CVD
phosphosilicate glass process", *Proc. 7th International Symposium on
Plasma- and Process-Induced Damage* (2002), pp. 76–79.
<https://doi.org/10.1109/PPID.2002.1042613> Plasma damage from an HDP
PSG process and its reduction. Used on step 089. Tier: deep dive.

**DAUBENSPECK-1991** — T. H. Daubenspeck, J. K. DeBrosse, C. W.
Koburger, M. Armacost and J. R. Abernathey, "Planarization of ULSI
Topography over Variable Pattern Densities", *Journal of The
Electrochemical Society* **138**(2), 506–509 (1991).
<https://doi.org/10.1149/1.2085619> Planarisation over variable pattern
densities. Used on steps 090 and 106. Tier: deep dive.

**DAVARI-1989** — B. Davari, C. W. Koburger, R. Schulz, J. D. Warnock,
T. Furukawa, M. Jost, Y. Taur, W. G. Schwittek, J. K. DeBrosse, M. L.
Kerbaugh and J. L. Mauer, "A new planarization technique, using a
combination of RIE and chemical mechanical polish (CMP)", *IEDM 1989
Technical Digest*, pp. 61–64. <https://doi.org/10.1109/IEDM.1989.74228>
RIE plus CMP planarisation of the inter-level dielectric. Used on steps
090 and 106. Tier: deep dive.

**FUJINO-1990** — K. Fujino, Y. Nishimoto, N. Tokumasu and K. Maeda,
"Silicon Dioxide Deposition by Atmospheric Pressure and Low-Temperature
CVD Using TEOS and Ozone", *Journal of The Electrochemical Society*
**137**(9), 2883–2887 (1990). <https://doi.org/10.1149/1.2087093>
TEOS/ozone oxide at atmospheric pressure. Used on step 091. Tier: deep
dive.

**FUJINO-1991** — K. Fujino, Y. Nishimoto, N. Tokumasu and K. Maeda,
"Doped Silicon Oxide Deposition by Atmospheric Pressure and Low
Temperature Chemical Vapor Deposition Using Tetraethoxysilane and
Ozone", *Journal of The Electrochemical Society* **138**(10), 3019–3024
(1991). <https://doi.org/10.1149/1.2085358> Doped oxide from TEOS and
ozone. Used on step 089. Tier: deep dive.

**HASHIMOTO-1977** — N. Hashimoto, Y. Yatsuda and S. Mutoh, "Glass Flow
Mechanism of Phosphosilicate Glass and Its Application in MOS Devices",
*Japanese Journal of Applied Physics* **16**(S1), 73 (1977).
<https://doi.org/10.7567/JJAPS.16S1.73> The glass-flow mechanism and its
use in MOS devices. Used on step 089. Tier: deep dive.

**HSIAO-2005** — W.-C. Hsiao, C.-P. Liu and Y.-L. Wang, "Influence of
thermal budget on phosphosilicate glass prepared by high-density plasma
chemical-vapor deposition", *Journal of Vacuum Science & Technology B*
**23**(5), 2146–2150 (2005). <https://doi.org/10.1116/1.2050670> HDP PSG
mechanism and thermal budget. Used on steps 089, 091 and 092. Tier: deep
dive.

**KERN-1991** — W. Kern and J. Hartman, "Simultaneous deposition and
fusion flow planarization of borophosphosilicate glass in a new chemical
vapor deposition reactor", *Thin Solid Films* **206**(1–2), 64–69
(1991). <https://doi.org/10.1016/0040-6090(91)90394-D> Simultaneous
deposition and flow of BPSG. Used on step 089. Tier: deep dive.

**KWOK-1994** — K. Kwok, E. Yieh, S. Robles and B. C. Nguyen, "Surface
Related Phenomena in Integrated PECVD/Ozone-TEOS SACVD Processes for
Sub-Half Micron Gap Fill: Electrostatic Effects", *Journal of The
Electrochemical Society* **141**(8), 2172–2177 (1994).
<https://doi.org/10.1149/1.2055081> Integrated PECVD/ozone-TEOS films
and their surface effects. Used on steps 091 and 105. Tier: deep dive.

**LAN-2004** — J. K. Lan and Y. L. Wang, "Mechanism of high density
plasma chemical vapor deposition phosphosilicate glass process without
in-situ plasma chamber clean", *Thin Solid Films* **469–470**, 438–443
(2004). <https://doi.org/10.1016/j.tsf.2004.06.193> HDP PSG mechanism
and thermal budget. Used on step 089. Tier: deep dive.

**LEVIN-1982** — R. M. Levin, "Water Absorption and Densification of
Phosphosilicate Glass Films", *Journal of The Electrochemical Society*
**129**(8), 1765–1770 (1982). <https://doi.org/10.1149/1.2124289> Water
absorption and densification of PSG films. Used on steps 089, 091, 092
and 096. Tier: deep dive.

**MAXIM-1994** — M. Maxim, M. Moinpour, J. Chu, H. Nguyen, P. Freiberger
and N. Stenton, "Borophosphosilicate Glass (BPSG) Fusion Using Rapid
Thermal Annealing and Steam Reflow: Physical Properties and Device
Implications", *MRS Proceedings* **342** (1994).
<https://doi.org/10.1557/PROC-342-289> BPSG fusion and implant
activation in one RTA. Used on step 092. Tier: deep dive.

**MEEK-1974** — R. L. Meek and C. F. Gibbon, "Preliminary Results of an
Ion Scattering Study of Phosphosilicate Glass Gettering", *Journal of
The Electrochemical Society* **121**(3), 444 (1974).
<https://doi.org/10.1149/1.2401834> PSG gettering studied by ion
scattering. Used on steps 089 and 092. Tier: deep dive.

**MIYAZAKI-1994** — H. Miyazaki, H. Kojima, A. Hiraiwa, Y. Homma and K.
Murakami, "Improved Phosphosilicate Glass Passivation Against Cu
Contamination Using the Rapid Thermal Annealing Process", *Journal of
The Electrochemical Society* **141**(3), 734–736 (1994).
<https://doi.org/10.1149/1.2054801> PSG as a barrier to copper
contamination. Used on steps 089 and 092. Tier: deep dive.

**NANZ-1995** — G. Nanz and L. E. Camilletti, "Modeling of
chemical-mechanical polishing: a review", *IEEE Transactions on
Semiconductor Manufacturing* **8**(4), 382–389 (1995).
<https://doi.org/10.1109/66.475179> The removal-rate law and a review of
CMP models. Used on steps 090 and 106. Tier: deep dive.

**NGUYEN-1990** — S. Nguyen, D. Dobuzinsky, D. Harmon, R. Gleason and S.
Fridmann, "Reaction Mechanisms of Plasma- and Thermal-Assisted Chemical
Vapor Deposition of Tetraethylorthosilicate Oxide Films", *Journal of
The Electrochemical Society* **137**(7), 2209–2215 (1990).
<https://doi.org/10.1149/1.2086914> Reaction mechanisms of plasma and
thermal TEOS oxide deposition. Used on steps 091 and 105. Tier: deep
dive.

**PAULSON-1974** — W. M. Paulson and R. W. Kirk, "The Effects of
Phosphorus-Doped Passivation Glass on the Corrosion of Aluminum", *12th
International Reliability Physics Symposium* (1974), pp. 172–179.
<https://doi.org/10.1109/IRPS.1974.362644> Phosphorus content and
aluminium corrosion. Used on steps 089 and 091. Tier: deep dive.

**THAR-1993** — R. P. S. Thar, F. Gonzalez, R. Hawthorne, V. Ward and N.
Jeng, "Reduced Thermal Budget Borophosphosilicate Glass (BPSG) Fusion
and Implant Activation Using Rapid Thermal Annealing and Steam Reflow",
*MRS Proceedings* **303** (1993). <https://doi.org/10.1557/PROC-303-283>
BPSG fusion and implant activation in one RTA. Used on step 092. Tier:
deep dive.


#### Local-interconnect contact lithography, etch, sacrificial etch and alloy (steps 093–096)

**BROWER-1990** — K. L. Brower, "Dissociation kinetics of
hydrogen-passivated (111) Si-SiO₂ interface defects", *Physical Review
B* **42**(6), 3444–3453 (1990).
<https://doi.org/10.1103/PhysRevB.42.3444> Dissociation kinetics of
hydrogen-passivated interface defects. Used on step 096. Tier: deep
dive.

**CHEN-1999-PSM** — Y.-T. Chen, Y.-C. Wang and R. Chu, "Optimization of
attenuated phase-shift mask for contact hole printing", *Proc. SPIE*
**3679**, Optical Microlithography XII, 812 (1999).
<https://doi.org/10.1117/12.354399> Attenuated PSM optimisation for
contact holes. Used on step 093. Tier: deep dive.

**COBB-1995** — N. B. Cobb and A. Zakhor, "Fast sparse aerial-image
calculation for OPC", *Proc. SPIE* **2621**, 534–545 (1995).
<https://doi.org/10.1117/12.228208> Rules-based, model-based and fast
aerial-image OPC. Used on steps 093 and 102. Tier: deep dive.

**DOEMLING-1996** — M. F. Doemling, N. R. Rueger and G. S. Oehrlein,
"Observation of inverse reactive ion etching lag for silicon dioxide
etching in inductively coupled plasmas", *Applied Physics Letters*
**68**(1), 10–12 (1996). <https://doi.org/10.1063/1.116772> Inverse RIE
lag. Used on steps 094 and 108. Tier: deep dive.

**FONASH-1990** — S. J. Fonash, "An Overview of Dry Etching Damage and
Contamination Effects", *Journal of The Electrochemical Society*
**137**(12), 3885–3892 (1990). <https://doi.org/10.1149/1.2086322> Etch
damage and contamination. Used on steps 094 and 095. Tier: deep dive.

**JOUBERT-1994** — O. Joubert, G. S. Oehrlein and M. Surendra,
"Fluorocarbon high density plasma. VI. Reactive ion etching lag model
for contact hole silicon dioxide etching in an electron cyclotron
resonance plasma", *Journal of Vacuum Science & Technology A* **12**(3),
665–670 (1994). <https://doi.org/10.1116/1.578850> RIE-lag model for
contact holes. Used on step 094. Tier: deep dive.

**MAES-1981** — H. E. Maes, S. H. Usmani and G. L. Heyns, "Effects of a
high-temperature hydrogen anneal on the memory retention of
metal-nitride-oxide-silicon transistors at elevated temperatures",
*Journal of Applied Physics* **52**(6), 4348–4350 (1981).
<https://doi.org/10.1063/1.329266> Hydrogen anneals and nitride-memory
retention. Used on step 096. Tier: deep dive.

**MORITA-1990** — M. Morita, T. Ohmi, E. Hasegawa, M. Kawakami and M.
Ohwada, "Growth of native oxide on a silicon surface", *Journal of
Applied Physics* **68**(3), 1272–1281 (1990).
<https://doi.org/10.1063/1.347181> Native oxide regrowth on silicon, the
queue-time constraint. Used on steps 095 and 096. Tier: deep dive.

**OEHRLEIN-1994-II** — G. S. Oehrlein, Y. Zhang, D. Vender and O.
Joubert, "Fluorocarbon high-density plasmas. II. Silicon dioxide and
silicon etching using CF₄ and CHF₃", *Journal of Vacuum Science &
Technology A* **12**(2), 333–344 (1994).
<https://doi.org/10.1116/1.578877> Fluorocarbon films in high-density
oxide etching. Used on step 094. Label ↔ key: the same article is cited
as `oehrlein-1994b` on step 108 (OEHRLEIN-1994B). Tier: deep dive.

**PANKOVE-1983** — J. I. Pankove, D. E. Carlson, J. E. Berkeyheiser and
R. O. Wance, "Neutralization of Shallow Acceptor Levels in Silicon by
Atomic Hydrogen", *Physical Review Letters* **51**(24), 2224–2225
(1983). <https://doi.org/10.1103/PhysRevLett.51.2224> Hydrogen
deactivation of boron, the side-effect that bounds the recipe. Used on
step 096. Tier: deep dive.

**RANGAN-1998** — S. Rangan, S. Krishnan and S. Ashok, "Process-induced
damage — a study of hydrogen and deuterium passivation", *Proc. 1998 3rd
International Symposium on Plasma Process-Induced Damage*, pp. 213–216.
<https://doi.org/10.1109/PPID.1998.725612> Hydrogen and deuterium
passivation of process-induced damage. Used on step 096. Tier: deep
dive.

**RUEGER-1997** — N. R. Rueger, J. J. Beulens, M. Schaepkens, M. F.
Doemling, J. M. Mirza, T. E. F. M. Standaert and G. S. Oehrlein, "Role
of steady state fluorocarbon films in the etching of silicon dioxide
using CHF₃ in an inductively coupled plasma reactor", *Journal of Vacuum
Science & Technology A* **15**(4), 1881–1889 (1997).
<https://doi.org/10.1116/1.580655> Fluorocarbon films in high-density
oxide etching. Used on step 094. Tier: deep dive.

**SAH-1983** — C.-T. Sah, J. Y.-C. Sun and J. J.-T. Tzou, "Deactivation
of the boron acceptor in silicon by hydrogen", *Applied Physics Letters*
**43**(2), 204–206 (1983). <https://doi.org/10.1063/1.94287> Hydrogen
deactivation of boron, the side-effect that bounds the recipe. Used on
step 096. Tier: deep dive.

**SCHAEPKENS-1999** — M. Schaepkens, T. E. F. M. Standaert, N. R.
Rueger, P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "Study of the
SiO₂-to-Si₃N₄ etch selectivity mechanism in inductively coupled
fluorocarbon plasmas and a comparison with the SiO₂-to-Si mechanism",
*Journal of Vacuum Science & Technology A* **17**(1), 26–37 (1999).
<https://doi.org/10.1116/1.582108> The SiO₂-to-Si₃N₄ selectivity
mechanism. Used on steps 094, 104 and 108. Tier: deep dive.

**STESMANS-1996** — A. Stesmans, "Passivation of P_b0 and P_b1 interface
defects in thermal (100) Si/SiO₂ with molecular hydrogen", *Applied
Physics Letters* **68**(15), 2076–2078 (1996).
<https://doi.org/10.1063/1.116308> Passivation of P_b0 and P_b1 centres
by molecular hydrogen. Used on step 096. Tier: deep dive.

**YANG-1998** — C.-H. Yang and C.-M. Dai, "Resist and oxide thickness
effect on process window for 0.2-μm contact patterns with off-axis
illumination and attenuated phase-shift mask", *Proc. SPIE* **3334**,
Optical Microlithography XI, 553 (1998).
<https://doi.org/10.1117/12.310784> Process window of 0.2 µm contacts
with OAI and attenuated PSM. Used on step 093. Tier: deep dive.


#### Ti/TiN liner, contact silicide, tungsten fill and LI tungsten CMP (steps 097–100)

**BERG-2005** — S. Berg and T. Nyberg, "Fundamental understanding and
modeling of reactive sputtering processes", *Thin Solid Films*
**476**(2), 215–230 (2005). <https://doi.org/10.1016/j.tsf.2004.10.051>
Reactive sputtering model and hysteresis. Used on steps 097, 101 and
109. Tier: deep dive.

**BIELMANN-1999** — M. Bielmann et al., "Effect of Particle Size during
Tungsten Chemical Mechanical Polishing", *Electrochemical and
Solid-State Letters* **2**(8), 401 (1999).
<https://doi.org/10.1149/1.1390851> Particle size in tungsten CMP. Used
on step 100. Tier: deep dive.

**ELBEL-1998** — N. Elbel, B. Neureither, B. Ebersberger and P. Lahnor,
"Tungsten Chemical Mechanical Polishing", *Journal of The
Electrochemical Society* **145**(5), 1659–1664 (1998).
<https://doi.org/10.1149/1.1838533> Tungsten chemical mechanical
polishing. Used on steps 100, 110 and 111. Tier: deep dive.

**HOPWOOD-1998** — J. Hopwood, "Ionized physical vapor deposition of
integrated circuit interconnects", *Physics of Plasmas* **5**(5),
1624–1631 (1998). <https://doi.org/10.1063/1.872829> Ionised PVD for
interconnects. Used on step 097. Tier: deep dive.

**KIM-2004** — S.-H. Kim, E.-S. Hwang, S.-Y. Han, S.-H. Pyi, N. Kwak, H.
Sohn, J. Kim and G. B. Choi, "Pulsed CVD of Tungsten Thin Film as a
Nucleation Layer for Tungsten Plug-Fill", *Electrochemical and
Solid-State Letters* **7**(9), G195 (2004).
<https://doi.org/10.1149/1.1784053> Pulsed CVD tungsten nucleation for
plug fill. Used on step 099. Tier: deep dive.

**KLEIJN-1991** — C. R. Kleijn, C. J. Hoogendoorn, A. Hasper, J.
Holleman and J. Middelhoek, "Transport Phenomena in Tungsten LPCVD in a
Single-Wafer Reactor", *Journal of The Electrochemical Society*
**138**(2), 509–517 (1991). <https://doi.org/10.1149/1.2085620>
Transport phenomena in a single-wafer tungsten reactor. Used on step
099. Tier: deep dive.

**KOERNER-1993** — H. Koerner, H. P. Erb and H. Melzner, "Evaluation of
Ti and TiN thicknesses for tungsten plug contact metallization",
*Applied Surface Science* **73**, 6–13 (1993).
<https://doi.org/10.1016/0169-4332(93)90139-3> Ti and TiN thicknesses
for tungsten-plug contacts. Used on steps 097, 098 and 099. Tier: deep
dive.

**LEE-2001-WCMP** — W.-S. Lee, S.-Y. Kim, Y.-J. Seo and J.-K. Lee, "An
optimization of tungsten plug chemical mechanical polishing (CMP) using
different consumables", *Journal of Materials Science: Materials in
Electronics* **12**(1), 63–68 (2001).
<https://doi.org/10.1023/A:1011276830620> Plug CMP optimisation across
consumables. Used on step 100. Tier: deep dive.

**MANN-1995** — R. W. Mann, L. A. Clevenger, P. D. Agnello and F. R.
White, "Silicides and local interconnections for high-performance VLSI
applications", *IBM Journal of Research and Development* **39**(4),
403–417 (1995). <https://doi.org/10.1147/rd.394.0403> Silicides and
local interconnections together. Used on steps 098 and 101. Tier: deep
dive.

**MCCONICA-1986** — C. M. McConica and K. Krishnamani, "The Kinetics of
LPCVD Tungsten Deposition in a Single Wafer Reactor", *Journal of The
Electrochemical Society* **133**(12), 2542–2548 (1986).
<https://doi.org/10.1149/1.2108468> Kinetics of LPCVD tungsten in a
single-wafer reactor. Used on steps 099 and 110. Tier: deep dive.

**MCCONICA-1988** — C. M. McConica and K. Cooper, "Tungsten Nucleation
on Thermal Oxide during LPCVD of Tungsten by the Hydrogen Reduction of
Tungsten Hexafluoride", *Journal of The Electrochemical Society*
**135**(4), 1003–1008 (1988). <https://doi.org/10.1149/1.2095756>
Tungsten nucleation on thermal oxide. Used on steps 099 and 110. Tier:
deep dive.

**MORGAN-1985** — A. E. Morgan, E. K. Broadbent and A. H. Reader,
"Formation of Titanium Nitride/Silicide Bilayers by Rapid Thermal Anneal
in Nitrogen", *MRS Proceedings* **52** (1985).
<https://doi.org/10.1557/PROC-52-279> TiN/TiSi₂ bilayers by RTA in
nitrogen. Used on step 098. Tier: deep dive.

**NICOLET-1978** — M.-A. Nicolet, "Diffusion barriers in thin films",
*Thin Solid Films* **52**(3), 415–443 (1978).
<https://doi.org/10.1016/0040-6090(78)90184-0> Diffusion barriers in
microelectronics in general. Used on step 097. Tier: deep dive.

**OHTO-1996** — K. Ohto, K. Urabe, T. Taguwa, S. Chikaki and T. Kikkawa,
"A novel TiN/Ti contact plug technology for gigabit scale DRAM using
Ti-PECVD and TiN-LPCVD", *IEDM 1996 Technical Digest*, pp. 361–364.
<https://doi.org/10.1109/IEDM.1996.553603> A TiN/Ti contact-plug
technology. Used on step 098. Tier: deep dive.

**PAT-PNL-NOVELLUS** — S.-H. Lee and J. Collins (Novellus Systems),
*Method for producing ultra-thin tungsten layers with improved step
coverage*, US 6,635,965 B1, filed 2001-10-09, granted 2003-10-21.
<https://patents.google.com/patent/US6635965B1/en> The pulsed nucleation
layer. Used on steps 099 and 110. Tier: cross-check.

**PETRI-1998** — R. Petri, H. Hauf, D. Berenbaum, J. C. Favreau and P.
Mazet, "Nitrogen effect on post-nucleation tungsten CVD film growth",
*Proc. IEEE 1998 International Interconnect Technology Conference*, pp.
202–204. <https://doi.org/10.1109/IITC.1998.704792> Nitrogen and
post-nucleation tungsten growth. Used on step 099. Tier: deep dive.

**PETROV-2003** — I. Petrov, P. B. Barna, L. Hultman and J. E. Greene,
"Microstructural evolution during film growth", *Journal of Vacuum
Science & Technology A* **21**(5), S117–S128 (2003).
<https://doi.org/10.1116/1.1601610> Microstructural evolution during
film growth. Used on steps 097 and 101. Tier: deep dive.

**ROSSNAGEL-1991** — S. M. Rossnagel, D. Mikalsen, H. Kinoshita and J.
J. Cuomo, "Collimated magnetron sputter deposition", *Journal of Vacuum
Science & Technology A* **9**(2), 261–265 (1991).
<https://doi.org/10.1116/1.577531> Collimated magnetron sputter
deposition. Used on steps 097, 109 and 112. Tier: deep dive.

**ROSSNAGEL-1993** — S. M. Rossnagel and J. Hopwood, "Magnetron sputter
deposition with high levels of metal ionization", *Applied Physics
Letters* **63**(24), 3285–3287 (1993).
<https://doi.org/10.1063/1.110176> Ionised magnetron sputtering and
metal-ion deposition. Used on steps 097 and 109. Tier: deep dive.

**RYAN-1995** — J. G. Ryan, S. B. Brodsky, T. Katata, M. Honda, N. Shoda
and H. Aochi, "Collimated Sputtering of Titanium and Titanium Nitride
Films", *MRS Bulletin* **20**(11), 42–45 (1995).
<https://doi.org/10.1557/S0883769400045553> Collimated sputtering of Ti
and TiN. Used on step 097. Tier: deep dive.

**SCHRODER-1984** — D. K. Schroder and D. L. Meier, "Solar cell contact
resistance — A review", *IEEE Transactions on Electron Devices*
**31**(5), 637–647 (1984). <https://doi.org/10.1109/T-ED.1984.21583>
Contact-resistance models and measurement. Used on step 098. Tier: deep
dive.

**SRINIVAS-1992** — D. Srinivas, R. Foster, S. Marcus, R. Arora and H.
Rebenne, "Nucleation of Tungsten on Titanium Nitride with Hydrogen
Reduction of Tungsten Hexafluoride", *MRS Proceedings* **282** (1992).
<https://doi.org/10.1557/PROC-282-365> Tungsten nucleation on TiN. Used
on steps 097, 099, 109 and 110. Tier: deep dive.

**SUE-1999** — L. Sue, J. Lültzen and S. Gonzales, "Tungsten Chemical
Mechanical Polishing Endpoint Detection", *MRS Proceedings* **566**, 109
(1999). <https://doi.org/10.1557/PROC-566-109> Tungsten CMP endpoint
detection. Used on steps 100 and 111. Tier: deep dive.

**SUNDGREN-1985** — J.-E. Sundgren, "Structure and properties of TiN
coatings", *Thin Solid Films* **128**(1–2), 21–44 (1985).
<https://doi.org/10.1016/0040-6090(85)90333-5> Structure and properties
of TiN coatings. Used on steps 097, 101 and 109. Tier: deep dive.

**TRIPATHI-1994** — S. Tripathi and F. Moghadam, "Development of a
Silane Rich CVD Tungsten Process", *MRS Proceedings* **337** (1994).
<https://doi.org/10.1557/PROC-337-561> A silane-rich CVD tungsten
process. Used on step 099. Tier: deep dive.

**VARAHRAMYAN-1996** — K. Varahramyan and E. J. Verret, "A model for
specific contact resistance applicable for titanium silicide-silicon
contacts", *Solid-State Electronics* **39**(11), 1601–1607 (1996).
<https://doi.org/10.1016/0038-1101(96)00091-3> Specific contact
resistance of TiSi₂–silicon contacts. Used on step 098. Tier: deep dive.

**WANG-2002-WCMP** — C.-K. Wang, H.-S. Wu, N.-T. Ou and H.-C. Cheng,
"Integrated Tungsten Chemical Mechanical Polishing Process
Characterization for Via Plug Interconnection in Ultralarge Scale
Integrated Circuits", *Japanese Journal of Applied Physics* **41**(8R),
5120–5124 (2002). <https://doi.org/10.1143/JJAP.41.5120> Integrated
tungsten CMP for via plugs. Used on step 100. Tier: deep dive.

**WITTMER-1980** — M. Wittmer, "TiN and TaN as diffusion barriers in
metallizations to silicon semiconductor devices", *Applied Physics
Letters* **36**(6), 456–458 (1980). <https://doi.org/10.1063/1.91505>
TiN as a diffusion barrier. Used on step 097. Tier: deep dive.

**YOO-1999** — W. S. Yoo, A. J. Atanos and D. M. Whitworth, "Titanium
Silicide Formation and Anneal Using a Susceptor-Based Low Pressure Rapid
Thermal Processing System", *Japanese Journal of Applied Physics*
**38**(3B), L304 (1999). <https://doi.org/10.1143/JJAP.38.L304> TiSi₂
formation in a low-pressure RTP system. Used on step 098. Tier: deep
dive.


#### Local-interconnect TiN, mask, etch and nitride cap (steps 101–104)

**BELL-1988** — H. B. Bell, H. M. Anderson and R. W. Light, "Reactive
Ion Etching of Aluminum/Silicon in BBr₃/Cl₂ and BCl₃/Cl₂ Mixtures",
*Journal of The Electrochemical Society* **135**(5), 1184–1191 (1988).
<https://doi.org/10.1149/1.2095919> Reactive ion etching in BCl₃/Cl₂
mixtures. Used on step 103. Tier: deep dive.

**BOUMERZOUG-1997** — M. Boumerzoug, H. Xu, R. Bersin, P. Mascher and G.
Balcaitis, "Removal of Titanium Oxide Grown on Titanium Nitride and
Reduction of VIA Contact Resistance using a Modern Plasma Asher", *MRS
Proceedings* **495** (1997). <https://doi.org/10.1557/PROC-495-345>
Oxide on TiN and via contact resistance. Used on step 101. Tier: deep
dive.

**LIAO-2004** — H. Liao, P. S. Lee, L. N. L. Goh, H. Liu, J. L.
Sudijono, Q. Elgin and C. Sanford, "The impact of etch-stop layer for
borderless contacts on deep submicron CMOS device performance — a
comparative study", *Thin Solid Films* **462–463**, 29–33 (2004).
<https://doi.org/10.1016/j.tsf.2004.05.035> Etch-stop layers for
borderless contacts and device performance. Used on step 104. Tier: deep
dive.

**MIN-2008** — S. R. Min, H. N. Cho, Y. L. Li, S. K. Lim, S. P. Choi and
C. W. Chung, "Inductively coupled plasma reactive ion etching of
titanium nitride thin films in a Cl₂/Ar plasma", *Journal of Industrial
and Engineering Chemistry* **14**(3), 297–302 (2008).
<https://doi.org/10.1016/j.jiec.2008.01.001> TiN etching in a Cl₂/Ar
inductively coupled plasma. Used on step 103. Tier: deep dive.

**PAT-LI-TI-HAKEN** — R. A. Haken and T. C. Holloway (Texas
Instruments), *VLSI local interconnect structure*, US 4,821,085 A, filed
1985-05-01, granted 1989-04-11.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4821085>
The VLSI local interconnect structure. Used on step 101. Tier: deep
dive.

**PAT-LI-TI-HOLLOWAY** — T. C. Holloway, T. E. Tang, C.-C. Wei, R. A.
Haken and D. A. Bell (Texas Instruments), *Process for patterning local
interconnects*, US 4,657,628 A, filed 1986-03-07, granted 1987-04-14.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4657628>
The process for patterning local interconnects. Used on steps 101 and
103. Tier: deep dive.

**PAT-TIN-ETCH-TI** — M. A. Douglas (Texas Instruments), *TiN etch
process*, US 4,675,073 A, filed 1986-03-07, granted 1987-06-23.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4675073>
A fluorine-deficient plasma etch of TiN selective to titanium silicide.
Used on step 103. Tier: deep dive.

**WHITE-1992** — White, Hill, Eslinger, Payne, Cote, Chen and Johnson,
"Damascene stud local interconnect in CMOS technology", *IEDM 1992
Technical Digest*, pp. 301–304.
<https://doi.org/10.1109/IEDM.1992.307365> A damascene-stud local
interconnect, the alternative structure. Used on step 101. Tier: deep
dive.


#### ILD2 oxide and CMP over local interconnect (steps 105–106)


#### Metal contact mask, etch, TiN liner, tungsten fill and CMP (steps 107–111)

**COBURN-1989** — J. W. Coburn and H. F. Winters, "Conductance
considerations in the reactive ion etching of high aspect ratio
features", *Applied Physics Letters* **55**(26), 2730–2732 (1989).
<https://doi.org/10.1063/1.101937> Conductance limits in
high-aspect-ratio feature etching. Used on step 108. Tier: deep dive.

**FUKUDA-1987** — H. Fukuda, N. Hasegawa, T. Tanaka and T. Hayashida, "A
new method for enhancing focus latitude in optical lithography: FLEX",
*IEEE Electron Device Letters* **8**(4), 179–180 (1987).
<https://doi.org/10.1109/EDL.1987.26594> FLEX, the focus-latitude
enhancement used for contact holes. Used on step 107. Tier: deep dive.

**HAMAGUCHI-1996** — S. Hamaguchi and S. M. Rossnagel, "Liner
conformality in ionized magnetron sputter metal deposition processes",
*Journal of Vacuum Science & Technology B* **14**(4), 2603–2608 (1996).
<https://doi.org/10.1116/1.588993> Liner conformality in ionised
sputtering, modelled. Used on step 109. Tier: deep dive.

**HEGDE-1997** — R. I. Hegde, P. J. Tobin, S. Sitaram and J. Klein,
"Thin Film Properties of Tungsten Nucleation Layer in Blanket Tungsten
Deposition", *Journal of The Electrochemical Society* **144**(3),
1087–1090 (1997). <https://doi.org/10.1149/1.1837536> Properties of the
nucleation layer in blanket tungsten deposition. Used on step 110. Tier:
deep dive.

**HOPWOOD-1992** — J. Hopwood, "Review of inductively coupled plasmas
for plasma processing", *Plasma Sources Science and Technology*
**1**(2), 109–116 (1992). <https://doi.org/10.1088/0963-0252/1/2/006>
The inductively coupled plasma sources behind IMP. Used on step 109.
Tier: deep dive.

**JOLLEY-1998** — R. Jolley, "Applications of Tetramethylammoninium
Hydroxide (TMAH) as a Post Tungsten CMP Cleaning Mixture", *Solid State
Phenomena* **65–66**, 105–108 (1998).
<https://doi.org/10.4028/www.scientific.net/SSP.65-66.105> TMAH as a
post-tungsten-CMP clean. Used on step 111. Tier: deep dive.

**KNEER-1997** — E. A. Kneer, C. Raghunath, V. Mathew, S. Raghavan and
J. S. Jeon, "Electrochemical Measurements during the Chemical Mechanical
Polishing of Tungsten Thin Films", *Journal of The Electrochemical
Society* **144**(9), 3041–3049 (1997).
<https://doi.org/10.1149/1.1837956> Electrochemistry of tungsten during
polishing. Used on step 111. Tier: deep dive.

**LEVY-1986** — R. A. Levy and M. L. Green, "Low Pressure Chemical Vapor
Deposition of Tungsten and Aluminum for VLSI Applications", *MRS
Proceedings* **71** (1986). <https://doi.org/10.1557/PROC-71-229> LPCVD
tungsten and aluminium for VLSI. Used on step 110. Tier: deep dive.

**LU-1999** — P. Lu, W. Cui, R. Thomas and S. Mansfield, "Selection of
attenuated phase shift mask compatible contact hole resists for KrF
optical lithography", *Proc. SPIE* **3678**, Advances in Resist
Technology and Processing XVI, 923 (1999).
<https://doi.org/10.1117/12.350280> Choosing contact-hole resists
compatible with an attenuated PSM at KrF. Used on step 107. Tier: deep
dive.

**MAO-2004** — D. Mao and J. Hopwood, "Ionized physical vapor deposition
of titanium nitride: A deposition model", *Journal of Applied Physics*
**96**(1), 820–828 (2004). <https://doi.org/10.1063/1.1753663> A
deposition model for ionised PVD of titanium nitride. Used on step 109.
Tier: deep dive.

**OEHRLEIN-1994B** — G. S. Oehrlein, Y. Zhang, D. Vender and O. Joubert,
"Fluorocarbon high-density plasmas. II. Silicon dioxide and silicon
etching using CF₄ and CHF₃", *Journal of Vacuum Science & Technology A*
**12**(2), 333–344 (1994). <https://doi.org/10.1116/1.578877> Oxide and
silicon etching in CF₄/CHF₃ high-density plasmas. Used on step 108.
Label ↔ key: the same article is cited as `oehrlein-1994-ii` on step 094
(OEHRLEIN-1994-II). Tier: deep dive.

**PAT-CMP-CABOT** — Cabot Corporation, *Composition and slurry useful
for metal CMP*, US 5,958,288 A, filed 1996-11-26, granted 1999-09-28.
<https://patents.google.com/patent/US5958288A/en> A
peroxide/ferric-catalyst tungsten slurry. Used on step 111. Tier:
cross-check.

**PAT-HCM-NOVELLUS** — K. F. Lai et al. (Novellus Systems), *Apparatus and
method for controlling plasma uniformity across a substrate*, US
6,179,973 B1, filed 1999-06-30, granted 2001-01-30.
<https://patents.google.com/patent/US6179973B1/en> The
hollow-cathode-magnetron ionised PVD source, a competing design. Used on
step 109. Tier: deep dive.

**PERRY-2001** — W. L. Perry, K. Waters, M. Barela and H. M. Anderson,
"Oxide etch behavior in a high-density, low-pressure, inductively coupled
C₂F₆ plasma: Etch rates, selectivity to photoresist, plasma parameters,
and CFx radical densities", *Journal of Vacuum Science & Technology A*
**19**(5), 2272–2281 (2001). <https://doi.org/10.1116/1.1382874> Oxide
etch rates and selectivity in a high-density C₂F₆ plasma. Used on steps
108, 119, 130 and 145. Tier: deep dive.

**SHIOYA-1987** — Y. Shioya, T. Ikegami, M. Maeda and K. Yanagida,
"High-temperature stress measurement on chemical-vapor-deposited
tungsten silicide and tungsten films", *Journal of Applied Physics*
**61**(2), 561–566 (1987). <https://doi.org/10.1063/1.338259> Stress of
CVD tungsten films at temperature. Used on step 110. Tier: deep dive.

**SOCHA-2004** — R. Socha, D. Van Den Broeke, S. Hsu, J. F. Chen et al.,
"Contact hole reticle optimization by using interference mapping
lithography (IML)", *Proc. SPIE* **5377**, Optical Microlithography
XVII, 222 (2004). <https://doi.org/10.1117/12.536581> Contact-hole
reticle optimisation with assist features by interference mapping. Used
on step 107. Tier: deep dive.

**STEIN-1998** — D. Stein, D. Hetherington, T. Guilinger and J. L.
Cecchi, "In Situ Electrochemical Investigation of Tungsten
Electrochemical Behavior during Chemical Mechanical Polishing", *Journal
of The Electrochemical Society* **145**(9), 3190–3196 (1998).
<https://doi.org/10.1149/1.1838785> In-situ electrochemistry of tungsten
during CMP. Used on step 111. Tier: deep dive.

**TOYOSHIMA-1998** — T. Toyoshima, T. Ishibashi, T. Minanide, K. Sugino
et al., "0.1 μm level contact hole pattern formation with KrF
lithography by resolution enhancement lithography assisted by chemical
shrink (RELACS)", *IEDM 1998 Technical Digest*, pp. 333–336.
<https://doi.org/10.1109/IEDM.1998.746367> Chemical shrink (RELACS) for
0.1 µm-class holes with KrF. Used on step 107. Tier: deep dive.

**VLASSAK-2001** — J. J. Vlassak, "A Contact-Mechanics Based Model for
Dishing and Erosion in Chemical-Mechanical Polishing", *MRS Proceedings*
**671**, M4.6 (2001). <https://doi.org/10.1557/PROC-671-M4.6> A
contact-mechanics model of dishing and erosion. Used on step 111. Tier:
deep dive.

**WITTMER-1985** — M. Wittmer, "Properties and microelectronic
applications of thin films of refractory metal nitrides", *Journal of
Vacuum Science & Technology A* **3**(4), 1797–1803 (1985).
<https://doi.org/10.1116/1.573382> Refractory-metal nitrides as barriers
in microelectronics. Used on step 109. Tier: deep dive.

**WODECKI-1999** — N. Wodecki, "Low open area multilayered dielectric
film etch endpoint detection using EndPoint Plus", *Proc. SPIE*
**3882**, Process, Equipment, and Materials Control in Integrated
Circuit Manufacturing V, 231 (1999). <https://doi.org/10.1117/12.361313>
Endpoint detection on low-open-area dielectric etches. Used on step 108.
Tier: deep dive.

**WONG-2001** — A. K.-K. Wong, *Resolution Enhancement Techniques in
Optical Lithography*, SPIE Tutorial Texts TT47, SPIE Press, 2001, ISBN
978-0-8194-7881-8. <https://doi.org/10.1117/3.401208> The SPIE text on
PSM, OPC and off-axis illumination. Used on steps 107 and 113. Tier:
deep dive.

**YAMAMOTO-2000** — K. Yamamoto, S. Kobayashi, T. Uno and T. Kotani,
"Hierarchical optical proximity correction on contact hole layers",
*Digest of Papers, Microprocesses and Nanotechnology 2000*, pp. 40–41.
<https://doi.org/10.1109/IMNC.2000.872612> Hierarchical OPC on
contact-hole layers. Used on step 107. Tier: deep dive.


#### Metal-1 stack, mask, etch, ILD3, CMP and cap oxide (steps 112–117)

**BONING-1994** — D. S. Boning, T. Maung, J. E. Chung, K.-J. Chang,
S.-Y. Oh and D. Bartelink, "Statistical metrology for interlevel
dielectric thickness variation", *Proc. SPIE* **2334**, Advanced
Microelectronic Manufacturing, 316–327 (1994).
<https://doi.org/10.1117/12.186764> Statistical metrology of ILD
thickness variation. Used on steps 116 and 117. Tier: deep dive.

**BYUN-2005** — K.-M. Byun, D.-H. Kim, Y.-W. Cha, S.-H. Lee et al.,
"Reduction of plasma-induced damage during intermetal dielectric
deposition in high-density plasma", *Proc. 2005 International Conference
on Integrated Circuit Design and Technology (ICICDT)*, pp. 99–102.
<https://doi.org/10.1109/ICICDT.2005.1502601> Reducing plasma damage
during HDP inter-metal dielectric deposition. Used on step 115. Tier:
deep dive.

**CHANG-1995** — E. Chang, B. Stine, T. Maung, R. Divecha, D. Boning, J.
Chung, K. Chang, G. Ray, D. Bradbury, O. S. Nakagawa, S. Oh and D.
Bartelink, "Using a statistical metrology framework to identify
systematic and random sources of die- and wafer-level ILD thickness
variation in CMP processes", *IEDM 1995 Technical Digest*, pp. 499–502.
<https://doi.org/10.1109/IEDM.1995.499247> Statistical metrology of ILD
thickness variation. Used on steps 116 and 117. Tier: deep dive.

**CHAUDHARI-1974** — P. Chaudhari, "Hillock growth in thin films",
*Journal of Applied Physics* **45**(10), 4339–4346 (1974).
<https://doi.org/10.1063/1.1663054> Hillock growth in thin films. Used
on step 115. Tier: deep dive.

**CHEN-1989** — C.-H. Chen, S. DeOrnellas and B. Burke, "Plasma Etching
of Aluminum Alloys in BCl₃/Cl₂ Plasmas", in *Semiconductor Fabrication:
Technology and Metrology*, ASTM STP 990, ASTM International, 1989, pp.
202–211. <https://doi.org/10.1520/STP26039S> Plasma etching of aluminium
alloys in BCl₃/Cl₂. Used on step 114. Tier: deep dive.

**CHENG-2002** — M. Cheng and A. R. Neureuther, "Effects of residual
aberrations on line-end shortening in 193-nm lithography", *Proc. SPIE*
**4691**, Optical Microlithography XV, 1421 (2002).
<https://doi.org/10.1117/12.474526> Line-end shortening from residual
aberrations. Used on step 113. Tier: deep dive.

**CHUN-1996** — J.-S. Chun, C.-K. Bok and K.-H. Baik, "Reduction of
substrate dependency of chemically amplified resist", *Proc. SPIE*
**2724**, Advances in Resist Technology and Processing XIII, 92 (1996).
<https://doi.org/10.1117/12.241877> The substrate effect in chemically
amplified resists and its reduction. Used on step 113. Tier: deep dive.

**COOPERBERG-2002** — D. J. Cooperberg, V. Vahedi and R. A. Gottscho,
"Semiempirical profile simulation of aluminum etching in a Cl₂/BCl₃
plasma", *Journal of Vacuum Science & Technology A* **20**(5), 1536–1556
(2002). <https://doi.org/10.1116/1.1494818> Profile simulation of
aluminium etching in Cl₂/BCl₃. Used on step 114. Tier: deep dive.

**CYP-PIN145273** — Cypress Semiconductor, *Product Information
Notification PIN145273: Improvement of Cypress Minnesota
Back-End-of-Line Integration for 130nm SONOS Product Families*, document
001-11741 Rev. *H, 2014-03-13 (copy hosted by Tokyo Electron Device).
<https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>
The product-change notification that carries the QTP 123907 report and
describes the TiW-based stack as Cypress's Minnesota process. Used on
steps 112 and 123. Tier: cross-check.

**CYP-QTP-014807** — Cypress Semiconductor, *Technology Derivative
Qualification Report, QTP# 014807 Version 2.0: Technology Derivative
R7FT-3R, Fab4, Synchronous Dual-Port RAM*, June 2005 (copy hosted by
Infineon Technologies).
<https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
R7FT-3R "Hot Al" derivative at Fab 4: 150 Å Ti / 4 200 Å Al / 300 Å TiW.
Used on steps 112 and 117. Tier: cross-check.

**CYP-QTP-030204** — Cypress Semiconductor, *Automotive Product
Qualification Report, QTP# 030204: 256K Static RAM Automotive Devices,
RAM42HA Technology, Fab 4*, document 001-88023 Rev. **, June 2013 (copy
hosted by Infineon Technologies).
<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030204-256k-static-ram-automotive-devices-ram42ha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714980870ac1>
RAM42HA at Fab 4: TiW/AlCu/TiW 500/6 000/300 Å. Used on step 112. Tier:
cross-check.

**CYP-QTP-113005** — Cypress Semiconductor, *Product Qualification Plan,
QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8 Technology,
CMI (Fab 4)*, document 001-85611 Rev. *A, January 2013 (copy hosted by
Infineon Technologies).
<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
S8TNV-5R metal composition at Bloomington: Metal 1 "100A Ti / 3200A
Al-0.5%Cu / 300A TiW", Metal 2 the same, Metal 3 "150A Ti / 7200A
Al-0.5%Cu / 300A TiW". Used on steps 112–114, 118–121, 123–125,
129–132, 134, 136, 138–141, 145 and 146 and on the etch category page.
Tier: cross-check.

**CYP-QTP-123907** — Cypress Semiconductor, *Fab Process Qualification
Report, QTP# 123907, 132302, 132301: Metal Stack Change, S8 Technology,
Fab 4 CMI*, document 001-91369 Rev. **, March 2014 (copy hosted by Tokyo
Electron Device as the attachment to Cypress Product Information
Notification PIN145273, 2014-03-13, which states the report is attached
and available from cypress.com;
<https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>).
<https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/145273-Qualification_Report.pdf>
S8 "Metal Stack Change from Ti/AlCu/TiW to Ti/TiN/AlCu/Ti/TiN in CMI Fab
4". Used on steps 112 and 117. Tier: cross-check.

**DALTON-1990** — C. M. Dalton, "Enhanced selective tungsten
encapsulation of TiW capped aluminum interconnect", *Proc. Seventh
International IEEE VLSI Multilevel Interconnection Conference (VMIC
1990)*, pp. 289–295. <https://doi.org/10.1109/VMIC.1990.127879> A
TiW-capped aluminium interconnect. Used on step 112. Tier: deep dive.

**DENISON-1996** — D. R. Denison, J. C. Barbour and J. H. Burkhart, "Low
dielectric constant, fluorine-doped SiO₂ for intermetal dielectric",
*Journal of Vacuum Science & Technology A* **14**(3), 1124–1126 (1996).
<https://doi.org/10.1116/1.580280> Fluorine-doped SiO₂ as a
low-permittivity inter-metal dielectric. Used on step 115. Tier: deep
dive.

**DEVRIENDT-1998** — K. Devriendt, E. Vrancken, N. Heylen, J. Grillaert,
M. Meuris, M. M. Heyns and Z. C. Lin, "Relation between Oxide-CMP
Induced Defects and Post-CMP Cleaning Strategies", *Solid State
Phenomena* **65–66**, 173–176 (1998).
<https://doi.org/10.4028/www.scientific.net/SSP.65-66.173> Oxide-CMP
defects versus post-CMP cleaning. Used on steps 116 and 117. Tier: deep
dive.

**DOMENICUCCI-1996** — A. G. Domenicucci, R. G. Filippi, K. W. Choi,
C.-K. Hu and K. P. Rodbell, "Effect of copper on the microstructure and
electromigration lifetime of Ti–AlCu–Ti fine lines in the presence of
tungsten diffusion barriers", *Journal of Applied Physics* **80**(9),
4952–4959 (1996). <https://doi.org/10.1063/1.363539> Ti–AlCu–Ti lines
over tungsten: copper, microstructure and lifetime. Used on step 112.
Tier: deep dive.

**FANG-1992** — S. Fang and J. P. McVittie, "Thin-oxide damage from gate
charging during plasma processing", *IEEE Electron Device Letters*
**13**(5), 288–290 (1992). <https://doi.org/10.1109/55.145056>
Thin-oxide damage from gate charging during plasma processing. Used on
step 114. Tier: deep dive.

**FISCHL-1987** — D. S. Fischl and D. W. Hess, "Plasma-Enhanced Etching
of Tungsten and Tungsten Silicide in Chlorine-Containing Discharges",
*Journal of The Electrochemical Society* **134**(9), 2265–2269 (1987).
<https://doi.org/10.1149/1.2100868> Chlorine etching of tungsten and
tungsten silicide, relevant to the TiW cap. Used on step 114. Tier: deep
dive.

**GHATE-1978** — P. B. Ghate, J. C. Blair, C. R. Fuller and G. E.
McGuire, "Application of Ti:W barrier metallization for integrated
circuits", *Thin Solid Films* **53**(2), 117–128 (1978).
<https://doi.org/10.1016/0040-6090(78)90024-X> Ti:W barrier
metallisation. Used on step 112. Tier: deep dive.

**HESS-1982** — D. W. Hess, "Plasma etch chemistry of aluminum and
aluminum alloy films", *Plasma Chemistry and Plasma Processing*
**2**(2), 141–155 (1982). <https://doi.org/10.1007/BF00633130> The
plasma etch chemistry of aluminium and aluminium alloy films. Used on
step 114. Tier: deep dive.

**HWANG-1997** — G. S. Hwang and K. P. Giapis, "On the origin of the
notching effect during etching in uniform high density plasmas",
*Journal of Vacuum Science & Technology B* **15**(1), 70–87 (1997).
<https://doi.org/10.1116/1.589258> The origin of notching in
high-density plasma etching. Used on step 114. Tier: deep dive.

**HWANG-1998** — G. S. Hwang and K. P. Giapis, "Mechanism of charging
damage during interlevel oxide deposition in high-density plasma tools",
*Proc. 1998 3rd International Symposium on Plasma Process-Induced Damage
(P2ID)*, pp. 164–167. <https://doi.org/10.1109/PPID.1998.725600>
Charging damage during interlevel oxide deposition in high-density
plasma tools. Used on step 115. Tier: deep dive.

**KAMOSHIDA-1997** — K. Kamoshida and Y. Ito, "Highly preferred (111)
texture aluminum-copper films formed with argon plasma treatment of the
titanium underlayer and their electromigration endurance as
interconnects", *Journal of Vacuum Science & Technology B* **15**(4),
961–966 (1997). <https://doi.org/10.1116/1.589515> (111) Al–Cu on a
plasma-treated Ti underlayer. Used on step 112. Tier: deep dive.

**KNORR-1996** — D. B. Knorr and K. P. Rodbell, "The role of texture in
the electromigration behavior of pure aluminum lines", *Journal of
Applied Physics* **79**(5), 2409–2417 (1996).
<https://doi.org/10.1063/1.361168> The role of texture in aluminium
electromigration. Used on step 112. Tier: deep dive.

**LEE-1981** — W.-Y. Lee, J. M. Eldridge and G. C. Schwartz, "Reactive
ion etching induced corrosion of Al and Al-Cu films", *Journal of
Applied Physics* **52**(4), 2994–2999 (1981).
<https://doi.org/10.1063/1.329043> RIE-induced corrosion of Al and Al–Cu
films. Used on step 114. Tier: deep dive.

**MANI-2007** — S. Mani and T. Saif, "Stress development in
plasma-deposited silicon dioxide thin-films due to hydrogen evolution",
*Thin Solid Films* **515**(5), 3120–3125 (2007).
<https://doi.org/10.1016/j.tsf.2006.08.025> Stress development in plasma
oxide from hydrogen evolution. Used on step 117. Tier: deep dive.

**MOON-2016** — Y. Moon, "Chemical and physical mechanisms of dielectric
chemical mechanical polishing (CMP)", in *Advances in Chemical
Mechanical Planarization (CMP)*, Woodhead Publishing, 2016, pp. 3–26,
ISBN 978-0-08-100165-3.
<https://doi.org/10.1016/B978-0-08-100165-3.00001-2> The chemical and
physical mechanisms of dielectric CMP. Used on steps 116 and 117. Tier:
high-level.

**MORI-1996** — S. Mori, T. Watanabe, K. Adachi, T. Fukushima, K. Uda
and Y. Sato, "Substrate effect in chemically amplified resist", *Proc.
SPIE* **2724**, Advances in Resist Technology and Processing XIII, 131
(1996). <https://doi.org/10.1117/12.241812> The substrate effect in
chemically amplified resists and its reduction. Used on step 113. Tier:
deep dive.

**NOWICKI-1978** — R. S. Nowicki, J. M. Harris, M.-A. Nicolet and I. V.
Mitchell, "Studies of the Ti-W/Au metallization on aluminum", *Thin
Solid Films* **53**(2), 195–205 (1978).
<https://doi.org/10.1016/0040-6090(78)90035-4> Ti–W on aluminium. Used
on step 112. Tier: deep dive.

**OLOWOLAFE-1985** — J. O. Olowolafe, C. J. Palmstrøm, E. G. Colgan and
J. W. Mayer, "Al/TiW reaction kinetics: Influence of Cu and interface
oxides", *Journal of Applied Physics* **58**(9), 3440–3443 (1985).
<https://doi.org/10.1063/1.335764> Al/TiW reaction kinetics and the
effect of Cu. Used on step 112. Tier: deep dive.

**PHILIPOSSIAN-2009** — A. Philipossian and T. Sun, "Frictional Analysis
of Various Poly(vinyl alcohol) Brush Roller Designs for Post-Interlevel
Dielectric CMP Scrubbing Applications", *Electrochemical and Solid-State
Letters* **12**(3), H84 (2009). <https://doi.org/10.1149/1.3058994>
Brush design for post-ILD-CMP scrubbing. Used on steps 116 and 117.
Tier: deep dive.

**ROCKE-1988** — M. Rocke and M. Schneegans, "Titanium nitride for
antireflection control and hillock suppression on aluminum silicon
metallization", *Journal of Vacuum Science & Technology B* **6**(4),
1113–1115 (1988). <https://doi.org/10.1116/1.584306> A refractory cap
for anti-reflection and hillock suppression on aluminium. Used on steps
112 and 113. Tier: deep dive.

**ROSENBERG-2000** — R. Rosenberg, D. C. Edelstein, C.-K. Hu and K. P.
Rodbell, "Copper Metallization for High Performance Silicon Technology",
*Annual Review of Materials Science* **30**(1), 229–262 (2000).
<https://doi.org/10.1146/annurev.matsci.30.1.229> The copper alternative
SKY130 did not take. Used on step 112. Tier: deep dive.

**SCHAIBLE-1978** — P. M. Schaible, W. C. Metzger and J. P. Anderson,
"Reactive ion etching of aluminum and aluminum alloys in an rf plasma
containing halogen species", *Journal of Vacuum Science and Technology*
**15**(2), 334–337 (1978). <https://doi.org/10.1116/1.569540> Reactive
ion etching of aluminium and its alloys in halogen plasmas. Used on step
114. Tier: deep dive.

**SHIRAISHI-1992** — N. Shiraishi, S. Hirukawa, Y. Takeuchi and N.
Magome, "New imaging technique for 64M-DRAM", *Proc. SPIE* **1674**,
Optical/Laser Microlithography V, 741 (1992).
<https://doi.org/10.1117/12.130364> Off-axis illumination for dense
lines. Used on step 113. Tier: deep dive.

**SIVARAM-1992** — S. Sivaram, R. Tolles, H. Bath, E. Lee and R.
Leggett, "Chemical Mechanical Polishing of Interlevel Dielectrics:
Models for Removal Rate and Planarity", *MRS Proceedings* **260**, 53
(1992). <https://doi.org/10.1557/PROC-260-53> Removal-rate and planarity
models for ILD CMP. Used on step 116. Tier: deep dive.

**STINE-1998-TED** — B. E. Stine, D. S. Boning, J. E. Chung, L.
Camilletti, F. Kruppa, E. R. Equi, W. Loh, S. Prasad, M. Muthukrishnan,
D. Towery, M. Berman and A. Kapoor, "The physical and electrical effects
of metal-fill patterning practices for oxide chemical-mechanical
polishing processes", *IEEE Transactions on Electron Devices* **45**(3),
665–679 (1998). <https://doi.org/10.1109/16.661228> The physical and
electrical effects of metal-fill patterning for oxide CMP. Used on step
116. Tier: deep dive.

**USAMI-1993** — T. Usami, K. Shimokawa and M. Yoshimaru, "Low
Dielectric Constant Interlayer Using Fluorine Doped Silicon Oxide",
*Extended Abstracts of the 1993 International Conference on Solid State
Devices and Materials*, S-II-9 (1993).
<https://doi.org/10.7567/SSDM.1993.S-II-9> A fluorine-doped oxide
interlayer. Used on step 115. Tier: deep dive.

**VAIDYA-1981** — S. Vaidya and A. K. Sinha, "Effect of texture and
grain structure on electromigration in Al-0.5%Cu thin films", *Thin
Solid Films* **75**(3), 253–259 (1981).
<https://doi.org/10.1016/0040-6090(81)90404-1> Texture and grain
structure versus electromigration in Al–0.5%Cu. Used on step 112. Tier:
deep dive.

**WAI-2017** — W. T. Wai and N. C. Ling, "Al-Cu interconnect corrosion
prevention in post metal etch and wet polymer clean wafers: CFM:
Contamination free manufacturing", *2017 28th Annual SEMI Advanced
Semiconductor Manufacturing Conference (ASMC)*, pp. 64–67.
<https://doi.org/10.1109/ASMC.2017.7969200> Al–Cu corrosion prevention
through the post-etch and polymer-clean sequence. Used on step 114.
Tier: deep dive.

**YAMANAKA-1999** — R. Yamanaka, T. Hattori, T. Mine, K. T. Hattori, T.
P. Tanaka and T. Terasawa, "Suppression of resist pattern deformation on
SiON bottom antireflective layer in deep-UV lithography", *Proc. SPIE*
**3678**, Advances in Resist Technology and Processing XVI, 198 (1999).
<https://doi.org/10.1117/12.350202> Resist deformation on a SiON BARC
and its suppression. Used on step 113. Tier: deep dive.

**YUE-1985** — J. T. Yue, W. P. Funsten and R. V. Taylor, "Stress
Induced Voids in Aluminum Interconnects During IC Processing", *23rd
International Reliability Physics Symposium* (1985), pp. 126–137.
<https://doi.org/10.1109/IRPS.1985.362087> Stress-induced voids in
aluminium interconnects. Used on step 115. Tier: deep dive.

### 8.13 Via-1, metal-2, via-2 and metal-3-stack module sources

Sources introduced by the writers of the via-1 module (steps 118–122),
the metal-2 module (steps 123–128) and the via-2 module and metal-3
stack (steps 129–134) that had no entry above. As in §8.12, each label
on those pages is the key below in lower case, the citation is the one
given in the page footnote, and the annotation is taken from the citing
page's reading list; entries are grouped by the sub-module that first
cited the source and name every page that uses it. None of these
sources describes SkyWater or the Bloomington fab.

#### Via 1: mask, etch, liner, tungsten fill and CMP (steps 118–122)

**BUI-1994** — N. D. Bui, V. H. Pham, D. D. Forsythe, R. T. Lee and J.
T. Yue, "Effect of TiN ARC on Electromigration Performance of Tungsten
Plug Via", *MRS Proceedings* **338** (1994).
<https://doi.org/10.1557/PROC-338-471> The anti-reflective TiN cap under
a tungsten-plug via and its effect on via electromigration. Used on
steps 119, 120, 130 and 131. Tier: deep dive.

**DOMAE-1998** — S. Domae, H. Masuda, K. Tateiwa, Y. Kato and M.
Fujimoto, "Stress-induced voiding in stacked tungsten via structure",
*1998 IEEE International Reliability Physics Symposium Proceedings*, pp.
318–323. <https://doi.org/10.1109/RELPHY.1998.670663> Stress-induced
voiding in stacked tungsten-via structures. Used on steps 121 and 132.
Tier: deep dive.

**GN-1994** — F. H. Gn, L. Liu and M. Guo, "Comparison study between
tungsten and aluminum plug for submicrometer contact via manufacturing",
*Proc. SPIE* **2335**, Microelectronic Manufacturing, 98–106 (1994).
<https://doi.org/10.1117/12.186049> Tungsten versus aluminium plugs for
submicrometre contacts and vias. Used on step 121. Tier: deep dive.

**GROVER-1998** — G. S. Grover, H. Liang, S. Ganeshkumar and W. Fortino,
"Effect of slurry viscosity modification on oxide and tungsten CMP",
*Wear* **214**(1), 10–13 (1998).
<https://doi.org/10.1016/S0043-1648(97)00219-6> Slurry viscosity and the
balance of oxide and tungsten removal in CMP. Used on steps 122 and 133.
Tier: deep dive.

**HU-1993** — C.-K. Hu, M. B. Small and P. S. Ho, "Electromigration in
Al(Cu) two-level structures: Effect of Cu and kinetics of damage
formation", *Journal of Applied Physics* **74**(2), 969–978 (1993).
<https://doi.org/10.1063/1.354839> Electromigration in two-level Al(Cu)
structures: the effect of copper and the kinetics of damage formation.
Used on steps 120, 121, 123, 131 and 132. Tier: deep dive.

**IRELAND-1997** — P. J. Ireland, "High aspect ratio contacts: A review
of the current tungsten plug process", *Thin Solid Films* **304**(1–2),
1–12 (1997). <https://doi.org/10.1016/S0040-6090(96)09557-0> A review of
the tungsten-plug process for high-aspect-ratio contacts and vias, liner
included. Used on steps 120, 121, 131 and 132. Tier: deep dive.

**KAWASAKI-1996** — H. Kawasaki and C.-K. Hu, "An electromigration
failure model of tungsten plug contacts/vias for realistic lifetime
prediction", *1996 Symposium on VLSI Technology, Digest of Technical
Papers*, pp. 192–193. <https://doi.org/10.1109/VLSIT.1996.507848> An
electromigration failure model for tungsten-plug contacts and vias. Used
on steps 121, 131 and 132. Tier: deep dive.

**KOBAYAKAWA-1991** — M. Kobayakawa, A. Arimatsu, F. Yokoyama, N.
Hirashita and T. Ajioka, "A study of outgassing from spin-on-glass films
used for planarization", *Proc. Eighth International IEEE VLSI
Multilevel Interconnection Conference (VMIC 1991)*, pp. 454–456.
<https://doi.org/10.1109/VMIC.1991.153054> Outgassing from spin-on-glass
planarising films, the mechanism behind via poisoning. Used on steps
119, 120, 121, 128, 130, 131 and 132. Tier: deep dive.

**KWOK-1990** — T. Kwok, C. Tan, D. Moy, J. J. Estabil, H. S. Rathore
and S. Basavaiah, "Electromigration in a two-level Al-Cu
interconnection with W studs", *Proc. Seventh International IEEE VLSI
Multilevel Interconnection Conference (VMIC 1990)*, pp. 106–112.
<https://doi.org/10.1109/VMIC.1990.127852> Electromigration in
two-level Al–Cu wiring with tungsten studs. Used on steps 120, 121,
123, 131 and 132. Tier: deep dive.

**LE-1996** — H. A. Le, K. Banerjee and J. W. McPherson, "The dependence
of W-plug via EM performance on via size", *Semiconductor Science and
Technology* **11**(6), 858–864 (1996).
<https://doi.org/10.1088/0268-1242/11/6/003> How tungsten-plug via
electromigration depends on the via size. Used on steps 118, 121, 129
and 132. Tier: deep dive.

**NGUYEN-2000** — V. H. Nguyen, P. Van Der Velden, R. Daamen, H. Van
Kranenburg and P. H. Woerlee, "Modelling of dishing for metal chemical
mechanical polishing", *IEDM 2000 Technical Digest*, pp. 499–502.
<https://doi.org/10.1109/IEDM.2000.904364> A model of dishing in metal
CMP. Used on steps 122 and 133. Tier: deep dive.

**PAT-ETCHSTOP-TI** — G. Xing, G. A. Cerny and M. R. Visokay (Texas
Instruments), *Etchstop for integrated circuits*, US 6,090,697 A, filed
1998-06-26, granted 2000-07-18.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6090697>
An etch stop for a fluorine-bearing via etch. Used on steps 119 and 130.
Tier: deep dive.

**PAT-VIA-POISON-UMC** — K.-L. Wu and H.-B. Lu (United
Microelectronics Corp.), *Method for preventing poisoned vias and
trenches*, US 6,013,581 A, filed 1998-10-05, granted 2000-01-11.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6013581>
Preventing poisoned vias and trenches. Used on steps 119, 121, 130
and 132. Tier: deep dive.

**PAT-WCVD-AMAT** — M. Chang, C. Leung, D. N. Wang and D. Cheng (Applied
Materials), *Process for CVD deposition of tungsten layer on
semiconductor wafer*, US 5,028,565 A, filed 1989-08-25, granted
1991-07-02.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5028565>
An early process patent for CVD tungsten deposition on semiconductor
wafers. Used on steps 121 and 132. Tier: deep dive.

**PETRI-1992** — R. Petri, D. Henry and N. Sadeghi, "Tungsten etching
mechanisms in low-pressure SF₆ plasma", *Journal of Applied Physics*
**72**(7), 2644–2651 (1992). <https://doi.org/10.1063/1.351565> Tungsten
etching mechanisms in fluorine plasmas, the reason a TiW floor is a
fragile etch stop. Used on steps 119 and 130. Tier: deep dive.

**RANG-1988** — S. Rang, R. Chow, R. H. Wilson, B. Gorowitz and A. G.
Williams, "Application of selective CVD tungsten for low contact
resistance via filling to aluminum multilayer interconnection", *Journal
of Electronic Materials* **17**(3), 213–216 (1988).
<https://doi.org/10.1007/BF02652180> Selective CVD tungsten via fill to
aluminium wiring, the alternative to blanket fill. Used on step 121.
Tier: deep dive.

**ROMERO-1991** — J. D. Romero, M. Khan, H. Fatemi and J. Turlo,
"Outgassing behavior of spin-on-glass (SOG)", *Journal of Materials
Research* **6**(9), 1996–2003 (1991).
<https://doi.org/10.1557/JMR.1991.1996> Outgassing behaviour of
spin-on-glass films and its link to via poisoning. Used on steps 119,
120, 130 and 131. Tier: deep dive.

**SAITO-1993** — T. Saito, H. Aoki, T. Tamaru and N. Owada, "Reliability
improvement in blanket tungsten CVD contact filling process for high
aspect ratio contact", *31st Annual Proceedings, Reliability Physics
1993*, pp. 334–339. <https://doi.org/10.1109/RELPHY.1993.283279>
Reliability of blanket-tungsten CVD filling of high-aspect-ratio
contacts. Used on steps 121 and 132. Tier: deep dive.

**SHIRATANI-2006** — M. Shiratani and K. Kumazawa, "Low Erosion Tungsten
CMP Process with High Productivity", *2006 IEEE International Symposium
on Semiconductor Manufacturing (ISSM)*, pp. 149–151.
<https://doi.org/10.1109/ISSM.2006.4493046> A low-erosion tungsten CMP
process. Used on steps 122 and 133. Tier: deep dive.

**UTTECHT-1991** — R. R. Uttecht and R. M. Geffken, "A
four-level-metal fully planarized interconnect technology for dense
high performance logic and SRAM applications", *Proc. Eighth
International IEEE VLSI Multilevel Interconnection Conference (VMIC
1991)*, pp. 20–26. <https://doi.org/10.1109/VMIC.1991.152961> IBM's
four-level-metal fully planarised interconnect for dense logic and
SRAM. Used on steps 121 and 127. Tier: deep dive.

**WALLS-1995** — J. A. Walls, "Stress-voiding in tungsten-plug
interconnect systems induced by high-temperature processing", *IEEE
Electron Device Letters* **16**(10), 430–432 (1995).
<https://doi.org/10.1109/55.464807> Stress voiding in tungsten-plug
interconnect induced by high-temperature processing. Used on steps 121
and 132. Tier: deep dive.

**WANG-1996-LINER** — C.-K. Wang, L. M. Liu, D. M. Liao, D. C. Smith and
M. Danek, "Optimization of PVD Ti/CVD TiN Liner for 0.35 μm Tungsten
Plug Technology", *MRS Proceedings* **427** (1996).
<https://doi.org/10.1557/PROC-427-383> Optimising a Ti/TiN liner for a
0.35 µm tungsten plug. Used on steps 120 and 131. Tier: deep dive.

**WIKI-VIA** — Wikipedia, *Via (electronics)*.
<https://en.wikipedia.org/wiki/Via_(electronics)> Vias between wiring
levels, an entry point for the via mask, etch and fill pages. Used on
steps 118, 119, 121, 129, 130 and 132. Tier: high-level.

#### Metal-2 stack, mask, etch, ILD4, CMP and cap oxide (steps 123–128)

**ABRAHAM-1997** — S. C. Abraham, C. T. Gabriel and J. Zheng,
"Performance of different etch chemistries on titanium nitride
antireflective coating layers and related selectivity and microloading
improvements for submicron geometries obtained with a high-density metal
etcher", *Journal of Vacuum Science & Technology A* **15**(3), 702–706
(1997). <https://doi.org/10.1116/1.580805> Etch chemistries, selectivity
and microloading for a TiN anti-reflective layer on a high-density metal
etcher. Used on step 125. Tier: deep dive.

**ARMSTRONG-1991** — N. P. Armstrong, "Evaluation of TiW + Al/Cu
electromigration performance", *Quality and Reliability Engineering
International* **7**(4), 281–286 (1991).
<https://doi.org/10.1002/qre.4680070414> Electromigration performance of
the TiW + Al/Cu system. Used on steps 123 and 134. Tier: deep dive.

**BLECH-1998** — I. A. Blech, "Diffusional back flows during
electromigration", *Acta Materialia* **46**(11), 3717–3723 (1998).
<https://doi.org/10.1016/S1359-6454(97)00446-1> Diffusional back-flow
during electromigration, the mechanism behind the critical length. Used
on step 123. Tier: deep dive.

**BLECH-HERRING-1976** — I. A. Blech and C. Herring, "Stress generation
by electromigration", *Applied Physics Letters* **29**(3), 131–133
(1976). <https://doi.org/10.1063/1.89024> The stress that
electromigration generates in a line. Used on step 123. Tier: deep dive.

**BURKE-1991** — P. A. Burke, "Semi-empirical modelling of SiO₂
chemical-mechanical polishing planarization", *Proc. Eighth
International IEEE VLSI Multilevel Interconnection Conference (VMIC
1991)*, pp. 379–384. <https://doi.org/10.1109/VMIC.1991.153031> A
semi-empirical model of oxide CMP planarisation. Used on step 127. Tier:
deep dive.

**CHEN-1991-TIN** — S. Chen, C. L. Chen and S. Tsou, "Sputtered TiN
performance as an anti-reflective coating in backend sub-µm i-line
lithography process", *Proc. Eighth International IEEE VLSI Multilevel
Interconnection Conference (VMIC 1991)*, pp. 393–395.
<https://doi.org/10.1109/VMIC.1991.153035> Sputtered TiN as a back-end
anti-reflective coating for sub-micrometre i-line lithography. Used on
steps 123 and 124. Tier: deep dive.

**FILIPPI-1993** — R. G. Filippi, G. A. Biery and M. H. Wood, "Evidence
of the Electromigration Short-Length Effect in Aluminum-Based Metallurgy
with Tungsten Diffusion Barriers", *MRS Proceedings* **309** (1993).
<https://doi.org/10.1557/PROC-309-141> The electromigration short-length
effect in aluminium wiring with tungsten diffusion barriers. Used on
steps 123 and 134. Tier: deep dive.

**GEORGIOU-1991** — G. E. Georgiou, M. Baker and S. A. Eshraghi, "Effect
of sputtered TiW deposition conditions on barrier properties for
submicron metallization", *Proc. Eighth International IEEE VLSI
Multilevel Interconnection Conference (VMIC 1991)*, pp. 420–422.
<https://doi.org/10.1109/VMIC.1991.153044> How sputtered-TiW deposition
conditions set its barrier properties. Used on steps 123 and 134. Tier:
deep dive.

**HARTSOUGH-1979** — L. D. Hartsough, "Resistivity of bias-sputtered TiW
films", *Thin Solid Films* **64**(1), 17–23 (1979).
<https://doi.org/10.1016/0040-6090(79)90536-4> Resistivity of
bias-sputtered TiW films. Used on steps 123 and 134. Tier: deep dive.

**KAANTA-1991** — C. W. Kaanta, S. G. Bombardier, W. J. Cote, W. R.
Hill, G. Kerszykowski, H. S. Landis, D. J. Poindexter, C. W. Pollard, G.
H. Ross, J. G. Ryan, S. Wolff and J. E. Cronin, "Dual Damascene: a ULSI
wiring technology", *Proc. Eighth International IEEE VLSI Multilevel
Interconnection Conference (VMIC 1991)*, pp. 144–152.
<https://doi.org/10.1109/VMIC.1991.152978> IBM's dual-damascene wiring,
the successor to the planarised aluminium back end. Used on step 127.
Tier: deep dive.

**KIM-2004-HDP** — S.-Y. Kim, W.-S. Lee and Y.-J. Seo, "Prevention of
plasma-induced damage during HDP–CVD deposition", *Journal of Materials
Processing Technology* **147**(2), 211–216 (2004).
<https://doi.org/10.1016/j.jmatprotec.2003.12.023> Preventing
plasma-induced damage during HDP-CVD inter-metal dielectric deposition.
Used on step 126. Tier: deep dive.

**MARTIN-1989** — C. A. Martin and J. W. McPherson, "Via
electromigration performance of Ti/W/Al-Cu(2%) multilayered
metallization", *Proc. Sixth International IEEE VLSI Multilevel
Interconnection Conference (VMIC 1989)*, pp. 168–175.
<https://doi.org/10.1109/VMIC.1989.78063> Via electromigration in
Ti/W/Al–Cu multilayer metallisation. Used on steps 123 and 134. Tier:
deep dive.

**MAY-1991** — J. S. May, "Electromigration Characteristics of Vias in
Ti:W/Al-Cu (2wt%) Multilayered Metallization", *29th International
Reliability Physics Symposium (IRPS 1991)*, pp. 91–96.
<https://doi.org/10.1109/IRPS.1991.363216> Electromigration of vias in
Ti:W/Al–Cu multilayer metallisation. Used on steps 123 and 134. Tier:
deep dive.

**NIX-1992** — W. D. Nix and E. Arzt, "On void nucleation and growth in
metal interconnect lines under electromigration conditions",
*Metallurgical Transactions A* **23**(7), 2007–2013 (1992).
<https://doi.org/10.1007/BF02647548> Void nucleation and growth in
interconnect lines under electromigration. Used on steps 123 and 134.
Tier: deep dive.

**PAT-DUMMY-TSMC** — W.-C. Chiou and S.-M. Jang (Taiwan Semiconductor
Manufacturing Co.), *Method for forming dummy structures for improved
CMP and reduced capacitance*, US 6,849,549 B1, filed 2003-12-04, granted
2005-02-01.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6849549>
Dummy structures for CMP planarity with reduced added capacitance. Used
on step 127. Tier: deep dive.

**PAT-DUMMY-UMC** — M.-S. Yang, Y. Huang, J.-Y. Wu and W. Lur (United
Microelectronics Corp.), *Method of improving surface planarity of
chemical-mechanical polishing operation by forming shallow dummy
pattern*, US 6,214,745 B1, filed 1998-11-19, granted 2001-04-10.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6214745>
Shallow dummy patterns to improve CMP planarity. Used on step 127. Tier:
deep dive.

**PAT-TAPER-ATT** — C. N. Bredbenner, T. A. Giniecki, N. Selamoglu and
H. J. Stocker (AT&T Bell Laboratories), *Method for tapered etching*, US
4,919,748 A, filed 1989-06-30, granted 1990-04-24.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4919748>
Tapered aluminium etching with CHF₃ and Cl₂, the pre-planarisation
alternative to a vertical profile. Used on step 125. Tier: deep dive.

**ROCHE-1996** — G. A. Roche and J. P. McVittie, "Application of Plasma
Charging Probe to Production HDP CVD Tool", *Proc. 1st International
Symposium on Plasma Process-Induced Damage (P2ID 1996)*, pp. 71–74.
<https://doi.org/10.1109/PPID.1996.715205> A plasma charging probe
applied to a production HDP-CVD tool. Used on step 126. Tier: deep dive.

**STAMPER-1998** — A. K. Stamper, M. B. Fuselier and X. Tian, "Advanced
wiring RC delay issues for sub-0.25-micron generation CMOS", *Proc. IEEE
1998 International Interconnect Technology Conference (IITC)*, pp.
62–64. <https://doi.org/10.1109/IITC.1998.704752> RC-delay issues of
aluminium wiring at the sub-0.25 µm generation. Used on steps 123, 126
and 134. Tier: deep dive.

**WIKI-INTERCONNECT** — Wikipedia, *Interconnect (integrated circuits)*.
<https://en.wikipedia.org/wiki/Interconnect_(integrated_circuits)>
Integrated-circuit interconnect, an entry point for the metal-stack
pages. Used on steps 123 and 134. Tier: high-level.

**YOO-1996** — W. S. Yoo and R. Swope, "Intermetal Dielectric Gap Fill
by Plasma Enhanced Chemical Vapor Deposited Fluorine-Doped Silicon
Dioxide Films", *Japanese Journal of Applied Physics* **35**(3A), L273
(1996). <https://doi.org/10.1143/JJAP.35.L273> Inter-metal gap fill by
PECVD fluorine-doped oxide. Used on step 126. Tier: deep dive.

#### Via 2 and the metal-3 stack (steps 129–134)

**CHU-2001** — S.-F. Chu, K. W. Chew, W. B. Loh, Y. M. Wang, B. G. Onn,
Y. Ju, J. Zhang and K. Shao, "High quality factor silicon-integrated
spiral inductors achieved by using thick top metal with different
passivation schemes", *2001 International Symposium on VLSI Technology,
Systems, and Applications (VLSI-TSA)*, pp. 154–157.
<https://doi.org/10.1109/VTSA.2001.934506> Thick top metal for
high-quality-factor spiral inductors on silicon. Used on step 134. Tier:
deep dive.

**GREENWOOD-2007** — B. B. Greenwood and J. Prasad, "Integrating TiN
only bottom plate metal-insulator metal capacitor (MIMC) for
contamination free manufacturing", *2007 International Semiconductor
Device Research Symposium (ISDRS)*, pp. 1–2.
<https://doi.org/10.1109/ISDRS.2007.4422363> A TiN-only bottom plate for
a MiM capacitor integrated in an aluminium back end. Used on step 134.
Tier: deep dive.

**LI-2003** — Y. Li, "Reservoir effect and maximum allowed VIA
misalignment for AlCu interconnect with tungsten VIA plug",
*Microelectronics Reliability* **43**(9–11), 1449–1454 (2003).
<https://doi.org/10.1016/S0026-2714(03)00257-9> The reservoir effect and
the maximum allowed via misalignment for Al–Cu wiring with tungsten
plugs. Used on step 132. Tier: deep dive.

**ZLATANOVIC-1990** — D. Zlatanović and G. Davinić, "Influence of
heat-treatment temperature and aluminum thickness on hillocks formation
in thin aluminum films", *Vacuum* **40**(1–2), 157–159 (1990).
<https://doi.org/10.1016/0042-207X(90)90144-N> Hillock formation in
aluminium films versus heat-treatment temperature and film thickness.
Used on step 134. Tier: deep dive.

### 8.14 MiM-capacitor, metal-3 and via-3 module sources

Sources introduced by the writers of the first MiM-capacitor module
(steps 135–138), the metal-3 module (steps 139–143) and the via-3
module (steps 144–148) that had no entry above. As in §8.13, each label
on those pages is the key below in lower case, the citation is the one
given in the page footnote, and the annotation is taken from the citing
page's reading list; entries are grouped by the sub-module that first
cited the source and name every page that uses it. None of these
sources describes SkyWater or the Bloomington fab.

#### MiM capacitor: dielectric, top plate, mask and etch (steps 135–138)

**ARMACOST-2000** — M. Armacost, A. Augustin, P. Felsner, Y. Feng, G.
Friese, J. Heidenreich, G. Hueckel, O. Prigge and K. Stein, "A high
reliability metal insulator metal capacitor for 0.18 μm copper
technology", *IEDM 2000 Technical Digest*, pp. 157–160.
<https://doi.org/10.1109/IEDM.2000.904282> A high-reliability MiM
capacitor in a 0.18 µm platform. Used on step 135. Tier: deep dive.

**BABCOCK-2001** — J. A. Babcock, S. G. Balster, A. Pinto, C. Dirnecker,
P. Steinmann, R. Jumpertz and B. El-Kareh, "Analog characteristics of
metal-insulator-metal capacitors using PECVD nitride dielectrics", *IEEE
Electron Device Letters* **22**(5), 230–232 (2001).
<https://doi.org/10.1109/55.919238> Frequency dependence and linearity
of PECVD-nitride MiM capacitors against oxide ones for precision
analogue use. Used on steps 135 and 136. Tier: deep dive.

**BLONKOWSKI-2007** — S. Blonkowski, "Nonlinear capacitance variations in
amorphous oxide metal-insulator-metal structures", *Applied Physics
Letters* **91**(17), 172903 (2007). <https://doi.org/10.1063/1.2800291>
The physics of the MiM voltage coefficient in amorphous oxides. Used on
step 135. Tier: deep dive.

**BOSE-2002** — M. Bose, D. N. Bose and D. K. Basa, "Plasma enhanced
growth, composition and refractive index of silicon oxynitride films",
*Materials Letters* **52**(6), 417–422 (2002).
<https://doi.org/10.1016/S0167-577X(01)00436-0> Composition and
refractive index of PECVD silicon oxynitride. Used on step 135. Tier:
deep dive.

**CHEUNG-2000** — K. P. Cheung, "On the mechanism of plasma enhanced
dielectric deposition charging damage", *Proc. 2000 5th International
Symposium on Plasma Process-Induced Damage (P2ID)*, pp. 161–163.
<https://doi.org/10.1109/PPID.2000.870658> Photoconduction as the
mechanism of charging damage during plasma-enhanced dielectric
deposition. Used on steps 138, 141 and 143. Tier: deep dive.

**DANZL-1997** — R. B. Danzl and A. McLaurin, "The use of concentrated
hydrogen peroxide for the removal of a TiW ARC from aluminum bond pads",
*Proc. Twenty-First IEEE/CPMT International Electronics Manufacturing
Technology Symposium (IEMT 1997)*, pp. 99–104.
<https://doi.org/10.1109/IEMT.1997.626884> Peroxide removal of a TiW
cap from aluminium pads, the wet chemistry that etches TiW. Used on
steps 136, 138 and 145. Tier: deep dive.

**DENISSE-1986** — C. M. M. Denisse, K. Z. Troost, J. B. Oude Elferink,
F. H. P. M. Habraken, W. F. van der Weg and M. Hendriks,
"Plasma-enhanced growth and composition of silicon oxynitride films",
*Journal of Applied Physics* **60**(7), 2536–2542 (1986).
<https://doi.org/10.1063/1.337117> How the gas mixture sets the
composition of PECVD silicon oxynitride. Used on step 135. Tier: deep
dive.

**DIRKS-1992** — A. G. Dirks, R. A. M. Wolters and A. E. M. De Veirman,
"Columnar microstructures in magnetron-sputtered refractory metal thin
films of tungsten, molybdenum and W-Ti-(N)", *Thin Solid Films*
**208**(2), 181–188 (1992).
<https://doi.org/10.1016/0040-6090(92)90640-W> Columnar microstructure
of sputtered W and W–Ti(N) films. Used on step 136. Tier: deep dive.

**GONON-2007** — P. Gonon and C. Vallée, "Modeling of nonlinearities in
the capacitance-voltage characteristics of high-k metal-insulator-metal
capacitors", *Applied Physics Letters* **90**(14), 142906 (2007).
<https://doi.org/10.1063/1.2719618> A model of the capacitance–voltage
nonlinearity of MiM capacitors. Used on step 135. Tier: deep dive.

**HILL-1980** — M. L. Hill, "Magnetron-sputtered Ti-W films", *Thin
Solid Films* **72**(2), 349–350 (1980).
<https://doi.org/10.1016/0040-6090(80)90017-6> Magnetron-sputtered Ti–W
films. Used on step 136. Tier: deep dive.

**KAR-ROY-1999** — A. Kar-Roy, C. Hu, M. Racanelli, C. A. Compton, P.
Kempf, G. Jolly, P. N. Sherman, J. Zheng, Z. Zhang and A. Yin, "High
density metal insulator metal capacitors using PECVD nitride for mixed
signal and RF circuits", *Proc. IEEE 1999 International Interconnect
Technology Conference (IITC)*, pp. 245–247.
<https://doi.org/10.1109/IITC.1999.787134> 1.0–2.0 fF/µm² PECVD-nitride
MiM capacitors integrated in a 0.25 µm CMOS back end. Used on steps 135
and 136. Tier: deep dive.

**LIU-2007-TIW** — G. Liu and Y. Kuo, "Reactive Ion Etching of Titanium
Tungsten Thin Films", *Journal of The Electrochemical Society*
**154**(7), H653 (2007). <https://doi.org/10.1149/1.2737631> Reactive
ion etching of TiW in CF₄/O₂, CF₄/Cl₂ and CF₄/HCl. Used on steps 114,
125, 136, 138 and 140. Tier: deep dive.

**MAHNKOPF-1999** — R. Mahnkopf, K.-H. Allers, M. Armacost, A. Augustin
et al., "'System on a chip' technology platform for 0.18 μm digital,
mixed signal and eDRAM applications", *IEDM 1999 Technical Digest*, pp.
849–852. <https://doi.org/10.1109/IEDM.1999.824282> A 0.18 µm digital,
mixed-signal and eDRAM technology platform. Used on step 135. Tier: deep
dive.

**NG-2003** — C. H. Ng, K. W. Chew and S. F. Chu, "Characterization and
comparison of PECVD silicon nitride and silicon oxynitride dielectric
for MIM capacitors", *IEEE Electron Device Letters* **24**(8), 506–508
(2003). <https://doi.org/10.1109/LED.2003.815154> PECVD nitride versus
oxynitride as the MiM dielectric. Used on step 135. Tier: deep dive.

**NG-2005** — C. H. Ng, C.-S. Ho, S.-F. S. Chu and S.-C. Sun, "MIM
Capacitor Integration for Mixed-Signal/RF Applications", *IEEE
Transactions on Electron Devices* **52**(7), 1399–1409 (2005).
<https://doi.org/10.1109/TED.2005.850642> A review of MiM capacitor
integration in Al–Cu and Cu back ends. Used on steps 135, 136, 137, 139
and 142. Tier: deep dive.

**PAT-MIM-FREESCALE** — D. R. Roberts and G. L. Huffman (Freescale
Semiconductor), *MIM capacitor in a semiconductor device and method
therefor*, US 7,375,002 B2, filed 2005-06-28, granted 2008-05-20.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7375002>
A MiM capacitor over planarised interconnect, with a via etch that stops
on the plates and the interconnect together. Used on steps 135, 136,
137, 144 and 145. Tier: deep dive.

**PAT-MIM-IBM** — T. J. Brabazon, B. El-Kareh, S. R. Martin, M. J. Rutten
and C. W. Kaanta (International Business Machines), *Precision analog
metal-metal capacitor*, US 5,708,559 A, filed 1995-10-27, granted
1998-01-13.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5708559>
A precision analogue metal–metal capacitor with a damascene bottom
plate. Used on steps 135, 136 and 137. Tier: deep dive.

**PAT-MIM-INFINEON** — S.-O. Kim and E. Demm (Infineon Technologies),
*MIM capacitor structure and method of fabrication*, US 7,112,507 B2,
filed 2003-11-24, granted 2006-09-26.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7112507>
A plate formed in the full thickness of a metallisation level. Used on
step 137. Tier: deep dive.

**PAT-MIM-NEWPORTFAB** — A. Kar-Roy and M. Racanelli (Newport Fab, LLC),
*Method for fabrication of an MIM capacitor and related structure*, US
6,430,028 B1, filed 2000-11-22, granted 2002-08-06.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6430028>
A nitride/TiN capacitor on an aluminium interconnect layer, etched
together and protected by an oxide spacer. Used on steps 135, 136, 137,
138, 139 and 140. Tier: deep dive.

**PAT-MIM-PHILIPS** — M. C. Olewine and K. F. Saiz (Koninklijke Philips
Electronics), *Metal-insulator-metal (MIM) capacitor structure and
methods of fabricating same*, US 6,717,193 B2, filed 2001-10-09, granted
2004-04-06.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6717193>
Ammonia-plasma treatment of the bottom electrode and a multi-rate etch
of the top electrode and insulator. Used on steps 135 and 138. Tier:
deep dive.

**PAT-MIM-TI-ALCAP** — D. L. Crenshaw, B. L. Williams, A. Tsao, H.
Shichijo, S. S. Papa Rao, K. D. Brennan and S. A. Lytle (Texas
Instruments), *Metal insulator metal (MIM) capacitor fabrication with
sidewall spacers and aluminum cap (ALCAP) top electrode*, US 7,250,334
B2, filed 2004-07-31, granted 2007-07-31.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7250334>
An aluminium cap over a Ta/TaN top electrode, with sidewall spacers, on
a copper back end. Used on step 136. Tier: deep dive.

**PAT-MIM-TI-ETCH** — M. O. Cathey Jr., P. Mahalingam, W. Tian, D. C.
Guiling, X. Chen, B. Hu and S. Chevacharoenkul (Texas Instruments),
*Forming integrated circuit devices with metal-insulator-metal capacitors
using selective etch of top electrodes*, US 8,110,414 B2, filed
2009-04-30, granted 2012-02-07.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8110414>
A selective plasma etch of MiM top electrodes that removes no more than
100 Å of the dielectric. Used on step 138. Tier: cross-check.

**TURBAN-1989** — G. Turban, J. F. Coulon and N. Mutsukura, "A
mechanistic study of SF₆ reactive ion etching of tungsten", *Thin Solid
Films* **176**(2), 289–308 (1989).
<https://doi.org/10.1016/0040-6090(89)90102-8> The mechanism of SF₆
reactive ion etching of tungsten. Used on steps 136 and 138. Tier: deep
dive.

**VAN-HUYLENBROECK-2002** — S. Van Huylenbroeck, S. Decoutere, R.
Venegas, S. Jenei and G. Winderickx, "Investigation of PECVD dielectrics
for nondispersive metal-insulator-metal capacitors", *IEEE Electron
Device Letters* **23**(4), 191–193 (2002).
<https://doi.org/10.1109/55.992835> Dispersion in PECVD MiM dielectrics
and how to avoid it. Used on step 135. Tier: deep dive.

**WIKI-CAPACITOR** — Wikipedia, *Capacitor*.
<https://en.wikipedia.org/wiki/Capacitor> Capacitance, dielectrics and
capacitor types, an entry point for the MiM-capacitor pages. Used on
steps 135 and 136. Tier: high-level.

**WIKI-SION** — Wikipedia, *Silicon oxynitride*.
<https://en.wikipedia.org/wiki/Silicon_oxynitride> Composition,
deposition and uses of silicon oxynitride films. Used on step 135. Tier:
high-level.

#### Metal 3: mask, etch, ILD5, CMP and cap oxide (steps 139–143)

**WANG-2004-MIM** — Z. Wang, J. Ackaert, C. Salm, F. G. Kuper, M. Tack,
E. De Backer, P. Coppens, L. De Schepper and B. Vlachakis,
"Plasma-charging damage of floating MIM capacitors", *IEEE Transactions
on Electron Devices* **51**(6), 1017–1024 (2004).
<https://doi.org/10.1109/TED.2004.829518> Plasma-charging damage of
floating MiM capacitors, its dependence on antenna areas and layout rules
against it. Used on steps 140, 141, 143 and 145. Tier: deep dive.

### 8.15 Metal-4, second MiM-capacitor, via-4 and metal-5 module sources

Sources introduced by the writers of the metal-4 stack and second
MiM-capacitor module (steps 149–153), the metal-4 patterning, ILD6, CMP
and cap-oxide steps (steps 154–158), the via-4 module (steps 159–160)
and the metal-5 module (steps 161–163) that had no entry above. As in
§8.14, each label on those pages is the key below in lower case, the
citation is the one given in the page footnote, and the annotation is
taken from the citing page's reading list; entries are grouped by the
sub-module that first cited the source and name every page that uses
it. Apart from PDK-PREVIOUS, none of these sources describes SkyWater,
SKY130 or the Bloomington fab.

#### Metal 4 stack and second MiM capacitor (steps 149–153)

**PAT-MIM-STACK-NEWPORTFAB** — A. Kar-Roy, M. Racanelli and P. Kempf
(Newport Fab, LLC), *Method for fabricating a high density composite MIM
capacitor with flexible routing in semiconductor dies*, US 7,078,310 B1,
filed 2004-05-19, granted 2006-07-18.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7078310>
A composite of two stacked MiM capacitors sharing a middle electrode and
joined in parallel. Used on steps 149, 150, 151 and 152. Tier: deep dive.

**PAT-MIM-STACK-TSMC** — K.-L. Chang, C.-Y. Lee and C.-H. Chen (Taiwan
Semiconductor Manufacturing Co.), *High density MIM capacitor structure
and fabrication process*, US 7,317,221 B2, filed 2003-12-04, granted
2008-01-08.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7317221>
Stacked MiM capacitor plates cross-connected through filled vias. Used on
steps 149, 150 and 152. Tier: deep dive.

**PDK-PREVIOUS** — SkyWater PDK Authors, *Previous Nomenclature*, SkyWater
SKY130 PDK documentation.
<https://skywater-pdk.readthedocs.io/en/main/previous.html> The older S8
process names, among them "s8phrc" with "dual MiM cap layers on metal 3
and metal 4", "s8pfhd" with a "5 metal layer backend stack" and
"s8phirs" with rdl metal inductors. Used on steps 150 and 161. Tier:
cross-check.

**SUL-2014** — W. S. Sul and S. G. Pyo, "RF Characteristic Analysis Model
Extraction on the Stacked Metal–Insulator–Metal Capacitors for Radio
Frequency Applications", *IEEE Transactions on Electron Devices*
**61**(8), 3011–3013 (2014). <https://doi.org/10.1109/TED.2014.2330842>
RF model extraction for stacked MiM capacitors. Used on step 150. Tier:
deep dive.

#### Metal 4: mask, etch, ILD6, CMP and cap oxide (steps 154–158)

**ALLEN-1994** — L. R. Allen and R. Rickard, "Tapered aluminum
interconnect etch", *Journal of Vacuum Science & Technology A* **12**(4),
1265–1268 (1994). <https://doi.org/10.1116/1.579306> A tapered aluminium
interconnect etch with N₂ additions in a TCP etcher. Used on steps 155,
162 and 163. Tier: deep dive.

**TAGUCHI-1998** — M. Taguchi, K. Maeda and J. Aoyama, "Improvement of
filling capability by control of water outgassing from via holes in
high-pressure aluminum reflow technology", in *Fourth International
Workshop on Stress Induced Phenomena in Metallization*, AIP, 1998, pp.
407–412. <https://doi.org/10.1063/1.54662> Water outgassing from via
holes and the filling of vias by high-pressure aluminium reflow. Used on
steps 158, 160 and 161. Tier: deep dive.

#### Via 4: mask and etch (steps 159–160)

**BAR-2002** — E. Bär, J. Lorenz and H. Ryssel, "Simulation of the
influence of via sidewall tapering on step coverage of sputter-deposited
barrier layers", *Microelectronic Engineering* **64**(1–4), 321–328
(2002). <https://doi.org/10.1016/S0167-9317(02)00805-5> The simulated
effect of via sidewall taper on the coverage of sputtered films. Used on
steps 159 and 160. Tier: deep dive.

**KIM-2011** — C.-G. Kim and W.-J. Lee, "Quantitative study on the
enhancement of sidewall coverage of sputter-deposited film by partially
tapering the sidewall of via holes", *Journal of Vacuum Science &
Technology B* **29**(2), 020604 (2011).
<https://doi.org/10.1116/1.3567184> Partially tapered vias and the
sidewall coverage of sputtered films. Used on steps 159 and 160. Tier:
deep dive.

**PAT-SLOPED-MOTOROLA** — R. K. Berglund, K. E. Mautz and R. Tyldesley
(Motorola), *Sloped contact etch process*, US 4,698,128 A, filed
1986-11-17, granted 1987-10-06.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4698128>
Sloped contact walls made by alternating oxide and resist etching, for
metal step coverage. Used on steps 159, 160 and 161. Tier: deep dive.

**PAT-TAPER-CHARTERED** — E.-N. Chou (Chartered Semiconductor
Manufacturing), *Enhancing step coverage by creating a tapered profile
through three dimensional resist pull back*, US 5,308,415 A, filed
1992-12-31, granted 1994-05-03.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5308415>
A tapered via profile made by three-dimensional resist pull-back. Used on
steps 159, 160 and 161. Tier: deep dive.

**SKELLY-1986** — D. W. Skelly and L. A. Gruenke, "Significant improvement
in step coverage using bias sputtered aluminum", *Journal of Vacuum
Science & Technology A* **4**(3), 457–460 (1986).
<https://doi.org/10.1116/1.573905> The step coverage of bias-sputtered
aluminium in straight-walled vias. Used on steps 159, 160 and 161. Tier:
deep dive.

#### Metal 5: stack, mask and etch (steps 161–163)

**CHANG-2004** — F.-Y. Chang, H.-C. Huang, S.-H. Yang and S. W. Kuo,
"Metal corrosion and passivation swelling defect study of ultra low
pattern density thick metal etch process", *2004 Semiconductor
Manufacturing Technology Workshop Proceedings*, pp. 153–155.
<https://doi.org/10.1109/SMTW.2004.1393753> Corrosion and
passivation-swelling defects in an ultra-low pattern-density thick-metal
etch. Used on steps 162 and 163. Tier: deep dive.

**DESHMUKH-2003** — A. R. Deshmukh, "The effect of ratio of deposition
times and via density on via fill in aluminum multilayer metallization",
*Thin Solid Films* **444**(1–2), 132–137 (2003).
<https://doi.org/10.1016/j.tsf.2003.08.041> Deposition-time ratio and via
density in aluminium via fill. Used on step 161. Tier: deep dive.

**DIRKS-1999** — A. G. Dirks, M. N. Webster, P. Turner, P. Rich and D. C.
Butler, "On the mechanism of aluminum via fill by reflow and forcefill as
studied by transmission electron microscopy", *Journal of Applied
Physics* **85**(1), 571–577 (1999). <https://doi.org/10.1063/1.369491>
The mechanisms of aluminium via fill by reflow and forcefill. Used on
step 161. Tier: deep dive.

**HARIU-1989** — T. Hariu, K. Watanabe, M. Inoue, T. Takada and H.
Tsuchikawa, "The Properties of Al-Cu/Ti Films Sputter Deposited at
Elevated Temperatures and High DC Bias", *27th International Reliability
Physics Symposium (IRPS 1989)*, pp. 210–214.
<https://doi.org/10.1109/IRPS.1989.363388> The electromigration lifetime
of Al–Cu/Ti films sputtered at 500 °C with substrate bias. Used on step
161. Tier: deep dive.

**HESS-2003** — K. J. Hess, S. H. Downey, G. B. Halt, T. Lee, L. L.
Mercado, J. W. Miter, W. C. Ng and D. G. Wontor, "Reliability of bond
over active pad structures for 0.13-μm CMOS technology", *53rd
Electronic Components and Technology Conference (ECTC 2003)*, pp.
1344–1349. <https://doi.org/10.1109/ECTC.2003.1216469> Wire-bond and
package-stress reliability of bond-over-active pad layouts for 0.13 µm
CMOS. Used on steps 161 and 162. Tier: deep dive.

**HUNTER-2012** — S. Hunter, J. L. Clark, D. Hornberger and L. Rubio,
"Use of Wire Bonding to Study Bond Pad Damage from Wafer Probe",
*International Symposium on Microelectronics* **2012**(1), 384–395
(IMAPS, 2012). <https://doi.org/10.4071/isom-2012-TP41> Wire bonding used
to reveal probe damage in aluminium bond pads. Used on step 161. Tier:
deep dive.

**JANSSEN-1998** — G. C. A. M. Janssen, J. F. Jongste, J. P. Lokker, A.
H. Verbruggen and S. Radelaar, "Aluminium via-fill at elevated pressure
and temperature", in *Fourth International Workshop on Stress Induced
Phenomena in Metallization*, AIP, 1998, pp. 349–358.
<https://doi.org/10.1063/1.54655> Aluminium via fill at elevated
pressure and temperature. Used on step 161. Tier: deep dive.

**KIKUTA-1995** — K. Kikuta, "Aluminum Reflow Sputtering", *MRS Bulletin*
**20**(11), 53–56 (1995). <https://doi.org/10.1557/S0883769400045577> A
short review of aluminium reflow sputtering. Used on step 161. Tier:
high-level.

**KROGH-1987** — O. Krogh, H. Slomowitz, Y. Melaku and H.-O. Blom,
"Spectroscopic Diagnostics of Photoresist Erosion in an Aluminum Etch
Plasma", *Journal of The Electrochemical Society* **134**(8), 2045–2048
(1987). <https://doi.org/10.1149/1.2100816> Spectroscopic diagnostics of
photoresist erosion in an aluminium etch plasma. Used on steps 162 and
163. Tier: deep dive.

**LEE-2003** — W.-J. Lee and S.-K. Rha, "Effect of Underlayer on the Via
Filling and the Microstructure of the Aluminum Film in Aluminum Plug
Process", *Japanese Journal of Applied Physics* **42**(6A), 3372–3376
(2003). <https://doi.org/10.1143/JJAP.42.3372> The underlayer's effect on
via fill and texture in a CVD–PVD aluminium plug process. Used on step
161. Tier: deep dive.

**MARSH-2016** — J. Marsh, A. Doutre, K. Syndergaard, P. Brown, K. I.
Hoo, E. De Jesus and S. Hunter, "Copper Ball Bond over a Variety of Probe
Marks in Two Pad Aluminum Thicknesses", *2016 IEEE 66th Electronic
Components and Technology Conference (ECTC)*, pp. 2228–2232.
<https://doi.org/10.1109/ECTC.2016.382> Copper ball bonds over probe
marks on two pad aluminium thicknesses. Used on step 161. Tier: deep
dive.

**MATSUOKA-1990** — F. Matsuoka, H. Iwai, K. Hama, H. Itoh, R. Nakata, T.
Nakakubo, K. Maeguchi and K. Kanzaki, "Electromigration reliability for
a tungsten-filled via hole structure", *IEEE Transactions on Electron
Devices* **37**(3), 562–568 (1990). <https://doi.org/10.1109/16.47758>
Electromigration reliability of tungsten-filled against unfilled via
holes. Used on step 161. Tier: deep dive.

**NISHIMURA-1991** — H. Nishimura, T. Yamada and S. Ogawa, "Reliable
submicron vias using aluminum alloy high temperature sputter filling",
*Proc. Eighth International IEEE VLSI Multilevel Interconnection
Conference (VMIC 1991)*, pp. 170–176.
<https://doi.org/10.1109/VMIC.1991.152982> High-temperature Al–Si–Cu
sputter filling of submicron vias. Used on step 161. Tier: deep dive.

**ONO-1990** — H. Ono, Y. Ushiku and T. Yoda, "Development of a
planarized Al-Si contact filling technology", *Proc. Seventh
International IEEE VLSI Multilevel Interconnection Conference (VMIC
1990)*, pp. 76–82. <https://doi.org/10.1109/VMIC.1990.127847> Al–Si
contact filling by sputtering at 500–550 °C. Used on step 161. Tier:
deep dive.

**PAT-AL-MULTISTEP-AMAT** — C.-R. Wang (Applied Materials), *Multistep
sputtering process for forming aluminum layer over stepped semiconductor
wafer*, US 5,108,570 A, filed 1990-03-30, granted 1992-04-28.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5108570>
A multistep, biased, heated aluminium sputter process for stepped wafers.
Used on step 161. Tier: deep dive.

**PAT-FORCEFILL-ELECTROTECH** — C. D. Dobson (Electrotech Ltd), *Method
for filing [sic] substrate recesses using elevated temperature and
pressure*, US 5,527,561 A, priority 1991-05-28, filed 1994-08-16, granted
1996-06-18.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5527561>
Filling recesses by high pressure and temperature after closing them
with sputtered metal. Used on step 161. Tier: deep dive.

**PRAMANIK-1990** — D. Pramanik and V. Jain, "Effect of underlayer on
sputtered aluminum grain structure and its correlation with step
coverage in submicron vias", *Proc. Seventh International IEEE VLSI
Multilevel Interconnection Conference (VMIC 1990)*, pp. 332–334.
<https://doi.org/10.1109/VMIC.1990.127888> The underlayer's effect on
sputtered aluminium grain structure and via step coverage. Used on step
161. Tier: deep dive.

**TAYLOR-1998** — D. S. Taylor, M. K. Jain and T. S. Cale, "Deposition
rate dependence of step coverage of sputter deposited aluminum-(1.5%)
copper films", *Journal of Vacuum Science & Technology A* **16**(5),
3123–3126 (1998). <https://doi.org/10.1116/1.581476> Temperature and
rate dependence of Al–Cu step coverage. Used on step 161. Tier: deep
dive.

**WIKI-WIRE-BONDING** — Wikipedia, *Wire bonding*.
<https://en.wikipedia.org/wiki/Wire_bonding> Wire bonding to aluminium
pads, an entry point for the bond-pad discussion. Used on step 161. Tier:
high-level.

### 8.16 Passivation, seal-ring, pad, alloy and electrical-test module sources

Sources introduced by the writers of the passivation oxide and seal-ring
steps (steps 164–166), the passivation nitride (step 167), the pad mask
and etch (steps 168–169) and the final alloy and electrical test (steps
170–171) that had no entry above. As in §8.15, each label on those pages
is the key below in lower case, the citation is the one given in the
page footnote, and the annotation is taken from the citing page's
reading list; entries are grouped by the sub-module that first cited the
source and name every page that uses it. Apart from CARAVEL-SEALRING and
PDK-IO-GPIOV2, none of these sources describes SkyWater, SKY130 or the
Bloomington fab.

#### Passivation oxide and seal-ring mask and etch (steps 164–166)

**CARAVEL-SEALRING** — Efabless Corporation, *caravel* repository,
`gds/advSeal_6um_gen.gds.gz` (seal-ring cell for SKY130 shuttle
designs), retrieved 2026-09-13.
<https://github.com/efabless/caravel/blob/main/gds/advSeal_6um_gen.gds.gz>
A published SKY130 seal-ring layout: a 6 µm `areaid.sl` band with a
5 µm `nsm` band over four 0.3 µm diffusion rings and no drawn metal or
via rings. Used on steps 165 and 166. Tier: cross-check.

**COMIZZOLI-1986** — R. B. Comizzoli, R. P. Frankenthal, P. C. Milner and
J. D. Sinclair, "Corrosion of Electronic Materials and Devices",
*Science* **234**(4774), 340–345 (1986).
<https://doi.org/10.1126/science.234.4774.340> Corrosion of electronic
materials and devices by humidity and ionic contamination. Used on steps
165, 166, 167, 168 and 169. Tier: deep dive.

**LANFORD-1978** — W. A. Lanford and M. J. Rand, "The hydrogen content of
plasma-deposited silicon nitride", *Journal of Applied Physics*
**49**(4), 2473–2477 (1978). <https://doi.org/10.1063/1.325095> Hydrogen
in plasma nitride, its infrared calibration, and hydrogen in a plasma
oxide deposited at 300 °C. Used on steps 164, 167 and 170. Tier: deep
dive.

**PAT-CRACKSTOP-IBM** — A. R. Mitwalsky and T.-C. Chen (Siemens
Aktiengesellschaft / International Business Machines), *Crack stops*,
US 5,789,302 A, filed 1997-03-24, granted 1998-08-04.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5789302>
Dielectric discontinuities in the dicing channel as crack stops. Used on
steps 165 and 166. Tier: deep dive.

**PAT-EDGESEAL-GF** — A. K. Stamper, V. J. McGahay and Z.-X. He
(GlobalFoundries), *Segmented guard-ring and chip edge seals*,
US 10,062,748 B1, filed 2017-02-27, granted 2018-08-28.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10062748>
An edge seal etched through the dielectrics and lined with passivation,
made with one mask. Used on steps 165, 166 and 167. Tier: deep dive.

**PAT-FUSE-IBM** — P.-I. P. Lee, W. A. Klaasen and A. Mitwalsky
(International Business Machines), *Fuse window with controlled fuse
oxide thickness*, US 5,872,390 A, filed 1997-08-14, granted 1999-02-16.
<https://patents.google.com/patent/US5872390A/en> Controlling the oxide
left over a laser fuse. Used on step 164. Tier: deep dive.

**PAT-FUSE-TSMC** — C.-H. Yang and C.-M. Su (Taiwan Semiconductor
Manufacturing Co.), *Method of forming a metal fuse on semiconductor
devices*, US 6,835,642 B2, filed 2002-12-18, granted 2004-12-28.
<https://patents.google.com/patent/US6835642B2/en> A shallow fuse window
in an oxide/nitride blanket that controls the remaining oxide. Used on
step 164. Tier: deep dive.

**PAT-FUSE-VANGUARD** — W.-T. Tzeng, Y.-F. Chen and K.-J. Wang (Vanguard
International Semiconductor), *Process for controlling oxide thickness
over a fusible link using transient etch stops*, US 6,294,474 B1, filed
1999-10-25, granted 2001-09-25.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6294474>
An oxide/nitride passivation stack with stated thicknesses, and bond-pad
and fuse openings made with one mask. Used on steps 164, 167 and 168.
Tier: deep dive.

**PAT-FUSEWIN-TSMC** — S. Ying and S.-C. Hung (Taiwan Semiconductor
Manufacturing Co.), *Method for etching fuse windows in IC devices and
devices made*, US 6,300,252 B1, filed 1999-10-01, granted 2001-10-09.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6300252>
Thick resist and a two-step window etch through a passivation and
several inter-metal dielectrics. Used on steps 165 and 166. Tier: deep
dive.

**PAT-SEALRING-ZEEVO** — S. Bothra, T. G. McKay and R. Jhota (Zeevo),
*Seal ring structure for IC containing integrated digital/RF/analog
circuits and functions*, US 6,492,716 B1, filed 2001-04-30, granted
2002-12-10.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6492716>
A seal ring under a passivation oxide and nitride, and the moisture path
around it. Used on steps 164, 165, 166 and 167. Tier: deep dive.

**PECK-1986** — D. S. Peck, "Comprehensive Model for Humidity Testing
Correlation", *24th International Reliability Physics Symposium* (1986),
pp. 44–50. <https://doi.org/10.1109/IRPS.1986.362110> A humidity-test
acceleration model for plastic packages. Used on steps 165 and 167.
Tier: deep dive.

**SINHA-1978** — A. K. Sinha, H. J. Levinstein, T. E. Smith, G. Quintana
and S. E. Haszko, "Reactive Plasma Deposited Si-N Films for MOS-LSI
Passivation", *Journal of The Electrochemical Society* **125**(4),
601–608 (1978). <https://doi.org/10.1149/1.2131509> Reactive-plasma
Si–N films for MOS-LSI passivation. Used on steps 164 and 167. Tier:
deep dive.

#### Passivation nitride (step 167)

**CHOW-1982** — R. Chow, W. A. Lanford, K.-M. Wang and R. S. Rosler,
"Hydrogen content of a variety of plasma-deposited silicon nitrides",
*Journal of Applied Physics* **53**(8), 5630–5633 (1982).
<https://doi.org/10.1063/1.331445> Hydrogen and etch rate across nine
commercial plasma-nitride reactors. Used on step 167. Tier: deep dive.

**SNOW-1965** — E. H. Snow, A. S. Grove, B. E. Deal and C. T. Sah, "Ion
Transport Phenomena in Insulating Films", *Journal of Applied Physics*
**36**(5), 1664–1673 (1965). <https://doi.org/10.1063/1.1703105>
Alkali-ion transport in oxide, the contamination the nitride blocks.
Used on step 167. Tier: deep dive.

#### Pad mask and etch (steps 168–169)

**PAT-PAD-FLUORINE-MICRON** — C. S. Jones, W. J. Crane, R. L. Gilchrist
and R. C. Langley (Micron Technology), *Method to remove fluorine
residues from bond pads*, US 5,380,401 A, filed 1993-01-14, granted
1995-01-10.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5380401>
Fluorine residues on bond pads after the nitride pad etch and their
in-situ plasma removal. Used on step 169. Tier: deep dive.

**PAT-PAD-FLUORINE-TSMC** — H.-C. Tsai and H.-H. Liu (Taiwan
Semiconductor Manufacturing Co.), *Method to remove fluorine residue
from bond pads*, US 7,055,532 B2, filed 2003-12-18, granted 2006-06-06.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7055532>
Reactive ion etching of Al–F–O deposits on bond pads. Used on step 169.
Tier: deep dive.

**PAT-TESTLINE-TSMC** — H.-W. Chen, S.-H. Hsu, H.-Y. Tsai and S.-P. Jeng
(Taiwan Semiconductor Manufacturing Co.), *Parametric testline with
increased test pattern areas*, US 7,679,384 B2, filed 2007-06-08,
granted 2010-03-16.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7679384>
Parametric testlines and their probe pads in the scribe line. Used on
steps 168 and 171. Tier: deep dive.

**PDK-IO-GPIOV2** — SkyWater PDK Authors, *skywater-pdk-libs-sky130_fd_io*
repository, cell `sky130_fd_io__top_gpiov2`, GDS layout
`sky130_fd_io__top_gpiov2.gds` and LEF abstract
`sky130_fd_io__top_gpiov2.lef`, retrieved 2026-09-13.
<https://github.com/google/skywater-pdk-libs-sky130_fd_io/tree/main/cells/top_gpiov2>
The SKY130 GPIO pad cell: an 80 µm × 200 µm LEF abstract and, in the GDS,
a chamfered 60 µm × 70 µm `pad` opening over a 65.4 µm × 75.4 µm metal-5
pad. Used on steps 168 and 169. Tier: cross-check.

**TEO-2015** — H. W. Teo, Y. Yang, Y. Wang, L. Zhu, Z. Q. Mo, S. P. Zhao
and J. Lam, "Feasibility study of TOF-SIMS surface measurement for
Aluminum bond pad fluorine contamination", *Proc. 2015 IEEE 22nd
International Symposium on the Physical and Failure Analysis of
Integrated Circuits (IPFA)*, pp. 61–63.
<https://doi.org/10.1109/IPFA.2015.7224333> TOF-SIMS measurement of
fluorine on aluminium bond pads. Used on step 169. Tier: deep dive.

#### Alloy and electrical test (steps 170–171)

**BUEHLER-1974** — M. G. Buehler, *Microelectronic Test Patterns*, NBS
Special Publication 400-6, National Bureau of Standards, 1974.
<https://doi.org/10.6028/NBS.SP.400-6> An early NBS publication on test
patterns. Used on step 171. Tier: deep dive.

**KIZILYALLI-1998** — I. C. Kizilyalli, G. C. Abeln, Z. Chen, J. Lee,
G. Weber, B. Kotzias, S. Chetlur, J. W. Lyding and K. Hess, "Improvement
of hot carrier reliability with deuterium anneals for manufacturing
multilevel metal/dielectric MOS systems", *IEEE Electron Device Letters*
**19**(11), 444–446 (1998). <https://doi.org/10.1109/55.728907> Deuterium
anneals for manufacturing multilevel metal/dielectric MOS systems. Used
on step 170. Tier: deep dive.

**LEARN-1976** — A. J. Learn, "Evolution and Current Status of Aluminum
Metallization", *Journal of The Electrochemical Society* **123**(6),
894–906 (1976). <https://doi.org/10.1149/1.2132964> Aluminium
metallisation and its processing. Used on step 170. Tier: deep dive.

**LYDING-1996** — J. W. Lyding, K. Hess and I. C. Kizilyalli, "Reduction
of hot electron degradation in metal oxide semiconductor transistors by
deuterium processing", *Applied Physics Letters* **68**(18), 2526–2528
(1996). <https://doi.org/10.1063/1.116172> Deuterium in the final sinter
and hot-electron degradation. Used on step 170. Tier: deep dive.

**PAT-DEUTERIUM-UIUC** — J. W. Lyding and K. Hess (Board of Trustees of
the University of Illinois), *Deuterium-treated semiconductor devices*,
US 5,872,387 A, filed 1996-01-16, granted 1999-02-16.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5872387>
Deuterium-treated devices and example anneal conditions. Used on step
170. Tier: deep dive.

**SAYAH-1988** — H. R. Sayah and M. G. Buehler, "Comb/serpentine/cross-bridge
test structure for fabrication process evaluation", *Proc. 1988 IEEE
International Conference on Microelectronic Test Structures (ICMTS)*,
pp. 23–28. <https://doi.org/10.1109/ICMTS.1988.672923> A
comb/serpentine/cross-bridge structure for process evaluation. Used on
step 171. Tier: deep dive.

### 8.17 sky130B ReRAM module

Sources introduced for the overview page on the optional sky130B ReRAM
(RRAM) tier between metal 1 and metal 2. As in §8.15, each label on that
page is the key below in lower case and the citation is the one given in
the page footnote. The SkyWater ReRAM documentation, its GitHub repository
and the open_pdks files describe SkyWater's module; the papers and
patents describe RRAM devices and their integration in general, and,
apart from HSIEH-2019 (a figure from which the SkyWater documentation
reproduces), none of them is stated to describe SkyWater's process.
Every URL was fetched on 2026-09-13; every DOI was checked through
Crossref on that date.

#### SkyWater ReRAM documentation and library

**RERAM-INDEX** — SkyWater PDK Authors, *sky130_fd_pr_reram - SKY130
ReRAM (SkyWater Provided)*, documentation index page.
<https://sky130-fd-pr-reram.readthedocs.io/en/latest/>
The library title "SKY130 ReRAM (SkyWater Provided)" and the note
"Initial documentation only release."; a contents list of the User Guide,
Background and Technology Specifications pages. Tier: cross-check.

**RERAM-BACKGROUND** — SkyWater PDK Authors, *Background*,
`sky130_fd_pr_reram` documentation.
<https://sky130-fd-pr-reram.readthedocs.io/en/latest/background.html>
States that "a HfO2-based RRAM layer is fabricated within the BEOL process
at multiple points as described in the physical design rules"; describes
a typical RRAM as a metal-oxide switching layer "sandwiched by top and
bottom metal electrodes"; defines FORM, SET, RESET and read ("0.1-0.2V"),
the 1T-1R cell and its bit line, word line and source line; "This
technology is still under development". Tier: cross-check.

**RERAM-SPECS** — SkyWater PDK Authors, *Technology Specifications*,
`sky130_fd_pr_reram` documentation.
<https://sky130-fd-pr-reram.readthedocs.io/en/latest/technology_specifications.html>
Forming data on a 1 Mbit array: fresh conductance "below 0.1 uS (e.g.,
resistance above 10MOhms)", forming voltages "from 2.2 to 3.1V" (average
2.5 V), yield above 99 % at 3.1 V, LRS after forming "30-120uS", pulse
width "1,000ns"; transcribed FORM/SET/RESET tables for 1T1R and 1T4R
test structures; 1T4R and 1T8R schematics; multi-bit programming; a
figure "extracted from" HSIEH-2019. Tier: cross-check.

**RERAM-UG** — SkyWater PDK Authors, *User Guide* (slide images
`page_1.svg`–`page_11.svg`, without `page_5`), `sky130_fd_pr_reram`
documentation.
<https://sky130-fd-pr-reram.readthedocs.io/en/latest/user_guide.html>
Slides "RRAM between met1/met2": FEOL "same as SKY130 PDK (met1 and
everything below)", BEOL "same as SKY130 PDK (met2 and everything
above)"; RRAM top electrode, oxide and bottom electrode "all are defined
by the same layer (r1c)"; "Both top & bottom parts of RRAM vias are drawn
on a single PDK layer, which is separated during mask generation"; mask
layers `cviam`, `r1c`, `r1v`; "RRAM bypass (2 stacked normal vias: 2x via
thickness, same via width & spacing)"; DRC example `rr1_cell.1 (0.230)`
and `rr1_cell.2 (0.230)`; the place-and-route tech-file slide with
thicknesses (met1 0.360, rr1_bot_electrode 0.010, rr1_oxide 0.005 with
dielectric constant 10 and "not in .ict", rr1_top_electrode 0.010, via
0.565 (via_bot 0.270, via_top 0.270 and the 0.025 of the RRAM layers; our
sum), met2 0.360), `r1c` minimum width 0.230 and spacing 0.140, and
z-levels 1.3761 to 2.6611. Tier: cross-check.

**RERAM-LAYERS** — SkyWater PDK Authors, `docs/figures/page_5.svg`
("sky130_fd_pr_reram Layer Descriptions" slide),
google/skywater-pdk-libs-sky130_fd_pr_reram repository, commit d6d2a3c
(2022-04-20); present in the repository but not included in the rendered
User Guide.
<https://github.com/google/skywater-pdk-libs-sky130_fd_pr_reram/blob/d6d2a3c6960aac0a0b12fc21221c31777bbf284d/docs/figures/page_5.svg>
Table of drawn and mask layers: `via` "defines both top & bottom contacts
to RRAM cell (when via is enclosed by r1c), or connects met1 and met2";
`cviam` (mask) "defines bottom part"; `r1c` (drawn and mask) "RRAM cell",
"defines RRAM cell between met1 and met2"; `r1v` (mask) "RRAM via",
"defines top part of contacts to RRAM tier1 cell". Tier: cross-check.

**RERAM-CELL** — SkyWater PDK Authors, `cells/reram_cell/`
(`sky130_fd_pr_reram__reram_cell.gds`, `.va`, `.spice`) and
`cells/reram_test_drc/`, google/skywater-pdk-libs-sky130_fd_pr_reram
repository, commit d6d2a3c.
<https://github.com/google/skywater-pdk-libs-sky130_fd_pr_reram/tree/d6d2a3c6960aac0a0b12fc21221c31777bbf284d/cells>
The cell layout carries a 0.32 µm × 0.32 µm shape on GDS 201:20, a
0.15 µm `via` (68:44) square, `met1` (68:20) and `met2` (69:20) with
labels BE and TE; the Verilog-A model's defaults are `area_ox` 0.1024e-12
m² and `Tox` 5.0e-9 m with filament-thickness parameters; the DRC test
layout carries rule labels `RR1_CELL.1` to `RR1_CELL.12` with values but
no descriptions. Tier: cross-check.

**RERAM-REFS** — SkyWater PDK Authors, *References*, `sky130_fd_pr_reram`
documentation.
<https://sky130-fd-pr-reram.readthedocs.io/en/latest/references.html>
"The ReRAM PDK from Skywater included academic references": GUAN-2012 and
JIANG-2014. Tier: cross-check.

#### open_pdks sky130B variant

**OPDKS-MAKEFILE** — R. T. Edwards et al., *open_pdks*,
`sky130/Makefile.in`, commit 1689ac3 (2026-08-27).
<https://github.com/RTimothyEdwards/open_pdks/blob/1689ac3f2dc763876eaf967227c7dfe831b031ae/sky130/Makefile.in>
"sky130B = 5-metal backend stack with dual MiM and ReRAM" (line 4);
"NOTE: ReRAM support is what distinguishes variant B from variant A."
followed by `SKY130B_DEFS += -DRERAM` (lines 345–346); installs the
`sky130_fd_pr_reram` library for variant B only. Tier: cross-check.

**OPDKS-README** — R. T. Edwards et al., *open_pdks*, `sky130/README`,
commit 1689ac3. <https://github.com/RTimothyEdwards/open_pdks/blob/1689ac3f2dc763876eaf967227c7dfe831b031ae/sky130/README>
"From open_pdks version 1.0.269, there is a process variant … sky130B …
which reflects support for ReRAM." Tier: cross-check.

**OPDKS-MAGIC-TECH** — R. T. Edwards et al., *open_pdks*,
`sky130/magic/sky130.tech` (Magic technology file source), commit
1689ac3.
<https://github.com/RTimothyEdwards/open_pdks/blob/1689ac3f2dc763876eaf967227c7dfe831b031ae/sky130/magic/sky130.tech>
Under `#ifdef RERAM`: a `reram` contact type between metal 1 and metal 2
written to GDS as `via` squares on 68:44 plus "layer RERAM reram / calma
201 20" (lines 1293–1301) and read back with "calma RERAM 201 20" (line
4194); DRC "width reram 260 "ReRAM width < %d (rr1.1)"", "spacing reram
reram 55 … (rr1.2)" and "no_overlap reram v1" (lines 4835–4842; the via-1 width rule, line 4821, is annotated "(via.1a + 2 * via.4a)");
extraction heights `v1` 1.7361/0.565, `allm2` 2.3011/0.36, `allm3`
3.0811, `mimcap` 2.7611 against `v1` 1.7361/0.27, `allm2` 2.0061 and
`mimcap` 2.4661 without ReRAM (lines 5303–5336); via-1 contact resistance
`m2c` 9000 against 4500 (nominal), 30000 against 15000 and 4000 against
2000 (corner variants) (lines 5421–5423, 5483–5485, 5545–5547). Tier:
cross-check.

#### RRAM devices, integration and the 3DSoC work

**GUAN-2012** — X. Guan, S. Yu and H.-S. P. Wong, "A SPICE Compact Model
of Metal Oxide Resistive Switching Memory With Variations", *IEEE Electron
Device Letters* **33**(10), 1405–1407 (2012).
<https://doi.org/10.1109/LED.2012.2210856> A SPICE model of metal-oxide
RRAM including temperature and temporal variation, fitted to HfOx RRAM
data; cited by the SkyWater ReRAM documentation. Tier: deep dive.

**JIANG-2014** — Z. Jiang, S. Yu, Y. Wu, J. H. Engel, X. Guan and
H.-S. P. Wong, "Verilog-A compact model for oxide-based resistive random
access memory (RRAM)", *2014 International Conference on Simulation of
Semiconductor Processes and Devices (SISPAD)*, pp. 41–44.
<https://doi.org/10.1109/SISPAD.2014.6931558> A dynamic Verilog-A RRAM
model for DC cycling and pulsed operation with variability; cited by the
SkyWater ReRAM documentation. Tier: deep dive.

**HSIEH-2019** — E. R. Hsieh, M. Giordano, B. Hodson, A. Levy, S. K.
Osekowsky, R. M. Radway, Y. C. Shih, W. Wan, T. F. Wu, X. Zheng,
M. Nelson, B. Q. Le, H.-S. P. Wong, S. Mitra and S. Wong, "High-Density
Multiple Bits-per-Cell 1T4R RRAM Array with Gradual SET/RESET and its
Effectiveness for Deep Learning", *2019 IEEE International Electron
Devices Meeting (IEDM)*, pp. 35.6.1–35.6.4.
<https://doi.org/10.1109/IEDM19573.2019.8993514> A 1T4R, two-bits-per-cell
array of "HfO2-based RRAM … built using a logic foundry technology that
is fully compatible with the CMOS back-end process" (abstract); the
source of a figure on RERAM-SPECS. Tier: deep dive.

**SRIMANI-2020** — T. Srimani, G. Hills, M. Bishop, C. Lau, P. Kanhaiya
et al., "Heterogeneous Integration of BEOL Logic and Memory in a
Commercial Foundry: Multi-Tier Complementary Carbon Nanotube Logic and
Resistive RAM at a 130 nm node", *2020 IEEE Symposium on VLSI
Technology*, pp. 1–2.
<https://doi.org/10.1109/VLSITechnology18217.2020.9265083> Four device
tiers (two of CNFET logic, two of RRAM) with 15 metal layers at a
~130 nm node in "a commercial foundry", with a monolithic 3D PDK
(abstract). Tier: deep dive.

**WONG-2012** — H.-S. P. Wong, H.-Y. Lee, S. Yu, Y.-S. Chen, Y. Wu,
P.-S. Chen, B. Lee, F. T. Chen and M.-J. Tsai, "Metal–Oxide RRAM",
*Proceedings of the IEEE* **100**(6), 1951–1970 (2012).
<https://doi.org/10.1109/JPROC.2012.2190369> Review of binary metal-oxide
RRAM: mechanism, materials, electrical characteristics, arrays,
uniformity, endurance, retention and scaling. Tier: deep dive.

**WASER-2007** — R. Waser and M. Aono, "Nanoionics-based resistive
switching memories", *Nature Materials* **6**(11), 833–840 (2007).
<https://doi.org/10.1038/nmat2023> Classification of resistive switching
mechanisms; in transition-metal-oxide "anion-migration cells" conducting
sub-oxide paths are formed and removed by local redox processes. Tier:
deep dive.

**IELMINI-2016** — D. Ielmini, "Resistive switching memories based on
metal oxides: mechanisms, reliability and scaling", *Semiconductor
Science and Technology* **31**(6), 063002 (2016).
<https://doi.org/10.1088/0268-1242/31/6/063002> Open-access review of
bipolar RRAM switching, state stability and scaling. Tier: deep dive.

**LEE-2008-HFO2** — H. Y. Lee, P. S. Chen, T. Y. Wu, Y. S. Chen,
C. C. Wang, P. J. Tzeng, C. H. Lin, F. Chen, C. H. Lien and M.-J. Tsai,
"Low power and high speed bipolar switching with a thin reactive Ti
buffer layer in robust HfO2 based RRAM", *2008 IEEE International
Electron Devices Meeting*, pp. 1–4.
<https://doi.org/10.1109/IEDM.2008.4796677> An HfO₂ RRAM "with the TiN
electrodes" and a thin Ti buffer layer, "fully integrated with 0.18 µm
CMOS technology" (abstract). Tier: deep dive.

**CHEN-2009-HFOX** — Y. S. Chen, H. Y. Lee, P. S. Chen, P. Y. Gu, C. W.
Chen, W. P. Lin, W. H. Liu, Y. Y. Hsu, S. S. Sheu, P. C. Chiang, W. S.
Chen, F. T. Chen, C. H. Lien and M.-J. Tsai, "Highly scalable hafnium
oxide memory with improvements of resistive distribution and read disturb
immunity", *2009 IEEE International Electron Devices Meeting (IEDM)*,
pp. 1–4. <https://doi.org/10.1109/IEDM.2009.5424411> A 30 nm × 30 nm HfOx
cell and a 1 kb 1T1R array with an AlOx buffer layer and verify schemes
(abstract). Tier: deep dive.

**GOVOREANU-2011** — B. Govoreanu, G. S. Kar, Y.-Y. Chen, V. Paraschiv et
al., "10×10nm² Hf/HfOx crossbar resistive RAM with excellent performance,
reliability and low-energy operation", *2011 International Electron
Devices Meeting*, pp. 31.6.1–31.6.4.
<https://doi.org/10.1109/IEDM.2011.6131652> A sub-10 nm × 10 nm Hf/HfOx
cell; the role of the cap layer and film crystallinity (abstract). Tier:
deep dive.

**BECKMANN-2016** — K. Beckmann, J. Holt, W. Olin-Ammentorp, J. Van
Nostrand and N. Cady, "Impact of Etch Process on Hafnium Dioxide Based
Nanoscale RRAM Devices", *ECS Transactions* **75**(13), 93–99 (2016).
<https://doi.org/10.1149/07513.0093ecst> A W/HfO₂/Ti/TiN RRAM on a 300 mm
65 nm platform; TiN/Ti etched by RIE and HfO₂ removed either by dilute
HF or a BCl₃/O₂ RIE, compared for structure, electrical behaviour and
yield (abstract). Tier: deep dive.

**GOLONZKA-2019** — O. Golonzka, U. Arslan, P. Bai, M. Bohr, O. Baykan et
al., "Non-Volatile RRAM Embedded into 22FFL FinFET Technology", *2019
Symposium on VLSI Technology*, pp. T230–T231.
<https://doi.org/10.23919/VLSIT.2019.8776570> An embedded RRAM in Intel's
22FFL logic technology: bit-cell integration into the logic flow,
endurance, retention and yield on 7.2 Mbit arrays (abstract). Tier: deep
dive.

**LE-2019** — B. Q. Le, A. Grossi, E. Vianello, T. Wu, G. Lama,
E. Beigne, H.-S. P. Wong and S. Mitra, "Resistive RAM With Multiple Bits
Per Cell: Array-Level Demonstration of 3 Bits Per Cell", *IEEE
Transactions on Electron Devices* **66**(1), 641–646 (2019).
<https://doi.org/10.1109/TED.2018.2879788> Multi-bit programming of 4 kbit
1T1R "HfOx-based RRAM integrated in the back end of the line of 130-nm
silicon CMOS technology" (abstract); cited by RERAM-BACKGROUND. Tier:
deep dive.

**GEORGE-2010** — S. M. George, "Atomic Layer Deposition: An Overview",
*Chemical Reviews* **110**(1), 111–131 (2010).
<https://doi.org/10.1021/cr900056b> Review of atomic layer deposition.
Tier: deep dive.

**WILK-2001** — G. D. Wilk, R. M. Wallace and J. M. Anthony, "High-κ gate
dielectrics: Current status and materials properties considerations",
*Journal of Applied Physics* **89**(10), 5243–5275 (2001).
<https://doi.org/10.1063/1.1361065> Review of the properties and process
compatibility of high-κ dielectrics, the materials background of HfO₂.
Tier: deep dive.

#### Patents on RRAM integration

**PAT-RRAM-OXIDE-TSMC** — T. H. Dang, H.-L. Lin, C.-Y. Tsai, C.-S. Tsai
and R.-L. Lee (Taiwan Semiconductor Manufacturing Co.), *Oxide film
scheme for RRAM structure*, US 9,431,609 B2, filed 2014-08-14, granted
2016-08-30.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9431609>
An RRAM stack over a lower interconnect: bottom electrode (Ta, TaN, Ti or
TiN by vapour deposition), ALD HfOx from HfCl₄ and H₂O pulses plus
HfAlOx, capping layer, top electrode, patterning by a masking layer with
a fluorine or argon plasma, nitride sidewall spacers, bottom-electrode
etch, upper ILD and a via landing on the top electrode. Tier: deep dive.

**PAT-RRAM-ETCHSTOP-TSMC** — M. C. Liu, Y.-T. Tseng, C.-Y. Hsu, S.-C. Liu
and C.-S. Tsai (Taiwan Semiconductor Manufacturing Co.), *RRAM cell
structure with conductive etch-stop layer*, US 10,003,022 B2, filed
2014-03-04, granted 2018-06-19.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10003022>
A conductive etch-stop layer between the lower interconnect and the
bottom electrode; a SiON anti-reflective layer on the top electrode; a
top-electrode etch, SiN sidewall spacers, a second etch through the HfO₂
and bottom electrode stopping on the etch-stop layer, and a third etch of
that layer (Cl- or F-based dry etch, or wet); and an enveloping
dielectric protection layer, reducing mask steps, CMP and copper etch
by-products. Tier: deep dive.

**PAT-RRAM-INTERMOLECULAR** — M. Lee, T. Chiang and D. Pramanik
(Intermolecular, Inc.), *Methods of manufacturing embedded bipolar
switching resistive memory*, US 9,076,523 B2, filed 2012-12-13, granted
2015-07-07.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9076523>
Embedded ReRAM with non-linear elements; its description notes ALD or
PVD "to remain within a Back End of Line (BEOL) thermal budget" for the
switching layer, titanium nitride as an oxygen-reactive electrode, and
that hafnium-oxide layers "may need about 7 Volts during their forming".
Tier: deep dive.

#### Encyclopaedia articles

**WIKI-RERAM** — Wikipedia, *Resistive random-access memory*.
<https://en.wikipedia.org/wiki/Resistive_random-access_memory> Oxygen
vacancies, forming and the set/reset cycle; HfO₂ as a low-voltage ReRAM
material. Tier: high-level.

**WIKI-ALD** — Wikipedia, *Atomic layer deposition*.
<https://en.wikipedia.org/wiki/Atomic_layer_deposition> Sequential,
self-limiting precursor pulses; ALD of high-κ oxides including HfO₂.
Tier: high-level.

**WIKI-HFO2** — Wikipedia, *Hafnium(IV) oxide*.
<https://en.wikipedia.org/wiki/Hafnium(IV)_oxide> Hafnia as a high-κ
dielectric ("4–6 times higher than that of SiO2, which is 3.9") and as a
candidate for resistive-switching memories. Tier: high-level.

## 9. Evidence about specific tools at SkyWater

Strength scale: **strong** = a SkyWater or tool-vendor statement;
**medium** = a SkyWater job posting (retrieved on the date stated;
listings expire) or an interview with a
named SkyWater employee; **weak** = indirect (an inference from public
evidence). Tools that
post-date the original Cypress S8 flow are marked † — they show what is
on the floor today, not necessarily what built the first S8 wafers.

| Area | Vendor / model | Public hit(s) | Strength |
|------|----------------|---------------|----------|
| Lithography | ASML i-line stepper and i-line scanner | SKW-01 | strong |
| Lithography | ASML DUV (KrF, 248 nm) stepper and scanner | SKW-01 | strong |
| Lithography | ASML 193 nm single-stage scanner ("90nm CD") and twin-stage scanner ("sub 65nm CD") † | SKW-01; SKW-06 names "the ASML TWINSCAN lithography tool" | strong |
| Lithography | Multibeam multicolumn e-beam (MEBL) † | SKW-14, SKW-06, GOV-01 context | strong |
| Coat/develop tracks | DNS (SCREEN) 80B; Sokudo RF3; TEL ProZ / Lithius | SKW-01 | strong |
| Photo metrology | AMAT Verity (CD-SEM), AMAT VeraSEM; KLA 5200/5300/Archer overlay | SKW-01 | strong |
| Defect inspection | KLA-Tencor AIT, SP1 (Surfscan); EV300 review; SEM | JOB-01 ("SEM/AIT/KLA/SP1/EV300/1X") | medium |
| CVD dielectrics | "C1"/"C2" PECVD (inferred to be Novellus Concept One/Two; SKW-01 gives only the abbreviations); AMAT Producer PECVD TEOS; Lam/Novellus HDP-CVD (doped and PSG) | SKW-01; SKW-07 ("Novellus high density plasma tool") | strong |
| CVD tungsten | Lam/Novellus PECVD tungsten with PNL nucleation (plug fill, ≤10:1) | SKW-01 | strong |
| PVD metals | AMAT PVD (Al and AlCu, TiW, TiN (ESC and IMP), collimated Ti, WN, Co, Nb) — consistent with Endura-class platforms | SKW-01 (platform name not given) | strong for vendor, weak for model |
| Electroplating † | AMAT Raider single-wafer Cu plating | SKW-01 | strong |
| ALD † | (vendor not named) AlN, TiN, SiO₂, Al₂O₃, HfO₂, TiO₂, ZrO₂ | SKW-01 | strong (capability), no vendor |
| Metal etch | Lam 9600 (Al, TiW, TiN, Pt); Lam 2300 Versys (Al, TiW, TiN, Nb, Pt) | SKW-01 | strong |
| Poly/oxide/trench etch | AMAT DPS II (HBr/Cl₂/NF₃/CF₄/CHF₃/O₂ — gate, trench, W/WN); Lam 9400 TCP (poly/nitride); Lam 4400 | SKW-01 | strong |
| Resist strip | Gasonics PEP (remote microwave); Iridia RF microwave; Mattson Aspen 2 | SKW-01 | strong |
| Wet clean / wet etch | Akrion Gamma batch bench (H₂SO₄, SC1, H₃PO₄, BOE); DNS wet bench (HF/SC1/SC2); FSI Mercury rotational; SEZ 223 and Lam DaVinci single-wafer (HF, DSP) | SKW-01; SKW-07 ("SEZ etcher tool") | strong |
| Batch solvent | Rotational EKC265/EKC270 solvent strip | SKW-01 | strong |
| Furnaces | Aviza — wet/dry oxidation to 1150 °C, LPCVD nitride/poly/oxide/ONO, BTBAS nitride, forming-gas alloy | SKW-01 ("Furnaces are all made by Aviza") | strong |
| RTA | AG Associates Heatpulse 8808 (NH₃, Ar, N₂, O₂, to 1200 °C) | SKW-01 | strong |
| Ion implant | Axcelis 8250 medium current; Axcelis GSD high current/high energy (10–3000 keV); Axcelis GSD high dose (2–180 keV) | SKW-01; SKW-07 (implanter maintenance) | strong |
| CMP | AMAT Mirra (oxide, nitride, W, Al, Cu, Nb) | SKW-01 | strong |
| Scribe | Lumonics Superclean laser scribe | SKW-01 | strong |
| Parametric / sort test | HP 4062UX; Advantest T5365P; Verigy V3308, V4108, 93000; Credence Duo, LT; Camtek Falcon; Qualitau reliability | SKW-01 | strong |
| Physical analysis | FEI dual-beam FIB/SEM; Hitachi S-4800 SEM; SELA EM2 cleaver; Oxford PlasmaLab RIE (deprocessing); Allied TechPrep polisher | SKW-01 | strong |
| Starting wafers | GlobalWafers and SEH America 200 mm silicon (Cypress qualified GlobalWafers for S8 at Fab 4 in 2015) | SEC-01, SEC-02, CYP-06 | strong |
| Sputter targets, gases, chemicals | Honeywell Electronic Materials and JX Metals targets; Air Products / Praxair / Linde / Airgas gases; KMG, EMD Performance Materials chemicals | SEC-01, SEC-02 | strong |
| Tool population | "at least 522 well-maintained fab and sort tools" (2021); "416 tools" (2015) | SEC-01; CYP-05 | strong |
| Cleanroom | 80,000 sq ft (2015–2017); 91,000 sq ft class 10 with SMIF after the 2020 addition (8,400–13,000 sq ft of new class 10 fab) | CYP-02, CYP-05, SKW-01, SKW-16, GOV-03, GOV-04 | strong |
| Throughput | ~17,000 wafers/month (2017); 16,700/month (2015); 156,000/year (2021); 10,000 30-mask CMOS wafers/month (2023) | CYP-02, CYP-05, SEC-01, SKW-16 | strong |

Not found in any public source: Nikon, Canon, Ultratech or Cymer
lithography; Varian/Eaton implanters; Ebara CMP; Rudolph/Onto or
Nanometrics metrology; Kokusai or ASM furnaces; Amtech. (Hitachi
appears in SKW-01 only as the S-4800 SEM in the physical-analysis
lab, not as a process tool.) Their absence from SKW-01 is itself weak
evidence that they are not (or no longer) on the floor.

## 10. Gaps and open questions

* **Film thicknesses.** Public thicknesses exist for the conductors
  and for the inter-level dielectric/via heights in PDK-04/ANN-16 and
  the few values in PDK-03; gate-oxide, ONO, spacer-nitride and
  silicide thicknesses are only bounded by the Cypress patents
  (PAT-01 to PAT-04) and generic references.
* **Lithography generation for S8.** SKW-01 lists i-line, KrF and ArF
  ASML tools; which layers of SKY130 use which wavelength is not stated
  publicly and must be inferred from feature size (ITRS-03).
* **Tool models behind generic entries.** SKW-01 names vendors but not
  models for PVD ("AMAT PVD Metal") and PECVD ("Producer", "C1", "C2");
  no public source found gives the models.
* **Historical tool set.** Every tool list is post-2017; the 2000s
  Cypress tool set that first ran S8 is documented only indirectly
  (CYP-04: "New tools and equipment have been installed several
  times"; PRESS-02 on the used-200 mm-tool market).
* **Cypress process papers.** No IEDM/VLSI/IRPS paper by Cypress
  authors describing the 130 nm S8 baseline (STI, TiN local
  interconnect, AlCu/TiW/TiN metallisation) was found; only SONOS
  module papers and patents.
