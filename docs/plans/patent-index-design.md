# Patent index — design

Status: proposal, 2026-09-14. Task: "Patent index pages" in
`docs/plans/TASKLOG.md`. This file sits in `docs/plans/`, which the
Sphinx build excludes.

## Goal

A set of reference pages under `docs/references/patents/` listing
patents and published applications related to the SKY130 process
modules and their lineage, generated from one curated dataset,
`data/patents.yaml`, and checked by `tools/check_patents.py`. The first
phase (this branch) builds and checks the dataset; the pages come later.

## Dataset: `data/patents.yaml`

### Unit of record: the family

One record per patent family. The family is the grouping Google Patents
shows on a record page: its family ID (the "ID=" heading of the
*Family* section) names the record (`id: GP40072804`), and the members
are the representative publication, its other versions (pre-grant
publications), the *Publications* table and the *Also Published As*
table (`docdbFamily` in the page markup). This grouping is close to,
but not the same as, the EPO DOCDB simple family or the INPADOC
extended family: Google places US continuations that share every
priority claim in the same family, and some continuations with extra
priority claims in a different one. The index says "family as grouped
by Google Patents" and does not claim a DOCDB or INPADOC family.
Espacenet's own family view can be reached through each member's
Espacenet link.

### Fields

Top level: `schema_version: 1`, `retrieved` (the date the records were
fetched) and `families` (a list, sorted by priority date).

Family:

| Key | Content |
|---|---|
| `id` | `GP` + Google Patents family ID |
| `family` | `source: Google Patents family ID`, `google_family_id` |
| `representative` | publication number whose record page was fetched (usually the one the docs cite, or the US grant) |
| `title` | title of the representative as shown |
| `assignees` | `original` and `current` lists as shown by Google Patents (its caveat applies: the lists "may be inaccurate") |
| `inventors` | as shown |
| `dates` | `priority` (earliest priority as shown), `filing` and `grant` of the representative (`grant: null` for an application) |
| `legal_status` | `status` of the representative as shown (IFI Claims via Google Patents: `Active`, `Expired - Lifetime`, `Expired - Fee Related`, `Abandoned`, `Granted` for a published application whose patent issued, …) and its `source` |
| `expiry` | `date`, `estimated: true`, `basis` (see below) |
| `expired` | `true`, `false` or `unknown` |
| `members` | list (below) |
| `relevance` | list of `{target, relation, reason}` |
| `inventory_keys` | keys in `docs/references/public-sources.md` (`PAT-…`) for a family the docs cite |
| `discovery`, `discovery_note` | how the family was found (below) |
| `verified` | date and the record page fetched |
| `notes` | optional list of plain-language caveats |

Member:

| Key | Content |
|---|---|
| `number`, `country`, `kind` | publication number with kind code, e.g. `CN101606236B`, `CN`, `B` |
| `document_type` | `granted-patent`, `application`, `international-application`, `search-report`, `utility-model`, `translation-of-granted-patent`, `reexamination-certificate`, `design`, `other` (derived from country and kind code; US kind `A` before 2001 is a grant, `B1`/`B2` before 2001 a reexamination certificate) |
| `publication_date` | as shown |
| `status` | as shown on the member's own record page, or `null` when that page was not fetched |
| `title`, `application_number`, `filing_date` | from the member's record page, when fetched (titles of non-English documents are Google's English rendering) |
| `expiry` | for a fetched grant: Google Patents' "Adjusted expiration" or "Anticipated expiration" date, `estimated: true`, `basis` |
| `links` | `espacenet: https://worldwide.espacenet.com/patent/search?q=pn%3D<number>` and `google_patents: https://patents.google.com/patent/<number>/en`; optional further links on official databases (WIPO Patentscope, USPTO, EPO Register, J-PlatPat, CNIPA, KIPRIS, TIPO, DPMA, UK IPO, INPI) |
| `verified` | `<date> Google Patents record page fetched`, or `<date> listed in the Google Patents family table of <representative> (record page not fetched)` |

### Verification levels

* Every family's representative record page is fetched; its number,
  title and assignee are taken from that page.
* A member is either fetched (its own record page confirms number,
  status and dates) or listed (it appears in the fetched family table
  of the representative). The member's `verified` field says which.
* Members of families whose earliest priority is on or after
  1999-05-29 (so that a US term adjustment or an unexpired term is
  possible) are fetched; older families' members may be listed only,
  because every possible term has ended (see the bound below).
* **Exception, recorded 2026-09-19 (round-3 verification finding H2):**
  the "13 named-missing families" and "SkyWater/salicide" discovery
  batches left 59 members of 8 post-1999-05-29 families listed only, a
  time-budgeted departure from the rule above (large continuation
  chains' non-US siblings, fetched for the representative's own family
  table but not individually). This is not silent: each such member's
  `status` is `null` and its `verified` field says so, and — because the
  rule above was not followed — its term is **not** assumed ended;
  instead it is bounded by rule 3 below (earliest family priority + 21
  years) like any other listed-only member, whether or not that leaves
  the family shown expired. 6 of the 8 families are *not* shown expired
  on this basis. The landing page states the split (members fetched vs.
  listed, and of the listed, how many sit in an already-expired family
  vs. a family bounded only by rule 3) instead of asserting that every
  possible term has ended, which would be true only of the pre-1999-05-29
  members the rule above already treats as listed-only for that reason.

### Status and expiry rules

Nothing in the index is a legal opinion. Every expiry is marked
`estimated: true` and carries its basis. The page text must say that
statuses and dates are as shown by the public databases on the
retrieval date and that maintenance-fee lapses, terminal disclaimers,
term extensions, oppositions, reissues and national validations of
European patents are not fully captured.

Per member:

1. A fetched grant takes Google Patents' "Adjusted expiration"
   (includes US patent term adjustment) or "Anticipated expiration";
   a status of `Expired - Lifetime`, `Expired - Fee Related`,
   `Abandoned` or `Ceased` marks it ended whatever the date.
2. A fetched application with no expiry event is ended if it is shown
   as abandoned, withdrawn or ceased, or if 20 years from its filing
   date have passed. One shown as `Granted` is covered by its patent,
   which is a member of the same family, and has no term of its own.
   An application still pending is bounded by 20 years from the
   earliest non-provisional filing date recorded anywhere in its own
   family, not necessarily its own filing date: a divisional or
   continuation is deemed filed on the original application's filing
   date for term purposes. For a Japanese divisional this is Patent
   Act (Act No. 121 of 1959) Art. 44(2), "a new patent application is
   deemed to have been filed at the time of filing of the original
   patent application", read with Art. 67(1), "the term of a patent
   ends 20 years after the filing date of the patent application"
   (English translation, Japanese Law Translation database, Ministry
   of Justice, `https://www.japaneselawtranslation.go.jp/en/laws/view/4097`,
   retrieved 2026-09-18); a US continuation's term is likewise measured
   from the earliest non-provisional US filing in its chain (35 U.S.C.
   154(a)(2)). Using the family's earliest recorded member filing date
   is therefore the generically correct bound, not the member's own
   filing date; if that bound is already past, the family is bounded
   ended even though the application itself is shown pending.
3. A listed-only member is bounded by the family's earliest priority
   date + 21 years (12-month priority period + 20-year term); for a US
   grant on an application filed before 1995-06-08 the bound is the
   later of that and grant date + 17 years. A US member with priority
   on or after 1999-05-29 is not bounded without its record (term
   adjustment), and stays `unknown`.
4. A reexamination certificate has no term of its own.

Per family:

* `expired: true` when every member is ended by these rules; `expiry.date`
  is the latest member estimate.
* `expired: false` when a member is shown as `Active` and its estimated
  expiry is after today; `expiry.date` is the latest such estimate.
* `expired: unknown` otherwise; the basis names the members that could
  not be bounded. Pages treat `unknown` like `false` (hidden).

The checker re-evaluates `expired` against today's date, so a family
whose estimated expiry passes is flagged until the dataset is refreshed.

### Relevance

Each family links to one or more docs labels with a relation:

* `cited-on-page` — the page with that label cites a member (the checker
  confirms the page mentions a member number). Reason: "Cited on this
  page as PAT-…; the inventory describes it as: …".
* `same-lineage-assignee` — the original assignee is in the process
  lineage: Cypress Semiconductor (SkyWater's Form S-1, inventory key
  SEC-01, says the fab "was owned and operated by Cypress Semiconductor
  Corporation … as a captive manufacturing facility for 20 years" and
  that S130 base design IP originated from Cypress, now Infineon),
  SkyWater Technology, or Infineon Technologies for patents that came
  from Cypress. The reason names the module and says that the patent is
  not evidence that the technique is used in SKY130.
* `technique-class` — the patent describes the class of technique a page
  covers, without a citation on that page.

Reasons are one sentence, never say or imply that SkyWater uses,
licenses or practises a patent unless a public source says so (the
checker rejects "SkyWater uses", "used at SkyWater" and the like), and
obey the common rules in `agent-briefs.md` (step names and codes are
not evidence).

### Discovery methods

* `cited-in-docs` — the patent is cited on a page and has a `PAT-…`
  inventory entry (the seed set).
* `assignee-search` — found by a Google Patents search restricted to an
  assignee (Cypress Semiconductor, SkyWater Technology, Infineon
  Technologies) and a process-module keyword, then fetched and read.
* `family-resolution` — reached through a seed's family table.
* `cited-by-seed`, `citing-seed` — in a seed record's citation tables
  (cited by a seed, or citing one), kept only where the patent concerns
  the same module.
* `continuation-search` — a later continuation or divisional of a lineage
  estate already in the index, found by a search targeted at that specific
  estate (by inventor name, title phrase, or assignee + priority-date
  window) rather than by following the seed's own family/citation tables,
  because Google Patents routinely places such a continuation in a
  *different* family from its parent (see "Known blind spot" below). Added
  2026-09-19 per this section's own instruction to the agent who closes
  it, once actually used (four families below: `GP49580623`,
  `GP49580624`, `GP48743295` and `GP46465479`).

A `discovery_note` records the searches (assignee, query, date limit,
retrieval date) and the seed records through which the family was
reached.

Search result lists are used only to find candidates; nothing is
recorded from a result list without fetching the record page.

**Known blind spot (round-1 review, coordinator note 2026-09-18):**
`family-resolution`/`cited-by-seed`/`citing-seed` only reach patents
Google groups into the *same* family as a seed. A later continuation or
divisional out of the same original filing is routinely placed by Google
in a *different* family from its parent (three confirmed examples: a
granted continuation of the `GP40071593` estate, a continuation of the
2007 Cypress ONO estate, and a Spansion continuation), so these methods
systematically miss an estate's later continuations even when its
original filing is in the index. Closing this gap needs a search *per
lineage estate* — by inventor name, by title phrase, or by assignee plus
a priority-date window — not just by following family/citation links
from the seeds already held. **Done, 2026-09-19 (round-3, L2):** this
is now the `continuation-search` discovery method above, used for four
families (`GP49580623`, `GP49580624`, `GP48743295`, `GP46465479`). The
gap is not closed everywhere, only wherever a `continuation-search` has
actually been run against a specific lineage estate.

## Page set (to be generated)

All under `docs/references/patents/`, linked from the references index.

1. `index.md` — landing page: scope, how families and members are
   counted, the status and expiry caveats, the relation legend, counts
   (families, members, by status), and links to the grouped pages.
2. `families.md` — the canonical entry for every family, in priority
   order, each under a label `patent-gp<family id>` (lower case). Other
   pages link to these entries instead of repeating them, so each entry
   has one place to be reviewed.
3. `by-module.md` — grouped by process module, in process order:
   substrate, isolation (STI), wells and threshold adjust, SONOS/ONO,
   gate oxides, poly and resistors, LDD/halo and spacers, source/drain
   and anneal, local interconnect and contacts, tungsten plugs and
   metallisation, MiM capacitors, passivation, fuses and pads, ReRAM,
   equipment and metrology, materials. A family appears under every
   module its relevance targets map to (step labels map to modules
   through the step's category and the overview's module table;
   machine and material labels map to "equipment" and "materials").
4. `by-assignee.md` — grouped by original assignee (normalised names,
   with the current assignee shown), Cypress, SkyWater and Infineon
   first.
5. `by-jurisdiction.md` — one table per country or office (US, EP, WO,
   JP, CN, KR, TW, DE, GB, FR, others), listing member publications and
   their family; plus a family-size table (members per family).
6. `by-date.md` — by decade of priority date, and a status section:
   expired, in force, unknown, with estimated expiry years.

### Hiding patents that have not expired

The build already loads `sphinx_design` (`docs/conf.py` and
`pyproject.toml`), so no new dependency is needed. An entry whose family
has `expired: false` or `unknown` is written as a collapsed dropdown
whose title shows only the number and status:

````markdown
:::{dropdown} US 8,093,128 B2 — shown as in force; estimated expiry 2028-05-22
:name: patent-gp40072804

(entry body: title, assignees, inventors, dates, members table, relevance)
:::
````

Expired families are shown open. The `{dropdown}` directive keeps MyST
cross-references working inside the body and renders as a
`<details>` element in HTML. Raw HTML `<details>` blocks are the
fallback if `sphinx_design` is removed, but MyST does not parse
Markdown inside raw HTML, so references in the body would be lost.
Grouped pages list non-expired families by number and status only,
linking to the collapsed entry (round-1 review finding M2: this must
hold on every grouped page, `by-jurisdiction.md` included, which
originally exposed a collapsed family's full member list — fixed by
having it contribute only the representative's own row for a collapsed
family, like every other grouped page).

L2 (round-1 review; agreed by the coordinator 2026-09-18, the estimated
expiry being part of the status): the
*collapsed dropdown's own title* (on `families.md`, the one place a
reader can open to see the rest) additionally names the estimated expiry
date, as the example above shows — this is deliberately more than
"number and status" so a reader scanning the closed list on
`families.md` can see roughly how long a family might run without
opening it, while every *other* page still shows only the representative
number and status word for a collapsed family, with no date, matching
the "grouped pages … only" wording above.

### Links inside entries

Entries are data listings. Each member's Espacenet and Google Patents
links are written as autolinks in the member table rather than as
footnotes. The citation style (`docs/plans/citation-style.md`) is
written for prose pages; a short exception for generated index pages
under `docs/references/papers/` and `docs/references/patents/` (no
footnotes, no reading-tier lists) is recorded in
`docs/plans/citation-style.md`'s "Exception: generated index pages"
(round-1 review finding L11, 2026-09-18) rather than left as an
unrecorded proposal — this was already `tools/check_refs.py`'s de-facto
behaviour (neither directory is in its target list), so nothing in the
checker changed.

## Generator and checks

* `tools/gen_patents.py` (to be written) reads `data/patents.yaml` and
  writes the six pages deterministically (stable sort orders, no dates
  other than those in the data, `retrieved` shown on the landing page).
  A `--check` option exits non-zero if the pages on disk differ from
  what the generator would write, so hand edits are caught.
* `tools/check_patents.py` (this branch) validates the dataset: schema
  and types, unique ids and publication numbers, ISO dates and their
  order, link shapes, `expired` against today, docs labels, inventory
  keys and the relevance wording. It is a PEP 723 script declaring
  `pyyaml` as its only dependency, so `uv run tools/check_patents.py`
  runs it in its own environment without changing `pyproject.toml`;
  `gen_patents.py` would do the same.
* The Sphinx `-W` build then checks every `{ref}` in the pages.
* Refreshing: re-fetch the record pages, rebuild the dataset keeping the
  curated fields (`relevance`, `discovery`, `notes`), rerun both
  scripts, and review status changes in the diff.

## Fetching

Record pages are fetched from Google Patents with the user agent
`sky130-process-tech docs checker`, no account or key, at most one
request every few seconds. Google Patents rate-limits bursts (HTTP 503
with an "unusual traffic" page); a refresh must pace itself and resume
from a local cache. Espacenet's web interface is script-driven and its
data service (OPS) needs registration, so Espacenet links are recorded
but not fetched; WIPO Patentscope pages can be fetched without an
account and are the second source for WO members.

### PPUBS fallback (added 2026-09-19, round 3 part 2)

Google Patents has been unreachable from this environment across
several rounds (IP-level "unusual traffic" bot-check on the bare
domain root, not a per-endpoint rate limit; see
`docs/plans/progress-index-patents.md` round 2's "H1" section and
`tmp/patent-cache/.blocked`). USPTO Patent Public Search (PPUBS), a
different, keyless USPTO service, stays reachable
(`tmp/verify-index-patents-coverage.md` section 7 documents its session
and search endpoints). A family discovered and built from PPUBS data
while Google stays blocked is recorded honestly rather than
misrepresented as Google-verified:

* `family.source` is the literal string `"USPTO Patent Public Search
  familyIdentifierCur (Google Patents unreachable)"` instead of
  `"Google Patents family ID"`; `id` still uses PPUBS's own
  `familyIdentifierCur` as the numeric part (`tools/check_patents.py`'s
  `FAMILY_SOURCES` accepts either string). The round-3 review confirmed
  this identifier equals the Google Patents family ID in all 16 families
  it independently cross-checked, so treating it as the same numbering
  space is a checked, not merely assumed, equivalence — but a family
  built this way has never had its own Google Patents page fetched, and
  says so.
* PPUBS gives no legal status, no adjusted-expiration date and no
  distinction between the assignee "as originally filed" and "as
  currently recorded" (design's `assignees.original`/`current`): a
  PPUBS-sourced family records the single `assigneeName` list PPUBS
  gives in both fields, with a note saying so, and `legal_status.status`
  and every member's own `status` are `null`, with `legal_status.source`
  naming PPUBS and stating that legal status was not determined.
* Without a legal-status signal, `expired`/`expiry` are computed purely
  from the same term-arithmetic bounds the design already uses for a
  listed-only member (`member_end_bound`/`family_max_estimate` in
  `tools/check_patents.py`, unchanged): a family whose bound has already
  passed with no possibility of a term adjustment (earliest priority
  before 1999-05-29, per the existing verification-level rule) is
  `expired: true`; a family whose bound has not passed, or could have
  been extended by a US patent term adjustment the record does not show,
  is `false` or `unknown` and stays collapsed. This is the fixer brief's
  own instruction: "treat its status conservatively (not certainly
  expired -> collapsed) unless the US term arithmetic alone proves
  expiry".
* Only the members PPUBS's own search actually returned are recorded
  (normally just the single US publication that matched the discovery
  query); the family is not claimed complete. A note says so and that
  non-US members, and any other US member of the same family PPUBS did
  not surface, were not searched for.
* `discovery` stays `assignee-search` (the method category is the same,
  an assignee-restricted search read and verified before being
  recorded); the `discovery_note` and a family `notes` entry name PPUBS
  specifically, the query used, and the Google-unreachable circumstance.

## Open questions

* Whether the family unit should switch to DOCDB simple families when a
  keyless public source for them is available.
* Whether patents assigned to Weebit Nano (the ReRAM offered in S130,
  per SkyWater's press release SKW-04) belong in scope; the first phase
  limits new discovery to Cypress, SkyWater and Infineon.
* Normalisation of assignee names across mergers (Cypress, Spansion,
  Longitude Flash Memory Solutions, Monterey Research, Infineon
  Technologies LLC) for the by-assignee page.
