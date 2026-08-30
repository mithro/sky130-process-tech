(step-014)=
# Step 014 — LVTNM: Low Vt NMOS mask

| | |
|---|---|
| **Step number** | 14 of 171 |
| **Step code** | `LVTNM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`NS19 <step-013>` |
| **Next step** | {ref}`LVTNI <step-015>` |

## What this step is

`LVTNM` is the third mask of the flow and the first of the well and
channel-implant module. The wafer arriving from
{ref}`NS19 <step-013>` is planar: oxide-filled isolation trenches
stand slightly proud of active islands that are covered only by the
thin pad oxide grown at {ref}`BOX <step-002>`. `LVTNM` coats this
surface with photoresist, exposes it through the *low-Vt N-channel
mask* reticle and develops it, leaving resist windows through which the
{ref}`LVTNI <step-015>` implant is placed. The resist is removed at
{ref}`LVTNIS <step-016>`.

The PDK's mask table lists "Low Vt Nch*, LVTNM" as a mask used in
SKY130 (PDK-05). The drawn layer is `lvtn` (GDS 125:44, "Low-Vt NMOS
device") and the generated mask layer is `clvtnm` (GDS 25:0, "Low Vt
Nch mask"), which also carries "mask add" (25:43) and "mask drop"
(25:42) purposes (PDK-06). The existence of add/drop purposes shows
that the reticle is *derived* from the drawn layer by Boolean
operations in the mask-generation flow rather than being a copy of it.

The periphery design rules state the layer's function directly: `lvtn`
rules "Define regions to block Vt adjust implant for low Vt LV
PMOS/NMOS, SONOS FETs and Native NMOS" (PDK-PERIPH). The rule values
are coarse for a 130 nm process: minimum width 0.380 µm (lvtn.1a),
minimum space 0.380 µm (lvtn.2), minimum enclosure of a gate by `lvtn`
0.180 µm (lvtn.4b), minimum spacing to a gate 0.180 µm (lvtn.3a),
spacing to a PMOS along the source/drain direction 0.235 µm (lvtn.3b),
no overlap with `hvtp` with 0.380 µm spacing (lvtn.9), enclosure by
`nwell` 0.380 µm when the layer is used inside an N-well (lvtn.10), and
minimum area 0.265 µm² (lvtn.13) (PDK-PERIPH). A separate poly rule
sets the minimum channel length of a PMOS overlapping `lvtn` at
0.350 µm (poly.1b) — much longer than the 0.150 µm baseline — which is
consistent with a device whose channel doping has been reduced and
which therefore needs more length to control short-channel effects
(PDK-PERIPH).

## Step category

`LVTNM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *implant-block* type: the image quality that matters is
placement relative to the active pattern and adequate resist
thickness, not minimum feature size. It aligns to the STI/active
pattern printed at {ref}`FOM <step-004>` and etched at
{ref}`STIE <step-006>`, which at this point is the only pattern on the
wafer.

## Why this step exists

SKY130 is a multi-threshold process. The device list offers, at 1.8 V,
a standard NMOS (`nfet_01v8`), a low-Vt NMOS (`nfet_01v8_lvt`), a
standard PMOS, a low-Vt PMOS (`pfet_01v8_lvt`) and a high-Vt PMOS
(`pfet_01v8_hvt`), together with native NMOS devices
(`nfet_03v3_nvt`, `nfet_05v0_nvt`) that are "constructed by blocking
out all VT implants" (PDK-07). The reason for offering several
thresholds is the familiar speed/leakage trade: "Low Vth devices
switch faster, and are therefore useful on critical delay paths to
minimize clock periods. The penalty is that low Vth devices have
substantially higher static leakage power", and the threshold "is
adjusted by altering the concentration of dopant atoms in the channel
region beneath the gate oxide" (WIKI-MTCMOS). The 2001 ITRS states
that "multiple threshold-voltage and multiple-oxide-thickness devices
also need to be available in order to enable more comprehensive
circuit/system-level power/performance optimization" (ITRS-04).

`LVTNM` is the mask that distinguishes the low-threshold (and, per the
rule text, the native and SONOS) channels from the standard ones. The
PDK's `lvtn` rule heading says the layer *blocks* a Vt-adjust implant.
That wording, and the fact that the same layer serves low-Vt NMOS,
low-Vt PMOS and native NMOS — devices whose thresholds could not all be
lowered by a single dopant species implanted *into* them — lead us to
infer that the physical reticle is generated so that resist *covers*
the drawn `lvtn` regions while the {ref}`LVTNI <step-015>` implant goes
into the rest of the wafer, or that Boolean combinations with `nwell`
and other layers produce separate NMOS and PMOS variants of the
opening. Which reading is right is not public; see *Open questions*.

Without this mask every 1.8 V NMOS would have the same threshold, and
the low-Vt, native and SONOS device options in the PDK would not exist.

## How it is typically performed

An industry-generic implant-block lithography sequence for a 200 mm,
130 nm-era fab:

1. **Surface preparation.** Dehydration bake and vapour HMDS prime on
   the track; the surface is oxide everywhere (pad oxide on active,
   trench oxide on field), which primes well.
2. **Resist coat.** A single-layer positive resist. The
   {ref}`LVTNI <step-015>` implant is a channel-type implant at tens
   of keV, which a resist of about 1 µm stops with a wide margin
   (industry-typical; TXT-02, ch. 9). The PDK's own assumptions table
   gives a nominal "Photoresist thickness" of 1.14 µm (PDK-03), so we
   take that as the plausible order of thickness. No anti-reflective
   coating is needed for a layer whose features are more than twice
   the wavelength (inference from the 0.380 µm rules; WIKI-LITHO).
3. **Exposure.** The 0.380 µm minimum width and space (PDK-PERIPH) are
   comfortably within reach of an i-line (365 nm) stepper: at NA 0.6
   the process factor is k₁ = 0.38 × 0.6 / 0.365 ≈ 0.62, well above
   the "0.4 for production" level (WIKI-LITHO). ITRS 2001 reserves
   248 nm for the critical layers of the 130 nm node (ITRS-03). We
   therefore infer that `LVTNM` is an **i-line layer**, like the other
   implant-block masks of this module and unlike
   {ref}`FOM <step-004>`.
4. **Alignment.** To the STI pattern. The tightest coupling of this
   layer is to the *future* gate: the 0.180 µm enclosure of gate by
   `lvtn` (lvtn.4b) means both this mask and the later poly mask must
   register to the same active reference within a fraction of that
   value.
5. **Develop** in aqueous TMAH (TXT-02), rinse, dry; a hard bake or UV
   cure may follow to stabilise the resist against the implant
   (industry practice, TXT-02).
6. **Inspection.** Overlay measured on box-in-box targets against the
   STI layer; CD checked loosely; after-develop inspection for defects.

## Machines typically used

* **i-line stepper**, 200 mm: ASML PAS 5500/100–/275 series, Nikon
  NSR-2205i, Canon FPA-3000i (TXT-05; see the category page).
* **Coat/develop track** linked to the stepper (TEL, DNS/SCREEN,
  SVG/ASML, Sokudo).
* **Overlay metrology** (KLA-Tencor 5xxx/Archer class) and a CD-SEM for
  periodic checks.

## Machines likely used at SkyWater

* **ASML i-line stepper / i-line scanner.** SKW-01 lists "ASML I-line
  stepper" and "ASML I-line scanner". Strength: **strong** for the
  existence of the tools; the assignment of `LVTNM` to the i-line
  tools is an **inference** from the 0.380 µm design rules, not a
  SkyWater statement.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ/Lithius** (SKW-01).
  Strength: strong for existence; which track serves which exposure
  tool is not public.
* **Overlay — KLA 5200/5300/Archer; CD — AMAT Verity/VeraSEM**
  (SKW-01). Strength: strong.

## Resources required

* **Positive i-line (DNQ/novolak) photoresist**, about 1 µm thick;
  SkyWater's S-1 names The Dow Chemical Company, JSR Corporation and
  Tokyo Ohka Kogyo America as photoresist suppliers (SEC-01).
* **HMDS** adhesion promoter; **TMAH developer** (0.26 N is the
  industry standard, TXT-02); edge-bead remover and rinse solvents;
  DI water and nitrogen.
* **The LVTNM reticle** — a chrome-on-quartz plate generated from the
  `clvtnm` layer with its add/drop corrections (PDK-06).

## Related steps and cross-references

* Previous: {ref}`NS19 <step-013>` (nitride strip; leaves the pad
  oxide that this module's implants pass through).
* Next: {ref}`LVTNI <step-015>` (the implant through this mask), then
  {ref}`LVTNIS <step-016>` (resist strip).
* The other Vt-flavour mask of the module is {ref}`HVTPM <step-022>`
  (`hvtp`, which must not overlap `lvtn`, rule lvtn.9).
* The baseline N-channel implant of the 1.8 V devices is
  {ref}`NCHI <step-045>`, placed later under the low-voltage oxide
  mask {ref}`LVOM <step-044>`; all of this module's implants are
  activated at {ref}`RTAI <step-034>`.
* Previous mask: {ref}`DNM <step-007>`; next mask:
  {ref}`NWM <step-017>`.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

## References

### Cross-check

* **PDK-05** — SkyWater PDK Authors, *Masks* page and `masks.csv`
  ("Low Vt Nch*, LVTNM, X").
  <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
  <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
* **PDK-06** — SkyWater PDK Authors, *Layers Reference* and
  `gds_layers.csv` (`lvtn` 125:44; `clvtnm` 25:0, 25:43, 25:42).
  <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
  <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
* **PDK-PERIPH** — SkyWater PDK Authors, *Periphery rules* (`lvtn`
  function text; lvtn.1a, lvtn.2, lvtn.3a, lvtn.3b, lvtn.4b, lvtn.9,
  lvtn.10, lvtn.13; poly.1b).
  <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
* **PDK-07** — SkyWater PDK Authors, *Device Details* (`nfet_01v8_lvt`,
  `pfet_01v8_lvt`, `pfet_01v8_hvt`, native NMOS "constructed by
  blocking out all VT implants").
  <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
* **PDK-03** — SkyWater PDK Authors, *Criteria & Assumptions*
  ("Photoresist thickness" 1.14 µm).
  <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 (ASML i-line stepper and scanner; tracks;
  overlay and CD tools).
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **SEC-01** — SkyWater Technology, Inc., Form S-1, 2021-03-22
  (photoresist suppliers).
  <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>

### High-level understanding

* **WIKI-MTCMOS** — Wikipedia, *Multi-threshold CMOS*.
  <https://en.wikipedia.org/wiki/Multi-threshold_CMOS>
* **WIKI-LITHO** — Wikipedia, *Photolithography* (365 nm i-line,
  CD = k₁·λ/NA).
  <https://en.wikipedia.org/wiki/Photolithography>
* **TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the
  VLSI Era, Vol. 1*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4 (lithography and implant-masking chapters).
  <https://openlibrary.org/isbn/9780961672164>
* **TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4*,
  Lattice Press, 2002, ISBN 978-0-9616721-7-1 (lithography tools of
  the 0.25–0.13 µm generations).
  <https://openlibrary.org/isbn/9780961672171>

### Deep dive

* **ITRS-03** — ITRS 2001, *Lithography* (exposure wavelength by
  node).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
* **ITRS-04** — ITRS 2001, *Process Integration, Devices, and
  Structures* ("multiple threshold-voltage and multiple-oxide-thickness
  devices").
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>
* **PAT-VT-RRR** — M. Helm and X. Zhou, US 2011/0006372 A1, *Formation
  of standard voltage threshold and low voltage threshold MOSFET
  devices* (Round Rock Research; priority 2002-07-08), published
  2011-01-13 — an example of low-Vt NMOS and PMOS defined by masked
  Vt-adjust implants.
  <https://patents.google.com/patent/US20110006372A1/en>

## Open questions

* **Reticle polarity.** The PDK says `lvtn` *blocks* a Vt-adjust
  implant, yet the step list pairs the mask with an implant
  ({ref}`LVTNI <step-015>`). Whether the reticle opens *over* `lvtn`
  (and `LVTNI` is a counter-doping implant) or *everywhere except*
  `lvtn` (and `LVTNI` is the baseline Vt-adjust implant that low-Vt
  devices skip) cannot be settled from public data; the "mask
  add/drop" purposes show only that the reticle is generated, not how.
* Whether separate NMOS and PMOS reticles are derived from the one
  drawn layer, or whether `nfet_01v8_lvt` and `pfet_01v8_lvt` share a
  single physical mask, is not public.
* Resist thickness, exposure tool and the use of a resist-hardening
  step are inferred from the design rules and general practice.
