# Progress — readability batch 11, steps 141–149 (`topic/rd-steps-141-149`)

Writer: Opus. Started 2026-09-27 from `main` at `e9bbf1a6`. Guide: `docs/plans/readability-guide.md`
§1, §2, §4.1, §5, §6, §7, §8, with the rulings of batches 4–10 (plain bullets over invented labels; no
H3 where none of the four titles fits; R-CATEGORY's 35 words a target; the connective rule inside list
items; derivations under 120 words as a numbered list without an H3; a third lead paragraph only for
base leads over 120 words; "Because X, Y" is not a connective opener; rows differing in unit carry the
unit in each cell; R-REPEAT only when the other copy adds nothing; no hand-inserted non-breaking
spaces; "What is specific … is (that) X, and (that) Y" over the cap → "… is (that):" and one bullet per
clause; one bullet per topic where a pronoun needs its antecedent; a hyphen or slash at a source line
break joined; a blank line after the glance box's closing `:::`; hedge scope at a semicolon split per
R-SENTENCE step 5 and D1). Medium classes avoided (batch 4–10 reviews): a pronoun whose referent
changes after a split; a marker lost when dash material moves; a sentence moved below the grade that
refers to it; glance wording that strengthens a grade; a whole-sentence trailing hedge not repeated on
every half of a split. Model pages: 126, 129 (batch 9), 139 (batch 10). One commit per page.

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
  count identical; one admonition (the glance box) followed by a blank line; no duplicate H3; every
  glance marker recurs below; the scope sentence is the italic lead-in; no consecutive duplicate line,
  no prose line ending in a hyphen or slash, no bare `>`, no NBSP.
* Caps: `rdtools.py caps` at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25) with
  `{figure}` blocks (captions), `{dropdown}` bodies, the generated block, `## References` and footnote
  definitions **excluded**; a leading bold run-in or italic R-TOOLS label is not counted into its
  sentence; a quotation and a code span count as one word; an em dash is not a word.
* Gates per page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`, `-W` build.

## Pages

### 141 NILD5 — done

Base `e9bbf1a6`. Caps before: 3 paragraphs, 7 items, 13 sentences over; after 0/0/0. Lead 164 words
(base 159, one paragraph) in two paragraphs (89, 75); first sentence 11 words.

* Lead: the dash material "0.845 µm tall … (m3.2)" moved after the sentence as "The lines are 0.845 µm
  tall …" with both markers (126 form); the sentence split before CMPM3 ("which" → "CMPM3 then polishes
  that layer flat and NCAPOX5 caps it"); the "_C" sentence split at ", and the diagram's levels". The
  trailing "(our arithmetic from the diagram)" stays on the levels sentence: its other half ("drawn with
  no separate "_C" film") is cited to `pdk-04`, which states it (D1).
* R-LIST: "Two things make this gap fill different …:" two bullets, each bolding its own opening words
  in place ("The gap is deeper:", "The surface is not only metal:"; "And" dropped); the CAPM sentence
  split at ", and the PDK's cross-section" (the "on our reading" hedge is inside the dash pair of the
  first half and stays there); "The oxide deposited here is therefore …" an indented continuation.
* R-CATEGORY: classification sentence to "(after NILD4)." (21 words); "which sets out" → "NILD3 sets
  out" (restored noun; the page's own Related bullet and 126 say NILD3 sets out the routes) with the two
  routes as bullets; the SkyWater sentence a paragraph; "What is specific to this instance is:" three
  bullets (only "and" dropped).
* R-PARA/R-SENTENCE (Why): insulation item split at the semicolon, the studies a continuation; the
  capacitor item's colon lead with the two studies as sub-bullets ("and" dropped) and "Here the top
  plate floats …" as a continuation, its trailing "(inference that …)" unchanged; capacitance item split
  at the semicolon ("they" → "The tables", restored noun); polishable-overburden item split at the
  semicolon, "on our reading" stays with the Oxide-Bias clause it was in.
* How: scope sentence as the italic lead-in; step 1 split at the semicolon (two separately cited facts);
  step 2 split at the semicolon, "Backside helium …" a continuation (126 form); step 4 split at the
  semicolon, "as-\ndeposited" joined; its "(industry practice; … not public)" stays on the second half,
  the first being covered by the italic scope sentence (as 140 step 2 in batch 10).
* R-TOOLS: HDP-CVD three-line item, model sentence as a continuation; PECVD TEOS two grades; C1 bullet
  unchanged (no "Strength:").
* R-RELATED: Previous · Next · Same module (the capacitor steps; every step 135–163 has the Phase cell
  "MiM capacitors, metal 3–5, via 3–4") · Depends on (NILD3, NILD4) · Same category (NILD6) · Category
  page.
* R-OPENQ: five labels from the bullets' own words.
* R-GLANCE: Does/Why from the lead and the "Without `NILD5` …" paragraph; numbers from the lead
  (`pdk-04`, `pdk-periph`); tool line = the R-TOOLS grades; Not public = Open question 1.
* `check_preserved --allow-regrouped`: ADDED only the glance box (markers `pdk-04`, `pdk-periph`,
  `skw-01`; numbers 0.300, 0.845, 4.1, 3, 4; quote "NILD5"; hedges inference, likely, not public;
  identifiers NILD5, metal-3) and the restored noun `NILD3` and the label "Metal-3 thickness";
  REGROUPED lines are the three splits above and the glance (same digits, same order).
  WORDS LOST: `and`, `strength`×2, `they`, `which`×2 (all named above). No DUPLICATED line.
* `cov`: 4 flags, all read — the "our arithmetic" and "on our reading" hedges stay on the clauses they
  qualify (see Lead and R-LIST above); two pairing noise.
* R-REPEAT: none (only the glance repeats body text).

## Content problems for the owner (not fixed; text kept verbatim)

* From the S9b figure notes: on the stop-on-dielectric reading of CAPME, the MiM dielectric stays on
  every metal-3 shape under the MM3 resist; 141's caption says so ("left on the metal-3 shapes on this
  drawing, as at MM3E"), the page text does not. The 145 page gives the via floor as the metal cap
  without saying so (see 145 below).
