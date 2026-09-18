# Financial filings index — design

Status: proposal, 2026-09-14. Task: "Financial filings index pages" in
`docs/plans/TASKLOG.md`. Dataset phase done (`data/filings.yaml`,
`tools/check_filings.py`); pages not yet written. This file lives in
`docs/plans/`, which the Sphinx build excludes.

## 1. Purpose and scope

The filings index lists financial and corporate filings that document
the ownership, business and process lineage of the fab that makes
SKY130: Cypress Semiconductor's Minnesota fab (Fab 4), its 2017 sale to
SkyWater Technology Foundry, SkyWater's life as a public company, its
licence of Cypress process IP (now Infineon's), its 2025 purchase of
Infineon's Austin fab (Fab 25, a former Cypress fab) and its 2026
acquisition by IonQ, together with filings by other companies that name
SkyWater or the Cypress fab. It complements the public sources
inventory the same way the paper and patent indexes do: the inventory
holds sources that a page cites; the index is a catalogue, and a filing
enters the inventory only when a page cites it (the existing SEC-01,
SEC-02, SEC-03, CYP-08, CYP-09 and CYP-10 entries are linked from their
records through `inventory_key`).

A document is **included** when it is a financial or corporate filing
(annual, quarterly or current report, exhibit, registration statement,
prospectus, proxy statement, annual report to shareholders, ad-hoc or
market announcement, deregistration) and it says something specific
about one of:

1. the Minnesota fab under Cypress (operations, processes made there,
   the plan to sell it, the sale);
2. SkyWater's history, IPO, Cypress licence, Oxbow relationships,
   customers named as Cypress or Infineon, Fab 25 and the IonQ merger;
3. Infineon's acquisition of Cypress and its sale of the Austin fab to
   SkyWater;
4. SkyWater as a supplier, foundry or partner in another company's
   filing (D-Wave's line-operation agreement inherited from Cypress,
   Weebit Nano's ReRAM in S130, IonQ's acquisition).

A document is **excluded** when it only mentions the companies in
passing (ownership reports, routine 8-Ks for earnings, officer changes
or loan amendments, equity plans), when it duplicates an included
document without adding anything (later S-1 amendments, the 424B3 copy
of a proxy statement already listed as a DEFM14A, a 10-K/A that only
restates internal-control language), or when it cannot be read from a
public copy other than `sec.gov` itself. Equipment-vendor 10-Ks already
in the inventory (AMAT-10K, LAM-10K and others) are cited for
technology, not for the lineage, and stay out unless they name Cypress
or SkyWater.

## 2. Dataset

`data/filings.yaml` is a mapping with `schema_version: 1`, `retrieved`,
`filings` (a list sorted by filing date and id), and an optional
`known_gaps` list (FIL-R1-13). It is the single source of truth; pages
are generated from it.

| Field | Content |
|---|---|
| `id` | `<company>-<form>-<filing date>` in lower case (`skywater-10-k-2024-03-15`); `cypress-annual-report-fy2004` for undated annual reports to shareholders; exhibits add the exhibit number |
| `company`, `company_key` | the filer as named in the document; key from a controlled list (`cypress`, `skywater`, `infineon`, `d-wave`, `ionq`, `quicklogic`, `weebit-nano`, `other`) |
| `form`, `document_type` | the form as the regulator or company names it (`10-K`, `8-K/A`, `DEFM14A`, `Annual Report`, `ASX announcement`); a controlled type (`annual-report`, `quarterly-report`, `current-report`, `exhibit`, `registration-statement`, `prospectus`, `proxy-statement`, `annual-report-to-shareholders`, `market-announcement`, …) |
| `parent` | the record id of the filing an exhibit belongs to |
| `title` | a short descriptive title |
| `period` | `label`, `start`, `end` (fiscal year or quarter; for an 8-K the event date) and an optional `note` |
| `filed` | the EDGAR filing date where retrieved; otherwise the latest signature date printed in the copy, explained in `notes` |
| `jurisdiction`, `regulator` | `US`/`SEC`, `DE`/`BaFin`, `AU`/`ASX` |
| `identifier` | `sec-accession` (`0001819974-24-000008`), `ir-filing-id` (the id in a company's investor-relations filings feed, when the accession number could not be retrieved without EDGAR), or `company-document` |
| `urls` | `original` (the `sec.gov` document or filing index where the accession is known, otherwise the company page or PDF), `wayback` (a capture of the original) and `ir` (an investor-relations or annual-report archive copy) |
| `about` | `summary` (what the document says about the other companies, factual, no further than the text read) and one or two `quotes` with `text` and `location` |
| `auditor_report` | `firm`, `subject`, `date` and a `quote` of the signature, when the document contains an auditor's report that was read |
| `relationships` | controlled tags (§3) |
| `related_docs` | `{label, relation, reason}`: `cites` when the labelled page cites the record's inventory key (checked), `context` otherwise |
| `inventory_key` | the `public-sources.md` key when the filing is already in the inventory |
| `discovery`, `discovery_note` | how the document was found (§5) |
| `verified` | `<ISO date> <source fetched>` |
| `notes` | optional caveats (dates taken from the copy, truncated captures) |

`known_gaps` (each `{company_key, description, reason}`) lists filings
known to exist -- named in another filing's exhibit index, an inventory
entry already cited elsewhere in this reference, or this project's own
discovery notes -- for which no copy could be found or read that is not
`sec.gov` itself. It renders as a "Known gaps" section on `index.md`
(grouped by company) so the shortfall is visible to a reader instead of
living only in this design doc and the progress file (FIL-R1-13, raised
after the round-1 independent review found the index silently missing
most of the Cypress Minnesota-fab era, FIL-R1-01).

Rules that follow from the common agent rules:

* **No direct EDGAR fetches.** `sec.gov` asks for a contact in the
  User-Agent, which rule 10 forbids. EDGAR documents are read through
  Wayback captures or investor-relations copies; a `sec.gov` URL is kept
  as the canonical link but the checker requires a non-`sec.gov` copy.
* **Claims go no further than the text read.** Summaries and quotes come
  from the fetched copy; every quote is re-checked by `--online`.
* **People.** Filings name directors, officers and signatories; records
  do not repeat personal names beyond audit firms.
* **Owner constraints.** Nothing is taken from the data.wafer.space mask
  renders or the process-steps sheet. Customer names appear only as a
  filing states them (SkyWater's 10-Ks name Infineon, D-Wave and others
  as customers).

## 3. Controlled relationship tags

Cypress era: `cypress-fab-operations`, `cypress-process-technology`,
`cypress-third-party-foundry`, `cypress-fab-sale`,
`cypress-technology-license`, `cypress-foundry-services`.

SkyWater: `skywater-fab-history`, `skywater-ipo`, `skywater-suppliers`,
`skywater-customers`, `oxbow-related-party`, `minnesota-fab-investment`,
`skywater-ionq-merger`, `skywater-governance` (added 2026-09-18: auditor
appointments, material weaknesses and restatements as a public company).

Infineon: `infineon-cypress-acquisition`, `infineon-fab25-sale`,
`infineon-wafer-supply`.

Others: `supplier-names-skywater`, `customer-names-skywater`,
`partner-names-skywater`.

The one-line definitions live in `tools/check_filings.py`
(`RELATIONSHIPS`), which the generator will also use for section
introductions.

## 4. Proposed pages

All pages live under `docs/references/filings/`, are listed in a
toctree from `docs/references/index.md`, and are generated.

| Page | Label | Grouping |
|---|---|---|
| `index.md` | `filings-index` | Landing page: scope (§1), a short timeline of the lineage events with links to the defining filings (fab sale 2017, IPO 2021, Fab 25 2025, IonQ 2026), counts by company, type and year, how to read an entry, the EDGAR access note, a "Known gaps" section listing `known_gaps` by company, links to the other views, and the canonical entry for every document in date order, each under a label `filing-<id>` |
| `by-company.md` | `filings-by-company` | Cypress, SkyWater, Infineon first (the lineage), then acquirer, customers and partners; within a company, by date |
| `by-year.md` | `filings-by-year` | Year of filing, newest first |
| `by-type.md` | `filings-by-type` | Annual reports (with auditor), quarterly reports, current reports and exhibits, registration statements and prospectuses, proxy statements, announcements |
| `by-relationship.md` | `filings-by-relationship` | One section per tag in §3 order, grouped under Cypress era, SkyWater, Infineon, others; the section introduction is the tag definition |
| `audits.md` | `filings-audits` | The auditor's reports found in the records: firm, subject, date, filing |

Entry format (on `index.md`; the other pages list the title, company,
form and date with a `{ref}` to the canonical entry):

```markdown
(filing-skywater-10-k-2024-03-15)=
* **SkyWater Technology, Inc. — Form 10-K, fiscal year 2023** (filed
  2024-03-15; SEC accession 0001819974-24-000008).
  [EDGAR](https://www.sec.gov/…) · [Wayback copy](https://web.archive.org/…) ·
  [investor-relations copy](https://…).
  Summary … "quote" (Item 1). Auditor: Deloitte & Touche LLP, 2024-03-15.
  Relationships: {ref}`Cypress technology licence <filings-rel-cypress-technology-license>` ·
  Inventory: SEC-02 · Related pages: {ref}`process overview <overview-index>` — reason.
```

Like the paper and patent index designs, entries use inline links
rather than footnotes (each entry is a full citation), so
`tools/check_refs.py` does not treat the pages as written pages; the
citation-style exception proposed for generated index pages would cover
`docs/references/filings/` too.

## 5. Discovery (as done for the first dataset)

Recorded per record in `discovery` (controlled list in the checker):

* `inventory-seed` — the SEC-01 to SEC-03 and CYP-07 to CYP-10 entries;
* `edgar-listing-wayback` — Wayback captures of EDGAR company filing
  lists (SkyWater 2025-05-08 and 2026-01-09; Cypress 2017-05-08 10-K/10-Q
  list and 2019-03-01 XML list), which give form, date and accession;
* `wayback-cdx` — CDX listings of captured files under each company's
  EDGAR folders (`sec.gov/Archives/edgar/data/<CIK>/…`), which find the
  captured primary documents and index pages;
* `ir-archive` — company investor-relations archives: the SEC filings
  feeds of SkyWater, D-Wave and IonQ (JSON feeds of their public
  investor sites, each with PDF copies of every filing), Infineon's
  annual reports page and investor documents, Weebit Nano's ASX
  announcements archive;
* `annualreports-com` — Cypress annual reports 2002–2018;
* `web-search` — web searches used only to find candidates (Infineon's
  copy of Cypress's merger-completion 8-K, D-Wave's line-operation
  amendment), each then fetched from the company copy;
* `exhibit-index` — exhibits found in a parent filing.

Keyword probes (SkyWater, Cypress, Infineon, Oxbow, Bloomington,
Minnesota, Fab 4, Fab 25, S130, SONOS, IonQ, auditor's report) were run
on every candidate before a record was written.

## 6. Generation and checks

* `tools/gen_filings.py` (to write) reads `data/filings.yaml` and writes
  the pages in §4 deterministically, each starting with a comment
  "Generated from data/filings.yaml by tools/gen_filings.py — do not
  edit"; `--check` fails if a committed page differs.
* `tools/check_filings.py` (this branch) validates the dataset offline:
  schema and key order, unique ids, accession format and its match with
  the EDGAR folder, ISO dates and period order, controlled lists, URL
  shapes, the Wayback-or-IR-copy rule for `sec.gov` originals, quote
  counts and lengths, e-mail addresses, docs labels, `cites` relations
  against the page's footnotes, inventory keys and sort order. It prints
  "N filings checked, M problems". `--online` fetches each record's
  Wayback copy, then its IR copy (never `sec.gov`), with the project user
  agent, and confirms that every quote and auditor signature occurs in
  the text (NFKC, quotation marks, dashes and whitespace normalised,
  because PDF extraction drops and inserts spaces). It is a PEP 723
  script (`pyyaml`, `pypdf`, `cryptography`), so `uv run` needs no
  project changes.
* The Sphinx `-W` build then checks every `{ref}` in the pages.
* Each batch gets an independent review (fetch a sample of copies,
  confirm summaries against the text, confirm the inclusion rules) and a
  provenance review (no non-public material; no names from the renders
  site or the sheet; no personal names).

Workflow for adding a filing: find it (§5), fetch the copy, write the
record, run `uv run tools/check_filings.py --online`, then the generator
and the `-W` build.

## 7. Gaps and open questions

Filings known to exist but not retrievable from a non-`sec.gov` copy are
recorded in the dataset's `known_gaps` list (§2) and rendered on
`index.md`, so that shortfall is visible on the page itself rather than
only here; see that section for the current list (Cypress's 10-Q/A for
Q1 2003 (inventory CYP-07), its 2019 8-K and DEFM14A for the Infineon
merger, its fiscal 2019 10-K and 10-K/A, its 15-12B, three Cypress
annual-report years whose text could not be extracted or that say
nothing about the Minnesota fab, and SkyWater's DRS/A No. 1 text and the
Process Technology License Agreement exhibit itself). The Cypress
Minnesota-fab era (fiscal 1991-2002, 2005, 2008-2014) that round-1
independent review finding FIL-R1-01 found largely missing has since
been filled from annualreports.com; see
`docs/plans/progress-index-filings.md` for the fiscal-year-by-fiscal-year
checklist.

Other open items, not yet resolved:

* **Accession numbers** are missing for records read only from
  investor-relations feeds (2026 SkyWater merger filings, D-Wave, IonQ);
  the feed filing id is recorded instead.
* **Dates of annual reports to shareholders and German annual reports**
  are the latest signature date printed in the copy, not a filing date;
  `by-year.md` says so in its introduction (FIL-R1-14).
* **Not yet searched:** equipment and materials suppliers naming
  SkyWater as a customer (the `supplier-names-skywater` tag has no
  records yet), QuickLogic's and D-Wave's 10-Qs, further Weebit Nano
  annual reports older than FY2023, Infineon's half-year/quarterly
  statements and ad-hoc (Art. 17 MAR) announcements (the
  `ad-hoc-announcement` document type has no records yet), the German
  company register, and Cypress's 2019 merger communications beyond the
  one captured DEFA14A.
* Whether exhibits (purchase agreements, the line-operation amendments)
  should be separate records or folded into their parent filing.
