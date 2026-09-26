# Progress — readability batch 7b, steps 098–106 (`topic/rd-steps-098-106`)

Writer: Opus. Started 2026-09-26 from `main` at `fd22efb3`. Guide: `docs/plans/readability-guide.md`
§1, §2, §4.1, §5, §6, §7, §8, with the rulings of batches 4–7 (plain bullets over invented labels; no H3
where none of the four titles fits; R-CATEGORY's 35 words a target; the connective rule inside list
items; derivations under 120 words as a numbered list without an H3; a third lead paragraph only for
base leads over 120 words; "Because X, Y" is not a connective opener; rows differing in unit carry the
unit in each cell; the R-REPEAT deletion declared here with the deleted text and where the surviving copy
sits). Medium classes avoided (batch 4–7 reviews): a pronoun whose referent changes after a split; a
marker lost when dash material moves; a sentence moved below the grade that refers to it; glance
wording that strengthens a grade or does not say what it grades. Model pages: 093, 097. One commit per
page.

## Method, every page

* Baseline build and one desktop tile set per page before any edit (`tmp/shots/*-before*`,
  git-ignored); one final pair (1280 px, `--max-height 40000`; 400 px, `--max-height 60000`) after.
* Preservation: `uv run python tools/check_preserved.py --base HEAD --allow-regrouped <page>` against
  the commit before the page, no other flag; never `--allow-added`, never `--allow-dropdown-edits`.
  Every ADDED line is named in the page entry; every REGROUPED line read; every `WORDS LOST` word
  accounted for; `--strict-words` as the final run.
* Marker coverage: `tmp/readability/rdtools.py cov` (git-ignored scratch script) pairs every sentence
  not verbatim in the base with its closest base sentence and flags any marker or hedge word the base
  sentence had and the new one lacks; semicolons and colons are split points too. Every flag read; the
  page entry says what each class is.
* Invariants: `rdtools.py inv` against the base: References section, footnote definitions, generated
  index-links block, `{figure}` blocks, `{dropdown}` blocks, quick-facts table, H2 list and Deep-dive
  count identical; admonitions, duplicate H3s, glance markers recurring below, italic scope lead-in.
* Caps: `rdtools.py caps` at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25) with
  `{figure}` blocks (captions), `{dropdown}` bodies, the generated block and `## References`
  **excluded**; a leading bold run-in label is not counted into its sentence. Also prints the lead.
* Repeats: `rdtools.py rep` lists 10-word runs that occur in two H2 sections (R-REPEAT).
* Gates per page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`, `-W` build.

## Batch summary

(filled in after the last page)

## Content problems for the owner

(filled in as found; kept verbatim on the pages)

## Pages

### 098 CSIL — done

* **Lead.** First sentence 38 → 13 words: the dash pair becomes commas ("`CSIL`, contact silicidation,
  is the anneal (on our reading a rapid thermal anneal)."), the rest is "It reacts the titanium …"
  ("It" = the anneal; "that" dropped). The hedge stays on the sentence that names the anneal. Lead 96
  words, one paragraph.
* **R-H3.** No H3 over the post-figure passage: it opens "That is the distinctive feature …", which
  continues the lead across the figure (R-H3 step 6). R-PARA instead: the 170-word paragraph split at
  its seams into three (salicide contrast; the PDK numbers and P1I; the conclusion "On that evidence
  …" and SkyWater's module).
* **R-SENTENCE.** The 55-word extraction-table sentence split at its dash pair: "… 197 000
  mΩ/sq.[^pdk-08] These are the values of heavily doped but *unsilicided* poly and diffusion. The
  LICON contact is listed at 15 000 …[^pdk-08]" — "These are" and "is" added (subject and verb); the
  marker stays on the values it followed, the LICON sentence keeps its own marker and "(our
  reading)". REGROUPED number order read: same six numbers, same order.
* **R-CATEGORY / R-LIST.** Classification sentence alone (26 words). The 17-word parenthetical becomes
  a sentence, "(The category page gives …)" ("it" → "The category page", R-PARA step 5), kept before
  the sequence so the number order is unchanged (an earlier draft that put it after the list failed
  `number_order`). The three-part sequence becomes a numbered list under the neutral lead-in "The
  sequence:", which carries `[^maex-1993][^osburn-1993]` (they closed the base sentence, R-LIST
  step 1). "What is specific …" is its own label (step 3); its 50-word sentence split at its colon.
* **Why.** "Contact resistance": split at the semicolon into a 27-word lead and a continuation.
  "Why not a salicide": "Three features …(inference):" then three plain sub-bullets (semicolons
  kept, the final "and" dropped), the closing two sentences as a continuation. "Phase and thickness":
  the dash-introduced study run becomes five plain sub-bullets, one study and marker each; the
  elided noun in "Zhang and Östling's of silicides" restored as "review" (WORDS ADDED, no new
  relation). "The TiN cap": split at the dash after `[^morgan-1985]` (the marker stays with the
  study; the nitrogen clause had no marker in the base) and before Koerner.
* **How.** Scope sentence as the italic lead-in, word for word. "Temperature and time": the 17-word
  citation parenthetical split — "(Osburn[^osburn-1993])" stays inline (attribution only, §1); the
  Yoo sentence becomes its own sentence with its marker, in a continuation. The item lead stays 40
  words: its only seam is the dash before "typical industry values (Osburn)", and splitting there
  would leave the values without their hedge and citation. "Alternative" split at the semicolon.
* **R-TOOLS.** Heatpulse: *SkyWater says:* (verb-first "lists"), *Tool exists:* **strong** for the
  tool, *Runs this step:* the inference and its two reasons (the listed application keeps
  `[^ag-8800]`; the colon that followed it becomes a full stop); the reseller/blog sentence and the
  ramp-rate parenthetical stay as the continuation, in base order. The "Ti and Co Silicide" module
  bullet is a capability, not a tool: unchanged.
* **Resources.** The 20-word parenthetical after "Nitrogen and argon": "(likely ambient, our
  inference)" stays; "SkyWater lists … any step.[^skw-01]" and "The titanium and TiN were consumed
  …" become sentences.
* **R-RELATED.** Previous and Next as two bullets (the base bullet named both); "The surfaces
  silicided" → `Depends on:`; "The other RTAs" → `Same category:` (all four are Anneal steps);
  "Why the gates are not silicided …" keeps its own gloss as a label (no rule label fits; 089
  precedent).
* **R-OPENQ.** Labels from the bullets' words: "Contact-only silicide", "Anneal conditions",
  "Silicide thickness", "The Co in the module" (no quotation marks added).
* **R-REPEAT.** None (`rdtools.py rep`: 0 runs).
* **R-GLANCE.** Does/Why from the lead and the Why lead; Public numbers poly 48 200 and N-diffusion
  120 000 mΩ/sq with "values of heavily doped but unsilicided" (the body's words) and LICON 15 Ω per
  contact "(our reading)", each `[^pdk-08]`; tool line with both grades named; Not public from the
  body's list (→ Open questions).
* **Preservation.** ADDED lines are the glance box only (markers `pdk-08`×2, `skw-01`; numbers;
  `step-097`; hedges). WORDS LOST: "strength" (R-TOOLS label), "that" (first sentence), "and"
  (list joins). WORDS ADDED: labels, "These are", "is", "The sequence", "category page", "review".
* **Marker coverage.** 13 flags read: list items under a lead-in marker (sequence, studies), clauses
  that had no marker of their own in the base (nitrogen clause, "It reacts …", the classification),
  and the tool head. None lost.
* **Caps after:** 0 paragraphs, 0 items, 0 sentences, 0 cells over; item lead over 30: "Temperature
  and time" (40, above).
