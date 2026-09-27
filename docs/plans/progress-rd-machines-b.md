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

## Guide problems

1. **`measure5.py` fuses a sentence ending in "…ch."** Its abbreviation guard `(?<!ch\.)` (meant
   for "ch." = chapter) also matches "etch.", "each.", "which.", so a sentence that ends "…the
   etch." is counted together with the next one (plasma-etcher-dielectric, base line 31: a 66-word
   "sentence" that is two). Every etch page is affected; a `\bch\.` guard would fix it. The scripts
   are under `docs/plans/readability/`, so this is a coordinator item.
2. **§1 says a quotation counts as one word, the scripts count every word in it.** Cells made of
   two quotations (2300 Exelan row) are reported over 25 words by `measure5.py`.
