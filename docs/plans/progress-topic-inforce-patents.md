# Progress — `topic/inforce-patents`

Branch: `topic/inforce-patents`, worktree `.worktrees/topic-inforce-patents`.

## The rule

A patent family the dataset does not show as certainly expired
(`expired: false` or `unknown` in `data/patents.yaml`) is shown only
behind a collapsed block, in the patent index and on the process pages
alike, so that a reader who must not read patents in force can use the
site without being shown their content. The patent index and the
generated `index-links` blocks already obeyed the rule; the process
pages were written before the index existed and did not.

Twelve inventory keys cite such a family — all twelve shown *in force*,
none of unknown status:

`PAT-02`, `PAT-03`, `PAT-04`, `PAT-DICO2-MKS`, `PAT-EDGESEAL-GF`,
`PAT-MIM-TI-ETCH`, `PAT-ONO-THICK-CYP`, `PAT-RADOX-CYP`,
`PAT-RRAM-ETCHSTOP-TSMC`, `PAT-RRAM-OXIDE-TSMC`, `PAT-SOFTMARK-GSI`,
`PAT-TESTLINE-TSMC`.

The measurement this branch works from is Part 2 of the independent
verification of `topic/index-links` (383 citations, 55 pages, 201
open-prose sentences, 75 verbatim quotations), with the per-citation
detail in that report's TSV.

## The pattern

Three moves, used everywhere:

1. **Prose.** The sentences that quote or paraphrase the patent's
   technical content move, unchanged in substance and with their
   footnote references, into a collapsed note placed where the argument
   needs it — under the paragraph, or under the list, that used them:

   ````markdown
   :::{dropdown} From a patent shown as in force (US 8,093,128; estimated expiry 2028-10-22) — open to read
   (the moved sentences)
   :::
   ````

   Two patents in one note give
   `From patents shown as in force (US 8,093,128, estimated expiry
   2028-10-22; US 8,796,098, estimated expiry 2034-02-26) — open to read`.
   The title carries number, status and estimated expiry only — never
   the technical content — matching `tools/gen_patents.py`'s
   `dropdown_title()` and the design in
   `docs/plans/patent-index-design.md`. The expiry is the *family*
   expiry from `data/patents.yaml`, as on the index.

   The visible text says what *kind* of evidence sits in the note
   without stating its content ("a Cypress patent that may still be in
   force gives thickness ranges for this layer; they are in the
   collapsed note below"), and keeps every statement resting on other
   public sources.

2. **Tables.** The affected cell keeps a pointer ("see the collapsed
   note under this table") and its content moves to one note placed
   immediately after the table.

3. **Reading lists.** Every `### Cross-check` / `### High-level
   understanding` / `### Deep dive` bullet citing one of the twelve
   moves, unchanged, into **one** collapsed block at the end of the list
   it belongs to. Bullet counts do not change, so `check_refs.py`'s
   Deep dive minimum still holds.

Footnote definitions stay at the foot of the page (a citation must stay
resolvable) and the inventory entries stay in
`docs/references/public-sources.md`; both carry the flag sentence

> Shown as in force; estimated expiry YYYY-MM-DD (estimate from public
> records, not legal advice).

appended as new lines, so no existing line was reflowed. (For a family
of unknown status the checker expects "Status shown as unknown;
estimated expiry no later than YYYY-MM-DD (…)"; no cited family is in
that state today.)

## The checker

`uv run tools/check_inforce.py` (PEP 723, `--selftest`). It derives the
restricted set from `data/patents.yaml`, maps it to inventory keys and
to the footnote labels defined on the pages, and fails when, on any page
under `docs/` outside `docs/references/patents/` and `docs/plans/`:

* a footnote reference to such a label,
* a member publication number in any usual spelling
  (`US8093128B2`, `US 8,093,128 B2`, `8,093,128`, `US 2009/0179253 A1`,
  `EP 2 104 648 B1`, …), or
* a family or member title (five words or more; shorter titles are too
  generic to match safely in prose)

appears outside a `{dropdown}` — colon fence or backtick fence, nesting
tracked. The dropdown's own title line counts as inside, because that is
where the number and status legitimately appear. Footnote definitions
and the family's own inventory entry are allowed but must carry the flag
sentence with the date the dataset gives; the checker compares the date,
so the flag cannot drift from the data. Matching runs on a
whitespace-flattened copy of the page, so a number or title broken over
a line by Markdown wrapping is still found.

It is in the README's checks list and in the Reviewer brief's list of
checks in `docs/plans/agent-briefs.md`.

### Opening a note up again when a patent expires

The same checker prints a **reverse report** (`note:` lines, not
failures): a `{dropdown}` whose title names a publication number of a
family the dataset now shows as `expired: true`, and any footnote
definition or inventory entry still carrying an in-force flag for such a
family. When `data/patents.yaml` is refreshed and a family flips to
expired:

1. `uv run tools/check_inforce.py` and read the `note:` lines.
2. For each, delete the `:::{dropdown} …` and closing `:::` lines and
   fold the sentences back into the paragraph or list above them,
   removing the "in the collapsed note below" pointer from the visible
   text.
3. Delete the flag sentence from that patent's footnote definitions and
   from its inventory entry.
4. Re-run the checker: the `note:` lines are gone and the problem count
   is still zero.

Nothing else has to change: the generated `index-links` blocks and the
patent index open up by themselves when `tools/gen_index_links.py` and
`tools/gen_patents.py` are re-run.

## Per-page status

Counted from the verification TSV (open-prose citations; the reading-list
bullets and footnote definitions of every page were handled by the two
mechanical passes).

| Page | Open citations | Status |
|---|---|---|
| `docs/machines/starting-material.md` | 5 | done |
| `docs/steps/001-smat.md` | 1 | done |
| `docs/steps/002-box.md` | 1 | done |
| `docs/steps/003-isonit.md` | 1 | done |
| `docs/steps/007-dnm.md` | 1 | done |
| `docs/steps/008-dni.md` | 1 | done |
| `docs/steps/015-lvtni.md` | 3 | done |
| `docs/steps/018-nwi.md` | 1 | done |
| `docs/steps/019-nwi2.md` | 1 | done |
| `docs/steps/020-lvtpi.md` | 2 | done |
| `docs/steps/023-pchi.md` | 1 | done |
| `docs/steps/024-pnchi.md` | 3 | done |
| `docs/steps/027-pwi.md` | 1 | done |
| `docs/steps/028-pwi2.md` | 1 | done |
| `docs/steps/034-rtai.md` | 4 | done |
| `docs/steps/036-tunarce.md` | 1 | done |
| `docs/steps/038-depi.md` | 1 | done |
| `docs/steps/071-ldntm.md` | 1 | done |
| `docs/steps/072-ldasti.md` | 0 (bullet only) | done |
| `docs/steps/136-captiw1.md` | 2 | done |
| `docs/steps/165-nsm.md` | 2 | done |
| `docs/steps/166-nsme.md` | 1 | done |
| `docs/steps/167-ntsd.md` | 1 | done |
| `docs/steps/168-pdm.md` | 1 | done |
| `docs/steps/171-hpetest.md` | 1 | done |
| `docs/machines/plasma-etcher-metal.md` | 3 | done |
| `docs/machines/vertical-furnace-lpcvd.md` | 3 | done |
| `docs/machines/vertical-furnace-oxidation.md` | 1 | done |
| `docs/machines/wet-bench.md` | 3 | done |
| `docs/materials/dopant-sources.md` | 2 | done |
| `docs/materials/etch-gases.md` | 1 | done |
| `docs/materials/index.md` | 2 | done |
| `docs/materials/substrates.md` | 1 | done |
| `docs/materials/ultrapure-water.md` | 5 | done |
| `docs/materials/wet-chemicals.md` | 1 | done |
| `docs/masks/lvom.md` | 3 | done |
| `docs/masks/nsm.md` | 1 | done |
| `docs/masks/onom.md` | 3 | done |
| `docs/masks/pdm.md` | 1 | done |
| `docs/masks/tunm.md` | 3 | done |
| `docs/overview/index.md` | 3 | done |
| `docs/overview/sky130b-reram.md` | 14 | TODO |
| `docs/steps/037-ptsi.md` | 6 | TODO |
| `docs/steps/039-tunme.md` | 24 | TODO (heavy) |
| `docs/steps/040-ono.md` | 27 | TODO (heavy) |
| `docs/steps/041-onom.md` | 11 | TODO |
| `docs/steps/042-onome.md` | 15 | TODO (heavy) |
| `docs/steps/043-gox100.md` | 17 | TODO (heavy) |
| `docs/steps/044-lvom.md` | 3 | TODO |
| `docs/steps/045-nchi.md` | 5 | TODO |
| `docs/steps/046-goxetch.md` | 9 | TODO |
| `docs/steps/047-lvgox.md` | 6 | TODO |
| `docs/steps/138-capme.md` | 10 | TODO |
| `docs/steps/153-cap2me.md` | 8 | TODO |

## Decisions in hard cases

* **A conclusion drawn from the patent.** Where the page's working value
  or inference came from the patent in force, the conclusion stays
  visible only if it can be stated without reproducing the teaching.
  `002-box.md` keeps its 10–20 nm pad oxide visible because the
  AmberWave STI patent (expired) gives "50-200 Å" independently; the
  Cypress quotation moves. `007-dnm.md` does the opposite: its
  conclusion ("in the Cypress lineage the deep N-well was first of all a
  high-voltage-device feature") *is* the patent's teaching, so the
  conclusion moved into the note with its reasoning and the visible text
  says only that the patent bears on where the deep N-well came from.
* **Bare mentions.** A sentence that only names the patent still carries
  a footnote reference, so it is collapsed too; the visible text keeps
  the point and says the supporting patent is in the note
  (`019-nwi2.md`, `028-pwi2.md`, `materials/etch-gases.md`).
* **A patent used on both sides of a comparison.** Where a page compares
  an in-force patent with another source, collapsing one side alone
  would leave a one-sided claim. The visible text therefore keeps the
  comparison *as a comparison* ("the second published account is in the
  collapsed note"), and the note carries only the in-force side's
  content (`136-captiw1.md`, and the same treatment is required on
  `138-capme.md` and `153-cap2me.md`).
* **Repeated citations of one patent on a page.** One note per argument,
  not one per sentence; later mentions point back to the note above
  rather than duplicating it (`materials/ultrapure-water.md`,
  `034-rtai.md`, `overview/index.md`).
* **Shared titles.** Several Cypress families publish under the same
  title, so the checker treats a title match as owned by every
  restricted family carrying it; otherwise a footnote definition that
  legitimately names one family was reported for its siblings.

## Commits

One logical commit per page or small group. The two mechanical passes
(the flag sentences; the reading-list bullets) are single commits of
their own.
