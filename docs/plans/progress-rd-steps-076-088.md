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
* Gates before each page's commit: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links
  --check` and a `-W` build (built from a snapshot copy of `docs/`, so the next page could be edited
  meanwhile; pages 078/079, 081/082, 084/085 and 086/087 shared one build each); `gen_figures --check`
  (about eight minutes, and no figure was touched) five times during the batch and at the end; tiles at 1280 px
  and 400 px (`tmp/shots/*-after*`) read against the baseline.

## Batch measurement (§1 caps; figure captions and dropdown bodies excluded)

Counted with `tmp/readability/caps.py`: `{figure}` blocks (the captions), `{dropdown}` bodies, the
generated index-links block and `## References` are **excluded**. Before = `main` at `c00cfefa`.

| §1 cap | Before | After |
|---|---:|---:|
| paragraphs > 100 words | 36 | 0 |
| list items > 60 words | 45 | 1 |
| sentences > 45 words | 104 | 3 |
| table cells > 25 words | 0 | 0 |

`measure5.py` as committed (it counts `{figure}` captions): paragraphs 49 → 13 (the 13 remaining are the
13 figure captions), items 45 → 1, sentences 120 → 19 (16 of them in captions), cells 0 → 0.

**Left over the caps, with reasons** (each is also in its page entry):

* Item: 082 "It does not dope the PMOS gate" (63 w lead block; its only seam is before "So SKY130
  avoids …", which may not open a continuation paragraph).
* Sentences: 076 "The film must coat the foot of a gate line …" (46; the only further split would move a
  20-word parenthetical and reorder its numbers); 083 the tilted-extension lead (51, restored in the fix
  round); 086 the test-tile values with the full extraction hedge repeated (50, fix round); 087 the first
  Resources bullet (46, restored in the fix round); 087
  "The surface under the resist is, on our reading of the flow, …" (47; the same reason).
* First sentence over 25 words: 082 (27), 086 (26); no seam that step 7 allows.
* Leads over 120 words, as in the base: 079 (136; base 135), 080 (121; base 122), 083 (128; base 125),
  088 (157; base 154). Two paragraphs each, except 088, which takes three (§4.1 note ¹).
* Lead-sentence of an item over 30 words with a continuation paragraph: 077 "Spacer profile" (the bold
  label is the sentence's subject), 082 "It does not dope the PMOS gate" (above). No item has sub-bullets
  under a lead of more than 30 words.

**Gates (end of batch, in the worktree):** `check_steps`, `check_refs`, `check_machines`,
`check_materials`, `check_masks`, `check_papers`, `check_patents`, `check_filings`, `check_inforce` — 0
problems; `gen_papers`, `gen_patents`, `gen_filings`, `gen_index_links`, `gen_steps`, `gen_step_tables`,
`gen_figures` `--check` — 0 differences; `sphinx-build -E -W` into a fresh directory — exit 0 (and an
incremental `-W` rebuild after the last fix commit). `invariants.py` over the 13 pages: 0 changes to
References, footnote definitions, generated blocks (including the generated `{dropdown}` on 077 and 084),
figures, quick facts, H2 lists or Deep-dive counts; one admonition (the glance box, `:class:
at-a-glance`) per page; every glance marker recurs below; no duplicate H3; every scope sentence is the
italic lead-in. `check_preserved.py --allow-regrouped` over the batch: the only lines are the declared
ADDED lines, REGROUPED lines and three LOST `number_order` (the `npc`, `psd` and `nsd` rule tables on
078, 081, 085), each re-paired by hand in its page entry; no `{dropdown}` line and no WARN line on any
page; `--strict-words` loses only "strength" (the R-TOOLS labels) and the connective or pronoun words
named per page. None of these pages has a hand-written in-force note, so no dropdown was touched.

**Self-review for the reviewers' classes** (after the pages were done): a scan of every new sentence and
paragraph that opens on a pronoun or demonstrative found three whose referent had changed with a split —
076 "It runs over the capped gate lines" (now "The film runs"), 079 "It stops on the poly" after the new
cap sentence (now "`NPCME` stops"), 080 "It is a behaviour Lim et al. later modelled" after a sentence
whose subject is "Implanting through a thin oxide" (now "This is a behaviour") — and one continuation
paragraph opening on "It" (077's over-etch clause, moved back into the lead block). Paragraphs that open
on a pronoun or demonstrative and were kept: 076 "These are the reasons …" and the R-LIST closing
sentences (R-LIST step 4, like the guide's "Both are controlled …"), 083 "Such an implant would be
shadowed …" (the base's own opener; "such" names the implant of the paragraph before, not a cause).

## Guide problems

1. **Closing sentences after a list.** R-PARA step 2 forbids a paragraph opening on "This"; R-LIST step 4
   keeps the closing sentence as prose after the list, and the guide's own example opens "Both are …".
   076's "These are the reasons …" follows that example. The guide could say that a list's closing
   sentence may open on a pronoun that names the list's items.
2. **Units in a rule table whose rows differ in unit.** R-TABLE step 4 puts units in the header; 081 and
   085 have µm rows and µm² rows. Moving "µm²" to the header made `check_preserved` report `LOST numbers:
   '²'` (it tokenises the superscript as a number), so the two area cells keep their unit, joined by a
   non-breaking space as on 018. A guide line (or a tool change that treats a unit superscript as part of
   its unit) would settle it.
3. **The 30-word item lead.** §1 limits the lead sentence only when the item has sub-bullets; R-PARA step 4
   says 30 words for any item over 60 words. The batch followed step 4 where a seam existed; the guide
   could state which applies.
4. **Leading hedges at a split.** R-SENTENCE step 5 is written for trailing hedges and markers. 083's
   "On that reading, …" governed two clauses; the batch repeated it on the second sentence. Saying that
   step 5 applies to a leading hedge too would make this routine.
5. **Measurement artefact.** `measure5.py`'s splitter (and this batch's copy of it) reads a bold run-in
   label ending "**" as part of the next sentence, so "**Label.** Sentence" is counted as one sentence
   with the label's words; three flags in this batch were only that. (The same family as §8 item 12.)
6. **Gate cost.** `gen_figures --check` takes about eight minutes per run here and the `-W` build about
   the same; per-page runs of both dominate the batch's time. Where no figure is touched, running
   `gen_figures --check` at the end of the batch would lose nothing.
7. **R-TOOLS with no verb to drop.** On 079, 083, 086 the base gives SkyWater's list entry as a bare
   quotation after the tool name (no "SkyWater lists"). `*SkyWater says:*` is followed by the quotation
   alone rather than an added "lists"; the guide's verb-first rule does not cover this case.

## Content problems for the owner

None was fixed here; each is recorded as found.

1. **079 lead against step 5 (from the S6 figure notes).** The base lead: "… and stops on the poly, leaving
   bare polysilicon exactly "under licon1 areas"" (now "`NPCME` stops on the poly, …"); step 5: "A few
   nanometres of poly loss and a damaged layer of the kind Oehrlein reviewed are unavoidable". The
   figure agent judged this not a contradiction (the figure draws no loss and says so); both texts are
   kept verbatim.
2. **081 "Two proximity effects follow from a high-dose implant edge in resist."** The paragraph then
   describes one mechanism (lateral scatter from the resist edge, with its well-edge version and its
   layout consequences); the second effect is not named. The owner may want to name it or say "One".
3. **081 psd.10b against 085 nsd.10a.** 081 gives "minimum area 0.255 µm² (psd.10b)"; 085 gives "minimum
   area 0.265 µm² (nsd.10a)", with the same 0.265 µm² for the minimum hole area on both. The rules are
   shared under one heading; whether the rule ids (10a/10b) and the two area values are both right is
   worth one look at the periphery rules.
4. **083 repeats the 8250 list entry.** Why quotes "Axcelis 8250 Mid current B11, BF2, As, ESC chuck, E
   shower, 1e11 to 1e14, 0-60 deg tilt" and Machines likely used quotes "B11, BF2, As, ESC chuck, E
   shower, 1e11 to 1e14, 0-60 deg tilt". R-REPEAT was not applied (the copies differ and the Why
   argument rests on its copy); the owner may prefer a pointer.
5. **082/086 test-tile structures.** 082 describes "two 25.05-square "p+ resistor" structures", 086
   "the test tile's 25-square "n+ resistor" structures". If both are the same drawn geometry the two
   pages give it differently; kept as written.

## Pages

### 076 SPNIT — done

* **Lead.** First sentence (37 w) split at its dash: "… over the whole wafer. The film runs over the capped
  gate lines …" (subject + verb added, R-SENTENCE step 7; the subject is "The film", not "It", so it cannot
  be read as the step). Lead split into two paragraphs before "The
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
* **Caps**: para > 100 6 → 0; item > 60 5 → 0; sentence > 45 11 → 1 (the 46-word "The film must
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
  the base. Over-etch (80 w): lead block = the chemistry clause with its `[^regis-1997]` and
  "It is long enough to remove nitride stringers … survives.[^regis-1997]" ("It is" added; the
  marker **repeated**, declared, because in the base that clause ran on through a colon into the
  Regis sentence and was covered by its marker; kept in the lead block so that no continuation
  paragraph opens on "It"); continuation from "Regis et al. report".
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

### 078 NPCM — done

* **Lead.** First sentence (31 w) split at its colon: "… for the *nitride poly cut*. It is the
  resist pattern that tells NPCME …" ("It is" added, step 7; "(on our reading)" stays in its
  clause). Lead in two paragraphs, split before "The wafer arriving from SPE" (what the mask is /
  why the cap must be opened). 100 words, first sentence 10.
* **R-H3.** `### What the public record shows` after the figure caption, over the 185-word PDK
  paragraph (mask table, layers, periphery and contact rules, rpm.5, minimum CD): all public record.
* **R-TABLE.** The five `npc` rules ("minimum width 0.270 µm (npc.1), …") → `Rule | Constrains |
  Value (µm)`, one row per rule in the base order; "a manual-merge instruction below minimum" has no
  value, so its cell is `—`; `[^pdk-periph]`, which ended the enumerating sentence, sits on the
  lead-in "… — and give:[^pdk-periph]" (R-TABLE step 3; the form of 068). The "Constrains" cells are
  the base clauses without their values ("spacing with no overlap to a gate", "a maximum enclosure of
  poly overlapping a slotted `licon` by `npcm`"; the joining "of" before each value dropped). The lead-in
  sentence is the caption (R-CAPTION on step pages). Units in the header. LOST `number_order`
  ('0.270', '1', '0.270', '2', '3', '0.090', '4', '0.095', '5') re-paired by hand: npc.1 0.270, npc.2
  0.270, npc.3 —, npc.4 0.090, npc.5 0.095 — the base pairs.
* **R-LIST.** The four contact rules carry quotations and verbs, so a table would have to reword
  them: plain bullets instead, every word kept, `[^pdk-periph]` on the lead-in "The contact rules
  complete the picture:" (R-LIST step 1). rpm.5 and the minimum-CD sentence stay as the closing
  paragraph.
* **R-CATEGORY.** Classification sentence (≈ 30 w) alone; one sentence remains → a plain second
  paragraph (step 2), split at ", so the layer's overlay" into "So the layer's overlay … is its
  critical parameter, not its CD." (a sentence, not a paragraph, may open "So").
* **Why items.** "Poly contacts" (129 w): lead = the `licon1` sentence; continuation 1 = the
  nitride/Cacciato and "Opening the nitride first" sentences; continuation 2 = Tang et al., split at
  the semicolon after its markers ("Their abstracts do not describe …"). "Doping the poly under the
  cut" (137 w, a 91-word sentence): lead "`NPCM` comes *before* the source/drain implants.";
  continuation 1 = "Poly exposed by the cut is therefore implanted … The rules make sense on that
  reading." (the colon of the base sentence became a full stop); continuation 2 = "A precision
  resistor must be enclosed … p-type body." and, split at the dash, "The PDK's rule licon.9 checks …
  is not.", followed unchanged by "This is an inference from the rule text; no public source states
  it." — kept in the same paragraph as both sentences of the reading, so the hedge still covers both.
* **R-HEDGE.** Italic lead-in, word for word.
* **How items.** "Resist and BARC" (62 w): split at its semicolon; continuation "The PDK's nominal
  … we infer, …" with the hedge. "Exposure" (112 w): lead = the k₁ sentence to "limit.[^wiki-litho]"
  (split at its semicolon); continuation 1 = "A 248 nm tool gives k₁ ≈ 0.65 …" and the ITRS sentence;
  continuation 2 = "We therefore infer a **DUV** exposure … SkyWater lists both.[^skw-01]".
  R-DERIVATION not applied to "k₁ = 0.27 × 0.6 / 0.365 ≈ 0.44": one formula inside a recipe step,
  left inline as on 064 (batch-5 precedent).
* **R-TOOLS.** ASML: *SkyWater says:* "lists … beside its i-line tools" (verb-first), *Tool exists:*,
  *Runs this step:* the DUV inference. Tracks and overlay/CD in 068's form (bold head ending in the
  marker, grades as sub-bullets). Three tools, no recap table.
* **R-RELATED.** Previous and Next as two bullets (the bullet named both); "The cap being opened … the
  spacer beside the opening" → `Depends on:`; "What the opening is for … what is implanted through
  it" → `Feeds:`; "Resistors whose heads it defines" keeps no label (those are earlier steps the cut
  serves, neither Depends on nor Feeds exactly). "Mask page:" and "Previous mask: …; next mask: …"
  → one `Mask:` bullet (the mask page first, then the two neighbouring masks with their own words).
  Every gloss and link kept.
* **R-OPENQ.** Labels "Exposure tool and resist", "Reticle generated from `npc`", "Resistor heads",
  "Nitride over diffusion"; text unchanged.
* **R-GLANCE.** Does/Why from the lead, keeping "on our reading"; Public numbers npc.1/npc.2 0.270 µm
  and npc.4 0.090 µm `[^pdk-periph]`; tool line with both grades; Not public from Open questions 1
  (with its "inferred … not stated").
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-periph`, `skw-01`, numbers 0.090,
  0.270, 1, 2, 4, refs `step-058`, `step-079`, hedges "inference", "likely", "not public", "our
  reading" — the glance box. REGROUPED: the contact rules (0.100, 15, 18, 0.090, 13, 0.110, 9 — the
  base order, now one bullet each), the rpm/licon.9 sentence, the resist sentence, the exposure
  sentence (same digits, same order). LOST `number_order` for the `npc` table, checked above. WORDS
  LOST: "m" (µm moved to the header), "of" (table), "page" ("Mask page:" → "Mask:"),
  "strength"×3.
* **Marker coverage.** 15 flags, all read: the contact-rule bullets (their marker is on the lead-in
  before the colon, R-LIST step 1); "So the layer's overlay …" (the base marker sat after "(npc.4)",
  unchanged); split halves whose base marker belonged to the other clause (Tang/abstracts, resist/PDK
  thickness, k₁/248 nm); glance and label lines.
* **Caps**: para > 100 1 → 0; item > 60 4 → 0; sentence > 45 6 → 0. Lead 100 words (base 98).

### 079 NPCME — done

* **Lead.** The 59-word second sentence split at its dash pair without reordering: "… it removes the
  dielectric cap standing on the poly. The cap is whatever remains of the POC oxide and the GATENIT
  nitride, about 0.2 µm of it … "poly cap after SPE".[^pdk-03] `NPCME` stops on the poly, leaving bare
  polysilicon exactly "under licon1 areas".[^pdk-06]" ("The cap is" and "`NPCME`" added, step 7 — the step named, because an "It" after the cap sentence
  would read as the cap; each
  piece keeps its own marker and "on our reading" stays with the 0.2 µm). Two paragraphs, split
  before "Inside a window". 136 words (base 135, over 120 already), first sentence 6.
* **R-LIST.** "The structures being opened are of two kinds." → colon and two plain bullets ("The
  first are …", "The second are …", R-LIST step 3: always plain for first/second items), each with
  its own marker.
* **R-CATEGORY.** Classification sentence (18 w) alone; "Its nearest relatives …" (a sentence that
  only lists other steps, step 2) as its own paragraph with its noun back ("`NPCME`'s nearest
  relatives", R-PARA step 5, so the paragraph does not open on a pronoun); "What is specific here is
  the stop: …" is its own label (step 3), split at ", and the selectivity" ("The selectivity that
  makes …").
* **Why.** Paragraph 1 (134 w) split before "Tang et al. built"; the `licon1` sentence split at its
  semicolon ("If the nitride cap were still under it, …"); Tang split at the semicolon after its
  markers. The 51-word "The order relative to the source/drain implants is deliberate on our reading
  (…): the opened poly is doped …" split at its colon with the leading hedge repeated: "… (inference from
  the PDK rules, NPCM). On that reading, the opened poly is doped …" (review L8, the 083 form). "Two failure modes make the recipe demanding." →
  colon and two bullets bolded in place ("Incomplete clearing", "Over-etching" were already bold
  run-ins in the base); the npc.4 inference and the two studies stay as the paragraph after the list
  (R-LIST step 4), the studies split at ", and Tuda" (each keeps its marker).
* **R-HEDGE.** Italic lead-in, word for word.
* **How items.** "Nitride main etch" (106 w): lead = the chemistry sentence to Kastenmeier's markers
  (split at the semicolon); continuation = Staffa and the endpoint sentence, split after the TEL
  quotation (the quotation keeps its place and marker): "Because the open area is small, …"
  ("and, because" → "Because"; "Because X, Y" is not a connective opener). "Stop on poly" (173 w; a 64-word first sentence with two dash pairs):
  split after the Lee and Chen dash material ("… the CF₄/O₂ silicon etch.[^lee-chen-1983] So the last
  part of the etch uses …"; a sentence, not a paragraph, may open "So"), so the claim and its marker stay
  in one sentence; the second dash pair became its own sentence at the head of continuation 1: "The
  chemistry is a fluorine-lean, polymerising fluorocarbon step in an RIE tool (industry practice,
  category page[^txt-01])." ("The chemistry is" added, step 7). Continuation 1 continues with Kastenmeier, Matsuo and
  Oehrlein, split at ", giving": "This gives nitride-to-poly etch-rate ratios …" ("This gives" added,
  step 7) with `[^kastenmeier-1999]` **repeated** on the first half, since the base's single marker
  covered the whole sentence (R-SENTENCE step 5, declared). Continuation 2 = "A few nanometres of
  poly loss … we infer …". "Strip and clean": split at its semicolon ("We infer no HF, …").
* **R-TOOLS.** Four tools → recap table `Tool | Evidence` (062's rows for the same four tools).
  Lam 9400: *SkyWater says:* the quotation (the base sentence has no subject or verb to drop),
  *Tool exists:*, *Runs this step:*. DPS II: pilot-form head (quotation plus this reference's gloss
  "being the gate etcher, has the poly-stop chemistries in hand", no seam), *Runs this step:*
  **medium**. Lam 4400: *Runs this step:* **weak** (062's form). Ashers and wet benches: *Tool
  exists:*.
* **R-RELATED.** Previous and Next split; "The stack being cut … the spacer beside it" → `Depends
  on:`; "the resistors whose heads are opened" (PRI, UPRI) as its own unlabelled bullet, as on 078 (the
  cut does not depend on the resistor implants; review L1); "The implants that dope the opened
  poly" and "The contacts that land in the opening" → one `Feeds:` bullet; "Other nitride etches" →
  `Same category:` (STINITE, ONOME, SPE are Etch steps). Every gloss and link kept.
* **R-OPENQ.** Labels "Chemistry and adjacent spacer", "POC oxide", "The opened poly", "Which
  etcher"; text unchanged.
* **R-GLANCE.** Does/Why from the lead and Why; Public numbers npc.4's 0.090 µm `[^pdk-periph]` and
  "about 0.2 µm … on our reading" of "poly cap after SPE" `[^pdk-03]`; tool line with both grades;
  Not public from Open questions 1 in its own words ("is allowed to remove").
* **Preservation** (`--allow-regrouped` only): ADDED markers `kastenmeier-1999` (repeat), `pdk-03`,
  `pdk-periph`, `skw-01` (glance); numbers 0.090, 0.2, 4 (glance), 4400, 9400×2 (recap table and
  glance); quotes "nitride", "poly cap after SPE" (glance); ref `step-078` (glance); hedges "about",
  "inference"×2, "likely", "not public", "our reading" (glance and recap table); `number_order`
  (4, 0.090, 0.2) — the glance. REGROUPED: Kastenmeier (10 | 40, 100, 70), same digits, same order.
  WORDS LOST: "giving" ("This gives"), "its" ("`NPCME`'s"), "strength"×4.
* **Marker coverage.** 19 flags, all read: split halves whose base marker belonged to the other
  clause (cap/stop/licon1, `licon1`/0.17 µm hole, Tang/abstracts, Joubert/Tuda, Kastenmeier/Staffa,
  TEL quotation/"Because …", asher/wet bench/"We infer no HF"); glance and label lines.
* **Caps**: para > 100 4 → 0; item > 60 2 → 0; sentence > 45 10 → 0 (the
  51-word "order … on our reading" sentence, above).

### 080 SPOX — done

* **Lead.** The 46-word second sentence split at ", and we infer": "… (variable `SpThickn`).[^pdk-03]
  We infer that this film is that oxide, so that …" (the hedge stays with the inference, the marker
  with the PDK entry). Two paragraphs, split before "What the PDK does not say". 121 words (base
  122), first sentence 21.
* **R-LIST.** "The surfaces the oxide lands on are, at this point:" → five plain bullets (bare noun
  phrases, no labels invented), "(inferred, SPE)" kept on its own item; the "A conformal 0.05 µm oxide
  …" sentence stays as the paragraph after (R-LIST step 4).
* **R-CATEGORY.** Classification sentence (22 w) alone; "What is specific to it is that …" is its own
  label (step 3): a paragraph, split at the colon ("Its thickness enters …") and at ", and its thermal
  budget" ("Its thermal budget must be low …").
* **Why items.** "Spacer width without a second etch" (102 w): the dash pair "the PDK's high-current
  implant angle is 0°[^pdk-03]" became its own sentence after the claim ("The PDK's high-current
  implant angle is 0°.[^pdk-03]", step 1; the marker travels with it); continuation from "It is a
  cheap way", with "It" → "The conformal oxide" (R-PARA step 5, so the continuation does not open on
  a pronoun under the label), and the Janapaty half split off at the semicolon. "Implant screen"
  (85 w): the appositive "a behaviour Lim et al. later modelled" became "This is a behaviour Lim et al.
  later modelled for (100) silicon.[^lim-1993]" ("This is" added, step 7; "It" would have read as
  "Implanting through a thin oxide", the subject of the sentence before) in the lead block;
  continuation from "For BF₂, Wang et al.". "Protecting the opened poly" split at ", and the poly heads"
  ("The poly heads receive …"). "A cap for the anneal": the three studies split at ", and" and
  ", while" into three sentences, each with its own marker (joining "and" and "while" dropped).
* **R-HEDGE.** Italic lead-in, word for word.
* **How.** "LPCVD TEOS oxide" (80 w): lead = the furnace clause, split at its semicolon; continuation
  from "Becker et al.".
* **R-TOOLS.** "C2"/Producer: *SkyWater says:* "lists "PECVD TEOS, C2 and Producer"" (verb-first),
  *Tool exists:* strong, *Runs this step:* weak; the inventory's reading of "C2" (this reference's,
  "(inference)") is its own clause, so it moves to the continuation after the grades (R-TOOLS step 2).
  "C1": *SkyWater says:* the quotation (no subject in the base), *Tool exists:*. Aviza: the head
  sentence ""LPCVD silane oxide" is among the furnace processes" is this reference's wording around
  SkyWater's words → pilot-form head, *Tool exists:*. The "Which of the three …" bullet is not a
  tool and keeps its form. Three tools, no recap table.
* **R-RELATED.** Previous/Next split. "The nitride component of the spacer" (SPNIT, SPE) →
  `Same module:`; "the oxide under the nitride" (IOX45, gate module) split off and left unlabelled
  (the bullet named two relationships). "The implants that pass through this oxide … the anneal it
  caps" → `Feeds:`; "Other CVD oxides" → `Same category:` (POC, PSG, NCAPOX are Thin-film deposition
  steps).
* **R-OPENQ.** Labels "Etch-back and deposition method", "Removal before PSG", "Oxide thickness at
  implant"; text unchanged.
* **R-GLANCE.** Does from the lead; Why from the Why lead ("serves several purposes at once",
  "the public evidence does not say which SKY130 had in mind"), naming two of the purposes (review L6); Public numbers the
  0.05 µm "oxide spacer" `[^pdk-03]` with "which we infer is this film"; tool line "C2"/Producer with
  both grades; Not public from Open questions 1 ("all inferred").
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03`, `skw-01`, number 0.05, quotes
  "C2", "oxide spacer", identifiers "C2", "SKY130", hedges "likely", "not public", "we infer" — the
  glance box. REGROUPED: the LPCVD TEOS item (650–750 | 400–450). WORDS LOST: "and"×2, "while"
  (joining words at splits), "strength"×3.
* **Marker coverage.** 17 flags, all read: split halves whose base marker belonged to the other
  clause (PDK entry/inference, the moved 0° sentence, Park/Lim, the three dose-loss studies, the
  inventory reading); the list lead-in; glance and label lines.
* **Caps**: para > 100 1 → 0; item > 60 3 → 0; sentence > 45 7 → 0.

### 081 PSDM — done

* **Lead.** The 50-word second sentence split at ", leaving": "… and develops it. It leaves resist
  windows over every region … (on our reading)." ("It leaves", step 7). A first draft split at the
  dash pair instead ("The wafer is now carrying spacers, …") and was reverted: it moved the SPOX clause
  out of the sentence whose trailing "(on our reading)" may cover it. One paragraph, 81 words; first
  sentence 7.
* **R-H3.** `### What the public record shows` after the figure caption, over the 173-word PDK
  paragraph (mask table, layers and their add/drop purposes, the psd rules, minimum CD).
* **R-SENTENCE.** The 61-word layer sentence split at its semicolon (`[^pdk-05]` on the mask table,
  the rest keeps `[^pdk-06]`) and at its dash: "… purposes.[^pdk-06] That is evidence that the reticle
  is derived … not copied from it.[^pdk-06]" ("That is" added, step 7; `[^pdk-06]` **repeated** on the
  first half because the base's single marker covered the whole sentence — masks-b H1 — declared).
* **R-TABLE.** The ten psd rules → `Rule | Constrains | Value (µm)`, one row per rule in the base order,
  `[^pdk-periph]` on the lead-in "… give:[^pdk-periph]". The two area rows keep their own unit, "0.255 µm²"
  and "0.265 µm²", joined by a non-breaking space (as on 018) so the unit does not wrap away from the
  number at 1280 px or 400 px — a first try with the unit in the header lost a `²` token in
  `check_preserved` and was not kept; psd.6's "zero enclosure at a diff/tap butting edge" → "enclosure at a
  diff/tap butting edge | zero"; psd.8 and psd.9 have no value (`—`), psd.9's quotation is in its cell
  unchanged. LOST `number_order` checked by hand against the base: psd.1 0.380, psd.2 0.380, psd.5a
  0.125, psd.5b 0.125, psd.6 zero, psd.7 0.130, psd.8 —, psd.9 —, psd.10b 0.255 µm², psd.11 0.265 µm².
  WORDS LOST "by"×2 ("enclosure of diffusion by 0.125 µm" → the cell without its value).
* **R-CATEGORY / R-LIST.** The classification sentence ends "but with two differences." → colon and
  two plain bullets, the second opening "It is printed …" (joining "and" dropped; "it" is the resist,
  the subject of the first bullet).
* **Why.** The 68-word proximity sentence: the "which is why …" clause moved up to follow the claim it
  explains, and the three studies follow as their own sentence: "Ions scattered laterally … shift the
  threshold of transistors placed near it,[^hook-2003] which is why the layer carries … rather than
  zero. Hook et al. measured …,[^hook-2003] Sheu et al. …,[^sheu-2006] and Drennan … layout.[^drennan-2006]"
  `[^hook-2003]` **repeated** on the claim, which in the base carried the studies' markers in its dash
  material (batch-4 M2, declared).
* **R-HEDGE.** Italic lead-in, word for word.
* **How items.** "Resist coat" (111 w): lead = the 1 µm / PDK 1.14 µm sentence (kept whole, so the
  1 µm claim keeps its PDK support in the same sentence); continuation = "The thickness is set …
  10¹⁵ cm⁻² beam." and the Smith/Romig sentence (split at the colon). "Exposure" split at its
  semicolon. "Develop" split at its dash ("… reduce outgassing. Lee et al. measured …").
* **R-TOOLS.** i-line: *SkyWater says:* "lists both.[^skw-01]" (verb-first, the guide's own example),
  *Tool exists:*, *Runs this step:*. Tracks, overlay/CD in 068's form. Three tools, no recap table.
* **R-RELATED.** Previous/Next split; "Complementary mask: NSDM" → `Same module: the complementary
  mask, NSDM`; "Structures it dopes …" unlabelled; "Mask page:" and "Previous mask: …; next mask: …" →
  one `Mask:` bullet.
* **R-OPENQ.** Labels "Resist and exposure tool", "How `cpsdm` is generated", "Intermediate step";
  text unchanged.
* **R-GLANCE.** Does from the lead with its "(on our reading)"; Why from the Why lead; Public numbers
  psd.1/psd.2 0.380 µm and psd.5a/psd.5b 0.125 µm `[^pdk-periph]`; tool line with both grades; Not
  public from Open questions 1.
* **Preservation** (`--allow-regrouped` only): ADDED markers `hook-2003`, `pdk-06` (repeats),
  `pdk-periph`, `skw-01` (glance); numbers 0.125, 0.380, 1, 2, 5×2, ⁺ (glance); refs `step-082`,
  `step-083` (glance); hedges "inference", "likely", "not public", "our reading" (glance). LOST
  `number_order` for the psd table, checked above. WORDS LOST: "by"×2, "m"×2 (table: "µm" moved to the header), "leaving" ("It
  leaves"), "page" ("Mask page:" → "Mask:"), "strength"×3.
* **Marker coverage.** 11 flags, all read: the table's lead-in; split halves whose base marker
  belonged to the other clause (mask table/layers, the category bullets, Develop/studies); the
  proximity claim now carrying `[^hook-2003]`; glance and label lines.
* **Caps**: para > 100 1 → 0; item > 60 1 → 0; sentence > 45 8 → 0.

### 082 PSDI — done

* **Lead.** The 61-word second sentence split at its colon ("… or a spacer. The implant is
  *self-aligned* …"; "(on our reading)" stays on the SPOX clause it governs). Two paragraphs, split
  before "A second p-type implant". 111 words as in the base. **First sentence 27 words, left**: its
  only seam (", together with all the other P⁺ diffusions") would need a new verb and object, more
  than step 7 allows.
* **R-H3.** `### What the public record shows` after the figure caption, over the 241-word PDK and
  test-tile paragraph and the P⁻ paragraph after it.
* **R-PARA (evidence sequence).** The 241-word paragraph → an opening sentence and three labelled
  paragraphs, every sentence in its base order: **Junction depth and angle.** (the junction-depth
  sentence split at ", limits" → "It limits …", `[^pdk-03]` **repeated** on the first half because the
  base's single marker covered all three clauses — masks-b H1, declared), **Sheet resistance.** (the
  extraction and e-test values), **Measured on the test tile.** (the raw-data sentence split at its
  semicolon; both markers `[^raw-data-passives][^raw-data-testtile-pads]` **repeated** on the first
  half, which states what the repository and the pad list publish; the "(our extraction …)" hedge
  stays on the measured values it governs, declared). "The species, energy and dose are not public …"
  closes the passage as its own paragraph. R-TABLE was considered for the sheet-resistance values and
  not used: pairing 205.5 Ω/sq with the "hv p+ res" structure is an inference the page draws only
  through "lower for the high-voltage structure", and a row would state it outright.
* **R-CATEGORY.** Classification sentence (≈ 40 w; no semicolon or closing dash to split at, so kept
  whole, batch-4 D3) alone; the partner sentence and the "It differs …" sentence as a second paragraph,
  "Its partner" → "`PSDI`'s partner" (R-PARA step 5).
* **R-LIST.** "The deep source/drain does three things the extension cannot." → colon and three plain
  bullets (each begins "It provides"/"It is", capitalised; joining "and" dropped); the closing sentence
  stays as prose after the list with "Placing it" → "Placing the deep source/drain" (the pronoun's noun
  back after the list). "Beyond the PMOS, the same implant makes …" → colon and four bullets; the taps
  and the PNP/NPN stay in one bullet because the base's first `[^pdk-07]` came after both; the
  NPCM hedge "on the reading of the NPCM page" opens its own bullet, in front of the claim it
  governs (the dashes became a comma). "Two things the implant does *not* do, on the reading used
  throughout this reference, are worth stating." → colon and two bullets (the hedge on the lead-in
  covers both). The first bullet's 82-word sentence split at "— so SKY130" ("So SKY130 avoids …", a
  sentence) and at the semicolon (continuation "The work-function dependence …"); its lead block (the
  gate sentence plus the "So" sentence, 63 w) is **over the 60-word item cap, listed**: its only
  internal seam is before "So", which may not open a continuation paragraph (R-PARA step 2).
* **R-HEDGE.** Italic lead-in, word for word.
* **How items.** Species (131 w): lead = the first sentence; continuation 1 = BF₂⁺, the 57-word
  sentence split at its semicolon ("The fluorine it brings …"; `[^wang-1997]` is attached to "as Wang
  et al. showed", which governs only the fluorine clause); continuation 2 = Bourdelle, Öztürk,
  Adachi, SkyWater's species, "not public". Energy and dose (72 w): lead = the industry-typical
  sentence, split at its semicolon; continuation from "The PDK's 0.1 µm junction depth". Tilt (72 w,
  a 66-word sentence): lead "0°, per the PDK's …"; continuation split at ", and it needs" ("It needs
  …") and at the semicolon ("On a batch spinning-disc implanter …"). Wafer handling (106 w): lead =
  the cooling sentence; continuation = the flood-gun sentence as a lead-in with the three studies as
  plain nested bullets (a list of studies; each keeps its marker; joining "and" dropped), then the
  gate-oxide sentence. Monitoring split at its semicolon ("We infer that …").
* **R-TOOLS.** GSD: *SkyWater says:* "lists "…" and, separately, "…"" (verb-first), *Tool exists:*
  **strong** …, *Runs this step:* the **inference** with its parenthetical and the 8250 quotation (the
  reason for the grade); the Axcelis press-release sentence (not SkyWater's) is the continuation.
  One tool, no recap table.
* **R-RELATED.** Previous/Next split; "Complementary implant: NSDI; activation: RTAD, RTAD2" → `Same
  module:` (NSDI) and `Feeds:` (activation, RTAD and RTAD2); "The offset it is aligned to … the screen
  … the poly it dopes through the cut" → one `Depends on:` bullet; "The PMOS channel it completes … the
  gate it does not dope" keeps no label.
* **R-OPENQ.** The 111-word "PMOS extension" bullet (label already present): lead = the cross-section
  and mask-list sentence with its markers plus "The extension may be formed:"; the three possibilities
  as sub-bullets, each keeping its "by" and the last its "or"; the HVPTM sentence and the question
  ("Which of these applies is an open question on this page.") as the continuation, in the base order
  (R-OPENQ step 2, batch-5 D6). Labels added to the other two: "Shielding of the PMOS gate",
  "Which implanter".
* **R-GLANCE.** Does/Why from the lead and Why; Public numbers the PDK's S/D XJ 0.1 µm and "High
  current" 0° `[^pdk-03]` and `RSP` 197 Ω/sq with its limits `[^pdk-07]`; tool line with both grades;
  Not public from Open questions 1–2.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03`, `raw-data-passives`,
  `raw-data-testtile-pads` (repeats), `pdk-07`, `skw-01` and a second `pdk-03` (glance); numbers 0,
  0.1, 166–228, 197, ⁺, quotes "High current", "N+ or P+ S/D (XJ)", ref `step-083`, hedges
  "inference", "likely", "not public" (glance); `number_order` (0.1, 0, 197, 166–228) — the glance.
  REGROUPED: the test-tile sentence (25.05 | 211.7, 205.5), the "Beyond the PMOS" list and the
  "Two things" list (same digits, same order). WORDS LOST: "it" ("Placing the deep source/drain"),
  "its" ("`PSDI`'s partner"), "strength".
* **Marker coverage.** 29 flags, all read: list lead-ins and bullets whose base marker belonged to
  another item; split halves whose base marker belonged to the other clause (BF₂/Wang, Krieger/"It
  needs"/Jones, the three flood-gun studies, the "(on our reading)" SPOX clause, the monitor
  sentence); the repeated markers above; glance and label lines.
* **Caps**: para > 100 5 → 0; item > 60 6 → 1 (the PMOS-gate bullet, above); sentence > 45 12 → 0.
  First sentence 27 w (above).

### 083 2PSDI — done

* **Lead.** First sentence (32 w) split at its colon: "… before the strip PDIS. The PDK's mask list
  has a single "P+ Implant, PSDM".[^pdk-05]" (the marker stays on the mask-list fact; "described in
  this reference" stays on the reading). The 61-word "On that reading, …" sentence split twice: the
  region list after the dash became "Those are the PMOS source/drains, … opened by the nitride cut."
  ("Those are" added, step 7), and "and differs from the first only in …" became "On that reading,
  `2PSDI` differs from the first only in …" (the noun rather than "it" after a list; review L7) — the leading hedge **repeated** so the second sentence keeps it
  (R-SENTENCE step 5), and "Nothing public says which." still follows it directly. Two paragraphs,
  split before "On that reading" (the reading / what follows from it). 128 words (base 125, over 120
  already); first sentence 22.
* **After the figure.** "The PDK's implant-angle table lists three angles:" → R-LIST, three plain
  bullets, `[^pdk-03]` on the lead-in (the marker ended the enumerating sentence). The next paragraph
  opens "The PDK's physical-criteria table" ("Its" → "The PDK's", R-PARA step 5). No H3: the passage
  is 109 words.
* **R-CATEGORY.** Classification sentence (15 w) alone; the rest (the two-implants-one-mask pattern,
  which lists other steps, and "This is the only source/drain implant …") as one second paragraph, so
  that "This" keeps its sentence before it.
* **Why items.** Profile-shaping pair (143 w): lead kept whole as in the base ("… the contact needs; or two
  boron energies do the same.", 41 words; review L7 found the "Or" sentence clumsy); continuation 1 = Ogura, split
  at ", and on the n-type side" (each half keeps its markers); continuation 2 = Bourdelle/Wang and
  Josse, split at the semicolon, then "On this reading …". PMOS extension (180 w): lead = the
  cross-section sentence; continuation 1 = the Lin sentence (kept whole: its only split would move
  the Lin marker away from the claim) and the PDK-angles sentence; continuation 2 = the 71-word
  shadowing sentence split at its dash pair: "Such an implant would be shadowed by … capped gates and
  by the resist.[^krieger-1989] That is the shadowing that Krieger et al. analysed[^krieger-1989] and
  that the PDK's shadowing allowances budget for. Such an implant would more naturally run on a
  medium-current tool with tilt: …" (`[^krieger-1989]` **repeated** on the claim, which in the base
  was followed by Krieger's marker in its dash material — batch-4 M2, declared; "That is" added; "and
  would" → "Such an implant would", the noun back rather than an "It" that could be read as the
  shadowing). Device-specific (65 w): the base dash pair kept in place (review M1: a first draft moved it
  after the claim as "That is the 5 V PMOS …", which read as the place where the first implant does no
  harm); only the semicolon split, continuation from "The mask sharing argues …".
* **R-REPEAT not applied.** The 8250 quotation appears in Why ("Axcelis 8250 Mid current B11, BF2,
  As, ESC chuck, …") and under Machines likely used ("B11, BF2, As, ESC chuck, …"). The two copies
  are not the same quotation (only the Why copy names the tool), and the Why argument rests on it;
  removing it would lose a quotation, so both stay.
* **R-HEDGE.** The scope sentence ("An industry-generic description …; the two main readings differ in
  tool and geometry:") as the italic lead-in, word for word.
* **How items.** Deep-junction (88 w): lead split at its semicolon; continuation from "The amorphous
  layer …". Tilted extension (110 w, a 93-word sentence): lead = the dose/tilt sentence to "… electron shower." as in the
  base (51 words without the label, **listed**; review L7: split off, the tool phrase read as a
  fragment opening a paragraph); continuation = "The tilt is limited by the resist height.", "We read the PDK's thinner resist budget … though the PDK does not say
  so." (split at its two semicolons; "we read" stays on its clause), then Adachi.
* **R-TOOLS.** GSD and 8250: *SkyWater says:* the quotation (no subject in the base), *Tool exists:*,
  *Runs this step:*; the Eaton 8250HT sentence (a vendor description) is the continuation. Two tools.
* **R-RELATED.** Previous/Next split. "The n-type extensions that the flow *does* mask separately" →
  `Same module:` (NTM, HVNTM, LDNTM); "activation" → `Feeds:`; "The other two-implant-one-mask pairs"
  → `Same category:` (all Ion implantation steps); "Mask: PSDM" kept as `Mask:`; "The PMOS channel
  and gate" unlabelled. Order per R-RELATED.
* **R-OPENQ.** Labels "What `2PSDI` is", "Where the extension is formed", "Species, energy and
  dose", "Which implanter"; text unchanged.
* **R-GLANCE.** Does keeps "described in this reference"; Why names the three readings and that none
  is stated; Public numbers "none published for `2PSDI`" plus the PDK's `HVPTM shadowing` 0.089 µm
  `[^pdk-03]` as the page gives it; tool line GSD with both grades and "depending on the reading"; Not
  public from Open questions 1 and 3.
* **Preservation** (`--allow-regrouped` only): ADDED markers `krieger-1989` (repeat), `pdk-03`,
  `skw-01` (glance); numbers 0.089 (glance), "2"×2 (the code `2PSDI` in the glance and in an OQ
  label); ref `step-082`, hedges "inference", "likely", "not public" (glance). REGROUPED: the angle
  list (0 | 7 | 40, 23), the shadowing sentence (0.4, 0.18, 0.2 | 8250, 1, 11, 1, 14, 0-60), the
  tilted-extension sentence (10¹³, 10¹⁴ | 0.3, 1.14): same digits, same order. WORDS LOST: "and"
  (joining word at a split), "strength"×2.
* **Marker coverage.** 25 flags, all read: the angle bullets (marker on the lead-in); split halves whose
  base marker belonged to the other clause (mask list/description, Ogura/Lee, shadowing/"would more
  naturally run", deep-junction/amorphous layer, the tilted-extension pieces); the region list (a
  description of the first implant's regions, not a hedged claim); glance, grade and label lines.
* **Caps**: para > 100 2 → 0; item > 60 5 → 0; sentence > 45 6 → 1 (the tilted-extension lead, above;
  `caps.py` also flags the profile-pair and device-specific leads at 48 and 47, but 7 and 3 of those words
  are the bold label — guide problem 5 — so the sentences themselves are 41 and 44).

### 084 PDIS — done

* **Lead.** First sentence (37 w) split at ", and cleans" ("It cleans the wafer …"; the "(on our
  reading)" stays on the 2PSDI clause it governs). The 77-word sentence split at its colon ("… the
  hardest strips in the front end. The resist has taken a dose …"), both halves kept in one paragraph
  so the claim and its explanation stay together. Two paragraphs, split before "`PDIS` is the first of
  the two source/drain strips" ("It" → "`PDIS`", R-PARA step 5). 114 words as in the base; first
  sentence 21.
* **R-CATEGORY.** Classification sentence (13 w) alone; the category-page crust sentence (background,
  not specific to this step) as a plain paragraph in its place; the two sentences that describe this
  strip ("At 10¹⁵ cm⁻² the crust is at its thickest …", "The strip is therefore engineered around the
  crust …") → `**Specific to this step:**` and two bullets, in the base order.
* **Why.** Paragraph 1 (135 w) split before "The strip also removes" (clean removal / contamination);
  "must be gone *cleanly*:" → a full stop, the flake consequences their own sentence; Popped
  crust / Chan split at the semicolon and the contamination sentence at its semicolon ("Fujimura et
  al. showed …"), each half with its own markers.
* **R-HEDGE.** Italic lead-in, word for word.
* **How items.** Plasma ash (167 w): lead "Downstream microwave or RF oxygen plasma."; continuation 1 =
  the two-step sentence (split at its semicolon, "Then a hotter step …"), Fujimura, the Wikipedia
  quotation; continuation 2 = "SkyWater's ashers span exactly this range:[^skw-01]" with the three
  quoted asher entries as nested plain bullets (the marker ended the enumerating sentence, so it
  sits on the lead-in; every quotation unchanged); continuation 3 = the Iridia/CF₄ sentence, split at
  its semicolon ("The CF₄ additions … would, we infer, be omitted here."). Wet strip and clean (100 w):
  lead = the SPM/SC-1/SC-2 sentence to `[^wiki-rca]` (split at the semicolon); continuation from
  "Visintin, Korzenski and Baum".
* **R-TOOLS.** Four tools → recap table `Tool | Evidence`, the rows and wording of 067 (the same four
  tools and grades). Ashers: head keeps this reference's "— named with their gases and temperatures on
  SkyWater's facilities page" (not SkyWater's words, so no *SkyWater says:*); *Tool exists:*,
  *Runs this step:* with its reason (the Iridia clause is the reason, so it stays in the grade line).
  Benches: head with the quotation, *Tool exists:*. AIT: head with "our reading", *Tool exists:*
  medium (067's form).
* **R-RELATED.** "The oxide the strip must preserve" (SPOX) → `Same module:`; "The companion strip …
  the other high-dose strip … light-dose strips for contrast" → one `Same category:` bullet (all Resist
  strip / clean steps). Previous (with its "mask:" and "first implant:"), Next and Category page
  unchanged, as on 066.
* **R-OPENQ.** Labels "Ash recipe and wet sequence", "SC-2 and oxide loss", "Which asher"; text
  unchanged.
* **R-GLANCE.** Does/Why from the lead and Why; Public numbers "none published for SKY130" (the only
  numbers on the page are industry-typical doses and SkyWater's asher temperature ranges); tool line
  with both grades; Not public from Open questions 1–2.
* **Preservation** (`--allow-regrouped` only): ADDED marker `skw-01`, refs `step-080`, `step-081`,
  identifiers "SC-2" (OQ label), "SKY130", hedges "inference", "likely", "not public", "our reading"
  (glance), "inference" and "our reading" (recap table). WORDS LOST: "strength"×4.
* **Marker coverage.** 11 flags, all read: the asher bullets (marker on the lead-in); split halves whose
  base marker belonged to the other clause (hardest strips/dose, two-step/"Then …", Iridia/CF₄);
  glance and label lines.
* **Caps**: para > 100 2 → 0; item > 60 2 → 0; sentence > 45 4 → 0.

### 085 NSDM — done

* **Lead.** 66 words in one paragraph, first sentence 11: unchanged.
* **R-H3.** `### What the public record shows` after the figure caption, over the 163-word PDK paragraph
  (mask table, layers, the nsd rules, rpm.6, minimum CD).
* **R-SENTENCE.** The layer sentence split at its semicolon (`[^pdk-05]` on the mask table; the
  layers, their add/drop purposes, `[^pdk-06]` and the "so the reticle is derived …" reading stay one
  sentence, as in the base).
* **R-TABLE.** The nsd rules → `Rule | Constrains | Value (µm)` in the base order, as on 081;
  `[^pdk-periph]` on the lead-in "… opening for N+/P+ implants":[^pdk-periph]" (the base colon kept).
  nsd.5a and nsd.5b stay in one row because the base gives them one clause and one value ("enclosure
  of diffusion and of tap by 0.125 µm (nsd.5a, nsd.5b)"); nsd.7's cell is the base's own words ("to
  diffusion or tap of the opposite implant", no "spacing" added); nsd.8 and nsd.9 have no value
  (`—`); the two area rows keep "µm²" joined by a non-breaking space. LOST `number_order` checked by
  hand: nsd.1 0.380, nsd.2 0.380, nsd.5a/5b 0.125, nsd.6 zero, nsd.7 0.130, nsd.8 —, nsd.9 —,
  nsd.10a 0.265 µm², nsd.11 0.265 µm² — the base pairs. WORDS LOST "by" and "m" (µm to the header).
  The rpm.6 and minimum-CD sentence stays as the closing paragraph.
* **R-CATEGORY / R-LIST.** Classification sentence (≈ 25 w) alone. The 94-word "The differences are in
  what the resist must withstand — … — and in the fact that …" → "The differences are:" and two plain
  bullets, each keeping its "in"; the dash material of the first became its explanation after a colon,
  split at ", and arsenic" into "Arsenic is a heavier ion …, so we infer … (the paper's abstract does
  not compare species)" — the "we infer" and the caveat stay with that clause; `[^fujimura-1989]` stays
  on the carbonisation clause and `[^pdk-periph]` on the rule clause.
* **Why items.** "Source/drain of every NMOS" split at its internal semicolon ("… extensions.[^pdk-07]
  The drain-extended NMOS source must be enclosed …"); "poly contact heads" split at its semicolon
  ("The precision resistors themselves are kept 0.200 µm clear …"; the NPCM hedge stays on the first
  clause, which it governed).
* **R-HEDGE.** Italic lead-in, word for word.
* **How items.** "Resist coat" (74 w): lead = the resist sentence; continuation from "The thickness is
  again set …".
* **R-TOOLS.** i-line: no SkyWater statement beyond the marker on the head, so only *Tool exists:*
  and *Runs this step:*; tracks and overlay/CD in 068's form. Three tools, no recap table.
* **R-RELATED.** Previous/Next split; "Complementary mask: PSDM" and "The extensions the N⁺ junction
  joins" (ASTI, HVASTI, LDASTI) → one `Same module:` bullet; "Structures it dopes" unlabelled; "Mask
  page:" and the previous/next-mask bullet → one `Mask:` bullet.
* **R-OPENQ.** Labels "Resist and exposure tool", "How `cnsdm` is generated", "SONOS cell
  source/drain"; text unchanged.
* **R-GLANCE.** Does/Why from the lead and Why; Public numbers nsd.1/nsd.2 0.380 µm and rpm.6's
  0.200 µm `[^pdk-periph]`; tool line with both grades; Not public from Open questions 1.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-periph`, `skw-01`, numbers 0.200,
  0.380, 1, 2, 6, ⁺, ref `step-086`, hedges "inference", "likely", "not public" — the glance box.
  LOST `number_order` for the nsd table, checked above. WORDS LOST: "by", "m", "page" ("Mask page:"
  → "Mask:"), "strength"×3.
* **Marker coverage.** 12 flags, all read: split halves whose base marker belonged to the other clause
  (mask table/layers, the two category bullets, the NMOS item, the poly-heads item); glance and label
  lines.
* **Caps**: para > 100 2 → 0; item > 60 1 → 0; sentence > 45 5 → 0.

### 086 NSDI — done

* **Lead.** The 54-word first sentence split at its dash: "… and all the other N⁺ diffusions of the
  process.[^pdk-07] These are the n⁺ taps …, the N⁺ diffusion resistors and the n-side of the P-well
  diodes.[^pdk-07]" ("These are" added; `[^pdk-07]` **repeated** on the first half because the base's
  single marker covered the whole sentence — masks-b H1, declared). The 48-word second sentence split at
  ", so that" ("So the heavy junction stands …", a sentence; "(on our reading)" stays on the SPOX
  clause it governs). Two paragraphs, split before "`NSDI` goes through" ("It" → "`NSDI`", R-PARA step
  5). 114 words as in the base. **First sentence 26 words, left**: no further seam.
* **R-H3.** `### What the public record shows` after the figure caption, over the 197-word PDK and
  test-tile paragraph.
* **R-LIST.** "What the PDK says about the result is the same as for the P⁺ junction:" → three plain
  bullets, each with its own marker as in the base (the joining "and" dropped).
* **R-SENTENCE (test tile).** The 64-word sentence split at its dash: "… 116.7 Ω per square, contacts
  included (our extraction from the published
  measurements; the files record no temperature, date or
  wafer).[^raw-data-passives][^raw-data-testtile-pads] They are inside those limits and, like the
  nominal values, lower for the high-voltage structure (our extraction from the published measurements;
  the files record no temperature, date or wafer).[^raw-data-passives][^raw-data-testtile-pads]". The
  trailing extraction hedge, with its "the files record no temperature, date or wafer" caveat, covered the
  values, so it is **repeated in full** on the first half with both markers (review L2), which makes that sentence 50 words (**listed**: the hedge
  cannot be shortened) and its paragraph 101, so the test-tile sentences became their own paragraph
  (a new source, not a connective)
  (R-SENTENCE step 5, the batch-4 form on 053/055/056; declared); "They are" added.
* **R-CATEGORY.** Classification sentence (≈ 30 w) alone; "Its partner is PSDI" → "`NSDI`'s partner"
  opens the second paragraph (R-PARA step 5), and the "What distinguishes it …" sentence (its own
  label) follows, split at its semicolon ("What distinguishes it from the boron side is the ion: …").
* **Why.** The 56-word depth/offset sentence split at ", and its offset" ("Its offset from the gate …").
  The arsenic paragraph (168 w): the four studies after "its activation is limited by clustering:"
  became plain bullets (a list of studies; each keeps its marker; the joining "and" dropped); the
  Rousseau bullet split at its dash ("… *injects interstitials*.[^rousseau-1994] So an over-active
  arsenic layer …", `[^rousseau-1994]` **repeated** on the finding, which in the base shared the one
  marker; declared). "Adding a lighter phosphorus component …" and the SkyWater sentence follow as a
  paragraph. "Two things this implant does *not* do, on the reading used throughout this reference" →
  colon and two bullets (the hedge on the lead-in covers both); the gate bullet split after its dash
  clause: "… would do no harm. That is one reason the capped-gate reading is hard to test from the NMOS
  side." ("which is" → "That is", step 7; "although" kept in its clause). The closing sentence opens
  "`NSDI` *does* dope" ("It" → "`NSDI`").
* **R-HEDGE.** Italic lead-in, word for word.
* **How items.** Energy and dose (74 w): lead split at its semicolon; the Wikipedia sentence split after
  the quotation's marker ("The layer regrows by solid-phase epitaxy …", each half keeps its markers).
  Tilt (63 w): lead "0°, per the PDK's … entry.[^pdk-03]"; continuation from "The amorphisation …".
  Wafer handling (79 w): lead = the cooling sentence; continuation = "Charging control by plasma flood
  gun is critical … wafer:" with the three studies as nested plain bullets (the dash became the colon).
* **R-TOOLS.** GSD: *SkyWater says:* the two quotations (no subject in the base), *Tool exists:*
  **strong** …, *Runs this step:* the **inference** with the 8250 quotation it rests on; the Axcelis
  press-release sentence is the continuation. One tool.
* **R-RELATED.** Previous/Next split; "Complementary implant", "The extensions it joins … the halos
  around them" → one `Same module:` bullet (PSDI, 2PSDI, ASTI, HVASTI, LDASTI, BHI, LDBHI all carry
  this module's Phase cell); "The offset … the screen … the poly heads it dopes" → `Depends on:`; "The
  n⁺ gate it does not need to dope" (P1I) unlabelled.
* **R-OPENQ.** Labels "Species, energy and dose", "SONOS cell source/drain", "Shielding of the capped
  gates", "Which implanter"; text unchanged.
* **R-GLANCE.** Does/Why from the lead and Why; Public numbers S/D XJ 0.1 µm and 0° `[^pdk-03]`,
  `RSN` 120 Ω/sq with its limits `[^pdk-07]`; tool line with both grades; Not public from Open
  questions 1.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-07` (repeat), `raw-data-passives`,
  `raw-data-testtile-pads` (repeats), `rousseau-1994` (repeat), `pdk-03`, a second `pdk-07`, `skw-01`
  (glance); numbers 0, 0.1, 108–132, 120, ⁺×2, quotes "High current", "N+ or P+ S/D (XJ)" (glance);
  hedges "our extraction" (the repeat above), "inference", "likely", "not public" (glance). REGROUPED:
  the lead, the PDK list, the "Two things" list, the tilt item (same digits, same order). WORDS LOST:
  "and"×2 (list joins), "it"×2 and "its" (the nouns put back), "strength".
* **Marker coverage.** 31 flags, all read: list lead-ins and items whose base marker belonged to
  another item (the PDK list, the four studies, the flood-gun studies); split halves whose base
  marker belonged to the other clause (depth/offset, screen oxide/amorphisation, tilt/amorphisation);
  the repeated markers above; glance and label lines.
* **Caps**: para > 100 4 → 0; item > 60 4 → 0; sentence > 45 9 → 0. First sentence 26 w (above).

### 087 NSDIS — done

* **Lead.** First sentence (26 w) split at ", and cleans" ("It cleans the wafer …"); the 60-word
  third sentence split at its semicolon ("It is therefore also the *pre-anneal clean*, …", the "(the
  species we infer on NSDI)" staying in its dash material). One paragraph, 86 words; first sentence 13.
* **After the figure.** The 123-word paragraph split before "The surface under the resist" (the crust
  / the surface). The 47-word surface sentence is **left**: "on our reading of the flow" governs its
  dash list and its closing participle ("thinned slightly … still needed to cap the anneal"), and
  either split would leave a piece outside that hedge.
* **R-CATEGORY.** Classification sentence (18 w) alone; the category-page crust sentence split at its
  semicolon ("At an arsenic dose of 10¹⁵ cm⁻² the crust is at its worst.") as the second paragraph;
  "What distinguishes this strip from `PDIS` is …" is its own label (step 3), split at ", so the wet
  clean" ("So the wet clean must …", a sentence).
* **Why.** "Two things must be true before RTAD." → colon and two bullets, each opening with its own
  claim in bold ("The resist must be entirely gone.", "The wafer must be clean of metals:"; the
  joining "And" dropped); the first split at its dash and at ", and a popped flake"; the Fujimura/Kern
  sentence stays as the paragraph after (R-LIST step 4). The arsenic paragraph's 59-word sentence split
  at its semicolon ("This is a matter of facility design …", both "(industry practice)" tags kept on
  their clauses).
* **R-HEDGE.** Italic lead-in, word for word.
* **How items.** Plasma ash (152 w): lead "Downstream microwave or RF oxygen plasma." (split at the
  semicolon); continuation 1 = the two-step sentence, Nitrogen/forming gas (split at its semicolon,
  "Chan, Chiu and Tao describe …"), the Wikipedia quotation; continuation 2 = "SkyWater's three ashers
  cover the gases and temperatures such a recipe needs:[^skw-01]" with the three quoted entries as
  nested plain bullets (the dash pair became the list; the marker, which ended the enumeration, sits on
  the lead-in), then "The CF₄ options would, we infer, be left out to spare the oxide." Wet strip and
  clean (126 w, a 67-word sentence): the label as the lead, the three chemistries as sub-bullets
  (SPM with its quotation and `[^wiki-piranha]`; "SC-1 for particles;[^wiki-rca]"; "and, we infer,
  SC-2 for metals … "…80 °C".[^wiki-rca]"), `[^wiki-rca]` **repeated** on the SC-1 item because the
  base's one marker after the SC-2 quotation closed the whole sentence (masks-b H1, declared); the
  continuation from "Visintin, Korzenski and Baum" unchanged.
* **R-TOOLS.** Ashers: this reference's head ("— named on SkyWater's facilities page …"), *Tool
  exists:*, *Runs this step:* with the Iridia reason. Benches: head with both quotations, *Tool
  exists:*, *Runs this step:* the DNS/FSI SC-2 "(inference)". AIT: *Tool exists:* medium. Three tools,
  no recap table.
* **Resources.** The 46-word first bullet is **left as in the base** (review L3): a split at the
  semicolon after `[^skw-01][^fujimura-1994]` left the last resource of the semicolon list, "arsenic-tolerant
  exhaust scrubbing", hanging off the CF₄ sentence, and its link text cannot be recapitalised to stand
  alone.
* **R-RELATED.** "The oxide the strip must preserve" → `Same module:`; "Companion strip … the other
  high-dose strip" → `Same category:` (PDIS, P1IS are Resist strip / clean steps); "the earlier
  pre-anneal strip of the well module: PWDEIS before RTAI" split off unlabelled (RTAI is an anneal, so
  `Same category:` would be false for it). Previous and Next unchanged.
* **R-OPENQ.** Labels "Ash recipe and wet sequence", "How much oxide survives", "Which asher and
  bench"; text unchanged.
* **R-GLANCE.** Does/Why from the lead ("(the species we infer)" kept); Public numbers "none published
  for SKY130"; tool line with both grades; Not public from the three Open questions.
* **Preservation** (`--allow-regrouped` only): ADDED markers `wiki-rca` (repeat), `skw-01`, number ⁺,
  refs `step-085`, `step-088`, identifiers "SC-2", "SKY130", hedges "inference", "likely", "not public",
  "we infer" — the glance box. REGROUPED: the wet-clean sentence (3, 1, 30 | 6, 1, 1, 75, 80), same
  digits, same order. WORDS LOST: "strength"×3.
* **Marker coverage.** 13 flags, all read: the asher bullets (marker on the lead-in); split halves whose
  base marker belonged to the other clause (crust quotation/"At an arsenic dose", "Downstream …"
  lead/quotation, CF₄); glance and label lines.
* **Caps**: para > 100 3 → 0; item > 60 2 → 0; sentence > 45 8 → 2 (the surface sentence and the
  Resources bullet, above).

### 088 RTAD — done

* **Lead.** The 98-word second sentence (three dash pairs) re-presented as four sentences, every
  clause kept and the numbers in the base order: "The three heavy implants of the module — PSDI,
  2PSDI and NSDI — have left … inactive. This step heats the wafer so that the amorphous layers regrow,
  … and the junctions reach their designed depth and no further. It does so in an inert ambient for
  seconds at around 1000 °C on the industry-typical recipe described below; SKY130's own conditions
  are not public. The designed depth is the PDK's 0.1 µm for "N+ or P+ S/D (XJ)".[^pdk-03]" — the
  paragraph break after it (review L5; a first draft broke one sentence earlier). That paragraph measured
  107 words, so the base's 154-word lead takes three paragraphs (§4.1 note ¹): a second break before
  the heating sentence, whose "this step" became "`RTAD`" so that no paragraph opens on "This" ("It does so" and "The designed depth is" added, step 7; the
  industry-typical hedge and "not public" stay with the 1000 °C clause they governed; the marker stays
  with the 0.1 µm). "This reference describes it" → "This reference describes `RTAD`" (R-PARA step 5,
  since the sentence before it is now about the depth). Two paragraphs; 157 words (base 154, over 120
  already); first sentence 6.
* **After the figure.** The NPCM-reading sentence split at its semicolon ("It re-anneals the extensions
  and halos …"; "On the reading of the NPCM page" governs the poly-head clause, as in the base).
* **R-CATEGORY / R-LIST.** The classification sentence ends "… but with the tightest constraint of the
  three:" and the three-way comparison (well anneal / tip anneal / this one) became three plain bullets;
  the third split at "while moving" ("It has to do so while moving the deep junctions …", "It has to do
  so" added so the "has to" still governs the second half). "It is the anneal for which the *spike* RTA
  was developed" follows the list as prose with its noun ("`RTAD` is …").
* **Why.** The 62-word regrowth sentence split at its semicolon ("Partially damaged layers need
  800–1000 °C …", each half with its own markers); "Two effects make … as the category page explains:"
  as its own lead-in paragraph. TED bullet (125 w): lead = the interstitial sentence (split at its
  semicolon); continuation 1 = Michel, Eaglesham, Stolk and "TED is worst for slow, cool anneals, so the
  resolution is to go hot and fast." (split at the colon); continuation 2 = Agarwal ×3, Fiory,
  Gerritsen. Activation bullet (95 w): continuation from "The highest activation is obtained …" with its
  "(inference; no public source describes a second anneal)". The 103-word Josse paragraph split before
  "The fluorine from BF₂ implants"; the 60-word sentence split at ", and the surrounding films matter"
  and at ", and shallow arsenic" (each piece with its own marker; "we infer" and "(its retention is not
  public)" stay on the SPOX clause).
* **R-HEDGE.** Italic lead-in, word for word.
* **How items.** Tool and ambient (65 w): lead = the RTP sentence with the Wikipedia quotations;
  continuation from "A small oxygen addition". Temperature and time (75 w): lead = the soak/spike
  sentence to `[^txt-05][^txt-10]` (split at the semicolon); continuation from "ITRS 2001 sets …".
  Control (85 w): lead = the emissivity sentence (split at its dash); continuation = Sorrell and
  Gyurcsik / Chen (split at the semicolon), Vandenabeele, Roozeboom, edge ring. Diffusion budget
  (65 w): continuation from "The PDK's out-diffusion limits".
* **R-TOOLS.** Heatpulse (154 w, an 82-word sentence): *SkyWater says:* "lists under RTA "Ag Heatpulse
  8808 …"" (verb-first, the fix batch 5 L5 asked for on 075); *Tool exists:* **strong** (SkyWater
  statement); *Runs this step:* the **inference** and its reason ("the only RTA on SkyWater's list, and
  a source/drain activation is the archetypal use of such a tool"). This reference's gloss of the list
  (the dash material "a single-wafer RTA with the inert ambients …") is the first continuation, with its
  noun ("The Heatpulse 8808 is …", R-TOOLS step 2); the reseller, blog and specification-PDF sentences
  follow unchanged except that "…applications,[^ag-8800] and a vendor blog post" became two sentences.
  The reseller paragraph comes directly after the grades, then the gloss (review L4: in the base a colon
  tied the grade's reason to that evidence).
  Aviza: pilot-form head, *Tool exists:* strong, *Runs this step:* weak.
* **R-RELATED.** Previous/Next split; "The cap during the anneal … the spacers the dopant meets" →
  `Same module:` (SPOX, SPNIT); "Earlier RTAs" → `Same category:` (RTAI and TIPRTAD are Anneal steps);
  "Anneals the implants of …" keeps no label (its gloss is a sentence; a label would reword it).
* **R-OPENQ.** Labels "Temperature, time and ambient", "Why two anneals", "Heatpulse 8808",
  "Specification PDF"; text unchanged.
* **R-GLANCE.** Does/Why from the lead and Why; Public numbers the S/D XJ 0.1 µm `[^pdk-03]` and the
  120/197 Ω/sq sheet resistances `[^pdk-08]`; tool line with both grades; Not public from Open
  questions 1–2.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03`, `pdk-08`, `skw-01`, numbers
  0.1, 120, 197, quote "N+ or P+ S/D (XJ)", hedges "inference", "likely", "not public" (glance);
  "8808"×3 (glance, the OQ label, the gloss's noun). REGROUPED: the lead (1000 | 0.1), the regrowth
  sentence (500 | 800–1000), the soak/spike item (… | 2001). WORDS LOST: "strength"×2.
* **Marker coverage.** 21 flags, all read: split halves whose base marker belonged to the other
  clause (the lead's depth, regrowth/defect clusters, fluorine/spacers/arsenic, emissivity/studies,
  reseller/blog); the gloss after the grades; glance and label lines.
* **Caps**: para > 100 3 → 0; item > 60 7 → 0; sentence > 45 10 → 0.
