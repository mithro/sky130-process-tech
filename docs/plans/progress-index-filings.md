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
| 10-Q | 2025-08-07 | records added | only one quarter recorded; systematic 10-Q sweep 2021-2026 **not searched** |
| DEF 14A | 2022-04-19 | records added | 2023-2026 proxies **not searched** (design §7 gap) |
| DEFM14A (IonQ merger proxy) | 2026-03-31 | records added | |
| 8-K | 2022-04-04, 2023-08-04, 2025-02-26, 2025-07-03, 2026-01-26, 2026-07-31 | records added | Fab 25 purchase, other current reports |
| 8-K/A | 2025-09-15 | records added | |
| EX-99.1 (press release exhibit) | 2026-01-26 | records added | |
| Auditor reports / restatements | none found yet | not searched | 10-Ks list auditor per year; no restatement found so far |
| DoD/RH90 funding, CHIPS Act | not searched | not searched | look for 8-K or 10-K risk-factor disclosure |
| Oxbow/CMI | related-party disclosures in S-1/10-K only so far | not searched | CMI Acquisition, LLC appears as EDGAR filer name on DRS; no independent Oxbow/CMI public filings found yet |

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
| ASX announcement | 2023-06-29 | records added |
| Annual report (Appendix 4E) | FY2023 (2023-08-25), FY2024 (2024-08-28) | records added |
| 2021 SkyWater agreement announcement, FY2022 annual report | not searched | design §7 gap (older than website archive) |

### IonQ, Inc. (acquirer, 2026)

| Form | Dates | Status |
|---|---|---|
| 10-K | FY2025 (2026-02-25) | records added |
| S-4 (merger registration) | 2026-03-20 | records added |
| 8-K | 2026-07-31 | records added |

### QuickLogic Corporation and other named partners/suppliers

| Company | Status |
|---|---|
| QuickLogic | not searched (design §7: "named in SkyWater press releases") |
| Equipment/materials suppliers naming SkyWater as customer | not searched |
| Technology licensors/partners named in public filings | not searched beyond D-Wave/Weebit Nano/IonQ |

## Gaps and open questions (from design §7, carried forward)

* **Not retrievable without EDGAR** (no Wayback capture, no company copy
  found): Cypress 10-Q/A Q1 2003 (CYP-07), Cypress 2019 8-K and DEFM14A for
  the Infineon merger, Cypress FY2019 10-K (filed 2020) and 10-K/A, Cypress
  15-12B (2020); SkyWater's DRS amendment No. 1 document text (2020-09-30,
  index captured only) and the Process Technology License Agreement
  exhibit itself (exhibit 10.6/10.7 of the S-1/A).
* **Accession numbers missing** for IR-feed-only records (2026 SkyWater
  merger filings, D-Wave, IonQ) — feed filing id recorded instead.
* **Dates of annual reports to shareholders / German annual reports** are
  the latest signature date printed in the copy, not a filing date.
* **Not yet searched:** QuickLogic's and other partners' 10-Ks; equipment
  and materials suppliers naming SkyWater as a customer; SkyWater's DEF 14A
  proxies for 2023-2026; SkyWater's 10-Q series (only one quarter
  recorded); Infineon's half-year reports and the German company register;
  Weebit Nano's 2021 SkyWater agreement announcement and FY2022 annual
  report; Cypress's 2019 merger communications beyond one DEFA14A capture.
* Whether exhibits (purchase agreements, line-operation amendments) should
  be separate records or folded into their parent filing — still open.

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
