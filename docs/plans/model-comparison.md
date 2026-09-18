# Reviewer model comparison

Reviews are run twice on the same input, once per model, by agents that
do not see each other's report. Each row records what each found, so the
more expensive model is used only where it adds findings.

| Date | Input | Sonnet findings (H/M/L) | Opus findings (H/M/L) | Found only by Opus | Found only by Sonnet | Conclusion |
|---|---|---|---|---|---|---|
| 2026-09-18 | `topic/followups-masks`, 21 commits re-describing eleven sources on 83 files | 1/0/0 — the one High was a false positive (the patent does give the quoted tunnel-dielectric figure, checked by the coordinator); 54 tool calls | 1/5/7 — a chapter title from the wrong edition of a book, non-verbatim quotes and same-source leftovers; 105 tool calls | all 13 | none valid | Sonnet passed a book's chapter titles against a different edition's contents and misread a patent; for reviews that verify quotations and source descriptions, use Opus. Sonnet cost about 0.7 of Opus in tokens and found nothing valid. |
| 2026-09-18 | Phase 4 technical review of steps 001–013 on `main` (13 pages) | 0/0/2, verdict approve; 101 tool calls, 0.33 M tokens | 1/7/38, approve with fixes; 210 tool calls, 0.45 M tokens — a trench depth derived from a drawing by double-counting a step height, a device name that does not match the device described, an unverifiable quotation | 44 (subject to the fixer's verification) | 1 of its 2 Lows | Sonnet confirms that quotations and numbers match their sources but does not question the reasoning built on them; Opus rechecks derivations and device identities. Phase 4 reviews and fix verification use Opus; Sonnet writes and fixes. |
