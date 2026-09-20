# Readability and formatting — work plan

Started 2026-09-20. The content is written and checked; this phase makes it readable. Four reviewers read
samples of every page type in source and as rendered (desktop and phone) and wrote rule sets:
`docs/plans/readability/report-A.md` (step pages), `report-B.md` (machine, material, mask, category pages and
indexes), `report-C.md` (navigation, links, references, theme), `report-D.md` (figures). Prototypes are under
`docs/plans/readability/prototypes/`. Rendered pages are inspected with `tools/shoot.py` (headless Chrome,
tiles a page into PNGs; `--width 400` for the phone layout; accepts `file://` for the local build).

The executor-facing rules are consolidated in `docs/plans/readability-guide.md` (rule ids `R-…`). This file
is the order of work and its status.

## Ground rules for every branch

* Presentation only: no fact, number, quotation, hedge or citation may change or disappear.
  `tools/check_preserved.py` (W0) compares a page before and after: the multisets of footnote markers,
  numbers and quoted strings must match (apart from declared additions such as step names in new tables).
* All checkers, generator `--check`s and the `-W` build pass before review.
* Writers and fixers: Sonnet. Reviewers: Opus, looking at the rendered result with `tools/shoot.py` as well
  as the diff. One worktree and branch per task; small commits; a progress file per branch; no rebase or
  force-push by agents; the coordinator merges fast-forward.
* A model that finds an arithmetic slip or factual doubt while re-presenting text reports it; it does not
  fix it in a readability branch.

## Workstreams

### W0 — tooling and theme (first; everything else depends on it)

| Id | Task | Source | Status |
|---|---|---|---|
| W0a | `docs/_static/custom.css` (footnote back-reference wrap, table cell alignment and zebra rows, sticky header, first-column stickiness on phones, 44 em text measure, caption and glossary-term styling), `footnote-popover.js`, `conf.py` entries | C2, C3, C12, B §3.2 | [ ] |
| W0b | `tools/check_preserved.py` — before/after preservation check used by every hand-edit branch | A §2, B §3.4 | [ ] |
| W0c | Citation policy: reword citation-style rule 5; add the "inline URL must equal a URL in the page's own footnote definitions" invariant to `check_refs.py` with a self-test; promote the dry-run script to `tools/fix_reading_list_links.py`; run it site-wide (about 6,200 bullets); hand-finish the leftovers under C1 rules 2–3; link named titles in prose (C4, 172 cases) | C1, C4, A F14, B10 | [ ] |
| W0d | Generators: sync `gen_steps.py` with the committed index intro, group the step index by module, short sidebar titles, `Machine class` and `Mask` columns, `--check`; `gen_index_links.py` heading and title link text; `gen_patents.py` clickable URLs and index order (papers, filings the same) | A F13, F17, B2, B11, C8, C11 | [ ] |
| W0e | Checker changes that unlock layout fixes: `check_machines.index_rows` (two-column main table), `check_materials.Index` (steps from a second table), `check_masks.OPTIONAL_H3` | B2, B8 | [ ] |
| W0f | Links: fix the Wayback lookup in `check_links.py` (retry, no long-lived negative cache, CDX fallback), add `--suggest-archive` and `--include-generated`; apply the archive-first citation form to every dead link; re-check THUNG-2016 | C5 | [ ] |

### W1 — figures

| Id | Task | Status |
|---|---|---|
| W1a | Productionise the prototype: `tools/gen_figures.py` (+ `--check`, embedded width table, no new dependency), `data/figures/`, `docs/_static/figures/`, `figure-theme.js`, tokens file, "Figure conventions" page, `check_inforce.py` hook for figure specs | [ ] |
| W1b | First set for a look before scaling: isolation series S1 (steps 001–013), the module flow map on the overview, the back-end stack chart | [ ] |
| W1c | Remaining series S2–S11 (series files by Opus, fact-checked against their pages; per-step figure specs by Sonnet) | [ ] |
| W1d | Machine block-chains (30), mask derivation chains (36), category mechanism sketches (10), remaining charts | [ ] |

Default taken on the open point in report D: figures may show a value that the page gives as its own reading,
always with the `our reading` tag and the hedge repeated in the caption. Reversible by the owner: the lint
can be switched to `public` only.

The owner asked for the style to live in a claude.ai design-system project. That needs the owner's
`/design-login`; until then `tokens.json` and the generated preview page are the single source and are laid
out so the sync is a copy.

### W2 — step pages (171), hand edits in module batches

Order per page: structure under H2 (A F2) → tables and derivations (F3, F5) → lists (F6, F7) → paragraph and
sentence splits (F1, F8) → tool evidence items (F4) → fixed-pattern sections (F15) → hedge placement and
repetition (F9, F10) → "At a glance" box last (F11). Batches follow the thirteen modules.
In-force dropdown titles stay as they are (owner's wording).

### W3 — machine, material, mask, category pages and their indexes

B1 step tables (generated), B3 index reorder, B4 model tables, B5 quick facts, B6 entry tables, B7 category
comparisons and links to material pages, B8 mask H3s (after W0e), B9 step-link text (scripted), B12–B15.

### W4 — site level

Landing page cards and module table (C6); overview reorder, H3 per module, "On this page" (C7); glossary by
letter, Phase cell terms, first-use `{term}` links (C9); inventory anchors and sentence order (C10);
references index table.

## Decisions taken by default (owner can reverse)

* Reading-list heads become links and markers stay (C1/C4); marker-free links are not used.
* Quick-facts cells may shrink when the removed text is already in the body or is moved there with its
  citations (B5).
* Mask renders are linked, not embedded as thumbnails.
* The metal-cap section stays on the overview; the inventory stays one page (anchors added).
* The materials `Key` column stays (checker contract) but moves out of the reader's first column only if W0e
  makes that safe.
* No Mermaid/Graphviz dependency; all figures come from the generator.

## Log

| Date | Event |
|---|---|
| 2026-09-20 | Four review reports and prototypes in; plan written. |
