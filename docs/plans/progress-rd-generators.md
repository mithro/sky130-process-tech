# W0d — generator changes — progress

Branch `topic/rd-generators`. Task W0d of `docs/plans/readability-plan.md`:
generator changes from report-A (F13, F17), report-B (B2, B9, B11) and
report-C (C8, C9 rule 1, C11). Working through the five numbered steps
of the task brief as separate commits, running the full check suite and
looking at a rendered sample after each.

## Step 1 — `gen_steps.py` sync + `--check` (done)

`write_index()` was stale: it dropped the committed intro paragraph
(the "lightly edited for 20 steps" sentence) and the `[^steps-sheet]`
footnote definition, so a real run would have deleted the citation.
Verified by diffing a scratch run against the committed file before
touching anything.

* Added `INDEX_INTRO` / `INDEX_FOOTNOTES` constants holding that text
  verbatim and an `index_text()` function so the committed file and the
  generator agree byte for byte (`uv run tools/gen_steps.py --check`
  now passes with 0 problems).
* Added `--check`: fails if `docs/steps/index.md` differs from the
  generated text, or if a step page listed in `steps.csv` is missing.
  It never writes.
* Confirmed the safety property the brief asked to keep: `write_stub()`
  still returns `False`/no-ops for any step page that already exists
  (all 171 are written; a plain run reports "0 stub(s) created" and
  leaves `docs/steps/index.md` byte-identical — verified with
  `git status` before/after).
* Added `python tools/gen_steps.py --check` to `.readthedocs.yaml`
  `pre_build` (after the other `check_*` entries, before `gen_papers.py
  --check`) and to the checker lists in `docs/plans/agent-briefs.md`
  (writer brief and reviewer brief).

No checker needed a semantic change for this step — it only reads the
generator's own output.

## Step 2 — step index grouped by module, reverse lookup, short titles (done)

* **Module reconciliation (asked for explicitly).** `gen_steps.py` already
  had a 10-entry `PHASES` list, used only for the quick-facts "Phase" cell
  that is already hand-written on all 171 pages (10-way FEOL/MOL/BEOL
  wording, e.g. "FEOL — isolation"); no checker reads it. The overview's
  module table (`docs/overview/index.md`, "The flow by module") has a
  *different*, 13-way grouping with its own names and step ranges. Rather
  than invent a third vocabulary, the step index now groups by the
  overview's 13 modules (new `MODULES` list, names and ranges copied from
  the overview table) and `PHASES`/the Phase cell are untouched — they
  serve a different purpose (page-level quick fact vs. index navigation)
  and are presentation content already committed on every page.
* **Short category labels** (`CATEGORY_SHORT`): the F17 examples ("Litho",
  "Implant", "Strip/clean", "CMP") plus the same shortening pattern for
  the other six categories. Link targets unchanged.
* **Reverse lookup (B2).** `machine_class_map()` inverts the *main*
  (unmarked) assignment of the machines index's "Machine classes and the
  steps that use them" table — text before the first role marker
  (`*alternative:*`, `*also …:*`, `*overlay:*`, `*CD-SEM:*`) counts as
  "main"; the rest does not. `mask_map()` inverts the masks index's "Mask
  steps in this reference" table: the mask step itself plus every step in
  its *Patterns* cell (including the strip step, when the cell names one)
  map to that mask. Both parse the two index files' own Markdown tables
  by locating the exact header row (`SystemExit` if not found, so a
  future rewording of either table is caught rather than silently
  mis-parsed) — no new facts, only what the two tables already say.
  Result: 0 of 171 steps lack a machine class; 71 of 171 lack a mask
  (correct — most steps are not photolithography or its resist-pattern
  followers), shown as "—".
* **Layout.** Rendered the 6-column combination (Step/Code/Name/Category/
  Machine class/Mask) mentally against the existing precedent (report-B
  already found 6-column tables unusable at 400 px on the masks index)
  and went straight to the fallback the brief allowed: each module gets
  two 4-column tables — `Step | Code | Name | Category` then
  `Step | Code | Machine class | Mask` — confirmed by
  `tools/shoot.py --width 400` on the built page: both tables render
  fully, no clipping, no horizontal scroll (`tmp/shots/rd-generators-phone-*.png`,
  not committed — `tmp/` is git-ignored).
* **Toctree.** Verified in a scratch Sphinx project first that MyST's
  `Title <target>` toctree syntax changes only the sidebar entry — the
  target page's own `<h1>` and "next/previous chapter" labels are
  unaffected. Applied `NNN CODE — Name <file>` to all 171 entries.
* **`{term}` on the Phase cell (C9 rule 1).** Confirmed `FEOL`, `MOL` and
  `BEOL` are all defined in `docs/glossary.md`, and confirmed no checker
  reads the Phase row (`grep -rn Phase tools/*.py` — only `gen_steps.py`
  itself). Added `phase_with_term()` and used it in the `STUB` template
  (for any future stub page) plus a one-off script (not committed as a
  tool) that rewrote the `| **Phase** | ... |` line on all 171 written
  step pages to wrap the leading FEOL/MOL/BEOL as `{term}`; nothing else
  on the line changed (diff-checked on a sample page).

No checker change was needed for this step either.

## Step 3 — `gen_index_links.py` heading and link text (done)

* **Heading.** New `heading_for(path)`: `### Patents, papers and filings
  about this step` on step pages, `### Related patents, papers and
  filings` elsewhere; `render_block()` now takes the heading and puts
  it first, only when there is content (an empty block still renders as
  nothing, checked in `--selftest`). The block always sits right before
  `## References`, so the new H3 lands under whatever H2 precedes it —
  on step pages that is the mandatory "Related steps and
  cross-references", matching F13 exactly.
* **Checker survey (as asked) before touching anything:**
  * `check_machines.py`, `check_materials.py` only restrict H3s under
    "At SkyWater"/"References"; "Related pages" (where the block lands
    on machine/material pages) is unchecked — no change needed.
  * `check_masks.py` forbids *any* H3 under an H2 not in
    `H3`/`OPTIONAL_H3`, for every mask page except `index.md`. The
    block lands under "Related pages" there, which was not listed —
    extended `OPTIONAL_H3` with `"Related pages": ["Related patents,
    papers and filings"]` (minimal: one new key, one new heading
    string) and updated the docstring. `masks/index.md` is excluded
    from that rule already, so the index page itself needed nothing.
  * No `check_categories.py` exists, and `check_steps.py` has no H3
    restriction at all: no change needed for either.
* **Link text (F13).** `expired_line()`: title first, number after
  (`{ref}`Title <patent-…>` — US 5,830,375 A (1996)`). One of 552
  titles contains a literal `<100>` (crystal-plane notation), which
  cannot sit inside a `{ref}` role's own `<target>` delimiter even
  backslash-escaped (verified empirically in a scratch Sphinx build:
  MyST's target regex runs before escape processing and matches the
  first `<...>`, not the last) — that single family falls back to the
  previous number-first format; a `--selftest` case pins both branches.
  Papers already render title-first (`gen_papers.line()` uses a bare
  `{ref}` to the paper's own label, which auto-resolves to its "###
  Title" heading) — no change needed there. Filings already embed the
  title in prose before the "(full entry)" link — left as is.
* **Split count-only sentence.** The `> THRESHOLD` branches of
  `render_patents`/`render_papers`/`render_filings` now return a count
  clause, a blank line, then a separate "See {ref}`...`" sentence (two
  paragraphs instead of one run-on sentence).
* **In-force safety.** Did not touch `family_link_line()` (the format
  used *inside* the collapsed dropdown for in-force/unknown families) —
  out of scope for F13, which only asked for the *expired*-family
  format. Re-ran `check_inforce.py` after regenerating: 0 problems, so
  restricted titles/numbers still never appear outside a dropdown.
* Regenerated all 206 pages in one `gen_index_links.py` run (no
  content pages hand-edited). All nine checkers, `gen_steps.py
  --check`, and `gen_index_links.py --check` (0 pages differ) pass.
  `-W` build clean; spot-checked `docs/steps/001-smat.md`,
  `docs/machines/wet-bench.md`, `docs/masks/fom.md` and a
  `> THRESHOLD` page (`docs/categories/cmp.md`) by reading the
  generated Markdown and the rendered HTML.

## Remaining

4. `gen_patents.py` / `gen_papers.py` / `gen_filings.py`: clickable
   URLs, index reorder, `{dropdown}` for methodology.
5. B9 step-link text script (11 files, 1,975 links).
