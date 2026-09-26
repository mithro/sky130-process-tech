# Progress — readability batch 10, steps 135–140 and 150–153 (`topic/rd-steps-135-153`)

Writer: Opus. Started 2026-09-27 from `main` at `b285acd8`. Guide: `docs/plans/readability-guide.md`
§1, §2, §4.1, §5, §6, §7, §8, with the rulings of batches 4–9 (plain bullets over invented labels; no H3
where none of the four titles fits; R-CATEGORY's 35 words a target; the connective rule inside list
items; derivations under 120 words as a numbered list without an H3; a third lead paragraph only for
base leads over 120 words; "Because X, Y" is not a connective opener; rows differing in unit carry the
unit in each cell; R-REPEAT only when the other copy adds nothing, declared with the deleted text and
the survivor's location; no hand-inserted non-breaking spaces; "What is specific … is that X, and that
Y" over the cap → "… is that:" and one bullet per clause; one bullet per topic where a pronoun needs its
antecedent; a hyphen or slash at a source line break is joined; a blank line after the glance box's
closing `:::`; hedge scope at a semicolon split per R-SENTENCE step 5, "when in doubt, repeat").
Medium classes avoided (batch 4–9 reviews): a pronoun whose referent changes after a split; a marker
lost when dash material moves; a sentence moved below the grade that refers to it; glance wording that
strengthens a grade; a whole-sentence trailing hedge not repeated on every half of a split. Model
pages: 124, 120. One commit per page.

## Method, every page

* Baseline build and one desktop tile set per page before any edit (`tmp/shots/*-before*`,
  git-ignored); one final pair (1280 px, `--max-height 40000`; 400 px, `--max-height 60000`) after.
* Preservation: `uv run python tools/check_preserved.py --base HEAD --allow-regrouped <page>` against
  the commit before the page, no other flag; never `--allow-added`, never `--allow-dropdown-edits`.
  Every ADDED line is named in the page entry; every REGROUPED line read; `--strict-words` as the final
  run, every LOST word named.
* Marker coverage: `tmp/readability/rdtools.py cov` (git-ignored scratch script) pairs every sentence
  not verbatim in the base — split at full stops **and semicolons** — with its closest base sentence
  and flags any marker or hedge word the base sentence had and the new one lacks. Every flag read.
* Invariants: `rdtools.py inv` against the base: References section, footnote definitions, generated
  index-links block, `{figure}` blocks, `{dropdown}` blocks, quick-facts rows, H2 list and Deep-dive
  count identical; one admonition (the glance box, `:class: at-a-glance`) followed by a blank line; no
  duplicate H3; every glance marker recurs below; the scope sentence is the italic lead-in; no
  consecutive duplicate line, no line ending in a hyphen or slash in prose, no bare `>`, no NBSP.
* Caps: `rdtools.py caps` at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25) with
  `{figure}` blocks (captions), `{dropdown}` bodies, the generated block, `## References` and footnote
  definitions **excluded**; a leading bold run-in label is not counted into its sentence; a quotation
  counts as one word; an em dash is not a word (D3 of batch 9).
* Gates per page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`, `-W` build.

## Pages

### 135 CAPILD — done

Base `b285acd8`. Caps before: 4 paragraphs, 8 items, 11 sentences over; after: 0/0/0. Lead 224 words
(base 225) in three paragraphs of at most 100 words (base lead over 120, one paragraph).

* R-H3: `### What the public record shows` over the PDK and measured values (public record ending in
  our extraction); `### How the thickness is estimated` over the thickness passage (≥ 120 words,
  its subject the bound on the thickness).
* R-DERIVATION: the thickness bound as a three-step numbered list after "one can bound the
  thickness:", results in bold, hedge line "This is our arithmetic …" after it, word for word; "so"
  dropped at the head of step 2 (connective rule in list items). Arithmetic checked: 8.854e-12 × k /
  2e-3 F/m² = 4.43 nm × k; × 4 = 17.7 ≈ 18, × 5–6 = 22–27, × 7.5 = 33; 8.854/1.87 = 4.73 ≈ 4.7, ratio
  2/1.87 = 1.07 (7 %). Correct.
* R-LIST: the three listings of MiM capacitors (README, platform table, announcement) as sub-bullets
  under "SkyWater and Google list MiM capacitors among SKY130's features:" (dash → colon, "and"
  dropped); the three PDK statements that name `met2`/`via2` as sub-bullets under "… over metal 3, but:"
  in the Open question.
* R-CATEGORY: classification sentence to the colon (35 words); "Specific to this step:" two bullets
  ("its" → "The film's" restored noun, since `CAPILD2` is now the nearest noun; the step-coverage
  clause as its own sentence "Step coverage does not, because …", link text capitalised, same term
  target); the relatives sentence as a paragraph after the bullets.
* R-PARA/R-SENTENCE: lead split at the semicolon after CAPTIW1 and before "Its cross-section drawing"
  (marker `pdk-07` repeated, declared); PDK values split at the semicolon (`pdk-07` repeated, declared);
  measured paragraph split into two paragraphs and three sentences. The trailing hedge "(our extraction
  from the published measurements, … wafer)" covered the whole long sentence, so it now follows the
  three sentences as "These values are our extraction from the published measurements, with no
  correction …; the files record no …[^raw-data-passives]" (R-SENTENCE step 5/7: subject and verb
  added, the hedge's words unchanged, one marker as in the base). Why items split into first block +
  indented continuations at sentence or semicolon seams, no continuation opening on a connective;
  "Surface." parenthetical (12 words) split: "exposed (WTIAL3). The cap is TiW or TiN, which the public
  record does not settle (overview-metal-cap); the cap is …" (subject and verb added).
* Open question "The capacitor's metal level": the "We follow the metal-3 reading … supports further:
  … "Via3"; … one level lower (inference)" sentence split at the colon; "(inference)" covered the
  whole sentence and no other passage ties it to one clause, so it is repeated on the first half
  (declared ADDED hedge); `pdk-periph` repeated on the periphery-rules sub-bullet (declared).
* R-TOOLS: the C1 chamber as a three-line item; the two inferences (assignment, C1 = Concept One)
  stay whole under *Runs this step:* (step 3). The TEOS bullet has no "Strength:", unchanged.
* R-OPENQ labels; R-RELATED: Previous / Next / Same module (the second capacitor; Phase cell "MiM
  capacitors, metal 3–5, via 3–4" on 135–163) / Feeds (MM3E, VIM3/VIM3E) / Same category (LINIT) /
  Category page. R-HEDGE: italic scope lead-in. R-REPEAT: none (no 10-word run in two H2s).
* Preservation (`--allow-regrouped`): ADDED markers `pdk-07` ×2, `pdk-periph` (declared repeats);
  ADDED hedge `inference` (declared repeat); REGROUPED the PDK values, the measured sentence and the
  derivation (same digits, same order, checked by eye). With the glance box: the glance's numbers,
  markers, quote "C1", hedges. `--strict-words`: LOST `strength` only (R-TOOLS). `cov`: the flags are
  the glance box and the declared hedge cover.

### 136 CAPTIW1 — done

Base `63fac342`. Caps before: 3 paragraphs, 4 items, 11 sentences over; after: 0/0/0. Lead 223 words
(base 217, the added words are "It is", "The metal-3 conductor is", "the plate") in three paragraphs; first
sentence 10 words (base 41). The in-force note after the Why list is untouched and stays directly after
the list; nothing of it is repeated.

* Lead: first sentence split at the colon ("It is a blanket conductor film …"); the stack parenthetical
  (over 11 words, with a dash pair inside) made its own sentence after the sandwich sentence, "The
  metal-3 conductor is … qualified in 2013–2014 (overview-metal-cap).[^cyp-qtp-113005][^cyp-qtp-123907]"
  (the dashes round the ref became parentheses; markers with it); the TiW sentence split at the
  semicolon, "it" → "the plate" (restored noun), and its 40-word "(inference: …)" parenthetical kept
  whole as the following sentence "(Inference: … see overview-metal-cap.)", directly after its claim.
* Post-figure: "Its role is electrical (…) and mechanical: …" → "The plate's role is:" and two plain
  bullets, "electrical — …" / "mechanical — …" (the parentheses became a dash; marker with its clause).
  The ρ/Rs estimate is a single operation and stays inline. Arithmetic: 50–100 µΩ·cm / 5.8 Ω/sq =
  0.086–0.17 µm; correct.
* R-CATEGORY: classification sentence (13 words) split at the semicolon; the category-page pointer as
  a second paragraph; "What is specific here is that X rather than on metal: A, and B (inference …)"
  kept as one sentence presented as "… on metal:" and two bullets (only "and" dropped). The trailing
  "(inference from the geometry; the same concern shapes the TiN top plate …)" stays on the second
  bullet: the first carries its own "we infer", and the Newport Fab clause speaks of "the same concern"
  (damage), so the page ties the parenthetical to the stress clause. Listed for the reviewer.
* Why: item 1 split after "a flat, continuous dielectric." (the capacitance clause becomes its own
  sentence, so it is no longer inside the "Because …" clause; nothing else changed) and at the
  Freescale semicolon; item 2 (370 words) as the four criteria (i)–(iv) and the four reasons as
  sub-bullets under "The plate must be a metal that:" / "TiW satisfies all four:", "and" dropped at each
  list end; the Kar-Roy/Babcock clause split at its semicolon; the TiW-or-TiN balance as "… (overview):"
  and two bullets; the Philips dash material moved directly after its bullet as "A TiW plate over a TiN
  cap is the arrangement the Philips process relies on, stopping "…".[^pat-mim-philips]" (restored
  subject; "This" would have pointed at the TiN plate). Item 3 split at the semicolon; item 4's dash
  pair (Thornton, Dirks) moved to its own sentence directly after its clause, the crack clause after it,
  so "therefore" still follows it.
* How: italic scope lead-in; step 3 split at its semicolon ("(industry-typical)" stays with the recipe
  clause it sits in).
* R-TOOLS: the AMAT item as three lines; "the platform model … and the use of the same chamber … are
  inferences" kept whole under *Runs this step:*. The Lam etcher bullet has no "Strength:", unchanged.
* R-RELATED: Previous / Next / Same module (CAPTIW2) / Depends on (WTIAL3, MM3/MM3E) / Feeds (VIM3E;
  CMPM3) / Same category (TIAL6, TIAL12) / Category page. R-OPENQ labels. R-REPEAT: none.
* Preservation: every ADDED line is the glance box (markers `pdk-07`, `skw-01`, its numbers and hedges)
  or "metal-3" (the restored "The metal-3 conductor"); REGROUPED lines read (lead, criteria, quality
  factor), same digits in the same order. `--strict-words`: LOST `strength` (R-TOOLS); `its` (→ "The
  plate's"). `cov`: flags are pairing noise and the declared hedge placement.

### 137 CAPM — done

Base `a7e812b0`. Caps before: 3 paragraphs, 4 items, 9 sentences over; after: 0/0/0. Lead 146 words
(base 144) in two paragraphs. No H3 added: the post-figure passage is part public record, part
description of the surface, and none of the four titles is true of the whole.

* Lead: the "— which lies on … WTIAL3 —" dash material moved to its own sentence directly after its
  clause, "The plate film lies on …" (restored subject); the mask-table sentence split at the
  semicolon, "it" → "`CAPM`" (restored noun; the nearest noun is now "the mask name").
* R-LIST: the twelve `capm` periphery rules as nine bullets under "The periphery rules give a set of
  twelve `capm` rules, all with their numeric values shown as "N/A" on the public page:[^pdk-periph]"
  (the "— all with …" tail moved into the lead-in, the marker on the lead-in per R-LIST step 1; "give"
  added, dash removed; the minimum-CD sentence gains "and" for the elided "gives"). The surface
  sentence as "The surface is unusual for a mask step:" and three plain bullets (only "and" dropped).
* R-CATEGORY: classification sentence (12 words); "Specific to this step:" two bullets (the k₁/ASML
  sentence; "We therefore infer …" with "Nothing public states the tool or resist."), split at the
  semicolon. k₁ = 0.84 × 0.6 / 0.365 = 1.38 ≈ 1.4, correct. The "What the layer shares … device
  parameter: a 0.1 µm bias … (inference from the model form[^pdk-07])" sentence split at the colon into
  a paragraph after the bullets; the hedge stays on the bias clause only: its own words ("from the model
  form") name the `CMIMP` clause, and repeated on the reflectivity clause it would mark as inferred from
  the model something the model does not bear on. Listed for the reviewer (R-SENTENCE step 5).
* Why: item 1 split at "fitted for;"; item 2 into first block + two continuations at the semicolons
  (the continuation opens "The plate edge lands …"; "This is the construction" keeps its base position
  after that clause); item 3: "— the rules capm.3 … contact,[^pdk-periph] whose text names …" → "The
  rules are capm.3 … contact.[^pdk-periph] The rules' text names … (inference; see CAPILD)." (subject,
  verb and noun restored), and the alignment sentence's 17-word parenthetical as the following sentence
  "(Inference; … overlay.[^levinson-2005])", covering the whole sentence as before (the Open question
  names both alignments as not public).
* How: italic scope lead-in; step 1 split at the semicolon and the Brunner/Rocke parenthetical (19
  words) unparenthesised as its own sentence; step 2's dash (the DNQ chemistry) moved after its clause as
  "DNQ/novolac is the chemistry … describe." (restored subject) and the 22-word parenthetical split:
  "(industry-typical for i-line resists[^mack-2007])" stays with "around 1 µm", the PDK-thickness clause
  becomes its own sentence with `pdk-03`; step 5's 27-word parenthetical split, "(our reading of
  industry practice)" repeated on both halves (declared ADDED hedge), Levinson as its own sentence.
* R-TOOLS as on 124 (the same three items). R-RELATED: Previous / Next / Same module (MM3, MM3E) /
  Depends on (CAPILD) / Feeds (VIM3) / Same category (CAP2M) / Mask (with previous and next mask) /
  Category page. R-OPENQ labels. R-REPEAT: none.
* Preservation: ADDED = the glance box (markers, numbers, the `step-138` ref, hedges) and the repeated
  "our reading" (step 5); REGROUPED lines read (lead-in numbers, the capm.3/4/5 rules, the resist
  thickness), same digits in the same order. `--strict-words`: LOST `strength` ×3 (R-TOOLS), `page`
  ("Mask page:" → "Mask:"); `whose`, `which`, `it` non-strict (restored nouns).

### 138 CAPME — done

Base `4c0ea844`. Caps before: 5 paragraphs, 8 items, 17 sentences over; after: 0/0/0. Lead 93 words
(one paragraph, as in the base). Two in-force notes in the body and one in the Deep-dive list:
untouched, each still directly after the paragraph it belongs to ("… in the collapsed note below." and
"The other two patents …" before the first; "… the operation this step performs." before the second);
no pointer sentence shortened; nothing from them in the glance box. No H3 added (the post-figure
passage argues between readings but is not laid out as two competing readings under separate heads;
no title of the four is true of it as a whole).

* Lead: the dash material (TiW, ~0.1 µm on our reading) moved to its own sentence directly after its
  clause, "The film is TiW, as assumed there, of the order of 0.1 µm on our reading …" (restored
  subject; hedge verbatim).
* Post-figure: the cap identity as "… a refractory film of unknown identity:[^cyp-qtp-113005]
  [^cyp-qtp-123907]" and two bullets (both markers on the lead-in per R-LIST step 1; "or" dropped);
  "It is not yet patterned" → "The metal-3 stack is not yet patterned" (restored noun, new paragraph);
  the selectivity sentence's dash pair moved after it as "For a TiW plate on an oxynitride, as assumed
  here (see …), that is a fluorine-etchable metal over a fluorine-etchable dielectric." (subject and
  verb added); Philips/Newport split at the semicolon; the 309-word and 204-word paragraphs split at
  sentence seams, none opening on a connective ("Taken at that floor it is" → "the figure is",
  restored noun); "…(inference; Liu and Kuo …, and … the collapsed note above)" (a 30-word
  parenthetical) made the following sentence "(Inference; … above.)"; the next sentence's "It is a
  consideration that CAPTIW1 weighs …" → "The comparison is a consideration …" (restored noun, because
  "It" would now follow the parenthetical sentence; the base referent is the comparison of the
  paragraph's first sentence); "If it is the Ti/TiN …" → "If the cap is the Ti/TiN …" (new paragraph).
* R-CATEGORY: classification sentence with its dash tail (18 words); "Specific to this step:" three
  bullets — the fluorine/WF₆ sentence split at its semicolon; the Liu–Kuo clause with the "only
  selectivity they report" sentence in one bullet (pronoun "they"), the 83-word sentence split at the
  closing dash ("where" dropped) and at "; and at that floor" ("(our arithmetic)" stays with the
  arithmetic clause, which is the only arithmetic in the sentence) as a continuation of that bullet
  (so "that floor" keeps its antecedent); the chlorine sentence's dash (Fischl and Hess) as its own
  sentence directly after "Chlorine also etches both metals." ("and" dropped; "on our reading" stays
  on its clause). "What is specific … is the stop" split at the colon.
* R-REPEAT considered and not applied: the category bullet's selectivity sentence repeats the
  post-figure passage (the guide's own R-CATEGORY example), but it carries the only `liu-2007-tiw`
  marker for the Liu–Kuo clause before it, so deleting it would leave that clause of Step category
  unmarked (R-REPEAT "Do not touch"). Kept, restructured.
* Why: item 2's two dash pairs (the fluorides; the AlF₃ residue) moved to sentences after their
  clause, "Fluorine etches TiW as WF₆ and TiF₄, TiN as TiF₄." and "AlF₃ is a residue …" (restored
  subjects; `hess-1982` stays on the AlF₃ clause); item 3 split at the semicolons.
* How: italic scope lead-in; step 3's dash material ("Cl₂ (or BCl₃) … in argon") as "It is …" and its
  parenthetical hedge as the following sentence "(Industry practice …; Nojiri sets out the
  regime.[^nojiri-2015])"; step 4 split at the semicolon; step 5: the ash-tool dash and the solvent
  parenthetical as sentences directly after the ash/clean sentence ("The ash is the "Gasonic PEP" …"
  — the batch-9 L1 form), "No HF and no peroxide." then the peroxide reason unparenthesised with its
  "by inference"; step 6: the test-tile structures as five sub-bullets under "The published SKY130 test
  tile has:[^raw-data-testtile-pads]" ("and" dropped). Arithmetic re-done: solving 17 600 a + 1 760 p =
  35 500 fF and 5 040 a + 5 328 p = 11 100 fF gives a = 2.00 fF/µm², p = 0.194 fF/µm; the area-intensive
  structure then gives 12.37 pF (12.4); 33.26/35.5, 10.37/11.1, 11.57/12.4 = 6.3 %, 6.6 %, 6.7 % below.
  Correct. 0.1 µm / 2 = 50 nm, correct.
* R-TOOLS: Lam item (existence grade; "Which runs this step is not public." as continuation); strip
  item (existence + assignment). R-RELATED: Previous / Next / Depends on (CAPTIW1, CAPILD; WTIAL3) /
  Feeds (VIM3E) / Same category (LI1ME; CAP2ME) / Category page. R-OPENQ labels; the first Open question
  split into a lead (the question, 25 words), a continuation (its dash, the "greater than 2" floor,
  moved after the sentence; "(inference)" still ends the "We describe the former because …" sentence
  as in the base) and a second continuation (Philips).
* Preservation: ADDED = the glance box (markers, numbers, refs, hedges) and "metal-3" ×2 (restored
  nouns); REGROUPED lines read (cap stack list, test-tile list, selectivity arithmetic), same digits in
  the same order. `--strict-words`: LOST `strength` ×2 (R-TOOLS), `where` (the connective at the
  category split); `it` non-strict.

### 139 MM3 — done

Base `49fc160b`. Caps before: 4 paragraphs, 8 items, 12 sentences over; after: 0/0/0. Lead 160 words
(as the base) in three paragraphs (base over 120; no paragraph opens on a connective).

* R-H3/R-TABLE (model 124): `### What the public record shows` over the mask-table, rule and
  thickness passage; the mask-table sentence split at its semicolon; the 125-word periphery-rule
  sentence as a `Rule | Constrains | Value` table after "The periphery rules for the flow described
  here give:[^pdk-periph]" (the lead-in marker covers every row, R-TABLE step 3), base order kept
  (m3.1, m3.2 with the pitch dash in its cell, m3.3c/d, m3.6, m3.4, m3.pd.1 with `RR` and the window
  in its cell, via3.4, via3.5), units in each cell; after it the dash aside "The assumptions table's
  separate, global "Min pattern density for oxide" is 0.75.[^pdk-03]" and "The layer also carries a
  `cmm3 waffleDrop` fill check.[^pdk-periph]" (the 124 form; `pdk-periph` repeated, declared). The
  `number_order` LOST line is this sentence; re-paired by hand against the base: 0.300 µm (m3.1),
  0.300 µm (m3.2; 0.6 µm pitch, 0.28 µm), 0.400 µm (m3.3c, m3.3d), 0.240 µm² (m3.6), 0.065 µm (m3.4),
  0.7 (m3.pd.1, 700 µm, 70 µm), 0.75 (assumptions table), 0.060 µm (via3.4), 0.090 µm (via3.5). The
  via-3 cells read "enclosure of the via-3 plugs that will later land on metal 3" / "… on one of two
  adjacent sides" (the base's "must be enclosed by it by" → cell wording, as on 124; `enclosed`,
  `must`, `by` are the LOST words).
* R-CATEGORY: classification sentence (27 words); "Specific to this step:" three bullets: "`MM3` is,
  however, no longer a critical layer …" ("It" → `MM3`, restored noun, since the bullet follows the
  label); the two k₁ values split into two sentences, "(our arithmetic)" repeated on the first (it
  covered the whole sentence; declared ADDED hedge; k₁ = 0.847 ≈ 0.85 and 0.493 ≈ 0.49, correct);
  SkyWater's list split at the semicolon ("Which prints metal 3 is not public, and either is plausible
  … (inference; …)" keeps its own hedge). "What is specific to this instance is the substrate" keeps its
  paragraph; its 74-word sentence split at the colon ("Like MM4, it is printed over a partly built
  device.") and the three things the resist sees as bullets, each dash in place, "and" dropped; the
  "two different thin-film stacks" dash stays directly after the plate item, where the base had it.
* Why: items split into first block + continuation at semicolons; the enclosure item's "(inference;
  Levinson's …)" stays on the alignment-tree sentence only: the first half ("The metal must enclose
  the via-2 plugs by 0.065 µm (m3.4)[^pdk-periph] and the capacitor plates by the unpublished capm.3
  value") is the PDK's rule, which the page cites and does not infer. Listed for the reviewer.
* How: italic scope lead-in (with its MM1 pointer, as on 124); step 1 split ("A dehydration bake …
  (inference). Then an organic BARC …"); step 2 at the semicolon; step 5: the dash (which marks) as
  "The marks are the via-2 level or the metal-2 targets it was aligned to." after the sentence, and the
  20-word parenthetical as the following sentence "(Our reading of industry practice; … not public.)",
  covering both.
* R-TOOLS as on 124 (the three items). R-RELATED: Previous / Next / Depends on (WTIAL3; the capacitor
  module; the via-2 plugs) / Feeds (NILD5; VIM3) / Same category (the other metal masks) / Mask (with
  previous/next mask) / Category page. R-OPENQ labels; the TLM/S8TM/PLM item split into first block +
  continuation. R-REPEAT: none.
* Preservation: ADDED = the glance box, the repeated `pdk-periph` and "(our arithmetic)", restored
  nouns (`MM3`, "via-3" in the via3.5 cell) and the Open-question label "TLM, S8TM and PLM" (`S8TM`);
  REGROUPED lines read. `--strict-words`: LOST `strength` ×3, `page` ("Mask page:"), `enclosed`,
  `must` (table cells).

### 140 MM3E — done

Base `32241413`. Caps before: 3 paragraphs, 9 items, 12 sentences over; after: 0/0/0. Lead 173 words
(base 168) in two paragraphs. The lead's "a chlorine plasma removes … first whatever remains of the
CAPILD dielectric outside the capacitor plates" is kept word for word (see Content problems).

* Lead: the "removes everything down to the via-2 level: first …, then …" sentence split at the colon
  ("It removes first …", subject and verb added; "It" = the chlorine plasma, the only candidate), the
  stack dash as "The stack is a refractory cap, a thick Al–Cu layer and a thin refractory bottom
  layer." directly after it; the `met3` sentence split at its semicolon.
* R-H3: the bold run-in "**How thick is the metal?**" that introduces the whole thickness passage →
  `### How thick is the metal?` (R-H3 step 4); the 253-word paragraph in four paragraphs at sentence
  seams; the two Cypress reports split at the semicolon ("and" dropped); the R7FT-3R sentence at its
  semicolon. No table: the numbers are three reports' own quoted stacks and two PDK readings with
  different kinds of claim attached to each ("which shows …", "whereas …"); the prose split keeps them.
  Arithmetic: 150 + 7 200 + 300 = 7 650 Å; 500 + 21 250 + 300 = 22 050 Å ≈ 2.2 µm; 150 + 8 000 + 300
  = 8 450 Å = 0.845 µm; 47 mΩ/sq × 0.72–0.80 µm = 3.4–3.8 µΩ·cm. Correct.
* R-CATEGORY: classification sentence with its dash tail (30 words); the MM1E pointer sentence as a
  paragraph; "Three things are specific to this instance:" (the page's own announcing sentence, R-LIST)
  and three bullets; "And" dropped from the third; its 20-word parenthetical as the sentence "For an
  oxynitride, as assumed at CAPILD, the dielectric is a film which …" (subject and verb added) in a
  continuation, and "which, on this reference's reading of CAPME, makes this one of …" → "On this
  reference's reading of CAPME, that makes this one of …" (the relative pronoun as "that").
* Why: items split into first block + continuations at semicolons; the stringer sentence's and the
  charging sentence's long parentheticals ("(inference from the stack; the Newport Fab patent …)",
  "(inference from the geometry; Wang, Ackaert et al. …)") made the following sentences "(Inference …
  .[^…])", each directly after the one sentence it qualified.
* How: italic scope lead-in (with its MM1E pointer); step 2 split, its "(industry practice; …
  Oehrlein …)" parenthetical as the following sentence after the breakthrough sentence only: its
  markers (Liu–Kuo, Abraham) are the cap-breakthrough sources, and the BARC-open clause before the
  semicolon is covered by the section's scope sentence like every other step. Listed for the
  reviewer. Step 3 into first block + continuation; step 7: the ash-tool dash and the solvent
  parenthetical as two sentences after the ash/clean sentence ("SkyWater lists GaSonics, Iridia and
  Mattson strippers …" — "strippers" names them as the ash tools); step 8 into first block +
  continuation.
* R-TOOLS: Lam item (three lines; the "(inference: the coarser, thicker level …)" stays with the
  assignment); strip item. Resources: the 20-word "(industry practice; SkyWater lists no gases …)"
  parenthetical split, "(industry practice[^nojiri-2015])" stays on the gas list.
* R-RELATED: Previous / Next / Depends on (WTIAL3; CAPILD, CAPTIW1, CAPME; NCAPOX4, WCMP4) / Feeds
  (VIM3E) / Same category (the other metal etches) / Category page. R-OPENQ labels; the thickness item
  split at its semicolon into first block + continuation (the question); the bottom-layer item's
  20-word "(as in the S8DI report, where metal 3 is …)" split: "(as in the S8DI report[^cyp-qtp-123907])"
  stays, "where …" → "In the S8DI report metal 3 is that three-metal flow's **top** metal, so the
  comparison is not level for level." in the continuation.
* Preservation: ADDED = the glance box (markers, numbers, `step-139`, hedges, identifiers), "S8DI"
  (the restored antecedent of "where"), "metal-3"/"via-2" in the glance; REGROUPED lines read.
  `--strict-words`: LOST `strength` ×2, `where` (→ "In the S8DI report").

### 150 CAPILD2 — done

Base `dbcbbff4`. Caps before: 6 paragraphs, 8 items, 14 sentences over; after: 0/0/0. Lead 162 words
(as the base) in three paragraphs.

* Lead: split at the step-list semicolon and at the dash that introduces the evidence for the
  oxynitride reading (the evidence sentence follows its claim directly); the CAPTIW2 sentence at its
  semicolon.
* R-H3: `### What the public record shows` over the PDK record, the thickness bound and the published
  measurements (public record ending in our arithmetic and our extraction); the bold run-in
  "**Where the public record is inconsistent.**" that introduces its own passage →
  `### Where the public record is inconsistent` (R-H3 step 4).
* PDK record: the device-page sentence split at its semicolon ("it names the cells" → "The device page
  names the cells", restored noun; `pdk-07` repeated on the first half, declared); the layer/stack
  sentence split before "The device's cross-section" ("and" added before the stack-diagram clause).
* R-DERIVATION: the thickness bound as a two-step numbered list, results in bold, the trailing
  "(our arithmetic with an assumed permittivity)" as the hedge line after the list "(Our arithmetic with
  an assumed permittivity.)", word for word; `pdk-04` stays with the nitride k. Arithmetic as on 135
  (4.43 nm × k), correct.
* Measurements: the 212-word paragraph in three; the 72-word sentence at its semicolon; "…, so the
  levels do not differ by a simple area capacitance, and an area-plus-periphery model …" split at
  ", and"; the final 28-word parenthetical "(our extraction … wafer)" made the following sentence
  "(Our extraction … wafer.)[^raw-data-passives]". Arithmetic: 35.27 pF / 17 600 µm² = 2.00 fF/µm²;
  68.78 / (33.26 + 35.27…35.29) = 1.0034–1.0036 (0.3–0.4 %). Correct.
* Inconsistency passage: "Other PDK tables do not match this picture:" and the three tables as bullets
  (the base's next sentence, "The mask table lists …", becomes the list; markers stay with each table);
  paragraph split before *Previous Nomenclature*.
* R-CATEGORY: classification sentence (13 words); "Specific to this step:" two bullets (the device-layer
  clause as "`CAPILD2` is one of the two PECVD films …", subject and verb added; the gate-oxide
  sentence with "Step coverage does not, because …" as on 135); the "What is specific to this
  instance …" paragraph kept, its stacked-pair sentence split at the colon and at ", so" (a sentence,
  not a paragraph, opening "So", R-PARA step 2).
* Why: item 1 split at its semicolon ("(our arithmetic from the identical CMIMA and CMIM2A)" stays on
  the doubling clause its words name) into first block + two continuations; item 2's three listings as
  sub-bullets (as on 135); item 3's over-long source line re-wrapped and split at its semicolon;
  items 4 and 5 into first block + continuation ("and" dropped before Bose).
* How: italic scope lead-in (with its CAPILD pointer); step 1 split at its semicolon ("That surface is
  the bottom electrode …"); step 5's 13-word parenthetical as its own sentence "The first capacitor
  lies below via 3 and metal 4 on the PDK's stack diagram.[^pdk-04]" and the unindented source line
  re-indented.
* R-TOOLS: the C1 chamber (three lines; the two inferences whole under *Runs this step:*); the TEOS
  and HP 4062UX bullets have no "Strength:", unchanged. R-RELATED: Previous / Next / Same module (the
  first capacitor) / Feeds (MM4E; VIM4, VIM4E) / Category page. R-OPENQ labels; the levels item split
  at "while" into two sentences, the seven markers kept in their order, each sentence with the markers
  of the sources it names (device page, layer table, stack diagram; mask table, minimum-CD table,
  periphery rules, extraction page).
* Preservation: ADDED = the glance box (markers, numbers, the quote "C1" ×2, hedges, identifiers) and
  the repeated `pdk-07`; REGROUPED lines read. `--strict-words`: LOST `strength`; `while`, `it`
  non-strict.

### 151 CAPTIW2 — done

Base `2a4a383c`. Caps before: 4 paragraphs, 4 items, 9 sentences over; after: 0/0/0. Lead 201 words
(base 198) in three paragraphs; first sentence 10 words (base 30). Same treatment as 136 wherever the
two pages share wording.

* Lead: first sentence split at the colon ("It is a blanket titanium–tungsten layer …"); the step-list
  sentence at its semicolon; the TiW sentence as on 136 ("it" → "the plate"; its "(inference: …)"
  parenthetical as the following sentence "(Inference: … as set out below.)").
* Post-figure: "Its thickness" → "The plate's thickness" (new paragraph); the 24-word "(textbook range
  …; Hartsough's 1979 paper …)" parenthetical as the following sentence "(Textbook range …
  readable.[^hartsough-1979])" directly after the ρ/Rs sentence (its hedge qualifies the one range in
  that sentence). This is the `number_order` LOST line (50–100, 1979, 5.8, 0.09, 0.17 → the same
  digits in the same order across the two sentences, hand-checked). The via-4 sentence (86 words):
  split at ", and it will be contacted" ("The plate will be contacted …", restored noun), its dash
  material as "That is four times the width … (via3.1a).[^pdk-periph]" directly after the 0.800 µm
  square it glosses, and "which lands on the plate" → "The opening lands on the plate" (restored
  noun). Markers unchanged in number and place.
* R-CATEGORY: classification sentence split at its semicolon (13 words); the category-page pointer as
  a paragraph; "As at CAPTIW1, what is specific is the substrate: …" kept as its own paragraph; its
  46-word last sentence split at ", and the film's stress", "(inference from the geometry)" repeated on
  the first half (it covered the whole sentence; declared ADDED hedge).
* Why: item 1 as on 136; item 2 (176 words): first block (the requirements, 40 words, no list needed),
  continuation with the TiW reasons split at the semicolons, continuation with the published
  alternatives; item 3: the 15-word "(our reading of the artwork; the drawing labels the vias only as
  …)" parenthetical split — "(our reading of the artwork)" stays on the via-shape clause, "The drawing
  labels the vias only as "Via3" and "Via4".[^pdk-07]" follows the sentence; item 4 as on 136.
* How: italic scope lead-in (with its CAPTIW1 pointer); step 3 split at the semicolon.
* R-TOOLS: AMAT item as on 136; the Lam bullet has no "Strength:", unchanged. R-RELATED: Previous /
  Next / Same module (CAPTIW1) / Depends on (WTIAL4, MM4/MM4E) / Feeds (VIM4E; CMPM4) / Same category
  (TIAL6) / Category page. R-OPENQ labels. R-REPEAT: none.
* Preservation: ADDED = the glance box (markers, numbers, the quote, `step-150`, hedges, `MiM2`,
  `cap2m`) and the repeated "(inference from the geometry)". `--strict-words`: LOST `strength`; `its`,
  `which` non-strict (restored nouns).

### 152 CAP2M — done

Base `04e5073a`. Caps before: 4 paragraphs, 5 items, 8 sentences over; after: 0/0/0 (one "sentence of
49 words" that `rdtools caps` and `measure.py` report is two sentences, 17 and 31 words: the second
opens with the numeral "0.1 µm", which their splitters do not treat as a sentence start). Lead 108
words (base 106) in two paragraphs. Same treatment as 137 wherever the two pages share wording.

* Lead: the "— which lies on … WTIAL4 —" dash as "The plate film lies on …" directly after its
  sentence; "It is one of the two capacitor-plate masks" → "`CAP2M` is one of …" (new paragraph,
  restored noun).
* R-H3/R-LIST: `### What the public record shows` over the record passage; "Less is public about this
  mask than about any neighbour:" and the three tables as bullets (markers with each); "What is
  public is that:" and one bullet per "that" clause (only "that"/"and" dropped; the batch-8 form);
  paragraph split before the test-tile sentence. The surface sentence as "The surface is the same
  kind as at CAPM:" and three bullets (as on 137). 71 pF = 2 × 35.5 pF, consistent.
* R-CATEGORY: classification sentence (12 words); "Specific to this step:" three bullets (k₁ with
  its hedge; the ASML sentence split at the semicolon; "We therefore infer … Nothing public states
  the tool or resist."); k₁ = 1.38 ≈ 1.4, correct. "What is specific to this instance is its place
  in a stack." keeps its paragraph; the 68-word CD-error sentence: its dash material ("0.1 µm of edge
  bias … (our arithmetic)") as a sentence directly after "A CD error on either plate changes the
  capacitance of its half", the misregistration clause as its own sentence ("and" dropped), and the
  trailing "(inference from the geometry)" repeated on the CD-error sentence (it covered the whole
  sentence; declared ADDED hedge).
* Why: items split into first block + continuation at semicolons; the Newport Fab line re-wrapped;
  the charging item split at ", so" (a sentence opening "So", R-PARA step 2).
* How: italic scope lead-in (with its CAPM pointer); step 1's dash split (the Brunner/Rocke sentence
  as a continuation); step 5's 12-word parenthetical split: "(our reading of industry practice)"
  stays on the alignment sentence it covered, Levinson as its own sentence.
* R-TOOLS as on 137 (the quoted heads keep their quotation marks). R-RELATED as on 137: Previous /
  Next / Same module (MM4, MM4E) / Depends on (CAPILD2) / Feeds (VIM4) / Same category (CAPM) / Mask
  (with previous/next mask) / Category page. R-OPENQ labels. R-REPEAT: none.
* Preservation: ADDED = the glance box (markers `pdk-07` ×2, `pdk-periph`, `skw-01`, its numbers,
  `step-153`, hedges, identifiers) and the repeated "(inference from the geometry)"; REGROUPED
  lines read. `--strict-words`: LOST `strength` ×3, `page` ("Mask page:"); `it`, `which` non-strict.

### 153 CAP2ME — done

Base `da0240bf`. Caps before: 4 paragraphs, 8 items, 10 sentences over; after: 0/0/0. Lead 119 words
(as the base) in two paragraphs. Same treatment as 138 wherever the two pages share wording. The in-force
note in the body is untouched and still directly after the paragraph that ends with the Philips and
Newport Fab sentences (as in the base); the one in the Deep-dive list is untouched.

* Lead: the dash pair (TiW, ~0.1 µm, an inference from the PDK's 5.8 Ω/sq[^pdk-07]) closes the first
  half as a comma apposition, "… film of CAPTIW2, described in this reference as TiW … resistance.
  [^pdk-07]", and "and stops on" → "It stops on …" ("It" = the plasma, the subject of the sentence
  before). A first draft that added "The film is …" took the lead from 119 to 122 words, over the
  120 cap the base met; this form adds no word.
* Post-figure: the cap identity as "… whose cap is:" and two bullets, each dash and marker in place;
  the absolute "which of the two SKY130's metal 4 carries not being public[^cyp-qtp-123907]
  (overview-metal-cap)" stays at the end of the second bullet, word for word, where the base had it;
  paragraph splits before "If the etch went through" and "Other published processes"; the
  Philips/Newport sentence split at ", and". "Which of these SKY130 follows" paragraph: the
  cross-section sentence split at the semicolon; the 78-word "we describe … — "greater than 2" … —
  and because … (inference)" sentence: the dash material as the following sentence "The selectivities
  are "greater than 2" …, which are not directly comparable." (subject and verb added); "(inference)"
  stays on the "we describe … because …" sentence it closed, which the Open question words the same
  way ("… a through-etch offers no selective stop (inference)"); the TiN-cap sentence split at its
  semicolon.
* R-CATEGORY: classification sentence with its dash tail (30 words); "Specific to this step:" three
  bullets (the WF₆/Liu–Kuo sentence; Fischl and Hess; the chlorine-blend sentence with its dash
  material as "Such a flow is the scheme of the Texas Instruments patent in the collapsed note above."
  — restored noun — and Flamm/Winters as a continuation). "What is specific to this instance is the
  history of the wafer" keeps its paragraph; its 66-word sentence split at the semicolon and its
  20-word "(inference from the PDK's stacked cross-section, …)" as the following sentence "(Inference
  …)", covering both halves.
* Why: items 2 and 3 into first block + continuation; item 3 split at its semicolon.
* How: italic scope lead-in (with its CAPME pointer); step 3 split at the semicolon ("(industry
  practice; Nojiri …)" stays on the chemistry sentence); step 4 split at the semicolon; step 5: the two
  dashes (the strippers; the batch rotational tools) as sentences directly after "Downstream O₂/N₂ ash,
  then a solvent clean.", "which must remove" → "The clean must remove …" (restored noun; "(requirement,
  not a property of the named products)" still follows the naming), then the peroxide sentence; step 6
  into first block + two continuations.
* R-TOOLS as on 138. Resources: the 25-word parenthetical split as on 138. R-RELATED as on 138:
  Previous / Next / Depends on (CAPTIW2, CAPILD2; WTIAL4) / Feeds (VIM4E) / Same category (CAPME;
  LI1ME) / Category page. R-OPENQ labels; the first item into first block + continuation.
* Preservation: ADDED = the glance box only (markers, numbers, refs, hedges, identifiers); REGROUPED
  lines read. `--strict-words`: LOST `strength` ×2 only.
