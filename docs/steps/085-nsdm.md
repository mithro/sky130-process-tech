(step-085)=
# Step 085 — NSDM: N+ source drain implant mask

| | |
|---|---|
| **Step number** | 85 of 171[^steps-sheet] |
| **Step code** | `NSDM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | FEOL — extensions, spacers, source/drain |
| **Previous step** | {ref}`PDIS <step-084>` |
| **Next step** | {ref}`NSDI <step-086>` |

## What this step is

`NSDM` is the N⁺ source/drain implant mask, the complement of
{ref}`PSDM <step-081>`. On the wafer cleaned at {ref}`PDIS <step-084>`
it coats, exposes and develops a resist whose windows lie over every
region that is to receive the heavy n-type implant of
{ref}`NSDI <step-086>`; the resist is stripped at
{ref}`NSDIS <step-087>`. It is the last mask before the source/drain
anneal {ref}`RTAD <step-088>` and the last implant mask of the front
end proper.

The PDK's mask table lists "N+ Implant, NSDM" as used in
SKY130;[^pdk-05] the drawn layer is `nsdm` (GDS 93:44, "N+
source/drain implant") and the generated mask layer `cnsdm` (30:0,
"N+ Implant mask") with "mask add" (29:21) and "mask drop" (29:22)
purposes,[^pdk-06] so the reticle is derived from the drawn layer by
Boolean operations. The rules are shared with `psdm` under "Defines
opening for N+/P+ implants": width 0.380 µm (nsd.1), space 0.380 µm
(nsd.2), enclosure of diffusion and of tap by 0.125 µm (nsd.5a,
nsd.5b), zero enclosure at a diff/tap butting edge (nsd.6), 0.130 µm
to diffusion or tap of the opposite implant (nsd.7), no overlap with
opposite-doping diffusion or tap (nsd.8), "Diff and tap must be
enclosed by their corresponding implant layers" (nsd.9), minimum area
0.265 µm² (nsd.10a) and minimum hole area 0.265 µm² (nsd.11).[^pdk-periph]
The precision-resistor rules add "Min spacing, no overlap, of rpm and
nsdm" of 0.200 µm (rpm.6),[^pdk-periph] and the minimum-CD table gives
0.38 µm feature and space (`NSDMCD`, `NSDMCDSP`).[^pdk-03]

## Step category

`NSDM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *implant-block* type, printed on the same topography and
to the same rules as {ref}`PSDM <step-081>`. The differences are in
what the resist must withstand — arsenic is a heavier ion than boron
or BF₂, so at the same dose it deposits more energy in the resist
surface and forms a harder crust[^fujimura-1989] — and in the fact
that its windows are, to a first approximation, the complement of
the P⁺ windows across the active area: nsd.7 and nsd.8 keep the two
layers apart except where they butt at a diff/tap edge with zero
enclosure (nsd.6).[^pdk-periph]

## Why this step exists

The N⁺ implant must reach the n-type structures and be kept out of
the p-type ones. From the PDK's device and layer descriptions, the
regions inside `nsdm` are:

* the **source/drain of every NMOS** — the 1.8 V and 5 V devices,
  the native and low-Vt variants, the isolated and drain-extended
  NMOS and the ESD NMOS, whose cross-sections show "N+" source/drain
  beside the "N−" extensions;[^pdk-07] the drain-extended NMOS
  source must be enclosed by `nsdm` (a `de_nFet_source` rule);[^pdk-periph]
* the **SONOS memory cells**, which are NMOS transistors with an ONO
  gate stack ({ref}`ONO <step-040>`) and whose source/drain are made
  here (inference from the device being an n-channel FET[^pdk-07]);
* the **n⁺ taps** (`tap`, "type equal to the well/substrate
  underneath"[^pdk-06]) that contact the N-wells and the deep
  N-well, with the 0.125 µm enclosure of nsd.5b;[^pdk-periph]
* the **emitter and collector contacts of the vertical NPN** and the
  **base contact of the PNP**, whose cross-sections show "N+" regions
  labelled E, C and B respectively;[^pdk-07]
* the **N⁺ diffusion resistor** (`res_generic_nd`, "N+
  diffusion"),[^pdk-07] with a sheet resistance of 120 000 mΩ/sq
  (120 Ω/sq) in the extraction tables;[^pdk-08]
* the **P-well-to-n⁺ diodes** (`diode_pw2nd_*`);[^pdk-07]
* the poly contact heads outside resistors, which — on the reading of
  the {ref}`NPCM <step-078>` page — receive an extra n⁺ dose through
  the {term}`nitride cut` wherever `nsdm` covers them; the precision
  resistors themselves are kept 0.200 µm clear of `nsdm` (rpm.6)[^pdk-periph]
  so that their p-type heads are not counter-doped.

Kept *out* are the PMOS source/drains, p⁺ taps, PNP emitters and
collectors and P⁺ resistors (nsd.8), and the capped gates, which on
our reading receive nothing from either source/drain implant. The
enclosure and spacing values reflect the lateral straggle and
{term}`mask-proximity effects <mask-proximity effect>` measured by Hook et al.[^hook-2003] and
modelled by Sheu et al.,[^sheu-2006] whose implications for analogue
layout Drennan, Kniffin and Locascio describe.[^drennan-2006]

Without `NSDM` no NMOS source/drain, N-well contact, NPN or n-type
resistor or diode could be made without doping the p-type devices.

## How it is typically performed

An industry-generic high-dose implant-block lithography sequence for
a 200 mm, 130 nm-era fab (SKY130's is not public):

1. **Surface preparation.** Dehydration bake and HMDS prime; the
   surface is the {ref}`SPOX <step-080>` oxide, slightly thinned by
   the {ref}`PDIS <step-084>` clean.[^txt-02]
2. **Resist coat.** A single-layer positive resist of about 1 µm —
   the PDK's nominal 1.14 µm[^pdk-03] — which stops an arsenic
   source/drain implant at tens of keV (industry-typical[^txt-02])
   with a wide margin. The thickness is again set by coverage over
   the capped gates and by the resist's endurance under a
   10¹⁵ cm⁻² arsenic beam, whose heating and charging Smith,[^smith-1983]
   Romig et al.,[^romig-1996] and Lukaszek, Reno and Bammi (for an
   arsenic implant specifically)[^lukaszek-1996] describe.
3. **Exposure.** At 0.380 µm minimum feature and space,[^pdk-periph]
   an i-line stepper at NA 0.6 gives k₁ ≈ 0.62, comfortably above
   the "0.4 for production" limit;[^wiki-litho] we infer an
   **i-line** exposure, as for `PSDM`. ITRS 2001 reserves 248 nm for
   the critical layers of the node.[^itrs-03]
4. **Alignment.** To the active/STI pattern (0.125 µm diffusion
   enclosure) and, for the butting edges and the resistor rule, to
   poly and to the `PSDM` pattern; Levinson treats the allocation of
   such multi-reference overlay budgets.[^levinson-2005]
5. **Develop** in 2.38 % (0.26 N) TMAH,[^txt-02] rinse, dry; hard bake or UV
   cure against the implant, the outgassing of thick resist under
   implantation having been measured by Lee et al.[^lee-1996] and
   Horsky.[^horsky-1998]
6. **Inspection.** Overlay on box-in-box targets; after-develop
   inspection for scumming at gate feet and at the nsdm/psdm butting
   edges.

## Machines typically used

* **{ref}`i-line stepper <machine-i-line-stepper>`**, 200 mm: ASML PAS 5500/100–/275, Nikon
  NSR-2205i, Canon FPA-3000i ({ref}`category-lithography`).
* **{ref}`Coat/develop track <machine-coat-develop-track>`** (TEL, DNS/SCREEN, SVG/ASML, Sokudo) with
  UV-cure or hard-bake.
* **{ref}`Overlay metrology <machine-cd-sem-overlay-metrology>`** (KLA-Tencor 5xxx/Archer); **CD-SEM**.

## Machines likely used at SkyWater

* **ASML i-line stepper / i-line scanner.**[^skw-01] Strength:
  **strong** for existence; the assignment of `NSDM` to i-line is an
  **inference** from the 0.38 µm rules.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius**.[^skw-01]
  Strength: strong for existence.
* **Overlay — KLA 5200/5300/Archer; CD — AMAT Verity/VeraSEM**.[^skw-01]
  Strength: strong for existence (SkyWater statement); use at this
  mask is an inference.

## Resources required

* **Positive i-line (DNQ/novolac) photoresist**, about 1 µm (PDK
  nominal 1.14 µm[^pdk-03]); suppliers named in SkyWater's 2021 S-1: Dow,
  JSR, Tokyo Ohka Kogyo.[^sec-01]
* **HMDS**, **2.38 % (0.26 N) TMAH developer**,[^txt-02] edge-bead remover,
  rinse solvents, DI water and nitrogen.
* **The NSDM reticle** — generated from `cnsdm` (30:0) with its
  add/drop corrections.[^pdk-06]

## Related steps and cross-references

* Previous: {ref}`PDIS <step-084>` (the clean this resist is coated
  after). Next: {ref}`NSDI <step-086>` (the implant), then
  {ref}`NSDIS <step-087>` (strip).
* Complementary mask: {ref}`PSDM <step-081>`.
* Structures it dopes: NMOS source/drain (including SONOS cells),
  n⁺ taps, NPN emitter/collector contacts, PNP base contacts, N⁺
  diffusion resistors, n-diodes, and n⁺ poly heads opened at
  {ref}`NPCM <step-078>`.
* The extensions the N⁺ junction joins: {ref}`ASTI <step-065>`,
  {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`.
* Previous mask: {ref}`PSDM <step-081>`; next mask:
  {ref}`LICM1 <step-093>`.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "N+ Implant, NSDM,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `nsdm`
  93:44; `cnsdm` 30:0, 29:21, 29:22; `tap` 65:44.[^pdk-06]
* SkyWater PDK, *Periphery rules* — nsd.1–nsd.11; rpm.6;
  `de_nFet_source` enclosure by nsdm.[^pdk-periph]
* SkyWater PDK, *Criteria & Assumptions* — `NSDMCD` 0.38 µm;
  photoresist thickness 1.14 µm.[^pdk-03]
* SkyWater PDK, *Device Details* — NMOS, NPN, PNP, diode and
  `res_generic_nd` descriptions and cross-sections.[^pdk-07]
* SkyWater PDK, *Parasitic Layout Extraction* — N-diffusion sheet
  resistance 120 000 mΩ/sq.[^pdk-08]
* SkyWater, *Facilities & Capabilities* — i-line tools, tracks,
  metrology.[^skw-01]
* SkyWater, Form S-1 (2021) — photoresist suppliers.[^sec-01]

### High-level understanding

* Wikipedia, *Photolithography* — i-line, k₁.[^wiki-litho]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography and implant masking.[^txt-02]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — the CMOS
  source/drain module.[^txt-01]

### Deep dive

* ITRS 2001, *Lithography* — wavelength by layer and node.[^itrs-03]
* Hook et al. (IBM), *IEEE TED* 2003 — lateral straggle and the
  mask-proximity effect.[^hook-2003]
* Sheu et al. (TSMC), *IEEE TED* 2006 — well-edge proximity
  model.[^sheu-2006]
* Drennan, Kniffin and Locascio, CICC 2006 — proximity effects in
  analogue design.[^drennan-2006]
* Levinson, *Principles of Lithography* — overlay budgets.[^levinson-2005]
* Mack, *Fundamental Principles of Optical Lithography* — thick-resist
  imaging.[^mack-2007]
* Fujimura et al. (Fujitsu), *JJAP* 1989 — what an implant does to
  the resist surface.[^fujimura-1989]
* Smith, 1983 — wafer cooling and resist masking in
  implantation.[^smith-1983]
* Romig, Bishop and Rio, IIT 1996 — resist burning in a high-current
  implanter.[^romig-1996]
* Lukaszek, Reno and Bammi, IIT 1996 — resist and wafer charging
  during a high-current arsenic implant.[^lukaszek-1996]
* Lee et al. (Genus), IIT 1996, and Horsky, IIT 1998 — resist
  outgassing under implantation.[^lee-1996][^horsky-1998]
* Buffat and Adams (Zilog), US 6,576,405 — resist design for
  high-energy implants, for contrast.[^pat-resist-zilog]

## Open questions

* The resist, thickness, exposure tool and hardening step for `NSDM`
  are inferred from the design rules and general practice.
* How `cnsdm` is generated from `nsdm` — whether taps, SONOS cells,
  poly heads or other structures are added by Boolean operations —
  is not public beyond the existence of the add/drop purposes.[^pdk-06]
* Whether the SONOS cell source/drain is formed by this implant or
  by a cell-specific one is inferred from the cell being an n-channel
  device; no public source states it.

<!-- footnotes -->

[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the per-device cross-section drawings.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://github.com/google/skywater-pdk/tree/main/docs/rules/device-details>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^sheu-2006]: Y.-M. Sheu, K.-W. Su, S. Tian, S.-J. Yang, C.-C. Wang,
    M.-J. Chen and S. Liu, "Modeling the Well-Edge Proximity Effect in
    Highly Scaled MOSFETs", *IEEE Transactions on Electron Devices*
    **53**(11), 2792–2798 (2006).
    <https://doi.org/10.1109/TED.2006.884070>
[^drennan-2006]: P. G. Drennan, M. Kniffin and D. Locascio,
    "Implications of Proximity Effects for Analog Design", *Proc. IEEE
    Custom Integrated Circuits Conference 2006*, pp. 169–176.
    <https://doi.org/10.1109/CICC.2006.320869>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007,
    ISBN 978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
    (companion site <https://www.lithoguru.com/textbook/>)
[^fujimura-1989]: S. Fujimura, J. Konno, K. Hikazutani and H. Yano,
    "Ashing of Ion-Implanted Resist Layer", *Japanese Journal of Applied
    Physics* **28**(10R), 2130 (1989).
    <https://doi.org/10.1143/JJAP.28.2130>
[^smith-1983]: T. C. Smith, "Wafer Cooling and Photoresist Masking
    Problems in Ion Implantation", in *Ion Implantation: Equipment and
    Techniques*, Springer Series in Electrophysics, Springer, 1983,
    pp. 196–213. <https://doi.org/10.1007/978-3-642-69156-0_25>
[^romig-1996]: T. Romig, M. Bishop and V. Rio, "Exploration and
    prevention of photo resist burning in a high current ion
    implanter", *Proc. 11th International Conference on Ion
    Implantation Technology* (1996), pp. 190–193.
    <https://doi.org/10.1109/IIT.1996.586181>
[^lukaszek-1996]: W. Lukaszek, S. Reno and R. Bammi, "Influence of
    photoresist on wafer charging during high current arsenic
    implant", *Proc. 11th International Conference on Ion Implantation
    Technology* (1996), pp. 89–92.
    <https://doi.org/10.1109/IIT.1996.586135>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy and
    high current ion implantation", *Proc. 1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
[^pat-resist-zilog]: S. J. Buffat and J. L. Adams (Zilog), *High aspect
    ratio photolithographic method for high energy implantation*, US
    6,576,405 B1, granted 2003-06-10.
    <https://patents.google.com/patent/US6576405B1/en>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
