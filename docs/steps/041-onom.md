(step-041)=
# Step 041 — ONOM: ONO mask

| | |
|---|---|
| **Step number** | 41 of 171[^steps-sheet] |
| **Step code** | `ONOM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | FEOL — SONOS and gate dielectrics |
| **Previous step** | {ref}`ONO <step-040>` |
| **Next step** | {ref}`ONOME <step-042>` |

## What this step is

`ONOM` is the second of the three SONOS-specific masks. The
oxide–nitride–oxide stack grown at {ref}`ONO <step-040>` covers the
whole wafer; this lithography step prints resist islands over the memory
transistors and leaves the stack exposed everywhere else, so that
{ref}`ONOME <step-042>` can etch it away from all the logic, 5 V and
high-voltage transistors before their gate oxides are grown. After the
etch the {term}`ONO` survives only as small islands, which, we infer, each cover
a tunnel window opened at {ref}`TUNM <step-035>` and its margin.

The PDK lists "ONO Mask, ONOM" as used in SKY130,[^pdk-05] with the
generated mask layer `conom` (GDS 88:0, "ONO Mask") and a drawing
purpose `conom` at 87:44.[^pdk-06] No `onom` design rules are
published in the periphery-rule set, and there is no described or
rule-bearing drawn `onom` layer for designers: we infer that the mask
is generated from the `tunm` layer (GDS 80:20)[^pdk-06] by oversizing,
so that the ONO island always encloses the tunnel window. That the
memory cells live only inside memory blocks marked `areaid.ce` (rule
tunm.8)[^pdk-periph] means the ONO islands are confined to the array
areas of a design.

The Cypress patents describe the same operation. In one, "a patterned
mask layer … is formed on or overlying the sacrificial oxide layer
234, and the sacrificial oxide, cap layer 232, and the charge-trapping
layer 230 etched or patterned to form a gate stack 236 overlying the
channel 224 of the NVM transistor and to remove the sacrificial oxide,
cap layer, and the charge trapping layers 230 from the second region
208 of the substrate 204"; "The patterned mask layer can include a
photoresist layer patterned using standard lithographic
techniques".[^pat-04] In another, "Conventional lithography and etching
techniques may be employed to remove the charge trapping dielectric
layers from other regions of the substrate, such as the HV MOS region
350 and MOS region 370".[^pat-03]

## Step category

`ONOM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *etch mask* type, printed on a dielectric stack rather than
on resist-friendly oxide alone: the top surface is the {term}`blocking oxide`
(or a sacrificial oxide cap over it[^pat-04]), which behaves like any
other oxide for coating purposes. Its features are the tunnel windows
plus an overlap — 0.410 µm windows[^pdk-periph] grown by a margin that
is not public — so it is a relaxed layer, and we infer an i-line
exposure as for {ref}`TUNM <step-035>`. Its critical {term}`overlay` is, we
infer, to the tunnel mask rather than to active, which is unusual: most
layers align to the {term}`STI` pattern or to poly.

## Why this step exists

The logic transistors must not have an ONO stack under their gates —
a nitride that traps charge is the last thing a 1.8 V or 5 V MOSFET
wants as a gate dielectric — and their gate oxides are grown by
thermal oxidation of bare silicon, which the stack would block. The
stack therefore has to be removed everywhere except the cells, and it
has to be removed *before* the gate oxidations
({ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`), which is where
Cypress's flow puts it: the ONO is formed and patterned, then "the
logic MOS gate insulator" is formed by a thermal process that
"additionally" reoxidises the ONO.[^pat-03] A 2011 Cypress/UMC
press release puts the cost of the module in the 65 nm S65 process at
"three additional mask layers" (it gives no count for S8),[^cyp-22] and
Cypress's 2020 article credits {term}`SONOS` with "the
simplicity of its integration (fewer extra lithography
masks)"[^cyp-25] — `ONOM` is the mask that pays for keeping the ONO
out of the logic.

Two geometric facts about the island matter. It must enclose the
tunnel window with margin, because the silicon inside the window has
only the {term}`tunnel oxide` on it: if the ONO etch reached it, the etch
would land on 1–3 nm of oxide[^pat-04] and then on the channel. And the
island edge is where the logic gate oxide will later grow up against
the nitride sidewall, so the edge must lie on field oxide or on
silicon that becomes part of the select transistor's structure, never
inside a logic channel — which the "(poly and diff) may not straddle
tunm" rule (tunm.5)[^pdk-periph] already guarantees for the window.
The Cypress integration patent notes for its window that "the
dimensions and alignment of window 305 and ONO charge trapping
dielectric stack 306 are important".[^pat-03]

Without `ONOM` the ONO etch would remove the memory stack too, or —
if the etch were skipped — every logic transistor would be a SONOS
transistor.

## How it is typically performed

An industry-generic etch-mask lithography sequence for a 200 mm,
130 nm-era fab (SKY130's recipe is not public):

1. **Surface.** The wafer's top surface is the blocking oxide of the
   ONO stack (or a thin sacrificial oxide over it, "between 2.0 nm and
   4.0 nm" in one Cypress flow[^pat-04]). Dehydration bake and
   {term}`HMDS` prime.
2. **Anti-reflective layer.** Optional. The Cypress integration patent
   uses "an inorganic spin-on anti-reflective coating (ARC)" on top of
   the stack, etched together with it;[^pat-03] on a relaxed i-line
   layer many fabs would omit an {term}`ARC`. If one is used, this
   reference treats its open as part of {ref}`ONOME <step-042>`, as in
   the Cypress flow where the ARC is etched with the stack.[^pat-03]
3. **Resist coat, soft bake.** A positive i-line resist of about 1 µm
   (the PDK's generic 1.14 µm[^pdk-03]); etch {term}`selectivity`, not implant
   stopping, sets the thickness here.
4. **Exposure.** Through the ONO {term}`reticle` on an i-line {term}`stepper` (our
   inference from feature size, as on {ref}`TUNM <step-035>`; ASML
   describes older exposure tools that "migrate to the lithography of
   choice for less critical layers"[^asml-30]). Overlay would be measured to the `TUNM` layer,
   because the island-to-window enclosure is the quantity that matters.
   Levinson's book has a chapter on overlay,[^levinson-2005] and van
   Haren et al. treat how alignment-mark placement limits
   overlay.[^van-haren-2019]
5. **Post-exposure bake, develop** in 2.38 % (0.26 N) TMAH,[^txt-02] rinse,
   hard bake.
6. **Inspection.** Overlay to `TUNM` (inferred), {term}`CD` of the islands, and
   after-develop inspection for resist residue on the open stack, which
   would leave nitride stringers after the etch.

The resist is consumed as the etch mask at {ref}`ONOME <step-042>`
and stripped there (this reference treats the strip as part of that
etch).

## Machines typically used

* **{ref}`i-line stepper <machine-i-line-stepper>`**, 200 mm: ASML PAS 5500/100–/275, Nikon
  NSR-2205i, Canon FPA-3000i ({ref}`category-lithography`).
* **{ref}`Coat/develop track <machine-coat-develop-track>`** (TEL, DNS/SCREEN, Sokudo).
* **{ref}`Overlay metrology <machine-cd-sem-overlay-metrology>`** (KLA-Tencor) and **{term}`CD-SEM`**.

## Machines likely used at SkyWater

* **ASML i-line stepper / scanner.**[^skw-01] Strength: **strong** for
  the tool class; **inference** for assigning `ONOM` to it.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius.**[^skw-01]
  Strength: strong for existence.
* **KLA 5200/5300/Archer overlay; AMAT Verity/VeraSEM CD.**[^skw-01]
  Strength: strong for existence (SkyWater statement); use at this
  mask is an inference.

## Resources required

* **i-line photoresist** ({ref}`lithography materials <material-lithography-materials>`; Dow, JSR, TOK are SkyWater's named
  suppliers[^sec-01]), **HMDS**, optional **inorganic or organic
  ARC**.[^pat-03]
* **2.38 % (0.26 N) TMAH developer**,[^txt-02] edge-bead remover, {ref}`DI water <material-ultrapure-water>`,
  {ref}`nitrogen <material-process-gases>`.
* **The ONO reticle** — chrome on quartz; relaxed features.

## Related steps and cross-references

* Previous: {ref}`ONO <step-040>` (the stack being masked).
* Next: {ref}`ONOME <step-042>` (the etch); then the first gate
  oxidation {ref}`GOX100 <step-043>`.
* The window the island must enclose: {ref}`TUNM <step-035>`.
* The other SONOS masks: {ref}`TUNM <step-035>`,
  {ref}`LDNTM <step-071>`.
* Mask page: {ref}`ONOM <mask-onom>` — the mask's layers, plates,
  renders and design rules.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "ONO Mask, ONOM,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `conom`
  88:0 and 87:44; `tunm` 80:20.[^pdk-06]
* SkyWater PDK, *Periphery rules* — tunm.1, tunm.5, tunm.8.[^pdk-periph]
* SkyWater PDK, *Criteria & Assumptions* — photoresist
  thickness.[^pdk-03]
* SkyWater, *Facilities & Capabilities* — lithography tools, tracks
  and metrology.[^skw-01]
* SkyWater, Form S-1 (2021) — photoresist suppliers.[^sec-01]
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — the
  patterned mask over the stack and what the etch removes.[^pat-04]
* Koutny et al. (Cypress), US 8,093,128 — removal of the stack from
  the HV and LV MOS regions; the inorganic spin-on ARC; the
  importance of window alignment.[^pat-03]
* Cypress/UMC press release — "three additional mask layers" for the
  S65 process; no count is given for S8.[^cyp-22]
* Ramkumar, Prabhakar and Kapre (Cypress), Semiconductor Digest —
  "fewer extra lithography masks".[^cyp-25]

### High-level understanding

* Wikipedia, *Photolithography* — i-line, resolution and
  overlay.[^wiki-litho]
* Wikipedia, *SONOS* — the stack being patterned.[^cyp-26]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography.[^txt-02]

### Deep dive

* ITRS 2001, *Lithography* — the exposure options it lists by node for
  critical layers.[^itrs-03]
* Levinson, *Principles of Lithography* — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]
* van Haren et al., SPIE 2019 — alignment-mark placement and
  layer-to-layer overlay.[^van-haren-2019]
* Mack, *Fundamental Principles of Optical Lithography* — imaging
  and resist theory for relaxed layers.[^mack-2007]
* Baker and Capsuto, SPIE 1996 — ARC and CD control on an i-line
  0.35 µm device.[^baker-1996]
* Kim et al. (Samsung), VLSI 2003 — a manufacturable embedded SONOS
  module and its patterning.[^pap-03]
* Seo et al. (Samsung), *IEEE JSSC* 2005 — a 130 nm local-SONOS
  embedded flash, another vendor's cell geometry.[^pap-02]
* Jiew, Chien and Yung, NVMTS 2012 — the 2T-SONOS cell whose control
  gate the ONO island defines.[^jiew-2012]
* Ramkumar et al. (Cypress), US 6,969,689 — the stack this mask
  protects.[^pat-01]
* Taniguchi et al., IMW 2023 — a three-mask SONOS module on a 130 nm
  platform.[^pap-05]

## Open questions

* The derivation of the ONO mask from `tunm` (oversize value, any
  merging inside the array) is not public.
* Whether the ONO layer is printed on the i-line or {term}`DUV` tools is an
  inference from feature size.
* Whether an ARC is used under the ONO-mask resist, and if so which
  kind, is an open question; this page describes no separate ARC etch
  here.
* Reticle tone and the resist thickness for this layer are not public.

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
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
[^cyp-22]: Cypress Semiconductor / UMC, *Cypress and UMC Deliver ICs on
    New 65-Nanometer SONOS Embedded Flash Technology*, PR Newswire,
    2011-07-27.
    <https://www.prnewswire.com/news-releases/cypress-and-umc-deliver-ics-on-new-65-nanometer-sonos-embedded-flash-technology-126238008.html>
[^cyp-25]: K. Ramkumar, V. Prabhakar and R. Kapre (Cypress
    Semiconductor), *Scalable SONOS based embedded non-volatile memory
    technology*, Semiconductor Digest, 2020-02.
    <https://sst.semiconductor-digest.com/2020/02/scalable-sonos-based-embedded-non-volatile-memory-technology/>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021.
    <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^van-haren-2019]: R. J. F. van Haren, S. Steinert, O. Mouraille,
    K. D'havé, L. van Dijk, J. Hermans and D. Beyer, "Wafer alignment
    mark placement accuracy impact on the layer-to-layer overlay
    performance", *Proc. SPIE* **11148**, Photomask Technology 2019, 37
    (2019). <https://doi.org/10.1117/12.2536270>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^cyp-26]: Wikipedia, *SONOS*. <https://en.wikipedia.org/wiki/SONOS>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007,
    ISBN 978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
    (companion site <https://www.lithoguru.com/textbook/>)
[^baker-1996]: D. C. Baker and E. S. Capsuto, "Critical dimension
    control for i-line 0.35-μm device using a new antireflective
    coating", *Proc. SPIE* **2724**, Advances in Resist Technology and
    Processing XIII, 710 (1996). <https://doi.org/10.1117/12.241869>
[^pap-03]: J.-H. Kim, I. W. Cho, G. J. Bae, S. S. Kim, K. C. Kim,
    S. H. Kim, K. W. Koh, N. I. Lee, H.-K. Kang, K.-P. Suh, S. T. Kang,
    M. K. Seo, S. H. Lee, M. C. Kim and I. S. Park (Samsung), "Highly
    manufacturable SONOS non-volatile memory for the embedded SoC
    solution", *2003 Symposium on VLSI Technology, Digest of Technical
    Papers*, pp. 31–32. <https://doi.org/10.1109/VLSIT.2003.1221071>
[^pap-02]: M.-K. Seo, S.-H. Sim, M.-H. Oh, H.-S. Lee, S.-W. Kim,
    I.-W. Cho, G.-H. Kim and M.-G. Kim (Samsung), "A 130-nm 0.9-V
    66-MHz 8-Mb (256K × 32) local SONOS embedded flash EEPROM", *IEEE
    Journal of Solid-State Circuits* **40**(4), 877–883 (2005).
    <https://doi.org/10.1109/JSSC.2005.845564>
[^jiew-2012]: C. B. Jiew, Y. E. Chien and R. T. T. Yung, "Development
    of a robust 2T-SONOS cell for embedded flash application", *2012
    12th Annual Non-Volatile Memory Technology Symposium (NVMTS)*,
    pp. 1–6. <https://doi.org/10.1109/NVMTS.2013.6632849>
[^pat-01]: K. Ramkumar, M. Rathor, B. Parameshwaran and L. Lancaster
    (Cypress Semiconductor), *Method of manufacturing an
    oxide-nitride-oxide (ONO) dielectric for SONOS-type devices*,
    US 6,969,689 B1, granted 2005-11-29.
    <https://patents.google.com/patent/US6969689B1/en>
[^pap-05]: Y. Taniguchi et al., "SONOS Embedded Flash IP Using
    Trap-Depth-Controlled SiN Film Enabling Data Retention more than
    10 years at 200°C", *2023 IEEE International Memory Workshop
    (IMW)*, pp. 1–4. <https://doi.org/10.1109/IMW56887.2023.10145990>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
