# Plan: Cypress process technologies before S8

Started 2026-09-25. Branch `topic/cypress-history`, worktree
`.worktrees/cypress-history`.

## Goal

Add a history of the process technologies Cypress Semiconductor
developed before S8, the 130 nm SONOS process that SKY130 comes from.
For each technology the history gives:

* where it was developed and which fab or foundry ran it;
* the parts made on it;
* its stackup (metal layers and their films, passivation, gate oxide,
  design rule);
* how it relates to S8 and SKY130.

## Constraints

* **Separate section.** The history lives in its own top-level section,
  `docs/history/`, with its own toctree. It must not change the SKY130
  overview, the step, machine, material or mask pages, or the indexes.
  The only link into it is one line on the landing page.
* **Every claim has at least two independent public sources**, and the
  sources are compared with each other. No source is trusted on its own:
  not Cypress, not SkyWater, not Infineon, not the trade press. Where
  sources disagree, the page shows the disagreement and does not pick a
  side silently. A claim that has only one source is labelled as
  single-source.
* The common rules of `agent-briefs.md` apply (public sources, user
  agent, British spelling, ISO dates, no staff names, no sub-agents of
  your own). Qualification reports print the names of the staff who
  prepared and approved them; never copy those names.
* The pages follow `readability-guide.md` from the start, so they need
  no separate readability pass.

## Evidence files

Evidence is kept as data, with verbatim quotes that can be checked
against the source, in the style of `data/filings.yaml`:

| File | Content | Producer |
|---|---|---|
| `data/history/qtp.yaml` | Every public Cypress qualification report (QTP), PCN or PIN that names a technology from before S8, plus the S8 reports that date S8's first qualifications: identifier, date, URL, technology code, fab, parts, the process-description block verbatim, and the qualification-history rows verbatim | agent `cyhist-qtp` |
| `data/history/corporate.yaml` | Statements from Cypress's SEC filings, annual reports, press releases and the trade press about process technologies, fabs, foundry partners, technology transfers and dates, 1982–2010 | agent `cyhist-corporate` |
| `data/history/literature.yaml` | Technical papers, patents, conference talks, teardown and cross-section reports, white papers and data sheets that describe Cypress processes before S8 (stackups, devices, masks, lineage) | agent `cyhist-literature` |

Common record fields: `id`, `source` (bibliographic), `url`,
`archive_url` (Wayback copy where one exists), `retrieved`, `quotes`
(each with `text`, verbatim, and `location`), `claims` (short
normalised facts that the quotes support: technology, attribute,
value), `notes` (conflicts with other sources).

Shared fetch cache: `tmp/cyhist-cache/` in the main checkout
(`qtp/`, `filings/`, `web/`). Save every fetched document there and
look there before fetching.

## Pages (`docs/history/`)

The pages are drafted once the evidence exists. The provisional list:

| Page | Content |
|---|---|
| `index.md` | What the section covers, a lineage figure, a timeline table of the technologies with dates, fabs and nodes |
| `naming.md` | How Cypress named its technologies (family letter, generation number, suffixes), only as far as the sources show it |
| `fabs.md` | Cypress's own fabs (Fab 1 San Jose, Fab 2 Round Rock, Fab 3 and Fab 4 Bloomington) and its foundry partners, with the technologies each ran |
| one page per technology family | Stackup table, products, fabs, dates, and relationship to S8 |
| `stackups.md` | Stackups of all the technologies side by side |
| `s8-lineage.md` | How the earlier technologies led to S8 and SKY130, with evidence and open questions |

## Checks (agreed with the readability coordinator, 2026-09-25)

* `tools/check_history.py` imports `check_refs.check()` and
  `inline_link_problems()` and runs them on `docs/history/*.md` against a
  history-only inventory, `docs/history/sources.md`, generated from the
  pages' footnotes by `tools/gen_history_sources.py` (anchor line, the
  citation with its URL, and the pages that cite it; a source defined two
  ways is an error). It also checks the claims matrix
  `data/history/claims.yaml`: every claim needs two independent sources,
  or is marked single-source in the prose the way
  `readability-guide.md` marks inferences. It has a `--selftest`, sits in
  the `pre_build` list of `.readthedocs.yaml`, and appears in both check
  lists of `agent-briefs.md`.
* The same tool checks that the footnotes and the evidence are the same
  documents. Every footnote on a history page must carry the `url` or
  `archive_url` of an evidence record (a filing's `urls`, a patent's
  number). In every claim, each source must be a document one of the
  claim's footnotes points at, and each footnote must have a source.
  So a reader who follows a footnote reaches exactly the evidence the
  claims matrix counted, and the quotes in that record are checked
  against a cached copy by `tools/check_history_quotes.py`.
* Every evidence record must carry `origin`, `url`, `retrieved` and
  `quotes` (`check_history.py`).
* `tools/check_history_quotes.py` (local; it needs the fetch cache) checks
  every evidence quote against the cached copy of its source, and every
  phrase the pages put in double quotes against the cached copies of the
  sources that paragraph cites. `…` splits a quotation; `[…]` marks an
  editorial insertion.
* `tools/history_cache.py` keeps the evidence re-checkable from what is
  committed: `status` lists what the cache holds, `archive` and `hash` add
  Wayback captures and SHA-256 values to the records, and `rebuild DIR`
  fetches every source afresh and re-finds every quote without the cache.
* `tools/check_links.py` must pick up the history pages' URLs, and
  `tools/fix_reading_list_links.py` must convert their reading-list
  bullets. Run both on the pages and confirm it.
* `tools/check_inforce.py` scans all of `docs/`. Any patent it does not
  treat as certainly expired goes in a collapsed note, as on the other
  pages.

## Workflow

1. Three research agents (Sonnet), one worktree and branch each
   (`topic/cyhist-qtp`, `topic/cyhist-corporate`,
   `topic/cyhist-literature`), each with a progress file
   `docs/plans/progress-cyhist-<name>.md`.
2. The coordinator merges their evidence into `topic/cypress-history`
   and builds a claims matrix that checks that every claim has two
   sources.
3. Pages are written from the matrix.
4. An independent Opus review, rendered pages included, then a fix
   round, a provenance check, and a hand-off to the readability
   coordinator for merging.

## Status

| Item | State |
|---|---|
| Plan | written 2026-09-25 |
| Evidence | `qtp.yaml`, `corporate.yaml`, `extra.yaml` and `literature.yaml` (papers and patents); every quote verified against a cached copy; counts in each file |
| Claims matrix | about 200 claims, checked by `tools/check_history.py`, with every claim's sources tied to its footnotes |
| Pages | index, fabs, technologies, sonos-s4, s8-lineage, naming; generated stackups, products, sources |
| Review r1 (Opus) | 19 High, 22 Medium, 15 Low; fixes applied 2026-09-25 |
| Review r2 (Opus) | 1 High, 10 Medium, 14 Low; fixes applied 2026-09-25 |
| Evidence integration | the round-3 QTP records, the literature evidence and the link and page-quote checks, 2026-09-25, branch `topic/cyhist-evidence`; the remaining QTP groups continue on `topic/cyhist-qtp4` |

Not done, for the owner: some research-branch commit messages need the owner's review under the
history-rewrite policy (review r1, H12/H13).
