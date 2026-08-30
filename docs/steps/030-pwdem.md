(step-030)=
# Step 030 — PWDEM: P-well drain extended mask

| | |
|---|---|
| **Step number** | 30 of 171 |
| **Step code** | `PWDEM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`PWIS <step-029>` |
| **Next step** | {ref}`PWDEI1 <step-031>` |

## What this step is

`PWDEM` prints the *P-well drain-extended mask*, the last lithography
of the well and channel module. A thick photoresist is coated,
exposed and developed to open windows over the regions of the 20 V
devices that are to receive a purpose-built, lightly doped P-well; the
two implants {ref}`PWDEI1 <step-031>` and {ref}`PWDEI2 <step-032>`
follow, and the resist is stripped at {ref}`PWDEIS <step-033>`.

The drawn layer is `pwde` (GDS 124:20), "Regions to receive p-well
drain-extended implants" (PDK-06). Its rules (pwdem.1–pwdem.6) have
no public numeric values but fix the geometry: `pwde` "must be
enclosed by UHVI" (pwdem.4), the 20 V node identifier; "pwdem.dg
inside UHVI must be enclosed by deep nwell" (pwdem.5), with a minimum
enclosure by deep N-well (pwdem.6); and it must be enclosed by the
P-well block layer `pwbm` (pwdem.3) (PDK-PERIPH). Read together with
the `pwbm` description — "Regions (in UHVI) blocked from p-well
implant (DE MOS devices only)" (PDK-06) — the sequence is: the
standard P-well was kept *out* of the 20 V device area at
{ref}`PWBM <step-026>`, and `PWDEM` now puts a *different* P-well
back into part of it, inside a deep-N-well tub.

The PDK's mask table lists "P-Well Drain Extended, PWDEM" but, as for
PWBM, leaves the "Used in SKY130" column blank (PDK-05); the layer,
its rules and the public step list all include it, so we treat the
blank as a documentation inconsistency (see *Open questions*).

## Step category

`PWDEM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *thick-resist implant-block* type, aligned to the STI
pattern and used only by the high-voltage device family. Its features
are large — the 20 V devices have drawn channel lengths of the order
of a micrometre (PDK-HV gives 1.055 µm and 1.050 µm for the 16 V VHV
NMOS and PMOS) and drift regions longer still (PDK-07).

## Why this step exists

SKY130 is a multi-voltage process: a 1.8 V core, 5 V I/O, and "HV
extended-drain NMOS and PMOS" (PDK-10) rated in the PDK at 10/16 V
(`nfet_g5v0d16v0`, `pfet_g5v0d16v0`) and 20 V (`nfet_20v0`,
`pfet_20v0`, `nfet_20v0_iso`, `nfet_20v0_nvt`, `nfet_20v0_zvt`)
(PDK-07); SkyWater's platform table lists "20+V, Drain-Extended CMOS
(16V)" for S130 (SKW-02). A drain-extended (DE) MOSFET keeps the thin
gate oxide and short channel of a 5 V transistor but inserts a
lightly doped *drift* region between channel and drain: "Drain
extended transistors differ from regular self aligned polysilicon gate
transistors in that they use a very lightly doped extension region
adjacent to the drain that depletes at high drain voltages"
(PAT-DEMOS-TI). The PDK says the same for its own devices: "The VHV
devices need to be designed with drain extentions (DE) fabricated by
lightly doped Nwells and Pwells respectively" and "All VHV devices
use 110A gate oxide thickness just like standard 5.0V Vcc devices"
(PDK-HV).

For the 16 V devices the ordinary wells serve as the drift regions
(PDK-HV; PAT-DEMOS-TI2 notes that DE devices can be made "without
adding new masks or processing steps"). For the 20 V devices the
standard P-well is too heavily doped: a drift region must deplete
fully at the rated voltage, which requires a doping and depth that a
4 × 10¹⁷ cm⁻³ well (PDK-03) cannot provide. `PWDEM` therefore defines
where a lighter, custom P-well goes — the drift region of the 20 V
PMOS and, we infer, the body of the 20 V NMOS whose standard P-well
was blocked. This is what makes the 20 V devices "similar
construction to the 11V/16V NMOS FET, with several differences:
Longer drift region, Longer poly gate, Larger W/L, Devices placed in
pairs" (PDK-07).

## How it is typically performed

An industry-generic drain-extension well lithography for a 200 mm,
130 nm-era fab:

1. **Track preparation.** HMDS prime; no BARC for micrometre-scale
   features (inference; WIKI-LITHO).
2. **Thick resist coat.** The resist must stop the deepest
   drain-extension implant. A DE well is *lighter* than the main well
   but not necessarily shallower — a deep, graded drift region gives
   the best breakdown — so a 2 µm-class implant resist like that of
   {ref}`PWBM <step-026>` is plausible (inference; TXT-02;
   PAT-WELL-IBM's 1800–2500 nm for 550 keV boron).
3. **Exposure.** i-line; the layer's features are micrometre-scale
   (PDK-HV) and its overlay requirements are set by the drift-region
   length rather than by a sub-micrometre CD. We infer an **i-line
   layer**.
4. **Alignment** to STI. In a DE device the field-oxide length and
   the poly-to-drift overlap are reliability-critical — "Under no
   circumstances the poly/extended drain overlap and field oxide
   length should be changed" (PDK-HV) — so the well edge position
   relative to the STI, and later the poly, matters more than for an
   ordinary well.
5. **Develop, hard bake, inspect.**

## Machines typically used

* **i-line stepper**, 200 mm (ASML PAS 5500/100–/275, Nikon NSR-2205i,
  Canon FPA-3000i) (TXT-05).
* **Coat/develop track** with thick-resist capability; **overlay
  tool**.

## Machines likely used at SkyWater

* **ASML i-line stepper / scanner** (SKW-01). Strength: **strong** for
  existence; assignment is an **inference** from the coarse geometry.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ/Lithius** (SKW-01).
  Strength: strong for existence.
* **Overlay — KLA 5200/5300/Archer** (SKW-01). Strength: strong.

## Resources required

* **Thick positive i-line implant resist** (inference); suppliers
  named in SEC-01: Dow, JSR, Tokyo Ohka Kogyo.
* **HMDS**, **TMAH developer**, edge-bead remover, DI water, nitrogen.
* **The PWDEM reticle** (from `pwde`, PDK-06).

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

* **PDK-05** — SkyWater PDK Authors, *Masks* / `masks.csv` ("P-Well
  Drain Extended, PWDEM").
  <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
  <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
* **PDK-06** — SkyWater PDK Authors, `gds_layers.csv` (`pwde` 124:20;
  `pwbm` 19:44; `uhvi` 74:22).
  <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
* **PDK-PERIPH** — SkyWater PDK Authors, *Periphery rules*
  (pwdem.1–pwdem.6).
  <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
* **PDK-07** — SkyWater PDK Authors, *Device Details* (20 V NMOS/PMOS,
  isolated, native and zero-Vt 20 V NMOS; 10/16 V devices).
  <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
* **PDK-HV** — SkyWater PDK Authors, *High Voltage / Very High Voltage
  Methodology* (DE by lightly doped wells; 110 Å oxide; channel
  lengths; poly/drift overlap rule).
  <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
* **PDK-10** — google/skywater-pdk README ("HV extended-drain NMOS and
  PMOS").
  <https://github.com/google/skywater-pdk>
* **PDK-03** — SkyWater PDK Authors, *Criteria & Assumptions* (P-well
  peak concentration).
  <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30.
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **SKW-02** — SkyWater Technology, *Mixed-Signal CMOS & ROIC* ("20+V,
  Drain-Extended CMOS (16V)").
  <https://www.skywatertechnology.com/cmos/>
* **SEC-01** — SkyWater Technology, Inc., Form S-1, 2021-03-22.
  <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>

### High-level understanding

* **WIKI-LDMOS** — Wikipedia, *LDMOS* (drift region formed by
  implantation).
  <https://en.wikipedia.org/wiki/LDMOS>
* **WIKI-LITHO** — Wikipedia, *Photolithography*.
  <https://en.wikipedia.org/wiki/Photolithography>
* **TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the
  VLSI Era, Vol. 1*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4.
  <https://openlibrary.org/isbn/9780961672164>
* **TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4*,
  Lattice Press, 2002, ISBN 978-0-9616721-7-1.
  <https://openlibrary.org/isbn/9780961672171>

### Deep dive

* **PAT-DEMOS-TI** — J. C. Mitros (Texas Instruments), US 6,660,603 B2,
  granted 2003-12-09.
  <https://patents.google.com/patent/US6660603B2/en>
* **PAT-DEMOS-TI2** — P. R. Chidambaram (Texas Instruments),
  US 2006/0006461 A1, *Drain extended MOS transistors and methods for
  making the same*, published 2006-01-12.
  <https://patents.google.com/patent/US20060006461A1/en>
* **MITROS-2001** — J. C. Mitros et al., "High-voltage drain extended
  MOS transistors for 0.18-µm logic CMOS process", *IEEE Transactions
  on Electron Devices*, vol. 48, pp. 1751–1755, 2001,
  DOI 10.1109/16.936703.
* **MAI-2011** — A. Mai and H. Rücker, "Drain-extended MOS transistors
  capable for operation at 10 V and at radio frequencies",
  *Solid-State Electronics*, pp. 45–50, 2011,
  DOI 10.1016/j.sse.2011.06.034 (DE devices in a 0.13 µm technology).
* **PAT-WELL-IBM** — US 6,667,205 B2 (IBM), granted 2003-12-23 (resist
  thickness for keV-hundreds boron).
  <https://patents.google.com/patent/US6667205B2/en>

## Open questions

* Whether `pwde` defines the body of the 20 V NMOS, the drift region
  of the 20 V PMOS, or both, is inferred from the rule geometry; the
  PDK's 20 V cross-section drawings are not labelled in text form.
* The blank "Used in SKY130" entry for PWDEM in the PDK mask table
  conflicts with the step list; which is authoritative is not
  resolvable publicly.
* Resist thickness and exposure tool are inferred.
