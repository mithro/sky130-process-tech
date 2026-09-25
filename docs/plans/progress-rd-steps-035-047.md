# Progress — W2 batch 3, step pages 035–047 (SONOS tunnel window and ONO stack; gate oxides)

Branch `topic/rd-steps-035-047`, worktree `.worktrees/rd-steps-035-047`, branched from
`main` at `4a4ed3cf` (batch 2, 014–034, already merged; carries the scripted
marker-coverage reviewer check). Applying `docs/plans/readability-guide.md` to
`docs/steps/035-tunm.md` … `047-lvgox.md`, following the corrected guide and
`docs/steps/018-nwi.md`/`022-hvtpm.md`/`030-pwdem.md` (batch 2) as the model of the
finished form. One commit per page. This file is updated as I go.

Setup done: `tmp/readability/a-tools/measure*.py` copied per §3; `tmp/preserve/`,
`tmp/shots/` created. Baseline `-W` build done once at the start (clean, 0 warnings).
`check_preserved.py` is run throughout with `--base 4a4ed3cf` (this branch's own start
point == merge-base with `main`).

Boundaries observed throughout (per task and guide §2): `## References` reading lists and
footnote definitions, the generated `<!-- index-links:begin … end -->` block, `{figure}`
blocks (left exactly where `gen_figures.py` already placed them, inside `## What this step
is`, after the lead), the quick-facts table, the 13 mandatory H2 headings, and `{dropdown}`
titles/boundaries/contents are never touched. This module is patent-sensitive
(037–044 got an in-force sweep in the previous batch); `check_inforce.py` is run after
every page, never just at the end, and no note content, number or title is ever moved
across a `{dropdown}` boundary or into a glance box, table or caption.

## Baseline measurement (§1 caps, `measure5.py`, before editing)

13 pages (`docs/steps/035-tunm.md` … `047-lvgox.md`):

* paragraphs > 100 words: 59
* list items > 60 words (outside References): 37
* sentences > 45 words: 117
* table cells > 25 words: 0

(Full worklist: `tmp/measure5-before.txt`, not committed — `tmp/` is git-ignored.)

## Content problems for the owner

(none found yet on 035; see per-page log for 042/043's pad-oxide-clearance contradiction
once reached.)

## Guide problems

(carried references to the pilot's and batch 2's numbered lists apply here too; new ones
for this batch are added below, continuing the numbering — batch 2 ended at 14, so new
items here start at 15, only if genuinely new.)

## Per-page log

### 035-tunm.md — done (2 in-force patents in the generated dropdown; no hand-written
in-force note in the body)

Rules applied: R-H3 (`### What the public record shows` before the drawn-layer/rules
discussion), R-TABLE (the `tunm.1`–`tunm.8` design-rule paragraph → Rule|Constrains|Value,
wrapped in `{table}` with `:widths:` since the Constrains column holds prose; the
`[^pdk-periph]` marker that sat mid-enumeration in the source is kept at 3 occurrences,
matching the original count exactly — one moved to the table's lead-in sentence (covering
rows 1–7, per the rule's own preferred practice), one kept on the tunm.8 row (its original
position), one kept on the hvi.4 sentence kept as prose outside the table (its original
position); `[^pdk-06]` likewise kept at its original 2 occurrences), R-LIST (the "Together
these say that…" sentence, a 3-item list written as one sentence, → 3 bullets with the
marker moved to the lead-in colon; the test-tile "characterised with" sentence → 3 bullets
the same way), R-PARA/R-SENTENCE (the lead split into 2 paragraphs at its
"opens-windows"/"windows-are-used" seam, and the "windows are used three times" sentence
further split there too; the "Why this step exists" section split into 3 bold-labelled
paragraphs — **SONOS at SkyWater.**, **The memory transistor.**, **Mask count.** — plus a
2-paragraph split of the threshold/implant paragraph at its e-test-numbers seam, moving the
em-dash aside into its own sentence; the Resist-coat item's 13-word parenthetical hedge
closed as its own sentence per the ≥12-word rule; the Exposure item's two parentheticals
merged into one before the em-dash/semicolon split, to stay at the 0–1-per-sentence cap),
R-CATEGORY (35-word classification sentence + `**Specific to this step:**` and 2 bullets,
one per remaining sentence), R-HEDGE step 1 (italic lead-in on the "How it is typically
performed" scope sentence — **this required re-adding the `## How it is typically
performed` heading line, which the first edit pass accidentally deleted along with the
sentence it replaced; caught immediately by `check_steps.py` reporting a missing heading**),
R-TOOLS (4 "Strength:" bullets → SkyWater-says/Tool-exists/Runs-this-step form + a
`Tool | Evidence` recap table, since 4 meets the rule 5 threshold; the "Tracks" and
"Metrology" bullets, whose bold head already carries the SkyWater statement and marker,
follow the batch 2 convention of omitting a redundant `*SkyWater says:*` sub-bullet),
R-RELATED (relabelled and reordered per the rule's own label order: `Previous:`, `Next:`,
`Depends on:` (deep-N-well requirement), `Feeds:` (the downstream ONO stack), `Same
category:` (the other SONOS masks), `Mask:` (renamed from "Mask page:"), `Category page:`),
R-OPENQ (bold labels added to all five bullets), R-GLANCE (box inserted last, after the
quick-facts table; "Public numbers" uses the three `tunm` design-rule values with their
marker; "Likely SkyWater tool" mirrors the first R-TOOLS item's grades).

**One mistake caught immediately by the checkers, not a reviewer**: the first edit pass to
"How it is typically performed" replaced the H2 heading line together with the old opening
sentence, instead of inserting the italic lead-in *after* the heading — `check_steps.py`
reported "missing ## How it is typically performed" straight away; fixed by re-adding the
heading before the italic line, in the same commit, before any checker was declared
passing.

Caps before → after (`measure5.py`): paragraphs > 100 words 3 → 0 (all real prose cleared;
the only remaining >100-word paragraph in the earlier count was the page's own `{figure}`
caption, which was already the case before this edit and is off limits — Guide problem 10
from batch 2, restated here since it recurs on this batch too); list items > 60 words 0 → 0;
sentences > 45 words 6 → 2 (both the figure's own alt text/caption, off limits, same
Guide-problem-10 pattern); table cells > 25 words 0 → 0.

`uv run python tools/check_preserved.py --base 4a4ed3cf --allow-added
markers,numbers,hedges,identifiers,number_order --allow-regrouped docs/steps/035-tunm.md`:
declared additions are exactly what R-GLANCE and R-TOOLS's recap table are specified to add
(the `tunm` design-rule values and the `skw-01`/`pdk-periph` markers repeated in the glance
box; the four tool names' identifiers and numbers repeated a second time in the new recap
table; "inference"×3 and "not public" from the glance box's own template wording, which
repeats grading words already on the page). Two `LOST number_order` findings remain, neither
a real loss (hand-verified against the diff, both digits/values checked present elsewhere on
the page):
* `('0.410','1','0.500','2','0.095','3','4','0.095','4','5','6','0.672','²','7','8')` — the
  whole design-rule enumeration. The automatic contiguous-run check fails only because the
  table puts each rule's identifier *before* its value (`tunm.1 | … | 0.410 µm`), the reverse
  of the source's `0.410 µm … (tunm.1)` order — the same order-reversal the guide's own
  R-TABLE worked example (`018-nwi.md`) uses. Every one of the 15 digits/values is present on
  the page, unchanged, spot-checked against the table row by row.
* `('4','5')` — the `tunm.4`/`tunm.5` rule-id pair, stranded because each is now the sole
  digit of its own table row (a single-number unit produces no `number_order` tuple at all
  for the regroup check to match against), the same "Guide problem 11" pattern documented in
  batch 2 (`docs/plans/progress-rd-steps-014-034.md`). Both digits are present, unchanged, in
  the `Rule` column.

`quotes` and `hedges` (undeclared) show no LOST; plain `numbers` (condition (a)) shows no
LOST. All other checkers (`check_steps.py`, `check_refs.py`, `check_machines.py`,
`check_materials.py`, `check_masks.py`, `check_inforce.py`, `check_papers.py`,
`check_patents.py`, `check_filings.py`, `gen_papers.py --check`, `gen_patents.py --check`,
`gen_filings.py --check`, `gen_index_links.py --check`) pass; `-W` build clean. Screenshots
(desktop + 400 px) read cleanly top to bottom: the glance box, the new `### What the public
record shows` H3 with its design-rule table (holds at 400 px, 3 columns, no horizontal
scroll), the Step-category bullets, the three bold-labelled "Why this step exists"
paragraphs, the R-TOOLS recap table and sub-bullets, and the Related/Open-questions sections
all render without overflow. The generated in-force dropdown (2 families) is untouched and
collapsed as before.
