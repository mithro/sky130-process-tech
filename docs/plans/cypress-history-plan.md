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
| Evidence: QTP | not started |
| Evidence: corporate | not started |
| Evidence: literature | not started |
| Claims matrix | not started |
| Pages | not started |
| Review | not started |
