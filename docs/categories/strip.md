(category-strip)=
# Resist strip / clean

## What this class of step does

A strip step takes off the photoresist once it has done its job as an
implant or etch mask, and then cleans the wafer so that the next step
starts from a bare, chemically defined surface. Resist is an organic
polymer; it is burnt off in an oxygen plasma ({term}`ash`) and the
inorganic residue and any remaining organic film are dissolved in hot
acid–peroxide baths. A few "strip" steps in the flow remove not resist
but a sacrificial inorganic film, most notably the STI nitride
({ref}`NS19 <step-013>`), by wet etching.

Precisely, a post-implant strip in a 130 nm flow is usually three
operations in one travelling group: a plasma ash in a downstream
microwave or RF oxygen plasma at 200–300 °C (a typical industry value;
the Gasonics L3510's platen range is 100–300 °C),[^gasonics-l3510] often
with a low-power first stage to break through the hardened "crust" that
a high-dose implant leaves on the resist surface; a wet strip in
sulfuric acid–hydrogen peroxide ({term}`SPM`, "piranha") which "is used
to clean organic residues off substrates";[^wiki-piranha] and a final
{term}`SC-1` (and sometimes {term}`SC-2`) clean of the {term}`RCA clean`
family to remove particles and metals.[^wiki-rca] Post-etch strips add a
solvent or semi-aqueous step to remove the halogenated polymer left by
plasma etching, and after aluminium etch the SPM step is omitted because
it attacks the metal.

In the SKY130 flow there are fourteen implant-mask strips (one after
every implant lithography, from {ref}`DNIS <step-009>` to
{ref}`NSDIS <step-087>`) plus the STI nitride strip
{ref}`NS19 <step-013>`. The strips that follow *etch* masks are not
listed as separate steps in the step list used in this reference and
are assumed to be part of the corresponding etch step group.

## Physics and engineering background

### Plasma ashing

In an asher, "using a plasma source, a monatomic (single atom) substance
known as a reactive species is generated. Oxygen or fluorine are the
most common reactive species".[^wiki-ash] Atomic oxygen oxidises the
resist's carbon and hydrogen to CO, CO₂ and H₂O, which are pumped away;
the rate is thermally activated, so ashers run hot for bulk removal —
typically 200–300 °C; the Gasonics L3510 platen spans 100–300
°C[^gasonics-l3510] and the Aura 1000 150–300 °C[^gasonics-aura] — and
cool for "descum". To avoid charging and ion damage to gate oxides,
"many machines now use a downstream plasma configuration, where plasma
is formed remotely and the desired particles are channeled to the
wafer"; "monatomic oxygen is electrically neutral and although it does
recombine during the channeling, it does so at a slower rate than the
positively or negatively charged free radicals".[^wiki-ash] Small
additions of fluorine (CF₄) attack silicon oxides and speed the removal
of inorganic residues; additions of hydrogen or water vapour help with
implanted resist. Endpoint is detected from the CO emission line,
followed by a timed over-ash.

### The post-implant crust

Resist that has masked a high-dose implant is a different material from
freshly developed resist. The ions deposit their energy in the top
100–200 nm, cross-linking and carbonising it and embedding the implanted
species; problems arise "when this photoresist has undergone an
implant step previously and heavy metal are embedded in the
photoresist and it has experienced high temperatures causing it to be
resistant to oxidizing".[^wiki-ash] If the
crusted wafer is heated quickly, solvent and nitrogen trapped in the
soft resist underneath blow the crust off in flakes ("popping") that
land elsewhere on the wafer as hard-to-remove particles. The standard
countermeasures are a low-temperature first ash step or a slow ramp,
forming-gas or H₂O-containing chemistries that penetrate the crust, and
a wet SPM follow-up, which is why implant strips are longer and more
carefully engineered than etch strips.[^kern-handbook]

### Wet strip and clean chemistry

* **SPM (piranha)**: "a typical mixture is 3 parts of concentrated
  sulfuric acid and 1 part of 30 wt. % hydrogen peroxide solution", with
  4:1 and 7:1 also used, and the exothermic mixing "can easily bring the
  solution temperature above 100 °C".[^wiki-piranha] It dissolves
  organics by oxidation and leaves the silicon surface hydroxylated and
  hydrophilic with a thin chemical oxide. It is incompatible with
  exposed aluminium and titanium nitride.
* **SC-1 (APM)**: "5 parts of deionized water, 1 part of ammonia water
  (29% by weight of NH3), 1 part of aqueous H2O2 (hydrogen peroxide,
  30%) at 75 or 80 °C typically for 10 minutes".[^wiki-rca] It removes
  particles by continuously growing and under-cutting a chemical oxide,
  and organics by oxidation; dilute variants (1:1:50 and weaker) with
  megasonic agitation were standard by the 130 nm node to limit silicon
  roughening.[^kern-1990]
* **SC-2 (HPM)**: "6 parts of deionized water, 1 part of aqueous HCl
  (hydrochloric acid, 37% by weight), 1 part of aqueous H2O2 (hydrogen
  peroxide, 30%) at 75 or 80 °C",[^wiki-rca] which dissolves metallic
  contamination as chlorides. Werner Kern "developed the basic procedure
  in 1965 while working for RCA".[^wiki-rca][^kern-1990]
* **Dilute HF**: a short dip removes the chemical oxide left by SC-1 or
  SPM and leaves a hydrogen-terminated, hydrophobic surface; used as
  "HF-last" before gate oxidation and before silicide deposition.
* **Solvent and semi-aqueous strippers**: N-methyl-2-pyrrolidone (NMP),
  dimethyl sulfoxide (DMSO) and hydroxylamine- or amine-based
  formulations (EKC265, ACT) dissolve resist and etch polymers where
  acids cannot be used, principally after metal etch, and are followed
  by an IPA or water rinse.[^wiki-nmp]

### Nitride strip

The STI nitride ({ref}`ISONIT <step-003>`) is removed after the oxide
CMP in hot phosphoric acid — 85 % H₃PO₄ at 150–180 °C — which etches
Si₃N₄ at a few nanometres per minute with a selectivity to SiO₂ of the
order of 30:1 or better; the pad oxide underneath protects the silicon
and is later removed in HF.[^txt-02][^wiki-h3po4] The bath temperature
and its water content (which the etch consumes) must be controlled, and
the bath is usually run with a reflux condenser and water spiking.

### Cleanliness, drying and surface state

Every clean ends with a de-ionised-water rinse and a dry: spin-rinse
drying for batch cassettes, or IPA-vapour (Marangoni) drying, which
draws the water off the wafer without leaving water marks. The state
in which the surface is left — hydrophilic chemical oxide or
hydrophobic H-terminated silicon — must match what the next step
expects: gate oxidation wants an HF-last surface with a re-grown
chemical oxide of controlled thickness, while resist coating wants a
hydrophobic surface obtained with HMDS ({ref}`category-lithography`).
The ITRS 2001 front-end chapter treats surface preparation, particles
and metals as a critical-dimension issue in its own right.[^itrs-01]

## Typical equipment

* **Ashers**: downstream microwave strippers such as the Gasonics L3510
  (a "production-proven downstream plasma photoresist ashing system" for
  75–200 mm wafers)[^gasonics-l3510] and the Gasonics Aura series;
  Mattson Aspen (ICP-based strip); Axcelis/Fusion ES and RadiantStrip;
  single-wafer RF ashers integrated onto etch platforms (Applied
  Materials ASP and Lam). University clean-room guides describe the
  class.[^snf-strip]
* **Wet benches**: automated multi-tank benches with SPM, SC-1, SC-2, HF
  and hot-phosphoric tanks, quick-dump rinsers and IPA dryers — Akrion
  GAMA,[^akrion-gama] SCP, DNS/Screen, Santa Clara Plastics, Semitool.
* **Spray processors** (FSI Mercury centrifugal spray) and
  **single-wafer spin processors** (SEZ, later Lam; DNS) for HF-based
  and solvent strips with better chemical freshness and no
  cross-contamination between wafers.
* **Metrology**: laser surface scanners for particles (KLA-Tencor
  Surfscan), TXRF and VPD-ICP-MS for surface metals, contact-angle and
  ellipsometric checks of the chemical oxide.

## Typical consumables

* **Gases**: O₂, N₂, forming gas (H₂/N₂), CF₄, water vapour.
* **Acids and bases**: 96–98 % sulfuric acid, 30 % hydrogen peroxide,
  29 % ammonium hydroxide, 37 % hydrochloric acid, 49 % HF, 85 %
  phosphoric acid; all semiconductor-grade (parts-per-trillion metals).
* **Solvents**: NMP, DMSO, hydroxylamine-based strippers, isopropanol
  for drying.
* **Water**: ultrapure de-ionised water at 18 MΩ·cm with sub-ppb TOC,
  in very large volumes (thousands of litres per wafer pass through a
  wet bench).
* **Hardware**: quartz and PFA tanks, PTFE/PFA cassettes and carriers,
  filters, megasonic transducers, and asher quartz tubes and windows.

## Steps in this category

| Step | Code | Name |
|------|------|------|
| 9 | {ref}`DNIS <step-009>` | High V deep N-well implant strip |
| 13 | {ref}`NS19 <step-013>` | Nitride strip |
| 16 | {ref}`LVTNIS <step-016>` | Low Vt NMOS implant strip |
| 21 | {ref}`LVTPIS <step-021>` | P-channel implant strip |
| 25 | {ref}`PCHIS <step-025>` | P-channel BF2 implant strip |
| 29 | {ref}`PWIS <step-029>` | P-well implant strip |
| 33 | {ref}`PWDEIS <step-033>` | PWDEIS implant strip |
| 51 | {ref}`P1IS <step-051>` | P1IS implant resist strip |
| 54 | {ref}`PRIS <step-054>` | PRI implant resist strip |
| 57 | {ref}`UPRIS <step-057>` | UPRIS implant resist strip |
| 67 | {ref}`ASTIS <step-067>` | As tip implant strip |
| 70 | {ref}`HVASTIS <step-070>` | HV As N-tip implant strip |
| 74 | {ref}`LDASTIS <step-074>` | LD ASTI implant strip |
| 84 | {ref}`PDIS <step-084>` | P+ source drain implant strip |
| 87 | {ref}`NSDIS <step-087>` | N+ source drain implant strip |

## References

### Cross-check

* Kern, *JES* 1990 — the history and chemistry of the RCA
  clean.[^kern-1990]
* Kern and Puotinen, *RCA Review* 1970 — the original SC-1/SC-2
  paper.[^kern-1970]
* Kern, ch. 1 of Reinhardt and Kern (eds.), *Handbook of Silicon Wafer
  Cleaning Technology* — overview of cleaning and of implanted-resist
  stripping.[^kern-handbook]
* ITRS 2001, *Front End Processes* — surface preparation
  requirements.[^itrs-01]
* SemiStar, Gasonics L3510 description — platen temperature
  100–300 °C.[^gasonics-l3510]
* Allwin21, Gasonics Aura 1000 specification — 150–300 °C.[^gasonics-aura]
* Stanford Nanofabrication Facility, *Downstream/Remote Plasma Resist
  Removal*.[^snf-strip]
* C2MI, *Akrion GAMA acid bench*.[^akrion-gama]

### High-level understanding

* Wikipedia, *Plasma ashing* — downstream ashing and implanted-resist
  problems.[^wiki-ash]
* Wikipedia, *Piranha solution* — SPM ratios and
  temperature.[^wiki-piranha]
* Wikipedia, *RCA clean* — SC-1 and SC-2 recipes.[^wiki-rca]
* Wikipedia, *Hydrofluoric acid*.[^wiki-hf]
* Wikipedia, *Phosphoric acid*.[^wiki-h3po4]
* Wikipedia, *N-Methyl-2-pyrrolidone*.[^wiki-nmp]
* Wikipedia, *Photoresist*.[^wiki-resist]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — ch. 4
  ("Semiconductor Manufacturing — Clean Rooms, Wafer Cleaning and
  Gettering").[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  ch. 15 ("Wet Processing: Cleaning, Etching and Liftoff").[^txt-02]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — ch. 7
  and 16.[^txt-07]
* Xiao, *Introduction to Semiconductor Manufacturing Technology* —
  ch. 8.[^txt-08]

### Deep dive

* Fujimura et al., *JJAP* 1989 — the crust and popping mechanism of
  implanted resist, measured.[^fujimura-1989]
* Fujimura et al., *JJAP* 1990 — why nitrogen is added to oxygen
  downstream ashing.[^fujimura-1990]
* Fujimura et al., *JVST B* 1994 — water-vapour downstream ashing to
  avoid sodium contamination.[^fujimura-1994]
* Ohmi, *JES* 1996 — a room-temperature alternative to the hot RCA
  sequence.[^ohmi-1996]
* Reinhardt and Reidy (eds.), *Handbook of Cleaning in Semiconductor
  Manufacturing* — modern wet and dry cleaning
  fundamentals.[^reinhardt-2010]
* van Gelder and Hauser, *JES* 1967 — hot phosphoric acid selectivity
  between nitride, oxide and silicon.[^vgh-1967]
* Horsky, IIT 1998 — resist outgassing in high-energy and high-current
  implantation, the origin of the crust.[^horsky-1998]
* Lee et al., IIT 1996 — thick-resist outgassing during MeV
  implantation.[^lee-1996]
* Roche, Michaud and Bruel, *MRS Proc.* 1985 — early measurements of
  resist outgassing under the beam.[^roche-1985]
* Tseng, Chao and Tsai (Mosel Vitelic), US 5,811,358 — a
  low-temperature dry strip after high-dose implantation.[^pat-strip-mosel]
* Chan, Chiu and Tao (TSMC), US 2004/0214448 — a one-step CₓHᵧF_z/O₂
  plasma ash for the carbonised crust of implanted resist.[^pat-strip-tsmc]
* Nakayama et al. (ULVAC), US 5,795,831 — cold stripping and cleaning
  processes.[^pat-strip-ulvac]
* Kamarehi and Simpson (Fusion Systems), US 5,498,308 — a downstream
  microwave asher design.[^pat-asher-fusion]
* Becknell, Hammar and Ferris (Axcelis), US 7,449,416 — an oxygen-free,
  nitrogen-free ashing chemistry for resist and post-etch residue
  removal over low-k dielectrics.[^pat-asher-axcelis]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — chapters on wafer cleaning and plasma
  stripping.[^txt-09]

<!-- footnotes -->

[^gasonics-l3510]: SemiStar Corp., *Gasonics L3510 plasma asher* (tool
    description; platen temperature 100–300 °C).
    <http://www.semistarcorp.com/product/gasonics-l3510-asher/>
[^wiki-piranha]: Wikipedia, *Piranha solution*.
    <https://en.wikipedia.org/wiki/Piranha_solution>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^wiki-ash]: Wikipedia, *Plasma ashing*.
    <https://en.wikipedia.org/wiki/Plasma_ashing>
[^gasonics-aura]: Allwin21, *Gasonics Aura 1000 Plasma Asher*
    (specification summary; temperature 150–300 °C typical).
    <https://allwin21.com/gasonics-aura-1000-plasma-asher-2/>
[^kern-handbook]: W. Kern, "Overview and Evolution of Silicon Wafer
    Cleaning Technology", ch. 1 in K. A. Reinhardt and W. Kern (eds.),
    *Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
    Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8.
    <https://doi.org/10.1016/b978-081551554-8.50004-5>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^wiki-nmp]: Wikipedia, *N-Methyl-2-pyrrolidone*.
    <https://en.wikipedia.org/wiki/N-Methyl-2-pyrrolidone>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^wiki-h3po4]: Wikipedia, *Phosphoric acid*.
    <https://en.wikipedia.org/wiki/Phosphoric_acid>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^snf-strip]: Stanford Nanofabrication Facility, *Downstream/Remote
    Plasma Resist Removal*, equipment guide.
    <https://snfguide.stanford.edu/guide/equipment/purpose/cleaning/resist-removal/dry-resist-removal/downstreamremote-plasma-resist-removal>
[^akrion-gama]: C2MI, *Akrion GAMA acid bench*, equipment page.
    <https://www.c2mi.ca/en/equipement/akrion-gama-acid-bench/>
[^kern-1970]: W. Kern and D. A. Puotinen, "Cleaning solutions based on
    hydrogen peroxide for use in silicon semiconductor technology", *RCA
    Review* **31**, 187–206 (1970).
[^wiki-hf]: Wikipedia, *Hydrofluoric acid*.
    <https://en.wikipedia.org/wiki/Hydrofluoric_acid>
[^wiki-resist]: Wikipedia, *Photoresist*.
    <https://en.wikipedia.org/wiki/Photoresist>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^txt-08]: H. Xiao, *Introduction to Semiconductor Manufacturing
    Technology*, 2nd ed., SPIE Press, 2012, ISBN 978-0-8194-9092-6.
    <https://doi.org/10.1117/3.924283>
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
[^vgh-1967]: W. van Gelder and V. E. Hauser, "The Etching of Silicon
    Nitride in Phosphoric Acid with Silicon Dioxide as a Mask", *Journal
    of The Electrochemical Society* **114**(8), 869 (1967).
    <https://doi.org/10.1149/1.2426757>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy and
    high current ion implantation", *Proc. 1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^roche-1985]: D. Roche, J. F. Michaud and M. Bruel, "Outgassing of
    Photoresist During Ion Implantation", *MRS Proceedings* **45**
    (1985). <https://doi.org/10.1557/PROC-45-203>
[^pat-strip-mosel]: M.-S. Tseng, F.-H. Chao and N.-Y. Tsai (Mosel
    Vitelic), *Low temperature dry process for stripping photoresist
    after high dose ion implantation*, US 5,811,358 A, granted
    1998-09-22. <https://patents.google.com/patent/US5811358A/en>
[^pat-strip-tsmc]: B.-W. Chan, Y.-H. Chiu and H.-J. Tao (TSMC), *Method
    of ashing a photoresist*, US 2004/0214448 A1, published 2004-10-28.
    <https://patents.google.com/patent/US20040214448A1/en>
[^pat-strip-ulvac]: I. Nakayama et al. (ULVAC Technologies), *Cold
    processes for cleaning and stripping photoresist from surfaces of
    semiconductor wafers*, US 5,795,831 A, granted 1998-08-18.
    <https://patents.google.com/patent/US5795831A/en>
[^pat-asher-fusion]: M. Kamarehi and J. E. Simpson (Fusion Systems),
    *Plasma asher with microwave trap*, US 5,498,308 A, granted
    1996-03-12.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5498308>
[^pat-asher-axcelis]: A. F. Becknell, P. Hammar and D. Ferris (Axcelis
    Technologies), *Apparatus and plasma ashing process for increasing
    photoresist removal rate*, US 7,449,416 B2, granted 2008-11-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7449416>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007,
    ISBN 978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
