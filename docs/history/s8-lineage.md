(history-s8-lineage)=
# From the earlier processes to S8 and SKY130

SKY130 is SkyWater's name for the process Cypress called S8 (see {ref}`overview-index`). This page
sets out what S8 inherited from the Cypress processes before it, and what the sources do and do not
say about that inheritance. The processes themselves are on {ref}`history-technologies` and
{ref}`history-sonos-s4`.

## What S8 was

* **A 0.13 µm SONOS process.** Electronics Weekly reported the first products "manufactured on
  Cypress's S8(tm) 0.13-micron SONOS (Silicon Oxide Nitride Oxide Silicon) embedded nonvolatile memory
  technology" in October 2007: 4 Mbit nvSRAMs.[^ew-2007-s8] EE Times called it "0.13-micron S8
  embedded-flash technology" the same year.[^eet-2007-fablite]
* **Qualified at Fab 4 in 2008.** Cypress's report history dates "To qualify S8 SONOS technology and
  4M nvSRAM devices" to November 2008, at "Cypress Minnesota CMI (Fab4)" (single source).[^qtp-113005]
* **The PSoC process.** Cypress's 2010 report calls S8 "our 0.13-micron, nonvolatile PSoC wafer
  fabrication process".[^ar-fy2010] Infineon's PSoC history says PSoC 3 was developed "using a 130 nm
  5 V process".[^psoc-history]

## Three lines of descent

The sources point to three earlier processes that S8 draws on.

**1. The 0.13 µm generation at Fab 4.** A 2015 Cypress notice lists "130nm C8/R8/S8/L8" together, the
0.13 µm families at Fab 4.[^pin-152804] The C8 logic process was qualified in January 2005, and L8C-3R
is a "Technology Derivative of the C8 Technology" (Cypress's reports).[^qtp-043004][^qtp-053301] S8's
first metal layer is the same as C8's, film for film: "100A Ti / 3200A Al -0.5%Cu / 300A TiW" against
"100A Ti/3,200A Al 0.5% Cu /300A TiW" (Cypress's reports).[^qtp-113005][^qtp-043004] No source found
says in words that S8 was derived from C8.

**2. The SONOS module from S4AD-5.** Cypress's earlier SONOS process, S4AD-5, had been in production
since 2001.[^eflash-brief][^qtp-021507] S8 carries SONOS to 0.13 µm. Cypress wrote in 2008 that its
SONOS module can be added "into a logic process flow or an SRAM process flow with the addition of three
to five masking layers" (single source).[^chipest-2008]

**3. The 110 Å gate oxide.** S8 has two gate oxides, 110 Å and 32 Å.[^qtp-113005] The 110 Å oxide is the
gate oxide of S4AD-5 and of the 0.42 µm R42HD and RAM42 processes of 1997 onwards (Cypress's
reports).[^qtp-021507][^qtp-102101][^qtp-030206] C8 instead pairs 32 Å with 55 Å.[^qtp-043004] The SKY130
PDK says its high-voltage devices "use 110A gate oxide thickness".[^pdk-hv]

## Side by side

| | S4AD-5 (2001) | C8Q-3R (2005) | S8TNV-5R (2008) | SKY130 PDK |
|---|---|---|---|---|
| Design rule | 0.35 µm (one report 0.5 µm) | 0.13 µm | 0.13 µm | 130 nm |
| Non-volatile memory | SONOS | none | SONOS | SONOS |
| Metal layers | 2 | 4 | 3 | 5 |
| Gate oxides | 110 Å | 32 Å and 55 Å | 110 Å and 32 Å | 110 Å for 5 V devices |
| Metal 1 | 500 Å Ti / 6000 Å Al–Cu / 1200 Å TiW | 100 Å Ti / 3200 Å Al–Cu / 300 Å TiW | 100 Å Ti / 3200 Å Al–Cu / 300 Å TiW | 0.36 µm thick |
| Passivation | 3000 Å TEOS / 6000 Å nitride | 1000 Å TEOS / 9000 Å nitride | 7000 ± 2000 Å nitride | — |

The values are as the reports and the PDK print them.[^qtp-021507][^qtp-043004][^qtp-113005][^pdk-hv][^pdk-metal-stack]
The S8 column is the one S8 report found in public; other S8 variants have more metal layers (see the
SKY130 overview). S8's first metal adds up to 0.36 µm (our arithmetic), the thickness the PDK draws for
`met1`.[^qtp-113005][^pdk-metal-stack] The same 0.36 µm recipe is used in Cypress's 90 nm reports of
2006 and 2007.[^qtp-063807][^qtp-061806]

## What does the "8" mean?

The SKY130 PDK says `s8` "stood for the "8th generation" of the SONOS technology developed originally by
Cypress".[^pdk-previous] The Cypress sources point elsewhere:

* **One SONOS process before S8.** The only earlier SONOS process in the sources is S4AD-5 at 0.35 µm;
  Cypress's own lists of processes from 2002 to 2006 name just one SONOS process.[^qtp-021507][^ar-fy2006]
* **The digit follows the process generation.** Cypress named its SRAM processes RAM3 (0.5 µm), RAM5
  (0.25 µm), RAM 7 and RAM 8 (0.13 µm).[^ar-fy1995][^ar-fy1998][^ar-fy2002] The 0.13 µm families are C8,
  R8, S8 and L8, and the 90 nm ones C9, R9 and R95.[^pin-152804] S4 was built on the 0.35 µm R42D
  process.[^qtp-021507]

We read the "8" as Cypress's eighth process generation, the 0.13 µm one, and the "S" as SONOS, just as
S4 was the SONOS process of the fourth generation (our reading). SkyWater's statement and this reading
disagree; no Cypress source found explains the name directly. The naming is set out on
{ref}`history-naming`.

## Open questions

* **C8 and S8.** Was S8 built on C8, on R8, or on both?
* **The medium oxide.** When and why did S8 replace C8's 55 Å oxide with the 110 Å oxide of S4AD-5?
* **SONOS generations.** Were there SONOS processes between S4AD-5 and S8 that no public source
  records?

## References

### Cross-check

* [SkyWater PDK, *Previous Nomenclature*](<https://skywater-pdk.readthedocs.io/en/main/previous.html>) — what `s8` stood for, in SkyWater's words.[^pdk-previous]
* [Cypress, PIN152804](<https://media.futureelectronics.com/PCN/45887_SPCN.PDF>) — the 0.13 µm families together.[^pin-152804]

### High-level understanding

* [Electronics Weekly, *Cypress 4-Mbit non-volatile static random access memory*](<https://www.electronicsweekly.com/news/products/memory-products/cypress-4-mbit-non-volatile-static-random-access-memory-2007-10/>) — the first S8 products.[^ew-2007-s8]
* [Infineon, *20 years of PSoC*](<http://web.archive.org/web/20250713043850/https://www.infineon.com/cms/en/product/promopages/20-years-of-psoc/how-it-started/>) — PSoC 1 and PSoC 3 processes.[^psoc-history]

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
    <http://web.archive.org/web/20250713043850/https://www.infineon.com/cms/en/product/promopages/20-years-of-psoc/how-it-started/>
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
[^qtp-063807]: Cypress Semiconductor, Product Qualification Report QTP 063807: *1 Meg Fast Asynchronous SRAM Family, C9FD-3R Technology, Fab4*, Jan 2024.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-063807-1-meg-fast-asynchronous-sram-family-c9fd-3r-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149f5380c45>
[^qtp-061806]: Cypress Semiconductor, Product Qualification Report QTP 061806: *4 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4*, March 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-061806-4-meg-mobl-sram-automotive-devices-r95ld-3r-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714fdec718db>
