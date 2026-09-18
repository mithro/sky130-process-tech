# Topic index links — progress

Status: in progress, 2026-09-19. Task: link every process page to the
patent, paper and filings indexes that concern it, with in-force/unknown
patents collapsed. This file lives in `docs/plans/`, which the Sphinx
build excludes.

## Design decisions

1. **Source of truth stays the three datasets.** `tools/gen_index_links.py`
   (PEP 723, `uv run`, `pyyaml` only) reads `data/patents.yaml`,
   `data/papers.yaml` and `data/filings.yaml` plus a docs-wide label scan
   (`check_patents.doc_labels()`, reused rather than duplicated) and
   rewrites one generated block per page. It writes nothing to the three
   datasets themselves.

2. **`related` field on papers: already there.** `data/papers.yaml`
   already carries a validated `related_docs: [{label, reason}]` field
   per record (`check_papers.py` already checks the labels exist and the
   reasons are one sentence); it was added for the papers-by-module
   index page and only needed to be *read* by this generator, not
   invented. Likewise `data/filings.yaml` already has `related_docs`.
   No dataset schema change was needed for either. (One label existence
   check was re-verified for both: every `related_docs` label used
   already resolves to a docs page — see Verification below.)

3. **Scope = "process pages".** A page qualifies for a generated block
   when its label is (a) a `relevance.target` in `data/patents.yaml`,
   (b) a `related_docs.label` in `data/papers.yaml`, or (c) a
   `related_docs.label` in `data/filings.yaml` — **and** the label
   resolves (via the docs-wide label scan) to a file outside
   `docs/references/` and `docs/plans/`. This keeps the direction
   strictly "index → process page" here; the reverse direction
   (index pages linking back) is already handled by `gen_patents.py` /
   `gen_papers.py` / `gen_filings.py` themselves (checked, not changed).
   A label that resolves inside `docs/references/` (there are none
   today) would be silently skipped by construction, since only
   `docs/steps`, `docs/categories`, `docs/machines`, `docs/materials`,
   `docs/masks` and `docs/overview` hold process pages.

4. **Granularity is the physical file, not the label.** Some pages
   define several labels (`docs/overview/index.md` has `overview-index`,
   `overview-modules`, `overview-cross-section`, …). Every dataset
   record naming any label on a page contributes to that page's single
   block; the block does not say which specific label matched — it is
   navigation, not annotation of one part of the page.

5. **Insertion point.** Immediately before the page's `## References`
   heading, which every step, category, machine, material, mask and
   overview page has exactly once (verified across all 205 pages that
   receive a block — see Verification). The generator finds
   `\n## References\n`, strips any existing
   `<!-- index-links:begin -->` … `<!-- index-links:end -->` block
   (wherever it is) plus its surrounding blank lines, and reinserts the
   current block (or nothing) with exactly one blank line on each side,
   matching the file's existing spacing convention. If a page no longer
   qualifies (a dataset shrinks), the block and its markers are removed
   entirely — `--check` catches a stale or hand-edited block because the
   stripped-and-reinserted text must match the file on disk byte for
   byte.

6. **Block content** (heading-less; bold inline lead-ins, not `#`/`##`
   headings, so `check_steps.py`/`check_machines.py`/`check_materials.py`/
   `check_masks.py`'s heading-adjacency checks are unaffected):
   * **Related patents** — expired families as
     `` {ref}`PN <patent-gpNNNN>` — Title (year)``, sorted by priority
     date; then, if any families are in force or of unknown status, one
     collapsed `{dropdown}` titled "*N* families in force or status
     unknown" listing each as
     `` {ref}`PN <patent-gpNNNN>` — in force`` /
     `` — unknown`` (reusing `gen_patents.family_link_line`'s own
     non-expired branch verbatim, so the wording matches the grouped
     pages) plus one fixed sentence that status and expiry are public
     estimates, not legal advice.
   * **Related papers** — `` {ref}`paper-label` `` lines, reusing
     `gen_papers.line()` verbatim (same wording as `by-module.md`).
   * **Related filings** — reusing `gen_filings.short_line()` verbatim.
   * **Overflow (>12 in one category on one page).** Only two pages hit
     this today: `docs/steps/040-ono.md` (42 patent families — SONOS/ONO
     is heavily patented) and `docs/overview/index.md` (72 filings — the
     corporate-lineage filings mostly cite the process overview
     generically). For these, the category's full list is replaced by
     one sentence with the count and a `{ref}` to the matching grouped
     page (`patents-by-module` for patents, `papers-by-module` for
     papers, `filings-by-relationship` for filings) — no patent numbers
     at all appear on the process page in this case, so the "in force ⇒
     collapsed" rule is trivially satisfied (nothing to hide).
   * Nothing here is a citation and nothing states a fact about the
     process, so it needs no footnotes.

7. **`check_refs.py`: no change needed.** It only ever looks at
   `[^label]` footnote syntax and the `### Deep dive` list; the
   generated block uses only `{ref}` roles, so it is invisible to
   `check_refs.py`'s regexes as either a reference or a Deep-dive entry.
   This is recorded here per the brief's instruction to say how, rather
   than left unstated.

8. **Checker changes (`check_steps.py`, `check_machines.py`,
   `check_materials.py`, `check_masks.py`).** Each gets one new check:
   if the page contains `<!-- index-links:begin -->`, the block content
   between the markers must equal what `tools/gen_index_links.py` would
   write for that page's label(s) today (imported and called directly,
   not shelled out), and a page that `gen_index_links.py` says should
   have a block must have one. This is what "extended to know the block
   and fail if stale or hand-edited" means in practice; the substantive
   staleness/hand-edit detection lives in one place
   (`gen_index_links.py`'s own diff logic) and each page checker just
   calls it, rather than four copies of the diff logic. `--selftest` on
   `gen_index_links.py` covers the block-building logic in isolation
   (strip/reinsert idempotence, threshold boundary, dropdown wording,
   multi-label-one-file merging) without touching the repo.

9. **Module grouping pages already exist for every module a step page
   points to.** `patents-by-module.md` and `papers-by-module.md` are
   generated from `STEP_MODULES`/module-prefix tables that already cover
   every step 1–171 plus category/machine/material/overview groups
   (checked by `gen_patents.py`'s own `check_step_modules()` guard); no
   new module pages were needed for constraint 3.

## Counts (from the datasets as of 2026-09-19)

* **205 process pages receive a block**: 144 step pages, 28 machine
  pages, 13 material pages, 9 category pages, 9 mask pages, 2 overview
  pages (`overview/index.md`, `overview/sky130b-reram.md`). The
  remaining 28 step pages, 3 machine pages, 2 mask pages and 2 category
  pages have no relevant patent, paper or filing record and get no
  block.
* **Patents:** all 252 families in `data/patents.yaml` are linked from
  at least one process page (182 expired, 47 in force, 23 unknown
  status). 745 relevance entries collapse to 745 (page, family) links
  after dedup by family per page. One page (`step-040`) exceeds the
  12-entry threshold (42 families: 33 in force, 5 unknown, 4 expired)
  and gets a count + link instead of a list.
* **Papers:** 21 of the 50 papers in `data/papers.yaml` have
  `related_docs` and are linked from 13 distinct labels (all ≤ 12 on any
  one page today — the largest is 10, on `overview-sky130b-reram`).
* **Filings:** 80 of the 86 filings in `data/filings.yaml` have
  `related_docs`, resolving to 5 labels. `overview-index` (72 filings)
  exceeds the 12-entry threshold and gets a count + link instead of a
  list; the other four labels (`machines-index` 4, `overview-sky130b-reram`
  4, `materials-index` 3, `step-001` 1) list individually.

## Verification

* Every `relevance.target` / `related_docs.label` used by the three
  datasets resolves to a docs label (checked with a throwaway script in
  `tmp/`, cross-checked against `check_patents.doc_labels()`); none
  resolves inside `docs/references/` or `docs/plans/`.
* All 205 target files contain exactly one `## References` heading and
  none is a stub (`This page is a stub.`), so the insertion point is
  unambiguous everywhere and no stub page gets a premature block.

## Remaining work in this pass

* Write `tools/gen_index_links.py` with `--check` and `--selftest`.
* Extend `check_steps.py`, `check_machines.py`, `check_materials.py`,
  `check_masks.py` per item 8.
* Run `tools/gen_index_links.py` to generate the 205 blocks, committed
  separately from the code by page type (steps, then
  machines+materials+masks+categories, then overview).
* Add "How the indexes link to the process pages" to
  `docs/references/index.md`.
* Add `gen_index_links.py --check` to the README's checker list and to
  `docs/plans/agent-briefs.md` Reviewer brief item 5.
* Full verification pass: all `check_*.py`, all four `gen_*.py --check`,
  `-W` Sphinx build, and an HTML grep confirming in-force patent numbers
  only ever appear inside `<details>` on process pages.
