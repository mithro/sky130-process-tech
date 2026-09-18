# Progress — topic/p4-048-063 (Phase 4 fixes, steps 048–063)

Applying `tmp/p4/review-048-063.md` (54 distinct finding ids: 1 High,
14 Medium, 39 Low, several ids being the same root cause repeated on
more than one page). Each finding is independently verified against the
cited public source (or by redoing the arithmetic/cross-page check)
before being fixed or declined.

| id | severity | status | note |
|---|---|---|---|
| 061-H1 | High | fixed | Confirmed m1.1/m2.1/li.1a = 0.140 µm < poly.1a 0.150 µm and difftap.1 = 0.150 µm (ties) in periphery rules cache; dropped the false "smallest drawn line" superlative, kept the CD-maps-to-gate-length point. |
| 048-M1 | Medium | fixed | Confirmed 058-gatenit.md leaves LPCVD-vs-PECVD open and 060-bfr.md hedges the same way; 048 stated it as an inference without noting the open question. Fixed the cross-reference. |
| 048-M2 | Medium | fixed | Confirmed via OpenAlex: Voutsas & Hatalis 1992 shows the amorphous/poly boundary depends on deposition rate, not just temperature (as-deposited poly obtained at 530 °C by controlling rate); Kamins/Kinsbron place the conventional boundary near 600 °C. Fixed on 048, and the same oversimplified "<580 °C" claim on overview/index.md and categories/deposition.md (minimal edits, shared files). |
| 049-M1 | Medium | fixed | Confirmed via OpenAlex abstract: Wright 2010 is a sputtered Cr-Si-B-SiO2/Al2O3 thin-film resistor paper, no polysilicon. Annotated Deep dive bullets on 049/053/055 correctly; replaced 053's and 055's in-text sentences. |
| 050-M1 | Medium | open | |
| 051-M1 | Medium | fixed | Checked Wayback (`archive.org/wayback/available`, empty) and archive.today (404, no snapshot) for both job-01 and job-03 URLs on 2026-09-18: neither is retrievable or archived. Removed the quoted strings and the specific tool claim on 051/054/057/060; removed job-03 entirely (051/054/057/060 still use job-01 for other, out-of-scope pages, so its inventory key stays; job-03 became fully unused, so its inventory entry was removed). |
| 052-M1 | Medium | fixed | Confirmed via OpenAlex abstract: Tsang 2014's mechanism is hydrogen diffusing through eroded LPCVD-nitride corners (a bank-position effect), not the implant-mask edge. Fixed in-text and Deep dive on 049/052/055. |
| 053-M1 | Medium | fixed | = 049-M1 |
| 054-M1 | Medium | fixed | = 051-M1 |
| 055-M1 | Medium | fixed | = 049-M1; replaced in-text sentence with Lane & Wrixon's design space, added lane-1989 footnote. |
| 055-M2 | Medium | fixed | = 052-M1 |
| 057-M1 | Medium | fixed | Confirmed via OpenAlex: Temple-Boyer 1998 is a silane/ammonia LPCVD study giving ~600 MPa, not 1 GPa DCS nitride. Reworded on 057/058 to cite it correctly and keep 1 GPa as a typical-industry-value claim. |
| 058-M1 | Medium | fixed | = 057-M1 |
| 062-M1 | Medium | open | |
| 062-M2 | Medium | open | |
| 063-M1 | Medium | open | |
| 048-L1 | Low | open | |
| 048-L2 | Low | open | |
| 048-L3 | Low | open | |
| 049-L1 | Low | open | |
| 049-L2 | Low | open | |
| 049-L3 | Low | open | |
| 050-L1 | Low | open | |
| 050-L2 | Low | open | |
| 050-L3 | Low | open | |
| 051-L1 | Low | open | |
| 051-L2 | Low | open | |
| 051-L3 | Low | open | shared with 057-L3 |
| 052-L1 | Low | open | |
| 053-L1 | Low | open | shared with 056-L2 |
| 053-L2 | Low | open | |
| 054-L1 | Low | open | |
| 054-L2 | Low | open | |
| 055-L1 | Low | open | |
| 055-L2 | Low | open | |
| 055-L3 | Low | open | |
| 056-L1 | Low | open | |
| 056-L2 | Low | open | = 053-L1 |
| 056-L3 | Low | open | |
| 057-L1 | Low | open | |
| 057-L2 | Low | fixed | = 051-M1 |
| 057-L3 | Low | open | = 051-L3 |
| 058-L1 | Low | fixed | Added the PDK's NGNIT e-test corroboration and the Tsang et al. nitride-cap corroboration (with correct mechanism) to What this step is / Resistor protection. |
| 059-L1 | Low | open | |
| 059-L2 | Low | open | |
| 060-L1 | Low | open | |
| 060-L2 | Low | open | |
| 060-L3 | Low | open | |
| 060-M-ref | Low | fixed | = 051-M1; replaced with lederer-2003 (already on page), which names the Surfscan SP1 BSIM explicitly. |
| 061-L1 | Low | open | |
| 061-L2 | Low | open | |
| 061-L3 | Low | open | |
| 062-L1 | Low | open | |
| 062-L2 | Low | open | |
| 063-L1 | Low | open | |
| 063-L2 | Low | open | |

## Checkers and build

To run from the worktree in the foreground before finishing:
`check_steps.py`, `check_refs.py`, `check_machines.py`,
`check_materials.py`, `check_masks.py`, `check_papers.py`,
`gen_papers.py --check`, and `sphinx-build -W -q -b html`.
