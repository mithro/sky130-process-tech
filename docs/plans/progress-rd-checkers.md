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

## Review response (independent review, verdict "approve with fixes": 1 High, 4 Medium, 7 Low)

Coordinator ruling on H1: the generator owns the whole presentation. Implemented exactly as ruled;
fixed all four Mediums; addressed every Low (one recorded as not applicable). Re-ran the full check
suite, all four `--selftest`s, the `-W` build, and regenerated all 42 pages after every change.

### H1 — the >25-link dropdown held no links; collided with R-STEPRUN

Per the coordinator's ruling, `gen_step_tables.py` now owns the whole presentation:

* **<= 25 links:** the run stays in the open, byte-identical, untouched — exactly as before. The
  generated block (a table) still goes directly after it.
* **> 25 links:** the generator now **wraps the run itself** — on a material page, the `Steps:` line
  and the run together — in a collapsed `{dropdown}` titled "All N steps as one line of links (checked
  against the index)". This is the *entire* generated block: no separate table, no pointer sentence, no
  link repeated outside the dropdown.

Implementation: `strip_wrap()` (new) undoes a previous wrap by matching the exact generated pattern
(begin marker, fence-open + title, blank line, the wrapped span captured verbatim, fence-close, end
marker) and replacing the whole thing with just the captured span — restoring the page's un-wrapped
form before the run is re-located. This runs *before* `strip_existing()` (the old trailing-block
stripper), which would otherwise delete the run along with the markers if it ever saw a wrap. `apply_wrap()`
splices the new wrap in by replacing `text[wrap_start:run_end]` with the rendered wrap — no padding
needed, since that span already sits between the same blank lines it always did.

**Verified with the real checkers** (not just this script's own copy of the selection logic): after
regenerating all 42 pages, `check_machines.py` and `check_materials.py` both report 0 problems —
including on the 8 machine and 10 material pages whose run is now wrapped in a dropdown. This confirms
the coordinator's/review's claim that a dropdown's opening fence+title line carries no step link, so it
is skipped by the "first non-bullet block with a step link" rule the same way a bullet list is, and the
run — now the fence's body — is still that first block; on material pages, wrapping `Steps:` and the run
together keeps the run "the paragraph directly after a line reading `Steps:`".

**Idempotence and no-nesting**, both unit-tested and checked end to end: `gen_step_tables.py --check`
reports 0 pages differing immediately after a plain run; the selftest re-runs `process_text` on its own
wrapped/tabled output for three cases (table, machine wrap, material wrap) and asserts the text is
unchanged and the dropdown count does not change (case 5); a hand-edited wrap title is corrected back to
the canonical form rather than accepted (case 7).

Guide: R-STEPRUN's **Do** section rewritten so it describes what the generator does (run it; never
hand-build a table or dropdown) rather than instructing a human to build one; the placement rules are
kept (now phrased "verified with a wrapped and an unwrapped run"); the worked examples now show the
real `wet-bench.md`/`process-gases.md` output. §9's `R-STEPRUN, generated tables` row updated to
describe the new design and cite this review finding.

### M1 — the second (Steps) table had no uniqueness/completeness check

`check_materials.read_steps_table()` now reports: a row with fewer than two cells; a row with no key at
all; a key used twice; and, after both tables are read, any steps-table key not present in the main
table ("steps table names key 'x', which is not in the main table"). Added selftest fixtures
`EXTRA_KEY_INDEX`, `DUPLICATE_KEY_INDEX`, `NO_KEY_ROW_INDEX`, one assertion each.

### M2 — the Role column carried no information when every role was "main"

`gen_step_tables.render_table()` drops the `Role on this page` column entirely (header and every row)
when the run's roles are not all different (`len({role for role, _ in entries}) > 1`). Material-page
tables never show it, since material runs have no markers so every role is always "main" — matching B1's
"Role only from the page's markers", which invents nothing there. Column widths adjusted:
`:widths: 10 16 74` (3 columns) or `10 16 58 16` (4). Verified on the real docs: `cmp-consumables.md` and
`sputter-targets.md` (the two material table pages) both drop the column; 12 of 22 machine table pages
also drop it (uniform "main"); `duv-krf-stepper.md` (mixed main/alternative) keeps it.

### M3 — the materials `Index` rejected a main table split into groups under H3s

New `_table_blocks_by_header()`: every table block under `## Materials index` whose header equals the
first block's is read as more of the same table, not only the first block (report-B B2 table rule 7,
"> 40 rows: split by group"); every other block is read the same way as the second "Material | Steps"
table (also possibly split into groups), sharing one header; a block matching neither is reported.
Selftest fixtures `GROUPED_MAIN_INDEX` (old, key-first shape, two H3 groups) and `GROUPED_NEW_INDEX`
(no-Steps-column shape, both tables split into two groups each) both parse to the expected two-key
`rows`/`owner` mapping with zero problems. The real, un-grouped `docs/materials/index.md` still passes
unchanged (0 problems).

### M4 — `check_masks` `OPEN_H3_H2` made the five B8 headings inert

`check_h3()`'s `OPEN_H3_H2` branch now also: rejects a synonym B8 says to merge
(`FORBIDDEN_H3_SYNONYMS = {"Resist": "Resist and tone", "Overlay": "Overlay and alignment", "Alignment":
"Overlay and alignment"}`) with the canonical name named in the message; rejects a heading that is one
of *another* section's mandatory H3s (e.g. `### Deep dive` copied into the wrong place) unless it is
itself one of this H2's own named headings; and requires the named five, when present, to appear in
canonical order (this changed one existing selftest case — "a subset, reordered, passes" — to now
expect a problem; renamed and kept as the in-canonical-order positive case instead). Four new selftest
cases (three synonyms plus the mandatory-heading-reuse case).

### Lows

* **L1 (garbled reviewer-brief text).** Fixed: `docs/plans/agent-briefs.md`'s reviewer-brief checklist
  had a duplicated "up to date, not stale or hand-edited)," fragment (introduced when the earlier
  commit inserted the `gen_step_tables.py --check` mention between two pre-existing fragments).
  Rewritten to one clean sentence per the review's suggested text.
* **L2 (a duplicate machine label silently let the last line win).** Fixed: `index_rows_from_lines()`
  now returns `(rows, duplicates)`; `main()` reports every duplicated label as a problem. The returned
  `rows` mapping still carries the last line's value (so a caller has *something* to compare against),
  but the page is now flagged. New selftest cases for both the old and new table shapes, plus a
  negative case (a single matching line is not a false-positive duplicate).
* **L3 (silent `?` / silent empty block on failure).** Fixed: `render_table()` raises `ValueError` if a
  step number is not in `tools/steps.csv` (was: silently emitted `"?"`); `process_text()` raises
  `ValueError` if the located run contains no entries (was: `render_block` returned `""`, and the
  generator would then quietly emit no block at all rather than fail loudly). Both are exercised by
  selftest case 8.
* **L4 (docstring overclaimed "reuses" the checkers' code).** Reworded: the module docstring's "Known
  scope" paragraph now says plainly that `locate_machine_run`/`locate_material_run` are "two
  implementations of the same rule, not one shared function", verified to agree with the real checkers
  on every page as of this commit, rather than claiming they "can never disagree".
* **L5 (caption repeats the H3; header cells render centred).** Both fixed. Caption is now
  `"The N step(s) above: number, code and name"` (dynamic, no H3 text repeated, no page-type
  branching needed since the table only exists for the <= 25-link, unwrapped case now). Header
  centring: the separator row's alignment markers are now explicit (`:---` for Code/Name/Role, `---:`
  for Step) instead of bare `---`; confirmed in the built HTML that every `<th>` now carries a
  `text-left`/`text-right` class instead of falling back to the browser's centred default for a `<th>`
  with no alignment class (this is a real, previously-unnoticed rendering quirk of *every* unaligned
  column in *every* pipe table sitewide, not unique to this generator; fixing it site-wide would be a
  CSS/theme change, out of scope here — this fix only covers this generator's own table).
* **L6 (selftest gaps).** Fixed: `gen_step_tables.py`'s cases 6/7 (previously near-duplicates) are now
  a genuine determinism check (two independent runs on the same fresh input) separate from the
  idempotence check (case 5, re-running on already-generated output); a new case 9 exercises `--check`
  semantics end to end (via `generate()`, with `MACHINES`/`MATERIALS` monkey-patched to a temporary
  directory): 0 pages differ once written, and a source change is detected again. `check_machines.py`
  gained an end-to-end `check()` test (case 7): a matching page/index pair reports nothing, and a
  "Steps not last" malformed index row (the real Steps content in an earlier cell, so the always-last
  Steps cell is something else) is caught as a mismatch. `check_materials.py` gained the M1/M3 fixture
  cases above (were the "gap" the review named).
* **L7 (stale W0e mentions elsewhere in the guide).** Not further addressed beyond what commit 5
  already recorded as a deliberate scope limit (progress file, "Commit 5" section above) — the review
  itself says this is "acceptable as flagged" and only asks that R-STEPRUN rules 2 and 4 be reconciled
  with what the generator now emits once H1 is decided, which is done above (R-STEPRUN's **Do** section
  and §9 row).

### R4 — `check_preserved.py` quote-pairing finding

**Not touched** (explicit coordinator instruction: `tools/check_preserved.py` belongs to the pilot
branch, not this one). The review corrected the mechanism this branch's progress file had originally
described (not "zero characters between the marks" — a `)` can sit between them, as in `(8")"`) and
found a third affected page (`docs/references/public-sources.md:11915`). Re-verified after every
regeneration in this branch that the same two pages (`starting-material.md`,
`single-wafer-spin-processor.md`) are still the only ones with an undeclared `check_preserved.py`
difference, and that it is still the same pre-existing, unrelated artifact (confirmed again: every
changed file in this branch is a pure insertion, `git diff --numstat main -- docs/machines
docs/materials` shows 0 deletions in all 42 files).

#### For the pilot branch

The review's patch (tested by the reviewer in a scratch copy of `tools/check_preserved.py`), copied
verbatim so whoever owns that file does not have to re-derive it:

> **Patch for the pilot branch** (tested in a scratch copy of `tools/check_preserved.py`):
>
> ```python
> # An inch mark: a straight double quote right after a digit, immediately
> # followed (optionally after a closing bracket) by another straight quote,
> # as in 8"" or (8")". The digit must follow "(" or "<non-letter><space>",
> # so a nested quotation ending in a number ("Fab 4")" is left alone.
> INCH_RE = re.compile(r'(?:(?<=\(\d)|(?<=[^A-Za-z\s] \d))"(?=[)\]]?")')
>
>
> def extract_quotes(text: str) -> Counter:
>     out = []
>     text = INCH_RE.sub("″", text)   # ″, so QUOTE_RE never pairs it
>     for m in QUOTE_RE.finditer(text):
>         ...
> ```
>
> **Results of the patch:**
>
> - `check_preserved.py --allow-added refs,numbers,number_order --allow-dropdown-edits docs/machines/*.md
>   docs/materials/*.md` now reports "44 page(s) checked against main, **0** with undeclared
>   differences". Before the patch it reported 2.
> - `--selftest` still passes.
> - Across every `docs/**/*.md` outside `docs/plans`, the patch changes quote extraction on exactly
>   three pages: `public-sources.md`, `starting-material.md` and `single-wafer-spin-processor.md`. On
>   all three the real quotations are recovered, e.g. "SEZ223, Davinci, HF, DSP+HF, titration
>   controlled" and "Laser marking system, 8″".
> - A first, looser version (`(?<=\d)"(?=[)\]]?")`) also rewrote the nested `("Fab 4")"` in
>   `filings/index.md` and `public-sources.md:947`. The lookbehind above avoids that.
>
> **Selftest cases to add:**
>
> - `'"a, 8"" b "c"'` → {`a, 8″`, `c`};
> - `'"(8")" x "y"'` → {`(8″)`, `y`};
> - `'("Fab 4")"'` is unchanged by `INCH_RE`.

### Full check suite after the review fixes

`check_steps/refs/machines/materials/masks/papers/patents/filings/inforce.py`, `gen_papers/patents/
filings/index_links/step_tables.py --check`, `check_machines/materials/masks/gen_step_tables.py
--selftest`, and `sphinx-build -W -q -b html docs tmp/_build/html`: all 0 problems / exit 0. Rendered
`docs/machines/wet-bench.md` and `docs/materials/process-gases.md` at desktop and 400 px with
`tools/shoot.py` and read the tiles: the collapsed dropdown sits exactly where the run used to be, its
title wraps cleanly at 400 px, nothing looks wrong.

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
