# Academic paper index — design

Status: proposal, 2026-09-14. Dataset phase done (`data/papers.yaml`,
`tools/check_papers.py`); pages not yet written. This file lives in
`docs/plans/`, which the Sphinx build excludes.

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
   extraction, design rules, extraction.
2. **Devices and test structures on SKY130** — measured devices, test
   structures, test vehicles and reliability, including radiation,
   cryogenic and high-temperature work, ReRAM/RRAM, SONOS, floating-gate,
   MiM, photonic or MEMS devices fabricated on the process.
3. **Silicon on SKY130 shuttles** — circuits and chips fabricated on the
   process (open MPW, ChipIgnite, Tiny Tapeout or other runs) where the
   paper reports silicon measurements or process-specific results.
4. **Lineage** — the Cypress S8 / SONOS 130 nm lineage and work from the
   Bloomington fab (Cypress Fab 4, later SkyWater), including the RRAM
   and monolithic-3D work at SkyWater from which the sky130B ReRAM
   module descends.

A paper is **excluded** when it only simulates with the PDK (unless it
characterises the process or its models), when the fabricated process
is not named in the public abstract or full text (the index does not
infer the process from authorship or shuttle context), when it is about
another SkyWater process (S90, 90 nm FDSOI, interposers, packaging), or
when it is not a paper (theses, datasets, software records, slides,
trade press). General textbooks and generic 130 nm papers stay in the
inventory only.

Borderline decisions are recorded in each record's `notes` field, which
starts "Borderline inclusion." where the case is marginal.

## 2. Dataset

`data/papers.yaml` is a YAML list, one mapping per paper, sorted by
year and title. It is the single source of truth; pages are generated
from it.

| Field | Content |
|---|---|
| `id` | `doi:<DOI in lower case>`; `arxiv:<id>` for arXiv-only papers; `web:<slug>` for workshop papers that have neither (currently WOSET only) |
| `title`, `authors`, `year` | as published: Crossref for DOIs, the arXiv abs page for arXiv, the proceedings page for `web:`; the conference year where the Crossref year is the later online date |
| `venue`, `venue_type` | container title; one of journal, magazine, conference, workshop, preprint, report |
| `doi`, `landing_url` | DOI as registered; publisher landing page from the Crossref `resource.primary.URL` (https) |
| `arxiv` | `null` or `{id, url}` |
| `paywalled` | `false` only when a free copy of the version of record is listed (publisher gold/hybrid/bronze/diamond, or an open proceedings page) or the paper is a preprint |
| `free_full_text` | list of `{url, host, oa_type, located_via, checked}`: arXiv, author or institutional repositories, OSTI, PubMed Central, conference open-access pages and publisher OA copies located through OpenAlex's open-access data (which is Unpaywall-derived) or the preprint's own DOI; `checked` records the date and HTTP result |
| `topics` | controlled list (§3) |
| `institutions` | OpenAlex normalised institutions, filtered against the raw affiliation strings, plus "SkyWater Technology" where a raw affiliation names SkyWater |
| `fabrication` | `null` or `{statement, source}`: the run or shuttle **as the paper states it** (abstract or full text) — never taken from the mask-renders site or the process-steps sheet |
| `related_docs` | `{label, reason}` pairs: a `{ref}` label under `docs/` and one sentence on why |
| `inventory_key` | the `public-sources.md` key when the paper is already in the inventory |
| `discovery` | how the paper was found (§5) |
| `notes` | borderline reasoning, what the abstract does and does not say |
| `verified` | `<ISO date> <source fetched>`: the DOI's Crossref record, arXiv abs page or proceedings page, with the title matched |

Rules that follow from the common agent rules:

* Claims in `notes`, `fabrication` and `related_docs` go no further than
  the abstract or the full text actually retrieved; anything else is
  marked as an inference with its basis (for example an affiliation).
* No e-mail addresses, and nothing in any request header or URL beyond
  the project user agent; the Crossref/OpenAlex `mailto` polite pool and
  the Unpaywall API (which requires an e-mail parameter) are not used.
* Never link Sci-Hub, Anna's Archive, LibGen, Z-Library or any other
  unauthorised copy; the checker rejects such hosts anywhere in a record.
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

Ecosystem and lineage: `tooling`, `education-shuttles`,
`fab-manufacturing`, `lineage-s8`.

The one-line definitions live in `tools/check_papers.py` (`TOPICS`),
which the generator will also use for section introductions. Adding a
topic means adding it there and to the page mapping in §4.

## 4. Proposed pages

All pages live under `docs/references/papers/`, are listed in a toctree
from `docs/references/index.md`, and are generated.

| Page | Label | Grouping |
|---|---|---|
| `index.md` | `papers-index` | Landing page: scope and inclusion rules (§1), counts by topic, year and access, how to read an entry, links to the other views, and the complete list sorted by first author |
| `by-topic.md` | `papers-by-topic` | One section per topic in §3 order, grouped under three headings (process, PDK and devices; circuits; ecosystem and lineage); each section opens with the topic definition and links to the process pages it relates to |
| `by-module.md` | `papers-by-module` | Entries grouped by the `related_docs` labels they carry: overview modules (for example the sky130B ReRAM page), steps, masks, machines and material classes, each heading linking the page; entries without related pages are listed at the end |
| `by-year.md` | `papers-by-year` | Newest year first |
| `by-venue.md` | `papers-by-venue` | Venue type, then venue name (IEDM, VLSI Symposium, ISCAS, ASMC/ISSM, IEEE Design & Test, arXiv, WOSET, …) |
| `by-institution.md` | `papers-by-institution` | Institution name, alphabetical; SkyWater Technology and Cypress Semiconductor first, as the fab's own publications |
| `by-device.md` | `papers-by-device` | Device or circuit type derived from topics: MOSFET models and cryogenic devices; RRAM; SONOS and floating-gate NVM; BEOL-integrated devices; analog and RF; data converters; power; digital and memory; sensors and quantum interfaces |

Entry format (identical on every page, so a reader recognises it):

```markdown
* **Title as published.** A. Author, B. Author and C. Author. *Venue*,
  2023. DOI [10.1109/…](https://doi.org/10.1109/…) ·
  [publisher page](https://…) · free copy: [arXiv](https://arxiv.org/abs/…) ·
  paywalled.
  Topics: {ref}`RRAM <papers-topic-rram>`, … ·
  Fabrication (as stated): "…" ·
  Related pages: {ref}`sky130B ReRAM <overview-sky130b-reram>` — reason.
  Note: … (when `notes` is set).
```

Only `index.md` carries one label per paper, `paper-<first-author
family>-<year><letter>` (for example `paper-hsieh-2019a`), assigned
deterministically in sort order, so that other pages can link a paper
with `{ref}`. Topic sections get `papers-topic-<topic>` labels. The
pages use inline links rather than footnotes: each entry is itself a
full citation, the inventory stays the store of cited sources, and
`tools/check_refs.py` (which targets step, category, machine, material,
mask and overview pages) is unaffected.

## 5. Discovery (as done for the first dataset)

Recorded per record in `discovery`:

* OpenAlex `title_and_abstract.search` for SKY130/SkyWater terms and
  spelling variants ("sky130", "sky130a", "skywater 130 nm",
  "open-source PDK", "open-source silicon", "Tiny Tapeout", "OpenMPW",
  "chipIgnite", …) and `fulltext.search` for "sky130";
* OpenAlex raw-affiliation search for SkyWater and for Cypress
  Semiconductor in Bloomington (2401 East 86th Street), and Cypress
  (US) works on SONOS and nonvolatile memory;
* Crossref bibliographic search (titles only; few Crossref records carry
  abstracts);
* Semantic Scholar's public search API without a key (heavily
  rate-limited);
* WOSET proceedings pages 2020–2024;
* the seed entries of `docs/references/public-sources.md`.

Not available on 2026-09-14: the arXiv export API and arXiv web search
returned HTTP 429 throughout (arXiv abs pages were fetchable and are
used for verification; arXiv papers indexed by OpenAlex were found
through it), DBLP refused connections, and from mid-session OpenAlex
search answered HTTP 429, so the hyphenated variants ("sky130-based",
"skywater-130", "skywater 130-nm", "130-nm skywater", "skywater cmos",
"skywater process") were not run. Google Scholar was not used.
The next batch should rerun arXiv and DBLP searches and add FSiC,
ESSCIRC, CICC and MWSCAS proceedings pages and the IEEE Xplore public
search pages.

## 6. Generation and checks

* `tools/gen_papers.py` (to write) reads `data/papers.yaml` and writes
  the pages in §4, overwriting them; each page starts with a comment
  "Generated from data/papers.yaml by tools/gen_papers.py — do not edit".
  `--check` regenerates into memory and fails if a committed page
  differs, so a stale page cannot be merged.
* `tools/check_papers.py` validates the dataset offline: schema and key
  order, unique ids and DOIs, DOI/arXiv/`web:` id formats, https URLs
  and matching hosts, forbidden hosts and e-mail addresses anywhere in
  a record, controlled topics, existing `docs/` labels with one-sentence
  reasons, existing inventory keys, dated `verified` and `checked`
  fields, and consistency of `paywalled` with the listed copies. It
  prints "N papers checked, M problems". `--online` re-fetches every
  DOI from Crossref and every arXiv abs page and compares titles; run it
  before each batch is merged.
* The Sphinx `-W` build then fails on any `{ref}` from a generated page
  to a label that does not exist.
* Each batch gets an independent review (reviewer brief: fetch at least
  a sample of DOIs and free copies; confirm every inclusion against the
  abstract; confirm `fabrication` statements against the paper) and a
  provenance review (no names from the renders site or the sheet; no
  non-public material; notes marked as inference where they are).

Workflow for adding a paper: add the record (metadata from Crossref or
arXiv, institutions and open-access locations from OpenAlex, free links
fetched), run `uv run tools/check_papers.py --online`, then
`uv run tools/gen_papers.py`, then the `-W` build.

## 7. Open questions

* `web:` ids depart from DOI/arXiv-only ids so that WOSET papers with no
  DOI can be listed; the alternative is to keep them out of the dataset.
* Several free copies (MDPI, Wiley, TechRxiv, Authorea, eScholarship,
  institutional handles) answer scripted requests with HTTP 403; they
  are kept with that result recorded, because the open-access location
  comes from OpenAlex or the preprint DOI. A browser check per batch
  would confirm them.
* OpenAlex institution normalisation is wrong for some affiliations
  (a Minnesota Cypress site normalised to Cypress Japan, a Colorado
  Springs company to a university); the dataset filters normalised names
  against the raw strings, but a reviewer should read the list.
* The fab-manufacturing and Cypress-era Bloomington papers do not name a
  process; they are included for the fab lineage and marked as such.
  If the owner prefers a stricter index, they move to a separate
  "fab publications" page or out of the dataset.
* Papers whose process is almost certainly SKY130 but not named in the
  abstract (for example open-source-silicon magazine articles and flow
  papers from 2020) are excluded until the full text is checked.
