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

### 041-onom.md — done (3 hand-written in-force notes in the body plus their copies
under References; content untouched, sentences split inside them under R-DROPDOWN
rule 2 — inside the 037–044 in-force-sweep range)

Rules applied: R-PARA/R-SENTENCE throughout (lead split at its stack/lithography seam;
the PDK-evidence paragraph split in two at its lists/inference seam; R-CATEGORY on
"Step category" — 24-word classification + `**Specific to this step:**` and 3 bullets;
all three "Why this step exists" paragraphs split extensively at their em-dashes,
colons and semicolons, always keeping the parenthetical-vs-em-dash count at 0–1 per
sentence; R-HEDGE step 1; the Exposure item's "would be measured… or, equally
possible…" sentence split at its "or" alternative), R-SENTENCE **inside two
`{dropdown}` notes** (splitting only before/after complete quotations — one 65-word
quotation was left whole since it is a single indivisible quoted clause with no
internal sentence break, the same accepted-exception pattern as 037's `PTSI` page),
R-TOOLS (3 "Strength:" bullets → SkyWater-says/Tool-exists/Runs-this-step form; no
recap table), R-RELATED (`Previous:`, `Next:`, `Depends on:`, `Same category:`,
`Mask:`, `Category page:`), R-OPENQ (bold labels on all four bullets, the ARC-use
bullet split into lead + indented continuation), R-GLANCE (box inserted last; checked
against `check_inforce.py` before commit, following 040's lesson — no in-force-patent
figure went into it, since none of this page's public numbers come from an in-force
note; "Public numbers" is "none published for SKY130").

Caps before → after (`measure5.py`): paragraphs > 100 words 6 → 1 (figure caption, off
limits); list items > 60 words 1 → 0; sentences > 45 words 11 → 2 (the figure caption,
plus the one accepted indivisible-quotation exception above).

`uv run python tools/check_preserved.py --base 4a4ed3cf --allow-added
markers,numbers,hedges,identifiers,number_order --allow-regrouped --allow-dropdown-edits
docs/steps/041-onom.md`: **0 undeclared differences**, no LOST in any category. All
other checkers, `check_inforce.py` included, pass; `-W` build clean. Screenshots
(desktop + 400 px) read cleanly top to bottom; both dropdowns collapsed and untouched.


### 040-ono.md — done (the densest page in the batch: 5 hand-written in-force notes in
the body plus their copies under References; content untouched, sentences split
inside them under R-DROPDOWN rule 2 — inside the 037–044 in-force-sweep range)

Rules applied: R-PARA/R-SENTENCE extensively throughout the open prose (the lead split
into 2 sentences/paragraphs; the Cypress-patent-embodiments paragraph split into 3
paragraphs, each embodiment its own sentence instead of a semicolon chain; R-CATEGORY
on "Step category" — 30-word classification + `**Specific to this step:**` and 2
bullets; the "Why this step exists" opening quotations split at their "and" joins
without altering any quote's own wording; both long bulleted "layer job" items split
into lead + indented continuation; the "formed *here*... for two reasons" sentence
split at its em-dash; R-HEDGE step 1 on the numbered-list intro (only the true scope
sentence italicised, not the following explanatory sentence — a mistake caught and
fixed on this page, see below); all four numbered-list items split into lead +
continuation), R-SENTENCE **inside five `{dropdown}` notes** (R-DROPDOWN rule 2): every
dense, quotation-heavy sentence was split only *before or after* a quotation, several
requiring the citing marker to be repeated on each resulting sentence since one
citation originally covered a whole compound sentence of parallel quoted clauses (declared
via `--allow-dropdown-edits`, `--allow-added markers`). R-TOOLS (2 "Strength:" bullets
→ SkyWater-says/Tool-exists/Runs-this-step form; no recap table, under the 4-tool
threshold), R-RELATED (labelled: `Previous:`, `Next:`, `Feeds:` ×2, `Same category:`),
R-OPENQ (bold labels on all five bullets), R-GLANCE (box inserted last).

**One R-HEDGE mistake caught by the measurement tool, not a reviewer.** The first edit
pass wrapped *both* sentences of the "How it is typically performed" intro in italics
("*An industry-generic ONO sequence…not public). The published values come from…in the
text:*"), when R-HEDGE step 1 only calls for the true scope sentence (the first one) to
become an italic lead-in. `measure5.py`'s sentence splitter, which requires a bare
`.`/`!`/`?` (optionally followed by a closing quote/bracket) before whitespace, does not
recognise a sentence boundary immediately before a closing `*`, so the over-wrapped
version silently merged into one 57-word "sentence" in the tool's own count. Re-reading
the source against R-HEDGE's own wording (`the existing opening scope sentence, **word
for word**`) showed the mistake before any checker was declared passing; fixed by closing
the italics after the first sentence only. Recorded as a caution for later pages: an
italic lead-in must end where the *scope sentence itself* ends, never absorb the
sentence after it.

**One in-force number nearly leaked into the glance box — caught by `check_inforce.py`,
fixed before commit.** The first glance-box draft cited `[^pat-02]` (US 2009/0179253, one
of this page's *in-force* patents) for the tunnel/trapping/blocking-oxide ranges quoted
inside the collapsed dropdown at the top of "What this step is" — exactly the mistake
the task brief warns against twice over ("never put anything from those notes in a
glance box"). `uv run python tools/check_inforce.py` failed immediately with `footnote
reference [^pat-02] ... outside a collapsed block`. Fixed by rewriting "Public numbers"
to cite only `[^pat-01]`, the *expired* Cypress ONO patent whose figures ("less than
about 25 Å" tunnel, "less than about 200 Å" trapping) are already quoted in the open
body text, not only inside a dropdown. Re-ran `check_inforce.py`: 0 problems. This is
the clearest instance in this batch of the exact trap the task brief calls out; recorded
in full because a future page's glance box must always be checked against
`check_inforce.py` before considering the page done, not just against `check_preserved.py`.

Caps before → after (`measure5.py`): paragraphs > 100 words 4 → 1 (figure caption, off
limits); list items > 60 words 0 → 0; sentences > 45 words 10 → 0; table cells > 25
words 0 → 0.

`uv run python tools/check_preserved.py --base 4a4ed3cf --allow-added
markers,numbers,hedges,identifiers,number_order,quotes --allow-regrouped
--allow-dropdown-edits docs/steps/040-ono.md`: **0 undeclared differences** after two
rounds of fixes. The first round found a real `LOST quotes` / `ADDED quotes` pair: an
early edit had moved a sentence-ending period from *outside* a closing quotation mark to
*inside* it ("...layer."[^cyp-25]" instead of the source's "...layer".[^cyp-25]"), which
is a forbidden change to the quotation's own content, not punctuation around it. Grepped
the whole batch (`grep -n '\."\[\^' docs/steps/035…047*.md`) to confirm no other page has
the same slip, then fixed this one occurrence. `quotes` added by the glance box (repeating
text already quoted in the body) are declared; every `number_order` finding is a clean
`REGROUPED` match except the glance box's own declared addition. All other checkers,
`check_inforce.py` above all, pass; `-W` build clean. Screenshots (desktop + 400 px) read
cleanly top to bottom, all five dropdowns collapsed and untouched, the new Step-category
bullets and the R-TOOLS blocks render correctly.


### 039-tunme.md — done (3 hand-written in-force notes in the body, plus their copies
under References; content untouched, sentences split inside them under R-DROPDOWN
rule 2 — inside the 037–044 in-force-sweep range)

Rules applied: R-PARA/R-SENTENCE throughout the open prose (lead split into 2
paragraphs; the "Step category" classification sentence + `**Specific to this
step:**` and 2 bullets; the "Three things follow" intro sentence split into 3; both
long "Why this step exists" bullets split into lead + continuation; the "Without
`TUNME`..." sentence split at its em-dash into 3 shorter sentences; both dense
"How it is typically performed" items (1 and 5) split into lead + continuation, with
item 2's internal semicolon split and its `(tunm.3)` parenthetical folded into plain
text to keep the em-dash-aside sentence at one parenthetical), R-SENTENCE **inside
three `{dropdown}` notes** (R-DROPDOWN rule 2 explicitly allows this): each dense,
quotation-heavy sentence was split only *before or after* a quotation, never inside
one, and no word or quotation mark was changed — see the "dropdown edits" list below
for the exact before/after text of each. R-HEDGE step 1 (italic lead-in), R-TOOLS (4
"Strength:" bullets → SkyWater-says/Tool-exists/Runs-this-step form + a `Tool |
Evidence` recap table, since 4 meets the rule 5 threshold), R-RELATED (labelled and
reordered: `Previous:`, `Next:`, `Same category:`, `Depends on:`, `Mask:`, `Category
pages:`), R-OPENQ (bold labels on all four bullets), R-GLANCE (box inserted last;
"Public numbers" is "none published for SKY130" since every number on the page either
belongs to a patent inside a dropdown or to a comparison step).

**Dropdown edits (`--allow-dropdown-edits`), named per §7 step 4:**

1. Body dropdown "From a patent shown as in force (US 8,796,098; estimated expiry
   2034-02-26) — open to read" (the one right after the lead). Old: one 68-word
   sentence running "The Cypress embedded-SONOS patent describes exactly this
   operation on the way to its tunnel dielectric: a "...209", the memory-transistor
   channel is implanted "...tunnel mask", and then "The pad oxide 209 is
   removed,...chemistry."" New: the same clauses and quotations, split into three
   sentences at the two points between quotations ("...pad oxide 209"." /
   "...tunnel mask". Then, "The pad oxide..." /  the "and then" connective replaced
   by "Then,"). No quotation altered; no word added or removed.
2. Body dropdown "From patents shown as in force (US 2009/0179253 …) — open to read"
   under "Why this step exists". Old: "...so that "between 1.5 nm and 2.5 nm of
   silicon dioxide may be removed" over a flow's worth of implants." joined to the
   previous quotations by "so that". New: split into two sentences at "so that" →
   "so that" capitalised to "So that", nothing else changed.
3. The same dropdown, repeated under "How it is typically performed": old "...H₂O at
   about 50 to 80° C.", and one of them replaces SC-1 with..."; new: split at "and
   one of them replaces" into two sentences ("...80° C.[^pat-04] One of them
   replaces...").

Caps before → after (`measure5.py`): paragraphs > 100 words 4 → 1 (figure caption,
off limits); list items > 60 words 3 → 0; sentences > 45 words 11 → 1 (same figure
caption); table cells > 25 words 0 → 0.

`uv run python tools/check_preserved.py --base 4a4ed3cf --allow-added
markers,numbers,hedges,identifiers --allow-regrouped --allow-dropdown-edits
docs/steps/039-tunme.md`: **0 undeclared differences**. Every `number_order` finding
is a clean `REGROUPED` match, including the three dropdown splits above (each
quotation's own digits stayed in their original relative order). All other checkers
(including `check_inforce.py`, run explicitly given the patent-sensitive dropdowns)
pass; `-W` build clean. Screenshots (desktop + 400 px) read cleanly top to bottom,
including all three dropdowns (collapsed, title unchanged) and the new recap table.


### 038-depi.md — done (1 hand-written in-force note under "How it is typically
performed" and its copy under References; both untouched — inside the 037–044
in-force-sweep range)

The densest page in the batch so far: a 300-word "Why this step exists" paragraph
mixing three device families' measured thresholds and body-effect coefficients.

Rules applied: R-PARA/R-SENTENCE throughout (the lead split at its
mechanism/drawing-label seam; the buried-channel paragraph's 53-word sentence split at
its em-dash; the read-condition paragraph split into 3 shorter paragraphs at its own
seams, each long sentence further split at its em-dashes/colons; the trapped-charge and
native-device paragraphs each split in two at natural seams; the 300-word measured-data
paragraph split into 4 paragraphs with 2 new bold run-in labels, **Measured
thresholds.** and **Body-effect coefficients.**, matching the "Relation to the native
devices." label already on the page), R-TOOLS (2 "Strength:" bullets split into
SkyWater-says/Tool-exists/Runs-this-step form; no recap table), R-HEDGE step 1 (italic
lead-in), R-RELATED (labelled and reordered: `Previous:`, `Next:`, `Same category:` ×2,
`Mask:`, `Category page:`), R-OPENQ (bold labels on all four bullets), R-GLANCE (box
inserted last; "Public numbers" is "none published for SKY130", since the page's only
SKY130-specific numbers belong to the native/zero-Vt comparison devices, not `DEPI`
itself).

**Two sentences deliberately left over the 45-word cap, not a miss.** The
"**Measured thresholds.**" sentence (121 words) and the "**Body-effect
coefficients.**" sentence (70 words) each carry a single "(our extraction from the
published measurements)"-type hedge that covers threshold or body-effect values for
*three different device families* named later in the same sentence. Splitting either
sentence at any of its internal semicolons would separate at least one device's
number from the hedge that supports it — exactly the mistake the task brief warns
against twice over (marker/hedge must travel with every resulting clause, and this
project's own precedent, batch 2's pages 022–024, treats this "which value belongs to
which device" pairing risk as a reason to keep dense measured-comparison prose intact
rather than force a split or a table). Both sentences were left as originally
written; only the paragraph around them was split. Recorded here per §7's "write it in
the progress file, do not force a fix" instruction.

**One checker-parsing artifact found and avoided, not a real preservation issue.**
Reformatting "Native devices: see {ref}`LVTNM <step-014>` for the `lvtn` block layer."
to "Same category: native devices — see {ref}`LVTNM <step-014>` for the\n  `lvtn`
block layer." (a plain rewording, wrapped onto two lines by the editor) produced a
`LOST refs` / `ADDED refs` pair in `check_preserved.py` even though the `{ref}` role
and the `` `lvtn` `` code span are byte-identical to the source. Root cause (read from
`tools/check_preserved.py`'s own `_mask_inline_code`/`_CODE_SPAN_SINGLE_RE`, not
changed): the single-backtick code-span masker only refuses to swallow a role's own
*opening* backtick, and its content class excludes newlines, so in the base commit —
where "for the" and `` `lvtn` `` sat on the same line — a stray, incorrect code-span
match already bridged the ref's closing backtick through "for the" to `lvtn`'s
opening backtick, mis-parsing the ref's target as `LVTNM <step-014> for the lvtn`.
Wrapping the same two spans onto separate lines put a newline inside that bridge,
which the masker's content class forbids, so the mis-parse silently stopped happening
and `check_preserved` reported it as a changed ref. Fixed by keeping "for the" and
`` `lvtn` `` on one line (no rewording change, just no new line break at that exact
point) — restores the original, if quirky, tokenisation so the diff shows nothing.
Recorded as **Guide problem 15**: a `{ref}`X`` role followed later on the *same
source line* by an unrelated inline-code span, with nothing between them but the
role's own closing backtick and plain words, can be mis-tokenised by
`check_preserved.py`'s code-span masker; rewrapping the line (even with no wording
change) can silently change which mis-parse happens and show up as a false
`LOST`/`ADDED refs` pair. Not a real content difference; the checker is off limits to
edit (§2 rule 15), so future pages should keep this exact line-wrapping relationship
undisturbed rather than "fix" the tokenisation by accident.

Caps before → after (`measure5.py`): paragraphs > 100 words 6 → 1 (figure caption,
off limits); list items > 60 words 2 → 0; sentences > 45 words 7 → 2 (the two
deliberately-unsplit measured-data sentences above, plus the figure caption no longer
counted separately since it wasn't a SENT hit this time); table cells > 25 words 0 → 0.

`uv run python tools/check_preserved.py --base 4a4ed3cf --allow-added
markers,numbers,hedges,identifiers --allow-regrouped docs/steps/038-depi.md`: **0
undeclared differences** after the line-wrap fix above. All `number_order` findings are
clean `REGROUPED` matches. All other checkers pass; `-W` build clean. Screenshots
(desktop + 400 px) read cleanly top to bottom, including the two new bold-labelled
measurement paragraphs (both readable in one screen-width, no overflow) and the
in-force dropdown (collapsed, untouched).


### 037-ptsi.md — done (1 hand-written in-force note under "How it is typically
performed" and its copy under References; both untouched — this page is inside the
037–044 in-force sweep range, checked with `check_inforce.py` after every edit)

Rules applied: R-PARA/R-SENTENCE throughout (the lead split into 3 short paragraphs at
its definition/inference/mechanism seams; the mask/screen-oxide paragraph split at its
"everywhere else"/"block reading" seam, each long sentence itself split further —
em-dash pairs converted to plain sentence breaks or commas where a second parenthetical
would otherwise push a sentence over the 0–1 dash-or-parenthetical cap; the
punch-through/ITRS paragraph split in two; all three "Why this step exists" bullets
split into lead + indented continuation, including turning one over-length
parenthetical into its own sentence per the ≥12-word rule; both "How it is typically
performed" items (Species, Energy) split the same way), R-CATEGORY (35-word
classification sentence + `**Specific to this step:**` and 2 bullets, since 2 sentences
remained), R-HEDGE step 1 (italic lead-in), R-TOOLS (2 "Strength:" bullets split into
SkyWater-says/Tool-exists/Runs-this-step form; no recap table), R-RELATED (labelled and
reordered: `Previous:`, `Next:`, `Same category:` ×2, `Feeds:`, `Mask:`, `Category
page:`), R-OPENQ (bold labels on all four bullets), R-GLANCE (box inserted last; "Public
numbers" is "none published for SKY130" since every number on the page belongs to a
comparison device, a literature citation, or the in-force dropdown).

Caps before → after (`measure5.py`): paragraphs > 100 words 4 → 0 (figure caption
excepted, off limits); list items > 60 words 4 → 0; sentences > 45 words 8 → 0; table
cells > 25 words 0 → 0.

`uv run python tools/check_preserved.py --base 4a4ed3cf --allow-added
markers,numbers,hedges,identifiers --allow-regrouped docs/steps/037-ptsi.md`: **0
undeclared differences**. Every `number_order` finding is a clean `REGROUPED` match (the
splits landed cleanly, unlike 035's table-reordering case) — spot-checked the
programme/erase-voltage tuple and the e-test W/L tuple by eye against the diff, both
match digit-for-digit. Declared additions are the glance box's own marker/hedge/identifier
repeats. All other checkers pass; `-W` build clean. Screenshots (desktop + 400 px) read
cleanly top to bottom, including the in-force dropdown (collapsed, untouched) and the new
Step-category bullets.


### 036-tunarce.md — done (1 hand-written in-force note in the body, plus its copy under
References; both untouched)

Rules applied: R-PARA/R-SENTENCE throughout (the lead split at its
definition/mechanism/consequence seams, and the semicolon inside its second sentence split
into two; the "industry-generic form" paragraph split at its resist-in-place/plasma-exposure
seam; both "Why this step exists" bullets split into lead + indented continuation at their
own seams; the "Chemistry" and "Selectivity" items split into lead + indented continuation),
R-HEDGE step 1 (italic lead-in on the "How it is typically performed" scope sentence — same
missing-heading slip as 035 happened again on the first pass and was caught the same way, by
`check_steps.py`, before any checker was declared passing), R-TOOLS (3 "Strength:" bullets
split into SkyWater-says/Tool-exists/Runs-this-step form; 3 tools, under the 4-tool
threshold, so no recap table), R-RELATED (`Same category:` label added to the FOM pointer
bullet), R-OPENQ (bold labels added to all four bullets), R-GLANCE (box inserted last;
"Public numbers" is "none published for SKY130" since every number on this page is either a
category-page generality or lives inside the in-force dropdown).

Caps before → after (`measure5.py`): paragraphs > 100 words 3 → 0 (figure caption
excepted, off limits); list items > 60 words 4 → 0; sentences > 45 words 5 → 0; table cells >
25 words 0 → 0.

`uv run python tools/check_preserved.py --base 4a4ed3cf --allow-added
markers,hedges,identifiers --allow-regrouped docs/steps/036-tunarce.md`: **0 undeclared
differences** — the cleanest page so far. Declared additions are exactly the glance box's own
marker (`skw-01`, repeating the first R-TOOLS item's grade) and its template words
("inference", "not public", the bare word "SKY130" in "none published for SKY130"). All other
checkers pass; `-W` build clean. Screenshots (desktop + 400 px) read cleanly top to bottom,
including both hand-written in-force dropdowns (title, body and the copy under References all
byte-identical to the source, confirmed by the preservation check's `dropdown` category
showing no finding).


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
