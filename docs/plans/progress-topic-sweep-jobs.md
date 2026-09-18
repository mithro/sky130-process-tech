# Progress: topic/sweep-jobs

Branch `topic/sweep-jobs`, worktree `.worktrees/topic-sweep-jobs`.

## Task A — job-listing citations (`JOB-0x`)

### Retrieval attempts (2026-09-19)

| Source | Live URL | Wayback | archive.today/.ph | Result |
|---|---|---|---|---|
| JOB-01 (Indeed, Bloomington listing) | HTTP 403 (reconfirmed; also 403 on 2026-09-13, cached fetch from an earlier pass in the repo's `tmp/p4/fetch/` shows the Indeed error shell) | `wayback/available` → no snapshot | archive.today `/newest/` → 404 (no snapshot); archive.ph → redirect to no-result; archive.is rate-limited (429), not retried per rule 12 | **Dead, not archived.** |
| JOB-02 (Indeed, Minnesota-wide + Bloomington) | Both URLs HTTP 403 | no snapshot | not separately checked beyond Wayback (uncited; low priority) | **Dead, not archived.** Not cited anywhere in `docs/`, so no page needed fixing; inventory entry marked dead/dated. |
| JOB-04 (LinkedIn, Equipment Maintenance Technician, Austin TX) | HTTP 200 | n/a (live) | n/a | **Still live.** No change needed beyond reconfirming the date; not cited by any step/machine page (recorded only as an example of SkyWater posting style). |
| JOB-05 (SkyWater Dayforce applicant portal) | Portal root HTTP 200 (client-rendered); found via search that individual posting URLs (`.../CANDIDATEPORTAL/jobs/<id>`) ARE plain server-rendered HTML and fetch directly | n/a | n/a | **Still live**; inventory note improved (individual postings are fetchable by URL after all, just not the search page). Not cited by any page. |

### Replacement evidence found

**JOB-06 (new inventory entry).** Web search for the exact posting title
("Defect Technician 2", Bloomington, SkyWater) turned up a live LinkedIn
repost: <https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>
(HTTP 200, retrieved 2026-09-19). Fetched and confirmed it contains the
identical sentence: "General operation of semiconductor defect
metrology tools: SEM/AIT/KLA/SP1/EV300/1X." This is a different job ID
than JOB-04's LinkedIn posting (Austin, Equipment Maintenance
Technician). Added as JOB-06 in `docs/references/public-sources.md`,
tier cross-check (medium strength) — the same strength JOB-01 carried,
since the evidence quality (an unexplained abbreviation list in a job
ad) is unchanged; only the retrievability changed.

Other avenues tried and not used: SkyWater's own `/careers/` page lists
"Defect Technician" as a role title but gives no posting text or tool
names; ZipRecruiter's SkyWater listing page returned HTTP 403;
SkyWater's Dayforce portal search page is client-rendered and did not
yield the specific posting by browsing.

### Pages fixed (rule 11 applied — citation swapped from `[^job-01]` to `[^job-06]`)

All 28 pages that cited `[^job-01]` (three machine pages + 25 step
pages) were updated by a helper script (`tmp/fix_job01.py`, not
committed) that (a) replaced the `[^job-01]` footnote definition with
the new JOB-06 definition, (b) changed every remaining `[^job-01]` to
`[^job-06]`, and (c) changed "Indeed, SkyWater …" reading-list bullets
to "LinkedIn, SkyWater …":

`docs/machines/defect-inspection.md`, `docs/machines/index.md`,
`docs/machines/starting-material.md`, `docs/steps/001-smat.md`,
`009-dnis.md`, `012-cmpnit.md`, `016-lvtnis.md`, `021-lvtpis.md`,
`025-pchis.md`, `029-pwis.md`, `033-pwdeis.md`, `035-tunm.md`,
`067-astis.md`, `070-hvastis.md`, `074-ldastis.md`, `084-pdis.md`,
`087-nsdis.md`, `090-cmpp.md`, `100-wcmpli.md`, `106-cmpl.md`,
`111-wcmp2.md`, `116-cmpm.md`, `122-wcmp3.md`, `127-cmpm2.md`,
`133-wcmp4.md`, `142-cmpm3.md`, `148-wcmp5.md`, `157-cmpm4.md`.

Manual follow-up fixes after the script:

* `docs/steps/035-tunm.md` — a prior pass had already downgraded this
  page to "Strength: weak — the source can no longer be checked." Since
  JOB-06 restores retrievability, reverted to "Strength: medium."
  (matching every other page that reads this quote).
* `docs/steps/001-smat.md` — removed the stale "of which no archived
  copy exists" clause in Open Questions (no longer true of JOB-06).

### Evidence that had been fully withdrawn — restored

`docs/machines/defect-inspection.md`'s "Strength of the evidence"
section recorded that four step pages — 051-p1is.md (P1IS), 054-pris.md
(PRIS), 057-upris.md (UPRIS), 060-bfr.md (BFR) — had **removed** their
AIT/SP1 claim entirely and graded it "Strength: none" once JOB-01 became
unretrievable with no replacement on hand (see
`docs/plans/progress-topic-p4-048-063.md`, row 051-M1). With JOB-06 now
live, evidence was restored on all four:

* `docs/steps/051-p1is.md` — "Strength: none" → new AIT paragraph,
  Strength: medium, `[^job-06]`, Cross-check bullet, footnote def added.
* `docs/steps/054-pris.md` — same treatment (AIT only).
* `docs/steps/057-upris.md` — same treatment (SP1 + AIT).
* `docs/steps/060-bfr.md` — same treatment (SP1 backside class only).

Updated `docs/machines/defect-inspection.md`'s "medium" bullet list and
narrative paragraph, and `docs/machines/index.md`'s parallel "medium"
row in the machine ↔ step table, to add P1IS/PRIS/UPRIS/BFR back in
(the two lists — "steps assigned to the class" vs. "steps that grade
the posting medium" — now match again).

### Tools that lost (and regained) their only evidence

None of the tools lost their *only* evidence permanently: KLA-Tencor
AIT and Surfscan SP1 at these four steps had temporarily lost their
sole piece of SkyWater-specific evidence (down to "Strength: none",
i.e. category-page evidence only) while JOB-01 was dead and unreplaced;
JOB-06 restored "Strength: medium" evidence on all four. No step page
in the sweep ended this task with a tool resting on JOB-01/JOB-02 alone.

### Files changed (file:line at time of writing; see `git diff` for exact ranges)

* `docs/references/public-sources.md` — JOB-01 entry rewritten (dead,
  no archive, superseded); JOB-02 entry rewritten (dead, no archive,
  uncited); JOB-04 entry reconfirmed live; JOB-05 entry note improved;
  new JOB-06 entry added; keyed-entry count bumped 1719 → 1720.
* `docs/machines/defect-inspection.md` — table cell, "What SkyWater
  lists" prose, "Strength of the evidence" paragraph, medium bullet
  list and the P1IS/PRIS/UPRIS/BFR narrative, footnote def.
* `docs/machines/index.md` — "A job posting" bullet, class table row,
  machine↔step medium row (add P1IS/PRIS/UPRIS/BFR), footnote def.
* `docs/machines/starting-material.md` — citation swap only (script).
* `docs/steps/{001,009,012,016,021,025,029,033,035,067,070,074,084,
  087,090,100,106,111,116,122,127,133,142,148,157}-*.md` — citation
  swap (script) plus the two manual fixes above.
* `docs/steps/{051,054,057,060}-*.md` — evidence restored (manual).

## Task B — vendor/tool spelling

### Audit method

For each pair, counted occurrences (`grep -rho`), then checked every
occurrence of the "wrong-looking" or minority spelling for whether it
sits inside a direct quotation (SkyWater's capabilities page, or a
third-party title/press release) vs. our own prose, using both manual
`grep -n` context reads and a small Python script
(`tmp/check_aspen2_quotes.py`, not committed) that flags any
`Aspen2`/`GaSonics` occurrence that is not inside an open quote on its
paragraph (checked against the surrounding lines by hand since Markdown
wraps quotes across lines).

### Findings: already consistent, no edits needed

* **GaSonics / Gasonic(s).** Our own prose uses "GaSonics" (matching
  the vendor's own style, "GaSonics International" — cited
  `[^gasonics-2000]` on `docs/machines/downstream-plasma-asher.md`).
  Every occurrence of the singular "Gasonic" (no final s) is inside a
  quotation of SkyWater's *Facilities & Capabilities* wording ("Gasonic
  PEP, remote microwave plasma…", `[^skw-01]`) — checked all ~40
  occurrences by hand/grep. The plural, non-camel-case "Gasonics" (19
  occurrences) appears only inside the *titles* of third-party sources
  (SemiStar/Allwin21/Stanford listings, e.g. "*Gasonics L3510 plasma
  asher*") — kept verbatim as those sources title themselves, not our
  prose and not attributed to SkyWater.
  An earlier branch (`docs/plans/progress-topic-p4-076-088.md`, finding
  079-L1) had found a real split at that point in time (38×
  mis-quoted "GaSonics PEP" vs. 34× correctly-quoted "Gasonic PEP") and
  deferred it to this site-wide sweep; a later merge already fixed it
  before this branch started — `grep -rn '"GaSonics' docs/` today finds
  zero mis-quotations. Nothing left to do.
* **Aspen II / Aspen2 / Aspen 2.** Our prose reads "Aspen II" (Mattson's
  own product name — Mattson's *Aspen Strip* product page names the
  "Aspen II Strip"/"Aspen II platform", `[^mattson-2001]`). Every
  "Aspen2" occurrence (42) is inside the SkyWater quotation ("Mattson
  Aspen2, RF plasma, O2, CF4, H2>N2, up to 250C"); confirmed none sit
  outside a quote. "Aspen 2" (with a space) does not occur anywhere.
* **Novellus / Novelus.** No misspelling ("Novelus", "Novellius",
  "Novellous") found anywhere in `docs/`.
* **AG Associates / Heatpulse.** Vendor's own legal name confirmed as
  "AG Associates, Inc." (its Form 10-K, inventory key `AG-10K`). Our
  prose consistently uses "AG Associates"; the abbreviated "Ag
  Heatpulse 8808…" only ever appears inside the SkyWater capabilities
  quotation. No unquoted "Ag Associates"/"Ag Heatpulse" found.
* **Mattson, Axcelis, KLA-Tencor, Lam Research.** All-caps forms
  ("MATTSON", "AXCELIS", "LAM") occur only in inventory keys (e.g.
  `AXCELIS-GSD`, `PAT-TCP-LAM`) or inside direct quotations of
  third-party text (e.g. "a LAM TCP9600 etcher" from a 1999 paper,
  "LAM TCP 9600 Etch Chamber" from a 1994 ASMC paper) — both proper.
  "KLA Tencor" without the hyphen occurs only inside
  `docs/references/patents/` (generated pages, assignee-name field from
  patent-office records — out of scope per the citation-style.md
  generated-index exception, not written prose). No unhyphenated
  "KLA Tencor" or "Kla-Tencor" in any written page.
* **Tegal.** Not mentioned anywhere in `docs/`; nothing to check.

### Convention page

`docs/machines/downstream-plasma-asher.md` (lines ~152–166) already
documents the rule correctly (vendor's own spelling in our prose,
SkyWater's exact wording preserved in quotes, with a worked example for
"Gasonic"/"Aspen2"). The convention has not changed, so it was left as
is; the glossary (`docs/glossary.md`) does not cover vendor/tool names
so has nothing to make consistent; `docs/machines/index.md` and
`docs/materials/index.md` were checked and already follow the same
rule throughout.

**No files changed for Task B** — the spelling split flagged in the
task brief had already been resolved by earlier merged work before this
branch started; this pass re-verified it and found no regressions.
