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

## Remaining (this branch)

* Commit 4 — `tools/gen_step_tables.py` (B1): generate the marker-delimited
  step tables/dropdowns on all 42 machine/material pages, wire into
  `.readthedocs.yaml` and `docs/plans/agent-briefs.md`, render three
  pages with `tools/shoot.py` (desktop + 400 px) and fix anything that
  looks wrong.
* Commit 5 — `docs/plans/readability-guide.md` §9 and R-STEPRUN updates.
* `tools/check_preserved.py --allow-added refs,numbers` on every page
  gen_step_tables.py touches.

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
