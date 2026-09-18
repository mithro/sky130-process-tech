(step-134)=
# Step 134 — WTIAL3: AlCu 2/TiW deposition

| | |
|---|---|
| **Step number** | 134 of 171[^steps-sheet] |
| **Step code** | `WTIAL3` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | BEOL — via 1, metal 2, via 2 |
| **Previous step** | {ref}`WCMP4 <step-133>` |
| **Next step** | {ref}`CAPILD <step-135>` |

## What this step is

`WTIAL3` deposits the metal-3 film stack — the first *thick* metal
of the flow. Onto the polished cap oxide and tungsten via-2 plugs left
by {ref}`WCMP4 <step-133>` a sputtering cluster tool lays down, in one
vacuum sequence on our reading, a thin refractory bottom layer, a
much thicker aluminium–copper alloy than at metals 1 and 2, and a
refractory cap. The stack is blanket and stays blanket for
longer than any other metal in the flow: before {ref}`MM3 <step-139>`
and {ref}`MM3E <step-140>` pattern it into the `met3` layer (GDS
70:20, "Metal 3"[^pdk-06]), the MiM capacitor module of
{ref}`CAPILD <step-135>`, {ref}`CAPTIW1 <step-136>`,
{ref}`CAPM <step-137>` and {ref}`CAPME <step-138>` is built on top of
it, so that the `capm` plate — "MiM capacitor plate over
metal 3"[^pdk-06] — sits on this stack's cap and the patterned
metal 3 becomes the capacitor's bottom electrode.

The public description of the stack is again the Cypress
qualification reports, and here they show two versions. The 2013
report for a 64 K nvSRAM family on "S8TNV-5R" technology gives
"Metal 3: 150A Ti / 7200A Al -0.5%Cu / 300A TiW", a 7 650 Å
(0.765 µm) stack against the 3 600 Å of its metals 1 and
2;[^cyp-qtp-113005] the 2014 metal-stack-change report gives, for the
S8DI technology, "Metal 3: 500A TiW/21,250A Al 0.5% Cu/300A TiW", a
22 050 Å (2.2 µm) stack with a TiW rather than a Ti bottom layer, and
notes that the S8P change excluded "top metal layers".[^cyp-qtp-123907]
Both reports describe three-metal processes — S8TNV-5R ("3
Metal")[^cyp-qtp-113005] and S8DI ("1P3M")[^cyp-qtp-123907] — in
which metal 3 is the top metal; applying their metal-3 descriptions to
SKY130's intermediate metal 3, under two further metals, is our
inference. The PDK matches both in its own way. Its stack diagram labels `met3`
0.845 µm[^pdk-04] and its extraction tables give metals 3 and 4
47 mΩ/sq against 125 mΩ/sq for metals 1 and 2;[^pdk-08] 0.8 µm of
aluminium alloy at 47 mΩ/sq implies a resistivity of about
3.8 µΩ·cm, the expected range for sputtered Al–0.5%Cu (typical
industry value;[^txt-02] our arithmetic). Its assumptions table lists
a "Metal 3 thickness for antenna ratio calculations" of 0.85 µm for
"S8T* other than S8TM*", 0.8 µm for the SP8T, S8P and S8Q flows, and
2 µm for the "S8TM* flow"; its minimum-CD table gives "Metal 3-PLM"
0.3 µm, "Metal 3-TLM" 0.36 µm and "Metal 3-S8TM" 0.8 µm, with a
matching "Via 2-S8TM" of 0.8 µm;[^pdk-03] and its mask table lists
the `MM3` mask three times, flagging only the PLM variant for
SKY130.[^pdk-05] On our reading, then, the flow described here
deposits a metal 3 of about 0.8 µm, and a 2 µm "S8TM" thick-metal
option exists whose via 2 and metal 3 differ; whether its bottom layer
matches the TiW-bottomed top metal of the 2014 S8DI report — a
different technology — is not public, and any such match would be an
inference. The metal-3 rules are coarser than the levels
below: 0.300 µm width and space (m3.1, m3.2), 0.240 µm² minimum area
(m3.6), and 0.065 µm enclosure of via 2 (m3.4).[^pdk-periph]

**On the cap.** Which refractory film caps this stack is not public,
and the same two reports point different ways. The 2013 S8TNV-5R
description gives a 300 Å TiW cap at every level, and the R7FT-3R
report the same at its thick metal 3;[^cyp-qtp-113005][^cyp-qtp-014807]
the 2014 report records the S8P metal stack as qualified for a change
"from Ti/AlCu/TiW to Ti/TiN/ALCu/Ti/TiN, excluding top metal
layers",[^cyp-qtp-123907] and in a five-metal S8P flow metal 3 is not a
top metal layer — a via connects it to metal 4.[^pdk-periph] Against
that, the PDK's 0.845 µm for `met3` exceeds its 0.8 µm antenna
thickness by exactly the 450 Å of titanium plus TiW that clad the
Cypress stacks, where the 2014 stack's cladding is 990 Å (our
arithmetic).[^pdk-03][^pdk-04] That argument has its own counter-check:
the same table's 0.85 µm for "S8T\* other than S8TM\*" exceeds the whole
7 650 Å of the 2013 report's S8TNV-5R metal 3 by about a tenth (our
arithmetic), so its antenna entries are not uniformly derived from film
thicknesses.[^pdk-03][^cyp-qtp-113005] This reference describes the cap as
"TiW or TiN" and writes its recipes for the TiW case; the whole of the
evidence, the counter-checks and the statements that depend on the
choice are set out under {ref}`overview-metal-cap`. This module is
where the choice matters most, because the cap is also the MiM
capacitor's bottom-electrode surface
({ref}`CAPILD <step-135>`, {ref}`CAPME <step-138>`).

**On the bottom layer.** The public evidence allows a TiW bottom
layer as well as a Ti one: the S8DI thick metal 3 of the 2014 report
is "500A TiW/…/300A TiW",[^cyp-qtp-123907] and an older Fab 4 process
used "TiW, AlCu, TiW" at 500/6 000/300 Å,[^cyp-qtp-030204] while the
S8TNV report's 150 Å Ti bottom layer[^cyp-qtp-113005] points to
titanium for the thin version. The step list used in this reference
does not explain its labels for this and the upper metal stacks
({ref}`WTIAL4 <step-149>`, {ref}`WTIAL5 <step-161>`), and they are not
taken here as evidence either way. We describe the bottom layer as
"Ti or TiW" (inference).

## Step category

`WTIAL3` is a {ref}`Thin-film deposition <category-deposition>` step
of the *PVD, multi-layer metal* class; {ref}`TIAL6 <step-112>` sets
out the sputtering of Ti, Al–Cu and Ti:W films and the reasons for
each layer, and {ref}`TIAL12 <step-123>` what a via level adds. What
is specific to this instance is thickness. Sputtering 0.72 µm of
aluminium alloy takes more than twice as long as the 0.32 µm of the
lower levels (and a 2 µm thick-metal option[^pdk-03] longer still),
heats the wafer more, grows larger grains, and stores more stress; the film's
hillocks, its wafer bow and its later etch ({ref}`MM3E <step-140>`)
all scale with it. And the stack must serve as a capacitor electrode:
its cap is the surface on which {ref}`CAPILD <step-135>` deposits
the MiM dielectric, so its roughness and its chemistry set the
capacitor's leakage and matching as much as the dielectric does.

## Why this step exists

Metal 3 is the flow's first coarse-pitch, low-resistance level; the
reasons for each film are those of metal 1, and the thickness adds
its own:

* **Low resistance for power and long signals.** At 47 mΩ/sq[^pdk-08]
  a metal-3 wire has less than two-fifths the resistance per square
  of a metal-1 or metal-2 wire, and at 0.3 µm width and space
  (m3.1, m3.2[^pdk-periph]) it is meant for block-level routing,
  clocks and power. Bohr's 1995 argument that interconnect limits
  performance,[^bohr-1995] Stamper, Fuselier and Tian's account of
  wiring RC at the sub-0.25 µm generation[^stamper-1998] and the ITRS
  2001 interconnect chapter's treatment of aluminium
  metallisation[^itrs-02] are the context; thick, wide upper metals
  are how an aluminium back end keeps global wires fast.
* **Thick metal for inductors and RF.** A 2 µm top-side metal is the
  classic route to a high-quality-factor spiral inductor on silicon,
  as Chu et al. showed for thick top metal with different passivation
  schemes;[^chu-2001] the PDK's "inductor-capable" option[^pdk-02]
  and its thick-metal thickness entries[^pdk-03] are, on our reading,
  the SKY130 form of that trade.
* **Electromigration in wide, thick lines.** Copper doping,[^ames-1970]
  the (111) texture a refractory underlayer promotes,[^knorr-1996][^kamoshida-1997]
  and the tungsten vias that bound each segment — the short-length
  effect Filippi, Biery and Wood demonstrated[^filippi-1993] after
  Blech's critical length[^blech-1976] — all apply; Nix and Arzt
  describe void nucleation and growth in such lines,[^nix-1992] and
  May, and Martin and McPherson, the via electromigration of
  Ti:W/Al–Cu multilayer metallisation.[^may-1991][^martin-1989]
* **Hillocks and stress in a thick film.** Hillock growth in
  aluminium films — Chaudhari's analysis[^chaudhari-1974] — and its
  dependence on film thickness and heat treatment, which Zlatanović
  and Davinić measured,[^zlatanovic-1990] make a thick Al–Cu film more
  prone to hillocks than a thin one; the refractory cap suppresses them and
  serves as the anti-reflective surface for {ref}`MM3 <step-139>`, the
  role Rocke and Schneegans documented.[^rocke-1988] Stress-induced
  voiding, described by Yue, Funsten and Taylor,[^yue-1985] and the
  wafer bow a thick film produces (Stoney's relation[^stoney-1909]) are
  the other thickness penalties.
* **TiW as bottom layer and cap.** Ghate et al.'s Ti:W barrier
  metallisation,[^ghate-1978] its reaction kinetics with aluminium
  measured by Olowolafe et al.,[^olowolafe-1985] Hartsough's
  resistivity data for sputtered TiW[^hartsough-1979] and Georgiou,
  Baker and Eshraghi's deposition-condition study[^georgiou-1991] are
  the public basis for a TiW-based sandwich; Armstrong evaluated the
  electromigration of the TiW + Al/Cu system.[^armstrong-1991]
* **The MiM bottom electrode.** The stack's cap becomes the bottom
  plate of the `cap_mim` device the PDK offers at 2 fF/µm²;[^pdk-07]
  Greenwood and Prasad describe the alternative of a TiN-only bottom
  plate for a MiM capacitor integrated in an aluminium back
  end,[^greenwood-2007] which shows what the plate material must
  provide.

Without `WTIAL3` there is no metal 3, no bottom plate for the MiM
capacitor, and the via-2 plugs would end in air.

## How it is typically performed

An industry-generic thick Ti(W)/Al–Cu/TiW deposition for a 200 mm,
130 nm-era fab (SKY130's recipe is not public beyond the layer
thicknesses in the Cypress reports[^cyp-qtp-113005][^cyp-qtp-123907]);
the film-by-film account is at {ref}`TIAL6 <step-112>`.

1. **Cluster tool.** A multi-chamber PVD platform — SkyWater's "AMAT
   PVD Metal" with "Sputter etch, degas"[^skw-01] — so that degas,
   pre-clean and the depositions happen without an air break; the
   Endura is the 200 mm-era Applied Materials platform.[^amat-endura]
2. **Degas and pre-clean.** A vacuum bake, then a light argon sputter
   etch to remove the tungsten oxide from the via-2 plug tops and any
   post-CMP residue (industry practice[^txt-05]).
3. **Bottom layer, 150 Å Ti or 500 Å TiW.** Per the two Cypress
   descriptions;[^cyp-qtp-113005][^cyp-qtp-123907] titanium collimated
   or ionised,[^rossnagel-1991][^rossnagel-1998] or Ti:W from a 10 wt.%
   Ti target.[^pat-tiw-hitachi]
4. **Al–0.5%Cu, 7 200 Å (or 21 250 Å).** Sputtered from an
   Al–Cu target (the Cypress reports give the film as Al-0.5%Cu) at a wafer temperature of roughly 150–300 °C
   (industry-typical[^txt-02]); a thick film is usually deposited in
   several passes or with a cooled pedestal so that the wafer does
   not drift into the hillock and copper-precipitation regime (industry
   practice[^txt-05]); grain size and texture follow the
   structure-zone relations.[^thornton-1974][^ohring-2002]
   Thicknesses per the Cypress reports.[^cyp-qtp-113005][^cyp-qtp-123907]
5. **Cap, 300 Å.** On the TiW reading, from a Ti:W
   target[^pat-tiw-hitachi] in argon; thickness per the Cypress
   reports.[^cyp-qtp-113005][^cyp-qtp-123907] On the 2014 stack it is
   90 Å of titanium and 500 Å of reactively sputtered TiN
   instead[^cyp-qtp-123907] (*On the cap*, above).
   Its surface must be smooth and clean enough to carry the MiM
   dielectric of {ref}`CAPILD <step-135>` (inference from the module
   order).
6. **Metrology.** Sheet resistance of the stack by
   {term}`four-point probe` (the PDK's 47 mΩ/sq[^pdk-08] is the target
   such a stack reads after the back-end anneals); thickness by XRF
   or profilometry; reflectivity; stress by wafer bow — a larger
   number than at the thin levels; particles.

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
  films; the platform model (Endura[^amat-endura]) and the choice of
  Ti or TiW as bottom layer are **inferences**.
* **Metal etchers "Lam 9600, Al, TiW, TiN, Pt" and "Lam 2300 Versys,
  Al, TiW, TiN, Nb, Pt"**[^skw-01] name aluminium, TiW and TiN among the
  materials they etch, so either candidate stack is etchable in the fab
  as publicly described (used at {ref}`MM3E <step-140>`).

## Resources required

* **{ref}`Sputter targets <material-sputter-targets>`** — titanium, Al–0.5%Cu and Ti:W (10 wt.%
  Ti[^pat-tiw-hitachi]); SkyWater's filings name Honeywell Electronic
  Materials (2021 S-1 and fiscal 2023 10-K) and JX Metals (fiscal 2023 10-K)
  as sputter-target suppliers.[^sec-01][^sec-02] A thick metal consumes
  Al–Cu targets several times faster per wafer than the thin levels.
* **{ref}`Argon <material-process-gases>`** for sputtering and pre-clean; **nitrogen** for venting. Gas
  suppliers named in SkyWater's filings: Air Products and Praxair (2021
  S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]
* **{ref}`Chamber shields <material-hardware-consumables>`, clamps and electrostatic-chuck consumables**,
  changed more often for a thick film.
* **{ref}`Monitor wafers <material-substrates>`** for sheet resistance, reflectivity, stress and
  particles.

## Related steps and cross-references

* Previous: {ref}`WCMP4 <step-133>` (the plugs and oxide it lands
  on). Next: {ref}`CAPILD <step-135>` (the MiM dielectric deposited on
  this stack), then {ref}`CAPTIW1 <step-136>`, {ref}`CAPM <step-137>`,
  {ref}`CAPME <step-138>`, and only then the metal-3 mask and etch,
  {ref}`MM3 <step-139>` and {ref}`MM3E <step-140>`.
* The plugs it contacts: {ref}`TIN4 <step-131>`, {ref}`WDEP4 <step-132>`.
* The dielectric that will surround the lines: {ref}`NILD5 <step-141>`;
  the via etch that stops on the cap: {ref}`VIM3E <step-145>`.
* The thin stacks below, where the films are explained in full:
  {ref}`TIAL6 <step-112>`, {ref}`TIAL12 <step-123>`; the upper thick
  metals: {ref}`WTIAL4 <step-149>`, {ref}`WTIAL5 <step-161>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* Cypress, QTP 113005 (2013) — S8TNV-5R "Metal 3: 150A Ti / 7200A
  Al -0.5%Cu / 300A TiW".[^cyp-qtp-113005]
* Cypress, QTP 123907/132302/132301 (2014) — S8DI "Metal 3: 500A
  TiW/21,250A Al 0.5% Cu/300A TiW"; the S8P change "excluding top
  metal layers".[^cyp-qtp-123907]
* Cypress, QTP 030204 (2013) — RAM42HA at Fab 4: TiW/AlCu/TiW
  500/6 000/300 Å.[^cyp-qtp-030204]
* SkyWater PDK, *Process stack diagram* — `met3` 0.845 µm; met3
  bottom 2.7861 µm.[^pdk-04]
* SkyWater PDK, *Criteria & Assumptions* — metal 3 thickness 0.8,
  0.85 and 2 µm by flow; `MM3CD` 0.3/0.36/0.8 µm; `VIM2CD` 0.8 µm for
  S8TM.[^pdk-03]
* SkyWater PDK, *Masks* — "Metal 3-TLM", "Metal 3-S8TM", "Metal
  3-PLM", all `MM3`; PLM flagged.[^pdk-05]
* SkyWater PDK, *Parasitic Layout Extraction* — metal 3–4 47 mΩ/sq;
  metal 1–2 125 mΩ/sq.[^pdk-08]
* SkyWater PDK, *Layers Reference* — `met3` 70:20; `capm` 89:44.[^pdk-06]
* SkyWater PDK, *Periphery rules* — m3.1, m3.2, m3.4, m3.6.[^pdk-periph]
* SkyWater PDK, *Background* and *Device Details* — the
  inductor-capable option; the MiM capacitor at 2 fF/µm².[^pdk-02][^pdk-07]
* SkyWater, *Facilities & Capabilities* — "AMAT PVD Metal" film
  list; metal etchers.[^skw-01]
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

* Chu et al., VLSI-TSA 2001 — thick top metal for high-Q spiral
  inductors on silicon.[^chu-2001]
* Bohr (Intel), IEDM 1995, and Stamper, Fuselier and Tian (IBM), IITC
  1998 — interconnect scaling and wiring RC delay.[^bohr-1995][^stamper-1998]
* ITRS 2001, *Interconnect* — aluminium metallisation at the 130 nm
  generation.[^itrs-02]
* Zlatanović and Davinić, *Vacuum* 1990, and Chaudhari (IBM), *J.
  Appl. Phys.* 1974 — hillock formation versus aluminium film
  thickness and heat treatment.[^zlatanovic-1990][^chaudhari-1974]
* Yue, Funsten and Taylor, IRPS 1985 — stress-induced voids in
  aluminium interconnects.[^yue-1985]
* Stoney, *Proc. R. Soc. A* 1909 — film stress from wafer
  curvature.[^stoney-1909]
* Rocke and Schneegans (Siemens), *JVST B* 1988 — a refractory cap
  for anti-reflection and hillock suppression.[^rocke-1988]
* Ghate et al. (TI), 1978; Olowolafe et al., 1985; Hartsough, 1979;
  Georgiou, Baker and Eshraghi, 1991 — Ti:W as barrier and cap: its
  reaction with aluminium, resistivity and deposition
  conditions.[^ghate-1978][^olowolafe-1985][^hartsough-1979][^georgiou-1991]
* Armstrong, 1991; May, IRPS 1991; Martin and McPherson, VMIC 1989 —
  electromigration of TiW/Al–Cu multilayer metallisation and its
  vias.[^armstrong-1991][^may-1991][^martin-1989]
* Ames, d'Heurle and Horstmann, 1970; Blech, 1976; Filippi, Biery
  and Wood, 1993; Nix and Arzt, 1992 — copper doping, the critical
  length, the short-length effect with tungsten barriers, and void
  growth.[^ames-1970][^blech-1976][^filippi-1993][^nix-1992]
* Knorr and Rodbell, 1996, and Kamoshida and Ito, 1997 — texture and
  the refractory underlayer.[^knorr-1996][^kamoshida-1997]
* Thornton, *JVST* 1974 — the structure-zone model for thick sputtered
  films.[^thornton-1974]
* Rossnagel et al., 1991, and Rossnagel, 1998 — collimated and
  ionised PVD for the thin underlayer.[^rossnagel-1991][^rossnagel-1998]
* Greenwood and Prasad, ISDRS 2007 — a TiN-only bottom plate for a
  MiM capacitor in an aluminium back end.[^greenwood-2007]

## Open questions

* Whether the metal-3 bottom layer is Ti or TiW is not public; the
  S8TNV report gives Ti,[^cyp-qtp-113005] and a TiW bottom layer is
  our inference from the S8DI and RAM42HA stack
  descriptions.[^cyp-qtp-123907][^cyp-qtp-030204]
* Whether the cap is TiW or the Ti/TiN of the stack qualified for S8P
  in February 2014 "excluding top metal layers" is not public, and
  neither is which levels of a five-metal S8P flow that exclusion
  covers;[^cyp-qtp-123907] see {ref}`overview-metal-cap`. The answer
  changes what {ref}`CAPME <step-138>` can stop on and what
  {ref}`VIM3E <step-145>` lands on.
* Whether the SKY130 metal 3 is the 0.765 µm Ti/AlCu/TiW stack of the
  S8TNV report,[^cyp-qtp-113005] the 0.845 µm of the PDK's
  diagram,[^pdk-04] or the 0.8–0.85 µm of its assumptions
  table[^pdk-03] — and how the difference arises — is not public.
* Whether the 2 µm "S8TM" option[^pdk-03] is offered in SKY130 as
  published is not clear: the mask table does not flag the S8TM
  variants of `MM3` and `VIM2`,[^pdk-05] and the 2014 report's 2.2 µm
  metal 3 belongs to the S8DI technology.[^cyp-qtp-123907]
* Deposition temperatures, pressures, powers and whether the thick
  Al–Cu is deposited in one pass or several are not public.
* What the MiM dielectric of {ref}`CAPILD <step-135>` requires of
  this stack's cap — and whether the cap is treated before it — is
  not public.

<!-- footnotes -->

[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
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
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^cyp-qtp-030204]: Cypress Semiconductor, *Automotive Product
    Qualification Report, QTP# 030204: 256K Static RAM Automotive
    Devices, RAM42HA Technology, Fab 4*, document 001-88023 Rev. **,
    June 2013 (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030204-256k-static-ram-automotive-devices-ram42ha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714980870ac1>
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
[^chu-2001]: S.-F. Chu, K. W. Chew, W. B. Loh, Y. M. Wang, B. G. Onn,
    Y. Ju, J. Zhang and K. Shao, "High quality factor silicon-integrated
    spiral inductors achieved by using thick top metal with different
    passivation schemes", *2001 International Symposium on VLSI
    Technology, Systems, and Applications (VLSI-TSA)*, pp. 154–157.
    <https://doi.org/10.1109/VTSA.2001.934506>
[^pdk-02]: SkyWater PDK Authors, *Background*, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/background.html>
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
[^filippi-1993]: R. G. Filippi, G. A. Biery and M. H. Wood, "Evidence of
    the Electromigration Short-Length Effect in Aluminum-Based Metallurgy
    with Tungsten Diffusion Barriers", *MRS Proceedings* **309** (1993).
    <https://doi.org/10.1557/PROC-309-141>
[^blech-1976]: I. A. Blech, "Electromigration in thin aluminum films on
    titanium nitride", *Journal of Applied Physics* **47**(4), 1203–1208
    (1976). <https://doi.org/10.1063/1.322842>
[^nix-1992]: W. D. Nix and E. Arzt, "On void nucleation and growth in
    metal interconnect lines under electromigration conditions",
    *Metallurgical Transactions A* **23**(7), 2007–2013 (1992).
    <https://doi.org/10.1007/BF02647548>
[^may-1991]: J. S. May, "Electromigration Characteristics of Vias in
    Ti:W/Al-Cu (2wt%) Multilayered Metallization", *29th International
    Reliability Physics Symposium (IRPS 1991)*, pp. 91–96.
    <https://doi.org/10.1109/IRPS.1991.363216>
[^martin-1989]: C. A. Martin and J. W. McPherson, "Via electromigration
    performance of Ti/W/Al-Cu(2%) multilayered metallization", *Proc.
    Sixth International IEEE VLSI Multilevel Interconnection Conference
    (VMIC 1989)*, pp. 168–175. <https://doi.org/10.1109/VMIC.1989.78063>
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
[^ghate-1978]: P. B. Ghate, J. C. Blair, C. R. Fuller and G. E.
    McGuire, "Application of Ti:W barrier metallization for integrated
    circuits", *Thin Solid Films* **53**(2), 117–128 (1978).
    <https://doi.org/10.1016/0040-6090(78)90024-X>
[^olowolafe-1985]: J. O. Olowolafe, C. J. Palmstrøm, E. G. Colgan and
    J. W. Mayer, "Al/TiW reaction kinetics: Influence of Cu and
    interface oxides", *Journal of Applied Physics* **58**(9),
    3440–3443 (1985). <https://doi.org/10.1063/1.335764>
[^hartsough-1979]: L. D. Hartsough, "Resistivity of bias-sputtered TiW
    films", *Thin Solid Films* **64**(1), 17–23 (1979).
    <https://doi.org/10.1016/0040-6090(79)90536-4>
[^georgiou-1991]: G. E. Georgiou, M. Baker and S. A. Eshraghi, "Effect of
    sputtered TiW deposition conditions on barrier properties for
    submicron metallization", *Proc. Eighth International IEEE VLSI
    Multilevel Interconnection Conference (VMIC 1991)*, pp. 420–422.
    <https://doi.org/10.1109/VMIC.1991.153044>
[^armstrong-1991]: N. P. Armstrong, "Evaluation of TiW + Al/Cu
    electromigration performance", *Quality and Reliability Engineering
    International* **7**(4), 281–286 (1991).
    <https://doi.org/10.1002/qre.4680070414>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, section "MiM capacitors" (CMIMA 2 fF/µm² nominal).
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^greenwood-2007]: B. B. Greenwood and J. Prasad, "Integrating TiN only
    bottom plate metal-insulator metal capacitor (MIMC) for contamination
    free manufacturing", *2007 International Semiconductor Device
    Research Symposium (ISDRS)*, pp. 1–2.
    <https://doi.org/10.1109/ISDRS.2007.4422363>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^amat-endura]: Applied Materials, *Endura PVD*, product page.
    <https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
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
[^cyp-qtp-014807]: Cypress Semiconductor, *Technology Derivative
    Qualification Report, QTP# 014807 Version 2.0: Technology Derivative
    R7FT-3R, Fab4, Synchronous Dual-Port RAM*, June 2005 (copy hosted by
    Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
