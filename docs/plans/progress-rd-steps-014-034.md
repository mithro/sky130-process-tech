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
paragraphs), R-SENTENCE (the em-dash/semicolon sentences in the same passages; one sentence
inside the in-force dropdown, per §2 rule 5, which allows R-SENTENCE inside a dropdown to text
already there — done with `--allow-dropdown-edits`, no word changed, only a semicolon/`and`
became two sentences), R-HEDGE step 1 (italic lead-in), R-TOOLS (both "Strength:" bullets
split; 2 tools, no recap table), R-RELATED (`Previous:`/`Next:` split onto separate lines per
the model pages; `Same category:` for the threshold-setting-companions bullet; `Feeds:` for
the RTAI-activation bullet), R-OPENQ (bold labels added to all three bullets), R-GLANCE (box
last, using the measured SKY130 threshold numbers as "Public numbers" since they are real
SKY130 test-tile values, not the not-public species/energy/dose).

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
