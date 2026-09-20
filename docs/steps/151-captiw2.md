(step-151)=
# Step 151 — CAPTIW2: Capacitor TiW deposition

| | |
|---|---|
| **Step number** | 151 of 171[^steps-sheet] |
| **Step code** | `CAPTIW2` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | {term}`BEOL` — MiM capacitors, metal 3–5, via 3–4 |
| **Previous step** | {ref}`CAPILD2 <step-150>` |
| **Next step** | {ref}`CAP2M <step-152>` |

## What this step is

`CAPTIW2` deposits the top-plate film of the second {term}`MiM capacitor`: a
blanket titanium–tungsten layer sputtered over the thin dielectric of
{ref}`CAPILD2 <step-150>`, which lies on the unpatterned metal-4 stack
of {ref}`WTIAL4 <step-149>`. For a few steps the wafer carries a
complete metal–insulator–metal sandwich across its whole surface: the
metal-4 conductor, the capacitor dielectric and this plate film. The
{ref}`CAP2M <step-152>` mask and {ref}`CAP2ME <step-153>` etch then
leave the film only where the layout draws `cap2m`, "MiM capacitor plate
over metal 4" (GDS 97:44),[^pdk-06] and {ref}`MM4 <step-154>` /
{ref}`MM4E <step-155>` afterwards cut the metal beneath into bottom
plates and the rest of the metal-4 wiring. The step list calls this
step "Capacitor TiW deposition";[^steps-sheet] a step name is not
evidence of a chemistry. The PDK calls the top plate
only "a thin conductor layer on top of the dielectric" and does not name
its material;[^pdk-07] this reference describes it as sputtered TiW
(inference: TiW is on SkyWater's PVD film list[^skw-01] and caps the
aluminium stacks on the 2013 Cypress description of this fab, though
not on the stack qualified in 2013–2014
({ref}`overview-metal-cap`), and the PDK's sheet resistance fits about
0.1 µm of it, as set out below). The step is the second-level repeat of
{ref}`CAPTIW1 <step-136>`.

The PDK gives this plate a "MiM2 top plate sheet resistance" of
5.8 Ω/sq (limits 4.8–6.8), the same as the first capacitor's
plate.[^pdk-07] Its thickness is not public, but the sheet resistance
bounds it as at {ref}`CAPTIW1 <step-136>`: for a sputtered Ti:W
resistivity of 50–100 µΩ·cm (textbook range for refractory barrier
films;[^txt-02] Hartsough's 1979 paper is titled *Resistivity of
bias-sputtered TiW films*; its values are not publicly
readable[^hartsough-1979]) a 5.8 Ω/sq sheet corresponds to
{math}`d = \rho / R_s \approx 0.09`–0.17 µm. We therefore read the plate
as roughly 0.1 µm of TiW (inference; our arithmetic), the same as the
first plate because the PDK calls the two constructions
"identical".[^pdk-07]

The plate has a different future from its twin one level down. It will
be buried in the via-4 dielectric of {ref}`NILD6 <step-156>`, 0.505 µm
thick above metal 4 on the PDK's stack diagram against 0.39 µm for via 3
above metal 3,[^pdk-04] and it will be contacted by a via-4 opening that
the rules allow only as a 0.800 µm square (via4.1, via4.3)[^pdk-periph]
— four times the width of the ordinary 0.200 µm via 3 (via3.1); the
rules also allow a 0.800 µm square via 3 inside `areaid.mt`
(via3.1a)[^pdk-periph] — which lands on the plate as the
{ref}`VIM4E <step-160>` etch finishes. In the PDK's stacked
cross-section the plate is joined upward to "M5 (plate 1)", the label
the drawing also gives the metal-5 shape joined through metal 4 to "M3
(plate 1)".[^pdk-07]

## Step category

`CAPTIW2` is a {ref}`Thin-film deposition <category-deposition>` step
of the *PVD, refractory metal* class; the category page's account of
magnetron sputtering applies, and {ref}`TIAL6 <step-112>` describes the
same material as the cap of the aluminium stacks. As at
{ref}`CAPTIW1 <step-136>`, what is specific is the substrate: a device
electrode sputtered onto a dielectric some 20–30 nm thick (our estimate
at {ref}`CAPILD2 <step-150>`). An argon {term}`sputter etch` pre-clean
of a few nanometres would remove a large fraction of that dielectric,
so on our reading it is omitted or made very light, and the film's
stress and deposition energy matter because the layer beneath is thin
(inference from the geometry).

## Why this step exists

* **A capacitor needs a second plate.** The dielectric alone is an
  insulator on metal 4; the plate makes it a capacitor. Because the top
  plate is deposited over the whole wafer and patterned by its own mask
  *before* the metal beneath is etched, the plate edge sits on a flat,
  continuous dielectric and the capacitance is set by the drawn `cap2m`
  area plus a periphery term — `CMIM2A` 2 fF/µm² and `CMIM2P`
  0.19 fF/µm.[^pdk-07] This is the top-plate-first order of the Newport
  Fab patent, which deposits dielectric and top-plate metal on
  unpatterned interconnect metal;[^pat-mim-newportfab] Kar-Roy et al.
  and Babcock et al. describe PECVD-nitride MiMs in aluminium back
  ends.[^kar-roy-1999][^babcock-2001]
* **Why TiW, on this reading.** The plate must sputter at low temperature onto a
  dielectric without reacting with it, etch with high {term}`selectivity`
  to that dielectric ({ref}`CAP2ME <step-153>`), survive the chlorine
  metal etch under resist and serve as the stop for the fluorocarbon via
  etch, and already be in the fab. TiW caps the aluminium levels on
  the 2013 Cypress description of this fab but not on the stack
  qualified in 2013–2014 ({ref}`TIAL6 <step-112>`,
  {ref}`overview-metal-cap`), and "TiW" is on SkyWater's PVD
  list;[^skw-01] it is a barrier whose properties Nicolet reviewed and Ghate
  et al. established;[^nicolet-1978][^ghate-1978] Liu and Kuo showed
  that TiW etches by reactive-ion etching in CF₄-based
  plasmas,[^liu-2007-tiw] Danzl and McLaurin removed a TiW cap from
  aluminium pads in hydrogen peroxide,[^danzl-1997] and the fab's metal
  etchers are qualified for it ("Lam 9600, Al, TiW, TiN, Pt"[^skw-01]).
  The published alternatives include the titanium nitride, tantalum
  nitride or aluminium top plates of the Newport Fab
  patent,[^pat-mim-newportfab] the TaN, TiN, Al, Cu, Ru or Ir plates of
  Freescale's[^pat-mim-freescale] and TI's aluminium-capped Ta/TaN top
  electrode for a copper back end ("ALCAP").[^pat-mim-ti-alcap]
* **Series resistance of a stacked pair.** The plate's 5.8 Ω/sq[^pdk-07]
  sits in series with the capacitor; the PDK's stacked cross-section
  shows more than one via shape on each plate (our reading of the
  artwork; the drawing labels the vias only as "Via3" and
  "Via4"[^pdk-07]), the layout by which the
  PDK's sub-circuit model — which "accounts for the parasitic contact
  resistance"[^pdk-07] — keeps that resistance small (inference from
  the drawing). Ng et al. review MiM integration choices in Al–Cu and
  copper back ends.[^ng-2005]
* **Stress on a thin dielectric.** Sputtered W-rich films are
  compressive or tensile according to pressure and composition —
  Thornton's structure-zone model[^thornton-1974] and Dirks, Wolters and
  De Veirman's study of the columnar microstructure of sputtered W and
  W–Ti(N)[^dirks-1992] describe the dependence — and a stressed plate
  can crack or lift a thin dielectric; the deposition pressure is chosen
  for low stress as well as low resistivity (industry practice[^ohring-2002]).

Without `CAPTIW2` the `cap2m` pattern would define nothing, and the
second capacitor's top terminal would not exist.

## How it is typically performed

An industry-generic MiM top-plate deposition for a 200 mm aluminium
back end (SKY130's recipe is not public); the sequence is that of
{ref}`CAPTIW1 <step-136>`.

1. **{term}`Queue time <queue time>`.** The dielectric surface should not sit long in air;
   moisture and hydrocarbons at the interface raise leakage (industry
   practice[^txt-05]). SkyWater's PECVD and PVD tools are listed
   separately,[^skw-01] so on our reading the transfer is governed by a
   queue-time rule rather than made under vacuum.
2. **Degas, no or minimal sputter etch.** A vacuum bake in the
   {term}`PVD` cluster's {term}`degas` chamber; the argon pre-clean
   SkyWater lists as "Sputter etch, degas"[^skw-01] is, we infer,
   omitted or made very light.
3. **Sputtering.** DC magnetron sputtering from a Ti:W target — 10 wt.%
   Ti is the standard composition[^pat-tiw-hitachi] — in argon at a few
   mTorr, with the wafer well below the aluminium limit
   (industry-typical[^txt-02]); Hill and Dirks et al. describe how
   sputtered Ti–W and W–Ti(N) films depend on the deposition
   conditions.[^hill-1980][^dirks-1992]
4. **Thickness.** Of the order of 0.1 µm, from the 5.8 Ω/sq of the
   PDK[^pdk-07] and the resistivity range above (inference). A thicker
   plate lowers the series resistance but lengthens the
   {ref}`CAP2ME <step-153>` etch and raises the step that the
   {ref}`MM4 <step-154>` resist must cover.
5. **Metrology.** Sheet resistance by {term}`four-point probe` on
   monitors (the quantity the PDK's MiM2 top-plate value
   describes[^pdk-07]); thickness by XRF; stress by wafer bow;
   reflectivity for the {ref}`CAP2M <step-152>` exposure; particles.
   Capacitance, leakage and breakdown are measured on finished
   structures at {term}`e-test`.

## Machines typically used

* **{ref}`PVD cluster tool <machine-pvd-cluster-tool>` with a Ti:W chamber**, 200 mm: Applied Materials
  Endura,[^amat-endura] Novellus INOVA, Ulvac and Anelva sputtering
  systems ({ref}`category-deposition`).
* **Degas chamber** on the same platform.
* **{ref}`Four-point probe <machine-sheet-resistance-metrology>`**, **{ref}`XRF <machine-film-thickness-metrology>`**, **stress gauge**, **reflectometer**.

## Machines likely used at SkyWater

* **AMAT PVD Metal platform, TiW chamber.** SkyWater lists "AMAT PVD
  Metal" with "TiW" among its films.[^skw-01] Strength: **strong** for
  the vendor and the material; the platform model (Endura is the 200 mm-era
  Applied Materials platform[^amat-endura]) and the use of the chamber
  that caps the aluminium stacks are **inferences**.
* **Lam 9600 / Lam 2300 Versys** metal etchers qualified for
  "TiW"[^skw-01] corroborate that TiW is a patterned film in this fab
  (used at {ref}`CAP2ME <step-153>`).

## Resources required

* **Ti:W {ref}`sputter target <material-sputter-targets>`** (10 wt.% Ti[^pat-tiw-hitachi]); SkyWater's filings
  name Honeywell Electronic Materials (2021 S-1 and fiscal 2023 10-K) and JX
  Metals (fiscal 2023 10-K) as sputter-target suppliers.[^sec-01][^sec-02]
* **{ref}`Argon <material-process-gases>`** for sputtering; **nitrogen** for venting.
* **{ref}`Chamber shields <material-hardware-consumables>` and clamp/chuck consumables**; **{ref}`monitor wafers <material-substrates>`**
  for sheet resistance, stress and particles.

## Related steps and cross-references

* Previous: {ref}`CAPILD2 <step-150>` (the dielectric it covers). Next:
  {ref}`CAP2M <step-152>` (the top-plate mask), then
  {ref}`CAP2ME <step-153>` (the etch that leaves the plates).
* The bottom plate beneath: {ref}`WTIAL4 <step-149>`, patterned later
  at {ref}`MM4 <step-154>` / {ref}`MM4E <step-155>`.
* The via that lands on the finished plate: {ref}`VIM4E <step-160>`;
  the polish that must not reach it: {ref}`CMPM4 <step-157>`.
* The first capacitor's plate: {ref}`CAPTIW1 <step-136>`; the same film
  as a cap on the aluminium stacks: {ref}`TIAL6 <step-112>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

**Related patents.**

* {ref}`Titanium-tungsten target material for sputtering and manufacturing method therefor <patent-gp27460980>` — US 5,160,534 A (1990)
* {ref}`Method for fabrication of an MIM capacitor and related structure <patent-gp24897586>` — US 6,430,028 B1 (2000)
* {ref}`Method for fabricating a high density composite MIM capacitor with flexible routing in semiconductor dies <patent-gp32851038>` — US 7,078,310 B1 (2003)
* {ref}`Metal insulator metal (MIM) capacitor fabrication with sidewall spacers and aluminum cap (ALCAP) top electrode <patent-gp35732850>` — US 7,250,334 B2 (2004)
* {ref}`MIM capacitor in a semiconductor device and method therefor <patent-gp37568077>` — US 7,375,002 B2 (2005)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, *Device Details* — "thin conductor layer on top of the
  dielectric"; MiM2 top plate 5.8 Ω/sq (4.8–6.8); `CMIM2A`, `CMIM2P`;
  the stacked `cap_mim` cross-section.[^pdk-07]
* SkyWater PDK, *Layers Reference* — `cap2m` 97:44.[^pdk-06]
* SkyWater PDK, *Process stack diagram* — `cap2m` between `metal4` and
  `metal5`; via4 0.505 µm; via3 0.39 µm.[^pdk-04]
* SkyWater PDK, *Periphery rules* — via4.1 and via4.3.[^pdk-periph]
* SkyWater, *Facilities & Capabilities* — "AMAT PVD Metal … TiW";
  "Sputter etch, degas"; TiW on the metal etchers.[^skw-01]
* SkyWater, Form S-1 and 10-K — sputter-target suppliers.[^sec-01][^sec-02]
* Hitachi Metals, US 5,160,534 — Ti:W target composition.[^pat-tiw-hitachi]
* Applied Materials, *Endura PVD*.[^amat-endura]

### High-level understanding

* Wikipedia, *Sputter deposition*, *Capacitor*.[^wiki-sputter][^wiki-capacitor]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  sputtering and refractory barrier films.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — passive devices
  in the deep-submicron back end.[^txt-05]
* Ohring, *Materials Science of Thin Films* — film growth, stress and
  structure.[^ohring-2002]

### Deep dive

* Ghate, Blair, Fuller and McGuire (TI), *Thin Solid Films* 1978 — Ti:W
  barrier metallisation for integrated circuits.[^ghate-1978]
* Nicolet, *Thin Solid Films* 1978 — diffusion barriers in thin films
  reviewed.[^nicolet-1978]
* Hill, *Thin Solid Films* 1980 — magnetron-sputtered Ti–W
  films.[^hill-1980]
* Hartsough, *Thin Solid Films* 1979 — the resistivity of bias-sputtered
  TiW.[^hartsough-1979]
* Dirks, Wolters and De Veirman (Philips), *Thin Solid Films* 1992 —
  columnar microstructure of sputtered W and W–Ti(N).[^dirks-1992]
* Thornton, *JVST* 1974 — the structure-zone model behind the pressure
  choice.[^thornton-1974]
* Liu and Kuo, *J. Electrochem. Soc.* 2007 — reactive-ion etching of TiW
  films, which makes the plate patternable.[^liu-2007-tiw]
* Danzl and McLaurin, IEMT 1997 — peroxide removal of a TiW cap from
  aluminium bond pads.[^danzl-1997]
* Kar-Roy et al., IITC 1999, and Babcock et al., *IEEE EDL* 2001 —
  PECVD-nitride MiMs in aluminium back ends.[^kar-roy-1999][^babcock-2001]
* Ng et al., *IEEE TED* 2005 — MiM integration in Al–Cu and copper back
  ends reviewed.[^ng-2005]
* Kar-Roy and Racanelli (Newport Fab), US 6,430,028; Roberts and Huffman
  (Freescale), US 7,375,002; Crenshaw et al. (TI), US 7,250,334 —
  top-plate constructions from three assignees.[^pat-mim-newportfab][^pat-mim-freescale][^pat-mim-ti-alcap]
* Kar-Roy, Racanelli and Kempf (Newport Fab), US 7,078,310 — the top
  plate of a stacked, parallel-connected MiM pair.[^pat-mim-stack-newportfab]

## Open questions

* The plate's thickness, composition (Ti fraction, any nitrogen) and
  deposition conditions are not public; ~0.1 µm is our estimate from the
  PDK's 5.8 Ω/sq[^pdk-07] with an assumed resistivity, and the reading
  that it repeats {ref}`CAPTIW1 <step-136>` rests on the PDK calling the
  constructions identical.
* Whether a pre-clean precedes the deposition, and the queue-time limit
  between dielectric and plate, are not public.
* Whether the plate is a single TiW film or carries a thin cap is not
  public; neither is whether the metal-4 cap beneath the dielectric is
  TiW or TiN, which bears on the plate material and on what
  {ref}`CAP2ME <step-153>` can stop on
  ({ref}`overview-metal-cap`).
* The PDK publishes no `cap2m` rules, so the plate's enclosure by
  metal 4 and of via 4 are not known;[^pdk-periph] the level
  inconsistencies in the PDK's MiM entries are set out at
  {ref}`CAPILD2 <step-150>`.
* The 0.1 µm plate thickness follows from a textbook resistivity range
  that cannot be checked from a public abstract; a factor of two in
  resistivity is a factor of two in thickness.

<!-- footnotes -->

[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (MiM capacitors),
    SkyWater SKY130 PDK documentation, and the `cap_mim` cross-section
    drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/cap_mim/cross-section-cap_mim.svg>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
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
[^pat-tiw-hitachi]: Hitachi Metals, *Titanium-tungsten target material
    for sputtering and manufacturing method therefor*, US 5,160,534 A,
    granted 1992-11-03. <https://patents.google.com/patent/US5160534A/en>
[^wiki-sputter]: Wikipedia, *Sputter deposition*.
    <https://en.wikipedia.org/wiki/Sputter_deposition>
[^wiki-capacitor]: Wikipedia, *Capacitor*.
    <https://en.wikipedia.org/wiki/Capacitor>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^ohring-2002]: M. Ohring, *Materials Science of Thin Films*, 2nd ed.,
    Academic Press, 2002.
    <https://doi.org/10.1016/B978-0-12-524975-1.X5000-9>
[^ghate-1978]: P. B. Ghate, J. C. Blair, C. R. Fuller and G. E.
    McGuire, "Application of Ti:W barrier metallization for integrated
    circuits", *Thin Solid Films* **53**(2), 117–128 (1978).
    <https://doi.org/10.1016/0040-6090(78)90024-X>
[^nicolet-1978]: M.-A. Nicolet, "Diffusion barriers in thin films",
    *Thin Solid Films* **52**(3), 415–443 (1978).
    <https://doi.org/10.1016/0040-6090(78)90184-0>
[^hill-1980]: M. L. Hill, "Magnetron-sputtered Ti-W films", *Thin
    Solid Films* **72**(2), 349–350 (1980).
    <https://doi.org/10.1016/0040-6090(80)90017-6>
[^hartsough-1979]: L. D. Hartsough, "Resistivity of bias-sputtered TiW
    films", *Thin Solid Films* **64**(1), 17–23 (1979).
    <https://doi.org/10.1016/0040-6090(79)90536-4>
[^dirks-1992]: A. G. Dirks, R. A. M. Wolters and A. E. M. De Veirman,
    "Columnar microstructures in magnetron-sputtered refractory metal
    thin films of tungsten, molybdenum and W-Ti-(N)", *Thin Solid
    Films* **208**(2), 181–188 (1992).
    <https://doi.org/10.1016/0040-6090(92)90640-W>
[^thornton-1974]: J. A. Thornton, "Influence of apparatus geometry and
    deposition conditions on the structure and topography of thick
    sputtered coatings", *Journal of Vacuum Science and Technology*
    **11**(4), 666–670 (1974). <https://doi.org/10.1116/1.1312732>
[^liu-2007-tiw]: G. Liu and Y. Kuo, "Reactive Ion Etching of Titanium
    Tungsten Thin Films", *Journal of The Electrochemical Society*
    **154**(7), H653 (2007). <https://doi.org/10.1149/1.2737631>
[^danzl-1997]: R. B. Danzl and A. McLaurin, "The use of concentrated
    hydrogen peroxide for the removal of a TiW ARC from aluminum bond
    pads", *Proc. Twenty-First IEEE/CPMT International Electronics
    Manufacturing Technology Symposium (IEMT 1997)*, pp. 99–104.
    <https://doi.org/10.1109/IEMT.1997.626884>
[^kar-roy-1999]: A. Kar-Roy, C. Hu, M. Racanelli, C. A. Compton,
    P. Kempf, G. Jolly, P. N. Sherman, J. Zheng, Z. Zhang and A. Yin,
    "High density metal insulator metal capacitors using PECVD nitride
    for mixed signal and RF circuits", *Proc. IEEE 1999 International
    Interconnect Technology Conference (IITC)*, pp. 245–247.
    <https://doi.org/10.1109/IITC.1999.787134>
[^babcock-2001]: J. A. Babcock, S. G. Balster, A. Pinto, C. Dirnecker,
    P. Steinmann, R. Jumpertz and B. El-Kareh, "Analog characteristics
    of metal-insulator-metal capacitors using PECVD nitride
    dielectrics", *IEEE Electron Device Letters* **22**(5), 230–232
    (2001). <https://doi.org/10.1109/55.919238>
[^ng-2005]: C. H. Ng, C.-S. Ho, S.-F. S. Chu and S.-C. Sun, "MIM
    Capacitor Integration for Mixed-Signal/RF Applications", *IEEE
    Transactions on Electron Devices* **52**(7), 1399–1409 (2005).
    <https://doi.org/10.1109/TED.2005.850642>
[^pat-mim-newportfab]: A. Kar-Roy and M. Racanelli (Newport Fab, LLC),
    *Method for fabrication of an MIM capacitor and related structure*,
    US 6,430,028 B1, filed 2000-11-22, granted 2002-08-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6430028>
[^pat-mim-freescale]: D. R. Roberts and G. L. Huffman (Freescale
    Semiconductor), *MIM capacitor in a semiconductor device and method
    therefor*, US 7,375,002 B2, filed 2005-06-28, granted 2008-05-20.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7375002>
[^pat-mim-ti-alcap]: D. L. Crenshaw, B. L. Williams, A. Tsao,
    H. Shichijo, S. S. Papa Rao, K. D. Brennan and S. A. Lytle (Texas
    Instruments), *Metal insulator metal (MIM) capacitor fabrication
    with sidewall spacers and aluminum cap (ALCAP) top electrode*,
    US 7,250,334 B2, filed 2004-07-31, granted 2007-07-31.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7250334>
[^pat-mim-stack-newportfab]: A. Kar-Roy, M. Racanelli and P. Kempf
    (Newport Fab, LLC), *Method for fabricating a high density composite
    MIM capacitor with flexible routing in semiconductor dies*,
    US 7,078,310 B1, filed 2004-05-19, granted 2006-07-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7078310>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
