(step-044)=
# Step 044 — LVOM: Low voltage oxide mask

| | |
|---|---|
| **Step number** | 44 of 171 |
| **Step code** | `LVOM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | FEOL — SONOS and gate dielectrics |
| **Previous step** | {ref}`GOX100 <step-043>` |
| **Next step** | {ref}`NCHI <step-045>` |

## What this step is

`LVOM` is the mask of the dual-gate-oxide process. After the first,
thick gate oxide has been grown over every active area at
{ref}`GOX100 <step-043>`, this lithography step opens resist windows
over the *low-voltage* (1.8 V) transistors and leaves resist over the
5 V and high-voltage ones. Through the windows the 1.8 V NMOS
channel implant is made ({ref}`NCHI <step-045>`) and the thick oxide is
then stripped ({ref}`GOXETCH <step-046>`), so that the thin 1.8 V gate
oxide can be grown on bare silicon at {ref}`LVGOX <step-047>` while
the covered regions keep their thick oxide.

The PDK lists "Low Voltage Oxide, LVOM" as used in SKY130,[^pdk-05]
with the generated mask layer `clvom` (GDS 46:0, "Low Voltage oxide
mask") and a drawing purpose at 45:20.[^pdk-06] Designers do not draw
`lvom`; they draw its complement, `hvi` (GDS 75:20, "High voltage
(5.0V) thick oxide gate regions"),[^pdk-06] whose rule set is headed
"Defines thick oxide for high voltage devices": minimum width
0.600 µm (hvi.1), minimum spacing 0.700 µm (hvi.2a, with "Manual merge
if space is below minimum", hvi.2b), "Hvi must not overlap tunm"
(hvi.4), and a minimum space of 0.700 µm "between hvi and nwell
(exclude coincident edges)" (hvi.5).[^pdk-periph] We infer that the
LVOM reticle is essentially NOT `hvi`: everything outside the drawn
thick-oxide regions is opened. The PDK's high-voltage methodology
confirms which devices sit inside `hvi`: "All high voltage devices use
110A gate oxide thickness just like low voltage (0 to Vcc)
devices"[^pdk-hv] — where "low voltage (0 to Vcc)" means the 5 V
`g5v0d10v5` family — and "All VHV devices use 110A gate oxide
thickness just like standard 5.0V Vcc devices".[^pdk-hv]

One subtlety follows from hvi.4. Because `hvi` must not overlap the
tunnel windows, the SONOS memory transistors are formally *outside*
the thick-oxide regions, yet their gate dielectric is the ONO island,
not the thin oxide. How the generated `clvom` mask treats the ONO
islands — whether it excludes them so that the resist protects the
blocking oxide during the etch and clean — is not public. The
Cypress integration patent shows that its equivalent resist does
exactly that: "while the photoresist layer 318 protects the ONO charge
trapping dielectric stack 306 a clean which would be detrimental to
the ONO charge trapping dielectric stack 306 if it were not protected
by the photoresist layer 318 may be performed at this time".[^pat-03]
We infer the same for SKY130 (see *Open questions*).

## Step category

`LVOM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *implant and wet-etch window* type — the same double duty
as {ref}`TUNM <step-035>`. Its minimum feature, the 0.600 µm `hvi`
width,[^pdk-periph] places it among the relaxed layers, and we infer
an i-line exposure. What is special about it is where its edges must
fall: the boundary between thick and thin oxide has to lie on field
oxide, never across an active area, because an oxide step inside a
channel would be a transistor with two thicknesses. The rule that
`hvi` keeps 0.700 µm from an N-well edge (hvi.5)[^pdk-periph] and the
PDK's photoresist thickness of 1.14 µm[^pdk-03] are the public
constraints; the enclosure of active by `hvi` that must exist inside
the generated mask is not published.

## Why this step exists

SKY130 runs a "1.8V core" with "5.0V I/O",[^pdk-10] plus 10–20 V
drain-extended devices that share the 5 V oxide.[^pdk-hv] A gate oxide
cannot serve both: ITRS 2001 puts the equivalent oxide thickness of
2001-era low-operating-power logic at 2.0–2.4 nm and of low-standby
logic at 2.4–2.8 nm,[^itrs-01] whereas an oxide that must sit under 5 V
(and, in the PDK's HV rules, survive "7.3 V @ 25C" gate stress without
failure[^pdk-hv]) needs roughly 11 nm — the PDK's 110 Å.[^pdk-hv] The
public SPICE models carry the two numbers: an electrical oxide
thickness (`toxe`) of 4.148 nm for `nfet_01v8`[^pdk-model-nfet01v8]
and 11.6 nm for `nfet_g5v0d10v5`.[^pdk-model-nfet5v]

A dual gate oxide is made by growing the thick oxide first, masking
the thick-oxide regions, stripping the oxide from the thin-oxide
regions and growing the thin oxide second ({ref}`category-oxidation`,
*Dual gate oxide processes*); the mask that does the masking is
`LVOM`. Multiple-thickness gate-oxide integration was worked out in
the late 1990s for logic-embedded DRAM,[^togo-1998] and the pairing of
the resist with the wet etch it must survive — the "'Resist / Wet
Etch' Couple for Dual Gate Oxide" — has its own literature.[^beverina-2003]
Cypress's flows describe the same mask: "a photoresist layer 318 …
patterned to have an opening 319 formed over a region of the substrate
302 that is to have the next insulator material and/or insulator
layer thickness",[^pat-03] and "a patterned mask layer 242 … includes
at least one opening 244 over a channel 218 in the second region
208".[^pat-04]

The window also serves the 1.8 V NMOS channel implant
({ref}`NCHI <step-045>`), which the earlier pages of this reference
identify as the baseline N-channel implant that all 1.8 V NMOS receive
(see {ref}`LVTNI <step-015>`). Without `LVOM` every transistor would
have the thick oxide: the 1.8 V core would be slow and its thresholds
wrong.

## How it is typically performed

An industry-generic sequence for a dual-gate-oxide mask in a 200 mm,
130 nm-era fab (SKY130's recipe is not public):

1. **Surface.** Fresh thermal oxide (~10 nm) over all active areas and
   trench oxide over the field; the ONO islands over the memory cells.
   Dehydration bake and {term}`HMDS` prime. Resist adhesion to a
   fresh, clean thermal oxide is good, which matters because the
   resist edge will be undercut by HF at {ref}`GOXETCH <step-046>`.
2. **Resist coat.** About 1 µm of positive i-line resist (PDK generic
   value 1.14 µm[^pdk-03]) — thick enough to stop the channel implant
   and to survive a wet etch. No ARC is indicated by the step list
   used in this reference.
3. **Exposure** through the LVOM reticle on an i-line stepper (our
   inference from the 0.6 µm rule; the 2001 ITRS reserves 248 nm for
   the critical layers[^itrs-03]), aligned to the STI pattern; the
   thick/thin boundary must land on field oxide, so overlay to active
   is the controlled quantity.
4. **Post-exposure bake, develop** in 2.38 % TMAH,[^txt-02] rinse.
5. **Hard bake.** A firm hard bake improves adhesion and reduces HF
   penetration along the resist–oxide interface at the etch, one of
   the resist/etch couple's known failure modes.[^beverina-2003]
6. **Inspection.** Overlay and CD; after-develop inspection for
   residue in the LV windows.

The resist then masks {ref}`NCHI <step-045>` and
{ref}`GOXETCH <step-046>` and is stripped after the etch (no separate
strip step is listed; see {ref}`GOXETCH <step-046>`).

## Machines typically used

* **i-line stepper**, 200 mm: ASML PAS 5500/100–/275, Nikon
  NSR-2205i, Canon FPA-3000i ({ref}`category-lithography`).
* **Coat/develop track** (TEL, DNS/SCREEN, Sokudo).
* **Overlay metrology** and **CD-SEM**.

## Machines likely used at SkyWater

* **ASML i-line stepper / scanner.**[^skw-01] Strength: **strong** for
  the tool class; **inference** for the assignment.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ/Lithius.**[^skw-01]
  Strength: strong for existence.
* **KLA 5200/5300/Archer overlay; AMAT Verity/VeraSEM CD.**[^skw-01]
  Strength: strong.

## Resources required

* **i-line photoresist** (Dow, JSR, TOK[^sec-01]), **HMDS**.
* **TMAH developer** (2.38 %),[^txt-02] edge-bead remover, DI water,
  nitrogen.
* **The LVOM reticle** — chrome on quartz, relaxed features.

## Related steps and cross-references

* Previous: {ref}`GOX100 <step-043>` (the thick oxide being masked).
* Next: {ref}`NCHI <step-045>` (implant through the window), then
  {ref}`GOXETCH <step-046>` (thick oxide stripped in the window) and
  {ref}`LVGOX <step-047>` (thin oxide grown).
* Devices inside `hvi`: the 5 V family and the 10–20 V drain-extended
  devices ({ref}`PWDEM <step-030>`).
* The memory cells' relationship to `hvi` (hvi.4): {ref}`TUNM <step-035>`.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`;
  dual-oxide background: {ref}`category-oxidation`.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "Low Voltage Oxide,
  LVOM, X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `hvi` 75:20,
  `clvom` 46:0 and 45:20.[^pdk-06]
* SkyWater PDK, *Periphery rules* — hvi.1, hvi.2a, hvi.2b, hvi.4,
  hvi.5.[^pdk-periph]
* SkyWater PDK, *High Voltage Methodology* — 110 Å gate oxide for
  HV and VHV devices; gate-stress limits.[^pdk-hv]
* SkyWater PDK, *Criteria & Assumptions* — photoresist
  thickness.[^pdk-03]
* SkyWater PDK, SPICE model files — `toxe` of `nfet_01v8` and
  `nfet_g5v0d10v5`.[^pdk-model-nfet01v8][^pdk-model-nfet5v]
* SkyWater PDK, repository README — "1.8V core", "5.0V I/O".[^pdk-10]
* SkyWater, *Facilities & Capabilities* — lithography tools.[^skw-01]
* SkyWater, Form S-1 (2021) — photoresist suppliers.[^sec-01]
* Koutny et al. (Cypress), US 8,093,128 — the resist opening over the
  next-oxide region and its protection of the ONO.[^pat-03]
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — the
  dual gate oxide mask 242.[^pat-04]

### High-level understanding

* Wikipedia, *Photolithography*.[^wiki-litho]
* Wikipedia, *Gate oxide* — what the thickness does.[^wiki-gate-oxide]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography.[^txt-02]

### Deep dive

* Togo, Noda and Tanigawa (NEC), IEDM 1998 — multiple-thickness gate
  oxide and dual-gate technologies for embedded DRAM.[^togo-1998]
* Beverina et al. (STMicroelectronics), *Solid State Phenomena* 2003 —
  the resist / wet-etch couple for dual gate oxide.[^beverina-2003]
* Lee (Hyundai), *Electrochem. Solid-State Lett.* 1999 — a dual gate
  oxide process with improved gate-oxide integrity.[^lee-1999]
* Lee et al., ICVC 1999 — gate oxide thinning at the STI edge in a
  dual gate oxide process.[^lee-1999-icvc]
* Kim et al., SSDM 2001 — an STI scheme that compensates thinning at
  the STI corner for thick dual gate oxides.[^kim-2001]
* Inukai and Hiramoto, *Jpn. J. Appl. Phys.* 2000 — dual oxide
  thickness / multiple threshold CMOS for stand-by leakage.[^inukai-2000]
* ITRS 2001, *Front End Processes* — EOT targets that force two
  oxides.[^itrs-01]
* ITRS 2001, *Lithography* — wavelength by layer criticality.[^itrs-03]
* Levinson, *Principles of Lithography* — overlay and resist
  processing for non-critical layers.[^levinson-2005]

## Open questions

* The derivation of the LVOM reticle from `hvi` (and whether it
  excludes the ONO islands) is not public; the NOT-`hvi` reading and
  the protection of the ONO are inferences, the latter from a Cypress
  patent.
* Whether the layer is exposed on i-line or DUV tools is inferred from
  the 0.6 µm rule.
* The enclosure of active regions by the generated mask, resist type
  and hard-bake conditions are not public.

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
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README. <https://github.com/google/skywater-pdk>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^pdk-model-nfet01v8]: SkyWater PDK Authors,
    `sky130_fd_pr__nfet_01v8__tt.pm3.spice` (typical-corner BSIM4
    model, parameter `toxe`), google/skywater-pdk-libs-sky130_fd_pr
    repository.
    <https://raw.githubusercontent.com/google/skywater-pdk-libs-sky130_fd_pr/main/cells/nfet_01v8/sky130_fd_pr__nfet_01v8__tt.pm3.spice>
[^pdk-model-nfet5v]: SkyWater PDK Authors,
    `sky130_fd_pr__nfet_g5v0d10v5__tt.pm3.spice` (typical-corner BSIM4
    model, parameter `toxe`), google/skywater-pdk-libs-sky130_fd_pr
    repository.
    <https://raw.githubusercontent.com/google/skywater-pdk-libs-sky130_fd_pr/main/cells/nfet_g5v0d10v5/sky130_fd_pr__nfet_g5v0d10v5__tt.pm3.spice>
[^togo-1998]: M. Togo, K. Noda and T. Tanigawa (NEC),
    "Multiple-thickness gate oxide and dual-gate technologies for
    high-performance logic-embedded DRAMs", *IEDM 1998 Technical
    Digest*, pp. 347–350. <https://doi.org/10.1109/IEDM.1998.746371>
[^beverina-2003]: A. Beverina, I. Guilmeau, J. P. Carrere, N. Emonet,
    F. Guyader, V. Huard, S. Petitdidier and R. Velard, "'Resist / Wet
    Etch' Couple for Dual Gate Oxide", *Solid State Phenomena* **92**,
    235–238 (2003). <https://doi.org/10.4028/www.scientific.net/SSP.92.235>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^wiki-gate-oxide]: Wikipedia, *Gate oxide*.
    <https://en.wikipedia.org/wiki/Gate_oxide>
[^lee-1999]: S.-W. Lee, "Novel Dual Gate Oxide Process with Improved
    Gate Oxide Integrity Reliability", *Electrochemical and Solid-State
    Letters* **3**(1), 56 (1999). <https://doi.org/10.1149/1.1390957>
[^lee-1999-icvc]: S.-W. Lee, I. H. Cho, S. H. Park, H. G. Choi,
    N. G. Kim, J.-K. Kim, S. B. Han and K. Lee, "Gate oxide thinning
    effects at the edge of shallow trench isolation in the dual gate
    oxide process", *ICVC '99: 6th International Conference on VLSI
    and CAD*, pp. 249–252. <https://doi.org/10.1109/ICVC.1999.820895>
[^kim-2001]: S.-H. Kim, S.-H. Kim, S.-E. Kim, M.-S. Kim, J.-H. Park and
    E.-S. Kim, "New STI Scheme to Compensate Gate Oxide Thinning at STI
    Corner Edge for the Devices Using Thick Dual Gate Oxide", *Extended
    Abstracts of the 2001 International Conference on Solid State
    Devices and Materials (SSDM)*, 2001.
    <https://doi.org/10.7567/SSDM.2001.A-6-6>
[^inukai-2000]: T. Inukai and T. Hiramoto, "Suppression of Stand-by
    Tunnel Current in Ultra-Thin Gate Oxide MOSFETs by Dual Oxide
    Thickness-Multiple Threshold Voltage CMOS (DOT-MTCMOS)", *Japanese
    Journal of Applied Physics* **39**(4S), 2287 (2000).
    <https://doi.org/10.1143/JJAP.39.2287>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005. <https://doi.org/10.1117/3.601520>
