# Progress: QTP evidence (agent cyhist-qtp)

Restartable checklist for building `data/history/qtp.yaml`. Read
`docs/plans/cypress-history-plan.md` and `docs/plans/agent-briefs.md`
(lines 1-67) before resuming.

## Summary table (from records so far)

Draft — filled in as records are finalised; will be replaced with the
full table once fetching/extraction is done.

## State

- Worktree: `.worktrees/cyhist-qtp`, branch `topic/cyhist-qtp`.
- Shared cache: `/home/admin/github/mithro/sky130-process-tech/tmp/cyhist-cache/qtp/`
  (main checkout, git-ignored). Every PDF is saved as `<id>.pdf` with a
  poppler `pdftotext -layout` extraction as `<id>.txt`.
- Fetch tool: `curl -A "sky130-process-tech docs checker"`, via
  `tmp/fetch_qtp.sh <id> <url>` in this worktree (not committed to
  `data/`, it's a working script under `tmp/`, git-ignored — copy its
  logic into `tools/` if it needs to persist... actually keeping only
  `tools/check_history_quotes.py` per the brief).

## Search routes tried

1. **Seeds file** (`tmp/cyhist-cache/seeds-qtp.txt` in the main
   checkout, 36 URLs, `Infineon-QTP_NNNNNN...-ProductQualificationReport-...pdf?fileId=...`
   under `/dgdl/`). Result: only 4 of 32 attempted (excluding 3
   obviously-modern PSoC6 URLs QTP174005/182809/192102, which are a
   40 nm-class ARM Cortex-M0+ node far later than S8 and out of scope)
   downloaded successfully:
   - qtp-021507 (S4AD-5, cached before this agent started)
   - qtp-003907 (R42LDHA/R42D, Fab 4)
   - qtp-024110 (RAM8NLD-1.8V, Fab 4)
   - qtp-144802 (Test Site Qualification Report, OSE-Taiwan — **no
     technology named**, excluded from qtp.yaml as out of scope)
   The other ~27 seed URLs under `/dgdl/` all redirect (still HTTP 200)
   to `sso.infineon.com` ("myInfineon Login") — i.e. Infineon's DAM
   marks those specific documents as access-restricted, not a
   transient rate limit (confirmed by re-requesting a working URL
   immediately afterwards: it still worked). Six seed URLs 404 outright
   (060208, 090604, 100203, 114003, 160202/dgdl, 98516). Wayback CDX
   has no capture of any of these `/dgdl/...fileId=...` URLs (they are
   Infineon's post-2020-migration URLs, not the original cypress.com
   ones, so nothing to archive). These documents are recorded as
   "known to exist (seed list), not publicly retrievable" below; per
   rule 11 they are not quoted or used as sources.
2. **WebSearch for `assets/row/public/documents` + technology-code
   queries** (e.g. `infineon.com QTP Cypress "R4"/"R5"/"R7"/"R8"/"R9"`,
   `"C7"/"C8"/"C9"`, `"L8"/"L28"`, `"B53"/"P26"`). This is by far the
   most productive route: it surfaces the *other* URL family Infineon
   serves qualification reports from,
   `https://www.infineon.com/assets/row/public/documents/10/316/infineon-<slug>-productqualificationreport-en.pdf`,
   which for most documents found this way is NOT login-gated (unlike
   many `/dgdl/` seed URLs — the gating is per-document in Infineon's
   DAM, not per-URL-family; some `assets/row/public/documents` URLs
   for modern PSoC4/PSoC6 parts ARE gated (`/gated/` path), but the
   pre-S8-era ones found this way opened directly). Continuing to run
   more technology-code queries (R42D/R42HD/R28/R5/R52/R8/S4/CMOS
   0.8-1.2 µm/BiCMOS/SONOS 0.35/GSMC/Grace/HHGrace/UMC/TSMC/Fab 1-5)
   and logging each hit below.
3. **Wayback CDX for cypress.com** (`cdx?url=cypress.com&matchType=domain&filter=original:.*qtp.*\.pdf`)
   — timed out (504) on the unscoped domain query; not pursued further
   given the WebSearch route is working. Exact-URL CDX lookups for the
   dead `/dgdl/` seed URLs returned no captures (see above).
4. Not yet tried: mouser.com/PCN, teldevice.co.jp distributor mirrors;
   Infineon community "How to find QTP" article
   (`community.infineon.com/.../ta-p/249658`, surfaced by search —
   describes searching www.cypress.com support > Quality and
   Reliability, which now redirects into the same infineon.com DAM).

## Documents found beyond the seeds (fetched so far)

| id | technology | fab | title (short) |
|---|---|---|---|
| qtp-097483 | R42D | Fab 4 | Low Voltage Deep Sync FIFOs, CY7C42*V |
| qtp-102101 | R42HD | Fab 4 | Sync/Async Dual Port SRAM 3.3V/5V |
| qtp-096091 | (check) | (check) | QTP 96091/96393 |
| qtp-098368 | R42HD | Fab 4 | Sync/Async Dual Port SRAM |
| qtp-001004 | (0.5 µm TLM?) | Fab HME | 0.5 µm TLM Technology qual |
| qtp-061806 | R95LD-3R | Fab 4 | 4 Meg MoBL SRAM Automotive |
| qtp-072002 | R95LD-3R | Fab 4 | 2 Meg MoBL SRAM CY62136/7FV30, AEC-Q100 |
| qtp-091302 | RAM42HNHA | Fab 5, GSMC | MoBL Async SRAM CY62256 |
| qtp-063807 | C9FD-3R | Fab 4 | 1 Meg Fast Async SRAM Family |
| qtp-097476 | R28 | Fab 2 | 256K Static RAM |
| qtp-023101 | R7FTW-3R (check) | Fab 4 | Sync Dual Port Family |
| qtp-011908 | R7FD | Fab 4 | Fast Async SRAM Technology Derivative |
| qtp-014807 | R7FT-3R | Fab 4 | Technology Derivative Qualification |
| qtp-051207 | R9Q-3R | Fab 4 | 18 Meg QDR Sync SRAM CY7C1313D |

All of the above still need: text QC read-through, quote extraction,
process-description transcription, and a record in `data/history/qtp.yaml`.

## Not retrievable (seed docs, login-gated or 404, no archive)

- qtp-fid-0b521b46 (Automotive PSoC CY8C21X34, S4AD-5, Fab4) — gated
- qtp-053402, 054603, 060201, 060401, 063210, 070505, 072402, 072502,
  072803, 082201, 083401, 090706, 092301, 093003, 100102, 102802,
  104407, 113905, 123502, 132905, 202903 — gated (myInfineon Login)
- qtp-060208, 090604, 100203, 114003, 160202, 098516 — HTTP 404, no
  archive
- qtp-042205 (R9T-3R, 9 Meg Sync SRAM CY7C1360CC) — both the `/dgdl/`
  and `assets/row/public/documents` URLs found by search 404; not
  retried further (rule: don't loop on repeated failures)

These are almost all **S4AD-5 and S8DIN-5R/S8P12-10P/S8PF-10R/etc.
reports** — i.e. exactly the ones the brief most wants for dating S8's
early qualifications. This is a real gap; flagged prominently in the
final report. The technology names are known from the seed filenames
alone (not usable as sourced facts, only as a to-do list) — e.g. this
confirms S4AD-5 and various S8 variants were run at Fab 4/Fab 5/GSMC/CMI,
per the *filenames*, but none of the process-description or
qualification-history detail is retrievable from them right now.

## Next steps

1. Keep running WebSearch queries per remaining technology code.
2. Read/QC each cached .txt, write `data/history/qtp.yaml` records.
3. Write `tools/check_history_quotes.py`.
4. Fill in the summary table above from the finished records.
