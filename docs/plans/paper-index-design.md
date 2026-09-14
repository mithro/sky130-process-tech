# Academic paper index — design

Status: proposal, 2026-09-14, revised after the independent review of
the dataset phase. Dataset phase done (`data/papers.yaml`,
`data/papers-excluded.yaml`, `tools/check_papers.py`); pages not yet
written. This file lives in `docs/plans/`, which the Sphinx build
excludes.

## 1. Purpose and scope

The paper index lists academic papers whose subject is SKY130 or the
SkyWater 130 nm process, so that a reader of a step, mask, machine or
overview page can find the published measurements, models and silicon
results behind it. It complements the public sources inventory: the
inventory holds only sources that a page cites; the index is a
catalogue, and a paper enters the inventory only when a page cites it.

A paper is **included** when it is one of:

1. **PDK and process** — the open PDK and its tooling as they relate to
   the process: device models and their calibration, parameter
   extraction, design rules, extraction, fill and integration findings
   specific to the process.
2. **Devices and test structures on SKY130** — measured devices, test
   structures, test vehicles and reliability, including radiation,
   cryogenic and high-temperature work, ReRAM/RRAM, SONOS, floating-gate,
   MiM, photonic or MEMS devices fabricated on the process.
3. **Silicon on SKY130 shuttles** — circuits and chips fabricated on the
   process (open MPW, ChipIgnite, Tiny Tapeout or other runs) where the
   paper reports silicon measurements or process-specific results.
4. **Lineage and the fab** — the Cypress S8 / SONOS 130 nm lineage, work
   from the Bloomington fab (Cypress Fab 4, later SkyWater), and the RRAM
   and monolithic-3D work at SkyWater from which the sky130B ReRAM module
   descends.

Every record carries a **`basis`** that says how its link to the process
is established:

| `basis` | Meaning |
|---|---|
| `named-process` | The abstract or retrieved full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry. |
| `affiliation-inference` | The process or fab is not named; the link rests on SkyWater or Cypress (Bloomington) author affiliations in the public records. |
| `lineage-inference` | The process is not named; the link rests on public Cypress statements about the S8 lineage (for example CYP-20). |

A paper whose process is not named is included **only** under one of
the two inference bases, with the inference and its public evidence
stated in `notes`. The index does not infer the process from shuttle
context alone: a Tiny Tapeout or "open-source 130 nm PDK" paper that
does not name the process is held until the full text does.

A paper is **excluded** when it only simulates with the PDK (unless it
characterises the process or its models), when it reports no silicon
results and no process-specific findings, when the process is not named
and no inference basis applies, when it is about another SkyWater
process (S90, 90 nm FDSOI, interposers, packaging), or when it is not a
paper (theses, datasets, software records, slides, posters, trade
press). General textbooks and generic 130 nm papers stay in the
inventory only.

Borderline decisions are recorded in each record's `notes` field, which
starts "Borderline inclusion." where the case is marginal. Papers that
were considered and excluded, or held pending a full-text check, are
listed with their reasons in `data/papers-excluded.yaml` (§2.2), so that
they are not rediscovered and re-argued each round.

## 2. Datasets

### 2.1 `data/papers.yaml`

A YAML list, one mapping per paper, sorted by `(year, title.casefold())`.
It is the single source of truth; pages are generated from it.

| Field | Content |
|---|---|
| `id` | `doi:<DOI in lower case>`; `arxiv:<id>` for arXiv-only papers; `web:<slug>` for workshop papers that have neither (owner decision: kept; currently WOSET only) |
| `label` | stable page label `paper-<first-author family>-<year><letter>` (for example `paper-hsieh-2019a`); **assigned once when the record is added and never changed**, so `{ref}`s from other pages keep pointing at the same paper |
| `title` | as registered (Crossref, arXiv abs page or proceedings page); used by `--online` |
| `title_display` | the title for pages: inline TeX converted to Unicode ("4 × 8"), backticks and U+2010 hyphens normalised, ASMC track tags (" : YE: …") removed |
| `authors`, `year` | as published; the conference year where the Crossref date is the later online date |
| `venue`, `venue_series`, `venue_type` | container title as registered; a normalised series for grouping (`ASMC`, `ISSM`, `IEDM`, `VLSI Symposium`, `ISCAS`, `ICM`, `IEEE Design & Test`, `WOSET`, `arXiv`, …); one of journal, magazine, conference, workshop, preprint, report |
| `volume`, `issue`, `pages`, `article_number` | from Crossref where registered, otherwise `null`, so that every entry is a full citation |
| `doi`, `landing_url` | DOI as registered; publisher landing page from the Crossref `resource.primary.URL` (https) |
| `arxiv` | `null` or `{id, url}` |
| `paywalled` | `false` only when a free copy of the version of record is listed (publisher gold/hybrid/bronze/diamond, or an open proceedings page) or the paper is a preprint |
| `free_full_text` | list of `{url, host, oa_type, located_via, checked}`: arXiv, author or institutional repositories, OSTI, PubMed Central, conference open-access pages and publisher OA copies located through OpenAlex's open-access data or the preprint's own DOI; the host must be on the checker's allowlist; `checked` records the date and HTTP result |
| `topics` | controlled list (§3) |
| `basis` | §1 |
| `institutions` | every institution named in the raw affiliation strings (OpenAlex) or on the paper itself (arXiv HTML, OSTI record, proceedings page), with OpenAlex display names used only for spelling; never empty |
| `fabrication` | `null` or `{quote, source}`: an **exact** quotation from the paper naming the run, shuttle or foundry (omissions marked "[…]"), and `source` one of `abstract`, `full text (HTML)`, `full text (PDF)` |
| `related_docs` | `{label, reason}` pairs: a `{ref}` label under `docs/` and one sentence that claims no more than the paper says |
| `inventory_key` | the `public-sources.md` key when the paper is already in the inventory |
| `discovery` | how the paper was found (§5) |
| `notes` | borderline reasoning, what the abstract does and does not say, and the inference for non-`named-process` records |
| `verified` | `<ISO date> <source fetched>`: the DOI's Crossref record, arXiv abs page or proceedings page, with the title matched |

### 2.2 `data/papers-excluded.yaml`

A YAML list of `{id, title, year, status, reason, decided}`, where
`status` is `excluded` (outside §1) or `held` (possibly in scope; waiting
for a full-text check, for example because the abstract does not name
the process and the publisher refuses scripted requests). An id may not
appear in both files. A held paper moves to `papers.yaml` when its full
text is read and names the process.

### 2.3 Rules

* Claims in `notes`, `fabrication` and `related_docs` go no further than
  the abstract or the full text actually retrieved; anything else is
  marked as an inference with its basis.
* Fabrication text is quoted, not paraphrased. A paper's shuttle wording
  ("CI 2309", "Open MPW", "Tinytapeout") is **never** mapped to run,
  reticle or frame identifiers from the mask-renders site or the
  process-steps sheet, even where the match looks obvious; the checker
  rejects renders, sheet and run/frame references anywhere in a record.
* No e-mail addresses, and nothing in any request header or URL beyond
  the project user agent. The Crossref/OpenAlex `mailto` polite pool is
  not used, and neither is the Unpaywall API that the task names, because
  it requires an e-mail parameter (Common rule 10); open-access locations
  come from OpenAlex's open-access data instead.
* Never link Sci-Hub or its successors, Anna's Archive, LibGen,
  Z-Library, ResearchGate, Academia.edu or any other unauthorised or
  scraped copy. Free copies must be on an allowlist of hosts
  (repositories, preprint servers, publishers, proceedings sites); the
  denylist is a second line of defence.
* No project, design, customer or recipient names taken from the
  data.wafer.space renders or the process-steps sheet. Papers are cited
  with their own titles and authors.

## 3. Controlled topics

Process, PDK and devices: `pdk-models`, `device-characterisation`,
`test-structures`, `reliability`, `radiation`, `cryogenic`,
`high-temperature`, `rram`, `sonos`, `floating-gate`,
`beol-integration`, `photonics`, `mems`.

Circuits fabricated on the process: `analog-rf`, `mixed-signal`,
`power-management`, `digital`, `memory`, `sensors`, `quantum`,
`security`.

Ecosystem and lineage: `tooling`, `education-shuttles` (papers about a
shuttle programme or its educational use, not every paper that used a
shuttle), `fab-manufacturing`, `lineage-s8`.

The one-line definitions live in `tools/check_papers.py` (`TOPICS`),
which the generator will also use for section introductions. Adding a
topic means adding it there and to the page mapping in §4. A derived
shuttle grouping, if wanted, is taken only from `fabrication.quote`.

## 4. Proposed pages

All pages live under `docs/references/papers/`, are listed in a toctree
from `docs/references/index.md`, and are generated.

| Page | Label | Grouping |
|---|---|---|
| `index.md` | `papers-index` | Landing page: scope, `basis` and inclusion rules (§1), counts by topic, year and access, how to read an entry, links to the other views, and **the only full entry for each paper**, sorted by first author, each under its stored `label` |
| `fab-publications.md` | `papers-fab-publications` | "Fab publications (Bloomington)": the `fab-manufacturing` records (Cypress Fab 4 and SkyWater-era manufacturing, yield and process-control papers, all `affiliation-inference`), grouped Cypress era then SkyWater era, with the basis explained once at the top; linked from `index.md` and from the related machine pages. These records appear on no topic or device page other than this one |
| `by-topic.md` | `papers-by-topic` | One section per topic in §3 order (except `fab-manufacturing`), grouped under three headings (process, PDK and devices; circuits; ecosystem and lineage); each section opens with the topic definition and links to the process pages it relates to |
| `by-module.md` | `papers-by-module` | Entries grouped by the `related_docs` labels they carry: overview modules (for example the sky130B ReRAM page), steps, masks, machines and material classes, each heading linking the page; entries without related pages are listed at the end |
| `by-year.md` | `papers-by-year` | Newest year first |
| `by-venue.md` | `papers-by-venue` | `venue_type`, then `venue_series` (IEDM, VLSI Symposium, ISCAS, ASMC, ISSM, IEEE Design & Test, arXiv, WOSET, …) |
| `by-institution.md` | `papers-by-institution` | Institution name, alphabetical; SkyWater Technology and Cypress Semiconductor first, as the fab's own publications |
| `by-device.md` | `papers-by-device` | Device or circuit type derived from topics: MOSFET models and cryogenic devices; RRAM; SONOS and floating-gate NVM; BEOL-integrated devices; analog and RF; data converters; power; digital and memory; sensors and quantum interfaces |

Full entry format (on `index.md` only):

```markdown
(paper-hsieh-2019a)=
* **Title (title_display).** A. Author, B. Author and C. Author.
  *Venue*, vol. V, no. N, pp. P, 2019. DOI
  [10.1109/…](https://doi.org/10.1109/…) · [publisher page](https://…) ·
  free copy: [arXiv](https://arxiv.org/abs/…) · paywalled.
  Basis: affiliation inference. Topics: {ref}`RRAM <papers-topic-rram>`, … ·
  Fabrication (quoted from the abstract): "…" ·
  Related pages: {ref}`sky130B ReRAM <overview-sky130b-reram>` — reason.
  Note: … (when `notes` is set).
```

Grouping pages list one line per paper — "Title — First author et al.,
Venue series Year" with a `{ref}` to the full entry, a free-copy mark
and, for inferred records, the basis — so a record change touches one
place in the generated diff and pages stay small as the index grows. A
free-copy link equal to the landing page is not repeated. Topic sections
get `papers-topic-<topic>` labels. The pages use inline links rather than
footnotes: each full entry is itself a citation, the inventory stays the
store of cited sources, and `tools/check_refs.py` (which targets step,
category, machine, material, mask and overview pages) is unaffected.

## 5. Discovery

Recorded per record in `discovery`.

First round (2026-09-14):

* OpenAlex `title_and_abstract.search` for SKY130/SkyWater terms and
  spelling variants ("sky130", "sky130a", "skywater 130 nm",
  "open-source PDK", "open-source silicon", "Tiny Tapeout", "OpenMPW",
  "chipIgnite", "efabless", "caravel", …) and `fulltext.search` for
  "sky130";
* OpenAlex raw-affiliation search for SkyWater and for Cypress
  Semiconductor in Bloomington (2401 East 86th Street), and Cypress
  (US) works on SONOS and nonvolatile memory; OpenAlex works citing the
  included papers;
* Crossref bibliographic search (titles only; few Crossref records carry
  abstracts);
* Semantic Scholar's public search API without a key (heavily
  rate-limited);
* WOSET proceedings pages 2020–2024;
* the seed entries of `docs/references/public-sources.md`.

Second round (after the review, 2026-09-14):

* the review's 20 likely-missing papers, each checked against its
  abstract and, where retrievable, its full text (IEEE Access PDFs,
  WOSET PDFs, Wayback Machine copies of ACM landing pages, OSTI): one
  added (WOSET 2024 article 8), the rest excluded or held in
  `data/papers-excluded.yaml`;
* arXiv web search (the export API still answered HTTP 429) for
  "sky130", "skywater 130", "skywater", "open-source PDK", "open source
  PDK", "efabless", "caravel", "tiny tapeout", "open MPW", "sky130a",
  "sky130b", "openlane", "openram": 118 results, no new paper in scope;
* Crossref searches restricted by container title (ESSCIRC, CICC,
  MWSCAS, ISCAS, SSC Letters, JSSC, TNS, REDW, RADECS, ICMTS, IRPS, EDL,
  TED, JINST, LASCAS, Austrochip, NorCAS) for "sky130", "skywater 130",
  "skywater open source" and "open-source PDK 130": every hit was already
  triaged; no new paper in scope.

WOSET decisions (proceedings-page abstracts read for every article that
mentions SkyWater, SKY130, Caravel, Efabless, an MPW or a tape-out; PDFs
read where noted):

| Year | Included | Considered and not included |
|---|---|---|
| 2020 | article 3 (Edwards, the open PDK and its process stack) | 21 OpenLANE (flow; striVe tape-out, no process results), 4, 6, 7, 23 (tools and flows, no silicon or process results) |
| 2021 | — | 11 analog standard cell library (PDF: "in process for fabrication"; its measured version is the included TCAS-I 2024 paper), 15 FABulous (PDF: MPW area comparison only), 19 (flow manager) |
| 2022 | — | 5, 10, 13 (MPW-7 designs; tape-out experience, no silicon results), 8 (register-file generator) |
| 2024 | article 8 (Caravel asynchronous integration; SKY130 fill-density and power-ring findings) | 5 (IHP PDK), 13 (inductor flow, simulation), 15 (clock gating tool), 17 (OpenLane 2) |

Not available on 2026-09-14:

* OpenAlex search: the anonymous daily budget was exhausted ("Resets at
  midnight UTC"), so the hyphenated variants ("sky130-based",
  "skywater-130", "skywater 130-nm", "130-nm skywater", "skywater cmos",
  "skywater process") are still to run;
* arXiv export API (HTTP 429) and DBLP (connection refused);
* Semantic Scholar beyond a few pages (HTTP 429);
* FSiC publishes talks and slides, not papers, so it has no proceedings
  to search.

The next round should run the OpenAlex variants after the budget resets,
retry DBLP, and read the full texts of the held papers.

## 6. Generation and checks

* `tools/gen_papers.py` (to write) reads `data/papers.yaml` and writes
  the pages in §4, overwriting them; each page starts with a comment
  "Generated from data/papers.yaml by tools/gen_papers.py — do not edit".
  `--check` regenerates into memory and fails if a committed page
  differs, so a stale page cannot be merged; it also refuses to change
  or drop a `label` that exists in git. It joins the five page checkers
  in the pre-merge checklist.
* `tools/check_papers.py` validates both files offline: schema and key
  order; sort order; string ids and their formats; unique ids across both
  files and unique DOIs, arXiv ids and labels; label form and year;
  `title_display` free of TeX and backticks; https URLs with matching
  hosts and the free-copy allowlist; forbidden hosts, e-mail addresses,
  `mailto` and encoded addresses anywhere; renders, sheet and run/frame
  references anywhere; enumerated `basis`, `fabrication.source` and
  exclusion `status`; controlled topics; existing `docs/` labels with
  one-sentence reasons; existing inventory keys; non-empty institutions;
  dated `verified`, `checked` and `decided`; and consistency of
  `paywalled` with the listed copies. It prints "N papers checked, M
  problems".
* `--online` re-fetches every DOI from Crossref and compares title,
  author family names, year, container title, landing URL, volume,
  issue and pages; checks arXiv titles (also for DOI records with an
  arXiv id) and `web:` titles and authors on their proceedings page (a
  Wayback Machine URL is accepted as `landing_url`); and checks each
  fabrication quote against the abstract (OpenAlex or arXiv) or the arXiv
  HTML full text. `--links` re-fetches free copies and reports changed
  results. Both back off on HTTP 429; OpenAlex is used only for single
  records, not searches, so verification does not spend the search
  budget. Run both before each batch is merged.
* The Sphinx `-W` build then fails on any `{ref}` from a generated page
  to a label that does not exist.
* Each batch gets an independent review (fetch the DOIs and free copies;
  confirm every inclusion and basis against the abstract; confirm
  fabrication quotes against the paper) and a provenance review (no
  names from the renders site or the sheet; no non-public material; notes
  marked as inference where they are).
* The checker's host, e-mail, provenance, date and `related_docs` rules
  are the ones the patent and filings indexes will need; when those
  checkers are written, move the shared parts into one module
  (`tools/refindex.py`) rather than copying them.

Workflow for adding a paper: add the record (metadata from Crossref or
arXiv, institutions from the raw affiliation strings, open-access
locations from OpenAlex, free links fetched, a new `label`), or add it to
`papers-excluded.yaml` with a reason; run
`uv run tools/check_papers.py --online --links`, then
`uv run tools/gen_papers.py`, then the `-W` build.

## 7. Decisions and open questions

Owner decisions (2026-09-14):

* `web:` ids are kept for workshop papers without a DOI.
* The Bloomington fab and Cypress-era papers are kept, marked with
  `basis: affiliation-inference`, and grouped on their own "Fab
  publications (Bloomington)" page.
* The Stanford RRAM papers with a SkyWater co-author are kept, with the
  inference marked in `basis` and `notes`.

Open questions:

* Several free copies (MDPI, Wiley, TechRxiv, Authorea, eScholarship)
  answer scripted requests with HTTP 403, and IEEE sometimes with 202;
  they are kept with that result recorded, because the open-access
  location comes from OpenAlex or the preprint DOI. A browser check per
  batch would confirm them.
* The 2006 *Microscopy and Microanalysis* extended abstract is recorded
  by OpenAlex as bronze open access, but its Cambridge PDF URL returns
  HTTP 404 and the publisher page refuses scripted requests; it stays
  `paywalled: true` until a browser check finds a free copy.
* The held papers in `data/papers-excluded.yaml` (the 4 K open-silicon
  magazine article, the ICCAD 2020 OpenLANE paper, the Tiny Tapeout
  platform article and preprint, an SSRN image-sensor preprint and the
  HSWTech 2025 amplifier) need their full texts read.
