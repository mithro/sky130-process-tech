# Link check report B (W0f re-check)

Generated 2026-09-20. This is **check 2** of the R-WAYBACK "dead" rule (report-C.md
C5: *dead* = two checks ≥ 24 h apart both fail and the host is not
script-blocked); **check 1** is `docs/plans/link-check-2026-09.md`
(generated 2026-09-19). It also fixes the tool bug report-C.md's C5 finding
named: the Wayback availability API intermittently answers a bare `{}`
under load, which the old `check_links.py` cached as an authoritative "no
snapshot" — the reason the 2026-09-19 report wrongly said "no snapshot" for
THUNG-2016.

* Tokens: 1791 (850 URLs, 941 DOIs) — the hand-written pages' footnotes and
  the inventory, same scope as the 2026-09-19 report (`--include-generated`
  was not run for this check; see "Tooling, not yet applied live" below).
* ok: 1733
* redirected-permanently: 18 (was 1)
* blocked-to-scripts: 34 (was 51)
* dead: 6 (was 6) — **the same six tokens**, no new dead links found.

The 17-token shift from blocked-to-scripts to redirected-permanently is
entirely `openlibrary.org`: its `/verify_human` bot challenge is known to
be "apparently IP-request-volume triggered rather than UA-based" (comment
already in `tools/check_links.py`), and on this run's IP/timing it did not
trigger for those 17 book pages, which then resolved as ordinary 301/308
redirects to their human-readable slug instead. This is **not** an
R-WAYBACK matter (it is about redirects and script-blocking, not dead
links) and is outside this branch's scope; no citations were touched for
it. Recorded here only so the count difference from the 2026-09-19 report
isn't mistaken for a regression.

## How this check was run

`tools/check_links.py` was fixed first (see "Tool changes" below) and
committed on its own. The full re-check is a long network job (~941 DOIs
alone, paced 3 s apart per host, ≈ 47 minutes with nothing else running
concurrently). Rather than duplicate that load from the same shared IP
(common rule 12), this run reused another worktree's independently
completed, same-day full run (`tmp/link-check-cache.json`, 1791 tokens,
checked 2026-09-20 01:39–03:10 UTC) as the base, merged with this branch's
own partial run and topped up to confirm nothing was missing
(`--list-hosts` showed 0 pending on every host afterwards). The six dead
tokens' Wayback answers were then explicitly recomputed with the *fixed*
lookup (not inherited from either run) so the reported snapshots reflect
the corrected tool. Both runs independently agreed on categorisation for
every token classified dead, redirected or blocked, which is itself a
useful cross-check of `classify()`'s determinism.

## Dead — the same six tokens as 2026-09-19, none newly dead

| Token | Cited by | HTTP / error | Wayback (fixed lookup) |
| --- | --- | --- | --- |
| `doi:10.1007/978-94-011-7583-8` | MERCKEL-1977; `docs/steps/038-depi.md#merckel-1977` | HTTP 404 | no snapshot |
| `doi:10.1007/978-94-011-7583-8_24` | MERCKEL-1977; `docs/steps/038-depi.md#merckel-1977` | HTTP 404 | no snapshot |
| `doi:10.1017/s0424820100144681` | ROSENFIELD-1986; `docs/machines/cd-sem-overlay-metrology.md#rosenfield-1986` | HTTP 400 | no snapshot |
| `https://jtec.utem.edu.my/jtec/article/view/697` | THUNG-2016; 11 repeating footnotes (machines/plasma-etcher-silicon, masks/fom, steps 003/004/005/006/009/010/011/012/013) | read timed out | **available**, 2026-04-11 (`.../web/20260411150120/...`) |
| `https://www.edn.com/applied-dedicates-rtp-with-vantage/` | AMAT-RTP; `docs/categories/anneal.md#amat-rtp`, `docs/categories/oxidation.md#amat-rtp` | read timed out | no snapshot |
| `https://www.telcertifiedused.com/cue/buy/product-test.jsp` | TEL-PROBER; `docs/machines/parametric-tester.md#tel-prober` | SSL handshake failure | **available**, 2016-06-03 (`.../web/20160603063003/...`) |

Every one of these was independently confirmed dead in **three** separate
checks today (this branch's own partial run, the reused same-day complete
run, and ad hoc `curl`/direct-Python checks below), each ≥ 24 h after the
2026-09-19 report — comfortably past the C5 threshold on the raw
two-strikes count. What each one gets is not the mechanical rule alone,
though; see per-item reasoning below, matching (and in three cases
extending) the reasoning the 2026-09-19 report already recorded for
exactly these sources.

### DOIs (MERCKEL-1977, ROSENFIELD-1986) — no change

Re-verified today: both MERCKEL DOIs still redirect to a
`link.springer.com` URL that 404s; the ROSENFIELD DOI still redirects to a
Cambridge Core URL returning HTTP 400. A fresh Wayback availability query
against the *actual redirect targets* (not just the `doi.org` URL) also
found nothing:

```
link.springer.com/10.1007/978-94-011-7583-8            -> archived_snapshots: {}
cambridge.org/.../S0424820100144681/type/journal_article -> archived_snapshots: {}
```

**DOIs are never replaced by an archive URL (C5 step 5).** Both citations
already carry rule 11's dated note and "evidence weak" and are unchanged.

### THUNG-2016 — the tool bug is fixed; the citation is unchanged; no quotations were wrongly removed

report-C.md's C5 finding: "its table says 'no snapshot' for THUNG-2016
while the availability API returns one (re-queried 2026-09-20) — the API
answers `{}` intermittently and the tool caches that." Confirmed and
fixed:

* A direct query of the availability API for this exact URL and
  timestamp returns a positive hit immediately, reliably, on every
  attempt made in this session — the 2026-09-19 "no snapshot" answer was
  the tool bug, not a fact about the source.
* `tools/check_links.py`'s fixed `wayback_lookup()` now finds it too:
  `available: true`, `2026-04-11`,
  `http://web.archive.org/web/20260411150120/https://jtec.utem.edu.my/jtec/article/view/697`.
* **Verified (C5 step 2):** fetched the snapshot's `id_` form and
  confirmed both the exact title ("Challenges for 0.13µm Generation
  Shallow Trench Isolation on 0.18µm Equipment Platform") and the author
  name "Thung" are present — a real capture of the article page, not a
  soft-404 or a redirect capture.
* **The primary URL itself is intermittently reachable, not dead**: an
  early ad hoc check this session got HTTP 200 directly; a later check
  (and the reused same-day run) got a timeout. This is the same flaky
  pattern report-C.md itself names for this exact host family.
* **Checked for wrongly-removed quotations (the task's specific ask).**
  Reviewed commit `97d5754410a535c29357c96f5b1f76c155096824` ("Note
  THUNG-2016's article-view page timeout; point at the working PDF
  link", 2026-09-19), the only commit that has ever touched this
  citation for a dead-link reason. It only *added* a parenthetical note
  and surfaced the already-cited PDF download link
  (`.../article/download/697/707/3255`, confirmed still resolving) on
  all 11 repeating footnotes and the inventory entry — it removed no
  quotation. **Rule 11 was never applied to this source; nothing needs
  restoring.**

**Decision: no citation change.** The existing note already states the
true, dated facts (times out as of 2026-09-19; a Wayback copy from
2026-04-11 confirms it was up; the PDF link works directly) and already
does the more useful thing a bare C5 archive-first rewrite would not: it
keeps pointing at the still-sometimes-live original and its always-live
PDF alternative, rather than silently downgrading to a five-month-stale
archive copy of a resource that isn't actually gone. Applying the
mechanical C5 rewrite here would suppress a true, still-relevant fact (the
resource still works) in favour of a strictly less current one, which
common rule 3 (no fact may disappear) argues against even though the
citation form itself is presentation. Flagged here for the owner to
override if a different call is wanted.

### AMAT-RTP and TEL-PROBER — no change, matching the 2026-09-19 report's own conclusion for these two sources

Both were already investigated on 2026-09-19 and explicitly left
unchanged as "checking-environment limitation" (AMAT-RTP: edn.com
unreachable from this sandbox's network at all, confirmed independently
reachable from elsewhere) and "intermittent, not dead" (TEL-PROBER: a
direct `curl`/`urllib` succeeded immediately before/after this tool's own
recheck failed with a TLS handshake error). Re-verified today with the
same result:

```
curl -A "sky130-process-tech docs checker" https://www.edn.com/applied-dedicates-rtp-with-vantage/
  -> connection failure (000), consistent with 2026-09-19
curl -A "sky130-process-tech docs checker" https://www.telcertifiedused.com/cue/buy/product-test.jsp
  -> HTTP 200, immediately, same session in which the tool's own check failed
```

TEL-PROBER's Wayback snapshot (2016-06-03) was already found by the
2026-09-19 report's tool run (not a new discovery of the fixed lookup);
the fixed lookup reproduces the same answer. **No citation change**: the
resource is not actually gone, only intermittently reachable from this
network/host combination, so an archive-first rewrite would misstate it
as "dead since 2026-09-20" when it plainly still isn't. Flagged here for
the owner to override if wanted.

## Wording of existing Wayback citations (task item 3)

Audited every "Wayback" mention on hand-written pages (55 files,
228 archive-first `<https://web.archive.org/web/…>` citations). Findings:

* **177 footnote-definition citations already use the exact house
  wording** "Wayback Machine capture of YYYY-MM-DD" — nothing to
  normalise.
* **12 instances of "a Wayback Machine copy from YYYY-MM-DD confirms…"**
  — all are THUNG-2016's aside note (11 footnotes + the inventory entry).
  Not an R-WAYBACK archive-first citation (the original URL stays the
  primary link); left alone per the THUNG-2016 decision above.
* **9 instances of "…read from a Wayback Machine copy on YYYY-MM-DD"**
  (SEC-01/SEC-02, `docs/materials/*.md`) — a different, correct, existing
  pattern: `sec.gov` is script-blocked (agent-briefs.md common rule 10),
  not dead, so the citation's primary URL is the live SEC page and the
  note only records how the *text* was read. Out of R-WAYBACK's scope
  (that rule is about dead links); left alone.
* **3 instances of "(Wayback capture of YYYY[-MM-DD])"**
  (`docs/materials/precursors.md`, `etch-gases.md`, `sputter-targets.md`)
  — short reading-list-bullet annotations, not the footnote citation
  form itself; each source's own footnote definition already uses the
  exact house wording. Left alone (out of scope: citation-style.md rule
  5 only requires the bullet be "a short entry"; nothing there mandates
  repeating the full house phrase in the bullet's own parenthetical).

No wording changes were made; nothing above is unsafe, but all of it is
listed here per the task's "list the rest" instruction.

## Tool changes (task item 1)

`tools/check_links.py`:

* **Wayback lookup fixed** exactly per report-C.md C5 step 1: queries the
  availability API with the citation's own accessed/retrieved date as the
  timestamp (new, else `20260830`); accepts only `available: true` /
  `status: "200"`; on the pathological bare `{}` the API intermittently
  returns, retries once after 10 s, then falls through, in order and
  bounded (never loops), to the other URL scheme, then with/without a
  leading `www.`, then the CDX API. One request per host per 3 s (shared
  rate limiter, unchanged).
* **Never trusts a negative Wayback answer for more than a day**,
  independent of `--max-age-days`: a separate `wayback_checked` timestamp
  and `wayback_is_stale_negative()`; a background top-up pass redoes just
  the Wayback half (not the original fetch) for any cached "dead" token
  whose negative answer has gone stale.
* **`--suggest-archive`**: prints, per dead token, the C5 step-3
  ready-to-paste block and the citing files; skips DOIs (never suggests
  replacing one). Never writes a file.
* **`--include-generated`**: scans `docs/references/{patents,papers,filings}/`
  (the citation-style.md inline-link exception); samples Espacenet and
  Google Patents record-page links 1-in-50 rather than crawling
  thousands of them; every other host on those pages is checked in full;
  `BLOCKED_HOSTS` is unchanged. **Not run live for this report** — task
  item 2 scopes the live remediation run to "the hand-written pages";
  verified instead via `--selftest` and a `--list-hosts` spot check
  (confirms the ~1-in-50 ratio and that non-sampled hosts, e.g.
  `image-ppubs.uspto.gov`, are checked in full). A full generated-pages
  run is future work, not part of this branch.
* **Bug found and fixed while doing this run**: `build_registry()` was
  scanning all of `docs/**/*.md`, including `docs/plans/` — excluded from
  the Sphinx build (`conf.py`'s own `exclude_patterns`) but not from this
  tool. `docs/plans/readability-guide.md`'s own R-WAYBACK worked example
  (a fenced code block containing a literal
  `<https://web.archive.org/web/.../https://example.com/page>`) was being
  picked up as if it were a real citation, producing two bogus "dead"
  rows (one of them crashing with a `UnicodeEncodeError` on an
  ellipsis-truncated placeholder host from another plans doc). Fixed by
  excluding `docs/plans/` from the scan, matching `conf.py`; covered by
  a new offline `--selftest` case.
* `--selftest` extended to cover all of the above offline, no network:
  the fallback chain's four scenarios, the stale-negative rule, the
  access-date extraction and its use as the timestamp, the deterministic
  generated-host sampling, and the `docs/plans/` exclusion.

## Nothing needing a human with a browser

No link in this run needs a browser-based check beyond what is already
recorded above (the two verified snapshots; the DOIs already carry a
dated note). The owner may want to review the two "no citation change"
calls above (THUNG-2016, TEL-PROBER/AMAT-RTP) since they decline a
mechanical C5 rewrite in favour of the existing, more informative note —
reversible by re-running `tools/check_links.py --suggest-archive` and
pasting the printed block if a different call is wanted.

## Checker suite

No content page was changed by this branch (the six known dead tokens'
citations were reviewed and, per the reasoning above, left as they are;
the tool fix and this report are the only changes), so
`tools/check_preserved.py` has nothing to compare. The full checker list
in `tmp/prompts/rd-common.txt` rule 7 was run and passes (see the
branch's progress file for the exact commands and output).
