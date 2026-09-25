# W0e — checker changes that unlock layout fixes — progress

Branch `topic/rd-checkers`. Task W0e of `docs/plans/readability-plan.md`
plus the generator of report-B finding B1 (`docs/plans/readability/report-B.md`
B1, B2, B8, section 2 "Table design rules", section 3 item 1;
`docs/plans/readability-guide.md` R-STEPRUN, R-INDEX, §5, §9). Working
through the five commits of the task brief in order, running the full
check suite and a `-W` build after each.

## Commit 1 — `check_masks.py`: `OPTIONAL_H3` for mask lithography H3s (done)

`OPTIONAL_H3["Lithography and pattern transfer"]` gained the five
headings B8 names (`Exposure class`, `Mask errors`, `Resist and tone`,
`Overlay and alignment`, `Pattern transfer`). Unlike the other two
`OPTIONAL_H3` entries (closed lists — any H3 not named there is still a
problem), this one needed to be a *floor*: report-B B8 says "then free
extras", i.e. any further H3 under this H2 is also allowed. Added a
second set, `OPEN_H3_H2 = {"Lithography and pattern transfer"}`, checked
before falling through to the closed-list logic. Extracted the H3
comparison loop out of `check()` into a standalone `check_h3(body)` so it
is unit-testable without building a full page/Index/pages fixture.

Added `--selftest` (the mask checker had none before): the five named
headings pass in any order/subset; a heading beyond the five also
passes; no H3 at all still passes (real mask pages are not converted in
this branch — that is a W3 batch, per the task); the other two
`OPTIONAL_H3` entries and an H2 outside it are still closed lists.

Not done, deliberately: converting any of the 36 mask pages' run-in
`**Bold.**` pseudo-headings to real H3s. That is W3 work; this commit
only unblocks the checker.

## Commit 2 — `check_machines.py`: two-column main-table support (done)

`index_rows()` required a matched line to have exactly 4 cells and read
`cells[3]` as the Steps cell. Generalised to `index_rows_from_lines()`:
any `| ` line whose first cell links a `machine-…` label is a row,
whatever the column count (>= 2), and its **last** cell is the Steps
cell. The old 4-column form still works unchanged (its last cell is
cell 3). Every existing check downstream of `index_rows()` (the per-list
set comparison, duplicate detection, `*also …:*` marker-wording
comparison) is untouched — they only consume the returned `{label:
steps_cell}` mapping, not the column count.

Added `--selftest`: old 4-column form, new 2-column form, a 3-column
in-between form, a 1-column line correctly *not* read as a row, "last
line wins" in both the old and new shapes, and a line with no machine
link in its first cell is not a row.

Kept in the docstring: the existing R-INDEX hazard note (a differently
shaped table with a machine link in its first cell, placed after the
main table, still silently overrides a checked row — this got no less
hazardous with the column-count restriction lifted; readability-guide.md
R-INDEX rule 4 already warns W3 executors about it and was not edited
here, since the task only asked for updates to §9 and R-STEPRUN).

## Commit 3 — `check_materials.py`: two-table / reader-facing-name support (done)

Two independent relaxations to `Index.__init__`'s main-table parsing,
both from report-B B2, **neither exercised by the committed
`docs/materials/index.md`, which keeps its current 6-column,
key-first shape** (restructuring the index itself is out of scope here
— that is W3):

1. **Steps from a second table.** If the main table's header's last
   cell does not mention "steps", the table is read as having no Steps
   column, and the Steps cell for each key is instead read from a
   second `Material | Steps`-shaped table in the same section
   (`read_steps_table()`), keyed the same way as the main table.
2. **Reader-facing name first.** The row's key no longer has to be the
   literal first cell (`` `key` ``): `find_key()` tries that first
   (so the current, real index page parses exactly as before), then
   falls back to a backtick key token embedded in the first cell or, if
   still not found, anywhere else in the row.

When the main table lacks a Steps column, the Class cell is no longer
read positionally either (its column is not fixed once the layout is
free to change) — the whole row is searched for the
`` {ref}`... <material-slug>` `` link instead, so the class/page
consistency check still runs. Noted in the docstring as a known,
deliberate scope limit: a row that happens to link two material pages
this way is not specially flagged.

Added a generic `table_blocks()` helper (any Markdown pipe table in a
section, as row cell-lists, separator rows skipped without ending the
table — an early version of this broke the header away from the data
row because it treated the separator line as ending the block; fixed by
recognising `|---|---|` as staying inside the table).

Added `--selftest`: builds two tiny two-page `materials/` fixtures in a
temporary directory (removed at the end) — one in the current shape, one
in the new no-Steps-column / reader-name-first shape with a second
`Material | Steps` table — and checks both parse to the same
`rows`/`owner` mapping with zero problems; also checks that a main table
with no Steps column *and* no second table is reported, not silently
missed.

## Full check suite after commits 1–3

`check_steps.py`, `check_refs.py`, `check_machines.py`,
`check_materials.py`, `check_masks.py`, `check_papers.py`,
`check_patents.py`, `check_filings.py`, `check_inforce.py`,
`gen_papers.py --check`, `gen_patents.py --check`, `gen_filings.py
--check`, `gen_index_links.py --check`: all 0 problems, unchanged
counts from `main`. `sphinx-build -W -q -b html docs tmp/_build/html`:
clean. The three new `--selftest`s all pass.

## Commit 4 — `tools/gen_step_tables.py` (B1) (done)

New generator, modelled on `gen_index_links.py`'s marker-delimited block:
inserts `<!-- step-tables:begin … --> … <!-- step-tables:end -->`
directly after the checked step-link run on every machine and material
page (`check_machines.STEPS_H3`/`check_materials.STEPS_H3` reused
directly, so the run is located exactly the same way the checkers
locate it — the two scripts can never disagree). `--check`,
`--selftest` (locate/extract/render logic on synthetic in-memory pages,
no repository files touched), idempotent (verified: a second run on
already-generated pages makes no change), deterministic.

* **≤ 25 links:** `{table}` `Step | Code | Name | Role on this page`
  (Step right-aligned; Code a fresh `{ref}` link with the step's code
  as text; Name from `tools/steps.csv`; Role from the run's own
  markers — "main" for the unmarked/only list, "alternative" for
  `*alternative:*`, or the `*also …:*` marker's own wording with the
  asterisks and trailing colon stripped — material-page runs have no
  markers, so every role there is "main"). 24 of 42 pages (22 machine,
  2 material: `cmp-consumables`, `sputter-targets`).
* **> 25 links:** `{dropdown}` titled "All N steps (links)" whose body
  adds nothing new, only a one-line pointer to the grouped bullets that
  already follow the run on the same page. 18 of 42 pages (8 machine,
  10 material).
* Ran over all 42 pages (30 machine + 12 material) in one commit, as
  asked. `check_machines.py`/`check_materials.py`: 0 problems on the
  generated result. Build: clean.
* Added `python tools/gen_step_tables.py --check` to `.readthedocs.yaml`
  `pre_build` (after `gen_index_links.py --check`, before
  `gen_figures.py --check`) and to both checklists in
  `docs/plans/agent-briefs.md` (the step-page writer brief's checker
  list, and the reviewer brief's item 5).
* Rendered three pages with `tools/shoot.py`, desktop and 400 px, and
  read the tiles: `machines/duv-krf-stepper` (table, 18 rows, several
  long names), `machines/wet-bench` (dropdown, 40 links), and
  `materials/cmp-consumables` (table, 12 rows). All three: clean
  columns, correct right-alignment on Step, no horizontal overflow at
  400 px, no cell wraps awkwardly, the dropdown's collapsed control
  renders like the page's other dropdowns. Nothing needed fixing.

### `tools/check_preserved.py` on the 42 changed pages

Ground rule 3 / the task's closing instruction: ran
`uv run python tools/check_preserved.py --allow-added refs,numbers
docs/machines/*.md docs/materials/*.md`. Two things showed up beyond
the declared `refs`/`numbers` additions, both investigated to ground
truth and both verified **not** a content loss:

1. **`ADDED number_order` on 24 pages** (every table page), always the
   same shape, e.g. `('130', '8', '14', '46', '32')`. Cause: the
   generated table's caption line (`:::{table} SKY130 steps assigned to
   this class`, containing "130" from "SKY130") and its `:widths: 8 14
   46 32` line are two adjacent non-blank lines with no list/table
   marker, so `extract_number_order`'s paragraph splitter treats them
   as one prose "sentence" and records their numbers' left-to-right
   order as one new tuple. MyST's colon-fence syntax requires directive
   options to immediately follow the directive line (no blank line
   between), so this cannot be avoided by reformatting while keeping a
   caption that mentions "SKY130" and a `:widths:` line — any table
   whose caption contains a number, followed by its widths line, would
   do this. No `LOST number_order` anywhere (confirmed). Re-ran with
   `--allow-added refs,numbers,number_order` for the record; this is
   the third declared category and is recorded here with its reason,
   as `agent-briefs.md` "Checking a readability edit" asks.
2. **`{dropdown} block count changed` / reindexed dropdowns on the 18
   pages that got a new dropdown.** `check_preserved.py` compares
   dropdowns *by position*, so inserting one new dropdown before a
   page's existing ones (the in-force patent notes, always further
   down) shifts every later dropdown's index and makes each one print
   as "changed" even though its text is untouched. Verified this is
   positional-only noise, not a real edit, two ways: (a)
   `git diff --numstat main -- docs/machines docs/materials` shows
   **zero deletions in all 42 files** (pure insertion), so no existing
   character was touched anywhere; (b) for a sample page (`wet-bench.md`)
   read the diff directly — the only change is the new block. Re-ran
   with `--allow-dropdown-edits` for the record.
3. **Two pages still report `LOST`/`ADDED quotes` even with both flags
   above: `docs/machines/starting-material.md` and
   `docs/machines/single-wafer-spin-processor.md`.** Root-caused this
   fully rather than accepting it on faith:
   `check_preserved.extract_quotes` pairs `"..."` marks strictly
   left-to-right, non-overlapping, minimum 1 character between marks.
   Both pages contain, pre-existing on `main`, a quoted phrase that
   itself ends in an inch mark immediately followed by the closing
   quote — `"Laser marking system, 8""` (starting-material.md) and
   `(8")"` (single-wafer-spin-processor.md) — i.e. two `"` characters
   with **zero** characters between them. Since the regex requires at
   least one character between marks, it cannot match that adjacent
   pair as a (degenerate, empty) quote; it matches the *first* of the
   two as the close of the *previous* quote instead, and the *second*
   becomes an orphaned "open" that pairs with whatever `"` comes next —
   which, on both pages, is dozens to hundreds of characters later,
   consuming ordinary prose as if it were quoted text. This
   mis-pairing cascades for the rest of the page's body. It is **not**
   caused by this branch: confirmed with `check_preserved.extract_all`
   that `strip_existing(new) == old` byte-for-byte on both pages (i.e.
   removing the generated block restores the committed `main` text
   exactly), and that the raw quote-mark count in each page's body is
   odd (189 on starting-material.md, 171 on
   single-wafer-spin-processor.md) independent of any edit here. Any
   future edit to either page that changes the flattened text at all
   (even one with zero quote characters, as this one does) can shift
   which spurious pairing the heuristic lands on, which is exactly
   what happened. This is a pre-existing fragility of
   `check_preserved.py`'s quote heuristic (documented in its own
   docstring as "necessary, not sufficient") meeting a pre-existing
   `8""`/`(8")"` inch-mark-before-closing-quote sequence already on
   `main`; **not fixed here** (out of scope: `check_preserved.py` is a
   different, already-merged W0b branch, and the inch-mark phrasing is
   page content, not this branch's to rewrite). Flagged for the
   coordinator. No actual quotation was added, changed or lost on
   either page — verified by the byte-identical `strip_existing`
   check above, which is definitive regardless of what the heuristic
   reports.

Final command run for the record:
`uv run python tools/check_preserved.py --allow-added
refs,numbers,number_order --allow-dropdown-edits docs/machines/*.md
docs/materials/*.md` → "44 page(s) checked against main, 2 with
undeclared differences" (the two pages in point 3 above, both verified
harmless).

## Commit 5 — `docs/plans/readability-guide.md` §9 and R-STEPRUN updates (done)

* §9 blocked-rules table: `R-H3 on mask pages`, `R-INDEX, machines main table`, `R-INDEX, materials
  main table` and `R-STEPRUN, generated tables` all changed from their `Wxx` blocker to
  **unblocked** (`topic/rd-checkers`), each with a one-line "done:" note saying what actually
  changed and, for the two `R-INDEX` rows and the `R-H3` row, an explicit reminder that the *content*
  work (restructuring the two indexes; converting the 36 mask pages' `**Bold.**` labels to H3s) is
  still a separate **W3** batch — this commit only unblocks the checkers, per the task brief.
* R-STEPRUN's own section (§4): reworded **Kind** to say the table/dropdown is generated, never
  hand-written, names `tools/gen_step_tables.py`, and tells a future hand-editor to re-run it (or
  `--check`) after any edit that changes a run's steps or markers.
* For internal consistency with the two edits above (avoiding a same-document contradiction one
  paragraph away), also updated: the §3 summary table's `R-STEPRUN`/`R-INDEX` "Blocked" cells, and
  R-INDEX's own "Do (blocked until W0e)" paragraph (§4) to "Do (unblocked, `topic/rd-checkers`)" with
  the same W3-content-work caveat.
* **Deliberately not touched** (out of the task's stated scope — "§9 and R-STEPRUN" only): the other
  scattered `W0e`/mask-H3 mentions elsewhere in the guide (§2 "Never" list item 9's "until W0e";
  §3's `R-H3` summary row; §4's `R-H3` section body; the MyST-crib mock-up annotations around line
  1591). These are now stale in the same sense the ones above were, but re-touching every mention
  across the whole guide was a much larger, more error-prone edit than the task asked for. Flagging
  this for the coordinator/whoever starts the W3 mask-H3 batch (B8): read §9's `R-H3 on mask pages`
  row (now accurate) rather than the older, now-stale mentions elsewhere.

## Remaining (this branch)

None — all five commits of the task are done. Final full check suite and `-W` build re-run after
commit 5 below.

## Decisions and things to flag for the coordinator

* The materials-index two-table/reader-name-first design (commit 3) is
  necessarily speculative: no concrete W3 design for the new index
  layout exists yet. The contract implemented (Steps-column detection
  by header wording; key found by `find_key()`; Class cell found by
  scanning the whole row when there is no Steps column) is documented
  in the checker's own docstring so a future W3 executor can read it
  before designing the real layout, rather than reverse-engineering it
  from the diff.
* No factual, numeric or citation content was touched by commits 1–3
  (checker/tooling only, no `docs/**/*.md` content pages changed).
