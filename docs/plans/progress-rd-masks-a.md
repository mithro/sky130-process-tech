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

* **G3.** R-PARAMS fixes four columns (`Parameter | PDK table | Published description | Value`), one of them
  prose, where §1 allows at most three columns when any holds prose. At 400 px the tables do not scroll,
  but a long code identifier (which does not wrap) widens the Parameter column and squeezes the
  description into one-word lines (`lvtnm.md`, `LvtEnc_forPowerRail`: about 12 lines). Merging
  "PDK table" into the Parameter cell (`` `LVTNMCD` (Table 2) ``) would fix it, but changes the rule's
  header, so it was not done.
* **G4.** B8 treats "Resist" and "Resist and tone" as true synonyms, and the checker rejects `### Resist`.
  On several implant pages the "Resist" passage says little about tone beyond "wherever the plate leaves
  it" (hvntm, ldntm) or "(on the positive-resist reading)" (dnm), so "Resist and tone" slightly
  overstates the passage (§8 item 11). Followed B8 and the checker.

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

### 4. dnm — done

* **Rules applied.** R-INTRO (137 → 51 words; first sentence split at its colon; "It is an implant block
  mask …[^pdk-03]" moved to the top of `## What the mask defines`, "It" → "The mask"); R-CAPTION (rule
  table); R-PARA, R-SENTENCE; R-LIST (the device pages' three uses of the isolation, marker on the
  lead-in; the 19 Table F2b rows as seven fragment bullets, marker on the lead-in — 1 + 1 + 2 + 1 + 5 +
  8 + 1 = 19, as the lead-in says); R-RELATED; R-H3 (Exposure class, Mask errors, Resist and tone ←
  "Resist", Overlay and alignment ← "Overlay", Pattern transfer).
* **Moved passage (G1):** the Overlay passage now precedes Pattern transfer, unchanged apart from the
  split below.
* **Overlay sentence (70 words) split at its em-dash pair (R-SENTENCE 1):** "The enclosures that depend on
  its placement are large — 0.400 µm … (nwell.6)[^pdk-periph] — against the "≤ 40 nm" …" → "The
  enclosures that depend on its placement are 0.400 µm … (nwell.6).[^pdk-periph] They are large against
  the "≤ 40 nm" …[^asml-pas5500-275d] (our comparison; …)." The values keep their marker, and "large …
  against" keeps the comparison and its hedge.
* **R-PARAMS not applied:** the design-rules paragraph names three parameters (`DNMCD`, `DNMCDSP`,
  `nwellDnwellSpc`); the "Three criteria" paragraph under In the PDK names three too.
* **Deleted template sentence:** "This page gathers what public sources say about the mask itself — its
  PDK entry and layers, the plates the process-steps sheet records for the MPW runs, what the public
  renders of those runs show, the lithography it needs and the rules that constrain it."
  (`LOST hedges: 'about'`).
* **Declared additions** (`--allow-added markers`): `mask-renders` ("… not 40 designs using the module.",
  split at its colon), `pdk-03` ×2 (Table 4 / Table 7 sentence; Table 2 / Table 4 sentence), `wong-1998`
  (the Wong sentence split before "and that dark-field spaces …", which becomes "Wong et al. found that
  dark-field spaces …": subject and verb repeated).
* **Marker coverage.** Only the two lists under lead-in markers were flagged.
* **Over the caps after the pass:** the x.15a sentence (46 by the script; two quotations) and the Wong
  sentence (46; one long quotation); the Polarity and tone cell (26; not in the body). Before → after:
  paragraphs 10 → 0, items 0 → 0, sentences 10 → 2, cells 1 → 1.
* **Content problems for the owner:** none found.

### 5. fom — done

* **Rules applied.** R-INTRO (164 → 48 words); R-PARAMS; R-CAPTION (rule table — the guide's own worked
  caption, with the page's words "blank in the published table"; parameter table); R-PARA,
  R-SENTENCE; R-LIST (Table F2b's `C` and `+` rows; the Table 4 pattern-density criteria; the two kinds
  of placement margin); R-RELATED; R-H3 (Exposure class, Mask errors, Pattern density, Resist and tone,
  Overlay and alignment ← "Alignment", Pattern transfer).
* **Intro split with a repeated hedge.** "On the FOM page's reading it is the first lithography of the
  flow: the resist printed through it stays … into the silicon." The first half stays in the intro; the
  second half opens `## What the mask defines` with the base's hedge repeated word for word ("On the
  {ref}`FOM <step-004>` page's reading, the resist printed through the mask stays …"; "it" → "the
  mask"). That repeat is the ADDED ref `step-004`. "Because nothing is on the wafer before it …" moved
  with it.
* **Moved passage (G1):** the Alignment passage (now `### Overlay and alignment`) moved above Pattern
  transfer. It refers to the trenches and the alignment marks, not to the pattern-transfer paragraph.
* **R-PARAMS.** The seven parameters of "Table 2 … `FOMCD` 0.14 … (`FOMSESC`);[^pdk-03] the PDK does not
  reconcile these … Table 3c … (`MINFWR`) … (`SDM3`), and Table 4 a … (`DEFC`).[^pdk-03]" are one table
  (the guide's R-PARAMS example). The two markers stay at the ends of their groups (the `FOMSESC` and
  `DEFC` value cells), so each still closes the rows its sentence covered. "the PDK does not reconcile
  these" follows the table as "The PDK does not reconcile the Table 2 and Table 7 values …": the pronoun
  given its noun back, so that it still means the four values it meant and not all seven rows. The
  descriptions are the page's words: quoted where it quoted ("MOSFET width" …), unquoted where it
  paraphrased ("minimum feature", "minimum space").
* **Deleted template sentence:** the "This page gathers …" sentence (same wording as cap2m;
  `LOST hedges: 'about'`).
* **Declared additions** (`--allow-added markers,numbers,refs`): markers `mask-renders` ×2 (render sentence;
  "… how many projects draw active area.", split at its colon), `pdk-errors` (*Error Messages*
  sentence), `steps-sheet` ("Plate number": its dash pair became a colon and a full stop);
  numbers — the PDK-table column (`2`, `7`, `3` from "3c") and "the Table 2 and Table 7 values", and `4`,
  `5` from difftap.4/difftap.5 in the rule-table caption; ref `step-004` (the repeated hedge above).
  Markers moved to their own clause, not added: the Table C3 / x.15a sentence ended
  `[^pdk-06][^pdk-periph]`; split, the C3 half takes `pdk-06` and the x.15a half `pdk-periph`.
* **LOST `number_order` (read by hand):** ('2', '0.14', '0.27', '7', '0.135', '0.075', '0.150', '1') and
  ('3', '0.12', '0.34', '4', '0.15') — the R-PARAMS table. The values run 0.14, 0.27, 0.135, 0.075, 0.12,
  0.34, 0.15 down the rows as in the base; each value's PDK table matches the base; the reconcile sentence
  (0.150, difftap.1) follows the table, as R-PARAMS 3 asks.
* **Marker coverage.** Flags read: lists and table rows under their lead-in or group-final markers; the
  reconcile sentence had no marker of its own in the base.
* **Over the caps after the pass:** the Exposure-class formula sentence (47 by the script); three
  quick-facts cells (Drawn layer 38 — checker-compared; Polarity and tone 41 and Exposure class 34, not in
  the body). Before → after: paragraphs 11 → 0, items 0 → 0, sentences 16 → 1, cells 3 → 3.
* **Content problems for the owner:** none found.

### 6. hvntm — done

* **Rules applied.** R-INTRO (191 → 67 words; first sentence split at its colon; "It is an implant block
  mask … the openings themselves." moved to the top of `## What the mask defines`, "It" → "The mask");
  R-CAPTION (rule table, with the page's unit caveat for hvntm.7); R-PARA, R-SENTENCE; R-LIST (the
  three `hvi` rules, marker pair moved to the lead-in; Table F2b's 12 `C` rows as seven fragment bullets,
  1 + 1 + 1 + 2 + 1 + 4 + 2 = 12; the eight `chvntm` checks plus the `chvntm.nikon` pair; the per-die
  counts; the Table 3f/4/8 tilt criteria; the "other criteria … quoted above"); R-RELATED; R-H3 (Exposure
  class, Mask errors, Resist and tone ← "Resist", Resist edges and shadowing, Overlay and alignment ←
  "Overlay", Pattern transfer).
* **Moved passage (G1):** Overlay above Pattern transfer.
* **R-PARAMS as a list, not a table.** The design-rules paragraph names two parameters with identifiers
  (`HVNTMCD`, `HVNTMCDSP`) and then re-lists, by table and description, eight criteria "quoted above"
  without their identifiers. A `Parameter` column would have to copy the identifiers from above (or be
  `—` in most rows), and "those quoted above" would be lost, so the enumeration became an R-LIST under
  the base's own lead-in; the "NTM shadowing" and "HV MOSFET channel length" sentences stay prose.
* **Wording added (all subject/verb or noun-for-pronoun):** "Table 4 gives", "Table 8 gives" in the
  tilt-criteria list (the base elided the verb); "It is kept out of the SRAM core" → "`hvntm` is kept out
  …", "It marks" → "The table marks", "It does not define" → "The page does not define" (each after a
  new list, where "It" would point at the list); "On the step pages' readings" repeated on the NTM
  sentence split off the `hvi`/P1M sentence (the base hedge covered both halves).
* **Deleted template sentence:** the "This page gathers …" sentence (same wording as cap2m;
  `LOST hedges: 'about'`).
* **Declared additions** (`--allow-added markers,numbers`): markers `pdk-06` (`gds_layers.csv` sentence),
  `pdk-errors` (*Error Messages* description), `mask-renders` (README / expression sentence split at its
  colon), `pdk-03` (the "quoted above" lead-in; the base's one `pdk-03` stays on the "NTM shadowing"
  sentence it ended); numbers `7` ×2 and `15` (x.7, hvntm.7, x.15a in the rule-table caption).
* **Marker coverage.** Flags read: list items under lead-in markers; clauses that had no marker of their
  own in the base (the LATID reading, "The step page treats it …", "That fits a reading of CL …", the
  thin-film reading, the alignment reading, the first Open question's first half).
* **Over the caps after the pass:** the intro's second sentence (53: its three clauses all sit inside
  "On the HVNTM page's reading"; a split would drop the hedge from two of them); the Pattern transfer
  sentence (46, one hedge over the whole); the Polarity and tone cell (60; not in the body). Before →
  after: paragraphs 11 → 0, items 0 → 0, sentences 20 → 2, cells 1 → 1.
* **Content problems for the owner:** none found.

### 7. hvtpm — done

* **Rules applied.** R-INTRO (186 → 70 words; first sentence split at its colon; "The public record
  disagrees …" moved to the top of `## What the mask defines`, its colon made a full stop); R-CAPTION;
  R-PARA, R-SENTENCE; R-LIST (Table F2b's `C` rows; the four `chvtpm` checks; the per-die counts);
  R-RELATED; R-H3 (Exposure class, Mask errors, Resist and tone ← "Resist", Resist edges, Overlay and
  alignment ← "Overlay", Pattern transfer).
* **Moved passage (G1):** Overlay above Pattern transfer.
* **R-PARAMS not applied:** the design-rules paragraph names two parameters.
* **Hedge repeated on a split (R-SENTENCE 5):** "On the table, then, the standard 1.8 V PMOS receives
  created `HVTPM` shapes and the low-Vt PMOS does not, and the three … flavours differ … (… our reading
  of the rows).[^pdk-06]" — the hedge and marker ended the whole sentence, so both halves now carry
  "(our reading of the rows)" and `pdk-06` (ADDED hedge `our reading`, ADDED marker `pdk-06`).
* **Markers moved to their own clause:** the `HVTRM` sentence ended `[^pdk-05][^pdk-06][^pdk-periph]`
  after "… folded into this mask". Split at its semicolon, the three markers stay with the half that
  holds the `masks.csv`, `gds_layers.csv` and hvtr.2 facts; the second half ("The step list used in this
  reference has no mask step for it, and the HVTPM page leaves open …") names none of those sources and
  is left without a marker, rather than citing the PDK for the step list. The reviewer may prefer the
  markers repeated on both halves; that is a one-line change.
* **Deleted template sentence:** the "This page gathers …" sentence (same wording as cap2m;
  `LOST hedges: 'about'`).
* **Declared additions** (`--allow-added markers,hedges`): `pdk-06` and `our reading` (above);
  `pdk-errors` ×2 (*Error Messages* description; the lead-in of the four-check list — the base's marker
  stays on the `hvtp.c1` / nikon sentence it ended); `mask-renders` (README sentence split at its colon);
  `steps-sheet` ("Plate number" lead, split at its dash pair).
* **Marker coverage.** Flags read: lists under lead-in markers; clauses without a marker of their own in
  the base; the `HVTRM` second half (above).
* **Over the caps after the pass:** "Kao and Chandrakasan … (our reading)" (54: the trailing "— the kind
  of trade … (our reading)" may qualify both studies, so a split could narrow the hedge to one); "On that
  reading the PDK requires …" (48: one hedged reading ending in a dash clause); the AMD-patent sentence
  (52, mostly one quotation); the Polarity and tone cell (48; not in the body). Before → after:
  paragraphs 10 → 0, items 2 → 0, sentences 16 → 3, cells 1 → 1.
* **Content problems for the owner:** none found.

### 8. ldntm — done

* **Rules applied.** R-INTRO (208 → 61 words; first sentence split at its colon; "It is an implant block
  mask … a mask of contrasts: …" moved to the top of `## What the mask defines`, "It" → "The mask", its
  colon a full stop and its two contrasts two sentences); R-CAPTION; R-PARA, R-SENTENCE; R-LIST (the six
  `ldntm.c*` checks; the other Error Messages checks; the two parts of the rule table; the tip criteria
  that name no mask); R-RELATED (`TIPRTAD` joins the step bullet, as on hvntm); R-H3 (Exposure class,
  Mask errors, Resist and tone ← "Resist", Resist edges and shadowing, Overlay and alignment ← "Overlay",
  Pattern transfer).
* **Moved passage (G1):** Overlay above Pattern transfer.
* **R-PARAMS as a list** (as on hvntm): the design-rules paragraph sorts the tip criteria into those that
  name no mask and those that name the HV tip and the other tip masks; a single parameter table would
  lose that grouping, so the first group is a list under the base's lead-in and the second stays a
  sentence.
* **Hedge repeated on splits:** "On the step pages' readings" on the NSDM clause (the hvi/P1M sentence
  split at its semicolon) and on the resist-removal clause of Pattern transfer (split after the LDBHI
  clause); both halves were inside that hedge in the base.
* **Deleted template sentence:** the "This page gathers …" sentence (same wording as cap2m;
  `LOST hedges: 'about'`).
* **Declared additions** (`--allow-added markers`): `pdk-06` (Table F2b `-` / `+` sentence split),
  `pdk-errors` (*Error Messages* description; the two list lead-ins carry the base's two markers),
  `pdk-03` (lead-in of the tip-criteria list; the base marker stays on the sentence it ended). The two
  repeated "On the step pages' readings" are not counted by the tool.
* **Marker coverage.** Flags read: lists under lead-in markers; clauses with no marker of their own in
  the base.
* **Over the caps after the pass:** "On our reading the checks confine the layer … (inference from the
  check wording).[^pdk-errors][^pdk-06][^pdk-periph]" (55: two hedges, "On our reading" at the start and
  "(inference …)" at the end, each covering the whole; a split would leave each half with one of them);
  "It lies between `230` …" (46); the Polarity and tone cell (33; not in the body). Before → after:
  paragraphs 9 → 0, items 1 → 0, sentences 15 → 2, cells 1 → 1.
* **Content problems for the owner:** none found.

### 9. li1m — done

* **Rules applied.** R-INTRO (162 → 58 words; first sentence split at its colon; "It prints lines rather
  than holes …" moved to the top of `## What the mask defines`, "It" → "The mask"); R-CAPTION; R-PARA,
  R-SENTENCE; R-LIST (the three kinds of shape, the base's end marker `pdk-periph` moved to the lead-in
  per R-TABLE 3 / R-LIST 1); R-RELATED; R-H3 (Exposure class, Mask errors, Proximity and line ends,
  Substrate and tone, Overlay and alignment ← "Overlay", Pattern transfer). "Substrate and tone" keeps its
  own words: it is not one of the checker's synonyms.
* **Moved passage (G1):** Overlay above Pattern transfer.
* **R-PARAMS not applied.** The design-rules paragraph names five parameters, but each carries the
  page's own commentary ("two "Local Intrcnct 1" rows under the same variable names", "the value of
  li.7", "besides the add/drop and proximity rows", "the value of nsm.3"). A four-column table would have
  to reword those clauses into cells or drop them; the sentences were split at their semicolons instead.
  A reviewer who prefers the table can add it with a Value cell such as "0.29, the value of li.7".
* **Hedge repeated on a split:** "On the step pages' readings" on the resist-strip clause of Pattern
  transfer (as on ldntm).
* **Deleted template sentence:** the "This page gathers …" sentence (same wording as cap2m;
  `LOST hedges: 'about'`).
* **Declared additions** (`--allow-added markers,identifiers`): markers `pdk-06` ×2 (`gds_layers.csv`
  sentence; Table F2b sentence split at its dash pair, "— `+` …" → "It marks `+` …"), `pdk-periph` (x.9 /
  x.15a sentence), `mask-renders` (render sentence), `wong-1998` (the second Wong finding, "Wong et al.
  found that "dense lines …""), `pdk-03` (Table 4 / Table 7 sentence); identifiers `li1`, `cli1m` (the
  rule-table caption, copied from the sentence above the table).
* **Marker coverage.** Flags read: the shape list (lead-in marker), "Like the site's other layer choices
  …" and the arithmetic sentence after the Wong quotation (no marker of their own in the base).
* **Over the caps after the pass:** the Exposure-class sentence with two formulas (54 by the script,
  about 35 with each formula as one word); the Exposure class quick-facts cell (31; not in the body) and
  the nsm.3 rule cell (27, a quotation). Before → after: paragraphs 12 → 0, items 0 → 0, sentences
  13 → 1, cells 2 → 2.
* **Content problems for the owner:** none found.

### 10. licm1 — done

* **Rules applied.** R-INTRO (163 → 61 words; first sentence split at its colon; "Every transistor
  terminal … a critical KrF level." moved to the top of `## What the mask defines`); R-CAPTION; R-PARA,
  R-SENTENCE; R-LIST (the three margins against the layers beneath, the base's end marker repeated on
  the lead-in, the li.5 sentence keeping its own); R-RELATED; R-H3 (Exposure class, Mask errors, Side
  lobes, Proximity correction, Resist and tone, Overlay and alignment ← "Overlay", Pattern transfer).
* **Moved passage (G1):** Overlay above Pattern transfer.
* **R-PARAMS not applied.** The design-rules paragraph's parameters (`LICM1SLCD` … `XMAXCON`) are there to
  compare Table 2's labels with the periphery rules ("with their labels the other way round (our
  comparison)", "matches licon.2c", "the value of licon.12"); tabulating them would split each value from
  its comparison. Sentences split at their semicolons; the paragraph split in two.
* **Hedge repeated on a split:** "On the step pages' readings" on the resist-strip clause of Pattern
  transfer.
* **Steps section:** the step bullets and the `Steps:` run are untouched; the closing paragraph's
  "The exception is `SACETCH`: …; on its page's third reading …" was split at its semicolon.
* **Deleted template sentence:** the "This page gathers …" sentence (same wording as cap2m;
  `LOST hedges: 'about'`).
* **Declared additions** (`--allow-added markers`): `pdk-06` ×2 (`gds_layers.csv` sentence; the Table F2b
  sentence split at its colon), `pdk-periph` ×2 (x.9 / x.15a sentence; the margin-list lead-in),
  `mask-renders` (render sentence).
* **Marker coverage.** Flags read: the margin list (lead-in marker); the Wong arithmetic and the
  repeated-hedge strip sentence (no marker of their own in the base).
* **Over the caps after the pass (7 sentences):** "The nitride openings … on the step pages' readings"
  (55: the trailing hedge may cover all three clauses or only the last, so neither a list nor a split
  keeps its scope); the x.1a grid sentence (46, two quotations); "Every rendered die … — at least
  6 533 865 … — so the count …" (50, one dash pair); the Exposure-class formula sentence (53 by the
  script); the Choo et al. sentence (50, one study's figures); the Pattern transfer sentence (49, one
  dash pair around a quotation); the `SACETCH` step bullet (54; step bullets are left alone, §4.4).
  Before → after: paragraphs 10 → 0, items 0 → 0, sentences 16 → 7, cells 0 → 0.
* **Content problem for the owner:** `docs/masks/licm1.md:178`, the "Plate number" bullet reads "The sheet
  does not say what `265` encodes. It falls Its neighbours in the tab are `260` …" — "It falls" is a
  broken fragment (compare "It falls between … and …" on cap2m and capm). Left as it is.

### 11. lvom — done (page with three in-force notes)

* **Dropdowns.** The three `{dropdown}` notes are byte-identical to the base (checked by extracting every
  fenced block before and after, and by `check_preserved`, which reports no dropdown change). The two
  notes in the body still follow directly the paragraph that points at them ("… in the collapsed note
  below this paragraph"), and nothing was inserted between paragraph and note. `check_inforce` passes.
* **Rules applied.** R-INTRO (193 → 45 words); R-CAPTION; R-PARA, R-SENTENCE; R-LIST (Table F2b's 30 `C`
  rows, 2 + 1 + 4 + 13 + 7 + 3 = 30; Table F3b's `hvi` row; the per-die counts; the two uses of the
  pattern, under the base's "On the step pages' readings the pattern is used twice:"); R-RELATED; R-H3
  (Exposure class, Resist and tone ← "Resist", Overlay and alignment ← "Overlay", Pattern transfer).
* **Intro split with a repeated hedge (as on fom).** The intro's first sentence ran on after its colon
  through three clauses, all inside "On the LVOM page's reading". The intro keeps the reticle clause and
  the first reading clause; the NCHI / GOXETCH / LVGOX clause opens `## What the mask defines` with the
  base's hedge repeated ("On the {ref}`LVOM <step-044>` page's reading, the 1.8 V NMOS channel implant …"):
  ADDED ref `step-044`. "Designers do not draw this mask …" follows it, split at its first semicolon.
* **Moved passage (G1):** the Overlay paragraph moved above the Pattern transfer paragraph and its note;
  the note stays attached to Pattern transfer, and no text crossed a fence.
* **Deleted template sentence:** the "This page gathers …" sentence (same wording as cap2m;
  `LOST hedges: 'about'`).
* **Declared additions** (`--allow-added markers,numbers,refs`): markers `pdk-periph` (the `hvi` /
  `hvnwell` sentence split at its semicolon: the first half keeps `pdk-06` and `pdk-periph`, the second,
  a periphery rule, takes `pdk-periph`), `pdk-06` (Table F2b `-` / `+` sentence), `pdk-summary` (Table F3b
  list lead-in; the base marker stays on "The table has no column headed `hvi`", where "and it" became
  "The table"), `pdk-errors` (*Error Messages* description); number `15` (x.15a in the rule-table caption);
  ref `step-044` (above).
* **LOST `number_order` ('44', '1.8', '5', '1.8'), read by hand:** the intro sentence (step 44, 1.8 V,
  5 V, then the 1.8 V NMOS implant) is now two pieces, the second after the quick-facts table; the digits
  and their order are unchanged, but the quick-facts numbers sit between the pieces, which breaks the
  tool's contiguity test.
* **Marker coverage.** Flags read: lists under lead-in markers; "It reads a firm hard bake …", "We read
  the 0.180 µm …" and the Open question's second half had no marker of their own in the base.
* **Over the caps after the pass, all because of the notes:** "The SONOS rows matter for the resist …"
  (134 words) and the Pattern transfer paragraph that points at the second note (108) each contain the
  pointer "in the collapsed note below this paragraph"; splitting either would leave the pointer's
  paragraph no longer directly above its note (R-DROPDOWN 4), so both stay whole (their long sentences
  were split). Two sentences inside the notes (48, 84) are not edited (§2.5). Also: "The table marks `-` …"
  (47, one dash pair), the Kim et al. sentence (46), the Polarity and tone cell (53; not in the body).
  Before → after: paragraphs 10 → 2, items 0 → 0, sentences 19 → 4 (two of them inside notes), cells
  1 → 1.
* **Content problems for the owner:** none found.

### 12. lvtnm — done

* **Rules applied.** R-INTRO (172 → 61 words; first sentence split at its colon; "What makes it unusual
  …" moved to the top of `## What the mask defines`, "it" → "the mask", its colon a full stop);
  R-PARAMS (four parameters: `LVTNMCD`, `LVTNMCDSP`, `lvtpmos_poly`, `LvtEnc_forPowerRail`); R-CAPTION;
  R-PARA, R-SENTENCE; R-LIST (the device pages' three descriptions; Table F2b's 28 `C` rows as ten
  fragment bullets, 2 + 2 + 2 + 1 + 3 + 4 + 2 + 5 + 6 + 1 = 28; the two Table C3 definitions; the
  `clvtnm` checks; the per-die counts); R-RELATED; R-H3 (Exposure class, Mask errors, Resist and tone ←
  "Resist", Resist edges, Overlay and alignment ← "Overlay", Pattern transfer).
* **Moved passage (G1):** Overlay above Pattern transfer.
* **R-PARAMS.** "Table 2 … repeats the width and space as `LVTNMCD` 0.38 and `LVTNMCDSP` 0.38, and Table 4
  gives a "Channel length for low Vt PMOS" of 0.35 (`lvtpmos_poly`), matching poly.1b, and a "Width of the
  Low Leakage gate …" of 0.28 (`LvtEnc_forPowerRail`).[^pdk-03][^pdk-periph]" → lead-in "*Criteria &
  Assumptions* repeats the width and space in Table 2 and gives two criteria in Table 4:[^pdk-03]" and a
  four-row table. "matching poly.1b" stays with its value in the Value cell, and `pdk-periph` (the
  source of poly.1b) goes with it; `pdk-03` stays on the lead-in. No marker added or lost here.
* **Hedge repeated on a split:** "The high-Vt PMOS and `pmos_core` rows are not devices the `lvtn`
  function line names, and on the table the three … flavours differ … (…; our reading of the
  rows).[^pdk-06]" — split at ", and on the table"; the first half now ends "(our reading of the
  rows).[^pdk-06]" too (ADDED hedge and marker).
* **Deleted template sentence:** the "This page gathers …" sentence (same wording as cap2m;
  `LOST hedges: 'about'`).
* **Declared additions** (`--allow-added markers,numbers,hedges`): markers `pdk-06` (above),
  `pdk-errors` (*Error Messages* description; the base marker moved to the check-list lead-in),
  `mask-renders` (README sentence split at its colon); numbers — the PDK-table column (`2` ×2, `4` ×2);
  hedge `our reading` (above).
* **LOST `number_order` ('2', '0.38', '0.38', '4', '0.35', '1', '0.28'), read by hand:** the R-PARAMS table;
  values 0.38, 0.38, 0.35 (poly.1b), 0.28 in the base's order, each on the table the base gives it.
* **Marker coverage.** Flags read: lists and table rows under lead-in markers; "The LVTNM page takes the
  word "block" …", "The sheet does not say what `038` encodes.", "Both register to …" and the second Open
  question's last sentence had no marker of their own in the base.
* **Phone check.** The parameter table does not scroll at 400 px, but the long identifier
  `LvtEnc_forPowerRail` keeps its column wide and the description cell runs to about 12 lines (§8.6's
  five-line question); see guide problem G3. The PDK-table cells were shortened from "Table 2" to "2"
  (header "PDK table") on this page and on ctm1 and fom to give the description column more room, and
  that column is right-aligned (numbers, R-TABLE 7).
* **Over the caps after the pass:** the Hook et al. sentence (68 by the script, nearly all of it two
  quotations); "At 365 nm that threshold …" (46); the Polarity and tone cell (45; not in the body).
  Before → after: paragraphs 10 → 0, items 1 → 0, sentences 16 → 2, cells 1 → 1.
* **Content problems for the owner:** none found.

### 13. mm1 — done

* **Rules applied.** R-INTRO (170 → 40 words; first sentence split at its colon; the "With 0.14 µm lines
  …" and waffle-drop sentences moved to the top of `## What the mask defines`, "it is" → "the mask is",
  the first split before "the step pages read it"); R-PARAMS (nine Table 4 / Table 7 criteria); R-CAPTION
  (rule table, parameter table); R-PARA, R-SENTENCE; R-LIST (what the mask carries, with the "dummy fill"
  item keeping its "on our reading of the waffle-drop rules below"); R-RELATED; R-H3 (Exposure class, Mask
  errors, Reflective substrate, Fill and the polish above, Overlay and alignment ← "Overlay", Pattern
  transfer).
* **Moved passage (G1):** Overlay above Pattern transfer.
* **R-PARAMS.** The Table 2 sentence (with its remark that the "Metal 1 - Cu" row belongs to a copper back
  end) stays prose. "Table 4 adds … (`DEFC`) … (`BiasMM1`) … (`Met1Thick`), and, among its pattern-density
  criteria, … (`OxideMinPD`) … (`MMPDrange`) … (`SMALLPDBOX`) … (`PD_FrameWP`); Table 7 gives … (`HugeM`)
  and … (`waffle_large`).[^pdk-03]" became "Tables 4 and 7 add the following:[^pdk-03]" and a nine-row
  table in the base's order; "among its pattern-density criteria" went into the caption with the four
  identifiers it covers.
* **Hedge repeated on a split:** "On the step pages' readings" on the passivation / strip / clean clause
  of Pattern transfer ("with passivation, resist strip and clean treated as part of that step" → "On the
  step pages' readings passivation, resist strip and clean are treated as part of that step").
* **Deleted template sentence:** the "This page gathers …" sentence (same wording as cap2m, here wrapped
  "gathers what public sources say / about the mask itself"; `LOST hedges: 'about'`).
* **Declared additions** (`--allow-added markers,numbers,identifiers`): markers `pdk-periph` ×2 (list
  lead-in, the base marker staying on the island/hole sentence; the fill-check sentence split at its
  colon), `pdk-06` (`gds_layers.csv` sentence), `mask-renders` (render sentence), `steps-sheet` ("Plate
  number" lead), `itrs-03` (ITRS sentence, as on ctm1), `word-2002` ("… and obtained" → "They obtained"),
  `wong-1998` (second Wong finding), `rocke-1988` ("… and use" → "They use"); numbers — the PDK-table
  column and caption (`4`, `7`), "ITRS 2001" repeated, `1` and `3` from "metal 1" and "nsm.3" in the rule
  caption; identifier `m1` (rule caption).
* **LOST `number_order`, read by hand:** the Exposure-class sentence (the repeated "ITRS 2001", as on
  ctm1); the Table 4 / Table 7 sentence (the parameter table: values 0.15, 0.6, 0.35, 0.75, 0.3, 700,
  0.55, 3, 7.2 in the base's order, each on the base's table; the "1" of "Metal 1 thickness" and the "4"
  of "divisible by 4" are inside the quoted descriptions as before).
* **Marker coverage.** Flags read: the shape list (lead-in marker); clauses with no marker of their own in
  the base. (`markcov`'s NEWHEDGE "assum" is "Criteria & Assumptions" in the caption, not a hedge.)
* **Over the caps after the pass:** the flag-legend sentence (68 by the script, seven quotations); the
  quick-facts Exposure class cell (36; not in the body) and two quoted rule cells (33, 27). Before →
  after: paragraphs 11 → 0, items 1 → 0, sentences 15 → 1, cells 3 → 3.
* **Content problems for the owner:** none found.

### 14. mm2 — done

* **Rules applied.** As on mm1: R-INTRO (171 → 40 words; "Its rules repeat …" → "The mask's rules
  repeat …", moved with the plate-case sentence to the top of `## What the mask defines`); R-PARAMS
  (`BiasMM2`, `Met2Thick`, `Met2_Qthick`, `FEXT`, `HugeM`); R-CAPTION; R-PARA, R-SENTENCE; R-LIST (what the
  mask carries; the plate-case label's five fields as sub-bullets inside its bullet); R-RELATED; R-H3
  (Exposure class, Mask errors, Reflective substrate, Fill and the polish above, Overlay and alignment ←
  "Overlay", Pattern transfer).
* **Moved passage (G1):** Overlay above Pattern transfer.
* **Rendering fix:** the base wrapped `"Metal 2` / `- Cu" row` so that a source line began with "- ",
  which CommonMark reads as a list item interrupting the paragraph (the same trap as §6's leading `>`).
  The words are unchanged; the line break moved so that "Metal 2 - Cu" stays on one line.
* **Plate-case label bullet (198 words).** R-PARA 4: the lead sentence stays (≤ 30 words); the base's
  "It gives the material …, the type …, a "Percent Clear" …, a "Level" … and a CD specification …
  in no stated unit.[^steps-sheet]" became "It gives:[^steps-sheet]" and five sub-bullets; the reading of
  the fields and the Hochmuth et al. passage follow as indented continuation paragraphs, each split at
  its semicolon.
* **R-PARAMS.** "Table 4 adds … (`BiasMM2`), … (`Met2Thick`) and the same 0.35 for "(SP8T/S8T\*)"
  (`Met2_Qthick`), and the pattern-density criteria it shares with metal 1; Table 5, the laser-fuse
  criteria, gives … (`FEXT`), and Table 7 a … (`HugeM`).[^pdk-03]" became "Table 4 adds the
  pattern-density criteria it shares with metal 1, and Tables 4, 5 and 7 give the following:[^pdk-03]",
  a five-row table ("the same, for "(SP8T/S8T\*)"" keeps the base's "the same"), and the caption note
  "Table 5 holds the laser-fuse criteria".
* **Hedge repeated on a split:** "On the step pages' readings" on the passivation / strip / clean clause
  (as on mm1).
* **Deleted template sentence:** the "This page gathers …" sentence (same wording as cap2m;
  `LOST hedges: 'about'`).
* **Declared additions** (`--allow-added markers,numbers,identifiers`): markers `pdk-periph` ×2 (list
  lead-in; the fill-check sentence split at "a limit." — "The limit falls from …"), `pdk-06`, `mask-renders`,
  `itrs-03`, `wong-1998` (the same splits as on mm1); numbers — the PDK-table column and the lead-in
  ("Tables 4, 5 and 7"), "ITRS 2001" repeated, the `2` of "Metal 2" and "metal 2" in the caption;
  identifiers `m2`, `via-2` (rule caption).
* **LOST `number_order`, read by hand:** the Exposure-class sentence (repeated "ITRS 2001"); the Table 4 /
  5 / 7 sentence (values 0.6, 0.35, 0.35, 0.005, 3 in the base's order, each on the base's table).
* **Marker coverage.** Flags read: lists under lead-in markers; clauses with no marker of their own in the
  base.
* **Over the caps after the pass:** the CD-specification sub-bullet (46; one field with its numbers);
  the Hochmuth et al. sentence (46, two quotations); the flag-legend sentence (73 by the script, eight
  quotations); the quick-facts Exposure class cell (36) and two quoted rule cells (33, 27). Before →
  after: paragraphs 11 → 0, items 2 → 0, sentences 15 → 3, cells 3 → 3.
* **Content problems for the owner:** none found.

### 15. mm3 — done

* **Rules applied.** R-INTRO (178 → 59 words; first sentence split at its colon; "It is the first of the
  thick upper metals …" and "Like `VIM2` …" moved to the top of `## What the mask defines`, "It" → "The
  mask"); R-CAPTION; R-PARA, R-SENTENCE; R-LIST (what the mask carries; the five metal-3 thicknesses of
  Table 4, under the base's own "metal-3 thicknesses "for antenna ratio calculation"" lead-in); R-RELATED;
  R-H3 (Exposure class, Mask errors, Thick metal, capacitors and the resist, Fill and the polish above,
  Overlay and alignment ← "Overlay", Pattern transfer). The `**Variants.**` run-in stays bold (it sits
  under `## What the mask defines`, where the checker allows no H3).
* **Moved passage (G1):** Overlay above Pattern transfer.
* **R-PARAMS as a list.** The Table 4 sentence nests its values inside two named blocks ("in its
  "Material Thicknesses" block", "its "Waffling / Pattern Density" block has criteria not tied to one
  level, among them …") and gives one description ("for antenna ratio calculation") for five variables.
  A four-column table would repeat that quotation five times and lose the block structure, so the five
  thicknesses became a list under the base's lead-in, and the block and Table 7 clauses sentences.
* **Hedges repeated on splits:** "(our comparison)" on the capacitor-numbering sentence of "Plate
  number" (split at its colon, as on cap2m); "On the step pages' readings" on the passivation / strip /
  clean clause of Pattern transfer.
* **Markers moved to their own clause:** Table C3 / capm.3 sentence (`pdk-06` to C3, `pdk-periph` to
  capm.3); x.11 / Table C3 / fuse note sentence (`pdk-periph`, `pdk-06`, `pdk-periph`).
* **Deleted template sentence:** the "This page gathers …" sentence (same wording as cap2m;
  `LOST hedges: 'about'`).
* **Declared additions** (`--allow-added markers,numbers,identifiers`): markers `pdk-summary` ×2 (Table F4
  sentence; Table F3c / F3d sentence), `pdk-periph` ×3 (list lead-in; the fuse-note clause; rule m3.pd.1
  split from the fill check), `pdk-06` ×2 (`gds_layers.csv` sentence; Table F2b `+` sentence),
  `pdk-errors` (*Error Messages* description), `mask-renders` (render sentence), `pdk-03` ×3 ("It gives
  0.3 and 0.3 for a "Metal 3-Cu" row"; the thickness-list lead-in; the `MMPDrange` sentence); numbers
  `3` ×2 and identifiers `m3`, `via-3` (rule caption).
* **Marker coverage.** Flags read: the lists (lead-in markers); clauses that had no marker of their own in
  the base (the capacitor reading, "The F3c values equal …", "It does not say what the "nikon cross" is
  …", "Whether the `MM3` plate is dry-etched …", and similar).
* **Over the caps after the pass:** "The rule set's first entry …" (48); the Exposure-class sentence with
  two formulas (62 by the script); "That threshold is about 0.18 µm …, so plate CD errors …" (52: a split
  would need "therefore" for "so"); "On the step pages' readings the resist is coated over the 0.845 µm
  metal-3 stack, which carries …" (57: the hedge covers the whole, and a split would need it repeated
  mid-argument); the Pattern transfer sentence (47); the flag legend (73, quotations); two quick-facts
  cells (37, 29; not in the body) and four quoted rule cells. Before → after: paragraphs 16 → 0, items
  1 → 0, sentences 23 → 6, cells 6 → 6.
* **Content problems for the owner:** none found.

### 16. mm4 — done

* **Rules applied.** R-INTRO (176 → 62 words; first sentence split at its colon; "Its lines are metal 3's
  0.3 µm, the step pages leave open …, and it is the one metal mask …" moved to the top of
  `## What the mask defines` as three sentences, "Its lines" → "The mask's lines"); R-PARAMS (the seven
  laser-fuse criteria of Tables 5 and 9); R-CAPTION; R-PARA, R-SENTENCE; R-LIST (what the mask carries;
  the four metal-4 fuse checks of the *Error Messages* page); R-RELATED; R-H3 (Exposure class, Mask errors,
  Thick metal, capacitors and the resist, Fill and the polish above, Overlay and alignment ← "Overlay",
  Pattern transfer). `**Fuses.**` and `**Variants and flows.**` stay bold (under `## What the mask
  defines`).
* **Moved passage (G1):** Overlay above Pattern transfer.
* **R-PARAMS.** "It lists in a column headed "Value (um)" a "Max. width …" of 0.8 (`FSW`), the width of
  mf.1; a "Min. L …" of 6.605 (`FSLE`), below the 7.200 µm of mf.2; … (`LASSPT`); … (`LASMA`); and …
  (`MELTRAD`); Table 9 gives … (`PimFuseEnc`) and … (`PimLaserEnc`).[^pdk-03]" → "It lists the first five
  rows below in a column headed "Value (um)", and Table 9 gives the last two:[^pdk-03]" and a seven-row
  table; the base's comparisons ("the width of mf.1", "below the 7.200 µm of mf.2") stay with their
  values. The closing design-rules paragraph ("Table 2 … Table 4 …; Table 5 gives the laser-fuse criteria
  quoted above; Table 7 …; and Table 9 …") refers back to these and was split into one sentence per table
  instead, each keeping `pdk-03` (R-SENTENCE 5; "Table 7 a …" → "Table 7 gives a …").
* **Hedges repeated on splits:** "(our comparison)" ("Plate number"); "On the step pages' readings"
  (Pattern transfer), as on mm3.
* **Markers moved to their own clause:** the Table 2 / Table 4 / Table C3 sentence under "Variants and
  flows" (`pdk-03`, `pdk-03`, `pdk-06`); the "other fuse rules" sentence (`pdk-periph` to the rules,
  `pdk-errors` to the Error Messages spacings).
* **Deleted template sentence:** the "This page gathers …" sentence (same wording as cap2m;
  `LOST hedges: 'about'`).
* **Declared additions** (`--allow-added markers,numbers,identifiers`): markers `pdk-periph` ×5 (list
  lead-in; fuse-note / x.11 split; m4.pd.1 split; Overlay split; first Open question), `pdk-06` ×4 (Table C3
  / `gds_layers.csv` fuse sentence; `gds_layers.csv` purposes; first and second Open questions),
  `pdk-errors` ×3 ("SkyWater's published DRC checks name the level." — its colon became a full stop, so it
  keeps the marker; the page description; "It gives target spacings …" — the base marker is on the list
  lead-in), `pdk-03` ×6 (the per-table sentences above; the Variants Table 2 sentence; the second Open
  question), `mask-renders` (render sentence); numbers — the PDK-table column (`5`, `9`) and "Table 9" in
  the lead-in, `4` of "metal 4" in the rule caption; identifiers `m4`, `via-4` (rule caption).
* **LOST `number_order` ('6.605', '7.200', '2', '3.5', '3', '0.3', '3.6', '9', '12', '30'), read by hand:**
  the laser-fuse table; values 0.8, 6.605 (with 7.200 and mf.2), 3.5, 0.3 (with "(3 s)"), 3.6, 12, 30 in the
  base's order, on the base's tables.
* **Marker coverage.** Flags read: lists and table rows under lead-in markers; clauses without a marker of
  their own in the base. One real case fixed: "SkyWater's published DRC checks name the level." (above).
* **Over the caps after the pass:** the same kinds as on mm3 — "The rule set's first entry …" (48), the
  two-formula Exposure-class sentence (55 by the script), "That threshold is about 0.18 µm … so …" (52),
  "On the step pages' readings the resist is coated over the 0.845 µm metal-4 stack, which carries …"
  (58), the Pattern transfer sentence (47), the flag legend (73, quotations); two quick-facts cells and
  three rule cells. Before → after: paragraphs 14 → 0, items 2 → 0, sentences 29 → 6, cells 5 → 5.
* **Content problems for the owner:** none found.
