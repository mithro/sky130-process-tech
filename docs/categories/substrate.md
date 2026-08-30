(category-substrate)=
# Substrate / starting material

## What this class of step does

Every wafer that enters the fab begins as a bare, polished disc of
single-crystal silicon bought from a wafer vendor. The "starting
material" step is not a process performed in the fab so much as a
*specification*: it fixes the diameter, thickness, crystal orientation,
doping type and resistivity, oxygen content, flatness and cleanliness
of the silicon on which every later step depends. Once the wafer lot is
released into the line, nothing can change the bulk properties of the
substrate, so the choice is made once, at process design time, and then
audited on every incoming lot.

More precisely, a starting-material specification for a 130 nm-era
CMOS process on 200 mm wafers defines:

* **Diameter and thickness.** 200 mm wafers are 725 µm thick and were
  introduced in 1992; wafers of 200 mm and above carry a single small
  notch, rather than flats, to indicate crystal orientation
  ([Wikipedia: Wafer (electronics)][wiki-wafer]). The ITRS 2001
  front-end-processes chapter notes that "200 mm will still be
  prevalent through the 130 nm node" even though 300 mm was then being
  phased in ([ITRS 2001, Front End Processes][itrs2001-fep]).
* **Crystal orientation.** Orientation is given by the Miller index,
  "(100) or (111) faces being the most common for silicon"
  ([Wikipedia: Wafer (electronics)][wiki-wafer]); CMOS uses (100)
  because it gives the lowest density of interface states at the
  Si/SiO₂ interface and therefore the best gate oxide
  (Plummer, Deal and Griffin, ch. 3).
* **Doping type and resistivity.** Wafers carry "an initial impurity
  doping concentration between 10¹³ and 10¹⁶ atoms per cm³ of boron,
  phosphorus, arsenic, or antimony" ([Wikipedia: Wafer
  (electronics)][wiki-wafer]). Bulk CMOS processes use lightly
  boron-doped p-type material, typically in the 1–20 Ω·cm range, or a
  lightly doped p-type {term}`epitaxial layer` on a heavily doped p⁺
  substrate (a "p/p⁺ epi" wafer) to suppress latch-up
  (Plummer, Deal and Griffin, ch. 2 and 3; Wolf and
  Tauber, ch. 1).
* **Oxygen and gettering.** {term}`CZ` silicon contains dissolved
  interstitial oxygen from the quartz crucible, typically of order
  10¹⁷–10¹⁸ cm⁻³, which can be precipitated deliberately during the
  early high-temperature steps to form an internal {term}`gettering`
  sink beneath a defect-free "denuded zone" at the surface
  (Plummer, Deal and Griffin, ch. 3 and 4).
* **Surface quality.** Site flatness, particle counts, surface metal
  contamination and bulk iron are the key incoming-quality metrics; the
  ITRS 2001 starting-materials table (Table 49a) tabulates their
  targets node by node ([ITRS 2001, Front End Processes][itrs2001-fep]).

The formal definitions of all these parameters are in
SEMI M1, *Specification for Polished Single Crystal Silicon Wafers*
([SEMI M1][semi-m1]), with SEMI M62 covering epitaxial wafers
([SEMI M62][semi-m62]) and SEMI M8 covering the cheaper test wafers used
for tool monitoring ([SEMI M8][semi-m8]).

The SKY130 documentation shows a layer set with an n-well, a deep
n-well and p-substrate contacts and states that the process runs on
200 mm wafers; from this we infer that the starting material is a
p-type 200 mm wafer, as is normal for a twin-well bulk CMOS process,
but the resistivity and whether an epitaxial layer is used are not
stated publicly ([SKY130 PDK documentation][pdk]).

## Physics and engineering background

### Crystal growth

Almost all IC wafers are cut from boules grown by the Czochralski
method, in which a seed crystal is dipped into molten silicon (melting
point 1414 °C) held in a quartz crucible and slowly withdrawn while
rotating, so that the melt freezes onto the seed as one continuous
crystal ([Wikipedia: Czochralski method][wiki-cz]). The dopant is added
to the melt; because the segregation coefficient of most dopants is
less than one, the crystal grows progressively more heavily doped from
seed to tail, and the resistivity is specified as a range rather than a
single value (Plummer, Deal and Griffin, ch. 3). Float-zone
growth, which avoids the crucible and gives much lower oxygen, is used
for power and detector devices but is not economical at 200 mm for CMOS
([Wikipedia: Float-zone silicon][wiki-fz]).

The boule is ground to diameter, notched, sliced with a wire saw,
lapped, edge-rounded, chemically etched to remove saw damage, and
finally polished on one side by {term}`CMP` to a mirror finish with
sub-nanometre roughness, then cleaned and packed
([Wikipedia: Wafer (electronics)][wiki-wafer]).

### Orientation, dopant and resistivity

The (100) surface has the lowest interface-trap density after
oxidation, which is why it displaced (111) for MOS devices; the notch
on a 200 mm wafer lies along a ⟨110⟩ direction so that the die edges,
and therefore the cleave planes, are aligned with the crystal
(Plummer, Deal and Griffin, ch. 3). Boron is the p-type
dopant of choice because it has a high solid solubility and a
segregation coefficient close to 0.8, giving a uniform axial profile;
the resistivity is chosen as a compromise between latch-up immunity
and well-implant dose (a lightly doped substrate is simply overwritten
by the well implants of {ref}`category-implant`).

### Epitaxial wafers

A p/p⁺ epitaxial wafer has a few micrometres of lightly doped silicon
grown by {term}`CVD` from a chlorosilane (SiHCl₃ or SiH₂Cl₂) at
1000–1150 °C on a heavily boron-doped (≈0.01 Ω·cm) substrate. The
heavily doped bulk shorts out the parasitic p-n-p-n thyristor that
causes latch-up and also getters metals, at the cost of a more
expensive wafer and a need to control autodoping and up-diffusion of
boron from the substrate during later hot steps
(Plummer, Deal and Griffin, ch. 3 and 14; Wolf and
Tauber, ch. 5). Many 130 nm-era logic processes used epi
wafers, and many did not; publicly, SKY130 does not say which.

### Oxygen, precipitates and gettering

Interstitial oxygen in CZ silicon is supersaturated at device
processing temperatures. A high-temperature step drives oxygen out of
the surface region (out-diffusion), a low-temperature step nucleates
precipitates in the bulk, and subsequent hot steps grow them. The
resulting SiO₂ precipitates and their associated dislocation loops trap
fast-diffusing metals such as Fe, Cu and Ni far from the transistors
("intrinsic gettering"), while the denuded zone near the surface stays
defect-free. Because the thermal budget of a 130 nm process is small,
wafer vendors increasingly supply material whose precipitation
behaviour has been pre-set by the crystal-growth conditions
(Plummer, Deal and Griffin, ch. 4; ITRS 2001 FEP
[itrs2001-fep]). Backside damage or polysilicon films provide
alternative "extrinsic" gettering ([Wikipedia: Getter][wiki-getter]).

### Flatness and particles

Site flatness matters because a scanner's depth of focus at the
130 nm node is only a few hundred nanometres (see
{ref}`category-lithography`). ITRS 2001 states that "for the 130 nm
technology node to the end of optical lithography, scanners will be
utilized with rectangular fields (nominally 25 mm x 32 mm for 4X
scanners)" and that the site-flatness metric should match that field
([ITRS 2001, Front End Processes][itrs2001-fep]). Incoming inspection
therefore measures flatness site by site, counts localised light
scatterers (particles and crystal-originated pits) with a laser
surface scanner, and checks surface metals.

## Typical equipment

The substrate category has no process tool in the fab itself; the
"equipment" is at the wafer vendor and in incoming quality control:

* **Crystal pullers** (CZ furnaces) and **wire saws**, **lappers**,
  **edge grinders** and **polishers** at the wafer maker. The major
  200 mm suppliers of the era were Shin-Etsu Handotai, SUMCO (formed
  from Sumitomo and Mitsubishi Materials silicon), MEMC (later
  SunEdison and now part of GlobalWafers), Wacker Siltronic ([Wikipedia: Shin-Etsu Chemical][wiki-seh];
  [Wikipedia: SUMCO][wiki-sumco]; [Wikipedia: SunEdison][wiki-memc];
  [Wikipedia: Siltronic][wiki-siltronic];
  [Wikipedia: GlobalWafers][wiki-gw]).
* **Epitaxial reactors** if epi wafers are specified: single-wafer
  lamp-heated reactors such as the ASM Epsilon series and the Applied
  Materials Centura Epi, or the older batch barrel reactors
  ([Wikipedia: ASM International][wiki-asm];
  [Wikipedia: Applied Materials][wiki-amat]).
* **Incoming inspection**: laser surface scanners (KLA-Tencor Surfscan
  family), capacitive flatness gauges (ADE), four-point-probe
  resistivity mapping, and FTIR for oxygen content
  ([Wikipedia: KLA Corporation][wiki-kla]).

## Typical consumables

* Polished prime wafers to SEMI M1 ([SEMI M1][semi-m1]); epitaxial
  wafers to SEMI M62 ([SEMI M62][semi-m62]).
* Test and monitor wafers to SEMI M8 ([SEMI M8][semi-m8]), and
  reclaimed wafers to SEMI M38 for non-critical tool monitoring.
* Wafer carriers (open cassettes or SMIF pods at 200 mm), which must
  not shed particles or outgas.

## Steps in this category

| Step | Code | Name |
|------|------|------|
| 1 | {ref}`SMAT <step-001>` | Starting material |

## References

### Cross-check

* SEMI M1, *Specification for Polished Single Crystal Silicon Wafers*,
  SEMI. <https://store-us.semi.org/products/m00100-semi-m1-specification-for-polished-single-crystal-silicon-wafers>
* SEMI M8, *Specification for Polished Monocrystalline Silicon Test
  Wafers*, SEMI. <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
* SEMI M62, *Specification for Silicon Epitaxial Wafers*, SEMI.
  <https://store-us.semi.org/products/m06200-semi-m62-specification-for-silicon-epitaxial-wafers>
* *International Technology Roadmap for Semiconductors 2001 Edition:
  Front End Processes*, SIA/ITRS, 2001 (Table 49a, starting
  materials). <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
* SkyWater Technology / Google, *SkyWater SKY130 PDK documentation*.
  <https://skywater-pdk.readthedocs.io/en/main/>

### High-level

* Wikipedia, "Wafer (electronics)".
  <https://en.wikipedia.org/wiki/Wafer_(electronics)>
* Wikipedia, "Czochralski method".
  <https://en.wikipedia.org/wiki/Czochralski_method>
* Wikipedia, "Float-zone silicon".
  <https://en.wikipedia.org/wiki/Float-zone_silicon>
* Wikipedia, "Monocrystalline silicon".
  <https://en.wikipedia.org/wiki/Monocrystalline_silicon>
* Wikipedia, "Miller index".
  <https://en.wikipedia.org/wiki/Miller_index>
* Wikipedia, "Epitaxy". <https://en.wikipedia.org/wiki/Epitaxy>
* Wikipedia, "Getter". <https://en.wikipedia.org/wiki/Gettering>
* Wikipedia, "Latch-up". <https://en.wikipedia.org/wiki/Latch-up>
* J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
  Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
  2000, ISBN 978-0-13-085037-9, ch. 3 ("Crystal Growth, Wafer
  Fabrication and Basic Properties of Silicon Wafers") and ch. 4
  ("Semiconductor Manufacturing — Clean Rooms, Wafer Cleaning and
  Gettering").
* S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI Era,
  Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4, ch. 1 ("Silicon: Single Crystal Growth and
  Wafer Preparation") and ch. 5 ("Silicon Epitaxial Growth").
* M. Quirk and J. Serda, *Semiconductor Manufacturing Technology*,
  Prentice Hall, 2001, ISBN 978-0-13-081520-0, ch. 4.
  <https://www.pearson.com/en-us/subject-catalog/p/semiconductor-manufacturing-technology/P200000003179/9780130815200>
* H. Xiao, *Introduction to Semiconductor Manufacturing Technology*,
  2nd ed., SPIE Press, 2012, ch. 4. <https://doi.org/10.1117/3.924283>

### Deep dive

* Wikipedia, "SkyWater Technology" (fab history and 200 mm capacity).
  <https://en.wikipedia.org/wiki/SkyWater_Technology>
* K. E. Bean, "Anisotropic etching of silicon", *IEEE Transactions on
  Electron Devices* **25**(10), 1185–1193 (1978), for crystal-plane
  behaviour of silicon. <https://doi.org/10.1109/T-ED.1978.19250>
* Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
  Manufacturing Technology*, 2nd ed., CRC Press, 2007, ch. 1–3 on
  silicon materials. <https://doi.org/10.1201/9781420017663>

[wiki-wafer]: https://en.wikipedia.org/wiki/Wafer_(electronics)
[wiki-cz]: https://en.wikipedia.org/wiki/Czochralski_method
[wiki-fz]: https://en.wikipedia.org/wiki/Float-zone_silicon
[wiki-getter]: https://en.wikipedia.org/wiki/Gettering
[wiki-seh]: https://en.wikipedia.org/wiki/Shin-Etsu_Chemical
[wiki-sumco]: https://en.wikipedia.org/wiki/SUMCO
[wiki-memc]: https://en.wikipedia.org/wiki/MEMC_Electronic_Materials
[wiki-siltronic]: https://en.wikipedia.org/wiki/Siltronic
[wiki-gw]: https://en.wikipedia.org/wiki/GlobalWafers
[wiki-asm]: https://en.wikipedia.org/wiki/ASM_International
[wiki-amat]: https://en.wikipedia.org/wiki/Applied_Materials
[wiki-kla]: https://en.wikipedia.org/wiki/KLA_Corporation
[itrs2001-fep]: https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf
[semi-m1]: https://store-us.semi.org/products/m00100-semi-m1-specification-for-polished-single-crystal-silicon-wafers
[semi-m62]: https://store-us.semi.org/products/m06200-semi-m62-specification-for-silicon-epitaxial-wafers
[semi-m8]: https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers
[pdk]: https://skywater-pdk.readthedocs.io/en/main/
