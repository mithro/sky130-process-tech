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
family or an INPADOC extended family.

Retrieved 2026-09-18. The index holds 211 families (1345 members in total). Every family's representative
record page was fetched; 1345 of the 1345 members have their own record page
fetched (the rest are listed in the fetched family table of their
representative but were not fetched separately — every possible term
of those families' members has already ended, so nothing about
their status turns on the record not fetched).

## Legal caveat

Statuses, dates and estimated expiries are as shown by the public
databases (Google Patents, using IFI Claims legal-status and expiry
data) on the retrieval date named on this page. They are not a legal
opinion and are not exhaustive: maintenance-fee lapses, terminal
disclaimers, patent term extensions, oppositions, reissues and the
national validations of a European patent are not fully captured.
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
| Total | 211 | 1345 |
| Shown as expired | 174 | 1069 |
| Shown as in force | 35 | 267 |
| Status unknown | 2 | 9 |

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
