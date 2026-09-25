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

## Third and fourth batches: further Fab 4 R7FT-3R/R42HD/R32/R32D/R42D reports

Ten more records added, all Fab 4 (Bloomington, MN):

| id | technology_codes | source file id | notes |
|---|---|---|---|
| qtp-024903 | R7FT-3R | 91731 | independently repeats and extends qtp-014807's history table |
| qtp-098115 | R42HD | 93971 | Die Fab Line ID printed "R4HD" |
| qtp-097201 | R32D | 93716 | process-description header printed "R32" |
| qtp-097517 | R42D | 93496 | |
| qtp-097195 | R32 | 93711 | single metal layer, distinct from double-metal R32D |
| qtp-098437 | R42HD | 94121 | running headers print "R42DH" (letters transposed) |
| qtp-003906 | R52D-3 | 91811 | dates R52D-3's own origin (QTP 99311, Aug 99) |
| qtp-098313 | R42HD | 94066 | Die Fab Line ID "R4HD" again; footnote calls a referenced QTP "R42H" |
| qtp-001605 | R42HDHA, R42HD | 92016 | **dates R42HD's own origin (QTP 98064, Apr 98)**, closing a reference-only gap qtp-098115/qtp-098313/qtp-098437 all left open |

**94146 (group C, "3.3v-synchronous-fifos-r42d-technology-w-hot-al") fetched
but unusable**, the same way as 94076: the cover and process-description
pages have no extractable text (only two reliability-data pages, for device
CY7C43684V, have selectable text). The QTP number (98517) and date (February
1999) are legible, but no title, technology code or process figures could be
confirmed without OCR, so no record was added.

## Fifth batch: R42D/R42H/R42HD Hot-Aluminum reports and two more R52 codes

Five more records, all Fab 4 (Bloomington, MN):

| id | technology_codes | source file id | notes |
|---|---|---|---|
| qtp-098357 | R42D | 94096 | this is QTP 98357 itself, cited differently by qtp-003907 and qtp-020305; its own cover title ("4 Meg") and device description ("1 Meg") for the same parts disagree internally |
| qtp-098111 | R42H, R42HHA | 93956 | cover/headers say "R42H", process block says "R42HHA" |
| qtp-098086 | R42HD | 93936 | distinguishes itself (Hot Al) from still-unretrieved QTP 98248 (no Hot Al), same technology code |
| qtp-099503 | R52D-3 | 94336 | repeats qtp-003906's origin row with different wording; gate oxide printed 50 Å here vs 55 Å in qtp-003906 |
| qtp-002603 | R52LD-3 | 92046 | new code; dates its own origin to QTP 99075 (Apr 99) |

## Still to do

- Group B: 46 more staged-and-extracted file ids not yet turned into records
  (all of `tmp/priority_order_b.txt` except the 2 duplicates and the 4 now
  recorded) -- R52T-3 clocks (many), R52FFD-3, B55SGT, C8Q-3R, R9Q-3R,
  R95LD-3R, further S4AD-5 variants (EZ-Color, Neutron, automotive, hydra,
  quark, Latch, nitride, ovation). Staged PDFs are at `tmp/stage/<fid>.pdf`,
  extracted text at `tmp/extracted/<fid>.txt` (both done).
- Group C: 17 more fetched-and-extracted file ids not yet turned into records
  (all of `tmp/priority_order_c.txt` except the 5 codes, 14 further reports
  handled above, and 94146 which is unusable):
  93646 (QTP 97118 -- referenced by qtp-097201 above),
  94266 (QTP 99325), 93731 (QTP 97211), 93746 (QTP 97222), 93801 (QTP 97344),
  93896 (QTP 97506), 93831 (QTP 97396 -- referenced by qtp-097517 above),
  93926 (QTP 98081), 94401 (QTP L000004, TSMC 0.25 µm foundry report),
  91736 (QTP 024907), 91621 (QTP 011103), 94381 (no "QTP#" prefix at all --
  numbered "G990003", a WaferTech 0.35 µm "Technology Qualification Report";
  keep `doc_type: QTP` for consistency with the rest of this corpus rather
  than adding a new `doc_type` value), 91526 (QTP 002703), 135526
  (QTP 002202), 121666 (QTP 005004). None of these QTP numbers duplicate an
  existing record (checked against the numeric set as of this session's third
  batch). QTP-number identification for all of them was done with `grep -om1
  -E "QTP#?\s*:?\s*[0-9]{4,6}" tmp/extracted/<fid>.txt`.
- Group B: 46 staged-and-extracted file ids not yet turned into records (all
  of `tmp/priority_order_b.txt` except the 2 duplicates and the 4 now
  recorded) -- R52T-3 clocks (many), R52FFD-3, B55SGT, C8Q-3R, R9Q-3R,
  R95LD-3R, further S4AD-5 variants (EZ-Color, Neutron, automotive, hydra,
  quark, Latch, nitride, ovation). Staged PDFs are at `tmp/stage/<fid>.pdf`,
  extracted text at `tmp/extracted/<fid>.txt` (both done).
- Once the stackup generator's new-band gap is resolved upstream, regenerate
  `docs/history/stackups.md`, `products.md` and `sources.md` and commit them.
- Cross-check every new QTP number against the existing (now 87) records
  before writing one, the way the qtp-072002/qtp-061806 duplicates were
  caught: `grep -oP "^  number: '?\K[0-9]+" data/history/qtp.yaml | sed
  's/^0*//' | sort -u`, comparing numerically since leading zeros vary
  between the printed field and the padded `id`.
- **YAML gotcha found this session:** a plain (unquoted) scalar in this file
  breaks the parser if it contains a colon followed by a space (reads as a
  new mapping key) or a space followed by `#` (reads as a comment) anywhere
  in the middle of the value -- both appear in verbatim report text (e.g.
  "QTP #98064", "Architecture:"). Wrap the `text:` value in single quotes
  whenever a quote itself contains " #"; for `notes:` (not verbatim-checked)
  it is simplest to reword around the colon or drop the "#". Always re-run
  `uv run tools/check_history_quotes.py` after appending records, since a
  YAML syntax error surfaces there as a Python traceback, not as a normal
  "problem" line.
