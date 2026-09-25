# Progress: cyhist-corporate (Cypress corporate record, 1982-2010)

Agent: `cyhist-corporate`. Branch/worktree: `topic/cyhist-corporate` /
`.worktrees/cyhist-corporate`. Evidence file: `data/history/corporate.yaml`
(27 records so far). Verifier: this agent's own
`tmp/check_history_quotes.py` (not `tools/check_history_quotes.py` -- no
such shared tool was visible on this branch; see that script's docstring).
Run `uv run tmp/check_history_quotes.py data/history/corporate.yaml` --
currently "27 records checked, 0 problems". Shared fetch cache:
`/home/admin/github/mithro/sky130-process-tech/tmp/cyhist-cache/{filings,web}/`
in the main checkout (not this worktree's own `tmp/`, which holds only this
agent's scripts, per the plan's "Shared fetch cache" note).

## Synthesis: year-by-year timeline, 1982-2011

Record ids below are `corporate.yaml` ids unless marked `[FUY]` (filings.yaml,
an existing dataset this task was told to reuse, not duplicate). SINGLE-SOURCE
marks a line resting on only one source; CONFLICT marks disagreement between
sources; both are also called out in the records' own `notes` fields.

- **1982-12**: Cypress Semiconductor incorporated in California by T.J.
  Rodgers. `cyhist-corp-sec-fundinguniverse`, `cyhist-corp-sec-encyclopedia`
  (one secondary source, republished twice -- see below), corroborated by
  Cypress's own FY2006 10-K's "We were incorporated in California in
  December 1982" (`cyhist-corp-2006-ar-history-grace-complete`). SUPPORTED
  (primary + secondary).
- **1984 (early)**: first product, a 1.2 µm CMOS memory chip.
  `cyhist-corp-sec-fundinguniverse`. SINGLE-SOURCE (secondary only; no
  Cypress filing from 1984 was found -- pre-EDGAR gap, see below).
- **1986-05**: IPO, raised $73M, Nasdaq listing.
  `cyhist-corp-sec-fundinguniverse`/`-encyclopedia`, corroborated by
  Cypress's own FY2006 10-K ("The initial public offering of our common
  stock occurred in May 1986"). SUPPORTED.
- **1986/1987**: Fab 2 (Round Rock, Texas) added as Cypress's second wafer
  fab. `cyhist-corp-sec-fundinguniverse` places it "by [1987]", next to the
  1986 IPO; `cyhist-corp-pr-2007-fab2exit-semidigest` (trade press, 2007)
  says Fab 2 "opened in 1986"; `cyhist-corp-pr-2008-roundrock-warehouse`
  (ConnectCRE) says the Round Rock campus was "open for 20 years" when
  shuttered in 2008, implying an opening around **1988**. **CONFLICT**
  (minor, 1986 vs ~1988) -- not resolved; no primary Cypress source with an
  exact Fab 2 opening date was found.
- **1987-02**: reincorporated in Delaware. `cyhist-corp-2006-ar-history-grace-complete`
  (primary), consistent with the (undated) secondary accounts. SUPPORTED.
- **1988-10**: NYSE listing (symbol CY). `cyhist-corp-2006-ar-history-grace-complete`
  (primary) and `cyhist-corp-sec-encyclopedia`'s "1988: Cypress lists on the
  New York Stock Exchange" (secondary). SUPPORTED.
- **1990 (end)**: Bloomington, Minnesota fab bought from Control Data VTC for
  $14.7 million -- this becomes Fab 3. `cyhist-corp-sec-fundinguniverse`.
  SINGLE-SOURCE for the price and the "Control Data VTC" seller name; no
  Cypress filing checked in this pass gives a purchase price (the FY1993
  10-K only says Fab 3 "commenced operations in 1991",
  `cyhist-corp-1993-10k`, which is consistent but not a confirmation of the
  1990 purchase / VTC seller / price).
- **1991**: Fab 3 (Minnesota) "commenced operations". `cyhist-corp-1993-10k`
  (primary, Cypress's own FY1993 10-K) -- matches
  `docs/plans/filings-index-design.md`'s note that SkyWater's later 10-Ks
  use 1991 for a 26-year captive period. SUPPORTED (this is also the basis
  for `[FUY] cypress-annual-report-fy1993`, reused here).
- **1994-03 / 1994-12**: Fab 4 (Bloomington, Minnesota, 8-inch) construction:
  ground broken August 1994; ten-year operating lease entered December
  1994. `cyhist-corp-1995-ar-cti` (primary, FY1995 annual report). Also
  `[FUY] cypress-annual-report-fy1993`'s own summary already noted the
  August 1994 groundbreaking date from this same later report.
- **1994**: Cypress Semiconductor (Texas), Inc. ("CTI") -- confirmed as
  Cypress's own name for its Texas wafer-fab subsidiary, ~17% owned by
  Altera Corporation as of FY1995. `cyhist-corp-1995-ar-cti`,
  `cyhist-corp-1994-1995-proxy-cmi` (CMI, the Minnesota analogue).
  **Seed claim "Fab 2 is CTI Round Rock, Texas" -- SUPPORTED.** The Altera
  17% ownership detail is SINGLE-SOURCE (not repeated in any other record
  found in this pass).
- **1994-1995**: earliest EDGAR-filed Cypress documents found (a DEF 14A
  proxy, 1994-03-15; another DEF 14A, 1995-05-08 area; an S-8, 1995-05-08).
  No 10-K or 10-Q from this span was found with a genuine (non-redirect)
  Wayback capture in the time available. See "Gaps" below.
- **1995**: Fab 4 (Bloomington) online (per `[FUY]` FY1993 summary: "began
  production in 1995"); an additional lease financing for "Fab IVb" in
  Minnesota entered October 1995. `cyhist-corp-1995-ar-cti`. "Fab IVb" as a
  name is SINGLE-SOURCE.
- **1996 Q1**: Cypress breaks ground on "Fab V" in Round Rock, Texas: a
  planned 225,000 sq ft, 8-inch (200 mm) facility with a 35,000 sq ft clean
  room. `cyhist-corp-1996-ar-fabv-fab1rd` (primary, FY1996 annual report).
  Also described (without the "Fab V"/"Fab 5" name) as "a second wafer fab
  in Round Rock", begun April 1996, by `cyhist-corp-sec-fundinguniverse`.
  **This is the most interesting open puzzle in the whole timeline** -- see
  "Fab 5 puzzle" below.
- **1996 Q3 / 1996-10**: Fab 1 (San Jose) restructured from production to an
  R&D-only facility; Cypress's own Q3 1996 10-Q gives a $9.1M pretax
  restructuring charge and a target to cease San Jose production by
  December 1996 (`cyhist-corp-1996-10q-q3-fab1-rd`, primary, filed
  1996-11-14). Corroborated independently by
  `cyhist-corp-sec-fundinguniverse`/`-encyclopedia` ("In October 1996,
  Cypress shut down its manufacturing facilities at its San Jose
  headquarters"). SUPPORTED (primary 10-Q + secondary, two independent
  accounts of the same event).
- **1996**: Cypress SRAM line widths "currently down to 0.35 microns".
  `cyhist-corp-1996-ar-fabv-fab1rd`.
- **1997**: Fab 2 and Fab 3 run 6-inch wafers, "primarily 0.6-micron"; Fab 4
  (Bloomington) is the newest facility, 8-inch, "1.78 times more chips per
  wafer" than the 6-inch fabs; only 21% of Q4 1997 wafers at 0.5-micron or
  better. `cyhist-corp-1997-ar-fabs` (primary).
- **1997/1998**: plan (announced, per the FY1998 letter, "last year", i.e.
  1997) to shut down Fab 3 (Minnesota, 6-inch) and ramp the new 8-inch Fab
  4. `cyhist-corp-1998-ar-fab3-close-025um` (primary). Matches
  `[FUY] cypress-annual-report-fy1993`'s note that the original Fab 3 "was
  shut down in 1998".
- **1998-03-09**: broad restructuring announced: Bloomington 6-inch fab
  (0.6-micron) to close, production moving to the 8-inch (0.35-micron)
  facility; Round Rock Fab 2 to stop SRAM production; a new "Fab 5", 8-inch,
  planned for Round Rock, "second half of 1999", to run 0.25-micron;
  Thailand test-plant closure, consolidating to Manila. Total charge $85.5M.
  `cyhist-corp-pr-1998-restructure` (EE Times, retrieval caveat -- see
  "Retrieval difficulties" below) -- corroborated on both ends by
  `cyhist-corp-1996-ar-fabv-fab1rd` (the Fab 5 groundbreaking, 1996) and
  `cyhist-corp-1998-ar-fab3-close-025um` (the Fab 3/Fab 4 SRAM transition,
  same year). SUPPORTED (primary Cypress reports both precede and follow
  this trade-press account of the same restructuring).
- **1998 Q4**: 67% of SRAM wafer starts at 0.35-micron or better; first
  revenue on 0.25-micron technology; Programmable Products Division used an
  external wafer foundry for a 0.18-micron logic technology (earliest
  foundry-use statement in this corpus); a 0.25-micron BiCMOS process (25
  GHz bipolar transistors) developed for HOTLink II.
  `cyhist-corp-1998-ar-fab3-close-025um` (primary).
- **1999**: Fab 2 (Round Rock) "expanded" (per `cyhist-corp-pr-2007-fab2exit-semidigest`,
  looking back from 2007). Consistent with, but not a repeat of, the "Fab 5
  ... second half of 1999" plan above -- see the Fab 5 puzzle.
- **1999**: bulk of production moved to 0.25-micron technology (`[FUY]`
  `cypress-annual-report-fy1999`, not independently re-quoted in this
  dataset -- reused from filings.yaml without a new record, since this
  agent's pass through FY1999 found no additional process/fab sentence
  beyond that one already-catalogued line).
- **2000**: FY2000 annual report fetched and cached
  (`filings/ar-fy2000.txt`, sha256 badeaf9e...) -- **this closes the
  FY2000 gap the task specifically asked about**, but no
  process-technology/fab sentence distinct from the FY1999/FY2001 reports
  was found on a first pass (the document is large -- 13 MB PDF -- and was
  only grepped for the standard keyword list, not read closely; flagged
  below as unfinished work, not as "nothing to find"). No corporate.yaml
  record written for it yet.
- **2001**: 0.15-micron ramping in manufacturing; 0.12-micron transferred
  from the San Jose eight-inch R&D fab (Fab 1) to the Minnesota eight-inch
  manufacturing fab (Fab 4); 0.10-micron development initiated at San Jose.
  `cyhist-corp-2001-ar-transfer` (primary; matches and extends
  `[FUY] cypress-annual-report-fy2001`'s summary).
- **2002**: RAM 7 process ramping in Fab 4; RAM 8 introduced in Fab 4,
  reducing SRAM line width from 0.15 µm to 0.13 µm; a SONOS process running
  in Fab 2, reducing its line width from 0.5 µm to 0.35 µm, for embedded
  non-volatile programmable products; 90-nanometer transferred from Fab 1
  (San Jose R&D) to Fab 4; a 0.13-micron SOI joint-development programme
  with Honeywell begun in Fab 4 (October 2002); a 0.20-micron SiGe BiCMOS
  process completed in Fab 4. `cyhist-corp-2002-ar-ram7-ram8-sonos`
  (primary). This is the corpus's first and clearest link of "SONOS" to a
  node (0.35 µm) and a fab (Fab 2) -- but NOT to the name "S4" (see the Fab
  naming section below).
- **2003**: 90-nanometer ramping in manufacturing; 65-nanometer initial
  development at the San Jose R&D facility; SOI/Honeywell programme
  continuing. `cyhist-corp-2003-ar-soi-90nm` (primary).
- **2004**: 90-nanometer now in production at the Minnesota facility (Fab
  4); 65-nanometer in development at San Jose; explicit statement that
  "wafer foundries manufactured the balance" of products alongside the two
  owned fabs (first such statement found, pre-dating the December 2005
  Grace agreement). `cyhist-corp-2004-ar-90nm-prod` (primary).
- **2005-12**: strategic foundry partnership with Grace Semiconductor
  Manufacturing Corporation (GSMC), Shanghai: Cypress to transfer certain
  proprietary process technologies to Grace; wafer purchases expected
  beginning fiscal 2006. `cyhist-corp-2005-ar-grace-flexmfg` (primary),
  `cyhist-corp-pr-2005-grace-deal` (EE Times, 2005-12-12, retrieval
  caveat): Grace to start with the PSoC mixed-signal array on Cypress's
  "S4" technology; Grace's own 130-nm logic process planned for first half
  2006. SUPPORTED (primary + trade press, same event, consistent details).
- **2006-07-19**: Cypress transfers its 0.13-micron **C8** process to Grace
  (Shanghai) in Q3 2006, for USB and clock chips starting early Q2 2007.
  `cyhist-corp-pr-2006-grace-c8-130nm` (EE Times, retrieval caveat).
  **Seed claim verdict: SUPPORTED** (matches the seed's date, node, foundry,
  products and quarter almost exactly).
- **2006**: transfer of the 0.35-micron SONOS process to Grace *completed*
  during fiscal 2006; Cypress began purchasing Grace-made wafers on this
  process. `cyhist-corp-2006-ar-history-grace-complete` (primary; also the
  source, in the same document, of Cypress's own incorporation/IPO/NYSE
  date sentence -- see 1982/1986/1988 above). This 0.35-micron transfer is
  distinct from the 0.13-micron C8 transfer reported by EE Times the same
  year -- two different process generations moved to Grace in 2006.
- **2007-02**: Electronics Weekly: Cypress moving to a "fab lite" model;
  UMC to take over all SRAM manufacturing at 65 nm and below (previously
  Cypress's own 65 nm technology ran at Grace); UMC's existing 130 nm flash
  deal with Cypress to expand to smaller nodes; ~$100M/year R&D savings
  expected (quoting Shahin Sharifzadeh, EVP wafer fabs and technology).
  `cyhist-corp-pr-2007-sram-foundry-ew` (directly fetchable, no caveat).
- **2007-03-05**: EE Times: Round Rock (Fab 2) 150 mm, nearly depreciated;
  Bloomington (Fab 4) 200 mm, upgraded 2001, ~18 months from full
  depreciation; both US fabs "considered for sale"; UMC to produce 65 nm
  SRAM plus PSoC/USB; Grace's 0.4-micron and 0.13-micron processes cannot
  extend to 65 nm. `cyhist-corp-pr-2007-fablite-umc` (retrieval caveat).
- **2007-12-19 (announced) / 2008 (executed)**: Cypress exits Fab 2 (Round
  Rock) by late 2008, moving production to Fab 4 (Bloomington, 200 mm) and
  external foundries; Fab 2 described as a mature 0.35-micron/150 mm (6
  inch) fab, "opened in 1986 and expanded in 1999", 245 workers, making
  legacy USB/programmable-logic/timing/comms devices; Fab 4 "opened in
  1995" as Cypress's first 200 mm facility, ~400 workers, making
  SRAM/specialty memories and CMOS image sensors.
  `cyhist-corp-pr-2007-fab2exit-semidigest` (Semiconductor Digest, directly
  fetchable). Matches `[FUY] cypress-annual-report-fy2008`'s own quote
  ("In December 2007, Cypress's Board of Directors approved a plan to exit
  its manufacturing facility in Texas..."). SUPPORTED (trade press +
  Cypress's own later 10-K).
- **2008**: Fab 2 campus shuttered; "open for 20 years" (implying ~1988,
  see the 1986/1988 CONFLICT above); 200 workers at closure.
  `cyhist-corp-pr-2008-roundrock-warehouse` (ConnectCRE, directly
  fetchable). Later converted to a light-industrial/warehouse park
  ("Round Rock Eagles Nest Industrial", Provident Realty Advisors, ~$23M,
  ~292,995 sq ft across three buildings). **Seed claim "Fab 2 is CTI Round
  Rock, Texas and was later converted to warehouses" -- SUPPORTED** (CTI
  identity from `cyhist-corp-1995-ar-cti`; warehouse conversion from this
  record).
- **2008**: Simtek Corporation acquired by Cypress, bringing nvSRAM products
  and the AgigaTech subsidiary. `cyhist-corp-2008-ar-simtek` (primary,
  extends `[FUY] cypress-annual-report-fy2008`). The FY2008 report frames
  this as a product-line/subsidiary acquisition; it does **not** itself say
  Simtek brought a distinct fab or process technology (see "gaps" on the
  Simtek/SONOS question below).
- **2009**: some nvSRAM devices (the Simtek product line) developed with
  foundry partner UMC; Grace foundry partnership described as ongoing.
  `cyhist-corp-2009-ar-nvsram-umc` (primary).
- **2010**: Cypress names its own 0.13-micron nonvolatile PSoC wafer
  fabrication process **"S8"**; 2011 plan to triple S8 capacity relative to
  Q4 2010 via added Fab 4 (Minnesota) capacity (kept ~50/50
  internal/external) and a second China foundry (already running first
  PSoC wafers, production Q4 2011). `cyhist-corp-2010-ar-s8` (primary).
  **Seed claim "S8 = 130 nm SONOS" -- PARTIALLY SUPPORTED**: S8 = 0.13
  micron (130 nm) nonvolatile PSoC is directly confirmed by Cypress itself;
  no source found in this pass pairs the words "S8" and "SONOS" in the same
  sentence (the SONOS/0.35 µm identity is stated for the *earlier*
  generation in Fab 2, 2002-2006). Likewise **"S4 = 0.35 µm SONOS" is
  UNSUPPORTED** as stated: S4 is confirmed (EE Times 2005) as the process
  used for the PSoC mixed-signal array, but no source gives S4's node as
  0.35 µm or calls it SONOS by name.
- **2011-02-17**: Cypress licenses 130-nm and 65-nm SONOS embedded NVM IP to
  Innopower Technology Corporation (a Faraday Technology subsidiary);
  Cypress's 130-nm SONOS embedded flash IP "has been shipping in high
  volumes ... at several foundries," and is "verified" (not yet high
  volume) on a 65-nm "LL" process. `cyhist-corp-pr-2011-innopower-sonos`
  (Business Wire release, mirrored verbatim by Design & Reuse, directly
  fetchable from the mirror). **Seed claim "Cypress licensed 130 nm and 65
  nm SONOS embedded NVM IP to Innopower in 2011" -- SUPPORTED**, exactly.

## Seed-claim verdicts (summary)

| Seed claim | Verdict | Record(s) |
|---|---|---|
| Fab 2 is CTI, Round Rock, Texas, later converted to warehouses | **SUPPORTED** | `cyhist-corp-1995-ar-cti`, `cyhist-corp-pr-2008-roundrock-warehouse`, `cyhist-corp-pr-2007-fablite-umc` |
| 2006 Cypress began transferring 0.13-micron C8 to Grace (Shanghai), USB/clock chips from Q2 2007 (EE Times 2006-07-19) | **SUPPORTED** | `cyhist-corp-pr-2006-grace-c8-130nm` |
| Cypress licensed 130 nm and 65 nm SONOS embedded NVM IP to Innopower in 2011 | **SUPPORTED** | `cyhist-corp-pr-2011-innopower-sonos` |
| Cypress Fab 4 was bought from Control Data/VTC | **SUPPORTED, but for Fab 3, not Fab 4** -- see "Fab-numbering correction" below | `cyhist-corp-sec-fundinguniverse` (SINGLE-SOURCE for price/seller name) |
| S4 = 0.35 µm SONOS and S8 = 130 nm SONOS ran in high volume in multiple fabs | **PARTIALLY SUPPORTED** -- S8 = 0.13 µm nonvolatile PSoC confirmed by Cypress itself and ran in Fab 4 + China foundries (multiple fabs, confirmed); S4 confirmed only as "the PSoC mixed-signal array" process (no node given); neither is tied to the word "SONOS" in the same sentence by any source found | `cyhist-corp-2010-ar-s8`, `cyhist-corp-pr-2005-grace-deal`, `cyhist-corp-2002-ar-ram7-ram8-sonos` |

### Fab-numbering correction (important for the coordinator's claims matrix)

The seed list says "Cypress Fab 4 was bought from Control Data/VTC". The
evidence found here says the **opposite pairing**: the Control Data VTC
purchase (end of 1990, $14.7M) is Cypress's **Fab 3** (Bloomington,
Minnesota, the company's first Minnesota fab, "commenced operations in
1991" per Cypress's own FY1993 10-K). **Fab 4** is a *separate*, later,
8-inch Bloomington facility that Cypress itself built (ground broken August
1994, per `cyhist-corp-1995-ar-cti`), not acquired. This matters directly
for the pages this evidence feeds: SkyWater's 2017 purchase was of "Fab 4"
(later "Fab 4a"), the *built*, not *bought*, Minnesota fab -- see
`docs/plans/filings-index-design.md`'s existing note to the same effect
under the FY1993 record. Treat the seed's "Fab 4...Control Data/VTC" pairing
as a naming slip to correct in the pages, not a fact to carry forward.

## The "Fab 5" puzzle (flagged for the coordinator / page-writing stage)

Three sources describe what looks like the same Round Rock construction
project under different names and with different implied timing:

1. `cyhist-corp-1996-ar-fabv-fab1rd` (Cypress's own FY1996 annual report):
   "Cypress breaks ground on **Fab V** in Round Rock, Texas" as a Q1 1996
   milestone -- 225,000 sq ft, 8-inch, named explicitly.
2. `cyhist-corp-sec-fundinguniverse` (secondary, same underlying text at
   `cyhist-corp-sec-encyclopedia`): "In April 1996, the company began
   building **a second wafer fab** in Round Rock" -- no fab number given,
   described as delayed by the 1996 memory-market slump.
3. `cyhist-corp-pr-1998-restructure` (EE Times, 1998-03-09): "**Fab 5**, an
   8-inch facility that will be built in the second half of **1999**" --
   i.e., as of March 1998, still not built.
4. `cyhist-corp-sec-encyclopedia` (secondary): as of ~1997, "a fourth Round
   Rock facility scheduled to come online in 1998" -- again no "Fab 5"
   name, and a third implied date (1998, not 1999).

No annual report from FY1997 onward (checked: 1997, 1998, 1999, 2001-2006,
2008-2010) ever mentions "Fab 5" or "Fab V" again; from FY1997 on, "Fab 2"
is used for Round Rock throughout, and `cyhist-corp-pr-2007-fab2exit-semidigest`
(2007) says Fab 2 itself was merely "expanded" in 1999 -- which may be the
same event as the "Fab 5"/"fourth Round Rock facility" project, just folded
into "Fab 2" rather than kept as a separately numbered fab. **This is an
open question for the page-writing stage**: is "Fab 5"/"Fab V" (1996
groundbreaking) the same physical construction as the "fourth Round Rock
facility" (secondary, due 1998) and the "Fab 5... second half of 1999"
(EE Times, 1998), and did it end up being called "Fab 2" (expanded) once
finished, or was a distinct "Fab 5" project cancelled and its site/shell
reused for something else? None of the sources in this corpus resolve it
directly. Recommend the QTP or literature agents' sources be checked for a
"Fab 5" mention before the fabs.md page is drafted.

## Retrieval difficulties

* **EE Times hangs on direct fetch.** Four EE Times URLs
  (`cypress-transfers-130-nm-process-to-grace`,
  `cypress-inks-foundry-deal-with-grace`,
  `cypress-restructures-manufacturing-operations`,
  `cypress-furthers-fab-lite`) all hang until read-timeout under a direct
  HTTP GET with the project user agent ("sky130-process-tech docs
  checker"), and none has a Wayback Machine capture (checked via the
  archive.org `available` API, 2026-09-25 -- all four returned an empty
  `archived_snapshots`). Per rule 11 (agent-briefs.md), the fallback used
  here was Claude's own WebFetch tool, which *can* reach these pages, with
  its extraction saved as the cached text and a retrieval-caveat note on
  each affected record (`cyhist-corp-pr-1998-restructure`,
  `cyhist-corp-pr-2005-grace-deal`, `cyhist-corp-pr-2006-grace-c8-130nm`,
  `cyhist-corp-pr-2007-fablite-umc`). This is a weaker evidentiary footing
  than a directly-fetched or Wayback-captured copy (WebFetch's extraction is
  itself a paraphrase/summary by another model, even though it presents
  some fragments as verbatim quotations), and is flagged as such in every
  affected record's `notes`. A later pass with a real browser (e.g. the
  `claude-in-chrome` tool, not used in this pass to keep scope down) might
  get a raw, independently-checkable copy.
* **BusinessWire returns HTTP 403 to WebFetch and hangs to a direct fetch.**
  Worked around by using Design & Reuse's verbatim mirror of the same press
  release (`cyhist-corp-pr-2011-innopower-sonos`), found via web search and
  fetched directly with no caveat.
* **statesman.com (Austin American-Statesman) is Cloudflare-gated** (a
  direct fetch returns a 3 KB "Client Challenge" JavaScript page); not used
  in any record. Its content (a 2014 real-estate story about the Round Rock
  campus) is superseded for this project's purposes by
  `cyhist-corp-pr-2008-roundrock-warehouse` (ConnectCRE), which covers the
  same site's redevelopment from a different, later story and was
  directly fetchable.
* **theporterco.com's Spansion/Fab 25 project page returns HTTP 404** (dead
  link as given in the seed list); not used. Fab 25 (Austin, ex-AMD, ex-
  Spansion) was not otherwise researched in this pass -- see "Not yet
  researched" below.
* **mouser.com's Cypress PCN PDF failed to parse** (the fetched bytes are
  not a valid PDF -- likely an interstitial/redirect page rather than the
  actual PCN); not used, not retried.
* **researchgate.net (NVSRAM heavy-ion paper) and techinsights.com (Cypress
  CY8CTMA301EES-3 node-assessment page)** were not fetched in this pass
  (both are typically paywalled/teaser pages for commercial reports; likely
  low yield for corporate-history claims specifically, more relevant to the
  literature agent's remit) -- not yet searched, not confirmed inaccessible.
* **annualreports.com 404s, confirmed this pass**: `NASDAQ_CY_1987`,
  `_1988`, `_1989`, `_1990`, `_1991`, `_1992` (all HTTP 404 on a HEAD
  probe, 2026-09-25) -- extends the existing filings.yaml note that 1991-
  1993 were already known 404s. `NASDAQ_CY_1993` is also 404 (the FY1993
  report is filed under `NASDAQ_CY_1994` instead -- see
  `cyhist-corp-1993-10k`'s notes). **`NASDAQ_CY_2000` exists and was
  fetched** (`filings/ar-fy2000.txt`) -- this closes the task's flagged
  FY2000 gap as far as *having a copy*, but no record was written from it
  yet (see "Not yet done" below).

## Gaps (confirmed absent, not just unsearched)

* **Fiscal years 1986-1992**: no 10-K, 10-Q, S-1 or annual report found by
  any means available under this project's rules (annualreports.com: 404
  for all of 1987-1993; EDGAR: mandatory e-filing was still phasing in,
  earliest full-text filing found for Cypress's CIK 791915 is a 1994-03-15
  DEF 14A). A paper-only S-1 for the May 1986 IPO likely exists in SEC's
  physical archives but is not obtainable under the "no sec.gov, no paid
  service" rules of this project.
* **Fiscal year 1994 10-K**: not on annualreports.com (see above); not
  found on EDGAR/Wayback in the time available for this pass (see "Not yet
  done" below -- this is flagged as unfinished search, not a confirmed
  absence, unlike 1986-1992).

## Not yet done (unfinished work, explicitly -- resume here)

1. **FY1994 10-K hunt.** A Wayback CDX listing of `sec.gov/Archives/edgar/
   data/791915/` (the full CIK folder, capped at the API's 500-row limit)
   found accession numbers from 1994 (`0000791915-94-000010`, a DEF 14A;
   `0000315066-94-000316` and `-001044`, filed by a filing agent, not yet
   checked) and 1995 (several), but most candidate `.txt` full-submission
   URLs have only a 301-redirect Wayback snapshot (sec.gov's own later
   URL restructuring), not a genuine 200-status capture; finding the real
   200-status snapshot for each candidate requires a per-URL CDX query
   (`cdx/search/cdx?url=<exact accession url>`), which is slow one at a
   time. Un-checked candidates from the same CDX pull: `0000315066-94-000316`,
   `0000315066-94-001044`, `0000350440-96-000017`, `0000350440-96-000040`,
   `0000791915-96-000004`, `0000791915-97-000004`, `-97-000010`,
   `-97-000012`. Resume by querying each individually for a 200-status
   snapshot, the same way `cyhist-corp-1996-10q-q1`/`-q3` were found.
2. **FY2000 annual report** (`filings/ar-fy2000.txt`, already fetched) has
   not yet been read for process/fab content beyond the standard keyword
   grep, which came back empty on the first (13 MB, likely OCR-heavy) pass
   -- worth another pass with the page-locator approach used successfully
   on `ar-fy2006.txt` (its front matter and body may use different fonts,
   as happened with FY2006).
2b. **FY1999 annual report**: only the pre-existing filings.yaml quote
   ("bulk of its production to 0.25-micron technology") was reused; not
   independently re-read for additional process/fab sentences in this pass.
3. **DEFM14A / most 8-Ks / most proxies, 1997-2010** not searched (only the
   1994/1995 proxies and 1996 10-Qs were pulled from EDGAR/Wayback in this
   pass; the annual-report-to-shareholders documents cover most years'
   process-technology content instead, but 8-Ks specifically announcing
   fab events -- e.g. the actual December 2007 Fab 2 exit 8-K/press-release
   exhibit at `sec.gov/Archives/edgar/data/791915/000119312507271117/dex991.htm`,
   found via web search but not yet located on Wayback -- would be more
   authoritative than the trade-press paraphrases used here).
4. **Acquisitions not yet researched from primary/press sources**: IC
   Designs, Performance Semiconductor, CONTAQ Microsystems (1993-1994, per
   `cyhist-corp-sec-fundinguniverse` only -- SINGLE-SOURCE, not in
   corporate.yaml as a record yet since only the secondary mention exists);
   Anchor Chips; Silicon Light Machines (spun out/acquired ~2000, appears
   only as a subsidiary-list entry so far); Silicon Magnetic Systems
   (created 2002 for MRAM, NVE Corp licence -- secondary only); Ramtron
   (2012, outside this task's core 1982-2010 window, not researched);
   Spansion/Fab 25 (2015, outside the window; the seed's theporterco.com
   link 404s -- an alternative source was not sought in this pass).
5. **Whether Simtek's nvSRAM used a SONOS process** -- the task's brief
   lists Simtek as bringing "nvSRAM/SONOS"; this pass found only the nvSRAM
   product-line acquisition (`cyhist-corp-2008-ar-simtek`) and a UMC
   foundry pairing for some nvSRAM devices (`cyhist-corp-2009-ar-nvsram-umc`),
   with no source stating Simtek's process technology by name -- UNSUPPORTED
   as stated in the brief, not refuted, not yet resolved.
6. **Altera's ~17% ownership of CTI** (found in the FY1995 annual report,
   `cyhist-corp-1995-ar-cti`) is SINGLE-SOURCE; an Altera SEC filing from
   the mid-1990s might corroborate or date this investment -- not searched.
7. **researchgate.net / techinsights.com / mouser.com PCN** -- see
   "Retrieval difficulties" above; not resolved.
8. **Fab 25 (Austin, ex-AMD, ex-Spansion) history** not researched in this
   pass at all (out of the 1982-2010 core window; the task named it as an
   example of an acquisition-linked fab, so at least a placeholder record
   may be wanted by the page-writing stage) -- the kvue.com Infineon/Fab 25
   article from the seed list was also not fetched.

## Counts

* 27 records in `data/history/corporate.yaml`, covering: 1 pre-EDGAR 10-K
  (FY1993, reused from filings.yaml with new quotes added), 2 EDGAR proxy
  statements (1994, 1995 -- one record for both, same text), 2 EDGAR 10-Qs
  (Q1 and Q3 1996), 13 annual reports (FY1995-1999, 2001-2006, 2008-2010),
  7 trade-press articles (EE Times x4, Electronics Weekly, Semiconductor
  Digest, ConnectCRE), 1 press release (Innopower/SONOS, via a direct
  mirror), 2 secondary company-history references (FundingUniverse and
  Encyclopedia.com -- explicitly noted as one underlying Gale source, not
  two independent ones).
* 33 documents fetched and cached in total under
  `tmp/cyhist-cache/{filings,web}/` (some not yet turned into records: the
  FY2000 annual report, the FY1993 duplicate probe, several CDX/availability
  probe files, two failed fetches (mouser PCN, theporterco 404)).
* 0 verifier problems (`tmp/check_history_quotes.py`, "27 records checked,
  0 problems").
* 5 seed claims addressed: 4 SUPPORTED outright (CTI/Fab 2/warehouses;
  C8-to-Grace 2006; Innopower 2011; -- and the Fab 4/Control-Data-VTC seed
  claim is corrected to Fab 3, see above), 1 PARTIALLY SUPPORTED (S4/S8).

## Tools

* `tmp/fetch.py` -- fetch-and-cache helper (User-Agent "sky130-process-tech
  docs checker"; refuses sec.gov; paces 4s between requests; gives up (does
  not loop) after 3 tries on HTTP 429/503; extracts PDF text via pypdf and
  HTML text via a tag-stripping regex, matching the general approach of
  `tools/check_filings.py`'s `fetch`/`document_text`).
* `tmp/check_history_quotes.py` -- this agent's own verbatim-quote checker
  (see its docstring for why it is not `tools/check_history_quotes.py`).

## How to resume

1. Read this file and `data/history/corporate.yaml`.
2. Run `uv run tmp/check_history_quotes.py data/history/corporate.yaml` to
   confirm the baseline still passes.
3. Pick an item from "Not yet done" above (the FY1994 10-K hunt and the
   FY2000/FY1999 re-reads are the highest-value next steps for closing the
   task's explicitly-named gaps).
4. Add new records to `data/history/corporate.yaml`, re-run the verifier,
   fix any quote mismatches (usually PDF-extraction stray spaces or a
   wrong-year sentence copied from an adjacent year -- see the fix history
   in this file's git log for examples), update this progress file's
   timeline/gaps/counts sections, commit, push.
