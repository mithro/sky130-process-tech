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
  nitride, about 0.2 µm of it … "poly cap after SPE".[^pdk-03] It stops on the poly, leaving bare
  polysilicon exactly "under licon1 areas".[^pdk-06]" ("The cap is" and "It" added, step 7; each
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
  (…): the opened poly is doped …" is **left whole**: every split point would put the doping clause
  outside the "on our reading" that governs it. "Two failure modes make the recipe demanding." →
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
* **R-RELATED.** Previous and Next split; "The stack being cut … the spacer beside it" and "the
  resistors whose heads are opened" → one `Depends on:` bullet; "The implants that dope the opened
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
* **Caps**: para > 100 4 → 0; item > 60 2 → 0; sentence > 45 10 → 1 (the
  51-word "order … on our reading" sentence, above).
