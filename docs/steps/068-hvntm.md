(step-068)=
# Step 068 — HVNTM: HV N-tip mask formation

| | |
|---|---|
| **Step number** | 68 of 171[^steps-sheet] |
| **Step code** | `HVNTM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | {term}`FEOL` — extensions, spacers, source/drain |
| **Previous step** | {ref}`ASTIS <step-067>` |
| **Next step** | {ref}`HVASTI <step-069>` |

## What this step is

`HVNTM` is the second tip mask of the module. On the surface cleaned at
{ref}`ASTIS <step-067>` it patterns a resist that exposes the
*high-voltage* NMOS transistors — those built on the 110 Å thick gate
oxide inside the `hvi` regions[^pdk-hv] — and covers everything else,
so that the arsenic implant {ref}`HVASTI <step-069>` forms their
lightly doped, graded drain {term}`extension`. The resist is removed at
{ref}`HVASTIS <step-070>`.

The PDK lists "High Volt. N-tip, HVNTM" as a mask used in
SKY130.[^pdk-05] Unlike the standard tip, this one has a designer-drawn
layer, `hvntm` (GDS 125:20, "High voltage N-tip implant"), and a
generated mask layer `chvntm` (39:0, "High voltage N-tip implant
mask") with a drawing purpose at 38:20.[^pdk-06] Its design rules are
headed "Defines tip implants for the HV NMOS" and begin with "Hvntm can
be drawn inside HVI. Drawn layer will be OR-ed with the CL and
rechecked for CLDRC" — which we read as: the {term}`reticle` is the
union of what the designer draws and a computed layer (the PDK does not
expand "CL").[^pdk-periph] The rules are coarse:
width 0.700 µm (hvntm.1), spacing 0.700 µm (hvntm.2), enclosure of n⁺
diffusion inside `hvi` by 0.185 µm (hvntm.3), a 0.185 µm space to n⁺
diffusion outside `hvi` and to p⁺ diffusion (hvntm.4, hvntm.5), "Hvntm
must overlap hvi" (hvntm.10) and "Hvntm must not overlap areaid.ce"
(hvntm.9), i.e. it is kept out of the SRAM core.[^pdk-periph]

The PDK's assumptions page is unusually explicit about this mask. Its
implant-angle table gives "Angle for HV tip implant" 40° and "Twist
angle for HV Tip" 23°; its physical-criteria table gives "Photoresist
thickness for HV Tip Implants" 0.3 µm (against 1.14 µm for the standard
resist), "HVNTM shadowing" 0.232 µm and "Min width of tip implant
opening" 0.1 µm; and its high-voltage table gives "Photoresist tilted
implant penetration" 0.02 µm, "Photoresist tilted implant blocking
distance" 0.013 µm, "Min size of HVTip" 0.1 µm and an "Extra CD tol for
HVNTM" of 0.015 µm.[^pdk-03] These numbers are mutually consistent: a
0.3 µm resist wall {term}`shadows <shadowing>` a 40° beam for 0.3 µm × tan 40° ≈ 0.25 µm,
which less the 0.02 µm the beam penetrates at the resist edge gives
the 0.232 µm figure (our arithmetic). We therefore read `HVNTM` as a
*thin-resist* mask for a *large-tilt* implant.

## Step category

`HVNTM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *implant-block* type, with a twist: the resist is about a
quarter of the usual thickness,[^pdk-03] because the implant it admits
arrives at 40° and a tall resist wall would shadow the gate edges it
is meant to reach. Thin resist is easier to image but must still stop
the implant everywhere else; at the tens of keV of an LDD-type arsenic
implant (typical),[^txt-04] 0.3 µm of resist is ample (the projected
range of arsenic at such energies is a few tens of nanometres in
resist-like materials).[^txt-01]

## Why this step exists

A 5 V NMOS cannot use the 1.8 V tip. The extension of
{ref}`ASTI <step-065>` is shallow, abrupt and heavily doped for drive
current at 0.15 µm; at 5.5 V on the drain such a junction would put the
peak lateral field at the gate edge and generate hot carriers at a rate
that destroys the device in hours — the degradation Hu and co-workers
modelled and showed how to monitor.[^hu-1985-hci] The classical remedies
are the lightly doped drain,[^ogura-1980] the double-diffused
drain[^takeda-1982] and, most relevant here, the *large-angle-tilt
implanted drain* ({term}`LATID`) of Hori, in which a tilted n⁻ implant is
driven under the gate edge so that the drain field is graded and
overlapped by the gate;[^hori-1989-latid][^hori-1992] Rafí and Campabadal
compared the hot-carrier behaviour of {term}`LDD` and LATID
devices directly.[^rafi-2001] The PDK's 40° HV tip angle[^pdk-03] is
the signature of exactly this kind of drain, and the PDK's Table F2b
marks `HVNTM` "created" for `nfet_g5v0d10v5`, the ESD NMOS built on it,
the 5 V and 3.3 V native NMOS, the 16 V drain-extended NMOS, four HV
diodes, an HV n-diffusion resistor and an HV varactor,[^pdk-06] so this is where those
devices' n-type extension is defined; how the implant is placed
relative to a drain-extended device's drift well is not stated. The
{term}`drain-extended <DEMOS>` 20 V
NMOS, which shares the 110 Å oxide,[^pdk-hv] uses an N-well {term}`drift region`
as its drain extension[^pdk-hv][^mitros-2001] and Table F2b marks it "-"
("Layer not created for the device"), so it does not take this tip; the
PDK's rule that `hvntm`
"must enclose ESD_nwell_tap inside hvi" (hvntm.7)[^pdk-periph] shows
that the layer is used on more than plain transistors.

Cypress, which the PDK says developed the technology SKY130 comes
from,[^pdk-02] patented
a "high-voltage device with self-aligned graded junctions" in a CMOS
flow;[^pat-hv-graded-cyp] the patent's inventor is also a named
inventor on the embedded-SONOS patent used throughout this reference,
which is circumstantial evidence that a graded-junction HV device of
this kind belongs to the same process lineage — we state it as no more
than that.

Without `HVNTM`, the 5 V transistors would either take the 1.8 V tip
and fail hot-carrier lifetime, or take no tip and have an undoped gap
under the {term}`spacer` between channel and n⁺ drain.

## How it is typically performed

An industry-generic thin-resist implant-mask sequence for a 200 mm,
130 nm-era fab:

1. **Surface preparation.** Dehydration bake and {term}`HMDS` prime on the
   screen-oxide surface left by {ref}`ASTIS <step-067>`.
2. **Resist coat.** A thin positive resist — the PDK's 0.3 µm
   "Photoresist thickness for HV Tip Implants"[^pdk-03] — spun at a
   speed and dilution chosen for that thickness. A thin film conforms
   more closely to the 0.18 µm poly steps,[^pdk-03] which reduces
   resist pooling beside gates, but is more prone to pinholes and to
   reflective notching; the PDK's "Photoresist tilted implant
   penetration" of 0.02 µm[^pdk-03] acknowledges that the resist edge
   is not a perfect wall to a 40° beam.
3. **Exposure.** The 0.7 µm width and space rules[^pdk-periph] are far
   above i-line resolution ({term}`k₁ <k1>` ≈ 1.2 at {term}`NA` 0.6);[^wiki-litho] with older
   exposure tools migrating, in ASML's words, "to the lithography of
   choice for less critical layers",[^asml-30] we infer an i-line
   exposure.
4. **Alignment.** To poly (inferred; the alignment tree is not public).
   The {term}`overlay` requirement comes from the shadowing geometry: the
   0.232 µm "HVNTM shadowing" and 0.1 µm minimum tip-opening
   width[^pdk-03] fix how far a resist edge must stand from a gate for
   the tilted beam to reach it on the intended side.
5. **Develop** in 2.38 % (0.26 N) TMAH,[^txt-02] rinse, dry; a post-develop bake
   or UV cure to stabilise the thin film against the implant (industry
   practice).[^txt-02]
6. **Inspection.** Overlay to poly; {term}`CD`; after-develop defect
   inspection, which matters more than usual because pinholes in a
   0.3 µm film would let arsenic through.

## Machines typically used

* **{ref}`i-line <machine-i-line-stepper>` {term}`stepper`**, 200 mm: ASML PAS 5500/100–/275 series, Nikon
  NSR-2205i, Canon FPA-3000i.[^txt-05]
* **{ref}`Coat/develop track <machine-coat-develop-track>`** with a thin-resist recipe (TEL, DNS/SCREEN,
  Sokudo).
* **{ref}`Overlay metrology <machine-cd-sem-overlay-metrology>`** (KLA-Tencor 5xxx/Archer) and a {term}`CD-SEM`.

## Machines likely used at SkyWater

* **ASML i-line stepper / i-line scanner.** SkyWater lists "ASML I-line
  stepper" and "ASML I-line scanner".[^skw-01] Strength: **strong** for
  the tools; **inference** for the assignment of `HVNTM` to them.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius**.[^skw-01] Strength:
  strong for existence.
* **Overlay — KLA 5200/5300/Archer; CD — AMAT Verity/VeraSEM**.[^skw-01]
  Strength: strong for existence (SkyWater statement); use at this
  mask is an inference.

## Resources required

* **Positive i-line photoresist** ({ref}`lithography materials <material-lithography-materials>`) at a thin-film viscosity, about
  0.3 µm;[^pdk-03] SkyWater's 2021 S-1 names The Dow Chemical Company, JSR
  Corporation and Tokyo Ohka Kogyo America as photoresist
  suppliers.[^sec-01]
* **HMDS**, **2.38 % (0.26 N) TMAH developer**,[^txt-02] edge-bead remover, {ref}`DI water <material-ultrapure-water>`, {ref}`nitrogen <material-process-gases>`.
* **The HVNTM reticle** — generated from the drawn `hvntm` layer OR-ed
  with "the CL" (read as a computed layer).[^pdk-periph][^pdk-06]

## Related steps and cross-references

* Previous: {ref}`ASTIS <step-067>` (clean surface); the thick-oxide
  regions this mask serves were defined at {ref}`LVOM <step-044>`
  (`hvi`) and oxidised at {ref}`GOX100 <step-043>`.
* Next: {ref}`HVASTI <step-069>` (the 40° arsenic implant), then
  {ref}`HVASTIS <step-070>` (strip).
* Sibling tip masks: {ref}`NTM <step-064>` (1.8 V NMOS),
  {ref}`LDNTM <step-071>` ({term}`SONOS` transistors).
* The drain-extended devices' N-well drift regions:
  {ref}`NWM <step-017>`, {ref}`PWDEM <step-030>`; activation:
  {ref}`TIPRTAD <step-075>`.
* Mask page: {ref}`HVNTM <mask-hvntm>` — the mask's layers, plates,
  renders and design rules.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,793,090 A <patent-gp25122771>` — Integrated circuit having multiple LDD and/or source/drain implant steps to enhance circuit performance (1997)
* {ref}`US 6,586,806 B1 <patent-gp26739424>` — Method and structure for a single-sided non-self-aligned transistor (1997)
* {ref}`US 6,660,603 B2 <patent-gp22880690>` — Higher voltage drain extended MOS transistors with self-aligned channel and drain extensions (2000)
* {ref}`US 6,531,366 B1 <patent-gp25418952>` — Method and structure for high-voltage device with self-aligned graded junctions (2001)

:::{dropdown} 2 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 9,111,985 B1 <patent-gp53786102>` — unknown
* {ref}`US 7,936,023 B1 <patent-gp43903297>` — unknown
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "High Volt. N-tip,
  HVNTM, X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `hvntm`
  125:20; `chvntm` 39:0, 38:20; `hvi` 75:20.[^pdk-06]
* SkyWater PDK, *Periphery rules* — hvntm.X.1, hvntm.1–hvntm.10, the
  "Defines tip implants for the HV NMOS" heading.[^pdk-periph]
* SkyWater PDK, *Error Messages* page and `errors.csv` — the `chvntm`
  checks on the undefined `CLHVNTM` layer.[^pdk-errors]
* SkyWater PDK, *Criteria & Assumptions* — 40° HV tip angle, 23°
  twist, 0.3 µm HV-tip resist, 0.232 µm HVNTM shadowing, 0.02 µm
  penetration, 0.013 µm blocking distance, 0.1 µm minimum HV tip.[^pdk-03]
* SkyWater PDK, *High Voltage Methodology* — 110 Å gate oxide for the
  5 V and drain-extended families; N-well drain extensions.[^pdk-hv]
* SkyWater PDK, *Device Details* — the 5 V NMOS, native 5 V NMOS and
  ESD NMOS devices.[^pdk-07]
* SkyWater, *Facilities & Capabilities* — ASML i-line tools, tracks,
  metrology.[^skw-01]
* SkyWater, Form S-1 (2021) — photoresist suppliers.[^sec-01]

### High-level understanding

* Wikipedia, *Hot-carrier injection* — the failure mode this drain
  design exists to prevent.[^wiki-hci]
* Wikipedia, *Photolithography* — i-line resolution.[^wiki-litho]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — LDD, DDD and
  LATID drain structures and hot-carrier reliability.[^txt-04]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography and implant masking.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — lithography
  tools of the era.[^txt-05]

### Deep dive

* Hori (Matsushita), IEDM 1989 — the quarter-micron LATID transistor
  for 3.3 V operation.[^hori-1989-latid]
* Hori et al. (Matsushita), *IEEE TED* 1992 — the full account of
  large-angle-tilt implanted drain technology.[^hori-1992]
* Hu et al. (Berkeley), *IEEE TED* 1985 — the hot-electron degradation
  model that sets the lifetime target.[^hu-1985-hci]
* Takeda et al. (Hitachi), *IEEE TED* 1982 — drain structures for
  minimising hot-carrier generation.[^takeda-1982]
* Ogura et al. (IBM), *IEEE TED* 1980 — the lightly doped
  drain.[^ogura-1980]
* Rafí and Campabadal, *Solid-State Electronics* 2001 — hot-carrier
  degradation of LDD versus LATID NMOS.[^rafi-2001]
* King, Lacoe and Wang-Ratkovic, IRPS 2000 — the role of the spacer
  oxide in hot-carrier stress of LDD NMOS.[^king-2000]
* Chen et al., *Solid-State Electronics* 1995 — beam shadowing in
  LATID devices, the effect behind the PDK's shadowing
  allowance.[^chen-1995]
* Mitros et al. (TI), *IEEE TED* 2001 — drain-extended transistors in
  a logic process, the other high-voltage drain design in SKY130.[^mitros-2001]
* Kouznetsov (Cypress), US 6,531,366 — a high-voltage device with
  self-aligned {term}`graded junctions <graded junction>` in a CMOS flow.[^pat-hv-graded-cyp]
* Mitros (TI), US 6,660,603 — drain-extended transistors with
  self-aligned channel and drain extensions.[^pat-demos-ti]
* Gardner, Hause and Fulford (AMD), US 5,793,090 — separate LDD
  implants for different transistors on one chip.[^pat-multi-ldd-amd]
* ITRS 2001, *Lithography* — the exposure options it lists by node for
  critical layers.[^itrs-03]
* Mack, *Fundamental Principles of Optical Lithography* — thin-resist
  imaging and reflective notching.[^mack-2007]

## Open questions

* Table F2b marks `HVNTM` "C (CREATED)" on the 5/10.5 V NMOS, the 5 V
  and 3 V native NMOS, the 16 V drain-extended NMOS, the HV and HV
  native ESD NMOS, the HV n-diffusion resistor, the HV varactor and
  four n-type diodes, and "-" ("Layer not created for the device") on
  every PMOS row and on all five UHV 5/20 V rows;[^pdk-06] see the
  {ref}`HVNTM mask page <mask-hvntm>`. What the table does not say is
  why the 20 V devices are excluded, or on which side of a
  drain-extended device the implant lands.
* The resist chemistry used at 0.3 µm (an i-line resist thinned, or a
  dedicated thin-film product) is not public.
* Whether "the CL" (read here as a computed layer) OR-ed with the drawn
  `hvntm`[^pdk-periph]
  is derived from `hvi` and `nsdm`, as we assume, is not stated in the
  periphery rules or on the Error Messages page; the latter's checks on
  an undefined `CLHVNTM` layer, such as "0.185 Min Enclosure of ndiff
  inside hvi by chvntm" (`chvntm.3`) and "0.7 min. width of CLHVNTM"
  (`chvntm.1`), state what the layer must cover and its width and
  spacing, not the operation that makes it; the
  {ref}`HVNTM mask page <mask-hvntm>` reads them.[^pdk-errors]
* No public source places `HVNTM` on a particular exposure tool; the
  i-line assignment follows from the 0.7 µm rules.

<!-- footnotes -->

[^pdk-02]: SkyWater PDK Authors, *Background*, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/background.html>
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
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing". <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-hci]: Wikipedia, *Hot-carrier injection*.
    <https://en.wikipedia.org/wiki/Hot-carrier_injection>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-04]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
    Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
    <https://openlibrary.org/isbn/9780961672157>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021, accessed
    2026-09-13. <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
[^hori-1989-latid]: T. Hori, "1/4-μm LATID (LArge-Tilt-angle Implanted
    Drain) technology for 3.3-V operation", *IEDM 1989 Technical
    Digest*, pp. 777–780. <https://doi.org/10.1109/IEDM.1989.74169>
[^hori-1992]: T. Hori, J. Hirase, Y. Odake and T. Yasui,
    "Deep-submicrometer large-angle-tilt implanted drain (LATID)
    technology", *IEEE Transactions on Electron Devices* **39**(10),
    2312–2324 (1992). <https://doi.org/10.1109/16.158803>
[^hu-1985-hci]: C. Hu, S. C. Tam, F.-C. Hsu, P.-K. Ko, T.-Y. Chan and K. W.
    Terrill, "Hot-electron-induced MOSFET degradation — Model, monitor,
    and improvement", *IEEE Transactions on Electron Devices* **32**(2),
    375–385 (1985). <https://doi.org/10.1109/T-ED.1985.21952>
[^takeda-1982]: E. Takeda, H. Kume, T. Toyabe and S. Asai,
    "Submicrometer MOSFET structure for minimizing hot-carrier
    generation", *IEEE Transactions on Electron Devices* **29**(4),
    611–618 (1982). <https://doi.org/10.1109/T-ED.1982.20752>
[^ogura-1980]: S. Ogura, P. J. Tsang, W. W. Walker, D. L. Critchlow and
    J. F. Shepard, "Design and characteristics of the lightly doped
    drain-source (LDD) insulated gate field-effect transistor", *IEEE
    Transactions on Electron Devices* **27**(8), 1359–1367 (1980).
    <https://doi.org/10.1109/T-ED.1980.20040>
[^rafi-2001]: J. M. Rafí and F. Campabadal, "Hot-carrier degradation in
    deep-submicrometer nMOSFETs: lightly doped drain vs. large angle
    tilt implanted drain", *Solid-State Electronics* **45**(8),
    1391–1401 (2001). <https://doi.org/10.1016/S0038-1101(01)00004-1>
[^king-2000]: E. E. King, R. C. Lacoe and J. Wang-Ratkovic, "The role
    of the spacer oxide in determining worst-case hot-carrier stress
    conditions for NMOS LDD devices", *Proc. 2000 IEEE International
    Reliability Physics Symposium*, pp. 83–92.
    <https://doi.org/10.1109/RELPHY.2000.843895>
[^chen-1995]: H.-S. Chen, C.-S. Teng, L. Moberly and R. Lahri, "Ion beam
    shadowing effect in submicrometer large-angle-tilt implanted drain
    (LATID) MOSFETs", *Solid-State Electronics* **38**(7), 1321–1323
    (1995). <https://doi.org/10.1016/0038-1101(94)00256-F>
[^mitros-2001]: J. C. Mitros, C.-Y. Tsai, H. Shichijo, M. Kunz, A.
    Morton, D. Goodpaster, D. Mosher and T. R. Efland, "High-voltage
    drain extended MOS transistors for 0.18-µm logic CMOS process",
    *IEEE Transactions on Electron Devices* **48**(8), 1751–1755 (2001).
    <https://doi.org/10.1109/16.936703>
[^pat-hv-graded-cyp]: I. Kouznetsov (Cypress Semiconductor), *Method
    and structure for high-voltage device with self-aligned graded
    junctions*, US 6,531,366 B1, granted 2003-03-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6531366>
[^pat-demos-ti]: J. C. Mitros (Texas Instruments), *Higher voltage drain
    extended MOS transistors with self-aligned channel and drain
    extensions*, US 6,660,603 B2, granted 2003-12-09.
    <https://patents.google.com/patent/US6660603B2/en>
[^pat-multi-ldd-amd]: M. I. Gardner, F. N. Hause and H. J. Fulford
    (Advanced Micro Devices), *Integrated circuit having multiple LDD
    and/or source/drain implant steps to enhance circuit performance*,
    US 5,793,090 A, granted 1998-08-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5793090>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
    (companion site <https://www.lithoguru.com/textbook/>)
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
