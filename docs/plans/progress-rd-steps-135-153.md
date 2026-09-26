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
