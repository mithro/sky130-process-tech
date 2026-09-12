(step-057)=
# Step 057 — UPRIS: UPRIS implant resist strip

| | |
|---|---|
| **Step number** | 57 of 171 |
| **Step code** | `UPRIS` |
| **Category** | {ref}`Resist strip / clean <category-strip>` |
| **Phase** | FEOL — gate and poly resistors |
| **Previous step** | {ref}`UPRI <step-056>` |
| **Next step** | {ref}`GATENIT <step-058>` |

## What this step is

`UPRIS` removes the ultra-high-resistor resist printed at
{ref}`URPM <step-055>` after the light resistor implant
{ref}`UPRI <step-056>`, and delivers a clean, fully doped
amorphous-silicon film to the deposition that caps it,
{ref}`GATENIT <step-058>`. It is the last of the three strips of the
gate module and the last time the gate film is exposed to a wet
chemistry before it is sealed under nitride and oxide. The next step
is a furnace or {term}`PECVD` deposition rather than another mask, which
changes what "clean" has to mean.

The resist being removed has taken the lightest implant of the module
— a p-type dose of order 10¹⁴ cm⁻² or less (illustrative,
{ref}`UPRI <step-056>`) — so its {term}`crust <implant crust>` is thin, in the same class as
the channel-implant strips of the well module
({ref}`LVTNIS <step-016>`). The surface it leaves behind carries three
doping levels (n⁺ gate poly, 300 Ω/sq and 2000 Ω/sq resistor bodies)
and the thin chemical oxides of two previous cleans.

## Step category

`UPRIS` is a {ref}`Resist strip / clean <category-strip>` step of the
*post-implant* type, at the light end of the range. What is specific
to it is that it is also the *pre-deposition clean* for the gate cap:
the category page notes that a strip before a furnace step has to
leave the surface in a state the deposition tolerates, and here that
surface is the top of every gate.

## Why this step exists

The resist must go, as always. Beyond that, the film that goes into
{ref}`GATENIT <step-058>` must be free of organic residue and particles,
because anything on it is buried under the cap and printed into the gate
at {ref}`P1ME <step-062>`: a particle becomes a micro-mask that leaves a
poly stringer, a residue becomes a local etch-rate change. The state of
the surface also matters for the film that is deposited on it. A silicon
nitride deposited by {term}`LPCVD` or PECVD on silicon nucleates and adheres
well; on a contaminated or rough surface it can blister or deposit
non-uniformly. A thin, uniform chemical oxide under the cap is harmless,
and LPCVD nitride's tensile stress of order 1 GPa[^temple-boyer-1998] is
one of the film-stress problems Hu reviews,[^hu-1991] so the surface it
is deposited on should at least be clean and uniform. The clean here is
therefore designed to leave that oxide, not remove it — an inference
from the step order, since no public source describes the SKY130 surface
state before the cap.

Metallic contamination is the other concern. The three implants of the module
have sputtered beam-line material onto the resist and the open film, and the
wafers have been through three tracks and two ashers. A furnace step may come
next ({ref}`GATENIT <step-058>`), and the category page explains why metals
must be removed before any high-temperature process: they diffuse and
precipitate, and the gate oxide is directly beneath the film. {term}`SC-1` and
{term}`SC-2` exist for exactly this.[^kern-1990][^wiki-rca]

## How it is typically performed

An industry-generic light-implant strip followed by a pre-deposition
clean, for a 200 mm, 130 nm-era fab:

1. **Plasma {term}`ash`.** Downstream O₂/N₂ plasma; a single hot step often
   suffices for a light implant, though a fab that runs all implant
   strips on one recipe will use the two-step sequence
   anyway.[^fujimura-1989][^pat-strip-mosel] The three ashers on
   SkyWater's list cover the gases and temperatures.[^skw-01]
2. **Wet strip and clean.** {term}`SPM` for organics, SC-1 for particles and,
   because a furnace step may follow, SC-2 (HCl/H₂O₂/H₂O) for
   metals[^wiki-rca] — the full RCA sequence of Kern and
   Puotinen.[^kern-1970] The SC-1 exposure is again limited by its silicon
   etch rate,[^lee-kt-1999] and the sequence finishes without an HF step so
   that a thin chemical oxide remains (inference above). SkyWater's benches
   cover the chemistries: "Akrion Gamma Batch Wet Bench – Sulfuric, SC1,
   phosphoric, BOE", "DNS wet bench industry standard HF/SC1/SC2" and "FSI
   Mercury industry standard HF/SC1/SC2 rotational".[^skw-01]
3. **Rinse and dry.** Cascade rinse and IPA/Marangoni dry, which
   leaves fewer drying marks than spin drying on a hydrophilic
   surface.[^reinhardt-2008]
4. **Queue time.** A limit between the clean and the deposition, so
   that the surface does not re-contaminate or grow further native
   oxide.
5. **Inspection.** Unpatterned-surface particle scan on monitors and
   patterned inspection on product.

## Machines typically used

* **Downstream plasma asher** (Gasonics Aura/PEP, Mattson Aspen,
  Axcelis/Fusion ES, PSK).
* **Batch wet bench** with SPM, SC-1, SC-2 and a Marangoni dryer
  (Akrion, DNS/SCREEN, SCP), or **spray processor** (FSI Mercury).
* **Surface particle scanner** (KLA-Tencor Surfscan SP1) and
  **patterned inspection** (AIT).

## Machines likely used at SkyWater

* **Gasonics PEP, Iridia and Mattson Aspen 2 ashers.**[^skw-01]
  Strength: **strong** for existence; assignment not stated.
* **DNS wet bench or FSI Mercury** ("industry standard HF/SC1/SC2")
  for a full RCA sequence, or the **Akrion Gamma** bench.[^skw-01]
  Strength: strong for existence.
* **KLA-Tencor SP1 and AIT** inspection, from a SkyWater job
  posting.[^job-01] Strength: medium.

## Resources required

* **Oxygen, nitrogen, {term}`forming gas`** for the ash.[^skw-01]
* **Sulphuric acid, hydrogen peroxide, ammonium hydroxide,
  hydrochloric acid** for SPM/SC-1/SC-2.[^wiki-rca]
* **Ultrapure DI water, isopropanol, nitrogen.**
* Chemical suppliers named by SkyWater: KMG Chemicals, EMD Performance
  Materials.[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`UPRI <step-056>`; mask: {ref}`URPM <step-055>`.
* Next: {ref}`GATENIT <step-058>` (the cap deposited on the cleaned
  film), then {ref}`POC <step-059>`.
* Companion strips: {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`;
  light-implant exemplar: {ref}`LVTNIS <step-016>`.
* Another pre-furnace clean is the one before {ref}`BOX <step-002>` (see
  {ref}`SMAT <step-001>`).
* Category page: {ref}`Resist strip / clean <category-strip>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — ashers; Akrion, DNS and
  FSI benches with their chemistries.[^skw-01]
* Indeed, SkyWater listings — "SEM/AIT/KLA/SP1/EV300/1X".[^job-01]
* SkyWater, Form S-1 and Form 10-K — chemical suppliers.[^sec-01][^sec-02]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — two-stage
  ash.[^pat-strip-mosel]

### High-level understanding

* Wikipedia, *Plasma ashing* and *RCA clean*.[^wiki-ash][^wiki-rca]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  cleaning before furnace steps.[^txt-02]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — wet
  benches and dryers.[^txt-07]

### Deep dive

* Kern and Puotinen, *RCA Review* 1970 — the original SC-1/SC-2
  sequence.[^kern-1970]
* Kern, *J. Electrochem. Soc.* 1990 — the evolution of wafer
  cleaning.[^kern-1990]
* Fujimura et al., *Jpn. J. Appl. Phys.* 1989 — ashing implanted
  resist.[^fujimura-1989]
* Fujimura et al., *Jpn. J. Appl. Phys.* 1990 — nitrogen additions in
  downstream ashing.[^fujimura-1990]
* Lee, *Electrochem. Solid-State Lett.* 1999 — silicon etch rate in
  SC-1.[^lee-kt-1999]
* Ohmi, *J. Electrochem. Soc.* 1996 — room-temperature cleaning as
  the alternative to hot RCA steps.[^ohmi-1996]
* Hu, *J. Appl. Phys.* 1991, and Temple-Boyer et al., *J. Vac. Sci.
  Technol. A* 1998 — nitride film stress and why a thin oxide under a
  nitride is welcome.[^hu-1991][^temple-boyer-1998]
* Reinhardt and Kern (eds.), *Handbook of Silicon Wafer Cleaning
  Technology* — pre-deposition cleaning and drying.[^reinhardt-2008]
* Reinhardt and Reidy (eds.), *Handbook of Cleaning in Semiconductor
  Manufacturing* — post-implant stripping in a modern
  handbook.[^reinhardt-2010]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — cold first
  ash.[^pat-strip-mosel]
* Becknell, Hammar and Ferris (Axcelis), US 7,449,416 — asher design
  for removal rate.[^pat-asher-axcelis]
* Roche, Michaud and Bruel, *MRS Proc.* 1985 — resist outgassing
  during implantation.[^roche-1985]
* ITRS 2001, *Front End Processes* — surface preparation before
  gate-stack steps.[^itrs-01]

## Open questions

* Whether the clean before {ref}`GATENIT <step-058>` includes SC-2, an
  HF step, or a dedicated pre-furnace clean separate from the strip,
  is not public; the RCA sequence without HF is an inference.
* The queue-time limit between this clean and the cap deposition is
  unknown.
* Which asher and bench run this step are not stated.

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^job-01]: Indeed, *Skywater Technology Foundry Jobs, Employment in
    Bloomington, MN* (listing page; Defect Technician 2 posting),
    retrieved 2026-08-30. <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^pat-strip-mosel]: M.-S. Tseng, F.-H. Chao and N.-Y. Tsai (Mosel
    Vitelic), *Low temperature dry process for stripping photoresist
    after high dose ion implantation*, US 5,811,358 A, granted
    1998-09-22. <https://patents.google.com/patent/US5811358A/en>
[^wiki-ash]: Wikipedia, *Plasma ashing*.
    <https://en.wikipedia.org/wiki/Plasma_ashing>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^kern-1970]: W. Kern and D. A. Puotinen, "Cleaning solutions based on
    hydrogen peroxide for use in silicon semiconductor technology", *RCA
    Review* **31**, 187–206 (1970).
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^fujimura-1989]: S. Fujimura, J. Konno, K. Hikazutani and H. Yano,
    "Ashing of Ion-Implanted Resist Layer", *Japanese Journal of Applied
    Physics* **28**(10R), 2130 (1989).
    <https://doi.org/10.1143/JJAP.28.2130>
[^fujimura-1990]: S. Fujimura, K. Shinagawa, M. Nakamura and H. Yano,
    "Additive Nitrogen Effects on Oxygen Plasma Downstream Ashing",
    *Japanese Journal of Applied Physics* **29**(10R), 2165 (1990).
    <https://doi.org/10.1143/JJAP.29.2165>
[^lee-kt-1999]: K. T. Lee, "Etch Rate of Silicon and Silicon Dioxide in
    Ammonia-Peroxide Solutions Measured by Quartz Crystal Microbalance
    Technique", *Electrochemical and Solid-State Letters* **2**(4), 172
    (1999). <https://doi.org/10.1149/1.1390773>
[^ohmi-1996]: T. Ohmi, "Total Room Temperature Wet Cleaning for Si
    Substrate Surface", *Journal of The Electrochemical Society*
    **143**(9), 2957–2964 (1996). <https://doi.org/10.1149/1.1837133>
[^hu-1991]: S. M. Hu, "Stress-related problems in silicon technology",
    *Journal of Applied Physics* **70**(6), R53–R80 (1991).
    <https://doi.org/10.1063/1.349282>
[^temple-boyer-1998]: P. Temple-Boyer, C. Rossi, E. Saint-Etienne and
    E. Scheid, "Residual stress in low pressure chemical vapor
    deposition SiNₓ films deposited from silane and ammonia", *Journal
    of Vacuum Science & Technology A* **16**(4), 2003–2007 (1998).
    <https://doi.org/10.1116/1.581302>
[^reinhardt-2008]: K. A. Reinhardt and W. Kern (eds.), *Handbook of
    Silicon Wafer Cleaning Technology*, 2nd ed., William Andrew, 2008,
    ISBN 978-0-8155-1554-8. <https://openlibrary.org/isbn/9780815515548>
[^reinhardt-2010]: K. A. Reinhardt and R. F. Reidy (eds.), *Handbook of
    Cleaning in Semiconductor Manufacturing: Fundamental and
    Applications*, Wiley, 2010, ISBN 978-0-470-62595-8.
    <https://doi.org/10.1002/9781118071748>
[^pat-asher-axcelis]: A. F. Becknell, P. Hammar and D. Ferris (Axcelis
    Technologies), *Apparatus and plasma ashing process for increasing
    photoresist removal rate*, US 7,449,416 B2, granted 2008-11-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7449416>
[^roche-1985]: D. Roche, J. F. Michaud and M. Bruel, "Outgassing of
    Photoresist During Ion Implantation", *MRS Proceedings* **45**
    (1985). <https://doi.org/10.1557/PROC-45-203>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
