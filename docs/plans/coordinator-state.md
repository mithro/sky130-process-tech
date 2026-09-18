# Coordinator state

Working notes for whoever coordinates the sub-agents, so the work can be
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

## In flight (2026-09-18 evening)

| Branch | Agent task | Model | State |
|---|---|---|---|
| `topic/index-patents-coverage` | fix the verification findings (member-status parser, listed-only members, fee-lapse family), then discovery through the patent office's keyless public search; triage log in `docs/plans/patent-discovery-log.md` | Sonnet | running; needs independent verification before merge |
| `topic/index-papers-r3` | add the 13 papers the review found, full-text and affiliation searches, extra generated page of excluded papers that name the process | Sonnet | running; needs review |
| `topic/link-check` | `tools/check_links.py`, site-wide run, repairs under Common rule 11 | Sonnet | running; needs review |
| `topic/consistency` | 14 findings of the whole-site conflict review (`tmp/review-consistency.md`) | Sonnet | running; needs verification |

Reports and prompts are under `tmp/` (not tracked): `tmp/p4/` (Phase 4
reviews and verifications), `tmp/prompts/` (reviewer, fixer and verifier
briefs used for every batch), `tmp/review-*.md`, `tmp/verify-*.md`.
Spend is logged by `tmp/tools/ledger.py` in `tmp/quota-ledger.jsonl`.

Done on 2026-09-18: Phase 4 technical review of all 171 step pages in
twelve batches; metal cap composition sweep; job-listing citation sweep;
first versions of the patent and filings indexes; paper index round 2.

## Queue

1. Verify and merge the four branches in flight.
2. Filings index next round: the review's remaining prioritised
   additions, the three deferred Low findings, and a location check that
   abstains less often (170 of the quotation locations are unchecked).
3. Links from step, machine, material and mask pages to the patent,
   paper and filings indexes (patents still in force inside collapsed
   blocks); needs the patent coverage round merged first.
4. Final provenance review of the tree and of the whole git history (the
   hosted repository is public), then the last full build.
5. Build polish: tracked lock file and frozen export for the hosted
   build, checker jobs before the build.
6. Close-out: TASKLOG brought up to date, progress files under
   `docs/plans/` kept as the record of each branch.

## Notes

* 2026-09-18: pushes hung because the forwarded SSH agent socket stopped
  answering once the owner's terminal went away. The repository has its
  own key file configured for the remote's host alias, so the local git
  config now sets `core.sshCommand` to ssh with `IdentityAgent=none`.
  Remove that setting if the key is ever moved back into an agent.
