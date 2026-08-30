# Standing briefs for sub-agents

These briefs are given verbatim to every sub-agent so that all pages are
written, reviewed and audited to the same standard.

## Common rules (all agents)

1. **Public sources only.** Cite only material anyone can obtain: PDK
   documentation, vendor data sheets and manuals, regulatory filings,
   press releases, patents, standards, textbooks, papers, conference
   talks, Wikipedia, reputable industry press.
2. **Never name, link, quote or allude to private material.** No cloud
   drive documents, no private backups, no NDA-covered sources, no
   "internal documents", "runsheets", "travelers" or "the foundry's own
   notes". If a fact is only known from a private source and cannot be
   found publicly, either leave it out or state it as an inference from
   public evidence with the reasoning shown.
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
* **References** — three tiers: *Cross-check* (primary public sources
  for the specific claims on this page), *High-level* (Wikipedia,
  textbooks, tutorials), *Deep dive* (papers, theses, patents).
  Every reference is a full citation with a URL where one exists.
* **Open questions** — anything you could not confirm publicly.

Run `uv run tools/check_steps.py` and
`uv run sphinx-build -W -q -b html docs docs/_build/html` before
finishing. Report the branch name, commits, and any claims you were
unable to source.

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
5. **Template and build** — mandatory headings present; build passes
   with `-W`.

Return a verdict (`approve`, `approve with fixes`, `reject`) and an
itemised list of required fixes.

## Leak-review brief (private-source exposure)

You are auditing the *public* repository for any exposure of private
source material. You have no need to know what the private material is;
you are looking for signs of it. Scan every tracked file **and the full
git log (`git log -p`)** for:

* hostnames, IP addresses, mount points, file-system paths or URLs that
  point at personal or private storage (cloud drives, backup servers,
  internal mirrors, code-review hosts other than public ones);
* Google Docs/Sheets/Drive/Photos links or IDs;
* the names of private documents, folders, spreadsheets or albums;
* phrases acknowledging a private origin: "internal", "NDA", "confidential",
  "proprietary document", "runsheet", "traveler", "the foundry's own",
  "from the spreadsheet", "Tim's notes", "personal archive";
* specific numeric process values (thickness, dose, energy, temperature,
  time, pressure) that carry no public citation;
* mask plate IDs, lot/wafer numbers, purchase-order numbers, serial
  numbers, or personal names of fab staff.

Report every hit with file path, line (or commit hash), the offending
text, and a proposed remediation. Return `clean` only if nothing is
found.
