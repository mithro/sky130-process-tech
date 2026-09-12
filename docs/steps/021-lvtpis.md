(step-021)=
# Step 021 — LVTPIS: P-channel implant strip

| | |
|---|---|
| **Step number** | 21 of 171 |
| **Step code** | `LVTPIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | FEOL — wells and channel implants |
| **Previous step** | {ref}`LVTPI <step-020>` |
| **Next step** | {ref}`HVTPM <step-022>` |

## What this step is

`LVTPIS` removes the thick N-well photoresist that was patterned at
{ref}`NWM <step-017>` and has since masked three implants — the two well
implants (MeV-class phosphorus, we infer) {ref}`NWI <step-018>` and
{ref}`NWI2 <step-019>` and the keV P-channel threshold implant
{ref}`LVTPI <step-020>` — and then cleans the wafer for the next
lithography, {ref}`HVTPM <step-022>`. The step list used in this
reference names it after the last implant it follows ("P-channel implant
strip"); the resist it removes is, we infer, the N-well resist.

This is the hardest strip of the module. The resist is the thickest
in the flow so far (2–3 µm class, inferred on the
{ref}`NWM <step-017>` page), it has been bombarded by high-energy
ions for the longest cumulative time, and the summed dose is of order
10¹³ cm⁻² (illustrative; {ref}`NWI <step-018>`). All three conditions
thicken the carbonised crust and raise the risk of popping. The wafer
surface under the resist is, we infer, still all oxide (pad oxide and trench
oxide), which allows the full SPM/SC-1 sequence.

## Step category

`LVTPIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type; it is the direct analogue of
{ref}`DNIS <step-009>`, which removed the resist of the deep N-well
implant, and shares its recipe considerations.

## Why this step exists

The resist has to go before the next coat, and it has to go completely:
residue over a future high-Vt PMOS region would block the
{ref}`PCHI <step-023>` implant locally and produce a transistor with the
wrong threshold. The crust of an MeV-implanted resist is the obstacle.
Ion bombardment turns "the top portion of the photoresist layer … into a
carbonized crust that is difficult to remove because of its low
solubility in wet strippers";[^pat-strip-tsmc] beneath it the
"subsurface resist generally contains more volatile, shorter molecular
weight polymer" whose vapours "build up pressure beneath the
implant-hardened surface layer" until "this pressure can violently
rupture the skin, an event that spreads particles of the
implant-hardened cross-link hydrogen deficient surface layer material
throughout the stripping chamber".[^pat-strip-mosel] Wikipedia's summary
is that problems arise "when this photoresist has undergone an implant
step previously and heavy metal are embedded in the photoresist and it
has experienced high temperatures causing it to be resistant to
oxidizing".[^wiki-ash]

## How it is typically performed

An industry-generic MeV-implant-resist strip for a 200 mm, 130 nm-era
fab:

1. **Two-stage plasma ash.** A first stage below the popping threshold —
   "removed by oxygen and nitrogen/hydrogen plasma in a low-temperature
   (<220 °C) environment", preferably 150–220 °C[^pat-strip-mosel] —
   until the crust is consumed, then a hotter oxygen stage for the bulk
   of the 2–3 µm film. The forming-gas addition helps because hydrogen
   penetrates and reduces the carbonised layer (category page).
   SkyWater's ashers offer exactly this: "Gasonic PEP, remote microwave
   plasma, N2, O2, 120C – 270C"; "Iridia RF microwave, N2, O2, H2, CF4,
   NH3, H2/N2, 40C-270C"; "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up
   to 250C".[^skw-01] Downstream plasma is used so that the neutral
   atomic oxygen does the work and charged species recombine before
   reaching the wafer.[^wiki-ash] Endpoint on the CO emission line, then
   a timed over-ash.
2. **Wet strip.** SPM (H₂SO₄:H₂O₂, roughly 3:1 to 4:1, self-heated to
   above 100 °C) to dissolve the remaining organics and any popped
   flakes (category page).[^txt-02] SkyWater's Akrion Gamma bench lists
   "Sulfuric".[^skw-01]
3. **Clean.** SC-1 (NH₄OH/H₂O₂/H₂O at 75–80 °C) for particles, SC-2
   (HCl/H₂O₂/H₂O) for the metals that an implanter's beam-line and disc
   can sputter onto the resist.[^wiki-rca] The pad oxide is preserved
   for the remaining implants.
4. **Rinse, dry, inspect.** Cascade rinse, spin or IPA dry; laser
   surface scan and patterned-wafer inspection for flakes.

The resist's thickness also matters for cycle time: at typical
downstream-asher rates of a few micrometres per minute[^txt-07] a thick
implant resist takes noticeably longer than an etch resist, and the
crust stage cannot be hurried.

## Machines typically used

* **Downstream plasma asher** with a two-step, forming-gas-capable
  recipe: Gasonics Aura/PEP, Mattson Aspen, Axcelis/Fusion ES, PSK
  (category page).
* **Batch wet bench** (SPM, SC-1, SC-2) or **spray processor**.
* **Surface scanner / patterned inspection**.

## Machines likely used at SkyWater

* **Gasonics PEP, Iridia RF microwave, Mattson Aspen 2**[^skw-01] — the
  Iridia's "H2/N2" and the Mattson's "H2>N2" options are the forming-gas
  chemistries used for implant crusts. Strength: **strong** for
  existence; assignment is an inference.
* **Akrion Gamma batch wet bench** ("Sulfuric, SC1").[^skw-01] Strength:
  strong for existence.
* **DNS wet bench / FSI Mercury** for HF/SC1/SC2.[^skw-01] Strength:
  strong for existence.
* **KLA-Tencor SP1 and AIT** ("SEM/AIT/KLA/SP1/EV300/1X")[^job-01] for
  particle and residue inspection. Strength: medium.

## Resources required

* **Oxygen, nitrogen, forming gas (H₂/N₂)**; **CF₄** is available but
  attacks the oxide surface and is normally omitted[^skw-01] (category
  page).
* **Sulphuric acid, hydrogen peroxide, ammonium hydroxide, hydrochloric
  acid**[^wiki-rca] (category page).
* **DI water, isopropanol, nitrogen**.
* Chemical suppliers named by SkyWater: KMG Chemicals, EMD Performance
  Materials.[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`LVTPI <step-020>`; the resist came from
  {ref}`NWM <step-017>` and masked {ref}`NWI <step-018>` and
  {ref}`NWI2 <step-019>` as well.
* Next: {ref}`HVTPM <step-022>`.
* The comparable heavy-implant-resist strips are {ref}`DNIS <step-009>` and
  {ref}`PWIS <step-029>`.
* Category page: {ref}`Resist strip / clean <category-strip>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — ashers with gases and
  temperatures; Akrion, DNS, FSI benches.[^skw-01]
* Indeed, SkyWater Technology Foundry listings — the defect-metrology
  tool list "SEM/AIT/KLA/SP1/EV300/1X".[^job-01]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — chemical
  suppliers.[^sec-01][^sec-02]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — the popping
  mechanism and a low-temperature O₂/N₂/H₂ first ash
  stage.[^pat-strip-mosel]
* Chan, Chiu and Tao (TSMC), US 2004/0214448 — the "carbonized crust" of
  implanted resist.[^pat-strip-tsmc]

### High-level understanding

* Wikipedia, *Plasma ashing* — downstream ashing and implanted-resist
  problems.[^wiki-ash]
* Wikipedia, *RCA clean* — SC-1 and SC-2 compositions and
  temperatures.[^wiki-rca]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography, resist stripping, wafer cleaning and implantation
  chapters.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — lithography
  tools, implanted-resist stripping and RTP of the 0.25–0.13 µm
  generations.[^txt-05]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — fab-floor
  view of ash and wet-clean tools.[^txt-07]

### Deep dive

* Kern, in Reinhardt and Kern (eds.), *Handbook of Silicon Wafer
  Cleaning Technology* — overview chapter on wet-cleaning chemistry and
  contamination.[^kern-handbook]
* ITRS 2001, *Front End Processes* — surface preparation.[^itrs-01]
* Fujimura et al. (Fujitsu), *Jpn. J. Appl. Phys.* 1989 — the measured
  crust-and-popping mechanism of ion-implanted resist that every implant
  strip has to defeat.[^fujimura-1989]
* Fujimura et al. (Fujitsu), *Jpn. J. Appl. Phys.* 1990 — why nitrogen
  is added to oxygen in downstream ashing.[^fujimura-1990]
* Fujimura et al. (Fujitsu), *J. Vac. Sci. Technol. B* 1994 —
  water-vapour addition to downstream ashing, the origin of the H₂O/H₂
  chemistries on modern ashers.[^fujimura-1994]
* Ohmi, *J. Electrochem. Soc.* 1996 — a room-temperature alternative to
  the hot SPM/SC-1/SC-2 sequence.[^ohmi-1996]
* Reinhardt and Reidy (eds.), *Handbook of Cleaning in Semiconductor
  Manufacturing* — a modern handbook treatment of post-implant stripping
  and wet cleaning.[^reinhardt-2010]
* Nakayama et al. (ULVAC), US 5,795,831 — a cold process for stripping
  implanted resist, showing the alternatives to hot
  ashing.[^pat-strip-ulvac]
* Lee et al. (Genus), IIT 1996 — outgassing of thick resists during MeV
  implantation, what the resist has been through before this
  strip.[^lee-1996]
* Horsky (Eaton), IIT 1998 — resist outgassing in high-energy and
  high-current implanters.[^horsky-1998]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — the two-stage
  low-temperature ash for high-dose implanted resist.[^pat-strip-mosel]
* Chan, Chiu and Tao (TSMC), US 2004/0214448 — an ashing sequence
  designed around the carbonised crust.[^pat-strip-tsmc]

## Open questions

* The ash recipe (stages, temperatures, gases) and wet sequence are
  not public.
* Whether the three implants really share one resist, and hence
  whether this is the strip of the N-well resist, is inferred from
  the step order.
* How much pad oxide is lost per strip/clean cycle, and whether that
  loss is budgeted against a later sacrificial-oxide step, is unknown
  (see the open question on {ref}`NS19 <step-013>`).

<!-- footnotes -->

[^pat-strip-tsmc]: B.-W. Chan, Y.-H. Chiu and H.-J. Tao (TSMC), *Method
    of ashing a photoresist*, US 2004/0214448 A1, published 2004-10-28.
    <https://patents.google.com/patent/US20040214448A1/en>
[^pat-strip-mosel]: M.-S. Tseng, F.-H. Chao and N.-Y. Tsai (Mosel
    Vitelic), *Low temperature dry process for stripping photoresist
    after high dose ion implantation*, US 5,811,358 A, granted
    1998-09-22. <https://patents.google.com/patent/US5811358A/en>
[^wiki-ash]: Wikipedia, *Plasma ashing*.
    <https://en.wikipedia.org/wiki/Plasma_ashing>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000, ISBN
    978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^job-01]: Indeed, *Skywater Technology Foundry Jobs, Employment in
    Bloomington, MN* (listing page), retrieved 2026-08-30.
    <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^kern-handbook]: W. Kern, "Overview and Evolution of Silicon Wafer
    Cleaning Technology", ch. 1 in K. A. Reinhardt and W. Kern (eds.),
    *Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
    Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8.
    <https://doi.org/10.1016/b978-081551554-8.50004-5>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^fujimura-1989]: S. Fujimura, J. Konno, K. Hikazutani and H. Yano,
    "Ashing of Ion-Implanted Resist Layer", *Japanese Journal of Applied
    Physics* **28**(10R), 2130 (1989).
    <https://doi.org/10.1143/JJAP.28.2130>
[^fujimura-1990]: S. Fujimura, K. Shinagawa, M. Nakamura and H. Yano,
    "Additive Nitrogen Effects on Oxygen Plasma Downstream Ashing",
    *Japanese Journal of Applied Physics* **29**(10R), 2165 (1990).
    <https://doi.org/10.1143/JJAP.29.2165>
[^fujimura-1994]: S. Fujimura, M. T. Suzuki, K. Shinagawa and M.
    Nakamura, "Sodium contamination free ashing process using O₂+H₂O
    plasma downstream", *Journal of Vacuum Science & Technology B*
    **12**(4), 2409–2413 (1994). <https://doi.org/10.1116/1.587773>
[^ohmi-1996]: T. Ohmi, "Total Room Temperature Wet Cleaning for Si
    Substrate Surface", *Journal of The Electrochemical Society*
    **143**(9), 2957–2964 (1996). <https://doi.org/10.1149/1.1837133>
[^reinhardt-2010]: K. A. Reinhardt and R. F. Reidy (eds.), *Handbook of
    Cleaning in Semiconductor Manufacturing: Fundamental and
    Applications*, Wiley, 2010, ISBN 978-0-470-62595-8.
    <https://doi.org/10.1002/9781118071748>
[^pat-strip-ulvac]: I. Nakayama et al. (ULVAC Technologies), *Cold
    processes for cleaning and stripping photoresist from surfaces of
    semiconductor wafers*, US 5,795,831 A, granted 1998-08-18.
    <https://patents.google.com/patent/US5795831A/en>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy and
    high current ion implantation", *Proc. 1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
