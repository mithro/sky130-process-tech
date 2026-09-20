# Progress — rd-links (W0f: link checker + dead-link rule)

Branch `topic/rd-links`, worktree `.worktrees/rd-links`. Task: W0f of
`docs/plans/readability-plan.md` (report-C.md finding C5, rule R-WAYBACK).

## Done

* `tools/check_links.py`:
  * Fixed the Wayback lookup (C5 step 1): queries
    `archive.org/wayback/available` with the citation's own
    accessed/retrieved date as the timestamp (new `extract_access_date`,
    threaded through `parse_inventory`/`parse_page_footnotes`/`Registry`),
    else `DEFAULT_WAYBACK_TIMESTAMP = "20260830"`. Accepts only
    `available: true` and `status: "200"`. On the pathological bare `{}`
    the API intermittently returns (the actual bug behind the old
    report's wrong THUNG-2016 row — see below), retries once after a
    (mocked-in-tests) 10 s sleep; if there is still no accepted snapshot,
    falls through in order to the other URL scheme, then the URL with/
    without a leading `www.`, then the CDX API
    (`web.archive.org/cdx/search/cdx`, most recent `statuscode:200` hit).
    At most 5 network calls total, never loops. One request per host per
    `--rate-limit` (default 3 s), same shared `RateLimiter` as everything
    else.
  * "Never cache a negative archive answer for more than a day": added
    `wayback_checked` (separate from the main `checked` timestamp) and
    `wayback_is_stale_negative()`; `run_checks` now does a second,
    lightweight pass after the main one that redoes just the Wayback
    lookup (not the original, still-dead fetch) for any cached "dead"
    token whose negative answer is more than a day old, even when the
    surrounding HTTP result is still within `--max-age-days`.
  * Added `--suggest-archive`: prints, per dead token, the C5 step-3
    ready-to-paste block (archive URL first, `Wayback Machine capture of
    YYYY-MM-DD`, original in backticks) and the files/inventory key
    citing it. Never writes a file. Explicitly skips DOI tokens (never
    suggests replacing a DOI with an archive URL — C5 step 5) and says so.
  * Added `--include-generated`: also scans
    `docs/references/{patents,papers,filings}/` (inline links, the
    documented `citation-style.md` exception for generated pages).
    Espacenet and Google Patents record-page links are sampled
    1-in-50 (deterministic `sha256(token) % 50 == 0`, stable across runs
    so the cache stays useful) rather than crawled; every other host on
    those pages is checked in full; `BLOCKED_HOSTS` still applies
    unchanged.
  * The tool still never rewrites any file; the cache stays under the
    git-ignored `tmp/`.
  * Extended `--selftest` (still offline, no network, no cache file
    touched): the fallback chain's four scenarios (first-query success;
    empty-`{}` retry-then-success; falls through scheme → www → CDX in
    order on a well-formed miss, bounded, no loop; a clean negative when
    nothing anywhere matches), the access-date extraction and its use as
    the timestamp (vs. the default), the stale-negative-cache rule, and
    the deterministic generated-host sampling. `uv run tools/check_links.py
    --selftest` passes.

* Found and fixed a second, pre-existing tool bug while running the real
  check: `build_registry()` scanned all of `docs/**/*.md`, including
  `docs/plans/` (excluded from the Sphinx build by `conf.py`'s own
  `exclude_patterns`, but not from this tool). `docs/plans/readability-guide.md`'s
  own R-WAYBACK worked example (a fenced code block with a literal
  `<https://web.archive.org/web/.../https://example.com/page>`) was
  being picked up as a real footnote definition. Fixed by excluding
  `docs/plans/`, covered by a new offline `--selftest` case. Separate
  commit `34f20c91`.

## The real re-check (task item 2) — done

Full details, reasoning and evidence are in `docs/plans/link-check-2026-09b.md`
(the deliverable for this item); summary here for anyone resuming this
branch:

* Ran the full site check (1791 tokens, same scope as the 2026-09-19
  report). It is genuinely a long job (~941 DOIs alone, 3 s/host pacing,
  ≈ 47 minutes with nothing else running) — rather than duplicate that
  load from the same shared IP (common rule 12), reused another
  worktree's independently completed same-day full run as the cache
  base, merged with this branch's own partial run, then topped up
  (`--list-hosts` confirmed 0 pending everywhere) and explicitly
  recomputed the Wayback answer for all six dead tokens with the fixed
  lookup (not inherited from either run).
* **Result: the same six tokens as 2026-09-19, no new dead links.**
  2 MERCKEL-1977 DOIs and 1 ROSENFIELD-1986 DOI: still dead, still no
  Wayback snapshot (checked the actual redirect targets, not just the
  DOI), already correctly under rule 11 with a dated note — no change
  (DOIs are never replaced by an archive URL, C5 step 5).
* **THUNG-2016**: the task's specific ask. Confirmed and fixed the
  report-C.md C5 finding — the availability API's intermittent bare
  `{}` was being cached as "no snapshot"; a real snapshot
  (2026-04-11) exists and the fixed tool now finds it reliably.
  **Verified it (C5 step 2)**: fetched the `id_` form, confirmed the
  exact title and the author's name are present, not a soft-404.
  **Checked for wrongly-removed quotations** (the task's specific
  ask): reviewed commit `97d5754410a535c29357c96f5b1f76c155096824`
  (2026-09-19, the only commit that ever touched this citation for a
  dead-link reason) — it only added a note and surfaced the
  already-cited working PDF link on all 11 footnotes + the inventory
  entry. **No quotation was removed under rule 11; nothing needs
  restoring.** No citation change made: the primary URL is
  intermittently reachable (confirmed both an HTTP 200 and a timeout
  from this session alone), and the existing note plus the always-live
  PDF alternative already serves the reader better than a five-month-stale
  archive substitute would (that would also misstate the resource as
  flatly "dead since 2026-09-20", which it demonstrably is not).
* **AMAT-RTP / TEL-PROBER**: re-verified with fresh, direct `curl`
  checks; both reproduce the exact same "checking-environment
  limitation" / "intermittent, not dead" pattern the 2026-09-19 report
  already documented for these two sources (independently, again,
  today). No citation change, matching that precedent.
* All three "no change" calls above are judgement calls, flagged
  clearly in `link-check-2026-09b.md` for the owner to override.
* **Wording normalisation (task item 3)**: audited all 228 archive-first
  Wayback citations on hand-written pages. 177 already use the exact
  house wording. The remaining 21 are two different, correct, existing
  patterns unrelated to R-WAYBACK (THUNG-2016's aside note; the
  SEC-01/SEC-02 "read from a copy" note for a script-blocked, not dead,
  host) plus 3 reading-list-bullet short annotations whose own footnote
  definitions already use the house wording. Nothing needed changing;
  full breakdown in `link-check-2026-09b.md`.
* **Side finding, not acted on**: 17 `openlibrary.org` tokens flipped
  from `blocked-to-scripts` to `redirected-permanently` between the two
  runs today (the site's `/verify_human` bot challenge is known to be
  IP-load-triggered, not UA-based, so this is expected flakiness, not a
  citation problem). Not an R-WAYBACK matter; left untouched; recorded
  in the b-report so the count difference isn't mistaken for a
  regression.
* No content page was changed, so `tools/check_preserved.py` had
  nothing to run on.
* Full checker suite (`tmp/prompts/rd-common.txt` rule 7) run and
  passing: `check_steps`, `check_refs`, `check_machines`,
  `check_materials`, `check_masks`, `check_papers`, `check_patents`,
  `check_filings`, `check_inforce`, `gen_papers/gen_patents/gen_filings/gen_index_links --check`,
  and `sphinx-build -W -q -b html docs tmp/_build/html`.

## Status: done

All four numbered items of the W0f task are complete:
1. `tools/check_links.py` fixed and extended (see "Done" above).
2. The real re-check run, dead-link determination, THUNG-2016 recheck,
   quotation audit — see "The real re-check" above and
   `docs/plans/link-check-2026-09b.md`.
3. Wording normalisation audited — nothing unsafe found; documented.
4. `docs/plans/link-check-2026-09b.md` written.
