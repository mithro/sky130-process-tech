(step-136)=
# Step 136 — CAPTIW1: Capacitor TiW deposition

| | |
|---|---|
| **Step number** | 136 of 171 |
| **Step code** | `CAPTIW1` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | BEOL — MiM capacitors, metal 3–5, via 3–4 |
| **Previous step** | {ref}`CAPILD <step-135>` |
| **Next step** | {ref}`CAPM <step-137>` |

## What this step is

`CAPTIW1` deposits the *top plate* of the first {term}`MiM capacitor`: a
blanket titanium–tungsten film sputtered over the thin oxynitride of
{ref}`CAPILD <step-135>`, which itself lies on the unpatterned
metal-3 stack of {ref}`WTIAL3 <step-134>`. At this moment the wafer
carries, from the bottom, the metal-3 conductor (Ti/Al–Cu/TiW on the
public description of the S8 metal stacks[^cyp-qtp-113005]), the
capacitor dielectric and this TiW — a complete
metal–insulator–metal sandwich across the whole wafer. The
{ref}`CAPM <step-137>` mask and {ref}`CAPME <step-138>` etch then
leave the TiW only where the layout draws `capm`, "MiM capacitor
plate over metal 3" (GDS 89:44),[^pdk-06] and {ref}`MM3 <step-139>` /
{ref}`MM3E <step-140>` afterwards cut the metal beneath into the
bottom plates and the rest of the metal-3 wiring. The PDK's device
page calls the top plate "a thin conductor layer on top of the
dielectric" and gives its {term}`sheet resistance`, `RSCAPM`, as
5.8 Ω/sq (limits 4.8–6.8);[^pdk-07] the "1" in the step code
distinguishes it from the second plate, {ref}`CAPTIW2 <step-151>`.

The film's thickness is not public, but the sheet resistance bounds
it. Sputtered Ti:W has a resistivity of some tens of µΩ·cm — Ghate et
al. and Hill characterised the films[^ghate-1978][^hill-1980] — and
for an industry-typical 50–100 µΩ·cm (textbook range for refractory
barrier films[^txt-02]) a 5.8 Ω/sq sheet corresponds to
{math}`d = \rho / R_s \approx 0.09`–0.17 µm. We therefore read the
top plate as roughly 0.1 µm of TiW (inferred; our arithmetic), several
times thicker than the 300 Å TiW cap of the metal stacks[^cyp-qtp-113005]
and several times thicker than the dielectric beneath it. Its role is
electrical (a low-resistance plate, in series with the capacitor in
the PDK's sub-circuit model, which "accounts for the parasitic contact
resistance"[^pdk-07])
and mechanical: it must survive the {ref}`CAPME <step-138>` etch as a
plate, the {ref}`MM3E <step-140>` aluminium etch as a masked island,
the {ref}`NILD5 <step-141>` deposition and {ref}`CMPM3 <step-142>`
polish above it, and serve as the landing pad on which
{ref}`VIM3E <step-145>` stops when a `via3` contacts the top plate.

## Step category

`CAPTIW1` is a {ref}`Thin-film deposition <category-deposition>` step
of the *PVD, refractory metal* class; the category page's account of
magnetron sputtering and of Ti:W films applies, and
{ref}`TIAL6 <step-112>` describes the same material as the cap of the
aluminium stacks. What is specific here is that the film is a device
electrode deposited on a 20–30 nm dielectric ({ref}`CAPILD <step-135>`)
rather than on metal: the sputter pre-clean that normally precedes a
PVD film is, we infer, omitted or kept very light, because a few
nanometres of argon {term}`sputter etch` would remove a large fraction
of the capacitor dielectric, and the film's stress and its deposition energy matter
because the dielectric beneath is thin enough to be damaged by them
(inference from the geometry; the same concern shapes the TiN top
plates of the published processes[^kar-roy-1999][^pat-mim-newportfab]).

## Why this step exists

* **A capacitor needs a second plate.** The oxynitride alone is a
  dielectric on a metal; the TiW makes it a capacitor. Because the
  top plate is deposited over the whole wafer and patterned by its
  own mask *before* the metal beneath is etched, the plate edge sits
  on a flat, continuous dielectric and the capacitance is set by the
  drawn `capm` area plus a periphery term — the `CMIMA` 2 fF/µm² and
  `CMIMP` 0.19 fF/µm of the PDK.[^pdk-07] This is the
  top-plate-first construction of the Newport Fab and Freescale
  patents,[^pat-mim-newportfab][^pat-mim-freescale] and of the Al-BEOL MiM
  processes Kar-Roy et al. and Babcock et al. describe.[^kar-roy-1999][^babcock-2001]
* **Why TiW.** The plate must be a metal that (i) sputters at low
  temperature onto a dielectric without reacting with it, (ii) can
  be etched with high {term}`selectivity` to that dielectric
  ({ref}`CAPME <step-138>`), (iii) withstands the chlorine chemistry
  of the later aluminium etch under resist and the fluorine
  chemistry of the via etch as a stop, and (iv) is already in the
  fab. TiW satisfies all four: it is the cap of every SKY130
  aluminium level ({ref}`TIAL6 <step-112>`; SkyWater lists "TiW"
  among its PVD films[^skw-01]), a barrier whose properties Nicolet
  reviewed and Ghate et al. established,[^nicolet-1978][^ghate-1978]
  it etches in fluorine plasmas (tungsten as WF₆ in SF₆,[^turban-1989]
  TiW in CF₄-based mixtures[^liu-2007-tiw]) and in hydrogen peroxide, which
  Danzl and McLaurin used to strip a TiW anti-reflective cap from
  aluminium pads,[^danzl-1997] and the fab's metal etchers are
  qualified for it ("Lam 9600, Al, TiW, TiN, Pt"[^skw-01]). The
  published alternatives — TiN top plates in the Conexant/Newport
  Fab and TI processes,[^kar-roy-1999][^pat-mim-newportfab][^babcock-2001]
  an aluminium cap over a Ta/TaN top electrode on a copper back end
  in TI's later "ALCAP" scheme[^pat-mim-ti-alcap]
  — play the same role with the fab's other refractory film.
* **Sheet resistance and quality factor.** A plate of 5.8 Ω/sq[^pdk-07]
  under a 2 fF/µm² dielectric gives a distributed RC whose series
  resistance limits the capacitor's {term}`quality factor` at RF; the PDK's
  maximum MiM capacitor aspect ratio of 20[^pdk-03] and its
  `CAPMCD` of 2 µm[^pdk-03] bound the plate geometry the model has
  been fitted for (inference), and Ng et al. review MiM integration
  in Al–Cu and Cu back ends.[^ng-2005]
* **Stress on a thin dielectric.** Sputtered W-rich films are
  compressive or tensile according to pressure and composition —
  Thornton's structure-zone model[^thornton-1974] and Dirks, Wolters
  and De Veirman's study of the columnar microstructure of sputtered
  W and W–Ti(N)[^dirks-1992] describe the dependence — and a highly
  stressed 0.1 µm plate on a 25 nm dielectric can crack or lift it.
  The deposition pressure is therefore chosen for low stress as well
  as low resistivity (industry practice[^ohring-2002]).

Without `CAPTIW1` the `capm` mask would define nothing, and the
capacitor's top terminal would not exist.

## How it is typically performed

An industry-generic MiM top-plate deposition for a 200 mm aluminium
back end (SKY130's recipe is not public):

1. **Queue time.** The dielectric surface should not sit long in
   air; moisture and hydrocarbons at the interface raise leakage
   (industry practice[^txt-05]). Some processes deposit the
   dielectric and the top plate on connected tools; SkyWater's PECVD
   and PVD tools are listed separately,[^skw-01] so on our reading
   the transfer is by {term}`queue-time <queue time>` rule rather than under vacuum.
2. **Degas, no sputter etch.** A vacuum bake in the {term}`PVD`
   cluster's {term}`degas` chamber; the argon pre-clean SkyWater lists
   as "Sputter etch, degas"[^skw-01] is, we infer, omitted or made
   very light, since it would thin the dielectric.
3. **Sputtering.** DC magnetron sputtering from a Ti:W target — 10 wt.%
   Ti is the standard target composition[^pat-tiw-hitachi] — in
   argon at a few mTorr, the wafer warm but well below the aluminium
   limit (industry-typical[^txt-02]); Hill and Dirks et al. give the
   dependence of resistivity and microstructure on pressure and
   composition.[^hill-1980][^dirks-1992] Ohring treats the growth
   of such films.[^ohring-2002]
4. **Thickness.** Of the order of 0.1 µm, from the 5.8 Ω/sq of the
   PDK[^pdk-07] and the resistivity range above (inferred). Thicker
   lowers the plate resistance but lengthens the
   {ref}`CAPME <step-138>` etch and raises the step the
   {ref}`MM3 <step-139>` resist must cover.
5. **Metrology.** Sheet resistance by {term}`four-point probe` on
   monitors (the number the PDK's `RSCAPM` describes[^pdk-07]);
   thickness by XRF; stress by wafer bow; reflectivity for the
   {ref}`CAPM <step-137>` exposure; particles. Capacitance, leakage
   and breakdown are measured on finished structures at {term}`e-test`.

## Machines typically used

* **PVD cluster tool with a Ti:W chamber**, 200 mm: Applied Materials
  Endura,[^amat-endura] Novellus INOVA, Ulvac and Anelva sputtering
  systems ({ref}`category-deposition`).
* **Degas chamber** on the same platform.
* **Four-point probe**, **XRF**, **stress gauge**, **reflectometer**.

## Machines likely used at SkyWater

* **AMAT PVD Metal platform, TiW chamber.** SkyWater lists "AMAT PVD
  Metal" with "TiW" among its films.[^skw-01] Strength: **strong** for
  the vendor and the material; the platform model (Endura is the
  200 mm-era Applied Materials platform[^amat-endura]) and the use of
  the same chamber that caps the aluminium stacks are **inferences**.
* **Lam 9600 / Lam 2300 Versys** metal etchers qualified for
  "TiW"[^skw-01] corroborate that TiW is a patterned film in this fab
  (used at {ref}`CAPME <step-138>`).

## Resources required

* **Ti:W sputter target** (10 wt.% Ti[^pat-tiw-hitachi]); SkyWater's
  filings name Honeywell Electronic Materials and JX Metals as
  sputter-target suppliers.[^sec-01][^sec-02]
* **Argon** for sputtering; **nitrogen** for venting.
* **Chamber shields and clamp/chuck consumables**; **monitor wafers**
  for sheet resistance, stress and particles.

## Related steps and cross-references

* Previous: {ref}`CAPILD <step-135>` (the dielectric it covers).
  Next: {ref}`CAPM <step-137>` (the top-plate mask), then
  {ref}`CAPME <step-138>` (the etch that leaves the plates).
* The bottom plate beneath: {ref}`WTIAL3 <step-134>`, patterned
  later at {ref}`MM3 <step-139>` / {ref}`MM3E <step-140>`.
* The via that lands on the finished plate: {ref}`VIM3E <step-145>`;
  the polish that must not reach it: {ref}`CMPM3 <step-142>`.
* The same film as a cap on the aluminium stacks:
  {ref}`TIAL6 <step-112>`, {ref}`TIAL12 <step-123>`; the second
  capacitor's plate: {ref}`CAPTIW2 <step-151>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, *Device Details* — "thin conductor layer on top of
  the dielectric"; `RSCAPM` 5.8 Ω/sq (4.8–6.8); `CMIMA`, `CMIMP`; the
  `cap_mim` cross-section ("CAPM" over "M3 (plate 1)").[^pdk-07]
* SkyWater PDK, *Layers Reference* — `capm` 89:44.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `CAPMCD` 2 µm; MiM
  aspect ratio 20.[^pdk-03]
* SkyWater PDK, *Process stack diagram* — `capm` between `metal3` and
  `metal4`.[^pdk-04]
* Cypress, QTP 113005 — the 300 Å TiW caps of the S8 metal
  stacks, for comparison.[^cyp-qtp-113005]
* SkyWater, *Facilities & Capabilities* — "AMAT PVD Metal … TiW";
  "Sputter etch, degas"; TiW on the metal etchers.[^skw-01]
* SkyWater, Form S-1 and 10-K — sputter-target suppliers.[^sec-01][^sec-02]
* Hitachi Metals, US 5,160,534 — Ti:W target composition.[^pat-tiw-hitachi]
* Applied Materials, *Endura PVD*.[^amat-endura]

### High-level understanding

* Wikipedia, *Sputter deposition*, *Capacitor*.[^wiki-sputter][^wiki-capacitor]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  sputtering and refractory barrier films.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — passive
  devices in the deep-submicron back end.[^txt-05]
* Ohring, *Materials Science of Thin Films* — film growth, stress and
  structure.[^ohring-2002]

### Deep dive

* Ghate, Blair, Fuller and McGuire (TI), *Thin Solid Films* 1978 —
  Ti:W barrier metallisation for integrated circuits.[^ghate-1978]
* Nicolet, *Thin Solid Films* 1978 — diffusion barriers in thin
  films, TiW among them.[^nicolet-1978]
* Hill, *Thin Solid Films* 1980 — magnetron-sputtered Ti–W
  films.[^hill-1980]
* Dirks, Wolters and De Veirman (Philips), *Thin Solid Films* 1992 —
  columnar microstructure of sputtered W and W–Ti(N).[^dirks-1992]
* Nowicki et al., *Thin Solid Films* 1978, and Olowolafe et al.,
  *J. Appl. Phys.* 1985 — TiW on and with aluminium.[^nowicki-1978][^olowolafe-1985]
* Thornton, *JVST* 1974 — the structure-zone model behind the
  pressure choice.[^thornton-1974]
* Turban, Coulon and Mutsukura, *Thin Solid Films* 1989, and Liu and
  Kuo, *J. Electrochem. Soc.* 2007 — the fluorine-plasma etching of
  tungsten and of TiW that makes the plate patternable.[^turban-1989][^liu-2007-tiw]
* Danzl and McLaurin, IEMT 1997 — peroxide removal of a TiW cap from
  aluminium, the wet alternative.[^danzl-1997]
* Kar-Roy et al., IITC 1999, and Babcock et al., *IEEE EDL* 2001 —
  TiN top plates in published Al-BEOL MiM processes.[^kar-roy-1999][^babcock-2001]
* Ng et al., *IEEE TED* 2005 — a review of MiM integration in Al–Cu
  and Cu back ends.[^ng-2005]
* Brabazon et al. (IBM), US 5,708,559; Kar-Roy and Racanelli
  (Newport Fab), US 6,430,028; Crenshaw et al. (TI), US 7,250,334 —
  plate materials and constructions from three assignees, including
  IBM's damascene bottom plate.[^pat-mim-ibm][^pat-mim-newportfab][^pat-mim-ti-alcap]

## Open questions

* The top-plate thickness, composition (Ti fraction, nitrogen
  content) and deposition conditions are not public; ~0.1 µm is our
  estimate from `RSCAPM`[^pdk-07] with an assumed resistivity.
* Whether a pre-clean precedes the deposition, and whether the
  dielectric and plate are deposited within a queue-time limit, is
  not public.
* Whether the plate is a single TiW film or carries a thin cap
  (as the TI "ALCAP" scheme does[^pat-mim-ti-alcap]) is not public;
  a single film is assumed here.
* The PVD chamber and platform model are inferred from SkyWater's
  film list.[^skw-01]

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
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
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^cyp-qtp-113005]: Cypress Semiconductor, *Product Qualification
    Plan, QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8
    Technology, CMI (Fab 4)*, document 001-85611 Rev. *A, January
    2013 (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
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
[^dirks-1992]: A. G. Dirks, R. A. M. Wolters and A. E. M. De Veirman,
    "Columnar microstructures in magnetron-sputtered refractory metal
    thin films of tungsten, molybdenum and W-Ti-(N)", *Thin Solid
    Films* **208**(2), 181–188 (1992).
    <https://doi.org/10.1016/0040-6090(92)90640-W>
[^nowicki-1978]: R. S. Nowicki, J. M. Harris, M.-A. Nicolet and
    I. V. Mitchell, "Studies of the Ti-W/Au metallization on aluminum",
    *Thin Solid Films* **53**(2), 195–205 (1978).
    <https://doi.org/10.1016/0040-6090(78)90035-4>
[^olowolafe-1985]: J. O. Olowolafe, C. J. Palmstrøm, E. G. Colgan and
    J. W. Mayer, "Al/TiW reaction kinetics: Influence of Cu and
    interface oxides", *Journal of Applied Physics* **58**(9),
    3440–3443 (1985). <https://doi.org/10.1063/1.335764>
[^thornton-1974]: J. A. Thornton, "Influence of apparatus geometry and
    deposition conditions on the structure and topography of thick
    sputtered coatings", *Journal of Vacuum Science and Technology*
    **11**(4), 666–670 (1974). <https://doi.org/10.1116/1.1312732>
[^turban-1989]: G. Turban, J. F. Coulon and N. Mutsukura, "A
    mechanistic study of SF₆ reactive ion etching of tungsten", *Thin
    Solid Films* **176**(2), 289–308 (1989).
    <https://doi.org/10.1016/0040-6090(89)90102-8>
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
[^pat-mim-ibm]: T. J. Brabazon, B. El-Kareh, S. R. Martin, M. J. Rutten
    and C. W. Kaanta (International Business Machines), *Precision
    analog metal-metal capacitor*, US 5,708,559 A, filed 1995-10-27,
    granted 1998-01-13.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5708559>
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
