(history-naming)=
# How Cypress named its processes

Cypress's reports name each process with a short code such as R42D, S4AD-5, C8Q-3R or S8TNV-5R. No
public Cypress document found explains the scheme. This page sets out what the sources show, and keeps
what they say apart from what we infer.

## The pattern

A code is a family letter, a generation number and suffixes: **R** + **5** + **2FFD-3** for a fast
0.25 µm SRAM process, **S** + **4** + **AD-5** for the 0.35 µm SONOS process. The table lists the
generations with the design rules the reports print:

| Generation digit | Codes in the reports | Design rule printed | Cypress's product name |
|---|---|---|---|
| 2 | R28, L28, L28EPD, P26 | 0.65 µm | — |
| 3 | R32, R32D | 0.5 µm | RAM3 |
| 4 | R42D, R42HD, RAM42, S4AD-5 | 0.42 µm and 0.35 µm | RAM4 |
| 5 | R52D-3, R52LD-3, R52FFD-3, R52T-3, R52D-5R, B53D-3, B55SGT | 0.25 µm (B55SGT: 0.21–0.35 µm) | RAM5 |
| 7 | R7LD-1.8, R7FD-3R, R7FT-3R | 0.16, 0.15 and 0.18 µm | RAM 7 |
| 8 | R8LD-1.8 (RAM8NLD-1.8), C8Q-3R, L8C-3R, S8TNV-5R | 0.13 µm | RAM 8 |
| 9 | R9T-3R, R9Q-3R, C9FD-3R, R95LD-3R | 90 nm | — |

The codes and design rules are from the qualification reports, which are all Cypress's.[^qtp-096091][^qtp-097132][^qtp-102101][^qtp-021507][^qtp-012705][^qtp-011908][^qtp-043004][^qtp-113005][^qtp-063807]
The product names are from Cypress's annual reports: RAM3 is "0.5-micron feature geometry", RAM5
"0.25-micron feature geometry", RAM4 is listed as a trademark, and RAM 8 took the line width "from
0.15-micron to 0.13-micron".[^ar-fy1995][^ar-fy1998][^ar-fy1997][^ar-fy2002] A 2015 Cypress notice
groups "130nm C8/R8/S8/L8" and "90nm C9/R9/R95".[^pin-152804]

That the digit of a code is the RAM generation number is our reading. The names match, but no source
says that R32 is RAM3 or that R42 is RAM4. No code with the digit 6 was found, and one source conflicts:
the 2015 notice says "250nm R7" while the R7 reports print 0.18–0.15 µm.[^pin-152804][^qtp-011908]

## The family letters

| Letter | Codes | What the sources show | Our reading |
|---|---|---|---|
| R | R28 to R95 | the reports also write "RAM42", "RAM7FT-3R" and "RAM8NLD-1.8" for these codes | RAM (SRAM) process |
| S | S4AD-5, S8 | "S4AD-5 (SONOS)"; S8 is "0.13-micron SONOS" | SONOS process |
| C | C8Q-3R, C9FD-3R | C8 made USB and clock chips; L8C-3R is a "Technology Derivative of the C8 Technology" | CMOS logic process |
| L | L28, L8C-3R | clock, PLL and logic products | a logic process |
| B | B53D-3, B55SGT | B55SGT is printed "SiGe Bipolar" | BiCMOS process |
| P | P26 | PROM and EPROM products | PROM process |

The evidence for each row is in Cypress's reports and the press.[^qtp-091302][^qtp-014807][^qtp-024110][^qtp-021507][^ew-2007-s8][^eet-2006-c8][^qtp-053301][^qtp-051101][^qtp-096411]
Only the R and S rows rest on the sources' own words. The C, L, B and P readings are inferences from
the products made on each process.

## The suffixes

The reports use the suffixes below. None is defined in any report; the right-hand column is our
reading from the products each suffix appears on.

| Suffix | Seen on | Our reading |
|---|---|---|
| D | R32D, R42D, R52D-3 | R32D has two metal layers where R32 has one; perhaps "double metal" |
| LD | R42LDHA, R52LD-3, R7LD-1.8, R8LD-1.8, R95LD-3R | low-power ("MoBL") SRAM products |
| FD, FFD | R52FD-3, R52FFD-3, R7FD-3R, C9FD-3R | fast asynchronous SRAM products |
| FT, T | R7FT-3R, R52T-3, R9T-3R | synchronous RAMs and clocks; no single meaning found |
| Q | C8Q-3R, R9Q-3R | R9Q-3R has one more metal layer than R9T-3R |
| -3, -3R, -5, -5R, -1.8 | most codes from R52 onwards | probably voltage or option codes; -1.8 appears on 1.8 V SRAMs |

Two relations between codes are stated outright. "Transfer of CY7C1021BV33 from Technology R52FD-3 to
R52FFD-3" shows R52FFD-3 replacing R52FD-3, and "New Technology Derivative" is written of R52FFD-3,
R52D-5R, R7FD-3R and R7FT-3R (Cypress's reports).[^qtp-012705][^qtp-098462][^qtp-011908][^qtp-014807]

## Spelling in the reports

The reports are not consistent with their own codes. One report spells the same process five ways
(B55SGT, B55SGT18A, 55SGT18A, B55SG and B55STG). Others drop a letter, as in "S4D-5" for S4AD-5 and
"R5D-5R" for R52D-5R. Some print a process-description heading taken from an unrelated report: an
L28 report carries the heading "R9T-3R" (Cypress's reports).[^qtp-051101][^qtp-051005][^qtp-098462][^qtp-110605]
Read a single code in a single report with care.

## Open questions

* **The scheme.** Is there a Cypress document that defines the codes?
* **The missing digits.** What were the 0.65 µm and 90 nm generations called, and was there a sixth?
* **The suffix numbers.** What do -3, -5, -3R and -5R mean? S8's variants carry -5R, -10R and -10P as
  well.

## References

### Cross-check

* [Cypress, 1995 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1995.pdf>) — RAM3 defined.[^ar-fy1995]
* [Cypress, 1998 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1998.pdf>) — RAM5 defined.[^ar-fy1998]
* [Cypress, PIN152804](<https://media.futureelectronics.com/PCN/45887_SPCN.PDF>) — the families of 2015.[^pin-152804]

### High-level understanding

* {ref}`history-technologies` — each generation in turn.
* {ref}`history-stackups` — the process descriptions behind the table.

### Deep dive

* [Cypress, 1997 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1997.pdf>) — RAM4 among the trademarks.[^ar-fy1997]
* [Cypress, 2002 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2002.pdf>) — RAM 7 and RAM 8.[^ar-fy2002]
* [Cypress, QTP 012705](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-012705-1meg-sram-fast-asynchronous-family-r52ffd-3-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148db7c0893>) — R52FD-3 to R52FFD-3.[^qtp-012705]
* [Cypress, QTP 098462](<https://www.infineon.cn/assets/row/public/documents/10/316/infineon-qtp-98462-fast-asynchronous-sram-family--cy7c106b-cy7c1006b-cy7c194b-cy7c195b-cy7c199c--r52d-5r-technology-skywater-productqualificationreport-en.pdf>) — R52D-5R, a "Technology Derivative".[^qtp-098462]
* [Cypress, QTP 014807](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>) — "RAM7FT-3R".[^qtp-014807]
* [Cypress, QTP 024110](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-024110-1-meg-3.0v-mobl-devices-ram8nld-1.8v-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152a1d61fde>) — "RAM8NLD-1.8".[^qtp-024110]
* [Cypress, QTP 091302](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-091302-mobl-asynchronous-sram-product-family-cy62256-ram42hnha-technology-fab5-gsmc-productqualificationreport-en.pdf?fileId=8ac78c8c93dda25b01953e8470a271d4>) — "RAM42".[^qtp-091302]
* [Cypress, QTP 053301](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-053301-l8c-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149c4a70b8f>) — L8C-3R from C8.[^qtp-053301]
* [Cypress, QTP 051101](<https://web.archive.org/web/20201028052046/https://www.cypress.com/file/92676/download>) — B55SGT and its spellings.[^qtp-051101]
* [Cypress, QTP 110605](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-110605-zero-delay-buffer-l28-technology-tsmc-2a-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714b37f41005>) — a borrowed heading.[^qtp-110605]
* [Cypress, QTP 096411](<https://web.archive.org/web/20201026124735/https://www.cypress.com/file/93566/download>) — P26.[^qtp-096411]
* [Electronics Weekly, *Cypress 4-Mbit non-volatile static random access memory*](<https://www.electronicsweekly.com/news/products/memory-products/cypress-4-mbit-non-volatile-static-random-access-memory-2007-10/>) — S8 as SONOS.[^ew-2007-s8]

<!-- footnotes -->

[^ar-fy1995]: Cypress Semiconductor Corp., *1995 Annual Report*, fiscal year ended 1996-01-01:
    shareholder letter, highlights timeline and notes on commitments and subsidiaries.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1995.pdf>
[^ar-fy1997]: Cypress Semiconductor Corp., *1997 Annual Report*, fiscal year ended 1997-12-28:
    manufacturing section and restructuring note.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1997.pdf>
[^ar-fy1998]: Cypress Semiconductor Corp., *1998 Annual Report*, fiscal year ended 1999-01-03:
    president's letter and restructuring discussion.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1998.pdf>
[^ar-fy2002]: Cypress Semiconductor Corp., *2002 Annual Report* with Form 10-K, fiscal year ended
    2002-12-29: Item 1, Research and development and Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2002.pdf>
[^pin-152804]: Cypress Semiconductor, Product Information Notification PIN152804, *Qualification of
    GlobalWafer Silicon Wafers for 250nm, 130nm and 90nm Technology Products at Cypress Fab 4*,
    2015-07-12 (copy hosted by Future Electronics).
    <https://media.futureelectronics.com/PCN/45887_SPCN.PDF>
[^ew-2007-s8]: Electronics Weekly, *Cypress 4-Mbit non-volatile static random access memory*,
    2007-10-18.
    <https://www.electronicsweekly.com/news/products/memory-products/cypress-4-mbit-non-volatile-static-random-access-memory-2007-10/>
[^eet-2006-c8]: Mark LaPedus, *Cypress transfers 130-nm process to Grace*, EE Times, 2006-07-19.
    <https://www.eetimes.com/cypress-transfers-130-nm-process-to-grace/>
[^qtp-096091]: Cypress Semiconductor, Product Qualification Report QTP 96091: *Dual Port SRAM - R28 Technology, 6% Shrink*, September 1996.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-96091-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148ab080847>
[^qtp-097132]: Cypress Semiconductor, Product Qualification Report QTP 97132: *32K x 8 Low Power SRAM, R32 Technology, Fab4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97132-32k-x-8-low-power-sram-r32-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714947ff09f5>
[^qtp-102101]: Cypress Semiconductor, Product Qualification Report QTP 102101: *Synchronous/Asynchronous Dual Port SRAM (3.3V and 5V), R42HD Technology, Fab 4 Qualification*, July 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-102101-synchronous-asynchronous-dual-port-sram-3.3v-and-5v-r42hd-technology-fab-4-qualification-productqualificationreport-en.pdf>
[^qtp-021507]: Cypress Semiconductor, Product Qualification Report QTP 021507: *Failsafe Device Family & Options S4AD-5 SONOS Technology, Fab 2*, December 2015.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>
[^qtp-012705]: Cypress Semiconductor, Product Qualification Report QTP 012705: *1MEG SRAM Fast Asynchronous Family, R52FFD-3 Technology, Fab 4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-012705-1meg-sram-fast-asynchronous-family-r52ffd-3-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148db7c0893>
[^qtp-011908]: Cypress Semiconductor, Product Qualification Report QTP 011908: *Fast Asynchronous SRAM Technology Derivative R7FD, Fab 4 Qualification*, August 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-011908-fast-asynchronous-sram-technology-derivative-r7fd-fab-4-qualification-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7150e6271aff>
[^qtp-043004]: Cypress Semiconductor, Product Qualification Report QTP 043004: *DDR2-PLL Device Family, C8Q-3R, Fab 4*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205122906/https://www.cypress.com/file/92151/download>
[^qtp-113005]: Cypress Semiconductor, Product Qualification Report QTP 113005: *64K Serial Non-Volatile SRAM Product Family, S8 Technology, CMI (Fab 4)*, January 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^qtp-063807]: Cypress Semiconductor, Product Qualification Report QTP 063807: *1 Meg Fast Asynchronous SRAM Family, C9FD-3R Technology, Fab4*, Jan 2024.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-063807-1-meg-fast-asynchronous-sram-family-c9fd-3r-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149f5380c45>
[^qtp-091302]: Cypress Semiconductor, Product Qualification Report QTP 091302: *MoBL Asynchronous SRAM Product Family, RAM42HNHA Technology, Fab5 GSMC*, February 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-091302-mobl-asynchronous-sram-product-family-cy62256-ram42hnha-technology-fab5-gsmc-productqualificationreport-en.pdf?fileId=8ac78c8c93dda25b01953e8470a271d4>
[^qtp-014807]: Cypress Semiconductor, Product Qualification Report QTP 014807: *Technology Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM CY7C085xV / CY7C083xV*, June 2005.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
[^qtp-024110]: Cypress Semiconductor, Product Qualification Report QTP 024110: *1 MEG (3.0V) MOBL DEVICES RAM8NLD-1.8V TECHNOLOGY, FAB4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-024110-1-meg-3.0v-mobl-devices-ram8nld-1.8v-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152a1d61fde>
[^qtp-053301]: Cypress Semiconductor, Product Qualification Report QTP 053301: *L8C-3R Technology, Fab 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-053301-l8c-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149c4a70b8f>
[^qtp-051101]: Cypress Semiconductor, Product Qualification Report QTP 051101: *FastEdge Series, B55SGT Technology, Fab 4*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201028052046/https://www.cypress.com/file/92676/download>
[^qtp-096411]: Cypress Semiconductor, Product Qualification Report QTP 96411: *256K/512K PROM - P26 Technology*, May 1997;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201026124735/https://www.cypress.com/file/93566/download>
[^qtp-098462]: Cypress Semiconductor, Product Qualification Report QTP 98462: *Fast Asynchronous SRAM Family, R5D-5R Technology, Skywater*, March 2019.
    <https://www.infineon.cn/assets/row/public/documents/10/316/infineon-qtp-98462-fast-asynchronous-sram-family--cy7c106b-cy7c1006b-cy7c194b-cy7c195b-cy7c199c--r52d-5r-technology-skywater-productqualificationreport-en.pdf>
[^qtp-051005]: Cypress Semiconductor, Product Qualification Report QTP 051005: *Automotive PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211130190834/https://www.cypress.com/file/92671/download>
[^qtp-110605]: Cypress Semiconductor, Product Qualification Report QTP 110605: *Zero Delay Buffer, L28 Technology, TSMC-2A*, March 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-110605-zero-delay-buffer-l28-technology-tsmc-2a-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714b37f41005>
