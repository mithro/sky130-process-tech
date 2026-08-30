(step-026)=
# Step 026 — PWBM: P-well block mask

| | |
|---|---|
| **Step number** | 26 of 171 |
| **Step code** | `PWBM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`PCHIS <step-025>` |
| **Next step** | {ref}`PWI <step-027>` |

## What this step is

`PWBM` prints the *P-well block mask*: a thick photoresist is coated,
exposed through the PWBM reticle and developed so that resist
*remains* over every region that must not receive the P-well and is
removed everywhere else. The two P-well implants
{ref}`PWI <step-027>` and {ref}`PWI2 <step-028>` follow through the
openings, and the resist is stripped at {ref}`PWIS <step-029>`. The
name says how the layer is used: this is a *block* mask, the negative
of the {ref}`NWM <step-017>` N-well mask in spirit, and the P-well is
implanted into all silicon that it does not cover.

Three pieces of public evidence support that reading. First, the PDK
has no drawn P-well layer: `gds_layers.csv` contains `nwell` as a
drawing layer (64:20) but `pwell` only as label, pin and resistor
purposes (64:59, 122:16, 64:13 …), so a layout defines P-well
implicitly as "not N-well" (PDK-06). Second, the drawn layer that
does exist is `pwbm` (GDS 19:44), described as "Regions (in UHVI)
blocked from p-well implant (DE MOS devices only)" (PDK-06); its rule
table is headed "Function: Define p-well block" (PDK-PERIPH). Third,
the device that uses it is described the same way: the 20 V zero-Vt
NMOS "has p-well and all Vt implants blocked to achieve a zero VT"
(PDK-07). We therefore infer that the physical reticle is generated
from `nwell` ∪ `pwbm` (plus any deep-N-well-related additions), so
that the P-well goes everywhere except into N-wells and into the
special 20 V regions.

The PDK's mask table lists "P-Well Block Mask, PWBM" but — unlike
`NWM`, `LVTNM` and `HVTPM` — does *not* tick it as "Used in SKY130"
(PDK-05). The public step list nevertheless contains the step, and the
`pwbm` layer and its rules exist, so we treat the unticked box as a
documentation inconsistency rather than as evidence that the mask is
absent (see *Open questions*).

The `pwbm` rules (pwbm.1–pwbm.5) have no public numeric values ("N/A")
but describe the geometry: `pwbm` regions live inside the 20 V
identifier `uhvi`; "dnwell inside UHVI must be enclosed by pwbm
(exempt pwbm hole inside dnwell)" (pwbm.4); and the drain-extended
implant layer `pwde` must be enclosed by `pwbm` (pwdem.3)
(PDK-PERIPH). In words: inside a 20 V device the standard P-well is
kept out of the deep-N-well tub, and a custom, lighter P-well is put
back by {ref}`PWDEM <step-030>`/{ref}`PWDEI1 <step-031>` where the
device needs it.

## Step category

`PWBM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *thick-resist implant-block* kind. The resist must stop
boron of several hundred keV; the pattern is the coarsest in the
front end after the deep N-well; and the layer is aligned to the STI
pattern, as is `NWM`, so that the two well edges meet in the isolation
between NMOS and PMOS.

## Why this step exists

CMOS needs a P-type body for its NMOS: "The N device is manufactured
on a p-type substrate" (WIKI-CMOS), but a 130 nm process cannot use
the lightly doped substrate (8 × 10¹⁴ cm⁻³ background, PDK-03) as it
comes — it needs a *retrograde P-well* with a peak of 4 × 10¹⁷ cm⁻³ at
0.42 µm depth (PDK-03) for punch-through, isolation and latch-up
control (see {ref}`PWI <step-027>`). That implant must be kept out
of the N-wells, where it would compensate the PMOS body, and out of
the regions where the PDK's 20 V devices want either no well
(`nfet_20v0_zvt`) or a lighter, purpose-built one (the
drain-extended devices, PDK-07; PDK-HV). A block mask does both with
one lithography.

The alternative — a self-aligned twin well in which an oxide grown on
the N-well blocks the P-well implant without a second mask — was used
in older generations (PAT-TWIN-HARRIS) but costs a thermal step and
cannot make the custom 20 V regions. A drawn P-well mask would be
equivalent to `PWBM` in effect; SKY130 simply chose to draw the
exceptions rather than the wells.

## How it is typically performed

An industry-generic P-well-block lithography for a 200 mm, 130 nm-era
fab:

1. **Track preparation.** HMDS prime; no BARC for a coarse layer
   (inference; WIKI-LITHO).
2. **Thick resist coat.** The resist must stop the deepest P-well
   boron. IBM's retrograde p-well used boron at 550 keV behind a
   resist "between 1800–2500 nm" (PAT-WELL-IBM); Hook's IBM study
   modelled a "2.3 µm-thick pwell mask" against 600 keV boron
   (HOOK-2003); Zilog's 600–800 keV p-well needed at least 3.4 µm
   (PAT-RESIST-ZILOG). For a P-well whose peak is at 0.42 µm and whose
   vertical extent is 0.75 µm (PDK-03), boron energies are lower than
   those examples and a resist of roughly 2 µm is plausible
   (inference; TXT-02).
3. **Exposure.** i-line: the `pwbm` rules carry no minimum width, but
   the reticle's tightest features are the N-well outlines
   (0.840 µm width, 1.270 µm space, PDK-PERIPH), for which i-line has
   ample margin (k₁ ≈ 1.4 at NA 0.6, WIKI-LITHO). We infer an
   **i-line layer**.
4. **Alignment** to STI. The N-well/P-well junction is budgeted at
   0.034 µm from the drawn edge (PDK-03), so `PWBM` and `NWM` must
   both register to the same STI marks; their mutual overlay is what
   sets the well-to-well junction position and hence the n⁺/p⁺
   spacing rules (RUBIN-2002).
5. **Develop, hard bake, inspect.** TMAH develop; resist hardening
   for the MeV-class implant; overlay to STI.

**Well proximity effect.** As with the N-well, ions scattered from the
resist edge shift the threshold of transistors within about a
micrometre of the well boundary (HOOK-2003; SHEU-2006); for P-well
edges the shift raises NMOS Vt (HOOK-2003).

## Machines typically used

* **i-line stepper**, 200 mm (ASML PAS 5500/100–/275, Nikon NSR-2205i,
  Canon FPA-3000i) (TXT-05).
* **Coat/develop track** with thick-resist capability.
* **Overlay metrology**.

## Machines likely used at SkyWater

* **ASML i-line stepper / scanner** (SKW-01). Strength: **strong** for
  existence; assignment to `PWBM` is an **inference** from the coarse
  rules and thick resist.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ/Lithius** (SKW-01).
  Strength: strong for existence.
* **Overlay — KLA 5200/5300/Archer** (SKW-01). Strength: strong.

## Resources required

* **Thick positive i-line implant resist** (~2 µm class, inference);
  suppliers named in SEC-01: Dow, JSR, Tokyo Ohka Kogyo.
* **HMDS**, **TMAH developer**, edge-bead remover, DI water, nitrogen.
* **The PWBM reticle**, generated from `nwell` and `pwbm` (inference;
  PDK-06).

## Related steps and cross-references

* Previous: {ref}`PCHIS <step-025>`.
* Next: {ref}`PWI <step-027>` and {ref}`PWI2 <step-028>` through this
  resist; strip at {ref}`PWIS <step-029>`.
* Complementary mask: {ref}`NWM <step-017>`. The regions blocked here
  and re-doped later: {ref}`PWDEM <step-030>`.
* The isolated P-well inside the deep N-well tub
  ({ref}`DNM <step-007>`) is formed by this same implant, ringed by
  N-well.
* Previous mask: {ref}`HVTPM <step-022>`; next mask:
  {ref}`PWDEM <step-030>`.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

## References

### Cross-check

* **PDK-05** — SkyWater PDK Authors, *Masks* / `masks.csv` ("P-Well
  Block Mask, PWBM" — "Used in SKY130" column blank).
  <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
  <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
* **PDK-06** — SkyWater PDK Authors, `gds_layers.csv` (`pwbm` 19:44;
  `nwell` 64:20; `pwell` label/pin/resistor purposes only).
  <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
* **PDK-PERIPH** — SkyWater PDK Authors, *Periphery rules* (pwbm.1–5
  "Define p-well block"; pwdem.3; nwell.1, nwell.2a).
  <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
* **PDK-07** — SkyWater PDK Authors, *Device Details*
  (`nfet_20v0_zvt`: "p-well and all Vt implants blocked").
  <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
* **PDK-03** — SkyWater PDK Authors, *Criteria & Assumptions* (P-well
  peak concentration and coordinate, vertical dimension, junction
  offset).
  <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
* **PDK-HV** — SkyWater PDK Authors, *High Voltage Methodology*.
  <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30.
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **SEC-01** — SkyWater Technology, Inc., Form S-1, 2021-03-22.
  <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>

### High-level understanding

* **WIKI-CMOS** — Wikipedia, *CMOS*. <https://en.wikipedia.org/wiki/CMOS>
* **WIKI-LITHO** — Wikipedia, *Photolithography*.
  <https://en.wikipedia.org/wiki/Photolithography>
* **TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the
  VLSI Era, Vol. 1*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4.
  <https://openlibrary.org/isbn/9780961672164>
* **TXT-03** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 2:
  Process Integration*, Lattice Press, 1990, ISBN 978-0-9616721-4-0
  (twin-well CMOS, well masking options).
  <https://openlibrary.org/isbn/9780961672140>
* **TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4*,
  Lattice Press, 2002, ISBN 978-0-9616721-7-1.
  <https://openlibrary.org/isbn/9780961672171>

### Deep dive

* **PAT-WELL-IBM** — US 6,667,205 B2 (IBM), granted 2003-12-23.
  <https://patents.google.com/patent/US6667205B2/en>
* **PAT-RESIST-ZILOG** — US 6,576,405 B1 (Zilog), granted 2003-06-10.
  <https://patents.google.com/patent/US6576405B1/en>
* **PAT-TWIN-HARRIS** — US 5,247,199 A (Harris), 1993-09-21.
  <https://patents.google.com/patent/US5247199A/en>
* **HOOK-2003** — T. B. Hook et al., *IEEE Trans. Electron Devices*,
  vol. 50, no. 9, pp. 1946–1951, 2003, DOI 10.1109/TED.2003.815371.
  <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
* **SHEU-2006** — Y.-M. Sheu et al., *IEEE Trans. Electron Devices*,
  vol. 53, no. 11, pp. 2792–2798, 2006, DOI 10.1109/TED.2006.884070.
* **RUBIN-2002** — L. Rubin, W. Morris and J. Jasper, *IIT 2002*,
  pp. 17–20, DOI 10.1109/IIT.2002.1257927.

## Open questions

* The PDK mask table leaves the "Used in SKY130" column blank for
  PWBM (and for PWDEM) while the step list and the layer rules include
  it; which of the two is authoritative is not resolvable publicly.
* That the reticle is derived from `nwell` ∪ `pwbm` is our inference
  from the absence of a drawn P-well layer; the actual Boolean
  generation rules are not public.
* Resist thickness and exposure tool are inferred.
