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

### 004-fom.md — done

Rules applied: R-SENTENCE (the mask-layer paragraph's semicolon/em-dash chains split into three
sentences), R-TABLE (the `cfom`/`fom` drawn-side layer:purpose list, 5 rows, → a Layer|Purpose
table), R-H3 ("### Which wavelength?" — a 190-word bold run-in that argues evidence → calculation
→ inference, a whole passage, not one point; "**Mask polarity.**" stayed bold, a single ~35-word
point), further R-SENTENCE inside that section (the two semicolon/long sentences of the k1
argument split), R-PARA (the 84-word "Anti-reflective coating" numbered-list item → lead sentence
+ indented continuation, itself split at its semicolon), R-CATEGORY + R-LIST together (the
"unusual in three ways" enumeration was already a clean 3-item list under one classification
sentence — no Guide-problem-3 single-bullet case this time), R-TOOLS (three "Strength:" bullets,
under 4 so no recap table; the two bullets whose only "SkyWater says" content was already the
bold head text skip an empty *SkyWater says:* sub-bullet and go straight to *Tool exists:*/*Runs
this step:*), R-OPENQ (three bullets labelled), R-GLANCE (box added last; first sentence already
9 words). R-DERIVATION: no candidate (no arithmetic, just a k1 comparison already given as
prose). R-CODE: no candidate.

One slip caught by `check_preserved.py` and fixed before committing: the first glance-box draft
quoted `"waffle"` as if it were the page's own quotation; the page only ever quotes "waffle drop"
and "waffles", never bare "waffle" — reworded to "dummy waffle pattern" (no quotation marks) since
inventing a new quoted string is exactly what `check_preserved.py`'s `quotes` category is there to
catch (§2 rule 1).

`check_preserved.py docs/steps/004-fom.md --allow-added markers,numbers,hedges,number_order`:
0 LOST outside `number_order`; six `number_order` LOST/ADDED pairs, all hand-verified (dumped
units script) as the table split, the two semicolon/em-dash sentence splits, and the numbered
anti-reflective-coating item split — one of the ADDED tuples' leading digit is the "2." of that
numbered list item itself (`_LIST_ITEM_RE`/`NUMBER_RE` count a list marker as a number), not page
content. All other checkers and the `-W` build pass; screenshots at both widths read cleanly, the
new layer table holds at 400 px.

### 005-stinite.md — done

Rules applied: R-SENTENCE (first sentence of "What this step is" split at its colon for the
≤25-word cap; the 81-word "Nitride main etch" item's semicolon chain converted to sentences
rather than forced into R-LIST bullets — no natural "announcing" clause existed to introduce a
list without inventing one), R-PARA (that same item: lead sentence + indented continuation),
R-CATEGORY (classification sentence + one-bullet "Specific to this step:" — Guide problem 3
again), R-TOOLS (three "Strength:" bullets, under 4, split into sub-bullets), R-RELATED
("Depends on:" for the films-etched bullet, "Same module:" for the other-nitride-etches bullet),
R-OPENQ (three bullets labelled), R-GLANCE (box last). R-H3: no candidate (no bold run-in, no
section over cap). R-TABLE/R-DERIVATION: no candidate. R-CODE: no candidate.

`check_preserved.py docs/steps/005-stinite.md --allow-added markers,numbers,hedges,number_order`:
0 LOST outside `number_order`; the two `number_order` pairs are the R-TOOLS bullet-head/sub-bullet
boundary shift (same pattern as page 002), hand-verified against the diff. All other checkers and
the `-W` build pass; screenshots at both widths read cleanly.

### 006-stie.md — done

This is the page the guide itself uses for its R-H3 and R-DERIVATION worked examples ("How
deep?" → "### How deep?"; the trench-depth arithmetic) and for R-GLANCE's own example box. The
page still had the pre-readability text, so this commit applies the guide's own examples,
extended to preserve every sentence the actual page carries that the guide's abbreviated
illustration omits (the PSG alternate-datum reading, the AmberWave/Thung era-practice bracket,
and the fill-aspect-ratio follow-on calculation, none of which appear in the guide's shortened
example table). Rules applied: R-H3 ("### How deep?" — kept the bold run-in's own words per rule
4, not the guide's illustrative alternate title), R-DERIVATION (5-row input table + 2 numbered
steps + result, with the era-practice and aspect-ratio material kept as prose around it, not
dropped), R-CATEGORY (classification + two-bullet "Specific to this step:" — a clean 2-item case,
no Guide problem 3), R-PARA (two 80+-word "How it is typically performed" items → lead + indented
continuation, with internal R-SENTENCE splits), R-TOOLS (four bullets/tool-groups → the
Tool|Evidence recap table this time, since "Lam 9400 TCP and Lam 4400" already bundles two named
tools into one bullet, taking the count to four), R-RELATED ("Feeds:", "Same module:"), R-OPENQ
(one previously unlabelled bullet), R-GLANCE (box built largely from the guide's own worked
example text). R-TABLE: no separate candidate (the test-tile paragraph in "Why this step exists"
is prose evidence, not parallel rows, and was left alone). R-CODE: no candidate.

Two slips caught by `check_preserved.py` before committing: an early R-TOOLS draft put quotation
marks around "Lam 9400 TCP" and "Lam 4400" (bold in the source, never quoted) — reworded to
plain text, matching page 004's "waffle" lesson (Guide problem 6 applies generally: watch for
quote marks added around a term that was only ever bold or plain in the source).

`check_preserved.py docs/steps/006-stie.md --allow-added markers,numbers,hedges,number_order`:
0 LOST outside `number_order`; the one large LOST/ADDED pair is exactly the trench-depth
paragraph's giant number sequence breaking into the table rows and the two numbered steps — the
textbook case this rule category exists to tolerate when a dense passage is deliberately
restructured. All other checkers and the `-W` build pass; screenshots at both widths read
cleanly — the derivation table and the "Which wavelength"-style recap table both hold at 400 px.

### 007-dnm.md — done

Rules applied: R-TABLE (twice: the four dnwell/nwell design-rule values → Rule|Constrains|Value;
the RSDNW-versus-measured comparison → a "measured against nominal" Parameter|Geometry|Measured|
PDK nominal|Limits table), R-LIST (the three PDK device-page quotes announced by "describe its
uses directly:" → three bullets), R-PARA (the 99- and 84-word numbered-list items under "Why
here?" and "How it is typically performed" → lead + indented continuation), R-SENTENCE (the
"Resist thickness" item's semicolon split), R-HEDGE step 1 (the second industry-generic-recipe
opener on this page, in "How it is typically performed", wrapped in a note — the "Why here?"
section's own numbered list of inference reasons is not a scope sentence and was left alone),
R-CATEGORY (two-bullet "Specific to this step:", a clean case), R-TOOLS (three bullets, under 4,
split), R-RELATED ("Feeds:" on the N-well-ring bullet; the page's own "Previous mask:"/"next
mask:" convention left as is, matching page 004), R-OPENQ (three bullets labelled), R-GLANCE (box
last). R-H3: no candidate (no bold run-in on this page, no section over cap once the two
paragraphs above were table-ised). R-DERIVATION: not applicable (no arithmetic, a straight
measured-vs-nominal comparison, which is R-TABLE's job per §3.2). R-CODE: no candidate.

Two quote-preservation slips caught by `check_preserved.py` and fixed before committing (the same
lesson as Guide problem 6, generalised: pulling a label out of the FRONT of an existing quotation
changes what the quotation covers):
* An early R-CATEGORY/R-TABLE draft paraphrased away the page's own quoted phrase `"must be
  enclosed by nwell by atleast"` for the nwell.5 row — restored the exact quotation in the
  table's "Constrains" cell instead of a paraphrase.
* An early R-LIST draft pulled "20V isolated NMOS FET" out of the front of its quotation to use
  as a bold bullet label, shortening the quoted string — fixed by keeping the full original
  quotation intact and using a non-overlapping label ("20 V isolated NMOS").
Also reworded a first-draft table row that implicitly changed "2 191 Ω" to "2 191 Ω/sq" (adding a
unit not in the source's literal wording, even though the surrounding sentence arguably implies
it) — kept the bare "Ω" from the source and moved the shared "per square two-terminal"
qualifier into the sentence beneath the table instead of inventing a per-cell unit.

`check_preserved.py docs/steps/007-dnm.md --allow-added markers,numbers,hedges,number_order`:
0 LOST outside `number_order` after the fixes above; all `number_order` LOST/ADDED pairs are the
table/list splits (hand-verified). All other checkers and the `-W` build pass; screenshots at
both widths read cleanly, both new tables hold at 400 px.

### 008-dni.md — done

The densest page in the batch: two "Why this step exists" paragraphs at 258 and 121 words, both
full of e-test data (RSDNW resistor measurements, an NPN Gummel-sweep comparison against the
PDK's `POLY` e-test limits), plus an "Energy"/"Dose" bullet pair in "How it is typically
performed" that compares three sources' published values. Rules applied: R-LIST (the "measures
the resulting well directly:" sentence → four bullets), R-TABLE (the RSDNW measured-vs-nominal
table, reused from page 007's pattern since it is literally the same dataset cited independently
here; the NPN Gummel-sweep-vs-`POLY`-limits comparison, transposed to 3 columns — see the phone
note below — after a first 5-column draft cut off on the right at 400 px; the Energy+Dose
bullets merged into one Source|Energy|Dose table, matching the guide's own NWI worked example
shape exactly), R-PARA (the single Axcelis GSD tool bullet, 106 words), R-TOOLS (that same bullet
split into SkyWater says/Tool exists/Runs this step, only one tool so no recap table), R-CATEGORY
(two-sentence classification/specific split), R-RELATED (both combined Previous/Next bullets
split into their own lines; "Feeds:" on the two forward-pointing bullets), R-OPENQ (four bullets
labelled), R-HEDGE step 1, R-GLANCE (box last).

Three preservation slips caught by `check_preserved.py` and fixed before committing, all the
same family of mistake as pages 004/007 (shortening or unquoting a source's exact wording while
condensing it into a table):
* The SkyWater GSD table cell first read only `"10-3000kev"`, dropping the full quoted tool
  listing `"Axcelis GSD High current/energy B11, BF2, P, As, 10-3000kev"` that the source
  "Energy" bullet actually quoted — restored the complete quotation.
* The Hynix energy-range table cell dropped the words "an ion implantation energy of" from the
  front of its quotation — restored the quotation in full.
* The two "DNW to DNW Space" / "Nwell to DNW Space" bullets lost their quotation marks entirely
  (written as plain bold labels) — restored the quotes around the exact test-tile pad names.
Also caught: an early NPN-table draft silently dropped two of the three original mentions of the
"0.316 µA"/"3.16 µA" emitter currents by replacing them with "at two emitter currents" — restored
one explicit mention (the PDK `POLY` sentence introducing the table) so the count matches. And a
genuine false positive: `check_preserved.py`'s hedge matching runs on the raw (non-flattened) page
text, so wrapping "(our extraction" and "from the published measurements" onto two different
source lines made `\bour extraction\b` fail to match even though the phrase reads fine once
Markdown soft-wraps it back together — re-wrapped the line so the phrase sits on one source line
instead of relying on the renderer to rejoin it. This is the same class of issue `check_preserved.py`'s
own comments flag for `QUOTE_RE` (not flattening before matching), just for the hedge patterns
instead of quotes; recorded as Guide problem 7 below since the tool does not flatten hedge text
the way it does for quotes.

`check_preserved.py docs/steps/008-dni.md --allow-added markers,numbers,hedges,number_order`:
0 LOST outside `number_order` after the fixes above; every remaining `number_order` LOST/ADDED
pair hand-verified as a table/list split of the giant data paragraphs. All other checkers and the
`-W` build pass. Screenshots: the first NPN-table draft (5 columns: Emitter current | Measured
gain | PDK nominal gain | Measured V_BE | PDK nominal V_BE) cut off the last column at 400 px;
transposing it to 3 columns (Parameter | at 0.316 µA | at 3.16 µA) fixed it — recorded as Guide
problem 8 (below) since R-TABLE's column-budget rule (§1: "≤6 when every cell is a number, a
code or ≤3 words") technically allows 5 short-celled columns but a table that also carries a
`Source`-shaped first column of longer labels needs the same "split by key or transpose" fallback
R-TABLE step 10 already names for a differently-shaped overflow. All other tables and sections
read cleanly at both widths.

## Guide problems (continued numbering from above)

7. **`check_preserved.py`'s hedge matching is not whitespace-flattened.** Unlike quote matching
   (whose flattening the tool's own comments explain was added for exactly this reason), a hedge
   phrase such as "our extraction" that happens to be split across a Markdown source line wrap
   (soft-wrapped, reads fine rendered) is invisible to `extract_hedges`, producing a false `LOST
   hedges` finding that has nothing to do with the edit's content. Found once on page 008;
   avoided by keeping hedge phrases on one source line rather than depending on the renderer to
   rejoin a wrapped one.
8. **R-TABLE's column budget doesn't anticipate an asymmetric table (one label column, several
   short data columns).** §1's rule ("≤4 columns with prose, ≤6 when every cell is short") reads
   as satisfied by five short data columns, but a table that pairs a row-label column against
   several codes-and-numbers columns can still overflow a 400 px phone even though every
   individual cell qualifies as "short" — the failure mode is the number of columns times their
   minimum content width, not any single cell's length. Transposing (put the thing with few
   values — here, two emitter currents — across the columns, and the thing with many attributes —
   gain, V_BE, measured, nominal — down the rows) fixed it; treated this as the same
   "split by key or transpose" escape hatch R-TABLE step 10 already gives for a table that needs
   more columns than the budget allows, just triggered by column *count* interacting with content
   width rather than by a strict column-count overshoot.

### 009-dnis.md — done

Rules applied: R-SENTENCE (first sentence of "What this step is" split at its comma for the
≤25-word cap), R-PARA (the "Plasma ash" and "Wet strip / clean" numbered items, 95 and 88 words,
→ lead + indented continuation), R-CATEGORY (classification + one-bullet "Specific to this
step:"), R-TOOLS (four bullets → the Tool|Evidence recap table, each split into sub-bullets),
R-RELATED ("Depends on:" for the mask cross-reference pulled out of the Previous bullet; "Same
module:" for the sibling-strips bullet), R-OPENQ (three bullets labelled), R-GLANCE (box last).
R-H3/R-TABLE/R-DERIVATION: no candidate.

**Operational note: local `main` moved during this session.** `check_preserved.py`'s default
`--base main` started reporting an unrelated `LOST`/`ADDED footnotes` pair for `[^thung-2016]` on
this page — a Wayback-link rewrite from the parallel `topic/rd-links` branch that reached local
`main` partway through this session (confirmed: `git diff ee3a94ee main -- docs/steps/003-isonit.md`
and three other already-committed pages in this batch show the same 18-line footnote-URL change,
present in current `main` but not in the commit this branch actually started from). None of this
batch's own edits touch a `## References` footnote definition, so from this page on I pin
`check_preserved.py --base ee3a94ee` (this branch's actual start point, confirmed as the
merge-base with `main`) instead of relying on the default, to stop unrelated upstream churn on
`main` from appearing as a false preservation failure. Checked that pages 001–008 were not
affected: their `check_preserved.py` runs happened before local `main` picked up the rd-links
commits (0-line `ee3a94ee`↔`main` diff for 001, 002, 007, 008 confirms this directly; 003–006's
18-line diff is exactly the same footnote-URL rewrite, and their recorded check runs show no
footnote-category finding, so `main` was still at this branch's start point when those checks
ran).

`check_preserved.py --base ee3a94ee --allow-added markers,numbers,hedges,quotes
docs/steps/009-dnis.md`: exit 0, no `number_order` involvement (no dense multi-number passage was
split on this page). `quotes` newly appears in the allow-list here: the R-TOOLS recap table's
first row repeats the bullet head's own `"Gasonic PEP"`/`"Mattson Aspen2"` quotations verbatim,
the same kind of expected repetition as R-GLANCE's markers/numbers, just in a table this time.
All other checkers and the `-W` build pass; screenshots at both widths read cleanly.

### 010-linox.md — done

Rules applied: R-SENTENCE (first sentence of "What this step is" split at its em-dash for the
≤25-word cap), R-TABLE (the "Public numbers for comparable flows" paragraph — three patents'
liner-thickness/temperature quotes — → a Source|Liner thickness|Temperature table), R-PARA (the
133-word "Rounds the corners" item → lead + indented continuation), R-CATEGORY (two-bullet
"Specific to this step:"), R-HEDGE step 1, R-TOOLS (two bullets, one of which names a second,
alternative tool inside its own parenthetical aside — kept that aside as trailing prose after the
Aviza sub-bullets rather than forcing it into the three-part template, since it grades a
different tool, not a different attribute of the same one), R-RELATED ("Depends on:", "Feeds:"),
R-OPENQ (four bullets labelled), R-GLANCE (box last).

Three quote-preservation slips caught by `check_preserved.py` and fixed before committing — the
by-now-familiar mistake of trimming a quotation's leading words when moving it into a table cell
(this time three at once, all in the same new table): "to a thickness of approximately 100-300 Å"
had "to a thickness of" trimmed off (and this exact quote also appears unedited in the page's own
figure caption, which is how the checker caught a multiset mismatch rather than a same-page
duplicate); "a high temperature (for example, in excess of approximately 1000 degrees C.) oxide
growth process" had its last three words trimmed; "the liner oxidation may take place in a wet,
i.e., steam ambient and/or at a low temperature, i.e., <1000° C." had its first eight words
trimmed (this one also caused a `LOST hedges: 'may'` finding, since the trimmed prefix carried the
page's only "may" — a reminder that a hedge can hide inside a quotation's own wording, not just in
the surrounding prose). All three restored to their full original wording.

`check_preserved.py --base ee3a94ee --allow-added markers,numbers,hedges,number_order
docs/steps/010-linox.md`: 0 LOST outside `number_order` after the fixes; the one `number_order`
LOST/ADDED pair is the "Public numbers" paragraph's giant number sequence breaking into the new
table's rows plus the "Rounds the corners" split, hand-verified. All other checkers and the `-W`
build pass; screenshots at both widths read cleanly, the three-column patent-comparison table
with long quotations wraps well even at 400 px.

### 011-filox.md — done

Rules applied: R-H3 (`### What the public record shows` before the film-thickness/HDP-method
paragraphs, following the page 001/003 pattern), R-PARA (that 137-word block split at its three
natural seams: thickness reasoning, HDP-as-industry-standard, PDK's own silence; the 115-word
"Chemistry" item split at its lead quotation's end), R-TABLE (the 215-word Bianchi/test-tile
paragraph's drain-current comparison across three devices and two `sa`=`sb` extents → a 3-column
Device|At 2.5 µm|At 0.265 µm table, transposed the same way as page 008's NPN table — geometry
values as columns, devices as rows — learned from that page's phone-width lesson), R-SENTENCE
(first sentence of "What this step is" split at its clause boundary), R-CATEGORY (two-bullet
"Specific to this step:"), R-HEDGE step 1, R-TOOLS (two bullets, split), R-RELATED ("Depends
on:", "Feeds:", "Same module:"), R-OPENQ (three bullets labelled), R-GLANCE (box last).

One marker-placement slip caught while re-reading my own diff before running the checker (not by
`check_preserved.py`, which would not have flagged it since the marker count was already correct):
an early draft of the drain-current table split moved `[^raw-data-lv-mosfets]` to sit right after
the table instead of leaving it at the end of the following "thresholds" sentence, effectively
attaching it to a different claim than the one it originally supported. Since the marker's total
page count would have stayed the same either way, this is exactly the kind of same-count-but-wrong-
place error `check_preserved.py`'s own documentation warns it cannot catch ("a footnote marker
moved from one claim to an adjacent one... can... pass with nothing printed") — fixed by reading
the diff itself rather than relying on the tool alone, per agent-briefs.md's instruction to do
so regardless of what the checker reports.

`check_preserved.py --base ee3a94ee --allow-added markers,numbers,hedges,number_order
docs/steps/011-filox.md`: 0 LOST outside `number_order`; the two `number_order` pairs are the
drain-current table split and the Chemistry-item split, hand-verified. All other checkers and the
`-W` build pass; screenshots at both widths read cleanly, including the transposed drain-current
table at 400 px.

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
