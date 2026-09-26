(history-s8-lineage)=
# From the earlier processes to S8 and SKY130

SKY130 is SkyWater's name for the process Cypress called S8 (see {ref}`overview-index`). This page sets out
what S8 has in common with the Cypress processes before it, and what the sources do and do not say about
where it came from. The processes themselves are on {ref}`history-technologies` and
{ref}`history-sonos-s4`.

## What S8 was

* **A 0.13 µm SONOS process.** Cypress's October 2007 announcement of its first S8 products, 4 Mbit nvSRAMs,
  calls S8 "Cypress's S8(tm) 0.13-micron SONOS (Silicon Oxide Nitride Oxide Silicon) embedded nonvolatile
  memory technology". EE Times called it "0.13-micron S8 embedded-flash technology" the same
  year.[^ew-2007-s8][^eet-2007-fablite] A teardown of a PSoC 4200 chip made on S8 found it "by SEM imaging
  to be 130nm tech".[^siliconpr0n-psoc4]
* **Qualified at Fab 4 in 2008.** Cypress's report history dates "To qualify S8 SONOS technology and 4M
  nvSRAM devices" to November 2008, at "Cypress Minnesota CMI (Fab4)" (single source).[^qtp-113005]
* **The PSoC process.** Cypress's 2010 report calls S8 "our 0.13-micron, nonvolatile PSoC wafer
  fabrication process"; Infineon's history of PSoC says PSoC 3 was developed "using a 130 nm 5 V process"
  (Cypress and Infineon).[^ar-fy2010][^psoc-history]
* **nvSRAM.** The first S8 products were nvSRAMs, and in 2008 Cypress bought Simtek, whose nvSRAM line it
  took over (Cypress's reports).[^ew-2007-s8][^ar-fy2008] A 2008 paper by Cypress and Simtek authors
  describes "A 15ns 4Mb NVSRAM in 0.13u SONOS Technology".[^fliesler-2008][^ew-2007-s8]

## What S8 has in common with earlier processes

No source found says from which process S8 was derived. We see three things S8 shares with earlier
Cypress processes (our reading):

**1. The 0.13 µm generation at Fab 4.** A 2015 Cypress notice lists "130nm C8/R8/S8/L8" together. The C8
logic process was qualified in January 2005, and L8C-3R is a "Technology Derivative of the C8 Technology".
S8's first metal layer is C8's, film for film: "100A Ti / 3200A Al -0.5%Cu / 300A TiW" against "100A
Ti/3,200A Al 0.5% Cu /300A TiW" (Cypress's reports).[^pin-152804][^qtp-043004][^qtp-053301][^qtp-113005]

**2. SONOS.** Cypress's earlier SONOS process, S4AD-5, had been in production since 2001. Cypress wrote in
2008 that its SONOS module can be added "into a logic process flow or an SRAM process flow with the
addition of three to five masking layers" (Cypress's reports).[^eflash-brief][^qtp-021507][^chipest-2008]

**3. The 110 Å gate oxide.** S8 has two gate oxides, 110 Å and 32 Å, and Cypress's 2008 article describes
a "dual gate oxide process" for multiple supply voltages.[^qtp-113005][^chipest-2008] The 110 Å oxide is
the gate oxide of S4AD-5 and of the 5 V versions of the 0.42 µm processes from 1997 onwards. C8 instead
pairs 32 Å with 55 Å (Cypress's reports).[^qtp-021507][^qtp-102101][^qtp-030206][^qtp-043004]

The SKY130 PDK, from SkyWater, says its high-voltage devices "use 110A gate oxide
thickness" (single source).[^pdk-hv]

**Grace.** Cypress's 2010 report says it moved its "0.35-micron SONOS, 0.13-micron SRAM and LOGIC
processes" to Grace in 2006 and 2007 (single source).[^ar-fy2010] It does not name S8 among them.
Cypress's own qualification reports nonetheless show S8 variants qualified there from 2010; see
{ref}`history-grace`.

## Side by side

| | S4AD-5 (2001) | C8Q-3R (2005) | S8TNV-5R (2008) |
|---|---|---|---|
| Design rule | 0.35 µm | 0.13 µm | 0.13 µm |
| Memory | SONOS | none | SONOS |
| Metal layers | 2 | 4 | 3 |
| Gate oxides | 110 Å | 32 Å, 55 Å | 110 Å, 32 Å |
| Metal 1 | 500 Å Ti / 6000 Å Al–Cu / 1200 Å TiW | 100 Å Ti / 3200 Å Al–Cu / 300 Å TiW | 100 Å Ti / 3200 Å Al–Cu / 300 Å TiW |
| Passivation | 3000 Å TEOS / 6000 Å nitride | 1000 Å TEOS / 9000 Å nitride | 7000 ± 2000 Å nitride |

Each column copies one Cypress report (Cypress's reports).[^qtp-021507][^qtp-043004][^qtp-113005] One
S4AD-5 report prints 0.5 µm. The S8 column copies the 2008 S8 report; a 2014 S8 report records a later
metal-stack change (see {ref}`overview-metal-cap`). SkyWater's PDK describes its base process, `s8pfhd`,
as a "5 metal layer backend stack" (single source).[^pdk-previous]

For SKY130, the PDK gives a 110 Å oxide for its 5 V devices and draws `met1` 0.36 µm thick.[^pdk-hv][^pdk-metal-stack]
S8's first metal adds up to 0.36 µm (our arithmetic). The same recipe is used in two of Cypress's 90 nm
processes of 2006 and 2007 (Cypress's reports).[^qtp-113005][^qtp-063807][^qtp-061806]

The PDK is not independent of the Cypress reports: SkyWater runs the fab it bought from Cypress in
2017.[^tenq-2017q1][^strib-2017]

## What does the "8" mean?

The SKY130 PDK says `s8` "stood for the '8th generation' of the SONOS technology developed originally by
Cypress" (single source).[^pdk-previous] The Cypress sources point elsewhere:

* **One SONOS process before S8 in the reports.** The only earlier SONOS process in the reports is S4AD-5.
  Cypress's own lists of processes from 2002 to 2006 name one SONOS process (Cypress's
  reports).[^ar-fy2002][^ar-fy2006] Infineon's history, though, claims SONOS CPLDs in the late 1980s,
  which conflicts with the reports and would allow earlier SONOS generations (see {ref}`history-sonos-s4`).[^psoc-history]
* **The digit follows the process generation.** Cypress named its SRAM processes RAM3 (0.5 µm), RAM5
  (0.25 µm), RAM 7 and RAM 8 (0.13 µm), and a 2015 notice lists the 0.13 µm families as C8, R8, S8 and L8
  (Cypress's reports).[^ar-fy1995][^ar-fy1998][^ar-fy2002][^pin-152804]

We read the "8" as the process generation Cypress numbered 8, the 0.13 µm one, and the "S" as SONOS, as S4
was the SONOS process of generation 4 (our reading). The numbering is Cypress's, not a scale: generation 6, R63D-25, prints 0.27 µm, coarser than generation 5,
and generation 2 covers 0.8 µm and 0.65 µm.[^qtp-012407] SkyWater's "8th generation of the
SONOS technology" and this reading agree that S8 is a SONOS process; they differ on what the 8 counts, and
no Cypress source found says.[^pdk-previous] The naming is set out on {ref}`history-naming`.

## Patents from the years before S8

Three Cypress patent families filed in 2005–2007 describe process modules of the kind S8 needed: a
high-voltage transistor, and ways to build SONOS memory and logic transistors together. A patent shows
what Cypress worked on, not what S8 used. The patent records show them as in force or of unknown status,
so each is in a collapsed note.

:::{dropdown} A high-voltage transistor patent of status shown as unknown (US 7,592,661; estimated expiry no later than 2026-07-29) — open to read
Filed with a 2005 priority date, it describes "a high voltage, drain-extended (DE) metal-oxide-
semiconductor (MOS) transistor" whose drain extension is formed in a deep n-well (single
source).[^pat-us7592661]
:::

:::{dropdown} A SONOS-and-logic oxide patent shown as in force (US 9,583,501 family; estimated expiry 2026-12-22) — open to read
Filed with a 2006 priority date, it forms the SONOS top oxide and the gate oxide of the logic transistors
in one step: "a top oxide layer over the nitride layer and a gate oxide layer over the surface of
substrate in the second region" (single source).[^pat-us9583501]
:::

:::{dropdown} A memory-and-logic integration patent shown as in force (US 8,093,128; estimated expiry 2028-10-22) — open to read
Filed with a 2007 priority date, it describes a chip with "a non-volatile charge trap memory device
disposed on a first region and a logic device disposed on a second region" (single
source).[^pat-us8093128]
:::

## Open questions

* **C8 and S8.** Was S8 built on C8, on R8, or on neither?
* **The oxides.** When did the 110 Å oxide join the 32 Å one in a 0.13 µm process?
* **SONOS generations.** Were there SONOS processes before S4AD-5, or between S4AD-5 and S8, that the
  reports do not record?

## References

### Cross-check

* [SkyWater PDK, *Previous Nomenclature*](<https://skywater-pdk.readthedocs.io/en/main/previous.html>) — what `s8` stood for, in SkyWater's words.[^pdk-previous]
* [Cypress, PIN152804](<https://media.futureelectronics.com/PCN/45887_SPCN.PDF>) — the 0.13 µm families together.[^pin-152804]

### High-level understanding

* [Electronics Weekly, *Cypress 4-Mbit non-volatile static random access memory*](<https://www.electronicsweekly.com/news/products/memory-products/cypress-4-mbit-non-volatile-static-random-access-memory-2007-10/>) — the first S8 products.[^ew-2007-s8]
* [Infineon, *20 years of PSoC*](<https://web.archive.org/web/20250713043850/https://www.infineon.com/cms/en/product/promopages/20-years-of-psoc/how-it-started/>) — PSoC 1 and PSoC 3 processes.[^psoc-history]

### Deep dive

* [Cypress, QTP 113005](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>) — S8TNV-5R and the first S8 qualification.[^qtp-113005]
* [Cypress, QTP 043004](<https://web.archive.org/web/20201205122906/https://www.cypress.com/file/92151/download>) — C8Q-3R.[^qtp-043004]
* [Cypress, QTP 053301](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-053301-l8c-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149c4a70b8f>) — L8C-3R, a derivative of C8.[^qtp-053301]
* [Cypress, QTP 021507](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>) — S4AD-5.[^qtp-021507]
* [Cypress, QTP 102101](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-102101-synchronous-asynchronous-dual-port-sram-3.3v-and-5v-r42hd-technology-fab-4-qualification-productqualificationreport-en.pdf>) — R42HD and its 110 Å oxide.[^qtp-102101]
* [Cypress, QTP 030206](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030206-256k-static-ram-automotive-devices-ram42hha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71491e3d0986>) — RAM42 and its 110 Å oxide.[^qtp-030206]
* [Cypress, QTP 063807](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-063807-1-meg-fast-asynchronous-sram-family-c9fd-3r-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149f5380c45>) — C9FD-3R's first metal.[^qtp-063807]
* [Cypress, QTP 061806](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-061806-4-meg-mobl-sram-automotive-devices-r95ld-3r-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714fdec718db>) — R95LD-3R's first metal.[^qtp-061806]
* [SkyWater PDK, *High Voltage Methodology*](<https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>) — the 110 Å oxide of SKY130.[^pdk-hv]
* [SkyWater PDK, *metal_stack.svg*](<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>) — the SKY130 metal thicknesses.[^pdk-metal-stack]
* [Cypress, *Cypress SONOS - A Scalable Embedded Flash Technology*](<https://www.chipestimate.com/Cypress-SONOS-A-Scalable-Embedded-Flash-Technology/Cypress-Semiconductor/Technical-Article/2008/10/21>) — the SONOS module.[^chipest-2008]
* [Cypress, 2010 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2010.pdf>) — S8 as the PSoC process.[^ar-fy2010]

<!-- footnotes -->

[^ew-2007-s8]: Electronics Weekly, *Cypress 4-Mbit non-volatile static random access memory*,
    2007-10-18.
    <https://www.electronicsweekly.com/news/products/memory-products/cypress-4-mbit-non-volatile-static-random-access-memory-2007-10/>
[^eet-2007-fablite]: EE Times, *Cypress furthers 'fab lite'*, 2007-03-05.
    <https://www.eetimes.com/cypress-furthers-fab-lite/>
[^ar-fy1995]: Cypress Semiconductor Corp., *1995 Annual Report*, fiscal year ended 1996-01-01:
    shareholder letter, highlights timeline and notes on commitments and subsidiaries.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1995.pdf>
[^ar-fy1998]: Cypress Semiconductor Corp., *1998 Annual Report*, fiscal year ended 1999-01-03:
    president's letter and restructuring discussion.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1998.pdf>
[^ar-fy2002]: Cypress Semiconductor Corp., *2002 Annual Report* with Form 10-K, fiscal year ended
    2002-12-29: Item 1, Research and development and Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2002.pdf>
[^ar-fy2006]: Cypress Semiconductor Corp., *2006 Annual Report* with Form 10-K, fiscal year ended
    2006-12-31: Item 1, Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2006.pdf>
[^ar-fy2010]: Cypress Semiconductor Corp., *2010 Annual Report* with Form 10-K, fiscal year ended
    2011-01-02: "Manufacturing" section.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2010.pdf>
[^pin-152804]: Cypress Semiconductor, Product Information Notification PIN152804, *Qualification of
    GlobalWafer Silicon Wafers for 250nm, 130nm and 90nm Technology Products at Cypress Fab 4*,
    2015-07-12 (copy hosted by Future Electronics).
    <https://media.futureelectronics.com/PCN/45887_SPCN.PDF>
[^psoc-history]: Infineon Technologies, *20 years of PSoC: How it started*, Wayback Machine copy of
    2025-07-13 (the live page now redirects elsewhere).
    <https://web.archive.org/web/20250713043850/https://www.infineon.com/cms/en/product/promopages/20-years-of-psoc/how-it-started/>
[^chipest-2008]: Cypress Semiconductor, *Cypress SONOS - A Scalable Embedded Flash Technology*,
    ChipEstimate.com Tech Talks, 2008-10-21.
    <https://www.chipestimate.com/Cypress-SONOS-A-Scalable-Embedded-Flash-Technology/Cypress-Semiconductor/Technical-Article/2008/10/21>
[^eflash-brief]: Cypress Semiconductor (an Infineon company), *SONOS eFlash* product overview,
    undated product brief.
    <https://www.infineon.com/assets/row/public/documents/10/45/infineon-sonos-eflash-product-overview-productbrief-en.pdf?fileId=8ac78c8c7d710014017d715307cf2069>
[^pdk-previous]: SkyWater PDK Authors, *Previous Nomenclature*, SkyWater SKY130 PDK documentation,
    retrieved 2026-09-25. <https://skywater-pdk.readthedocs.io/en/main/previous.html>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater SKY130 PDK documentation,
    retrieved 2026-09-25. <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^pdk-metal-stack]: SkyWater PDK Authors, *metal_stack.svg* (process stack diagram),
    google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^qtp-113005]: Cypress Semiconductor, Product Qualification Report QTP 113005: *64K Serial Non-Volatile SRAM Product Family, S8 Technology, CMI (Fab 4)*, January 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^qtp-043004]: Cypress Semiconductor, Product Qualification Report QTP 043004: *DDR2-PLL Device Family, C8Q-3R, Fab 4*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205122906/https://www.cypress.com/file/92151/download>
[^qtp-053301]: Cypress Semiconductor, Product Qualification Report QTP 053301: *L8C-3R Technology, Fab 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-053301-l8c-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149c4a70b8f>
[^qtp-021507]: Cypress Semiconductor, Product Qualification Report QTP 021507: *Failsafe Device Family & Options S4AD-5 SONOS Technology, Fab 2*, December 2015.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>
[^qtp-102101]: Cypress Semiconductor, Product Qualification Report QTP 102101: *Synchronous/Asynchronous Dual Port SRAM (3.3V and 5V), R42HD Technology, Fab 4 Qualification*, July 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-102101-synchronous-asynchronous-dual-port-sram-3.3v-and-5v-r42hd-technology-fab-4-qualification-productqualificationreport-en.pdf>
[^qtp-030206]: Cypress Semiconductor, Product Qualification Report QTP 030206: *256K Static RAM Automotive Devices, RAM42HHA Technology, Fab 4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030206-256k-static-ram-automotive-devices-ram42hha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71491e3d0986>
[^qtp-063807]: Cypress Semiconductor, Product Qualification Report QTP 063807: *1 Meg Fast Asynchronous SRAM Family, C9FD-3R Technology, Fab4*, January 2024.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-063807-1-meg-fast-asynchronous-sram-family-c9fd-3r-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149f5380c45>
[^qtp-061806]: Cypress Semiconductor, Product Qualification Report QTP 061806: *4 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4*, March 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-061806-4-meg-mobl-sram-automotive-devices-r95ld-3r-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714fdec718db>
[^ar-fy2008]: Cypress Semiconductor Corp., *2008 Annual Report* with Form 10-K, fiscal year ended
    2008-12-28: shareholder letter and Item 1, Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2008.pdf>

[^strib-2017]: Alex Van Abbema, *Twin Cities tech executives form new company, buy Cypress chip
    plant in Bloomington*, Star Tribune, 2017-03-31.
    <https://www.startribune.com/twin-cities-tech-executives-form-new-company-buy-cypress-chip-plant-in-bloomington/417672063>

[^tenq-2017q1]: Cypress Semiconductor Corp., Form 10-Q for the quarter ended 2017-04-02, filed
    2017-05-02, Notes (assets held for sale); Wayback Machine copy of the EDGAR filing.
    <https://web.archive.org/web/20170503100919/https://www.sec.gov/Archives/edgar/data/791915/000079191517000030/cy-04022017x10xq.htm>
[^fliesler-2008]: M. Fliesler, D. Still and J.-M. Hwang (Cypress Semiconductor and Simtek), *A 15ns 4Mb
    NVSRAM in 0.13u SONOS Technology*, 2008 Joint Non-Volatile Semiconductor Memory Workshop and
    International Conference on Memory Technology and Design, DOI 10.1109/NVSMW.2008.30.
    <https://ieeexplore.ieee.org/document/4531830/>
[^pat-us7592661]: S. Lee et al. (Cypress Semiconductor), US 7,592,661 B1, priority 2005-07-29. Status
    shown as unknown; estimated expiry no later than 2026-07-29 (estimate from public records, not legal
    advice). <https://patents.google.com/patent/US7592661B1/en>
[^pat-us9583501]: J.-M. Hwang (Cypress Semiconductor), US 9,583,501 B1, priority 2006-12-22. Shown as in
    force; estimated expiry 2026-12-22 (estimate from public records, not legal advice).
    <https://patents.google.com/patent/US9583501B1/en>
[^pat-us8093128]: W. W. C. Koutny Jr. et al. (Cypress Semiconductor), US 8,093,128 B2, priority 2007-05-25.
    Shown as in force; estimated expiry 2028-10-22 (estimate from public records, not legal advice).
    <https://patents.google.com/patent/US8093128B2/en>
[^siliconpr0n-psoc4]: Silicon Prawn wiki, *azonenberg:cypress:cy8c4245axi* (teardown of the Cypress
    CY8C4245AXI, PSoC 4200), last modified 2025-08-04.
    <https://siliconpr0n.org/archive/doku.php?id=azonenberg:cypress:cy8c4245axi>
[^qtp-012407]: Cypress Semiconductor, Product Qualification Report QTP 012407: *Synchronous SRAM Family, R63D-25 Technology, Fab4*, November 2002;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210517162336/https://www.cypress.com/file/91686/download>
