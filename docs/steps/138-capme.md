(step-138)=
# Step 138 — CAPME: Capacitor mask etch

| | |
|---|---|
| **Step number** | 138 of 171[^steps-sheet] |
| **Step code** | `CAPME` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | BEOL — MiM capacitors, metal 3–5, via 3–4 |
| **Previous step** | {ref}`CAPM <step-137>` |
| **Next step** | {ref}`MM3 <step-139>` |

## What this step is

`CAPME` etches the top plates of the first {term}`MiM capacitor`. Through
the resist islands of {ref}`CAPM <step-137>` a plasma removes the
blanket plate film of {ref}`CAPTIW1 <step-136>` — TiW, as assumed
there, of the order of 0.1 µm on our reading of the PDK's top-plate
sheet resistance — and stops on, or a little way into, the thin
capacitor dielectric of {ref}`CAPILD <step-135>`,
leaving TiW only where the layout draws `capm`, "MiM capacitor plate
over metal 3".[^pdk-06] The resist is then stripped; this reference
treats the strip and post-etch clean as part of this step.

What makes this etch unlike any other in the process is what lies
under the film being removed. Beneath the TiW is a dielectric some
20–30 nm thick (our estimate at {ref}`CAPILD <step-135>`), and beneath
*that* is the metal-3 stack, whose cap is a refractory film of unknown
identity: 300 Å of TiW on the 2013 Cypress description of this fab's
S8TNV-5R, or 500 Å of TiN over 90 Å of titanium on the stack qualified
in 2013–2014, the February 2014 S8P qualification having excluded only
"top metal layers" and metal 3 not being one of them on this
reference's reading[^cyp-qtp-113005][^cyp-qtp-123907]
({ref}`overview-metal-cap`). It is not yet patterned and must be etched, with its dielectric, at
{ref}`MM3E <step-140>`. If `CAPME` etched through the dielectric it
would begin to consume the bottom plate's cap everywhere outside the
capacitors, and the capacitor's edge would be a dielectric sidewall
exposed to plasma. The etch therefore has to remove a refractory
metal with very high {term}`selectivity` to a very thin dielectric —
for a TiW plate on an oxynitride, as assumed here (see
{ref}`CAPTIW1 <step-136>` and {ref}`CAPILD <step-135>`), a
fluorine-etchable metal over a fluorine-etchable dielectric — and to
stop within a few nanometres. A Texas Instruments patent that may still
be in force states the target for exactly this operation — the
dielectric thickness it assumes, how little of it the etch may remove
and the gas scheme it uses; those sentences are in the collapsed note
below. The other two patents take the alternative, in which the
dielectric is patterned with the plate. The Philips patent etches its
~3000 Å TiN top electrode and the insulator in a multi-rate etch,
slowing near the TiN/insulator interface and stopping close to the TiN
ARC on the bottom electrode;[^pat-mim-philips] the Newport Fab process
etches the TiN top plate and the nitride dielectric together and then
protects the stack's sidewall with an oxide spacer.[^pat-mim-newportfab]

:::{dropdown} From a patent shown as in force (US 8,110,414; estimated expiry 2030-01-02) — open to read
A Texas Instruments patent on the same operation for a TiN top
electrode states the target: a silicon-based dielectric "<1,000 Å" thick
(typically 150–400 Å), and a dry etch of the top electrode that removes
no more than 100 Å (typically under 50 Å) of it, using a chlorine- or
bromine-based first halogen gas, a fluorocarbon (CHF₃, CH₂F₂ or CF₄) as
the fluorine-bearing second halogen gas, and a noble-gas
carrier.[^pat-mim-ti-etch]
:::

Which of the two SKY130 follows — stop on the dielectric, or cut
through it — is not public, and the public numbers bear on it in two
ways. The PDK's `cap_mim` cross-section draws the thin "CAPILD" layer
with exactly the lateral extent of the "CAPM" plate above it, over a
much wider "M3 (plate 1)";[^pdk-07] read literally, that shows the
dielectric removed outside the plate, but the drawing is a schematic
and cannot show a few nanometres of residual film.

Against the literal reading stands the selectivity available, so far as
it is published. For a TiW plate the only figure this reference has
found is Liu and Kuo's: etching TiW in CF₄-based plasmas they report
that "an etch selectivity of greater than 2 was achieved under the low
ion bombardment condition" against plasma-enhanced CVD silicon
nitride.[^liu-2007-tiw] That is a floor they reached, not a maximum they
measured, and the abstract gives no upper figure. Taken at that floor it
is an illustration rather than a prediction: an etch clearing 0.1 µm of
plate at a selectivity of 2 would cost some 50 nm of dielectric, more
than the whole capacitor dielectric on this reference's estimate (our
arithmetic). What can be said is that no published TiW figure shows the
margin such an etch needs. The Texas Instruments patent, whose top
electrode is TiN and whose dielectric is silicon-based, reports a
selectivity and a worked example that do have that margin; the figures,
the chemistry and the tool are in the collapsed note below. That is a
published stop-on-dielectric etch of a MiM top plate over an aluminium
bottom electrode, on a dielectric ten times thinner than the plate — the
operation this step performs.

:::{dropdown} From a patent shown as in force (US 8,110,414; estimated expiry 2030-01-02) — open to read
The Texas Instruments patent reports that "an etch rate selectivity of
the TiN to the silicon comprising dielectric layer is at least 8:1", and
its worked Example 1 does much better still. There a 1 800 Å TiN top
electrode over "a 250 A thick dielectric stack comprising silicon
oxide/SiON/silicon oxide" on an aluminium bottom electrode was etched on
an Applied Materials DPS with "Cl2:90 sccm, Ar:10 sccm, CHF3:10 sccm" at
15 mTorr, 25 W bias and an 800 W source; "the TiN:oxide selectivity was
found to be 210:1 and the TiN etch rate was found to be about
1,800 A/min", and "a 365 nm wavelength … was used to allow the TiN etch
to endpoint on the thin silicon oxide layer".[^pat-mim-ti-etch]
:::

The two sets of numbers are not directly comparable, and this page does
not treat them as though they were: Liu and Kuo etch **TiW** against
**silicon nitride** in a **CF₄-based** plasma,[^liu-2007-tiw] while the
Texas Instruments figures are for a different film, a different
dielectric and a different chemistry — which, the collapsed note above
sets out. What the comparison supports is the chemistry: this reference
reads the SKY130 recipe as a chlorine-majority one with a small
fluorine addition (inference; Liu and Kuo found both fluorine and
chlorine effective etchants on TiW,[^liu-2007-tiw] and the published
stop-on-dielectric demonstration is the one in the collapsed note
above). It is a consideration that {ref}`CAPTIW1 <step-136>` weighs in
choosing between a TiW and a TiN plate, not a settled argument about the
plate material.

What the etch would have left to stop on if it did cut through depends
on the unresolved metal-3 cap. If the cap is TiW — the same material as
the plate on this reference's reading of {ref}`CAPTIW1 <step-136>` — a
through-etch would have no selective layer left beneath the dielectric.
If it is the Ti/TiN of the stack qualified in 2014, plate and cap are
different films and the through-etch has a stop: that is exactly the
Philips process, in which "the etch is controlled to stop in the TiN
ARC film that coats the M5 layer and forms the bottom
electrode".[^pat-mim-philips][^cyp-qtp-123907] So the choice between
the two `CAPME` variants turns partly on a question about the metal-3
cap that the public record does not settle
({ref}`overview-metal-cap`). This reference describes the
stop-on-dielectric version as the more plausible (inference), on the
selectivity argument above and on the same-material case, and records
the other under *Open questions*.
Either way, after this step the wafer carries TiW islands a fraction
of a micrometre high over blanket metal 3, and the
{ref}`MM3 <step-139>` resist is coated over that topography.

## Step category

`CAPME` is an {ref}`Etch <category-etch>` step of the *refractory
metal, fluorine-chemistry* class — the category page's "Ti:W and TiN"
entry. Tungsten etches in fluorine plasmas as WF₆ (Turban, Coulon and
Mutsukura's mechanistic study of SF₆ etching of tungsten[^turban-1989]
and Petri, Henry and Sadeghi's[^petri-1992]), so fluorine-based
chemistries attack the tungsten-rich TiW readily; Liu and Kuo,
etching TiW in CF₄/O₂, CF₄/Cl₂ and CF₄/HCl plasmas, found both
fluorine and chlorine effective etchants, with the rate set by the
etchant concentration and the ion energy. The only selectivity they
report against plasma-enhanced CVD silicon nitride is "greater than 2 …
under the low ion bombardment condition" — a floor, with no upper figure
given[^liu-2007-tiw] — where the Texas Instruments patent, which may
still be in force, reports a much higher figure for a different film,
dielectric and chemistry (collapsed notes above), so that the two are
not directly comparable; and at that floor an etch clearing 0.1 µm of
TiW would consume more dielectric than the capacitor has (our
arithmetic). Chlorine also etches both metals — Fischl and Hess studied
tungsten in chlorine discharges[^fischl-1987] — and a majority chlorine
flow with a small fluorocarbon addition is, on our reading, a blend
chosen so that the metal etches by chlorine while the oxide-like
dielectric, which chlorine alone barely etches, is attacked only by the
small fluorine fraction. What is specific
to this instance within the flow is the stop: the other refractory
etches (the TiN local interconnect of {ref}`LI1ME <step-103>`, the
caps opened at the start of every aluminium etch) land on thick
oxide or continue into aluminium; this one must land on a film thinner
than its own {term}`over-etch` would normally consume.

## Why this step exists

* **It makes the plates.** The etch turns the `capm` resist image into
  discrete top electrodes; their area, with the dielectric's
  thickness, is the capacitance the PDK models as 2 fF/µm² plus
  0.19 fF/µm of periphery.[^pdk-07] The etch bias — how much the
  plate shrinks or grows relative to the drawn shape — is folded
  into those two numbers.
* **It must not open the dielectric.** Outside the plates the
  dielectric is all that separates the plasma from the metal-3 cap.
  Because fluorine etches both candidate caps — TiW as WF₆ and TiF₄,
  TiN as TiF₄ — punching through would thin the cap of every metal-3
  line (the film {ref}`VIM3E <step-145>` later
  stops on) and expose aluminium to a fluorine plasma, which forms
  involatile AlF₃ rather than etching it[^hess-1982] — a residue the
  {ref}`MM3E <step-140>` chlorine etch would then have to break
  through. The dielectric loss the Texas Instruments patent allows (the
  collapsed notes above) is the scale of the margin.
* **It must not damage the dielectric under the plates.** Ion
  bombardment and {term}`charging <plasma charging>` during the over-etch reach the capacitor
  through its top plate: the plate is a metal island on a thin
  insulator over a large conductor, the geometry that collects
  plasma charge. Hwang and Giapis explained pattern-dependent
  charging in high-density plasmas,[^hwang-1997] Fang and McVittie
  the thin-dielectric damage it causes,[^fang-1992] and Cheung the
  same charging mechanism during plasma-enhanced dielectric
  deposition, as at {ref}`NILD5 <step-141>` later;[^cheung-2000] a
  MiM dielectric that has been charged shows higher leakage and a
  shifted {math}`C(V)`. We infer that the final stage of the etch is
  run at low bias to limit this; Nojiri treats charging damage in dry
  etching.[^nojiri-2015]
* **Clean plate edges.** Residue or a re-entrant foot at the plate
  edge becomes a fringing-field and leakage site and a place where
  the {ref}`NILD5 <step-141>` fill can void; the two-rate etch of
  the Philips patent[^pat-mim-philips] and the spacer of the Newport
  Fab patent[^pat-mim-newportfab] both address the edge.

Without `CAPME` the top-plate metal would remain a sheet and be lost,
with the dielectric, at {ref}`MM3E <step-140>`.

## How it is typically performed

An industry-generic MiM top-plate etch for a 200 mm aluminium back
end (SKY130's recipe is not public):

1. **Chamber.** A single-wafer metal etcher with a high-density
   source and independent bias — Lam's {term}`TCP` 9600 or 2300
   family,[^pat-tcp-lam][^lam-10k] Applied Materials' DPS[^pat-dps-amat]
   — with helium backside cooling and optical-emission
   {term}`endpoint`; SkyWater's metal etchers are both qualified for
   "TiW".[^skw-01]
2. **BARC open** (if a BARC was used at {ref}`CAPM <step-137>`): a
   short O₂/N₂ step.
3. **Main etch.** A halogen chemistry — Cl₂ (or BCl₃) with a small
   fluorine-bearing addition such as CF₄, CHF₃ or SF₆, in argon
   (industry practice for a refractory metal over a thin dielectric;
   Nojiri sets out the regime[^nojiri-2015]) — at moderate bias; the
   Texas Instruments patent's own scheme is in the collapsed notes
   above; for a ~0.1 µm
   film the main etch is short (our estimate), and Turban et al. and
   Liu and Kuo give the dependence of the rate on chemistry, power
   and pressure.[^turban-1989][^liu-2007-tiw] Flamm and Donnelly and
   Winters and Coburn set out the surface chemistry that makes the
   fluorine-to-oxide rate low without ion assistance.[^flamm-1981][^winters-1992]
4. **Endpoint and over-etch.** Optical emission on a tungsten or
   fluorine line as the TiW clears; the open area is large (the
   plates are a small fraction of the wafer), so the signal is strong
   — the reverse of Wodecki's low-open-area via problem.[^wodecki-1999]
   The over-etch is short and at reduced bias, sized to clear TiW
   stringers while removing at most a few nanometres of the dielectric
   (the target in the collapsed notes above).
5. **Strip and clean.** Downstream O₂/N₂ {term}`ash` — the "Gasonic
   PEP", Iridia or Mattson class in SkyWater's list[^skw-01] — then a
   solvent or semi-aqueous clean (SkyWater lists "EKS265, EKC270
   solvents" under "Batch Rotational"[^skw-01]) that removes fluorocarbon and
   metal-fluoride residue without attacking TiW or the dielectric;
   no HF and no peroxide (H₂O₂ etches TiW — the wet route Danzl and
   McLaurin describe for stripping a TiW cap[^danzl-1997] — so it is
   excluded here by inference).
6. **Metrology.** Plate {term}`CD` by {term}`CD-SEM`; remaining
   dielectric thickness outside the plates by ellipsometry on
   monitors; particle and residue inspection; capacitance, leakage,
   breakdown and {math}`C(V)` on test structures at {term}`e-test`
   against the PDK's `CMIMA`/`CMIMP` limits.[^pdk-07] The published
   SKY130 {term}`test tile` has a "Large MiM capacitor, CAPM on M3, 11
   plates, each 40x40" with "Total expected capacitance 35.5 pF", a
   "Periphery-intensive" one of 72 plates of 2 × 35 µm (11.1 pF) and an
   "Area-intensive" one of 5 plates of 35 × 35 µm (12.4 pF), "CAPM
   linewidth" and "CAPM sheet rho" lines, and "M3-M3" and "CAPM-CAPM
   serp/comb" structures.[^raw-data-testtile-pads] Solving the first
   two expected values for an area and a perimeter term gives about
   2.0 fF/µm² and 0.19 fF/µm, which reproduces the third and equals the
   PDK's nominal `CMIMA` and `CMIMP`[^pdk-07] (our arithmetic; the
   values are expected design values, not measurements). The
   published C–V measurements of the three structures, 33.26 pF,
   10.37 pF and 11.57 pF at 0 V, are 6–7 % below those expected values
   (our extraction; see {ref}`CAPILD <step-135>`).[^raw-data-passives]

## Machines typically used

* **{ref}`High-density metal etcher <machine-plasma-etcher-metal>`**, 200 mm: Lam TCP 9600 / 2300
  Versys,[^lam-10k] Applied Materials Centura DPS,[^pat-dps-amat]
  TEL Unity ({ref}`category-etch`).
* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`**; **{ref}`solvent wet bench <machine-wet-bench>`**.
* **{ref}`CD-SEM <machine-cd-sem-overlay-metrology>`**, **{ref}`ellipsometer <machine-film-thickness-metrology>`**, **{ref}`e-test <machine-parametric-tester>`** for capacitor structures.

## Machines likely used at SkyWater

* **Lam 9600 or Lam 2300 Versys.** SkyWater lists "Lam 9600, Al, TiW,
  TiN, Pt" and "Lam 2300 Versys, Al, TiW, TiN, Nb, Pt".[^skw-01]
  Strength: **strong** for the tools and for TiW as a qualified
  material; which runs this step is not public.
* **Strip — "Gasonic PEP", Iridia, Mattson Aspen II; clean — batch
  rotational tools with "EKS265, EKC270 solvents".**[^skw-01]
  Strength: strong for existence; assignment is an inference.

## Resources required

* **{ref}`Cl₂ <material-etch-gases>`** (or **BCl₃**, **Br₂** or **HBr**) with a small flow of a
  fluorine-bearing gas (**CF₄**, **CHF₃**, **CH₂F₂** or **SF₆**) in
  **{ref}`Ar <material-process-gases>`**, **He** or **N₂** for the etch (industry
  practice[^nojiri-2015] and the collapsed notes above; SkyWater lists
  no gases
  for its metal etchers, but names Cl₂, HBr, CF₄, CHF₃ and SF₆ on its
  poly/silicon etchers[^skw-01]); **He** for backside cooling. The
  gas set is the one given at {ref}`CAP2ME <step-153>`, since the PDK
  calls the two capacitor constructions identical.[^pdk-07]
* **O₂/N₂** for the ash;[^skw-01] **amine or semi-aqueous solvent** ({ref}`wet chemicals <material-wet-chemicals>`)
  and {ref}`DI water <material-ultrapure-water>` for the clean.[^skw-01]
* **{ref}`Chamber consumables <material-hardware-consumables>`** and **{ref}`monitor wafers <material-substrates>`** carrying the plate
  film over the capacitor dielectric for rate and selectivity checks.

## Related steps and cross-references

* Previous: {ref}`CAPM <step-137>` (the mask). Next:
  {ref}`MM3 <step-139>` (the metal-3 mask printed over the plates),
  then {ref}`MM3E <step-140>` (which removes the remaining
  dielectric and the metal outside the wiring).
* The films it etches and stops on: {ref}`CAPTIW1 <step-136>`,
  {ref}`CAPILD <step-135>`; the metal beneath: {ref}`WTIAL3 <step-134>`.
* The via etch that later lands on the plate: {ref}`VIM3E <step-145>`.
* The other refractory-metal etches: {ref}`LI1ME <step-103>`; the
  second capacitor's etch: {ref}`CAP2ME <step-153>`.
* Category page: {ref}`Etch <category-etch>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,005,102 A <patent-gp23452232>` — Multilayer electrodes for integrated circuit capacitors (1989)
* {ref}`US 4,948,458 A <patent-gp23554962>` — Method and apparatus for producing magnetically-coupled planar plasma (1989)
* {ref}`US 5,170,242 A <patent-gp27034223>` — Reaction barrier for a multilayer structure in an integrated circuit (1991)
* {ref}`US 5,540,824 A <patent-gp23061269>` — Plasma reactor with multi-section RF coil and isolated conducting lid (1994)
* {ref}`US 6,430,028 B1 <patent-gp24897586>` — Method for fabrication of an MIM capacitor and related structure (2000)
* {ref}`US 6,717,193 B2 <patent-gp25521092>` — Metal-insulator-metal (MIM) capacitor structure and methods of fabricating same (2001)

:::{dropdown} 2 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 7,166,902 B1 <patent-gp37663627>` — unknown
* {ref}`US 8,110,414 B2 <patent-gp43029761>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, *Device Details* — MiM construction, `CMIMA`,
  `CMIMP`, `RSCAPM`; the `cap_mim` cross-section with "CAPILD" drawn
  exactly under "CAPM" on a wider "M3 (plate 1)".[^pdk-07]
* SkyWater PDK, *Layers Reference* — `capm` 89:44.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `CAPMCD` 2 µm,
  `CAPMCDSP` 0.84 µm.[^pdk-03]
* Cypress, QTP 113005 and QTP 123907 — the two candidate caps of the
  metal beneath the
  dielectric.[^cyp-qtp-113005][^cyp-qtp-123907]
* SkyWater, *Facilities & Capabilities* — Lam 9600 and 2300 Versys
  with TiW; ashers; solvents.[^skw-01]
* Lam Research, Form 10-K (2003) — the 9600 and 2300 lines.[^lam-10k]
* SKY130 raw-data repository, test-tile pad documentation — the MiM
  capacitor, plate linewidth, sheet-resistance and serpentine/comb
  structures of the published test tile.[^raw-data-testtile-pads]
* SKY130 raw-data repository, measured data — C–V sweeps of those
  capacitors; the values quoted here are our
  extraction.[^raw-data-passives]

:::{dropdown} From a patent shown as in force (US 8,110,414; estimated expiry 2030-01-02) — open to read
* Cathey et al. (TI), US 8,110,414 — a TiN top-electrode etch that
  removes no more than 100 Å of the dielectric.[^pat-mim-ti-etch]
:::

### High-level understanding

* Wikipedia, *Reactive-ion etching*, *Dry etching*.[^wiki-rie][^wiki-dry-etch]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — refractory
  metal etching in the back end.[^txt-05]
* Nojiri, *Dry Etching Technology for Semiconductors* — metal etch
  chemistry, endpoint and charging damage.[^nojiri-2015]

### Deep dive

* Turban, Coulon and Mutsukura, *Thin Solid Films* 1989 — the
  mechanism of SF₆ reactive ion etching of tungsten.[^turban-1989]
* Petri, Henry and Sadeghi, *J. Appl. Phys.* 1992 — tungsten etching
  mechanisms in SF₆ plasma.[^petri-1992]
* Liu and Kuo, *J. Electrochem. Soc.* 2007 — reactive ion etching of
  titanium–tungsten films.[^liu-2007-tiw]
* Fischl and Hess, *J. Electrochem. Soc.* 1987 — tungsten in chlorine
  discharges, the other halogen.[^fischl-1987]
* Flamm and Donnelly, 1981, and Winters and Coburn, 1992 — the
  surface chemistry behind metal-to-dielectric selectivity.[^flamm-1981][^winters-1992]
* Hwang and Giapis, *JVST B* 1997; Fang and McVittie, *IEEE EDL*
  1992; Cheung, P2ID 2000 — plasma charging and thin-dielectric
  damage.[^hwang-1997][^fang-1992][^cheung-2000]
* Wodecki, SPIE 1999 — emission endpoint and open area.[^wodecki-1999]
* Danzl and McLaurin, IEMT 1997 — peroxide etching of TiW, the wet
  chemistry this etch's clean must avoid.[^danzl-1997]
* Olewine and Saiz (Philips), US 6,717,193 — a multi-rate etch of the
  top electrode and insulator that slows near their interface and
  stops close to the bottom electrode's TiN ARC.[^pat-mim-philips]
* Kar-Roy and Racanelli (Newport Fab), US 6,430,028 — etching plate
  and dielectric together and spacering the edge.[^pat-mim-newportfab]
* Ogle (Lam Research), US 4,948,458, and Yin et al. (Applied
  Materials), US 5,540,824 — the two high-density metal-etch
  sources.[^pat-tcp-lam][^pat-dps-amat]

:::{dropdown} From a patent shown as in force (US 8,110,414; estimated expiry 2030-01-02) — open to read
* Hess, *Plasma Chem. Plasma Process.* 1982 — why fluorine does not
  etch aluminium, the hazard of punching through (paywalled beyond
  the title; the TI patent states the same mechanism in publicly
  readable text — "fluorine … cannot generally damage the underlying
  aluminum comprising layer by forming non-volatile aluminum
  fluoride").[^hess-1982][^pat-mim-ti-etch]
* Cathey et al. (TI), US 8,110,414 — selective plasma etch of MiM
  top electrodes; its Example 1 gives a complete Cl₂/Ar/CHF₃ recipe and
  a 210:1 TiN-to-oxide selectivity on an aluminium bottom
  electrode.[^pat-mim-ti-etch]
:::

## Open questions

* Whether `CAPME` stops on the capacitor dielectric or etches through it (so
  that the dielectric is patterned with the plate) is not public. The
  PDK's schematic cross-section draws the dielectric only under the
  plate,[^pdk-07] which read literally favours the latter; we describe
  the former because no published TiW-to-dielectric selectivity shows
  the margin such an etch needs — the only figure found is a floor of
  "greater than 2"[^liu-2007-tiw] — and because, if the metal-3 cap is
  the same TiW as the plate, a through-etch has no selective stop
  (inference). A
  rate-controlled stop of the Philips kind[^pat-mim-philips] would be
  possible, and would be much easier if the metal-3 cap were the TiN of
  the stack qualified in 2014;[^cyp-qtp-123907] see
  {ref}`overview-metal-cap`.
* Which refractory film caps metal 3 is itself not public, and this
  page's central conclusion depends on it
  ({ref}`overview-metal-cap`).
* The chemistry, endpoint, over-etch and dielectric loss of the etch
  are not public.
* Whether the plate edge receives a spacer or other edge treatment,
  as in the Newport Fab patent,[^pat-mim-newportfab] is not stated
  publicly for SKY130; this reference describes none.
* Which of the two listed Lam metal etchers runs the step is not
  public.[^skw-01]
* This page treats the resist strip and clean as part of the etch.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (MiM capacitors),
    SkyWater SKY130 PDK documentation, and the `cap_mim` cross-section
    drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/cap_mim/cross-section-cap_mim.svg>
[^cyp-qtp-113005]: Cypress Semiconductor, *Product Qualification
    Plan, QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8
    Technology, CMI (Fab 4)*, document 001-85611 Rev. *A, January
    2013 (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^lam-10k]: Lam Research Corporation, Form 10-K for the fiscal year
    ended 2003-06-29 (product line: TCP 9400PTX/DFM, 2300, Exelan).
    <https://www.sec.gov/Archives/edgar/data/707549/000089161803004913/f93126e10vk.htm>
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^wiki-dry-etch]: Wikipedia, *Dry etching*.
    <https://en.wikipedia.org/wiki/Dry_etching>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^nojiri-2015]: K. Nojiri, *Dry Etching Technology for Semiconductors*,
    Springer, 2015. <https://doi.org/10.1007/978-3-319-10295-5>
[^turban-1989]: G. Turban, J. F. Coulon and N. Mutsukura, "A
    mechanistic study of SF₆ reactive ion etching of tungsten", *Thin
    Solid Films* **176**(2), 289–308 (1989).
    <https://doi.org/10.1016/0040-6090(89)90102-8>
[^petri-1992]: R. Petri, D. Henry and N. Sadeghi, "Tungsten etching
    mechanisms in low-pressure SF₆ plasma", *Journal of Applied Physics*
    **72**(7), 2644–2651 (1992). <https://doi.org/10.1063/1.351565>
[^liu-2007-tiw]: G. Liu and Y. Kuo, "Reactive Ion Etching of Titanium
    Tungsten Thin Films", *Journal of The Electrochemical Society*
    **154**(7), H653 (2007). <https://doi.org/10.1149/1.2737631>
[^fischl-1987]: D. S. Fischl and D. W. Hess, "Plasma-Enhanced Etching
    of Tungsten and Tungsten Silicide in Chlorine-Containing
    Discharges", *Journal of The Electrochemical Society* **134**(9),
    2265–2269 (1987). <https://doi.org/10.1149/1.2100868>
[^flamm-1981]: D. L. Flamm and V. M. Donnelly, "The design of plasma
    etchants", *Plasma Chemistry and Plasma Processing* **1**(4),
    317–363 (1981). <https://doi.org/10.1007/BF00565992>
[^winters-1992]: H. F. Winters and J. W. Coburn, "Surface science
    aspects of etching reactions", *Surface Science Reports*
    **14**(4–6), 162–269 (1992).
    <https://doi.org/10.1016/0167-5729(92)90009-Z>
[^hess-1982]: D. W. Hess, "Plasma etch chemistry of aluminum and
    aluminum alloy films", *Plasma Chemistry and Plasma Processing*
    **2**(2), 141–155 (1982). <https://doi.org/10.1007/BF00633130>
[^hwang-1997]: G. S. Hwang and K. P. Giapis, "On the origin of the
    notching effect during etching in uniform high density plasmas",
    *Journal of Vacuum Science & Technology B* **15**(1), 70–87 (1997).
    <https://doi.org/10.1116/1.589258>
[^fang-1992]: S. Fang and J. P. McVittie, "Thin-oxide damage from gate
    charging during plasma processing", *IEEE Electron Device Letters*
    **13**(5), 288–290 (1992). <https://doi.org/10.1109/55.145056>
[^cheung-2000]: K. P. Cheung, "On the mechanism of plasma enhanced
    dielectric deposition charging damage", *Proc. 2000 5th
    International Symposium on Plasma Process-Induced Damage (P2ID)*,
    pp. 161–163. <https://doi.org/10.1109/PPID.2000.870658>
[^wodecki-1999]: N. Wodecki, "Low open area multilayered dielectric
    film etch endpoint detection using EndPoint Plus", *Proc. SPIE*
    **3882**, Process, Equipment, and Materials Control in Integrated
    Circuit Manufacturing V, 231 (1999).
    <https://doi.org/10.1117/12.361313>
[^danzl-1997]: R. B. Danzl and A. McLaurin, "The use of concentrated
    hydrogen peroxide for the removal of a TiW ARC from aluminum bond
    pads", *Proc. Twenty-First IEEE/CPMT International Electronics
    Manufacturing Technology Symposium (IEMT 1997)*, pp. 99–104.
    <https://doi.org/10.1109/IEMT.1997.626884>
[^pat-mim-ti-etch]: M. O. Cathey Jr., P. Mahalingam, W. Tian,
    D. C. Guiling, X. Chen, B. Hu and S. Chevacharoenkul (Texas
    Instruments), *Forming integrated circuit devices with
    metal-insulator-metal capacitors using selective etch of top
    electrodes*, US 8,110,414 B2, filed 2009-04-30, granted 2012-02-07.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8110414>
    Shown as in force; estimated expiry 2030-01-02 (estimate from public
    records, not legal advice).
[^pat-mim-philips]: M. C. Olewine and K. F. Saiz (Koninklijke Philips
    Electronics), *Metal-insulator-metal (MIM) capacitor structure and
    methods of fabricating same*, US 6,717,193 B2, filed 2001-10-09,
    granted 2004-04-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6717193>
[^pat-mim-newportfab]: A. Kar-Roy and M. Racanelli (Newport Fab, LLC),
    *Method for fabrication of an MIM capacitor and related structure*,
    US 6,430,028 B1, filed 2000-11-22, granted 2002-08-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6430028>
[^pat-tcp-lam]: J. S. Ogle (Lam Research Corporation), *Method and
    apparatus for producing magnetically-coupled planar plasma*, US
    4,948,458 A, granted 1990-08-14.
    <https://patents.google.com/patent/US4948458A/en>
[^pat-dps-amat]: G. Z. Yin, H. Hanawa, D. X. Ma and D. Olgado (Applied
    Materials), *Plasma reactor with multi-section RF coil and isolated
    conducting lid*, US 5,540,824 A, granted 1996-07-30.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5540824>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^raw-data-passives]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the poly, diffusion
    and well resistors, MiM capacitors, varactors and bipolar
    transistors of the test tile, IC-CAP `.mdm` files in
    `sky130_fd_pr/cells/unsorted/`, `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells/unsorted>
[^cyp-qtp-123907]: Cypress Semiconductor, *Fab Process Qualification
    Report, QTP# 123907, 132302, 132301: Metal Stack Change, S8
    Technology, Fab 4 CMI*, document 001-91369 Rev. **, March 2014 (copy
    hosted by Tokyo Electron Device as the attachment to Cypress Product
    Information Notification PIN145273, 2014-03-13, which states the
    report is attached and available from cypress.com;
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>).
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/145273-Qualification_Report.pdf>
