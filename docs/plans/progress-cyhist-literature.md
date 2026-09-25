# Progress: cyhist-literature (technical-literature evidence for pre-S8 Cypress process technologies)

Branch `topic/cyhist-literature`, worktree `.worktrees/cyhist-literature`.
Evidence file: `data/history/literature.yaml`, 30 records, each with a
`cache:` path and `sha256` under `tmp/cyhist-cache/` (main checkout) and at
least one verbatim quote. `uv run tools/check_history_quotes.py` (which
already checks all of `data/history/*.yaml`, literature.yaml included)
reports 0 problems and 0 records with no cached text, across 374 quotes in
5 files.

## Records kept (30)

**Web / app-note / teardown (4)**
- `web-techinsights-cy8ctma301e-pna` -- TechInsights product-page title
  for the CY8CTMA301EES-3 130 nm touchscreen controller.
- `teardown-siliconpr0n-cy8c4245axi` -- siliconpr0n SEM teardown of a PSoC
  4200 (CY8C4245AXI): S8, 130 nm, code S8DIN-5R, dual gate oxide, Fab 4 +
  GSMC.
- `web-design-reuse-innopower-2011` -- Cypress press release: 130 nm and
  65 nm SONOS IP licensed to Innopower/Faraday, Feb 2011.
- `web-semidigest-honeywell-150nm-2005` -- Semiconductor Digest on the
  Honeywell 150 nm rad-hard SOI foundry (Plymouth, MN).

**Papers, Cypress-authored (10)**
- `paper-qiao-1999-sac-018um-sram` -- 0.18 µm SRAM self-aligned-contact
  process (full Crossref abstract).
- `paper-hu-1992-bifamos-eprom` -- BiFAMOS 0.8 µm BiCMOS EPROM cell
  (OpenAlex abstract).
- `paper-isscc1985-cmos-prom` -- 1.2 µm n-well CMOS PROM, ISSCC 1985
  (OpenAlex abstract; earliest Cypress paper found).
- `paper-cicc1994-altera-eprom` -- 0.65 µm double-poly/metal UV EPROM CMOS
  with poly-buffer LOCOS isolation, Cypress + Altera (OpenAlex abstract).
- `paper-kennings-2000-delta39k-cpld` -- Delta39K CPLD architecture
  (OpenAlex abstract).
- `paper-lovett-2001-nonvolatile-hidden-cmos` -- zero-extra-mask
  nonvolatile cell in standard CMOS (OpenAlex abstract).
- `paper-yang-white-2000-sonos-retention` -- SONOS retention at elevated
  temperature (Cypress + Lehigh); title only, no abstract found anywhere.
- `paper-radaelli-2005-150nm-mbu-sram` -- 150 nm SRAM multi-bit-upset
  study (OpenAlex abstract).
- `paper-kitonaki-2006-015um-cmos-ekv3` -- 0.15 µm single-poly,
  buried-channel-PMOS CMOS, compact-model study (OpenAlex abstract, open
  access).
- `paper-fliesler-2008-nvsram-013u-sonos` -- 4 Mb 0.13 µm SONOS NVSRAM,
  Cypress + Simtek (OpenAlex abstract; also indexed in data/papers.yaml).

**Patents (16)**, each newly fetched from its own Google Patents page and
quoted from that page's own abstract (previously title-only):
`pat-us4764248a-locos-1987`, `pat-us5648669a-flash-cell-1995`,
`pat-us5844271a-splitgate-eeprom-1995`, `pat-us6091129a-sti-1996`,
`pat-us6033991a-locos-sti-transition-1997`, `pat-us5914895a-nvsram-1997`,
`pat-us6114724a-nvmemory-selectgate-1998`,
`pat-us6207991b1-integrated-nv-cmos-1998`,
`pat-us6172907b1-sonos-jenne-1999`, `pat-us6525962b1-cpld-nvcell-2000`,
`pat-us6818558b1-sonos-dielectric-2001`,
`pat-us6677213b1-sonos-deuterated-2002`,
`pat-us7371637b2-oxide-nitride-gate-2003`,
`pat-us7592661b1-cmos-hv-transistor-2005`,
`pat-us9583501b1-sonos-mos-simultaneous-2006`,
`pat-us8093128b2-s8-family-2007`. Family, priority date and expiry/status
are repeated from data/patents.yaml unchanged; four of them
(`pat-us6172907b1-sonos-jenne-1999`, `pat-us6525962b1-cpld-nvcell-2000`,
`pat-us7371637b2-oxide-nitride-gate-2003`,
`pat-us7592661b1-cmos-hv-transistor-2005`) now show a determinable
legal-status field on a fresh fetch where data/patents.yaml (verified
2026-09-14) recorded none -- see "Facts for the coordinator" below. The
two patents data/patents.yaml shows in force
(`pat-us9583501b1-sonos-mos-simultaneous-2006`,
`pat-us8093128b2-s8-family-2007`) keep their collapsed-block flag text.

## Records removed as duplicates (12)

| literature.yaml id | existing id |
|---|---|
| `web-chipestimate-sonos-scalable-2008` | `extra.yaml: cyx-chipestimate-sonos-2008` / `cyx-chipestimate-dual-oxide` |
| `web-infineon-sonos-eflash-brief-2018` | `extra.yaml: cyx-infineon-sonos-eflash-brief` |
| `web-infineon-psoc-history-2022` | `extra.yaml: cyx-infineon-psoc-history` |
| `web-eetimes-cypress-grace-2005` | `corporate.yaml: cyhist-corp-pr-2005-grace-deal` |
| `web-edn-honeywell-radhard-2005` | `extra.yaml: cyx-edn-2005-honeywell-soi` |
| `web-eetimes-mosel-vitelic-013um-2000` | `extra.yaml: cyx-eetimes-2000-mosel-vitelic` |
| `web-eetimes-first-035um-sram-1997` | `extra.yaml: cyx-eetimes-1997-first-035um-sram` |
| `appnote-cypress-pin152804-globalwafer` | `extra.yaml: cyx-pin152804-fab4-families` |
| `datasheet-cypress-1988-cmos-databook` | `extra.yaml: cyx-databook-1988` |
| `datasheet-qtp-ram42hha-cy62256a` | `qtp.yaml: qtp-030206` |
| `datasheet-qtp-s4ad5-neutron-gsmc` | `qtp.yaml: qtp-062509` |
| `paper-jin-1999-locos-cop-025um-sram` | `extra.yaml: cyx-jin-1999-locos` |

Four of these twelve (`web-eetimes-cypress-grace-2005`,
`web-edn-honeywell-radhard-2005`, `web-eetimes-mosel-vitelic-013um-2000`,
`web-eetimes-first-035um-sram-1997`) had quotes obtained through an
AI-summarising fetch tool rather than a cached copy; each turned out to
duplicate a source another record already holds with a real cache, so
they were removed as duplicates rather than independently re-verified.

## Records dropped as not verifiable

None. Every record that was not a duplicate could be given a real cached
quote (a fresh Google Patents fetch for every patent, a Crossref or
OpenAlex abstract for every paper still missing one, and the existing
scripted caches already on disk for the remaining web/app-note/teardown
sources).

## Facts for the coordinator

Cache-verified content found in the sources above that the record it
duplicates does not currently quote:

1. The Infineon SONOS eFlash brief (cache `web/infineon-sonos-eflash-brief.txt`,
   held by `extra.yaml: cyx-infineon-sonos-eflash-brief`) also states:
   ">2 billion PSoC units" shipped with SONOS eFlash "over 15 years"; SONOS
   eFlash volume production at the 350 nm node in 2001 and the 130 nm node
   in 2007; and qualification at the 65 nm node in 2012.
2. The Infineon "20 Years of PSoC" page (cache
   `web/infineon-psoc-history-wayback.html.txt`, held by `extra.yaml:
   cyx-infineon-psoc-history`) also states that PSoC 3 formed the basis
   for PSoC 5 (the CY8C5 series, moving to a 32-bit 80 MHz Arm Cortex M3
   core), and that PSoC 3 and PSoC 5 both launched in 2009.
3. The ChipEstimate SONOS article (cache
   `web/chipestimate-sonos-scalable.html.txt`, held by `extra.yaml:
   cyx-chipestimate-sonos-2008` / `cyx-chipestimate-dual-oxide`) also
   states that conventional floating-gate technology was used for
   embedded flash at the 0.25 µm and 0.18 µm nodes before SONOS, and that
   scaling floating-gate down to 130 nm and beyond proved difficult and
   expensive.
4. The 1999 LOCOS/COPs paper abstract (cache
   `web/iop-locos-cop-025um.html.txt`, held by `extra.yaml:
   cyx-jin-1999-locos`) continues, past the sentence already quoted there,
   with: most COPs were found in the narrow active region, and design of
   experiments showed the thickness of pad oxide, nitride and field oxide
   modulates COP density.
5. The Mosel Vitelic EE Times article (cache
   `web/chrome-eetimes-2000-07-07-cypress-mosel-vitelic-013um.txt`, held
   by `extra.yaml: cyx-eetimes-2000-mosel-vitelic`) also states that the
   joint development was expected to extend to 300 mm wafer processing,
   low-k dielectrics, copper interconnects and a follow-on 0.10-micron
   generation.
6. The first-0.35-µm-SRAM EE Times article (cache
   `web/chrome-eetimes-1997-11-19-cypress-first-035um-sram.txt`, held by
   `extra.yaml: cyx-eetimes-1997-first-035um-sram`) also gives product
   detail for the CY7C1021 (1 Mbit, organised 64K by 16, 10 ns access, 300
   µA standby), states the six-transistor cell design was by then used
   for all of Cypress's new SRAMs, and that quarter-micron (0.25 µm)
   production was expected within six to nine months of the article date.
7. Four patents that data/patents.yaml (verified 2026-09-14) records with
   no determinable legal status now show one on a fresh fetch of the same
   Google Patents page (2026-09-25): `US6172907B1`, `US6525962B1` and
   `US7371637B2` each now read "Expired - Lifetime"; `US7592661B1` now
   reads "Active". Each literature.yaml record for these four notes the
   disagreement but keeps data/patents.yaml's own recorded value for its
   claims, per project rule.

## Open questions

- No public source found gives an explicit node, mask count or stackup
  for Cypress's 1.2/0.8/0.65/0.5 µm 1980s-1990s CMOS/BiCMOS generations
  as a group; the individual papers now in literature.yaml give isolated
  node data points (1.2 µm CMOS PROM 1985, 0.65 µm EPROM CMOS 1994, 0.8 µm
  BiFAMOS 1992) but no single source ties these into one generational
  sequence.
- No document was found using the literal string "R42D-5"; the QTP
  records in `qtp.yaml` use "RAM42"/"RAM42HHA" instead, and whether that
  is the same technology as an "R42D-5" is not established there.
- No source distinguishing what "C8" vs. "R8" vs. "L8" each specifically
  cover within the 130 nm generation was found.
- "Ultra37000" was not found in any retrieved source; the closest process
  evidence for a Cypress CPLD of that era is the Delta39K architecture
  paper plus a contemporaneous (2000) dedicated electrically-erasable PLD
  cell patent (`pat-us6525962b1-cpld-nvcell-2000`), neither naming a SONOS
  process.
- `paper-yang-white-2000-sonos-retention` has no abstract available from
  either Crossref or OpenAlex; only its title is verifiable without
  paying for the article.
- A handful of other Cypress-affiliated papers turned up during the
  OpenAlex institution search but were not added as literature.yaml
  records (no clear pre-S8 stackup/node content beyond what the 10
  papers above already give): a 1988 CICC paper on Bi-CMOS technology for
  semi-custom ICs, a 1990 ISCAS overview of BiCMOS technology, a 1990 VMIC
  paper on planarisation for 0.5 µm CMOS/BiCMOS, a 1993 VLSI Symposium
  paper on an 18.4 µm² 6-T SRAM cell, and a 1994 Bipolar Circuits and
  Technology Meeting paper on a 0.5 µm BiCMOS TTL PAL.
