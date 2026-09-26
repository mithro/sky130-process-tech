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
