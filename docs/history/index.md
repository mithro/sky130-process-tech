(history-index)=
# Before S8: Cypress's process technologies

SKY130 began as S8, a Cypress Semiconductor process. This section traces the Cypress processes that
came before S8: where they were developed and run, what was made on them, what their stackups were, and
how they led to S8. It is a history kept apart from the SKY130 reference, which starts at
{ref}`overview-index`, and it uses its own source list, {ref}`history-sources`.

## The short version

* **Cypress made its own processes, one generation at a time.** From 1.2 µm CMOS in 1984 to 90 nm in
  2004, most generations began as SRAM processes: RAM3 at 0.5 µm, RAM5 at 0.25 µm, RAM 8 at 0.13 µm.
  See {ref}`history-technologies`.[^fu-cypress][^ar-fy1995][^ar-fy1998][^ar-fy2002]
* **Four fabs of its own.** San Jose (Fab 1), Round Rock, Texas (Fab 2) and two fabs on one site in
  Bloomington, Minnesota (Fab 3 and Fab 4). Fab 4, built from 1994, is the fab SkyWater runs today.
  See {ref}`history-fabs`.[^ar-fy1993][^ar-fy1995]
* **SONOS arrived in 2001.** S4AD-5, a 0.35 µm process built on the R42D SRAM process with six more
  masks, made the first PSoC chips at Round Rock and later at Bloomington and at Grace in Shanghai. See
  {ref}`history-sonos-s4`.[^qtp-021507]
* **S8 joined the two lines.** S8 is a 0.13 µm SONOS process of the same generation as Cypress's C8,
  R8 and L8, with S4AD-5's 110 Å oxide as its thick gate oxide. See
  {ref}`history-s8-lineage`.[^pin-152804][^qtp-113005]

:::{figure} /_static/figures/history-lineage.svg
:alt: Four boxes one above the other joined by downward arrows: R42D in 1997, S4AD-5 in 2001, S8 in 2007 to 2008, and SKY130. A side box, C8 in 2005, points into the S8 box.
:width: 560px
:name: fig-history-lineage

How S8 descends from the earlier Cypress processes. S4AD-5 was built on R42D, and S8 carries the SONOS of S4AD-5 into the 0.13 µm generation.[^qtp-021507][^qtp-113005] The link from C8 is our reading of the shared first metal and the common generation; no source states it.[^qtp-043004]
:::

## Timeline

| Year | Event |
|---|---|
| 1984 | First product, a CMOS memory with 1.2 µm transistors (single source)[^fu-cypress] |
| 1986 | Fab 2 opens in Round Rock, Texas[^ar-fy2008][^sd-2007-fab2] |
| 1991 | Fab 3 in Bloomington, bought from Control Data, begins operation[^ar-fy1993][^strib-2017] |
| 1995 | Fab 4, eight-inch, opens beside Fab 3; RAM3, the 0.5 µm SRAM process, is released[^ar-fy1995][^ar-fy1996] |
| 1996 | Fab 1 in San Jose becomes an R&D fab[^tenq-1996q3] |
| 1997 | First 0.35 µm SRAM; R42D and R42HD qualified at Fab 4[^eet-1997-sram035][^qtp-097483] |
| 1998 | Fab 3 closes; first revenue on 0.25 µm (RAM5)[^ar-fy1998] |
| 2001 | S4AD-5, the first SONOS process, qualified at Fab 2; R7 processes at 0.16 and 0.15 µm (Cypress's reports)[^qtp-021507][^qtp-012801] |
| 2002 | RAM 8 brings 0.13 µm to Fab 4 (single source)[^ar-fy2002] |
| 2005 | C8 logic process qualified; foundry deal with Grace[^qtp-043004][^ar-fy2005] |
| 2006 | 0.35 µm SONOS and C8 move to Grace[^ar-fy2006][^eet-2006-c8] |
| 2007 | First S8 products announced; Fab 1 sold[^ew-2007-s8][^ar-fy2009] |
| 2008 | First S8 qualification at Fab 4; Fab 2 closes[^qtp-113005][^ar-fy2008] |

Every year in the table is cited; the pages give the full sources and the points where sources
disagree.

## How to read this section

* **Several sources per claim.** Each claim is backed by two or more independent sources where they
  exist. A claim resting on Cypress's own documents alone says so ("Cypress's reports"), and a claim
  with one source is marked "(single source)".
* **Conflicts are shown.** Where sources disagree, the page gives each version and its source.
* **Readings are labelled.** Our inferences are marked "our reading" or "our arithmetic".
* **Qualification reports.** Much of the detail comes from Cypress's product qualification reports,
  now published by Infineon. They were reissued over the years, and the reissues sometimes rename
  sites and drop or misprint codes; see {ref}`history-fabs` and {ref}`history-naming`.

```{toctree}
:maxdepth: 1
:hidden:

fabs
technologies
sonos-s4
s8-lineage
naming
stackups
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
[^eet-1997-sram035]: EE Times, *Cypress Introduces its First 0.35-µm SRAM*, 1997-11-19.
    <https://www.eetimes.com/cypress-introduces-its-first-0-35-m-sram/>
[^eet-2006-c8]: Mark LaPedus, *Cypress transfers 130-nm process to Grace*, EE Times, 2006-07-19.
    <https://www.eetimes.com/cypress-transfers-130-nm-process-to-grace/>
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
    <https://www.infineon.com/dgdl/Infineon-QTP_021507_Failsafe_Device_Family_&_Options_S4AD-5_SONOS_Technology_Fab_2-ProductQualificationReport-v02_00-EN.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>
[^qtp-113005]: Cypress Semiconductor, Product Qualification Report QTP 113005: *64K Serial Non-Volatile SRAM Product Family, S8 Technology, CMI (Fab 4)*, January 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^qtp-097483]: Cypress Semiconductor, Product Qualification Report QTP 97483: *Low Voltage Deep Synchronous FIFO High Speed 100-MHZ Operation, R42D -- Fab 4*, May 2017.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97483-low-voltage-deep-sync-fifos-r42d-technology-fab4-device-cy7c42-v-productqualificationreport-en.pdf>
[^qtp-012801]: Cypress Semiconductor, Product Qualification Report QTP 012801: *4 Meg SRAM Device R7LD-1.8 Technology, Fab4*, October 2004;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210302225236/https://www.cypress.com/file/91706/download>
[^qtp-043004]: Cypress Semiconductor, Product Qualification Report QTP 043004: *DDR2-PLL Device Family, C8Q-3R, Fab 4*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205122906/https://www.cypress.com/file/92151/download>
