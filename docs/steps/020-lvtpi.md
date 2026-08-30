(step-020)=
# Step 020 — LVTPI: Low V P-channel implant

| | |
|---|---|
| **Step number** | 20 of 171 |
| **Step code** | `LVTPI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`NWI2 <step-019>` |
| **Next step** | {ref}`LVTPIS <step-021>` |

## What this step is

`LVTPI` is the third and last implant placed through the N-well
resist of {ref}`NWM <step-017>`, after the two well implants
{ref}`NWI <step-018>` and {ref}`NWI2 <step-019>`. Where those set the
buried profile of the N-well, `LVTPI` is a low-energy *channel*
implant that sets the surface doping under the future PMOS gates —
that is, the PMOS threshold voltage. The step list calls it the
"Low V P-channel implant"; the code reads naturally as
"low-voltage(-Vt) P-channel implant". Because it shares the N-well
window, it reaches every N-well region on the wafer: the 1.8 V PMOS,
the 5 V PMOS, the N-well rings and the drain extensions alike, unless
the reticle is generated differently for some of them (not public).
It is the P-channel counterpart of {ref}`NCHI <step-045>`, the
N-channel implant that the 1.8 V NMOS receive later under the
low-voltage oxide mask.

The step's position is what makes it economical: no extra
lithography is needed because the N-well mask already outlines exactly
the regions where PMOS channels can exist. The IBM retrograde-well
patent describes the same arrangement, with a "low dose implant …
(50 kEv, 5×10 E 11 per cm²)" of phosphorus as the shallowest member
of the N-well chain, placed through the same mask (PAT-WELL-IBM).

## Step category

`LVTPI` is an {ref}`Ion implantation <category-implant>` step of the
*threshold-adjust* class — light dose, tens of keV, medium-current
tool (category page) — even though it is grouped with the well
implants in the flow.

## Why this step exists

The PMOS threshold must be set independently of the well profile. The
buried N-well peak of {ref}`NWI <step-018>` is placed deep for
latch-up and punch-through reasons and leaves the surface only
lightly doped; a p⁺-gated surface-channel PMOS on such a surface would
have too small a |Vt|. A shallow n-type implant raises the surface
concentration to the value that gives the wanted threshold; in the
body-effect expression γ ∝ √N (WIKI-VT), and multi-Vt CMOS is made by
"altering the concentration of dopant atoms in the channel region
beneath the gate oxide" (WIKI-MTCMOS). The 2001 ITRS FEP table gives,
as illustration of the magnitudes involved, a "Uniform channel
concentration … for Vt=0.4" of 0.8–1.5 × 10¹⁸ cm⁻³ for the 2001
high-performance node and a "Retrograde channel depth" of 21–30 nm
(ITRS-01) — SKY130's 1.8 V devices are a low-power, longer-channel
design and will not match those numbers, but the order of magnitude
is the same.

`LVTPI` therefore establishes the *baseline* PMOS: `pfet_01v8` and,
we infer, the 5 V `pfet_g5v0d10v5`. The other PMOS flavours are
derived from it — `pfet_01v8_hvt` by the additional implants of
{ref}`PCHI <step-023>`/{ref}`PNCHI <step-024>` under
{ref}`HVTPM <step-022>`, and `pfet_01v8_lvt` through the `lvtn`
blocking layer (PDK-07; PDK-PERIPH; see {ref}`LVTNM <step-014>`).

## How it is typically performed

An industry-generic PMOS threshold implant for a 200 mm, 130 nm-era
fab (SKY130 values are not public):

* **Species.** For a surface-channel PMOS with a p⁺ polysilicon gate
  the threshold-setting species is *n-type*: arsenic, which stays
  shallow and diffuses slowly, or phosphorus. The Round Rock/Micron
  multi-Vt patent uses "an implant of Arsenic" as its first threshold
  adjust (PAT-VT-RRR); IBM used 50 keV phosphorus at 5 × 10¹¹ cm⁻²
  (PAT-WELL-IBM). A *p-type* species (boron/BF₂) would instead
  counter-dope the surface and lower |Vt| — the recipe of a
  buried-channel PMOS with an n⁺ gate, which was common up to the
  0.35 µm generation but rare at 130 nm (TXT-04). Which SKY130 uses is
  not public; arsenic or phosphorus is the more plausible reading,
  and "BF2" appears in the public step list only for the *high-Vt*
  module ({ref}`PNCHI <step-024>`).
* **Energy and dose.** Tens of keV and 10¹²–10¹³ cm⁻² are typical for
  threshold adjusts (category page; PAT-VT-LSI gives 1 × 10¹²–1 × 10¹³
  cm⁻² for the boron equivalent; PAT-VT-AMD 1.0–2.5 × 10¹³ cm⁻²).
* **Tilt and twist.** 7° with twist (WIKI-IMPLANT; TXT-02); the
  implant is symmetric, so no rotation is needed.
* **Screen oxide.** Through the pad oxide of 10–20 nm that a Cypress
  patent describes under its well and channel implants (PAT-04).
* **Charge control.** Electron shower; the resist is thick and
  already charged by two MeV implants (SKW-01 lists "E shower" on the
  8250).
* **Anneal.** {ref}`RTAI <step-034>` — "a rapid thermal anneal is
  performed after implanting both the n-well and p-well" and "any
  number of channel implants may also be performed … to adjust
  threshold voltages" before it (PAT-03).

## Machines typically used

* **Medium-current implanter** with serial end station and tilt:
  Axcelis (Eaton) 8250/8250HT ("3keV to 750keV", AXCELIS-8250),
  Varian E220/E500, Nissin (category page).
* If the batch high-energy tool has just run `NWI`/`NWI2`, some fabs
  run the channel implant on it too to avoid a cassette move; both
  tool classes cover tens of keV.
* **Thermal-wave** metrology for dose control.

## Machines likely used at SkyWater

* **Axcelis 8250 medium-current** — "B11, BF2, As, ESC chuck, E
  shower, 1e11 to 1e14, 0-60 deg tilt" (SKW-01): arsenic is available
  and the dose window fits. Strength: **strong** for the tool;
  assignment is an **inference**. Note that phosphorus is *not* in
  the 8250's public species list, which favours arsenic if this tool
  is used.
* **Axcelis GSD** — "B11, BF2, P, As, 10-3000kev" (SKW-01) could run
  either species. Strength: strong for existence.

## Resources required

* **Arsine (AsH₃)** or **phosphine (PH₃)** source gas (WIKI-IMPLANT);
  **BF₃** if the implant is p-type.
* Support gases, cryopump and source consumables, monitor wafers
  (category page).
* No new resist: the {ref}`NWM <step-017>` resist is reused.

## Related steps and cross-references

* Previous: {ref}`NWI2 <step-019>`; next: {ref}`LVTPIS <step-021>`
  (strip of the N-well resist).
* Threshold companions: {ref}`LVTNI <step-015>` (NMOS low-Vt),
  {ref}`PCHI <step-023>`/{ref}`PNCHI <step-024>` (PMOS high-Vt),
  {ref}`NCHI <step-045>` (N-channel baseline).
* Activated at {ref}`RTAI <step-034>`; the PMOS gate oxide grows at
  {ref}`GOX100 <step-043>`/{ref}`LVGOX <step-047>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 (Axcelis 8250 species and dose range; GSD).
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **PDK-07** — SkyWater PDK Authors, *Device Details* (`pfet_01v8`,
  `pfet_01v8_lvt`, `pfet_01v8_hvt`, `pfet_g5v0d10v5`).
  <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
* **PDK-PERIPH** — SkyWater PDK Authors, *Periphery rules* (`lvtn`
  and `hvtp` function text).
  <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
* **PAT-03** — W. Koutny et al. (Cypress), US 8,093,128 B2, granted
  2012-01-10 (channel implants and RTA before the SONOS module).
  <https://patents.google.com/patent/US8093128B2/en>
* **PAT-04** — K. Ramkumar et al. (Cypress), US 8,796,098 B1, granted
  2014-08-05 (implants through a 10–20 nm pad oxide).
  <https://patents.google.com/patent/US8796098B1/en>
* **AXCELIS-8250** — Semiconductor Online, *8250HT Medium Current Ion
  Implanter*.
  <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>

### High-level understanding

* **WIKI-IMPLANT** — Wikipedia, *Ion implantation*.
  <https://en.wikipedia.org/wiki/Ion_implantation>
* **WIKI-VT** — Wikipedia, *Threshold voltage*.
  <https://en.wikipedia.org/wiki/Threshold_voltage>
* **WIKI-MTCMOS** — Wikipedia, *Multi-threshold CMOS*.
  <https://en.wikipedia.org/wiki/Multi-threshold_CMOS>
* **TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the
  VLSI Era, Vol. 1*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4, ch. 9.
  <https://openlibrary.org/isbn/9780961672164>
* **TXT-04** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3:
  The Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7
  (surface- versus buried-channel PMOS, dual-gate CMOS).
  <https://openlibrary.org/isbn/9780961672157>

### Deep dive

* **ITRS-01** — ITRS 2001, *Front End Processes* (Table 51: channel
  concentration, retrograde channel depth).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
* **PAT-WELL-IBM** — US 6,667,205 B2 (IBM), granted 2003-12-23
  (50 keV phosphorus channel-side implant through the N-well mask).
  <https://patents.google.com/patent/US6667205B2/en>
* **PAT-VT-RRR** — US 2011/0006372 A1 (Round Rock Research),
  published 2011-01-13 (arsenic first Vt adjust).
  <https://patents.google.com/patent/US20110006372A1/en>
* **PAT-VT-LSI** — US 5,963,801 A (LSI Logic), granted 1999-10-05.
  <https://patents.google.com/patent/US5963801A/en>
* **PAT-VT-AMD** — US 6,238,982 B1 (AMD), granted 2001-05-29.
  <https://patents.google.com/patent/US6238982B1/en>

## Open questions

* Whether "Low V" means low-voltage (1.8 V) or low-Vt, and whether the
  implant also reaches the 5 V PMOS regions, is not stated publicly;
  we read it as the baseline PMOS channel implant for all N-wells.
* Species (arsenic or phosphorus versus BF₂), energy and dose are not
  public.
* Whether SKY130's PMOS is surface-channel with a p⁺ gate — the
  assumption behind the n-type species reading — is inferred from the
  node and the presence of a separate P⁺ source/drain mask
  ({ref}`PSDM <step-081>`), not documented.
