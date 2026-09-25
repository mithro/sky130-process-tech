# Progress — rd-overview (W4 overview page)

Branch: topic/rd-overview. Task: docs/overview/index.md only (C7 + guide §4.7).
`docs/overview/sky130b-reram.md` checked: it is a different page type (companion
ReRAM page), not named by C7 or guide §4.7, and none of the guide's overview rules
mention it. Left untouched.

## Plan (from the task)

1. Reorder H2 sections (labels travel with them) — done.
2. "On this page" five-bullet {ref} list after the opening paragraph.
3. Run-in bold module paragraphs -> H3 (module names must match module table exactly).
4. Prose rules on the 13 paragraphs > 120 words; back-end stack table caption.
5. Read rendered page top to bottom, desktop + 400px, fix what reads badly.

## Step 1 — H2 reorder (commit 1)

Reordered whole H2 blocks (each including its own `(label)=` line and all content
down to, but not including, the next section's label/heading) with a Python script
that sliced the file by exact line ranges and reassembled it — no line was
edited, only moved. Verified with `diff <(sort before) <(sort after)` = identical
(pure permutation of lines).

New order (matches task and report-C7 exactly):
How to read this reference -> The flow by module -> A simplified cross-section ->
Front end, middle of line and back end -> What SKY130 is -> The metal cap and
barrier question -> Key open questions -> (generated block, unchanged) -> References.

Checks after step 1: check_preserved.py (no --allow-added needed, plain move),
check_steps/refs/machines/materials/masks/papers/patents/filings/inforce,
gen_papers/gen_patents/gen_filings/gen_index_links/gen_figures --check, and a
`-W` sphinx build — all pass, 0 problems.

## Open items / guide ambiguities to record

(filled in as work proceeds)
