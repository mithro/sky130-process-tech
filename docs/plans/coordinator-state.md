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

## In flight (2026-09-19)

| Branch | Agent task | Model | State |
|---|---|---|---|
| `topic/index-patents-r3` | classification-based sweep of the lineage assignees in the patent office's public search, every hit family triaged in `docs/plans/patent-discovery-log.md`; the acquired company's estate re-triaged as out of scope except technique examples | Sonnet | running; needs independent verification before merge |

Everything else is merged on `main` (see `TASKLOG.md`): all 171 step
pages technically reviewed and fixed, the metal cap sweep, the conflict
review, the three indexes with their generators and checkers, links from
the process pages, collapsed notes for patents in force, the link check,
the final provenance audit, the hosted build running every offline
checker before building.

## Queue

1. Verify and merge the patent sweep.
2. Optional further rounds, in order of value: filings location check
   (case-insensitive captions, sub-item numbers); non-US member records
   for the newer patent families once the patent full-text site answers
   this machine again; the five held papers.
3. Close-out report to the owner, including the decision left to them:
   whether patents in force should be collapsed in page prose (done) or
   only flagged.

## Notes

* 2026-09-18: pushes hung because the forwarded SSH agent socket stopped
  answering once the owner's terminal went away. The repository has its
  own key file configured for the remote's host alias, so the local git
  config now sets `core.sshCommand` to ssh with `IdentityAgent=none`.
  Remove that setting if the key is ever moved back into an agent.
