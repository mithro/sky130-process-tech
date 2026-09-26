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
* Writers: Opus for content batches from 2026-09-26 (see `model-comparison.md`); Sonnet for scripted and
  tool work. Reviewers: Opus, looking at the rendered result with `tools/shoot.py` as well
  as the diff. One worktree and branch per task; small commits; a progress file per branch; no rebase or
  force-push by agents; the coordinator merges fast-forward.
* A model that finds an arithmetic slip or factual doubt while re-presenting text reports it; it does not
  fix it in a readability branch.

## Workstreams

### W0 — tooling and theme (first; everything else depends on it)

| Id | Task | Source | Status |
|---|---|---|---|
| W0a | `docs/_static/custom.css` (footnote back-reference wrap, table cell alignment and zebra rows, sticky header, first-column stickiness on phones, 44 em text measure, caption and glossary-term styling), `footnote-popover.js`, `conf.py` entries | C2, C3, C12, B §3.2 | [x] merged 2026-09-20 (reviewed; sticky first column and keyboard navigation dropped after review) |
| W0b | `tools/check_preserved.py` — before/after preservation check used by every hand-edit branch | A §2, B §3.4 | [x] merged 2026-09-20; second round 2026-09-25 (fence skipping, numbered labels, tabulation regroups under `--allow-regrouped`, `Q4 2020`, inline-code masking); third round 2026-09-26 (role/code-span masking, per-paragraph quotes to 800 chars, wider hedge list, `--allow-deduplicated`, word-multiset diff with `--strict-words`, glance and SkyWater-says warnings) |
| W0c | Citation policy: reword citation-style rule 5; add the "inline URL must equal a URL in the page's own footnote definitions" invariant to `check_refs.py` with a self-test; promote the dry-run script to `tools/fix_reading_list_links.py`; run it site-wide (about 6,200 bullets); hand-finish the leftovers under C1 rules 2–3; link named titles in prose (C4, 172 cases) | C1, C4, A F14, B10 | [x] merged 2026-09-20 (reviewed): 6,580 reading-list heads linked, all 568 Wikipedia bullets; 395 multi-marker, 77 in-dropdown, 16 role-in-head, 6 no-URL bullets left; 46 named titles linked in prose; `check_refs.py` invariant; `--refresh` mode |
| W0d | Generators: sync `gen_steps.py` with the committed index intro, group the step index by module, short sidebar titles, `Machine class` and `Mask` columns, `--check`; `gen_index_links.py` heading and title link text; `gen_patents.py` clickable URLs and index order (papers, filings the same) | A F13, F17, B2, B11, C8, C11 | [x] merged 2026-09-20 (reviewed; B9 step-link text done here too) |
| W0e | Checker changes that unlock layout fixes: `check_machines.index_rows` (two-column main table), `check_materials.Index` (steps from a second table), `check_masks.OPTIONAL_H3` | B2, B8 | [x] merged 2026-09-25 (reviewed): the three checkers relaxed with selftests; `tools/gen_step_tables.py` generates the step tables / collapsed link runs on all 42 machine and material pages |
| W0f | Links: fix the Wayback lookup in `check_links.py` (retry, no long-lived negative cache, CDX fallback), add `--suggest-archive` and `--include-generated`; apply the archive-first citation form to every dead link; re-check THUNG-2016 | C5 | [x] merged 2026-09-20 (content diff checked by the coordinator; report `docs/plans/link-check-2026-09b.md`). Two sources moved to verified Wayback copies, one handled under rule 11; soft-404 suspects and bot-challenge redirects now detected (136 DOI links were never really verified: publisher bot wall); generated pages checked for the first time — 4 dead tokens there need their second check after 2026-09-21, fix via `archive_url` in `data/*.yaml`; a list for a human with a browser is in the report |

### W1 — figures

| Id | Task | Status |
|---|---|---|
| W1a | Productionise the prototype: `tools/gen_figures.py` (+ `--check`, embedded width table, no new dependency), `data/figures/`, `docs/_static/figures/`, `figure-theme.js`, tokens file, "Figure conventions" page, `check_inforce.py` hook for figure specs | [x] merged 2026-09-20 (reviewed; leader routing rewritten, in-force screen covers all figure text) |
| W1b | First set for a look before scaling: isolation series S1 (steps 001–013), the module flow map on the overview, the back-end stack chart | [x] merged 2026-09-20 — 16 figures; authoring guide `docs/plans/figure-authoring.md` |
| W1c | Remaining series S2–S11 (series files by Opus, fact-checked against their pages; per-step figure specs by Sonnet) | [~] S2 wells (014–034) merged 2026-09-25 after review: faded context layers as dashed outlines, pattern-only implant overlay, one-panel rule for steps with no drawn change, figure-after-dropdown placement rule. S3 SONOS + S4 gate oxides (035–047) merged 2026-09-25 after review (new lint: paired gutter legs, labels below the drawing; `arc` material). S5 poly (048–063) merged 2026-09-25 after review (`dope` can target a named film; leader lint covers highlight strokes). S6 tips/halos/spacers/S-D (064–088) merged 2026-09-25 after review (close-up windows; ion arrowheads fixed site-wide; dots only on visible material; no leader through a beam). S7 MOL (089–106) merged 2026-09-25 after review (leader-rise limit; per-figure leader routes; close-ups at finer sampling; faded films keep colour in close-ups). S8 contact + metal 1 (107–117) merged 2026-09-26 after review (emulator: rounded conformal films, gap-fill PSG, straight tapers; cut close-ups marked; level codes no longer read as numbers). S9a via 1 – metal 3 (118–134) merged 2026-09-26 after review (series templates; thin liners; leftover-placeholder lint). S10 MiM (135–140, 150–153) merged 2026-09-26 after review (`etch_materials` template parameter with lints; metal 3 patterned at 139–140). S9b (141–149, 154–163) and S11 passivation (164–170) to do; 171 gets a prober block-chain |
| W1d | Machine block-chains (30), mask derivation chains (36), category mechanism sketches (10), remaining charts | [ ] |

Default taken on the open point in report D: figures may show a value that the page gives as its own reading,
always with the `our reading` tag and the hedge repeated in the caption. Reversible by the owner: the lint
can be switched to `public` only.

The owner asked for the style to live in a claude.ai design-system project. That needs the owner's
`/design-login`; until then `tokens.json` and the generated preview page are the single source and are laid
out so the sync is a copy.

### W2 — step pages (171), hand edits in module batches

Status: pilot 001–013 merged 2026-09-25 after an Opus review, a fix round and a verification round; the
guide was corrected from it (14 rulings + 8 new rules) and `check_preserved.py` gained `--allow-regrouped`,
an `identifiers` category, flattened hedge matching and inch-mark masking. Batch 2 (014–034, wells) merged 2026-09-25 after review, fix round, verification and a
short final round. Batch 3 (035–047, SONOS + gate oxides) merged 2026-09-25 after review, fix round, verification and
a final round; the guide now forbids any edit inside an in-force note. Batch 4 (048–063, poly) merged 2026-09-26: written by Opus, 0 High / 3 Medium on first review, one
small fix round. Batch 5 (064–075, tips and halos) merged 2026-09-26: Opus writer, 0 High / 1 Medium, one small round.
Batch 6 (076–088, spacers and source/drain) merged 2026-09-27: Opus writer, 0 High / 1 Medium, one small
round. Batch 7a (089–097) merged 2026-09-27: Opus writer, 0 High / 1 Medium, one small round. Batch 7b (098–106) merged 2026-09-27: Opus writer, 0 High / 1 Medium, one small round. Steps 001–106
done. Each module's figures land before its batch.

Order per page: structure under H2 (A F2) → tables and derivations (F3, F5) → lists (F6, F7) → paragraph and
sentence splits (F1, F8) → tool evidence items (F4) → fixed-pattern sections (F15) → hedge placement and
repetition (F9, F10) → "At a glance" box last (F11). Batches follow the thirteen modules.
In-force dropdown titles stay as they are (owner's wording).

### W3 — machine, material, mask, category pages and their indexes

Status: the three index pages (machines cards + two-column lookup, materials per-material tables, masks
"Find a mask" table, methodology moved below the lookups, captions) merged 2026-09-25 after review and a
fix round. The twelve material pages merged 2026-09-26 after review, fix round, verification and a one-row
round (specification tables now `Material | Source | What the source says`). Machine pages 1–15 (cd-sem … pecvd) merged 2026-09-26 after review, fix round, verification and a
final round (Year cells hold only the model's year; `:widths:` is inert). Mask pages 1–18 (cap2m … npcm) merged 2026-09-26: Opus writer, 0 High / 4 Medium on first review, one
small round. The ten category pages merged 2026-09-26 (Sonnet writer; review, fix round, verification, final round —
nine lost markers and a false rewording caught in review). Machines 16–30 to do; masks 19–36 in progress.

B1 step tables (generated), B3 index reorder, B4 model tables, B5 quick facts, B6 entry tables, B7 category
comparisons and links to material pages, B8 mask H3s (after W0e), B9 step-link text (scripted), B12–B15.

### W4 — site level

Status: landing page (cards, module table, hidden toctrees), references index table, glossary by letter,
inventory anchors + entry order + hover-card link, and the overview (guided-tour order, module H3s, prose
rules) merged 2026-09-25 after Opus reviews. The first-use `{term}` links were taken OUT of the branch: the
tool `tools/link_terms.py` (skip list, context guards, 3 per paragraph, opt-out marker, `--report`) runs once
on `main` as the final pass after the content batches merge.

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
| 2026-09-20 | Guide, theme + preservation checker, generators, figure tooling + first 16 figures merged, each after an Opus review and a fix round. W0c and the step-page pilot (001–013) started. |
| 2026-09-26 | Merged: step batches 048–063 and 064–075 (Opus writers), machine pages 1–15, material pages, category pages, mask pages 1–36, index pages, figures S6–S10 (steps 001–140, 150–153), check_preserved round 3, in-force fixes on masks onom/tunm and step 041. Launches paused at ≈64 of the 75-point quota share until the 2026-10-01 reset. |
| 2026-09-25 | Merged: pilot 001–013 (+ guide corrections), W0e checkers + step tables, figures S2–S5, site pages, overview, checker round 2, in-force patent leaks on 037–044 (found by the S3/S4 figure review; `check_inforce.py` PHRASES extended), second dead-link check on generated pages (`archive_url`/`dead_since` in the papers dataset; report `link-check-2026-09c.md`), the Cypress history section from another session. |
