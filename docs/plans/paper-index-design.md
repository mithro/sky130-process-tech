# Academic paper index — design

Status: 2026-09-19 (round 3, verified). Dataset, generator and pages
done and reviewed four times (`data/papers.yaml`, `data/papers-excluded.yaml`,
`data/papers-labels.yaml`, `tools/check_papers.py`, `tools/gen_papers.py`,
`docs/references/papers/`). Round 3 added a `names_process` field (with
`authors` and `venue`) to `data/papers-excluded.yaml` and a generated
page, `designed-on-sky130.md`, listing the excluded/held records that
name the process (§2.2, §4). An independent verification of round 3
(`tmp/verify-index-papers-r3.md`, findings V3-01…V3-12) found two
inclusion decisions that contradicted exclusions made in the same
commit and a `names_process` definition drawn from the wrong text; all
required and follow-up fixes are applied (`paper-pepel-2025a` and
`paper-yu-2022a` moved to `held`, §1.4's 130 nm-flow rule and §1.3's
tape-out rule written down, `names_process` recomputed from each
record's own title/abstract). Not yet done: links to the paper pages
from pages outside `docs/references/` (deferred on instruction; see §7).
This file lives in `docs/plans/`, which the Sphinx build excludes.

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
   paper reports silicon measurements or process-specific results, **or**
   states that the design achieved tape-out on a named SKY130 run, even
   without a reported measurement (round 3, V3-05: this is the test the
   index actually applies in practice, e.g. `paper-singhani-2023a`,
   `paper-teo-2024a`, `paper-wang-2024a`; a "fabrication-ready" or
   pre-tape-out layout is not enough).
4. **Lineage and the fab** — the Cypress S8 / SONOS 130 nm lineage, work
   from the Bloomington fab (Cypress Fab 4, later SkyWater), and the RRAM
   and monolithic-3D work at SkyWater from which the sky130B ReRAM module
   descends. This basis is for the **130 nm flow specifically**: a paper
   from a Bloomington-fab programme that reports work at another node
   (for example the MIT × SkyWater CNFET programme's 90 nm devices) is
   out under the other-SkyWater-process clause below unless it also
   reports the 130 nm line, the way `paper-srimani-2023a` does ("90/130nm
   technology node"); a paper from the same programme whose own abstract
   does not state a node is `held`, not included, once a sibling paper
   from the same authors and year states a different node (round 3,
   V3-02).

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
| `venue`, `venue_series`, `venue_type` | container title as registered (pages drop catalogue numbers such as "(Cat. No.01CH37203)" and trailing punctuation); a normalised series for grouping — the full name for journals and magazines ("IEEE Transactions on Electron Devices"), the usual acronym for conferences and workshops (`ASMC`, `ISSM`, `IEDM`, `VLSI Symposium`, `ISCAS`, `ICM`, `WOSET`), and `arXiv`; one of journal, magazine, conference, workshop, preprint, report |
| `volume`, `issue`, `pages`, `article_number` | from Crossref where registered, otherwise `null`, so that every entry is a full citation |
| `doi`, `landing_url` | DOI as registered; publisher landing page from the Crossref `resource.primary.URL` (https) |
| `arxiv` | `null` or `{id, url}` |
| `paywalled` | `false` only when a free copy of the version of record is listed (publisher gold/hybrid/bronze/diamond, or an open proceedings page) or the paper is a preprint |
| `free_full_text` | list of `{url, host, oa_type, located_via, checked}`: arXiv, author or institutional repositories, OSTI, PubMed Central, conference open-access pages and publisher OA copies located through OpenAlex's open-access data or the preprint's own DOI; the host must be on the checker's allowlist; `checked` records the date and HTTP result |
| `topics` | controlled list (§3) |
| `basis` | §1 |
| `institutions` | every institution named in the raw affiliation strings (OpenAlex) or on the paper itself (arXiv HTML, OSTI record, proceedings page), with OpenAlex display names used only for spelling; never empty |
| `fabrication` | `null` or `{quote, source}`: an **exact** quotation from the paper naming the process, foundry, run or shuttle, or stating the fabrication or silicon result (omissions marked "[…]"); shown on pages as "Process and fabrication (quoted from …)", and `source` one of `abstract`, `full text (HTML)`, `full text (PDF)` |
| `related_docs` | `{label, reason}` pairs: a `{ref}` label under `docs/` and one sentence that claims no more than the paper says |
| `inventory_key` | the `public-sources.md` key when the paper is already in the inventory |
| `discovery` | how the paper was found (§5) |
| `notes` | borderline reasoning, what the abstract does and does not say, and the inference for non-`named-process` records |
| `verified` | `<ISO date> <source fetched>`: the DOI's Crossref record, arXiv abs page or proceedings page, with the title matched |

### 2.2 `data/papers-excluded.yaml`

A YAML list of `{id, title, authors, year, venue, status, names_process,
reason, decided}`, where `status` is `excluded` (outside §1) or `held`
(possibly in scope; waiting for a full-text check, for example because
the abstract does not name the process and the publisher refuses
scripted requests). An id may not appear in both files. A held paper
moves to `papers.yaml` when its full text is read and names the process.

`authors` (a list, empty when not recorded — for example a workshop
paper with no proceedings page) and `venue` (a string, or null when not
recorded) are the same citation fields as `papers.yaml`, gathered from
Crossref, OpenAlex or the arXiv record. `names_process` is `true` when
the record's own title or retrieved abstract names SKY130, the SkyWater
130 nm process or the SkyWater foundry — the literal test behind `basis:
named-process` in §1, applied here to records that do not meet the
inclusion rules. It is computed from the paper's own text, **never**
from the `reason` prose (a record can be excluded *because* its own text
does not name the process, and the reason then has to say so; that
sentence must not make the record read as if it names the process).
Round 3 added these three fields and backfilled them for every record
already in the file (2026-09-19), fetching each record's own abstract
(OpenAlex, or the arXiv summary) to compute `names_process`; two
`web:woset-*` records have no fetchable abstract, so their `title` alone
was used. `tools/gen_papers.py` lists every `names_process: true` record
on `docs/references/papers/designed-on-sky130.md` (§4); because some
records genuinely do name a SkyWater process or site (S90, a 90 nm
node, a different fab location) while reporting real measured silicon
just not on SKY130, and one (a slide deck) genuinely reports measured
SKY130 values, the page's lead says this explicitly rather than
claiming every listed record reports no fabrication. The offline check
only validates that `names_process` is a boolean; `--online` re-fetches
each record's own abstract and fails if the stored value disagrees with
a fresh recomputation. The page lets a reader of the academic literature
on SKY130 find work that uses the PDK even where it stops short of the
index's evidential standard.

### 2.3 `data/papers-labels.yaml`

An append-only YAML list of `{label, id, previous_ids, published}`, one
entry for every page label ever published. `check_papers.py` requires
every record's label to be in the map with its id and every mapped label
to be still used by the same paper, so a label cannot be dropped, renamed
or reused; an id correction adds the old id to `previous_ids`. A paper
that turns out not to meet §1 after its label was published (round 3,
V3-01/V3-02) moves to `papers-excluded.yaml`; its label-map entry is
left exactly as published (same id, same `published` date) so the label
stays reserved, and `check_labels()` treats a label whose id is in the
exclusions file as a valid reclassification rather than a dropped label.
`gen_papers.py --check` also compares the map with its versions at the
merge base with `main` and at `HEAD`, so a change that is already
committed on a branch still fails.

### 2.4 Rules

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

Circuits designed for or fabricated on the process: `analog-rf`, `mixed-signal`,
`power-management`, `digital`, `memory`, `sensors`, `quantum`,
`security`.

Ecosystem and lineage: `tooling`, `education-shuttles` (papers about a
shuttle programme or its educational use, not every paper that used a
shuttle), `fab-manufacturing`, `lineage-s8`.

The one-line definitions live in `tools/check_papers.py` (`TOPICS`),
which the generator uses for section introductions and checks against its
display names. The circuit topics describe what a paper is about, not
whether it has silicon results; the inclusion rules in §1 and the entry's
quotation and notes say that. Adding a
topic means adding it there and to the page mapping in §4. A derived
shuttle grouping, if wanted, is taken only from `fabrication.quote`.

## 4. Pages

All pages live under `docs/references/papers/`, are listed in a toctree
from `docs/references/index.md`, and are generated.

| Page | Label | Grouping |
|---|---|---|
| `index.md` | `papers-index` | Landing page: scope (`papers-scope`), basis and inclusion rules (§1), access counts, year counts linking the by-year sections, a topic table (non-fab papers, with a column for fab publications that share the topic, and a row for the fab page), how to read an entry, links to the other views, and **the only full entry for each paper**, sorted by label (first author's family name, then year) |
| `fab-publications.md` | `papers-fab-publications` | "Fab publications (Bloomington)": the `fab-manufacturing` records, all `affiliation-inference`, grouped by the company named in their institutions (a name containing "Cypress" or "SkyWater"; the generator fails if a record names neither or both) |
| `by-topic.md` | `papers-by-topic` | One section per topic with papers, in §3 order under three headings, each opening with the topic definition and, for RRAM, BEOL integration and SONOS, links to the related process pages; fab publications are not listed but counted ("Also N fab publications with this topic"); topics without papers are named in one closing line |
| `by-module.md` | `papers-by-module` | "Papers by related page": entries grouped by their `related_docs` labels (overview, step, mask, category, machine and material pages) with the reasons; papers without a related page at the end |
| `by-device.md` | `papers-by-device` | PDK and process overviews; transistor models, characterisation and cryogenic operation (excluding work on memory devices); RRAM; SONOS and floating-gate NVM; BEOL-integrated devices; test structures, reliability and radiation; analog and RF; data converters; power; digital logic, memory and security; sensors and quantum interfaces — fab publications counted as on the topic page |
| `by-year.md` | `papers-by-year` | Newest year first, each year labelled `papers-year-<year>` |
| `by-venue.md` | `papers-by-venue` | `venue_type`, then `venue_series` |
| `by-institution.md` | `papers-by-institution` | Cypress Semiconductor and SkyWater Technology sections first; the other institutions in one alphabetical table with links to their papers |
| `designed-on-sky130.md` | `papers-designed-on-sky130` | Round 3: **not part of the index** — every `data/papers-excluded.yaml` record with `names_process: true` (§2.2), grouped by year, title-then-year within a year; each line gives the title, authors, venue, year, DOI/arXiv link and the existing exclusion `reason` verbatim, with a **Held** mark for `status: held`. Linked from `index.md`'s "Other views" list with an explicit note that it does not meet §1, and given one `{ref}` back to `papers-scope`. |

Full entry format (on `index.md` only):

```markdown
(paper-hsieh-2019a)=
### Title (title_display)

A. Author, B. Author and C. Author. "Title." *Venue*, vol. V, no. N,
pp. P, 2019.

* **Publication:** [IEEE Xplore](https://…) (paywalled) · DOI [10.1109/…](https://doi.org/10.1109/…) · arXiv […](https://arxiv.org/abs/…)
* **Free copies:** [arXiv](https://…) — preprint; … (or "none located")
* **Basis:** process named (see {ref}`papers-scope`).  — or, for inferred records: affiliation inference — definition. Note explaining the inference.
* **Topics:** {ref}`RRAM (ReRAM) <papers-topic-rram>`, …
* **Institutions:** …
* **Process and fabrication (quoted from the abstract):** "…"
* **Related pages:** {ref}`overview-sky130b-reram` — reason.
* **Note:** … (named-process records with notes)
* **Checked:** 2026-09-14 against the Crossref record.
```

For arXiv-only records the Publication line gives the arXiv id as a free
preprint and the Free copies line lists only other copies. The title
appears both as the heading and in the citation so that the citation
line is complete when copied.

Grouping pages list one line per paper — a `{ref}` to the full entry
(its text is the title), first author et al., venue series and year, and
marks for a free copy and an inferred basis — so a record change touches
one place in the generated diff and pages stay small as the index grows.
The pages use inline links rather than footnotes: each full entry is
itself a citation, the inventory stays the store of cited sources, and
`tools/check_refs.py` (which targets step, category, machine, material,
mask and overview pages) is unaffected. Text is escaped for Markdown and
single-line fields are enforced by the checker.

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

Third round (after the independent review of round 2, 2026-09-19):

* OpenAlex `fulltext.search` for `sky130` (348 works) and `skywater` (696
  works), paged through in full (round 2 had stopped at 600 of 696 for
  `skywater`); triaged by abstract (or, where the match was full-text-only,
  by the query tag itself as evidence that the term appears in the
  document). Found four included papers the round 2 sweep missed
  (paper-dubey-2023a, paper-li-2024a, paper-teo-2024a,
  paper-baungarten-leon-2024a) and about three dozen excluded/held
  records now in `data/papers-excluded.yaml`;
* OpenAlex `raw_affiliation_strings.search:SkyWater` (35 works, one page —
  round 2 had not re-run this surface since round 1). Most of the
  SkyWater-Bloomington CNFET/RRAM/monolithic-3D strand this surfaced was
  already in `data/papers.yaml` or `data/papers-excluded.yaml` from
  earlier rounds; added two device papers (paper-bishop-2020a,
  paper-yu-2022a) and one reliability paper (paper-pepel-2025a) as
  `affiliation-inference`, and recorded five more as excluded (a
  different node, a different SkyWater site, or a layout-only
  contribution) so they are not re-argued. The Kissimmee, FL MIM-capacitor
  paper and the 90 nm TID/RTN papers are recorded excluded per the design's
  other-SkyWater-process exclusion (§1);
* OpenAlex citing-works (`filter=cites:`) of every `named-process` paper
  in `data/papers.yaml` that carries a `fabrication` quote and a DOI (33
  seeds, up to 200 citing works each); no new in-scope paper found beyond
  what the surfaces above already located. See
  `docs/plans/progress-index-papers-r3.md` for the per-seed counts;
* the review's own 13-item table and its "not triaged at all" list were
  individually verified against Crossref and OpenAlex (or arXiv) and
  added to one file or the other.

The next round should retry DBLP, read the full texts of the held
papers (leading with `doi:10.1109/sbmicro70495.2026.11684413`, the
cryogenic SPICE model calibrated on experimental 4 K data), and consider
a second raw-affiliation pass for "Cypress" alongside "SkyWater" to catch
earlier Bloomington-era lineage work the same way.

## 6. Generation and checks

* `tools/gen_papers.py` reads `data/papers.yaml` and writes the pages in
  §4, overwriting them; each page starts with a comment "Generated from
  data/papers.yaml by tools/gen_papers.py; do not edit". It first runs
  `check_papers.py`'s offline record and label-map checks and stops on
  any problem. `--check` regenerates into memory and fails if a committed
  page differs, is missing or is not generated, and if the label map lost
  or changed an entry since the merge base with `main` or `HEAD` (§2.3).
  `check_papers.py` and `gen_papers.py --check` are in the pre-merge
  checklists of `docs/plans/agent-briefs.md`.
* `tools/check_papers.py` validates both files offline: schema and key
  order; sort order; string ids and their formats; unique ids across both
  files and unique DOIs, arXiv ids and labels; label form and year;
  `title_display` free of TeX and backticks; https URLs with matching
  hosts and the free-copy allowlist; forbidden hosts, e-mail addresses,
  `mailto` and encoded addresses anywhere; renders, sheet and run/frame
  references anywhere; enumerated `basis`, `fabrication.source` and
  exclusion `status`; controlled topics; existing `docs/` labels with
  one-sentence reasons; existing inventory keys; non-empty institutions;
  dated `verified`, `checked` and `decided`; single-line titles, notes,
  quotes and reasons; the label map (§2.3); and consistency of
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

Owner decisions (2026-09-19, round 3):

* No new controlled topic was added for the SkyWater-Bloomington
  device-R&D strand (carbon-nanotube FETs, monolithic-3D RRAM,
  radiation/RTN reliability): the existing topics already fit the
  records found (`beol-integration`, `rram`, `device-characterisation`,
  `reliability`, `radiation`, as the pre-existing entries for this
  strand already show), so §3's topic list is unchanged.
* `data/papers-excluded.yaml` gained `authors`, `venue` and
  `names_process` (§2.2) and a generated page listing the
  `names_process: true` records (§4), per the round 2 review's
  recommendation. `papers.yaml`'s inclusion rules (§1) are unchanged.

Deferred and not adopted:

* Links to the paper pages from outside `docs/references/` (the fab page
  from the related machine pages, paper labels from step or overview
  pages) are deferred: this phase adds the pages only to the references
  landing page.
* A "silicon" mark on grouping lines is not adopted: silicon status is
  not a data field, and deriving it from quotations or notes would claim
  more than the records say.
* The page review suggested dropping the title from the citation line;
  it is kept so that the citation is complete (§4).
* Commit 4204e04 (the generated pages) does not build under `-W` on its
  own because the toctree entry landed one commit later (41e6694); the
  branch history is not rewritten, and the two can be squashed when
  merging.

Open questions:

* `paper-bishop-2020a`'s `fabrication.quote` is sourced from the
  publisher's own abstract (nature.com meta description, retrieved
  2026-09-19), because OpenAlex and Crossref both carry no abstract for
  this record; `--online`'s quote check only fetches OpenAlex or arXiv,
  so it reports "quote not found" for this one record even though the
  quote is correct (verified by hand against the publisher page). Worth
  teaching `--online` to fall back to a publisher-page fetch when
  OpenAlex has no abstract, rather than special-casing this one id.
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
* (Round 3, R2-21) Slide decks and conference presentations that carry
  measured SKY130 data (for example `doi:10.5281/zenodo.18008454`,
  Silicluster v2) are excluded under the "not a paper" rule (§1) even
  where a closing slide reports a real measured value. Owner decision
  needed on whether a presentation with a genuine, attributable
  measurement should instead be included with a note that it is a
  presentation rather than a paper.
* (Round 3) IEEE magazine articles (*Solid-State Circuits Magazine*,
  *Design & Test*, *Spectrum*) are judged on content like any other
  paper (R2-22): several are included (`paper-li-2024a`,
  `paper-dubey-2026a`) and several excluded or held on their abstract.
  This is now stated here rather than left implicit.
