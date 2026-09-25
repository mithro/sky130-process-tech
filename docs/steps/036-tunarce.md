(step-036)=
# Step 036 — TUNARCE: Tunnel mask ARC etch

| | |
|---|---|
| **Step number** | 36 of 171[^steps-sheet] |
| **Step code** | `TUNARCE` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | {term}`FEOL` — SONOS and gate dielectrics |
| **Previous step** | {ref}`TUNM <step-035>` |
| **Next step** | {ref}`PTSI <step-037>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** on this reference's reading, etches the ARC out of the
  tunnel windows, stopping on the oxide beneath.
* **Why:** the coating would otherwise absorb part of the following
  implants' dose (inference) and block the later oxide etch.
* **Public numbers:** none published for SKY130.
* **Likely SkyWater tool:** Applied Materials DPS II — strong (tool);
  inference (assignment).[^skw-01]
* **Not public:** whether the ARC is organic or inorganic, and its
  thickness (→ Open questions).
:::

## What this step is

The step list describes `TUNARCE` as "Tunnel mask ARC etch" and does not
explain it.[^steps-sheet] We read it as a short plasma etch that removes
the anti-reflective coating from the bottom of the windows that
{ref}`TUNM <step-035>` opened in the photoresist.

A bottom anti-reflective coating
({term}`BARC`) is spun on *under* the resist and is not photosensitive.

After
develop, the resist is gone from the tunnel windows, but the {term}`ARC`
film still covers the oxide inside them — the pad oxide from
{ref}`BOX <step-002>`, we infer (its retention is not public).

This etch
transfers the resist pattern through the ARC and stops on that oxide, so
that the
two implants that follow ({ref}`PTSI <step-037>`,
{ref}`DEPI <step-038>`) enter the silicon through a known, thin oxide
only. It also lets the wet etch at {ref}`TUNME <step-039>` reach and
remove that oxide.

:::{figure} /_static/figures/sonos-036-tunarce.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step photoresist covers the surface except for a window over the right-hand active area, and a thin anti-reflective film runs under the resist and across the bottom of the window. After it the film is gone from the bottom of the window, leaving the thin pad oxide bare there, and is unchanged under the resist.
:width: 560px
:name: fig-sonos-036-tunarce

Before, the tunnel-mask window with the anti-reflective coating still across its bottom; after, the coating cleared from the window only, down to the oxide, and left in place under the resist. The step list gives only the step's name; that it is an etch of the coating in the windows, stopping on the oxide, is this page's reading.[^steps-sheet] Whether the coating is organic or inorganic, how thick it is and how much resist the etch consumes are not public, so the resist is drawn unchanged. The oxide in the window is drawn as the pad oxide, which the page infers; the fill oxide and the deep N-well are drawn but not labelled, and the liner oxide is drawn faded. Not to scale.
:::

In its industry-generic form (SKY130's recipe is not public), the
tunnel-mask resist stays in place. The wafer is exposed to an
oxygen-based plasma, we infer, that {term}`ashes <ash>` the organic ARC in the
open windows (the resist is attacked at a similar rate but is many
times thicker).

The etch is run
to an optical-emission {term}`endpoint` plus a timed {term}`over-etch`, and
stops on the pad oxide beneath, whose thickness in a Cypress patent
that may still be in force is in the collapsed note below. This
reference describes the film only as an ARC; whether it is an organic
BARC or an inorganic dielectric ARC is discussed under *Open questions*.

:::{dropdown} From a patent shown as in force (US 8,796,098; estimated expiry 2034-02-26) — open to read
The pad oxide beneath is 10–20 nm in the Cypress patent.[^pat-04]
:::

## Step category

`TUNARCE` is an {ref}`Etch <category-etch>` step of the *ARC open*
type — the category page notes that organic BARC "opens in O₂/N₂ or
HBr/O₂" while an inorganic silicon {term}`oxynitride` ARC is opened "in
CF₄-based plasmas". It is the only ARC etch this reference describes
as a separate step. On the critical layers ({ref}`FOM <step-004>`,
{ref}`P1M <step-061>`) this reference treats any ARC open as part of
the main etch recipe on the same tool (inference from industry
practice).

## Why this step exists

An ARC exists to make the resist image good; the ARC etch exists
because the ARC then gets in the way of everything else the resist
window is for.

* **Why the ARC.** Anti-reflective coatings "help reduce standing
  waves, thin-film interference, and specular reflections"[^wiki-arc]
  from the substrate.

  At the tunnel mask the substrate is a thin pad
  oxide over silicon next to thick trench oxide over silicon. These are two
  stacks with very different reflectivity at 365 nm, side by side,
  under a resist that must define 0.410 µm windows with 0.095 µm
  clearances to the gates (tunm.1, tunm.3, tunm.4).[^pdk-periph]

  Reflectivity swings of that kind change the effective dose inside
  the resist and shift the printed {term}`CD` ({ref}`category-lithography`).
  An ARC removes the substrate from the exposure equation. A 1996
  study on an i-line 0.35 µm device is the classic demonstration that
  a new anti-reflective coating tightens CD control.[^baker-1996]
* **Why the ARC must be opened before implanting.** The thickness of
  the ARC is not public, and this reference has no checked figure for
  it.

  The channel-type implants that follow are at tens to several
  hundred keV on the published analogues
  ({ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`). An unopened organic film in their path
  would absorb part of the dose, by an amount that depends on its
  thickness and the ions' {term}`projected range` in it (inference).
  This would shift the profile of the memory transistor's channel —
  precisely the parameter these implants exist to set.
* **Why it must be opened before the oxide etch.** The (inferred)
  HF-based etch at {ref}`TUNME <step-039>` cannot penetrate an organic
  film; the window has to be clear down to the oxide.

Without `TUNARCE` the tunnel window would be printed but not usable. Its
cost is resist loss of the order of the ARC thickness plus the
over-etch, because the two films etch at similar rates (see
*Selectivity* below), and a plasma exposure of the (inferred) pad
oxide; both have to be budgeted in the resist thickness.

## How it is typically performed

*An industry-generic BARC-open recipe for a 200 mm, 130 nm-era fab
(SKY130's recipe is not public):*

* **Chamber.** A high-density or medium-density plasma etcher of the
  silicon/poly class, at a few to tens of millitorr
  (industry-typical)[^txt-02] with a modest bias — the same chamber
  types used for gate etch. Reactive-ion etching holds the wafer on an
  RF-driven electrode; "due to the mostly vertical delivery of reactive
  ions" the etch is anisotropic ({ref}`category-etch`).[^wiki-rie]
* **Chemistry.** Oxygen with nitrogen, or oxygen with a hydrogen
  halide such as HBr. Pure O₂ etches organics fast but isotropically;
  adding N₂ or HBr passivates the sidewall so that the ARC opening does
  not undercut the resist edge.

  Xu, Lill and Podlesnik (Applied
  Materials) characterised organic ARC etching "in O₂+halogen/hydrogen
  halide plasma" and showed how the sidewall chemistry controls the
  profile;[^xu-2001] Ramanathan et al. discuss the integration issues
  of {term}`DUV` resist over organic BARC, including resist loss during the
  BARC open.[^ramanathan-1998]
* **{term}`Selectivity <selectivity>`.** Organic ARC and resist are chemically similar, so
  selectivity to resist is close to 1:1 and the resist budget must
  include the ARC thickness plus over-etch (industry practice; Nojiri,
  ch. 3).[^nojiri-2015]

  Selectivity to the underlying oxide is very
  high in an oxygen plasma, because oxide has no volatile product
  without fluorine; a small HBr addition etches oxide only slowly.
* **Endpoint.** Optical emission of a carbon-containing product line
  followed by a fixed over-etch to clear the ARC in the smallest
  windows ({ref}`category-etch`).
* **Post-etch.** No strip — the resist stays on for
  {ref}`PTSI <step-037>` and {ref}`DEPI <step-038>`. The plasma leaves
  the resist surface slightly hardened, which the eventual strip must
  cope with.
* **Inorganic alternative.** If the ARC were a {term}`PECVD` silicon
  oxynitride, the open would be a CF₄/CHF₃-based dielectric etch with
  its own selectivity problem to the oxide underneath
  ({ref}`category-etch`).

## Machines typically used

* **{ref}`Silicon/poly plasma etcher <machine-plasma-etcher-silicon>`** with O₂/N₂/HBr capability, 200 mm:
  Lam {term}`TCP` 9400 series, Applied Materials DPS Centura
  ({ref}`category-etch`).
* **{ref}`Dielectric etcher <machine-plasma-etcher-dielectric>`** (Lam Exelan, Applied MxP) if the ARC is
  inorganic.
* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`** — some fabs open thin organic ARCs on relaxed
  layers with a timed, isotropic ash rather than a directional etch
  ({ref}`category-strip`).
* **Optical emission endpoint** on the etcher; **{ref}`CD-SEM <machine-cd-sem-overlay-metrology>`** for the
  post-etch window.

## Machines likely used at SkyWater

* **Applied Materials DPS II**
  - *SkyWater says:* lists "AMAT DPSII, HBR, Cl2,
    NF3, CF4, CHF3, O2 – gate, trench, W/WN".[^skw-01]
  - *Tool exists:* **strong** — the HBr/O₂ gas set
    is exactly an organic-ARC-open chemistry.
  - *Runs this step:* **inference**, for its assignment to `TUNARCE`.
* **Lam 9400 TCP**
  - *SkyWater says:* lists "Lam 9400 TCP, poly/nitride, HBr, CF4,
    SF6, O2".[^skw-01]
  - *Tool exists:* strong — also capable of O₂/HBr ARC opens and, with
    CF₄, of an inorganic ARC open.
  - *Runs this step:* inference.

  A university clean-room describes the 9400 as "a Transformer Coupled
  Plasma (TCP) etcher" with a gas list including oxygen.[^snf-9400]
* **GaSonics PEP / Iridia / Mattson Aspen II ashers**
  - *SkyWater says:* lists them ("N2, O2",
    "N2, O2, H2, CF4, NH3, H2/N2").[^skw-01]
  - *Tool exists:* strong for existence — the isotropic alternative.
  - *Runs this step:* weak.

## Resources required

* **{ref}`Oxygen <material-process-gases>`, nitrogen, {ref}`hydrogen bromide <material-etch-gases>`, helium/argon** process gases;
  the DPS II and 9400 gas sets are public.[^skw-01] SkyWater's filings name
  Air Products and Praxair (2021 S-1) and Linde and Airgas (fiscal 2023
  10-K) as gas suppliers.[^sec-01][^sec-02]
* **CF₄/CHF₃** only if the {ref}`ARC <material-lithography-materials>` is inorganic.[^skw-01]
* **Helium backside cooling**, {ref}`chamber consumables <material-hardware-consumables>` (electrostatic
  chuck, liners, focus ring).
* **Endpoint optics** and their windows.

## Related steps and cross-references

* Previous: {ref}`TUNM <step-035>` (the resist and ARC being opened).
* Next: {ref}`PTSI <step-037>` and {ref}`DEPI <step-038>` implant
  through the cleared windows; {ref}`TUNME <step-039>` etches the pad
  oxide in them.
* Same category: the ARC question for the other mask layers is
  discussed on {ref}`FOM <step-004>`.
* Category page: {ref}`Etch <category-etch>`; the ARC itself belongs
  to {ref}`category-lithography`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

:::{dropdown} 1 family in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 8,796,098 B1 <patent-gp51229009>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — AMAT DPS II and Lam 9400 TCP
  gas sets; ashers.[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — tunm.1, tunm.3 and tunm.4, the
  dimensions the ARC protects.[^pdk-periph]
* [Stanford Nanofabrication Facility, *Lam Research TCP 9400*](<https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>) — the
  reactor class and its gases.[^snf-9400]

:::{dropdown} From a patent shown as in force (US 8,796,098; estimated expiry 2034-02-26) — open to read
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — the
  10–20 nm pad oxide on which the ARC etch stops.[^pat-04]
:::

### High-level understanding

* [Wikipedia, *Anti-reflective coating*](<https://en.wikipedia.org/wiki/Anti-reflective_coating>) — ARCs in photolithography,
  BARC.[^wiki-arc]
* [Wikipedia, *Reactive-ion etching*](<https://en.wikipedia.org/wiki/Reactive-ion_etching>) — the plasma etch
  basics.[^wiki-rie]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) —
  plasma etching and resist processing.[^txt-02]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on photoresists and
  on modeling and thin film effects.[^levinson-2005]

### Deep dive

* [Xu, Lill and Podlesnik (Applied Materials), *JVST A* 2001](<https://doi.org/10.1116/1.1412655>) —
  wall-dependent etching of organic ARC in O₂ + halogen / hydrogen
  halide plasmas.[^xu-2001]
* [Ramanathan et al., SPIE 1998](<https://doi.org/10.1117/12.312473>) — etch integration issues with DUV
  resist over organic BARC.[^ramanathan-1998]
* [Baker and Capsuto, SPIE 1996](<https://doi.org/10.1117/12.241869>) — CD control for an i-line 0.35 µm
  device using a new anti-reflective coating.[^baker-1996]
* [Linliu, Kuo and Huang, SPIE 2000](<https://doi.org/10.1117/12.389087>) — a polymeric ARC for better CD
  uniformity.[^linliu-2000]
* [Coburn and Winters, *J. Appl. Phys.* 1979](<https://doi.org/10.1063/1.326355>) — how ion and electron
  bombardment enhances gas–surface reactions, and its implications for
  plasma etching.[^coburn-1979]
* [Steinbrüchel, *Appl. Phys. Lett.* 1989](<https://doi.org/10.1063/1.102336>) — the energy dependence of
  ion-enhanced etch yields, governing the low-bias ARC open.[^steinbruchel-1989]
* [Flamm and Donnelly, *Plasma Chem. Plasma Process.* 1981](<https://doi.org/10.1007/BF00565992>) — the design
  of plasma etchants, including oxygen-based organic etches.[^flamm-1981]
* [Nojiri, *Dry Etching Technology for Semiconductors*](<https://doi.org/10.1007/978-3-319-10295-5>) — selectivity,
  endpoint and the practical recipe structure.[^nojiri-2015]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — the
  reflectivity and standing-wave theory behind the ARC.[^mack-2007]

## Open questions

* **ARC type.** Whether the tunnel-mask ARC is an organic BARC or an
  inorganic dielectric ARC is not public; the O₂/HBr reading is an
  inference from the tool gas sets and from industry practice on
  i-line layers.
* **Why an ARC here.** Why a relaxed implant layer would carry an ARC,
  when this reference describes no ARC etch at the other implant
  masks, is an open question; the reflectivity contrast of the
  pad-oxide/trench-oxide substrate is our best reading.
* **Which tool and method.** Which etcher runs the step, and whether
  the open is directional or a timed ash, is inferred, not stated.
* **Thickness and timing.** ARC thickness, etch time and over-etch are
  not public.

<!-- footnotes -->

[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
    Shown as in force; estimated expiry 2034-02-26 (estimate from public
    records, not legal advice).
[^wiki-arc]: Wikipedia, *Anti-reflective coating*.
    <https://en.wikipedia.org/wiki/Anti-reflective_coating>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^baker-1996]: D. C. Baker and E. S. Capsuto, "Critical dimension
    control for i-line 0.35-μm device using a new antireflective
    coating", *Proc. SPIE* **2724**, Advances in Resist Technology and
    Processing XIII, 710 (1996). <https://doi.org/10.1117/12.241869>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^xu-2001]: S. Xu, T. Lill and D. Podlesnik, "Wall-dependent etching
    characteristics of organic antireflection coating in
    O₂+halogen/hydrogen halide plasma", *Journal of Vacuum Science &
    Technology A* **19**(6), 2893–2899 (2001).
    <https://doi.org/10.1116/1.1412655>
[^ramanathan-1998]: V. Ramanathan, S. Chen, K. Lai, M. R. Brongo and
    N. Samarakone, "Etch integration issues in the development of deep
    submicron contacts utilizing DUV resist and organic BARC", *Proc.
    SPIE* **3333**, Advances in Resist Technology and Processing XV,
    909 (1998). <https://doi.org/10.1117/12.312473>
[^nojiri-2015]: K. Nojiri, *Dry Etching Technology for Semiconductors*,
    Springer, 2015. <https://doi.org/10.1007/978-3-319-10295-5>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^snf-9400]: Stanford Nanofabrication Facility, *Lam Research TCP 9400
    Poly Etcher (lampoly)*, equipment page.
    <https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^linliu-2000]: K. Linliu, M.-R. Kuo and Y.-R. Huang, "Novel polymeric
    antireflective coating (PARC) for better uniformity control of
    critical dimension", *Proc. SPIE* **4000**, Optical
    Microlithography XIII, 915 (2000). <https://doi.org/10.1117/12.389087>
[^coburn-1979]: J. W. Coburn and H. F. Winters, "Ion- and
    electron-assisted gas-surface chemistry — An important effect in
    plasma etching", *Journal of Applied Physics* **50**(5), 3189–3196
    (1979). <https://doi.org/10.1063/1.326355>
[^steinbruchel-1989]: C. Steinbrüchel, "Universal energy dependence of
    physical and ion-enhanced chemical etch yields at low ion energy",
    *Applied Physics Letters* **55**(19), 1960–1962 (1989).
    <https://doi.org/10.1063/1.102336>
[^flamm-1981]: D. L. Flamm and V. M. Donnelly, "The design of plasma
    etchants", *Plasma Chemistry and Plasma Processing* **1**(4),
    317–363 (1981). <https://doi.org/10.1007/BF00565992>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007,
    ISBN 978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
    (companion site <https://www.lithoguru.com/textbook/>)
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
