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
  22 → 2, cells > 25 1 → 1.
* **Open question 1** keeps its markers where the base had them: the split is at its semicolon only, so
  `pdk-05`, `pdk-03`, `pdk-periph` and `pdk-07` stay after "construction" as before.
* **Content problems for the owner:** none found.

### 2. capm — done

* **Rules applied.** R-INTRO (intro 195 → 54 words; first sentence split at its colon; "It is a device
  mask …" and "Its public record is uneven …" moved to the top of `## What the mask defines`, "It" →
  "The mask"); R-CAPTION (rule table); R-PARA, R-SENTENCE; R-LIST (test-tile structures, five fragment
  bullets, closing marker on the lead-in); R-RELATED; R-H3 (Exposure class, Mask errors and the plate,
  Why the plate CD matters, Reflective substrate, Pattern transfer, Overlay and charging — no canonical
  order conflict).
* **R-PARAMS not applied:** three parameters (`CAPMCD`, `CAPMCDSP`, `MiM_AR`).
* **Deleted template sentence:** the same "This page gathers what public sources say about the mask
  itself — …" sentence as on cap2m, word for word. `LOST hedges: 'about'` is its preposition.
* **Declared additions** (`--allow-added markers`), all repeats on split sentences: `pdk-periph` (the
  function / twelve-rules sentence; "and publish" → "They publish"), `pdk-errors` (*Error Messages*
  sentence), `pdk-07` (*Device Details* sentence; "it gives" → "The page gives"), `pdk-06` ×3 (Table C3 /
  C4b / F2b / "In that row" — the base sentence carried one `pdk-06` at its end), `mask-renders` (render
  sentence), `pdk-05` and `steps-sheet` ("A plate for an unmarked entry" split at its semicolon), a
  second `steps-sheet` with "(our comparison)" ("Plate number"), `pdk-03` (Table 2 / Table 7 sentence
  split at its semicolon).
* **Marker coverage.** Flags read; all are clauses that had no marker of their own in the base, or the
  test-tile items under a lead-in marker.
* **Over the caps after the pass (5):** the formula sentence under Exposure class (50 by the script);
  "At 4× a 2 µm plate is 8 µm on the reticle … sizing the data" (63: the reading and its evidence are
  one sentence joined by a colon; a split would strand the reading, as on cap2m); "The step page puts a
  0.1 µm bias …" (46, the script counts "40 µm × 40 µm" as five words); "For the plate the decisive
  published figures …" (47; splitting it would need "The plate is", which turns a figure into a claim
  about the plate); the quick-facts Exposure class cell (34; its words are not in the body) and the
  x.22 rule-text cell (26, a quotation). Before → after: paragraphs 12 → 0, items 2 → 0, sentences
  20 → 4, cells 2 → 2.
* **Content problems for the owner:** none found.

### 3. ctm1 — done

* **Rules applied.** R-INTRO (162 → 57 words; first sentence split at its colon; "It is the first mask of
  the BEOL …" moved to the top of `## What the mask defines`, "It" → "The mask"); R-PARAMS (new table
  after the rule table, see below); R-CAPTION (rule table, parameter table); R-PARA, R-SENTENCE;
  R-LIST (the step page's hole-printing toolkit: Lu, Fukuda, Socha as three sentence bullets under the
  base's own lead-in); R-RELATED; R-H3 (Exposure class, Mask errors, Defects on the plate, Drawn and final
  size, Resist and tone, Overlay and alignment, Pattern transfer).
* **Moved passage (G1):** "**Overlay.** The contact needs no enclosure …" followed "**Pattern transfer.**";
  it now sits, unchanged, under `### Overlay and alignment` before `### Pattern transfer`. Neither
  passage refers to the other.
* **R-PARAMS.** "Table 2 … repeats the size and space as `CTM1CD` 0.17 and `CTM1CDSP` 0.19; Table 4 adds the
  `CEFC` 0.14 and `TCONOVLP` 0.12 above, a "Mcon enclosure by Li" of 0 (`mconLiEnclosure`) and a "Bowing
  …" of 0.015 (`TBOWINGSEAL`), which does not say which contact layer it means; Table 5 gives the 0.09
  bottom CD without a variable name.[^pdk-03]" became a lead-in ("*Criteria & Assumptions* repeats the
  size and space in Table 2 and adds contact criteria in Tables 4 and 5:[^pdk-03]"), a seven-row
  `Parameter | PDK table | Published description | Value` table, and the base's relative clause as its
  own sentence ("`TBOWINGSEAL` does not say which contact layer it means.[^pdk-03]"). The descriptions of
  `CEFC`, `TCONOVLP` and the Table 5 bottom CD are the page's own quotations of them from "In the PDK" and
  "Overlay" (the base said "above" instead): three ADDED quotes, each a copy of a quotation already on
  the page. The Table 2 descriptions are the base's unquoted "size" and "space"; the Table 5 parameter
  cell is the base's "without a variable name".
* **Deleted template sentence:** the "This page gathers what public sources say about the mask itself —
  …" sentence (same wording as cap2m). `LOST hedges: 'about'` is its preposition.
* **Declared additions** (`--allow-added markers,numbers,quotes,identifiers`):
  * markers — `mask-renders` ×2 and `steps-sheet` (render sentence and the renders/sheet-notes sentence
    split at their semicolons), `itrs-03` ("… from ITRS 2001.[^itrs-03] ITRS 2001 lists …"), `pdk-03` (the
    `TBOWINGSEAL` sentence);
  * numbers — `2` ×2, `4` ×4, `5` (the PDK-table column), `1` and `2` ("Rules ct.1 and ct.2 are the only
    rules …", the pronoun "they" given its noun back), `2001` ("ITRS 2001 lists", the relative "which"
    given its noun back);
  * quotes — the three described above;
  * identifier `metal-1` — the rule-table caption, copied from the sentence above the table.
* **LOST lines that are not losses (read by hand):**
  * `number_order` ('0.17' … '2001', '248', '193', '130', '248'): the Exposure-class sentence became two;
    the new page reads 0.17 0.70 0.248 0.48 0.7 248 2001 | 2001 248 193 130 248 — the same digits in the
    same order with the repeated "ITRS 2001" between them, which breaks the tool's contiguity test;
  * `number_order` ('2', '0.17', '0.19', '4', '0.14', '0.12', '0', '0.015', '5', '0.09'): the R-PARAMS table;
    values in row order 0.17, 0.19, 0.14, 0.12, 0, 0.015, 0.09 — the base's order — and the table numbers
    2, 2, 4, 4, 4, 4, 5 match the base's assignment of each value;
  * `refs` 'masks-renders-sheet-notes); both also call the VIM' → '…).[^steps-sheet][^mask-renders] Both
    also call the VIM': a tool artefact (its inline-code stripping pairs the backtick closing the role with
    the one opening `` `VIM` ``); the role is `{ref}`masks-renders-sheet-notes`` before and after, and the
    nitpicky build resolves it.
* **Marker coverage.** Flags read: every flagged piece is a clause with no marker of its own in the base,
  a toolkit lead-in, or a parameter row under the lead-in marker; the one real case (`TBOWINGSEAL`) was
  given its `pdk-03` back.
* **Over the caps after the pass:** the Exposure-class formula sentence (51 by the script); "On the step
  pages' readings the holes are etched …" (46; its second clause, "the next step, TIN2, lines the holes",
  sits inside "On the step pages' readings", so a split would drop the hedge from it); the flag-legend
  sentence (60 by the script, almost all of it seven quotations, which §1 counts as one word each); the
  quick-facts Exposure class cell (43; not in the body) and the ct.irdrop rule cell (31, quoted rule
  text). Before → after: paragraphs 10 → 0, items 0 → 0, sentences 14 → 3, cells 2 → 2.
* **Content problems for the owner:** none found.
