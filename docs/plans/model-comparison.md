# Reviewer model comparison

Reviews are run twice on the same input, once per model, by agents that
do not see each other's report. Each row records what each found, so the
more expensive model is used only where it adds findings.

| Date | Input | Sonnet findings (H/M/L) | Opus findings (H/M/L) | Found only by Opus | Found only by Sonnet | Conclusion |
|---|---|---|---|---|---|---|
| 2026-09-18 | `topic/followups-masks`, 21 commits re-describing eleven sources on 83 files | 1/0/0 — the one High was a false positive (the patent does give the quoted tunnel-dielectric figure, checked by the coordinator); 54 tool calls | 1/5/7 — a chapter title from the wrong edition of a book, non-verbatim quotes and same-source leftovers; 105 tool calls | all 13 | none valid | Sonnet passed a book's chapter titles against a different edition's contents and misread a patent; for reviews that verify quotations and source descriptions, use Opus. Sonnet cost about 0.7 of Opus in tokens and found nothing valid. |
