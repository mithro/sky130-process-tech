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

## In progress / next

* Committing the tool fix (this file + `tools/check_links.py`) before
  running the real, long, foreground site check per common rule 4 and
  the task's "commit the tool first" instruction.
* Full re-check of every hand-written page (chunked by directory, cache
  kept, foreground) — this is check 2 for the C5 "two checks ≥ 24 h
  apart" dead rule; `docs/plans/link-check-2026-09.md` (2026-09-19) is
  check 1.
* Early finding (smoke test, `--only-host jtec.utem.edu.my`, before the
  full run): `https://jtec.utem.edu.my/jtec/article/view/697` (THUNG-2016)
  now resolves **200 OK** directly. Check 1 failed (timeout, 2026-09-19);
  check 2 (today, 2026-09-20) succeeds — by the C5 rule ("two checks ≥
  24 h apart both fail") this is **not dead**, confirming report-C.md's
  C5 finding that the old report's "no snapshot" row for THUNG-2016 was
  wrong (the tool's stale/glitchy Wayback answer, not a real dead link).
  Checked commit `97d5754410a535c29357c96f5b1f76c155096824` ("Note
  THUNG-2016's article-view page timeout; point at the working PDF
  link"): it only added a note and surfaced the already-cited PDF link
  on all 11 repeating footnotes plus the inventory entry — **no
  quotation was removed under rule 11** for this source. Nothing to
  restore. No citation change needed for THUNG-2016 (leaving the
  existing "(times out as of 2026-09-19...)" note as a true, dated
  historical record — presentation-only, not something this branch
  rewrites).
* Still to do: the full run; verify (fetch `id_` form) and rewrite any
  link found genuinely dead by the two-check rule, in every repeating
  footnote and the inventory entry, C5 step-3 form; wording
  normalisation pass on existing Wayback citations where trivially
  safe; `docs/plans/link-check-2026-09b.md`; `check_preserved.py` on
  every page touched; the full checker/build suite from
  `tmp/prompts/rd-common.txt` rule 7.
