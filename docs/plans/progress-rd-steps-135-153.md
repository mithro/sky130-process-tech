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
