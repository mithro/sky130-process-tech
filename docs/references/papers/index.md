<!-- Generated from data/papers.yaml by tools/gen_papers.py; do not edit. -->

(papers-index)=
# Academic paper index

Academic papers whose subject is SKY130 or the SkyWater 130 nm process:
device models and characterisation, test structures and reliability,
devices and circuits fabricated on the process with silicon results, and
the Cypress S8 lineage and the Bloomington fab. The list is a catalogue:
a paper is added to the {doc}`public sources inventory <../public-sources>`
only when a page cites it.

The index holds 49 papers: 40 paywalled, 9 free to read, and
12 with at least one free copy (preprint, repository or publisher).
Every entry was checked against its Crossref, arXiv or proceedings record.

## Other views

* {ref}`papers-by-topic`
* {ref}`papers-by-module`
* {ref}`papers-by-device`
* {ref}`papers-by-year`
* {ref}`papers-by-venue`
* {ref}`papers-by-institution`
* {ref}`papers-fab-publications`

```{toctree}
:hidden:

by-topic
by-module
by-device
by-year
by-venue
by-institution
fab-publications
```

## Scope

A paper is included when its subject is the open PDK and its models, a
device, test structure or reliability study on SKY130, a circuit
fabricated on the process with silicon or process-specific results, or
the S8 lineage and the Bloomington fab. Papers that only simulate with
the PDK, report no silicon or process results, concern another SkyWater
process, or are theses, datasets, slides or posters are left out.

Each entry states its **basis**, how its link to the process is
established:

* **Process named** (34 papers): the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Affiliation inference** (14 papers): the process or fab is not named; the link rests on author affiliations, as the entry's note explains.
* **Lineage inference** (1 paper): the process is not named; the link rests on public Cypress statements about the S8 lineage, as the entry's note explains.

Fabrication statements are quoted from the paper itself. Free copies are
limited to legitimate sources: arXiv, OSTI, institutional repositories,
preprint servers, open proceedings pages and open-access publisher
versions.

## How to read an entry

Each entry gives the full citation (authors, title, venue, volume,
issue, pages and year), the DOI, arXiv and publisher links, the free
copies with their host and open-access type, whether the version of
record is paywalled, the basis, the topics, the institutions named in
the author affiliations, the fabrication statement where the paper
gives one, the related pages of this reference, and the date and
source of verification.

## Counts

| Year | Papers |
|---|---|
| 1999 | 1 |
| 2001 | 1 |
| 2005 | 2 |
| 2006 | 3 |
| 2008 | 1 |
| 2019 | 2 |
| 2020 | 3 |
| 2021 | 3 |
| 2022 | 2 |
| 2023 | 9 |
| 2024 | 7 |
| 2025 | 9 |
| 2026 | 6 |

| Topic | Papers |
|---|---|
| PDK models and parameter extraction | 6 |
| Device characterisation | 10 |
| Test structures and test vehicles | 2 |
| Reliability and harsh environments | 3 |
| Radiation effects | 1 |
| Cryogenic operation | 4 |
| RRAM (ReRAM) | 9 |
| SONOS memory | 1 |
| Floating-gate devices | 2 |
| BEOL-integrated devices | 3 |
| Analog and RF circuits | 5 |
| Data converters and mixed-signal circuits | 4 |
| Power management | 2 |
| Digital circuits | 12 |
| Memory | 3 |
| Sensors | 4 |
| Quantum | 1 |
| Hardware security | 2 |
| Open-source tooling | 8 |
| Shuttle programmes and education | 1 |
| Cypress S8 lineage | 8 |
| Fab manufacturing | 10 |

## All papers

Sorted by first author's family name, then year.

(paper-akturk-2023a)=
### Cryogenic Modeling for Open-Source Process Design Kit Technology

Akin Akturk, Ayushman Tripathi and Mehdi Saligane. "Cryogenic Modeling for Open-Source Process Design Kit Technology." *2023 IEEE BiCMOS and Compound Semiconductor Integrated Circuits and Technology Symposium (BCICTS)*, pp. 58–65, 2023.

* **Links:** DOI [10.1109/bcicts54660.2023.10310944](https://doi.org/10.1109/bcicts54660.2023.10310944) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10310944/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Cryogenic operation <papers-topic-cryogenic>`, {ref}`PDK models and parameter extraction <papers-topic-pdk-models>`, {ref}`Device characterisation <papers-topic-device-characterisation>`, {ref}`Analog and RF circuits <papers-topic-analog-rf>`
* **Institutions:** CoolCAD Electronics; University of Michigan
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/bcicts54660.2023.10310944 resolved; title matches Crossref and OpenAlex

(paper-alshaya-2022a)=
### RRAM, Device, Model and Memory

Abdulaziz Alshaya, Qihao Han and Christos Papavassiliou. "RRAM, Device, Model and Memory." *2022 International Conference on Microelectronics (ICM)*, pp. 117–120, 2022.

* **Links:** DOI [10.1109/icm56065.2022.10005367](https://doi.org/10.1109/icm56065.2022.10005367) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10005367/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`PDK models and parameter extraction <papers-topic-pdk-models>`
* **Institutions:** Imperial College London
* **Related pages:**
  * {ref}`overview-sky130b-reram` — The overview page describes the sky130B ReRAM module whose device model this paper exercises.
* **Note:** Borderline inclusion. Simulation of the PDK's SkyWater memristor model (1R and 1T1R read and write); no silicon.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/icm56065.2022.10005367 resolved; title matches Crossref and OpenAlex

(paper-beall-2026a)=
### DC Cryogenic Modeling of Open-Source SkyWater 130 nm MOSFETs at 77 K Using BSIM4

F. Beall, A. Rimal, O. Seidel, Y. Mei, A. D. McDonald, I. Parmaksiz, V. A. Chirayath, J. Asaadi, D. Braga and J. B. R. Battat. "DC Cryogenic Modeling of Open-Source SkyWater 130 nm MOSFETs at 77 K Using BSIM4." *arXiv*, 2026.

* **Links:** arXiv [2604.21625](https://arxiv.org/abs/2604.21625)
* **Free copies:** free at the publisher or proceedings page (arxiv.org; preprint (arXiv)); [www.osti.gov](https://www.osti.gov/servlets/purl/3363571) (repository copy (OSTI))
* **Access:** free to read
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Cryogenic operation <papers-topic-cryogenic>`, {ref}`PDK models and parameter extraction <papers-topic-pdk-models>`, {ref}`Device characterisation <papers-topic-device-characterisation>`
* **Institutions:** University of Texas at Arlington; Rice University; Fermi National Accelerator Laboratory; Wellesley College
* **Verified:** 2026-09-14 arXiv abs page 2604.21625 resolved; title matches arXiv and the OpenAlex record for DOI 10.48550/arXiv.2604.21625

(paper-blocklove-2024a)=
### Evaluating LLMs for Hardware Design and Test

Jason Blocklove, Siddharth Garg, Ramesh Karri and Hammond Pearce. "Evaluating LLMs for Hardware Design and Test." *2024 IEEE LLM Aided Design Workshop (LAD)*, pp. 1–6, 2024.

* **Links:** DOI [10.1109/lad62341.2024.10691811](https://doi.org/10.1109/lad62341.2024.10691811) · arXiv [2405.02326](https://arxiv.org/abs/2405.02326) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10691811/)
* **Free copies:** arXiv (arxiv.org; preprint (arXiv))
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Digital circuits <papers-topic-digital>`, {ref}`Open-source tooling <papers-topic-tooling>`
* **Institutions:** New York University; University of New South Wales
* **Fabrication (quoted from the abstract):** "We taped out the benchmarks on a Skywater 130nm shuttle and received the functional chip."
* **Note:** Borderline inclusion. An LLM benchmarking paper; included because the abstract reports a functional chip from a SkyWater 130 nm shuttle.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/lad62341.2024.10691811 resolved; title matches Crossref and OpenAlex; arXiv abs page 2405.02326 title matches

(paper-bloomer-2026a)=
### Ising-ReRAM: A Low Power Ising Machine ReRAM Crossbar for NP Problems

Everest Bloomer, Irem Didin, Ching-Yi Lin and Sahil Shah. "Ising-ReRAM: A Low Power Ising Machine ReRAM Crossbar for NP Problems." *arXiv*, 2026.

* **Links:** arXiv [2603.12415](https://arxiv.org/abs/2603.12415)
* **Free copies:** free at the publisher or proceedings page (arxiv.org; preprint (arXiv))
* **Access:** free to read
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`RRAM (ReRAM) <papers-topic-rram>`, {ref}`Device characterisation <papers-topic-device-characterisation>`
* **Institutions:** University of Maryland, College Park
* **Related pages:**
  * {ref}`overview-sky130b-reram` — The crossbar is a ReRAM array fabricated in the Skywater 130 nm process; the overview page describes the sky130B ReRAM module.
* **Verified:** 2026-09-14 arXiv abs page 2603.12415 resolved; title matches arXiv and the OpenAlex record for DOI 10.48550/arXiv.2603.12415

(paper-castoria-2025a)=
### Selective Shuttling of Electrons on Helium Using a CMOS Control Platform

K. E. Castoria, H. Byeon, N. R. Beysengulov, E. O. Glen, M. Sammon, J. Pollanen, D. G. Rees and S. A. Lyon. "Selective Shuttling of Electrons on Helium Using a CMOS Control Platform." *arXiv*, 2025.

* **Links:** arXiv [2511.15922](https://arxiv.org/abs/2511.15922)
* **Free copies:** free at the publisher or proceedings page (arxiv.org; preprint (arXiv))
* **Access:** free to read
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Quantum <papers-topic-quantum>`, {ref}`Cryogenic operation <papers-topic-cryogenic>`, {ref}`Sensors <papers-topic-sensors>`
* **Institutions:** EeroQ Corporation
* **Fabrication (quoted from the HTML full text):** "The CMOS control chip \[…\] was fabricated using the SKY130 130 nm CMOS process at the SkyWater Technologies silicon foundry"
* **Verified:** 2026-09-14 arXiv abs page 2511.15922 resolved; title matches arXiv and the OpenAlex record for DOI 10.48550/arXiv.2511.15922

(paper-chen-2023a)=
### An Open-Source 4 × 8 Coarse-Grained Reconfigurable Array Using SkyWater 130 nm Technology and Agile Hardware Design Flow

Po-Han Chen, Charles Tsao and Priyanka Raina. "An Open-Source 4 × 8 Coarse-Grained Reconfigurable Array Using SkyWater 130 nm Technology and Agile Hardware Design Flow." *2023 IEEE International Symposium on Circuits and Systems (ISCAS)*, pp. 1–5, 2023.

* **Links:** DOI [10.1109/iscas46773.2023.10182052](https://doi.org/10.1109/iscas46773.2023.10182052) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10182052/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Digital circuits <papers-topic-digital>`
* **Institutions:** Stanford University
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/iscas46773.2023.10182052 resolved; title matches Crossref and OpenAlex

(paper-chen-2024a)=
### Open-source floating-gate cell for analogue synapses

Matthew Chen, Charana Sonnadara and Sahil Shah. "Open-source floating-gate cell for analogue synapses." *Electronics Letters*, vol. 60, no. 17, art. no. e70036, 2024.

* **Links:** DOI [10.1049/ell2.70036](https://doi.org/10.1049/ell2.70036) · [publisher or proceedings page](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/ell2.70036)
* **Free copies:** [onlinelibrary.wiley.com](https://onlinelibrary.wiley.com/doi/pdfdirect/10.1049/ell2.70036) (gold (publisher version)); [www.authorea.com](https://www.authorea.com/doi/full/10.22541/au.172413095.53999511/v1) (preprint)
* **Access:** free to read
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Floating-gate devices <papers-topic-floating-gate>`, {ref}`Device characterisation <papers-topic-device-characterisation>`
* **Institutions:** University of Maryland, College Park
* **Verified:** 2026-09-14 Crossref REST API works/10.1049/ell2.70036 resolved; title matches Crossref and OpenAlex

(paper-choi-2025a)=
### Foundry Monolithic 3D Unlocks Large Throughput Benefits: 3D Memory with Tucked Sense Amplifiers + Logic using Heterogeneous Silicon CMOS + Resistive RAM + Carbon Nanotube FETs

S. Choi, A. Raut, T. Wu, S. Dayo, A. Bechdolt, G. Dutta, S. Li, D. T. Rich, R. H. Yang, A. C. Yu, M. Nelson, M. M. Shulaker, R. M. Radway, S. Mitra and T. Srimani. "Foundry Monolithic 3D Unlocks Large Throughput Benefits: 3D Memory with Tucked Sense Amplifiers + Logic using Heterogeneous Silicon CMOS + Resistive RAM + Carbon Nanotube FETs." *2025 IEEE International Electron Devices Meeting (IEDM)*, pp. 1–4, 2025.

* **Links:** DOI [10.1109/iedm50572.2025.11353729](https://doi.org/10.1109/iedm50572.2025.11353729) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/11353729/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`BEOL-integrated devices <papers-topic-beol-integration>`, {ref}`RRAM (ReRAM) <papers-topic-rram>`
* **Institutions:** Stanford University; Carnegie Mellon University; Massachusetts Institute of Technology; SkyWater Technology
* **Fabrication (quoted from the abstract):** "This is achieved at SkyWater Technology Foundry using a 90/130 nm process on 200 mm wafers."
* **Related pages:**
  * {ref}`overview-sky130b-reram` — The overview page describes the BEOL ReRAM tier; this work integrates RRAM and CNFETs in the BEOL at SkyWater.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/iedm50572.2025.11353729 resolved; title matches Crossref and OpenAlex

(paper-cirimelli-low-2023a)=
### SRAM Design with OpenRAM in SkyWater 130nm

Jesse Cirimelli-Low, Muhammad Hadir Khan, Samuel Crow, Amogh Lonkar, Bugra Onal, Andrew D. Zonenberg and Matthew R. Guthaus. "SRAM Design with OpenRAM in SkyWater 130nm." *2023 IEEE International Symposium on Circuits and Systems (ISCAS)*, pp. 1–5, 2023.

* **Links:** DOI [10.1109/iscas46773.2023.10181379](https://doi.org/10.1109/iscas46773.2023.10181379) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10181379/)
* **Free copies:** [escholarship.org](https://escholarship.org/uc/item/9dc0v8g3) (preprint)
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Memory <papers-topic-memory>`, {ref}`Digital circuits <papers-topic-digital>`, {ref}`Open-source tooling <papers-topic-tooling>`
* **Institutions:** University of California, Santa Cruz; IOActive
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/iscas46773.2023.10181379 resolved; title matches Crossref and OpenAlex

(paper-conway-2020a)=
### Effect of Sparse or Asymmetric Sampling on the Estimation of Photolithography Overlay Regression Parameters

Tim Conway. "Effect of Sparse or Asymmetric Sampling on the Estimation of Photolithography Overlay Regression Parameters." *2020 31st Annual SEMI Advanced Semiconductor Manufacturing Conference (ASMC)*, pp. 1–6, 2020.

* **Links:** DOI [10.1109/asmc49169.2020.9185229](https://doi.org/10.1109/asmc49169.2020.9185229) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/9185229/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. Borderline inclusion. Fab publication: the author is affiliated with SkyWater Technology; the abstract does not name a process.
* **Topics:** {ref}`Fab manufacturing <papers-fab-publications>`
* **Institutions:** SkyWater Technology
* **Related pages:**
  * {ref}`machine-cd-sem-overlay-metrology` — The paper studies metrology sampling plans for photolithography overlay feedback control.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/asmc49169.2020.9185229 resolved; title matches Crossref and OpenAlex

(paper-didin-2026a)=
### Characterization and Modeling of Multilevel Analog ReRAM Synapses in the Sky130 Process

Irem Didin, Carl Brando, Ching-Yi Lin and Sahil Shah. "Characterization and Modeling of Multilevel Analog ReRAM Synapses in the Sky130 Process." *IEEE Journal on Exploratory Solid-State Computational Devices and Circuits*, vol. 12, pp. 27–35, 2026.

* **Links:** DOI [10.1109/jxcdc.2026.3670667](https://doi.org/10.1109/jxcdc.2026.3670667) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/11421367/)
* **Free copies:** free at the publisher or proceedings page (ieeexplore.ieee.org; gold (publisher version)); [www.techrxiv.org](https://www.techrxiv.org/doi/full/10.36227/techrxiv.176539494.47601473/v1) (preprint)
* **Access:** free to read
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`RRAM (ReRAM) <papers-topic-rram>`, {ref}`Device characterisation <papers-topic-device-characterisation>`, {ref}`PDK models and parameter extraction <papers-topic-pdk-models>`
* **Institutions:** University of Maryland, College Park
* **Related pages:**
  * {ref}`overview-sky130b-reram` — The paper characterises ReRAM devices fabricated in the SkyWater 130 nm process; the overview page describes the sky130B ReRAM module.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/jxcdc.2026.3670667 resolved; title matches Crossref and OpenAlex

(paper-edwards-2020a)=
### Google/SkyWater and the Promise of the Open PDK

Tim Edwards. "Google/SkyWater and the Promise of the Open PDK." *Workshop on Open-Source EDA Technology (WOSET 2020)*, 2020.

* **Links:** [publisher or proceedings page](https://woset-workshop.github.io/WOSET2020.html)
* **Free copies:** [woset-workshop.github.io](https://woset-workshop.github.io/PDFs/2020/a03.pdf) (conference open-access page)
* **Access:** free to read
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`PDK models and parameter extraction <papers-topic-pdk-models>`, {ref}`Open-source tooling <papers-topic-tooling>`
* **Institutions:** Open Circuit Design; Efabless
* **Related pages:**
  * {ref}`overview-cross-section` — The paper's first figure is a process stack of the SkyWater 130 nm open process, the subject of the overview's cross-section.
* **Verified:** 2026-09-14 WOSET proceedings page lists the title and authors; PDF fetched (HTTP 200)

(paper-fliesler-2008a)=
### A 15ns 4Mb NVSRAM in 0.13u SONOS Technology

Michael Fliesler, David Still and Jeong-Mo Hwang. "A 15ns 4Mb NVSRAM in 0.13u SONOS Technology." *2008 Joint Non-Volatile Semiconductor Memory Workshop and International Conference on Memory Technology and Design*, 2008.

* **Links:** DOI [10.1109/nvsmw.2008.30](https://doi.org/10.1109/nvsmw.2008.30) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/4531830/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** lineage inference — the process is not named; the link rests on public Cypress statements about the S8 lineage. The abstract describes a SONOS-based 4 Mb nvSRAM in "0.13u SONOS Technology" from Cypress and Simtek authors; that this is the S8 process is an inference from Cypress product coverage of its 4-Mbit nvSRAMs (inventory CYP-20), which says they are "the first manufactured on Cypress's S8(tm) 0.13-micron SONOS" technology, not a statement of the paper.
* **Topics:** {ref}`Cypress S8 lineage <papers-topic-lineage-s8>`, {ref}`SONOS memory <papers-topic-sonos>`, {ref}`Memory <papers-topic-memory>`
* **Institutions:** Cypress Semiconductor (San Jose, California); Simtek Corporation
* **Related pages:**
  * {ref}`step-040` — If, as Cypress's 2007 product coverage suggests (inventory CYP-20), the nvSRAM was made in S8, its SONOS stack is the one the ONO step page describes; the paper does not name the process.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/nvsmw.2008.30 resolved; title matches Crossref and OpenAlex

(paper-grenci-2001a)=
### Polymer control in aluminum etch chambers to achieve \<450 hours MTBC

C. Grenci, V. Sauers, R. King, D. Dodge, M. Schlecht, K. Gray and R. Foley. "Polymer control in aluminum etch chambers to achieve \<450 hours MTBC." *2001 IEEE International Symposium on Semiconductor Manufacturing. ISSM 2001. Conference Proceedings (Cat. No.01CH37203)*, pp. 313–316, 2001.

* **Links:** DOI [10.1109/issm.2001.962975](https://doi.org/10.1109/issm.2001.962975) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/962975/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. Fab publication: the Cypress co-authors are affiliated with Cypress Semiconductor, Bloomington, MN. The abstract does not name a process.
* **Topics:** {ref}`Cypress S8 lineage <papers-topic-lineage-s8>`, {ref}`Fab manufacturing <papers-fab-publications>`
* **Institutions:** Galiso, Inc.; Cypress Semiconductor (Bloomington, Minnesota)
* **Related pages:**
  * {ref}`machine-plasma-etcher-metal` — The paper reports polymer control and mean time between cleans in aluminium etch chambers.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/issm.2001.962975 resolved; title matches Crossref and OpenAlex

(paper-gross-2021a)=
### Fab Fingerprint for Proactive Yield Management

David Gross, Katherine Gramling and Prasad L. Bachiraju. "Fab Fingerprint for Proactive Yield Management." *2021 32nd Annual SEMI Advanced Semiconductor Manufacturing Conference (ASMC)*, pp. 1–4, 2021.

* **Links:** DOI [10.1109/asmc51741.2021.9435686](https://doi.org/10.1109/asmc51741.2021.9435686) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/9435686/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. Borderline inclusion. Fab publication: authors affiliated with SkyWater Technology and Onto Innovation; the abstract does not name a process.
* **Topics:** {ref}`Fab manufacturing <papers-fab-publications>`
* **Institutions:** SkyWater Technology; Onto Innovation
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/asmc51741.2021.9435686 resolved; title matches Crossref and OpenAlex

(paper-grover-2019a)=
### Optimization of Metal Photo Rework Dry Strip Scheme for Yield Improvement

Sidhant Grover and Philip Thompson. "Optimization of Metal Photo Rework Dry Strip Scheme for Yield Improvement." *2019 30th Annual SEMI Advanced Semiconductor Manufacturing Conference (ASMC)*, pp. 1–4, 2019.

* **Links:** DOI [10.1109/asmc.2019.8791800](https://doi.org/10.1109/asmc.2019.8791800) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/8791800/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. Fab publication: authors affiliated with Fab Module Engineering, SkyWater Technology Foundry, Bloomington, Minnesota. The abstract covers 90-130 nm technology nodes without naming a process.
* **Topics:** {ref}`Fab manufacturing <papers-fab-publications>`
* **Institutions:** SkyWater Technology
* **Related pages:**
  * {ref}`machine-downstream-plasma-asher` — The paper changes the dry strip chamber temperature used to rework patterned Al-0.5 wt% Cu metal wafers.
  * {ref}`category-strip` — Resist strip on metal layers is the step the rework scheme modifies.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/asmc.2019.8791800 resolved; title matches Crossref and OpenAlex

(paper-hasler-2024a)=
### A 130nm CMOS Programmable Analog Standard Cell Library

Jennifer Hasler, Praveen Raj Ayyappan, Afolabi Ige and Pranav Mathews. "A 130nm CMOS Programmable Analog Standard Cell Library." *IEEE Transactions on Circuits and Systems I: Regular Papers*, vol. 71, no. 6, pp. 2497–2510, 2024.

* **Links:** DOI [10.1109/tcsi.2024.3355070](https://doi.org/10.1109/tcsi.2024.3355070) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10431551/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Analog and RF circuits <papers-topic-analog-rf>`, {ref}`Open-source tooling <papers-topic-tooling>`
* **Institutions:** Georgia Institute of Technology
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/tcsi.2024.3355070 resolved; title matches Crossref and OpenAlex

(paper-hossain-2026a)=
### SPORT: Spherical-PSNR-Optimized tRuncaTion for Power-Efficient 360-Degree Video Systems

Md. Sajjad Hossain, Hasibur Rahman Hemel, Kyle Mooney, Yiwen Xu, William Oswald, Mario Renteria-Pinon, Hritom Das, Zhenlin Pei, Jinhui Wang and Na Gong. "SPORT: Spherical-PSNR-Optimized tRuncaTion for Power-Efficient 360-Degree Video Systems." *arXiv*, 2026.

* **Links:** arXiv [2606.24916](https://arxiv.org/abs/2606.24916)
* **Free copies:** free at the publisher or proceedings page (arxiv.org; preprint (arXiv))
* **Access:** free to read
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Memory <papers-topic-memory>`, {ref}`Digital circuits <papers-topic-digital>`
* **Institutions:** University of Alabama; New Mexico State University; Oklahoma State University
* **Note:** Borderline inclusion. A video-system paper validated on an SRAM ASIC fabricated in SkyWater 130 nm CMOS.
* **Verified:** 2026-09-14 arXiv abs page 2606.24916 resolved; title matches arXiv and the OpenAlex record for DOI 10.48550/arXiv.2606.24916

(paper-hsieh-2019a)=
### High-Density Multiple Bits-per-Cell 1T4R RRAM Array with Gradual SET/RESET and its Effectiveness for Deep Learning

E.R. Hsieh, M. Giordano, B. Hodson, A. Levy, S.K. Osekowsky, R.M. Radway, Y.C. Shih, W. Wan, T. F. Wu, X. Zheng, M. Nelson, B.Q. Le, H.-S.P. Wong, S. Mitra and S. Wong. "High-Density Multiple Bits-per-Cell 1T4R RRAM Array with Gradual SET/RESET and its Effectiveness for Deep Learning." *2019 IEEE International Electron Devices Meeting (IEDM)*, pp. 35.6.1–35.6.4, 2019.

* **Links:** DOI [10.1109/iedm19573.2019.8993514](https://doi.org/10.1109/iedm19573.2019.8993514) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/8993514/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. The abstract says only "a logic foundry technology"; the basis is the SkyWater Technology Foundry co-author affiliations and the SkyWater ReRAM documentation, which reproduces a figure from this paper (inventory HSIEH-2019). That the foundry is SkyWater is not stated in the abstract.
* **Topics:** {ref}`RRAM (ReRAM) <papers-topic-rram>`, {ref}`Device characterisation <papers-topic-device-characterisation>`
* **Institutions:** Stanford University; SkyWater Technology
* **Related pages:**
  * {ref}`overview-sky130b-reram` — The SkyWater ReRAM documentation cited on the overview page reproduces a figure from this paper.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/iedm19573.2019.8993514 resolved; title matches Crossref and OpenAlex

(paper-hsieh-2021a)=
### Four-Bits-Per-Memory One-Transistor-and-Eight-Resistive-Random-Access-Memory (1T8R) Array

E. R. Hsieh, X. Zheng, B. Q. Le, Y. C. Shih, R. M. Radway, M. Nelson, S. Mitra and S. Wong. "Four-Bits-Per-Memory One-Transistor-and-Eight-Resistive-Random-Access-Memory (1T8R) Array." *IEEE Electron Device Letters*, vol. 42, no. 3, pp. 335–338, 2021.

* **Links:** DOI [10.1109/led.2021.3055017](https://doi.org/10.1109/led.2021.3055017) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/9336666/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. The abstract says "a foundry logic technology"; a SkyWater Technology Foundry co-author affiliation is the basis for inclusion. That the foundry is SkyWater is not stated in the abstract.
* **Topics:** {ref}`RRAM (ReRAM) <papers-topic-rram>`, {ref}`Device characterisation <papers-topic-device-characterisation>`
* **Institutions:** National Central University; Stanford University; San José State University; Taiwan Semiconductor Manufacturing Company; SkyWater Technology
* **Related pages:**
  * {ref}`overview-sky130b-reram` — The paper reports RRAM arrays in a foundry process with a SkyWater co-author; the overview page describes the sky130B ReRAM module, and that these arrays use it is not stated.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/led.2021.3055017 resolved; title matches Crossref and OpenAlex

(paper-irfansyah-2025a)=
### A Silicon-Proven Wide-Range Voltage Controlled Oscillator Designed Using Open-Source CMOS 130nm PDK

Astria Nur Irfansyah. "A Silicon-Proven Wide-Range Voltage Controlled Oscillator Designed Using Open-Source CMOS 130nm PDK." *2025 International Symposium on Intelligent Signal Processing and Communication Systems (ISPACS)*, pp. 1–4, 2025.

* **Links:** DOI [10.1109/ispacs68724.2025.11383342](https://doi.org/10.1109/ispacs68724.2025.11383342) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/11383342/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Analog and RF circuits <papers-topic-analog-rf>`
* **Institutions:** Institut Teknologi Sepuluh Nopember
* **Fabrication (quoted from the abstract):** "The VCO design is included in a test-chip fabricated through the Tinytapeout community-driven shuttle service."
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/ispacs68724.2025.11383342 resolved; title matches Crossref and OpenAlex

(paper-ivanov-2006a)=
### Electrical conductivity of high aspect ratio trenches in chemical-vapor deposition W technology

Ivan P. Ivanov, Indradeep Sen and Peter Keswick. "Electrical conductivity of high aspect ratio trenches in chemical-vapor deposition W technology." *Journal of Vacuum Science & Technology B: Microelectronics and Nanometer Structures Processing, Measurement, and Phenomena*, vol. 24, no. 2, pp. 523–533, 2006.

* **Links:** DOI [10.1116/1.2166859](https://doi.org/10.1116/1.2166859) · [publisher or proceedings page](https://pubs.aip.org/jvb/article/24/2/523/930553/Electrical-conductivity-of-high-aspect-ratio)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. Fab publication: authors affiliated with Cypress Semiconductor Corporation, 2401 East 86th Street, Bloomington, Minnesota (the fab's address). The abstract does not name the S8 process.
* **Topics:** {ref}`Cypress S8 lineage <papers-topic-lineage-s8>`, {ref}`Fab manufacturing <papers-fab-publications>`
* **Institutions:** Cypress Semiconductor (Bloomington, Minnesota)
* **Related pages:**
  * {ref}`machine-tungsten-cvd` — The paper studies CVD tungsten trench fills with a TiN barrier, nucleation W and bulk W.
* **Verified:** 2026-09-14 Crossref REST API works/10.1116/1.2166859 resolved; title matches Crossref and OpenAlex

(paper-jagielski-2024a)=
### Integrating Asynchronous Circuits into the Caravel Testing Harness

Thomas Jagielski, Xiayuan Wen, Matthew Dobre and Rajit Manohar. "Integrating Asynchronous Circuits into the Caravel Testing Harness." *Workshop on Open-Source EDA Technology (WOSET 2024)*, 2024.

* **Links:** [publisher or proceedings page](https://woset-workshop.github.io/WOSET2024.html)
* **Free copies:** [woset-workshop.github.io](https://woset-workshop.github.io/PDFs/2024/8_Integrating_Asynchronous_Cir.pdf) (conference open-access page)
* **Access:** free to read
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Open-source tooling <papers-topic-tooling>`, {ref}`Digital circuits <papers-topic-digital>`
* **Institutions:** Yale University
* **Note:** Borderline inclusion. No silicon results; included for SKY130-specific integration findings in the full text: the provided fill scripts "could not meet the density requirements", so the authors developed custom fill insertion, and a power ring was needed for technologies "with fewer number of metal layers like SKY130".
* **Verified:** 2026-09-14 WOSET proceedings page lists the title and authors; PDF fetched (HTTP 200)

(paper-karatas-2025a)=
### Silicon-Proven Chaos-Based Random Number Generator Using the Sky130 PDK

Onur Karataş, Sezen Bal and Hayriye Korkmaz. "Silicon-Proven Chaos-Based Random Number Generator Using the Sky130 PDK." *2025 12th International Conference on Electrical and Electronics Engineering (ICEEE)*, pp. 85–88, 2025.

* **Links:** DOI [10.1109/iceee67194.2025.11261982](https://doi.org/10.1109/iceee67194.2025.11261982) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/11261982/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Digital circuits <papers-topic-digital>`, {ref}`Hardware security <papers-topic-security>`
* **Institutions:** Marmara University
* **Fabrication (quoted from the abstract):** "designed, fabricated, and validated via the Efabless Open Multi-Project Wafer (MPW) shuttle program using the Sky130 Process Design Kit (PDK)"
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/iceee67194.2025.11261982 resolved; title matches Crossref and OpenAlex

(paper-le-2021a)=
### RADAR: A Fast and Energy-Efficient Programming Technique for Multiple Bits-Per-Cell RRAM Arrays

Binh Q. Le, Akash Levy, Tony F. Wu, Robert M. Radway, E. Ray Hsieh, Xin Zheng, Mark Nelson, Priyanka Raina, H.-S. Philip Wong, Simon Wong and Subhasish Mitra. "RADAR: A Fast and Energy-Efficient Programming Technique for Multiple Bits-Per-Cell RRAM Arrays." *IEEE Transactions on Electron Devices*, vol. 68, no. 9, pp. 4397–4403, 2021.

* **Links:** DOI [10.1109/ted.2021.3097975](https://doi.org/10.1109/ted.2021.3097975) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/9497347/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. The abstract reports arrays "fabricated in a 130-nm CMOS process"; a SkyWater Technology Foundry co-author affiliation is the basis for inclusion. The foundry is not named in the abstract.
* **Topics:** {ref}`RRAM (ReRAM) <papers-topic-rram>`, {ref}`Device characterisation <papers-topic-device-characterisation>`
* **Institutions:** San José State University; Stanford University; Facebook, Inc.; National Central University; SkyWater Technology
* **Related pages:**
  * {ref}`overview-sky130b-reram` — The paper reports HfO2-based RRAM arrays in a 130 nm process with a SkyWater co-author; the overview page describes the sky130B ReRAM module, and that these arrays use it is not stated.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/ted.2021.3097975 resolved; title matches Crossref and OpenAlex

(paper-li-2025a)=
### Open-ALOE: An Analog Layout Automation Flow for the Open-Source Ecosystem

Yueting Li, Xingyu Ni, Sara Achour and Boris Murmann. "Open-ALOE: An Analog Layout Automation Flow for the Open-Source Ecosystem." *2025 26th International Symposium on Quality Electronic Design (ISQED)*, pp. 1–6, 2025.

* **Links:** DOI [10.1109/isqed65160.2025.11014456](https://doi.org/10.1109/isqed65160.2025.11014456) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/11014456/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Analog and RF circuits <papers-topic-analog-rf>`, {ref}`Open-source tooling <papers-topic-tooling>`
* **Institutions:** University of California, Berkeley; Stanford University; University of Hawaiʻi at Mānoa
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/isqed65160.2025.11014456 resolved; title matches Crossref and OpenAlex

(paper-maldonado-2026a)=
### Design, Implementation and Verification of an Open-Source ASIC for Grayscale and Sobel Edge Detection

Diana N. Maldonado R., Sebastián Eslava G. and Kevin D. Patino-Sosa. "Design, Implementation and Verification of an Open-Source ASIC for Grayscale and Sobel Edge Detection." *2026 IEEE 17th Latin America Symposium on Circuits and System (LASCAS)*, pp. 1–5, 2026.

* **Links:** DOI [10.1109/lascas67804.2026.11457090](https://doi.org/10.1109/lascas67804.2026.11457090) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/11457090/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Digital circuits <papers-topic-digital>`
* **Institutions:** Universidad Nacional de Colombia; Georgia Institute of Technology
* **Fabrication (quoted from the abstract):** "on the SkyWater 130 nm open PDK, implemented with OpenLane and fabricated via TinyTapeout"
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/lascas67804.2026.11457090 resolved; title matches Crossref and OpenAlex

(paper-marin-2024a)=
### Open-Source Multilevel Converter Power IC Design and Test

Jorge Marin, Christian A. Rojas, Alan H. Wilson-Veas, Nelson Salvador, Joel Gak, Nicolas Calarco, Matias Miguez and Alejandro R. Oliva. "Open-Source Multilevel Converter Power IC Design and Test." *IEEE Design & Test*, vol. 41, no. 6, pp. 19–27, 2024.

* **Links:** DOI [10.1109/mdat.2024.3405892](https://doi.org/10.1109/mdat.2024.3405892) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10539610/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Power management <papers-topic-power-management>`
* **Institutions:** Universidad Técnica Federico Santa María; Universidad Católica del Uruguay; Universidad Nacional del Sur; CONICET
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/mdat.2024.3405892 resolved; title matches Crossref and OpenAlex

(paper-mathews-2024a)=
### A 65nm and 130nm CMOS Programmable Analog Standard Cell Library for Scalable System Synthesis

Pranav Mathews, Praveen Raj Ayyappan, Afolabi Ige, Swagat Bhattacharyya, Linhao Yang and Jennifer Hasler. "A 65nm and 130nm CMOS Programmable Analog Standard Cell Library for Scalable System Synthesis." *2024 IEEE Custom Integrated Circuits Conference (CICC)*, pp. 1–2, 2024.

* **Links:** DOI [10.1109/cicc60959.2024.10529028](https://doi.org/10.1109/cicc60959.2024.10529028) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10529028/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Floating-gate devices <papers-topic-floating-gate>`, {ref}`Analog and RF circuits <papers-topic-analog-rf>`
* **Institutions:** Georgia Institute of Technology
* **Note:** Borderline inclusion. The abstract names a library developed in 65 nm CMOS and SkyWater 130 nm with floating-gate devices but does not state silicon results.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/cicc60959.2024.10529028 resolved; title matches Crossref and OpenAlex

(paper-mathur-2005a)=
### One Time Programming Device Yield Study Based On Anti-Fuse Gate Oxide Breakdown on P-type and N-type Substrates

N. Mathur, Y. Ahn, I. Kouznetov, F. Jenne and J. Fulford. "One Time Programming Device Yield Study Based On Anti-Fuse Gate Oxide Breakdown on P-type and N-type Substrates." *2005 IEEE International Integrated Reliability Workshop*, pp. 111–113, 2005.

* **Links:** DOI [10.1109/irws.2005.1609576](https://doi.org/10.1109/irws.2005.1609576) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/1609576/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. Fab publication: authors affiliated with Cypress Semiconductor, Bloomington, MN. The abstract does not name a process.
* **Topics:** {ref}`Cypress S8 lineage <papers-topic-lineage-s8>`, {ref}`Fab manufacturing <papers-fab-publications>`, {ref}`Reliability and harsh environments <papers-topic-reliability>`, {ref}`Device characterisation <papers-topic-device-characterisation>`
* **Institutions:** Cypress Semiconductor (Bloomington, Minnesota)
* **Related pages:**
  * {ref}`category-oxidation` — The OTP device's programming relies on breakdown of the gate oxide that the oxidation category covers.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/irws.2005.1609576 resolved; title matches Crossref and OpenAlex

(paper-montanares-2025a)=
### Open-Source 4 K CMOS Calibration: Integrating IceMOS and Sky130 PDK

Mauricio Montanares, V.H. Arzate Palma, Kevin G. McCarthy and Gerardo Molina Salgado. "Open-Source 4 K CMOS Calibration: Integrating IceMOS and Sky130 PDK." *2025 IFIP/IEEE 33rd International Conference on Very Large Scale Integration (VLSI-SoC)*, pp. 1–5, 2025.

* **Links:** DOI [10.1109/vlsi-soc64688.2025.11421773](https://doi.org/10.1109/vlsi-soc64688.2025.11421773) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/11421773/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Cryogenic operation <papers-topic-cryogenic>`, {ref}`PDK models and parameter extraction <papers-topic-pdk-models>`, {ref}`Device characterisation <papers-topic-device-characterisation>`
* **Institutions:** Microelectronics Circuits Centre Ireland (MCCI); University College Cork
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/vlsi-soc64688.2025.11421773 resolved; title matches Crossref and OpenAlex

(paper-munoz-2026a)=
### Testbed for Custom Open-Source Power Management Integrated Circuit in Harsh Space Environments

Ítalo Muñoz, Jorge Marin, Felipe Illanes, Marcos Díaz Quezada and Christian A. Rojas. "Testbed for Custom Open-Source Power Management Integrated Circuit in Harsh Space Environments." *2026 Argentine Conference on Electronics (CAE)*, pp. 71–76, 2026.

* **Links:** DOI [10.1109/cae69023.2026.11450324](https://doi.org/10.1109/cae69023.2026.11450324) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/11450324/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Power management <papers-topic-power-management>`, {ref}`Reliability and harsh environments <papers-topic-reliability>`
* **Institutions:** Universidad Técnica Federico Santa María; Universidad de Chile
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/cae69023.2026.11450324 resolved; title matches Crossref and OpenAlex

(paper-olyanasab-2025a)=
### An 8.1-µW 12-bit Non-Binary Self-Clocked SAR-ADC in 130 nm Open-Source PDK

Ali Olyanasab, Patrick Fath, Leonhard Schreiner, Christoph Guger and Harald Pretl. "An 8.1-µW 12-bit Non-Binary Self-Clocked SAR-ADC in 130 nm Open-Source PDK." *2025 Austrochip Workshop on Microelectronics (Austrochip)*, pp. 45–48, 2025.

* **Links:** DOI [10.1109/austrochip67945.2025.11183685](https://doi.org/10.1109/austrochip67945.2025.11183685) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/11183685/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Data converters and mixed-signal circuits <papers-topic-mixed-signal>`
* **Institutions:** g.tec Medical Engineering GmbH; Johannes Kepler University Linz
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/austrochip67945.2025.11183685 resolved; title matches Crossref and OpenAlex

(paper-poole-2023a)=
### A 130-nm Fusion-Based Deconvolution Kernel Generator IC for Real-Time mmWave Radar Motion Compensation

Nikhil Poole and Amin Arbabian. "A 130-nm Fusion-Based Deconvolution Kernel Generator IC for Real-Time mmWave Radar Motion Compensation." *IEEE Access*, vol. 11, pp. 132223–132238, 2023.

* **Links:** DOI [10.1109/access.2023.3336408](https://doi.org/10.1109/access.2023.3336408) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10328566/)
* **Free copies:** [ieeexplore.ieee.org](https://ieeexplore.ieee.org/ielx7/6287639/6514899/10328566.pdf) (gold (publisher version))
* **Access:** free to read
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Digital circuits <papers-topic-digital>`, {ref}`Data converters and mixed-signal circuits <papers-topic-mixed-signal>`, {ref}`Sensors <papers-topic-sensors>`
* **Institutions:** Stanford University
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/access.2023.3336408 resolved; title matches Crossref and OpenAlex

(paper-price-2025a)=
### Towards A Modular Digital Sensor Interface for Resilient Sensor Measurements

Ryan M. Price, Gabriel Saucedo, Emilio Jackson, Zander Lin Cox, John Perez and Robert C. Roberts. "Towards A Modular Digital Sensor Interface for Resilient Sensor Measurements." *2025 IEEE SENSORS*, pp. 1–4, 2025.

* **Links:** DOI [10.1109/sensors59705.2025.11330220](https://doi.org/10.1109/sensors59705.2025.11330220) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/11330220/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Sensors <papers-topic-sensors>`, {ref}`Digital circuits <papers-topic-digital>`
* **Institutions:** University of Texas at El Paso; Texas A&M University; Pantex Plant
* **Fabrication (quoted from the abstract):** "resulted in a valid ChipIgnite design which was selected for fabrication on shuttle CI 2309"
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/sensors59705.2025.11330220 resolved; title matches Crossref and OpenAlex

(paper-rodriguez-ferrandez-2023a)=
### Space Shuttle: A Test Vehicle for the Reliability of the SkyWater 130nm PDK for Future Space Processors

Ivan Rodriguez-Ferrandez, Leonidas Kosmidis, Maris Tali and David Steenari. "Space Shuttle: A Test Vehicle for the Reliability of the SkyWater 130nm PDK for Future Space Processors." *2023 IEEE 29th International Symposium on On-Line Testing and Robust System Design (IOLTS)*, pp. 1–3, 2023.

* **Links:** DOI [10.1109/iolts59296.2023.10224899](https://doi.org/10.1109/iolts59296.2023.10224899) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10224899/)
* **Free copies:** [upcommons.upc.edu](https://upcommons.upc.edu/bitstreams/0df9d4ec-b398-4934-b55e-79709208e1df/download) (preprint)
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Radiation effects <papers-topic-radiation>`, {ref}`Reliability and harsh environments <papers-topic-reliability>`, {ref}`Test structures and test vehicles <papers-topic-test-structures>`
* **Institutions:** Universitat Politècnica de Catalunya; Barcelona Supercomputing Center; European Space Agency
* **Fabrication (quoted from the abstract):** "the design and tape-out of Space Shuttle, the first test chip for the evaluation of the suitability of the SkyWater 130nm PDK and the OpenLane EDA toolchain using the Google/E-fabless shuttle run"
* **Note:** No radiation results in the abstract; the paper describes the design and tape-out of the test vehicle.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/iolts59296.2023.10224899 resolved; title matches Crossref and OpenAlex

(paper-sajoto-1999a)=
### Inspection optimization for excursion and baseline defect monitoring in a manufacturing environment

D. Sajoto, A. Gordon and A. McCauley. "Inspection optimization for excursion and baseline defect monitoring in a manufacturing environment." *1999 IEEE International Symposium on Semiconductor Manufacturing Conference Proceedings (Cat No.99CH36314)*, pp. 371–374, 1999.

* **Links:** DOI [10.1109/issm.1999.808813](https://doi.org/10.1109/issm.1999.808813) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/808813/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. Fab publication: authors affiliated with Cypress Semiconductor, Bloomington, MN. The abstract does not name a process.
* **Topics:** {ref}`Cypress S8 lineage <papers-topic-lineage-s8>`, {ref}`Fab manufacturing <papers-fab-publications>`
* **Institutions:** Cypress Semiconductor (Bloomington, Minnesota)
* **Related pages:**
  * {ref}`machine-defect-inspection` — The paper optimises in-line defect inspection against end-of-line bit failures.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/issm.1999.808813 resolved; title matches Crossref and OpenAlex

(paper-shah-2023a)=
### FABulous Demo: Open Source FPGA on Sky130

Myrtle Shah, Jakob Ternes and Dirk Koch. "FABulous Demo: Open Source FPGA on Sky130." *2023 33rd International Conference on Field-Programmable Logic and Applications (FPL)*, pp. 365–365, 2023.

* **Links:** DOI [10.1109/fpl60245.2023.00070](https://doi.org/10.1109/fpl60245.2023.00070) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10296224/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Digital circuits <papers-topic-digital>`, {ref}`Open-source tooling <papers-topic-tooling>`
* **Institutions:** Heidelberg University
* **Fabrication (quoted from the abstract):** "our first silicon taped out on a fully open PDK, Skywater 130nm with shuttle runs sponsored by Google"
* **Note:** Borderline inclusion. A demonstration paper; the abstract reports fabric functionality working on first silicon.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/fpl60245.2023.00070 resolved; title matches Crossref and OpenAlex

(paper-singhani-2023a)=
### Open-Source, End-to-End Auditable Tapeout of Hardware Cryptography Module

Anish Singhani. "Open-Source, End-to-End Auditable Tapeout of Hardware Cryptography Module." *2023 IEEE International Symposium on Circuits and Systems (ISCAS)*, pp. 1–5, 2023.

* **Links:** DOI [10.1109/iscas46773.2023.10181702](https://doi.org/10.1109/iscas46773.2023.10181702) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10181702/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Hardware security <papers-topic-security>`, {ref}`Digital circuits <papers-topic-digital>`
* **Institutions:** Carnegie Mellon University
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/iscas46773.2023.10181702 resolved; title matches Crossref and OpenAlex

(paper-smith-2005a)=
### Simple implementation of a first order advanced process control engine for thin film applications

E. Smith and A. Raviswaran. "Simple implementation of a first order advanced process control engine for thin film applications." *ISSM 2005, IEEE International Symposium on Semiconductor Manufacturing, 2005.*, pp. 162–165, 2005.

* **Links:** DOI [10.1109/issm.2005.1513324](https://doi.org/10.1109/issm.2005.1513324) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/1513324/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. Fab publication: authors affiliated with Cypress Semiconductor Minnesota, Bloomington, MN. The abstract does not name a process.
* **Topics:** {ref}`Cypress S8 lineage <papers-topic-lineage-s8>`, {ref}`Fab manufacturing <papers-fab-publications>`
* **Institutions:** Cypress Semiconductor (Bloomington, Minnesota)
* **Related pages:**
  * {ref}`machine-pecvd` — The paper describes run-to-run control of PECVD dielectric deposition.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/issm.2005.1513324 resolved; title matches Crossref and OpenAlex

(paper-smith-2006a)=
### Using a ‘Z’ Tool Controller for APC Applications

Eugene Smith and Russell Elias. "Using a ‘Z’ Tool Controller for APC Applications." *2006 IEEE International Symposium on Semiconductor Manufacturing*, pp. 118–121, 2006.

* **Links:** DOI [10.1109/issm.2006.4493038](https://doi.org/10.1109/issm.2006.4493038) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/4493038/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. Fab publication: authors affiliated with Cypress Semiconductor, 2401 East 86th Street, Bloomington, MN. The abstract mentions CMP control at the 130 nm node without naming a process.
* **Topics:** {ref}`Cypress S8 lineage <papers-topic-lineage-s8>`, {ref}`Fab manufacturing <papers-fab-publications>`
* **Institutions:** Cypress Semiconductor (Bloomington, Minnesota)
* **Related pages:**
  * {ref}`machine-cmp-polisher` — The abstract cites CMP at the 130 nm node as an established advanced-process-control application.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/issm.2006.4493038 resolved; title matches Crossref and OpenAlex

(paper-srimani-2020a)=
### Heterogeneous Integration of BEOL Logic and Memory in a Commercial Foundry: Multi-Tier Complementary Carbon Nanotube Logic and Resistive RAM at a 130 nm node

T. Srimani, G. Hills, M. Bishop, C. Lau, P. Kanhaiya, R. Ho, A. Amer, M. Chao, A. Yu, A. Wright, A. Ratkovich, D. Aguilar, A. Bramer, C. Cecman, A. Chov, G. Clark, G. Michaelson, M. Johnson, K. Kelley, P. Manos, K. Mi, U. Suriono, S. Vuntangboon, H. Xue, J. Humes, S. Soares, B. Jones, S. Burack, Arvind, A. Chandrakasan, B. Ferguson, M. Nelson and M. M. Shulaker. "Heterogeneous Integration of BEOL Logic and Memory in a Commercial Foundry: Multi-Tier Complementary Carbon Nanotube Logic and Resistive RAM at a 130 nm node." *2020 IEEE Symposium on VLSI Technology*, pp. 1–2, 2020.

* **Links:** DOI [10.1109/vlsitechnology18217.2020.9265083](https://doi.org/10.1109/vlsitechnology18217.2020.9265083) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/9265083/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. The abstract says "a commercial foundry" at a 130 nm node; the basis is the SkyWater Technology co-author affiliations (inventory SRIMANI-2020). The foundry is not named in the abstract.
* **Topics:** {ref}`BEOL-integrated devices <papers-topic-beol-integration>`, {ref}`RRAM (ReRAM) <papers-topic-rram>`
* **Institutions:** Massachusetts Institute of Technology; SkyWater Technology; NanoIntegris; Intrinsix
* **Related pages:**
  * {ref}`overview-sky130b-reram` — The page's ReRAM section cites this BEOL RRAM integration work.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/vlsitechnology18217.2020.9265083 resolved; title matches Crossref and OpenAlex

(paper-srimani-2023a)=
### Foundry Monolithic 3D BEOL Transistor + Memory Stack: Iso-performance and Iso-footprint BEOL Carbon Nanotube FET+RRAM vs. FEOL Silicon FET+RRAM

T. Srimani, A. C. Yu, R. M. Radway, D. T. Rich, M. Nelson, S. Wong, D. Murphy, S. Fuller, G. Hills, S. Mitra and M. M. Shulaker. "Foundry Monolithic 3D BEOL Transistor + Memory Stack: Iso-performance and Iso-footprint BEOL Carbon Nanotube FET+RRAM vs. FEOL Silicon FET+RRAM." *2023 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits)*, pp. 1–2, 2023.

* **Links:** DOI [10.23919/vlsitechnologyandcir57934.2023.10185414](https://doi.org/10.23919/vlsitechnologyandcir57934.2023.10185414) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10185414/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`BEOL-integrated devices <papers-topic-beol-integration>`, {ref}`RRAM (ReRAM) <papers-topic-rram>`
* **Institutions:** Stanford University; Massachusetts Institute of Technology; SkyWater Technology; Analog Devices; Harvard University
* **Fabrication (quoted from the abstract):** "This process is established within SkyWater Technology Foundry (90/130nm technology node on 200mm Si wafers)"
* **Related pages:**
  * {ref}`overview-sky130b-reram` — The overview page describes the BEOL ReRAM tier; this work stacks RRAM in the BEOL at SkyWater.
* **Verified:** 2026-09-14 Crossref REST API works/10.23919/vlsitechnologyandcir57934.2023.10185414 resolved; title matches Crossref and OpenAlex

(paper-tarabata-2025a)=
### Silicon-Proven Synchronous and Asynchronous Frequency-to-Digital Converters Using Open-Source EDA Tools

Byron Tarabata, Eduardo Holguín, Martín Gavilánez, Esteban Astudillo, Ana Salcedo and Luis Miguel Prócel. "Silicon-Proven Synchronous and Asynchronous Frequency-to-Digital Converters Using Open-Source EDA Tools." *2025 38th SBC/SBMicro/IEEE Symposium on Integrated Circuits and Systems Design (SBCCI)*, pp. 1–6, 2025.

* **Links:** DOI [10.1109/sbcci66862.2025.11218693](https://doi.org/10.1109/sbcci66862.2025.11218693) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/11218693/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Digital circuits <papers-topic-digital>`, {ref}`Shuttle programmes and education <papers-topic-education-shuttles>`
* **Institutions:** Escuela Politécnica Nacional; Universidad San Francisco de Quito
* **Fabrication (quoted from the abstract):** "fabricated via the Tiny Tapeout multi-project wafer (MPW) service using the SKY130 PDK"
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/sbcci66862.2025.11218693 resolved; title matches Crossref and OpenAlex

(paper-upton-2023a)=
### Testbench on a Chip: A Yield Test Vehicle for Resistive Memory Devices

Luke R. Upton, Guénolé Lallement, Michael D. Scott, Joyce Taylor, Robert M. Radway, Dennis Rich, Mark Nelson, Subhasish Mitra and Boris Murmann. "Testbench on a Chip: A Yield Test Vehicle for Resistive Memory Devices." *2023 24th International Symposium on Quality Electronic Design (ISQED)*, pp. 1–7, 2023.

* **Links:** DOI [10.1109/isqed57927.2023.10129298](https://doi.org/10.1109/isqed57927.2023.10129298) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10129298/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`RRAM (ReRAM) <papers-topic-rram>`, {ref}`Test structures and test vehicles <papers-topic-test-structures>`
* **Institutions:** Stanford University; Intrinsix; SkyWater Technology
* **Related pages:**
  * {ref}`overview-sky130b-reram` — The yield test vehicle characterises RRAM in SkyWater's 130 nm technology; the overview page describes the sky130B ReRAM module.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/isqed57927.2023.10129298 resolved; title matches Crossref and OpenAlex

(paper-wang-2006a)=
### Precise Ion Milling and 3D TEM technique to Deal with Feature Blocking in TEM Viewing Semiconductor Devices

N Wang, W Gruenewald and S Miller. "Precise Ion Milling and 3D TEM technique to Deal with Feature Blocking in TEM Viewing Semiconductor Devices." *Microscopy and Microanalysis*, vol. 12, no. S02, pp. 1240–1241, 2006.

* **Links:** DOI [10.1017/s1431927606063112](https://doi.org/10.1017/s1431927606063112) · [publisher or proceedings page](https://academic.oup.com/mam/article/12/S02/1240/6916148)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** affiliation inference — the process or fab is not named; the link rests on author affiliations. Borderline inclusion. Fab publication: extended abstract; one author affiliation is Cypress Semiconductor, 2401 E. 86th St, Bloomington. No process is named. OpenAlex records the paper as bronze open access, but its Cambridge PDF URL returned HTTP 404 on 2026-09-14 and no free copy was confirmed.
* **Topics:** {ref}`Cypress S8 lineage <papers-topic-lineage-s8>`, {ref}`Fab manufacturing <papers-fab-publications>`
* **Institutions:** BAL-TEC Innovations; Cypress Semiconductor (Bloomington, Minnesota)
* **Related pages:**
  * {ref}`machine-cross-section-sem-profilers` — The paper concerns ion-milling and 3D TEM techniques for viewing semiconductor devices (title; abstract not available).
* **Verified:** 2026-09-14 Crossref REST API works/10.1017/s1431927606063112 resolved; title matches Crossref and OpenAlex

(paper-yang-2024a)=
### An Open-Source 12-bit 10-kS/s Incremental ADC in 130-nm CMOS

Raymond H. Yang and Yaqing Xia. "An Open-Source 12-bit 10-kS/s Incremental ADC in 130-nm CMOS." *IEEE Design & Test*, vol. 41, no. 6, pp. 28–35, 2024.

* **Links:** DOI [10.1109/mdat.2024.3444728](https://doi.org/10.1109/mdat.2024.3444728) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/10637433/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Data converters and mixed-signal circuits <papers-topic-mixed-signal>`
* **Institutions:** Apple; Cannan Inc.
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/mdat.2024.3444728 resolved; title matches Crossref and OpenAlex

(paper-zhang-2022a)=
### An Open-Source and Autonomous Temperature Sensor Generator Verified With 64 Instances in SkyWater 130 nm for Comprehensive Design Space Exploration

Qirui Zhang, Wenbo Duan, Tim Edwards, Tim Ansell, David Blaauw, Dennis Sylvester and Mehdi Saligane. "An Open-Source and Autonomous Temperature Sensor Generator Verified With 64 Instances in SkyWater 130 nm for Comprehensive Design Space Exploration." *IEEE Solid-State Circuits Letters*, vol. 5, pp. 174–177, 2022.

* **Links:** DOI [10.1109/lssc.2022.3188925](https://doi.org/10.1109/lssc.2022.3188925) · [publisher or proceedings page](https://ieeexplore.ieee.org/document/9816083/)
* **Free copies:** none located
* **Access:** paywalled
* **Basis:** process named — the abstract or full text names SKY130, the SkyWater 130 nm process or the SkyWater foundry.
* **Topics:** {ref}`Sensors <papers-topic-sensors>`, {ref}`Data converters and mixed-signal circuits <papers-topic-mixed-signal>`, {ref}`Open-source tooling <papers-topic-tooling>`
* **Institutions:** University of Michigan; Efabless; Google
* **Verified:** 2026-09-14 Crossref REST API works/10.1109/lssc.2022.3188925 resolved; title matches Crossref and OpenAlex
