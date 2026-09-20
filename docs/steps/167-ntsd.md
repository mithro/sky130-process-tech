(step-167)=
# Step 167 — NTSD: Nitride topside deposition

| | |
|---|---|
| **Step number** | 167 of 171[^steps-sheet] |
| **Step code** | `NTSD` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | {term}`BEOL` — passivation, pads, alloy, test |
| **Previous step** | {ref}`NSME <step-166>` |
| **Next step** | {ref}`PDM <step-168>` |

## What this step is

`NTSD` deposits the silicon nitride that is the outer skin of the die:
a blanket nitride — on our reading a plasma (PECVD) nitride — laid over the thin passivation oxide of
{ref}`NFUSOX <step-164>`, over the metal-5 lines and pads beneath it,
and — on our reading of {ref}`NSM <step-165>` and
{ref}`NSME <step-166>` — into the ring-shaped opening just etched along
the edge of every die. After it, the only front-side processing left is
the pad opening with its strip and clean ({ref}`PDM <step-168>`,
{ref}`PDME <step-169>`), the final anneal ({ref}`ALLY <step-170>`) and
electrical test ({ref}`HPETEST <step-171>`).

The PDK's process stack diagram draws this film as "TOPNIT K=7.5" over
the thin "TOPOX K=3.9": 0.54 µm thick on top of `metal5` and 0.4223 µm
on its sidewall, with a "glass cut" through it over the metal; beside
the metal it places the top of the nitride 0.3777 µm above the bottom
of metal 5, with no separate TOPOX drawn (our reading of the
drawing).[^pdk-04] Cypress qualification reports for two other S8 variants and
for the R7FT-3R technology at the same fab give thicker nitrides —
"1000Å TEOS / 9000Å PECVD Nitride" (R7FT-3R, 2005),[^cyp-qtp-014807]
"1000A TEOS/9000A Si3N4" (S8DI, 2014)[^cyp-qtp-123907] and "7000 +/-
2000A Nitride" (S8TNV-5R, 2013)[^cyp-qtp-113005] — so the public record puts the passivation
nitride between 0.54 µm and 0.9 µm; which value applies to SKY130 lots
is not public. The R7FT-3R report calls its nitride "PECVD", and
SkyWater lists "PECVD nitride C1" and "PECVD silane
oxide/nitride/oxynitride, C1 – low temp, range of R.I.
options";[^cyp-qtp-014807][^skw-01] we read `NTSD` as a {term}`PECVD`
silicon nitride (inference). The step list used in this reference does
not explain the film.

## Step category

`NTSD` is a {ref}`Thin-film deposition <category-deposition>` step of
the *PECVD nitride* class — the film the category page describes as
"the final scratch- and moisture-resistant passivation".
{ref}`LINIT <step-104>`, over the local interconnect, is the flow's
other nitride on conductors (a plasma nitride on the reading of that
page), 0.075 µm thick;[^pdk-04] this one is several times thicker,
is deposited over the tallest topography in the flow (1.26 µm metal-5
lines on 1.600 µm spaces, m5.1 and m5.2[^pdk-periph][^pdk-04]) and, on
our reading, into a trench several micrometres deep at the die edge, so
{term}`step coverage` and film stress matter more than at any earlier
nitride. The diagram's 0.4223 µm on the sidewall against 0.54 µm on top
is a sidewall coverage of about 78 % (our arithmetic from the
labels[^pdk-04]). Whether a polyimide is applied to SKY130 wafers in
this flow is not public. SkyWater's S130 technology table lists
polyimide as "Yes",[^skw-02] and SkyWater lists a "Polyimide cure"
furnace process,[^skw-01] but the mask table flags "Polyimide 2 (2)"
(PMM2), "DECA PBO" (PBO) and "Cu Inductor/Redist." (CU1M) and not
"Polyimide" (PMM) for SKY130,[^pdk-05] the step list has no polyimide
step, and the PDK's stack diagram draws "PI1 K=2.94" over the
nitride.[^pdk-04] Whether a given lot receives it is an option, not a
property of the flow described here. Nothing is deposited over `NTSD`
in the flow described here except possibly that polyimide; on a die
without it, `NTSD` is also the surface the package mould compound
touches.

## Why this step exists

* **A moisture and mobile-ion barrier.** As a passivation layer
  silicon nitride "is a significantly better diffusion barrier against
  water molecules and sodium ions" than silicon dioxide;[^wiki-sin] Sinha et al.
  described reactive-plasma Si–N films for MOS-LSI
  passivation,[^sinha-1978] and a seal-ring patent calls the passivation
  nitride "a very good barrier of moisture and ionic
  contamination".[^pat-sealring-zeevo] Mobile alkali ions drift through
  oxide under bias and shift MOS characteristics — Snow, Grove, Deal and
  Sah measured their transport in thermal oxide[^snow-1965] — and
  moisture with ionic contamination corrodes aluminium, as Comizzoli et
  al. reviewed;[^comizzoli-1986] Peck's acceleration model is used to
  shorten such humidity tests.[^peck-1986] Habraken and
  Kuiper review the films' composition and properties.[^habraken-1994]
* **Sealing the die edge (inference).** Deposited into the `nsm`
  opening, the nitride can form a wall through the dielectric stack at
  the seal ring, the construction a GlobalFoundries edge-seal patent
  that may still be in force describes (collapsed note below this list).
  That SKY130's nitride does
  this is our reading of the `nsm` rules and seal-ring layout
  ({ref}`NSM <step-165>`).
* **Mechanical protection.** A hard nitride resists scratches during
  handling, probing and assembly, and with the oxide beneath it spreads
  the load of probe needles and wire bonds on the pad edges (industry
  practice;[^txt-05] Hunter et al. describe probe- and bond-induced
  cracking of the oxide in aluminium pad structures[^hunter-2012]).
* **The price: hydrogen and stress.** Plasma nitride from silane and
  ammonia contains a great deal of hydrogen — Lanford and Rand measured
  about 20–25 at.% in films deposited at 330–350 °C,[^lanford-1978] and
  Chow et al. found 4–39 at.% across nine commercial reactors, with etch
  rate correlated to hydrogen content[^chow-1982] — and its stress
  depends on temperature, pressure, gas ratio and RF frequency, as
  Claassen et al. showed;[^claassen-1985] Hughey and Cook found an
  irreversible tensile change on heating.[^hughey-2003] Hydrogen and
  water in and through the nitride can degrade hot-carrier lifetime:
  Shimaya proposed a water-diffusion model for the enhancement of
  hot-carrier degradation by nitride passivation.[^shimaya-1995] The
  recipe is therefore a compromise between barrier quality, stress and
  hydrogen, and the {ref}`ALLY <step-170>` anneal follows it.

:::{dropdown} From a patent shown as in force (US 10,062,748; estimated expiry 2038-02-27) — open to read
The GlobalFoundries edge-seal patent describes a PECVD passivation on
the sidewalls of a trench through the dielectrics.[^pat-edgeseal-gf]
:::

Without `NTSD` the die would be protected only by oxide, whose water
uptake and ion permeability are what the nitride exists to block.

## How it is typically performed

An industry-generic passivation-nitride deposition over a thick
aluminium top metal for a 200 mm, 130 nm-era fab (SKY130's recipe is not
public):

1. **Surface.** The wafer comes from the {ref}`NSME <step-166>` strip
   and clean; a short {term}`queue time` and, often, a degas or N₂
   plasma before deposition (industry practice[^txt-05]).
2. **Chamber and temperature.** A single-wafer or multi-station PECVD
   reactor at roughly 300–400 °C (industry-typical for films on
   aluminium[^txt-05][^wiki-pecvd]); the RF frequency is one of the
   levers on stress — Claassen et al. measured how deposition
   temperature, pressure, gas composition and RF frequency move the
   composition and mechanical stress of plasma nitride[^claassen-1985] —
   and mixed-frequency chambers are the industry-typical way to trim a
   passivation nitride towards mild compression (industry
   practice;[^txt-05] SKY130's recipe is not public).
3. **Chemistry.** SiH₄ with NH₃ and N₂; Smith et al. set out the
   deposition mechanism of SiNₓHᵧ from NH₃–SiH₄ plasmas.[^smith-1990]
   The SiH₄/NH₃ ratio moves the composition, and with it the
   refractive index (Habraken and Kuiper review the
   dependence[^habraken-1994]) and the Si–H/N–H bonding that Lanford
   and Rand calibrated by infrared absorption.[^lanford-1978] Sinha
   et al.'s reactive-plasma films, deposited at 275 °C, spanned Si/N of
   0.75–1.5 and refractive index 1.9–2.3 with stress ranging from
   compressive to tensile, and at 450–500 °C gave crack-resistant 1 µm
   films with good adhesion to aluminium — the same levers and the same
   constraint.[^sinha-1978]
4. **Thickness.** Of the order of 0.5–0.9 µm: 0.54 µm on the PDK's
   diagram[^pdk-04] and 0.7–0.9 µm in the Cypress reports for the S8DI
   and S8TNV-5R variants of S8, and in the 0.18 µm R7FT-3R technology,
   at the same fab.[^cyp-qtp-113005][^cyp-qtp-123907][^cyp-qtp-014807]
   A Vanguard fuse patent describes a passivation of "silicon oxide
   layer … between about 0.4 and 0.7 microns thick" under "silicon
   nitride layer … between about 0.4 and 0.7 microns thick" and, in its
   claim 7, a polyimide "between about 8 and 12 microns
   thick".[^pat-fuse-vanguard] Its nitride is of the same order as the
   0.54 µm here; its oxide, which is the controlled dielectric over a
   fusible link, is four to eight times the 0.09 µm the PDK draws
   ({ref}`NFUSOX <step-164>`).
5. **Metrology.** Thickness and refractive index by ellipsometry on
   monitors; stress by wafer bow; hydrogen content (FTIR) and wet-etch
   rate when the recipe is qualified, the correlation Chow et al.
   reported;[^chow-1982] pinholes and particles; step coverage by
   cross-section SEM over metal-5 lines and, on our reading, in the
   seal-ring opening.
6. **Chamber clean.** NF₃ remote or in-situ plasma clean between runs.

## Machines typically used

* **{ref}`PECVD dielectric system <machine-pecvd>`**, 200 mm: Novellus Concept One/Two or
  Sequel,[^novellus-history] Applied Materials Producer or Centura
  DxZ[^amat-10k] ({ref}`category-deposition`).
* **{ref}`Ellipsometer <machine-film-thickness-metrology>`**, **stress gauge**, **FTIR**, **{ref}`particle inspection <machine-defect-inspection>`**.

## Machines likely used at SkyWater

* **"C1" PECVD system, nitride.** SkyWater lists "PECVD nitride C1" and
  "PECVD silane oxide/nitride/oxynitride, C1 – low temp, range of R.I.
  options".[^skw-01] Strength: **strong** for the existence of a PECVD
  nitride process; assignment to `NTSD` is an **inference** supported by
  the "PECVD Nitride" passivation of a Cypress report from the same
  fab.[^cyp-qtp-014807] Reading "C1" as a Novellus Concept One is an
  inference from the vendor's product names.[^novellus-history]
* **Aviza furnace nitrides** (LPCVD, BTBAS)[^skw-01] are excluded on
  thermal grounds for a wafer carrying aluminium (inference).

## Resources required

* **{ref}`Silane <material-precursors>`**, **ammonia** and **{ref}`nitrogen <material-process-gases>`**.[^wiki-silane][^wiki-pecvd] Gas
  suppliers named in SkyWater's filings: Air Products and Praxair (2021
  S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]
* **{ref}`NF₃ <material-etch-gases>`** for the chamber clean.
* **{ref}`Showerhead, heater and liner consumables <material-hardware-consumables>`**; **{ref}`monitor wafers <material-substrates>`** for
  thickness, index, stress and hydrogen checks.

## Related steps and cross-references

* Previous: {ref}`NSME <step-166>` (the seal-ring opening the nitride
  lines, on our reading). Next: {ref}`PDM <step-168>` and
  {ref}`PDME <step-169>` (the pad opening through this nitride).
* The oxide beneath: {ref}`NFUSOX <step-164>`; the metal it covers:
  {ref}`MM5E <step-163>`.
* The anneal after passivation: {ref}`ALLY <step-170>`.
* The other nitride over conductors: {ref}`LINIT <step-104>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Method and apparatus for preventing cracks in semiconductor die <patent-gp24244903>` — US 5,650,666 A (1995)
* {ref}`Process for controlling oxide thickness over a fusible link using transient etch stops <patent-gp23688532>` — US 6,294,474 B1 (1999)
* {ref}`Seal ring structure for IC containing integrated digital/RF/analog circuits and functions <patent-gp25297601>` — US 6,492,716 B1 (2001)

:::{dropdown} 2 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 8,093,719 B1 <patent-gp45419097>` — unknown
* {ref}`US 10,062,748 B1 <patent-gp63208306>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater PDK, *Process stack diagram*](<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>) — "TOPNIT K=7.5", 0.54 µm and
  0.4223 µm; 0.3777 µm; "TOPOX"; "PI1"; `metal5` 1.26 µm.[^pdk-04]
* [SkyWater PDK, *Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) — PMM not flagged for SKY130; PMM2, PBO and
  CU1M flagged.[^pdk-05]
* [SkyWater Technology, *Mixed-Signal CMOS & ROIC* platform table](<https://www.skywatertechnology.com/cmos/>) —
  polyimide "Yes" for S130.[^skw-02]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — m5.1, m5.2.[^pdk-periph]
* Cypress, QTP 014807, QTP 123907/132302/132301 and QTP 113005 — the
  passivation descriptions at Fab 4.[^cyp-qtp-014807][^cyp-qtp-123907][^cyp-qtp-113005]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — "PECVD nitride C1"; furnace
  nitrides; "Polyimide cure".[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]

### High-level understanding

* Wikipedia, [*Silicon nitride*](<https://en.wikipedia.org/wiki/Silicon_nitride>), [*Plasma-enhanced chemical vapor
  deposition*](<https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>), [*Silane*](<https://en.wikipedia.org/wiki/Silane>).[^wiki-sin][^wiki-pecvd][^wiki-silane]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) — passivation
  films in the deep-submicron back end.[^txt-05]
* Novellus company history; Applied Materials 10-K — the 200 mm PECVD
  platforms.[^novellus-history][^amat-10k]

### Deep dive

* [Sinha et al., *J. Electrochem. Soc.* 1978](<https://doi.org/10.1149/1.2131509>) — reactive-plasma Si–N
  films for MOS-LSI passivation.[^sinha-1978]
* [Lanford and Rand, *J. Appl. Phys.* 1978](<https://doi.org/10.1063/1.325095>) — hydrogen content of plasma
  nitride and its infrared calibration.[^lanford-1978]
* [Chow et al., *J. Appl. Phys.* 1982](<https://doi.org/10.1063/1.331445>) — hydrogen and etch rate across
  nine commercial plasma-nitride reactors.[^chow-1982]
* [Claassen et al., *J. Electrochem. Soc.* 1985](<https://doi.org/10.1149/1.2113980>) — composition and stress
  versus temperature, pressure, gas ratio and RF
  frequency.[^claassen-1985]
* [Smith et al., *J. Electrochem. Soc.* 1990](<https://doi.org/10.1149/1.2086517>) — the SiNₓHᵧ deposition
  mechanism.[^smith-1990]
* [Habraken and Kuiper, *Mater. Sci. Eng. R* 1994](<https://doi.org/10.1016/0927-796X(94)90006-X>) — review of silicon
  nitride and oxynitride films.[^habraken-1994]
* [Hughey and Cook, MRS 2003](<https://doi.org/10.1557/PROC-795-U1.6>) — irreversible tensile stress in PECVD
  nitride on heating.[^hughey-2003]
* [Shimaya, IRPS 1995](<https://doi.org/10.1109/RELPHY.1995.513694>) — nitride passivation and hot-carrier
  degradation.[^shimaya-1995]
* [Snow, Grove, Deal and Sah, *J. Appl. Phys.* 1965](<https://doi.org/10.1063/1.1703105>) — alkali-ion
  transport in oxide, the contamination the nitride blocks.[^snow-1965]
* [Peck, IRPS 1986](<https://doi.org/10.1109/IRPS.1986.362110>) — a humidity-test acceleration model for plastic
  packages.[^peck-1986]
* [Hunter et al., IMAPS 2012](<https://doi.org/10.4071/isom-2012-TP41>) — probe- and bond-induced cracking in
  aluminium pad structures.[^hunter-2012]
* [Tzeng, Chen and Wang (Vanguard), US 6,294,474](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6294474>) — an oxide/nitride
  passivation stack with stated thicknesses.[^pat-fuse-vanguard]

:::{dropdown} From a patent shown as in force (US 10,062,748; estimated expiry 2038-02-27) — open to read
* Bothra, McKay and Jhota (Zeevo), US 6,492,716; Stamper, McGahay and He
  (GlobalFoundries), US 10,062,748 — passivation nitride over a seal
  ring and an edge seal through the
  dielectrics.[^pat-sealring-zeevo][^pat-edgeseal-gf]
:::

## Open questions

* The nitride thickness for SKY130 is not public: 0.54 µm on the PDK
  diagram[^pdk-04] against 0.7–0.9 µm in Cypress reports for the S8DI
  and S8TNV-5R variants of S8, and in the 0.18 µm R7FT-3R technology, at
  the same fab.[^cyp-qtp-113005][^cyp-qtp-123907][^cyp-qtp-014807]
* The diagram's 0.3777 µm beside metal 5 runs, on our reading, from the
  bottom of metal 5 to the top of the nitride, with no TOPOX drawn
  there;[^pdk-04] whether the passivation is really thinner between
  lines is not stated.
* Whether the nitride fills, lines or merely bridges the `nsm` opening,
  and what it lands on there, is not public.
* The deposition chemistry, temperature, refractive index, stress and
  hydrogen content are not public; that the film is PECVD is an
  inference from SkyWater's list and a Cypress report.[^skw-01][^cyp-qtp-014807]
* Whether a polyimide is applied to SKY130 wafers in this flow is not
  public. SkyWater's S130 technology table lists polyimide as
  "Yes",[^skw-02] and SkyWater lists a "Polyimide cure" furnace
  process,[^skw-01] but the mask table flags PMM2, PBO and CU1M and not
  PMM for SKY130,[^pdk-05] the step list has no polyimide step, and the
  PDK's stack diagram draws "PI1 K=2.94" over the
  nitride.[^pdk-04] Whether a given lot receives it is an option, not a
  property of the flow described here.

<!-- footnotes -->

[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^cyp-qtp-113005]: Cypress Semiconductor, *Product Qualification
    Plan, QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8
    Technology, CMI (Fab 4)*, document 001-85611 Rev. *A, January
    2013 (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^cyp-qtp-123907]: Cypress Semiconductor, *Fab Process Qualification
    Report, QTP# 123907, 132302, 132301: Metal Stack Change, S8
    Technology, Fab 4 CMI*, document 001-91369 Rev. **, March 2014
    (copy hosted by Tokyo Electron Device as the attachment to
    Cypress Product Information Notification PIN145273, 2014-03-13,
    which states the report is attached and available from
    cypress.com; <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>).
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/145273-Qualification_Report.pdf>
[^cyp-qtp-014807]: Cypress Semiconductor, *Technology Derivative
    Qualification Report, QTP# 014807 Version 2.0: Technology
    Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM*, June 2005
    (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^skw-02]: SkyWater Technology, *Mixed-Signal CMOS & ROIC*, platform
    table, accessed 2026-09-13. <https://www.skywatertechnology.com/cmos/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.*
    (company history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^amat-10k]: Applied Materials, Inc., Form 10-K for fiscal 2003
    (platform descriptions: Centura, Endura, Endura SL, Producer).
    <https://www.sec.gov/Archives/edgar/data/6951/000089161804000093/f95058e10vk.htm>
[^wiki-sin]: Wikipedia, *Silicon nitride*.
    <https://en.wikipedia.org/wiki/Silicon_nitride>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^wiki-silane]: Wikipedia, *Silane*. <https://en.wikipedia.org/wiki/Silane>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^sinha-1978]: A. K. Sinha, H. J. Levinstein, T. E. Smith, G. Quintana
    and S. E. Haszko, "Reactive Plasma Deposited Si-N Films for MOS-LSI
    Passivation", *Journal of The Electrochemical Society* **125**(4),
    601–608 (1978). <https://doi.org/10.1149/1.2131509>
[^lanford-1978]: W. A. Lanford and M. J. Rand, "The hydrogen content of
    plasma-deposited silicon nitride", *Journal of Applied Physics*
    **49**(4), 2473–2477 (1978). <https://doi.org/10.1063/1.325095>
[^chow-1982]: R. Chow, W. A. Lanford, K.-M. Wang and R. S. Rosler,
    "Hydrogen content of a variety of plasma-deposited silicon
    nitrides", *Journal of Applied Physics* **53**(8), 5630–5633 (1982).
    <https://doi.org/10.1063/1.331445>
[^claassen-1985]: W. A. P. Claassen, W. G. J. N. Valkenburg,
    M. F. C. Willemsen and W. M. v. d. Wijgert, "Influence of Deposition
    Temperature, Gas Pressure, Gas Phase Composition, and RF Frequency
    on Composition and Mechanical Stress of Plasma Silicon Nitride
    Layers", *Journal of The Electrochemical Society* **132**(4),
    893–898 (1985). <https://doi.org/10.1149/1.2113980>
[^smith-1990]: D. L. Smith, A. S. Alimonda, C.-C. Chen, S. E. Ready and
    B. Wacker, "Mechanism of SiNₓHᵧ Deposition from NH₃-SiH₄ Plasma",
    *Journal of The Electrochemical Society* **137**(2), 614–623 (1990).
    <https://doi.org/10.1149/1.2086517>
[^habraken-1994]: F. H. P. M. Habraken and A. E. T. Kuiper, "Silicon
    nitride and oxynitride films", *Materials Science and Engineering:
    R: Reports* **12**(3), 123–175 (1994).
    <https://doi.org/10.1016/0927-796X(94)90006-X>
[^hughey-2003]: M. P. Hughey and R. F. Cook, "Irreversible Tensile
    Stress Development in PECVD Silicon Nitride Films", *MRS
    Proceedings* **795** (2003). <https://doi.org/10.1557/PROC-795-U1.6>
[^shimaya-1995]: M. Shimaya, "Water diffusion model for the enhancement
    of hot-carrier-induced degradation due to silicon nitride
    passivation in submicron MOSFET's", *33rd IEEE International
    Reliability Physics Symposium Proceedings* (1995), pp. 292–296.
    <https://doi.org/10.1109/RELPHY.1995.513694>
[^snow-1965]: E. H. Snow, A. S. Grove, B. E. Deal and C. T. Sah, "Ion
    Transport Phenomena in Insulating Films", *Journal of Applied
    Physics* **36**(5), 1664–1673 (1965).
    <https://doi.org/10.1063/1.1703105>
[^comizzoli-1986]: R. B. Comizzoli, R. P. Frankenthal, P. C. Milner and
    J. D. Sinclair, "Corrosion of Electronic Materials and Devices",
    *Science* **234**(4774), 340–345 (1986).
    <https://doi.org/10.1126/science.234.4774.340>
[^peck-1986]: D. S. Peck, "Comprehensive Model for Humidity Testing
    Correlation", *24th International Reliability Physics Symposium*
    (1986), pp. 44–50. <https://doi.org/10.1109/IRPS.1986.362110>
[^hunter-2012]: S. Hunter, J. L. Clark, D. Hornberger and L. Rubio, "Use
    of Wire Bonding to Study Bond Pad Damage from Wafer Probe",
    *International Symposium on Microelectronics* **2012**(1), 384–395
    (IMAPS, 2012). <https://doi.org/10.4071/isom-2012-TP41>
[^pat-sealring-zeevo]: S. Bothra, T. G. McKay and R. Jhota (Zeevo),
    *Seal ring structure for IC containing integrated digital/RF/analog
    circuits and functions*, US 6,492,716 B1, filed 2001-04-30, granted
    2002-12-10.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6492716>
[^pat-edgeseal-gf]: A. K. Stamper, V. J. McGahay and Z.-X. He
    (GlobalFoundries), *Segmented guard-ring and chip edge seals*,
    US 10,062,748 B1, filed 2017-02-27, granted 2018-08-28.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10062748>
    Shown as in force; estimated expiry 2038-02-27 (estimate from public
    records, not legal advice).
[^pat-fuse-vanguard]: W.-T. Tzeng, Y.-F. Chen and K.-J. Wang (Vanguard
    International Semiconductor), *Process for controlling oxide
    thickness over a fusible link using transient etch stops*,
    US 6,294,474 B1, filed 1999-10-25, granted 2001-09-25.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6294474>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
