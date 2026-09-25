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

## In flight (2026-09-25)

Owner rule since 2026-09-25: at most FOUR sub-agents running at any time. Everything else waits in the
queue below; a stopped agent is restarted by giving a fresh agent the same task text plus "read the
progress file docs/plans/progress-<name>.md and continue from where it stops".

Running: rd-steps-014-034; the queue is resumed in order as the 5-hour window allows

| Branch / worktree | Task | Model | State |
|---|---|---|---|
| `topic/rd-figures-s8` | W1c: emulator improvements (conformal rounding, PSG profile, straight tapers) then series S8 contact + metal 1 (107–117) | Opus | running since 2026-09-25 |
| `topic/rd-steps-035-047` | W2 batch 3 (SONOS + gate oxides) | Sonnet | running since 2026-09-25 |
| `topic/rd-materials` | W3 batch 3: the twelve material class pages | Sonnet | running since 2026-09-25 |
| `topic/rd-machines-a` | W3 batch 2: machine class pages 1–15 (alphabetical) | Sonnet | running since 2026-09-25 |

Queue, in order (stopped 2026-09-25 to respect the four-agent rule; each has a worktree and progress file):

6. Reviews as branches finish: rd-site (verify fixes), rd-figures-s3s4 (verify), rd-steps-014-034, rd-indexes, rd-links2, rd-preserved2, rd-inforce-sonos, rd-figures-s5.
7. Next batches after those: W2 035–047 (after the S3/S4 figures merge), 048–063 (after S5), figure series S6–S11, W3 class-page batches (machines, materials, masks, categories), the final term-link pass on main.
8. `topic/cypress-history`: merged 2026-09-25 (two review rounds by its own session; landing-page card added by the coordinator). Its two tool follow-ups: chain-layout arrow floating below a branch box and dashed hedged arrows in `gen_figures.py`; smart dashes turning `--` into an en dash in autolink text.

Merge order when several are ready: tooling first, then site pages, then content batches; rebase +
fast-forward only; a batch's rebase conflicts in scripted regions are resolved by re-running the script.

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
