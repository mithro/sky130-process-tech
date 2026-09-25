# Progress — readability batch 5, steps 064–075 (`topic/rd-steps-064-075`)

Writer: Opus. Started 2026-09-26 from `main` at `7fea7c90`. Guide: `docs/plans/readability-guide.md`
(§1, §2, §4.1, §5, §6, §7, §8), including the batch-4 rulings (R-LIST plain bullets, R-H3 step 6,
R-CATEGORY step 1, R-PARA step 2 inside list items, R-TOOLS step 2 pilot form). Model pages: 052, 058,
043. One commit per page.

## Method, every page

* Baseline build and tiles (1280 px and 400 px, `--max-height 40000/60000`) of all 12 pages before any
  edit.
* Preservation: `uv run python tools/check_preserved.py --base main <page> --allow-regrouped` first,
  with no other allowance; every ADDED line is named in the page entry below, with the rule that adds
  it, before the categories are declared with `--allow-added`. `--allow-dropdown-edits` is never used.
* Marker coverage: `tmp/readability/markcov.py` (git-ignored) pairs every new sentence that is not
  verbatim in the base with its closest base sentence and flags a lost marker or hedge word; every flag
  is read and explained in the page entry.
* Invariants: `tmp/readability/invariants.py` (git-ignored) compares with `main`: `## References`
  section, footnote definitions, generated index-links block, `{figure}` blocks, quick-facts table,
  every `{dropdown}` block, H2 list, Deep-dive `* ` count; and reports admonitions, the glance box,
  glance markers that do not recur below it, duplicate H3s and the italic scope lead-in.
* Caps: `tmp/readability/caps.py` (git-ignored): `measure.py`'s blocks and `measure5.py`'s sentence
  split at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25), `{figure}` blocks,
  `{dropdown}` bodies, the generated block and `## References` excluded.
* Repeats: `tmp/readability/repeat.py` (git-ignored), 10-word runs shared by two H2 sections.
* Dropped words: `tmp/readability/worddiff.py` (git-ignored, added after 074's first draft) lists every
  run of words present in the base and missing from the page (glance box, recap table, References and
  footnotes excluded), so a word lost in a replacement cannot hide behind unchanged numbers and markers.
  Every page was re-run with it; each run it lists is a move, a case change at a split, a joining
  "and"/"which" at a split, a "Strength:" label, or the table and label rewordings named in the page
  entries. (On 074 it caught "removing step:" dropped by an overlapping replacement in the first draft;
  restored before the commit.)
* Checkers after each page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`,
  `gen_figures --check`; `-W` build; tiles at 1280 px and 400 px, read against the baseline.

## Batch measurement (§1 caps, open text; figure captions excluded)

Counted with `tmp/readability/caps.py`: `{figure}` blocks, `{dropdown}` bodies (in-force notes may not be
edited), the generated index-links block and `## References` are **excluded**. Before = `main` at
`7fea7c90`.

| §1 cap | Before | After |
|---|---:|---:|
| paragraphs > 100 words | 26 | 0 |
| list items > 60 words | 48 | 2 |
| sentences > 45 words | 87 | 10 |
| table cells > 25 words | 0 | 0 |

`measure5.py` as committed (it still counts `{figure}` caption text and dropdown bodies): paragraphs
38 → 12 (the 12 remaining are the 12 figure captions), items 48 → 2, sentences 96 → 19, cells 0 → 0.

**Left over the caps, with reasons** (each is also in its page entry):

* Items: 064 "5 V NMOS" (61 w; its only seam is before "That is the HVNTM tip"); 064 "Exposure" lead
  (62 w; its only seam is before "That is well within …").
* Sentences (46–50 w): 064 the `ntm` inference (46); 065 "We read that value …" (46), "Gate overlap" (46
  + label), "Without `ASTI` …" (47), "For SKY130's 0.15 µm drawn gate …" (47); 066 the GSD pilot-form head
  (48 with the tool name); 068 "The Error Messages page's checks …" (46); 069 the Hu sentence (49) and
  Hori's LATID (50); 073 the Cypress two-quotation lead (46 + label). Each would need a split inside a
  quotation, a split that leaves part of a claim outside its hedge or marker, or a pilot-form head.
* First sentence over 25 words: 074 (27; no seam).
* Leads over 120 words, as in the base: 064 (129), 065 (129), 075 (163, three paragraphs).

**Gates (end of batch, in the worktree):** `check_steps`, `check_refs`, `check_machines`,
`check_materials`, `check_masks`, `check_papers`, `check_patents`, `check_filings`, `check_inforce` — 0
problems; `gen_papers`, `gen_patents`, `gen_filings`, `gen_index_links`, `gen_steps`, `gen_figures`,
`gen_step_tables` `--check` — 0 differences; `sphinx-build -W -E` into a fresh directory — exit 0.
`invariants.py` over the 12 pages: 0 changes to References, footnote definitions, generated blocks,
figures, quick facts, dropdowns, H2 lists or Deep-dive counts; one admonition (the glance box) per page;
every glance marker recurs below; no duplicate H3; every scope sentence is the italic lead-in.
`check_preserved.py --allow-regrouped` (plus the categories named per page): the only remaining lines are
three LOST `number_order` (066 threshold table, 068 rule table, 071 "-38" hedge moved to the end of its
sentence), each checked by hand in its page entry; no `{dropdown}` line on any page.

## Pages

### 064 NTM — done

* **Lead.** Split into two paragraphs before "`NTM` coats this now-topographic surface" (what arrives /
  what the step does). The 16-word parenthetical "(inference: the tip and its halo … serves both)"
  closed as its own sentence, "(Inference: … serves both.)" (R-SENTENCE step 7). Lead 129 words, as in
  the base: §1's 120 cannot be met without dropping words. First sentence 20 words.
* **R-H3.** `### What the public record shows` after the figure caption, over the PDK evidence (mask
  table, layer list, Error Messages, Table F2b, Criteria & Assumptions; ≈ 390 words, one inference
  that the derivation is Boolean, stated with its hedge).
* **R-PARA.** The 230-word evidence paragraph split at its seams, with run-in labels (evidence
  sequence, R-PARA step 3): "**Mask and layer.**", "**Error checks.**", "**Created data.**" (the mask
  page's reading of the created data and Table F2b), "**Drawn tip layers.**" (the two designer-drawn
  tip layers), "**Published parameters.**".
* **R-SENTENCE.** "The generated mask layer is `cntm` …;[^pdk-06] there is no designer-drawn `ntm`
  layer …" split at the semicolon (each half keeps its own marker; the inference clause had none).
  Error Messages sentence split at the colon and at the semicolon; `[^pdk-errors]` **repeated** on
  "names other layers." and on the checks sentence so each claim keeps it (declared). Table F2b
  sentence split at ", which is consistent with" → "This is consistent with …"; `[^pdk-06]`
  **repeated** on the first half (declared).
* **R-LIST.** The *Criteria & Assumptions* parameters ("a tip implant angle of 7° …, an "NTM
  shadowing" distance of 0.16 µm and, immediately below it …, a "pseudo-shadowing" allowance …") →
  three plain bullets (no invented labels), every word kept except the list-joining "and"; the
  sentence had no marker of its own (`[^pdk-03]` ended the next sentence), so `[^pdk-03]` is
  **repeated** on the lead-in before the colon (declared). The 0.1 µm / 0.01 µm sentence and the
  "These are the quantities …" sentence stay as prose after the list, unchanged.
* **R-CATEGORY.** Classification sentence (38 words, no semicolon or closing dash to split at, so kept
  whole: R-CATEGORY step 1 as ruled in batch 4) alone; the three remaining sentences describe this step
  → `**Specific to this step:**` and three bullets. The third ("It is the first mask … — 0.18 µm of
  poly … (the PDK's figure … no thinner)[^pdk-03] — rather than on a planar surface", 60 words, a dash
  pair holding a 19-word parenthetical) split per R-SENTENCE step 1: the frame closes ("… topography
  rather than on a planar surface."), the dash material becomes "The topography is …" (subject + verb
  added, step 7) in an indented continuation paragraph, and the parenthetical closes as its own
  sentence "(The PDK's figure … no thinner.)[^pdk-03]"; `[^pdk-03]` **repeated** after "poly cap after
  SPE"" so the 0.2 µm claim keeps its marker (declared).
* **Why.** Paragraph 1 (150 words) split before "ITRS 2001 asks" (history / roadmap). The Ogura
  sentence split at its semicolon (each half keeps its marker). The 85-word ITRS sentence split at "—
  and defines" ("It defines …", subject added) and at the semicolon before "the same rule applied to
  SKY130's …"; `[^itrs-01]` **repeated** on the first two pieces (declared, ×2). The hedge "(our
  reading of the roadmap; SKY130's physical gate length is not published)" stays with the sentence it
  sat in, the application to SKY130; grammatically it never governed the ITRS values.
* **R-HEDGE.** Scope sentence as the italic lead-in, word for word.
* **R-PARA step 4 (items).** "Resist coat" (70 w): continuation paragraph at "The poly steps cause …".
  "Exposure": the 60-word first sentence split at its dash ("That is well within …", subject + verb
  added); continuation paragraph at "ASML describes …". "Alignment": split at the colon ("The overlay
  budget … by shadowing." / "The PDK's 0.16 µm …" continuation; the marker sat in the second half in
  the base).
* **R-DERIVATION not applied** to "(k₁ = 0.7 × 0.6 / 0.365 ≈ 1.2 at NA 0.6 for the space)": one formula
  inside a recipe step, not a passage; left inline as on 052.
* **R-TOOLS.** ASML: *SkyWater says:* "facilities page lists …" (verb-first form of 034), *Tool
  exists:*, *Runs this step:*. Tracks: *Tool exists:* "strong for existence."; the clause "pairing with
  exposure tools not public" is not a grade and becomes the continuation paragraph ("Pairing …",
  capital only). Overlay/CD: two grades. Three tools: no recap table.
* **R-RELATED.** "Sibling tip masks:" → "Same module: sibling tip masks …" (HVNTM, LDNTM, TIPRTAD all
  carry this module's Phase cell); "Mask page:" → "Mask:". The SPNIT/PSDM/NSDM bullet ("The spacer that
  follows the module") keeps no label: "Same module" would contradict its own gloss.
* **R-OPENQ.** "PMOS extensions" (80 w): lead "The mask table has no P-tip mask,[^pdk-05] yet" with the
  two PDK facts as sub-bullets (every word, the joining comma now a semicolon) and the question as the
  continuation paragraph, in the original order. Labels added to the other three ("Boolean recipe",
  "Resist, tool and hardening", "Film under the resist"), text unchanged; "Boolean recipe" split at its
  semicolon (56 w sentence).
* **R-GLANCE.** Does and Why from the lead and "Three tip masks exist because …"; Public numbers:
  `NTMCD`/`NTMCDSP` 0.84/0.7 µm, the 7° angle and the 0.16 µm "NTM shadowing" `[^pdk-03]`; tool line
  with the page's grades; Not public from Open questions 1–2.
* **Skipped.** R-REPEAT (no 10-word repeat across H2s); R-TABLE on the parameters (the items carry
  their own glosses and the one inference; a list keeps every word).
* **Preservation** (`--allow-regrouped` only): ADDED markers `itrs-01`×2, `pdk-03`×3, `pdk-06`,
  `pdk-errors`×2 (the repeats above), `skw-01` (glance) and one `pdk-03` of the three (glance);
  numbers 0.16, 0.7, 0.84, 1.8, 7, quote "NTM shadowing", hedges "inference", "not public",
  number_order (0.84, 0.7, 7, 0.16) — the glance box. REGROUPED: the parameters list (7, 0.16, 0.045),
  the ITRS sentence (same digits, same order, split into three), the Exposure sentence (0.84, 0.7, 1, 2
  | 0.7, 0.6, 0.365, 1.2, 0.6). Declared `--allow-added markers,numbers,quotes,hedges,number_order`:
  clean.
* **Marker coverage.** 19 flags, all read: the repeats above; split halves whose base marker belonged
  to the other clause (`cntm` layer / inference; openings / k₁; overlay budget / PDK distances); the
  ITRS "our reading" (see Why); glance and label lines.
* **Caps**: para > 100 5 → 0; item > 60 5 → 2; sentence > 45 11 → 1. Left: the 5 V NMOS item (61 w; its
  only seam is before "That is the HVNTM tip"), the Exposure item's lead (62 w; its only seam is before
  "That is well within"); the 46-word `ntm` inference sentence (no seam that keeps "we infer" with its
  whole claim).

### 065 ASTI — done

* **Lead.** Split into two paragraphs before "The gate stack itself masks the channel" (what the step
  does / why the tip is self-aligned); its 49-word sentence split at the semicolon ("The gate poly is
  shielded …"). Lead 129 words, as in the base; first sentence 21 words.
* **R-H3 not applied.** The passage after the figure is 107 words, under R-H3's 120.
* **R-SENTENCE.** The 85-word "That the tip is arsenic is stated publicly: …" sentence split at
  ", which we read as" → "We read that value as the tip's lateral extent because … (inference),
  beside the deeper … row …" (R-PARA step 5: the relative pronoun gets its noun back) and at the
  semicolon ("The same page gives …"); `[^pdk-03]` **repeated** on the first piece so the "N Tip
  (As)" claim keeps it (declared). The clause order is the base's (an earlier try moved the "beside"
  clause forward and `check_preserved` reported a LOST `number_order`; reverted). The halo/strip
  sentence becomes its own short paragraph.
* **R-CATEGORY.** Classification sentence (40 w; no semicolon or closing dash) kept whole. The
  remaining sentence (55 w, a dash pair around the category page's quotation) split per R-SENTENCE
  step 1 into "It is the shallowest implant in the flow." + the quotation sentence, and "With the
  deep source/drain implants (…), it is one of the implants that amorphise …" ("it is" added). Two
  statements about this step → `**Specific to this step:**` with two bullets; the quotation stays in
  the bullet of the claim it supports.
* **R-PARA step 4 (Why items).** "Short-channel control" (101 w): lead split at its semicolon, the three
  sources (Wikipedia, ITRS, Thompson) as plain sub-bullets, each with its marker (a list of studies:
  no labels). "Series resistance" (77 w): lead split at the semicolon, the ITRS and LDD sentences as the
  continuation paragraph. "Gate overlap": split at its semicolon ("Too much overlap adds Miller
  capacitance.").
* **R-PARA.** "Arsenic rather than phosphorus" (109 w) split before "Its drawbacks are electrical"
  ("Its" → "Arsenic's", R-PARA step 5); its 50-word first sentence split at ", and it diffuses" ("It
  diffuses slowly …"; each half keeps its marker); the Nobili sentence split at its semicolon. The bold
  run-in labels a single paragraph, so it stays bold (R-H3 step 4).
* **R-HEDGE.** Italic lead-in, word for word, including "(SKY130's energy and dose are not public)".
* **R-PARA step 4 (How items).** "Energy" (96 w): lead = the first sentence; the ITRS sentence split at
  its semicolon ("ITRS 2001 defines … length.[^itrs-01]" with the marker **repeated**, declared; "For
  SKY130's 0.15 µm drawn gate … (our reading of the roadmap).[^itrs-01]" keeps the hedge on the
  SKY130 application, which is all it governed). "Dose" (66 w): lead = the first sentence; the
  amorphisation sentence split before ", so the implanted layer" ("So the implanted layer …", the
  split R-PARA step 2 allows inside a paragraph), which keeps the lowercase Wikipedia quotation inside
  its own sentence (R-SENTENCE step 6). "Tilt and twist" (144 w, a 104-word sentence): the dash pair
  becomes "The stack is 0.18 µm of poly … "poly cap after SPE".[^pdk-03]" (subject + verb added;
  `[^pdk-03]` **repeated**, declared) and "(The PDK's figure … no thinner.)[^pdk-03]", then "So a 7°
  beam is blocked for at least about 0.38 µm × tan 7° ≈ 47 nm …" (a single-operation estimate, inline
  per R-DERIVATION step 6); Yoneda and "rotation scheme is not public" as a second continuation
  paragraph. Same treatment as 064's category bullet.
* **R-TOOLS.** GSD: *SkyWater says:* holds only the two quotations with `[^skw-01]`; the gloss "both
  offer arsenic and reach the 10¹⁵ cm⁻² decade, …" is this reference's and becomes the continuation
  paragraph ("Both …"), as on 050. 8250: *SkyWater says:* the quotation; grades; the platform and dose
  sentences (vendor facts and our gloss) as the continuation paragraph. Grades unchanged. Two tools:
  no recap table.
* **R-RELATED.** "The other tip implants:" → "Same module: the other tip implants …". "Activation: …;
  spacer: …; deep n⁺ junction: …" keeps its own labels (three relationships, none of them one R-RELATED
  label).
* **R-OPENQ.** Labels "Energy and dose", "Rotation scheme", "Pre-amorphisation", "Tip and halo order";
  text unchanged.
* **R-GLANCE.** Does/Why from the lead and "The extension does three jobs"; Public numbers the "N Tip
  (As)" row, its 0.01 µm entry with the page's "(inference)", the 7° angle `[^pdk-03]`; tool line with
  both tools' grades; Not public from Open questions 1–2.
* **Preservation** (`--allow-regrouped` only): ADDED markers `itrs-01`, `pdk-03`×2 (the repeats above),
  `pdk-03`, `skw-01` (glance); numbers 0.01, 1.8, 7, 8250, quote "N Tip (As)", hedges "inference"×2,
  "not public", number_order (0.01, 7) — the glance box. REGROUPED lines: the arsenic sentence, the
  Energy and Dose items, the tilt item — same digits, same order. Declared
  `--allow-added markers,numbers,quotes,hedges,number_order`: clean.
* **Marker coverage.** 23 flags, all read: the repeats; split halves whose base marker belonged to the
  other clause (DIBL / Wikipedia; drain current / ITRS; "So the implanted layer …" after the three
  amorphisation markers; "So a 7° beam …" after the stack markers; the GSD gloss after the quotations);
  labels and glance lines. No claim lost its marker.
* **Caps**: para > 100 3 → 0; item > 60 7 → 0; sentence > 45 12 → 4. Left: "We read that value …"
  (46 w; splitting it would separate the reading from "(inference)"), "Gate overlap" (46 w + label;
  its dash pair holds the reading and marker), "Without `ASTI` …" (47 w; the colon introduces the two
  consequences), "For SKY130's 0.15 µm drawn gate …" (47 w; a split at ", so" would leave half the
  claim outside "(our reading of the roadmap)").

### 066 BHI — done

* **Lead.** The guide's own R-SENTENCE example (`:16`) applied as written: the dash pair "— we infer
  that the two share the `NTM` resist, since … (see below) —" becomes the following sentence "We infer
  that the two share …", hedge first. The lead then splits into two paragraphs before "After the anneal
  at `TIPRTAD`" (what is done / what results). Lead 120 words (122 in the base); first sentence 15 words.
* **R-H3 not applied.** The passage after the figure is 75 words.
* **R-CATEGORY.** The 63-word classification sentence is split at its opening dash: "`BHI` is an Ion
  implantation step of the *channel-engineering* class." alone; the dash material becomes "It is a
  low-dose (10¹²–10¹³ cm⁻², typical)[^txt-01] boron implant at tens of keV, like …, but placed by
  geometry rather than by a mask." ("It is" added, R-SENTENCE step 7), then its colon clause as its own
  sentence ("The tilt puts it …"). The second sentence (dash before "the PDK publishes angles only …")
  is split at the dash, `[^pdk-03]` **repeated** on "… one whose SKY130 angle is not published" (the
  base marker covered the whole sentence; declared). Two statements about this step →
  `**Specific to this step:**` with two bullets.
* **R-PARA step 4 (Why items).** "Punch-through and threshold roll-off" (83 w): lead = the Wikipedia
  sentence, continuation from "Raising the doping uniformly …". "Reverse short-channel effect" (88 w):
  split at the semicolon after Rafferty; continuation "Machala et al. … A deliberately implanted halo
  …". "Lower channel doping elsewhere" (63 w): continuation from "Taur, Wann and Frank's …".
* **R-TABLE (measured against nominal).** The 155-word threshold paragraph: the test-tile values
  (7/8 µm, 7/0.15 µm, and W = 0.42 µm at L = 8–25, 0.5 and 0.15 µm) and the PDK's e-test nominals
  (7/8, 7/0.15 µm) become a `W/L (µm) | Test tile (V) | PDK e-test nominal (V)` table; the lead-in
  keeps "In the published test-tile measurements it is as below, and the PDK's e-test nominals rise the
  same way:" with both markers before the colon (R-TABLE step 3; new words "as below", as 053's
  "at the values below"); e-test cells the page does not give are `—`. The extraction hedge covered
  the test-tile values only; it goes directly under the table, word for word, as "(Test tile:
  maximum-transconductance … our extraction from the published measurements.)" (R-TABLE step 5; the
  two words "Test tile:" name the column it covers). The PMOS sentence and "A halo is one mechanism …"
  stay prose after the table, unchanged. The W/L notation is the page's own ("7/8 µm"); units moved to
  the headers after the first 400 px shot broke "0.53–0.54 V" and "8–25 µm" across lines. Pairings
  checked against the base: 7/8 ↔ 0.534 ↔ 0.541; 7/0.15 ↔ 0.707 ↔ 0.700; 0.42/8–25 ↔ 0.53–0.54;
  0.42/0.5 ↔ 0.60–0.64; 0.42/0.15 ↔ 0.72; the hedge keeps 0.1 and 100.
* **R-HEDGE.** Italic lead-in, word for word.
* **R-PARA step 4 (How items).** "Species and source" (87 w): continuation from "Indium is the heavier
  alternative"; its 51-word sentence split before ", so the absence" ("So the absence …", R-PARA step
  2). "Energy and dose" (83 w): split at the semicolon ("An AMD multi-threshold patent …"), and ", and a
  halo sits in the same range (inference)" becomes "A halo sits in the same range (inference)." so the
  hedge stays with its claim. "Tilt and rotation" (159 w): lead "Large tilts — 20–45° are typical — push
  the pocket under the gate edge."; continuation 1 from "The beam is shadowed …" (to Chen); continuation 2
  the "NTM shadowing" argument, its 82-word sentence split at the semicolon ("A halo at a much larger
  tilt …"); the single-operation estimate "(1.14 µm × tan 7° ≈ 0.14 µm)" stays inline (R-DERIVATION
  step 6). "Order relative to the tip" (78 w): lead "This reference describes the arsenic first.",
  the rest as the continuation.
* **R-TOOLS.** 8250: *SkyWater says:* the quotation; grades; the gloss "Boron and BF₂, … everything a
  halo needs." as the continuation paragraph. GSD: the head mixes SkyWater's quoted ranges with this
  reference's gloss ("batch tools that SkyWater lists with tilt and twist capability, so …") and cannot be
  separated at a seam (the quotations sit in parentheses on the tool name), so the pilot form: head kept
  whole, grades as sub-bullets, nothing under *SkyWater says:* (R-TOOLS step 2).
* **R-RELATED.** "The other halo:" → "Same module: the other halo, `LDBHI`; …" (colon → comma). The
  "Earlier channel engineering …; activation of the halo: …" bullet keeps its own wording (two
  relationships; neither is exactly an R-RELATED label).
* **R-OPENQ.** Labels "Species, energy, dose and tilt", "The "NTM shadowing" allowance", "Halo on the
  5 V NMOS", "PMOS halo"; text unchanged.
* **R-GLANCE.** Does keeps "our inference" for the shared resist and says "p-type pocket", not "boron"
  (the page calls boron this reference's description, industry-typical); Public numbers "none
  published for the halo" plus the e-test threshold rise `[^pdk-07]`; tool line the 8250's grades; Not
  public from Open questions 1.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03` (the category repeat), `pdk-07`,
  `skw-01` (glance); numbers 0.42×2 (the W/L cells repeat W = 0.42 µm on each of its three rows),
  0.541, 0.700, 8250 (glance), 5 (the OQ label "Halo on the 5 V NMOS", from the bullet's words); quote
  "NTM shadowing" (the OQ label, from the bullet's words); hedges "inference"×2, "not public" (glance).
  **LOST `number_order`** — the base's one test-tile sentence (0.534, 7, 8, 0.707, …, 0.1, 100) is
  now five table rows that put W/L first, plus the hedge line; pairings checked above. ADDED
  number_order: the five rows. Declared `--allow-added markers,numbers,quotes,hedges,number_order`;
  the LOST line is the only one left and is this table's transposition. Words the table replaces (from
  `worddiff.py`): "V at", "at L", "for L", "µm", "from … to", and one of the two "7/8 µm" and "7/0.15 µm"
  mentions (the test-tile and e-test values for the same geometry now share a row).
* **Marker coverage.** 17 flags, all read: the dash-pair move ("infer" now in the next sentence, as in
  the guide's example); the category repeat; split halves whose base marker belonged to the other clause
  (Lu/Rafferty – Machala; txt-01 – AMD patent; Large tilts – the beam; the NTM-shadowing estimate – the
  larger-tilt reasoning); "So the absence …" (our conclusion, no marker in the base); glance and label
  lines.
* **Caps**: para > 100 3 → 0; item > 60 8 → 0; sentence > 45 9 → 1. Left: the GSD head (48 w with the
  tool name; the pilot form keeps it whole).

### 067 ASTIS — done

* **Lead.** First sentence (40 w) split before ", and cleans the wafer" → "It cleans the wafer …"
  (R-GLANCE step 8, the form batch 4 used on 051/054); now 23 words. "…in the tip module; in this
  reference …" split at the semicolon. Lead 87 words, one paragraph.
* **R-H3 not applied.** The passage after the figure (136 words) is industry-typical and inferred
  (resist thickness "inferred on the NTM page", the dose "typical", the surface "we infer"); none of
  the four titles is true of it (R-H3 step 6). **R-PARA** split it before "The surface under the resist
  is, we infer, …" (the resist / the surface); that sentence split at its semicolon ("No metal is
  present, …"): "we infer" sat inside the first clause and stays there.
* **R-CATEGORY.** Classification sentence (19 w) alone. The rest is the category page's general account
  (implanted resist, Fujimura, "popping") and one comparison with other steps' strips: not "specific to
  this step" (R-CATEGORY step 2), so plain paragraphs. The 58-word account sentence split at its colon
  and before ", and, on the category page's account" ("On the category page's account, …"); each piece
  keeps its own marker (only the Fujimura clause had one).
* **R-PARA / R-SENTENCE (Why).** The 153-word paragraph split before "The crust also carries" (the next
  resist / what the crust carries). The HVNTM sentence split at its dash ("It is a film that …",
  subject + verb added). The flakes sentence: its dash pair (the patent quotation) becomes the following
  sentence "One patent has the implant-hardened surface "…".[^pat-strip-mosel]" (R-SENTENCE step 1),
  the marker with its quotation.
* **R-HEDGE.** Italic lead-in, word for word.
* **R-PARA step 4 (How items).** "Plasma ash, two stages" (185 w): lead "Downstream (remote) microwave or RF
  oxygen plasma."; continuation 1 the two-patent "Because …" sentence, its dash-pair quotation (a
  lowercase quotation from the same patent) given the neutral lead-in "The patent adds:" (R-SENTENCE
  step 7) and "until the crust is opened, after which …" as "The cool stage runs until …" (subject + verb
  added); continuation 2 Fujimura, Yegnasubramanian and SkyWater's asher list; continuation 3 "Downstream
  operation is used because …". "Wet strip and clean" (76 w): split at the semicolon; continuation from
  "SC-1 …".
* **R-TOOLS.** Four tools → `Tool | Evidence` recap table above the list (grades as the page gives them;
  the AIT row keeps "(our reading)"). Ashers: the head "— all named on SkyWater's facilities page with
  their gases and temperatures" is this reference's gloss of SkyWater's list, so the pilot form (as 051):
  head kept, *Tool exists:* and *Runs this step:*, and "The Iridia's H₂/N₂ chemistry … fit a cool first
  stage best." as the continuation paragraph. Akrion, DNS/FSI: heads keep the quotation with our
  "for the SPM/SC-1 sequence" / "as alternative clean tools", grade as sub-bullet. AIT: head keeps "our
  reading of "AIT" …", grade as sub-bullet (as 009).
* **R-RELATED.** "Companion strips in this module:" → "Same module: companion strips …" (HVASTIS,
  LDASTIS, and PDIS/NSDIS all carry this module's Phase cell).
* **R-OPENQ.** Labels "Ash recipe and wet sequence", "Oxide-thinning budget", "Which asher", "Tip dose";
  text unchanged.
* **R-GLANCE.** Does/Why from the lead and the Why section (the Why line drops the 40° figure rather than
  carry a number without its marker); Public numbers "none published for this strip" plus the next
  resist's 0.3 µm `[^pdk-03]`; tool line the ashers' grades; Not public from Open questions 1 and 3.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03`, `skw-01`, number 0.3, quote
  "Photoresist thickness for HV Tip Implants", hedges "inference" (glance), "not public" (glance label),
  "inference" and "our reading" (recap table). Declared `--allow-added markers,numbers,quotes,hedges`:
  clean.
* **Marker coverage.** 14 flags, all read: split halves whose base marker sat on another clause (the
  "popping" account; the flakes sentence; "The cool stage runs until …", which follows three quotation
  markers in the base and had none of its own; SPM / SC-1); glance and label lines.
* **Caps**: para > 100 3 → 0; item > 60 2 → 0; sentence > 45 6 → 0.

### 068 HVNTM — done

* **Lead.** The 48-word second sentence: its dash pair "— those built on the 110 Å thick gate oxide
  inside the `hvi` regions[^pdk-hv] —" becomes the following sentence "These transistors are those
  built on …[^pdk-hv]" (R-SENTENCE step 1; subject + verb added), marker with its clause. Lead 64 words;
  first sentence 9 words.
* **R-H3.** `### What the public record shows` after the figure caption, over the PDK mask, layer,
  rule and assumptions-page evidence (≈ 310 words, mostly public record, ending in "our arithmetic"
  and "we therefore read", as R-H3 step 6 allows).
* **R-PARA.** The 164-word paragraph split into "**Mask and layers.**" and "**Design rules.**" ("Its
  design rules" → "The layer's design rules", R-PARA step 5); the assumptions paragraph labelled
  "**Assumptions page.**" (evidence sequence, R-PARA step 3).
* **R-SENTENCE.** "… begin with "Hvntm can be drawn … CLDRC" — which we read as: …" split at the dash:
  "We read this as: …" ("which" → "this"); `[^pdk-periph]` **repeated** after the quotation, which it
  covered in the base (declared).
* **R-TABLE (design rules).** "The rules are coarse: width 0.700 µm (hvntm.1), … i.e. it is kept out of
  the SRAM core.[^pdk-periph]" → `Rule | Constrains | Value (µm)`, six rows in the base order, rule ids
  bare as the page writes them, the two quoted rules in the Constrains cell with `—` for the value,
  "i.e. it is kept out of the SRAM core" kept in hvntm.9's cell; `[^pdk-periph]` on the lead-in before
  the colon (R-TABLE step 3). Words dropped only where the cell structure replaces them ("by" before
  0.185 µm, "a … space" → "space"). Pairings checked: hvntm.1 width 0.700; hvntm.2 spacing 0.700;
  hvntm.3 enclosure 0.185; hvntm.4, hvntm.5 space 0.185; hvntm.10, hvntm.9 quoted.
* **R-TABLE (assumptions page).** The 83-word sentence listing nine entries from three PDK tables →
  `Table | Entry, as quoted | Value`, one row per entry in the base order, the table name on its first
  row (R-TABLE step 2), units per cell because the entries mix degrees and micrometres (R-TABLE step 4),
  "(against 1.14 µm for the standard resist)" kept in its row. Lead-in "Its tables give:[^pdk-03]"
  (the marker, which ended the enumerating sentence, before the colon).
* **R-DERIVATION.** "These numbers are mutually consistent: a 0.3 µm resist wall shadows a 40° beam for
  0.3 µm × tan 40° ≈ 0.25 µm, which less the 0.02 µm … gives the 0.232 µm figure (our arithmetic)."
  → a two-line numbered list, the page's own words per line, results in bold; "(Our arithmetic.)"
  closed as its own sentence after the list, then "We therefore read …" unchanged. The inputs are the
  table just above, so no second input table. No H3: the derivation is about 60 words, and R-H3 step 6
  allows an H3 only over ≥ 120 (see Guide problems). Arithmetic checked: 0.3 × tan 40° = 0.252 ≈ 0.25;
  0.252 − 0.02 = 0.232 ✓.
* **R-CATEGORY.** Classification sentence (47 w) split at its colon ("… type, with a twist." / "The resist
  is about a quarter …"); the remaining statements are about this step → `**Specific to this step:**`,
  two bullets; the second split at its semicolon.
* **R-PARA / R-SENTENCE / R-LIST (Why).** The 270-word paragraph split into five: the 1.8 V tip and hot
  carriers (its 60-word sentence split at the semicolon); "The classical remedies are:" → three plain
  bullets, each with its own marker (R-LIST; "and," dropped; no labels, batch-4 ruling); Rafí and
  Campabadal as prose after the list; the 40° angle and Table F2b (the 80-word sentence split into
  three: "…signature of exactly this kind of drain." / "The PDK's Table F2b marks …[^pdk-06]" / "So this
  is where …" / "How the implant is placed … is not stated."); the 20 V NMOS and hvntm.7 (split at the
  semicolon). The Cypress sentence (66 w) split at its semicolon.
* **R-HEDGE.** Italic lead-in, word for word.
* **R-PARA step 4.** "Resist coat" (80 w): continuation from "A thin film conforms …", split at its
  semicolon.
* **R-TOOLS.** As 064 (*SkyWater says:* "lists …", verb-first); three tools, no recap table.
* **R-RELATED.** "Sibling tip masks:" → "Same module: sibling tip masks …"; "Mask page:" → "Mask:".
* **R-OPENQ.** "20 V devices excluded" (93 w): the Table F2b lists as two sub-bullets, `[^pdk-06]` on the
  lead-in before the colon (it ended the enumeration), "See the HVNTM mask page. What the table does not
  say …" as the continuation, in the base order. "How "the CL" is derived" (87 w): split at its first
  semicolon; the continuation "The Error Messages page's checks …" ("the latter's" → the noun) and
  "The HVNTM mask page reads them.", `[^pdk-errors]` **repeated** on the checks sentence (declared).
  Labels "Resist chemistry", "Exposure tool" on the other two; text unchanged.
* **R-REPEAT not applied.** `repeat.py` finds a 10-word run shared by Why and Open questions (the Table
  F2b device list). The two lists are not the same sentence and differ (see Content problems: "3.3 V
  native" in Why, "3 V native" in Open questions); both kept.
* **R-GLANCE.** Does/Why without numbers (a number would need its marker); Public numbers 0.3 µm, 40°,
  23°, 0.232 µm `[^pdk-03]`; tool line; Not public from Open questions 2–4.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-periph`, `pdk-errors` (repeats above),
  `pdk-03`, `skw-01` (glance); numbers 0.232, 0.3, 23, 40, 1.8, 5 (glance), 20 (the OQ label, from the
  bullet's "20 V devices"); quotes "HVNTM shadowing" (glance), "the CL"×2 (glance and the OQ label, the
  bullet's own words); hedges "inference", "not public" (glance). **LOST `number_order`**: the rule
  sentence, now six rows with the rule id first; pairings checked above. Declared
  `--allow-added markers,numbers,quotes,hedges,number_order`; the LOST line is the only one left.
  Words the two tables replace (from `worddiff.py`): "by", "a", "µm" and the rule ids' repeated "hvntm"
  in the rule table; "Its … table gives" ×3 (the table names are the first column), "and", "an", "of"
  in the assumptions table.
* **Marker coverage.** 24 flags, all read: split halves whose base marker sat on another clause (the
  1.8 V tip / Hu; the remedies / Rafí; F2b / "So this is where …" and "How the implant is placed …",
  which had no marker of their own in the base; the 20 V NMOS / hvntm.7; Cypress / the inventor); the
  derivation lines ("our arithmetic" now closes the list); glance and label lines.
* **Caps**: para > 100 3 → 0; item > 60 3 → 0; sentence > 45 13 → 1. Left: "The Error Messages page's
  checks …" in Open questions (46 w; two quoted checks).

### 069 HVASTI — done

* **Lead.** The 63-word second sentence: its dash pair (the assumptions page's 40° and 23° with
  `[^pdk-03]`) becomes the following sentence "The PDK's assumptions page gives …[^pdk-03]"
  (R-SENTENCE step 1). Lead split into two paragraphs before "After `TIPRTAD` the result is …" (what
  is done / what results). Lead 114 words; first sentence 17.
* **R-H3 not applied.** The passage after the figure is 55 words. The only `{dropdown}` on the page is
  inside the generated index-links block, untouched.
* **R-CATEGORY.** Classification sentence (40 w; its dash pair holds the typical dose and its marker, no
  closing seam that leaves both halves whole) kept; the one remaining sentence becomes a second
  paragraph with no label (R-CATEGORY step 2).
* **R-PARA / R-SENTENCE (Why).** The 149-word paragraph split into three: the hot-carrier problem; the
  remedies (the 70-word "The LDD spreads …; Takeda's group …; and Hori's LATID …" split at its two
  semicolons, each piece with its own markers, "and" dropped); Rafí and King. The 131-word F2b paragraph:
  the 70-word sentence split at ", so this is where" ("So this is where …, all on the 110 Å
  oxide.[^pdk-hv]") and at the semicolon ("How the implant is placed … is not stated."); the 20 V NMOS
  sentence becomes its own paragraph. Same treatment as 068.
* **R-HEDGE.** Italic lead-in, word for word.
* **R-PARA step 4 (How items).** "Energy and dose" (65 w): split at the semicolon; continuation from "The
  dose sets …". "Tilt, twist and rotation" (155 w): lead "40° tilt with a 23° twist.[^pdk-03]";
  continuation 1 "We read the twist …" split at its colon ("With gates on a Manhattan grid, … (inference;
  …[^pdk-03]).": "We read" stays on the first piece and the parenthetical on the second) and "We further
  infer …"; continuation 2 "The lateral reach …" split at the semicolon and before ", and Chen et al."
  (each piece keeps its marker). "Resist" (102 w): continuation from "Outgassing scales …"; the dash
  pair (Lee and co-workers, `[^lee-1996]`) becomes the following sentence "Lee and co-workers
  characterised it …" so "(inference)" stays with its claim; the semicolons before "charging" and
  "platen cooling" become full stops.
* **R-TOOLS.** 8250: *SkyWater says:* the quotation; grades (the *Runs this step:* reason, "the only
  listed tool with a *stated* tilt range", points at SkyWater's list, which is above it); the gloss
  "Arsenic, a dose window …, and a tilt range that reaches 60° — the published 40° HV tip angle fits
  inside it." as the continuation. GSD: pilot form, as 066.
* **R-RELATED.** "The other tips:" → "Same module: the other tips …". The thick-oxide/drift-well bullet
  and "Activation: …" keep their own wording.
* **R-OPENQ.** "Energy and dose", "Rotations and twist"; "20 V devices excluded" (93 w) as on 068; "A 5 V
  PMOS p-tip" (64 w): the dash pair (the PDK evidence, three markers) becomes the continuation paragraph
  after the question "Whether the 5 V PMOS has a corresponding tilted p-tip is not stated publicly; this
  reference describes none." (R-OPENQ step 2: the lead keeps the question and its hedge).
* **R-REPEAT not applied**, as on 068 (the Table F2b lists in Why and Open questions differ: "3.3 V" /
  "3 V" native NMOS; see Content problems).
* **R-GLANCE.** Does/Why from the lead and Why (no unmarked numbers); Public numbers 40°, 23°, 0.3 µm,
  0.232 µm `[^pdk-03]`; tool line the 8250's grades; Not public from Open questions 1–2.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03`, `skw-01`, numbers 0.232, 0.3, 23,
  40, 8250, 5×2, quote "HVNTM shadowing", hedges "inference", "not public" — the glance box; numbers 5
  and 20 from the OQ labels ("A 5 V PMOS p-tip", "20 V devices excluded", the bullets' own words).
  Declared `--allow-added markers,numbers,quotes,hedges`: clean.
* **Marker coverage.** 26 flags, all read: split pieces each keeping the markers of their own clauses
  (the remedies, the F2b pieces, the lateral-reach pieces, the resist pieces, the moved Lee sentence);
  "How the implant is placed … is not stated." had no marker in the base; glance and labels.
* **Caps**: para > 100 3 → 0; item > 60 6 → 0; sentence > 45 9 → 2. Left: "At 5.5 V on the drain, …
  — the degradation mechanism Hu and co-workers modelled …[^hu-1985-hci]" (49 w; the only seam would
  leave the physics claim without the marker that covered the whole sentence) and Hori's LATID sentence
  (50 w; no seam).

### 070 HVASTIS — done

* **Lead.** First sentence (31 w) split before ", and cleans the wafer" → "It cleans the wafer …" (R-GLANCE
  step 8); now 17 words. Lead 41 words.
* **R-LIST.** "Two things distinguish it from `ASTIS`. The resist is thin — … — and the implant it has absorbed
  is, we infer …" → lead-in with a colon and two plain bullets (the second item offers no 2–4-word label
  of its own; batch-4 ruling), every word kept except the joining "and"; `[^pdk-03]` ends the first
  item, where the dash pair's closing dash stood; "we infer" and `[^txt-04]` stay in the second.
  "The crust is correspondingly thinner and the strip easier." stays as prose after the list (R-LIST
  step 4).
* **R-PARA / R-SENTENCE.** The 161-word paragraph: list, then the crust/40° paragraph, then "The surface
  under the resist is, we infer, …" as its own paragraph. The 59-word 40° sentence split at ", and we read"
  ("We read the PDK's 0.02 µm … (inference)."); "(inference)" governed that clause only.
* **R-CATEGORY.** Classification sentence (49 w) split at its colon ("… of medium difficulty."); the two
  remaining statements describe this step → `**Specific to this step:**` and two bullets.
* **R-PARA / R-SENTENCE (Why).** The 109-word paragraph split before "A thin implanted resist has its own
  failure mode"; its 62-word sentence split at the colon ("If the ash is tuned …") and at the dash ("That
  is one reason downstream (charge-free) ashing is preferred …[^wiki-ash]", subject + verb added); the
  marker stays with the downstream-ashing claim it supported.
* **R-HEDGE.** Italic lead-in, word for word.
* **R-PARA step 4.** "Plasma ash" (121 w): lead = the Fujimura sentence; continuation 1 the two-stage
  sentence; continuation 2 Horsky/Roche and SkyWater's asher list. "Wet strip and clean": the 46-word
  sentence split at its semicolon ("SkyWater's Akrion Gamma bench lists …").
* **R-TOOLS.** As 067: recap table (four tools), pilot-form heads (the asher head "— named on SkyWater's
  facilities page …" is our gloss), grades as sub-bullets.
* **R-RELATED.** "Companion strips:" → "Same module: companion strips …".
* **R-OPENQ.** Labels "Ash recipe", "HV tip dose", "Which asher and wet bench"; text unchanged.
* **R-GLANCE.** Does/Why from the lead and Why; Public numbers "none published for this strip" plus the
  0.3 µm resist `[^pdk-03]`; tool line the ashers' grades; Not public from Open questions 1 and 3.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03`, `skw-01`, number 0.3, hedges
  "inference", "not public" (glance); "inference", "our reading" (recap table). Declared
  `--allow-added markers,numbers,hedges`: clean.
* **Marker coverage.** 14 flags, all read: the list items (each keeps its own marker); the failure-mode
  pieces (the base marker covered only the downstream-ashing claim, which keeps it); the SPM / Akrion
  split; glance and labels.
* **Caps**: para > 100 2 → 0; item > 60 1 → 0; sentence > 45 5 → 0.

### 071 LDNTM — done

* **In-force notes.** The page has two hand-written `{dropdown}` notes (Why this step exists; References)
  and one inside the generated block. None was edited: `invariants.py` confirms every dropdown block
  byte-identical, and `check_inforce.py` passes. The paragraph the Why note belongs to stays directly
  above it; inside that paragraph only its 70-word sentence was split at the semicolon ("Cypress's
  embedded-SONOS patents, which may still be in force, describe the cell in the collapsed note below,
  …"), wording unchanged; nothing from the note appears elsewhere (glance box included).
* **Lead.** Unchanged (84 words; first sentence 11).
* **R-H3.** `### What the public record shows` after the figure caption, over the PDK mask, layer,
  Error Messages and assumptions-page evidence (≈ 200 words; ends in one hedged reading, "(inference)").
* **R-PARA.** Labels "**Mask and layers.**", "**Core checks.**", "**Tip angle.**" (evidence sequence).
  "The public periphery rule set contains no `ldntm` rules;[^pdk-periph] the PDK's *Error Messages* page,
  however, …" split at the semicolon.
* **R-LIST.** The six quoted core checks ("… `ldntm.c1` to `ldntm.c6`: "…", … and "…".[^pdk-errors]")
  → lead-in with the marker before the colon (it ended the enumeration; R-LIST step 1 / R-TABLE step 3)
  and six plain bullets, each quotation unchanged (the double space inside "must be more than  0.180"
  kept). Not a `Rule | …` table: the page does not pair each id with a check.
* **R-CATEGORY.** Classification sentence (21 w) alone; two statements about this step →
  `**Specific to this step:**`, two bullets.
* **R-LIST / R-SENTENCE (Why).** The 117-word e-test sentence ("… describe it at drawn W/L …; its
  programme and erase conditions apply …; and it must keep its window over 100 000 cycles.[^pdk-07]")
  → lead-in "The PDK's e-test parameters describe it:[^pdk-07]" (the marker, which ended the enumeration,
  before the colon) and three plain bullets, "and" dropped. The 40-word mid-sentence parenthetical on
  the "-38" source voltage ("we read it as −3.8 V …") moves, unchanged, to the end of its own sentence
  and is closed as "(The PDK's table prints … junction limits.)" (R-SENTENCE steps 2 and 7), as an
  indented continuation of that bullet. This moves "-38" and its "−3.8" after the erase voltages, so
  `check_preserved` reports a **LOST `number_order`** on that sentence; every value and pairing is
  unchanged (programme: gate +6.7 V, source/drain/body −3.8 V; erase: gate −3.8 V, the other three
  +6.7 V; "-38" read as −3.8 V).
* **R-PARA step 4.** "Junction voltage" (101 w): continuation from "A heavily doped, abrupt tip …".
  "Charge-trapping reliability" (62 w): split at its semicolon; continuation from "Any hot-carrier
  injection …".
* **R-HEDGE.** Italic lead-in, word for word.
* **R-TOOLS.** As 064/068.
* **R-RELATED.** "Sibling tip masks:" → "Same module: sibling tip masks …"; "Mask page:" → "Mask:".
* **R-OPENQ.** "Select transistor" (83 w): lead = the question; continuation "The Error Messages page …
  without naming the device.[^pdk-errors] Table F2b … "NV SONOS Diode".[^pdk-06] On our reading these
  may include the select transistor, but neither source says so." (split at ", and Table F2b" and at the
  semicolon; each piece keeps its own marker; the hedge stays with its claim). Labels "Resist thickness
  and tilt", "Why lightly doped", "Exposure tool"; text unchanged. One line re-wrapped so that the
  `{term}` role and a code span do not share a line (the known G15 false positive in `check_preserved`).
* **R-GLANCE.** Does from the lead; Why hedged "on our reading of the cell's published voltages" (Open
  questions 3 says the reasoning is our reading); Public numbers the two 0.7 core checks
  `[^pdk-errors]`; tool line; Not public from Open questions 1–2. Nothing from either in-force note.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-errors`, `skw-01`, numbers 0.7×2,
  quotes "0.7 min. width of ldntmCore", "0.7 min. spacing/notch of ldntmCore", hedges "inference", "not
  public", "our reading" — all the glance box. LOST `number_order` as above. Declared
  `--allow-added markers,numbers,quotes,hedges,number_order`; the LOST line is the only one left.
* **Marker coverage.** 17 flags, all read: the list lead-ins (markers before the colon, by rule); the
  split pieces (periphery rules / Error Messages; bottom oxide / hot carriers; Error Messages / Table F2b
  / our reading), each with its own marker; the paragraph before the note (flagged only because the
  script sees the note's markers as its neighbours); glance and labels.
* **Caps**: para > 100 2 → 0; item > 60 3 → 0; sentence > 45 5 → 0.

### 072 LDASTI — done

* **In-force note.** One hand-written `{dropdown}` (in References) and one in the generated block; both
  byte-identical (`invariants.py`), `check_inforce.py` passes, nothing from the note is used elsewhere.
* **Lead.** First sentence (45 w) split at its first colon: "`LDASTI` is the *lightly doped* arsenic tip
  implant of the SONOS memory transistors." (13 w) / "It is the counterpart of `ASTI` made through the
  `LDNTM` resist, at a dose that is, we infer, lower …: the PDK calls the mask …[^pdk-06]" ("It is"
  added; "we infer" and the marker stay in their sentence). Lead (101 w) split into two paragraphs
  before "Arsenic ions enter …" (what the step is / what it does in the silicon).
* **R-H3 not applied.** The passage after the figure is 45 words.
* **R-CATEGORY.** The classification sentence (after "small tilt") split at its dash: "… of the *LDD*
  class: low energy, moderate dose, small tilt." (17 w); the dash material "The PDK's 7° "Angle for tip
  implant"[^pdk-03] applies, we infer, to this tip as to the standard one." and "It is the module's
  smallest implant by area, …" describe this step → `**Specific to this step:**`, two bullets. The "we
  infer" stays in its sentence, word for word (see Content problems: the S6 figure agent's note on this
  sentence against Open questions).
* **R-SENTENCE / R-PARA (Why).** The 76-word first sentence split at its colon ("The reasons are set out
  on the `LDNTM` page. The SONOS memory transistor's junctions … (…).[^pdk-07]") and at ", so a heavily
  doped" ("So a heavily doped abrupt tip … argument.[^ogura-1980]"); each piece keeps its own marker.
  Paragraph split before "The trade-off is …". The 54-word arsenic sentence split at its semicolon.
* **R-HEDGE.** Italic lead-in, word for word.
* **R-PARA step 4 (How items).** "Dose" (77 w, a 60-word sentence): lead "Of order 10¹³ cm⁻² (typical of an
  LDD).[^txt-04]"; the continuation "It is below the room-temperature amorphisation threshold … (typical
  value).[^rev-05][^txt-01]" ("It is" added to the verbless clause); the dash-pair quotation "— above
  which "the amount … surface"[^wiki-implant] —" becomes "Above that threshold, "the amount … surface".
  [^wiki-implant]" ("which" → "that threshold", R-PARA step 5; the quotation unchanged, still after a
  comma); "So, unlike `ASTI`, the silicon stays crystalline …" (the split R-PARA step 2 allows at "—
  so"). "Screen" (49-word sentence): split at its semicolon ("Which is the case is not public …").
* **R-TOOLS.** 8250: *SkyWater says:* the quotation; grades; the gloss "An LDD-class arsenic dose sits
  inside its quoted window, and its 3 keV floor[^axcelis-8250] covers a shallow tip." as the
  continuation. GSD: pilot form, as 066.
* **R-RELATED.** "The other tips:" → "Same module: the other tips …".
* **R-OPENQ.** Labels "Energy and dose", "Dielectric over the source/drain", "Tilt and rotations",
  "Select transistor"; text unchanged.
* **R-GLANCE.** Does from the lead; Why from the Why section's "So a heavily doped abrupt tip …, while a
  lightly doped, graded junction keeps the peak field low"; Public numbers "none published for SKY130"
  plus the "N Tip (As)" species row `[^pdk-03]` (as 065); tool line; Not public from Open questions 1–3.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03`, `skw-01`, number 8250, quote "N Tip
  (As)", hedges "inference", "not public", identifier SKY130 — all the glance box. Declared
  `--allow-added markers,numbers,quotes,hedges,identifiers`: clean.
* **Marker coverage.** 21 flags, all read: split pieces each keeping their own markers (the Why pieces;
  the arsenic pieces; the Dose pieces — "So, unlike `ASTI`, …" had no marker of its own in the base);
  the category bullets; glance and labels.
* **Caps**: para > 100 1 → 0; item > 60 2 → 0; sentence > 45 4 → 0.

### 073 LDBHI — done

* **Lead.** First sentence (30 w) split at its dash: "`LDBHI` is the boron halo implant of the SONOS
  memory transistors." (11 w) / "It is the counterpart of `BHI` made through …" ("It is" added). Lead 95
  words.
* **R-LIST (after the figure).** The 46-word "What distinguishes this halo … is its host: a transistor
  whose channel …, whose gate …, and whose tip is lightly doped and, we infer, non-amorphising (…)."
  → lead-in "… is its host, a transistor:" and three plain "whose …" bullets, every word kept except the
  joining "and"; "we infer" stays in its bullet. No H3 (the passage is 60 words).
* **R-CATEGORY.** The classification sentence (37 w) split at its dash pair: "`LDBHI` is an Ion
  implantation step of the *channel-engineering* class, placed by the gate geometry rather than by a
  mask edge." (21 w); the dash material becomes "It is boron at tens of keV and 10¹²–10¹³ cm⁻²
  (typical)[^txt-01] at a tilt." ("It is" added); with "It is the second of the two halo implants …" →
  `**Specific to this step:**`, two bullets.
* **R-PARA step 4 (Why items).** "Its tip is lightly doped" (55-word sentence): split at the semicolon
  ("Without a pocket …[^pdk-07]"; the marker supported the gate lengths in that clause). "Its surface
  channel must stay lightly doped" (97 w): the Cypress sentence split before ", and the cell's depletion
  implant"; continuation from "The cell's depletion implant …". The item's lead stays one 46-word
  sentence (a two-quotation statement with no seam outside the quotations).
* **R-HEDGE.** Italic lead-in, word for word.
* **R-PARA step 4 (How items).** "Energy and dose" as on 066 (the semicolon; "A halo sits in the same range
  (inference)."). "Channelling" (81 w): continuation from "Its damage is sub-amorphising …"; its first
  sentence (45 w, a semicolon before a marker that covered both clauses) kept whole.
* **R-TOOLS.** 8250: *SkyWater says:*, grades, the fragment "Boron and BF₂, the halo dose window and a
  tilt range to 60°." as the continuation (our gloss). GSD: pilot form (the head quotes "tilt/twist"
  inside our gloss).
* **R-RELATED.** "The logic halo: BHI; the memory transistor's other channel implants: PTSI, DEPI" names
  two relationships, so it becomes two bullets: "Same module: the logic halo, `BHI`." and "The memory
  transistor's other channel implants: …" (unlabelled: PTSI/DEPI are in another module).
* **R-OPENQ.** Labels "Species, energy, dose and tilt", "Crystalline surface", "Select transistor",
  "Threshold targets"; text unchanged.
* **R-GLANCE.** Does/Why from the lead and the first Why bullet; Public numbers "none published for the
  halo" plus the cell variants' 0.15–0.22 µm gate lengths `[^pdk-07]`; tool line; Not public from Open
  questions 1.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-07`, `skw-01`, numbers 0.15–0.22,
  8250, hedges "inference", "not public" — the glance box. Declared `--allow-added markers,numbers,hedges`:
  clean.
* **Marker coverage.** 12 flags, all read: split pieces whose base marker belonged to the other clause
  (the depletion-tail physics / the gate lengths; Cypress / the depletion implant; txt-01 / the AMD
  patent); the host list (no markers in the base); glance and labels.
* **Caps**: para > 100 0 → 0; item > 60 3 → 0; sentence > 45 4 → 1 (the Cypress lead, above).

### 074 LDASTIS — done

* **Lead.** First sentence (32 w) split before ", and cleans the wafer" ("It cleans the wafer."); now 27
  words. Lead 66 words.
* **R-SENTENCE.** After the figure: the 47-word resist sentence split at ", and it has received" ("It has
  received a moderate arsenic dose …"); "we infer" governed the first clause only. No H3 (72 words).
* **R-CATEGORY.** Classification sentence (22 w) alone. The rest is the category page's general
  statement and one sentence about this step ("Here the extra care goes into the wet clean, …"), split
  at its semicolon: one specific sentence, so a plain second paragraph (R-CATEGORY step 2).
* **R-LIST (Why).** "Two reasons, one ordinary and one specific to its position." announces a count and
  its two paragraphs already begin "The ordinary one:" / "The specific one:" → the announcing sentence
  ends in a colon and the two paragraphs become bullets with those words bolded in place (R-LIST step 3).
  "The specific one" (95 w): lead split before ", and any metallic contamination" ("Any metallic
  contamination …"), continuation paragraph. "metal-⏎removing" and "arsenic-⏎bearing" (hard-wrapped
  after the hyphen, so they rendered as "metal- removing" and "arsenic- bearing") are joined; spacing
  only.
* **R-HEDGE.** Italic lead-in, word for word.
* **R-PARA step 4.** "Plasma ash" (88 w): split at its first semicolon; continuation from "A cooler first
  stage …". "Pre-anneal clean" (72 w): split at the semicolon after Kern; continuation from "SkyWater's
  DNS bench …".
* **R-TOOLS.** As 067/070: recap table (four tools, grades as the page gives them), pilot-form heads,
  grades as sub-bullets; DNS/FSI keeps its gloss "— the tools with the SC-2 chemistry …" in the head,
  with both grades below.
* **R-RELATED.** "Companion strips: ASTIS, HVASTIS; the earlier pre-anneal clean: PWDEIS" names two
  relationships → "Same module: companion strips …" and "Same category: the earlier pre-anneal clean,
  `PWDEIS`." (a strip/clean step elsewhere in the flow).
* **R-OPENQ.** Labels "Ash recipe and wet sequence", "Which asher and wet bench", "Queue time"; text
  unchanged.
* **R-GLANCE.** Does/Why from the lead and "The specific one"; Public numbers "none published for
  SKY130" (the only thickness on the page, ~1 µm, is "we infer"); tool line the ashers' grades; Not public
  from Open questions 1 and 3.
* **Preservation** (`--allow-regrouped` only): ADDED marker `skw-01`, hedges "inference", "not public",
  identifier SKY130 (glance); "inference"×2, "our reading" (recap table). Declared
  `--allow-added markers,hedges,identifiers`: clean.
* **Marker coverage.** 11 flags, all read: split pieces each keeping their own markers (the resist /
  dose; the anneal / metal contamination, which had no marker of its own in the base; the ash pieces;
  SC-1/SC-2 / DNS); glance and labels.
* **Caps**: para > 100 0 → 0; item > 60 2 → 0; sentence > 45 3 → 0.

### 075 TIPRTAD — done

* **Lead.** The 162-word one-paragraph lead: its 55-word sentence "`TIPRTAD` heats the wafer — in an
  inert ambient for seconds on the industry-typical recipe described below; SKY130's own conditions are
  not public — to a temperature high enough to …" becomes "`TIPRTAD` heats the wafer to a temperature
  high enough to …, while moving the junctions as little as possible. It does so in an inert ambient for
  seconds on the industry-typical recipe described below; SKY130's own conditions are not public."
  (R-SENTENCE step 1; "It does so" is the added subject and verb; the hedge moves with its clause, word
  for word). The lead is split into **three** paragraphs (what arrives; what the anneal does, with its
  hedge; the RTA evidence and what follows). Two paragraphs would leave one at 107–114 words, over the
  100-word paragraph cap; the base lead is 162 words, over §1's 120, so the two-paragraph target cannot
  be met without dropping words (see Guide problems). First sentence 11 words.
* **R-H3 not applied.** The passage after the figure is 30 words.
* **R-CATEGORY.** Classification sentence (35 w, its dash pair kept) alone; the category page's account
  (general, not specific to this step) as a plain second paragraph, its 55-word sentence split at the
  semicolon ("The resolution "is the RTA: …"".[^stolk-1997]); `[^stolk-1997]` **repeated** after the TED
  quotation, which it covered in the base (declared).
* **R-PARA step 4 (Why items).** "Activation and regrowth" (81 w): lead split at the semicolon; the arsenic
  sentence split before ", and the boron halos" ("The boron halos … need 800–1000 °C-class
  temperatures …[^gibbons-1972]"), each piece with its own marker. "Junction position" (163 w): lead =
  the ITRS values with `[^itrs-01]` **repeated** (split at the semicolon; declared); continuation 1 "Its
  rule Xj = 0.55 × physical gate length would put SKY130's tip nearer 80 nm … (our reading; …)" (a
  single-operation estimate, inline, R-DERIVATION step 6; the hedge stays with it) and the PDK sentence;
  continuation 2 the halo-boron TED, Agarwal, Shishiguchi and Jones/Ishida. "Before the spacer" (78 w):
  continuation from "Unannealed tips and halos …".
* **R-HEDGE.** Italic lead-in, word for word.
* **R-PARA step 4 (How items).** "Tool and ambient" (73 w): split at the semicolon; continuation from
  "RTP "heats …"". "Temperature and time" (62 w): split at the semicolon; continuation from "Agarwal's
  spike-anneal study …". Two lines re-wrapped as in the base ("1 – 180°C" on one line; "400 –" at a line
  end) because `check_preserved` reads an en-dash range on one line as one token and reported a LOST /
  ADDED number pair for the same text.
* **R-TOOLS.** Heatpulse 8808: *SkyWater says:* "facilities page lists under RTA "…"" (the 034 form);
  *Tool exists:*, *Runs this step:* (the reason refers to "the only RTA on the list", which is above it);
  the gloss "— a single-wafer lamp RTA with the inert ambients and the temperature reach an extension
  anneal needs" as the continuation "It is a single-wafer lamp RTA …" ("It is" added); the reseller
  sentence (73 w) split at its semicolon into two continuation sentences, each with its own marker.
  Aviza: pilot form (the head's quotations and our "an unlikely home for a tip anneal" are one sentence).
  Two tools: no recap table.
* **R-RELATED.** "Other RTAs:" → "Same category: other RTAs, …" (Anneal category). "Anneals the tips and
  halos of …" keeps its wording.
* **R-OPENQ.** Labels "Anneal conditions", "Heatpulse 8808 assignment", "Screen oxide", "Heatpulse 8808
  figures"; text unchanged.
* **R-GLANCE.** Does/Why from the lead and "Before the spacer"; Public numbers "none published for
  SKY130" (the lead and Open questions say the conditions are not public); tool line; Not public from
  Open questions 1.
* **Preservation** (`--allow-regrouped` only): ADDED markers `itrs-01`, `stolk-1997` (repeats above),
  `skw-01` (glance); numbers 8808 (glance and the two OQ labels, the bullets' own words); hedges
  "inference", "not public" and identifier SKY130 (glance). Declared
  `--allow-added markers,numbers,hedges,identifiers`: clean.
* **Marker coverage.** 18 flags, all read: split pieces each keeping their own markers (the category
  quotations; the activation pieces; ITRS / the rule; the ambient / RTP quotation, where the first
  clause is the industry-generic description under the italic scope sentence; temperature / Agarwal; the
  two reseller sentences); glance and labels.
* **Caps**: para > 100 1 → 0; item > 60 6 → 0; sentence > 45 6 → 0.

## Content problems for the owner (not fixed)

* `068-hvntm.md` and `069-hvasti.md`: the Table F2b device list in *Why this step exists* reads "the 5 V
  and 3.3 V native NMOS … the ESD NMOS built on it … four HV diodes, an HV n-diffusion resistor and an HV
  varactor", while the Open questions bullet on the same page reads "the 5 V and 3 V native NMOS … the HV
  and HV native ESD NMOS … four n-type diodes". Both kept verbatim (this is also why R-REPEAT was not
  applied to the shared 10-word run).
* `072-ldasti.md` (the S6 figure agent's note): the category sentence says the PDK's 7° tip angle
  "applies, we infer, to this tip as to the standard one"; *How it is typically performed* says "7° (PDK
  tip angle), with twist; two or four rotations, or 0°, for symmetry — not public"; Open questions says
  "Whether the implant is at 7° with rotations or at 0° is not public." Consistent, but the category
  sentence reads more certain than the rest. All three kept verbatim; the category sentence is now the
  first "Specific to this step" bullet, word for word.
* `070-hvastis.md`: two consecutive sentences state the same conclusion, first as fact ("so the resist
  sidewalls facing the beam have been implanted along their whole height") and then as an inference
  ("so the sidewalls facing the beam are implanted through their whole height (inference)"). Kept
  verbatim (they were one sentence in the base; the split at ", and we read" left each clause with its
  own wording).
* `072-ldasti.md` against `071-ldntm.md` (review C2): 072's *Why this step exists* states the
  leakage argument unhedged ("So a heavily doped abrupt tip at the gate edge would leak by band-to-band
  tunnelling and inject unwanted charge into the nitride, …"), while 071's Open questions calls the same
  junction-leakage and disturb argument "our reading of the cell's published operating voltages; no
  public source states why the SONOS tip is lightly doped". 071's glance box carries the hedge; 072's
  body does not. Both kept verbatim; the owner should decide whether 072's Why wants "on this
  reference's reading".
* Figure captions (generated) were not touched. Of the S6 figure agent's other points (field-oxide step,
  halo colour, 079 lead, no PMOS in the slice) none concerns a page in this batch.
* Arithmetic re-checked while copying, all consistent: 064 k₁ = 0.7 × 0.6 / 0.365 ≈ 1.15 ("≈ 1.2"); 065
  0.38 µm × tan 7° ≈ 47 nm; 066 1.14 µm × tan 7° ≈ 0.14 µm; 068 0.3 µm × tan 40° ≈ 0.25 µm, less 0.02 µm
  ≈ 0.232 µm.

## Guide problems

1. **R-DERIVATION step 1 against R-H3 step 6.** R-DERIVATION always asks for an H3 `How <quantity> is
   estimated`; R-H3 allows an H3 only over ≥ 120 words. 068's derivation (two lines, about 60 words, its
   inputs in the table just above) got a numbered list and no H3. The guide could say that a derivation
   under 120 words takes the list without the H3.
2. **Lead: ≤ 2 paragraphs against the 100-word paragraph cap.** When the base lead is well over 120 words
   (075: 162), two paragraphs leave one over 100 words; 075 uses three. The guide could say which limit
   wins.
3. **`check_preserved.py` and line wrapping.** An en-dash range written with spaces ("400 – 1200°C") is
   read as one number when it sits on one line and as two when a line break falls inside it, so a re-wrap
   gives a false LOST/ADDED pair (075; fixed here by wrapping as the base did). G15 (a role followed by a
   code span on the same line) is still present (071; avoided by re-wrapping).
4. **`check_preserved.py` does not see dropped words** that carry no number, quotation, marker, hedge,
   role or identifier. A first draft of 074 lost "removing step:" through an overlapping replacement and
   every check passed; `tmp/readability/worddiff.py` (a word-level difference against the base, glance
   box and recap table excluded) caught it. A word-level mode in the tool would close this gap.
5. **R-TOOLS: a gloss the grade rests on but does not name.** The batch followed 050 (the gloss as the
   continuation paragraph below the grades) where the grade's reason does not refer to the gloss by name
   (065, 066, 069, 072, 073, 075), and the pilot form where the gloss and SkyWater's quotation are one
   sentence (066, 069, 072, 073 GSD; 067, 070, 074 ashers; 075 Aviza). The guide could say so.
6. **R-OPENQ step 2 when the question comes last.** The Table F2b bullets on 068/069 give the evidence
   first and the question last; the batch kept that order (label, evidence as sub-bullets, question in
   the continuation) rather than moving the question into the lead.

## Review fix round (review `rd-steps-064-075`, 2026-09-26: 0 High, 1 Medium, 9 Low)

One commit each.

* **M1.** Pronouns given their nouns back (R-PARA step 5): 073 "Its damage" → "The halo's damage" (under
  **Channelling.** the pronoun read as channelling's); 075 "Its rule Xj" → "The roadmap's rule Xj"; 069
  "characterised it" → "characterised resist outgassing" (after the Lee dash pair moved, "it" pointed at
  the resist film). Paragraphs re-wrapped; `check_preserved` output unchanged on all three pages.
* **L1, 067.** "The patent adds:" → "The second patent adds:" (the sentence before quotes two patents; the
  quotation is `pat-strip-mosel`'s, the second one named). `check_preserved` output unchanged.
* **L2, glance wording.** 065 "Axcelis 8250 weak" → "Axcelis 8250 weak (assignment)" (its existence is
  graded strong on the page); 070 "the next mask is coated here" → "coated on this surface" (the page's
  words); 075 "with little junction movement" → "while moving the junctions as little as possible" (the
  lead's words: an aim, not a result). All bullets ≤ 25 words; `check_preserved` output unchanged.
* **L3, 069.** The 49-word Hu sentence split at its dash: "… inject hot electrons into the gate
  oxide.[^hu-1985-hci] That is the degradation mechanism Hu and co-workers modelled, …[^hu-1985-hci]"
  (subject + verb added; `[^hu-1985-hci]` **repeated**, declared — `check_preserved` now adds
  `hu-1985-hci` to 069's ADDED markers, nothing else changes).
* **069:79, Hori's LATID (50 w): left as it is**, as the review rules borderline: the only split, at ",
  instead of under the spacer", needs a new subject and a repeated marker for a contrast that is one
  claim.
* **L6, 070 `[^wiki-ash]` scope — checked against the source, no change.** The current Wikipedia
  *Plasma ashing* article (wikitext fetched once, 2026-09-26, with the project's user agent) says that
  ions formed in an in-chamber plasma "could damage the wafer" and that a downstream configuration
  "prevents damage to the wafer surface"; it mentions implanted resist becoming "resistant to
  oxidizing". It says nothing about a thin film being over-ashed when the recipe is tuned for a thick
  one, nor about screen oxide, gate-oxide edges or poly sidewalls seeing the plasma for longer. So the
  marker supports "That is one reason downstream (charge-free) ashing is preferred over direct plasma
  exposure once gates exist.", where it stands, and not the over-ashing sentence; repeating it there would
  attribute to Wikipedia a claim it does not make. The over-ashing sentence is this reference's own
  reasoning and had no separate marker in the base either.

## For the tool branch (review D3, D4; the tool is not edited here)

* **D3, `check_preserved.py` and line wrapping.** "Flatten whitespace (newlines and runs of spaces to one
  space) before the number tokenizer runs, so that `400 –\n1200°C` and `400 – 1200°C` yield the same
  tokens. Add a self-test pair that differs only in where the line breaks. G15 (a role and a code span on
  one line) is still open from batch 3; the same flattening test should cover it." Guide §7 step 4, once
  the coordinator adds it: "A LOST/ADDED pair whose text is identical once wrapping is ignored is the
  tool's; re-wrap as the base did and say so in the progress file."
* **D4, `check_preserved.py` does not see dropped words.** "Add `--words`: a multiset diff of word tokens
  outside the glance box, recap table, References and footnote definitions. Print every lost word with
  40 characters of base context. Accept an allowlist file of structural words (`Strength`, `Mask page`,
  joining `and`/`which`, case changes at a split)." Guide §8 and §7 step 4, once the coordinator adds it:
  "Run `check_preserved.py --words` (until it exists, a word-multiset diff) and account for every lost
  word in the progress file."
* **Guide rulings applied in this branch** (one commit each, wording as the review gives it): D1
  R-DERIVATION step 1; D2 the §4.1 lead footnote; D5 R-TOOLS step 2; D6 R-OPENQ step 2; D7 R-PARA step 2.
