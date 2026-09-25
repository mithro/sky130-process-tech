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

## Still to do

- Group B: 46 more staged-but-unprocessed file ids (all of `tmp/priority_order_b.txt`
  except the 2 duplicates and the one now recorded as qtp-098296/qtp-060201/qtp-070505/qtp-071104
  handled above) -- R52T-3 clocks (many), R52FFD-3, B55SGT, C8Q-3R, R9Q-3R,
  R95LD-3R, further S4AD-5 variants (EZ-Color, Neutron, automotive, hydra,
  quark, Latch, nitride, ovation). Staged PDFs are at `tmp/stage/<fid>.pdf`;
  extracted text for all of them is at `tmp/extracted/<fid>.txt` (done this
  session via `tmp/extract.py`).
- Group C: fetch was started this session (`tmp/priority_order_retry_c.txt`,
  running in the background); check `tmp/fetch_retry_c.log` and
  `tmp/fetch_log.jsonl` for its outcome before re-fetching. Includes the five
  new codes R3 (93606), R7LD-3 (91666), R52LD-5R (91836), R63D-25 (91686,
  91656) and L31 (93881); these are new process codes for `qtp.yaml` and
  need careful records.
- Cross-check every new QTP number against the existing 73+ records (now 77)
  before writing a record, the way qtp-072002/qtp-061806 duplicates were
  caught here: `grep -oP "^  number: '?\K[0-9]+" data/history/qtp.yaml | sort -u`,
  compared numerically (leading zeros vary between the printed field and the
  padded `id`).
