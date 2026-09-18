<!-- Generated from data/filings.yaml by tools/gen_filings.py; do not edit. -->

(filings-index)=
# Financial and corporate filings index

A catalogue of financial and corporate filings that document the
ownership, business and process lineage of the fab that makes
SKY130: Cypress Semiconductor's Minnesota fab (Fab 4), its 2017 sale
to SkyWater Technology Foundry, SkyWater's life as a public company,
its licence of Cypress process IP (now Infineon's), its 2025 purchase
of Infineon's Austin fab (Fab 25, a former Cypress fab) and its 2026
acquisition by IonQ, together with filings by other companies that
name SkyWater or the Cypress fab. It complements the
{doc}`public sources inventory <../public-sources>`: a filing enters
the inventory only when a page cites it. See
`docs/plans/filings-index-design.md` for the inclusion rules.

The index holds 86 filings.

## Other views

* {ref}`filings-by-company`
* {ref}`filings-by-year`
* {ref}`filings-by-type`
* {ref}`filings-by-relationship`
* {ref}`filings-audits`

```{toctree}
:hidden:

by-company
by-year
by-type
by-relationship
audits
```

## Lineage timeline

* **2017-03-01** — Cypress reports the sale of its Minnesota fab (Fab 4, Bloomington) to SkyWater's owners as completed during the first quarter of fiscal 2017. See {ref}`the filing <filing-cypress-10-q-2017-05-02>`.
* **2020-04-16** — Infineon completes its acquisition of Cypress Semiconductor. See {ref}`the filing <filing-cypress-8-k-2020-04-16>`.
* **2021-04-22** — SkyWater Technology files the final prospectus for its initial public offering. See {ref}`the filing <filing-skywater-424b4-2021-04-22>`.
* **2025-06-30** — SkyWater completes the purchase of Infineon's Austin fab (Fab 25). See {ref}`the filing <filing-skywater-8-k-2025-07-03>`.
* **2026-07-31** — IonQ completes its acquisition of SkyWater Technology. See {ref}`the filing <filing-skywater-8-k-2026-07-31>`.
* **2026-08-10** — SkyWater deregisters from SEC reporting following the IonQ merger. See {ref}`the filing <filing-skywater-15-12g-2026-08-10>`.

## How to read an entry

Each entry gives the filer, the form and what it covers, the filing
date and identifier, links to the copies used, a short summary of
what it says about the SKY130 lineage with one or two verbatim
quotes and their location in the document, the auditor's report when
one was read, the record's relationship tags, its public-sources
inventory key when it has one, and related pages of this reference.
A `Note:` line records a caveat, including a disagreement between
this filing and another public source.

## EDGAR access note

`sec.gov` requires a contact address in the HTTP User-Agent header,
which this project's checking tools do not send. Every EDGAR
document below is therefore read from a Wayback Machine capture or a
company investor-relations copy; the `sec.gov` link is kept as the
canonical citation but was not itself fetched by this project.

## Counts

By company: Cypress Semiconductor Corporation (25), SkyWater Technology, Inc. (42), Infineon Technologies AG (7), IonQ, Inc. (3), D-Wave Quantum Inc. (4), QuickLogic Corporation (1), Weebit Nano Limited (4).

By type: Annual reports (41), Quarterly and half-year reports (18), Current reports and exhibits (11), Registration statements and prospectuses (7), Proxy statements (6), Announcements and deregistrations (3).

By year: 1994 (1), 1996 (1), 1997 (1), 1998 (1), 1999 (1), 2000 (1), 2002 (1), 2003 (1), 2004 (1), 2005 (1), 2006 (1), 2007 (1), 2008 (1), 2009 (1), 2010 (1), 2011 (1), 2012 (1), 2013 (1), 2014 (1), 2016 (1), 2017 (2), 2018 (1), 2019 (2), 2020 (3), 2021 (9), 2022 (8), 2023 (11), 2024 (9), 2025 (9), 2026 (12).

## Known gaps

Filings known to exist -- named in another filing's exhibit index, an
inventory entry already cited elsewhere in this reference, or this
project's own discovery notes -- but for which no copy could be found
or read that is not `sec.gov` itself.

**Cypress Semiconductor Corporation**

* Form 10-Q/A for the quarter ended 2003-03-30 -- No Wayback capture of the EDGAR folder exists; the document is EDGAR-only. Cited elsewhere in this reference as inventory key CYP-07.
* 8-K announcing the 2019 merger agreement with Infineon (~June 2019) -- No Wayback capture and no non-EDGAR copy found; only a DEFA14A capture from the same period has been located.
* DEFM14A, definitive merger proxy statement for the 2019-2020 Infineon acquisition -- No Wayback capture and no non-EDGAR copy found.
* Form 10-K for fiscal year 2019 (last Cypress 10-K, filed in early 2020) -- annualreports.com has no NASDAQ\_CY\_2019 file (confirmed HTTP 404 again in this session); no Wayback capture found either.
* Form 10-K/A, 2020 -- No Wayback capture and no non-EDGAR copy found.
* Form 15-12B, deregistration following the Infineon merger (2020) -- No Wayback capture and no non-EDGAR copy found.
* Annual reports to shareholders for fiscal years 1991-1993 -- annualreports.com's Cypress archive begins at fiscal 1994 (NASDAQ\_CY\_1991, \_1992 and \_1993 each answer HTTP 404, confirmed in this session); no other public copy of these years was found. (The fiscal-1993 Form 10-K itself, a different document, is held: see cypress-annual-report-fy1993).
* A standalone annual report to shareholders for fiscal year 1994 -- annualreports.com's archive has no NASDAQ\_CY file of its own for fiscal 1994; that year's figures appear only as prior-year comparatives inside the fiscal-1995 report (cypress-annual-report-fy1995).
* Annual report to shareholders for fiscal year 2000 (NASDAQ\_CY\_2000.pdf) -- A public copy exists and was fetched, but every page returned zero extractable characters of body text with the tools available in this project's environment (pypdf and PyMuPDF); no quotation from it could be verified, so no record was added.
* Annual report to shareholders for fiscal year 2014 (NASDAQ\_CY\_2014.pdf) -- A public copy exists and its text was fully readable, but this particular edition is a short "highlights" booklet that does not mention Bloomington, Minnesota, Fab 4 or wafer manufacturing anywhere in its 8 pages; it does not meet the design's inclusion rule (section 1) of saying something specific about the Minnesota fab, so no record was added.

**SkyWater Technology, Inc.**

* Confidential draft registration statement DRS/A No. 1 (2020-09-30) -- Only the EDGAR filing-index page was captured by the Wayback Machine; the document text itself was not found there or elsewhere.
* Process Technology License Agreement (exhibit 10.6/10.7 of the S-1/A) -- Not retrievable without EDGAR; known only from the S-1/A's own exhibit index, which is not itself a copy of the exhibit.

## All filings

Sorted by filing date, then id.

(filing-cypress-annual-report-fy1993)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor Form 10-K for the fiscal year ended 1994-01-03 (fiscal year 1993)** (filed 1994-03-16; document NASDAQ_CY_1994).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1994.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1994.pdf).
  The earliest Cypress filing in this index. This bare Form 10-K for fiscal year 1993 names the Minnesota plant "Fab 3", says it commenced operations in 1991 (the year SkyWater's later 10-Ks use for a 26-year captive period, at odds with the 20-year figure in SkyWater's IPO filings), and gives its size as 170,000 square feet on 17 acres in Bloomington. The Company's three fabs then ran 0.65-1.2 µm CMOS, 0.5-0.8 µm BiCMOS and 0.65 µm Flash processes. This 1991-start "Fab 3" is the original, 6-inch plant, shut down in 1998 (cypress-annual-report-fy1998); the 8-inch fab SkyWater actually bought in 2017 -- called "Fab 4", then "Fab 4a" -- broke ground in August 1994 and began production in 1995 (cypress-annual-report-fy1995), so the 26-year figure (1991-2017) counts continuous Cypress operation of the Bloomington site, not the age of the building SkyWater received. "Cypress Minnesota (Fab 3), which commenced operations in 1991, is the Company's newest wafer fabrication facility." (Form 10-K, Item 1, Business, Manufacturing); "an approximately 170,000 square foot wafer fabrication facility (Fab 3) on 17 acres of land in Bloomington, Minnesota" (Form 10-K, Item 2, Properties)
  Auditor: Price Waterhouse, 1994-01-25: "PRICE WATERHOUSE San Jose, California January 25, 1994".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`investment and government funding for the Minnesota fab <filings-rel-minnesota-fab-investment>`.
  Related pages: {ref}`overview-index` — The 10-K is the earliest filing in this index to date the Minnesota fab's 1991 start, the year later cited for a 26-year captive period.
  Note: The EDGAR filing date and accession number were not retrieved; the cover page of this copy prints "Filed 03/16/94 for the Period Ending 01/03/94", which is used as filed.

(filing-cypress-annual-report-fy1995)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 1995 Annual Report to shareholders, for the fiscal year ended 1996-01-01** (filed 1996-01-19; document NASDAQ_CY_1995).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1995.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1995.pdf).
  Cypress's 1995 annual report. It records that a new, second Minnesota plant, "Fab IV" (an 8-inch wafer fab, distinct from the original 1991 "Fab III"), broke ground in August 1994 and shipped first revenue wafers in 1995, and that the Company invested \$194.9 million in capital equipment in 1995, mainly to expand the Minnesota, Texas and San Jose fabs. "Fab IV in Bloomington, Minnesota, produced its first revenue wafers in only 11 months, and contributed over \$18 million to Cypress's 1995 revenue." (Annual report, "Capacity to Grow" section); "The Company opens its new, state-of-the-art 8-inch wafer manufacturing plant in Bloomington, Minnesota, which offers enough additional manufacturing capacity to permit growth to the \$1 billion revenue level." (Annual report, 1995 highlights timeline)
  Auditor: Price Waterhouse LLP, 1996-01-19: "Price Waterhouse LLP San Jose, California January 19, 1996".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`investment and government funding for the Minnesota fab <filings-rel-minnesota-fab-investment>`.
  Related pages: {ref}`overview-index` — The report records the 1995 addition of a second, 8-inch Minnesota fab (Fab IV) alongside the original 1991 fab, by then called Fab III.
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the date of the auditor's report printed in the copy, so the document was published on or after it.

(filing-cypress-annual-report-fy1996)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 1996 Annual Report to shareholders, for the fiscal year ended 1996-12-30** (filed 1997-02-25; document NASDAQ_CY_1996).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1996.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1996.pdf).
  Cypress's 1996 annual report. It says the Company manufactured its products at four wafer fabs in California, Minnesota and Texas, and records restructuring charges that transferred equipment to the Texas and Minnesota production fabs. "Cypress manufactures its products at four wafer manufacturing plants in California, Minnesota, and Texas." (Annual report, corporate overview)
  Auditor: Price Waterhouse LLP, 1997-02-25: "Price Waterhouse LLP San Jose, California January 20, 1997, except as to Note 8, which is as of February 25, 1997".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>`.
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the later of the two dates in the auditor's report (a note-specific qualification), so the document was published on or after it.

(filing-cypress-annual-report-fy1997)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 1997 Annual Report to shareholders, for the fiscal year ended 1997-12-29** (filed 1998-03-06; document NASDAQ_CY_1997).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1997.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1997.pdf).
  Cypress's 1997 annual report. It is the first report in this index to name the 8-inch Minnesota plant "Fab 4" (distinct from the original, 6-inch "Fab 3"), producing 1.78 times more chips per wafer, and says the Company's primary production facilities were Texas Fab 2 and Minnesota Fabs 3 and 4, with Fabs 2 and 3 running 6-inch wafers primarily on 0.6 µm processes; before the restructuring announced on 1998-03-09, its plan had been to ramp sub-0.5 µm processes in Fab 4. "Our newest wafer fabrication facility, Fab 4 in Bloomington, Minnesota, produces 8-inch wafers with 1.78 times more chips per wafer than the 6-inch wafers manufactured in Minnesota Fab 3 and Fab 2 in Round Rock, Texas." (Annual report, shareholder letter); "Cypress's primary production facilities are Texas Fab 2 and Minnesota Fabs 3 and 4." (Annual report, shareholder letter)
  Auditor: Price Waterhouse LLP, 1998-03-06: "Price Waterhouse LLP San Jose, California January 20, 1998, except as to Note 9, which is as of March 6, 1998".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`Cypress process technologies made or transferred at the fab (0.13 µm, S8, SONOS) <filings-rel-cypress-process-technology>`.
  Related pages: {ref}`overview-index` — The report is the first in this index to name "Fab 4" as the 8-inch Minnesota plant, alongside the original, 6-inch "Fab 3".
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the later of the two dates in the auditor's report (a note-specific qualification), so the document was published on or after it.

(filing-cypress-annual-report-fy1998)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 1998 Annual Report to shareholders, for the fiscal year ended 1999-01-03** (filed 1999-01-25; document NASDAQ_CY_1998).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1998.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1998.pdf).
  Cypress's 1998 annual report. During 1998 Cypress shut down the original, 6-inch Minnesota "Fab 3" and consolidated its assets into the 8-inch "Fab 4", and separately upgraded its San Jose R&D fab (Fab 1) to eight-inch capability to match Fab 4, as part of a \$58.9 million restructuring described as a "major and rapid move away from six-inch to eight-inch manufacturing capability". "The shutdown of Fab 3, located in Bloomington, Minnesota and consolidation of parts of Fab 3 operations with other operations of Cypress." (Annual report, Management's Discussion and Analysis, restructuring); "The conversion of an existing research and development fab located in San Jose (Fab 1) to eight-inch capability in order to be compatible with the state of the art eight-inch Minnesota manufacturing facility." (Annual report, Management's Discussion and Analysis, restructuring)
  Auditor: PricewaterhouseCoopers LLP, 1999-01-25: "PricewaterhouseCoopers LLP San Jose, California January 25, 1999".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`Cypress process technologies made or transferred at the fab (0.13 µm, S8, SONOS) <filings-rel-cypress-process-technology>`.
  Related pages: {ref}`overview-index` — The report records the 1998 shutdown of the original 6-inch Minnesota Fab 3 and the consolidation of Minnesota manufacturing into the 8-inch Fab 4.
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the date of the auditor's report printed in the copy, so the document was published on or after it.

(filing-cypress-annual-report-fy1999)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 1999 Annual Report to shareholders, for the fiscal year ended 2000-01-02** (filed 2000-03-02; document NASDAQ_CY_1999).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1999.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1999.pdf).
  Cypress's 1999 annual report. Its body pages are set in a font whose glyphs pypdf cannot map to Unicode, so ordinary extraction returns literal glyph-id names or garbled text; the font's glyph table turns out to be a constant offset from the character's WinAnsi code, which tools/check\_filings.py now decodes for this one document (independent review finding V-11). Decoded, the report recaps the 1998 shutdown of the original, 6-inch Minnesota Fab 3, and records a 1999-2000 capital-equipment plan to expand the Minnesota site with two further fabs, "Fab 4b" and "Fab 4c", alongside the existing 8-inch "Fab 4a" -- fab designations that appear nowhere else in this index. "A majority of the equipment purchased was for Fab 4a located in Minnesota to increase its capacity and capability." (Annual report, Management's Discussion and Analysis, Liquidity and Capital Resources); "Capital expenditures in 2000 are expected to be significantly higher compared to 1999 as Cypress continues its efforts to increase its wafer manufacturing capabilities and capacity by purchasing more equipment for Fab 4a and by constructing Fab 4b and Fab 4c, located on the same site as Fab 4a in Minnesota." (Annual report, Management's Discussion and Analysis, Liquidity and Capital Resources)
  Auditor: PricewaterhouseCoopers LLP, 2000-03-02: "PricewaterhouseCoopers LLP San Jose, California January 26, 2000, except as to Note 12 which is as of March 2, 2000".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`investment and government funding for the Minnesota fab <filings-rel-minnesota-fab-investment>`.
  Related pages: {ref}`overview-index` — The report is the only one in this index to name a planned "Fab 4b" and "Fab 4c" alongside "Fab 4a" on the Minnesota site, and recaps the 1998 shutdown of the original Fab 3.
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the later of the two dates in the auditor's report (a note-specific qualification), so the document was published on or after it. Ordinary PDF text extraction (pypdf, with and without fontTools, and PyMuPDF) cannot read the body pages of this particular copy; the font's glyph table happens to be a constant offset from the character's WinAnsi code, which tools/check\_filings.py decodes for this one document only (keyed by identifier.value), so the quotes above remain machine-verifiable with --online.

(filing-cypress-annual-report-fy2001)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 2001 Annual Report to shareholders, for the fiscal year ended 2001-12-30** (filed 2002-02-28; document NASDAQ_CY_2001).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2001.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2001.pdf).
  Cypress's 2001 annual report. It records the transfer of 0.12-micron technology from the San Jose R&D fab to the Minnesota manufacturing fab (Fab 4), notes that the San Jose R&D fab was itself converted from six-inch to eight-inch wafers in fiscal 2000 to match Minnesota, and describes Fab 4 as Cypress's "technologically advanced, eight-inch wafer production facility located in Minnesota". "0.12-micron technology from our eight-inch R&D Fab in San Jose, California to our eight-inch manufacturing fab in Minnesota" (Management's Discussion and Analysis, Research and development); "Cypress's technologically advanced, eight-inch wafer production facility located in Minnesota (Fab 4)." (Notes to Consolidated Financial Statements, Segment Information)
  Auditor: PricewaterhouseCoopers LLP, 2002-02-28: "PricewaterhouseCoopers LLP San Jose, California January 23, 2002, except as to Notes 15 and 18, which are as of February 28, 2002".
  Relationships: {ref}`Cypress process technologies made or transferred at the fab (0.13 µm, S8, SONOS) <filings-rel-cypress-process-technology>`.
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the later of the two dates in the auditor's report (a note-specific qualification), so the document was published on or after it.

(filing-cypress-annual-report-fy2002)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 2002 Annual Report, including the Form 10-K for the fiscal year ended 2002-12-29** (filed 2003-03-07; document NASDAQ_CY_2002).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2002.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2002.pdf).
  Cypress's 2002 annual report. In October 2002 the Company entered into an agreement with Honeywell to jointly develop a 0.13-micron Silicon-On-Insulator process in Fab 4 (the earliest dated record of this partnership in this index; the FY2003 report already in the inventory describes the continuing programme). It also records manufacturing at two sub-micron fabs, Fab 4 and Fab 2, running 0.13 through 0.8 µm CMOS, 0.25 and 0.8 µm BiCMOS and 0.35 µm SONOS processes. "In October 2002, we entered into an agreement with Honeywell to jointly develop a 0.13-micron Silicon-On-Insulator ("SOI") process technology in Fab 4." (Form 10-K, Item 1, Business, Manufacturing); "In fiscal 2002, we continued to manufacture our products at two sub-micron wafer fabrication facilities located in Fab 4 and Fab 2." (Form 10-K, Item 1, Business, Manufacturing)
  Auditor: PricewaterhouseCoopers LLP, 2003-03-07: "PricewaterhouseCoopers LLP San Jose, California March 7, 2003".
  Relationships: {ref}`Cypress process technologies made or transferred at the fab (0.13 µm, S8, SONOS) <filings-rel-cypress-process-technology>`.
  Related pages: {ref}`overview-index` — The report dates the start of the Honeywell 0.13 µm silicon-on-insulator programme in Fab 4 to October 2002, a year earlier than the FY2003 report already in the inventory.
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the date of the auditor's report printed in the copy, so the document was published on or after it.

(filing-cypress-annual-report-fy2003)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 2003 Annual Report, including the Form 10-K for the fiscal year ended 2003-12-28** (filed 2004-02-27; document NASDAQ_CY_2003).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2003.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2003.pdf).
  Cypress's 2003 annual report. It names its two sub-micron fabs (Fab 2 in Texas, Fab 4 in Minnesota), lists the CMOS, BiCMOS and 0.35 µm SONOS processes they run, says 0.13 µm and 0.15 µm CMOS were about 65 % of Fab 4's output in 2003, and describes a 0.13 µm silicon-on-insulator development programme with Honeywell in Fab 4. "In 2003 these processes accounted for approximately 65% of the output of Fab 4." (Form 10-K section); "Fab 2, located in Texas and Fab 4, located in Minnesota. These fabrication facilities utilize our proprietary 0.13 through 0.8-micron CMOS, 0.25 and 0.8-micron BiCMOS, and 0.35-micron Silicon Nitride Oxide Silicon (SONOS) processes." (Form 10-K section)
  Auditor: PricewaterhouseCoopers LLP, 2004-02-27: "/s/ PricewaterhouseCoopers LLP San Jose, California February 27, 2004".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`Cypress process technologies made or transferred at the fab (0.13 µm, S8, SONOS) <filings-rel-cypress-process-technology>`.
  Related pages: {ref}`overview-index` — The report dates the 0.13 µm ramp in Fab 4 that the overview's history cites from the 2003 10-Q/A.
  Note: The EDGAR filing date and accession number of the 10-K were not retrieved; filed gives the date of the auditor's report printed in the copy, so the document was published on or after it.

(filing-cypress-annual-report-fy2004)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 2004 Annual Report, including the Form 10-K for the fiscal year ended 2005-01-02** (filed 2005-03-18; document NASDAQ_CY_2004).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2004.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2004.pdf).
  Cypress's 2004 annual report (inventory CYP-08). It says 90 nm technology is in production at the Minnesota facility, lists the fabs' CMOS, BiCMOS and SONOS processes, and says an image sensor was made in Fab 4 in Bloomington. "Our 90-nanometer technology is now in production at our Minnesota facility." (Form 10-K section); "The Belgian team has already produced a working image sensor in Cypress's Fab 4 wafer fabrication plant in Bloomington, Minn." (Letter to shareholders)
  Auditor: PricewaterhouseCoopers LLP, 2005-03-17: "/s/ PricewaterhouseCoopers LLP San Jose, California March 17, 2005".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`Cypress process technologies made or transferred at the fab (0.13 µm, S8, SONOS) <filings-rel-cypress-process-technology>`.
  Inventory: CYP-08.
  Related pages: {ref}`overview-index` — The report places Cypress's 90 nm production in the Minnesota fab whose history the overview gives.
  Note: The EDGAR filing date and accession number of the 10-K were not retrieved; filed gives the date of the 10-K signatures printed in the copy.

(filing-cypress-annual-report-fy2005)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 2005 Annual Report, including the Form 10-K for the fiscal year ended 2006-01-01** (filed 2006-03-17; document NASDAQ_CY_2005).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2005.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2005.pdf).
  Cypress's 2005 annual report. It records the December 2005 strategic foundry partnership with China's Grace Semiconductor Manufacturing Corporation (which the FY2006 report already in the inventory describes as taking effect), continued transition of the Bloomington, Minnesota facility to 90 nm and 0.13 µm CMOS, and, in its Item 2 Properties table, lists Bloomington, Minnesota twice: 170,000 square feet owned and a further 108,000 square feet leased under a synthetic lease, 278,000 square feet in total -- the same total the cypress-annual-report-fy2008 record quotes as wholly owned, after that synthetic lease was terminated in fiscal 2007. "During fiscal 2005, we continued our transition to more advanced process technologies in our facility in Bloomington, Minnesota including our 90-nanometer and 0.13-micron CMOS process technologies." (Form 10-K, Item 1, Business, Manufacturing); "In December 2005, we entered into a strategic foundry partnership with China's Grace Semiconductor Manufacturing Corporation ("Grace"). Under the terms of the agreement, we will transfer certain of our proprietary process technologies to Grace." (Form 10-K, Item 1, Business, Manufacturing)
  Auditor: PricewaterhouseCoopers LLP, 2006-03-17: "PricewaterhouseCoopers LLP San Jose, California March 17, 2006".
  Relationships: {ref}`Cypress process technologies made or transferred at the fab (0.13 µm, S8, SONOS) <filings-rel-cypress-process-technology>` · {ref}`Cypress selling wafer-line capacity to outside customers before the 2017 sale <filings-rel-cypress-third-party-foundry>`.
  Related pages: {ref}`overview-index` — The report is the original December 2005 announcement of the Grace Semiconductor foundry partnership that the FY2006 report already in the inventory describes as in effect.
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the date of the auditor's report printed in the copy, so the document was published on or after it. The Item 2 Properties table lists 170,000 square feet owned and 108,000 square feet leased (one building under a synthetic lease with San Jose, footnote 2) at Bloomington, Minnesota, 278,000 square feet in total; this matches the 278,000 square feet cypress-annual-report-fy2008 gives as wholly owned once that synthetic lease was terminated in fiscal 2007, and the 170,000 square feet cypress-annual-report-fy1993 gives earlier. The figures are consistent across these three records, not conflicting.

(filing-cypress-annual-report-fy2006)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 2006 Annual Report and 2007 Proxy Statement, including the Form 10-K for the fiscal year ended 2006-12-31** (filed 2007-03-28; document NASDAQ_CY_2006).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2006.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2006.pdf).
  Cypress's 2006 annual report. The shareholder letter says 0.35 µm production moved to Grace Semiconductor in Shanghai, freeing Fab 4 in Minnesota for 90 nm technologies; the 10-K lists the 90 nm to 0.8 µm CMOS, BiCMOS and 0.35 µm SONOS processes of the Round Rock and Bloomington fabs. "Grace Semiconductor Manufacturing Corp. (GSMC) in Shanghai to produce 0.35-micron wafers, freeing up capacity in our Minnesota Fab 4 plant" (Letter to shareholders); "These fabrication facilities utilize our proprietary 90-nanometer and 0.13 through 0.8-micron CMOS, 0.25 and 0.8-micron BiCMOS, and 0.35-micron Silicon Nitride Oxide Silicon ("SONOS") processes." (Form 10-K section, Item 1, Business)
  Auditor: PricewaterhouseCoopers LLP, 2007-03-01: "/s/ PricewaterhouseCoopers LLP San Jose, California March 1, 2007".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`Cypress process technologies made or transferred at the fab (0.13 µm, S8, SONOS) <filings-rel-cypress-process-technology>`.
  Related pages: {ref}`overview-index` — The report records moving 0.35 µm wafer production to an outside foundry to free the Minnesota fab for 90 nm technologies.
  Note: The EDGAR filing dates and accession numbers were not retrieved; filed gives the latest date printed in the combined document (the proxy statement's), so the copy was published on or after it.

(filing-cypress-10-k-2008-03-03)=
* **Cypress Semiconductor Corporation — Annual report on Form 10-K for the fiscal year ended 2007-12-30** (filed 2008-03-03; SEC accession 0001047469-08-002122).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/791915/000104746908002122/a2182468z10-k.htm) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2007.pdf).
  Cypress's fiscal 2007 10-K (inventory CYP-09), read in the 2007 annual report that wraps it. It records the plan to exit the Texas fab and move production to Minnesota and outside foundries, and the transfers of the 0.35 µm SONOS (2006) and 0.13 µm SRAM and logic (2007) processes to Grace Semiconductor. "In December 2007, Cypress's Board of Directors approved a plan to exit its manufacturing facility in Texas and transfer production to its more cost-competitive facility in Minnesota and outside foundries." (Item 1, Business); "During fiscal 2006, Cypress completed the transfer of its 0.35-micron SONOS process to Grace" (Item 1, Business)
  Auditor: PricewaterhouseCoopers LLP, 2008-03-02: "/s/ PricewaterhouseCoopers LLP".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`Cypress process technologies made or transferred at the fab (0.13 µm, S8, SONOS) <filings-rel-cypress-process-technology>`.
  Inventory: CYP-09.
  Related pages: {ref}`overview-index` — The report explains why production was concentrated in the Minnesota fab from 2008.

(filing-cypress-annual-report-fy2008)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 2008 Annual Report, including the Form 10-K for the fiscal year ended 2008-12-28** (filed 2009-02-26; document NASDAQ_CY_2008).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2008.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2008.pdf).
  Cypress's 2008 annual report. In December 2007 Cypress's board approved exiting its Round Rock, Texas fab and transferring production to the more cost-competitive Minnesota fab and outside foundries, substantially completed in December 2008; from this point Minnesota (Fab 4) was Cypress's only US wafer fab. The Item 2 Properties table gives the owned Bloomington, Minnesota building as 278,000 square feet. "In December 2007, Cypress's Board of Directors approved a plan to exit its manufacturing facility in Texas and transfer production to its more cost-competitive facility in Minnesota and outside foundries." (Form 10-K, Item 1, Business, Manufacturing); "Bloomington, Minnesota 278,000 Manufacturing, research and development" (Form 10-K, Item 2, Properties)
  Auditor: PricewaterhouseCoopers LLP, 2009-02-26: "PricewaterhouseCoopers LLP San Jose, California February 26, 2009".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`Cypress selling wafer-line capacity to outside customers before the 2017 sale <filings-rel-cypress-third-party-foundry>`.
  Related pages: {ref}`overview-index` — The report records the 2007-2008 exit of the Texas fab that left Minnesota (Fab 4) as Cypress's only US wafer fab.
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the date of the auditor's report printed in the copy, so the document was published on or after it.

(filing-cypress-annual-report-fy2009)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 2009 Annual Report, including the Form 10-K for the fiscal year ended 2010-01-03** (filed 2010-03-03; document NASDAQ_CY_2009).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2009.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2009.pdf).
  Cypress's 2009 annual report. The shareholder letter says Cypress sold its San Jose R&D fab (Fab 1) in 2007 and closed the Round Rock, Texas fab (Fab 2) in 2008, leaving Fab 4 in Bloomington, Minnesota as its sole wafer fab; the Form 10-K section says 65% of products were made internally at Fab 4, the balance by external foundries. "While we maintained our Fab 4 facility in Bloomington, Minn., to develop and manufacture new technologies, we sold our Fab 1 R&D plant in San Jose, Calif., in 2007 and closed our Fab 2 facility in Round Rock, Texas, in 2008." (Annual report, shareholder letter); "During fiscal 2009, we manufactured approximately 65% of our semiconductor products at our wafer manufacturing facility in Bloomington, Minnesota. External wafer foundries manufactured the balance of our products." (Form 10-K, Item 1, Business, Manufacturing)
  Auditor: PricewaterhouseCoopers LLP, 2010-03-03: "PricewaterhouseCoopers LLP San Jose, California March 3, 2010".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`Cypress selling wafer-line capacity to outside customers before the 2017 sale <filings-rel-cypress-third-party-foundry>`.
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the date of the auditor's report printed in the copy, so the document was published on or after it.

(filing-cypress-annual-report-fy2010)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 2010 Annual Report, including the Form 10-K for the fiscal year ended 2011-01-02** (filed 2011-02-25; document NASDAQ_CY_2010).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2010.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2010.pdf).
  Cypress's 2010 annual report. It says Cypress decided in 2005 to stop investing in Moore's Law in its internal fabs and adopt a "flex fab" strategy of running and improving Fab 4 while expanding capacity externally with foundry partners, and names "S8" as its 0.13-micron, nonvolatile PSoC wafer fabrication process at Fab 4 -- the process name this reference's step pages trace to SKY130. "Cypress decided to stop investing in Moore's Law in our internal wafer fabs in 2005 and switch to a "flex fab" strategy, meaning that we would continue to run and improve our Fab 4 wafer fabrication plant in Bloomington, Minnesota, but expand our fab capacity externally with foundry partners." (Annual report, "Manufacturing" section); "The rapid rise in demand for PSoC has filled our capacity to manufacture wafers in S8, our 0.13-micron, nonvolatile PSoC wafer fabrication process." (Annual report, "Manufacturing" section)
  Auditor: PricewaterhouseCoopers LLP, 2011-02-25: "PricewaterhouseCoopers LLP San Jose, California February 25, 2011".
  Relationships: {ref}`Cypress process technologies made or transferred at the fab (0.13 µm, S8, SONOS) <filings-rel-cypress-process-technology>` · {ref}`Cypress selling wafer-line capacity to outside customers before the 2017 sale <filings-rel-cypress-third-party-foundry>`.
  Related pages: {ref}`overview-index` — The report is the earliest filing in this index to name Cypress's "S8" process, the 0.13 µm SONOS lineage this reference traces to SKY130.
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the date of the auditor's report printed in the copy, so the document was published on or after it. "Stop investing in Moore's Law" describes a 2005 decision not to develop process nodes below what was already in flight at Fab 4; it does not contradict cypress-annual-report-fy2005 and the existing (already in the index) cypress-annual-report-fy2006, which describe continuing the already-underway 90 nm transition at Fab 4 through 2005 and into 2006 production.

(filing-cypress-annual-report-fy2011)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 2011 Annual Report, including the Form 10-K for the fiscal year ended 2012-01-01** (filed 2012-02-24; document NASDAQ_CY_2011).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2011.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2011.pdf).
  Cypress's 2011 annual report. It attributes anomalously high 2011 capital expenditure to the final build-out of the Minnesota fab to its maximum capacity to support PSoC growth, and says the Company then manufactured approximately 42% of its products internally at Bloomington, Minnesota, the balance by external foundries mainly in Asia -- a lower internal share than the FY2009 (65%) and FY2012 (69%) reports in this index. "The anomalously high capital expenditures in 2011 are due to the final build out of our Minnesota wafer fabrication plant to its maximum capacity to support PSoC growth." (Annual report, capital expenditures discussion); "We currently manufacture approximately 42% of our semiconductor products at our wafer manufacturing facility in Bloomington, Minnesota. External wafer foundries, mainly in Asia, manufactured the balance of our products" (Form 10-K, Item 1, Business, Manufacturing)
  Auditor: PricewaterhouseCoopers LLP, 2012-02-24: "PricewaterhouseCoopers LLP San Jose, California February 24, 2012".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`investment and government funding for the Minnesota fab <filings-rel-minnesota-fab-investment>`.
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the date of the auditor's report printed in the copy, so the document was published on or after it. The 42% internal-manufacturing share is markedly lower than the 65% (FY2009), 69% (FY2012) and 62% (FY2013) figures elsewhere in this index; the report attributes the dip to the Minnesota fab's capacity build-out that year, not to a change in strategy.

(filing-cypress-annual-report-fy2012)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 2012 Annual Report, including the Form 10-K for the fiscal year ended 2012-12-30** (filed 2013-02-28; document NASDAQ_CY_2012).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2012.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2012.pdf).
  Cypress's 2012 annual report. It says the Company manufactured approximately 69% of its products internally at Bloomington, Minnesota (Fab 4), the balance by external foundries mainly in Asia, and that 2012 gross margin reflected underloading in both Fab 4 and the Philippines assembly and test plant. "We currently manufacture approximately 69% of our semiconductor products at our wafer manufacturing facility in Bloomington, Minnesota. External wafer foundries, mainly in Asia, manufactured the balance of our products" (Form 10-K, Item 1, Business, Manufacturing); "underloading in both our wafer fabrication plant (Fab 4 in Minnesota) and our assembly and test plant (CML in Manila)" (Annual report, gross margin discussion)
  Auditor: PricewaterhouseCoopers LLP, 2013-02-28: "PricewaterhouseCoopers LLP San Jose, California February 28, 2013".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`Cypress selling wafer-line capacity to outside customers before the 2017 sale <filings-rel-cypress-third-party-foundry>`.
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the date of the auditor's report printed in the copy, so the document was published on or after it.

(filing-cypress-annual-report-fy2013)=
* **Cypress Semiconductor Corporation — Cypress Semiconductor 2013 Annual Report, including the Form 10-K for the fiscal year ended 2013-12-29** (filed 2014-02-27; document NASDAQ_CY_2013).
  [Original](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2013.pdf) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2013.pdf).
  Cypress's 2013 annual report. It says the Company manufactured approximately 62% of its products internally at Bloomington, Minnesota, the balance by external foundries mainly in Asia, and that during 2013 Cypress completed the sale of the Round Rock, Texas fab whose production it had transferred to Minnesota and outside foundries back in 2008. "We currently manufacture approximately 62% of our semiconductor products at our wafer manufacturing facility in Bloomington, Minnesota. External wafer foundries, mainly in Asia, manufactured the balance of our products" (Form 10-K, Item 1, Business, Manufacturing); "in fiscal 2008 we substantially completed the exit of our manufacturing facility in Texas and transferred production to our more cost-competitive facility in Minnesota and outside foundries. During 2013 we completed the sale of this manufacturing facility." (Form 10-K, Item 7, Management's Discussion and Analysis)
  Auditor: PricewaterhouseCoopers LLP, 2014-02-27: "PricewaterhouseCoopers LLP San Jose, California February 27, 2014".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>` · {ref}`Cypress selling wafer-line capacity to outside customers before the 2017 sale <filings-rel-cypress-third-party-foundry>`.
  Note: The EDGAR filing date and accession number were not retrieved; filed gives the date of the auditor's report printed in the copy, so the document was published on or after it.

(filing-cypress-10-k-2016-03-02)=
* **Cypress Semiconductor Corporation — Annual report on Form 10-K for the fiscal year ended 2016-01-03** (filed 2016-03-02; SEC accession 0001564590-16-013820).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/791915/000156459016013820/cy-10k_20160103.htm) · [Wayback copy](https://web.archive.org/web/20160314155334/https://www.sec.gov/Archives/edgar/data/791915/000156459016013820/cy-10k_20160103.htm) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2015.pdf).
  Cypress's last 10-K before the decision to sell the Minnesota fab. It says about half of its products were made in its Bloomington and Austin wafer fabs and lists the 337,000 square foot Bloomington property. "We currently manufacture approximately 50% of our semiconductor products at our wafer manufacturing facilities in Bloomington, Minnesota and Austin, Texas." (Item 1, Business, Manufacturing); "Bloomington, Minnesota 337,000 Manufacturing, research and development" (Item 2, Properties)
  Auditor: PricewaterhouseCoopers LLP, 2016-03-01: "/s/ PricewaterhouseCoopers LLP San Jose, California March 1, 2016".
  Relationships: {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>`.
  Related pages: {ref}`overview-index` — The report gives the size and role of the Minnesota fab shortly before its sale.

(filing-cypress-10-k-2017-03-01)=
* **Cypress Semiconductor Corporation — Annual report on Form 10-K for the fiscal year ended 2017-01-01** (filed 2017-03-01; SEC accession 0000791915-17-000007).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/791915/000079191517000007/cy-01012017x10xk.htm) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2016.pdf).
  Cypress's fiscal 2016 10-K (inventory CYP-10), read in the 2016 annual report that wraps it. It records the 2016 plan to sell the Bloomington fab, the completed sale in March 2017, and the purchaser's intention to run it as a stand-alone foundry for Cypress and others. "The purchaser intends to operate the fab as a stand-alone business that will manufacture wafers for Cypress and for other semiconductor manufacturers." (Item 1A, Risk factors); "During fiscal 2016, we committed to a plan to sell our wafer manufacturing facility located in Bloomington, Minnesota" (Item 7, Management's discussion and analysis)
  Auditor: PricewaterhouseCoopers LLP, 2017-03-01: "/s/ PricewaterhouseCoopers LLP San Jose, California March 1, 2017".
  Relationships: {ref}`sale of the Minnesota fab subsidiary to SkyWater's owners (2017) <filings-rel-cypress-fab-sale>` · {ref}`Cypress describes its Minnesota (Bloomington) fab <filings-rel-cypress-fab-operations>`.
  Inventory: CYP-10.
  Related pages: {ref}`overview-index` — The report is Cypress's own account of the 2017 sale that the overview cites from the press release CYP-01.

(filing-cypress-10-q-2017-05-02)=
* **Cypress Semiconductor Corporation — Quarterly report on Form 10-Q for the quarter ended 2017-04-02** (filed 2017-05-02; SEC accession 0000791915-17-000030).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/791915/000079191517000030/cy-04022017x10xq.htm) · [Wayback copy](https://web.archive.org/web/20170503100919/https://www.sec.gov/Archives/edgar/data/791915/000079191517000030/cy-04022017x10xq.htm).
  The quarterly report for the quarter in which the Minnesota fab was sold; it reports the sale as completed with a small gain against the 2016 impairment. "The sales of the wafer fabrication facility in Minnesota and the sale of the building in Austin were completed during the first quarter of fiscal 2017." (Notes to the condensed consolidated financial statements, assets held for sale); "In the third quarter of fiscal 2016, the Company committed to a plan to sell its wafer manufacturing facility located in Bloomington, Minnesota" (Notes to the condensed consolidated financial statements, assets held for sale)
  Relationships: {ref}`sale of the Minnesota fab subsidiary to SkyWater's owners (2017) <filings-rel-cypress-fab-sale>`.
  Related pages: {ref}`overview-index` — The report dates the completion of the sale that the overview cites from the press release CYP-01.

(filing-cypress-10-k-2018-02-26)=
* **Cypress Semiconductor Corporation — Annual report on Form 10-K for the fiscal year ended 2017-12-31** (filed 2018-02-26; SEC accession 0000791915-18-000007).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/791915/000079191518000007/cy-12312017x10xk.htm) · [Wayback copy](https://web.archive.org/web/20180304113258/https://www.sec.gov/Archives/edgar/data/791915/000079191518000007/cy-12312017x10xk.htm) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2017.pdf).
  Cypress's fiscal 2017 10-K. It reports the sale of the Minnesota fab subsidiary (headed "Sale of CMI") for gross proceeds of \$30.5 million and repeats that the purchaser makes wafers for Cypress and others. "In fiscal 2017, we completed the sale of our wafer fabrication facility in Minnesota for gross proceeds from the sale of \$30.5 million." (Item 7, Management's discussion and analysis, Sale of CMI); "The purchaser intends to operate the fabrication facility as a stand-alone business that will manufacture wafers for Cypress and for other semiconductor manufacturers." (Item 1A, Risk factors)
  Auditor: PricewaterhouseCoopers LLP, 2018-02-26: "/s/ PricewaterhouseCoopers LLP San Jose, California February 26, 2018 We have served as the Company’s auditor since 1982.".
  Relationships: {ref}`sale of the Minnesota fab subsidiary to SkyWater's owners (2017) <filings-rel-cypress-fab-sale>`.
  Related pages: {ref}`overview-index` — The report gives Cypress's proceeds from the sale of the fab whose history the overview gives.

(filing-cypress-10-k-2019-02-27)=
* **Cypress Semiconductor Corporation — Annual report on Form 10-K for the fiscal year ended 2018-12-30** (filed 2019-02-27; SEC accession 0000791915-19-000006).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/791915/000079191519000006/0000791915-19-000006-index.htm) · [Wayback copy](https://web.archive.org/web/20190228130230/https://www.sec.gov/Archives/edgar/data/791915/000079191519000006/0000791915-19-000006-index.htm) · [investor-relations copy](https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2018.pdf).
  Cypress's fiscal 2018 10-K. It says Cypress still buys manufacturing services from the Bloomington fab it divested in March 2017 and reports the "Sale of Cypress Minnesota Incorporated". "In March 2017, we divested a wafer fabrication facility (commonly called a fab or foundry) located in Bloomington, Minnesota, which reduced our internal manufacturing capacity though we continue to outsource manufacturing services from this facility." (Part I); "Sale of Cypress Minnesota Incorporated In fiscal 2017, we completed the sale of our wafer fabrication facility in Minnesota for gross proceeds of \$30.5 million." (Item 7, Management's discussion and analysis)
  Auditor: PricewaterhouseCoopers LLP, 2019-02-27: "/s/ PricewaterhouseCoopers LLP San Jose, California February 27, 2019".
  Relationships: {ref}`sale of the Minnesota fab subsidiary to SkyWater's owners (2017) <filings-rel-cypress-fab-sale>` · {ref}`Cypress (later Infineon) as SkyWater's wafer customer under the foundry services agreement <filings-rel-cypress-foundry-services>`.
  Related pages: {ref}`overview-index` — The report confirms that Cypress remained a customer of the fab after the sale.

(filing-infineon-annual-report-fy2019)=
* **Infineon Technologies AG — Infineon Technologies Annual Report 2019** (filed 2019-11-22).
  [Original](https://www.infineon.com/assets/row/public/documents/corporate/investors/annual-reports/2019/infineon-annual-report-report-v09-00-en.pdf).
  Infineon's first annual report after agreeing to acquire Cypress. The management's letter calls the planned acquisition the most significant event of the year, and the strategy section introduces Cypress as a company founded in 1982 in San José. "the most significant event is the planned acquisition of Cypress" (Introductory section); "Cypress Semiconductor Corporation was founded in 1982 in San José (USA)" (Introductory section)
  Auditor: KPMG AG Wirtschaftsprüfungsgesellschaft, 2019-11-22: "Munich, 22 November 2019 KPMG AG Wirtschaftsprüfungsgesellschaft".
  Relationships: {ref}`Infineon's acquisition of Cypress (2019-2020) <filings-rel-infineon-cypress-acquisition>`.
  Related pages: {ref}`overview-index` — The report documents Infineon becoming the successor to Cypress, which SkyWater's filings name as the origin of the S130 IP.
  Note: filed gives the latest signature date printed in the report (the responsibility statement, Neubiberg, 22 November 2019); the publication date was not retrieved.

(filing-cypress-8-k-2020-04-16)=
* **Cypress Semiconductor Corporation — Current report: completion of the merger with IFX Merger Sub (Infineon)** (filed 2020-04-16; SEC accession 0001104659-20-047540).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/791915/000110465920047540/0001104659-20-047540-index.htm) · [Wayback copy](https://web.archive.org/web/20250414174141/https://www.sec.gov/Archives/edgar/data/791915/000110465920047540/0001104659-20-047540-index.htm) · [investor-relations copy](https://www.infineon.com/assets/row/public/documents/corporate/investors/infineon-8k-cypress-legaldocument-v50-00-en.pdf).
  Period: event of 2020-04-16.
  Cypress's current report on the closing of its acquisition by Infineon on 2020-04-16, including the termination of its credit agreement and employee stock purchase plan; Infineon hosts a copy on its investor site. "On the Closing Date, Infineon completed the acquisition of Cypress through the Merger." (Item 2.01); "Date of Report (Date of the earliest event reported): April 16, 2020" (Cover page)
  Relationships: {ref}`Infineon's acquisition of Cypress (2019-2020) <filings-rel-infineon-cypress-acquisition>`.
  Related pages: {ref}`overview-index` — The filing dates the change of ownership of the Cypress process IP that SkyWater licenses.

(filing-skywater-drs-2020-08-12)=
* **SkyWater Technology, Inc. — Draft registration statement on Form S-1, confidentially submitted 2020-08-12 (EDGAR filer CMI Acquisition, LLC)** (filed 2020-08-12; SEC accession 0000950123-20-008396).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000095012320008396/filename1.htm) · [Wayback copy](https://web.archive.org/web/20260501234934/https://www.sec.gov/Archives/edgar/data/1819974/000095012320008396/filename1.htm).
  The first draft of SkyWater's IPO registration statement, submitted confidentially in August 2020 and later released on EDGAR. It already gives the 20-year Cypress captive history, the 2017 S130 licence and Cypress's (by then Infineon's) share of revenue: 48 % in 2019 and 65 % in 2018. "Our foundry business was owned and operated by Cypress Semiconductor Corporation, or Cypress, as a captive manufacturing facility for 20 years." (Prospectus Summary); "Cypress, which was acquired in April 2020 by Infineon Technologies AG, accounted for approximately 48% and 65% of our revenue for the fiscal years ended December 29, 2019 and December 30, 2018, respectively." (Risk Factors)
  Relationships: {ref}`SkyWater's 2021 initial public offering <filings-rel-skywater-ipo>` · {ref}`SkyWater describes the fab's Cypress origin <filings-rel-skywater-fab-history>` · {ref}`the 2017 Process Technology License Agreement and its amendments <filings-rel-cypress-technology-license>` · {ref}`Cypress (later Infineon) as SkyWater's wafer customer under the foundry services agreement <filings-rel-cypress-foundry-services>`.
  Related pages: {ref}`overview-index` — The draft is the earliest public SkyWater statement of the fab's Cypress history that the overview relies on.
  Note: The cover legend says the draft "has not been publicly filed"; that describes its status when submitted. The SEC has since released it on EDGAR, and it is cited here from that public copy. This "20 years" figure disagrees with SkyWater's later 10-Ks (skywater-10-k-2025-03-14, skywater-10-k-2026-03-11), which give the Cypress captive period as 26 years.

(filing-infineon-annual-report-fy2020)=
* **Infineon Technologies AG — Infineon Technologies Annual Report 2020** (filed 2020-11-20).
  [Original](https://www.infineon.com/assets/row/public/documents/corporate/investors/annual-reports/2020/infineon-annual-report-report-v10-00-en.pdf).
  Infineon's annual report for the year in which the Cypress acquisition closed (2020-04-16); it describes the integration of Cypress's manufacturing sites, with Austin, Texas as the front-end site. "The acquisition of Cypress was completed on 16 April 2020." (Combined management report); "Infineon integrated the Cypress sites into its manufacturing landscape: Austin (Texas, USA)" (Combined management report, manufacturing)
  Auditor: KPMG AG Wirtschaftsprüfungsgesellschaft, 2020-11-20: "Munich, 20 November 2020 KPMG AG Wirtschaftsprüfungsgesellschaft".
  Relationships: {ref}`Infineon's acquisition of Cypress (2019-2020) <filings-rel-infineon-cypress-acquisition>`.
  Related pages: {ref}`overview-index` — The report shows the Austin fab passing to Infineon, five years before SkyWater bought it.
  Note: filed gives the signature date printed in the report (Neubiberg, 20 November 2020); the publication date was not retrieved.

(filing-skywater-drs-a-2021-01-20)=
* **SkyWater Technology, Inc. — Amendment No. 2 to the draft registration statement on Form S-1, confidentially submitted 2021-01-20** (filed 2021-01-20; SEC accession 0000950123-21-000456).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000095012321000456/filename1.htm) · [Wayback copy](https://web.archive.org/web/20250212175424/https://www.sec.gov/Archives/edgar/data/1819974/000095012321000456/filename1.htm).
  The second amendment to the draft IPO registration statement. It adds interim figures (Cypress/Infineon 32 % of revenue for the nine months to September 2020) and an exhibit index listing the Process Technology License Agreement with Cypress and its first amendment. "Cypress, which was acquired in April 2020 by Infineon Technologies AG, accounted for approximately 32% and 54% of our revenues for the nine months ended September 27, 2020 and September 29, 2019" (Risk Factors); "Process Technology License Agreement, dated as of March 1, 2017, between Cypress Semiconductor Corporation and Cypress Semiconductor (Minnesota) Inc." (Exhibit index, exhibit 10.6)
  Relationships: {ref}`SkyWater's 2021 initial public offering <filings-rel-skywater-ipo>` · {ref}`SkyWater describes the fab's Cypress origin <filings-rel-skywater-fab-history>` · {ref}`the 2017 Process Technology License Agreement and its amendments <filings-rel-cypress-technology-license>` · {ref}`Cypress (later Infineon) as SkyWater's wafer customer under the foundry services agreement <filings-rel-cypress-foundry-services>`.
  Related pages: {ref}`overview-index` — The draft adds the exhibit index that first names the Cypress process licence behind the S130 platform.
  Note: The cover legend describes the draft's status when submitted; the SEC has since released it on EDGAR. Amendment No. 1 (DRS/A, 2020-09-30, accession 0000950123-20-010026) has a captured index page but no captured document.

(filing-skywater-s-1-2021-03-22)=
* **SkyWater Technology, Inc. — Form S-1 registration statement (initial public offering), Registration No. 333-254580** (filed 2021-03-22; SEC accession 0001193125-21-089687).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm) · [Wayback copy](https://web.archive.org/web/20210323222220/https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm).
  SkyWater's IPO registration statement. It says the Bloomington fab was a Cypress captive fab for 20 years, that Oxbow Industries acquired the business from Cypress in March 2017, that a foundry services agreement with Cypress ran to June 2020, that Cypress (acquired by Infineon in April 2020) was 29 % of 2020 revenue, and that S130 base design IP from Cypress was licensed in 2017; the exhibit index lists the Process Technology License Agreement with Cypress (exhibit 10.6). "Before we began independent operations, our fab was owned and operated by Cypress Semiconductor Corporation, or Cypress, as a captive manufacturing facility for 20 years." (Prospectus Summary); "the base design IP portfolio for S130 technologies originating from Cypress (now Infineon) was licensed via a technology license agreement in 2017" (Business)
  Relationships: {ref}`SkyWater's 2021 initial public offering <filings-rel-skywater-ipo>` · {ref}`SkyWater describes the fab's Cypress origin <filings-rel-skywater-fab-history>` · {ref}`sale of the Minnesota fab subsidiary to SkyWater's owners (2017) <filings-rel-cypress-fab-sale>` · {ref}`the 2017 Process Technology License Agreement and its amendments <filings-rel-cypress-technology-license>` · {ref}`Cypress (later Infineon) as SkyWater's wafer customer under the foundry services agreement <filings-rel-cypress-foundry-services>` · {ref}`Oxbow ownership, management fees and property transactions <filings-rel-oxbow-related-party>` · {ref}`SkyWater names its suppliers <filings-rel-skywater-suppliers>`.
  Inventory: SEC-01.
  Related pages: {ref}`step-001` — The starting-material step page cites the registration statement as SEC-01 for the wafer suppliers SkyWater names.; {ref}`machines-index` — The machines index cites SEC-01 for the fab's tool count and process platforms.; {ref}`materials-index` — The materials index cites SEC-01 for the raw-material suppliers SkyWater names.
  Note: This "20 years" figure disagrees with SkyWater's later 10-Ks (skywater-10-k-2025-03-14, skywater-10-k-2026-03-11), which give the Cypress captive period as 26 years.

(filing-skywater-s-1-a-2021-04-12)=
* **SkyWater Technology, Inc. — Amendment No. 1 to Form S-1 registration statement, Registration No. 333-254580** (filed 2021-04-12; SEC accession 0001193125-21-112378).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000119312521112378/d26688ds1a.htm) · [Wayback copy](https://web.archive.org/web/20210412120508/https://www.sec.gov/Archives/edgar/data/1819974/000119312521112378/d26688ds1a.htm).
  First amendment to the IPO registration statement, with the same Cypress history. Its exhibit index adds Amendment No. 1 (2020-03-19) and Amendment No. 2 (2020-04-16) to the Process Technology License Agreement between Cypress Semiconductor Corporation and SkyWater Technology Foundry (formerly Cypress Semiconductor (Minnesota) Inc.), and lists the management fee agreement with Oxbow. It contains Deloitte & Touche LLP's audit report on CMI Acquisition, LLC. "Amendment No. 1 to the Process Technology License Agreement, dated as of March 19, 2020, by and between Cypress Semiconductor Corporation and SkyWater Technology Foundry, Inc. (f/k/a Cypress Semiconductor (Minnesota) Inc.)" (Exhibit index, exhibit 10.7); "We became an independent company in March 2017 when we were acquired by Oxbow Industries, LLC, or Oxbow, as part of a divestiture from Cypress." (Prospectus Summary)
  Auditor: Deloitte & Touche LLP, 2021-03-22: "/s/ Deloitte & Touche LLP Minneapolis, Minnesota March 22, 2021".
  Relationships: {ref}`SkyWater's 2021 initial public offering <filings-rel-skywater-ipo>` · {ref}`SkyWater describes the fab's Cypress origin <filings-rel-skywater-fab-history>` · {ref}`the 2017 Process Technology License Agreement and its amendments <filings-rel-cypress-technology-license>` · {ref}`Oxbow ownership, management fees and property transactions <filings-rel-oxbow-related-party>`.
  Inventory: SEC-01.
  Related pages: {ref}`machines-index` — The machines index cites the S-1 and its amendment together as SEC-01.

(filing-skywater-424b4-2021-04-22)=
* **SkyWater Technology, Inc. — Final prospectus for the initial public offering of 6,960,000 shares of common stock** (filed 2021-04-22; SEC accession 0001193125-21-126725).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000119312521126725/d26688d424b4.htm) · [Wayback copy](https://web.archive.org/web/20230805173604/https://www.sec.gov/Archives/edgar/data/1819974/000119312521126725/d26688d424b4.htm).
  The final IPO prospectus (registration nos. 333-254580 and 333-255385). It repeats the Cypress captive-fab history and the 2017 S130 IP licence, and names Infineon as Cypress's acquirer when giving Cypress's share of revenue. "Cypress, which was acquired in April 2020 by Infineon Technologies AG, accounted for approximately 29% and 48% of our revenue for the fiscal years ended January 3, 2021 and December 29, 2019, respectively." (Risk Factors); "This is our initial public offering." (Cover page)
  Relationships: {ref}`SkyWater's 2021 initial public offering <filings-rel-skywater-ipo>` · {ref}`SkyWater describes the fab's Cypress origin <filings-rel-skywater-fab-history>` · {ref}`Cypress (later Infineon) as SkyWater's wafer customer under the foundry services agreement <filings-rel-cypress-foundry-services>` · {ref}`the 2017 Process Technology License Agreement and its amendments <filings-rel-cypress-technology-license>`.
  Inventory: SEC-01.
  Related pages: {ref}`materials-index` — The materials index cites the S-1 family, including the final prospectus, as SEC-01.

(filing-skywater-10-q-2021-05-19)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2021-04-04** (filed 2021-05-19; SEC accession 0001193125-21-166596).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000119312521166596/d155085d10q.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/39e36151-3d18-495a-af24-8fc05f5e7b7a.pdf).
  SkyWater's first quarterly report as a public company, covering the quarter that ended two days after its IPO. It already discloses that disclosure controls and procedures were not effective because of material weaknesses, and describes the Oxbow management fee agreement dating from the 2017 divestiture from Cypress. "our disclosure controls and procedures were not effective as of April 4, 2021 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures); "Oxbow Industries, LLC ("Oxbow"), our principal owner, provides management and financial consulting services to us for an annual management fee not to exceed \$700" (Notes to the condensed consolidated financial statements, Related Party Transactions)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>` · {ref}`Oxbow ownership, management fees and property transactions <filings-rel-oxbow-related-party>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-skywater-10-q-2021-08-04)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2021-07-04** (filed 2021-08-04; SEC accession 0001819974-21-000012).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997421000012/0001819974-21-000012-index.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/69fd7163-93f6-4597-843a-c4f7f73d8b61.pdf).
  SkyWater's second quarterly report as a public company. It discloses that disclosure controls and procedures were not effective as of the quarter end because of material weaknesses in internal control over financial reporting, and gives customer-concentration data for accounts receivable. "our disclosure controls and procedures were not effective as of July 4, 2021 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures); "We had four major customers that accounted for 26%, 19%, 10% and 10% of outstanding trade accounts receivable as of July 4, 2021" (Notes to the condensed consolidated financial statements, Major Customers and Concentration Risk)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>` · {ref}`SkyWater names its customers <filings-rel-skywater-customers>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-weebit-nano-announcement-2021-09-09)=
* **Weebit Nano Limited — Weebit signs first commercial deal to take its ReRAM technology to volume production with US-based SkyWater** (filed 2021-09-09).
  [Original](https://www.weebit-nano.com/wp-content/uploads/2021/09/2262984_ASX_Weebit-Nano-signs-first-commercial-deal-to-take-its-ReRAM-technology-to-volume-production-with-US-based-SkyWater.pdf).
  Weebit Nano's original 2021 announcement of its ReRAM licensing agreement with SkyWater, made before the technology was qualified in S130 (see the 2023 follow-up announcement); it names SkyWater's Minnesota fab as the manufacturing site and the 130 nm PDK as the target process. "SkyWater intends to add Weebit's qualified memory module (and later additional variants of it) to its 130nm Process Design Kit (PDK)" (First page); "The technology licensing agreement is for SkyWater to manufacture designs from customers worldwide in their Minnesota fab" (page 2)
  Relationships: {ref}`a technology partner's filing names SkyWater <filings-rel-partner-names-skywater>`.
  Related pages: {ref}`overview-sky130b-reram` — The announcement is the partner's own record of the original 2021 agreement that led to the ReRAM qualification the page discusses.

(filing-skywater-10-q-2021-11-08)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2021-10-03** (filed 2021-11-08; SEC accession 0001819974-21-000020).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997421000020/0001819974-21-000020-index.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/f1e9cf45-ca6b-4a94-a570-32de7363558e.pdf).
  SkyWater's third quarterly report as a public company, again disclosing that controls and procedures were not effective as of the quarter end due to material weaknesses, and giving customer-concentration data. "our disclosure controls and procedures were not effective as of October 3, 2021 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures); "We had four major customers that accounted for 19%, 16%, 12% and 10% of outstanding trade accounts receivable as of October 3, 2021" (Notes to the condensed consolidated financial statements, Major Customers and Concentration Risk)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>` · {ref}`SkyWater names its customers <filings-rel-skywater-customers>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-infineon-annual-report-fy2021)=
* **Infineon Technologies AG — Infineon Technologies Annual Report 2021** (filed 2021-11-25).
  [Original](https://www.infineon.com/dgdl/Infineon+Annual+Report+2021.pdf?fileId=8ac78c8b7d507352017d622b5bfb0161).
  Infineon's second annual report after closing the Cypress acquisition. The CEO's letter says the integration of Cypress increased Infineon's system-solutions expertise, and the management report attributes part of the year's revenue shortfall to a winter storm at the Austin, Texas site (the former Cypress fab, later sold to SkyWater as Fab 25). "With Cypress, we have significantly increased our expertise in system solutions, especially with regard to the IoT." (Introductory section); "the aftermath of the winter storm in Austin (Texas, USA) held down revenue growth" (Combined management report)
  Auditor: KPMG AG Wirtschaftsprüfungsgesellschaft, 2021-11-25: "Munich, 25 November 2021 KPMG AG Wirtschaftsprüfungsgesellschaft".
  Relationships: {ref}`Infineon's acquisition of Cypress (2019-2020) <filings-rel-infineon-cypress-acquisition>`.
  Related pages: {ref}`overview-index` — The report continues Infineon's account of integrating Cypress, including the Austin site later sold to SkyWater.
  Note: filed gives the latest signature date printed in the report (Neubiberg, 25 November 2021); the publication date was not retrieved.

(filing-skywater-10-k-2022-03-10)=
* **SkyWater Technology, Inc. — Annual report on Form 10-K for the fiscal year ended 2022-01-02** (filed 2022-03-10; SEC accession 0001819974-22-000013).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997422000013/skyt-20220102.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/16ff78f5-a540-4c2e-9a6b-f9b923443e02.pdf).
  SkyWater's first annual report after the IPO. It repeats the Cypress captive-fab history, the Oxbow acquisition and the 2017 S130 IP licence, names Infineon among its customers, and says Cypress was acquired by Infineon in April 2020. "Cypress was acquired in April 2020 by Infineon Technologies AG, or Infineon." (Item 1, Business); "Our Advanced Technology Services and Wafer Services customers include Infineon, D-Wave, L3Harris, Leonardo DRS, MGI, Rockley Photonics and Steifpower." (Item 1, Business)
  Auditor: Deloitte & Touche LLP, 2022-03-09: "/s/ DELOITTE & TOUCHE LLP Minneapolis, Minnesota March 9, 2022".
  Relationships: {ref}`SkyWater describes the fab's Cypress origin <filings-rel-skywater-fab-history>` · {ref}`the 2017 Process Technology License Agreement and its amendments <filings-rel-cypress-technology-license>` · {ref}`Cypress (later Infineon) as SkyWater's wafer customer under the foundry services agreement <filings-rel-cypress-foundry-services>` · {ref}`SkyWater names its customers <filings-rel-skywater-customers>` · {ref}`Oxbow ownership, management fees and property transactions <filings-rel-oxbow-related-party>`.
  Related pages: {ref}`overview-index` — The overview's history of the fab is restated in this annual report's business section.

(filing-d-wave-s-4-2022-03-15)=
* **D-Wave Quantum Inc. — Form S-4 registration statement for the business combination of D-Wave Systems and DPCM Capital** (filed 2022-03-15; investor-relations filing 15660313; SEC accession not retrieved).
  [Original](https://ir.dwavequantum.com/financials/sec-filings/sec-filings-details/default.aspx?FilingId=15660313) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001907982/ab041b6c-cbb7-46ac-ad70-9bb9e2d6754e.pdf).
  D-Wave's registration statement for its listing. The filing includes an amendment to its 2012 Agreement for Semiconductor Line Operation that records Cypress's assignment of the agreement to SkyWater Technology Foundry in 2017. "On September 30, 2017, Cypress assigned the 2012 Agreement to SkyWater Technology Foundry, Inc. ("SkyWater"), which assignment D-Wave consented to on November 9, 2017" (Exhibit, amendment to the Agreement for Semiconductor Line Operation (recitals))
  Relationships: {ref}`a customer's filing names SkyWater <filings-rel-customer-names-skywater>` · {ref}`Cypress selling wafer-line capacity to outside customers before the 2017 sale <filings-rel-cypress-third-party-foundry>`.
  Related pages: {ref}`overview-index` — The agreement shows a Cypress wafer-line contract with an outside customer passing to SkyWater after the 2017 sale.

(filing-skywater-8-k-2022-04-04)=
* **SkyWater Technology, Inc. — Current report, item 1.01: Frame Agreement for the Purchase of Wafers and Services with Infineon** (filed 2022-04-04; SEC accession 0001819974-22-000015).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997422000015/skyt-20220329.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/b783ce86-6080-43b7-acf9-ba70ac32097b.pdf).
  Period: event of 2022-03-29.
  SkyWater Technology Foundry entered into a frame agreement with Infineon for the manufacture and delivery of wafers and foundry services, with an initial four-year term; the agreement is filed as an exhibit. "entered into a Frame Agreement for the Purchase of Wafers and Services (the "Frame Agreement") with Infineon Technologies AG ("Infineon")" (Item 1.01); "The Frame Agreement has an initial four year term" (Item 1.01)
  Relationships: {ref}`Infineon as SkyWater's wafer customer (2022 frame agreement, Fab 25 supply agreement) <filings-rel-infineon-wafer-supply>` · {ref}`Cypress (later Infineon) as SkyWater's wafer customer under the foundry services agreement <filings-rel-cypress-foundry-services>`.
  Related pages: {ref}`overview-index` — The agreement continues the Cypress-era wafer supply that the overview describes in the fab's history.

(filing-skywater-def-14a-2022-04-19)=
* **SkyWater Technology, Inc. — Definitive proxy statement for the 2022 annual meeting of stockholders** (filed 2022-04-19; SEC accession 0001140361-22-015022).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000114036122015022/ny20002114x1_def14a.htm) · [Wayback copy](https://web.archive.org/web/20250403124257/https://www.sec.gov/Archives/edgar/data/1819974/000114036122015022/ny20002114x1_def14a.htm).
  SkyWater's first proxy statement. Its related-party section describes the management fee agreement with Oxbow entered into at the 2017 divestiture from Cypress, and the 2020 sale of the Bloomington office and manufacturing facility (2401 and 2411 East 86th Street) to Oxbow Realty Partners for \$39 million. "In connection with our divestiture from Cypress Semiconductor Corporation on March 1, 2017, our wholly-owned subsidiary, SkyWater Technology Foundry, entered into a management fee agreement with Oxbow" (Certain Relationships and Related Party Transactions); "we sold our property, consisting of our office and manufacturing facility, located at 2401 and 2411 East 86th Street, in Bloomington, Minnesota, to Oxbow Realty for a purchase price of \$39 million" (Certain Relationships and Related Party Transactions)
  Relationships: {ref}`Oxbow ownership, management fees and property transactions <filings-rel-oxbow-related-party>` · {ref}`sale of the Minnesota fab subsidiary to SkyWater's owners (2017) <filings-rel-cypress-fab-sale>`.
  Related pages: {ref}`overview-index` — The overview's account of the fab's ownership is complemented by the proxy's description of the 2020 sale-leaseback of the Bloomington site.

(filing-skywater-10-q-2022-05-18)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2022-04-03** (filed 2022-05-18; SEC accession 0001819974-22-000021).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997422000021/0001819974-22-000021-index.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/7b98390b-a523-4439-9fa5-10dc62321af2.pdf).
  First-quarter fiscal 2022 report; discloses continuing material weaknesses in internal control over financial reporting and gives customer-concentration data for receivables. "our disclosure controls and procedures were not effective as of April 3, 2022 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures); "We had two major customers that accounted for 33% and 29% of outstanding trade accounts receivable as of April 3, 2022" (Notes to the condensed consolidated financial statements, Major Customers and Concentration Risk)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>` · {ref}`SkyWater names its customers <filings-rel-skywater-customers>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-skywater-10-q-2022-08-17)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2022-07-03** (filed 2022-08-17; SEC accession 0001819974-22-000069).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997422000069/0001819974-22-000069-index.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/95b788aa-d2d5-4446-8c51-c192dde6015d.pdf).
  Second-quarter fiscal 2022 report; discloses that disclosure controls and procedures remained not effective as of the quarter end because of material weaknesses in internal control over financial reporting. "our disclosure controls and procedures were not effective as of July 3, 2022 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-skywater-10-q-2022-11-10)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2022-10-02** (filed 2022-11-10; SEC accession 0001819974-22-000085).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997422000085/0001819974-22-000085-index.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/479a15ab-361b-438c-ac9f-0e54825bcf26.pdf).
  Third-quarter fiscal 2022 report; discloses that disclosure controls and procedures remained not effective as of the quarter end because of material weaknesses in internal control over financial reporting, and gives the size of SkyWater's two DoD rad-hard manufacturing awards. "our disclosure controls and procedures were not effective as of October 2, 2022 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures); "In September 2019, we entered into a contract with the DoD to receive up to \$170 million to expand and upgrade our manufacturing capabilities, specifically to build next-generation rad-hard wafer solutions" (Part I, Item 2, Overview)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>` · {ref}`investment and government funding for the Minnesota fab <filings-rel-minnesota-fab-investment>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.
  Note: The same quarter's MD&A also states: "In September 2022, the DoD awarded us up to an additional \$99 million as a continuation of the previous initiative to broaden onshore production capabilities for strategic rad-hard electronics" (not quoted verbatim above to stay within the two-quote limit).

(filing-infineon-annual-report-fy2022)=
* **Infineon Technologies AG — Infineon Technologies Annual Report 2022** (filed 2022-11-25).
  [Original](https://www.infineon.com/assets/row/public/documents/corporate/investors/annual-reports/2022/infineon-annual-report-report-v12-00-en.pdf).
  Infineon's annual report crediting outgoing Chief Marketing Officer Helmut Gassel's contribution to the acquisition and integration of Cypress, and recording that Austin, Texas manufacturing (the former Cypress fab) moved to renewable electricity during the year. "he made a decisive contribution to the successful acquisition and integration of Cypress and accelerated the digitalization of sales and marketing" (Introductory section)
  Auditor: KPMG AG Wirtschaftsprüfungsgesellschaft, 2022-11-25: "Munich, 25 November 2022 KPMG AG Wirtschaftsprüfungsgesellschaft".
  Relationships: {ref}`Infineon's acquisition of Cypress (2019-2020) <filings-rel-infineon-cypress-acquisition>`.
  Related pages: {ref}`overview-index` — The report continues Infineon's account of integrating Cypress, including the Austin site later sold to SkyWater.
  Note: filed gives the latest signature date printed in the report (Neubiberg, 25 November 2022; an earlier statement in the same report is dated 21 November 2022); the publication date was not retrieved.

(filing-d-wave-8-k-2023-03-03)=
* **D-Wave Quantum Inc. — Current report: Thirteenth Amendment to the Agreement for Semiconductor Line Operation with SkyWater Technology Foundry** (filed 2023-03-03; investor-relations filing 16461334; SEC accession not retrieved).
  [Original](https://ir.dwavequantum.com/financials/sec-filings/sec-filings-details/default.aspx?FilingId=16461334) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001907982/50391077-e63b-41de-b592-5e0f37ea99fe.pdf).
  Period: event of 2023-03-01.
  D-Wave files the Thirteenth Amendment (2023-03-01) to its 2012 semiconductor line operation agreement, originally with Cypress and assigned to SkyWater Technology Foundry, revising SkyWater's activity billing rates. "Thirteenth Amendment, dated March 1, 2023, between D-Wave Systems Inc. and SkyWater Technology Foundry, Inc. to the Agreement for Semiconductor Line Operation, dated as of December 23, 2012, by and between Cypress Semiconductor Corporation and D-Wave Systems Inc." (Item 9.01, exhibit 10.1); "to address the SkyWater's revised Activity Billing rates as of January 2022" (Exhibit 10.1, recitals)
  Relationships: {ref}`a customer's filing names SkyWater <filings-rel-customer-names-skywater>` · {ref}`Cypress selling wafer-line capacity to outside customers before the 2017 sale <filings-rel-cypress-third-party-foundry>`.
  Related pages: {ref}`overview-index` — The exhibit is a public contract between SkyWater and a foundry customer inherited from Cypress.

(filing-skywater-10-k-2023-03-15)=
* **SkyWater Technology, Inc. — Annual report on Form 10-K for the fiscal year ended 2023-01-01** (filed 2023-03-15; SEC accession 0001819974-23-000011).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997423000011/skyt-20230101.htm) · [Wayback copy](https://web.archive.org/web/20230329202011/https://www.sec.gov/Archives/edgar/data/1819974/000181997423000011/skyt-20230101.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/0a7f9a2c-fc5a-4db4-8cff-85ff40d93adf.pdf).
  Annual report for fiscal 2022. It gives Infineon's share of revenue (28 % in 2022, 25 % in 2021), names Infineon first among its customers and repeats the Cypress history and S130 licence. "Infineon accounted for 28% and 25% of our revenue for the years ended January 1, 2023 and January 2, 2022, respectively." (Item 1, Business, Our Customers); "Our Advanced Technology Services and Wafer Services customers include Infineon, D-Wave, L3Harris, and Leonardo DRS." (Item 1, Business)
  Auditor: Deloitte & Touche LLP, 2023-03-14: "/s/ DELOITTE & TOUCHE LLP Minneapolis, Minnesota March 14, 2023".
  Relationships: {ref}`SkyWater describes the fab's Cypress origin <filings-rel-skywater-fab-history>` · {ref}`Infineon as SkyWater's wafer customer (2022 frame agreement, Fab 25 supply agreement) <filings-rel-infineon-wafer-supply>` · {ref}`SkyWater names its customers <filings-rel-skywater-customers>` · {ref}`the 2017 Process Technology License Agreement and its amendments <filings-rel-cypress-technology-license>`.
  Related pages: {ref}`overview-index` — The overview's history of the fab is restated in this annual report's business section.

(filing-d-wave-10-k-2023-04-18)=
* **D-Wave Quantum Inc. — Annual report on Form 10-K for the fiscal year ended 2022-12-31** (filed 2023-04-18; investor-relations filing 16570514; SEC accession not retrieved).
  [Original](https://ir.dwavequantum.com/financials/sec-filings/sec-filings-details/default.aspx?FilingId=16570514) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001907982/f08a6a0c-2ea5-4a3f-bda0-4eb7769ed224.pdf).
  D-Wave's first 10-K. Its "Operation Agreements" section describes a 2006 agreement to buy capacity on a Cypress 8-inch wafer pilot line, the 2012 Semiconductor Line Operation Agreement, and Cypress's 2017 assignment of that agreement to SkyWater Technology Foundry. "On July 31, 2006, we entered into an agreement with Cypress Semiconductor Corporation ("Cypress") for the purchase of available capacity of Cypress' 8" wafer pilot line" (Item 1, Business, Operation Agreements); "On September 30, 2017, Cypress assigned the Semiconductor Line Operation Agreement to SkyWater Technology Foundry, Inc., to which we consented on November 9, 2017." (Item 1, Business, Operation Agreements)
  Auditor: PricewaterhouseCoopers LLP, 2023-04-18: "/s/ PricewaterhouseCoopers LLP Chartered Professional Accountants Vancouver, Canada April 18, 2023 We have served as the Company's auditor since 2010.".
  Relationships: {ref}`a customer's filing names SkyWater <filings-rel-customer-names-skywater>` · {ref}`Cypress selling wafer-line capacity to outside customers before the 2017 sale <filings-rel-cypress-third-party-foundry>`.
  Related pages: {ref}`overview-index` — The report shows Cypress selling wafer-line capacity to an outside customer from 2006, before the fab became a foundry.

(filing-skywater-def-14a-2023-04-25)=
* **SkyWater Technology, Inc. — Definitive proxy statement for the 2023 annual meeting of stockholders** (filed 2023-04-25; SEC accession 0001140361-23-020146).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000114036123020146/ny20006439x1_def14a.htm) · [Wayback copy](https://web.archive.org/web/20230502184124/https://www.sec.gov/Archives/edgar/data/1819974/000114036123020146/ny20006439x1_def14a.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/212963f3-8d41-40a9-b748-88ad1f583d42.pdf).
  The 2023 proxy statement's related-party section gives CMI Oxbow's ownership share and the 2020 sale-leaseback of the Bloomington land and building to Oxbow Realty, including the fiscal 2022 lease payment and the future minimum payments outstanding. "On September 29, 2020, we entered into an agreement to sell the land and building representing our primary operating location in Bloomington, Minnesota to an Oxbow Realty Partners, LLC ("Oxbow Realty"), an affiliate of our principal stockholder, CMI Oxbow" (Certain Relationships and Transactions with Related Persons, Sale Leaseback Transaction with Oxbow Realty); "CMI Oxbow Partners, LLC ("CMI Oxbow"), an affiliate of Oxbow, owns approximately 44.56% of our outstanding common stock as of the Record Date" (Certain Relationships and Transactions with Related Persons)
  Relationships: {ref}`Oxbow ownership, management fees and property transactions <filings-rel-oxbow-related-party>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-skywater-10-q-2023-05-12)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2023-04-02** (filed 2023-05-12; SEC accession 0001819974-23-000022).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997423000022/skyt-20230402.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/a2d39029-ae99-4c82-aeb0-79d99808961c.pdf).
  First-quarter fiscal 2023 report. Its Item 4 evaluation date reads "April 3, 2022" rather than the quarter's own end date of April 2, 2023, an internal dating inconsistency in the filed document; the material weaknesses it describes are the same ones reported each quarter. "our disclosure controls and procedures were not effective as of April 3, 2022 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.
  Note: The evaluation date in Item 4 ("April 3, 2022") does not match the cover page's quarterly period ended April 2, 2023, or the filing date; the apparent copy-paste error is quoted verbatim rather than corrected here.

(filing-weebit-nano-announcement-2023-06-29)=
* **Weebit Nano Limited — WBT's ReRAM IP now fully qualified in SkyWater S130 process** (filed 2023-06-29).
  [Original](https://investors.weebit-nano.com/site/pdf/d613063e-b334-434d-b33a-d120ca071bd9/WBTs-ReRAM-IP-now-fully-qualified-in-SkyWater-S130-process.pdf).
  Weebit Nano's market announcement, issued jointly with SkyWater, that its ReRAM IP was fully qualified for industrial temperatures in SkyWater's 130 nm CMOS (S130) process, using demo chips SkyWater produced. "confirm Weebit Resistive Random-Access Memory (ReRAM) IP has been fully qualified for industrial temperatures employing SkyWater's 130nm CMOS (S130) process" (First paragraph); "The qualification used demo chips produced by SkyWater which integrate Weebit ReRAM IP." (Second paragraph)
  Relationships: {ref}`a technology partner's filing names SkyWater <filings-rel-partner-names-skywater>`.
  Related pages: {ref}`overview-sky130b-reram` — The announcement is the partner's own record of qualifying its ReRAM in the S130 process that the ReRAM page discusses.

(filing-skywater-8-k-2023-08-04)=
* **SkyWater Technology, Inc. — Current report, item 1.01: Consulting Agreement with Oxbow Industries** (filed 2023-08-04; SEC accession 0001193125-23-203313).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000119312523203313/d494973d8k.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/421c650f-42bd-48c1-a73a-87ca4096994e.pdf).
  Period: event of 2023-08-01.
  SkyWater Technology Foundry engaged Oxbow Industries (an affiliate of which acquired the business from Cypress in 2017) to provide an employee as a consultant on fab operations (efficiency, lot velocity and wafer-services loading). "entered into a Consulting Agreement (the "Consulting Agreement") with Oxbow Industries, LLC ("Oxbow")" (Item 1.01); "evaluating and implementing changes to fab operations to improve fab efficiency and lot velocity" (Item 1.01)
  Relationships: {ref}`Oxbow ownership, management fees and property transactions <filings-rel-oxbow-related-party>`.
  Related pages: {ref}`machines-index` — The filing is one of the few public statements about how the Minnesota fab's operations were managed after the Cypress era.

(filing-skywater-10-q-2023-08-11)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2023-07-02** (filed 2023-08-11; SEC accession 0001819974-23-000059).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997423000059/skyt-20230702.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/43a7c607-bf24-4451-a832-4e5cff8c5478.pdf).
  Second-quarter fiscal 2023 report; discloses that disclosure controls and procedures remained not effective as of the quarter end because of material weaknesses in internal control over financial reporting. "our disclosure controls and procedures were not effective as of July 2, 2023 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-weebit-nano-annual-report-fy2023)=
* **Weebit Nano Limited — Appendix 4E and Annual Report for the year ended 30 June 2023** (filed 2023-08-25).
  [Original](https://investors.weebit-nano.com/site/pdf/6036278c-d1ec-4ecf-be9c-dc8ba1e945a9/Appendix-4E-and-Annual-Report.pdf).
  Weebit Nano's FY2023 annual report says its embedded ReRAM IP is commercially available in SkyWater's 130 nm CMOS process, lists full qualification in S130 among the year's highlights and calls SkyWater a partner instrumental to its progress. "Our proven embedded ReRAM intellectual property (IP) is now commercially available in SkyWater Technology's 130nm CMOS process" (Introductory section); "Weebit ReRAM fully qualified in SkyWater S130 process" (2022-2023 highlights)
  Auditor: Nexia Perth Audit Services Pty Ltd, 2023-08-24: "Nexia Perth Audit Services Pty Ltd M. Janse Van Nieuwenhuizen Director Perth 24 August 2023".
  Relationships: {ref}`a technology partner's filing names SkyWater <filings-rel-partner-names-skywater>`.
  Related pages: {ref}`overview-sky130b-reram` — The report describes the commercial status of the ReRAM IP offered in SkyWater's S130 process.

(filing-skywater-10-q-2023-11-09)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2023-10-01** (filed 2023-11-09; SEC accession 0001819974-23-000117).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997423000117/skyt-20231001.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/8634d45f-b73c-446c-a319-5ff48d9ade21.pdf).
  Third-quarter fiscal 2023 report; discloses that disclosure controls and procedures remained not effective as of the quarter end because of material weaknesses in internal control over financial reporting. "our disclosure controls and procedures were not effective as of October 1, 2023 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-infineon-annual-report-fy2023)=
* **Infineon Technologies AG — Infineon Technologies Annual Report 2023** (filed 2023-11-23).
  [Original](https://www.infineon.com/assets/row/public/documents/corporate/investors/annual-reports/2023/2023-infineon-annual-report-v01-00-en.pdf).
  Infineon's annual report lists the Cypress acquisition, alongside Industrial Analytics and Imagimob, among the strategic acquisitions behind its software ecosystem, and records a PFC-abatement project launched during the year at the Austin, Texas site (the former Cypress fab). "through our own organic growth and strategic partnerships, as well as through the acquisitions of Cypress, Industrial Analytics and Imagimob" (Combined management report, Group strategy)
  Auditor: KPMG AG Wirtschaftsprüfungsgesellschaft, 2023-11-23: "Munich, 23 November 2023 KPMG AG Wirtschaftsprüfungsgesellschaft".
  Relationships: {ref}`Infineon's acquisition of Cypress (2019-2020) <filings-rel-infineon-cypress-acquisition>`.
  Related pages: {ref}`overview-index` — The report continues Infineon's account of integrating Cypress, including the Austin site later sold to SkyWater.
  Note: filed gives the latest signature date printed in the report (Neubiberg, 23 November 2023; an earlier statement in the same report is dated 21 November 2023); the publication date was not retrieved.

(filing-skywater-10-k-2024-03-15)=
* **SkyWater Technology, Inc. — Annual report on Form 10-K for the fiscal year ended 2023-12-31** (filed 2024-03-15; SEC accession 0001819974-24-000008).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm) · [Wayback copy](https://web.archive.org/web/20240323004216/https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/0a08518f-8844-432d-b3dd-6a066589bb98.pdf).
  Annual report for fiscal 2023, cited on many pages as SEC-02 for the Minnesota fab's node range, facilities and supplier list. It says the S130 and S90 base design IP came from Cypress under the 2017 licence and gives Infineon's share of revenue (17 % in 2023). "the base design IP portfolio for S130 and S90 technologies originating from Cypress was licensed via a technology license agreement in 2017" (Item 1, Business); "Infineon accounted for 17% and 28% of our revenue for the fiscal years ended December 31, 2023 and January 1, 2023, respectively." (Item 1, Business, Our Customers)
  Auditor: Deloitte & Touche LLP, 2024-03-15: "/s/ DELOITTE & TOUCHE LLP Minneapolis, Minnesota March 15, 2024".
  Relationships: {ref}`SkyWater describes the fab's Cypress origin <filings-rel-skywater-fab-history>` · {ref}`the 2017 Process Technology License Agreement and its amendments <filings-rel-cypress-technology-license>` · {ref}`Infineon as SkyWater's wafer customer (2022 frame agreement, Fab 25 supply agreement) <filings-rel-infineon-wafer-supply>` · {ref}`SkyWater names its suppliers <filings-rel-skywater-suppliers>`.
  Inventory: SEC-02.
  Related pages: {ref}`overview-index` — The process overview cites the annual report as SEC-02 for the Minnesota fab's node range.; {ref}`machines-index` — The machines index cites SEC-02 for the fab's capabilities.; {ref}`materials-index` — The materials index cites SEC-02 for the updated supplier list.

(filing-quicklogic-10-k-2024-03-27)=
* **QuickLogic Corporation — Annual report on Form 10-K for the fiscal year ended 2023-12-31** (filed 2024-03-27; SEC accession 0001437749-24-009469).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/882508/000143774924009469/quicklo20231127_10k.htm) · [investor-relations copy](https://ir.quicklogic.com/sec-filings/content/0001437749-24-009469/0001437749-24-009469.pdf).
  QuickLogic's FY2023 10-K names SkyWater (spelled "SkyWater Technologies" in the filing) among the foundries it depends on to manufacture its hardware products, alongside GlobalFoundries and TSMC; QuickLogic's own FY2022 10-K, filed a year earlier, does not mention SkyWater at all. "We depend upon GlobalFoundries, TSMC, SkyWater Technologies, Honeywell Aerospace, Amkor Technology, Inc., Integra Specialty Products, JCET Group Co. Ltd., and Golden Altos Corp. to manufacture our new hardware products" (Item 1A, Risk Factors)
  Auditor: Moss Adams LLP, 2024-03-26: "/s/ Moss Adams LLP San Francisco, California March 26, 2024 We have served as the Company’s auditor since 2016.".
  Relationships: {ref}`a customer's filing names SkyWater <filings-rel-customer-names-skywater>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.
  Note: QuickLogic's prior 10-K (FY2022, accession 0001437749-23-008214, filed 2023) was fetched and grepped for "SkyWater" with zero matches, even though QuickLogic's March 2022 press releases name the RH90 rad-hard eFPGA partnership; this FY2023 10-K is the first of QuickLogic's own annual reports found to name SkyWater.

(filing-d-wave-10-k-2024-03-29)=
* **D-Wave Quantum Inc. — Annual report on Form 10-K for the fiscal year ended 2023-12-31** (filed 2024-03-29; investor-relations filing 17413336; SEC accession not retrieved).
  [Original](https://ir.dwavequantum.com/financials/sec-filings/sec-filings-details/default.aspx?FilingId=17413336) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001907982/eb4559fa-d0e8-4374-8651-901c2dbd7e29.pdf).
  D-Wave's fiscal 2023 10-K, which repeats the operation-agreement history and files the Fourteenth Amendment (2023-12-26) with SkyWater Technology Foundry as an exhibit. "Fourteenth Amendment, dated December 26, 2023, between D-Wave Systems Inc. and SkyWater Technology Foundry, Inc. to the Agreement for Semiconductor Line Operation" (Item 15, exhibit 10.65); "On September 30, 2017, Cypress assigned the Semiconductor Line Operation Agreement to SkyWater Technology Foundry, Inc., to which we consented on November 9, 2017." (Item 1, Business, Operation Agreements)
  Auditor: Grant Thornton LLP, 2024-03-29: "/s/ GRANT THORNTON LLP We have served as the Company’s auditor since 2023. Bellevue, Washington March 29, 2024".
  Relationships: {ref}`a customer's filing names SkyWater <filings-rel-customer-names-skywater>`.
  Related pages: {ref}`overview-index` — The report keeps the SkyWater line-operation agreement inherited from Cypress on the public record.

(filing-skywater-def-14a-2024-04-10)=
* **SkyWater Technology, Inc. — Definitive proxy statement for the 2024 annual meeting of stockholders** (filed 2024-04-10; SEC accession 0001140361-24-019075).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000114036124019075/ny20018380x1_def14a.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/b7768f8c-19df-4a51-8d52-e198a9f786cc.pdf).
  The 2024 proxy statement repeats the Oxbow Realty sale-leaseback of the Bloomington fab site, updates the fiscal 2023 lease payment and outstanding balance, and shows CMI Oxbow's ownership share falling as SkyWater's public float grew. "In fiscal 2023, we paid \$4.9 million to Oxbow Realty pursuant to the lease agreement. Future contractual payments to Oxbow Realty as of December 31, 2023 were \$98.7 million" (Certain Relationships and Transactions with Related Persons, Sale Leaseback Transaction with Oxbow Realty); "CMI Oxbow Partners, LLC ("CMI Oxbow"), an affiliate of Oxbow, beneficially owns approximately 27.51% of our outstanding common stock as of the Record Date" (Certain Relationships and Transactions with Related Persons)
  Relationships: {ref}`Oxbow ownership, management fees and property transactions <filings-rel-oxbow-related-party>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-skywater-10-q-2024-05-10)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2024-03-31** (filed 2024-05-10; SEC accession 0001819974-24-000014).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997424000014/skyt-20240331.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/ddf436d3-a775-425d-befc-43d190489d7a.pdf).
  First-quarter fiscal 2024 report, filed a few weeks after the June 2024 auditor change was set in motion; discloses that disclosure controls and procedures remained not effective as of the quarter end because of material weaknesses in internal control over financial reporting. "our disclosure controls and procedures were not effective as of March 31, 2024 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-skywater-10-q-2024-08-07)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2024-06-30** (filed 2024-08-07; SEC accession 0001819974-24-000028).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997424000028/skyt-20240630.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/48b19fa6-fd36-4c34-9b56-e798e9b019d3.pdf).
  Second-quarter fiscal 2024 report, the first quarterly report after the June 2024 change of auditor to KPMG LLP; discloses that disclosure controls and procedures remained not effective as of the quarter end because of material weaknesses in internal control over financial reporting. "our disclosure controls and procedures were not effective as of June 30, 2024 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-weebit-nano-annual-report-fy2024)=
* **Weebit Nano Limited — Appendix 4E and 2024 Annual Report for the year ended 30 June 2024** (filed 2024-08-28).
  [Original](https://investors.weebit-nano.com/site/pdf/ff240513-07ab-46f3-a651-17a5cb22204b/Appendix-4E-and-2024-Annual-Report.pdf).
  Weebit Nano's FY2024 annual report lists qualification at 125 °C in SkyWater S130 among its highlights and says missing IP in SkyWater's foundry offering delayed licensing agreements with companies wanting to manufacture at SkyWater. "Factors beyond our control, such as missing IPs in SkyWater's foundry offering, have delayed licensing agreements with product companies wanting to manufacture at SkyWater" (Introductory section); "Weebit ReRAM qualified 125⁰C in SkyWater S130" (Highlights)
  Auditor: Nexia Perth Audit Services Pty Ltd, 2024-08-27: "Nexia Perth Audit Services Pty Ltd Michael Fay Director Perth, Western Australia 27 August 2024".
  Relationships: {ref}`a technology partner's filing names SkyWater <filings-rel-partner-names-skywater>`.
  Related pages: {ref}`overview-sky130b-reram` — The report gives the partner's view of adoption of the ReRAM IP in SkyWater's S130 process.

(filing-skywater-10-q-2024-11-07)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2024-09-29** (filed 2024-11-07; SEC accession 0001819974-24-000040).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997424000040/skyt-20240929.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/dd08d284-e824-44ac-b520-1b11565ad93d.pdf).
  Third-quarter fiscal 2024 report; discloses that disclosure controls and procedures remained not effective as of the quarter end because of material weaknesses in internal control over financial reporting. "our disclosure controls and procedures were not effective as of September 29, 2024 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-infineon-annual-report-fy2024)=
* **Infineon Technologies AG — Infineon Technologies Annual Report 2024** (filed 2024-11-26).
  [Original](https://www.infineon.com/dgdl/Infineon+Annual+Report+2024.pdf?fileId=8ac78c8b92bced620193694bfb970095).
  Infineon's last annual report before agreeing to sell its Austin, Texas fab (the former Cypress fab) to SkyWater. It repeats, in the same wording as the 2023 report, that the Cypress acquisition contributed to its software ecosystem, and lists Austin among its manufacturing sites. "through our own organic growth and strategic partnerships, as well as through the acquisitions of Cypress, Industrial Analytics and Imagimob" (Combined management report, Group strategy)
  Auditor: Deloitte GmbH Wirtschaftsprüfungsgesellschaft, 2024-11-26: "Munich/Germany, 26 November 2024 Deloitte GmbH Wirtschaftsprüfungsgesellschaft".
  Relationships: {ref}`Infineon's acquisition of Cypress (2019-2020) <filings-rel-infineon-cypress-acquisition>`.
  Related pages: {ref}`overview-index` — The report is Infineon's last annual account of the Austin site before agreeing, in 2025, to sell it to SkyWater.
  Note: filed gives the latest signature date printed in the report (Neubiberg, 26 November 2024; an earlier statement in the same report is dated 21 November 2024); the publication date was not retrieved.

(filing-skywater-8-k-2025-02-26)=
* **SkyWater Technology, Inc. — Current report, item 1.01: Membership Interest Purchase Agreement for Infineon's Austin fab** (filed 2025-02-26; SEC accession 0001819974-25-000007).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997425000007/0001819974-25-000007-index.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/f35511a4-f771-44da-9bda-5de8585580bd.pdf).
  Period: event of 2025-02-25.
  SkyWater agreed to buy, from Spansion LLC (an Infineon affiliate), a new company holding the assets and liabilities of Infineon's 200 mm fab in Austin, Texas, for about \$110 million, part of it payable through wafer credits under a wafer supply agreement with a seller affiliate. "entered into a Membership Interest Purchase Agreement (the "Purchase Agreement") with Spansion LLC ("Seller"), an affiliate of Infineon Technologies AG" (Item 1.01); "certain assets and liabilities related to Infineon Technologies AG's 200 mm fab in Austin, Texas (the "Transaction")" (Item 1.01)
  Relationships: {ref}`SkyWater's purchase of Infineon's Austin fab (Fab 25) <filings-rel-infineon-fab25-sale>` · {ref}`Infineon as SkyWater's wafer customer (2022 frame agreement, Fab 25 supply agreement) <filings-rel-infineon-wafer-supply>`.
  Related pages: {ref}`overview-index` — The purchase adds a second 200 mm fab to the company that runs the Minnesota fab the overview describes.

(filing-skywater-10-k-2025-03-14)=
* **SkyWater Technology, Inc. — Annual report on Form 10-K for the fiscal year ended 2024-12-29** (filed 2025-03-14; SEC accession 0001819974-25-000010).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997425000010/skyt-20241229.htm) · [Wayback copy](https://web.archive.org/web/20250319191155/https://www.sec.gov/Archives/edgar/data/1819974/000181997425000010/skyt-20241229.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/722e1c1f-52ff-40e9-9dfd-c16c31905edf.pdf).
  Annual report for fiscal 2024. It now gives the Cypress captive period as 26 years, repeats the S130 and S90 licence, and describes the pending purchase of Infineon's Austin fab (Fab 25) among its risk factors. First year audited by KPMG. "our Minnesota fab was owned and operated by Cypress Semiconductor Corporation ("Cypress"), as a captive manufacturing facility for 26 years" (Item 1, Business); "We may not realize the anticipated benefits of the agreement entered into with Infineon Technologies AG to purchase Fab 25 (the "Transaction")" (Risk factors summary)
  Auditor: KPMG LLP, 2025-03-14: "/s/ KPMG LLP We have served as the Company's auditor since 2024. Minneapolis, Minnesota March 14, 2025".
  Relationships: {ref}`SkyWater describes the fab's Cypress origin <filings-rel-skywater-fab-history>` · {ref}`the 2017 Process Technology License Agreement and its amendments <filings-rel-cypress-technology-license>` · {ref}`SkyWater's purchase of Infineon's Austin fab (Fab 25) <filings-rel-infineon-fab25-sale>`.
  Related pages: {ref}`overview-index` — The 26-year figure differs from the 20 years of the S-1 that the overview's history relies on.
  Note: This "26 years" figure disagrees with SkyWater's earlier IPO filings (skywater-drs-2020-08-12, skywater-s-1-2021-03-22), which gave the Cypress captive period as 20 years; 26 years (1991-2017) is the figure consistent with the fab's Control Data origin.

(filing-skywater-def-14a-2025-04-08)=
* **SkyWater Technology, Inc. — Definitive proxy statement for the 2025 annual meeting of stockholders** (filed 2025-04-08; SEC accession 0001140361-25-012823).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000114036125012823/ny20041354x1_def14a.htm) · [Wayback copy](https://web.archive.org/web/20250803205251/https://www.sec.gov/Archives/edgar/data/1819974/000114036125012823/ny20041354x1_def14a.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/f9865520-b380-4f31-9343-229aa9cf97ed.pdf).
  The 2025 proxy statement, filed shortly before the Fab 25 purchase agreement was announced, again repeats the Oxbow Realty sale-leaseback of the Bloomington site and shows CMI Oxbow's ownership share continuing to decline. "CMI Oxbow Partners, LLC ("CMI Oxbow"), an affiliate of Oxbow, beneficially owns approximately 23.23% of our outstanding common stock as of the Record Date" (Certain Relationships and Transactions with Related Persons)
  Relationships: {ref}`Oxbow ownership, management fees and property transactions <filings-rel-oxbow-related-party>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-skywater-10-q-2025-05-08)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2025-03-30** (filed 2025-05-08; SEC accession 0001819974-25-000018).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997425000018/skyt-20250330.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/571da460-02a1-4e04-bf37-124208325864.pdf).
  First-quarter fiscal 2025 report, filed while the Fab 25 (Austin) purchase from Infineon was pending; lists completing the acquisition among the risk factors and discloses that disclosure controls and procedures remained not effective because of a material weakness. "our disclosure controls and procedures were not effective as of March 30, 2025 due to the material weakness in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures); "our ability to complete our acquisition of Infineon's Fab 25 facility on anticipated timing and terms" (Part I, Item 2, forward-looking statements)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>` · {ref}`SkyWater's purchase of Infineon's Austin fab (Fab 25) <filings-rel-infineon-fab25-sale>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-skywater-8-k-2025-07-03)=
* **SkyWater Technology, Inc. — Current report, items 1.01, 2.01 and 2.03: completion of the Fab 25 acquisition** (filed 2025-07-03; SEC accession 0001193125-25-155467).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000119312525155467/d90812d8k.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/1b266a26-2e16-4886-80ee-7e7baab63f52.pdf).
  Period: event of 2025-06-30.
  SkyWater completed the purchase of Spansion Fab 25, LLC, holding substantially all of the property, plant, equipment and employees of Infineon's 200 mm Austin fab, on 2025-06-30 for about \$93 million in cash; an amendment removed the \$25 million payable at the end of the multi-year supply agreement. "On June 30, 2025, the Company and the Seller completed the Transaction in accordance with the terms and conditions of Purchase Agreement, as amended by the Amendment." (Item 2.01); "to eliminate the \$25 million payable at the conclusion of the multi-year supply agreement entered into in connection with the Transaction" (Item 1.01)
  Relationships: {ref}`SkyWater's purchase of Infineon's Austin fab (Fab 25) <filings-rel-infineon-fab25-sale>` · {ref}`Infineon as SkyWater's wafer customer (2022 frame agreement, Fab 25 supply agreement) <filings-rel-infineon-wafer-supply>`.
  Related pages: {ref}`overview-index` — The acquisition adds a second 200 mm fab to the company that runs the Minnesota fab the overview describes.

(filing-skywater-10-q-2025-08-07)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2025-06-29** (filed 2025-08-07; SEC accession 0001819974-25-000028).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997425000028/skyt-20250629.htm) · [Wayback copy](https://web.archive.org/web/20250811133256/https://www.sec.gov/Archives/edgar/data/1819974/000181997425000028/skyt-20250629.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/38837663-a163-4ef3-b631-bead9f54c8f2.pdf).
  The quarterly report covering the quarter in which the Fab 25 purchase closed; it reports the closing as a subsequent event financed through debt. "Subsequent to the end of the Company's second quarter, on June 30, 2025, the Company completed the Transaction." (Notes to the condensed consolidated financial statements, note 1); "The Company financed the purchase price for the Transaction through debt financing." (Notes to the condensed consolidated financial statements, note 1)
  Relationships: {ref}`SkyWater's purchase of Infineon's Austin fab (Fab 25) <filings-rel-infineon-fab25-sale>`.
  Related pages: {ref}`overview-index` — The report records the date on which the company running the Minnesota fab acquired the Austin fab.

(filing-skywater-8-k-a-2025-09-15)=
* **SkyWater Technology, Inc. — Amendment No. 1 to current report, item 9.01: financial statements of the Fab 25 Business of Infineon Technologies AG** (filed 2025-09-15; SEC accession 0001819974-25-000037).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997425000037/0001819974-25-000037-index.htm) · [Wayback copy](https://web.archive.org/web/20251014015221/https://www.sec.gov/Archives/edgar/data/1819974/000181997425000037/0001819974-25-000037-index.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/8d1da1bd-cbff-4677-b8bc-cb02f7d3d82a.pdf).
  Period: Fab 25 Business fiscal years ended 2023-09-30 and 2024-09-30.
  Files the audited combined abbreviated financial statements of the Fab 25 Business of Infineon Technologies AG (assets acquired and liabilities assumed; revenues and direct expenses) and pro forma combined information for the acquisition, with Deloitte & Touche's consent. "The audited Combined Abbreviated Financial Statements of the Fab 25 Business of Infineon Technologies" (Item 9.01(a)); "our report dated September 11, 2025, relating to the financial statements of the Fab 25 Business of Infineon Technologies AG" (Exhibit 23.1, consent of independent auditors)
  Auditor: Deloitte & Touche LLP, 2025-09-11: "/s/ Deloitte & Touche LLP San Jose, California September 15, 2025".
  Relationships: {ref}`SkyWater's purchase of Infineon's Austin fab (Fab 25) <filings-rel-infineon-fab25-sale>`.
  Related pages: {ref}`overview-index` — The statements give audited figures for the Austin fab that joined the Minnesota fab's owner in 2025.
  Amends/filed with: {ref}`full entry <filing-skywater-8-k-2025-07-03>`.

(filing-skywater-10-q-2025-11-12)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2025-09-28** (filed 2025-11-12; SEC accession 0001819974-25-000052).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997425000052/skyt-20250928.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/d24b279d-c983-4376-a089-7a960f374046.pdf).
  Third-quarter fiscal 2025 report, the first full quarter after the Fab 25 purchase closed; gives the Membership Interest Purchase Agreement structure (Spansion LLC selling Spansion Fab 25, LLC) and the purchase price, and discloses a continuing material weakness. "our disclosure controls and procedures were not effective as of September 28, 2025 due to the material weakness in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures); "pursuant to which the Company acquired all of the issued and outstanding membership interests of Spansion Fab 25, LLC ("Fab 25")" (Notes to the condensed consolidated financial statements, note 1)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>` · {ref}`SkyWater's purchase of Infineon's Austin fab (Fab 25) <filings-rel-infineon-fab25-sale>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-infineon-annual-report-fy2025)=
* **Infineon Technologies AG — Infineon Technologies Annual Report 2025** (filed 2025-11-27).
  [Original](https://www.infineon.com/assets/row/public/documents/corporate/investors/annual-reports/2025/2025-annual-report-v01-00-en.pdf).
  Infineon's account of the sale of its 200 mm Austin fab to SkyWater on 2025-06-30 with a long-term supply agreement, including the €149 million impairment it recorded on the disposal. "In June 2025, we sold our 200-millimeter fab in Austin (Texas, USA) to the U.S.-based company SkyWater and entered into a long-term supply agreement." (Introductory section); "On 30 June 2025, the 200-millimeter fab in Austin (USA) was sold to SkyWater Technology, Inc. ("SkyWater")." (Notes to the consolidated financial statements, note 7)
  Auditor: Deloitte GmbH Wirtschaftsprüfungsgesellschaft, 2025-11-27: "Munich/Germany, 27 November 2025 Deloitte GmbH Wirtschaftsprüfungsgesellschaft".
  Relationships: {ref}`SkyWater's purchase of Infineon's Austin fab (Fab 25) <filings-rel-infineon-fab25-sale>` · {ref}`Infineon as SkyWater's wafer customer (2022 frame agreement, Fab 25 supply agreement) <filings-rel-infineon-wafer-supply>`.
  Related pages: {ref}`overview-index` — The report is the seller's side of the 2025 transaction that joined the Austin fab to the owner of the Minnesota fab.
  Note: filed gives the latest signature date printed in the report (Neubiberg, 27 November 2025); the publication date was not retrieved.

(filing-skywater-8-k-2026-01-26)=
* **SkyWater Technology, Inc. — Current report: Agreement and Plan of Merger with IonQ, Inc.** (filed 2026-01-26; SEC accession 0001193125-26-021606).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000119312526021606/d20158d8k.htm) · [Wayback copy](https://web.archive.org/web/20260131215354/https://www.sec.gov/Archives/edgar/data/1819974/000119312526021606/d20158d8k.htm).
  Period: event of 2026-01-25.
  SkyWater reports its merger agreement with IonQ, under which IonQ would acquire SkyWater through two mergers with IonQ subsidiaries; the forward-looking statements refer to the newly acquired Texas operations (Fab 25). "entered into an Agreement and Plan of Merger (the "Merger Agreement") with IonQ, Inc., a Delaware corporation ("Parent" or "IonQ")" (Item 8.01); "our ability to integrate the operations of our newly-acquired operations in Texas ("Fab 25") with our existing operations" (Forward-looking statements)
  Relationships: {ref}`IonQ's acquisition of SkyWater (2026) <filings-rel-skywater-ionq-merger>` · {ref}`SkyWater's purchase of Infineon's Austin fab (Fab 25) <filings-rel-infineon-fab25-sale>`.
  Related pages: {ref}`overview-index` — The merger changes the ownership of the fab whose history the overview gives.

(filing-skywater-ex-99-1-2026-01-26)=
* **SkyWater Technology, Inc. — Joint press release: IonQ to Acquire SkyWater Technology** (filed 2026-01-26; SEC accession 0001193125-26-021606).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000119312526021606/d20158dex991.htm) · [Wayback copy](https://web.archive.org/web/20260126163552/https://www.sec.gov/Archives/edgar/data/1819974/000119312526021606/d20158dex991.htm).
  The joint IonQ and SkyWater announcement of the acquisition at \$35.00 per share in cash and stock (about \$1.8 billion equity value); SkyWater keeps its Bloomington headquarters and its Minnesota, Florida and Texas facilities become "Regional Quantum Production Hubs". "IonQ will acquire SkyWater for \$35.00 per share in a cash-and-stock transaction, subject to a collar, implying a total equity value of approximately \$1.8 billion" (First paragraph); "SkyWater will maintain its headquarters in Bloomington, Minnesota and its facilities in Minnesota, Florida, and Texas will serve as Regional Quantum Production Hubs." (Transaction details)
  Relationships: {ref}`IonQ's acquisition of SkyWater (2026) <filings-rel-skywater-ionq-merger>`.
  Related pages: {ref}`overview-index` — The release states the planned role of the Minnesota fab under its new owner.
  Amends/filed with: {ref}`full entry <filing-skywater-8-k-2026-01-26>`.

(filing-ionq-10-k-2026-02-25)=
* **IonQ, Inc. — Annual report on Form 10-K for the fiscal year ended 2025-12-31** (filed 2026-02-25; investor-relations filing 19184000; SEC accession not retrieved).
  [Original](https://investors.ionq.com/financials/sec-filings/sec-filings-details/default.aspx?FilingId=19184000) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001824920/b593e7b3-f252-422f-b4f0-ded524a5d58a.pdf).
  IonQ's annual report written while the SkyWater acquisition was pending; it presents the acquisition as giving IonQ embedded access to a secure quantum foundry and lists its completion and integration among forward-looking risks. "we announced the currently-pending acquisition, which we refer to as the SkyWater Acquisition, of SkyWater Technologies, Inc., which we refer to as SkyWater" (Item 1, Business); "including the pending acquisition of SkyWater Technology, Inc." (Forward-looking statements)
  Auditor: Ernst & Young LLP, 2026-02-25: "/s/ Ernst & Young LLP We have served as the Company’s auditor since 2020. Tysons, Virginia February 25, 2026".
  Relationships: {ref}`IonQ's acquisition of SkyWater (2026) <filings-rel-skywater-ionq-merger>`.
  Related pages: {ref}`overview-index` — The acquirer's annual report states why it is buying the company that runs the Minnesota fab.

(filing-skywater-10-k-2026-03-11)=
* **SkyWater Technology, Inc. — Annual report on Form 10-K for the fiscal year ended 2025-12-28** (filed 2026-03-11; SEC accession 0001819974-26-000009).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997426000009/skyt-20251228.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/b2fdfb0f-75d5-4f1c-8de5-0ece215053ce.pdf).
  SkyWater's last annual report before the IonQ merger. It describes the completed Fab 25 purchase, gives Infineon's share of revenue (43 % in 2025, 7 % in 2024), repeats the 26-year Cypress captive period and lists the Cypress Process Technology License Agreement and its amendments as exhibits. "Infineon accounted for 43% and 7% of our revenue for fiscal years ended December 28, 2025 and December 29, 2024, respectively." (Item 1, Business, Our Customers); "Process Technology License Agreement, dated as of March 1, 2017, by and between Cypress Semiconductor Corporation and Cypress Semiconductor (Minnesota) Inc." (Item 15, exhibit 10.7)
  Auditor: KPMG LLP, 2026-03-11: "/s/ KPMG LLP We have served as the Company's auditor since 2024. Minneapolis, Minnesota March 11, 2026".
  Relationships: {ref}`SkyWater describes the fab's Cypress origin <filings-rel-skywater-fab-history>` · {ref}`the 2017 Process Technology License Agreement and its amendments <filings-rel-cypress-technology-license>` · {ref}`SkyWater's purchase of Infineon's Austin fab (Fab 25) <filings-rel-infineon-fab25-sale>` · {ref}`Infineon as SkyWater's wafer customer (2022 frame agreement, Fab 25 supply agreement) <filings-rel-infineon-wafer-supply>` · {ref}`IonQ's acquisition of SkyWater (2026) <filings-rel-skywater-ionq-merger>`.
  Inventory: SEC-03.
  Related pages: {ref}`overview-index` — The report's Cypress history and licence exhibits are the latest restatement of the lineage the overview describes.
  Note: This "26 years" figure disagrees with SkyWater's earlier IPO filings (skywater-drs-2020-08-12, skywater-s-1-2021-03-22), which gave the Cypress captive period as 20 years; 26 years (1991-2017) is the figure consistent with the fab's Control Data origin.

(filing-ionq-s-4-2026-03-20)=
* **IonQ, Inc. — Form S-4 registration statement (proxy statement/prospectus) for the acquisition of SkyWater Technology** (filed 2026-03-20; investor-relations filing 19273247; SEC accession not retrieved).
  [Original](https://investors.ionq.com/financials/sec-filings/sec-filings-details/default.aspx?FilingId=19273247) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001824920/5eb66363-f41e-4a4d-a84d-a80608d25100.pdf).
  IonQ's registration statement for the shares issued to SkyWater stockholders, containing the joint proxy statement/prospectus. It says IonQ expects to keep SkyWater's lease of the Minnesota facility from Oxbow Realty Partners and the related \$39 million loan of Oxbow Realty. "IonQ expects to retain (i) SkyWater's lease agreement for the SkyWater Minnesota facility with Oxbow Realty Partners, LLC ("Oxbow Realty"), a consolidated variable interest entity of SkyWater" (Summary); "Its principal executive offices are located at 2401 East 86th Street, Bloomington, Minnesota 55425" (Summary, the parties)
  Relationships: {ref}`IonQ's acquisition of SkyWater (2026) <filings-rel-skywater-ionq-merger>` · {ref}`Oxbow ownership, management fees and property transactions <filings-rel-oxbow-related-party>`.
  Related pages: {ref}`overview-index` — The prospectus records how the Minnesota fab's site is held under its new owner.

(filing-skywater-defm14a-2026-03-31)=
* **SkyWater Technology, Inc. — Definitive merger proxy statement for the special meeting on the IonQ merger** (filed 2026-03-31; investor-relations filing 19306852; SEC accession not retrieved).
  [Original](https://ir.skywatertechnology.com/financials/sec-filings/sec-filings-details/default.aspx?FilingId=19306852) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/8dd8e057-784d-4944-9c8f-d6adde088aab.pdf).
  The proxy statement asking SkyWater stockholders to adopt the merger agreement with IonQ at a virtual special meeting on 2026-05-08; the merger agreement is attached as Annex A. "On January 25, 2026, SkyWater Technology, Inc. ("SkyWater") entered into an Agreement and Plan of Merger (the "Merger Agreement") with IonQ, Inc. ("IonQ")" (Letter to stockholders); "A copy of the Merger Agreement is attached as Annex A" (Summary)
  Relationships: {ref}`IonQ's acquisition of SkyWater (2026) <filings-rel-skywater-ionq-merger>`.
  Related pages: {ref}`overview-index` — The merger changes the ownership of the fab whose history the overview gives.

(filing-skywater-def-14a-2026-04-27)=
* **SkyWater Technology, Inc. — Definitive proxy statement for the 2026 annual meeting of stockholders** (filed 2026-04-27; SEC accession 0001140361-26-016806).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000114036126016806/ny20064068x1_def14a.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/640878fa-0e76-4252-97ef-295516dfc5ee.pdf).
  The 2026 proxy statement, for a routine annual meeting held while the IonQ merger was pending, asks stockholders to ratify KPMG LLP as auditor and discloses that KPMG replaced Deloitte & Touche LLP as SkyWater's independent registered public accounting firm in mid-2024. "On June 21, 2024, the audit committee selected KPMG LLP to serve as our independent registered public accounting firm, effective as of such date, and notified Deloitte & Touche LLP ("Deloitte") of its dismissal as our independent registered public accounting firm effective as of that date" (Proposal to ratify the appointment of the independent registered public accounting firm, Change in Auditors); "Deloitte's reports on our consolidated financial statements for each of the fiscal years ended December 31, 2023 and January 1, 2023 did not contain any adverse opinion or a disclaimer of opinion, nor were they qualified or modified as to uncertainty, audit scope, or accounting principles" (Proposal to ratify the appointment of the independent registered public accounting firm, Change in Auditors)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-skywater-10-q-2026-05-08)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2026-03-29** (filed 2026-05-08; SEC accession 0001819974-26-000014).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997426000014/skyt-20260329.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/093d3206-7e3f-4bca-8e02-20c0acfb1d14.pdf).
  First-quarter fiscal 2026 report, filed after the IonQ merger agreement was signed (2026-01-25) and while the Fab 25 (Austin) purchase price of \$206,466 thousand from Infineon's Spansion affiliate was on the balance sheet; discloses a material weakness specific to Fab 25 account reconciliation. "our disclosure controls and procedures were not effective as of March 29, 2026 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures); "related to Infineon's 200 mm fab in Austin, Texas (the "Transaction"). The purchase price for the Transaction was \$206,466" (Notes to the condensed consolidated financial statements, note 4)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>` · {ref}`SkyWater's purchase of Infineon's Austin fab (Fab 25) <filings-rel-infineon-fab25-sale>` · {ref}`IonQ's acquisition of SkyWater (2026) <filings-rel-skywater-ionq-merger>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-ionq-8-k-2026-07-31)=
* **IonQ, Inc. — Current report: completion of the acquisition of SkyWater Technology** (filed 2026-07-31; investor-relations filing 19650888; SEC accession not retrieved).
  [Original](https://investors.ionq.com/financials/sec-filings/sec-filings-details/default.aspx?FilingId=19650888) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001824920/530109bf-a75a-43c0-bf8f-e757dffff526.pdf).
  Period: event of 2026-07-31.
  IonQ's current report on completing the two-step merger by which SkyWater became a wholly owned subsidiary of IonQ. "Merger Sub 1 merged with and into SkyWater, with SkyWater surviving as a wholly owned subsidiary of the Company (the "First Merger")" (Introductory note)
  Relationships: {ref}`IonQ's acquisition of SkyWater (2026) <filings-rel-skywater-ionq-merger>`.
  Related pages: {ref}`overview-index` — The acquirer's filing dates the change of ownership of the fab whose history the overview gives.

(filing-skywater-8-k-2026-07-31)=
* **SkyWater Technology, Inc. — Current report: completion of the mergers with IonQ subsidiaries** (filed 2026-07-31; investor-relations filing 19650903; SEC accession not retrieved).
  [Original](https://ir.skywatertechnology.com/financials/sec-filings/sec-filings-details/default.aspx?FilingId=19650903) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/b6e5e06b-f163-4568-ac5a-c5a78fa919c6.pdf).
  Period: event of 2026-07-31.
  SkyWater reports the completion of the IonQ mergers on 2026-07-31: it became a wholly-owned subsidiary of IonQ and then merged into SkyWater Technology, LLC, and its revolving credit facility was repaid. "On July 31, 2026 (the "Closing Date"), pursuant to the Merger Agreement, (i) Merger Subsidiary 1 merged with and into the Company, with the Company surviving as a wholly-owned subsidiary of Parent" (Introductory Note); "the Registrant merged with and into SkyWater Technology, LLC (formerly known as Iris Merger Subsidiary 2 LLC), with SkyWater Technology, LLC surviving the merger" (Cover page note)
  Relationships: {ref}`IonQ's acquisition of SkyWater (2026) <filings-rel-skywater-ionq-merger>`.
  Related pages: {ref}`overview-index` — The filing dates the change of ownership of the fab whose history the overview gives.

(filing-skywater-10-q-2026-08-07)=
* **SkyWater Technology, Inc. — Quarterly report on Form 10-Q for the quarter ended 2026-06-28** (filed 2026-08-07; SEC accession 0001819974-26-000031).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000181997426000031/skyt-20260628.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/66d4e736-03c2-4909-86da-e9dc76376884.pdf).
  SkyWater's last quarterly report as a Nasdaq-listed filer, covering the quarter in which the IonQ merger closed (2026-07-31); still filed under Commission file number 001-40345, and still discloses material weaknesses in internal control over financial reporting, including one specific to Fab 25 account reconciliation. "our disclosure controls and procedures were not effective as of June 28, 2026 due to the material weaknesses in our internal control over financial reporting described below" (Part I, Item 4, Controls and Procedures); "As of June 28, 2026, we have a material weakness in our revenue accounting process and a material weakness in our Fab 25 account reconciliation processes" (Part I, Item 4, Controls and Procedures)
  Relationships: {ref}`SkyWater's auditor appointments, material weaknesses and restatements as a public company <filings-rel-skywater-governance>` · {ref}`SkyWater's purchase of Infineon's Austin fab (Fab 25) <filings-rel-infineon-fab25-sale>` · {ref}`IonQ's acquisition of SkyWater (2026) <filings-rel-skywater-ionq-merger>`.
  Related pages: {ref}`overview-index` — The report is one of the periodic filings the overview's account of SkyWater's public-company history draws on.

(filing-skywater-15-12g-2026-08-10)=
* **SkyWater Technology, LLC — Form 15-12G, certification and notice of termination of registration** (filed 2026-08-10; SEC accession 0000950142-26-002290).
  [EDGAR](https://www.sec.gov/Archives/edgar/data/1819974/000095014226002290/eh260818332_1512g-sky.htm) · [investor-relations copy](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/9db539a8-ff58-4a9b-b002-7686653cbd62.pdf).
  SkyWater's deregistration filing after the IonQ merger closed (2026-07-31), filed under the surviving entity's new name, SkyWater Technology, LLC, certifying that its common stock has one holder of record. "Approximate number of holders of record as of the certification or notice date: One (1)" (Form 15-12G cover)
  Relationships: {ref}`IonQ's acquisition of SkyWater (2026) <filings-rel-skywater-ionq-merger>`.
  Related pages: {ref}`overview-index` — The filing marks the end of SkyWater's life as a Nasdaq-listed company that the overview's history covers.
