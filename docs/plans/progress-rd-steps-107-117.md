# Progress — readability batch 8, steps 107–117 (`topic/rd-steps-107-117`)

Writer: Opus. Started 2026-09-26 from `main` at `fb02bd1f`. Guide: `docs/plans/readability-guide.md`
§1, §2, §4.1, §5, §6, §7, §8, with the rulings of batches 4–7 (plain bullets over invented labels; no H3
where none of the four titles fits; R-CATEGORY's 35 words a target; the connective rule inside list
items; derivations under 120 words as a numbered list without an H3; a third lead paragraph only for
base leads over 120 words; "Because X, Y" is not a connective opener; rows differing in unit carry the
unit in each cell; R-REPEAT only when the other copy adds nothing, declared with the deleted text and
the survivor's location; no hand-inserted non-breaking spaces). Medium classes avoided (batch 4–7b
reviews): a pronoun whose referent changes after a split; a marker lost when dash material moves; a
sentence moved below the grade that refers to it; glance wording that strengthens a grade; a
whole-sentence trailing hedge not repeated on every half of a split. Model pages: 101, 097. One commit
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
  flags any marker or hedge word the base sentence had and the new one lacks. Every flag read; the page
  entry says what each class is.
* Invariants: `rdtools.py inv` against the base: References section, footnote definitions, generated
  index-links block, `{figure}` blocks, `{dropdown}` blocks, quick-facts table, H2 list and Deep-dive
  count identical; one admonition (the glance box, `:class: at-a-glance`); no duplicate H3; every glance
  marker recurs below; the scope sentence is the italic lead-in.
* Caps: `rdtools.py caps` at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25) with
  `{figure}` blocks (captions), `{dropdown}` bodies, the generated block and `## References`
  **excluded**; a leading bold run-in label is not counted into its sentence.
* Gates per page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`, `-W` build.

## Pages

### 107 CTM1 — done

* **R-H3:** `### What the public record shows` over the post-figure passage (rules, CD tables,
  extraction, stack diagram), which is public record ending in the hedged 0.34 µm depth.
* **R-TABLE:** the ct.1–ct.4, m1.4, m1.5 enumeration → `Rule | Constrains | Value`, unit in each cell
  (ct.3's value is `0.170\*L`); `[^pdk-periph]` on the lead-in. number_order LOST
  `('0.170','1','0.190','2','3','0.170','4','0.000','1','0.030','4','0.060','5')` hand-checked
  against the rows: ct.1 0.170 µm, ct.2 0.190 µm, ct.3 0.170\*L, ct.4 0.000 µm, m1.4 0.030 µm,
  m1.5 0.060 µm — same digits, same pairing.
* **R-LIST:** the four physical-criteria entries as bullets, `[^pdk-03]` on the lead-in "The
  physical-criteria table adds:"; the era's four exposure answers as sub-bullets under **Exposure**,
  each with its own markers.
* **R-CATEGORY:** classification split at the colon ("… for a projection printer.[^mack-2007] An
  isolated small square …[^mack-2007]"; marker repeated, declared); the remaining five sentences as
  plain bullets under **Specific to this step:**; "it" → `CTM1` in the first (R-PARA step 5).
* **R-PARA/R-SENTENCE:** lead in two paragraphs (split at the full stop before "The holes are
  etched"; the 59-word sentence split at its semicolon). The extraction sentence: the mid-sentence
  parenthetical hedge "(the PDK heads the column … we read the contact rows as per-contact resistance)"
  moved, unchanged, to directly after its sentence as "(The PDK heads … resistance.[^pdk-08])" —
  `[^pdk-08]` repeated because the parenthetical states what the PDK does (declared). The stack
  sentence split at its semicolon; the compound hedge divided per the batch-7b ruling D5: the first
  half (where the drawing places the two bottoms) takes "(our reading of a drawing marked "not to
  scale")" with `[^pdk-04]`, the second keeps the full "(our reading … and our arithmetic)". Resist
  coat: the 17-word PDK parenthetical became its own sentence; item split into lead and continuation.
  Exposure: the NA parenthetical became its own sentence; k₁ stays inline (single-operation estimate).
  Placement: split at the semicolon before "Levinson's book".
* **R-TOOLS:** three items; *SkyWater says:* only on the ASML item (a quotation of `[^skw-01]`);
  "The model is not public." stays after the grades as continuation. Grades unchanged.
* **R-OPENQ:** four labels from each bullet's own words. **R-RELATED:** Previous / Next split (the
  bullet named two relationships); Depends on / Feeds / Same category (all four masks are
  lithography steps) / Mask / Category page. **R-HEDGE:** italic scope lead-in.
* **R-REPEAT:** `rdtools.py rep` finds no 10-word run in two H2 sections.
* **R-GLANCE:** Does/Why from the lead and Why; numbers ct.1, ct.2 (`[^pdk-periph]`) and the bottom
  CD (`[^pdk-03]`); tool line mirrors the grades ("strong for existence", "inference" for the DUV
  assignment); Not public from Open questions.
* **check_preserved (`--allow-regrouped --strict-words`):** ADDED markers `mack-2007`, `pdk-04`,
  `pdk-08` (the three repeats above) and the glance markers; ADDED numbers `1`×3 ("metal 1" in two
  table cells, plus the glance), `2` and the glance numbers; ADDED quotes "not to scale" (hedge
  divided) and "Standard contact bottom CD" (glance); ADDED hedges "our reading" (divided hedge),
  "inference", "likely", "not public" (glance); ADDED identifiers `CTM1` (noun restored), `met1`,
  `metal-1` (glance). LOST words: "page" ("Mask page:" → "Mask:"), "strength"×3 (R-TOOLS labels),
  "and"×2, "it". Nothing else.
* **Coverage flags read:** table rows and list entries whose marker is on the lead-in (by design);
  each exposure sub-bullet carries only its own markers; R-TOOLS grades whose marker is on the head;
  the ITRS/critical-layers semicolon clause (its markers stay with their own clauses). No claim
  sentence lost a marker or hedge.
* **Left over the caps:** lead 122 words (base 122); "The PDK's "Standard contact bottom CD" …"
  (49 words): its only seam is the dash before "which eases", and "on our reading" scopes the
  which-clause, so the second half would lose the hedge; "The 0.1 µm `li`, the 0.075 µm LINT …"
  (46 words): the only seam is ", so", and both halves would need the full compound hedge with its
  quotation (R-SENTENCE step 5: "or do not split"). Resist-coat item lead block 39 words (the
  PDK-thickness parenthetical sentence stays next to the thickness it qualifies).
* Tiles: desktop 01–03 and phone 02–03 read; the rule table fits at 400 px (units wrap below the
  number in the Value column, the known batch-7b D4 case; no number breaks).
