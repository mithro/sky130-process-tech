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

(to be filled in)
