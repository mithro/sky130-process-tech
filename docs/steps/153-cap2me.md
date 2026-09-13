(step-153)=
# Step 153 — CAP2ME: Capacitor 2 mask etch

| | |
|---|---|
| **Step number** | 153 of 171[^steps-sheet] |
| **Step code** | `CAP2ME` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | BEOL — MiM capacitors, metal 3–5, via 3–4 |
| **Previous step** | {ref}`CAP2M <step-152>` |
| **Next step** | {ref}`MM4 <step-154>` |

## What this step is

`CAP2ME` etches the top plates of the second {term}`MiM capacitor`. Through the
resist islands of {ref}`CAP2M <step-152>` a plasma removes the blanket
top-plate film of {ref}`CAPTIW2 <step-151>` — described in this reference
as TiW of the order of 0.1 µm, an inference from the PDK's 5.8 Ω/sq
MiM2 top-plate sheet resistance[^pdk-07] — and stops on, or a little way
into, the thin capacitor dielectric of {ref}`CAPILD2 <step-150>`, leaving
the plate film only where the
layout draws `cap2m`, "MiM capacitor plate over metal 4".[^pdk-06] The
resist is then stripped: the step list used in this reference has no
separate strip step after `CAP2ME`, so this page treats the resist
strip and clean as part of the etch. The step repeats
{ref}`CAPME <step-138>` one metal level higher.

What lies under the film sets the difficulty. Beneath the plate film
is a dielectric some 20–30 nm thick (our estimate at
{ref}`CAPILD2 <step-150>`), and beneath that is the unpatterned
metal-4 stack of {ref}`WTIAL4 <step-149>`, whose cap is — on the
public description of the S8 metal stacks at lower levels — TiW over
Al–Cu.[^cyp-qtp-113005] If the etch went through the dielectric it
would start on the metal-4 cap everywhere outside the capacitors. The
etch therefore removes a refractory metal with high {term}`selectivity`
to a very thin silicon-based dielectric. A Texas Instruments patent
describes such an etch for a TiN (or TiN/Ti/TiN) top electrode on a
silicon-based dielectric "<1,000 Å" thick (typically 150–400 Å): a
dry etch that removes "≦100 Å" of the dielectric, using Cl₂ or Br₂ as
a first halogen gas, a small flow of CHF₃, CF₄ or CH₂F₂ as a
fluorine-containing second gas, and a noble-gas carrier, with a
selectivity of at least 8:1.[^pat-mim-ti-etch] Other published
processes etch through the dielectric instead: the Philips patent
etches its TiN top electrode and the insulator beneath with a fast, a
slower and a timed step, stopping near the TiN anti-reflective coating
of the bottom electrode,[^pat-mim-philips] and the Newport Fab patent
etches top plate and dielectric together and protects their sidewall
with a spacer before the bottom metal is etched.[^pat-mim-newportfab]

Which of these SKY130 follows is not public. The PDK's `cap_mim`
cross-section draws the thin "CAPILD" film under `CAP2M` with the same
lateral extent as the plate, over a wider "M4 (plate 2)",[^pdk-07] as it
does for `CAPM`; read literally that shows the dielectric removed
outside the plate, but a schematic cannot show a few nanometres of
residual film. As at {ref}`CAPME <step-138>`, we describe the
stop-on-dielectric version, because the metal-4 cap beneath is the same
kind of film the etch is removing and offers no selective stop
(inference), and we record the other under *Open questions*.

## Step category

`CAP2ME` is an {ref}`Etch <category-etch>` step of the *refractory
metal* class — the category page's "Ti:W and TiN" entry — and one of
the two capacitor-plate etches of the flow, with {ref}`CAPME <step-138>`.
Tungsten forms volatile WF₆ in fluorine plasmas — the mechanisms that
Turban, Coulon and Mutsukura and Petri, Henry and Sadeghi studied for
SF₆[^turban-1989][^petri-1992] — and Liu and Kuo showed that
titanium–tungsten films etch by reactive-ion etching in CF₄-based
plasmas, CF₄/Cl₂ among them.[^liu-2007-tiw] Chlorine discharges also etch
tungsten, as Fischl and Hess showed for tungsten and tungsten silicide
in chlorine-containing plasmas.[^fischl-1987] The TI recipe — mostly
Cl₂ or Br₂ with a small fluorocarbon flow[^pat-mim-ti-etch] — is, on
our reading, a blend in which the metal etches in chlorine while the
dielectric, which chlorine alone barely attacks, sees only the small
fluorine fraction; Flamm and Donnelly and Winters and Coburn set out the
surface chemistry behind such selectivity.[^flamm-1981][^winters-1992]

What is specific to this instance is the history of the wafer. Under
the metal-4 stack lies a finished first capacitor whose plates connect,
through via 3, to metal-4 shapes that are still one continuous sheet;
every `capm` top plate on the wafer is electrically tied to the blanket
metal 4 during this etch (inference from the PDK's stacked cross-section,[^pdk-07] in the sequence
described in this reference, where metal 4 is patterned after this etch).

## Why this step exists

* **It makes the plates.** The etch turns the `cap2m` resist image
  into discrete top electrodes whose area, with the dielectric
  thickness, sets the `CMIM2A` 2 fF/µm² and `CMIM2P` 0.19 fF/µm the PDK
  models;[^pdk-07] the etch bias is folded into those two numbers.
* **It must not open the dielectric.** Outside the plates the
  dielectric is all that separates the plasma from the metal-4 cap. A
  fluorine-rich punch-through would thin the cap of every metal-4 line —
  the film {ref}`VIM4E <step-160>` later stops on — and expose aluminium
  to fluorine, which forms involatile AlF₃ rather than etching it,[^hess-1982]
  leaving a residue the {ref}`MM4E <step-155>` chlorine etch must break
  through. The TI patent's ≤100 Å loss[^pat-mim-ti-etch] is the scale of
  the margin.
* **It must not damage the dielectric under the plates.** A metal plate
  on a thin insulator over a large conductor is the geometry that
  collects plasma charge. Hwang and Giapis explained the notching that
  pattern-dependent charging produces in high-density
  plasmas,[^hwang-1997] Fang and McVittie the thin-oxide damage that
  charging causes,[^fang-1992] and Wang, Ackaert et al. the
  {term}`plasma-charging <plasma charging>` damage of floating MiM capacitors;[^wang-2004-mim]
  Cheung analysed charging during plasma-enhanced dielectric
  deposition, which follows at {ref}`NILD6 <step-156>`.[^cheung-2000]
  The final etch stage is run at low bias for this reason (industry
  practice[^nojiri-2015]).
* **Clean plate edges.** Residue or a foot at the plate edge is a
  leakage and fringing-field site and a place where the
  {ref}`NILD6 <step-156>` fill can void; the multi-step etch of the
  Philips patent[^pat-mim-philips] and the spacer of the Newport Fab
  patent[^pat-mim-newportfab] both address the edge.

Without `CAP2ME` the second top-plate film would remain a sheet and be
lost, with the dielectric, at {ref}`MM4E <step-155>`.

## How it is typically performed

An industry-generic MiM top-plate etch for a 200 mm aluminium back end
(SKY130's recipe is not public); {ref}`CAPME <step-138>` describes the
same sequence.

1. **Chamber.** A single-wafer metal etcher with a high-density source
   and independent bias — Lam's {term}`TCP` family[^pat-tcp-lam][^lam-10k]
   or Applied Materials' DPS reactor[^pat-dps-amat] — with helium
   backside cooling and optical-emission {term}`endpoint`; SkyWater's
   two metal etchers are both listed for "TiW".[^skw-01]
2. **BARC open** (if a BARC was used at {ref}`CAP2M <step-152>`): a
   short O₂/N₂ step.
3. **Main etch.** A chlorine- or bromine-based chemistry with a small
   fluorocarbon addition in a noble-gas carrier — the scheme of the TI
   patent, which gives top-electrode etch rates of at least 1 200 Å/min
   (typically 1 800–3 000 Å/min)[^pat-mim-ti-etch] — so that about 0.1 µm
   of TiW clears in well under a minute (our arithmetic; the patent
   describes TiN, not TiW).
4. **Endpoint and {term}`over-etch`.** Optical emission as the plate film clears; the
   open area is most of the wafer, so the signal is strong — the reverse
   of the low-open-area problem Wodecki describes for via
   etches.[^wodecki-1999] The over-etch is short and at reduced bias,
   sized to clear stringers while removing at most a few nanometres of
   dielectric.[^pat-mim-ti-etch]
5. **Strip and clean.** Downstream O₂/N₂ {term}`ash` — SkyWater lists
   "Gasonic PEP", Iridia and Mattson Aspen II strippers[^skw-01] — then a
   solvent clean (the "EKS265, EKC270 solvents" of its batch rotational
   tools[^skw-01]) that removes fluorocarbon and metal-halide residue
   without attacking TiW or the dielectric; hydrogen peroxide etches TiW,
   as Danzl and McLaurin used it to,[^danzl-1997] so on our reading it is
   excluded here.
6. **Metrology.** Plate {term}`CD` by {term}`CD-SEM`; remaining
   dielectric outside the plates by ellipsometry on monitors; residue
   inspection; capacitance, leakage and breakdown on test structures at
   {term}`e-test` against `CMIM2A` and `CMIM2P`.[^pdk-07]

## Machines typically used

* **High-density metal etcher**, 200 mm: Lam TCP 9600 / 2300
  Versys,[^lam-10k] Applied Materials Centura DPS,[^pat-dps-amat]
  TEL Unity ({ref}`category-etch`).
* **Downstream plasma asher**; **solvent wet bench**.
* **CD-SEM**, **ellipsometer**, **e-test** for capacitor structures.

## Machines likely used at SkyWater

* **Lam 9600 or Lam 2300 Versys.** SkyWater lists "Lam 9600, Al, TiW,
  TiN, Pt" and "Lam 2300 Versys, Al, TiW, TiN, Nb, Pt".[^skw-01]
  Strength: **strong** for the tools and for TiW as a qualified
  material; which runs this step is not public.
* **Strip — "Gasonic PEP", "Iridia RF microwave", "Mattson Aspen2";
  clean — "Batch Rotational", "EKS265, EKC270 solvents, CO2 injected
  DI".**[^skw-01]
  Strength: strong for existence; assignment is an inference.

## Resources required

* **Cl₂ or Br₂** (or HBr), a small flow of **CHF₃, CF₄ or CH₂F₂**, and
  **Ar or He** for the etch (industry practice;[^pat-mim-ti-etch][^nojiri-2015]
  SkyWater lists no gases for its metal etchers, but names Cl₂, HBr,
  CF₄ and CHF₃ on its poly/silicon etchers[^skw-01]); **He** for
  backside cooling.
* **O₂/N₂** for the ash;[^skw-01] **amine or semi-aqueous solvent** and
  DI water for the clean.[^skw-01]
* **Chamber consumables** and **monitor wafers** with TiW over thin
  dielectric for rate and selectivity checks.

## Related steps and cross-references

* Previous: {ref}`CAP2M <step-152>` (the mask). Next:
  {ref}`MM4 <step-154>` (the metal-4 mask printed over the plates), then
  {ref}`MM4E <step-155>` (which removes the remaining dielectric and the
  metal outside the wiring).
* The films it etches and stops on: {ref}`CAPTIW2 <step-151>`,
  {ref}`CAPILD2 <step-150>`; the metal beneath: {ref}`WTIAL4 <step-149>`.
* The via etch that later lands on the plate: {ref}`VIM4E <step-160>`.
* The first capacitor's plate etch: {ref}`CAPME <step-138>`; the other
  refractory-metal etch: {ref}`LI1ME <step-103>`.
* Category page: {ref}`Etch <category-etch>`.

## References

### Cross-check

* SkyWater PDK, *Device Details* — `CMIM2A`, `CMIM2P`, MiM2 top plate
  5.8 Ω/sq; the stacked `cap_mim` cross-section with "CAPILD" under
  `CAP2M`.[^pdk-07]
* SkyWater PDK, *Layers Reference* — `cap2m` 97:44.[^pdk-06]
* Cypress, QTP 113005 — the TiW caps of the S8 metal stacks.[^cyp-qtp-113005]
* SkyWater, *Facilities & Capabilities* — Lam 9600 and 2300 Versys with
  TiW; strippers; solvents; etch gases on the poly/silicon etchers.[^skw-01]
* Lam Research, Form 10-K (2003) — the 9600 and 2300 lines.[^lam-10k]
* Cathey et al. (TI), US 8,110,414 — a top-electrode etch removing
  ≦100 Å of a silicon-based dielectric.[^pat-mim-ti-etch]

### High-level understanding

* Wikipedia, *Reactive-ion etching*, *Dry etching*.[^wiki-rie][^wiki-dry-etch]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — refractory
  metal etching in the back end.[^txt-05]
* Nojiri, *Dry Etching Technology for Semiconductors* — metal etch
  chemistry, endpoint and charging damage.[^nojiri-2015]

### Deep dive

* Cathey et al. (TI), US 8,110,414 — selective plasma etch of MiM top
  electrodes over a thin dielectric.[^pat-mim-ti-etch]
* Olewine and Saiz (Philips), US 6,717,193 — a fast, slow and timed
  etch through top electrode and insulator, stopping near the bottom
  electrode's TiN coating.[^pat-mim-philips]
* Kar-Roy and Racanelli (Newport Fab), US 6,430,028 — top plate and
  dielectric etched together, with a sidewall spacer.[^pat-mim-newportfab]
* Liu and Kuo, *J. Electrochem. Soc.* 2007 — reactive-ion etching of
  titanium–tungsten films.[^liu-2007-tiw]
* Turban, Coulon and Mutsukura, *Thin Solid Films* 1989, and Petri,
  Henry and Sadeghi, *J. Appl. Phys.* 1992 — tungsten etching mechanisms
  in SF₆ plasmas.[^turban-1989][^petri-1992]
* Fischl and Hess, *J. Electrochem. Soc.* 1987 — tungsten and tungsten
  silicide in chlorine-containing discharges.[^fischl-1987]
* Flamm and Donnelly, 1981, and Winters and Coburn, 1992 — the design
  of plasma etchants and the surface chemistry of
  selectivity.[^flamm-1981][^winters-1992]
* Hess, *Plasma Chem. Plasma Process.* 1982 — the plasma etch chemistry
  of aluminium, and why fluorine does not remove it.[^hess-1982]
* Hwang and Giapis, *JVST B* 1997; Fang and McVittie, *IEEE EDL* 1992;
  Cheung, P2ID 2000 — charging, notching and thin-dielectric
  damage.[^hwang-1997][^fang-1992][^cheung-2000]
* Wang, Ackaert et al., *IEEE TED* 2004 — plasma-charging damage of
  floating MiM capacitors.[^wang-2004-mim]
* Wodecki, SPIE 1999 — emission endpoint and open area.[^wodecki-1999]
* Danzl and McLaurin, IEMT 1997 — peroxide etching of a TiW cap, the wet
  chemistry the clean must avoid.[^danzl-1997]
* Ogle (Lam Research), US 4,948,458, and Yin et al. (Applied Materials),
  US 5,540,824 — the two high-density metal-etch sources.[^pat-tcp-lam][^pat-dps-amat]

## Open questions

* Whether `CAP2ME` stops on the dielectric or etches through it is not
  public. The PDK's schematic cross-section draws the dielectric only
  under the plate,[^pdk-07] which read literally favours a through-etch;
  we describe a stop on the dielectric because the metal-4 cap offers no
  selective stop (inference).
* The chemistry, endpoint, over-etch and dielectric loss are not public;
  the TI patent describes a TiN, not a TiW, electrode.[^pat-mim-ti-etch]
* Whether a sidewall spacer or other edge treatment follows is not
  public.
* Which of the two listed Lam metal etchers runs the step is not
  public.[^skw-01]
* The step list used in this reference has no separate strip step after
  `CAP2ME`; this page treats the resist strip and clean as part of the
  etch.

<!-- footnotes -->

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
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^wiki-dry-etch]: Wikipedia, *Dry etching*.
    <https://en.wikipedia.org/wiki/Dry_etching>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^nojiri-2015]: K. Nojiri, *Dry Etching Technology for Semiconductors*,
    Springer, 2015. <https://doi.org/10.1007/978-3-319-10295-5>
[^liu-2007-tiw]: G. Liu and Y. Kuo, "Reactive Ion Etching of Titanium
    Tungsten Thin Films", *Journal of The Electrochemical Society*
    **154**(7), H653 (2007). <https://doi.org/10.1149/1.2737631>
[^turban-1989]: G. Turban, J. F. Coulon and N. Mutsukura, "A
    mechanistic study of SF₆ reactive ion etching of tungsten", *Thin
    Solid Films* **176**(2), 289–308 (1989).
    <https://doi.org/10.1016/0040-6090(89)90102-8>
[^petri-1992]: R. Petri, D. Henry and N. Sadeghi, "Tungsten etching
    mechanisms in low-pressure SF₆ plasma", *Journal of Applied Physics*
    **72**(7), 2644–2651 (1992). <https://doi.org/10.1063/1.351565>
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
[^wang-2004-mim]: Z. Wang, J. Ackaert, C. Salm, F. G. Kuper, M. Tack,
    E. De Backer, P. Coppens, L. De Schepper and B. Vlachakis,
    "Plasma-charging damage of floating MIM capacitors", *IEEE
    Transactions on Electron Devices* **51**(6), 1017–1024 (2004).
    <https://doi.org/10.1109/TED.2004.829518>
[^wodecki-1999]: N. Wodecki, "Low open area multilayered dielectric film
    etch endpoint detection using EndPoint Plus", *Proc. SPIE* **3882**,
    Process, Equipment, and Materials Control in Integrated Circuit
    Manufacturing V, 231 (1999). <https://doi.org/10.1117/12.361313>
[^danzl-1997]: R. B. Danzl and A. McLaurin, "The use of concentrated
    hydrogen peroxide for the removal of a TiW ARC from aluminum bond
    pads", *Proc. Twenty-First IEEE/CPMT International Electronics
    Manufacturing Technology Symposium (IEMT 1997)*, pp. 99–104.
    <https://doi.org/10.1109/IEMT.1997.626884>
[^pat-tcp-lam]: J. S. Ogle (Lam Research Corporation), *Method and
    apparatus for producing magnetically-coupled planar plasma*,
    US 4,948,458 A, granted 1990-08-14.
    <https://patents.google.com/patent/US4948458A/en>
[^pat-dps-amat]: G. Z. Yin, H. Hanawa, D. X. Ma and D. Olgado (Applied
    Materials), *Plasma reactor with multi-section RF coil and isolated
    conducting lid*, US 5,540,824 A, granted 1996-07-30.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5540824>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
