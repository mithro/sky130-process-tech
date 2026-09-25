# Progress: rd-inforce-masks

Task: fix the six open-text passages that paraphrase US8093128B2 content
without a bare pointer, per tmp/reviews/rd-masks-b.md section E ("Existing
pages: onom and tunm open text against their in-force notes"). Worktree:
.worktrees/rd-inforce-masks, branch topic/rd-inforce-masks.

House form (from docs/plans/progress-rd-inforce-sonos.md): a pointer
sentence stays in the open; the patent's content stays only inside the
existing collapsed note; never create an open paraphrase; never move
anything out of a note. None of this review's six rulings asks for text to
be moved into a note, so no dropdown body was touched.

## Rulings applied (reviewer's exact fix)

1. **onom.md:84-86 — leak.** "says the same of its own flow" attributed the
   island/margin/logic-channel requirement to the patent. Reworded to
   "Cypress's integration patent, which may still be in force, is cited
   here too; the passage is in the collapsed note below this paragraph."
   Nothing else in the paragraph changed.
2. **onom.md:277-279 — leak.** "describes the same combination and notes
   what the wet step does to the masked region" attributed the dry-then-wet
   sequence and its effect on the masked region to the patent. Reworded to
   "The Cypress integration patent, which may still be in force, is cited
   here too; the passage is in the collapsed note below this paragraph."
3. **onom.md:280-282 — leak, the clearest.** "The undercut it describes
   shrinks the island's overlap of the window, which is why the patent
   calls the dimensions and alignment of the two important (above)."
   Deleted from the open text, per the ruling (the review says explicitly
   this reasoning is not to be moved into the note by a readability pass;
   that is an owner decision outside this task). Applied together with #2
   in one paragraph edit.
4. **tunm.md:235-238 — leak.** "takes the other view for tight layouts"
   states the patent's position (critical-layer vs. i-line lithography).
   Reworded to "is cited on the exposure class". The caveat sentence ("That
   is the patent's flow, not a statement about SKY130.") stays, as ruled.
5. **tunm.md:304-306 — leak.** "describe the same sequence, the mask it
   uses and the undercut the isotropic etch leaves" attributes the
   sequence, the mask and the undercut to the patents. Reworded to "are
   cited on this sequence". The following sentence (`ctunm` sizing) stays.
6. **docs/steps/041-onom.md:136-137 — leak, same shape as #1.** "makes the
   same point about its own window" attributes the tunm.5 straddle rule to
   the patent. Reworded to "Cypress's integration patent, which may still
   be in force, is cited here too; the passage is in the collapsed note
   below." (no "this paragraph": the dropdown sits directly below, as the
   page already phrased other pointers on this page).

## tools/check_inforce.py: PHRASES extension

Added three fragments to the `US8093128B2` entry, each with a `--selftest`
case (open text refused, dropdown text allowed), as section 3e (after the
existing rd-figures-s3s4 3d block):

* `"dimensions and alignment of"` (catches ruling 3's leak)
* `"the masked region"` (catches ruling 2's leak)
* `"the isotropic etch leaves"` (catches ruling 5's leak)

**Phrase-choice note:** the review's own suggested fragment was the bare
`"the isotropic etch"`, said to "occur nowhere else on the site outside
tunm's notes". Grepping the fixed tree found that claim false: BUCK-1994's
entry in `docs/references/public-sources.md` (a plate/chrome-etch source,
unrelated to any patent) contains "...the isotropic etch undercuts the
chrome by about 150 nm...". Adding the bare fragment made check_inforce
report a false-positive leak on that unrelated inventory entry. Used the
longer, still-verbatim `"the isotropic etch leaves"` instead, which is not
a substring of the BUCK-1994 sentence and still catches ruling 5's leak.
Re-grepped all three final fragments against the whole `docs/` tree
(outside `docs/references/patents/` and `docs/plans/`, which the checker
itself skips): each matches only the ruled passages' notes.

**Verification (git show main:<page>, written under tmp/, git-ignored):**
with the three pages' pre-fix (`main`) text swapped in and the extended
PHRASES/checker in place, `tools/check_inforce.py` reports 3 problems (one
per ruling 2/3 combined on onom.md at one location, ruling 3 separately,
and ruling 5 on tunm.md — see below for the exact lines):

```
docs/masks/onom.md:280: phrase of US8093128B2 (GP40072804) outside a collapsed block: 'dimensions and alignment of'
docs/masks/onom.md:278: phrase of US8093128B2 (GP40072804) outside a collapsed block: 'the masked region'
docs/masks/tunm.md:308: phrase of US8093128B2 (GP40072804) outside a collapsed block: 'the isotropic etch leaves'
287 families not certainly expired (12 inventory keys, 13 footnote labels), 295 pages checked, 3 problems, 0 notes that can be opened up
```

(Ruling 1, 4 and 6's leaks have no non-patent-wording phrase that could
catch them, per the review: they attribute content without quoting the
patent's distinctive wording, so they are not — and cannot be — caught by
a `PHRASES` fragment; the fix is the pointer rewrite itself.)

With the three pages restored to their fixed (this branch's) text,
`tools/check_inforce.py` reports 0 problems, and `--selftest` passes.

## check_preserved.py (informational; not in the required gate list)

Run with `--base main`, no other flags (no dropdown body was edited, so
`--allow-dropdown-edits` was not needed):

* **docs/masks/onom.md**: 0 undeclared differences. WORDS LOST are the
  content words of the deleted/reworded clauses (patent, describes, notes,
  masked, region, dimensions, alignment, undercut, overlap, window, etc.)
  — expected, since ruling 2/3 delete a whole sentence and ruling 1/2
  reword a clause to a bare pointer. Destination: **deleted as ruled** (no
  non-patent source for this content exists on the page; ruling 3 says
  explicitly the reasoning is not to be moved into the note by this pass).
* **docs/masks/tunm.md**: 0 undeclared differences. Same shape: WORDS LOST
  are the content words of "takes the other view for tight layouts" and
  "describe the same sequence, the mask it uses and the undercut the
  isotropic etch leaves". Destination: **deleted as ruled**.
* **docs/steps/041-onom.md**: 1 undeclared difference — `LOST hedges:
  'about'` / `ADDED hedges: 'may'`. This is the same false-positive shape
  already documented in tmp/reviews/rd-masks-b.md section A and in
  docs/plans/progress-rd-inforce-sonos.md: `check_preserved`'s hedge list
  matches the bare word "about" regardless of context, and the deleted
  clause "about its own window" used it as a preposition, not a hedge; the
  added "which may still be in force" clause happens to contain "may".
  Destination: **deleted as ruled** (the deleted clause's content, "makes
  the same point about its own window", has no non-patent source and is
  the same leak shape as ruling 1). No word of the tunm.5 rule itself, or
  of the patent's flag/citation, changed.

No content was moved into any note in this task, so `--allow-dropdown-edits`
was never used, and no note gained an appended sentence.

## Status

- [x] onom.md (rulings 1, 2, 3)
- [x] tunm.md (rulings 4, 5)
- [x] docs/steps/041-onom.md (ruling 6)
- [x] tools/check_inforce.py PHRASES extension (3 fragments) + selftest
      cases; verified fails on pre-fix pages (3 problems), passes on fixed
      pages (0 problems), `--selftest` OK
- [x] check_preserved.py run and recorded per page (informational)
- [x] Checker suite: check_steps, check_refs, check_machines,
      check_materials, check_masks (and `--selftest`), check_papers,
      check_patents, check_filings, check_inforce (0 problems each);
      gen_papers, gen_patents, gen_filings, gen_index_links --check
      (0 problems each)
- [x] `sphinx-build -W -q -b html docs tmp/_build/html` — exit 0, no
      warnings
- [x] Push
