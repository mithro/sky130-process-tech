(history-technologies)=
# Cypress's process generations, 1984–2008

Cypress developed its own processes, one generation after another, for SRAMs first and then for
logic, programmable devices and embedded memory. This page goes through the generations before S8:
what each was called, where it ran, what was made on it, and what its stackup looked like. The
stackups are copied in full on {ref}`history-stackups`; the naming is explained on
{ref}`history-naming`.

## At a glance

| Design rule | Cypress names | Main fabs | First dated in the sources | Section |
|---|---|---|---|---|
| 1.2–0.65 µm | CMOS, BiCMOS, Flash; R28, L28, P26 | Fab 1, Fab 2, Fab 3 | 1984 | [Before 0.5 µm](#before-0-5-um) |
| 0.5 µm | RAM3: R32, R32D | Fab 1, Fab 4 | 1995 | [RAM3](#ram3-0-5-um) |
| 0.42–0.35 µm | RAM4: R42D, R42HD, RAM42; S4AD-5 | Fab 4, Fab 2 | 1997 | [RAM4](#ram4-0-42-and-0-35-um) |
| 0.25 µm | RAM5: R52 variants; B53D-3 | Fab 4 | 1998 | [RAM5](#ram5-0-25-um) |
| 0.18–0.15 µm | RAM7: R7FT-3R, R7LD-1.8, R7FD-3R; B55SGT | Fab 4 | 2001 | [RAM7](#ram7-0-18-to-0-15-um) |
| 0.13 µm | RAM8: R8LD-1.8; C8: C8Q-3R, L8C-3R; S8 | Fab 4 | 2002 | [RAM8 and C8](#ram8-and-c8-0-13-um) |
| 90 nm | R9T-3R, R9Q-3R, C9FD-3R, R95LD-3R | Fab 4 | 2004 | [90 nm](#the-90-nm-generation) |

The SONOS process S4AD-5 has its own page, {ref}`history-sonos-s4`. The dates in the table are the
earliest found in the sources for each generation, not necessarily its first use.

## Before 0.5 µm

**The first processes.** Cypress's first product, early in 1984, was a CMOS memory made with
"1.2 microns" transistors (single source).[^fu-cypress] By 1993 Cypress listed "proprietary 0.65,
0.8 and 1.2-micron CMOS, 0.8 and 0.5-micron BiCMOS and 0.65-micron Flash technologies" in three
fabs.[^ar-fy1993] The same report names 0.8 µm and 0.65 µm as its "established" SRAM generations and
0.5 µm as the next one.[^ar-fy1993] No public report found gives the stackups of these early
processes.

**0.65 µm: R28, L28 and P26.** Cypress's reports show three 0.65 µm processes, all with two metal
layers:

* **R28**, an SRAM process: double poly, 165 Å of gate oxide, first at Fab 3 in 1996 and at Fab 2
  from November 1997 (Cypress's reports).[^qtp-096091][^qtp-097476]
* **P26**, for PROMs and EPROMs such as the CY27C256A, at Fab 2: 165 Å of gate oxide (single
  source).[^qtp-096411]
* **L28**, for clock and logic parts, "New Technology L28" at Fab 2 in April 1998: single poly,
  145 Å of gate oxide (Cypress's reports).[^qtp-011503][^qtp-098333]

L28 was moved to TSMC in 2003. The TSMC version keeps the name and the 0.65 µm rule, but its metal
stack, passivation and 125 Å gate oxide differ from the Fab 2 version (Cypress's reports).[^qtp-080608][^qtp-011503]

The metal of these processes is aluminium–silicon between TiW layers: R28's first metal is
"Ti/TiW/AL-Si/TiW, 500A/1200A/6000A/1200A" (Cypress's reports).[^qtp-096091][^qtp-097476]

## RAM3, 0.5 µm

Cypress's own name for its 0.5 µm SRAM process was RAM3. The 1995 annual report defines it as a
process "allowing the fabrication of ICs having 0.5-micron feature geometry", and the 1996 report
says it was released "in early 1995", was developed in the Fab I R&D fab and was "already" being
made "at a leading-edge 0.35-micron size" (Cypress's reports).[^ar-fy1995][^ar-fy1996] EE Times
dates Cypress's first 0.5 µm products to 1996.[^eet-1997-sram035]

The qualification reports call the 0.5 µm SRAM process R32 (one metal layer) and R32D (two metal
layers, with local interconnect), both with 145 Å of gate oxide and both at Fab 4 (Cypress's
reports).[^qtp-097132][^qtp-098021] That R32 is RAM3 is our reading of the matching name and design
rule; no report says so.

## RAM4, 0.42 and 0.35 µm

EE Times reported Cypress's "first SRAM built in a 0.35-µm feature size", the CY7C1021, on
1997-11-18.[^eet-1997-sram035] Cypress's 1997 report lists RAM4 among its trademarks.[^ar-fy1997]
The qualification reports show three processes of this generation at Fab 4:

* **R42D**, "New R42D Technology Qualification" in October 1997; two metal layers, 0.35 µm, 70 Å of
  gate oxide; FIFOs, clock generators and SRAMs (Cypress's reports).[^qtp-097483][^qtp-003907]
* **R42HD**, qualified in November 1997 with a 1 Mbit SRAM; two metal layers, 0.42 µm, 110 Å of
  gate oxide; dual-port SRAMs (Cypress's reports).[^qtp-098368][^qtp-102101]
* **RAM42**, a single-metal 0.42 µm version with 110 Å of gate oxide for the CY62256 256 Kbit SRAM,
  which moved to Grace in 2009 (Cypress's reports).[^qtp-030206][^qtp-091302]

The metal stack of R42D and R42HD is TiW, aluminium–copper and TiW: "500Å TiW/6000Å Al -5%Cu/1200Å
TiW" for metal 1 (Cypress's reports).[^qtp-003907][^qtp-102101] The reports print "-5%Cu"; other
reports of the time print "0.5% Cu".

**S4AD-5.** Cypress's first SONOS process was built on this generation. Its reports describe it as
an "R42D-5 derivative w/ 6 additional mask" (single source).[^qtp-021507] It is covered on
{ref}`history-sonos-s4`.

## RAM5, 0.25 µm

Cypress's 1998 report defines RAM5 as a process "with 0.25-micron feature geometry" and says it
shipped "first revenue on our 0.25-micron technology" in the fourth quarter of 1998.[^ar-fy1998]
EE Times had reported working 0.25 µm silicon in November 1997.[^eet-1997-sram035] In the
qualification reports this generation is R52, in several variants, all at Fab 4 (Cypress's
reports):[^qtp-062201][^qtp-099202][^qtp-012705][^qtp-082506]

| Variant | First dated row | Metal layers | Gate oxide | Products |
|---|---|---|---|---|
| R52LD-3 | "New Technology R52LD-3", April 1999 | 2 | 55 Å | low-power MoBL SRAMs |
| R52D-3 | September 1999 | 2 | 50 Å | 3.3 V dual-port SRAMs |
| R52FD-3, then R52FFD-3 | October 2000; "New Technology Derivative R52FFD-3", June 2001 | 2 | 55 Å | fast SRAMs |
| R52T-3 | "Process Derivative Qual", May 2003 | 3 | 55 Å | PCI Express clocks |

Two things change in this generation. The metal stacks start using a CoTi or Ti underlayer below
the aluminium–copper, and the gate oxide drops to 50–55 Å.[^qtp-099202][^qtp-082506]

**BiCMOS.** Cypress's 1998 report describes "a new, 0.25-micron BiCMOS process technology" with
bipolar transistors up to 25 GHz.[^ar-fy1998] A Fab 4 process called B53D-3, "New Technology,
B53D-3" in August 2000 and printed as 0.25 µm CMOS, was used for WirelessUSB radio chips and
clock parts. That B53D-3 is the BiCMOS process is our reading: the report does not say
"BiCMOS".[^qtp-032005]

## RAM7, 0.18 to 0.15 µm

Cypress began developing 0.18 µm in 1998 and 0.16 µm in 1999.[^ar-fy1998][^ar-fy1999] Its 2001 report
says it was "ramping our latest 0.15-micron technology in manufacturing".[^ar-fy2001] Its 2002 report
calls the process RAM 7.[^ar-fy2002] The qualification reports show three R7 processes at Fab 4,
all with 32 Å of gate oxide (Cypress's reports):[^qtp-012801][^qtp-014807][^qtp-011908]

* **R7LD-1.8**, "New Technology R7LD-1.8", June 2001: 0.16 µm, two metal layers, low-power 1.8 V
  SRAMs.
* **R7FD-3R**, "New Technology Derivative R7FD-3R", December 2001: 0.15 µm, two metal layers, fast
  SRAMs.
* **R7FT-3R**, "New Technology Derivative R7FT-3R (Hot Al)", February 2002: 0.18 µm, three metal
  layers, synchronous dual-port RAMs.

A 2015 Cypress notice calls R7 "250nm R7".[^pin-152804] The R7 reports print 0.18, 0.16 and 0.15 µm,
so the sources disagree on R7's node.

The R7 stacks put 150 Å of titanium under the aluminium and 300 Å of TiW on top, with 1000 Å of TEOS
and 9000 Å of nitride as passivation: the pattern S8 keeps (see {ref}`history-s8-lineage`).[^qtp-011908][^qtp-113005]

**SiGe BiCMOS.** In 2002 Cypress "completed development of 0.20-micron Silicon Germanium ("SiGe")
Bipolar Complementary Metal Oxide Semiconductor ("BiCMOS") technology" at Fab 4.[^ar-fy2002] Its
qualification report, B55SGT ("New Technology B55SGT18A", May 2003), prints the design rule as "CMOS
(0.21 – 0.35 µm), SiGe Bipolar", with three metal layers.[^qtp-051101] The two sources give different
figures.

## RAM8 and C8, 0.13 µm

Cypress and Mosel Vitelic agreed in 2000 to develop 0.13 µm together in Fab 1
(single source).[^eet-2000-mosel] In
2002 Cypress introduced "our RAM 8 manufacturing process in Fab 4", which "reduced our leading edge
line widths from 0.15-micron to 0.13-micron".[^ar-fy2002] The qualification reports show two
0.13 µm families at Fab 4 before S8:

* **R8LD-1.8**, also printed RAM8NLD-1.8: "New Technology R8LD-1.8V" in March 2003, two metal
  layers, 26 Å of gate oxide, low-power SRAMs (Cypress's reports).[^qtp-024110][^qtp-041406]
* **C8**, a logic process. "New C8Q-3R Technology" was qualified in January 2005, and L8C-3R is
  called a "Technology Derivative of the C8 Technology". Both have four metal layers and a dual gate
  oxide of 32 Å and 55 Å, and were used for clock and PLL parts (Cypress's reports).[^qtp-043004][^qtp-053301]

In 2006 Cypress began moving "its 0.13-micron C8 process technology" to Grace for USB and clock
chips.[^eet-2006-c8] A 2015 notice lists "130nm C8/R8/S8/L8" as the 0.13 µm families at Fab 4.[^pin-152804]
S8 is the fourth of these; how it relates to the other three is on {ref}`history-s8-lineage`.

## The 90 nm generation

Cypress's 90 nm process was developed in Fab 1 and moved to Fab 4 from 2002; its 2004 report says it
was "now in production at our Minnesota facility".[^ar-fy2002][^ar-fy2004] The qualification
reports show four 90 nm processes at Fab 4, qualified from 2004 to 2007 (Cypress's reports):[^qtp-032003][^qtp-051207][^qtp-063807][^qtp-061806]

* **R9T-3R** and **R9Q-3R**: three and four metal layers, nitrided gate oxide of 22 Å, synchronous and
  QDR SRAMs.
* **C9FD-3R**: two metal layers, 23 Å of gate oxide, fast SRAMs.
* **R95LD-3R**: two metal layers, 28 Å of gate oxide, low-power SRAMs.

These processes were developed alongside S8, not before it. They matter here because their first
metal layer, "100Å Ti / 3200Å Al / 300Å TiW", is the same as S8's (Cypress's reports).[^qtp-063807][^qtp-113005]

## Other processes

* **Silicon on insulator.** Cypress and Honeywell developed an SOI process together from 2002; the
  sources disagree on its node (see {ref}`history-fabs`).[^ar-fy2002][^edn-2005-honeywell]
* **Foundry processes.** Some products were made on foundry processes: Hyundai's 0.5 µm three-metal
  process, ProMOS's 0.17 µm S17, Powerchip's 0.16 µm with a stacked capacitor, and Chartered's
  0.35 µm (Cypress's reports).[^qtp-001004][^qtp-032301][^qtp-051501][^qtp-i000005] They are not
  Cypress processes and are listed only for completeness.

## Open questions

* **R28, L28 and P26.** Which name did Cypress give the 0.65 µm generation (a "RAM2")? No source found
  says.
* **RAM4 and R42.** Is R42 the process Cypress called RAM4? The names match, but no source says so.
* **R7's node.** Is R7 the 0.25 µm process of the 2015 notice or the 0.18–0.15 µm processes of the
  reports?
* **The early stackups.** What were the stackups of the 1.2 µm and 0.8 µm processes?

## References

### Cross-check

* [Cypress, Form 10-K for fiscal 1993](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1994.pdf>) — the process generations of 1993.[^ar-fy1993]
* [Cypress, 2002 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2002.pdf>) — RAM 7, RAM 8 and the 90 nm transfer.[^ar-fy2002]
* [Cypress, PIN152804](<https://media.futureelectronics.com/PCN/45887_SPCN.PDF>) — the families at Fab 4 in 2015.[^pin-152804]

### High-level understanding

* [EE Times, *Cypress Introduces its First 0.35-µm SRAM*](<https://www.eetimes.com/cypress-introduces-its-first-0-35-m-sram/>) — the 0.5 µm, 0.35 µm and 0.25 µm dates.[^eet-1997-sram035]
* [FundingUniverse, *History of Cypress Semiconductor Corporation*](<https://www.fundinguniverse.com/company-histories/cypress-semiconductor-corporation-history/>) — the first product in 1984.[^fu-cypress]

### Deep dive

* [Cypress, 1995 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1995.pdf>) — RAM3 defined.[^ar-fy1995]
* [Cypress, 1996 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1996.pdf>) — RAM3's release and shrink to 0.35 µm.[^ar-fy1996]
* [Cypress, 1998 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1998.pdf>) — RAM5 and the 0.25 µm BiCMOS process.[^ar-fy1998]
* [Cypress, QTP 96091](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-96091-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148ab080847>) — R28 at Fab 3.[^qtp-096091]
* [Cypress, QTP 011503](<https://web.archive.org/web/20201205124212/https://www.cypress.com/file/91641/download>) — L28 at Fab 2.[^qtp-011503]
* [Cypress, QTP 97132](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97132-32k-x-8-low-power-sram-r32-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714947ff09f5>) — R32.[^qtp-097132]
* [Cypress, QTP 003907](<https://www.infineon.com/dgdl/Infineon-QTP_003907_High_Frequency_Programmable_PECL_Clock_Generator_R42LDHA_Technology_Fab_4-ProductQualificationReport-v02_00-EN.pdf?fileId=8ac78c8c7d710014017d714957940a14>) — R42D.[^qtp-003907]
* [Cypress, QTP 102101](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-102101-synchronous-asynchronous-dual-port-sram-3.3v-and-5v-r42hd-technology-fab-4-qualification-productqualificationreport-en.pdf>) — R42HD.[^qtp-102101]
* [Cypress, QTP 012705](<https://www.infineon.com/dgdl/Infineon-QTP_012705_1MEG_SRAM_FAST_ASYNCHRONOUS_FAMILY_R52FFD-3_TECHNOLOGY_FAB_4-ProductQualificationReport-v02_00-EN.pdf?fileId=8ac78c8c7d710014017d7148db7c0893>) — R52FFD-3.[^qtp-012705]
* [Cypress, QTP 011908](<https://www.infineon.com/dgdl/Infineon-QTP_011908_Fast_Asynchronous_SRAM_Technology_Derivative_R7FD_Fab_4_Qualification-ProductQualificationReport-v02_00-EN.pdf?fileId=8ac78c8c7d710014017d7150e6271aff>) — R7FD-3R.[^qtp-011908]
* [Cypress, QTP 053301](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-053301-l8c-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149c4a70b8f>) — L8C-3R, a derivative of C8.[^qtp-053301]
* [Cypress, QTP 051207](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-051207-18-meg-qdr-synchronous-sram--cy7c1313d-product-family--r9q-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148e37b08a2>) — R9Q-3R.[^qtp-051207]
* [EE Times, *Cypress transfers 130-nm process to Grace*](<https://www.eetimes.com/cypress-transfers-130-nm-process-to-grace/>) — C8 moved to Grace.[^eet-2006-c8]

<!-- footnotes -->

[^fu-cypress]: FundingUniverse (from the *International Directory of Company Histories*), *History
    of Cypress Semiconductor Corporation*, retrieved 2026-09-25.
    <https://www.fundinguniverse.com/company-histories/cypress-semiconductor-corporation-history/>
[^ar-fy1993]: Cypress Semiconductor Corp., Form 10-K for the fiscal year ended 1994-01-03, filed
    1994-03-16, Item 1, Manufacturing and Research and development.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1994.pdf>
[^ar-fy1995]: Cypress Semiconductor Corp., *1995 Annual Report*, fiscal year ended 1996-01-01:
    shareholder letter, highlights timeline and notes on commitments and subsidiaries.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1995.pdf>
[^ar-fy1996]: Cypress Semiconductor Corp., *1996 Annual Report*, fiscal year ended 1996-12-29:
    Business Highlights timeline (Q1 and Q3) and restructuring note.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1996.pdf>
[^ar-fy1997]: Cypress Semiconductor Corp., *1997 Annual Report*, fiscal year ended 1997-12-28:
    manufacturing section and restructuring note.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1997.pdf>
[^ar-fy1998]: Cypress Semiconductor Corp., *1998 Annual Report*, fiscal year ended 1999-01-03:
    president's letter and restructuring discussion.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1998.pdf>
[^ar-fy1999]: Cypress Semiconductor Corp., *1999 Annual Report*, fiscal year ended 2000-01-02:
    Liquidity and Capital Resources.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1999.pdf>
[^ar-fy2001]: Cypress Semiconductor Corp., *2001 Annual Report*, fiscal year ended 2001-12-30:
    research and development.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2001.pdf>
[^ar-fy2002]: Cypress Semiconductor Corp., *2002 Annual Report* with Form 10-K, fiscal year ended
    2002-12-29: Item 1, Research and development and Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2002.pdf>
[^ar-fy2004]: Cypress Semiconductor Corp., *2004 Annual Report* with Form 10-K, fiscal year ended
    2005-01-02: Item 1, Research and development.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2004.pdf>
[^eet-1997-sram035]: EE Times, *Cypress Introduces its First 0.35-µm SRAM*, 1997-11-19.
    <https://www.eetimes.com/cypress-introduces-its-first-0-35-m-sram/>
[^eet-2000-mosel]: EE Times, *Cypress, Mosel Vitelic to develop 0.13-micron process technology*,
    2000-07-07.
    <https://www.eetimes.com/cypress-mosel-vitelic-to-develop-0-13-micron-process-technology/>
[^eet-2006-c8]: Mark LaPedus, *Cypress transfers 130-nm process to Grace*, EE Times, 2006-07-19.
    <https://www.eetimes.com/cypress-transfers-130-nm-process-to-grace/>
[^edn-2005-honeywell]: Mark LaPedus, *Honeywell debuts rad-hard process in new foundry fab*, EDN,
    2005-04-27. <https://www.edn.com/honeywell-debuts-rad-hard-process-in-new-foundry-fab/>
[^pin-152804]: Cypress Semiconductor, Product Information Notification PIN152804, *Qualification of
    GlobalWafer Silicon Wafers for 250nm, 130nm and 90nm Technology Products at Cypress Fab 4*,
    2015-07-12 (copy hosted by Future Electronics).
    <https://media.futureelectronics.com/PCN/45887_SPCN.PDF>
[^qtp-096091]: Cypress Semiconductor, Product Qualification Report QTP 96091: *Dual Port SRAM - R28 Technology, 6% Shrink*, September 1996.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-96091-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148ab080847>
[^qtp-097476]: Cypress Semiconductor, Product Qualification Report QTP 97476: *256K STATIC RAM "CY7C194/CY7195/CY7C199" R28 PROCESS, FAB 2 QUALIFICATION*, August 2016.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97476-256k-static-ram-r28-process-fab-2-qualification-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7150d8bb1af5>
[^qtp-096411]: Cypress Semiconductor, Product Qualification Report QTP 96411: *256K/512K PROM - P26 Technology*, May 1997;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201026124735/https://www.cypress.com/file/93566/download>
[^qtp-011503]: Cypress Semiconductor, Product Qualification Report QTP 011503: *Spread Spectrum Timing Solution for Serverworks Chipset, L28 Technology, Fab 2*, December 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205124212/https://www.cypress.com/file/91641/download>
[^qtp-098333]: Cypress Semiconductor, Product Qualification Report QTP 98333: *100-MHz Spread Spectrum Clock Synthesizer/Driver, USB, Hublink and SDRAM Support (CY2287PVC), Fab2, L28 Technology*, August 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205131229/https://www.cypress.com/file/94086/download>
[^qtp-080608]: Cypress Semiconductor, Product Qualification Report QTP 080608: *High Accuracy EPROM Programmable Device Family, L28 Technology, TSMC-2A*, May 2013.
    <https://www.infineon.com/dgdl/Infineon-QTP_080608_HIGH_ACCURACY_EPROM_PROGRAMMABLE_DEVICE_FAMILY_L28_TECHNOLOGY_TSMC-2A-ProductQualificationReport-v01_00-EN.pdf?fileId=8ac78c8c7d710014017d714a27090cd2>
[^qtp-097132]: Cypress Semiconductor, Product Qualification Report QTP 97132: *32K x 8 Low Power SRAM, R32 Technology, Fab4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97132-32k-x-8-low-power-sram-r32-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714947ff09f5>
[^qtp-098021]: Cypress Semiconductor, Product Qualification Report QTP 98021: *1 Meg SRAM (5% Shrink), R32D Technology, Fab 4 -- Military Devices*, July 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507141403/https://www.cypress.com/file/93501/download>
[^qtp-097483]: Cypress Semiconductor, Product Qualification Report QTP 97483: *Low Voltage Deep Synchronous FIFO High Speed 100-MHZ Operation, R42D -- Fab 4*, May 2017.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97483-low-voltage-deep-sync-fifos-r42d-technology-fab4-device-cy7c42-v-productqualificationreport-en.pdf>
[^qtp-003907]: Cypress Semiconductor, Product Qualification Report QTP 003907: *High Frequency Programmable PECL Clock Generator R42LDHA Technology, Fab 4*, June 2013.
    <https://www.infineon.com/dgdl/Infineon-QTP_003907_High_Frequency_Programmable_PECL_Clock_Generator_R42LDHA_Technology_Fab_4-ProductQualificationReport-v02_00-EN.pdf?fileId=8ac78c8c7d710014017d714957940a14>
[^qtp-098368]: Cypress Semiconductor, Product Qualification Report QTP 98368: *SYNCHRONOUS/ASYNCHRONOUS DUAL PORT SRAM (3.3V AND 5V), R42HD TECHNOLOGY, FAB 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-98368-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152cc652012>
[^qtp-102101]: Cypress Semiconductor, Product Qualification Report QTP 102101: *Synchronous/Asynchronous Dual Port SRAM (3.3V and 5V), R42HD Technology, Fab 4 Qualification*, July 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-102101-synchronous-asynchronous-dual-port-sram-3.3v-and-5v-r42hd-technology-fab-4-qualification-productqualificationreport-en.pdf>
[^qtp-030206]: Cypress Semiconductor, Product Qualification Report QTP 030206: *256K Static RAM Automotive Devices, RAM42HHA Technology, Fab 4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030206-256k-static-ram-automotive-devices-ram42hha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71491e3d0986>
[^qtp-091302]: Cypress Semiconductor, Product Qualification Report QTP 091302: *MoBL Asynchronous SRAM Product Family, RAM42HNHA Technology, Fab5 GSMC*, February 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-091302-mobl-asynchronous-sram-product-family-cy62256-ram42hnha-technology-fab5-gsmc-productqualificationreport-en.pdf?fileId=8ac78c8c93dda25b01953e8470a271d4>
[^qtp-021507]: Cypress Semiconductor, Product Qualification Report QTP 021507: *Failsafe Device Family & Options S4AD-5 SONOS Technology, Fab 2*, December 2015.
    <https://www.infineon.com/dgdl/Infineon-QTP_021507_Failsafe_Device_Family_&_Options_S4AD-5_SONOS_Technology_Fab_2-ProductQualificationReport-v02_00-EN.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>
[^qtp-062201]: Cypress Semiconductor, Product Qualification Report QTP 062201: *MoBL ADM Dual Port Static RAM Family, R52LD-3 Technology, Fab4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-062201-mobl-adm-dual-port-static-ram-family-r52ld-3-technology-fab4-productqualificationreport-en.pdf>
[^qtp-099202]: Cypress Semiconductor, Product Qualification Report QTP 99202: *Low Voltage Synchronous/Asynchronous RAM, R52D-3 Technology at Fab 4*, May 2014.
    <https://www.infineon.com/dgdl/Infineon-QTP_99202_Low_Voltage_Synchronous_Asynchronous_RAM_R52D-3_Technology_at_Fab_4-ProductQualificationReport-v03_00-EN.pdf?fileId=8ac78c8c7d710014017d71491c270982>
[^qtp-012705]: Cypress Semiconductor, Product Qualification Report QTP 012705: *1MEG SRAM Fast Asynchronous Family, R52FFD-3 Technology, Fab 4*, June 2014.
    <https://www.infineon.com/dgdl/Infineon-QTP_012705_1MEG_SRAM_FAST_ASYNCHRONOUS_FAMILY_R52FFD-3_TECHNOLOGY_FAB_4-ProductQualificationReport-v02_00-EN.pdf?fileId=8ac78c8c7d710014017d7148db7c0893>
[^qtp-082506]: Cypress Semiconductor, Product Qualification Report QTP 082506: *PCI-E Clock Family, R52T-3 Technology, Fab 4*, September 2014.
    <https://www.infineon.com/dgdl/Infineon-QTP_082506_PCI-E_Clock_Family_R52T-3_Technology_Fab_4-ProductQualificationReport-v03_00-EN.pdf?fileId=8ac78c8c7d710014017d714a4cbb0d39>
[^qtp-032005]: Cypress Semiconductor, Product Qualification Report QTP 032005: *WirelessUSB Device Family, B53D-3RF Technology, Fab 4*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211206184334/https://www.cypress.com/file/92296/download>
[^qtp-012801]: Cypress Semiconductor, Product Qualification Report QTP 012801: *4 Meg SRAM Device R7LD-1.8 Technology, Fab4*, October 2004;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210302225236/https://www.cypress.com/file/91706/download>
[^qtp-014807]: Cypress Semiconductor, Product Qualification Report QTP 014807: *Technology Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM CY7C085xV / CY7C083xV*, June 2005.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
[^qtp-011908]: Cypress Semiconductor, Product Qualification Report QTP 011908: *Fast Asynchronous SRAM Technology Derivative R7FD, Fab 4 Qualification*, August 2014.
    <https://www.infineon.com/dgdl/Infineon-QTP_011908_Fast_Asynchronous_SRAM_Technology_Derivative_R7FD_Fab_4_Qualification-ProductQualificationReport-v02_00-EN.pdf?fileId=8ac78c8c7d710014017d7150e6271aff>
[^qtp-113005]: Cypress Semiconductor, Product Qualification Report QTP 113005: *64K Serial Non-Volatile SRAM Product Family, S8 Technology, CMI (Fab 4)*, January 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^qtp-051101]: Cypress Semiconductor, Product Qualification Report QTP 051101: *FastEdge Series, B55SGT Technology, Fab 4*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201028052046/https://www.cypress.com/file/92676/download>
[^qtp-024110]: Cypress Semiconductor, Product Qualification Report QTP 024110: *1 MEG (3.0V) MOBL DEVICES RAM8NLD-1.8V TECHNOLOGY, FAB4*, June 2013.
    <https://www.infineon.com/dgdl/Infineon-QTP_024110_1_MEG_(3.0V)_MOBL_DEVICES_RAM8NLD-1.8V_TECHNOLOGY_FAB4-ProductQualificationReport-v01_00-EN.pdf?fileId=8ac78c8c7d710014017d7152a1d61fde>
[^qtp-041406]: Cypress Semiconductor, Product Qualification Report QTP 041406: *4 MEG (1.8V/3.0V) MOBL DEVICES, RAM8NLD-1.8 TECHNOLOGY, Skywater*, February 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-041406-4-meg-1-8v-3-0v-mobl-devices-ram8nld-1-productqualificationreport-en.pdf>
[^qtp-043004]: Cypress Semiconductor, Product Qualification Report QTP 043004: *DDR2-PLL Device Family, C8Q-3R, Fab 4*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205122906/https://www.cypress.com/file/92151/download>
[^qtp-053301]: Cypress Semiconductor, Product Qualification Report QTP 053301: *L8C-3R Technology, Fab 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-053301-l8c-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149c4a70b8f>
[^qtp-032003]: Cypress Semiconductor, Product Qualification Report QTP 032003: *36 Meg Synchronous SRAM Family, Technology R9T-3R, Fab4*, August 2014.
    <https://www.infineon.com/dgdl/Infineon-QTP_032003_36_Meg_Synchronous_SRAM_Family_Technology_R9T-3R_Fab4-ProductQualificationReport-v04_00-EN.pdf?fileId=8ac78c8c7d710014017d714983cb0ac5>
[^qtp-051207]: Cypress Semiconductor, Product Qualification Report QTP 051207: *18 MEG QDR SYNCHRONOUS SRAM FAMILY, R9Q-3R TECHNOLOGY, FAB4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-051207-18-meg-qdr-synchronous-sram--cy7c1313d-product-family--r9q-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148e37b08a2>
[^qtp-063807]: Cypress Semiconductor, Product Qualification Report QTP 063807: *1 Meg Fast Asynchronous SRAM Family, C9FD-3R Technology, Fab4*, Jan 2024.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-063807-1-meg-fast-asynchronous-sram-family-c9fd-3r-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149f5380c45>
[^qtp-061806]: Cypress Semiconductor, Product Qualification Report QTP 061806: *4 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4*, March 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-061806-4-meg-mobl-sram-automotive-devices-r95ld-3r-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714fdec718db>
[^qtp-001004]: Cypress Semiconductor, Product Qualification Report QTP 001004: *0.5um TLM Technology, Fab HME, Dual Port SRAM with PCI Bus Controller*, January 2001.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-001004-productqualificationreport-en.pdf>
[^qtp-032301]: Cypress Semiconductor, Product Qualification Report QTP 032301: *16 MEG A/D MUX SRAM, S17 Technology, Promos Fab in Taiwan*, May 2004;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201204235131/https://www.cypress.com/file/92311/download>
[^qtp-051501]: Cypress Semiconductor, Product Qualification Report QTP 051501: *Cypress Minnesota (CMI) Sort Site Qualification -- 2 Meg, 3V PSRAM Device, PowerChip 0.165µm*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201028052812/https://www.cypress.com/file/92636/download>
[^qtp-i000005]: Cypress Semiconductor, Product Qualification Report QTP I000005: *0.35um Technology, CSM Fab 2*, October 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-i000005-0.35um-technology-csm-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152d1a52016>
