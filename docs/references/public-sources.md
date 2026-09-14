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
written page has exactly one entry here; the inventory holds 1703
keyed entries as of 2026-09-13, and `tools/check_refs.py` keeps the
page-side labels well formed. Sections 8.4 (keyed Wikipedia entries),
8.8, 8.9, 8.10, 8.11, 8.12, 8.13, 8.14, 8.15, 8.16, 8.17, 8.18, 8.19,
8.20 and 8.21 were added to cover the sources the writers of the step,
category, overview, machine, material and mask pages introduced; a
"Label ↔ key" note marks the few cases where one source has two keys.

:::{note}
Nothing in this inventory comes from private material. Where a public
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
contact (`mcon`) drawn CD 0.17 µm and "standard contact bottom CD" 0.09 µm, licon bottom CD 0.08 µm, via 0.15 µm.
Also used on the medium-current and high-current implanter pages.
Also used on the i-line stepper or scanner, DUV (KrF, 248 nm) stepper or
scanner and coat/develop track pages.
Tier: cross-check.
Also used on the lithography materials material page.
Also used on the substrates material page.
Also used on the FOM, DNM, LVTNM, NWM, HVTPM, PWBM, PWDEM, P1M, LICM1,
LI1M, CTM1, MM1, VIM, MM2 and VIM4 mask pages.

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
the inter-level dielectric / via heights directly: LINT top over li to
met1 bottom (NILD2) 0.265 µm, via1 (NILD3) 0.27 µm, via2 (NILD4) 0.42 µm,
via3 (NILD5) 0.39 µm, via4 (NILD6) 0.505 µm, LINT 0.075 µm, TOPOX
0.09 µm, TOPNIT 0.54 µm on metal (0.3777 µm from the metal-5 bottom to its top in the field, on our
reading of the drawing), NILD3_C/NILD4_C liners 0.030 µm, PSG
0.6099 µm from the field-oxide top to the li bottom and 0.4299 µm from
the field-poly top to the li bottom (our reading of the drawing); and levels
above the substrate: FOX top 0.3262, li bottom 0.9361, 1.0111 (read as the top of
the LINT beside li, 0.9361 + 0.075 µm; our reading of the drawing),
met1 bottom 1.3761, met2 bottom 2.0061, met3 bottom 2.7861, met4
bottom 4.0211, met5 bottom 5.3711, and PI1 top 11.8834 µm (further
labels 5.2523, 6.1346, 0.4223 and 0.070 µm dimension the
metal5/passivation region). Tier: cross-check.
Also used on the PECVD, HDP-CVD and PVD cluster tool pages.
Also used on the sputter targets material page.
Also used on the substrates material page.
Also used on the LI1M and VIM mask pages.

**PDK-05** — *Masks* page and `masks.csv`.
<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
<https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>.
Table of mask names and acronyms flagged as used in SKY130 (FOM, DNM,
NWM, HVTPM, LVTNM, HVTRM, NTM, HVNTM, LDNTM, PSDM, NSDM, TUNM, ONOM,
LVOM, RPM, NPCM, P1M, LICM1, LI1M, CTM1, MM1–MM5, VIM, VIM2–VIM4, NSM,
PDM, CU1M, PMM2, …). This is the public basis for the mask index and
for the order of the lithography steps. Tier: cross-check.
Also used on the FOM, DNM, LVTNM, NWM, HVTPM, PWBM, PWDEM, P1M, LICM1,
LI1M, CTM1, MM1, VIM, MM2 and VIM4 mask pages.

**PDK-06** — *Layers Reference* and `gds_layers.csv`.
<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
<https://github.com/google/skywater-pdk/blob/main/docs/rules/gds_layers.csv>.
GDS layer/purpose numbers and the process meaning of each drawn layer
(e.g. `vhvi` "used to identify nodes that operate at 12V nominal (16V
max)"). No thicknesses. Tier: cross-check.
Also used on the FOM, DNM, LVTNM, NWM, HVTPM, PWBM, PWDEM, P1M, LICM1,
LI1M, CTM1, MM1, VIM, MM2 and VIM4 mask pages.

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
endurance.
Also used on the silicon and polysilicon plasma etcher and metal plasma
etcher pages.
Also used on the PECVD and PVD cluster tool pages.
Tier: cross-check.
Also used on the sputter targets material page.
Also used on the DNM, LVTNM, NWM, HVTPM, PWBM, PWDEM and VIM4 mask
pages.

**PDK-08** — *Parasitic Layout Extraction* page.
<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
(source: <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/rcx.rst>).
Sheet resistances by layer (as listed: metal 1–2 125 mΩ/sq,
metal 3–4 47 mΩ/sq, metal 5 29 mΩ/sq, poly 48 200 mΩ/sq, XHR poly
319 800 mΩ/sq, local interconnect 12 800 mΩ/sq, N-diffusion
120 000 mΩ/sq, P-diffusion 197 000 mΩ/sq) and contact/via resistances.
Useful for inferring film thicknesses and materials (e.g. the 0.36 µm
and 0.845 µm aluminium metals). Tier: cross-check.
Also used on the CTM1, MM1, VIM and MM2 mask pages.

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
licence, links to documentation and the announcement list.
Also used on the metal plasma etcher page. Tier:
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
Also used on the FOM, DNM, LVTNM, NWM, HVTPM, PWBM, PWDEM, P1M, LICM1,
LI1M, CTM1, MM1, VIM, MM2 and VIM4 mask pages.

**PDK-HV** — *High Voltage Methodology* page.
<https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>.
Design methodology for the HV and VHV (drain-extended) devices: "The
VHV devices need to be designed with drain extentions (DE) fabricated
by lightly doped Nwells and Pwells respectively"; "All VHV devices use
110A gate oxide thickness just like standard 5.0V Vcc devices"; drawn
channel lengths of 1.055 µm and 1.050 µm for the 16 V VHV NMOS and
PMOS; "Under no circumstances the poly/extended drain overlap and
field oxide length should be changed". Tier: cross-check.
Also used on the NWM and PWDEM mask pages.

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
redistribution layer (4.0 µm RDL, 5.25 µm polyimide via).
Also used on the metal plasma etcher page. Tier:
high-level (numbers should be cross-checked against PDK-04).
Also used on the PVD cluster tool page.
Also used on the sputter targets material page.

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
PDK mask table set against MPW-1 to MPW-8, each run's columns headed by
a reticle-set ID such as `5CS8007AC`, recording for each run whether a
plate exists for each mask and its plate ID such as `S8007AA020A`, with
"Info" notes including the sky130B ReRAM masks `RRM` and `VIMC`);
"SKY130 MPW-3 Mask Information" (images of via-2 and via-3 plates);
"Random Mask Case Label Info" (Photronics plate-case labels: 6 × 6 ×
0.25 in blanks, 4×, CD specifications); and "Sheet4" (mask-type codes,
e.g. `F4-248-EAPSM-A43-APRX` for `VIM2`/`VIM3` and `B4-248-BIM-LSR-WET`
for `VIM4`). Each tab can be exported anonymously as CSV. Used on the
landing page, the steps index and every step page; the mask index uses
"Run Mask IDs" for the reticle-set IDs, plate IDs and plate numbers of
each run, "Masks" for the mask-step list, "Sheet4" for the mask-type
codes and "Random Mask Case Label Info" for the blank size and "4X"
type field.
Also used on the i-line stepper or scanner and DUV (KrF, 248 nm) stepper
or scanner pages.
Tier: cross-check.
Also used on the lithography materials material page.
Also used on the FOM, DNM, LVTNM, NWM, HVTPM, PWBM, PWDEM, P1M, LICM1,
LI1M, CTM1, MM1, VIM, MM2 and VIM4 mask pages.

**MASK-RENDERS** — *SKY130 Open MPW mask-layer renders* (public web
directory), retrieved 2026-09-13.
<https://data.wafer.space/big-storage/sky130-masks/> (start pages
<https://data.wafer.space/big-storage/sky130-masks/README.md> and
<https://data.wafer.space/big-storage/sky130-masks/masks.html>, and one
page per run, `mpw-001.html` to `mpw-008.html`). Images, for each of
the open MPW shuttle runs MPW-1 to MPW-8 and each of 42 mask layers, of
the drawn shapes in the 40 tape-out layouts placed on that run's
reticle, rendered from the public shuttle repositories under
<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>
(each slot's source file, reticle frame position and SHA-1 are named
in the metadata). Each run × mask directory (`<run>_<mask>/`) holds a
page, `job.json` and `result.json` (the drawn layers or the Boolean
`expr` rendered, per-mask notes, and run metadata: reticle-set ID, fab
lot where given, identification confidence, project count) and one
JSON file per die slot (die extent, shape count, source path), with a
PNG per die at 0.125 µm per pixel and a stitched reticle image at
0.5 µm per pixel. The README warns: "These are renders of *drawn* data,
not photomask artwork: reticle pitch, 4x reduction, mirroring and the
frame features the fab adds are not modelled. Empty images are real
results - several masks are used by no project on a given shuttle."
Frames A7 and C5 of each reticle are shown as "SkyWater test
structures" and not rendered. The `expr` definitions and notes are the
site's own reconstructions, not SkyWater data, and several notes use
the same wording as the notes in the process-steps sheet's "Run Mask
IDs" tab (STEPS-SHEET), so the two are not independent sources. Used
on the mask index, the HVTPM step page and the sky130B ReRAM overview.
Tier: cross-check.
Also used on the FOM, DNM, LVTNM, NWM, HVTPM, PWBM, PWDEM, P1M, LICM1,
LI1M, CTM1, MM1, VIM, MM2 and VIM4 mask pages.

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
niobium, 193 nm scanners, ALD).
Also used on the medium-current, high-current and high-energy implanter
pages.
Also used on the vertical-furnace oxidation, LPCVD and anneal pages and
the rapid thermal processor and plasma nitridation chamber pages.
Also used on the silicon and polysilicon plasma etcher, dielectric and
nitride plasma etcher, metal plasma etcher, downstream plasma asher and
wet bench and spray processor pages.
Also used on the PECVD, HDP-CVD, tungsten CVD and PVD cluster tool
pages.
Also used on the i-line stepper or scanner, DUV (KrF, 248 nm) stepper or
scanner, coat/develop track and CD-SEM and overlay metrology pages.
Also used on the starting-material machine page.
Also used on the single-wafer spin processor machine page.
Also used on the CMP polisher machine page.
Also used on the post-CMP cleaner machine page.
Also used on the defect and particle inspection, film thickness and stress
metrology, sheet-resistance and dose metrology, cross-section SEM and
profilers and parametric tester and prober pages.
Tier: cross-check (SkyWater statement).
Also used on the wet chemicals material page.
Also used on the lithography materials material page.
Also used on the sputter targets material page.
Also used on the substrates material page.
Also used on the CMP consumables material page.
Also used on the anneal ambients material page.
Also used on the ultrapure water material page.
Also used on the hardware consumables material page.
Also used on the process gases material page.
Also used on the dopant gases and implant sources material page.
Also used on the precursors material page.
Also used on the etch and chamber-clean gases material page.
Also used on the FOM, DNM, LVTNM, NWM, HVTPM, PWBM, PWDEM, P1M, LICM1,
LI1M, CTM1, MM1, VIM, MM2 and VIM4 mask pages.

**SKW-02** — SkyWater Technology, *"Mixed-Signal CMOS & Read Out IC
(ROIC)"* platform page, accessed 2026-08-30.
<https://www.skywatertechnology.com/cmos/>. Table of platforms: S130 —
"130nm CMOS", "200mm", metal layers "5: Al", local interconnect "1",
core 1.8 V, I/O "3.3V, 5.0V", high voltage "20+V, Drain-Extended CMOS
(16V)", "MiM Capacitor", "Precision Resistor", "Bulk" substrate; S90LN
— 90 nm, 7 Al metals, 2 dual-damascene local interconnect, 4 µm epi;
RH90 — 90 nm FD-SOI. Re-read 2026-09-13: the S130 column also gives
top metal "1.2 µm", "Mask Steps" "30 – 34", isolation "STI", gate
"Poly", precision resistors "2000Ω/□ 300Ω/□ (Both P-poly)", inductor
"No" and polyimide "Yes" (all used on the overview page). Tier:
cross-check.
Also used on the substrates material page.

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
Multibeam direct-write tool".
Also used on the DUV (KrF, 248 nm) stepper or scanner page.
Tier: cross-check (tool naming).

**SKW-07** — SkyWater Technology, *"A Day in the Life of a SkyWater
Maintenance Technician"*, 2023-12-14.
<https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>.
Names a "Novellus high density plasma tool" and the "SEZ etcher tool";
photo captions show technicians troubleshooting "an implanter" and,
separately, servicing tool robots (robot teach points, "a robot fault
on a Novellus high density plasma tool", "a motor for a robot on a SEZ
etcher tool") and "the pneumatic controls of a vacuum system". Tier:
cross-check (tool naming).
Also used on the HDP-CVD page.
Also used on the single-wafer spin processor machine page.
Also used on the CMP consumables material page.
Also used on the hardware consumables material page.

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
descriptive `User-Agent`.
Also used on the dielectric and nitride plasma etcher page.
Also used on the PVD cluster tool page.
Also used on the i-line stepper or scanner, DUV (KrF, 248 nm) stepper or
scanner and coat/develop track pages.
Also used on the starting-material machine page.
Also used on the CMP polisher machine page.
Tier: cross-check.
Also used on the wet chemicals material page.
Also used on the lithography materials material page.
Also used on the sputter targets material page, which also quotes the
"Business" section: "Before we began independent operations, our fab
was owned and operated by Cypress Semiconductor Corporation, or Cypress,
as a captive manufacturing facility for 20 years".
Also used on the substrates material page.
Also used on the CMP consumables material page.
Also used on the anneal ambients material page.
Also used on the ultrapure water material page.
Also used on the hardware consumables material page.
Also used on the process gases material page.
Also used on the dopant gases and implant sources material page.
Also used on the precursors material page.
Also used on the etch and chamber-clean gases material page.

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
Also used on the PVD cluster tool page.
Also used on the wet chemicals material page.
Also used on the lithography materials material page.
Also used on the sputter targets material page.
Also used on the substrates material page.
Also used on the CMP consumables material page.
Also used on the anneal ambients material page.
Also used on the ultrapure water material page.
Also used on the hardware consumables material page.
Also used on the process gases material page.
Also used on the dopant gases and implant sources material page.
Also used on the precursors material page.
Also used on the etch and chamber-clean gases material page.

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
which the step and machine pages read as KLA-Tencor's AIT
(patterned-wafer) and Surfscan SP1 (unpatterned-wafer) inspectors and an
eV300 review SEM (our reading; the posting expands none of the
abbreviations). Other
titles on the page (Equipment Maintenance Technician – Metrology,
Senior Metals Process Technician, Development Engineering Senior
Technician) name no tools.
Also used on the starting-material machine page.
Also used on the defect and particle inspection page.
Tier: cross-check (medium strength).

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
to life") but names no tools.
Also used on the silicon and polysilicon plasma etcher page.
Tier: high-level.

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
Sale of "the subsidiary that owns its semiconductor wafer fabrication
facility in Bloomington, Minnesota" for $30 M to SkyWater Technology
Foundry (Oxbow Industries), which the CEO's quotation calls "The sale of
Fab 4 in Minnesota"; wafer-supply agreement. Tier: cross-check.
Also used on the precursors material page.

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
Also used on the starting-material machine page.
Also used on the substrates material page.

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
Compares S65 with "the current 130-nanometer S8™ process" and states
that the S65 process "only requires three additional mask layers to a
standard CMOS process"; the mask count concerns S65, and no count is
given for S8. Tier: cross-check.

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
Also used on the dopant gases and implant sources material page.

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
3.0–5.0 nm.
Also used on the vertical-furnace oxidation and LPCVD pages.
Tier: deep dive.

**PAT-04** — US 8,796,098 B1, *"Embedded SONOS based memory cells"*,
K. Ramkumar, I. Kouznetsov, V. Prabhakar (Cypress); filed 2013-09-04,
granted 2014-08-05.
<https://patents.google.com/patent/US8796098B1/en>. Pad oxide 10–20 nm,
tunnel dielectric 1.0–4.0 nm, oxynitride charge-trapping layers
2.0–5.0 nm, blocking oxide ~3–4.5 nm, HV gate oxide 5–7 nm, LV gate
oxide 1–3 nm, indium channel doping.
Also used on the wet bench page. Tier: deep dive.
Also used on the wet chemicals material page.
Also used on the substrates material page.
Also used on the dopant gases and implant sources material page.

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
graduate text for this era.
Also used on the medium-current, high-current and high-energy implanter
pages.
Also used on the vertical-furnace oxidation, LPCVD and anneal pages and
the rapid thermal processor and plasma nitridation chamber pages.
Also used on the silicon and polysilicon plasma etcher and dielectric
and nitride plasma etcher pages.
Also used on the PECVD, HDP-CVD and tungsten CVD pages.
Tier: high-level.
Also used on the substrates material page.
Also used on the anneal ambients material page.
Also used on the process gases material page.

**TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
ISBN 978-0-9616721-6-4.
<https://openlibrary.org/isbn/9780961672164>. Unit processes (wafer
cleaning, oxidation, LPCVD/PECVD, sputtering, lithography, plasma
etch, implantation).
Also used on the high-energy implanter page.
Also used on the vertical-furnace LPCVD and anneal pages.
Also used on the silicon and polysilicon plasma etcher, dielectric and
nitride plasma etcher and metal plasma etcher pages.
Also used on the PECVD and PVD cluster tool pages.
Tier: high-level.
Also used on the sputter targets material page.
Also used on the anneal ambients material page.
Also used on the dopant gases and implant sources material page.
Also used on the precursors material page.
Also used on the DNM, NWM, PWBM and PWDEM mask pages.

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
generations.
Also used on the rapid thermal processor and plasma nitridation chamber
pages.
Also used on the tungsten CVD page.
Also used on the DUV (KrF, 248 nm) stepper or scanner page.
Tier: high-level.
Also used on the P1M mask page.

**TXT-06** — S. M. Sze (ed.), *VLSI Technology*, 2nd ed., McGraw-Hill,
1988, ISBN 978-0-07-062735-2.
<https://openlibrary.org/isbn/9780070627352>. Tier: high-level.

**TXT-07** — M. Quirk and J. Serda, *Semiconductor Manufacturing
Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
<https://openlibrary.org/isbn/9780130815200>. Fab-floor view of each
tool class, written around a 200 mm, 0.18 µm-era fab.
Also used on the medium-current and high-current implanter pages.
Also used on the vertical-furnace oxidation page.
Also used on the downstream plasma asher page.
Also used on the starting-material machine page.
Also used on the defect and particle inspection and film thickness and
stress metrology pages.
Tier: high-level.
Also used on the substrates material page.
Also used on the CMP consumables material page.
Also used on the ultrapure water material page.

**TXT-08** — H. Xiao, *Introduction to Semiconductor Manufacturing
Technology*, 2nd ed., SPIE Press, 2012, ISBN 978-0-8194-9092-6.
<https://openlibrary.org/isbn/9780819490926>; publisher page
<https://spie.org/Publications/Book/924283>. Tier: high-level.

**TXT-09** — Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
Manufacturing Technology*, 2nd ed., CRC Press, 2007,
ISBN 978-1-57444-675-3.
<https://openlibrary.org/isbn/9781574446753>. Chapter-per-process
reference with equipment detail.
Also used on the medium-current implanter page.
Also used on the vertical-furnace oxidation page and the rapid thermal
processor page.
Also used on the HDP-CVD page.
Tier: high-level.
Also used on the anneal ambients material page.
Also used on the hardware consumables material page.

**TXT-10** — R. B. Fair (ed.), *Rapid Thermal Processing: Science and
Technology*, Academic Press, 1993, ISBN 978-0-12-247690-7.
<https://openlibrary.org/isbn/9780122476907>.
Also used on the rapid thermal processor page.
Tier: deep dive.

### 8.2 ITRS roadmaps (2001 and 2003 editions)

Semiconductor Industry Association archive pages:
<https://www.semiconductors.org/resources/2001-international-technology-roadmap-for-semiconductors-itrs/>
and
<https://www.semiconductors.org/resources/2003-international-technology-roadmap-for-semiconductors-itrs/>.
The chapters most useful for a 130 nm flow (all verified PDFs):

**ITRS-01** — ITRS 2001, *Front End Processes*.
<https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>.
Starting material, STI, gate stack, junctions, contacts. Tier: deep dive.
Also used on the substrates material page.

**ITRS-02** — ITRS 2001, *Interconnect*.
<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Interconnect.pdf>.
Al versus Cu, dielectric k, via/metal dimensions by node. Tier: deep dive.

**ITRS-03** — ITRS 2001, *Lithography*.
<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>.
Exposure-tool options by node for critical layers ("248 nm + PSM" and
"193 nm" at the 130 nm node in Figure 34; "For critical layer imaging,
optical lithography is represented by three wavelengths—248 nm, 193 nm,
and 157 nm. Currently, only 248 nm lithography has a mature
infrastructure"); the optical mask table notes "The requirements are for
critical layers at defined year". It does not mention i-line or
exposure tools for non-critical layers. Table 57a gives half-pitch, gate
and contact CDs in resist and after etch, overlay and CD control by year
(2001: DRAM half-pitch 130 nm, contact 165 nm in resist, overlay 46 nm,
CD control 15.9 nm DRAM, 5.3 nm MPU gate, 7.3 nm ASIC/LP); Table 59a
gives mask magnification (4× in 2001), 45 nm overlay and "Primary PSM
choices are attenuated shifter and alternating aperture". The
requirements text says "contacts have very small process windows and
large mask error factors", and the metrology crosscut calls the "20%
measurement precision to process tolerance metric" "somewhat relaxed".
Also used on the CD-SEM and overlay metrology page.
Tier: deep dive.
Also used on the FOM, DNM, LVTNM, NWM, HVTPM, PWBM, PWDEM, P1M, LICM1,
LI1M, CTM1, MM1, VIM, MM2 and VIM4 mask pages.

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
Also used on the CMP polisher machine page.
Also used on the CMP consumables material page.

**REV-03** — E. K. Broadbent and C. L. Ramiller, *"Selective Low
Pressure Chemical Vapor Deposition of Tungsten"*, Journal of The
Electrochemical Society, vol. 131, no. 6, pp. 1427–1433, 1984,
DOI 10.1149/1.2115864.
<https://iopscience.iop.org/article/10.1149/1.2115864>. Foundational
WF₆/H₂ and WF₆/SiH₄ kinetics behind W plug fill. Tier: deep dive.
Also used on the tungsten CVD page.

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
contact measurements. Used on the test category page.
Also used on the sheet-resistance and dose metrology page.
Tier: high-level.

**WIKI-ADVANTEST** — Wikipedia, *Advantest*.
<https://en.wikipedia.org/wiki/Advantest> Company article on the
test-equipment maker Advantest. Used on the test category page. Tier:
high-level.

**WIKI-AGILENT** — Wikipedia, *Agilent Technologies*.
<https://en.wikipedia.org/wiki/Agilent_Technologies> Company article on
Agilent Technologies, successor to the HP test-and-measurement business
behind the 4062UX tester. Used on the test category page.
Also used on the parametric tester and prober page.
Tier: high-level.

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
Also used on the lithography materials material page.

**WIKI-ARRHENIUS** — Wikipedia, *Arrhenius equation*.
<https://en.wikipedia.org/wiki/Arrhenius_equation> Arrhenius temperature
dependence of rate constants, used for diffusion and etch rates. Used on
the anneal category page. Tier: high-level.

**WIKI-ASH** — Wikipedia, *Plasma ashing*.
<https://en.wikipedia.org/wiki/Plasma_ashing> Downstream ashing and
implanted-resist problems. Used on steps 016, 021, 025, 029 and 033 and
the strip category page.
Also used on the downstream plasma asher page.
Tier: high-level.
Also used on the anneal ambients material page.
Also used on the process gases material page.

**WIKI-ASH3** — Wikipedia, *Arsine*.
<https://en.wikipedia.org/wiki/Arsine> Arsine, the arsenic source gas
for implanters. Used on the implant category page, and on the
medium-current and high-current implanter pages. Tier: high-level.
Also used on the dopant gases and implant sources material page.

**WIKI-ASM** — Wikipedia, *ASM International*.
<https://en.wikipedia.org/wiki/ASM_International> Company article on ASM
International (vertical furnaces, ALD). Used on the substrate category
page. Tier: high-level.

**WIKI-ATE** — Wikipedia, *Automatic test equipment*.
<https://en.wikipedia.org/wiki/Automatic_test_equipment> Automatic test
equipment: what a tester and handler do at wafer sort and final test.
Used on the test category page.
Also used on the parametric tester and prober page.
Tier: high-level.

**WIKI-AXCELIS** — Wikipedia, *Axcelis Technologies*.
<https://en.wikipedia.org/wiki/Axcelis_Technologies> Company article on
Axcelis Technologies, the former Eaton implanter business. Used on the
implant category page, and on the medium-current, high-current and
high-energy implanter pages. Tier: high-level.

**WIKI-BF3** — Wikipedia, *Boron trifluoride*.
<https://en.wikipedia.org/wiki/Boron_trifluoride> Boron trifluoride, the
boron source gas for B⁺ and BF₂⁺ implants. Used on the implant category
page, and on the medium-current implanter page. Tier: high-level.
Also used on the dopant gases and implant sources material page.

**WIKI-BOE** — Wikipedia, *Buffered oxide etch*.
<https://en.wikipedia.org/wiki/Buffered_oxide_etch> BOE composition and
etch rate. Used on steps 039 and 046 and the etch category page.
Also used on the wet bench and spray processor page.
Tier:
high-level.
Also used on the wet chemicals material page.

**WIKI-CD** — Wikipedia, *Critical dimension*.
<https://en.wikipedia.org/wiki/Critical_dimension> Critical dimension:
the smallest printed feature and how it is measured. Used on the
lithography category page.
Also used on the CD-SEM and overlay metrology page.
Tier: high-level.

**WIKI-CERIA** — Wikipedia, *Cerium(IV) oxide*.
<https://en.wikipedia.org/wiki/Cerium(IV)_oxide> Cerium(IV) oxide, the
abrasive in high-selectivity STI slurries. Used on the cmp category
page. Tier: high-level.
Also used on the CMP consumables material page.

**WIKI-CHANNEL** — Wikipedia, *Channelling (physics)*.
<https://en.wikipedia.org/wiki/Channelling_(physics)> Ion channelling
along crystal axes and why implants use tilt and twist. Used on the
implant category page. Tier: high-level.

**WIKI-CMOS** — Wikipedia, *CMOS*. <https://en.wikipedia.org/wiki/CMOS>
NMOS on the p-substrate, PMOS in an N-well. Used on steps 017, 018 and
026. Tier: high-level.
Also used on the NWM and PWBM mask pages.

**WIKI-CMP** — Wikipedia, *Chemical-mechanical polishing*.
<https://en.wikipedia.org/wiki/Chemical-mechanical_polishing> Pads,
conditioners, abrasives, endpoint and REB + CMP for STI. Used on step
012 and the cmp category page. Tier: high-level.
Also used on the CMP polisher machine page.
Also used on the CMP consumables material page.

**WIKI-COLLOIDAL-SILICA** — Wikipedia, *Colloidal silica*.
<https://en.wikipedia.org/wiki/Colloidal_silica> Colloidal silica, the
abrasive in conventional oxide slurries. Used on the cmp category page.
Tier: high-level.
Also used on the CMP consumables material page.

**WIKI-CTF** — Wikipedia, *Charge trap flash*.
<https://en.wikipedia.org/wiki/Charge_trap_flash> Why trapped charge
tolerates oxide defects. Used on step 040. Tier: high-level.

**WIKI-CVD** — Wikipedia, *Chemical vapor deposition*.
<https://en.wikipedia.org/wiki/Chemical_vapor_deposition> LPCVD in
context. Used on step 003 and the deposition category page.
Also used on the vertical-furnace LPCVD page.
Tier: high-level.

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
the photoactive compound of i-line novolac resists. Used on the
lithography category page.
Also used on the i-line stepper or scanner page.
Tier: high-level.
Also used on the lithography materials material page.

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
Also used on the sputter targets material page.

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
lithography category page and step 159.
Also used on the DUV (KrF, 248 nm) stepper or scanner page.
Tier: high-level.
Also used on the lithography materials material page.

**WIKI-FG** — Wikipedia, *Forming gas*.
<https://en.wikipedia.org/wiki/Forming_gas> The 5 % H₂ in N₂ mixture and
interface passivation. Used on the anneal category page.
Also used on the vertical-furnace anneal page.
Tier: high-level.
Also used on the anneal ambients material page.
Also used on the process gases material page.

**WIKI-FICK** — Wikipedia, *Fick's laws of diffusion*.
<https://en.wikipedia.org/wiki/Fick%27s_laws_of_diffusion> Fick's laws,
the basis of diffusion and Deal–Grove modelling. Used on the anneal
category page. Tier: high-level.

**WIKI-FURNACE** — Wikipedia, *Furnace anneal*.
<https://en.wikipedia.org/wiki/Diffusion_furnace> Furnace anneals being
supplanted by RTA. The label keeps the page's *Furnace anneal* wording;
the article is titled *Diffusion furnace*. Used on step 034 and the
anneal category page.
Also used on the vertical-furnace anneal page.
Tier: high-level.

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
Also used on the substrates material page.

**WIKI-H3PO4** — Wikipedia, *Phosphoric acid*.
<https://en.wikipedia.org/wiki/Phosphoric_acid> Phosphoric acid, the hot
nitride-strip chemistry. Used on the etch and strip category pages.
Also used on the wet bench and spray processor page.
Tier: high-level.
Also used on the wet chemicals material page.

**WIKI-HF** — Wikipedia, *Hydrofluoric acid*.
<https://en.wikipedia.org/wiki/Hydrofluoric_acid> Hydrofluoric acid, the
oxide etchant, and its hazards. Used on the etch and strip category
pages.
Also used on the wet bench and spray processor page.
Also used on the single-wafer spin processor machine page.
Tier: high-level.
Also used on the wet chemicals material page.

**WIKI-ICP** — Wikipedia, *Inductively coupled plasma*.
<https://en.wikipedia.org/wiki/Inductively_coupled_plasma> Inductively
coupled plasma, the source type behind TCP and DPS etchers. Used on the
etch category page.
Also used on the silicon and polysilicon plasma etcher page.
Tier: high-level.

**WIKI-IMPLANT** — Wikipedia, *Ion implantation*.
<https://en.wikipedia.org/wiki/Ion_implantation> Energies, ranges,
channelling, amorphisation and implanter classes. Used on steps 007,
008, 015, 018, 019, 020, 023, 024, 027, 028, 031, 032, 037, 038 and 045
and the implant category page, and on the medium-current, high-current
and high-energy implanter pages. Tier: high-level.
Also used on the process gases material page.
Also used on the dopant gases and implant sources material page.
Also used on the DNM, LVTNM, NWM, HVTPM, PWBM and PWDEM mask pages.

**WIKI-KEITHLEY** — Wikipedia, *Keithley Instruments*.
<https://en.wikipedia.org/wiki/Keithley_Instruments> Company article on
Keithley Instruments (parametric test systems). Used on the test
category page.
Also used on the parametric tester and prober page.
Tier: high-level.

**WIKI-KLA** — Wikipedia, *KLA Corporation*.
<https://en.wikipedia.org/wiki/KLA_Corporation> The inspection and
metrology vendor. Used on the lithography and substrate category pages.
Also used on the CD-SEM and overlay metrology page.
Also used on the starting-material machine page.
Also used on the defect and particle inspection page.
Tier: high-level.

**WIKI-LATCHUP** — Wikipedia, *Latch-up*.
<https://en.wikipedia.org/wiki/Latch-up> The parasitic n-p-n-p path
through the wells. Used on steps 017, 018 and 027 and the substrate
category page. Tier: high-level.
Also used on the NWM mask page.

**WIKI-LDMOS** — Wikipedia, *LDMOS*.
<https://en.wikipedia.org/wiki/LDMOS> Drift regions formed by chained
implants. Used on steps 030, 031 and 032. Tier: high-level.

**WIKI-LITHO** — Wikipedia, *Photolithography*.
<https://en.wikipedia.org/wiki/Photolithography> The process sequence,
the resolution equation and wavelengths. Used on steps 004, 007, 014,
017, 022, 026, 030, 035, 041 and 044 and the lithography category page.
Also used on the i-line stepper or scanner, DUV (KrF, 248 nm) stepper or
scanner and coat/develop track pages.
Tier: high-level.
Also used on the lithography materials material page.
Also used on the FOM and DNM mask pages.

**WIKI-LOCOS** — Wikipedia, *LOCOS*.
<https://en.wikipedia.org/wiki/LOCOS> LOCOS isolation, the predecessor
of STI. Used on the oxidation category page. Tier: high-level.

**WIKI-MASK** — Wikipedia, *Photomask*.
<https://en.wikipedia.org/wiki/Photomask> Photomasks: substrates,
absorber and pellicles. Used on the lithography category page. Tier:
high-level.
Also used on the lithography materials material page.
Also used on the FOM, DNM, LVTNM, HVTPM, PWBM, PWDEM, P1M, LICM1, LI1M,
CTM1, MM1, VIM, MM2 and VIM4 mask pages.

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
Also used on the LVTNM and HVTPM mask pages.

**WIKI-NA** — Wikipedia, *Numerical aperture*.
<https://en.wikipedia.org/wiki/Numerical_aperture> Numerical aperture
and its place in the Rayleigh resolution criterion. Used on the
lithography category page. Tier: high-level.

**WIKI-NMP** — Wikipedia, *N-Methyl-2-pyrrolidone*.
<https://en.wikipedia.org/wiki/N-Methyl-2-pyrrolidone>
N-Methyl-2-pyrrolidone, a solvent-strip chemistry. Used on the strip
category page.
Also used on the wet bench and spray processor page.
Tier: high-level.

**WIKI-OPC** — Wikipedia, *Optical proximity correction*.
<https://en.wikipedia.org/wiki/Optical_proximity_correction> Optical
proximity correction of mask shapes. Used on the lithography category
page. Tier: high-level.
Also used on the P1M, LICM1, LI1M, MM1 and MM2 mask pages.

**WIKI-PECVD** — Wikipedia, *Plasma-enhanced chemical vapor deposition*.
<https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
High-density plasma, sputtering during deposition, SiH₄/O₂/Ar oxide.
Used on step 011 and the deposition category page. Tier: high-level.
Also used on the PECVD and HDP-CVD pages.

**WIKI-PH3** — Wikipedia, *Phosphine*.
<https://en.wikipedia.org/wiki/Phosphine> Phosphine, the phosphorus
source gas for implanters. Used on the implant category page, and on the
medium-current and high-energy implanter pages. Tier:
high-level.
Also used on the HDP-CVD page.
Also used on the dopant gases and implant sources material page.

**WIKI-PIRANHA** — Wikipedia, *Piranha solution*.
<https://en.wikipedia.org/wiki/Piranha_solution> SPM ratios and
temperature. Used on the strip category page.
Also used on the wet bench and spray processor page.
Tier: high-level.
Also used on the wet chemicals material page.

**WIKI-PLASMA-ETCH** — Wikipedia, *Plasma etching*.
<https://en.wikipedia.org/wiki/Plasma_etching> Plasma etching mechanisms
and chemistries. Used on the etch category page.
Also used on the silicon and polysilicon plasma etcher and metal plasma
etcher pages.
Tier: high-level.

**WIKI-POLY** — Wikipedia, *Polycrystalline silicon*.
<https://en.wikipedia.org/wiki/Polycrystalline_silicon> Polycrystalline
silicon as a gate and resistor material. Used on the deposition category
page. Tier: high-level.

**WIKI-POLYURETHANE** — Wikipedia, *Polyurethane*.
<https://en.wikipedia.org/wiki/Polyurethane> Polyurethane, the CMP pad
material. Used on the cmp category page. Tier: high-level.

**WIKI-PROBECARD** — Wikipedia, *Probe card*.
<https://en.wikipedia.org/wiki/Probe_card> Probe cards for wafer test.
Used on the test category page.
Also used on the parametric tester and prober page.
Tier: high-level.
Also used on the hardware consumables material page.

**WIKI-PSG** — Wikipedia, *Phosphosilicate glass*.
<https://en.wikipedia.org/wiki/Phosphosilicate_glass> Phosphosilicate
glass, the doped CVD dielectric. Used on the deposition category page.
Tier: high-level.

**WIKI-PSM** — Wikipedia, *Phase-shift mask*.
<https://en.wikipedia.org/wiki/Phase-shift_mask> Phase-shift masks as a
resolution-enhancement technique. Used on the lithography category page.
Tier: high-level.
Also used on the P1M, LICM1, CTM1 and VIM mask pages.

**WIKI-PVD** — Wikipedia, *Physical vapor deposition*.
<https://en.wikipedia.org/wiki/Physical_vapor_deposition> Physical
vapour deposition overview. Used on the deposition category page. Tier:
high-level.
Also used on the PVD cluster tool page.
Also used on the sputter targets material page.

**WIKI-RC** — Wikipedia, *Contact resistance*.
<https://en.wikipedia.org/wiki/Contact_resistance> Contact resistance
and specific contact resistivity. Used on the test category page. Tier:
high-level.

**WIKI-RCA** — Wikipedia, *RCA clean*.
<https://en.wikipedia.org/wiki/RCA_clean> SC-1 and SC-2 compositions and
temperatures. Used on steps 001, 002, 006, 009, 010, 013, 016, 021, 025,
029, 033, 039 and 046 and the strip category page.
Also used on the wet bench and spray processor page.
Also used on the post-CMP cleaner machine page.
Tier: high-level.
Also used on the wet chemicals material page.
Also used on the ultrapure water material page.

**WIKI-RESIST** — Wikipedia, *Photoresist*.
<https://en.wikipedia.org/wiki/Photoresist> Photoresist chemistry, tone
and processing. Used on the lithography and strip category pages. Tier:
high-level.
Also used on the lithography materials material page.

**WIKI-RET** — Wikipedia, *Resolution enhancement technologies*.
<https://en.wikipedia.org/wiki/Resolution_enhancement_technologies>
Resolution enhancement technologies: OPC, phase-shift masks and off-axis
illumination. Used on the lithography category page. Tier: high-level.

**WIKI-RIE** — Wikipedia, *Reactive-ion etching*.
<https://en.wikipedia.org/wiki/Reactive-ion_etching> RF frequency,
self-bias, pressure range and ICP sources. Used on steps 005, 006, 036
and 042 and the etch category page.
Also used on the silicon and polysilicon plasma etcher, dielectric and
nitride plasma etcher and metal plasma etcher pages.
Tier: high-level.

**WIKI-RS** — Wikipedia, *Sheet resistance*.
<https://en.wikipedia.org/wiki/Sheet_resistance> Sheet resistance and
the ohms-per-square convention. Used on the test category page.
Also used on the sheet-resistance and dose metrology page.
Tier: high-level.

**WIKI-RTP** — Wikipedia, *Rapid thermal processing*.
<https://en.wikipedia.org/wiki/Rapid_thermal_processing> Lamp heating,
seconds above 1000 °C, in-situ pyrometry. Used on step 034 and the
anneal and oxidation category pages.
Also used on the rapid thermal processor page.
Tier: high-level.

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
and 135 and the deposition category page.
Also used on the vertical-furnace LPCVD page.
Tier: high-level.

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
Also used on the PVD cluster tool page.
Also used on the sputter targets material page.

**WIKI-SRIM** — Wikipedia, *Stopping and Range of Ions in Matter*.
<https://en.wikipedia.org/wiki/Stopping_and_Range_of_Ions_in_Matter>
SRIM, the Monte Carlo range and straggle calculator for implants. Used
on the implant category page. Tier: high-level.

**WIKI-STEPPER** — Wikipedia, *Stepper*.
<https://en.wikipedia.org/wiki/Stepper> Steppers and step-and-scan
systems: reduction optics, alignment and overlay. Used on the
lithography category page.
Also used on the i-line stepper or scanner and DUV (KrF, 248 nm) stepper
or scanner pages.
Tier: high-level.

**WIKI-STI** — Wikipedia, *Shallow trench isolation*.
<https://en.wikipedia.org/wiki/Shallow_trench_isolation> The three STI
operations and the LOCOS cross-over node. Used on steps 002, 003, 005,
006, 007, 011, 012 and 013 and the cmp and oxidation category pages.
Tier: high-level.
Also used on the FOM mask page.

**WIKI-SUMCO** — Wikipedia, *SUMCO*.
<https://en.wikipedia.org/wiki/SUMCO> Company article on the wafer maker
SUMCO. Used on the substrate category page. Tier: high-level.

**WIKI-TEOS** — Wikipedia, *Tetraethyl orthosilicate*.
<https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate> Tetraethyl
orthosilicate, the liquid precursor for CVD oxide. Used on the
deposition category page. Tier: high-level.
Also used on the PECVD page.
Also used on the precursors material page.

**WIKI-TERADYNE** — Wikipedia, *Teradyne*.
<https://en.wikipedia.org/wiki/Teradyne> Company article on the
test-equipment maker Teradyne. Used on the test category page. Tier:
high-level.

**WIKI-TEST** — Wikipedia, *Wafer testing*.
<https://en.wikipedia.org/wiki/Wafer_testing> Parametric versus
functional test and the wafermap. Used on the test category page.
Also used on the parametric tester and prober page.
Tier: high-level.

**WIKI-THINFILM** — Wikipedia, *Thin film*.
<https://en.wikipedia.org/wiki/Thin_film> Thin films: deposition methods
and properties. Used on the deposition category page. Tier: high-level.

**WIKI-THOX** — Wikipedia, *Thermal oxidation*.
<https://en.wikipedia.org/wiki/Thermal_oxidation> Reaction, silicon
consumption, chlorine additions and dry–wet–dry cycles. Used on steps
002, 010, 038 and 043 and the oxidation category page.
Also used on the vertical-furnace oxidation and anneal pages.
Tier: high-level.
Also used on the process gases material page.

**WIKI-TIN** — Wikipedia, *Titanium nitride*.
<https://en.wikipedia.org/wiki/Titanium_nitride> Titanium nitride as a
barrier and local-interconnect material. Used on the deposition category
page. Tier: high-level.
Also used on the PVD cluster tool page.
Also used on the sputter targets material page.

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
Used on the lithography category page.
Also used on the coat/develop track page.
Tier: high-level.
Also used on the lithography materials material page.

**WIKI-VARIAN** — Wikipedia, *Varian Semiconductor*.
<https://en.wikipedia.org/wiki/Varian_Semiconductor> Company article on
Varian Semiconductor Equipment (implanters; now part of Applied
Materials). Used on the implant category page, and on the
medium-current, high-current and high-energy implanter pages. Tier:
high-level.

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
Also used on the starting-material machine page.
Also used on the substrates material page.

**WIKI-WF6** — Wikipedia, *Tungsten hexafluoride*.
<https://en.wikipedia.org/wiki/Tungsten_hexafluoride> Tungsten
hexafluoride, the CVD tungsten precursor. Used on the deposition
category page. Tier: high-level.
Also used on the tungsten CVD page.
Also used on the precursors material page.

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
the selectivity behind every wet nitride strip.
Also used on the wet bench and spray processor page.
Tier: deep dive.
Also used on the wet chemicals material page.

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
as "Thung Beng Joo" (family name Thung).
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep dive.
Also used on the FOM mask page.

**NISHIMURA-2002** — H. Nishimura, S. Takagi, M. Fujino and N. Nishi,
*"Gap-Fill Process of Shallow Trench Isolation for 0.13 µm
Technologies"*, Japanese Journal of Applied Physics, vol. 41, part 1,
no. 5A, pp. 2886–2893, 2002, DOI 10.1143/JJAP.41.2886. HDP-CVD
gap-fill modelling (sputter-yield angular dependence and ionic
deposition) demonstrated on STI "of space width 0.13 µm and aspect
ratio 3.9". Tier: deep dive.
Also used on the HDP-CVD page.

**CHEW-2002** — K. W. Chew, J. Zhang, K. Shao, W. B. Loh and S.-F. Chu,
*"Impact of Deep N-well Implantation on Substrate Noise Coupling and RF
Transistor Performance for Systems-on-a-Chip Integration"*, ESSDERC
2002, pp. 251–254, DOI 10.1109/ESSDERC.2002.194917. Deep N-well as a
substrate-noise isolation structure. Tier: deep dive.
Also used on the DNM mask page.

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
Also used on the high-energy implanter page.
Tier: deep dive.
Also used on the DNM mask page.

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
Also used on the HDP-CVD page.

**AXCELIS-GSD** — Axcelis Technologies, *"Axcelis Announces
Introduction Of The 'GSD Ovation' High Current And High Energy Batch
Implanters"*, PR Newswire, 2021-11-02.
<https://www.prnewswire.com/news-releases/axcelis-announces-introduction-of-the-gsd-ovation-high-current-and-high-energy-batch-implanters-301412520.html>.
Calls the GSD series "the industry benchmark for the longest
manufactured and supported batch ion implanter" and names "the GSD/HE
Ovation with energies up to 3 MeV, and the GSD/VHE Ovation with
energies up to 4.9 MeV".
Also used on the high-current and high-energy implanter pages.
Tier: cross-check (vendor statement).

**SNF-9400** — Stanford Nanofabrication Facility, *"Lam Research TCP
9400 Poly Etcher (lampoly)"* equipment page.
<https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>.
"a Transformer Coupled Plasma (TCP) etcher, generates a uniform, high
density plasma for selective etching of silicon and polysilicon"; the
gas list includes chlorine, hydrogen bromide, oxygen and
tetrafluoromethane.
Also used on the silicon and polysilicon plasma etcher page.
Tier: high-level.

**AVIZA-AVP** — Moov used-equipment marketplace, *"Aviza / SVG /
Thermco AVP 8000"* listing.
<https://moov.co/marketplace/furnaces-diffusion/aviza-svg/aviza-asml-svg-watkinsjohnson-avp-8000>.
"The AVP-8000 is a vertical batch furnace with a flexible platform for
diffusion, oxidation, and LPCVD processes … can handle 150-200mm
wafers." A dealer listing rather than a vendor data sheet.
Also used on the vertical-furnace oxidation, LPCVD and anneal pages.
Tier: high-level (weak).
Also used on the anneal ambients material page.

**AXCELIS-GSD-PAGE** — Axcelis Technologies, *"GSD Ovation — High
Current & High Energy Batch Ion Implanters"*, product page, accessed
2026-08-30. <https://www.axcelis.com/products/gsd-ovation/>. Describes
the GSD/HE as a "10 stage LINAC with energies up to 3 MeV" and notes
"source operating costs especially with fluorinated species". Distinct
from the PR Newswire release AXCELIS-GSD.
Also used on the high-current and high-energy implanter pages.
Tier: cross-check (vendor
statement).
Also used on the dopant gases and implant sources material page.

**AXCELIS-8250** — Semiconductor Online, *"8250HT Medium Current Ion
Implanter"* (Eaton Semiconductor Equipment Operations product
description).
<https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>.
The 8250HT covers "3keV to 750keV" with beam currents "between 4µA and
3,500µA"; the medium-current class that SKW-01 lists as "Axcelis 8250".
Also used on the medium-current implanter page.
Tier: high-level (vendor description reproduced by a trade site).

**AG-8800** — SemiStar Corp., *"AG Associates Heatpulse 8800 / 8808
Rapid Thermal Processing"* (reseller specification page), accessed
2026-08-30.
<https://www.semistarcorp.com/product/ag-associates-heatpulse-8800-8808/>.
"Recommended steady-state temperature range: 400 – 1200°C", ramp-up
"Programmable, 1 – 180°C per second", "2 banks of 14 lamps" with
"10-zone lamp control", pyrometer or thermocouple sensing, wafer sizes
to 8 inches, "Implant annealing" among the applications. Its operating
specifications are word for word the 8108 section of the same reseller's
PDF (AG-8108), not its 8800 section (checked 2026-09-13).
Also used on the rapid thermal processor page.
Tier: high-level (reseller page for the tool SKW-01 lists as "Ag Heatpulse
8808").
Also used on the hardware consumables material page.

**AG-8108** — SemiStar Corp., *"AG Associates Heatpulse 4100 / 8108 /
8800 / 8800i Specifications"* (reseller PDF), accessed 2026-08-30.
<https://www.semistarcorp.com/wp-content/uploads/2025/12/AG-Associates-Heatpulse-4100-8108-8800-8800i-Specifications-Rapid-Thermal-Processor.pdf>.
Re-read on 2026-09-13, the PDF has operating-specification, dimension
and facility sections for the Heatpulse 4100 (400–1300 °C; ramp-up
"10°C to 200°C per second"; ±5 °C across a 150 mm wafer at 1150 °C),
the 8108 (400–1200 °C; ramp-up "1 - 180°C per second"; ±5 °C across an
8-inch wafer at 1150 °C) and the 8800 and 8800i (400–1200 °C; ramp-up
"up to 100°C per second with Ceramic Shield; up to 150°C per second
without Ceramic Shield"; ±3 °C across an 8-inch wafer at 1150 °C), with
facility tables (cooling water, CDA/N₂, exhausts). No section names the
8808.
Also used on the rapid thermal processor page.
Tier: high-level (weak for the 8808 itself).
Also used on the hardware consumables material page.

**GASONICS-2000** — GaSonics International, home page, Wayback Machine
capture of 2000-03-01.
<https://web.archive.org/web/20000301102837/http://www.gasonics.com:80/>
The company styles itself "GaSonics International", "a leading supplier
of semiconductor processing equipment", with photoresist removal and
wafer cleaning among its applications. Used on the machines index for the spelling of the vendor name.
Also used on the downstream plasma asher page.
Tier: cross-check (vendor statement).

**MATTSON-2001** — Mattson Technology, *The Aspen Strip*, product page,
Wayback Machine capture of 2001-12-19.
<https://web.archive.org/web/20011219013713/http://www.mattson.com/products/aspen_strip.html>
Names the "Aspen II Strip" and "Aspen III Strip" systems built on the
"Aspen II platform" and "Aspen III platform". Used on the machines index
for the spelling of the platform name.
Also used on the downstream plasma asher page.
Tier: cross-check (vendor
statement).
Also used on the anneal ambients material page.

**SEZ-2005** — SEZ Group, *World-Leading Korean Manufacturer Places
Multi-System Order for SEZ Da Vinci Tools*, press release, 2005-03-02,
Wayback Machine capture of 2009-01-07.
<https://web.archive.org/web/20090107032902/http://www.sez.com/02_Mar_05__World_Leading_Korean_Manufacturer_Places_Multi_System_Order_for_SEZ_Da_Vinci__Tools.SEZ>
SEZ's "Da Vinci™ family of cleaning tools" (DV-38F systems for 300 mm
back-end polymer removal); "Having sold the first Da Vinci tool in Q2
04". Used on the machines index for the spelling of the tool name.
Also used on the single-wafer spin processor machine page.
Tier: cross-check (vendor statement).

**TEL-LITHIUS** — Tokyo Electron, *Coater/Developer LITHIUS Series*,
product page, accessed 2026-09-13.
<https://www.tel.com/product/lithius.html> Describes the "CLEAN TRACK™
LITHIUS Pro™ Z" as "TEL's most advanced 300mm coater/developer for the
10nm technology node and beyond" and the original "CLEAN TRACK™
LITHIUS™" as "a 300/200mm coater/developer". Used on the machines index
to explain why SkyWater's "TEL ProZ Lithius track" is not identified
with a model.
Also used on the coat/develop track page.
Tier: cross-check (vendor statement).

**PHOTRONICS-ABR** — Photronics, Inc., *Advanced Binary Reticle*,
product page, retrieved 2026-09-13.
<https://www.photronics.com/products/advanced-binary-reticle/> Describes
the company's "advanced binary reticles", with the resist pattern
"transferred to the chrome absorber layer" by dry etch, and, under
"Specialty Phase-Shift Masks", states "At 248nm and 193nm wavelengths,
our embedded attenuated phase-shift masks (EAPSM) rely on a
wavelength-tuned, 6% transmission MoSiON absorber". The page does not state a reduction ratio.
Used on the mask index and steps 129, 144 and 159 for the mask maker's
name and abbreviation for an embedded attenuated phase-shift mask. Tier: cross-check (vendor
statement).
Also used on the lithography materials material page.
Also used on the VIM4 mask page.

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
Also used on the LVTNM and HVTPM mask pages.

**PAT-VT-LSI** — US 5,963,801 A, *"Method of forming retrograde well
structures and punch-through barriers using low energy implants"*,
S. Aronowitz, L. Khan and J. Kimball (LSI Logic), granted 1999-10-05.
<https://patents.google.com/patent/US5963801A/en>. Threshold-adjust
boron "implanted through the sacrificial gate oxide in doses between
1×10¹² and 1×10¹³ atoms/cm² … at implant energies between 50 and
100 keV"; chained punch-through barriers at 100, 70 and 50 keV; a well
anneal "at approximately 900° C. in a neutral ambient such as nitrogen
for approximately 30 minutes" (the patent does not name the tool).
Also used on the vertical-furnace anneal page.
Tier: deep dive.

**PAT-VT-AMD** — US 6,238,982 B1, *"Multiple threshold voltage
semiconductor device fabrication technology"*, Z. Krivokapic and
O. Milic (AMD), granted 2001-05-29.
<https://patents.google.com/patent/US6238982B1/en>. Channel implant
"approximately 10-20 KeV for boron or 45-90 KeV for BF₂ at a
concentration of about 1.0 to 2.5×10¹³ ions/cm²". Tier: deep dive.
Also used on the HVTPM mask page.

**PAT-WELL-IBM** — US 6,667,205 B2, *"Method of forming retrograde
n-well and p-well"*, M. J. Breitwisch, C. H. Lam and J. A. Slinkman
(IBM), granted 2003-12-23.
<https://patents.google.com/patent/US6667205B2/en>. Photoresist
"typically 1800–2500 nm in thickness"; N-well phosphorus 850 keV at
5.2 × 10¹³ cm⁻², 550 keV at 1.25 × 10¹² cm⁻² and 50 keV at
5 × 10¹¹ cm⁻²; P-well boron 550, 150 and 45 keV; "The concentration of
dopant is higher at the bottom of the well and lower at the upper
surface of the well".
Also used on the high-energy implanter page.
Tier: deep dive.
Also used on the NWM, PWBM and PWDEM mask pages.

**PAT-WELL-HYNIX** — US 6,455,402 B2, *"Method of forming retrograde
doping profile in twin well CMOS device"*, J.-H. Lee and J.-H. Son
(Hyundai/Hynix), granted 2002-09-24.
<https://patents.google.com/patent/US6455402B2/en>. N-well 700 keV at
2.0 × 10¹³ cm⁻² plus 120 keV at 2.0 × 10¹² cm⁻²; P-well 350 keV at
1.5 × 10¹³ cm⁻², 150 keV at 6.0 × 10¹² cm⁻² and 80 keV at
1.0 × 10¹² cm⁻²; "an annealing at 1000 C for 10 sec in an RTA" before
gate oxidation.
Also used on the vertical-furnace anneal page.
Tier: deep dive.
Also used on the PWBM mask page.

**PAT-TWIN-HARRIS** — US 5,247,199 A, *"Process for forming twin well
CMOS integrated circuits"*, D. A. Matlock (Harris Corporation), granted
1993-09-21. <https://patents.google.com/patent/US5247199A/en>. Twin
wells by chained implants — 500/275/130 keV phosphorus and
360/185/55 keV boron — with "an implant blocking photoresist layer 18"
patterned to expose the region "adjacent to N-type well 17". Tier:
deep dive.
Also used on the PWBM mask page.

**PAT-UMC-DC** — US 5,393,679 A, *"Use of double charge implant to
improve retrograde process PMOS punch through voltage"*, S.-H. Yang
(United Microelectronics), granted 1995-02-28.
<https://patents.google.com/patent/US5393679A/en>. Retrograde well by
"double charge … P++ … at an energy within a range from about 380 keV
to about 400 keV" on a medium-current implanter.
Also used on the medium-current and high-energy implanter pages.
Tier: deep dive.

**PAT-RESIST-ZILOG** — US 6,576,405 B1, *"High aspect ratio
photolithographic method for high energy implantation"*, S. J. Buffat
and J. L. Adams (Zilog), granted 2003-06-10.
<https://patents.google.com/patent/US6576405B1/en>. Resist "minimum
thicknesses of 3.4 µm … with the preferred thickness for the resist
between 3.8 µm and 4.2 µm" for a 1.3–1.5 MeV phosphorus N-well and a
600–800 keV boron P-well.
Also used on the i-line stepper or scanner page.
Tier: deep dive.
Also used on the DNM, NWM and PWBM mask pages.

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
Also used on the NWM and PWDEM mask pages.

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
environment".
Also used on the downstream plasma asher page.
Tier: deep dive.

**PAT-STRIP-TSMC** — US 2004/0214448 A1, *"Method of ashing a
photoresist"*, B.-W. Chan, Y.-H. Chiu and H.-J. Tao (TSMC), published
2004-10-28. <https://patents.google.com/patent/US20040214448A1/en>.
After implantation "the top portion of the photoresist layer is
transformed into a carbonized crust that is difficult to remove because
of its low solubility in wet strippers".
Also used on the downstream plasma asher page.
Tier: deep dive.

**PAT-STRIP-ULVAC** — US 5,795,831 A, *"Cold processes for cleaning
and stripping photoresist from surfaces of semiconductor wafers"*,
I. Nakayama et al. (ULVAC Technologies), granted 1998-08-18.
<https://patents.google.com/patent/US5795831A/en>. A cold stripping
and cleaning process for implanted resist, an alternative to hot
ashing.
Also used on the downstream plasma asher page.
Tier: deep dive.

**PAT-RESURF-TI** — US 5,406,110 A, *"Resurf lateral double diffused
insulated gate field effect transistor"*, O.-K. Kwon, T. R. Efland,
S. Malhi and W. T. Ng (Texas Instruments), granted 1995-04-11.
<https://patents.google.com/patent/US5406110A/en>. A RESURF lateral
DMOS with an implanted drift region. Tier: deep dive.

**PAT-RTP-AMAT** — US 5,155,336 A, *"Rapid thermal heating apparatus
and method"*, C. M. Gronet and J. F. Gibbons (Applied Materials),
granted 1992-10-13. <https://patents.google.com/patent/US5155336A/en>.
A lamp-heated single-wafer RTP chamber design.
Also used on the rapid thermal processor page.
Tier: deep dive.

**PAT-RTP-TAMARACK** — US 4,649,261 A, *"Apparatus for heating
semiconductor wafers in order to achieve annealing, silicide
formation, reflow of glass passivation layers, etc."*, R. E. Sheets
(Tamarack Scientific), granted 1987-03-10.
<https://patents.google.com/patent/US4649261A/en>. An early
lamp-heating apparatus for wafer annealing.
Also used on the rapid thermal processor page.
Tier: deep dive.

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
"2.3 µm-thick pwell mask".
Also used on the high-energy implanter page.
Tier: deep dive.
Also used on the LVTNM, NWM, HVTPM and PWBM mask pages.

**SHEU-2006** — Y.-M. Sheu, K.-W. Su, S. Tian, S.-J. Yang, C.-C. Wang,
M.-J. Chen and S. Liu, *"Modeling the Well-Edge Proximity Effect in
Highly Scaled MOSFETs"*, IEEE Transactions on Electron Devices,
vol. 53, no. 11, pp. 2792–2798, 2006, DOI 10.1109/TED.2006.884070. A
compact model of the well-edge proximity effect. Tier: deep dive.
Also used on the LVTNM, NWM, HVTPM and PWBM mask pages.

**DRENNAN-2006** — P. G. Drennan, M. Kniffin and D. Locascio,
*"Implications of Proximity Effects for Analog Design"*, IEEE Custom
Integrated Circuits Conference 2006, pp. 169–176,
DOI 10.1109/CICC.2006.320869. Designer-side consequences of the well
proximity effect. Tier: deep dive.
Also used on the LVTNM and HVTPM mask pages.

**MORRIS-2000** — W. Morris and L. Rubin, *"Technical and economic
considerations for retrograde well and channel implants"*, 2000
International Conference on Ion Implantation Technology, pp. 73–76,
DOI 10.1109/IIT.2000.924093. Why MeV retrograde wells replaced diffused
wells, with the cost trade-offs.
Also used on the medium-current and high-energy implanter pages.
Tier: deep dive.
Also used on the NWM mask page.

**RUBIN-2002** — L. M. Rubin, W. Morris and C. Jasper, *"Process
control issues for retrograde well implants for narrow n+/p+ isolation
in CMOS"*, 2002 International Conference on Ion Implantation
Technology, pp. 17–20, DOI 10.1109/IIT.2002.1257927. How well-implant
control sets the n⁺/p⁺ isolation spacing.
Also used on the high-energy implanter page.
Tier: deep dive.
Also used on the NWM and PWBM mask pages.

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
Also used on the DNM and NWM mask pages.

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
annealing.
Also used on the high-energy implanter page.
Tier: deep dive.
Also used on the DNM and NWM mask pages.

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
n-well implants in production.
Also used on the high-energy implanter page.
Tier: deep dive.

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
with MeV implants.
Also used on the high-energy implanter page.
Tier: deep dive.

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
Also used on the dopant gases and implant sources material page.

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
Also used on the LVTNM and HVTPM mask pages.

**WEI-1998** — L. Wei, Z. Chen, M. Johnson, K. Roy and V. De, *"Design
and optimization of low voltage high performance dual threshold CMOS
circuits"*, Proceedings of the 35th Design Automation Conference,
pp. 489–494, 1998, DOI 10.1109/DAC.1998.724521. The circuit-level case
for a second threshold voltage. Tier: deep dive.
Also used on the HVTPM mask page.

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
monitor.
Also used on the medium-current implanter page.
Also used on the sheet-resistance and dose metrology page.
Tier: deep dive.

**CURRENT-1996** — M. I. Current, *"Ion implantation for silicon device
manufacturing: A vacuum perspective"*, Journal of Vacuum Science &
Technology A, vol. 14, no. 3, pp. 1115–1123, 1996,
DOI 10.1116/1.580279. Production-implanter overview: sources, beam
lines, end stations and vacuum.
Also used on the medium-current, high-current and high-energy implanter
pages.
Tier: deep dive.
Also used on the dopant gases and implant sources material page.

**MACK-2007** — C. Mack, *Fundamental Principles of Optical
Lithography: The Science of Microfabrication*, Wiley, 2007,
ISBN 978-0-470-01893-4, DOI 10.1002/9780470723876. k₁, resist profiles,
thick-resist imaging.
Also used on the i-line stepper or scanner and coat/develop track pages.
Tier: deep dive.
Also used on the lithography materials material page.
Also used on the FOM, DNM, LVTNM, HVTPM, P1M, LICM1, LI1M, CTM1, MM1,
VIM, MM2 and VIM4 mask pages.

**LEVINSON-2005** — H. J. Levinson, *Principles of Lithography*, 2nd
ed., SPIE Press, 2005, ISBN 978-0-8194-5660-1, DOI 10.1117/3.601520.
Overlay budgets and non-critical-layer tool choice.
Also used on the i-line stepper or scanner page.
Tier: deep dive.
Also used on the FOM, DNM, LVTNM, NWM, HVTPM, P1M, LICM1, LI1M, CTM1,
MM1, VIM, MM2 and VIM4 mask pages.

**ROCHE-1985** — D. Roche, J. F. Michaud and M. Bruel, *"Outgassing of
Photoresist During Ion Implantation"*, MRS Proceedings, vol. 45, 1985,
DOI 10.1557/PROC-45-203. Resist outgassing during implantation. Tier:
deep dive.

**LEE-1996** — W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland,
M. Dennon and C. Kozak, *"Thick photoresist outgassing during MeV
implantation (mechanism and impact on production)"*, Proceedings of
the 11th International Conference on Ion Implantation Technology
(1996), pp. 186–189, DOI 10.1109/IIT.1996.586180. Outgassing of thick
resists during MeV implantation.
Also used on the high-energy implanter page, and on the downstream
plasma asher page.
Tier: deep dive.
Also used on the DNM, NWM, PWBM and PWDEM mask pages.

**HORSKY-1998** — T. N. Horsky, *"Photoresist outgassing in high energy
and high current ion implantation"*, 1998 International Conference on
Ion Implantation Technology, vol. 1, pp. 654–657,
DOI 10.1109/IIT.1999.812201. Resist outgassing in high-energy and
high-current implanters.
Also used on the medium-current, high-current and high-energy implanter
pages, and on the downstream plasma asher page.
Tier: deep dive.

**FUJIMURA-1989** — S. Fujimura, J. Konno, K. Hikazutani and H. Yano,
*"Ashing of Ion-Implanted Resist Layer"*, Japanese Journal of Applied
Physics, vol. 28, no. 10R, p. 2130, 1989, DOI 10.1143/JJAP.28.2130. The
crust and popping mechanism of implanted resist, measured.
Also used on the downstream plasma asher and wet bench and spray
processor pages.
Tier: deep
dive.

**FUJIMURA-1990** — S. Fujimura, K. Shinagawa, M. Nakamura and
H. Yano, *"Additive Nitrogen Effects on Oxygen Plasma Downstream
Ashing"*, Japanese Journal of Applied Physics, vol. 29, no. 10R,
p. 2165, 1990, DOI 10.1143/JJAP.29.2165. Why nitrogen is added to
oxygen in downstream ashing.
Also used on the downstream plasma asher page.
Tier: deep dive.

**FUJIMURA-1994** — S. Fujimura, M. T. Suzuki, K. Shinagawa and
M. Nakamura, *"Sodium contamination free ashing process using O₂+H₂O
plasma downstream"*, Journal of Vacuum Science & Technology B, vol. 12,
no. 4, pp. 2409–2413, 1994, DOI 10.1116/1.587773. Water-vapour
addition to downstream ashing.
Also used on the downstream plasma asher page.
Tier: deep dive.
Also used on the process gases material page.

**OHMI-1996** — T. Ohmi, *"Total Room Temperature Wet Cleaning for Si
Substrate Surface"*, Journal of The Electrochemical Society, vol. 143,
no. 9, pp. 2957–2964, 1996, DOI 10.1149/1.1837133. A room-temperature
alternative to the hot RCA sequence.
Also used on the wet bench and spray processor page.
Tier: deep dive.
Also used on the wet chemicals material page.
Also used on the ultrapure water material page.

**KERN-1990** — W. Kern, *"The Evolution of Silicon Wafer Cleaning
Technology"*, Journal of The Electrochemical Society, vol. 137, no. 6,
pp. 1887–1892, 1990, DOI 10.1149/1.2086825. History and chemistry of
the RCA clean.
Also used on the downstream plasma asher and wet bench and spray
processor pages.
Also used on the starting-material machine page.
Tier: deep dive.
Also used on the wet chemicals material page.
Also used on the ultrapure water material page.

**KERN-HANDBOOK** — W. Kern, *"Overview and Evolution of Silicon Wafer
Cleaning Technology"*, ch. 1 in K. A. Reinhardt and W. Kern (eds.),
*Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8,
DOI 10.1016/b978-081551554-8.50004-5. Overview chapter on wet-cleaning
chemistry and contamination.
Also used on the wet bench and spray processor page.
Also used on the single-wafer spin processor machine page.
Tier: deep dive.
Also used on the wet chemicals material page.

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
Also used on the PWDEM mask page.

**MAI-2011** — A. Mai and H. Rücker, *"Drain-extended MOS transistors
capable for operation at 10 V and at radio frequencies"*, Solid-State
Electronics, vol. 65–66, pp. 45–50, 2011,
DOI 10.1016/j.sse.2011.06.034. 10 V drain-extended devices in a
0.13 µm technology. Tier: deep dive.

**APPELS-1979** — J. A. Appels and H. M. J. Vaes, *"High voltage thin
layer devices (RESURF devices)"*, 1979 International Electron Devices
Meeting, pp. 238–241, DOI 10.1109/IEDM.1979.189589. The original RESURF
paper. Tier: deep dive.
Also used on the PWDEM mask page.

**LUDIKHUIZE-2000** — A. W. Ludikhuize, *"A review of RESURF
technology"*, 12th International Symposium on Power Semiconductor
Devices & ICs (2000), pp. 11–18, DOI 10.1109/ISPSD.2000.856763. Review
of RESURF design rules for drift regions. Tier: deep dive.
Also used on the PWDEM mask page.

**BALIGA-2008** — B. J. Baliga, *Fundamentals of Power Semiconductor
Devices*, Springer, 2008, ISBN 978-0-387-47313-0,
DOI 10.1007/978-0-387-47314-7. Breakdown, drift-region doping and
on-resistance trade-offs. Tier: deep dive.
Also used on the PWDEM mask page.

**EFLAND-1998** — T. R. Efland, C.-Y. Tsai and S. Pendharkar, *"Lateral
thinking about power devices (LDMOS)"*, IEDM 1998 Technical Digest,
pp. 679–682, DOI 10.1109/IEDM.1998.746447. LDMOS integration into logic
CMOS. Tier: deep dive.
Also used on the PWDEM mask page.

**STOLK-1997** — P. A. Stolk, H.-J. Gossmann, D. J. Eaglesham,
D. C. Jacobson, C. S. Rafferty, G. H. Gilmer, M. Jaraíz, J. M. Poate,
H. S. Luftman and T. E. Haynes, *"Physical mechanisms of transient
enhanced dopant diffusion in ion-implanted silicon"*, Journal of
Applied Physics, vol. 81, no. 9, pp. 6031–6050, 1997,
DOI 10.1063/1.364452. The physical mechanisms of transient enhanced
diffusion.
Also used on the vertical-furnace anneal page and the rapid thermal
processor page.
Tier: deep dive.

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
emphasis on temperature control.
Also used on the rapid thermal processor page.
Tier: deep dive.

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
Also used on the CMP consumables material page.

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
Also used on the substrates material page.

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
<https://doi.org/10.1063/1.326355> Per its abstract, describes how far
gas–surface reactions giving volatile products can be enhanced by
energetic radiation ("primarily ions and electrons"), examines
experimentally "the reactions of Si, SiO2, and Si3N4 with XeF2, F2, and
Cl2", and discusses possible mechanisms and implications for plasma
etching and lithography. Used on steps 005, 036 and 042 and the etch
category page. Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

**COOK-1990** — L. M. Cook, "Chemical processes in glass polishing",
*Journal of Non-Crystalline Solids* **120**(1–3), 152–171 (1990).
<https://doi.org/10.1016/0022-3093(90)90200-6> The chemical mechanism of
glass (oxide) polishing that oxide CMP inherits. Used on step 012 and
the cmp category page. Tier: deep dive.
Also used on the CMP consumables material page.

**DEAL-1965** — B. E. Deal and A. S. Grove, "General Relationship for
the Thermal Oxidation of Silicon", *Journal of Applied Physics*
**36**(12), 3770–3778 (1965). <https://doi.org/10.1063/1.1713945> The
planar oxidation model that the corner results are measured against.
Used on steps 002, 010, 040, 042, 043 and 047 and the oxidation category
page.
Also used on the vertical-furnace oxidation page.
Tier: deep dive.
Also used on the process gases material page.

**DEAL-1980** — B. E. Deal, "Standardized terminology for oxide charges
associated with thermally oxidized silicon", *IEEE Transactions on
Electron Devices* **27**(3), 606–608 (1980), DOI
10.1109/T-ED.1980.19908; published simultaneously in *Journal of The
Electrochemical Society* **127**(4), 979–981 (1980).
<https://doi.org/10.1109/T-ED.1980.19908>,
<https://doi.org/10.1149/1.2129800> The standard terminology for oxide
charges (fixed, trapped, mobile, interface) used when qualifying any
thermal oxide. Used on steps 002, 043 and 047 and the anneal and
oxidation category pages.
Also used on the vertical-furnace anneal page.
Tier: deep dive.
Also used on the anneal ambients material page.

**DECKERT-1978** — C. A. Deckert, "Etching of CVD Si₃N₄ in Acidic
Fluoride Media", *Journal of The Electrochemical Society* **125**(2),
320–323 (1978). <https://doi.org/10.1149/1.2131436> Etching of CVD Si₃N₄
in acidic fluoride media, the older data on the same chemistry. Used on
step 013.
Also used on the wet bench and spray processor page.
Tier: deep dive.

**EDMARK-1985** — K. W. Edmark and C. P. Ausschnitt, "Stepper Overlay
Calibration Using Alignment To A Latent Image", *Proc. SPIE* **0538**,
Optical Microlithography IV, 91 (1985).
<https://doi.org/10.1117/12.947752> Stepper overlay calibration by
aligning to a latent image, an early treatment of stepper
self-calibration relevant to an unaligned first layer. Used on step 004.
Tier: deep dive.
Also used on the FOM mask page.

**FALSTER-2000** — R. Falster and V. V. Voronkov, "The engineering of
intrinsic point defects in silicon wafers and crystals", *Materials
Science and Engineering: B* **73**(1–3), 87–94 (2000).
<https://doi.org/10.1016/S0921-5107(99)00439-0> Engineering of intrinsic
point defects in crystals and wafers, the basis of "perfect silicon" and
controlled precipitation. Used on step 001 and the substrate category
page. Tier: deep dive.
Also used on the substrates material page.

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
Also used on the etch and chamber-clean gases material page.

**FUJIMURA-1991** — S. Fujimura, K. Shinagawa, M. T. Suzuki and M.
Nakamura, "Resist stripping in an O₂+H₂O plasma downstream", *Journal of
Vacuum Science & Technology B* **9**(2), 357–361 (1991).
<https://doi.org/10.1116/1.585575> Resist stripping in an O₂ + H₂O
downstream plasma, a low-damage alternative. Used on step 009. Tier:
deep dive.
Also used on the anneal ambients material page.

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
Also used on the CMP consumables material page.

**HU-1991** — S. M. Hu, "Stress-related problems in silicon technology",
*Journal of Applied Physics* **70**(6), R53–R80 (1991).
<https://doi.org/10.1063/1.349282> A review of stress-related problems
in silicon technology, including nitride-on-pad-oxide stress and
dislocation generation. Used on steps 002, 003 and 010.
Also used on the film thickness and stress metrology page.
Tier: deep dive.

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
Also used on the lithography materials material page.
Also used on the VIM4 mask page.

**KAHNG-2008** — A. B. Kahng and K. Samadi, "CMP Fill Synthesis: A
Survey of Recent Studies", *IEEE Transactions on Computer-Aided Design
of Integrated Circuits and Systems* **27**(1), 3–19 (2008).
<https://doi.org/10.1109/TCAD.2007.907061> A survey of dummy-fill
synthesis for CMP, the design-side view of the FOM "waffles". Used on
step 004. Tier: deep dive.
Also used on the FOM, MM1 and MM2 mask pages.

**KANG-1989** — J. S. Kang and D. K. Schroder, "Gettering in silicon",
*Journal of Applied Physics* **65**(8), 2974–2985 (1989).
<https://doi.org/10.1063/1.342714> Gettering experiments: per the
abstract, oxidation and oxynitridation "do not getter metallic
impurities such as Au, Cu, Fe, and Ni while phosphorus (P) diffusion
does"; P diffusion, Ar ion implantation and Ni-film gettering show an
optimum gettering temperature; and a model based on impurity segregation
is proposed. The abstract does not discuss oxygen-precipitate
(intrinsic) gettering. Used on step 001 and the substrate category
page. Tier: deep dive.
Also used on the substrates material page.

**KASTENMEIER-1999** — B. E. E. Kastenmeier, P. J. Matsuo and G. S.
Oehrlein, "Highly selective etching of silicon nitride over silicon and
silicon dioxide", *Journal of Vacuum Science & Technology A* **17**(6),
3179–3184 (1999). <https://doi.org/10.1116/1.582097> How to etch silicon
nitride selectively over silicon and silicon dioxide in fluorine-based
plasmas. Used on step 005.
Also used on the dielectric and nitride plasma etcher page.
Tier: deep dive.

**KNOTTER-2001** — D. M. Knotter and T. J. J. Denteneer, "Etching
Mechanism of Silicon Nitride in HF-Based Solutions", *Journal of The
Electrochemical Society* **148**(3), F43 (2001).
<https://doi.org/10.1149/1.1348262> The etching mechanism of silicon
nitride in HF-based solutions, relevant to the pre-strip breakthrough
dip. Used on step 013.
Also used on the wet bench and spray processor page.
Also used on the single-wafer spin processor machine page.
Tier: deep dive.
Also used on the wet chemicals material page.

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
wet-bench vendor SKW-01 names. Used on step 013.
Also used on the wet bench and spray processor page.
Tier: deep dive.
Also used on the wet chemicals material page.

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
on steps 002, 040, 043 and 047 and the oxidation category page.
Also used on the vertical-furnace oxidation page.
Tier: deep dive.

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
Also used on the HDP-CVD page.
Also used on the precursors material page.

**OCONNOR-1996** — J. P. O'Connor and N. Tokoro, "End station and beam
line design considerations for photoresist outgassing with high energy
(MeV) ion implantation", *Proc. 11th International Conference on Ion
Implantation Technology (1996)*, pp. 350–354.
<https://doi.org/10.1109/IIT.1996.586285> End-station and beam-line
design to cope with resist outgassing at MeV energies. Used on step 007,
and on the high-energy implanter page.
Tier: deep dive.

**OEHRLEIN-1994** — G. S. Oehrlein, Y. Zhang, D. Vender and M. Haverlag,
"Fluorocarbon high-density plasmas. I. Fluorocarbon film deposition and
etching using CF₄ and CHF₃", *Journal of Vacuum Science & Technology A*
**12**(2), 323–332 (1994). <https://doi.org/10.1116/1.578876>
Fluorocarbon high-density plasmas with CF₄ and CHF₃: polymer deposition
versus etching, the mechanism behind sidewall passivation. Used on step
005 and the etch category page.
Also used on the dielectric and nitride plasma etcher page.
Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

**OHASHI-2007** — T. Ohashi, T. Kubota and A. Nakajima, "Ar Annealing
for Suppression of Gate Oxide Thinning at Shallow Trench Isolation
Edge", *IEEE Electron Device Letters* **28**(7), 562–564 (2007).
<https://doi.org/10.1109/LED.2007.899328> An argon anneal that
suppresses gate-oxide thinning at the STI edge, a later view of the same
problem. Used on step 010.
Also used on the vertical-furnace anneal page.
Tier: deep dive.
Also used on the anneal ambients material page.

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
Also used on the FOM, P1M and LI1M mask pages.

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
data. Used on steps 005 and 042.
Also used on the dielectric and nitride plasma etcher page.
Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

**ROENIGK-1987** — K. F. Roenigk and K. F. Jensen, "Low Pressure CVD of
Silicon Nitride", *Journal of The Electrochemical Society* **134**(7),
1777–1785 (1987). <https://doi.org/10.1149/1.2100756> A reactor model of
LPCVD nitride from DCS/NH₃, explaining thickness uniformity along a
hot-wall tube. Used on step 003.
Also used on the vertical-furnace LPCVD page.
Tier: deep dive.
Also used on the precursors material page.

**RYUTA-1990** — J. Ryuta, E. Morita, T. Tanaka and Y. Shimanuki,
"Crystal-Originated Singularities on Si Wafer Surface after SC1
Cleaning", *Japanese Journal of Applied Physics* **29**(11A), L1947
(1990). <https://doi.org/10.1143/JJAP.29.L1947> The paper that
identified "crystal-originated singularities" (COPs) revealed by SC-1
cleaning, the defect class that gate-oxide yield depends on. Used on
step 001 and the substrate category page. Tier: deep dive.
Also used on the starting-material machine page.
Also used on the substrates material page.

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
rules. Used on step 012 and the cmp category page.
Also used on the CMP polisher machine page.
Also used on the cross-section SEM and profilers page.
Tier: deep dive.
Also used on the FOM, MM1 and MM2 mask pages.

**STONEY-1909** — G. G. Stoney, "The tension of metallic films deposited
by electrolysis", *Proceedings of the Royal Society of London A*
**82**(553), 172–175 (1909). <https://doi.org/10.1098/rspa.1909.0021>
The wafer-curvature relation used to turn a bow measurement into a film
stress. Used on step 003.
Also used on the film thickness and stress metrology page.
Tier: deep dive.

**TEASDALE-2001** — D. Teasdale, Y. Senzaki, R. Herring, G. Hoeye, L.
Page and P. Schubert, "LPCVD of Silicon Nitride from Dichlorosilane and
Ammonia by Single Wafer Rapid Thermal Processing", *Electrochemical and
Solid-State Letters* **4**(5), F11 (2001).
<https://doi.org/10.1149/1.1359056> Single-wafer RTCVD of DCS/NH₃
nitride, the alternative to a batch furnace. Used on step 003.
Also used on the vertical-furnace LPCVD page and the rapid thermal
processor page.
Tier: deep dive.

**TEMPLE-BOYER-1998** — P. Temple-Boyer, C. Rossi, E. Saint-Etienne and
E. Scheid, "Residual stress in low pressure chemical vapor deposition
SiNₓ films deposited from silane and ammonia", *Journal of Vacuum
Science & Technology A* **16**(4), 2003–2007 (1998).
<https://doi.org/10.1116/1.581302> Residual stress in LPCVD SiNₓ as a
function of composition, the reason stoichiometric films are highly
tensile. Used on step 003.
Also used on the vertical-furnace LPCVD page.
Tier: deep dive.

**VAN-HAREN-2019** — R. J. F. van Haren, S. Steinert, O. Mouraille, K.
D'havé, L. van Dijk, J. Hermans and D. Beyer, "Wafer alignment mark
placement accuracy impact on the layer-to-layer overlay performance",
*Proc. SPIE* **11148**, Photomask Technology 2019, 37 (2019).
<https://doi.org/10.1117/12.2536270> How alignment-mark placement
accuracy limits layer-to-layer overlay. Used on steps 004 and 041. Tier:
deep dive.
Also used on the FOM mask page.

**VASSILIEV-1999** — V. Y. Vassiliev, "Properties and Gap-Fill
Capability of HPD-CVD Phosphosilicate Glass Films for
Subquarter-Micrometer ULSI Device Technology", *Electrochemical and
Solid-State Letters* **3**(2), 80 (1999).
<https://doi.org/10.1149/1.1390964> Properties and gap-fill capability
of HDP-CVD phosphosilicate glass, the doped variant SkyWater also lists.
Used on step 011. Tier: deep dive.
Also used on the HDP-CVD page.

**VISINTIN-2006** — P. M. Visintin, M. B. Korzenski and T. H. Baum,
"Liquid Clean Formulations for Stripping High-Dose Ion-Implanted
Photoresist from Microelectronic Devices", *Journal of The
Electrochemical Society* **153**(7), G591 (2006).
<https://doi.org/10.1149/1.2195884> Liquid formulations for stripping
high-dose implanted resist when ashing alone is insufficient. Used on
step 009. Tier: deep dive.
Also used on the wet chemicals material page.

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
012.
Also used on the cross-section SEM and profilers page.
Tier: deep dive.

**ZIEGLER-2010** — J. F. Ziegler, M. D. Ziegler and J. P. Biersack,
"SRIM – The stopping and range of ions in matter (2010)", *Nuclear
Instruments and Methods in Physics Research B* **268**(11–12), 1818–1823
(2010). <https://doi.org/10.1016/j.nimb.2010.02.091> SRIM, the tool used
to compute the ion range in resist that sets the mask thickness. Used on
step 007 and the implant category page. Tier: deep dive.
Also used on the DNM, LVTNM, NWM, HVTPM, PWBM and PWDEM mask pages.

**ZULEHNER-1983** — W. Zulehner, "Czochralski growth of silicon",
*Journal of Crystal Growth* **65**(1–3), 189–213 (1983).
<https://doi.org/10.1016/0022-0248(83)90051-9> A wafer-maker's review of
Czochralski silicon growth: pulling, oxygen and carbon incorporation,
dopant segregation. Used on step 001 and the substrate category page.
Tier: deep dive.
Also used on the substrates material page.

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
Used on step 005 and the deposition and etch category pages.
Also used on the silicon and polysilicon plasma etcher and dielectric
and nitride plasma etcher pages.
Also used on the PECVD page.
Tier: deep
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
Also used on the CMP polisher machine page.
Also used on the CMP consumables material page.

**REINHARDT-2008** — K. A. Reinhardt and W. Kern (eds.), *Handbook of
Silicon Wafer Cleaning Technology*, 2nd ed., William Andrew, 2008, ISBN
978-0-8155-1554-8. <https://openlibrary.org/isbn/9780815515548> The
reference volume on wet and dry cleaning, resist removal and particle
control. Label ↔ key: the handbook whose first chapter is listed
separately as KERN-HANDBOOK. Used on steps 009 and 013.
Also used on the wet bench and spray processor page.
Also used on the single-wafer spin processor machine page.
Tier: deep dive.
Also used on the wet chemicals material page.

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
Also used on the starting-material machine page.
Also used on the substrates material page.

**SMITH-1983** — T. C. Smith, "Wafer Cooling and Photoresist Masking
Problems in Ion Implantation", in *Ion Implantation: Equipment and
Techniques*, Springer Series in Electrophysics, Springer, 1983, pp.
196–213. <https://doi.org/10.1007/978-3-642-69156-0_25> Wafer cooling
and photoresist masking problems (flow, crust, popping) in implantation.
Used on steps 007 and 009, and on the high-current implanter page. Tier:
deep dive.

**STEIGERWALD-1997** — J. M. Steigerwald, S. P. Murarka and R. J.
Gutmann, *Chemical Mechanical Planarization of Microelectronic
Materials*, Wiley, 1997, ISBN 978-0-471-13827-6.
<https://doi.org/10.1002/9783527617746> The standard CMP textbook:
Preston's law, pads, slurries and process control. Used on step 012 and
the cmp category page. Tier: deep dive.
Also used on the CMP polisher machine page.
Also used on the CMP consumables material page.

**SUN-2017** — T. Sun, Z. Han and M. Keswani, "Brush Scrubbing for
Post-CMP Cleaning", in *Developments in Surface Contamination and
Cleaning, Volume 9*, Elsevier, 2017, pp. 109–133.
<https://doi.org/10.1016/B978-0-323-43157-6.00004-5> Brush scrubbing for
post-CMP cleaning. Used on step 012. Tier: deep dive.
Also used on the post-CMP cleaner machine page.

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
Also used on the CMP polisher machine page.

**PAT-CMP-WINDOW** — M. Birang, A. Gleason and W. L. Guthrie (Applied
Materials), *Forming a transparent window in a polishing pad for a
chemical mechanical polishing apparatus*, US 5,893,796 A, granted
1999-04-13. <https://patents.google.com/patent/US5893796A/en> A
transparent window in the pad for in-situ optical endpoint detection.
Used on step 012. Tier: deep dive.
Also used on the CMP polisher machine page.
Also used on the CMP consumables material page.

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
Also used on the HDP-CVD page.

**PAT-HDP-NOVELLUS** — G. D. Papasouliotis, A. B. Chakravarti, R. A.
Conti, L. Economikos and P. A. Van Cleemput (Novellus Systems /
International Business Machines), *High throughput chemical vapor
deposition process capable of filling high aspect ratio structures*, US
6,030,881 A, granted 2000-02-29.
<https://patents.google.com/patent/US6030881A/en> A high-throughput
HDP-CVD process for filling high-aspect-ratio structures. Used on step
011. Tier: deep dive.
Also used on the HDP-CVD page.

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
Used on step 005 and the etch category page.
Also used on the silicon and polysilicon plasma etcher and metal plasma
etcher pages.
Tier: deep dive.

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
Also used on the starting-material machine page.
Also used on the substrates material page.

**SEMI-P1** — SEMI, *SEMI P1 — Specification for Hard Surface Photomask
Substrates*, SEMI Standards store listing (revision P1-0708E, inactive),
accessed 2026-09-13.
<https://store-us.semi.org/products/p00100-semi-p1-specification-for-hard-surface-photomask-substrates>
The specification for hard-surface photomask substrates. Used on step
004 and the lithography category page. Tier: deep dive.
Also used on the lithography materials material page.

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
on step 013.
Also used on the wet bench and spray processor page.
Tier: deep dive.

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
materials, integration, reliability. Used on step 047.
Also used on the plasma nitridation chamber page.
Tier: deep dive.

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
oxidation category page.
Also used on the vertical-furnace oxidation page and the plasma
nitridation chamber page.
Tier: deep dive.
Also used on the process gases material page.

**HATTANGADY-1995** — S. V. Hattangady, H. Niimi and G. Lucovsky,
"Controlled nitrogen incorporation at the gate oxide surface", *Applied
Physics Letters* **66**(25), 3495–3497 (1995).
<https://doi.org/10.1063/1.113775> Controlled nitrogen incorporation at
the gate-oxide surface. Used on step 047.
Also used on the plasma nitridation chamber page.
Tier: deep dive.

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
047 and the oxidation category page.
Also used on the rapid thermal processor and plasma nitridation chamber
pages.
Tier: deep dive.

**HWANG-1991** — H. Hwang, W. Ting, D.-L. Kwong and J. Lee, "A physical
model for boron penetration through an oxynitride gate dielectric
prepared by rapid thermal processing in N₂O", *Applied Physics Letters*
**59**(13), 1581–1582 (1991). <https://doi.org/10.1063/1.106290> A
physical model of boron penetration through N₂O oxynitride. Used on step
047.
Also used on the rapid thermal processor and plasma nitridation chamber
pages.
Tier: deep dive.
Also used on the process gases material page.

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
in ammonia. Used on step 047.
Also used on the rapid thermal processor and plasma nitridation chamber
pages.
Tier: deep dive.

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
reaction of extremely dilute HF. Used on steps 039 and 046.
Also used on the wet bench and spray processor page.
Also used on the single-wafer spin processor machine page.
Tier: deep
dive.
Also used on the wet chemicals material page.

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
of SiO₂ with a high-density nitrogen plasma. Used on step 047.
Also used on the plasma nitridation chamber page.
Tier: deep dive.

**KUEHNE-1997** — J. Kuehne, S. Hattangady, J. Piccirillo, G. C. Xing,
G. E. Miner and D. Lopes, "Nitric Oxide Rapid Thermal Nitridation of
Thin Gate Oxides", *MRS Proceedings* **470**, 381 (1997).
<https://doi.org/10.1557/PROC-470-381> Nitric oxide rapid thermal
nitridation of thin gate oxides. Used on step 047. Tier: deep dive.
Also used on the process gases material page.

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
gate dielectrics. Used on steps 043 and 047.
Also used on the rapid thermal processor page.
Tier: deep dive.

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
047.
Also used on the vertical-furnace oxidation page.
Tier: deep dive.

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
Also used on the etch and chamber-clean gases material page.

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
on step 036.
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep dive.

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
047 and the oxidation category page.
Also used on the vertical-furnace oxidation page and the rapid thermal
processor page.
Tier: deep dive.
Also used on the process gases material page.

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
on steps 036 and 042 and the etch category page.
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

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
Also used on the substrates material page.

##### Standards and roadmaps

**SEMI-M62** — SEMI M62, *Specification for Silicon Epitaxial Wafers*,
SEMI.
<https://store-us.semi.org/products/m06200-semi-m62-specification-for-silicon-epitaxial-wafers>
The specification for epitaxial wafers. Used on the substrate category
page. Tier: cross-check.
Also used on the substrates material page.

**SEMI-M8** — SEMI M8, *Specification for Polished Monocrystalline
Silicon Test Wafers*, SEMI.
<https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
The looser specification for polished test wafers. Used on the substrate
category page. Tier: cross-check.
Also used on the starting-material machine page.
Also used on the substrates material page.

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
refractive index on silicon. Used on the oxidation category page.
Also used on the film thickness and stress metrology page.
Tier: deep dive.

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
TEOS and doped glasses. Used on the deposition category page.
Also used on the vertical-furnace LPCVD page.
Tier: deep
dive.

**AMES-1970** — I. Ames, F. M. d'Heurle and R. E. Horstmann, "Reduction
of Electromigration in Aluminum Films by Copper Doping", *IBM Journal of
Research and Development* **14**(4), 461–463 (1970).
<https://doi.org/10.1147/rd.144.0461> The original demonstration that
copper doping suppresses aluminium electromigration. Used on the
deposition category page. Tier: deep dive.
Also used on the sputter targets material page.

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
Also used on the tungsten CVD page.

**KAMINS-1980** — T. I. Kamins, "Structure and Properties of LPCVD
Silicon Films", *Journal of The Electrochemical Society* **127**(3),
686–690 (1980). <https://doi.org/10.1149/1.2129733> Structure and
properties of LPCVD silicon films as a function of deposition
temperature. Used on the deposition category page.
Also used on the vertical-furnace LPCVD page.
Tier: deep dive.
Also used on the precursors material page.

**RAUPP-1992** — G. B. Raupp, T. S. Cale and H. P. W. Hey, "The role of
oxygen excitation and loss in plasma-enhanced deposition of silicon
dioxide from tetraethylorthosilicate", *Journal of Vacuum Science &
Technology B* **10**(1), 37–45 (1992).
<https://doi.org/10.1116/1.586361> Reaction kinetics of PECVD TEOS oxide
and their effect on step coverage. Used on the deposition category page.
Also used on the PECVD page.
Tier: deep dive.

**ROSSNAGEL-1994** — S. M. Rossnagel and J. Hopwood, "Metal ion
deposition from ionized magnetron sputtering discharge", *Journal of
Vacuum Science & Technology B* **12**(1), 449–453 (1994).
<https://doi.org/10.1116/1.587142> The first ionised-magnetron (IMP)
metal deposition experiments. Used on the deposition category page.
Also used on the PVD cluster tool page.
Tier: deep dive.

**ROSSNAGEL-1998** — S. M. Rossnagel, "Directional and ionized physical
vapor deposition for microelectronics applications", *Journal of Vacuum
Science & Technology B* **16**(5), 2585–2608 (1998).
<https://doi.org/10.1116/1.590242> Review of collimated and ionised PVD
for liners and barriers. Used on the deposition category page. Tier:
deep dive.
Also used on the PVD cluster tool page.

**THORNTON-1974** — J. A. Thornton, "Influence of apparatus geometry and
deposition conditions on the structure and topography of thick sputtered
coatings", *Journal of Vacuum Science and Technology* **11**(4), 666–670
(1974). <https://doi.org/10.1116/1.1312732> The structure-zone diagram
for sputtered films versus pressure and temperature. Used on the
deposition category page. Tier: deep dive.
Also used on the PVD cluster tool page.
Also used on the sputter targets material page.

##### Books and book chapters

**OHRING-2002** — M. Ohring, *Materials Science of Thin Films*, 2nd ed.,
Academic Press, 2002.
<https://doi.org/10.1016/B978-0-12-524975-1.X5000-9> Nucleation, growth
regimes, step coverage and the structure-zone model. Used on the
deposition category page. Tier: deep dive.
Also used on the PVD cluster tool page.
Also used on the sputter targets material page.

**SESHAN-2002** — K. Seshan (ed.), *Handbook of Thin-Film Deposition
Processes and Techniques: Principles, Methods, Equipment and
Applications*, 2nd ed., Noyes Publications / William Andrew, 2002, ISBN
978-0-8155-1442-8. <https://openlibrary.org/isbn/9780815514428>
Chapter-per-technique reference on CVD, PECVD, PVD and their equipment.
Used on the deposition category page. Tier: deep dive.
Also used on the PVD cluster tool page.
Also used on the sputter targets material page.

##### Patents

**PAT-IMP-AMAT** — P. Gopalraja, S. Edelstein, A. Tepman, P. Ding, D. Ghosh
and N. Maity (Applied Materials), *Alternate steps of IMP and sputtering
process to improve sidewall coverage*, US 6,350,353 B2, filed 1999-11-24,
granted 2002-02-26.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6350353>
Alternating IMP and conventional sputtering to improve sidewall
coverage. Used on the deposition category page. Tier: cross-check.
Also used on the PVD cluster tool page.

**PAT-TIW-HITACHI** — Hitachi Metals, *Titanium-tungsten target material
for sputtering and manufacturing method therefor*, US 5,160,534 A,
granted 1992-11-03. <https://patents.google.com/patent/US5160534A/en>
The 10 wt.% Ti composition of Ti:W sputter targets. Used on the
deposition category page. Tier: cross-check.
Also used on the PVD cluster tool page, whose footnote adds the inventor
(A. Hiraki) and the filing date (1991-05-31) from Google Patents; the
patent gives the 10 wt% titanium as the composition of the barrier film.
Also used on the sputter targets material page.

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
Also used on the PVD cluster tool page, read from the Wayback Machine
capture of 2026-06-11 because the live page refused the checker's
request on 2026-09-13:
<https://web.archive.org/web/20260611155710/https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html>

**ASM-A400** — ASM International, *ASM International N.V. launches A400
DUO vertical furnace system*, press release, 2019-11-11.
<https://www.asm.com/press-releases/asm-international-nv-launches-a400-duo-vertical-furnace-system-1944469>
Wayback Machine capture of 2024-10-14 (the live page now serves a script
shell without the release text; checked 2026-09-13):
<https://web.archive.org/web/20241014215529/https://www.asm.com/press-releases/asm-international-nv-launches-a400-duo-vertical-furnace-system-1944469>
The A400 furnace's install base and wet-oxidation/anneal use. Used on
the deposition and oxidation category pages.
Also used on the vertical-furnace oxidation, LPCVD and anneal pages.
Tier: cross-check.

**NOVELLUS-HISTORY** — Encyclopedia.com, *Novellus Systems, Inc.*
(company history: Concept One/Two, Sequel, SPEED, Altus).
<https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
The Concept One/Two, Sequel, SPEED and Altus product history. Used on
the deposition category page. Tier: cross-check.
Also used on the PECVD, HDP-CVD and tungsten CVD pages.

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
category page.
Also used on the i-line stepper or scanner and DUV (KrF, 248 nm) stepper
or scanner pages.
Tier: deep dive.

**BRUNNER-1991** — T. A. Brunner, "Optimization of optical properties of
resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
<https://doi.org/10.1117/12.46410> Optimising resist-stack optical
properties: swing curves and anti-reflective layers. Used on the
lithography category page.
Also used on the coat/develop track page.
Tier: deep dive.
Also used on the lithography materials material page.
Also used on the MM1, VIM and MM2 mask pages.

**DAMMEL-1993** — R. R. Dammel, *Diazonaphthoquinone-based Resists*,
SPIE Tutorial Texts TT11, SPIE Press, 1993.
<https://doi.org/10.1117/3.2265072> The SPIE tutorial text on i-line
resist chemistry. Used on the lithography category page.
Also used on the i-line stepper or scanner and coat/develop track pages.
Tier: deep dive.
Also used on the lithography materials material page.

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
lithography category page.
Also used on the DUV (KrF, 248 nm) stepper or scanner and coat/develop
track pages.
Tier: deep dive.
Also used on the lithography materials material page.

**LEVENSON-1982** — M. D. Levenson, N. S. Viswanathan and R. A. Simpson,
"Improving resolution in photolithography with a phase-shifting mask",
*IEEE Transactions on Electron Devices* **29**(12), 1828–1836 (1982).
<https://doi.org/10.1109/T-ED.1982.21037> The original phase-shifting
mask paper. Used on the lithography category page. Tier: deep dive.
Also used on the P1M and LICM1 mask pages.

**LEVINSON-1987** — H. J. Levinson and W. H. Arnold, "Focus: The
critical parameter for submicron lithography", *Journal of Vacuum
Science & Technology B* **5**(1), 293–298 (1987).
<https://doi.org/10.1116/1.583886> Focus as the critical parameter for
submicron lithography, and its budget. Used on the lithography category
page.
Also used on the i-line stepper or scanner page.
Tier: deep dive.

**LIN-1986** — B. J. Lin, "Where Is The Lost Resolution?", *Proc. SPIE*
**633**, 44 (1986). <https://doi.org/10.1117/12.963701> Where the
resolution is lost between the Rayleigh limit and production practice.
Used on the lithography category page. Tier: deep dive.

**LIN-1993** — B. J. Lin, "Phase-shifting masks gain an edge", *IEEE
Circuits and Devices Magazine* **9**(2), 28–35 (1993).
<https://doi.org/10.1109/101.200850> A tutorial on alternating and
attenuated phase-shift masks. Used on the lithography category page.
Also used on the DUV (KrF, 248 nm) stepper or scanner page.
Tier: deep dive.
Also used on the P1M and LICM1 mask pages.

**LIN-2002** — B. J. Lin, "The k₃ coefficient in nonparaxial λ/NA
scaling equations for resolution, depth of focus, and immersion
lithography", *Journal of Micro/Nanolithography, MEMS, and MOEMS*
**1**(1), 7–12 (2002). <https://doi.org/10.1117/1.1445798> The k₁ and k₃
coefficients and the nonparaxial scaling equations for resolution and
depth of focus. Used on the lithography category page.
Also used on the DUV (KrF, 248 nm) stepper or scanner page.
Tier: deep dive.

**MACK-1988** — C. A. Mack, "Understanding Focus Effects In
Submicrometer Optical Lithography", *Optical Engineering* **27**(12)
(1988). <https://doi.org/10.1117/12.7978683> Understanding focus effects
in submicrometre optical lithography. Used on the lithography category
page. Tier: deep dive.

**REICHMANIS-1989** — E. Reichmanis and L. F. Thompson, "Polymer
materials for microlithography", *Chemical Reviews* **89**(6), 1273–1289
(1989). <https://doi.org/10.1021/cr00096a001> Polymer materials for
microlithography, DNQ/novolac included. Used on the lithography category
page. Tier: deep dive.
Also used on the lithography materials material page.

**RIEGER-1994** — M. L. Rieger and J. P. Stirniman, "Using behavior
modeling for proximity correction", *Proc. SPIE* **2197**, 371–376
(1994). <https://doi.org/10.1117/12.175431> Model-based ("behaviour
modelling") proximity correction. Used on the lithography category page.
Tier: deep dive.
Also used on the LI1M mask page.

**STARIKOV-1992** — A. Starikov, "Accuracy of overlay measurements: tool
and mark asymmetry effects", *Optical Engineering* **31**(6), 1298
(1992). <https://doi.org/10.1117/12.56172> Accuracy of overlay
measurements and tool-induced shift. Used on the lithography category
page.
Also used on the CD-SEM and overlay metrology page.
Tier: deep dive.
Also used on the P1M mask page.

**TOLPYGO-2014** — S. K. Tolpygo et al., "Fabrication Process and
Properties of Fully-Planarized Deep-Submicron Nb/Al-AlOx/Nb Josephson
Junctions for VLSI Circuits", arXiv:1408.5829 (2014) — describes a Canon
FPA-3000EX4 248 nm stepper with 5× reduction and NA 0.6.
<https://arxiv.org/abs/1408.5829> A Canon FPA-3000EX4 described in use.
Used on the lithography category page.
Also used on the DUV (KrF, 248 nm) stepper or scanner page.
Tier: cross-check.

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
metrology in one volume. Used on the lithography category page.
Also used on the DUV (KrF, 248 nm) stepper or scanner and CD-SEM and
overlay metrology pages.
Tier: high-level.

##### Patents

**PAT-BIM-TSMC** — S.-J. Lin and W.-C. Wang (Taiwan Semiconductor
Manufacturing Co.), *Method for forming binary intensity masks*, US
6,379,849 B1, filed 2000-10-26, granted 2002-04-30.
<https://patents.google.com/patent/US6379849B1/en>,
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6379849>
A two-step e-beam write for binary masks; its background defines
"Binary intensity masks (binary masks, chrome-on-glass, BIM)", in which
"a layer of opaque material, such as chrome, is deposited on a
transparent substrate material, such as quartz". Used on the mask index
and steps 129, 144 and 159 for the abbreviation for a binary mask. Tier: cross-check.
Also used on the VIM4 mask page.

##### Vendor, regulatory, marketplace and press pages

**ASML-30** — ASML, *Three decades of PAS 5500*, 2021.
<https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
ASML's own account of the PAS 5500 platform's three-decade lifetime.
States that "older systems remain in constant use but migrate to the
lithography of choice for less critical layers" (a general statement,
not about SKY130).
Used on the lithography category page.
Also used on the i-line stepper or scanner page.
Tier: cross-check.

**ASML-750E** — ASML, *ASML introduces KrF lithography scanner* (PAS
5500/750E), press release, 2000-04-04.
<https://www.asml.com/en/news/press-releases/2000/asml-introduces-krf-lithography-scanner-optimized-for>
130 nm resolution at 248 nm, NA 0.7, 120 wafers per hour. Used on the
lithography category page.
Also used on the DUV (KrF, 248 nm) stepper or scanner page.
Tier: cross-check.
Also used on the FOM, P1M, LICM1 and LI1M mask pages.

**ASML-800** — ASML, *ASML introduces new KrF Step & Scan system* (PAS
5500/800), press release, 2001-01-31.
<https://www.asml.com/en/news/press-releases/2001/asml-introduces-new-krf-step-and-scan-system-that-extends>
NA 0.80, 120 nm resolution. Used on the lithography category page.
Also used on the i-line stepper or scanner and DUV (KrF, 248 nm) stepper
or scanner pages.
Tier: cross-check.

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
page.
Also used on the CD-SEM and overlay metrology page.
The address now redirects to
<https://www.gcemarket.com/equipment/kla-tencor-8100-cd-sem-d2c9j>
(checked 2026-09-13).
Tier: cross-check.

**MICROCHEMICALS-DEV** — MicroChemicals, *Development of photoresists*,
application note.
<https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>
TMAH developer strength and practice. Used on the lithography category
page.
Also used on the coat/develop track page.
Tier: cross-check.
Also used on the lithography materials material page.

**NIKON-S204B** — Nikon, *NSR-S204B 248 nm Scanner Exposure System
Overview* (specification summary, reseller copy), attached to the
listing Tara Semiconductor Technology, *Used 2002 NIKON S204 Scanner*
(listing LITV25-01), accessed 2026-09-12.
<https://f.machineryhost.com/fc49306d97602c8ed1be1dfbf0835ead/aa008f2897d7d4a224ff92839b4299e9/SpecSummary_LITV25-01_NSR-S204B.pdf>,
<https://www.tarasemi.com/listings/5223879-used-2002-nikon-s204-scanner>
Field size, NA and wavelength of the NSR-S204B KrF scanner. Used on the
lithography category page.
Also used on the DUV (KrF, 248 nm) stepper or scanner and coat/develop
track pages.
Tier: cross-check.

**TEL-ACT** — Tokyo Electron, *Coater/Developer ACT Series*, product
page. <https://www.tel.com/product/act.html> TEL product page for the
ACT coater/developer family. Used on the lithography category page.
Also used on the coat/develop track page.
Tier: cross-check.

**TEL-ACT8** — Semiconductor Online, *CLEAN TRACK ACT 8 System for
Spin-On Dielectric (SOD) Applications*.
<https://www.semiconductoronline.com/doc/clean-track-act-8-system-for-spin-on-dielectr-0001>
Introduction date and throughput of the CLEAN TRACK ACT 8. Used on the
lithography category page.
Also used on the coat/develop track page.
Tier: cross-check.

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
analysis of HBr/Cl₂/O₂ gate-etch sidewalls under resist and oxide masks;
the passivation layer is "a chlorine rich silicon oxide film". Used on
the etch category page.
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

**COBURN-1979B** — J. W. Coburn and H. F. Winters, "Plasma etching — A
discussion of mechanisms", *Journal of Vacuum Science and Technology*
**16**(2), 391–403 (1979). <https://doi.org/10.1116/1.569958> A
discussion of plasma etching mechanisms. Used on the etch category page.
Tier: deep dive.

**DONNELLY-2013** — V. M. Donnelly and A. Kornblit, "Plasma etching:
Yesterday, today, and tomorrow", *Journal of Vacuum Science & Technology
A* **31**(5), 050825 (2013). <https://doi.org/10.1116/1.4819316> A long
review of plasma etching from its origins to the present. Used on the
etch category page.
Also used on the silicon and polysilicon plasma etcher, dielectric and
nitride plasma etcher and metal plasma etcher pages.
Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

**GOTTSCHO-1992** — R. A. Gottscho, C. W. Jurgensen and D. J. Vitkavage,
"Microscopic uniformity in plasma etching", *Journal of Vacuum Science &
Technology B* **10**(5), 2133–2147 (1992).
<https://doi.org/10.1116/1.586180> Microscopic uniformity:
aspect-ratio-dependent etching and its causes. Used on the etch category
page.
Also used on the silicon and polysilicon plasma etcher and dielectric
and nitride plasma etcher pages.
Tier: deep dive.

**HASHIMOTO-1994** — K. Hashimoto, "Charge Damage Caused by Electron
Shading Effect", *Japanese Journal of Applied Physics* **33**(10R), 6013
(1994). <https://doi.org/10.1143/JJAP.33.6013> Electron-shading charging
damage during high-density plasma etching. Used on the etch category
page.
Also used on the silicon and polysilicon plasma etcher, dielectric and
nitride plasma etcher and metal plasma etcher pages.
Tier: deep dive.

**MOGAB-1977** — C. J. Mogab, "The Loading Effect in Plasma Etching",
*Journal of The Electrochemical Society* **124**(8), 1262–1268 (1977).
<https://doi.org/10.1149/1.2133542> The loading effect. Used on the etch
category page.
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep dive.

**OEHRLEIN-1989** — G. S. Oehrlein, "Dry etching damage of silicon: A
review", *Materials Science and Engineering: B* **4**(1–4), 441–450
(1989). <https://doi.org/10.1016/0921-5107(89)90284-5> Review of
dry-etching damage to silicon. Used on the etch category page.
Also used on the silicon and polysilicon plasma etcher page.
Tier:
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
the etch category page.
Also used on the metal plasma etcher page.
Tier: deep dive.

**STANDAERT-1998** — T. E. F. M. Standaert, M. Schaepkens, N. R. Rueger,
P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "High density
fluorocarbon etching of silicon in an inductively coupled plasma:
Mechanism of etching through a thick steady state fluorocarbon layer",
*Journal of Vacuum Science & Technology A* **16**(1), 239–249 (1998).
<https://doi.org/10.1116/1.580978> Etching through a steady-state
fluorocarbon layer, the mechanism behind oxide-to-silicon selectivity.
Used on the etch category page.
Also used on the dielectric and nitride plasma etcher page.
Tier: deep dive.

**TUDA-2001** — M. Tuda, K. Shintani and H. Ootera, "Profile evolution
during polysilicon gate etching with low-pressure high-density
Cl₂/HBr/O₂ plasma chemistries", *Journal of Vacuum Science & Technology
A* **19**(3), 711–717 (2001). <https://doi.org/10.1116/1.1365135>
Profile evolution during Cl₂/HBr/O₂ high-density poly gate etching. Used
on the etch category page.
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

##### Patents

**PAT-DPS-AMAT** — G. Z. Yin, H. Hanawa, D. X. Ma and D. Olgado (Applied
Materials), *Plasma reactor with multi-section RF coil and isolated
conducting lid*, US 5,540,824 A, granted 1996-07-30.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5540824>
The multi-section RF coil and isolated lid of the DPS reactor. Used on
the etch category page.
Also used on the silicon and polysilicon plasma etcher and metal plasma
etcher pages.
Tier: deep dive.

**PAT-ENDPOINT-TEL** — Tokyo Electron, *Method of forming a
semiconductor device using double endpoint detection*, US 6,376,262 B1,
granted 2002-04-23 (CN emission at 387 nm as the nitride etch endpoint
signal). <https://patents.google.com/patent/US6376262B1/en> CN emission
at 387 nm as the nitride etch endpoint signal. Label ↔ key: the same
patent is cited as `pat-cn-tel` on step 042 (PAT-CN-TEL). Used on the
etch category page.
Also used on the dielectric and nitride plasma etcher page.
Tier: cross-check.

##### Vendor, regulatory, marketplace and press pages

**AKRION-GAMA** — C2MI, *Akrion GAMA acid bench*, equipment page.
<https://www.c2mi.ca/en/equipement/akrion-gama-acid-bench/> Facility
equipment page describing an Akrion GAMA automated acid wet bench, the
bench type SKW-01 lists. Used on the etch and strip category pages.
Also used on the wet bench and spray processor page.
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
the etch category page.
Also used on the dielectric and nitride plasma etcher page.
Tier: cross-check.

#### Strip

##### Papers and review articles

**KERN-1970** — W. Kern and D. A. Puotinen, "Cleaning solutions based on
hydrogen peroxide for use in silicon semiconductor technology", *RCA
Review* **31**, 187–206 (1970). The original SC-1/SC-2 paper. Used on
the strip category page.
Also used on the wet bench and spray processor page.
Tier: cross-check.
Also used on the wet chemicals material page.

##### Patents

**PAT-ASHER-AXCELIS** — A. F. Becknell, P. Hammar and D. Ferris (Axcelis
Technologies), *Apparatus and plasma ashing process for increasing
photoresist removal rate*, US 7,449,416 B2, granted 2008-11-11.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7449416>
An oxygen-free, nitrogen-free ashing chemistry for resist and post-etch
residue removal over low-k dielectrics. Used on the strip category page.
Also used on the downstream plasma asher page.
Tier: deep dive.

**PAT-ASHER-FUSION** — M. Kamarehi and J. E. Simpson (Fusion Systems),
*Plasma asher with microwave trap*, US 5,498,308 A, granted 1996-03-12.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5498308>
A downstream microwave asher design. Used on the strip category page.
Also used on the downstream plasma asher page.
Tier: deep dive.

##### Vendor, regulatory, marketplace and press pages

**GASONICS-AURA** — Allwin21, *Gasonics Aura 1000 Plasma Asher*
(specification summary; temperature 150–300 °C typical).
<https://allwin21.com/gasonics-aura-1000-plasma-asher-2/> Specification
summary for the GaSonics Aura 1000 downstream asher (150–300 °C
typical). Used on the strip category page.
Also used on the downstream plasma asher page.
Tier: cross-check.

**GASONICS-L3510** — SemiStar Corp., *Gasonics L3510 plasma asher* (tool
description; platen temperature 100–300 °C).
<http://www.semistarcorp.com/product/gasonics-l3510-asher/> Tool
description for the GaSonics L3510 asher (platen temperature 100–300
°C). Used on the strip category page.
Also used on the downstream plasma asher page.
Tier: cross-check.

##### University and course pages

**SNF-STRIP** — Stanford Nanofabrication Facility, *Downstream/Remote
Plasma Resist Removal*, equipment guide.
<https://snfguide.stanford.edu/guide/equipment/purpose/cleaning/resist-removal/dry-resist-removal/downstreamremote-plasma-resist-removal>
University equipment guide on downstream/remote-plasma resist removal.
Used on the strip category page.
Also used on the downstream plasma asher page.
Tier: cross-check.

#### Implant

##### Papers and review articles

**CURRENT-2017** — M. I. Current, "Ion implantation of advanced silicon
devices: Past, present and future", *Materials Science in Semiconductor
Processing* **62**, 13–22 (2017).
<https://doi.org/10.1016/j.mssp.2016.10.045> Implantation for advanced
silicon devices, past to future. Used on the implant category page, and
on the medium-current implanter page.
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
category page, and on the medium-current implanter page. Tier: deep
dive.
Also used on the dopant gases and implant sources material page.

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
anneal category page.
Also used on the vertical-furnace anneal page.
Tier: deep dive.
Also used on the anneal ambients material page.

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
category page.
Also used on the vertical-furnace anneal page.
Tier: deep dive.
Also used on the anneal ambients material page.

**SEDGWICK-1983** — T. O. Sedgwick, "Short Time Annealing", *Journal of
The Electrochemical Society* **130**(2), 484–493 (1983).
<https://doi.org/10.1149/1.2119736> An early review of short-time
annealing. Used on the anneal category page.
Also used on the rapid thermal processor page.
Tier: deep dive.

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
and etch category pages.
Also used on the rapid thermal processor page.
Also used on the silicon and polysilicon plasma etcher, dielectric and
nitride plasma etcher and metal plasma etcher pages.
Also used on the PECVD, HDP-CVD, tungsten CVD and PVD cluster tool
pages.
Also used on the CD-SEM and overlay metrology page.
Also used on the CMP polisher machine page.
Tier: cross-check.

**AMAT-RTP** — EDN, *Applied dedicates RTP with Vantage*, 2002-09-23
(Applied Materials Radiance/Vantage RTP chambers).
<https://www.edn.com/applied-dedicates-rtp-with-vantage/> The
Radiance/Vantage RTP chamber family. Used on the anneal and oxidation
category pages. Tier: cross-check.

**ASM-VF** — ASM International, *Vertical furnace*, product page.
<https://www.asm.com/our-technology-products/vertical-furnace> ASM
product page for its vertical furnace family (A400/A412). Used on the
anneal and oxidation category pages.
Also used on the vertical-furnace oxidation and LPCVD pages.
Tier: cross-check.
Also used on the anneal ambients material page.

**PLASMATHERM-AG** — Plasma-Therm, *Product Spotlight: AG Heatpulse 8800
/ 8108 RTP*, blog post.
<https://blog.plasmatherm.com/product-spotlight-ag-heatpulse-8800-8108-rtp>
Vendor blog post on the AG Associates Heatpulse 8800 and 8108 RTP
systems, now supported by Plasma-Therm. Used on the anneal and oxidation
category pages.
Also used on the rapid thermal processor page.
Tier: cross-check.

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
Also used on the CMP consumables material page.

**LUO-2001** — J. Luo and D. A. Dornfeld, "Material removal mechanism in
chemical mechanical polishing: theory and modeling", *IEEE Transactions
on Semiconductor Manufacturing* **14**(2), 112–133 (2001).
<https://doi.org/10.1109/66.920723> The abrasive-contact model of
material removal. Used on the cmp category page. Tier: deep dive.
Also used on the CMP polisher machine page.
Also used on the CMP consumables material page.

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
Also used on the CMP polisher machine page.

**RUNNELS-1994** — S. R. Runnels and L. M. Eyman, "Tribology Analysis of
Chemical-Mechanical Polishing", *Journal of The Electrochemical Society*
**141**(6), 1698–1701 (1994). <https://doi.org/10.1149/1.2054985> A
tribology (fluid-film) analysis of the wafer–pad contact. Used on the
cmp category page. Tier: deep dive.
Also used on the CMP polisher machine page.

**STEIN-1999** — D. Stein, D. L. Hetherington and J. L. Cecchi,
"Investigation of the Kinetics of Tungsten Chemical Mechanical Polishing
in Potassium Iodate-Based Slurries: I. Role of Alumina and Potassium
Iodate", *Journal of The Electrochemical Society* **146**(1), 376–381
(1999). <https://doi.org/10.1149/1.1391617> Kinetics of tungsten CMP:
the roles of alumina abrasive and oxidiser. Used on the cmp category
page. Tier: deep dive.
Also used on the CMP polisher machine page.
Also used on the CMP consumables material page.

**ZANTYE-2004** — P. B. Zantye, A. Kumar and A. K. Sikder, "Chemical
mechanical planarization for microelectronics applications", *Materials
Science and Engineering: R* **45**(3–6), 89–220 (2004).
<https://doi.org/10.1016/j.mser.2004.06.002> A long review of CMP for
microelectronics, including Preston deviations and slurry consumption.
Used on the cmp category page. Tier: deep dive.
Also used on the CMP polisher machine page.
Also used on the CMP consumables material page.

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
Also used on the CMP polisher machine page.

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
The Mirra polisher in its historical context; calls it "the first CMP
system that successfully integrated endpoint detection and integrated
cleaning", although Applied's own release (AMAT-MESA-1999) introduces its
integrated Mesa cleaner, "specifically developed for the Mirra", with the
Mirra Mesa in 1999, and its "Announced in 1997" differs from Applied's
December 1995 (AMAT-1997). Used on the cmp category page. Tier:
cross-check.
Also used on the CMP polisher machine page.
Also used on the CMPP, WCMPLI, CMPL, WCMP2, CMPM, WCMP3, CMPM2, WCMP4,
CMPM3, WCMP5 and CMPM4 step pages.

**EBARA-FREX** — EBARA Precision Machinery Europe, *CMP Tools*
(F-REX200M2). <https://www.ebara-pm.eu/systems/cmp-tools/> The
F-REX200M2 200 mm CMP tool. Used on the cmp category page. Tier:
cross-check.
Also used on the CMP polisher machine page.

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
test category page.
Also used on the parametric tester and prober page.
Tier: deep dive.

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
category page.
Also used on the parametric tester and prober page.
Tier: deep dive.

**PROCTOR-1983** — S. J. Proctor, L. W. Linholm and J. A. Mazer, "Direct
measurements of interfacial contact resistance, end contact resistance,
and interfacial contact layer uniformity", *IEEE Transactions on
Electron Devices* **30**(11), 1535–1542 (1983).
<https://doi.org/10.1109/T-ED.1983.21334> Kelvin measurement of
interfacial contact resistance and its pitfalls. Used on the test
category page.
Also used on the parametric tester and prober page.
Tier: deep dive.

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
the test category page.
Also used on the starting-material machine page.
Also used on the sheet-resistance and dose metrology page.
Tier: deep dive.

**STAPPER-1983** — C. H. Stapper, "Modeling of Integrated Circuit Defect
Sensitivities", *IBM Journal of Research and Development* **27**(6),
549–557 (1983). <https://doi.org/10.1147/rd.276.0549> Defect-sensitivity
and critical-area yield modelling. Used on the test category page.
Also used on the defect and particle inspection page.
Tier: deep dive.

**VALDES-1954** — L. B. Valdes, "Resistivity Measurements on Germanium
for Transistors", *Proceedings of the IRE* **42**(2), 420–427 (1954).
<https://doi.org/10.1109/JRPROC.1954.274680> The original
four-point-probe resistivity measurement. Used on the test category
page.
Also used on the sheet-resistance and dose metrology page.
Tier: deep dive.

**VDP-1958** — L. J. van der Pauw, "A method of measuring specific
resistivity and Hall effect of discs of arbitrary shape", *Philips
Research Reports* **13**, 1–9 (1958); reprinted in S. M. Sze (ed.),
*Semiconductor Devices: Pioneering Papers*, World Scientific, 1991, pp.
174–182. <https://doi.org/10.1142/9789814503464_0017> The theorem behind
the four-contact sheet-resistance structure. Used on the test category
page.
Also used on the sheet-resistance and dose metrology page.
Tier: deep dive.

##### Books and book chapters

**CHENG-1999** — Y. Cheng and C. Hu, *MOSFET Modeling & BSIM3 User's
Guide*, Kluwer Academic, 1999. <https://doi.org/10.1007/b117400> How
parametric data become compact-model parameters. Used on the test
category page.
Also used on the parametric tester and prober page.
Tier: deep dive.

**SCHRODER-2006** — D. K. Schroder, *Semiconductor Material and Device
Characterization*, 3rd ed., Wiley, 2006.
<https://doi.org/10.1002/0471749095> The reference text on resistivity,
contact, C–V and MOSFET measurements. Used on the test category page.
Also used on the sheet-resistance and dose metrology page.
Tier: deep dive.

##### Standards and roadmaps

**ITRS-2001-MET** — International Technology Roadmap for Semiconductors,
*2001 Edition: Metrology*.
<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Met.pdf>
The test-structure and in-line metrology needs. Used on the test
category page.
Also used on the film thickness and stress metrology, sheet-resistance and
dose metrology and cross-section SEM and profilers pages.
Tier: cross-check.

**ITRS-2001-TEST** — International Technology Roadmap for
Semiconductors, *2001 Edition: Test and Test Equipment*.
<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Test.pdf>
Wafer sort and tester requirements. Used on the test category page.
Tier: cross-check.

**ITRS-2001-YIELD** — International Technology Roadmap for
Semiconductors, *2001 Edition: Yield Enhancement*.
<https://www.semiconductors.org/wp-content/uploads/2018/08/2001YieldEnhance.pdf>
The yield-learning loop. Used on the test category page.
Also used on the defect and particle inspection and parametric tester and
prober pages.
Tier: cross-check.
Also used on the ultrapure water material page.

**SEMI-MF84** — SEMI MF84, *Test Method for Measuring Resistivity of
Silicon Wafers With an In-Line Four-Point Probe*, SEMI.
<https://store-us.semi.org/products/mf008400-semi-mf84-test-method-for-measuring-resistivity-of-silicon-wafers-with-an-in-line-four-point-probe>
The standard four-point-probe resistivity test method. Used on the test
category page.
Also used on the sheet-resistance and dose metrology page.
Tier: deep dive.

##### Vendor, regulatory, marketplace and press pages

**BRLTEST-4062** — BRL Test, *4062UX — Keysight / Agilent Parametric
Testers* (listing).
<https://www.brltest.com/index.php?main_page=product_info&products_id=7874>
Used-equipment listing for the HP/Agilent 4062UX parametric tester named
in SKW-01. Used on the test category page.
Also used on the parametric tester and prober page.
Tier: cross-check.

**KEITHLEY-S600** — Keithley Instruments, *Series S600 Parametric Test
Systems*, data sheet.
<https://download.tek.com/datasheet/SeriesS600_DataSht.pdf> Data sheet
giving the S600 tester's intended uses. Used on the test category page.
Also used on the parametric tester and prober page.
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
regime. Used on step 048.
Also used on the vertical-furnace LPCVD page.
Tier: deep dive.

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
margin. Used on step 048.
Also used on the vertical-furnace LPCVD page.
Tier: deep dive.

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
step 063.
Also used on the vertical-furnace oxidation page.
Tier: deep dive.

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
gate. Used on step 048.
Also used on the vertical-furnace LPCVD page.
Tier: deep dive.

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
Also used on the PECVD page.
Also used on the precursors material page.

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
bare poly film. Used on steps 051, 054 and 057.
Also used on the wet bench and spray processor page.
Tier: deep dive.

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
Low-pressure TEOS oxide deposition. Used on step 059.
Also used on the vertical-furnace LPCVD page.
Tier: deep dive.
Also used on the precursors material page.

**BELL-1996** — F. H. Bell and O. Joubert, "Polysilicon gate etching in
high density plasmas. III. X-ray photoelectron spectroscopy
investigation of sidewall passivation of silicon trenches using an oxide
hard mask", *Journal of Vacuum Science & Technology B* **14**(4),
2493–2499 (1996). <https://doi.org/10.1116/1.588758> Sidewall
passivation of silicon etched with an oxide hard mask. Used on steps 059
and 062.
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep dive.
Also used on the hardware consumables material page.

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
HBr/Cl₂/O₂ high-density plasmas. Used on step 062.
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep dive.

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
and the limits of the technology. Used on steps 058 and 062.
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep
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
Also used on the LI1M mask page.

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
Used on step 062.
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep dive.

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
for gate etching. Used on step 062.
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep dive.

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
electron-shading charging during the poly etch. Used on step 062.
Also used on the silicon and polysilicon plasma etcher and metal plasma
etcher pages.
Tier:
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
etch rates in chlorine. Used on step 062.
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep dive.

**ORSHANSKY-2004** — M. Orshansky, L. Milor and C. Hu, "Characterization
of Spatial Intrafield Gate CD Variability, Its Impact on Circuit
Performance, and Spatial Mask-Level Correction", *IEEE Transactions on
Semiconductor Manufacturing* **17**(1), 2–11 (2004).
<https://doi.org/10.1109/TSM.2003.822735> Spatial intrafield gate-CD
variability, its circuit impact and mask-level correction. Used on step
061. Tier: deep dive.
Also used on the P1M mask page.

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
Also used on the PECVD page.

**STURTEVANT-1994** — J. L. Sturtevant, S. J. Holmes, S. E. Knight, D.
Poley, P. A. Rabidoux, L. K. Somerville, T. L. McDevitt and A. Stamper,
"Substrate contamination effects in the processing of chemically
amplified DUV photoresists", *Proc. SPIE* **2197**, Optical/Laser
Microlithography VII, 770–780 (1994).
<https://doi.org/10.1117/12.175469> Substrate contamination effects on
chemically amplified DUV resists, the case for an inert cap under the
resist. Used on step 059. Tier: deep dive.
Also used on the LI1M mask page.

**VALLIER-2003** — L. Vallier, J. Foucher, X. Detter, E. Pargon, O.
Joubert, G. Cunge and T. Lill, "Chemical topography analyses of silicon
gates etched in HBr/Cl₂/O₂ and HBr/Cl₂/O₂/CF₄ high density plasmas",
*Journal of Vacuum Science & Technology B* **21**(2), 904–911 (2003).
<https://doi.org/10.1116/1.1563255> Chemical topography of gates etched
in HBr/Cl₂/O₂ and HBr/Cl₂/O₂/CF₄. Used on step 062.
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep dive.

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
Also used on the single-wafer spin processor machine page.

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
Also used on the single-wafer spin processor machine page.
Also used on the wet chemicals material page.

**SEZ-223-MOOV** — Moov used-equipment marketplace, *Lam Research / SEZ
SP223* listing, accessed 2026-09-12.
<https://moov.co/marketplace/wet-etch/sez-lam-research/lam-research-sez-sp223>
Used-equipment listing for a 200 mm SEZ SP223 spin processor that names
backside film removal among its applications (weak evidence). Used on
step 060. Tier: cross-check.
Also used on the single-wafer spin processor machine page.
Also used on the post-CMP cleaner machine page.

**SEZ-223-PR** — SEZ Group, *SEZ Doubles Wafer Processing Capabilities
With New Dual Chamber Spin-Processing System* (press release,
1999-12-13), reproduced by Surface Finishing / VertMarkets.
<https://www.surfacefinishing.com/doc/sez-doubles-wafer-processing-capabilities-wit-0001>
Press release on the SEZ Spin-Processor 223: dual chambers, throughput,
three chemistries and film-removal applications. Used on step 060. Tier:
cross-check.
Also used on the single-wafer spin processor machine page.

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
073, and on the medium-current implanter page. Tier: deep dive.

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
steps 065 and 067, and on the high-current implanter page. Tier: deep
dive.

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
Used on steps 066, 069 and 073, and on the medium-current implanter
page. Tier: deep dive.

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
angle error. Used on steps 064 and 065, and on the high-current
implanter page. Tier: deep dive.

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
steps 076 and 077.
Also used on the dielectric and nitride plasma etcher page.
Tier: deep dive.

**GUMPHER-2004** — J. Gumpher, W. Bather, N. Mehta and D. Wedel,
"Characterization of Low-Temperature Silicon Nitride LPCVD from
Bis(tertiary-butylamino)silane and Ammonia", *Journal of The
Electrochemical Society* **151**(5), G353 (2004).
<https://doi.org/10.1149/1.1690294> BTBAS low-temperature LPCVD nitride.
Used on steps 076 and 104.
Also used on the vertical-furnace LPCVD page.
Tier: deep dive.
Also used on the precursors material page.

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
poly in high-density plasmas. Used on step 079.
Also used on the silicon and polysilicon plasma etcher page.
Tier: deep dive.

**KASTENMEIER-1996** — B. E. E. Kastenmeier, P. J. Matsuo, J. J. Beulens
and G. S. Oehrlein, "Chemical dry etching of silicon nitride and silicon
dioxide using CF₄/O₂/N₂ gas mixtures", *Journal of Vacuum Science &
Technology A* **14**(5), 2802–2813 (1996).
<https://doi.org/10.1116/1.580203> Nitride and oxide etching in
CF₄/O₂/N₂. Used on steps 077, 079 and 108.
Also used on the dielectric and nitride plasma etcher and downstream
plasma asher pages.
Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

**KRIEGER-1989** — G. Krieger, G. Spadini, P. Cuevas and J. Schuur,
"Shadowing effects due to tilted arsenic source/drain implant", *IEEE
Transactions on Electron Devices* **36**(11), 2458–2461 (1989).
<https://doi.org/10.1109/16.43667> Shadowing of a tilted source/drain
implant by the gate and spacer. Used on steps 077, 082, 083 and 086, and
on the high-current implanter page.
Tier: deep dive.

**LEE-CHEN-1983** — Y. H. Lee and M.-M. Chen, "Silicon etching mechanism
and anisotropy in CF₄+O₂ plasma", *Journal of Applied Physics*
**54**(10), 5966–5973 (1983). <https://doi.org/10.1063/1.331774>
Mechanism and anisotropy in CF₄+O₂ plasmas. Used on steps 077 and 079.
Also used on the dielectric and nitride plasma etcher page.
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
low-temperature LPCVD nitride. Used on step 076.
Also used on the vertical-furnace LPCVD page.
Tier: deep dive.

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
Also used on the LI1M mask page.

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
emissivity in RTP. Used on steps 088 and 092.
Also used on the rapid thermal processor page.
Tier: deep dive.
Also used on the substrates material page.
Also used on the hardware consumables material page.

**CURRENT-1996-IIT** — M. I. Current, M. Vella and W. Lukaszek,
"Beam-plasma concepts for wafer charging control during ion
implantation", *Proc. 11th International Conference on Ion Implantation
Technology* (1996), pp. 53–56. <https://doi.org/10.1109/IIT.1996.586119>
Wafer charging and flood-gun control during high-current implants. Used
on step 082, and on the medium-current implanter page. Tier: deep dive.

**CURRENT-1998** — M. I. Current, M. Foad, S. Brown, W. Lukaszek and M.
Vella, "Photoresist effects on wafer charging control: current-voltage
characteristics measured with Charm-2 monitors during high-current As⁺
implantation", *Proc. 1998 International Conference on Ion Implantation
Technology*, vol. 1, pp. 490–493.
<https://doi.org/10.1109/IIT.1999.812159> Charging control during
high-current arsenic implants. Used on step 086, and on the high-current
implanter page. Tier: deep dive.

**DIXON-1996** — W. Dixon, W. Lukaszek and C. Heden,
"Photoresist-enhanced wafer charging during high current ion
implantation", *Proc. 11th International Conference on Ion Implantation
Technology* (1996), pp. 85–88. <https://doi.org/10.1109/IIT.1996.586134>
Resist-enhanced wafer charging during high-current implants. Used on
steps 081, 082 and 083, and on the high-current implanter page. Tier:
deep dive.

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
spinning-disc batch implanter. Used on steps 082 and 086, and on the
high-current implanter page. Tier: deep
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
control during high-current implants. Used on steps 082 and 086, and on
the high-current implanter page. Tier:
deep dive.

**MEZACK-2000** — G. Mezack, T. Callahan, S. Mehta and U. Jeong,
"Advantages of the Varian VIISta single wafer high current ion implanter
for advanced device fabrication", *Proc. 2000 International Conference
on Ion Implantation Technology*, pp. 431–434.
<https://doi.org/10.1109/IIT.2000.924180> The single-wafer high-current
implanter alternative. Used on steps 082, 083 and 086, and on the
high-current implanter page. Tier: deep dive.

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
and 086, and on the high-current implanter page. Tier: deep dive.

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
098.
Also used on the rapid thermal processor page.
Tier: deep dive.

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
Also used on the PECVD page.
Also used on the precursors material page.

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
The public abstract (retrieved 2026-09-13) notes motor-current friction
sensing for metal polishing, patented acoustic methods and optical
methods with "some success" for STI, and says the paper discusses "many
of the approaches that have been published", categorised as global or
local and direct or indirect. Used on steps 090, 100 and 106. Tier: deep
dive.
Also used on the CMP polisher machine page.

**CHEN-2002-PSG** — S. Chen, C.-Y. Fu, S.-M. Jang, C.-H. Yu and M.-S.
Liang, "Plasma damage reduction for high density plasma CVD
phosphosilicate glass process", *Proc. 7th International Symposium on
Plasma- and Process-Induced Damage* (2002), pp. 76–79.
<https://doi.org/10.1109/PPID.2002.1042613> Plasma damage from an HDP
PSG process and its reduction. Used on step 089. Tier: deep dive.
Also used on the HDP-CVD page.

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
Also used on the PECVD page.
Also used on the precursors material page.

**FUJINO-1991** — K. Fujino, Y. Nishimoto, N. Tokumasu and K. Maeda,
"Doped Silicon Oxide Deposition by Atmospheric Pressure and Low
Temperature Chemical Vapor Deposition Using Tetraethoxysilane and
Ozone", *Journal of The Electrochemical Society* **138**(10), 3019–3024
(1991). <https://doi.org/10.1149/1.2085358> Doped oxide from TEOS and
ozone. Used on step 089. Tier: deep dive.
Also used on the dopant gases and implant sources material page.
Also used on the precursors material page.

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
Also used on the HDP-CVD page.
Also used on the dopant gases and implant sources material page.

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
Also used on the PECVD page.
Also used on the precursors material page.

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
Also used on the CMP polisher machine page.

**NGUYEN-1990** — S. Nguyen, D. Dobuzinsky, D. Harmon, R. Gleason and S.
Fridmann, "Reaction Mechanisms of Plasma- and Thermal-Assisted Chemical
Vapor Deposition of Tetraethylorthosilicate Oxide Films", *Journal of
The Electrochemical Society* **137**(7), 2209–2215 (1990).
<https://doi.org/10.1149/1.2086914> Reaction mechanisms of plasma and
thermal TEOS oxide deposition. Used on steps 091 and 105. Tier: deep
dive.
Also used on the PECVD page.

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
hydrogen-passivated interface defects. Used on step 096.
Also used on the vertical-furnace anneal page.
Tier: deep
dive.
Also used on the anneal ambients material page.

**CHEN-1999-PSM** — Y.-T. Chen, Y.-C. Wang and R. Chu, "Optimization of
attenuated phase-shift mask for contact hole printing", *Proc. SPIE*
**3679**, Optical Microlithography XII, 812 (1999).
<https://doi.org/10.1117/12.354399> Attenuated PSM optimisation for
contact holes. Used on step 093. Tier: deep dive.
Also used on the LICM1, VIM and VIM4 mask pages.

**COBB-1995** — N. B. Cobb and A. Zakhor, "Fast sparse aerial-image
calculation for OPC", *Proc. SPIE* **2621**, 534–545 (1995).
<https://doi.org/10.1117/12.228208> Rules-based, model-based and fast
aerial-image OPC. Used on steps 093 and 102. Tier: deep dive.
Also used on the LI1M mask page.

**DOEMLING-1996** — M. F. Doemling, N. R. Rueger and G. S. Oehrlein,
"Observation of inverse reactive ion etching lag for silicon dioxide
etching in inductively coupled plasmas", *Applied Physics Letters*
**68**(1), 10–12 (1996). <https://doi.org/10.1063/1.116772> Inverse RIE
lag. Used on steps 094 and 108.
Also used on the dielectric and nitride plasma etcher page.
Tier: deep dive.

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
retention. Used on step 096.
Also used on the vertical-furnace anneal page.
Tier: deep dive.
Also used on the anneal ambients material page.

**MORITA-1990** — M. Morita, T. Ohmi, E. Hasegawa, M. Kawakami and M.
Ohwada, "Growth of native oxide on a silicon surface", *Journal of
Applied Physics* **68**(3), 1272–1281 (1990).
<https://doi.org/10.1063/1.347181> Native oxide regrowth on silicon, the
queue-time constraint. Used on steps 095 and 096.
Also used on the vertical-furnace oxidation page.
Tier: deep dive.
Also used on the wet chemicals material page.
Also used on the ultrapure water material page.

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
Also used on the anneal ambients material page.

**RANGAN-1998** — S. Rangan, S. Krishnan and S. Ashok, "Process-induced
damage — a study of hydrogen and deuterium passivation", *Proc. 1998 3rd
International Symposium on Plasma Process-Induced Damage*, pp. 213–216.
<https://doi.org/10.1109/PPID.1998.725612> Hydrogen and deuterium
passivation of process-induced damage. Used on step 096. Tier: deep
dive.
Also used on the anneal ambients material page.

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
step 096.
Also used on the vertical-furnace anneal page.
Tier: deep dive.
Also used on the anneal ambients material page.

**SCHAEPKENS-1999** — M. Schaepkens, T. E. F. M. Standaert, N. R.
Rueger, P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "Study of the
SiO₂-to-Si₃N₄ etch selectivity mechanism in inductively coupled
fluorocarbon plasmas and a comparison with the SiO₂-to-Si mechanism",
*Journal of Vacuum Science & Technology A* **17**(1), 26–37 (1999).
<https://doi.org/10.1116/1.582108> The SiO₂-to-Si₃N₄ selectivity
mechanism. Used on steps 094, 104 and 108.
Also used on the dielectric and nitride plasma etcher page.
Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

**STESMANS-1996** — A. Stesmans, "Passivation of P_b0 and P_b1 interface
defects in thermal (100) Si/SiO₂ with molecular hydrogen", *Applied
Physics Letters* **68**(15), 2076–2078 (1996).
<https://doi.org/10.1063/1.116308> Passivation of P_b0 and P_b1 centres
by molecular hydrogen. Used on step 096.
Also used on the vertical-furnace anneal page.
Tier: deep dive.
Also used on the anneal ambients material page.

**YANG-1998** — C.-H. Yang and C.-M. Dai, "Resist and oxide thickness
effect on process window for 0.2-μm contact patterns with off-axis
illumination and attenuated phase-shift mask", *Proc. SPIE* **3334**,
Optical Microlithography XI, 553 (1998).
<https://doi.org/10.1117/12.310784> Process window of 0.2 µm contacts
with OAI and attenuated PSM. Used on step 093. Tier: deep dive.
Also used on the LICM1 mask page.


#### Ti/TiN liner, contact silicide, tungsten fill and LI tungsten CMP (steps 097–100)

**BERG-2005** — S. Berg and T. Nyberg, "Fundamental understanding and
modeling of reactive sputtering processes", *Thin Solid Films*
**476**(2), 215–230 (2005). <https://doi.org/10.1016/j.tsf.2004.10.051>
Reactive sputtering model and hysteresis. Used on steps 097, 101 and
109. Tier: deep dive.
Also used on the PVD cluster tool page.
Also used on the sputter targets material page.
Also used on the process gases material page.

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
Also used on the PVD cluster tool page.

**KIM-2004** — S.-H. Kim, E.-S. Hwang, S.-Y. Han, S.-H. Pyi, N. Kwak, H.
Sohn, J. Kim and G. B. Choi, "Pulsed CVD of Tungsten Thin Film as a
Nucleation Layer for Tungsten Plug-Fill", *Electrochemical and
Solid-State Letters* **7**(9), G195 (2004).
<https://doi.org/10.1149/1.1784053> Pulsed CVD tungsten nucleation for
plug fill. Used on step 099. Tier: deep dive.
Also used on the tungsten CVD page.

**KLEIJN-1991** — C. R. Kleijn, C. J. Hoogendoorn, A. Hasper, J.
Holleman and J. Middelhoek, "Transport Phenomena in Tungsten LPCVD in a
Single-Wafer Reactor", *Journal of The Electrochemical Society*
**138**(2), 509–517 (1991). <https://doi.org/10.1149/1.2085620>
Transport phenomena in a single-wafer tungsten reactor. Used on step
099. Tier: deep dive.
Also used on the tungsten CVD page.
Also used on the precursors material page.

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
Also used on the tungsten CVD page.
Also used on the precursors material page.

**MCCONICA-1988** — C. M. McConica and K. Cooper, "Tungsten Nucleation
on Thermal Oxide during LPCVD of Tungsten by the Hydrogen Reduction of
Tungsten Hexafluoride", *Journal of The Electrochemical Society*
**135**(4), 1003–1008 (1988). <https://doi.org/10.1149/1.2095756>
Tungsten nucleation on thermal oxide. Used on steps 099 and 110. Tier:
deep dive.
Also used on the tungsten CVD page.

**MORGAN-1985** — A. E. Morgan, E. K. Broadbent and A. H. Reader,
"Formation of Titanium Nitride/Silicide Bilayers by Rapid Thermal Anneal
in Nitrogen", *MRS Proceedings* **52** (1985).
<https://doi.org/10.1557/PROC-52-279> TiN/TiSi₂ bilayers by RTA in
nitrogen. Used on step 098. Tier: deep dive.

**NICOLET-1978** — M.-A. Nicolet, "Diffusion barriers in thin films",
*Thin Solid Films* **52**(3), 415–443 (1978).
<https://doi.org/10.1016/0040-6090(78)90184-0> Diffusion barriers in
microelectronics in general. Used on step 097. Tier: deep dive.
Also used on the sputter targets material page.

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
Also used on the tungsten CVD page.
Also used on the precursors material page.

**PETRI-1998** — R. Petri, H. Hauf, D. Berenbaum, J. C. Favreau and P.
Mazet, "Nitrogen effect on post-nucleation tungsten CVD film growth",
*Proc. IEEE 1998 International Interconnect Technology Conference*, pp.
202–204. <https://doi.org/10.1109/IITC.1998.704792> Nitrogen and
post-nucleation tungsten growth. Used on step 099. Tier: deep dive.
Also used on the tungsten CVD page.

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
Also used on the PVD cluster tool page.
Also used on the sputter targets material page.
Also used on the hardware consumables material page.

**ROSSNAGEL-1993** — S. M. Rossnagel and J. Hopwood, "Magnetron sputter
deposition with high levels of metal ionization", *Applied Physics
Letters* **63**(24), 3285–3287 (1993).
<https://doi.org/10.1063/1.110176> Ionised magnetron sputtering and
metal-ion deposition. Used on steps 097 and 109. Tier: deep dive.
Also used on the PVD cluster tool page.

**RYAN-1995** — J. G. Ryan, S. B. Brodsky, T. Katata, M. Honda, N. Shoda
and H. Aochi, "Collimated Sputtering of Titanium and Titanium Nitride
Films", *MRS Bulletin* **20**(11), 42–45 (1995).
<https://doi.org/10.1557/S0883769400045553> Collimated sputtering of Ti
and TiN. Used on step 097. Tier: deep dive.
Also used on the PVD cluster tool page.

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
mixtures. Used on step 103.
Also used on the metal plasma etcher page.
Tier: deep dive.

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
Used on step 103.
Also used on the metal plasma etcher page.
Tier: deep dive.

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
high-aspect-ratio feature etching. Used on step 108.
Also used on the dielectric and nitride plasma etcher page.
Tier: deep dive.

**FUKUDA-1987** — H. Fukuda, N. Hasegawa, T. Tanaka and T. Hayashida, "A
new method for enhancing focus latitude in optical lithography: FLEX",
*IEEE Electron Device Letters* **8**(4), 179–180 (1987).
<https://doi.org/10.1109/EDL.1987.26594> FLEX, the focus-latitude
enhancement used for contact holes. Used on step 107. Tier: deep dive.
Also used on the CTM1 mask page.

**HAMAGUCHI-1996** — S. Hamaguchi and S. M. Rossnagel, "Liner
conformality in ionized magnetron sputter metal deposition processes",
*Journal of Vacuum Science & Technology B* **14**(4), 2603–2608 (1996).
<https://doi.org/10.1116/1.588993> Liner conformality in ionised
sputtering, modelled. Used on step 109. Tier: deep dive.
Also used on the PVD cluster tool page.

**HEGDE-1997** — R. I. Hegde, P. J. Tobin, S. Sitaram and J. Klein,
"Thin Film Properties of Tungsten Nucleation Layer in Blanket Tungsten
Deposition", *Journal of The Electrochemical Society* **144**(3),
1087–1090 (1997). <https://doi.org/10.1149/1.1837536> Properties of the
nucleation layer in blanket tungsten deposition. Used on step 110. Tier:
deep dive.
Also used on the tungsten CVD page.

**HOPWOOD-1992** — J. Hopwood, "Review of inductively coupled plasmas
for plasma processing", *Plasma Sources Science and Technology*
**1**(2), 109–116 (1992). <https://doi.org/10.1088/0963-0252/1/2/006>
The inductively coupled plasma sources behind IMP. Used on step 109.
Also used on the silicon and polysilicon plasma etcher page.
Also used on the HDP-CVD page.
Tier: deep dive.

**JOLLEY-1998** — M. Jolley, "Applications of Tetramethylammoninium
Hydroxide (TMAH) as a Post Tungsten CMP Cleaning Mixture", *Solid State
Phenomena* **65–66**, 105–108 (1998).
<https://doi.org/10.4028/www.scientific.net/SSP.65-66.105> TMAH as a
post-tungsten-CMP clean. Used on step 111. Tier: deep dive.
Also used on the post-CMP cleaner machine page.
Also used on the CMP consumables material page.

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

**LU-1999** — Z. G. Lu, Y. Cui, A. C. Thomas, S. M. Mansfield et al., "Selection of
attenuated phase shift mask compatible contact hole resists for KrF
optical lithography", *Proc. SPIE* **3678**, Advances in Resist
Technology and Processing XVI, 923 (1999).
<https://doi.org/10.1117/12.350280> Choosing contact-hole resists
compatible with an attenuated PSM at KrF. Used on step 107. Tier: deep
dive.
Also used on steps 118 and 129.
Also used on the LICM1 and CTM1 mask pages.

**MAO-2004** — D. Mao and J. Hopwood, "Ionized physical vapor deposition
of titanium nitride: A deposition model", *Journal of Applied Physics*
**96**(1), 820–828 (2004). <https://doi.org/10.1063/1.1753663> A
deposition model for ionised PVD of titanium nitride. Used on step 109.
Also used on the PVD cluster tool page.
Tier: deep dive.
Also used on the sputter targets material page.

**OEHRLEIN-1994B** — G. S. Oehrlein, Y. Zhang, D. Vender and O. Joubert,
"Fluorocarbon high-density plasmas. II. Silicon dioxide and silicon
etching using CF₄ and CHF₃", *Journal of Vacuum Science & Technology A*
**12**(2), 333–344 (1994). <https://doi.org/10.1116/1.578877> Oxide and
silicon etching in CF₄/CHF₃ high-density plasmas. Used on step 108.
Label ↔ key: the same article is cited as `oehrlein-1994-ii` on step 094
(OEHRLEIN-1994-II).
Also used on the dielectric and nitride plasma etcher page.
Tier: deep dive.

**PAT-CMP-CABOT** — Cabot Corporation, *Composition and slurry useful
for metal CMP*, US 5,958,288 A, filed 1996-11-26, granted 1999-09-28.
<https://patents.google.com/patent/US5958288A/en> A
peroxide/ferric-catalyst tungsten slurry. Used on step 111. Tier:
cross-check.
Also used on the CMP polisher machine page.
Also used on the CMP consumables material page.

**PAT-HCM-NOVELLUS** — K. F. Lai et al. (Novellus Systems), *Apparatus and
method for controlling plasma uniformity across a substrate*, US
6,179,973 B1, filed 1999-06-30, granted 2001-01-30.
<https://patents.google.com/patent/US6179973B1/en> The
hollow-cathode-magnetron ionised PVD source, a competing design. Used on
step 109. Tier: deep dive.
Also used on the PVD cluster tool page.

**PERRY-2001** — W. L. Perry, K. Waters, M. Barela and H. M. Anderson,
"Oxide etch behavior in a high-density, low-pressure, inductively coupled
C₂F₆ plasma: Etch rates, selectivity to photoresist, plasma parameters,
and CFx radical densities", *Journal of Vacuum Science & Technology A*
**19**(5), 2272–2281 (2001). <https://doi.org/10.1116/1.1382874> Oxide
etch rates and selectivity in a high-density C₂F₆ plasma. Used on steps
108, 119, 130 and 145.
Also used on the dielectric and nitride plasma etcher page.
Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

**SHIOYA-1987** — Y. Shioya, T. Ikegami, M. Maeda and K. Yanagida,
"High-temperature stress measurement on chemical-vapor-deposited
tungsten silicide and tungsten films", *Journal of Applied Physics*
**61**(2), 561–566 (1987). <https://doi.org/10.1063/1.338259> Stress of
CVD tungsten films at temperature. Used on step 110. Tier: deep dive.
Also used on the tungsten CVD page.

**SOCHA-2004** — R. Socha, D. Van Den Broeke, S. Hsu, J. F. Chen et al.,
"Contact hole reticle optimization by using interference mapping
lithography (IML)", *Proc. SPIE* **5377**, Optical Microlithography
XVII, 222 (2004). <https://doi.org/10.1117/12.536581> Contact-hole
reticle optimisation with assist features by interference mapping. Used
on step 107. Tier: deep dive.
Also used on the CTM1 mask page.

**STEIN-1998** — D. Stein, D. Hetherington, T. Guilinger and J. L.
Cecchi, "In Situ Electrochemical Investigation of Tungsten
Electrochemical Behavior during Chemical Mechanical Polishing", *Journal
of The Electrochemical Society* **145**(9), 3190–3196 (1998).
<https://doi.org/10.1149/1.1838785> In-situ electrochemistry of tungsten
during CMP. Used on step 111. Tier: deep dive.

**TOYOSHIMA-1998** — T. Toyoshima, T. Ishibashi, A. Minanide, K. Sugino
et al., "0.1 μm level contact hole pattern formation with KrF
lithography by resolution enhancement lithography assisted by chemical
shrink (RELACS)", *IEDM 1998 Technical Digest*, pp. 333–336.
<https://doi.org/10.1109/IEDM.1998.746367> Chemical shrink (RELACS) for
0.1 µm-class holes with KrF. Used on step 107. Tier: deep dive.
Also used on step 118.
Also used on the CTM1 and VIM mask pages.

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
Also used on the dielectric and nitride plasma etcher page.
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
Also used on the LICM1, CTM1 and VIM mask pages.


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
alloys in BCl₃/Cl₂, including the etch rate of "native aluminum oxide
films". Used on step 114.
Also used on the metal plasma etcher page.
Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

**CHENG-2002** — M. Cheng and A. R. Neureuther, "Effects of residual
aberrations on line-end shortening in 193-nm lithography", *Proc. SPIE*
**4691**, Optical Microlithography XV, 1421 (2002).
<https://doi.org/10.1117/12.474526> Line-end shortening from residual
aberrations. Used on step 113. Tier: deep dive.
Also used on the MM1 mask page.

**CHUN-1996** — J.-S. Chun, C.-K. Bok and K.-H. Baik, "Reduction of
substrate dependency of chemically amplified resist", *Proc. SPIE*
**2724**, Advances in Resist Technology and Processing XIII, 92 (1996).
<https://doi.org/10.1117/12.241877> The substrate effect in chemically
amplified resists and its reduction. Used on step 113. Tier: deep dive.

**COOPERBERG-2002** — D. J. Cooperberg, V. Vahedi and R. A. Gottscho,
"Semiempirical profile simulation of aluminum etching in a Cl₂/BCl₃
plasma", *Journal of Vacuum Science & Technology A* **20**(5), 1536–1556
(2002). <https://doi.org/10.1116/1.1494818> Profile simulation of
aluminium etching in Cl₂/BCl₃. Used on step 114.
Also used on the metal plasma etcher page.
Tier: deep dive.

**CYP-PIN145273** — Cypress Semiconductor, *Product Information
Notification PIN145273: Improvement of Cypress Minnesota
Back-End-of-Line Integration for 130nm SONOS Product Families*, document
001-11741 Rev. *H, 2014-03-13 (copy hosted by Tokyo Electron Device).
<https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>
The product-change notification that carries the QTP 123907 report and
describes the TiW-based stack as Cypress's Minnesota process. Used on
steps 112 and 123. Tier: cross-check.
Also used on the PVD cluster tool page.
Also used on the sputter targets material page.

**CYP-QTP-014807** — Cypress Semiconductor, *Technology Derivative
Qualification Report, QTP# 014807 Version 2.0: Technology Derivative
R7FT-3R, Fab4, Synchronous Dual-Port RAM*, June 2005 (copy hosted by
Infineon Technologies).
<https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
R7FT-3R "Hot Al" derivative at Fab 4: 150 Å Ti / 4 200 Å Al / 300 Å TiW.
Used on steps 112 and 117. Tier: cross-check.
Also used on the PECVD page.
Also used on the precursors material page.

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
Also used on the metal plasma etcher page.
Also used on the PVD cluster tool page.
Tier: cross-check.
Also used on the sputter targets material page.

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
Also used on the sputter targets material page.

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
Also used on the HDP-CVD page.
Also used on the precursors material page.

**DEVRIENDT-1998** — K. Devriendt, E. Vrancken, N. Heylen, J. Grillaert,
M. Meuris, M. M. Heyns and Z. C. Lin, "Relation between Oxide-CMP
Induced Defects and Post-CMP Cleaning Strategies", *Solid State
Phenomena* **65–66**, 173–176 (1998).
<https://doi.org/10.4028/www.scientific.net/SSP.65-66.173> Oxide-CMP
defects versus post-CMP cleaning. Used on steps 116 and 117. Tier: deep
dive.
Also used on the post-CMP cleaner machine page.

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
Also used on the anneal ambients material page.

**FISCHL-1987** — D. S. Fischl and D. W. Hess, "Plasma-Enhanced Etching
of Tungsten and Tungsten Silicide in Chlorine-Containing Discharges",
*Journal of The Electrochemical Society* **134**(9), 2265–2269 (1987).
<https://doi.org/10.1149/1.2100868> Chlorine etching of tungsten and
tungsten silicide, relevant to the TiW cap. Used on step 114.
Also used on the metal plasma etcher page.
Tier: deep
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
step 114.
Also used on the metal plasma etcher page.
Tier: deep dive.

**HWANG-1997** — G. S. Hwang and K. P. Giapis, "On the origin of the
notching effect during etching in uniform high density plasmas",
*Journal of Vacuum Science & Technology B* **15**(1), 70–87 (1997).
<https://doi.org/10.1116/1.589258> The origin of notching in
high-density plasma etching. Used on step 114.
Also used on the metal plasma etcher page.
Tier: deep dive.

**HWANG-1998** — G. S. Hwang and K. P. Giapis, "Mechanism of charging
damage during interlevel oxide deposition in high-density plasma tools",
*Proc. 1998 3rd International Symposium on Plasma Process-Induced Damage
(P2ID)*, pp. 164–167. <https://doi.org/10.1109/PPID.1998.725600>
Charging damage during interlevel oxide deposition in high-density
plasma tools. Used on step 115. Tier: deep dive.
Also used on the HDP-CVD page.

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
Also used on the post-CMP cleaner machine page.
Tier: deep dive.
Also used on the CMP consumables material page.

**ROCKE-1988** — M. Rocke and M. Schneegans, "Titanium nitride for
antireflection control and hillock suppression on aluminum silicon
metallization", *Journal of Vacuum Science & Technology B* **6**(4),
1113–1115 (1988). <https://doi.org/10.1116/1.584306> A refractory cap
for anti-reflection and hillock suppression on aluminium. Used on steps
112 and 113. Tier: deep dive.
Also used on the MM1 and MM2 mask pages.

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
114.
Also used on the metal plasma etcher page.
Tier: deep dive.

**SHIRAISHI-1992** — N. Shiraishi, S. Hirukawa, Y. Takeuchi and N.
Magome, "New imaging technique for 64M-DRAM", *Proc. SPIE* **1674**,
Optical/Laser Microlithography V, 741 (1992).
<https://doi.org/10.1117/12.130364> Off-axis illumination for dense
lines. Used on step 113. Tier: deep dive.
Also used on the MM1 and MM2 mask pages.

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
Also used on the metal plasma etcher and wet bench and spray processor
pages.
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
Also used on the tungsten CVD page.

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
Also used on the VIM mask page.

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
Also used on the tungsten CVD page.

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
Also used on the tungsten CVD page.

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
Also used on the VIM and VIM4 mask pages.

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
Also used on the MM2 mask page.

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
Also used on the FOM mask page.

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
alternative to a vertical profile. Used on step 125.
Also used on the metal plasma etcher page.
Tier: deep dive.

**ROCHE-1996** — G. A. Roche and J. P. McVittie, "Application of Plasma
Charging Probe to Production HDP CVD Tool", *Proc. 1st International
Symposium on Plasma Process-Induced Damage (P2ID 1996)*, pp. 71–74.
<https://doi.org/10.1109/PPID.1996.715205> A plasma charging probe
applied to a production HDP-CVD tool. Used on step 126. Tier: deep dive.
Also used on the HDP-CVD page.

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
Also used on the PECVD page.

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
Also used on the PECVD page.

**DANZL-1997** — R. B. Danzl and A. McLaurin, "The use of concentrated
hydrogen peroxide for the removal of a TiW ARC from aluminum bond pads",
*Proc. Twenty-First IEEE/CPMT International Electronics Manufacturing
Technology Symposium (IEMT 1997)*, pp. 99–104.
<https://doi.org/10.1109/IEMT.1997.626884> Peroxide removal of a TiW
cap from aluminium pads, the wet chemistry that etches TiW. Used on
steps 136, 138 and 145.
Also used on the metal plasma etcher page.
Tier: deep dive.

**DENISSE-1986** — C. M. M. Denisse, K. Z. Troost, J. B. Oude Elferink,
F. H. P. M. Habraken, W. F. van der Weg and M. Hendriks,
"Plasma-enhanced growth and composition of silicon oxynitride films",
*Journal of Applied Physics* **60**(7), 2536–2542 (1986).
<https://doi.org/10.1063/1.337117> How the gas mixture sets the
composition of PECVD silicon oxynitride. Used on step 135. Tier: deep
dive.
Also used on the PECVD page.
Also used on the precursors material page.

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
Also used on the PECVD page.

**LIU-2007-TIW** — G. Liu and Y. Kuo, "Reactive Ion Etching of Titanium
Tungsten Thin Films", *Journal of The Electrochemical Society*
**154**(7), H653 (2007). <https://doi.org/10.1149/1.2737631> Reactive
ion etching of TiW in CF₄/O₂, CF₄/Cl₂ and CF₄/HCl. Used on steps 114,
125, 136, 138 and 140.
Also used on the metal plasma etcher page.
Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

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
100 Å of the dielectric. Used on step 138.
Also used on the metal plasma etcher page.
Tier: cross-check.
Also used on the etch and chamber-clean gases material page.

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
Also used on the PECVD page.

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
162 and 163.
Also used on the metal plasma etcher page.
Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

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
Also used on the PVD cluster tool page.

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
Also used on the PVD cluster tool page.

**HARIU-1989** — T. Hariu, K. Watanabe, M. Inoue, T. Takada and H.
Tsuchikawa, "The Properties of Al-Cu/Ti Films Sputter Deposited at
Elevated Temperatures and High DC Bias", *27th International Reliability
Physics Symposium (IRPS 1989)*, pp. 210–214.
<https://doi.org/10.1109/IRPS.1989.363388> The electromigration lifetime
of Al–Cu/Ti films sputtered at 500 °C with substrate bias. Used on step
161. Tier: deep dive.
Also used on the PVD cluster tool page.

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
to reveal probe damage in aluminium bond pads. Used on step 161.
Also used on the parametric tester and prober page.
Tier: deep dive.

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
Also used on the PVD cluster tool page.

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
Also used on the PVD cluster tool page.

**TAYLOR-1998** — D. S. Taylor, M. K. Jain and T. S. Cale, "Deposition
rate dependence of step coverage of sputter deposited aluminum-(1.5%)
copper films", *Journal of Vacuum Science & Technology A* **16**(5),
3123–3126 (1998). <https://doi.org/10.1116/1.581476> Temperature and
rate dependence of Al–Cu step coverage. Used on step 161. Tier: deep
dive.
Also used on the PVD cluster tool page.

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
Also used on the PECVD page.
Also used on the anneal ambients material page.

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
Also used on the PECVD page.

#### Passivation nitride (step 167)

**CHOW-1982** — R. Chow, W. A. Lanford, K.-M. Wang and R. S. Rosler,
"Hydrogen content of a variety of plasma-deposited silicon nitrides",
*Journal of Applied Physics* **53**(8), 5630–5633 (1982).
<https://doi.org/10.1063/1.331445> Hydrogen and etch rate across nine
commercial plasma-nitride reactors. Used on step 167. Tier: deep dive.
Also used on the PECVD page.

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
patterns. Used on step 171.
Also used on the parametric tester and prober page.
Tier: deep dive.

**KIZILYALLI-1998** — I. C. Kizilyalli, G. C. Abeln, Z. Chen, J. Lee,
G. Weber, B. Kotzias, S. Chetlur, J. W. Lyding and K. Hess, "Improvement
of hot carrier reliability with deuterium anneals for manufacturing
multilevel metal/dielectric MOS systems", *IEEE Electron Device Letters*
**19**(11), 444–446 (1998). <https://doi.org/10.1109/55.728907> Deuterium
anneals for manufacturing multilevel metal/dielectric MOS systems. Used
on step 170.
Also used on the vertical-furnace anneal page.
Tier: deep dive.
Also used on the anneal ambients material page.

**LEARN-1976** — A. J. Learn, "Evolution and Current Status of Aluminum
Metallization", *Journal of The Electrochemical Society* **123**(6),
894–906 (1976). <https://doi.org/10.1149/1.2132964> Aluminium
metallisation and its processing. Used on step 170. Tier: deep dive.

**LYDING-1996** — J. W. Lyding, K. Hess and I. C. Kizilyalli, "Reduction
of hot electron degradation in metal oxide semiconductor transistors by
deuterium processing", *Applied Physics Letters* **68**(18), 2526–2528
(1996). <https://doi.org/10.1063/1.116172> Deuterium in the final sinter
and hot-electron degradation. Used on step 170.
Also used on the vertical-furnace anneal page.
Tier: deep dive.
Also used on the anneal ambients material page.

**PAT-DEUTERIUM-UIUC** — J. W. Lyding and K. Hess (Board of Trustees of
the University of Illinois), *Deuterium-treated semiconductor devices*,
US 5,872,387 A, filed 1996-01-16, granted 1999-02-16.
<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5872387>,
<https://patents.google.com/patent/US5872387A/en> (the form the pages
cite). Deuterium-treated devices and example anneal conditions. Used on step
170.
Also used on the vertical-furnace anneal page.
Tier: deep dive.
Also used on the anneal ambients material page.

**SAYAH-1988** — H. R. Sayah and M. G. Buehler, "Comb/serpentine/cross-bridge
test structure for fabrication process evaluation", *Proc. 1988 IEEE
International Conference on Microelectronic Test Structures (ICMTS)*,
pp. 23–28. <https://doi.org/10.1109/ICMTS.1988.672923> A
comb/serpentine/cross-bridge structure for process evaluation. Used on
step 171.
Also used on the parametric tester and prober page.
Tier: deep dive.

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
switching layer; titanium nitride listed both among inert
(oxygen-resistant) electrode materials (col. 5) and as an example of a
reactive one (cols. 6–7), the naming being "relative"; forming
"considered to be a part of the fabrication of ReRAM cell" (col. 9); and
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

### 8.18 SkyWater PDK raw measurement data

Sources introduced for the pages that describe the public test tile and
its measured data: the `google/skywater-pdk-sky130-raw-data`
repository (public, archived; checked at commit `1f7214f`) and the
IC-CAP file-format page its README links to. The repository describes a
test tile placed on Google's MPW runs and data measured on it to help
validate the open PDK; it does not say that the tile's modules are the
production e-test modules of the SKY130 frame, and the pages do not
present them as such. Per-category module counts quoted on the pages
are our own classification of the pad table. Every URL was fetched on
2026-09-13.

**RAW-DATA-README** — SkyWater PDK Authors, *sky130-raw-data - Raw data
collected about the SKY130 process technology*, `README.rst` and
`AUTHORS` of the `skywater-pdk-sky130-raw-data` repository, 2022
(Apache 2.0).
<https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/README.rst>
States that the repository "contains the raw data that has been
collected about SkyWater's 130nm bulk process technology to help
validate" the open PDK, that "The initial data … was collected under
contract by CoolCAD Electronics LLC using the manufacturing test tile
created by SkyWater", and that the data are "stored in the `.mdm` file
format"; separates a "**Current** proprietary SkyWater Test Tile" from a
"**Future** fully open source Test Tile" (Google, NIST and the
University of Michigan). `AUTHORS` lists Google LLC, SkyWater Technology
Foundry and CoolCAD Electronics LLC. Used on step 171, the test category
page and the overview.
Also used on the parametric tester and prober page.
Tier: cross-check.

**RAW-DATA-TESTTILE-PROP** — SkyWater PDK Authors, *SkyWater 130nm
Proprietary Manufacturing Test Tile*,
`docs/sky130-testtile-proprietary/README.rst` and
`sky130-testtile-pad-layout.png`, raw-data repository, 2022.
<https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/README.rst>
"each of the Google MPW runs includes two copies of a 'manufacturing
test tile'", which "consists of a grid of probe points"; "The schematics
and layout of the circuits connected to these probe points are **not**
currently available". The pad-layout photograph labels "Row 1"–"Row 4",
pin numbers 01–12, a "Lithographic Calibration Region" and "Alignment
Marks". No position on the reticle is given. Used on step 171 and the
test category page.
Also used on the parametric tester and prober page.
Tier: cross-check.
Also used on the substrates material page.
Also used on the hardware consumables material page.

**RAW-DATA-TESTTILE-PADS** — SkyWater PDK Authors, *Manufacturing Test
Tile Pad Documentation* (PDF title "Pad documentation for SKY130 MPW
Manufacturing E-Test Tile"), `sky130-testtile-pad-documentation.csv`,
`.ods` and `.pdf`, raw-data repository, "Public Release - Apache 2.0",
2022.
<https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
A table of 273 numbered modules (columns `Mod #`, `Group`, new- and
old-style device names, `Description`, `Pin 01`–`Pin 12`, `Die Row`)
naming the terminal on each pad: transistor families swept in W, L and
source/drain extent; field-oxide FETs; well and deep-N-well isolation
and resistors; diffusion and 300 Ω/sq and 2 kΩ/sq poly resistors with
four-terminal and van der Pauw wiring; licon and mcon contact strings
and Kelvin contacts; via-1 to via-4 chains; comb/serpentine structures
on diffusion, poly, LI and metals 1–5; finger (VPP), charge-based,
varactor, MOS and MiM capacitors with their expected values; diodes;
bipolar transistors; ring oscillators; SRAM, SONOS, 2T-flash and
antifuse structures. One continuation row reads "PLACE IN CENTER,
CORNER OF RETICLE"; several poly-resistor rows name an "RRPM mask" and a
"URPM mask". Used on step 171, the test category page, the overview and
the well, deep-N-well mask, high-Vt mask, isolation, poly-resistor, poly,
SONOS, drain-extended-well, P-well block, depletion-implant,
gate-oxidation, source/drain-implant, contact, via, metal and MiM step
pages.
Also used on the parametric tester and prober page.
Tier: cross-check.
Also used on the FOM, NWM, PWBM and PWDEM mask pages.

**RAW-DATA-TESTTILE-OPEN** — SkyWater PDK Authors, *SkyWater 130nm Open
Manufacturing Test Tile*, `docs/sky130-testtile-open/README.rst` with
`resultanttestdie.png` and `testinterface.png`, raw-data repository,
2022.
<https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-open/README.rst>
An open test tile by Google, NIST and the University of Michigan built
with OpenFASoC and gdsfactory generators (ring oscillators; line and
via-chain resistance; MIM capacitor and diode modules); "The first test
version of this tile was included in the MPW-5 run". The die image
lists "Over 1400 Pads", "400+ Transistor Structures", "30 Capacitor Test
Structures", "24 Ring Oscillators", "18 line and via chain modules" and
"7 Diode Test Structures"; the test-interface figure shows a pad grid
with "40 µm" pads, "60 µm" and "80 µm" dimensions and a photograph of a
needle "Probe Card". Used on step 171 and the test category page. Tier:
cross-check.
Also used on the hardware consumables material page.

**RAW-DATA-MDM** — Agilent Technologies, *IC-CAP User's Guide*, "MDM
File Structure" (IC-CAP 2008 documentation, copy linked from the
raw-data README), with the raw-data repository's annotated figure
`docs/_static/mdm-format.png`.
<https://people.ece.ubc.ca/robertor/Links_files/Files/ICCAP-2008-doc/icug/icug136.html>,
<https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/_static/mdm-format.png>
The MDM format is "ASCII based" and "Table-based"; "The file extension
for the data files is .mdm (measured data management)"; the header's
mandatory `ICCAP_INPUTS` and `ICCAP_OUTPUTS` sections describe the
sweeps and outputs. The raw-data figure annotates a transistor file:
"Aliases given to each source measurement unit", "Source measurement
unit number on the curve tracer", "Compliance", "Linear sweep, constant,
etc.", "Sweep order", "Start value", "Final value", "Number of steps",
"Step size". Used on step 171.
Also used on the parametric tester and prober page.
Tier: cross-check.

**RAW-DATA-NOTEBOOKS** — Google LLC, *SKY130 plots of {IC,IB,IG}/VG*
(`sky130_plot_current.ipynb`), and B. Murmann, *SKY130 plots of ID-VG
derivatives* (`sky130_plot_gm.ipynb`, August 2022), Colab notebooks in
the raw-data repository.
<https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/notebooks>
Load `.mdm` files with DMT-core and plot transistor currents and
derivatives. The second notebook's comments: "the data gets noisy below
2nA" and the data "cannot be used to predict the subthreshold slope
(digital leakage) or peak gm/ID (for low power analog)". Evidence about
the resolution of the published data, not about the process. Used on
step 171. Tier: high-level.

**RAW-DATA-HV-MOSFETS** — SkyWater PDK Authors (measurements by CoolCAD
Electronics LLC), measured data for the 5 V, 10/16 V and 20 V
transistors, the native and zero-Vt NMOS, the ESD NMOS and the
thick-oxide gate capacitors: IC-CAP `.mdm` files in the
`sky130_fd_pr/cells/` directories `nfet_g5v0d10v5`, `pfet_g5v0d10v5`,
`nfet_g5v0d16v0`, `pfet_g5v0d16v0`, `nfet_g5v0d20v0`, `pfet_g5v0d20v0`,
`nfet_03v3_nvt`, `nfet_05v0_nvt`, `nfet_20v0_nvt`, `esd_nfet_01v8` and
`esd_nfet_g5v0d10v5` of the raw-data repository, 2022 (Apache 2.0).
<https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
576 files: 273 I_D–V_G sweeps (V_DS 0.1 V and the highest drain
voltage, three body biases), 273 matching I_D–V_D sweeps (gate in 1 V
steps; 0.36 V or 0.6 V steps on the 1.8 V and 3 V sweeps) and 30 C–V
sweeps between −5 V and +5 V. File names give the drawn
W, L and multiplier and the test-tile module and pad numbers, which
match the rows of RAW-DATA-TESTTILE-PADS. Headers give only the sweeps,
compliance and instrument-channel names — no temperature, date, lot,
wafer, die or measurement frequency. The drain is swept to at most 5 V
(3 V on the 3.3 V native devices, 1.8 V on the 1.8 V ESD devices and on
the module-2624 `nfet_05v0_nvt` structures, 10 V on the symmetric 16 V
structures), so the files do not bear on breakdown or on
the 10.5–20 V ratings. Labelling points that affect readings: the ten
module-7203 files in `nfet_g5v0d16v0` are swept with negative gate and
drain voltages and the pad list calls module 7203 "VHV DE PMOS"; the
`nfet_20v0_nvt` directory holds module 4451, which the pad list calls
`n20zvtvhv1` at W/L 30/5.5 µm, m = 2 — the geometry of the PDK's
`nfet_20v0_zvt` e-test structure, not of `nfet_20v0_nvt` (30/1.0 µm);
one 0.42/0.5 µm `nfet_g5v0d10v5` structure (module 8389, pads 11–12)
carries no current. Every threshold, current, resistance, body-effect
coefficient and capacitance quoted from these files on this site is our
extraction from the published measurements, with the method stated
where it is quoted. Used on steps 001, 026, 030, 038, 043 and 171, the
test category page and the overview. Tier: cross-check.
Also used on the substrates material page.

**RAW-DATA-LV-MOSFETS** — SkyWater PDK Authors (measurements by CoolCAD
Electronics LLC), measured data for the 1.8 V transistors: IC-CAP
`.mdm` files in the `sky130_fd_pr/cells/` directories `nfet_01v8`,
`nfet_01v8_lvt`, `pfet_01v8`, `pfet_01v8_hvt` and `pfet_01v8_lvt` of
the raw-data repository, 2022 (Apache 2.0).
<https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
480 files: 237 I_D–V_G sweeps (gate 0 to ±1.8 V in 50 mV steps at
|V_DS| = 0.1 V and 1.8 V, with 0, 0.9 V and 1.8 V of reverse body
bias except on the 20 array files, which are at zero body bias), 237
matching I_D–V_D sweeps (gate in 0.36 V steps) and 6 gate C–V sweeps
(−1.8 V to 1.8 V) of the low-Vt NMOS (module 5219) and high-Vt PMOS
(modules 5207 and 5219) overlap-capacitance structures. For each of the five
types one module holds the geometries of the PDK's e-test thresholds
and currents (7/8, 7/0.15, 0.42/8 or 0.42/1 and 0.42/0.15 µm; 7/8,
7/0.35, 0.42/8 and 0.42/0.35 µm for `pfet_01v8_lvt`), all except the
0.42/1 µm `nfet_01v8`, and there are NMOS
devices the pad list places "in DNW", series in which only the
source/drain extent (`sa` = `sb`, 2.5 µm down to 0.265 µm) changes, and
multi-finger arrays. File names give the drawn W, L and multiplier and
the test-tile module and pad numbers, which match the rows of
RAW-DATA-TESTTILE-PADS, except that the array files `5290_9`
(`nfet_01v8`) and `5291_9` (`pfet_01v8_hvt`) are named L = 0.15 µm
where the pad list gives "w=0.42; l=0.5; m=1680". Headers give only the
sweeps, compliance and instrument-channel names — no temperature, date,
lot, wafer or die. Points that affect readings: the drain currents per
drawn width of the module-26xx "fet mismatch" structures are about two
to four times those of the same drawn geometries in other modules
(whose currents are close to the e-test nominals), although their
thresholds agree to within about 0.05 V; the linear-region currents of the arrays level off
at a few milliamperes; the sweeps of several `pfet_01v8` structures
(modules 8405 and 8407) and of the 3/1, 7/8 and 7/0.35 µm
`pfet_01v8_lvt` of module 8396 are erratic (for the 7/8 µm device only
below about 0.5 µA), and two module-5290 arrays carry about 0.7 µA at zero
gate voltage and V_DS = 0.1 V (about 4.6 µA at 1.8 V). Every threshold, current and body-effect value quoted
from these files on this site is our extraction from the published
measurements, with the method stated where it is quoted. Used on steps
008, 011, 014, 015, 020, 023, 024, 045, 066 and 171, the test category
page and the overview. Tier: cross-check.

**RAW-DATA-PASSIVES** — SkyWater PDK Authors (measurements by CoolCAD
Electronics LLC), measured data for resistors, capacitors, varactors and
bipolar transistors: IC-CAP `.mdm` files in the
`sky130_fd_pr/cells/unsorted/` directory of the raw-data repository
(subdirectories `res`, `cap_mim`, `cap_var`, `npn`, `pnp`, `diode`,
`isolation` and `unknown`), 2022 (Apache 2.0).
<https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells/unsorted>
307 `.mdm` files (two of them duplicates), beside seven ring-oscillator oscilloscope captures
(CSV with PNG plots; the CSV headers are the only dated files, "18 JUL
2022"). Two-terminal I–V sweeps (to ±1 V or less) of 88 "300 ohm/sq
P+" and 88 "2K ohm/sq P-" poly resistors (drawn widths 0.33–5.73 µm,
0.5–20 squares), of 25-square N⁺, high-voltage N⁺, P⁺ and
high-voltage P⁺ diffusion resistors and a 0.14 µm N⁺ line, of one
N-well, two deep N-well and two isolated P-well resistors of about one
square, of five `xpwres` (`res_iso_pw`) lengths, of well-isolation
structures and of a via-4 chain and a via-4 array; four-terminal sweeps of van der Pauw
structures, narrow poly and P⁺ lines and metal-1/metal-2 lines; C–V sweeps from −3.3 V to +3.3 V of
first-level, second-level and stacked MiM capacitors (nine files) and
from −4 V to +4 V of `cap_var_lvt` and `cap_var_hvt` varactors
(14 files); forward and reverse Gummel and Early sweeps of a
poly-emitter NPN and 0.68 µm lateral PNPs; diode I–V and MOS overlap
C–V sweeps. File names give the structure, drawn geometry, test-tile
module and pad numbers, which match the rows of RAW-DATA-TESTTILE-PADS;
headers give only the sources, sweeps, compliance and instrument-channel
names — no temperature, date, lot, wafer, die or C–V frequency — and
the undocumented suffixes `_D2`/`_D3` do not match the pad list's die
rows. Labelling points that affect readings: the 2.85 µm poly-resistor
pairs the pad list gives four squares in modules 6210 and 6224 (pads
4–6) measure about one square's resistance; the 1.41 µm "L = 13.142,
sq = 4" pairs measure like the other four-square structures; module
4549, whose file is named `large_mim_cap`, is the pad list's "CAP2M
over M4" capacitor and measures like the second-level module 4541; one
sense channel of the module-3379 van der Pauw file stays at about
0.2 mV. Every value quoted from these files on this site is our
extraction from the published measurements, with the method stated
where it is quoted. Used on steps 007, 008, 018, 022, 023, 024, 027,
047, 052, 053, 055, 056, 082, 086, 135, 138, 150, 153 and 171, the test
category page and the overview. Tier: cross-check.

### 8.19 Machine-class page sources

Sources introduced for the machine-class pages under `docs/machines/`
that had no entry above. Each label on those pages is the key below in
lower case and the citation is the one given in the page footnote; the
entries are grouped by the machine page that first cited the source and
name every page that uses it. None of these sources mentions SkyWater,
SKY130 or the Bloomington fab; they describe equipment classes and
models in general. Every URL was fetched on 2026-09-13, and the IEEE and
AIP papers were checked through Crossref (bibliographic data) and
OpenAlex (abstracts) on that date; the annotations of papers rest on
their abstracts. The papers of the thermal-processing pages (ECS, JJAP,
SPIE and others as well) were checked the same way, and their patents
through Google Patents (bibliographic data, abstract and the passages
quoted); pages that no longer serve their content were read from the
Wayback Machine capture named in the entry. An entry's tier records its first use; a page that
cites the source later may list it under a different reading tier.

#### Medium-current implanter (first cited there)

**AXCELIS-HISTORY** — Axcelis Technologies, *Our History* ("45 Years of
Innovation"), company web page, accessed 2026-09-13.
<https://www.axcelis.com/about/our-history/> Year-by-year history of
Nova, Eaton and Axcelis implanters: the NV-10 "Slot Disk" with a
"dosimetry slot in the disk", the NV-GSD of 1990 with a "Gyroscopic end
station" and ">600 units shipped", the NV-6200AV with "tilt angles from
0 to 60 degrees", the 1994 NV-GSD-HE combining "the GSD end station and
the LINAC technology", the "back biased Secondary Electron Flood (SEF)"
of 1996, the NV-8250HT of 2000 and the spin-off as Axcelis in 2000. Used
on the medium-current, high-current and high-energy implanter pages, and
on the implant category page.
Tier: cross-check (vendor statement).

**TANJYO-2011** — M. Tanjyo and M. Naito, "History of Ion Implanter and
Its Future Perspective", *SEI Technical Review* No. 73, October 2011,
pp. 22–30. <https://global-sei.com/technology/tr/bn73/pdf/73-03.pdf>
Nissin Ion Equipment's account of its medium-current EXCEED line: the
four implanter types (HC, MC, HE, UHD), an example CMOS flow with the
energy, dose and implanter type of each implant, the energy filter
magnet, magnetic beam scan and collimator, Faraday arrays, the
filament-type plasma flood gun for 200 mm, graphite shields, IHC
sources and tilt/twist control to ±0.1°. Used on the medium-current,
high-current and high-energy implanter pages. Tier: deep dive (vendor
technical paper).

**GLAVISH-2018** — H. Glavish and M. Farley, "Review of Major
Innovations in Beam Line Design", *2018 22nd International Conference
on Ion Implantation Technology (IIT)*, pp. 9–18.
<https://doi.org/10.1109/IIT.2018.8807986> Review of implanter beam-line
design from 1970: uniformity, species and energy purity, particles,
angle control in medium-current machines and "the transition from high
current and high energy batch implanters to serial implanters". Used on
the medium-current, high-current and high-energy implanter pages. Tier:
deep dive.

**HORSKY-1998-IHC** — T. N. Horsky, "Indirectly heated cathode arc
discharge source for ion implantation of semiconductors", *Review of
Scientific Instruments* **69**(4), 1688–1690 (1998).
<https://doi.org/10.1063/1.1148866> An indirectly heated cathode source
with "several times the lifetime of commercial Bernas sources", cathode
lives "from 70 h … to over 500 h" and doubly charged fractions of 15 %
for phosphorus and 2 % for boron. Distinct from HORSKY-1998 (resist
outgassing). Used on the medium-current and high-energy implanter
pages. Tier: deep dive.
Also used on the dopant gases and implant sources material page.

**PAT-SDS-ATMI** — G. M. Tom and J. V. McManus (Advanced Technology
Materials), *Storage and delivery system for gaseous hydride, halide,
and organometallic group V compounds*, US 5,518,528 A, granted
1996-05-21. <https://patents.google.com/patent/US5518528A/en> The
sorbent-based sub-atmospheric gas source for implanter arsine and
phosphine; its background records dilute (10–15 %) hydride cylinders at
400–1800 psig and species-change times for solid and gas sources. Used
on the medium-current, high-current and high-energy implanter pages.
Tier: cross-check (patent).
Also used on the dopant gases and implant sources material page.

**SWENSON-1996** — D. R. Swenson, D. F. Downey, S. R. Walther, A. Renau,
G. Gammel and M. E. Mack, "Metals-contamination-reduction program for
the Varian EHP-220/500 medium-current ion implanter", *Proc. 11th
International Conference on Ion Implantation Technology* (1996), pp.
139–142. <https://doi.org/10.1109/IIT.1996.586154> "Additional graphite
and Si-coated shields were added to the beamline" to cut Al, Fe and Cr
contamination of arsenic implants. Used on the medium-current and
high-current implanter pages. Tier: deep dive.
Also used on the dopant gases and implant sources material page.

**SWENSON-1996-BERNAS** — D. R. Swenson, A. Renau, S. R. Walther and M.
E. Mack, "Enhanced Bernas ion source for the Varian EHP-500
medium-current ion implanter", *Proc. 11th International Conference on
Ion Implantation Technology* (1996), pp. 283–286.
<https://doi.org/10.1109/IIT.1996.586263> A higher-current arc supply
and reversible source magnet for more multiply charged beam, operating
"at lower arc voltages to reduce sputter erosion of the filament". Used
on the medium-current implanter page. Tier: deep dive.

**HARLAN-1998** — J. M. Harlan and K. Petry, "Overview of the Eaton 8250
medium current implanter", *Proc. 1998 International Conference on Ion
Implantation Technology*, vol. 1, pp. 266–269 (Crossref title spells
"Eaten"). <https://doi.org/10.1109/IIT.1999.812103> The 8250's hybrid
scanning with "a novel electrostatic scan angle correction lens",
parallelism "better than +/-0.2 degrees", an indirectly heated cathode
source, dosimetry "at the plane of the wafer" and an electrostatic
clamp. Used on the medium-current implanter page. Tier: deep dive.

**RATHMELL-1998** — R. D. Rathmell, D. E. Kamenitsa, M. L. King and A. M.
Ray, "Beam parallelism in the 8250 medium current implanter", *Proc.
1998 International Conference on Ion Implantation Technology*, vol. 1,
pp. 392–395. <https://doi.org/10.1109/IIT.1999.812136> How beam-angle
variations as small as ±0.5° change channelled profiles and monitor
readings, and how the 8250's scan lens keeps angles within 0.2°. Used
on the medium-current implanter page. Tier: deep dive.

**CURELLO-1998** — G. Curello and T. McWilliams, "Charge exchange in
Eaton's NV-8250 medium current ion implanter", *Proc. 1998 International
Conference on Ion Implantation Technology*, vol. 1, pp. 543–545.
<https://doi.org/10.1109/IIT.1999.812173> Dose error from charge
exchange measured by raising the chamber pressure of an 8250 from 5E-7
to 7E-5 Torr, for low-dose BF₂⁺ and higher-dose B⁺. Used on the
medium-current implanter page. Tier: deep dive.

**OLSON-1998** — J. C. Olson, A. Renau and J. Buff, "Scanned beam
uniformity control in the VIISta 810 ion implanter", *Proc. 1998
International Conference on Ion Implantation Technology*, vol. 1, pp.
169–172. <https://doi.org/10.1109/IIT.1999.812079> The VIISta 810, "a
200 mm/300 mm serial medium current ion implanter": a 1 kHz
electrostatic scanner, a 45° angle-corrector magnet and mechanical
wafer scan. Used on the medium-current implanter page. Tier: deep dive.

**KUBO-1996** — T. Kubo, T. Hisaeda, T. Miyake, T. Ishigaki, M. Kase, K.
Watanabe and T. Fukuda, "Energy contamination from multiple-charged ion
implantation in conventional implanter", *Proc. 11th International
Conference on Ion Implantation Technology* (1996), pp. 100–103.
<https://doi.org/10.1109/IIT.1996.586141> Low-energy contamination of
P⁺⁺ implants from charge exchange with resist outgassing — 12 % of the
dose at 400 pμA, 5 % at 200 pμA — and its effect on a retrograde n-well
device. Used on the medium-current and high-energy implanter pages.
Tier: deep dive.

**VARIAN-ESERIES-2003** — Varian Semiconductor Equipment Associates,
*Productivity Plus Option / Upgrade, E220 / E500 Series Implanter*,
presentation, July 2003, hosted by the AVS Northern California Chapter
user groups.
<https://nccavs-usergroups.avs.org/wp-content/uploads/JTG2003/WCJTG_07_2003_Varian.pdf>
A vendor upgrade presentation for Varian's "E-series medium current
implanter" install base (E220, E500 and their HP, EHP and EHPi
versions), for "150mm and 200mm electrostatic-clamp" wafers, with
mechanical throughput figures. Used on the medium-current implanter
page. Tier: cross-check (vendor document).

**FABSURPLUS-E500** — Fabsurplus (SDI), *Varian E500 HP Medium Current
Implanter* (used-equipment specification sheet, item 44950), accessed
2026-09-13. <https://www.fabsurplus.com/sdicatalog/download?id=44950> A
dealer sheet for a 1995 E500 HP "Medium Current Implanter" used for
150 mm production: SDS PH₃, AsH₃ and BF₃ bottles and argon in the gas
box, a "Type II Bernas ion source w/ tungsten arc chamber", CTI
cryopumps, Pfeiffer turbopumps and Edwards dry pumps. Used on the
medium-current implanter page. Tier: high-level (dealer listing).
Also used on the dopant gases and implant sources material page.

**PAT-FARADAY-VARIAN** — J. Bisson, Z. Zhao, G. Gammel, D. Alvarado and
C. Walker (Varian Semiconductor Equipment Associates), *Faraday system
for ion implanters*, US 6,723,998 B2, granted 2004-04-20.
<https://patents.google.com/patent/US6723998B2/en> A Faraday cup with an
electrostatic suppression electrode and a magnet assembly; its
background records that "Escape of secondary and tertiary electrons
from the Faraday cup body … causes a measurement error" and the
established negatively biased suppression electrode at the cup
entrance. Used on the medium-current implanter page. Tier: cross-check
(patent).

#### High-current implanter (first cited there)

**AMAT-QUANTUM-1999** — Applied Materials, *Applied Materials Announces
New Quantum System for All High Current Sub-0.18 Micron Ion Implantation
Applications*, press release (Business Wire), 1999-07-12.
<https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-new-quantum-system-all-high-current/>
The Quantum LEAP ("200eV to 80keV"), Quantum 80 ("2keV to 80keV") and
Quantum 120 high-current implanters on a platform that "bridges 150mm,
200mm or 300mm wafers"; "Nearly 100" xR80 and xR LEAP systems in use;
the short beam path that "minimizes beam 'blow up' and energy
contamination". Used on the high-current implanter page. Tier:
cross-check (vendor statement).

**PAT-DISK-NOVA** — G. Ryding (Nova Associates), *Treating workpieces
with beams*, US 4,234,797 A, granted 1980-11-18.
<https://patents.google.com/patent/US4234797A/en> The batch end station
with "a constantly spinning disk the axis of which is translated", a
detector behind the disc sampling the beam "through a moving slot" to
control the translation speed for uniform dose, and an electron shower
that "neutralizes charge on the workpieces". Used on the high-current
implanter page. Tier: cross-check (patent).

**PAT-DOSE-EATON** — H. Chen and F. Sinclair (Eaton Corporation), *Dose
control for use in an ion implanter*, US 5,760,409 A, granted
1998-06-02. <https://patents.google.com/patent/US5760409A/en> Dose
control that corrects the Faraday reading for charge neutralisation and
charge stripping as a function of beam-path pressure, up to MeV
energies; records that "Such Faraday cages do not measure neutral atoms
in the ion beam" and dose tolerances "at the 1% level". Used on the
high-current and high-energy implanter pages. Tier: cross-check
(patent).

**KRAUPNER-2002** — J. Kraupner, A. Kyek, J. Vogl and S. Weiss, "Dose
theory and pressure compensation on Axcelis GSD high current implanter",
*Proc. 14th International Conference on Ion Implantation Technology*
(2002), pp. 260–263. <https://doi.org/10.1109/IIT.2002.1257988>
Dosimetry and pressure compensation on the GSD, where neutralisation by
gas in the beam line or end station "may lead to wrong dose and bad
uniformity". Used on the high-current implanter page. Tier: deep dive.

**XU-1996** — J. Xu and H. S. Lee, "High current implanter dopant
cross-contamination and its control", *Proc. 11th International
Conference on Ion Implantation Technology* (1996), pp. 151–154.
<https://doi.org/10.1109/IIT.1996.586161> Boron cross-contamination in
high-dose arsenic implants on multi-species high-current implanters,
with energetic boron tied to the post-analyser acceleration voltage and
surface boron sputtered from the beam line. Used on the high-current
implanter page. Tier: deep dive.

**LUNDQUIST-1996** — P. Lundquist, B. Pedersen, D. Ackerman and D.
Brown, "The VIISion 80 and VIISion 200: high current ion implantation
systems for greater throughput with excellent performance at low to high
doses", *Proc. 11th International Conference on Ion Implantation
Technology* (1996), pp. 466–469. <https://doi.org/10.1109/IIT.1996.586401>
Varian's 80 keV and 200 keV VIISion high-current systems, which
"autotune and implant high doses with high beam currents" and use a
plasma flood gun against wafer charging. Used on the high-current
implanter page. Tier: deep dive.

**TODOROV-1998** — S. S. Todorov, G. B. Latona, J. J. Cummings and M.
Kase, "Investigation of energy purity of sub-10 keV B⁺ implants on a
Varian VIISion PLUS ion implanter", *Proc. 1998 International Conference
on Ion Implantation Technology*, vol. 1, pp. 650–653.
<https://doi.org/10.1109/IIT.1999.812200> Energy purity of 2 and 5 keV
B⁺ on a VIISion 80 PLUS with a dual Einzel lens, against photoresist
load, dose and "disc tilt angle". Used on the high-current implanter
page. Tier: deep dive.

#### High-energy implanter (first cited there)

**VARIAN-VIISTA3000** — Semiconductor Online, *High Energy Ion
Implantation System* (Varian Semiconductor Equipment product
description of the VIISta 3000), accessed 2026-09-13.
<https://www.semiconductoronline.com/doc/high-energy-ion-implantation-system-0001>
The single-wafer VIISta 3000 with "DC tandem-based high-energy ion
acceleration", energies to "greater than 3.75 MeV", a claim to be "the
only high-energy ion implanter that directly measures and interlocks the
final implant energy", and electrostatic scanning "about 10 times more
often than alternative (magnetic scan) approaches". Used on the
high-energy implanter page. Tier: high-level (vendor description
reproduced by a trade site).

**TOKORO-2000** — N. Tokoro, D. Holbrook and D. Hacker, "Introduction
of the Varian VIISta 3000 single wafer high-energy ion implanter",
*Proc. 2000 International Conference on Ion Implantation Technology*,
pp. 368–371. <https://doi.org/10.1109/IIT.2000.924164> The VIISta 3000
for "200 and 300 mm wafer processes": a Tandetron DC beam line with the
VIISta 810's electrostatic scanning and dose control, beam currents,
uniformity and dose shift from resist outgassing. Used on the
high-energy implanter page. Tier: deep dive.

**TOKORO-1996** — N. Tokoro, T. Sakase, C. M. Bowen, P. E. Maciejowski
and J. P. O'Connor, "The beam performance of the Genus Tandetron 1520 MeV
implanter", *Proc. 11th International Conference on Ion Implantation
Technology* (1996), pp. 443–446.
<https://doi.org/10.1109/IIT.1996.586393> Genus's third-generation MeV
implanter after the G1500 and G1510: beam-line design and boron and
phosphorus beam performance. Used on the high-energy implanter page.
Tier: deep dive.

**SUETSUGU-2000** — N. Suetsugu, H. Kariya, M. Kabasawa and M. Sugitani,
"Energy accuracy and control method of the NV-GSD-HE", *Proc. 2000
International Conference on Ion Implantation Technology*, pp. 448–451.
<https://doi.org/10.1109/IIT.2000.924184> Why the energy of an RF-linac
beam is harder to fix than that of an electrostatic one, and how the
NV-GSD-HE's Hall-probed final energy magnet measures it. Used on the
high-energy implanter page. Tier: deep dive.

**WILSON-1996** — S. Wilson and E. McIntyre, "Introducing the
NV-GSD/VHE very high energy implanter", *Proc. 11th International
Conference on Ion Implantation Technology* (1996), pp. 375–378.
<https://doi.org/10.1109/IIT.1996.586351> The linac-based NV-GSD/VHE:
B⁺ above 1 pmA near 1.7 MeV, B⁺⁺ near 3 MeV and P⁺⁺⁺ near 5 MeV, with
the source, injector and end station of the NV-GSD/HE. Used on the
high-energy implanter page. Tier: deep dive.

**NAMAROFF-2000** — M. Namaroff and J. Merrill, "High energy, high
current performance of the GSD/VHE implanter for the production of high
dose p-type buried layers", *Proc. 2000 International Conference on Ion
Implantation Technology*, pp. 411–414.
<https://doi.org/10.1109/IIT.2000.924175> MeV boron buried layers at
1.3–1.6 MeV and up to 2 × 10¹⁵ cm⁻² on the GSD/VHE, with source life and
uniformity from a production test. Used on the high-energy implanter
page. Tier: deep dive.

**PAT-LINAC-EATON** — H. F. Glavish and A. S. Denholm (Eaton
Corporation), *Accelerator for ion implantation*, US 4,667,111 A,
granted 1987-05-19. <https://patents.google.com/patent/US4667111A/en>
The multi-cell RF ion accelerator for implantation, each cell an
electrode on an RF resonant tank circuit, giving "energies on the order
of 1 mev per charge state". Used on the high-energy implanter page.
Tier: cross-check (patent).

**PAT-LINAC-AXCELIS** — W. F. Divergilio (Axcelis Technologies),
*Integrated resonator and amplifier system*, US 6,653,803 B1, granted
2003-11-25. <https://patents.google.com/patent/US6653803B1/en> Linac
resonator modules for high-energy implanters; its background calls
1.5 MeV "typical for the deep implants", requires 300–700 keV capability
and names the "Eaton GSD/HE and GSD/VHE ion implanters". Used on the
high-energy implanter page. Tier: cross-check (patent).

#### Vertical batch furnace: oxidation (first cited there)

**EXPERTECH-VTR** — Expertech, *VTR7000PLUS Thermal Reactor | Vertical
Diffusion Furnaces*, product page, accessed 2026-09-13.
<https://www.exper-tech.com/products/vertical-thermal-reactor> The
vertical thermal reactor "originated by Silicon Valley Group (SVG)", with
"over 1000 VTR systems currently in production use worldwide", "a unique
dual-boat design", a "ULPA-filtered Class 1 loading area", "a
double-walled process tube to eliminate film particle formation near the
loading door", loads of "150 product, test, and filler wafers" and a
heating element of "600-1200° C (Up to 1250° C for > 4 Hours)". Used on
the vertical-furnace oxidation, LPCVD and anneal pages. Tier:
cross-check (vendor statement).
Also used on the substrates material page.
Also used on the hardware consumables material page.

**PAT-TORCH-DRIMER** — G. Drimer, A. Glaser and D. M. Rowell, *Fast,
safe, pyrogenic external torch assembly*, US 5,257,926 A, filed
1991-12-17, granted 1993-11-02.
<https://patents.google.com/patent/US5257926A/en> An external
hydrogen–oxygen torch that "provides pure steam for semiconductor
processing"; its background describes the "Pyrogenic Internal Torch", the
"+/-0.5° C. temperature stabilization" oxide uniformity requires, and the
parts of earlier external torches. Used on the vertical-furnace oxidation
page. Tier: cross-check (patent).

**PAT-VF-INSULATION-TEL** — T. Shimazu (Tokyo Electron), *Vertical heat
treatment apparatus*, US 5,709,543 A, filed 1996-09-04, granted
1998-01-20. <https://patents.google.com/patent/US5709543A/en> A vertical
furnace whose substrate holder stands on a cap closing "the bottom
opening (furnace throat)" through a heat-insulation structure of "thin
heat insulation plates"; describes the load, nitrogen purge, heat-up and
process sequence. Used on the vertical-furnace oxidation page. Tier: deep
dive (patent).
Also used on the hardware consumables material page.

**PAT-LOADLOCK-KOKUSAI** — M. Shimada (Kokusai Electric), *Semiconductor
fabricating apparatus, method for controlling oxygen concentration within
load-lock chamber and method for generating native oxide*, US 5,735,961
A, filed 1996-05-16, granted 1998-04-07.
<https://patents.google.com/patent/US5735961A/en> A vertical-furnace
load lock purged to "oxygen concentration less than 1 ppm" or held at
"1-100 ppm" to grow a native oxide of "1-2 atomic layers" before loading
into a tube at "approx. 750° C." Used on the vertical-furnace oxidation
page. Tier: cross-check (patent).

**TEL-TELINDY** — Tokyo Electron, *Deposition TELINDY Series*, product
page (including the ALPHA-8SE i), accessed 2026-09-13.
<https://www.tel.com/product/telindy.html> The ALPHA-8SE i, "a vertical
batch thermal processing system for 200mm wafers", "Released in 2018" as
a remodel of the ALPHA-8SE, for "150/200mm wafers in a batch of up to 150"
and "oxidation/annealing, chemical vapor deposition (CVD) of Si (Poly,
a-Si), SiN, and SiO₂ films"; "more than two decades have passed since the
release of ALPHA-8SE". Used on the vertical-furnace oxidation, LPCVD and
anneal pages. Tier: cross-check (vendor statement).

**TEL-ALPHA8SE** — Semiconductor Online, *Thermal Processing Applications
— Alpha-8SE* (Tokyo Electron America product description), undated,
accessed 2026-09-13.
<https://www.semiconductoronline.com/doc/thermal-processing-applications-alpha-8se-0001>
TEL's "Alpha-8 series diffusion and LP-CVD furnaces", with the Alpha-8SE
generation aimed at devices "that require sub-0.18 micron design rules".
Used on the vertical-furnace oxidation, LPCVD and anneal pages. Tier:
high-level (vendor description reproduced by a trade site).

**AVIZA-VERT** — Aviza Technology, *Vertical Processors*, product page,
2005; Wayback Machine capture of 2005-11-08.
<https://web.archive.org/web/20051108133056/http://www.avizatechnology.com/products/vert.htm>
The AVP/RVP, Aviza's "third-generation vertical diffusion furnaces", with
"Dual boat feature, fast temperature ramping and Advanced Temperature
Control (ATC)", described as "smallest footprint systems for 150/200mm
wafer processing"; the 300 mm RVP-300 with "sequential processing for
nitrided oxides or composite oxide-nitride stacks". Used on the
vertical-furnace oxidation, LPCVD and anneal pages. Tier: cross-check
(vendor statement).

**PAT-BOAT-TEL** — T. Osawa (Tokyo Electron), *Boat for heat treatment*,
US 5,820,367 A, filed 1996-09-18, granted 1998-10-13.
<https://patents.google.com/patent/US5820367A/en> A vertical-furnace boat
with annular ring supports so that "a surface defect called a slip
generated when the wafer is heat treated can be eliminated". Used on the
vertical-furnace oxidation page. Tier: deep dive (patent).
Also used on the hardware consumables material page.

**PAT-VF-TRANSFER-TEL** — T. Tanahashi (Tokyo Electron; Tokyo Electron
Tohoku), *Vertical heat treatment apparatus with a circulation gas
passage*, US 5,551,984 A, filed 1994-12-05, granted 1996-09-03.
<https://patents.google.com/patent/US5551984A/en> Filtered gas
circulation in the transfer chamber below a vertical furnace, which, the
patent says, may be "in the form of a load-lock chamber, and the gas
streams are nitrogen gas streams", with PTFE filter material. Used on the vertical-furnace
oxidation page. Tier: deep dive (patent).

**PAT-TORCH-PERSYS** — G. Drimer, L. Mendelovici and N. Borivker (Persys
Technology), *Compact external torch assembly for semiconductor
processing*, US 6,179,609 B1, filed 1999-07-02, granted 2001-01-30.
<https://patents.google.com/patent/US6179609B1/en> A torch used "both to
produce steam and to perform wet or dry dichlorethylene (DCE) oxidation".
Used on the vertical-furnace oxidation page. Tier: deep dive (patent).
Also used on the process gases material page.

**PAT-TORCH-YAMAHA** — T. Yuuki (Yamaha), *Pyrogenic wet thermal
oxidation of semiconductor wafers*, US 5,633,212 A, filed 1994-07-22,
granted 1997-05-27. <https://patents.google.com/patent/US5633212A/en>
Steam from "an external gas burner" fed to the top of the process tube,
with dilute nitrogen admitted until the flame is stable "so as to
suppress the initial oxidation". Used on the vertical-furnace oxidation
page. Tier: deep dive (patent).

**RAZOUK-1979** — R. R. Razouk and B. E. Deal, "Dependence of Interface
State Density on Silicon Thermal Oxidation Process Variables", *Journal
of The Electrochemical Society* **126**(9), 1573–1581 (1979).
<https://doi.org/10.1149/1.2129333> Interface-state density against
oxidation ambient, anneal and cooling ambient, temperature and
orientation; oxides cooled in nitrogen or argon show large densities that
a low-temperature hydrogen anneal reduces. Used on the vertical-furnace
oxidation and anneal pages. Tier: deep dive.
Also used on the anneal ambients material page.

**AVIZA-COMPANY** — Aviza Technology, *Company*, web page, 2005; Wayback
Machine capture of 2005-11-24.
<https://web.archive.org/web/20051124224446/http://www.avizatechnology.com/company/index.htm>
Aviza "Established in October 2003", tracing "its roots back to 1962 to
the establishment of Thermco, an Orange, California-based supplier of
heater element assemblies", with thermal furnace, ALD and APCVD product
lines. Used on the vertical-furnace oxidation page. Tier: cross-check
(vendor statement).

**TETREON-HTR-2004** — Tetreon Technologies (release hosted by Aviza
Technology), *Tetreon Technologies Acquires Thermco Horizontal Furnaces
from Aviza Technology*, Business Wire, 2004-11-08; Wayback Machine
capture of 2005-03-09.
<https://web.archive.org/web/20050309110126/http://www.avizatechnology.com:80/news/pressrel/110804.htm>
Tetreon buys the manufacturing rights, intellectual property and
inventory of the "'Thermco' Horizontal Furnace (HTR) product line",
"originally marketed under the 'Thermco' name and later produced by
Silicon Valley Group and ASML", with "an estimated installed base of over
8,000 processing tubes"; Aviza "had elected to not pursue the HTR as part
of the company's long-term strategy". Replaces the earlier citation of
Aviza's news index, which only listed the headline. Used on the
vertical-furnace oxidation and anneal pages. Tier: cross-check (vendor
statement).

#### Vertical batch furnace: LPCVD (first cited there)

**PAT-NH4CL-TSMC** — L. Lin, T. Fan, S. Chen, V. Lee and Y.-H. Wu (Taiwan
Semiconductor Manufacturing Company), *Cold trap for CVD furnace*, US
2004/0069224 A1, filed 2002-10-11, published 2004-04-15.
<https://patents.google.com/patent/US20040069224A1/en> Dichlorosilane
nitride in a hot-wall vertical furnace at about 750–800 °C and "several
hundred m Torr", and its ammonium chloride by-product "in the form of a
fine powder" that deposits on cold surfaces and "may be syphoned back
into the furnace". Used on the vertical-furnace LPCVD page. Tier:
cross-check (patent).
Also used on the hardware consumables material page.
Also used on the precursors material page.

**PAT-NH4CL-VLSI** — O. L. Caton, C. A. Bellows, C. M. Hebert, Jr. and
S. J. Schaper (VLSI Technology), *Thermal trap for gaseous materials*,
US 5,303,558 A, filed 1992-07-30, granted 1994-04-19.
<https://patents.google.com/patent/US5303558A/en> Ammonium chloride from
a nitride process is gaseous at "typically about 700° C." but "forms a
solid condensate at temperatures below about 125° C." in exhaust pipes
and pumps; a trap with walls at about 140 °C and a water-cooled
collection surface. Used on the vertical-furnace LPCVD page. Tier: deep
dive (patent).
Also used on the hardware consumables material page.
Also used on the precursors material page.

**PAT-LPCVD-SONY** — S. C. Persyn (Sony), *Vertical LPCVD furnace with
reversible manifold collar and method of retrofitting same*, US 5,800,616
A, filed 1997-12-15, granted 1998-09-01.
<https://patents.google.com/patent/US5800616A/en> Describes "the TEL
VCF-615S LP-TEOS furnace": a bell-shaped chamber with an inner sleeve, a
boat on "a boat elevator and boat pedestal", "A multi-zone heating
element", a bottom exhaust port and TEOS injected into the bottom zone.
Used on the vertical-furnace LPCVD page. Tier: cross-check (patent).

**PAT-LPCVD-KOKUSAI** — K. Maeda, S. Kakizaki, T. Taniyama, H. Yanagawa
and K. Suzaki (Kokusai Electric), *Vertical furnace of a semiconductor
manufacturing apparatus and a boat cover thereof*, US 5,902,103 A, filed
1996-12-23, granted 1999-05-11.
<https://patents.google.com/patent/US5902103A/en> The conventional outer
and inner tubes, gas inlet and annular exhaust of a vertical CVD furnace,
and a boat cover that splits the gas into "branched streams" so that the
film "is improved in uniformity and homogeneity". Used on the
vertical-furnace LPCVD page. Tier: deep dive (patent).
Also used on the hardware consumables material page.

**PAT-LPCVD-NEC** — T. Usami (NEC), *Vertical low pressure CVD apparatus
with an adjustable nozzle*, US 5,503,678 A, filed 1994-11-04, granted
1996-04-02. <https://patents.google.com/patent/US5503678A/en> Separate
annular nozzles for "silane gas and an oxidizing gas", spaced so that the
gases mix uniformly "without an early reaction". Used on the
vertical-furnace LPCVD page. Tier: deep dive (patent).

**AVIZA-SATIN-2004** — Aviza Technology, *Aviza Technology Introduces New
Low Temperature Silicon Nitride Process* ("New Satin Process Aimed at
Sub-90nm DRAM and Logic IC Manufacturing"), press release, 2004-11-29;
Wayback Machine capture of 2005-03-09.
<https://web.archive.org/web/20050309110319/http://www.avizatechnology.com/news/pressrel/113004.htm>
An LPCVD nitride "at approximately 500 degrees C" on the RVP-500, set
against dichlorosilane–ammonia nitride "above 630 degrees C" and BTBAS
"at 570 degrees C or above". Used on the vertical-furnace LPCVD page.
Tier: cross-check (vendor statement).

#### Rapid thermal processor (first cited there)

**MATTSON-METRON-2002** — Mattson Technology, Inc. and Metron Technology
N.V., *Mattson Technology Inc. and Metron Technology N.V. Announce the
Sale of Mattson's AG Associates RTP Product Line to Metron*, press
release, 2002-02-27; Wayback Machine capture of 2003-07-13.
<https://web.archive.org/web/20030713065644/http://mattson.com/news/pr020227.html>
Mattson, which "obtained" the AG Associates RTP line "through its
acquisition last year of the semiconductor division of STEAG Electronic
Systems AG", sells the "4000 and 8000 series RTP product line" to Metron
and keeps its "2000 and 3000 series RTP products". Used on the rapid
thermal processor page. Tier: cross-check (vendor statement).

**HEBB-1996** — J. P. Hebb and K. F. Jensen, "The Effect of Multilayer
Patterns on Temperature Uniformity during Rapid Thermal Processing",
*Journal of The Electrochemical Society* **143**(3), 1142–1151 (1996).
<https://doi.org/10.1149/1.1836598> Radiative properties of patterned
wafers coupled to a reactor model; pattern-induced temperature
non-uniformity in shallow-junction anneals and titanium silicidation.
Used on the rapid thermal processor page. Tier: deep dive.

**DEATON-1991** — R. Deaton and H. Z. Massoud, "Effect of thermally
induced stresses on the rapid-thermal oxidation of silicon", *Journal of
Applied Physics* **70**(7), 3588–3592 (1991).
<https://doi.org/10.1063/1.349254> Edge radiative loss in uniformly
irradiated wafers creates a radial gradient and a stress distribution,
largest along the slip directions, that affects rapid thermal oxidation
kinetics. Used on the rapid thermal processor page. Tier: deep dive.

**SCHAPER-1994** — C. D. Schaper, M. M. Moslehi, K. C. Saraswat and T.
Kailath, "Modeling, Identification, and Control of Rapid Thermal
Processing Systems", *Journal of The Electrochemical Society*
**141**(11), 3200–3209 (1994). <https://doi.org/10.1149/1.2059302>
Model-based multivariable control of multizone RTP systems, with ramps at
45 °C/s and "less than ±1°C average nonuniformity during steady state".
Used on the rapid thermal processor page. Tier: deep dive.

**YOO-2002** — W. S. Yoo, T. Fukada, I. Yokoyama, K. Kang and N.
Takahashi, "Thermal Behavior of Large-Diameter Silicon Wafers during
High-Temperature Rapid Thermal Processing in Single Wafer Furnace",
*Japanese Journal of Applied Physics* **41**(7A), 4442–4449 (2002).
<https://doi.org/10.1143/JJAP.41.4442> Deformation and slip of 200 mm and
300 mm wafers in a single-wafer furnace, with slip "frequently observed in
wafers processed above 1050°C" and slip-free results after optimising
wafer handling. Used on the rapid thermal processor page. Tier: deep
dive.

#### Plasma nitridation chamber (first cited there)

**AMAT-DPN-2001** — Light Reading, *Applied Materials Nitridates*
(reproducing Applied Materials' announcement of its DPN chamber),
2001-11-28, accessed 2026-09-13.
<https://www.lightreading.com/business-management/applied-materials-nitridates>
The single-wafer Decoupled Plasma Nitridation chamber, which "incorporates
a high concentration of nitrogen into the surface of an ultra-thin gate
oxide to prevent boron penetration and reduce leakage current" for
"130nm and below device designs", with "over a dozen DPN chambers in use
for production". Used on the plasma nitridation chamber page. Tier:
cross-check (vendor statement reproduced by trade press).

**PAT-PNA-AMAT** — C. S. Olsen (Applied Materials), *Manufacturing method
for two-step post nitridation annealing of plasma nitrided gate
dielectric*, US 7,429,538 B2, filed 2005-06-27, granted 2008-09-30.
<https://patents.google.com/patent/US7429538B2/en> Describes DPN as "a
technology using inductive coupling to generate nitrogen plasma", run at
"about 5-20 mTorr", "200-800 Watt" and "pulse at about 5-15 kHz" in the
"DPN Centura™", followed by a two-step post-nitridation anneal. Used on
the plasma nitridation chamber page. Tier: cross-check (patent).

**PAT-SPA-TEL** — M. Igeta, C. Wajda, D. L. O'Meara, K. Scheer and T.
Eurakawa (Tokyo Electron; International Business Machines), *Method and
system for forming an oxynitride layer*, US 7,501,352 B2, filed
2005-03-30, granted 2009-03-10.
<https://patents.google.com/patent/US7501352B2/en> Nitridation with a
"slot plane antenna (SPA) plasma source" of "low electron temperature
(less than about 1.5 eV) and high plasma density", naming a TRIAS SPA
processing system. Used on the plasma nitridation chamber page. Tier:
deep dive (patent).

**PAT-RPN-TI** — R. Kraft, S. Hattangady and D. T. Grider (Texas
Instruments), *Method of forming thin silicon nitride or silicon
oxynitride gate dielectrics*, US 6,136,654 A, filed 1997-12-04, granted
2000-10-24. <https://patents.google.com/patent/US6136654A/en> Nitridation
of a gate oxide in a high-density plasma (helicon, helical-resonator, ECR
or inductively coupled) at millitorr pressures for seconds; its
background sets out the temperature and control problems of ammonia
nitridation. Used on the plasma nitridation chamber page. Tier:
cross-check (patent).

**NIIMI-2002** — H. Niimi, A. Khandelwal, H. H. Lamb and G. Lucovsky,
"Reaction pathways in remote plasma nitridation of ultrathin SiO₂ films",
*Journal of Applied Physics* **91**(1), 48–55 (2002).
<https://doi.org/10.1063/1.1419208> Remote He/N₂ and N₂ plasma
nitridation of 3 nm oxides at 300 °C: surface nitrogen at 0.1 Torr,
distributed nitrogen at 0.3 Torr, and the plasma species responsible.
Used on the plasma nitridation chamber page. Tier: deep dive.

**HATTANGADY-1998** — S. Hattangady, D. T. Grider, R. Kraft, W.-T.
Shiau, M. A. Douglas, P. Nicollian, M. Rodder, G. A. Brown, A.
Chatterjee, J. C. Hu, S. Aur, H.-L. Tsai, R. A. Chapman, R. H. Eklund,
I.-C. Chen and M. F. Pas, "Remote plasma nitrided oxides for ultrathin
gate dielectric applications", *Proc. SPIE* **3506**, 30 (1998).
<https://doi.org/10.1117/12.323956> Remote-plasma nitrided oxides against
boron penetration and leakage, without the mobility loss of thermal
oxynitrides, and the production advantages of a self-limiting process on a
thicker starting oxide. Used on the plasma nitridation chamber page. Tier:
deep dive.

**KAPILA-1999** — D. Kapila, S. Hattangady, M. Douglas, R. Kraft and M.
Gribelyuk, "Modeling and Optimization of Oxynitride Gate Dielectrics
Formation by Remote Plasma Nitridation of Silicon Dioxide", *Journal of
The Electrochemical Society* **146**(3), 1111–1116 (1999).
<https://doi.org/10.1149/1.1391730> Response-surface and physical models
of the nitrogen profile from remote plasma nitridation, optimised for top
surface nitrogen and minimum nitrogen at the bottom interface. Used on the
plasma nitridation chamber page. Tier: deep dive.

**PAT-DPN-RF-AMAT** — P. A. Kraus and T. C. Chua (Applied Materials),
*Method and apparatus for plasma nitridation of gate dielectrics using
amplitude modulated radio-frequency energy*, US 7,514,373 B2, filed
2006-05-31 (priority 2003-05-28), granted 2009-04-07.
<https://patents.google.com/patent/US7514373B2/en> A
"smooth-varying modulated RF power source to reduce electron temperature
spike" in plasma nitridation, improving channel mobility and gate leakage
over square-wave modulation. Used on the plasma nitridation chamber page.
Tier: deep dive (patent).

**PAT-DPN-ANNEAL-CHARTERED** — D. Zhong, Y. Tan, C. Ang and J. Zheng
(Chartered Semiconductor Manufacturing), *Ultra-thin gate oxide through
post decoupled plasma nitridation anneal*, US 2003/0170956 A1, filed
2002-03-06, published 2003-09-11.
<https://patents.google.com/patent/US20030170956A1/en> Replaces the
conventional post-DPN anneal "in pure helium" with one "in a 1:4
oxygen-nitrogen mixture (1,050° C. at about 10 torr)". Used on the plasma
nitridation chamber page. Tier: deep dive (patent).

**TEL-TRIASE** — Tokyo Electron, *Deposition Trias e+ Series*, product
page, accessed 2026-09-13. <https://www.tel.com/product/triase.html> The
Trias e+ single-wafer platform for 300 mm modules; the Trias SPA series'
"Slot Plane Antenna technology" generates "high-density, low-electron
temperature plasma". Used on the plasma nitridation chamber page. Tier:
cross-check (vendor statement).

**LEK-2002** — C. M. Lek, B. J. Cho, C. H. Ang, S. S. Tan, W. Y. Loh,
J. Z. Zhen and L. Chan, "Impact of decoupled plasma nitridation of
ultra-thin gate oxide on the performance of p-channel MOSFETs",
*Semiconductor Science and Technology* **17**(6), L25–L28 (2002).
<https://doi.org/10.1088/0268-1242/17/6/101> DPN of 15–17 Å oxides
suppresses boron penetration by placing nitrogen near the top interface,
but lowers transconductance and raises interface-trap density compared
with thermal nitridation. Used on the plasma nitridation chamber page.
Tier: deep dive.

**CHEN-2002-RPN** — C.-H. Chen, Y.-K. Fang, S.-F. Ting, W.-T. Hsieh,
C.-W. Yang, T.-H. Hsu, M.-C. Yu, T.-L. Lee, S.-C. Chen, C.-H. Yu and
M.-S. Liang, "Downscaling limit of equivalent oxide thickness in
formation of ultrathin gate dielectric by thermal-enhanced remote plasma
nitridation", *IEEE Transactions on Electron Devices* **49**(5), 840–846
(2002). <https://doi.org/10.1109/16.998593> Radical-induced reoxidation
below 20 Å base oxide, effective EOT reduction above 17 Å, and a 14 Å EOT
limit for remote plasma nitridation. Used on the plasma nitridation
chamber page. Tier: deep dive.

**YEO-2003** — K. L. Yeo, A. T. S. Wee, R. Liu, F. F. Zhou and A. See,
"Investigation of boron penetration through decoupled plasma nitrided
gate oxide using backside secondary ion mass spectrometry depth
profiling", *Journal of Vacuum Science & Technology B* **21**(1), 193–197
(2003). <https://doi.org/10.1116/1.1535925> Backside SIMS on SOI wafers to
quantify boron penetration through DPN oxide after rapid thermal
activation. Used on the plasma nitridation chamber page. Tier: deep dive.

#### Etch, strip and clean machine pages (first cited there)

The entries below were introduced by the three plasma-etcher pages, the
downstream plasma asher page and the wet bench and spray processor page,
and are grouped in that order by the page that first cited them. The
vendor press releases and product pages were fetched on 2026-09-13; the
papers were checked through Crossref and OpenAlex on that date, and
their annotations rest on their abstracts.

**AMAT-DPS-PLUS-1999** — Applied Materials, *Applied Materials Launches
Silicon Etch System for Sub-0.15 Micron Chip Generations* (Silicon Etch
DPS Plus Centura), press release, 1999-06-24.
<https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-launches-silicon-etch-system-sub-015-micron>
The DPS Plus on the Etch Centura II platform: "Predictive Endpoint" for a
"soft-landing" before the gate oxide, in use in "more than 80 Silicon
Etch DPS process chambers"; "More than 350 silicon etch DPS chambers"
installed; the DPS Centura "Introduced in 1997"; a dome temperature
control design and "A dual cooling zone ceramic electrostatic chuck".
Used on the silicon and polysilicon plasma etcher page. Tier:
cross-check (vendor statement).

**AMAT-300-ETCH-2000** — Applied Materials, *Applied Materials Unveils
300mm Etch Product Line*, press release, 2000-07-10.
<https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-unveils-300mm-etch-product-line>
Applied's 300 mm etchers on the Centura 300 platform, "derived from
Applied Materials' production-proven Centura 200mm design": the
Dielectric Etch eMax 300 and IPS 300, the Silicon and Metal Etch DPS 300,
"200mm-proven chamber materials and surface coatings", and a metal etch
strip chamber "based on its 200mm ASP technology" that also performs a
passivation. Used on the silicon, dielectric and metal plasma etcher
pages and the downstream plasma asher page. Tier: cross-check (vendor
statement).

**LAM-2300-2000** — Lam Research, *Lam Research Corporation Launches
Industry's First 200- And 300-Mm Capable Etch Product Line*, press
release, 2000-11-16.
<https://newsroom.lamresearch.com/2000-11-16-Lam-Research-Corporation-Launches-Industrys-First-200-And-300-Mm-Capable-Etch-Product-Line>
The 2300 Etch Series "for both 200- and 300-mm wafers", a platform that
"handles four process modules": the 2300 Exelan dielectric etcher, the
Versys Silicon (gate BARC, resist trim, hardmask open and STI in one
chamber; "in situ waferless auto cleans"; interferometric endpoint) and
the Versys Metal ("aluminum etch and integrated resist removal",
convertible to a silicon etch chamber). Used on the silicon, dielectric
and metal plasma etcher pages. Tier: cross-check (vendor statement).

**ALLWIN-RAINBOW-4400** — Allwin21, *Lam Rainbow 44XX Plasma Etcher*,
reseller product description, accessed 2026-09-13.
<https://allwin21.com/lam-rainbow-44xx-plasma-etcher/> The Rainbow
etchers as "single-wafer plasma/RIE etching systems" for 6-inch or
8-inch wafers with upper and lower RF match networks "for programmable
switching between plasma and RIE modes"; 44XX applications including
native-oxide breakthrough, a three-step nitride spacer etch and a
"Cl2/HBr Main Etch and Cl2/HBr/O2 Overetch" for doped polysilicon; a
typical gas list. Used on the silicon and polysilicon plasma etcher
page. Tier: high-level (reseller description).

**CUNGE-2005** — G. Cunge, M. Kogelschatz, O. Joubert and N. Sadeghi,
"Plasma–wall interactions during silicon etching processes in
high-density HBr/Cl₂/O₂ plasmas", *Plasma Sources Science and
Technology* **14**(2), S42–S52 (2005).
<https://doi.org/10.1088/0963-0252/14/2/S06> SiClₓ radical densities and
reactor-wall deposits in gate-etch plasmas: walls "stay clean" without
O₂, and a silicon oxychloride layer grows on them as O₂ is added. Used
on the silicon and polysilicon plasma etcher page. Tier: deep dive.
Also used on the hardware consumables material page.

**WIKI-HBR** — Wikipedia, *Hydrogen bromide*.
<https://en.wikipedia.org/wiki/Hydrogen_bromide> The silicon etch gas
and its hazard ("highly corrosive and, if inhaled, can cause lung
damage"). Used on the silicon and polysilicon plasma etcher page. Tier:
high-level.
Also used on the etch and chamber-clean gases material page.

**WIKI-NF3** — Wikipedia, *Nitrogen trifluoride*.
<https://en.wikipedia.org/wiki/Nitrogen_trifluoride> NF₃ broken down in
a plasma to fluorine radicals that attack polysilicon, nitride and
oxide, and its use to clean PECVD chambers; a GWP "17,200 times greater
than that of CO2", citing the IPCC fourth assessment (AR4). Used on the
silicon and polysilicon plasma etcher page. Tier: high-level.
Also used on the PECVD, HDP-CVD and tungsten CVD pages.
Also used on the hardware consumables material page.
Also used on the etch and chamber-clean gases material page.

**ALLWIN-RAINBOW-4500** — Allwin21, *Lam Rainbow 45XX Plasma Etcher*,
reseller product description, accessed 2026-09-13.
<https://allwin21.com/lam-rainbow-45xx-plasma-etcher/> The Rainbow 45XX
parallel-plate etchers, "mainly for Oxide Etch": Ar/CF₄/CHF₃ contact and
oxide spacer etches selective to polysilicon, etch-back planarisation, a
front-end nitride etch, and a helium backside-cooling controller. Used
on the dielectric and nitride plasma etcher page. Tier: high-level
(reseller description).

**PAT-MERIE-AMAT** — D. Cheng, V. J. Zeitlin, D. L. Andrews, M. Chang,
D. Maydan, S. Somekh, K. R. Stalder, D. N. Wang, J. M. White and J. Y. K.
Wong (Applied Materials), *Magnetic field-enhanced plasma etch reactor*,
US 4,842,683 A, filed 1988-04-25, granted 1989-06-27.
<https://patents.google.com/patent/US4842683A/en> A magnetic field
enhanced single-wafer etch reactor with a stepped magnetic field for
uniform etching at high pressure, a gas-cooled wafer interface, quartz
protective coatings and in-situ self-cleaning. Used on the dielectric
and nitride plasma etcher page. Tier: cross-check (patent).

**KASTENMEIER-1998** — B. E. E. Kastenmeier, P. J. Matsuo, G. S.
Oehrlein and J. G. Langan, "Remote plasma etching of silicon nitride and
silicon dioxide using NF₃/O₂ gas mixtures", *Journal of Vacuum Science &
Technology A* **16**(4), 2047–2056 (1998).
<https://doi.org/10.1116/1.581309> Nitride and oxide etching in the
afterglow of NF₃ and NF₃/O₂ microwave discharges; O₂ injection enhances
the nitride rate, attributed to NO at the surface. Used on the
dielectric and nitride plasma etcher page. Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

**BLANC-2013** — R. Blanc, F. Leverd, T. David and O. Joubert,
"Patterning of silicon nitride for CMOS gate spacer technology. I.
Mechanisms involved in the silicon consumption in CH₃F/O₂/He high
density plasmas", *Journal of Vacuum Science & Technology B* **31**(5),
051801 (2013). <https://doi.org/10.1116/1.4816466> Silicon recess under
CH₃F/O₂/He spacer etches: selectivity from a SiOₓFᵧ passivation layer,
and an oxidised layer driven by ion energy. Used on the dielectric and
nitride plasma etcher page. Tier: deep dive.

**WIKI-CHF3** — Wikipedia, *Fluoroform*.
<https://en.wikipedia.org/wiki/Fluoroform> CHF₃ and its use in plasma
etching of silicon oxide and nitride; a 100-year GWP of "14,800 for
HFC-23", citing the IPCC fourth assessment (AR4). Used on the dielectric
and nitride plasma etcher page. Tier: high-level.
Also used on the etch and chamber-clean gases material page.

**WIKI-C2F6** — Wikipedia, *Hexafluoroethane*.
<https://en.wikipedia.org/wiki/Hexafluoroethane> C₂F₆ as an etchant and
its global warming potential of 9200, given without naming an IPCC
assessment. Used on the dielectric and nitride plasma etcher page. Tier:
high-level.
Also used on the etch and chamber-clean gases material page.

**CHRISTIE-1994** — R. Christie, S. Burns, V. S. Grewal and B. Spuler,
"Sub 0.5 μm TCP metal etching in the ASTC", *Proceedings of 1994
IEEE/SEMI Advanced Semiconductor Manufacturing Conference and Workshop
(ASMC)*, p. 224. <https://doi.org/10.1109/ASMC.1994.588254> Sub-0.5 µm
aluminium etching "in a 200 mm LAM TCP 9600 Etch Chamber" and post-etch
treatment against corrosion, with resist selectivity, RIE lag, profile
uniformity and hardware life optimised (summary only). Used on the metal
plasma etcher page. Tier: deep dive.

**LAM-9600SE-STRIPPER-1998** — Lam Research Corporation, *Lam Research
Introduces Microwave Stripper for High-Density Metal Etch System*, news
item, Semiconductor Online, 1998-01-09.
<https://www.semiconductoronline.com/doc/lam-research-introduces-microwave-stripper-fo-0001>
A microwave stripper option for the TCP 9600SE, which etches aluminium
and tungsten in one chamber: a downstream source that avoids
charge-induced gate-oxide damage, polymer removal and "no corrosion
during 48-hour wet box tests". Used on the metal plasma etcher and
downstream plasma asher pages. Tier: cross-check (vendor statement).

**LAM-9600PTX-1999** — Lam Research, *Lam Research Corporation Gaining
Momentum In Metal Etch With Multiple Wins*, press release, 1999-02-16.
<https://newsroom.lamresearch.com/1999-02-16-Lam-Research-Corporation-Gaining-Momentum-In-Metal-Etch-With-Multiple-Wins>
Orders for the TCP 9600PTX metal etcher, claimed at 45 wafers per hour
against 35 for the competition, qualified for 0.18 µm aluminium etch
with 0.13 µm capability demonstrated. Used on the metal plasma etcher
page. Tier: cross-check (vendor statement).

**LAM-9600DFM-2001** — Lam Research, *Lam Research Corporation Takes
Metal Processing To New Level With New TCP 9600DFM*, press release,
2001-06-18.
<https://investor.lamresearch.com/2001-06-18-Lam-Research-Corporation-Takes-Metal-Processing-To-New-Level-With-New-TCP-R-9600DFM>
The TCP 9600DFM metal etcher for sub-150 nm applications, designed to cut
consumables cost, with a customer reporting a mean time between cleans
above 300 RF hours after moving from the 9600PTX. Used on the metal
plasma etcher page. Tier: cross-check (vendor statement).
Also used on the hardware consumables material page.

**AMAT-METAL-DPS-PLUS-1999** — Applied Materials, *Applied Materials
Introduces the Metal Etch DPS Plus Centura for Sub-0.18 Micron Metal
Etch*, press release, 1999-04-13.
<https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-metal-etch-dps-plus-centura-sub-018/>
The Metal Etch DPS Plus: throughput above 50 wafers per hour, uptime
above 90 %, lower defect densities, and "more than 200 Metal Etch DPS
Centura systems installed". Used on the metal plasma etcher page. Tier:
cross-check (vendor statement).

**WIKI-BCL3** — Wikipedia, *Boron trichloride*.
<https://en.wikipedia.org/wiki/Boron_trichloride> BCl₃ in semiconductor
plasma etching, where it etches metal oxides through volatile
oxychlorides. Used on the metal plasma etcher page. Tier: high-level.
Also used on the etch and chamber-clean gases material page.

**SEMISTAR-IRIDIA** — SemiStar Corp., *Novellus Gasonics PEP Iridia DL
Plasma Asher*, used-equipment listing, accessed 2026-09-13.
<http://www.semistarcorp.com/product/novellus-gasonics-pep-iridia-dl-plasma-asher/>
A dual-module PEP 4800DL system whose modules each carry an "Astex
Microwave Generator" and an "ENI ACG-5XL RF Generator", with gas lines
including CF₄, N₂, O₂ and 4 % H₂/N₂. Used on the downstream plasma asher
page. Tier: high-level (dealer listing).
Also used on the anneal ambients material page.

**SNF-AURA** — Stanford Nanofabrication Facility, *Gasonics Aura Asher
(gasonics)*, equipment page, accessed 2026-09-13.
<https://snfguide.stanford.edu/guide/equipment/gasonics-aura-asher-gasonics>
A GaSonics Aura downstream microwave asher: an O₂/N₂ plasma whose
products reach the wafer in an "afterglow" that is no longer electrically
damaging; single-wafer cassette loading and lamp heating. Used on the
downstream plasma asher page. Tier: high-level.

**SST-GASONICS-2000** — Solid State Technology, *Novellus Acquires
Gasonics*, 2000-10-27.
<https://sst.semiconductor-digest.com/2000/10/novellus-acquires-gasonics/>
Reports that Novellus "is acquiring" GaSonics International, "a
supplier of dry resist removal and surface preparation equipment", in a
stock-for-stock merger "valued at approximately $347 million": the deal
as announced in October 2000 (SST-NOVELLUS-SPEC-2006 dates the purchase
to 2001). Used on the downstream plasma asher page.
Tier: high-level (trade press).

**SST-NOVELLUS-SPEC-2006** — Solid State Technology, *Novellus
licenses–not sells–legacy strip tools to SPEC*, 2006-10-19.
<https://sst.semiconductor-digest.com/2006/10/novellus-licenses-not-sells-legacy-strip-tools-to-spec/>
Novellus licensed the GaSonics Aura 1000/2000LL, AE 2001/2000LL and L3510
strip systems to a refurbisher, while the Gamma and PEP Iridia lines from
what the article calls "Novellus' 2001 purchase of GaSonics" stayed with
Novellus (the deal was announced in October 2000, SST-GASONICS-2000). Used on the downstream
plasma asher page. Tier: high-level (trade press).

**AKRION-GAMA-SERIES** — Akrion Technologies, *GAMA Automated Wet
Station*, product page, accessed 2026-09-13.
<https://www.akriontech.com/product-3> The GAMA series as a modular batch
immersion wet station for cleaning, etching and stripping, with
concentration control and dilute chemistry. Used on the wet bench and
spray processor page. Tier: cross-check (vendor statement).

**LEENAARS-1990** — A. F. M. Leenaars, J. A. M. Huethorst and J. J. van
Oekel, "Marangoni drying: A new extremely clean drying process",
*Langmuir* **6**(11), 1701–1703 (1990).
<https://doi.org/10.1021/la00101a014> The paper that introduced
Marangoni drying (no abstract in Crossref or OpenAlex; the annotation
rests on the title). Used on the wet bench and spray processor page.
Tier: deep dive.
Also used on the wet chemicals material page.
Also used on the ultrapure water material page.

**PAT-DICO2-MKS** — C. Gottschalk, U. Brammer, J. Lohr and J. Seiwert
(MKS Instruments), *System and method for carbonation of deionized
water*, EP 2 104 648 B1, granted 2013-04-17.
<https://patents.google.com/patent/EP2104648B1/en> CO₂-dissolved DI water
for wet cleaning, whose dissolved CO₂ lowers the water's resistivity "to
a level that prevents surface charging". Used on the wet bench and spray
processor page. Tier: cross-check (patent).
Also used on the ultrapure water material page.

**PAT-EKC-HYDROXYLAMINE** — W. M. Lee (EKC Technology), *Cleaning
compositions for removing etching residue and method of using*,
US 5,334,332 A, filed 1992-07-09, granted 1994-08-02.
<https://patents.google.com/patent/US5334332A/en> Resist and etch-residue
removers of hydroxylamine and an alkanolamine, with a chelating agent
such as 1,2-dihydroxybenzene. Used on the wet bench and spray processor
page. Tier: cross-check (patent).
Also used on the wet chemicals material page.

**PAT-SPRAY-SEMITOOL** — C. Meuchel, M. Bernt and T. Henke (Semitool),
*Centrifugal spray processor and retrofit kit*, US 7,305,999 B2, filed
2002-07-19, granted 2007-12-11.
<https://patents.google.com/patent/US7305999B2/en> A centrifugal spray
processor with cassettes in a motor-driven rotor and arrays of smaller,
higher-back-pressure nozzles to cut chemical consumption. Used on the wet
bench and spray processor page. Tier: cross-check (patent).

**SCREEN-WS820** — SCREEN Semiconductor Solutions, *Wet Station: WS-620C
/ WS-820L*, product page, accessed 2026-09-13.
<https://www.screen.co.jp/spe/en/products/ws-620c820l> The WS-620C
(150 mm) and WS-820C and WS-820L (200 mm, carrier and carrierless) wet
stations: up to 13 baths and six transfer robots, and an optional
low-pressure drying unit against watermarks. Used on the wet bench and
spray processor page. Tier: cross-check (vendor statement).

**SST-AKRION-SCP-2007** — Solid State Technology, *Akrion sells "SCP"
automated wet station for wafer cleaning*, 2007-06-11.
<https://sst.semiconductor-digest.com/2007/06/akrion-sells-scp-automated-wet-station-for-wafer-cleaning/>
Sale of an Akrion E200 200 mm wet bench for resist strip and etch; the
E200's RCA-clean, nitride-etch and strip configurations, rinse tanks and
dryers with "true" HF-last capability; Akrion's 2006 purchase of SCP
Global Technologies' assets. Used on the wet bench and spray processor
page. Tier: high-level (trade press).

**TEL-MERCURY-2018** — Tokyo Electron, *TEL announces the relaunch of
MERCURY MP, a Batch Spray Cleaning System*, news release, 2018-07-10,
accessed 2026-09-13.
<https://www.tel.com/news/product/2018/20180710_001.html> The return to
production of the MERCURY batch spray cleaner for 75–200 mm wafers, with
"over 1,000 systems installed"; a 2024 notice on the page transfers the
product line to another supplier. Used on the wet bench and spray
processor page. Tier: cross-check (vendor statement).
Also used on the etch and strip category pages.

#### Deposition machine pages (first cited there)

The entries below were introduced by the PECVD, HDP-CVD, tungsten CVD
and PVD cluster tool pages, and are grouped in that order by the page
that first cited them. The vendor pages of 1998–2003 were read from the
Wayback Machine captures named in each entry, the patents through Google
Patents (bibliographic data, abstract and the passages quoted), and the
papers through Crossref and OpenAlex, all on 2026-09-13; the annotations
of papers rest on their abstracts.

**NOVELLUS-PECVD-1998** — Novellus Systems, *Dielectric – PECVD
Solutions*, product page; Wayback Machine capture of 1998-06-11.
<https://web.archive.org/web/19980611202815/http://www.novellus.com:80/products/pecvd.htm>
Novellus's PECVD line: the Concept One ("Introduced in 1987", "150/200mm"),
the Concept One MAXUS with "an enhanced dual frequency design", the
Concept Two Sequel, which "integrates the production-proven Concept One
process chamber on Concept Two's modular platform", and the Dual Sequel,
which "combines two process chambers with 12 deposition stations". Used
on the PECVD page. Tier: cross-check (vendor statement).

**NOVELLUS-PECVD-2002** — Novellus Systems, *Dielectric – PECVD
Solutions*, product page; Wayback Machine capture of 2002-06-02.
<https://web.archive.org/web/20020602073706/http://www.novellus.com:80/products/pecvd.asp>
The Sequel Express and Dual Sequel Express, the 300 mm Concept Three
Sequel, whose "multistation sequential deposition" "offers superior
reproducibility because every wafer sees the same environment", and the
VECTOR, "Introduced in 2000" as "a 200mm/300mm bridge tool". Used on the
PECVD page. Tier: cross-check (vendor statement).

**AMAT-PRODUCER-2001** — Applied Materials, *PECVD* (Producer), product
page; Wayback Machine capture of 2001-08-17.
<https://web.archive.org/web/20010817124824/http://www.appliedmaterials.com:80/products/pecvd.html>
The Producer as "the first 200mm system to be upgradable to meet future
300mm needs", with "single-wafer twin process chambers that permit
simultaneous processing of two wafers side-by-side in separate
compartments with identical environments" and up to three twin chambers.
Used on the PECVD page. Tier: cross-check (vendor statement).

**AMAT-PRODUCER-SE-2001** — Applied Materials, *Producer SE*, product
page; Wayback Machine capture of 2001-08-17.
<https://web.archive.org/web/20010817134045/http://www.appliedmaterials.com:80/products/producer_se.html>
The Producer "Since its introduction in 1998", and the Producer SE with
one to three chambers, twin wafer handling and "a new low-flow remote
clean that reduces gas costs by up to 40 percent". Used on the PECVD
page. Tier: cross-check (vendor statement).
Also used on the etch and chamber-clean gases material page.

**AMAT-PECVD-TEOS-2002** — Applied Materials, *Producer PECVD TEOS
Oxide*, product page; Wayback Machine capture of 2002-07-01.
<https://web.archive.org/web/20020701042739/http://www.appliedmaterials.com:80/products/pecvd_teos_oxide.html>
PECVD TEOS oxides that "can be used as liners or cap layers for HDP-CVD
applications and as the dielectric for damascene schemes", "available in
single and mixed frequency". Used on the PECVD page. Tier: cross-check
(vendor statement).

**AMAT-PECVD-PSG-2002** — Applied Materials, *Producer PECVD TEOS PSG*,
product page; Wayback Machine capture of 2002-07-05.
<https://web.archive.org/web/20020705144451/http://www.appliedmaterials.com:80/products/pecvd_teos_psg.html>
PECVD TEOS PSG films "for PMD applications, demonstrating outstanding
gettering properties, which prevent device damage". Used on the PECVD
page. Tier: cross-check (vendor statement).

**AMAT-PECVD-SIN-2002** — Applied Materials, *Producer PECVD Nitride*,
product page; Wayback Machine capture of 2002-07-01.
<https://web.archive.org/web/20020701050143/http://www.appliedmaterials.com:80/products/pecvd_nitride.html>
PECVD nitrides from "single-wafer, twin chamber" hardware: UV-transparent,
passivation and damascene nitrides. Used on the PECVD page. Tier:
cross-check (vendor statement).

**AMAT-SACVD-2000** — Applied Materials, *SACVD* (Giga-Fill SACVD
Centura), product page; Wayback Machine capture of 2000-07-09.
<https://web.archive.org/web/20000709131617/http://www.appliedmaterials.com:80/products/sacvd.html>
SACVD introduced "in 1994 on its Precision 5000® platform", "Using TEOS
(tetraethylorthosilicate) and Ozone (O3) chemistry at near-atmospheric
pressure"; the Giga-Fill chamber's "ceramic heater" at ">550°C" for
"BPSG and STI applications", remote plasma clean and ">40,000" mean wafers
between cleans. Used on the PECVD page. Tier: cross-check (vendor
statement).
Also used on the precursors material page.

**AMAT-SIN-WP** — L. D'Cruz, C. Bencher and C. Ngai (Applied Materials),
*PECVD SiN performance as barrier/etch stop for Damascene copper
interconnects*, white paper, undated; Wayback Machine capture of
2003-03-08.
<https://web.archive.org/web/20030308041708/http://www.appliedmaterials.com:80/products/assets/dielectric/pecvd_sin_performance.pdf>
Thin 400 °C PECVD nitrides as etch stops and copper barriers; a
"400°C (LDR) nitride with thickness between 500Å and 1000Å" for MIM
capacitors "switching from oxide to nitride for increased specific
capacitance". Used on the PECVD page. Tier: deep dive (vendor white
paper).

**PAT-P5000-AMAT** — D. N. Wang, J. M. White, K. S. Law, C. Leung, S. P.
Umotoy, K. S. Collins, J. A. Adamik, I. Perlov and D. Maydan (Applied
Materials), *Thermal CVD/PECVD reactor and use for thermal chemical vapor
deposition of silicon dioxide and in-situ multi-step planarized process*,
US 5,000,113 A, filed 1986-12-19, granted 1991-03-19.
<https://patents.google.com/patent/US5000113A/en> A single-wafer reactor
"capable of thermal CVD, plasma-enhanced CVD, plasma-assisted etchback,
plasma self-cleaning, and deposition topography modification by
sputtering", with RF applied to the gas inlet manifold; plasma TEOS oxide
at "about 1 to 50 torr" and ozone–TEOS oxide at "10 torr to 200 torr".
Used on the PECVD page. Tier: cross-check (patent).

**PAT-RPC-AMAT** — G. Fong, L.-Q. Xia, S. Nemani and E. Yieh (Applied
Materials), *Methods and apparatus for cleaning surfaces in a substrate
processing system*, US 5,812,403 A, filed 1996-11-13, granted
1998-09-22. <https://patents.google.com/patent/US5812403A/en> A chamber
clean with reactive species from "a clean gas that is input to a remote
microwave plasma system", with the ceramic heater kept above about
500 °C. Used on the PECVD page. Tier: deep dive (patent).

**VAN-DE-VEN-1990** — E. P. van de Ven, I.-W. Connick and A. S. Harrus,
"Advantages of dual frequency PECVD for deposition of ILD and passivation
films", *Proc. Seventh International IEEE VLSI Multilevel Interconnection
Conference (VMIC 1990)*, pp. 194–201.
<https://doi.org/10.1109/VMIC.1990.127865> Dual-frequency PECVD of
nitride, oxynitride and TEOS oxide: the high frequency generates the
reactive species, the low frequency controls ion bombardment and with it
step coverage, stress and density. Used on the PECVD page. Tier: deep
dive.

**PEARCE-1992** — C. W. Pearce, R. F. Fetcho, M. D. Gross, R. F. Koefer
and R. A. Pudliner, "Characteristics of silicon nitride deposited by
plasma-enhanced chemical vapor deposition using a dual frequency
radio-frequency source", *Journal of Applied Physics* **71**(4),
1838–1841 (1992). <https://doi.org/10.1063/1.351396> Nitride deposited
with 270 kHz and 13.56 MHz sources; stress varied through the power split,
and low-frequency excitation favouring N–H bonds. Used on the PECVD page.
Tier: deep dive.

**COTLER-1993** — T. J. Cotler and J. Chapple-Sokol, "High Quality
Plasma-Enhanced Chemical Vapor Deposited Silicon Nitride Films", *Journal
of The Electrochemical Society* **140**(7), 2071–2075 (1993).
<https://doi.org/10.1149/1.2220766> PECVD nitride against LPCVD nitride:
stress shifting "from tensile to compressive with increasing temperature
and power", and all properties but conformality comparable. Used on the
PECVD page. Tier: deep dive.

**SOBOLEWSKI-1998** — M. A. Sobolewski, J. G. Langan and B. S. Felker,
"Electrical optimization of plasma-enhanced chemical vapor deposition
chamber cleaning plasmas", *Journal of Vacuum Science & Technology B*
**16**(1), 173–182 (1998). <https://doi.org/10.1116/1.589774> Electrical
measurements of NF₃/Ar, CF₄/O₂/Ar and C₂F₆/O₂/Ar chamber-clean plasmas in
a 13.56 MHz capacitive reactor, and the discharge impedance at which power
is absorbed most efficiently. Used on the PECVD page. Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

**ALLGOOD-2003** — C. Allgood, M. Mocella, H. Chae and H. Sawin,
"Evaluation of Octafluorocyclobutane as a Chamber Clean Gas in a
Plasma-Enhanced Silicon Dioxide Chemical Vapor Deposition Reactor",
*Journal of The Electrochemical Society* **150**(2), G122 (2003).
<https://doi.org/10.1149/1.1535911> Clean time and perfluorocompound
emissions of a C₄F₈-based chamber clean "in a Novellus Concept One 200, a
widely used commercial PECVD tool". Used on the PECVD page. Tier: deep
dive.

**WIKI-NOVELLUS** — Wikipedia, *Novellus Systems*.
<https://en.wikipedia.org/wiki/Novellus_Systems> The CVD, PECVD and PVD
equipment maker, its product lines and its acquisition by Lam Research,
"completed in June 2012". Used on the PECVD, HDP-CVD and tungsten CVD
pages. Tier: high-level.

**TRIKON-10K-1996** — Trikon Technologies, Inc., *Annual Report on Form
10-K for the fiscal year ended December 31, 1996*; copy on
GetFilings.com, Wayback Machine capture of 2008-10-12.
<http://web.archive.org/web/20081012193325/http://www.getfilings.com/o0000898430-97-001539.html>
Trikon's product lines after it acquired Electrotech "on November 15,
1996": the Delta 201, "a versatile, single-chamber production system for
producing films, including silicon dioxide or silicon nitride", and the
Planar 200 Flowfill, a "multi-chambered cluster system" in which "The
plasma CVD films are deposited in one module and the CVD planarizing
flow layer is deposited in the Flowfill(TM) module", offered against SOG
and HDP gap fill. Used on the PECVD and HDP-CVD pages.
Tier: cross-check (regulatory filing).
Also used on the FILOX, PSG, NCAPOX, NILD3 and NILD4 step pages.

**SEMITODAY-SPTS-2009** — Semiconductor Today, *Sumitomo Precision
Products completes acquisition of Aviza*, news item, 2009-10-19.
<https://www.semiconductor-today.com/news_items/2009/OCT/STS_191009.htm>
The lineage of Newport-based Electrotech "(founded in 1968)", bought in
1996 by Plasma & Materials Technologies, which became Trikon
Technologies; "Trikon later merged with Aviza Technology Inc in 2005",
and SPP's 2009 purchase of Aviza's assets to form SPP Process Technology
Systems (SPTS). Used on the PECVD page. Tier: high-level (trade press).
Also used on the NCAPOX step page.

**NOVELLUS-HDP-2001** — Novellus Systems, *Dielectric – HDP Solutions*,
product page; Wayback Machine capture of 2001-12-02.
<https://web.archive.org/web/20011202103556/http://www.novellus.com:80/products/hdp.asp>
HDP-CVD "provides void-free gap fill of high-quality dielectric films in
high aspect ratio device structures"; SPEED "captured the heart of the
marketplace in 1996", with a "patented hemispherical source" of "a single
excitation frequency and a single coil"; the SPEED/SEQUEL combining two
SPEED chambers with one SEQUEL chamber; the 300 mm Concept Three SPEED
with a "bi-polar electrostatic chuck". Used on the HDP-CVD page. Tier:
cross-check (vendor statement).

**AMAT-HDP-2001** — Applied Materials, *HDP-CVD* (Ultima HDP-CVD Centura
and Ultima X), product page; Wayback Machine capture of 2001-08-17.
<https://web.archive.org/web/20010817112354/http://www.appliedmaterials.com:80/products/hdp_cvd.html>
The Ultima "can deposit both undoped and doped films for numerous
processes including USG, FSG, PSG, SiN and low k films"; up to three
Ultima chambers, or Ultima and PECVD chambers, on the Centura platform;
the Ultima X "for both 200mm and 300mm advanced STI, IMD and PMD
applications". Used on the HDP-CVD page. Tier: cross-check (vendor
statement).

**AMAT-HDP-PSG-2002** — Applied Materials, *Ultima HDP-CVD PSG*, product
page; Wayback Machine capture of 2002-10-21.
<https://web.archive.org/web/20021021022321/http://www.appliedmaterials.com:80/products/hdp_cvd_psg.html>
An HDP PSG for 0.18 µm devices and below at the pre-metal dielectric
level, whose films "provide ion-gettering properties as well as device
isolation". Used on the HDP-CVD page. Tier: cross-check (vendor
statement).

**AMAT-HDP-IMD-2002** — Applied Materials, *Ultima HDP-CVD (USG) IMD*,
product page; Wayback Machine capture of 2002-08-09.
<https://web.archive.org/web/20020809163156/http://www.appliedmaterials.com:80/products/hdp_cvd_usg_imd.html>
A "low-temperature USG" for IMD and passivation "with demonstrated gap
fill down to 0.25 microns in 3:1 aspect ratio structures". Used on the
HDP-CVD page. Tier: cross-check (vendor statement).

**AMAT-HDP-STI-2002** — Applied Materials, *Ultima HDP-CVD (USG) STI*,
product page; Wayback Machine capture of 2002-08-09.
<https://web.archive.org/web/20020809163834/http://www.appliedmaterials.com:80/products/hdp_cvd_usg_sti.html>
"high-temperature USG" for shallow trench isolation, with void-free fill
"down to 0.12-micron, 4:1-aspect-ratio spaces for use in 0.18-micron
device generations and beyond". Used on the HDP-CVD page. Tier:
cross-check (vendor statement).

**PAT-ICP-NOVELLUS** — J. C. Benzing, E. K. Broadbent and J. K. H. Rough
(Novellus Systems), *Induction plasma source*, US 5,346,578 A, filed
1992-11-04, granted 1994-09-13.
<https://patents.google.com/patent/US5346578A/en> A "hemispherically
shaped induction coil" around a quartz bell jar, driven at "about 450
KHz" at "about 0.1-100 mTorr", with a high-frequency source that
"independently adjusts the bias voltage on the wafer"; the description
notes that with "careful substrate bias control" the source "is suitable
for dielectric gap filling". Used on the HDP-CVD and PVD cluster tool
pages. Tier: cross-check (patent).

**PAT-HDP-REACTOR-AMAT** — F. C. Redeker, F. Moghadam, H. Hanawa, T.
Ishikawa, D. Maydan, S. Li, B. Lue, R. J. Steger, M. Wong, Y. Wong and
A. K. Sinha (Applied Materials), *Symmetric tunable inductively coupled
HDP-CVD reactor*, US 6,170,428 B1, filed 1996-07-15, granted 2001-01-09.
<https://patents.google.com/patent/US6170428B1/en> An HDP-CVD tool with
simultaneous deposition and sputtering: dual RF zone inductive source,
dual-zone gas distribution, temperature-controlled dome, turbomolecular
pumping, "a dual helium cooling zone electrostatic chuck", ceramic and
aluminium-alloy construction and a remote fluorine plasma clean. Used on
the HDP-CVD page. Tier: cross-check (patent).
Also used on the hardware consumables material page.

**PAT-HDP-CLEAN-NOVELLUS** — M. D. Kilgore, W. G. M. van den Hoek, C. J.
Rau, B. J. van Schravendijk, J. A. Tobin, T. W. Mountsier and J. C.
Oswalt (Novellus Systems), *Chemical vapor deposition system including
dedicated cleaning gas injection*, US 6,200,412 B1, filed 1996-02-16,
granted 2001-03-13. <https://patents.google.com/patent/US6200412B1/en>
A dedicated clean-gas injector in an HDP-CVD chamber with a hemispherical
coil, and the fluorine residue that "must be removed for safety reasons
and to insure that the film adheres". Used on the HDP-CVD page. Tier:
deep dive (patent).

**PAT-SEASONING-AMAT** — K. Rossman, T. Sahin, H. M'Saad and R. Nowak
(Applied Materials), *Reduction of mobile ion and metal contamination in
HDP-CVD chambers using chamber seasoning film depositions*, US 6,121,161
A, filed 1999-01-19, granted 2000-09-19.
<https://patents.google.com/patent/US6121161A/en> Sodium from the quartz
dome and alumina nozzles of an HDP-CVD chamber, and a seasoning film
deposited after each clean to hold it back. Used on the HDP-CVD page.
Tier: deep dive (patent).
Also used on the hardware consumables material page.

**SCHWARTZ-1992** — G. C. Schwartz and P. Johns, "Gap-Fill with PECVD
SiO₂ Using Deposition/Sputter Etch Cycles", *Journal of The
Electrochemical Society* **139**(3), 927–932 (1992).
<https://doi.org/10.1149/1.2069327> Gap fill between metal lines by
cycles of PECVD oxide and argon sputter etching: a fast-etching region and
then voids as the aspect ratio rises. Used on the HDP-CVD page. Tier:
deep dive.

**LEE-1998-STI** — S.-H. Lee, J.-H. Son, H.-D. Lee, W. Yang and Y.-J.
Lee, "Shallow Trench Isolation Characteristics with High-Density-Plasma
Chemical Vapor Deposition Gap-Fill Oxide for Deep-Submicron CMOS
Technologies", *Japanese Journal of Applied Physics* **37**(3S), 1222
(1998). <https://doi.org/10.1143/JJAP.37.1222> STI leakage and isolation
with HDP-CVD fill at different deposition/sputter ratios and liner
thicknesses, with "negligible sputter effect of HDP" on the trench
sidewall. Used on the HDP-CVD page. Tier: deep dive.

**NOVELLUS-WCVD-1998** — Novellus Systems, *Tungsten Product Solutions*
(metal CVD), product page; Wayback Machine capture of 1998-06-11.
<https://web.archive.org/web/19980611202803/http://www.novellus.com:80/products/cvd.htm>
Blanket tungsten "for plug fill and low-stress composite interconnects"
with "high-pressure nucleation, resistive heating, vacuum wafer clamping
and full-coverage deposition, using patented wafer backside exclusion
technology"; the Concept Two Altus, "Integrating the Concept One tungsten
process chamber on the modular Concept Two platform", and the Dual Altus
with "a total of 10 stations". Used on the tungsten CVD page. Tier:
cross-check (vendor statement).

**NOVELLUS-WCVD-2002** — Novellus Systems, *Tungsten Product Solutions*
(metal CVD), product page; Wayback Machine capture of 2002-02-10.
<https://web.archive.org/web/20020210183923/http://www.novellus.com:80/products/cvd.asp>
The Altus and Dual Altus, the PRISM MOCVD TiN system and the 300 mm
Concept Three Altus with "a new exclusion ring reference design". Used on
the tungsten CVD page. Tier: cross-check (vendor statement).
Also used on the hardware consumables material page.

**AMAT-ISM-2000** — Applied Materials, *Interconnect Systems & Modules*
(liner/barrier and tungsten CVD systems), product page; Wayback Machine
capture of 2000-08-15.
<https://web.archive.org/web/20000815075033/http://www.appliedmaterials.com:80/products/ism_liner.html>
The WxZ Centura as "the industry's leading tungsten chemical vapor
deposition (WCVD) tool for plug fill and interconnects", with a remote
microwave clean; the Sprint Centura, which "operates at 300 Torr" at
">60 wph"; and the Endura Integrated PVD/CVD Liner/Barrier system with a
Vectra IMP Ti chamber, a CVD TiN TxZ chamber and a Preclean II chamber,
and the Vectra IMP chamber's bottom coverage and chamber count. Used on
the tungsten CVD and PVD cluster tool pages. Tier: cross-check (vendor
statement).
Also used on the sputter targets material page.
Also used on the hardware consumables material page.

**PAT-BACKSIDE-NOVELLUS** — E. P. van de Ven, E. K. Broadbent, J. C.
Benzing, B. L. Chin and C. W. Burkhart (Novellus Systems), *Gas-based
backside protection during substrate processing*, US 5,374,594 A, filed
1993-01-22, granted 1994-12-20.
<https://patents.google.com/patent/US5374594A/en> Argon or argon–hydrogen
backside gas at each station of a tungsten CVD reactor, fed at the edge of
a vacuum chuck at a pressure above the chamber's so that process gas does
not reach the wafer backside. Used on the tungsten CVD page. Tier:
cross-check (patent).

**PAT-MULTISTATION-NOVELLUS** — E. J. McInerney, T. M. Pratt and S. D.
Hancock (Novellus Systems), *Isolation of incompatible processes in a
multi-station processing chamber*, US 6,319,553 B1, filed 2000-02-28,
granted 2001-11-20. <https://patents.google.com/patent/US6319553B1/en>
Pedestals in wells under flush showerheads, an indexing plate and an
argon purge plate, so that silane initiation and WF₆ nucleation or
hydrogen reduction can run at different stations of one chamber. Used on
the tungsten CVD page. Tier: cross-check (patent).

**RILEY-1991** — P. E. Riley and T. E. Clark, "Integrated Chemical Vapor
Deposition and Plasma Etchback of Tungsten in a Multichamber,
Single-Wafer System", *Journal of The Electrochemical Society*
**138**(10), 3008–3013 (1991). <https://doi.org/10.1149/1.2085356>
Tungsten plugs by deposition at 80 torr and 475 °C and a two-step
magnetron-enhanced etchback on an Applied Materials P5000 WCVD system for
150 mm wafers. Used on the tungsten CVD page. Tier: deep dive.

**NOVELLUS-PVD-1998** — Novellus Systems, *Metal – PVD Solutions*,
product page; Wayback Machine capture of 1998-06-11.
<https://web.archive.org/web/19980611202757/http://www.novellus.com:80/products/pvd.htm>
The INOVA, "made possible through the acquisition of the Thin Film
Systems business of Varian Associates, Inc.", delivering "Maxfill™
aluminum and superior Ti/Ti-nitride film quality"; a Ti/TiN process "in
production with Controlled Divergence Technology" ahead of the ionised
HCM source. Used on the PVD cluster tool page. Tier: cross-check (vendor
statement).

**NOVELLUS-PVD-2001** — Novellus Systems, *Metal PVD Solutions*, product
page; Wayback Machine capture of 2001-12-14.
<https://web.archive.org/web/20011214001648/http://www.novellus.com:80/products/pvd.asp>
The INOVA with the Hollow Cathode Magnetron source, whose "HCM Ti/TiN
films make an excellent diffusion barrier for CVD W applications", the
"MaxFill™ low pressure aluminum plug solution", and the 300 mm INOVA xT
of 2000. Used on the PVD cluster tool page. Tier: cross-check (vendor
statement).

**AMAT-ISM-CU-2000** — Applied Materials, *Interconnect Systems & Modules*
(copper and aluminium systems, Endura SL), product page; Wayback Machine
capture of 2000-08-16.
<https://web.archive.org/web/20000816055835/http://www.appliedmaterials.com:80/products/ism_coppalum.html>
The Endura SL with "dual VHP+ robots" and "up to six process chambers"
at "greater than 60 wph", and Applied's IMP and SIP copper barrier and
seed chambers. Used on the PVD cluster tool page. Tier: cross-check
(vendor statement).

**AMAT-LINER-BARRIER-2001** — Applied Materials, *Aluminum
Liner/Barrier*, product page; Wayback Machine capture of 2001-08-07.
<https://web.archive.org/web/20010807161527/http://www.appliedmaterials.com:80/products/liner_barrier.html>
The Integrated PVD/CVD Liner/Barrier system on the Endura, and the
Self-Ionized Plasma (SIP) Ti/TiN ("TTN") chamber, "used in volume
production for advanced devices with aspect ratios of 7:1", with a
"biased electrostatic chuck". Used on the PVD cluster tool page. Tier:
cross-check (vendor statement).

**AMAT-AL-SLAB-2002** — Applied Materials, *Aluminum Slab and Fill*,
product page; Wayback Machine capture of 2002-06-25.
<https://web.archive.org/web/20020625163718/http://www.appliedmaterials.com:80/products/aluminum_slab_and_fill.html>
The Endura PVD aluminium slab system, which "deposits aluminum over
tungsten plugs in logic and DRAM devices to form metal wiring", and the
ALPS+ aluminium fill source with "low-fill temperatures (<430°C)". Used
on the PVD cluster tool page. Tier: cross-check (vendor statement).

**PAT-STAGED-VACUUM-AMAT** — A. Tepman, H. Grunes, S. Somekh and D.
Maydan (Applied Materials), *Staged-vacuum wafer processing system and
method*, US 5,186,718 A, filed 1991-04-15 (priority 1989-05-19), granted
1993-02-16. <https://patents.google.com/patent/US5186718A/en> A
multi-chamber platform with isolated vacuum stages and a vacuum gradient
from the load locks to the process chambers, separate buffer and transfer
robots, and pre-clean and cool-down chambers in the paths between them.
Used on the PVD cluster tool page. Tier: cross-check (patent).

**PAT-COLLIMATOR-VARIAN** — R. E. Demaray, V. E. Hoffman, J. C. Helmer,
Y. H. Park and R. R. Cochran (Varian Associates), *Collimated deposition
apparatus and method*, US 5,330,628 A, filed 1991-10-23 (priority
1990-01-29), granted 1994-07-19.
<https://patents.google.com/patent/US5330628A/en> Sputtering at a
pressure low enough to avoid gas scattering, through "a collimating filter
having a plurality of transmissive cells with a length to diameter ratio
on the order of 1:1 to 3:1", for step coverage in holes. Used on the PVD
cluster tool page. Tier: cross-check (patent).

**PAT-IMP-COIL-AMAT** — K. K.-T. Ngan (Applied Materials), *Avoiding
contamination from induction coil in ionized sputtering*, US 5,707,498 A,
filed 1996-07-12, granted 1998-01-13.
<https://patents.google.com/patent/US5707498A/en> In an inductively
coupled sputtering chamber, a "pasting" step with no coil power coats the
coil with target material, repeated after a number of wafers, so that
material sputtered off the coil does not contaminate the film. Used on
the PVD cluster tool page. Tier: deep dive (patent).
Also used on the sputter targets material page.
Also used on the hardware consumables material page.

#### Lithography machine pages (first cited there)

The entries below were introduced by the i-line stepper or scanner, DUV
(KrF, 248 nm) stepper or scanner, coat/develop track and CD-SEM and
overlay metrology pages, and are grouped in that order by the page that
first cited them. The vendor data sheets, product pages and press
releases were fetched on 2026-09-13; the papers were checked through
Crossref and OpenAlex on that date, and their annotations rest on their
abstracts.

**ASML-PAS5500-100D** — ASML, *PAS 5500/100D i-Line Stepper*, refurbished
systems data sheet, 2019.
<https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-100d.pdf>
An i-line stepper "designed for mass production at 0.4 µm": wavelength
365 nm, NA "0.48—0.60 (variable)", field 31.1 mm diameter and 22.0 mm ×
27.4 mm, usable depth of focus ≥ 1.1 µm, overlay < 60 nm, ≥ 72 wafers per
hour on 200 mm, a 1.5 kW illuminator, field-by-field levelling and
through-the-lens phase-grating alignment. Used on the i-line stepper or
scanner page. Tier: cross-check (vendor statement).

**ASML-PAS5500-275D** — ASML, *PAS 5500/275D High Productivity i-Line
Stepper*, refurbished systems data sheet, 2019.
<https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-275d.pdf>
An i-line stepper "stretching resolution down to 0.28 µm": NA 0.48–0.60,
single-machine overlay ≤ 40 nm and ≤ 80 nm matched to another /275,
≥ 100 wafers per hour on 200 mm at 200 mJ/cm², a 3.5 kW AERIAL
illuminator with conventional and annular modes, and phase-modulated
TTL alignment. Used on the i-line stepper or scanner page. Tier:
cross-check (vendor statement).
Also used on the DNM, LVTNM, NWM and HVTPM mask pages.

**ASML-PAS5500-450F** — ASML, *PAS 5500/450F i-Line Step-and-Scan*,
refurbished systems data sheet, 2019.
<https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-450f.pdf>
The i-line scanner "successor of the PAS 5500/400 for non-critical
applications": a 0.48–0.65 NA 4× lens, 26.0 mm × 33.0 mm field,
resolution ≤ 220 nm, ≥ 150 wafers per hour on 200 mm, and commonality
with the PAS 5500 DUV and 193 nm scanners "Optimized for
mix-and-matching". Used on the i-line stepper or scanner page. Tier:
cross-check (vendor statement).

**CANON-FPA3000I5PLUS-1998** — Semiconductor Online, *High Productivity
i-Line Lithography Stepper* (Canon U.S.A. announcement of the FPA-3000i5+
for SEMICON/Europa '98).
<https://www.semiconductoronline.com/doc/high-productivity-i-line-lithography-stepper-0001>
A 5:1 i-line stepper with NA 0.45–0.63, resolution below 0.35 µm, a
22 mm × 22 mm field, alignment accuracy below 40 nm and 100 wafers per
hour on 200 mm at 90 mJ/cm², designed "as a mix-and-match companion for
its FPA-3000EX5 DUV stepper". Used on the i-line stepper or scanner page.
Tier: cross-check (vendor statement).

**CANON-FPA3030I5PLUS** — Canon U.S.A., *FPA-3030i5+ Stepper Product
Specifications*, 2015.
<http://downloads.canon.com/nw/pdfs/industrial/fpa-3030i5-plus-stepper-specs.pdf>
A current 200 mm/150 mm i-line stepper: resolution ≤ 0.35 µm, NA
0.45–0.63, 5:1, 22 mm × 22 mm field, overlay ≤ 40 nm, ≥ 104 wafers per
hour on 200 mm. Used on the i-line stepper or scanner page. Tier:
cross-check (vendor statement).

**NIKON-S202A-S102B** — Semiconductor Online, *Two Scanning Steppers*
(Nikon Precision Europe announcement of the NSR-S202A and NSR-S102B),
undated.
<https://www.semiconductoronline.com/doc/two-scanning-steppers-0001> Two
scanning steppers "designed for 256M DRAM mass production" with 25 mm ×
33 mm fields, synchronised reticle and wafer stages and designs that
accommodate mix-and-match: the KrF NSR-S202A (80 wafers per hour on
8-inch wafers) and the i-line NSR-S102B ("0.35 micron or better
resolution") for "less critical layers". Used on the i-line stepper or
scanner and DUV (KrF, 248 nm) stepper or scanner pages. Tier:
cross-check (vendor statement).

**NIKON-2205IL1** — Nikon, *NSR-2205iL1 5x Reduction i-line Stepper*,
product page (announced 2023-08-31).
<https://www.nikon.com/business/semi/sp_nsr-2205il1/> A current 5×
i-line stepper for 2- to 8-inch wafers: resolution ≤ 350 nm, NA 0.45,
22 mm × 22 mm field, single-machine overlay ≤ 70 nm, compatible with
existing Nikon i-line recipes and photomasks. Used on the i-line stepper
or scanner page. Tier: cross-check (vendor statement).

**USHIO-UV-LAMPS** — Ushio Inc., *Super high-pressure UV lamps
(500W~35kW)*, product page.
<https://www.ushio.co.jp/en/products/1010.html> Lithography mercury
lamps using "three ultraviolet wavelengths (436, 405 and 365 nm)", with a
near-point arc, from 500 W to 35 kW class. Used on the i-line stepper or
scanner page. Tier: cross-check (vendor statement).
Also used on the lithography materials material page.

**KATO-2007** — A. Kato, *Chronology of Lithography Milestones*, version
0.9, May 2007, hosted on lithoguru.com.
<https://www.lithoguru.com/scientist/litho_history/Kato_Litho_History.pdf>
A dated list of exposure-tool milestones: the first i-line steppers of
Nikon (1984), ASML (1987) and Canon (1990), the first KrF steppers and
scanners (Nikon NSR-1505EX 1988, ASML PAS 5000/70 1991, SVGL Micrascan
1990 and Micrascan III 1996, Nikon NSR-S201A 1995, ASML PAS 5500/500 and
Canon FPA-4000ES1 1997), Cymer's market share and first solid-state KrF
laser, Ushio as the leading mercury-lamp supplier and Cobilt as the
origin of Tokyo Electron's tracks. Used on the i-line stepper or
scanner, DUV (KrF, 248 nm) stepper or scanner and coat/develop track
pages. Tier: high-level (industry chronology).

**BUCKLEY-1989** — J. D. Buckley, D. N. Galburt and C. Karatzas,
"Step-and-scan lithography using reduction optics", *Journal of Vacuum
Science & Technology B* **7**(6), 1607–1612 (1989).
<https://doi.org/10.1116/1.584499> A step-and-scan tool sequentially
scanning 20 mm × 32.5 mm subfields through 4:1 ring-field optics, with
reticle and wafer on separate synchronised stages. Used on the i-line
stepper or scanner and DUV (KrF, 248 nm) stepper or scanner pages. Tier:
deep dive.

**BUCKLEY-KARATZAS-1989** — J. D. Buckley and C. Karatzas, "Step and
scan: a systems overview of a new lithography tool", *Proc. SPIE*
**1088**, 424 (1989). <https://doi.org/10.1117/12.953171> The Micrascan I,
a 0.5 µm step-and-scan tool with catadioptric 4:1 optics and a
mercury-xenon lamp; the concept "enables very large field sizes and high
system productivity". Used on the i-line stepper or scanner page. Tier:
deep dive.

**SUWA-1988** — K. Suwa, K. Ushida and B. J. Lin, "The optical stepper
with a high numerical aperture i-line lens and a field-by-field leveling
system", *Proc. SPIE* **0922**, 270–276 (1988).
<https://doi.org/10.1117/12.968424> A high-NA i-line lens resolving
better than 0.65 µm and a field-by-field levelling system. Used on the
i-line stepper or scanner page. Tier: deep dive.

**KATZ-1990** — B. A. Katz, J. S. Greeneich, M. G. Bigelow, A. Katz, F. J.
van Hout and J. F. Coolsen, "High-numerical-aperture I-line stepper",
*Proc. SPIE* **1264**, 94 (1990). <https://doi.org/10.1117/12.20183> A
high-NA i-line stepper with phase grating alignment supporting 0.5 µm
without lens-heating effects, overlay below 100 nm and extension to
0.41 µm. Used on the i-line stepper or scanner page. Tier: deep dive.

**WITTEKOEK-1986** — S. Wittekoek, H. Linders, H. Stover, G. Johnson, D.
Gallagher and R. Fergusson, "Precision wafer-stepper alignment and
metrology using diffraction gratings and laser interferometry", *Proc.
SPIE* **0565**, 22 (1986). <https://doi.org/10.1117/12.949728> The ASM
Lithography stepper's grating alignment and interferometer metrology used
in machine assembly, test and matching. Used on the i-line stepper or
scanner page. Tier: deep dive.

**WISE-1992** — L. Wise, R. Mahany and L. Wang, "New ultra large field
submicron i-line stepper for advanced mix-and-match applications",
*ASMC '92 Proceedings*, pp. 75–78 (1992).
<https://doi.org/10.1109/ASMC.1992.253841> A 22 mm × 44 mm-field i-line
stepper of 0.8 µm production resolution for non-critical levels, with
cost-of-ownership models for mix-and-match lithography. Used on the
i-line stepper or scanner page. Tier: deep dive.

**PRASAD-2001** — K. J. Prasad et al., "W-CMP alignment using ASML's
ATHENA system on an I-line stepper", *Proc. SPIE* **4344**, 79 (2001).
<https://doi.org/10.1117/12.436730> Mark selection, alignment recipes and
long-term overlay of ATHENA alignment on i-line steppers over tungsten
CMP for a 0.35 µm device. Used on the i-line stepper or scanner page.
Tier: deep dive.

**DEMOOR-2004** — S. J. DeMoor, J. M. Brown, J. C. Robinson, S. Chang and
C. Tan, "Scanner overlay mix and match matrix generation: capturing all
sources of variation", *Proc. SPIE* **5375**, 66 (2004).
<https://doi.org/10.1117/12.534359> Mix-and-match overlay matrices between
exposure tools, combining lens distortion signatures with stepping and
scanning repeatability. Used on the i-line stepper or scanner page. Tier:
deep dive.

**CHU-1999** — R. Chu, C. Hsu and T. Hwang, "Characterizing lens
distortion to overlay accuracy by using fine measurement pattern",
*Proc. SPIE* **3677**, 83 (1999).
<https://doi.org/10.1117/12.350790> Fine-pattern overlay targets against
box-in-box targets; lens aberration causing over 15 nm of overlay
displacement. Used on the i-line stepper or scanner and CD-SEM and
overlay metrology pages. Tier: deep dive.

**NORTON-2000** — C. Norton, D. Marshall, M. Ameen, D. Whiteside, J.
Hallock and A. Becknell, "Photoresist properties during high current
implantation: an I-line vs. DUV resist comparison", *Proc. 2000
International Conference on Ion Implantation Technology*, pp. 813–816.
<https://doi.org/10.1109/IIT.2000.924278> DUV and i-line resists
compared under high-current, high-dose implants, the DUV resist found
equivalent. Used on the i-line stepper or scanner and coat/develop track
pages. Tier: deep dive.
Also used on the lithography materials material page.

**NAKAGAWA-1990** — K. Nakagawa, M. Taguchi and T. Ema, "Fabrication of
64 M DRAM with i-line phase-shift lithography", *IEDM Technical Digest*
1990, pp. 817–820. <https://doi.org/10.1109/IEDM.1990.237037> Phase-shift
lithography making 0.3 µm patterns with i-line exposure. Used on the
i-line stepper or scanner page. Tier: deep dive.

**ASML-PAS5500-350C** — ASML, *PAS 5500/350C* (Deep UV stepper),
refurbished systems data sheet, 2019.
<https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-350c.pdf>
A KrF stepper "for 0.15-µm applications and beyond": NA 0.40–0.63, 4×,
22.0 mm × 22.0 mm field, single-machine overlay ≤ 28 nm and matched ≤ 60
nm, 88 wafers per hour on 200 mm at 30 mJ/cm², a 10 W, 1 kHz Cymer 5610
laser with 20 m remote beam delivery, and mix-and-match with PAS 5500
i-line and DUV steppers. Used on the DUV (KrF, 248 nm) stepper or scanner
page. Tier: cross-check (vendor statement).

**ASML-PAS5500-750F** — ASML, *PAS 5500/750F DUV Step and Scan*,
refurbished systems data sheet, 2019.
<https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-750f.pdf>
A KrF scanner that "enables 130-nm mass production using mature 248-nm
KrF technology": NA 0.5–0.7, 26.0 mm × 33.0 mm field, CD uniformity
through focus, single-machine overlay ≤ 25 nm and matched ≤ 40 nm,
≥ 130 wafers per hour at 50 mJ/cm², a 20 W laser variable to 2 kHz,
TTL and ATHENA alignment, an 8-spot level sensor and commonality with
the i-line and 193 nm scanners. Used on the DUV (KrF, 248 nm) stepper or
scanner page. Tier: cross-check (vendor statement).

**ASML-PAS5500-850C** — ASML, *PAS 5500/850C DUV Step-and-Scan*,
refurbished systems data sheet, 2019.
<https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-850c.pdf>
A 248 nm scanner that "enables 110-nm mass production": NA 0.55–0.80,
26.0 mm × 33.0 mm field, single-machine overlay ≤ 15 nm and matched
≤ 25 nm, ≥ 135 wafers per hour, a 20 W Cymer ELS6610 laser with variable
laser frequency control. Used on the DUV (KrF, 248 nm) stepper or scanner
page. Tier: cross-check (vendor statement).

**CANON-FPA3030EX6** — Canon Inc., *FPA-3030EX6: KrF Stepper for IoT
devices*, product page.
<https://global.canon/en/product/indtech/semicon/fpa3030ex6.html> A
current KrF stepper for 100–200 mm wafers inheriting the FPA-3000EX6:
resolution ≤ 150 nm, NA 0.50–0.65, 1:5, 22 mm × 22 mm field, overlay
≤ 25 nm, 121 wafers per hour on 200 mm. Used on the DUV (KrF, 248 nm)
stepper or scanner page. Tier: cross-check (vendor statement).

**JAIN-1982** — K. Jain, C. G. Willson and B. J. Lin, "Ultrafast deep UV
lithography with excimer lasers", *IEEE Electron Device Letters* **3**(3),
53–55 (1982). <https://doi.org/10.1109/EDL.1982.25476> The first use of
pulsed excimer lasers (XeCl at 308 nm, KrF at 248 nm) for photolithography,
about two orders of magnitude faster than lamp exposure. Used on the DUV
(KrF, 248 nm) stepper or scanner page. Tier: deep dive.

**POL-1986** — V. Pol et al., "Excimer laser-based lithography: a deep
ultraviolet wafer stepper", *Proc. SPIE* **0633**, 6 (1986).
<https://doi.org/10.1117/12.963697> A commercial step-and-repeat tool
modified for 248 nm with an all-quartz 5× lens of NA 0.20–0.38 and a KrF
laser, giving 0.5 µm practical resolution. Used on the DUV (KrF, 248 nm)
stepper or scanner page. Tier: deep dive.

**TANIMOTO-1989** — A. Tanimoto, A. Miyaji, Y. Ichihara, T. Uemura and I.
Tanaka, "Excimer laser stepper for sub-half micron lithography", *Proc.
SPIE* **1088**, 434 (1989). <https://doi.org/10.1117/12.953172> A
flat-field excimer laser stepper with a narrow-band KrF laser, dose
control, off-axis He–Ne alignment and enhanced global alignment reaching
overlay better than 0.18 µm. Used on the DUV (KrF, 248 nm) stepper or
scanner page. Tier: deep dive.

**WITTEKOEK-1990** — S. Wittekoek, M. A. van den Brink, H. F. Linders, J.
M. D. Stoeldraijer, J. W. Martens and D. R. Ritchie, "Deep-UV wafer
stepper with through-the-lens wafer to reticle alignment", *Proc. SPIE*
**1264**, 534 (1990). <https://doi.org/10.1117/12.20207> A 248 nm stepper
with an all-quartz 5× lens of NA 0.42 and 21.2 mm field, 633 nm
through-the-lens alignment with correction optics, and laser wavelength
calibration. Used on the DUV (KrF, 248 nm) stepper or scanner page. Tier:
deep dive.

**DE-ZWART-1997** — G. de Zwart et al., "Performance of a step-and-scan
system for DUV lithography", *Proc. SPIE* **3051**, 817 (1997).
<https://doi.org/10.1117/12.276002> A 248 nm step-and-scan system exposing
26 mm × 33 mm fields with a variable 0.40–0.63 NA lens, with results on
dynamic distortion, focus, imaging, overlay and dose accuracy for sub
0.25 µm manufacturing. Used on the DUV (KrF, 248 nm) stepper or scanner
page. Tier: deep dive.

**DAS-2002** — P. Das and R. L. Sandstrom, "Advances in excimer laser
technology for sub-0.25-μm lithography", *Proceedings of the IEEE*
**90**(10), 1637–1652 (2002). <https://doi.org/10.1109/JPROC.2002.803665>
A review of excimer lasers as lithography sources at 248, 193 and 157 nm:
specifications, narrow spectral width, coherence and the advances made to
meet them. Used on the DUV (KrF, 248 nm) stepper or scanner page. Tier:
deep dive.
Also used on the lithography materials material page.

**LALOVIC-2001** — I. Lalovic, A. Kroyan, N. R. Farrar, D. Taitano, P.
Zambon and A. H. Smith, "Investigation of cross-field wavefront
aberrations of KrF lithography exposure systems as a function of excimer
laser bandwidth", *Proc. SPIE* **4346**, 1262 (2001).
<https://doi.org/10.1117/12.435655> Measured wavefront error against laser
bandwidth on a 0.6 NA KrF stepper and scanner. Used on the DUV (KrF,
248 nm) stepper or scanner page. Tier: deep dive.

**LAIDLER-2002** — D. W. Laidler, H. J. L. Megens, S. Lalbahadoersing,
R. J. F. van Haren and F. Bornebroek, "Advances in process overlay: ATHENA
alignment system performance on critical process layers", *Proc. SPIE*
**4689**, 397 (2002). <https://doi.org/10.1117/12.473478> ATHENA alignment
strategies and mark designs evaluated on shallow trench isolation,
tungsten CMP and copper dual-damascene levels. Used on the DUV (KrF,
248 nm) stepper or scanner page. Tier: deep dive.

**MACDONALD-1991** — S. A. MacDonald et al., "Airborne chemical
contamination of a chemically amplified resist", *Proc. SPIE* **1466**,
2–12 (1991).
<https://doi.org/10.1117/12.46354> Degradation of a t-BOC/onium salt
resist by parts-per-billion airborne organic bases, and its cure by
carbon-filtered air. Used on the DUV (KrF, 248 nm) stepper or scanner
and coat/develop track pages. Tier: deep dive.
Also used on the lithography materials material page.

**SCREEN-SK80EX** — SCREEN Semiconductor Solutions, *Coat/Develop Track:
SK-60EX/SK-80EX*, product page.
<https://www.screen.co.jp/spe/en/products/sk-60ex80ex> Coat/develop tracks
for 50–200 mm wafers "Continuing the Reliability of the Long-Selling 60/80
Series" with its large installed base, compatible with the recipes of
the 60/80 series. Used on the coat/develop track page. Tier: cross-check
(vendor statement).

**SCREEN-RF200EX** — SCREEN Semiconductor Solutions, *Coat/Develop Track:
RF-200EX/RF-300EX*, product page.
<https://www.screen.co.jp/spe/en/products/rf-200ex300ex> A current track
"Dedicated design for 200mm wafers" for DUV processes, redeploying 300 mm
unit technology, with reduced resist consumption. Used on the coat/develop
track page. Tier: cross-check (vendor statement).

**SOKUDO-RF3-2006** — Sokudo Co., Ltd. and JSR Micro, Inc., *JSR Micro,
Inc. Selects RF3 Track System from Sokudo Co., Ltd.*, press release,
2006-09-20, hosted by SCREEN (document PR060920E).
<https://www.screen.co.jp/eng/spe/mt-images/pr060920_e.pdf> The sale of
an RF3 coat/develop track of modular structure for 65 nm and 45 nm node
work; Sokudo as a joint venture of Dainippon Screen and Applied Materials
established on 2006-07-03. Used on the coat/develop track page. Tier:
cross-check (vendor statement).

**WIKI-SPIN-COATING** — Wikipedia, *Spin coating*.
<https://en.wikipedia.org/wiki/Spin_coating> Spin coating of photoresist
"about 1 micrometre thick" at 20 to 80 revolutions per second, the
dependence of thickness on speed and viscosity, and edge beads. Used on
the coat/develop track page. Tier: high-level.

**EMSLIE-1958** — A. G. Emslie, F. T. Bonner and L. G. Peck, "Flow of a
viscous liquid on a rotating disk", *Journal of Applied Physics*
**29**(5), 858–862 (1958). <https://doi.org/10.1063/1.1723300> The flow
equations of a Newtonian liquid on a rotating disk: an initially uniform
layer stays uniform and irregular layers level out under centrifugation.
Used on the coat/develop track page. Tier: deep dive.
Also used on the single-wafer spin processor machine page.

**MEYERHOFER-1978** — D. Meyerhofer, "Characteristics of resist films
produced by spinning", *Journal of Applied Physics* **49**(7), 3993–3997
(1978). <https://doi.org/10.1063/1.325357> A model of spun resist films
with evaporation: thickness independent of substrate size and scaling with
spin speed, viscosity and evaporation rate, checked on positive resists.
Used on the coat/develop track page. Tier: deep dive.

**SMITH-MACK-2001** — M. D. Smith and C. A. Mack, "Examination of a
simplified reaction-diffusion model for post-exposure bake of chemically
amplified resists", *Proc. SPIE* **4345**, 1022 (2001).
<https://doi.org/10.1117/12.436827> Coupled and decoupled
reaction–diffusion models of the post-exposure bake compared analytically.
Used on the coat/develop track page. Tier: deep dive.

**RAMANAN-2000** — N. Ramanan, A. Kozman and J. B. Sims, "Differences
between wafer and bake plate temperature uniformity in proximity bake: a
theoretical and experimental study", *Proc. SPIE* **3999**, 890 (2000).
<https://doi.org/10.1117/12.388375> Wafer temperature uniformity in
proximity bake as set by lid design, air flow, plate design and plate and
wafer flatness. Used on the coat/develop track page. Tier: deep dive.

**PERERA-1989** — T. Perera, "Characteristics of a developer for spray
puddle develop processes", *Proc. SPIE* **1086**, 470 (1989).
<https://doi.org/10.1117/12.953060> A surfactant-bearing developer for
spray-puddle develop, its sensitivities, exposure latitude and linewidth
uniformity. Used on the coat/develop track page. Tier: deep dive.
Also used on the lithography materials material page.

**ETO-2007** — H. Eto, Y. Ito and T. Homma, "Effect of temperature on
photoresist critical dimension during puddle development", *Japanese
Journal of Applied Physics* **46**(6R), 3354 (2007).
<https://doi.org/10.1143/JJAP.46.3354> Evaporative cooling of the wafer
edge during puddle develop and a DNQ/novolac CD change of about 5 nm/°C.
Used on the coat/develop track page. Tier: deep dive.

**FUJIWARA-2006** — T. Fujiwara, K. Shiraishi, H. Tanizaki, Y. Ishii, H.
Kyoda, T. Yamamoto and S. Ishida, "Wafer management between coat/developer
track and immersion lithography tool", *Proc. SPIE* **6154**, 61544L
(2006). <https://doi.org/10.1117/12.656303> Wafer handling between an
in-line coat/developer and an immersion scanner before the post-exposure
bake. Used on the coat/develop track page. Tier: deep dive.

**HITACHI-2011** — T. Ikegami, A. Yamaguchi, M. Tanaka, S. Takami, Y.
Hojo and A. Sugimoto, "Evolution and Future of Critical Dimension
Measurement System for Semiconductor Processes", *Hitachi Review*
**60**(5), 203–209 (2011).
<https://www.hitachihyoron.com/rev/pdf/2011/r2011_05_104.pdf> Hitachi's
CD-SEMs from the S-6000 of 1984 to the CG4100: design aims (in-lens
detection, low-energy beams, field-emission gun, recipes), pitch
calibration standards, and the resolution, repeatability, throughput and
wafer sizes of the S-6000, S-8820, S-9200 and CG4000. Used on the CD-SEM
and overlay metrology page. Tier: cross-check (vendor statement).
Also used on the lithography category page and the P1M, CTM1 and VIM step
pages.

**KLA-5200XP** — KLA-Tencor, *5200XP Overlay Metrology System*, product
page; Wayback Machine capture of 2001-08-07.
<https://web.archive.org/web/20010807104430/http://www.kla-tencor.com:80/products/semicon_process_para_ctrl/overlay/5200xp-overlay-met_sys.html>
Fully automated overlay measurement on product and test wafers for
0.18 µm technology, with coherence probe measurement optimised for
planarised layers. Used on the CD-SEM and overlay metrology page. Tier:
cross-check (vendor statement).

**CLASSONE-KLA5200XP** — ClassOne Equipment, *KLA-Tencor 5200XP Overlay
Registration System*, refurbished-equipment listing.
<https://www.classoneequipment.com/KLA-Tencor-5200XP-Overlay-Registration-System>
A 200 mm overlay and CD measurement system: non-contact box-in-box overlay
measurement, coherence probe microscopy, CD measurement recommended for
1.5 µm and above, and KLASS stepper set-up software. Used on the CD-SEM
and overlay metrology page. Tier: cross-check (reseller description).

**KLA-ARCHER10** — KLA-Tencor, *Archer 10: Automated Optical Overlay
Metrology*, product page; Wayback Machine capture of 2003-02-19.
<https://web.archive.org/web/20030219061753/http://www.kla-tencor.com:80/products/archer10/archer10.html>
An optical overlay tool for 300 mm manufacturing at the sub-0.13 µm node
with 30 % more throughput than its predecessors, low-contrast target
measurement, transfer of overlay data to ASML PAS 5500 steppers and
analysis for lot disposition and stepper correction. Used on the CD-SEM
and overlay metrology page. Tier: cross-check (vendor statement).

**AMAT-VERASEM-1999** — Applied Materials, *Applied Materials Introduces
New CD-SEM System for Sub-0.15 Micron Metrology*, press release,
1999-02-01.
<https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-new-cd-sem-system-sub-015-micron/>
The VeraSEM for 200 mm and 300 mm wafers: Process Variation Monitoring
(line edge roughness, line edge width variation, open and closed contact
holes), high throughput and system matching with shared libraries. Used
on the CD-SEM and overlay metrology page. Tier: cross-check (vendor
statement).

**AMAT-VERITYSEM-2004** — Applied Materials, *Applied Materials Shatters
Metrology Roadblocks for 65-45nm Production with Applied VeritySEM
System*, press release, 2004-02-23.
<https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-shatters-metrology-roadblocks-65-45nm>
The VeritySEM: less than 1.8 nm resolution at 200 eV, less than 0.5 nm
precision on ArF resist and gate features, and tool matching within 1 nm.
Used on the CD-SEM and overlay metrology page. Tier: cross-check (vendor
statement).

**KLA-ARCHER300-2010** — KLA-Tencor, *KLA-Tencor Launches the Archer(TM)
300 LCM Overlay Metrology System*, press release, 2010-06-22.
<https://ir.kla.com/news-events/press-releases/detail/269/kla-tencor-launches-the-archertm-300-lcm-overlay>
The Archer 300 LCM, successor of the Archer 200, with in-die overlay
measurement and upgrades from existing Archer tools. Used on the CD-SEM
and overlay metrology page. Tier: cross-check (vendor statement).

**WIKI-SEM** — Wikipedia, *Scanning electron microscope*.
<https://en.wikipedia.org/wiki/Scanning_electron_microscope>
Secondary-electron imaging, electron sources and specimen charging. Used
on the CD-SEM and overlay metrology page.
Also used on the defect and particle inspection and cross-section SEM and
profilers pages.
Tier: high-level.

**POSTEK-1994** — M. T. Postek, "Scanning electron microscope metrology",
*Proc. SPIE* **10274**, 1027405 (1994).
<https://doi.org/10.1117/12.187461> A review of SEM metrology of
submicrometre integrated-circuit structures and its recent improvements.
Used on the CD-SEM and overlay metrology page.
Also used on the cross-section SEM and profilers page.
Tier: high-level.

**ROSENFIELD-1986** — M. G. Rosenfield, "Linewidth measurement using the
low voltage SEM", *Proceedings, Annual Meeting, Electron Microscopy
Society of America* **44**, 652–653 (1986).
<https://doi.org/10.1017/S0424820100144681> Non-destructive linewidth
measurement in resist with the low-voltage SEM and the choice of
peak-to-peak or threshold edge methods. Used on the CD-SEM and overlay
metrology page. Tier: deep dive.

**SINGH-1988** — B. Singh and W. H. Arnold, "Linewidth measurement by low
voltage SEM", *Proc. SPIE* **0921**, 16 (1988).
<https://doi.org/10.1117/12.968347> Low-voltage SEM linewidths compared
with physical and electrical widths; the threshold method's sensitivity
to beam energy, diameter and defocus. Used on the CD-SEM and overlay
metrology page. Tier: deep dive.

**POSTEK-1988** — M. T. Postek, W. J. Keery and R. D. Larrabee, "The
relationship between accelerating voltage and electron detection modes to
linewidth measurement in an SEM", *Scanning* **10**(1), 10–18 (1988).
<https://doi.org/10.1002/sca.4950100104> How beam–specimen interaction and
detector type distort SEM linewidths, and why edge errors add in width
but cancel in pitch. Used on the CD-SEM and overlay metrology page. Tier:
deep dive.

**LOWNEY-1995** — J. R. Lowney, "Use of Monte Carlo modeling for
interpreting scanning electron microscope linewidth measurements",
*Scanning* **17**(5), 281–286 (1995).
<https://doi.org/10.1002/sca.4950170503> A Monte Carlo code for extracting
line edge positions from SEM signals. Used on the CD-SEM and overlay
metrology page. Tier: deep dive.

**SOLECKY-2002** — E. P. Solecky, J. Mayer and C. N. Archie, "Improving
sub-150-nm lithography and etch CD-SEM correlations to AFM and electrical
test", *Proc. SPIE* **4689**, 473 (2002).
<https://doi.org/10.1117/12.473486> CD-SEM waveforms and algorithm settings
at gate develop and etch, correlated with AFM and electrical
measurements. Used on the CD-SEM and overlay metrology page. Tier: deep
dive.

**YOU-2002** — T.-J. You, C.-K. Bok and K.-S. Shin, "CD metrology for
avoiding shrinkage of ArF resist patterns in 100 nm ArF lithography",
*Proc. SPIE* **4689**, 724 (2002). <https://doi.org/10.1117/12.473516>
Shrinkage of ArF resist lines under repeated SEM measurement and ways to
avoid it. Used on the CD-SEM and overlay metrology page. Tier: deep dive.

**MARSCHNER-2006** — T. Marschner et al., "Challenges and Methodology of
Fab-to-fab CD-SEM Matching", *17th Annual SEMI/IEEE ASMC* (2006), pp.
228–232. <https://doi.org/10.1109/ASMC.2006.1638758> Matching CD-SEMs in
fabs on different continents, correcting for changes to the matching
wafers in shipment. Used on the CD-SEM and overlay metrology page. Tier:
deep dive.

**DOCKREY-1989** — J. W. Dockrey and D. Hendricks, "The application of
coherence probe microscopy for submicron critical dimension linewidth
measurement", *Proc. SPIE* **1087**, 120 (1989).
<https://doi.org/10.1117/12.953086> Coherence probe imaging with a Linnik
interferometer and broadband illumination for linewidths, compared with
in-line SEM. Used on the CD-SEM and overlay metrology page. Tier: deep
dive.

**PLAMBECK-1995** — B. F. Plambeck, N. Knoll and P. J. Lord,
"Characterization of chemical-mechanical polished overlay targets using
coherence probe microscopy", *Proc. SPIE* **2439**, 298 (1995).
<https://doi.org/10.1117/12.209213> Overlay measurement on CMP-planarised
targets with coherence probe microscopy. Used on the CD-SEM and overlay
metrology page. Tier: deep dive.

**HOSHI-2002** — K. Hoshi, E. Kawamura, H. Morohoshi, H. Ina, T.
Fujimura, H. Kurita and J. L. Seligson, "TIS-WIS interaction
characterization on overlay measurement tool", *Proc. SPIE* **4689**, 715
(2002). <https://doi.org/10.1117/12.473514> Tool-induced shift calibration
and residual TIS on overlay metrology tools. Used on the CD-SEM and
overlay metrology page. Tier: deep dive.

**DEN-BOEF-2016** — A. J. den Boef, "Optical wafer metrology sensors for
process-robust CD and overlay control in semiconductor device
manufacturing", *Surface Topography: Metrology and Properties* **4**(2),
023001 (2016). <https://doi.org/10.1088/2051-672X/4/2/023001> A review of
level, alignment and scatterometry sensors in lithography. Used on the
CD-SEM and overlay metrology page. Tier: deep dive.

**DEMOOR-2000** — S. J. DeMoor, S. Hilbun, G. P. Beck III, K. L. Bushman,
R. D. Fields, R. M. Peters and T. E. Calvert, "Enhancing Overlay Metrology
Productivity and Stability Using an Off-line Recipe Database Manager",
*Yield Management Solutions* (KLA-Tencor), Summer 2000, pp. 44–48;
Wayback Machine capture of 2004-02-28.
<https://web.archive.org/web/20040228101521/http://www.kla-tencor.com:80/company/magazine/summer00/enhancing_overlay.pdf>
Recipe creation and management for overlay metrology in a high-volume
ASIC fab with many active reticles, using standard targets and an
off-line recipe database. Used on the CD-SEM and overlay metrology page.
Tier: deep dive.

#### CMP, clean and starting-material machine pages (first cited there)

The entries below were introduced by the starting-material, single-wafer
spin processor, CMP polisher and post-CMP cleaner pages, and are grouped
in that order by the page that first cited them. The vendor pages,
brochures, standards listings and press releases were fetched on
2026-09-13, those no longer served from the Wayback Machine capture
named in the entry; the papers were checked through Crossref and
OpenAlex on that date, and their annotations rest on their abstracts;
the patents were read on Google Patents (bibliographic data, abstract
and the passages quoted).

**KLA-SP1-2021** — KLA Corporation, *Surfscan® SP1TBI Pro / SP1DLS Pro:
Unpatterned Wafer Defect Inspection Systems*, brochure, rev. 1.0,
2021-05-25.
<https://www.kla.com/documents/products/brochures/Surfscan_SP1.pdf>
The SP1 scanner family as restarted for 150–300 mm wafers: oblique,
normal and brightfield-DIC illumination, haze maps, sensitivity "down to
60nm on the SP1 TBI and 50nm on the SP1 DLS on prime bare silicon",
"Industry standard for wafer qualification – wafer manufacturer OQC and
wafer fab IQC", "Industry standard for process tool qualification" and
"Onboard grading capability with up to 4 x 200mm load port sorting
stations". Used on the starting-material machine page. Tier:
cross-check (vendor statement).

**KLA-SP1DLS-2002** — KLA-Tencor, *Surfscan SP1 DLS: Unpatterned surface
inspection*, product page; Wayback Machine capture of 2002-02-08.
<https://web.archive.org/web/20020208135136/http://www.kla-tencor.com:80/products/defect_control/surfscan-sp1/surfscan.html>
The SP1 DLS with a backside inspection module, "enhanced sensitivity in
200 mm/300 mm wafer process qualification", continuity with the SP1 TBI,
and "tool-qualification and tool monitoring in 0.13 µm design rules and
below". Used on the starting-material machine page. Tier: cross-check
(vendor statement).
Also used on the defect and particle inspection page.

**THINKLASER-SIGMACLEAN** — Thinklaser USA, *SigmaClean: Debris-Free
100 - 200 mm Wafer Marking*, product page, accessed 2026-09-13.
<https://www.thinklaserusa.com/sigmaclean> A WaferMark soft-mark laser
marker for 100–200 mm wafers: "debris-free soft marking", SEMI T7, M12
and M13 compliance, marks "within a 25 mm band around the wafer's
circumference", dot depth "2.4 μm - 5 μm", "240 wph", a 1053 nm
diode-pumped Nd:YLF laser, and facilities (process vacuum, "Mark Point
Exhaust", static-charge limit). Used on the starting-material machine
page. Tier: cross-check (vendor statement).

**CAE-WAFERMARK-SUPERCLEAN** — Capital Asset Exchange (CAE), *GSI
LUMONICS WaferMark SuperClean Marking Machine*, used-equipment listing
no. 293743883, accessed 2026-09-13.
<https://caeonline.com/buy/marking-machines/gsi-lumonics-wafermark-superclean/293743883>
Listing of a "GSI LUMONICS WaferMark SuperClean", "Laser marking system,
8"", "1995 vintage"; only the model name, wafer size and vintage are
used, not the listing's generic description. Used on the
starting-material machine page. Tier: high-level (marketplace listing).

**WHS-T4** — Wafer Handling Systems, *2-Cassette automation sorter with
OCR (WHS-T4) 200 mm (8")*, product page, accessed 2026-09-13.
<https://www.waferhandlingsystems.com/product/2-cassette-automation-sorter-with-ocr-whs-t4-200-mm-8/287/>
A current 100–200 mm wafer sorter: tilt-stage load ports, linear robot,
notch/flat aligner, an ID reader "for OCR, barcode, or data matrix
recognition", sorting by wafer ID in 25-slot cassettes, SECS/GEM lot and
ID tracking and "up to 650 wafers per hour". Used on the
starting-material machine page. Tier: cross-check (vendor statement).

**SEMI-M12** — SEMI, *SEMI M12 — Specification for Serial Alphanumeric
Marking of Silicon Wafers*, SEMI Standards store listing, accessed
2026-09-13.
<https://store-us.semi.org/products/m01200-semi-m12-specification-for-serial-alphanumeric-marking-of-the-front-surface-of-wafers>
Scope of the standard: a coded alphanumeric mark that "links the
properties of the wafer stored in an appropriate database system to each
individual wafer", its geometric and spatial limits for flatted and
notched wafers, and consistency of marking "performed by silicon
manufacturers" that simplifies OCR equipment; marking
techniques are not addressed. Used on the starting-material machine
page. Tier: cross-check (standard).
Also used on the substrates material page.

**SEMI-M13** — SEMI, *SEMI M13 — Specification for Alphanumeric Marking
of Silicon Wafers*, SEMI Standards store listing, accessed 2026-09-13.
<https://store-us.semi.org/products/m01300-semi-m13-specification-for-alphanumeric-marking-of-silicon-wafers>
Scope of the standard: a mark coding "the origin, approximate
resistivity, dopant species, and crystal growth orientation in addition
to a wafer identification number" for marking "performed by silicon
manufacturers"; marking techniques are not addressed. Used on the
starting-material machine page. Tier: cross-check (standard).
Also used on the substrates material page.

**PAT-SOFTMARK-GSI** — B. Gu and J. S. Ehrmann (GSI Group), *Method and
system for laser soft marking*, US 7,705,268 B2, filed 2005-11-09,
granted 2010-04-27. <https://patents.google.com/patent/US7705268B2/en>
Soft and hard laser marks, the WaferMark as "believed to be the first
industrial laser marking system on silicon wafer", the "debris free"
Supersoftmark® of the Wafermark Sigma Clean and its narrow energy
window, and soft-mark depth set by pulse width. Used on the
starting-material machine page. Tier: deep dive.

**PAT-LASERMARK-WACKER** — F. Kuhn-Kuhnenfeld, J. Kramler and H.-A.
Gerber (Wacker Siltronic), *Method of making reference surface markings
on semiconductor wafers by laser beam*, US 4,522,656 A, filed
1984-04-26, granted 1985-06-11.
<https://patents.google.com/patent/US4522656A/en> "Contrast rich,
permanent and slag-free" marks made by irradiating 1.5 to 6.5 times the
mark area and melting the silicon only at the centre. Used on the
starting-material machine page. Tier: deep dive.

**PAT-SORTER-INFINEON** — D. Caspary and D. Kaulfuss (Infineon
Technologies), *Method and device for sorting wafers*, US 6,747,230 B2,
filed 2002-09-03, granted 2004-06-08.
<https://patents.google.com/patent/US6747230B2/en> Sorting wafers from
random slots into sequence by reading each wafer's information carrier.
Used on the starting-material machine page. Tier: deep dive.

**LIU-1993** — B. Y. H. Liu, S.-K. Chae and G.-N. Bae, "Sizing Accuracy,
Counting Efficiency, Lower Detection Limit and Repeatability of a Wafer
Surface Scanner for Ideal and Real‐World Particles", *Journal of The
Electrochemical Society* **140**(5), 1403–1409 (1993).
<https://doi.org/10.1149/1.2221569> A Tencor Surfscan 4000 evaluated
with PSL spheres and real Si and SiO₂ particles, with scattering
calculations; Si particles detected well below the PSL-based limit. Used
on the starting-material machine page. Tier: deep dive.

**HUFF-1997** — H. R. Huff et al., "Measurement of Silicon Particles by
Laser Surface Scanning and Angle‐Resolved Light Scattering", *Journal of
The Electrochemical Society* **144**(1), 243–250 (1997).
<https://doi.org/10.1149/1.1837392> A SEMATECH task force on false counts
from haze, the mis-sizing of silicon particles by PSL-calibrated
scanners, and angle-resolved scattering. Used on the starting-material
machine page. Tier: deep dive.

**SCHEER-1996** — B. W. Scheer, "Development of a physical haze and
microroughness standard", *Proc. SPIE* **2862**, 78–95 (1996).
<https://doi.org/10.1117/12.256193> Haze masking particle detection, the
instrument dependence of roughness, and a lithographically etched haze
standard on 150 mm wafers. Used on the starting-material machine page.
Tier: deep dive.
Also used on the defect and particle inspection page.

**ISHII-1996** — H. Ishii, S. Shiratake, K. Oka, K. Motonami, T. Koyama
and J. Izumitani, "Direct Observation of Crystal-Originated Particles on
Czochralski-Grown Silicon Wafer Surface and Effect on Gate Oxide
Reliability", *Japanese Journal of Applied Physics* **35**(11A), L1385
(1996). <https://doi.org/10.1143/JJAP.35.L1385> Single and pair COP pits
and their effect on the TDDB of about 10 nm gate oxides. Used on the
starting-material machine page. Tier: deep dive.
Also used on the substrates material page.

**MIYAZAKI-1997** — M. Miyazaki, S. Miyazaki, T. Kitamura, Y. Yanase, T.
Ochiai and H. Tsuya, "Influence of Crystal-Originated 'Particle'
Microstructure on Silicon Wafers on Gate Oxide Integrity", *Japanese
Journal of Applied Physics* **36**(10R), 6187 (1997).
<https://doi.org/10.1143/JJAP.36.6187> COPs as the main cause of GOI
failure, their shape after SC-1, anneal and repolish, and the octahedral
void behind them. Used on the starting-material machine page. Tier: deep
dive.
Also used on the substrates material page.

**CHRIST-1983** — M. H. Christ and B. S. Maurantonio, "Influence of Laser
Marking on Silicon Wafer Properties", in *Silicon Processing*, ASTM STP
804, ASTM International, 1983, pp. 62–82.
<https://doi.org/10.1520/STP36160S> Dislocations and slip near unetched
laser marks after oxidation, slag around dot-matrix marks, and its effect
on epitaxial growth. Used on the starting-material machine page. Tier:
deep dive.

**KHOONG-2010** — L. E. Khoong, Y. C. Lam, H. Y. Zheng and X. Chen,
"Laser soft marking on silicon wafer", *Journal of Applied Physics*
**107**(5), 053107 (2010). <https://doi.org/10.1063/1.3319611> Soft marks
invisible except under condensation, explained by a thin, poorly
conducting polycrystalline surface layer. Used on the starting-material
machine page. Tier: deep dive.

**SEZ-8200-2001** — SEZ Group, *First Double Sided Single Wafer
Spin-Processor Available for Cleaning Applications*, press release,
2001-01-31; Wayback Machine capture of 2008-11-20.
<https://web.archive.org/web/20081120145130/http://www.sez.com/31_Jan_01__First_Double_Sided_Single_Wafer_Spin_Processor_Available_for_Cleaning_Applications.SEZ>
The four-chamber Spin-Processor 8200, based on the 4200, as "the first
non-contact, single wafer, double sided cleaner", with up to 200 wafers
per hour, spin-off that "eliminates redeposition and cross-contamination",
and SEZ's headquarters in Villach. Used on the single-wafer spin
processor machine page. Tier: cross-check (vendor statement).

**SEZ-DAVINCI-2008** — SEZ Group, *Da Vinci*, product page; Wayback
Machine capture of 2008-03-22.
<https://web.archive.org/web/20080322001425/http://www.sez.com:80/Da_Vinci.SEZ>
The Da Vinci single-wafer platform for BEOL polymer cleaning and backside
etch and clean on 200 mm and 300 mm wafers, "Originally developed to
address 90-nm technology nodes", with double-sided processing and
separated rinse and chemical chambers. Used on the single-wafer spin
processor machine page. Tier: cross-check (vendor statement).
Also used on the post-CMP cleaner machine page.

**SEZ-LAM-2007** — SEZ Group, *SEZ Holding Welcomes Planned Acquisition
by Lam Research*, press release, 2007-12-11; Wayback Machine capture of
2007-12-13.
<https://web.archive.org/web/20071213223543/http://www.sez.com:80/11_Dec_07__SEZ_Holding_Welcomes_Planned_Acquisition_by_Lam_Research.SEZ>
The agreement for a Lam Research tender offer for SEZ, SEZ to become a
Lam division for single-wafer cleaning, and SEZ's "installed base of over
1,200 tools". Used on the single-wafer spin processor machine page.
Tier: cross-check (vendor statement).

**SEZ-POLYMER-1999** — E. Gaulhofer, H. Kruwinus (SEZ), G. Goebel, E.
Finson and T. Maw (EKC), "Single-Wafer Polymer Removal for 0.18-micron to
0.25-micron Technology", *European Semiconductor*, April 1999; reprint on
the SEZ website, Wayback Machine capture of 2006-01-17.
<https://web.archive.org/web/20060117001812/http://www.sez.com:80/NR/rdonlyres/e3nsv7jtmjelajokwc2pivxpcigbahrzmpkjqmcqjbeiv4nzvl7qlr3sxhl7otzjxbrsdw6tls4y3ubhoiijpiwz2qb/polymer_removal_0499.pdf>
How a single-wafer spin processor dispenses, spins off, rinses and dries;
post-etch residue removal with room-temperature semi-aqueous EKC removers
on 200 mm wafers (10–120 s, 400–800 rpm, 0.8–2.0 l/min) after a Lam
TCP9600 metal etch; chemical and water use per wafer; the four-chamber
SEZ 4200. Used on the single-wafer spin processor machine page. Tier:
high-level (vendor application article).

**KINOSHITA-SEZ** — K. Kinoshita (SEZ application department, Sumitomo
Electronics), *Post-CMP Cleaning Technique by SEZ: Cleaning of Backside
by Wet Etching*, application article, undated; SEZ website, Wayback
Machine capture of 2006-01-17.
<https://web.archive.org/web/20060117013206/http://www.sez.com:80/NR/rdonlyres/e7enpr5qqh5rriqc5rsb2wuafgjsrvoycez2ufodmguu27gfnn2xqfmf4al2ukmo7cfqmdm5dwfkx3lfnkizldcy2nb/postcmp.pdf>
Backside particles after CMP and lithography focus; compounds between
backside films and metals that brush and megasonic cleaning do not
remove; backside wet etching on a chemical spin etcher that "requires no
protection for the device surface"; slurry and metal removal examples.
Used on the single-wafer spin processor machine page. Tier: high-level
(vendor application article).
Also used on the post-CMP cleaner machine page.

**SCREEN-SP2100** — SCREEN Semiconductor Solutions, *SCREEN Launches New
Spin Processor for Single Wafer Cleaning*, news release, 2020-06-25.
<https://www.screen.co.jp/spe/en/information/spe200625> The SP-2100 spin
processor for wafers up to 200 mm, with an optional metal-etch
configuration, a built-in chemical cabinet and a selectable number of
chambers. Used on the single-wafer spin processor machine page. Tier:
cross-check (vendor statement).

**FRAUNHOFER-DSP** — Fraunhofer Institute for Microengineering and
Microsystems IMM, *DSP Cleaning Agent Online Monitoring System*, product
sheet, accessed 2026-09-13.
<https://www.imm.fraunhofer.de/content/dam/imm/de/documents/PDFs-neu2018/A-und-S/IMM-DSP_Cleaning_Agent_Online_Monitoring_System%20.pdf>
DSP as "3.7 wt% hydrogen peroxide (H2O2) and 8.5 wt% sulfuric acid
(H2SO4)", DSP+ with 150 or 300 ppm HF as a replacement for SPM on
post-etch residues, and optical in-line monitoring of the two
concentrations. Used on the single-wafer spin processor machine page.
Tier: cross-check (research institute statement).

**PAT-SPIN-SEZ** — F. Sumnitsch (SEZ), *Support for slice-shaped articles
and device for etching silicon wafers with such a support*, US 4,903,717
A, filed 1988-11-09, granted 1990-02-27 (assigned to SEZ; current
assignee listed as Lam Research AG).
<https://patents.google.com/patent/US4903717A/en> A wafer support with
an annular gas nozzle whose gas cushion keeps treatment fluid off the
underside, inside an annular tank with ducts at several levels for
collecting fluids. Used on the single-wafer spin processor machine page.
Tier: deep dive.

**HATTORI-1998** — T. Hattori, T. Osaka, A. Okamoto, K. Saga and H.
Kuniyasu, "Contamination Removal by Single‐Wafer Spin Cleaning with
Repetitive Use of Ozonized Water and Dilute HF", *Journal of The
Electrochemical Society* **145**(9), 3278–3284 (1998).
<https://doi.org/10.1149/1.1838798> Room-temperature spin cleaning with
alternating 10 s doses of ozonised water and dilute HF. Used on the
single-wafer spin processor machine page. Tier: deep dive.
Also used on the wet chemicals material page.

**HATTORI-2007** — T. Hattori, H. Hirano, T. Osaka and H. Kuniyasu,
"Environmentally Benign Single-Wafer Spin Cleaning Using Ultra-Diluted
HF/Nitrogen Jet Spray Without Causing Structural Damage and Material
Loss", *IEEE Transactions on Semiconductor Manufacturing* **20**(3),
252–258 (2007). <https://doi.org/10.1109/TSM.2007.901845> A 20 s
ultra-dilute HF and nitrogen spray clean with negligible silicon and
oxide loss. Used on the single-wafer spin processor machine page. Tier:
deep dive.

**OINOUE-2018** — T. Oinoue, S. Saito, A. Okuyama, Y. Hagimoto and H.
Iwamoto, "Behavior Analysis of Si Etching Process with HF/HNO3 Mixture in
Single-Spin Wafer Process", *Solid State Phenomena* **282**, 83–87 (2018).
<https://doi.org/10.4028/www.scientific.net/SSP.282.83> Radial etch-rate
distributions of silicon and oxide in HF/HNO₃ on a spinning wafer,
explained by chemical consumption. Used on the single-wafer spin
processor machine page. Tier: deep dive.

**LEE-2012-DSP** — H. H. Lee, M. S. Yun, H. W. Lee and J. G. Park,
"Removing W Polymer Residue from BEOL Structures Using DSP+ (Dilute
Sulfuric-Peroxide-HF) Mixture – A Case Study", *Solid State Phenomena*
**195**, 128–131 (2012).
<https://doi.org/10.4028/www.scientific.net/SSP.195.128> DSP+ as the
replacement for SPM in removing post-etch metal and polymer residues.
Used on the single-wafer spin processor machine page. Tier: deep dive.

**MUI-2011** — D. Mui, E. H. Lenz, C. Cyterski, K. Venkataraman and M.
Kawaguchi, "Wafer Surface Charging Model for Single-Wafer Wet-Spin
Processes", *IEEE Transactions on Semiconductor Manufacturing* **24**(4),
552–558 (2011). <https://doi.org/10.1109/TSM.2011.2162346> Surface
charging in a single-wafer wet spin tool modelled as charge advection by
the liquid's shear flow. Used on the single-wafer spin processor machine
page. Tier: deep dive.

**AMAT-MIRRA-500-2000** — Applied Materials, *Applied Materials Ships
500th Mirra CMP System; Success of the Mirra System Ranks Applied
Materials as the World's Leading Supplier of CMP Systems*, press release,
2000-02-22.
<https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-ships-500th-mirra-cmp-system-success-mirra/>
The 500th Mirra, "the industry's largest installed base of multi-platen
CMP tools", introduced in December 1995, with Mesa cleaning and film
metrology added and the Mirra Mesa introduced in 1999. Used on the CMP
polisher machine page. Tier: cross-check (vendor statement).

**AMAT-MESA-1999** — Applied Materials, *Applied Materials Announces New
Mirra Mesa System to Address Market Demand for Integrated CMP Solutions*,
press release, 1999-06-10.
<https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-new-mirra-mesa-system-address-market>
The Mirra Mesa, polishing and cleaning on one dry-in/dry-out system; the
Mesa cleaner's megasonic module, two double-sided brush scrubber stations
and spin rinse dryer, vertical edge-gripped wafers, on-board chemical
mixing, HF in the brush modules and heated RCA chemistries in the
megasonic module. Used on the CMP polisher machine page. Tier:
cross-check (vendor statement).
Also used on the post-CMP cleaner machine page, the CMP category page and
the CMPP, WCMPLI and CMPL step pages.
Also used on the CMP consumables material page.

**IPEC-472-1997** — IPEC-Planar, *AVANTI 472*, product page; Wayback
Machine capture of 1997-06-26.
<https://web.archive.org/web/19970626104141/http://www.ipec.com:80/planar/472.html>
IPEC-Planar's third-generation polisher: single-wafer, two-step polishing
for wafers up to 200 mm, oxide and metal processes, APP1000 pad profiling,
slurries of pH 2–12, slurry pumps to 1000 ml/min, platen temperature
control and a two-platen buff. Used on the CMP polisher machine page.
Tier: cross-check (vendor statement).
Also used on the CMP consumables material page.

**IPEC-676-1997** — IPEC-Planar, *IPEC AvantGaard 676 Highlights*,
product page; Wayback Machine capture of 1997-06-26.
<https://web.archive.org/web/19970626104827/http://www.ipec.com:80/planar/676-spec.html>
Feature list of the AvantGaard 676: four polishing modules, integrated
post-CMP spray-box cleaning, through-the-pad slurry delivery and endpoint
capability. Used on the CMP polisher machine page. Tier: cross-check
(vendor statement).
Also used on the post-CMP cleaner machine page.

**SPEEDFAM-IPEC-2001** — SpeedFam-IPEC CMP Group, *Products* (Momentum,
Auriga, AvantGaard), product page; Wayback Machine capture of 2001-04-12.
<https://web.archive.org/web/20010412141846/http://www.ipec.com:80/cmp/products.htm>
The Momentum (orbital and rotational heritage, four platens, zonal
carrier, integrated metrology with predictive process adjustment,
integrated cleaner) for 0.18 µm and 0.13 µm; the Auriga family with
optical endpoint, dual-station box cleaner, PVA brush boxes, megasonic
option and spin rinse dryer; the AvantGaard 676 with "a unique orbital
polishing technique" and "Endpoint detection capability -- motor current
or optical"; the AvantGaard 776. Used on the CMP polisher machine page.
Tier: cross-check (vendor statement).
Also used on the post-CMP cleaner machine page.
Also used on step 090.

**STRASBAUGH-6DS-1999** — Strasbaugh, *The 6DS-SP Series Planarizers*,
product page; Wayback Machine capture of 1999-02-10.
<https://web.archive.org/web/19990210100559/http://www.strasbaugh.com:80/cmp1.htm>
A dual-spindle production polisher processing two wafers at once, with
polish force to 500 lb, integrated cleaning options and optional dual
tables, post-CMP scrubber and on-line thickness measurement. Used on the
CMP polisher machine page. Tier: cross-check (vendor statement).
Also used on the post-CMP cleaner machine page.

**STRASBAUGH-6EC-1999** — Strasbaugh, *The Model 6EC Laboratory
Planarizer*, product page; Wayback Machine capture of 1999-02-10.
<https://web.archive.org/web/19990210113246/http://www.strasbaugh.com:80/cmp2.htm>
The 6EC as a semi-automatic "Laboratory Planarizer" for CMP research and
small-quantity production, sharing carriers and conditioner with the
production tool. Used on the CMP polisher machine page. Tier: cross-check
(vendor statement).

**LAM-INTEGRA-1999** — Lam Research, *Lam Research Corporation Ships
100th Synergy Integra Integrated CMP Cleaning System*, press release,
1999-06-17.
<https://newsroom.lamresearch.com/1999-06-17-Lam-Research-Corporation-Ships-100th-Synergy-IntegraTM-Integrated-CMP-Cleaning-System>
The Synergy Integra (introduced 1997) combining polisher and cleaner on
one platform to avoid slurry drying on the wafer, integrated with six
polisher suppliers including Lam's Teres; chemical mechanical cleaning
technology; more than 750 OnTrak cleaners installed. Used on the CMP
polisher machine page. Tier: cross-check (vendor statement).
Also used on the post-CMP cleaner machine page.

**LAM-CLEAN-1000-2001** — Lam Research, *Lam Research Ships 1,000th
Post-CMP Clean System To Philips*, press release, 2001-02-14.
<https://investor.lamresearch.com/2001-02-14-Lam-Research-Ships-1,000th-Post-CMP-Clean-System-To-Philips>
A Synergy Integra on a Teres polisher for post-CMP clean after
direct-polish STI; all Synergy Integra systems use double-sided scrubbing
and chemical mechanical cleaning, with an open architecture for other
polishers. Used on the CMP polisher machine page. Tier: cross-check
(vendor statement).
Also used on the post-CMP cleaner machine page.

**PAT-CARRIER-AMAT** — S. M. Zuniga, M. Birang, H. Chen and S.-H. Ko
(Applied Materials), *Carrier head with a flexible membrane for a
chemical mechanical polishing system*, US 6,183,354 B1, filed 1997-05-21,
granted 2001-02-06. <https://patents.google.com/patent/US6183354B1/en>
Why a non-uniform carrier load gives non-uniform removal, and a carrier
head with a flexure-mounted flexible membrane, gimbal and retaining ring.
Used on the CMP polisher machine page. Tier: deep dive.
Also used on the CMP consumables material page.

**PAT-LINEAR-LAM** — A. K. Pant, D. W. Young, G. Travis, K. Volodarsky,
A. Nagengast et al. (Lam Research), *Polishing head for chemical
mechanical polishing using linear planarization technology*, US 6,425,812
B1, filed 1999-12-30, granted 2002-07-30.
<https://patents.google.com/patent/US6425812B1/en> Rotary and linear
polishers compared, the Teres as the example of a linear belt polisher
with a fluid platen, and a diaphragm head that limits horizontal carrier
movement. Used on the CMP polisher machine page. Tier: deep dive.

**KWON-2013** — T.-Y. Kwon, M. Ramachandran and J.-G. Park, "Scratch
formation and its mechanism in chemical mechanical planarization (CMP)",
*Friction* **1**(4), 279–305 (2013).
<https://doi.org/10.1007/s40544-013-0026-y> A review of scratch formation
against process conditions and consumables, scratch inspection, and
filtration and water-jet spraying to reduce scratches. Used on the CMP
polisher machine page. Tier: deep dive.
Also used on the CMP consumables material page.

**OLLENDORF-2004** — H. Ollendorf, S. Cabral and R. Fuller, "Reduction of
CMP μ-scratch induced metal shorts by introduction of a post CMP tungsten
plasma clean process in a high volume DRAM manufacturing environment",
*2004 IEEE/SEMI Advanced Semiconductor Manufacturing Conference and
Workshop*, pp. 1–4. <https://doi.org/10.1109/ASMC.2004.1309523>
Tungsten-filled microscratches from tungsten CMP shorting lines, removed
by a plasma etch after the polish. Used on the CMP polisher machine page.
Tier: deep dive.
Also used on the post-CMP cleaner machine page.
Also used on the CMP consumables material page.

**SCREEN-SS3200** — SCREEN Semiconductor Solutions, *Launch of 200mm
Wafer Cleaning System — New SS-3200 for 200mm expands SCREEN SPE's
world-leading spin scrubber lineup*, news release, 2024-11-06.
<https://www.screen.co.jp/spe/en/information/spe241106> A 200 mm spin
scrubber, "Method in which wafers are physically cleaned using soft
brushes and DI water", with throughput up to 500 wafers per hour and
lower DI water use per wafer. Used on the post-CMP cleaner machine page.
Tier: cross-check (vendor statement).
Also used on the ultrapure water material page.

**PAT-SCRUBBER-ONTRAK** — R. A. Lutz (OnTrak Systems), *Double-sided
wafer scrubber with a wet submersing silicon wafer indexer*, US 5,442,828
A, filed 1992-11-30, granted 1995-08-22.
<https://patents.google.com/patent/US5442828A/en> The DSS-200 and DSS-150
double-sided scrubbers for bare-silicon and post-CMP cleaning; why slurry
must not dry; brush stations with hollow-core, water-flushed nylon or PVA
brushes; a spin-dry station; a wet indexer that keeps wafers submerged.
Used on the post-CMP cleaner machine page. Tier: deep dive.
Also used on the CMP consumables material page.
Also used on the ultrapure water material page.

**PAT-MEGASONIC-RCA** — A. Mayer and S. Shwartzman (RCA), *Megasonic
cleaning system*, US 3,893,869 A, granted 1975-07-08.
<https://patents.google.com/patent/US3893869A/en> A cleaning, rinsing and
drying system with a transducer at about 0.2–5 MHz propagating sound
parallel to the wafer surfaces. Used on the post-CMP cleaner machine
page. Tier: deep dive.

**BUSNAINA-1995** — A. A. Busnaina, I. I. Kashkoush and G. W. Gale, "An
Experimental Study of Megasonic Cleaning of Silicon Wafers", *Journal of
The Electrochemical Society* **142**(8), 2812–2817 (1995).
<https://doi.org/10.1149/1.2050096> Megasonic removal of PSL, SiO₂ and
Si₃N₄ particles at 862 kHz in DI water and SC-1 against time, particle
size and power. Used on the post-CMP cleaner machine page. Tier: deep
dive.
Also used on the ultrapure water material page.

**GALE-1999** — G. W. Gale and A. A. Busnaina, "Roles of cavitation and
acoustic streaming in megasonic cleaning", *Particulate Science and
Technology* **17**(3), 229–238 (1999).
<https://doi.org/10.1080/02726359908906815> Mechanisms of megasonic
particle removal and the effects of frequency, temperature and power
density. Used on the post-CMP cleaner machine page. Tier: deep dive.

**ZHANG-BUSNAINA-1999** — F. Zhang, A. A. Busnaina and G. Ahmadi,
"Particle Adhesion and Removal in Chemical Mechanical Polishing and
Post‐CMP Cleaning", *Journal of The Electrochemical Society* **146**(7),
2665–2669 (1999). <https://doi.org/10.1149/1.1391989> A model of particle
penetration during CMP and of particle removal by rolling in final
polishing and brush cleaning. Used on the post-CMP cleaner machine page.
Tier: deep dive.

**ZHANG-RAGHAVAN-1999** — L. Zhang, S. Raghavan and M. Weling,
"Minimization of chemical-mechanical planarization (CMP) defects and
post-CMP cleaning", *Journal of Vacuum Science & Technology B* **17**(5),
2248–2255 (1999). <https://doi.org/10.1116/1.590901> A review of CMP
contamination (particulate, metallic, organic), slurry additives and
approaches to post-CMP cleaning. Used on the post-CMP cleaner machine
page. Tier: deep dive.
Also used on the CMP consumables material page.

**BUSNAINA-2002** — A. A. Busnaina, H. Lin, N. Moumen, J.-W. Feng and J.
Taylor, "Particle adhesion and removal mechanisms in post-CMP cleaning
processes", *IEEE Transactions on Semiconductor Manufacturing* **15**(4),
374–382 (2002). <https://doi.org/10.1109/TSM.2002.804872> Particle
adhesion strengthened by chemical reaction with moisture and ageing, and
brush contact, pressure and time in particle removal. Used on the
post-CMP cleaner machine page. Tier: deep dive.

**XU-2004** — K. Xu, R. Vos, G. Vereecke, G. Doumen, W. Fyen, P. W.
Mertens, M. M. Heyns, C. Vinckier and J. Fransaer, "Particle adhesion and
removal mechanisms during brush scrubber cleaning", *Journal of Vacuum
Science & Technology B* **22**(6), 2844–2852 (2004).
<https://doi.org/10.1116/1.1815319> Force analysis and experiments on
34 nm silica particles: rolling, not lifting, removes them, in a
hydrodynamic lubrication regime. Used on the post-CMP cleaner machine
page. Tier: deep dive.
Also used on the CMP consumables material page.

**GE-2006** — D.-W. Ge, B.-C. Qiu, L.-R. Chen, F.-Y. He, J.-N. Liu,
C.-X. Zhi and X. Cheng, "Optimizing post cleaning of Tungsten contact CMP
to improve the yield of logic products with copper interconnect", *2006
8th International Conference on Solid-State and Integrated Circuit
Technology (ICSICT)*, pp. 351–353.
<https://doi.org/10.1109/ICSICT.2006.306249> Organic particles from a
post-tungsten-contact-CMP brush station with HF spray causing metal-1
bridges in sub-130 nm logic, and the brush and megasonic changes that
reduced them. Used on the post-CMP cleaner machine page. Tier: deep dive.
Also used on the CMP consumables material page.

#### Metrology and test machine pages (first cited there)

The entries below were introduced by the defect and particle inspection,
film thickness and stress metrology, sheet-resistance and dose metrology,
cross-section SEM and profilers, and parametric tester and prober pages,
and are grouped in that order by the page that first cited them. The
vendor pages, press releases and data sheets were fetched on 2026-09-13,
most of them from the Wayback Machine capture named in the entry; the
papers were checked through Crossref and OpenAlex on that date, and their
annotations rest on their abstracts; the patents were checked through
Google Patents (bibliographic data and abstract).

**TENCOR-SP1-1996** — Tencor Instruments, *Tencor Instruments Introduces
Revolutionary 300mm Wafer Inspection System* (Surfscan SP1), press release,
1996-06-17; Wayback Machine capture of 1997-03-02.
<https://web.archive.org/web/19970302033839/http://www.tencor.com:80/press/SP1EMBG.html>
Tencor's announcement of the Surfscan SP1, dated "JUNE 17, 1996": a
stationary beam with axi-symmetric collection on a rotating wafer, an
optional bright-field channel, detection "down to 0.08 micron" and up to
100 wafers per hour on 300 mm (150 on 200 mm). Used on the defect and
particle inspection page. Tier: cross-check (vendor statement).

**TENCOR-SP1-WP** — Tencor Instruments, *Surfscan SP1: New Inspection
Technology for Unpatterned 300mm Wafers*, technology white paper, web
page; Wayback Machine capture of 1997-03-02.
<https://web.archive.org/web/19970302034319/http://www.tencor.com:80/products/SP1WhitePaper.html>
Describes laser-scattering inspection ("a laser illuminates the wafer
surface, and light scattered by contaminants and other surface
irregularities is collected by specially positioned collection optics"),
detection "down to 0.08 micron", haze measurement "down to a few parts per
billion" and 150 wafers per hour on 200 mm (100 on 300 mm). Used on the
defect and particle inspection page. Tier: cross-check (vendor statement).

**TENCOR-SP1-TECH** — Tencor Instruments, *Technical Details of the
Surfscan SP1 Unpatterned Wafer Inspection System*, web page; Wayback
Machine capture of 1997-03-02.
<https://web.archive.org/web/19970302034311/http://www.tencor.com:80/products/SP1TechDetails.html>
The stationary illumination beam with a rotating and translating wafer,
axi-symmetric dark-field collection independent of defect orientation, and
an optional Nomarski bright-field channel for mounds and dimples. Used on
the defect and particle inspection page. Tier: cross-check (vendor
statement).

**TENCOR-UNPATTERNED-1997** — Tencor Instruments, *Unpatterned Wafer
Inspection* (Surfscan SP1, 6420 and 6220), product page; Wayback Machine
capture of 1997-03-02.
<https://web.archive.org/web/19970302033400/http://www.tencor.com:80/products/uwaferinpection.html>
The Surfscan 6220 for bare and smooth blanket-film wafers and haze, "down
to 0.09 micron on well-polished silicon", and the 6420 for metal films,
rough surfaces and CMP applications, "down to 0.1 micron on polished
silicon". Used on the defect and particle inspection page. Tier:
cross-check (vendor statement).

**TENCOR-PATTERNED-1997** — Tencor Instruments, *Patterned Wafer
Inspection* (Surfscan AIT and 7700), product page; Wayback Machine capture
of 1997-03-02.
<https://web.archive.org/web/19970302033408/http://www.tencor.com:80/products/pwaferinpection.html>
The Surfscan AIT (30 full-wafer inspections per hour, "Ideal for
after-etch and post-CMP inspection levels") and the Surfscan 7700 (optimal
sensitivity 0.15 µm, contaminants below 0.20 µm on nitride, oxide and TEOS
levels, and a microscope review option). Used on the defect and particle inspection page. Tier:
cross-check (vendor statement).

**TENCOR-AIT-1995** — Tencor Instruments, *Tencor Instruments Unveils
Surfscan AIT Wafer Inspection System*, press release, 1995-10-23; Wayback
Machine capture of 1997-03-02.
<https://web.archive.org/web/19970302034359/http://www.tencor.com:80/press/surfscan.html>
Introduces the Surfscan AIT as the first high-speed in-line inspector for
both pattern defects and particles, developed with SEMATECH for 0.25 µm
technology, building on Tencor's laser-scattering tools. Used on the
defect and particle inspection page. Tier: cross-check (vendor statement).

**TENCOR-CRS-1997** — Tencor Instruments, *Laser Confocal Review* (Tencor
CRS), product page; Wayback Machine capture of 1997-03-02.
<https://web.archive.org/web/19970302033431/http://www.tencor.com:80/products/lasercreview.html>
A review station for defects found by automatic inspection, resolving
features "as small as 0.15 micron" and placing defects under, within or on
top of a film. Used on the defect and particle inspection page. Tier:
cross-check (vendor statement).

**TENCOR-ADC-1996** — Tencor Instruments, *Tencor Instruments Introduces
Automatic Defect Classification (ADC) for its Tencor CRS Laser Confocal
Review Station*, press release, 1996-07-16; Wayback Machine capture of
1997-03-02.
<https://web.archive.org/web/19970302033828/http://www.tencor.com:80/press/ADCrelease.html>
An ADC module for the CRS-1010 that automates defect relocation and
classification and allows expanded sampling plans. Used on the defect and
particle inspection page. Tier: cross-check (vendor statement).

**TENCOR-DEFECTDATA-1997** — Tencor Instruments, *Defect Data Analysis*
(SwiftAccess), product page; Wayback Machine capture of 1997-03-02.
<https://web.archive.org/web/19970302033417/http://www.tencor.com:80/products/defectdata.html>
A fab-wide defect database whose control charts can be shown on the
Surfscan AIT. Used on the defect and particle inspection page. Tier:
cross-check (vendor statement).

**KLA-AITXP** — KLA-Tencor, *AIT XP: High-throughput scanning for
patterned wafer inspection*, product page; Wayback Machine capture of
2002-06-04.
<https://web.archive.org/web/20020604135033/http://www.kla-tencor.com:80/products/defect_control/aitxp/aitxp.html>
Extends the AIT II and AIT III, and groups the 23xx, AIT and eS20 series
as a combination of "brightfield/darkfield and e-beam" inspection. Used on
the defect and particle inspection page. Tier: cross-check (vendor
statement).

**KLA-2351** — KLA-Tencor, *2351: High-resolution imaging for patterned
wafer inspection*, product page; Wayback Machine capture of 2002-01-31.
<https://web.archive.org/web/20020131004355/http://www.kla-tencor.com:80/products/defect_control/2351/2351.html>
Critical-defect detection "at design rules of 0.13 µm and smaller", an
upgrade path from the 2350 and 200/300 mm bridging. Used on the defect and
particle inspection page. Tier: cross-check (vendor statement).

**KLA-EV300** — KLA-Tencor, *eV300: E-beam defect review*, product page;
Wayback Machine capture of 2002-02-08.
<https://web.archive.org/web/20020208135357/http://www.kla-tencor.com:80/products/defect_control/ev300/ev300.html>
An SEM review tool that reads defect files from inspection and optical
review systems and has integrated automatic defect classification. Used on
the defect and particle inspection page. Tier: cross-check (vendor
statement).

**KLA-DEFECT-2002** — KLA-Tencor, *Defect Control* (inspection, review and
analysis products), product menu page; Wayback Machine capture of
2002-06-03.
<https://web.archive.org/web/20020603184120/http://www.kla-tencor.com:80/products/defect_control/index.html>
Lists the inspection (AIT XP, Surfscan SP1 DLS, 2351, 2401, eS20XP and
others) and review (CRS-3000, eV300) products, and describes e-beam and
optical review. Used on the defect and particle inspection page. Tier:
cross-check (vendor statement).

**WIKI-DARKFIELD** — Wikipedia, *Dark-field microscopy*.
<https://en.wikipedia.org/wiki/Dark-field_microscopy> Microscopy methods
that exclude the unscattered beam from the image. Used on the defect and
particle inspection page. Tier: high-level.

**PAT-SCAN-TENCOR** — L. K. Galbraith (Tencor Instruments), *Scanning
contaminant and defect detector*, US 4,378,159 A, filed 1981-03-30,
granted 1983-03-29. <https://patents.google.com/patent/US4378159A/en> A
scanning laser detector for reflective surfaces with a light collector
for scattered light. Used on the defect and particle inspection page.
Tier: deep dive.

**PAT-COLLECTOR-TENCOR** — L. K. Galbraith (Tencor Instruments), *Light
collector for optical contaminant and flaw detector*, US 4,601,576 A, filed
1983-12-09, granted 1986-07-22.
<https://patents.google.com/patent/US4601576A/en> A two-stage collector
that re-images diffusely scattered light onto a detector. Used on the
defect and particle inspection page. Tier: deep dive.

**PAT-PHOTOMASK-KLA** — K. Levy and P. Sandland (KLA Instruments),
*Automatic photomask inspection system and apparatus*, US 4,247,203 A,
filed 1978-04-03, granted 1981-01-27.
<https://patents.google.com/patent/US4247203A/en> Optical inspection that
detects differences between two dies by comparing aligned detector
signals. Used on the defect and particle inspection page. Tier: deep dive.

**PAT-INSPECT-KLA** — J. R. Jordan III, M. Nikoonahad and K. B. Wells
(KLA-Tencor), *Surface inspection system*, US 5,864,394 A, filed
1995-09-29, granted 1999-01-26.
<https://patents.google.com/patent/US5864394A/en> A high-throughput
inspection system that detects anomalies by comparing adjacent repeating
patterns, with dynamic height correction. Used on the defect and particle
inspection page. Tier: deep dive.

**PAT-OBLIQUE-KLA** — M. Vaez-Iravani, S. Stokowski and G. Zhao
(KLA-Tencor), *Sample inspection system*, US 6,201,601 B1, filed
1997-09-19, granted 2001-03-13.
<https://patents.google.com/patent/US6201601B1/en> Normal and oblique
illumination with a curved-mirror collector and butterfly-shaped spatial
filters, for bare or unpatterned wafers and rough films, separating
particles from COPs. Used on the defect and particle inspection page.
Tier: deep dive.

**PAT-TWOPHASE-ORBOT** — D. Alumot, G. Neumann, R. Sherman and E. Tirosh
(Orbot Instruments), *Two-phase optical inspection method and apparatus
for defect detection*, US 5,699,447 A, filed 1991-11-12, granted
1997-12-16. <https://patents.google.com/patent/US5699447A/en> A fast laser
scan of the whole surface followed by high-resolution examination of the
suspected locations only. Used on the defect and particle inspection page.
Tier: deep dive.

**RADIN-1988** — C. Radin, "A Defect Reduction Methodology For Increased
Sort Yield Using Automated Defect Inspection", *Proc. SPIE* **0921**, 224
(1988). <https://doi.org/10.1117/12.968369> Automated inspection with a
KLA-2020 compared with operator inspection and electrical short-loop
experiments. Used on the defect and particle inspection page. Tier: deep
dive.

**SHERMAN-1993** — R. Sherman, E. Tirosh and Z. Smilansky, "Automatic
defect classification system for semiconductor wafers", *Proc. SPIE*
**1907**, 72–79 (1993). <https://doi.org/10.1117/12.144824> An adaptive
classifier for patterned-wafer defects on Orbot's inspection system. Used
on the defect and particle inspection page. Tier: deep dive.

**BREAUX-1995** — L. Breaux and B. Singh, "Automatic defect classification
system for patterned semiconductor wafers", *Proc. ISSM* 1995, pp. 68–73.
<https://doi.org/10.1109/ISSM.1995.524362> A commercial ADC system
combining image processing and a fuzzy-logic expert system. Used on the
defect and particle inspection page. Tier: deep dive.

**NURANI-1996** — R. K. Nurani, R. Akella and A. J. Strojwas, "In-line
defect sampling methodology in yield management: an integrated framework",
*IEEE Transactions on Semiconductor Manufacturing* **9**(4), 506–517
(1996). <https://doi.org/10.1109/66.542166> Cost-based defect sampling
trading inspection cost against the yield impact of undetected defects.
Used on the defect and particle inspection page. Tier: deep dive.

**TOBIN-1997** — K. W. Tobin Jr., S. S. Gleason, T. P. Karnowski, S. L.
Cohen and F. Lakhani, "Automatic classification of spatial signatures on
semiconductor wafer maps", *Proc. SPIE* **3050**, 434 (1997).
<https://doi.org/10.1117/12.275936> Spatial signature analysis of wafer
defect maps (SEMATECH and Oak Ridge National Laboratory). Used on the
defect and particle inspection page. Tier: deep dive.

**ONO-2002** — M. Ono, H. Iwata and K. Watanabe, "Accuracy of yield impact
calculation based on kill ratio", *ASMC 2002*.
<https://doi.org/10.1109/ASMC.2002.1001580> Simulated defect and bin maps
showing when kill-ratio yield-impact estimates fail. Used on the defect
and particle inspection page. Tier: deep dive.

**TENCOR-THINFILM-1997** — Tencor Instruments, *Thin Film Measurement*
(Prometrix UV-1250SE, UV-1270SE, UV-1050, FT-750 and SpectraMap SM300),
product page; Wayback Machine capture of 1997-03-02.
<https://web.archive.org/web/19970302033547/http://www.tencor.com:80/products/thinfilmmesaurement.html>
Spectroscopic ellipsometry combined with UV spectrophotometry for
thickness, refractive index and extinction coefficient of single films and
stacks; a broadband reflectometer for resists and ARCs; a visible
spectrophotometer for films down to about 150 Å; and a mapper for
dielectric films from 200 Å to 4 µm on monitor wafers. Used on the film
thickness and stress metrology page. Tier: cross-check (vendor
statement).

**TENCOR-STRESS-1997** — Tencor Instruments, *Thin Film Stress
Measurement* (FLX-5400, FLX-2320, FLX-2350fp and FLX-2900), product page;
Wayback Machine capture of 1997-03-02.
<https://web.archive.org/web/19970302033500/http://www.tencor.com:80/products/thinfilmstress.html>
Dual-wavelength stress gauges: radial stress maps (FLX-5400), measurements
from −65 °C to 500 °C (FLX-2320) and in-situ measurements up to 900 °C
(FLX-2900). Used on the film thickness and stress metrology page. Tier:
cross-check (vendor statement).

**TENCOR-UV1270SE-1996** — Tencor Instruments, *Tencor Instruments
Introduces Next-Generation Film Measurement System with Advanced
Automation Capabilities* (Prometrix UV-1270SE), press release, 1996-06-06;
Wayback Machine capture of 1997-03-02.
<https://web.archive.org/web/19970302033849/http://www.tencor.com:80/press/uv-1270s.html>
A UV spectrophotometry and spectroscopic ellipsometry film gauge with an
integrated SMIF minienvironment and measurement areas smaller than
50 µm. Used on the film thickness and stress metrology page. Tier:
cross-check (vendor statement).

**KLA-FLX2320** — KLA-Tencor, *FLX-2320: Thin Film Stress Metrology*,
product page; Wayback Machine capture of 2002-08-20.
<https://web.archive.org/web/20020820125852/http://www.kla-tencor.com:80/products/metrology/FLX-2320/FLX-2320.html>
Stress measurement on all film types for production monitoring of
cracking, voiding and lifting, with dual-wavelength switching for
transparent films such as silicon nitride; lists the ASET-F5x and Quantox
XP beside it. Used on the film thickness and stress metrology page. Tier:
cross-check (vendor statement).

**TW-OP3260** — Therma-Wave, *The Opti-Probe 3260*, product page; Wayback
Machine capture of 1998-12-05.
<https://web.archive.org/web/19981205083736/http://www.thermawave.com:80/op3260.htm>
Beam profile ellipsometry, beam profile reflectometry and spectrometry in
one gauge: dielectric films from 0 to 150,000 Å, better than 0.1 Å
precision in a 0.9 µm spot, ONO and OPO stacks, simultaneous thickness and
index of PECVD nitrides, subtractive etch-rate maps, and its light
sources. Used on the film thickness and stress metrology page. Tier:
cross-check (vendor statement).

**TW-OP5000** — Therma-Wave, *Opti-Probe 5000 Product Family*, product
page; Wayback Machine capture of 1998-12-06.
<https://web.archive.org/web/19981206005043/http://www.thermawave.com:80/op5000.htm>
The Opti-Probe 5240, adding deep-UV spectroscopic and absolute
ellipsometry to beam profile reflectometry. Used on the film thickness and
stress metrology page. Tier: cross-check (vendor statement).

**TW-HISTORY** — Therma-Wave, *Therma-Wave Corporate History*, web page;
Wayback Machine capture of 2001-07-13.
<https://web.archive.org/web/20010713111217/http://www.thermawave.com:80/aboutus/corphistory.htm>
The company's two product lines: the Therma-Probe implant monitor
(introduced 1985) and the Opti-Probe film gauge (introduced 1992). Used
on the film thickness and stress metrology and sheet-resistance and dose
metrology pages. Tier: cross-check (vendor statement).

**RUDOLPH-1999** — Rudolph Technologies, Inc., *1999 Annual Report*
(including the Form 10-K for 1999); Wayback Machine capture of 2000-08-30.
<https://web.archive.org/web/20000830152419/http://www.rudolphtech.com:80/ir/6859Rudolph99AR.pdf>
Describes the AutoEL of 1977, the four-laser SpectraLASER ellipsometers,
the MatrixMetrology line (1999), reflectometry for thicker films, and the
MetaPULSE optical-acoustic gauges for up to six opaque layers from under
20 Å to over 5 µm at 60 wafers per hour. Used on the film thickness and
stress metrology page. Tier: cross-check (vendor statement).

**NANOMETRICS-2000** — Nanometrics Incorporated, Form 10-K for the fiscal
year ended 2000-12-31; Wayback Machine capture of 2003-03-23.
<https://web.archive.org/web/20030323070701/http://www.nanometrics.com:80/Downloads/10k_2000.pdf>
Microscope-based spectroscopic reflectometry with ellipsometry and FTIR
options (NanoSpec 8000X, 9100 and others), integrated metrology for
deposition, CMP and etch tools, and OEM supply for Applied Materials'
Mirra Mesa (1998) and Producer QA (1999). Used on the film thickness and
stress metrology page. Tier: cross-check (vendor statement).

**WIKI-ELLIPSOMETRY** — Wikipedia, *Ellipsometry*.
<https://en.wikipedia.org/wiki/Ellipsometry> The change of polarisation
on reflection, compared with a model, to characterise thin films. Used on
the film thickness and stress metrology page. Tier: high-level.

**WIKI-PICOSECOND** — Wikipedia, *Picosecond ultrasonics*.
<https://en.wikipedia.org/wiki/Picosecond_ultrasonics> Laser-generated
acoustic echoes used as a thin-film metrology technique in semiconductor
processing. Used on the film thickness and stress metrology page. Tier:
high-level.

**WIKI-FTIR** — Wikipedia, *Fourier-transform infrared spectroscopy*.
<https://en.wikipedia.org/wiki/Fourier-transform_infrared_spectroscopy>
The infrared method behind composition measurements of dielectric films.
Used on the film thickness and stress metrology page. Tier: high-level.

**PAT-BPR-THERMAWAVE** — N. Gold, D. L. Willenborg, J. Opsal and A.
Rosencwaig (Therma-Wave), *Method and apparatus for measuring thickness of
thin films*, US 4,999,014 A, filed 1989-05-04, granted 1991-03-12.
<https://patents.google.com/patent/US4999014A/en> Thickness from the
reflected intensity against angle of incidence within a beam focused by a
high-numerical-aperture lens. Used on the film thickness and stress
metrology page. Tier: deep dive.

**PAT-MAIWL-RUDOLPH** — R. F. Spanier, R. G. Wolf, R. M. Loiterman and
M. E. Haller (Rudolph Technologies), *Simultaneous multiple angle/multiple
wavelength ellipsometer and method*, US 5,166,752 A, filed 1990-01-11,
granted 1992-11-24. <https://patents.google.com/patent/US5166752A/en>
Illumination over a range of angles from one focused beam, detected on an
array without scanning. Used on the film thickness and stress metrology
page. Tier: deep dive.

**PAT-PICOSECOND-BROWN** — J. Tauc, H. J. Maris and C. Thomsen (Brown
University Research Foundation), *Optical generator and detector of
stress pulses*, US 4,710,030 A, filed 1985-05-17, granted 1987-12-01.
<https://patents.google.com/patent/US4710030A/en> A pump beam generates a
stress pulse and a probe beam detects the change of optical constants it
causes. Used on the film thickness and stress metrology page. Tier: deep
dive.

**ROSENCWAIG-1992** — A. Rosencwaig, J. Opsal, D. L. Willenborg, S. M.
Kelso and J. T. Fanton, "Beam profile reflectometry: A new technique for
dielectric film measurements", *Applied Physics Letters* **60**(11),
1301–1303 (1992). <https://doi.org/10.1063/1.107323> Thickness and optical
constants of films from 30 Å to 20,000 Å with a submicron spot. Used on
the film thickness and stress metrology page. Tier: deep dive.

**FANTON-1993** — J. T. Fanton, J. Opsal, D. L. Willenborg, S. M. Kelso
and A. Rosencwaig, "Multiparameter measurements of thin films using
beam-profile reflectometry", *Journal of Applied Physics* **73**(11),
7035–7040 (1993). <https://doi.org/10.1063/1.352421> S- and
P-polarisation reflectivities over a range of angles, fitting up to three
film parameters. Used on the film thickness and stress metrology page.
Tier: deep dive.

**CHANDLER-HOROWITZ-2003** — D. Chandler-Horowitz, "Assessment of
Ultra-Thin SiO2 Film Thickness Measurement Precision by Ellipsometry",
*AIP Conference Proceedings* **683**, 326–330 (2003).
<https://doi.org/10.1063/1.1622490> The factors behind instrument-to-
instrument and lab-to-lab differences in ellipsometric thickness of
oxides of 10 nm and below. Used on the film thickness and stress metrology
page. Tier: deep dive.

**KAISER-1991** — A. M. Kaiser, "Semiconductor thin-film optical constant
determination and thin-film thickness measurement equipment correlation",
*Proc. SPIE* **1464**, 386 (1991). <https://doi.org/10.1117/12.44451>
Correlating thickness gauges by refining optical constants rather than
applying offsets. Used on the film thickness and stress metrology page.
Tier: deep dive.

**STOUT-1989** — P. J. Stout and K. Krishnan, "A Comparison Of
Multicomponent Quantitative Analysis Methods For The Determination Of
Boron And Phosphorous In BPSG Films On Silicon", *Proc. SPIE* **1145**,
494 (1989). <https://doi.org/10.1117/12.969563> Infrared bands for
phosphorus (about 1335 cm⁻¹) and boron (about 1420 cm⁻¹) in doped glass,
substrate requirements and calibration. Used on the film thickness and
stress metrology page. Tier: deep dive.

**SHIRAIWA-1968** — T. Shiraiwa and N. Fujino, "Theoretical Formulas for
Film Thickness Measurement by Means of Fluorescence X-Rays", *Advances in
X-ray Analysis* **12**, 446–456 (1968).
<https://doi.org/10.1154/S0376030800005917> Fluorescence X-ray intensities
from coating and substrate as functions of coating thickness. Used on the
film thickness and stress metrology page. Tier: deep dive.

**WINDOVER-2001** — D. Windover, "Development of an in-line X-ray
reflectivity technique for metal film thickness measurement", *AIP
Conference Proceedings* **550**, 243–248 (2001).
<https://doi.org/10.1063/1.1354405> Fixed-angle energy-dispersive X-ray
reflectivity for tantalum films below 10 nm. Used on the film thickness
and stress metrology page. Tier: deep dive.

**THOMSEN-1986** — C. Thomsen, H. T. Grahn, H. J. Maris and J. Tauc,
"Surface generation and detection of phonons by picosecond light pulses",
*Physical Review B* **34**(6), 4129–4138 (1986).
<https://doi.org/10.1103/PhysRevB.34.4129> Generation and optical
detection of picosecond stress pulses. Used on the film thickness and
stress metrology page. Tier: deep dive.

**STONER-1998** — R. J. Stoner, C. J. Morath, G. Tas, G. Antonelli and
H. J. Maris, "Picosecond ultrasonics: A new approach for control of thin
metal processes", *Characterization and Metrology for ULSI Technology:
1998 International Conference*, pp. 385–394 (AIP, 1998).
<https://doi.org/10.1063/1.56821> Applications to PVD TiN, CVD WNx and W,
Ti/TiN stacks and five-layer interconnect stacks. Used on the film
thickness and stress metrology page. Tier: deep dive.

**FLINN-1987** — P. A. Flinn, D. S. Gardner and W. D. Nix, "Measurement
and interpretation of stress in aluminum-based metallization as a
function of thermal history", *IEEE Transactions on Electron Devices*
**34**(3), 689–699 (1987). <https://doi.org/10.1109/T-ED.1987.22981>
Stress from wafer curvature measured by laser scanning, through thermal
cycles. Used on the film thickness and stress metrology page. Tier: deep
dive.

**TENCOR-RS75-1995** — Tencor Instruments, *Tencor's Film Measurement
Division Introduces New OmniMap RS75 Resistivity Mapping System*, press
release, 1995-10-10; Wayback Machine capture of 1997-03-02.
<https://web.archive.org/web/19970302035054/http://www.tencor.com:80/press/omnimaprs75.html>
A four-point-probe mapper based on Prometrix technology for implant,
metallisation, diffusion, epitaxy and polysilicon: about one second per
site, over 100 wafers per hour at five sites on 200 mm, and a
temperature-compensated RS75/tc model. Used on the sheet-resistance and
dose metrology page. Tier: cross-check (vendor statement).

**TENCOR-RESISTIVITY-1997** — Tencor Instruments, *Resistivity
Measurement* (OmniMap NC110 and RS75), product page; Wayback Machine
capture of 1997-03-02.
<https://web.archive.org/web/19970302033556/http://www.tencor.com:80/products/resistivity.html>
The NC110 for resistivity on product wafers with aluminium and tungsten
metallisation (to 10 Ω/sq) and the RS75 four-point probe from implant
monitoring to thin-film control. Used on the sheet-resistance and dose
metrology page. Tier: cross-check (vendor statement).

**KLA-RS100** — KLA-Tencor, *RS-100: Advanced Resistivity Metrology*,
product page; Wayback Machine capture of 2002-08-16.
<https://web.archive.org/web/20020816223302/http://www.kla-tencor.com:80/products/metrology/rs-100/rs-100.html>
A 200/300 mm resistivity mapper measuring to within 1 mm of the film edge,
described as the tool of choice in the metals, CMP and diffusion modules.
Used on the sheet-resistance and dose metrology page. Tier: cross-check
(vendor statement).

**TW-IMPLANT** — Therma-Wave, *Ion Implantation Monitoring*
(applications), web page; Wayback Machine capture of 2001-07-13.
<https://web.archive.org/web/20010713111006/http://www.thermawave.com:80/apps/implant.htm>
The thermal-wave implant monitor: sensitivity to damage and dose, to
energy (varying with depth), to channelling and scanning effects;
measurement before anneal on product wafers; low-dose monitoring for
threshold control; and the annealed test-wafer practice it replaces. Used
on the sheet-resistance and dose metrology page. Tier: cross-check
(vendor statement).

**TW-TP-2000** — Therma-Wave, *The Therma-Probe Family*, product page;
Wayback Machine capture of 2000-10-06.
<https://web.archive.org/web/20001006232958/http://www.thermawave.com:80/prod_tpf.htm>
The Therma-Probe 500 (introduced July 1996): 10 µm × 10 µm sites on product
wafers, solid-state lasers, and more than 360 Therma-Probe systems
installed by April 1998. Used on the sheet-resistance and dose metrology
page. Tier: cross-check (vendor statement).

**TW-PRODUCTS-1997** — Therma-Wave, *Therma-Wave Products* (Opti-Probe and
Therma-Probe 500 Series), web page; Wayback Machine capture of 1997-01-26.
<https://web.archive.org/web/19970126142849/http://www.thermawave.com:80/products.html>
Presents the Therma-Probe as the industry standard for monitoring implants
on product wafers. Used on the sheet-resistance and dose metrology page.
Tier: cross-check (vendor statement).

**PERLOFF-1977** — D. S. Perloff, F. E. Wahl and J. Conragan, "Four-Point
Sheet Resistance Measurements of Semiconductor Doping Uniformity",
*Journal of The Electrochemical Society* **124**(4), 582–590 (1977).
<https://doi.org/10.1149/1.2133355> Automated sheet-resistance maps with
four-point probes and van der Pauw resistors, shown to be interchangeable
for uniformity measurements. Used on the sheet-resistance and dose
metrology page. Tier: deep dive.

**PAT-RSMAP-PROMETRIX** — D. S. Perloff and C. Mallory (Prometrix),
*Apparatus and methods for resistivity testing*, US 4,703,252 A, filed
1985-02-22, granted 1987-10-27.
<https://patents.google.com/patent/US4703252A/en> An automatic sheet
resistance mapping system with a rotatable stage and a linear four-tip
probe head, in contour and diameter scan modes. Used on the
sheet-resistance and dose metrology page. Tier: deep dive.

**SMITH-1986** — A. K. Smith, W. H. Johnson and W. A. Keenan, "Sheet
Resistance Low Dose Monitoring Using The Double Implant Technique", *Proc.
SPIE* **0623**, 50 (1986). <https://doi.org/10.1117/12.961194> Direct
sheet-resistance monitoring down to 2 × 10¹¹ cm⁻² and the double-implant
technique for low doses. Used on the sheet-resistance and dose metrology
page. Tier: deep dive.

**HILLARD-2004** — R. J. Hillard, J. Borland and C. W. Ye, "Accurate
determination of ultra-shallow junction sheet resistance with a
non-penetrating four point probe", *IWJT 2004*, pp. 98–101.
<https://doi.org/10.1109/IWJT.2004.1306768> Elastic-material probes
forming non-penetrating contacts for ultra-shallow junctions. Used on the
sheet-resistance and dose metrology page. Tier: deep dive.

**MILLER-1976** — G. L. Miller, D. A. H. Robinson and J. D. Wiley,
"Contactless measurement of semiconductor conductivity by radio
frequency-free-carrier power absorption", *Review of Scientific
Instruments* **47**(7), 799–805 (1976). <https://doi.org/10.1063/1.1134756>
Conductivity from the power a slice absorbs in an oscillating magnetic
field, for semiconductors to metals. Used on the sheet-resistance and dose
metrology page. Tier: deep dive.

**PAT-THERMALWAVE-THERMAWAVE** — A. Rosencwaig, J. Opsal, W. L. Smith and
D. L. Willenborg (Therma-Wave Partners), *Detecting thermal waves to
evaluate thermal parameters*, US 4,579,463 A, filed 1984-05-21, granted
1986-04-01. <https://patents.google.com/patent/US4579463A/en> Thermal
waves detected through the change of reflectivity of a periodically heated
surface. Used on the sheet-resistance and dose metrology page. Tier: deep
dive.

**ROSENCWAIG-1985** — A. Rosencwaig, J. Opsal, W. L. Smith and D. L.
Willenborg, "Detection of thermal waves through optical reflectance",
*Applied Physics Letters* **46**(11), 1013–1015 (1985).
<https://doi.org/10.1063/1.95794> Non-contact thermal-wave detection
through the temperature dependence of reflectance. Used on the
sheet-resistance and dose metrology page. Tier: deep dive.

**OPSAL-1985** — J. Opsal and A. Rosencwaig, "Thermal and plasma wave depth
profiling in silicon", *Applied Physics Letters* **47**(5), 498–500 (1985).
<https://doi.org/10.1063/1.96105> Depth profiling with the plasma wave of
laser-generated free carriers. Used on the sheet-resistance and dose
metrology page. Tier: deep dive.

**PAT-PLASMAWAVE-THERMAWAVE** — J. Opsal, A. Rosencwaig and W. L. Smith
(Therma-Wave), *Method and apparatus for evaluating surface and subsurface
features in a semiconductor*, US 4,854,710 A, filed 1987-07-23, granted
1989-08-08. <https://patents.google.com/patent/US4854710A/en> A periodic
electron–hole plasma monitored through reflectivity to evaluate dopants,
residues and defects. Used on the sheet-resistance and dose metrology
page. Tier: deep dive.

**SING-2000** — D. Sing, P. Borden and L. Bechtler, "Low and high dose
process monitoring using the BX-10 implant monitor system", *2000
International Conference on Ion Implantation Technology Proceedings*,
pp. 639–641. <https://doi.org/10.1109/IIT.2000.924234> An in-line
ultra-shallow-junction tool evaluated as a low- and high-dose implant
monitor. Used on the sheet-resistance and dose metrology page. Tier: deep
dive.

**HITACHI-S4800** — Hitachi High Technologies America, *S-4800 UHR
FE-SEM*, product page; Wayback Machine capture of 2009-10-21.
<https://web.archive.org/web/20091021203654/http://www.hitachi-hta.com:80/products/electron-microscopes-and-focused-ion-beam/field-emission-sem/s-4800-uhr-fe-sem>
Secondary-electron resolution of 1.0 nm at 15 kV and 2.0 nm at 1 kV
(1.4 nm with beam deceleration), 200 mm specimens, a semi in-lens detector
with signal separation, and EDX options. Used on the cross-section SEM and
profilers page. Tier: cross-check (vendor statement).

**FEI-FIB200XP-1999** — FEI Company, *FIB workstations: FIB 200xP*, product
page; Wayback Machine capture of 1999-01-28.
<https://web.archive.org/web/19990128142220/http://www.feic.com:80/products/fib200xp.htm>
A gallium focused-ion-beam workstation for milling, deposition and imaging,
including SEM/TEM cross-section preparation on small specimens. Used on the
cross-section SEM and profilers page. Tier: cross-check (vendor statement).

**FEI-FIB800-1999** — FEI Company, *FIB workstations: FIB 800xP*, product
page; Wayback Machine capture of 1999-04-17.
<https://web.archive.org/web/19990417131418/http://www.feic.com:80/products/fib800xp.htm>
A FIB for packaged parts and 8-inch wafers that sections submicron
features, deposits metal and dielectric, and navigates by inspection-tool
particle maps. Used on the cross-section SEM and profilers page. Tier:
cross-check (vendor statement).

**FEI-DUALBEAM-2006** — FEI Company, *DualBeam Systems*, product-type page;
Wayback Machine capture of 2006-11-01.
<https://web.archive.org/web/20061101125513/http://www.fei.com:80/Products/ProdTypes/DualBeamFIB/tabid/69/Default.aspx>
The Nova, Quanta, Helios and Strata FIB/SEM families and their
site-specific cross-sectioning and TEM preparation. Used on the
cross-section SEM and profilers page. Tier: cross-check (vendor
statement).

**SELA-2001** — SELA, *Company Background* (conventional, automated SEM and
automated TEM sample preparation), web page; Wayback Machine capture of
2001-10-31. <https://web.archive.org/web/20011031233400/http://sela.com:80/about.htm>
Cleave-and-polish cross-sections and their drawbacks, automated
microcleaving through a targeted feature in about ten minutes, and FIB
pre-thinning for TEM. Used on the cross-section SEM and profilers page.
Tier: cross-check (vendor statement).

**TENCOR-PROFILING-1997** — Tencor Instruments, *Surface Profiling*
(HRP-200, P-22, P-30 SMIF, P-10, P-11, P-12, FP-20 and Alpha-Step 500),
product page; Wayback Machine capture of 1997-03-02.
<https://web.archive.org/web/19970302033450/http://www.tencor.com:80/products/surfaceprof.html>
Stylus profilers for wafers and other substrates, with low-force heads,
and the HRP-200 combining a stylus profiler with AFM-like imaging. Used on
the cross-section SEM and profilers page. Tier: cross-check (vendor
statement).

**TENCOR-HRP200-1996** — Tencor Instruments, *Tencor Instruments Unveils
Advanced Metrology Product for Production-Level Wafer Surface
Characterization* (HRP-200 High Resolution Profiler), press release,
1996-10-14; Wayback Machine capture of 1997-03-02.
<https://web.archive.org/web/19970302033817/http://www.tencor.com:80/press/HRP_200PR.html>
A production profiler for metal CMP (tungsten plug recess, erosion,
dishing, ILD scratches) with 205 mm scans, 8 Å step-height repeatability
and a 0.05 mg stylus force. Used on the cross-section SEM and profilers
page. Tier: cross-check (vendor statement).

**KLA-HRP** — KLA-Tencor, *HRPs 240/340: Automated high-resolution surface
metrology*, product page; Wayback Machine capture of 2002-06-04.
<https://web.archive.org/web/20020604105300/http://www.kla-tencor.com:80/products/metrology/hrps/hrps.html>
Long-scan profilometry and high-resolution imaging for CMP and etch, with
a dipping mode for high-aspect-ratio depths. Used on the cross-section SEM
and profilers page. Tier: cross-check (vendor statement).

**KLA-P15** — KLA-Tencor, *Profilers P-15: High Performance Surface
Metrology*, product page; Wayback Machine capture of 2002-06-04.
<https://web.archive.org/web/20020604110248/http://www.kla-tencor.com:80/products/metrology/profilers/profilers.html>
A stylus profiler with 7.5 Å (1σ) repeatability that reports CMP dishing
and erosion. Used on the cross-section SEM and profilers page. Tier:
cross-check (vendor statement).

**VEECO-STYLUS-2000** — Veeco Instruments, *Dektak Stylus Profilers*,
product page; Wayback Machine capture of 2000-05-23.
<https://web.archive.org/web/20000523020041/http://www.veeco.com:80/body_stylus_profilers.html>
Dektak profilers for step heights, planarity and roughness, and etch and
deposition uniformity on 200 mm and 300 mm wafers. Used on the
cross-section SEM and profilers page. Tier: cross-check (vendor
statement).

**VEECO-AFM-2000** — Veeco Instruments, *Digital Instruments Atomic Force
Microscopes (AFMs)*, product page; Wayback Machine capture of 2000-05-21.
<https://web.archive.org/web/20000521223941/http://www.veeco.com:80/body_di_afm.html>
The Dimension 3100, 5000 and 9000 AFMs, the last fully automated for
in-fab metrology on 200 mm wafers. Used on the cross-section SEM and
profilers page. Tier: cross-check (vendor statement).

**WIKI-FIB** — Wikipedia, *Focused ion beam*.
<https://en.wikipedia.org/wiki/Focused_ion_beam> Ion-beam milling,
deposition and imaging, dual-beam FIB/SEM systems and TEM sample
preparation. Used on the cross-section SEM and profilers page. Tier:
high-level.

**WIKI-AFM** — Wikipedia, *Atomic force microscopy*.
<https://en.wikipedia.org/wiki/Atomic_force_microscopy> The AFM and its
history. Used on the cross-section SEM and profilers page. Tier:
high-level.

**WIKI-PROFILOMETER** — Wikipedia, *Profilometer*.
<https://en.wikipedia.org/wiki/Profilometer> Contact and non-contact
surface profiling. Used on the cross-section SEM and profilers page. Tier:
high-level.

**REUSS-1985** — R. H. Reuss, "Potential applications of focused ion beam
technology for the semiconductor industry", *Nuclear Instruments and
Methods in Physics Research B* **10–11**, 515–521 (1985).
<https://doi.org/10.1016/0168-583X(85)90299-X> An early survey of FIB uses
in the semiconductor industry (bibliographic data only checked). Used on
the cross-section SEM and profilers page. Tier: deep dive.

**NIKAWA-1991** — K. Nikawa, "Applications of focused ion beam technique to
failure analysis of very large scale integrations: A review", *Journal of
Vacuum Science & Technology B* **9**(5), 2566–2577 (1991).
<https://doi.org/10.1116/1.585694> FIB cross-sections of VLSI failures and
FIB preparation methods for further analysis. Used on the cross-section
SEM and profilers page. Tier: deep dive.

**GIANNUZZI-1999** — L. A. Giannuzzi and F. A. Stevie, "A review of focused
ion beam milling techniques for TEM specimen preparation", *Micron*
**30**(3), 197–204 (1999). <https://doi.org/10.1016/S0968-4328(99)00005-0>
A review of FIB milling for TEM specimens (bibliographic data only
checked). Used on the cross-section SEM and profilers page. Tier: deep
dive.

**BENNETT-1981** — J. M. Bennett and J. H. Dancy, "Stylus profiling
instrument for measuring statistical properties of smooth optical
surfaces", *Applied Optics* **20**(10), 1785 (1981).
<https://doi.org/10.1364/AO.20.001785> A stylus instrument with 1–2 Å
height resolution and adjustable, non-marking stylus loading. Used on the
cross-section SEM and profilers page. Tier: deep dive.

**BINNIG-1986** — G. Binnig, C. F. Quate and Ch. Gerber, "Atomic Force
Microscope", *Physical Review Letters* **56**(9), 930–933 (1986).
<https://doi.org/10.1103/PhysRevLett.56.930> The atomic force microscope,
combining the scanning tunnelling microscope and the stylus profilometer.
Used on the cross-section SEM and profilers page. Tier: deep dive.

**MARTIN-1994** — Y. Martin and H. K. Wickramasinghe, "Method for imaging
sidewalls by atomic force microscopy", *Applied Physics Letters*
**64**(19), 2498–2500 (1994). <https://doi.org/10.1063/1.111578> Sidewall
profiles and critical dimensions of lines and trenches with a boot-shaped
AFM tip. Used on the cross-section SEM and profilers page. Tier: deep
dive.

**SPINELLA-1996** — C. Spinella, V. Raineri, F. La Via and S. U.
Campisano, "Two-dimensional junction profiling by selective chemical
etching: Applications to electron device characterization", *Journal of
Vacuum Science & Technology B* **14**(1), 414–420 (1996).
<https://doi.org/10.1116/1.588485> Delineation of two-dimensional junction
profiles for transmission electron microscopy by selective HF:HNO3
etching of doped silicon, including boron-doped samples. Used on the
cross-section SEM and profilers page. Tier: deep dive.

**DIXSON-2002** — R. G. Dixson, A. Guerry, M. H. Bennett, T. V. Vorburger
and M. T. Postek, "Toward traceability for at-line AFM dimensional
metrology", *Proc. SPIE* **4689**, 313 (2002).
<https://doi.org/10.1117/12.473471> A CD-AFM reference measurement system
at International SEMATECH with NIST, its scale calibration and uncertainty
budgets, as a traceable reference for CD-SEM benchmarking. Used on the
cross-section SEM and profilers page. Tier: deep dive.

**SAKATA-2002** — T. Sakata, H. Takahashi and T. Sekine, "Investigation of
Ga contamination due to analysis by dual beam FIB", *Proceedings of the
9th International Symposium on the Physical and Failure Analysis of
Integrated Circuits (IPFA 2002)*, pp. 174–178.
<https://doi.org/10.1109/IPFA.2002.1025643> Dual-beam FIB/SEM sectioning of
defects for yield management, and the gallium contamination that bears on
whether a wafer can return to the production line. Used on the
cross-section SEM and profilers page. Tier: deep dive.

**EEPOWER-4070** — EE Power, *Agilent Technologies Offers New 4070 Series
Testers*, new-products item, 2002-12-03.
<https://eepower.com/new-industry-products/agilent-technologies-offers-new-4070-series-testers/>
Agilent's 4072B and 4073B parametric testers with a capacitance meter in
each test head, up to 40 per cent higher throughput, prices including
on-site calibration, and shipments planned for May 2003. Used on the
parametric tester and prober page. Tier: cross-check (vendor statement
reported by trade press).

**ELECTROGLAS-4090** — Electroglas, *The Horizon 4090*, product page;
Wayback Machine capture of 1998-02-11.
<https://web.archive.org/web/19980211212301/http://www.electroglas.com:80/products/4090.htm>
A 200 mm automatic wafer prober with automatic probe-to-pad alignment,
linear motors, OCR and GEM integration. Used on the parametric tester and
prober page. Tier: cross-check (vendor statement).

**ELECTROGLAS-4085X** — Electroglas, *Horizon 4085X*, product page;
Wayback Machine capture of 1998-02-11.
<https://web.archive.org/web/19980211212526/http://www.electroglas.com:80/products/4085x.htm>
A high-force 200 mm prober for high-pin-count devices with a Class 1
internal environment. Used on the parametric tester and prober page.
Tier: cross-check (vendor statement).

**ELECTROGLAS-4090U** — Electroglas, *Horizon 4090µ*, product page;
Wayback Machine capture of 2001-07-13.
<https://web.archive.org/web/20010713004941/http://www.electroglas.com:80/products/4090micro.html>
A prober with an integrated mini-environment and SMIF for ultra-clean
parametric test and high-force sort. Used on the parametric tester and
prober page. Tier: cross-check (vendor statement).

**ELECTROGLAS-1999** — Electroglas, *1999 Annual Report*, "Wafer Probing"
section, web page; Wayback Machine capture of 2002-05-30.
<https://web.archive.org/web/20020530031508/http://www.electroglas.com:80/press/pressreleases/reports/1999annual/wafer.htm>
What a wafer prober does, how it connects to the parametric or functional
tester through the probe card, and the high-force and 300 mm trends. Used
on the parametric tester and prober page. Tier: cross-check (vendor
statement).
Also used on the hardware consumables material page.

**TEL-PROBER** — Tokyo Electron, *P-8XL & P-12XL Series Wafer Prober*
(Certified Used Equipment), product page, accessed 2026-09-13.
<https://www.telcertifiedused.com/cue/buy/product-test.jsp> Refurbished
TEL P-8 and P-12 series probers; the P-8XL handles 100–200 mm wafers.
Used on the parametric tester and prober page. Tier: cross-check (vendor
statement).

**FORMFACTOR-SUMMIT200** — FormFactor, *Cascade SUMMIT200 Probe Station*,
product page, accessed 2026-09-13.
<https://www.formfactor.com/product/probe-systems/200-mm-systems/summit200/>
A 200 mm semi- and fully automatic probe system for R&D, device
characterisation and niche production over −60 °C to 300 °C. Used on the
parametric tester and prober page. Tier: cross-check (vendor statement).

**FORMFACTOR-PMC200** — FormFactor, *Cascade PMC200 — 200 mm Cryogenic
Probe Station*, product page, accessed 2026-09-13.
<https://www.formfactor.com/product/probe-systems/wafer-multi-chip-cryogenic-systems/pmc200/>
A manual probe system for wafers up to 200 mm in high vacuum, down to 77 K
with liquid nitrogen or below 7 K with liquid helium. Used on the
parametric tester and prober page. Tier: cross-check (vendor statement).

**LINHOLM-1994** — L. W. Linholm, R. A. Allen and M. W. Cresswell,
"Microelectronic test structures for feature placement and electrical
linewidth metrology", *Proc. SPIE* **10274**, 1027407 (1994).
<https://doi.org/10.1117/12.187462> A review of electrical test structures
for feature placement and line width, measured on commercial test
equipment. Used on the parametric tester and prober page. Tier: deep dive.

**LUKASZEK-1990** — W. Lukaszek, K. G. Grambow and W. J. Yarbrough, "Test
chip based approach to automated diagnosis of CMOS yield problems", *IEEE
Transactions on Semiconductor Manufacturing* **3**(1), 18–27 (1990).
<https://doi.org/10.1109/66.47972> A test chip built by systematic
structural decomposition for unambiguous diagnosis of electrical faults.
Used on the parametric tester and prober page. Tier: deep dive.

**BHUSHAN-2006** — M. Bhushan, M. B. Ketchen, S. Polonsky and A. Gattiker,
"Ring oscillator based technique for measuring variability statistics",
*2006 IEEE ICMTS*, pp. 87–92. <https://doi.org/10.1109/ICMTS.2006.1614281>
Threshold-voltage variation from an array of ring oscillators read with a
frequency counter. Used on the parametric tester and prober page. Tier:
deep dive.

**SPANOS-1992** — C. J. Spanos, "Statistical process control in
semiconductor manufacturing", *Proceedings of the IEEE* **80**(6),
819–830 (1992). <https://doi.org/10.1109/5.149445> A survey of SPC schemes
with semiconductor examples. Used on the parametric tester and prober
page. Tier: deep dive.

**BROZ-1999** — J. J. Broz and R. M. Rincon, "Probe contact resistance
variations during elevated temperature wafer test", *Proc. International
Test Conference 1999*, pp. 396–405.
<https://doi.org/10.1109/TEST.1999.805761> Contact resistance of W, WRe,
BeCu and alloy probes on aluminium pads at 85 °C and the role of oxide
from local Joule heating. Used on the parametric tester and prober page.
Tier: deep dive.
Also used on the hardware consumables material page.

### 8.20 Material-class page sources

Sources introduced for the material-class pages under `docs/materials/`
that had no entry above. Each label on those pages is the key below in
lower case and the citation is the one given in the page footnote; the
entries are grouped by the material page that first cited the source,
and sources already listed above record their use on a material page in
an "Also used on" line of their own. Apart from SKW-CERTS,
EPA-GHGRP-SKYWATER (the EPA's greenhouse-gas reporting record for the
Bloomington facility) and MPCA-2025, which name SkyWater and its
Minnesota site, none of these sources mentions SkyWater, SKY130 or the
Bloomington fab; they describe materials, grades, suppliers and their
products in general. Every URL was fetched on 2026-09-13:
papers were checked through Crossref (bibliographic data) and OpenAlex
(abstracts) and their annotations rest on their abstracts; patents were
checked through Google Patents (bibliographic data and abstract); SEMI
and ASTM standards through their store or catalogue listings (the ASTM
listings through the Wayback Machine capture named in the entry); and
Wikipedia articles through the text of the current article. An entry's
tier records its first use.

#### Wet chemicals (first cited there)

**SEMI-C28** — SEMI, *SEMI C28 — Specification and Guide for
Hydrofluoric Acid*, SEMI Standards store listing (revision C28-0618,
inactive), accessed 2026-09-13.
<https://store-us.semi.org/products/c02800-semi-c28-specification-and-guide-for-hydrofluoric-acid>
The listing's abstract: the purpose "is to standardize requirements for
hydrofluoric acid used in the semiconductor industry", and the scope is
"grades of hydrofluoric acid used in the semiconductor industry". Used on
the wet chemicals material page. Tier: cross-check (standard).

**SEMI-C23** — SEMI, *SEMI C23 — Specification for Buffered Oxide
Etchants*, SEMI Standards store listing (revision C23-0714, reapproved
0620), accessed 2026-09-13.
<https://store-us.semi.org/products/c02300-semi-c23-specifications-for-buffered-oxide-etchants>
Standardises requirements for buffered oxide etchants; scope "grades of
buffered oxide etchants used in the semiconductor industry". Used on the
wet chemicals material page. Tier: cross-check (standard).

**SEMI-C30** — SEMI, *SEMI C30 — Specification and Guide for Hydrogen
Peroxide*, SEMI Standards store listing (revision C30-1223), accessed
2026-09-13.
<https://store-us.semi.org/products/c03000-semi-c30-specification-for-hydrogen-peroxide>
Standardises requirements for grades of hydrogen peroxide and guides a
higher-purity tier; scope "five Grades and one Tier of hydrogen peroxide
used in the semiconductor industry". Used on the wet chemicals material
page. Tier: cross-check (standard).

**SEMI-C44** — SEMI, *SEMI C44 — Specification and Guide for Sulfuric
Acid*, SEMI Standards store listing (revision C44-1223), accessed
2026-09-13.
<https://store-us.semi.org/products/c04400-semi-c44-specification-and-guide-for-sulfuric-acid>
Standardises grades of sulphuric acid and "provides assay and impurity
limits for higher purity Tiers"; scope "two Grades and three Tiers of
sulfuric acid used in the semiconductor industry". Used on the wet
chemicals material page. Tier: cross-check (standard).

**SEMI-C41** — SEMI, *SEMI C41 — Specification and Guide for
2-Propanol*, SEMI Standards store listing (revision C41-0618), accessed
2026-09-13.
<https://store-us.semi.org/products/c04100-semi-c41-specification-and-guide-for-2-propanol>
Covers "all grades of 2-propanol used in the semiconductor industry";
"The VLSI grade purity level is typically required by semiconductor
devices with geometries of 0.8 to 1.2 microns". Used on the wet
chemicals material page. Tier: cross-check (standard).

**WIKI-H2O2** — Wikipedia, *Hydrogen peroxide*.
<https://en.wikipedia.org/wiki/Hydrogen_peroxide> Properties, decomposition
("decomposes slowly into water and elemental oxygen when exposed to
light, and rapidly in the presence of organic or reactive compounds")
and storage with a stabiliser. Used on the wet chemicals material page.
Tier: high-level.

**WIKI-H2SO4** — Wikipedia, *Sulfuric acid*.
<https://en.wikipedia.org/wiki/Sulfuric_acid> Properties, the heat
released on dilution and its use in piranha solution. Used on the wet
chemicals material page. Tier: high-level.

**WIKI-HNO3** — Wikipedia, *Nitric acid*.
<https://en.wikipedia.org/wiki/Nitric_acid> Properties; "Most commercially
available nitric acid has a concentration of 68% in water". Used on the
wet chemicals material page. Tier: high-level.

**WIKI-IPA** — Wikipedia, *Isopropyl alcohol*.
<https://en.wikipedia.org/wiki/Isopropyl_alcohol> Properties, uses and
flammability ("a flammability range of between 2% and 12.7% in air").
Used on the wet chemicals material page. Tier: high-level.

**HIGASHI-1990** — G. S. Higashi, Y. J. Chabal, G. W. Trucks and K.
Raghavachari, "Ideal hydrogen termination of the Si (111) surface",
*Applied Physics Letters* **56**(7), 656–658 (1990).
<https://doi.org/10.1063/1.102728> Aqueous HF removes the oxide and
leaves silicon terminated by hydrogen; basic solutions give ideally
terminated Si(111). Used on the wet chemicals material page. Tier: deep
dive.

**ITANO-1993** — M. Itano, F. W. Kern, M. Miyashita and T. Ohmi,
"Particle removal from silicon wafer surface in wet cleaning process",
*IEEE Transactions on Semiconductor Manufacturing* **6**(3), 258–267
(1993). <https://doi.org/10.1109/66.238174> Alkaline cleans remove
particles better than acid ones by etching and electrostatic repulsion;
an etch rate of at least 0.25 nm/min lifts particles off; a mixing ratio
of 0.05:1:5 is suggested. Used on the wet chemicals material page. Tier:
deep dive.

**NORGA-1997** — G. J. Norga, M. Platero, K. A. Black, A. J. Reddy, J.
Michel and L. C. Kimerling, "Mechanism of Copper Deposition on Silicon
from Dilute Hydrofluoric Acid Solution", *Journal of The Electrochemical
Society* **144**(8), 2801–2810 (1997).
<https://doi.org/10.1149/1.1837898> Electrochemical reduction of metal
ions on silicon in HF; copper nucleates as nanometre-sized precipitates;
tested in 1:100 HF. Used on the wet chemicals material page. Tier: deep
dive.

**ROBBINS-1959** — H. Robbins and B. Schwartz, "Chemical Etching of
Silicon", *Journal of The Electrochemical Society* **106**(6), 505
(1959). <https://doi.org/10.1149/1.2427397> The kinetics of silicon
etching in HF–HNO₃–H₂O at 25 °C over the composition triangle: oxidation
followed by dissolution of the oxide, with the rate-limiting step
depending on composition. Used on the wet chemicals material page. Tier:
deep dive.

**CHEN-2003-EKC** — B.-H. Chen, H. Zhang, Chooi, L. Chan, Y. Xu and J. H.
Ye, "Corrosive Behavior of Tungsten in Post Dry-Etch Residue Remover",
*Industrial & Engineering Chemistry Research* **42**(24), 6096–6103
(2003). <https://doi.org/10.1021/ie030025h> Electrochemical study of
blanket tungsten in EKC265 at 65 °C: the solution is aggressive to
tungsten, and water and chloride increase corrosion and pitting. Used on
the wet chemicals material page. Tier: deep dive.

**PAT-BHF-HASHIMOTO** — T. Ohmi, N. Miki and H. Kikuyama (Hashimoto
Chemical Industries), *Surface treating composition for micro
processing*, US 4,795,582 A, priority 1986-09-29, granted 1989-01-03.
<https://patents.google.com/patent/US4795582A/en> Hydrofluoric acid,
ammonium fluoride and water with aliphatic carboxylic acid, amine or
alcohol surfactants. Used on the wet chemicals material page. Tier: deep
dive.

**PAT-BHF-DAIKIN** — N. Enjo and K. Tamura (Daikin Industries),
*Etchant composition*, US 4,582,624 A, filed 1984-08-09, granted
1986-04-15. <https://patents.google.com/patent/US4582624A/en> HF,
ammonium fluoride and a fluorinated carboxylic-acid surfactant for
etching fine patterns in oxide. Used on the wet chemicals material page.
Tier: deep dive.

**PAT-BHF-STARTEC** — J. G. Hoffman and R. S. Clark (Startec Ventures),
*On-site generation of ultra-high-purity buffered-HF for semiconductor
processing*, US 5,722,442 A, priority 1994-01-07, filed 1996-07-01,
granted 1998-03-03. <https://patents.google.com/patent/US5722442A/en>
Buffered HF made at the fab from scrubbed ammonia and purified aqueous
HF, with density monitoring to control pH and buffering. Used on the
wet chemicals material page. Tier: deep dive.

#### Lithography materials (first cited there)

**JSR-EM** — JSR Corporation, *About our Electronic Materials Business*,
business introduction page, accessed 2026-09-13.
<https://www.jsr.co.jp/jsr_e/products/em/biz/> Describes photoresists as
"Photo-imageable liquids", positive and negative tone, a lineup
"compatible with various exposure sources, including EUV (MOR), EUV
(CAR), ArF, KrF, i-line, and g-line", and "multilayer materials"
(underlayers and topcoats). Used on the lithography materials material page.
Tier: cross-check (vendor statement).

**TOK-PRODUCTS** — Tokyo Ohka Kogyo Co., Ltd., *Semiconductor
Manufacturing Field*, products page, accessed 2026-09-13.
<https://www.tok.co.jp/eng/products/semiconductor-pre> Lists the
company's front-end products: "g/i-Line photoresists", "KrF excimer laser
photoresists", ArF and EUV photoresists, "Developer and Rinse Solutions",
"Thinners", "Stripping Solution" and "Adhesion Enhancing Materials". The
page's market-share figures are projections attributed to a market
research firm and are not used. Used on the lithography materials material page.
Tier: cross-check (vendor statement).

**MLI-TMAH** — Moses Lake Industries, *TMAH Aqueous Solutions*, product
page, accessed 2026-09-13.
<https://mlindustries.com/products/tmah-aqueous-solutions/> TMAH for
"photoresist developer, surface preparation, cleaning, and etching",
made by a "chlorine-free manufacturing method", with "metallic impurity
levels of <1000 ppt", "at concentrations of choice (in water) up to 25%,
and with or without surfactants", in IBCs, drums and bottles. Used on the
lithography materials material page. Tier: cross-check (vendor statement).

**MLI-ABOUT** — Moses Lake Industries, *About MLI*, company page,
accessed 2026-09-13. <https://mlindustries.com/about-mli/> "Founded in
1984 as a wholly owned subsidiary of Tama Chemicals"; a supplier of
chemicals for the semiconductor industry. Used on the lithography
materials material page. Tier: cross-check (company statement).

**SEMI-C46** — SEMI, *SEMI C46 — Guide for 25% Tetramethylammonium
Hydroxide*, SEMI Standards store listing (revision C46-0812, inactive),
accessed 2026-09-13.
<https://store-us.semi.org/products/c04600-semi-c46-guide-for-25-tetramethylammonium-hydroxide>
A "guide for a grade of 25% tetramethylammonium hydroxide", listing
proposed impurity limits; originally published in 1991. Used on the
lithography materials material page. Tier: deep dive (standard).

**SEMI-P5** — SEMI, *SEMI P5 — Specification for Pellicles*, SEMI
Standards store listing (revision P5-0416, reapproved 1221), accessed
2026-09-13.
<https://store-us.semi.org/products/p00500-semi-p5-specification-for-pellicles>
"covers the general requirements for pellicles used on photomasks or
reticles in photolithographic exposure systems", for broadband,
polychromatic or monochromatic exposure; first published 1986. Used on
the lithography materials material page. Tier: deep dive (standard).

**WIKI-HMDS** — Wikipedia, *Bis(trimethylsilyl)amine*
(hexamethyldisilazane).
<https://en.wikipedia.org/wiki/Bis(trimethylsilyl)amine> The compound and
its uses; "In photolithography, HMDS is often used as an adhesion promoter
for photoresists", best applied "from the gas phase on heated
substrates". Used on the lithography materials material page. Tier: high-level.

**WIKI-PGMEA** — Wikipedia, *Propylene glycol methyl ether acetate*.
<https://en.wikipedia.org/wiki/Propylene_glycol_methyl_ether_acetate>
PGMEA as "a commonly used solvent" in the semiconductor industry and
often "the most abundant airborne, molecular contamination (AMC) in
semiconductor cleanrooms". Used on the lithography materials material page. Tier:
high-level.

**DILL-1975** — F. H. Dill, W. P. Hornberger, P. S. Hauge and J. M. Shaw,
"Characterization of positive photoresist", *IEEE Transactions on
Electron Devices* **22**(7), 445–452 (1975).
<https://doi.org/10.1109/T-ED.1975.18159> Exposure described by the
optical parameters A, B and C and development by a rate function R(M).
Used on the lithography materials material page. Tier: deep dive.

**PACANSKY-1979** — J. Pacansky and J. R. Lyerla, "Photochemical
Decomposition Mechanisms for AZ-Type Photoresists", *IBM Journal of
Research and Development* **23**(1), 42–55 (1979).
<https://doi.org/10.1147/rd.231.0042> Infrared and ¹³C NMR study of
naphthoquinonediazide photolysis via a ketene to 3-indenecarboxylic acid
in air, or to esters in vacuum. Used on the lithography materials material page.
Tier: deep dive.

**KIM-1984** — D. J. Kim, W. G. Oldham and A. R. Neureuther,
"Development of positive photoresist", *IEEE Transactions on Electron
Devices* **31**(12), 1730–1736 (1984).
<https://doi.org/10.1109/T-ED.1984.21779> A development-rate model with
depth dependence over the full exposure range, and its measurement.
Used on the lithography materials material page. Tier: deep dive.

**ITO-1994** — H. Ito, G. Breyta, D. Hofer, R. Sooriyakumaran, K.
Petrillo and D. Seeger, "Environmentally stable chemical amplification
positive resist: principle, chemistry, contamination resistance, and
lithographic feasibility", *Journal of Photopolymer Science and
Technology* **7**(3), 433–447 (1994).
<https://doi.org/10.2494/photopolymer.7.433> The ESCAP resist, a
4-hydroxystyrene/t-butyl acrylate copolymer annealed above its glass
transition for resistance to airborne contamination and delay. Used on
the lithography materials material page. Tier: deep dive.

**HUANG-1994** — W.-S. Huang, R. W. Kwong, A. D. Katnani and M.
Khojasteh, "Evaluation of a new environmentally stable positive tone
chemically amplified deep-UV resist", *Proc. SPIE* **2195**, 37 (1994).
<https://doi.org/10.1117/12.175370> A positive DUV resist resilient to
airborne bases, with stable linewidth after more than 24 hours between
exposure and develop. Used on the lithography materials material page. Tier: deep
dive.

**HERSHEL-1981** — R. Hershel, "Pellicle Protection Of Integrated
Circuit (IC) Masks", *Proc. SPIE* **0275**, Semiconductor
Microlithography VI, 23–28 (1981). <https://doi.org/10.1117/12.931869>
The mask-protection problem and the optical requirements of pellicles
for projection systems. Used on the lithography materials material page. Tier:
deep dive.

**WANG-2013-TMAH** — Y. Wang, Z. Zhang, C. Jiang and T. Xu,
"Electrodialysis Process for the Recycling and Concentrating of
Tetramethylammonium Hydroxide (TMAH) from Photoresist Developer
Wastewater", *Industrial & Engineering Chemistry Research* **52**(51),
18356–18361 (2013). <https://doi.org/10.1021/ie4023995> Recovery and
concentration of TMAH from developer wastewater by electrodialysis. Used
on the lithography materials material page. Tier: deep dive.

**PAT-ARC-BREWER** — J. W. Arnold, T. L. Brewer and S. Punyakumleard
(Brewer Science), *Anti-reflective coating*, US 4,910,122 A, priority
1982-09-30, granted 1990-03-20.
<https://patents.google.com/patent/US4910122A/en> A dyed polymer layer
under the resist that absorbs reflected light and fills small
depressions. Used on the lithography materials material page. Tier: deep dive.

**PAT-RESIST-TOK** — H. Kohara, H. Tanaka, M. Miyabe, Y. Arai, S. Asaumi
and T. Nakayama (Tokyo Ohka Kogyo), *Positive-working naphthoquinone
diazide photoresist composition with two cresol novolac resins*,
US 4,731,319 A, priority 1985-08-09, granted 1988-03-15.
<https://patents.google.com/patent/US4731319A/en> A DNQ resist with two
cresol novolacs differing in molecular weight and m-/p-cresol ratio.
Used on the lithography materials material page. Tier: deep dive.

**PAT-EBR-CLARIANT** — W. C. Nelson and O. Lehar (Clariant Finance
(BVI)), *Use of mixtures of ethyl lactate and N-methyl pyrollidone as an
edge bead remover for photoresists*, US 5,814,433 A, priority 1996-05-17,
granted 1998-09-29. <https://patents.google.com/patent/US5814433A/en> An
ethyl lactate–NMP edge-bead remover with a flash point above 38 °C, for
backside and topside use. Used on the lithography materials material page. Tier:
deep dive.

**PAT-THINNER-SAMSUNG** — M.-S. Jeon, C.-D. Lee and B.-Y. Lee (Samsung
Electronics), *Rework method utilizing thinner for wafers in
manufacturing of semiconductor devices*, US 6,159,646 A, priority
1997-09-04, granted 2000-12-12.
<https://patents.google.com/patent/US6159646A/en> Ethyl lactate,
ethyl-3-ethoxy propionate and γ-butyrolactone thinners for edge and
backside rinse and for rework. Used on the lithography materials material page.
Tier: deep dive.

#### Sputter targets (first cited there)

**SOLSTICE-TARGETS** — Solstice Advanced Materials, *PVD Sputtering
Targets and Coil Sets*, brochure 7610006-esm-sls-sputtering-targets
(08/26), accessed 2026-09-13.
<https://www.solstice.com/content/dam/advancedmaterials/solstice/events/semicon-tw-2026/sputtering-targets.pdf>
Current specifications for Cu and CuMn (ECAE and diffusion-bonded), Al
and Al alloy (AlCu and AlSiCu at "99.99% (4N)-99.9995% (5N5)", with grain
size and precipitate size by design), Ti (4N5, 5N, 5N5), powder-metallurgy
WTi ("3N~4N8", density "Above 99%"), W, Mo and Ru targets with diffusion,
"Nano" or indium bonding, and Ti, Cu and Ta coils that "support ion metal
plasma sputtering technology". Used on the sputter targets material page.
Tier: cross-check (vendor statement).

**SOLSTICE-HISTORY** — Solstice Advanced Materials, *Solstice Advanced
Materials: History and Brand Transition*, company page, accessed
2026-09-13.
<https://www.solstice.com/us/en/about-us/solstice-advanced-materials-history-and-brand-transition>
Solstice "was created through the spin-off of the former Advanced
Materials business of Honeywell International Inc.", announced on
2024-10-08 and completed on 2025-10-30; the business had worked on
"electronic materials" among other products. Does not name Honeywell
Electronic Materials, Inc. Used on the sputter targets material page.
Tier: cross-check (company statement).

**JX-SEMI-TARGETS** — JX Advanced Metals Corporation, *Sputtering Target
(PVD) for Semiconductor*, product page, accessed 2026-09-13.
<https://www.jx-nmm.com/english/products/sputtering/semiconductor_st/>
Titanium targets "widely used ... such as barrier layers for Al
interconnects, and hard masks" at "4N5 (Ti 99.995% or above) 5N 5N5",
with fine-grain and sputter-ready finishes against particles and
burn-in; 6N copper, tantalum, sintered tungsten with diffusion bonding;
and Ti, Cu and Ta coils and parts sets for Applied Materials chambers as
"an officially authorized supplier". Used on the sputter targets material
page. Tier: cross-check (vendor statement).

**JX-SPUTTERING** — JX Advanced Metals Corporation, *What Is
Sputtering?*, sputtering targets page, accessed 2026-09-13.
<https://www.jx-nmm.com/english/products/sputtering/about_sputtering.html>
A short explanation: the target "is bombarded with argon ions", emits
atoms that form the film, and "is the object of the ion bombardment when
sputtering takes place". Used on the sputter targets material page.
Tier: high-level.

**ASTM-F1512** — ASTM International, *F1512-94(2011) Standard Practice
for Ultrasonic C-Scan Bond Evaluation of Sputtering Target-Backing Plate
Assemblies* (withdrawn 2020), catalogue page; read from the Wayback
Machine capture of 2025-01-14 because the live site refused the request.
<https://www.astm.org/f1512-94r11.html>,
<https://web.archive.org/web/20250114231553/https://www.astm.org/f1512-94r11.html>
The significance statement: the target–backing plate bond "is a critical
reliability element in a sputter deposition system", needs high thermal
conductivity and shear strength, and may otherwise fail with
"catastrophic separation of the target from the backing plate". Used on
the sputter targets material page. Tier: deep dive (standard).

**ASTM-F3166** — ASTM International, *F3166-16 Standard Specification for
High-Purity Titanium Sputtering Target Used for Through-Silicon Vias
(TSV) Metallization* (withdrawn 2023), catalogue page; read from the
Wayback Machine capture of 2025-01-17.
<https://www.astm.org/f3166-16.html>,
<https://web.archive.org/web/20250117070227/https://www.astm.org/f3166-16.html>
The scope lists target "purity, grain size, inner quality, bonding,
dimension, and appearance" requirements, with qualification test
methods. Used on the sputter targets material page. Tier: deep dive
(standard).

**LEYBOVICH-1993** — A. Leybovich and T. Kuniya, "Effects of aluminum
sputtering target surface grain relief and crystallographic orientation
on sputtering I–V characteristics", *Journal of Vacuum Science &
Technology A* **11**(4), 1553–1557 (1993).
<https://doi.org/10.1116/1.578504> Single-crystal and polycrystalline
Al–Si and Al–Cu targets: orientation and surface relief both change the
magnetron I–V characteristics. Used on the sputter targets material page.
Tier: deep dive.

**WICKERSHAM-2001** — C. E. Wickersham, J. E. Poole, A. Leybovich and L.
Zhu, "Measurements of the critical inclusion size for arcing and
macroparticle ejection from aluminum sputtering targets", *Journal of
Vacuum Science & Technology A* **19**(6), 2767–2772 (2001).
<https://doi.org/10.1116/1.1403719> A critical Al₂O₃ inclusion size of
440 ± 160 µm for arcing in aluminium targets, independent of power
density. Used on the sputter targets material page. Tier: deep dive.

**WATERMAN-1990** — E. Waterman, J. Dunlop and T. Brat, "Tungsten-titanium
sputtering target processing effects on particle generation and thin
film properties for VLSI applications", *Proc. Seventh International
IEEE VLSI Multilevel Interconnection Conference (VMIC 1990)*,
pp. 329–331. <https://doi.org/10.1109/VMIC.1990.127887> W–Ti targets made
three ways: manufacturing technique and purity change film defect
density. Used on the sputter targets material page. Tier: deep dive.

**PAT-TARGET-TEXTURE-PRAXAIR** — A. C. Perry, P. S. Gilman and J. Van den
Sype (Praxair S.T. Technology), *Textured-metastable aluminum alloy
sputter targets and method of manufacture*, US 6,605,199 B2, filed
2001-11-14, granted 2003-08-12.
<https://patents.google.com/patent/US6605199B2/en> Aluminium alloy
targets with at least 35 % (200) orientation and grains below 5 µm,
made by deforming a blank cooled below −50 °C. Used on the sputter
targets material page. Tier: deep dive.

**PAT-TARGET-BOND-MRC** — T. J. Hunt and P. S. Gilman (Materials Research
Corp. and Sony Corp.), *Sputter target/backing plate assembly and method
of making same*, US 5,836,506 A, filed 1995-04-21, granted 1998-11-17.
<https://patents.google.com/patent/US5836506A/en> Bonding a target to a
backing plate by roughening or drilling one bonding surface, then heating
and pressing in a controlled atmosphere. Used on the sputter targets
material page. Tier: deep dive.

**PAT-TARGET-BOND-JAPANENERGY** — T. Ohhashi, H. Fukuyo, I. Sawamura, K.
Nakamura, A. Fukushima and M. Nagasawa (Japan Energy Corp.), *Sputtering
target assembly having solid-phase bonded interface*, US 5,693,203 A,
priority 1992-09-29, granted 1997-12-02.
<https://patents.google.com/patent/US5693203A/en> Low-temperature
solid-phase bonding of target and backing plate that preserves the
target's microstructure and orientation. Used on the sputter targets
material page. Tier: deep dive.

**PAT-TARGET-PROFILE-GENUS** — D. R. Boys (Genus), *Composite sputtering
target structures and process for producing such structures*,
US 5,215,639 A, priority 1984-10-09, granted 1993-06-01.
<https://patents.google.com/patent/US5215639A/en> A target whose back is
profiled to its known end-of-life erosion shape, bonded to a matching
backing plate by isostatic pressing. Used on the sputter targets material
page. Tier: deep dive.

#### Substrates and test wafers (first cited there)

**SEMI-M24** — SEMI, *SEMI M24 — Specification for Polished
Monocrystalline Silicon Premium Wafers*, SEMI Standards store listing
(revision M24-0612, inactive), accessed 2026-09-13.
<https://store-us.semi.org/products/m02400-semi-m24-specification-for-polished-monocrystalline-silicon-premium-wafers>
The listing's abstract: requirements "for virgin silicon premium wafers
with nominal diameter from 150–300 mm used for particle counting, metal
contamination monitoring, and measuring pattern resolution in the
photolithography process", with "tighter specification values in some
specific items for the specific usage" than a prime wafer. Used on the
substrates material page. Tier: cross-check (standard).

**SEMI-M38** — SEMI, *SEMI M38 — Specification for Polished Reclaimed
Silicon Wafers*, SEMI Standards store listing (revision M38-0312,
reapproved 1023, current), accessed 2026-09-13.
<https://store-us.semi.org/products/m03800-semi-m38-specification-for-polished-reclaimed-silicon-wafers>
The abstract "divides reclaimed wafers into four application categories:
Mechanical, Furnace, Particle, and Lithography", includes requirements
for "devices in the 180 and 130 nm technology generations", and cautions
against sources "with unknown thermal histories, unknown bulk
contamination, or unknown deposits". Used on the substrates material
page. Tier: cross-check (standard).

**GW-PRODUCTS** — GlobalWafers, *Products*, product page, accessed
2026-09-13. <https://www.gw-semi.com/products/> Application tables and
product descriptions: the "prime polished wafer" as "Our principal
product"; MDZ wafers "with built-in denuding and nucleation"; argon
annealed wafers with a "COP-free surface zone"; "Test and Monitor
Wafers", which "are substantially the same as prime polished wafers with
respect to cleanliness, and in some cases flatness" while "other
specifications are generally less rigorous"; and CMOS substrate
resistivities "from a low of about 5 mohm-cm on heavily doped epi
substrates to a high of around 30 ohm-cm on polished wafers". Does not
name SkyWater. Used on the substrates material page. Tier: cross-check
(vendor statement).

**GW-HOME** — GlobalWafers, *Silicon Wafer Manufacturing*, home page,
accessed 2026-09-13. <https://www.gw-semi.com/> States "we serve 100% of
the top 25 customers in the semiconductor industry". Used on the
substrates material page. Tier: cross-check (vendor statement).

**SEH-PRODUCTS** — SEH America, *Products*, product page, accessed
2026-09-13. <https://sehamerica.com/products/> Polished wafers "in
orientations <100>, <111>, and <110>" with boron or phosphorus; a 200 mm
range of "standard CZ polished wafers, COP free polished wafers, epi
wafers of all types, argon annealed wafers, FZ wafers" and SOI; epitaxial
"P/P-, P/P+, N/N-, and N/N+ wafers"; nitrogen-doped, argon-annealed
wafers. Does not name SkyWater. Used on the substrates material page.
Tier: cross-check (vendor statement).

**ENTEGRIS-SUPERSIC** — Entegris, Inc., *SUPERSiC® Silicon Carbide:
Products for semiconductor front end processes*, brochure 6116, accessed
2026-09-13.
<https://www.entegris.com/content/dam/shared-product-assets/specialty-shared/brochure-supersic-semiconductor-front-end-6116.pdf>
Silicon carbide converted from graphite, with contamination "typically
below 5 ppm"; horizontal-furnace carriers, "baffle assemblies", "LTO
cages" and pickup tools; SiC dummy and baffle wafers that "can be cleaned
and reused indefinitely in LPCVD or diffusion processes" (200 mm, "0.724
mm" thick); and the statement that "It is still common for silicon dummy
wafers to be made from reclaimed Si material". Used on the substrates
material page. Tier: cross-check (vendor statement).
Also used on the hardware consumables material page.

**KAO-2021** — I. Kao and C. Chung, *Wafer Manufacturing: Shaping of
Single Crystal Silicon Wafers*, Wiley, 2021, ISBN 978-0-470-06121-3.
<https://doi.org/10.1002/9781118696224> A textbook on the wafering
chain: slicing, lapping, grinding, polishing and wafer metrology (chapter
titles in Crossref). Used on the substrates material page. Tier:
high-level.

**POPOVICH-1997** — S. B. Popovich, S. R. Chilton and B. Kilgore,
"Implementation of a test wafer inventory tracking system to increase
efficiency in monitor wafer usage", *ASMC 97*, pp. 440–443.
<https://doi.org/10.1109/ASMC.1997.630777> Abstract: manufacturers
"spend millions of dollars annually on the purchase of test wafers",
used "to qualify tools, monitor processes, and develop new process
techniques"; many "use reclaim to polish off the top surface"; Motorola
MOS12's system tracks and forces internal reuse. Used on the substrates
material page. Tier: deep dive.

**OZELKAN-2006** — E. C. Ozelkan and M. Cakanyildirim, "Test Wafer
Management for Semiconductor Manufacturing", *IEEE Transactions on
Semiconductor Manufacturing* **19**(2), 241–251 (2006).
<https://doi.org/10.1109/TSM.2006.873401> A network model for buying,
downgrading and holding test wafers, whose "yearly TW costs add up to
several million dollars for a typical semiconductor fab". Used on the
substrates material page. Tier: deep dive.

**WATANABE-1999** — A. Watanabe, T. Kobayashi, T. Egi and T. Yoshida,
"Continuous and independent monitor wafer reduction in DRAM fab", *ISSM
1999*, pp. 303–306. <https://doi.org/10.1109/ISSM.1999.808796> Abstract:
more vendor-reclaimed wafers, in-house recycling and fewer measurements
cut "the ratio of monitor wafer to wafer start" from "1.5 (1993) to 0.5
(1999)". Used on the substrates material page. Tier: deep dive.

**FARUQI-2008** — A. Faruqi, R. Goss, D. Adhikari and T. Kowtsch, "Test
Wafer Management and Automated Wafer Sorting", *ASMC 2008*, pp. 322–326.
<https://doi.org/10.1109/ASMC.2008.4529062> An automated test-wafer
management and sorting system for a 300 mm fab. Used on the substrates
material page. Tier: deep dive.

**DONG-2024** — X. Dong, S. Mukherjee, M. Asokan, Y. Yang and V.
Duvvuru, "In-house Test Wafer Reclaim for Fab Cost and Wastage
Reduction", *ASMC 2024*, pp. 1–7.
<https://doi.org/10.1109/ASMC61125.2024.10545463> Micron's in-house
reclaim of test wafers with CMP and wet processes that "met with the
global reclaim specifications". Used on the substrates material page.
Tier: deep dive.

#### CMP consumables (first cited there)

**ENTEGRIS-CMC-2022** — Entegris, Inc., *CMC Materials | July 2022*,
acquisition information page, accessed 2026-09-13.
<https://www.entegris.com/en/home/brands/cmc-materials-july-2022.html>
Entegris and CMC Materials announced the acquisition on 2021-12-15 and
"The close of the transaction was announced on July 6, 2022"; CMC
Materials' "leading CMP slurries and pads" join Entegris' "liquid
filtration, post-CMP cleaning chemistries and brushes, CMP pad
conditioners, chemical monitoring, and chemical packaging products"; CMC's
"CMP Slurries, CMP Pads, and Electronic Chemicals businesses" form the
Advanced Planarization Solutions division. Names neither "CMC Chemicals,
Inc.", KMG Chemicals nor SkyWater. Used on the CMP consumables material
page. Tier: cross-check (company statement).
Also used on the hardware consumables material page.

**ENTEGRIS-POST-CMP** — Entegris, Inc., *Semiconductor Cleaning
Solutions*, post-CMP cleaning solutions product page, accessed
2026-09-13.
<https://www.entegris.com/en/home/products/chemistries/specialty-chemicals/post-cmp-cleaning-solutions/semiconductor-cleaning-solutions.html>
"We offer a complete range of solutions for the post chemical mechanical
planarization (Post-CMP) cleaning process", with "excellent corrosion
control, surface contamination removal"; the PlanarClean® and ESC
families. Used on the CMP consumables material page. Tier: cross-check
(vendor statement).

**WIKI-ENTEGRIS** — Wikipedia, *Entegris*.
<https://en.wikipedia.org/wiki/Entegris> "In July 2022, Entegris acquired
another U.S. semiconductor chemicals company, CMC Materials Inc.", which
was "previously known as Cabot Microelectronics Corp". Used on the CMP
consumables material page. Tier: high-level.

**QNITY-CMP-PADS** — Qnity Electronics, *CMP Pads*, product page,
accessed 2026-09-13. <https://www.qnityelectronics.com/cmp-pads.html>
An application chart of the company's pad lines: "IC1000™" listed for
copper bulk, tungsten, STI/ceria and oxide polishing, "Politex™,
Politex™ AT" for buff polishing, with the Ikonic™, Visionpad™,
Optivision™ and Emblem™ families. Does not name SkyWater. Used on the
CMP consumables material page. Tier: cross-check (vendor statement).

**QNITY-STORY** — Qnity Electronics, *Our story*, company page, accessed
2026-09-13. <https://www.qnityelectronics.com/our-story.html> FAQ: DuPont
"is targeting November 1, 2025, to complete the separation of its
Electronics business with the intention to create a new independent,
publicly traded company, Qnity Electronics, Inc.". Used on the CMP
consumables material page. Tier: cross-check (company statement).

**PAT-PAD-RODEL** — H. F. Reinhardt, J. V. H. Roberts, H. G. McClain,
W. D. Budinger and E. W. Jensen (Rodel Inc.), *Polymeric polishing pad
containing hollow polymeric microelements*, US 5,578,362 A, priority
1992-08-19, granted 1996-11-26.
<https://patents.google.com/patent/US5578362A/en> Abstract: "a polymeric
matrix impregnated with a plurality of polymeric microelements, each
polymeric microelement having a void space therein", whose work surface
"may be continuously regenerated" as it is abraded, for "polishing or
planarizing a semiconductor device". Used on the CMP consumables
material page. Tier: deep dive.

**KAKIREDDY-2010** — R. Kakireddy, A. Galpin, J. Smith and D. Slutz,
"Effects of CMP Pad Conditioner Properties and Performance on Polishing
Pad, Process and Wafer Removal Rate", *ECS Transactions* **33**(10),
157–163 (2010). <https://doi.org/10.1149/1.3489056> Abstract: diamond
"shape, size, density and protrusion" set "pad cut rate, pad surface
roughness and wafer removal rate"; uneven diamonds "exhibited high drop
in pad cut rate and wafer removal rate"; diamonds found "missing or
sheared off". Used on the CMP consumables material page. Tier: deep
dive.

**CASTILLO-MEJIA-2004** — D. Castillo-Mejia, J. Kelchner and S.
Beaudoin, "Polishing Pad Surface Morphology and Chemical Mechanical
Planarization", *Journal of The Electrochemical Society* **151**(4), G271
(2004). <https://doi.org/10.1149/1.1649751> A Greenwood–Williamson model
of the pad asperity layer that improves removal-rate and uniformity
prediction against a commercial CMP system. Used on the CMP consumables
material page. Tier: deep dive.

**KIM-2002-CERIA** — S.-D. Kim, I.-S. Hwang, H.-M. Park, J.-K. Rhee and
C.-W. Nam, "Chemical mechanical polishing of shallow trench isolation
using the ceria-based high selectivity slurry for sub-0.18 μm
complementary metal–oxide–semiconductor fabrication", *Journal of Vacuum
Science & Technology B* **20**(3), 918–923 (2002).
<https://doi.org/10.1116/1.1475984> Abstract: with a CeO₂ high-selectivity
slurry, variations of remaining pad nitride and field-oxide erosion "are
significantly reduced to ∼150 and ∼400 Å"; scratches, "∼80% of the total
defect", minimised by in-situ filtering, which improved the gate-oxide
integrity of MOS capacitors. Used on the CMP consumables material page.
Tier: deep dive.

**BENNETT-2014** — J. Bennett and M. A. Fury, "Correlation of large
particle count data in CMP slurry with production wafer defects", *ICPT
2014*, pp. 50–53. <https://doi.org/10.1109/ICPT.2014.7017243> A
SlurryScope at the point of use and in the slurry distribution loop of a
production fab: "A strong correlation was found between defects and the
total particle count in the smallest (1.0-1.2μm) particle bin". Used on
the CMP consumables material page. Tier: deep dive.

**LAI-2003** — C. L. Lai and S. H. Lin, "Electrocoagulation of chemical
mechanical polishing (CMP) wastewater from semiconductor fabrication",
*Chemical Engineering Journal* **95**(1–3), 205–211 (2003).
<https://doi.org/10.1016/S1385-8947(03)00106-2> Treatment of CMP waste
water by electrocoagulation (no abstract in Crossref or OpenAlex; the
annotation rests on the title). Used on the CMP consumables material
page. Tier: deep dive.

#### Anneal ambients (first cited there)

**WIKI-FLAMMABILITY** — Wikipedia, *Flammability limit*.
<https://en.wikipedia.org/wiki/Flammability_limit> Table of flammability
limits in air; the hydrogen row gives a lower limit of 4 % and an upper
limit of 75 % by volume. Used on the anneal ambients material page.
Tier: high-level.

**XU-2008** — S. Xu and L. Diao, "Study of tungsten oxidation in
O₂/H₂/N₂ downstream plasma", *Journal of Vacuum Science & Technology A*
**26**(3), 360–364 (2008). <https://doi.org/10.1116/1.2897316>
Abstract: tungsten oxidises rapidly to WO₃ in an O₂ downstream plasma at
up to 300 °C; "oxidation can be reduced effectively by adding H2"; adding
N₂ lowers the efficiency of the hydrogen. Used on the anneal ambients
material page. Tier: deep dive.

#### Ultrapure water (first cited there)

**SEMI-F63** — SEMI, *SEMI F63 — Guide for Ultrapure Water Used in
Semiconductor Processing*, SEMI Standards store listing (revision
F63-1224, current), accessed 2026-09-13.
<https://store-us.semi.org/products/f06300-semi-f63-guide-for-ultrapure-water-used-in-semiconductor-processing>
The abstract: the guide may be used to set purchasing criteria for UPW
equipment, "To set the process control parameters for UPW-system
operation" and "To establish quality expectations for the supplied UPW";
"UPW is used extensively in the production of semiconductor devices for
all wet-processing steps (including wafer rinsing)"; written for
facilities making semiconductors "with line widths of 32 nm and smaller"
with IRDS UPW committee input. Used on the ultrapure water material page.
Tier: cross-check (standard).

**SEMI-F61** — SEMI, *SEMI F61 — Guide to Design and Operation of a
Semiconductor Ultrapure Water System*, SEMI Standards store listing
(revision F61-0521, current), accessed 2026-09-13.
<https://store-us.semi.org/products/f06100-semi-f61-guide-to-design-and-operation-of-a-semiconductor-ultrapure-water-system>
The abstract: "the engineering and component requirements for a UPW
system used in semiconductor manufacturing", for UPW and hot UPW systems,
used with SEMI F63 and F75. Used on the ultrapure water material page.
Tier: cross-check (standard).

**ASTM-D5127** — ASTM International, *D5127-13(2018) Standard Guide for
Ultra-Pure Water Used in the Electronics and Semiconductor Industries*
(active), catalogue page; read from the Wayback Machine capture of
2024-09-17 (the live page refuses automated requests).
<https://www.astm.org/d5127-13r18.html>
<https://web.archive.org/web/20240917021043/https://www.astm.org/d5127-13r18.html>
"Significance and Use": the guide "recommends the water quality required
for the electronics and microelectronics industries"; "The types of
ultra-pure water are defined with respect to device line width"; the
recommendations "apply at the point of distribution". Used on the
ultrapure water material page. Tier: cross-check (standard).

**WIKI-UPW** — Wikipedia, *Ultrapure water*.
<https://en.wikipedia.org/wiki/Ultrapure_water> Pretreatment, reverse
osmosis, degassing, UV and ion-exchange or electrodeionization polishing;
a semiconductor UPW table with resistivity ">18.18 MΩ·cm" and TOC
"<1 μg/L"; dissolved oxygen "<10 μg/L in the ultrapure rinse water";
advanced fabs "consuming several million gallons of UPW per day"; TOC
measured by oxidising organics to CO₂. Used on the ultrapure water
material page. Tier: high-level.

**WIKI-PURIFIED-WATER** — Wikipedia, *Purified water*.
<https://en.wikipedia.org/wiki/Purified_water> A table of laboratory
water standards in which ASTM D1193 Type I water has a resistivity of
18.2 MΩ·cm at 25 °C. Used on the ultrapure water material page. Tier:
high-level.

**LIBMAN-2015** — S. Libman, D. Wilcox and B. Zerfas, "Ultrapure Water
for Advance Semiconductor Manufacturing: Challenges and Opportunities",
*ECS Transactions* **69**(8), 17–28 (2015).
<https://doi.org/10.1149/06908.0017ecst> Abstract: killer particle size
near 10 nm, particles in UPW exceeding requirements, "hydrogen peroxide
generated in Ultraviolet treatment" and dissolved organics "either
originating from incoming city water or introduced by UPW system
materials". Used on the ultrapure water material page. Tier: deep dive.

**LI-2005** — F. Li, M. K. Balazs and S. Anderson, "Effects of Ambient
and Dissolved Oxygen Concentration in Ultrapure Water on Initial Growth
of Native Oxide on a Silicon (100) Surface", *Journal of The
Electrochemical Society* **152**(8), G669 (2005).
<https://doi.org/10.1149/1.1946487> Abstract: "the ambient and the
dissolved oxygen concentration in UPW dramatically affect the growth rate
of the native oxide" after HF cleaning. Used on the ultrapure water
material page. Tier: deep dive.

**YAGI-1992** — Y. Yagi, T. Imaoka, Y. Kasama and T. Ohmi, "Advanced
ultrapure water systems with low dissolved oxygen for native oxide free
wafer processing", *IEEE Transactions on Semiconductor Manufacturing*
**5**(2), 121–127 (1992). <https://doi.org/10.1109/66.136273> Abstract:
two UPW systems with membrane vacuum degassing plus catalytic reduction or
nitrogen bubbling supply "10 ppb or less in dissolved oxygen
concentration", with TOC, silica and residue at 1 ppb or less. Used on
the ultrapure water material page. Tier: deep dive.

**GAUDET-1984** — P. W. Gaudet, "Point-Of-Use Ultrafiltration of
Deionized Rinse Water and Effects on Microelectronics Device Quality", in
*Semiconductor Processing*, ASTM International, 1984,
ISBN 978-0-8031-0403-7, pp. 184–197. <https://doi.org/10.1520/STP32652S>
Abstract: control of "colloidal particles of 0.2 micron and smaller" in
critical rinses by point-of-use ultrafiltration. Used on the ultrapure
water material page. Tier: deep dive.

**CARTWRIGHT-1985** — P. S. Cartwright, "Total Effluent Treatment and
Rinse Water Reclamation in a Semiconductor Device Manufacturing
Facility", *Water Science and Technology* **17**(2–3), 325–336 (1985).
<https://doi.org/10.2166/wst.1985.0141> Abstract: "over 90% of the rinse
water is purified back to 18 megohm/cm quality for reuse", with toxic
chemicals precipitated as sludge. Used on the ultrapure water material
page. Tier: deep dive.

**NAKATA-2016** — K. Nakata, T. Fukui and T. Nagai, "Particle adsorption
onto Si wafers in ultrapure water; its mechanism and effect of carbon
dioxide", *ISSM 2016*, pp. 1–4. <https://doi.org/10.1109/ISSM.2016.7934544>
A model of particle adsorption onto silicon in UPW from spin-cleaning and
impurity experiments. Used on the ultrapure water material page. Tier:
deep dive.

#### Hardware consumables and abatement (first cited there)

**HERAEUS-TUBES** — Heraeus Covantics, *Fused Quartz and Silica Tubes for
Semiconductor Applications*, product page, accessed 2026-09-13.
<https://www.heraeus-covantics.com/products-and-solutions/products-by-shape/tubes/fused-quartz-and-silica-tubes-for-semiconductor-applications>
Tubes "needed in the semiconductor industry for the manufacturing of
batch processing equipment used in CVD, Diffusion and Annealing tools",
serving "as chemically pure reaction chambers, as gas or liquid inlets or
as transportation pipes"; electrically fused HSQ®100 to HSQ®330S grades,
stabilised HSQ®400 "to reduce the possibility of sagging at elevated
working temperatures" and synthetic HSQ®900 of "parts per billion class
purity". Used on the hardware consumables material page. Tier:
cross-check (vendor statement).

**SKW-CERTS** — SkyWater Technology, *Certifications & Policies*, company
page, accessed 2026-09-13.
<https://www.skywatertechnology.com/certifications-policies/> Lists for
SkyWater Minnesota "ISO9001", "AS9100", "IATF16949", "ISO13485" and
"ISO14004 Environmental Management system"; for SkyWater Texas
"ISO14001 Environmental Management System" among others. Used on the
hardware consumables material page. Tier: cross-check (SkyWater
statement).

**MPCA-2025** — Minnesota Pollution Control Agency, *SkyWater Technology
fined more than $97,000 for violations with their air permit, federal
regulations and Minnesota rules*, news release, 2025-02-04, accessed
2026-09-13.
<https://www.pca.state.mn.us/news-and-stories/skywater-technology-fined-more-than-97000-for-air-permit-violations>
SkyWater "was fined $97,130 for operating without an air permit" at its
Bloomington semiconductor plant; violations include "Taking credit for
greenhouse gas emissions control equipment that was not allowed in
permit"; SkyWater "has taken corrective action
and has submitted a complete permit application". Used on the hardware
consumables material page. Tier: cross-check (regulator statement).

**EISELE-1978** — K. M. Eisele and R. Ruthardt, "Stabilized Fused-Quartz
Tubes with Reduced Sodium Diffusion for Semiconductor Device Technology",
*Journal of The Electrochemical Society* **125**(7), 1188–1190 (1978).
<https://doi.org/10.1149/1.2131646> Stabilised quartz furnace tubes that
pass less sodium (no abstract in Crossref or OpenAlex; the annotation
rests on the title). Used on the hardware consumables material page.
Tier: deep dive.

**JOUBERT-2004** — O. Joubert, G. Cunge, B. Pelissier, L. Vallier, M.
Kogelschatz and E. Pargon, "Monitoring chamber walls coating deposited
during plasma processes: Application to silicon gate etch processes",
*Journal of Vacuum Science & Technology A* **22**(3), 553–563 (2004).
<https://doi.org/10.1116/1.1697484> Abstract: wall layers "cause large
and uncontrolled shifts in the etch process"; an XPS technique with a
floating Al₂O₃ sample on a 200 mm wafer shows silicon oxychloride wall
layers in HBr/Cl₂/O₂, changed by CF₄ and by resist on the wafer. Used on
the hardware consumables material page. Tier: deep dive.

**ITO-2008** — N. Ito, T. Moriya, F. Uesugi, M. Matsumoto, S. Liu and Y.
Kitayama, "Reduction of Particle Contamination in Plasma-Etching
Equipment by Dehydration of Chamber Wall", *Japanese Journal of Applied
Physics* **47**(5R), 3630 (2008). <https://doi.org/10.1143/JJAP.47.3630>
Abstract: AlF₃ particles formed from the "coating material Al2O3 on the
etching chamber wall" with fluorine and adsorbed water in WSi/poly
etching, suppressed by plasma dehydration of chamber parts. Used on the
hardware consumables material page. Tier: deep dive.

**PAT-YTTRIA** — J. Y. Sun, S. J. Wu, S. Thach, A. H. Kumar, R. W. Wu,
H. Wang, Y. Lin and C. C. Stow, *Yttrium oxide based surface coating for
semiconductor IC processing vacuum chambers*, US 6,776,873 B1, filed
2002-02-14, granted 2004-08-17.
<https://patents.google.com/patent/US6776873B1/en> Abstract: "a
ceramic-based surface coating, high purity yttrium oxide coating" on
anodised aluminium chamber parts "against fluorine and oxygen plasma
attack". Google Patents lists the assignee as "Individual". Used on the
hardware consumables material page. Tier: deep dive.

**FIALA-1999** — A. Fiala, M. Kiehlbauch, S. Mahnovski and D. B. Graves,
"Model of point-of-use plasma abatement of perfluorinated compounds with
an inductively coupled plasma", *Journal of Applied Physics* **86**(1),
152–162 (1999). <https://doi.org/10.1063/1.370711> Abstract: a high
density plasma "between the process tool turbomolecular pump and the
backing pump", with oxygen added, converts PFCs "to products that can be
scrubbed downstream of the backing pump"; a C₂F₆/O₂ model. Used on the
hardware consumables material page. Tier: deep dive.

**HU-2018** — S.-C. Hu, A. Shiue, W.-T. Tseng and G. Leggett,
"Perfluorocompound Emissions Control and Kinetic Characteristics in
Point-of-Use Wet-Thermal-Wet Abatement of Plasma-Enhanced Chemical Vapor
Deposition Chamber Cleaning", *IEEE Transactions on Semiconductor
Manufacturing* **31**(2), 302–308 (2018).
<https://doi.org/10.1109/TSM.2018.2808173> Electric thermal oxidation of
NF₃ from PECVD chamber cleans in wet-thermal-wet point-of-use abatement,
with first-order kinetics against NF₃ and N₂ flow and temperature. Used
on the hardware consumables material page. Tier: deep dive.

**MANGYOU-2005** — H. Mangyou, N. Watanabe, K. Hattori, T. Watanabe, Y.
Sugimori, K. Shibuya and S. Hasaka, "High performance atmospheric plasma
abatement system for PFC reduction", *ISSM 2005*, pp. 263–266.
<https://doi.org/10.1109/ISSM.2005.1513352> Abstract: a microwave
atmospheric plasma abatement system for a single oxide etcher or PECVD
tool that treats "up to 80 L/min of CF4 exhaust with 95% of DRE" at
5.9 kW. Used on the hardware consumables material page. Tier: deep dive.

**JOHNSON-2004** — A. D. Johnson, R. G. Ridgeway and P. J. Maroulis,
"Reduction of PFC emissions to the environment through advances in CVD
and etch processes", *IEEE Transactions on Semiconductor Manufacturing*
**17**(4), 491–496 (2004). <https://doi.org/10.1109/TSM.2004.835700>
Abstract: two strategies for reducing PFC emissions from CVD chamber
cleaning and plasma etch while improving process performance. Used on
the hardware consumables material page. Tier: deep dive.

**SHERER-2005** — J. M. Sherer, *Semiconductor Industry: Wafer Fab
Exhaust Management*, CRC Press, 2005.
<https://doi.org/10.1201/9781420027198> Exhaust types, point-of-use
devices, exhaust lines, central acid and ammonia wet scrubbers, VOC
control and emergency releases (book description in OpenAlex). Used on
the hardware consumables material page. Tier: high-level.

**ROGGEI-1999** — A. Roggei and K. Seshan, "Reduction of probe to pad
contact resistance: technology development targeted for cost
effectiveness Pentium II(R) processors testing", *ISSM 1999*,
pp. 217–219. <https://doi.org/10.1109/ISSM.1999.808775> Abstract: probing
problems from "resistance increase between probes and pads during the
probing process" removed by a fab process improvement at Intel. Used on
the hardware consumables material page. Tier: deep dive.

**HORII-2010** — N. Horii, M. Kamide, A. Inouye and N. Kuzuu,
"Crystallization of silica glass upon heating by contact with a NaCl
crystal grain", *Journal of the Ceramic Society of Japan* **118**(1376),
318–320 (2010). <https://doi.org/10.2109/jcersj2.118.318> Abstract: silica
glasses of various types crystallised where heated in contact with a NaCl
grain, the depth of the crystallised region proportional to the square
root of heating time, with an Arrhenius dependence that bends at about
1000 °C. Used on the hardware consumables material page. Tier: deep dive.

**HSU-2007** — J.-N. Hsu, C.-J. Tsai, C. Chiang and S.-N. Li, "Silane
Removal at Ambient Temperature by Using Alumina-Supported Metal Oxide
Adsorbents", *Journal of the Air & Waste Management Association*
**57**(2), 204–210 (2007). <https://doi.org/10.1080/10473289.2007.10465309>
Abstract: copper, zinc and cerium oxide adsorbents on alumina "had a
removal efficiency >99.9% for SiH4 before breakthrough", mixed oxides
having the greater capacity. Used on the hardware consumables material
page. Tier: deep dive.

**HSU-2010** — J.-N. Hsu, H. Bai, S.-N. Li and C.-J. Tsai, "Copper Loaded
on Sol-Gel-Derived Alumina Adsorbents for Phosphine Removal", *Journal of
the Air & Waste Management Association* **60**(5), 629–635 (2010).
<https://doi.org/10.3155/1047-3289.60.5.629> Abstract: phosphine, "commonly
used for semiconductor and optoelectronic industries", which "local
scrubbers must immediately abate"; copper on sol-gel gamma-alumina
adsorbed 18 mg PH₃ per gram and could be regenerated by air purging.
Used on the hardware consumables material page. Tier: deep dive.

**WIKI-ISO14000** — Wikipedia, *ISO 14000 series*, accessed 2026-09-13.
<https://en.wikipedia.org/wiki/ISO_14000_series> ISO 14001 as "the core
set of standards used by organizations for designing and implementing an
effective environmental management system"; its list of the series
gives "ISO 14001 Environmental management systems - Requirements with
guidance for use" and "ISO 14004 Environmental management systems -
General guidelines on implementation". Used on the hardware consumables
material page. Tier: high-level.

**WIKI-GWP** — Wikipedia, *Global warming potential*, accessed
2026-09-13. <https://en.wikipedia.org/wiki/Global_warming_potential>
Tables of GWPs: IPCC Sixth Assessment Report values at 20, 100 and 500
years, and "Earlier values from 2007" from the IPCC Fourth Assessment
Report at 100 years, in which hexafluoroethane (PFC-116) is 12,200 and
nitrogen trifluoride 17,200. Used on the hardware consumables material
page. Tier: high-level.

#### Process gases (first cited there)

**SEMI-C3** — SEMI, *SEMI C3 — Specification for Gases*, SEMI Standards
store listing (revision C3-0317), accessed 2026-09-13.
<https://store-us.semi.org/products/c00300-semi-c3-specification-for-gases>
The listing's abstract: the Gases Committee "establishes the
definitions, general procedures, specifications, and analytical
procedures for the gases listed in the index"; the specifications "are
intended to serve for gases to be used in the manufacture and processing
of semiconductors and advanced electronic devices and circuits";
"originally published in 1981". Used on the process gases material page.
Tier: cross-check (standard).

**SEMI-C59** — SEMI, *SEMI C59 — Specification for Nitrogen*, SEMI
Standards store listing (revision C59-0317), accessed 2026-09-13.
<https://store-us.semi.org/products/c05900-semi-c59-specification-for-nitrogen>
"a series of specifications for different grades of nitrogen (N2) that
are used in the semiconductor industry"; covers "all grades of nitrogen
used in the semiconductor industry". Used on the process gases material
page. Tier: cross-check (standard).

**SEMI-C54** — SEMI, *SEMI C54 — Specification for Oxygen (O2)*, SEMI
Standards store listing (revision C54-0624), accessed 2026-09-13.
<https://store-us.semi.org/products/c05400-semi-c54-specification-for-oxygen>
"a series of specifications for different grades of oxygen (O2)";
references SEMI C3.22, C3.23 and "SEMI C3.41 — Standard for Oxygen (O2),
Bulk, 99.9998% Quality". Used on the process gases material page. Tier:
cross-check (standard).

**SEMI-C58** — SEMI, *SEMI C58 — Specification for Hydrogen*, SEMI
Standards store listing (revision C58-1116), accessed 2026-09-13.
<https://store-us.semi.org/products/c05800-semi-c58-specification-for-hydrogen>
Specifications for grades of hydrogen; covers "two grades of hydrogen
used in the semiconductor industry". Used on the process gases material
page. Tier: cross-check (standard).

**SEMI-C3-20** — SEMI, *SEMI C3.20 — Specification for Helium (He), in
Cylinders, 99.9995%*, SEMI Standards store listing (revision C3.20-0414
(Reapproved 0319)E), accessed 2026-09-13.
<https://store-us.semi.org/products/c00320-semi-c3-20-specification-for-helium-he-in-cylinders-99-9995>
"specifications for helium (He) that is used in the semiconductor
industry". Used on the process gases material page. Tier: cross-check
(standard).

**EPA-GHGRP-SKYWATER** — U.S. Environmental Protection Agency,
Greenhouse Gas Reporting Program, Envirofacts tables `PUB_DIM_FACILITY`
and `PUB_FACTS_SUBP_GHG_EMISSION` for facility ID 1000354 (Bloomington,
Minnesota; "SKYWATER TECHNOLOGY FOUNDRY INC" for 2010–2013 and
"SKYWATER TECHNOLOGY INC" from 2014), reporting years 2010–2023,
retrieved 2026-09-13.
<https://data.epa.gov/efservice/PUB_DIM_FACILITY/FACILITY_ID/1000354/JSON>
<https://data.epa.gov/efservice/PUB_FACTS_SUBP_GHG_EMISSION/FACILITY_ID/1000354/SUB_PART_ID/43/JSON>
<https://data.epa.gov/efservice/pub_dim_facility/facility_name/CONTAINING/SKYWATER/JSON>
Public regulatory data (retrieved through the Envirofacts web service).
The facility table gives reported subparts "C" for 2010 and "C,I" for
2011–2023, NAICS 334413, and parent company "Cypress Semiconductor
Corporation (100%)" or "CYPRESS SEMICONDUCTOR CORP (100%)" for 2010–2016,
"SKYWATER TECHNOLOGY FOUNDRY INC (100%)" for 2017–2019, "OXBOW INDUSTRIES
LLC (100%)" for 2020–2022 and "SkyWater Technology Inc (100%)" for 2023;
the facility name field reads "SKYWATER TECHNOLOGY FOUNDRY INC" for
2010–2013 and "SKYWATER TECHNOLOGY INC" for 2014–2023, later names
applied to the Cypress years, and the address is "2401 E. 86TH ST.". The
emissions table gives, for subpart I (subpart ID 43, "Electronics
Manufacture"), CO₂-equivalent values by gas group for each year
2011–2023: for 2023, PFCs 47106.6, HFCs 6112.6, SF₆ 2302.8, other fully
fluorinated GHGs 2141, NF₃ 1441.36, N₂O 185.058, HFEs 82.1; PFCs were
101763.7 in 2011. The tables do not give individual gases, processes or
tools. Used on the process gases material page. Tier: cross-check
(regulatory filing data).
Also used on the etch and chamber-clean gases material page.
Also used on the hardware consumables material page, which notes that
the records name no abatement system.
Also used on the materials index page (the public basis section and the
N₂O/NO, SF₆ and NF₃ rows).

**EPA-GHGRP-SUBPART-I** — U.S. Environmental Protection Agency,
*Electronics Manufacturing: Subpart I, Greenhouse Gas Reporting
Program*, information sheet, December 2024, accessed 2026-09-13.
<https://www.epa.gov/system/files/documents/2024-04/i_electronics_infosheet_2024.pdf>
Defines the source category (plasma etching and chamber cleaning with
"plasma-generated fluorine (F2) atoms", wafer cleaning, "Processes in
which the chemical vapor deposition (CVD) process or other production
processes use nitrous oxide (N2O)", and fluorinated heat transfer
fluids); facilities report "Fluorinated GHG emissions from electronic
manufacturing production processes and HTF use", "N2O emissions from
CVD and other production processes" and "Controlled emissions of GHGs
from abatement systems, if applicable"; per-fab reporting by process
type; a facility "must determine the total annual emissions of each
fluorinated GHG emitted", "including each input gas and each by-product
gas"; and an "Inventory and description of all abatement systems" for
which destruction or removal efficiency is claimed. Used on the process
gases material page. Tier: cross-check (regulatory guidance).
Also used on the etch and chamber-clean gases material page.
Also used on the hardware consumables material page.
Also used on the materials index page.

**NIOSH-HCL** — National Institute for Occupational Safety and Health,
*NIOSH Pocket Guide to Chemical Hazards: Hydrogen chloride*, CDC; read
from the Wayback Machine capture of 2025-12-29 (the CDC site refused the
project's user agent).
<https://www.cdc.gov/niosh/npg/npgd0332.html>
<https://web.archive.org/web/20251229130832/https://www.cdc.gov/niosh/npg/npgd0332.html>
IDLH "50 ppm"; NIOSH REL "C 5 ppm (7 mg/m3)"; OSHA PEL "C 5 ppm (7
mg/m3)"; "Colorless to slightly yellow gas with a pungent, irritating
odor. [Note: Shipped as a liquefied compressed gas.]". Used on the
process gases material page. Tier: cross-check (safety data).

**NIOSH-NO** — National Institute for Occupational Safety and Health,
*NIOSH Pocket Guide to Chemical Hazards: Nitric oxide*, CDC; read from
the Wayback Machine capture of 2025-12-07.
<https://www.cdc.gov/niosh/npg/npgd0448.html>
<https://web.archive.org/web/20251207003006/https://www.cdc.gov/niosh/npg/npgd0448.html>
IDLH "100 ppm"; NIOSH REL and OSHA PEL "TWA 25 ppm (30 mg/m3)";
"Colorless gas. [Note: Shipped as a nonliquefied compressed gas.]". Used
on the process gases material page. Tier: cross-check (safety data).

**LINDE-SEMI** — Linde, *Supporting digitalization with gases for
semiconductors*, industry page (Linde US), accessed 2026-09-13.
<https://www.lindeus.com/industries/electronics/semiconductors>
Vendor statement: "Linde provides wafer fabs worldwide with
ultra-high-purity gases and chemicals, specialty equipment, and
customized services"; "Linde's extensive global network of bulk gas
production plants ensures a reliable supply of ultra-high-purity
nitrogen (N₂), oxygen (O₂), argon (Ar), hydrogen (H₂), helium (He), and
carbon dioxide (CO₂) in the volumes required". Does not name SkyWater.
Used on the process gases material page. Tier: cross-check (vendor
statement).

**LINDE-ENG-ELECTRONICS** — Linde Engineering, *Serving the Electronics
Industry Worldwide*, industry page, accessed 2026-09-13.
<https://www.linde-engineering.com/industries/electronics>
Vendor statement: gases "such as nitrogen (N2), oxygen (O2), argon (Ar),
helium (He), carbon dioxide (CO2) and hydrogen (H2) plus a host of
electronics specialty gases and mixtures support processes as diverse as
deposition, etching, doping and chamber cleaning"; bulk delivery "by
road tanker or ISO container"; SPECTRA on-site plants "deliver ultra-pure
gaseous and liquid N2 and O2 with less than 1 part per billion (ppb)
impurities"; NITRON E plants for "less exacting purity requirements (100
ppb)"; "High-purity hydrogen (H2) is often supplied in liquid form for
low-volume electronics applications"; on-site fluorine generators as a
replacement for NF₃, ClF₃ and SF₆ in chamber cleaning. Does not name
SkyWater. Used on the process gases material page. Tier: cross-check
(vendor statement).
Also used on the etch and chamber-clean gases material page.

**KRIEGLER-1972** — R. J. Kriegler, Y. C. Cheng and D. R. Colton, "The
Effect of HCl and Cl₂ on the Thermal Oxidation of Silicon", *Journal of
The Electrochemical Society* **119**(3), 388 (1972).
<https://doi.org/10.1149/1.2404208> A few mole per cent of HCl or Cl₂ in
dry oxidation (30 min at 1150 °C) improves electrical stability, reduces
mobile ions and interface states, increases the oxidation rate, and HCl
in O₂ cleans quartz tubes. Used on the process gases material page.
Tier: deep dive.

**YONEDA-1995** — K. Yoneda, K. Hagiwara, H. Oishi and Y. Todokoro, "The
Dielectric Breakdown Characteristics of Thin Silicon Dioxide Prepared by
trans-1,2-Dichloroethylene Added Oxidation", *Journal of The
Electrochemical Society* **142**(12), 4304–4309 (1995).
<https://doi.org/10.1149/1.2048502> trans-1,2-DCE as a substitute for
1,1,1-trichloroethane in gate oxidation, with lower ozone depletion
potential and improved breakdown reliability; 5 wt % recommended. Used
on the process gases material page. Tier: deep dive.

**HWANG-1990** — H. Hwang, W. Ting, B. Maiti, D.-L. Kwong and J. Lee,
"Electrical characteristics of ultrathin oxynitride gate dielectric
prepared by rapid thermal oxidation of Si in N₂O", *Applied Physics
Letters* **57**(10), 1010–1011 (1990).
<https://doi.org/10.1063/1.103550> About 60 Å oxynitride grown in N₂O by
rapid thermal oxidation, with higher charge-to-breakdown than RTO oxide
and a nitrogen-rich layer at the interface. Used on the process gases
material page. Tier: deep dive.

**TOBIN-1994** — P. J. Tobin, Y. Okada, S. A. Ajuria, V. Lakhotia, W. A.
Feil and R. I. Hegde, "Furnace formation of silicon oxynitride thin
dielectrics in nitrous oxide (N₂O): The role of nitric oxide (NO)",
*Journal of Applied Physics* **75**(3), 1811–1817 (1994).
<https://doi.org/10.1063/1.356374> In a 950 °C furnace N₂O decomposes to
N₂, O₂ and NO before the wafers; nitrogen incorporation follows the NO
concentration, which depends on gas residence time. Used on the process
gases material page. Tier: deep dive.

**OKADA-1994** — Y. Okada, P. J. Tobin, K. G. Reid, R. I. Hegde, B. Maiti
and S. A. Ajuria, "Furnace grown gate oxynitride using nitric oxide
(NO)", *IEEE Transactions on Electron Devices* **41**(9), 1608–1613
(1994). <https://doi.org/10.1109/16.310113> Gate oxynitride grown in NO,
with nitrogen near the interface and a much lower thermal budget than an
N₂O process. Used on the process gases material page. Tier: deep dive.

**LEE-1981-CORROSION** — W.-Y. Lee, J. M. Eldridge and G. C. Schwartz,
"Reactive ion etching induced corrosion of Al and Al-Cu films", *Journal
of Applied Physics* **52**(4), 2994–2999 (1981).
<https://doi.org/10.1063/1.329043> Al and Al–Cu lines etched in chlorine
plasmas corrode rapidly in air; carbon and chlorine contamination,
damage and copper enrichment contribute; a thermal oxidation restores the
protective oxide. Label ↔ key note: the key carries a suffix because
LEE-1981 is another source. Used on the process gases material page.
Tier: deep dive.
Also used on the etch and chamber-clean gases material page.

**OHMI-1993** — T. Ohmi, "ULSI reliability through ultraclean
processing", *Proceedings of the IEEE* **81**(5), 716–729 (1993).
<https://doi.org/10.1109/5.220903> The three principles of ultraclean
technology (wafer surface, processing environment, process-parameter
control) and their application to oxidation, epitaxy and metallisation.
Used on the process gases material page. Tier: deep dive.

**GOODMAN-2008** — D. L. Goodman, "Effect of wafer bow on electrostatic
chucking and back side gas cooling", *Journal of Applied Physics*
**104**(12), 124902 (2008). <https://doi.org/10.1063/1.3043843> A model
and measurements of the wafer bow an electrostatic chuck can clamp and
the backside gas pressure it can then hold. Used on the process gases
material page. Tier: deep dive.

**WIKI-NITROGEN** — Wikipedia, *Nitrogen*.
<https://en.wikipedia.org/wiki/Nitrogen> Production ("fractional
distillation of liquid air, or by mechanical means using gaseous air"),
uses and the asphyxiation hazard. Used on the process gases material
page. Tier: high-level.

**WIKI-OXYGEN** — Wikipedia, *Oxygen*.
<https://en.wikipedia.org/wiki/Oxygen> Production by air separation and
hazards; "The NFPA 704 standard rates compressed oxygen gas as
nonhazardous to health, nonflammable, and nonreactive, but an oxidizer".
Used on the process gases material page. Tier: high-level.

**WIKI-HYDROGEN** — Wikipedia, *Hydrogen*.
<https://en.wikipedia.org/wiki/Hydrogen> Properties, uses and hazards;
"Hydrogen gas forms explosive mixtures with air in concentrations from
4%–74%". Used on the process gases material page. Tier: high-level.

**WIKI-ARGON** — Wikipedia, *Argon*.
<https://en.wikipedia.org/wiki/Argon> Production as a by-product of
cryogenic air separation, use "for sputter deposition of thin films as in
microelectronics", and the asphyxiation hazard. Used on the process gases
material page. Tier: high-level.

**WIKI-HELIUM** — Wikipedia, *Helium*.
<https://en.wikipedia.org/wiki/Helium> Extraction from natural gas,
industrial uses and the history of shortages. Used on the process gases
material page. Tier: high-level.

**WIKI-AIR-SEPARATION** — Wikipedia, *Air separation*.
<https://en.wikipedia.org/wiki/Air_separation> Cryogenic and membrane air
separation; "High purity oxygen, nitrogen, and argon, used for
semiconductor device fabrication, require cryogenic distillation". Used
on the process gases material page. Tier: high-level.

**WIKI-N2O** — Wikipedia, *Nitrous oxide*.
<https://en.wikipedia.org/wiki/Nitrous_oxide> Properties; "At elevated
temperatures, nitrous oxide is a powerful oxidiser similar to molecular
oxygen". Used on the process gases material page. Tier: high-level.

**WIKI-NO** — Wikipedia, *Nitric oxide*.
<https://en.wikipedia.org/wiki/Nitric_oxide> Properties and hazards (the
infobox classes it "Very toxic, corrosive, oxidizer"). Used on the
process gases material page. Tier: high-level.

**WIKI-DCE** — Wikipedia, *1,2-Dichloroethylene*.
<https://en.wikipedia.org/wiki/1,2-Dichloroethylene> The cis and trans
isomers; "trans-1,2-DCE has applications including electronics cleaning,
precision cleaning, and certain metal cleaning applications". Used on the
process gases material page. Tier: high-level.

**WIKI-PRAXAIR** — Wikipedia, *Praxair*.
<https://en.wikipedia.org/wiki/Praxair> Company history; "In 2018 it
merged with Linde AG to form Linde plc". Does not mention SkyWater. Used
on the process gases material page. Tier: high-level.

**WIKI-AIRGAS** — Wikipedia, *Airgas*.
<https://en.wikipedia.org/wiki/Airgas> "Airgas, an Air Liquide company,
is an American supplier of industrial, medical and specialty gases";
acquired by Air Liquide after a 2015 agreement. Used on the process gases
material page. Tier: high-level.

**WIKI-VERSUM** — Wikipedia, *Versum Materials*.
<https://en.wikipedia.org/wiki/Versum_Materials> "On October 3, 2016, Air
Products & Chemicals completed the corporate spin-off of the company";
"In October 2019, Merck Group acquired the company"; its products include
"ultra-thin dielectric and metal precursors of film" and "delivery
equipment for the semiconductor industry". Used on the process gases
material page. Tier: high-level.
Also used on the dopant gases and implant sources material page.

#### Dopant gases and implant sources (first cited there)

**SEMI-C3-6** — SEMI, *SEMI C3.6 — Specification for Phosphine (PH3) in
Cylinders, 99.98% Quality*, SEMI Standards store listing (revision
C3.6-0421), accessed 2026-09-13.
<https://store-us.semi.org/products/c00306-semi-c3-6-specification-for-phosphine-ph3-in-cylinders-99-98-quality>
"specifications for phosphine (PH3) that are used in the semiconductor
industry"; revision history from "SEMI C3.6-81 (first published)". Used
on the dopant gases and implant sources material page. Tier: cross-check
(standard).

**SEMI-C3-2** — SEMI, *SEMI C3.2 — Specification for Arsine (AsH3) in
Cylinders, 99.94% Quality*, SEMI Standards store listing (revision
C3.2-0611 (Reapproved 0218)), accessed 2026-09-13.
<https://store-us.semi.org/products/c00302-semi-c3-2-specification-for-arsine-ash3-in-cylinders-99-94-quality>
"specifications for arsine (AsH3) that is used in the semiconductor
industry"; "originally published in 1992". Used on the dopant gases and
implant sources material page. Tier: cross-check (standard).

**SEMI-C3-27** — SEMI, *SEMI C3.27 — Specification for Boron Trifluoride
(BF3) in Cylinders, 99.0% Quality*, SEMI Standards store listing
(revision C3.27-1102 (Reapproved 0118)), accessed 2026-09-13.
<https://store-us.semi.org/products/c00327-semi-c3-27-specification-for-boron-trifluoride-bf3-in-cylinders-99-0-quality>
"a specification for boron trifluoride (BF3) used in the semiconductor
industry"; "originally published in 1984". Used on the dopant gases and
implant sources material page. Tier: cross-check (standard).

**NIOSH-ARSINE** — National Institute for Occupational Safety and
Health, *NIOSH Pocket Guide to Chemical Hazards: Arsine*, CDC; read from
the Wayback Machine capture of 2025-11-30.
<https://www.cdc.gov/niosh/npg/npgd0040.html>
<https://web.archive.org/web/20251130093607/https://www.cdc.gov/niosh/npg/npgd0040.html>
IDLH "Ca [3 ppm]"; NIOSH REL "Ca C 0.002 mg/m3 [15-minute]"; OSHA PEL
"TWA 0.05 ppm (0.2 mg/m3)"; "Colorless gas with a mild, garlic-like
odor. [Note: Shipped as a liquefied compressed gas.]". Used on the dopant
gases and implant sources material page. Tier: cross-check (safety
data).

**NIOSH-PHOSPHINE** — National Institute for Occupational Safety and
Health, *NIOSH Pocket Guide to Chemical Hazards: Phosphine*, CDC; read
from the Wayback Machine capture of 2025-11-30.
<https://www.cdc.gov/niosh/npg/npgd0505.html>
<https://web.archive.org/web/20251130140523/https://www.cdc.gov/niosh/npg/npgd0505.html>
IDLH "50 ppm"; NIOSH REL "TWA 0.3 ppm (0.4 mg/m3) ST 1 ppm (1 mg/m3)";
"Shipped as a liquefied compressed gas". Used on the dopant gases and
implant sources material page. Tier: cross-check (safety data).

**NIOSH-BF3** — National Institute for Occupational Safety and Health,
*NIOSH Pocket Guide to Chemical Hazards: Boron trifluoride*, CDC; read
from the Wayback Machine capture of 2026-01-15.
<https://www.cdc.gov/niosh/npg/npgd0062.html>
<https://web.archive.org/web/20260115022425/https://www.cdc.gov/niosh/npg/npgd0062.html>
IDLH "25 ppm"; NIOSH REL and OSHA PEL "C 1 ppm (3 mg/m3)"; "Colorless gas
with a pungent, suffocating odor. [Note: Forms dense white fumes in moist
air. Shipped as a nonliquefied compressed gas.]". Used on the dopant gases
and implant sources material page. Tier: cross-check (safety data).

**EMD-ION-X** — EMD Electronics (Merck KGaA, Darmstadt), *ION-X® BF3 —
Boron Trifluoride ION-X® Dopant Gas Storage and Delivery System*,
product page, accessed 2026-09-13.
<https://www.emdgroup.com/en/expertise/semiconductors/offering/isotopically-enriched-bf3.html>
Vendor statement: "Isotopically Enriched BF3"; "ION-X® is used for the
safe storage and delivery of sub-atmospheric dopant gases such as arsine,
phosphine and boron trifluoride"; "With its Metal-Organic Framework
(MOF), ION-X® can selectively adsorb, store and safely deliver ultra-high
purity gases at sub-atmospheric pressures". Does not name SkyWater. Used
on the dopant gases and implant sources material page. Tier: cross-check
(vendor statement).

**ENTEGRIS-IMPLANT-GASES** — Entegris, *Specialty Gases and Delivery
Systems for Ion Implantation*, industry-insights page, accessed
2026-09-13.
<https://www.entegris.com/en/home/resources/industry-insights/specialty-gases-and-delivery-systems-for-ion-implantation.html>
Vendor statement: Entegris pioneered "the Safe Delivery Source® (SDS®)
package over 30 years ago", which "provides subatmospheric gas storage
and delivery for ion implant dopant materials"; the fourth generation
(SDS4) was qualified with "SDS4 phosphine (PH3) and SDS4 arsine (AsH3)
cylinders" on production implanters. Does not name SkyWater. Used on the
dopant gases and implant sources material page. Tier: cross-check (vendor
statement).

**OLANDER-2000** — W. K. Olander, M. Donatucci, J. Mayer and L. Wang,
"Vacuum actuated gas delivery", *2000 International Conference on Ion
Implantation Technology Proceedings*, pp. 722–725.
<https://doi.org/10.1109/IIT.2000.924255> The Vacuum Actuated Cylinder:
sub-atmospheric delivery of dopant fluorides through a pressure-control
device inside the cylinder that opens only when the manifold is below a
preset pressure. Used on the dopant gases and implant sources material
page. Tier: deep dive.

**MCKEE-2002** — D. J. McKee and L. J. Van Horn, "Evaluation and
integration of a new gas source package for boron trifluoride used in ion
implantation", *Proc. 14th International Conference on Ion Implantation
Technology* (2002), pp. 424–427. <https://doi.org/10.1109/IIT.2002.1258031>
A production test at Agere Systems of an ATMI VAC package for BF₃ on an
Axcelis GSD200E implanter. Used on the dopant gases and implant sources
material page. Tier: deep dive.

**HAM-2017** — S. Ham, C. Yoon, S. Kim, J. Park, O. Kwon, J. Heo, D.
Park, S. Choi, S. Kim, K. Ha and W. Kim, "Arsenic Exposure during
Preventive Maintenance of an Ion Implanter in a Semiconductor
Manufacturing Factory", *Aerosol and Air Quality Research* **17**(4),
990–999 (2017). <https://doi.org/10.4209/aaqr.2016.07.0310> Airborne and
bulk arsenic during implanter maintenance, highest for medium-current
tools. Used on the dopant gases and implant sources material page. Tier:
deep dive.

**MOMIYAMA-1999** — Y. Momiyama, S. Yamaguchi, S. Ohkubo and T. Sugii,
"Indium tilted channel implantation technology for 60 nm nMOSFET",
*1999 Symposium on VLSI Technology, Digest of Technical Papers*, pp.
67–68. <https://doi.org/10.1109/VLSIT.1999.799343> A tilted indium channel
implant with a steeper lateral profile than boron and no reliability
penalty. Used on the dopant gases and implant sources material page.
Tier: deep dive.

**WIKI-INDUSTRIAL-GAS** — Wikipedia, *Industrial gas*.
<https://en.wikipedia.org/wiki/Industrial_gas> Production and supply of
industrial gases; "Toxic or flammable gas cylinders are often stored by
end users in gas cabinets for protection from external fire or from any
leak". Used on the dopant gases and implant sources material page. Tier:
high-level.
Also used on the precursors material page.

#### Precursors (first cited there)

**SEMI-C3-55** — SEMI, *SEMI C3.55 — Specification for Silane (SiH4),
Bulk, 99.994% Quality*, SEMI Standards store listing (revision C3.55-1011
(Reapproved 0218)), accessed 2026-09-13.
<https://store-us.semi.org/products/c00355-semi-c3-55-specification-for-silane-sih4-bulk-99-994-quality>
"specifications for silane (SiH4) that is used in the semiconductor
industry"; covers "requirements for bulk silane (SiH4)"; "originally
published February 2000". Used on the precursors material page. Tier:
cross-check (standard).

**SEMI-C3-12** — SEMI, *SEMI C3.12 — Specification for Ammonia (NH3) in
Cylinders, 99.998% Quality*, SEMI Standards store listing (revision
C3.12-0116 (Reapproved 0922)), accessed 2026-09-13.
<https://store-us.semi.org/products/c00312-semi-c3-12-specification-for-ammonia-nh3-in-cylinders-99-998-quality>
"specification for ammonia (NH3) that is used in the semiconductor
industry"; revision history from "SEMI C3.12-83 (first published)". Used
on the precursors material page. Tier: cross-check (standard).

**SEMI-C70** — SEMI, *SEMI C70 — Specification for Tungsten Hexafluoride
(WF6)*, SEMI Standards store listing (revision C70-0924), accessed
2026-09-13.
<https://store-us.semi.org/products/c0700-semi-c70-specification-for-tungsten-hexafluoride>
"specifications for tungsten hexafluoride (WF6) that are used in the
semiconductor industry"; first published as C70-0611. Used on the
precursors material page. Tier: cross-check (standard).

**NIOSH-NH3** — National Institute for Occupational Safety and Health,
*NIOSH Pocket Guide to Chemical Hazards: Ammonia*, CDC; read from the
Wayback Machine capture of 2026-01-08.
<https://www.cdc.gov/niosh/npg/npgd0028.html>
<https://web.archive.org/web/20260108051903/https://www.cdc.gov/niosh/npg/npgd0028.html>
IDLH "300 ppm"; NIOSH REL "TWA 25 ppm (18 mg/m3) ST 35 ppm (27 mg/m3)";
OSHA PEL "TWA 50 ppm (35 mg/m3)". Used on the precursors material page.
Tier: cross-check (safety data).

**NIOSH-DIBORANE** — National Institute for Occupational Safety and
Health, *NIOSH Pocket Guide to Chemical Hazards: Diborane*, CDC; read from
the Wayback Machine capture of 2026-01-22.
<https://www.cdc.gov/niosh/npg/npgd0183.html>
<https://web.archive.org/web/20260122103710/https://www.cdc.gov/niosh/npg/npgd0183.html>
IDLH "15 ppm"; REL and PEL "TWA 0.1 ppm (0.1 mg/m3)"; "[Note: Usually
shipped in pressurized cylinders diluted with hydrogen, argon, nitrogen,
or helium.]". Used on the precursors material page. Tier: cross-check
(safety data).

**BRITTON-1990** — L. G. Britton, "Combustion hazards of silane and its
chlorides", *Plant/Operations Progress* **9**(1), 16–38 (1990).
<https://doi.org/10.1002/prsb.720090107> Review and new experiments on
the combustion of silane and chlorosilanes, including sudden releases
into air, ignition sensitivity and flame acceleration. Used on the
precursors material page. Tier: deep dive.

**WIKI-DCS** — Wikipedia, *Dichlorosilane*.
<https://en.wikipedia.org/wiki/Dichlorosilane> "In its major use, it is
mixed with ammonia (NH3) in LPCVD chambers to grow silicon nitride in
semiconductor processing"; purity and toxicity. Used on the precursors
material page. Tier: high-level.

**WIKI-AMMONIA** — Wikipedia, *Ammonia*.
<https://en.wikipedia.org/wiki/Ammonia> Properties, production and
hazards; "regulated in the US as a non-flammable gas, but it meets the
definition of a material that is toxic by inhalation". Used on the
precursors material page. Tier: high-level.

**WIKI-OZONE** — Wikipedia, *Ozone*. <https://en.wikipedia.org/wiki/Ozone>
Properties, generation ("Ozone is produced in the corona discharge"),
toxicity "above concentrations of about 0.1 ppm" and catalytic
decomposition. Used on the precursors material page. Tier: high-level.

**WIKI-SIF4** — Wikipedia, *Silicon tetrafluoride*.
<https://en.wikipedia.org/wiki/Silicon_tetrafluoride> Properties; "This
volatile compound finds limited use in microelectronics and organic
synthesis"; infobox hazards "toxic, corrosive"; "It is fatal if
inhaled". Used on the precursors material page. Tier: high-level.

**WIKI-DIBORANE** — Wikipedia, *Diborane*.
<https://en.wikipedia.org/wiki/Diborane> "a highly toxic, colorless, and
pyrophoric gas"; investigated "for the p-doping of silicon
semiconductors". Used on the precursors material page. Tier: high-level.

#### Etch and chamber-clean gases (first cited there)

**SEMI-C3-40** — SEMI, *SEMI C3.40 — Specification for Carbon
Tetrafluoride (CF4), 99.997% Quality*, SEMI Standards store listing
(revision C3.40-1011 (Reapproved 0218)), accessed 2026-09-13.
<https://store-us.semi.org/products/c00340-semi-c3-40-specification-for-carbon-tetrafluoride-cf4-99-997-quality>
"specification for carbon tetrafluoride (CF4) that is used in the
semiconductor industry"; "originally published in 1989". Used on the etch
and chamber-clean gases material page. Tier: cross-check (standard).

**SEMI-C3-24** — SEMI, *SEMI C3.24 — Specification for Sulfur
Hexafluoride (SF6) in Cylinders, 99.97% Quality*, SEMI Standards store
listing (revision C3.24-0414 (Reapproved 0319)E), accessed 2026-09-13.
<https://store-us.semi.org/products/c00324-semi-c3-24-specification-for-sulfur-hexafluoride-sf6-in-cylinders-99-97-quality>
"specifications for sulfur hexafluoride (SF6) that is used in the
semiconductor industry". Used on the etch and chamber-clean gases material
page. Tier: cross-check (standard).

**NIOSH-CL2** — National Institute for Occupational Safety and Health,
*NIOSH Pocket Guide to Chemical Hazards: Chlorine*, CDC; read from the
Wayback Machine capture of 2025-11-30.
<https://www.cdc.gov/niosh/npg/npgd0115.html>
<https://web.archive.org/web/20251130134447/https://www.cdc.gov/niosh/npg/npgd0115.html>
IDLH "10 ppm"; NIOSH REL "C 0.5 ppm (1.45 mg/m3) [15-minute]"; OSHA PEL
"C 1 ppm (3 mg/m3)"; "Greenish-yellow gas with a pungent, irritating
odor. [Note: Shipped as a liquefied compressed gas.]"; incompatibilities
include hydrogen, ammonia and finely divided metals. Used on the etch and
chamber-clean gases material page. Tier: cross-check (safety data).

**NIOSH-HBR** — National Institute for Occupational Safety and Health,
*NIOSH Pocket Guide to Chemical Hazards: Hydrogen bromide*, CDC; read from
the Wayback Machine capture of 2025-11-30.
<https://www.cdc.gov/niosh/npg/npgd0331.html>
<https://web.archive.org/web/20251130093033/https://www.cdc.gov/niosh/npg/npgd0331.html>
IDLH "30 ppm"; NIOSH REL "C 3 ppm (10 mg/m3)"; "Colorless gas with a
sharp, irritating odor. [Note: Shipped as a liquefied compressed gas.]".
Used on the etch and chamber-clean gases material page. Tier: cross-check
(safety data).

**NIOSH-NF3** — National Institute for Occupational Safety and Health,
*NIOSH Pocket Guide to Chemical Hazards: Nitrogen trifluoride*, CDC; read
from the Wayback Machine capture of 2025-11-30.
<https://www.cdc.gov/niosh/npg/npgd0455.html>
<https://web.archive.org/web/20251130135138/https://www.cdc.gov/niosh/npg/npgd0455.html>
IDLH "1000 ppm"; NIOSH REL and OSHA PEL "TWA 10 ppm (29 mg/m3)";
"Colorless gas with a moldy odor. [Note: Shipped as a nonliquefied
compressed gas.]". Used on the etch and chamber-clean gases material page.
Tier: cross-check (safety data).

**EPA-GHGRP-FGAS** — U.S. Environmental Protection Agency, *Fluorinated
Greenhouse Gas Emissions and Supplies Reported to the GHGRP*, web page,
accessed 2026-09-13.
<https://www.epa.gov/ghgreporting/fluorinated-greenhouse-gas-emissions-and-supplies-reported-ghgrp>
"The five main types of fluorinated GHGs are hydrofluorocarbons (HFCs),
perfluorocarbons (PFCs), sulfur hexafluoride (SF6), nitrogen trifluoride
(NF3), and other fully fluorinated greenhouse gases"; electronics
manufacturers above the threshold must report; emissions are given in
metric tons of CO₂ equivalent ("about 7.6 million metric tons of carbon
dioxide equivalent (MMT CO2e)" for the non-production emitters in 2023);
the CO₂e figures "reflect the global warming potential (GWP) values from
Table A-1, which is generally based on the IPCC’s Fourth Assessment
Report (AR4), with the addition of GWPs from the IPCC’s Fifth Assessment
Report for fluorinated GHGs that did not have GWPs in the AR4". Used on
the etch and chamber-clean gases material page. Tier: cross-check
(regulatory data).

**CHAN-2004** — E. M. Chan, G. Loh and C. C. Allgood, "Process
Optimization and PFC Emission Reduction Using a c-C₄F₈ Chamber Cleaning
Process on a Novellus Concept 1 Dielectric PECVD Tool", *IEEE
Transactions on Semiconductor Manufacturing* **17**(4), 497–503 (2004).
<https://doi.org/10.1109/TSM.2004.835712> A production comparison in a
150 mm fab of an optimised C₂F₆ clean with c-C₄F₈ cleans on a TEOS PECVD
tool; the C₄F₈ recipes lowered gas use and PFC emissions. Used on the etch
and chamber-clean gases material page. Tier: deep dive.

**SELAMOGLU-1991** — N. Selamoglu, C. N. Bredbenner, T. A. Giniecki and
H. J. Stocker, "Tapered etching of aluminum with CHF₃/Cl₂/BCl₃ and its
impact on step coverage of plasma-deposited silicon oxide from
tetraethoxysilane", *Journal of Vacuum Science & Technology B* **9**(5),
2530–2535 (1991). <https://doi.org/10.1116/1.585687> Sidewall polymer from
CHF₃ tapers aluminium lines; taper grows with CHF₃ flow and falls with
Cl₂ flow, improving TEOS oxide step coverage. Used on the etch and
chamber-clean gases material page. Tier: deep dive.

**RIDGEWAY-1995** — R. G. Ridgeway, "Determination of emissions and
evaluation of abatement equipment for selected semiconductor processes",
*Proceedings of SEMI Advanced Semiconductor Manufacturing Conference and
Workshop* (1995), p. 89. <https://doi.org/10.1109/ASMC.1995.484346>
Summary of real-time analytical methods for unconsumed process gases,
by-products (HAPs and PFCs) and abatement effectiveness in production
fabs. Used on the etch and chamber-clean gases material page. Tier: deep
dive.

**WIKI-CF4** — Wikipedia, *Carbon tetrafluoride*.
<https://en.wikipedia.org/wiki/Carbon_tetrafluoride> Use "as a plasma
etchant for silicon, silicon dioxide, and silicon nitride"; "an
atmospheric lifetime of 50,000 years". Used on the etch and chamber-clean
gases material page. Tier: high-level.

**WIKI-SF6** — Wikipedia, *Sulfur hexafluoride*.
<https://en.wikipedia.org/wiki/Sulfur_hexafluoride> Properties, uses
including "a silicon etchant for semiconductor manufacturing", a GWP
"23,500 times greater" than CO₂ (citing the IPCC fifth assessment, AR5),
a GWP of 23,900 (citing the fourth assessment, AR4) and an atmospheric
lifetime "of around 3200 years". Used on the etch and chamber-clean
gases material page. Tier: high-level.

**WIKI-C4F8** — Wikipedia, *Octafluorocyclobutane*.
<https://en.wikipedia.org/wiki/Octafluorocyclobutane> "serves mainly as a
passivation layer material in etching processes". Used on the etch and
chamber-clean gases material page. Tier: high-level.

**WIKI-CH3F** — Wikipedia, *Fluoromethane*.
<https://en.wikipedia.org/wiki/Fluoromethane> "a non-toxic, liquefiable,
and flammable gas"; "used in semiconductor manufacturing processes as an
etching gas in plasma etch reactors". Used on the etch and chamber-clean
gases material page. Tier: high-level.

**WIKI-PFC** — Wikipedia, *Fluorocarbon* (the *Perfluorocarbon* title
redirects to it).
<https://en.wikipedia.org/wiki/Fluorocarbon> Properties of
fluorocarbons and an extract of IPCC fifth assessment lifetimes and
100-year GWPs (CF₄ 50,000 years and 6630; C₂F₆ 10,000 years and 11,100;
c-C₄F₈ 3200 years and 9540). Used on the etch and chamber-clean gases
material page. Tier: high-level.
Also used on the dielectric and nitride plasma etcher page.

### 8.21 Mask page sources

Sources introduced for the per-mask pages under `docs/masks/` that had
no entry above. Each label on those pages is the key below in lower case
and the citation is the one given in the page footnote; the entries are
grouped by the mask page that first cited the source, and sources
already listed above record their use on a mask page in an "Also used
on" line of their own. None of these sources mentions SkyWater, SKY130
or the Bloomington fab; they describe masks, mask making, lithography,
implantation, well engineering, CMP fill, multi-threshold and
high-voltage devices in general. Every URL was fetched on 2026-09-13 or
2026-09-14: papers and books were checked through Crossref
(bibliographic data) and OpenAlex (abstracts or tables of contents), and
their annotations rest on those. An entry's tier records its first use.

#### DNM mask page (first cited there)

**WONG-1998** — A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic effects
of mask critical dimension error", *Proc. SPIE* **3334**, 106 (1998).
<https://doi.org/10.1117/12.310718> Quantifies the mask error factor
(MEF) for lines and holes on chrome-on-glass, attenuated and alternating
phase-shift masks; the abstract: the MEF "is unity for large features,
but increases rapidly when the critical dimension (CD) is less than 0.5
(lambda) /NA for line-space patterns and 0.75 (lambda) /NA for
contacts", dark-field spaces are more sensitive than light-field lines,
and attenuated PSMs behave like chrome-on-glass masks. Used on the DNM
mask page. Tier: deep dive.
Also used on the FOM, LVTNM, NWM, HVTPM, PWBM, PWDEM, P1M, LICM1, LI1M,
CTM1, MM1, VIM, MM2 and VIM4 mask pages.

**RIZVI-2005** — S. Rizvi (ed.), *Handbook of Photomask Manufacturing
Technology*, CRC Press, 2005, ISBN 978-1-4200-2878-2.
<https://doi.org/10.1201/9781420028782> A reference volume whose
chapters cover mask data preparation, e-beam and laser mask writers,
conventional and advanced optical masks, mask substrates, resists and
processing, pellicles, metrology, inspection and repair. Used on the DNM
mask page. Tier: deep dive.
Also used on the FOM, P1M, LICM1, CTM1 and VIM4 mask pages.

**BUERGER-1999** — B. Buerger, U. Baetz, K.-D. Kunze and H. Wolf,
"Hierarchical mask data preparation and special fracturing techniques
in MGS", *Proc. SPIE* **3665**, 135 (1999).
<https://doi.org/10.1117/12.346217> A layout post-processor with a
fracturing engine for e-beam mask writers, and the two data-preparation
tasks it addresses: processing large, dense layouts and improving mask
quality by optimised fracturing. Used on the DNM mask page. Tier: deep
dive.

**HONG-1999** — S.-P. Hong, H.-S. Chun, J.-J. Kim, M.-G. Kang and
H.-S. Oh, "Fabrication of 0.22 μm triple well CMOS devices by using high
energy ion implantation", *Proc. IEEE Region 10 Conference (TENCON 99)*,
vol. 2, pp. 1106–1108 (1999).
<https://doi.org/10.1109/TENCON.1999.818617> A 0.22 µm triple-well CMOS
process with deep wells implanted at 1.5–2 MeV and an RTA; the triple
well gave better leakage, breakdown and latch-up immunity than a twin
well. Used on the DNM mask page. Tier: deep dive.

**VOLDMAN-2007** — S. H. Voldman, "CMOS Latchup Process Features and
Solutions – Dual-Well and Triple-Well CMOS", chapter 5 of *Latchup*,
Wiley, 2007, pp. 257–299, ISBN 978-0-470-01642-8.
<https://doi.org/10.1002/9780470516171.ch5> A book chapter on process
solutions to latch-up, with sections on n-wells, p-wells, isolation,
triple wells and high-dose buried layers. Used on the DNM mask page.
Tier: deep dive.

**ROSS-1996** — M. F. Ross, W. R. Livesay, V. Starov, K. Ostrowski and
S. Y. Wong, "Photoresist stabilization for ion implant processing",
*Proc. SPIE* **2724**, 632 (1996).
<https://doi.org/10.1117/12.241862> Flood electron-beam stabilisation
of three i-line resists for implant masking, which reduced post-implant
shrinkage and CD variation, improved thermal stability and eliminated
popping during resist removal. Used on the DNM mask page. Tier: deep
dive.
Also used on the LVTNM, NWM and HVTPM mask pages.

#### P1M mask page (first cited there)

**ARTHUR-1999** — G. G. Arthur and B. Martin, "Mask error factor and
critical dimension budgets for sub-half-micron CMOS processes", *Proc.
SPIE* **3677**, 918 (1999). <https://doi.org/10.1117/12.350880> A
PROLITH/2 simulation study of the mask error factor against pitch,
linewidth, OPC, focus, aberrations, partial coherence and resist, carried
through process windows and CD budgets to reticle procurement
specifications. Used on the P1M mask page. Tier: deep dive.
Also used on the LI1M mask page.

**KUIJTEN-1998** — J. P. Kuijten, F. Duray and T. der Kinderen, "Reticle
contributions to CD uniformity for 0.25-μm DUV lithography", *Proc.
SPIE* **3334**, 620 (1998). <https://doi.org/10.1117/12.310792> On an
ASML PAS 5500/300 DUV stepper, subtracts the reticle fingerprint from
intrafield CD data: a reticle CD error component of 10 nm (3σ), from
32 nm (3σ) mask CD uniformity and a reticle sensitivity factor of 1.3,
against an exposure-tool component of 8 nm (3σ) for 0.25 µm dense
lines. Used on the P1M mask page. Tier: deep dive.

**GAROFALO-1995** — J. G. Garofalo, J. DeMarco, J. Bailey, J. Xiao and
S. Vaidya, "Reduction of ASIC gate-level line-end shortening by mask
compensation", *Proc. SPIE* **2440**, 171–183 (1995).
<https://doi.org/10.1117/12.209250> Line-end shortening of transistor
geometries on ASIC gate levels, which "reduces the wafer process
latitude and in some cases even eliminates the level-to-level overlay
margin", and its reduction by mask compensation and modified
illumination. Used on the P1M mask page. Tier: deep dive.
Also used on the LI1M mask page.

**ZHENG-2003** — S. Zheng, G. Zhang, C. Wang and S. F. Detweiler,
"Characterization of optical proximity matching for 130-nm node gate
line width", *Proc. SPIE* **5040**, 894 (2003).
<https://doi.org/10.1117/12.485431> The error sources in matching one
OPC model for the gate line width through pitch across the exposure
field and across several scanners at the 130 nm node, measured by
scatterometry and correlated with lens aberration and partial-coherence
measurements. Used on the P1M mask page. Tier: deep dive.

#### VIM4 mask page (first cited there)

**KIM-1999** — H.-E. Kim, J.-S. Chun, S. Barnett and J. Shih, "Effect of
mask critical dimension error for subquarter-micron contact hole",
*Proc. SPIE* **3679**, 821 (1999). <https://doi.org/10.1117/12.354400>
Simulated and measured mask error factor for contact holes on binary and
attenuated phase-shift masks: about one for large features, rising
rapidly near the resolution limit, larger for dense than for isolated
contacts, and smaller on attenuated masks because of their positive mask
bias. Used on the VIM4 mask page. Tier: deep dive.
Also used on the LICM1, CTM1 and VIM mask pages.

**MORGANTE-2000** — C. G. Morgante and H. C. Hamaker, "ALTA 3700:
extending the application space of the ALTA 3500 laser reticle writer",
*Proc. SPIE* **4066**, 613 (2000). <https://doi.org/10.1117/12.392079>
Subsystem improvements, including a redesigned acousto-optic modulator,
that let the ALTA 3700 laser reticle writer "address the needs of
maskmakers in the 180 nm and 150 nm technology nodes", with
print-quality and throughput results. Used on the VIM4 mask page. Tier:
deep dive.

**BUCK-1994** — P. D. Buck and B. J. Grenon, "Comparison of wet and dry
chrome etching with the CORE-2564", *Proc. SPIE* **2087**, 42–49 (1994).
<https://doi.org/10.1117/12.167247> Chrome masks "have traditionally
been wet etched in an acidic solution of cerric ammonium nitrate"; the
isotropic etch undercuts the chrome by about 150 nm per edge, which is
compensated by sizing the data; wet and dry chrome etch compared on
plates printed with the CORE-2564. Used on the VIM4 mask page. Tier:
deep dive.

**FLACK-1993** — W. W. Flack, K. E. Tokunaga and K. D. Edwards, "Chrome
dry-etching for photomask fabrication", *Proc. SPIE* **1809**, 85
(1993). <https://doi.org/10.1117/12.142153> A chrome dry-etch process for
sub-half-micron reticle features, which "traditional wet etch is not
capable of successfully transferring", with its selectivity and process
sensitivities. Used on the VIM4 mask page. Tier: deep dive.

#### LICM1 mask page (first cited there)

**PDK-SUMMARY** — SkyWater PDK Authors, *Summary of Key Periphery Rules*,
SkyWater SKY130 PDK documentation, retrieved 2026-09-13.
<https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>,
<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/summary/table-f4-connectivity-of-drawn-and-mask.csv>.
Summary tables of widths, spacings and enclosures for the front-end and
back-end layers (Tables F3a–F3d; F3c, "Back end layers for S8D\* flow",
and F3d, "Back end layers for S8T\* flow", note "All enclosures in tables
are nominal and do not apply to butting edges or corners") and Table F4,
"Connectivity of Drawn and Mask Layers", which names the layer joining
each pair of conducting layers: "Licon1" from `li1` to diff and tap,
"Licon1 AND Npc" from `li1` to poly, "Mcon" from met1 to `li1` and "Via"
from met2 to met1. Used on the LICM1 mask page. Tier: cross-check.
Also used on the LI1M, CTM1, MM1, VIM and MM2 mask pages.

**CHOO-2000** — L. C. Choo, O. Park, M. J. Sack and S. C. Tam,
"Integration of attenuated phase-shift mask to 0.13-μm technology
contact level masking process", *Proc. SPIE* **4000**, Optical
Microlithography XIII, 1193 (2000). <https://doi.org/10.1117/12.388956>
Moving an attenuated-mask contact process from 0.22 µm holes (0.18 µm
technology, NA 0.68, k₁ 0.60) to 0.16 µm holes for a 0.13 µm
technology, "a low 0.44" in k₁: simulations favour isolated
holes, dense holes need higher mask transmission, and a 6 % attenuated
mask with 0.16, 0.18 and 0.20 µm hole patterns biased by 0.04, 0.06 and
0.08 µm was exposed at moderate and low partial coherence, with the
effect on the mask error enhancement factor discussed. Used on the LICM1
mask page. Tier: deep dive.
Also used on the CTM1 mask page.

#### LI1M mask page (first cited there)

**SHI-2002** — X. Shi, S. Hsu, J. F. Chen, C. M. Hsu, R. J. Socha and
M. V. Dusa, "Understanding the forbidden pitch phenomenon and assist
feature placement", *Proc. SPIE* **4689**, Metrology, Inspection, and
Process Control for Microlithography XVI, 985 (2002).
<https://doi.org/10.1117/12.473427> Shows that the change of a main
feature's CD and exposure latitude with its neighbours is a consequence
of light-field interference; "the forbidden pitch lies in the location
where the field produced by the neighboring features interferes with the
field of the main feature destructively", which gives a basis for
illumination design and scattering-bar placement. Used on the LI1M mask
page. Tier: deep dive.
Also used on the MM2 mask page.

**SEKIGUCHI-1998** — A. Sekiguchi, F. Uesawa, K. Takeuchi and T. Oda,
"Influence of underlayer reflection on optical proximity effects in
sub-quarter-micron lithography", *Proc. SPIE* **3334**, Optical
Microlithography XI, 347 (1998). <https://doi.org/10.1117/12.310764>
Relates the optical proximity effect to underlayer reflection for
negative and positive resists: the effect of underlayer reflection on
the isolated–dense CD bias is significant for the negative resist and
small for the positive resist, for which the partial coherence is the
lever. Used on the LI1M mask page. Tier: deep dive.

#### CTM1 mask page (first cited there)

**TAKEUCHI-1999** — K. Takeuchi and Y. Miyahara, "Defect detectability
and printability of contact hole pattern of KrF halftone reticle",
*Proc. SPIE* **3748**, Photomask and X-Ray Mask Technology VI, 579
(1999). <https://doi.org/10.1117/12.360251> Judging defects on KrF
halftone contact-hole reticles by size alone is vague; a Defect Area
Ratio method is proposed, and reticle defect specifications derived from
the wafer CD variation budget prove "too tight to be met with current
reticle inspection machines". Used on the CTM1 mask page. Tier: deep
dive.

#### MM1 mask page (first cited there)

**WORD-2002** — J. C. Word, S. Zhu and J. L. Sturtevant, "Assist feature
OPC implementation for the 130 nm technology node with KrF and no
forbidden pitches", *Proc. SPIE* **4691**, Optical Microlithography XV,
1139 (2002). <https://doi.org/10.1117/12.474494> At the 130 nm node
"with KrF illumination the k1 factor is only approximately 0.35", where
"it becomes essential to apply some form of Resolution Enhancement
Technology"; sub-resolution assist features with optimised illumination
give a manufacturable process window for all pitches, including the
"forbidden pitch" zone, shown in simulation and confirmed by experiment.
Used on the MM1 mask page. Tier: deep dive.
Also used on the MM2 mask page.

**SAMUELS-1995** — D. J. Samuels, W. Maurer and T. R. Farrell, "Good OPC,
where will this drive mask CD tolerance and mask grid size", *Proc.
SPIE* **2621**, 15th Annual BACUS Symposium on Photomask Technology and
Management, 588–596 (1995). <https://doi.org/10.1117/12.228213> The
effect of random mask CD variation, exposure latitude and defocus on an
OPC mask at low k₁, giving the expected aerial-image CD variation for
each, "how fine an OPC can realistically be obtained, and how fine a grid
size is needed in the manufacture of the mask". Used on the MM1 mask
page. Tier: deep dive.
Also used on the VIM and MM2 mask pages.

#### VIM mask page (first cited there)

**MA-ANDERSSON-1998** — Z. M. Ma and A. Andersson, "Preventing sidelobe
printing in applying attenuated phase-shift reticles", *Proc. SPIE*
**3334**, Optical Microlithography XI, 543 (1998).
<https://doi.org/10.1117/12.310783> "One major limitation of applying
attenuated phase shift mask (PSM) is sidelobe printing", "caused by
constructive interference of the first order of diffraction maximum from
nearby features, plus the electrical fields from semi-transparent
materials in the surrounding area"; the effects of defocus, lens
aberration and layout, the need to qualify a stepper for PSM use, and an
attenuated rim-shifter plate that prevents side lobes. Used on the VIM
mask page. Tier: deep dive.

**IWASAKI-1998** — H. Iwasaki, K. Hoshi and H. Tanabe,
"High-transmittance rim-type attenuated phase-shift masks for
sub-0.2-μm hole patterns", *Proc. SPIE* **3412**, Photomask and X-Ray
Mask Technology V, 601 (1998). <https://doi.org/10.1117/12.328842>
High- and standard-transmittance attenuated plates, both with rim
structures "to eliminate side lobes" and a chromium-fluoride shifter
under an opaque chromium layer, compared for 0.15 µm hole patterns; both
performed "high enough for 0.15 micrometers hole patterns". Used on the
VIM mask page. Tier: deep dive.

#### MM2 mask page (first cited there)

**HOCHMUTH-1999** — J. Hochmuth, G. G. Ruhl and T. P. Coleman, "Control
methodology of off-target for varying pattern densities with chrome dry
etch", *Proc. SPIE* **3873**, 19th Annual Symposium on Photomask
Technology, 297 (1999). <https://doi.org/10.1117/12.373324> With ZEP 7000
resist and ICP chrome dry etch, "the deviation of the CD from the target
value is a function of the chrome loading on the plate", so CD control
varies the exposure dose or develop time "based on the pattern loading of
a particular mask level"; a model built from designed experiments
predicts the settings for any level and was verified on production mask
levels of varying pattern density. Used on the MM2 mask page. Tier: deep
dive.

#### FOM mask page (first cited there)

**TIAN-2002** — R. Tian, X. Tang and M. D. F. Wong, "Dummy-feature
placement for chemical-mechanical polishing uniformity in a
shallow-trench isolation process", *IEEE Transactions on Computer-Aided
Design of Integrated Circuits and Systems* **21**(1), 63–71 (2002).
<https://doi.org/10.1109/43.974138> The abstract: the STI polish "is a
dual-material polish for which all previous studies on dummy-feature
placement for single-material polish" are not applicable; the paper
derives a time-dependent relation between post-CMP topography and layout
pattern density, formulates dummy-feature placement for STI as a
nonlinear-programming problem and solves it iteratively on four
industrial layouts. Used on the FOM mask page. Tier: deep dive.

**GAN-2001** — T. Gan, T. Tugbawa, B. Lee, D. S. Boning and S. Jang,
"Modeling of Reverse Tone Etchback Shallow Trench Isolation Chemical
Mechanical Polishing", *Journal of The Electrochemical Society*
**148**(3), G159 (2001). <https://doi.org/10.1149/1.1348266> A
mathematical model of the CMP of reverse-tone etchback STI structures,
validated with a purpose-designed STI CMP characterisation mask, with a
parameter-extraction method and predictions of the effect of pre-CMP
step height, pattern density, polish time, pad hardness and slurry
selectivity on dishing and nitride erosion. Used on the FOM mask page.
Tier: deep dive.

**PDK-ERRORS** — SkyWater PDK Authors, *Error Messages* page and
`errors.csv`, SkyWater SKY130 PDK documentation, retrieved 2026-09-14.
<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>.
A table of DRC message IDs, rule names and descriptions; the page says
the file "provides a raw description for many of the automated DRC
rules that are checked by SkyWater as part of the acceptance criteria
for GDS data". Several descriptions give values for rules the periphery
tables list as "N/A" — `pwbm.5` "0.84 min. spacing of pwbm_holes",
`pwde.6` "1.00 min. enclosure of pwde_uhvi by dnwell_uhvi", `rpm.10` "2
min. spacing of rpmNotXmt & pwbm" — and some differ from them (`lvtn.3b`
"0.19 min spacing of lvtn(peri) to pfet along S/D direction"). It lists
checks on created layers, such as `chvtpm.3` "0 min. enclosure of
((LVnwell not overlapping Var_channel) NOT lvtn) by CLHVTPM", `chvtpm.4`
"0 min. enclosure of ((LVnwell overlapping Var_channel) AND hvtp) by
CLHVTPM" and `clvtnm.1` "0.38 min. width of clvtnm in periphery", and
"nikon cross" checks for most mask layers (`cfom.nikon` "FOMmk in the
nikon cross has the wrong polarity"). Used on the FOM mask page. Tier:
cross-check.
Also used on the LVTNM mask page.

#### LVTNM mask page (first cited there)

**MUTOH-1995** — S. Mutoh, T. Douseki, Y. Matsuya, T. Aoki,
S. Shigematsu and J. Yamada, "1-V power supply high-speed digital
circuit technology with multithreshold-voltage CMOS", *IEEE Journal of
Solid-State Circuits* **30**(8), 847–854 (1995).
<https://doi.org/10.1109/4.400426> Multithreshold-voltage CMOS
(MTCMOS) at 0.5 µm, which "features both low-threshold voltage and
high-threshold voltage MOSFET's in a single LSI": the low-threshold
devices give speed at a supply of 1 V or less, the high-threshold ones
suppress stand-by leakage during sleep; with a standard-cell library
and a PLL demonstrator. Used on the LVTNM mask page. Tier: deep dive.
Also used on the HVTPM mask page.

**FARICELLI-2010** — J. V. Faricelli, "Layout-dependent proximity
effects in deep nanoscale CMOS", *IEEE Custom Integrated Circuits
Conference 2010*, pp. 1–8. <https://doi.org/10.1109/CICC.2010.5617407>
A review of the process technology features that make device behaviour
depend on layout details and the surrounding neighbourhood, including
stress engineering, and of how to account for them in circuit and layout
design. Used on the LVTNM mask page. Tier: deep dive.

#### NWM mask page (first cited there)

**RUNG-1981** — R. D. Rung, C. J. Dell'Oca and L. G. Walker, "A
retrograde p-well for higher density CMOS", *IEEE Transactions on
Electron Devices* **28**(10), 1115–1119 (1981).
<https://doi.org/10.1109/T-ED.1981.20498> A CMOS well (p-well or
n-well) formed by a deep implant followed by a brief anneal, giving a
retrograde profile, a much shallower well, a reduction of n- to
p-channel device spacing from 10–15 µm to 5–6 µm and a lower latch-up
risk, demonstrated on a shrunk 4K static RAM. Used on the NWM mask page.
Tier: deep dive.
Also used on the PWBM mask page.

**MARTIN-1986** — R. A. Martin and J. Y.-T. Chen, "Optimized retrograde
N-well for 1-μm CMOS technology", *IEEE Journal of Solid-State Circuits*
**21**(2), 286–292 (1986). <https://doi.org/10.1109/JSSC.1986.1052516>
Transistors in a high-energy implanted N-well designed, by experiment
and simulation, for 1 µm CMOS, with better body effect, junction
capacitance, punch-through voltage and subthreshold slope, and latch-up
immunity on shallow P/P+ epitaxial material. Used on the NWM mask page.
Tier: deep dive.

#### HVTPM mask page (first cited there)

**KAO-2000** — J. T. Kao and A. P. Chandrakasan, "Dual-threshold voltage
techniques for low-power digital circuits", *IEEE Journal of Solid-State
Circuits* **35**(7), 1009–1018 (2000). <https://doi.org/10.1109/4.848210>
Dual-threshold techniques "for reducing standby power dissipation while
still maintaining high performance" in static and dynamic logic:
MTCMOS sleep-transistor sizing by mutually exclusive discharge patterns,
and a dual-Vt domino style with low-Vt performance and high-Vt stand-by
leakage. Used on the HVTPM mask page. Tier: deep dive.

**KIZILYALLI-1995** — I. C. Kizilyalli, M. M. Rambaud, A. Duncan,
S. A. Lytle and M. J. Thoma, "Threshold voltage-minimum gate length
trade-off in buried channel PMOS devices for scaled supply voltage CMOS
technologies", *IEEE Electron Device Letters* **16**(10), 457–459
(1995). <https://doi.org/10.1109/55.464816> For n+-polysilicon-gate
buried-channel PMOS at 3.3 to 1.8 V, threshold voltage and minimum gate
length "cannot be scaled independently due to the channel punch-through
effect"; trading threshold for a shorter gate gives faster circuits, and
the optimum threshold magnitude for the authors' 0.5 µm 3.3 V process is
about 0.85–0.90 V. Used on the HVTPM mask page. Tier: deep dive.

**ANDREANI-2000** — P. Andreani and S. Mattisson, "On the use of MOS
varactors in RF VCOs", *IEEE Journal of Solid-State Circuits* **35**(6),
905–910 (2000). <https://doi.org/10.1109/4.845194> Two 1.8 GHz CMOS
oscillators in a 0.6 µm process, tuned by an inversion-mode and an
accumulation-mode MOS varactor, both with lower power and phase noise
than a diode-varactor reference, the accumulation-mode one best. Used on
the HVTPM mask page. Tier: deep dive.

#### PWBM mask page (first cited there)

**COMBS-1981** — S. R. Combs, "Scaleable retrograde p-well CMOS
technology", *1981 International Electron Devices Meeting*, pp. 346–349.
<https://doi.org/10.1109/IEDM.1981.190084> A retrograde P-well made with
"a single high-energy boron implant to produce a self-aligned channel
stop and an extremely shallow, low sheet-resistance p-well" with low
n-channel thresholds; the buried peak about 1 µm deep lowers the npn
gain and lets n- to p-channel spacing shrink from 12–15 µm to 3–6 µm,
with better density and latch-up behaviour on a 1K RAM test structure.
Used on the PWBM mask page. Tier: deep dive.

**TEE-2010** — E. K. C. Tee, D. K. Pal, S. H. Tia and Y. H. Hu, "High
voltage NMOS double hump prevention by using baseline CMOS p-well
implant", *2010 International Conference on Electronic Devices, Systems
and Applications*, pp. 289–293.
<https://doi.org/10.1109/ICEDSA.2010.5503059> A 32 V LDMOS integrated
into a 0.18 µm STI CMOS process showed a double hump from a
low-threshold transistor corner; a boron implant in the HV LDNMOS
suppressed it, and the retrograde baseline CMOS P-well implant was used
"to avoid an additional mask and process step". Used on the PWBM mask
page. Tier: deep dive.

#### PWDEM mask page (first cited there)

**LUDIKHUIZE-1982** — A. W. Ludikhuize, "High-voltage DMOS and PMOS in
analog IC's", *1982 International Electron Devices Meeting*, pp. 81–84.
<https://doi.org/10.1109/IEDM.1982.190218> A lateral 300 V DMOS for a
standard bipolar IC process, based on the "double-acting resurf"
principle, with an interrupted p− top layer or a stepped field plate;
the p− layer improves interconnection-induced breakdown "and can be used
in the extended drain of a 280 V PMOST". Used on the PWDEM mask page.
Tier: deep dive.

**MEI-1994** — P. C. Mei, K. Fujikura, T. Fawano and S. Malhi, "A high
performance 30 V extended drain RESURF CMOS device for VLSI intelligent
power applications", *Proceedings of 1994 VLSI Technology Symposium*,
pp. 81–82. <https://doi.org/10.1109/VLSIT.1994.324367> 30 V lateral DMOS
devices for high-side and low-side drivers in a twin-well, single-tank,
one-metal 2.0 µm CMOS process that optimises N- and P-channel
high-voltage devices together with a self-aligned extended-drain RESURF
approach, reporting specific on-resistance and avalanche breakdown for
both. Used on the PWDEM mask page. Tier: deep dive.

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
| Coat/develop tracks | DNS (SCREEN) 80B; Sokudo RF3; TEL ProZ Lithius | SKW-01 | strong |
| Photo metrology | AMAT Verity (CD-SEM), AMAT VeraSEM; KLA 5200/5300/Archer overlay | SKW-01 | strong |
| Defect inspection | "SEM/AIT/KLA/SP1/EV300/1X" (read as KLA-Tencor AIT, Surfscan SP1 and eV300 review; reading ours) | JOB-01 ("SEM/AIT/KLA/SP1/EV300/1X") | medium |
| CVD dielectrics | "C1"/"C2" PECVD (inferred to be Novellus Concept One/Two; SKW-01 gives only the abbreviations); AMAT Producer PECVD TEOS; Lam/Novellus HDP-CVD (doped and PSG) | SKW-01; SKW-07 ("Novellus high density plasma tool") | strong |
| CVD tungsten | Lam/Novellus PECVD tungsten with PNL nucleation (plug fill, ≤10:1) | SKW-01 | strong |
| PVD metals | AMAT PVD (Al and AlCu, TiW, TiN (ESC and IMP), collimated Ti, WN, Co, Nb) — consistent with Endura-class platforms | SKW-01 (platform name not given) | strong for vendor, weak for model |
| Electroplating † | AMAT Raider single-wafer Cu plating | SKW-01 | strong |
| ALD † | (vendor not named) AlN, TiN, SiO₂, Al₂O₃, HfO₂, TiO₂, ZrO₂ | SKW-01 | strong (capability), no vendor |
| Metal etch | Lam 9600 (Al, TiW, TiN, Pt); Lam 2300 Versys (Al, TiW, TiN, Nb, Pt) | SKW-01 | strong |
| Poly/oxide/trench etch | AMAT DPS II (HBr/Cl₂/NF₃/CF₄/CHF₃/O₂ — gate, trench, W/WN); Lam 9400 TCP (poly/nitride); Lam 4400 | SKW-01 | strong |
| Resist strip | GaSonics PEP (remote microwave); Iridia RF microwave; Mattson Aspen II | SKW-01 | strong |
| Wet clean / wet etch | Akrion Gamma batch bench (H₂SO₄, SC1, H₃PO₄, BOE); DNS wet bench (HF/SC1/SC2); FSI Mercury rotational; SEZ 223 and Da Vinci single-wafer (HF, DSP) | SKW-01; SKW-07 ("SEZ etcher tool") | strong |
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
  publicly and must be inferred from feature size (ITRS-03 gives the
  critical-layer wavelengths only; ASML-30 describes older tools moving
  to less critical layers).
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
