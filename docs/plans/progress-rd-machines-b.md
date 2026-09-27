# Progress — W3, machine pages batch B

Branch `topic/rd-machines-b`, worktree `.worktrees/rd-machines-b`, cut from `main` at `79de86aa`
(merge base for every check below). Task: `docs/plans/readability-guide.md` §4.2 on the last fifteen
machine class pages in file-name order (`ls docs/machines/*.md | grep -v index | tail -15`):
plasma-etcher-dielectric, plasma-etcher-metal, plasma-etcher-silicon, plasma-nitridation-chamber,
post-cmp-cleaner, pvd-cluster-tool, rapid-thermal-processor, sheet-resistance-metrology,
single-wafer-spin-processor, starting-material, tungsten-cvd, vertical-furnace-anneal,
vertical-furnace-lpcvd, vertical-furnace-oxidation, wet-bench. One commit per page.

## Method (every page)

* Rule order of §4.2: R-INTRO → R-STEPRUN (generator-owned; only `gen_step_tables.py --check`) →
  R-MODELS → R-ENTRIES → R-QUICKFACTS → R-PARA / R-SENTENCE / R-LIST → R-RELATED → R-CAPTION.
  R-LINKS was done site-wide under W0c and is not touched.
* Preservation: `tools/check_preserved.py --base main --allow-regrouped` first, with nothing else;
  then `--allow-deduplicated` for quick-facts copies deleted because the body keeps them (every
  `DEDUPLICATED` line is listed per page); then `--strict-words`, with every lost content word
  accounted for below. No `--allow-added` is used as a blanket: every ADDED item is named per page
  with the rule that adds it. `--allow-dropdown-edits` is never used; no in-force note is touched.
* Marker coverage: `tmp/tools/markcov.py` (git-ignored) splits base and new open text into
  sentences and clauses, pairs every new piece that is not verbatim in the base with the base
  sentence it came from, and flags a lost marker, a marker not in that base sentence, or a hedge word
  missing from the piece. Every flag is read; the per-page line says what they were.
* Caps: `docs/plans/readability/prototypes/measure/measure5.py` from its tracked location (the §1
  caps), plus `tmp/tools/caps.py` for the intro and the quick-facts cells (> 20 words or > 1
  quotation). Before-batch counts are in the batch table at the end.
* Checkers per page: `check_machines`, `check_refs`, `check_inforce`, `gen_step_tables --check`,
  `gen_index_links --check`; `-W` build; tiles at 1280 px and 400 px, read before committing.
* Year cells hold only the year the page gives for that model; a capture, listing, award,
  statement or manufacture date stays in Published figures in the page's words. Where the page gives
  a year with a qualifier ("from 1993", "mid-1997") the qualifier stays in the Year cell. Status
  cells carry only the page's own hedge; `—` where the page gives none. A marker that sat on a
  bare "—" goes on the Model cell instead (review rd-machines-a M6). `:widths:` is not added.
* R-QUICKFACTS is applied only where the removed words are verbatim in the body
  (`DEDUPLICATED`) or are moved into the body with their quotation marks and markers. A cell whose
  over-cap part is numbers in one number-order unit, a hedge word ("about"), or a quotation that is
  on the page only there and has no natural home in the body, is left as it is and listed.
* R-INTRO step 3: the template sentence is deleted, and it is pasted here per page. Its loss of
  `SKY130`, "about" (the preposition) and sometimes "200" ("200 mm-era models") is expected.

## Pages

### 1. `docs/machines/plasma-etcher-dielectric.md` — done

Rules applied: R-INTRO, R-MODELS, R-QUICKFACTS, R-PARA, R-SENTENCE, R-LIST, R-RELATED, R-CAPTION.
No "term by term" passage, so no R-ENTRIES table (the What SkyWater lists paragraph is prose over
the other class's entries; it was only split).

* **R-INTRO.** 142 → 62 words. Kept the "what it is" sentence and "It runs fluorocarbon chemistries
  … what does not." The rest of that sentence ("and in the 200 mm, 130 nm era it was most often a
  capacitively coupled reactor — magnetically enhanced or dual-frequency — rather than the
  inductive sources of silicon and metal etch") moved to the second paragraph of the first H2, with
  its subject restored ("it" → "a dielectric etcher"). Pointer sentence ("The physics and chemistry
  … category page") moved to `{seealso}` word for word. Deleted template sentence: "This page
  describes the class in general, lists representative 200 mm-era models, and then says what
  SkyWater has published about tools of this class (nothing among its production etchers) and which
  SKY130 steps this reference assigns to it." Its one factual clause, "(nothing among its production
  etchers)", is an R-REPEAT deletion: the survivors are the quick-facts row "SkyWater-listed tool"
  ("None among the production etchers") and `### What SkyWater lists`, first sentence ("lists its
  production plasma etchers under "Metal Etch" and "Poly/Silicon Etch" only; it names no dielectric
  etcher").
* **R-MODELS.** Two vendor bullets → a 9-row `Vendor | Model | Year | Published figures` table.
  Year cells: HDP Dielectric Etch Centura "of 1993"; MxP chambers "from 1993"; eMxP+ "in mid-1997";
  IPS Centura "in April 1997"; eMax 300 / IPS 300 "followed in 2000"; Exelan High Performance
  "version of 2001"; 2300 Exelan "of 2000" — all the page's own dates for those models
  (`[^amat-1997]`, `[^amat-300-etch-2000]`, `[^lam-exelan]`, `[^lam-2300-2000]`). Precision 5000:
  Year `—`, because the page dates only its dielectric etch ("from 1989–1990", kept in Published
  figures). Rainbow 45XX: `—`. The 200 mm Rainbow 4520 stays inside the 45XX row, "including the
  200 mm Rainbow 4520", so "including" survives. "300 mm" is written in the eMax Model cell and "200
  mm" before "Rainbow 4520" to keep the page's number order. Remarks under the table: the MERIE
  patent sentence, and **Other vendors.** (TEL DRM and Unity, "no vendor description … retrieved"),
  unchanged.
* **R-QUICKFACTS.** Cells over cap 7 → 4.
  * What it does: the Schaepkens sentence ("selective etching of "a SiO2 layer …" is "a process of
    vital importance …"") moved verbatim, capitalised, to the start of `### Fluorocarbon films and
    selectivity`, with its marker; the cell keeps its first clause, the marker repeated, and a pointer.
  * Plasma source: the Exelan clause (quotation and marker verbatim in the body, DEDUPLICATED) and
    "High-density dielectric etchers were also sold, such as Applied's IPS Centura.[^amat-1997]"
    (body: `### Capacitive …`, "High-density sources were used for dielectrics too: Applied launched
    the Dielectric Etch IPS Centura …"[^amat-1997]) deleted. Still three quotations (MxP+ "MERIE
    chamber", Rainbow "plasma/RIE", "mainly for Oxide Etch"): none is verbatim in the body as a
    quotation string, and moving the Rainbow one would put "mainly for Oxide Etch" twice in one
    paragraph. Left at 19 words.
  * Chemistry: the Rainbow contact-oxide quotation moved verbatim into `### Capacitive …` after the
    45XX recipes, with its marker.
  * SkyWater-listed tool: "Oxford PlasmaLab RIE deprocessing" and "Physical Analysis" deleted
    (DEDUPLICATED; body: What SkyWater lists, last sentence); "the contact, via and nitride-seal
    etch pages" became "the step pages" (body keeps "the oxide contact, via and seal-ring etches" in
    the grade prose of `### SKY130 steps assigned to this class`); pointer added.
  * Left over cap: Selectivity (46 words: numbers of one number-order unit and four "about"),
    Endpoint (two quotations that exist only here as quotation strings, with 387 and 3 in one unit),
    200 mm era (26 words, all dates).
* **R-PARA / R-SENTENCE / R-LIST.** Every paragraph over 100 split at a source or topic seam; every
  sentence over 45 split (semicolons, a colon, a dash pair, ", and showed" → "Oehrlein et al.
  showed"). The downstream-etching sentence (three results, three markers) became a lead-in and
  three plain bullets. "Two kinds of step" (106 words) keeps a 46-word lead and an indented
  continuation. "Fluorocarbon gases" (67) keeps a lead and a continuation paragraph. Strength of the
  evidence split into two paragraphs (80-word target).
* **R-RELATED.** Eight bullets → Category / Machines / Materials / Indexes, every link and gloss kept.
* **R-CAPTION.** The models table has a caption; no `:widths:`.

Caps (measure5, §1): paragraphs > 100 7 → 0; list items > 60 4 → 0; sentences > 45 15 → 0; table
cells > 25 7 → 4 (the three quick-facts cells above and the 2300 Exelan Published-figures cell, two
quotations of 24 words; §1 counts a quotation as one word).

Preservation (`--allow-regrouped`, then `--allow-deduplicated`): no LOST marker, quotation or number
except the template sentence's `200`, `about` (preposition) and `SKY130`. DEDUPLICATED: markers
`lam-exelan`; quotes "Dual Frequency Confined (DFC) technology", "Oxford PlasmaLab RIE
deprocessing", "Physical Analysis". REGROUPED number_order, each read digit for digit: the two
model bullets → table rows (same digits, same order), the Kastenmeier sentence → list, the
Poly/Silicon entries sentence → entries sentence + "The 9400 entry names nitride." ADDED markers,
each a repeat on both halves of a split whose base marker covered both clauses, or on each table row
of the clause it cited: `allwin-rainbow-4500` (Rainbow sentence split at its semicolon),
`amat-1997`×3 (one per table row, less the deleted quick-facts copy), `pat-endpoint-tel` (the CN
sentence, second half now "In the patent, …"), `pat-merie-amat` ×2 (the colon split, and the "It
describes a cooled cathode …" split), `schaepkens-1999` ×3 (the What-it-does cell; "extended this to
nitride."; the semicolon split before "The differences are …"), `skw-01` ×2 (the entries sentence; the grade
prose split at its semicolon), `wodecki-1999` (the endpoint sentence split at its semicolon).
Strict words: every lost content word is from the template sentence, the three deleted quick-facts
clauses above, "followed" (eMax row: the Year column now carries 2000), "whose … version" (the
Exelan row names the "Exelan High Performance"). Marker coverage: 10 flags, all read — the
Kastenmeier lead-in and items (each item keeps its marker), the "usually" of the CN quotation
(stays in the quotation's half), "about" of the Schaepkens and Oehrlein halves (stays with its
number), repeated markers above.

Content problems for the owner: none found.

### 2. `docs/machines/plasma-etcher-metal.md` — done

Rules applied: R-INTRO, R-MODELS, R-QUICKFACTS, R-PARA, R-SENTENCE, R-LIST, R-RELATED, R-CAPTION.
Skipped R-ENTRIES: the "Read term by term" paragraph glosses the materials across both entries
("both entries name …, and the 2300 entry adds niobium; neither names …"), not entry by entry; a
per-entry table would have to quote parts of each entry separately. It was split instead. The
three in-force notes are untouched, and each still follows its own paragraph.

* **R-INTRO.** 132 → 43 words: the "what it is" sentence. "It etches in chlorine chemistries …
  vacuum clean." moved to open the first H2, subject restored ("It" → "A metal plasma etcher").
  Pointer sentence → `{seealso}`. Deleted template sentence: "This page describes the class in
  general, lists representative 200 mm-era models, and then says what SkyWater has published about
  its own tools of this class and which SKY130 steps this reference assigns to it."
* **R-MODELS.** Three bullets → an 11-row table (Lam, then Applied, in the page's order) plus
  **Other vendors.** under it. Year cells: 2300 Versys Metal 2000 (the quick facts' "the 2300
  Versys Metal of 2000"); MxP "from 1993"; Metal Etch DPS Centura 1996; second-generation DPS metal
  chamber July 1997; Metal Etch DPS Plus Centura 1999; Metal Etch DPS 300 2000 — each a year the
  page writes directly after the model's name. `—` for TCP 9600 ("by 1994" is when it was used, kept
  in Published figures), TCP 9600SE ("with a microwave stripper option (1998)"), TCP 9600PTX
  ("… demonstrated (1999)"), TCP 9600DFM ("… applications" (2001)): in those three the page's year
  follows a clause about an option, a qualification or an application, so it stays with that clause
  in Published figures. Precision 5000 `—` ("metal etch from 1989–1990").
* **R-QUICKFACTS.** Cells over cap 7 → 4.
  * What it does: the Lam 9600SE quotation ("meets all requirements …") moved verbatim, as its own
    sentence with its marker, under the models table; the cell keeps its first clause (which had no
    marker of its own).
  * Plasma source: "Earlier parallel-plate tools etched aluminium in "BCl3/CL2 plasmas"." moved
    verbatim to `### Plasma source and chamber`, after the TCP/DPS sentence. Two quotations remain
    (TCP, DPS), neither in the body: left at 22 words.
  * Chemistry: the BCl₃ quotation (DEDUPLICATED) and "N₂ additions give a tapered profile in a TCP
    etcher" (body: Allen and Rickard, `### Aluminium chemistry …`) deleted.
  * Post-etch treatment: the Christie quotation (DEDUPLICATED) and "the microwave stripper Lam
    offered for the TCP 9600SE[^lam-9600se-stripper-1998]" (body: `### Corrosion control …`, "Lam's
    microwave stripper for the TCP 9600SE …"[^lam-9600se-stripper-1998]) deleted; value first.
  * SkyWater-listed tool: the two entries (DEDUPLICATED, blockquote) → "Lam 9600 and Lam 2300
    Versys", plus a pointer.
  * Left over cap: Throughput (29 words, two quotations: moving either breaks the cell's number
    order 45, 35, 9600, 50), 200 mm era (45 words, dates and a quotation found only here, in one
    number-order unit).
* **R-PARA / R-SENTENCE / R-LIST.** Five H3 bodies split at source seams. Split: Chen ("…, and
  that" → "They found that", marker repeated); the AT&T / Allen sentence at ", and"; the MiM
  pointer sentence at its semicolon (wording kept). "Three kinds of metal etch" (167 words, one
  104-word sentence) → "The class covers:" and three plain items, the "— though a 2014 report …
  —" dash material after the list as "A 2014 report, though, records …" (R-SENTENCE step 7), and the
  PDK/TiW sentences split at their semicolon. "Stopping on tungsten plugs …" (94 words, one sentence)
  → lead of two sentences and a continuation (the in-force pointer wording unchanged).
* **R-RELATED**, **R-CAPTION**: as page 1.

Caps (measure5): paragraphs > 100 6 → 0; list items > 60 3 → 0; sentences > 45 11 → 3; table
cells > 25 6 → 3. Left: the Christie sentence (48 words, 30 of them inside three quotations), a
false 56-word flag (measure5 fuses "…as silicon etch." with the next sentence; guide problem 1),
and the grading bullet under `### SKY130 steps assigned`, untouched by rule. Cells: Throughput, 200
mm era, and the 9600DFM row (27 words, three quotations).

Preservation. DEDUPLICATED: markers `wiki-bcl3`, `allen-1994`, `christie-1994`; number 200; quotes
the BCl₃ and Christie quotations and both SkyWater entries. **LOST marker `lam-9600se-stripper-1998`
×1 and number `9600` ×1**: the Post-etch cell's copy of "the microwave stripper Lam offered for the
TCP 9600SE[^lam-9600se-stripper-1998]" was deleted as a copy of the body sentence named above; the
tool cannot reclassify it because the What-it-does sentence, carrying the same marker and "9600",
moved into the body in the same edit (body count +1, quick facts −2). Net count checked by hand: the
body now has both the remark and the Corrosion sentence. ADDED markers: `amat-1997` ×3 (one per
Applied row of the 1989–1997 clause), `chen-1989` (the Chen split). REGROUPED: the two model bullets
→ rows (same digits, same order); the "Three kinds" item → list + paragraph. Template losses:
`about`, `SKY130`. Strict words: every lost content word is from the template sentence or the
deleted quick-facts clauses listed above. Marker coverage: 13 flags, all read — list items keep
their own markers; the "The class covers:" lead-in had none; the MiM and capacitor pointer clauses
had none in the base; the skw-01 of the new SkyWater cell is the cell's own.

Content problems for the owner: none found.

### 3. `docs/machines/plasma-etcher-silicon.md` — done

Rules applied: R-INTRO, R-MODELS, R-ENTRIES, R-QUICKFACTS, R-PARA, R-SENTENCE, R-RELATED,
R-CAPTION.

* **R-INTRO.** 131 → 47 words. The first sentence (46 words) split after "the polysilicon gates"
  with "it cuts" added for the second half (R-SENTENCE step 7). "In the 200 mm, 130 nm era it was
  usually a high-density reactor …" moved into the first H2's second paragraph, subject restored
  ("a silicon and polysilicon etcher"). Pointer → `{seealso}`. Deleted template sentence: "This
  page describes the class in general, lists representative 200 mm-era models, and then says what
  SkyWater has published about its own tools of this class and which SKY130 steps this reference
  assigns to it."
* **R-MODELS.** 8 rows. Year cells: MxP "from 1993"; Silicon Etch DPS 300 2000 ("In 2000 Applied
  announced a Silicon Etch DPS 300"); 2300 Versys Silicon 2000 ("of 2000"). `—` for Precision 5000
  ("silicon etch from 1988" kept in Published figures), Silicon Etch DPS Centura (the page gives two
  dates from two sources, 1996 from the 1997 annual report and 1997 from the 1999 press release;
  both stay in Published figures with their sources), DPS Plus (the page says only that the 1999
  release "introduces" it; the row reads "introduced by that press release", the release being
  named in the row above), Rainbow 44XX, TCP 9400 family. Remarks (three): the DPS II reading
  ("We read … an inference from the name"), the two quick-facts sentences moved here (below), and
  **Other vendors.**
* **R-ENTRIES.** The "Read term by term" sentence → a 3-row table. Status: `—` for the DPS II and
  9400 rows (SkyWater's own words, read without a hedge); the 4400 row carries the page's own
  "we read "Lam 4400" as a Rainbow 4400 … an inference from the model number". The two sentences
  about the list as a whole stay as prose under it.
* **R-QUICKFACTS.** Cells over cap 7 → 5.
  * What it does: "Stanford's TCP 9400 is "for selective etching of silicon and polysilicon"." moved
    verbatim under the models table. 26 words by measure5, one quotation (18 of the words).
  * Chemistry: the reseller gas-line sentence moved verbatim under the models table; its marker
    repeated on the C₂F₆ clause it also covered. 26 words, one quotation.
  * Endpoint: the Hsu quotation moved verbatim to `### Endpoint, soft landing and over-etch`, after
    Hsu's model; "Predictive Endpoint" unquoted in the cell (DEDUPLICATED; the quotation stays in
    the body).
  * SkyWater-listed tool: the three entries (in the blockquote) → their tool names; "gate, trench,
    W/WN" DEDUPLICATED.
  * Left: Plasma source (56 words, three quotations, 13.56 and 10¹² in one number-order unit),
    Wafer handling (29 words, two quotations found only here), 200 mm era (41 words, dates).
* **R-PARA / R-SENTENCE.** Every long H3 body split at source seams; sentences split at semicolons
  (Bell 1997/1996, the DPS dome, the TCP/Stanford sentence, the gate and strip bullets), at ", and
  is turned" ("The layer is turned …"), ", and was by 1999" ("It was by 1999 …"), and ", and the
  polysilicon/oxide selectivity" (Joubert, marker repeated). Four consumables and integration items
  over 60 words → lead + indented continuation.
* **R-RELATED**, **R-CAPTION** as page 1.

Caps (measure5): paragraphs > 100 8 → 0; list items > 60 6 → 0; sentences > 45 15 → 2 (the Tuda
sentence, 50 words of which 17 inside its quotation, and a false flag: measure5 fuses "…main
etch." with the next sentence, guide problem 1); table cells > 25 7 → 7 (five quick-facts cells,
two models cells whose length is their quotations).

Preservation. DEDUPLICATED: quotes "Predictive Endpoint", "gate, trench, W/WN". ADDED quotes:
"Poly/Silicon Etch" (the entries-table caption). ADDED markers, each a repeat on a split or a row:
`allwin-rainbow-4400` (Chemistry cell), `amat-1997` ×2 (the Precision 5000 and MxP rows),
`amat-dps-plus-1999` ×2 (the "It was by 1999" split; the DPS Centura row), `joubert-1997`,
`skw-01` ×2 (entries rows), `vallier-2003`, `wiki-rie`. **LOST number_order ('2000', '300', '300',
'200')**: the DPS 300 row puts the model's "300" before its Year 2000 (the page: "In 2000 Applied
announced a Silicon Etch DPS 300 on the Centura 300 platform, … 200mm"); same four digits, the
Year column interposed, read by hand. REGROUPED: the models bullets → rows, the entries sentence →
rows. Template losses: `200`, `about`, `SKY130`. Strict words: template sentence; "for the DPS
Centura" (the row is that model); "introduces" → "introduced"; "term by term", "entry", "names",
"DPS II" (the entries sentence, now the table); "gate, trench, W/WN" (quick facts). Marker
coverage: 17 flags, all read — model cells whose row's figures carry the marker, table headers,
the "If so" split (the base markers covered the doping clause only), the TUNARCE clause (base
marker before the semicolon).

Content problems for the owner: none found.

### 4. `docs/machines/plasma-nitridation-chamber.md` — done

Rules applied: R-INTRO, R-MODELS, R-QUICKFACTS, R-PARA, R-SENTENCE, R-LIST, R-RELATED,
R-CAPTION. No "term by term" passage (What SkyWater lists quotes one module, then prose).

* **R-INTRO.** 130 → 40 words: the first sentence. The next two sentences ("The nitrogen blocks
  boron …[^pat-rpn-ti][^hattangady-1998] … transconductance.[^lek-2002] The class arrived as a
  production tool around the 130 nm node.[^amat-dpn-2001]") moved unchanged to open the first H2,
  before its first H3 (52 words). Pointer → `{seealso}`. Deleted template sentence: "This page
  describes the class in general, lists representative models, and then says what SkyWater has
  published and which SKY130 step this reference associates with the class."
* **R-MODELS.** 3 rows. All Year cells `—`: the DPN chamber's only date on the page body is the
  copy date of the announcement ("Light Reading's copy is dated 2001-11-28", kept in Published
  figures); the Texas Instruments row is process work (Model `—`, the page's words in Published
  figures); the Trias SPA date is a patent filing date ("filed in 2005", kept). Caption says
  "chambers and process work" because of the TI row. The remark paragraph stays.
* **R-QUICKFACTS.** Cells over cap 6 → 6 by count, but What it does (2 → 1 quotation: "130nm and
  below device designs", DEDUPLICATED) and Plasma source (3 → 1 quotation: "slot plane antenna
  (SPA) plasma source", DEDUPLICATED, words kept; "Decoupled Plasma Nitridation (DPN)" → "DPN",
  the expansion is in `### High-density and decoupled plasma nitridation`) now each hold one
  quotation. Left: Pressure, power and time (five quoted figures), Nitrogen profile (three; "in 10
  s" and "confined …" are only here), Wafer handling (its quotation differs from the body's copy by
  "can be easily integrated"), 200 mm era (two quotations and 130/2001 in one number-order unit).
* **R-PARA / R-SENTENCE / R-LIST.** Three one-sentence enumerations became lists: the Texas
  Instruments patent's three drawbacks, Niimi et al.'s three findings, and the TI group's three
  attractions; in each the single end marker moved to the lead-in before the colon (R-LIST step 1,
  R-TABLE step 3). Splits at semicolons (Ito/Hwang, Hattangady 1995, anneal bullet), at ";
  "The nitrogen ion energy …"" (the quotation now opens its own sentence, marker repeated), at
  ", naming" ("It names …"), "run at" ("The process is run at …") and ", and names" ("The patent
  names …"), and ", and put the limit" ("They put the limit …"). Two integration items → lead +
  continuation.
* **R-RELATED**, **R-CAPTION** as page 1.

Caps (measure5): paragraphs > 100 6 → 0; list items > 60 2 → 0; sentences > 45 13 → 3 (Kraft
55, TI patent 47, Applied patent 46 — each over only by the words inside its quotations); table
cells > 25 5 → 5 (four quick-facts cells, the DPN row's two quotations).

Preservation. DEDUPLICATED: the two quotations above. **LOST number `130` ×1**: the What-it-does
cell's copy of "130nm and below device designs" (DEDUPLICATED as a quotation); the number is not
reclassified because the moved intro sentence ("around the 130 nm node") added a 130 to the body in
the same edit. ADDED markers, each a repeat on a split: `chen-2002-rpn`, `hattangady-1995`,
`kraft-1997`, `lek-2002` (the "Where the nitrogen goes" lead, whose clause the base marker
covered), `pat-pna-amat` ×2, `pat-spa-tel`. Template loss: `SKY130`. Strict words: the template
sentence; "Decoupled" (cell), "naming" → "It names". Marker coverage: 16 flags, all read — the
three lists (marker on the lead-in), the repeats above, model cells.

Content problems for the owner: none found.

### 5. `docs/machines/post-cmp-cleaner.md` — done

Rules applied: R-INTRO, R-MODELS, R-ENTRIES, R-QUICKFACTS, R-PARA, R-SENTENCE, R-RELATED,
R-CAPTION.

* **R-INTRO.** 153 → 59 words. The 59-word first sentence split at its colon ("It scrubs both
  faces …"). "In the 200 mm era it was first a separate double-sided scrubber … dry." moved to the
  end of the first H2's second paragraph, subject restored ("a post-CMP cleaner"). The two pointer
  sentences → `{seealso}`. Deleted template sentence: "This page describes the class in general,
  lists representative 200 mm-era models, and then says what SkyWater has published about tools
  that could serve this purpose and which SKY130 steps this reference assigns to the class." (Its
  "tools that could serve this purpose" is said in full under What SkyWater lists: "lists no brush
  scrubber … Two groups of entries touch the post-CMP clean".)
* **R-MODELS.** Six bullets → 8 rows + **Other vendors.** Year cells: SS-3200 2024 ("the SS-3200
  for 200 mm, launched in 2024"; "launched" is the Year column's meaning, "a current model" kept).
  Everything else `—`: Synergy Integra keeps the quotation "Introduced in 1997" verbatim in
  Published figures (a quotation is not cut to fill a cell; the merged `pecvd.md` does the same);
  "installed by 1999", "1,000th … in 2001" are counts and statements, kept in Published figures.
  "whose integrated cleaner's" → "its integrated cleaner's". SCREEN's single end marker repeated
  on its first row.
* **R-ENTRIES.** The "Read term by term" sentence → 3 rows. Status: "our reading of the words
  only" on "ammonia clean" and "IPA clean" (the page's hedge, which covered both glosses, repeated —
  ADDED hedge `our reading` ×1); "not stated" on "Track" (the page: "what "Track" denotes … are not
  stated"). The rest of that sentence stays as prose ("Which films either clean follows …").
* **R-QUICKFACTS.** Cells over cap 7 → 6 by count. Brush scrubbing: the spin-station clause
  (quotation DEDUPLICATED; body: `### Backside, drying and integration`) deleted, 4 → 3 quotations.
  Chemistries: "TMAH has been studied for post-tungsten-CMP cleaning.[^jolley-1998]" deleted
  (body: `### Chemistry after oxide and tungsten polishes`, Jolley; marker DEDUPLICATED).
  SkyWater-listed tool: "Track ammonia clean", "IPA clean" DEDUPLICATED, pointer added. Left: What
  it does (one 36-word quotation, only here), Megasonics (two quotations with 1, 0.8, 1.0 in one
  number-order unit), Integration (22 words; "dry in/dry out" is quoted in the body only inside a
  longer quotation), 200 mm era (23 words, no quotation, names only).
* **R-PARA / R-SENTENCE.** H3 bodies split at source seams; sentences split at semicolons (OnTrak
  wet track; the category-page/Mesa sentence; Ge et al.; the lithography bullet) and at ", and
  Applied's Mirra Mesa" (Lam/Applied). Three integration items → lead + continuation; the tungsten
  continuation opens "The outlines of the tungsten polishes" (for "those of"), and the oxide half
  repeats "(industry practice)", which closed the whole base sentence.
* **R-RELATED**, **R-CAPTION** as page 1.

Caps (measure5): paragraphs > 100 6 → 0; list items > 60 4 → 1; sentences > 45 12 → 1 (both the
untouched grading bullet under `### SKY130 steps assigned`); table cells > 25 4 → 6 (three
quick-facts cells, and the Synergy Integra, Auriga C and Strasbaugh rows, whose length is their
quotations).

Preservation. DEDUPLICATED: marker `jolley-1998`; quotes "without contacting the wafer surfaces",
"Track ammonia clean", "IPA clean". ADDED markers: `ge-2006` (semicolon split),
`pat-scrubber-ontrak` (OnTrak wet-track split), `screen-ss3200` (SCREEN rows). ADDED hedge: `our
reading` (above). REGROUPED: the models bullets → rows, same digits in the same order. Template
losses: `200`, `about`, `SKY130`. Strict words: the template sentence; "launched" (SS-3200 row);
the three quick-facts deletions; "Read term by term … "Track" denotes" (entries table); "studied",
"TMAH" (Chemistries cell). Marker coverage: 15 flags, all read — model cells, table headers, the
strength split (no marker on "there is no listing of this class", an index statement), the
lithography bullet's first clause (the base marker belonged to the SEZ note clause).

Content problems for the owner: none found.

## Guide problems

1. **`measure5.py` fuses a sentence ending in "…ch."** Its abbreviation guard `(?<!ch\.)` (meant
   for "ch." = chapter) also matches "etch.", "each.", "which.", so a sentence that ends "…the
   etch." is counted together with the next one (plasma-etcher-dielectric, base line 31: a 66-word
   "sentence" that is two). Every etch page is affected; a `\bch\.` guard would fix it. The scripts
   are under `docs/plans/readability/`, so this is a coordinator item.
2. **§1 says a quotation counts as one word, the scripts count every word in it.** Cells made of
   two quotations (2300 Exelan row) are reported over 25 words by `measure5.py`.
