(step-079)=
# Step 079 — NPCME: Nitride poly cut mask etch

| | |
|---|---|
| **Step number** | 79 of 171[^steps-sheet] |
| **Step code** | `NPCME` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | FEOL — extensions, spacers, source/drain |
| **Previous step** | {ref}`NPCM <step-078>` |
| **Next step** | {ref}`SPOX <step-080>` |

## What this step is

`NPCME` etches the {term}`nitride poly cut <nitride cut>`. Through the resist windows printed
at {ref}`NPCM <step-078>`, it removes the dielectric cap standing on
the poly — whatever remains of the {ref}`POC <step-059>` oxide and the
{ref}`GATENIT <step-058>` nitride, about 0.2 µm of it after the spacer
etch on our reading of the PDK's "poly cap after SPE"[^pdk-03] — and
stops on the poly, leaving bare polysilicon exactly "under licon1
areas".[^pdk-06] Inside a window the etch also meets the nitride
spacers on the poly sidewalls and whatever spacer nitride lies on the
field oxide beside them; how much of the spacer it is allowed to take
is a recipe choice discussed below. The resist is stripped and the
wafer cleaned afterwards; this reference treats the strip and clean
as part of this step. The next step is an oxide deposition
({ref}`SPOX <step-080>`).

The structures being opened are of two kinds. The first are the
contact heads of poly interconnect and gate leads, kept at least
0.090 µm from any gate by npc.4.[^pdk-periph] The second are the ends
of the precision resistors, which rpm.5 requires to be enclosed by
`npc` by 0.095 µm[^pdk-periph] and which, on the reading set out on
the {ref}`NPCM <step-078>` page, are doped through this opening by the
P⁺ source/drain implant that follows.

## Step category

`NPCME` is an {ref}`Etch <category-etch>` step of the *dielectric,
fluorine-chemistry* class, masked, with a hard stop on polysilicon.
Its nearest relatives are the spacer etch {ref}`SPE <step-077>` (same
films, no mask, stops on oxide) and the STI hard-mask etch
{ref}`STINITE <step-005>` (masked nitride etch that continues into
silicon). What is specific here is the stop: a nitride-over-oxide
stack must be cleared *completely* — a residue of nitride under a
contact is an open circuit — without etching the doped poly beneath,
and the selectivity that makes a fluorocarbon etch stop on oxide is
of little help, because the last film before the poly is nitride.

## Why this step exists

Everything a poly line will ever connect to passes through this
opening. The local-interconnect contact `licon1` is etched later
({ref}`LICM1E <step-094>`) through the sacrificial PSG and {term}`cap oxide`
({ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`); if the nitride cap
were still under it, the contact etch would have to change chemistry
at the bottom of a 0.17 µm hole[^pdk-periph] and would stop unevenly
on gates, resistor ends and interconnect. Cutting the nitride now, on
a flat, resist-defined pattern, is easier to control and lets the
contact etch stop on a uniform surface. Tang et al. built a
titanium-nitride {term}`local interconnect` at Texas Instruments from the
TiN layer that forms during self-aligned silicidation, patterned to join
gates and junctions;[^tang-1985][^tang-1987] their abstracts do not
describe a nitride cap over poly removed at contact sites, and the
papers' full text was not checked.

The order relative to the source/drain implants is deliberate on our
reading (inference from the PDK rules, {ref}`NPCM <step-078>`): the
opened poly is doped by {ref}`PSDI <step-082>` inside `psdm` and by
{ref}`NSDI <step-086>` inside `nsdm`, which gives the p-type precision
resistors heavily doped contact heads and gives n⁺ interconnect heads
an extra n⁺ dose. A bare-poly surface also receives the
{ref}`SPOX <step-080>` oxide that follows, which protects it through
the implant lithography and acts as the implant screen.

Two failure modes make the recipe demanding. **Incomplete clearing**
leaves nitride stringers at the foot of the spacer, where the cap
nitride and the spacer nitride meet at a re-entrant corner; a contact
that lands on a stringer is high-resistance or open. **Over-etching**
consumes the spacer inside the window, erodes the poly and its doped
surface, and — where the window is close to a gate — thins the cap
whose job is to keep the gate sealed. The npc.4 gate margin of
0.090 µm[^pdk-periph] is, we infer, sized partly to keep the etch's
lateral effects away from the gate edge. Joubert and Bell compared
oxide-hard-mask and resist-mask gate etching, which is the same
resist-on-cap-on-poly system seen from the other side,[^joubert-1997]
and Tuda, Shintani and Tanimura describe removing oxide hard masks and
residues from poly gates selectively.[^tuda-2004]

Without `NPCME` the poly would remain capped and un-contactable; the
resistor ends would keep the light doping of their bodies; and the
{ref}`LICM1E <step-094>` etch would have to open nitride at the
bottom of every poly contact.

## How it is typically performed

An industry-generic nitride/oxide cut etch for a 200 mm, 130 nm-era
fab (SKY130's recipe is not public):

1. **Chamber.** Single-wafer fluorocarbon etcher (TCP/ICP or
   medium-density RIE) with optical emission endpoint and helium
   backside cooling ({ref}`category-etch`).
2. **BARC open.** If an organic BARC was used at {ref}`NPCM <step-078>`
   (inferred there), a short O₂/N₂ or CF₄/O₂ step opens it in the
   windows.
3. **Oxide cap breakthrough.** Where any {ref}`POC <step-059>` oxide
   survives, a CF₄/CHF₃/Ar step removes it; fluorocarbon chemistry
   etches oxide readily under ion bombardment.[^flamm-1981][^winters-1992]
4. **Nitride main etch.** CF₄/O₂ or CHF₃/O₂ with N₂ or Ar at a few
   tens of mTorr and moderate bias — the same family as the spacer
   etch — whose rates and selectivities Kastenmeier et al.
   measured;[^kastenmeier-1996][^kastenmeier-1999] a remote NF₃/Cl₂
   chemistry of the kind Staffa et al. characterised is the
   low-damage alternative.[^staffa-1995] The etch is run to an
   {term}`endpoint` on the 387 nm CN emission — "a strong peak at 387
   nm indicates that CN is present in the plasma, usually indicating
   that nitride is being etched"[^pat-cn-tel] — and, because the
   open area is small, the signal is weak and often supplemented by
   a timed component.
5. **Stop on poly.** Fluorine etches silicon faster than nitride
   unless the chemistry is arranged otherwise — Lee and Chen describe
   the CF₄/O₂ silicon etch[^lee-chen-1983] — so the last part of the
   etch uses a chemistry with selectivity to silicon (high
   carbon-to-fluorine ratio, or O₂-lean, per Kastenmeier
   et al.[^kastenmeier-1999]) and a low bias, and the over-etch is
   kept short. A few nanometres of poly loss and a damaged layer of
   the kind Oehrlein reviewed[^oehrlein-1989] are unavoidable and
   are, we infer, part of why the poly heads are re-doped by the
   source/drain implants.
6. **Loading.** Because only a small fraction of the wafer is open,
   micro-loading and aspect-ratio effects in the 0.27 µm
   windows[^pdk-periph] dominate the uniformity, as Gottscho,
   Jurgensen and Vitkavage analysed.[^gottscho-1992]
7. **Strip and clean.** In-situ O₂ plasma or a downstream asher
   (SkyWater lists GaSonics PEP, Iridia and Mattson Aspen II[^skw-01])
   for the resist, then SPM/SC-1 on a wet bench;[^wiki-rca] we infer
   no HF, because the thin oxide over the source/drain is still needed
   as the implant screen and the PSG/CMP module has not yet begun.
8. **Metrology.** Cross-section SEM of cut windows on monitors for
   residual nitride and spacer erosion; poly loss on test pads; after
   {ref}`LICM1E <step-094>` and {ref}`category-test`, poly contact
   resistance and resistor-head resistance are the electrical
   monitors.

## Machines typically used

* **{ref}`Dielectric/nitride plasma etcher <machine-plasma-etcher-dielectric>`**, 200 mm single-wafer: Lam TCP 9400
  (poly/nitride class[^snf-9400]), Lam Exelan/4520XLE, Applied
  Materials MxP/eMax, TEL DRM; remote-plasma NF₃-based tools for a
  low-damage alternative.
* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`** and **{ref}`wet bench <machine-wet-bench>`** for the strip and clean.
* **{ref}`Cross-section SEM <machine-cross-section-sem-profilers>`**.

## Machines likely used at SkyWater

* **Lam 9400 TCP.** "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6,
  O2".[^skw-01] Strength: **strong** for the tool and the "nitride"
  label with CF₄/O₂; assignment to this step is an **inference**.
* **AMAT DPS II** ("HBR, Cl2, NF3, CF4, CHF3, O2 – gate, trench,
  W/WN"[^skw-01]) — carries CF₄/CHF₃ and, being the gate etcher, has
  the poly-stop chemistries in hand. Strength: **medium** for this
  step, since its CF₄ and CHF₃ etch nitride although the entry names no
  nitride application.
* **Lam 4400** ("HBr, Cl2, C2F6, CF4, SF6, O2"[^skw-01]). Strength:
  **weak**, as the entry names no application.
* **Ashers — GaSonics PEP, Iridia, Mattson Aspen II; wet benches —
  Akrion Gamma, DNS, FSI Mercury.**[^skw-01] Strength: strong for
  existence.

## Resources required

* **{ref}`CF₄ <material-etch-gases>`, CHF₃, {ref}`O₂ <material-process-gases>`, N₂/Ar** for the nitride and oxide etch; **NF₃** for
  a remote-plasma variant or chamber clean.[^skw-01]
* **Helium** backside cooling.
* **O₂/N₂/{ref}`forming gas <material-anneal-ambients>`** for the strip; **H₂SO₄/H₂O₂ and SC-1** ({ref}`wet chemicals <material-wet-chemicals>`) for the
  clean.[^wiki-rca]
* **{ref}`Chamber consumables <material-hardware-consumables>`**, **{ref}`monitor wafers <material-substrates>`** with blanket nitride,
  oxide and poly for rate and selectivity checks.

## Related steps and cross-references

* Previous: {ref}`NPCM <step-078>` (the resist pattern). Next:
  {ref}`SPOX <step-080>` (oxide over the opened poly).
* The stack being cut: {ref}`POC <step-059>`, {ref}`GATENIT <step-058>`;
  the spacer beside it: {ref}`SPNIT <step-076>`, {ref}`SPE <step-077>`.
* The implants that dope the opened poly: {ref}`PSDI <step-082>`,
  {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`; the resistors whose
  heads are opened: {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`.
* The contacts that land in the opening: {ref}`LICM1 <step-093>`,
  {ref}`LICM1E <step-094>`.
* Other nitride etches: {ref}`STINITE <step-005>`,
  {ref}`ONOME <step-042>`, {ref}`SPE <step-077>`.
* Category page: {ref}`Etch <category-etch>`.

## References

### Cross-check

* SkyWater PDK, *Layers Reference* — `npc` "Nitride poly cut (under
  licon1 areas)".[^pdk-06]
* SkyWater PDK, *Periphery rules* — npc.1–npc.5, rpm.5,
  licon.13–licon.18.[^pdk-periph]
* SkyWater PDK, *Criteria & Assumptions* — "poly cap after SPE"
  0.2 µm.[^pdk-03]
* SkyWater, *Facilities & Capabilities* — Lam 9400 TCP
  "poly/nitride"; AMAT DPS II; ashers and wet benches.[^skw-01]
* Stanford Nanofabrication Facility, *Lam Research TCP 9400* — the
  tool class.[^snf-9400]
* Tokyo Electron, US 6,376,262 — the 387 nm CN endpoint for nitride
  etching.[^pat-cn-tel]

### High-level understanding

* Wikipedia, *Reactive-ion etching*.[^wiki-rie]
* Wikipedia, *RCA clean* — the post-etch clean.[^wiki-rca]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — dielectric
  etching and selectivity.[^txt-01]
* Nojiri, *Dry Etching Technology for Semiconductors* — fluorocarbon
  etching and endpoint detection.[^nojiri-2015]

### Deep dive

* Tang et al. (Texas Instruments), IEDM 1985 and *IEEE TED* 1987 — a
  TiN local-interconnect layer formed during self-aligned silicidation
  and patterned between gates and junctions
  (abstracts).[^tang-1985][^tang-1987]
* Kastenmeier, Matsuo, Beulens and Oehrlein, *JVST A* 1996 — nitride
  and oxide etch rates in CF₄/O₂/N₂.[^kastenmeier-1996]
* Kastenmeier, Matsuo and Oehrlein, *JVST A* 1999 — nitride etching
  selective to silicon and oxide, the stop this etch needs.[^kastenmeier-1999]
* Staffa et al., *Appl. Phys. Lett.* 1995 — remote NF₃/Cl₂ nitride
  etching and its selectivity.[^staffa-1995]
* Lee and Chen, *J. Appl. Phys.* 1983 — how CF₄/O₂ etches silicon,
  the competing reaction at the stop.[^lee-chen-1983]
* Flamm and Donnelly, *Plasma Chem. Plasma Process.* 1981, and
  Winters and Coburn, *Surf. Sci. Rep.* 1992 — the chemistry of
  fluorocarbon selectivity.[^flamm-1981][^winters-1992]
* Joubert and Bell, *J. Electrochem. Soc.* 1997 — resist and oxide
  masks over poly in high-density plasmas.[^joubert-1997]
* Tuda, Shintani and Tanimura, *JJAP* 2004 — selective removal of
  hard masks and residues from poly gates.[^tuda-2004]
* Cacciato et al., P2ID 2003 — charging when a contact etch meets a
  nitride layer, the risk the cut removes.[^cacciato-2003]
* Oehrlein, *Mater. Sci. Eng. B* 1989 — dry-etch damage to the
  silicon (here poly) surface.[^oehrlein-1989]
* Gottscho, Jurgensen and Vitkavage, *JVST B* 1992 — micro-loading
  in small openings.[^gottscho-1992]
* Regis et al. (Applied Materials), ASMC 1997 — the selective nitride
  RIE family.[^regis-1997]

## Open questions

* The chemistry, endpoint and over-etch of the cut, and how much of
  the adjacent spacer it is allowed to remove, are not public.
* Whether any {ref}`POC <step-059>` oxide is still present at the
  start of the etch is not public.
* The reading that the opened poly is deliberately doped by the
  source/drain implants is an inference from the PDK rules
  ({ref}`NPCM <step-078>`).
* Which etcher on SkyWater's list runs the step is inferred from the
  "poly/nitride" label.[^skw-01]

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^snf-9400]: Stanford Nanofabrication Facility, *Lam Research TCP 9400
    Poly Etcher (lampoly)*, equipment page.
    <https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>
[^pat-cn-tel]: Tokyo Electron Ltd., *Method of forming a semiconductor
    device using double endpoint detection*, US 6,376,262 B1, granted
    2002-04-23. <https://patents.google.com/patent/US6376262B1/en>
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^nojiri-2015]: K. Nojiri, *Dry Etching Technology for Semiconductors*,
    Springer, 2015. <https://doi.org/10.1007/978-3-319-10295-5>
[^tang-1985]: T. E. Tang, C.-C. Wei, R. A. Haken, T. C. Holloway,
    C.-F. Wan and M. A. Douglas, "VLSI local interconnect level using
    titanium nitride", *IEDM 1985 Technical Digest*, pp. 590–593.
    <https://doi.org/10.1109/IEDM.1985.191041>
[^tang-1987]: T. E. Tang, C.-C. Wei, R. A. Haken, T. C. Holloway,
    L. R. Hite and T. G. W. Blake, "Titanium nitride local interconnect
    technology for VLSI", *IEEE Transactions on Electron Devices*
    **34**(3), 682–688 (1987). <https://doi.org/10.1109/T-ED.1987.22980>
[^kastenmeier-1996]: B. E. E. Kastenmeier, P. J. Matsuo, J. J. Beulens
    and G. S. Oehrlein, "Chemical dry etching of silicon nitride and
    silicon dioxide using CF₄/O₂/N₂ gas mixtures", *Journal of Vacuum
    Science & Technology A* **14**(5), 2802–2813 (1996).
    <https://doi.org/10.1116/1.580203>
[^kastenmeier-1999]: B. E. E. Kastenmeier, P. J. Matsuo and
    G. S. Oehrlein, "Highly selective etching of silicon nitride over
    silicon and silicon dioxide", *Journal of Vacuum Science &
    Technology A* **17**(6), 3179–3184 (1999).
    <https://doi.org/10.1116/1.582097>
[^staffa-1995]: J. Staffa, D. Hwang, B. Luther, J. Ruzyllo and R. Grant,
    "Temperature dependence of the etch rate and selectivity of silicon
    nitride over silicon dioxide in remote plasma NF₃/Cl₂", *Applied
    Physics Letters* **67**(13), 1902–1904 (1995).
    <https://doi.org/10.1063/1.114371>
[^lee-chen-1983]: Y. H. Lee and M.-M. Chen, "Silicon etching mechanism
    and anisotropy in CF₄+O₂ plasma", *Journal of Applied Physics*
    **54**(10), 5966–5973 (1983). <https://doi.org/10.1063/1.331774>
[^flamm-1981]: D. L. Flamm and V. M. Donnelly, "The design of plasma
    etchants", *Plasma Chemistry and Plasma Processing* **1**(4),
    317–363 (1981). <https://doi.org/10.1007/BF00565992>
[^winters-1992]: H. F. Winters and J. W. Coburn, "Surface science
    aspects of etching reactions", *Surface Science Reports*
    **14**(4–6), 162–269 (1992).
    <https://doi.org/10.1016/0167-5729(92)90009-Z>
[^joubert-1997]: O. Joubert and F. H. Bell, "Polysilicon Gate Etching
    in High-Density Plasmas: Comparison Between Oxide Hard Mask and
    Resist Mask", *Journal of The Electrochemical Society* **144**(5),
    1854–1861 (1997). <https://doi.org/10.1149/1.1837690>
[^tuda-2004]: M. Tuda, K. Shintani and J. Tanimura, "Highly Selective
    Removal of Residual Deposited Films and Oxide Hard Masks on
    Polysilicon Gate Electrodes in Anhydrous HF Gases", *Japanese
    Journal of Applied Physics* **43**(3R), 945 (2004).
    <https://doi.org/10.1143/JJAP.43.945>
[^cacciato-2003]: A. Cacciato, A. Scarpa, S. Evseev and M. Diekema,
    "Charging damage during contact etch triggered by increased
    borderless nitride conductivity", *Proc. 2003 8th International
    Symposium on Plasma- and Process-Induced Damage*, pp. 20–23.
    <https://doi.org/10.1109/PPID.2003.1199721>
[^oehrlein-1989]: G. S. Oehrlein, "Dry etching damage of silicon: A
    review", *Materials Science and Engineering: B* **4**(1–4), 441–450
    (1989). <https://doi.org/10.1016/0921-5107(89)90284-5>
[^gottscho-1992]: R. A. Gottscho, C. W. Jurgensen and D. J. Vitkavage,
    "Microscopic uniformity in plasma etching", *Journal of Vacuum
    Science & Technology B* **10**(5), 2133–2147 (1992).
    <https://doi.org/10.1116/1.586180>
[^regis-1997]: J. M. Regis, A. M. Joshi, T. Lill and M. Yu, "Reactive
    ion etch of silicon nitride spacer with high selectivity to oxide",
    *1997 IEEE/SEMI Advanced Semiconductor Manufacturing Conference and
    Workshop (ASMC 97) Proceedings*, pp. 252–256.
    <https://doi.org/10.1109/ASMC.1997.630744>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
