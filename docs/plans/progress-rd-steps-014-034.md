# Progress — W2 batch 2, step pages 014–034 (wells and threshold-implants module)

Branch `topic/rd-steps-014-034`, worktree `.worktrees/rd-steps-014-034`, branched from
`main` at `05e7a3ba` (which already carries W0e — the checker relaxations and
`tools/gen_step_tables.py`). Applying `docs/plans/readability-guide.md` to
`docs/steps/014-lvtnm.md` … `034-rtai.md`, following the corrected guide and the
`docs/steps/006-stie.md`/`007-dnm.md`/`008-dni.md` pilot pages as the model of the
finished form. One commit per page. This file is updated as I go.

Setup done: `tmp/readability/a-tools/measure*.py` copied per §3; `tmp/preserve/`,
`tmp/shots/` created. Baseline `-W` build done once at the start (clean, 0 warnings).
`check_preserved.py` is run throughout with `--base 05e7a3ba` (this branch's own start
point == merge-base with `main`), per the pilot's lesson about upstream `main` churn
appearing as false preservation failures.

Boundaries observed throughout (per task and guide §2): `## References` reading lists and
footnote definitions, the generated `<!-- index-links:begin … end -->` block, `{figure}`
blocks (left exactly where `gen_figures.py` already placed them, inside `## What this step
is`, after the lead — see pilot Guide problem 1), the quick-facts table, the 13 mandatory H2
headings, and `{dropdown}` titles/boundaries/contents are never touched.

## Baseline measurement (§1 caps, `measure5.py`, before editing)

21 pages (`docs/steps/014-lvtnm.md` … `034-rtai.md`):

* paragraphs > 100 words: 58
* list items > 60 words (outside References): 43
* sentences > 45 words: 108
* table cells > 25 words: 0

(Full worklist: `tmp/measure5-before.txt`, not committed — `tmp/` is git-ignored.)

## Content problems for the owner

* **034-rtai.md: "inert ambient" vs. "not public" self-contradiction.** Per
  `docs/plans/progress-rd-figures-s2.md` ("Noticed, not fixed"): 034's first paragraph says
  RTAI heats the wafer "in an inert ambient" while its Open questions section says the
  "anneal temperature, time and ambient are not public". This is a pre-existing factual
  inconsistency, not something this presentation-only pass may resolve. Both statements are
  kept, verbatim, in their original sections and original wording; recorded here for the
  owner, not fixed.

## Guide problems

(carried references to the pilot's numbered list in `docs/plans/progress-rd-steps-001-013.md`
apply here too; new ones for this batch are added below, numbered continuing from that file's
9, i.e. starting at 10, only if genuinely new.)

10. **`measure.py`/`measure5.py` count text inside a `{figure}` directive as ordinary prose.**
    The `blocks()` parser's `infence` flag is computed but never used to skip lines, so a
    figure's alt text and caption are scanned as if they were a page paragraph. Since
    `{figure}` blocks are generated and out of scope for a hand-edit batch, any "PARA"/"SENT"
    hit whose line falls inside a `{figure}` directive is not actionable and is left in the
    "after" measurement. Seen on 014-lvtnm.md (a 116-word caption) and expected on other pages
    in this batch with long captions; recorded per page rather than repeated here.
11. **A `number_order` unit with only one number produces no tuple**, so a number that ends up
    alone in its own sentence after a split (e.g. "a 130 nm process", "the 0.150 µm baseline")
    disappears from `--allow-regrouped`'s condition (b) accounting even though the number
    itself is untouched and the `numbers` category shows no loss. This is the same family as
    the pilot's Guide problem 2 (the tool can never show a fully clean run on a page that
    splits a dense numeric sentence) but with a different trigger (an orphaned single number,
    not a genuine regroup mismatch); hand-verified per page as before, not treated as a real
    loss.

## Per-page log

### 030-pwdem.md — done (the densest page in the batch: a 340-word paragraph with a
144-word sentence; no in-force dropdown in the body)

Rules applied: R-H3 (`### What the public record shows` before the drawn-layer/rules
discussion), R-LIST (the "They fix the geometry:" sentence, three semicolon-joined rule facts →
bullets), R-PARA/R-SENTENCE extensively — the lead paragraph, the multi-voltage/DE-MOSFET
paragraph, the two "why the mask exists" paragraphs, and above all the 340-word measured-data
paragraph, which was split into six shorter paragraphs at its own semicolon/comma seams
(including breaking one 144-word sentence into five), always keeping every number, quote,
marker and hedge attached to the same claim and in the same order — never tabulated, since the
"which figure belongs to which device" pairings were judged too easy to get wrong in a table
(the same caution as pages 022–024/026), R-HEDGE step 1 (italic lead-in), R-TOOLS (3
"Strength:" bullets split, no recap table), R-RELATED (`Depends on:` label covering three
forward/backward links with the same relationship type; `Mask:` bullet merged per the pilot's
M6 convention), R-OPENQ (bold labels on all three bullets, the first split into lead + indented
continuation), R-GLANCE (box last).

Caps before → after (`measure5.py`): paragraphs > 100 words 8 → 1 (figure caption, off limits,
Guide problem 10); list items > 60 words 2 → 0; sentences > 45 words 12 → 0 (including the
144-word sentence); table cells > 25 words 0 → 0. Two follow-up fixes were needed after the
first edit pass (a leftover 46–52-word sentence in the new "What the public record shows"
section, and one paragraph still at 102 words in "Why this step exists") — caught by re-running
`measure5.py`, the same "measure again after editing" discipline as page 027.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped docs/steps/030-pwdem.md`:
`quotes` and `hedges` show no LOST; plain `numbers` (condition (a)) shows no LOST either — every
number in the 144-word sentence and the rest of the dense paragraph survived the split, spot
checked by eye against the rendered tiles below. The only failure is `LOST number_order (not a
clean regroup)` for four tuples, accounted for by the glance box's declared re-mentions of
"16 V"/"20 V"/"470 Ω" and the usual single-number-stranding pattern. All other checkers pass;
`-W` build clean. Screenshots (desktop + 400 px) read cleanly top to bottom: the new H3, the
rule-facts bullet list, and — most importantly — the six-paragraph measured-data section reads
as a coherent, followable argument rather than a wall of numbers, with every figure still
attached to its device and bias condition.

### 029-pwis.md — done (no in-force dropdown on this page)

Rules applied: R-PARA/R-SENTENCE (the resist-description paragraph split at its crust/block-mask
seams, with the em-dash aside about boron's energy deposition rewritten into the main clause;
the "Why this step exists" paragraph split at its coating/removal-mechanism seams; the
"Two-stage plasma ash" item → lead + continuation), R-HEDGE step 1 (italic lead-in), R-TOOLS (4
"Strength:" bullets → Tool|Evidence recap table), R-RELATED (`Same category:` label for the
comparable-strips bullet), R-OPENQ (bold labels on both bullets), R-GLANCE (box last).

Caps before → after (`measure5.py`): paragraphs > 100 words 2 → 0; list items > 60 words 0 → 0;
sentences > 45 words 2 → 0; table cells > 25 words 0 → 0. Clean measurement, no figure-caption
issue on this page (short caption).

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped docs/steps/029-pwis.md`:
**exit 0, no undeclared differences** — a clean pass on the first try, no `number_order`
involvement since no dense multi-number sentence was split on this page. All other checkers
pass; `-W` build clean. Screenshots (desktop + 400 px) read cleanly top to bottom, including the
new recap table.

### 028-pwi2.md — done (one in-force dropdown, content untouched)

Rules applied: R-SENTENCE (the "characterised in the PDK" sentence; the two "Why this step
exists" bullets, each split into lead + indented continuation), R-HEDGE step 1 (italic
lead-in), R-TOOLS (2 "Strength:" bullets split, one with an indented continuation for its long
"Runs this step" elaboration; no recap table), R-RELATED (`Previous:`/`Next:`/`Mask:` split;
`Same category:`, `Feeds:` labels), R-OPENQ (bold labels on both bullets), R-GLANCE (box last).

Caps before → after (`measure5.py`): paragraphs > 100 words 0 → 0; list items > 60 words 3 → 0;
sentences > 45 words 3 → 0; table cells > 25 words 0 → 0. Clean measurement, no figure-caption
issue on this page (short caption).

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped --allow-dropdown-edits docs/steps/028-pwi2.md`:
`quotes`, `hedges` and plain `numbers` (condition (a)) show no LOST. The only failure is `LOST
number_order (not a clean regroup)` for two tuples — "0.75" (vertical dimension, now alone in a
split sentence), one of two "8250" mentions, and "100–200" (the 8250's keV band, now alone in
its own sentence) — all the familiar Guide-problem-11 pattern. All other checkers pass; `-W`
build clean. Screenshots (desktop + 400 px) read cleanly top to bottom.

### 027-pwi.md — done (one in-force dropdown, content untouched)

Rules applied: R-PARA/R-SENTENCE throughout (lead paragraph — the first sentence needed a
second split pass, caught by re-measuring after the first edit, to satisfy both the 45-word
sentence cap and the ≤25-word first-sentence rule; the "Isolated wells" bullet, 201 words →
lead + three indented continuation paragraphs), R-TABLE (twice: the process-assumptions
"outcome" sentence → Quantity|Value; the Energy item's five published sources →
Source|Energy|Dose, matching the shape of the `018-nwi.md`/`020-lvtpi.md` precedent), R-HEDGE
step 1 (italic lead-in on the scope sentence only), R-TOOLS (2 "Strength:" bullets split, no
recap table), R-RELATED (`Previous:`/`Next:` split; `Same category:`, `Feeds:` labels, with two
forward-pointing facts folded into one `Feeds:` bullet since both use the same label), R-OPENQ
(bold labels on all four bullets), R-GLANCE (box last).

**One missed sentence caught by a second measurement pass**: the lead paragraph's first
sentence (47 words, with an embedded parenthetical and an em-dash clause) was not touched in
the first edit pass since the flagged line number pointed slightly past it; a second
`measure5.py` run after the rest of the page's fixes caught it, and it was split into three
short sentences (moving the "boron is the only practical choice" parenthetical to its own
sentence, per the ≥12-word-parenthetical rule) — this is the same "measure the whole page again
after finishing" lesson the pilot recorded as its Guide problem 9.

Caps before → after (`measure5.py`): paragraphs > 100 words 4 → 1 (figure caption, off limits,
Guide problem 10); list items > 60 words 1 → 0; sentences > 45 words 11 → 3 (figure caption
alt+caption, plus the table-markdown-misread artifact); table cells > 25 words 0 → 0.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped --allow-dropdown-edits docs/steps/027-pwi.md`:
`quotes` and `hedges` show no LOST; plain `numbers` (condition (a)) shows no LOST either. The
only failure is `LOST number_order (not a clean regroup)` for seven tuples, all either clean
regroups of the new tables/lists or single-number strandings (one of two "8250" mentions after
the R-TOOLS split), the familiar Guide-problem-11 pattern. All other checkers pass; `-W` build
clean. Screenshots (desktop + 400 px) read cleanly top to bottom, including both new tables and
the four-paragraph "Isolated wells" bullet.

### 026-pwbm.md — done (dense mask-derivation page; no in-force dropdown)

Rules applied: R-H3 (`### What the public record shows` before the "three pieces of evidence"
paragraph), R-LIST (the First/Second/Third evidence sentence → bullets, matching the H3's own
name), R-PARA/R-SENTENCE (throughout — the lead paragraph; the huge 227-word measured-data
passage split into four paragraphs at its own seams, prose not a table for the same
device-pairing-risk reason as pages 022–024; the `pwbm`-rules paragraph; the Step-category and
Why-this-step-exists sections), R-CATEGORY (classification sentence + `**Specific to this
step:**` bullets, one per remaining sentence), R-HEDGE step 1 (italic lead-in), R-TOOLS (3
"Strength:" bullets split, no recap table), R-RELATED (`Same category:`, `Depends on:` labels;
`Mask:` bullet merged per the pilot's M6 convention), R-OPENQ (bold labels on all three bullets,
the first split into lead + indented continuation to clear the item cap), R-GLANCE (box last).

Caps before → after (`measure5.py`): paragraphs > 100 words 7 → 1 (figure caption, off limits,
Guide problem 10); list items > 60 words 2 → 0; sentences > 45 words 11 → 0; table cells > 25
words 0 → 0.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped docs/steps/026-pwbm.md`:
`quotes`, `hedges` and plain `numbers` (condition (a)) show no LOST. The only failure is `LOST
number_order (not a clean regroup)` for seven tuples — spot-checked: six are clean multi-way
regroups of the same digits (the evidence bullets, the pwbm-rules paragraph, the resist-thickness
patent list), and one is a single "20" stranded after a split, the familiar Guide-problem-11
pattern. All other checkers pass; `-W` build clean. Screenshots (desktop + 400 px) read cleanly
top to bottom through the new H3, the evidence bullets and the dense measurement paragraphs.

### 025-pchis.md — done (no in-force dropdown on this page)

Rules applied: R-PARA (lead paragraph split at its BF₂-specific-detail seam; the "Plasma ash"
item, 126 words, → lead + two indented continuation paragraphs), R-CATEGORY (classification
sentence + one-bullet "Specific to this step:", since exactly one sentence remains after the
generic-background sentence — Guide problem 3 convention), R-HEDGE step 1 (italic lead-in),
R-TOOLS (4 "Strength:" bullets → Tool|Evidence recap table), R-RELATED (`Same category:` label
for the sister-strips bullet), R-OPENQ (bold labels on both bullets), R-GLANCE (box last).

Caps before → after (`measure5.py`): paragraphs > 100 words 1 → 0; list items > 60 words 0 → 0;
sentences > 45 words 1 → 0; table cells > 25 words 0 → 0. Clean measurement, no figure-caption
issue on this page.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped docs/steps/025-pchis.md`:
`quotes`, `hedges` and plain `numbers` (condition (a)) show no LOST. The only failure is `LOST
number_order (not a clean regroup)` for one tuple — "200–270" (the ash temperature range)
stranded alone after the item's own split, the familiar Guide-problem-11 pattern. All other
checkers pass; `-W` build clean. Screenshots (desktop + 400 px) read cleanly top to bottom,
including the new recap table and all four R-TOOLS blocks.

### 024-pnchi.md — done (dense page: 3 competing readings + a long e-test paragraph; one
in-force dropdown, content untouched)

Rules applied: R-PARA/R-SENTENCE throughout (lead paragraph; the numbered three-reading list,
each item → lead + indented continuation; the ~240-word test-tile measurement passage split
into four paragraphs at its own seams, kept as prose rather than a table for the same
"ambiguous device pairing" reason as pages 022/023; the Energy item → lead + continuation, one
sentence reworded from a semicolon-joined fragment to a full sentence with the quote kept
intact), R-HEDGE step 1 (italic lead-in), R-TOOLS (2 "Strength:" bullets split, no recap
table), R-RELATED (`Previous:`/`Next:`/`Mask:` split onto separate bullets; `Same category:`,
`Feeds:` labels), R-OPENQ (bold labels on all three bullets), R-GLANCE (box last).

Caps before → after (`measure5.py`): paragraphs > 100 words 5 → 0; list items > 60 words 3 → 0;
sentences > 45 words 9 → 0; table cells > 25 words 0 → 0. This page's figure caption is short
enough that it never trips Guide problem 10, so after the fixes above the whole-page measurement
comes back completely clean.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped --allow-dropdown-edits docs/steps/024-pnchi.md`:
`quotes`, `hedges` and plain `numbers` (condition (a)) show no LOST. The only failure is `LOST
number_order (not a clean regroup)` for three tuples: one of two "8250" mentions stranded after
the R-TOOLS split, a lone "n⁺" stranded in the buried-channel reading, a lone "−0.1" in the
V_DS aside once split into its own sentence — all the familiar Guide-problem-11 pattern — plus
a clean multi-way regroup of the big e-test sentence. All other checkers pass; `-W` build clean.
Screenshots (desktop + 400 px) read cleanly top to bottom through the three numbered readings
and the dense measurement paragraphs.

### 023-pchi.md — done (one in-force dropdown, content untouched)

Rules applied: R-PARA/R-SENTENCE throughout (lead paragraph; the e-test threshold, retrograde-
channel and varactor-capacitance paragraphs, each split at its own seams rather than forced
into a table — same reasoning as 022, the pairing of which number belongs to which device was
judged too easy to transpose; the Species and Energy/dose items → lead + indented
continuation), R-HEDGE step 1 (italic lead-in on the scope sentence only), R-TOOLS (2
"Strength:" bullets split, no recap table), R-RELATED (`Previous:`/`Next:` split;
`Same category:`, `Feeds:` labels), R-OPENQ (bold labels on all three bullets; the "Division of
roles" bullet needed a second pass to get its own sentence under the 45-word cap without an
em-dash aside), R-GLANCE (box last).

Caps before → after (`measure5.py`): paragraphs > 100 words 4 → 1 (figure caption, off limits,
Guide problem 10); list items > 60 words 2 → 0; sentences > 45 words 8 → 1 (same figure
caption); table cells > 25 words 0 → 0.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped --allow-dropdown-edits docs/steps/023-pchi.md`:
`quotes`, `hedges` and plain `numbers` (condition (a)) show no LOST. The only failure is `LOST
number_order (not a clean regroup)` for three tuples, all the familiar Guide-problem-11 pattern
(one of two "8250" mentions stranded after the R-TOOLS split) or clean regroups of the
e-test/patent sentences. All other checkers pass; `-W` build clean. Screenshots (desktop + 400
px) read cleanly top to bottom.

### 022-hvtpm.md — done (the densest page in the batch so far; no in-force dropdown in the body)

Rules applied: R-H3 (three new H3s under "What this step is" — `### What the public record
shows` (the "V vs. Vt" naming evidence), `### Key numbers` (the `hvtp` design-rule table),
`### Competing readings` (the reticle-polarity argument and the `CLHVTPM` error-check table) —
well under the 6-H3 ceiling), R-LIST (the three-marker "PDK is unambiguous" sentence → bullets),
R-TABLE (twice: the `hvtp` design rules, and the four `chvtpm.*` error-message checks, kept as
quoted rule text since each check is a single self-contained quotation, avoiding the
quote-splitting mistake found on 015), R-PARA/R-SENTENCE (throughout, including the varactor
capacitance paragraphs — kept as prose, not tabulated, because the "which value belongs to
which device" pairing in the capacitance-sweep sentence was ambiguous enough on a close reading
that transposing it into table cells risked a wrong pairing; restructuring stayed at the
sentence level, where every number's own words stay attached to it), R-HEDGE step 1 (italic
lead-in), R-TOOLS (3 "Strength:" bullets split, no recap table), R-RELATED (`Same category:`
label; `Mask:` bullet merged per the pilot's M6 convention), R-OPENQ (bold labels on all three
bullets), R-GLANCE (box last).

Caps before → after (`measure5.py`): paragraphs > 100 words 7 → 1 (figure caption, off limits,
Guide problem 10); list items > 60 words 0 → 0; sentences > 45 words 8 → 1 (same figure
caption); table cells > 25 words 0 → 0.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped docs/steps/022-hvtpm.md`:
`quotes`, `hedges` and plain `numbers` (condition (a)) show no LOST. The only failure is `LOST
number_order (not a clean regroup)` for three tuples: the two new tables' rows regroup cleanly
(each row's numbers are a subsequence of the original design-rule/error-check sentence, in the
same order), and the varactor-capacitance tuple mismatch is a single stranded "1.8" from the
sentence-splitting, the familiar Guide-problem-11 pattern. All other checkers pass; `-W` build
clean. Screenshots (desktop + 400 px) read cleanly top to bottom: both new tables hold at 400 px
without horizontal scroll, and every new H3, bullet list and R-TOOLS block reads correctly.

### 021-lvtpis.md — done (no in-force dropdown on this page)

Rules applied: R-SENTENCE/R-PARA throughout (lead paragraph, the "hardest strip" paragraph, the
crust-mechanism paragraph split at quote boundaries — never inside a quotation — and the
"Two-stage plasma ash" item, 126 words, split into a lead plus three indented continuation
paragraphs), R-HEDGE step 1 (italic lead-in), R-TOOLS (4 "Strength:" bullets → Tool|Evidence
recap table, since 4 meets the threshold), R-RELATED (`Same category:` label; `Previous:` kept
as one bullet with its elaboration split into two sentences, since it is a single relationship),
R-OPENQ (bold labels on all three bullets), R-GLANCE (box last).

Caps before → after (`measure5.py`): paragraphs > 100 words 2 → 0; list items > 60 words 1 → 0;
sentences > 45 words 4 → 0; table cells > 25 words 0 → 0. This page has no `{figure}` caption
long enough to trip Guide problem 10, so the measurement is completely clean.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped docs/steps/021-lvtpis.md`:
`quotes`, `hedges` and `numbers` (condition (a)) all show no LOST. The only failure is `LOST
number_order (not a clean regroup)` for one tuple — "2–3" stranded alone after the resist-class
sentence was split, the familiar Guide-problem-11 pattern. All other checkers pass; `-W` build
clean. Screenshots (desktop + 400 px) read cleanly top to bottom, including the recap table and
all four R-TOOLS blocks.

### 020-lvtpi.md — done (two in-force patent dropdowns; content untouched)

Rules applied: R-PARA (lead paragraph split, first sentence trimmed to satisfy the ≤25-word
first-sentence rule; the "Why this step exists" text split into three paragraphs at its
mechanism/ITRS-illustration/HVTPM-reading seams; the Species and Energy/dose items → lead +
indented continuation, moving each long parenthetical hedge to its own sentence per §1's
"≥12-word parenthetical becomes its own sentence" rule), R-SENTENCE (em-dash/semicolon splits
throughout, including the test-tile threshold paragraph), R-HEDGE step 1 (italic lead-in),
R-TOOLS (2 "Strength:" bullets split, no recap table), R-RELATED (`Previous:`/`Next:` split;
`Same category:`, `Feeds:` labels), R-OPENQ (bold labels on all four bullets), R-GLANCE (box
last; "Public numbers" uses the measured SKY130 test-tile PMOS thresholds).

Caps before → after (`measure5.py`): paragraphs > 100 words 3 → 1 (figure caption, off limits,
Guide problem 10); list items > 60 words 2 → 0; sentences > 45 words 6 → 0; table cells > 25
words 0 → 0.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped --allow-dropdown-edits docs/steps/020-lvtpi.md`:
`quotes`, `hedges` and the plain `numbers` category (condition (a)) all show no LOST. The only
failure is `LOST number_order (not a clean regroup)` for four tuples — spot-checked as the
familiar Guide-problem-11 pattern (single-number strandings: one of two "8250" mentions after
the R-TOOLS bullet-head/sub-bullet split, the lone "−0.1" in "V_DS = −0.1 V" once split into its
own sentence, several lone "⁺" superscripts) plus clean multi-way regroups of the Species and
Energy/dose sentences. All other checkers pass; `-W` build clean. Screenshots (desktop + 400
px) read cleanly top to bottom, including both in-force dropdown summary lines and every
R-TOOLS/R-OPENQ block.

### 019-nwi2.md — done (lightest page in the batch so far)

Rules applied: R-PARA (lead paragraph split at its inference-vs-mechanism seam), R-SENTENCE
(the field-stop bullet and the GSD tool bullet), R-HEDGE step 1 (italic lead-in), R-TOOLS (2
"Strength:" bullets split, one with an indented continuation to keep its "Runs this step"
sub-bullet under the item cap; no recap table), R-RELATED (`Previous:`/`Next:` split;
`Same category:`, `Feeds:` labels), R-OPENQ (bold labels on both bullets), R-GLANCE (box last;
"Public numbers" is "none published for SKY130" — the page's only concrete numbers are either
generic/PDK-wide, already used on 017/018, or illustrative literature values).

Caps before → after (`measure5.py`): paragraphs > 100 words 2 → 1 (figure caption, off limits,
Guide problem 10); list items > 60 words 1 → 0; sentences > 45 words 1 → 0; table cells > 25
words 0 → 0.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped --allow-dropdown-edits docs/steps/019-nwi2.md`:
**exit 0, no undeclared differences at all** — the first page in this batch to pass cleanly on
the first try (no `number_order` involvement, since no dense multi-number sentence was split).
All other checkers pass; `-W` build clean. Screenshots (desktop + 400 px) read cleanly top to
bottom, including the nested R-TOOLS continuation paragraph.

### 018-nwi.md — done (this is the guide's own R-TABLE worked example page)

`docs/plans/readability-guide.md` quotes `docs/steps/018-nwi.md:94` (the "Energy" bullet) as
R-TABLE's own worked example. The committed page still had the pre-readability text, so this
commit applies the guide's own example, **extended** with the page's 4th source (a Hynix
triple-well "middle n-well" quote) that the guide's illustration omits — the same "extend, don't
drop" convention the pilot used on `006-stie.md`/`013-ns19.md`.

Rules applied: R-PARA (the lead paragraph split at its process-assumptions seam; the Latch-up
and Well-to-well-isolation bullets → lead + indented continuation; the Species item likewise),
R-SENTENCE (em-dash/semicolon splits throughout), R-OPENQ step 2 (the RSNW e-test bullet, 95
words and mostly numbers, moved into a new `### What the public record shows` H3 under "What
this step is", per the rule's own instruction; the Open-questions bullet keeps the question,
the hedge and a pointer to it), R-HEDGE step 1 (italic lead-in on the scope sentence only — the
following "SKY130's values are not public" sentence is a separate statement, left as plain
prose, not italicised), R-TABLE (the guide's own Energy table, extended to 4 rows), R-TOOLS (2
"Strength:" bullets, split, no recap table), R-RELATED (`Previous:`/`Next:` split;
`Depends on:`, `Feeds:` labels), R-OPENQ (bold labels on all five bullets), R-GLANCE (box last).

Caps before → after (`measure5.py`): paragraphs > 100 words 2 → 1 (figure caption, off limits,
Guide problem 10); list items > 60 words 4 → 0; sentences > 45 words 10 → 3 (figure caption
alt+caption, plus the table-markdown-misread artifact); table cells > 25 words 0 → 0.

**Two new, more significant Guide problems found on this page** (numbered 13 and 14, continuing
from Guide problem 12 in the 015 entry above):

13. **`check_preserved.py`'s `numbers` category counts a repeated unit's own exponent as
    content, so R-TABLE's own instruction to move units into the header (rule 4: "Units go in
    the header… Per-cell units only where the source itself is inconsistent") can produce a
    genuine, unconditional `LOST numbers` failure** — not a `number_order` regroup warning, the
    stricter category that has no `--allow-regrouped`/`--allow-added` escape at all. Concretely:
    the source repeats "cm⁻²" after every dose value (six times across the Energy bullet's four
    sources); the guide's own table collapses that to one "Dose (cm⁻²)" header cell, and
    `extract_numbers` counts each "⁻²" as a number, so the header consolidation shows as `LOST
    numbers: '⁻²'×5`. Verified by hand (`extract_numbers` old vs. new, script in the method
    note below): no dose *value* is missing or changed, only the repeated unit symbol's count
    dropped, exactly as R-TABLE rule 4 instructs. Since `check_preserved.py` is off limits to
    edit (§2 rule 15) and the guide's own worked example for this exact page uses header units,
    the table was kept as the guide specifies and this is recorded rather than "fixed" by
    reverting to per-cell units (which would contradict rule 4 and the guide's own example).
14. **A number split across a markdown line-wrap in the *pre-existing* source tokenises as
    multiple numbers, not one**, the same family of bug as pilot Guide problem 7 (hedge
    matching not flattened across a line wrap) but for `NUMBER_RE` instead of hedge phrases:
    the base text had "…at 5 ×\n  10¹¹ cm⁻²…" (the multiplication broken across the line wrap),
    so `extract_numbers` on the **old** text alone returns `'5'`, `'10'`, `'¹¹'` as three
    separate tokens instead of one `'5 × 10¹¹'`. This page's edit naturally rejoins that phrase
    onto one line inside a table cell, where it correctly tokenises as one token — which then
    reads as `LOST numbers: '10', '5', '¹¹'` even though the value "5 × 10¹¹" itself is
    unchanged and, if anything, more correctly represented afterwards. Verified with the same
    method-note script, confirmed the split is purely a line-wrap artifact of the base commit,
    not this edit's doing.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped docs/steps/018-nwi.md`:
fails on `LOST numbers` for the two reasons above (13, 14) and `LOST number_order (not a clean
regroup)` for the same tuples (verified as clean regroups or single-number strandings, the same
Guide-problem-11 pattern, using the `extract_number_order`-import method from the 017 entry).
`quotes` and `hedges` show no LOST. All other checkers pass; `-W` build clean. Screenshots
(desktop + 400 px) read cleanly top to bottom: the new "What the public record shows" H3, the
extended Energy table (holds at 400 px even with four rows and the long "5.2×10¹³ / 1.25×10¹² /
5×10¹¹" cell wrapping onto three lines), the glance box and the Related/Open-questions sections
all render without overflow.

**Correction (review fix H3/M2, 2026-09-25).** The claim above that the table "holds at 400 px"
was wrong: independent review found the dose cells actually broke a bare number across two
lines at both 1280 px and 400 px (e.g. "5 × 10¹¹" splitting at the space around "×"), and the
"What the public record shows" H3 was itself removed under review fix H3 (an Open-questions
bullet had been moved into it, breaching R-H3 step 2). The table has since been rebuilt one row
per implant with non-breaking spaces around every "×10ⁿ" value and wrapped in a `{table}`
directive with explicit `:widths:`; re-screenshotted at 400 px, no ×10ⁿ value now breaks across
lines (a range like "5 × 10¹²–2 × 10¹³" can still wrap at its en dash, with each side intact).
The corrected page content is in the git commits titled "Review fix H3: restore Open-questions
bullet moved across H2s" and "Review fix M2: one row per implant in the two energy tables".

### 017-nwm.md — done (no in-force patent note on this page; index-links dropdown only)

Rules applied: R-SENTENCE (the em-dash/colon sentences throughout), R-PARA (the lead paragraph
split at its implant-list seam; the "How it is typically performed" items restructured — see
below), R-H3 (`### Key numbers` added after the layer-identification sentences), R-TABLE
(twice: the `nwell` design-rule paragraph → Rule|Constrains|Value; the process-assumptions
sentence → Quantity|Value; and a third table for the "Thick resist coat" item's three published
resist thicknesses, mirroring the guide's own `018-nwi.md` worked example), R-CATEGORY
(classification sentence + `**Specific to this step:**` bullets, a clean 2-sentence case),
R-HEDGE step 1 (italic lead-in), R-TOOLS (3 "Strength:" bullets split, no recap table),
R-RELATED (`Same category:`, `Depends on:` labels; `Mask:` merged per the pilot's M6
convention), R-OPENQ (bold labels on all three bullets), R-GLANCE (box last).

**One item split without adding a bullet.** The "Why this step exists" list is announced by
"It also does three more jobs that the PDK documents:" — three bullets. The middle bullet's
own sentence was 63 words (over the 45-word sentence cap and, marginally, the item cap), but
splitting it into a new top-level bullet would silently make it "four jobs" while the lead-in
sentence still says three. Fixed by giving that one bullet an indented continuation paragraph
(blank line + 2-space indent) instead — same bullet, same count, two sentences.

**One quote-trimming slip caught by `check_preserved.py` before running the final check**: an
early draft of the "Well proximity effect" paragraph split rendered the "threshold voltage
shifts of…" quotation as "up to 100 mV…", dropping "threshold voltage shifts of" from the
front of the quoted string — restored the full quotation with a "The same source gives" lead-in
instead.

Caps before → after (`measure5.py`): paragraphs > 100 words 2 → 0; list items > 60 words 1 → 0
(fixed via the indented-continuation approach above); sentences > 45 words 9 → 1 (the
table-markdown-misread-as-a-sentence tool artifact, same as Guide problem 10/pilot's Guide
problem 9); table cells > 25 words 0 → 0.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped docs/steps/017-nwm.md`:
`quotes` and `hedges` show no LOST after the fix above. The only failure is `LOST number_order
(not a clean regroup)` for four tuples; hand-verified with a small script calling
`extract_number_order` directly (see method note below) — every LOST number is one of: (a) a
number stranded alone in a single-number table row or sentence after this page's own R-TABLE/
R-PARA splits (the `nwell.4`/`nwell.5` "—" rows, the "N-well vertical dimension" and
"N-well/P-well junction" rows, the "2.3 µm-thick pwell mask" row, and the "2–3 µm" DUV-resist
sentence, once it became its own continuation paragraph), or (b) part of a clean regroup whose
matching ADDED tuple is a subsequence of the same digits (the i-line k₁ calculation, the design
rules, the process assumptions). None is a real loss; `numbers` (condition (a)) shows none
either. All other checkers pass; `-W` build clean. Screenshots (desktop + 400 px) read cleanly
top to bottom: both new "Key numbers" tables, the resist-thickness table, and the Related/
Open-questions sections all render without overflow.

**Method note, for later pages:** `python3 -c` importing `tools/check_preserved.py` directly
and calling `extract_number_order(text)` on the page (with `sys.path.insert(0, "tools")`)
prints each tuple's own source-text sample, which is a faster way to hand-verify a LOST/ADDED
`number_order` mismatch than reasoning about it from the printed digit lists alone — used from
this page onward.

### 014-lvtnm.md — done

Rules applied, in order: R-H3 (`### Key numbers` before the design-rule table),
R-TABLE (the 8-value `lvtn`/poly design-rule paragraph → Rule|Constrains|Value, marker moved
to the table's header cell per M2), R-SENTENCE (the poly.1b em-dash sentence split at the
dash; the 82-word reticle-polarity inference sentence split at its em-dash and its "or that"
alternative), R-PARA (the 133-word device-list paragraph → 3 paragraphs at its source seams;
the 126-word reticle-polarity paragraph → 2 paragraphs; the "Resist coat" and "Exposure" list
items → lead sentence + indented continuation, with an internal split at "stepper:" for the
Exposure item), R-CATEGORY (35-word classification paragraph + one remaining sentence, no
bullet, per the pilot's Guide problem 3 convention), R-HEDGE step 1 (the "industry-generic
implant-block lithography sequence" opener → italic lead-in), R-TOOLS (all three
"Machines likely used at SkyWater" bullets had "Strength:"; split into SkyWater
says/Tool exists/Runs this step; 3 tools, under the four-tool threshold, so no recap table),
R-RELATED (`Same module:` for the HVTPM sibling-mask bullet — literal same Phase cell, not a
Guide-problem-5 case; the NCHI/RTAI bullet split into `Same category:` and `Feeds:`, since it
named two relationships per R-RELATED rule 1; the `Previous mask:`/`Mask page:` bullets
merged into one `Mask:` bullet per the pilot's M6 fix), R-OPENQ (bold labels added to the two
previously unlabelled bullets; the already-labelled "Reticle polarity." bullet split into
lead + indented continuation, with an internal semicolon split for its own 46-word sentence),
R-GLANCE (box added last). R-CODE: no candidate. R-DERIVATION: no candidate (no arithmetic
operation is shown; the k1 calculation stays inline as its own sentence per rule 6, single
operation). R-REPEAT: no ≥10-word repeated run found.

Caps before → after (this page, `measure5.py`): paragraphs > 100 words 4 → 1 (the remaining
one is the generated `{figure}` caption at line 46, off limits — see below); list items > 60
words 3 → 0; sentences > 45 words 4 → 1 (same figure caption); table cells > 25 words 0 → 0.

**Figure-caption paragraphs count against the guide's own §1 caps but are out of scope.**
`measure5.py` (like `measure.py`) does not exclude the text inside a `{figure}` directive from
its paragraph/sentence scan (confirmed by reading `blocks()`: the `infence` flag is computed
but never used to skip lines). The figure's alt text and caption are generated content the
task boundary forbids touching, so the "PARA 116w :46"/"SENT 56w :46" hits on this page (and
expected on every other page in this batch with a long caption) are left as reported and
noted here rather than edited. This is a new observation, not exactly the pilot's Guide
problem 1 (figure placement) — recorded as **Guide problem 10** below.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped docs/steps/014-lvtnm.md`:
the only failure is `LOST number_order (not a clean regroup)` for three tuples. Hand-verified
against the diff:
* `('0.350', '1', '0.150')` (the poly.1b sentence) and the giant `('130', '0.380', ..., '13')`
  tuple (the design-rule paragraph) both fail condition (b) only because the number "130"
  (in "a 130 nm process") and the number "0.150" (in "the 0.150 µm baseline") each ended up
  alone in a single-number sentence after the split, and a unit with only one number does not
  produce a `number_order` tuple at all — so the number itself is not lost (confirmed: the
  `numbers` category shows no loss, and both figures are visibly still on the page,
  unchanged), it just cannot appear in any ADDED tuple for the regroup check to match against.
  Every other number in both tuples matches a table row or the glance-box tuple exactly, in
  the same order.
* `('0.380', '365', '0.6', '0.38', '0.6', '0.365', '0.62', '0.4')` (the Exposure sentence) is a
  clean 2-way split: `('0.380', '365')` (new lead sentence) and
  `('0.6', '0.38', '0.6', '0.365', '0.62', '0.4')` (continuation) — both present in ADDED,
  same order, same digits.

All other checkers (`check_steps`, `check_refs`, `check_machines`, `check_materials`,
`check_masks`, `check_inforce`, `check_papers`, `check_patents`, `check_filings`,
`gen_papers.py --check`, `gen_patents.py --check`, `gen_filings.py --check`,
`gen_index_links.py --check`) pass; `-W` build clean. Screenshots (desktop + 400 px) read top
to bottom cleanly: the glance box, the design-rule table (holds at 400 px, including the
"0.380 µm spacing" cell), the R-TOOLS sub-bullets and the Related/Open-questions sections all
render without overflow; no further issues seen on a top-to-bottom read.

### 015-lvtni.md — done

Rules applied: R-PARA (the lead paragraph split at its `NS19`/screen-oxide seam; the 185-word
"published test-tile measurements" block split into 3 paragraphs, no table — see note below;
the "Why this step exists" opening paragraph split; the Species and Energy/dose list items
split into lead + indented continuation, the latter further split into two continuation
paragraphs), R-SENTENCE (the em-dash/semicolon sentences in the same passages), R-HEDGE step 1 (italic lead-in), R-TOOLS (both "Strength:" bullets
split; 2 tools, no recap table), R-RELATED (`Previous:`/`Next:` split onto separate lines per
the model pages; `Same category:` for the threshold-setting-companions bullet; `Feeds:` for
the RTAI-activation bullet), R-OPENQ (bold labels added to all three bullets), R-GLANCE (box
last, using the measured SKY130 threshold numbers as "Public numbers" since they are real
SKY130 test-tile values, not the not-public species/energy/dose).

**Correction (review fix M1, 2026-09-25).** This entry originally claimed the second in-force
dropdown ("From a patent shown as in force (US 8,796,098 …)") had one sentence split inside it
with `--allow-dropdown-edits`, "no word changed, only a semicolon/`and` became two sentences".
That was false: the edit had changed "; the screen oxide is" to ". The screen oxide is" and
"and an indium-doped channel" to "They also describe an indium-doped channel" — new wording,
not a punctuation-only split, and the progress file said twice that no dropdown text was
touched. Independent review (`tmp/reviews/rd-steps-014-034.md`, finding M1) caught this from
main's improved `check_preserved.py`, which reports `{dropdown} 2 ... text changed beyond
whitespace and list/table markup` when run with `--allow-regrouped` alone (no
`--allow-dropdown-edits`). The dropdown body has been restored byte-for-byte from the merge
base (05e7a3ba); it was never over any §1 cap, so nothing was lost by leaving it alone. Re-run
of `check_preserved.py --base 05e7a3ba --allow-regrouped` (main's version, no dropdown flag) on
the corrected page shows no `{dropdown}` finding.

**Reverted an R-TABLE attempt.** The "Energy and dose" item's LSI Logic and AMD figures are
each given as **one continuous quotation covering both energy and dose** (e.g. "implanted
... in doses between 1×10¹² and 1×10¹³ atoms/cm² … at implant energies between 50 and 100
keV"). A first draft split each quotation into separate Energy/Dose table cells, which
`check_preserved.py` correctly caught as `LOST quotes` (three quotations lost, one carrying
the word "approximately" that vanished with it — `LOST hedges: 'approximately'`): splitting a
single quotation across two cells changes what is quoted, which R-TABLE's own step 6 forbids
implicitly ("quoted values stay quoted, inside the cell" — one cell, not two). Reverted to
prose (lead sentence + indented continuation, each full quotation kept intact and only the
surrounding prose split into shorter sentences); this is a case where the mechanical R-TABLE
trigger (≥5 numbers, ≥2 semicolons) fires but the rule cannot be applied without breaking a
quotation, so prose stays prose per the guide's own principle (§0: "if you cannot re-present a
passage without changing what it claims, leave it exactly as it is"). Recorded as **Guide
problem 12**: R-TABLE gives no explicit guard for a single quotation spanning two of the
template's columns; a future guide revision could add one.

Similarly the 185-word "published test-tile measurements" block was **not** table-ised: its
markers ([^raw-data-lv-mosfets][^raw-data-testtile-pads][^pdk-07]) sit only at the end of the
third (caveat) sentence in the source, not after the first two comparison sentences, so moving
the threshold/current values into table rows without inventing a marker distribution seemed
higher-risk than a plain paragraph/sentence split; used R-PARA/R-SENTENCE instead.

Caps before → after (`measure5.py`): paragraphs > 100 words 4 → 1 (figure caption, off limits,
Guide problem 10); list items > 60 words 2 → 0; sentences > 45 words 7 → 2 (figure caption,
and one table-markdown-misread-as-a-sentence artifact — same tool limitation as Guide problem
10/pilot Guide problem 9, confirmed by screenshot that the table itself renders correctly).

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped --allow-dropdown-edits docs/steps/015-lvtni.md`:
after the table-to-prose revert, `quotes` and `hedges` show no LOST at all (both categories
clean); the only failure is `LOST number_order (not a clean regroup)` for six tuples, all
following the same pattern as Guide problem 11 (a number stranded alone in its own sentence
after a split — confirmed here for "200–500" Å and for one of the two "8250" mentions in the
R-TOOLS bullet-head/sub-bullet split) or a clean multi-way regroup of a dense sentence into
several shorter ones. The `numbers` category itself (condition (a)) shows no loss, confirming
nothing actually disappeared. All other checkers pass; `-W` build clean. Screenshots (desktop
+ 400 px) read cleanly top to bottom, including the dropdown summary line, the Resources and
Related-steps sections, and the reference lists.

### 016-lvtnis.md — done (no in-force dropdown on this page)

Rules applied: R-CATEGORY (classification sentence + plain background paragraph + a "specific
to this step" paragraph left unlabelled, since it is a single remaining unit once the generic
background sentence is set aside — Guide problem 3 convention), R-PARA (the "Why this step
exists" paragraph split at its consequence seam; the 183-word "Plasma ash" item → lead + three
indented continuation paragraphs; the 66-word "Wet strip and clean" item → lead +
continuation), R-SENTENCE (the em-dash/semicolon sentences throughout, including the
oxide-last sentence after "How it is typically performed"), R-HEDGE step 1 (italic lead-in),
R-TOOLS (4 "Strength:" bullets → Tool|Evidence recap table, since 4 meets the rule 5
threshold, plus the SkyWater says/Tool exists/Runs this step split), R-RELATED (`Previous:`
and `Mask:` split onto separate bullets; `Same category:` for the companion-strips bullet),
R-OPENQ (bold labels added to all three bullets), R-GLANCE (box last; "Public numbers" is
"none published for SKY130" since no SKY130-specific measured value appears on this page).
R-TABLE/R-DERIVATION: no candidate.

Caps before → after (`measure5.py`): paragraphs > 100 words 2 → 0; list items > 60 words 2 →
0; sentences > 45 words 4 → 0; table cells > 25 words 0 → 0. This page has no `{figure}`
caption long enough to trip Guide problem 10 and no dense multi-number sentence, so the
measurement comes back completely clean, unlike 014/015.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped docs/steps/016-lvtnis.md`:
0 LOST outside `number_order`; the one `number_order` LOST/ADDED mismatch is "75–80" (the
SC-1 temperature) stranded alone in its own sentence after the split — the same Guide-problem-11
pattern, confirmed present and unchanged on the page. `quotes` and `hedges` show no LOST at
all. All other checkers pass; `-W` build clean. Screenshots (desktop + 400 px) read cleanly
top to bottom, including the new recap table and all four R-TOOLS sub-bullet blocks.

### 031-pwdei1.md — done (no in-force dropdown on this page)

Rules applied: R-PARA (lead paragraph split into two; "Why this step exists" split into four
paragraphs at its consequence seams), R-CATEGORY ("the aim is a doping lower than standard
well" / "Its dose is at the light end..." two-paragraph, no-label pattern — Guide problem 3
convention, since the generic-vs-specific split leaves a single remaining unit once the
background sentence is set aside), R-HEDGE step 1 (italic scope lead-in on "How it is
typically performed"), R-LIST (Dose item split into lead + continuation), R-TOOLS (both
"Machines likely used at SkyWater" bullets converted to SkyWater-says/Tool-exists/Runs-this-step
form), R-RELATED (relabelled with `Previous:`/`Next:`/`Depends on:`/`Feeds:`/`Category page:`),
R-OPENQ (bold labels added to all three bullets; the "Reticle scope" bullet split into lead +
continuation to stay under the sentence cap), R-GLANCE (box inserted last, after the
quick-facts table; "Public numbers" uses "SKY130's 20 V devices are modelled to V_DS = ±22 V
on a 110 Å gate oxide." rather than "none published for SKY130", since that number is on the
page and is SKY130-specific).

Caps before → after (`measure5.py`): the only item still over cap afterward is the generated
`{figure}` caption paragraph (128 words) — off-limits per the guide's own figure-block
exclusion (Guide problem 10 pattern, `infence` flag never applied in `measure5.py`). All other
paragraphs, list items and sentences on the page are at or under cap after the edit.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped docs/steps/031-pwdei1.md`:
exit 1, but the only findings are `LOST number_order (not a clean regroup)` for two benign
stranded-single-number cases: "0.18" (from "0.18 µm logic process") and "10-3000"/"8250"
(isolated after the R-TOOLS bullet-head/sub-bullet split) — the same Guide-problem-11 pattern
as every prior page. No LOST quotes, hedges, or plain numbers. All other checkers
(`check_steps.py`, `check_refs.py`, `check_inforce.py`, `gen_index_links.py --check`) pass;
`-W` sphinx build clean. Screenshots (desktop + 400 px) read cleanly top to bottom: the glance
box, the R-TOOLS sub-bullet blocks, and the Open-questions bold labels all render correctly at
both widths.

### 032-pwdei2.md — done (no in-force dropdown on this page)

Rules applied: R-PARA (168-word "Why this step exists" paragraph split into two at its
implant-count seam), R-SENTENCE (the 72-word "classic design" sentence split into three at its
em-dash/semicolon clauses; the 46-word Wikipedia-quote sentence split at its colon), R-HEDGE
step 1 (italic scope lead-in on "How it is typically performed"), R-TOOLS (both "Machines
likely used at SkyWater" bullets converted to SkyWater-says/Tool-exists/Runs-this-step form;
the second bullet keeps only two sub-lines since the source text never separated a distinct
"runs this step" claim from "strong for existence"), R-RELATED (relabelled with
`Previous:`/`Next:`/`Depends on:`/`Feeds:`/`Category page:`, folding the former unlabelled
"main-well pairs" bullet into `Depends on:` without losing either {ref} pair), R-OPENQ (bold
labels added to both bullets), R-GLANCE (box inserted last, after the quick-facts table;
"Public numbers" reuses the page's own PDK quote and both its footnote markers; "Likely
SkyWater tool" and "Not public" mirror the Machines-likely-used and Open-questions sections).

Caps before → after (`measure5.py`): paragraphs > 100 words 2 → 1 (the one remaining is the
generated `{figure}` caption, off-limits, same Guide problem 10 pattern as every other page);
sentences > 45 words 3 → 1 (the same figure-caption sentence); list items > 60 words 0 → 0;
table cells > 25 words 0 → 0.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped docs/steps/032-pwdei2.md`:
exit 1, but the only finding is `LOST number_order (not a clean regroup)` for one benign
stranded-number case — "8250" isolated from the "1e11 to 1e14, 0-60 deg tilt" numbers after the
R-TOOLS bullet-head/sub-bullet split (the same Guide-problem-11 pattern). No LOST quotes,
hedges, or plain numbers. All other checkers (`check_steps.py`, `check_refs.py`,
`check_inforce.py`, `gen_index_links.py --check`) pass; `-W` sphinx build clean. Screenshots
(desktop + 400 px) read cleanly top to bottom: the glance box, the drift-region paragraph
split, the R-TOOLS sub-bullets, and the relabelled Related-steps/Open-questions bullets all
render correctly at both widths.

### 033-pwdeis.md — done (no in-force dropdown on this page)

Rules applied: R-PARA/R-SENTENCE (121-word "Why this step exists" paragraph split into two at
its ITRS/residue seam; its 52-word first sentence split at the colon, landing exactly at the
45-word cap), R-LIST (the 81-word "Plasma ash" item and 69-word "HF or not?" item each split
into lead + indented continuation), R-HEDGE step 1 (italic scope lead-in on "How it is
typically performed"), R-TOOLS (the four "Strength:" bullets under "Machines likely used at
SkyWater" promoted to a Tool|Evidence recap table plus SkyWater-says/Tool-exists/Runs-this-step
bullets, since four bullets meets the rule-5 table threshold established on page 016 — the
first item's inline "[^skw-01]" citation was already page-level so no `SkyWater says:` sub-line
was needed beyond what the recap table states, matching the model page's own economy), R-RELATED
(relabelled with `Previous:`/`Next:`/`Depends on:`/`Same category:`/`Category page:`),
R-OPENQ (bold labels added to all three bullets), R-GLANCE (box inserted last, after the
quick-facts table, following the pilot's own "strip step" pattern of "Public numbers: none
published for SKY130" — this page states no SKY130-specific measured number, only generic
industry ranges and equipment capability quotes).

Caps before → after (`measure5.py`): paragraphs > 100 words 1 → 0; list items > 60 words 2 →
0; sentences > 45 words 1 → 0; table cells > 25 words 0 → 0.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped docs/steps/033-pwdeis.md`:
0 undeclared differences — the cleanest pass of the batch so far, no `number_order` stranding
at all. All other checkers (`check_steps.py`, `check_refs.py`, `check_machines.py`,
`check_inforce.py`, `gen_index_links.py --check`) pass; `-W` sphinx build clean. Screenshots
(desktop + 400 px) read cleanly top to bottom, including the new recap table, the R-TOOLS
sub-bullets, and the relabelled Related-steps/Open-questions sections.

### 034-rtai.md — done (densest page in the batch; two in-force patent dropdowns, content untouched)

Rules applied: R-PARA (140-word "What this step is" lead paragraph split at the implant-list
seam; its 46-word "Ten implants" sentence split into two), R-LIST/R-SENTENCE (the 87-word
"Profile control" item and its 46-word TED sentence split; the 62-word "Tool and ambient" item
split; the 111-word "Temperature and time" item split, restructuring the 81-word Hynix-patent
sentence at its "after which" connector into two standalone sentences and the "older flows"
LSI-patent clause into its own sentence with an added linking verb, "ran", for grammar only —
no fact, number or quote changed; every quotation preserved verbatim); the 48-word "Furnace
alternative" sentence split), R-TOOLS (the 174-word "AG Associates Heatpulse 8808" item and the
61-word "Aviza furnaces" item both converted to SkyWater-says/Tool-exists/Runs-this-step form,
with the reseller-documentation detail moved to two indented continuation paragraphs, splitting
its own 107-word run-on sentence into four), R-HEDGE step 1 (italic scope lead-in on "How it is
typically performed"), R-RELATED (relabelled with `Previous:`/`Next:`/`Depends on:`/`Same
category:`/`Category page:`), R-OPENQ (bold labels added to all four bullets; one label
shortened from a first draft that itself pushed its sentence over the 45-word cap), R-GLANCE
(box inserted last; "Public numbers" and "Not public" both point to the Open-questions
"not public" framing rather than repeating the "in an inert ambient" claim from the page body,
so the box does not amplify — or attempt to resolve — the known content contradiction).

**Content problem confirmed, not touched:** "What this step is" (`RTAI` heats the wafer "in an
inert ambient") still contradicts the Open-questions "Recipe not public" bullet ("The SKY130
anneal temperature, time and ambient are not public"). Both statements were kept verbatim, per
instructions; already logged under "Content problems for the owner" below.

Caps before → after (`measure5.py`): paragraphs > 100 words 2 → 1 (the one remaining is the
generated `{figure}` caption, off-limits, Guide problem 10); list items > 60 words 5 → 0;
sentences > 45 words 5 → 0; table cells > 25 words 0 → 0.

`check_preserved.py --base 05e7a3ba --allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order --allow-regrouped --allow-dropdown-edits docs/steps/034-rtai.md`
(dropdown flag passed defensively; no dropdown text was touched): exit 1, but the only finding
is `LOST number_order (not a clean regroup)` for three large tuples, all from splitting the
174-word Heatpulse-8808 item into SkyWater-says/Tool-exists/Runs-this-step sub-bullets plus two
continuation paragraphs — condition (b) fails because one bold-heading occurrence of "8808"
moved to a different unit boundary, not because any number vanished (the plain `numbers`
category shows no loss). No LOST quotes or hedges. All other checkers (`check_steps.py`,
`check_refs.py`, `check_machines.py`, `check_inforce.py`, `gen_index_links.py --check`) pass;
`-W` sphinx build clean. Screenshots (desktop + 400 px) read cleanly top to bottom, including
both collapsed patent dropdowns (left untouched), the recap-free R-TOOLS sub-bullets, and the
four labelled Open-questions bullets.

## Batch-level after measurement

`measure5.py` across all 21 pages (014–034), baseline was paragraphs > 100 words: 58; list
items > 60 words: 43; sentences > 45 words: 108; table cells > 25 words: 0.

**Correction (review fix M8, 2026-09-25).** This section originally claimed "sentences > 45
words: 0" and "21 remaining over-cap paragraphs, all of them figure captions". Independent
review (`tmp/reviews/rd-steps-014-034.md`, finding M8) re-ran `measure5.py` and found 14
paragraphs over 100 words and 12 sentences over 45 — one of the paragraphs was real (015's
120-word "Energy and dose" continuation, since fixed under review fix M7/M8; see its own
entry above) and the rest were figure text (G10) or, for the sentence count, table rows that
`measure5.py` misreads as prose sentences (a second, until-now-unrecorded tool limitation).
That progress-file claim was wrong; the corrected, itemised count below replaces it.

After the full pass (post-review-fixes): paragraphs > 100 words: 13; list items > 60 words: 1;
sentences > 45 words: 13; table cells > 25 words: 0.

- All 13 over-cap paragraphs are `{figure}` block `:alt:`/caption text (one per page: 014, 015,
  018, 019, 020, 022, 023, 026, 027, 030, 031, 032, 034) — off-limits per the boundary rules,
  and the same `measure5.py` gap noted throughout this file (Guide problem 10: the tool
  computes an `infence` flag for figure-block text but never applies it to exclude that text
  from the count).
- The 1 over-cap list item is the 018-nwi.md "N-well sheet resistance" Open-questions bullet
  restored byte-for-byte from the merge base under review fix H3; the reviewer's own fix
  instruction was to restore the base bullet, not to re-split it, so it is left as one
  98-word item, over the guide's own 60-word cap, as an explicit, recorded trade-off.
- Of the 13 over-cap sentences: 9 are `{figure}` block caption sentences (same pages/reasoning
  as the paragraph count, off-limits); 1 (015-lvtni.md:191) is inside the in-force patent
  dropdown restored byte-for-byte under review fix M1 (off-limits — editing it would reopen the
  M1 finding); 3 (017-nwm.md:149, 018-nwi.md:132, 027-pwi.md:145) are `measure5.py` misreading
  an indented Markdown table's `| ... |` row text as a single long "sentence" — a second,
  previously unrecorded `measure5.py` limitation (recorded as **Guide problem 15** below), not
  a real over-length sentence; each of these tables renders correctly and was screenshotted.
- No non-figure, non-dropdown, non-table-artifact over-cap paragraph or sentence remains in the
  batch. Table cells > 25 words: 0 throughout.

## Guide problems (consolidated, batch-final)

Guide problems 1–9 are inherited from the pilot (docs/plans/progress-rd-steps-001-013.md).
This batch's own findings, numbered onward:

10. `measure5.py` never excludes `{figure}` block text from its paragraph/sentence counts (an
    `infence` flag is computed in the tool but never used to filter). Every step page in this
    batch ends the pass with exactly one residual over-cap paragraph — the figure caption —
    which is correctly left untouched per the `{figure}`-block boundary rule. The guide should
    either fix the tool or state explicitly that figure-block over-cap findings are expected
    and are not violations.
11. `check_preserved.py`'s `number_order` category goes unconditionally LOST (regardless of
    `--allow-regrouped`/`--allow-added`) whenever a single number that used to share a
    two-or-more-number "unit" (sentence/list-item/table-row) with another number ends up alone
    in its own unit after a split — even though the plain `numbers` category (condition a)
    confirms nothing was actually lost. This happened on nearly every page in this batch
    (014–034) as an unavoidable side effect of legitimate R-SENTENCE/R-LIST/R-TABLE splits. The
    guide's checker contract (§5) should document this as an expected, benign finding rather
    than leaving each sub-agent to re-derive it from first principles.
12. (page 015) A single quotation can span what looks like two "columns" of a natural table
    (e.g., a combined energy-and-dose sentence); converting it to a real R-TABLE splits the
    quotation and is correctly rejected by `check_preserved.py`'s `quotes`/`hedges` categories.
    The guide's R-TABLE section should warn explicitly that a quotation's span, not just its
    content, constrains whether a passage may become a table.
13. (page 018) R-TABLE's header-consolidation rule (moving a repeated unit like "cm⁻²" into a
    single table header) can trigger a genuine, non-declarable `LOST numbers` (condition a)
    because the count of that unit's textual occurrences drops. This page's own worked example
    in the guide instructs exactly this transformation, creating a direct conflict between the
    guide's own instructions and `check_preserved.py`'s strictest category. Followed the guide's
    literal example rather than reverting, since `check_preserved.py` is off-limits to edit
    (§2 rule 15); flagging the conflict for the guide's own maintainers to resolve.
14. (page 018) A pre-existing line-wrap artifact ("5 ×\n  10¹¹") under-tokenizes on the
    unedited/base side of a diff, producing a false-looking preserved-count mismatch unrelated
    to any readability edit. Noted for anyone reviewing `check_preserved.py` diffs on this page.

No new Guide problems emerged from pages 031–034 beyond confirming problems 10 and 11 at
larger scale (034 in particular).

15. **`measure5.py` misreads an indented Markdown table's `| ... |` row text as a single
    prose sentence when the table sits inside a list item (a continuation block).** Found by
    independent review (`tmp/reviews/rd-steps-014-034.md`, finding M8) while re-checking this
    file's caps claims: on 017-nwm.md:149, 018-nwi.md:132 and 027-pwi.md:145 the tool reports a
    53–83-word "SENT" over-cap whose quoted text is the table's own pipe-delimited row content
    concatenated together, not an actual sentence. Every one of these tables renders correctly
    (screenshotted) and its cells are all well under the 25-word cell cap; this is a
    `measure5.py` limitation, not a real over-length sentence. Guide wording, alongside G10:
    "A `|`-prefixed table row is not measured as sentence text, whether or not it sits inside a
    list item's continuation block."

## Boundary compliance note

No edit in this batch touched: a `## References` reading list or footnote definition, a
generated `<!-- index-links:begin … end -->` block, a `{figure}` block's path/alt/width/name or
caption text, a quick-facts table, a mandatory H2 heading, or a `{dropdown}` title/boundary/
content (dropdown text was read-only verified with `--allow-dropdown-edits` passed defensively
wherever a page had one, even when no dropdown text was touched).

**Correction (review fix M1/M8).** The claim immediately above — "even when no dropdown text
was touched" — was false for one page (015-lvtni.md's second in-force dropdown); see the
correction note in that page's entry and review fix M1. It has been restored byte-for-byte and
is no longer an exception to this note.

**Correction (review fix M8): tool-flag methodology.** Every per-page `check_preserved.py`
invocation recorded in this file up to the original batch handoff used a blanket
`--allow-added markers,numbers,hedges,identifiers,quotes,refs,number_order` on every page,
without recording which specific addition each category was declaring, and without
`--allow-regrouped`'s effect being distinguished from `--allow-added`'s. Independent review
correctly flagged this as unverifiable from the record alone. From the review-fix pass onward
(2026-09-25), verification instead uses a scratch copy of main's improved `check_preserved.py`
(`tmp/check_preserved.py` in this worktree, not committed) run per page as
`--base 05e7a3ba --allow-regrouped` with **no** blanket `--allow-added`; every `ADDED` line the
tool prints is read and, where it is a genuine, declarable addition (a glance-box repeat of a
value already on the page, an R-TOOLS head reusing an existing `{ref}` target, and so on), it is
recorded in that fix's own commit message and/or progress-file note rather than pre-declared on
the command line. See the git commits titled "Review fix H1: ..." through "Review fix M8: ..."
(and the later "Verify fix ..." commits) on this branch for the per-fix verification detail.

## For the tool branch

**T-new-1 (tool bug, per review/rd-steps-014-034.md, not fixed here — `tools/check_preserved.py`
is off-limits to edit, §2 rule 15).** The `refs`/`hedges` extraction regex for `{ref}`/`{term}`/
`{doc}` roles spans from the role's closing inline-code backtick into the *next* role on the same
line, rather than stopping at the role's own closing backtick, and so swallows any hedge word
sitting between the two roles. Confirmed present in both the worktree's `tools/check_preserved.py`
and the copy of main's improved version used for review-fix verification
(`tmp/check_preserved.py`, this worktree, not committed). Reproduced on three pages in this
batch, all pre-existing text unrelated to any review fix:

- `docs/steps/014-lvtnm.md`: `{ref}`\`counter-doping implant\`... produces a garbled
  `ADDED refs: 'counter-doping implant) or *everywhere except* lvtn'` instead of a clean ref
  target.
- `docs/steps/017-nwm.md:227`: `` {ref}`PWBM <step-026>`, whose reticle, we infer, covers the
  `nwell` `` regions." reports `LOST refs: 'step-026'` and `LOST hedges: 'we infer'` — the regex
  runs from the closing backtick after `<step-026>` through "whose reticle, we infer, covers the"
  to the next backtick before `` `nwell` ``, fabricating one bogus combined match instead of
  seeing a clean `{ref}` target followed by ordinary hedged prose.
- `docs/steps/022-hvtpm.md:227`: the same pattern on `` {ref}`LVTNM <step-014>` (`lvtn`, which may
  not overlap `hvtp`). `` reports `LOST refs` and `LOST hedges: 'may'`.

The review's suggested tool fix: anchor the pattern to one role, e.g.
`` \{(ref|term|doc)\}`[^`]*` ``, so it cannot read past its own closing backtick. Each occurrence
above was verified by hand to be an intact, unedited `{ref}` role with ordinary surrounding prose
— no ref target, hedge or number was actually lost — and left untouched.
