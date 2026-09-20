# Readability and formatting review — shared brief

The SKY130 process reference (171 step pages, 30 machine, 12 material, 36 mask pages, categories, overview,
glossary, reference indexes) has its content written and fact-checked. It now needs to become pleasant to read
and easy to skim. You are one of four senior reviewers (copywriting / technical editing / information design).
Your output is NOT edits: it is a precise, general set of improvement rules that less capable models can then
execute page by page without supervision.

Repository: /home/admin/github/mithro/sky130-process-tech (always `cd` there explicitly in every command;
ignore the directory you start in). Source: `docs/**/*.md` (MyST Markdown, Sphinx, furo theme, `sphinx_design`
is enabled; `docs/plans/**` is not part of the site). Rendered site:
https://sky130-process-tech.readthedocs.io/en/latest/ (path mirrors the source: `docs/steps/006-stie.md` →
`/en/latest/steps/006-stie.html`).

## You must look at BOTH the source and the rendered page
Render with the screenshot tool, then open the PNG tiles with the Read tool:
`uv run -q --with pillow python tools/shoot.py URL tmp/readability/shots/<yourletter>-<name>`
(add `--width 400` for the phone layout; do that for at least three pages). One page at a time, in the
foreground, a few seconds apart. For any other HTTP request use exactly the User-Agent
`sky130-process-tech docs checker`; never a browser User-Agent; never loop on an error or bot-check page.

## What the owner already noticed (not exhaustive — find the rest)
* Large numbers of lists written as sentences rather than as proper bulleted lists.
* Items that should be direct links but are reference footnotes holding the link, so a reader clicks the
  footnote and then the link. Worst: lists that are meant to link to Wikipedia but are footnotes.
* Giant paragraphs that are almost impossible to skim.
* Dead (404) links that need converting to archive.org / Wayback Machine copies.
* Pages where data should be in well-formatted tables but is in bulleted lists.
* Many pages that should have clear diagrams and have none.

## Hard constraints on any rule you propose
* No fact, number, quotation, citation or hedge may be lost or changed; every claim keeps its reference.
  Rules are about presentation: structure, order, sentence length, lists, tables, links, headings, diagrams.
* The checkers in `tools/check_*.py` and the generators `tools/gen_*.py --check` must keep passing. Read them
  before proposing structural changes (mandatory headings on step pages, quick-facts table, footnote/inventory
  rules in `check_refs.py`, generated `<!-- index-links:begin … end -->` blocks, generated pages under
  `docs/references/{patents,papers,filings}/`, collapsed notes for patents in force enforced by
  `check_inforce.py`). If a good improvement needs a checker or generator change, say so explicitly and
  describe the change.
* The build runs with `-W` (warnings are errors).
* Do not edit any tracked file. Write only under `tmp/readability/`. Do not commit, push or create branches.

## Deliverable
Write `tmp/readability/report-<letter>.md`, saving it early and updating it as you go (so the work survives an
interruption). Structure:
1. **Findings catalogue.** One entry per recurring problem: short name; what is wrong and why it hurts the
   reader; a real before example (file:line, quoted briefly) and the after you would want; a rule precise
   enough for a weaker model to apply mechanically; how to detect candidates (grep/regex/heuristic, with a
   measured count of how widespread it is across `docs/`); what must NOT be touched; priority (P1–P3); whether
   it can be scripted rather than hand-edited.
2. **Page-type guidance** for the page types in your lens: the ideal skeleton, what belongs in tables, lists,
   admonitions, dropdowns, figures; target paragraph and sentence lengths.
3. **Risks and open questions** for the coordinator (checker changes, anything needing the owner's decision).
Keep the report under 3,000 words excluding examples. Be concrete; no generic style-guide filler. Your final
message back should be a 200-word summary plus the report path.
