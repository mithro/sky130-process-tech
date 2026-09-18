(step-047)=
# Step 047 — LVGOX: Gate oxidation

| | |
|---|---|
| **Step number** | 47 of 171[^steps-sheet] |
| **Step code** | `LVGOX` |
| **Category** | {ref}`Thermal oxidation <category-oxidation>` |
| **Phase** | FEOL — SONOS and gate dielectrics |
| **Previous step** | {ref}`GOXETCH <step-046>` |
| **Next step** | {ref}`SAGD <step-048>` |

## What this step is

`LVGOX` grows the thin gate oxide of the 1.8 V transistors — the
*low-voltage gate oxide* — on the silicon that
{ref}`GOXETCH <step-046>` cleared. It is the last step before the gate
electrode is deposited at {ref}`SAGD <step-048>`, and the film it grows
is the one every `nfet_01v8` and `pfet_01v8` switches through. At the
same time the thick oxide left over the 5 V and high-voltage regions
grows a little thicker, and the {term}`ONO` islands of the memory cells see
the same ambient. If the oxide is nitrided — which SkyWater's
"Nitrided gate oxide" special module makes likely[^skw-01] — the
nitridation belongs here too.

The public numbers: the 1.8 V NMOS model carries `toxe = 4.148e-9`
(4.148 nm) as its oxide thickness for electrical
purposes,[^pdk-model-nfet01v8] against 11.6 nm for the 5 V
device;[^pdk-model-nfet5v] the PDK rates the 1.8 V models to
V<sub>GS</sub> of 1.95 V.[^pdk-07] Measured capacitance gives a
consistent figure. The PDK's varactors are "1.8V accumulation-mode
MOS varactors", with "no equivalent varactor for 5V
operation",[^pdk-07] so we read them as built on this oxide. The
SKY130 raw-data repository publishes capacitance–voltage sweeps of the
test tile's `cap_var_lvt` and `cap_var_hvt` structures, five sizes of
each from one 40 × 40 µm device to 462 devices of 5 × 0.5 µm, whose
dimensions the pad list gives.[^raw-data-testtile-pads][^raw-data-passives]
Splitting the accumulation capacitance at 1.8 V into an area and an
edge term gives 8.52 fF/µm² (low-Vt; raw-data module 3320, as the pad
list names it) and 8.40 fF/µm² (high-Vt; raw-data module 3316); for a
relative permittivity of 3.9 these correspond to an electrical
thickness of about 4.06 nm and 4.11 nm (our extraction from the
published measurements, without corrections for gate depletion, the
thickness of the accumulation layer or pad and wiring capacitance, so
not a physical thickness; the files record neither the measurement
frequency nor the temperature).[^raw-data-passives] For comparison,
ITRS 2001 lists an
equivalent oxide thickness of 2.0–2.4 nm for low-operating-power and
2.4–2.8 nm for low-standby-power logic in 2001, with a thickness
control requirement of "<± 4" % 3σ;[^itrs-01] SKY130's oxide is
thicker because its core runs at 1.8 V rather than the roadmap's
scaled supply. Cypress's integration patent puts its thin gate
insulator at "between approximately 3.0 nm and 8.0 nm" against
5–15 nm for the thick one,[^pat-03] and its later cell patent grows
"a thin, second gate oxide 246 having a thickness from about 1 nm to
about 3 nm"[^pat-04] — for a more advanced node than SKY130.

## Step category

`LVGOX` is a {ref}`Thermal oxidation <category-oxidation>` step of
the *thin gate oxide* class, grown in the regime where "very thin
oxides (less than about 25 nanometres) grow much more quickly in O₂
than the model predicts"[^wiki-dg] and where recipes are calibrated on
the tool rather than from {term}`Deal–Grove <Deal–Grove model>`.[^massoud-1985] It is the second
pass of the {term}`dual-gate-oxide <dual gate oxide>` process and, in a 130 nm flow, generally
the most tightly controlled oxidation (ITRS 2001 asks for EOT control
of "<± 4" % 3σ on the gate dielectric[^itrs-01]; SKY130 publishes no
control data). The category page's *Nitrided oxides and ONO
stacks* section gives the background on nitridation.

## Why this step exists

The 1.8 V core needs a gate oxide thin enough for drive current and
short-channel control at a 0.15 µm gate length[^pdk-periph] and thick
enough not to leak or break: a gate oxide "serves as the dielectric
layer so that the gate can sustain as high as 1 to 5 MV/cm transverse
electric field in order to strongly modulate the conductance of the
channel".[^wiki-gate-oxide] At 4 nm the direct-tunnelling gate leakage
that dominates below ~3 nm[^lo-1997] is still small, and the reliability
limits of thin oxides[^stathis-2002][^wright-1990] leave margin at
1.8 V. Buchanan's review lays out the trade-offs of scaling the gate
dielectric,[^buchanan-1999] and Green et al. the processing and physical
limits of sub-4 nm SiO₂ and Si–O–N films.[^green-2001]

**Why thin second.** In general, a thin gate oxide tolerates subsequent
processing worse than a thick one: every furnace step thickens it
proportionally more, every HF exposure thins it by a larger fraction,
every implant through it damages it more severely (a generality about
dual-gate-oxide flows; SKY130 publishes no process-sensitivity data of
its own). Growing it
last in the gate-dielectric module, on freshly cleaned silicon, after
the thick oxide has absorbed the long oxidation and the masked etch,
gives it the smallest thermal and chemical history
({ref}`category-oxidation`). The price is that the thick oxide grows
further during this step — in the parabolic Deal–Grove regime, where
the increment is small and calculable[^deal-1965] — so the
{ref}`GOX100 <step-043>` target is set with this growth included.

**Why nitrided.** By the 130 nm node "most gate oxides were lightly
nitrided" ({ref}`category-oxidation`), and ITRS 2001 expected the
"evolution of the oxynitride gate dielectric materials" to continue
until high-κ matured.[^itrs-01] Nitrogen near the top of the oxide
blocks boron from a p⁺ polysilicon gate from diffusing through into
the channel — "the effects of boron penetration on p⁺ polysilicon
gated PMOS devices" were quantified by Pfiester et al.[^pfiester-1990]
and modelled for N₂O {term}`oxynitrides <oxynitride>` by Hwang et al.[^hwang-1991] — and
nitrogen also reduces hot-carrier degradation and raises the dielectric
constant slightly.[^hori-1997][^hori-1989] SkyWater lists "Nitrided gate
oxide" among its special modules,[^skw-01] and Cypress's integration
patent nitrides its gate insulators and the ONO together, "heating
substrate 302 in an atmosphere including nitrogen at a temperature
approximately in the range of 900-1100° C." to incorporate
"approximately 4-10 wt % nitrogen".[^pat-03] Whether SKY130's 1.8 V
oxide is nitrided is not stated publicly; we infer that it is, from
the special-module listing and the Cypress lineage.

## How it is typically performed

An industry-generic thin gate oxidation for a 200 mm, 130 nm-era fab
(SKY130's recipe is not public):

1. **Load.** Straight from the pre-gate clean ({ref}`GOXETCH <step-046>`)
   into a vertical furnace under nitrogen, or into a single-wafer {term}`RTP`
   chamber; queue time is limited.
2. **Oxidation.** Dry O₂ at 750–900 °C to about 4 nm (industry-typical
   range),[^txt-01] often with a dilute-oxygen or reduced-pressure
   ambient to slow the growth to a controllable rate in the thin
   regime;[^massoud-1985] alternatives are N₂O or NO ambients, which
   grow and nitride at once, and rapid thermal oxidation, whose early
   demonstration for thin gate dielectrics is Nulman's,[^nulman-1985] or
   in-situ steam generation.[^yu-1999][^roze-2017] Cypress describes the
   thick oxide by "dilute wet oxidation" at 800–900 °C[^pat-03] and the
   thin one by "a thermal oxidation process".[^pat-04]
3. **Nitridation** (inferred). Three public routes: thermal
   nitridation in NH₃, the original direct-nitridation technique
   (Ito, Nozaki and Ishikawa),[^ito-1980] which incorporates hydrogen
   and needs a reoxidation;[^hori-1989] rapid thermal nitridation in NO
   or N₂O, which places nitrogen at the interface;[^kuehne-1997] or
   plasma nitridation, which puts nitrogen at the *top* surface where
   it blocks boron without degrading the interface — the remote-plasma
   method of Hattangady et al.[^hattangady-1995] and the high-density
   plasma surface nitridation of Kraft et al.[^kraft-1997] Cypress's
   patent lists "nitrogen (N₂), nitrous oxide (N₂O), nitrogen dioxide
   (NO₂), nitric oxide (NO) and ammonia (NH₃)" as its nitriding
   atmospheres at 900–1100 °C.[^pat-03]
4. **Post-oxidation anneal.** Inert N₂ or Ar anneal to reduce fixed
   charge and interface traps;[^deal-1980] a post-nitridation anneal
   in O₂ or N₂ heals plasma damage if plasma nitridation is used.
5. **Unload and gate deposition.** The oxide is covered by the
   amorphous-silicon gate at {ref}`SAGD <step-048>` as soon as
   possible, since a 4 nm oxide's surface is easily contaminated.
6. **Metrology.** Spectroscopic ellipsometry (repeatability typically of
   order 0.1 nm) on monitor wafers and on product test sites; C–V for
   electrical thickness and nitrogen-induced flat-band shift; ITRS
   2001's "<± 4" % 3σ control[^itrs-01] is the era's target.

## Machines typically used

* **{ref}`Vertical oxidation furnace <machine-vertical-furnace-oxidation>`**, 200 mm, with dry O₂, N₂O/NO and
  NH₃ capability: ASM A400, TEL Alpha-8, Aviza/Thermco
  ({ref}`category-oxidation`).
* **{ref}`Single-wafer RTP/RTO/RTN <machine-rapid-thermal-processor>`** chamber: Applied Materials RTP
  Centura, AG Associates Heatpulse.[^nulman-1985]
* **{ref}`Plasma nitridation <machine-plasma-nitridation-chamber>`** chamber (decoupled or remote plasma) if the
  oxide is plasma-nitrided.[^kraft-1997][^hattangady-1995]
* **{ref}`Spectroscopic ellipsometer <machine-film-thickness-metrology>`**; **{ref}`C–V <machine-parametric-tester>`** test.

## Machines likely used at SkyWater

* **Aviza vertical furnaces** — "wet oxidation to 1150C", "dry
  oxidation to 1150C".[^skw-01] Strength: **strong** for the tool;
  **inference** for the assignment to `LVGOX`.
* **AG Associates Heatpulse 8808** — "NH3, Ar, N2, O2, up to
  1200C".[^skw-01] An RTP with ammonia and oxygen is a rapid thermal
  oxidation/nitridation tool; its NH₃ capability is one public route
  by which a nitrided gate oxide could be produced in this fab.
  Strength: strong for existence; **weak** for assignment.
* **"Nitrided gate oxide"** is listed by SkyWater as a special
  module.[^skw-01] The listing shows that SkyWater offers nitrided
  gate oxide as a capability; it does not say which process or which
  product uses it. Strength: strong for the capability; inference for
  its use on SKY130's 1.8 V oxide.

## Resources required

* **{ref}`Oxygen <material-process-gases>`**, **nitrogen/argon**; if the oxide is nitrided, **N₂O, NO or {ref}`NH₃ <material-precursors>`**
  ({ref}`category-oxidation`); the Heatpulse 8808's listed gases are
  NH₃, Ar, N₂ and O₂.[^skw-01]
* **HCl or DCE** as chlorine source for furnace oxidation
  ({ref}`category-oxidation`).
* **{ref}`Quartz tubes <material-hardware-consumables>`, boats, liners**; **{ref}`monitor wafers <material-substrates>`**.
* Gas suppliers named in SkyWater's filings: Air Products and Praxair
  (2021 S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`GOXETCH <step-046>` (silicon cleared and cleaned).
* Next: {ref}`SAGD <step-048>` (amorphous-silicon gate deposition).
* The thick oxide that grows further here: {ref}`GOX100 <step-043>`;
  the mask that decided which is which: {ref}`LVOM <step-044>`.
* The ONO islands, nitrided or reoxidised alongside:
  {ref}`ONO <step-040>`.
* The channel implants this oxidation anneals: {ref}`NCHI <step-045>`,
  {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`.
* Category page: {ref}`Thermal oxidation <category-oxidation>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,851,892 A <patent-gp25314008>` — Fabrication sequence employing an oxide formed with minimized inducted charge and/or maximized breakdown voltage (1997)

:::{dropdown} 2 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 8,093,128 B2 <patent-gp40072804>` — in force
* {ref}`US 8,796,098 B1 <patent-gp51229009>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, SPICE models of `nfet_01v8` and `nfet_g5v0d10v5` —
  `toxe` 4.148 nm and 11.6 nm.[^pdk-model-nfet01v8][^pdk-model-nfet5v]
* SkyWater PDK, *Device Details* — 1.8 V device operating
  voltages; "1.8V accumulation-mode MOS varactors".[^pdk-07]
* SKY130 raw-data repository — C–V sweeps of the test tile's
  varactors and the pad list that gives their sizes; the area
  capacitance and electrical thickness quoted here are our
  extraction.[^raw-data-passives][^raw-data-testtile-pads]
* SkyWater, *Facilities & Capabilities* — Aviza furnaces; Heatpulse
  8808 with NH₃; "Nitrided gate oxide" special module.[^skw-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]
* Koutny et al. (Cypress), US 8,093,128 — thin versus thick gate
  insulator thicknesses; nitridation at 900–1100 °C with 4–10 wt %
  nitrogen; nitriding gases.[^pat-03]
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — the
  thin second gate oxide grown by thermal oxidation.[^pat-04]
* ITRS 2001, *Front End Processes* — {term}`EOT` targets and thickness
  control; oxynitride evolution.[^itrs-01]

### High-level understanding

* Wikipedia, *Gate oxide* — role and field strength.[^wiki-gate-oxide]
* Wikipedia, *Deal–Grove model* — the thin-oxide deviation.[^wiki-dg]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — ch. 6,
  thermal oxidation.[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — gate
  dielectrics of the deep-submicron era.[^txt-05]

### Deep dive

* Green, Gusev, Degraeve and Garfunkel, *J. Appl. Phys.* 2001 — the
  review of ultrathin SiO₂ and Si–O–N gate dielectrics.[^green-2001]
* Hori, *Gate Dielectrics and MOS ULSIs* — the monograph on gate
  oxides and nitrided oxides.[^hori-1997]
* Hori, Iwasaki and Tsuji, *IEEE TED* 1989 — ultrathin reoxidised
  nitrided oxides by rapid thermal processing.[^hori-1989]
* Ito, Nozaki and Ishikawa, *J. Electrochem. Soc.* 1980 — direct
  thermal nitridation of SiO₂ in ammonia.[^ito-1980]
* Hattangady, Niimi and Lucovsky, *Appl. Phys. Lett.* 1995 —
  controlled nitrogen incorporation at the gate-oxide surface.[^hattangady-1995]
* Kraft et al., *JVST B* 1997 — surface nitridation of SiO₂ with a
  high-density nitrogen plasma.[^kraft-1997]
* Kuehne et al., MRS 1997 — nitric oxide rapid thermal nitridation of
  thin gate oxides.[^kuehne-1997]
* Pfiester et al., *IEEE TED* 1990 — {term}`boron penetration` through thin
  oxides from p⁺ poly gates.[^pfiester-1990]
* Hwang, Ting, Kwong and Lee, *Appl. Phys. Lett.* 1991 — a physical
  model of boron penetration through N₂O oxynitride.[^hwang-1991]
* Tseng et al. (Motorola), IEDM 1998 — reduced leakage and boron
  penetration with an RTCVD oxynitride at 0.18 µm.[^tseng-1998]
* Massoud, Plummer and Irene, *J. Electrochem. Soc.* 1985 — thin-regime
  growth kinetics.[^massoud-1985]
* Deal and Grove, *J. Appl. Phys.* 1965 — the oxidation law.[^deal-1965]
* Deal, *J. Electrochem. Soc.* 1980 — oxide-charge terminology.[^deal-1980]
* Nulman, Krusius and Gat, *IEEE EDL* 1985 — rapid thermal oxidation
  of thin gate dielectrics.[^nulman-1985]
* Yu et al. (TSMC), SPIE 1999 and Rozé et al., *J. Appl. Phys.* 2017 —
  {term}`ISSG` oxidation and its kinetics.[^yu-1999][^roze-2017]
* Lo, Buchanan, Taur and Wang, *IEEE EDL* 1997 — tunnelling current
  through ultrathin oxides.[^lo-1997]
* Stathis, *IBM J. Res. Dev.* 2002 — reliability limits of the gate
  insulator.[^stathis-2002]
* Buchanan, *IBM J. Res. Dev.* 1999 — scaling the gate dielectric:
  materials, integration, reliability.[^buchanan-1999]
* Wright and Saraswat, *IEEE TED* 1990 — thickness limitations of SiO₂
  gate dielectrics.[^wright-1990]
* Ma, *IEEE TED* 1998 — silicon nitride as a gate dielectric, the
  nitrogen-rich end of the spectrum.[^ma-1998]

## Open questions

* The physical thickness of the 1.8 V gate oxide is not public; the
  model's 4.148 nm `toxe` is an electrical-model parameter, and the
  4.06–4.11 nm from the published varactor measurements is an
  uncorrected electrical figure.[^raw-data-passives]
* Whether the oxide is nitrided, and by which method (NH₃, N₂O/NO,
  or plasma), is inferred from SkyWater's special-module listing and
  the Cypress lineage, not stated.
* Furnace versus RTO, temperature, ambient and time are not public.
* How much the thick oxide grows during this step, and hence the
  {ref}`GOX100 <step-043>` target, is not public.
* Whether the ONO {term}`blocking oxide` is nitrided together with the gate
  oxides, as in the Cypress patent, is not public.

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
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
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
[^wiki-dg]: Wikipedia, *Deal–Grove model*.
    <https://en.wikipedia.org/wiki/Deal%E2%80%93Grove_model>
[^massoud-1985]: H. Z. Massoud, J. D. Plummer and E. A. Irene,
    "Thermal Oxidation of Silicon in Dry Oxygen: Growth-Rate
    Enhancement in the Thin Regime. I. Experimental Results", *Journal
    of The Electrochemical Society* **132**(11), 2685–2693 (1985).
    <https://doi.org/10.1149/1.2113648>
[^wiki-gate-oxide]: Wikipedia, *Gate oxide*.
    <https://en.wikipedia.org/wiki/Gate_oxide>
[^lo-1997]: S.-H. Lo, D. A. Buchanan, Y. Taur and W. Wang,
    "Quantum-mechanical modeling of electron tunneling current from
    the inversion layer of ultra-thin-oxide nMOSFET's", *IEEE Electron
    Device Letters* **18**(5), 209–211 (1997).
    <https://doi.org/10.1109/55.568766>
[^stathis-2002]: J. H. Stathis, "Reliability limits for the gate
    insulator in CMOS technology", *IBM Journal of Research and
    Development* **46**(2.3), 265–286 (2002).
    <https://doi.org/10.1147/rd.462.0265>
[^wright-1990]: P. J. Wright and K. C. Saraswat, "Thickness
    limitations of SiO₂ gate dielectrics for MOS ULSI", *IEEE
    Transactions on Electron Devices* **37**(8), 1884–1892 (1990).
    <https://doi.org/10.1109/16.57140>
[^buchanan-1999]: D. A. Buchanan, "Scaling the gate dielectric:
    Materials, integration, and reliability", *IBM Journal of Research
    and Development* **43**(3), 245–264 (1999).
    <https://doi.org/10.1147/rd.433.0245>
[^green-2001]: M. L. Green, E. P. Gusev, R. Degraeve and
    E. L. Garfunkel, "Ultrathin (<4 nm) SiO₂ and Si–O–N gate dielectric
    layers for silicon microelectronics: Understanding the processing,
    structure, and physical and electrical limits", *Journal of Applied
    Physics* **90**(5), 2057–2121 (2001).
    <https://doi.org/10.1063/1.1385803>
[^deal-1965]: B. E. Deal and A. S. Grove, "General Relationship
    for the Thermal Oxidation of Silicon", *Journal of Applied Physics*
    **36**(12), 3770–3778 (1965). <https://doi.org/10.1063/1.1713945>
[^pfiester-1990]: J. R. Pfiester, F. K. Baker, T. C. Mele, H.-H. Tseng,
    P. J. Tobin, J. D. Hayden, J. W. Miller, C. D. Gunderson and
    L. C. Parrillo, "The effects of boron penetration on p⁺
    polysilicon gated PMOS devices", *IEEE Transactions on Electron
    Devices* **37**(8), 1842–1851 (1990). <https://doi.org/10.1109/16.57135>
[^hwang-1991]: H. Hwang, W. Ting, D.-L. Kwong and J. Lee, "A physical
    model for boron penetration through an oxynitride gate dielectric
    prepared by rapid thermal processing in N₂O", *Applied Physics
    Letters* **59**(13), 1581–1582 (1991).
    <https://doi.org/10.1063/1.106290>
[^hori-1997]: T. Hori, *Gate Dielectrics and MOS ULSIs: Physics,
    Technology and Applications*, Springer Series in Electronics and
    Photonics, vol. 34, Springer, 1997.
    <https://doi.org/10.1007/978-3-642-60856-8>
[^hori-1989]: T. Hori, H. Iwasaki and K. Tsuji, "Electrical and
    physical properties of ultrathin reoxidized nitrided oxides prepared
    by rapid thermal processing", *IEEE Transactions on Electron
    Devices* **36**(2), 340–350 (1989). <https://doi.org/10.1109/16.19935>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^nulman-1985]: J. Nulman, J. P. Krusius and A. Gat, "Rapid thermal
    processing of thin gate dielectrics. Oxidation of silicon", *IEEE
    Electron Device Letters* **6**(5), 205–207 (1985).
    <https://doi.org/10.1109/EDL.1985.26099>
[^yu-1999]: M.-C. Yu, S.-M. Jang, C. H. Diaz, C. H. Yu, S. C. Sun and
    M. S. Liang (TSMC), "Improvement of ultrathin gate oxide by a novel
    rapid thermal oxidation process with in-situ steam generation",
    *Proc. SPIE* **3881**, Microelectronic Device Technology III, 234
    (1999). <https://doi.org/10.1117/12.360557>
[^roze-2017]: F. Rozé, O. Gourhant, E. Blanquet, F. Bertin, M. Juhel,
    F. Abbate, C. Pribat and R. Duru, "Oxidation kinetics of Si and
    SiGe by dry rapid thermal oxidation, in-situ steam generation
    oxidation and dry furnace oxidation", *Journal of Applied Physics*
    **121**(24), 245308 (2017). <https://doi.org/10.1063/1.4987040>
[^ito-1980]: T. Ito, T. Nozaki and H. Ishikawa, "Direct Thermal
    Nitridation of Silicon Dioxide Films in Anhydrous Ammonia Gas",
    *Journal of The Electrochemical Society* **127**(9), 2053–2057
    (1980). <https://doi.org/10.1149/1.2130065>
[^kuehne-1997]: J. Kuehne, S. Hattangady, J. Piccirillo, G. C. Xing,
    G. E. Miner and D. Lopes, "Nitric Oxide Rapid Thermal Nitridation
    of Thin Gate Oxides", *MRS Proceedings* **470**, 381 (1997).
    <https://doi.org/10.1557/PROC-470-381>
[^hattangady-1995]: S. V. Hattangady, H. Niimi and G. Lucovsky,
    "Controlled nitrogen incorporation at the gate oxide surface",
    *Applied Physics Letters* **66**(25), 3495–3497 (1995).
    <https://doi.org/10.1063/1.113775>
[^kraft-1997]: R. Kraft, T. P. Schneider, W. W. Dostalik and
    S. Hattangady, "Surface nitridation of silicon dioxide with a high
    density nitrogen plasma", *Journal of Vacuum Science & Technology
    B* **15**(4), 967–970 (1997). <https://doi.org/10.1116/1.589516>
[^deal-1980]: B. E. Deal, "Standardized terminology for oxide charges
    associated with thermally oxidized silicon", *IEEE Transactions on
    Electron Devices* **27**(3), 606–608 (1980),
    DOI 10.1109/T-ED.1980.19908; published simultaneously in *Journal of
    The Electrochemical Society* **127**(4), 979–981 (1980).
    <https://doi.org/10.1109/T-ED.1980.19908>,
    <https://doi.org/10.1149/1.2129800>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^tseng-1998]: H.-H. Tseng, D. L. O'Meara, P. J. Tobin, V. S. Wang,
    X. Guo, R. Hegde, I. Y. Yang, P. Gilbert et al. (Motorola), "Reduced
    gate leakage current and boron penetration of 0.18 μm 1.5 V
    MOSFETs using integrated RTCVD oxynitride gate dielectric", *IEDM
    1998 Technical Digest*, pp. 793–796.
    <https://doi.org/10.1109/IEDM.1998.746475>
[^ma-1998]: T. P. Ma, "Making silicon nitride film a viable gate
    dielectric", *IEEE Transactions on Electron Devices* **45**(3),
    680–690 (1998). <https://doi.org/10.1109/16.661229>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
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
