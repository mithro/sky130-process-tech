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

### 099 WDEP — done

* **Lead.** Base 124 words in one paragraph (over 100): two paragraphs at the seam between the fill
  and the polish (55 + 71; lead 126 words, base over 120, text before the figure). The 46-word second
  sentence split at its colon: "It is a thin nucleation layer first, then a bulk film …" ("It" = the
  blanket film, the previous subject; "It is" added, R-SENTENCE 7). The film-thickness sentence split
  at its semicolon ("… is not public. A blanket of …").
* **R-H3.** No H3 after the figure: the passage is 120 words and none of the four titles is needed
  once it is a list (below).
* **R-LIST.** "Two public facts anchor the step" → colon and two plain bullets (SkyWater's list; the
  PDK). The PDK bullet's 59-word sentence split at its semicolon and at ", and its physical criteria";
  `[^pdk-06]` stays on the `licon1` description, `[^pdk-08]` and "(our reading)" on the LICON
  sentence, `[^pdk-03]` on the fill-capability sentence.
* **R-REPEAT — not applied.** `rdtools.py rep` finds SkyWater's "Lam/Novellus PECVD Tungsten … (up to
  10:1)" quotation in both the post-figure passage and `## Machines likely used at SkyWater` (the
  home). The passage's copy is not a pure duplicate: it adds "among its deposition tools" and pairs
  the entry with "W plug dual damascene" "among its special modules", which the home copy does not
  say. Replacing it with a pointer would delete those facts (§2.1), so both copies stay.
* **R-CATEGORY / R-LIST.** Classification sentence (79 words) → "`WDEP` is a … step of the *CVD
  tungsten* type, which the category page describes:" with `[^wiki-wf6][^txt-01]` on the lead-in
  (they closed the enumeration and cover both reactions, R-LIST step 1), then the two-step sequence as
  a numbered list. The conformality quotation becomes "CVD tungsten is, in the category page's words,
  …" (its subject in the base was the CVD-tungsten type; named, so no pronoun points at list item 2).
  The next sentence's "It" → "`WDEP`" (its base referent), so the pronoun does not change referent.
  "What is specific …" (its own label, step 3) as a paragraph; its 59-word sentence split at ", and
  the "PNL option …"" — the `[^skw-01]` sentence keeps its marker, the aspect-ratio sentence its two
  `[^pdk-03]`.
* **Why.** "Conformality and fill" split at its semicolon (lead + continuation opening "If the mouth
  closes …"). "Nucleation": lead is the base's first sentence to the semicolon (33 words, dash pair of
  studies kept inside it so the claim keeps its support — over the 30-word item-lead target, listed);
  continuation 1 Tripathi and the reason PNL was developed (split at its colon); continuation 2 the
  Novellus quotation (`hole",` → `hole".`, the comma outside the quotation), Kim, Petri. "Barrier
  dependence": the 12-word parenthetical → "(category page). Koerner et al. evaluated … needed.[^koerner-1993]".
* **How.** Scope sentence as the italic lead-in, word for word.
* **R-TOOLS.** Lam/Novellus: *SkyWater says:* verb-first; *Tool exists:* **strong** for the three
  things; *Runs this step:* the model-and-assignment sentence kept whole (one sentence grading two
  things at the same strength, ruling D5), with its "we infer" parenthetical and the "— though …"
  clause. The PNL-patent and "PECVD Tungsten" reading sentences stay as the continuation. The "W plug
  dual damascene" module bullet is a capability: unchanged.
* **R-RELATED.** Previous / Next split (the bullet named both); liner and holes → `Depends on:`;
  later tungsten fills → `Same category:` (all Thin-film deposition).
* **R-OPENQ.** "Film thickness and chemistry", "Novellus/Lam model", "Label for the tool", "What the
  phrase refers to" (no quotation marks added).
* **R-GLANCE.** Does/Why from the lead and the Why lead; Public numbers "none for the film" plus the
  0.08 µm bottom under 0.5 µm `[^pdk-03]`; tool line names both grades and what each covers
  ("**inferences** (the model and the assignment to this step)"); Not public from Open questions 1.
* **Preservation.** ADDED: glance only (`pdk-03`, `skw-01`, 0.08, 0.5, `licon1`, "likely", "not
  public"). WORDS LOST: "strength" (R-TOOLS label). WORDS ADDED: labels, "It is", "`WDEP`", "CVD
  tungsten".
* **Marker coverage.** 12 flags read: list items under lead-in markers, the conformality quotation (no
  marker in the base), sentence halves each keeping their own markers, glance lines. None lost.
* **Caps after:** 0 / 0 / 0 / 0. Lead 126 words (base 124). Item lead over 30: "Nucleation" (33).

### 100 WCMPLI — done

* **Lead.** First sentence 31 → 22 words: the dash pair becomes commas; "leaving tungsten only inside
  the contact holes" → "It leaves tungsten only …" ("It" = `WCMPLI`, the subject; "leaving" survives in
  the glance, so the tool does not list it). Base 108 words in one paragraph → two (61 + 46) at the seam before "The surface that
  results"; its 46-word sentence split at the semicolon. "(industry-typical)" untouched.
* **R-SENTENCE.** Post-figure 58-word sentence split at its colon ("… are in the rules. The local
  interconnect must …"); both `[^pdk-periph]` stay on their rules. No H3 (the passage is 60 words).
* **R-REPEAT — applied (declared).** Deleted from the post-figure passage (base `100-wcmpli.md:42–44`):
  "SkyWater's capability list names "AMAT Mirra CMP" with "tungsten" and "high selectivity tungsten"
  among its processes.[^skw-01]" The surviving copy is the *SkyWater says:* line under `## Machines
  likely used at SkyWater` (the home for tool quotations): "lists "AMAT Mirra CMP" with "tungsten" and
  "high selectivity tungsten" among its processes.[^skw-01]" — the same quotations, the same marker,
  "lists" for "capability list names". Pointer, 11 words, marker kept: "SkyWater's capability list is
  quoted under Machines likely used at SkyWater.[^skw-01]" This gives `LOST quotes: 'AMAT Mirra CMP';
  'high selectivity tungsten'; 'tungsten'` and WORDS LOST "amat", "among", "names", "processes",
  "with" — all words of the deleted copy; hand-verified that each survives in the home copy.
  `[^skw-01]` still occurs 6 times on the page.
* **R-CATEGORY / R-LIST.** Classification sentence (64 words) → lead-in "… which the category page
  contrasts with the STI and oxide polishes:" (the classification, 21 words) and four plain bullets
  (film removed, stop, slurry, failure modes; semicolons kept, the final "and" dropped). "It is the
  first metal polish in the flow" → "`WCMPLI` is …" (after the list "It" would point at the last
  bullet; `WCMPLI` is its base referent). **"What is specific …" left byte-identical** (65 words, over
  the 45 cap): it holds the "only the {term}`cap oxide` separates" wording that the S7 figure notes ask
  to keep verbatim; see Content problems.
* **Why.** "Etch-back versus polish" split at ", and Kaufman" (lead = the Kaanta sentence; the Kaufman
  sentence keeps its dash and its marker in the continuation). "Chemistry" split at its first
  semicolon (lead = the review; the gapped study sentence kept whole in the continuation — no elided
  verb to restore). "Plug recess and erosion" split at the semicolon after "contact resistance" (the
  continuation opens on "Wang et al.", not on "Both"). "Endpoint" split at its colon (lead: "Because
  …, tungsten CMP is one of the easier polishes to endpoint." — "Because X, Y" is allowed). The
  17-word "coring" parenthetical stays inline and over the parenthetical cap: its only sentence form
  would start with the quotation "coring", whose case may not change (R-SENTENCE 6).
* **How.** Scope sentence as the italic lead-in. "Recipe": the four-part semicolon sequence → a
  numbered sub-list; the 12-word parenthetical about the liner loses its brackets and becomes the
  relative clause ", which polishes more slowly … slurry" (no word changed). The nested numbers give
  `ADDED numbers: '1'…'4'` (list labels, not content).
* **R-TOOLS.** Mirra: *SkyWater says:*, *Tool exists:*, *Runs this step:* (the 13-word parenthetical
  → "(A tungsten polish … levels.)", its own sentence inside the grade it supports); "Which of the two
  tungsten processes …" as the continuation. KLA AIT / SP1: pilot form (012): the head keeps "our
  reading …" and the quotation; "Strength: medium" → *Tool exists:* medium. Post-CMP cleaning has no
  grade: unchanged.
* **R-RELATED.** Previous / Next split; liner and stop oxide → `Depends on:`; CMPP, CMPNIT and the later
  tungsten polishes → one `Same category:` bullet (all CMP; the two base bullets merged, every gloss
  and link kept).
* **R-OPENQ.** "Slurry and endpoint", "High selectivity process", "Plug recess and oxide erosion",
  "Brush scrubber".
* **R-GLANCE.** Public numbers: "none for the polish" and li.5's 0.080 µm `[^pdk-periph]`; tool line
  with both grades named; Not public from Open questions 1 and 3.
* **Preservation.** ADDED: glance (`pdk-periph`, `skw-01`, 0.080, li.5's 5, hedges) and the nested list
  labels. LOST: the R-REPEAT quotations above. WORDS LOST: "strength"×2 (R-TOOLS labels) and the
  R-REPEAT words.
* **Marker coverage.** 7 flags read: glance lines, the pointer, the category bullets (no markers in
  the base), the Kaanta/Kaufman halves (each keeps its own marker), the tool head, the parenthetical
  sentence. None lost.
* **Caps after:** 0 paragraphs, 0 items, 1 sentence (the kept cap-oxide sentence, 65), 0 cells.

### 101 LITIN — done

* **Lead.** First sentence 34 → 6 words: split at its colon ("… itself. It is a blanket film of titanium
  nitride, about 0.1 µm thick, sputtered (on our reading) …" — "It" = the local interconnect; the
  hedge stays with "sputtered"). Lead 99 words, one paragraph.
* **R-H3.** `### What the public record shows` after the figure caption, over the 213-word evidence
  passage (PDK, README, lecture, press release, then the resistivity arithmetic and SkyWater's list).
  The passage does not continue a sentence of the lead.
* **R-LIST.** The 124-word seven-source sentence → the opening sentence ends in a colon; seven plain
  bullets, each with its own marker, in order (semicolons kept, the final "and" dropped). The
  single-operation arithmetic (12.8 Ω/sq × 0.1 µm ≈ 128 µΩ·cm) stays inline as its own sentence
  (R-DERIVATION step 6); checked: 12.8 Ω × 0.1 µm = 1.28 µΩ·m = 128 µΩ·cm.
* **R-REPEAT — applied (declared), two copies.** The supplier sentence "SkyWater's filings name
  Honeywell Electronic Materials (2021 S-1 and fiscal 2023 10-K) and JX Metals (fiscal 2023 10-K) as
  sputter-target suppliers[^sec-01][^sec-02]" stood three times (base `101-litin.md:55–57` in the
  public-record passage, `:179–181` under Machines likely used, `:186–188` under Resources required).
  Home: `## Resources required` (`:186–188`), unchanged. The public-record copy ("… tool[^skw-01] and its
  filings name … suppliers.[^sec-01][^sec-02]") → "… tool.[^skw-01] Its sputter-target suppliers are
  named under Resources required.[^sec-01][^sec-02]" (9-word pointer, markers kept). The Machines copy
  → "**Sputter targets.** Suppliers are named under Resources required.[^sec-01][^sec-02] Strength:
  strong for the suppliers; the specific target is not named." — the 097 model's wording; the grade
  stays. `LOST numbers: 2021×2, 2023×4, 10×4` (the 10-K), `LOST identifiers: S-1×2` and the WORDS LOST
  "honeywell", "electronic", "jx", "metals", "fiscal", "filings", "name" are exactly the two deleted
  copies; hand-verified against the surviving Resources copy.
* **R-CATEGORY.** Classification sentence alone (19 words, ends at "(inferred)"); the 13-word
  parenthetical's reason becomes "SkyWater's public list has PVD TiN chambers and no CVD TiN.[^skw-01]"
  opening the next paragraph; "and the only step …" → "`LITIN` is the only step …" (its base
  subject, so no pronoun after the SkyWater sentence). "What is specific …" is its own label (step 3):
  the 65-word sentence split at its colon and at ", which is exactly" → "This is exactly what makes it
  useful …" ("This" = the comparison the base "which" pointed at; "it" = the film, as in the base).
* **R-TABLE** (Why, "Routing density"). The four-rule enumeration → `Rule | Constrains | Value`, one row
  per rule pair, units in each cell (µm and µm² differ, batch ruling). The base's end marker
  `[^pdk-periph]` is on the lead-in "The PDK's rules allow:"; its mid-sentence marker stays on the
  li.1a/li.3a row it followed. Row 2 restores the elided "lines and spaces" (base "0.14 µm inside
  certain RF cells"); row 4 uses "width", the next sentence's word for li.7. `LOST number_order`
  hand-checked (rule-table form, as 093): li.1/li.3 0.17 µm; li.1a/li.3a 0.14 µm; li.6 0.0561 µm²;
  li.7 0.290 µm — same values, same order. The resistor sentence's dash material (the two
  table citations with their markers) becomes its own sentence after "A `li1` resistor is in fact a PDK
  device, which only a film … can provide." (the main clause had no marker of its own).
* **Why, other items.** "Origins": split at the semicolon; lead 40 words (its only earlier seam,
  ", using the TiN", would leave "using …" without the Tang markers that support it — over the 30-word
  item-lead target, listed); continuation 1 the patents, Mann and White; continuation 2 "SKY130's
  version, on our reading …". "Why TiN and not a metal": the four-clause property sentence split at
  its first semicolon (lead + "TiN does not react …" — noun back for "it"); the resistivity sentence's
  dash material becomes "The resistivity is set by …" after "TiN's resistivity is high …" (noun back
  for "Its"; its attribution parenthetical kept whole); ", and the li.2 rule" → "The li.2 rule …" with
  its "we infer". "What it lands on" split at its semicolon.
* **How.** Scope sentence italic. Degas: the 17-word Boumerzoug parenthetical becomes its own sentence
  (brackets dropped, no word changed). Reactive sputtering: split at the closing dash and the
  semicolon; the industry-typical tag stays on the temperature sentence it closed.
* **R-TOOLS.** AMAT PVD: three sub-bullets, the platform-and-assignment sentence kept whole under
  *Runs this step:* (two things, one grade, ruling D5). Sputter targets: supplier bullet, R-REPEAT only.
* **R-RELATED.** Previous / Next split; "The plugs it lands on …; the contacts to it from above …" named
  two relationships → `Depends on:` and `Feeds:`; the TiN films → `Same category:`; "Why the poly is
  not silicided …" keeps its own gloss as label (as 098).
* **R-OPENQ.** "Deposition conditions", "Stack-diagram label", "As-deposited value" (no numbers in the
  labels). The 90-word stack-diagram item: the observation with its markers as the lead (37 words, no
  seam without losing the contrast — listed), then a continuation; the 55-word reading sentence split
  at its semicolon, and `[^pdk-04]`, which closed the whole base sentence, is repeated on the
  drawing-description half (declared ADDED). (0.9361 + 0.075 = 1.0111 checked.)
* **R-GLANCE.** Public numbers `li` 0.1 µm `[^pdk-04]` and 12.8 Ω/sq `[^pdk-08]`; tool line names both
  grades and what each covers; Not public from Open questions 1.
* **Preservation.** ADDED: glance (`pdk-04`, `pdk-08`, `skw-01`, 0.1, 12.8, metal 1's 1, quotes, `li1`,
  `metal-1`, hedges) and the repeated `[^pdk-04]`. LOST: the R-REPEAT copies and the rule-table
  number order (both above). WORDS LOST besides those: "strength" (R-TOOLS label), "wide" (li.7's
  "0.290 µm wide" → the row "resistor form width | 0.290 µm"), "with", "an", "as", "and" (list joins).
* **Marker coverage.** 20 flags read: list bullets and table rows under their lead-in marker, halves
  of split sentences each keeping their own markers, glance lines, the tool head. None lost.
* **Caps after:** 0 / 0 / 0 / 0. Item leads over 30: "Origins" (40), stack-diagram question (37).

### 102 LI1M — done (model: 093)

* **Lead.** The 57-word second sentence split at its semicolon ("… wiring level. Everything else is
  etched away …"). Lead 97 words, one paragraph; first sentence 8 words.
* **R-H3.** `### What the public record shows` after the figure caption (186-word PDK passage, ending in
  the hedged OPC inference), as on 093.
* **R-TABLE.** The 81-word rule enumeration → `Rule | Constrains | Value`, eight rows in the base order;
  the end marker `[^pdk-periph]` on the lead-in "… and give:" (R-TABLE step 3). Units in each cell
  (µm, µm² and the unitless ratio 10 differ, batch ruling). li.1a and li.3a restore the elided
  "width" / "spacing" from their parent rules. `LOST number_order` hand-checked (rule-table form, as
  093): li.1 0.170 µm; li.1a 0.140 µm; li.2 10; li.3 0.170 µm; li.3a 0.140 µm; li.5 0.080 µm; li.6
  0.0561 µm²; li.7 0.290 µm — same values, same order. At 400 px the Value cells wrap between number
  and unit (no number is broken; no horizontal scroll). The mask-table sentence split at its
  semicolon (two separately cited facts); the minimum-CD sentence split at ", and the "other
  criteria" table", its elided verb restored ("carries").
* **R-CATEGORY.** Classification sentence (33 words) ends at "which makes the task easier."; the colon's
  explanation is the one remaining sentence (a paragraph, no label). "What is specific …" is its own
  label (step 3); the 54-word substrate sentence split at its colon and at ", but the nitrogen"
  ("But the nitrogen …" — a sentence, not a paragraph, opening on the split's own conjunction).
* **Why.** Density, Enclosure of plugs, Proximity correction and Resist over TiN each split at their
  semicolon into a lead ≤ 30 words and a continuation. On Density `[^pdk-periph]`, which in the base
  sat mid-sentence after li.1a/li.3a, is repeated on the li.1/li.3 half so the 0.17/0.34 µm rule
  figures keep their citation (declared ADDED).
* **How.** Scope sentence italic. Exposure (116 words): split at its semicolon and before "We infer a
  **DUV (KrF) exposure …**" — lead (i-line excluded), continuation (248 nm and ITRS), continuation
  (the inference with "not public — SkyWater lists both", Brunner). k₁ arithmetic not shown as
  operations on the page, so no R-DERIVATION; values checked: 0.17 × 0.6 / 0.365 = 0.279; 0.17 ×
  0.6–0.7 / 0.248 = 0.41–0.48.
* **R-TOOLS.** As 093, word for word apart from the step code and "0.17 µm and 0.14 µm rules":
  DUV stepper/scanner three-line; Tracks *Tool exists:*; Overlay/CD *Tool exists:* + *Runs this
  step:*.
* **R-RELATED.** Previous / Next split; "The contacts the pattern must cover …; the contacts that will
  land on it …" → `Depends on:` and `Feeds:`; the other DUV layers → `Same category:`; "Mask page:" →
  `Mask:` (WORDS LOST "page", as 093).
* **R-OPENQ.** "Exposure tool and resist" (093's), "Add/drop values", "Barrier or ARC layer".
* **R-GLANCE.** As 093: li.1/li.3 0.170 µm `[^pdk-periph]`, the "Li1 proximity correction" 0.25 µm
  `[^pdk-03]`; tool line with both grades named.
* **Preservation.** ADDED: glance and the repeated `[^pdk-periph]`. LOST: the rule-table number order
  (above). WORDS LOST: "strength"×3 (R-TOOLS labels), "page", "of" (li.2's "ratio of 10" → the Value
  cell).
* **Marker coverage.** 9 flags read: table rows under the lead-in marker, the split criteria sentence
  (each half keeps its `[^pdk-03]`), glance and tool head. None lost.
* **Caps after:** 0 / 0 / 0 / 0.

### 103 LI1ME — done

* **Lead.** Base 140 words in one paragraph → two (70 + 69) at the seam before "What remains"; lead
  139 words (base over 120; text before the figure). The 55-word second sentence: its dash material
  ("wherever a tungsten plug lies outside the LI pattern, which the rules forbid (licon.4,
  li.5[^pdk-periph]) but overlay can cause") becomes its own sentence, "Wherever …, it stops on the top
  of a tungsten plug." ("it" = the etch, the previous sentence's subject; "it stops" added, "and"
  dropped). `[^pdk-periph]` stays on the rule clause, `[^pdk-04]` on the film. The 51-word "What
  remains" sentence split at its colon.
* **R-REPEAT — applied (declared).** Deleted from the post-figure passage (base `103-li1me.md:38–41`):
  "SkyWater names two metal etchers with TiN among their materials — "Lam 9600, Al, TiW, TiN, Pt" and
  "Lam 2300 Versys, Al, TiW, TiN, Nb, Pt".[^skw-01]" The surviving copy is the *SkyWater says:* line
  under `## Machines likely used at SkyWater` (home for tool quotations): "lists "Lam 9600, Al, TiW,
  TiN, Pt" and "Lam 2300 Versys, Al, TiW, TiN, Nb, Pt".[^skw-01]", with *Tool exists:* "**strong** for
  the tools and for TiN being among their etched materials"; that they are metal etchers stays under
  `## Machines typically used` ("Metal etcher … Lam TCP 9600 and 2300 Versys Metal"). The passage now
  reads "The public evidence for how it is done is the capability list, quoted under Machines likely
  used at SkyWater.[^skw-01]" (pointer clause 8 words; marker kept). `LOST quotes` for the two
  quotations and WORDS LOST "al", "tiw", "pt", "nb", "names", "two", "metal", "etchers", "with" are
  the deleted copy; hand-verified against the home copy.
* **R-CATEGORY.** Classification sentence alone (33 words); the category-page chemistry sentence as a
  second paragraph (the one remaining sentence before the step's own label); "What is specific …"
  (its own label, step 3) with the inference sentence as a third paragraph. No sentence over 45.
* **Why.** CD control split at its semicolon (lead 37 words: the only earlier seam, ", and the "Li1
  proximity correction" entry … the lithographic part", would take that clause out from under "we
  infer" — over the 30-word target, listed). **Selectivity to oxide left byte-identical** (61 words,
  one over the item cap): it holds "(on the CMPP cap-stop reading, only the cap oxide separates them)",
  which the S7 figure notes ask to keep verbatim; see Content problems. Residue and stringers,
  Precedent split at their semicolons. Charging: split at its semicolon; the 13-word li.2
  parenthetical becomes "The li.2 rule is a maximum length-to-width ratio of 10 for LI without a
  licon or mcon.[^pdk-periph]" after the sentence that names li.2 (its marker moves with it; "The …
  rule is" added so the sentence does not open on a lower-case rule id).
* **How.** Scope sentence italic. Chamber: the 27-word parenthetical keeps "(Lam's TCP source of the
  Ogle patent[^pat-tcp-lam])" inline (attribution); the SkyWater and Lam 10-K clauses become a
  sentence. Main etch: split at its semicolon (lead 38 words with its two short parentheticals and the
  "typical industry conditions" hedge — listed); Endpoint split at its semicolon. Metrology: the
  63-word test-tile sentence → lead-in "The published SKY130 test tile has:" carrying
  `[^raw-data-testtile-pads]` (it closed the enumeration, R-LIST step 1) and three plain sub-bullets;
  the 13-word "(the sheet gives no unit; we read micrometres …)" hedge becomes its own bracketed
  sentence inside item 1, word for word.
* **R-TOOLS.** Lam 9600 / 2300 Versys: three-line. AMAT DPS II: pilot form (SkyWater's gases and this
  reference's "could etch TiN" are one sentence); "Strength: medium" → *Runs this step:* medium (it
  grades the "could etch TiN" use, not existence — as 077's DPS II). Strip and clean: *Tool exists:*.
* **R-RELATED.** Previous / Next split; the film, stop and plugs → `Depends on:`; the later metal and
  capacitor-plate etches → `Same category:`; "Category pages:" kept.
* **R-OPENQ.** "Etch chemistry and tool", "BARC, hard mask and strip", "Oxide loss over the gates".
  In item 1, "chlorine-on-a-metal-\n  etcher" (rendered "metal- etcher") rejoined as
  "chlorine-on-a-metal-etcher" — whitespace only.
* **R-GLANCE.** Public numbers the 0.1 µm film `[^pdk-04]` and li.1/li.3 0.17 µm `[^pdk-periph]`; tool
  line with both grades named; Not public from Open questions 1 and 3.
* **Preservation.** ADDED: glance only. LOST: the R-REPEAT quotations (above). WORDS LOST besides:
  "strength"×3 (R-TOOLS labels).
* **Marker coverage.** 8 flags read: the lead split (each half keeps its own marker), the test-tile
  sub-bullets under the lead-in marker, glance and tool head. None lost.
* **Caps after:** 0 paragraphs, 1 item (Selectivity to oxide, 61, kept verbatim), 0 sentences, 0
  cells. Item leads over 30: CD control (37), Main etch (38).
