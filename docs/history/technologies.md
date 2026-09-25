(history-technologies)=
# Cypress's process generations, 1984–2008

Cypress developed its own processes, one generation after another, for SRAMs first and then for logic,
programmable devices and embedded memory. This page goes through the generations before S8: what each
was called, where it ran, what was made on it, and what its stackup looked like. The stackups are copied
in full on {ref}`history-stackups`, the products on {ref}`history-products`, and the naming is discussed
on {ref}`history-naming`.

## At a glance

| Design rule | Process codes in the reports | Main fabs | Earliest date in the sources |
|---|---|---|---|
| 1.2 µm and 0.8 µm | P20 (0.8 µm) | Fab 1, Fab 2 | 1.2 µm in 1984; 0.8 µm in production by 1988 |
| 0.65 µm | R28, L28, P26 | Fab 2, Fab 3 | "established" in 1993 |
| 0.5 µm | R32, R32D | Fab 1, Fab 4 | "emerging" in 1993; RAM3 released in 1995 |
| 0.42 µm and 0.35 µm | R42D, R42HD, RAM42; S4AD-5 | Fab 4, Fab 2 | 0.35 µm SRAMs in production by early 1997 |
| 0.25 µm | R52 variants, B53D-3, B55SGT | Fab 4 | working silicon in 1997 |
| 0.18 µm to 0.15 µm | R7LD-1.8, R7FD-3R, R7FT-3R | Fab 4 | development from 1998 |
| 0.13 µm | R8LD-1.8, C8Q-3R, L8C-3R; S8 | Fab 4 | development from 2000 |
| 90 nm | R9T-3R, R9Q-3R, C9FD-3R, R95LD-3R | Fab 4 | moved to Fab 4 in 2002 |

The sections below give each row's sources. Which code belongs to which generation is our reading of
the design rules the reports print (see {ref}`history-naming`). The SONOS process S4AD-5 has its own page,
{ref}`history-sonos-s4`.

(history-tech-early)=
## 1.2 µm to 0.8 µm

Cypress's 1988 data book describes its first process: "a 1.2 micron "N" well technology with double layer
poly, and a single layer metal", with lightly doped source and drain extensions. The same book says a
0.8 µm process was in production, and lists "multi-layer metal interconnections", silicides and plasma
etching as recent innovations (single source).[^databook-1988] The Gale company history dates the first product, a
1.2 µm CMOS memory, to early 1984.[^fu-cypress]

The 1988 book's PROMs and programmable logic used "an EPROM programming element".[^databook-1988] By 1993
Cypress listed "proprietary 0.65, 0.8 and 1.2-micron CMOS, 0.8 and 0.5-micron BiCMOS and 0.65-micron
Flash technologies".[^ar-fy1993]

**P20.** The one 0.8 µm process in the qualification reports is P20, at Fab 2, for the CY7C344 and
CY7C346 MAX EPLDs: two metal layers and 195 Å of gate oxide (Cypress's reports).[^qtp-091216][^qtp-093332]
Its history lists a 1993 military qualification "with ONO" without saying what the ONO was for.[^qtp-091216]
No report found covers the 1.2 µm process.

(history-tech-065)=
## 0.65 µm: R28, L28 and P26

Cypress's 1993 10-K calls 0.8 µm and 0.65 µm its "established" SRAM geometries (single
source).[^ar-fy1993] The reports show three 0.65 µm processes, all with two metal layers (Cypress's
reports):[^qtp-096091][^qtp-096411][^qtp-011503]

* **R28**, an SRAM process: double poly and 165 Å of gate oxide. The earliest R28 reports found are of
  September 1996, at Fab 3; Fab 2 followed in November 1997 (Cypress's reports).[^qtp-096091][^qtp-097476]
* **P26**, for PROMs and EPROMs such as the CY27C256A, at Fab 2: 165 Å of gate oxide (single source).[^qtp-096411]
* **L28**, for clock and logic parts: single poly and 145 Å of gate oxide. One report dates "New
  Technology L28" to February 1996 (Cypress's reports).[^qtp-000901][^qtp-011503]

The metals differ. R28 has aluminium–silicon between TiW layers ("Ti/TiW/AL-Si/TiW,
500A/1200A/6000A/1200A"); P26 and the Fab 2 L28 print plain aluminium with TiW (Cypress's
reports).[^qtp-096091][^qtp-096411][^qtp-011503]

**L28's first fab.** Two reports describe the same April 1998 row differently: "New Technology L28/New
Device CY227*" in one, "Qualified Technology L28 transfer from Fab 3 to Fab 2" in the other. The second, with
the 1996 row, suggests L28 began at Fab 3 and moved to Fab 2 in 1998; the reports disagree (Cypress's
reports).[^qtp-011503][^qtp-031101][^qtp-000901]

L28 was moved to TSMC in 2003. The TSMC version keeps the name and the 0.65 µm rule but uses AlSiCu with
TiN, a different passivation and 125 Å of gate oxide (Cypress's reports).[^qtp-080608][^qtp-011503]

(history-tech-ram3)=
## RAM3, 0.5 µm

Cypress's 1993 10-K calls 0.5 µm its "emerging" SRAM geometry (single source).[^ar-fy1993] Its own name
for the 0.5 µm SRAM process was RAM3. The 1995 annual report defines it as a process "allowing the
fabrication of ICs having 0.5-micron feature geometry". The 1996 report says it was released "in early
1995" and developed in the Fab I R&D fab (Cypress's reports).[^ar-fy1995][^ar-fy1996]

**First products.** EE Times dates Cypress's first 0.5 µm products to 1996, and Cypress's third-quarter
1996 10-Q speaks of ramping its 0.5 µm process "to full commercial production".[^eet-1997-sram035][^tenq-1996q3]

**R32.** The qualification reports call the 0.5 µm SRAM process R32 (one metal layer) and R32D (two metal
layers, with local interconnect), both with 145 Å of gate oxide and both at Fab 4 (Cypress's
reports).[^qtp-097132][^qtp-098021] That R32 is RAM3 is our reading of the matching name and design rule;
no report says so.

(history-tech-ram4)=
## RAM4, 0.42 and 0.35 µm

**The first 0.35 µm SRAM.** The sources disagree on the date. Cypress's 1996 report, published early in
1997, shows 256K SRAMs "manufactured on 0.5-micron and 0.35-micron technologies" and says RAM3 was already
made "at a leading-edge 0.35-micron size". EE Times called the CY7C1021, announced on 1997-11-18, Cypress's
"first SRAM built in a 0.35-µm feature size". The two disagree; the shrunk RAM3 parts and a new 0.35 µm
design may explain it (our reading).[^ar-fy1996][^eet-1997-sram035]

**The R42 processes.** Cypress's 1997 report lists RAM4 among its trademarks.[^ar-fy1997] The qualification
reports show four processes of this generation at Fab 4 (Cypress's reports):[^qtp-097483][^qtp-003907][^qtp-102101][^qtp-030204][^qtp-030206]

* **R42D**, "New R42D Technology Qualification" in October 1997; FIFOs, clocks and SRAMs. Its variant "R42D
  with Hot Al" prints two metal layers, 0.35 µm and 70 Å of gate oxide.
* **R42HD**, November 1997: two metal layers, 0.42 µm, 110 Å of gate oxide; 3.3 V and 5 V dual-port SRAMs.
* **RAM42HA and RAM42HHA**, single-metal 0.42 µm versions for the CY62256 256K SRAM: 70 Å of gate oxide
  for the 3 V part, 110 Å for the 5 V part. RAM42 moved to Grace in 2009 (single source).[^qtp-091302]

**Metal.** The two-metal R42 stacks are TiW, aluminium–copper and TiW: "500Å TiW/6000Å Al -5%Cu/1200Å TiW"
for metal 1 (Cypress's reports).[^qtp-003907][^qtp-102101] The reports print "-5%Cu"; other reports of the
time print "0.5% Cu".

**S4AD-5.** Cypress's first SONOS process was built on this generation. Its report describes it as an
"R42D-5 derivative w/ 6 additional mask" (single source).[^qtp-021507] It is covered on
{ref}`history-sonos-s4`.

(history-tech-ram5)=
## RAM5, 0.25 µm

Cypress's 1998 report defines RAM5 as a process "with 0.25-micron feature geometry" and says it shipped
"first revenue on our 0.25-micron technology" in the fourth quarter of 1998 (single
source).[^ar-fy1998] EE Times had reported working 0.25 µm silicon in November 1997 (single
source).[^eet-1997-sram035]

**Isolation.** A 1999 paper by Cypress's R&D staff describes the "local oxidation of silicon (LOCOS)
process in 0.25 µm static random access memory (SRAM) technology" (single source).[^jin-1999] SKY130 uses
shallow trench isolation instead; when Cypress changed is not in the sources found.

**The R52 processes.** In the qualification reports this generation is R52, in several variants, all at
Fab 4 (Cypress's reports):[^qtp-062201][^qtp-099202][^qtp-012705][^qtp-098462][^qtp-082506]

| Variant | First dated row | Layers, gate oxide | Products |
|---|---|---|---|
| R52LD-3 | "New Technology R52LD-3", April 1999 | 2, 55 Å | low-power SRAMs |
| R52D-3 | September 1999 | 2, 50 Å | 3.3 V dual-port SRAMs |
| R52D-5R | "New Technology Derivative R52D-5R", April 2000 | not printed | fast SRAMs |
| R52FD-3, R52FFD-3 | October 2000; June 2001 | 2, 55 Å | fast SRAMs |
| R52T-3 | "Process Derivative Qual", May 2003 | 3, 55 Å | PCI Express clocks |

The gate oxide drops to 50–55 Å in this generation. Metal 1 keeps 500 Å of TiW under the aluminium, while
the upper metals start using CoTi or Ti (Cypress's reports).[^qtp-099202][^qtp-082506]

**BiCMOS.** Cypress's 1998 report describes "a new, 0.25-micron BiCMOS process technology" with bipolar
transistors up to 25 GHz (single source).[^ar-fy1998] B53D-3, "New Technology, B53D-3" at Fab 4 in August
2000 and printed as 0.25 µm CMOS, made WirelessUSB radio chips and clocks. That it is the BiCMOS process is
our reading; the report does not say "BiCMOS".[^qtp-032005]

**SiGe BiCMOS.** In 2002 Cypress "completed development of 0.20-micron Silicon Germanium ("SiGe")"
BiCMOS at Fab 4. Its qualification report, B55SGT ("New Technology B55SGT18A", May 2003), prints "CMOS
(0.21 – 0.35 µm), SiGe Bipolar", with three metal layers. The two design rules differ.[^ar-fy2002][^qtp-051101]

(history-tech-ram7)=
## RAM7, 0.18 to 0.15 µm

Cypress began developing 0.18 µm in 1998 and 0.16 µm in 1999 (Cypress's reports).[^ar-fy1998][^ar-fy1999]
Its 2001 report says it was "ramping our latest 0.15-micron technology in manufacturing", and its 2002
report calls the process RAM 7 (Cypress's reports).[^ar-fy2001][^ar-fy2002]

The qualification reports show three R7 processes at Fab 4, all with 32 Å of gate oxide (Cypress's
reports):[^qtp-012801][^qtp-011908][^qtp-014807]

* **R7LD-1.8**, "New Technology R7LD-1.8", June 2001: 0.16 µm, two metal layers, low-power 1.8 V SRAMs.
* **R7FD-3R**, "New Technology Derivative R7FD-3R", December 2001: 0.15 µm, two metal layers, fast SRAMs.
* **R7FT-3R**, "New Technology Derivative R7FT-3R (Hot Al)", February 2002: 0.18 µm, three metal layers,
  synchronous dual-port RAMs.

A 2015 Cypress notice calls R7 "250nm R7", while the R7 reports print 0.18, 0.16 and 0.15 µm; the sources
disagree on R7's node.[^pin-152804][^qtp-011908]

**Metal.** The R7 stacks put 150 Å of titanium under the aluminium and 300 Å of TiW on top, with 1000 Å of
TEOS and 9000 Å of nitride as passivation. S8 keeps the titanium, aluminium and TiW sandwich, with 100 Å of
titanium on its first two metals, but its one public report prints a nitride-only passivation of
7000 ± 2000 Å (Cypress's reports).[^qtp-011908][^qtp-113005]

(history-tech-ram8)=
## RAM8 and C8, 0.13 µm

**Development.** Cypress and Mosel Vitelic agreed in 2000 to develop 0.13 µm together in Fab 1 (single
source).[^eet-2000-mosel] Cypress's 2001 report records "0.12-micron technology" moving from Fab 1 to
Minnesota. In 2002 it introduced "our RAM 8 manufacturing process in Fab 4", which "reduced our leading
edge line widths from 0.15-micron to 0.13-micron" (Cypress's reports).[^ar-fy2001][^ar-fy2002] Whether the
0.12 µm technology and RAM 8 are the same process is not said.

**The processes.** The qualification reports show two 0.13 µm families at Fab 4 before S8 (Cypress's
reports):[^qtp-024110][^qtp-043004][^qtp-053301]

* **R8LD-1.8**, also printed RAM8NLD-1.8: "New Technology R8LD-1.8V" in March 2003, two metal layers, 26 Å
  of gate oxide, low-power SRAMs.
* **C8**, a logic process: "New C8Q-3R Technology" in January 2005, and L8C-3R is a "Technology Derivative
  of the C8 Technology". Both have four metal layers and a dual gate oxide of 32 Å and 55 Å, for clock
  and PLL parts.

In 2006 Cypress announced it would move "its 0.13-micron C8 process technology" to Grace, for USB and
clock chips. A 2015 notice lists "130nm C8/R8/S8/L8" as the 0.13 µm families at Fab 4.[^eet-2006-c8][^pin-152804]
S8 is the fourth of these; how it relates to the other three is on {ref}`history-s8-lineage`.

(history-tech-90nm)=
## The 90 nm generation

Cypress moved its 90 nm process from Fab 1 to Fab 4 from 2002, was "ramping" it in 2003, and says in its
2004 report that it was "now in production at our Minnesota facility" (Cypress's
reports).[^ar-fy2002][^ar-fy2003][^ar-fy2004]

The qualification reports show four 90 nm processes at Fab 4,
qualified from 2004 to 2007 (Cypress's reports):[^qtp-032003][^qtp-051207][^qtp-063807][^qtp-061806]

* **R9T-3R** and **R9Q-3R**: three and four metal layers, nitrided gate oxide of 22 Å, synchronous and QDR
  SRAMs.
* **C9FD-3R**: two metal layers, 23 Å of gate oxide, fast SRAMs.
* **R95LD-3R**: two metal layers, 28 Å of gate oxide, low-power SRAMs.

These processes were developed alongside S8, not before it. C9FD-3R and R95LD-3R have the same first
metal as S8, "100Å Ti / 3200Å Al / 300Å TiW"; R9T-3R and R9Q-3R use 150 Å of titanium (Cypress's
reports).[^qtp-063807][^qtp-061806][^qtp-032003][^qtp-113005]

## Other processes

* **Silicon on insulator.** Cypress and Honeywell developed an SOI process together from 2002; the
  sources disagree on its node (see {ref}`history-fabs`).[^ar-fy2002][^edn-2005-honeywell]
* **Foundry processes.** Some products were made on foundry processes: Hyundai's 0.5 µm three-metal
  process, ProMOS's 0.17 µm S17, Powerchip's 0.16 µm with a stacked capacitor, and Chartered's 0.35 µm
  (Cypress's reports).[^qtp-001004][^qtp-032301][^qtp-051501][^qtp-i000005] They are not Cypress processes
  and are listed only for completeness.

## Open questions

* **The early processes.** Which fabs ran the 1.2 µm and 0.8 µm processes, and what were their codes?
* **RAM4 and R42.** Is R42 the process Cypress called RAM4? The names match, but no source says so.
* **R7's node.** Is R7 the 0.25 µm process of the 2015 notice or the 0.18–0.15 µm processes of the
  reports?
* **STI.** When did Cypress change from LOCOS to shallow trench isolation?

## References

### Cross-check

* [Cypress, Form 10-K for fiscal 1993](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1994.pdf>) — the process generations of 1993.[^ar-fy1993]
* [Cypress, 2002 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2002.pdf>) — RAM 7, RAM 8 and the 90 nm transfer.[^ar-fy2002]
* [Cypress, PIN152804](<https://media.futureelectronics.com/PCN/45887_SPCN.PDF>) — the families at Fab 4 in 2015.[^pin-152804]

### High-level understanding

* [EE Times, *Cypress Introduces its First 0.35-µm SRAM*](<https://www.eetimes.com/cypress-introduces-its-first-0-35-m-sram/>) — the 0.5 µm, 0.35 µm and 0.25 µm dates.[^eet-1997-sram035]
* [FundingUniverse, *History of Cypress Semiconductor Corporation*](<https://www.fundinguniverse.com/company-histories/cypress-semiconductor-corporation-history/>) — the first product in 1984.[^fu-cypress]

### Deep dive

* [Cypress, *CMOS Data Book*, 1988](<https://deramp.com/downloads/mfe_archive/050-Component%20Specifications/Cypress%20Semiconductor/1988_Cypress_CMOS_Data_Book.pdf>) — the first 1.2 µm process and the 0.8 µm one.[^databook-1988]
* [Jin et al. (Cypress), *Electrochemical and Solid-State Letters*, 1999](<https://iopscience.iop.org/article/10.1149/1.1390832>) — LOCOS isolation in the 0.25 µm SRAM process.[^jin-1999]
* [Cypress, 1995 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1995.pdf>) — RAM3 defined.[^ar-fy1995]
* [Cypress, 1996 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1996.pdf>) — RAM3's release and shrink to 0.35 µm.[^ar-fy1996]
* [Cypress, 1998 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1998.pdf>) — RAM5 and the 0.25 µm BiCMOS process.[^ar-fy1998]
* [Cypress, QTP 96091](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-96091-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148ab080847>) — R28 at Fab 3.[^qtp-096091]
* [Cypress, QTP 011503](<https://web.archive.org/web/20201205124212/https://www.cypress.com/file/91641/download>) — L28 at Fab 2.[^qtp-011503]
* [Cypress, QTP 97132](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97132-32k-x-8-low-power-sram-r32-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714947ff09f5>) — R32.[^qtp-097132]
* [Cypress, QTP 003907](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-003907-high-frequency-programmable-pecl-clock-generator-r42ldha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714957940a14>) — R42D.[^qtp-003907]
* [Cypress, QTP 102101](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-102101-synchronous-asynchronous-dual-port-sram-3.3v-and-5v-r42hd-technology-fab-4-qualification-productqualificationreport-en.pdf>) — R42HD.[^qtp-102101]
* [Cypress, QTP 012705](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-012705-1meg-sram-fast-asynchronous-family-r52ffd-3-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148db7c0893>) — R52FFD-3.[^qtp-012705]
* [Cypress, QTP 011908](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-011908-fast-asynchronous-sram-technology-derivative-r7fd-fab-4-qualification-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7150e6271aff>) — R7FD-3R.[^qtp-011908]
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
[^qtp-080608]: Cypress Semiconductor, Product Qualification Report QTP 080608: *High Accuracy EPROM Programmable Device Family, L28 Technology, TSMC-2A*, May 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-080608-high-accuracy-eprom-programmable-device-family-l28-technology-tsmc-2a-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714a27090cd2>
[^qtp-097132]: Cypress Semiconductor, Product Qualification Report QTP 97132: *32K x 8 Low Power SRAM, R32 Technology, Fab4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97132-32k-x-8-low-power-sram-r32-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714947ff09f5>
[^qtp-098021]: Cypress Semiconductor, Product Qualification Report QTP 98021: *1 Meg SRAM (5% Shrink), R32D Technology, Fab 4 -- Military Devices*, July 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507141403/https://www.cypress.com/file/93501/download>
[^qtp-097483]: Cypress Semiconductor, Product Qualification Report QTP 97483: *Low Voltage Deep Synchronous FIFO High Speed 100-MHZ Operation, R42D -- Fab 4*, May 2017.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97483-low-voltage-deep-sync-fifos-r42d-technology-fab4-device-cy7c42-v-productqualificationreport-en.pdf>
[^qtp-003907]: Cypress Semiconductor, Product Qualification Report QTP 003907: *High Frequency Programmable PECL Clock Generator R42LDHA Technology, Fab 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-003907-high-frequency-programmable-pecl-clock-generator-r42ldha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714957940a14>
[^qtp-102101]: Cypress Semiconductor, Product Qualification Report QTP 102101: *Synchronous/Asynchronous Dual Port SRAM (3.3V and 5V), R42HD Technology, Fab 4 Qualification*, July 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-102101-synchronous-asynchronous-dual-port-sram-3.3v-and-5v-r42hd-technology-fab-4-qualification-productqualificationreport-en.pdf>
[^qtp-030206]: Cypress Semiconductor, Product Qualification Report QTP 030206: *256K Static RAM Automotive Devices, RAM42HHA Technology, Fab 4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030206-256k-static-ram-automotive-devices-ram42hha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71491e3d0986>
[^qtp-091302]: Cypress Semiconductor, Product Qualification Report QTP 091302: *MoBL Asynchronous SRAM Product Family, RAM42HNHA Technology, Fab5 GSMC*, February 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-091302-mobl-asynchronous-sram-product-family-cy62256-ram42hnha-technology-fab5-gsmc-productqualificationreport-en.pdf?fileId=8ac78c8c93dda25b01953e8470a271d4>
[^qtp-021507]: Cypress Semiconductor, Product Qualification Report QTP 021507: *Failsafe Device Family & Options S4AD-5 SONOS Technology, Fab 2*, December 2015.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>
[^qtp-062201]: Cypress Semiconductor, Product Qualification Report QTP 062201: *MoBL ADM Dual Port Static RAM Family, R52LD-3 Technology, Fab4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-062201-mobl-adm-dual-port-static-ram-family-r52ld-3-technology-fab4-productqualificationreport-en.pdf>
[^qtp-099202]: Cypress Semiconductor, Product Qualification Report QTP 99202: *Low Voltage Synchronous/Asynchronous RAM, R52D-3 Technology at Fab 4*, May 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-99202-low-voltage-synchronous-asynchronous-ram-r52d-3-technology-at-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71491c270982>
[^qtp-012705]: Cypress Semiconductor, Product Qualification Report QTP 012705: *1MEG SRAM Fast Asynchronous Family, R52FFD-3 Technology, Fab 4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-012705-1meg-sram-fast-asynchronous-family-r52ffd-3-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148db7c0893>
[^qtp-082506]: Cypress Semiconductor, Product Qualification Report QTP 082506: *PCI-E Clock Family, R52T-3 Technology, Fab 4*, September 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-082506-pci-e-clock-family-r52t-3-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714a4cbb0d39>
[^qtp-032005]: Cypress Semiconductor, Product Qualification Report QTP 032005: *WirelessUSB Device Family, B53D-3RF Technology, Fab 4*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211206184334/https://www.cypress.com/file/92296/download>
[^qtp-012801]: Cypress Semiconductor, Product Qualification Report QTP 012801: *4 Meg SRAM Device R7LD-1.8 Technology, Fab4*, October 2004;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210302225236/https://www.cypress.com/file/91706/download>
[^qtp-014807]: Cypress Semiconductor, Product Qualification Report QTP 014807: *Technology Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM CY7C085xV / CY7C083xV*, June 2005.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
[^qtp-011908]: Cypress Semiconductor, Product Qualification Report QTP 011908: *Fast Asynchronous SRAM Technology Derivative R7FD, Fab 4 Qualification*, August 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-011908-fast-asynchronous-sram-technology-derivative-r7fd-fab-4-qualification-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7150e6271aff>
[^qtp-113005]: Cypress Semiconductor, Product Qualification Report QTP 113005: *64K Serial Non-Volatile SRAM Product Family, S8 Technology, CMI (Fab 4)*, January 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^qtp-051101]: Cypress Semiconductor, Product Qualification Report QTP 051101: *FastEdge Series, B55SGT Technology, Fab 4*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201028052046/https://www.cypress.com/file/92676/download>
[^qtp-024110]: Cypress Semiconductor, Product Qualification Report QTP 024110: *1 MEG (3.0V) MOBL DEVICES RAM8NLD-1.8V TECHNOLOGY, FAB4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-024110-1-meg-3.0v-mobl-devices-ram8nld-1.8v-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152a1d61fde>
[^qtp-043004]: Cypress Semiconductor, Product Qualification Report QTP 043004: *DDR2-PLL Device Family, C8Q-3R, Fab 4*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205122906/https://www.cypress.com/file/92151/download>
[^qtp-053301]: Cypress Semiconductor, Product Qualification Report QTP 053301: *L8C-3R Technology, Fab 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-053301-l8c-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149c4a70b8f>
[^qtp-032003]: Cypress Semiconductor, Product Qualification Report QTP 032003: *36 Meg Synchronous SRAM Family, Technology R9T-3R, Fab4*, August 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-032003-36-meg-synchronous-sram-family-technology-r9t-3r-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714983cb0ac5>
[^qtp-051207]: Cypress Semiconductor, Product Qualification Report QTP 051207: *18 MEG QDR SYNCHRONOUS SRAM FAMILY, R9Q-3R TECHNOLOGY, FAB4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-051207-18-meg-qdr-synchronous-sram--cy7c1313d-product-family--r9q-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148e37b08a2>
[^qtp-063807]: Cypress Semiconductor, Product Qualification Report QTP 063807: *1 Meg Fast Asynchronous SRAM Family, C9FD-3R Technology, Fab4*, January 2024.
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
[^qtp-030204]: Cypress Semiconductor, Product Qualification Report QTP 030204: *256K Static RAM Automotive Devices, RAM42HA Technology, Fab 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030204-256k-static-ram-automotive-devices-ram42ha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714980870ac1>
[^qtp-098462]: Cypress Semiconductor, Product Qualification Report QTP 98462: *Fast Asynchronous SRAM Family, R5D-5R Technology, Skywater*, March 2019.
    <https://www.infineon.cn/assets/row/public/documents/10/316/infineon-qtp-98462-fast-asynchronous-sram-family--cy7c106b-cy7c1006b-cy7c194b-cy7c195b-cy7c199c--r52d-5r-technology-skywater-productqualificationreport-en.pdf>
[^ar-fy2003]: Cypress Semiconductor Corp., *2003 Annual Report* with Form 10-K, fiscal year ended
    2003-12-28: Item 1, Research and development.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2003.pdf>
[^tenq-1996q3]: Cypress Semiconductor Corp., Form 10-Q for the quarter ended 1996-09-30, filed
    1996-11-14, Notes to financial statements (restructuring); Wayback Machine copy of the EDGAR
    filing.
    <https://web.archive.org/web/20170530145033/https://www.sec.gov/Archives/edgar/data/791915/0000791915-96-000013.txt>
[^databook-1988]: Cypress Semiconductor, *CMOS Data Book*, 1988, pages 1-1 and 1-2 (scanned copy in
    deramp.com's archive of component documentation).
    <https://deramp.com/downloads/mfe_archive/050-Component%20Specifications/Cypress%20Semiconductor/1988_Cypress_CMOS_Data_Book.pdf>
[^jin-1999]: B. Jin, S. Sadoughi, K. Ramkumar, P. Goplan, S. Wong and S. Sharifzadeh (Cypress
    Semiconductor), *The Modulation of Crystal Originated Pits by the LOCOS Process in 0.25 µm SRAM
    Technology*, Electrochemical and Solid-State Letters 2 (7), 347, 1999, DOI 10.1149/1.1390832.
    <https://iopscience.iop.org/article/10.1149/1.1390832>
[^qtp-000901]: Cypress Semiconductor, Product Qualification Report QTP 000901: *Three-PLL Programmable Clock Generator, Fab 2 – L28 Technology*, May 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025142441/https://www.cypress.com/file/91341/download>
[^qtp-031101]: Cypress Semiconductor, Product Qualification Report QTP 031101: *High-Accuracy EPROM Programmable Device Family, L28 Technology, Fab 2*, January 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210128152257/https://www.cypress.com/file/92261/download>
[^qtp-091216]: Cypress Semiconductor, Product Qualification Report QTP 91216: *MAX EPLD, P20 Technology, Fab 2*, March 2000;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20200810011720/https://www.cypress.com/file/93411/download>
[^qtp-093332]: Cypress Semiconductor, Product Qualification Report QTP 93332: *MAX EPLD, P20 Technology, Fab 2*, March 2000;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201025104819/https://www.cypress.com/file/93456/download>
