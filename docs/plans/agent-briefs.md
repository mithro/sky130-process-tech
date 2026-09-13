# Standing briefs for sub-agents

These briefs are given verbatim to every sub-agent so that all pages are
written, reviewed and audited to the same standard.

## Common rules (all agents)

1. **Public sources only.** Cite only material anyone can obtain: PDK
   documentation, vendor data sheets and manuals, regulatory filings,
   press releases, patents, standards, textbooks, papers, conference
   talks, Wikipedia, reputable industry press.
2. **Every fact needs a public source.** If a
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
`uv run tools/check_masks.py` (mask-page headings, plates and step lists) and
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

* **Template** *(checked)*. Label `(mask-<code in lower case>)=` on the
  first line, matching the file name; title `# CODE — <Mask field of
  masks.csv>` (for a mask step without a `masks.csv` entry, the step
  list's description); the H2 and H3 headings of the checker; a
  quick-facts table before the first H2 whose first row is "Mask step"
  (one link, `{ref}`CODE <step-NNN>``, to the mask step the index's
  "Mask steps in this reference" table gives), with rows "Plates
  recorded", "Plate no." and "Dies with shapes, MPW-1 to MPW-8
  (renders)" that read exactly as the mask's cells in the index's
  "Plates by mask" table, and whose last row is "Steps that use the
  pattern | N steps; see {ref}`… <mask-<code>-steps>`". Between them
  give the PDK `masks.csv` entry, mask-level and drawn layers, minimum
  CD, polarity and tone, exposure class with its basis, and the
  mask-type reading of the process-steps sheet, as the index gives them.
* **Plates** *(checked)*. Under "Plates and reticle sets", a table
  `| Run | Reticle set (sheet column heading) | Plate ID |` with one row
  per run, MPW-1 to MPW-8 in order: the index's reticle set, and the
  plate ID from the sheet, or "none recorded". Plate IDs, reticle-set
  IDs, lot IDs and mask-type codes may be cited. Do not name projects,
  people or lot records beyond what the masks index already uses, and
  cite the renders site only for its images, layer and note metadata and
  per-die shape counts.
* **Steps that use this mask** *(checked)*. Under the
  `(mask-<code>-steps)=` label, a line "Steps:", a blank line and one
  paragraph of `{ref}`CODE <step-NNN>`` links: the mask step and the
  consecutive steps after it, before the next mask step, that the step
  pages read as using its resist pattern — the mask's *Patterns* cell on
  the index, in step order, each linked page linking the mask step.
  Explain each step in bullets below, say where the list stops, and
  record any exception to the rule. If the step pages' reading
  changes, change the index's *Patterns* cell in the same branch.
* **Evidence.** State which facts come from the PDK, which from the
  sheet and which from the renders. The renders show drawn tape-out
  data, not photomask artwork; their layer choices, expressions and
  notes are one public derivation, not SkyWater's recipe; the sheet's
  notes and the site's notes share wording and do not corroborate each
  other. Exposure class, tone, resist and reticle type are readings,
  marked as such, with their basis (design rules, the sheet's
  mask-type codes as read on the index); step names and codes are not
  evidence (Common rule 2).
* **Design rules** are quoted from the periphery rules and *Criteria &
  Assumptions* with their names, flags and values as published.
* **Links.** Publishing the page is a link-only change to the index:
  add the page to the toctree and link the mask acronym in the page's
  row of "Mask steps in this reference" (`{ref}`CODE <mask-code>``;
  for a row without a `masks.csv` entry, add the link in the Step
  cell). Link the page from its mask step page (a *Related steps*
  bullet) and, where natural, from the exposure machine page's
  *Related pages*.
* **Inventory.** New sources go in §8.21 of
  `docs/references/public-sources.md` under the page's `####`
  sub-section; the header count must equal the number of `**KEY** —`
  lines, with no duplicate keys; an existing entry gets a separate line
  "Also used on the <CODE> mask page." after its "Tier:" text. A mask
  page needs at least eight Deep dive entries (`tools/check_refs.py`).

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

You are auditing the repository for any statement, link or value that
has no public source. Scan every tracked file **and the full git log
(`git log -p`)** for:

* links that do not resolve publicly;
* statements that carry no public citation;
* specific numeric process values (thickness, dose, energy, temperature,
  time, pressure) that carry no public citation and no "typical" label;
* identifiers such as plate, lot, wafer, order or serial numbers, or
  personal names of staff.

Report every hit with file path, line (or commit hash), the offending
text, and a proposed remediation. Return `clean` only if nothing is
found.
