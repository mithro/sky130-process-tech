# Report A — step pages (`docs/steps/*.md`) and the step index

Sampled, source and rendered: 001, 006, 013, 018, 043, 058, 061, 066, 097, 112, 134, 138, 160, 171 and `steps/index`. Phone width (400 px): 006, 018, index. Screenshots: `tmp/readability/shots/a-*`. Counts cover all 171 step pages, body only (no footnote definitions), from the re-runnable `tmp/readability/a-tools/measure*.py`, which also print file:line worklists.

## 0. The pages in numbers

| Measure | Value |
|---|---|
| Words per page | median ≈ 2,750 (1,636–4,813) |
| Share of words in `## References` lists + footnote definitions | median 39 % |
| Prose paragraphs | 1,425; median 53 words, p90 158, max 438 |
| Paragraphs ≥ 120 / ≥ 200 words | 355 (25 %) on 157 pages / 56 on 45 pages |
| Paragraph median in "What this step is" / "Step category" | **120** / 104 words |
| Opening paragraph; first sentence | median 114 words; median 18, 21 pages > 40 words |
| List items outside References ≥ 80 words | 363 on 148 pages (max 373) |
| Sentences | 9,628; median 22 words, p90 51, max 173 |
| Sentences ≥ 40 / ≥ 60 words | 1,917 (every page) / 563 (159 pages) |
| Sentences with ≥ 2 em-dashes; parentheticals ≥ 15 words | 759 (164 pages); 197 (102 pages) |
| Tables besides quick facts; figures; headings below H2 outside References | **0; 0; 0** |
| Footnote definitions / body markers per page | median 30 / 43; up to 15 markers in one paragraph |
| Code spans | 2,600, of which 994 are step codes |

The averages are fine; the tail is the problem. Every page has two to five unskimmable blocks (the evidence essay in "What this step is", the "Step category" paragraph, the longest "Why"/"How" items), and nothing below H2 breaks them up.

---

## 1. Findings catalogue

### F1. Wall-of-text paragraphs and list items — P1, hand edit
**Wrong.** A quarter of paragraphs are ≥ 120 words. At 400 px a 280-word paragraph fills two screens (`a-phone-006-stie-01.png`).

**Before.** `043-gox100.md:26` is one 278-word paragraph covering the PDK thickness quote, SPICE `toxe`, the C–V modules, the area/edge split, two results, the thickness conversion, caveats, the dual-oxide argument and a step-code note.

**After.** Same sentences, same order, split into 4–5 paragraphs of ≤ 80 words, each opening with a bold run-in label ("**PDK thickness.**", "**Measured capacitance.**"); the numbers go in a table (F3).

**Rule.**
1. Paragraph ≤ 100 words and ≤ 5 sentences; aim for 40–80.
2. Split where a new source, quantity or question starts.
3. Never separate a quotation from its attribution or a claim from its footnote marker.
4. List item ≤ 60 words. If longer, keep a lead sentence ≤ 30 words and move the rest into sub-bullets (one fact and footnote each) or an indented continuation paragraph.
5. Reword only as far as the split requires.

**Detect.** `measure.py`; worst: 171:206 (438 words), 134:30, 030:93, 056:73, 149:52, 053:79, 138:25; item 136:92 (373).
**Do not touch.** Quotes, numbers, hedges, order of claims. **Scriptable:** worklist only.

### F2. No structure below H2; evidence essays in "What this step is" — P1, hand edit
**Wrong.** "What this step is" has a median of 283 words (max 1,231; 141 pages exceed 200). The definition takes about 60 words; the rest weighs evidence. Authors faked sub-headings with bold text 36 times on 26 pages.

**Examples.** 138-capme: eight paragraphs and two dropdowns on etch selectivity precede "Why". Bold labels: `006-stie.md:30` "**How deep?**", `134-wtial3.md` "**On the cap.**", `061-p1m.md` "**Alignment.**".

**Rule.**
1. Before the first H3, keep ≤ 2 paragraphs and ≤ 120 words: what is done, what arrives, what leaves, place in the module.
2. Keep the rest in the same H2 and order, under H3s from this vocabulary: `### Key numbers` (table, F3), `### What the public record shows`, `### How <quantity> is estimated` (F5), `### Competing readings`.
3. Turn each paragraph-start bold label into an H3.
4. H3 titles must be unique within a page and must not be "Cross-check", "High-level understanding" or "Deep dive".

H3s are safe: `check_steps.py` only tests that the 13 headings exist; `check_refs.py` reads only `### Deep dive`.

**Detect.** Section word count; `^\*\*[^*\n]{3,80}[.?:]\*\*` outside the index-links block.
**Do not touch.** The 13 mandatory heading strings; dropdown placement (F12).

### F3. Numeric data written as prose or bullets — P1, hand edit from templates
**Wrong.** No page has a table beyond quick facts, yet 97 blocks on 72 pages carry ≥ 5 unit-bearing numbers and ≥ 2 semicolons; 60 blocks on 50 pages recite ≥ 3 design-rule IDs. Five kinds recur:

| Kind | Example | Columns |
|---|---|---|
| Published recipes from other fabs | `018-nwi.md:94` | Source · Species · Energy · Dose · Note |
| Film stacks | `134-wtial3.md:30` | Report (year, technology) · Stack as quoted · Total |
| Design rules | `061-p1m.md:26-41` (six poly rules) | Rule · Constrains · Value |
| Measured against nominal | `171-hpetest.md:178`, `:206`; `066-bhi.md:83`; `030-pwdem.md:93` | Parameter · Geometry · Test tile · PDK nominal · Limits |
| Generic recipe parameters | the 44 pages with a bulleted "How" | Parameter · Typical · Public for SKY130? |

**Before** (`018-nwi.md:94`): "…500, 275 and 130 keV phosphorus in a Harris twin-well flow;[^pat-twin-harris] 700 keV at 2.0 × 10¹³ cm⁻² plus 120 keV at 2.0 × 10¹² cm⁻² in a Hynix flow;[^pat-well-hynix] 850 keV at 5.2 × 10¹³ …"

**After:**
```
* **Energy.** Set by the wanted peak depth. Published retrograde N-wells of the 0.25–0.13 µm era:

  | Source | Energy (keV) | Dose (cm⁻²) |
  |---|---|---|
  | Harris twin-well[^pat-twin-harris] | 500, 275, 130 | — |
  | Hynix[^pat-well-hynix] | 700 + 120 | 2.0 × 10¹³ + 2.0 × 10¹² |
  | IBM[^pat-well-ibm] | 850 / 550 / 50 | 5.2 × 10¹³ / 1.25 × 10¹² / 5 × 10¹¹ |
  | Hynix triple-well, "middle n-well"[^pat-dnw-hynix] | "about 500 keV to about 600 keV" | 5 × 10¹²–2 × 10¹³ |

  For a 1.1 µm well depth[^pdk-03] the deepest `NWI` energy is plausibly 500 keV–1 MeV (inference from range tables).[^txt-01]
```

**Rule.**
1. Use a table when ≥ 3 parallel items each have ≥ 2 attributes.
2. Every row keeps its footnote marker, in the first or last cell.
3. A hedge covering the whole table ("our extraction…", "industry-typical") goes word for word in one sentence directly under it; a row-level hedge goes in a final "Basis" column.
4. Quoted values stay quoted. An unpublished value is "—" or "not public"; never invent one.
5. At most 5 columns; units in the header.
6. The concluding sentence stays as prose after the table.
7. A row citing a patent shown as in force sits in a table inside that patent's dropdown.

**Detect.** `measure3.py`, `measure4.py`.
**Do not touch.** Significant figures, thousands spacing ("1 800 Å"), "about" and "~".

### F4. "Machines likely used at SkyWater": grading buried in run-on bullets — P1, semi-scripted
**Wrong.** All 171 pages grade evidence with a run-in "Strength:" sentence (396 uses: strong 358, medium 34, weak 4). Bolding varies (`013:121` plain, `018:145` bold). Two gradings — the tool exists; the tool runs this step — share one sentence.

**Before** (`013-ns19.md:120`): "…SkyWater lists it with "phosphoric" among its chemistries.[^skw-01] Strength: strong (SkyWater statement) that a hot-phosphoric capable bench exists; the assignment to `NS19` follows from it being the only phosphoric tank listed."

**After:**
```
* **Akrion Gamma batch wet bench (phosphoric)**
  - *SkyWater says:* it lists the bench with "phosphoric" among its chemistries.[^skw-01]
  - *Tool exists:* strong (SkyWater statement).
  - *Runs this step:* inference — it is the only phosphoric tank listed.
```

**Rule.** Every tool item uses these three sub-bullets, with the original wording moved unchanged under the matching label. Omit the third line if the page grades only existence. With ≥ 4 tools, add a recap table (Tool | Evidence) above the list. A full table is worse: long quotes in four columns overflow a phone.

**Detect.** `grep -n "Strength:"`. **Scriptable:** a script splits at "Strength:"; a model assigns clauses.

### F5. Arithmetic and derivations buried in prose — P1, hand edit
**Wrong.** "Our arithmetic" appears 56 times on 42 pages; 24 blocks have inline "=" or "≈" chains; more are spelled out in words.

**Before** (`006-stie.md:36`): one sentence holds two subtractions, the conclusion "so the drawing shows no field-oxide step", and a judgement on `FOXSTEP`. Same pattern: `066-bhi.md:~139` (1.14 µm × tan 7°), `138-capme.md` (0.1 µm at selectivity 2 → 50 nm, stated twice), `134-wtial3.md` (resistivity from 47 mΩ/sq × 0.8 µm).

**After:**
```
### How the trench depth is estimated

| Quantity (PDK stack drawing[^pdk-04]) | Value (µm) |
|---|---|
| `li` bottom | 0.9361 |
| `licon` over `diffusion` | 0.6099 |
| `licon` over `field poly` | 0.4299 |
| `field poly` thickness | 0.18 |

1. Diffusion surface: 0.9361 − 0.6099 = **0.3262 µm**.
2. Field-oxide top: 0.9361 − 0.4299 − 0.18 = **0.3262 µm**.
3. The two are equal, so the drawing shows no field-oxide step. The 0.07 µm `FOXSTEP`[^pdk-03] cannot be combined with it.

Result: about 0.33 µm **only if** the drawing's zero is the trench floor. That is our reading, not a documented fact, and the drawing says "Diagram not to scale!".[^pdk-04]
```

**Rule.**
1. A derivation with ≥ 2 inputs or operations becomes: input table (footnote per input), numbered steps (one operation per line), bold result line, then all original hedges word for word.
2. A single-operation estimate stays inline as its own sentence.
3. If a derivation appears twice on a page, work it once; the other place keeps result, hedge, footnote and "(derived above)".

**Detect.** `our arithmetic|our extraction|≈| = \d`.
**Do not touch.** The numbers. A model that finds a slip reports it and does not fix it.

### F6. Enumerations written as sentences — P1, hand edit
**Wrong.** Parallel items are chained with semicolons. 117 sentences on 95 pages have ≥ 3 semicolons; a noisier heuristic finds about 390 candidates on 152 pages.

**Examples.** `013-ns19.md:69` "Two things can go wrong: over-etching … (which …), and leaving nitride residue (which …)"; `160-vim4e.md:58` "Two things are specific to this instance. At an aspect ratio … And the profile …".

**After** (`013:69`):
```
Two things can go wrong:

* **Field-oxide over-etch** — recesses the exposed field oxide and creates divots at the active edge, where the pad oxide meets the trench liner.
* **Nitride residue** — blocks later oxidations locally.

Both are controlled by …
```

**Rule.**
1. Convert to a colon lead-in plus bullets when the sentence announces a count ("two things", "three reasons", first/second/third), or lists ≥ 3 parallel items of which at least one has its own clause, number or footnote.
2. Each bullet keeps its footnote and opens with a 2–4 word bold label.
3. Lists of ≤ 4 bare nouns stay inline.
4. Numbered lists for sequences only; nest at most two levels.

### F7. "Step category" is one dense paragraph — P1, hand edit
**Wrong.** Median 104 words, max 276, one paragraph. Its job is a single line. `138-capme.md:140` repeats the selectivity argument of `:77-91` almost sentence for sentence.

**Rule.** First paragraph ≤ 35 words: "`X` is a {ref}`<category>` step of the *<class>* class" plus its defining parameter. Then "**Specific to this step:**" and 2–4 bullets holding the remaining sentences. Duplicates of other sections follow F10.

### F8. Long sentences, em-dash chains, nested parentheticals — P2, hand edit
**Wrong.** 563 sentences ≥ 60 words; 759 with ≥ 2 em-dashes, usually wrapping a hedge or second source.

**Examples.** Longest: `161-wtial5.md` (173 words), `056-upri.md` (150), `030-pwdem.md` (144). Typical: `066-bhi.md:16-25`, "It is made through the same resist windows … — we infer that the two share the NTM resist, since … (see below) — but with a tilted beam, so that …".

**Rule.**
1. Aim for ≤ 30 words; split anything over 45.
2. At most one em-dash pair or parenthetical per sentence.
3. A parenthetical ≥ 12 words becomes the next sentence; a hedge begins "We infer this because …".
4. A semicolon joining two cited facts becomes a full stop.
5. Subject and verb within the first 12 words. Markers travel with their clause.

**Detect.** `measure2.py`. **Do not touch.** Quotations; split around them.

### F9. Hedging and scope boilerplate — P2, part scripted
**Wrong.** "Not public" and variants 613 (165 pages); "we infer"/"inference" 798 (169); "our reading/arithmetic/extraction/estimate" 333; "industry-typical/generic" 302; "this reference" 194. The "How" opener "An industry-generic … 200 mm, 130 nm-era fab (SKY130's recipe is not public)" is on 151 pages in varying words. Every hedge must stay; the harm is mid-sentence placement and varied phrasing.

**Rule.**
1. Wrap the existing "How" lead sentences, word for word, in `:::{note}`. Scriptable: the paragraph between the H2 and the first list item when it matches `industry-generic|industry-typical`.
2. Move in-sentence hedges to the sentence end using one of four tags — "(inference)", "(our reading)", "(our arithmetic)", "(industry-typical)" — only when the existing hedge means exactly that; otherwise leave it.
3. Where a body "not public" has a matching Open-questions bullet, the body keeps its hedge and adds "(see Open questions)"; the reasoning is given once.
4. Never delete a hedge.

### F10. Repetition between sections and across pages — P2, hand edit
**Wrong.** 54 pages repeat a ≥ 10-word run in two H2 sections: What↔Machines-at-SkyWater 15 pages, What↔How 12, What↔Open questions 12, What↔Why 9. Across pages, 9 sentences recur verbatim on ≥ 10 pages (gas suppliers on 18, litho track and overlay on 13).

**Example.** `097-ti-tin1.md:173` and `:181` give the Honeywell/JX Metals sentence twice, 8 lines apart.

**Rule.**
1. One home section per fact: suppliers → Resources; tool quotes → Machines at SkyWater; unknowns → Open questions; numbers → Key numbers.
2. Elsewhere, a pointer of ≤ 12 words; the marker stays where the fact is first used.
3. Before removing a duplicate, confirm each of its footnote labels still occurs on the page (`check_refs.py` fails on unreferenced footnotes).
4. Cross-page boilerplate stays, in one standard wording.

### F11. No summary at the top — P1, hand edit
**Wrong.** The first screen is a navigation table and a 114-word paragraph; nothing gives the gist in 20 seconds.

**Rule.**
1. Insert an "At a glance" admonition between quick facts and `## What this step is` (template in §2).
2. 4–6 bullets of ≤ 25 words, each condensing a sentence already on the page with the same marker and hedge tag. No new facts.
3. No in-force patent, number or content (`check_inforce.py` would fail).
4. First sentence of "What this step is" ≤ 25 words: "`CODE` <verb> <object>".

### F12. In-force-patent dropdowns as the reader sees them — P2, part scripted, owner decision
**Wrong.** 93 hand-written dropdowns on 37 pages. Titles have a median of 16 words and render as a two-line bold bar. The same title repeats on a page 44 times over 33 pages. "Collapsed note" pointer prose appears 107 times on 35 pages.

**Examples.** "From a patent shown as in force (US 8,110,414; estimated expiry 2030-01-02) — open to read", four times on 138-capme; "which, the collapsed note above sets out".

**Rule.**
1. Shorten titles to `In-force patent note — US 8,110,414 (est. expiry 2030-01-02)`. Number and date stay in the title, which `check_inforce.py` permits. `sed`-able.
2. For repeated titles append "· note 1 of 3", so pointers can say "(in-force note 2)".
3. Pointer prose becomes one end-of-sentence clause: "(details in the in-force patent note below)".
4. Never move text across a dropdown boundary or paraphrase its content outside. F1, F3, F6 apply inside.

### F13. Generated index-links block — P2, generator change
**Wrong.** On 144 pages it renders as an orphan bold "**Related patents.**" at the foot of "Related steps", with no heading or TOC entry. The link text is the patent number, so readers scan numbers. The 12 count-only pages get one 40-word sentence.

**Change `tools/gen_index_links.py`:**
1. Emit `### Patents, papers and filings about this step` first; it falls under Related, and `check_steps` is unaffected.
2. Format as `{ref}`Title <patent-…>` — US 5,830,375 A (1996)`.
3. Split the count-only sentence into a count line and a link line.
4. Update `--selftest`, then regenerate. Never hand-edit the blocks.

### F14. References: every title is two clicks away — P1, scripted after a rule change
**Wrong.** 4,211 reading-list bullets, 0 with a direct link. 267 are "Wikipedia, *Title*" (all 171 pages); 420 body sentences also cite a `wiki-` footnote, often naming the article. Reading lists and footnote list show the same ~30 sources twice.

**Rule.** Make each tier bullet's head ("Author, *Title*") a link to the first URL in its footnote definition; keep the marker. Where prose names Wikipedia or an article, link the name and keep the marker. Bullets inside in-force dropdowns may be linked.

**Requires:** reversing citation-style rule 5 ("Do not repeat URLs in the bullets"); a check (in `check_links.py` or `check_refs.py`) that every inline URL equals a URL in one of that page's footnote definitions, so link-rot coverage holds; and Wayback fixes applied to definition and bullet together.

### F15. Fixed-pattern sections — P2/P3, hand edit
* **Open questions (P2).** 647 of 667 bullets open with a sentence, not a label. Every bullet opens with a 2–5 word bold label ("**Tilt angle.**") then the existing text. Data-heavy bullets (`018` RSNW; `001` resistivity, 207 words) move their numbers to a table under `### What the public record shows`, keeping question, hedge and pointer.
* **Related steps (P3).** All 171 pages restate Previous/Next; 166 end with "Category page:". Keep the glosses. Order and label bullets: Previous / Next / Same module / Depends on / Feeds / Category.
* **Code formatting (P3).** Code-format searchable identifiers (layers, rules, model parameters, files, step codes). Put numbers and drawing labels (`0.0` at `006:32`) in quotation marks.

### F16. No figures — P1 (see the diagram reviewer)
0 of 171 pages have one. Two would do most: a before/after cross-section per module (one SVG per quick-facts "Phase", about 10, current step highlighted), and a generated flow strip of the 5–9 neighbouring steps ("… → STINITE → **STIE** → DNM → …") from `steps.csv`. Pages needing their own figure: etch profiles, implant tilt and shadowing (065, 066, 068), the MiM stack (135–140, 150–155).

### F17. Step index — P2, generator change
**Wrong.** One flat 171-row table; at 400 px the Category column is clipped (`a-phone-index-01.png`); the sidebar is a flat 171-item list. **`tools/gen_steps.py` is stale:** its `write_index()` lacks the committed intro paragraph and `[^steps-sheet]` footnote, so running it deletes the citation (verified by generating into the scratchpad and diffing).

**Change.** Sync the generator with the committed intro. Emit a `## <Phase>` heading and table for each of the 10 `PHASES`. Use short linked category labels ("Litho", "Implant", "Strip/clean", "CMP"). Optionally one toctree per phase with `:caption:`. Add `--check`.

---

## 2. Page-type guidance: the step page

Mandatory headings unchanged; `+` marks additions.

```
(step-NNN)=
# Step NNN — CODE: Name
| quick-facts table — unchanged |

+ :::{admonition} At a glance
+ * **Does:** one line.[^x]
+ * **Why:** one line.
+ * **Public numbers:** 1–3 values with markers, or "none published".
+ * **Likely SkyWater tool:** name — existence strong / assignment inference.[^skw-01]
+ * **Not public:** the 1–2 biggest unknowns (→ Open questions).
+ :::
+ (optional generated flow strip / shared module cross-section)

## What this step is                 ≤ 2 paragraphs, ≤ 120 words; first sentence ≤ 25 words
+ ### Key numbers                    table: Quantity · Value · Source · Basis
+ ### What the public record shows   short paragraphs; measured-vs-nominal tables
+ ### How <x> is estimated           input table, numbered arithmetic, hedged result
## Step category                     one classification sentence, then "Specific to this step:" bullets
## Why this step exists              1–2 lead sentences; 3–5 labelled bullets ≤ 60 words;
                                     studies as sub-bullets "Author (year) — finding.[^x]";
                                     keep the closing "Without `X` …" paragraph (on 105 pages; it works)
## How it is typically performed     :::{note} scope lead, word for word :::
                                     numbered list for sequences (127 pages); parameter table or
                                     labelled bullets for parameter sets (44 pages);
                                     SkyWater-specific statements in a final short paragraph
## Machines typically used           bullets ≤ 40 words: class link, then example models
## Machines likely used at SkyWater  three-line items (F4)
## Resources required                bullets; supplier sentence once, last
## Related steps and cross-references   labelled bullets (F15)
+ ### Patents, papers and filings about this step   generated (F13)
## References                        three tiers, linked heads (F14); keep `* ` bullets
## Open questions                    labelled bullets (F15); in-force notes last
<!-- footnotes -->
```

| Form | Use it for |
|---|---|
| Table | Any ≥ 3 × 2 parallel data: recipes, stacks, rules, measured against nominal, derivation inputs. Not the reference tiers (`check_refs.py` counts `* ` under "Deep dive"). |
| Numbered list / bullets | Sequences and arithmetic steps / reasons, failure modes, tools, resources, unknowns |
| Admonition | "At a glance" and the "How" scope note; at most 2 per page |
| Dropdown | **Only** in-force-patent notes. The collapsed look is the reader's "patent in force" signal and `check_inforce.py` inspects every dropdown. |
| Figure | Module cross-sections, tilt/shadow geometry, flow strip |

| Element | Target |
|---|---|
| Paragraph | 40–80 words; cap 100 |
| List item | ≤ 60 words |
| Sentence | ≤ 30 words; cap 45; ≤ 1 dash pair or parenthetical |
| Footnote markers per paragraph | ≤ 6; more means it is a table |
| Words before the first H3 or list in an H2 | ≤ 120; 3–6 H3s per page |

**Order of work per page.** F2 → F3, F5 → F6, F7 → F1, F8 → F4, F15 → F11 (written last, from the finished page) → `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`, build with `-W`.

**Acceptance check, every page.** The multiset of footnote markers and the sets of numbers and quoted strings must be identical before and after. A diff script over `\[\^[^\]]+\]`, digit runs and quoted strings is cheap and should be mandatory.

---

## 3. Risks and open questions for the coordinator

1. **`gen_steps.py` is stale (F17).** Fix before any index work.
2. **Direct links in reference bullets (F14)** contradict citation-style rule 5 and escape `check_links.py`. Owner decision plus a checker extension; the change readers will notice most.
3. **Generated-block heading and link text (F13):** generator change, selftest update, 144 pages regenerated in one commit.
4. **Dropdown titles (F12).** `check_inforce.py` exempts the title line and does not appear to constrain its wording, but "shown as in force … open to read" looks like the owner's phrasing. Confirm, and test the expired-family reverse report.
5. **"At a glance" repeats facts by design.** It must repeat hedges and avoid in-force content. Consider a checker: box present, ≤ 6 bullets, every marker in it also occurs below.
6. **Tables.** Footnotes in cells already work (quick facts). Tables inside list items need a blank line and consistent indentation; build one page under `-W` first. New H3s get slugs (`myst_heading_anchors = 3`), so keep titles unique per page.
7. **Re-presented arithmetic (F5) will expose slips.** Instruction: report, do not fix.
8. **Source defect:** `160-vim4e.md:74-76` is a list continuation that lost its indentation. It renders, but will trip a mechanical splitter; normalise indentation before scripted passes.
9. **Moving sentences between H2 sections is the riskiest operation** (F7, F10, F15). Allow it only within F10's home-section map, with the acceptance check on every page.
