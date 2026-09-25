# Readability guide — the rule book for the readability phase

This is the one document an executor needs. It consolidates `docs/plans/readability/report-A.md`
(step pages), `report-B.md` (machine, material, mask and category pages and their indexes),
`report-C.md` (links, navigation, references, theme) and `report-D.md` (figures) with the decisions in
`docs/plans/readability-plan.md`. Where two reports gave different numbers for the same thing, this guide
picks one and says so in §1; the reports are history, this guide is the rule.

**Who reads what.**

* **Executor** (Sonnet-class): you are given this guide and a batch of pages. Work one page at a time.
  Apply only the rules your page type lists, in the order it lists them (§4), then run the per-page
  procedure (§7). If a rule does not clearly apply, leave the text alone. You are never asked to judge
  whether a fact is right.
* **Reviewer** (Opus): check the diff and the rendered tiles against §8.
* Rules marked **blocked** (§9) must not be started until the named workstream has landed.

**The one sentence that outranks everything else:** this phase changes presentation, never content. If you
cannot re-present a passage without changing what it claims, leave it exactly as it is and write a line in
your progress file.

## 1. Limits for the whole site

One table. It applies to every page type unless a page-type section in §4 narrows it.

| Element | Target | Hard cap | Measured how | Resolved from |
|---|---|---|---|---|
| Prose paragraph | 40–80 words | **100 words**; anything ≥ 120 must be split | words after deleting `[^…]` markers and `{role}` wrappers (`measure.py` counts this way) | A F1 (cap 100) vs B15 (cap 120/flag 150) vs C7 (cap 130) → **100** |
| List item (outside `## References`) | ≤ 40 words | **60 words** | same | A F1 and B15 agree |
| List item lead sentence, when the item has sub-bullets | ≤ 30 words | 30 | same | A F1 |
| Sentence | ≤ 30 words | **45 words** | words between full stops, markers removed | A F8 (30/45) vs B (35/45) → **30/45** |
| Em-dash pairs or parentheticals per sentence | 0–1 | 1 | count of ` — ` pairs and `(…)` | A F8 |
| Parenthetical length | ≤ 11 words | 11; ≥ 12 words becomes its own sentence | words inside `(…)` | A F8 |
| Step-page lead (text between `## What this step is` and the first `###`) | ≤ 2 paragraphs, ≤ 120 words | 120 | `measure.py` section stats | A F2 |
| First sentence of a step page | ≤ 25 words | 25 | — | A F11 |
| Class-page intro (machine, material, mask, category), before the quick-facts table | ≤ 70 words | 70 | — | B15 |
| Index-page purpose paragraph | ≤ 80 words | 80 | — | B3, C §2 |
| Glossary entry | ≤ 80 words | 80 | — | C9 |
| Table cell | ≤ 25 words | 25 | words in the cell, markers removed | B §2.3 |
| Quick-facts cell | ≤ 20 words, ≤ 1 quotation | 20 | same | B5 |
| Links in one table cell | ≤ 8 | 8; more becomes "N steps — see §…" | count of `{ref}` | B §2.3 |
| Table columns | ≤ 3 if any column holds prose; ≤ 5 if every cell is a number, a code or ≤ 3 words | must pass the phone test: no horizontal scroll at 400 px, no number broken across lines (a thousands-space number such as "1 825" wraps at the space, so a cell holding one must be ≤ 12 characters) | header row, then rendered at 400 px | A F3 (≤ 5) vs B §2.1 vs review D8 (tested, not counted) |
| Table rows | ≤ 40 | 40; more → split by group under H3s | — | B §2.7 |
| Footnote markers per paragraph | ≤ 4 | **6**; at 5 or more, ask whether the paragraph is a table | count of `[^…]` | A F2/F3 (≤ 6) vs C7 (consider at > 4) → target 4, cap 6 |
| H3s per step page | 3–6 | — | — | A F2 |
| Admonitions per page | ≤ 2 | 2 | `:::{note}`, `:::{admonition}`, `:::{seealso}` | A §2 |
| Figure caption | what is shown · the page's hedges · the citation · "Not to scale" | — | — | D §3 |
| Figure alt text | 60–450 characters, no citations | 450 | — | D §3 |

Word counts ignore footnote markers and role wrappers, because that is what the measurement scripts do
(`docs/plans/readability/prototypes/measure/measure.py`, function `clean`). A number, a code span or a
quotation counts as one word.

## 2. Never

These are absolute. A reviewer who finds one of them rejects the whole page.

1. **Never change a fact, a number, a unit, a significant figure, a quotation, a hedge or a citation.**
   Not "1 800 Å" → "1800 Å", not "about 0.33 µm" → "0.33 µm", not "we infer" → "the PDK shows".
   Thousands spacing, "about", "~", "approximately" and quotation marks stay exactly as written.
2. **Never upgrade a hedge**, in either direction. "our reading" does not become "the PDK gives";
   "SkyWater states" does not become "we infer". When you move a sentence, its hedge moves with it,
   word for word. Never delete a hedge, even when the same hedge already appears two lines above.
3. **Never remove or move a footnote marker away from the claim it supports.** A marker travels with its
   clause. When a paragraph is split, each half keeps the markers of its own sentences.
4. **Never fill an empty cell from memory.** A value the page does not give is `—` (em dash), or the
   page's own words ("not public", "not stated", "no vendor description was retrieved").
5. **Never move text across a `{dropdown}` boundary**, in or out, and never paraphrase, summarise or
   quote the content of a collapsed in-force note outside it. Rules R-PARA, R-TABLE, R-LIST and
   R-SENTENCE apply *inside* a dropdown, to the text that is already there.
6. **Never mention an in-force patent's content, number or title in the open.** What
   `tools/check_inforce.py` enforces, from the code:
   * every family in `data/patents.yaml` whose `expired` is not `true` is *restricted*: its members'
     publication numbers **in any spelling** (`US8093128B2`, `US 8,093,128 B2`, `8093128`, `8,093,128`,
     `US 2009/0179253 A1`, `EP 2 104 648 B1`), its titles of five words or more, and the footnote labels
     and inventory keys whose definitions name one of those numbers;
   * plus, per family, a list of `PHRASES` — distinctive wording taken from the patent. A phrase is
     *content*, so it is refused everywhere outside a collapsed block, footnote definitions and the
     inventory entry included;
   * any of those outside a `{dropdown}` (colon fence or backtick fence) is an error. Matching runs on a
     whitespace-flattened page, so a number split over a line break is still caught;
   * exceptions: the dropdown's own **title line**, a footnote *definition* at the foot of the page, and
     the patent's own inventory entry — and each of those must carry the exact flag sentence
     "Shown as in force; estimated expiry YYYY-MM-DD (estimate from public records, not legal advice)."
     (or the "Status shown as unknown; estimated expiry no later than …" wording) with the dataset's date;
   * a `{dropdown}` whose body is blank is an error ("it renders as an empty collapsible"): never leave a
     note empty by moving its content out.
   Practical consequence: **"At a glance" boxes, tables, captions, figures and summaries must not repeat
   anything from a collapsed note** — not the number, not the title, not the numbers inside it.
7. **In-force dropdown titles stay as they are.** The owner's wording
   (`From a patent shown as in force (…; estimated expiry …) — open to read`) is not to be shortened by an
   executor. A F12 proposes a shorter form; it is an owner decision and is **blocked** (§9).
8. **Never hand-edit a generated block or a generated page.** These are generator output:
   * the block between `<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->`
     and `<!-- index-links:end -->` on 206 pages (steps, machines, materials, categories, masks, overview);
   * `docs/steps/index.md` in full (written by `tools/gen_steps.py`);
   * everything under `docs/references/papers/`, `docs/references/patents/` and
     `docs/references/filings/` (`gen_papers.py`, `gen_patents.py`, `gen_filings.py`);
   * once W1a lands: `docs/_static/figures/*.svg` and the MyST blocks in `data/figures/*.yaml` output.
   A change to any of these is a change to the generator plus one regeneration commit.
9. **Never rename, reorder, delete or add a mandatory heading.** Per page type, from the checkers:
   * **step page** (`tools/check_steps.py`, all 13 must appear, each alone on its line):
     `## What this step is`, `## Step category`, `## Why this step exists`,
     `## How it is typically performed`, `## Machines typically used`,
     `## Machines likely used at SkyWater`, `## Resources required`,
     `## Related steps and cross-references`, `## References`, `### Cross-check`,
     `### High-level understanding`, `### Deep dive`, `## Open questions`;
   * **machine page** (`check_machines.py`, H2s exactly these, in order): `What the machine class is and
     how it works`, `Representative 200 mm-era models`, `At SkyWater`, `Consumables and facilities`,
     `Process-integration notes for SKY130`, `Related pages`, `References`, `Open questions`; H3s under
     `At SkyWater` exactly `What SkyWater lists`, `Strength of the evidence`,
     `SKY130 steps assigned to this class`; under `References` exactly the three tiers;
   * **material page** (`check_materials.py`): `What the class is and what it does`,
     `Representative materials and grades`, `At SkyWater`, `Supply, handling, safety and facilities`,
     `Process-integration notes for SKY130`, `Related pages`, `References`, `Open questions`; H3s under
     `At SkyWater` exactly `What SkyWater's filings and pages list`, `Strength of the evidence`,
     `SKY130 steps that use this class`; under `References` the three tiers;
   * **mask page** (`check_masks.py`): `What the mask defines`, `Drawn layers and derivation`,
     `Plates and reticle sets`, `Lithography and pattern transfer`, `Steps that use this mask`,
     `Design rules and critical dimensions`, `Related pages`, `References`, `Open questions`; H3s under
     `Drawn layers and derivation` exactly `In the PDK`, `In the public renders`; under `References` the
     three tiers; under `Plates and reticle sets` only `The mask-type record`; **no other H2 may have any
     H3 at all** until W0e;
   * `## References` must occur **exactly once** on every page that carries a generated index-links block.
10. **Never use `{numref}`.** `numfig` is off; `{numref}` emits a warning and the `-W` build fails
    (verified in this project, §6).
11. **Never add an external link whose URL is not already written in one of that page's own footnote
    definitions**, character for character. An inline link is only a convenience copy of a keyed
    footnote; that is what keeps `tools/check_links.py` coverage and the inventory keys complete.
12. **Never delete a reading-list bullet, and never change how many `* ` bullets sit under
    `### Deep dive`.** `check_refs.py` counts them (minimum 8 on a step or per-mask page, 12 on a
    category, machine, material or overview page and the masks index). Splitting one bullet into two, or
    folding two into one, changes the count.
13. **Never delete a duplicate sentence before checking its footnote labels.** Every definition must
    still be referenced at least once on the page, or the `-W` build fails.
14. **Never fix arithmetic, a wrong unit or a doubtful fact.** Write it in your progress file with
    `file:line` and move on.
15. **Never touch another worktree, `main`, a checker, a generator or `docs/plans/readability/`.**

## 3. The rules

| Id | What it fixes | Page types | Kind | Blocked |
|---|---|---|---|---|
| **R-PARA** | paragraphs > 100 words, list items > 60 | all | hand | — |
| **R-SENTENCE** | sentences > 45 words, em-dash chains, long parentheticals | all | hand | — |
| **R-LIST** | enumerations written as one sentence | all | hand | — |
| **R-H3** | > 120 words under an H2 with no structure; bold run-ins that are headings | step, machine, material, overview; **mask** blocked | hand | W0e (masks) |
| **R-INTRO** | intros > 70 words; pointer sentences; the template sentence | machine, material, mask, category | hand | — |
| **R-CATEGORY** | `## Step category` as one dense paragraph | step | hand | — |
| **R-HEDGE** | the scope sentence; mid-sentence hedges | step | part scripted | — |
| **R-REPEAT** | the same sentence in two sections | step, class | hand | — |
| **R-GLANCE** | no summary at the top | step | hand, last | — |
| **R-TOOLS** | "Strength:" run-on bullets | step | scripted split, hand assignment | — |
| **R-OPENQ** | Open-questions bullets with no label | step | hand | — |
| **R-RELATED** | unordered related-links sections | step, class | hand | — |
| **R-CODE** | identifiers not code-formatted | all | hand, opportunistic | — |
| **R-TABLE** | parallel numeric data written as prose or bullets | all | hand | — |
| **R-DERIVATION** | arithmetic buried in prose | step | hand | — |
| **R-MODELS** | "Representative …" as vendor paragraphs | machine, material | hand | — |
| **R-ENTRIES** | "read term by term" paragraphs | machine, material, mask | hand | — |
| **R-QUICKFACTS** | quick-facts cells > 20 words | machine, material (mask: leave) | hand | — |
| **R-PARAMS** | number-dense paragraph beside a table | mask | hand | — |
| **R-COMPARE** | category comparisons; consumables that link nowhere | category | part scripted | — |
| **R-CAPTION** | tables with no caption | all | hand | — |
| **R-LINKS** | reading-list bullets and named titles are not links | all | scripted + hand | **W0c** |
| **R-WAYBACK** | dead cited URLs | all | hand | W0f (tooling) |
| **R-STEPRUN** | runs of step links; bare-number link text | machine, material, index | scripted / generated | — |
| **R-INDEX** | methodology before navigation on index pages | the five indexes | hand (moves) | W0d (parts) |
| **R-TERM** | missing `{term}` links; the glossary page | all, glossary | scripted proposal | W0d (Phase cell) |
| **R-CARDS** | landing page is a bare table of contents | landing, section fronts | hand | — |
| **R-ANCHOR** | inventory entries have no anchors | inventory | scripted | — |
| **R-DROPDOWN** | in-force notes and their pointer prose | any page with a note | hand | owner (titles) |
| **R-GENBLOCK** | the generated index-links block | 206 pages | **generator only** | W0d |
| **R-FIGURE** | no figures anywhere | step, machine, mask, category, overview | **generator only** | **W1a** |

Every rule has the same six fields.

* **Applies when** — a trigger you can decide mechanically, without judgement about content.
* **Do** — numbered steps.
* **Example** — a real passage. Line numbers are as of commit `5a70cf3c` on `main`; if the text has
  moved, search for the quoted words rather than trusting the number.
* **Do not touch** — what stays byte-identical.
* **Find** — the grep or the measurement script that lists candidates.
* **Kind** — `hand` (a model edits), `scripted` (a script proposes the edit, a model accepts or rejects
  each one), `generator` (**never done by hand**: change the generator, regenerate).

**Running the measurement scripts.** `docs/plans/readability/prototypes/measure/measure*.py` resolve the
repository root as `Path(__file__).resolve().parents[3]`; at their committed location that is
`docs/plans`, so they silently measure nothing. Copy them three levels below the root first, which is
where they were written to live:

```
mkdir -p tmp/readability/a-tools
cp docs/plans/readability/prototypes/measure/measure*.py tmp/readability/a-tools/
python3 tmp/readability/a-tools/measure.py      # paragraph, item and section stats + file:line worklists
python3 tmp/readability/a-tools/measure2.py     # sentence, hedge, em-dash and parenthetical stats
python3 tmp/readability/a-tools/measure3.py     # repetition and table candidates
python3 tmp/readability/a-tools/measure4.py     # roll-call clauses, design-rule ids, inline enumerations
```

`measure_b.py` (machine, material, mask, category pages) resolves paths from the current directory
instead, so run it from the repository root and pass `--list` for examples:

```
python3 docs/plans/readability/prototypes/measure/measure_b.py --list
```

Its keys are the triggers used below: `para>100w`, `para>150w`, `para>=3semicolons`, `bullet>60w`,
`bullet>100w`, `sentence>45w`, `steplink-run-paragraph`, `bullet>=8steplinks`, `tablecell>=8steplinks`,
`tablecell>40w`, `table>=5cols`.

### 3.1 Prose

#### R-PARA — paragraphs and list items that are too long
*(reports A F1 and B15, merged)*

**Applies when** a prose paragraph exceeds 100 words, or a list item outside `## References` exceeds
60 words.

**Do.**
1. Read the block and find its seams: a new source, a new quantity, a new question, a change of subject.
2. Split at a seam. Keep every sentence, in its original order and wording. Never start a new
   paragraph with a connective (So, This, But, Which, Because): it means the seam was not real, and
   the reader is left inferring a cause the split removed. If the only split point is before one, do
   not split. A split that leaves a block over the cap is no split.
3. Give each new paragraph a bold run-in label of 2–4 words followed by a full stop
   (`**PDK thickness.** …`) when the block is part of an evidence sequence; a narrative passage takes no
   label.
4. A list item over 60 words keeps a lead sentence of ≤ 30 words; the rest becomes sub-bullets (one fact
   and one marker each) or an indented continuation paragraph — indented by two spaces, with a blank
   line before it.
5. Reword only as far as the split requires: a pronoun may need its noun back ("it" → "the oxide").
   Nothing else.
6. If the block is mostly numbers, stop and apply **R-TABLE** instead; if it is mostly arithmetic,
   **R-DERIVATION**.

**Example** — `docs/steps/043-gox100.md:26`, one 278-word paragraph.

Before:

```
The PDK gives the finished thickness: "All high voltage devices use
110A gate oxide thickness just like low voltage (0 to Vcc) devices" …
[^pdk-hv] … `toxe = 1.16e-8` (11.6 nm) …[^pdk-model-nfet5v] Measured
capacitance is consistent with those figures. The SKY130 raw-data
repository publishes capacitance–voltage sweeps … [^raw-data-testtile-pads]
Splitting the accumulation capacitance … (our extraction from the published
measurements, without corrections …).[^raw-data-hv-mosfets] The files record
neither the measurement frequency nor the temperature. …
```

After (same sentences, same order, same markers):

```
**PDK thickness.** The PDK gives the finished thickness: "All high voltage devices use
110A gate oxide thickness just like low voltage (0 to Vcc) devices" …[^pdk-hv] … `toxe =
1.16e-8` (11.6 nm) as its oxide thickness for electrical purposes.[^pdk-model-nfet5v]

**Measured capacitance.** Measured capacitance is consistent with those figures. The
SKY130 raw-data repository publishes capacitance–voltage sweeps …[^raw-data-testtile-pads]
Splitting the accumulation capacitance … (our extraction from the published measurements,
without corrections for gate depletion, the thickness of the accumulation layer or fringing
fields, so not a physical thickness).[^raw-data-hv-mosfets] The files record neither the
measurement frequency nor the temperature.
```

**Do not touch.** The quotations, the numbers, the parenthetical hedge, the order of the claims, the
markers. Never split between a quotation and its attribution, or between a claim and its marker.

**Find.** `python3 tmp/readability/a-tools/measure.py` prints "top 15 paragraphs" and "top 10 list items
outside refs" as `file:line`; `measure_b.py --list` keys `para>100w`, `bullet>60w`.

**Kind.** hand (the worklist is scripted).

#### R-SENTENCE — long sentences, em-dash chains, nested parentheticals
*(report A F8; B's length rule folded in)*

**Applies when** a sentence exceeds 45 words, or contains two or more em-dash pairs, or a parenthetical
of 12 words or more, or a semicolon joining two separately cited facts.

**Do.**
1. Split at the semicolon or at the em-dash pair: the material inside the dashes becomes its own
   sentence.
2. A hedge that was mid-sentence becomes a following sentence beginning "We infer this because …" —
   **only if those are already the page's words**; otherwise move the hedge, unchanged, to the end of
   its own sentence.
3. Keep at most one em-dash pair or one parenthetical per sentence.
4. Put the subject and the verb in the first 12 words.
5. Markers travel with their clause.
6. Never split inside a quotation: split before it or after it.
7. A split may add a subject and a verb ("It is", "This is"). It may not add a clause ("This holds
   even though"): that states a relationship the original sentence did not, in different words. A
   hedge in parentheses that ends up alone at a split may be capitalised and closed as its own
   sentence — "(our extraction …)" → "(Our extraction ….)" — do nothing else to it.

**Example** — `docs/steps/066-bhi.md:16`.

Before:

```
It is made through the same resist windows as the arsenic tip of {ref}`ASTI <step-065>` — we
infer that the two share the {ref}`NTM <step-064>` resist, since the halo belongs to the same
transistors as the tip (see below) — but with a tilted beam, so that boron ions pass beneath
the edge of the polysilicon gate and land in the silicon *around* the tip, on the channel side
of it.
```

After:

```
It is made through the same resist windows as the arsenic tip of {ref}`ASTI <step-065>`, but
with a tilted beam, so that boron ions pass beneath the edge of the polysilicon gate and land
in the silicon *around* the tip, on the channel side of it. We infer that the two share the
{ref}`NTM <step-064>` resist, since the halo belongs to the same transistors as the tip
(see below).
```

**Do not touch.** Quotations; "we infer" (it is the page's hedge and must survive the move); the
`{ref}` roles and their link text.

**Find.** `python3 tmp/readability/a-tools/measure2.py`; `measure_b.py --list` key `sentence>45w`;
`grep -nE '—[^—]{0,200}—' docs/steps/*.md` for dash pairs.

**Kind.** hand.

#### R-LIST — enumerations written as sentences
*(report A F6)*

**Applies when** a sentence announces a count ("Two things can go wrong", "three reasons",
"first … second …"), or lists three or more parallel items of which at least one carries its own clause,
number or footnote marker.

**Do.**
1. End the announcing sentence with a colon. A marker at the end of the announcing sentence
   supports every item that follows: keep it there, on the lead-in, before the colon — never move
   it onto the last item only, which leaves the other items looking uncited.
2. One bullet per item, in the original order, with the item's own clause and marker.
3. Open each bullet with a bold label of 2–4 words taken from the item's own words, then an em dash.
   If the item already begins with the words the label would use, bold those words in place; do not
   repeat them as a separate label.
4. Keep the closing sentence ("Both are controlled by …") as prose after the list.
5. A list of four or fewer bare nouns stays inline.
6. Numbered lists are for sequences only (a recipe, an arithmetic derivation). Nest at most two levels.

**Example** — `docs/steps/013-ns19.md:69`.

Before:

```
Two things can go wrong: {term}`over-etching <over-etch>` the exposed field oxide (which
recesses it and creates divots at the active edge where the pad oxide meets the trench liner),
and leaving nitride residue (which blocks later oxidations locally). Both are controlled by the
acid's water content and temperature and by the pre-strip treatment.
```

After:

```
Two things can go wrong:

* **Field-oxide over-etch** — {term}`over-etching <over-etch>` the exposed field oxide recesses
  it and creates divots at the active edge, where the pad oxide meets the trench liner.
* **Nitride residue** — blocks later oxidations locally.

Both are controlled by the acid's water content and temperature and by the pre-strip treatment.
```

**Do not touch.** The `{term}` and `{ref}` roles, the markers, the closing sentence.

**Find.** `python3 tmp/readability/a-tools/measure4.py` ("inline-enumeration candidate sentences");
`grep -nE '\b(Two|Three|Four|Both) [a-z]+ (things|reasons|effects|mechanisms|constraints)' docs/steps/*.md`;
`measure_b.py --list` key `para>=3semicolons`.

**Kind.** hand.

#### R-H3 — no structure below H2; bold run-ins that are really headings
*(report A F2; report B B8 for mask pages)*

**Applies when** an H2 section holds more than 120 words before its first H3 or list, **or** a paragraph
starts with a bold run-in label that introduces a whole passage rather than one point
(`^\*\*[^*\n]{3,80}[.?:]\*\*`).

**Do.**
1. Keep at most two paragraphs and 120 words between the H2 and the first H3: what is done, what
   arrives, what leaves, where it sits in the module.
2. Move nothing between H2 sections. Everything stays in its own H2, in its own order; you are only
   adding H3 lines.
3. Use this vocabulary for new H3s on step pages: `### Key numbers`, `### What the public record shows`,
   `### How <quantity> is estimated`, `### Competing readings`.
4. A bold run-in that introduces a passage becomes an H3 with the same words, minus the trailing
   punctuation: `**How deep?**` → `### How deep?`. A bold run-in that labels a single paragraph
   (R-PARA step 3) stays bold.
5. H3 titles must be unique on the page (`myst_heading_anchors = 3` turns each into a slug) and must
   never be `Cross-check`, `High-level understanding`, `Deep dive`, or any mandatory heading of §2.9.
6. At most six H3s. An H3 is added only over a passage of ≥ 120 words with its own subject, and its
   title says what the passage shows. Do not use `What the public record shows` over era-typical or
   "working figure" text, and never directly after a sentence that the passage continues
   ("Precisely: …").

**Example** — `docs/steps/006-stie.md:30`.

Before: `**How deep?** No SkyWater document gives the SKY130 trench depth, and the PDK stack drawing does
not settle it. …`

After: a heading line `### How deep?`, a blank line, then `No SkyWater document gives the SKY130 trench
depth, and the PDK stack drawing does not settle it. …`

**Do not touch.** The 13 mandatory step headings; the H2/H3 template of machine, material and mask pages
(§2.9); the placement of `{dropdown}` blocks — a note stays directly after the paragraph it belongs to,
and an H3 is never inserted between them; the `{figure}` block and its position — it stays where
`gen_figures` put it, directly after the lead, and a new H3 goes after the figure's caption, never
between the lead and the figure.

**Where it is safe.** Step pages: yes — `check_steps.py` only tests that the 13 headings exist, and
`check_refs.py` reads only `### Deep dive`. Machine and material pages: yes **except** under
`At SkyWater` and `References`, where the H3 list is exact. Mask pages: **blocked until W0e** — any H3
under an H2 other than `Drawn layers and derivation`, `References` or `Plates and reticle sets` fails
`check_masks.py`.

**Find.** `grep -rnE '^\*\*[^*]{3,80}[.?:]\*\*' docs/steps/*.md | grep -v 'Related patents\|Related
papers\|Related filings'` — 184 hits, 146 of them the generated index-links block, so 38 real candidates on
step pages; the same grep on `docs/masks/*.md` finds 217 mask run-ins (report B8 counted 208). Section word counts come
from `measure.py`.

**Kind.** hand.

#### R-INTRO — page intros that are too long, and pointer sentences
*(report B B15)*

**Applies when** the text between the page title and the quick-facts table exceeds 70 words (machine,
material, mask pages), or a category page has no intro at all, or the intro contains the boilerplate
sentence "This page describes the class in general, lists …".

**Do.**
1. Keep the first sentences that say what the thing is and what it does in SKY130, up to 70 words.
2. Move every pointer sentence ("… is on the category page", "the tools that use most of these gases
   are …") into one `:::{seealso}` block directly under the quick-facts table, wording unchanged.
3. Delete **only** the sentence that lists the page's own sections ("This page describes the class in
   general, lists representative 200 mm-era models, and then says what SkyWater has published …"): it
   describes the template, carries no fact and no marker. If it carries a marker, keep it.
4. A category page with no intro gets a ≤ 60-word intro assembled from sentences already on the page
   (first paragraph of "What this class of step does"), with their markers.

**Example** — `docs/machines/wet-bench.md:4-16`: 12 lines of intro ending in "This page describes the
class in general, lists representative 200 mm-era models, and then says what SkyWater has published about
its own tools of this class and which SKY130 steps use them." Keep lines 4–11 (what a wet bench is and
what it runs); drop the template sentence; move nothing else.

**Do not touch.** Any sentence with a footnote marker, a number or a quotation.

**Find.** `awk` the text before the first `|` table line on each class page, or `measure_b.py --list`
key `para>100w`; `grep -rn "This page describes the class in general" docs/` (62 pages).

**Kind.** hand.

#### R-CATEGORY — "Step category" is one dense paragraph
*(report A F7)*

**Applies when** the `## Step category` section is a single paragraph of more than 35 words.

**Do.**
1. First paragraph, ≤ 35 words: the classification sentence, with its markers.
2. If **two or more** sentences remain and they describe this step, add `**Specific to this
   step:**` and one bullet per sentence. If one sentence remains, leave it as a second paragraph
   with no label and no bullet. A sentence that only lists other steps ("Similar etches occur
   later at …", "Later well implants …") is not "specific to this step": leave it as a paragraph
   after the bullets.
3. If a remaining sentence already begins "What is specific to … is that …", it is its own label:
   leave it as a paragraph and add nothing.
4. If a sentence here repeats a passage from another H2 on the same page, apply **R-REPEAT**: the fact
   keeps its home section and this section gets a pointer of ≤ 12 words.

**Example** — `docs/steps/138-capme.md:140`, a 276-word single paragraph that repeats the selectivity
argument of `:77-91` almost sentence for sentence. After: the classification sentence
("`CAPME` is an {ref}`Etch <category-etch>` step of the *refractory metal, fluorine-chemistry* class —
the category page's "Ti:W and TiN" entry."), then `**Specific to this step:**` and bullets; the repeated
selectivity sentences are replaced by a pointer to the section above, which keeps them and their markers.

**Do not touch.** The category `{ref}` link, the class name, any quotation.

**Find.** `measure.py` section stats ("Step category", median 104 words, max 276).

**Kind.** hand.

#### R-HEDGE — hedge placement and the scope note
*(report A F9)*

**Applies when** a `## How it is typically performed` section opens with a scope sentence matching
`industry-generic|industry-typical`, **or** a hedge sits in the middle of a sentence you are splitting
under R-PARA/R-SENTENCE.

**Do.**
1. Render the existing opening scope sentence, **word for word**, as an italic lead-in paragraph:
   `*An industry-generic recipe for a 200 mm, 130 nm-era fab:*`. Do not wrap it in an admonition —
   a note box renders as a 13 px callout holding one sentence that ends in a colon, cut off from
   the list the colon introduces, and it spends the page's admonition budget (§1). Italics is
   presentation only and keeps every word.
2. When splitting a sentence, move its hedge to the end of the sentence it qualifies. Four end tags are
   allowed — "(inference)", "(our reading)", "(our arithmetic)", "(industry-typical)" — and only when
   the existing hedge already means exactly that. Otherwise keep the hedge's own words.
3. Where a body "not public" has a matching bullet under `## Open questions`, the body keeps its hedge
   and may add "(see Open questions)". The reasoning is given once, in Open questions.
4. Never delete, weaken or strengthen a hedge. Never add a hedge to a sentence that had none.

**Example** — `docs/steps/006-stie.md:101`: `An industry-generic recipe for a 200 mm, 130 nm-era fab:`
becomes

```
*An industry-generic recipe for a 200 mm, 130 nm-era fab:*
```

immediately before the numbered list, which is unchanged. (`docs/steps/013-ns19.md:77` is the same
sentence with "nitride strip" in place of "recipe"; 166 of the 171 step pages contain the phrase.)

**Do not touch.** The sentence's wording, including the colon. The list that follows.

**Find.** `grep -rn "industry-generic\|industry-typical" docs/steps/*.md`;
`grep -rn "we infer\|our reading\|our arithmetic\|our extraction\|not public" docs/steps/*.md`.
Verify every hit got the treatment: `grep -n 'industry-generic\|industry-typical'` on the page;
every scope sentence under `## How it is typically performed` has the italic lead-in (§7 step 8).

**Kind.** step 1 scripted (the paragraph between the H2 and the first list item), steps 2–4 hand.

#### R-REPEAT — the same sentence twice
*(report A F10)*

**Applies when** a run of ten or more words appears twice on the page, in two different H2 sections.

**Do.**
1. Decide the home section from this map: suppliers → `## Resources required`; tool quotations →
   `## Machines likely used at SkyWater`; unknowns → `## Open questions`; numbers → the
   `### Key numbers` table; classification → `## Step category`.
2. The home copy keeps the full sentence and its markers.
3. The other copy becomes a pointer of ≤ 12 words ("the suppliers are named under Resources required").
4. **Before deleting anything, check that each footnote label in the deleted text still occurs elsewhere
   on the page.** `check_refs.py` fails on an unreferenced definition, and so does the `-W` build.
5. Cross-page boilerplate (the gas-supplier sentence on 18 pages, the litho-track sentence on 13) stays
   on every page. Do not deduplicate across pages.

**Example** — `docs/steps/097-ti-tin1.md:173` and `:180`: the Honeywell/JX Metals supplier sentence
appears under `## Machines likely used at SkyWater` and again under `## Resources required`, eight lines
apart, with `[^sec-01][^sec-02]` both times. Home: `## Resources required`. The Machines bullet keeps its
grading sentence and points: "**Sputter targets.** Suppliers are named under Resources
required.[^sec-01][^sec-02]" — the markers stay, because the bullet still makes the claim.

**Do not touch.** The markers. If removing the duplicate would leave a definition unreferenced, keep the
duplicate.

**Find.** `python3 tmp/readability/a-tools/measure3.py` (10-word shingles repeated across sections).

**Kind.** hand. This is the riskiest rule in the guide: it is the only one that deletes words. A reviewer
checks every R-REPEAT edit.

#### R-GLANCE — the summary box at the top of a step page
*(report A F11)*

**Applies when** a step page has no "At a glance" box. Written **last**, from the finished page.

**Do.**
1. Insert between the quick-facts table and `## What this step is`:

```
:::{admonition} At a glance
:class: at-a-glance

* **Does:** one line.[^x]
* **Why:** one line.
* **Public numbers:** one to three SKY130 values with their markers, or "none published for
  SKY130".
* **Likely SkyWater tool:** name — existence strong / assignment inference.[^skw-01]
* **Not public:** the one or two biggest unknowns (→ Open questions).
:::
```

   The `:class: at-a-glance` line is required: it is what lets the theme give the box's text the
   same size as body text instead of furo's default 13 px admonition size (W0a).
2. Four to six bullets, each ≤ 25 words, each condensing a sentence that is already on the page, with
   that sentence's marker and its hedge tag.
3. **Public numbers:** SKY130 values only — the PDK, a SkyWater statement, or the published test
   tile — with their marker. If there are none, write "none published for SKY130" and stop there;
   never file a generic, era-typical or textbook figure under this label. Such a value may appear
   elsewhere in the box, but only with the page's own qualifier ("typical", "era-typical",
   "Wikipedia's standard") and marker, never presented as a SKY130 number.
4. **Likely SkyWater tool:** a tool named in `## Machines likely used at SkyWater`, with its grades,
   or "none assignable". Never a supplier or a material — if the page's only graded item there is a
   supplier, write "none assignable" rather than naming it here.
5. Markers are required on every number and on the tool line. The Does and Why lines condense the
   lead and need none. Every qualifier in the source sentence ("part of", "typical", "standard",
   "our reading") must survive the condensing unchanged.
6. No new fact, no new number, no new source. Every marker in the box must occur again below it.
7. Nothing from an in-force note: no patent number, no title, no value that only the collapsed note
   gives (§2.6).
8. Make the first sentence of `## What this step is` ≤ 25 words: "`CODE` <verb> <object>".

**Example** — for `docs/steps/006-stie.md` the box is built from `:15` ("the plasma etch that cuts the
isolation trenches into the silicon"), `:30-44` (the depth reading, "about 0.33 µm … our reading, not a
documented fact"[^pdk-04]) and `:269` ("**Trench depth.** No SkyWater document states it …").

**Do not touch.** Everything below it. The box is additive.

**Find.** `grep -L "At a glance" docs/steps/*.md`.

**Kind.** hand, last, then re-read against the page.

#### R-TOOLS — evidence grading buried in run-on bullets
*(report A F4)*

**Applies when** a bullet under `## Machines likely used at SkyWater` names a *machine or tool
family* and contains "Strength:". A bullet about a material, a supplier or a wafer keeps its
original form and is left out of the recap table.

**Do.**
1. Keep the tool name as the bullet's bold head.
2. Three sub-bullets, with the original words moved unchanged under the matching label:
   * `*SkyWater says:*` holds **only** statements SkyWater made: the capability list, a filing, a
     job posting. Drop the leading subject and write it verb-first: `*SkyWater says:* lists "Lam
     4400, …"`, never "it lists it". A statement from any other source (Cypress, Stanford, a
     vendor, a used-equipment listing) stays as a plain continuation paragraph under the
     sub-bullets, in its original words.
   * `*Tool exists:*` — the grading of existence, and its reason only.
   * `*Runs this step:*` — the grading of the assignment to this step, and its reason only. Any
     other sentence stays in the continuation paragraph.
3. Omit the third sub-bullet when the page grades only existence.
4. Do not normalise the grades: "strong", "**strong**", "medium", "weak", "inference" stay as the page
   writes them.
5. With four or more tools, add a recap table above the list: `Tool | Evidence`, two columns only. Do
   not put the quotations in the table; they overflow a phone.

**Example** — `docs/steps/013-ns19.md:120`.

Before:

```
* **Akrion Gamma batch wet bench (phosphoric).** SkyWater lists it
  with "phosphoric" among its chemistries.[^skw-01] Strength: strong
  (SkyWater statement) that a hot-phosphoric capable bench exists; the
  assignment to `NS19` follows from it being the only phosphoric tank
  listed.
```

After:

```
* **Akrion Gamma batch wet bench (phosphoric)**
  - *SkyWater says:* lists the bench with "phosphoric" among its chemistries.[^skw-01]
  - *Tool exists:* strong (SkyWater statement).
  - *Runs this step:* the assignment to `NS19` follows from it being the only phosphoric
    tank listed.
```

**Do not touch.** The tool names, the quotations, the markers, the grade words.

**Find.** `grep -rn "Strength:" docs/steps/*.md` (396 uses on all 171 pages).

**Kind.** scripted split at "Strength:", then hand assignment of the clauses.

#### R-OPENQ — Open-questions bullets without a label
*(report A F15)*

**Applies when** a bullet under `## Open questions` does not start with `* **`.

**Do.**
1. Add a bold label of 2–5 words naming the unknown, taken from the bullet's own words, then a full
   stop, then the existing text unchanged.
2. A bullet over 60 words that is mostly numbers moves its numbers into a table under
   `### What the public record shows` (R-TABLE) and keeps here the question, the hedge and a pointer.
3. In-force notes stay last in the section, in place.

**Example** — `docs/steps/002-box.md:250`.

Before: `* The actual SKY130 pad-oxide thickness, ambient and temperature are not public; 10–20 nm and
~900 °C dry are era-typical figures taken from the patents and textbooks cited.`

After: `* **Pad-oxide thickness and ambient.** The actual SKY130 pad-oxide thickness, ambient and
temperature are not public; 10–20 nm and ~900 °C dry are era-typical figures taken from the patents and
textbooks cited.`

(`docs/steps/006-stie.md:269` is already in the target form and needs no edit.)

**Do not touch.** The question itself, the hedge, "not public", the numbers, the markers.

**Find.**

```
awk '/^## Open questions/{f=1} /^<!-- footnotes/{f=0} f && /^\* [^*]/ {print FILENAME":"FNR": "$0}' \
    docs/steps/*.md
```

647 bullets on this branch.

**Kind.** hand.

#### R-RELATED — related-links sections
*(report A F15, report B B12)*

**Applies when** `## Related steps and cross-references` (step pages) or `## Related pages` (class
pages) is an unordered run of sentence-bullets.

**Do.**
1. Step pages: labels, in this order: `Previous:` · `Next:` · `Same module:` (only steps whose
   Phase cell in `docs/steps/index.md` names the same module) · `Depends on:` · `Feeds:` ·
   `Same category:` (steps of the same kind elsewhere in the flow) · `Mask:` (mask page,
   previous/next mask) · `Evidence:` (e.g. a die-shot) · `Category page:`. Keep every gloss and
   link. Never split one bullet's links over two labels unless the bullet already names two
   relationships.
2. Class pages: group under bold labels — Category · Machines · Materials · Masks · Indexes — and keep
   each gloss to ≤ 12 words. Six or more mask links with one shared gloss become a single line.
3. Drop no link, add no link, change no link text.

**Example** — `docs/machines/duv-krf-stepper.md:333-352`: seven bullets beginning "per-mask pages
for …". After: a `**Masks.**` line holding the mask links, a `**Indexes.**` line holding
`{ref}`masks-index``, and so on; the gloss of each group is the shortest of the existing glosses.

**Do not touch.** Any `{ref}` target or link text. On step pages, "Category page:" stays (166 pages have
it; it is the last bullet).

**Find.** `sed -n '/^## Related pages/,/^## /p'` per page; `measure_b.py --list` key `bullet>60w`.

**Kind.** hand.

#### R-CODE — code formatting of identifiers
*(report A F15; scope narrowed, see below)*

**Applies when** an identifier that the **same page** already writes in backticks (a GDS layer name, a
model parameter, a file name, a step code) also appears bare in body prose, outside a quotation.

**Do.**
1. Add backticks to that occurrence only.
2. Never inside a quotation. Never in a heading, a link text, a footnote definition or a table header.
3. Never to a design-rule identifier (`poly.1a`, `difftap.10`, `dnwell.6`): the whole site writes those
   bare, in tables and prose alike, and changing some of them would make the site inconsistent.
4. Never to an English word that happens to be a layer name ("diffusion surface", "the overlay tool",
   "the ash", "the reticle", "a via").

**Example — what not to touch.** `docs/steps/022-hvtpm.md:55` contains bare `lvtn` and `hvtp` inside a
quoted PDK rule: "min. enclosure of ((LVnwell not overlapping Var_channel) NOT lvtn) by …". It stays
exactly as it is (rule 2, and §2.1).

**Measured on this branch:** a scan of all 171 step pages and 36 mask pages for identifiers written both
ways on one page returned only quotations and ordinary English words. Treat R-CODE as a check, not as a
work item: if you find no candidate, that is the expected result.

**Find.**

```
grep -rnE '[^`A-Za-z](toxe|metal_stack\.svg|masks\.csv|gds_layers\.csv)[^`A-Za-z]' docs/steps | grep -v '^\S*:[0-9]*: *\[\^'
```

(or the Python scan in §7). Report A's other half of this finding — putting drawing labels such as `0.0`
at `docs/steps/006-stie.md:32` into quotation marks instead of backticks — is **not** an executor rule:
it changes quoting, which §2.1 forbids. Owner decision; left out.

**Kind.** hand, opportunistic.

### 3.2 Tables, data and derivations

Read §2.4 (never fill a cell from memory) and the column budget in §1 before any of these.

#### R-TABLE — numeric data written as prose or bullets
*(report A F3; report B §2 supplies the column budget)*

**Applies when** a paragraph or bullet holds **three or more parallel items that each carry two or more
attributes** — a source and a value, a rule and a number, a layer and a thickness. Mechanical proxies:
five or more unit-bearing numbers plus two or more semicolons in one block; three or more design-rule
identifiers in one block.

**Do.**
1. Choose the columns from the kind of block:

   | Kind | Columns |
   |---|---|
   | Published recipes from other fabs | Source · Species · Energy · Dose · Note |
   | Film stacks | Report (year, technology) · Stack as quoted · Total |
   | Design rules | Rule · Constrains · Value |
   | Measured against nominal | Parameter · Geometry · Test tile · PDK nominal · Limits |
   | Generic recipe parameters | Parameter · Typical · Public for SKY130? |

2. One row per item, in the original order.
3. Every row keeps its footnote marker, in the first or the last cell. A marker at the end of an
   enumerating sentence that becomes the table supports every row: keep it in the table's first
   header cell (`Layer[^pdk-06]`) or the lead-in sentence before the colon, not on the last row only.
4. Units go in the header (`Energy (keV)`). Per-cell units only where the source itself is
   inconsistent, and then say so in the caption (R-CAPTION).
5. A hedge that covers the whole table goes, word for word, in one sentence directly under it. A hedge
   that covers one row goes in a final `Basis` column.
6. Quoted values stay quoted, inside the cell. A value the page does not give is `—`.
7. Numbers, step numbers and years are right-aligned (`---:`); everything else left; never centred.
8. The sentence that draws the conclusion stays as prose after the table.
9. A row whose only source is a patent shown as in force belongs **inside that patent's dropdown**, in a
   table of its own (§2.5, §2.6).
10. Obey the column budget of §1: ≤ 3 columns if any column holds prose, ≤ 5 if every cell is a
    number, a code or ≤ 3 words. Beyond the count, the table must pass the phone test: no
    horizontal scroll at 400 px, and no number broken across lines. A column whose value is the
    same in every row is not a column: put it in the lead-in sentence. If the table still fails
    (too many columns, or a column-count table that fails the phone test anyway), transpose it:
    conditions (currents, extents) across the columns, quantities (gain, V_BE, measured, nominal)
    down the rows.

**Example** — `docs/steps/018-nwi.md:94`.

Before:

```
* **Energy.** Set by the wanted peak depth. Published retrograde N-wells
  of the 0.25–0.13 µm era: 500, 275 and 130 keV phosphorus in a Harris
  twin-well flow;[^pat-twin-harris] 700 keV at 2.0 × 10¹³ cm⁻² plus
  120 keV at 2.0 × 10¹² cm⁻² in a Hynix flow;[^pat-well-hynix] 850 keV
  at 5.2 × 10¹³ cm⁻², 550 keV at 1.25 × 10¹² cm⁻² and 50 keV at 5 ×
  10¹¹ cm⁻² at IBM;[^pat-well-ibm] …
```

After:

```
* **Energy.** Set by the wanted peak depth. Published retrograde N-wells of the
  0.25–0.13 µm era:

  | Source | Energy (keV) | Dose (cm⁻²) |
  |---|---:|---:|
  | Harris twin-well[^pat-twin-harris] | 500, 275, 130 | — |
  | Hynix[^pat-well-hynix] | 700 + 120 | 2.0 × 10¹³ + 2.0 × 10¹² |
  | IBM[^pat-well-ibm] | 850 / 550 / 50 | 5.2 × 10¹³ / 1.25 × 10¹² / 5 × 10¹¹ |

  For a 1.1 µm well depth[^pdk-03] the deepest `NWI` energy is plausibly
  500 keV–1 MeV (inference from range tables).[^txt-01]
```

(The Harris row has no published dose, so its cell is `—`, not a number from memory.)

A second worked case: `docs/steps/061-p1m.md:30-38` recites six poly rules in one paragraph
("the minimum poly width (poly.1a) is 0.150 µm and the minimum poly-to-poly spacing (poly.2) is
0.210 µm;[^pdk-periph] … 0.130 µm (poly.8, the endcap) … 0.250 µm (poly.7 …) … 0.075 µm (poly.4) …
0.330 µm (poly.3)"). That becomes a three-column `Rule | Constrains | Value` table with one marker per
row, and the closing sentence about the drawn gate length stays as prose.

**Do not touch.** Significant figures, thousands spacing ("1 800 Å"), "about", "~", the order of the
items, the markers, the rule identifiers (bare, per R-CODE step 3).

**Find.** `python3 tmp/readability/a-tools/measure3.py` (table candidates: blocks with ≥ 5 unit-bearing
numbers and ≥ 2 semicolons) and `measure4.py` (blocks citing ≥ 3 design-rule ids).

**Kind.** hand, from the templates above.

#### R-DERIVATION — arithmetic buried in prose
*(report A F5)*

**Applies when** a passage writes out at least one arithmetic operation (`−`, `+`, `×`, `÷`, `=`) and
either performs two or more of them or takes two or more inputs to reach a number; or contains "our
arithmetic", an inline `=` chain or "≈" with an operation shown. Not when the page only names its
inputs and states a result with no operation shown, even if it also says "our extraction" or takes
"two or more inputs" in prose — that is a reading or a model inversion, not a derivation, and
forcing it into this template invents working the page never showed (see 001-smat.md's
body-doping estimate, where "step 1" had no operation at all). A derivation in `## Open questions`
is never moved out of that H2 (see R-PARA step 4 instead: it stays there as sub-bullets, one per
indirect figure).

**Do.**
1. Give it an H3: `### How <the quantity> is estimated`.
2. Input table first: one row per input, each with its own footnote marker and the source's own wording
   for the quantity.
3. Numbered list: **one operation per line**, the arithmetic written out, the result of that line in
   bold. A reason line (a line with no operation, only a comparison or a judgement, such as the
   trench-depth example's step 3) uses the page's own comparison, word for word where possible —
   never a new comparison the page did not make.
4. A bold result line.
5. Then every hedge the original carried, word for word, in the original order.
6. A single-operation estimate stays inline as its own sentence — no table.
7. If the same derivation appears twice on the page, work it once; the second place keeps the result,
   the hedge, the marker and "(derived above)".
8. **Check the arithmetic as you copy it. If it does not come out, copy it exactly as written and put a
   line in your progress file.** Never correct a number.

**Example** — `docs/steps/006-stie.md:30-44`, where one sentence holds two subtractions, the
conclusion, and a judgement about `FOXSTEP`.

After:

```
### How the trench depth is estimated

| Quantity (PDK stack drawing[^pdk-04]) | Value (µm) |
|---|---:|
| `li` bottom | 0.9361 |
| `licon` over `diffusion` | 0.6099 |
| `licon` over `field poly` | 0.4299 |
| `field poly` thickness | 0.18 |

1. Diffusion surface: 0.9361 − 0.6099 = **0.3262 µm**.
2. Field-oxide top: 0.9361 − 0.4299 − 0.18 = **0.3262 µm**.
3. The two are equal, so the drawing shows no field-oxide step, and the 0.07 µm `FOXSTEP`
   of the assumptions table[^pdk-03] cannot be combined with it to derive a trench depth.

Result: about 0.33 µm **only if** the drawing's zero is the trench floor. That is our reading,
not a documented fact, and the drawing says "Diagram not to scale!".[^pdk-04]
```

**Do not touch.** Any number. Any hedge. The markers on the inputs.

**Find.** `grep -rn "our arithmetic\|our extraction\|≈\| = [0-9]" docs/steps/*.md` (56 "our arithmetic"
uses on 42 pages).

**Kind.** hand.

#### R-MODELS — "Representative models / materials and grades" as vendor paragraphs
*(report B B4)*

**Applies when** the `## Representative 200 mm-era models` (machine pages) or
`## Representative materials and grades` (material pages) section contains no line starting with `| `.

**Do.**
1. One row per model or grade. Machine pages: `Vendor | Model | Year | Type | Published figures`.
   Material pages: `Material | As supplied | Specification | Note`.
2. Quotation marks and footnote markers travel with the value into the cell.
3. A value the page does not give is `—`.
4. Sentences that fit no column — litigation, "still used in 2014", "no vendor description was
   retrieved" — stay as a short paragraph under the table, unchanged.
5. Wrap the table per R-CAPTION.

**Example** — `docs/machines/duv-krf-stepper.md:144`.

Before:

```
* **ASML.** Its first KrF stepper, the PAS 5000/70 of 1991, had NA
  0.42;[^kato-2007] its first step-and-scan tool, the PAS 5500/500 of 1997,
  had "a resolution of 0.22µm, with 96wph throughput
  (200mm)".[^kato-2007] The PAS 5500/350C is "a Deep UV stepper for
  0.15-µm applications and beyond".[^asml-pas5500-350c] …
```

After:

```
:::{table} Representative KrF exposure tools of the 200 mm era (figures as each source gives them)
:widths: 12 20 8 12 48

| Vendor | Model | Year | Type | Published figures |
|---|---|---:|---|---|
| ASML | PAS 5000/70 | 1991 | stepper | NA 0.42[^kato-2007] |
| ASML | PAS 5500/500 | 1997 | scanner | "a resolution of 0.22µm, with 96wph throughput (200mm)"[^kato-2007] |
| ASML | PAS 5500/350C | — | stepper | "a Deep UV stepper for 0.15-µm applications and beyond"[^asml-pas5500-350c] |
:::
```

**Do not touch.** The vendor names, the model designations, the quotations, the markers. Do not add a
year the page does not give.

**Find.** per class page, `sed -n '/^## Representative/,/^## /p' FILE | grep -c '^| '` → 0 means the
rule applies (42 of 42 class pages today).

**Kind.** hand. Not scriptable: deciding which clause is a "published figure" is judgement.

#### R-ENTRIES — "read term by term" paragraphs
*(report B B6)*

**Applies when** a paragraph glosses the entries of a quoted list in turn, one after another, usually
separated by semicolons; often signalled by the words "term by term" or "The mask-type record".

**Do.**
1. One row per quoted entry: `Entry as listed | What it names | Status`.
2. `Entry as listed` is the quotation, unchanged, in quotation marks.
3. `Status` is **the page's own hedge**: "SkyWater statement", "our reading", "our inference",
   "not stated". Never invent one, never upgrade one.
4. Sentences about the list as a whole stay as prose above or below the table.
5. Two-column material (term → explanation) may use a definition list instead (§6).

**Example** — `docs/machines/duv-krf-stepper.md:191`: "Read term by term: "DUV" names no wavelength; the
step pages read "ASML DUV stepper" and "ASML DUV scanner" as 248 nm (KrF) tools, as the machines index
records, and that the list gives the two 193 nm scanners as separate entries is consistent with that …".
After: a table whose first row is `"DUV" | names no wavelength | not stated` and whose second is
`"ASML DUV stepper", "ASML DUV scanner" | read as 248 nm (KrF) tools | our reading (machines index)`,
with the markers in the cells and the concluding sentence left as prose.

**Do not touch.** The quotations, the order of the entries, the markers, the hedge words.

**Find.** `grep -rln "term by term" docs/` (34 pages); `measure_b.py --list` key `para>=3semicolons`
(129 paragraphs on 65 pages).

**Kind.** hand.

#### R-QUICKFACTS — quick-facts cells that are not quick
*(report B B5)*

**Applies when** a quick-facts cell exceeds 20 words or holds more than one quotation.

**Do.**
1. Value first, in the page's own words. At most one quotation. Then the markers. Then, if needed, a
   pointer: "see *Excimer laser source*".
2. **Before deleting anything from a cell, find the same words in the body.** If they are not there,
   move them into the right section *with their markers and quotation marks first*, in a separate step,
   and only then shorten the cell.
3. Keep every row label. Keep the row order.
4. **Mask pages:** do not touch the cells the checker compares with the index — `Mask step`,
   `PDK mask (`masks.csv`)`, `Mask-level layer (`gds_layers.csv`)`, `Drawn layer (`gds_layers.csv`)`,
   `Minimum CD, feature / space`, `Mask type (process-steps sheet)`, `Plates recorded`, `Plate no.`,
   `Dies with shapes, MPW-1 to MPW-8 (renders)`, `Steps that use the pattern`. That is every row except
   `Polarity and tone` and `Exposure class`, which must stay non-empty and keep its machine link.
   In practice: **mask quick facts are already the model; leave them alone.**
5. **Material pages:** the summary table must still start with `What they do` and end with
   `SkyWater evidence` then `SKY130 steps`, and the last cell must still read "N steps; see …" with N
   equal to the number of step links in the steps paragraph.
6. **Step pages:** the quick-facts table has no checker, but `Step number`, `Step code`, `Category`,
   `Phase`, `Previous step` and `Next step` are the site's navigation. Do not reword them.

**Example** — `docs/machines/duv-krf-stepper.md:22`, the `Light source` cell: 38 words and six
quotations. The /350C figures ("Type: Cymer 5610", "Power: 10 W", "Frequency: 1 kHz") appear **only**
here, so they move into `### Excimer laser source` (`docs/machines/duv-krf-stepper.md:42`) with
`[^asml-pas5500-350c]`; the cell then reads: `A KrF excimer laser, "Type: Cymer ELS6600, Gigaphoton
KES-G2OK", 20 W, up to 2 kHz on the PAS 5500/750F;[^asml-pas5500-750f] see *Excimer laser source*.`

**Do not touch.** Row labels; any cell listed in step 4; numbers; quotation marks.

**Find.** `measure_b.py --list` key `tablecell>40w` (97 cells on 42 pages).

**Kind.** hand. Never scripted.

#### R-PARAMS — number-dense paragraphs beside a table
*(report B B14)*

**Applies when** a paragraph names four or more identified parameters with values ("Table 2 gives …
`FOMCD` 0.14 …; Table 7 gives … 0.135 (`FOMSE`) …"), next to an existing table.

**Do.**
1. Second table: `Parameter | PDK table | Published description | Value`.
2. One row per parameter, values and identifiers exactly as written.
3. The interpretation ("the PDK does not reconcile these with the 0.150 µm of difftap.1", "our
   reading") stays as prose after the table, unchanged.
4. Do not merge it into the existing design-rule table: that one is quoted rule text, this one is
   parameters.

**Example** — `docs/masks/fom.md:331` ("Table 2 of *Criteria & Assumptions* gives the minimum feature
and space as `FOMCD` 0.14 and `FOMCDSP` 0.27, and Table 7 gives a "MOSFET width" of 0.135 (`FOMSE`) and a
"MOSFET width in standard cells" of 0.075 (`FOMSESC`);[^pdk-03] the PDK does not reconcile these …").
All 36 mask pages have a paragraph of this shape.

**Do not touch.** The sentence beginning "the PDK does not reconcile …"; the unit caveat (it belongs in
the caption, R-CAPTION, *and* stays in the prose if that is where the page put it).

**Find.** `grep -rn "Table [0-9] gives\|Table [0-9] of" docs/masks/*.md`.

**Kind.** hand.

#### R-COMPARE — category-page comparisons and consumables
*(report B B7)*

**Applies when** a category page has three or more bullets of the shape *thing (steps): values;
explanation*, or a "Typical consumables" list whose lead-ins name materials but link nowhere.

**Do.**
1. Comparison bullets become `Material | SKY130 steps | Typical chemistry | Why`. An explanation over
   40 words stays as prose below the table, under the same name.
2. Each consumables lead-in becomes a link to its material page. Map the name through the class-page
   table of `docs/materials/index.md` (`## How to read the index`, the `Consumable class | Page` table);
   if the name is not in that table, leave it unlinked.
3. Add a `Machine class` column to the category's steps table, taken from the machines index.
4. Add no material that the page does not already name.

**Example** — `docs/categories/etch.md:91`: `* **Silicon and polysilicon** (STI trench {ref}`STIE
<step-006>`, gate {ref}`P1ME <step-062>`): HBr/Cl₂ with a little O₂, which forms …` — seven bullets of
this shape become one table with the columns above. `docs/categories/etch.md:219`
(`* **Fluorine sources**: CF₄, CHF₃, C₄F₈, C₂F₆, SF₆, NF₃ (chamber clean).`) keeps its text and gains a
link on the lead-in to the etch-gases material page. `docs/categories/cmp.md:134` (`Polish | Film removed | Stop | Slurry | Failure modes`) is the model to copy.

**Do not touch.** The chemistry, the step links, the order.

**Find.** `grep -rn "^\* \*\*[^*]*\*\* (\|^\* \*\*[^*]*\*\*:" docs/categories/*.md`.

**Kind.** the table is hand work; the consumables links and the machine-class column are scripted.

#### R-CAPTION — every table says what it is
*(report B B13)*

**Applies when** a table is not the page's quick-facts table and has no caption. (185 tables on the 92
class pages today; 0 captions.) **On step pages**, the lead-in sentence ending in a colon that
introduces the table (as R-TABLE and R-DERIVATION already require) *is* the caption; do not also
wrap the table in `:::{table}` unless it has a prose column and needs `:widths:` set (the "measured
against nominal" and multi-quotation tables usually do; a short numeric table usually does not). §4.1
lists R-CAPTION for step pages for this reason, even though the class-page count above is what
motivated the rule.

**Do.**
1. Wrap it:

```
:::{table} What the rows are, from which source; unit note if the units are uneven
:widths: 12 20 8 12 48

| … |
:::
```

2. The caption says three things: what one row is, where the values come from, and any unit caveat
   ("values in µm where the PDK gives a unit; blank units are blank in the PDK").
3. `:widths:` is required on any table with a prose column; the numbers are relative.
4. The pipe table inside stays exactly as it was — same rows, same cells, same order (§5).
5. Never `{numref}`, and do not refer to tables by number in prose.

**Example** — `docs/masks/fom.md:310`, the rule table `| Rule | Description (published wording, abridged
where marked "[…]") | Value |`, gets
`:::{table} Periphery design rules naming `diff` and `tap`, as published; the unit column of difftap.4
and difftap.5 is blank in the PDK[^pdk-periph]` and `:widths: 14 62 24`.

**Do not touch.** Cell contents, column order, row order.

**Find.** `grep -rn "^| " docs/{machines,materials,masks,categories}/*.md | grep -v "|---"` and check
which tables have no `:::{table}` line above them.

**Kind.** hand (one line per table); safe to do in the same commit as the table rule that created it.

### 3.3 Links, references and navigation

#### R-LINKS — reading-list heads and named titles become links
*(reports A F14, B B10 and C C1/C4, merged — one rule)*

**Blocked until W0c** (citation-style rule 5 reworded, the `check_refs.py` invariant added, the script
promoted to `tools/fix_reading_list_links.py`). Do not start it by hand before then.

**Applies when** a bullet under `## References` ends in exactly one footnote marker and contains no
link, **or** prose names a source by its italic title in the same sentence as that source's marker.

**Do.**
1. **Reading-list bullets.** The *head* is the text before the first ` — `, or — a bullet with no
   annotation at all — everything before the trailing marker run, minus its final `.`:
   * head contains no `{role}`, no `[`, no backtick → wrap the whole head: `[head](<URL>)`;
   * head contains a role or a backtick but exactly one `*italic title*` → link only that span;
   * N markers and exactly N italic titles in the same order → link title *i* to marker *i*'s URL;
   * multi-marker, that exact count fails, but exactly one marker's own definition names a given
     italic title (any italic span in its body, whitespace-normalised) → link that title only, and
     only when no two titles would claim the same marker; a title or marker left over stays plain;
   * anything else → leave the bullet alone.
   Every one of these applies the same way whether or not the bullet has a dash.
2. The URL is **the first `<URL>` in that page's own `[^k]: …` definition**, copied character for
   character. Where the definition gives an archive URL first (R-WAYBACK), that is the URL you copy.
3. Angle brackets around the URL are mandatory: `[head](<https://…>)`. They keep URLs containing
   parentheses valid.
4. **The marker always stays**, at the end of the bullet, unchanged. It carries the inventory key.
5. **Named titles in prose** (C4): link the italic title to the definition's first URL, **first
   occurrence per H2 only**, marker unchanged.
6. Leave alone: vendor model names in "Representative …" and "Machines typically used" sections (the
   footnote is the evidence); short "name + marker" bullets outside the reading lists (22 site-wide);
   the generated index pages (already inline).
7. Bullets inside a `{dropdown}` may be converted, **in place** (§2.5).
8. Rules 1/1b wrap the *whole* head, including the publisher ("**Wikipedia, Shallow trench
   isolation**"); rules 3/3b/3c wrap only the title, leaving the publisher plain ("Wikipedia,
   **Silane**, **Tetraethyl orthosilicate** …"). This is deliberate, not an inconsistency to fix: a
   single-source head has nothing else to point the link at, and a multi-source head must not point
   two different sources' worth of text at one URL.

**Example** — `docs/steps/006-stie.md:215`.

Before:

```
* Wikipedia, *Shallow trench isolation* — the three STI operations and
  the LOCOS cross-over node.[^wiki-sti]
```

After:

```
* [Wikipedia, *Shallow trench isolation*](<https://en.wikipedia.org/wiki/Shallow_trench_isolation>) — the
  three STI operations and the LOCOS cross-over node.[^wiki-sti]
```

The three-marker case is `docs/machines/pecvd.md:468` ("Wikipedia, *Silane*, *Tetraethyl orthosilicate*
and *Nitrogen trifluoride* — the precursors and the clean gas.[^wiki-silane][^wiki-teos][^wiki-nf3]"):
three italic titles, three markers, in the same order, each title linked to its own marker's URL.

**Do not touch.** Footnote definitions; the annotation after the dash; **the number of bullets**
(`check_refs.py` counts `^\* ` under `### Deep dive`); the generated index-links block. Never invent a
URL, and never use a URL that is not in one of that page's own definitions (§2.11).

**Find.** The dry run, from the repository root — it prints, it never writes:

```
python3 docs/plans/readability/prototypes/links-theme/titlelink_dryrun.py              # site totals
python3 docs/plans/readability/prototypes/links-theme/titlelink_dryrun.py docs/steps/006-stie.md
```

On this branch: `{'ok': 6200, 'multi-marker': 676, 'no-dash': 176, 'role-in-head': 16, 'no-url': 6}`.
The 6,200 are the script's; the ≈ 870 leftovers are hand work under steps 1b and 1c.

**Kind.** scripted for the 6,200 (once W0c lands: `tools/fix_reading_list_links.py`); hand for the rest.
After running it: `check_refs.py`, `check_inforce.py`, `gen_index_links.py --check`, `-W` build.

#### R-WAYBACK — a cited page that no longer resolves
*(report C C5)*

**Blocked until W0f** for the tooling half (`check_links.py` lookup fix, `--suggest-archive`,
`--include-generated`). The citation *form* below applies from now on.

**Applies when** `check_links.py` reports a URL dead in two runs at least 24 h apart (404, 410, DNS
failure, 5xx or timeout) and the host is not in its `BLOCKED_HOSTS`. A single failure is not "dead".

**Do.**
1. **Find a snapshot.** Query the availability API with the citation's accessed/retrieved date as the
   timestamp (else `20260830`), `User-Agent: sky130-process-tech docs checker`, one request per 3 s.
   Accept only `available: true` and `status: "200"`. On an empty answer: retry once after 10 s, then
   the other scheme, then with and without `www.`, then the CDX endpoint. Never loop on an error page.
2. **Verify it.** Fetch the snapshot once and confirm the title, or a string the pages quote from it, is
   present. A captured soft-404 or a redirect counts as no snapshot.
3. **Cite both URLs**, in every footnote definition that repeats it *and* in the inventory entry:

```
[^key]: Author, *Title*, publisher, date.
    <https://web.archive.org/web/20260411150120/https://example.com/page>
    (Wayback Machine capture of 2026-04-11; original, dead since 2026-09-19:
    `https://example.com/page`).
```

   The archive URL comes **first** — R-LINKS and the hover card take the first URL. Always `https://`,
   even where an older definition on the page writes `http://web.archive.org/…`. The original goes in
   backticks: searchable, but not a link, so the checker stops reporting it. Use exactly the house
   wording "Wayback Machine capture of YYYY-MM-DD" (87 inventory entries already use it).
4. **No snapshot anywhere** (try `archive.ph/newest/` by hand as well): rule 11 of
   `docs/plans/agent-briefs.md` applies, unchanged — and that rule *deletes quotations*, so never reach
   it on a lookup that merely failed intermittently.
5. A DOI whose landing page is broken keeps the DOI plus a dated note. **Never replace a DOI with an
   archive URL.**

**Do not touch.** The bibliographic text of the definition; any quotation resting on the source; hosts
that block scripts.

**Find.** `uv run tools/check_links.py` (and, after W0f, `--suggest-archive`). The existing report is
`docs/plans/link-check-2026-09.md`; note its THUNG-2016 row says "no snapshot" and is wrong.

**Kind.** hand, one source at a time, with the fetch etiquette of `agent-briefs.md` rules 10 and 12.

#### R-STEPRUN — runs of step links, and link text that is a bare number
*(report B B1 and B9)*

**Applies when** a paragraph, bullet or table cell contains six or more `{ref}` links to step pages,
**or** a step link's text is a three-digit number instead of the step code.

**Do.** Run `uv run tools/gen_step_tables.py` (or `--check` to verify without writing). **The
generator owns the whole presentation; nobody hand-builds a table or a dropdown here any more** — an
executor's job is only to run it after any edit that changes a run's step list, its markers or its
"*also …:*" wording, and to never hand-edit the generated block. What it emits, inside one
`<!-- step-tables:begin --> … <!-- step-tables:end -->` block, depends only on the run's own link
count:

1. **Run of 25 links or fewer.** The run **stays in the open, exactly where it is, byte-identical** —
   the generator does not touch it at all. Directly after it, the generated block is a table
   `Step | Code | Name` (`Step` right-aligned; `Code`/`Name` from `tools/steps.csv`), plus a `Role on
   this page` column *only when the run's roles are not all the same* — a column that reads "main" on
   every row tells the reader nothing, and material-page runs, which carry no markers at all, never get
   one. `Role`, when shown, comes only from the run's own markers ("main", "alternative", the
   `*also …:*` wording, asterisks and the trailing colon stripped) — never invented.
2. **Run of more than 25 links.** The generator **wraps the run itself** — on a material page, the
   `Steps:` line and the run together — in a collapsed `{dropdown}` titled "All N steps as one line of
   links (checked against the index)". That is the *entire* generated block: no separate table, no
   pointer sentence, no link repeated outside the dropdown. (An earlier design pointed to the page's
   grouped bullets from an otherwise-empty dropdown instead of moving the run; report-B review finding
   H1 rejected that as a control that promises links and delivers none, and this rule replaced it.)
3. **Mask pages** — six steps or fewer, one bullet each; the generator does not touch them.

**Placement is a checker contract, and the generator is verified against it, both with a wrapped and
an unwrapped run:**
* *machine pages* — the run (wrapped or not) must remain the **first block under `### SKY130 steps
  assigned to this class` that contains a step link and does not start with `* `**. A dropdown's
  opening fence and title line carry no step link, so they are skipped the same way a bullet list is;
  the run, now the fence's body, is still that first block. Verified: the table placed after an
  unwrapped run passes; the same table placed before the run fails with "steps: page only [], index
  only [...]"; a run wrapped in the dropdown, alone, also passes.
* *material pages* — the run (wrapped or not) must stay in the paragraph directly after a line reading
  `Steps:`. Verified: wrapping the `Steps:` line and the run together inside the dropdown passes.

**Example (run of 40 links, machine page)** — `docs/machines/wet-bench.md`:

```
Steps whose "Machines typically used" section names a wet bench …:

:::{dropdown} All 40 steps as one line of links (checked against the index)

{ref}`NS19 <step-013>`, {ref}`TUNME <step-039>`, …
:::

How the step pages grade the SkyWater tools for each step …
```

**Example (run of 148 links, material page)** — `docs/materials/process-gases.md`: the `Steps:` line
goes inside the dropdown with the run:

```
:::{dropdown} All 148 steps as one line of links (checked against the index)

Steps:

{ref}`SMAT <step-001>`, {ref}`BOX <step-002>`, …
:::
```

**Do not touch.** The order of the links, the `*alternative:*` and `*also …:*` markers and their
wording, the `N steps; see …` quick-facts row, and the generated block itself — re-run the generator
instead of hand-editing it; it is idempotent and never nests one dropdown inside another.

**Find.** `measure_b.py --list` keys `steplink-run-paragraph` (37), `bullet>=8steplinks` (41),
`tablecell>=8steplinks` (46); `grep -rEn '\{ref\}`[0-9]{3} <step-' docs/` for the bare-number links
(1,975 in 11 files).

**Kind.** the link text is scripted; the table or dropdown is **generated, never hand-written** —
`tools/gen_step_tables.py` (unblocked, `topic/rd-checkers`).

#### R-INDEX — index pages put methodology before navigation
*(reports B B2, B3 and C C6/C7)*

**Applies when** the first lookup table of an index page starts more than 300 words into the page, or
the page opens with evidence policy rather than with what the page is for.

**Do (safe now).**
1. Reorder whole H2 sections, with their `(label)=` lines, into: (1) purpose, ≤ 80 words;
   (2) navigation (cards or a lookup table); (3) detail tables; (4) "How to read this index" — the
   evidence and grading text, moved unchanged; (5) open questions; (6) references.
2. Move sections whole. Rewrite nothing, renumber nothing, drop no label.
3. Any **new** navigation table gets **its own heading**, and goes *above* the checked section or after
   it — never inside a checked section before the checked table. Verified on the masks index: a
   four-column navigation table inserted before `| Step | PDK mask (`masks.csv`) | …` inside
   `## Mask steps in this reference` makes `check_masks.py` report 76 problems; the same table under its
   own `## Find a mask` heading passes.
4. On `docs/machines/index.md`, a new table must **not** have exactly four columns with a machine link
   in its first cell: `index_rows()` maps every such line and the **last** one wins. Verified: such a
   table after the main table silently replaces the checked row and the page checks fail; before it, it
   is overwritten and passes — do not rely on that, give the new table a different shape.
5. Replace a bulleted list that merely repeats the sidebar (the 30 bare links at
   `docs/machines/index.md:17-57`) with a navigation table `class → one clause → number of steps`, and
   make the toctree `:hidden:`.

**Do (unblocked, `topic/rd-checkers`).** The main-table restructurings: machines index to
`Machine class | Steps` plus a `{grid}` of cards (`check_machines.index_rows` now reads a main-table
row of any width, first cell a machine link, last cell the Steps cell); materials index split into
`Material | Class page | Role | SkyWater evidence` and `Material | Steps` (`check_materials.Index` now
reads the Steps cell from a second table, keyed by key rather than by position, when the main table has
no Steps column). The restructuring itself — actually rewriting `docs/machines/index.md` and
`docs/materials/index.md` — is still **W3**; until it happens, the cosmetic fix remains available too:
wrap in `{table}` with a caption and `:widths:` (R-CAPTION).

**Do (blocked until W0d).** `docs/steps/index.md` — grouping into the 13 module H3s, the short sidebar
titles, the `Machine class` and `Mask` columns. It is generated; §2.8.

**Do not touch.** Cell wording, quotations, footnotes, the row order of any checked table; the six
checked columns of the masks index; the mask-types paragraph under `### Mask types and plate labels`
(the checker parses its **first paragraph**, sentence by sentence); the words "custody", "shipment",
"exp_ship" must never appear on a mask page or the masks index (`FORBIDDEN`).

**Find.** `grep -n "^## \|^| " docs/machines/index.md | head -40` and the same for the other three
indexes: the first `| ` line tells you how deep the first table sits.

**Kind.** hand (moves only).

#### R-TERM — glossary links and the glossary page
*(report C C9)*

**Applies when** a glossary term appears in a page's prose and that page has no `{term}` link for it,
or the glossary page is one undivided block.

**Do.**
1. Per page, link the **first** prose occurrence of each term: whole word, case-sensitive for
   acronyms. Plurals take the explicit form: ``{term}`vias <via>` ``.
2. Never inside: a heading, a code span, link text, a table header row, a footnote definition,
   `## References`, or **a quotation**.
3. Skip the ambiguous terms: `via`, `liner`, `TED`.
4. The `**Phase**` row of the step quick-facts table gets its leading `FEOL`/`MOL`/`BEOL` as a `{term}`
   (no checker reads that row; the stub template in `gen_steps.py` must be updated in the same
   change — **blocked until W0d** for the generator half).
5. Glossary page: one `{glossary}` block per initial under `## A` … `## W`, plus an A–Z link line.
   Sphinx merges the blocks and every existing `{term}` still resolves. Entries keep their wording.

**Do not touch.** Any term inside a quotation; the definitions themselves; the 15 terms that are never
linked (they are still definitions).

**Find.** `python3 docs/plans/readability/prototypes/links-theme/gloss.py` from the repository root
(prints terms, uses, and the per-page misses).

**Kind.** scripted proposal, hand acceptance — a `{term}` inside a quotation is the failure mode to
watch for.

#### R-CARDS — the landing page and section fronts
*(report C C6)*

**Applies when** a landing or section-front page is prose plus a toctree that repeats the sidebar.

**Do.**
1. Keep the existing paragraphs and their footnotes verbatim.
2. Add a `{grid} 1 2 3 3` of `{grid-item-card}`s with `:link:` and `:link-type: ref`, one sentence and
   a count per card: Overview ("start here"), Process steps (171), Categories (10), Machines (30),
   Materials (12), Masks (36), Glossary (219), References (1,826 sources + three indexes).
3. Add "The flow in 13 modules": the first four columns of the overview's module table
   (`docs/overview/index.md:328`), so a step is two clicks away. Copy the cells; change nothing.
4. Four lines on how to read a page (fact / typical / inference; footnotes), linking to the overview.
5. Make the three toctrees `:hidden:`.

**Do not touch.** The three opening paragraphs of `docs/index.md` and their markers. Counts must be
counted, not remembered: `ls docs/steps/[0-9]*.md | wc -l`, and so on.

**Find.** one page: `docs/index.md`. The same defect opens `docs/machines/index.md:17-57`.

**Kind.** hand. `docs/index.md` is not a `check_refs.py` target, so it needs no reading list.

#### R-ANCHOR — the inventory page
*(report C C10)*

**Applies when** an inventory entry has no anchor, or its `Tier:` and "Also used on …" sentences sit
before the bibliographic text.

**Do.**
1. Script an anchor line `(src-pdk-04)=` above every `**PDK-04** —` entry (label = key, lower-cased).
   Nothing else on the page changes; the popover can then link to the entry.
2. Move each entry's `Tier:` sentence and its "used on" sentences to the end of the entry, each on its
   own line. Whole sentences only, in their existing order.
3. Keep every heading, every key, every URL.

**Do not touch.** The keys (`check_refs.py` matches footnote labels against them, case-folded); the
status-flag sentence of any in-force patent entry (`check_inforce.py` compares it with the dataset,
character for character); the URLs (`check_links.py` reads this file).

**Example** — `docs/references/public-sources.md:83`, entry `**PDK-04**`: the bibliographic line and the
URL stay first; anything after them that begins "Tier:" or "Also used on" moves to the end.

**Find.** `grep -n "^\*\*[A-Z0-9-]*\*\* —" docs/references/public-sources.md` (1,826 entries).

**Kind.** scripted; nine tools read this file, so run every checker afterwards.

#### R-DROPDOWN — in-force notes as the reader meets them
*(report A F12)*

**Applies when** you are editing a page that contains a `{dropdown}`.

**Do.**
1. **Leave the dropdown title exactly as it is** (§2.7). The shortened title of report A F12 is an owner
   decision and is **blocked**.
2. Leave the body of the note in place. R-PARA, R-LIST, R-SENTENCE and R-TABLE may be applied *inside*
   it; nothing crosses the fence.
3. Pointer prose in the body text ("which, the collapsed note above sets out", 107 occurrences on 35
   pages) may be shortened to one end-of-sentence clause — "(details in the in-force patent note
   below)" — **only** when the sentence keeps its own meaning without it and no content of the note
   moves out.
4. The note stays directly after the paragraph it belongs to. Do not insert a heading, a figure or a
   table between them.
5. Never leave a dropdown empty: `check_inforce.py` reports an empty `{dropdown}` as a lost note.

**Example** — `docs/steps/138-capme.md:55` and `:92` carry the same title twice, and `:109`, `:114`,
`:153`, `:185`, `:225`, `:238` and `:289` point at "the collapsed note(s) above". The titles stay;
`:109` ("which, the collapsed note above sets out") may become a trailing clause.

**Do not touch.** Titles, fence markers, blank lines inside the block, the order of the notes.

**Find.** `grep -rn "{dropdown}" docs/steps/*.md` and `grep -rn "collapsed note" docs/steps/*.md`.
Counted on this branch, outside the generated block: 93 hand-written notes on 37 step pages, and 107
"collapsed note" pointers on 35 of them.

**Kind.** hand.

#### R-GENBLOCK — the generated "related index entries" block
*(reports A F13 and B B11, merged)*

**Applies when** never, for an executor. This rule exists so that you recognise the block and leave it
alone.

**The block** is everything between
`<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->` and
`<!-- index-links:end -->`, spliced immediately before `## References` on 206 pages (144 steps, 28
machines, 13 materials, 10 categories, 9 masks, 2 overview).

**Do.**
1. Nothing by hand. `gen_index_links.py --check` fails if the block differs by one character from what
   the generator would write, and `check_steps.py`, `check_machines.py`, `check_materials.py` and
   `check_masks.py` each call `stale_pages_in()` and fail too.
2. Keep `## References` occurring **exactly once** on the page: the generator finds its splice point by
   that heading and refuses a page with two.
3. Do not move the block, and do not put a heading between it and `## References`.

**The generator changes themselves (W0d, blocked):** emit
`### Patents, papers and filings about this step` (or an H2 on class pages, with the H2 added to the
three checker templates), use `{ref}`Title <patent-…>` — US 5,830,375 A (1996)` as the link text instead
of a bare number, and split the count-only sentence into a count line and a link line. One generator
commit plus one regeneration commit.

**Find.** `grep -rln "index-links:begin" docs/`.

**Kind.** generator. **Never by hand.**

### 3.4 Figures

#### R-FIGURE — figures are generated, never drawn
*(report D)*

**Blocked until W1a** (`tools/gen_figures.py`, `data/figures/`, `docs/_static/figures/`,
`figure-theme.js`, the tokens file, the "Figure conventions" page and the `check_inforce.py` hook for
figure specs). Until then no page gets a figure.

**Applies when** W1a has landed and your page type is listed in §4 as taking a figure.

**Do.**
1. **Never write SVG, and never hand-edit a generated SVG.** Copy an existing figure YAML in
   `data/figures/`, set `page`, `series`, the two `state_after` values, the panel titles, the arrow
   text, the alt text and the caption — **using only wording that is already on the page**.
2. Run the generator, fix every `LINT:` line, then look at the rendered result (the harness pages, shot
   at desktop and phone width) before pasting anything.
3. Paste the generated MyST block from `out/NAME.myst.txt` after the first paragraph of the section §4
   names for your page type.
4. Every label carries `basis: public | reading | inferred | typical`; anything other than `public`
   prints its tag. Every label note containing a number carries `cite:`, and that footnote key must
   already be defined on the target page.
5. Every cross-section carries "Not to scale. Thin films are drawn thicker than they are."
6. A dimension that is not public is never drawn to scale, and its label says "not public" first and the
   reading second.
7. **Nothing from a patent that `check_inforce.py` treats as in force may appear in a figure**, in any
   form: a figure cannot sit inside a collapsed note (§2.6).
8. The caption says what is shown, repeats the page's hedges, carries the citation and ends with "Not to
   scale". Alt text is 60–450 characters, describes the geometry and carries no citations.
9. At most two panels (three only for a deposit → pattern → etch summary on a category page). A figure
   never replaces text or a table, never sits inside a dropdown, and is always followed by prose.
10. The default taken in `readability-plan.md`: a figure **may** show a value the page gives as its own
    reading, always with the `our reading` tag and the hedge repeated in the caption.

**Example** — the prototype block, `docs/plans/readability/prototypes/diagrams/out/sti-006-stie.myst.txt`:

```
:::{figure} /_static/figures/sti-006-stie.svg
:alt: Two cross-sections of the wafer, one above the other. …
:width: 560px
:name: fig-sti-006-stie

The wafer before and after `STIE`. … about 0.33 µm is this page's reading of the PDK stack
drawing.[^pdk-04] Not to scale.
:::
```

(The prototype writes `/figures/<dir>/` in its paste blocks; production writes `/_static/figures/`.)

**Do not touch.** Any page text. A figure is additive: no sentence is deleted because a drawing now
shows it.

**Find.** §4 says which pages take which figure. `grep -rl '{figure}\|{image}' docs` returns nothing
today.

**Kind.** generator. **Never by hand.**

## 4. Page types

Each section gives the target skeleton, the order in which the rules are applied to that page, and the
limits that differ from §1. `+` marks an addition; everything else already exists and keeps its words.

### 4.1 Step page (`docs/steps/NNN-code.md`, 171 pages)

```
(step-NNN)=
# Step NNN — CODE: Name
| quick-facts table |                     unchanged; Phase cell gains a {term} link (R-TERM, W0d)

+ :::{admonition} At a glance                                         R-GLANCE, written last
+ :class: at-a-glance
+ * **Does:** …[^x]  * **Why:** …  * **Public numbers:** … (SKY130 only, or "none published")
+ * **Likely SkyWater tool:** …[^skw-01]  * **Not public:** … (→ Open questions)
+ :::

## What this step is                   lead: ≤ 2 paragraphs, ≤ 120 words, first sentence ≤ 25 words
   (generated {figure} block)          stays where gen_figures put it: directly after the lead
+ ### …                                any new H3 goes after the figure's caption, never between
                                       the lead and the figure
+ ### Key numbers                      table: Quantity · Value · Source · Basis   R-TABLE, R-CAPTION
+ ### What the public record shows     short paragraphs; measured-against-nominal tables  R-CAPTION
+ ### How <quantity> is estimated      input table, numbered arithmetic, hedged result  R-DERIVATION, R-CAPTION
+ ### Competing readings               where the page weighs two readings
## Step category                       one classification sentence ≤ 35 words, then
                                       "**Specific to this step:**" and 2–4 bullets       R-CATEGORY
## Why this step exists                1–2 lead sentences; 3–5 labelled bullets ≤ 60 words;
                                       studies as sub-bullets "Author (year) — finding.[^x]";
                                       keep the closing "Without `X` …" paragraph
## How it is typically performed       *italic lead-in*: the existing scope sentence, word for word
                                       numbered list for a sequence; parameter table or labelled
                                       bullets for a parameter set; SkyWater-specific statements last
## Machines typically used             bullets ≤ 40 words: class link, then example models
## Machines likely used at SkyWater    three-line items                                   R-TOOLS
## Resources required                  bullets; the supplier sentence once, last
## Related steps and cross-references  labelled bullets, in order Previous / Next / Same module /
                                       Depends on / Feeds / Category                      R-RELATED
   (generated index-links block)                                       never touched      R-GENBLOCK
## References                          three tiers, linked heads, `* ` bullets and their count unchanged
## Open questions                      labelled bullets; in-force notes last               R-OPENQ
<!-- footnotes -->
```

**Order of work.**

1. **R-H3** — structure below H2 (do this first; everything else is easier afterwards).
2. **R-TABLE**, **R-DERIVATION** — the numbers come out of the prose. **R-CAPTION** applies to step
   pages too: the lead-in sentence that introduces the table is its caption (see R-CAPTION).
3. **R-LIST**, **R-CATEGORY** — enumerations and the category paragraph.
4. **R-PARA**, **R-SENTENCE** — what is left of the prose.
5. **R-TOOLS** — the SkyWater tool items.
6. **R-OPENQ**, **R-RELATED**, **R-CODE** — the fixed-pattern sections.
7. **R-HEDGE**, **R-REPEAT** — hedge placement and repetition, once the sections are settled.
8. **R-GLANCE** — written last, from the finished page.
9. **R-DROPDOWN** applies throughout, whenever the page has a note.
10. **R-LINKS** (W0c) and **R-FIGURE** (W1a) are separate passes, not part of the hand edit.

**Form to use.**

| Form | Use it for |
|---|---|
| Table | any ≥ 3 × 2 parallel data: recipes, stacks, rules, measured against nominal, derivation inputs. **Not** the reference tiers |
| Numbered list | sequences and arithmetic steps |
| Bullets | reasons, failure modes, tools, resources, unknowns |
| Admonition | "At a glance"; at most 2 per page. The "How" scope sentence is an italic lead-in, not an admonition (R-HEDGE step 1) |
| Dropdown | **only** in-force-patent notes |
| Figure | module cross-section, tilt/shadow geometry, flow strip (W1a) |

**Checkers to run:** `check_steps.py`, `check_refs.py`, `check_inforce.py`, `gen_index_links.py --check`,
`-W` build.

### 4.2 Machine page (`docs/machines/*.md`, 30 pages)

```
(machine-slug)=
# Title
intro ≤ 70 words                                                     R-INTRO
| quick facts |                         cells ≤ 20 words             R-QUICKFACTS
+ :::{seealso} pointer sentences moved out of the intro :::          R-INTRO
## What the machine class is and how it works
   H3 per subsystem (allowed here), opening paragraph ≤ 60 words
+  (generated block-chain figure)                                    R-FIGURE, W1a
## Representative 200 mm-era models     table + ≤ 3 remarks           R-MODELS, R-CAPTION
## At SkyWater
### What SkyWater lists                 blockquote, then an entry table   R-ENTRIES
### Strength of the evidence            grade in bold in the first sentence, ≤ 80 words
### SKY130 steps assigned to this class dropdown holding the run FIRST, then the steps table,
                                        then the grade table Tool | Grade | Steps   R-STEPRUN
## Consumables and facilities           bullets whose lead-ins link material pages   R-COMPARE step 2
## Process-integration notes for SKY130 bullets ≤ 60 words, lead-in names the steps
## Related pages                        grouped under bold labels                    R-RELATED
   (generated index-links block)
## References
## Open questions                       one question per bullet
```

**Order.** R-INTRO → R-STEPRUN → R-MODELS → R-ENTRIES → R-QUICKFACTS → R-PARA/R-SENTENCE/R-LIST →
R-RELATED → R-CAPTION → R-LINKS (W0c).

**The H2 and the three H3s under `At SkyWater` are fixed** (§2.9). H3s **are** allowed under
`What the machine class is and how it works` — `docs/machines/duv-krf-stepper.md:42`
(`### Excimer laser source`) is an existing example.

**Checkers:** `check_machines.py`, `check_refs.py`, `check_inforce.py`, `gen_index_links.py --check`.

### 4.3 Material page (`docs/materials/*.md`, 12 pages)

Same skeleton as the machine page with the material H2s (§2.9), plus:

* the summary table before the first H2 must still start with `What they do` and end with
  `SkyWater evidence`, `SKY130 steps`; the last cell reads "N steps; see …" and **N must equal the
  number of step links in the steps paragraph**;
* under `### SKY130 steps that use this class`: the `Materials index rows covered:` line and its
  `` * `key` — short name `` bullets stay exactly as they are (one key per bullet, first on its line);
* the `Steps:` line and the paragraph after it stay adjacent, the steps in ascending order, each link
  showing the step's code. The pair may move inside a `{dropdown}` together (verified);
* `+ Material | Steps (count) | Used for` table after the steps paragraph, built from the grouped
  bullets — no new facts;
* the supplier table at `docs/materials/sputter-targets.md:195` is the model for "What SkyWater's
  filings list".

**Order.** R-INTRO → R-STEPRUN → R-MODELS → R-ENTRIES → R-QUICKFACTS → prose rules → R-RELATED →
R-CAPTION.

**Checkers:** `check_materials.py` (also on the index), `check_refs.py`, `check_inforce.py`,
`gen_index_links.py --check`.

### 4.4 Mask page (`docs/masks/*.md`, 36 pages)

The strictest checker and the most consistent pages. **Leave alone:** quick facts (every row except
`Polarity and tone` and `Exposure class` is compared with the index), the plates table, the step
bullets, the design-rule table's rows, the reticle-set column, the title, the `(mask-<stem>-steps)=`
label before `## Steps that use this mask`.

```
(mask-slug)=
# CODE — name                            title text is checked against the index
| quick facts |                          leave                       §2.9, R-QUICKFACTS step 4
intro ≤ 70 words                                                     R-INTRO
## What the mask defines
## Drawn layers and derivation
### In the PDK
### In the public renders                must keep "not SkyWater's" and "renders of *drawn* data"
+ (derivation-chain figure)                                          R-FIGURE, W1a
## Plates and reticle sets               optional H3 `The mask-type record` only
## Lithography and pattern transfer      + H3s: Exposure class, Mask errors, Resist and tone,
                                         Overlay and alignment, Pattern transfer   R-H3 — **W0e**
## Steps that use this mask
## Design rules and critical dimensions  + parameter table               R-PARAMS, R-CAPTION
## Related pages                                                        R-RELATED
## References
## Open questions
```

**Order.** R-INTRO → R-PARAMS → R-CAPTION → prose rules → R-RELATED → (W0e) R-H3.

**Never** write "custody", "shipment" or "exp_ship" on a mask page or the masks index.

**Checkers:** `check_masks.py`, `check_refs.py`, `check_inforce.py`, `gen_index_links.py --check`.

### 4.5 Category page (`docs/categories/*.md`, 10 pages)

No heading checker, so this is the freest page type — and the one where `check_refs.py` still demands
**12** Deep dive entries.

```
(category-slug)=
# Title
+ intro ≤ 60 words, assembled from the first paragraph of "What this class of step does"   R-INTRO
+ | quick facts | What it does · Steps in SKY130 (N) · Tool classes (links) ·
                  Consumable classes (links) · Governing relation
## What this class of step does
+ (generic mechanism figure)                                          R-FIGURE, W1a
## Physics and engineering background    H3s welcome; comparisons as tables   R-COMPARE, R-CAPTION
## Typical equipment                     Tool class (link) | Representative models | Note;
                                         model history stays on the machine page
## Typical consumables                   lead-ins link material pages          R-COMPARE step 2
## Steps in this category                + `Machine class` column              R-COMPARE step 3
   (generated index-links block)
## References                            ≥ 12 Deep dive bullets — count unchanged
```

**Order.** R-INTRO → R-COMPARE → R-TABLE → R-CAPTION → prose rules → R-LINKS (W0c).

### 4.6 Index pages (`{machines,materials,masks,categories}/index.md`, `steps/index.md`)

Target shape, in this order: **purpose ≤ 80 words → navigation table or cards → detail tables → "How to
read this index" (the evidence and grading text, moved unchanged) → open questions → references.**
`docs/categories/index.md` is already in this shape; copy it.

| Index | Safe now | Blocked |
|---|---|---|
| `machines/index.md` | reorder H2s (R-INDEX 1–2); replace the 30 bare links at `:17-57` with a table; caption the tables | two-column main table + card grid — **W0e** |
| `materials/index.md` | reorder; caption; `{table}` + `:widths:` on the six-column table | split into two tables keyed by material — **W0e** |
| `masks/index.md` | reorder; caption; a navigation table **under its own heading** | none of the six checked columns may move |
| `categories/index.md` | nothing needed | — |
| `steps/index.md` | nothing by hand | grouping, columns, sidebar titles — **W0d**, generator |

**Do not** put a new table inside a checked section above the checked table (verified failure), and do
not give `machines/index.md` a new four-column table whose first cell links a machine page (verified
failure). See §5.

### 4.7 Overview (`docs/overview/index.md`)

* **Reorder H2s only**, labels and text unchanged: *How to read this reference* → *The flow by module* →
  *A simplified cross-section* → *Front end, middle of line and back end* → *What SKY130 is* → *The
  metal cap and barrier question* → *Key open questions* → *References*.
* Add a five-bullet "On this page" of `{ref}` links after the opening paragraph (furo hides the contents
  list below about 1,300 px).
* Turn each run-in bold module paragraph into an H3 (R-H3), so the 13 modules appear in the contents
  list and can be linked from the landing page. **Each collapsed in-force note stays directly after its
  own paragraph** — the overview has them (for example at `docs/overview/index.md:344`).
* Paragraphs ≤ 90 words here (the page has 13 over 120, longest 517); more than four markers in a
  paragraph means a list or a table.
* Figures (W1a): the module flow strip directly above the module table at `:328`; the to-scale back-end
  stack at the top of *A simplified cross-section*; the two Cypress metal-1 stacks in the metal-cap
  section.
* Moving the metal-cap section to its own page is an **owner decision**; 57 pages use its label.

### 4.8 Landing page (`docs/index.md`)

Three paragraphs and their footnotes verbatim → **R-CARDS** grid → the 13-module table (first four
columns of the overview's) → four lines on how to read a page → `:hidden:` toctrees. No reading list;
this page is not a `check_refs.py` target. Every section in one click, a module's first step in two.

### 4.9 Glossary (`docs/glossary.md`)

One `{glossary}` block per initial under `## A` … `## W`, plus an A–Z link line; entries unchanged, ≤ 80
words, first sentence expands the acronym; `{term}` and `{ref}` roles only. Bold terms come from CSS
(W0a), not from markup. **R-TERM** step 5.

### 4.10 Inventory (`docs/references/public-sources.md`)

Entry = anchor line, bold key, bibliographic sentence, URL(s), what it gives, then `Tier:` and the "used
on" lines last. Keep all ten section headings and every key. **R-ANCHOR**. Nine tools read this file:
run every checker after any change to it.

### 4.11 References index (`docs/references/index.md`)

After the first paragraph, add a four-row table — Inventory · Papers · Patents · Filings, each with its
count and one clause. Update "How citations work" for the linked reading-list heads (R-LINKS) once W0c
has landed.

### 4.12 Generated index pages (`docs/references/{papers,patents,filings}/`)

**Never edited.** Their order (purpose → browse the views with counts → how to read an entry → legal
caveat → a `{dropdown}` holding the present methodology text verbatim) and their clickable URLs are
generator changes, in `gen_patents.py`, `gen_papers.py` and `gen_filings.py`. **W0d.**

## 5. Checker contract

Every checker in `tools/` is a **positional text parser**. It does not build a document tree; it splits
on headings, on blank lines and on `| ` at the start of a line. That is why layout changes can break a
check that seems unrelated to the text you edited. This section says, per checker, exactly what
structure it depends on. It was written by reading the code, and the "verified" notes were produced by
running the checker on a copy of the tree.

### `tools/check_steps.py`

* Tests only that each of the 13 strings of §2.9 occurs as `"\n" + heading + "\n"`. Exact characters,
  alone on its line. Order is not checked; extra headings are free; **that is why new H3s on step pages
  are safe**.
* Reports pages still containing "This page is a stub."
* Calls `gen_index_links.stale_pages_in("steps")`, so a hand-edited generated block fails here too.

### `tools/check_refs.py`

* Targets and Deep dive minimums: `docs/steps/NNN-*.md` 8; `docs/categories/*.md` (not `index.md`) 12;
  **`docs/machines/*.md` and `docs/materials/*.md`, `index.md` included**, 12; `docs/masks/index.md` 12;
  other `docs/masks/*.md` 8; `docs/overview/*.md` 12.
* `deep_dive_count()` matches from `^### Deep dive\n` **to the next `^## ` or `^### ` or the end of the
  file**, and counts lines matching `^\* `. Consequences:
  * inserting any heading inside the Deep dive list truncates the count;
  * a bullet turned into a table row, or indented into a sub-bullet, stops counting;
  * two bullets merged into one lose a count.
  **Never change the number of `* ` lines under `### Deep dive`.**
* Every `[^label]` must have a definition and every definition a reference; no duplicates; every label
  must be an inventory key of `docs/references/public-sources.md` (case-folded).
* `^\[not-caret\]:` anywhere is an error ("reference-style link definitions present"), so never use the
  `[text]: url` link style.
* Pages containing "This page is a stub." or "This section is a stub." are skipped entirely.

### `tools/check_machines.py`

* H2 headings, by `re.findall(r"^## (.+)$")`, must equal the template list **in order**. H3s under
  `At SkyWater` and under `References` likewise. H3s under the other H2s are unconstrained.
* The page needs a `^(machine-…)=$` label line.
* `index_rows()` scans **every line of `docs/machines/index.md`** that starts with `| `, splits it on
  `" | "`, and records `rows[label] = cells[3]` when `cells[0]` contains `<machine-…>` **and there are
  exactly four cells**. The **last** matching line wins.
  *Verified:* a four-column navigation table with a machine link in its first cell, placed **after** the
  main table, silently replaces the checked row and the page checks fail (three problems on
  `wet-bench.md`); placed before it, it is overwritten and passes. Give any new table a different shape.
* The page's step run is `next(p for p in body.split("\n\n") if STEP_RE.search(p) and not
  p.lstrip().startswith("* "))` inside `### SKY130 steps assigned to this class` — **the first
  blank-line-separated block there that contains a step link and is not a bullet list**. A table block
  starts with `| `, not `* `, so a table placed before the run *becomes* "the run".
  *Verified:* dropdown + run first, table after → passes; table before the run → "steps: page only [],
  index only ['step-039', …]".
* Main, `*alternative:*` and `*also …:*` lists are compared as **sets** with the index cell, duplicates
  are reported, and the `*also …:*` **marker wording must match the index's, character for character**.
* Both `{ref}`CODE <step-NNN>`` and bare `{ref}`step-NNN`` are accepted.

### `tools/check_materials.py`

* Main table of `index.md` under `## Materials index`: lines starting `| ` (except `| Key |`) must split
  into **exactly six** cells, the first being `` `key` `` and nothing else, and the sixth must start
  with "all except" or with `{ref}`. Changing the column count or the key position is the **W0e**
  change.
* Class-page table under `## How to read the index` starts at the line `| Consumable class | Page |` and
  needs three cells per row.
* Per page: the `(material-…)=` label, the exact H2 list, the exact H3 lists under `At SkyWater` and
  `References`, and an entry in the class-page table.
* `Materials index rows covered:` must be followed immediately by `* ` bullets shaped
  `` * `key` — name``; a continuation line must start with two spaces, and the first line that is
  neither stops the list.
* `paragraph_after(body, "Steps:")` matches `^Steps:[ \t]*\n[ \t]*\n(.+?)(\n[ \t]*\n|\Z)`: a line
  reading **exactly** `Steps:`, one blank line, then the run as one block. Nothing may come between
  them. *Verified:* wrapping both in a `{dropdown}` (fence, blank line, `Steps:`, blank line, run, blank
  line, closing fence) passes.
* The steps paragraph must link exactly the union of the owned rows' steps, in ascending order, without
  duplicates, each link's text being the step's code taken from the title of its step page.
* `check_summary()` takes the text before the first `\n## `, keeps **every** line starting with `|`,
  drops the first two, and treats the rest as rows. A second table before the first H2 would be read as
  more rows. The first row must be `What they do`, the last two `SkyWater evidence` and `SKY130 steps`,
  and the last cell must read "N steps; see …" with N equal to the number of step links in the steps
  paragraph. *Verified:* wrapping the summary table in `:::{table}` with a caption and `:widths:`
  passes — directive lines do not start with `|`.

### `tools/check_masks.py`

* The index is read **by heading title**, and in each section by `table()`, which returns **the first
  markdown table in that section's body** (it starts at the first `|` line and stops at the first
  non-`|` line after that).
  *Verified:* a navigation table inserted before `| Step | PDK mask (`masks.csv`) | …` inside
  `## Mask steps in this reference` makes the checker report 76 problems across the 36 mask pages; the
  same table under its own `## Find a mask` heading passes.
* Sections it reads: `## Mask steps in this reference` (the six-column table),
  `## Plates recorded for the MPW runs` (its **opening paragraph**, for the "Run Mask IDs" names),
  `### Runs, reticle sets and plate IDs`, `### Plates by mask` (first table),
  `### Mask types and plate labels` (its **first paragraph**, parsed sentence by sentence).
* Per page: H2 list exact and ordered; H3s under `Drawn layers and derivation` and `References` exact;
  `Plates and reticle sets` may have only `The mask-type record`; **every other H2 must have no H3** —
  the `OPTIONAL_H3` extension is the **W0e** change that unblocks R-H3 on mask pages.
* `## Steps that use this mask` must be immediately preceded by `(mask-<stem>-steps)=`.
* Quick facts: the **first** table before the first H2; header exactly `| | CODE — name |`; rows exactly
  `FACT_ROWS`, in order. Cells are compared with the index after footnote markers are stripped and
  whitespace collapsed: `Plates recorded`, `Plate no.` and `Dies with shapes …` must match the index
  cell **exactly**; the layer, drawn-layer and CD rows must contain, **in the index's order**, every
  code span, quotation, `layer:datatype` pair, number and `N/A` of the index cell. `Polarity and tone`
  must be non-empty; `Exposure class` must link a machine page; `Mask type …` must start with the
  index's code or read the exact `NO_TYPE` sentence; the last row must read "N steps; see …" and link
  `mask-<stem>-steps`.
* The plate table under `Plates and reticle sets` has a header starting `| Run |` and one row per run,
  MPW-1 to MPW-8 in order.
* `In the public renders` must keep "not SkyWater's" and "renders of *drawn* data".
* The words `custody`, `shipment`, `exp_ship` are forbidden anywhere on a mask page or the index.

### `tools/check_inforce.py`

* See §2.6 for what it forbids. Structurally:
  * it flattens the page (all whitespace collapsed) before matching, so a number or a title split across
    lines is still found, and **line numbers come from a character-to-line map**;
  * "inside a collapsed block" is computed **by line**: `dropdown_lines()` tracks `:::{name}` and
    ```` ```{name} ```` fences and their nesting, and treats the `{dropdown}` directive line itself as
    inside (that is where the number legitimately sits);
  * a footnote definition is its `[^label]:` line plus the following lines indented by **four spaces**;
    a blank line only continues the definition when the next line is indented. Re-wrapping a definition
    with a different indent moves it out of its own exemption;
  * the inventory is split into entries by blank lines, each starting `**KEY**`;
  * the status-flag sentence is compared with the dataset **character for character**, including the
    date;
  * a `{dropdown}` with a blank body is an error;
  * `docs/plans/` and `docs/references/patents/` are skipped, which is why this guide may quote a
    dropdown title.

### `tools/check_links.py`

* Scans **only** the inventory entries and the **footnote definitions** of pages under `docs/`. It does
  not scan the generated index directories, and it does not see a URL written inline in the body.
* That is the whole reason for §2.11: an inline link must copy a URL that already exists in a footnote
  definition on the same page, or it escapes link-rot checking. The `check_refs.py` invariant that
  enforces it is the **W0c** change.

### `tools/gen_index_links.py --check`

* Finds its splice point with `"\n## References\n"` and **refuses a page that has it twice**.
* Rebuilds the block and compares it byte for byte with what is on the page; any difference is "stale".
* `stale_pages_in()` is called by `check_steps`, `check_machines`, `check_materials` and `check_masks`,
  so a hand edit to the block fails four checkers at once.

### `tools/gen_steps.py`

* Rewrites `docs/steps/index.md` **in full** and never overwrites an existing step page.
* **It is stale.** Its `write_index()` emits a two-sentence intro and no `[^steps-sheet]` footnote,
  while the committed page carries a longer intro, the marker and the definition. Running it today
  **silently deletes that citation** — `check_refs.py` does not target `steps/index.md`, so nothing
  would fail. Do not run it before W0d.

### `tools/check_papers.py`, `check_patents.py`, `check_filings.py`

Dataset checkers (`data/*.yaml`). They constrain no prose on a hand-edited page. Run them anyway: they
are cheap and they catch an accidental edit to a generated page.

### `tools/check_preserved.py` (W0b, being written on another branch)

The before/after preservation check every hand-edit branch must run. Per
`docs/plans/readability-plan.md` W0b it compares a page before and after an edit and requires the
multisets of **footnote markers, numbers and quoted strings** to be identical, apart from declared
additions (such as step names and step numbers added by a new table). Use it as §7 step 4 describes.
Until it exists, do the same comparison by hand with the snippet in §7.

## 6. MyST crib — forms verified to build in this project

Every form below was built with `uv run sphinx-build -W -q -b html` in a scratch project carrying this
project's `conf.py` settings (`myst_parser`, `sphinx_copybutton`, `sphinx_design`, furo,
`colon_fence`, `deflist`, `fieldlist`, `substitution`, `tasklist`, `attrs_inline`,
`myst_heading_anchors = 3`, `nitpicky = True`). Copy them; do not invent variants.

**Table with a caption and widths.** The blank line after the options is optional — both build, both
produce a `<caption>`. `:widths:` numbers are relative; `:class:` is optional.

```
:::{table} Published retrograde N-well implants, as each source gives them
:widths: 24 20 20 36

| Source | Energy (keV) | Dose (cm⁻²) | Basis |
|---|---:|---:|---|
| Harris twin-well[^a] | 500, 275, 130 | — | as published |
:::
```

A caption may carry a footnote marker (`… blank in the PDK[^pdk-periph]`) — verified.

**Table inside a list item.** Blank line before and after; the table indented two spaces with the item.

```
* **Energy.** Set by the wanted peak depth.

  | Source | Energy (keV) |
  |---|---:|
  | Harris[^a] | 500 |

  For a 1.1 µm well depth the deepest energy is plausibly 500 keV–1 MeV (our reading).
```

**Admonition with a title** (use for "At a glance"; `:class: at-a-glance` is required, see R-GLANCE
step 1 and W0a):

```
:::{admonition} At a glance
:class: at-a-glance
* **Does:** etches the isolation trench.[^a]
:::
```

**Italic lead-in** (use for the "How" scope sentence, R-HEDGE step 1 — not an admonition) and
**see-also** (use for pointer sentences moved out of an intro):

```
*An industry-generic recipe for a 200 mm, 130 nm-era fab.*

:::{seealso}
The mechanism is on the category page.
:::
```

Both also build **inside a list item**, indented with it and surrounded by blank lines — verified.

**Dropdown**, colon fence or backtick fence; both are recognised by `check_inforce.py`:

```
:::{dropdown} From a patent shown as in force (US 8,110,414; estimated expiry 2030-01-02) — open to read
A sentence inside the collapsed note.[^b]

* A reading-list bullet inside the note.[^a]
:::
```

````
```{dropdown} Title
Text inside.
```
````

A dropdown also builds inside a list item, and around a `Steps:` line plus its link run — verified.

**Grid of cards** (landing page, R-CARDS). Four fences: `::::` outside, `:::` per card.

```
::::{grid} 1 2 3 3
:gutter: 2

:::{grid-item-card} Process steps
:link: steps-index
:link-type: ref

171 pages, one per step.
:::

:::{grid-item-card} Machines
:link: machines-index
:link-type: ref

30 machine classes.
:::
::::
```

**Tab set** (two views of one dataset):

```
::::{tab-set}
:::{tab-item} By class
…
:::
:::{tab-item} By SkyWater tool
…
:::
::::
```

**Definition list** (term → explanation, two columns only):

```
Entry as listed
: What it names — "phosphoric" is the acid.[^a]

Another entry
: Our reading, not a documented fact.
```

**Figure** with alt text, width, name and a caption carrying footnotes:

```
:::{figure} /_static/figures/sti-006-stie.svg
:alt: Two cross-sections of the wafer, one above the other, showing a trench etched through
    nitride and pad oxide into silicon.
:width: 560px
:name: fig-sti-006-stie

The wafer before and after `STIE`; about 0.33 µm is this page's reading of the PDK stack
drawing.[^pdk-04] Not to scale.
:::
```

**Footnotes in table cells** build — that is how the quick-facts tables already work.

**`{numref}` does not build.** `numfig` is off; `See {numref}`fig-…`` produces
`WARNING: numfig is disabled. :numref: is ignored.` and `-W` turns it into a failure (verified, exit 1).
Refer to a figure by its caption words, not by a number.

**Roles.** `{ref}`CODE <step-NNN>``, `{ref}`category-etch``, `{term}`vias <via>``. `nitpicky = True`
means a broken target fails the build.

**What not to use.** `{numref}`; `list-table` inside any checked table (§5); reference-style links
(`[text]: url`, refused by `check_refs.py`); MyST `linkify` (not enabled — a bare URL does not become a
link, which is why generated pages wrap URLs in `<…>`).

## 7. Per-page procedure (executor)

One page at a time. Do not start a second page before the first passes.

**0. Set up once per branch.**

```
cd <repo>
git worktree add .worktrees/<name> -b topic/<name> main
mkdir -p tmp/readability/a-tools tmp/preserve tmp/shots
cp docs/plans/readability/prototypes/measure/measure*.py tmp/readability/a-tools/
```

Everything below runs from the worktree. `tmp/` is git-ignored.

**1. Baseline.** Build once and photograph the page **before** you touch it, at both widths, and open
the tiles:

```
uv run sphinx-build -W -q -b html docs tmp/_build/html
uv run -q --with pillow python tools/shoot.py "file://$PWD/tmp/_build/html/steps/006-stie.html" \
    tmp/shots/006-before
uv run -q --with pillow python tools/shoot.py "file://$PWD/tmp/_build/html/steps/006-stie.html" \
    tmp/shots/006-before-phone --width 400
```

Read the PNGs with the Read tool. You are fixing what you can see there.

**2. Save the "before" copy** for the preservation check:

```
git show HEAD:docs/steps/006-stie.md > tmp/preserve/before.md
```

**3. Apply the rules in the order your page type gives** (§4). One rule at a time over the whole page,
not one paragraph at a time over all rules. Commit after each rule, or at least every 15 minutes.

**4. Preservation check.** `tools/check_preserved.py` is being written on another branch (W0b). When it
exists, run it as `uv run python tools/check_preserved.py docs/steps/006-stie.md` against the committed
version, and declare additions (step numbers and step names added by a new table) the way its help
says. Until then, run the same comparison by hand:

```
python3 - tmp/preserve/before.md docs/steps/006-stie.md <<'PY'
import re, sys, collections
MARK = re.compile(r"\[\^[A-Za-z0-9_-]+\]")
NUM  = re.compile(r"(?<![\w.])\d[\d   ,.]*\d(?![\w])|(?<![\w.])\d(?![\w.])")
QUOT = re.compile(r'"[^"\n]{1,400}"')
def bag(p):
    t = open(p).read()
    markers = collections.Counter(MARK.findall(t))
    t = MARK.sub("", t)
    return (markers,
            collections.Counter(n.strip() for n in NUM.findall(t)),
            collections.Counter(QUOT.findall(re.sub(r"\s+", " ", t))))
a, b = bag(sys.argv[1]), bag(sys.argv[2])
for name, x, y in zip(("markers", "numbers", "quotations"), a, b):
    if x != y:
        print(f"{name}: lost {dict(x - y)}")
        print(f"{name}: gained {dict(y - x)}")
print("identical" if a == b else "DIFFERENT")
PY
```

The only acceptable gains are step numbers and step names that a new table introduces, and an em dash
`—` where a cell has no value. **Any loss is a bug in your edit.** (Tested: an unchanged page prints
`identical`; a page with one marker deleted and one digit changed prints exactly what was lost.)

**5. Checkers**, from §4 for your page type, then always these:

```
uv run python tools/check_steps.py ; uv run python tools/check_refs.py
uv run python tools/check_machines.py ; uv run python tools/check_materials.py
uv run python tools/check_masks.py ; uv run python tools/check_inforce.py
uv run python tools/gen_index_links.py --check
```

**6. Build with `-W`.** `uv run sphinx-build -W -q -b html docs tmp/_build/html`. A warning is a
failure. The usual causes are a broken `{ref}` (nitpicky), an unreferenced footnote definition after a
deletion, and `{numref}`.

**7. Look at the result**, desktop and phone, with `tools/shoot.py`, and open every tile. Compare with
the "before" tiles. Fix what looks wrong: a table that scrolls sideways, a cell that fills the screen, a
caption that wraps badly, a bullet list that lost its indentation.

**8. Self-review checklist** — all of these before you commit the page:

* [ ] The preservation check prints `identical`, or the only gains are new step numbers, step names and
      `—`.
* [ ] No sentence was deleted except a duplicate handled under R-REPEAT, and every footnote label in it
      still occurs on the page.
* [ ] Every hedge that was there is still there, in the same strength.
* [ ] Every `{dropdown}` has the same title, the same body, and nothing moved across its fence.
* [ ] No empty table cell was filled; empties are `—`.
* [ ] No new external link, unless its URL appears verbatim in a footnote definition on this page.
* [ ] The number of `* ` bullets under `### Deep dive` is unchanged.
* [ ] The mandatory headings of §2.9 are untouched, and any new H3 is allowed on this page type.
* [ ] The generated index-links block is untouched and `## References` occurs once.
* [ ] Paragraphs ≤ 100 words, list items ≤ 60, sentences ≤ 45, cells ≤ 25 (quick facts ≤ 20).
      Measure against these §1 caps, never against looser "flag" thresholds. After the last page
      of a batch, run the measurement over the whole batch again and put the counts at the §1 caps
      in the progress file.
* [ ] Every new table has a caption (R-CAPTION): on a step page its lead-in sentence ending in a
      colon; a `:::{table}` wrapper and `:widths:` only when it has a prose column. It obeys the §1
      column budget (≤ 3 prose, ≤ 5 short-cell), tested at 400 px.
* [ ] Every checker and the `-W` build pass.
* [ ] The phone tiles show no horizontal scrolling outside a table.
* [ ] Anything doubtful — an arithmetic slip, a number that looks wrong, a source that contradicts the
      text — is written in `docs/plans/progress-<branch>.md` and **not fixed**.

**9. Commit** with the page name in the subject and the rule ids in the body, and update the progress
file in the same commit.

## 8. Reviewer checklist (Opus)

Review the diff **and** the rendered tiles. The executor cannot see what it did not think to look at.

1. **Read the diff as a fact diff, not a text diff.** For every hunk: did a number, a unit, a quotation,
   a hedge or a marker change? Re-run the preservation snippet of §7 yourself against `main`.
2. **Spot-check the tables.** Pick three cells of every new table and find the same value in the
   original prose — same digits, same significant figures, same quotation marks, same marker. Confirm
   that an empty cell is empty in the source too, and is `—`.
3. **Check the hedges.** Every "our reading", "inference", "industry-typical", "not public" that was in
   the prose must be somewhere in the new structure, at the same strength, and a table-wide hedge must
   sit directly under its table.
4. **Check the dropdowns.** Title unchanged; body unchanged; nothing about an in-force patent anywhere
   else on the page, in the "At a glance" box or a caption least of all. Run `check_inforce.py`.
5. **Check the Deep dive count** and the reading-list bullets: same number of `* ` lines, same order,
   markers still last.
6. **Look at the tiles**, desktop and phone, before and after. Ask: can I find the page's three numbers
   in ten seconds? Does the first screen say what the step does? Is any table wider than the column? Is
   any cell taller than five lines?
7. **Check the checker contract** for the page type (§5), especially: the step run is still the first
   non-bullet block with step links on a machine page; the `Steps:` paragraph is still adjacent on a
   material page; no new table sits above a checked table in the same section.
8. **Confirm the blocked rules were not started** (§9).
9. **Read the progress file.** Anything the executor flagged as doubtful is a finding for the
   coordinator, not something the reviewer fixes in the readability branch.
10. **Reject the page if any item of the Never list (§2) was broken**, however good the rest is.

## 9. Blocked rules

Nothing in this table may be started by an executor before the workstream lands. `readability-plan.md`
holds the status.

| Rule | Blocked on | What is blocked |
|---|---|---|
| R-LINKS | **W0c** | citation-style rule 5 reworded; the "inline URL must be in this page's own footnote definitions" invariant in `check_refs.py`; `tools/fix_reading_list_links.py` |
| R-WAYBACK (tooling) | **W0f** | `check_links.py` lookup fix, `--suggest-archive`, `--include-generated`. The citation *form* is usable now |
| R-H3 on mask pages | **unblocked** (`topic/rd-checkers`) | done: `check_masks.OPTIONAL_H3` accepts `Exposure class`, `Mask errors`, `Resist and tone`, `Overlay and alignment`, `Pattern transfer` for "Lithography and pattern transfer", plus any further H3 there. Converting the 36 mask pages' run-in `**Bold.**` labels to real H3s (B8) is unaffected by this and is still a separate **W3** batch |
| R-INDEX, machines main table | **unblocked** (`topic/rd-checkers`) | done: `check_machines.index_rows()` reads a main-table row of any width (>= 2 cells), first cell a machine link, last cell the Steps cell — the old 4-column form still works. Restructuring `docs/machines/index.md` itself to `Machine class \| Steps` plus a card grid is still **W3** |
| R-INDEX, materials main table | **unblocked** (`topic/rd-checkers`) | done: `check_materials.Index` reads the Steps cell from a second `Material \| Steps` table, keyed the same way as the main table, when the main table has no Steps column; the main-table key no longer has to be the literal first cell. Restructuring `docs/materials/index.md` itself is still **W3** |
| R-INDEX, `docs/steps/index.md` | **W0d** | `gen_steps.py`: sync with the committed intro **first** (it is stale), then module grouping, short sidebar titles, `Machine class` and `Mask` columns, `--check` |
| R-GENBLOCK | **W0d** | `gen_index_links.py` heading and link text, `--selftest` update, one regeneration commit |
| R-STEPRUN, generated tables | **unblocked** (`topic/rd-checkers`) | done: `tools/gen_step_tables.py` owns the whole presentation — a run of <= 25 links stays in the open and gets a table after it; a run of > 25 links is wrapped, by the generator, in a collapsed dropdown (report-B review H1: no separate empty-shell dropdown) — on all 42 machine and material pages; wired into `.readthedocs.yaml` and `agent-briefs.md` |
| R-TERM, Phase cell | **W0d** | the stub template in `gen_steps.py` must change in the same commit |
| R-FIGURE | **W1a** | `tools/gen_figures.py --check`, `data/figures/`, `docs/_static/figures/`, `figure-theme.js`, tokens, the "Figure conventions" page, the `check_inforce.py` hook for figure specs |
| R-DROPDOWN, shorter titles | **owner** | the in-force title wording is the owner's; A F12 is a proposal |
| Theme work (C2, C3, C12) | **W0a** | `docs/_static/custom.css`, `footnote-popover.js`, `conf.py`. Not a content edit; it fixes the phone layout for all 291 pages at once |
| `check_preserved.py` | **W0b** | until it lands, use the snippet in §7 |

Owner decisions still open, recorded here so that no executor decides them by accident: shortening
in-force dropdown titles; moving the metal-cap section off the overview; splitting the inventory or
generating its "used on" lines; mask-render thumbnails versus links; whether the materials `Key` column
is reader-facing; the 44 em text measure; whether a figure may show a value the page gives as its own
reading (default: yes, tagged).
