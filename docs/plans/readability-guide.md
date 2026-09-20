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
step pages; the same grep on `docs/masks/*.md` finds the 208 mask run-ins of B8. Section word counts come
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
