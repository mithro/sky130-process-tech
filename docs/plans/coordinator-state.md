# Coordinator state

Notes for whoever coordinates the sub-agents, so the work can be
picked up after a restart. The task list itself is `TASKLOG.md`; the
standing rules are `agent-briefs.md`.

## Operating rules (2026-09-18)

* Every sub-agent works in its own branch and worktree
  (`.worktrees/topic-*`), makes small logical commits, keeps a
  `docs/plans/progress-<topic>.md` checklist so it can be stopped and
  restarted, and pushes its branch regularly.
* Nothing merges without an independent review by a different agent,
  followed by a fix round and a provenance check. Merge is rebase on
  `main`, fast-forward only, then push `main` and delete the branch.
* Every fact carries a public citation and is cross-checked against a
  second source where one exists. The foundry's own web pages are not
  assumed correct; disagreements between sources are recorded.
* Models: Sonnet does the research, writing and fixing. Reviews are run
  with both Sonnet and Opus on the same input until
  `model-comparison.md` shows where Opus adds findings; after that Opus
  is used only where it does. The top-tier model is an escalation only
  (a cheaper model failed twice, planning, unclear data).
* Spend: this project may use at most 75 % of the weekly quota, counted
  up to 24 h before the weekly reset (Thursday 10:00 UTC). Only this
  project's own sessions count. The coordinator reads the quota and its
  own spend before launching agents, and pauses until the reset when the
  budget is used. Finishing properly matters more than saving tokens.
* The coordinator wakes on agent completion, with a 20-minute heartbeat
  to keep its context cached (one-hour cache lifetime), and keeps its
  context small: state lives in these files, not in the conversation.
* Patents still in force are listed behind a collapsed block and may be
  linked from step pages, also collapsed.
* The five-hour usage window is the tighter limit in practice: on 2026-09-18 it filled in under five hours with five or six agents running and cut one agent off in mid-work. Keep to about three agents at a time, launch nothing new once the window is above 80 %, and require agents to commit at least every 15 minutes so that a cut-off loses little. The usage endpoint allows only a few reads per hour; the ledger script reads it at most hourly.

## In flight

| Branch | Agent task | Model | State |
|---|---|---|---|
| `topic/index-filings` | round 3: review findings and Cypress annual-report coverage | Sonnet | running |
| none (read-only) | Phase 4 reviews of steps 076–088 and 089–106, reports under `tmp/p4/` | Opus | running |

Phase 4 status is in `TASKLOG.md` (001–075 merged 2026-09-18).

Phase 4 plan: twelve module batches (the Phase 2 groups in `TASKLOG.md`). Per batch: read-only review report, then a fixer on `topic/p4-<range>` applying it, then verification of the fixes, then merge. Reviewer brief: `tmp/prompts/p4-review.txt` (not tracked; its content is the Reviewer brief plus source re-fetching, second-source checks and distrust of any single source).

## Queue

2. Dual review of the patent and filings indexes, fix, merge.
3. Step-page links to the patent, paper and filings indexes.
4. Paper index second round (remaining searches, held full-text checks).
5. Phase 4: technical accuracy review of every step page by process
   module, conflict review across pages, bibliography page, final
   provenance review of the tree and the whole history.
6. Sweep of the job-listing citations (JOB-01 and the others) on about 35 pages under Common rule 11, after the Phase 4 batches that touch them.
7. Patent index coverage round on `topic/index-patents-coverage` once the patent search site stops answering with a bot check (alternative: EPO linked data as the discovery source).
8. Build polish: tracked lock file and frozen export for the hosted
   build, checker jobs before the build.
