# Progress — readability batch 9, steps 118–134 (`topic/rd-steps-118-134`)

Writer: Opus. Started 2026-09-26 from `main` at `b74bba1a`. Guide: `docs/plans/readability-guide.md`
§1, §2, §4.1, §5, §6, §7, §8, with the rulings of batches 4–8 (plain bullets over invented labels; no H3
where none of the four titles fits; R-CATEGORY's 35 words a target; the connective rule inside list
items; derivations under 120 words as a numbered list without an H3; a third lead paragraph only for
base leads over 120 words; "Because X, Y" is not a connective opener; rows differing in unit carry the
unit in each cell; R-REPEAT only when the other copy adds nothing, declared with the deleted text and
the survivor's location; no hand-inserted non-breaking spaces; "What is specific … is that X, and that
Y" over the cap → "… is that:" and one bullet per clause; one bullet per topic where a pronoun needs its
antecedent; a hyphen or slash at a source line break is joined). Medium classes avoided (batch 4–8
reviews): a pronoun whose referent changes after a split; a marker lost when dash material moves; a
sentence moved below the grade that refers to it; glance wording that strengthens a grade; a
whole-sentence trailing hedge not repeated on every half of a split. Model pages: 113, 110. One commit
per page.

## Method, every page

* Baseline build and one desktop tile set per page before any edit (`tmp/shots/*-before*`,
  git-ignored); one final pair (1280 px, `--max-height 40000`; 400 px, `--max-height 60000`) after.
* Preservation: `uv run python tools/check_preserved.py --base HEAD --allow-regrouped <page>` against
  the commit before the page, no other flag; never `--allow-added`, never `--allow-dropdown-edits`.
  Every ADDED line is named in the page entry; every REGROUPED and number_order line read;
  `--strict-words` as the final run, every LOST word named.
* Marker coverage: `tmp/readability/rdtools.py cov` (git-ignored scratch script) pairs every sentence
  not verbatim in the base — split at full stops **and semicolons** — with its closest base sentence and
  flags any marker or hedge word the base sentence had and the new one lacks. Every flag read.
* Invariants: `rdtools.py inv` against the base: References section, footnote definitions, generated
  index-links block, `{figure}` blocks, `{dropdown}` blocks, quick-facts rows, H2 list and Deep-dive
  count identical; one admonition (the glance box, `:class: at-a-glance`); no duplicate H3; every glance
  marker recurs below; the scope sentence is the italic lead-in.
* Caps: `rdtools.py caps` at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25) with
  `{figure}` blocks (captions), `{dropdown}` bodies, the generated block, `## References` and footnote
  definitions **excluded**; a leading bold run-in label is not counted into its sentence; a quotation
  counts as one word.
* Gates per page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`, `-W` build.

## Content problems for the owner (not fixed; text kept verbatim)

(filled in per page below and collected here at the end)

## Pages

### 118 VIM — done

* **Lead:** 112 words → two paragraphs at "The holes are etched at".
* **R-H3 + R-TABLE:** `### What the public record shows` over the post-figure passage (rules, CD
  table, extraction values, then the two differences from the contact level). The via.1a–via.5a,
  m2.4/m2.5 enumeration → `Rule | Constrains | Value`, unit in each cell (via.3 is `0.2\*L`;
  m2.4/m2.5 one row, "the same 0.055 µm and 0.085 µm" as in the base); `[^pdk-periph]` on the lead-in
  "The periphery rules give:". number_order LOST
  `('0.150','1','0.150','0.230','0.280','1','0.170','2','3','0.2','1','0.055','4','0.085','5','2','0.055','0.085','4','5')`
  hand-checked against the rows: via.1a 0.150 µm; via.1b 0.150, 0.230 and 0.280 µm; via.2 0.170 µm;
  via.3 0.2\*L; via.4a 0.055 µm; via.5a 0.085 µm; m2.4, m2.5 0.055 and 0.085 µm — same digits, same
  pairing. "enclosures by metal 1" → "enclosure by metal 1" in two cells (word "enclosures" lost).
* **R-LIST:** "in two ways …: First, … Second, …" → plain bullets. First: split at its colon ("… though
  it is narrower. The stack diagram gives …"). Second: the dash material (the two Cypress stacks)
  becomes its own continuation sentence "The stack is a 300 Å …[^cyp-qtp-113005][^cyp-qtp-123907]
  ({ref}`overview-metal-cap`)." ("The stack is" added by the split); the which-clause (etch stop and
  mirror) stays with "the top of the metal-1 stack" it describes. Wording of both stacks verbatim.
* **R-CATEGORY:** classification sentence kept whole (33 words); **Specific to this step:** with three
  bullets: the k₁ passage (split at its semicolon; the k₁ formula stays inline, single operation), the
  ITRS quotation, "We infer …" (split from the ITRS sentence at its semicolon) with "Nothing public
  states …" in the same bullet (ruling D2). "What distinguishes it from `CTM1` …" is its own label and
  stays a paragraph; its 50-word sentence split at the semicolon ("… reflective metal. Light that …").
* **R-PARA/R-SENTENCE (Why):** Hole size: lead ends at "top opening;" (the "on our reading" of the
  second clause stays with the slope and capability readings in the continuation). Placement: split at
  ", but a via" — "but" dropped (a continuation paragraph may not open on a connective). Uniformity:
  split at the semicolon. Resistance: the 13-word "(inference: …)" parenthetical closed as its own
  parenthetical sentence directly after the clause it qualifies ("(Inference: … from.)"); the Le et al.
  clause is the continuation.
* **How:** italic scope lead-in (the whole sentence, with its CTM1 pointer). Resist coat: lead ends at
  "if one is used". Exposure: "the era's toolkit was:" + three plain sub-bullets (PSM with OPC, FLEX,
  chemical shrink), each with its markers; the Chen/Wang/Chu dash material becomes its own sentence
  after the list, "its" → "the attenuated PSM's" (R-PARA step 5).
* **R-TOOLS:** three items; *SkyWater says:* only on the ASML item (a quotation of `[^skw-01]`); "The
  model is not public." stays after the grades. Grades unchanged.
* **R-OPENQ:** four labels from each bullet's own words. **R-RELATED:** Previous / Next split; Depends
  on (metal it lands on, oxide it opens), Feeds (the metal that covers it), Same category (the
  analogous hole masks), Mask (mask page, previous and next mask), Category page.
* **R-REPEAT:** `rdtools.py rep` finds no 10-word run in two H2 sections.
* **R-GLANCE:** Does/Why from the lead and Why; numbers via.1a, via.2 (`[^pdk-periph]`) and the
  via-1 height 0.27 µm (`[^pdk-04]`); tool line mirrors the grades; Not public from Open questions.
* **check_preserved (`--allow-regrouped --strict-words`):** ADDED markers `pdk-04`, `pdk-periph`,
  `skw-01`, numbers 0.150, 0.170, 0.27, `2`, ref `step-119`, hedges "inference", "likely", "not
  public", identifiers `NILD3`, `via-1` — all the glance box; ADDED numbers `1`×3 ("metal 1" in two
  table cells, "via 1" in the glance). LOST words "but" (above), "enclosures" (table cells), "its"
  (→ "the attenuated PSM's"), "page" ("Mask page:" → "Mask:"), "strength"×3 (R-TOOLS labels).
* **Coverage flags read:** table rows (marker on the lead-in); glance lines; the stack sentence took
  its Cypress markers; the Placement continuation (its enclosure marker stays with the enclosure
  clause); the Resistance and Resist-coat splits (each half keeps its own markers and hedges); the
  toolkit sub-bullets (own markers). None lost a marker or hedge.
* **Left over the caps:** none. Item lead over 30 words: Placement (37; one sentence).
