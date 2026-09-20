# Link check report B (W0f re-check)

Generated 2026-09-20, in two passes: the original W0f re-check, then a
coordinator follow-up that converts the confirmed-dead links, adds a
soft-404 ("soft-dead?") check and a cross-domain-redirect review, and
runs `--include-generated`. This is **check 2** of the R-WAYBACK "dead"
rule (report-C.md C5: *dead* = two checks ≥ 24 h apart both fail and the
host is not script-blocked); **check 1** is
`docs/plans/link-check-2026-09.md` (2026-09-19).

## Counts

* Hand-written pages (footnotes + inventory), same scope as the
  2026-09-19 report: 1791 tokens (850 URLs, 941 DOIs).
  * ok: 1578
  * blocked-to-scripts: 172 (was 51) — see "The IOP Science finding"
  * redirected-permanently: 18 (was 1) — openlibrary.org flakiness, see
    below; not an R-WAYBACK matter
  * soft-dead? (suspects, all reviewed): 19 → 0 needing action (all
    false positives of the heuristic or intermittent hosts already
    covered by an existing precedent) — see "Soft-dead? suspects"
  * dead: 6 (was 6), the same six tokens, no new dead links
* Generated pages (`docs/references/{patents,papers,filings}/`,
  `--include-generated`, Espacenet/Google Patents sampled 1-in-50):
  checked for the **first time ever** — 2540 tokens total (749 new).
  * ok: 2048 (of the whole 2540-token set, hand-written pages included)
  * blocked-to-scripts: 438 (see "Generated pages" below — mostly new
    hosts this run added, all reachable, all script-blocking)
  * redirected-permanently: 20 (18 hand-written + 2 new, Infineon annual
    reports that moved to a new canonical URL; still resolve, no action)
  * dead: 10 (the same 6 hand-written ones + 4 new — **first check
    only, not yet "dead" by the two-check rule**; see below)
  * soft-dead?: 19 (unchanged — `--include-generated` ran with
    `--no-soft-dead`, see "Generated pages")

**Converted to Wayback form (C5 step 3):** 2 (THUNG-2016, TEL-PROBER).
**Moved:** 0. **Rule 11 applied:** 1 (AMAT-RTP). **Suspects cleared
(fine or intermittent, no edit):** 19 hand-written-page soft-dead
suspects + the cross-domain redirects reviewed below. **Left for a
human:** the IOP Science / Radware finding needs no citation edit (nature
of a script-block, not a dead link) but is worth the owner knowing about
directly; see "Needs a human with a browser".

## 1. Converted, moved, and rule-11 (task item 1)

### THUNG-2016 — converted to the C5 step-3 form

Failed two checks ≥ 24 h apart (2026-09-19 report; today, independently,
three times: this branch's partial run, a reused same-day complete run
from another worktree, and ad hoc `curl`s). A snapshot exists and is
verified: fetched the `id_` form of
`https://web.archive.org/web/20260411150120/...` and confirmed both the
exact title ("Challenges for 0.13µm Generation Shallow Trench Isolation
on 0.18µm Equipment Platform") and the author name "Thung" are present —
not a soft-404 or a redirect capture.

Rewrote all 11 repeating footnote definitions (`docs/machines/plasma-etcher-silicon.md`,
`docs/masks/fom.md`, `docs/steps/{003,004,005,006,009,010,011,012,013}-*.md`)
and the inventory entry (`docs/references/public-sources.md`) to the C5
step-3 form: archive URL first, original in backticks, "Wayback Machine
capture of 2026-04-11", "dead since 2026-09-19" (the date of the first
confirmed failure). The already-cited, still-working PDF alternative
(`.../article/download/697/707/3255`) is kept alongside, unchanged — a
real, additional fact, not something C5 asks to remove.

**Checked for wrongly-removed quotations (the task's specific ask).**
Reviewed commit `97d5754410a535c29357c96f5b1f76c155096824` ("Note
THUNG-2016's article-view page timeout...", 2026-09-19), the only commit
that ever touched this citation for a dead-link reason: it only added a
note and surfaced the PDF link, on all 11 footnotes and the inventory
entry. **Rule 11 was never applied to this source; nothing needs
restoring.**

### TEL-PROBER — converted to the C5 step-3 form

Same two-check failure pattern; a snapshot from 2016-06-03 exists (the
2026-09-19 report's own tool run already found it) and is verified (the
`id_` form contains "P-8XL", "P-12XL", "Wafer Prober", "Tokyo Electron").
Rewrote the one footnote definition (`docs/machines/parametric-tester.md`)
and the inventory entry to the C5 step-3 form; "dead since 2026-09-19".

### AMAT-RTP — rule 11 applied

Tried the remaining C5 fallbacks by hand: the other URL scheme, the
`www.` toggle, the CDX API (all empty), and one `archive.ph/newest/`
request (HTTP 429, rate-limited — inconclusive, not a hit; common rule 9
says never loop on a 429, so left at one try). No snapshot found
anywhere. Applied rule 11 of `agent-briefs.md` as written:

* Removed the one verbatim quotation resting on this source
  (`docs/categories/anneal.md`: "the temperature 100 times per second at
  seven different places on the wafer"), replaced with a weak-evidence,
  dated mention that keeps the claim it can still support (the chamber
  names) without the unverifiable specific.
* Added the same dated note ("No longer retrievable as of 2026-09-19
  (confirmed again 2026-09-20); no Wayback, CDX or archive.ph copy
  found") to both citing pages' footnote definitions
  (`docs/categories/anneal.md`, `docs/categories/oxidation.md`) and the
  inventory entry, with "evidence weak" recorded (inventory: at the Tier
  line, matching the existing ROSENFIELD-1986 precedent; footnote defs:
  inline, matching the same precedent).

### The other four known-dead tokens — DOIs, unchanged

MERCKEL-1977 (2 DOIs) and ROSENFIELD-1986 (1 DOI): re-verified still
dead (still 404 / 400 at their redirect targets), still no Wayback
snapshot anywhere (checked the actual `link.springer.com` /
`cambridge.org` landing pages, not just the `doi.org` URL). Already
correctly under rule 11 from an earlier round; **DOIs are never replaced
by an archive URL (C5 step 5)** — no change.

### `check_preserved.py`

Run with explicit paths on every changed page (the default whole-repo
auto-discovery picks up unrelated drift from other branches merged into
`main` since this worktree was created, and trips a pre-existing
`check_preserved.py` crash on one of those files' `number_order` tuples —
not touched here). Clean apart from the intended, declared changes:

* `--allow-added urls,numbers,number_order,footnotes` (`footnotes` is a
  whole-text field per label; any definition edit shows as a LOST+ADDED
  pair for that one label, unavoidably, since a loss can never be
  declared away — the 13 pairs are exactly the 13 rewritten citations,
  nothing else).
* One substantive `LOST quotes`/`LOST numbers` in `anneal.md`: the
  removed AMAT-RTP quotation and its "100" — rule 11's own removal, not
  an oversight.
* The remaining `number_order` LOST/ADDED pairs are the heuristic
  sentence-splitter regrouping around newly inserted dates (confirmed no
  number itself was lost — the plain `numbers` category shows only
  additions).

## 2. What the checker misses (task item 2)

### (a) Soft-404 detection — added to `tools/check_links.py`

A new `soft-dead?` classification: for every non-DOI token classified
`ok`/`redirected-permanently`, one extra GET (a body the main HEAD/GET
check doesn't necessarily read) feeds cheap heuristics — final-URL path
collapsed to a shorter prefix or the site root, a generic
landing/search/login/error path, a fetched `<title>`/`<h1>` containing a
not-found/error phrase, a suspiciously thin body, or a fetched title
sharing no significant word with the cited `*Title*` (extracted from the
same footnote/inventory block, nearest-preceding the URL). Never
auto-decided: it only ever flags a suspect, never reclassifies to dead.
`--selftest` covers every heuristic with canned inputs, offline.

Two real bugs were found and fixed while building this (see "Tool
changes" below): the cited-title extraction was per-block instead of
per-URL, and it didn't handle a title wrapped across a hard-wrapped
source line.

### Soft-dead? suspects on hand-written pages — 19 found, all reviewed, none need an edit

| Token | Reason(s) flagged | Decision | Evidence |
| --- | --- | --- | --- |
| `docs.google.com/.../edit#gid=...` (PDK-09) | title mismatch | Fine | Title-extraction bug (see below), fixed; re-verified the fetched title now matches PDK-09's own cited title exactly |
| `en.wikipedia.org/wiki/Control_Data_Corporation` (CYP-13) | title mismatch | Fine | CYP-13 cites two titles then both URLs in one sentence — an ambiguous pattern the nearest-preceding heuristic can't fully resolve (documented limitation); content matches CYP-13's own claim |
| `en.wikipedia.org/wiki/MEMC_Electronic_Materials` | title mismatch | Fine | Wikipedia retitled the article to SunEdison (MEMC's successor); same URL, content still covers MEMC |
| `github.com/.../blob/.../mdm-format.png` | title mismatch | Fine | GitHub's blob viewer always shows a generic repo/path title for a raw file, never the cited work's title |
| `github.com/.../blob/.../pad-documentation.csv` | title mismatch | Fine | Same as above |
| `people.ece.ubc.ca/.../icug136.html` (RAW-DATA-MDM) | title mismatch | Fine | The citation's own text says this chapter is titled "MDM File Structure" — matches exactly once the title-extraction bug (below) is fixed |
| `raw.githubusercontent.com/.../cross-section-cap_mim.svg` | thin body | Fine | SVG/XML, not HTML — the text-stripping heuristic isn't suited to it; fetched directly: a real, complete 37 KB SVG |
| `raw.githubusercontent.com/.../cross-section-nfet_01v8.svg` | thin body | Fine | Same as above |
| `skywater-pdk.readthedocs.io/.../errors.html` | title contains "error" | Fine | Genuinely the PDK's own "Error Messages" reference page |
| `spie.org/Publications/Book/924283` | title contains "404" | Fine (intermittent) | One fetch redirected to spie.org's own 404 page; two immediate re-fetches (this UA and a browser UA) resolved the original URL directly. Not dead by the two-check rule |
| `web.archive.org/.../novellus.com.../cvd.htm` | title mismatch | Fine | 1998 capture, generic `<title>Untitled Document</title>`; `id_` form contains "Tungsten", "CVD" |
| `web.archive.org/.../novellus.com.../pecvd.htm` | title mismatch | Fine | Same pattern; contains "PECVD", "Dielectric" |
| `web.archive.org/.../novellus.com.../cvd.asp` | title mismatch | Fine | 2002 capture, generic title "Novellus Systems - metal CVD"; contains "Tungsten", "CVD" |
| `web.archive.org/.../strasbaugh.com/cmp1.htm` | title mismatch | Fine | Generic title "STRASBAUGH"; contains "6DS", "Planariz-" |
| `web.archive.org/.../sela.com/about.htm` | title mismatch | Fine | Generic company tagline as title; contains "SELA" |
| `web.archive.org/.../mattson.com/aspen_strip.html` | title mismatch | Fine | Generic title "Mattson - Products"; contains "Aspen", "Strip" |
| `www.axcelis.com/about/our-history/` | title mismatch | Fine | Templated site-wide title; body contains "1978", "founded", "GCA", "Eaton", "History" |
| `www.qnityelectronics.com/our-story.html` | title mismatch | Fine | Templated title; body contains "DuPont", "spin-off", "Electronics" |
| `www.semimarket.com/item/.../94062` | thin body (403 page) | Fine, host added to `BLOCKED_HOSTS` | Intermittently 403s this checker's User-Agent (200 to a browser one, verified) — added for future runs; this run's main check got 200 (content is live) |

All 14 "title mismatch" false positives above trace to two bugs, both
fixed (see "Tool changes"): `extract_cited_title()` took the block's
*first* italic span for every URL in it — wrong whenever a block holds
more than one citation (an inventory `**KEY**` block runs to the next
`**KEY**` marker, which can be a whole reading-list section away: the
"Encyclopaedia articles" list under one key wrongly gave every Wikipedia
citation after the first the first bullet's title) — replaced with
`extract_url_titles()`, pairing each URL with its *nearest preceding*
title. That still can't fully resolve CYP-13's "title X and title Y ...
url1, url2" pattern (a known, documented limitation), which is why it
still shows one suspect there — reviewed by hand above, and fine.

### (b) Cross-domain redirects — the IOP Science / Radware finding

Added a report section listing every non-dead/blocked token whose fetch
chain crossed hosts. Two found:

* `books.google.com` → `books.google.com.au`: benign country-domain
  redirect, same book. Fine.
* **`iopscience.iop.org` → `validate.perfdrive.com` (Radware), HTTP
  200.** This is a bot-challenge page, not the cited article — and the
  old `classify()` only ever checked for a same-host challenge by *path*
  (openlibrary.org's `/verify_human`), so a *different-host* challenge
  landing with a 2xx status was being counted "ok". Fixed:
  `is_challenge_url()` now also matches by host
  (`CHALLENGE_HOST_MARKERS`, currently `perfdrive.com`) regardless of
  path or status. Effect, via `--reclassify` against the existing cache
  (no new network calls, pure recomputation from stored HTTP results):
  **136 DOI citations resolving to iopscience.iop.org, previously
  counted "ok", are now correctly `blocked-to-scripts`.**

This is very likely a real, meaningful part of what the owner is seeing:
136 citations to IOP Publishing journal articles (IOP journals are used
across many step and machine pages) were never actually verified by any
run of this checker — reachable by a person in a browser (the challenge
is IP/volume-triggered, the same pattern already documented for
openlibrary.org), but not by an automated client, and definitely not
"ok" in the sense the count implied. They are correctly still not "dead"
either (a person can read them), so no citation changes; see "Needs a
human with a browser".

### (c) `--include-generated` — the generated pages' links, checked for the first time ever

Ran to completion (papers and filings hosts checked in full; Espacenet
and Google Patents record-page links sampled 1-in-50 per the tool's
design — 749 new tokens total, run with `--no-soft-dead` given the time
already spent on the hand-written-page soft-dead pass; the soft-dead
check on generated pages is future work). Findings:

* **29 `worldwide.espacenet.com` tokens came back 403.** Confirmed with
  a separate `curl`, both this checker's User-Agent and a full browser
  one — both 403. EPO's Espacenet blocks scripted access broadly, not
  these specific 29 records; added `espacenet.com` to `BLOCKED_HOSTS`.
* **A dozen individual academic-publisher hosts** (`academic.oup.com`,
  `dl.acm.org`, `escholarship.org`, `onlinelibrary.wiley.com` /
  `ietresearch.onlinelibrary.wiley.com`, `pubs.aip.org`,
  `authorea.com`, `mdpi.com`, `techrxiv.org`) each returned exactly one
  403 apiece — one paper record checked per host, all 403. Re-verified
  each with a browser-UA `curl`: still 403 for all but `escholarship.org`
  (403 → 202, a clear UA-sensitive case) — most of today's anti-bot
  services fingerprint more than the declared User-Agent string, so a
  403 to a "browser" `curl` doesn't rule out scripted-client blocking,
  and these are all live, actively-maintained scholarly platforms, not
  hosts plausibly returning identical 403s because of unrelated,
  simultaneous content removal. Added all to `BLOCKED_HOSTS`. This is a
  judgement call with less certainty than the Espacenet finding (each
  is one data point, not dozens); worth the owner spot-checking one or
  two of these specific DOIs in a browser if in doubt.
* **4 tokens are genuinely, freshly dead** — but this is their *first*
  check ever (generated pages were never checked before this branch), so
  **none of them meet the C5 two-check rule yet** and none were touched:
  * `doi:10.5281/zenodo.20032068` and `doi:10.5281/zenodo.20950316` —
    both resolve to a real HTTP 410 Gone at Zenodo (re-verified directly,
    following the DOI redirect) — most likely a genuinely withdrawn or
    merged record, not a script block.
  * `https://www.osti.gov/servlets/purl/3363571` — timed out both in
    the run and on a direct re-check.
  * A cached Wayback capture of an SEC filing (`web.archive.org/web/20230502184124/.../ny20006439x1_def14a.htm`)
    came back 404 in the run but 200 on an immediate re-check —
    intermittent, not dead.
  * **Next step (not done here, needs to wait for the 24 h to genuinely
    pass):** re-run `uv run tools/check_links.py --include-generated
    --only-host zenodo.org --only-host osti.gov` (plus doi.org, since
    DOIs route through it) after 2026-09-21 and, if still dead, follow
    C5's data-file remediation for generated pages: an `archive_url`
    field in the relevant `data/*.yaml` record that `gen_papers.py`
    prefers, then regenerate — not a hand edit to the generated page.
* Two Infineon annual-report PDFs permanently redirect to a new
  canonical URL (still resolve, HTTP 200) — a data-file URL update, not
  a dead link; noted for a future pass, not fixed here (out of C5's
  dead-link scope).
* `nature.com` self-redirects with a `?error=cookies_not_supported`
  query param appended (still HTTP 200, same host) — a common
  cookie-consent-flow artifact, not a sign of missing content; not
  actioned.

## 3. Manual review outcomes

See the soft-dead? table above for the hand-written-page suspects (all
"fine" or an intermittent host, one `BLOCKED_HOSTS` addition, no
citation edits). No "moved" cases were found (a page whose content
genuinely relocated to a new URL) on hand-written pages this round.

## Needs a human with a browser

* **The IOP Science / Radware finding above.** 136 DOI citations
  resolving to iopscience.iop.org cannot be verified by any script from
  this environment (or, per the openlibrary.org precedent, quite
  possibly any automated environment) — a person following the DOI in
  an ordinary browser should not hit the challenge. Nothing to fix in
  the citations; flagged so the owner knows the true verification
  status of this large a slice of the DOI corpus.
* **Every `blocked-to-scripts` host below** — confirmed live via
  Wayback, a differently-configured request, or a browser-UA `curl` in
  this or an earlier round, but still worth a click-through if the owner
  wants first-hand confirmation: `sec.gov`, `cdc.gov`, `astm.org`,
  `startribune.com`, `appliedmaterials.com`, `businesswire.com`,
  `forbes.com`, `linkedin.com`, `indeed.com`, `glassdoor.com`,
  `researchgate.net`, `semimarket.com` (new this round), `openlibrary.org`
  (intermittent — see the redirected-permanently note below), plus, new
  this round via `--include-generated`: `iopscience.iop.org`/
  `validate.perfdrive.com` (via `doi.org`), `espacenet.com` (EPO,
  dozens of records checked, all 403), and — lower confidence, one data
  point each, worth a spot-check — `academic.oup.com`, `dl.acm.org`,
  `escholarship.org`, `wiley.com`, `pubs.aip.org`, `authorea.com`,
  `mdpi.com`, `techrxiv.org`.
* **`spie.org/Publications/Book/924283`** — flickered to a soft-404 once
  this session; resolved fine on immediate re-checks both times after.
  Not actionable now, but if the owner has personally seen this one 404,
  it would confirm the intermittency is real rather than a fluke on this
  end.
* **Two Zenodo DOIs and one OSTI PDF from `--include-generated`**
  (`doi:10.5281/zenodo.20032068`, `doi:10.5281/zenodo.20950316` — both a
  genuine HTTP 410 Gone; `https://www.osti.gov/servlets/purl/3363571` —
  timed out twice) are dead on their *first* check; this is generated-page
  data never checked before this branch, so C5's two-check rule isn't met
  yet. Re-run after 2026-09-21; if still dead, the fix is an
  `archive_url` field in the relevant `data/*.yaml` record (per C5, for
  generated pages) plus a regeneration, not a hand edit — not done here.

## Wording of existing Wayback citations (task item 3 of the original W0f task)

Audited every "Wayback" mention on hand-written pages (55 files, 228
archive-first `<https://web.archive.org/web/…>` citations, plus the 2
newly converted this round). 177 pre-existing citations already used the
exact house wording "Wayback Machine capture of YYYY-MM-DD" — nothing to
normalise. The 21 remaining are different, correctly-scoped patterns
(THUNG-2016's own aside note, the SEC-01/SEC-02 "read from a copy" note
for a script-blocked-not-dead host, 3 reading-list-bullet short
annotations) unrelated to R-WAYBACK's archive-first form; left alone. No
wording changes were needed or made.

The `redirected-permanently` count (18, was 1) is unrelated to R-WAYBACK
or the soft-dead work: 17 are `openlibrary.org` book pages whose
`/verify_human` bot challenge (known IP/volume-triggered, not
UA-based) simply didn't trigger on this run's timing, resolving as plain
301/308 redirects instead of the challenge. Recorded so the count
difference from the 2026-09-19 report (`blocked-to-scripts: 51`) isn't
mistaken for a regression; no citation changes made.

## Tool changes (`tools/check_links.py`)

All of the original W0f fixes (Wayback lookup retry/fallback chain,
never trusting a negative answer more than a day, `--suggest-archive`,
`--include-generated`, the `docs/plans/` scan-exclusion bug) plus, from
this round:

* **`soft_dead_reasons()`** and **`apply_soft_dead_check()`**: the
  soft-404 heuristics described above, plus a background top-up pass
  (mirroring the existing stale-Wayback-negative top-up) for tokens that
  were already fresh and so skipped the main HTTP recheck.
* **`extract_url_titles()`** replaces `extract_cited_title()`: per-URL
  nearest-preceding title instead of per-block first title (fixes the
  reading-list-contamination bug above), and flattens the block first so
  a title wrapped across a hard-wrapped source line is matched whole
  (fixes the CYP-13-style bug above).
* **`CHALLENGE_HOST_MARKERS`**: `is_challenge_url()` now also matches by
  host (currently `perfdrive.com`), not just by path on the same host,
  catching a cross-domain bot-challenge redirect regardless of its HTTP
  status.
* **`BLOCKED_HOSTS`** gains `semimarket.com` (403 to this checker,
  200 to a browser one) and, from `--include-generated`'s first-ever
  check of the generated pages' hosts: `espacenet.com`,
  `academic.oup.com`, `dl.acm.org`, `escholarship.org`, `wiley.com`,
  `pubs.aip.org`, `authorea.com`, `mdpi.com`, `techrxiv.org`.
* The report gained a "Soft-dead?" table and a "Cross-domain redirects"
  table.
* `--selftest` extended to cover all of the above offline: the four
  soft-dead heuristics, the per-URL title extraction (including the
  reading-list-contamination regression and the line-wrap regression),
  and the cross-domain challenge-host match.

## Checker suite

Full checker list (`tmp/prompts/rd-common.txt` rule 7) run and passing:
`check_steps`, `check_refs`, `check_machines`, `check_materials`,
`check_masks`, `check_papers`, `check_patents`, `check_filings`,
`check_inforce`, `gen_papers/gen_patents/gen_filings/gen_index_links
--check`, and `sphinx-build -W -q -b html docs tmp/_build/html`.
