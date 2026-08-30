# SKY130 Process Technology Documentation — Design

Date: 2026-08-30

## Goal

Produce the most comprehensive publicly available reference describing how
the SKY130 130 nm CMOS process technology is manufactured, step by step,
as a worked example of how a mass-produced 130 nm process is set up.

The documentation is written in Markdown, built with Sphinx + MyST, and
targeted at publication on Read the Docs.

## Scope

* One Markdown page per process step in the SKY130 flow (171 steps,
  `SMAT` → `HPETEST`).
* One page per *category* of step (oxidation, deposition, lithography,
  etch, implant, anneal, CMP, clean/strip, metallisation, test, …).
* One page per class of manufacturing tool (machine), with an index
  mapping tools ↔ steps.
* One page per consumable resource class (gases, chemicals, targets,
  slurries, photoresists, …) with an index mapping resources ↔ steps.
* A mask index (mask name ↔ step ↔ GDS layer).
* A glossary of terms and acronyms.
* A bibliography of public references, split into
  *cross-check*, *high-level* and *deep-dive* tiers.

## Non-goals

* No proprietary recipes, parameters, or content from non-public sources.
* No references — direct or oblique — to private source material.
* Not a PDK design-rule manual (that already exists in
  `skywater-pdk` docs); we link to it instead.

## Source policy (critical)

Public documents **only** may be cited. Private material (personal
cloud storage, private backups, NDA-covered sources) may be used solely
as a *starting point* to discover what public information exists. Any
working notes that mention private material live in a separate, private
repository outside this tree; nothing in this repository names, links to
or depends on it.

An independent "leak-review" sub-agent audits the public tree and the
commit history at regular intervals for:

* file paths, hostnames, or URLs of private storage;
* names of private documents or folders;
* phrasing that acknowledges a private origin ("internal document",
  "from the NDA package", "SkyWater's runsheet says", …);
* numeric values that appear nowhere in the public record and cannot be
  attributed to a public source.

## Approaches considered

1. **Sphinx + MyST-Parser (chosen).** Native Read the Docs support,
   Markdown authoring, cross-references (`{ref}`/`{term}`), glossary
   directive, bibliography via `sphinxcontrib-bibtex` if needed.
2. MkDocs + Material. Simpler, but weaker glossary/cross-reference
   support and RTD integration is second-class.
3. Plain Markdown in a git repo (GitHub rendering). No cross-reference
   resolution, no glossary, no index generation.

Sphinx + MyST gives us term cross-references and a build that fails on
broken links, which matters for a document of this size.

## Repository layout

```
docs/
  conf.py                 Sphinx configuration (MyST enabled)
  index.md                Landing page + master toctree
  overview/               Process flow overview, FEOL/BEOL, history
  steps/NNN-code.md       One page per process step (NNN = step number)
  categories/             One page per step type (etch, litho, …)
  machines/               One page per tool class + index
  materials/              One page per consumable class + index
  masks/                  Mask index and per-mask pages
  glossary.md             Sphinx glossary
  references/             Bibliography tiers
  plans/                  This design + task log (excluded from build)
```

## Step page template

Every `docs/steps/NNN-code.md` file uses the same section order so the
pages are comparable and machine-checkable:

1. Title: `Step NNN — CODE: Long name`
2. Summary table: step number, code, category, phase (FEOL/MOL/BEOL),
   mask (if any), previous/next step links.
3. What this step is.
4. Step category (link to category page).
5. Why this step exists (purpose in the device/integration flow).
6. How it is typically performed (industry-generic description).
7. Machines typically used (generic tool classes → machine pages).
8. Machines likely used at SkyWater (public evidence only, with the
   basis for the inference stated).
9. Resources required (gases, chemicals, targets, resists, …).
10. Related steps and cross-references.
11. References — three tiers: cross-check, high-level, deep-dive.
12. Open questions / uncertainty notes.

A checker script (`tools/check_steps.py`) verifies every step page
contains every mandatory heading and that every link resolves.

## Workflow

* Main agent owns `main`, the plan, the task log and merges.
* Writer sub-agents each work in an isolated worktree under
  `.worktrees/<branch>` on a `step/<code>` or `topic/<name>` branch.
* Every branch is reviewed by an independent reviewer sub-agent for
  technical accuracy and for conflicts with already-merged pages before
  merge.
* At most two sub-agents run concurrently.
* A leak-review sub-agent runs after every batch of merges.
* Small, logical commits; the task log is updated one item at a time.

## Decisions made without user input

* Worktree location: `.worktrees/` (project-local, git-ignored).
* Build system: Sphinx + MyST-Parser, `furo` theme, `uv` for Python.
* Licence: Apache 2.0 (per standing instruction).
* Private working notes are kept in a local-only git repository outside
  this tree and are never referenced from it.
* Step file naming: three-digit zero-padded step number + lower-case
  step code (`001-smat.md`). Codes containing `/` become `-`
  (`TI/TIN1` → `097-ti-tin1.md`).
