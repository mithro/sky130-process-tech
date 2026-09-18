# Progress — topic/consistency

Applying the whole-site conflict review at
`/home/admin/github/mithro/sky130-process-tech/tmp/review-consistency.md`
(0 High, 6 Medium, 8 Low; findings C-001 … C-014).

| ID | Severity | Status | Note |
|---|---|---|---|
| C-001 | Medium | fixed | 003-isonit.md:25 now reads "of the order of 150 nm — the working figure used throughout this module, not a SkyWater number", matching the module's later pages and the materials index. |
| C-002 | Medium | fixed | 006-stie.md:49 and :268 now use 0.33 µm (matching :42 and 011-filox.md's rounding), and the fill aspect ratio corrected to ~1.8:1. |
| C-003 | Medium | fixed | Verified both embodiments in cached tmp/patent-cache/US8796098B1.html; 038-depi.md, 039-tunme.md, 040-ono.md and the PAT-04 inventory entry now state both ranges. |
| C-004 | Medium | fixed | US 5,811,358 strip quotation normalised to verbatim "(<220° C.)" at all 8 non-verbatim locations (016, 021, 029, 033, 051, 084, 087, public-sources.md:2558); verified against cached tmp/patent-cache/US5811358A.html. |
| C-005 | Medium | fixed | Checked cached STEPS-SHEET CSV export (tmp/p4/fetch/steps-sheet1.csv row 149, also 123/134/161): sheet reads "Al Cu 2/TiW deposition" (with space) at all four levels. Fixed the one non-verbatim quotation (123-tial12.md:50, was "AlCu…") to match; 149-wtial4.md and overview/index.md:705 quotes were already verbatim. Added a clause on both 123 and 149 noting the page title/steps index normalise to "AlCu" without the space, consistent with 134/161's titles (which carry no quotation of the sheet's name). No change needed to tools/steps.csv, docs/steps/index.md or docs/categories/deposition.md — their normalised spelling was already internally consistent. |
| C-006 | Medium | fixed | Overview stack-table cell for passivation nitride now also gives the NTSD page's 0.5–0.9 µm reading and the Cypress 0.7–0.9 µm figure, matching the caption's promise to quote what the step pages say. |
| C-007 | Low | fixed (partial disagreement) | Fixed 8 of the review's 11 locations (categories/strip.md:155, wet-bench.md:5,99,174,238, single-wafer-spin-processor.md:174,236,303). Declined the other 3 (materials/wet-chemicals.md:183, steps/016-lvtnis.md:87, steps/087-nsdis.md:105): each is inside a verbatim quotation attributed to Wikipedia ([^wiki-h2so4], [^wiki-piranha]); fetched en.wikipedia.org/wiki/Sulfuric_acid and .../Piranha_solution directly and confirmed both articles use the American spelling "sulfuric" in the exact quoted sentences, so changing it there would make the quotation non-verbatim. The review's own quotation exemption ("Leave quotations… untouched") applies to these three; they were mis-scanned as prose. |
| C-008 | Low | open | Typographic markup inserted inside verbatim quotations (multiple locations/sources). |
| C-009 | Low | open | Minus sign in "P− poly precision resistors" written 3 ways. |
| C-010 | Low | open | HMDS discussion present on 3 of 5 metal-mask steps, missing on MM3/MM4. |
| C-011 | Low | open | Same source cited with two different access dates (9 keys). |
| C-012 | Low | open | Footnote definitions of the same key differ in substance (7 keys/locations). |
| C-013 | Low | open | "line-width" vs "linewidth". |
| C-014 | Low | open | `asml-30` access date present on one page, absent on 31 others. |
