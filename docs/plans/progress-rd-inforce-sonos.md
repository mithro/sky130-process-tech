# Progress: rd-inforce-sonos

Task: fix in-force-patent content that sits in the open on the SONOS/gate-oxide
pages (037-045), per tmp/reviews/rd-figures-s3s4.md "Existing pages" section.
Worktree: .worktrees/rd-inforce-sonos, branch topic/rd-inforce-sonos.

## Rulings to apply (reviewer's exact fix)

1. **037:115-117 — indium leak.** Cut "implants the memory-transistor channel
   with indium at an energy and dose given in the collapsed note below this
   list, and" down to "describes its own channel implant in the collapsed
   note below this list, and". Public indium case ([^cyp-25], Shahidi) stays.
2. **042:68-70 — leak.** Delete "only tens of nanometres thick in the Cypress
   patent (collapsed note below this section)"; re-source in the open to
   "of the order of 10-20 nm on the era-typical range {ref}`BOX <step-002>`
   gives".
3. **038:158-161 — leak.** Replace "of the thickness a Cypress patent that
   may still be in force gives it (collapsed note below this list)" with
   "for the 2 nm lower oxide of Wikipedia's generic SONOS stack[^cyp-26]"
   (reviewer's option 1; [^cyp-26] already defined/used on this page).
4. **039:128-130 — public knowledge.** Re-source "far too fast to control for
   a 10-20 nm film" to "…for a pad oxide of the order of 10-20 nm (the
   era-typical range on {ref}`BOX <step-002>`)…".
5. **040:73-77 — public knowledge.** Replace "on the published patent ranges
   (the collapsed notes on this page)" with "on the expired ONO patent's
   'less than about 25 Å'[^pat-01] and Wikipedia's generic 2 nm[^cyp-26]".

## Eight open summaries (Never §2.5) — decisions

| Passage | Verdict | Action |
|---|---|---|
| 042:36-40 "describes exactly this two-stage approach...the same patterning" | distinctive content (confirms patents match the inferred sequence exactly) | moved confirming clause into the existing dropdown (43-56) as a lead sentence; left a bare pointer in the open |
| 042:139-142 "One of them warns...the other protects...sacrificial cap" | duplicate of what the dropdown at 155-167 already states verbatim | deleted from open (content already safe in dropdown); left the existing pointer ("both passages are in that note") |
| 042:300 "removed dry (as the Cypress patents describe)" | attributes an inferred process fact to the patents in the open | deleted the attributing clause "(as the Cypress patents describe)"; the dry/wet uncertainty stays, unattributed |
| 043:58-70 "keeps the blocking oxide from growing too thick" | paraphrase of the US 9,824,895 PHRASE "it may be grown to be too thick", already safely quoted in the dropdown just below | reworded to a bare pointer: "How SKY130 manages this during the oxidation is not public." |
| 044:57-60 "its equivalent resist does exactly that" | confirms an exact match between SKY130's inferred practice and the patent's — content | deleted the confirming clause; kept the existing pointer ("its wording is in the collapsed note below") |
| 040:170-181 "one of them completes the layer at the logic gate oxidation"; step 5 sacrificial-cap function | (a) duplicate of dropdown text at 209-211; (b) distinctive pat-04 content dressed as generic practice | (a) deleted the clause (content already in dropdown); (b) moved "protects the blocking oxide through the ONO patterning" verbatim into the "Sacrificial cap and metrology" dropdown paragraph, left a bare pointer in the open |
| 045:42-46 | reviewer's table entry is empty ("—") | reviewed: the passage ("a Cypress patent...says what an implant does to an oxide that is then stripped (collapsed note below)") is already a compliant generic pointer, naming no content. No change made. |
| 039:23-24 "uses a wet chemistry of its own" | confirms the patent's technique matches the inferred wet etch — content, and redundant with the paragraph's own closing pointer | deleted the clause "and the Cypress patent, which may still be in force, uses a wet chemistry of its own (collapsed note below)"; kept the paragraph's closing pointer sentence |

## check_preserved (per page, `--allow-dropdown-edits` + `--allow-regrouped`,
`--allow-added` as noted; ran per commit, `--base main`)

* **037-ptsi.md**: clean, 0 undeclared differences.
* **038-depi.md** (`--allow-added markers,numbers,number_order`): LOST hedges
  'may' — part of the deleted "a Cypress patent that may still be in force
  gives it" attributing clause; the patent's in-force status is still stated
  via this page's own dropdown and its flag sentence. Deleted as ruled.
* **039-tunme.md** (`--allow-added markers,numbers,refs,hedges`): LOST
  hedges 'may' — same pattern, from the deleted "which may still be in
  force" clause in the 23-24 fix. Deleted as ruled.
* **040-ono.md** (`--allow-added markers,numbers,number_order,quotes,hedges`):
  LOST refs 'step-043' (one instance) — from the deleted step-4 clause
  "...completes the layer at the logic gate oxidation ({ref}`GOX100
  <step-043>`)"; content already in the dropdown at 209-211, and two other
  {ref}`GOX100 <step-043>` links remain on the page. Deleted as ruled.
* **042-onome.md** (`--allow-added markers,numbers,refs,quotes,hedges`):
  - LOST quotes (one pair, both truncated to the same "class of tool..."
    prefix): a pre-existing checker artifact, not a real content loss —
    `check_preserved`'s "quotes" scan already pairs a quote mark inside the
    dropdown's block quote with "poly/nitride"'s quote mark *on main*
    (verified directly against `check_preserved.extract_all()` on both
    `main` and this branch's text); editing anything between them changes
    the bogus paired substring. "poly/nitride", "selectivity to oxide" and
    "stop on a thin oxide without trenching the silicon" are all still on
    the page, unchanged.
  - LOST hedges 'about' — from deleting "warns about" in the 139-142 fix
    (the idiom "warns about", not an epistemic hedge); the warning's content
    is still verbatim in the dropdown at 155-167.
* **043-gox100.md**: clean, 0 undeclared differences.
* **044-lvom.md**: clean, 0 undeclared differences.
* **045-nchi.md**: no edit, not run.

## Status

- [x] 037-ptsi.md (indium leak)
- [x] 038-depi.md (leak, re-source)
- [x] 039-tunme.md (public knowledge + open summary)
- [x] 040-ono.md (public knowledge + two open summaries)
- [x] 042-onome.md (leak + three open summaries)
- [x] 043-gox100.md (open summary)
- [x] 044-lvom.md (open summary)
- [x] 045-nchi.md (reviewed, no change needed)
- [x] tools/check_inforce.py PHRASES extension + selftest cases (3d): verified
      the checker now fails on `main`'s pre-fix 037/042/043 and passes (0
      problems) on this branch's fixed pages
- [x] Full checker suite: check_steps, check_refs, check_machines,
      check_materials, check_masks, check_papers, check_patents,
      check_filings, check_inforce (0 problems each); gen_papers,
      gen_patents, gen_filings, gen_index_links --check (0 problems each);
      `sphinx-build -W -q -b html docs tmp/_build/html` rc 0
- [ ] Push

## Notes

- 038's leak is an *arithmetic* leak (46% x the patent's 1-3/1-4 nm range ~=
  "order 1 nm"): no literal patent phrase to add to PHRASES for it.
- main has moved since this branch's base; another branch
  (topic/rd-figures-s3s4) inserts figure blocks on these same pages. Edits
  here are kept to the exact lines the rulings/summaries name, to keep a
  rebase clean.
