# Progress: QTP evidence, round 2 (agent cyhist-qtp2)

Restartable checklist/log for extending `data/history/qtp.yaml` beyond the
24 records left by round 1 (`docs/plans/progress-cyhist-qtp.md`). Read that
file, `docs/plans/cypress-history-plan.md` and `docs/plans/agent-briefs.md`
(lines 1-67) before resuming. Checker: `uv run tools/check_history_quotes.py`
(0 problems as of the last commit; 210 quotes across 50 documents).

## Status: 50 documents (24 from round 1 + 26 new this round)

New IDs added this round, in the order fetched: qtp-012801 (R7LD-1.8),
qtp-096411 (P26), qtp-032301 (ProMOS S17), qtp-082506 (R52T-3), qtp-099202
(R52D-3), qtp-062201 (R52LD-3), qtp-080608 (L28/TSMC-2A), qtp-110605
(L28/TSMC-2A), qtp-012705 (R52FFD-3), qtp-097132 (R32), qtp-053301
(L8C-3R/C8Q-3R), qtp-s050001 (TSMC 0.35um, Fab 3), qtp-051501 (PowerChip
0.165um), qtp-032005 (B53D-3RF), qtp-051101 (B55SGT), qtp-043004 (C8Q-3R),
qtp-042806 (S4ADLatch/S4AD-5), qtp-051005 (S4AD-5CTI), qtp-011503 (L28,
Fab 2), qtp-098333 (L28, Fab 2), qtp-099034 (L28EPD), qtp-032003 (R9T-3R),
qtp-098021 (R32D), qtp-062509 (S4AD-5, GSMC), qtp-098462 (R52D-5R,
"Skywater" reissue), qtp-i000005 (CSM/Chartered 0.35um, G35C).

## Routes used this round

1. **Coordinator's archived-library map** (`tmp/cyhist-cache/web/qrpages-map.jsonl`,
   growing throughout this session from ~57 to 278+ lines) cross-checked
   against `tmp/cyhist-cache/web/cdx-cypress-file-pdfs.txt` for an archived
   `/file/<id>/download` PDF, fetched via Wayback at the required pace
   (>=10 s between requests, never looped on errors). This found: R7LD-1.8,
   P26, ProMOS S17 (early in the session), then later TSMC Fab3 0.35um,
   PowerChip 0.165um, B53D-3RF, B55SGT, C8Q-3R, S4ADLatch, S4AD-5CTI, two
   Fab2/L28 reports, L28EPD, and R32D. One archived-PDF fetch (file id
   94071, an L28EPD page) returned a Wayback "no capture" placeholder
   despite a 200 in the CDX list; not retried further per the
   don't-loop rule. A single CDX API lookup was tried once each for two
   other un-archived file ids (94396 Tower 0.6um -- 504 gateway timeout;
   93196 ProMOS S12 -- empty result) and not retried.
2. **Direct `infineon.com` fetches from WebSearch hits.** Confirmed this
   round that `/dgdl/...` URLs 301-redirect to the public
   `assets/row/public/documents/...` mirror rather than to `sso.infineon.com`
   login in most cases (round 1 had only seen the gated redirect) -- the
   gating is still per-document, not per-URL-family. This route found:
   R52T-3, R52D-3, R52LD-3, both L28/TSMC-2A reports, R52FFD-3, R32, L8C-3R,
   R9T-3R (fills the round-1 "404" gap for a standalone R9T-3R report, under
   a different QTP number), R52D-5R (a 2019 reissue, `infineon.cn` host),
   and the CSM/Chartered 0.35um (G35C) report. Two `/dgdl/` URLs (S8DIN-5R
   QTP 130702; S4CAP QTP 081401 on both `.cn` and `.com`) confirmed gated
   (redirect to `myInfineon Login`) or 404, matching round 1's pattern for
   S8 variants.
3. **cypress.com qualification-report pages fetched directly (not via
   Wayback).** These now 301-redirect to a generic Infineon product-family
   landing page (`utm_campaign=...&redirId=...`), not to the document
   itself -- a dead end post-migration; the R32D standalone page found this
   way could not be resolved this way (its Wayback-archived cousin page,
   found later via the coordinator's map, worked instead).
4. **Distributor mirrors**: not tried this round (WebSearch + the growing
   archived-library map were productive enough).

## Summary table -- ALL technologies in qtp.yaml (50 documents)

Design rule and gate oxide are given as printed (font/OCR quirks noted in
the individual records, not repeated here). "Reports" counts documents in
qtp.yaml, not qualification-history rows.

| Code(s) | Earliest dated qual | Latest dated qual | Fab(s)/location(s) | Wafer process ID (as printed) | Metal layers | Design rule | Gate oxide | Example parts | Reports |
|---|---|---|---|---|---|---|---|---|---|
| S4AD-5 (+ "S4ADLatch", S4AD-5CTI as a sibling) | Apr 01 (QTP 010702) | Jul 2015 (QTP 151005) | Fab 2 (Round Rock, TX); HHGrace (Shanghai); GSMC (Shanghai) | Fab2/S4AD-5; HHGrace S4AD-5; S4AD-5 GSMC SONOS | 2 | 0.5 µm (qtp-021507 only) vs 0.35 µm (4 other reports: qtp-042806, qtp-051005/CTI, qtp-151005, qtp-062509) | 110 Å (7 Å in one report, see inconsistencies) | CY26049*, CY2414ZC, CY5048WAF, CY8C21x34, CY8C24x94 | 5 |
| S4AD-5CTI | not fixed (no "New Technology" row found) | Aug 05 (QTP 051005 content) | Fab 2 (Round Rock, TX) | Fab2, S4AD-5CTI SONOS | 2 | 0.35 µm | 110 Å | CY8C21334/534 | 1 |
| R42D (incl. "R42LDHA") | Oct 97 (QTP 97211) | May 2017 reissue | Fab 4 (Bloomington, MN) | Fab4/R42D | 2 (Proprietary in 2017 reissue) | 0.35 µm (redacted in reissue) | 70 Å | CY2213ZC-1, CY7C4255V family | 2 |
| R42HD | Nov 97 (QTP 98064) | Jul 2014 reissue | Fab 4 / CMI (Bloomington, MN) | Fab4/R42HD | 2 | 0.42 µm | 110 Å | CY7C024E, CY7C09xxx(V) | 2 |
| RAM42 (RAM42HHA/RAM42HNHA) | Jun 03 | Oct 09 (transfer to GSMC) | Fab 4 (Bloomington, MN) -> GSMC (Shanghai) | Fab4/RAM42 | 1 | 0.42 µm | 110 Å | CY62256 | 2 |
| RAM8NLD-1.8 (+ "R8LD-1.8V") | Mar 03 | Feb 2025 reissue | Fab 4, named Cypress (2013 report) or "Skywater" (2025 reissue of the same 2004 event) | Fab4/RAM8NLD-1.8V | 2 (Proprietary in reissue) | 0.13 µm (redacted in reissue) | 26 Å | CY62125-8DV* | 2 |
| R28 | Sep 1996 (no history table) | Aug 2016 reissue | Fab 3 (Bloomington, MN) -> Fab 2 (Round Rock, TX), transfer dated Mar 1999 | Fab3/R28; Fab2/R28 | 2 | 0.65 µm (all agree) | 165 Å | CY7C024/025/0251, CY7C194/195/199 | 4 |
| P26 | not fixed (no history table) | May 1997 (content) | Fab 2 (Round Rock, TX) | Fab 2/ P26 | 2 | 0.65 µm | 165 Å | CY27C256A, CY27C512 | 1 |
| R32 | not fixed (no "New Technology" row) | Jun 03 (content) | Fab 4 (Bloomington, MN) | Fab4/R32 | 1 | 0.5 µm | 145 Å | CY62256, CY62256V | 1 |
| R32D | not fixed (no history table) | Jul 1998 (content, "5% Shrink") | Fab 4 (Bloomington, MN) | Fab4/R32D | 2 | 0.5 µm | 145 Å | CY7C109/1009 | 1 |
| L28 (Cypress Fab2) | Apr 98 (QTP 97403, "New Technology L28") | Aug 2003 (content) | Fab 2 (Round Rock, TX) | Fab2/L28 | 2 | 0.65 µm | 145 Å | CY2287PVC, CY28158 | 2 |
| L28EPD | not fixed (no history table) | Mar 1999 (content) | Fab 2 (Round Rock, TX) | Fab2/L28EPD | 2 | 0.65 µm (identical figures to plain L28) | 145 Å | CY54/74FCT543T | 1 |
| L28 (TSMC-2A) | May 2003 (QTP 99285, transfer) | May 2011 (content) | TSMC-2A, Taiwan (transferred from Cypress CTI Fab 2) | TSMC-2A/L28 TSMC | 2 | 0.65 µm | 125 Å | CY2077, CY5037, CY2305ES | 2 |
| R7FT-3R | Feb 02 (QTP 014807) | Dec 02 (QTP 023101) | Fab 4 (Bloomington, MN) | RAM7FT-3R (sic) | 3 | 0.18 µm | 32 Å | CY7C0831V-0853V | 2 |
| R7FD(-3R) | Dec 01 (QTP 011305) | Jan 2014 reissue | Fab 4 (Bloomington, MN) | Fab4/R7FD-3R | 2 | 0.15 µm | 32 Å | CY7C1018CV33 | 1 |
| R7LD-1.8 (Die Fab Line ID drops to "R7-1.8") | Jun 01 (QTP 012411) | Oct 2004 (content) | Fab 4 (Bloomington, MN) | Fab4/R7-1.8 | 2 | 0.16 µm | 32 Å | CY62146/7CV18 | 1 |
| R9Q-3R (R9T-3R referenced) | Sep 04 (QTP 033302) | Jun 2014 reissue | Fab 4 (Bloomington, MN) | Fab4/R9Q-3R | 4 (table) vs "Triple Metal" (text) -- internal mismatch | 90 nm | 22 Å nitridized SiO2 | CY7C1302-1394 | 1 |
| R9T-3R | not fixed (both rows are device quals) | Aug 2014 reissue | Fab 4 (Bloomington, MN) | Fab4/R9T-3R | 3 (table and text agree) | 90 nm | Nitridized SiO2, thin/thick GOX (truncated) | CY7C1440-1465AV | 1 |
| R95LD-3R | Mar 07 (QTP 071103) | Jul 2014 (QTP 134803) | Fab 4 (Bloomington, MN) | Fab4/R95LD-3R | 2 | 0.09 µm | 28 Å | CY62136-62148 | 2 |
| C9FD-3R | Mar 06 (QTP 052207) | Feb 12 (QTP 114503) | Fab 4 (Bloomington, MN) | Fab4/C9FD-3R | 2 | 0.09 µm | 23 Å | CY7C106D-1021D | 1 |
| R52T-3 | May 03 (QTP 024604, "Process Derivative Qual", ref. only) | Sep 2014 (content) | Fab 4 / CMI (Bloomington, MN) | Fab4/R52T-3 | 3 | 0.25 µm | 55 Å | CY28437, CY24291-93 | 1 |
| R52D-3 | Sep 99 (QTP 99202, own row, no "New Technology" wording) | May 2014 reissue | Fab 4 (Bloomington, MN) | Fab4/R52D-3 | 2 | 0.25 µm | 50 Å | CY7C09569V/79V | 1 |
| R52LD-3 | Apr 99 (QTP 99075, "New Technology R52LD-3") | Jun 2014 reissue | Fab 4 (Bloomington, MN) | (die id printed instead of a process code) | 2 | 0.25 µm (via "R52 TDR (01-30065)") | 55 Å | CYDMX256A16 family | 1 |
| R52FD-3 | Oct 00 (QTP 000505, referenced only, not independently retrieved) | -- | Fab 4 (Bloomington, MN) | -- | -- | -- | -- | CY7C1021BV33 (pre-transfer) | 0 (referenced) |
| R52FFD-3 | Jun 01 (QTP 011205, "New Technology Derivative") | Jun 2014 reissue | Fab 4 (Bloomington, MN) | Fab4/R52FFD-3 | 2 | 0.25 µm | 55 Å | CY7C1021BV33, CY7C1019BV33 | 1 |
| R52D-5R (title also "R5D-5R") | Apr 00 (QTP 000301, "New Technology Derivative") | Mar 2019 reissue | Fab 4 originally; "Skywater -- Bloomington, MN" in the 2019 reissue | Skywater/R52D-5R | Proprietary (redacted) | Proprietary (redacted) | Proprietary (redacted) | CY7C106B/109B family | 1 |
| L8C-3R | Sep 06 (own row; a "Technology Derivative of the C8 Technology") | Jun 2013 (content) | Fab 4 / CMI (Bloomington, MN) | Fab4, L8C-3R | 4 | 0.13 µm | 32/55 Å (DGOX) | CY5077, CY22M1/U1 | 1 |
| C8Q-3R | Jan 05 (QTP 042106, "New C8Q-3R Technology") | Mar 2007 (content) | Fab 4 / CMI (Bloomington, MN) | Fab4, C8Q-3R | 4 | 0.13 µm | 32/55 Å (DGOX) | CY2SSTU877 | 1 |
| B53D-3(RF) | Aug 00 (QTP 99256, "New Technology, B53D-3") | May 2005 (content) | Fab 4 / CMI (Bloomington, MN) | Fab4 / B53D-3 | 2 | 0.25 µm | 55 Å | CYWUSB6932/4/5/41 | 1 |
| B55SGT (+"B55SGT18A"/"B55SG") | May 03 (QTP 015104, "New Technology B55SGT18A") | May 2005 (content) | Fab 4 / CMI (Bloomington, MN) | Fab 4/ B55SGT | 3 | CMOS (0.21-0.35 µm), SiGe Bipolar | 45 Å | CY2DP3110, CY2DP314 | 1 |
| S8 / S8TNV-5R | Nov 2008 (QTP 071304, "S8 SONOS technology") | Nov 2012 (QTP 113005) | CMI / Fab 4 (Bloomington, MN) | Fab4 / S8TNV-5 | 3 | 0.13 µm | 110 & 32 Å (dual gate oxide) | CY14MB064*, CY14B104L/N | 1 |
| 0.5um TLM (Hyundai) | Aug 00 | Jan 2001 | Fab HME = Hyundai Electronics, Cheongju, Korea | CF4 / HL50 | 3 | 0.5 µm | 95 Å | CY7C09449PV-AC | 1 |
| TSMC 0.35um (Cypress-owned "Fab 3" label at TSMC) | Dec 03 (QTP S050001, "New Technology") | Jun 2005 (content) | TSMC | Fab 3 (most fields left blank) | 5 | not printed (title/text only) | not printed | ASIC (SMaL Camera) | 1 |
| PowerChip (0.165um brief name; printed "0.16um + Stack Capacitor") | Mar 05 (sort-site qual, not the technology's own origin) | May 05 (content) | Powerchip Semiconductor Corp, HsinChu, Taiwan (+ CMI sort site) | BF04301 | 2 | 0.16 µm + Stack Capacitor | 72 Å | K002MC5BW, GC2016V5BW | 1 |
| ProMOS S17 | Feb 03 (QTP 020606, "New Technology S17") | May 04 (content) | ProMOS Technologies, Taiwan | U016TFF | 2 | 0.17 µm | 62 Å | CYU001M16TFFA family | 1 |
| ProMOS S12 | not retrieved (page found, PDF not archived) | -- | ProMOS Technologies, Taiwan | -- | -- | -- | -- | CYU01M1SCE/16FE | 0 (page only) |
| Tower 0.6um | not retrieved (page found, PDF not archived; one CDX lookup timed out) | -- | Tower Semiconductor, Israel | -- | -- | -- | -- | (Low EMI Spectrum Spread Clock) | 0 (page only) |
| CSM/Chartered 0.35um (G35C) | dated "2000" in its own history row | Oct 2013 (content) | Chartered Semiconductor Singapore ("Fab 2" in Cypress's own numbering) | 2L313-698-CBB/CRA | 3 | 0.35 µm | 65 Å | CY29972, CY29973, CY28346 | 1 |
| IMI-acquired foundry technologies (TS60D/RX11/KB14, RF06 -- Tower Israel; CMOS5SF/ZB15/ZB17 -- IBM NY; "CSM"/A35C-G35C -- Chartered Singapore) | Feb 2001 (acquisition) | Mar 2007 (latest device addition) | Tower (Israel); IBM (New York); Chartered (Singapore) | not printed (summary document) | 2 (RF06/ZB15/17); 3 (A35C-G35C) | 0.6 µm; 1.0 µm; 0.35 µm | not printed | CY2LL843*, CY25561/2 | 1 |

Not in the table: qtp-144802 (Test Site Qualification Report, out of scope,
excluded from qtp.yaml entirely, unchanged from round 1).

## Naming evidence (verbatim, with record ids)

Every quote below is copied from a `qtp.yaml` record's `quotes` or `notes`
field; see that record for the exact page/location.

- **R42D-5 / S4AD-5**: "Fab2, S4AD-5 (SONOS), R42D-5 derivative w/ 6
  additional mask" (qtp-021507) -- S4AD-5 is explicitly a derivative of
  R42D-5 with 6 extra masks (round 1 finding, unchanged).
- **R7FT-3R**: "New Technology Derivative R7FT-3R (Hot Al)" (qtp-014807) --
  round 1 finding, unchanged.
- **R52FD-3 -> R52FFD-3**: "Transfer of CY7C1021BV33 from Technology
  R52FD-3 to R52FFD-3" and "New Technology Derivative R52FFD-3, Fab 4"
  (qtp-012705) -- R52FFD-3 is a direct, explicitly-named derivative of
  R52FD-3 (one extra "F").
- **R52D -> R52D-5R**: "New Technology Derivative R52D-5R / New CY7C149B,
  4Meg Async SRAM Product." (qtp-098462) -- R52D-5R is likewise called a
  "Technology Derivative", presumably of R52D(-3).
- **C8 -> L8C-3R / C8Q-3R**: "Qualify L8C-3R Technology Derivative of the
  C8 Technology at Fab4 using CY5077 Device" (qtp-053301) -- L8C-3R is
  explicitly a derivative of a base "C8" technology; the same document's
  own history dates "New C8Q-3R Technology" to QTP 042106, Jan 05
  (independently confirmed by qtp-043004's own "New C8Q-3R Technology"
  row) -- C8Q-3R and L8C-3R are sibling C8 derivatives, and their
  process-description figures (4 metal layers, 0.13 µm, dual gate oxide
  32/55 Å, CMI/Bloomington MN) are identical in the two independently
  retrieved reports.
- **R32 -> R32D**: no report states the derivation explicitly, but R32
  (qtp-097132: "Double Poly, Single Metal", 1 metal layer) and R32D
  (qtp-098021: "Single Local Interconnect, Double Metal", 2 metal layers,
  titled "R32D Technology... 5% Shrink") share the same 0.5 µm design rule
  and 145 Å gate oxide and the same Fab 4 -- consistent with "D" meaning a
  double-metal derivative of the single-metal base code. The same pattern
  (single base code + "D" = a related/derivative code) recurs by name
  across R42/R42D, R52/R52D, R7/R7D-ish codes, but this corpus has no
  report that states the R32/R32D relationship in words -- **this line is
  an inference**, not a verbatim statement.
- **L28 -> L28EPD**: no report explains "EPD"; L28EPD's process-description
  figures (qtp-099034) are byte-for-byte identical to plain L28's at the
  same Fab 2 (qtp-011503, qtp-098333) -- **inference**: EPD is a
  device/option suffix on the same Fab 2 L28 process, not a different
  process.
- **L28 origin and transfer**: "New Technology L28/New Device CY227*"
  (QTP 97403, Apr 98, qtp-011503) at Cypress's own Fab 2, and later "To
  qualify L28-TSMC Technology in TMSC-2A" (QTP 99285, May 2003, qtp-080608)
  -- verbatim confirmation that L28 originated at a Cypress fab and was
  later transferred to the TSMC-2A foundry, five years afterwards.
- **S4AD-5 foundry transfers**: "Qualify HHGrace using PSoC Device Product
  Family on S4AD-5 Technology" (QTP 060605, Aug 06, qtp-151005) and
  "Qualification of GSMC R42 technology..." / "Transfer Neutron Device
  Product Family in S4D-5 Technology at GSMC Foundry" (qtp-062509) --
  S4AD-5 was run at, at minimum, Fab 2, HHGrace and GSMC.
- **RAM42 foundry transfer**: "RAM42 Technology and 7C62256 256K Micro
  Power Asynchronous SRAM Product Transfer from CMI to GSMC Qualification"
  (qtp-091302) -- round 1 finding, unchanged.
- **R28 fab transfer**: "Transfer CY7C0241 (Rev. C, 7C025D chop) and its
  options from Fab3 to Fab2" (qtp-098393) -- round 1 finding, unchanged.
- **Suffix meanings observed directly in the text** (not inferred):
  - "-3", "-3R": appears on R52T-3, R52D-3, R52LD-3, R52FD-3, R52FFD-3,
    R95LD-3R, C9FD-3R, R7FD-3R, R7FT-3R, R9Q-3R, R9T-3R, L8C-3R, C8Q-3R --
    no report defines what the digit/letter means, but it is the single
    most common suffix family in the corpus, always following a
    Bloomington/Fab4-era 0.09-0.25 µm-class code.
  - "-5", "-5R": on S4AD-5, R95LD-3R (already has "-3R"), S8TNV-5R,
    R52D-5R -- likewise undefined in the text.
  - "D": on R42D, R52D-3, R32D -- in every case, the "D" code has more
    metal layers than (or is a straightforward process variant of) a
    plainer sibling code (R42 vs R42D is not directly evidenced in this
    corpus; R32 vs R32D is, see above) -- **partially an inference**.
  - "LD": on R42LDHA (=R42D per qtp-003907's own process block), R7LD-1.8,
    R7LD-3R (referenced, not retrieved), R52LD-3, R52LD-5R (referenced,
    not retrieved), RAM8NLD-1.8 -- consistently used on "Low"-something
    device families (Low Voltage RAM, MoBL Low-power) in the product
    titles; no report defines "LD" itself.
  - "FD", "FT": on R7FD-3R, R7FT-3R, R52FD-3, R52FFD-3 -- FD titles are
    "Fast ... SRAM" (R7FD-3R: "Fast Asynchronous SRAM"), FT titles are
    "Synchronous ... RAM" (R7FT-3R: "Synchronous Dual Port RAM") -- textual
    correlation with product type, not a stated definition.
  - "HD": on R42HD -- title "Synchronous/Asynchronous Dual Port SRAM" --
    no stated meaning.
  - "HA"/"HHA"/"HNHA": on RAM42HHA (Fab4), RAM42HNHA (GSMC) -- appear only
    in cover titles, never in the shared "RAM42" process-description
    heading; no report defines them (round 1 finding).
  - "CTI": on S4AD-5CTI -- qtp-051005's Die Fab Line ID literally appends
    "SONOS" ("Fab2, S4AD-5CTI SONOS"), so "CTI" here modifies an
    already-SONOS S4AD-5 base, most plausibly for "Automotive" given every
    product on this code is an "Automotive PSoC" family -- **inference**,
    not stated.
  - "CAP": on S4CAP -- title only found via search snippet ("S4CAP
    Technology, Fab5"); the PDF was not retrieved (see gaps), so no
    verbatim text is available in this corpus.
  - "Q": on C8Q-3R, R9Q-3R -- both are the higher-metal-layer/QDR-style
    sibling of a plainer "T"-suffixed code in the same family (R9Q-3R vs
    R9T-3R: 4 vs 3 metal layers in this corpus's independently retrieved
    reports) -- title correlation, not a stated definition.
  - "T": on R52T-3, R9T-3R -- R52T-3's own products are all clock
    generators/buffers ("PCI-E Clock Family", "AV Clock Generator");
    R9T-3R's are SRAMs -- no consistent product-type correlation found, so
    no meaning is inferred here.
  - "HA" on B55SGT18A / B53D-3RF's "RF": B55SGT's own history calls the
    base device family "HF Buffer" (High Frequency); B53D-3RF's products
    are all "WirelessUSB...Radio SoC" -- "RF" plausibly stands for the
    radio-frequency product line, but no report states this --
    **inference**.

## Inconsistencies found this round (new; round 1's 13 are unchanged, see
`progress-cyhist-qtp.md`)

1. **S4AD-5 design rule, now 4 reports at 0.35 µm vs 1 at 0.5 µm**:
   qtp-042806 (Fab 2, 2005), qtp-051005 (Fab 2/S4AD-5CTI, 2007),
   qtp-151005 (HHGrace, 2015) and qtp-062509 (GSMC, 2014) all give 0.35 µm;
   only qtp-021507 (Fab 2, 2003) gives 0.5 µm for the same Die Fab Line ID
   ("Fab2, S4AD-5"). With four independent reports now agreeing on 0.35 µm
   across three different fabs, qtp-021507's "0.5 m" reads increasingly
   like a misprint (e.g. a dropped "3") rather than a genuine value, though
   no report says so.
2. **S4AD-5 gate oxide, "7A"**: qtp-042806 prints the gate oxide as "SiO2 /
   7A" for the same Die Fab Line ID ("Fab2, S4AD-5") that qtp-021507 and
   qtp-051005 both give as "110 Å" -- almost certainly a truncated print of
   "110A" (dropped leading digits), not a real value.
3. **R52D-3 heading inside an R52T-3 report**: qtp-082506's
   Technology/Fab Process Description section heading reads "R52D-3" even
   though the report's title, history rows and Die Fab Line ID all say
   "R52T-3" throughout.
4. **R9T-3R heading inside an L28/TSMC-2A report**: qtp-110605's
   process-description heading reads "R9T-3R" -- an unrelated technology --
   even though every other field in the same block matches qtp-080608's
   L28/TSMC-2A description exactly.
5. **S4AD-5 heading inside a CSM/Chartered 0.35um report**: qtp-i000005's
   process-description heading reads "S4AD-5" -- again an unrelated
   technology -- for a report that is otherwise entirely about the
   G35C/Chartered Semiconductor 0.35 µm foundry process. This is the third
   independent example of a stale/mismatched process-description heading
   found in this corpus (see also items 3 and 4), suggesting Cypress's QTP
   template was routinely cloned from an unrelated prior document without
   this one heading field being corrected.
6. **"S4D-5" / "S4D-5CTI" (dropped "A")**: qtp-051005's own Qualification
   Purpose sentence reads "Qualify CY8C21x34 Product Family in S4D-5CTI
   Technology" and qtp-062509's reads "Transfer Neutron Device Product
   Family in S4D-5 Technology at GSMC Foundry" -- both drop the "A" from
   "S4AD-5"/"S4AD-5CTI" in running prose even though their own
   process-description headings and Die Fab Line IDs spell the code out in
   full elsewhere in the same document.
7. **"R5D-5R" (dropped "2")**: qtp-098462's own title page reads "R5D-5R
   TECHNOLOGY, Skywater" while its qualification history and
   process-description heading both say "R52D-5R" in full.
8. **"R9FT-3R" (added "F")**: qtp-032003's Qualification Purpose sentence
   reads "...in qualified technology R9FT-3R, Fab 4" where the title,
   history rows and Die Fab Line ID all say "R9T-3R".
9. **L28 (Fab 2) vs L28 (TSMC-2A): same name, two recipes**: both sites
   give 0.65 µm as the design rule, but their metal compositions,
   passivation and gate-oxide thickness all differ (Fab 2, qtp-011503/
   qtp-098333: Metal1 500 Å Ti/1,200 Å TiW/6,000 Å Al/1,200 Å TiW, 3,000 Å
   TEOS + 15,000 Å Si2N4, 145 Å gate oxide; TSMC-2A, qtp-080608/qtp-110605:
   Metal1 400 Å Ti/1,000 Å TiN/4,700 Å AlSiCu/375 Å TiN, 3,000 Å SiN/3,150 Å
   SOG/1,200 Å SiN, 125 Å gate oxide) -- the same technology name and
   design rule cover two measurably different process recipes at the two
   sites, unlike (for example) R28's Fab3-to-Fab2 transfer, where the
   process figures stayed identical across both sites' reports.
10. **B53D-3 vs B53D-3RF**: qtp-032005's title and its two mask-change
    history rows (041503, 041605) call the technology "B53D-3RF"; its
    process-description heading and Die Fab Line ID both instead say plain
    "B53D-3" -- the same drop-the-suffix-in-running-text pattern already
    noted for R7LD-1.8/R7-1.8 and R42D-5/R42D (round 1).
11. **B55SGT / B55STG / B55SG / B55SGT18A**: within the single document
    qtp-051101, the title says "B55SGT", the earliest history row says
    "B55SGT18A", a later history row abbreviates "55SGT18A", the most
    recent history row says "B55SG", and the process-description section
    heading itself misprints "B55STG" (transposed letters) -- five
    spellings of one technology inside one report.
12. **"Fab 2" and "Fab 3" used for three unrelated fabs each**: this
    corpus's own "Fab 2" now names (a) Cypress's Round Rock, TX site
    (dozens of records), (b) TSMC's foundry line in qtp-s050001 ("Die Fab
    Line ID/Wafer Process ID: Fab 3" for a *TSMC* fab, confusingly labelled
    "Fab 3" not "Fab 2" -- see next point), and (c) Chartered Semiconductor
    Singapore in qtp-i000005 ("Chartered Semiconductor Singapore, Fab 2" in
    the qualification-history description, Cypress's own numbering for a
    foreign foundry). Similarly "Fab 3" names both Cypress's own
    Bloomington, MN site (R28's early reports) and TSMC's foundry line
    (qtp-s050001). No report cross-references these different meanings of
    the same fab-number label.
13. **TSMC 0.35um report is almost entirely blank**: qtp-s050001 leaves
    Metal Composition, Passivation, Free Phosphorus and (most
    strikingly) the Design Rule and Gate Oxide fields themselves blank in
    the source PDF -- the only place "0.35um" appears is in the title and
    qualification-purpose text, not in the Design Rule field that every
    other record in this corpus fills in.

## Gaps: codes named in the brief with no report retrieved (or only
partially retrieved) in this round

- **R5, R3** (as standalone family-root codes): not found as report
  titles anywhere in this pass; "R5" only appears as an apparent
  typo/abbreviation inside "R5D-5R" (qtp-098462, itself really an
  "R52D-5R" report).
- **R63D-25**: no report or page found under this name in any route tried
  (WebSearch, the growing archived-page map, or the cdx-cypress-file-pdfs
  list).
- **S4CAP**: one page found via WebSearch snippet only ("QTP 081401,
  S4CAP Technology, Fab5", document number 001-87789); both a `.cn` and a
  guessed `.com` `assets/row/public/documents` URL 404'd. Not retrieved.
- **S4D-5 (standalone, pre-GSMC-transfer)**: a dedicated page exists in the
  coordinator's archived-page map ("Fab 2 Neuron Chip Network Processor,
  Technology Derivative S4D-5 (CY7C531*)", cypress.com file id 91911) but
  its PDF is not in the archived-file-PDF list; not retrieved. (The only
  S4D-5 text actually retrieved is the misprint inside qtp-062509's
  S4AD-5/GSMC report.)
- **S8DI-5R, S8DIN-5R** (and every other S8 variant except S8TNV-5R):
  confirmed still gated behind `myInfineon Login` this round (QTP 130702,
  S8DIN-5R, Fab4 CMI) -- matches round 1's finding exactly; no new route
  found them public.
- **ProMOS S12**: one page found ("16 Meg MoBL A/D Mux (Rev. C2) Device
  Family (CYU01M1SCE/CYU01M16FE), ProMos S12", file id 93196) but its PDF
  is not archived; a single CDX API lookup for the file id returned an
  empty result (no captures). Not retrieved.
- **Tower 0.6um**: one page found ("0.60um Technology, Tower Semiconductor
  Fab, Low EMI Spectrum Spread Clock", file id 94396) but its PDF is not
  archived; a single CDX API lookup for the file id returned a 504
  gateway timeout (not retried, per the don't-loop rule). Not retrieved.
  (The IMI-acquisition summary report qtp-i000006, already in the corpus
  from round 1, does give Tower Semiconductor a design rule of 0.6 µm for
  its "TS60D/RX11/KB14" base-die platform, so the 0.6 µm figure itself is
  independently corroborated even without this specific report.)
- **UMC 0.35um**: not found. The only UMC-related documents found this
  round are a 65 nm UMC Fab 12A SRAM report (LL65P-18R, clearly a much
  later/finer-geometry generation than S8, out of scope) and a
  modern-template PSoC3/UMC report (QTP 201202) that carries no
  Technology/Fab Process Description block at all (just JESD47 stress-test
  summary tables) -- neither is usable evidence for a "UMC 0.35um"
  technology as named in the brief.
- **TSMC 0.25um**: not found under this specific value; this corpus has
  TSMC at 0.35 µm (Fab 3, qtp-s050001) and TSMC-2A at 0.65 µm (qtp-080608,
  qtp-110605), but no report giving TSMC at 0.25 µm specifically. (One
  search hit, QTP 125101 "TSMC Fab 2B TSMC 0.5 Technology", 404s on every
  URL tried, per round 1's notes -- also not the 0.25 µm figure asked
  for.)
- **Fab 12, Fab 25**: every hit found under these names is from the
  PSoC4/PSoC4S/PSoC5LP/PSoC4100S-Plus era (UMC Fab 12A/12I, Infineon
  "Fab25 S8 Technology Qualification" reports dated well after Cypress's
  April 2020 acquisition by Infineon) -- these read as *later* fabs than
  the "first S8 qualifications" the brief scopes this corpus to, not
  earlier ones; none was fetched, since none looked like it would predate
  or date S8's own origin. Flagged here rather than silently skipped, in
  case the coordinator judges one of these fabs relevant after all.
- **R52LD-5R, R7LD-3R** (referenced but not independently retrieved):
  named in qtp-021507's era search hits and the coordinator's page map
  respectively; the one `/dgdl/` URL tried for R52LD-5R (QTP 032403)
  redirected to the plain infineon.com homepage rather than the document
  (not a login gate, but not the document either); not retried further.
- **L28 Technology Qualification (dedicated page)**: "Fab 2 - L28EPD
  Technology Qualification" (file id 94001) looked like it might be the
  clean "New Technology L28EPD" report, but its PDF is not archived; not
  retrieved. (qtp-011503 already supplies a clean "New Technology L28"
  row for plain L28 at Fab 2, so this gap is for the L28EPD variant's own
  origin date specifically, not for L28 generally.)

## Documents in qtp.yaml after this round (50)

24 from round 1 (unchanged; see `progress-cyhist-qtp.md`) plus, this
round: qtp-012801, qtp-096411, qtp-032301, qtp-082506, qtp-099202,
qtp-062201, qtp-080608, qtp-110605, qtp-012705, qtp-097132, qtp-053301,
qtp-s050001, qtp-051501, qtp-032005, qtp-051101, qtp-043004, qtp-042806,
qtp-051005, qtp-011503, qtp-098333, qtp-099034, qtp-032003, qtp-098021,
qtp-062509, qtp-098462, qtp-i000005.

## Next steps for a resumption

1. Re-check `tmp/cyhist-cache/web/qrpages-map.jsonl` (it keeps growing) for
   R5, R3, R63D-25, S4CAP, S4D-5, ProMOS S12, Tower 0.6um and UMC 0.35um --
   none of these had a mapped, archived PDF as of this session's end, but
   the coordinator's background job may map more pages later.
2. Retry the three known-timed-out/empty single CDX lookups (Tower 0.6um
   file 94396; ProMOS S12 file 93196) after some time has passed.
3. Try mouser.com/PCN and teldevice.co.jp for R5, R3, R63D-25, S4CAP and
   S4D-5 -- not tried in either round yet.
4. If corporate.yaml or literature.yaml turn up Cypress's own naming-
   convention documentation (e.g. an internal spec explaining the R5/R7/R9
   family-number scheme), that would resolve most of the "verbatim
   suffix meaning" gaps left as inferences above.
