# Filings index — progress

Status tracker for the task in `docs/plans/TASKLOG.md` ("Financial filings
index pages"), design in `docs/plans/filings-index-design.md`. Update this
file as work proceeds so the task can be resumed at any point. Status
values: `not searched`, `searched` (candidates identified, none/some
fetched), `records added`, `verified` (checker `--online` passes and a
human/agent read the fetched copy against the summary and quotes).

## Checklist by company x form x year

### Cypress Semiconductor Corporation (Fab 4 era through 2019 Infineon merger)

| Form | Years covered | Status | Notes |
|---|---|---|---|
| Annual report / 10-K | FY2003, FY2004, FY2006, FY2007 (as annual-report-to-shareholders), FY2007 (10-K), FY2015 (10-K), FY2016 (10-K) | records added | `cypress-annual-report-fy2003/2004/2006`, `cypress-10-k-2008-03-03` (FY2007), `cypress-10-k-2016-03-02` (FY2015), `cypress-10-k-2017-03-01` (FY2016) |
| 10-K | FY2017 (2018-02-26), FY2018 (2019-02-27) | records added | fab-sale and post-sale 10-Ks in place |
| 10-K | FY2019 (filed 2020, pre-merger final 10-K) | **not retrievable** | design §7: no Wayback capture, no non-EDGAR copy found yet |
| 10-K/A | any | not searched | none found yet |
| 10-Q | Q1 2003 | **not retrievable** | inventory CYP-07; EDGAR only |
| 10-Q | 2017-05-02 (Q1 2017, fab-sale quarter) | records added | `cypress-10-q-2017-05-02` |
| 10-Q | other quarters (2003-2019) | not searched | design scope: only quarters germane to fab/lineage facts are in scope; a systematic sweep of all 10-Qs is not planned unless a specific fact needs one |
| 8-K | 2019 merger announcement/completion | **not retrievable** | design §7 |
| 8-K | 2020-04-16 (Infineon deal closing / deregistration context) | records added | `cypress-8-k-2020-04-16` |
| DEFM14A (merger proxy) | 2019 | **not retrievable** | design §7; only a DEFA14A capture exists, not yet a record |
| 15-12B | 2020 | **not retrievable** | design §7 |
| Auditor reports | FY2003, FY2004, FY2006, FY2007 | records added | all PwC; see `audits.md` once generated |

### SkyWater Technology, Inc. (and Oxbow/CMI predecessors)

| Form | Years/dates | Status | Notes |
|---|---|---|---|
| DRS / DRS/A (confidential draft S-1) | 2020-08-12, 2021-01-20 | records added, **verify pending** | uncommitted diff under review; DRS/A No.1 (2020-09-30) index captured but no document text found |
| S-1 | 2021-03-22 | records added | |
| S-1/A | 2021-04-12 | records added | only one amendment recorded; other S-1/A dates not yet searched |
| 424B4 (prospectus) | 2021-04-22 | records added | |
| 10-K | FY2021 (2022-03-10), FY2022 (2023-03-15), FY2023 (2024-03-15), FY2024 (2025-03-14), FY2025 (2026-03-11) | records added | five consecutive annual 10-Ks in place |
| 10-Q | every quarter 2021-Q1 (2021-05-19) through 2026-Q2 (2026-08-07), 17 quarters | records added | complete self-filed quarterly series (SkyWater files three 10-Qs a year; no Q4 10-Q); found via SkyWater's investor-relations SEC-filings JSON feed (`ir.skywatertechnology.com/feed/SECFiling.svc/GetEdgarFilingList`), which lists every filing with a non-`sec.gov` PDF; the three 10-Q/A's (2023-09-26 x2, 2025-09-22) were checked and excluded per design §1 — each is a certification-only correction that restates no substantive text (matches the design's own "10-K/A that only restates internal-control language" exclusion example) |
| 10-K/A | 2023-09-26 | **excluded, not a record** | same certification-only correction as the 10-Q/A's above; not added per design §1 |
| DEF 14A | 2022-04-19, 2023-04-25, 2024-04-10, 2025-04-08, 2026-04-27 | records added | complete annual-meeting proxy series 2022-2026; the 2026-04-27 proxy is the routine annual meeting, separate from the DEFM14A merger proxy already recorded |
| DEFM14A (IonQ merger proxy) | 2026-03-31 | records added | |
| 8-K | 2022-04-04, 2023-08-04, 2025-02-26, 2025-07-03, 2026-01-26, 2026-07-31 | records added | Fab 25 purchase, other current reports; a systematic sweep of all routine 8-Ks (earnings, officer changes) is still not planned, per design §1's exclusion of routine current reports |
| 8-K/A | 2025-09-15 | records added | |
| EX-99.1 (press release exhibit) | 2026-01-26 | records added | |
| 15-12G (deregistration) | 2026-08-10 | records added | filed as "SkyWater Technology, LLC" after the IonQ merger closed; one holder of record |
| Auditor reports / restatements | KPMG replaced Deloitte & Touche, effective 2024-06-21 | records added | disclosed in the 2026 DEF 14A; found via the 10-Qs' and 10-K/A's continuous Item 4/9A material-weakness disclosures, present in **every** quarterly and annual report from the first 10-Q (2021-05-19, weaknesses as of 2021-04-04) through the 2026-Q2 10-Q (2026-08-07, weaknesses as of 2026-06-28) — i.e. the weaknesses were never remediated across the company's whole public life; by 2026-Q2 the two named weaknesses are "revenue accounting process" and "Fab 25 account reconciliation processes" |
| DoD/RH90 funding, CHIPS Act | records added (as a second quote on `skywater-10-q-2022-11-10`) | found | the 10-Qs' MD&A repeats: a September 2019 DoD contract for "up to $170 million" to build rad-hard (RH90) wafer capability, and a September 2022 DoD award of "up to an additional $99 million"; the CHIPS Act's 25% investment tax credit is also discussed in the FY2023-2024 10-Qs' tax notes as a generic provision, not tied to a SkyWater-specific dollar figure |
| Oxbow/CMI | related-party disclosures in S-1/10-K/proxies | records added (via DEF 14As) | the 2023-2025 DEF 14As give the Oxbow Realty sale-leaseback (Bloomington land and building), its lease payments by fiscal year, and CMI Oxbow's declining ownership share (44.56% in 2023, 27.51% in 2024, 23.23% in 2025); no independent Oxbow/CMI public filings found (Oxbow itself does not appear to be an SEC or other-jurisdiction filer) |

### Infineon Technologies AG

| Form | Years | Status | Notes |
|---|---|---|---|
| Annual report | FY2019, FY2020, FY2021, FY2022, FY2023, FY2024, FY2025 | records added | full FY2019-2025 series now in place; found by web search for the Infineon-hosted PDF (the investor-relations annual-reports listing page itself 404s when fetched directly, so it was not browsed) |
| Half-year reports | none | not searched | design §7 gap |
| German company register (Unternehmensregister) | none | not searched | design §7 gap |

### D-Wave Quantum Inc. (customer, inherited Cypress line-operation agreement)

| Form | Dates | Status |
|---|---|---|
| S-4 (SPAC merger) | 2022-03-15 | records added |
| 8-K | 2023-03-03 | records added |
| 10-K | FY2022 (2023-04-18), FY2023 (2024-03-29) | records added |

### Weebit Nano Limited (partner, ReRAM in S130)

| Form | Dates | Status |
|---|---|---|
| ASX announcement | 2021-09-09, 2023-06-29 | records added | 2021-09-09 is the original SkyWater ReRAM agreement announcement, found as a company-hosted PDF on weebit-nano.com (not the ASX archive itself, which does not go back that far via web search) |
| Annual report (Appendix 4E) | FY2023 (2023-08-25), FY2024 (2024-08-28) | records added | FY2022 annual report still **not searched** |

### IonQ, Inc. (acquirer, 2026)

| Form | Dates | Status |
|---|---|---|
| 10-K | FY2025 (2026-02-25) | records added |
| S-4 (merger registration) | 2026-03-20 | records added |
| 8-K | 2026-07-31 | records added |

### QuickLogic Corporation and other named partners/suppliers

| Company | Status |
|---|---|
| QuickLogic | records added (1): the 10-K for fiscal year 2023 (filed 2024-03-27) names "SkyWater Technologies" (sic) among the foundries QuickLogic depends on. Checked and found nothing in the FY2022 10-K (period ended 2023-01-01, filed 2023, i.e. the one covering the year the RH90 partnership was announced) — grepped its full extracted text for "SkyWater" with zero matches, even though QuickLogic's 2022 press releases name the partnership. QuickLogic's 10-Qs not yet searched. |
| Equipment/materials suppliers naming SkyWater as customer | not searched |
| Technology licensors/partners named in public filings | not searched beyond D-Wave/Weebit Nano/IonQ |

## Gaps and open questions (from design §7, carried forward)

* **Not retrievable without EDGAR** (no Wayback capture, no company copy
  found): Cypress 10-Q/A Q1 2003 (CYP-07), Cypress 2019 8-K and DEFM14A for
  the Infineon merger, Cypress FY2019 10-K (filed 2020) and 10-K/A, Cypress
  15-12B (2020); SkyWater's DRS amendment No. 1 document text (2020-09-30,
  index captured only) and the Process Technology License Agreement
  exhibit itself (exhibit 10.6/10.7 of the S-1/A). Tried the Wayback
  "save now" API for one 2026 SkyWater filing (the 2026-04-27 DEF 14A) when
  no capture existed yet; it returned HTTP 500/504 both times, so that
  filing was instead read from SkyWater's own investor-relations PDF copy
  (which succeeded) — the DEF 14A record is not blocked, only the "save
  now" approach failed as a discovery technique.
* **Accession numbers missing** for IR-feed-only records (2026 SkyWater
  merger filings, D-Wave, IonQ) — feed filing id recorded instead.
* **Dates of annual reports to shareholders / German annual reports** are
  the latest signature date printed in the copy, not a filing date.
* **10-K/A and 10-Q/A excluded, not a gap:** SkyWater's 2023-09-26 10-K/A
  and two 10-Q/A's, and its 2025-09-22 10-Q/A, were fetched and read in
  full; each is a certification-only correction (the 10-K/A "restate[s]
  in its entirety Part II, Item 9A ... for the purpose of filing revised
  certifications ... to correct an inadvertent omission of certain
  language") with no new financial or narrative content, matching design
  §1's own exclusion example ("a 10-K/A that only restates
  internal-control language"). Not added as records; the material
  weakness content they restate is already covered by the surrounding
  original 10-K/10-Qs.
* **Not yet searched:** QuickLogic's 10-Qs; other named
  partners'/suppliers' 10-Ks; equipment and materials suppliers naming
  SkyWater as a customer; Infineon's half-year reports and the German
  company register; Weebit Nano's FY2022 annual report; Cypress's 2019
  merger communications beyond one DEFA14A capture.
* Whether exhibits (purchase agreements, line-operation amendments) should
  be separate records or folded into their parent filing — still open.
* **New relationship tag added:** `skywater-governance` ("SkyWater's
  auditor appointments, material weaknesses and restatements as a public
  company"), added to `tools/check_filings.py`, `tools/gen_filings.py`
  (`REL_GROUPS`) and the design doc, because the brief's request for
  "auditor changes, material weakness or restatement disclosures" did not
  fit any of the existing controlled tags.

## Round 3 — independent review findings (`tmp/review-index-filings-r1.md`)

| Id | Severity | Status | Note |
|---|---|---|---|
| FIL-R1-01 | High | mostly fixed | Added 14 Cypress records (FY1993, 1995-1998, 2001, 2002, 2005, 2008-2013). Remaining Minnesota-fab-era years (FY1991-1992, 1994, 1999-2000, 2019, plus the previously-known EDGAR-only 2003 10-Q/A, 2019 merger 8-K/DEFM14A, 2020 10-K/A and 15-12B) are declared with reasons in `known_gaps`, rendered on `index.md`. FY2014 has a public copy but says nothing about the Minnesota fab, so it stays a declared gap rather than a record, per design section 1's inclusion rule. |
| FIL-R1-02 | Medium | fixed | Added `notes` cross-referencing the other figure on all four records (`skywater-drs-2020-08-12`, `skywater-s-1-2021-03-22`, `skywater-10-k-2025-03-14`, `skywater-10-k-2026-03-11`). |
| FIL-R1-03 | Medium | fixed | (inherited from the earlier session) `f"(filing-{r['id']})="`, no nested f-string. |
| FIL-R1-04 | Medium | fixed | (inherited) case-sensitive `normalise()`; `fragments_match_in_order()` requires ellipsis fragments in order within `FRAGMENT_MAX_GAP` (4000 chars). |
| FIL-R1-05 | Medium | fixed | (inherited, with a bug found and fixed this session) `check_location()` and `check_metadata()` added. `_drop_toc_runs`'s 700-character gap threshold falsely dropped three genuine, tightly-spaced Part III item headings on `skywater-10-k-2026-03-11` (Items 10-15 are one-sentence stubs there), misreporting the Item 15 exhibit-index quote as nearest Item 12; tightened to 200 characters (real TOC entries in the record checked are all under 150 characters apart) and re-verified clean. |
| FIL-R1-06 | Medium | fixed | Added the auditor's report for all 15 records the reviewer listed (2 Cypress, 7 Infineon, 2 D-Wave, QuickLogic, IonQ, 2 Weebit Nano); `audits.md` now lists 43 reports (was 13). |
| FIL-R1-07 | Low | fixed | (inherited) `related_docs` line no longer appends a second full stop. |
| FIL-R1-08 | Low | fixed | (inherited) `company_keys_in_order()` drives the "By company" counts line. |
| FIL-R1-09 | Low | fixed | (inherited) `company_keys_in_order()` raises `SystemExit` on an uncovered `company_key`. |
| FIL-R1-10 | Low | fixed | Reworded both timeline headlines to what the cited filing itself supports (see session log). |
| FIL-R1-11 | Low | partially fixed | (inherited) `--online` now reports "no fetchable copy" instead of silently skipping. Cache-staleness / re-fetch-after-N-days not implemented (declined for this session: no record's cached copy is known to have changed, and the 1-in-5 external link sample the reviewer ran already found every non-`sec.gov` URL live). |
| FIL-R1-12 | Low | fixed | (inherited) `parent` renders as "Amends/filed with: {ref}`...`"; `period.label` still not rendered for 8-Ks (accepted as a minor cosmetic gap, not required by the design's entry format). |
| FIL-R1-13 | Low | fixed | Added the `known_gaps` dataset list, checker validation and a "Known gaps" section on `index.md`, grouped by company. |
| FIL-R1-14 | Low | fixed | (inherited) `by-year.md`'s introduction explains that some `filed` dates are signature dates. |
| FIL-R1-15 | Low | declined for this session | `supplier-names-skywater` and `ad-hoc-announcement` remain unpopulated; finding a compliant (non-EDGAR) copy for either is genuinely new research, not a fix to existing records, and was out of time this session. Design doc section 7 now names them explicitly as not-yet-searched rather than leaving them silently empty. |

Each row is updated to `fixed` (with what was done) or `declined` (with why) as the
session works through them; see the session log below for detail.

## Round 4 — independent review findings (`tmp/verify-index-filings-r3.md`)

| Id | Severity | Status | Note |
|---|---|---|---|
| V-01 | Medium | fixed | `cypress-annual-report-fy2008` quote 1: `location` Item 7 -> Item 1, Business, Manufacturing. Verified independently against the cached PDF (sentence occurs once, on the page between the Item 1 and Item 2 headings). |
| V-02 | Medium | fixed | `cypress-annual-report-fy2001` quote 1: `location` "Notes to Consolidated Financial Statements" -> "Management's Discussion and Analysis, Research and development". Verified independently: the sentence sits on printed page F-6 (PDF p16), before the Notes section, which starts on F-22 (PDF p32). |
| V-03 | Medium | fixed | `cypress-annual-report-fy2005`'s summary/notes invented a footprint "disagreement"; the same Item 2 table lists Bloomington, Minnesota under both Owned (170,000) and Leased (108,000) = 278,000, matching `cypress-annual-report-fy2008`'s 278,000 owned after the synthetic lease was terminated in fiscal 2007, and `cypress-annual-report-fy1993`'s earlier 170,000 owned. Reworded to state the reconciliation. |
| V-04 | Low | fixed | `cypress-annual-report-fy1997`'s summary over-read two claims: 0.6 µm belongs to Fabs 2 and 3 only, and the sub-0.5 µm Fab 4 ramp is stated in the filing as a pre-restructuring plan (superseded by the 1998-03-09 restructuring). Reworded. |
| V-05 | Medium | fixed | Added a clause to `cypress-annual-report-fy1993`'s summary: the 1991-start "Fab 3" is the original 6-inch plant, shut down in 1998 (`cypress-annual-report-fy1998`); the 8-inch fab SkyWater actually bought in 2017 began production in 1995 (`cypress-annual-report-fy1995`); the 26-year figure counts continuous Cypress operation of the site, not the age of the specific building. |
| V-06 | Low | no action (verifier's own conclusion) | The 79%/84%/65%/42%/69%/62% internal-manufacturing figures aren't wrong in any record; the two-fab-vs-one-fab context isn't stored as a quote to correct. Verifier explicitly said "no further action". |
| V-07 | Low | fixed | Added a note to `cypress-annual-report-fy2010` explaining that "stopped investing in Moore's Law ... in 2005" describes not developing nodes beyond what was already in flight, not halting the in-flight 90 nm ramp `cypress-annual-report-fy2005` and the existing `cypress-annual-report-fy2006` describe. |
| V-08 | Low | resolved as a side effect of V-03 | Once V-03 removed the invented "differing figures" framing, there is no one-sided disagreement left to flag; the existing `cypress-10-k-2016-03-02` (337,000 sq ft) already states its own figure plainly with no editorializing. |
| V-09 | Low | fixed | Added a line to `audits.md`'s introduction (via `tools/gen_filings.py`) stating that only firm, subject and report date are recorded, not opinion type, since the schema has no field for it. |
| V-10 | Low | resolved as a side effect of V-11 | The count was 42 (not 43) when the verifier checked; adding the FY1999 record's auditor's report (V-11) brought it back to exactly 43, matching what commit `8795228` and the round-3 table both said. `grep -c` on both `audits.md` and `data/filings.yaml` now agree at 43. |
| V-11 | Medium | fixed | The known_gaps reason for the FY1999 annual report was false: the body pages ARE extractable. Decoded the constant WinAnsi-code glyph offset (`chr(code + 29)`, plus dropping a stray literal "._" some kerning-only glyphs decode to) and added `cypress-annual-report-fy1999` with two verified quotes ("Fab 4a", plus the planned "Fab 4b"/"Fab 4c" construction — names that appear nowhere else in this index). Added `tools/check_filings.py`'s `GLYPH_OFFSET_DOCS`/`decode_glyph_font`, keyed by `identifier.value` so it can only ever apply to this one document, so the quotes stay verifiable with `--online`. Removed the false `known_gaps` entry. |
| V-12 | Low | fixed | Set `parent: skywater-8-k-2025-07-03` on `skywater-8-k-a-2025-09-15` (round-1 finding FIL-R1-12 asked for this; the round-2 progress table had marked it fixed, but it was still `null`). |
| V-13 | Medium | fixed | `check_location` no longer returns silently in any of its four abstain cases; each now appends a message to a new `abstentions` list that `main()` prints and counts ("N locations not checked") whenever `--online` runs. Added a whitespace-tolerant fallback search (`loose_tolerant_pattern`) before abstaining, which alone turns the reviewer's case F (fy2008 as shipped) into a real, reported problem. Verified against all eight of the reviewer's constructed cases in `tmp/verify-r3/cases/`: A-D unchanged, E/G/H now report an abstention instead of returning silently, F now fails with the correct wrong-Item message. |
| V-14 | Low | fixed | Added a parenthetical to the FY1991-1993 `known_gaps` entry pointing to `cypress-annual-report-fy1993` (a different, bare 10-K document that IS held), so a reader doesn't mistake the two for a contradiction. |

## Session log

* 2026-09-18 — Inherited an uncommitted diff in `data/filings.yaml` from an
  interrupted prior session (~140 added lines: two new SkyWater DRS/DRS-A
  records, plus edits to several existing records' quote `location` fields
  making many of them vaguer, e.g. "Form 10-K, Item 1, Manufacturing" ->
  "Form 10-K section"). Rebased branch onto `main` (picked up the merged
  paper-index tooling as the model to copy). Offline checker: 44 filings,
  0 problems.
* 2026-09-18 — Verified the diff: fetched and re-extracted text for both
  new DRS/DRS-A records (quotes and section locations confirmed against
  the cached Wayback captures) and spot-checked several of the changed
  locations (e.g. the fy2007 10-K's "Manufacturing" subheading really
  exists under Item 1; the IonQ S-4's Oxbow quote really is in the
  Summary section). `tools/check_filings.py --online` (full run, all 44
  records): 0 problems, every quote found in its fetched copy. Committed
  the diff as-is (commit 1fa181e).
* 2026-09-18 — Wrote `tools/gen_filings.py` (modelled on `gen_papers.py`)
  and generated `docs/references/filings/{index,by-company,by-year,
  by-type,by-relationship,audits}.md`; linked from
  `docs/references/index.md`. Fixed a `{ref}` cross-reference bug (link
  targets need explicit text since filing entries are anchored to list
  items, not headings). `uv run sphinx-build -W -q -b html docs
  <scratch>`: clean. All of `check_refs.py`, `check_steps.py`,
  `check_machines.py`, `check_materials.py`, `check_masks.py`,
  `check_papers.py` pass with 0 problems.
* 2026-09-18 — Added Infineon's FY2021-FY2024 annual reports (found by
  web search for the Infineon-hosted PDF, since the IR listing page 404s
  on direct fetch; dates are the latest "Neubiberg, DD Month YYYY"
  signature line found in each PDF). Closes the "Infineon annual reports
  2021-2024" gap. Tried to find SkyWater's 2023-2026 DEF 14A proxies and
  further 10-Qs, a QuickLogic 10-K naming SkyWater's RH90 process, and a
  Weebit Nano WordPress search endpoint for its 2021 announcement, but
  ran out of time to fetch a compliant (non-EDGAR) copy for any of them
  before this session had to stop; left as open items below rather than
  adding an unverified record.
* 2026-09-18 — Each new Infineon quote was individually fetched and
  grep-verified against the extracted PDF text before being added
  (exact substring match, all four). Offline `check_filings.py`: 48
  filings, 0 problems (twice, before and after the Infineon commit). A
  full-dataset `--online` re-run (48 records) was started in the
  background before this session had to stop; the previous full run (44
  records, before the Infineon commit) passed with 0 problems. The next
  session should re-check the `--online` result before adding more
  records (the fetch cache is warm so no new network access is needed,
  but the run still takes ~10 CPU-minutes for PDF text extraction —
  redirect to a log file and background it rather than waiting inline).
* 2026-09-18 — Found SkyWater's investor-relations JSON feed
  (`ir.skywatertechnology.com/feed/SECFiling.svc/GetEdgarFilingList`,
  discovered via the browser's network log on the public SEC-filings
  page) which lists every EDGAR filing back to the 2021 IPO with a
  non-`sec.gov` PDF link (`d18rn0p25nwr6d.cloudfront.net/CIK-0001819974/
  ...`), plus EDGAR accession numbers cross-checked against Wayback CDX
  listings and web search results. Used it to add: the complete 10-Q
  series (17 quarters, 2021-Q1 through 2026-Q2), the 2023-2026 DEF 14A
  proxies, and the 2026-08-10 Form 15-12G deregistration. Read (but did
  not add as records) the FY2022 10-K/A and two FY2023 10-Q/A's plus a
  2025 10-Q/A, all filed 2023-09-26/2025-09-22: each is a
  certification-only correction with no new substantive text, matching
  design §1's own exclusion example for a 10-K/A. Found, in the course of
  reading every 10-Q's Item 4: material weaknesses in internal control
  over financial reporting were disclosed continuously from the first
  10-Q (2021-05-19, as of 2021-04-04) through the last one checked
  (2026-08-07, as of 2026-06-28) — never reported as remediated — and
  that KPMG LLP replaced Deloitte & Touche LLP as auditor effective
  2024-06-21 (per the 2026 DEF 14A). Added relationship tag
  `skywater-governance` for this material (to `check_filings.py`,
  `gen_filings.py`'s `REL_GROUPS`, and the design doc) since none of the
  existing tags fit. Also found and quoted the DoD's two rad-hard (RH90)
  funding awards ($170 million in 2019, a further $99 million in 2022),
  closing that design-§7 gap. Found one internal dating error in
  SkyWater's own Q1 FY2023 10-Q (Item 4 evaluation date reads "April 3,
  2022" instead of the quarter's own April 2, 2023) and flagged it in
  that record's `notes` rather than silently correcting it. Removed a
  director's personal name from a drafted DEF 14A quote before
  committing, per the design's "no personal names beyond audit firms"
  rule. Added Weebit Nano's original 2021-09-09 ASX announcement (found
  as a company-hosted PDF, not the ASX archive itself) of the SkyWater
  ReRAM agreement, closing that design-§7 gap; its FY2022 annual report
  is still not searched. Checked QuickLogic's FY2022 10-K (IR-hosted
  copy, period ended 2023-01-01, the one covering the year the RH90
  partnership was announced) for "SkyWater" — zero mentions, despite 2022
  press releases naming the partnership; its FY2023 10-K (filed
  2024-03-27), fetched the same way, does name "SkyWater Technologies"
  (sic) among the foundries it depends on, so that record was added
  instead; QuickLogic's 10-Qs are still not searched. Net result:
  48 -> 71 filings. Offline `check_filings.py`: 71 filings, 0 problems;
  `gen_filings.py`: 6 pages, 0 problems; `sphinx-build -W -q`: clean;
  `check_refs.py`, `check_steps.py`, `check_machines.py`,
  `check_materials.py`, `check_masks.py`, `check_papers.py`: all 0
  problems. A full-dataset `--online` re-run (71 records) was run in the
  background; see the next log entry for its result.
* 2026-09-18 — Ran the full `--online` verification (71 records) three
  times, fixing real problems each time rather than re-running blindly:
  (1) first pass found 3 problems, all in two 2025 10-Qs
  (`skywater-10-q-2025-05-08`, `skywater-10-q-2025-11-12`): their Item 4
  text actually reads "the material **weakness**" (singular — SkyWater
  had temporarily consolidated down to one reported weakness that
  quarter), not "weaknesses" as the shared quote-building helper had
  assumed for every quarter; fixed by making the helper take a
  `plural` flag; (2) second pass found 1 remaining problem in
  `skywater-10-q-2025-11-12`: the quoted text spanned across a
  parenthetical the drafted quote had missed ("...Infineon Technologies
  AG ("Infinion"), pursuant to which...", where "Infinion" is
  the filing's own misspelling of "Infineon") and separately hit a PDF
  text-extraction artifact where the opening curly quote before
  "Spansion" is dropped by pypdf; fixed by re-quoting a nearby span of
  the same sentence that avoids both spots, verified letter-for-letter
  against the extracted text before re-testing; (3) third pass: **71
  filings checked, 0 problems** — clean. `gen_filings.py` regenerated (6
  pages, 0 problems) and `sphinx-build -W -q` re-run clean after each
  fix. All of `check_refs.py`, `check_steps.py`, `check_machines.py`,
  `check_materials.py`, `check_masks.py`, `check_papers.py` also re-run
  clean at the end. Final state: 71 filings (up from 48 at the start of
  this session), committed and pushed to `topic/index-filings`.
* 2026-09-19 — Fixer session applying `tmp/verify-index-filings-r3.md`
  (round 4). Verified each of the report's V-01..V-14 findings
  independently against the cached PDFs (own extraction/decode scripts
  under a scratch directory, not the verifier's) before changing
  anything; agreed with all of them. Fixed the four required items
  (V-01, V-02, V-13, V-11) and every should-fix/nice-to-have item
  (V-03..V-10, V-12, V-14) except V-06 and V-08, where the verifier's own
  conclusion was "no further action" / "resolved once V-03 is fixed" and
  nothing more was needed. One small commit per item; see the round-4
  table above for what each did. Notable fix: `check_location`'s four
  silent-abstain paths (V-13) now each append to a printed, counted
  `abstentions` list, and a whitespace-tolerant fallback search was added
  before abstaining -- verified against all eight of the reviewer's
  constructed cases in `tmp/verify-r3/cases/` (E/G/H now report instead
  of going silent; F, the real fy2008 bug, now fails with the correct
  message instead of passing). Decoded the FY1999 Cypress annual
  report's constant-offset glyph encoding (V-11) and added it as a
  record with two independently re-verified quotes, scoping the decoder
  to that one document by `identifier.value` so it can never affect an
  unrelated filing; removed the false `known_gaps` entry it replaces.
  Final state: 86 filings (up from 85). `check_filings.py`: 86 filings,
  0 problems. `gen_filings.py --check`: 6 pages, 0 problems.
  `check_filings.py --online` (full, 86 records): **86 filings checked,
  0 problems, 170 locations not checked** -- the first time this count
  has ever been printed; it is not a regression, it is V-13 making
  visible what was always true (most `location` values name a
  non-Item-numbered section, or the document has no machine-matchable
  "ITEM 1" heading, so `check_location` had nothing to compare).
  `check_refs.py`, `check_steps.py`, `check_machines.py`,
  `check_materials.py`, `check_masks.py`, `check_papers.py`/
  `gen_papers.py --check`, `check_patents.py`/`gen_patents.py --check`:
  all 0 problems. `sphinx-build -W -q -b html docs tmp/build-filings`:
  clean, exit 0. Pushed to `topic/index-filings`.

## Round 5 — location-check coverage (task A), new filings (task B), FIL-R1-11/-12/-15 (task C)

Worktree `.worktrees/topic-index-filings-r5`, branch `topic/index-filings-r5`
(fresh worktree off `main`, which already carried round 4's merged state).

**Task A.** `check_location` previously understood only "ITEM N." captions;
everything else (most annual-report section headings, page/paragraph
positions, and every auditor-signature quote, which has no `location`
field at all) abstained. Added three more checkable location shapes:

* a PDF page number (`page N`), checked against `document_pages` (new:
  per-page extracted text, not just the joined whole-document text);
* a position (`cover page`, `first page`, `cover page note`, `first
  paragraph`, `second paragraph`), checked against PDF page 1 or a
  paragraph index that skips non-prose paragraphs (a press release's
  headline and subheadline are their own blank-line-delimited
  "paragraphs" ahead of the body text, and would otherwise be miscounted
  as the first one or two paragraphs);
* a prose section heading (`heading_phrase` extracts the most specific
  comma-separated segment, or a trailing parenthetical), matched only
  against an occurrence that starts a line (`heading_like`) -- the same
  words also turn up mid-sentence as an ordinary cross-reference (e.g.
  fy2006's boilerplate "The letter to Shareholders and 'MD&A' contain
  forward-looking statements...", 55000 characters after that record's
  real, differently-worded "FELLOW SHAREHOLDERS:" heading -- counting it
  would have wrongly failed a correct location).

Also: an `auditor_report` quote has no `location` field in the schema (it
never claimed a position to check), so it no longer counts as an
abstention at all -- previously every one of the ~43 auditor quotes
abstained with "names no Item number", which was never a real gap.

First full `--online` run under the new checks (still 86 records) found 6
"problems" where the old checker had abstained. Investigated each against
the cached fetched text before changing anything, rather than assuming
the checker was right: three were checker false positives (fixed above,
in `check_heading_location`'s `heading_like` filter and
`check_positional_location`'s prose-paragraph filter) and three were real
wrong locations, fixed in the data:

* `weebit-nano-announcement-2021-09-09` quote 2: "First page" -> the
  quote is on page 2.
* `skywater-10-q-2025-11-12` quote 2: "...Business Combination" -> the
  quote is actually in "Note 1 -- Nature of Business", a general
  paragraph mentioning the Fab 25 purchase agreement, not the "Business
  Combinations" accounting-policy note that follows a paragraph later;
  fixed to "note 1".
* `skywater-10-q-2026-05-08` quote 2: same shape of bug, found by
  checking the sibling record above manually (the checker itself only
  abstained here, since "Business Combination" does not occur at all in
  this quarter's document -- its equivalent note is "Note 4
  Acquisition"); fixed to "note 4".

Abstention count on the original 86-record dataset, `--online`, full
runs before and after (same records, only `check_filings.py` and the
three location fixes above changed): **170 -> 96** locations not checked.
The remaining 96 are genuinely unverifiable with the text extracted from
these particular copies (a heading rendered as a stylised graphic with no
extractable text; a phrase that recurs only far from the quote in either
direction; a handful of styles -- "Part I" alone, "Introductory section",
"Form 15-12G cover" -- that name no specific heading at all) rather than
locations the checker gave up on for lack of trying.

**Task B.** Fetched and verified, each against its own cached copy:

* `weebit-nano-annual-report-fy2022` (annualreports.com/.../ASX_WBT_2022.pdf):
  closes design section 7's "Weebit Nano's FY2022 annual report" gap.
* `skywater-8-k-2024-06-26` (Item 4.01, Wayback capture): SkyWater's own
  primary record of KPMG replacing Deloitte & Touche, previously known
  only from the 2026 DEF 14A.
* `cypress-8-k-2019-06-03` (Item 1.01, Wayback capture, accession
  0001104659-19-033282): the Agreement and Plan of Merger with Infineon
  at $23.85/share, closing the "8-K announcing the 2019 merger agreement"
  `known_gaps` entry. Found while looking for a related, later
  Infineon-hosted 8-K (Item 8.01, employee/customer/supplier
  communications) in the same EDGAR "a19-10962" submission series --
  that related 8-K was read but not added as a separate record (its
  substance, a change-of-control announcement to stakeholders, adds
  little beyond what the merger-agreement 8-K and the closing 8-K already
  cover, and design section 1 does not ask for every 8-K in a submission
  series).

Checked and found nothing to add: six QuickLogic 10-Qs (FY2023-FY2025,
via `ir.quicklogic.com`), none naming SkyWater, unlike its FY2023 10-K;
Infineon's Q3 FY2025 quarterly press release, which does not mention
Austin, Fab 25 or SkyWater; a SkyWater Form S-8 (2021-04-21) and Form S-3
(2022), both squarely design section 1's "equity plans"/generic-shelf
exclusions; Infineon's 2025-06-30 press release on completing the Fab 25
sale (found, read, and not added -- no confirmed Art. 17 MAR "ad hoc"
heading, so not forced into that document type; see design section 7).
The DEFM14A and 15-12B for the 2019 Cypress/Infineon merger, the German
company register, D-Wave's 10-Qs, Infineon's half-year reports and the
`supplier-names-skywater` tag remain unsearched or not found (design
section 7).

**Task C.** FIL-R1-11 (cache staleness): `fetch()` now re-fetches a
non-Wayback copy once its cache entry (the file's own mtime) is more
than `CACHE_MAX_AGE_DAYS` (90) old; a Wayback capture, whose timestamp is
fixed in the URL, is cached forever. FIL-R1-12 (`period.label`
rendering): `gen_filings.py` now renders a "Period: ..." line for
`current-report`/`exhibit` records, whose titles carry no period (10-Ks
and 10-Qs already have their fiscal year or quarter in the title).
FIL-R1-15 (unused vocabulary): `ad-hoc-announcement` and
`supplier-names-skywater` are still unused after a real search this round
(see task B); design section 7 keeps naming both as reserved, not
silently declared done.

**Provenance cleanup (found opportunistically, not a task item):**
`weebit-nano-annual-report-fy2023`'s and `-fy2024`'s `auditor_report.quote`
each carried the signing Nexia partner's own name between the firm name
and the city/date (the Australian audit-report signature format
interposes it, unlike a US "/s/ Firm City Date" line); trimmed both, and
the new fy2022 record's quote, to just the firm name, per design section
2's "no personal names beyond audit firms" rule.

Net result: 86 -> 89 filings (+3: `weebit-nano-annual-report-fy2022`,
`skywater-8-k-2024-06-26`, `cypress-8-k-2019-06-03`); by company, 26
Cypress (+1), 43 SkyWater (+1), 7 Infineon, 5 Weebit Nano (+1), 4 D-Wave,
3 IonQ, 1 QuickLogic.

**Final checks (foreground, this session).** `uv run tools/check_filings.py`:
89 filings, 0 problems. `uv run tools/gen_filings.py --check`: 6 pages, 0
problems. `uv run tools/check_filings.py --online` (full, all 89
records): **89 filings checked, 0 problems, 100 locations not checked**
(up from 96 on the 86-record dataset before task B's three additions,
each of which added a couple of abstained locations of its own; none of
the three new records' locations were wrong). `uv run
tools/check_refs.py`: 264 written pages, 0 with problems. `uv run
tools/check_steps.py`: 171 pages, 0 missing headings. `uv run
tools/check_machines.py`: 30 pages, 0 problems. `uv run
tools/check_materials.py`: 12 pages, 0 problems. `uv run
tools/check_masks.py`: 36 pages, 0 problems. `uv run
tools/check_papers.py`: 56 papers, 0 problems. `uv run
tools/gen_papers.py --check`: 9 pages, 0 problems. `uv run
tools/check_patents.py`: 252 patent families, 0 problems. `uv run
tools/gen_patents.py --check`: 6 pages, 0 problems. `uv run
sphinx-build -W -q -b html docs tmp/build-filings-r5`: clean, exit 0.
Pushed to `topic/index-filings-r5`.

### Round 5 — verification follow-ups (2026-09-19)

* The FY2022 Weebit Nano summary no longer says the report covers the
  licensing deal "for a full financial year"; it is the first annual
  report to cover it. Earlier Weebit annual reports (FY2019–FY2021)
  predate the deal and are out of scope.
* Open, for a later round: of the 100 quotation locations the online
  check does not verify, about 44 are documents whose Item captions are
  mixed-case (the caption test is upper-case only) and about 15 are HTML
  documents flattened without line breaks (the heading test wants a line
  start); sub-item numbers such as "4.01" are read as "4"; the quotation
  should be located on the same normalised text as the verbatim check;
  PDFs are parsed twice per run.
