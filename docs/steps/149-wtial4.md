(step-149)=
# Step 149 — WTIAL4: AlCu 2/TiW deposition

| | |
|---|---|
| **Step number** | 149 of 171[^steps-sheet] |
| **Step code** | `WTIAL4` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | BEOL — MiM capacitors, metal 3–5, via 3–4 |
| **Previous step** | {ref}`WCMP5 <step-148>` |
| **Next step** | {ref}`CAPILD2 <step-150>` |

## What this step is

`WTIAL4` deposits the metal-4 film stack. Onto the polished cap oxide
and tungsten via-3 plugs left by {ref}`WCMP5 <step-148>` a sputtering
{term}`cluster tool` lays down, in one vacuum sequence on our reading, a thin
refractory bottom layer, a thick aluminium–copper alloy and a
titanium–tungsten cap — the construction described for metal 3 at
{ref}`WTIAL3 <step-134>`. The stack is blanket, and like metal 3 it
stays blanket while a {term}`MiM capacitor` is built on it: the second
capacitor module — {ref}`CAPILD2 <step-150>`,
{ref}`CAPTIW2 <step-151>`, {ref}`CAP2M <step-152>` and
{ref}`CAP2ME <step-153>` — comes before {ref}`MM4 <step-154>` and
{ref}`MM4E <step-155>` pattern the stack into the `met4` layer (GDS
71:20, "Metal 4").[^pdk-06] The layer table calls the second plate
`cap2m` (97:44), "MiM capacitor plate over metal 4",[^pdk-06] and the
PDK's device page lists "CAP2M over Metal-4" beside "CAPM over
Metal-3" as its two MiM constructions.[^pdk-07]

The PDK gives metal 4 the same numbers as metal 3. The process stack
diagram labels `metal4` 0.845 µm, with its bottom 4.0211 µm above the
substrate reference and the bottom of `metal5` at 5.3711 µm;[^pdk-04]
the device page and extraction tables give metal 4 a
{term}`sheet resistance` of 47 mΩ/sq (limits 38–56 mΩ/sq), identical to
metal 3;[^pdk-07][^pdk-08] and Edwards's introductory slides on the
open PDK repeat the 0.845 µm.[^ann-16] The assumptions table lists a
"Metal4 thickness for antenna ratio calculation" of 0.8 µm for the
"S8P*/SP8P*" flows and 2 µm for the "S8Q*/SP8Q" flows,[^pdk-03] and
the rule tables name "SKY130P*/SP8P*" as the flow in which via 4
connects metal 4 to metal 5 and call the SP8P*/SKY130P* CAD flow
"PLM",[^pdk-periph] and the mask table flags its "Via 2-PLM", "Metal
3-PLM" and "Via3-PLM" entries as used in SKY130;[^pdk-05] and the
background page lists "5 levels of metal (p - penta)" among the
technology's features.[^pdk-02] On that reading SKY130 as published is
a "P" flow, so the 0.8 µm value applies and the 2 µm entry belongs to
another variant (inference). The metal-4 design rules match metal 3's:
0.300 µm width and space (m4.1, m4.2), 0.065 µm enclosure of via 3 (m4.3),
0.240 µm² minimum area (m4.4a) and a 0.7 minimum oxide pattern
density checked in 700 µm windows (m4.pd.1, m4.pd.2a).[^pdk-periph]

The step list calls this step "AlCu 2/TiW deposition";[^steps-sheet] a
step name is not evidence of a chemistry, and no public source
describes the metal-4 films themselves. The Cypress
qualification reports that give Ti/Al–Cu/TiW thicknesses for the S8
technologies at the same fab describe three-metal processes and stop
at metal 3;[^cyp-qtp-113005][^cyp-qtp-123907] SkyWater's PVD film list
("Aluminum both pure and Cu doped", "TiW", "Collimated Ti"[^skw-01])
and the 0.845 µm and 47 mΩ/sq that the PDK gives both metal 3 and
metal 4 are the public basis for describing this stack as a repeat of
metal 3 (inference). With 0.8 µm of Al–Cu, 47 mΩ/sq corresponds to a
resistivity of about 3.8 µΩ·cm, within the range expected for
sputtered Al–0.5%Cu (typical industry value;[^txt-02] our arithmetic).
The reading of the bottom layer as Ti or TiW is discussed at
{ref}`WTIAL3 <step-134>` and applies here unchanged.

## Step category

`WTIAL4` is a {ref}`Thin-film deposition <category-deposition>` step
of the *PVD, multi-layer metal* class; {ref}`TIAL6 <step-112>` sets out
the sputtering of Ti, Al–Cu and Ti:W films, {ref}`TIAL12 <step-123>`
what a via level adds and {ref}`WTIAL3 <step-134>` what a thick film
changes — longer deposition, more wafer heating, larger grains, more
stored stress and more {term}`hillock` risk. What is specific here is the
position of the stack in the capacitor structure. The PDK's `cap_mim`
cross-section, drawn for the "stacked" arrangement, shows metal 4
split into two shapes: one, "M4 (plate 2)", lies under `CAP2M` and is
joined by vias to the `CAPM` plate below, and the other, "M4
(plate 1)", joins "M3 (plate 1)" below to "M5 (plate 1)"
above.[^pdk-07] On that drawing, the stack deposited here is the
bottom electrode of the second capacitor *and* the conductor that
carries the first capacitor's top plate, so the two capacitors share
it as a middle electrode and add in parallel — the device page says
the capacitors "may be stacked to maximize total
capacitance".[^pdk-07] The Newport Fab and TSMC stacked-MiM patents
describe the same sharing of a middle electrode between an upper and a
lower capacitor.[^pat-mim-stack-newportfab][^pat-mim-stack-tsmc]

## Why this step exists

Metal 4 is the second coarse-pitch, low-resistance routing level and
the bottom plate of the second MiM capacitor; the reasons for each film
are those of metals 1–3:

* **Low resistance for power, clocks and long signals.** At 47 mΩ/sq
  and 0.3 µm width and space[^pdk-07][^pdk-periph] metal 4 doubles the
  thick routing resource of metal 3. Bohr's argument that interconnect
  limits performance,[^bohr-1995] Stamper, Fuselier and Tian's account
  of wiring RC delay at the sub-0.25 µm generation[^stamper-1998] and
  the ITRS 2001 interconnect chapter[^itrs-02] are the context; the
  PDK's extraction tables give a metal-4-to-metal-5 plate capacitance of
  68.33 aF/µm², against 84.03 aF/µm² from metal 3 to metal 4.[^pdk-08]
* **{term}`Electromigration <electromigration>` in thick Al–Cu between tungsten studs.** Below
  each metal-4 line sit tungsten via-3 plugs; copper doping,[^ames-1970]
  the (111) texture a refractory underlayer promotes,[^knorr-1996][^kamoshida-1997]
  Blech's critical length[^blech-1976] and the short-length effect with
  tungsten barriers that Filippi, Biery and Wood showed[^filippi-1993]
  apply as at metal 3; Nix and Arzt describe void nucleation and growth
  in such lines.[^nix-1992] Above metal 4 the connection is different:
  via 4 is 0.8 µm (via4.1)[^pdk-periph] and is discussed at
  {ref}`VIM4E <step-160>` and {ref}`WTIAL5 <step-161>`.
* **Hillocks and stress.** Hillock growth in aluminium films —
  Chaudhari's analysis[^chaudhari-1974] — rises with film thickness and
  heat treatment, as Zlatanović and Davinić measured;[^zlatanovic-1990]
  the TiW cap suppresses hillocks and serves as the anti-reflective
  surface, the role Rocke and Schneegans documented for a refractory
  cap.[^rocke-1988] Stress-induced voiding (Yue, Funsten and
  Taylor[^yue-1985]) and wafer bow (Stoney's relation[^stoney-1909])
  accumulate with a fourth aluminium level on the wafer.
* **The second MiM bottom electrode.** The PDK gives the metal-4
  capacitor the same electrical specification as the metal-3 one —
  `CMIM2A` 2 fF/µm², `CMIM2P` 0.19 fF/µm and a 5.8 Ω/sq top plate —
  and calls the two constructions "identical".[^pdk-07] The TiW cap
  of this stack is therefore the bottom-electrode surface for
  {ref}`CAPILD2 <step-150>`, and its smoothness and cleanliness matter
  as at {ref}`WTIAL3 <step-134>`; Greenwood and Prasad describe the
  alternative of a TiN-only bottom plate for a MiM capacitor in an
  aluminium back end.[^greenwood-2007]
* **A fuse level.** The PDK's {term}`metal-fuse <metal fuse>` rules say that the
  "SP8P*/SKY130P* (PLM) CADflow" uses "MM4 for Metal Fuse", with a fuse
  width of 0.800 µm and length of 7.200 µm (mf.1, mf.2), and the layer
  table carries a `met4` "fuse" purpose (71:17).[^pdk-periph][^pdk-06]
  On that reading some metal-4 shapes are fuse links, which this stack
  must also serve (inference from the PDK's metal-fuse note and the `met4` fuse
  purpose[^pdk-periph][^pdk-06]).

Without `WTIAL4` there is no metal 4, no bottom plate for the second
MiM capacitor, and the via-3 plugs would end in air.

## How it is typically performed

An industry-generic thick Ti(W)/Al–Cu/TiW deposition for a 200 mm,
130 nm-era fab (SKY130's recipe is not public; the film-by-film
account is at {ref}`TIAL6 <step-112>` and the thick-film changes at
{ref}`WTIAL3 <step-134>`):

1. **Cluster tool.** A multi-chamber PVD platform — SkyWater's "AMAT
   PVD Metal" with "Sputter etch, degas"[^skw-01] — so that {term}`degas`,
   pre-clean and the depositions happen without an air break; the
   Endura is the 200 mm-era Applied Materials platform.[^amat-endura]
2. **Degas and pre-clean.** A vacuum bake, then a light argon
   {term}`sputter etch` to remove the tungsten oxide from the via-3 plug tops and any
   post-CMP residue (industry practice[^txt-05]).
3. **Bottom layer.** A thin Ti or TiW film — collimated or ionised
   titanium[^rossnagel-1991][^rossnagel-1998] or Ti:W from a 10 wt.% Ti
   target[^pat-tiw-hitachi]; the choice and thickness are not public,
   and the metal-3 descriptions of 150 Å Ti[^cyp-qtp-113005] and 500 Å
   TiW[^cyp-qtp-123907] are the nearest public analogues.
4. **Al–0.5%Cu, of the order of 0.8 µm.** Sputtered from an
   Al–Cu target (the Cypress reports give the film as Al-0.5%Cu) at a wafer temperature of roughly 150–300 °C
   (industry-typical[^txt-02]), in several passes or on a cooled
   pedestal so that the wafer does not drift into the hillock and
   copper-precipitation regime (industry practice[^txt-05]); grain size
   and texture follow the structure-zone relations.[^thornton-1974][^ohring-2002]
   The thickness is inferred from the 0.845 µm stack of the
   PDK[^pdk-04] less the refractory layers.
5. **TiW cap.** From a Ti:W target[^pat-tiw-hitachi]; about 300 Å by
   analogy with the metal-3 descriptions[^cyp-qtp-113005] (inference).
   Its surface receives the second MiM dielectric at
   {ref}`CAPILD2 <step-150>`, so particle and queue-time control
   matter as at {ref}`WTIAL3 <step-134>` (inference).
6. **Metrology.** Sheet resistance by {term}`four-point probe` (the
   PDK's 47 mΩ/sq[^pdk-07] is what a finished stack reads after the
   back-end anneals); thickness by XRF or profilometry; reflectivity;
   stress by wafer bow; particles.

## Machines typically used

* **{ref}`PVD cluster tool <machine-pvd-cluster-tool>` with Ti/TiW, Al–Cu and TiW chambers**, 200 mm:
  Applied Materials Endura,[^amat-endura] Novellus INOVA, Ulvac and
  Anelva sputtering systems ({ref}`category-deposition`).
* **Degas and sputter-etch pre-clean chambers**.
* **{ref}`Four-point probe <machine-sheet-resistance-metrology>`**, **{ref}`XRF <machine-film-thickness-metrology>`**, **reflectometer**, **stress gauge**.

## Machines likely used at SkyWater

* **AMAT PVD Metal platform.** SkyWater lists "AMAT PVD Metal" with
  "Sputter etch, degas", "Aluminum both pure and Cu doped", "TiW",
  "ESC TiN", "Imp TiN", "Collimated Ti", "WN", "Cobalt",
  "Niobium".[^skw-01] Strength: **strong** for the vendor and for the
  films; the platform model (Endura[^amat-endura]) and the bottom-layer
  choice are **inferences**.
* **Metal etchers "Lam 9600, Al, TiW, TiN, Pt" and "Lam 2300 Versys,
  Al, TiW, TiN, Nb, Pt"**[^skw-01] corroborate that TiW-capped
  aluminium is etched in the fab (used at {ref}`MM4E <step-155>`).

## Resources required

* **{ref}`Sputter targets <material-sputter-targets>`** — titanium, Al–0.5%Cu and Ti:W (10 wt.%
  Ti[^pat-tiw-hitachi]); SkyWater's filings name Honeywell Electronic
  Materials (2021 S-1 and fiscal 2023 10-K) and JX Metals (fiscal 2023 10-K)
  as sputter-target suppliers.[^sec-01][^sec-02]
* **{ref}`Argon <material-process-gases>`** for sputtering and pre-clean; **nitrogen** for venting. Gas
  suppliers named in SkyWater's filings: Air Products and Praxair (2021
  S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]
* **{ref}`Chamber shields <material-hardware-consumables>`, clamps and electrostatic-chuck consumables**,
  consumed at the thick-film rate of metal 3.
* **{ref}`Monitor wafers <material-substrates>`** for sheet resistance, reflectivity, stress and
  particles.

## Related steps and cross-references

* Previous: {ref}`WCMP5 <step-148>` (the via-3 plugs and oxide it lands
  on). Next: {ref}`CAPILD2 <step-150>` (the second MiM dielectric),
  then {ref}`CAPTIW2 <step-151>`, {ref}`CAP2M <step-152>`,
  {ref}`CAP2ME <step-153>`, and only then {ref}`MM4 <step-154>` and
  {ref}`MM4E <step-155>`.
* The plugs it contacts: {ref}`TIN5 <step-146>`, {ref}`WDEP5 <step-147>`.
* The dielectric that will surround the lines: {ref}`NILD6 <step-156>`;
  the via etch that stops on the TiW cap: {ref}`VIM4E <step-160>`.
* The same construction at metal 3, with its capacitor module:
  {ref}`WTIAL3 <step-134>`, {ref}`CAPILD <step-135>`; the thin stacks
  where the films are explained in full: {ref}`TIAL6 <step-112>`,
  {ref}`TIAL12 <step-123>`; the top metal: {ref}`WTIAL5 <step-161>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, *Process stack diagram* — `metal4` 0.845 µm; metal4
  and metal5 bottom levels 4.0211 and 5.3711 µm; `cap2m` between
  `metal4` and `metal5`.[^pdk-04]
* SkyWater PDK, *Device Details* — `RSM4` 0.047 Ω/sq; "CAP2M over
  Metal-4"; `CMIM2A`, `CMIM2P`; the stacked `cap_mim`
  cross-section.[^pdk-07]
* SkyWater PDK, *Parasitic Layout Extraction* — metal 4 47 mΩ/sq;
  metal-3-to-4 and metal-4-to-5 plate capacitances.[^pdk-08]
* SkyWater PDK, *Criteria & Assumptions* — metal-4 antenna thickness
  0.8 µm (S8P*/SP8P*) and 2 µm (S8Q*/SP8Q).[^pdk-03]
* SkyWater PDK, *Background* — "5 levels of metal (p - penta)".[^pdk-02]
* SkyWater PDK, *Masks* — "Via 2-PLM", "Metal 3-PLM", "Via3-PLM" flagged
  as used in SKY130.[^pdk-05]
* SkyWater PDK, *Periphery rules* — m4.1–m4.pd.2b; via4 function
  "SKY130P*/SP8P*"; the metal-fuse note and mf.1–mf.2.[^pdk-periph]
* SkyWater PDK, *Layers Reference* — `met4` 71:20, `met4` fuse 71:17;
  `cap2m` 97:44.[^pdk-06]
* Edwards, 2021 lecture slides — metal4 0.845 µm.[^ann-16]
* Cypress, QTP 113005 and QTP 123907/132302/132301 — the three-metal
  S8 stacks, for comparison.[^cyp-qtp-113005][^cyp-qtp-123907]
* SkyWater, *Facilities & Capabilities* — "AMAT PVD Metal" film list;
  metal etchers.[^skw-01]
* SkyWater, Form S-1 and 10-K — target suppliers.[^sec-01][^sec-02]
* Hitachi Metals, US 5,160,534 — Ti:W target composition.[^pat-tiw-hitachi]
* Applied Materials, *Endura PVD*.[^amat-endura]

### High-level understanding

* Wikipedia, *Electromigration*, *Sputter deposition*, *Interconnect
  (integrated circuits)*.[^wiki-em][^wiki-sputter][^wiki-interconnect]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  sputtering and aluminium metallisation.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — multilevel
  aluminium stacks and thick upper metals.[^txt-05]
* Ohring, *Materials Science of Thin Films* — film growth, stress and
  structure.[^ohring-2002]

### Deep dive

* Kar-Roy, Racanelli and Kempf (Newport Fab), US 7,078,310 — a
  composite MiM of two capacitors stacked between interconnect levels
  and joined in parallel.[^pat-mim-stack-newportfab]
* Chang, Lee and Chen (TSMC), US 7,317,221 — stacked MiM capacitors
  cross-connected through filled vias.[^pat-mim-stack-tsmc]
* Greenwood and Prasad, ISDRS 2007 — a TiN-only MiM bottom plate in
  an aluminium back end.[^greenwood-2007]
* Bohr (Intel), IEDM 1995, and Stamper, Fuselier and Tian (IBM), IITC
  1998 — interconnect scaling and wiring RC delay.[^bohr-1995][^stamper-1998]
* ITRS 2001, *Interconnect* — aluminium metallisation at the 130 nm
  generation.[^itrs-02]
* Zlatanović and Davinić, *Vacuum* 1990, and Chaudhari (IBM), *J.
  Appl. Phys.* 1974 — hillock formation versus aluminium thickness and
  heat treatment.[^zlatanovic-1990][^chaudhari-1974]
* Yue, Funsten and Taylor, IRPS 1985, and Stoney, *Proc. R. Soc. A*
  1909 — stress-induced voids and film stress from wafer
  curvature.[^yue-1985][^stoney-1909]
* Rocke and Schneegans (Siemens), *JVST B* 1988 — a refractory cap for
  anti-reflection and hillock suppression.[^rocke-1988]
* Ames, d'Heurle and Horstmann, 1970; Blech, 1976; Filippi, Biery and
  Wood, 1993; Nix and Arzt, 1992 — copper doping, the critical length,
  the short-length effect with tungsten barriers, and void
  growth.[^ames-1970][^blech-1976][^filippi-1993][^nix-1992]
* Knorr and Rodbell, 1996, and Kamoshida and Ito, 1997 — texture and
  the refractory underlayer.[^knorr-1996][^kamoshida-1997]
* Thornton, *JVST* 1974 — the structure-zone model for thick sputtered
  films.[^thornton-1974]
* Rossnagel et al., 1991, and Rossnagel, 1998 — collimated and ionised
  PVD for the thin underlayer.[^rossnagel-1991][^rossnagel-1998]

## Open questions

* No public source gives the metal-4 film thicknesses or the
  bottom-layer material; the Cypress reports that describe S8 metal
  stacks stop at metal 3.[^cyp-qtp-113005][^cyp-qtp-123907] The Ti or
  TiW reading discussed at {ref}`WTIAL3 <step-134>` applies here
  unresolved.
* Whether the SKY130 metal 4 is the 0.845 µm of the PDK's diagram[^pdk-04]
  or the 0.8 µm of the antenna table's P-flow entry[^pdk-03] — the same
  difference discussed for metal 3 at {ref}`MM3E <step-140>` — is not
  public; the 2 µm "S8Q*/SP8Q" entry[^pdk-03] is read here as another
  flow.
* That SKY130 is the "P" flow of the rule tables (SKY130P*, PLM) is our
  reading of the via-4 and metal-fuse notes,[^pdk-periph] of the mask
  table's flagged "-PLM" entries[^pdk-05] and of the background page's
  "p - penta".[^pdk-02]
* Whether fuses are drawn in metal 4 in SKY130 designs as
  published, and how that constrains this stack, is not public beyond
  the fuse note.[^pdk-periph]
* Deposition temperatures, pressures, powers and whether the Al–Cu is
  deposited in one pass or several are not public.

<!-- footnotes -->

[^pdk-02]: SkyWater PDK Authors, *Background*, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/background.html>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (generic resistors;
    MiM capacitors), SkyWater SKY130 PDK documentation, and the
    `cap_mim` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/cap_mim/cross-section-cap_mim.svg>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance and capacitance tables), SkyWater SKY130 PDK
    documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^ann-16]: T. Edwards (Efabless), *Introduction to the SkyWater PDK —
    The New Age of Open Source Silicon*, lecture slides, 2021-10-08
    (UC San Diego BENG 207).
    <https://isn.ucsd.edu/courses/beng207/lectures/Tim_Edwards_2021_slides.pdf>
[^cyp-qtp-113005]: Cypress Semiconductor, *Product Qualification
    Plan, QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8
    Technology, CMI (Fab 4)*, document 001-85611 Rev. *A, January
    2013 (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^cyp-qtp-123907]: Cypress Semiconductor, *Fab Process Qualification
    Report, QTP# 123907, 132302, 132301: Metal Stack Change, S8
    Technology, Fab 4 CMI*, document 001-91369 Rev. **, March 2014
    (copy hosted by Tokyo Electron Device as the attachment to
    Cypress Product Information Notification PIN145273, 2014-03-13,
    which states the report is attached and available from
    cypress.com; <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>).
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/145273-Qualification_Report.pdf>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^pat-mim-stack-newportfab]: A. Kar-Roy, M. Racanelli and P. Kempf
    (Newport Fab, LLC), *Method for fabricating a high density composite
    MIM capacitor with flexible routing in semiconductor dies*,
    US 7,078,310 B1, filed 2004-05-19, granted 2006-07-18.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7078310>
[^pat-mim-stack-tsmc]: K.-L. Chang, C.-Y. Lee and C.-H. Chen (Taiwan
    Semiconductor Manufacturing Co.), *High density MIM capacitor
    structure and fabrication process*, US 7,317,221 B2, filed
    2003-12-04, granted 2008-01-08.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7317221>
[^bohr-1995]: M. T. Bohr, "Interconnect scaling — the real limiter to
    high performance ULSI", *IEDM 1995 Technical Digest*, pp. 241–244.
    <https://doi.org/10.1109/IEDM.1995.499187>
[^stamper-1998]: A. K. Stamper, M. B. Fuselier and X. Tian, "Advanced
    wiring RC delay issues for sub-0.25-micron generation CMOS", *Proc.
    IEEE 1998 International Interconnect Technology Conference (IITC)*,
    pp. 62–64. <https://doi.org/10.1109/IITC.1998.704752>
[^itrs-02]: International Technology Roadmap for Semiconductors, *2001
    Edition: Interconnect*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Interconnect.pdf>
[^ames-1970]: I. Ames, F. M. d'Heurle and R. E. Horstmann, "Reduction of
    Electromigration in Aluminum Films by Copper Doping", *IBM Journal
    of Research and Development* **14**(4), 461–463 (1970).
    <https://doi.org/10.1147/rd.144.0461>
[^knorr-1996]: D. B. Knorr and K. P. Rodbell, "The role of texture in
    the electromigration behavior of pure aluminum lines", *Journal of
    Applied Physics* **79**(5), 2409–2417 (1996).
    <https://doi.org/10.1063/1.361168>
[^kamoshida-1997]: K. Kamoshida and Y. Ito, "Highly preferred (111)
    texture aluminum-copper films formed with argon plasma treatment
    of the titanium underlayer and their electromigration endurance as
    interconnects", *Journal of Vacuum Science & Technology B*
    **15**(4), 961–966 (1997). <https://doi.org/10.1116/1.589515>
[^blech-1976]: I. A. Blech, "Electromigration in thin aluminum films on
    titanium nitride", *Journal of Applied Physics* **47**(4), 1203–1208
    (1976). <https://doi.org/10.1063/1.322842>
[^filippi-1993]: R. G. Filippi, G. A. Biery and M. H. Wood, "Evidence of
    the Electromigration Short-Length Effect in Aluminum-Based Metallurgy
    with Tungsten Diffusion Barriers", *MRS Proceedings* **309** (1993).
    <https://doi.org/10.1557/PROC-309-141>
[^nix-1992]: W. D. Nix and E. Arzt, "On void nucleation and growth in
    metal interconnect lines under electromigration conditions",
    *Metallurgical Transactions A* **23**(7), 2007–2013 (1992).
    <https://doi.org/10.1007/BF02647548>
[^chaudhari-1974]: P. Chaudhari, "Hillock growth in thin films",
    *Journal of Applied Physics* **45**(10), 4339–4346 (1974).
    <https://doi.org/10.1063/1.1663054>
[^zlatanovic-1990]: D. Zlatanović and G. Davinić, "Influence of
    heat-treatment temperature and aluminum thickness on hillocks
    formation in thin aluminum films", *Vacuum* **40**(1–2), 157–159
    (1990). <https://doi.org/10.1016/0042-207X(90)90144-N>
[^rocke-1988]: M. Rocke and M. Schneegans, "Titanium nitride for
    antireflection control and hillock suppression on aluminum silicon
    metallization", *Journal of Vacuum Science & Technology B* **6**(4),
    1113–1115 (1988). <https://doi.org/10.1116/1.584306>
[^yue-1985]: J. T. Yue, W. P. Funsten and R. V. Taylor, "Stress
    Induced Voids in Aluminum Interconnects During IC Processing",
    *23rd International Reliability Physics Symposium* (1985),
    pp. 126–137. <https://doi.org/10.1109/IRPS.1985.362087>
[^stoney-1909]: G. G. Stoney, "The tension of metallic films deposited
    by electrolysis", *Proceedings of the Royal Society of London A*
    **82**(553), 172–175 (1909). <https://doi.org/10.1098/rspa.1909.0021>
[^greenwood-2007]: B. B. Greenwood and J. Prasad, "Integrating TiN only
    bottom plate metal-insulator metal capacitor (MIMC) for contamination
    free manufacturing", *2007 International Semiconductor Device
    Research Symposium (ISDRS)*, pp. 1–2.
    <https://doi.org/10.1109/ISDRS.2007.4422363>
[^amat-endura]: Applied Materials, *Endura PVD*, product page.
    <https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html>
[^rossnagel-1991]: S. M. Rossnagel, D. Mikalsen, H. Kinoshita and
    J. J. Cuomo, "Collimated magnetron sputter deposition", *Journal of
    Vacuum Science & Technology A* **9**(2), 261–265 (1991).
    <https://doi.org/10.1116/1.577531>
[^rossnagel-1998]: S. M. Rossnagel, "Directional and ionized physical
    vapor deposition for microelectronics applications", *Journal of
    Vacuum Science & Technology B* **16**(5), 2585–2608 (1998).
    <https://doi.org/10.1116/1.590242>
[^pat-tiw-hitachi]: Hitachi Metals, *Titanium-tungsten target material
    for sputtering and manufacturing method therefor*, US 5,160,534 A,
    granted 1992-11-03.
    <https://patents.google.com/patent/US5160534A/en>
[^thornton-1974]: J. A. Thornton, "Influence of apparatus geometry and
    deposition conditions on the structure and topography of thick
    sputtered coatings", *Journal of Vacuum Science and Technology*
    **11**(4), 666–670 (1974). <https://doi.org/10.1116/1.1312732>
[^ohring-2002]: M. Ohring, *Materials Science of Thin Films*, 2nd ed.,
    Academic Press, 2002.
    <https://doi.org/10.1016/B978-0-12-524975-1.X5000-9>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing". <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^wiki-em]: Wikipedia, *Electromigration*.
    <https://en.wikipedia.org/wiki/Electromigration>
[^wiki-sputter]: Wikipedia, *Sputter deposition*.
    <https://en.wikipedia.org/wiki/Sputter_deposition>
[^wiki-interconnect]: Wikipedia, *Interconnect (integrated circuits)*.
    <https://en.wikipedia.org/wiki/Interconnect_(integrated_circuits)>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
