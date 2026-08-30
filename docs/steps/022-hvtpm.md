(step-022)=
# Step 022 — HVTPM: High V P-channel implant mask

| | |
|---|---|
| **Step number** | 22 of 171 |
| **Step code** | `HVTPM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`LVTPIS <step-021>` |
| **Next step** | {ref}`PCHI <step-023>` |

## What this step is

`HVTPM` prints the *high-Vt P-channel mask*: photoresist is coated on
the cleaned wafer, exposed through the HVTPM reticle and developed,
opening windows over the PMOS channels that are to have a raised
threshold. Two implants follow through the same resist — the
P-channel implant {ref}`PCHI <step-023>` and the P-channel BF₂ implant
{ref}`PNCHI <step-024>` — and the resist is stripped at
{ref}`PCHIS <step-025>`.

A note on the name. The step list expands the code as "High V
P-channel implant mask", which could be read as *high-voltage*. The
PDK is unambiguous that the "V" is a threshold: the mask table lists
"High Vt PCh*, HVTPM" (PDK-05); the drawn layer `hvtp` (GDS 78:44) is
"High-Vt LVPMOS implant" and the generated mask `chvtpm` (GDS 97:0) is
"High Vt Pch mask", with mask add/drop purposes 97:43 and 97:42
(PDK-06); and the rule table's function line reads "Define Vt adjust
implant region for high Vt LV PMOS" (PDK-PERIPH). The device it
creates is `pfet_01v8_hvt`, the "1.8V high-VT PMOS FET", and the
high-Vt varactor option `cap_var_hvt` (PDK-07). The "LV" in the
layer's description makes the point twice: this is a low-voltage
(1.8 V) device with a high threshold, nothing to do with the 5 V or
20 V families.

The design rules are as coarse as those of `lvtn`: minimum width
0.380 µm (hvtp.1), minimum spacing 0.380 µm (hvtp.2), minimum
enclosure of a PMOS by `hvtp` 0.180 µm (hvtp.3), minimum spacing from
a PMOS not meant to be high-Vt 0.180 µm (hvtp.4), minimum area
0.265 µm² (hvtp.5, hvtp.6), and no overlap with `lvtn`, with 0.380 µm
spacing between the two (lvtn.9) (PDK-PERIPH). Unlike `lvtn`, whose
rule heading says it *blocks* an implant, `hvtp` is described as the
*region that receives* the implant, so the reticle polarity here is
straightforward: resist is removed over `hvtp`.

## Step category

`HVTPM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *implant-block* type: coarse features, a standard-thickness
resist (the implants behind it are keV channel implants), aligned to
the STI/active pattern.

## Why this step exists

SKY130 offers three 1.8 V PMOS thresholds — `pfet_01v8`,
`pfet_01v8_lvt`, `pfet_01v8_hvt` (PDK-07) — because a high-threshold
device is the tool for cutting standby leakage: "High Vth devices are
used on non-critical paths to reduce static leakage power without
incurring a delay penalty. Typical high Vth devices reduce static
leakage by 10 times compared with low Vth devices" (WIKI-MTCMOS). The
2001 ITRS treats "Multiple Vt" as a standard feature of the mixed-
signal and low-power roadmap (ITRS-04). In a flow where the baseline
PMOS threshold is set by {ref}`LVTPI <step-020>` through the N-well
mask, a *separate* mask is the only way to give some PMOS a different
channel dose; `HVTPM` is that mask. Without it the PDK's `_hvt` PMOS
and high-Vt varactor would not exist, and low-leakage standard-cell
libraries built on them could not be offered.

There is no NMOS equivalent in the step list: NMOS come in standard,
low-Vt and native flavours only (PDK-07), so the high-Vt option is
PMOS-only in SKY130.

## How it is typically performed

An industry-generic implant-block lithography for a 200 mm, 130 nm-era
fab:

1. **Track preparation.** HMDS prime on the oxide surface.
2. **Resist coat.** A conventional positive resist of roughly 1 µm
   (the PDK's nominal "Photoresist thickness" is 1.14 µm, PDK-03) is
   ample for keV channel implants (TXT-02). No BARC is needed for
   0.38 µm features at i-line (inference; WIKI-LITHO).
3. **Exposure.** i-line: k₁ ≈ 0.62 for 0.38 µm at NA 0.6 (WIKI-LITHO),
   well within production margins; the KrF tools are reserved for the
   critical layers (ITRS-03). We infer an **i-line layer**.
4. **Alignment** to STI. The 0.180 µm enclosure and spacing rules
   (hvtp.3, hvtp.4) define the overlay budget between this mask and
   the active pattern that determines which transistor is which.
5. **Develop** in TMAH; optional hard bake or UV cure before the
   implant (TXT-02).
6. **Metrology.** Overlay to STI; CD sampled; after-develop
   inspection.

## Machines typically used

* **i-line stepper**, 200 mm (ASML PAS 5500/100–/275, Nikon NSR-2205i,
  Canon FPA-3000i) (TXT-05).
* **Coat/develop track**; **overlay tool**; **CD-SEM** for sampling.

## Machines likely used at SkyWater

* **ASML i-line stepper / scanner** (SKW-01). Strength: **strong** for
  existence; assignment to `HVTPM` is an **inference** from the
  0.38 µm rules.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ/Lithius** (SKW-01).
  Strength: strong for existence.
* **Overlay — KLA 5200/5300/Archer; CD — AMAT Verity/VeraSEM**
  (SKW-01). Strength: strong.

## Resources required

* **Positive i-line photoresist** (~1 µm); suppliers named in SEC-01:
  Dow, JSR, Tokyo Ohka Kogyo.
* **HMDS**, **TMAH developer**, edge-bead remover, DI water, nitrogen.
* **The HVTPM reticle** (generated from `chvtpm`, PDK-06).

## Related steps and cross-references

* Previous: {ref}`LVTPIS <step-021>`.
* Next: {ref}`PCHI <step-023>` and {ref}`PNCHI <step-024>` through
  this resist; strip at {ref}`PCHIS <step-025>`.
* The baseline PMOS channel implant is {ref}`LVTPI <step-020>`; the
  low-Vt option is defined by {ref}`LVTNM <step-014>` (`lvtn`, which
  may not overlap `hvtp`).
* Previous mask: {ref}`NWM <step-017>`; next mask:
  {ref}`PWBM <step-026>`.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

## References

### Cross-check

* **PDK-05** — SkyWater PDK Authors, *Masks* / `masks.csv` ("High Vt
  PCh*, HVTPM, X").
  <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
  <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
* **PDK-06** — SkyWater PDK Authors, `gds_layers.csv` (`hvtp` 78:44
  "High-Vt LVPMOS implant"; `chvtpm` 97:0, 97:43, 97:42).
  <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
* **PDK-PERIPH** — SkyWater PDK Authors, *Periphery rules* (`hvtp`
  function text; hvtp.1–hvtp.6; lvtn.9).
  <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
* **PDK-07** — SkyWater PDK Authors, *Device Details*
  (`pfet_01v8_hvt`; `cap_var_hvt`).
  <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
* **PDK-03** — SkyWater PDK Authors, *Criteria & Assumptions*
  (photoresist thickness).
  <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30.
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **SEC-01** — SkyWater Technology, Inc., Form S-1, 2021-03-22.
  <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>

### High-level understanding

* **WIKI-MTCMOS** — Wikipedia, *Multi-threshold CMOS*.
  <https://en.wikipedia.org/wiki/Multi-threshold_CMOS>
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

* **ITRS-03** — ITRS 2001, *Lithography*.
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
* **ITRS-04** — ITRS 2001, *Process Integration, Devices, and
  Structures* ("Multiple Vt").
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>
* **WEI-1998** — L. Wei, Z. Chen, M. Johnson, K. Roy and V. De, "Design
  and optimization of low voltage high performance dual threshold
  CMOS circuits", *Proceedings of the 35th Design Automation
  Conference*, pp. 489–494, 1998, DOI 10.1109/DAC.1998.724521 — the
  circuit-level case for a second PMOS/NMOS threshold.

## Open questions

* The PDK mask table also flags "HLow VT PCh Radio*, HVTRM" as used in
  SKY130 (PDK-05), with a drawn layer `hvtr` (GDS 18:20, "High-Vt RF
  transistor implant", PDK-06), yet the public step list has no
  HVTRM step. Whether that mask is absent, folded into `HVTPM`, or
  belongs to an option not in the baseline flow is unknown.
* Resist thickness and exposure tool are inferred.
