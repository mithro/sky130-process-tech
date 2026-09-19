(step-009)=
# Step 009 — DNIS: High V deep N-well implant strip

| | |
|---|---|
| **Step number** | 9 of 171[^steps-sheet] |
| **Step code** | `DNIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | FEOL — isolation |
| **Previous step** | {ref}`DNI <step-008>` |
| **Next step** | {ref}`LINOX <step-010>` |

## What this step is

`DNIS` removes the thick photoresist that masked the deep N-well
implant at {ref}`DNI <step-008>`, and cleans the wafer so that it can
go into the liner-oxidation furnace at {ref}`LINOX <step-010>`. It is
the first of the many *implant strip* steps in this reference, which
pairs almost every implant mask with a strip step. The deep N-well is
associated with the high-voltage device family on the evidence of the
PDK's isolated 20 V NMOS and a Cypress SONOS patent (see
{ref}`DNM <step-007>`).

What makes this strip different from an ordinary post-etch strip is
the state of the resist and of the wafer:

* the resist has been bombarded by MeV phosphorus ions, which
  carbonise its top surface into a hard {term}`crust <implant crust>` that ordinary O₂ {term}`ashing <ash>`
  removes slowly and that can {term}`pop <popping>` or flake during heating;[^orvek-1985][^smith-1983][^txt-02]
* the wafer has open silicon trenches with bare, plasma-damaged
  sidewalls, so the clean must be gentle enough not to roughen or
  etch them, and thorough enough that no organic or metallic residue
  goes into the furnace that follows — a liner oxidation which
  comparable flows run at "900-1100 degrees Celsius".[^pat-sti-cr]

## Step category

`DNIS` is a {ref}`Resist strip / clean <category-strip>` step — an
implant-resist strip followed by a pre-furnace clean. The same
combination recurs after every masked implant
({ref}`LVTNIS <step-016>`, {ref}`PWIS <step-029>`,
{ref}`PDIS <step-084>`, …), but this instance is followed directly by
a high-temperature oxidation, which raises the cleanliness
requirement.

## Why this step exists

Photoresist cannot survive a furnace: it would carbonise, contaminate
the tube and leave the wafer covered in particles. It also holds
mobile-ion and organic contamination that must not reach the
silicon–oxide interface formed at {ref}`LINOX <step-010>`. The strip
therefore has to remove every trace of the resist, the implant crust
and any sputtered material, and the clean has to leave a
hydrophilic, particle-free surface — inside the trenches as well as
on the nitride.

A residue left here would be sealed under the liner oxide and the HDP
fill, where it can cause voids, leakage or gate-oxide defects at the
active edge much later in the flow.

## How it is typically performed

An industry-generic implant-strip sequence for a 200 mm, 130 nm-era
fab:

1. **Plasma ash.** Downstream (remote) microwave or RF O₂ plasma at
   150–270 °C. Fabs commonly use a two-stage recipe for high-dose or
   high-energy implant resist: a low-temperature first stage, often
   with a forming-gas (H₂/N₂) or N₂/O₂ addition, that breaks up the
   carbonised crust without popping, then a hotter O₂ stage to remove
   the bulk resist.[^txt-02][^txt-05] SkyWater's own list describes its
   ashers as "Gasonic PEP, remote microwave plasma, N2, O2, 120C –
   270C" and "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to
   250C"[^skw-01] — the N₂, O₂ and forming-gas set this kind of
   recipe needs.
2. **Wet strip / clean.** Sulphuric-peroxide mixture (H₂SO₄ : H₂O₂,
   "piranha" or {term}`SPM`) at roughly 100–130 °C[^txt-02] to remove the last
   organics, then
   {term}`SC-1` (NH₄OH/H₂O₂/H₂O at 75 or 80 °C) for particles and {term}`SC-2`
   (HCl/H₂O₂/H₂O) for metals.[^wiki-rca] Because the nitride and the
   trench silicon are both exposed, the sequence avoids any long HF
   step that would undercut the pad oxide beneath the nitride (some
   flows do use a controlled short HF dip for exactly that
   reason,[^pat-sti-cr] but that belongs to the liner-oxidation
   preparation and is discussed at {ref}`LINOX <step-010>`).
3. **Rinse and dry.** DI-water rinse and spin or IPA (Marangoni) dry —
   SkyWater lists "spin or IPA dry" for its Akrion
   bench.[^skw-01]
4. **Inspection.** Bright-field or laser-scatter inspection for resist
   residue and particles; sometimes a monitor check of the nitride
   thickness to confirm the clean has not thinned it.

## Machines typically used

* **{ref}`Downstream plasma asher <machine-downstream-plasma-asher>`**, 200 mm single-wafer: GaSonics (Novellus)
  Aura/PEP series, Mattson Aspen, Axcelis/Fusion ES series, PSK.
* **{ref}`Batch wet bench <machine-wet-bench>`** with SPM, SC-1 and SC-2 tanks and a rinser/dryer;
  or a single-wafer spray tool.
* **{ref}`Defect inspection <machine-defect-inspection>`** (patterned-wafer optical inspection).

## Machines likely used at SkyWater

* **"Gasonic PEP", Iridia RF microwave and "Mattson Aspen2" ashers** —
  named on SkyWater's facilities page with their gases and
  temperatures.[^skw-01] Strength: **strong** for existence; the
  assignment of this strip to any one of them is an inference.
* **Akrion Gamma batch wet bench** — SkyWater lists it with sulphuric,
  SC1, phosphoric and {term}`BOE` chemistries and spin and IPA
  drying.[^skw-01] Strength: strong for existence. A sulphuric (SPM) +
  SC-1 sequence on this bench is the natural post-implant clean
  (inference).
* **DNS / FSI Mercury** HF/SC1/SC2 benches[^skw-01] as the pre-furnace
  clean. Strength: strong for existence; the assignment is an inference
  from their HF/SC1/SC2 chemistry, SC-2 being listed only for these two
  benches.
* **Patterned-wafer inspection — KLA-Tencor AIT**, our reading of "AIT"
  in a SkyWater job posting's "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
  Strength: medium.

## Resources required

* **{ref}`Oxygen <material-process-gases>`, nitrogen, {term}`forming gas` ({ref}`H₂/N₂ <material-anneal-ambients>`)** for the
  ash;[^skw-01] **{ref}`CF₄ <material-etch-gases>`**, listed on the Iridia and Mattson ashers,[^skw-01]
  attacks the exposed trench silicon and pad oxide and would, we infer,
  be omitted here (category page).
* **Sulphuric acid and hydrogen peroxide** (SPM; {ref}`wet chemicals <material-wet-chemicals>`).
* **Ammonium hydroxide, hydrochloric acid, hydrogen peroxide**
  (SC-1/SC-2).[^wiki-rca]
* **{ref}`DI water <material-ultrapure-water>`**, **isopropanol** for drying.[^skw-01]
* **Nitrogen** for drying/purge.

## Related steps and cross-references

* Previous: {ref}`DNI <step-008>` (the implant whose resist is
  stripped); mask: {ref}`DNM <step-007>`.
* Next: {ref}`LINOX <step-010>` (liner oxidation — the reason the
  clean must be furnace-grade).
* The next implant strips in the flow: {ref}`LVTNIS <step-016>`,
  {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 6,033,991 A <patent-gp25473825>` — Isolation scheme based on recessed locos using a sloped Si etch and dry field oxidation (1997)
* {ref}`US 7,439,141 B2 <patent-gp26708682>` — Shallow trench isolation approach for improved STI corner rounding (2001)

:::{dropdown} 9 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 6,727,161 B2 <patent-gp24011612>` — unknown
* {ref}`US 8,030,172 B1 <patent-gp44676718>` — unknown
* {ref}`US 6,831,346 B1 <patent-gp33491100>` — unknown
* {ref}`US 6,773,975 B1 <patent-gp32823653>` — unknown
* {ref}`US 6,794,269 B1 <patent-gp32987143>` — unknown
* {ref}`US 7,981,800 B1 <patent-gp44261896>` — unknown
* {ref}`US 9,437,470 B2 <patent-gp52776290>` — unknown
* {ref}`US 9,252,026 B2 <patent-gp54069643>` — unknown
* {ref}`US 10,622,370 B1 <patent-gp50002947>` — unknown
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — "Gasonic PEP"; "Mattson
  Aspen2"; Iridia; Akrion Gamma with sulphuric/SC1/phosphoric/BOE and
  spin/IPA dry; DNS and FSI Mercury HF/SC1/SC2.[^skw-01]
* LinkedIn, SkyWater Defect Technician 2 posting —
  "SEM/AIT/KLA/SP1/EV300/1X".[^job-06]
* Kim et al. (Spansion), US 7,439,141 — pad-oxide undercut of
  100–300 Å before liner oxidation.[^pat-sti-cr]

### High-level understanding

* Wikipedia, *RCA clean* — SC-1 and SC-2 compositions and
  temperatures.[^wiki-rca]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  resist stripping; wafer cleaning.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 —
  implanted-resist stripping.[^txt-05]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — ash and
  wet-clean tools.[^txt-07]

### Deep dive

* Nandakumar et al., IEDM 1998 — the {term}`STI` flow and its defectivity
  drivers.[^rev-01]
* Thung et al., *JTEC* 2016 — the post-trench-etch wet clean in a
  0.13 µm STI module.[^thung-2016]
* Orvek and Huffman, *NIM B* 1985 — the carbonised layer that forms on
  ion-implanted photoresist, the reason implant strips are
  hard.[^orvek-1985]
* Smith, *Ion Implantation: Equipment and Techniques* 1983 — resist
  heating, flow and crust formation during implantation.[^smith-1983]
* Lee et al., IIT 1996 — thick-resist outgassing during MeV
  implantation, which conditions the crust this step
  removes.[^lee-1996]
* Fujimura et al., *Jpn. J. Appl. Phys.* 1990 — the effect of nitrogen
  addition on downstream O₂ ashing, the chemistry behind an N₂/O₂
  first stage.[^fujimura-1990]
* Fujimura et al., *J. Vac. Sci. Technol. B* 1991 — resist stripping in
  an O₂ + H₂O downstream plasma, a low-damage
  alternative.[^fujimura-1991]
* Visintin, Korzenski and Baum, *J. Electrochem. Soc.* 2006 — liquid
  formulations for stripping high-dose implanted resist when ashing
  alone is insufficient.[^visintin-2006]
* Bergman and Leonhard, *Solid State Phenomena* 2009 — wet stripping of
  high-dose implanted resist with sulphur trioxide, a sulphuric-family
  alternative to SPM.[^bergman-2009]
* Kern, *J. Electrochem. Soc.* 1990 — the evolution of the {term}`RCA clean`
  used as the pre-furnace clean.[^kern-1990]
* Ohmi, *J. Electrochem. Soc.* 1996 — room-temperature wet cleaning,
  the later alternative to hot RCA chemistry.[^ohmi-1996]
* Reinhardt and Kern (eds.), *Handbook of Silicon Wafer Cleaning
  Technology* — the reference volume on wet and dry cleaning, resist
  removal and particle control.[^reinhardt-2008]

## Open questions

* The actual SKY130 ash recipe (single or two-stage, temperatures) and
  wet sequence are not public.
* Whether the post-trench-etch polymer clean (see
  {ref}`STIE <step-006>`) is performed here, at `STIE`, or before
  {ref}`DNM <step-007>` is not stated publicly.
* Whether `DNIS` includes the pre-liner-oxidation HF treatment or
  whether that belongs to {ref}`LINOX <step-010>` is unknown.

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^job-06]: LinkedIn, *SkyWater Technology hiring Defect Technician 2 in
    Bloomington, MN* (job posting), retrieved 2026-09-19.
    <https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>
[^pat-sti-cr]: U. Kim, Y. Sun, M. S. Chang et al. (Spansion LLC; later
    Cypress Semiconductor / Infineon), *Shallow trench isolation
    approach for improved STI corner rounding*, US 7,439,141 B2,
    priority 2001-12-27, granted 2008-10-21.
    <https://patents.google.com/patent/US7439141B2/en>
[^wiki-rca]: Wikipedia, *RCA clean*. <https://en.wikipedia.org/wiki/RCA_clean>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^rev-01]: M. Nandakumar, A. Chatterjee, S. Sridhar, K. Joyner,
    M. Rodder and I.-C. Chen, "Shallow trench isolation for advanced
    ULSI CMOS technologies", *IEDM 1998 Technical Digest*, pp. 133–136.
    <https://doi.org/10.1109/IEDM.1998.746297>
[^thung-2016]: B. J. Thung, K. Ibrahim, N. A. Manap and F. Salehuddin,
    "Challenges for 0.13µm Generation Shallow Trench Isolation on
    0.18µm Equipment Platform", *Journal of Telecommunication,
    Electronic and Computer Engineering* **8**(5), 15–21 (2016).
    <https://jtec.utem.edu.my/jtec/article/view/697> (times out as of
    2026-09-19; a Wayback Machine copy from 2026-04-11 confirms it was
    up; the PDF link below still works directly) (PDF:
    <https://jtec.utem.edu.my/jtec/article/download/697/707/3255>).
[^orvek-1985]: K. J. Orvek and C. Huffman, "Carbonized layer formation
    in ion implanted photoresist masks", *Nuclear Instruments and
    Methods in Physics Research B* **7–8**, 501–506 (1985).
    <https://doi.org/10.1016/0168-583X(85)90421-5>
[^smith-1983]: T. C. Smith, "Wafer Cooling and Photoresist Masking
    Problems in Ion Implantation", in *Ion Implantation: Equipment and
    Techniques*, Springer Series in Electrophysics, Springer, 1983,
    pp. 196–213. <https://doi.org/10.1007/978-3-642-69156-0_25>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^fujimura-1990]: S. Fujimura, K. Shinagawa, M. Nakamura and H. Yano,
    "Additive Nitrogen Effects on Oxygen Plasma Downstream Ashing",
    *Japanese Journal of Applied Physics* **29**(10R), 2165 (1990).
    <https://doi.org/10.1143/JJAP.29.2165>
[^fujimura-1991]: S. Fujimura, K. Shinagawa, M. T. Suzuki and
    M. Nakamura, "Resist stripping in an O₂+H₂O plasma downstream",
    *Journal of Vacuum Science & Technology B* **9**(2), 357–361 (1991).
    <https://doi.org/10.1116/1.585575>
[^visintin-2006]: P. M. Visintin, M. B. Korzenski and T. H. Baum,
    "Liquid Clean Formulations for Stripping High-Dose Ion-Implanted
    Photoresist from Microelectronic Devices", *Journal of The
    Electrochemical Society* **153**(7), G591 (2006).
    <https://doi.org/10.1149/1.2195884>
[^bergman-2009]: E. J. Bergman and J. D. Leonhard, "Novel Methods for
    Wet Stripping High Dose Implanted Photoresist Using Sulfur
    Trioxide", *Solid State Phenomena* **145–146**, 281–284 (2009).
    <https://doi.org/10.4028/www.scientific.net/SSP.145-146.281>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^ohmi-1996]: T. Ohmi, "Total Room Temperature Wet Cleaning for Si
    Substrate Surface", *Journal of The Electrochemical Society*
    **143**(9), 2957–2964 (1996). <https://doi.org/10.1149/1.1837133>
[^reinhardt-2008]: K. A. Reinhardt and W. Kern (eds.), *Handbook of
    Silicon Wafer Cleaning Technology*, 2nd ed., William Andrew, 2008,
    ISBN 978-0-8155-1554-8. <https://openlibrary.org/isbn/9780815515548>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
