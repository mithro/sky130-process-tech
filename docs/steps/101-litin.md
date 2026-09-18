(step-101)=
# Step 101 — LITIN: TiN deposition

| | |
|---|---|
| **Step number** | 101 of 171[^steps-sheet] |
| **Step code** | `LITIN` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | MOL — silicide and local interconnect |
| **Previous step** | {ref}`WCMPLI <step-100>` |
| **Next step** | {ref}`LI1M <step-102>` |

## What this step is

`LITIN` deposits the {term}`local interconnect` itself: a blanket film of
titanium nitride, about 0.1 µm thick, sputtered (on our reading) onto
the polished surface of {ref}`WCMPLI <step-100>` — planar {term}`cap oxide`
studded with
tungsten plugs. The next two steps pattern it ({ref}`LI1M <step-102>`,
{ref}`LI1ME <step-103>`) into the `li1` layer of the PDK, a wiring
level *below* metal 1 that connects transistor terminals to one
another and to the `mcon` contacts of metal 1 over short distances.
This reference describes the film as the local-interconnect titanium
nitride, distinct from the {term}`liner` TiN of {ref}`TI/TIN1 <step-097>`;
the public basis for that description follows.

The public record on this film is better than for most of the flow.
The PDK's stack diagram labels the conductor `li` with a thickness of
0.1 µm and places it between the "PSG" dielectric and the "LINT"
nitride;[^pdk-04] the assumptions table gives "LI1 thickness for
antenna ratio calculations" as 0.1 µm;[^pdk-03] the extraction
tables give "Local interconnect" a {term}`sheet resistance` of
12 800 mΩ/sq (12.8 Ω/sq);[^pdk-08] the layer list describes `li1`
(67:20) as "Local interconnect" and `licon1` and `mcon` as the
contacts to and from it;[^pdk-06] SkyWater's PDK README summarises
the process as having "1 level of local interconnect";[^pdk-10] an
Efabless lecture on the PDK gives the local interconnect as
"Titanium Nitride (TiN)" at 0.1 µm;[^ann-16] and SkyWater's press
release on the first open-source shuttle counts "the local
interconnect" among the features SKY130 "offers … as
standard".[^ann-11] The arithmetic closes: 12.8 Ω/sq × 0.1 µm gives
a resistivity of about 128 µΩ·cm, several times the roughly
39 µΩ·cm Wikipedia quotes for bulk TiN[^wiki-tin] and squarely in
the range of reactively sputtered TiN films (Sundgren's
review[^sundgren-1985]). SkyWater's capability list includes "ESC
TiN" and "Imp TiN" chambers on its AMAT {term}`PVD` tool[^skw-01] and
its filings name Honeywell Electronic Materials (2021 S-1 and fiscal
2023 10-K) and JX Metals (fiscal 2023 10-K) as sputter-target
suppliers.[^sec-01][^sec-02]

## Step category

`LITIN` is a {ref}`Thin-film deposition <category-deposition>` step of
the *PVD* type — {term}`reactive sputtering` of titanium in argon–nitrogen
(inferred; SkyWater's public list has PVD TiN chambers and no {term}`CVD`
TiN[^skw-01]) — and the only step in the flow whose sputtered
*titanium nitride* is a wiring level in its own right rather than a
liner, barrier or cap; the aluminium levels above it are sputtered
wiring too. The category
page describes the technique and TiN's other roles (barrier, {term}`ARC`,
the underlayer on which Blech discovered the critical-length
effect[^blech-1976]). What is specific to this instance is that the
film's *sheet resistance* is a circuit parameter: at 12.8 Ω/sq[^pdk-08]
it is a hundred times metal 1's 125 mΩ/sq[^pdk-08] but four times
better than the unsilicided poly (48.2 Ω/sq[^pdk-08]), which is
exactly what makes it useful for the short connections inside a
standard cell or an SRAM bit cell that would otherwise cost a metal-1
track. Thickness uniformity, resistivity (set by stoichiometry and
microstructure) and stress are therefore controlled as they would be
for a metal.

## Why this step exists

A titanium-nitride local interconnect is an idea from the mid-1980s
that SKY130 carried into the 130 nm generation. Its history and
reasons:

* **Origins.** Tang et al. at Texas Instruments described a "VLSI
  local interconnect level using titanium nitride" at IEDM 1985 and
  in *IEEE TED* 1987,[^tang-1985][^tang-1987] using the TiN that
  forms on top of a titanium {term}`salicide` during its nitrogen anneal as
  a patternable conductor; the corresponding TI patents by Haken and
  Holloway and by Holloway et al. claim the structure and the
  patterning process.[^pat-li-ti-haken][^pat-li-ti-holloway] Mann et
  al. at IBM reviewed {term}`silicides <silicide>` and local interconnections
  together,[^mann-1995] and White et al. described a damascene-stud
  local interconnect.[^white-1992] SKY130's version, on our reading,
  differs from TI's in that the TiN is a *deposited* film on a
  polished dielectric rather than the by-product of a salicide —
  consistent with the contact-only silicide of {ref}`CSIL <step-098>`.
* **Routing density.** A wiring level below metal 1 that can run
  over gates and along diffusions lets a cell connect its
  transistors without consuming metal-1 tracks; the PDK's rules
  allow 0.17 µm lines and spaces (li.1, li.3) and 0.14 µm inside
  certain RF cells (li.1a, li.3a),[^pdk-periph] with an area minimum
  of 0.0561 µm² (li.6) and a resistor form (li.7) 0.290 µm wide.[^pdk-periph]
  A `li1` resistor is in fact a PDK device — the physical-criteria
  table carries a "Li resistor width (to drop one Licon w/o
  dogbones)" of 0.29 µm (`LIRESCD`)[^pdk-03] and the periphery rules
  a minimum LI-resistor width of 0.290 µm (li.7)[^pdk-periph] — which
  only a film with a well-controlled, moderately high sheet
  resistance can provide.
* **Why TiN and not a metal.** TiN is refractory, so the levels
  above it can be processed at the 400–450 °C of the tungsten and
  oxide depositions without {term}`hillocks <hillock>` or interdiffusion; it does not
  react with the tungsten plugs it lands on; it adheres to oxide;
  and it can be etched in chlorine or fluorine plasmas with
  {term}`selectivity` to oxide ({ref}`LI1ME <step-103>`). Its resistivity —
  set by nitrogen stoichiometry, density and grain structure
  (Sundgren;[^sundgren-1985] the reactive-sputtering model of Berg
  and Nyberg;[^berg-2005] the microstructural evolution Petrov et
  al. review[^petrov-2003]) — is high for a wire but acceptable for
  runs of a few micrometres, and the li.2 rule ("Max ratio of length
  to width of LI without licon or mcon", 10)[^pdk-periph] is, we
  infer, partly an antenna and partly a resistance constraint.
* **What it lands on.** The film must cover the tungsten plugs
  completely (licon.4, li.5[^pdk-periph]) and step down into
  whatever recess the polish left; a conventional (non-IMP) sputter
  suffices on a planar surface, which is why an "ESC TiN"
  chamber[^skw-01] rather than an {term}`IMP` chamber is, we infer, the
  natural choice here.

Without `LITIN` there would be no `li1`: every transistor terminal
would need a metal-1 connection, and the standard-cell and SRAM
layouts of the PDK would not fit.

## How it is typically performed

An industry-generic reactively sputtered TiN film for a 200 mm,
130 nm-era fab (SKY130's recipe is not public):

1. **Degas and pre-clean.** {term}`Degas <degas>` on the {term}`cluster tool` to drive
   water from the polished oxide; a light argon sputter pre-clean to
   remove the tungsten oxide from the plug tops (Boumerzoug et al.
   describe the effect of titanium oxide on TiN on {term}`via`
   resistance,[^boumerzoug-1997] the analogous problem).
2. **Reactive sputtering.** DC magnetron sputtering from a titanium
   target in Ar/N₂ at a few mTorr, with the nitrogen flow held in
   the nitrided ("poisoned") target regime for stoichiometric TiN —
   the hysteresis Berg and Nyberg model[^berg-2005] is managed by
   flow or partial-pressure control; wafer temperature of the order
   of 200–350 °C on an {term}`electrostatic chuck` ("ESC TiN"[^skw-01]) for
   density and low resistivity (industry-typical[^txt-09][^sundgren-1985]).
   Thornton's zone model[^thornton-1974][^ohring-2002] predicts the
   columnar structure such films have.
3. **Thickness.** 0.1 µm (PDK).[^pdk-04][^pdk-03]
4. **Optional treatments.** A brief N₂ or N₂/H₂ plasma after
   deposition to saturate the surface, or a short in-situ anneal to
   stabilise resistivity; some flows deposit a thin titanium
   adhesion layer first (whether SKY130 does is not public).
5. **Metrology.** Sheet resistance by {term}`four-point probe` on
   product monitor sites and blanket wafers — the 12.8 Ω/sq target;
   thickness by XRF; stress by wafer bow; reflectivity as a
   stoichiometry check; particles.

## Machines typically used

* **{ref}`Cluster PVD system <machine-pvd-cluster-tool>`**, 200 mm, with degas, pre-clean and reactive
  TiN chambers: Applied Materials Endura,[^amat-endura][^amat-1997]
  Novellus INOVA, MRC Eclipse, Varian M2i (category page).
* **{ref}`Four-point probe <machine-sheet-resistance-metrology>`**, **{ref}`XRF <machine-film-thickness-metrology>`**, **stress gauge**, **reflectometer**.

## Machines likely used at SkyWater

* **Applied Materials PVD, "ESC TiN" chamber.** SkyWater lists
  "AMAT PVD Metal" with "ESC TiN" and "Imp TiN".[^skw-01] Strength:
  **strong** for the vendor and for a conventional TiN chamber; the
  platform (Endura-class) and the assignment of `LITIN` to the {term}`ESC`
  chamber rather than the IMP chamber are **inferences** from the
  film's role and the planar surface.
* **Sputter targets.** SkyWater's filings name Honeywell Electronic
  Materials (2021 S-1 and fiscal 2023 10-K) and JX Metals (fiscal 2023 10-K)
  as sputter-target suppliers.[^sec-01][^sec-02] Strength: strong for the
  suppliers; the specific target is not named.

## Resources required

* **Titanium {ref}`sputter targets <material-sputter-targets>`** (SkyWater's filings name Honeywell Electronic
  Materials (2021 S-1 and fiscal 2023 10-K) and JX Metals (fiscal 2023 10-K)
  as sputter-target suppliers[^sec-01][^sec-02]); **{ref}`argon <material-process-gases>`** and
  **nitrogen**.[^wiki-sputter]
* **Helium** backside cooling; {ref}`chamber shields <material-hardware-consumables>`, clamp/ESC parts,
  pasting cycles.
* **{ref}`Monitor wafers <material-substrates>`** (SEMI M8 class)[^semi-m8] for sheet resistance,
  thickness and particle control.
* Gas suppliers named in SkyWater's 2021 S-1: Air Products,
  Praxair.[^sec-01]

## Related steps and cross-references

* Previous: {ref}`WCMPLI <step-100>` (the polished plug surface).
  Next: {ref}`LI1M <step-102>` (the {term}`LI` mask), {ref}`LI1ME <step-103>`
  (the TiN etch), {ref}`LINIT <step-104>` (the nitride cap over it).
* The plugs it lands on: {ref}`WDEP <step-099>`; the contacts to it
  from above: {ref}`CTM1 <step-107>`, {ref}`CTME <step-108>`.
* The liner TiN of the same module: {ref}`TI/TIN1 <step-097>`;
  later TiN liners: {ref}`TIN2 <step-109>`.
* Why the poly is not silicided, and so why LI matters:
  {ref}`P1I <step-050>`, {ref}`CSIL <step-098>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, process stack diagram — `li` 0.1 µm between "PSG"
  and "LINT".[^pdk-04]
* SkyWater PDK, *Criteria & Assumptions* — "LI1 thickness for
  antenna ratio calculations" 0.1 µm; "Li resistor width".[^pdk-03]
* SkyWater PDK, *Parasitic Layout Extraction* — Local interconnect
  12 800 mΩ/sq; Metal1 125 mΩ/sq; Poly 48 200 mΩ/sq.[^pdk-08]
* SkyWater PDK, *Layers Reference* — `li1` 67:20 "Local
  interconnect".[^pdk-06]
* SkyWater PDK, *Periphery rules* — li.1–li.7; licon.4.[^pdk-periph]
* google/skywater-pdk README — "1 level of local interconnect".[^pdk-10]
* Edwards (Efabless), *Introduction to the SkyWater PDK* — local
  interconnect "Titanium Nitride (TiN)", 0.1 µm.[^ann-16]
* SkyWater/Efabless press release, 2021-04-06 — "the local
  interconnect" as a standard feature.[^ann-11]
* SkyWater, *Facilities & Capabilities* — "ESC TiN", "Imp TiN".[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — sputter-target and
  gas suppliers.[^sec-01][^sec-02]

### High-level understanding

* Wikipedia, *Titanium nitride* — properties and microelectronic
  uses.[^wiki-tin]
* Wikipedia, *Sputter deposition*.[^wiki-sputter]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — PVD equipment.[^txt-09]
* Ohring, *Materials Science of Thin Films* — growth and
  microstructure of sputtered films.[^ohring-2002]

### Deep dive

* Tang et al. (TI), IEDM 1985 and *IEEE TED* 1987 — the titanium
  nitride local interconnect.[^tang-1985][^tang-1987]
* Haken and Holloway (TI), US 4,821,085 — the VLSI local interconnect
  structure.[^pat-li-ti-haken]
* Holloway et al. (TI), US 4,657,628 — the process for patterning
  local interconnects.[^pat-li-ti-holloway]
* Mann et al. (IBM), *IBM J. Res. Dev.* 1995 — silicides and local
  interconnections.[^mann-1995]
* White et al., IEDM 1992 — a damascene-stud local interconnect,
  the alternative structure.[^white-1992]
* Sundgren, *Thin Solid Films* 1985 — structure, resistivity and
  properties of TiN coatings.[^sundgren-1985]
* Berg and Nyberg, *Thin Solid Films* 2005 — reactive sputtering
  and its hysteresis.[^berg-2005]
* Petrov et al., *JVST A* 2003 — microstructural evolution during
  film growth.[^petrov-2003]
* Thornton, *J. Vac. Sci. Technol.* 1974 — the structure-zone
  diagram.[^thornton-1974]
* Blech, *J. Appl. Phys.* 1976 — electromigration in aluminium on
  TiN, the classic TiN-underlayer study.[^blech-1976]
* Boumerzoug et al., *MRS Proc.* 1997 — oxide on TiN and via contact
  resistance.[^boumerzoug-1997]

## Open questions

* The deposition conditions (pressure, nitrogen fraction,
  temperature, bias), whether a titanium adhesion layer precedes the
  TiN, and whether the film is IMP or conventionally sputtered are
  not public.
* The stack diagram gives the `li` bottom at 0.9361 µm and a level of
  1.0111 µm only 0.075 µm higher, against the 0.1 µm that its
  conductor label and the assumptions table give for
  `li`.[^pdk-04][^pdk-03] The 1.0111 µm leader line runs to the top of
  the LINT on the glass beside `li`, which the drawing (marked "not to
  scale") puts at the same height as the `li` top; we read the label
  as that LINT top (0.9361 + 0.075 µm), which fits every other label
  (our reading of the drawing).[^pdk-04]
* Whether the 12.8 Ω/sq figure is the as-deposited value or the
  value after the nitride cap and later anneals is not stated.

<!-- footnotes -->

[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram). <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance and capacitance tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README. <https://github.com/google/skywater-pdk>
[^ann-16]: T. Edwards (Efabless), *Introduction to the SkyWater PDK —
    The New Age of Open Source Silicon*, lecture slides, 2021-10-08
    (UC San Diego BENG 207).
    <https://isn.ucsd.edu/courses/beng207/lectures/Tim_Edwards_2021_slides.pdf>
[^ann-11]: SkyWater Technology / Efabless, *First Google-Sponsored MPW
    Shuttle Launched at SkyWater with 40 Open Source Community
    Submitted Designs*, press release, 2021-04-06.
    <https://skywatertechnology.com/press-releases/first-google-sponsored-mpw-shuttle-launched-at-skywater-with-40-open-source-community-submitted-designs>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^amat-endura]: Applied Materials, *Endura PVD*, product page.
    <https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report*.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^wiki-tin]: Wikipedia, *Titanium nitride*.
    <https://en.wikipedia.org/wiki/Titanium_nitride>
[^wiki-sputter]: Wikipedia, *Sputter deposition*.
    <https://en.wikipedia.org/wiki/Sputter_deposition>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007,
    ISBN 978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^ohring-2002]: M. Ohring, *Materials Science of Thin Films*, 2nd ed.,
    Academic Press, 2002.
    <https://doi.org/10.1016/B978-0-12-524975-1.X5000-9>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^tang-1985]: T. E. Tang, C.-C. Wei, R. A. Haken, T. C. Holloway,
    C.-F. Wan and M. A. Douglas, "VLSI local interconnect level using
    titanium nitride", *IEDM 1985 Technical Digest*, pp. 590–593.
    <https://doi.org/10.1109/IEDM.1985.191041>
[^tang-1987]: T. E. Tang, C.-C. Wei, R. A. Haken, T. C. Holloway,
    L. R. Hite and T. G. W. Blake, "Titanium nitride local interconnect
    technology for VLSI", *IEEE Transactions on Electron Devices*
    **34**(3), 682–688 (1987). <https://doi.org/10.1109/T-ED.1987.22980>
[^pat-li-ti-haken]: R. A. Haken and T. C. Holloway (Texas Instruments),
    *VLSI local interconnect structure*, US 4,821,085 A, filed
    1985-05-01, granted 1989-04-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4821085>
[^pat-li-ti-holloway]: T. C. Holloway, T. E. Tang, C.-C. Wei,
    R. A. Haken and D. A. Bell (Texas Instruments), *Process for
    patterning local interconnects*, US 4,657,628 A, filed 1986-03-07,
    granted 1987-04-14.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4657628>
[^mann-1995]: R. W. Mann, L. A. Clevenger, P. D. Agnello and
    F. R. White, "Silicides and local interconnections for
    high-performance VLSI applications", *IBM Journal of Research and
    Development* **39**(4), 403–417 (1995).
    <https://doi.org/10.1147/rd.394.0403>
[^white-1992]: White, Hill, Eslinger, Payne, Cote, Chen and Johnson,
    "Damascene stud local interconnect in CMOS technology", *IEDM 1992
    Technical Digest*, pp. 301–304.
    <https://doi.org/10.1109/IEDM.1992.307365>
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
[^blech-1976]: I. A. Blech, "Electromigration in thin aluminum films on
    titanium nitride", *Journal of Applied Physics* **47**(4), 1203–1208
    (1976). <https://doi.org/10.1063/1.322842>
[^boumerzoug-1997]: M. Boumerzoug, H. Xu, R. Bersin, P. Mascher and
    G. Balcaitis, "Removal of Titanium Oxide Grown on Titanium Nitride
    and Reduction of VIA Contact Resistance using a Modern Plasma
    Asher", *MRS Proceedings* **495** (1997).
    <https://doi.org/10.1557/PROC-495-345>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
