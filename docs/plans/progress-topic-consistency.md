# Progress — topic/consistency

Applying the whole-site conflict review at
`tmp/review-consistency.md`
(0 High, 6 Medium, 8 Low; findings C-001 … C-014).

| ID | Severity | Status | Note |
|---|---|---|---|
| C-001 | Medium | open | Isolation nitride "of the order of 100 nm" vs 150 nm working figure on 003-isonit.md. |
| C-002 | Medium | open | STI trench depth 0.33 µm vs 0.3 µm on 006-stie.md. |
| C-003 | Medium | open | US 8,796,098 tunnel-oxide range: thermal (1.0–3.0 nm) vs radical (1.0–4.0 nm) embodiments not distinguished. |
| C-004 | Medium | fixed | US 5,811,358 strip quotation normalised to verbatim "(<220° C.)" at all 8 non-verbatim locations (016, 021, 029, 033, 051, 084, 087, public-sources.md:2558); verified against cached tmp/patent-cache/US5811358A.html. |
| C-005 | Medium | fixed | Checked cached STEPS-SHEET CSV export (tmp/p4/fetch/steps-sheet1.csv row 149, also 123/134/161): sheet reads "Al Cu 2/TiW deposition" (with space) at all four levels. Fixed the one non-verbatim quotation (123-tial12.md:50, was "AlCu…") to match; 149-wtial4.md and overview/index.md:705 quotes were already verbatim. Added a clause on both 123 and 149 noting the page title/steps index normalise to "AlCu" without the space, consistent with 134/161's titles (which carry no quotation of the sheet's name). No change needed to tools/steps.csv, docs/steps/index.md or docs/categories/deposition.md — their normalised spelling was already internally consistent. |
| C-006 | Medium | open | Overview passivation-nitride stack-table cell omits the step page's 0.7–0.9 µm Cypress reading. |
| C-007 | Low | open | "sulfuric" vs "sulphuric" (11 locations). |
| C-008 | Low | open | Typographic markup inserted inside verbatim quotations (multiple locations/sources). |
| C-009 | Low | open | Minus sign in "P− poly precision resistors" written 3 ways. |
| C-010 | Low | open | HMDS discussion present on 3 of 5 metal-mask steps, missing on MM3/MM4. |
| C-011 | Low | open | Same source cited with two different access dates (9 keys). |
| C-012 | Low | open | Footnote definitions of the same key differ in substance (7 keys/locations). |
| C-013 | Low | open | "line-width" vs "linewidth". |
| C-014 | Low | open | `asml-30` access date present on one page, absent on 31 others. |
