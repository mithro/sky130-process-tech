<!-- Generated from data/patents.yaml by tools/gen_patents.py; do not edit. -->

(patents-index)=
# Patent index

A worldwide index of patents and published applications related to
the SKY130 process technology and its lineage (Cypress
Semiconductor, SkyWater Technology and Infineon Technologies, and
suppliers' patents that a docs page already cites or that a public
source ties to this process lineage), generated from one curated
dataset, `data/patents.yaml`. The unit of record is the patent
**family as grouped by Google Patents**: its family ID, the
representative record page, and its other publications and
applications (the family's *Publications* and *Also Published As*
tables). This is close to, but not the same as, an EPO DOCDB simple
family or an INPADOC extended family. Each member's Espacenet link
is a search query for its own number, not a direct record link (the
Espacenet web interface does not accept scripted retrieval); Google
Patents' own record page, linked alongside it, is the working
full-text link this index relies on for every member.

Records were retrieved 2026-09-14 to 2026-09-21 (individual records carry their own
`verified` date). The index holds 552 families (1845 members in total). Every family's representative
record page was fetched; 1786 of the 1845 members have their own record page
fetched (1460 from Google Patents, 326 from USPTO Patent Public
Search).
The remaining 59 are listed in the fetched Google Patents family table of
their representative but were not fetched separately: a
time-budgeted departure from this index's rule of fetching every
member of a family whose earliest priority is on or after
1999-05-29, recorded as an exception in
`docs/plans/patent-index-design.md`'s "Verification levels". Each
such row carries its publication number, country, kind and
publication date from the representative's own family table, says
so in its *Verified* column, and shows no status. 15 members of these sit in 2 families already shown expired on other grounds; the remaining 44 members, in 6 families **not** shown expired, are each bounded
conservatively (the family's earliest priority date + 21 years)
rather than assumed ended, per the design's rule 3.
 Separately, 324 of the 552 families in this index
rest on USPTO Patent Public Search instead of Google Patents, for two different reasons:
34 families because Google Patents stayed unreachable while
they were found, and 290 families by design, sourced via PPUBS for
consistency with the round's own PPUBS-based classification-sweep discovery method even though
a plain fetch showed Google Patents reachable that day
(see "PPUBS fallback" and its "round 5 source variant" in
`docs/plans/patent-index-design.md`); each says which reason applies
in its own *Legal status* and *Verified* lines, carries no legal status or adjusted-expiration
date, and enumerates only the single member PPUBS's own search returned, not a complete family.
Its expiry is a term-arithmetic bound, conservative for the collapse decision (a family is not
shown expired unless that bound has already passed with no possible US patent term adjustment)
but not necessarily an upper bound on the true date: PPUBS does not report a term adjustment a
still-collapsed family's real term may already include.

## Legal caveat

Statuses, dates and estimated expiries are as shown by the public
databases (Google Patents, using IFI Claims legal-status and expiry
data) on the retrieval date named on this page. They are not a legal
opinion and are not exhaustive: maintenance-fee lapses, terminal
disclaimers, patent term extensions, oppositions, reissues and the
national validations of a European patent are not fully captured. A US
patent lapsed for non-payment of a maintenance fee can be reinstated on
a petition showing the delay was unintentional, within statutory time
limits that depend on which fee was missed (37 CFR 1.378(a)/(c),
Cornell LII, https://www.law.cornell.edu/cfr/text/37/1.378); a family
shown as expired solely on the strength of a fee lapse, while its term
has not otherwise run, says so in its notes.
Before relying on the status of any family, check the linked
official record.

## Unexpired and unknown-status families are collapsed

A family shown as in force, or whose expiry could not be bounded
from the records retrieved (`unknown`), appears on {ref}`patents-families`
as a collapsed block whose title shows only the representative's
publication number and its status; open it to see the rest. A
family shown as expired is written out in full. The grouped pages
below never repeat a collapsed family's status or dates outside the
collapsed entry.

## Relations

Each family links to one or more pages of this reference, with a
relation:

* **cited on this page** (`cited-on-page`) — the page cites a member of this family.
* **same-lineage assignee** (`same-lineage-assignee`) — the original assignee is in the process lineage (Cypress Semiconductor, SkyWater Technology, or Infineon Technologies for patents that came from Cypress); this is not evidence that SKY130 uses the technique.
* **technique class** (`technique-class`) — the family describes the class of technique the page covers, without a citation on that page.

## Counts

| | Families | Members |
|---|---|---|
| Total | 552 | 1845 |
| Shown as expired | 265 | 1177 |
| Shown as in force | 47 | 419 |
| Status unknown | 240 | 249 |

## Scope and completeness

This index began as every patent already cited on a docs page (169 families of the total entered this way and no other), then widened by following each seed's Google Patents family table and citation lists, by a handful of assignee+keyword searches for specific process modules, and by an `assignee="Weebit Nano"` search once ReRAM was brought into scope. It is **not** the result of an exhaustive, systematic sweep of every process module against every lineage assignee: an independent review of this dataset during its construction found at least a dozen absent Cypress/Infineon families from just three more searches, named six process modules never searched at all, and notes that the index holds 356 Cypress Semiconductor families and 7 Infineon Technologies families but only 1 SkyWater Technology family, though SkyWater is named in this index's own scope. Treat this index as a starting point for the SKY130/Cypress/SkyWater/Infineon patent landscape, not as proof that a family absent from it does not exist.

Discovery methods recorded across the 552 families: 371 families `assignee-search`; 172 families `cited-in-docs`; 13 families `citing-seed`; 10 families `cited-by-seed`; 4 families `continuation-search`. A family can carry more than one method (reached more than one way), so these do not sum to the family count.

A systematic assignee sweep of USPTO Patent Public Search on 2026-09-19 (Cypress Semiconductor, SkyWater Technology, Longitude Flash Memory Solutions, Infineon Technologies LLC, Spansion, Ramtron, Weebit Nano, restricted to process-module title keywords, run because Google Patents was unreachable that day) found 211 distinct families: 39 were already in this index and 24 were added. A second sweep on 2026-09-20 dropped the title-keyword restriction and queried the same core assignees (Cypress, SkyWater, Longitude, Infineon Technologies LLC, Ramtron) by CPC class instead (H01L21/23/27/29, H10B, H10N70, G03F, C23C, C30B, plus the H10D/H10P/H10W reclassification targets the first sweep's own review found necessary). It found 559 distinct families across 587 assignee-restricted hits, corrected SkyWater's indexed name to "Sky Water Technology Foundry, Inc." (two words -- the keyword sweep's "skywater" spelling had matched nothing), and added 81 more families plus one new member (a just-granted patent) of an existing SkyWater family. Of the 559, 387 were rejected by a scripted title-keyword classifier rather than individually reviewed; a later audit found the classifier's vocabulary list, not its underlying CPC-class sweep, was the weak link, and its default reject bucket was materially wrong (see the next paragraph). The 91 Spansion families the round-4 sweep had left undecided were re-triaged on a coordinator decision that Spansion is not process lineage (the 2015 Cypress-Spansion merger is ownership, not fab lineage): each row names the specific existing index entry that already covers its technique. Two rows (process/UV-induced-charging damage protection during BEOL processing) briefly had no covering entry and were held as the coordinator's own named exception, but this round's own H1 re-triage of the default bucket (see the next paragraph) then added two same-lineage-assignee Cypress families of that identical technique class, so the exception's premise no longer held; both rows were re-decided out of scope, now naming those two Cypress families as their covering entries. Of the round-4 Weebit Nano backlog and that round's own supplementary Weebit CPC sweep, only one further family (a device/process patent on ReRAM retention) was added; the rest remain circuit-level programming/read/write/sensing schemes, out of scope by this index's own exclusion of circuit patents. The Saifun/Cypress Semiconductor Ltd. NROM estate (the Netanya line, merged into Spansion in 2008) is excluded by this same Spansion decision, not overlooked: it is a real gap in the sense that no public source disproves it belongs, but the coordinator's ruling applies to it identically.

A later audit (round 6) found the classifier's title-keyword vocabulary rejected roughly a third of the 387 by default without any individual review, including families whose titles used a synonym or a different granularity of an in-scope phrase ("contact openings" for "contact structure", "planarized structure" for "CMP", and so on) and at least one family (a method of ONO integration into a logic CMOS flow) a previous round had already judged in scope before the classifier silently reversed it. Every one of the 387 rejected rows was re-read this round from that family's own USPTO Patent Public Search full-text title and abstract (not the classifier's title-only heuristic): 189 families were found in scope and added -- process, device-structure and equipment/metrology technique classes across CMP, etch, deposition, implant, oxidation, lithography, strip, contact/interconnect, STI, NVM device structures, and process-induced-charging protection -- and the remaining rejections were confirmed out of scope with a reason specific to that family's own abstract (ferroelectric/FRAM material, packaging/assembly, circuit or system-level content, EDA/software tooling, or a memory technology -- MRAM, FinFET, 3-D NAND -- no public source shows this lineage's planar-CMOS PDK offering). A handful of rows turned out to be the same DOCDB family as one already decided elsewhere in this round (found again under a different assignee query) and are recorded as such rather than duplicated. One family's abstract could not be fetched after repeated retries (a persistent server error) and was decided from its title and CPC classes alone, consistent with the already-validated keyword-bucket pattern for the same phrase. The same audit found two further gaps in the CPC-classification sweep itself: 5 Monterey Research families, the entity Cypress sold a tranche of its flash-memory patents to in 2019 (patents granted after the transfer print Monterey, not Cypress, so the original sweep's assignee list never found them), and 13 process/equipment families in CPC classes (B24B, B08B, H01J37, H05H, C25D and neighbours -- CMP, chamber cleaning, plasma conditioning, wet-process carriers, electroplating) the original sweep's own class list did not reach; both gaps were swept and triaged the same way, by abstract. Every decision this round, and the reason for each, is recorded in the repository at `docs/plans/patent-discovery-log.md` (outside the built site). The round-5 sweep's own residue has now been read and decided in full, not merely triaged by keyword, and round 7 closed the class-restriction gap the round-5 verification report had flagged but only sampled: that report's own unrestricted "cypress semiconductor".as. query, read from just its first 999 hits without grouping by family, had reported "roughly 586" distinct families against this index's 494 CPC-restricted ones. Properly paginating that same query round 7 found the true total is **3,142** distinct families -- the round-5 figure was itself an undercount, not a completed sweep. Of the 3,142: 494 were already covered by the CPC-restricted sweep (no paging gap) and 24 more were already decided in an earlier discovery-log round under a different query; of the remaining 2,624, 2,473 were decided out of scope by their own CPC classes and title (predominantly circuit content spanning Cypress's full history -- programmable logic, PLL/clock, sense-amplifier, CAM/FIFO, USB-PD, touch-sensing and wireless/IoT patents -- using the same CPC-facet method this index's own design already uses to define the swept boundary), 141 more were decided out of scope individually by abstract (packaging, test circuits and assorted circuit schemes), and 10 families were added: an antifuse device structure, seven CMOS image-sensor/photodiode device structures (wells, junction and implant/isolation structures -- this index has a public source, filing CYP-08, for image-sensor fabrication at this lineage's own fab, and an existing precedent family, so the exclusion an earlier draft of this round gave them was withdrawn), and two MEMS/SAW wafer-fabrication device structures. The same unrestricted query, re-run for every other lineage assignee whose CPC-restricted total looked incomplete (Longitude Flash Memory Solutions, Infineon Technologies LLC, Monterey Research), found 68 previously-unswept rows, 20 of them the same DOCDB family as a Cypress row above (found again under a second assignee query) and recorded as such rather than duplicated -- 48 distinct new families, all out of scope; no additions from these three. `docs/plans/patent-discovery-log.md`'s "Round 7" section records every decision, including a small number of borderline rulings. What remains: the 2,473-family CPC-classification bucket was decided by CPC facet and title, not read individually -- a random and a targeted adversarial sample (`tmp/verify-index-patents-r4.md`) found the split reliable once two narrow leaks in the CPC exclusion list were closed, but a future round could still spot-check a further sample; no round's sweep has looked outside the United States -- PPUBS indexes only US grants, US pre-grant publications and USOCR, so a lineage family with no US member is invisible to this index however it was found; and no attempt has been made to find a PPUBS-sourced family's other-jurisdiction or other-US-member siblings.

## Other views

* {ref}`patents-families` — the canonical entry for every family, in priority-date order.
* {ref}`patents-by-module` — grouped by process module.
* {ref}`patents-by-assignee` — grouped by original assignee.
* {ref}`patents-by-jurisdiction` — grouped by country or office, and by family size.
* {ref}`patents-by-date` — grouped by decade of priority date, and by status.

```{toctree}
:hidden:

families
by-module
by-assignee
by-jurisdiction
by-date
```
