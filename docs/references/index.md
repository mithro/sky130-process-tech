(references-index)=
# References

Every source cited anywhere in this reference is publicly available and
is listed, with notes on what it contains, in the
{doc}`public sources inventory <public-sources>`. This page explains how
the citations are organised.

## How citations work

Pages cite sources with Markdown footnotes. A footnote label is the
inventory key of the source in lower case: the inventory entry
**PDK-04** (the PDK's process stack diagram) is cited as `[^pdk-04]`,
and **STEPS-SHEET** (the public *S8 / SKY130 Process Steps* sheet,
the source of the 171-step list) as `[^steps-sheet]`. Each page repeats
the full citation of every source it uses in its own footnotes, so a
page can be read on its own, and the inventory holds exactly one entry
per key. The checker `tools/check_refs.py` fails the build if a page
uses a label that has no inventory entry, defines a footnote it never
cites, or cites one it never defines.

Where a page draws on a web page that changes or expires (a capability
list, a job listing, a dealer listing), the footnote gives the date it
was retrieved. Search-engine snippets and pages that could not be
retrieved are not cited.

## Reading tiers

Every step, category and index page ends with three annotated reading
lists:

* **Cross-check** — primary public sources that can verify a specific
  claim: the SkyWater PDK documentation, SkyWater's own statements and
  capability list, regulatory filings, Cypress qualification reports,
  patents and vendor data.
* **High-level understanding** — introductory material: encyclopaedia
  articles, textbooks, trade press and talks.
* **Deep dive** — papers, theses, roadmaps and conference proceedings.
  Step pages list at least eight, category and index pages at least
  twelve.

## How the inventory is organised

The {doc}`inventory <public-sources>` is grouped by where a source comes
from:

1. SkyWater open PDK documentation.
2. Google and SkyWater announcements and talks about the open PDK, and
   the public process-steps sheet.
3. SkyWater Technology corporate sources: website pages, press
   releases, SEC filings and government sources about the Minnesota fab.
4. SkyWater job listings that name tools.
5. Cypress Semiconductor, "Fab 4" and the S8 process: fab history,
   qualification reports and notices, Cypress patents and SONOS papers.
6. Trade press and analyst coverage of the Bloomington fab.
7. Teardowns, die photographs and cross-sections of SKY130 silicon.
8. General 130 nm-era process references: textbooks, ITRS roadmaps,
   review papers, encyclopaedia articles, and the papers, patents and
   vendor pages gathered module by module as the step pages were
   written (sections 8.5 to 8.18: 8.17 covers the sky130B ReRAM
   module, 8.18 the SkyWater PDK raw measurement data and test tile).
9. Evidence about specific tools at SkyWater, weighed by strength.
10. Gaps and open questions: what the public record does not say.

## Where inference begins

Much of how SKY130 is made is not published. Pages say so, and mark
their own reasoning with "we infer", "(inference)" or "on our reading",
giving the public evidence the inference rests on. For tools, the
evidence scale is **strong** (a SkyWater or tool-vendor statement),
**medium** (a SkyWater job listing or an interview with a named SkyWater
employee) and **weak** (indirect evidence), with the assignment of a
tool to a particular step graded separately; the
{ref}`machines index <machines-index>` explains the wording in full.

The {ref}`academic paper index <papers-index>` catalogues papers about
SKY130, devices and circuits made on it, and its Cypress lineage; a paper
enters the inventory only when a page cites it.

```{toctree}
:maxdepth: 1

public-sources
papers/index
```
