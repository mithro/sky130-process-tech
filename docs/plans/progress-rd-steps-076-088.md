# Progress — readability batch 6, steps 076–088 (`topic/rd-steps-076-088`)

Writer: Opus. Started 2026-09-26 from `main` at `c00cfefa`. Guide: `docs/plans/readability-guide.md`
(§1, §2, §4.1, §5, §6, §7, §8), with the rulings merged from batches 4 and 5 (R-LIST plain bullets over
invented labels; no H3 where none of the four titles fits; R-CATEGORY's 35 words a target; the
connective rule inside list items; R-DERIVATION under 120 words without its own H3; a third lead
paragraph only for base leads over 120 words; "Because X, Y" is not a connective opener). Reviews read:
batch 4 and batch 5 (pronoun whose referent changed after a split; marker lost when dash material
moved; a sentence moved below the grade that refers to it; glance wording that does not say what it
grades) and masks-b H1 (a split at a semicolon leaving the first half without its marker). Model
pages: 066, 068, 072. One commit per page.

## Method, every page

* Baseline build and tiles (1280 px and 400 px, `--max-height 40000/60000`) of all 13 pages before any
  edit (`tmp/shots/*-before*`, git-ignored).
* Preservation: `uv run python tools/check_preserved.py <page> --allow-regrouped` (base `main`), no
  other flag; never `--allow-added`, never `--allow-dropdown-edits`. Every ADDED line is named in the
  page entry with the rule that adds it; every REGROUPED line is read; every `WORDS LOST` word is
  accounted for. `--strict-words` run as the final check on each page.
* Marker coverage: `tmp/readability/markcov.py` (git-ignored) pairs every new sentence that is not
  verbatim in the base with its closest base sentence and flags any marker or hedge word the base
  sentence had and the new one lacks. Every flag is read; the page entry says what each class is.
* Invariants: `tmp/readability/invariants.py` (git-ignored) against `main`: References section,
  footnote definitions, generated index-links block, `{figure}` blocks, quick-facts table, every
  `{dropdown}` block, H2 list and Deep-dive `* ` count must be identical; it also reports admonitions,
  glance markers that do not recur below the box, duplicate H3s and the italic scope lead-in.
* Caps: `tmp/readability/caps.py` (git-ignored), `measure.py`'s block parser and `measure5.py`'s
  sentence split at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25), with
  `{figure}` blocks, `{dropdown}` bodies, the generated block and `## References` excluded; it also
  prints the lead's word count and first-sentence length.
* Repeats: `tmp/readability/repeat.py` (git-ignored), 10-word runs shared by two H2 sections.
* Gates after each page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`,
  `gen_figures --check`, `-W` build; tiles at 1280 px and 400 px read against the baseline.

## Pages

### 076 SPNIT — done

* **Lead.** First sentence (37 w) split at its dash: "… over the whole wafer. It runs over the capped
  gate lines …" (subject + verb added, R-SENTENCE step 7). Lead split into two paragraphs before "The
  film is not a device layer" (where it goes / what it becomes). 103 words, first sentence 12.
* **R-H3 not applied.** The 232-word passage after the figure is PDK facts plus this reference's
  reading of the flow ("On this reading of the flow …"); `What the public record shows` is not true of
  the second half and no other title fits, so no H3 (batch-4 D2).
* **R-LIST.** "Two public facts bear on the step." → colon and two bullets, each opening with its own
  words bolded in place ("The PDK's process stack diagram", "The PDK's assumptions table"); the
  list-joining "And" dropped. The first item split at its semicolon ("This reference uses the same
  word …"; the marker stays on the SPNIT/7.5 claim). The second split at its dash: "… 0.05
  µm.[^pdk-03] So the finished SKY130 spacer is, we infer, …" ("So" opens a sentence, not a
  paragraph); `we infer` stays in the inference sentence. "The nitride thickness itself is not
  public." stays as the closing prose. "On this reading of the flow, the surface is oxide everywhere:"
  → three plain bullets (no invented labels); the hedge is on the lead-in before the colon, so it
  covers every item. The 17-word parenthetical in the cap item closed as its own sentence "(The PDK's
  figure … no thinner.)[^pdk-03]"; `[^pdk-03]` **repeated** after "poly cap after SPE"" so the 0.2 µm
  claim keeps it (declared). The "Whether … is not public" sentence stays as the paragraph after.
* **R-CATEGORY.** Classification sentence (20 w) alone. The next sentence begins "What is specific to
  this instance is that …", so it is its own label (step 3): a paragraph, no bullets. Its 90 words
  split at the colon and at ", and the film must" ("The film must coat …", joining "and" dropped). The
  last sentence ("The second distinguishing property …") is its own paragraph. The 46-word "The film
  must coat …" sentence is left: its only further split would move the 20-word parenthetical and
  reorder the 0.38/0.18/0.2/0.21 numbers.
* **Why.** Paragraph 1 (160 w) split before "Every CMOS process since" (history / the idea's use); the
  Ogura/Tsang sentence split at ", and Tsang et al." (each half keeps its own marker). "Etch
  selectivity" split at its semicolon. "Fringing field" (67 w): lead = the first clause (split at the
  semicolon), continuation paragraph from "Mizuno et al."; the PDK sentence split off at its dash
  ("The PDK's 7.5 value … need.", each half keeps its own markers). "The cost of nitride is hydrogen
  and stress." → colon and two bullets bolded in place ("CVD nitride carries hydrogen", "The film's
  stress"), the closing "These are the reasons a composite spacer …" kept as prose after the list
  (R-LIST step 4) so "These" still covers both; the hydrogen item (63 w) has a one-clause lead and a
  continuation paragraph from "Sambonsugi and Sugii" (joining "and" dropped).
* **R-HEDGE.** Scope sentence as the italic lead-in, word for word.
* **R-PARA step 4 (How items).** DCS: lead = the first sentence, split at its semicolon; continuation
  from "Roenigk and Jensen", the 56-word film sentence split at its semicolon ("Temple-Boyer et al.
  measured …"); "The drawback is thermal budget" as a second continuation. BTBAS: the first sentence (39 w with the label) split at ", which Gumpher": lead "… deposits nitride in a
  furnace at 550–600 °C.[^gumpher-2004]" (marker **repeated** so the temperature claim keeps it, declared),
  continuation "Gumpher et al. demonstrated it …" ("which" → "it", R-PARA step 5). Thickness: lead "Not public."; continuation 1 = the poly.1a sentence (split at its
  semicolon) and the `LD` reading; continuation 2 = ITRS, split at its dash: "… 2001 technology
  year.[^itrs-01] That is for an MPU of 65 nm physical gate length,[^itrs-01] not for SKY130's …"
  ("That is" added, step 7; `[^itrs-01]` **repeated** so the ITRS MPU fact keeps its marker after the
  dash material moved, declared). "(our reading of the roadmap …)" stays with the SKY130 application
  it governs.
* **R-TOOLS.** Aviza: *SkyWater says:* "states that "Furnaces are all made by Aviza" and lists …"
  (verb-first), *Tool exists:* **strong** …, *Runs this step:* the **inference** clause and "a DCS/NH₃
  LPCVD spacer … equally consistent" (both about the assignment); the dealer sentence, not
  SkyWater's, is the continuation paragraph. "C1": the head sentence ""PECVD nitride C1" is on the
  same list" is this reference's statement, not a quotation of SkyWater's wording, so it stays as the
  head (pilot form) with the two grades as sub-bullets. Two tools, no recap table.
* **R-RELATED.** Previous and Next as two bullets (the bullet named both). "The oxide component of the
  spacer" (SPOX) and "where the nitride is later cut for contacts" (NPCM, NPCME) → one `Same module:`
  bullet (all three carry this module's Phase cell); "The oxide the film is deposited on … the cap it
  covers" → `Depends on:`; "the implants the finished spacer masks" → `Feeds:`. "Other nitrides" keeps
  no label: `ONO` is a Thermal-oxidation step, so `Same category:` would be false. Every gloss and link
  kept.
* **R-OPENQ.** Labels from the bullets' own words: "Deposition route and thickness", "Spacer
  structure", "Pre-spacer oxide", "Oxide over the source/drain"; text unchanged.
* **R-GLANCE.** Does/Why from the lead; Public numbers: "SPNIT" 7.5 `[^pdk-04]`, "oxide spacer"
  0.05 µm `[^pdk-03]`; tool line with the page's two grades, each named; Not public from Open
  questions 1.
* **Skipped.** R-REPEAT (no 10-word repeat across H2s); R-DERIVATION (the 0.38 µm = 0.18 + 0.2 is one
  operation, inline, step 6); R-TABLE (no ≥ 3 × 2 parallel data).
* **Preservation** (`--allow-regrouped` only): ADDED markers `gumpher-2004` (repeat), `itrs-01` (repeat), `pdk-03`×2 (one
  repeat, one glance), `pdk-04` (glance), `skw-01` (glance); numbers 0.05, 7.5, quotes "SPNIT",
  "oxide spacer", ref `step-077`, hedges "inference", "likely", "not public" — the glance box.
  REGROUPED: Ogura/Tsang (1980 | 1982), the DCS film sentence (1 | 600), BTBAS (550–600 | 200, 4–30), Thickness (0.15, 1 | 0.06),
  ITRS (2001, 48–95, 2001 | 65, 0.15): same digits, same order, split at the seams above. WORDS LOST:
  "and"×2 (list-joining), "strength"×2 (R-TOOLS labels).
* **Marker coverage.** 16 flags, all read: split halves whose base marker belonged to the other
  clause (SPNIT/label, oxide spacer/inference, Ogura/Tsang, Mizuno/PDK, hydrogen lead/authors,
  poly.1a/`LD`, ITRS values/MPU, now repeated); the list lead-in carrying "On this reading"; the
  category sentence split (the markers belong to the 0.38 µm clause); two tokenizer mismatches.
* **Caps**: para > 100 5 → 0; item > 60 5 → 0; sentence > 45 11 → 1 (the 46-word "The film must
  coat …", above).

### 077 SPE — done

* **Lead.** The 59-word second sentence split at the closing dash of its dash pair: "… every
  horizontal surface — the tops of the gate caps, the source/drain silicon, the field oxide. It
  remains only where …" ("and remains" → "It remains", step 7). Lead split into two paragraphs
  before "Their width"; "Their" → "The spacers'" (R-PARA step 5, so the new paragraph does not open
  on a pronoun). 113 words as in the base, first sentence 5.
* **After the figure.** The 131-word paragraph split before "The etch must clear" (the PDK entry
  and its reading / what the constraint means for the etch); the 66-word sentence split at
  ", while over the gates" ("Over the gates it eats …"; "while" dropped). "(on our reading)" stays
  on the stop-on-oxide clause it governed. No H3: the passage is mostly this reference's reading.
* **R-CATEGORY.** Classification sentence (29 w) alone; the two remaining sentences both describe this
  step → `**Specific to this step:**` and two bullets, text unchanged.
* **Why.** "Spacer profile" (71 w) split at its semicolon: lead = the dash-pair sentence (the label is
  its subject, so it cannot be shortened), continuation from "Krieger et al."; "Residual damage"
  split at ", and Om et al." (each half keeps its marker).
* **R-HEDGE.** Italic lead-in, word for word.
* **How.** Main etch: lead = the gas sentence; continuation 1 = the mechanism sentence (split only
  at its second semicolon, after `[^flamm-1981][^winters-1992]`, so the SiF₄/N₂ clause keeps those
  markers — masks-b H1), Lee and Chen split from Kastenmeier at ", and"; the 17-word parenthetical
  closed as its own sentence "(Both in downstream, ion-free reactors: … used here.)" (R-SENTENCE
  step 7, capitalised and closed, nothing else changed); continuation 2 = "The bias is set …".
  Endpoint (55 w): the dash pair holding the TEL quotation moved after the sentence with the
  neutral lead-in "The patent adds:" (step 7); both pieces keep their own `[^pat-cn-tel]` as in
  the base. Over-etch (80 w): lead = the chemistry clause with its `[^regis-1997]`; continuation
  "It is long enough to remove nitride stringers … survives.[^regis-1997]" ("It is" added; the
  marker **repeated**, declared, because in the base that clause ran on through a colon into the
  Regis sentence and was covered by its marker).
* **R-TOOLS.** Four tool bullets → recap table `Tool | Evidence` above the list (grades in the page's
  words). Lam 9400: *SkyWater says:* "lists "…"" (verb-first), *Tool exists:*, *Runs this step:*.
  DPS II: its head sentence mixes SkyWater's quotation with this reference's gloss ("carries CF₄ and
  CHF₃ and could run a nitride etch-back") with no seam → pilot form, the grade as *Runs this step:*
  (the page grades only the step). Lam 4400: *Runs this step:* **weak** (as on 062). Wet clean:
  *Tool exists:*.
* **R-RELATED.** Previous/Next split into two bullets. "The extensions it protects" → `Same module:`
  (ASTI, HVASTI, LDASTI carry this module's Phase cell); "The oxide it stops on … the cap it thins"
  → `Depends on:`; "The implants the spacer masks" → `Feeds:`; "Other nitride etches … the gate
  etch whose profile the spacer follows" → `Same category:` (STINITE, ONOME, NPCME, P1ME are all
  Etch steps). Every gloss and link kept.
* **R-OPENQ.** Labels "Chemistry and spacer width", "What the etch stops on", "POC oxide cap",
  "Which etcher"; text unchanged except the stop-layer bullet (47 w with its label) split at its
  semicolon ("… is not public. Our reading is that an oxide survives …"; the hedge keeps its own
  sentence).
* **R-GLANCE.** Does/Why from the lead and Why; Public numbers: the 0.2 µm "poly cap after SPE" with
  its "(inference)" reading; tool line with both grades named; Not public from Open questions 1–2.
* **Skipped.** R-H3, R-TABLE, R-DERIVATION (nothing qualifies); R-REPEAT (no repeat).
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03` (glance), `regis-1997`
  (repeat), `skw-01` (glance); numbers 0.2 (glance), 4400, 9400×2 (recap table and glance); quotes
  "nitride", "poly cap after SPE" (glance); ref `step-076` (glance); hedges "inference"×3 (glance ×2,
  recap table), "likely", "not public" (glance). REGROUPED: the 387 nm sentence (387 | 387), the
  quotation moved after its sentence. WORDS LOST: "strength"×4 (R-TOOLS), "their" ("The spacers'"),
  "while" (split).
* **Marker coverage.** 13 flags, all read: glance lines; split halves whose base marker belonged to
  the other clause (Reinhardt/Om, Lee and Chen/Kastenmeier, the Kastenmeier caveat, the over-etch
  clause now carrying its repeated marker); the "(on our reading)" clause kept with the source/drain
  half; the Tool-exists/Runs-this-step split; OQ label lines.
* **Caps**: para > 100 2 → 0; item > 60 3 → 0; sentence > 45 7 → 0. Lead 113 words (base 113).
