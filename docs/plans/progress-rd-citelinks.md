# Progress — rd-citelinks (W0c: reading-list and named-title links)

Task: `docs/plans/readability-plan.md` W0c. Spec: `docs/plans/readability/report-C.md` C1/C4,
`docs/plans/readability-guide.md` R-LINKS and the Never list, `docs/plans/citation-style.md`,
`tools/check_refs.py`, `tools/check_inforce.py`, `tools/check_links.py`. Prototype:
`docs/plans/readability/prototypes/links-theme/titlelink_dryrun.py`.

## Plan (commit order)

1. [x] Policy: reword `citation-style.md` rule 5; R-LINKS already matched the new wording, no change
   needed there; added a clarifying sentence to `agent-briefs.md`.
2. [ ] `check_refs.py` invariant + selftest.
3. [ ] `tools/fix_reading_list_links.py` (rules 1–3 of C1) + selftest + `--check`.
4. [ ] Run site-wide, one commit per directory; checkers + `-W` build after each.
5. [ ] Hand-finish unambiguous leftovers under rules 2–3.
6. [ ] C4 row 2 script: named italic titles in prose linked, first occurrence per H2.
7. [ ] `docs/references/index.md` "How citations work" wording.

## Decisions / notes

* citation-style.md rule 5 now says the bullet head links to the first URL of its own `[^label]:`
  definition; the footnote is unchanged and stays (full citation, hover card, inventory key).
* No change was needed to `readability-guide.md`'s R-LINKS section: it already specifies exactly this
  behaviour (it was written anticipating W0c landing).

## Open points for the coordinator

(none yet)
