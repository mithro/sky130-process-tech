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
*that* is the metal-3 stack — on the public description of the S8
metal stacks, a 300 Å TiW cap over Al–0.5%Cu[^cyp-qtp-113005] — which
is not yet patterned and must be etched, with its dielectric, at
{ref}`MM3E <step-140>`. If `CAPME` etched through the dielectric it
would begin to consume the bottom plate's cap everywhere outside the
capacitors, and the capacitor's edge would be a dielectric sidewall
exposed to plasma. The etch therefore has to remove a refractory
metal with very high {term}`selectivity` to a very thin dielectric —
for a TiW plate on an oxynitride, as assumed here (see
{ref}`CAPTIW1 <step-136>` and {ref}`CAPILD <step-135>`), a
fluorine-etchable metal over a fluorine-etchable dielectric — and to
stop within a few nanometres. A Texas
Instruments patent on the same operation for a TiN top electrode
states the target: a silicon-based dielectric "<1,000 Å" thick
(typically 150–400 Å), and a dry etch of the top electrode that
removes no more than 100 Å (typically under 50 Å) of it, using a
chlorine- or bromine-based first halogen gas, a fluorocarbon (CHF₃,
CH₂F₂ or CF₄) as the fluorine-bearing second halogen gas, and a
noble-gas carrier.[^pat-mim-ti-etch] The other two patents take the
alternative, in which the dielectric is patterned with the plate. The
Philips patent etches its ~3000 Å TiN top electrode and the insulator
in a multi-rate etch, slowing near the TiN/insulator interface and
stopping close to the TiN ARC on the bottom
electrode;[^pat-mim-philips] the Newport Fab process etches the TiN
top plate and the nitride dielectric together and then protects the
stack's sidewall with an oxide spacer.[^pat-mim-newportfab]

Which of the two SKY130 follows — stop on the dielectric, or cut
through it — is not public. The PDK's `cap_mim` cross-section draws
the thin "CAPILD" layer with exactly the lateral extent of the "CAPM"
plate above it, over a much wider "M3 (plate 1)";[^pdk-07] read
literally, that shows the dielectric removed outside the plate, but
the drawing is a schematic and cannot show a few nanometres of
residual film. Against the literal reading stands the stack itself:
under the dielectric lies the metal-3 cap, which is the same TiW the
etch is removing,[^cyp-qtp-113005] so an etch that cleared the
dielectric would have no selective layer left to stop on — although
the Philips process shows that a through-etch can be stopped by rate
control on the bottom-electrode cap.[^pat-mim-philips] We therefore
describe the stop-on-dielectric version as the more plausible
(inference) and record the other under *Open questions*.
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
etchant concentration and the ion energy.[^liu-2007-tiw] Chlorine
also etches both metals — Fischl and Hess studied tungsten in
chlorine discharges[^fischl-1987] — and the TI recipe's majority
Cl₂ (or Br₂) with a small fluorocarbon addition[^pat-mim-ti-etch] is,
on our reading, a blend chosen so that the metal etches by chlorine
while the oxide-like dielectric, which chlorine alone barely etches,
is attacked only by the small fluorine fraction. What is specific
to this instance within the flow is the stop: the other refractory
etches (the TiN local interconnect of {ref}`LI1ME <step-103>`, the
TiW caps opened at the start of every aluminium etch) land on thick
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
  Because fluorine etches TiW, punching through would thin the cap
  of every metal-3 line (the film {ref}`VIM3E <step-145>` later
  stops on) and expose aluminium to a fluorine plasma, which forms
  involatile AlF₃ rather than etching it[^hess-1982] — a residue the
  {ref}`MM3E <step-140>` chlorine etch would then have to break
  through. The ≤100 Å loss the TI patent allows[^pat-mim-ti-etch] is
  the scale of the margin.
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
   fluorine-bearing addition such as CF₄, CHF₃ or SF₆, in argon (the
   TI patent's Cl₂ or Br₂ / fluorocarbon / noble-gas
   scheme[^pat-mim-ti-etch]) — at moderate bias; for a ~0.1 µm
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
   (the TI patent's ≤100 Å[^pat-mim-ti-etch]).
5. **Strip and clean.** Downstream O₂/N₂ {term}`ash` — the "Gasonic
   PEP", Iridia or Mattson class in SkyWater's list[^skw-01] — then a
   solvent or semi-aqueous clean (the "EKS265, EKC270 solvents" of
   the wet-bench list[^skw-01]) that removes fluorocarbon and
   metal-fluoride residue without attacking TiW or the dielectric;
   no HF and no peroxide (H₂O₂ etches TiW — the wet route Danzl and
   McLaurin describe for stripping a TiW cap[^danzl-1997] — so it is
   excluded here by inference).
6. **Metrology.** Plate {term}`CD` by {term}`CD-SEM`; remaining
   dielectric thickness outside the plates by ellipsometry on
   monitors; particle and residue inspection; capacitance, leakage,
   breakdown and {math}`C(V)` on test structures at {term}`e-test`
   against the PDK's `CMIMA`/`CMIMP` limits.[^pdk-07]

## Machines typically used

* **High-density metal etcher**, 200 mm: Lam TCP 9600 / 2300
  Versys,[^lam-10k] Applied Materials Centura DPS,[^pat-dps-amat]
  TEL Unity ({ref}`category-etch`).
* **Downstream asher**; **solvent wet bench**.
* **CD-SEM**, **ellipsometer**, **e-test** for capacitor structures.

## Machines likely used at SkyWater

* **Lam 9600 or Lam 2300 Versys.** SkyWater lists "Lam 9600, Al, TiW,
  TiN, Pt" and "Lam 2300 Versys, Al, TiW, TiN, Nb, Pt".[^skw-01]
  Strength: **strong** for the tools and for TiW as a qualified
  material; which runs this step is not public.
* **Strip — "Gasonic PEP", Iridia, Mattson Aspen II; clean — batch
  rotational tools with "EKS265, EKC270 solvents".**[^skw-01]
  Strength: strong for existence; assignment is an inference.

## Resources required

* **SF₆ or CF₄**, **Cl₂ and/or BCl₃**, **Ar or N₂** for the etch
  (industry practice;[^nojiri-2015][^pat-mim-ti-etch] SkyWater lists
  no gases for its metal etchers, but names Cl₂, CF₄ and SF₆ on its
  poly/silicon etchers[^skw-01]); **He** for backside
  cooling.
* **O₂/N₂** for the ash;[^skw-01] **amine or semi-aqueous solvent**
  and DI water for the clean.[^skw-01]
* **Chamber consumables** and **monitor wafers** carrying the plate
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

## References

### Cross-check

* SkyWater PDK, *Device Details* — MiM construction, `CMIMA`,
  `CMIMP`, `RSCAPM`; the `cap_mim` cross-section with "CAPILD" drawn
  exactly under "CAPM" on a wider "M3 (plate 1)".[^pdk-07]
* SkyWater PDK, *Layers Reference* — `capm` 89:44.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `CAPMCD` 2 µm,
  `CAPMCDSP` 0.84 µm.[^pdk-03]
* Cypress, QTP 113005 — the 300 Å TiW cap of the metal beneath the
  dielectric.[^cyp-qtp-113005]
* SkyWater, *Facilities & Capabilities* — Lam 9600 and 2300 Versys
  with TiW; ashers; solvents.[^skw-01]
* Lam Research, Form 10-K (2003) — the 9600 and 2300 lines.[^lam-10k]
* Cathey et al. (TI), US 8,110,414 — a TiN top-electrode etch that
  removes no more than 100 Å of the dielectric.[^pat-mim-ti-etch]

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
* Hess, *Plasma Chem. Plasma Process.* 1982 — why fluorine does not
  etch aluminium, the hazard of punching through.[^hess-1982]
* Hwang and Giapis, *JVST B* 1997; Fang and McVittie, *IEEE EDL*
  1992; Cheung, P2ID 2000 — plasma charging and thin-dielectric
  damage.[^hwang-1997][^fang-1992][^cheung-2000]
* Wodecki, SPIE 1999 — emission endpoint and open area.[^wodecki-1999]
* Danzl and McLaurin, IEMT 1997 — peroxide etching of TiW, the wet
  chemistry this etch's clean must avoid.[^danzl-1997]
* Cathey et al. (TI), US 8,110,414 — selective plasma etch of MiM
  top electrodes.[^pat-mim-ti-etch]
* Olewine and Saiz (Philips), US 6,717,193 — a multi-rate etch of the
  top electrode and insulator that slows near their interface and
  stops close to the bottom electrode's TiN ARC.[^pat-mim-philips]
* Kar-Roy and Racanelli (Newport Fab), US 6,430,028 — etching plate
  and dielectric together and spacering the edge.[^pat-mim-newportfab]
* Ogle (Lam Research), US 4,948,458, and Yin et al. (Applied
  Materials), US 5,540,824 — the two high-density metal-etch
  sources.[^pat-tcp-lam][^pat-dps-amat]

## Open questions

* Whether `CAPME` stops on the capacitor dielectric or etches through it (so
  that the dielectric is patterned with the plate) is not public. The
  PDK's schematic cross-section draws the dielectric only under the
  plate,[^pdk-07] which read literally favours the latter; we describe
  the former because the metal-3 TiW cap beneath offers no selective
  stop for a through-etch (inference), although a rate-controlled
  stop of the Philips kind[^pat-mim-philips] would be possible.
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
    ended 2003-06-29.
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
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
