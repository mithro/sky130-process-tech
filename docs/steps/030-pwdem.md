(step-030)=
# Step 030 — PWDEM: P-well drain extended mask

| | |
|---|---|
| **Step number** | 30 of 171[^steps-sheet] |
| **Step code** | `PWDEM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`PWIS <step-029>` |
| **Next step** | {ref}`PWDEI1 <step-031>` |

## What this step is

`PWDEM` prints the *P-well {term}`drain-extended <DEMOS>` mask*, the last lithography of
the well and channel module. A photoresist (thick, we infer) is coated,
exposed and developed to open windows over the regions of the 20 V
devices that are to receive a purpose-built, lightly doped P-well; the
two implants {ref}`PWDEI1 <step-031>` and {ref}`PWDEI2 <step-032>`
follow (through the same resist in the sequence this reference
describes), and the
resist is stripped at {ref}`PWDEIS <step-033>`.

The drawn layer is `pwde` (GDS 124:20), "Regions to receive p-well
drain-extended implants".[^pdk-06] Its rules (pwdem.1–pwdem.6) have no
public numeric values but fix the geometry: `pwde` "must be enclosed by
UHVI" (pwdem.4), the 20 V node identifier; "pwdem.dg inside UHVI must be
enclosed by deep nwell" (pwdem.5), with a minimum enclosure by deep
N-well (pwdem.6); and it must be enclosed by the P-well block layer
`pwbm` (pwdem.3).[^pdk-periph] Read together with the `pwbm` description
— "Regions (in UHVI) blocked from p-well implant (DE MOS devices
only)"[^pdk-06] — the sequence is: the standard P-well was kept *out* of
the 20 V device area at {ref}`PWBM <step-026>`, and `PWDEM` now puts a
*different* P-well back into part of it, inside a deep-N-well tub.

The PDK's mask table lists "P-Well Drain Extended, PWDEM" but, as for
PWBM, leaves the "Used in SKY130" column blank;[^pdk-05] the layer and
its rules exist,[^pdk-06] so this reference treats the blank as a
documentation inconsistency (see *Open questions*).

## Step category

`PWDEM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *thick-resist implant-block* type, aligned (we infer) to the
{term}`STI` pattern and used only by the high-voltage device family. Its
features are large — the 20 V devices have drawn channel lengths of the
order of a micrometre (the PDK's HV methodology gives 1.055 µm and
1.050 µm for the 16 V VHV NMOS and PMOS[^pdk-hv]) and {term}`drift regions <drift region>`
longer still.[^pdk-07]

## Why this step exists

SKY130 is a multi-voltage process: a 1.8 V core, 5 V I/O, and "HV
extended-drain NMOS and PMOS"[^pdk-10] rated in the PDK at 10/16 V
(`nfet_g5v0d16v0`, `pfet_g5v0d16v0`) and 20 V (`nfet_20v0`, `pfet_20v0`,
`nfet_20v0_iso`, `nfet_20v0_nvt`, `nfet_20v0_zvt`);[^pdk-07] SkyWater's
platform table lists "20+V, Drain-Extended CMOS (16V)" for
S130.[^skw-02] A drain-extended (DE) MOSFET keeps the thin gate oxide
and short channel of a 5 V transistor but inserts a lightly doped
*drift* region between channel and drain: "Drain extended transistors
differ from regular self aligned polysilicon gate transistors in that
they use a very lightly doped extension region adjacent to the drain
that depletes at high drain voltages".[^pat-demos-ti] The PDK says the
same for its own devices: "The VHV devices need to be designed with
drain extentions (DE) fabricated by lightly doped Nwells and Pwells
respectively" and "All VHV devices use 110A gate oxide thickness just
like standard 5.0V Vcc devices".[^pdk-hv]

For the 16 V devices the ordinary wells serve, we infer, as the drift
regions;[^pdk-hv] a second TI patent notes that DE devices can be made
"without the addition of extra masks or processing
steps".[^pat-demos-ti2] For the 20 V devices the standard P-well is too
heavily doped: a drift region must deplete fully at the rated voltage,
which requires a doping and depth that a 4 × 10¹⁷ cm⁻³ well[^pdk-03]
cannot provide. `PWDEM` therefore defines where a lighter, custom P-well
goes — we infer, the drift region of the 20 V PMOS and the body of the
20 V NMOS whose standard P-well was blocked. This is what makes the 20 V
devices "similar construction to the 11V/16V NMOS FET, with several
differences: Longer drift region, Longer poly gate, Larger W/L, Devices
placed in pairs".[^pdk-07]

## How it is typically performed

An industry-generic drain-extension well lithography for a 200 mm,
130 nm-era fab:

1. **Track preparation.** {term}`HMDS` prime; no {term}`BARC` for micrometre-scale
   features (inference).[^wiki-litho]
2. **Thick resist coat.** The resist must stop the deepest
   drain-extension implant. A DE well is *lighter* than the main well
   but not necessarily shallower — a deep, graded drift region gives the
   best breakdown — so a 2 µm-class implant resist like that of
   {ref}`PWBM <step-026>` is plausible (inference;[^txt-02] compare
   IBM's 1800–2500 nm for 550 keV boron[^pat-well-ibm]).
3. **Exposure.** i-line; the layer's features are
   micrometre-scale[^pdk-hv] and its {term}`overlay` requirements are set by the
   drift-region length rather than by a sub-micrometre {term}`CD`. We infer an
   **i-line layer**.
4. **Alignment** to STI. In a DE device the field-oxide length and the
   poly-to-drift overlap are reliability-critical — "Under no
   circumstances the poly/extended drain overlap and field oxide length
   should be changed"[^pdk-hv] — so the well edge position relative to
   the STI, and later the poly, matters more than for an ordinary well.
5. **Develop, hard bake, inspect.**

## Machines typically used

* **i-line {term}`stepper`**, 200 mm (ASML PAS 5500/100–/275, Nikon NSR-2205i,
  Canon FPA-3000i).[^txt-05]
* **Coat/develop track** with thick-resist capability; **overlay tool**.

## Machines likely used at SkyWater

* **ASML i-line stepper / scanner**.[^skw-01] Strength: **strong** for
  existence; assignment is an **inference** from the coarse geometry.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius**.[^skw-01] Strength:
  strong for existence.
* **Overlay — KLA 5200/5300/Archer**.[^skw-01] Strength: strong.

## Resources required

* **Thick positive i-line implant resist** (inference); suppliers named
  in SkyWater's S-1: Dow, JSR, Tokyo Ohka Kogyo.[^sec-01]
* **HMDS**, **TMAH developer**, edge-bead remover, DI water, nitrogen.
* **The PWDEM {term}`reticle`** (from `pwde`).[^pdk-06]

## Related steps and cross-references

* Previous: {ref}`PWIS <step-029>`.
* Next: {ref}`PWDEI1 <step-031>` and {ref}`PWDEI2 <step-032>` through
  this resist; strip at {ref}`PWDEIS <step-033>`.
* The standard P-well blocked from these regions: {ref}`PWBM <step-026>`;
  the deep N-well tub they sit in: {ref}`DNM <step-007>`; the N-well
  drift regions of the DE NMOS: {ref}`NWM <step-017>`.
* Previous mask: {ref}`PWBM <step-026>`; next mask:
  {ref}`TUNM <step-035>`.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "P-Well Drain Extended,
  PWDEM".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `pwde` 124:20;
  `pwbm` 19:44; `uhvi` 74:22.[^pdk-06]
* SkyWater PDK, *Periphery rules* — pwdem.1–pwdem.6.[^pdk-periph]
* SkyWater PDK, *Device Details* — 20 V NMOS/PMOS, isolated, native and
  zero-Vt 20 V NMOS; 10/16 V devices.[^pdk-07]
* SkyWater PDK, *High Voltage Methodology* — DE by lightly doped wells;
  110 Å oxide; channel lengths; poly/drift overlap rule.[^pdk-hv]
* google/skywater-pdk repository README — "HV extended-drain NMOS and
  PMOS".[^pdk-10]
* SkyWater PDK, *Criteria & Assumptions* — P-well peak
  concentration.[^pdk-03]
* SkyWater, *Facilities & Capabilities* — the site tool list.[^skw-01]
* SkyWater, *Mixed-Signal CMOS & ROIC* platform table — "20+V,
  Drain-Extended CMOS (16V)".[^skw-02]
* SkyWater, Form S-1 (2021) — photoresist, gas and chemical
  suppliers.[^sec-01]

### High-level understanding

* Wikipedia, *LDMOS* — drift region formed by implantation.[^wiki-ldmos]
* Wikipedia, *Photolithography* — 365 nm i-line and CD =
  {term}`k₁ <k1>`·λ/{term}`NA`.[^wiki-litho]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography, resist stripping, wafer cleaning and implantation
  chapters.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — lithography
  tools, implanted-resist stripping and {term}`RTP` of the 0.25–0.13 µm
  generations.[^txt-05]

### Deep dive

* Mitros (Texas Instruments), US 6,660,603 — drain-extended MOS built on
  the existing wells, with drift-well doses and energies.[^pat-demos-ti]
* Chidambaram (Texas Instruments), US 2006/0006461 — DE devices "without
  the addition of extra masks or processing steps".[^pat-demos-ti2]
* Mitros et al. (Texas Instruments), *IEEE TED* 2001 — drain-extended
  MOS transistors added to a 0.18 µm logic process.[^mitros-2001]
* Mai and Rücker (IHP), *Solid-State Electronics* 2011 — DE devices in a
  0.13 µm technology.[^mai-2011]
* Breitwisch, Lam and Slinkman (IBM), US 6,667,205 — resist thickness
  for keV-hundreds boron.[^pat-well-ibm]
* Appels and Vaes (Philips), IEDM 1979 — the original RESURF paper: why
  a thin, lightly doped layer holds off high voltage.[^appels-1979]
* Ludikhuize (Philips), ISPSD 2000 — a review of RESURF design rules for
  drift regions.[^ludikhuize-2000]
* Baliga, *Fundamentals of Power Semiconductor Devices* — breakdown,
  drift-region doping and on-resistance trade-offs.[^baliga-2008]
* Efland, Tsai and Pendharkar (Texas Instruments), IEDM 1998 — LDMOS
  integration into logic CMOS from the TI group behind the DE
  devices.[^efland-1998]
* Kwon, Efland, Malhi and Ng (Texas Instruments), US 5,406,110 — a
  RESURF lateral DMOS with an implanted drift region.[^pat-resurf-ti]
* Buffat and Adams (Zilog), US 6,576,405 — thick-resist lithography for
  high-energy implants.[^pat-resist-zilog]
* Lee et al. (Genus), IIT 1996 — outgassing of thick resists during MeV
  implantation.[^lee-1996]

## Open questions

* Whether `pwde` defines the body of the 20 V NMOS, the drift region
  of the 20 V PMOS, or both, is inferred from the rule geometry; the
  PDK's 20 V cross-section drawings are not labelled in text form.
* The blank "Used in SKY130" entry for PWDEM in the PDK mask table sits
  oddly with the existence of the `pwde` layer and its rules; we treat
  it as a documentation inconsistency that cannot be resolved publicly.
* Resist thickness and exposure tool are inferred.

<!-- footnotes -->

[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README. <https://github.com/google/skywater-pdk>
[^skw-02]: SkyWater Technology, *Mixed-Signal CMOS & ROIC*, platform
    table, accessed 2026-08-30.
    <https://www.skywatertechnology.com/cmos/>
[^pat-demos-ti]: J. C. Mitros (Texas Instruments), *Higher voltage drain
    extended MOS transistors with self-aligned channel and drain
    extensions*, US 6,660,603 B2, granted 2003-12-09.
    <https://patents.google.com/patent/US6660603B2/en>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-ldmos]: Wikipedia, *LDMOS*. <https://en.wikipedia.org/wiki/LDMOS>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^pat-demos-ti2]: P. R. Chidambaram (Texas Instruments), *Drain extended
    MOS transistors and methods for making the same*, US 2006/0006461
    A1, published 2006-01-12.
    <https://patents.google.com/patent/US20060006461A1/en>
[^mitros-2001]: J. C. Mitros, C.-Y. Tsai, H. Shichijo, M. Kunz, A.
    Morton, D. Goodpaster, D. Mosher and T. R. Efland, "High-voltage
    drain extended MOS transistors for 0.18-µm logic CMOS process",
    *IEEE Transactions on Electron Devices* **48**(8), 1751–1755 (2001).
    <https://doi.org/10.1109/16.936703>
[^mai-2011]: A. Mai and H. Rücker, "Drain-extended MOS transistors
    capable for operation at 10 V and at radio frequencies",
    *Solid-State Electronics* **65–66**, 45–50 (2011).
    <https://doi.org/10.1016/j.sse.2011.06.034>
[^pat-well-ibm]: M. J. Breitwisch, C. H. Lam and J. A. Slinkman (IBM),
    *Method of forming retrograde n-well and p-well*, US 6,667,205 B2,
    granted 2003-12-23.
    <https://patents.google.com/patent/US6667205B2/en>
[^appels-1979]: J. A. Appels and H. M. J. Vaes, "High voltage thin layer
    devices (RESURF devices)", *1979 International Electron Devices
    Meeting*, pp. 238–241. <https://doi.org/10.1109/IEDM.1979.189589>
[^ludikhuize-2000]: A. W. Ludikhuize, "A review of RESURF technology",
    *Proc. 12th International Symposium on Power Semiconductor Devices &
    ICs* (2000), pp. 11–18. <https://doi.org/10.1109/ISPSD.2000.856763>
[^baliga-2008]: B. J. Baliga, *Fundamentals of Power Semiconductor
    Devices*, Springer, 2008, ISBN 978-0-387-47313-0.
    <https://doi.org/10.1007/978-0-387-47314-7>
[^efland-1998]: T. R. Efland, C.-Y. Tsai and S. Pendharkar, "Lateral
    thinking about power devices (LDMOS)", *IEDM 1998 Technical Digest*,
    pp. 679–682. <https://doi.org/10.1109/IEDM.1998.746447>
[^pat-resurf-ti]: O.-K. Kwon, T. R. Efland, S. Malhi and W. T. Ng (Texas
    Instruments), *Resurf lateral double diffused insulated gate field
    effect transistor*, US 5,406,110 A, granted 1995-04-11.
    <https://patents.google.com/patent/US5406110A/en>
[^pat-resist-zilog]: S. J. Buffat and J. L. Adams (Zilog), *High aspect
    ratio photolithographic method for high energy implantation*, US
    6,576,405 B1, granted 2003-06-10.
    <https://patents.google.com/patent/US6576405B1/en>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
