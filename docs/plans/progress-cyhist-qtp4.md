# Progress: QTP evidence, agent cyhist-qtp4

Continues from `tmp/progress-cyhist-qtp3-reference.md` (gitignored scratch,
kept in this worktree's `tmp/` for reference, not committed): the previous
session's group-B fetch had already staged 48 of 50 file ids (2 connection
refused: 92076, 92601) but turned none of them into records; group C (36 file
ids, including the new codes R3, R7LD-3, R52LD-5R, R63D-25, L31) had not been
fetched at all. `tmp/fetch_batch.py` and `tmp/extract.py` had hard-coded paths
into the old `cyhist-qtp3` worktree; both were repointed at this worktree
before any fetch or extraction ran, so nothing was written outside
`.worktrees/cyhist-qtp4`.

Read first: `docs/plans/agent-briefs.md` (lines 1-67), `docs/plans/cypress-history-plan.md`.

## Fetching

- Retried 94056 and 94076 (Group A) and 92076, 92601 (Group B connection
  failures), then group C's 36 file ids, via
  `tmp/priority_order_retry_c.txt` and `tmp/fetch_batch.py`.
- 94056, 92076, 92601: fetched successfully this time.
- **94076: fetched, but the PDF has no extractable text on its cover or
  process-description pages (image-only); only two reliability-data pages
  (CY7C425, CY7C199 stress tables) have selectable text.** No QTP number,
  title or technology code could be confirmed without OCR, so no record was
  added and no further retry is planned.
- Group C: see below.

## Records added this session

| id | technology_codes | fab | source file id | notes |
|---|---|---|---|---|
| qtp-060201 | S4AD-5 | Fab 4 (Minnesota) | 121336 | Hydra device family transfer |
| qtp-070505 | S4AD-5 | Fab 5 (GSMC, China) | 130041 | Quark device family; first Fab 5/GSMC S4AD-5 report |
| qtp-071104 | S4AD-5 | Fab 5 (GSMC, China) | 134771 | process-description header misprinted "R28"; figures match S4AD-5 |
| qtp-098296 | R28 | Fab 2 (Round Rock, TX) | 94056 (Group A retry) | 1998-format report; cites QTP 97476 as "256K SRAM", agreeing with qtp-097476's own title against qtp-098252's "32K x 8 SRAM" citation of the same QTP number |

Duplicates found in Group B (fetched under a new file id, but the same QTP
number already has a record from an earlier file id -- no new record added):

- file id 124116 -> QTP 072002, already `qtp-072002`.
- file id 134221 -> QTP 061806, already `qtp-061806`.

## Checks after this batch

- `uv run tools/check_history_quotes.py`: 357 quotes checked across 4 files, 0 problems.
- `uv run tools/gen_history_stackups.py --check`: found stale pages; regenerated
  with `gen_history_stackups.py`, `--sync`, and `gen_history_sources.py`.
- `uv run tools/check_history.py`: 9 pages, 177 claims checked, 0 problems.

## Second batch: the five new process codes (Group C)

All 40 outstanding fetches (94056/94076/92076/92601 retries plus group C's 36
file ids) completed with no errors this session; see `tmp/fetch_retry_c.log`.
94076 remains unusable (see above). All 37 usable files were extracted with
`tmp/extract.py` into `tmp/extracted/`; none of their QTP numbers duplicate an
existing record.

Six records added for the five new codes:

| id | technology_codes | fab | source file id | notes |
|---|---|---|---|---|
| qtp-097044 | R3 | Fab 4 (Bloomington, MN) | 93606 | 0.5 µm, matches R28's and L31's figures |
| qtp-012005 | R7LD-3 | Fab 4 (Bloomington, MN) | 91666 | 0.16 µm; Die Fab Line ID printed "R7LD-3R" |
| qtp-004405 | R52LD-5R | Fab 4 (Bloomington, MN) | 91836 | 0.25 µm/0.3 FETS; cover date and running-header date disagree (Dec 2002 vs Apr 2001) |
| qtp-012407 | R63D-25 | Fab 4 (Bloomington, MN) | 91686 | technology's own origin report (QTP 011308); 0.27 µm |
| qtp-011805 | R63D-25 | Fab 4 (Bloomington, MN) | 91656 | independently repeats the same 0.27 µm figure |
| qtp-097461 | L31 | Fab 4 (Bloomington, MN) | 93881 | same figures as R3; names the technology three different ways in one document (see notes) |

**Stackup generator gap:** `uv run tools/gen_history_stackups.py --check` (and
plain `gen_history_stackups.py`) now stops with `no design-rule band for
['qtp-011805', 'qtp-012407']`. Both R63D-25 reports print "0.27 µm", which
falls in the gap between the generator's "0.25 µm" band (0.24-0.26) and its
"0.42 µm and 0.35 µm" band (0.33-0.45); no existing band covers 0.27. Left
for the tool's owner rather than editing `tools/`. Because of this, this
session's `docs/history/stackups.md`, `products.md` and `sources.md` were
**not** regenerated after the second batch and are now stale (they still
reflect the state after the first batch only); `check_history.py` still
passes (177 claims, 0 problems) since it does not depend on those pages being
current relative to the newest `qtp.yaml` additions.

## Checks after the second batch

- `uv run tools/check_history_quotes.py`: 376 quotes checked, 0 problems (one
  quote for qtp-012407 had to stop at "...with NoBL" rather than continue
  into "Architecture": the cached PDF text has an unmapped private-use-area
  glyph, distinct from the three micron-sign PUA codepoints
  `check_history_quotes.py` already maps, standing in for a trademark symbol
  between "NoBL" and "Architecture" everywhere that phrase appears in this
  one document -- not fixed here since it means editing `tools/`).
- `uv run tools/check_history.py`: 9 pages, 177 claims checked, 0 problems.
- `uv run tools/gen_history_stackups.py --check`: blocked, see above.

## Still to do

- Group B: 46 more staged-and-extracted file ids not yet turned into records
  (all of `tmp/priority_order_b.txt` except the 2 duplicates and the 4 now
  recorded) -- R52T-3 clocks (many), R52FFD-3, B55SGT, C8Q-3R, R9Q-3R,
  R95LD-3R, further S4AD-5 variants (EZ-Color, Neutron, automotive, hydra,
  quark, Latch, nitride, ovation). Staged PDFs are at `tmp/stage/<fid>.pdf`,
  extracted text at `tmp/extracted/<fid>.txt` (both done).
- Group C: 31 more fetched-and-extracted file ids not yet turned into records
  (all of `tmp/priority_order_c.txt` except the 5 codes handled above) --
  further R7FT-3R, R42HD, R32, R42D, R32D, R52D-3, R52LD-3, B53D-3 Fab 4
  reports, plus two foundry reports (TSMC 0.25 µm "L000004", WaferTech 0.35 µm
  "G990003", the latter a "Technology Qualification Report" rather than
  "Product Qualification Report" -- keep `doc_type: QTP` for consistency with
  the rest of this corpus, per the existing convention of not adding new
  `doc_type` values). QTP-number identification for all of them (via `grep
  -om1 -E "QTP#?\s*:?\s*[0-9]{4,6}"`) is in this session's scrollback only, not
  saved to a file -- rerun it against `tmp/extracted/*.txt` before resuming.
- Once the stackup generator's new-band gap is resolved upstream, regenerate
  `docs/history/stackups.md`, `products.md` and `sources.md` and commit them.
- Cross-check every new QTP number against the existing (now 83) records
  before writing one, the way the qtp-072002/qtp-061806 duplicates were
  caught: `grep -oP "^  number: '?\K[0-9]+" data/history/qtp.yaml | sed
  's/^0*//' | sort -u`, comparing numerically since leading zeros vary
  between the printed field and the padded `id`.
