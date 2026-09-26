(history-index)=
# Before S8: Cypress's process technologies

SKY130 began as S8, a Cypress Semiconductor process. This section traces the Cypress processes that came
before S8: where they were developed and run, what was made on them, what their stackups were, and how
they relate to S8. It is a history kept apart from the SKY130 reference, which starts at
{ref}`overview-index`, and it uses its own source list, {ref}`history-sources`.

## The short version

* **Cypress made its own processes, one generation at a time.** From 1.2 µm CMOS in 1984 to 90 nm in 2004,
  with SRAM processes named RAM3 at 0.5 µm, RAM5 at 0.25 µm and RAM 8 at 0.13 µm. See
  {ref}`history-technologies`.[^fu-cypress][^ar-fy1995][^ar-fy1998][^ar-fy2002][^ar-fy2004]
* **Four fabs of its own.** San Jose (Fab 1), Round Rock, Texas (Fab 2) and two fabs on one site in
  Bloomington, Minnesota (Fab 3 and Fab 4). Fab 4, built from 1994, is the fab SkyWater runs today. See
  {ref}`history-fabs`.[^ar-fy1993][^ar-fy1995][^strib-2017]
* **SONOS in the reports from 2001.** S4AD-5, a 0.35 µm process built on the R42D SRAM process with six
  more masks, was qualified at Round Rock in 2001 with clock chips. It made automotive PSoC parts there by
  2004, and PSoC at Grace in Shanghai from 2006 (Cypress's reports).[^qtp-021507][^qtp-051005][^qtp-062509]
  An Infineon history claims SONOS in the 1980s (single source). See
  {ref}`history-sonos-s4`.[^psoc-history]
* **S8, in our reading, joined the two lines.** S8 is a 0.13 µm SONOS process of the same generation as
  Cypress's C8, R8 and L8, and its thick gate oxide is 110 Å, like S4AD-5's (our reading). See
  {ref}`history-s8-lineage`.[^pin-152804][^qtp-113005][^qtp-021507]

:::{figure} /_static/figures/history-lineage.svg
:alt: Four boxes one above the other joined by downward arrows: R42D in 1997, S4AD-5 in 2001, S8 in 2007 to 2008, and SKY130. A side box, C8 in 2005, points into the S8 box.
:width: 560px
:name: fig-history-lineage

The processes S8 shares most with. S4AD-5 was built on R42D, as its report says.[^qtp-021507] The arrows into S8, from S4AD-5 (SONOS and the 110 Å oxide) and from C8 (the same first metal and generation), are our reading; no source says from which process S8 was derived.[^qtp-113005][^qtp-043004]
:::

## Timeline

| Year | Event |
|---|---|
| 1984 | First product, a CMOS memory with 1.2 µm transistors[^fu-cypress][^databook-1988] |
| 1986 | Fab 2 opens in Round Rock, Texas[^ar-fy2008][^sd-2007-fab2] |
| 1991 | Fab 3 in Bloomington, bought from Control Data, begins operation[^ar-fy1993][^strib-2017] |
| 1995 | Fab 4, eight-inch, opens beside Fab 3[^ar-fy1995][^sd-2007-fab2] |
| 1995 | RAM3, the 0.5 µm SRAM process, is released (Cypress's reports)[^ar-fy1995][^ar-fy1996] |
| 1996 | Fab 1 in San Jose becomes an R&D fab[^tenq-1996q3][^fu-cypress] |
| 1997 | R42D and R42HD qualified at Fab 4 (Cypress's reports)[^qtp-097483][^qtp-102101] |
| 1998 | Fab 3 closes[^ar-fy1998][^eet-1998-restructure] |
| 1998 | First revenue on 0.25 µm (RAM5) (single source)[^ar-fy1998] |
| 2001 | S4AD-5, the first SONOS process in the reports, qualified at Fab 2 (Cypress's reports)[^qtp-021507][^qtp-042806] |
| 2002 | RAM 8 brings 0.13 µm to Fab 4 (single source)[^ar-fy2002] |
| 2005 | C8 logic process qualified (single source)[^qtp-043004] |
| 2005 | Foundry deal with Grace[^ar-fy2005][^eet-2005-grace] |
| 2006 | 0.35 µm SONOS moves to Grace (Cypress's reports)[^ar-fy2006][^tenk-fy2007] |
| 2007 | First S8 products announced (single source)[^ew-2007-s8] |
| 2007 | Fab 1 sold[^ar-fy2009][^eet-2007-fablite] |
| 2008 | First S8 qualification at Fab 4 (single source)[^qtp-113005] |
| 2008 | Fab 2 closes[^ar-fy2008][^sd-2007-fab2] |

Each row cites its sources; rows marked "single source" or "Cypress's reports" rest on one source or on
Cypress alone. The pages give the details and the points where sources disagree.

## How to read this section

* **Several sources per claim.** Each claim is backed by two or more independent sources where they
  exist. A claim resting on Cypress's own documents alone says so ("Cypress's reports"), and a claim
  with one source is marked "(single source)".
* **Conflicts are shown.** Where sources disagree, the page gives each version and its source.
* **Readings are labelled.** Our inferences are marked "our reading" or "our arithmetic".
* **Qualification reports.** Much of the detail comes from Cypress's product qualification reports,
  now published by Infineon. They were reissued over the years, and the reissues sometimes rename
  sites and drop or misprint codes; see {ref}`history-fabs` and {ref}`history-naming`.
* **Gaps in the reports.** The reports give metals, passivation and gate oxides, but rarely isolation,
  poly, contacts or implants, and none covers the 1.2 µm and 0.8 µm processes in detail. Some reports can
  be read only after logging in to Infineon's site and are not used.
* **Gaps in the filings.** Cypress's annual reports before fiscal 1993 were not found online, and the
  fiscal 2000 report is a scan whose text could not be read.

```{toctree}
:maxdepth: 1
:hidden:

fabs
technologies
sonos-s4
s8-lineage
grace
naming
stackups
products
sources
```

## References

### Cross-check

* [Cypress, Form 10-K for fiscal 1993](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1994.pdf>) — Cypress's fabs and processes in 1993.[^ar-fy1993]
* [SkyWater PDK, *Previous Nomenclature*](<https://skywater-pdk.readthedocs.io/en/main/previous.html>) — S8 as the old name of SKY130.[^pdk-previous]

### Deep dive

* {ref}`history-stackups` — every process description in the reports.

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
[^ar-fy1998]: Cypress Semiconductor Corp., *1998 Annual Report*, fiscal year ended 1999-01-03:
    president's letter and restructuring discussion.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1998.pdf>
[^ar-fy2002]: Cypress Semiconductor Corp., *2002 Annual Report* with Form 10-K, fiscal year ended
    2002-12-29: Item 1, Research and development and Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2002.pdf>
[^ar-fy2005]: Cypress Semiconductor Corp., *2005 Annual Report* with Form 10-K, fiscal year ended
    2006-01-01: Item 1, Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2005.pdf>
[^ar-fy2006]: Cypress Semiconductor Corp., *2006 Annual Report* with Form 10-K, fiscal year ended
    2006-12-31: Item 1, Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2006.pdf>
[^ar-fy2008]: Cypress Semiconductor Corp., *2008 Annual Report* with Form 10-K, fiscal year ended
    2008-12-28: shareholder letter and Item 1, Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2008.pdf>
[^ar-fy2009]: Cypress Semiconductor Corp., *2009 Annual Report* with Form 10-K, fiscal year ended
    2010-01-03: shareholder letter.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2009.pdf>
[^tenq-1996q3]: Cypress Semiconductor Corp., Form 10-Q for the quarter ended 1996-09-30, filed
    1996-11-14, Notes to financial statements (restructuring); Wayback Machine copy of the EDGAR
    filing.
    <https://web.archive.org/web/20170530145033/https://www.sec.gov/Archives/edgar/data/791915/0000791915-96-000013.txt>
[^sd-2007-fab2]: Semiconductor Digest, *Cypress getting rid of Round Rock, TX fab*, 2007-12-19.
    <https://sst.semiconductor-digest.com/2007/12/cypress-getting-rid-of-round-rock-tx-fab/>
[^strib-2017]: Alex Van Abbema, *Twin Cities tech executives form new company, buy Cypress chip
    plant in Bloomington*, Star Tribune, 2017-03-31.
    <https://www.startribune.com/twin-cities-tech-executives-form-new-company-buy-cypress-chip-plant-in-bloomington/417672063>
[^ew-2007-s8]: Electronics Weekly, *Cypress 4-Mbit non-volatile static random access memory*,
    2007-10-18.
    <https://www.electronicsweekly.com/news/products/memory-products/cypress-4-mbit-non-volatile-static-random-access-memory-2007-10/>
[^pin-152804]: Cypress Semiconductor, Product Information Notification PIN152804, *Qualification of
    GlobalWafer Silicon Wafers for 250nm, 130nm and 90nm Technology Products at Cypress Fab 4*,
    2015-07-12 (copy hosted by Future Electronics).
    <https://media.futureelectronics.com/PCN/45887_SPCN.PDF>
[^pdk-previous]: SkyWater PDK Authors, *Previous Nomenclature*, SkyWater SKY130 PDK documentation,
    retrieved 2026-09-25. <https://skywater-pdk.readthedocs.io/en/main/previous.html>
[^qtp-021507]: Cypress Semiconductor, Product Qualification Report QTP 021507: *Failsafe Device Family & Options S4AD-5 SONOS Technology, Fab 2*, December 2015.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>
[^qtp-113005]: Cypress Semiconductor, Product Qualification Report QTP 113005: *64K Serial Non-Volatile SRAM Product Family, S8 Technology, CMI (Fab 4)*, January 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^qtp-097483]: Cypress Semiconductor, Product Qualification Report QTP 97483: *Low Voltage Deep Synchronous FIFO High Speed 100-MHZ Operation, R42D -- Fab 4*, May 2017.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97483-low-voltage-deep-sync-fifos-r42d-technology-fab4-device-cy7c42-v-productqualificationreport-en.pdf>
[^qtp-043004]: Cypress Semiconductor, Product Qualification Report QTP 043004: *DDR2-PLL Device Family, C8Q-3R, Fab 4*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205122906/https://www.cypress.com/file/92151/download>
[^databook-1988]: Cypress Semiconductor, *CMOS Data Book*, 1988, pages 1-1 and 1-2 (scanned copy in
    deramp.com's archive of component documentation).
    <https://deramp.com/downloads/mfe_archive/050-Component%20Specifications/Cypress%20Semiconductor/1988_Cypress_CMOS_Data_Book.pdf>
[^eet-1998-restructure]: EE Times staff, *Cypress Restructures Manufacturing Operations*, EE Times,
    1998-03-09. <https://www.eetimes.com/cypress-restructures-manufacturing-operations/>
[^eet-2005-grace]: Mark LaPedus, *Cypress inks foundry deal with Grace*, EE Times, 2005-12-12.
    <https://www.eetimes.com/cypress-inks-foundry-deal-with-grace/>
[^eet-2007-fablite]: EE Times, *Cypress furthers 'fab lite'*, 2007-03-05.
    <https://www.eetimes.com/cypress-furthers-fab-lite/>
[^tenk-fy2007]: Cypress Semiconductor Corp., Form 10-K for fiscal 2007, filed 2008-03-03, Item 1,
    Business. <https://www.sec.gov/Archives/edgar/data/791915/000104746908002122/a2182468z10-k.htm>
[^qtp-042806]: Cypress Semiconductor, Product Qualification Report QTP 042806: *S4ADLATCH Technology, Fab 2*, January 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025144943/https://www.cypress.com/file/92521/download>
[^qtp-051005]: Cypress Semiconductor, Product Qualification Report QTP 051005: *Automotive PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211130190834/https://www.cypress.com/file/92671/download>
[^qtp-062509]: Cypress Semiconductor, Product Qualification Report QTP 062509: *Neutron Device Family, S4AD-5 Technology, GSMC*, July 2014.
    <https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-062509-psoc21x34-95xx-gsmc-productqualificationreport-en.pdf>
[^qtp-102101]: Cypress Semiconductor, Product Qualification Report QTP 102101: *Synchronous/Asynchronous Dual Port SRAM (3.3V and 5V), R42HD Technology, Fab 4 Qualification*, July 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-102101-synchronous-asynchronous-dual-port-sram-3.3v-and-5v-r42hd-technology-fab-4-qualification-productqualificationreport-en.pdf>

[^ar-fy2004]: Cypress Semiconductor Corp., *2004 Annual Report* with Form 10-K, fiscal year ended
    2005-01-02: Item 1, Research and development.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2004.pdf>

[^psoc-history]: Infineon Technologies, *20 years of PSoC: How it started*, Wayback Machine copy of
    2025-07-13 (the live page now redirects elsewhere).
    <https://web.archive.org/web/20250713043850/https://www.infineon.com/cms/en/product/promopages/20-years-of-psoc/how-it-started/>
