(history-fabs)=
# Cypress's fabs and foundries, 1983–2010

Before S8, Cypress made wafers in fabs of its own: one in San Jose, one in Round Rock, Texas, and two on
one site in Bloomington, Minnesota. From 1998 it also used foundries (single source).[^ar-fy1998] This page says which
fab ran what, and when, as far as public sources show. The processes themselves are described on
{ref}`history-technologies`.

## At a glance

| Fab | Where and wafer size | Cypress years | Processes the sources place there |
|---|---|---|---|
| Fab 1 | San Jose, California; 6-inch by 1993, 8-inch from 2000 | first fab; production to 1996, then R&D to 2007 | development of RAM3, 0.13 µm and 90 nm |
| Fab 2 ("Cypress Texas", CTI) | Round Rock, Texas; 6-inch (150 mm) | 1986–2008 | P20 (0.8 µm, reports undated); R28, L28, L28EPD, P26 (0.65 µm); S4AD-5 (SONOS) |
| Fab 3 ("Cypress Minnesota", CMI) | Bloomington, Minnesota; 6-inch | 1991–1998 | R28 and L28 (0.65 µm), about 0.6 µm |
| Fab 4 (later "Fab 4a") | Bloomington, beside Fab 3; 8-inch (200 mm) | 1995–2017 | R32, R42, RAM42, R52, B53D-3, B55SGT, R7, R8, C8, 90 nm, S8 |

The table summarises the sections below, where each entry carries its sources.

## Fab 1, San Jose

Cypress's 1993 10-K calls Fab 1 "the Company's first fabrication facility, recently upgraded to 6-inch
wafers" and the heart of its research and development (single source).[^ar-fy1993] Cypress developed
its RAM3 process there (single source).[^ar-fy1996]

In the third quarter of 1996 Cypress announced that Fab 1 would stop production and become "strictly a
research and development facility", with production to cease by December 1996.[^tenq-1996q3][^ar-fy1996]
The Gale company history dates the shutdown of manufacturing in San Jose to October 1996 (single
source).[^fu-cypress]

The move of production to one eight-inch fab led Cypress to decide in 1998 to convert Fab 1 from six-inch
to eight-inch wafers "to ensure compatibility". Cypress's 2001 report says the conversion was done in
fiscal 2000 (Cypress's reports).[^ar-fy1997][^ar-fy1998][^ar-fy2001] Fab 1 then served as the development
fab for the next generations:

* **0.13 µm.** In July 2000 Cypress and Mosel Vitelic agreed to develop 0.13 µm technology together,
  "initially be deployed in Cypress's Fab 1 R&D facility" (single source).[^eet-2000-mosel]
* **0.12 µm and 90 nm.** Cypress's reports record the transfer of 0.12 µm technology from the San Jose
  R&D fab to Minnesota in 2001, and of 90 nm in 2002.[^ar-fy2001][^ar-fy2002]

Cypress sold Fab 1 in 2007. EE Times reported the sale of the R&D fab unit, the "Silicon Valley
Technology Center", for about $53 million; Cypress's 2009 report says "we sold our Fab 1 R&D plant in San
Jose, Calif., in 2007".[^eet-2007-fablite][^ar-fy2009]

## Fab 2, Round Rock, Texas

Fab 2 belonged to a subsidiary, Cypress Semiconductor (Texas), Inc. ("CTI"). Cypress's 1995 report says
Altera owned about 17 % of it (single source).[^ar-fy1995]

The qualification reports name the fab "CTI Round Rock, TX" (Cypress's reports).[^ar-fy1995][^qtp-021507]
In 1993 it was the company's largest fab (single source).[^ar-fy1993]

**Opening.** Cypress's 2008 report says Fab 2 ran "for all of its 22 years of operation" up to 2008, and
Semiconductor Digest says it "opened in 1986".[^ar-fy2008][^sd-2007-fab2] A later property report says the
campus "had been open for 20 years" when it closed in 2008, which would put the opening around 1988;
the sources disagree on this point.[^ar-fy2008][^ccre-roundrock]

**Wafers and processes.** Fab 2 ran six-inch (150 mm) wafers throughout.[^ar-fy1997][^eet-2007-fablite] In
1997 Cypress said Fabs 2 and 3 produced six-inch wafers "primarily with 0.6-micron" processes (single
source).[^ar-fy1997] Cypress's qualification reports show:

* **0.8 µm.** P20, for MAX EPLDs (Cypress's reports). The reports are undated; their QTP numbers,
  91216 and 93321, suggest 1991 and 1993 (our reading).[^qtp-091216][^qtp-093332]
* **0.65 µm.** The R28 SRAM process qualified at Fab 2 in November 1997. A further R28 product moved from
  Fab 3 in 1998 (the report's number; its version 1.3 is dated March 1999). The L28 clock and logic
  process moved from Fab 3 in April 1998, and P26 ran there for PROMs (Cypress's reports).[^qtp-097476][^qtp-098393][^qtp-031101][^qtp-096411]
* **S4AD-5.** "New Technology S4AD-5" was qualified in April 2001 with a clock generator (Cypress's
  reports).[^qtp-021507][^qtp-042806]

In 2002 Cypress wrote that its "SONOS process reduced our Fab 2 line width from 0.5-micron to
0.35-micron" (single source).[^ar-fy2002] How that sentence bears on the S4AD-5 design rules is discussed
on {ref}`history-sonos-s4`.

**SRAMs.** In March 1998 Cypress said Fab 2 would "stop making SRAMs" and keep to "data communication
ICs, programmable logic, and chips for its Computer Products divisions".[^eet-1998-restructure][^ar-fy1997]
Its reports, though, record an R28 dual-port SRAM moved from Fab 3 into Fab 2, in 1998 by the report's
number; the plan and the reports disagree (Cypress's reports).[^qtp-098393][^ar-fy1997]

**Other work.** Cypress's CEO later wrote that during the 1998 downturn Fab 2 made micro-mechanical
optical chips for Silicon Light Machines as foundry work, "using only standard CMOS" (single
source).[^edn-2000-slm]

**Closure.** Cypress's board approved leaving the Texas fab in December 2007, and Fab 2 closed in
2008.[^ar-fy2008][^sd-2007-fab2][^ar-fy2009] Cypress wrote that its "0.35-micron technology on 6-inch
wafers was no longer economically viable" (single source).[^ar-fy2008]

Cypress completed the sale of the building in 2013. A property report says the site is being redeveloped
as warehouses.[^ar-fy2013][^ccre-roundrock]

## Fab 3, Bloomington, Minnesota

**Who built the plant.** The Star Tribune gives two builders. In 2017 it wrote that the plant was "built
in the 1980s by Control Data"; in 2019 it wrote that VTC Inc., the chip business Control Data sold in 1982,
"added the plant", and that Control Data bought it back in the late 1980s. The two articles
disagree.[^strib-2017][^strib-2019]

**The purchase.** Cypress paid $14.7 million. The Gale company history dates the purchase to the end of
1990 and the Star Tribune to January 1991.[^fu-cypress][^strib-2017]

**Fab 3.** Cypress named the plant Fab 3 and said it "commenced operations in 1991". A 1994 proxy
statement names the subsidiary that ran it: Cypress Semiconductor (Minnesota) Inc., "CMI", the company's
third wafer fab (Cypress's reports).[^ar-fy1993][^proxy-1994] Fab 3 ran six-inch wafers, mostly at
0.6 µm.[^ar-fy1997][^eet-1998-restructure] The earliest R28 SRAM reports found, of September 1996, place
that 0.65 µm process at Fab 3 (single source).[^qtp-096091]

**Closure.** Cypress shut Fab 3 down in 1998 and moved its SRAM production to the eight-inch Fab 4 next
door. The Fab 3 tools that could be upgraded to eight-inch were moved to Fab 4.[^ar-fy1998][^eet-1998-restructure][^ar-fy1997]

## Fab 4, Bloomington, Minnesota

**Building it.** Cypress built Fab 4 on the Fab 3 site: ground was broken in August 1994, and "Fab IV"
produced its first revenue wafers "in only 11 months", in 1995.[^ar-fy1995][^sd-2007-fab2] It was
Cypress's first eight-inch fab.[^ar-fy1995][^ar-fy1997][^sd-2007-fab2]

**One site, two fabs.** SkyWater's plant is described in the press as the plant Cypress bought in 1991,
and the SKY130 reference counts Cypress's time there as 26 years, 1991 to 2017 (see {ref}`filings-index`).[^strib-2017]
Both descriptions fit the reports: the site bought in 1991 held Fab 3, and Fab 4 was added to it in 1994–95.[^ar-fy1993] We read the Star Tribune's "under Cypress, the size of the cleanroom at SkyWater's plant more than
doubled" as the Fab 4 addition (our reading).[^strib-2019]

**Fab 4a, 4b and 4c.** Cypress's 1997 report planned to use Fab 3's upgraded tools "to build out Fab
4b". Its 1998 report says only that they "were transferred to Fab 4 production". Its 1999 report still
plans to spend 2000 "constructing Fab 4b and Fab 4c". The reports disagree on whether Fab 4b was built
in 1998, unless the 1998 move was into Fab 4a.[^ar-fy1997][^ar-fy1998][^ar-fy1999] No later source found
says whether Fab 4b or Fab 4c was completed.

**Processes.** Fab 4 ran every Cypress SRAM and logic generation from 0.5 µm to 90 nm:

* **R42.** "New R42D Technology Qualification" is dated October 1997 and R42HD November 1997 (Cypress's
  reports).[^qtp-097483][^qtp-102101]
* **R7, R8, C8, L8, C9, R9, R95 and S8.** A 2015 Cypress notice lists "250nm R7, 130nm C8/R8/S8/L8 and
  90nm C9/R9/R95 technology products at Cypress Fab 4" (single source).[^pin-152804]
* **S8.** The first S8 qualification, "S8 SONOS technology", was at "Cypress Minnesota CMI (Fab4)" in
  November 2008 (single source).[^qtp-113005] Cypress's 2010 report calls S8 its PSoC process, run in Fab 4
  and at foundries.[^ar-fy2010]

Cypress sold Fab 4 in March 2017 to the new SkyWater Technology Foundry.[^tenq-2017q1][^strib-2017]

## The "Fab 5" that was not built

Cypress planned a second, eight-inch fab in Round Rock, called "Fab V" or "Fab 5". Its own reports trace
the project:

* **1995–1996.** Cypress bought 110 more acres in Round Rock and "broken ground on Fab V", to be "almost
  identical" to Fab IV. The Gale history dates the start of building to April 1996.[^ar-fy1995][^ar-fy1996][^fu-cypress]
* **1996.** "In the third quarter, the Company decided to put on hold construction of Fab V due to market
  conditions." (single source)[^ar-fy1996]
* **1998.** Fab 5 "can now be deferred until late 1999", and 0.25 µm technology would go into "Fab 5, an
  8-inch facility that will be built in the second half of 1999".[^ar-fy1997][^eet-1998-restructure]

No later report found mentions Fab 5. Semiconductor Digest says only that Fab 2 was "expanded in
1999" (single source).[^sd-2007-fab2] Whether anything was built after 1999 is not in the public record
found.

In the qualification reports, "Fab 5" means something else: the Grace foundry in Shanghai (see below).
The reports use that name from 2009 onwards (Cypress's reports).[^qtp-091302][^qtp-151005]

## Foundries and partners

Cypress's 1998 report says "we have also begun to use wafer foundries", for a 0.18 µm logic
technology (single source).[^ar-fy1998] The foundries the sources name before S8:

| Partner | What the sources say | Sources |
|---|---|---|
| Magnachip, Cheong-Ju, Korea | P26 moved from Fab 2 as a three-metal "P26 TLM", qualified March 2006 | single source[^qtp-054605] |
| NEC Electronics America, Roseville, California | a USB 2.0 bridge chip on NEC's "0.25um" process, five metal layers, qualified June 2003 | single source[^qtp-030310] |
| Hyundai Electronics ("Fab HME"), Korea | a "0.5um TLM" (three-metal) process for a dual-port SRAM, qualified August 2000 | single source[^qtp-001004] |
| Tower, IBM and Chartered | foundries of IMI, which Cypress bought in February 2001 | single source[^qtp-i000006] |
| TSMC, Taiwan | process development for CPLDs in 1998; L28 moved there in 2003; a 0.35 µm ASIC process qualified in December 2003 | Cypress's reports[^ar-fy1998][^qtp-080608][^qtp-s050001] |
| ProMOS and Powerchip, Taiwan | memory processes: ProMOS S17 (0.17 µm, 2003), Powerchip 0.16 µm | Cypress's reports[^qtp-032301][^qtp-051501] |
| Honeywell, Minnesota | a joint silicon-on-insulator process from 2002 | conflict on the node[^ar-fy2002][^edn-2005-honeywell] |
| Grace (GSMC, later HHGrace), Shanghai | foundry deal of December 2005; S4 PSoC first; 0.35 µm SONOS and C8 moved from 2006 | Cypress and EE Times[^ar-fy2005][^eet-2005-grace][^ar-fy2006][^eet-2006-c8] |
| UMC, Taiwan | a 130 nm flash product deal by 2007; all SRAM at 65 nm and below from 2007 | Electronics Weekly and EE Times[^ew-2007-umc][^eet-2007-fablite] |

**Honeywell.** Cypress's 2002 and 2003 reports call the joint programme a "0.13-micron
Silicon-On-Insulator" process in Fab 4.[^ar-fy2002][^ar-fy2003] EDN calls the resulting process
"SOI-based, 150-nm technology" co-developed with Cypress, which "evolved from Honeywell's
previous-generation, 0.25-micron technology".[^edn-2005-honeywell] The node therefore differs between the
sources.

**Grace.** The December 2005 deal covered Cypress's PSoC, image-sensor, wireless USB and PC clock
processes, and production was to start with "the PSoC mixed-signal array on Cypress's proprietary S4
technology".[^eet-2005-grace][^ar-fy2005] Cypress completed the transfer of its "[0].35-micron SONOS process"
during 2006 (Cypress's reports).[^ar-fy2006][^tenk-fy2007] In July 2006 it announced it would begin moving
"its 0.13-micron C8 process technology" to Grace in the third quarter, for USB and clock chips (single
source).[^eet-2006-c8] In 2009 an older SRAM process, RAM42, followed (single source).[^qtp-091302]

**Grace and 65 nm.** In 2007 the press disagreed about Grace. Electronics Weekly wrote that "Cypress
currently uses its own 65nm technology" there; EE Times wrote that Grace "isn't capable of 65-nm
manufacturing".[^ew-2007-umc][^eet-2007-fablite]

**UMC and S8.** In 2007 EE Times reported a plan to "shift its 0.13-micron S8 embedded-flash technology"
to UMC (single source).[^eet-2007-fablite]

## How the reports name fabs

The qualification reports are reissued from time to time, and the reissues do not keep the original
names of the sites. Read them with these points in mind:

* **"Fab 5" is a foundry.** Reports from 2009 onwards call Grace in Shanghai "Fab 5" or "Fab5 GSMC"
  (Cypress's reports).[^qtp-091302][^qtp-151005]
* **GSMC becomes HHGrace.** A 2015 reissue lists the August 2006 qualification of the foundry as "Qualify
  HHGrace using PSoC Device Product Family", under the foundry's later name (single source).[^qtp-151005]
* **Fab 4 becomes "Skywater".** A 2025 reissue of a 2004 report gives the fab as "Skywater --
  Bloomington, MN" and writes "from Skywater" into the 2004 history rows. An earlier issue of a report on
  the same process says "Cypress Semiconductor -- Bloomington, MN" (Cypress's reports).[^qtp-041406][^qtp-024110]
* **Stale fields.** A 2009 report of the move of RAM42 to Grace still prints the die fab line as
  "Fab4/RAM42" (single source).[^qtp-091302]

## Open questions

* **Fab 2's opening year.** 1986 or about 1988?
* **Fab 5.** Was anything built on the Round Rock site after 1999?
* **Fab 4b and Fab 4c.** Were they built, and when?
* **The Honeywell SOI node.** Was it 0.13 µm or 150 nm?
* **The builder of the Bloomington plant.** Control Data or VTC?

## References

### Cross-check

* [Cypress, Form 10-K for fiscal 1993](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1994.pdf>) — the three fabs of 1993 and their processes.[^ar-fy1993]
* [Cypress, 2008 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2008.pdf>) — the closure of Fab 2 after 22 years.[^ar-fy2008]
* [Semiconductor Digest, *Cypress getting rid of Round Rock, TX fab*](<https://sst.semiconductor-digest.com/2007/12/cypress-getting-rid-of-round-rock-tx-fab/>) — opening years of Fab 2 and Fab 4.[^sd-2007-fab2]

### High-level understanding

* [FundingUniverse, *History of Cypress Semiconductor Corporation*](<https://www.fundinguniverse.com/company-histories/cypress-semiconductor-corporation-history/>) — a company history to 1998.[^fu-cypress]
* [Star Tribune, *Why computer-chip factories from the 1980s are still going strong in Bloomington*](<https://www.startribune.com/why-computer-chip-factories-from-the-1980s-are-still-going-strong-in-bloomington/510984342>) — the Bloomington plant's Control Data and VTC origins.[^strib-2019]

### Deep dive

* [Cypress, 1995 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1995.pdf>) — Fab IV's ground-breaking and first wafers, and CTI's ownership.[^ar-fy1995]
* [Cypress, 1996 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1996.pdf>) — Fab 1 made an R&D fab; the Fab V ground-breaking.[^ar-fy1996]
* [Cypress, 1997 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1997.pdf>) — wafer sizes and processes of Fabs 2, 3 and 4.[^ar-fy1997]
* [Cypress, 1998 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1998.pdf>) — the 1998 restructuring and the move to eight-inch wafers.[^ar-fy1998]
* [Cypress, 1999 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_1999.pdf>) — Fab 4a, and Fabs 4b and 4c planned.[^ar-fy1999]
* [Cypress, 2002 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2002.pdf>) — RAM 7, RAM 8 and the Fab 2 SONOS process.[^ar-fy2002]
* [Cypress, 2006 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2006.pdf>) — the 0.35 µm SONOS process moved to Grace.[^ar-fy2006]
* [Cypress, Form 10-Q for the third quarter of 1996](<https://web.archive.org/web/20170530145033/https://www.sec.gov/Archives/edgar/data/791915/0000791915-96-000013.txt>) — Fab 1's restructuring into an R&D fab.[^tenq-1996q3]
* [EE Times, *Cypress Restructures Manufacturing Operations*](<https://www.eetimes.com/cypress-restructures-manufacturing-operations/>) — the 1998 plan for Fabs 2, 3, 4 and 5.[^eet-1998-restructure]
* [EE Times, *Cypress inks foundry deal with Grace*](<https://www.eetimes.com/cypress-inks-foundry-deal-with-grace/>) — the processes to be moved to Grace.[^eet-2005-grace]
* [EE Times, *Cypress furthers 'fab lite'*](<https://www.eetimes.com/cypress-furthers-fab-lite/>) — UMC, the sale of Fab 1 and the S8 plan.[^eet-2007-fablite]
* [EDN, *Honeywell debuts rad-hard process in new foundry fab*](<https://www.edn.com/honeywell-debuts-rad-hard-process-in-new-foundry-fab/>) — the SOI process developed with Honeywell.[^edn-2005-honeywell]
* [Cypress, QTP 021507](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>) — S4AD-5 at "CTI Round Rock".[^qtp-021507]
* [Cypress, QTP 091302](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-091302-mobl-asynchronous-sram-product-family-cy62256-ram42hnha-technology-fab5-gsmc-productqualificationreport-en.pdf?fileId=8ac78c8c93dda25b01953e8470a271d4>) — RAM42 moved to Grace, "Fab5 GSMC".[^qtp-091302]

<!-- footnotes -->

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
[^ar-fy2003]: Cypress Semiconductor Corp., *2003 Annual Report* with Form 10-K, fiscal year ended
    2003-12-28: Item 1, Research and development.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2003.pdf>
[^ar-fy2005]: Cypress Semiconductor Corp., *2005 Annual Report* with Form 10-K, fiscal year ended
    2006-01-01: Item 1, Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2005.pdf>
[^ar-fy2006]: Cypress Semiconductor Corp., *2006 Annual Report* with Form 10-K, fiscal year ended
    2006-12-31: Item 1, Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2006.pdf>
[^tenk-fy2007]: Cypress Semiconductor Corp., Form 10-K for fiscal 2007, filed 2008-03-03, Item 1,
    Business. <https://www.sec.gov/Archives/edgar/data/791915/000104746908002122/a2182468z10-k.htm>
[^ar-fy2008]: Cypress Semiconductor Corp., *2008 Annual Report* with Form 10-K, fiscal year ended
    2008-12-28: shareholder letter and Item 1, Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2008.pdf>
[^ar-fy2009]: Cypress Semiconductor Corp., *2009 Annual Report* with Form 10-K, fiscal year ended
    2010-01-03: shareholder letter.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2009.pdf>
[^ar-fy2010]: Cypress Semiconductor Corp., *2010 Annual Report* with Form 10-K, fiscal year ended
    2011-01-02: "Manufacturing" section.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2010.pdf>
[^ar-fy2013]: Cypress Semiconductor Corp., *2013 Annual Report* with Form 10-K: Item 7, Management's
    Discussion and Analysis.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2013.pdf>
[^tenq-1996q3]: Cypress Semiconductor Corp., Form 10-Q for the quarter ended 1996-09-30, filed
    1996-11-14, Notes to financial statements (restructuring); Wayback Machine copy of the EDGAR
    filing.
    <https://web.archive.org/web/20170530145033/https://www.sec.gov/Archives/edgar/data/791915/0000791915-96-000013.txt>
[^tenq-2017q1]: Cypress Semiconductor Corp., Form 10-Q for the quarter ended 2017-04-02, filed
    2017-05-02, Notes (assets held for sale); Wayback Machine copy of the EDGAR filing.
    <https://web.archive.org/web/20170503100919/https://www.sec.gov/Archives/edgar/data/791915/000079191517000030/cy-04022017x10xq.htm>
[^proxy-1994]: Cypress Semiconductor Corp., definitive proxy statement (Schedule 14A), filed
    1994-03-15; Wayback Machine copy of the EDGAR filing.
    <https://web.archive.org/web/20170224082226/https://www.sec.gov/Archives/edgar/data/791915/0000791915-94-000010.txt>
[^eet-1998-restructure]: EE Times staff, *Cypress Restructures Manufacturing Operations*, EE Times,
    1998-03-09. <https://www.eetimes.com/cypress-restructures-manufacturing-operations/>
[^eet-2000-mosel]: EE Times, *Cypress, Mosel Vitelic to develop 0.13-micron process technology*,
    2000-07-07.
    <https://www.eetimes.com/cypress-mosel-vitelic-to-develop-0-13-micron-process-technology/>
[^eet-2005-grace]: Mark LaPedus, *Cypress inks foundry deal with Grace*, EE Times, 2005-12-12.
    <https://www.eetimes.com/cypress-inks-foundry-deal-with-grace/>
[^eet-2006-c8]: Mark LaPedus, *Cypress transfers 130-nm process to Grace*, EE Times, 2006-07-19.
    <https://www.eetimes.com/cypress-transfers-130-nm-process-to-grace/>
[^eet-2007-fablite]: EE Times, *Cypress furthers 'fab lite'*, 2007-03-05.
    <https://www.eetimes.com/cypress-furthers-fab-lite/>
[^ew-2007-umc]: Electronics Weekly, *Cypress moves SRAM production to foundry*, February 2007.
    <https://www.electronicsweekly.com/news/business/manufacturing/cypress-moves-sram-production-to-foundry-2007-02/>
[^sd-2007-fab2]: Semiconductor Digest, *Cypress getting rid of Round Rock, TX fab*, 2007-12-19.
    <https://sst.semiconductor-digest.com/2007/12/cypress-getting-rid-of-round-rock-tx-fab/>
[^ccre-roundrock]: Connect CRE, *Former Round Rock Cypress Plant Converting to Warehouses*, undated,
    retrieved 2026-09-25.
    <https://www.connectcre.com/stories/former-round-rock-cypress-plant-converting-to-warehouses/>
[^strib-2017]: Alex Van Abbema, *Twin Cities tech executives form new company, buy Cypress chip
    plant in Bloomington*, Star Tribune, 2017-03-31.
    <https://www.startribune.com/twin-cities-tech-executives-form-new-company-buy-cypress-chip-plant-in-bloomington/417672063>
[^strib-2019]: Evan Ramstad, *Why computer-chip factories from the 1980s are still going strong in
    Bloomington*, Star Tribune, 2019-06-09.
    <https://www.startribune.com/why-computer-chip-factories-from-the-1980s-are-still-going-strong-in-bloomington/510984342>
[^fu-cypress]: FundingUniverse (from the *International Directory of Company Histories*), *History
    of Cypress Semiconductor Corporation*, retrieved 2026-09-25.
    <https://www.fundinguniverse.com/company-histories/cypress-semiconductor-corporation-history/>
[^edn-2000-slm]: T. J. Rodgers, *Why Cypress Acquired Silicon Light Machines*, EDN, 2000-07-31.
    <https://www.edn.com/why-cypress-acquired-silicon-light-machines/>
[^edn-2005-honeywell]: Mark LaPedus, *Honeywell debuts rad-hard process in new foundry fab*, EDN,
    2005-04-27. <https://www.edn.com/honeywell-debuts-rad-hard-process-in-new-foundry-fab/>
[^pin-152804]: Cypress Semiconductor, Product Information Notification PIN152804, *Qualification of
    GlobalWafer Silicon Wafers for 250nm, 130nm and 90nm Technology Products at Cypress Fab 4*,
    2015-07-12 (copy hosted by Future Electronics).
    <https://media.futureelectronics.com/PCN/45887_SPCN.PDF>
[^qtp-021507]: Cypress Semiconductor, Product Qualification Report QTP 021507: *Failsafe Device Family & Options S4AD-5 SONOS Technology, Fab 2*, December 2015.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>
[^qtp-096091]: Cypress Semiconductor, Product Qualification Report QTP 96091: *Dual Port SRAM - R28 Technology, 6% Shrink*, September 1996.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-96091-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148ab080847>
[^qtp-097476]: Cypress Semiconductor, Product Qualification Report QTP 97476: *256K STATIC RAM "CY7C194/CY7195/CY7C199" R28 PROCESS, FAB 2 QUALIFICATION*, August 2016.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97476-256k-static-ram-r28-process-fab-2-qualification-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7150d8bb1af5>
[^qtp-098393]: Cypress Semiconductor, Product Qualification Report QTP 98393: *Dual Port SRAM - R28 Technology - Fab 2*, March 1999.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-98393-productqualificationreport-en.pdf>
[^qtp-102101]: Cypress Semiconductor, Product Qualification Report QTP 102101: *Synchronous/Asynchronous Dual Port SRAM (3.3V and 5V), R42HD Technology, Fab 4 Qualification*, July 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-102101-synchronous-asynchronous-dual-port-sram-3.3v-and-5v-r42hd-technology-fab-4-qualification-productqualificationreport-en.pdf>
[^qtp-113005]: Cypress Semiconductor, Product Qualification Report QTP 113005: *64K Serial Non-Volatile SRAM Product Family, S8 Technology, CMI (Fab 4)*, January 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^qtp-001004]: Cypress Semiconductor, Product Qualification Report QTP 001004: *0.5um TLM Technology, Fab HME, Dual Port SRAM with PCI Bus Controller*, January 2001.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-001004-productqualificationreport-en.pdf>
[^qtp-i000006]: Cypress Semiconductor, Product Qualification Report QTP I000006: *TS60D [0.6um CMOS] -- Tower (Fab28), CMOS5SF [Micrus] -- IBM/NY (Fab32), CSM 0.35um Logic Salicide -- Charter Semiconductor (Fab11)*, March 2007.
    <https://www.infineon.cn/assets/row/public/documents/10/316/infineon-qtp-i000006-ts60d-0.6um-cmos-tower-fab28-cmos5sf-micrus-ibm-ny-fab32csm-0.35um-logic-salicide-charter-semiconductor-fab11-productqualificationreport-en.pdf>
[^qtp-091302]: Cypress Semiconductor, Product Qualification Report QTP 091302: *MoBL Asynchronous SRAM Product Family, RAM42HNHA Technology, Fab5 GSMC*, February 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-091302-mobl-asynchronous-sram-product-family-cy62256-ram42hnha-technology-fab5-gsmc-productqualificationreport-en.pdf?fileId=8ac78c8c93dda25b01953e8470a271d4>
[^qtp-151005]: Cypress Semiconductor, Product Qualification Report QTP 151005: *PSoC RADON Device Family, S4AD-5 Technology, HHGrace FAB5*, October 2015.
    <https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-151005-psoc24x94-hhgrace-productqualificationreport-en.pdf>
[^qtp-041406]: Cypress Semiconductor, Product Qualification Report QTP 041406: *4 MEG (1.8V/3.0V) MOBL DEVICES, RAM8NLD-1.8 TECHNOLOGY, Skywater*, February 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-041406-4-meg-1-8v-3-0v-mobl-devices-ram8nld-1-productqualificationreport-en.pdf>
[^qtp-024110]: Cypress Semiconductor, Product Qualification Report QTP 024110: *1 MEG (3.0V) MOBL DEVICES RAM8NLD-1.8V TECHNOLOGY, FAB4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-024110-1-meg-3.0v-mobl-devices-ram8nld-1.8v-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152a1d61fde>
[^qtp-032301]: Cypress Semiconductor, Product Qualification Report QTP 032301: *16 MEG A/D MUX SRAM, S17 Technology, Promos Fab in Taiwan*, May 2004;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201204235131/https://www.cypress.com/file/92311/download>
[^qtp-042806]: Cypress Semiconductor, Product Qualification Report QTP 042806: *S4ADLATCH Technology, Fab 2*, January 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025144943/https://www.cypress.com/file/92521/download>
[^qtp-051501]: Cypress Semiconductor, Product Qualification Report QTP 051501: *Cypress Minnesota (CMI) Sort Site Qualification -- 2 Meg, 3V PSRAM Device, PowerChip 0.165µm*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201028052812/https://www.cypress.com/file/92636/download>
[^qtp-080608]: Cypress Semiconductor, Product Qualification Report QTP 080608: *High Accuracy EPROM Programmable Device Family, L28 Technology, TSMC-2A*, May 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-080608-high-accuracy-eprom-programmable-device-family-l28-technology-tsmc-2a-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714a27090cd2>
[^qtp-096411]: Cypress Semiconductor, Product Qualification Report QTP 96411: *256K/512K PROM - P26 Technology*, May 1997;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201026124735/https://www.cypress.com/file/93566/download>
[^qtp-097483]: Cypress Semiconductor, Product Qualification Report QTP 97483: *Low Voltage Deep Synchronous FIFO High Speed 100-MHZ Operation, R42D -- Fab 4*, May 2017.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97483-low-voltage-deep-sync-fifos-r42d-technology-fab4-device-cy7c42-v-productqualificationreport-en.pdf>
[^qtp-s050001]: Cypress Semiconductor, Product Qualification Report QTP S050001: *TSMC Fab 3, 0.35um -- SMaL Camera ASIC*, June 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201028064815/https://www.cypress.com/file/94406/download>
[^qtp-031101]: Cypress Semiconductor, Product Qualification Report QTP 031101: *High-Accuracy EPROM Programmable Device Family, L28 Technology, Fab 2*, January 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210128152257/https://www.cypress.com/file/92261/download>
[^qtp-091216]: Cypress Semiconductor, Product Qualification Report QTP 91216: *MAX EPLD, P20 Technology, Fab 2*, March 2000;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20200810011720/https://www.cypress.com/file/93411/download>
[^qtp-093332]: Cypress Semiconductor, Product Qualification Report QTP 93332: *MAX EPLD, P20 Technology, Fab 2*, March 2000;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201025104819/https://www.cypress.com/file/93456/download>
[^qtp-054605]: Cypress Semiconductor, Product Qualification Report QTP 054605: *P26 TLM Technology Transfer to Magnachip*, March 2006;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211206085735/https://www.cypress.com/file/92866/download>
[^qtp-030310]: Cypress Semiconductor, Product Qualification Report QTP 030310: *ISD-300LP Low Power USB 2.0 to ATA/ATAPI Bridge IC, NEC 0.25um Technology*, June 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507193447/https://www.cypress.com/file/92226/download>
