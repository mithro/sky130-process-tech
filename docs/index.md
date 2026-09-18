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

```{toctree}
:maxdepth: 1
:caption: Overview

overview/index
```

```{toctree}
:maxdepth: 1
:caption: Process steps

steps/index
```

```{toctree}
:maxdepth: 1
:caption: Cross-cutting references

categories/index
machines/index
materials/index
masks/index
glossary
references/index
```

<!-- footnotes -->

[^pdk-01]: SkyWater PDK Authors, *SkyWater SKY130 PDK documentation*.
    <https://skywater-pdk.readthedocs.io/en/main/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    retrieved 2026-09-14; tab "Sheet1" lists the 171 steps (number, code and
    description). <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
