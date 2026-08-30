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
the Gasonics L3510's platen range is 100–300 °C [gasonics]), often
with a low-power first stage to break through the hardened "crust"
that a high-dose
implant leaves on the resist surface; a wet strip in sulfuric
acid–hydrogen peroxide ({term}`SPM`, "piranha") which "is used to clean
organic residues off substrates" ([Wikipedia: Piranha
solution][wiki-piranha]); and a final {term}`SC-1` (and sometimes
{term}`SC-2`) clean of the {term}`RCA clean` family to remove particles
and metals ([Wikipedia: RCA clean][wiki-rca]). Post-etch strips add a
solvent or semi-aqueous step to remove the halogenated polymer left by
plasma etching, and after aluminium etch the SPM step is omitted
because it attacks the metal.

In the SKY130 flow there are fourteen implant-mask strips (one after
every implant lithography, from {ref}`DNIS <step-009>` to
{ref}`NSDIS <step-087>`) plus the STI nitride strip
{ref}`NS19 <step-013>`. The strips that follow *etch* masks are not
listed as separate steps in the step list used in this reference and
are assumed to be part of the corresponding etch step group.

## Physics and engineering background

### Plasma ashing

In an asher, "using a plasma source, a monatomic (single atom)
substance known as a reactive species is generated. Oxygen or fluorine
are the most common reactive species" ([Wikipedia: Plasma
ashing][wiki-ash]). Atomic oxygen oxidises the resist's carbon and
hydrogen to CO, CO₂ and H₂O, which are pumped away; the rate is
thermally activated, so ashers run hot for bulk removal — typically
200–300 °C; the Gasonics L3510 platen spans 100–300 °C [gasonics] and
the Aura 1000 150–300 °C [aura1000] — and cool for "descum". To avoid charging and ion damage to gate oxides,
"many machines now use a downstream plasma configuration, where plasma
is formed remotely and the desired particles are channeled to the
wafer"; "monatomic oxygen is electrically neutral and although it does
recombine during the channeling, it does so at a slower rate than the
positively or negatively charged free radicals" ([Wikipedia: Plasma
ashing][wiki-ash]). Small additions of fluorine (CF₄) attack silicon
oxides and speed the removal of inorganic residues; additions of
hydrogen or water vapour help with implanted resist. Endpoint is
detected from the CO emission line, followed by a timed over-ash.

### The post-implant crust

Resist that has masked a high-dose implant is a different material from
freshly developed resist. The ions deposit their energy in the top
100–200 nm, cross-linking and carbonising it and embedding the implanted
species; problems arise "when this photoresist has undergone an
implant step previously and heavy metal are embedded in the
photoresist and it has experienced high temperatures causing it to be
resistant to oxidizing" ([Wikipedia: Plasma ashing][wiki-ash]). If the
crusted wafer is heated quickly, solvent and nitrogen trapped in the
soft resist underneath blow the crust off in flakes ("popping") that
land elsewhere on the wafer as hard-to-remove particles. The standard
countermeasures are a low-temperature first ash step or a slow ramp,
forming-gas or H₂O-containing chemistries that penetrate the crust, and
a wet SPM follow-up, which is why implant strips are longer and more
carefully engineered than etch strips (Reinhardt and Kern, ch. 1
[kern-handbook]).

### Wet strip and clean chemistry

* **SPM (piranha)**: "a typical mixture is 3 parts of concentrated
  sulfuric acid and 1 part of 30 wt. % hydrogen peroxide solution",
  with 4:1 and 7:1 also used, and the exothermic mixing "can easily
  bring the solution temperature above 100 °C" ([Wikipedia: Piranha
  solution][wiki-piranha]). It dissolves organics by oxidation and
  leaves the silicon surface hydroxylated and hydrophilic with a thin
  chemical oxide. It is incompatible with exposed aluminium and
  titanium nitride.
* **SC-1 (APM)**: "5 parts of deionized water, 1 part of ammonia water
  (29% by weight of NH3), 1 part of aqueous H2O2 (hydrogen peroxide,
  30%) at 75 or 80 °C typically for 10 minutes" ([Wikipedia: RCA
  clean][wiki-rca]). It removes particles by continuously growing and
  under-cutting a chemical oxide, and organics by oxidation; dilute
  variants (1:1:50 and weaker) with megasonic agitation were standard by
  the 130 nm node to limit silicon roughening
  ([Kern 1990][kern1990]).
* **SC-2 (HPM)**: "6 parts of deionized water, 1 part of aqueous HCl
  (hydrochloric acid, 37% by weight), 1 part of aqueous H2O2 (hydrogen
  peroxide, 30%) at 75 or 80 °C" ([Wikipedia: RCA clean][wiki-rca]),
  which dissolves metallic contamination as chlorides. Werner Kern
  "developed the basic procedure in 1965 while working for RCA"
  ([Wikipedia: RCA clean][wiki-rca]; [Kern 1990][kern1990]).
* **Dilute HF**: a short dip removes the chemical oxide left by SC-1
  or SPM and leaves a hydrogen-terminated, hydrophobic surface; used
  as "HF-last" before gate oxidation and before silicide deposition.
* **Solvent and semi-aqueous strippers**: N-methyl-2-pyrrolidone
  (NMP), dimethyl sulfoxide (DMSO) and hydroxylamine- or amine-based
  formulations (EKC265, ACT) dissolve resist and etch polymers where
  acids cannot be used, principally after metal etch, and are followed
  by an IPA or water rinse ([Wikipedia: N-Methyl-2-pyrrolidone][wiki-nmp]).

### Nitride strip

The STI nitride ({ref}`ISONIT <step-003>`) is removed after the oxide
CMP in hot phosphoric acid — 85 % H₃PO₄ at 150–180 °C — which etches
Si₃N₄ at a few nanometres per minute with a selectivity to SiO₂ of the
order of 30:1 or better; the pad oxide underneath protects the silicon
and is later removed in HF (Wolf and Tauber, ch. 15; [Wikipedia:
Phosphoric acid][wiki-h3po4]). The bath temperature and its water
content (which the etch consumes) must be controlled, and the bath is
usually run with a reflux condenser and water spiking.

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
and metals as a critical-dimension issue in its own right
([ITRS 2001, Front End Processes][itrs2001-fep]).

## Typical equipment

* **Ashers**: downstream microwave strippers such as the Gasonics
  L3510 (a "production-proven downstream plasma photoresist ashing
  system" for 75–200 mm wafers [gasonics]) and the Gasonics Aura
  series; Mattson Aspen
  (ICP-based strip); Axcelis/Fusion ES and RadiantStrip; single-wafer
  RF ashers integrated onto etch platforms (Applied Materials ASP and
  Lam). University clean-room guides describe the class ([SNF:
  Downstream/remote plasma resist removal][snf-strip]).
* **Wet benches**: automated multi-tank benches with SPM, SC-1, SC-2,
  HF and hot-phosphoric tanks, quick-dump rinsers and IPA dryers —
  Akrion GAMA ([C2MI: Akrion GAMA acid bench][akrion]), SCP, DNS/Screen,
  Santa Clara Plastics, Semitool.
* **Spray processors** (FSI Mercury centrifugal spray) and
  **single-wafer spin processors** (SEZ, later Lam; DNS) for
  HF-based and solvent strips with better chemical freshness and no
  cross-contamination between wafers.
* **Metrology**: laser surface scanners for particles (KLA-Tencor
  Surfscan), TXRF and VPD-ICP-MS for surface metals, contact-angle
  and ellipsometric checks of the chemical oxide.

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

* W. Kern, "The Evolution of Silicon Wafer Cleaning Technology",
  *Journal of the Electrochemical Society* **137**, 1887–1892 (1990).
  <https://doi.org/10.1149/1.2086825>
* W. Kern and D. A. Puotinen, "Cleaning solutions based on hydrogen
  peroxide for use in silicon semiconductor technology", *RCA Review*
  **31**, 187–206 (1970).
* K. A. Reinhardt and W. Kern (eds.), *Handbook of Silicon Wafer
  Cleaning Technology*, 2nd ed., William Andrew, 2008 — ch. 1,
  W. Kern, "Overview and Evolution of Silicon Wafer Cleaning
  Technology". <https://doi.org/10.1016/b978-081551554-8.50004-5>
* *ITRS 2001 Edition: Front End Processes* (surface preparation).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
* SemiStar, "Gasonics L3510 plasma asher" (tool description; platen
  temperature 100–300 °C).
  <http://www.semistarcorp.com/product/gasonics-l3510-asher/>
* Allwin21, "Gasonics Aura 1000 Plasma Asher" (specification summary;
  temperature 150–300 °C typical).
  <https://allwin21.com/gasonics-aura-1000-plasma-asher-2/>
* Stanford Nanofabrication Facility, "Downstream/Remote Plasma Resist
  Removal". <https://snfguide.stanford.edu/guide/equipment/purpose/cleaning/resist-removal/dry-resist-removal/downstreamremote-plasma-resist-removal>
* C2MI, "Akrion GAMA acid bench".
  <https://www.c2mi.ca/en/equipement/akrion-gama-acid-bench/>

### High-level

* Wikipedia, "Plasma ashing".
  <https://en.wikipedia.org/wiki/Plasma_ashing>
* Wikipedia, "Piranha solution".
  <https://en.wikipedia.org/wiki/Piranha_solution>
* Wikipedia, "RCA clean". <https://en.wikipedia.org/wiki/RCA_clean>
* Wikipedia, "Hydrofluoric acid".
  <https://en.wikipedia.org/wiki/Hydrofluoric_acid>
* Wikipedia, "Phosphoric acid".
  <https://en.wikipedia.org/wiki/Phosphoric_acid>
* Wikipedia, "N-Methyl-2-pyrrolidone".
  <https://en.wikipedia.org/wiki/N-Methyl-2-pyrrolidone>
* Wikipedia, "Photoresist". <https://en.wikipedia.org/wiki/Photoresist>
* J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
  Technology*, Prentice Hall, 2000, ISBN 978-0-13-085037-9, ch. 4
  ("Semiconductor Manufacturing — Clean Rooms, Wafer Cleaning and
  Gettering").
* S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI Era,
  Vol. 1*, 2nd ed., Lattice Press, 2000, ISBN 978-0-9616721-6-4,
  ch. 15 ("Wet Processing: Cleaning, Etching and Liftoff").
* M. Quirk and J. Serda, *Semiconductor Manufacturing Technology*,
  Prentice Hall, 2001, ISBN 978-0-13-081520-0, ch. 7 and 16.
* H. Xiao, *Introduction to Semiconductor Manufacturing Technology*,
  2nd ed., SPIE Press, 2012, ch. 8. <https://doi.org/10.1117/3.924283>

### Deep dive

* Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
  Manufacturing Technology*, 2nd ed., CRC Press, 2007 (chapters on
  wafer cleaning and plasma stripping).
  <https://doi.org/10.1201/9781420017663>
* US Patent 5,498,308, "Plasma asher with microwave trap" (downstream
  microwave asher design).
  <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5498308>
* US Patent 7,449,416, "Apparatus and plasma ashing process for
  increasing photoresist removal rate" (implanted-resist strip).
  <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7449416>

[wiki-piranha]: https://en.wikipedia.org/wiki/Piranha_solution
[wiki-rca]: https://en.wikipedia.org/wiki/RCA_clean
[wiki-ash]: https://en.wikipedia.org/wiki/Plasma_ashing
[wiki-nmp]: https://en.wikipedia.org/wiki/N-Methyl-2-pyrrolidone
[wiki-h3po4]: https://en.wikipedia.org/wiki/Phosphoric_acid
[kern1990]: https://doi.org/10.1149/1.2086825
[kern-handbook]: https://doi.org/10.1016/b978-081551554-8.50004-5
[itrs2001-fep]: https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf
[gasonics]: http://www.semistarcorp.com/product/gasonics-l3510-asher/
[aura1000]: https://allwin21.com/gasonics-aura-1000-plasma-asher-2/
[snf-strip]: https://snfguide.stanford.edu/guide/equipment/purpose/cleaning/resist-removal/dry-resist-removal/downstreamremote-plasma-resist-removal
[akrion]: https://www.c2mi.ca/en/equipement/akrion-gama-acid-bench/
