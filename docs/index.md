# SKY130 Process Technology

A step-by-step reference on how the SKY130 130 nm CMOS process
technology is manufactured, written as a worked example of how a
mass-produced 130 nm process is set up.

SKY130 is the open-source process design kit released by SkyWater
Technology and Google in 2020. It descends from the Cypress
Semiconductor "S8" 130 nm process and is fabricated on 200 mm wafers at
SkyWater's Bloomington, Minnesota fab.[^pdk-01][^skw-01] It offers one
polysilicon gate level, a local-interconnect level, five aluminium metal
levels, SONOS non-volatile memory, metal–insulator–metal capacitors and
a family of 1.8 V and 5 V (and higher) transistors.

Every page in this reference cites only publicly available sources. The
171-step sequence, with its step codes and names, is taken from the
public *S8 / SKY130 Process Steps* sheet.[^steps-sheet]

## Where to go

::::{grid} 1 2 3 3
:gutter: 2

:::{grid-item-card} Overview
:link: overview-index
:link-type: ref

Start here — what SKY130 is, how this reference is organised, and the flow by module.
:::

:::{grid-item-card} Process steps
:link: steps-index
:link-type: ref

The full manufacturing sequence: 171 steps, one page per step.
:::

:::{grid-item-card} Categories
:link: categories-index
:link-type: ref

The 10 kinds of step — etch, deposition, implant and the rest — and what each has in common.
:::

:::{grid-item-card} Machines
:link: machines-index
:link-type: ref

The 30 classes of tool used across the flow.
:::

:::{grid-item-card} Materials
:link: materials-index
:link-type: ref

The 12 classes of consumable — gases, wet chemicals, targets, resists — used across the flow.
:::

:::{grid-item-card} Masks
:link: masks-index
:link-type: ref

The 36 lithography masks that pattern the wafer.
:::

:::{grid-item-card} Glossary
:link: glossary
:link-type: ref

219 terms and acronyms used throughout this reference.
:::

:::{grid-item-card} References
:link: references-index
:link-type: ref

1,720 sources in the inventory, and the papers, patents and filings indexes.
:::

:::{grid-item-card} Figure conventions
:link: figure-conventions
:link-type: doc

How to read a diagram: what is to scale, what is a reading, and what "Not to scale" means.
:::

::::

## The flow in 13 modules

| Module | Steps | Number of steps | Mask steps |
|--------|-------|-----------------|------------|
| {ref}`Starting material, isolation and deep N-well <step-001>` | {ref}`SMAT <step-001>` – {ref}`NS19 <step-013>` | 13 | 2 (`FOM`, `DNM`) |
| {ref}`Wells and threshold implants <step-014>` | {ref}`LVTNM <step-014>` – {ref}`RTAI <step-034>` | 21 | 5 (`LVTNM`, `NWM`, `HVTPM`, `PWBM`, `PWDEM`) |
| {ref}`SONOS tunnel window and ONO stack <step-035>` | {ref}`TUNM <step-035>` – {ref}`ONOME <step-042>` | 8 | 2 (`TUNM`, `ONOM`) |
| {ref}`Gate oxides <step-043>` | {ref}`GOX100 <step-043>` – {ref}`LVGOX <step-047>` | 5 | 1 (`LVOM`) |
| {ref}`Poly gate and poly resistors <step-048>` | {ref}`SAGD <step-048>` – {ref}`IOX45 <step-063>` | 16 | 4 (`RPM`, `RRPM`, `URPM`, `P1M`) |
| {ref}`Tips and halos <step-064>` | {ref}`NTM <step-064>` – {ref}`TIPRTAD <step-075>` | 12 | 3 (`NTM`, `HVNTM`, `LDNTM`) |
| {ref}`Spacers and source/drain <step-076>` | {ref}`SPNIT <step-076>` – {ref}`RTAD <step-088>` | 13 | 3 (`NPCM`, `PSDM`, `NSDM`) |
| {ref}`Pre-metal dielectric, contact silicide and local interconnect <step-089>` | {ref}`PSG <step-089>` – {ref}`CMPL <step-106>` | 18 | 2 (`LICM1`, `LI1M`) |
| {ref}`Metal contact and metal 1 <step-107>` | {ref}`CTM1 <step-107>` – {ref}`NCAPOX3 <step-117>` | 11 | 2 (`CTM1`, `MM1`) |
| {ref}`Via 1, metal 2 and via 2 <step-118>` | {ref}`VIM <step-118>` – {ref}`WTIAL3 <step-134>` | 17 | 3 (`VIM`, `MM2`, `VIM2`) |
| {ref}`First MiM capacitor, metal 3 and via 3 <step-135>` | {ref}`CAPILD <step-135>` – {ref}`WCMP5 <step-148>` | 14 | 3 (`CAPM`, `MM3`, `VIM3`) |
| {ref}`Metal 4, second MiM capacitor, via 4 and metal 5 <step-149>` | {ref}`WTIAL4 <step-149>` – {ref}`MM5E <step-163>` | 15 | 4 (`CAP2M`, `MM4`, `VIM4`, `MM5`) |
| {ref}`Passivation, pads, alloy and test <step-164>` | {ref}`NFUSOX <step-164>` – {ref}`HPETEST <step-171>` | 8 | 2 (`NSM`, `PDM`) |

The full table, with the public facts each module rests on, is on the
[overview](overview/index.md#the-flow-by-module).

## How to read a page

Each page marks what is a stated fact, what is a typical value for a process of this kind, and
what is this reference's own inference, and cites a public source for every one of them with a
footnote marker. Hovering, focusing or tapping a marker shows the citation without leaving the
page. The [overview's "How to read this reference"](overview/index.md#how-to-read-this-reference)
section explains the wording in full.

```{toctree}
:maxdepth: 1
:caption: Overview
:hidden:

overview/index
```

```{toctree}
:maxdepth: 1
:caption: Process steps
:hidden:

steps/index
```

```{toctree}
:maxdepth: 1
:caption: Cross-cutting references
:hidden:

categories/index
machines/index
materials/index
masks/index
glossary
figure-conventions
references/index
```

```{toctree}
:maxdepth: 1
:caption: History

history/index
```

<!-- footnotes -->

[^pdk-01]: SkyWater PDK Authors, *SkyWater SKY130 PDK documentation*.
    <https://skywater-pdk.readthedocs.io/en/main/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    retrieved 2026-09-14; tab "Sheet1" lists the 171 steps (number, code and
    description). <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
