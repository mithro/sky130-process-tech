(step-034)=
# Step 034 — RTAI: Pre-gate oxide anneal

| | |
|---|---|
| **Step number** | 34 of 171[^steps-sheet] |
| **Step code** | `RTAI` |
| **Category** | {ref}`Anneal / thermal processing <category-anneal>` |
| **Phase** | {term}`FEOL` — wells and channel implants |
| **Previous step** | {ref}`PWDEIS <step-033>` |
| **Next step** | {ref}`TUNM <step-035>` |

## What this step is

`RTAI` is the anneal that closes the well and channel module. Ten
implants have gone into the wafer since {ref}`NS19 <step-013>` — the
low-Vt channel implant {ref}`LVTNI <step-015>`, the N-well pair
{ref}`NWI <step-018>`/{ref}`NWI2 <step-019>` and the PMOS channel
implant {ref}`LVTPI <step-020>`, the high-Vt PMOS pair
{ref}`PCHI <step-023>`/{ref}`PNCHI <step-024>`, the P-well pair
{ref}`PWI <step-027>`/{ref}`PWI2 <step-028>` and the {term}`drain-extended <DEMOS>` pair
{ref}`PWDEI1 <step-031>`/{ref}`PWDEI2 <step-032>` — and none has yet
been annealed. `RTAI` heats the wafer, in an inert ambient, to repair
the lattice damage they left, move the dopant atoms onto substitutional
sites where they are electrically active, and settle the well and
channel profiles before the first gate dielectric is grown. This
reference labels it "Pre-gate oxide anneal" and describes it as a
rapid thermal anneal — an inference from the Cypress integration
patent and SkyWater's RTA tool (below). After it, the flow enters
the {term}`SONOS` module ({ref}`TUNM <step-035>`) and then gate oxidation
({ref}`GOX100 <step-043>`).

:::{figure} /_static/figures/wells-034-rtai.svg
:alt: One cross-section of the wafer: pad oxide over a P-well on the left and an N-well on the right, which meet under the middle of an oxide-filled trench, with a thin implanted band at the surface of each active area. The drawing is the same as the state before the step.
:width: 560px
:name: fig-wells-034-rtai

The state the module leaves: at RTAI the wafer is heated to repair the implant damage and activate the implants of the module, and the drawing is the same as before it. No public source says how far the anneal moves any of the wells or channel bands, so no diffusion is drawn. The anneal's temperature, time and ambient are not public. The pad oxide is drawn in place, as the pages assume; whether it is present during the anneal is not stated publicly. The NMOS channel implant, the PMOS channel implant and the liner oxide are drawn faded. Not to scale.
:::

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
clusters" (category page, citing Gibbons and
Plummer).[^gibbons-1972][^txt-01] Three things depend on doing that now
rather than later:

* **Gate-oxide quality.** The gate oxide is grown on a silicon surface
  that has been implanted through a thin pad oxide several times;
  residual damage and interstitial clusters at the surface would be
  incorporated into the oxide and its interface. Annealing first, and
  then removing damaged surface oxide, gives the gate oxidation a clean
  crystal to grow on.[^txt-01]
* **Profile control.** The well and channel profiles set every
  transistor's threshold, body effect and {term}`punch-through` margin.
  Annealing them in one defined step, before the SONOS and gate modules
  add their own thermal cycles, makes the profiles a known starting
  point. Transient enhanced diffusion — the boost in boron and
  phosphorus diffusivity from implant-generated interstitials
  ({term}`TED`) — is worst for slow anneals, "because the damage
  dissolves while the dopant is still mobile"; the resolution is "the
  RTA: seconds at 1000–1100 °C" (category page, citing Stolk et
  al.).[^stolk-1997]
* **Retrograde profiles must stay retrograde.** The point of the MeV
  wells is a peak below the surface; a long furnace drive would smear
  it. ITRS 2001 demands a "Retrograde channel depth" of 21–30 nm for its
  2001 high-performance node,[^itrs-01] which is only compatible with
  short anneals.

The order matters for the SONOS module too. Cypress's integration
patent, which may still be in force, bears on where this step falls and
on what kind of anneal it is; its two sentences are in the collapsed
note below, and they are the strongest public evidence this reference
has on either question.

:::{dropdown} From a patent shown as in force (US 8,093,128; estimated expiry 2028-10-22) — open to read
Cypress's integration patent describes forming the charge-trapping stack
"after at least some of the well and channel implants for the logic MOS
transistors are formed", and states that "a rapid thermal anneal is
performed after implanting both the n-well and p-well".[^pat-03]
:::

## How it is typically performed

An industry-generic well/channel activation anneal for a 200 mm,
130 nm-era fab (SKY130's recipe is not public):

* **Tool and ambient.** Single-wafer lamp-heated RTA in nitrogen or
  argon; {term}`RTP` "heats silicon wafers to temperatures exceeding 1,000°C for
  not more than a few seconds" using "high intensity lamps" with "in
  situ pyrometry to effect real time control".[^wiki-rtp] A small oxygen
  addition is sometimes used to suppress boron out-diffusion from the
  surface; a pure inert ambient avoids growing oxide (category page).
* **Temperature and time.** Published well anneals of the era: "an
  annealing at 1000 C for 10 sec in an RTA (Rapid Thermal Anneal)
  apparatus", after which "the gate insulating layer … is formed on the
  N Well and P Well regions … by a thermal oxidation or CVD (Chemical
  Vapor Deposition) method";[^pat-well-hynix] in
  older flows a well anneal "at approximately 900° C. in a neutral
  ambient such as nitrogen for approximately 30 minutes" (the patent does
  not name the tool).[^pat-vt-lsi] A
  1000–1050 °C, 10–30 s RTA is the typical 130 nm-era
  choice.[^txt-05][^txt-10] Ramp rates of "1 – 180°C per second" are the
  range of the AG Associates Heatpulse 8800-class tools.[^ag-8800]
* **Sequence.** Pre-anneal clean (at {ref}`PWDEIS <step-033>`); load;
  purge; ramp; soak; ramp-down; unload. The pad oxide, if retained, caps
  the surface during the soak.
* **Control.** Pyrometer emissivity calibration against
  thermocouple-instrumented wafers; edge-ring design to avoid slip;
  sheet-resistance mapping of monitor wafers after each lot to track
  activation and uniformity (category page).[^txt-10]
* **Furnace alternative.** A vertical furnace at 900–1000 °C for tens of
  minutes (typical)[^txt-01] gives the same activation with more
  diffusion, and some fabs prefer it for wells precisely because a
  little extra drive smooths the chained profiles ("Increasingly,
  furnace anneals are being supplanted by Rapid Thermal
  Anneal").[^wiki-furnace]

## Machines typically used

* **{ref}`Rapid thermal processors <machine-rapid-thermal-processor>`**, 200 mm: AG Associates Heatpulse
  8108/8800 series, Applied Materials RTP Centura (XE/Radiance), Steag
  (later Mattson) RTP, Kokusai and TEL RTP (category page).
* **{ref}`Vertical furnaces <machine-vertical-furnace-anneal>`** (ASM A400, TEL Alpha-8, Aviza/Thermco) as the
  batch alternative.
* **{term}`Four-point probe <four-point probe>`** ({ref}`sheet-resistance metrology <machine-sheet-resistance-metrology>`) for {term}`sheet resistance`; **thermocouple wafers**
  for calibration.

## Machines likely used at SkyWater

* **AG Associates Heatpulse 8808.** SkyWater's facilities page lists
  under RTA "Ag Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C"[^skw-01] —
  a single-wafer RTA with the inert ambients (Ar, N₂) and the
  temperature reach this step needs. Strength: **strong** for the tool
  (SkyWater statement); assignment to `RTAI` is an **inference** from
  the Cypress integration patent, which may still be in force (collapsed
  note below this list).
  Reseller documentation for the Heatpulse 8800/8808 family gives a
  "Recommended steady-state temperature range: 400 – 1200°C", ramp-up
  "Programmable, 1 – 180°C per second", "2 banks of 14 lamps" with
  "10-zone lamp control", pyrometer or thermocouple sensing, wafer sizes
  to 8 inches, and "Implant annealing" among the listed
  applications[^ag-8800] (the reseller's family specification PDF gives, in its
  Heatpulse 8108 section, the same 400–1200 °C range, a programmable
  1–180 °C/s ramp-up, a maximum ramp-down of 150 °C/s and ±5 °C
  uniformity across an 8-inch (200 mm) wafer at 1150 °C; its Heatpulse
  4100 section differs: 400–1300 °C, 10–200 °C/s ramp-up and ±5 °C
  across a 6-inch (150 mm) wafer).[^ag-8108]
* **Aviza furnaces.** SkyWater's facilities page states "Furnaces are
  all made by Aviza"[^skw-01] with "Ar anneal to 1150C" and "N2 anneal
  to 1150C" — the batch alternative if the fab chose a furnace well
  anneal. Strength: strong for existence; weak for assignment, since the
  Cypress integration patent, which may still be in force, bears on it
  (collapsed note below this list).

:::{dropdown} From a patent shown as in force (US 8,093,128; estimated expiry 2028-10-22) — open to read
The assignment to `RTAI` follows the Cypress integration patent's rapid
thermal anneal after the well implants; the same patent describes an RTA
rather than a furnace anneal at this point.[^pat-03]
:::

## Resources required

* **{ref}`Nitrogen <material-process-gases>` and argon** (likely ambient, our inference; SkyWater lists
  the Heatpulse's gases, "NH3, Ar, N2, O2", but no ambient for any
  step);[^skw-01] **oxygen** if a minor addition is used.
* **{ref}`Tungsten-halogen lamps <material-hardware-consumables>`, quartz chamber/window, edge rings**;
  pyrometer calibration and {ref}`thermocouple wafers <material-substrates>` (category page).
* **Cooling water and CDA/N₂** for lamp and chamber cooling (facility
  table for the Heatpulse 4100).[^ag-8108]
* **Monitor wafers** (SEMI M8 class) for sheet resistance.
* Gas suppliers named in SkyWater's filings: Air Products and Praxair
  (2021 S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]

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

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Apparatus for heating semiconductor wafers in order to achieve annealing, silicide formation, reflow of glass passivation layers, etc. <patent-gp27541944>` — US 4,649,261 A (1984)
* {ref}`Rapid thermal heating apparatus and method <patent-gp27042189>` — US 5,155,336 A (1990)
* {ref}`Method of forming retrograde well structures and punch-through barriers using low energy implants <patent-gp25087511>` — US 5,963,801 A (1996)
* {ref}`Method of forming retrograde doping file in twin well CMOS device <patent-gp19572018>` — US 6,455,402 B2 (1999)

:::{dropdown} 3 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 2002/0090817 A1 <patent-gp23341388>` — unknown
* {ref}`US 8,093,128 B2 <patent-gp40072804>` — in force
* {ref}`US 9,236,448 B2 <patent-gp41726088>` — unknown
:::
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — "Ag Heatpulse 8808 NH3, Ar,
  N2, O2, up to 1200C"; Aviza furnaces, Ar/N₂ anneal to
  1150 °C.[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]
* [SemiStar, *AG Associates Heatpulse 8800 / 8808* reseller page](<https://www.semistarcorp.com/product/ag-associates-heatpulse-8800-8808/>) —
  temperature range, ramp rates, lamp banks and applications.[^ag-8800]
* [SemiStar, *AG Associates Heatpulse 4100 / 8108 / 8800 / 8800i
  Specifications* (PDF)](<https://www.semistarcorp.com/wp-content/uploads/2025/12/AG-Associates-Heatpulse-4100-8108-8800-8800i-Specifications-Rapid-Thermal-Processor.pdf>) — operating specifications and facility tables
  of the Heatpulse 4100 and 8108.[^ag-8108]

:::{dropdown} From a patent shown as in force (US 8,093,128; estimated expiry 2028-10-22) — open to read
* Koutny et al. (Cypress), US 8,093,128 — "a rapid thermal anneal is
  performed after implanting both the n-well and p-well".[^pat-03]
:::

### High-level understanding

* [Wikipedia, *Rapid thermal processing*](<https://en.wikipedia.org/wiki/Rapid_thermal_processing>) — lamp heating, seconds above
  1000 °C, in-situ pyrometry.[^wiki-rtp]
* [Wikipedia, *Furnace anneal*](<https://en.wikipedia.org/wiki/Diffusion_furnace>) — furnace anneals being supplanted by
  RTA.[^wiki-furnace]
* [Plummer, Deal and Griffin, *Silicon VLSI Technology*](<https://openlibrary.org/isbn/9780130850379>) — ch. 2 (CMOS
  well formation) and ch. 8 (ion implantation).[^txt-01]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) — RTP.[^txt-05]

### Deep dive

* [Fair (ed.), *Rapid Thermal Processing: Science and Technology*](<https://doi.org/10.1016/b978-0-12-247690-7.50009-3>) — the
  chapter on junction formation by rapid thermal annealing.[^txt-10]
* [ITRS 2001, *Front End Processes*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>) — Table 51, retrograde channel
  depth.[^itrs-01]
* [Lee and Son (Hyundai/Hynix), US 6,455,402](<https://patents.google.com/patent/US6455402B2/en>) — RTA 1000 °C, 10 s, then
  gate oxidation.[^pat-well-hynix]
* [Aronowitz, Khan and Kimball (LSI Logic), US 5,963,801](<https://patents.google.com/patent/US5963801A/en>) — a well
  anneal at 900 °C for 30 min in nitrogen, tool not named.[^pat-vt-lsi]
* [Stolk et al. (Bell Labs), *J. Appl. Phys.* 1997](<https://doi.org/10.1063/1.364452>) — the physical
  mechanisms of transient enhanced diffusion.[^stolk-1997]
* [Roozeboom and Parekh (Philips), *J. Vac. Sci. Technol. B* 1990](<https://doi.org/10.1116/1.584902>) — a
  review of RTP systems with emphasis on temperature
  control.[^roozeboom-1990]
* [Fiory, *J. Electron. Mater.* 2002](<https://doi.org/10.1007/s11664-002-0031-9>) — RTP developments of the 130 nm
  era.[^fiory-2002]
* [Michel et al. (IBM), *Appl. Phys. Lett.* 1987](<https://doi.org/10.1063/1.98160>) — the first report of
  anomalous boron diffusion under rapid annealing.[^michel-1987]
* [Eaglesham et al. (AT&T), *Appl. Phys. Lett.* 1994](<https://doi.org/10.1063/1.112725>) — the interstitial
  source behind transient enhanced boron diffusion.[^eaglesham-1994]
* [Gronet and Gibbons (Applied Materials), US 5,155,336](<https://patents.google.com/patent/US5155336A/en>) — a lamp-heated
  single-wafer RTP chamber design.[^pat-rtp-amat]
* [Sheets (Tamarack Scientific), US 4,649,261](<https://patents.google.com/patent/US4649261A/en>) — an early lamp-heating
  apparatus for wafer annealing.[^pat-rtp-tamarack]
* [Taur et al., *Proc. IEEE* 1997](<https://doi.org/10.1109/5.573737>) — why retrograde channel profiles
  demand short anneals.[^taur-1997]

## Open questions

* The SKY130 anneal temperature, time and ambient are not public; the
  1000 °C/10 s figure is from a contemporaneous third-party patent.
* Whether `RTAI` is a single RTA or an RTA plus a short furnace step,
  and whether the Heatpulse 8808 or an Aviza furnace runs it, is
  inferred from the Cypress integration patent (collapsed notes above)
  and SkyWater's tool list.[^skw-01]
* Whether the pad oxide is present during the anneal, and where the
  sacrificial oxide before gate oxidation is removed, is not stated
  publicly (see {ref}`NS19 <step-013>` and {ref}`PWDEIS <step-033>`).
* The reseller's specification PDF cited for the Heatpulse
  family[^ag-8108] documents the Heatpulse 4100, 8108, 8800 and 8800i, not the 8808
  itself; the two share a family but the
  8808's own data sheet is not public.

<!-- footnotes -->

[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
    Shown as in force; estimated expiry 2028-10-22 (estimate from public
    records, not legal advice).
[^wiki-rtp]: Wikipedia, *Rapid thermal processing*.
    <https://en.wikipedia.org/wiki/Rapid_thermal_processing>
[^pat-well-hynix]: J.-H. Lee and J.-H. Son (Hyundai/Hynix), *Method of
    forming retrograde doping profile in twin well CMOS device*, US
    6,455,402 B2, granted 2002-09-24.
    <https://patents.google.com/patent/US6455402B2/en>
[^pat-vt-lsi]: S. Aronowitz, L. Khan and J. Kimball (LSI Logic), *Method
    of forming retrograde well structures and punch-through barriers
    using low energy implants*, US 5,963,801 A, granted 1999-10-05.
    <https://patents.google.com/patent/US5963801A/en>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^txt-10]: R. B. Fair (ed.), *Rapid Thermal Processing: Science and
    Technology*, Academic Press, 1993, ISBN 978-0-12-247690-7; R. B.
    Fair, "Junction Formation in Silicon by Rapid Thermal Annealing",
    pp. 169–226. <https://doi.org/10.1016/b978-0-12-247690-7.50009-3>
[^ag-8800]: SemiStar Corp., *AG Associates Heatpulse 8800 / 8808 Rapid
    Thermal Processing* (reseller specification page), accessed
    2026-08-30.
    <https://www.semistarcorp.com/product/ag-associates-heatpulse-8800-8808/>
[^wiki-furnace]: Wikipedia, *Furnace anneal*.
    <https://en.wikipedia.org/wiki/Diffusion_furnace>
[^ag-8108]: SemiStar Corp., *AG Associates Heatpulse 4100 / 8108 / 8800
    / 8800i Specifications* (reseller PDF; operating specifications for
    the Heatpulse 4100 and 8108), accessed 2026-08-30.
    <https://www.semistarcorp.com/wp-content/uploads/2025/12/AG-Associates-Heatpulse-4100-8108-8800-8800i-Specifications-Rapid-Thermal-Processor.pdf>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^stolk-1997]: P. A. Stolk, H.-J. Gossmann, D. J. Eaglesham, D. C.
    Jacobson, C. S. Rafferty, G. H. Gilmer, M. Jaraíz, J. M. Poate, H.
    S. Luftman and T. E. Haynes, "Physical mechanisms of transient
    enhanced dopant diffusion in ion-implanted silicon", *Journal of
    Applied Physics* **81**(9), 6031–6050 (1997).
    <https://doi.org/10.1063/1.364452>
[^roozeboom-1990]: F. Roozeboom and N. Parekh, "Rapid thermal processing
    systems: A review with emphasis on temperature control", *Journal of
    Vacuum Science & Technology B* **8**(6), 1249–1259 (1990).
    <https://doi.org/10.1116/1.584902>
[^fiory-2002]: A. T. Fiory, "Recent developments in rapid thermal
    processing", *Journal of Electronic Materials* **31**(10), 981–987
    (2002). <https://doi.org/10.1007/s11664-002-0031-9>
[^michel-1987]: A. E. Michel, W. Rausch, P. A. Ronsheim and R. H. Kastl,
    "Rapid annealing and the anomalous diffusion of ion implanted boron
    into silicon", *Applied Physics Letters* **50**(7), 416–418 (1987).
    <https://doi.org/10.1063/1.98160>
[^eaglesham-1994]: D. J. Eaglesham, P. A. Stolk, H.-J. Gossmann and J.
    M. Poate, "Implantation and transient B diffusion in Si: The source
    of the interstitials", *Applied Physics Letters* **65**(18),
    2305–2307 (1994). <https://doi.org/10.1063/1.112725>
[^pat-rtp-amat]: C. M. Gronet and J. F. Gibbons (Applied Materials),
    *Rapid thermal heating apparatus and method*, US 5,155,336 A,
    granted 1992-10-13.
    <https://patents.google.com/patent/US5155336A/en>
[^pat-rtp-tamarack]: R. E. Sheets (Tamarack Scientific), *Apparatus for
    heating semiconductor wafers in order to achieve annealing, silicide
    formation, reflow of glass passivation layers, etc.*, US 4,649,261
    A, granted 1987-03-10.
    <https://patents.google.com/patent/US4649261A/en>
[^taur-1997]: Y. Taur, D. A. Buchanan, W. Chen, D. J. Frank, K. E.
    Ismail, S.-H. Lo, G. A. Sai-Halasz, R. G. Viswanathan, H.-J. C.
    Wann, S. J. Wind and H.-S. Wong, "CMOS scaling into the nanometer
    regime", *Proceedings of the IEEE* **85**(4), 486–504 (1997).
    <https://doi.org/10.1109/5.573737>
[^gibbons-1972]: J. F. Gibbons, "Ion implantation in semiconductors —
    Part II: Damage production and annealing", *Proceedings of the IEEE*
    **60**(9), 1062–1096 (1972). <https://doi.org/10.1109/PROC.1972.8854>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
