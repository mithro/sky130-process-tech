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

### 6. `docs/machines/pvd-cluster-tool.md` — done

Rules applied: R-INTRO, R-MODELS, R-ENTRIES, R-QUICKFACTS, R-PARA, R-SENTENCE, R-LIST, R-RELATED,
R-CAPTION.

* **R-INTRO.** 143 → 37 words: the first sentence. The next two ("Several single-wafer chambers —
  … — sit around robots …"; "Within the class the chambers differ … ({term}`IMP`).") moved unchanged
  to the end of the first H2's lead, as its own paragraph. Pointer → `{seealso}`. Deleted template
  sentence: "This page describes the class in general, lists representative 200 mm-era models, and
  then says what SkyWater has published about its own tool of this class and which SKY130 steps
  this reference assigns to it."
* **R-MODELS.** Four bullets → 10 rows + three remarks (the litigation sentence, **Varian.**,
  **Other vendors.**). Year cells: Endura "April 1990", Endura HP 1993 and VHP 1994 ("the Endura HP
  and VHP of 1993 and 1994", respectively — digits checked), HP Metal options "from December 1996",
  300 mm INOVA xT 2000 ("of 2000"): each the page's own year for the model. `—` for the Liner/Barrier
  system ("by 2000" is a shipment count's date, kept in Published figures), Vectra IMP, Endura SL,
  SIP chamber, INOVA. The Endura's "today" description moved into its row (same bullet, no digits).
* **R-ENTRIES.** The "Read term by term" list → 6 rows grouped as the page groups them ("two
  titanium nitride processes" one row; "tungsten nitride, cobalt, niobium and silicon dioxide" one
  row). Status "our reading" on the ESC/Imp row only (the page's hedge sits on that reading); `—`
  elsewhere. "The page does not expand "ESC" or "Imp"." stays as prose under the table.
* **R-QUICKFACTS.** Cells over cap 7 → 7 by count, three improved. What it does: the second
  Wikipedia quotation ("Sputtering is used extensively …") moved verbatim to open the first H2
  (21 words, one quotation, marker kept on both). SkyWater-listed tool: 11 → 1 quotation — the ten
  sub-entries are written unquoted (DEDUPLICATED as quotations; the blockquote keeps them) so that
  the cell keeps its `{term}` link on ESC. Left: Sources, Platform, Films, Bottom coverage, 200 mm
  era — each a run of quotations and numbers found only there (Platform's two quotations are
  longer than the body's copies, so they are not the same strings).
* **R-PARA / R-SENTENCE / R-LIST.** "What makes a machine a production PVD cluster tool … :" and
  the staged-vacuum patent's four features became lists (the patent's single marker on its
  lead-in). The Vectra IMP sentence (three quotations separated by semicolons) became four
  sentences, the marker on each; the liner-system, Rossnagel–Hopwood, Nishimura, HCM, Cypress and
  top-plate sentences split at their semicolons or at ', and "The sequential …"'. "In its
  description" → "In the patent's description" (new paragraph). Items over 60 → lead +
  continuation.
* **R-RELATED**, **R-CAPTION** as page 1.

Caps (measure5): paragraphs > 100 11 → 0; list items > 60 5 → 0; sentences > 45 16 → 1 (Varian's
patent sentence, 51 words, 34 of them inside its two quotations); table cells > 25 5 → 6 (four
quick-facts cells, the INOVA row, the ESC/Imp row).

Preservation. DEDUPLICATED: number 200 (quick facts). **LOST quote 'TiN' / ADDED quote 'ESC
TiN'**: the old cell wrote `"{term}`ESC` TiN"`, which the tool reads as the quotation "TiN"; the
entries table writes "ESC TiN" as the blockquote does. ADDED quotes: "AMAT PVD Metal" (the
entries-table caption). The table's other Entry quotations replace the cell's quoted copies one for
one. ADDED identifier `SiO2` (the unquoted cell list). ADDED markers: `amat-1997` ×3 (Endura, HP,
VHP rows of one clause), `amat-ism-2000` ×5 (the Vectra split ×3, the liner-system split, the
Vectra IMP row), `rossnagel-1993` (split), `skw-01` (the grade prose "They grade …"),
`wiki-sputter` (the What-it-does split). Template losses: `about`, `SKY130`. Strict words: the
template sentence; "Read term by term" (now the table). Marker coverage: 32 flags, all read — list
items (marker on lead-in), model cells, table headers, and split halves whose own clause carries a
hedge ("not public", "(inference)") or a cited source.

Content problems for the owner: none found.

### 7. `docs/machines/rapid-thermal-processor.md` — done

Rules applied: R-INTRO, R-MODELS, R-PARA, R-SENTENCE, R-LIST, R-RELATED, R-CAPTION. Skipped
R-ENTRIES: the page quotes one entry and glosses its parts; a table would put new quotation marks
around parts of SkyWater's single quotation. Skipped R-QUICKFACTS on every cell (below).

* **R-INTRO.** 123 → 65 words: the two "what it is" sentences kept; the pointer sentence →
  `{seealso}`. Deleted template sentence: "This page describes the class in general, lists
  representative 200 mm-era models, and then says what SkyWater has published about its own tool
  of this class and which SKY130 steps this reference assigns to it."
* **R-MODELS.** Three rows + three remarks (the 2002 sale and Plasma-Therm; the Gronet and Gibbons
  patent and the April 1997 suit, "The lamp …" and "Its …" given their noun, "Applied's"; **Others.**).
  Year cells: RTP XE Centura 1997 ("launched in 1997"). RTP Centura `—`: its year is inside the
  quotation "entered the fast-growing RTP market in 1995", which is not cut. AG row `—` (families).
* **R-QUICKFACTS.** Not applied: all seven over-cap cells are runs of quotations and figures that
  appear only in the quick facts, or are longer or shorter than the body's copies (Uniformity's
  Gronet quotation is also in the body, but deleting it drops "approximately" and breaks the cell's
  number order 3, 8, 1150, 8800, 5, 8108, 1150, 5).
* **R-PARA / R-SENTENCE / R-LIST.** H3 bodies split at source seams. The Gronet and Gibbons
  sentence (three quoted features) → lead-in and three items, marker on the lead-in. Splits at
  '; "To provide cold-wall …' (a quotation-only sentence), ", and offers" ("It offers …"), the
  Mattson semicolon, ", and none of them", the grade-prose semicolon. "Rapid thermal oxidation and
  nitridation" (99 words) and two integration items → lead + continuation.
* **R-RELATED**, **R-CAPTION** as page 1.

Caps (measure5): paragraphs > 100 7 → 0; list items > 60 4 → 0; sentences > 45 8 → 3 (the
Heatpulse lamp sentence 58, Deaton 48, the Mattson sale 47 — each over only by the words inside its
quotations); table cells > 25 7 → 7 (the quick facts, untouched).

Preservation. DEDUPLICATED: number 200 (quick facts' "200 mm era" row label is not touched; the
template sentence's "200 mm-era"). ADDED markers, each a repeat on a split: `ag-8800`,
`amat-1997` (the RTP XE row), `mattson-metron-2002`, `plasmatherm-ag`, `skw-01`. REGROUPED: the
models bullets → rows and remarks. **LOST number_order** none; the AG bullet's digits (4100, 8108,
8800 | 2002, 4000, 8000, 2000, 3000 | 8800, 8108) are read in the same order across the AG row and
the first remark, with the two Applied rows between them (checked by hand). Template losses:
`about`, `SKY130`. Strict words: the template sentence; "launched" (the Year column). Marker
coverage: 10 flags, all read — the list items (marker on lead-in), model cells, "None of them
describes …" (the base markers sat before that clause).

Content problems for the owner: none found.

### 8. `docs/machines/sheet-resistance-metrology.md` — done

Rules applied: R-INTRO, R-MODELS, R-PARA, R-SENTENCE, R-RELATED, R-CAPTION. No "term by term"
passage (SkyWater lists no tool of the class). R-QUICKFACTS skipped (below). The generated
46-step dropdown under `### SKY130 steps assigned` is untouched.

* **R-INTRO.** 135 → 22 words: "An implanter reports the dose … Two instrument families do this in
  line." The three sentences that describe the families (four-point probe, thermal-wave monitor,
  eddy-current gauges) moved unchanged to open the first H2, directly before "Both families measure
  a proxy." (70 words). Pointer → `{seealso}`. Deleted template sentence: "This page describes the
  classes, lists representative 200 mm-era models, and then says what SkyWater has published and
  which SKY130 steps this reference assigns to the class."
* **R-MODELS.** Three bullets → 7 rows. Year cells: RS75 series 1995 ("the RS75 series of 1995"),
  Therma-Probe 1985 ("introduced in 1985", unquoted), BX-10 2000 (the year after its name). `—`
  for the Therma-Probe 500 (its date is inside the quotation "introduced in July of 1996", which is
  not cut), RS-100 ("described on a 2002 capture" kept in Published figures), the OmniMap family
  and NC110.
* **R-QUICKFACTS.** Not applied: the seven over-cap cells are quotations and figures that are not
  in the body as the same strings (What it does, Modulated reflectance, Dose range, Speed,
  Requirement at 130 nm) or dates and names only (200 mm era, 26 words), and the Dose-range, Speed
  and 200 mm cells hold several numbers in one number-order unit.
* **R-PARA / R-SENTENCE.** H3 bodies split at source seams; sentences split at semicolons (Smits,
  the Therma-Wave patents) and at " and described" ("They described a double-implant technique
  …", marker repeated). Two integration items → lead + continuation; the e-test sentence split at
  its semicolon and at ", and the public test tile" (the "on this reference's reading" stays in its
  own clause). Left unsplit: "The nearest entries are the implanters, …" (57 words by measure5,
  about 45 counting each quotation as one word): its trailing "(our reading)" would have to be
  repeated on the implanters' half, which states SkyWater's own dose ranges.
* **R-RELATED**, **R-CAPTION** as page 1.

Caps (measure5): paragraphs > 100 3 → 0; list items > 60 3 → 0; sentences > 45 8 → 1 (above);
table cells > 25 6 → 6 (quick facts, untouched).

Preservation. DEDUPLICATED: number 200 (the template sentence's "200 mm-era"). ADDED markers:
`smith-1986` (split), `tencor-rs75-1995` (the RS75 row; the OmniMap row keeps the base's).
REGROUPED: the models bullets → rows, same digits in the same order. Template loss: `SKY130`.
Strict words: the template sentence; "including" (the RS75 row), "introduced" (the Therma-Probe
Year cell). Marker coverage: 8 flags, all read — model cells, the e-test halves (the base marker
belonged to Perloff's finding), the Related-pages bullet (no markers in the base either).

Content problems for the owner: none found.

### 9. `docs/machines/single-wafer-spin-processor.md` — done

Rules applied: R-INTRO, R-MODELS, R-ENTRIES, R-QUICKFACTS, R-PARA, R-SENTENCE, R-LIST, R-RELATED,
R-CAPTION.

* **R-INTRO.** 168 → 54 words: the first sentence, split at its colon ("It holds one wafer …").
  The second sentence ("Because a gas cushion … after etch or polish.", 56 words) moved to the
  end of the first H2's lead and split at ", which makes" → "This makes the class …" (R-SENTENCE
  step 7). Pointer → `{seealso}`. Deleted template sentence: "This page describes the class in
  general, lists representative 200 mm-era models, and then says what SkyWater has published about
  its own tools of this class and which SKY130 steps this reference assigns to it."
* **R-MODELS.** Three bullets → 5 rows + three remarks (the SEZ 223 sentence moved from the quick
  facts; **SEZ,** Villach and the 2007 Lam tender; **Other vendors.**). Year cells: Spin-Processor
  223 1999 ("introduced in 1999", unquoted), 8200 2001 ("the 8200 of 2001"), SP-2100 2020 ("of
  2020"). `—` for the 4200 and for the Da Vinci family (its date is inside the quotation "Having
  sold the first Da Vinci tool in Q2 04", not cut).
* **R-ENTRIES.** The "Read term by term" sentence → 5 rows. Status "we read" (the page's words) on
  "SEZ223", "DSP+HF" and "titration controlled"; `—` on "Davinci" (the page: "matches") and "HF".
  The rest of the paragraph stays as prose.
* **R-QUICKFACTS.** Cells over cap 7 → 6 by count. What it does: "SEZ introduced its
  Spin-Processor 223 "for high throughput …" …" moved verbatim under the models table; the cell
  keeps its first sentence (which had no marker of its own). SkyWater-listed tool: the entry's
  quotation DEDUPLICATED (blockquote), 3 → 2 quotations. Left: Wafer holding (one 43-word patent
  quotation, longer than the body's excerpts), Dispense and spin-off (three quotations only here,
  with no subject to stand as a body sentence), Chemistries, Throughput, 200 mm era (quotations and
  figures only here).
* **R-PARA / R-SENTENCE / R-LIST.** "What makes a machine a production spin processor …:" → four
  items. H3 bodies split at source seams; sentences split at semicolons (the SEZ patent, the
  Gaulhofer figures) and at ", and explains" ("It explains …"), ", and traced" ("They traced …"),
  ", and later removed" ("They later removed …"). "Their post-etch residue cleans" (new paragraph)
  → "Gaulhofer et al.'s …". Four integration items → lead + continuation.
* **R-RELATED**, **R-CAPTION** as page 1.

Caps (measure5): paragraphs > 100 7 → 0; list items > 60 5 → 0; sentences > 45 12 → 2 (the
untouched grading bullet; a Related-pages false flag, reviewer checklist item 12); table cells >
25 4 → 5 (three quick-facts cells; the 223 and Da Vinci rows, whose length is their quotations).

Preservation. DEDUPLICATED: number 200 (template sentence); quote "SEZ223, Davinci, HF, DSP+HF,
titration controlled". ADDED quote: "Single Wafer" (the entries-table caption). ADDED markers:
`oinoue-2018`, `pat-spin-sez` ×2, `sez-polymer-1999` (splits), `sez-8200-2001` (the 4200 and 8200
rows of one sentence). **number_order**: the SEZ bullet's digits read in the same order through the
rows, except that the SCREEN row now stands between the Da Vinci row and the SEZ remark (2007,
1,200) — reported REGROUPED by the tool, checked by hand. Template losses: `about`, `SKY130`.
Strict words: template sentence; "introduced" (Year cell); "their" (noun restored); "read", "term"
(entries table); the quick-facts entry. Marker coverage: 9 flags, all read — model cells, table
headers, entry rows whose Status column carries the hedge, the BFR split (the base marker belonged
to the patent clause).

Content problems for the owner: none found.

### 10. `docs/machines/starting-material.md` — done

Rules applied: R-INTRO, R-MODELS, R-QUICKFACTS, R-PARA, R-SENTENCE, R-LIST, R-RELATED, R-CAPTION.
Skipped R-ENTRIES (one entry, "Scribe: Lumonics Superclean", glossed in two clauses). The three
in-force notes are untouched; each still follows the text it belongs to (the first follows the
quick-facts table, so the `{seealso}` goes after that note, not between table and note).

* **R-INTRO.** 170 → 68 words: "A fab does not grow or polish its own silicon." and the sentence
  naming the three machines, as a lead-in and three items ("on them" → "on the wafers", its noun
  restored because the sentence it pointed back to moved). "Crystal pulling, slicing, lapping and
  polishing … written specification." moved to open the first H2. The pointer sentence (three
  pointers) → `{seealso}`, split at its semicolons. Deleted template sentence: "This page describes
  that group in general, lists representative 200 mm-era models, and then says what SkyWater has
  published about its own tools of this class and which SKY130 step this reference assigns to it."
* **R-MODELS.** Two bullets → 5 rows + three remarks (**Sorters.**, **At the wafer vendor.**, and
  **Lumonics / GSI Lumonics WaferMark.**, the in-force pointer, which stays directly above its
  note; its "below this list" became "below", R-DROPDOWN step 3). All Year cells `—`: "evaluated in
  1993" is a study date, "of 1995 vintage" a manufacture date (review H1), and no other row has a
  model year. Vendors as the page attributes them: "Tencor / KLA-Tencor" (the page's group head),
  "KLA" for the restarted Pro models, "Thinklaser USA" for the SigmaClean.
* **R-QUICKFACTS.** Cells over cap 6 → 5. What it does: the KLA "Industry standard for wafer
  qualification …" sentence moved verbatim into `### Laser surface scanners`, and the SEMI M12
  "links the properties …" sentence into the SEMI paragraph of `### Laser marking`, each with its
  marker. Left: Surface inspection and Sorting (quotations only here), Marking (it carries the
  pointer the first in-force note answers: "see the collapsed note under this table"; not
  touched), Standards and 200 mm era (quotations and figures only here).
* **R-PARA / R-SENTENCE / R-LIST.** Long H3 bodies split at source seams. The COP studies (Ishii,
  Miyazaki) → lead-in and two plain items ("and Miyazaki et al. that" → "Miyazaki et al. found
  that"). Splits: the PSL sentence at its colon (Liu's marker repeated on the first half), Ryuta at
  ", corresponding to" ("They correspond to …"), the SEMI M12/M13 semicolon, the strength
  semicolon, the integration items at their semicolons, and ", so the incoming scan" ("So the
  incoming scan …", R-PARA step 2). The in-force pointer sentences outside the notes keep their
  wording.
* **R-RELATED** with a **Steps.** label for the SMAT link; **R-CAPTION** as page 1.

Caps (measure5): paragraphs > 100 8 → 0; list items > 60 4 → 1 (the untouched grading bullet);
sentences > 45 17 → 8 (Liu 64, SEMATECH 47, Wacker 46, Christ 56, Infineon 52, the sorter 46 — each
over only by the words inside its quotations; a 62-word sentence inside an in-force note, which
measure5 counts and this pass may not edit; the Open-questions model-list bullet, 48, unchanged);
table cells > 25 6 → 7 (five quick-facts cells, the KLA Pro and SigmaClean rows).

Preservation. DEDUPLICATED: number 200 (template sentence). ADDED markers: `liu-1993`,
`ryuta-1990` (splits). REGROUPED: the models bullets → rows, same digits in the same order. Template
losses: `about`, `SKY130`. Strict words: the template sentence ("group", "describes"); "list" (the
pointer); "corresponding" ("They correspond"); one "Surfscan" (the bullet head, now the rows'
model names). Marker coverage: 15 flags, all read — the intro list (no markers in the base),
model cells, the integration halves that carry their own "not public" or "(our reading)".

Content problems for the owner: none found.

### 11. `docs/machines/tungsten-cvd.md` — done

Rules applied: R-INTRO, R-MODELS, R-QUICKFACTS, R-PARA, R-SENTENCE, R-RELATED, R-CAPTION. Skipped
R-ENTRIES: the "Read term by term" gloss is one sentence over the entry and its two sub-entries,
with the reading of "PECVD" and "PNL" as prose; a table would add quotation marks around parts
of the entries.

* **R-INTRO.** 159 → 59 words: the first sentence and the process sentence up to "from its walls
  inward" (split at its semicolon). "The film on the field is polished away afterwards, leaving the
  plugs." and "The main tools of the 200 mm era …" moved to a paragraph at the end of the first H2's
  lead. Pointer → `{seealso}`. Deleted template sentence: "This page describes the class in
  general, lists representative 200 mm-era models, and then says what SkyWater has published about
  its own tool of this class and which SKY130 steps this reference assigns to it."
* **R-MODELS.** Two bullets → 7 rows + two remarks (the Novellus sentence moved from the quick
  facts; **Other vendors.**). Year cells: Precision 5000 WCVD 1989 (the page's "(1989)" after the
  name, and "of 1989" in the body), Concept One-W "September 1990" ("introduced in September
  1990"), Concept Two Altus 1993 ("of 1993"). `—` elsewhere; "certified by Sematech in 1993", "by
  1997" stay in Published figures.
* **R-QUICKFACTS.** Cells over cap 6 → 6 by count; What it does 36 → 24 words (the Novellus
  sentence moved under the models table) and Chemistry 38 → 27 (the McConica rate-law quotation,
  DEDUPLICATED; body `### Chemistry and kinetics`), one quotation each. Left: Pressure and
  temperature, Nucleation (its "approximately 1000 Å thick" is in the body, but deleting it drops the
  hedge "approximately" and a number from the cell's order), Wafer handling, SkyWater-listed tool
  (the sub-entries are quoted in the blockquote with their dashes, so not the same strings).
* **R-PARA / R-SENTENCE.** H3 bodies split at source seams; splits at semicolons (Wikipedia's
  by-product sentence; the WxZ/Sprint sentence), at ", and the scheme" (Kaanta), ', and "A previous
  problem …"' (a quotation-only sentence), ", and an Applied Materials patent", and the 82-word PNL
  patent sentence into three ("It states …", "In one arrangement it runs …"). "Its
  backside-protection patent" (new paragraph) → "Novellus's …". "A liner first": ", because" →
  ". This is because …"; its 20-word parenthetical of step links stands as its own parenthetical
  sentence after it (R-SENTENCE step 7), before the Saito sentence.
* **R-RELATED**, **R-CAPTION** as page 1.

Caps (measure5): paragraphs > 100 8 → 0; list items > 60 2 → 0; sentences > 45 13 → 3 (Saito 54,
the backside patent 56, the multi-station patent 53 — each over only by the words in its
quotations); table cells > 25 5 → 5 (four quick-facts cells, the Concept Two Altus row).

Preservation. DEDUPLICATED: marker `mcconica-1986`; the rate-law quotation. **LOST number `200` ×1**:
the template sentence's "200 mm-era"; the tool cannot reclassify it because the moved intro
sentence ("The main tools of the 200 mm era …") added a 200 to the body. ADDED markers, each a
repeat on a split or a row: `amat-ism-2000` ×2, `novellus-history` ×2, `novellus-wcvd-1998`,
`pat-pnl-novellus` ×2, `wiki-wf6`. REGROUPED: the models bullets → rows, same digits in the same
order. Template losses: `about`, `SKY130`. Strict words: template sentence; "introduced" (Year
cell); the rate-law quotation's words (quick facts). Marker coverage: 11 flags, all read — model
cells, split halves whose base marker sat on the other clause ("The scheme …", "The page does not
explain "PECVD".", the liner halves), and "approximately"/"may", which stay in their own
quotations.

Content problems for the owner: none found.

### 12. `docs/machines/vertical-furnace-anneal.md` — done

Rules applied: R-INTRO, R-MODELS, R-PARA, R-SENTENCE, R-RELATED, R-CAPTION. Skipped R-ENTRIES:
the gloss is two clauses over three entries ("argon and nitrogen anneals up to 1150 °C, and an
alloy …"); a table would repeat the three quotations, their numbers included. Skipped
R-QUICKFACTS: every over-cap cell is quotations and figures in one number-order unit, or found
only in the quick facts (Ambients' two quotations are in the body, but removing them drops 5 and
10 from the cell's number order).

* **R-INTRO.** 134 → 63 words: the first sentence and "In a 130 nm flow its main task is the
  hydrogen alloy — … interface." (the second sentence split at "— and it is"). "It is the batch
  alternative to rapid thermal annealing for higher-temperature anneals" moved to the end of the
  first H2's lead, subject restored ("An anneal furnace is …"). Pointer → `{seealso}`. Deleted
  template sentence: "This page describes the class in general, lists representative 200 mm-era
  models, and then says what SkyWater has published about its own furnaces and which SKY130 steps
  this reference assigns to the class."
* **R-MODELS.** Four bullets → 7 rows; the category-page remark stays. All Year cells `—`: the page
  gives no model year ("sold on to Tetreon Technologies in 2004" is a sale, kept in Published
  figures). Vendor "SVG Thermco, later Aviza Technology" as the page groups it.
* **R-PARA / R-SENTENCE.** Long H3 bodies split at source seams. The Wikipedia sentence (87 words
  by measure5) split after "the high-temperature anneals" with the neutral lead-in "In its words,"
  before the lower-case quotation (R-SENTENCE step 7). Splits at semicolons (Ohashi, the well
  anneal, forming gas / Illinois, Lyding / Kizilyalli, three integration items) and at ", and a slow
  ramp".
* **R-RELATED**, **R-CAPTION** as page 1.

Caps (measure5): paragraphs > 100 6 → 0; list items > 60 1 → 0; sentences > 45 10 → 3 (Ohashi 58,
over only by its quotations; a false 70-word flag, measure5 fusing "…oxygen and torch." with the
next sentence, guide problem 1; the untouched grading bullet); table cells > 25 5 → 5 (quick facts).

Preservation. DEDUPLICATED: number 200 (template sentence). ADDED markers: `ohashi-2007`,
`wiki-furnace` (splits). REGROUPED: the models bullets → rows. Template losses: `about`, `SKY130`.
Strict words: the template sentence only. Marker coverage: 10 flags, all read — model cells, halves
whose base marker sat on the other clause ("A slow ramp …" is the category page's; "A well anneal
is …" carries no source in the base either), and hedge words that stay inside their quotations.

Content problems for the owner: none found.

### 13. `docs/machines/vertical-furnace-lpcvd.md` — done

Rules applied: R-INTRO, R-MODELS, R-ENTRIES, R-QUICKFACTS, R-PARA, R-SENTENCE, R-LIST, R-RELATED,
R-CAPTION. The two in-force notes are untouched; the first follows the quick-facts table (whose
Pressure row points to it), so the `{seealso}` goes after that note.

* **R-INTRO.** 139 → 50 words. The first sentence (51 words) split at its colon: the definition
  stays; the hardware list moved to open the first H2 as "The furnace has a quartz tube …"
  (subject and verb added at the split, R-SENTENCE step 7). "It deposits the conformal thermal
  films …" stays. Pointer → `{seealso}`. Deleted template sentence: "This page describes the class
  in general, lists representative 200 mm-era models, and then says what SkyWater has published
  about its own furnaces and which SKY130 steps this reference assigns to the class."
* **R-MODELS.** Four bullets → 8 rows; the single-wafer remark stays. All Year cells `—` ("in
  2004" dates a process introduced on the RVP-500, kept in Published figures).
* **R-ENTRIES.** "Read term by term: …" → 5 rows, one per quoted entry, in the page's order, each
  gloss word for word; Status `—` (the page gives no hedge). The "DH3" sentences stay as prose.
* **R-QUICKFACTS.** Cells over cap 7 → 5. What it does: the Wikipedia clause ("LPCVD "dominates …",
  and "Reduced pressures …"") moved verbatim to the first H2's second paragraph. SkyWater-listed
  tool: the five entry quotations (now in the blockquote and the entries table) → their process
  names, plus a pointer. Left: Pressure (it carries the pointer to the in-force note; not touched),
  Films and temperatures, By-products, Wafer handling, 200 mm era (quotations and figures only
  here).
* **R-PARA / R-SENTENCE / R-LIST.** The Kokusai and Sony tube descriptions and the step-grade
  sentence ("The grades rest on the listed processes: …") became lead-ins and lists, each single
  marker on its lead-in. Splits at semicolons (Kamins, the ammonium-chloride trap, the precursors
  item, two integration items) and at ", and in TEOS oxide" and ", and Aviza's 300 mm RVP-300"
  (the in-force pointer sentence keeps its words). Items over 60 → lead + continuation.
* **R-RELATED**, **R-CAPTION** as page 1.

Caps (measure5): paragraphs > 100 5 → 0; list items > 60 3 → 0; sentences > 45 15 → 3 (Becker 49
and the TSMC patent 53, over only by their quotations; the untouched grading bullet); table cells >
25 5 → 4 (quick facts).

Preservation. DEDUPLICATED: number 200 (template sentence). The entries table's quotations replace
the quick-facts cell's copies one for one, so no quotation is lost or added. ADDED marker:
`pat-nh4cl-vlsi` (split). REGROUPED: the models bullets → rows; the grade sentence → list. Template
losses: `about`, `SKY130`. Strict words: the template sentence; "Read term by term" (the table).
Marker coverage: 33 flags, all read — list items (markers on the lead-ins, R-LIST step 1),
model and entry cells, and split halves whose own clause carries no source in the base.

Content problems for the owner: none found.

## Guide problems

1. **`measure5.py` fuses a sentence ending in "…ch."** Its abbreviation guard `(?<!ch\.)` (meant
   for "ch." = chapter) also matches "etch.", "each.", "which.", so a sentence that ends "…the
   etch." is counted together with the next one (plasma-etcher-dielectric, base line 31: a 66-word
   "sentence" that is two). Every etch page is affected; a `\bch\.` guard would fix it. The scripts
   are under `docs/plans/readability/`, so this is a coordinator item.
2. **§1 says a quotation counts as one word, the scripts count every word in it.** Cells made of
   two quotations (2300 Exelan row) are reported over 25 words by `measure5.py`.
