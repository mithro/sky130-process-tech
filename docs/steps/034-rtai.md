(step-034)=
# Step 034 — RTAI: Pre-gate oxide anneal

| | |
|---|---|
| **Step number** | 34 of 171 |
| **Step code** | `RTAI` |
| **Category** | {ref}`Anneal / thermal processing <category-anneal>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`PWDEIS <step-033>` |
| **Next step** | {ref}`TUNM <step-035>` |

## What this step is

`RTAI` is the anneal that closes the well and channel module. Ten
implants have gone into the wafer since {ref}`NS19 <step-013>` — the
low-Vt channel implant {ref}`LVTNI <step-015>`, the N-well pair
{ref}`NWI <step-018>`/{ref}`NWI2 <step-019>` and the PMOS channel
implant {ref}`LVTPI <step-020>`, the high-Vt PMOS pair
{ref}`PCHI <step-023>`/{ref}`PNCHI <step-024>`, the P-well pair
{ref}`PWI <step-027>`/{ref}`PWI2 <step-028>` and the drain-extended
pair {ref}`PWDEI1 <step-031>`/{ref}`PWDEI2 <step-032>` — and none has
yet been annealed. `RTAI` heats the wafer, in an inert ambient, to
repair the lattice damage they left, move the dopant atoms onto
substitutional sites where they are electrically active, and settle
the well and channel profiles before the first gate dielectric is
grown. The step list calls it the "Pre-gate oxide anneal"; the code
`RTAI` reads as "RTA, implant" — a rapid thermal anneal — and the
public evidence supports that reading (below). After it, the flow
enters the SONOS module ({ref}`TUNM <step-035>`) and then gate
oxidation ({ref}`GOX100 <step-043>`).

The only other anneal the wells have seen is incidental: the deep
N-well of {ref}`DNI <step-008>` was driven by the liner oxidation at
{ref}`LINOX <step-010>` and the subsequent isolation steps (see
{ref}`DNM <step-007>`), but every implant since then has waited for
this step.

## Step category

`RTAI` is an {ref}`Anneal / thermal processing <category-anneal>` step
of the *implant activation and well anneal* type, the first of the
four such anneals in the flow (the others are
{ref}`TIPRTAD <step-075>`, {ref}`RTAD <step-088>` and
{ref}`RTAD2 <step-092>`). It is the one with the deepest profiles to
anneal and the least concern for junction movement, so it can be the
hottest and longest of the four.

## Why this step exists

Implanted dopant is inactive until the lattice is restored, and
"partially damaged layers need 800–1000 °C to dissolve the defect
clusters" (category page, citing Gibbons and Plummer). Three things
depend on doing that now rather than later:

* **Gate-oxide quality.** The gate oxide is grown on a silicon
  surface that has been implanted through a thin pad oxide several
  times; residual damage and interstitial clusters at the surface
  would be incorporated into the oxide and its interface. Annealing
  first, and then removing damaged surface oxide, gives the gate
  oxidation a clean crystal to grow on (TXT-01, ch. 6 and 8).
* **Profile control.** The well and channel profiles set every
  transistor's threshold, body effect and punch-through margin.
  Annealing them in one defined step, before the SONOS and gate
  modules add their own thermal cycles, makes the profiles a known
  starting point. Transient enhanced diffusion — the boost in boron
  and phosphorus diffusivity from implant-generated interstitials
  ({term}`TED`) — is worst for slow anneals, "because the damage
  dissolves while the dopant is still mobile"; the resolution is "the
  RTA: seconds at 1000–1100 °C" (category page, citing Stolk et al.).
* **Retrograde profiles must stay retrograde.** The point of the MeV
  wells is a peak below the surface; a long furnace drive would
  smear it. ITRS 2001 demands a "Retrograde channel depth" of
  21–30 nm for its 2001 high-performance node (ITRS-01), which is
  only compatible with short anneals.

The order matters for the SONOS module too. Cypress's integration
patent describes forming the charge-trapping stack "after at least
some of the well and channel implants for the logic MOS transistors
are formed", and states that "a rapid thermal anneal is performed
after implanting both the n-well and p-well" (PAT-03) — the strongest
public evidence that the SKY130 lineage anneals its wells by RTA
before the SONOS and gate steps.

## How it is typically performed

An industry-generic well/channel activation anneal for a 200 mm,
130 nm-era fab (SKY130's recipe is not public):

* **Tool and ambient.** Single-wafer lamp-heated RTA in nitrogen or
  argon; RTP "heats silicon wafers to temperatures exceeding 1,000°C
  for not more than a few seconds" using "high intensity lamps" with
  "in situ pyrometry to effect real time control" (WIKI-RTP). A small
  oxygen addition is sometimes used to suppress boron out-diffusion
  from the surface; a pure inert ambient avoids growing oxide
  (category page).
* **Temperature and time.** Published well anneals of the era: "an
  annealing at 1000 C for 10 sec in an RTA (Rapid Thermal Anneal)
  apparatus", after which "the gate insulating layer is formed on the
  N well and P well regions by a thermal oxidation" (PAT-WELL-HYNIX);
  in older flows a furnace at "approximately 900 °C in a neutral
  ambient such as nitrogen for approximately 30 minutes"
  (PAT-VT-LSI). A 1000–1050 °C, 10–30 s RTA is the typical
  130 nm-era choice (TXT-05; TXT-10). Ramp rates of "1 – 180°C per
  second" are the range of the AG Heatpulse 8800-class tools
  (AG-8800).
* **Sequence.** Pre-anneal clean (at {ref}`PWDEIS <step-033>`);
  load; purge; ramp; soak; ramp-down; unload. The pad oxide, if
  retained, caps the surface during the soak.
* **Control.** Pyrometer emissivity calibration against
  thermocouple-instrumented wafers; edge-ring design to avoid slip;
  sheet-resistance mapping of monitor wafers after each lot to track
  activation and uniformity (category page; TXT-10).
* **Furnace alternative.** A vertical furnace at 900–1000 °C for tens
  of minutes gives the same activation with more diffusion, and some
  fabs prefer it for wells precisely because a little extra drive
  smooths the chained profiles (WIKI-FURNACE: "Increasingly, furnace
  anneals are being supplanted by Rapid Thermal Anneal").

## Machines typically used

* **Rapid thermal processors**, 200 mm: AG Associates Heatpulse
  8108/8800 series, Applied Materials RTP Centura (XE/Radiance), Steag
  (later Mattson) RTP, Kokusai and TEL RTP (category page).
* **Vertical furnaces** (ASM A400, TEL Alpha-8, Aviza/Thermco) as the
  batch alternative.
* **Four-point probe** for sheet resistance; **thermocouple wafers**
  for calibration.

## Machines likely used at SkyWater

* **AG Associates Heatpulse 8808.** SKW-01 lists under RTA "Ag
  Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C" — a single-wafer RTA
  with the inert ambients (Ar, N₂) and the temperature reach this
  step needs. Strength: **strong** for the tool (SkyWater statement);
  assignment to `RTAI` is an **inference** from the step name and
  from PAT-03. Reseller documentation for the Heatpulse 8800/8808
  family gives a "Recommended steady-state temperature range: 400 –
  1200°C", ramp-up "Programmable, 1 – 180°C per second", "2 banks of
  14 lamps" with "10-zone lamp control", pyrometer or thermocouple
  sensing, wafer sizes to 8 inches, and "Implant annealing" among
  the listed applications (AG-8800; the specification sheet for the
  sibling 8108 gives the same 400–1200 °C range and ±5 °C uniformity
  across an 8-inch wafer at 1150 °C, AG-8108).
* **Aviza furnaces.** SKW-01 states "Furnaces are all made by Aviza"
  with "Ar anneal to 1150C" and "N2 anneal to 1150C" — the batch
  alternative if the fab chose a furnace well anneal. Strength:
  strong for existence; weak for assignment, since the step code
  says RTA.

## Resources required

* **Nitrogen and argon** (process ambient, SKW-01); **oxygen** if a
  minor addition is used.
* **Tungsten-halogen lamps, quartz chamber/window, edge rings**;
  pyrometer calibration and thermocouple wafers (category page).
* **Cooling water and CDA/N₂** for lamp and tube cooling (AG-8108).
* **Monitor wafers** (SEMI M8 class) for sheet resistance.
* Gas suppliers named by SkyWater: Air Products, Praxair, Linde,
  Airgas (SEC-01, SEC-02).

## Related steps and cross-references

* Previous: {ref}`PWDEIS <step-033>` (strip and pre-anneal clean).
* Next: {ref}`TUNM <step-035>` (start of the SONOS module); gate
  oxidation at {ref}`GOX100 <step-043>` and {ref}`LVGOX <step-047>`.
* Anneals every implant from {ref}`LVTNI <step-015>` to
  {ref}`PWDEI2 <step-032>`; the deep N-well ({ref}`DNI <step-008>`)
  was annealed earlier by {ref}`LINOX <step-010>`.
* Later RTAs: {ref}`TIPRTAD <step-075>`, {ref}`RTAD <step-088>`,
  {ref}`RTAD2 <step-092>`.
* Category page: {ref}`Anneal / thermal processing <category-anneal>`.

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 ("Ag Heatpulse 8808 NH3, Ar, N2, O2, up to
  1200C"; Aviza furnaces, Ar/N₂ anneal to 1150 °C).
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **SEC-01 / SEC-02** — SkyWater Technology, Inc., Form S-1 (2021) and
  Form 10-K (fiscal 2023).
  <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>,
  <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
* **PAT-03** — W. Koutny et al. (Cypress), US 8,093,128 B2,
  *Integration of non-volatile charge trap memory devices and logic
  CMOS devices*, granted 2012-01-10 ("a rapid thermal anneal is
  performed after implanting both the n-well and p-well").
  <https://patents.google.com/patent/US8093128B2/en>
* **AG-8800** — SemiStar Corp., *AG Associates Heatpulse 8800 / 8808
  Rapid Thermal Processing* (reseller specification page), accessed
  2026-08-30.
  <https://www.semistarcorp.com/product/ag-associates-heatpulse-8800-8808/>
* **AG-8108** — SemiStar Corp., *AG Associates Heatpulse 4100 / 8108 /
  8800 / 8800i Specifications* (PDF), accessed 2026-08-30.
  <http://www.semistarcorp.com/wp-content/uploads/2025/12/AG-Associates-Heatpulse-4100-8108-8800-8800i-Specifications-Rapid-Thermal-Processor.pdf>

### High-level understanding

* **WIKI-RTP** — Wikipedia, *Rapid thermal processing*.
  <https://en.wikipedia.org/wiki/Rapid_thermal_processing>
* **WIKI-FURNACE** — Wikipedia, *Furnace anneal*.
  <https://en.wikipedia.org/wiki/Diffusion_furnace>
* **TXT-01** — J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon
  VLSI Technology*, Prentice Hall, 2000, ISBN 978-0-13-085037-9,
  ch. 6–8.
  <https://openlibrary.org/isbn/9780130850379>
* **TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4*,
  Lattice Press, 2002, ISBN 978-0-9616721-7-1 (RTP).
  <https://openlibrary.org/isbn/9780961672171>

### Deep dive

* **TXT-10** — R. B. Fair (ed.), *Rapid Thermal Processing: Science
  and Technology*, Academic Press, 1993, ISBN 978-0-12-247690-7;
  R. B. Fair, "Junction Formation in Silicon by Rapid Thermal
  Annealing". <https://doi.org/10.1016/b978-0-12-247690-7.50009-3>
* **ITRS-01** — ITRS 2001, *Front End Processes* (Table 51, retrograde
  channel depth).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
* **PAT-WELL-HYNIX** — J.-H. Lee and J.-H. Son (Hyundai/Hynix),
  US 6,455,402 B2, granted 2002-09-24 (RTA 1000 °C, 10 s, then gate
  oxidation).
  <https://patents.google.com/patent/US6455402B2/en>
* **PAT-VT-LSI** — US 5,963,801 A (LSI Logic), granted 1999-10-05
  (furnace 900 °C, 30 min, N₂).
  <https://patents.google.com/patent/US5963801A/en>
* **STOLK-1997** — P. A. Stolk et al., "Physical mechanisms of
  transient enhanced dopant diffusion in ion-implanted silicon",
  *Journal of Applied Physics*, vol. 81, pp. 6031–6050, 1997,
  DOI 10.1063/1.364452. <https://doi.org/10.1063/1.364452>

## Open questions

* The SKY130 anneal temperature, time and ambient are not public; the
  1000 °C/10 s figure is from a contemporaneous third-party patent.
* Whether `RTAI` is a single RTA or an RTA plus a short furnace step,
  and whether the Heatpulse 8808 or an Aviza furnace runs it, is
  inferred from the step code and SKW-01.
* Whether the pad oxide is present during the anneal, and where the
  sacrificial oxide before gate oxidation is removed, is not
  resolvable from the public step list (see {ref}`NS19 <step-013>` and
  {ref}`PWDEIS <step-033>`).
* The expansion of `RTAI` ("RTA, implant"?) is our reading of the
  code.
