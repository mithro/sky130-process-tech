# Progress: QTP evidence (agent cyhist-qtp)

Restartable checklist for `data/history/qtp.yaml`. Read
`docs/plans/cypress-history-plan.md` and `docs/plans/agent-briefs.md`
(lines 1-67) before resuming. Checker: `uv run tools/check_history_quotes.py`
(0 problems as of the last commit; 44 quotes across 24 documents).

## Summary table (derived only from the 24 records in qtp.yaml)

| Technology code(s) | Earliest dated qual | Latest dated qual | Fab(s) | Metal layers | Design rule (as printed) | Gate oxide | Example parts | Reports |
|---|---|---|---|---|---|---|---|---|
| S4AD-5 | Apr 01 (QTP 010702, "New Technology S4AD-5") | Jul 2015 (QTP 151005) | Fab 2 (Round Rock, TX); HHGrace (Shanghai, "Fab5") | 2 | **0.5 µm** (qtp-021507, Fab 2) vs **0.35 µm** (qtp-151005, HHGrace) -- same code, two values | 110 Å SiO2 | CY26049*, CY23FS*, CY8C24794/CY8C24894 | 2 |
| R42D (incl. "R42LDHA" title) | Oct 97 (QTP 97211, "New R42D Technology Qualification") | May 2017 reissue | Fab 4 (Bloomington, MN) | 2 (qtp-003907); "Proprietary" (qtp-097483, 2017 redaction) | 0.35 µm (qtp-003907); redacted in the later reissue | 70 Å SiO2 (qtp-003907) | CY2213ZC-1, CY7C4255V family | 2 |
| R42HD | Nov 97 (QTP 98064) | Jul 2014 reissue | Fab 4 / CMI (Bloomington, MN) | 2 | 0.42 µm | 110 Å SiO2 | CY7C024E family, CY7C09xxx(V) family | 2 |
| RAM8NLD-1.8 (incl. "R8LD-1.8V") | Mar 03 (QTP 031102, "New Technology R8LD-1.8V") | Feb 2025 reissue | Fab 4, named "Cypress Semiconductor -- Bloomington, MN" (2013 report) or "Skywater -- Bloomington, MN" (2025 reissue of the *same* 2004 event) | 2 | 0.13 µm (2013 report); redacted "Proprietary" in the 2025 reissue | 26 Å | CY62125DV*/CY62126-8DV* family | 2 |
| R28 | Sep 1996 (Fab 3 reports, no history table) | Aug 2016 reissue (content dated Nov 1997 / Mar 1999) | Fab 3 (Bloomington, MN) -> Fab 2 (Round Rock, TX), an explicit transfer dated Mar 1999 | 2 | 0.65 µm (all four reports agree) | 165 Å SiO2 | CY7C024/0241/025/0251, CY7C133-146, CY7C194/195/199 | 4 |
| R7FT-3R (title typo "R7FTW-3R" in one reissue) | Feb 02 (QTP 014807, "New Technology Derivative R7FT-3R (Hot Al)") | Dec 02 (QTP 023101) | Fab 4 (Bloomington, MN) | 3 | 0.18 µm | 32 Å SiO2 | CY7C0831V-0853V family | 2 (near-duplicate PDFs, different sha256) |
| R7FD(-3R) | Dec 01 (QTP 011305) | Jan 2014 reissue | Fab 4 (Bloomington, MN) | 2 | 0.15 µm | 32 Å SiO2 | CY7C1018CV33 family | 1 |
| R9Q-3R (R9T-3R referenced, not independently retrieved) | Sep 04 (QTP 033302, "New Technology R9T-3R") | Jun 2014 reissue (content: Mar 05) | Fab 4 (Bloomington, MN) | 4 (composition table) vs "Triple Metal" (design-rule text) -- internal mismatch | 90 nm | 22 Å nitridized SiO2 | CY7C1302-1394 QDR/DDR family | 1 |
| R95LD-3R | Mar 07 (QTP 071103, "8 Meg MoBL...Qualification at Fab 4") | Jul 2014 (QTP 134803) | Fab 4 (Bloomington, MN) | 2 | 0.09 µm (both reports agree; PUA-glyph micron sign in one) | 28 Å | CY62136-62148 MoBL Automotive family | 2 |
| C9FD-3R | Mar 06 (QTP 052207) | Feb 12 (QTP 114503) | Fab 4 (Bloomington, MN) | 2 | 0.09 µm | 23 Å | CY7C106D-1021D, CY7C194D/197D/199D family | 1 |
| RAM42 (RAM42HHA / RAM42HNHA -- cover titles differ from the shared "RAM42" process-block heading; "GSMC R42" in one qualification-purpose sentence) | Jun 03 (QTP 030206, Fab 4) | Oct 09 (QTP 091302, transfer to GSMC) | Fab 4 (Bloomington, MN) -> GSMC (Grace Semiconductor, Shanghai) | 1 | 0.42 µm (both agree) | 110 Å SiO2 | CY62256 family | 2 |
| 0.5um TLM (Cypress's own name; wafer IDs CF4/HL50) | Aug 00 (QTP 001004) | Jan 2001 | Fab HME = Hyundai Electronics, Cheongju, Korea (outsourced, not a Cypress-numbered fab) | 3 | 0.5 micron | 95 Å SiO2 | CY7C09449PV-AC | 1 |
| S8 / S8TNV-5R | **Nov 2008** (QTP 071304, "To qualify S8 SONOS technology... using S8TNV-5R, fabricated at Cypress Minnesota CMI (Fab4)") | Nov 2012 (QTP 113005) | CMI / Fab 4 (Bloomington, MN) | 3 | 0.13 µm | 110 Å & 32 Å SiO2 (dual gate oxide) | CY14MB064*/CY14ME064* NVSRAM, CY14B104L/N | 1 |
| IMI-acquired foundry technologies: TS60D/RX11/KB14 (Tower, Israel), RF06 (Tower, Israel), CMOS5SF/ZB15/ZB17 (IBM, NY), "CSM"/A35C-G35C (Chartered Semiconductor, Singapore) | Feb 2001 (acquisition) | Mar 2007 (latest device addition) | Tower Semiconductor (Israel); IBM (New York); Chartered Semiconductor Manufacturing (Singapore) | 2 (RF06, ZB15/17); 3 (A35C-G35C); not stated (RX11/KB14) | 0.6 µm (TS60D/RX11/KB14); 1.0 µm (RF06); 0.35 µm (ZB15/17, A35C-G35C) | not printed (no process-description block in this document type) | CY2LL843*, CY2SSTV*, CY25561/2, CY7C827042AR | 1 |

Not in the table above: qtp-144802 (Test Site Qualification Report, OSE-Taiwan
assembly/test-site qual, no fab technology named) is excluded from qtp.yaml
entirely -- it is out of scope for this corpus.

## Inconsistencies found (verbatim in the records' `notes` fields; listed here for the coordinator)

1. **S4AD-5 design rule**: qtp-021507 (Fab 2, 2003) prints "0.5 m" (0.5 µm);
   qtp-151005 (HHGrace, 2015) prints "0.35 m" (0.35 µm) for the *same*
   technology code. Neither report explains the difference.
2. **R42D vs R42LDHA**: qtp-003907's cover/title calls the technology
   "R42LDHA"; its own Technology/Fab Process Description heading and Die Fab
   Line ID field both instead say plain "R42D (with Hot AL)" -- the name
   "R42LDHA" never recurs inside the process-description block.
3. **RAM8NLD-1.8 fab-owner name changes between reissues of the same
   historical event**: qtp-024110 (Rev **, June 2013, pre-2017) gives "Cypress
   Semiconductor -- Bloomington, MN"; qtp-041406 (Rev *B, February 2025) gives
   "Skywater -- Bloomington, MN" for the *same* 2004 qualification event, even
   substituting "from Skywater" into the qualification-history description
   text of that 2004 event -- SkyWater did not exist as a company until 2017.
   This looks like Infineon's reissue process back-filling the *current*
   fab-owner name into historical text rather than preserving the original.
4. **RAM42 family naming**: both qtp-030206 (title "RAM42HHA") and qtp-091302
   (title "RAM42HNHA") use plain "RAM42" in their Technology/Fab Process
   Description heading and Die Fab Line ID; qtp-091302's own qualification
   purpose sentence instead calls it "GSMC R42 technology" -- four spellings
   for what appears to be one technology inside one document (qtp-091302).
   qtp-091302's Die Fab Line ID also still reads "Fab4/RAM42" even though the
   same document's title, history and fab-location field all say the product
   transferred to GSMC/Fab 5 -- a stale field.
5. **R9Q-3R metal-layer count**: qtp-051207's Number-of-Metal-Layers field and
   Metal Composition table both show 4 layers, but the Design Rule text in
   the same field reads "CMOS, Triple Metal, 90 nm" -- three vs four layers
   for the same technology in the same document. The qualification-history
   row for this same QTP independently calls it a "4 Metal Layer Process",
   agreeing with the table rather than the "Triple Metal" text.
6. **R7FTW-3R vs R7FT-3R**: qtp-023101's cover title says "R7FTW-3R"; every
   other occurrence in the same document (and in the near-duplicate
   qtp-014807) says "R7FT-3R" -- most likely a typo (stray "W").
7. **RAM7FT-3R prefix**: both qtp-014807 and qtp-023101 give the Die Fab Line
   ID as "RAM7FT-3R" (with a "RAM" prefix), even though every other mention in
   both documents drops it ("R7FT-3R").
8. **IMI/"Fab11" naming**: qtp-i000006's cover title calls a foundry "CMOS5SF
   [Micrus] -- IBM/NY (Fab32)" and "CSM 0.35um Logic Salicide -- Charter
   Semiconductor (Fab11)"; the body's die-qualification-test headings instead
   say only "IBM-NY" (no "CMOS5SF"/"Micrus"/"Fab32") and "CSM - Singapore" (no
   "Charter"/"Fab11") -- the cover page's fab labels do not recur in the body.
9. **Font/Unicode**: three different Private-Use-Area codepoints (U+F06D,
   U+F0B0, U+F0B5) stand in for the micron sign "µ" across different
   documents/reissue templates in this corpus (confirmed byte-for-byte, not
   assumed) -- e.g. qtp-061806 prints "0.09m", qtp-151005 prints
   "0.35 m". `tools/check_history_quotes.py` maps all three so quotes
   can still be written with an ordinary "µ" and verified.
10. **CY63... typo**: qtp-072002's Automotive Marketing Part # line prints
    "CY63136FV30, CY63137FV30, CY63138FV30" (a "63" prefix) where the cover
    page and every other reference use "CY62136/7/8FV30" ("62").
11. **Blank Date column**: qtp-098368's Product Qualification History table
    prints the "Date" column header but no dates in either of its two rows
    (unlike qtp-102101's version of essentially the same history, which dates
    QTP 98064 to Nov 97).
12. **90 nm vs 0.09 µm**: not a contradiction (same value, different units),
    but worth flagging together: qtp-051207 (R9Q-3R) states "90 nm" directly,
    while qtp-061806/qtp-072002 (R95LD-3R) and qtp-063807 (C9FD-3R) state
    "0.09 µm" for their own, differently named, contemporary (mid-2000s) Fab 4
    technologies -- three separate codes at the same geometry.
13. A WebSearch AI-generated summary for qtp-096182 falsely claimed the
    document "documents a technology conversion from BiCMOS to CMOS" -- the
    fetched PDF text contains no mention of BiCMOS at all. Not used as a
    source; recorded as a caution that search-engine summaries in this task
    must be checked against the actual retrieved document, never trusted on
    their own.

No report in this corpus gives a Fab 4 (or CMI/Skywater) location as
"Round Rock, TX" (the R28 reports that do name Round Rock, TX --
qtp-097476, qtp-098393 -- consistently call it Fab 2, not Fab 4), so the
specific "Fab 4 reports that give Round Rock, TX" inconsistency the brief
asked to watch for was **not observed** in this corpus; noted for completeness
rather than left unmentioned.

## Search routes tried

1. **Seeds file** (`tmp/cyhist-cache/seeds-qtp.txt`, main checkout, 36 URLs
   under `infineon.com/dgdl/...ProductQualificationReport...pdf?fileId=...`).
   Result: only 4 of 32 attempted (excluding 3 obviously-modern PSoC6 URLs,
   QTP174005/182809/192102 -- a 40 nm-class ARM Cortex-M0+ node, far later
   than S8 and out of scope) downloaded successfully: qtp-021507 (cached
   before this agent started), qtp-003907, qtp-024110, and qtp-144802
   (excluded -- no technology named, a test-site qual). The other ~27 seed
   URLs all either 404 (6: 060208, 090604, 100203, 114003, 160202, 98516) or
   redirect (still HTTP 200) to `sso.infineon.com` "myInfineon Login" (21) --
   confirmed a *per-document* access restriction in Infineon's DAM, not a
   transient rate limit (re-requesting a working seed URL immediately
   afterwards still succeeded). Wayback CDX has no capture of any dead/gated
   `/dgdl/...fileId=...` URL (checked individually and via the availability
   API for all of them) -- these are Infineon's post-2020-migration URLs, not
   the original cypress.com ones, so there is nothing to archive.
2. **WebSearch for the `assets/row/public/documents` URL family plus a
   technology-code or foundry-name query** (e.g. `infineon.com QTP Cypress
   "R7"`, `"C9"`, `"R28"`, `"HHGrace"`, `"BiCMOS"`). By far the most
   productive route: it surfaced a *different* URL family Infineon serves
   qualification reports from,
   `https://www.infineon.com/assets/row/public/documents/.../infineon-<slug>-productqualificationreport-en.pdf`,
   which for the pre-S8-era documents found this way was almost always
   directly downloadable (not gated) -- the gating in Infineon's DAM is
   per-document, not per-URL-family (a few PSoC4/PSoC6-era documents surfaced
   this way *were* behind `/gated/` or `/cms/en/product/gated-document/`
   paths and were skipped). This route found all 20 non-seed documents in
   qtp.yaml. Search queries tried and their yield: R4/R5/R52/R7/R8/R9 family
   codes (yielded R42D, R42HD, R7FD, R7FT-3R, R9Q-3R, R95LD-3R, R28-Fab3-Fab2
   transfer reports); C7/C8/C9 (yielded C9FD-3R only; no C7 or C8 report
   found); L8/L28 (yielded one L28 hit, `infineon-qtp-081704-...l28...tsmc-2a...`,
   but its URL both on `.com` and `.cn` 404'd -- not retrieved); B53/P26 (no
   hits at all in two separate searches); S4AD/RAM8NLD/S4AD-5 (yielded
   qtp-151005, qtp-041406, plus several gated hits already in the seed list);
   CMOS 0.8/0.65/1.2 micron (yielded qtp-i000006, the IMI-acquisition
   multi-foundry report); BiCMOS/SONOS (yielded qtp-113005, the S8TNV-5R
   report, plus a false-positive AI summary for qtp-096182 -- see
   inconsistency 13); S8DI-5R/S8Q-5R/S8TMC-5R (found QTP 103209, S8DI-5R,
   CapSense Express, Fab4 CMI -- but its only URL is behind `/gated/`,
   confirmed with a login-page fetch, not retrieved); HHGrace/UMC/TSMC
   (yielded qtp-151005 HHGrace; a UMC hit, QTP 203304 PSoC4000S/4700S, judged
   too modern/out of scope and not fetched; a TSMC hit, QTP 125101, Timing
   Technology PC Product TSMC Fab 2B TSMC 0.5 Technology, but both its
   `/dgdl/` and a guessed `assets/row/public/documents` URL 404'd -- not
   retried further per the "don't loop on repeated failures" rule); R5/R52
   alone (no hits distinct from the R9/R28/R7 results already found).
3. **Wayback CDX for cypress.com** (`cdx?url=cypress.com&matchType=domain&filter=original:.*qtp.*\.pdf`)
   -- timed out (504 Gateway Time-out) on the unscoped whole-domain query;
   not pursued further given how productive the WebSearch route already was.
   Exact-URL CDX/availability-API lookups for every dead or gated `/dgdl/`
   seed URL, and for a handful of the 404'd `assets/row/public/documents`
   guesses, returned no captures.
4. **Not tried**: mouser.com/PCN, teldevice.co.jp distributor mirrors (the
   WebSearch route already found far more than could be fully processed in
   the time available, so these were not needed to reach a reasonably broad
   corpus, but they remain an avenue for a resumption to widen coverage
   further, especially for the still-missing S8 variants). The Infineon
   community "How to find QTP" article
   (`community.infineon.com/.../ta-p/249658`) was surfaced but not read in
   detail; it describes searching via `www.cypress.com` support > Quality and
   Reliability, which today redirects into the same infineon.com DAM already
   searched.

## Documents in qtp.yaml (24)

qtp-021507, qtp-003907, qtp-024110, qtp-097483, qtp-102101, qtp-096091,
qtp-098368, qtp-001004, qtp-061806, qtp-072002, qtp-091302, qtp-063807,
qtp-097476, qtp-023101, qtp-011908, qtp-014807, qtp-051207, qtp-i000006,
qtp-041406, qtp-113005, qtp-096182, qtp-030206, qtp-098393, qtp-151005.

Excluded: qtp-144802 (Test Site Qualification Report, no technology named).

## Not retrievable (known to exist, but not usable as a public source)

Gated (redirect to myInfineon Login, confirmed, no Wayback capture):
- Seed list: the automotive S4AD-5/CY8C21X34 report, and QTP 053402, 054603,
  060201, 060401, 063210, 070505, 072402, 072502, 072803, 082201, 083401,
  090706, 092301, 093003, 100102, 102802, 104407, 113905, 123502, 132905,
  202903 -- almost all S4AD-5 PSoC reports and S8DIN-5R/S8P12-10P/S8PF-10R/
  S8TMA-5R/S8_K2 reports, i.e. exactly the technologies and the S8-dating
  reports the brief most wants. This is the single biggest gap in this
  corpus.
- Found via search but gated: QTP 103209 (S8DI-5R, CapSense Express, Fab 4
  CMI); QTP 151403 (S8PF-10R, Fab25 S8 technology qualification).

404, no archive:
- Seed list: QTP 060208, 090604, 100203, 114003, 160202, 98516.
- Found via search: QTP 081704 (L28, TSMC-2A -- both `.com` and `.cn` URLs
  404); QTP 042205 (R9T-3R standalone report -- both a `/dgdl/` and an
  `assets/row/public/documents` URL 404, though R9T-3R's *existence* and its
  Sep 04 qualification date are independently confirmed via qtp-051207's own
  history table); QTP 125101 (TSMC Fab 2B, TSMC 0.5 µm technology).

Technology codes named in the task brief with **no report retrieved at all**
in this pass: R4 (as a standalone code -- only seen as informal shorthand for
R42HD inside qtp-102101), R5, R52, C7, C8, L8, B53, P26, standalone
CMOS 0.8/0.65/1.2 µm outside the IMI report, standalone BiCMOS, "SONOS 0.35",
Fab 1, UMC (as a Cypress/pre-S8 foundry; a UMC hit found is a modern
PSoC4000S/4700S report, judged out of scope), TSMC (a hit exists, QTP 125101,
but 404s), and every S8 variant *except* S8TNV-5R (S8DI-5R, S8DIN-5R,
S8Q-5R, S8TMC-5R, S8P12-10P, S8PF-10R are all named in gated seed URLs but
none was retrieved).

## Next steps for a resumption

1. Retry the still-gated/404 documents after some time has passed, in case
   Infineon's per-document access flags or CDN caching change; do not loop on
   them repeatedly in one sitting.
2. Try mouser.com/PCN and teldevice.co.jp for the missing S8 variants and
   R4/R5/R8/C7/C8/B53/P26 codes.
3. Chase the QTP numbers already named as history-table cross-references but
   not independently fetched: 95226 (original R28 qual, referenced in
   qtp-096091), 042205 (R9T-3R standalone, 404s -- try alternate slugs).
4. If corporate.yaml/literature.yaml (the other two evidence agents) turn up
   Ramtron/F-RAM-era documents, that is the most likely place to find B53/P26
   (Cypress acquired Ramtron's F-RAM business in 2012).
