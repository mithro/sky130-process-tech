(history-sonos-s4)=
# S4AD-5: Cypress's SONOS process before S8

S8 is a 0.13 µm process with SONOS non-volatile memory. Its predecessor, and Cypress's first SONOS
process in production, was a 0.35 µm process that the qualification reports call S4AD-5 and the
press calls S4. It made the first PSoC microcontrollers and a line of clock chips. This page
collects what the public sources say about it.

## At a glance

| Question | Answer | Sources |
|---|---|---|
| Name | S4AD-5 in the reports, S4 in the press; variants S4AD-5CTI and "S4ADLatch" | Cypress's reports, EE Times |
| Built on | "R42D-5 derivative w/ 6 additional mask" | single source |
| Design rule | 0.35 µm in four reports, 0.5 µm in one; 0.4 µm in one article | conflict |
| First qualified | "New Technology S4AD-5", April 2001, at Fab 2 | Cypress's reports |
| Fabs | Fab 2 (Round Rock), Fab 4 (Bloomington), Grace (GSMC, later HHGrace) in Shanghai | Cypress's reports, EE Times |
| Stack | single poly, two metal layers, 110 Å gate oxide | Cypress's reports |
| Products | PSoC 1 mixed-signal arrays, clock generators and buffers | Cypress's reports, Infineon |

The rows are explained, with their sources, below.

## A derivative of the 0.35 µm SRAM process

The earliest S4AD-5 report describes the process as "Fab2, S4AD-5 (SONOS), R42D-5 derivative w/ 6
additional mask" (single source).[^qtp-021507] R42D is the 0.35 µm SRAM and logic process of 1997
(see {ref}`history-technologies`). The metal layers support this: the Fab 2 S4AD-5 stack and the
Fab 4 R42D stack use the same films in the same thicknesses, 6000 Å and 8000 Å of aluminium–copper
between titanium or TiW layers (Cypress's reports).[^qtp-021507][^qtp-003907]

How many masks SONOS added is given three ways:

* **Six** in the S4AD-5 report.[^qtp-021507]
* **Three to five** "as compared to about ten in the case of floating gate flash", in a 2008 article
  by Cypress.[^chipest-2008]
* **Five** "beyond the standard CMOS process", in a later Cypress product brief.[^eflash-brief]

The three sources describe different generations and do not necessarily conflict.

## Dates and fabs

**First qualification.** The S4AD-5 reports date "New Technology S4AD-5" to April 2001, with a
programmable clock generator, the CY2414ZC, at Fab 2 (Cypress's reports).[^qtp-021507][^qtp-042806]
Cypress's product brief says its SONOS embedded flash "has been in production since 2001".[^eflash-brief]

**Earlier SONOS?** An Infineon history of PSoC says Cypress had CPLDs "based on its SONOS
process technology" in the late 1980s.[^psoc-history] No other source found supports this, and it
conflicts with the 2001 dates above. Cypress's 1993 10-K lists "0.65-micron Flash technologies", but
does not say they were SONOS.[^ar-fy1993]

**Fab 2.** Cypress's 2002 report says "our SONOS process in Fab 2" was ramping, and that it "reduced
our Fab 2 line width from 0.5-micron to 0.35-micron".[^ar-fy2002] From 2002 to 2006 the 10-Ks list
"0.35-micron Silicon Nitride Oxide Silicon (SONOS)" among Cypress's processes (Cypress's
reports).[^ar-fy2003][^ar-fy2006]

**Fab 4.** The PSoC "Neutron" family, the CY8C21x34 parts, was made on S4AD-5 at Fab 4 before part of
it moved to Grace (Cypress's reports).[^qtp-062509]

**Grace.** The December 2005 foundry deal was to start with "the PSoC mixed-signal array on
Cypress's proprietary S4 technology".[^eet-2005-grace] The Grace qualification with a PSoC family is
dated August 2006, and Cypress completed the transfer of its "0.35-micron SONOS process" to Grace
during 2006.[^qtp-062509][^qtp-151005][^ar-fy2006] Later reissues name the foundry HHGrace.[^qtp-151005]

## The design rule

The sources give three different design rules for the same process:

| Design rule | Where | Source |
|---|---|---|
| 0.5 µm | Fab 2, a report of January 2003 | one report[^qtp-021507] |
| 0.35 µm | Fab 2 (2005, 2007), Grace (2006), HHGrace (2015) | four reports[^qtp-042806][^qtp-051005][^qtp-062509][^qtp-151005] |
| 0.4 µm | Grace, 2007 | EE Times: "a 0.4-micron process for its mixed-signal programmable system-on-chip (PSoC)"[^eet-2007-fablite] |

Cypress's own 2002 sentence, that the SONOS process "reduced our Fab 2 line width from 0.5-micron to
0.35-micron", suggests the process started at 0.5 µm and was shrunk.[^ar-fy2002] The 0.5 µm report
is dated after that shrink, though, so the sources are not reconciled.

## Stackup

The two sites used different metal stacks for the same process name (Cypress's reports):[^qtp-021507][^qtp-051005][^qtp-062509][^qtp-151005]

| | Cypress Fab 2 | Grace (GSMC, HHGrace) |
|---|---|---|
| Metal 1 | 500 Å Ti / 6000 Å Al 0.5 % Cu / 1200 Å TiW | 250 Å TiN / 5800 Å Al / 700 Å TiN |
| Metal 2 | 500 Å Ti / 8000 Å Al 0.5 % Cu / 300 Å TiW | 500 Å TiN / 8000 Å Al / 250 Å TiN |
| Passivation | 3000 Å TEOS / 6000 Å Si3N4 | 7000 Å TEOS / 6000 Å Si3N4 |
| Gate oxide | 110 Å SiO2 | 110 Å SiO2 |

The same split between a TiW-capped stack and a TiN-capped stack appears in the Cypress reports on
S8; the SKY130 overview discusses it in {ref}`overview-metal-cap`. One Fab 2 report prints the gate
oxide as "7A", which reads as a truncated "110A".[^qtp-042806] The full tables are on
{ref}`history-stackups`.

## Products

The S4AD-5 reports name these products (Cypress's reports):[^qtp-021507][^qtp-042806][^qtp-051005][^qtp-062509][^qtp-151005]

* **PSoC 1 mixed-signal arrays.** The CY8C21x34 "Neutron" family, the CY8C24x94 family, and the
  CY8C9520 port expander; automotive versions on the S4AD-5CTI variant at Fab 2.
* **Clocks.** The CY2414ZC programmable clock generator, the CY2308A and CY2309A zero-delay
  buffers, the CY23FP12, the Failsafe CY26049 and CY23FS04/CY23FS08, and the CY5048WAF WLAN clock
  generator on the "S4ADLatch" variant.

Infineon's history of PSoC says "PSoC™ 1, used the SONOS process technology", which agrees with the
reports.[^psoc-history]

## The patents

Cypress patented its SONOS dielectrics in the early 2000s. These families are shown as expired:

* **The ONO dielectric.** A method for the SONOS dielectric layer, with a 2001 priority date.[^pat-us6818558]
* **A deuterated interface.** A SONOS structure with a deuterated oxide–silicon interface, filed in
  2002.[^pat-us6677213]
* **The ONO stack.** A method for the ONO dielectric of SONOS-type devices, filed in 2002.[^pat-us6969689]

:::{dropdown} A SONOS cell patent of status shown as unknown (US 6,172,907; estimated expiry no later than 2020-10-22) — open to read
Cypress's SONOS memory-cell patent, filed on 1999-10-22, is the earliest Cypress SONOS cell patent
found. Its legal status is not recorded in the public sources consulted.[^pat-us6172907]
:::

## What carried over into S8

S4AD-5 and S8 share the SONOS approach, the 110 Å gate oxide and part of the metal recipe. The
details, and what changed, are on {ref}`history-s8-lineage`.

## Open questions

* **The design rule.** Was S4AD-5 a 0.5 µm process shrunk to 0.35 µm, and where does the 0.4 µm of
  2007 fit?
* **SONOS before 2001.** Did any Cypress product before 2001 use SONOS?
* **The six masks.** Which six masks did S4AD-5 add to R42D-5?

## References

### Cross-check

* [Cypress, QTP 021507](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>) — S4AD-5 as an R42D-5 derivative.[^qtp-021507]
* [Cypress, 2002 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2002.pdf>) — the SONOS process in Fab 2.[^ar-fy2002]

### High-level understanding

* [Infineon, *20 years of PSoC*](<http://web.archive.org/web/20250713043850/https://www.infineon.com/cms/en/product/promopages/20-years-of-psoc/how-it-started/>) — PSoC 1 on SONOS.[^psoc-history]
* [Cypress, *Cypress SONOS - A Scalable Embedded Flash Technology*](<https://www.chipestimate.com/Cypress-SONOS-A-Scalable-Embedded-Flash-Technology/Cypress-Semiconductor/Technical-Article/2008/10/21>) — how SONOS fits into a CMOS flow.[^chipest-2008]

### Deep dive

* [Cypress, SONOS eFlash product brief](<https://www.infineon.com/assets/row/public/documents/10/45/infineon-sonos-eflash-product-overview-productbrief-en.pdf?fileId=8ac78c8c7d710014017d715307cf2069>) — the cell and its extra masks.[^eflash-brief]
* [Cypress, QTP 042806](<https://web.archive.org/web/20211025144943/https://www.cypress.com/file/92521/download>) — "S4ADLatch" at Fab 2.[^qtp-042806]
* [Cypress, QTP 051005](<https://web.archive.org/web/20211130190834/https://www.cypress.com/file/92671/download>) — S4AD-5CTI, automotive PSoC.[^qtp-051005]
* [Cypress, QTP 062509](<https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-062509-psoc21x34-95xx-gsmc-productqualificationreport-en.pdf>) — the Neutron family moved to GSMC.[^qtp-062509]
* [Cypress, QTP 151005](<https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-151005-psoc24x94-hhgrace-productqualificationreport-en.pdf>) — S4AD-5 at HHGrace.[^qtp-151005]
* [Cypress, QTP 003907](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-003907-high-frequency-programmable-pecl-clock-generator-r42ldha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714957940a14>) — the R42D stack for comparison.[^qtp-003907]
* [EE Times, *Cypress inks foundry deal with Grace*](<https://www.eetimes.com/cypress-inks-foundry-deal-with-grace/>) — the S4 process at Grace.[^eet-2005-grace]
* [EE Times, *Cypress furthers 'fab lite'*](<https://www.eetimes.com/cypress-furthers-fab-lite/>) — the 0.4 µm PSoC process at Grace.[^eet-2007-fablite]
* [Cypress, 2006 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2006.pdf>) — the 0.35 µm SONOS process moved to Grace.[^ar-fy2006]
* [Rathor et al., US 6,818,558](<https://patents.google.com/patent/US6818558B1/en>) — the SONOS dielectric.[^pat-us6818558]
* [Ramkumar and Jenne, US 6,677,213](<https://patents.google.com/patent/US6677213B1/en>) — a deuterated SONOS interface.[^pat-us6677213]
* [Ramkumar et al., US 6,969,689](<https://patents.google.com/patent/US6969689B1/en>) — the ONO dielectric.[^pat-us6969689]

<!-- footnotes -->

[^ar-fy1993]: Cypress Semiconductor Corp., Form 10-K for the fiscal year ended 1994-01-03, filed
    1994-03-16, Item 1, Manufacturing and Research and development.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1994.pdf>
[^ar-fy2002]: Cypress Semiconductor Corp., *2002 Annual Report* with Form 10-K, fiscal year ended
    2002-12-29: Item 1, Research and development and Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2002.pdf>
[^ar-fy2003]: Cypress Semiconductor Corp., *2003 Annual Report* with Form 10-K, fiscal year ended
    2003-12-28: Item 1, Research and development.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2003.pdf>
[^ar-fy2006]: Cypress Semiconductor Corp., *2006 Annual Report* with Form 10-K, fiscal year ended
    2006-12-31: Item 1, Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2006.pdf>
[^eet-2005-grace]: Mark LaPedus, *Cypress inks foundry deal with Grace*, EE Times, 2005-12-12.
    <https://www.eetimes.com/cypress-inks-foundry-deal-with-grace/>
[^eet-2007-fablite]: EE Times, *Cypress furthers 'fab lite'*, 2007-03-05.
    <https://www.eetimes.com/cypress-furthers-fab-lite/>
[^psoc-history]: Infineon Technologies, *20 years of PSoC: How it started*, Wayback Machine copy of
    2025-07-13 (the live page now redirects elsewhere).
    <http://web.archive.org/web/20250713043850/https://www.infineon.com/cms/en/product/promopages/20-years-of-psoc/how-it-started/>
[^chipest-2008]: Cypress Semiconductor, *Cypress SONOS - A Scalable Embedded Flash Technology*,
    ChipEstimate.com Tech Talks, 2008-10-21.
    <https://www.chipestimate.com/Cypress-SONOS-A-Scalable-Embedded-Flash-Technology/Cypress-Semiconductor/Technical-Article/2008/10/21>
[^eflash-brief]: Cypress Semiconductor (an Infineon company), *SONOS eFlash* product overview,
    undated product brief.
    <https://www.infineon.com/assets/row/public/documents/10/45/infineon-sonos-eflash-product-overview-productbrief-en.pdf?fileId=8ac78c8c7d710014017d715307cf2069>
[^pat-us6818558]: M. Rathor, K. Ramkumar, F. Jenne and L. Lancaster (Cypress Semiconductor), *Method of
    manufacturing a dielectric layer for a silicon-oxide-nitride-oxide-silicon (SONOS) type
    devices*, US 6,818,558 B1, priority 2001-07-31. <https://patents.google.com/patent/US6818558B1/en>
[^pat-us6677213]: K. Ramkumar and F. B. Jenne (Cypress Semiconductor), *SONOS structure including a
    deuterated oxide-silicon interface and method for making the same*, US 6,677,213 B1, priority
    2002-03-08. <https://patents.google.com/patent/US6677213B1/en>
[^pat-us6969689]: K. Ramkumar, M. Rathor, B. Parameshwaran and L. Lancaster (Cypress Semiconductor), *Method of
    manufacturing an oxide-nitride-oxide (ONO) dielectric for SONOS-type devices*, US 6,969,689 B1,
    priority 2002-06-28. <https://patents.google.com/patent/US6969689B1/en>
[^pat-us6172907]: F. Jenne (Cypress Semiconductor), *Silicon-oxide-nitride-oxide-semiconductor
    (SONOS) type memory cell and method for retaining data in the same*, US 6,172,907 B1, priority
    1999-10-22. Status shown as unknown; estimated expiry no later than 2020-10-22 (estimate from
    public records, not legal advice). <https://patents.google.com/patent/US6172907B1/en>
[^qtp-021507]: Cypress Semiconductor, Product Qualification Report QTP 021507: *Failsafe Device Family & Options S4AD-5 SONOS Technology, Fab 2*, December 2015.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>
[^qtp-003907]: Cypress Semiconductor, Product Qualification Report QTP 003907: *High Frequency Programmable PECL Clock Generator R42LDHA Technology, Fab 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-003907-high-frequency-programmable-pecl-clock-generator-r42ldha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714957940a14>
[^qtp-042806]: Cypress Semiconductor, Product Qualification Report QTP 042806: *S4ADLATCH Technology, Fab 2*, January 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025144943/https://www.cypress.com/file/92521/download>
[^qtp-051005]: Cypress Semiconductor, Product Qualification Report QTP 051005: *Automotive PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211130190834/https://www.cypress.com/file/92671/download>
[^qtp-062509]: Cypress Semiconductor, Product Qualification Report QTP 062509: *Neutron Device Family, S4AD-5 Technology, GSMC*, July 2014.
    <https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-062509-psoc21x34-95xx-gsmc-productqualificationreport-en.pdf>
[^qtp-151005]: Cypress Semiconductor, Product Qualification Report QTP 151005: *PSoC RADON Device Family, S4AD-5 Technology, HHGrace FAB5*, October 2015.
    <https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-151005-psoc24x94-hhgrace-productqualificationreport-en.pdf>
