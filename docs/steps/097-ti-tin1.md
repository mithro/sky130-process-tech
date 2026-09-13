(step-097)=
# Step 097 — TI/TIN1: IMP Ti/TiN deposition

| | |
|---|---|
| **Step number** | 97 of 171[^steps-sheet] |
| **Step code** | `TI/TIN1` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | MOL — silicide and local interconnect |
| **Previous step** | {ref}`ALLY1 <step-096>` |
| **Next step** | {ref}`CSIL <step-098>` |

## What this step is

`TI/TIN1` sputters the contact {term}`liner`: a thin titanium film followed
by a thin titanium-nitride film, sputtered into the open contact holes
of {ref}`LICM1E <step-094>` and over the field. The titanium lands on
the freshly cleaned silicon and poly at the bottom of each hole,
where the next step ({ref}`CSIL <step-098>`) will react it into
titanium disilicide; the titanium nitride covers the titanium and
the oxide walls of the hole and is the barrier and adhesion layer on
which the {term}`CVD` tungsten of {ref}`WDEP <step-099>` nucleates. It
is the first of the liner depositions described in this reference —
{ref}`TIN2 <step-109>`, {ref}`TIN3 <step-120>` and later are the
TiN-only liners of the contact and {term}`via` levels.

The public evidence is unusually direct for a tool assignment.
SkyWater's capability list gives, under "AMAT PVD Metal", "Imp TiN"
and "Collimated Ti" alongside "ESC TiN", TiW and the aluminium
alloys,[^skw-01] and this reference reads the liner as titanium followed
by ionised-metal-plasma ({term}`IMP`) TiN, from "Imp TiN" (inference);
whether the titanium is collimated, as "Collimated Ti" would allow, or
ionised is not public. Ionised {term}`PVD` is the technique Rossnagel and
Hopwood introduced for exactly this purpose — filling the bottom of
a hole that line-of-sight sputtering cannot
reach[^rossnagel-1993][^rossnagel-1994] — and Applied Materials sold
it as the IMP chamber on its Endura platform.[^amat-endura][^pat-imp-amat]
The film thicknesses are not public. Industry-typical values for a
0.17 µm contact at this node are of the order of 10–30 nm of
titanium and 10–30 nm of TiN on the field, with bottom coverage of
tens of per cent (Koerner, Erb and Melzner evaluated Ti and TiN
thicknesses for tungsten-plug contacts[^koerner-1993]); the
titanium thickness at the hole bottom, together with the anneal,
sets the {term}`silicide` thickness of the next step.

## Step category

`TI/TIN1` is a {ref}`Thin-film deposition <category-deposition>` step
of the *PVD* type — the first sputtered film in the flow and the
first metal of any kind on the wafer. The category page describes
magnetron sputtering, its line-of-sight flux, Thornton's zone
model[^thornton-1974][^ohring-2002] and the reason IMP exists: an
ordinary sputter source cannot coat the bottom of a hole of aspect
ratio above about 2:1, and the licons are about 6:1 at the bottom
("Standard Licon bottom CD" 0.08 µm[^pdk-03] under 0.5 µm of
dielectric[^pdk-03]). What is specific to this instance is the dual
role of the titanium — a silicide precursor at the hole bottoms and
a mere adhesion layer elsewhere — and the fact that the titanium
nitride is deposited *reactively*, by sputtering titanium in an
argon–nitrogen plasma, so that its stoichiometry, resistivity and
stress are set by the nitrogen flow (Sundgren's review of TiN
coatings[^sundgren-1985]; Berg and Nyberg's model of reactive
sputtering[^berg-2005]).

## Why this step exists

A tungsten plug cannot be put straight onto silicon. The reasons for
each film:

* **Titanium: the contact.** Titanium reduces the last traces of
  native oxide on the silicon and, on annealing, forms TiSi₂ — the
  low-resistivity, low-barrier contact the {ref}`CSIL <step-098>`
  page describes (Murarka on formation,[^murarka-1983] Maex on TiSi₂
  and its silicon consumption[^maex-1993]). Without it the tungsten
  would contact bare silicon through whatever oxide survived, with
  a high and variable resistance.
* **Titanium nitride: the barrier.** Tungsten hexafluoride attacks
  silicon and titanium during the CVD nucleation, and the reaction
  by-products would consume the silicide; a TiN film is inert to WF₆
  at deposition temperature, adheres to oxide, and is the surface on
  which the silane-nucleated tungsten grows (Srinivas et al. studied
  tungsten nucleation on TiN[^srinivas-1992]). Wittmer established
  TiN as a diffusion barrier in silicon metallisation,[^wittmer-1980]
  building on Nicolet's survey of thin-film barriers.[^nicolet-1978]
  Wikipedia summarises the role: TiN films "serve as a conductive
  connection between the active device and the metal contacts …
  while acting as a diffusion barrier".[^wiki-tin]
* **Ionised deposition: the coverage.** The barrier must be
  continuous at the hole bottom and on the lower sidewalls, where a
  conventional sputtered film is thinnest. Rossnagel and Hopwood
  showed that ionising the sputtered metal in a secondary RF plasma
  and biasing the wafer draws the ions vertically into the
  hole;[^rossnagel-1993][^rossnagel-1994] Hopwood reviewed ionised
  PVD for interconnects[^hopwood-1998] and Rossnagel the directional
  and ionised alternatives.[^rossnagel-1998] The older alternative,
  {term}`collimated sputtering` — a honeycomb collimator between target and
  wafer that passes only near-normal atoms — is what "Collimated Ti"
  on SkyWater's list refers to,[^skw-01] introduced by Rossnagel et
  al.[^rossnagel-1991] and applied to Ti/TiN by Ryan et al.[^ryan-1995]
  Applied Materials' patent alternates IMP and conventional steps to
  improve sidewall coverage.[^pat-imp-amat]
* **Silicide thickness control.** Because the silicide is formed
  only in the contact bottoms, the titanium thickness there — a
  fraction of the field thickness set by the bottom coverage — is
  what decides how much of the 0.1 µm junction[^pdk-03] the silicide
  consumes: TiSi₂ consumes about 2.3 nm of silicon per nanometre of
  titanium (Maex[^maex-1993]).

Without `TI/TIN1` the tungsten fill would fail to nucleate, the
contacts would be rectifying or open, and the junctions would be
attacked by fluorine.

## How it is typically performed

An industry-generic IMP Ti/TiN contact liner for a 200 mm,
130 nm-era fab (SKY130's recipe is not public):

1. **Degas and pre-clean.** On the {term}`cluster tool`: a {term}`degas` station
   (lamp or heated chuck, 300–400 °C, minutes) to drive water out of
   the dielectric, then an argon RF sputter-etch pre-clean that
   removes the last nanometre of native oxide from the contact
   bottoms — light enough not to sputter oxide from the walls onto
   the silicon (category page[^txt-09]). SkyWater's "AMAT PVD Metal"
   entry lists "Sputter etch, degas" among its chambers.[^skw-01]
2. **IMP titanium.** DC magnetron sputtering from a titanium target
   in argon at a few tens of mTorr — higher than conventional
   sputtering, so that the sputtered atoms thermalise and are
   ionised by the RF coil — with a substrate bias that draws the Ti⁺
   ions normally into the holes; wafer temperature of the order of
   100–300 °C (industry-typical[^rossnagel-1998][^txt-09]).
3. **IMP or reactive TiN.** Either in the same chamber with
   nitrogen added, or in a second chamber: titanium sputtered in
   Ar/N₂ forms TiN on the wafer, with the nitrogen flow held in the
   "poisoned" regime for stoichiometric, golden TiN; the transition
   is hysteretic and is the main control problem of reactive
   sputtering.[^berg-2005] IMP TiN deposits with a bombardment that
   densifies the film and improves its barrier quality (the
   microstructural evolution Petrov et al. review[^petrov-2003]).
   SkyWater lists both "Imp TiN" and "ESC TiN" (electrostatic-chuck
   TiN, a conventional chamber).[^skw-01]
4. **Thicknesses.** Of the order of 10–30 nm Ti and 10–30 nm TiN on
   the field (industry-typical for this node; Koerner et
   al.[^koerner-1993]); not public for SKY130.
5. **Optional in-situ treatment.** Some flows add a short N₂/H₂
   plasma or a low-temperature anneal on the platform to "stuff" the
   TiN grain boundaries and reduce its fluorine uptake.
6. **Metrology.** {term}`Sheet resistance <sheet resistance>` of Ti and TiN monitors by
   {term}`four-point probe`; thickness by XRF or ellipsometry; stress
   by wafer bow; {term}`step coverage` by cross-section SEM during
   development; particles.

## Machines typically used

* **{ref}`Cluster PVD system <machine-pvd-cluster-tool>`**, 200 mm, with degas, pre-clean, Ti and TiN
  chambers: Applied Materials Endura with IMP
  chambers,[^amat-endura][^amat-1997] Novellus INOVA (hollow-cathode
  magnetron), Varian/Novellus M2i, MRC Eclipse (category page).
* **{ref}`Four-point probe <machine-sheet-resistance-metrology>`**, **{ref}`XRF <machine-film-thickness-metrology>`**, **stress gauge**, **{ref}`cross-section SEM <machine-cross-section-sem-profilers>`**.

## Machines likely used at SkyWater

* **Applied Materials PVD with IMP TiN and collimated Ti chambers.**
  SkyWater lists "AMAT PVD Metal" with "Imp TiN", "Collimated Ti"
  and "ESC TiN".[^skw-01] Strength: **strong** for the vendor and
  the chamber types; the platform (Endura is the AMAT 200 mm PVD
  cluster of the era[^amat-endura]) is an **inference**, as is the
  assignment of this step to the IMP TiN and collimated Ti chambers,
  from those chamber types and the contact's aspect ratio. Whether the
  titanium is deposited by IMP or by collimation
  is not public; SkyWater's list names collimation for Ti and IMP for
  TiN.
* **Sputter targets.** SkyWater's filings name Honeywell Electronic
  Materials (2021 S-1 and fiscal 2023 10-K) and JX Metals (fiscal 2023 10-K)
  as sputter-target suppliers.[^sec-01][^sec-02] Strength: strong for the
  suppliers; the specific target is not named.

## Resources required

* **Titanium sputter targets** (high-purity, bonded to backing plates;
  SkyWater's filings name Honeywell Electronic Materials (2021 S-1 and
  fiscal 2023 10-K) and JX Metals (fiscal 2023 10-K) as sputter-target
  suppliers[^sec-01][^sec-02]).
* **Argon** (sputter gas) and **nitrogen** (reactive gas for
  TiN);[^wiki-sputter] **helium** backside cooling.
* **Chamber consumables** — shields, coils, clamp or {term}`ESC` rings,
  collimators (for the collimated chamber), pasting targets.
* **Monitor wafers** (SEMI M8 class)[^semi-m8] for sheet resistance,
  thickness and particles.
* Gas suppliers named in SkyWater's 2021 S-1: Air Products,
  Praxair.[^sec-01]

## Related steps and cross-references

* Previous: {ref}`ALLY1 <step-096>` (the anneal that precedes the
  liner). Next: {ref}`CSIL <step-098>` (the silicide anneal that
  reacts the titanium), then {ref}`WDEP <step-099>` and
  {ref}`WCMPLI <step-100>`.
* The holes lined: {ref}`LICM1 <step-093>`, {ref}`LICM1E <step-094>`;
  the clean before it: {ref}`SACETCH <step-095>`.
* Later liners: {ref}`TIN2 <step-109>`, {ref}`TIN3 <step-120>`,
  {ref}`TIN4 <step-131>`, {ref}`TIN5 <step-146>`; the other TiN
  film of this module: {ref}`LITIN <step-101>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — "AMAT PVD Metal": "Imp
  TiN", "Collimated Ti", "ESC TiN".[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — sputter-target and
  gas suppliers.[^sec-01][^sec-02]
* SkyWater PDK, *Criteria & Assumptions* — "Standard Licon bottom
  CD" 0.08 µm; "Pre-LI ILD thickness" 0.5 µm; S/D junction
  0.1 µm.[^pdk-03]
* Applied Materials, *Endura PVD* product page and 1997 Annual
  Report.[^amat-endura][^amat-1997]
* Applied Materials, US 6,350,353 — IMP/sputter alternation.[^pat-imp-amat]

### High-level understanding

* Wikipedia, *Titanium nitride*, *Sputter deposition*, *Physical
  vapor deposition*.[^wiki-tin][^wiki-sputter][^wiki-pvd]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  sputtering and barrier metals.[^txt-02]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — PVD equipment, degas and pre-clean.[^txt-09]
* Ohring, *Materials Science of Thin Films* — nucleation, growth and
  the structure-zone model.[^ohring-2002]

### Deep dive

* Rossnagel and Hopwood, *Appl. Phys. Lett.* 1993 and *JVST B*
  1994 — ionised magnetron sputtering and metal-ion
  deposition.[^rossnagel-1993][^rossnagel-1994]
* Hopwood, *Phys. Plasmas* 1998 — ionised PVD for
  interconnects.[^hopwood-1998]
* Rossnagel, *JVST B* 1998 — review of directional and ionised
  PVD.[^rossnagel-1998]
* Rossnagel et al., *JVST A* 1991 — collimated magnetron sputter
  deposition.[^rossnagel-1991]
* Ryan et al., *MRS Bulletin* 1995 — collimated sputtering of Ti and
  TiN.[^ryan-1995]
* Wittmer, *Appl. Phys. Lett.* 1980, and Nicolet, *Thin Solid Films*
  1978 — TiN as a diffusion barrier; barriers in
  general.[^wittmer-1980][^nicolet-1978]
* Sundgren, *Thin Solid Films* 1985 — structure and properties of
  TiN coatings.[^sundgren-1985]
* Berg and Nyberg, *Thin Solid Films* 2005 — reactive sputtering
  model and hysteresis.[^berg-2005]
* Petrov et al., *JVST A* 2003 — microstructural evolution during
  film growth.[^petrov-2003]
* Thornton, *J. Vac. Sci. Technol.* 1974 — the structure-zone
  diagram.[^thornton-1974]
* Koerner, Erb and Melzner, *Appl. Surf. Sci.* 1993 — Ti and TiN
  thicknesses for tungsten-plug contacts.[^koerner-1993]
* Srinivas et al., *MRS Proc.* 1992 — tungsten nucleation on
  TiN.[^srinivas-1992]
* Murarka, *Silicides for VLSI Applications* 1983, and Maex, *Mater.
  Sci. Eng. R* 1993 — silicide formation and silicon
  consumption.[^murarka-1983][^maex-1993]

## Open questions

* The Ti and TiN thicknesses, the bottom coverage, the bias and
  pressure, and whether the titanium is deposited by IMP or by
  collimation are not public; SkyWater's list names collimated Ti
  and IMP TiN but assigns neither to a step.
* Whether a degas and sputter pre-clean precede the titanium on the
  platform, and how they interact with {ref}`ALLY1 <step-096>` and
  {ref}`SACETCH <step-095>`, is not public.
* Whether the TiN is deposited in the same chamber as the titanium
  or in a separate one is not public.

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^amat-endura]: Applied Materials, *Endura PVD*, product page.
    <https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report*.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^pat-imp-amat]: P. Gopalraja, S. Edelstein, A. Tepman, P. Ding,
    D. Ghosh and N. Maity (Applied Materials), *Alternate steps of IMP
    and sputtering process to improve sidewall coverage*,
    US 6,350,353 B2, filed 1999-11-24, granted 2002-02-26.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6350353>
[^wiki-tin]: Wikipedia, *Titanium nitride*.
    <https://en.wikipedia.org/wiki/Titanium_nitride>
[^wiki-sputter]: Wikipedia, *Sputter deposition*.
    <https://en.wikipedia.org/wiki/Sputter_deposition>
[^wiki-pvd]: Wikipedia, *Physical vapor deposition*.
    <https://en.wikipedia.org/wiki/Physical_vapor_deposition>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007,
    ISBN 978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^ohring-2002]: M. Ohring, *Materials Science of Thin Films*, 2nd ed.,
    Academic Press, 2002.
    <https://doi.org/10.1016/B978-0-12-524975-1.X5000-9>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^rossnagel-1993]: S. M. Rossnagel and J. Hopwood, "Magnetron sputter
    deposition with high levels of metal ionization", *Applied Physics
    Letters* **63**(24), 3285–3287 (1993).
    <https://doi.org/10.1063/1.110176>
[^rossnagel-1994]: S. M. Rossnagel and J. Hopwood, "Metal ion deposition
    from ionized magnetron sputtering discharge", *Journal of Vacuum
    Science & Technology B* **12**(1), 449–453 (1994).
    <https://doi.org/10.1116/1.587142>
[^hopwood-1998]: J. Hopwood, "Ionized physical vapor deposition of
    integrated circuit interconnects", *Physics of Plasmas* **5**(5),
    1624–1631 (1998). <https://doi.org/10.1063/1.872829>
[^rossnagel-1998]: S. M. Rossnagel, "Directional and ionized physical
    vapor deposition for microelectronics applications", *Journal of
    Vacuum Science & Technology B* **16**(5), 2585–2608 (1998).
    <https://doi.org/10.1116/1.590242>
[^rossnagel-1991]: S. M. Rossnagel, D. Mikalsen, H. Kinoshita and
    J. J. Cuomo, "Collimated magnetron sputter deposition", *Journal of
    Vacuum Science & Technology A* **9**(2), 261–265 (1991).
    <https://doi.org/10.1116/1.577531>
[^ryan-1995]: J. G. Ryan, S. B. Brodsky, T. Katata, M. Honda, N. Shoda
    and H. Aochi, "Collimated Sputtering of Titanium and Titanium
    Nitride Films", *MRS Bulletin* **20**(11), 42–45 (1995).
    <https://doi.org/10.1557/S0883769400045553>
[^wittmer-1980]: M. Wittmer, "TiN and TaN as diffusion barriers in
    metallizations to silicon semiconductor devices", *Applied Physics
    Letters* **36**(6), 456–458 (1980). <https://doi.org/10.1063/1.91505>
[^nicolet-1978]: M.-A. Nicolet, "Diffusion barriers in thin films",
    *Thin Solid Films* **52**(3), 415–443 (1978).
    <https://doi.org/10.1016/0040-6090(78)90184-0>
[^sundgren-1985]: J.-E. Sundgren, "Structure and properties of TiN
    coatings", *Thin Solid Films* **128**(1–2), 21–44 (1985).
    <https://doi.org/10.1016/0040-6090(85)90333-5>
[^berg-2005]: S. Berg and T. Nyberg, "Fundamental understanding and
    modeling of reactive sputtering processes", *Thin Solid Films*
    **476**(2), 215–230 (2005).
    <https://doi.org/10.1016/j.tsf.2004.10.051>
[^petrov-2003]: I. Petrov, P. B. Barna, L. Hultman and J. E. Greene,
    "Microstructural evolution during film growth", *Journal of Vacuum
    Science & Technology A* **21**(5), S117–S128 (2003).
    <https://doi.org/10.1116/1.1601610>
[^thornton-1974]: J. A. Thornton, "Influence of apparatus geometry and
    deposition conditions on the structure and topography of thick
    sputtered coatings", *Journal of Vacuum Science and Technology*
    **11**(4), 666–670 (1974). <https://doi.org/10.1116/1.1312732>
[^koerner-1993]: H. Koerner, H. P. Erb and H. Melzner, "Evaluation of
    Ti and TiN thicknesses for tungsten plug contact metallization",
    *Applied Surface Science* **73**, 6–13 (1993).
    <https://doi.org/10.1016/0169-4332(93)90139-3>
[^srinivas-1992]: D. Srinivas, R. Foster, S. Marcus, R. Arora and
    H. Rebenne, "Nucleation of Tungsten on Titanium Nitride with
    Hydrogen Reduction of Tungsten Hexafluoride", *MRS Proceedings*
    **282** (1992). <https://doi.org/10.1557/PROC-282-365>
[^murarka-1983]: S. P. Murarka, "Formation", in *Silicides for VLSI
    Applications*, Academic Press, 1983, pp. 99–131.
    <https://doi.org/10.1016/b978-0-08-057056-3.50009-4>
[^maex-1993]: K. Maex, "Silicides for integrated circuits: TiSi₂ and
    CoSi₂", *Materials Science and Engineering: R* **11**(2–3), vii–153
    (1993). <https://doi.org/10.1016/0927-796X(93)90001-J>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
