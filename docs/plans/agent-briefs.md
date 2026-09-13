# Standing briefs for sub-agents

These briefs are given verbatim to every sub-agent so that all pages are
written, reviewed and audited to the same standard.

## Common rules (all agents)

1. **Public sources only.** Cite only material anyone can obtain: PDK
   documentation, vendor data sheets and manuals, regulatory filings,
   press releases, patents, standards, textbooks, papers, conference
   talks, Wikipedia, reputable industry press.
2. **Never name, link, quote or allude to non-public material.** If a
   fact cannot be found publicly, either leave it out or state it as an
   inference from public evidence with the reasoning shown. The step
   list comes from the public *S8 / SKY130 Process Steps* sheet, cited
   as `[^steps-sheet]` (inventory key STEPS-SHEET); its mask tabs may be
   cited too. The sheet records step codes, names and order, not process
   conditions: a step name is evidence of what the sheet calls a step,
   not of films, chemistries, tools or doses, so do not use it alone as
   evidence for those, and do not call a name's meaning "not public".
   Write "the step list does not explain X; we read …" and base readings
   on public sources (PDK, filings, qualification reports). This
   includes soft forms ("as the name suggests", "the suffix makes it
   the Nth …", "consistent with the step name"). Search-engine snippets and pages that were never
   retrieved are not cited or mentioned. A public page that was
   retrieved (e.g. a job listing) may be cited with its retrieval date.
3. **Numbers need a public citation.** Every thickness, temperature,
   dose, energy, pressure or time carries a citation to a public source
   or is explicitly marked as a typical industry value with a textbook
   or paper reference.
4. **Distinguish known from inferred.** Use "SkyWater has publicly
   stated…", "the PDK documentation shows…", "a 200 mm fab of this
   vintage would typically use…", "we infer … because …".
5. **British spelling** (planarisation, metallisation, aluminium),
   ISO 8601 dates, SI units with a space before the unit (`1.8 V`,
   `130 nm`, `900 °C`).
6. **Markdown + MyST.** Use `{ref}` roles with the page labels
   (`step-NNN`, `category-<slug>`, `machine-<slug>`, `material-<slug>`,
   `mask-<slug>`) and `{term}` for glossary entries. The build runs
   with `-W` and `nitpicky = True`: a broken reference fails the build.
7. **Commit small and often** in your own worktree/branch. Never commit
   to `main`. Commit messages must obey rule 2 as strictly as page text.
8. Work in a git worktree under `.worktrees/<branch>`; never touch other
   worktrees.
9. **Do not launch sub-agents of your own.** Do all the work yourself,
   sequentially; the coordinator keeps at most two agents running at
   once.
10. **No personal details in web requests.** Fetch with the user agent
    `sky130-process-tech docs checker` and never put an e-mail address,
    name or account in any request header or URL. Where a site demands
    a contact (e.g. SEC EDGAR), use the Wayback Machine copy instead.

## Writer brief (step pages)

You are writing `docs/steps/NNN-code.md` for one or more steps. Keep
the template headings exactly (see `tools/check_steps.py`). For each
step provide:

* **What this step is** — a plain-language description, then a precise
  process description (films, thicknesses, what is patterned, etc.).
* **Step category** — link the category page and say what is specific
  about this instance.
* **Why this step exists** — the device or integration reason; what
  would go wrong without it; what earlier/later steps depend on it.
* **How it is typically performed** — industry-generic recipe outline
  for a 200 mm, 130 nm-era fab (tool type, chemistry, temperature
  range, endpoint, typical thickness), with citations.
* **Machines typically used** — tool classes, linked to machine pages;
  representative models from the 130 nm era from any vendor.
* **Machines likely used at SkyWater** — only public evidence: SkyWater
  press releases, SEC filings, job adverts, conference talks, tool
  vendor press releases naming SkyWater, photos on SkyWater's public
  site, trade press. State the evidence and its strength.
* **Resources required** — gases, wet chemicals, targets, slurries,
  resists, developers, wafers; link material pages.
* **Related steps** — previous/next, the mask used, the strip step that
  follows a mask, the etch that follows a deposition, etc.
* **Citations** — Markdown footnotes exactly as specified in
  `docs/plans/citation-style.md`: `[^label]` after every claim, number
  or quotation; full citation with URL in the footnote definition at
  the end of the page; labels reuse the inventory keys in lower case.
* **References** — three annotated reading lists: *Cross-check*
  (primary public sources for the specific claims on this page),
  *High-level* (Wikipedia, textbooks, tutorials), *Deep dive* (papers,
  review articles, theses, patents from several assignees, book
  chapters, standards, vendor application notes; **at least eight
  entries**, each with one clause on what it contributes). Bullets are
  short and end with the footnote reference that carries the full
  citation.
* **Open questions** — anything you could not confirm publicly.

Run `uv run tools/check_steps.py`, `uv run tools/check_refs.py`,
`uv run tools/check_machines.py` (machine-page headings and step lists),
`uv run tools/check_materials.py` (material-page headings, index row
keys and class-page table, rows covered, step lists and summary table),
`uv run tools/check_masks.py` (mask-page titles, headings, quick facts, plates,
step lists and links) and
`uv run sphinx-build -W -q -b html docs docs/_build/html` before
finishing. Report the branch name, commits, and any claims you were
unable to source.

## Material-page writer brief

You are writing `docs/materials/<slug>.md` for one consumable class.
The three pilot pages (wet chemicals, lithography materials, sputter
targets) are the model; `tools/check_materials.py` enforces the points
marked *(checked)*.

* **Rows you own.** The class-page table under "How to read the index"
  in `docs/materials/index.md` assigns every main-table row, by its key,
  to exactly one class page: the page for the row's primary role, which
  is the first term of its *Class* cell *(checked)*. Cover exactly your
  page's keys. A row whose *Class* cell names your class only as a second
  term (nitrogen as an anneal ambient, say) is discussed with a link to
  the {ref}`materials index <materials-table>`, not listed. If a row
  seems misassigned, or mixes two classes, report it; a split or
  reassignment is a separate index change.
* **Template** *(checked)*. Label `(material-<slug>)=`; the H2 and H3
  headings of the checker; a summary table before the first H2 whose
  first row is "What they do" and whose last two rows are "SkyWater
  evidence" and "SKY130 steps | N steps; see {ref}`…
  <material-<slug>-steps>`", with N the number of steps listed.
* **Steps section** *(checked)*. Under the `(material-<slug>-steps)=`
  label and "SKY130 steps that use this class": a line reading
  "Materials index rows covered:", a blank line, and one bullet per
  owned row in the form `` * `key` — short name `` (no footnotes); then
  a line reading "Steps:", a blank line, and one paragraph of
  `{ref}`CODE <step-NNN>`` links, in ascending order, each with the
  step's code as its text, together the union of the rows' *Steps*
  cells ("all except" cells count as their complement). Grouping text
  may follow.
* **Publishing the page in the index** *(checked)*. Replace
  `` `slug` (not yet written) `` in the class-page table with
  `{ref}`slug <material-slug>``, link the *Class* cell of every owned
  row to the page, add the page to the toctree, and link the class's
  bullet under "Consumable classes".
* **Step pages' readings.** Wherever the page says what a SKY130 step
  uses or does, attribute it: "the NS19 page reads …", "on the step
  pages' readings". Never let a step code or step-list name stand in for
  evidence (Common rule 2); where the name is the only evidence, write
  "the step list calls X "…" and does not explain it; its step page
  reads …". The same goes for the page's introduction and summary table.
* **Suppliers.** SkyWater's filings name suppliers, not the products,
  chemistries or grades SkyWater buys from them. Say so in *At
  SkyWater*, and where *Representative materials and grades* quotes a
  supplier's catalogue, say that the statements describe the catalogue,
  not SkyWater's purchases, even when the supplier is named in a filing.
  Company-lineage links (Honeywell → Solstice, Air Products → Moses Lake,
  Praxair → Linde, Versum → EMD, KMG → CMC/Entegris) stay open questions
  unless a public source joins them. When Cypress reports are used as
  evidence for the fab, cite the S-1 for the fab's Cypress history.
* **Standards** are cited through store or catalogue listings, with the
  revision, status and access date.
* **Links from other pages.** Link-only edits: on each covered step
  page, put `{ref}`existing words <material-slug>`` on the first mention
  of a material of the class in *Resources required*, without adding
  words ("see", parentheses); on each machine page that consumes the
  class, one sentence in *Consumables and facilities* and one *Related
  pages* bullet.
* **Inventory.** New sources get entries in the material-pages section
  of `docs/references/public-sources.md`, and the header count must
  equal the number of `**KEY** —` lines, with no duplicate keys. An
  existing entry gets a separate line "Also used on the <class> material
  page." after its "Tier:" text.

Run all five checkers and the `-W` build as in the step-page brief.

## Mask-page writer brief

You are writing `docs/masks/<code>.md` for one mask step. The three
pilot pages (DNM, P1M, VIM4) are the model; `tools/check_masks.py`
enforces the points marked *(checked)*.

* **Title** *(checked)*. Label `(mask-<code in lower case>)=` on the
  first line, matching the file name, and title `# CODE — <name>`:
  * a mask with a `masks.csv` entry takes the `Mask` field of the
    variant marked `X`, or of its only entry when none is marked
    (`PWBM`, `PWDEM`, `CAPM`); for `VIM2`, `MM3` and `PDM` that is the
    `X` variant ("Via 2-PLM", "Metal 3-PLM", "Pad (scribe protect)");
  * a mask without one (`RRPM`, `URPM`, `CAP2M`) takes the name of its
    row in the sheet's "Run Mask IDs" tab, as the masks index quotes it
    ("Rev Resistor Protect", "Ultra-High Resistor Poly", "Capacitor
    MiM 2"), not the step list's description (which calls both `CAPM`
    and `CAP2M` "Capacitor mask");
  * escape Markdown characters as the index does (`Low Vt Nch\*`).
* **Headings** *(checked)*. The H2 and H3 headings of the checker.
  "Plates and reticle sets" may carry the optional H3 "The mask-type
  record" (the via 2, via 3 and via 4 masks); no other H3 is allowed.
* **Quick facts** *(checked)*. A table before the first H2 headed
  `| | CODE — <name> |` with exactly these rows, in this order
  (footnotes go at the end of a cell):
  * "Mask step" — one link, `{ref}`CODE <step-NNN>``, to the mask step
    the index's "Mask steps in this reference" table gives, then "step
    N of 171".
  * "PDK mask (`masks.csv`)" — every variant in the index's *PDK mask*
    cell, as `"Mask", `CODE`, marked `X` in `Used in SKY130`` or
    `"Mask", `CODE`, unmarked`; for a mask without an entry, "not
    listed; the name is the "Run Mask IDs" tab's "<name>"".
  * "Mask-level layer (`gds_layers.csv`)" (singular even where there
    are several purposes), "Drawn layer (`gds_layers.csv`)" and
    "Minimum CD, feature / space" — every code span, quotation,
    layer:datatype, value and "N/A" of the index cell, in the index's
    order, with the layer descriptions added; "none" and "none listed"
    exactly as the index gives them; "inference" kept where the index
    marks one. For variants, give every variant's values, as the index
    does.
  * "Polarity and tone" — "Not published." and the reading, marked as
    such.
  * "Exposure class" — the step page's reading with its basis and a
    link to the machine page.
  * "Mask type (process-steps sheet)" — the "Sheet4" code as a code
    span followed by the index's reading, or exactly "None recorded;
    the sheet codes a type for the via 2, via 3 and via 4 plates only".
  * "Plates recorded", "Plate no." and "Dies with shapes, MPW-1 to
    MPW-8 (renders)" — exactly the mask's cells in the index's "Plates
    by mask" table ("not rendered" for `RRPM`).
  * "Steps that use the pattern" — "N steps; see
    {ref}`Steps that use this mask <mask-<code>-steps>`", with N the
    number of steps listed.
* **Plates** *(checked)*. Under "Plates and reticle sets", a table
  `| Run | Reticle set (sheet column heading) | Plate ID |` with one row
  per run, MPW-1 to MPW-8 in order: the index's reticle set, and the
  plate ID from the sheet, or "none recorded".
  * **Variants** (`VIM2`, `MM3`, `PDM`): the table covers the `X`
    variant only; add one sentence saying the sheet records no plates
    for the unmarked variants.
  * **Partial records** (`PWBM`, `PWDEM`, and the MPW-5 gaps): keep the
    "none recorded" rows and add a bullet repeating the index's
    non-conclusion (the page reports what is recorded and does not
    conclude that the mask was absent). For `PWBM` and `PWDEM` also say
    that no rendered die draws `pwbm` or `pwde`, so that the page does
    not imply use.
  * **Anomalous plate numbers** (`NSM` on MPW-6, `S8014AA616A`): one
    bullet quoting the plate ID and saying the sheet does not explain
    it.
  * Before writing, run `uv run tools/check_masks.py --sheet <file>`
    once with a local CSV export of the "Run Mask IDs" tab (saved under
    the worktree's `tmp/`, which is deleted afterwards) to compare the
    index-derived plate IDs with the sheet.
* **Steps that use this mask** *(checked)*. Under the
  `(mask-<code>-steps)=` label, a line "Steps:", a blank line and one
  paragraph of `{ref}`CODE <step-NNN>`` links, each with the step's code
  as its text: the mask step and the consecutive steps after it, before
  the next mask step, that the step pages read as using its resist
  pattern — the mask's *Patterns* cell on the index, in step order, each
  linked page linking the mask step. Explain each step in bullets
  below. Close with three sentences: what the next step does, attributed
  ("on its step page's reading, …"); the next mask step; and "no
  exception" or the exception. If the step pages' reading changes,
  change the index's *Patterns* cell in the same branch. Known cases:
  for `TUNM`, say that ONO (step 40) is not listed because it does not
  use the resist; for `NWM`, that LVTPI uses the `NWM` resist on the
  step pages' reading; for `PSDM`, that the "Masks" tab repeats the
  mask's description for `PSDI`.
* **Evidence.**
  * State which facts come from the PDK, which from the sheet and which
    from the renders.
  * The renders show drawn tape-out data, not photomask artwork: quote
    the site's "renders of *drawn* data" *(checked)*. Their layer
    choices, `expr` expressions and notes are one public derivation,
    "not SkyWater's" recipe *(checked)*. For a mask rendered from an
    expression (`LVTNM`, `HVTPM`, `NTM`, `HVNTM`) or from layers that
    differ from the index's pairing (`LVOM`, `PWBM`, `RPM`, `MM4`), quote
    the `expr` or the layers verbatim with layer names, and repeat the
    index's note contradictions for the mask. The sheet's notes and the site's notes share wording and do
    not corroborate each other.
  * For a mask used on few dies (`TUNM`, `ONOM`, `LDNTM`, `RPM`), give
    dies by run and frame only ("MPW-1, frame A4"), and say where a plate
    is recorded on a run on which no die draws the layer. For a mask with
    shapes on 39 or 40 dies of every run (`CAPM`, `CAP2M`, `URPM`,
    `NSM`, `DNM`, `VIM4`), give the minimum per-die shape count and,
    where counts repeat, the number of dies with a repeated count, and
    read repeated counts as common to the dies (inference), as the DNM
    and VIM4 pages do.
  * Exposure class, tone, resist and reticle type are readings, marked
    as such, with their basis (design rules, the sheet's mask-type codes
    as read on the index); step names and codes are not evidence
    (Common rule 2).
  * Attribute every description of an adjacent step to its step page.
  * Do not state a design rule's or criterion's purpose (a margin, a
    budget) as fact; mark it as a reading.
  * Claims about a paper go no further than its abstract (or, for a
    book, its table of contents) unless marked as the paper's or book's
    content not checked.
* **Design rules.** Quote the periphery rules and *Criteria &
  Assumptions* with their names, flags and values as published. Head
  the rule table's description column "Description (published wording,
  abridged where marked "[…]")" and end a cut-short quotation with
  "[…]" inside the quotation marks (an ellipsis in the published text
  stays as printed). Give each rule's flag in parentheses and quote the
  flag legend verbatim, escaping asterisks (`\*`). Before writing, grep
  every *Criteria & Assumptions* CSV (`01` to `10`), not only Table 2,
  for the mask's acronym and its drawn layer's name; mask-named criteria
  are easy to miss (for example `P1MCDcontrol`, `PdmCD_tol`,
  `NSMKeepout`, `NwellCvxSerif`, `LI1PROXSpace`, `NCM_0LVL`, the
  photoresist thickness for HV tip implants). Quote the periphery rules
  that name mask data: x.1a (the `p1m`, `met1`, `via` and `met2` mask
  data, on the MM1, VIM and MM2 pages as well as P1M), x.7, x.9 and
  x.15a, and any rule flagged `DNF` or `A`, on the page of the mask it
  belongs to.
* **Implant masks.** The DNM page's "Lithography and pattern transfer"
  is the model: resist stopping power, thickness and outgassing, and
  "Nothing is etched through this resist". Reuse its sources through
  "Also used on" lines rather than new keys. For the thin tip-implant
  masks (`NTM`, `HVNTM`, `LDNTM`), quote Table 4's "Photoresist
  thickness for HV Tip Implants" (0.3, `PrThickImplant`) and the
  `ntmShadowing` and `hvntmShadowing` values.
* **Owner constraints.** The renders site and the sheet may be cited
  for plate IDs, reticle-set IDs, lot IDs, mask-type codes, images,
  layer and note metadata, and per-die and per-run shape and render
  counts. Do not:
  * name any project, design, customer, person or recipient taken from
    the renders site or the sheet (the site's per-die `project` field,
    shuttle product names, lot `customer` fields and the like);
  * report any lot status, custody, shipping or ownership information
    from either source;
  * name, link or cite the software that generated the renders or any related software repository;
  * link the sheet's photo albums or cite order or job numbers.
* **Links.** Publishing the page is a link-only change to the index:
  add the page to the toctree and link the mask acronym in the page's
  row of "Mask steps in this reference" as `{ref}`CODE <mask-code>``
  *(checked)*; for a row without a `masks.csv` entry, add "mask page
  {ref}`CODE <mask-code>`" after the link in the Step cell.
  Link the page from its mask step page with a *Related steps* bullet
  containing `{ref}`CODE <mask-code>`` *(checked)* and, where natural,
  from the exposure machine page's *Related pages*, symmetrically for
  a class that is the mask's alternative.
* **Inventory.** New sources go in §8.21 of
  `docs/references/public-sources.md` under the page's `####`
  sub-section; the header count must equal the number of `**KEY** —`
  lines, with no duplicate keys; an existing entry gets a separate line
  "Also used on the <CODE> mask page." after its "Tier:" text. A mask
  page needs at least eight Deep dive entries (`tools/check_refs.py`).
* **Before committing**, check the page and every commit message:
  * no project, design, customer, person or recipient names from the
    renders site or the sheet; dies by run and frame only;
  * no lot status, custody, shipping or ownership fields;
  * no mention of the software that generated the renders or of any related software repository;
  * the renders are described as drawn data, and `expr` and notes as
    one public derivation, not SkyWater's;
  * sheet and site notes are not cited as corroborating each other.

Run all five checkers (`check_steps.py`, `check_refs.py`,
`check_machines.py`, `check_materials.py`, `check_masks.py`) and the
`-W` build as in the step-page brief.

## Reviewer brief (technical accuracy and consistency)

You are reviewing a branch that adds or changes pages. You did not write
them. Check, and report with file and line references:

1. **Technical accuracy** — is the physics/chemistry/equipment
   description correct for a 130 nm, 200 mm process of this type?
   Verify at least three specific claims per page against the cited
   sources by fetching them.
2. **Citation integrity** — does every cited source exist, is it public,
   and does it actually say what the page claims? Flag dead links and
   misattributed claims.
3. **Consistency** — do names, thicknesses, layer order, mask names and
   step numbers agree with already-merged pages (grep `docs/`)? List
   every conflict with both locations.
4. **Inference hygiene** — is every "likely used at SkyWater" claim
   backed by stated public evidence, with the inference marked as such?
5. **Template, citations and build** — mandatory headings present;
   citations follow `docs/plans/citation-style.md` (footnotes, no
   reference-style links, Deep dive at or above the minimum length and
   genuinely varied); `tools/check_refs.py` and the `-W` build pass.

Return a verdict (`approve`, `approve with fixes`, `reject`) and an
itemised list of required fixes.

## Provenance-review brief

You are auditing the repository for any statement, link or value whose
origin is not public. Scan every tracked file **and the full git log
(`git log -p`)** for:

* hostnames, IP addresses, file-system paths or URLs that are not
  public;
* document links or IDs that are not demonstrably public (linked from a
  public page, repository or publication);
* phrasing that implies a non-public origin for a statement;
* specific numeric process values (thickness, dose, energy, temperature,
  time, pressure) that carry no public citation and no "typical" label;
* identifiers such as plate, lot, wafer, order or serial numbers, or
  personal names of staff. Plate IDs, reticle-set IDs, MPW lot IDs and
  mask-type codes taken from the public process-steps sheet or the
  public mask-layer renders, and citations of the renders site
  (`[^mask-renders]`, `https://data.wafer.space/big-storage/sky130-masks/`),
  are approved by the owner and are not findings;
* names of projects, designs, customers or recipients taken from the
  renders site or the sheet (the site's per-die project names, shuttle
  product names, lot customer fields), any lot status, custody,
  shipping or ownership information from either source, and any
  mention of the software that generated the renders or of any related software repository — these are findings wherever they appear, including
  commit messages.

Report every hit with file path, line (or commit hash), the offending
text, and a proposed remediation. Return `clean` only if nothing is
found.
