# Progress — readability batch 7a, steps 089–097 (`topic/rd-steps-089-097`)

Writer: Opus. Started 2026-09-26 from `main` at `e369d634`. A half-size batch (quota near the weekly
cap). Guide: `docs/plans/readability-guide.md` §1, §2, §4.1, §5, §6, §7, §8, with the rulings of
batches 4–6 (plain bullets over invented labels; no H3 where none of the four titles fits; R-CATEGORY's
35 words a target; the connective rule inside list items; derivations under 120 words as a numbered
list without an H3; a third lead paragraph only for base leads over 120 words; "Because X, Y" is not a
connective opener; rows differing in unit carry the unit in each cell). Medium classes avoided (batch
4–6 reviews): a pronoun whose referent changes after a split; a marker lost when dash material moves; a
sentence moved below the grade that refers to it; glance wording that does not say what it grades.
Model pages: 078, 083. One commit per page.

## Method, every page

* Baseline build and one desktop tile set per page before any edit (`tmp/shots/*-before*`,
  git-ignored); one final pair (1280 px, `--max-height 40000`; 400 px, `--max-height 60000`) after.
* Preservation: `uv run python tools/check_preserved.py --base HEAD --allow-regrouped <page>` against
  the commit before the page, no other flag; never `--allow-added`, never `--allow-dropdown-edits`.
  Every ADDED line is named in the page entry; every REGROUPED line read; every `WORDS LOST` word
  accounted for; `--strict-words` as the final run.
* Marker coverage: `tmp/readability/rdtools.py cov` (git-ignored scratch script) pairs every sentence
  not verbatim in the base with its closest base sentence and flags any marker or hedge word the base
  sentence had and the new one lacks; splits at semicolons and colons are split points too. Every flag
  read; the page entry says what each class is.
* Invariants: `rdtools.py inv` against the base: References section, footnote definitions, generated
  index-links block, `{figure}` blocks, `{dropdown}` blocks, quick-facts table, H2 list and Deep-dive
  count identical; admonitions, duplicate H3s, glance markers recurring below, italic scope lead-in.
* Caps: `rdtools.py caps` at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25) with
  `{figure}` blocks (captions), `{dropdown}` bodies, the generated block and `## References`
  **excluded**; a leading bold run-in label is not counted into its sentence. Also prints the lead.
* Gates per page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`, `-W` build.

## Pages

### 089 PSG — done

* **R-H3.** `### What the public record shows` after the figure caption, over the 257-word evidence
  paragraph (PDK stack diagram and assumptions table, SkyWater's list, then the hedged sacrificial
  reading and thickness estimate). The lead is now the 91-word first paragraph.
* **R-DERIVATION** (under 120 words, no H3): the stack-diagram sentence split at its semicolon, then
  "It places … 0.9361 µm." and "It dimensions the film … to the `li` bottom:" and the two operations as
  a numbered list with bold results; the hedge "(Our arithmetic from the labels and our reading of the
  drawing.)" under it, word for word. `[^pdk-04]`, which closed the whole base sentence, is on each of
  the three diagram sentences (two repeats, declared). Arithmetic checked: 0.9361 − 0.3262 = 0.6099;
  0.6099 − 0.18 = 0.4299. Number order identical to the base.
* **R-LIST.** Why "Insulation": the 54-word studies sentence → lead-in "… because it *flows*:" and
  three plain sub-bullets, one study and marker each. Why "Contamination": "a compromise:" → two plain
  sub-bullets (too little / too much); the dash-joined Levin clause becomes its own sentence opening
  the continuation, so "This is one reason …" still follows the water-absorption sentence it followed
  in the base. How "Sequence": the four-part semicolon sequence → a numbered sub-list;
  `[^txt-09]`, which closed the base sentence, is on the lead-in (R-LIST step 1), not on item 4 only.
* **R-CATEGORY.** Classification sentence alone (36 words; no seam allowed by the rule). "What
  distinguishes this instance …" is its own label (step 3): a paragraph with the gap sentence split at
  its semicolon; the surface sentence split at the closing dash ("… nitride cuts. The deposition
  temperature …").
* **R-PARA / R-SENTENCE.** Lead: the 48-word sentence split at its semicolon ("… and the field oxide.
  Above it, …"). Evidence paragraph: the 67-word sacrificial sentence split before "which takes": "On
  our reading, the polish takes …" — the leading hedge repeated (batch-6 ruling D4), "which" → "the
  polish". The thickness sentence split at its semicolon. Why "Gettering" split at its semicolon into
  lead and continuation. How "HDP-CVD PSG": lead, studies, tools/temperature as three blocks; the
  48-word gapped studies sentence split before Chen et al., whose elided verb "characterised" is
  restored (WORDS ADDED; no new relation); the tools/temperature sentence split at its semicolon (two
  separately cited facts). "PECVD or SACVD" split at its semicolon.
* **R-TOOLS.** HDP-CVD: *SkyWater says:* (verb-first "lists"), *Tool exists:*, *Runs this step:*;
  the 5:1 sub-bullet sentence (SkyWater's words plus this reference's gloss, no seam) and the
  technician-profile sentence with its own "Strength: strong (a SkyWater statement) that such a tool
  exists" stay as continuation paragraphs in base order (the profile grades a different statement, so
  it is not folded into the first *Tool exists:*). PECVD TEOS: two grades as sub-bullets. Two tools,
  no recap table.
* **R-OPENQ.** Labels from the bullets' words: "Deposition route and thickness", "Film removed by the
  polish", "SPOX under the PSG", "Stack-diagram labels".
* **R-RELATED.** Previous and Next as two bullets; "What is cut through it" → `Feeds:`; "Other CVD
  oxides" → `Same category:` (FILOX and NILD2 are deposition steps); "What is buried" keeps its own
  label (burying is not a dependency the rule's labels name). Every gloss and link kept.
* **R-HEDGE.** Scope sentence as the italic lead-in, word for word.
* **R-GLANCE.** Does/Why from the lead and the Why section; Public numbers "PSG K=3.9" `[^pdk-04]` and
  "Pre-LI ILD thickness" 0.5 µm `[^pdk-03]`; tool line with the page's two grades, each named; Not
  public from Open questions 1.
* **Skipped.** R-REPEAT: the SkyWater HDP quotation is in the evidence paragraph and under Machines
  likely used; deleting either copy loses a quotation the evidence rests on, so both stay (as batch 6
  did for 083). R-TABLE: nothing ≥ 3 × 2.
* **Preservation.** ADDED markers `pdk-04`×3 (two repeats, one glance), `pdk-03`, `skw-01` (glance);
  numbers 0.5, 3.9 (glance), 1–4 (numbered-list ordinals); quotes "PSG K=3.9", "Pre-LI ILD thickness",
  hedges "inference", "likely", "not public", "our reading" (glance box and the repeated "On our
  reading"). REGROUPED: the stack-diagram sentence (same digits, same order, now five units), the gap
  sentence (0.21 … 0.2 | 2:1), the tools sentence (200 | 350–450). WORDS LOST: "strength"×2 (R-TOOLS
  labels), "which" (→ "the polish").
* **Marker coverage.** 11 flags, all read: glance condensations (3); the arithmetic hedge line (inputs
  cited on the lead-in); split halves whose base marker belonged to the other clause (sacrificial /
  "poly cap after SPE"; surface / 0.1 µm junctions; the three studies; Paulson / Levin); the NF₃ item
  (marker on the list lead-in).
* **Caps.** para > 100: 2 → 0; item > 60: 6 → 0; sentence > 45: 12 → 1 — "A film thick enough to
  bury …" (46, of which 2 are the dashes of its one dash pair; moving the dash material would separate
  the 0.6–0.9 µm figure from its "(inferred)").

### 090 CMPP — done

* **R-H3.** `### Competing readings` after the figure caption, over the 181-word passage that weighs the
  fixed-removal and cap-stop readings. The lead is the 97-word first paragraph.
* **R-PARA / R-SENTENCE.** Lead: the 47-word topography sentence split at its colon ("… beneath it.
  It stands roughly 0.4 µm higher …"). Competing readings: three paragraphs (first reading; second
  reading; the adopted reading and what follows on it). The 65-word second-reading sentence keeps its
  dash pair in place and splits before "using": "On the second, the polish uses the GATENIT nitride …"
  (the reading's own opener repeated, batch-6 ruling D4; "using" → "uses", a verb for the new
  sentence). The 48-word "On it, …" sentence split at ", and": the second half opens "On that
  reading," — the pronoun "it" given its noun back (R-PARA step 5), because a second "On it" directly
  after "… the local interconnect." could be read as "on the interconnect". The S7 wording "the tops of
  the caps over the densest poly arrays" is unchanged. Why intro: the 51-word IBM sentence split at its
  semicolon. "The cost is …" paragraph (126 w, one 86-word sentence) split at its semicolon and its
  ", and the PDK's" seam into two paragraphs; the Kahng and Samadi parenthetical, a second
  parenthetical in a sentence that already had a dash pair, becomes its own sentence "(The survey …
  synthesis.[^kahng-2008])" (R-SENTENCE step 7). How "Slurry" split at its semicolon into lead and
  continuation.
* **R-LIST.** How "Recipe": the three platens as a nested numbered list (a sequence); the
  "Down-force …[^txt-05]" sentence, its own sentence in the base, stays as the continuation.
* **R-CATEGORY.** Classification sentence alone (42 words, under the 45 cap; the target is 35 and its
  only seam is an opening dash, not a closing one). One sentence remains → a plain second paragraph.
* **R-TOOLS.** Mirra: *SkyWater says:* (verb-first), *Tool exists:*, *Runs this step:*. "Post-CMP
  cleaning" has no "Strength:" and stays as it is. "Defect inspection — KLA AIT / SP1 … Strength:
  medium." stays in its base form: the grade does not say whether it grades existence or assignment,
  so filing it under either label would be a claim the page does not make. One graded tool, no recap
  table.
* **R-OPENQ.** "Polish stop", "Slurry, removal and endpoint", "Brush scrubber".
* **R-RELATED.** Previous and Next as two bullets; "The stop, on our reading" → `Depends on:`; "The
  lithography that needs the flat surface" → `Feeds:`; the STI polish and later oxide polishes (both
  CMP steps) → one `Same category:` bullet (the bullet already named both). Every gloss and link kept.
* **R-HEDGE.** Scope sentence as the italic lead-in, word for word.
* **R-GLANCE.** Does from the lead; Why from the lead ("flat to within the depth of focus of the
  contact lithography") and Why bullet 2; Public numbers "Pre-LI ILD thickness" 0.5 µm and "Min
  pattern density for oxide" 0.75 `[^pdk-03]`; tool line with the two grades, each named; Not public
  from Open questions 1–2, with "the cap-stop reading is our inference".
* **Skipped.** R-REPEAT (no 10-word repeat across H2s); R-TABLE, R-DERIVATION (nothing qualifies:
  0.4 µm = 0.18 + 0.2 is one operation).
* **Preservation.** ADDED markers `pdk-03`, `skw-01`, numbers 0.5, 0.75, quotes "Pre-LI ILD
  thickness", "Min pattern density for oxide", ref `step-089`, identifier `licon1`, hedges
  "inference"×2, "likely", "not public" — all the glance box; numbers 1–3 — the nested list ordinals.
  REGROUPED: the tool paired the glance's 0.5 with the unchanged `{figure}` caption sentence ("On that
  reading the PDK's 0.5 µm …"); the caption is byte-identical (invariants). WORDS LOST: "strength"
  (R-TOOLS label), "using" (→ "uses").
* **Marker coverage.** 7 flags, all read: two glance condensations; the "On it / On that reading"
  split (each half keeps its own marker); the IBM/Ouma and Ouma/PDK/Kahng splits (each piece keeps its
  own markers); "Depends on:" (tokenizer split at the colon; "on our reading" is in the same bullet).
* **Caps.** para > 100: 2 → 0; item > 60: 2 → 0; sentence > 45: 7 → 0.

### 091 NCAPOX — done

* **R-H3.** `### What the public record shows` after the figure caption, over the 138-word passage (what
  the PDK does and does not name, the stack-diagram and assumptions-table reading, SkyWater's two
  entries; it ends in the hedged thickness estimate and the inferred film identity). The lead is the
  110-word text before the figure, now two paragraphs (80 + 30) split before "This reference
  describes …".
* **R-PARA / R-SENTENCE.** Lead: the 67-word sentence split at its semicolon ("… to be uniform. Its
  purpose is …"). Evidence passage: two paragraphs, split before "The film's identity …". Why
  "Keeping phosphorus": lead at the semicolon; the dash material "the phosphorus out-diffusion from
  HDP PSG is a known integration concern (Hsiao …[^hsiao-2005])" becomes its own sentence with its
  marker. Why "Restoring": lead is the "If CMPP lands …" sentence; continuation from "The local
  interconnect …". How "PECVD TEOS": lead at its semicolon; studies, film and SkyWater sentence as the
  continuation. Machines typically used, PECVD: split at the semicolon after the Novellus marker; "the
  Trikon Delta 201, a …" → "The Trikon Delta 201 is a …" (a subject and verb for the new sentence,
  R-SENTENCE step 7).
* **R-LIST.** How "Sequence": three steps as a numbered sub-list; `[^txt-09]` stays on the deposition
  step, the clause it closed in the base (it was mid-sentence, not on the announcing words).
* **R-CATEGORY.** Classification sentence alone (27 words). The two "What distinguishes it …" clauses,
  joined by a semicolon, become two sentences in one paragraph; each is its own label (step 3).
* **R-TOOLS.** "C2 and Producer": pilot form — the head keeps SkyWater's quotation with this
  reference's gloss (the two tools it names), because the grade's reason refers to them ("on those
  tools"); grades as *Tool exists:* / *Runs this step:*. "C1": two grades as sub-bullets. Two tools, no
  recap table.
* **R-OPENQ.** "Thickness, precursor and temperature", "What the cap is deposited on".
* **R-RELATED.** Previous and Next as two bullets; the bullet naming three relationships split:
  "the glass it seals" → `Depends on:`, "what is etched through it" and "what lies on it" → `Feeds:`;
  the earlier and later CVD oxide caps (all deposition steps) → `Same category:`. Every gloss and link
  kept.
* **R-HEDGE.** Scope sentence as the italic lead-in, word for word.
* **R-GLANCE.** Does and Why from the lead; Public numbers "none published for the cap itself" plus
  the page's own reading of the 0.5 µm "Pre-LI ILD thickness" `[^pdk-03]`, with "on our reading"; tool
  line with both grades, each named; Not public from Open questions 1–2.
* **Skipped.** R-REPEAT (none); R-TABLE, R-DERIVATION (the 0.2–0.3 µm estimate shows no operation).
* **Preservation.** ADDED markers `pdk-03`, `skw-01`, number 0.5, quotes "C2 and Producer", "Pre-LI
  ILD thickness", "cap", ref `step-090`, identifier `C2`, hedges "inference", "likely", "not public",
  "our reading" — the glance box; numbers 1–3 — the Sequence ordinals. REGROUPED: the PECVD machines
  bullet (200 | 201, 10, 2005) at its semicolon. WORDS LOST: "strength"×2 (R-TOOLS labels).
* **Marker coverage.** 5 flags, all read: three glance condensations; the phosphorus split (the
  `[^hsiao-2005]` marker belongs to the out-diffusion-concern clause, which keeps it; "could" is in the
  first sentence, which keeps it).
* **Caps.** para > 100: 2 → 0; item > 60: 4 → 0; sentence > 45: 6 → 1 — "If the polish stops on the
  0.2 µm gate caps …" (46). Its only seam is ", and its thickness …", and the second half would lose
  the "If the polish stops …" condition that governs it unless the condition were repeated, which adds
  a number; kept whole.
