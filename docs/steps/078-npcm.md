(step-078)=
# Step 078 — NPCM: Nitride poly cut mask

| | |
|---|---|
| **Step number** | 78 of 171[^steps-sheet] |
| **Step code** | `NPCM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | FEOL — extensions, spacers, source/drain |
| **Previous step** | {ref}`SPE <step-077>` |
| **Next step** | {ref}`NPCME <step-079>` |

## What this step is

`NPCM` is the lithography step for the *nitride poly cut*: the resist
pattern that tells {ref}`NPCME <step-079>` where to remove the nitride
that (on our reading) has covered the poly since
{ref}`GATENIT <step-058>`. The wafer arriving from
{ref}`SPE <step-077>` carries gates and resistor bodies that are, on
our reading of the flow, still capped by about 0.2 µm of nitride/oxide
("poly cap after SPE"[^pdk-03]) and flanked by the new nitride
spacers. Nothing can be contacted through that cap, so before the
local-interconnect contacts ({ref}`LICM1 <step-093>`) can land on poly
the cap must be opened where they will land. `NPCM` prints those
openings.

The mask is one of the best-documented in the public PDK. The mask
table lists "Nitride Poly Cut, NPCM" as used in SKY130,[^pdk-05] the
drawn layer is `npc` (GDS 95:20, "Nitride poly cut (under licon1
areas)") and the generated mask layer is `cnpc` (49:0, "Nitride poly
cut mask").[^pdk-06] The periphery rules head the `npc` section with
its function — "Defines nitride openings to contact poly and Li1" —
and give: minimum width 0.270 µm (npc.1), minimum space 0.270 µm
(npc.2), a manual-merge instruction below minimum (npc.3), spacing
with no overlap to a gate of 0.090 µm (npc.4), and a maximum
enclosure of poly overlapping a slotted `licon` by `npcm` of 0.095 µm
(npc.5).[^pdk-periph] The contact rules complete the picture: a
`poly_licon` "must be enclosed by npc by" 0.100 µm (licon.15), "Npc
must enclose poly_licon" (licon.18), `npc` must keep 0.090 µm from a
`licon` on diffusion or tap (licon.13), and a `poly_licon` must keep
0.110 µm from `psdm` (licon.9).[^pdk-periph] The precision-resistor
rules require the resistor to be enclosed by `npc` by 0.095 µm
(rpm.5).[^pdk-periph] The minimum-CD table repeats the 0.27 µm
feature and space (`NPCMCD`, `NPCMCDSP`).[^pdk-03]

## Step category

`NPCM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *cut* type: a dark-field layer of isolated openings whose
own dimensions are relaxed (0.27 µm) but whose *placement* is not.
The 0.090 µm "spacing, no overlap" to a gate (npc.4)[^pdk-periph]
means that an opening printed 0.09 µm out of position over a poly line
would expose the gate edge to the nitride etch, so the layer's overlay
to poly ({ref}`P1M <step-061>`) is its critical parameter, not its
CD.

## Why this step exists

The reason for a separate nitride-cut mask follows from the way the
SKY130 poly is capped. Because the nitride deposited at
{ref}`GATENIT <step-058>` stays on the poly through the gate etch,
the tip module and the spacer etch, every poly surface that a contact
must touch has to be opened deliberately. The PDK says exactly where:
"under licon1 areas".[^pdk-06] Three things depend on the opening
being a separate mask rather than part of the contact etch:

* **Poly contacts through a nitride cap.** The local-interconnect
  contact `licon1` (66:44, "Contact to local interconnect"[^pdk-06])
  is etched at {ref}`LICM1E <step-094>` through the PSG and any cap
  oxide. If the nitride under the contact were still present, the
  contact etch would need a second chemistry and would risk the
  gate-edge charging that Cacciato et al. saw when a borderless
  nitride became conductive.[^cacciato-2003] Opening the nitride
  first, with a dedicated mask, lets the contact etch stop on oxide
  and poly alike. The concept of a nitride layer over poly that is
  opened only under contacts goes back to the titanium-nitride local
  interconnect processes of Tang et al.[^tang-1985][^tang-1987]
* **Doping the poly under the cut.** `NPCM` comes *before* the
  source/drain implants. Poly exposed by the cut is therefore
  implanted by {ref}`PSDI <step-082>`/{ref}`2PSDI <step-083>` where
  it lies inside `psdm`, and by {ref}`NSDI <step-086>` inside `nsdm`.
  The rules make sense on that reading: a precision resistor must be
  enclosed by `psdm` (rpm.4) *and* by `npc` (rpm.5) and kept away from
  `nsdm` (rpm.6),[^pdk-periph] so its contact heads receive the P⁺
  implant through the cut and become low-resistance ends to a lightly
  doped p-type body — the PDK's rule licon.9 checks the
  `poly_licon`–`psdm` spacing "only between (poly_licon outside rpm)
  and psdm" in several flows,[^pdk-periph] which is what one expects
  if the P⁺ implant into resistor heads is intended and the same
  implant into ordinary n⁺ poly contacts is not. This is an inference
  from the rule text; no public source states it.
* **Keeping the gates sealed.** npc.4 forbids the cut over any gate
  with a 0.090 µm margin.[^pdk-periph] The gates therefore keep their
  cap through the source/drain implants, which is the basis of the
  reading (see {ref}`P1I <step-050>` and {ref}`GATENIT <step-058>`)
  that the SKY130 gates are n⁺ on both NMOS and PMOS and are not
  doped by the source/drain implants.

The layer also affects the resistor bank uniformity that Tsang et al.
studied for high-value poly resistors, since the cut defines where the
resistor ends begin.[^tsang-2014] Without `NPCM` the poly could not be
contacted at all.

## How it is typically performed

An industry-generic cut-layer lithography sequence for a 200 mm,
130 nm-era fab (SKY130's recipe is not public):

1. **Surface preparation.** The wafer is topographic: roughly 0.4 µm-tall (0.18 µm poly plus the ~0.2 µm cap[^pdk-03])
   capped poly lines with nitride spacers on a planar oxide. A
   dehydration bake and HMDS prime on the track.[^txt-02]
2. **Resist and BARC.** A 0.27 µm opening over reflective, stepped
   topography calls for a bottom anti-reflective coating and a DUV
   resist of the order of 0.5–0.7 µm (industry-typical for a
   248 nm cut layer[^txt-05][^mack-2007]); the PDK's nominal
   "Photoresist thickness" of 1.14 µm[^pdk-03] is, we infer, the
   implant-layer value rather than this layer's. The resist need only
   withstand a short nitride etch.
3. **Exposure.** At 0.27 µm minimum feature and space, an i-line
   stepper of NA 0.6 would work at k₁ = 0.27 × 0.6 / 0.365 ≈ 0.44,
   close to the "0.4 for production" limit;[^wiki-litho] a 248 nm
   tool gives k₁ ≈ 0.65 with margin for overlay-driven proximity
   effects. ITRS 2001 assigns 248 nm to the critical layers of the
   130 nm node.[^itrs-03] We therefore infer a **DUV** exposure for
   `NPCM`, driven by its 0.09 µm placement tolerance to poly rather
   than by its CD. Whether the tool is a stepper or a scanner is not
   public; SkyWater lists both.[^skw-01]
4. **Alignment.** To the poly layer ({ref}`P1M <step-061>`), since
   npc.4 and licon.15 are both poly-referenced.[^pdk-periph] Overlay
   budgets and how they are allocated are treated by
   Levinson[^levinson-2005] and, for alignment-mark placement, by
   van Haren et al.[^van-haren-2019]
5. **Post-exposure bake and develop** in 2.38 % (0.26 N) TMAH;[^txt-02]
   after-develop CD and overlay measurement on box-in-box targets
   against poly; the dose/focus process window is characterised the
   way Bossung[^bossung-1977] and Ausschnitt[^ausschnitt-1999]
   describe.
6. **Inspection.** After-develop inspection for missing or bridged
   openings, which would become open contacts or exposed gates.

## Machines typically used

* **{ref}`DUV (KrF, 248 nm) stepper or scanner <machine-duv-krf-stepper>`**, 200 mm: ASML PAS 5500/300–/750
  series, Nikon NSR-S20x, Canon FPA-3000EX ({ref}`category-lithography`);
  an **{ref}`i-line stepper <machine-i-line-stepper>`** is the alternative if the layer is relaxed.
* **{ref}`Coat/develop track <machine-coat-develop-track>`** (TEL, DNS/SCREEN, Sokudo) with BARC and DUV
  resist modules.
* **{ref}`Overlay metrology <machine-cd-sem-overlay-metrology>`** (KLA-Tencor 5xxx/Archer) and **CD-SEM**.

## Machines likely used at SkyWater

* **ASML DUV stepper / DUV scanner.** SkyWater lists "ASML DUV
  stepper" and "ASML DUV scanner" beside its i-line tools.[^skw-01]
  Strength: **strong** for the existence of the tools; the assignment
  of `NPCM` to DUV is an **inference** from the design rules.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius**.[^skw-01]
  Strength: strong for existence.
* **Overlay — KLA 5200/5300/Archer; CD — AMAT Verity/VeraSEM**.[^skw-01]
  Strength: strong for existence (SkyWater statement); use at this
  mask is an inference.

## Resources required

* **DUV (chemically amplified) or i-line photoresist** and **organic
  BARC**; SkyWater's 2021 S-1 names Dow, JSR and Tokyo Ohka Kogyo as resist
  suppliers.[^sec-01]
* **HMDS**, **2.38 % (0.26 N) TMAH developer**,[^txt-02] edge-bead remover,
  rinse solvents, DI water and nitrogen.
* **The NPCM reticle** — generated from the `cnpc` mask layer
  (49:0).[^pdk-06]

## Related steps and cross-references

* Previous: {ref}`SPE <step-077>`; next: {ref}`NPCME <step-079>`
  (the etch through this resist, which also strips it).
* The cap being opened: {ref}`GATENIT <step-058>`,
  {ref}`POC <step-059>`; the spacer beside the opening:
  {ref}`SPNIT <step-076>`.
* What the opening is for: {ref}`LICM1 <step-093>`,
  {ref}`LICM1E <step-094>`; what is implanted through it:
  {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`.
* Resistors whose heads it defines: {ref}`RPM <step-049>`,
  {ref}`URPM <step-055>`, {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`.
* Previous mask: {ref}`LDNTM <step-071>`; next mask:
  {ref}`PSDM <step-081>`.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "Nitride Poly Cut,
  NPCM, X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `npc` 95:20
  "Nitride poly cut (under licon1 areas)"; `cnpc` 49:0; `licon1`
  66:44.[^pdk-06]
* SkyWater PDK, *Periphery rules* — npc.1–npc.5; licon.9, licon.13,
  licon.15, licon.18; rpm.4–rpm.6.[^pdk-periph]
* SkyWater PDK, *Criteria & Assumptions* — `NPCMCD` 0.27 µm; "poly cap
  after SPE" 0.2 µm; photoresist thickness 1.14 µm.[^pdk-03]
* SkyWater, *Facilities & Capabilities* — ASML DUV stepper and
  scanner; tracks; metrology.[^skw-01]
* SkyWater, Form S-1 (2021) — photoresist suppliers.[^sec-01]

### High-level understanding

* Wikipedia, *Photolithography* — k₁, wavelengths, resolution.[^wiki-litho]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography fundamentals.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — DUV
  lithography and BARC in the 0.25–0.13 µm generations.[^txt-05]

### Deep dive

* Tang et al. (Texas Instruments), IEDM 1985 and *IEEE TED* 1987 —
  the TiN local-interconnect scheme in which a nitride over poly is
  opened only where contacts are made.[^tang-1985][^tang-1987]
* Cacciato et al., P2ID 2003 — charging damage when a contact etch
  meets a borderless nitride.[^cacciato-2003]
* Ito et al. (NEC), IEDM 2000 — what a nitride over the gate does to
  the transistor, the film this mask cuts.[^ito-2000]
* Tsang et al., *IEEE TSM* 2014 — resistance variation across
  high-value poly resistor banks, whose ends the cut defines.[^tsang-2014]
* ITRS 2001, *Lithography* — exposure wavelength and overlay
  requirements by node.[^itrs-03]
* Mack, *Fundamental Principles of Optical Lithography* — k₁, BARC
  and process windows.[^mack-2007]
* Levinson, *Principles of Lithography* — overlay budgets and layer
  assignment.[^levinson-2005]
* Bossung, SPIE 1977 — the focus–exposure process window.[^bossung-1977]
* Ausschnitt, SPIE 1999 — separating dose from defocus in
  production.[^ausschnitt-1999]
* van Haren et al., SPIE 2019 — alignment-mark placement and
  layer-to-layer overlay.[^van-haren-2019]
* Brunner, *IBM J. Res. Dev.* 1997 — lens aberrations and their
  effect on printed features.[^brunner-1997]

## Open questions

* The exposure tool (i-line or DUV, stepper or scanner), resist and
  BARC used for `NPCM` are inferred from the design rules, not
  stated.
* Whether the reticle is generated from `npc` with additions for
  resistor heads and other structures, or copies the drawn layer, is
  not public; the `cnpc` mask layer exists,[^pdk-06] which shows only
  that it is generated.
* The reading that the P⁺ source/drain implant is *intended* to dope
  the resistor heads through the cut is an inference from rpm.4,
  rpm.5 and licon.9.[^pdk-periph]
* Whether the cut also opens nitride on top of *diffusion* anywhere
  (licon.13 keeps it 0.090 µm from diffusion contacts,[^pdk-periph]
  suggesting not) is not stated.

<!-- footnotes -->

[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007,
    ISBN 978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
    (companion site <https://www.lithoguru.com/textbook/>)
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^bossung-1977]: J. W. Bossung, "Projection Printing Characterization",
    *Proc. SPIE* **100**, 80–85 (1977).
    <https://doi.org/10.1117/12.955357>
[^ausschnitt-1999]: C. P. Ausschnitt, "Distinguishing dose from
    defocus for in-line lithography control", *Proc. SPIE* **3677**,
    Metrology, Inspection, and Process Control for Microlithography
    XIII, 140 (1999). <https://doi.org/10.1117/12.350800>
[^van-haren-2019]: R. J. F. van Haren, S. Steinert, O. Mouraille,
    K. D'havé, L. van Dijk, J. Hermans and D. Beyer, "Wafer alignment
    mark placement accuracy impact on the layer-to-layer overlay
    performance", *Proc. SPIE* **11148**, Photomask Technology 2019, 37
    (2019). <https://doi.org/10.1117/12.2536270>
[^brunner-1997]: T. A. Brunner, "Impact of lens aberrations on optical
    lithography", *IBM Journal of Research and Development* **41**(1.2),
    57–67 (1997). <https://doi.org/10.1147/rd.411.0057>
[^tang-1985]: T. E. Tang, C.-C. Wei, R. A. Haken, T. C. Holloway,
    C.-F. Wan and M. A. Douglas, "VLSI local interconnect level using
    titanium nitride", *IEDM 1985 Technical Digest*, pp. 590–593.
    <https://doi.org/10.1109/IEDM.1985.191041>
[^tang-1987]: T. E. Tang, C.-C. Wei, R. A. Haken, T. C. Holloway,
    L. R. Hite and T. G. W. Blake, "Titanium nitride local interconnect
    technology for VLSI", *IEEE Transactions on Electron Devices*
    **34**(3), 682–688 (1987). <https://doi.org/10.1109/T-ED.1987.22980>
[^cacciato-2003]: A. Cacciato, A. Scarpa, S. Evseev and M. Diekema,
    "Charging damage during contact etch triggered by increased
    borderless nitride conductivity", *Proc. 2003 8th International
    Symposium on Plasma- and Process-Induced Damage*, pp. 20–23.
    <https://doi.org/10.1109/PPID.2003.1199721>
[^ito-2000]: S. Ito, H. Namba, K. Yamaguchi, T. Hirata, K. Ando,
    S. Koyama, S. Kuroki, N. Ikezawa, T. Suzuki, T. Saitoh and
    T. Horiuchi, "Mechanical stress effect of etch-stop nitride and its
    impact on deep submicron transistor design", *IEDM 2000 Technical
    Digest*, pp. 247–250. <https://doi.org/10.1109/IEDM.2000.904303>
[^tsang-2014]: Y. Tsang, R. Shiono, G. Pfeffer and S. Kwan,
    "Characterization and Understanding of High Valued Polysilicon
    Resistor Resistance Variation Across a Resistor Bank With Parallel
    Resistor Fingers", *IEEE Transactions on Semiconductor
    Manufacturing* **27**(2), 294–300 (2014).
    <https://doi.org/10.1109/TSM.2014.2311375>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
