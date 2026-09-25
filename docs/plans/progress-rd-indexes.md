# W3 first batch — machine/material/mask indexes — progress

Branch `topic/rd-indexes`. Task: W3 of `docs/plans/readability-plan.md`, first
batch (the three index pages `docs/machines/index.md`, `docs/materials/index.md`,
`docs/masks/index.md`), per `docs/plans/readability/report-B.md` B2, B3, B13, B16
and `docs/plans/readability-guide.md` R-INDEX, R-TABLE, R-CAPTION.

## Method

Restructuring these pages by hand risked transcription errors on very large
tables (30–90 rows, many with long quoted cells and footnote markers), so each
page's restructuring was done with a one-off Python script (kept under
`tmp/build/`, git-ignored, not a project generator) that:

1. Reads the current committed page.
2. Cuts it into named sections by exact heading/marker text (verified byte-for-
   byte reconstruction against the original before any transform is applied).
3. Rebuilds each new block (cards, split tables, moved sections) from the
   extracted cell text, copied verbatim — no cell content is retyped by hand.
4. Writes the new file, which is then checked exactly like a hand edit
   (checkers, `check_preserved.py`, `-W` build, `tools/shoot.py`).

This is presentation tooling for this branch only, not a repository generator;
nothing under `tools/` was touched.

## 1. Machines index (`docs/machines/index.md`) — done

**New order:** purpose (49 words, was one 113-word paragraph including
methodology text) → navigation (`## Equipment classes in a 200 mm, 130 nm fab`,
unchanged, then `## Machine-class pages` with the 8 unit-process groups as H3s,
each a `{grid} 1 2 2 2` of cards, plus 8 hidden captioned toctrees) → detail
tables (`## Machine classes and the steps that use them` shrunk to
`Machine class | Steps`, wrapped in `{table}` with a caption;
`## SkyWater's listed tools and the steps assigned to them` split into one row
per (tool, grade), further split into the same 8 groups under H3s to stay under
the 40-row cap, each also captioned) → how-to-read-this-index (`## Reading the
SkyWater evidence`, promoted from H3 to H2 since it no longer nests under
`## Machine-class pages`; `## What SkyWater has published about its tools`;
`## "Machines typically used" and "Machines likely used at SkyWater"` — all
three moved as complete, unchanged blocks) → open questions (moved before
references) → references (generated block + `## References`, untouched,
glued together as the checker requires).

**Card grid.** Card title/link = the class-link cell's `{ref}` target, with
its display text plus any trailing qualifier text kept as the visible title
(needed because several furnace pages share the display text "Vertical batch
furnace" and are told apart only by the qualifier: "oxidation", "LPCVD",
"anneal and alloy"); the whole card links via `:link:`/`:link-type: ref`
rather than a role inside the directive argument (matches the crib's R-CARDS
example, avoids an unverified syntax). Card body = the "What it does in
SKY130" cell, verbatim. Card footer (`+++`) = the "Tools SkyWater lists
publicly" cell, verbatim, footnotes intact.

**Groups.** The 8 groups are the ones already named under "Equipment classes
in a 200 mm, 130 nm fab", in that section's own order; classes within a group
are in main-table (flow) order. Two classes are not explicitly named by any of
the 8 bullets and needed a judgement call, both flagged here for the
coordinator:
* `starting-material` — the "Metrology…" bullet explicitly says "incoming
  wafer inspection belongs with the starting material (`category-substrate`)"
  without giving that class its own bullet; placed under "Metrology,
  inspection and test" (first by flow order, since it is step 1).
* `plasma-nitridation-chamber` — named in no bullet; placed under "Thermal
  processing" as the closest process fit (a single-wafer chamber treating a
  grown film, like the RTP entry in the same group). Purely a card-grouping
  choice; changes no fact.

**SkyWater-tools table split.** Each of the 32 original rows' third cell was
split at its own `*label:*` markers (regex on `\*([^*]+):\*`, verified against
every row — none has text before its first label). The original second column
("Source; strength of the listing", e.g. `strong[^skw-01]`) has no place in
the new 3-column shape (`Tool as listed | Grade in the step pages' words |
Steps`), so it was merged into the first column as
`<original col 1> — <original col 2>` (an em dash), repeated on every split
row for that tool; the lead-in sentence "The second column gives the source
and strength…" was reworded to "…is given in the first column, after the
tool's name" (structural pointer, not a fact). 90 split rows total; grouped
into the same 8 unit-process H3s (6/4/3/5/4/5/1/4 rows... i.e. per-tool-row
counts summing to 14/9/18/13/17/13/2/4 split rows respectively) to stay under
the 40-row cap (B2 table rule 7), each table captioned.

**Bug found and fixed while building this page:** a `{table}` caption written
across two source lines silently breaks the directive (MyST directive
arguments must be a single line) — the table rendered as nothing at all, with
no build warning and no checker complaint (this table has no checker reading
it). Caught only by looking at the rendered tiles, not by the checkers or the
build. **Guide problem to flag:** §6's crib should say directive arguments,
including a `{table}` caption, must be one line; nothing in the guide warns
against wrapping a long caption.

**Lead-in text adjusted for the new structure** (not a fact change, but noted
since it goes beyond a pure move): the two "In the table:" bullets that used
to describe the "What it does" and "Tools SkyWater lists" *columns* now say
these are the card's *body* and *footer* respectively (the columns no longer
exist in the shrunk table).

**Checker/preservation note.** `check_preserved.py --base main --allow-added
markers,numbers,quotes,identifiers,number_order docs/machines/index.md`
leaves one undeclared difference: `LOST number_order` on 5 tuples, and
`--allow-regrouped` does not downgrade it (condition (b), the flattened-digit
count check, fails by a handful of numbers). Root-caused, not just accepted:
`extract_number_order` treats each **raw table-row line** as one unit, so the
original 4-column row (all of "what it does", "tools" and "steps" on one
line) was one number-bearing unit; splitting that row into a 2-column table
row (class + steps) *and* separate card-body/footer prose (further split into
per-sentence units by the checker) means some numbers that used to be paired
with a neighbour in the same unit now sit alone in their own one-number
sentence, which `add_unit` does not record at all (it only keeps units with
2+ numbers) — so they vanish from the `number_order` comparison on **both**
sides without ever being reported as `LOST numbers` (the separate, stronger
check, which reported nothing here). Confirmed no digit is actually missing:
there is no `LOST numbers` line in the report at any point, only `LOST
number_order`, and every one of the 5 "lost" tuples' digits was hand-checked
against the new file and found present, just regrouped into more pieces than
the heuristic's regroup verifier expects. **Guide problem to flag:**
`check_preserved.py`'s `--allow-regrouped` path assumes a row-splits-into-
rows or sentence-splits-into-sentences regrouping; it has no accommodation
for a table row splitting into a table row *plus* prose (the R-INDEX case
here), so this kind of split will always need a hand-verified note like this
one rather than a clean `--allow-regrouped` pass.

**Checkers:** `check_machines.py`, `check_steps.py`, `check_refs.py`,
`check_materials.py`, `check_masks.py`, `check_inforce.py`,
`gen_index_links.py --check`, `gen_step_tables.py --check` — all 0 problems.
`-W` build clean. All 30 machine-class labels still linked (verified: same
30-element set before/after). Rendered `docs/machines/index.html` at desktop
and 400 px (`tools/shoot.py`, full-page captures at `--max-height 60000` for
phone to reach the tables): cards, both shrunk/split tables and their
captions all render correctly, no horizontal scroll, no oversized cells.
Toctree captions (`:caption:` on the 8 hidden toctrees) do **not** render as
visible sidebar dividers in furo — the "Machines" sidebar entry is one flat
list in the correct (grouped, flow-ordered) sequence, but the 8 group names
are not shown as separators. **Guide problem to flag:** the guide's own
uncertainty ("captioned toctrees if furo supports it cleanly") resolves to
"no" for a toctree nested under a class-index page (as opposed to the root
doc); kept anyway since the order is still correct and harmless, but the
visual grouping benefit the task asked for is not actually delivered by furo
here.

## 2. Materials index — in progress

(to be written up after the page-step)

## 3. Masks index — not started

## 4. Remaining captions and prose limits — not started

## Measurements (to fill in after all page-steps)

Before/after counts of paragraphs over 100 words and tables with captions,
per page, go here.
