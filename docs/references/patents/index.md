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
`verified` date). The index holds 443 families (1735 members in total). Every family's representative
record page was fetched; 1676 of the 1735 members have their own record page
fetched (1460 from Google Patents, 216 from USPTO Patent Public
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
 Separately, 215 of the 443 families in this index
rest on USPTO Patent Public Search instead of Google Patents, which stayed unreachable while
they were found (see "PPUBS fallback" in `docs/plans/patent-index-design.md`); each says so
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
| Total | 443 | 1735 |
| Shown as expired | 265 | 1177 |
| Shown as in force | 47 | 419 |
| Status unknown | 131 | 139 |

## Scope and completeness

This index began as every patent already cited on a docs page (169 families of the total entered this way and no other), then widened by following each seed's Google Patents family table and citation lists, by a handful of assignee+keyword searches for specific process modules, and by an `assignee="Weebit Nano"` search once ReRAM was brought into scope. It is **not** the result of an exhaustive, systematic sweep of every process module against every lineage assignee: an independent review of this dataset during its construction found at least a dozen absent Cypress/Infineon families from just three more searches, named six process modules never searched at all, and notes that the index holds 245 Cypress Semiconductor families and 7 Infineon Technologies families but only 1 SkyWater Technology family, though SkyWater is named in this index's own scope. Treat this index as a starting point for the SKY130/Cypress/SkyWater/Infineon patent landscape, not as proof that a family absent from it does not exist.

Discovery methods recorded across the 443 families: 262 families `assignee-search`; 172 families `cited-in-docs`; 13 families `citing-seed`; 10 families `cited-by-seed`; 4 families `continuation-search`. A family can carry more than one method (reached more than one way), so these do not sum to the family count.

A systematic assignee sweep of USPTO Patent Public Search on 2026-09-19 (Cypress Semiconductor, SkyWater Technology, Longitude Flash Memory Solutions, Infineon Technologies LLC, Spansion, Ramtron, Weebit Nano, restricted to process-module title keywords, run because Google Patents was unreachable that day) found 211 distinct families: 39 were already in this index and 24 were added. A second sweep on 2026-09-20 dropped the title-keyword restriction and queried the same core assignees (Cypress, SkyWater, Longitude, Infineon Technologies LLC, Ramtron) by CPC class instead (H01L21/23/27/29, H10B, H10N70, G03F, C23C, C30B, plus the H10D/H10P/H10W reclassification targets the first sweep's own review found necessary) -- systematic by classification rather than by guessed keywords, per this index's own stated goal. It found 559 distinct families across 587 assignee-restricted hits, corrected SkyWater's indexed name to "Sky Water Technology Foundry, Inc." (two words -- the keyword sweep's "skywater" spelling had matched nothing), and added 81 more families plus one new member (a just-granted patent) of an existing SkyWater family. The Spansion estate was separately re-triaged on a coordinator decision that it is not process lineage (the 2015 Cypress-Spansion merger is ownership, not fab lineage): a systematic check found every Spansion technique the estate covers already has a lineage or expired example elsewhere in this index, so all 91 still-deferred Spansion families were marked out of scope rather than added. Of the round-4 Weebit Nano backlog and this round's own supplementary Weebit CPC sweep, only one further family (a device/process patent on ReRAM retention) was added; the rest remain circuit-level programming/read/write/sensing schemes, out of scope by this index's own exclusion of circuit patents. Both sweeps, every family's triage decision and the reason for each are recorded in the repository at `docs/plans/patent-discovery-log.md` (outside the built site). What is left: the Cypress CPC sweep's own "in scope, left for later" residue is empty (every hit was triaged to a decision this round), but neither sweep looked beyond these five core assignees, and no attempt has been made to find a PPUBS-sourced family's other-jurisdiction or other-US-member siblings.

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
