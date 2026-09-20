# W0d — generator changes — progress

Branch `topic/rd-generators`. Task W0d of `docs/plans/readability-plan.md`:
generator changes from report-A (F13, F17), report-B (B2, B9, B11) and
report-C (C8, C9 rule 1, C11). Working through the five numbered steps
of the task brief as separate commits, running the full check suite and
looking at a rendered sample after each.

## Checker changes (summary; see each step below for detail)

Only one checker needed a semantic change across all five steps:

* **`tools/check_masks.py`** (step 3): `OPTIONAL_H3` gained
  `"Related pages": ["Related patents, papers and filings"]`. Reason:
  it forbids *any* H3 under an H2 not listed there, for every
  `docs/masks/*.md` page except `index.md`; `gen_index_links.py`'s new
  heading (report-A F13) lands under "Related pages" on the 36
  per-mask pages, which was not previously allowed to have H3s at all.

Every other checker was surveyed and found not to need a change:
`check_steps.py` has no H3 restriction at all; `check_machines.py` and
`check_materials.py` restrict H3s only under "At SkyWater"/"References"
(not "Related pages", where the same new heading lands on those page
types); there is no `check_categories.py`; and `check_machines.py` /
`check_materials.py`'s step-list comparisons (step 5) already accept a
`{ref}` step link with or without custom link text, so changing the
link text alone from a bare number to the step's code required no
checker change. `check_inforce.py` was re-run after every step that
touched a dropdown (3 and 4) and after step 5's link-text-only change;
0 problems throughout.

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

## Step 4 — `gen_patents.py` / `gen_papers.py` / `gen_filings.py` (done)

* **Clickable URLs (patents).** Added `esc_urls()` (wraps a bare
  `https?://…` in `<…>`, trailing sentence punctuation — comma, full
  stop, `;`, `:` — put back outside the brackets, everything else
  still backslash-escaped as `esc()` does) and used it for the family
  `Verified:` line, each member's `Verified` cell, and each `Notes:`
  bullet — the three places bare URLs came from (227 + 305 = 532,
  matching the brief's 533 with the one hand-fixed Cornell CFR URL in
  the legal-caveat text). Regenerating produced exactly 533
  insertions/533 deletions in `docs/references/patents/{index,families}.md`
  — matches the brief's count exactly. `gen_papers.py`/`gen_filings.py`
  were checked (`grep`) for the same pattern in their datasets: 0 bare
  URLs found in `notes`/free-text fields today, so no equivalent bug
  exists there yet — no rendering change was needed for those two
  beyond the reorder below.
* **Index reorder**, all three generators, to purpose → browse the
  views, with counts → how to read an entry → legal caveat (where one
  exists) → `:::{dropdown} Scope, method and counts` holding the
  present methodology text verbatim:
  * `gen_patents.py`: purpose paragraph unchanged; "Other views"
    (+toctree) then "Counts" moved up together right after it ("browse
    ... with counts"); "Unexpired and unknown-status families are
    collapsed" + "Relations" next (how to read an entry); "Legal
    caveat" next; the retrieval/fetched-note paragraph and "Scope and
    completeness" moved into the closing dropdown, their own standalone
    `##` headings dropped (the dropdown's own title now serves that
    role, matching the site's existing convention of no redundant
    heading inside a `{dropdown}` — see `family_entry()`).
  * `gen_papers.py`: same shape, no legal caveat section exists so that
    step is skipped. The pre-existing `(papers-scope)=` label had to
    move with its "Scope" content into the dropdown; ~40 bare
    `{ref}`papers-scope`` mentions elsewhere in this same file
    auto-resolve to the *target's* heading text, which would have
    silently changed from "Scope" to "Scope, method and counts"
    everywhere. Fixed by making that one call site explicit
    (`{ref}`Scope <papers-scope>``) before moving the label, so the
    rendered text is unchanged (verified in the rendered HTML — "Basis:
    process named (see Scope)." reads exactly as before). The other
    existing bare use, in `designed-on-sky130.md`, was already explicit
    text ("the index proper") and needed nothing.
  * `gen_filings.py`: purpose → Other views+toctree → "How to read an
    entry" → "Lineage timeline" (kept visible and un-collapsed: it is
    substantive lineage narrative, not methodology, so folding it away
    would have worked against the readability goal) → dropdown holding
    the EDGAR access note, the by-company/type/year counts and the
    "Known gaps" section (its own `## Known gaps` heading changed to a
    bold `**Known gaps.**` lead-in for the same no-redundant-heading
    reason as above; not checker-read, confirmed by grep) → "All
    filings" unaffected.
* No dataset field, number, quotation or citation changed — verified by
  reading full diffs of all three regenerated `index.md` files (and
  `patents/families.md` for the URL wrapping): only headings moved,
  wording is byte-identical apart from the two heading-to-bold-lead-in
  conversions and the one explicit-ref-text fix above.
* Ran all nine checkers, `gen_steps.py --check`, `gen_index_links.py
  --check`, and all four `gen_*.py --check` (0 problems throughout,
  including `check_inforce.py`, which inspects dropdowns). `-W` build
  clean. Rendered and read all three landing pages
  (`tmp/shots/rd4-{patents,papers,filings}-*.png`, not committed).

## Step 5 — B9 step-link text script (done)

Ran a one-off script (not committed; same treatment as the step-2
Phase-cell edit): built a step-number -> code map from every
`docs/steps/NNN-*.md` page's own `# Step NNN — CODE: Name` title, then
replaced every `{ref}`NNN <step-NNN>`` (bare-number link text) with
`{ref}`CODE <step-NNN>`` in the 11 files `grep -rlE
'\{ref\}\`[0-9]{3} <step-' docs/` found — machines/index.md,
materials/index.md, and nine machine class pages (mostly the
"SKY130 steps assigned to this class" paragraphs). Exactly 1,975
replacements, matching the brief's count. None of the 11 files has a
table with a separate plain step-number column next to these links —
all occurrences are either prose paragraphs or a single "Steps" table
cell — so the "keep both" case did not arise; confirmed by inspecting
every match's context before running.

`check_machines.py`/`check_materials.py` (the checkers whose "Steps"
comparisons touch these exact lines) both already accept `{ref}` with
or without custom link text (`STEP_RE` matches either form and reads
only the `step-NNN` label), so no checker change was needed — all
nine checkers, `gen_steps.py --check`, `gen_index_links.py --check`
and the three `gen_*.py --check` (patents/papers/filings) pass with 0
problems after the edit. `-W` build clean.

## Remaining

None. All five steps of the W0d task are done.
