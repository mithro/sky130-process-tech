# Progress — `topic/rd-masks-a` (W3 masks, pages 1–18)

Readability pass over the first eighteen mask pages in file-name order
(`ls docs/masks/*.md | grep -v index | head -18`): cap2m, capm, ctm1, dnm, fom, hvntm, hvtpm, ldntm,
li1m, licm1, lvom, lvtnm, mm1, mm2, mm3, mm4, mm5, npcm. Rules per `docs/plans/readability-guide.md`
§4.4, in its order: R-INTRO → R-PARAMS → R-CAPTION → prose rules (R-PARA, R-SENTENCE, R-LIST,
R-REPEAT, R-CODE) → R-RELATED → R-H3. Base for every page: `c79af95b` (main when the branch was cut).

## Method, the same on every page

* **Preservation.** `uv run python tools/check_preserved.py --base c79af95b --allow-regrouped <page>`,
  every ADDED item read and listed per page below; `--allow-added` is given only the categories named
  there, never `--allow-dropdown-edits`.
* **Marker coverage.** `tmp/readability/markcov.py c79af95b <page>` (git-ignored scratch script): maps
  every changed sentence to its source sentence and flags a piece of ≥ 6 words that lost the marker
  its source had (NOMARK), a hedge phrase that no piece keeps (HEDGE) and a hedge phrase a piece gained
  (NEWHEDGE). Every flag is read by eye; the per-page entry says which were real.
* **Checkers.** check_masks, check_refs, check_inforce, gen_index_links --check, gen_figures --check,
  `-W` build; desktop and 400 px tiles before and after.
* **Measurement.** `docs/plans/readability/prototypes/measure/measure5.py` (copied to
  `tmp/readability/a-tools/`) at the §1 caps: paragraph > 100 words, list item > 60, sentence > 45,
  cell > 25.

## Decisions taken on this branch (same on every page)

* **Intro (R-INTRO).** The intro keeps the first sentences that say what the mask is and what it does,
  ≤ 70 words. The pointer sentence ("How the step is performed is on the step page; every mask is
  indexed on the masks index.") moves word for word into a `{seealso}` under the quick facts. The
  sentence listing the page's own sections ("This page gathers what public sources say about the mask
  itself — its PDK entry and layers, …") is deleted; it is pasted per page below. Every other intro
  sentence moves, unchanged apart from "it" → "the mask" where it would open the section, to the top
  of `## What the mask defines`, as the machine batch did (`duv-krf-stepper.md`).
* **H3s (R-H3, B8).** Every bold run-in under `## Lithography and pattern transfer` becomes an H3 with
  its own words, except the true synonyms the checker names: `Resist` → `Resist and tone`, `Overlay`
  and `Alignment` → `Overlay and alignment`. A run-in that is not one of the five canonical names keeps
  its words (for example "Mask errors and the plate", "Reflective substrate"). Run-ins under other H2s
  stay bold (the checker forbids H3s there).
* **Order of the overlay passage.** `check_masks.py` requires the canonical H3s in canonical order
  (…, Overlay and alignment, Pattern transfer). On pages where the overlay passage followed the pattern
  transfer passage, the overlay passage (heading plus its paragraphs, unchanged) moves above the pattern
  transfer passage, inside the same H2. See guide problem G1.
* **Lists (R-LIST).** Items that are full sentences beginning with their own subject become plain
  bullets without an invented bold label (the batch-3 review's remark on invented labels); a trailing
  "and" before the last item is dropped, and a trailing semicolon becomes a full stop.
* **Split sentences (R-SENTENCE 5).** A marker or a hedge that covered a whole split sentence is repeated
  on each piece that carries its claim; a marker that belonged only to one clause stays with that
  clause. A sentence over 45 words whose only split would need new words beyond a subject and a verb is
  left as it is and listed.
* **Related pages (R-RELATED).** Grouped under **Category.** · **Machines.** · **Materials.** ·
  **Masks.** · **Indexes.**, links, link text and glosses unchanged. The class-page label set has no
  label for step links, so the mask page's step bullet(s) stay first and unlabelled (guide problem G2).
  Glosses are not shortened.
* **Captions (R-CAPTION).** Every non-quick-facts table except the checked plate table gets a
  `:::{table}` caption with no `:widths:`. The plate table (`| Run | Reticle set … |`) is left bare: it
  is checker-read and §4.4 says to leave it alone.
* **Renders.** Report B17's decision "render link, not thumbnail": each page already links the renders
  from its Cross-check reading list; nothing is added.

## Guide problems

* **G1.** R-H3 step 2 says passages stay "in their own order", but `check_masks.py` requires the
  canonical H3s in canonical order, and on almost every page the overlay passage follows the pattern
  transfer passage. Moving it (within the same H2, unchanged) was the only way to satisfy both B8's
  synonym merge (`Overlay` is rejected) and the checker.
* **G2.** R-RELATED step 2's class-page labels (Category · Machines · Materials · Masks · Indexes) have
  none for step links, which every mask page's Related pages starts with.

## Pages

### 1. cap2m — done

* **Rules applied.** R-INTRO (intro 215 → 58 words; first sentence split at its colon); R-CAPTION (rule
  table); R-PARA and R-SENTENCE throughout; R-LIST ("What the PDK does not publish" — four sentence
  bullets; the test-tile structures — seven fragment bullets, the closing marker moved to the lead-in
  per R-LIST 1; the three rules the design-rule table covers); R-RELATED; R-H3 (six H3s under
  Lithography: Exposure class, Mask errors and the plate, Stacked plates, Reflective substrate, Pattern
  transfer, Overlay and charging — none is a synonym of a canonical name except Exposure class and
  Pattern transfer, so no reordering was needed).
* **R-PARAMS not applied:** the design-rules paragraph names three parameters (`CAPMCD`, `CAPMCDSP`,
  `MiM_AR`), below the rule's four.
* **Deleted template sentence (R-INTRO 3):** "This page gathers what public sources say about the mask
  itself — its PDK entry and layers, the plates the process-steps sheet records for the MPW runs, what
  the public renders of those runs show, the lithography it needs and the rules that constrain it."
  It is the cause of `LOST hedges: 'about'` (the preposition). Nothing else in it.
* **Moved:** "Less is public about it … a single shape." (intro) → top of `## What the mask defines`,
  "it" → "the mask"; the pointer sentence → `{seealso}`.
* **Declared additions** (`--allow-added markers,identifiers`), each a repeat on a split sentence
  (R-SENTENCE 5) or a pronoun given its noun back:
  * `pdk-07` ×3 — the *Device Details* sentence split in three (constructions / cell and model / area
    and periphery capacitance), each piece quoting or citing that page;
  * `pdk-06` — the `gds_layers.csv` sentence split at its semicolon;
  * `pdk-errors` ×2 — the *Error Messages* sentence split in three;
  * `mask-renders` — the render sentence split at its semicolon (the first half is about the renders
    only, so it takes `mask-renders` and not `steps-sheet`);
  * `steps-sheet` ×3, `pdk-05` — "Plate number" continuation (`steps-sheet`, with "(our comparison)"
    repeated — a hedge the tool does not count), "A plate without a PDK entry" (`steps-sheet`,
    `pdk-05`), the second Open question (`steps-sheet`);
  * `pdk-10` — the second Open question split at its semicolon; its first half is the README claim.
    The first half takes `steps-sheet` and `pdk-10` only: `mask-renders` supports the renders clause,
    which is in the second half and keeps all three;
  * identifier `cap2m` — "does name it" → "does name `cap2m`" (pronoun given its noun back).
* **Marker coverage (markcov).** Flags read: the seven test-tile items (marker on the lead-in, R-LIST 1);
  "The i-line stepper page lists it there", "At 365 nm …", "A misregistration …", "The step page reads
  this as …" — each clause had no marker of its own in the base (the marker belonged to the preceding
  clause). A split of "Plates of this size … (our reading): a laser writer …" was reverted: the reading
  would have lost the evidence that follows its colon.
* **Over the caps after the pass:** "The CAP2M page gives {math}`k_1 …`" (52 by the script, which counts
  the formula as several words; about 35 with it as one); "Plates of this size …" (49; see above); the
  quick-facts Exposure class cell (26 words; its words are not in the body, so R-QUICKFACTS 2 cannot
  shorten it). Before → after: paragraphs > 100 words 11 → 0, list items > 60 1 → 0, sentences > 45
  17 → 2, cells > 25 1 → 1.
* **Open question 1** keeps its markers where the base had them: the split is at its semicolon only, so
  `pdk-05`, `pdk-03`, `pdk-periph` and `pdk-07` stay after "construction" as before.
* **Content problems for the owner:** none found.
