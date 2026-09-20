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
| Table columns | ≤ 4 when any column holds prose (at most 2 prose columns); ≤ 6 when every cell is a number, a code or ≤ 3 words | — | header row | A F3 (≤ 5) vs B §2.1 → **B's rule**; it is measured against furo's ~740 px column |
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
2. Split at a seam. Keep every sentence, in its original order and wording.
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
1. End the announcing sentence with a colon.
2. One bullet per item, in the original order, with the item's own clause and marker.
3. Open each bullet with a bold label of 2–4 words taken from the item's own words, then an em dash.
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
6. Three to six H3s per step page. More than six means the H3s are labelling paragraphs, not sections.

**Example** — `docs/steps/006-stie.md:30`.

Before: `**How deep?** No SkyWater document gives the SKY130 trench depth, and the PDK stack drawing does
not settle it. …`

After: a heading line `### How deep?`, a blank line, then `No SkyWater document gives the SKY130 trench
depth, and the PDK stack drawing does not settle it. …`

**Do not touch.** The 13 mandatory step headings; the H2/H3 template of machine, material and mask pages
(§2.9); the placement of `{dropdown}` blocks — a note stays directly after the paragraph it belongs to,
and an H3 is never inserted between them.

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
1. First paragraph, ≤ 35 words: "`CODE` is a {ref}`<category>` step of the *<class>* class", plus the
   one parameter that defines the class, with its markers.
2. Then a line `**Specific to this step:**` and 2–4 bullets holding the remaining sentences, unchanged
   except for the splitting.
3. If a sentence here repeats a passage from another H2 on the same page, apply **R-REPEAT**: the fact
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
1. Wrap the existing opening scope sentence, **word for word**, in `:::{note}` … `:::`. Nothing else
   goes inside.
2. When splitting a sentence, move its hedge to the end of the sentence it qualifies. Four end tags are
   allowed — "(inference)", "(our reading)", "(our arithmetic)", "(industry-typical)" — and only when
   the existing hedge already means exactly that. Otherwise keep the hedge's own words.
3. Where a body "not public" has a matching bullet under `## Open questions`, the body keeps its hedge
   and may add "(see Open questions)". The reasoning is given once, in Open questions.
4. Never delete, weaken or strengthen a hedge. Never add a hedge to a sentence that had none.

**Example** — `docs/steps/006-stie.md:101`: `An industry-generic recipe for a 200 mm, 130 nm-era fab:`
becomes

```
:::{note}
An industry-generic recipe for a 200 mm, 130 nm-era fab:
:::
```

immediately before the numbered list, which is unchanged. (`docs/steps/013-ns19.md:77` is the same
sentence with "nitride strip" in place of "recipe"; 166 of the 171 step pages contain the phrase.)

**Do not touch.** The sentence's wording, including the colon. The list that follows.

**Find.** `grep -rn "industry-generic\|industry-typical" docs/steps/*.md`;
`grep -rn "we infer\|our reading\|our arithmetic\|our extraction\|not public" docs/steps/*.md`.

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
* **Does:** one line.[^x]
* **Why:** one line.
* **Public numbers:** one to three values with their markers, or "none published".
* **Likely SkyWater tool:** name — existence strong / assignment inference.[^skw-01]
* **Not public:** the one or two biggest unknowns (→ Open questions).
:::
```

2. Four to six bullets, each ≤ 25 words, each condensing a sentence that is already on the page, with
   that sentence's marker and its hedge tag.
3. No new fact, no new number, no new source. Every marker in the box must occur again below it.
4. Nothing from an in-force note: no patent number, no title, no value that only the collapsed note
   gives (§2.6).
5. Make the first sentence of `## What this step is` ≤ 25 words: "`CODE` <verb> <object>".

**Example** — for `docs/steps/006-stie.md` the box is built from `:15` ("the plasma etch that cuts the
isolation trenches into the silicon"), `:30-44` (the depth reading, "about 0.33 µm … our reading, not a
documented fact"[^pdk-04]) and `:269` ("**Trench depth.** No SkyWater document states it …").

**Do not touch.** Everything below it. The box is additive.

**Find.** `grep -L "At a glance" docs/steps/*.md`.

**Kind.** hand, last, then re-read against the page.

#### R-TOOLS — evidence grading buried in run-on bullets
*(report A F4)*

**Applies when** a bullet under `## Machines likely used at SkyWater` contains "Strength:".

**Do.**
1. Keep the tool name as the bullet's bold head.
2. Three sub-bullets, with the original words moved unchanged under the matching label:
   * `*SkyWater says:*` — what the public list or filing says, with its marker;
   * `*Tool exists:*` — the grading of existence;
   * `*Runs this step:*` — the grading of the assignment to this step.
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
  - *SkyWater says:* it lists the bench with "phosphoric" among its chemistries.[^skw-01]
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
1. Step pages: order the bullets Previous / Next / Same module / Depends on / Feeds / Category, and
   label each with that word. Keep every gloss and every link.
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
3. Every row keeps its footnote marker, in the first or the last cell.
4. Units go in the header (`Energy (keV)`). Per-cell units only where the source itself is
   inconsistent, and then say so in the caption (R-CAPTION).
5. A hedge that covers the whole table goes, word for word, in one sentence directly under it. A hedge
   that covers one row goes in a final `Basis` column.
6. Quoted values stay quoted, inside the cell. A value the page does not give is `—`.
7. Numbers, step numbers and years are right-aligned (`---:`); everything else left; never centred.
8. The sentence that draws the conclusion stays as prose after the table.
9. A row whose only source is a patent shown as in force belongs **inside that patent's dropdown**, in a
   table of its own (§2.5, §2.6).
10. Obey the column budget of §1. If the data needs more columns, split the table by key or transpose it.

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

**Applies when** a passage performs two or more arithmetic operations, or takes two or more inputs to
reach a number; or contains "our arithmetic", "our extraction", an inline `=` chain or "≈".

**Do.**
1. Give it an H3: `### How <the quantity> is estimated`.
2. Input table first: one row per input, each with its own footnote marker and the source's own wording
   for the quantity.
3. Numbered list: **one operation per line**, the arithmetic written out, the result of that line in
   bold.
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
class pages today; 0 captions.)

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
1. **Reading-list bullets.** The *head* is the text before the first ` — `.
   * head contains no `{role}`, no `[`, no backtick → wrap the whole head: `[head](<URL>)`;
   * head contains a role or a backtick but exactly one `*italic title*` → link only that span;
   * N markers and exactly N italic titles in the same order → link title *i* to marker *i*'s URL;
   * anything else → leave the bullet alone.
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

**Do.**
1. **Run of 25 links or fewer:** add a table `Step | Code | Name | Role`. `Name` comes from the step
   page's title; `Role` only from the page's own markers and grouped bullets ("main", "alternative",
   the `*also …:*` wording). Right-align `Step`.
2. **Run of more than 25 links:** no table. Keep the page's grouped bullets first and put the run in a
   `{dropdown}` titled "All N steps (links)".
3. **The run itself stays byte-identical**, wherever it ends up.
4. **Placement is a checker contract:**
   * *machine pages* — the run must remain the **first block under `### SKY130 steps assigned to this
     class` that contains a step link and does not start with `* `**. So: dropdown (with the run inside
     it) first, new table **after** it. Verified: table after the run passes; the same table placed
     before the run fails with "steps: page only [], index only [...]".
   * *material pages* — the run must stay in the paragraph directly after a line reading `Steps:`.
     Verified: moving the `Steps:` line and the run together inside a `{dropdown}` passes.
   * *mask pages* — six steps or fewer, one bullet each; nothing to do.
5. **Link text**: make it the step code everywhere (`{ref}`PSG <step-089>``, not `{ref}`089
   <step-089>``). In a table with a `Step` number column, show the number in that column and the code in
   the link. Index cells need only *start* with a link, so the checkers still pass.

**Example** — `docs/materials/process-gases.md:307-309`: a `Steps:` line followed by 142 links. After:
the grouped bullets stay, then

```
:::{dropdown} All 142 steps (links)

Steps:

{ref}`SMAT <step-001>`, {ref}`BOX <step-002>`, …
:::
```

`docs/machines/wet-bench.md:213` is the 40-link machine case (4 main + 36 "*also for a clean or
strip:*").

**Do not touch.** The order of the links, the `*alternative:*` and `*also …:*` markers and their
wording, the `N steps; see …` quick-facts row.

**Find.** `measure_b.py --list` keys `steplink-run-paragraph` (37), `bullet>=8steplinks` (41),
`tablecell>=8steplinks` (46); `grep -rEn '\{ref\}`[0-9]{3} <step-' docs/` for the bare-number links
(1,975 in 11 files).

**Kind.** the link text is scripted; the table is best generated (a `gen_step_tables.py` fed by
`tools/steps.csv` and the index rows) — **blocked until W0d** if generated. Building it by hand is
allowed only for a single page, and then the run must be re-checked against the index.

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

**Do (blocked until W0e).** The main-table restructurings: machines index to `Machine class | Steps`
plus a `{grid}` of cards (needs `check_machines.index_rows` to read a two-column table); materials index
split into `Material | Class page | Role | SkyWater evidence` and `Material | Steps` (needs
`check_materials.Index` to read the Steps cell from a second table, keyed by key rather than by
position). Until then only the cosmetic fix is available: wrap in `{table}` with a caption and
`:widths:` (R-CAPTION).

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
