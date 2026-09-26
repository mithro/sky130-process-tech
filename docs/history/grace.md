(history-grace)=
# Grace and HHGrace: S8 in Shanghai

S8 was not made only in Bloomington. From 2010 Cypress also qualified S8 variants at a foundry in
Shanghai: Grace Semiconductor (宏力半导体, GSMC), which merged with Hua Hong NEC in 2011 to form
Shanghai Huahong Grace (华虹宏力, HHGrace), now part of Hua Hong Semiconductor (华虹半导体). This page
collects what public sources say about which Cypress processes ran there, in which fab, and how the
Shanghai S8 differs from the Fab 4 S8 that SkyWater runs today. Cypress's own fabs and its other
foundries are on {ref}`history-fabs`; S8 itself is on {ref}`history-s8-lineage`.

Chinese sources are quoted in the original in the evidence file, `data/history/grace.yaml`. On this page
they appear only in our English translation, marked as ours.

## At a glance

| Question | Answer | Sources |
|---|---|---|
| The foundry | Grace Semiconductor Manufacturing Corporation (GSMC), Shanghai, formed in 2000; merged with Hua Hong NEC (HHNEC) into HHGrace in 2011 | Wikipedia, Hua Hong, US Commerce Department |
| The fab | the former Grace fab at 1399 Zuchongzhi Road, Zhangjiang, called "GFab1" in 2013 and HH FAB3 from 2017; 8-inch (200 mm) | US Commerce Department, Hua Hong |
| Names in Cypress's reports | "Fab 5", "Fab5 GSMC", "GSMC-Fab 5", then "HHGrace Fab 3"; also "HHGrace Fab1" for a former HHNEC fab | Cypress's reports |
| Processes moved | S4AD-5 (0.35 µm SONOS) from 2006; C8 (0.13 µm logic) from 2006; RAM42 and the 0.09 µm SRAM R95LD-3R later | Cypress's reports, EE Times |
| S8 there | S8DIN-5R from March 2010; then S8TMC-5R, S8P12-10P, S8PF-10R, S8SPF-10P, S8PR2-10R | Cypress's reports |
| Parts | CapSense and touch-screen controllers, PSoC 4 (CY8C4013, CY8C4014), USB Type-C controllers (CCG2) | Cypress's reports |
| Stack, where printed | five metals of Ti/TiN/AlCu/Ti/TiN, 32 Å and 110 Å gate oxides (HHGrace Fab 3, 2014) | single source |
| SONOS licences | 0.13 µm SONOS licensed to Hua Hong NEC in 2007; SONOS and eCT licensed to HH-Grace by 2018 | EE Times, a Chinese trade report, Cypress |

The rows are explained, with their sources, below.

## The foundry and its fabs

**Grace.** Grace Shanghai was "formed by Grace Cayman as a pure-play foundry" in December 2000 (single
source).[^wiki-huahong] Its Chinese name was 上海宏力半导体制造有限公司, as a 2006 Chinese trade report of
the Cypress deal gives it.[^eepw-2006-grace]

**The merger.** The offshore parents merged in 2011: Hua Hong's 2023 prospectus says that in 2011 it
bought back a shareholder's stake and merged with Grace Cayman (our translation).[^hh-prospectus-2023]
Wikipedia also dates the merger of "HHNEC and Grace Shanghai" to 2011.[^wiki-huahong] The US Commerce
Department removed GSMC and HHNEC from its list of validated end-users in June 2013 "as a result of the
merger of the two companies to create HHGrace".[^fr-2013-veu] The operating company, 上海华虹宏力, was
established on 2013-01-24 (single source).[^hh-prospectus-2023]

**Which fab.** The 2013 rule lists three HHGrace fabs and keeps their old owners in the names: "HFab 1"
and "HFab 2" of Hua Hong NEC, and "GFab1, 1399 Zuchongzhi Road, Zhangjiang Hi-Tech Park".[^fr-2013-veu]
In 2017 Hua Hong numbered its fabs, and gave 华虹三厂 (HH FAB3) the address 祖冲之路1399号 (1399
Zuchongzhi Road) and 8-inch wafers (our translation).[^hh-fab-naming-2017] The same address is the
registered address of 上海华虹宏力 in the 2023 prospectus.[^hh-prospectus-2023] So HH FAB3 is the former
Grace fab (our reading).[^fr-2013-veu][^hh-fab-naming-2017]

**HH FAB1 is the former Hua Hong NEC fab.** The 2013 rule puts "HFab 1" at 1188 Chuanqiao Road, and Hua
Hong's 2017 list puts HH FAB1 at 川桥路1188号 (1188 Chuanqiao Road, our translation).[^fr-2013-veu][^hh-fab-naming-2017]
A 2020 Cypress report names its fab both "HHNEC / China" and "HHGrace Fab1 / S8SPF-10P" (single
source).[^qtp-152604] HH FAB2 is at 668 Guoshoujing Road in the 2013 rule but at 288 Halei Road in the
2017 list; the two sources differ, and we have not resolved this.[^fr-2013-veu][^hh-fab-naming-2017]

**Wafer size.** The Shanghai fabs run 200 mm wafers, as Fab 4 does. EE Times wrote in 2005 of "Grace's
8-inch facility in Shanghai"; Hua Hong gives HH FAB1 to FAB3 as 8-inch; Wikipedia counts "three 200mm
wafer fabs".[^eet-2005-grace][^hh-fab-naming-2017][^wiki-huahong] Hua Hong has three 8-inch fabs and one
12-inch fab, by its 2023 prospectus (single source).[^hh-prospectus-2023]

## What Cypress moved to Grace

**The deal.** In December 2005 Cypress and Grace agreed that Cypress would transfer its PSoC, CMOS image
sensor, wireless USB and PC clock processes, starting with "the PSoC mixed-signal array on Cypress's
proprietary S4 technology". A Chinese trade magazine, 电子产品世界, reported the same deal in early 2006,
with Grace to give Cypress priority for its foundry capacity (our translation).[^eet-2005-grace][^ar-fy2005][^eepw-2006-grace]

**Before S8.** Cypress's reports record these moves:

| Year | Process | Sources |
|---|---|---|
| 2006 | S4AD-5, the "[0].35-micron SONOS process", for PSoC 1 | Cypress's reports[^ar-fy2006][^qtp-062509] |
| 2006–2007 | "its 0.13-micron C8 process technology", for USB and clock chips; C8Q-3R at "GSMC Foundry (Fab 5)" | EE Times and Cypress[^eet-2006-c8][^qtp-082609] |
| to 2007 | "0.35-micron SONOS, 0.13-micron SRAM and LOGIC processes and 0.09-micron SRAM" | Cypress's reports[^ar-fy2010][^ar-fy2012] |
| 2009 | RAM42, an older SRAM process, at "Fab5 GSMC" | single source[^qtp-091302] |
| 2010 | R95LD-3R, the 0.09 µm SRAM, "Product Transfer from CMI to GSMC" | single source[^qtp-091206] |

The S4 and 0.35 µm SONOS work is on {ref}`history-sonos-s4`.

**S8 is not in the 10-Ks.** Cypress's annual reports from 2010 to 2015 list the processes transferred to
Grace, and none of them names S8 or a 0.13 µm SONOS process (Cypress's reports).[^ar-fy2010][^ar-fy2012][^ar-fy2015]
The qualification reports below show S8 there all the same.

## S8 at Grace and HHGrace

**The first S8 qualification.** A 2014 report's qualification history dates the first S8 qualification
at the Shanghai foundry to March 2010: CapSense parts "in Fab 5 GSMC on S8DIN-5R Process". Infineon still
lists a report titled "Capsense Device Family S8DIN-5R Fab 5 GSMC" (Cypress's reports).[^qtp-142304][^ifx-qtp-122801]

**External S8 capacity.** Cypress's 2010 report says demand for PSoC had filled its capacity in "S8, our
0.13-micron, nonvolatile PSoC wafer fabrication process". It planned to "triple our S8 capacity" in 2011
by adding internal and external capacity, keeping an "internal-external mix at approximately 50-50", and
was "bringing on a second foundry in China" (single source).[^ar-fy2010] The report does not name the
foundries. By 2010 Grace was already running S8 (the reports above); the second Chinese foundry may be
Hua Hong NEC, whose fab later appears as "HHGrace Fab1" in S8 reports, but no source says so (our
reading).[^qtp-142304][^qtp-152604]

**The S8 qualifications found.** Each row copies one Cypress report or listing title:

| Date | Technology | Fab as printed | Parts | Source |
|---|---|---|---|---|
| March 2010 | S8DIN-5R | "Fab 5 GSMC" | CapSense controllers (CY8C20x36A to CY8C20x96A) | QTP 142304 history[^qtp-142304] |
| April 2010 | S8TMC-5R | GSMC | touch-screen PSoC | QTP 142304 history[^qtp-142304] |
| undated | S8DIN-5R | "Fab 5 GSMC" | CapSense (QTP 122801) | Infineon listing[^ifx-qtp-122801] |
| May 2013 | S8P12-10P | "GSMC-Fab 5" | 5th-generation touch screen (TSG5_M) | QTP 142304 history[^qtp-142304] |
| undated | S8P12-10P | "HHGrace Fab1" | 5th-generation touch screen (QTP 141906) | single source, Infineon listing[^ifx-qtp-141906] |
| June 2014 | S8PF-10R | "Fab 3 / HHGrace, Shanghai China" | PSoC 4, CY8C4013 and CY8C4014 | single source, QTP 142304[^qtp-142304] |
| March 2016 | S8SPF-10P | "HHGrace Fab1" | automotive touch-screen controller, CYAT8168X | single source, QTP 152604[^qtp-152604] |
| September 2017 | S8PR2-10R | "HH Grace Fab 1" | EZ-PD CCG2 USB Type-C controllers | single source, QTP 164010[^qtp-164010] |

The reports for the 2010 and 2013 rows (QTP 090706, 100101 and 124505) were not found in a public copy;
Infineon now serves them only after log-in. The 2010 to 2014 rows are all from one report's history
table (single source).[^qtp-142304]

**Dual sourcing.** The Shanghai S8 was a second source beside Minnesota, not a replacement. The 2014
PSoC 4 report lists "CMI Fab 4" as its alternative fab, and the 2017 CCG2 report lists Fab 4 in
Bloomington and Fab 25 in Austin (Cypress's reports).[^qtp-142304][^qtp-164010] The 2014 report computes
one long-term failure rate from the Shanghai reports of 2010 to 2014 together, "QTPs 090706, 100101,
124505 & 142304" (single source).[^qtp-142304]

**Names that do not agree.** The 2014 report's title was changed "from S8P12-10R to S8PF-10R", and
Cypress's web page for it kept the old name. The 2017 report puts "HH Grace (Fab 1)" in "Taiwan", which
no other source supports; we read it as a clerical error (Cypress's reports).[^qtp-142304][^qtp-164010]
How the suffixes of S8 names are built is on {ref}`history-naming`.

## How the Shanghai S8 differs

Only one public Shanghai S8 report prints a stack, the 2014 HHGrace Fab 3 PSoC 4 report. The 2016 and
2017 HHGrace Fab 1 reports print "Proprietary" in place of every layer (Cypress's
reports).[^qtp-142304][^qtp-152604][^qtp-164010] The comparison is therefore between one Fab 3 report and
the Fab 4 S8 reports.

| | Fab 4 S8, 2013 report | Fab 4 S8, after the 2013 change | HHGrace Fab 3 S8PF-10R, 2014 |
|---|---|---|---|
| Metal layers | 3 (S8TNV-5R) | 3 (S8DIN-5R) | 5 |
| Metal 1 | 100 Å Ti / 3200 Å Al–Cu / 300 Å TiW | 150 Å Ti / 250 Å TiN / 3200 Å Al–Cu / 90 Å Ti / 500 Å TiN | 150 Å Ti / 250 Å TiN / 3200 Å Al–Cu / 90 Å Ti / 500 Å TiN |
| Metals 3 and 4 | — | — | 6500 Å Al–Cu in the same Ti/TiN sandwich |
| Metal 5 | — | — | 190 Å Ti / 450 Å TiN / 10000 Å Al–Cu / 90 Å Ti / 200 Å TiN |
| Gate oxides | 110 Å and 32 Å | not printed | 32 Å and 110 Å |
| Passivation | 7000 ± 2000 Å nitride | not printed | "NFUSOX / 1K oxide / 6k Nitride" |

Each column copies one Cypress report.[^qtp-113005][^qtp-123907][^qtp-142304] What they show:

* **The same oxides.** The HHGrace report prints "SiO2 / 32A/110A", the two gate oxides of the Fab 4
  S8 report (Cypress's reports).[^qtp-142304][^qtp-113005]
* **The same first metal, from 2013.** Fab 4 changed its S8 metals "from Ti/AlCu/TiW to
  Ti/TiN/AlCu/Ti/TiN" in 2013–2014, and the new Fab 4 metal 1 is film for film the HHGrace one (Cypress's
  reports).[^qtp-123907][^qtp-142304] The overview page describes the Fab 4 change ({ref}`overview-index`).
* **TiN at Grace before that.** Other Cypress processes at Grace also print TiN-clad aluminium where Fab 2
  and Fab 4 printed TiW: S4AD-5 at GSMC has "250A TiN/5,800A Al/700A TiN" against Fab 2's Ti/Al/TiW, and
  R95LD-3R at HHGrace Fab 3 has "Ti/TiN/Al/Ti/TiN: 150/250/3200/90/500" against Fab 4's "100Å Ti / 3200Å
  Al / 300Å TiW" (Cypress's reports).[^qtp-062509][^qtp-021507][^qtp-091206][^qtp-071302] The
  C8Q-3R report from GSMC is an exception: it prints the Fab 4 TiW stack (Cypress's reports).[^qtp-082609][^qtp-043004]
  We read this as the foundry using its own metallisation for most transferred processes (our reading).
* **Five metals.** The HHGrace S8PF-10R has five metal layers. The Fab 4 reports in this history are
  three-metal S8 versions; SkyWater's `s8pfhd` is also a five-metal stack (see {ref}`history-s8-lineage`).
  The HHGrace metal 3 to 5 thicknesses cannot be compared with a Fab 4 five-metal report here, because
  no such report is in the evidence (our reading).[^qtp-142304][^qtp-113005]
* **Different passivation.** HHGrace prints "NFUSOX / 1K oxide / 6k Nitride"; the 2013 Fab 4 S8 report
  prints "7000 +/- 2000A Nitride" (Cypress's reports).[^qtp-142304][^qtp-113005]

No public source found gives design rules, device lists or electrical parameters for the Shanghai S8, and
none says whether the SKY130 PDK describes it. The SKY130 PDK comes from the Minnesota fab.

## Hua Hong's side

**The 2007 SONOS licence.** EE Times reported in April 2007 that Cypress "will license its 0.13um SONOS
(Silicon Oxide Nitride Oxide Silicon) embedded nonvolatile memory technology to foundry Shanghai Hua Hong
NEC". A Chinese report says the same: Hua Hong NEC would obtain a process licence for 0.13 µm SONOS
embedded non-volatile memory from Cypress (our translation).[^eet-2007-hhnec-sonos][^mms-hhnec-sonos] The
two read as versions of one announcement, and neither says whether the licensed process was S8.

**Licences to HHGrace.** Cypress's 2018 report describes the licensing of its "embedded nonvolatile
memory technologies (SONOS and … eCT) to foundries, including UMC, HLMC and HH-Grace" (single
source).[^ar-fy2018] The same report lists an agreement with "HuaHong Grace" for foundry services beside
one with SkyWater.[^ar-fy2018]

**Money.** Cypress guaranteed lease payments for Grace's equipment and received options on "40.3 million
ordinary shares of Grace"; in 2010 and 2011 it prepaid for Grace wafers (Cypress's
reports).[^ar-fy2010][^ar-fy2012] In 2014 it bought "6.9 million ordinary shares of Hua Hong Semiconductor
Limited" in the Hong Kong listing (single source).[^ar-fy2015]

**What Hua Hong says.** Hua Hong's 2023 prospectus describes its embedded non-volatile memory platform as
covering 8-inch 0.35 µm to 90 nm and 12-inch 90 nm to 55 nm (our translation). It names no customers, and
Cypress (赛普拉斯) does not appear in it (single source).[^hh-prospectus-2023]

## Open questions

* **The first S8 at Grace.** Which S8 variant and which part came first, and what stack did S8DIN-5R
  print at GSMC in 2010? The reports QTP 090706, 100101, 122801 and 124505 would say; they are behind
  Infineon's log-in.
* **Which Chinese foundry was second.** Was the "second foundry in China" of 2011 Hua Hong NEC?
* **The licence and S8.** Was the 0.13 µm SONOS licensed to Hua Hong NEC in 2007 the S8 cell?
* **Fab 1 and Fab 3.** Did S8 run in both HHGrace fabs at the same time, and with the same stack?
* **Later S8 at HHGrace.** Which Infineon S8 parts are made in Shanghai now? No public notice was read for
  this page.
* **HH FAB2's address.** 668 Guoshoujing Road or 288 Halei Road?

## References

### Cross-check

* [US Commerce Department, validated end-users rule of 2013-06-03](<https://www.govinfo.gov/content/pkg/FR-2013-06-03/html/2013-13076.htm>) — the merger and the three HHGrace fabs with their addresses.[^fr-2013-veu]
* [Hua Hong Group, 华虹集团集成电路制造工厂启用统一命名](<https://www.huahong.com.cn/?m=detail&id=459>) — the 2017 fab numbers and addresses.[^hh-fab-naming-2017]
* [Cypress, QTP 142304](<https://web.archive.org/web/20210517161353/https://www.cypress.com/file/138901/download>) — S8PF-10R at HHGrace Fab 3, with the stack.[^qtp-142304]

### High-level understanding

* [Wikipedia, *Hua Hong Semiconductor*](<https://en.wikipedia.org/wiki/Hua_Hong_Semiconductor>) — the company's history and fabs.[^wiki-huahong]
* [EE Times, *Cypress inks foundry deal with Grace*](<https://www.eetimes.com/cypress-inks-foundry-deal-with-grace/>) — the 2005 deal.[^eet-2005-grace]

### Deep dive

* [Hua Hong Semiconductor, STAR-market prospectus, 2023](<http://static.sse.com.cn/stock/disclosure/announcement/c/202305/001307_20230510_ETYJ.pdf>) — the merger, the fabs and the eNVM platform, in Chinese.[^hh-prospectus-2023]
* [电子产品世界, 赛普拉斯与上海宏力达成代工协议](<https://m.fx361.com/news/2006/0101/29693231.html>) — the 2005 deal in the Chinese press.[^eepw-2006-grace]
* [EE Times, *Cypress licensing SONOS memory to Hua Hong NEC*](<https://www.eetimes.com/cypress-licensing-sonos-memory-to-hua-hong-nec/>) — the 2007 SONOS licence.[^eet-2007-hhnec-sonos]
* [国际金属加工网, 华虹NEC获Cypress 0.13微米SONOS NVM工艺授权](<https://www.mmsonline.com.cn/info/91858.shtml>) — the same licence in Chinese.[^mms-hhnec-sonos]
* [Cypress, QTP 152604](<https://web.archive.org/web/20201205000354/https://www.cypress.com/file/278091/download>) — S8SPF-10P at HHGrace Fab 1, "HHNEC".[^qtp-152604]
* [Cypress, QTP 164010](<https://web.archive.org/web/20211025133935/https://www.cypress.com/file/383716/download>) — S8PR2-10R at HH Grace Fab 1, with its alternative fabs.[^qtp-164010]
* [Cypress, QTP 123907](<https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/145273-Qualification_Report.pdf>) — the Fab 4 metal-stack change.[^qtp-123907]
* [Cypress, QTP 113005](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>) — the Fab 4 S8 stack of 2013.[^qtp-113005]
* [Cypress, QTP 091206](<https://web.archive.org/web/20201001021848/https://www.cypress.com/file/138641/download>) — the 0.09 µm SRAM at HHGrace Fab 3.[^qtp-091206]
* [Cypress, QTP 062509](<https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-062509-psoc21x34-95xx-gsmc-productqualificationreport-en.pdf>) — S4AD-5 at GSMC.[^qtp-062509]
* [Cypress, QTP 082609](<https://web.archive.org/web/20201026131537/https://www.cypress.com/file/95566/download>) — C8Q-3R at GSMC.[^qtp-082609]
* [Cypress, 2010 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2010.pdf>) — S8 capacity and a second Chinese foundry.[^ar-fy2010]
* [Cypress, 2012 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2012.pdf>) — the processes transferred to Grace.[^ar-fy2012]
* [Cypress, 2015 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2015.pdf>) — HuaHong Grace and the Hua Hong shares.[^ar-fy2015]
* [Cypress, 2018 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2018.pdf>) — the SONOS licences and foundry agreements.[^ar-fy2018]

<!-- footnotes -->

[^wiki-huahong]: Wikipedia, *Hua Hong Semiconductor*, retrieved 2026-09-26.
    <https://en.wikipedia.org/wiki/Hua_Hong_Semiconductor>
[^eepw-2006-grace]: 电子产品世界 (EEPW), *赛普拉斯与上海宏力达成代工协议* (Cypress and Shanghai Grace reach a
    foundry agreement), 2006 issue 2; copy on fx361.com.
    <https://m.fx361.com/news/2006/0101/29693231.html>
[^hh-prospectus-2023]: 华虹半导体有限公司 (Hua Hong Semiconductor Limited), *首次公开发行人民币普通股（A股）股票并在科创板上市招股说明书（上会稿）*
    (prospectus for the STAR Market listing, committee draft), Shanghai Stock Exchange, 2023-05-10.
    <http://static.sse.com.cn/stock/disclosure/announcement/c/202305/001307_20230510_ETYJ.pdf>
[^fr-2013-veu]: US Department of Commerce, Bureau of Industry and Security, *Addition, Removals, and
    Revisions to the List of Validated End-Users in the People's Republic of China*, Federal Register
    vol. 78 no. 106, 2013-06-03, FR Doc. 2013-13076.
    <https://www.govinfo.gov/content/pkg/FR-2013-06-03/html/2013-13076.htm>
[^hh-fab-naming-2017]: 华虹集团 (Hua Hong Group), *华虹集团集成电路制造工厂启用统一命名* (Hua Hong Group adopts
    uniform names for its IC fabs), 2017-08-10.
    <https://www.huahong.com.cn/?m=detail&id=459>
[^qtp-152604]: Cypress Semiconductor, Automotive Product Qualification Report QTP 152604: *Automotive Generation6 TouchScreen (TSG6_XL) Product Family, S8SPF-10P Technology, HHGrace1*, July 2020;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205000354/https://www.cypress.com/file/278091/download>
[^eet-2005-grace]: Mark LaPedus, *Cypress inks foundry deal with Grace*, EE Times, 2005-12-12.
    <https://www.eetimes.com/cypress-inks-foundry-deal-with-grace/>
[^ar-fy2005]: Cypress Semiconductor Corp., *2005 Annual Report* with Form 10-K, fiscal year ended
    2006-01-01: Item 1, Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2005.pdf>
[^ar-fy2006]: Cypress Semiconductor Corp., *2006 Annual Report* with Form 10-K, fiscal year ended
    2006-12-31: Item 1, Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2006.pdf>
[^qtp-062509]: Cypress Semiconductor, Product Qualification Report QTP 062509: *Neutron Device Family, S4AD-5 Technology, GSMC*, July 2014.
    <https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-062509-psoc21x34-95xx-gsmc-productqualificationreport-en.pdf>
[^eet-2006-c8]: Mark LaPedus, *Cypress transfers 130-nm process to Grace*, EE Times, 2006-07-19.
    <https://www.eetimes.com/cypress-transfers-130-nm-process-to-grace/>
[^qtp-082609]: Cypress Semiconductor, Product Qualification Report QTP 082609: *HX2LP Device Family, C8Q-3R Technology, Fab 5*, June 2009;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201026131537/https://www.cypress.com/file/95566/download>
[^ar-fy2010]: Cypress Semiconductor Corp., *2010 Annual Report* with Form 10-K, fiscal year ended
    2011-01-02: "Manufacturing" section.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2010.pdf>
[^ar-fy2012]: Cypress Semiconductor Corp., *2012 Annual Report* with Form 10-K, fiscal year ended
    2012-12-30: Item 1, Manufacturing, and the note on the pre-payment to Grace.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2012.pdf>
[^qtp-091302]: Cypress Semiconductor, Product Qualification Report QTP 091302: *MoBL Asynchronous SRAM Product Family, RAM42HNHA Technology, Fab5 GSMC*, February 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-091302-mobl-asynchronous-sram-product-family-cy62256-ram42hnha-technology-fab5-gsmc-productqualificationreport-en.pdf?fileId=8ac78c8c93dda25b01953e8470a271d4>
[^qtp-091206]: Cypress Semiconductor, Product Qualification Report QTP 091206: *16 Meg MoBL SRAM Family, Technology R95LD-3R, HHGrace Fab 3*, January, 2015;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201001021848/https://www.cypress.com/file/138641/download>
[^ar-fy2015]: Cypress Semiconductor Corp., *2015 Annual Report* with Form 10-K, fiscal year ended
    2016-01-03: Item 1, Manufacturing.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2015.pdf>
[^qtp-142304]: Cypress Semiconductor, Product Qualification Report QTP 142304: *PSoC4 Family, S8PF-10R, Fab 3 HHGrace*, July 2014, document 001-92842 Rev. *B;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210517161353/https://www.cypress.com/file/138901/download>
[^ifx-qtp-122801]: Infineon Technologies, listing page for Cypress report *QTP 122801: Capsense Device
    Family S8DIN-5R Fab 5 GSMC* (the report itself needs a log-in).
    <https://www.infineon.com/cms/en/product/gated-document/qtp-122801-capsense-device-family-s8din-5r-fab-5-gsmc-8ac78c8c7d710014017d714c885f12e0/>
[^ifx-qtp-141906]: Infineon Technologies, listing page for Cypress report *QTP 141906: Generation 5
    Touch Screen (TSG5_M) Product Family S8P12-10P HHGrace Fab1 (CYTMA4xx / CYTMA5xx)* (the report itself
    needs a log-in).
    <https://www.infineon.com/cms/en/product/gated-document/qtp-141906-generation-5-touch-screen-tsg5-m-product-family-s8p12-10p-hhgrace-fab1-cytma4xx-cytma5xx-8ac78c8c82ce56640182da34ac9669cc/>
[^qtp-164010]: Cypress Semiconductor, Product Qualification Report QTP 164010: *EZ-PD CCG2 USB Type-C PD Controller Device Family, S8PR2-10R Technology, HH Grace Fab 1*, September 2017;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025133935/https://www.cypress.com/file/383716/download>
[^qtp-113005]: Cypress Semiconductor, Product Qualification Report QTP 113005: *64K Serial Non-Volatile SRAM Product Family, S8 Technology, CMI (Fab 4)*, January 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^qtp-123907]: Cypress Semiconductor, Fab Process Qualification Report QTP 123907, 132302, 132301:
    *Metal Stack Change, S8 Technology, Fab 4 CMI*, March 2014, document 001-91369 Rev. **; copy hosted by
    Tokyo Electron Device as an attachment to PIN145273.
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/145273-Qualification_Report.pdf>
[^qtp-021507]: Cypress Semiconductor, Product Qualification Report QTP 021507: *Failsafe Device Family & Options S4AD-5 SONOS Technology, Fab 2*, December 2015.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>
[^qtp-071302]: Cypress Semiconductor, Product Qualification Report QTP 071302: *16 Meg MoBL SRAM Family, Technology R95LD-3R, Fab4*, April 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211130000623/https://www.cypress.com/file/93006/download>
[^qtp-043004]: Cypress Semiconductor, Product Qualification Report QTP 043004: *DDR2-PLL Device Family, C8Q-3R, Fab 4*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205122906/https://www.cypress.com/file/92151/download>
[^eet-2007-hhnec-sonos]: Cai Yan, *Cypress licensing SONOS memory to Hua Hong NEC*, EE Times, 2007-04-17.
    <https://www.eetimes.com/cypress-licensing-sonos-memory-to-hua-hong-nec/>
[^mms-hhnec-sonos]: 国际金属加工网 (mmsonline.com.cn), *华虹NEC获Cypress 0.13微米SONOS NVM工艺授权* (Hua Hong
    NEC obtains a licence for Cypress's 0.13 µm SONOS NVM process), undated.
    <https://www.mmsonline.com.cn/info/91858.shtml>
[^ar-fy2018]: Cypress Semiconductor Corp., *2018 Annual Report* with Form 10-K, fiscal year ended
    2018-12-30: Item 1, Manufacturing, and Executive officers.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/c/NASDAQ_CY_2018.pdf>
