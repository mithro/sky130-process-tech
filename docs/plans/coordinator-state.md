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

## In flight (2026-09-20)

Readability phase. Plan: `docs/plans/readability-plan.md`. Agents get the ground rules of that plan, the
check list of `agent-briefs.md`, one worktree and branch each, and a progress file
`docs/plans/progress-<name>.md`.

| Branch / worktree | Task | Model | State |
|---|---|---|---|
| `topic/rd-site` | W4: landing page cards, references index table, glossary by letter, first-use `{term}` links, inventory anchors | Sonnet | running since 2026-09-25 |
| `topic/rd-overview` | W4: overview page reorder, module H3s, prose rules | Sonnet | running since 2026-09-25 |
| `topic/rd-links2` | second check of the four dead generated-page links; `archive_url` in the datasets | Sonnet | running since 2026-09-25 |
| `topic/rd-figures-s3s4` | W1c series S3 SONOS + S4 gate oxides (035–047) | Opus | running since 2026-09-25 |
| `topic/rd-figures-s5` | W1c series S5 poly (048–063); starting state assumed from the S4 pages, reconcile at merge | Opus | running since 2026-09-25 |
| `topic/rd-steps-014-034` | W2 batch 2 (wells module) | Sonnet | running since 2026-09-25 |
| `topic/rd-indexes` | W3 batch 1: machines, materials and masks index pages | Sonnet | running since 2026-09-25 |
| `topic/cypress-history` (another session, `sky130-process-tech-54`) | Cypress process history in a new `docs/history/` section; merges only when told | — | running since 2026-09-25 |

Every branch gets an Opus review (rendered pages included), a fix round by its writer, then the coordinator
rebases and fast-forward merges. Merge order when several are ready: tooling/generators first, then site
pages, then content batches (rebase conflicts in the scripted term links are resolved by re-running
`tools/link_terms.py`, not by hand).

Order after these: apply the pilot review's guide corrections, merge the pilot, then W2 batches module by
module, each module's figures landing before its readability batch. Quota week now runs 2026-09-24 → 2026-10-01
10:00 UTC (75-point cap by 2026-09-30 10:00 UTC).

Merged 2026-09-20: W0c citation links (all Wikipedia reading-list bullets are direct links; `--refresh` re-points
inline links after a definition's first URL changes — run both link tools with `--refresh` after any Wayback conversion).

If the account quota stops the agents: each commits per page or per step and keeps
`docs/plans/progress-<name>.md`; restart by giving a new agent the same task text (the plan's W-item), the
worktree and "read the progress file and continue".

Merged so far: guide, theme + `check_preserved.py`, generators, figure tooling + 16 figures (see the plan's
status column). Reviews live under the git-ignored `tmp/reviews/`.

Next: Opus review of each branch (rendered pages included), fixes, merge; then W0c (citation links — after the
generators branch, which touches the same region of 206 pages), W0e, W0f, W1a; then the page batches W2–W4.
Local `main` is pushed to the `next` branch on origin.

## Open items, none of them blocking (details in `TASKLOG.md`)

* Patent index: families found through the patent office's public search
  carry only their US member; non-US members and the full-text site's
  status data can be added once that site answers this machine again.
* Filings index: 48 quotation locations the online check cannot
  determine; merger proxy and deregistration documents with no public
  copy are declared gaps.
* Paper index: five held items; two bibliographic services refuse
  scripted access.
* Decisions left to the owner: whether passages from patents in force should stay collapsed
  in page prose (done) or only be flagged.

## Notes

* 2026-09-18: pushes hung because the forwarded SSH agent socket stopped
  answering once the owner's terminal went away. The repository has its
  own key file configured for the remote's host alias, so the local git
  config now sets `core.sshCommand` to ssh with `IdentityAgent=none`.
  Remove that setting if the key is ever moved back into an agent.
