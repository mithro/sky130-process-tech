(step-042)=
# Step 042 — ONOME: ONO mask etch

| | |
|---|---|
| **Step number** | 42 of 171[^steps-sheet] |
| **Step code** | `ONOME` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | {term}`FEOL` — SONOS and gate dielectrics |
| **Previous step** | {ref}`ONOM <step-041>` |
| **Next step** | {ref}`GOX100 <step-043>` |

## What this step is

`ONOME` etches the oxide–nitride–oxide stack away from everywhere the
{ref}`ONOM <step-041>` resist does not cover — that is, from every
logic, 5 V and high-voltage transistor, from the select transistors of
the memory cells and from the field — leaving the {term}`ONO` only as
islands over the {term}`SONOS` memory transistors. It is the step that
separates the memory from the logic: after it, the logic silicon can
be cleaned and oxidised to make ordinary gate oxides at
{ref}`GOX100 <step-043>` and {ref}`LVGOX <step-047>`, while the
islands keep their charge-trapping dielectric.

Precisely: the {term}`blocking oxide` (and any sacrificial cap) and the
nitride or {term}`oxynitride` trapping layer are removed by a plasma etch that
stops on the underlying oxide — we infer the pad oxide from
{ref}`BOX <step-002>`, still present outside the tunnel
windows — and the last oxide is then cleared, either here or at the
gate-oxide pre-clean, by a wet etch. The Cypress integration patent
describes exactly this two-stage approach, and the other Cypress flow
the same patterning; both patents are shown as in force and their
wording is in the collapsed note below.

:::{dropdown} From patents shown as in force (US 8,093,128, estimated expiry 2028-10-22; US 8,796,098, estimated expiry 2034-02-26) — open to read
The Cypress integration patent: "a combination of dry and wet etch is
performed to achieve a good stack sidewall profile. In one such
embodiment, an inorganic spin-on anti-reflective coating (ARC), the
blocking layer 304C, and the dielectric layers 304A and 304B are dry
etched, with the dry etch process stopping on the sacrificial dielectric
layer 303. In a subsequent wet etch operation, an etchant, such as BOE,
is employed to clear sacrificial dielectric layer 303."[^pat-03] In the
other Cypress flow the "sacrificial oxide, cap layer 232, and the
charge-trapping layer 230" are "etched or patterned to form a gate stack
236 overlying the channel 224 of the NVM transistor and to remove the
sacrificial oxide, cap layer, and the charge trapping layers 230 from
the second region 208".[^pat-04]
:::

This reference treats the resist strip and the pre-gate-oxide clean
as part of this step; they could equally belong to the next,
{ref}`GOX100 <step-043>`.

## Step category

`ONOME` is an {ref}`Etch <category-etch>` step of the *thin-film stack
etch* type: a nitride etch with an oxide etch above it and a very thin
oxide stop below it, on the Lam 9400 / DPS "poly/nitride" class of tool
(the assignment is inferred — see below). Its distinctive difficulty is
the stop layer: the oxide beneath the nitride — the pad oxide, we infer,
only tens of nanometres thick in the Cypress patent (collapsed note
below this section) — and the silicon under it will become the channel
of every logic transistor. The etch is therefore run like a
{term}`spacer` etch — a nitride etch with "selectivity to oxide" that
must "stop on a thin oxide without trenching the silicon"
({ref}`category-etch`) — rather than like a {term}`hard-mask <hard mask>` open.

:::{dropdown} From a patent shown as in force (US 8,796,098; estimated expiry 2034-02-26) — open to read
The pad oxide beneath the nitride is 10–20 nm in the Cypress
patent.[^pat-04]
:::

## Why this step exists

The reasons are those of {ref}`ONOM <step-041>` seen from the etch
side:

* **Logic transistors must not have a charge-trapping dielectric.**
  Nitride under a gate traps charge and shifts thresholds; the ONO
  must be gone before the logic gate oxides are grown.
* **Gate oxide must grow on silicon.** Thermal oxidation at
  {ref}`GOX100 <step-043>` needs bare silicon; the nitride is an
  oxidation mask (it is the {term}`LOCOS` mask material), so any
  residue would leave an unoxidised patch — a gate-oxide pinhole.
* **The silicon must not be damaged.** The plasma must stop before it
  reaches the channel silicon; ion bombardment leaves "a few
  nanometres of damaged, sometimes amorphised silicon" that "the next
  oxidation or clean must remove" ({ref}`category-etch`). Landing on
  the oxide and finishing wet is how the damage is kept off the
  channel.
* **The ONO edge must be clean.** The island sidewall is the boundary
  along which the logic gate oxide will later grow; the sidewall
  profile the Cypress patent aims at (the collapsed note above) avoids
  nitride feet that would leave stringers and re-entrant profiles that
  would trap resist.

Without `ONOME`, there would be no logic transistors in the ordinary
sense — every gate would sit on ONO.

## How it is typically performed

An industry-generic ONO stack etch for a 200 mm, 130 nm-era embedded
memory (SKY130's recipe is not public):

1. **{term}`ARC` open (if used).** If the ONO mask carries an inorganic or
   organic ARC, it is opened first in the same chamber
   ({ref}`TUNARCE <step-036>` describes the organic case; how Cypress
   removes its inorganic spin-on ARC is in the collapsed note above).
2. **Top oxide.** The blocking oxide and any sacrificial cap — the
   Cypress thicknesses are in the collapsed note below this list — are
   opened in a fluorocarbon plasma (CF₄/CHF₃ with O₂ or Ar) — the
   chemistry that "etches oxide as SiF₄ only under ion bombardment"
   ({ref}`category-etch`, citing Flamm and Donnelly[^flamm-1981]).
3. **Nitride.** The trapping layer — the two Cypress ranges are in the
   same note — is etched in CF₄/O₂,
   CHF₃/O₂ or SF₆-based chemistry tuned for {term}`selectivity` to the oxide
   below; a 1997 ASMC paper reports a nitride spacer etch "with high
   selectivity to oxide" of the kind required.[^regis-1997] {term}`Endpoint <endpoint>`
   is by optical emission — "a strong peak at 387 nm indicates that
   CN is present in the plasma, usually indicating that nitride is
   being etched"[^pat-cn-tel] — followed by a short {term}`over-etch` that
   lands on the oxide. Because the nitride is only a few
   nanometres thick, the endpoint signal is brief and the over-etch
   is timed.
4. **Resist strip.** Oxygen-plasma {term}`ash` and a wet strip
   ({ref}`category-strip`); the resist has seen a fluorocarbon plasma
   and carries polymer residue that the wet step removes.
5. **Bottom oxide.** The remaining (inferred) pad oxide (plus the
   fraction of a nanometre that the tunnel oxidation added[^deal-1965])
   is removed in {term}`BOE` or dilute HF — the etchant the Cypress
   patent names (collapsed note below this list) — exposing the logic
   silicon for gate oxidation. Whether this happens here or as the
   {ref}`GOX100 <step-043>` pre-clean is not stated publicly; the
   Cypress flows differ on it (see {ref}`GOX100 <step-043>`). One of
   them warns about what an HF-based pre-clean would do to an exposed
   stack, and the other protects the blocking oxide with a sacrificial
   cap; both passages are in that note.
6. **All-wet alternative.** The stack could in principle be removed
   entirely wet — BOE for the top oxide, hot phosphoric acid for the
   nitride, whose selectivity to oxide was established by van Gelder
   and Hauser,[^vgh-1967] and BOE again — but hot H₃PO₄ destroys
   photoresist, so this route needs a hard mask; the Cypress patents
   describe the dry-then-wet route.
7. **Inspection.** Patterned-wafer inspection for nitride residue and
   stringers at island edges; ellipsometry on monitor wafers.

:::{dropdown} From patents shown as in force (US 2009/0179253, estimated expiry 2027-06-17; US 8,093,128, estimated expiry 2028-10-22; US 8,796,098, estimated expiry 2034-02-26) — open to read
The blocking oxide is 3–5 nm and the trapping layer 9–11 nm in one
Cypress patent;[^pat-03] another gives the trapping layer as
70–150 Å,[^pat-02] and the sacrificial cap is 2–4 nm.[^pat-04] The
bottom oxide goes in "an etchant, such as BOE, … employed to clear
sacrificial dielectric layer 303". The same patent warns that once the
stack is exposed, "Conventional HF-based gate insulator pre-cleans will
etch or otherwise degrade the quality of the ONO charge trapping
dielectric stack 306, particularly when the stack includes a CVD formed
blocking layer", which is why its pre-clean is "substantially free of
HF";[^pat-03] the other protects the blocking oxide with a sacrificial
cap that the BOE removes.[^pat-04]
:::

## Machines typically used

* **{ref}`Dielectric/nitride plasma etcher <machine-plasma-etcher-dielectric>`**, 200 mm: Lam {term}`TCP` 9400
  series, Applied Materials DPS Centura
  ({ref}`silicon and polysilicon etcher class <machine-plasma-etcher-silicon>`);
  or a **{ref}`dielectric etcher <machine-plasma-etcher-dielectric>`** (Lam
  Exelan, Applied MxP) for a fluorocarbon-only recipe
  ({ref}`category-etch`).
* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`** and **{ref}`wet bench <machine-wet-bench>`** for the strip and the
  bottom-oxide clear.
* **Optical emission endpoint**; **{ref}`patterned-wafer inspection <machine-defect-inspection>`**.

## Machines likely used at SkyWater

* **Lam 9400 TCP.** SkyWater lists "Lam 9400 TCP, poly/nitride, HBr,
  CF4, SF6, O2"[^skw-01] — a nitride-capable tool with the CF₄/SF₆/O₂
  chemistries of steps 2–3. Strength: **strong** for the tool;
  **inference** for its assignment to `ONOME`. A university
  clean-room describes the 9400 as a TCP etcher "for selective etching
  of silicon and polysilicon" with tetrafluoromethane
  and oxygen in its gas list.[^snf-9400]
* **Applied Materials DPS II** ("HBR, Cl2, NF3, CF4, CHF3, O2 – gate,
  trench, W/WN")[^skw-01] — has CHF₃ for the oxide layers. Strength: strong
  for existence; **medium** for this step, since its CF₄ and CHF₃ etch
  nitride although the entry names no nitride application.
* **Lam 4400** ("HBr, Cl2, C2F6, CF4, SF6, O2").[^skw-01] Strength:
  strong for existence; **weak** for assignment, as the entry names no
  application.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1, phosphoric,
  BOE")[^skw-01] — for the BOE clear (and the phosphoric route, if
  used). Strength: strong for existence.
* **GaSonics PEP / Iridia / Mattson Aspen II** ashers.[^skw-01]
  Strength: strong for existence.

## Resources required

* **{ref}`CF₄ <material-etch-gases>`, CHF₃, SF₆ and {ref}`O₂ <material-process-gases>`** process gases,[^skw-01] with **Ar** or
  **He** as typical diluents; **HBr** if a silicon-selective landing
  step is used.
* **Oxygen/nitrogen/{ref}`forming gas <material-anneal-ambients>`** for the ash; **{term}`SPM`** for the wet
  strip ({ref}`category-strip`; {ref}`wet chemicals <material-wet-chemicals>`).
* **BOE or dilute HF** for the bottom oxide (the collapsed note above);
  **hot phosphoric acid** only for the all-wet alternative.[^vgh-1967]
* **{ref}`DI water <material-ultrapure-water>`, isopropanol, nitrogen**; {ref}`chamber consumables <material-hardware-consumables>`.
* Gas and chemical suppliers named in SkyWater's filings: Air
  Products, Praxair and KMG (2021 S-1); Linde, Airgas and EMD
  (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`ONOM <step-041>` (the resist islands).
* Next: {ref}`GOX100 <step-043>` (first gate oxidation on the cleared
  silicon).
* The stack being removed was formed at {ref}`ONO <step-040>`; the
  same nitride chemistry serves the {term}`STI` hard-mask etch
  {ref}`STINITE <step-005>` and the spacer etch {ref}`SPE <step-077>`.
* The ONO islands are etched again, self-aligned to the gate, at the
  poly etch ({ref}`P1ME <step-062>`).
* Category page: {ref}`Etch <category-etch>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 6,376,262 B1 <patent-gp25360011>` — Method of forming a semiconductor device using double endpoint detection (2001)
* {ref}`US 6,969,689 B1 <patent-gp35405131>` — Method of manufacturing an oxide-nitride-oxide (ONO) dielectric for SONOS-type devices (2002)

:::{dropdown} 3 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 2009/0179253 A1 <patent-gp40849883>` — in force
* {ref}`US 8,093,128 B2 <patent-gp40072804>` — in force
* {ref}`US 8,796,098 B1 <patent-gp51229009>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — Lam 9400 TCP, AMAT DPS II,
  Akrion Gamma, ashers.[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) —
  suppliers.[^sec-01][^sec-02]
* Stanford Nanofabrication Facility, *Lam Research TCP 9400*.[^snf-9400]
* Tokyo Electron, US 6,376,262 — CN emission at 387 nm as the nitride
  etch endpoint.[^pat-cn-tel]

:::{dropdown} From patents shown as in force (US 8,093,128, estimated expiry 2028-10-22; US 8,796,098, estimated expiry 2034-02-26) — open to read
* Koutny et al. (Cypress), US 8,093,128 — the dry-then-wet ONO etch,
  the inorganic ARC, the HF warning and the non-HF pre-clean.[^pat-03]
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — the
  patterned removal of sacrificial oxide, cap and trapping layers, the
  BOE pre-clean and the pad-oxide thickness.[^pat-04]
:::

### High-level understanding

* Wikipedia, *Reactive-ion etching* — plasma etch basics.[^wiki-rie]
* Wikipedia, *Silicon nitride* — nitride as an oxidation mask and its
  etches.[^wiki-sin]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  plasma etching of dielectrics.[^txt-02]

### Deep dive

* Regis et al., ASMC 1997 — reactive-ion etch of a nitride spacer
  with high selectivity to oxide.[^regis-1997]
* van Gelder and Hauser, *J. Electrochem. Soc.* 1967 — phosphoric
  acid etch rates of nitride and oxide.[^vgh-1967]
* Flamm and Donnelly, *Plasma Chem. Plasma Process.* 1981 — the design
  of fluorocarbon plasma etchants.[^flamm-1981]
* Winters and Coburn, *Surf. Sci. Rep.* 1992 — surface-science
  mechanisms of fluorine-based etching.[^winters-1992]
* Coburn and Winters, *J. Appl. Phys.* 1979 — ion- and
  electron-enhanced gas–surface reactions of Si, SiO₂ and Si₃N₄, and
  their implications for plasma etching.[^coburn-1979]
* Nojiri, *Dry Etching Technology for Semiconductors* — endpoint,
  selectivity and stack-etch practice.[^nojiri-2015]
* Kern, *J. Electrochem. Soc.* 1990 — the wet-clean chemistry used
  for the bottom oxide and the pre-gate clean.[^kern-1990]
* Kim et al. (Samsung), VLSI 2003 — patterning of an embedded SONOS
  module in a logic flow.[^pap-03]
* Ramkumar et al. (Cypress), US 6,969,689 — the stack being
  etched.[^pat-01]

## Open questions

* That the oxide under the resist/nitride is the pad oxide from
  {ref}`BOX <step-002>` rather than a later sacrificial oxide is
  inferred; its retention after {ref}`NS19 <step-013>` is not public.
* Whether the nitride is removed dry (as the Cypress patents describe)
  or wet, and on which tool, is inferred.
* Whether the bottom oxide is cleared here or at the
  {ref}`GOX100 <step-043>` pre-clean is not stated publicly.
* Whether an ARC is used on the ONO mask and opened in this etch is
  not public.
* Where the resist is stripped is not stated publicly; this page
  treats the strip as part of this etch.
* Endpoint method, over-etch and the resulting pad-oxide loss are not
  public.

<!-- footnotes -->

[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
    Shown as in force; estimated expiry 2028-10-22 (estimate from public
    records, not legal advice).
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
    Shown as in force; estimated expiry 2034-02-26 (estimate from public
    records, not legal advice).
[^flamm-1981]: D. L. Flamm and V. M. Donnelly, "The design of plasma
    etchants", *Plasma Chemistry and Plasma Processing* **1**(4),
    317–363 (1981). <https://doi.org/10.1007/BF00565992>
[^regis-1997]: J. M. Regis, A. M. Joshi, T. Lill and M. Yu, "Reactive
    ion etch of silicon nitride spacer with high selectivity to oxide",
    *1997 IEEE/SEMI Advanced Semiconductor Manufacturing Conference and
    Workshop (ASMC 97) Proceedings*, pp. 252–256.
    <https://doi.org/10.1109/ASMC.1997.630744>
[^pat-cn-tel]: Tokyo Electron Ltd., *Method of forming a semiconductor
    device using double endpoint detection*, US 6,376,262 B1, granted
    2002-04-23. <https://patents.google.com/patent/US6376262B1/en>
[^vgh-1967]: W. van Gelder and V. E. Hauser, "The Etching of Silicon
    Nitride in Phosphoric Acid with Silicon Dioxide as a Mask", *Journal
    of The Electrochemical Society* **114**(8), 869 (1967).
    <https://doi.org/10.1149/1.2426757>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^snf-9400]: Stanford Nanofabrication Facility, *Lam Research TCP 9400
    Poly Etcher (lampoly)*, equipment page.
    <https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^wiki-sin]: Wikipedia, *Silicon nitride*.
    <https://en.wikipedia.org/wiki/Silicon_nitride>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^winters-1992]: H. F. Winters and J. W. Coburn, "Surface science
    aspects of etching reactions", *Surface Science Reports*
    **14**(4–6), 162–269 (1992).
    <https://doi.org/10.1016/0167-5729(92)90009-Z>
[^coburn-1979]: J. W. Coburn and H. F. Winters, "Ion- and
    electron-assisted gas-surface chemistry — An important effect in
    plasma etching", *Journal of Applied Physics* **50**(5), 3189–3196
    (1979). <https://doi.org/10.1063/1.326355>
[^nojiri-2015]: K. Nojiri, *Dry Etching Technology for Semiconductors*,
    Springer, 2015. <https://doi.org/10.1007/978-3-319-10295-5>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^pap-03]: J.-H. Kim, I. W. Cho, G. J. Bae, S. S. Kim, K. C. Kim,
    S. H. Kim, K. W. Koh, N. I. Lee, H.-K. Kang, K.-P. Suh, S. T. Kang,
    M. K. Seo, S. H. Lee, M. C. Kim and I. S. Park (Samsung), "Highly
    manufacturable SONOS non-volatile memory for the embedded SoC
    solution", *2003 Symposium on VLSI Technology, Digest of Technical
    Papers*, pp. 31–32. <https://doi.org/10.1109/VLSIT.2003.1221071>
[^pat-01]: K. Ramkumar, M. Rathor, B. Parameshwaran and L. Lancaster
    (Cypress Semiconductor), *Method of manufacturing an
    oxide-nitride-oxide (ONO) dielectric for SONOS-type devices*,
    US 6,969,689 B1, granted 2005-11-29.
    <https://patents.google.com/patent/US6969689B1/en>
[^pat-02]: S. Levy, K. Ramkumar, F. Jenne and S. Geha (Cypress
    Semiconductor), *Oxide-nitride-oxide stack having multiple
    oxynitride layers*, US 2009/0179253 A1, published 2009-07-16.
    <https://patents.google.com/patent/US20090179253A1/en>
    Shown as in force; estimated expiry 2027-06-17 (estimate from public
    records, not legal advice).
[^deal-1965]: B. E. Deal and A. S. Grove, "General Relationship
    for the Thermal Oxidation of Silicon", *Journal of Applied Physics*
    **36**(12), 3770–3778 (1965). <https://doi.org/10.1063/1.1713945>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
