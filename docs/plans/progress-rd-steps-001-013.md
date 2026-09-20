# Progress — W2 pilot, step pages 001–013

Branch `topic/rd-steps-001-013`, worktree `.worktrees/rd-steps-001-013`. Applying
`docs/plans/readability-guide.md` to `docs/steps/001-smat.md` … `013-ns19.md` (the W2 pilot
named in `docs/plans/readability-plan.md`). One commit per page. This file is updated as I go.

Setup done: `tmp/readability/a-tools/measure*.py` copied per §3; `tmp/preserve/`, `tmp/shots/`
created. Baseline `-W` build done once at the start (clean, 0 warnings); pages are then rebuilt
incrementally per edit (a few seconds each).

Boundaries observed throughout: `## References` reading lists/footnote definitions, the
generated `<!-- index-links:begin … end -->` block, `{figure}` blocks, the quick-facts table,
the 13 mandatory H2 headings, and `{dropdown}` titles/boundaries are never touched. Figures are
also left in their existing position inside `## What this step is` (see "Guide problems" —
the §4.1 skeleton implies the figure sits above the H2, but every already-merged step page has
it inline; moving it is out of scope for a presentation-only batch and risks being read as
"touching" a generated block).

## Method note: check_preserved.py and restructuring rules

`tools/check_preserved.py`'s `number_order` category treats a table row, list item or heuristic
sentence as a "unit" and tracks the left-to-right order of numbers *within* that unit. R-TABLE,
R-DERIVATION and R-LIST all work by taking one prose unit that holds several numbers and
splitting it into several smaller units (table rows, numbered steps, bullets). This
deterministically produces LOST tuples (the one big unit no longer exists) paired with ADDED
tuples (the same numbers, regrouped into smaller units) — and the tool always fails on any LOST
entry, in any category, with no flag to declare it away (checked in `tools/check_preserved.py`,
`diff_page`: `if lost: results.append((True, ...))` unconditionally, unlike `added` which
respects `--allow-added`). So a page that gets any R-TABLE/R-DERIVATION/R-LIST treatment at all
can never show a clean `check_preserved.py` exit 0 — see "Guide problems" below. Per page I
verify by hand (a small script dumping each old/new numeric unit and its source text) that every
LOST/ADDED number_order pair is the same digits regrouped, not a real transposition or loss, and
record the categories used with `--allow-added` and why. `numbers`, `markers` and `hedges`
additions are the expected result of the "At a glance" box and R-TOOLS/R-DERIVATION templates
repeating an existing figure/marker/hedge (agent-briefs.md, "Checking a readability edit";
task boundaries, "declare additions only when the guide tells you to add text").

## Guide problems

1. **R-H3 skeleton vs. figure placement (§4.1).** The step-page skeleton in §4.1 shows the
   generated figure sitting between the "At a glance" box and `## What this step is`. Every
   step page already merged from W1b instead has the `{figure}` block *inside* `## What this
   step is`, after the lead paragraph. The task boundary for this batch says not to touch
   `{figure}` blocks; moving one (even verbatim) to match the skeleton is a layout change to
   generated content that `tools/gen_figures.py --check` does not itself forbid (it only checks
   the block text, not its position — verified by reading `page_block_problems`/`page_blocks`
   in `tools/gen_figures.py`), but is outside what this batch was asked to do. Conservative
   reading applied: left every figure exactly where it already sits; restructured the prose
   around it instead (new H3s follow the figure, keeping the intro before it short).
2. **`check_preserved.py`'s `number_order` LOST is unconditional (§5, §7 step 4).** See the
   method note above. §7's checklist item ("The preservation check prints `identical`, or the
   only gains are new step numbers, step names and `—`") describes the pre-W0b hand snippet, not
   the shipped tool's `number_order` category, which cannot reach a clean run on any page that
   gets R-TABLE/R-DERIVATION/R-LIST treatment of a multi-number passage. Conservative approach:
   manually diff every LOST/ADDED `number_order` tuple against the source text before accepting
   a page (see per-page notes); never used to justify an actual missing number.
3. **R-CATEGORY step 2's "2–4 bullets" when only one sentence remains.** Several step-category
   paragraphs have exactly one sentence of "specific to this step" material after the
   classification sentence is separated out, so "2–4 bullets" is not reachable without inventing
   text. Conservative reading: one bullet is used where only one sentence remains (rule text
   gives no minimum-count instruction beyond "holding the remaining sentences", and inventing
   an extra bullet would fabricate structure that is not in the source).
4. **R-TOOLS applied to a non-tool bullet.** `## Machines likely used at SkyWater` on 001-smat.md
   includes a "Wafers themselves — GlobalWafers and SEH America" bullet (the wafer material, not
   a machine) carrying a bare "Strength: strong." R-TOOLS's trigger is purely mechanical ("a
   bullet … contains 'Strength:'"), so it was split into the same *SkyWater says:*/*Tool
   exists:* sub-bullet form as the others, and included in the required four-tool recap table,
   even though "Tool" is a slight misnomer for a wafer supplier. Recorded rather than silently
   left out, since the rule gives no exception for this case.
5. **R-RELATED's six labels don't cover a "same category, several modules away" bullet.**
   Several step pages list sibling steps of the same process category that are scattered across
   different flow modules (e.g. 002-box.md's "other thermal oxidations in the flow"). None of
   Previous/Next/Same module/Depends on/Feeds/Category is a clean fit. Conservative choice:
   "Same module" as the least-wrong label, since it is the closest in spirit (a same-kind
   sibling list) even where the steps are not literally in one module.
6. **`check_preserved.py`'s `NUMBER_RE` has no word-boundary guard.** Unlike
   `measure.py`/`measure2.py`'s number regex, `check_preserved.py`'s matches any digit run
   anywhere, including inside identifiers such as "SKY130" (→ "130"), "EV300" (→ "300"), "1X"
   (→ "1"), "SC-1"/"SC-2" (→ "1"/"2"). Any new sentence that so much as says "SKY130" registers
   as an "ADDED numbers" difference. This is harmless (verified by hand each time) but means the
   `numbers` category is essentially always touched by an "At a glance" box or any new sentence
   mentioning the technology name, and `--allow-added numbers` ends up declared on nearly every
   page in this batch, not just ones with a genuine new figure.

## Per-page log

### 001-smat.md — done, commit pending

Rules applied, in order: R-H3 (added `### What the public record shows` around the existing
evidence bullets, keeping the figure in place; added `### How the effective body doping is
estimated` — see R-DERIVATION below), R-SENTENCE (split the Suppliers bullet's semicolon
sentence; split the first sentence of "What this step is" at its semicolon for R-GLANCE's ≤25
word cap), R-PARA (Suppliers list item >100 words → lead sentence + two sub-bullets), R-LIST
(the RCA sequence "SC-1, dip, SC-2" sentence in the numbered recipe → three sub-bullets; "Two
indirect figures exist" in Open Questions → two sub-bullets), R-DERIVATION (the effective
body-doping estimate, previously one ~150-word sentence buried in Open Questions, moved to its
own H3 with an input table and a two-step numbered derivation; Open Questions keeps the
question, the hedge and a plain-text pointer, no restated numbers), R-CATEGORY (classification
sentence + "Specific to this step:" bullet, one bullet — see Guide problem 3), R-TOOLS (all four
"Machines likely used at SkyWater" bullets had "Strength:"; added the Tool|Evidence recap table
and split each into SkyWater says/Tool exists/Runs this step — see Guide problem 4 for the
wafers bullet), R-RELATED ("Feeds:" label added to the two forward-pointing bullets; "Next:" and
"Category page:" already present and left as they were), R-GLANCE (added the "At a glance" box
last; split the opening sentence at its semicolon so the first sentence of "What this step is"
is 13 words). R-CODE: no candidate (matches the guide's own finding). R-HEDGE step 1: does not
apply (the "How it is typically performed" opener does not match `industry-generic|industry-
typical` on this page). R-REPEAT: no ≥10-word repeated run found by `measure3.py` for this page.

Paragraphs/items over cap before → after: the Suppliers list item (112 words) → lead sentence
(≈26 words) + two sub-bullets; the Open-Questions "Resistivity and orientation" item (207 words,
containing a 2-op derivation) → lead (≈28 words) + two short sub-bullets + a new H3 elsewhere
carrying the derivation. No paragraph on this page was ever ≥120 words (page had none in the
"before" batch measurement).

`check_preserved.py docs/steps/001-smat.md --allow-added markers,numbers,hedges,number_order`:
0 LOST outside `number_order`; all `number_order` LOST/ADDED pairs hand-verified against the
diff (dumped units script) as the same digits regrouped by the R-LIST/R-DERIVATION splits, not a
real change. All other checkers (`check_steps`, `check_refs`, `check_machines`,
`check_materials`, `check_masks`, `check_inforce`, `check_papers`, `check_patents`,
`check_filings`, `gen_index_links.py --check`, `gen_papers.py --check`, `gen_figures.py
--check`) pass. `-W` build clean. Screenshots (desktop + 400 px) read top to bottom: the new
derivation table, category bullet, and Machines-likely-used-at-SkyWater recap table all render
without overflow at 400 px; no other issue seen.

### 002-box.md — done

Rules applied: R-SENTENCE (first sentence of "What this step is" split at its colon for the
≤25-word cap), R-CATEGORY (classification sentence + one "Specific to this step:" bullet — Guide
problem 3 again, only one sentence remained), R-HEDGE step 1 (the "industry-generic recipe for a
200 mm fab of the 130 nm era:" opener wrapped in `:::{note}` word for word), R-TOOLS (two
"Strength:" bullets, both < 4 tools so no recap table per the rule's own threshold — split into
SkyWater says/Tool exists/Runs this step sub-bullets), R-RELATED ("Feeds:" added to the
pad-oxide-fate bullet; "Same module:" added to the "other thermal oxidations in the flow" bullet
— see Guide problem 5, a new one: the bullet spans several modules, not one, and none of the six
labels fits cleanly; "Same module" was the least-wrong choice), R-OPENQ (bold labels added to all
three previously unlabelled bullets), R-GLANCE (box added last; "Public numbers" is "none
published" per the rule's own fallback, since the only published range for SKY130 lives inside
the in-force-patent dropdown and R-GLANCE point 4 forbids drawing from it — the AmberWave-patent
range in open prose has no number-of-its-own attached at the point it would need one, so it was
left out rather than restated loosely). R-H3: evaluated, not applied — "What this step is" is
already exactly 2 paragraphs and only slightly over 120 words (~130), and the content is
narrative rather than an evidence list or derivation that the H3 vocabulary fits; left alone per
"if a rule does not clearly apply, leave the text alone." R-TABLE/R-DERIVATION/R-LIST: no
candidate (measure3/measure4 found none on this page). R-CODE: no candidate.

No paragraph or list item on this page was over its cap before editing (per-page
`measure_batch.py` run: 0 paragraphs ≥120, 1 item ≥80 words — the "Furnace" Machines-likely-used
bullet, resolved by the R-TOOLS split above).

`check_preserved.py docs/steps/002-box.md --allow-added markers,numbers,hedges`: exit 0, no
`number_order` involvement at all (no multi-number unit was split this page). The `numbers`
addition is two more instances of literal "130" — traced to `check_preserved.py`'s `NUMBER_RE`,
which (unlike `measure.py`'s) has no word-boundary guard, so it matches "130" inside "SKY130"
every time that word appears in new prose (also explains the "'130'"/"'300'"/"'1'" additions on
page 001, which come from "SKY130", "EV300" and "1X" the same way) — recorded as Guide problem 2b
below. All other checkers and the `-W` build pass; screenshots at both widths read cleanly, note
admonition and both tool sub-bullet blocks render without overflow.

### 003-isonit.md — done

Rules applied: R-H3 (`### What the public record shows` before the 173-word thickness/evidence
paragraph), R-SENTENCE (split the 76-word "thickness is a compromise" sentence at its em-dash),
R-CATEGORY (classification sentence + one-bullet "Specific to this step:" — Guide problem 3
again), R-HEDGE step 1 (industry-generic recipe opener → note), R-TOOLS (the one "Strength:"
bullet split into SkyWater says/Tool exists; the trailing "Vertical configuration: … (weak)"
sentence, which grades a different attribute than existence/assignment, kept as plain text after
the sub-bullets rather than forced into "Runs this step"), R-RELATED ("Feeds:" and "Same module:"
labels, per Guide problem 5's convention), R-OPENQ (three bullets labelled), R-GLANCE (box added
last; first sentence of "What this step is" already exactly 25 words, no split needed).
R-TABLE/R-DERIVATION: no candidate. R-CODE: no candidate. R-LIST: the CMP-stop bullet (60 words)
is at, not over, the item cap — left alone.

`check_preserved.py docs/steps/003-isonit.md --allow-added markers,numbers,hedges,number_order`:
exit 0, 0 LOST in any category (the one `number_order` addition, `('130','150')`, comes from the
new glance-box sentence naming "SKY130" and "150 nm" together, not a real transposition — no
LOST counterpart at all this time, unlike page 001). All other checkers and the `-W` build pass;
screenshots at both widths read cleanly.

## Batch measurements (all 13 pages, before editing)

`tmp/readability/a-tools/measure_batch.py` (written for this batch; reuses `measure.py`'s
`clean`/`words`/`blocks` and `measure2.py`'s sentence-splitting so the thresholds match the
guide's own scripts) against `docs/steps/00[1-9]-*.md docs/steps/01[0-3]-*.md`:

* paragraphs ≥120 words: 11 / 147 total prose paragraphs
* list items ≥80 words (outside References): 17 / 387 total non-ref items
* sentences ≥60 words: 21 / 768 total sentences
* tables (markdown `|` blocks): 13
* H3 headings: 52

"After" numbers are collected once all 13 pages are done (see bottom of this file).
