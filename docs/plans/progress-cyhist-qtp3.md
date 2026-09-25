# Progress: QTP evidence, round 3 (agent cyhist-qtp3)

Restartable checklist/log for extending `data/history/qtp.yaml` beyond the
50 records left by round 2 (`docs/plans/progress-cyhist-qtp2.md`). Read that
file, `docs/plans/cypress-history-plan.md` and `docs/plans/agent-briefs.md`
(lines 1-67) before resuming. Checker: `uv run tools/check_history_quotes.py`
(must stay at 0 problems).

Source list for this round: `tmp/cyhist-cache/web/qtp3-todo.txt` (main
checkout), 123 lines / 112 unique cypress.com file ids (`?page=1` duplicate
slugs share the same file id as the base slug and are not fetched twice).
Timestamps come from `tmp/cyhist-cache/web/cdx-cypress-file-pdfs.txt`.

## Fetch groups (by priority, as briefed)

- **Group A** (earliest technologies / new codes) -- 26 file ids: P20 MAX
  EPLD (93411, 93456), P26 (93301, 94191, 92866), R28 at Fab 2/3 (94051,
  94056, 94076, 94431, 94216, 94181, 93461, 93546) plus one Fab-4-labelled
  R28 (94031), L28 (91846, 91341, 91681, 92261, 94251 TSMC, 94071 L28EPD),
  PSoC CY8C25/26 S4AD-5 Fab 2 (91396), S4AD-5+R42LDHA clock (91946), NEC
  0.25um (92226), PowerChip (92446), R7FFT-18 (92306), R52FD-3 (91326).
- **Group B** (the rest, named) -- 50 file ids: R52T-3 clocks (20 ids) +
  R52FFD-3 (91571), B55SGT (92681, 92146), C8Q-3R (92096, 92091, 93281,
  92551, 95566), R9Q-3R/R9 (92546, 92956, 92721, 92796), R95LD-3R (93006,
  134221, 136266, 124116, 138641), S4AD-5 family variants incl.
  EZ-Color/Neutron/automotive/hydra/quark/Latch/nitride/ovation (13 ids).
- **Group C** (everything else in the todo list, mostly further R42D/R42HD/
  R32/R32D/R52D-3/R52LD-3/R7FT-3R Fab 4 reports) -- 36 file ids, including
  three genuinely new codes not yet in qtp.yaml at all: R3 (93606), R7LD-3
  (91666, referenced-only gap from round 2), R52LD-5R (91836, referenced-only
  gap from round 2), R63D-25 (91686, 91656), and L31 (93881).

Lists are kept as `tmp/priority_order.txt` / `_b.txt` / `_c.txt` in this
worktree (gitignored scratch, not committed) plus `tmp/fetch_log.jsonl`
(append-only fetch ledger: fid, label, ok, url/error) and `tmp/id_url_ts.txt`
(file id -> original cypress.com URL + Wayback timestamp, derived from the
CDX list).

## Status

**Group A: done (26/26 file ids attempted).** 12 new qtp.yaml records added
(76 documents total after this round so far), 1 file id was a duplicate of
an already-cached document, 1 file id 404s (not archived, matching round
2's finding), 2 file ids failed with connection-refused errors that did not
recur on retry after the pause (so treated as transient, not gating).

| File id | Label | Outcome |
|---|---|---|
| 93411 | P20 MAX EPLD | qtp-091216 (new) |
| 93456 | P20 MAX EPLD | qtp-093332 (new) |
| 93301 | P26 | qtp-095075 (new) |
| 94191 | P26 | qtp-099092 (new) |
| 92866 | P26 | qtp-054605 (new, P26 at Magnachip) |
| 94051 | R28 | qtp-098252 (new) |
| 94056 | R28 | **failed** -- connection refused twice in the 10 s-paced sequence (triggered the 15-minute pause); not retried again this round; worth a retry next session |
| 94076 | R28 | **failed** -- connection refused (same pause episode as 94056); not retried again this round |
| 94431 | R28 | **duplicate** -- same QTP# 98393 already in qtp.yaml as `qtp-098393` (round 1, fetched via a different infineon.com URL); no new record added |
| 94216 | R28 | qtp-099175 (new) |
| 93461 | R28 | qtp-095515 (new, first Fab-3 R28 report retrieved this round; cover spells it "RAM28") |
| 93546 | R28 | qtp-096361 (new, second Fab-3 R28 report) |
| 94031 | R28-Fab4 | qtp-098236 (new) -- **the "Fab 4" in the file's slug is a mislabel on Cypress's own web page; the document itself is Fab 2 throughout** |
| 91846 | L28 | qtp-004604 (new; independently repeats round 2's L28 origin row QTP 97403 verbatim and adds two later dated L28 history rows) |
| 91341 | L28 | fetched, staged, **not yet turned into a record** (see Next steps) |
| 91681 | L28 | fetched, staged, **not yet turned into a record** |
| 92261 | L28 | fetched, staged, **not yet turned into a record** |
| 94251 | L28-TSMC | fetched, staged, **not yet turned into a record** |
| 94071 | L28EPD | **failed, HTTP 404** -- not archived, matching round 2's exact finding for this same file id; do not retry again without a long gap |
| 91396 | S4AD-5 PSoC CY8C25/26, Fab 2 | fetched, staged, **not yet turned into a record** (priority item) |
| 91946 | S4AD-5 + R42LDHA clock | fetched, staged, **not yet turned into a record** (priority item) |
| 92226 | NEC 0.25um | fetched, staged, **not yet turned into a record** (priority item) |
| 92446 | PowerChip | fetched, staged, **not yet turned into a record** (priority item -- likely the "8 Meg PSRAM" companion report round 2 flagged as ungathered next to qtp-051501) |
| 92306 | R7FFT-18 | fetched (per fetch log), staged, **not yet turned into a record** (priority item) |
| 91326 | R52FD-3 | fetched (per fetch log), staged, **not yet turned into a record** (priority item -- this is the report round 1/2 could only reference, never independently retrieve) |

**All 6 remaining Group A priority reports now done** (91341, 91681, 92261,
94251 for L28; 91396, 91946, 92226, 92446, 92306, 91326 for the rest --
22 new records total from Group A). Headline finds:

- **L28's origin is now dated Feb 1996** (QTP 95197, qtp-000901), over two
  years earlier than the previous earliest date (QTP 97403, Apr 98). A
  second report (qtp-031101) independently describes QTP 97403 itself as a
  "transfer from Fab 3 to Fab 2", not an origination -- resolving the
  apparent conflict.
- **qtp-099285 is the primary origin report for L28-TSMC**, previously
  known in this corpus only by reference; confirms May 2003 verbatim but
  gives a tenfold-different final passivation thickness (12,000 Å vs
  1,200 Å in the two already-known L28-TSMC reports).
- **qtp-000505 is the R52FD-3 report round 1/2 could only reference** --
  now retrieved directly, dating R52FD-3's own origin to QTP 001603, Jul 00
  ("New Technology Derivative R52FD-3").
- **qtp-041005 is the "8 Meg PSRAM" PowerChip companion report** round 2
  flagged as ungathered (it had mis-cited the cypress.com file id as a QTP
  number, "92626"); real QTP number is 041005, Mar 04, referencing a still
  earlier unretrieved "16-Meg" sibling (QTP 040504, Jan 04).
- **qtp-022505 confirms S4AD-5 at 0.35 µm for a sixth independent report**
  (further undermining qtp-021507's "0.5 m" outlier) and dates PSoC's own
  arrival on S4AD-5 to QTP 013507, Sept 01.
- **qtp-030310 (NEC 0.25um)** is a foundry (NEC Electronics America,
  Roseville CA) not named anywhere else in this corpus.
- **qtp-020305** documents S4AD-5 (Fab 2) and R42LDHA (Fab 4) side by side
  for one product, confirming both technologies' figures independently.

**Groups B and C** were not finished here; they continue in
`docs/plans/progress-cyhist-qtp4.md` (branch `topic/cyhist-qtp4`).

## Fetch mechanics used

`tmp/fetch_batch.py <order-file>` (gitignored, in this worktree): reads a
priority-order file, looks up each file id's original URL + Wayback
timestamp, and fetches `https://web.archive.org/web/<ts>id_/<url>` with
user agent `sky130-process-tech docs checker`, sleeping >=11 s between
requests, staging PDFs at `tmp/stage/<fid>.pdf`. On 2 consecutive
503/429/connection errors it sleeps 15 minutes and retries once; after 3
such pauses it stops (never loops indefinitely). Every attempt (success or
failure) is appended to `tmp/fetch_log.jsonl`, so the script is resumable
and idempotent (already-staged or already-logged-ok file ids are skipped).

`tmp/extract.py [fid ...]` (gitignored): pymupdf text extraction from
staged PDFs into `tmp/extracted/<fid>.txt`, printing sha256, page count and
the first ~45 lines so the QTP number can be identified before the file is
renamed into the shared cache as `tmp/cyhist-cache/qtp/qtp-<id>.pdf`/`.txt`
(main checkout, per `agent-briefs.md`).
