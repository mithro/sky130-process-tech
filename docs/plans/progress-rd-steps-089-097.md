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

## Batch summary (all nine pages done)

### Batch measurement (§1 caps; figure captions and dropdown bodies excluded)

Counted with `rdtools.py caps`: `{figure}` blocks (the captions), `{dropdown}` bodies (none on these
pages), the generated index-links block and `## References` are **excluded**; a leading bold run-in
label is not counted into its sentence. Before = `main` at `e369d634`.

| §1 cap | Before | After |
|---|---:|---:|
| paragraphs > 100 words | 21 | 0 |
| list items > 60 words | 49 | 0 |
| sentences > 45 words | 76 | 3 |
| table cells > 25 words | 0 | 0 |

**Left over the caps, with reasons** (each is also in its page entry):

* Sentences (46 words each): 089 "A film thick enough to bury …" (2 of the 46 are its dash pair; moving
  the dash material would separate the 0.6–0.9 µm figure from "(inferred)"); 091 "If the polish stops
  on the 0.2 µm gate caps …" (the second half would lose its condition); 092 the dielectric-anneal
  reading (3 of the words are the bold label that is its subject).
* Leads over 120 words, as in the base (text before the figure): 093 (137, base 137), 094 (217, base
  214; three paragraphs, §4.1 ¹), 095 (138, base 138), 096 (149, base 149). On 094 and 096 the passage
  after the figure takes no H3 (094: none of the four titles fits; 096: under 120 words), so by §1's
  definition their "lead" also includes that list.
* Item leads over 30 words: 095 reading 1 (52; its only seam is inside the sentence the S7 notes
  record as disputed, kept verbatim), 092 dielectric reading (46), 091 "C2 and Producer" head (pilot
  form, the grade refers to the tools the gloss names).
* No `{dropdown}` on any of the nine pages; no in-force content anywhere.

### Gates (end of batch, in the worktree)

`check_steps`, `check_refs`, `check_machines`, `check_materials`, `check_masks`, `check_papers`,
`check_patents`, `check_filings`, `check_inforce` — 0 problems; `gen_papers`, `gen_patents`,
`gen_filings`, `gen_index_links`, `gen_step_tables`, `gen_figures` `--check` — 0 differences (figures
untouched; `gen_figures` run once, at the end); `sphinx-build -E -W` into a fresh directory — exit 0.
`rdtools.py inv` against `e369d634` for all nine pages: References, footnote definitions, generated
blocks, `{figure}` blocks, quick facts, H2 lists and Deep-dive counts identical; one admonition per
page (the glance box, `:class: at-a-glance`); every glance marker recurs below; no duplicate H3; every
scope sentence is the italic lead-in. `check_preserved.py --allow-regrouped` over the batch: the only
LOST lines are 093's rule-table number order (hand-checked, entry 093) and 097's R-REPEAT sentence
(entry 097); every other line is a declared addition, a regroup, or a WORDS LOST word named per page.

### Guide problems

1. **R-REPEAT cannot pass the preservation gate.** Its own worked example (097's supplier sentence)
   deletes numbers and an identifier that stay elsewhere on the page, and `check_preserved.py` has no
   flag for that on step pages (`--allow-deduplicated` is machine/material only). Suggest extending
   `--allow-deduplicated` to a sentence still present verbatim in another H2 of the same page.
2. **R-TABLE rows in `Rule · Constrains · Value` order always fail `number_order`**, because the rule id
   (a number to the tool) now precedes its value; `--allow-regrouped` does not reclassify it (093; the
   same form as 078). A regroup condition that accepts a per-row swap would save a hand check.
3. **§1/§4.1 "lead" when the post-figure passage takes no H3.** The lead is defined as the text up to
   the first `###`; when R-H3 forbids an H3 (094, 096) the lead then includes the post-figure list.
   Suggest defining the lead as the text before the `{figure}`.
4. **§1 parenthetical cap against citation parentheticals.** A 12-word parenthetical of two noun
   phrases and markers (097 "(Sundgren's review …; Berg and Nyberg's model …)") would become a verbless
   sentence; suggest exempting citation-only parentheticals.
5. **R-TOOLS with one sentence grading two things.** 097's "the platform … is an inference, as is the
   assignment …" grades the platform identity and the assignment together; neither label fits the
   whole without rewording.

## Content problems for the owner

Kept verbatim on both sides; not fixed.

1. **094 against 095 on the contact-bottom oxide** (the S7 figure notes). 094's lead says the etch
   reaches "the SPOX oxide over a source/drain or tap, which the etch must also clear", and its recipe
   step 4 has the timed over-etch clear it. 095's reading 1 says that "on the reading of the SPOX and
   LICM1E pages" the plasma contact etch "is stopped on or in it rather than driven into the silicon",
   and 095's Why "Screen oxide" bullet cites "the LICM1E reading" for an etch that stops on SPOX. The
   two pages disagree on what LICM1E says.
2. **Which caps the polish stops on (089, 090, 091).** 089 says the polish takes the glass "down to, or
   close to, the tops of the 0.2 µm gate caps"; 090 says it "reaches the tops of the caps over the
   densest poly arrays"; neither says which caps. 091 says that on the cap-stop reading "the cap oxide
   is what separates the cap tops from the local interconnect" and, in Why, "the cap oxide is that
   insulator" — true of caps at the polish level, but, with the PDK's heights, gates on active area
   keep about 0.33 µm of PSG over them (S7 notes; 100 and 103, outside this batch, carry the "only the
   cap oxide separates" wording).
3. **Arithmetic checked, no slip found:** 089 0.9361 − 0.3262 = 0.6099 and 0.6099 − 0.18 = 0.4299;
   093 0.17 × 0.6 / 0.365 = 0.279 ≈ 0.28 and 0.17 × NA / 0.248 = 0.41–0.48; 094 2 × 0.5 µm × tan 10° ≈
   0.18 µm and atan(0.045 / 0.5) ≈ 5°.

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

### 092 RTAD2 — done

* **R-H3.** `### Competing readings` after the figure caption, over the 183-word passage that weighs the
  source/drain-anneal and dielectric-anneal readings and then says why the anneal comes here on either
  reading. The lead is the 91-word first paragraph.
* **R-GLANCE step 8 / R-SENTENCE.** First sentence 41 → 23 words: split before "but placed", the
  second sentence opening "`RTAD2` is placed *after* …" — the step's name, not "It", because "It"
  directly after "… {ref}`RTAD` four steps earlier." would read as RTAD (the pronoun-referent class).
* **R-PARA / R-SENTENCE.** Readings: the source/drain bullet split into lead and a continuation from
  "The RTAD page sets out …"; the dielectric bullet's 58-word first sentence loses its second
  parenthetical, which becomes its own sentence "(Miyazaki et al. used exactly such an RTA to improve
  PSG's passivation.[^miyazaki-1994])" (R-SENTENCE steps 3 and 7), and the studies start the
  continuation. "On either reading …" split at its colon. Step category: "What is specific to it" →
  "What is specific to `RTAD2`" (the preceding sentence ends on CSIL, so "it" could be read as CSIL;
  R-PARA step 5); its colon and its dash become full stops; "It is also the anneal with the least
  freedom" → "`RTAD2` is also …", opening a second paragraph (the paragraph was 108 words), and its
  colon becomes a full stop. Why "Stable activation" split at its semicolon into lead and
  continuation; "Dielectric densification" likewise.
* **R-LIST.** How "Temperature and time": the reseller disagreement becomes "The two reseller documents
  disagree on the 8800's ramp rate:" and one plain sub-bullet per document, each with its own marker
  ("while" dropped); "Both put the steady-state range at 400–1200 °C." stays after the list (a plural
  pronoun naming the two documents, review 6 D1).
* **R-CATEGORY.** The 45-word classification sentence stays whole (35 is a target; splitting at its
  semicolon would leave the CSIL comparison as a one-sentence paragraph directly before "What is
  specific to …"). "What is specific to …" is its own label (step 3).
* **R-TOOLS.** Heatpulse: *SkyWater says:* (verb-first), *Tool exists:*, *Runs this step:*; the
  reseller evidence and the blog post follow directly as the continuation (split at its semicolon).
  Aviza: pilot form — the head keeps the quoted entries and this reference's gloss ("the batch
  alternative but … an unlikely one"), one sentence with no seam; grades as sub-bullets. Two tools, no
  recap table.
* **R-OPENQ.** "Purpose of the second anneal", "Temperature, time and ambient", "Reflow or
  densification".
* **R-RELATED.** Previous and Next as two bullets; "The films annealed … the polish between them"
  (PSG, NCAPOX, CMPP; all MOL) → `Same module:`; the first source/drain anneal, the earlier RTAs and
  the lower-temperature anneals that follow (all Anneal-category steps) → one `Same category:` bullet
  (two bullets merged; every gloss and link kept).
* **R-HEDGE.** Scope sentence as the italic lead-in, word for word.
* **R-GLANCE.** Does from the lead with "described in this reference as"; Why names both readings and
  says both are inferences; Public numbers "none for the anneal itself" plus the 0.1 µm design depth
  `[^pdk-03]`; tool line with both grades, each named; Not public from Open questions 1–2.
* **Skipped.** R-REPEAT (none); R-TABLE (the two reseller documents are two items, not ≥ 3 × 2).
* **Preservation.** ADDED markers `pdk-03`, `skw-01`, numbers 0.1, 8808, hedges "inference", "likely",
  "not public" — the glance box; identifiers `RTAD2`×4 (three pronouns given their noun back, one
  glance). REGROUPED: the reseller-disagreement sentence (now a lead-in and two items) and the
  Heatpulse reseller sentence (split at its semicolon) — same digits, same order. WORDS LOST: "but",
  "while" (connectives at splits), "it"×2 (→ `RTAD2`), "strength"×2 (R-TOOLS labels).
* **Marker coverage.** 3 flags, all read: two glance condensations; the second reseller item (the
  `[^ag-8800]` marker belongs to the first item, which keeps it).
* **Caps.** para > 100: 1 → 0; item > 60: 6 → 0; sentence > 45: 9 → 1 — the dielectric-anneal lead
  (46, of which 3 are the bold label that is the sentence's subject; its only other seam would need an
  added "also").

### 093 LICM1 — done

* **R-H3.** `### What the public record shows` after the figure caption, over the 225-word PDK passage
  (mask table, layers, rules, minimum-CD and physical-criteria entries). The lead is the text before
  the figure: 137 words in the base, 139 now (§4.1 ¹: over 120 in the base; two paragraphs, 59 + 78,
  both under 100, so no third). Listed.
* **R-TABLE.** The ten-part `licon` rule sentence → a `Rule | Constrains | Value (µm)` table under the
  lead-in "The rules head the `licon` section "Defines contacts …" and give:[^pdk-periph]" (the marker
  that closed the enumerating sentence stays on the lead-in, step 3). One row per rule in the base
  order; the three nitride-cut rules, named together in the base, are one row. The four rules with no
  value are `—`; the two quoted rules stay quoted in their cells. All values are µm in the base, so the
  unit is in the header ("µm" leaves five cells, WORDS LOST "m"×2 after the glance's own "µm"). Phone
  tile: no horizontal scroll. As on 078, no `:::{table}` wrapper (the lead-in is the caption).
  Hand-checked: licon.1 0.170, licon.2 0.170, licon.5a 0.040, licon.8 0.050, licon.11 0.055 — the base
  digits; the tool reports the rule sentence as a number-order LOST only because each row puts the
  rule id before its value.
* **R-LIST.** Step category: "Hole layers differ from line layers in every lithographic respect:" →
  four plain sub-bullets, one respect each.
* **R-CATEGORY.** The 61-word classification sentence split after the parenthesis that closes its
  dash appositive: "`LICM1` is a … step of the *contact-hole* type — the first of the flow's three hole
  layers (…)." (22 words). Two sentences about this step remain → `**Specific to this step:**` and a
  bullet each: "At 0.17 µm holes …, `LICM1` is printed at a k1 close to …" (the layer named, not "it",
  because the sentence before ends on "vias"), with the hole-layer list as its continuation; "The
  surface is flat …".
* **R-PARA / R-SENTENCE.** Lead: the 50-word sentence loses its dash pair, whose content becomes "The
  holes are 0.17 µm squares at minimum." (no marker was involved); the 79-word sentence split at ", and
  they have" ("They have …", referent "Those holes", the sentence's subject) and at its colon and at "but"
  ("But the drawn `licon1` maps …"; `[^pdk-03][^pdk-periph]` stay on the via.1a clause they closed).
  Record: the mask-table sentence split at its semicolon; the minimum-CD sentence split at ", and the
  physical criteria" ("The physical criteria give …", a verb for the new sentence). Why "Contact
  resistance": lead at its semicolon, `[^pdk-08]` repeated on the first half (the marker closed the
  whole base sentence, masks-b H1). "Enclosure rules": lead at its semicolon, `[^pdk-periph]` repeated
  on the first half for the same reason. "Slotted" split at its semicolon. "Lithographic difficulty":
  lead, then the 248 nm passage split at its colon, then the OPC sentence. How "BARC and resist": lead
  ends after the industry-typical resist thickness; "The resist is thin enough …" (the resist named
  for the new sentence) and the dash material "The PDK's nominal 1.14 µm "Photoresist
  thickness"[^pdk-03] is, we infer, the implant-layer value." as sentences of the continuation. How
  "Exposure": split at its semicolon and before "We therefore infer", as 078 does; the k₁ arithmetic
  stays inline, as on the 078 model (one sentence, the i-line case).
* **R-TOOLS.** As 078: DUV stepper/scanner with *SkyWater says:*, *Tool exists:*, *Runs this step:*;
  tracks and overlay/CD with their grades as sub-bullets. Three tools, no recap table (as 078).
* **R-OPENQ.** "Exposure tool and resist", "Drawn size to bottom CD", "Mask add and mask drop".
* **R-RELATED.** Previous and Next as two bullets; the NPCM/NPCME openings and "the films the holes go
  through" → one `Depends on:` bullet; "what fills them" and "the interconnect they connect to" → one
  `Feeds:` bullet; "the next hole layer" → `Same category:`; the slotted-resistor bullet keeps its own
  label, as 078's resistor bullet does; "Mask page:" → `Mask:`. Every gloss and link kept.
* **R-HEDGE.** Scope sentence as the italic lead-in, word for word.
* **R-GLANCE.** Does from the lead; Why from the Why intro; Public numbers licon.1/licon.2 0.170 µm
  `[^pdk-periph]` and the 0.08 µm "Standard Licon bottom CD" `[^pdk-03]`; tool line as 078; Not public
  from Open questions 1.
* **Skipped.** R-REPEAT (none); R-DERIVATION (the k₁ line is kept inline as on 078).
* **Preservation.** ADDED markers `pdk-08`, `pdk-periph` (repeats), `pdk-03`, `pdk-periph`, `skw-01`,
  numbers 0.08, 0.170, 1, 2, quote "Standard Licon bottom CD", ref `step-094`, hedges "inference",
  "likely", "not public" (glance); identifiers `LICM1`×2, `licon1` (one pronoun given its noun back,
  two glance). REGROUPED: nine sentences split at the seams above, same digits in the same order; the
  rule sentence → table as above. WORDS LOST: "m"×2 (units to the header), "page" ("Mask page:" →
  "Mask:"), "strength"×3 (R-TOOLS labels).
* **Marker coverage.** 9 flags, all read: glance condensations (2); the tool head (marker on the
  *SkyWater says:* line); split pieces whose base marker belonged to the other clause (via.1a /
  bottom CD; resist thickness / PDK photoresist; the poly.1a marker now in the first bullet); the
  physical-criteria sentence (tokenizer split at "min.").
* **Caps.** para > 100: 3 → 0; item > 60: 5 → 0; sentence > 45: 11 → 0.

### 094 LICM1E — done

* **Lead.** 214 words in the base (one paragraph), 217 now in three paragraphs (75, 84, 58; §4.1 ¹ —
  the base lead is over 120 and two paragraphs would leave one over 100). Listed. The 66-word sentence
  split at its colon: "The landing surface is the SPOX oxide over a source/drain or tap, which the etch
  must also clear, or the bare poly head …" (a subject and verb for the new sentence; the S7 wording
  "which the etch must also clear" unchanged). The 54-word reconciliation sentence split at ", and
  they": "The two numbers are not stated to belong to the same depth. They do not reconcile …: … about 5°
  (our arithmetic)." — the conclusion stays in one sentence with the arithmetic and its hedge; "They"
  is the previous sentence's subject. No R-DERIVATION: the 0.18 µm and 5° results show no operation.
* **R-H3 not applied / R-LIST.** The 142-word "Three landing surfaces make this etch unusual" passage
  after the figure fits none of the four H3 titles (it is an argument, not the public record, a
  quantity estimate or two readings), so it gets no H3 (batch-4 ruling) and becomes the announced list
  with plain bullets (no invented labels). Item 1 split at its semicolon ("The etch therefore needs
  …"); item 3's opening "And" dropped and its dash-enclosed condition moved to the head of its own
  sentence: "If the CMPP polish landed on the gate caps, the holes over poly are shallower …" (same
  words; the condition still governs its clause).
* **R-CATEGORY.** Classification sentence alone (27 words). The chemistry sentence split at its
  semicolon, with `[^flamm-1981][^winters-1992]`, which closed the whole base sentence, on both halves
  (declared repeats, masks-b H1). "What is specific to this instance …" is its own label (step 3); the
  "same class recurs at CTME … and at every via etch" sentence only lists other steps and stays a
  paragraph after it.
* **R-PARA / R-SENTENCE.** Why: each of the four bullets gets a lead at its first seam (colon or
  semicolon) and a continuation — the studies and the licon.3 sentence ("Because …, …" is not a
  connective opener), the four film studies, the three damage studies with the dash-joined Hashimoto
  clause kept in place. How "Main etch" split at its semicolon (the markers stay on the chemistry
  clause they closed); "Endpoint" split after its first sentence (the S7 wording, the over-etch that
  "clears the SPOX oxide", unchanged); "Post-etch treatment": the 69-word sentence split at its
  semicolon and its 30-word parenthetical made its own sentence, "This is the step SkyWater's
  "Mattson Aspen2 …" — without its CF₄, … (inference) — or "Gasonic PEP" ashers could also
  perform.[^skw-01]" (R-SENTENCE step 7: "This is" added; the parentheses dropped because a
  parenthesised sentence beginning "This is" would read as a fragment; the inner dash pair, its
  "(inference)" and the marker are unchanged). Resources "O₂/N₂" split at its semicolon.
* **R-LIST.** How "Metrology": the test-tile chains as three plain sub-bullets under "The published
  SKY130 test tile lists such chains:[^raw-data-testtile-pads]" (the marker that closed the
  enumerating sentence on the lead-in).
* **R-TOOLS.** "No dielectric etcher is named …": pilot form — the head keeps this reference's
  statement and SkyWater's three quoted entries; "All three carry fluorine-bearing gases that can etch
  oxide." stays above the grade because the grade's reason refers to "any of them"; *Runs this step:*
  **weak** …; "Which tool performs the etch is an open question (below)." as the continuation. Lam
  Exelan has no grade and stays as it is. The asher/wet-clean bullet keeps its head, with *Tool
  exists:* strong for existence.
* **R-OPENQ.** "Chemistry, tool and endpoint", "Where the strip and clean happen", "Oxide at the
  contact bottom", "Shallower holes over poly".
* **R-RELATED.** Previous and Next as two bullets; "the films etched" and "the cut that removed
  nitride from under the poly contacts" → one `Depends on:` bullet; "The nitride the etch must not
  breach" keeps its own label (not one of the rule's relationships); "The next dielectric hole etch"
  → `Same category:`. Every gloss and link kept.
* **R-HEDGE.** Scope sentence as the italic lead-in, word for word.
* **R-GLANCE.** Does and Why from the lead and the Why intro (no numbers, so no markers); Public
  numbers "Licon1 etch angle" 10°, "Standard Licon bottom CD" 0.08 µm, "Pre-LI ILD thickness" 0.5 µm
  `[^pdk-03]`; tool line "none assignable" (the page's only grade is **weak** across three etchers);
  Not public from Open questions 1.
* **Skipped.** R-REPEAT (none); R-TABLE (nothing ≥ 3 × 2 outside the test-tile list, which is now a
  list); R-DERIVATION (above).
* **Preservation.** ADDED markers `flamm-1981`, `winters-1992` (repeats), `pdk-03`, `skw-01`,
  numbers 0.08, 0.5, 10, quotes "Licon1 etch angle", "Pre-LI ILD thickness", "Standard Licon bottom
  CD", identifier `Licon1`, hedges "likely", "not public" (glance). REGROUPED: the taper sentence (now
  split), the test-tile sentence (lead-in and three items) — same digits, same order. WORDS LOST:
  "strength"×2 (R-TOOLS labels).
* **Marker coverage.** 8 flags, all read: glance condensations (3); "They do not reconcile" ("not
  stated" is in the sentence before, which keeps it); item 3's split ("if" is in the second
  sentence); the post-etch split (`[^skw-01]` and "(inference)" moved with the asher sentence they
  belong to); the two test-tile items (marker on the lead-in).
* **Caps.** para > 100: 3 → 0; item > 60: 9 → 0; sentence > 45: 13 → 0.

### 095 SACETCH — done

* **R-H3.** `### Competing readings` after the figure caption, over the three readings and the closing
  "On all three readings …" paragraph. The lead is the 138-word text before the figure (138 in the
  base), now two paragraphs (52 + 86) split before "At this point in the sequence …". Listed (over 120
  as in the base; two paragraphs suffice).
* **Reading 1 kept verbatim.** Its lead sentence ("On the reading of the SPOX and LICM1E pages, … the
  plasma contact etch is stopped on or in it rather than driven into the silicon.") is one side of the
  094/095 disagreement the S7 figure notes record, so it is not split; the item gets a continuation
  from "A short dilute-HF dip …", and its lead stays at 52 words (listed; its only seam is inside the
  disputed sentence).
* **R-PARA / R-SENTENCE.** Reading 2 split at its semicolon ("… then strip it." / "The step would then
  be that strip."), continuation from there. Step category: the 46-word category-page sentence split
  at ", and that": "It says that dilute HF is the tool it infers for …" ("It", the category page, the
  previous sentence's subject). Why "Native and residual oxide": the dash-enclosed Morita clause stays
  where it is and closes the first sentence with its marker; "The plasma etch leaves …[^fonash-1990]"
  starts the continuation; the Dilute-HF sentence is a second continuation paragraph. "What must
  survive" split at its semicolon. "Particles and metals" split at its semicolon. How "HF dip": split
  at its semicolon; the 16-word BOE parenthetical becomes its own sentence "(6:1 BOE etches … too fast
  for this purpose undiluted.)" (§1 parenthetical cap; R-SENTENCE step 7).
* **R-LIST.** Step category: "… and consequence:" → two plain bullets (what the etch leaves, what it
  removes).
* **R-CATEGORY.** Classification sentence alone (12 words). The category-page sentences stay a
  paragraph; "What distinguishes this instance …" is its own label (step 3); the handbook sentence
  closes the section.
* **R-TOOLS.** Four graded tools → a `Tool | Evidence` recap table above the list, in the 084 form
  (no lead-in). DNS/FSI: *SkyWater says:* (verb-first "lists"), *Tool exists:*, *Runs this step:*
  (with its `[^kern-1990]`). SEZ/Da Vinci: pilot form (the head keeps "Single-wafer" beside
  SkyWater's quotation, since the page does not say whose word it is) with two grades. Akrion/EKC and
  the ashers: heads unchanged, *Tool exists:* strong for existence.
* **R-OPENQ.** "What the etch removes", "Chemistry, tool and strip", "Chemical oxide or HF-last".
* **R-RELATED.** Previous and Next as two bullets; "the oxide that may be the "sacrificial" film" and
  "the resist and BARC being stripped" → one `Depends on:` bullet; "the other wet oxide etches" →
  `Same category:`; "Category pages:" kept (two links). Every gloss and link kept.
* **R-HEDGE.** Scope sentence as the italic lead-in, word for word.
* **R-GLANCE.** Does from the lead, saying that what the etch removes is this reference's reading;
  Why from the Why intro; Public numbers "none for the etch itself" plus the 0.08 µm contact bottoms
  `[^pdk-03]`; tool line with the two grades, each named; Not public from Open questions 1–2.
* **Skipped.** R-REPEAT (none); R-TABLE, R-DERIVATION (nothing qualifies).
* **Preservation.** ADDED markers `pdk-03`, `skw-01`, number 0.08, quote "Standard Licon bottom CD",
  hedges "inference", "likely", "not public" (glance); number 223, identifiers `EKC265`, `EKC270`,
  hedge "inference" (the recap table). REGROUPED: the HF-dip item (100:1 to 500:1 | 6:1, 2), same
  digits, same order. WORDS LOST: "strength"×4 (R-TOOLS labels).
* **Marker coverage.** 6 flags, all read: glance condensations (2); the consequence list ("if" is in
  the first bullet); the Morita/Fonash split (each keeps its own marker); the BOE split (the marker and
  "approximately" moved with the parenthetical they belong to).
* **Caps.** para > 100: 2 → 0; item > 60: 5 → 0; sentence > 45: 5 → 0.

### 096 ALLY1 — done

* **Lead.** 149 words in the base, 149 now, in two paragraphs (64 + 84; over 120 as in the base,
  listed). First sentence 29 → 13 words: split at its dash, "The other, {ref}`ALLY`, is the
  conventional final forming-gas anneal …".
* **R-H3 not applied / R-LIST.** The 102-word reading passage after the figure is under the 120-word H3
  threshold (R-H3 step 6), so no H3; its "(a) … and (b) …" sentence (70 words) becomes "We read the
  step, as an inference, as a hydrogen anneal that:" and two plain bullets ("(a)"/"(b)" dropped; the
  hedge on the lead-in covers both). The "third possibility" and "not public" sentences follow as a
  paragraph.
* **R-CATEGORY.** Classification sentence alone (27 words). Two sentences about this step remain →
  `**Specific to this step:**` and a bullet each: the thermal budget; hydrogen. The 54-word hydrogen
  sentence split at ", less welcome,": "… at these temperatures and passivates dangling bonds …[^reed-1988][^cartier-1993]"
  ("and" for the comma of the shortened list) and "Less welcome, hydrogen can neutralise …" (the
  subject named for the new sentence), which opens the bullet's continuation with the Maes et al.
  parenthetical (15 words) made its own sentence "(Maes, Usmani and Heyns measured … retention.[^maes-1981])"
  and "Those side-effects are the reason …" after it; "({ref}`ONO`)" stays with the SONOS cells.
* **R-PARA / R-SENTENCE.** Why "Interface-trap passivation": lead is the Wikipedia quotation; the
  64-word gapped studies sentence split before Stesmans, whose elided verb "set out" is restored
  (WORDS ADDED), so the dash clause "the defects whose density sets …" still follows the P_b centres
  it names. "Plasma damage": split before "and Rangan, Krishnan and Ashok showed …" (the closing dash of
  the pair becomes the full stop after Hashimoto's marker). "Outgassing": split at its semicolon (the
  Levin and Adams markers stay in the first sentence; "them" in the continuation is the water and
  hydrogen of that sentence). How "Tool and ambient": lead, then two continuation paragraphs.
* **R-LIST.** How "Temperature and time": "the ceiling is … the stability of the surfaces:" and the two
  conditions as plain sub-bullets (the Sah, Sun and Tzou marker on the hydrogen condition it closed).
* **R-TOOLS.** Aviza: *SkyWater says:* ("states … and lists …", verb-first), *Tool exists:*, *Runs
  this step:* — its 17-word parenthetical becomes its own parenthesised sentence and "whether it is
  used here …" its own sentence; the dealer sentence is the continuation. Heatpulse: no "Strength:",
  unchanged.
* **R-OPENQ.** "Purpose before any metal", "Ambient, temperature and time", "Furnace or single-wafer",
  "SONOS nitride response".
* **R-RELATED.** Previous and Next as two bullets; the etch it may heal and the dielectrics it
  outgasses (LICM1E, PSG, NCAPOX; all MOL) → `Same module:`; the final alloy and the higher-temperature
  anneal (ALLY, RTAD2; both Anneal-category) → `Same category:`; the SONOS bullet keeps its own label.
* **R-HEDGE.** Scope sentence as the italic lead-in, word for word.
* **R-GLANCE.** Does from the lead; Why "not public" with the page's inference, word "as an
  inference" kept; Public numbers "none published for SKY130" (the page gives none); tool line with the
  two grades, each named; Not public from Open questions 1–3.
* **Skipped.** R-REPEAT (none); R-TABLE, R-DERIVATION (nothing qualifies).
* **Preservation.** ADDED marker `skw-01`, quote "H2 and forming gas alloy", identifiers `ALLY1`,
  `H2`, `SKY130`, hedges "inference"×2, "likely", "not public"×2 — all the glance box. No REGROUPED.
  WORDS LOST: "b" (the "(b)" enumerator), "strength" (R-TOOLS label).
* **Marker coverage.** 13 flags, all read: glance (1); the reading list items (hedge on the lead-in);
  split pieces whose base markers belonged to the other clause (hydrogen effects; the four interface
  studies; Cacciato/Hashimoto vs Rangan; the two ceiling conditions); the Aviza head and the
  parenthetical (tokenizer pairing with an Open-questions line).
* **Caps.** para > 100: 3 → 0; item > 60: 6 → 0; sentence > 45: 7 → 0.

### 097 TI/TIN1 — done

* **Lead.** First sentence 27 → 5 words: split at its colon, "It is a thin titanium film followed by …"
  ("It", the liner just named). The 55-word sentence split at its semicolon ("The titanium nitride
  covers …"). "It is the first of the liner depositions …" → "`TI/TIN1` is the first …" (the step
  named, because the sentence before now ends on the tungsten of WDEP), opening a second paragraph
  (84 + 27 words; the base paragraph was 109).
* **R-H3.** `### What the public record shows` after the figure caption, over the 188-word evidence
  passage (SkyWater's PVD entries, this reference's reading, the step-list description, the IMP
  literature, the industry-typical thicknesses). Three paragraphs. The 67-word first sentence split
  at ", and this reference reads" and at its semicolon; `[^skw-01]` stays on the list clause it closed.
  The 12-word Koerner parenthetical becomes its own sentence (§1 cap) and the thickness sentence is
  split at its semicolon.
* **R-CATEGORY.** Classification sentence alone (28 words). The category-page sentence split at its
  colon. "What is specific to this instance …" is its own label (step 3); its 70-word sentence split
  before ", so that its stoichiometry …" as "So its stoichiometry, resistivity and stress are set by the
  nitrogen flow (…)." (R-PARA step 2 allows a sentence to begin "So" where a split at ", so" requires
  it). Its 12-word citation parenthetical (two noun phrases, no verb) stays inline: as its own sentence
  it would be a fragment.
* **R-PARA / R-SENTENCE.** Why "TiN": split at its semicolon, continuation from "A TiN film …". "Ionised
  deposition": lead, then the IMP studies (split at the semicolon) and the collimation passage as two
  continuation paragraphs. "Silicide thickness control": split at its colon. How "IMP titanium": split
  at its semicolon; the dash material "higher than conventional sputtering, so that …" becomes "The
  pressure is higher than conventional sputtering, so that …" (a subject and verb for the new sentence;
  "higher" described the pressure). "IMP or reactive TiN": split at its semicolon.
* **R-LIST.** How "Degas and pre-clean": the two stations as a numbered sub-list under "On the cluster
  tool (category page[^txt-09]):" — the source parenthesis that closed the base sentence moved, word for
  word, to the lead-in (R-LIST step 1), so it still covers both stations.
* **R-TOOLS.** AMAT PVD: *SkyWater says:* (verb-first), *Tool exists:* **strong** for the vendor and the
  chamber types, *Runs this step:* the platform-and-assignment sentence. That sentence grades the
  Endura platform identity and the assignment together ("… is an **inference**, as is the assignment
  …, from those chamber types and the contact's aspect ratio"); it cannot be separated without
  rewording, so it stays whole under *Runs this step:* (a label that fits its main reason, not its
  first clause — flagged for the reviewer). The IMP/collimation sentence is the continuation.
* **R-REPEAT (the guide's own example, R-REPEAT "Example").** The Honeywell/JX Metals sentence appeared
  under `## Machines likely used at SkyWater` and in the first `## Resources required` bullet. Home:
  Resources required (unchanged). The Machines bullet now reads "**Sputter targets.** Suppliers are
  named under Resources required.[^sec-01][^sec-02] Strength: strong for the suppliers; the specific
  target is not named." — the markers stay, and a supplier bullet keeps its "Strength:" form (R-TOOLS
  applies to machines only). Deleted sentence, verbatim: "SkyWater's filings name Honeywell Electronic
  Materials (2021 S-1 and fiscal 2023 10-K) and JX Metals (fiscal 2023 10-K) as sputter-target
  suppliers." Both labels remain referenced on the page. This deletion is the page's only LOST in the
  preservation check (numbers 10×2, 2021, 2023×2; identifier S-1; the words of that sentence), all of
  it still present in the Resources bullet.
* **R-OPENQ.** "Thicknesses, coverage and titanium route", "Degas and pre-clean", "Same or separate TiN
  chamber".
* **R-RELATED.** Previous and Next as two bullets; "the other TiN film of this module" (LITIN, MOL) →
  `Same module:`; "the holes lined" and "the clean before it" → `Depends on:`; "Later liners" (all
  deposition steps) → `Same category:`. Every gloss and link kept.
* **R-HEDGE.** Scope sentence as the italic lead-in, word for word.
* **R-GLANCE.** Does and Why from the lead; Public numbers "none for the films" plus the 0.08 µm bottom
  CD `[^pdk-03]` (the page's "about 6:1" is its own ratio, so it is not given as a SKY130 number);
  tool line with both grades, each named ("the platform and the assignment"); Not public from Open
  questions 1.
* **Skipped.** R-TABLE, R-DERIVATION (the 6:1 ratio shows no operation).
* **Preservation.** ADDED markers `pdk-03`, `skw-01`, number 0.08, quote "Standard Licon bottom CD",
  identifier `TIN1`, hedges "inference", "likely", "not public" (glance, and the step named in the
  lead); numbers 1, 2 (sub-list ordinals). LOST: the R-REPEAT sentence above. REGROUPED: the silicide
  sentence (0.1 | 2.3) and the IMP-titanium item, same order. WORDS LOST: the R-REPEAT sentence's words,
  "strength" (R-TOOLS label), "that", "as".
* **Marker coverage.** 9 flags, all read: glance (2); split pieces whose base markers belonged to the
  other clause (SkyWater list / reading; Koerner now its own sentence; Sundgren/Berg with the "So …"
  sentence); the degas stations (marker on the lead-in); a tokenizer pairing of the tool head.
* **Caps.** para > 100: 3 → 0; item > 60: 6 → 0; sentence > 45: 13 → 0.
