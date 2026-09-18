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
  personal name ("Mr. Unterseher") from a drafted DEF 14A quote before
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
