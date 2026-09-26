# Progress — readability batch 12, steps 154–171 (`topic/rd-steps-154-171`)

Writer: Opus. Started 2026-09-27 from `main` at `773b9dbe`. Guide: `docs/plans/readability-guide.md`
§1, §2, §4.1, §5, §6, §7, §8, with the rulings of batches 4–11 (plain bullets over invented labels; no
H3 where none of the four titles fits; R-CATEGORY's 35 words a target; the connective rule inside list
items; derivations under 120 words as a numbered list without an H3; a third lead paragraph only for
base leads over 120 words; "Because X, Y" is not a connective opener; rows differing in unit carry the
unit in each cell; R-REPEAT only when the other copy adds nothing; no hand-inserted non-breaking
spaces; "What is specific … is (that) X, and (that) Y" over the cap → "… is (that):" and one bullet per
clause; one bullet per topic where a pronoun needs its antecedent; a hyphen or slash at a source line
break joined; a blank line after the glance box's closing `:::`; hedge scope at a semicolon split per
R-SENTENCE step 5; a lead within 120 words stays within 120, zero-word forms first; the gloss and
", though" forms of R-SENTENCE step 7; R-CATEGORY step 3 with elaborating sentences). Medium classes
avoided (batch 4–11 reviews): a pronoun whose referent changes after a split; a marker lost when dash
material moves; a sentence moved below the grade that refers to it; glance wording that strengthens a
grade; a whole-sentence trailing hedge not repeated on every half of a split; an added subject that
takes a lead over its cap. Model pages: 139, 140 (batch 10) and 141–149 (batch 11). One commit per
page. No edit of any kind inside an in-force `{dropdown}`.

## Method, every page

* Baseline build and one desktop tile set per page before any edit (`tmp/shots/*-before*`,
  git-ignored); one final pair (1280 px, `--max-height 40000`; 400 px, `--max-height 60000`) after.
* Preservation: `uv run python tools/check_preserved.py --base <commit before the page>
  --allow-regrouped <page>`, no other flag; never `--allow-added`, never `--allow-dropdown-edits`.
  Every ADDED line outside the glance box is named in the page entry; every REGROUPED and
  `number_order` LOST line read and re-paired by hand; `--strict-words` as the final run, every LOST
  word named.
* Marker coverage: `tmp/readability/rdtools.py cov` (git-ignored scratch script) pairs every
  sentence not verbatim in the base — split at full stops **and semicolons** — with its closest base
  sentence and flags any marker or hedge word the base sentence had and the new one (with its ±2
  neighbours) lacks. Every flag read.
* Invariants: `rdtools.py inv` against the base: References section, footnote definitions, generated
  index-links block, `{figure}` blocks, `{dropdown}` blocks, quick-facts rows, H2 list and Deep-dive
  count identical; one admonition (the glance box) followed by a blank line; no duplicate H3; every
  glance marker recurs below; the How scope sentence is the italic lead-in; no consecutive duplicate
  line, no prose line ending in a hyphen or slash, no bare `>`, no NBSP change.
* Caps: `rdtools.py caps` at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25) with
  `{figure}` blocks (captions), `{dropdown}` bodies, the generated block, `## References` and footnote
  definitions **excluded**; a leading bold run-in or italic R-TOOLS label is not counted into its
  sentence; a quotation and a code span count as one word; an em dash is not a word.
* Gates per page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`, `-W` build.

## Pages

### 154 MM4 — done (base `773b9dbe`)

* Lead (base 127 words, one paragraph): three paragraphs (36, 46, 45); the 46-word "As at MM3 …"
  sentence split at its colon (no word added). First sentence 5 words.
* R-H3 + R-TABLE: `### What the public record shows` after the figure caption over the PDK passage
  (≈ 245 words, public record ending in a hedged fuse reading, 139 form). The periphery-rule sentence
  became a `Rule | Constrains | Value` table (139/144 form), rows in base order; the `cmm4 waffleDrop`
  fill check has no rule id or value in the base, so both cells are `—`. `number_order` LOST line
  re-paired by hand: m4.1 0.300 µm · m4.2 0.300 µm · m4.5a, m4.5b 0.400 µm · m4.4a 0.240 µm² · m4.3
  0.065 µm · m4.pd.1 0.7, 700 µm windows, 70 µm steps · fill check — · via4.4 0.190 µm. The lead-in
  "The periphery rules give:[^pdk-periph]" carries the base sentence's only marker. Via4.4 cell
  reworded from "the via-4 openings that will land on metal 4 must be enclosed by it by" to
  "enclosure, by metal 4, of the via-4 openings that will land on it" (144's form; words lost
  `must`, `be`, `enclosed`).
* Fuse sentence (49 words) split at ", and give": "They give fuses …"; `[^pdk-periph]` repeated on
  the first half (declared marker), since the base's single marker covered both clauses.
* R-CATEGORY (139 form): classification sentence alone, then **Specific to this step:** with two
  bullets. The 49-word k₁ sentence split at ", and on an i-line"; "(our arithmetic)" repeated on the
  248 nm half (declared hedge). The SkyWater sentence split at its semicolon. The "What is specific …
  is the substrate, and it is …" sentence (70 words) split at the clause with its own subject; the
  two substrates as two bullets; the closing apposition "two thin-film stacks …" became "These are two
  thin-film stacks …" (declared subject, "These are").
* Why: overlay item split at ", so" ("So whether `MM4` aligns …"); its "(inference; …)" stays on the
  So-sentence, which is the clause the page's Open-questions bullet ("The alignment tree — to via 3, to
  `cap2m`, or both — … not public") ties it to; the first half is cited (`pdk-periph`) or a flow fact.
  Reflectivity item split at its semicolon; each half keeps its own hedge.
* How: scope sentence italic. Step 1 split at its semicolon and before "then an organic BARC" (the
  base's own "then", capitalised); "(inference)" stays with the HMDS clause it closes, the markers with
  the BARC clause. Step 5: the 18-word hedge parenthetical became its own parenthetical sentence
  directly after the sentence it qualified (R-SENTENCE step 7); the "whether … cap2m plate edges"
  sentence is an indented continuation paragraph.
* R-TOOLS (three items, 139 form); R-RELATED (Previous · Next · Depends on · Feeds · Same category ·
  Mask · Category page; "Mask page:" → "Mask:", word `page` lost); R-OPENQ labels on five bullets.
* Glance box (139 form).
* `check_preserved --allow-regrouped`: ADDED only in the glance box, plus the declared
  `pdk-periph` (fuse split), "(our arithmetic)", "These are", the H3, the table header and the
  Open-questions labels. `--strict-words` LOST: `enclosed`, `must`, `page`, `strength`×3. cov: no
  flag. inv: OK.
