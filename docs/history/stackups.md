(history-stackups)=
# Stackups before S8, as the reports print them

Cypress's qualification reports each carry a "Technology/Fab Process Description": the number of metal
layers, the films of each layer, the passivation, the design rule and the gate oxide. This page copies
those blocks for every report in the evidence file that prints them, so the processes can be compared
with each other and with S8. The page is generated from `data/history/qtp.yaml` by
`tools/gen_history_stackups.py`; edit the evidence, not this page.

## How to read the tables

* **As printed.** Every value is copied from one report, spelling and units included ("A" for Å,
  "Si2N4", "TeOs"). Where two reports on one process disagree, both appear.
* **Our arithmetic.** The "Layer total" column adds up the films of one metal layer. It is not printed in
  the reports.
* **What is missing.** The reports give no inter-metal dielectric thicknesses, no via or contact
  materials and no well or implant data, so the stack cannot be drawn to scale from them.
* **Reissues.** Some reports are reissues with the process block replaced by "Proprietary"; those are
  left out here. See {ref}`history-fabs` for how reissues rename sites.

## Summary by design rule

### 0.8 µm

| Code and report | Fab as printed | Metal layers | Gate oxide |
|---|---|---|---|
| P20, QTP 91216[^qtp-091216] | Cypress Semiconductor - Round Rock, TX (Fab2) | 2 | SiO2 / 195 Å |
| P20, QTP 93332[^qtp-093332] | Cypress Semiconductor - Round Rock, TX (Fab2) | 2 | SiO2 / 195 Å |

### 0.65 µm

| Code and report | Fab as printed | Metal layers | Gate oxide |
|---|---|---|---|
| L28, QTP 000901[^qtp-000901] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 145 Å |
| L28, QTP 004604[^qtp-004604] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 145 Å |
| L28, QTP 011503[^qtp-011503] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 145 A |
| L28, QTP 012204[^qtp-012204] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 145 Å |
| L28, QTP 031101[^qtp-031101] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 145 Å |
| L28, QTP 080608[^qtp-080608] | TSMC-2A, Taiwan | 2 | SiO2 / 125 Å |
| L28, QTP 98333[^qtp-098333] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 145 A |
| L28, QTP 99285[^qtp-099285] | TSMC-2A, Taiwan | 2 | SiO2 / 125 Å |
| L28, QTP 110605[^qtp-110605] | TSMC-2A, Taiwan | 2 | SiO2 / 125 Å |
| L28EPD, QTP 99034[^qtp-099034] | Cypress Semiconductor – Round Rock, Texas | 2 | SiO2 / 145 Å |
| P26, QTP 054605[^qtp-054605] | Magnachip/Cheong-Ju-Korea | 3 | SiO2, 165Å |
| P26, QTP 95075[^qtp-095075] | Cypress Semiconductor – Round Rock, Tx (Fab2) | 2 | SiO2, 165Å |
| P26, QTP 96411[^qtp-096411] | Cypress Semiconductor - Round Rock, TX (Fab2) | 2 | SiO2 / 165A |
| P26, QTP 99092[^qtp-099092] | Cypress Semiconductor - Round Rock, TX (Fab2) | 2 | SiO2 / 165 Å |
| R28, QTP 95515[^qtp-095515] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 165 Å |
| R28, QTP 96091[^qtp-096091] | Cypress Semiconductor, Bloomington, MN | 2 | SiO2 / 165 A |
| R28, QTP 96182[^qtp-096182] | Cypress Semiconductor, Bloomington, MN | 2 | SiO2 / 165 A |
| R28, QTP 96361[^qtp-096361] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 165 Å |
| R28, QTP 97476[^qtp-097476] | Cypress Semiconductor -- Round Rock, TX | 2 | SiO2 / 165 Å |
| R28, QTP 98236[^qtp-098236] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 165 Å |
| R28, QTP 98252[^qtp-098252] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 165 Å |
| R28, QTP 98296[^qtp-098296] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 165 Å |
| R28, QTP 98393[^qtp-098393] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 165 Å |
| R28, QTP 99083[^qtp-099083] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 165 Å |
| R28, QTP 99175[^qtp-099175] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 165 Å |

### 0.5 µm

| Code and report | Fab as printed | Metal layers | Gate oxide |
|---|---|---|---|
| 0.5um TLM, QTP 001004[^qtp-001004] | Hyundai / Cheong Ju, Korea | 3 | SiO2 / 95 A |
| L31, QTP 97461[^qtp-097461] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 145 Å |
| R3, QTP 97044[^qtp-097044] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 145 Å |
| R32, QTP 97132[^qtp-097132] | Cypress Semiconductor - Bloomington, MN | 1 | SiO2 / 145Å |
| R32, QTP 97195[^qtp-097195] | Cypress Semiconductor - Bloomington, MN | 1 | SiO2 / 145Å |
| R32D, QTP 97118[^qtp-097118] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 145Å |
| R32D, QTP 97201[^qtp-097201] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 145Å |
| R32D, QTP 97222[^qtp-097222] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 145Å |
| R32D, QTP 97344[^qtp-097344] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 145Å |
| R32D, QTP 98021[^qtp-098021] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 145Å |
| S4AD-5, QTP 021507[^qtp-021507] | Cypress Semiconductor -- CTI Round Rock, TX | 2 | SiO2 / 110Å |

### 0.42 µm and 0.35 µm

| Code and report | Fab as printed | Metal layers | Gate oxide |
|---|---|---|---|
| 0.35um TLM, QTP 002703[^qtp-002703] | Fab 25-Hyundai-Korea (HME) | 3 | N/A |
| CSM 0.35um, QTP I000005[^qtp-i000005] | Chartered Semiconductor Singapore | 3 | SiO2 / 65Å |
| R42, QTP 97506[^qtp-097506] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 70 Å |
| R42D, QTP 97211[^qtp-097211] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 70 Å |
| R42D, QTP 97396[^qtp-097396] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 70 Å |
| R42D, QTP 97517[^qtp-097517] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 70 Å |
| R42D, QTP 98081[^qtp-098081] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 70 Å |
| R42D, QTP 98357[^qtp-098357] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 70Å |
| R42H, QTP 98111[^qtp-098111] | Cypress Semiconductor - Bloomington, MN | 1 | SiO2 / 110Å |
| R42HD, QTP 98086[^qtp-098086] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 110Å |
| R42HD, QTP 98115[^qtp-098115] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 110Å |
| R42HD, QTP 98313[^qtp-098313] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 110Å |
| R42HD, QTP 98368[^qtp-098368] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 110Å |
| R42HD, QTP 98437[^qtp-098437] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 110Å |
| R42HD, QTP 102101[^qtp-102101] | Fab 4 / CMI - Bloomington, MN | 2 | SiO2 / 110Å |
| R42HDHA, QTP 001605[^qtp-001605] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 110Å |
| R42HDHA, QTP 99325[^qtp-099325] | Cypress Semiconductor - Bloomington, MN (fab 4) | 2 | SiO2 / 110Å |
| R42LDHA, QTP 003907[^qtp-003907] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 70Å |
| R42LHDHA, QTP 005004[^qtp-005004] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 110Å |
| RAM42HA, QTP 030204[^qtp-030204] | Cypress Semiconductor -- Bloomington, MN | 1 | SiO2 /70A |
| RAM42HHA, QTP 030206[^qtp-030206] | Cypress Semiconductor -- Bloomington, MN | 1 | SiO2 /110A |
| RAM42HNHA, QTP 091302[^qtp-091302] | Grace Semiconductor, Shanghai, China | 1 | SiO2 /110A |
| S4AD-5, QTP 010902[^qtp-010902] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 110Å |
| S4AD-5, QTP 020305[^qtp-020305] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 110 Å |
| S4AD-5, QTP 022505[^qtp-022505] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 110 Å |
| S4AD-5, QTP 032508[^qtp-032508] | Cypress Semiconductor – CTI Round Rock, TX | 2 | SiO2 / 110°A |
| S4AD-5, QTP 042505[^qtp-042505] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 110A |
| S4AD-5, QTP 060201[^qtp-060201] | Cypress Semiconductor -- Minnesota | 2 | SiO2 / 110A |
| S4AD-5, QTP 062509[^qtp-062509] | GSMC/Shanghai-China | 2 | SiO2 / 110A |
| S4AD-5, QTP 063003[^qtp-063003] | Cypress Semiconductor – Round Rock, TX | 2 | SiO2/ 110A |
| S4AD-5, QTP 070505[^qtp-070505] | GSMC China | 2 | SiO2 / 110A |
| S4AD-5, QTP 071104[^qtp-071104] | GSMC/China | 2 | SiO2 / 110A |
| S4AD-5, QTP 071502[^qtp-071502] | Cypress CTI-Texas | 2 | SiO2/ 11 |
| S4AD-5, QTP 072105[^qtp-072105] | GSMC/Shanghai-China | 2 | SiO2 / 110A |
| S4AD-5, QTP 151005[^qtp-151005] | HHGrace /Shanghai-China | 2 | SiO2 / 110A |
| S4AD-5CTI, QTP 030702[^qtp-030702] | Cypress Semiconductor - Round Rock, TX (CTI) | 2 | SiO2 / 110Å |
| S4AD-5CTI, QTP 040901[^qtp-040901] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 110A |
| S4AD-5CTI, QTP 042702[^qtp-042702] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 110A |
| S4AD-5CTI, QTP 051005[^qtp-051005] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 110A |
| S4AD-LATCH, QTP 050507[^qtp-050507] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 70Å |
| S4ADLatch, QTP 042806[^qtp-042806] | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 7A |
| WaferTech 0.35um, QTP G990003[^qtp-g990003] | WaferTech, WA, USA | 2 | 70A SiO2 |

### 0.27 µm and 0.25 µm

| Code and report | Fab as printed | Metal layers | Gate oxide |
|---|---|---|---|
| B53D-3, QTP 002202[^qtp-002202] | Cypress Semiconductor -- Bloomington, MN | 2 | SiO2 55Å |
| B53D-3, QTP 024907[^qtp-024907] | Cypress Minnesota, Fab4 | 2 | SiO2 / 55Å |
| B53D-3RF, QTP 032005[^qtp-032005] | Cypress Minnesota, Fab4 | 2 | SiO2 / 55Å |
| R52D-3, QTP 003906[^qtp-003906] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 55 Å |
| R52D-3, QTP 99202[^qtp-099202] | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 50 Å |
| R52D-3, QTP 99503[^qtp-099503] | Cypress Semiconductor -- Bloomington, MN | 2 | SiO2 / 50 Å |
| R52FD-3, QTP 000505[^qtp-000505] | Cypress Semiconductor -- Bloomington, MN | 2 | SiO2 / 55 Å |
| R52FFD-3, QTP 005105[^qtp-005105] | Cypress Semiconductor – Bloomington, MN | 2 | SiO2 55Å |
| R52FFD-3, QTP 012705[^qtp-012705] | Cypress Semiconductor – Bloomington, MN | 2 | SiO2 55Å |
| R52LD-3, QTP 002603[^qtp-002603] | Cypress Semiconductor -- Bloomington, MN | 2 | SiO2 / 70 Å |
| R52LD-3, QTP 062201[^qtp-062201] | Cypress Semiconductor – Bloomington Minnesota | 2 | 55Å |
| R52LD-5R, QTP 004405[^qtp-004405] | Cypress Semiconductor -- Bloomington, MN | 2 | 70Å (core) 110Å Regulator |
| R52T-3, QTP 025003[^qtp-025003] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 041603[^qtp-041603] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 041801[^qtp-041801] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 043502[^qtp-043502] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 050401[^qtp-050401] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 050502[^qtp-050502] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 051203[^qtp-051203] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 051804[^qtp-051804] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 053404[^qtp-053404] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 054203[^qtp-054203] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 054810[^qtp-054810] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 060703[^qtp-060703] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 063108[^qtp-063108] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 063109[^qtp-063109] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 063606[^qtp-063606] | Cypress Semiconductor - Bloomington, MN | 3 | SiO2, 55Å |
| R52T-3, QTP 082506[^qtp-082506] | Cypress Semiconductor - Bloomington, MN | 3 | SiO2, 55Å |
| R63D-25, QTP 011805[^qtp-011805] | Cypress Semiconductor -- Bloomington, MN | 2 | SiO2, 55 Å |
| R63D-25, QTP 012407[^qtp-012407] | Cypress Semiconductor -- Bloomington, MN | 2 | SiO2, 55 Å |
| WaferTech 0.25um, QTP 011103[^qtp-011103] | WaferTech, WA USA | 2 | SiO2 / 70Å |

### 0.21 µm to 0.15 µm

| Code and report | Fab as printed | Metal layers | Gate oxide |
|---|---|---|---|
| B55SGT, QTP 043001[^qtp-043001] | Cypress Semiconductor – Bloomington, MN (CMI) | 3 | SiO2, 45Å |
| B55SGT, QTP 051101[^qtp-051101] | Cypress Semiconductor – Bloomington, MN (CMI) | 3 | SiO2, 45Å |
| B55SGT, QTP 051102[^qtp-051102] | Cypress Semiconductor – Bloomington, MN (CMI) | 3 | SiO2, 45Å |
| PowerChip 0.165um, QTP 041005[^qtp-041005] | Power Chip (Foundry) - Taiwan | 2 | SiO2, 7.2nm |
| PowerChip 0.165um, QTP 051501[^qtp-051501] | Powerchip Semiconductor Corp, HsinChu, Taiwan | 2 | SiO2 / 72A |
| R7FD, QTP 011908[^qtp-011908] | Cypress Semiconductor -- Bloomington, MN | 2 | SiO2, 32Å |
| R7FFT-18, QTP 032105[^qtp-032105] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 32 Å |
| R7FT-3R, QTP 014807[^qtp-014807] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 32Å |
| R7FT-3R, QTP 024903[^qtp-024903] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 32Å |
| R7FTW-3R, QTP 023101[^qtp-023101] | Cypress Semiconductor -- Bloomington Minnesota | 3 | SiO2 32Å |
| R7LD-1.8, QTP 012801[^qtp-012801] | Cypress Semiconductor -- Bloomington, MN | 2 | SiO2, 32Å |
| R7LD-3, QTP 012005[^qtp-012005] | Cypress Semiconductor -- Bloomington, MN | 2 | SiO2, 32Å / 70Å |
| S17, QTP 032301[^qtp-032301] | Promos (Taiwan) | 2 | SiO2, 62Å |

### 0.13 µm

| Code and report | Fab as printed | Metal layers | Gate oxide |
|---|---|---|---|
| C8Q-3R, QTP 042105[^qtp-042105] | CMI/Fab4 | 4 | SiO2 DGOX 32/55A |
| C8Q-3R, QTP 042106[^qtp-042106] | CMI/Bloomington MN | 4 | SiO2 DGOX 32/55A |
| C8Q-3R, QTP 043004[^qtp-043004] | CMI/Bloomington MN | 4 | SiO2 DGOX 32/55A |
| C8Q-3R, QTP 044505[^qtp-044505] | CMI/Fab4 | 4 | SiO2 DGOX 32/55A |
| C8Q-3R, QTP 071005[^qtp-071005] | CMI/Bloomington MN | 4 | SiO2 DGOX 32/55Å |
| C8Q-3R, QTP 082609[^qtp-082609] | GSMC China | 4 | SiO2 /55A |
| L8C-3R, QTP 053301[^qtp-053301] | CMI / Bloomington MN | 4 | SiO2 DGOX 32/55A |
| RAM8NLD-1.8, QTP 024110[^qtp-024110] | Cypress Semiconductor -- Bloomington, MN | 2 | 26Å |
| S8, QTP 113005[^qtp-113005] | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2 /110A & SiO2/32A |

### 90 nm

| Code and report | Fab as printed | Metal layers | Gate oxide |
|---|---|---|---|
| C9FD-3R, QTP 063807[^qtp-063807] | Cypress Semiconductor -- Bloomington, MN | 2 | 23Å |
| R95LD-3R, QTP 061806[^qtp-061806] | Cypress Semiconductor -- Bloomington, MN | 2 | 28Å |
| R95LD-3R, QTP 071302[^qtp-071302] | Cypress Semiconductor -- Bloomington, MN | 2 | 28Å |
| R95LD-3R, QTP 072002[^qtp-072002] | Cypress Semiconductor -- Bloomington, MN | 2 | 28Å |
| R95LD-3R, QTP 091206[^qtp-091206] | HHGrace Fab 3, Shanghai, China | 2 | SiO2 /28A |
| R9Q-3R, QTP 044201[^qtp-044201] | Cypress Semiconductor - Bloomington, MN | 4 | Nitridized SiO2, Thin GOX 20A, Thick GOX, 58A |
| R9Q-3R, QTP 051207[^qtp-051207] | Cypress Semiconductor - Bloomington, MN | 4 | Nitridized SiO2, 22Å |
| R9Q-3R, QTP 051901[^qtp-051901] | Cypress Semiconductor -- Bloomington, MN | 4 | — |
| R9Q-3R, QTP 060908[^qtp-060908] | Cypress Semiconductor – Bloomington, MN | 4 | Nitridized SiO2, Thin GOX 20A, Thick GOX, 58A |
| R9T-3R, QTP 032003[^qtp-032003] | Cypress Semiconductor -- Bloomington, MN | 3 | Nitridized SiO2, Thin GOX 22A, Thick GOx |
| R9T-3R, QTP 053103[^qtp-053103] | Cypress Semiconductor - Bloomington, MN | 3 or 4 | Nitridized SiO2, 23Å |

## Film by film

Each table gives one report's metal layers and passivation, with its design rule and the earliest dated row of its qualification history.

### QTP 91216: Fab2/P20

*MAX EPLD, P20 Technology, Fab 2.* Design rule: CMOS, Double Metal /0.8 µm. Earliest dated history row: the history table gives no dates.[^qtp-091216]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å Ti/ 1200Å TiW/6000Å Al/500Å Ti | 0.820 µm |
| Metal 2 | 1minRF/1500Å Ti/9000Å Al | 1.050 µm |
| Passivation | Oxide/Oxynitride | — |

### QTP 93332: Fab2/P20

*MAX EPLD, P20 Technology, Fab 2.* Design rule: CMOS, Double Metal /0.8 µm. Earliest dated history row: the history table gives no dates.[^qtp-093332]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500 Ti/ 1200TiW6K Al/500Ti | 0.600 µm |
| Metal 2 | 1minRF/1500Ti/9KAl | 0.900 µm |
| Passivation | Oxide | — |

### QTP 000901: Fab2/L28

*Three-PLL Programmable Clock Generator, Fab 2 – L28 Technology.* Design rule: CMOS, Single Poly, Double Metal /0.65 µm. Earliest dated history row: Feb 96 (QTP 95197).[^qtp-000901]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å Ti/1,200Å TiW/6,000Å Al/1,200Å TiW | 0.890 µm |
| Metal 2 | 1,500Å TiW/10,000Å Al/150Å Ti | 1.165 µm |
| Passivation | 3,000Å TEOS + 15,000Å Si2N4 | — |

### QTP 004604: Fab2/L28

*High Accuracy EPROM Programmable Crystal Oscillator, L28 Technology, Fab 2.* Design rule: CMOS, Single Poly, Double Metal /0.65 µm. Earliest dated history row: Apr 98 (QTP 97403).[^qtp-004604]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å Ti/1,200Å TiW/6,000Å Al/1,200Å TiW | 0.890 µm |
| Metal 2 | 1,500Å TiW/10,000Å Al/150Å Ti | 1.165 µm |
| Passivation | 3,000Å TEOS + 15,000Å Si2N4 | — |

### QTP 011503: Fab2/L28

*Spread Spectrum Timing Solution for Serverworks Chipset, L28 Technology, Fab 2.* Design rule: CMOS, Single Poly, Double Metal /0.65 µm. Earliest dated history row: Apr 98 (QTP 97403).[^qtp-011503]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/1,200A TiW/6,000A Al/1,200A TiW | 0.890 µm |
| Metal 2 | 1,500A TiW/10,000A Al/150A Ti | 1.165 µm |
| Passivation | 3,000A TEOS + 15,000A Si2N4 | — |

### QTP 012204: Fab2/L28

*High Accuracy EPROM Programmable Crystal Oscillator, L28 Technology, Fab 2.* Design rule: CMOS, Single Poly, Double Metal /0.65 µm. Earliest dated history row: Apr 98 (QTP 97403).[^qtp-012204]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å Ti/1,200Å TiW/6,000Å Al/1,200Å TiW | 0.890 µm |
| Metal 2 | 1,500Å TiW/10,000Å Al/150Å Ti | 1.165 µm |
| Passivation | 3,000Å TEOS + 15,000Å Si2N4 | — |

### QTP 031101: Fab2/L28

*High-Accuracy EPROM Programmable Device Family, L28 Technology, Fab 2.* Design rule: CMOS, Single Poly, Double Metal /0.65 µm. Earliest dated history row: Apr 98 (QTP 97403).[^qtp-031101]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å Ti/1,200Å TiW/6,000Å Al/1,200Å TiW | 0.890 µm |
| Metal 2 | 1,500Å TiW/10,000Å Al/150Å Ti | 1.165 µm |
| Passivation | 3,000Å TEOS + 15,000Å Si2N4 | — |

### QTP 054605: Fab2/P26

*P26 TLM Technology Transfer to Magnachip.* Design rule: CMOS, Double Metal/0.65µm. Earliest dated history row: Mar 06 (QTP 054605).[^qtp-054605]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 1500Å TiW / 4000Å Al / 750Å TiW | 0.625 µm |
| Metal 2 | 1500Å TiW / 4000Å Al / 750Å TiW | 0.625 µm |
| Metal 3 | 1500Å TiW / 8000Å Al / 750Å TiW | 1.025 µm |
| Passivation | Oxynitride | — |

### QTP 080608: TSMC-2A/L28 TSMC

*High Accuracy EPROM Programmable Device Family, L28 Technology, TSMC-2A.* Design rule: CMOS, Single Poly, Double Metal/0.65um. Earliest dated history row: May 2003 (QTP 99285).[^qtp-080608]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 400Å Ti / 1,000Å TiN/ 4,700Å AlSiCu/ 375Å TiN | 0.648 µm |
| Metal 2 | 1,500 Å Ti / 8,000Å AlSiCu / 375Å TiN | 0.988 µm |
| Passivation | 3,000Å SiN / 3,150Å SOG, 1,200Å SiN | — |

### QTP 95075: Fab2/P26

*CY27H010 128 x 8 High Speed CMOS EPROM, P26 Technology, Fab2.* Design rule: CMOS. Double Metal/0.65µm. Earliest dated history row: Aug 96 (QTP 95075).[^qtp-095075]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 6000Å Al / 1200Å TiW | 0.720 µm |
| Metal 2 | 1500Å TiW / 9000Å Al / 320Å TiW | 1.082 µm |
| Passivation | Oxynitride | — |

### QTP 95515: Fab3/R28

*64K SRAM, RAM28 TECHNOLOGY.* Design rule: CMOS, Double Poly, Double Metal /0.65 µm. Earliest dated history row: the history table gives no dates.[^qtp-095515]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Ti/TiW/Al-Si/TiW, 500Å/1.2KÅ/6KÅ/1.2KÅ | 0.890 µm |
| Metal 2 | TiW/Al-Si/Ti, 1.2KÅ/10KÅ/150Å | 1.135 µm |
| Passivation | 7000A TEOS + 6000A Si2N4 | — |

### QTP 96091: Fab3/R28

*Dual Port SRAM - R28 Technology, 6% Shrink.* Design rule: CMOS, Double Poly, Double Metal /0.65 µm. Earliest dated history row: no history table.[^qtp-096091]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Ti/TiW/AL-Si/TiW, 500A/1200A/6000A/1200A | 0.890 µm |
| Metal 2 | TiW/Al-Si/Ti 1200A/10000A/150A | 1.135 µm |
| Passivation | 7000A TEOS + 6000A Oxynitride | — |

### QTP 96182: Fab3/R28

*Dual Port SRAM - R28 Technology.* Design rule: CMOS, Double Poly, Double Metal /0.65 µm. Earliest dated history row: no history table.[^qtp-096182]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Ti/TiW/AL-Si/TiW, 500A/1200A/6000A/1200A | 0.890 µm |
| Metal 2 | TiW/Al-Si/Ti 1200A/10000A/150A | 1.135 µm |
| Passivation | 7000A TEOS + 6000A Oxynitride | — |

### QTP 96361: Fab3/R28

*Double Sync (tm) FIFO.* Design rule: CMOS, Double Poly, Double Metal /0.65 µm. Earliest dated history row: June 1997 (QTP 96361).[^qtp-096361]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Ti/TiW/Al-Si/TiW, 500Å/1.2KÅ/6KÅ/1.2KÅ | 0.890 µm |
| Metal 2 | TiW/Al-Si/TiW, 1.2KÅ/10KÅ/150Å | 1.135 µm |
| Passivation | 7000A TEOS + 6000A Si2N4 | — |

### QTP 96411: Fab 2/ P26

*256K/512K PROM - P26 Technology.* Design rule: CMOS, Double Metal / 0.65µm. Earliest dated history row: no history table.[^qtp-096411]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 6K Al, 1200A TiW | 0.720 µm |
| Metal 2 | 1,500A TiW, 9K Al, 320A TiW | 1.082 µm |
| Passivation | Oxynitride | — |

### QTP 97476: Fab2/R28

*256K STATIC RAM "CY7C194/CY7195/CY7C199" R28 PROCESS, FAB 2 QUALIFICATION.* Design rule: CMOS, Double Poly, Double Metal /0.65 m (the µ is not printed in the report). Earliest dated history row: Nov. 1997 (QTP 97476).[^qtp-097476]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Ti/TiW/Al-Si/TiW, 500Å/1.2KÅ/6KÅ/1.2K Å | 0.890 µm |
| Metal 2 | TiW/Al-Si/TiW, 1.2KÅ/10KÅ/150Å | 1.135 µm |
| Passivation | 7000A TEOS + 6000A Si2N4 | — |

### QTP 98236: Fab2/R28

*256K x 1 Static RAM, R28 Process, Fab 2 Qualification.* Design rule: CMOS, Double Poly, Double Metal /0.65 µm. Earliest dated history row: the history table gives no dates.[^qtp-098236]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Ti/TiW/Al-Si/TiW, 500Å/1.2KÅ/6KÅ/1.2KÅ | 0.890 µm |
| Metal 2 | TiW/Al-Si/TiW, 1.2KÅ/10KÅ/150Å | 1.135 µm |
| Passivation | 7000A TEOS + 6000A Si2N4 | — |

### QTP 98252: Fab2/R28

*CY7C188 32K x 9 Static RAM – R28 Technology – Fab2.* Design rule: CMOS, Double Poly, Double Metal /0.65 µm. Earliest dated history row: the history table gives no dates.[^qtp-098252]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Ti/TiW/Al-Si/TiW, 500Å/1.2KÅ/6KÅ/1.2K Å | 0.890 µm |
| Metal 2 | TiW/Al-Si/TiW, 1.2KÅ/10KÅ/150Å | 1.135 µm |
| Passivation | 7000A TEOS + 6000A Si2N4 | — |

### QTP 98296: Fab2/R28

*64K Static RAM – R28 Technology – Fab 2.* Design rule: CMOS, Double Poly, Double Metal /0.65 µm. Earliest dated history row: the history table gives no dates.[^qtp-098296]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Ti/TiW/Al-Si/TiW, 500Å/1.2KÅ/6KÅ/1.2K Å | 0.890 µm |
| Metal 2 | TiW/Al-Si/TiW, 1.2KÅ/10KÅ/150Å | 1.135 µm |
| Passivation | 7000A TEOS + 6000A Si2N4 | — |

### QTP 98333: Fab2/L28

*100-MHz Spread Spectrum Clock Synthesizer/Driver, USB, Hublink and SDRAM Support (CY2287PVC), Fab2, L28 Technology.* Design rule: CMOS, Single Poly, Double Metal /0.65 µm. Earliest dated history row: no history table.[^qtp-098333]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/1,200A TiW/6,000A Al/1,200A TiW | 0.890 µm |
| Metal 2 | 1,500A TiW/10,000A Al/150A Ti | 1.165 µm |
| Passivation | 3,000A TEOS + 15,000A Si2N4 | — |

### QTP 98393: Fab2/R28

*Dual Port SRAM - R28 Technology - Fab 2.* Design rule: CMOS, Double Poly, Double Metal /0.65 µm. Earliest dated history row: no history table.[^qtp-098393]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Ti/TiW/Al-Si/TiW, 500Å/1.2KÅ/6KÅ/1.2K Å | 0.890 µm |
| Metal 2 | TiW/Al-Si/TiW, 1.2KÅ/10KÅ/150Å | 1.135 µm |
| Passivation | 7000A TEOS + 6000A Si2N4 | — |

### QTP 99034: Fab2/L28EPD

*5V, 8/10 Bit FCT-T, L28EPD Technology, Fab 2.* Design rule: CMOS, Single Poly, Double Metal /0.65 µm. Earliest dated history row: no history table.[^qtp-099034]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/1,200A TiW/6,000A Al/1,200A TiW | 0.890 µm |
| Metal 2 | 1,500A TiW/10,000A Al/150A Ti | 1.165 µm |
| Passivation | 3,000A TEOS + 15,000A Si2N4 | — |

### QTP 99083: Fab2/R28

*Low Voltage Synchronous FIFO – R28 Technology – Fab2.* Design rule: CMOS, Double Poly, Double Metal /0.65 µm. Earliest dated history row: the history table gives no dates.[^qtp-099083]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Ti/TiW/Al-Si/TiW, 500Å/1.2KÅ/6KÅ/1.2KÅ | 0.890 µm |
| Metal 2 | TiW/Al-Si/TiW, 1.2KÅ/10KÅ/150Å | 1.135 µm |
| Passivation | 7000A TEOS + 6000A Si2N4 | — |

### QTP 99092: Fab 2/ P26

*Universal Serial Bus Microcontroller - P26 Technology in Fab 2.* Design rule: CMOS, Double Poly, Double Metal / 0.65µm. Earliest dated history row: the history table gives no dates.[^qtp-099092]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 6000Å Al, 1200 Å TiW | 0.720 µm |
| Metal 2 | 1500Å TiW, 9000Å Al, 320Å TiW | 1.082 µm |
| Passivation | Oxynitride | — |

### QTP 99175: Fab2/R28

*Military Clocked FIFOs – R28 Technology – Fab2.* Design rule: CMOS, Double Poly, Double Metal /0.65 µm. Earliest dated history row: the history table gives no dates.[^qtp-099175]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Ti/TiW/Al-Si/TiW, 500Å/1.2KÅ/6KÅ/1.2KÅ | 0.890 µm |
| Metal 2 | TiW/Al-Si/TiW, 1.2KÅ/10KÅ/150Å | 1.135 µm |
| Passivation | 7000A TEOS + 6000A Si2N4 | — |

### QTP 99285: TSMC-2A /L28-TSMC

*L28-TSMC Technology in TSMC-2A, Taiwan.* Design rule: CMOS, Single Poly, Double Metal /0.65 µm. Earliest dated history row: May 2003 (QTP 99285).[^qtp-099285]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Ti 400Å/TiN 1,000Å/AlSiCu 4,700Å/TiN 375Å | 0.648 µm |
| Metal 2 | Ti 1,500Å/AlSiCu 8,000Å/TiN 375Å | 0.988 µm |
| Passivation | SiN 3,000Å/SOG 3,150Å/SiN 12,000Å | — |

### QTP 110605: TSMC-2A/L28 TSMC

*Zero Delay Buffer, L28 Technology, TSMC-2A.* Design rule: CMOS, Single Poly, Double Metal/0.65um. Earliest dated history row: May 2003 (QTP 99285).[^qtp-110605]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 400Å Ti / 1,000Å TiN/ 4,700Å AlSiCu / 375Å TiN | 0.648 µm |
| Metal 2 | 1,500 Å Ti / 8,000Å AlSiCu / 375Å TiN | 0.988 µm |
| Passivation | 3,000Å SiN / 3,150Å SOG, 1,200Å SiN | — |

### QTP 001004: CF4 / HL50 (Hyundai)

*0.5um TLM Technology, Fab HME, Dual Port SRAM with PCI Bus Controller.* Design rule: CMOS / 0.5 micron. Earliest dated history row: Aug 00 (QTP 001004).[^qtp-001004]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | (Ti/TiN)/Ti/Al-1%Si-0.5%Cu/Ti/TiN | — |
| Metal 2 | (Ti/TiN)/Ti/Al-1%Si-0.5%Cu/Ti/TiN | — |
| Metal 3 | (Ti/TiN)/Ti/Al-1%Si-0.5%Cu/TiN | — |
| Passivation | Silicon Nitride | — |

### QTP 021507: Fab2, S4AD-5 (SONOS), R42D-5 derivative w/ 6 additional mask

*Failsafe Device Family & Options S4AD-5 SONOS Technology, Fab 2.* Design rule: CMOS, Single Poly, Double Metal, 0.5 m (the µ is not printed in the report). Earliest dated history row: April 01 (QTP 010702).[^qtp-021507]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å Ti/6,000Å Al 0.5% Cu /1,200Å TiW | 0.770 µm |
| Metal 2 | 500Å Ti/8,000Å Al 0.5% Cu/300Å TiW | 0.880 µm |
| Passivation | 3,000Å TeOs / 6,000Å Si3N4 | — |

### QTP 97044: Fab4/R3

*32K x 16 SRAM, R3 Technology, Fab 4 Qualification.* Design rule: CMOS, Single Poly, Double Metal /0.5 µm. Earliest dated history row: the history table gives no dates.[^qtp-097044]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW, 6,000Å Al/0.5%Cu 1,200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW, 9,000Å Al/0.5%Cu 1,200Å TiW | 1.070 µm |
| Passivation | 7,000A TEOS + 6,000A Si2N4 | — |

### QTP 97118: Fab4/R32D

*512K x 8 SRAM - R32D Technology - Fab4.* Design rule: CMOS, Single Local Interconnect, Double Metal /0.5 µm. Earliest dated history row: the history table gives no dates.[^qtp-097118]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Al-Cu/TiW | — |
| Metal 2 | TiW/Al-Cu/TiW | — |
| Passivation | Silicon Dioxide 7,000Å + Silicon Nitride 6,000Å | — |

### QTP 97132: Fab4/R32

*32K x 8 Low Power SRAM, R32 Technology, Fab4.* Design rule: CMOS, Double Poly, Single Metal /0.5 µm. Earliest dated history row: Jun 03 (QTP 97132).[^qtp-097132]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | TiW/Al, 500Å/8,000Å | 0.850 µm |
| Passivation | Silicon Dioxide 7,000Å + Silicon Nitride 6,000Å | — |

### QTP 97195: Fab4/R32

*128K x 8 SRAM - R32 Technology - Fab4 Qualification.* Design rule: CMOS, Single Local Interconnect, Single Metal /0.5 µm. Earliest dated history row: the history table gives no dates.[^qtp-097195]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | TiW/Al, 500Å/8,000Å | 0.850 µm |
| Passivation | Silicon Dioxide 7,000Å + Silicon Nitride 6,000Å | — |

### QTP 97201: Fab4/R32D

*1 Meg SRAM, R32D Technology, Fab 4 Qualification.* Design rule: CMOS, Single Local Interconnect, Double Metal /0.5 µm. Earliest dated history row: the history table gives no dates.[^qtp-097201]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Al-Cu/TiW | — |
| Metal 2 | TiW/Al-Cu/TiW | — |
| Passivation | Silicon Dioxide 7,000Å + Silicon Nitride 6,000Å | — |

### QTP 97222: Fab4/R32D

*Asynchronous FIFOs - R3.2D Technology.* Design rule: CMOS, Single Local Interconnect, Double Metal /0.5 µm. Earliest dated history row: the history table gives no dates.[^qtp-097222]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Al-Cu/TiW | — |
| Metal 2 | TiW/Al-Cu/TiW | — |
| Passivation | Silicon Dioxide 7,000Å + Silicon Nitride 6,000Å | — |

### QTP 97344: Fab4/R32D

*R32D Technology - Metal 2 Hot Aluminum.* Design rule: CMOS, Single Local Interconnect, Double Metal /0.5 µm. Earliest dated history row: the history table gives no dates.[^qtp-097344]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Al-Cu/TiW | — |
| Metal 2 | TiW/Al-Cu/TiW | — |
| Passivation | Silicon Dioxide 7,000Å + Silicon Nitride 6,000Å | — |

### QTP 97461: Fab4/L31

*3.3V, Light Device 16-Bit FCT Family.* Design rule: CMOS, Single Poly, Double Metal /0.5 µm. Earliest dated history row: the history table gives no dates.[^qtp-097461]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW, 6,000Å Al/0.5%Cu 1,200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW, 9,000Å Al/0.5%Cu 1,200Å TiW | 1.070 µm |
| Passivation | 7,000A TEOS + 6,000A Si2N4 | — |

### QTP 98021: Fab4/R32D

*1 Meg SRAM (5% Shrink), R32D Technology, Fab 4 -- Military Devices.* Design rule: CMOS, Single Local Interconnect, Double Metal /0.5 µm. Earliest dated history row: no history table.[^qtp-098021]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Al-Cu/TiW | — |
| Metal 2 | TiW/Al-Cu/TiW | — |
| Passivation | Silicon Dioxide 7,000Å + Silicon Nitride 6,000Å | — |

### QTP 001605: Fab4/R42HDHA

*256K Fast Asynchronous SRAM, R42HDHA Technology, Fab 4.* Design rule: CMOS, Double Metal /0.42 µm. Earliest dated history row: Apr 98 (QTP 98064).[^qtp-001605]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6000Å Al -5%Cu/1200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW/8000Å Al -5%Cu/300Å TiW | 0.880 µm |
| Passivation | 7000Å SiO2 + 6000Å Si3N4 | — |

### QTP 030204: Fab4/RAM42HA

*256K Static RAM Automotive Devices, RAM42HA Technology, Fab 4.* Design rule: CMOS, Single Metal / 0.42um. Earliest dated history row: Jun 03 (QTP 030206).[^qtp-030204]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | TiW, AlCu, TiW/500A , 6000A, 300A | 0.680 µm |
| Passivation | 3KA Oxide + 6000A Nitride (both with PECVD) | — |

### QTP 030206: Fab4/RAM42

*256K Static RAM Automotive Devices, RAM42HHA Technology, Fab 4.* Design rule: CMOS, Single Metal / 0.42UM. Earliest dated history row: Jun 03 (QTP 030206).[^qtp-030206]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Cu-Ti/8000A A1 | 0.850 µm |
| Passivation | 3KA Oxide + 6000A Nitride (both with PECVD) | — |

### QTP 091302: Fab4/RAM42

*MoBL Asynchronous SRAM Product Family, RAM42HNHA Technology, Fab5 GSMC.* Design rule: CMOS, Single Metal / 0.42µM. Earliest dated history row: Oct 09 (QTP 091302).[^qtp-091302]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500TiN/8000Al/250TiN | — |
| Passivation | 7000 TEOS + 6000Si3N4 | — |

### QTP 98086: Fab4/R4HD

*4 Meg SRAM, R42HD Technology, Hot Aluminum.* Design rule: CMOS, Double Metal /0.42 µm. Earliest dated history row: the history table gives no dates.[^qtp-098086]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6000Å Al -5%Cu/1200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW/8000Å Al -5%Cu/300Å TiW | 0.880 µm |
| Passivation | 7000Å SiO2 + 6000Å Si3N4 | — |

### QTP 98111: Fab4/R42HHA

*4 Meg SRAM, R42H Technology, Hot Aluminum.* Design rule: CMOS, Single Metal /0.42 µm. Earliest dated history row: the history table gives no dates.[^qtp-098111]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å Cu-Ti/8000Å Al | 0.850 µm |
| Passivation | 3K Å Oxide + 6,000 Å Nitride (both with PECVD) | — |

### QTP 98115: Fab4/R4HD

*1 Meg SRAM, R42HD Technology (5V operation).* Design rule: CMOS, Double Metal /0.42 µm. Earliest dated history row: the history table gives no dates.[^qtp-098115]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6000Å Al -5%Cu/1200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW/8000Å Al -5%Cu/300Å TiW | 0.880 µm |
| Passivation | 7000Å SiO2 + 6000Å Si3N4 | — |

### QTP 98313: Fab4/R4HD

*2 Meg SRAM, R42HD Technology (5V operation).* Design rule: CMOS, Double Metal /0.42 µm. Earliest dated history row: the history table gives no dates.[^qtp-098313]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6000Å Al -5%Cu/1200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW/8000Å Al -5%Cu/300Å TiW | 0.880 µm |
| Passivation | 7000Å SiO2 + 6000Å Si3N4 | — |

### QTP 98368: Fab4/R42HD

*SYNCHRONOUS/ASYNCHRONOUS DUAL PORT SRAM (3.3V AND 5V), R42HD TECHNOLOGY, FAB 4.* Design rule: CMOS, Double Metal /0.42 m (the µ is not printed in the report). Earliest dated history row: the history table gives no dates.[^qtp-098368]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6000Å Al -5%Cu/1200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW/8000Å Al -5%Cu/300Å TiW | 0.880 µm |
| Passivation | 7000Å SiO2 + 6000Å Si3N4 | — |

### QTP 98437: Fab4/R42HD

*1 Meg SRAM, R42HD Technology, Fab 4 Qualification.* Design rule: CMOS, Double Metal /0.42 µm. Earliest dated history row: the history table gives no dates.[^qtp-098437]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6000Å Al -5%Cu/1200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW/8000Å Al -5%Cu/300Å TiW | 0.880 µm |
| Passivation | 7000Å SiO2 + 6000Å Si3N4 | — |

### QTP 99325: Cypress Semiconductor-Bloomington, MN / R42HDHA

*5V Synchronous FIFOs, R42HDHA Technology, Fab 4.* Design rule: CMOS, Double Metal 0.42 µm. Earliest dated history row: the history table gives no dates.[^qtp-099325]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al -5%Cu - / 1200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW / 6000Å Al -5%Cu / 1200Å TiW | 0.770 µm |
| Passivation | 7000Å SiO2 + 6000Å Si3N4 | — |

### QTP 102101: R42HD

*Synchronous/Asynchronous Dual Port SRAM (3.3V and 5V), R42HD Technology, Fab 4 Qualification.* Design rule: CMOS, Double Metal /0.42 µm. Earliest dated history row: Nov 97 (QTP 98064).[^qtp-102101]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6000Å Al -5%Cu/1200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW/8000Å Al -5%Cu/300Å TiW | 0.880 µm |
| Passivation | 7000Å SiO2 + 6000Å Si3N4 | — |

### QTP 002703: Fab 25 / 0.35TLM

*Full Speed CYUSB Family, EZ-USB FX, 0.35um TLM Technology, Fab 25.* Design rule: CMOS, Triple Metal /0.35 µm. Earliest dated history row: Jun 00 (QTP 000602).[^qtp-002703]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Al-Si-Cu/Ti/TiN | — |
| Metal 2 | Al-Si-Cu/Ti/TiN/W-PLUG | — |
| Metal 3 | Al-Si-Cu/Ti/TiN/W-PLUG | — |
| Passivation | Double Layer, Nitride, Oxide | — |

### QTP 003907: Fab4/R42D (with Hot AL)

*High Frequency Programmable PECL Clock Generator R42LDHA Technology, Fab 4.* Design rule: CMOS, Double Metal /0.35 m (the µ is not printed in the report). Earliest dated history row: Sep 98 (QTP 98357).[^qtp-003907]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6000Å Al -5%Cu/1200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW/8000Å Al -5%Cu/300Å TiW | 0.880 µm |
| Passivation | 3,000Å SiO2 + 6000Å Si3N4 | — |

### QTP 005004: Fab 4/R42LHDHA

*HOTLink DX Family, R42LHDHA Technology, Fab 4.* Design rule: CMOS, Double Metal /0.35 m (the µ is not printed in the report). Earliest dated history row: Nov 99 (QTP 99041).[^qtp-005004]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW /600A AL5% | 0.110 µm (implausibly thin for a metal layer; the report may omit a film or misprint a unit) |
| Metal 2 | 500Å TiW/800 Å Al | 0.130 µm (implausibly thin for a metal layer; the report may omit a film or misprint a unit) |
| Passivation | 7,000 Å SiO2 + 6,000 Å Si2N4 | — |

### QTP 010902: Fab2, S4AD-5

*Programmable Clock Generator Family, S4AD-5 Technology, Fab 2.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Apr 01 (QTP 010702).[^qtp-010902]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å Ti/6,000Å Al 0.5% Cu /1,200Å TiW | 0.770 µm |
| Metal 2 | 500Å Ti/8,000Å Al 0.5% Cu/300Å TiW | 0.880 µm |
| Passivation | 3,000Å TeOs / 6,000Å Si3N4 | — |

### QTP 020305: Fab2, S4AD-5

*Two-PLL Clock Generator, S4AD-5 Technology, Fab 2 / R42LDHA, Fab 4.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Sep 98 (QTP 98357).[^qtp-020305]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å Ti/6,000Å Al 0.5% Cu/1,200Å TiW | 0.770 µm |
| Metal 2 | 500Å Ti/8,000Å Al 0.5% Cu/300Å TiW | 0.880 µm |
| Passivation | 3,000Å TeOs / 6,000Å Si3N4 | — |

### QTP 022505: Fab2, S4AD-5

*PSoC Microcontrollers Family, S4AD-5 Technology, Fab 2.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Apr 01 (QTP 010702).[^qtp-022505]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å Ti/6,000Å Al 0.5% Cu/1,200Å TiW | 0.770 µm |
| Metal 2 | 500Å Ti/8,000Å Al 0.5% Cu/300Å TiW | 0.880 µm |
| Passivation | 3,000Å TeOs / 6,000Å Si3N4 | — |

### QTP 030702: Fab2 SONOS, S4AD-5 CTI

*PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2 CTI.* Design rule: 1Poly/2Metal, 0.35 µm. Earliest dated history row: Apr 01 (QTP 010702).[^qtp-030702]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/6,000A Al 0.5% Cu /1,200A TiW | 0.770 µm |
| Metal 2 | 500A Ti/8,000A Al 0.5% Cu/300A TiW | 0.880 µm |
| Passivation | 3,000A TEOS / 6,000A Si3N4 | — |

### QTP 032508: Fab2, S4AD-5CTI SONOS

*PSoC Mixed Signal Array Product Family, S4AD-5 Technology, Fab 2.* Design rule: 1P2M/0.35um. Earliest dated history row: Apr 01 (QTP 010702).[^qtp-032508]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/6,000A Al 0.5% Cu /1,200A TiW | 0.770 µm |
| Metal 2 | 500A Ti/8,000A Al 0.5% Cu/300A TiW | 0.880 µm |
| Passivation | 3,000A TeOs / 6,000A Si3N4 | — |

### QTP 040901: Fab2, S4AD-5 CTI

*PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2.* Design rule: Single Poly, Double Metal, 0.35 m (the µ is not printed in the report). Earliest dated history row: Apr 01 (QTP 010702).[^qtp-040901]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/6000A Al 0.5% Cu /1200A TiW | 0.770 µm |
| Metal 2 | 500A Ti/8000A Al 0.5% Cu/300A TiW | 0.880 µm |
| Passivation | 3,000A TeOs / 6000A Si3N4 | — |

### QTP 042505: Fab2, S4AD-5 CTI, SONOS

*PSoC Mixed Signal Array (Neutron Product) Family, S4AD-5 Technology, Fab 2.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Apr 01 (QTP 010702).[^qtp-042505]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/6,000A Al 0.5% Cu /1,200A TiW | 0.770 µm |
| Metal 2 | 500A Ti/8,000A Al 0.5% Cu/300A TiW | 0.880 µm |
| Passivation | 3,000A TEOs / 6,000A Si3N4 | — |

### QTP 042702: Fab2, S4AD-5CTI SONOS

*Automotive PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2.* Design rule: Single Poly, Double Metal, 0.35 m (the µ is not printed in the report). Earliest dated history row: Nov 04 (QTP 042702).[^qtp-042702]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/6000A Al 0.5% Cu /1200A TiW | 0.770 µm |
| Metal 2 | 500A Ti/8000A Al 0.5% Cu/300A TiW | 0.880 µm |
| Passivation | 3,000A TeOs / 6000A Si3N4 | — |

### QTP 042806: Fab2, S4AD-5

*S4ADLATCH Technology, Fab 2.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Apr 01 (QTP 010702).[^qtp-042806]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/6,000A Al 0.5% Cu /1,200A TiW | 0.770 µm |
| Metal 2 | 500A Ti/8,000A Al 0.5% Cu/300A TiW | 0.880 µm |
| Passivation | 3,000A TeOs / 6,000A Si3N4 | — |

### QTP 050507: Fab2, S4AD-LATCH Sonos

*Programmable Clock Generator w/ VCXO Device Family, S4AD-LATCH, Fab 2.* Design rule: 1P2m, 0.35 µm (the µ is not printed in the report). Earliest dated history row: Apr 01 (QTP 010702).[^qtp-050507]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/6,000A Al 0.5% Cu /1,200A TiW | 0.770 µm |
| Metal 2 | 500A Ti/8,000A Al 0.5% Cu/300A TiW | 0.880 µm |
| Passivation | — | — |

### QTP 051005: Fab2, S4AD-5CTI SONOS

*Automotive PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2.* Design rule: Single Poly, Double Metal, 0.35 um. Earliest dated history row: Nov 04 (QTP 042702).[^qtp-051005]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/6000A Al 0.5% Cu /1200A TiW | 0.770 µm |
| Metal 2 | 500A Ti/8000A Al 0.5% Cu/300A TiW | 0.880 µm |
| Passivation | 3,000A TeOs / 6000A Si3N4 | — |

### QTP 060201: Fab 4, S4AD-5, SONOS

*PSoC Mixed Signal Array Hydra Device Family S4AD-5 Technology, Fab4.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Aug 05 (QTP 052004).[^qtp-060201]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A TiW/6,000A Al 0.5% Cu /300A TiW | 0.680 µm |
| Metal 2 | 500A TiW/8,000A Al 0.5% Cu/300A TiW | 0.880 µm |
| Passivation | 7,000A TeOs / 6,000A Si3N4 | — |

### QTP 062509: S4AD-5 GSMC SONOS

*Neutron Device Family, S4AD-5 Technology, GSMC.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Aug 06 (QTP 060605).[^qtp-062509]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 250A TiN/5,800A Al/700A TiN | 0.675 µm |
| Metal 2 | 500A TiN/8,000A Al/250A TiN | 0.875 µm |
| Passivation | 7,000A TeOs /6,000A Si3N4 | — |

### QTP 063003: Fab2, S4AD-5

*Nitride Seal Mask (NSM) Qualification, S4AD-5 Technology, Fab 2.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Apr 01 (QTP 010702).[^qtp-063003]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/6,000A Al 0.5% Cu /1,200A TiW | 0.770 µm |
| Metal 2 | 500A Ti/8,000A A1 0.5% Cu/300A TiW | 0.880 µm |
| Passivation | 3000A TeOs / 6,000A Si3N4 | — |

### QTP 070505: S4AD-5 GSMC Sonos

*PSoC Quark Device Family, S4AD-5 Technology, Fab 5.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Aug 06 (QTP 060605).[^qtp-070505]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 250A TiN/5,800A Al/700A TiN | 0.675 µm |
| Metal 2 | 500A TiN/8,000A Al/250A TiN | 0.875 µm |
| Passivation | 7,000A TeOs /6,000A Si3N4 | — |

### QTP 071104: S4AD-5 GSMC SONOS

*PSoC Mixed Signal Array Product Family, S4AD-5 Technology, Fab5.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Aug 06 (QTP 060605).[^qtp-071104]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 250A TiN/5,800A Al/700A TiN Metal 2: 500A TiN/8,000A Al/250A TiN | 1.550 µm |
| Passivation | 7,000A TeOs /6,000A Si3N4 | — |

The report gives 2 metal layers but lists films for 1.

### QTP 071502: Fab2, S4AD-5

*Ovation 1 Family, S4AD-5/C8QR-3R Technology, Fab2/4.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Aug 07 (QTP 071502).[^qtp-071502]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti / 6000A Al 0.5% Cu / 1200A TiW | 0.770 µm |
| Metal 2 | 500A T i/ 8000A A1 0.5% Cu / 300A TiW | 0.880 µm |
| Passivation | 7000A TEOS / 6000A Si3N4 | — |

### QTP 072105: S4AD-5

*EZ-Color Device Family, S4AD-5 Technology, GSMC.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Aug 06 (QTP 060605).[^qtp-072105]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 250A TiN/5,800A Al/700A TiN | 0.675 µm |
| Metal 2 | 500A TiN/8,000A Al/250A TiN | 0.875 µm |
| Passivation | 7,000A TeOs /6,000A Si3N4 | — |

### QTP 97211: Fab4/R42D

*1 Meg SRAM, R42D Technology, Fab 4 Qualification.* Design rule: CMOS, Single Poly, Double Metal /0.35µm. Earliest dated history row: the history table gives no dates.[^qtp-097211]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | TiW,AlCu,TiW/500Å,6000Å,300Å | 0.680 µm |
| Metal 2 | TiW,AlCu,TiW/500Å,8000Å,300Å | 0.880 µm |
| Passivation | 7,000 Å TEOS + 6,000 Å SiN | — |

### QTP 97396: Fab4/R42D

*4 Meg SRAM, R42D Technology, Fab 4 Qualification.* Design rule: CMOS, Double Metal /0.35 µm. Earliest dated history row: the history table gives no dates.[^qtp-097396]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | TiW,AlCu,TiW/500Å,6000Å,1200Å | 0.770 µm |
| Metal 2 | TiW,AlCu,TiW/500Å,8000Å,300Å | 0.880 µm |
| Passivation | 3000Å SiO2 + 6000Å Si3N4 | — |

### QTP 97506: Fab4/R42

*1 Meg SRAM, R42 Technology, Fab 4 Qualification.* Design rule: CMOS , 0.35µm. Earliest dated history row: the history table gives no dates.[^qtp-097506]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | TiW,AlCu,TiW/500Å,6000Å,300Å | 0.680 µm |
| Passivation | 3K Å Oxide + 6,000 Å Nitride (both with PECVD) | — |

The report gives 2 metal layers but lists films for 1.

### QTP 97517: Fab4/R42D

*1/2 Meg SRAM, R42D Technology, Fab 4 Qualification.* Design rule: CMOS, Double Metal /0.35 µm. Earliest dated history row: the history table gives no dates.[^qtp-097517]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | TiW,AlCu,TiW/500Å,6000Å,1200Å | 0.770 µm |
| Metal 2 | TiW,AlCu,TiW/500Å,8000Å,300Å | 0.880 µm |
| Passivation | 3000Å SiO2 + 6000Å Si3N4 | — |

### QTP 98081: Fab4/R42D w/ Hot Al

*Synchronous 3.3V Cache RAM, R42D Technology w/ Hot Al, Fab 4 Qualification.* Design rule: CMOS, Double Metal /0.35 µm. Earliest dated history row: the history table gives no dates.[^qtp-098081]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | TiW,AlCu,TiW/500Å,6000Å,1200Å | 0.770 µm |
| Metal 2 | TiW,AlCu,TiW/500Å,8000Å,300Å | 0.880 µm |
| Passivation | 3000Å SiO2 + 6000Å Si3N4 | — |

### QTP 98357: Fab4/R42D (with Hot AL)

*4 Meg SRAM With NoBL Architecture, R42D Technology, Hot Aluminum.* Design rule: CMOS, Double Metal /0.35 µm. Earliest dated history row: the history table gives no dates.[^qtp-098357]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6000Å Al -5%Cu/1200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW/8000Å Al -5%Cu/300Å TiW | 0.880 µm |
| Passivation | 7000Å SiO2 + 6000Å Si3N4 | — |

### QTP 151005: S4AD-5

*PSoC RADON Device Family, S4AD-5 Technology, HHGrace FAB5.* Design rule: Single Poly, Double Metal, 0.35 µm (the report prints µ with a non-standard font glyph). Earliest dated history row: Aug 06 (QTP 060605).[^qtp-151005]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 250A TiN/5,800A Al/700A TiN | 0.675 µm |
| Metal 2 | 500A TiN/8,000A Al/250A TiN | 0.875 µm |
| Passivation | 7,000A TeOs /6,000A Si3N4 | — |

### QTP G990003: WaferTech 0.35um

*WaferTech 0.35um.* Design rule: CMOS, Double Metal, 0.35um. Earliest dated history row: Jan 98 (QTP G990003).[^qtp-g990003]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 4,000K Å Ti/1,000K Å TiN/4,000K Å AlCu/250K Å TiN | 925.000 µm |
| Metal 2 | 1,500K Å Ti/6,000K Å AlCu/250K Å TiN | 775.000 µm |
| Passivation | 2K PE-Oxide + 6.5K PE-Nitride | — |

### QTP I000005: 2L313-698-CBB/CRA

*0.35um Technology, CSM Fab 2.* Design rule: CMOS, Triple Metal /0.35 µm. Earliest dated history row: 2000 (QTP I000005).[^qtp-i000005]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100Å IMPTi/300Å TiN/.5KAlCu/350Å Tin ARC | 0.125 µm (implausibly thin for a metal layer; the report may omit a film or misprint a unit) |
| Metal 2 | 100Å IMPTi/300Å TiN/.5KAlCu/350Å Tin ARC | 0.125 µm (implausibly thin for a metal layer; the report may omit a film or misprint a unit) |
| Metal 3 | 300Å IMPTi /300Å TiN/.8K AlCu/350Å TiN ARC | 0.175 µm (implausibly thin for a metal layer; the report may omit a film or misprint a unit) |
| Passivation | 350Å TiN/2K PSG/7K Si3N4 | — |

### QTP 011805: Fab4/R63D-25

*Unidirectional Synchronous FIFO with Bus Matching, R63D-25 Technology, Fab4.* Design rule: CMOS, Double Metal /0.27 µm. Earliest dated history row: Apr 01 (QTP 011308).[^qtp-011805]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6,000Å AlCu/300Å TiW | 0.680 µm |
| Metal 2 | 500Å TiW/8,000Å AlCu/300Å TiW | 0.880 µm |
| Passivation | 1000Å PECVD oxide / 9000Å PECVD | — |

### QTP 012407: Fab4/R63D-25

*Synchronous SRAM Family, R63D-25 Technology, Fab4.* Design rule: CMOS, Double Metal /0.27 µm. Earliest dated history row: Apr 01 (QTP 011308).[^qtp-012407]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6,000Å AlCu/300Å TiW | 0.680 µm |
| Metal 2 | 500Å TiW/8,000Å AlCu/300Å TiW | 0.880 µm |
| Passivation | 1000Å PECVD oxide / 9000Å PECVD | — |

### QTP 000505: Fab4/R52FD-3

*1 Meg Fast Asynchronous SRAM, R52FD-3 Technology, Fab 4.* Design rule: CMOS, Double Metal /0.25 µm/0.3 FETS. Earliest dated history row: Jul 00 (QTP 001603).[^qtp-000505]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6,000Å Al-0.5%Cu/300Å TiW | 0.680 µm |
| Metal 2 | 300Å CoTi/8,000Å Al-0.5%Cu/300Å TiW | 0.860 µm |
| Passivation | Oxide - Nitride | — |

### QTP 002202: Fab4/B53D-3

*Robo Clock II High-Speed Multi-Phase PLL Clock, B53D-3 Technology, Fab 4.* Design rule: CMOS, Double Metal/0.25 m (the µ is not printed in the report). Earliest dated history row: Aug 00 (QTP 99256).[^qtp-002202]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A TiW+6,000A Al/0.5%Cu/300A TiW | 0.680 µm |
| Metal 2 | 300A TiW+8,000A Al/0.5%Cu/300A TiW | 0.860 µm |
| Passivation | 1,000A TEOS + 9,000A SiN | — |

### QTP 002603: Fab4/R52LD-3

*4 Meg FCP MoBL SRAM Family, R52LD-3 Technology, Fab 4.* Design rule: CMOS, Double Metal /0.25 µm/0.3 FETS. Earliest dated history row: Apr 99 (QTP 99075).[^qtp-002603]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6000Å Al-0.5%Cu/300Å TiW | 0.680 µm |
| Metal 2 | 300Å CoTi/8,000Å Al-0.5%Cu/300Å TiW | 0.860 µm |
| Passivation | 1000Å PECVD Oxide + 9000Å PECVD Si2N4 | — |

### QTP 003906: Fab4/R52D-3

*4 Meg MoBL2 SRAM, R52D-3 Technology, Fab 4.* Design rule: CMOS, Double Metal /0.25 µm. Earliest dated history row: Aug 99 (QTP 99311).[^qtp-003906]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6,000Å Al -0.5% Cu/300Å TiW | 0.680 µm |
| Metal 2 | 300Å CoTi/8,000A Al -0.5% Cu /300 TiW | 0.830 µm |
| Passivation | 1000Å Oxide + 9000Å Nitride | — |

### QTP 004405: Fab4/R52LD-5R

*Micro Power Asynchronous, R52LD-5R Technology Fab 4 Cypress.* Design rule: CMOS, Double Metal , 0.25 µm/0.3 FETS. Earliest dated history row: Sep 00 (QTP 99396).[^qtp-004405]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500 Å TiW/6000 Å Al-.5%Cu/300 Å TiW | 0.680 µm |
| Metal 2 | 300Å CoTi /8000Å Al-.5%Cu/300Å TiW | 0.860 µm |
| Passivation | 1000Å PECVD Oxide, 9000Å PECVD Si3N4 | — |

### QTP 005105: Fab4/R52FFD-3

*CY7C65640A TetraHub High Speed USB Hub Controller, R52FFD-3 Technology, Fab 4.* Design rule: CMOS, Double Metal, 0.25 µm. Earliest dated history row: Aug 99 (QTP 99311).[^qtp-005105]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6,000Å Al-0.5%Cu/300Å TiW | 0.680 µm |
| Metal 2 | 300Å Ti/8,000Å Al-0.5%Cu/300Å TiW | 0.860 µm |
| Passivation | 1,000Å Oxide / 9,000 Å Nitride | — |

### QTP 011103: WaferTech 0.25um 3P2M Process Technology

*WaferTech 0.25um 3P2M Process Technology.* Design rule: CMOS, Double Metal / 0.25um. Earliest dated history row: Mar 01 (QTP 011103).[^qtp-011103]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 4,000Å AlCu/.700Å TiN | 0.400 µm |
| Metal 2 | 1,000Å TiN/6,000Å AlCu/250Å TiN | 0.725 µm |
| Passivation | 1,500Å SiON / 5,000Å SOG/10,000Å PESN | — |

### QTP 012705: Fab4/R52FFD-3

*1MEG SRAM Fast Asynchronous Family, R52FFD-3 Technology, Fab 4.* Design rule: CMOS, Double Metal, 0.25 m (the µ is not printed in the report). Earliest dated history row: Oct 00 (QTP 000505).[^qtp-012705]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6,000Å Al-0.5%Cu/300Å TiW | 0.680 µm |
| Metal 2 | 300Å Ti/8,000Å Al-0.5%Cu/300Å TiW | 0.860 µm |
| Passivation | 1,000Å Oxide / 9,000 Å Nitride | — |

### QTP 024907: Fab4 / B53D-3

*WirelessUSB Radio, CYWUSB6941, B53D-3 Technology, Fab4.* Design rule: CMOS, 0.25 µm. Earliest dated history row: Oct 01 (QTP 011406).[^qtp-024907]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500/6000/300 [Å] | 0.680 µm |
| Metal 2 | 500/6000/300 [Å] | 0.680 µm |
| Passivation | 1,000A TEOS + 9,000A Si2N4 | — |

### QTP 025003: Fab4/R52T-3

*Clock Synthesizer with Differential SRC and CPU Outputs, R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: May 03 (QTP 024604).[^qtp-025003]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 032005: Fab4 / B53D-3

*WirelessUSB Device Family, B53D-3RF Technology, Fab 4.* Design rule: CMOS, 0.25 µm. Earliest dated history row: Aug 00 (QTP 99256).[^qtp-032005]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500/6000/300 [Å] | 0.680 µm |
| Metal 2 | 500/6000/300 [Å] | 0.680 µm |
| Passivation | 1,000A TEOS + 9,000A Si2N4 | — |

### QTP 041603: Fab4/R52T-3

*Next Generation FTG for Intel Architecture, R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: the history table gives no dates.[^qtp-041603]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 041801: Fab4/R52T-3

*Clock Generator for Intel Grantsdale Chipset, R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: the history table gives no dates.[^qtp-041801]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 043502: Fab4/R52T-3

*Clock Generator for Intel Alviso Chipset, R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: June 03 (QTP 025003).[^qtp-043502]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å A1 / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 050401: Fab4/R52T-3

*AV Clock Generator, R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: May 03 (QTP 024604).[^qtp-050401]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1,000Å TEOS + 9000Å Si2N4 | — |

### QTP 050502: Fab4/R52T-3

*Clock Generator for Intel Blackford and Bayshore Chipset, R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: the history table gives no dates.[^qtp-050502]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 051203: Fab4/R52T-3

*Clock Generator for Intel Grantsdale Chipset, R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: Feb 05 (QTP 040903).[^qtp-051203]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 051804: Fab4/R52T-3

*Microsoft Xenon Clock Generator (Option D), R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: Feb 05 (QTP 040903).[^qtp-051804]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 053404: Fab4/R52T-3

*Clock Generator for Intel Calistoga Chipset, R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: Feb 05 (QTP 040903).[^qtp-053404]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 054203: Fab4/R52T-3

*Clock Generator for Intel Calistoga Chipset, R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: Feb 05 (QTP 040903).[^qtp-054203]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 054810: Fab4/R52T-3

*Clock Generator for Intel Calistoga Chipset, R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: Feb 05 (QTP 040903).[^qtp-054810]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 060703: Fab4/R52T-3

*Clock Generator for Intel Lakeport Chipset, R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: Feb 05 (QTP 040903).[^qtp-060703]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 062201: 7C02638A

*MoBL ADM Dual Port Static RAM Family, R52LD-3 Technology, Fab4.* Design rule: R52 TDR (01-30065), 0.25um Technology. Earliest dated history row: Apr 99 (QTP 99075).[^qtp-062201]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500 Å-TiW/6000 Å Al-Cu/500 Å TiW | 0.700 µm |
| Metal 2 | 300 Å-Ti/8000 Å Al-Cu/300 Å TiW | 0.860 µm |
| Passivation | 1,000A TEOS + 9,000A SiN | — |

### QTP 063108: Fab4/R52T-3

*Clock Generator For Intel CK410M/CK505, R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: Feb 05 (QTP 040903).[^qtp-063108]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 063109: Fab4/R52T-3

*Clock Generator for Intel CK410M/CK505, R52T-3 Technology, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: Feb 05 (QTP 040903).[^qtp-063109]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 063606: Fab4/R52T-3

*Clock Generator for Intel Crestline Chipset, R52T-3, Fab4.* Design rule: CMOS – Triple Metal, 0.25µm. Earliest dated history row: Feb 05 (QTP 040903).[^qtp-063606]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 082506: Fab4/R52T-3

*PCI-E Clock Family, R52T-3 Technology, Fab 4.* Design rule: CMOS – Triple Metal, 0.25μm. Earliest dated history row: May 03 (QTP 024604).[^qtp-082506]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 3 | 300Å Ti / 8000Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å SiO2 / 9000Å Si3N4 | — |

### QTP 99202: Fab4/R52D-3

*Low Voltage Synchronous/Asynchronous RAM, R52D-3 Technology at Fab 4.* Design rule: CMOS, Double Metal /0.25 m (the µ is not printed in the report). Earliest dated history row: Sep 99 (QTP 99202).[^qtp-099202]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500 Å TiW/6000 Å Al-.5%Cu/300 Å TiW | 0.680 µm |
| Metal 2 | 300Å CoTi/8000Å Al-.5%Cu/300Å TiW | 0.860 µm |
| Passivation | 1000Å Oxide + 9000Å Nitride | — |

### QTP 99503: Fab4/R52D-3

*4 Meg Synchronous Cache RAM, R52D-3 Technology at Fab 4.* Design rule: CMOS, Double Metal /0.25 µm. Earliest dated history row: Aug 99 (QTP 99311).[^qtp-099503]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500 Å TiW/6000 Å Al-.5%Cu/300 Å TiW | 0.680 µm |
| Metal 2 | 300Å CoTi/8000Å Al-.5%Cu/300Å TiW | 0.860 µm |
| Passivation | 1000Å Oxide + 9000Å Nitride | — |

### QTP 043001: Fab 4/ B55SGT

*FastEdge Series, B55SGT Technology, Fab 4.* Design rule: CMOS (0.21 – 0.35 µm), SiGe Bipolar. Earliest dated history row: May 03 (QTP 015104).[^qtp-043001]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 8000Å Al / 500Å TiW | 0.900 µm |
| Metal 3 | 500Å TiW / 40,000Å Al / 300Å TiW | 4.080 µm |
| Passivation | 4000Å TEOS / 9000Å Si3N4 | — |

### QTP 051101: Fab 4/ B55SGT

*FastEdge Series, B55SGT Technology, Fab 4.* Design rule: CMOS (0.21 – 0.35 µm), SiGe Bipolar. Earliest dated history row: May 03 (QTP 015104).[^qtp-051101]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 8000Å Al / 500Å TiW | 0.900 µm |
| Metal 3 | 500Å TiW / 40,000Å Al / 300Å TiW | 4.080 µm |
| Passivation | 4000Å TEOS / 9000Å Si3N4 | — |

### QTP 051102: Fab 4/ B55SGT

*FastEdge Series, B55SGT Technology, Fab 4.* Design rule: CMOS (0.21 – 0.35 µm), SiGe Bipolar. Earliest dated history row: May 03 (QTP 015104).[^qtp-051102]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW / 6000Å Al / 500Å TiW | 0.700 µm |
| Metal 2 | 500Å TiW / 8000Å Al / 500Å TiW | 0.900 µm |
| Metal 3 | 500Å TiW / 40,000Å Al / 300Å TiW | 4.080 µm |
| Passivation | 4000Å TEOS / 9000Å Si3N4 | — |

### QTP 014807: RAM7FT-3R

*Technology Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM CY7C085xV / CY7C083xV.* Design rule: CMOS, Triple Metal /0.18 um. Earliest dated history row: Feb 02 (QTP 014807).[^qtp-014807]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti / 4,200Å Al / 300Å TiW | 0.465 µm |
| Metal 2 | 150Å Ti /4,200 Å Al / 300Å TiW | 0.465 µm |
| Metal 3 | 150Å Ti / 8,000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1000Å TEOS / 9000Å PECVD Nitride | — |

### QTP 023101: RAM7FT-3R

*Synchronous Dual Port RAM Family CY7C083xV / CY7C085xV, R7FTW-3R Technology Fab4.* Design rule: CMOS, Triple Metal /0.18 um. Earliest dated history row: Feb 02 (QTP 014807).[^qtp-023101]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti / 4,200Å Al / 300Å TiW | 0.465 µm |
| Metal 2 | 150Å Ti /4,200 Å Al / 300Å TiW | 0.465 µm |
| Metal 3 | 150Å Ti / 8,000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1,000A TEOS + 9,000A SiN | — |

### QTP 032301: U016TFF

*16 MEG A/D MUX SRAM, S17 Technology, Promos Fab in Taiwan.* Design rule: Promos S17/0.17 µm. Earliest dated history row: Feb 03 (QTP 020606).[^qtp-032301]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Al Cu (WL) | — |
| Metal 2 | Al Cu | — |
| Passivation | 1650Å TEOS / 4500Å Nitride | — |

### QTP 041005: BF009S1

*8-Meg Super TSRAM Device, 0.165um Technology, Power Chip in Taiwan.* Design rule: 0.165 µm. Earliest dated history row: Jan 04 (QTP 040504).[^qtp-041005]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | TiN/Ti (18/8.5nm) | 0.027 µm (implausibly thin for a metal layer; the report may omit a film or misprint a unit) |
| Metal 2 | TiN/AlCu/TiN (23/800/28nm) | 0.851 µm |
| Passivation | Si3N4 and Polyimide | — |

### QTP 012005: Fab4/R7LD-3R

*MoBL and Micropower-Low Power Asynchronous SRAM, Technology Derivative R7LD-3, Fab4.* Design rule: CMOS, Double Metal /0.16 µm. Earliest dated history row: Dec 01 (QTP 014502).[^qtp-012005]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100Å Ti / 300Å TiN / 6,000Å Al / 300Å TiW | 0.670 µm |
| Metal 2 | 8,000Å TiAl / 300Å TiN | 0.830 µm |
| Passivation | 1000Å TEOS / 9000Å Nitride | — |

### QTP 012801: Fab4/R7-1.8

*4 Meg SRAM Device R7LD-1.8 Technology, Fab4.* Design rule: CMOS, Double Metal /0.16 µm. Earliest dated history row: Jun 01 (QTP 012411).[^qtp-012801]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti / 4,200Å Al / 300Å TiW | 0.465 µm |
| Metal 2 | 300Å Ti/8,000 Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å TEOS / 9000Å Nitride | — |

### QTP 051501: BF04301

*Cypress Minnesota (CMI) Sort Site Qualification -- 2 Meg, 3V PSRAM Device, PowerChip 0.165µm.* Design rule: 0.16um + Stack Capacitor. Earliest dated history row: Mar 05 (QTP 050707).[^qtp-051501]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | TiN/Ti (18/8.5nm) | 0.027 µm (implausibly thin for a metal layer; the report may omit a film or misprint a unit) |
| Metal 2 | TiN/Alcu/TiN (23/800/28nm) | 0.851 µm |
| Passivation | Si3N4 & Polyimide | — |

### QTP 011908: Fab4/R7FD-3R

*Fast Asynchronous SRAM Technology Derivative R7FD, Fab 4 Qualification.* Design rule: CMOS, Double Metal /0.15 um. Earliest dated history row: Dec 01 (QTP 011305).[^qtp-011908]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti / 4,200Å Al / 300Å TiW | 0.465 µm |
| Metal 2 | 300Å Ti /8,000 Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å TEOS / 9000Å PECVD Nitride | — |

### QTP 024903: Fab4/R7FT-3R

*Synchronous SRAM Family, Technology Derivative R7FT-3R, Fab4.* Design rule: CMOS, Triple Metal /0.15 µm. Earliest dated history row: Feb 02 (QTP 014807).[^qtp-024903]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti / 4,200Å Al / 300Å TiW | 0.465 µm |
| Metal 2 | 150Å Ti /4,200 Å Al / 300Å TiW | 0.465 µm |
| Metal 3 | 150Å Ti / 8,000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1000Å TEOS / 9000Å PECVD Nitride | — |

### QTP 032105: Fab4/R7FFT-1.8

*18 Meg QDR/DDR Synchronous SRAM, R7FFT-18, Fab 4.* Design rule: 0.15 µm. Earliest dated history row: Aug 03 (QTP 032105).[^qtp-032105]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti/4,230Å Al/300Å TiW | 0.468 µm |
| Metal 2 | 150Å Ti/4,230Å Al/300Å TiW | 0.468 µm |
| Metal 3 | 150Å Ti/8,000Å Al/300Å TiW | 0.845 µm |
| Passivation | 700Å TEOS over M3 / 7,000Å Nitride over Oxide | — |

### QTP 024110: Fab4/RAM8NLD-1.8V

*1 MEG (3.0V) MOBL DEVICES RAM8NLD-1.8V TECHNOLOGY, FAB4.* Design rule: 0.13 m (the µ is not printed in the report). Earliest dated history row: Mar 03 (QTP 031102).[^qtp-024110]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150 Å Ti / 300 Å Al / 300 Å Cu | 0.075 µm (implausibly thin for a metal layer; the report may omit a film or misprint a unit) |
| Metal 2 | 300 Å Ti / 8000 Å Al | 0.830 µm |
| Passivation | 1000Å TEOS / 9000Å Si3N4 | — |

### QTP 042105: Fab4, C8Q-3R

*DDR2 Register Device Family, C8Q-3R Technology, Fab 4.* Design rule: CMOS, 0.13 µm. Earliest dated history row: Jan 05 (QTP 042106).[^qtp-042105]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 300A Ti/3,200A Al 0.5% Cu /300A TiW | 0.380 µm |
| Metal 2 | 150A Ti/4,000A Al 0.5% Cu/300A TiW | 0.445 µm |
| Metal 3 | 150A Ti/4,000A Al 0.5% Cu/300A TiW | 0.445 µm |
| Metal 4 | 150A Ti/4,000A Al 0.5% Cu/300A TiW | 0.445 µm |
| Passivation | 1,000A TeOs / 9,000A Si3N4 | — |

### QTP 042106: Fab4, C8Q-3R

*DDR2 PLL Device Family, C8Q-3R Technology, Fab 4.* Design rule: CMOS, 0.13 µm. Earliest dated history row: Jan 05 (QTP 042106).[^qtp-042106]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100A Ti/3,200A Al 0.5% Cu /300A TiW | 0.360 µm |
| Metal 2 | 150A Ti/4,230A Al 0.5% Cu/300A TiW | 0.468 µm |
| Metal 3 | 150A Ti/4,230A Al 0.5% Cu/300A TiW | 0.468 µm |
| Metal 4 | 150A Ti/8,000A Al 0.5% Cu/300A TiW | 0.845 µm |
| Passivation | 1,000A TeOs / 9,000A Si3N4 | — |

### QTP 043004: Fab4, C8Q-3R

*DDR2-PLL Device Family, C8Q-3R, Fab 4.* Design rule: CMOS, 0.13 µm. Earliest dated history row: Jan 05 (QTP 042106).[^qtp-043004]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100A Ti/3,200A Al 0.5% Cu /300A TiW | 0.360 µm |
| Metal 2 | 150A Ti/4,230A Al 0.5% Cu/300A TiW | 0.468 µm |
| Metal 3 | 150A Ti/4,230A Al 0.5% Cu/300A TiW | 0.468 µm |
| Metal 4 | 150A Ti/8,000A Al 0.5% Cu/300A TiW | 0.845 µm |
| Passivation | 1,000A TEOs / 9,000A Si3N4 | — |

### QTP 044505: Fab4, C8Q-3R

*FX2LP/FX1-128 Device Family, C8Q-3R Technology, Fab 4.* Design rule: CMOS, 0.13 µm. Earliest dated history row: Jan 05 (QTP 033805).[^qtp-044505]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 300A Ti/3,200A Al 0.5% Cu /300A TiW | 0.380 µm |
| Metal 2 | 150A Ti/4,000A Al 0.5% Cu/300A TiW | 0.445 µm |
| Metal 3 | 150A Ti/4,000A Al 0.5% Cu/300A TiW | 0.445 µm |
| Metal 4 | 150A Ti/4,000A Al 0.5% Cu/300A TiW | 0.445 µm |
| Passivation | 1,000A TeOs / 9,000A Si3N4 | — |

### QTP 053301: Fab4, L8C-3R

*L8C-3R Technology, Fab 4.* Design rule: CMOS, 0.13 µm. Earliest dated history row: Jan 05 (QTP 042106).[^qtp-053301]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100A Ti/3,200A Al 0.5% Cu /300A TiW | 0.360 µm |
| Metal 2 | 150A Ti/4,230A Al 0.5% Cu/300A TiW | 0.468 µm |
| Metal 3 | 150A Ti/4,230A Al 0.5% Cu/300A TiW | 0.468 µm |
| Metal 4 | 150A Ti/8,000A Al 0.5% Cu/300A TiW | 0.845 µm |
| Passivation | 1,000A TeOs / 9,000A Si3N4 | — |

### QTP 071005: Fab4, C8Q-3R

*West Bridge Astoria, C8Q-3R Technology, Fab4.* Design rule: CMOS, 0.13 µm. Earliest dated history row: Jan 05 (QTP 033805).[^qtp-071005]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti / 3,200Å Al 0.5% Cu / 300Å TiW | 0.365 µm |
| Metal 2 | 150Å Ti / 4,000Å Al 0.5% Cu / 300 Å TiW | 0.445 µm |
| Metal 3 | 150Å Ti / 4,000 Å Al 0.5% Cu / 300Å TiW | 0.445 µm |
| Metal 4 | 150Å Ti / 8,000Å Al 0.5% Cu / 300Å TiW | 0.845 µm |
| Passivation | 1,000Å TeOs / 9,000Å Si3N4 | — |

### QTP 082609: Fab5, C8Q-3R

*HX2LP Device Family, C8Q-3R Technology, Fab 5.* Design rule: CMOS, 0.13µm. Earliest dated history row: Sep 07 (QTP 065201).[^qtp-082609]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100A Ti/3,200A Al 0.5% Cu/300A TiW | 0.360 µm |
| Metal 2 | 150A Ti/4,230A Al 0.5% Cu/300A TiW | 0.468 µm |
| Metal 3 | 150A Ti/4,230 Al 0.5% Cu/300A TiW | 0.045 µm (implausibly thin for a metal layer; the report may omit a film or misprint a unit) |
| Metal 4 | 150A Ti/8,000 Al 0.5% Cu/300A TiW | 0.045 µm (implausibly thin for a metal layer; the report may omit a film or misprint a unit) |
| Passivation | 1000Å TEOS / 9000Å Si3N4 | — |

### QTP 113005: Fab4 / S8TNV-5

*64K Serial Non-Volatile SRAM Product Family, S8 Technology, CMI (Fab 4).* Design rule: S8TNV-5R/0.13µm (the report prints µ with a non-standard font glyph). Earliest dated history row: Nov 2008 (QTP 071304).[^qtp-113005]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100A Ti / 3200A Al -0.5%Cu / 300A TiW | 0.360 µm |
| Metal 2 | 100A Ti / 3200A Al -0.5%Cu / 300A TiW | 0.360 µm |
| Metal 3 | 150A Ti / 7200A Al -0.5%Cu / 300A TiW | 0.765 µm |
| Passivation | 7000 +/- 2000A Nitride | — |

### QTP 032003: Fab4/R9T-3R

*36 Meg Synchronous SRAM Family, Technology R9T-3R, Fab4.* Design rule: CMOS, Triple Metal, 90 nm. Earliest dated history row: Nov 04 (QTP 044403).[^qtp-032003]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti /3200Å Al / 300Å TiW | 0.365 µm |
| Metal 2 | 150Å Ti /6000 Å Al / 300Å TiW | 0.645 µm |
| Metal 3 | 150Å Ti / 8,000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1000Å Oxide TEOS / 9000Å Nitride | — |

### QTP 044201: Fab4/R9Q-3R

*36 Meg QDR Synchronous SRAM Family, R9Q-3R Technology, Fab4.* Design rule: CMOS, Quad Metal, 90 nm. Earliest dated history row: Sep 04 (QTP 033302).[^qtp-044201]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti / 3200Å Al / 300Å TiW | 0.365 µm |
| Metal 2 | 150Å Ti / 6000Å Al / 300Å TiW | 0.645 µm |
| Metal 3 | 150Å Ti / 6000Å Al / 300Å TiW | 0.645 µm |
| Metal 4 | 150Å Ti / 8000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1000Å Oxide TEOS / 9000Å Nitride | — |

### QTP 051207: Fab4/R9Q-3R

*18 MEG QDR SYNCHRONOUS SRAM FAMILY, R9Q-3R TECHNOLOGY, FAB4.* Design rule: CMOS, Triple Metal, 90 nm. Earliest dated history row: Sep 04 (QTP 033302).[^qtp-051207]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti /3200Å Al / 300Å TiW | 0.365 µm |
| Metal 2 | 150Å Ti /6000 Å Al / 300Å TiW | 0.645 µm |
| Metal 3 | 150Å Ti / 6000Å Al / 300Å TiW | 0.645 µm |
| Metal 4 | 150Å Ti / 8000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1000Å Oxide TEOS / 9000Å Nitride | — |

### QTP 051901: Fab4/R9Q-3R

*72 Meg QDR Synchronous SRAM Family, R9Q-3R Technology, Fab4.* Design rule: CMOS, Quad Metal, 90 nm. Earliest dated history row: Sept 04 (QTP 033302).[^qtp-051901]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti /3200Å Al / 300Å TiW | 0.365 µm |
| Metal 2 | 150Å Ti /6000 Å Al / 300Å TiW | 0.645 µm |
| Metal 3 | 150Å Ti / 6000Å Al / 300Å TiW | 0.645 µm |
| Metal 4 | 150Å Ti / 8000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1000Å Oxide TEOS / 9000Å Nitride | — |

### QTP 053103: Fab4/R9 Technology

*Nitride Seal Mask (NSM) Qualification, R9T and R9Q Technology, Fab 4.* Design rule: CMOS 90 nm. Earliest dated history row: Sept 04 (QTP 033302).[^qtp-053103]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 2 | 150Å Ti / 6000Å Al / 300Å TiW | 0.645 µm |
| Metal 3 | 150Å Ti / 8000Å Al / 300Å TiW. Four Metal Layers Process: Metal 1: 150Å Ti / 3200Å Al / 300Å TiW | 1.210 µm |
| Metal 2 | 150Å Ti / 6000Å Al / 300Å TiW | 0.645 µm |
| Metal 2 | 150Å Ti / 6000Å Al / 300Å TiW | 0.645 µm |
| Metal 4 | 150Å Ti / 8000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1000Å Oxide TEOS / 9000Å Nitride | — |

### QTP 060908: Fab4/R9Q-3R

*36 Meg QDR/DDR Synchronous SRAM Family, R9Q-3R Technology, Fab4.* Design rule: CMOS, Quad Metal, 90 nm. Earliest dated history row: Sep 04 (QTP 033302).[^qtp-060908]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti / 3200Å Al / 300Å TiW | 0.365 µm |
| Metal 2 | 150Å Ti / 6000Å Al / 300Å TiW | 0.645 µm |
| Metal 3 | 150Å Ti / 6000Å Al / 300Å TiW | 0.645 µm |
| Metal 4 | 150Å Ti / 8000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1000Å Oxide TEOS / 9000Å Nitride | — |

### QTP 061806: Fab4/R95LD-3R

*4 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4.* Design rule: CMOS, Double Metal, 0.09µm (the report prints µ with a non-standard font glyph). Earliest dated history row: Mar 07 (QTP 071103).[^qtp-061806]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100Å Ti / 3200Å Al / 300Å TiW | 0.360 µm |
| Metal 2 | 150Å Ti / 8000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1000Å Oxide TEOS / 9000Å Nitride | — |

### QTP 063807: Fab4/C9FD-3R

*1 Meg Fast Asynchronous SRAM Family, C9FD-3R Technology, Fab4.* Design rule: CMOS, Double Metal, 0.09μm. Earliest dated history row: Mar 06 (QTP 052207).[^qtp-063807]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100Å Ti / 3200Å Al / 300Å TiW | 0.360 µm |
| Metal 2 | 150Å Ti / 8000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1000Å Oxide TEOS / 9000Å Nitride | — |

### QTP 071302: Fab4/R95LD-3R

*16 Meg MoBL SRAM Family, Technology R95LD-3R, Fab4.* Design rule: CMOS, Double Metal, 0.09µm. Earliest dated history row: Dec 05 (QTP 054302).[^qtp-071302]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100Å Ti / 3200Å Al / 300Å TiW | 0.360 µm |
| Metal 2 | 150Å Ti / 8000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1000Å Oxide TEOS / 9000Å Nitride | — |

### QTP 072002: Fab4/R95LD-3R

*2 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4.* Design rule: CMOS, Double Metal, 0.09μm. Earliest dated history row: Mar 07 (QTP 071103).[^qtp-072002]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100Å Ti / 3200Å Al / 300Å TiW | 0.360 µm |
| Metal 2 | 150Å Ti / 8000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1000Å Oxide TEOS / 9000Å Nitride | — |

### QTP 091206: HHGrace Fab 3/R95LD-3R

*16 Meg MoBL SRAM Family, Technology R95LD-3R, HHGrace Fab 3.* Design rule: CMOS, Double Metal, 0.09µm. Earliest dated history row: Dec 2010 (QTP 091206).[^qtp-091206]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Ti/TiN/Al/Ti/TiN: 150/250/3200/90/500 Å | 0.050 µm (implausibly thin for a metal layer; the report may omit a film or misprint a unit) |
| Metal 2 | TiN/Al/TiN: 500/6500/250Å | 0.025 µm (implausibly thin for a metal layer; the report may omit a film or misprint a unit) |
| Passivation | 1000A TEOS/ 9000A Nitride | — |

## References

### Cross-check

* {ref}`history-fabs` — which fab ran each process, from annual reports and the press.

### Deep dive

* [Cypress, QTP 000505](<https://web.archive.org/web/20210517171315/https://www.cypress.com/file/91326/download>) — 1 Meg Fast Asynchronous SRAM, R52FD-3 Technology, Fab 4.[^qtp-000505]
* [Cypress, QTP 000901](<https://web.archive.org/web/20211025142441/https://www.cypress.com/file/91341/download>) — Three-PLL Programmable Clock Generator, Fab 2 – L28 Technology.[^qtp-000901]
* [Cypress, QTP 001004](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-001004-productqualificationreport-en.pdf>) — 0.5um TLM Technology, Fab HME, Dual Port SRAM with PCI Bus Controller.[^qtp-001004]
* [Cypress, QTP 001605](<https://web.archive.org/web/20211203231803/https://www.cypress.com/file/92016/download>) — 256K Fast Asynchronous SRAM, R42HDHA Technology, Fab 4.[^qtp-001605]
* [Cypress, QTP 002202](<https://web.archive.org/web/20210509103832/https://www.cypress.com/file/135526/download>) — Robo Clock II High-Speed Multi-Phase PLL Clock, B53D-3 Technology, Fab 4.[^qtp-002202]
* [Cypress, QTP 002603](<https://web.archive.org/web/20211207090612/https://www.cypress.com/file/92046/download>) — 4 Meg FCP MoBL SRAM Family, R52LD-3 Technology, Fab 4.[^qtp-002603]
* [Cypress, QTP 002703](<https://web.archive.org/web/20201031003107/https://www.cypress.com/file/91526/download>) — Full Speed CYUSB Family, EZ-USB FX, 0.35um TLM Technology, Fab 25.[^qtp-002703]
* [Cypress, QTP 003906](<https://web.archive.org/web/20210506140210/https://www.cypress.com/file/91811/download>) — 4 Meg MoBL2 SRAM, R52D-3 Technology, Fab 4.[^qtp-003906]
* [Cypress, QTP 003907](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-003907-high-frequency-programmable-pecl-clock-generator-r42ldha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714957940a14>) — High Frequency Programmable PECL Clock Generator R42LDHA Technology, Fab 4.[^qtp-003907]
* [Cypress, QTP 004405](<https://web.archive.org/web/20211207081647/https://www.cypress.com/file/91836/download>) — Micro Power Asynchronous, R52LD-5R Technology Fab 4 Cypress.[^qtp-004405]
* [Cypress, QTP 004604](<https://web.archive.org/web/20201025122042/https://www.cypress.com/file/91846/download>) — High Accuracy EPROM Programmable Crystal Oscillator, L28 Technology, Fab 2.[^qtp-004604]
* [Cypress, QTP 005004](<https://web.archive.org/web/20170606123624/http://www.cypress.com:80/file/121666/download>) — HOTLink DX Family, R42LHDHA Technology, Fab 4.[^qtp-005004]
* [Cypress, QTP 005105](<https://web.archive.org/web/20210507215953/https://www.cypress.com/file/91571/download>) — CY7C65640A TetraHub High Speed USB Hub Controller, R52FFD-3 Technology, Fab 4.[^qtp-005105]
* [Cypress, QTP 010902](<https://web.archive.org/web/20210518082051/https://www.cypress.com/file/91606/download>) — Programmable Clock Generator Family, S4AD-5 Technology, Fab 2.[^qtp-010902]
* [Cypress, QTP 011103](<https://web.archive.org/web/20201101013242/https://www.cypress.com/file/91621/download>) — WaferTech 0.25um 3P2M Process Technology.[^qtp-011103]
* [Cypress, QTP 011503](<https://web.archive.org/web/20201205124212/https://www.cypress.com/file/91641/download>) — Spread Spectrum Timing Solution for Serverworks Chipset, L28 Technology, Fab 2.[^qtp-011503]
* [Cypress, QTP 011805](<https://web.archive.org/web/20211206073612/https://www.cypress.com/file/91656/download>) — Unidirectional Synchronous FIFO with Bus Matching, R63D-25 Technology, Fab4.[^qtp-011805]
* [Cypress, QTP 011908](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-011908-fast-asynchronous-sram-technology-derivative-r7fd-fab-4-qualification-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7150e6271aff>) — Fast Asynchronous SRAM Technology Derivative R7FD, Fab 4 Qualification.[^qtp-011908]
* [Cypress, QTP 012005](<https://web.archive.org/web/20201025120945/https://www.cypress.com/file/91666/download>) — MoBL and Micropower-Low Power Asynchronous SRAM, Technology Derivative R7LD-3, Fab4.[^qtp-012005]
* [Cypress, QTP 012204](<https://web.archive.org/web/20211208062410/https://www.cypress.com/file/91681/download>) — High Accuracy EPROM Programmable Crystal Oscillator, L28 Technology, Fab 2.[^qtp-012204]
* [Cypress, QTP 012407](<https://web.archive.org/web/20210517162336/https://www.cypress.com/file/91686/download>) — Synchronous SRAM Family, R63D-25 Technology, Fab4.[^qtp-012407]
* [Cypress, QTP 012705](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-012705-1meg-sram-fast-asynchronous-family-r52ffd-3-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148db7c0893>) — 1MEG SRAM Fast Asynchronous Family, R52FFD-3 Technology, Fab 4.[^qtp-012705]
* [Cypress, QTP 012801](<https://web.archive.org/web/20210302225236/https://www.cypress.com/file/91706/download>) — 4 Meg SRAM Device R7LD-1.8 Technology, Fab4.[^qtp-012801]
* [Cypress, QTP 014807](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>) — Technology Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM CY7C085xV / CY7C083xV.[^qtp-014807]
* [Cypress, QTP 020305](<https://web.archive.org/web/20211203215015/https://www.cypress.com/file/91946/download>) — Two-PLL Clock Generator, S4AD-5 Technology, Fab 2 / R42LDHA, Fab 4.[^qtp-020305]
* [Cypress, QTP 021507](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>) — Failsafe Device Family & Options S4AD-5 SONOS Technology, Fab 2.[^qtp-021507]
* [Cypress, QTP 022505](<https://web.archive.org/web/20211025133341/https://www.cypress.com/file/91396/download>) — PSoC Microcontrollers Family, S4AD-5 Technology, Fab 2.[^qtp-022505]
* [Cypress, QTP 023101](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-023101-rev2.0-sync-dual-port-family-productqualificationreport-en.pdf>) — Synchronous Dual Port RAM Family CY7C083xV / CY7C085xV, R7FTW-3R Technology Fab4.[^qtp-023101]
* [Cypress, QTP 024110](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-024110-1-meg-3.0v-mobl-devices-ram8nld-1.8v-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152a1d61fde>) — 1 MEG (3.0V) MOBL DEVICES RAM8NLD-1.8V TECHNOLOGY, FAB4.[^qtp-024110]
* [Cypress, QTP 024903](<https://web.archive.org/web/20210302233052/https://www.cypress.com/file/91731/download>) — Synchronous SRAM Family, Technology Derivative R7FT-3R, Fab4.[^qtp-024903]
* [Cypress, QTP 024907](<https://web.archive.org/web/20210921021823/https://www.cypress.com/file/91736/download>) — WirelessUSB Radio, CYWUSB6941, B53D-3 Technology, Fab4.[^qtp-024907]
* [Cypress, QTP 025003](<https://web.archive.org/web/20211025144417/https://www.cypress.com/file/91741/download>) — Clock Synthesizer with Differential SRC and CPU Outputs, R52T-3 Technology, Fab4.[^qtp-025003]
* [Cypress, QTP 030204](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030204-256k-static-ram-automotive-devices-ram42ha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714980870ac1>) — 256K Static RAM Automotive Devices, RAM42HA Technology, Fab 4.[^qtp-030204]
* [Cypress, QTP 030206](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030206-256k-static-ram-automotive-devices-ram42hha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71491e3d0986>) — 256K Static RAM Automotive Devices, RAM42HHA Technology, Fab 4.[^qtp-030206]
* [Cypress, QTP 030702](<https://web.archive.org/web/20211130181945/https://www.cypress.com/file/92246/download>) — PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2 CTI.[^qtp-030702]
* [Cypress, QTP 031101](<https://web.archive.org/web/20210128152257/https://www.cypress.com/file/92261/download>) — High-Accuracy EPROM Programmable Device Family, L28 Technology, Fab 2.[^qtp-031101]
* [Cypress, QTP 032003](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-032003-36-meg-synchronous-sram-family-technology-r9t-3r-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714983cb0ac5>) — 36 Meg Synchronous SRAM Family, Technology R9T-3R, Fab4.[^qtp-032003]
* [Cypress, QTP 032005](<https://web.archive.org/web/20211206184334/https://www.cypress.com/file/92296/download>) — WirelessUSB Device Family, B53D-3RF Technology, Fab 4.[^qtp-032005]
* [Cypress, QTP 032105](<https://web.archive.org/web/20211207080356/https://www.cypress.com/file/92306/download>) — 18 Meg QDR/DDR Synchronous SRAM, R7FFT-18, Fab 4.[^qtp-032105]
* [Cypress, QTP 032301](<https://web.archive.org/web/20201204235131/https://www.cypress.com/file/92311/download>) — 16 MEG A/D MUX SRAM, S17 Technology, Promos Fab in Taiwan.[^qtp-032301]
* [Cypress, QTP 032508](<https://web.archive.org/web/20211130004251/https://www.cypress.com/file/92321/download>) — PSoC Mixed Signal Array Product Family, S4AD-5 Technology, Fab 2.[^qtp-032508]
* [Cypress, QTP 040901](<https://web.archive.org/web/20211025144251/https://www.cypress.com/file/92431/download>) — PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2.[^qtp-040901]
* [Cypress, QTP 041005](<https://web.archive.org/web/20210517162948/https://www.cypress.com/file/92446/download>) — 8-Meg Super TSRAM Device, 0.165um Technology, Power Chip in Taiwan.[^qtp-041005]
* [Cypress, QTP 041603](<https://web.archive.org/web/20210415090123/https://www.cypress.com/file/92056/download>) — Next Generation FTG for Intel Architecture, R52T-3 Technology, Fab4.[^qtp-041603]
* [Cypress, QTP 041801](<https://web.archive.org/web/20211203231242/https://www.cypress.com/file/92076/download>) — Clock Generator for Intel Grantsdale Chipset, R52T-3 Technology, Fab4.[^qtp-041801]
* [Cypress, QTP 042105](<https://web.archive.org/web/20210509141440/https://www.cypress.com/file/92091/download>) — DDR2 Register Device Family, C8Q-3R Technology, Fab 4.[^qtp-042105]
* [Cypress, QTP 042106](<https://web.archive.org/web/20210419230227/https://www.cypress.com/file/92096/download>) — DDR2 PLL Device Family, C8Q-3R Technology, Fab 4.[^qtp-042106]
* [Cypress, QTP 042505](<https://web.archive.org/web/20201202160306/https://www.cypress.com/file/92111/download>) — PSoC Mixed Signal Array (Neutron Product) Family, S4AD-5 Technology, Fab 2.[^qtp-042505]
* [Cypress, QTP 042702](<https://web.archive.org/web/20201205134142/https://www.cypress.com/file/92126/download>) — Automotive PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2.[^qtp-042702]
* [Cypress, QTP 042806](<https://web.archive.org/web/20211025144943/https://www.cypress.com/file/92521/download>) — S4ADLATCH Technology, Fab 2.[^qtp-042806]
* [Cypress, QTP 043001](<https://web.archive.org/web/20210422152204/https://www.cypress.com/file/92146/download>) — FastEdge Series, B55SGT Technology, Fab 4.[^qtp-043001]
* [Cypress, QTP 043004](<https://web.archive.org/web/20201205122906/https://www.cypress.com/file/92151/download>) — DDR2-PLL Device Family, C8Q-3R, Fab 4.[^qtp-043004]
* [Cypress, QTP 043502](<https://web.archive.org/web/20210507131607/https://www.cypress.com/file/92196/download>) — Clock Generator for Intel Alviso Chipset, R52T-3 Technology, Fab4.[^qtp-043502]
* [Cypress, QTP 044201](<https://web.archive.org/web/20201127164450/https://www.cypress.com/file/92546/download>) — 36 Meg QDR Synchronous SRAM Family, R9Q-3R Technology, Fab4.[^qtp-044201]
* [Cypress, QTP 044505](<https://web.archive.org/web/20210305103805/https://www.cypress.com/file/92551/download>) — FX2LP/FX1-128 Device Family, C8Q-3R Technology, Fab 4.[^qtp-044505]
* [Cypress, QTP 050401](<https://web.archive.org/web/20210422140813/https://www.cypress.com/file/92591/download>) — AV Clock Generator, R52T-3 Technology, Fab4.[^qtp-050401]
* [Cypress, QTP 050502](<https://web.archive.org/web/20201028061532/https://www.cypress.com/file/92601/download>) — Clock Generator for Intel Blackford and Bayshore Chipset, R52T-3 Technology, Fab4.[^qtp-050502]
* [Cypress, QTP 050507](<https://web.archive.org/web/20211208073525/https://www.cypress.com/file/92611/download>) — Programmable Clock Generator w/ VCXO Device Family, S4AD-LATCH, Fab 2.[^qtp-050507]
* [Cypress, QTP 051005](<https://web.archive.org/web/20211130190834/https://www.cypress.com/file/92671/download>) — Automotive PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2.[^qtp-051005]
* [Cypress, QTP 051101](<https://web.archive.org/web/20201028052046/https://www.cypress.com/file/92676/download>) — FastEdge Series, B55SGT Technology, Fab 4.[^qtp-051101]
* [Cypress, QTP 051102](<https://web.archive.org/web/20201130144548/https://www.cypress.com/file/92681/download>) — FastEdge Series, B55SGT Technology, Fab 4.[^qtp-051102]
* [Cypress, QTP 051203](<https://web.archive.org/web/20211203223904/https://www.cypress.com/file/92686/download>) — Clock Generator for Intel Grantsdale Chipset, R52T-3 Technology, Fab4.[^qtp-051203]
* [Cypress, QTP 051207](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-051207-18-meg-qdr-synchronous-sram--cy7c1313d-product-family--r9q-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148e37b08a2>) — 18 MEG QDR SYNCHRONOUS SRAM FAMILY, R9Q-3R TECHNOLOGY, FAB4.[^qtp-051207]
* [Cypress, QTP 051501](<https://web.archive.org/web/20201028052812/https://www.cypress.com/file/92636/download>) — Cypress Minnesota (CMI) Sort Site Qualification -- 2 Meg, 3V PSRAM Device, PowerChip 0.165µm.[^qtp-051501]
* [Cypress, QTP 051804](<https://web.archive.org/web/20201205002124/https://www.cypress.com/file/92716/download>) — Microsoft Xenon Clock Generator (Option D), R52T-3 Technology, Fab4.[^qtp-051804]
* [Cypress, QTP 051901](<https://web.archive.org/web/20211203232112/https://www.cypress.com/file/92721/download>) — 72 Meg QDR Synchronous SRAM Family, R9Q-3R Technology, Fab4.[^qtp-051901]
* [Cypress, QTP 053103](<https://web.archive.org/web/20210517163643/https://www.cypress.com/file/92796/download>) — Nitride Seal Mask (NSM) Qualification, R9T and R9Q Technology, Fab 4.[^qtp-053103]
* [Cypress, QTP 053301](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-053301-l8c-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149c4a70b8f>) — L8C-3R Technology, Fab 4.[^qtp-053301]
* [Cypress, QTP 053404](<https://web.archive.org/web/20210507134623/https://www.cypress.com/file/92806/download>) — Clock Generator for Intel Calistoga Chipset, R52T-3 Technology, Fab4.[^qtp-053404]
* [Cypress, QTP 054203](<https://web.archive.org/web/20201205130428/https://www.cypress.com/file/92841/download>) — Clock Generator for Intel Calistoga Chipset, R52T-3 Technology, Fab4.[^qtp-054203]
* [Cypress, QTP 054605](<https://web.archive.org/web/20211206085735/https://www.cypress.com/file/92866/download>) — P26 TLM Technology Transfer to Magnachip.[^qtp-054605]
* [Cypress, QTP 054810](<https://web.archive.org/web/20210423032337/https://www.cypress.com/file/92871/download>) — Clock Generator for Intel Calistoga Chipset, R52T-3 Technology, Fab4.[^qtp-054810]
* [Cypress, QTP 060201](<https://web.archive.org/web/20210127141736/https://www.cypress.com/file/121336/download>) — PSoC Mixed Signal Array Hydra Device Family S4AD-5 Technology, Fab4.[^qtp-060201]
* [Cypress, QTP 060703](<https://web.archive.org/web/20211203225403/https://www.cypress.com/file/92916/download>) — Clock Generator for Intel Lakeport Chipset, R52T-3 Technology, Fab4.[^qtp-060703]
* [Cypress, QTP 060908](<https://web.archive.org/web/20211025141847/https://www.cypress.com/file/92956/download>) — 36 Meg QDR/DDR Synchronous SRAM Family, R9Q-3R Technology, Fab4.[^qtp-060908]
* [Cypress, QTP 061806](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-061806-4-meg-mobl-sram-automotive-devices-r95ld-3r-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714fdec718db>) — 4 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4.[^qtp-061806]
* [Cypress, QTP 062201](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-062201-mobl-adm-dual-port-static-ram-family-r52ld-3-technology-fab4-productqualificationreport-en.pdf>) — MoBL ADM Dual Port Static RAM Family, R52LD-3 Technology, Fab4.[^qtp-062201]
* [Cypress, QTP 062509](<https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-062509-psoc21x34-95xx-gsmc-productqualificationreport-en.pdf>) — Neutron Device Family, S4AD-5 Technology, GSMC.[^qtp-062509]
* [Cypress, QTP 063003](<https://web.archive.org/web/20201101021800/https://www.cypress.com/file/93161/download>) — Nitride Seal Mask (NSM) Qualification, S4AD-5 Technology, Fab 2.[^qtp-063003]
* [Cypress, QTP 063108](<https://web.archive.org/web/20210517162439/https://www.cypress.com/file/93176/download>) — Clock Generator For Intel CK410M/CK505, R52T-3 Technology, Fab4.[^qtp-063108]
* [Cypress, QTP 063109](<https://web.archive.org/web/20201205133211/https://www.cypress.com/file/93181/download>) — Clock Generator for Intel CK410M/CK505, R52T-3 Technology, Fab4.[^qtp-063109]
* [Cypress, QTP 063606](<https://web.archive.org/web/20201204231336/https://www.cypress.com/file/93216/download>) — Clock Generator for Intel Crestline Chipset, R52T-3, Fab4.[^qtp-063606]
* [Cypress, QTP 063807](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-063807-1-meg-fast-asynchronous-sram-family-c9fd-3r-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149f5380c45>) — 1 Meg Fast Asynchronous SRAM Family, C9FD-3R Technology, Fab4.[^qtp-063807]
* [Cypress, QTP 070505](<https://web.archive.org/web/20210507230215/https://www.cypress.com/file/130041/download>) — PSoC Quark Device Family, S4AD-5 Technology, Fab 5.[^qtp-070505]
* [Cypress, QTP 071005](<https://web.archive.org/web/20211203221107/https://www.cypress.com/file/93281/download>) — West Bridge Astoria, C8Q-3R Technology, Fab4.[^qtp-071005]
* [Cypress, QTP 071104](<https://web.archive.org/web/20211203232141/https://www.cypress.com/file/134771/download>) — PSoC Mixed Signal Array Product Family, S4AD-5 Technology, Fab5.[^qtp-071104]
* [Cypress, QTP 071302](<https://web.archive.org/web/20211130000623/https://www.cypress.com/file/93006/download>) — 16 Meg MoBL SRAM Family, Technology R95LD-3R, Fab4.[^qtp-071302]
* [Cypress, QTP 071502](<https://web.archive.org/web/20211130175633/https://www.cypress.com/file/93021/download>) — Ovation 1 Family, S4AD-5/C8QR-3R Technology, Fab2/4.[^qtp-071502]
* [Cypress, QTP 072002](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-072002-2-meg-mobl-sram-cy62136-7fv30-r95ld-3rfab4-aec-q100-productqualificationreport-en.pdf>) — 2 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4.[^qtp-072002]
* [Cypress, QTP 072105](<https://web.archive.org/web/20201031161537/https://www.cypress.com/file/95561/download>) — EZ-Color Device Family, S4AD-5 Technology, GSMC.[^qtp-072105]
* [Cypress, QTP 080608](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-080608-high-accuracy-eprom-programmable-device-family-l28-technology-tsmc-2a-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714a27090cd2>) — High Accuracy EPROM Programmable Device Family, L28 Technology, TSMC-2A.[^qtp-080608]
* [Cypress, QTP 082506](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-082506-pci-e-clock-family-r52t-3-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714a4cbb0d39>) — PCI-E Clock Family, R52T-3 Technology, Fab 4.[^qtp-082506]
* [Cypress, QTP 082609](<https://web.archive.org/web/20201026131537/https://www.cypress.com/file/95566/download>) — HX2LP Device Family, C8Q-3R Technology, Fab 5.[^qtp-082609]
* [Cypress, QTP 091206](<https://web.archive.org/web/20201001021848/https://www.cypress.com/file/138641/download>) — 16 Meg MoBL SRAM Family, Technology R95LD-3R, HHGrace Fab 3.[^qtp-091206]
* [Cypress, QTP 91216](<https://web.archive.org/web/20200810011720/https://www.cypress.com/file/93411/download>) — MAX EPLD, P20 Technology, Fab 2.[^qtp-091216]
* [Cypress, QTP 091302](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-091302-mobl-asynchronous-sram-product-family-cy62256-ram42hnha-technology-fab5-gsmc-productqualificationreport-en.pdf?fileId=8ac78c8c93dda25b01953e8470a271d4>) — MoBL Asynchronous SRAM Product Family, RAM42HNHA Technology, Fab5 GSMC.[^qtp-091302]
* [Cypress, QTP 93332](<https://web.archive.org/web/20201025104819/https://www.cypress.com/file/93456/download>) — MAX EPLD, P20 Technology, Fab 2.[^qtp-093332]
* [Cypress, QTP 95075](<https://web.archive.org/web/20201028070349/https://www.cypress.com/file/93301/download>) — CY27H010 128 x 8 High Speed CMOS EPROM, P26 Technology, Fab2.[^qtp-095075]
* [Cypress, QTP 95515](<https://web.archive.org/web/20201026132608/https://www.cypress.com/file/93461/download>) — 64K SRAM, RAM28 TECHNOLOGY.[^qtp-095515]
* [Cypress, QTP 96091](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-96091-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148ab080847>) — Dual Port SRAM - R28 Technology, 6% Shrink.[^qtp-096091]
* [Cypress, QTP 96182](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-96182-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148acf9084a>) — Dual Port SRAM - R28 Technology.[^qtp-096182]
* [Cypress, QTP 96361](<https://web.archive.org/web/20210518225925/https://www.cypress.com/file/93546/download>) — Double Sync (tm) FIFO.[^qtp-096361]
* [Cypress, QTP 96411](<https://web.archive.org/web/20201026124735/https://www.cypress.com/file/93566/download>) — 256K/512K PROM - P26 Technology.[^qtp-096411]
* [Cypress, QTP 97044](<https://web.archive.org/web/20210507195824/https://www.cypress.com/file/93606/download>) — 32K x 16 SRAM, R3 Technology, Fab 4 Qualification.[^qtp-097044]
* [Cypress, QTP 97118](<https://web.archive.org/web/20210415083340/https://www.cypress.com/file/93646/download>) — 512K x 8 SRAM - R32D Technology - Fab4.[^qtp-097118]
* [Cypress, QTP 97132](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97132-32k-x-8-low-power-sram-r32-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714947ff09f5>) — 32K x 8 Low Power SRAM, R32 Technology, Fab4.[^qtp-097132]
* [Cypress, QTP 97195](<https://web.archive.org/web/20180711105406/http://www.cypress.com:80/file/93711/download>) — 128K x 8 SRAM - R32 Technology - Fab4 Qualification.[^qtp-097195]
* [Cypress, QTP 97201](<https://web.archive.org/web/20211021091010/https://www.cypress.com/file/93716/download>) — 1 Meg SRAM, R32D Technology, Fab 4 Qualification.[^qtp-097201]
* [Cypress, QTP 97211](<https://web.archive.org/web/20210517162842/https://www.cypress.com/file/93731/download>) — 1 Meg SRAM, R42D Technology, Fab 4 Qualification.[^qtp-097211]
* [Cypress, QTP 97222](<https://web.archive.org/web/20210731180045/https://www.cypress.com/file/93746/download>) — Asynchronous FIFOs - R3.2D Technology.[^qtp-097222]
* [Cypress, QTP 97344](<https://web.archive.org/web/20211025140555/https://www.cypress.com/file/93801/download>) — R32D Technology - Metal 2 Hot Aluminum.[^qtp-097344]
* [Cypress, QTP 97396](<https://web.archive.org/web/20210507122518/https://www.cypress.com/file/93831/download>) — 4 Meg SRAM, R42D Technology, Fab 4 Qualification.[^qtp-097396]
* [Cypress, QTP 97461](<https://web.archive.org/web/20210517162807/https://www.cypress.com/file/93881/download>) — 3.3V, Light Device 16-Bit FCT Family.[^qtp-097461]
* [Cypress, QTP 97476](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97476-256k-static-ram-r28-process-fab-2-qualification-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7150d8bb1af5>) — 256K STATIC RAM "CY7C194/CY7195/CY7C199" R28 PROCESS, FAB 2 QUALIFICATION.[^qtp-097476]
* [Cypress, QTP 97506](<https://web.archive.org/web/20211207083723/https://www.cypress.com/file/93896/download>) — 1 Meg SRAM, R42 Technology, Fab 4 Qualification.[^qtp-097506]
* [Cypress, QTP 97517](<https://web.archive.org/web/20210506115548/https://www.cypress.com/file/93496/download>) — 1/2 Meg SRAM, R42D Technology, Fab 4 Qualification.[^qtp-097517]
* [Cypress, QTP 98021](<https://web.archive.org/web/20210507141403/https://www.cypress.com/file/93501/download>) — 1 Meg SRAM (5% Shrink), R32D Technology, Fab 4 -- Military Devices.[^qtp-098021]
* [Cypress, QTP 98081](<https://web.archive.org/web/20211206081930/https://www.cypress.com/file/93926/download>) — Synchronous 3.3V Cache RAM, R42D Technology w/ Hot Al, Fab 4 Qualification.[^qtp-098081]
* [Cypress, QTP 98086](<https://web.archive.org/web/20211025143415/https://www.cypress.com/file/93936/download>) — 4 Meg SRAM, R42HD Technology, Hot Aluminum.[^qtp-098086]
* [Cypress, QTP 98111](<https://web.archive.org/web/20210418214054/https://www.cypress.com/file/93956/download>) — 4 Meg SRAM, R42H Technology, Hot Aluminum.[^qtp-098111]
* [Cypress, QTP 98115](<https://web.archive.org/web/20211130182828/https://www.cypress.com/file/93971/download>) — 1 Meg SRAM, R42HD Technology (5V operation).[^qtp-098115]
* [Cypress, QTP 98236](<https://web.archive.org/web/20210507140402/https://www.cypress.com/file/94031/download>) — 256K x 1 Static RAM, R28 Process, Fab 2 Qualification.[^qtp-098236]
* [Cypress, QTP 98252](<https://web.archive.org/web/20200810004607/https://www.cypress.com/file/94051/download>) — CY7C188 32K x 9 Static RAM – R28 Technology – Fab2.[^qtp-098252]
* [Cypress, QTP 98296](<https://web.archive.org/web/20210519014520/https://www.cypress.com/file/94056/download>) — 64K Static RAM – R28 Technology – Fab 2.[^qtp-098296]
* [Cypress, QTP 98313](<https://web.archive.org/web/20201205094935/https://www.cypress.com/file/94066/download>) — 2 Meg SRAM, R42HD Technology (5V operation).[^qtp-098313]
* [Cypress, QTP 98333](<https://web.archive.org/web/20201205131229/https://www.cypress.com/file/94086/download>) — 100-MHz Spread Spectrum Clock Synthesizer/Driver, USB, Hublink and SDRAM Support (CY2287PVC), Fab2, L28 Technology.[^qtp-098333]
* [Cypress, QTP 98357](<https://web.archive.org/web/20201205080246/https://www.cypress.com/file/94096/download>) — 4 Meg SRAM With NoBL Architecture, R42D Technology, Hot Aluminum.[^qtp-098357]
* [Cypress, QTP 98368](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-98368-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152cc652012>) — SYNCHRONOUS/ASYNCHRONOUS DUAL PORT SRAM (3.3V AND 5V), R42HD TECHNOLOGY, FAB 4.[^qtp-098368]
* [Cypress, QTP 98393](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-98393-productqualificationreport-en.pdf>) — Dual Port SRAM - R28 Technology - Fab 2.[^qtp-098393]
* [Cypress, QTP 98437](<https://web.archive.org/web/20210507202024/https://www.cypress.com/file/94121/download>) — 1 Meg SRAM, R42HD Technology, Fab 4 Qualification.[^qtp-098437]
* [Cypress, QTP 99034](<https://web.archive.org/web/20210507224233/https://www.cypress.com/file/94156/download>) — 5V, 8/10 Bit FCT-T, L28EPD Technology, Fab 2.[^qtp-099034]
* [Cypress, QTP 99083](<https://web.archive.org/web/20201031174241/https://www.cypress.com/file/94181/download>) — Low Voltage Synchronous FIFO – R28 Technology – Fab2.[^qtp-099083]
* [Cypress, QTP 99092](<https://web.archive.org/web/20201202161536/https://www.cypress.com/file/94191/download>) — Universal Serial Bus Microcontroller - P26 Technology in Fab 2.[^qtp-099092]
* [Cypress, QTP 99175](<https://web.archive.org/web/20211025130802/https://www.cypress.com/file/94216/download>) — Military Clocked FIFOs – R28 Technology – Fab2.[^qtp-099175]
* [Cypress, QTP 99202](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-99202-low-voltage-synchronous-asynchronous-ram-r52d-3-technology-at-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71491c270982>) — Low Voltage Synchronous/Asynchronous RAM, R52D-3 Technology at Fab 4.[^qtp-099202]
* [Cypress, QTP 99285](<https://web.archive.org/web/20201101022945/https://www.cypress.com/file/94251/download>) — L28-TSMC Technology in TSMC-2A, Taiwan.[^qtp-099285]
* [Cypress, QTP 99325](<https://web.archive.org/web/20210507133537/https://www.cypress.com/file/94266/download>) — 5V Synchronous FIFOs, R42HDHA Technology, Fab 4.[^qtp-099325]
* [Cypress, QTP 99503](<https://web.archive.org/web/20210422145212/https://www.cypress.com/file/94336/download>) — 4 Meg Synchronous Cache RAM, R52D-3 Technology at Fab 4.[^qtp-099503]
* [Cypress, QTP 102101](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-102101-synchronous-asynchronous-dual-port-sram-3.3v-and-5v-r42hd-technology-fab-4-qualification-productqualificationreport-en.pdf>) — Synchronous/Asynchronous Dual Port SRAM (3.3V and 5V), R42HD Technology, Fab 4 Qualification.[^qtp-102101]
* [Cypress, QTP 110605](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-110605-zero-delay-buffer-l28-technology-tsmc-2a-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714b37f41005>) — Zero Delay Buffer, L28 Technology, TSMC-2A.[^qtp-110605]
* [Cypress, QTP 113005](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>) — 64K Serial Non-Volatile SRAM Product Family, S8 Technology, CMI (Fab 4).[^qtp-113005]
* [Cypress, QTP 151005](<https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-151005-psoc24x94-hhgrace-productqualificationreport-en.pdf>) — PSoC RADON Device Family, S4AD-5 Technology, HHGrace FAB5.[^qtp-151005]
* [Cypress, QTP G990003](<https://web.archive.org/web/20200810011117/https://www.cypress.com/file/94381/download>) — WaferTech 0.35um.[^qtp-g990003]
* [Cypress, QTP I000005](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-i000005-0.35um-technology-csm-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152d1a52016>) — 0.35um Technology, CSM Fab 2.[^qtp-i000005]

<!-- footnotes -->

[^qtp-000505]: Cypress Semiconductor, Product Qualification Report QTP 000505: *1 Meg Fast Asynchronous SRAM, R52FD-3 Technology, Fab 4*, December 2002;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210517171315/https://www.cypress.com/file/91326/download>
[^qtp-000901]: Cypress Semiconductor, Product Qualification Report QTP 000901: *Three-PLL Programmable Clock Generator, Fab 2 – L28 Technology*, May 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025142441/https://www.cypress.com/file/91341/download>
[^qtp-001004]: Cypress Semiconductor, Product Qualification Report QTP 001004: *0.5um TLM Technology, Fab HME, Dual Port SRAM with PCI Bus Controller*, January 2001.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-001004-productqualificationreport-en.pdf>
[^qtp-001605]: Cypress Semiconductor, Product Qualification Report QTP 001605: *256K Fast Asynchronous SRAM, R42HDHA Technology, Fab 4*, December, 2002;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211203231803/https://www.cypress.com/file/92016/download>
[^qtp-002202]: Cypress Semiconductor, Product Qualification Report QTP 002202: *Robo Clock II High-Speed Multi-Phase PLL Clock, B53D-3 Technology, Fab 4*, October 2014;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210509103832/https://www.cypress.com/file/135526/download>
[^qtp-002603]: Cypress Semiconductor, Product Qualification Report QTP 002603: *4 Meg FCP MoBL SRAM Family, R52LD-3 Technology, Fab 4*, December, 2002;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211207090612/https://www.cypress.com/file/92046/download>
[^qtp-002703]: Cypress Semiconductor, Product Qualification Report QTP 002703: *Full Speed CYUSB Family, EZ-USB FX, 0.35um TLM Technology, Fab 25*, June, 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201031003107/https://www.cypress.com/file/91526/download>
[^qtp-003906]: Cypress Semiconductor, Product Qualification Report QTP 003906: *4 Meg MoBL2 SRAM, R52D-3 Technology, Fab 4*, December, 2002;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210506140210/https://www.cypress.com/file/91811/download>
[^qtp-003907]: Cypress Semiconductor, Product Qualification Report QTP 003907: *High Frequency Programmable PECL Clock Generator R42LDHA Technology, Fab 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-003907-high-frequency-programmable-pecl-clock-generator-r42ldha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714957940a14>
[^qtp-004405]: Cypress Semiconductor, Product Qualification Report QTP 004405: *Micro Power Asynchronous, R52LD-5R Technology Fab 4 Cypress*, December, 2002;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211207081647/https://www.cypress.com/file/91836/download>
[^qtp-004604]: Cypress Semiconductor, Product Qualification Report QTP 004604: *High Accuracy EPROM Programmable Crystal Oscillator, L28 Technology, Fab 2*, May 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201025122042/https://www.cypress.com/file/91846/download>
[^qtp-005004]: Cypress Semiconductor, Product Qualification Report QTP 005004: *HOTLink DX Family, R42LHDHA Technology, Fab 4*, June 2013;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20170606123624/http://www.cypress.com:80/file/121666/download>
[^qtp-005105]: Cypress Semiconductor, Product Qualification Report QTP 005105: *CY7C65640A TetraHub High Speed USB Hub Controller, R52FFD-3 Technology, Fab 4*, June 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507215953/https://www.cypress.com/file/91571/download>
[^qtp-010902]: Cypress Semiconductor, Product Qualification Report QTP 010902: *Programmable Clock Generator Family, S4AD-5 Technology, Fab 2*, March 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210518082051/https://www.cypress.com/file/91606/download>
[^qtp-011103]: Cypress Semiconductor, Product Qualification Report QTP 011103: *WaferTech 0.25um 3P2M Process Technology*, April, 2001;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201101013242/https://www.cypress.com/file/91621/download>
[^qtp-011503]: Cypress Semiconductor, Product Qualification Report QTP 011503: *Spread Spectrum Timing Solution for Serverworks Chipset, L28 Technology, Fab 2*, December 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205124212/https://www.cypress.com/file/91641/download>
[^qtp-011805]: Cypress Semiconductor, Product Qualification Report QTP 011805: *Unidirectional Synchronous FIFO with Bus Matching, R63D-25 Technology, Fab4*, February, 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211206073612/https://www.cypress.com/file/91656/download>
[^qtp-011908]: Cypress Semiconductor, Product Qualification Report QTP 011908: *Fast Asynchronous SRAM Technology Derivative R7FD, Fab 4 Qualification*, August 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-011908-fast-asynchronous-sram-technology-derivative-r7fd-fab-4-qualification-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7150e6271aff>
[^qtp-012005]: Cypress Semiconductor, Product Qualification Report QTP 012005: *MoBL and Micropower-Low Power Asynchronous SRAM, Technology Derivative R7LD-3, Fab4*, November, 2002;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201025120945/https://www.cypress.com/file/91666/download>
[^qtp-012204]: Cypress Semiconductor, Product Qualification Report QTP 012204: *High Accuracy EPROM Programmable Crystal Oscillator, L28 Technology, Fab 2*, September 2001;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211208062410/https://www.cypress.com/file/91681/download>
[^qtp-012407]: Cypress Semiconductor, Product Qualification Report QTP 012407: *Synchronous SRAM Family, R63D-25 Technology, Fab4*, November 2002;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210517162336/https://www.cypress.com/file/91686/download>
[^qtp-012705]: Cypress Semiconductor, Product Qualification Report QTP 012705: *1MEG SRAM Fast Asynchronous Family, R52FFD-3 Technology, Fab 4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-012705-1meg-sram-fast-asynchronous-family-r52ffd-3-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148db7c0893>
[^qtp-012801]: Cypress Semiconductor, Product Qualification Report QTP 012801: *4 Meg SRAM Device R7LD-1.8 Technology, Fab4*, October 2004;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210302225236/https://www.cypress.com/file/91706/download>
[^qtp-014807]: Cypress Semiconductor, Product Qualification Report QTP 014807: *Technology Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM CY7C085xV / CY7C083xV*, June 2005.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
[^qtp-020305]: Cypress Semiconductor, Product Qualification Report QTP 020305: *Two-PLL Clock Generator, S4AD-5 Technology, Fab 2 / R42LDHA, Fab 4*, August 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211203215015/https://www.cypress.com/file/91946/download>
[^qtp-021507]: Cypress Semiconductor, Product Qualification Report QTP 021507: *Failsafe Device Family & Options S4AD-5 SONOS Technology, Fab 2*, December 2015.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>
[^qtp-022505]: Cypress Semiconductor, Product Qualification Report QTP 022505: *PSoC Microcontrollers Family, S4AD-5 Technology, Fab 2*, June 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025133341/https://www.cypress.com/file/91396/download>
[^qtp-023101]: Cypress Semiconductor, Product Qualification Report QTP 023101: *Synchronous Dual Port RAM Family CY7C083xV / CY7C085xV, R7FTW-3R Technology Fab4*, June 2005.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-023101-rev2.0-sync-dual-port-family-productqualificationreport-en.pdf>
[^qtp-024110]: Cypress Semiconductor, Product Qualification Report QTP 024110: *1 MEG (3.0V) MOBL DEVICES RAM8NLD-1.8V TECHNOLOGY, FAB4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-024110-1-meg-3.0v-mobl-devices-ram8nld-1.8v-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152a1d61fde>
[^qtp-024903]: Cypress Semiconductor, Product Qualification Report QTP 024903: *Synchronous SRAM Family, Technology Derivative R7FT-3R, Fab4*, January 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210302233052/https://www.cypress.com/file/91731/download>
[^qtp-024907]: Cypress Semiconductor, Product Qualification Report QTP 024907: *WirelessUSB Radio, CYWUSB6941, B53D-3 Technology, Fab4*, June, 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210921021823/https://www.cypress.com/file/91736/download>
[^qtp-025003]: Cypress Semiconductor, Product Qualification Report QTP 025003: *Clock Synthesizer with Differential SRC and CPU Outputs, R52T-3 Technology, Fab4*, December 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025144417/https://www.cypress.com/file/91741/download>
[^qtp-030204]: Cypress Semiconductor, Product Qualification Report QTP 030204: *256K Static RAM Automotive Devices, RAM42HA Technology, Fab 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030204-256k-static-ram-automotive-devices-ram42ha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714980870ac1>
[^qtp-030206]: Cypress Semiconductor, Product Qualification Report QTP 030206: *256K Static RAM Automotive Devices, RAM42HHA Technology, Fab 4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030206-256k-static-ram-automotive-devices-ram42hha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71491e3d0986>
[^qtp-030702]: Cypress Semiconductor, Product Qualification Report QTP 030702: *PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2 CTI*, March 2008;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211130181945/https://www.cypress.com/file/92246/download>
[^qtp-031101]: Cypress Semiconductor, Product Qualification Report QTP 031101: *High-Accuracy EPROM Programmable Device Family, L28 Technology, Fab 2*, January 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210128152257/https://www.cypress.com/file/92261/download>
[^qtp-032003]: Cypress Semiconductor, Product Qualification Report QTP 032003: *36 Meg Synchronous SRAM Family, Technology R9T-3R, Fab4*, August 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-032003-36-meg-synchronous-sram-family-technology-r9t-3r-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714983cb0ac5>
[^qtp-032005]: Cypress Semiconductor, Product Qualification Report QTP 032005: *WirelessUSB Device Family, B53D-3RF Technology, Fab 4*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211206184334/https://www.cypress.com/file/92296/download>
[^qtp-032105]: Cypress Semiconductor, Product Qualification Report QTP 032105: *18 Meg QDR/DDR Synchronous SRAM, R7FFT-18, Fab 4*, May 2004;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211207080356/https://www.cypress.com/file/92306/download>
[^qtp-032301]: Cypress Semiconductor, Product Qualification Report QTP 032301: *16 MEG A/D MUX SRAM, S17 Technology, Promos Fab in Taiwan*, May 2004;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201204235131/https://www.cypress.com/file/92311/download>
[^qtp-032508]: Cypress Semiconductor, Product Qualification Report QTP 032508: *PSoC Mixed Signal Array Product Family, S4AD-5 Technology, Fab 2*, January 2008;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211130004251/https://www.cypress.com/file/92321/download>
[^qtp-040901]: Cypress Semiconductor, Product Qualification Report QTP 040901: *PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2*, March 2008;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025144251/https://www.cypress.com/file/92431/download>
[^qtp-041005]: Cypress Semiconductor, Product Qualification Report QTP 041005: *8-Meg Super TSRAM Device, 0.165um Technology, Power Chip in Taiwan*, March 2004;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210517162948/https://www.cypress.com/file/92446/download>
[^qtp-041603]: Cypress Semiconductor, Product Qualification Report QTP 041603: *Next Generation FTG for Intel Architecture, R52T-3 Technology, Fab4*, December 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210415090123/https://www.cypress.com/file/92056/download>
[^qtp-041801]: Cypress Semiconductor, Product Qualification Report QTP 041801: *Clock Generator for Intel Grantsdale Chipset, R52T-3 Technology, Fab4*, December 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211203231242/https://www.cypress.com/file/92076/download>
[^qtp-042105]: Cypress Semiconductor, Product Qualification Report QTP 042105: *DDR2 Register Device Family, C8Q-3R Technology, Fab 4*, July 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210509141440/https://www.cypress.com/file/92091/download>
[^qtp-042106]: Cypress Semiconductor, Product Qualification Report QTP 042106: *DDR2 PLL Device Family, C8Q-3R Technology, Fab 4*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210419230227/https://www.cypress.com/file/92096/download>
[^qtp-042505]: Cypress Semiconductor, Product Qualification Report QTP 042505: *PSoC Mixed Signal Array (Neutron Product) Family, S4AD-5 Technology, Fab 2*, April 2006;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201202160306/https://www.cypress.com/file/92111/download>
[^qtp-042702]: Cypress Semiconductor, Product Qualification Report QTP 042702: *Automotive PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2*, October 2006;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205134142/https://www.cypress.com/file/92126/download>
[^qtp-042806]: Cypress Semiconductor, Product Qualification Report QTP 042806: *S4ADLATCH Technology, Fab 2*, January 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025144943/https://www.cypress.com/file/92521/download>
[^qtp-043001]: Cypress Semiconductor, Product Qualification Report QTP 043001: *FastEdge Series, B55SGT Technology, Fab 4*, July 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210422152204/https://www.cypress.com/file/92146/download>
[^qtp-043004]: Cypress Semiconductor, Product Qualification Report QTP 043004: *DDR2-PLL Device Family, C8Q-3R, Fab 4*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205122906/https://www.cypress.com/file/92151/download>
[^qtp-043502]: Cypress Semiconductor, Product Qualification Report QTP 043502: *Clock Generator for Intel Alviso Chipset, R52T-3 Technology, Fab4*, December 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507131607/https://www.cypress.com/file/92196/download>
[^qtp-044201]: Cypress Semiconductor, Product Qualification Report QTP 044201: *36 Meg QDR Synchronous SRAM Family, R9Q-3R Technology, Fab4*, May 2008;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201127164450/https://www.cypress.com/file/92546/download>
[^qtp-044505]: Cypress Semiconductor, Product Qualification Report QTP 044505: *FX2LP/FX1-128 Device Family, C8Q-3R Technology, Fab 4*, July 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210305103805/https://www.cypress.com/file/92551/download>
[^qtp-050401]: Cypress Semiconductor, Product Qualification Report QTP 050401: *AV Clock Generator, R52T-3 Technology, Fab4*, December 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210422140813/https://www.cypress.com/file/92591/download>
[^qtp-050502]: Cypress Semiconductor, Product Qualification Report QTP 050502: *Clock Generator for Intel Blackford and Bayshore Chipset, R52T-3 Technology, Fab4*, December 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201028061532/https://www.cypress.com/file/92601/download>
[^qtp-050507]: Cypress Semiconductor, Product Qualification Report QTP 050507: *Programmable Clock Generator w/ VCXO Device Family, S4AD-LATCH, Fab 2*, August 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211208073525/https://www.cypress.com/file/92611/download>
[^qtp-051005]: Cypress Semiconductor, Product Qualification Report QTP 051005: *Automotive PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211130190834/https://www.cypress.com/file/92671/download>
[^qtp-051101]: Cypress Semiconductor, Product Qualification Report QTP 051101: *FastEdge Series, B55SGT Technology, Fab 4*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201028052046/https://www.cypress.com/file/92676/download>
[^qtp-051102]: Cypress Semiconductor, Product Qualification Report QTP 051102: *FastEdge Series, B55SGT Technology, Fab 4*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201130144548/https://www.cypress.com/file/92681/download>
[^qtp-051203]: Cypress Semiconductor, Product Qualification Report QTP 051203: *Clock Generator for Intel Grantsdale Chipset, R52T-3 Technology, Fab4*, December 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211203223904/https://www.cypress.com/file/92686/download>
[^qtp-051207]: Cypress Semiconductor, Product Qualification Report QTP 051207: *18 MEG QDR SYNCHRONOUS SRAM FAMILY, R9Q-3R TECHNOLOGY, FAB4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-051207-18-meg-qdr-synchronous-sram--cy7c1313d-product-family--r9q-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148e37b08a2>
[^qtp-051501]: Cypress Semiconductor, Product Qualification Report QTP 051501: *Cypress Minnesota (CMI) Sort Site Qualification -- 2 Meg, 3V PSRAM Device, PowerChip 0.165µm*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201028052812/https://www.cypress.com/file/92636/download>
[^qtp-051804]: Cypress Semiconductor, Product Qualification Report QTP 051804: *Microsoft Xenon Clock Generator (Option D), R52T-3 Technology, Fab4*, December 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205002124/https://www.cypress.com/file/92716/download>
[^qtp-051901]: Cypress Semiconductor, Product Qualification Report QTP 051901: *72 Meg QDR Synchronous SRAM Family, R9Q-3R Technology, Fab4*, May 2008;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211203232112/https://www.cypress.com/file/92721/download>
[^qtp-053103]: Cypress Semiconductor, Product Qualification Report QTP 053103: *Nitride Seal Mask (NSM) Qualification, R9T and R9Q Technology, Fab 4*, November 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210517163643/https://www.cypress.com/file/92796/download>
[^qtp-053301]: Cypress Semiconductor, Product Qualification Report QTP 053301: *L8C-3R Technology, Fab 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-053301-l8c-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149c4a70b8f>
[^qtp-053404]: Cypress Semiconductor, Product Qualification Report QTP 053404: *Clock Generator for Intel Calistoga Chipset, R52T-3 Technology, Fab4*, December 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507134623/https://www.cypress.com/file/92806/download>
[^qtp-054203]: Cypress Semiconductor, Product Qualification Report QTP 054203: *Clock Generator for Intel Calistoga Chipset, R52T-3 Technology, Fab4*, March 2006;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205130428/https://www.cypress.com/file/92841/download>
[^qtp-054605]: Cypress Semiconductor, Product Qualification Report QTP 054605: *P26 TLM Technology Transfer to Magnachip*, March 2006;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211206085735/https://www.cypress.com/file/92866/download>
[^qtp-054810]: Cypress Semiconductor, Product Qualification Report QTP 054810: *Clock Generator for Intel Calistoga Chipset, R52T-3 Technology, Fab4*, January 2006;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210423032337/https://www.cypress.com/file/92871/download>
[^qtp-060201]: Cypress Semiconductor, Product Qualification Report QTP 060201: *PSoC Mixed Signal Array Hydra Device Family S4AD-5 Technology, Fab4*, May 2013;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210127141736/https://www.cypress.com/file/121336/download>
[^qtp-060703]: Cypress Semiconductor, Product Qualification Report QTP 060703: *Clock Generator for Intel Lakeport Chipset, R52T-3 Technology, Fab4*, June 2006;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211203225403/https://www.cypress.com/file/92916/download>
[^qtp-060908]: Cypress Semiconductor, Product Qualification Report QTP 060908: *36 Meg QDR/DDR Synchronous SRAM Family, R9Q-3R Technology, Fab4*, February 2009;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025141847/https://www.cypress.com/file/92956/download>
[^qtp-061806]: Cypress Semiconductor, Product Qualification Report QTP 061806: *4 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4*, March 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-061806-4-meg-mobl-sram-automotive-devices-r95ld-3r-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714fdec718db>
[^qtp-062201]: Cypress Semiconductor, Product Qualification Report QTP 062201: *MoBL ADM Dual Port Static RAM Family, R52LD-3 Technology, Fab4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-062201-mobl-adm-dual-port-static-ram-family-r52ld-3-technology-fab4-productqualificationreport-en.pdf>
[^qtp-062509]: Cypress Semiconductor, Product Qualification Report QTP 062509: *Neutron Device Family, S4AD-5 Technology, GSMC*, July 2014.
    <https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-062509-psoc21x34-95xx-gsmc-productqualificationreport-en.pdf>
[^qtp-063003]: Cypress Semiconductor, Product Qualification Report QTP 063003: *Nitride Seal Mask (NSM) Qualification, S4AD-5 Technology, Fab 2*, June 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201101021800/https://www.cypress.com/file/93161/download>
[^qtp-063108]: Cypress Semiconductor, Product Qualification Report QTP 063108: *Clock Generator For Intel CK410M/CK505, R52T-3 Technology, Fab4*, October 2006;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210517162439/https://www.cypress.com/file/93176/download>
[^qtp-063109]: Cypress Semiconductor, Product Qualification Report QTP 063109: *Clock Generator for Intel CK410M/CK505, R52T-3 Technology, Fab4*, September 2006;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205133211/https://www.cypress.com/file/93181/download>
[^qtp-063606]: Cypress Semiconductor, Product Qualification Report QTP 063606: *Clock Generator for Intel Crestline Chipset, R52T-3, Fab4*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201204231336/https://www.cypress.com/file/93216/download>
[^qtp-063807]: Cypress Semiconductor, Product Qualification Report QTP 063807: *1 Meg Fast Asynchronous SRAM Family, C9FD-3R Technology, Fab4*, January 2024.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-063807-1-meg-fast-asynchronous-sram-family-c9fd-3r-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149f5380c45>
[^qtp-070505]: Cypress Semiconductor, Product Qualification Report QTP 070505: *PSoC Quark Device Family, S4AD-5 Technology, Fab 5*, June 2014;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507230215/https://www.cypress.com/file/130041/download>
[^qtp-071005]: Cypress Semiconductor, Product Qualification Report QTP 071005: *West Bridge Astoria, C8Q-3R Technology, Fab4*, April 2008;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211203221107/https://www.cypress.com/file/93281/download>
[^qtp-071104]: Cypress Semiconductor, Product Qualification Report QTP 071104: *PSoC Mixed Signal Array Product Family, S4AD-5 Technology, Fab5*, September 2014;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211203232141/https://www.cypress.com/file/134771/download>
[^qtp-071302]: Cypress Semiconductor, Product Qualification Report QTP 071302: *16 Meg MoBL SRAM Family, Technology R95LD-3R, Fab4*, April 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211130000623/https://www.cypress.com/file/93006/download>
[^qtp-071502]: Cypress Semiconductor, Product Qualification Report QTP 071502: *Ovation 1 Family, S4AD-5/C8QR-3R Technology, Fab2/4*, August 2008;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211130175633/https://www.cypress.com/file/93021/download>
[^qtp-072002]: Cypress Semiconductor, Product Qualification Report QTP 072002: *2 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4*, March 2025 rev*B.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-072002-2-meg-mobl-sram-cy62136-7fv30-r95ld-3rfab4-aec-q100-productqualificationreport-en.pdf>
[^qtp-072105]: Cypress Semiconductor, Product Qualification Report QTP 072105: *EZ-Color Device Family, S4AD-5 Technology, GSMC*, August 2009;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201031161537/https://www.cypress.com/file/95561/download>
[^qtp-080608]: Cypress Semiconductor, Product Qualification Report QTP 080608: *High Accuracy EPROM Programmable Device Family, L28 Technology, TSMC-2A*, May 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-080608-high-accuracy-eprom-programmable-device-family-l28-technology-tsmc-2a-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714a27090cd2>
[^qtp-082506]: Cypress Semiconductor, Product Qualification Report QTP 082506: *PCI-E Clock Family, R52T-3 Technology, Fab 4*, September 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-082506-pci-e-clock-family-r52t-3-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714a4cbb0d39>
[^qtp-082609]: Cypress Semiconductor, Product Qualification Report QTP 082609: *HX2LP Device Family, C8Q-3R Technology, Fab 5*, June 2009;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201026131537/https://www.cypress.com/file/95566/download>
[^qtp-091206]: Cypress Semiconductor, Product Qualification Report QTP 091206: *16 Meg MoBL SRAM Family, Technology R95LD-3R, HHGrace Fab 3*, January, 2015;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201001021848/https://www.cypress.com/file/138641/download>
[^qtp-091216]: Cypress Semiconductor, Product Qualification Report QTP 91216: *MAX EPLD, P20 Technology, Fab 2*, March 2000;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20200810011720/https://www.cypress.com/file/93411/download>
[^qtp-091302]: Cypress Semiconductor, Product Qualification Report QTP 091302: *MoBL Asynchronous SRAM Product Family, RAM42HNHA Technology, Fab5 GSMC*, February 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-091302-mobl-asynchronous-sram-product-family-cy62256-ram42hnha-technology-fab5-gsmc-productqualificationreport-en.pdf?fileId=8ac78c8c93dda25b01953e8470a271d4>
[^qtp-093332]: Cypress Semiconductor, Product Qualification Report QTP 93332: *MAX EPLD, P20 Technology, Fab 2*, March 2000;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201025104819/https://www.cypress.com/file/93456/download>
[^qtp-095075]: Cypress Semiconductor, Product Qualification Report QTP 95075: *CY27H010 128 x 8 High Speed CMOS EPROM, P26 Technology, Fab2*, November 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201028070349/https://www.cypress.com/file/93301/download>
[^qtp-095515]: Cypress Semiconductor, Product Qualification Report QTP 95515: *64K SRAM, RAM28 TECHNOLOGY*, July 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201026132608/https://www.cypress.com/file/93461/download>
[^qtp-096091]: Cypress Semiconductor, Product Qualification Report QTP 96091: *Dual Port SRAM - R28 Technology, 6% Shrink*, September 1996.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-96091-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148ab080847>
[^qtp-096182]: Cypress Semiconductor, Product Qualification Report QTP 96182: *Dual Port SRAM - R28 Technology*, September 1996.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-96182-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148acf9084a>
[^qtp-096361]: Cypress Semiconductor, Product Qualification Report QTP 96361: *Double Sync (tm) FIFO*, June 1997;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210518225925/https://www.cypress.com/file/93546/download>
[^qtp-096411]: Cypress Semiconductor, Product Qualification Report QTP 96411: *256K/512K PROM - P26 Technology*, May 1997;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201026124735/https://www.cypress.com/file/93566/download>
[^qtp-097044]: Cypress Semiconductor, Product Qualification Report QTP 97044: *32K x 16 SRAM, R3 Technology, Fab 4 Qualification*, November, 2002;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507195824/https://www.cypress.com/file/93606/download>
[^qtp-097118]: Cypress Semiconductor, Product Qualification Report QTP 97118: *512K x 8 SRAM - R32D Technology - Fab4*, July, 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210415083340/https://www.cypress.com/file/93646/download>
[^qtp-097132]: Cypress Semiconductor, Product Qualification Report QTP 97132: *32K x 8 Low Power SRAM, R32 Technology, Fab4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97132-32k-x-8-low-power-sram-r32-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714947ff09f5>
[^qtp-097195]: Cypress Semiconductor, Product Qualification Report QTP 97195: *128K x 8 SRAM - R32 Technology - Fab4 Qualification*, July, 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20180711105406/http://www.cypress.com:80/file/93711/download>
[^qtp-097201]: Cypress Semiconductor, Product Qualification Report QTP 97201: *1 Meg SRAM, R32D Technology, Fab 4 Qualification*, February, 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211021091010/https://www.cypress.com/file/93716/download>
[^qtp-097211]: Cypress Semiconductor, Product Qualification Report QTP 97211: *1 Meg SRAM, R42D Technology, Fab 4 Qualification*, July, 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210517162842/https://www.cypress.com/file/93731/download>
[^qtp-097222]: Cypress Semiconductor, Product Qualification Report QTP 97222: *Asynchronous FIFOs - R3.2D Technology*, December, 1997;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210731180045/https://www.cypress.com/file/93746/download>
[^qtp-097344]: Cypress Semiconductor, Product Qualification Report QTP 97344: *R32D Technology - Metal 2 Hot Aluminum*, March, 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025140555/https://www.cypress.com/file/93801/download>
[^qtp-097396]: Cypress Semiconductor, Product Qualification Report QTP 97396: *4 Meg SRAM, R42D Technology, Fab 4 Qualification*, June, 1999;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507122518/https://www.cypress.com/file/93831/download>
[^qtp-097461]: Cypress Semiconductor, Product Qualification Report QTP 97461: *3.3V, Light Device 16-Bit FCT Family*, April, 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210517162807/https://www.cypress.com/file/93881/download>
[^qtp-097476]: Cypress Semiconductor, Product Qualification Report QTP 97476: *256K STATIC RAM "CY7C194/CY7195/CY7C199" R28 PROCESS, FAB 2 QUALIFICATION*, August 2016.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97476-256k-static-ram-r28-process-fab-2-qualification-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7150d8bb1af5>
[^qtp-097506]: Cypress Semiconductor, Product Qualification Report QTP 97506: *1 Meg SRAM, R42 Technology, Fab 4 Qualification*, May, 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211207083723/https://www.cypress.com/file/93896/download>
[^qtp-097517]: Cypress Semiconductor, Product Qualification Report QTP 97517: *1/2 Meg SRAM, R42D Technology, Fab 4 Qualification*, August, 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210506115548/https://www.cypress.com/file/93496/download>
[^qtp-098021]: Cypress Semiconductor, Product Qualification Report QTP 98021: *1 Meg SRAM (5% Shrink), R32D Technology, Fab 4 -- Military Devices*, July 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507141403/https://www.cypress.com/file/93501/download>
[^qtp-098081]: Cypress Semiconductor, Product Qualification Report QTP 98081: *Synchronous 3.3V Cache RAM, R42D Technology w/ Hot Al, Fab 4 Qualification*, August, 1999;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211206081930/https://www.cypress.com/file/93926/download>
[^qtp-098086]: Cypress Semiconductor, Product Qualification Report QTP 98086: *4 Meg SRAM, R42HD Technology, Hot Aluminum*, January, 1999;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025143415/https://www.cypress.com/file/93936/download>
[^qtp-098111]: Cypress Semiconductor, Product Qualification Report QTP 98111: *4 Meg SRAM, R42H Technology, Hot Aluminum*, June, 1999;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210418214054/https://www.cypress.com/file/93956/download>
[^qtp-098115]: Cypress Semiconductor, Product Qualification Report QTP 98115: *1 Meg SRAM, R42HD Technology (5V operation)*, July, 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211130182828/https://www.cypress.com/file/93971/download>
[^qtp-098236]: Cypress Semiconductor, Product Qualification Report QTP 98236: *256K x 1 Static RAM, R28 Process, Fab 2 Qualification*, August 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507140402/https://www.cypress.com/file/94031/download>
[^qtp-098252]: Cypress Semiconductor, Product Qualification Report QTP 98252: *CY7C188 32K x 9 Static RAM – R28 Technology – Fab2*, November 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20200810004607/https://www.cypress.com/file/94051/download>
[^qtp-098296]: Cypress Semiconductor, Product Qualification Report QTP 98296: *64K Static RAM – R28 Technology – Fab 2*, September, 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210519014520/https://www.cypress.com/file/94056/download>
[^qtp-098313]: Cypress Semiconductor, Product Qualification Report QTP 98313: *2 Meg SRAM, R42HD Technology (5V operation)*, September, 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205094935/https://www.cypress.com/file/94066/download>
[^qtp-098333]: Cypress Semiconductor, Product Qualification Report QTP 98333: *100-MHz Spread Spectrum Clock Synthesizer/Driver, USB, Hublink and SDRAM Support (CY2287PVC), Fab2, L28 Technology*, August 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205131229/https://www.cypress.com/file/94086/download>
[^qtp-098357]: Cypress Semiconductor, Product Qualification Report QTP 98357: *4 Meg SRAM With NoBL Architecture, R42D Technology, Hot Aluminum*, May, 1999;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205080246/https://www.cypress.com/file/94096/download>
[^qtp-098368]: Cypress Semiconductor, Product Qualification Report QTP 98368: *SYNCHRONOUS/ASYNCHRONOUS DUAL PORT SRAM (3.3V AND 5V), R42HD TECHNOLOGY, FAB 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-98368-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152cc652012>
[^qtp-098393]: Cypress Semiconductor, Product Qualification Report QTP 98393: *Dual Port SRAM - R28 Technology - Fab 2*, March 1999.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-98393-productqualificationreport-en.pdf>
[^qtp-098437]: Cypress Semiconductor, Product Qualification Report QTP 98437: *1 Meg SRAM, R42HD Technology, Fab 4 Qualification*, November, 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507202024/https://www.cypress.com/file/94121/download>
[^qtp-099034]: Cypress Semiconductor, Product Qualification Report QTP 99034: *5V, 8/10 Bit FCT-T, L28EPD Technology, Fab 2*, March 1999;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507224233/https://www.cypress.com/file/94156/download>
[^qtp-099083]: Cypress Semiconductor, Product Qualification Report QTP 99083: *Low Voltage Synchronous FIFO – R28 Technology – Fab2*, March 1999;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201031174241/https://www.cypress.com/file/94181/download>
[^qtp-099092]: Cypress Semiconductor, Product Qualification Report QTP 99092: *Universal Serial Bus Microcontroller - P26 Technology in Fab 2*, August 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201202161536/https://www.cypress.com/file/94191/download>
[^qtp-099175]: Cypress Semiconductor, Product Qualification Report QTP 99175: *Military Clocked FIFOs – R28 Technology – Fab2*, October 1999;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025130802/https://www.cypress.com/file/94216/download>
[^qtp-099202]: Cypress Semiconductor, Product Qualification Report QTP 99202: *Low Voltage Synchronous/Asynchronous RAM, R52D-3 Technology at Fab 4*, May 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-99202-low-voltage-synchronous-asynchronous-ram-r52d-3-technology-at-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71491c270982>
[^qtp-099285]: Cypress Semiconductor, Product Qualification Report QTP 99285: *L28-TSMC Technology in TSMC-2A, Taiwan*, November 2008;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201101022945/https://www.cypress.com/file/94251/download>
[^qtp-099325]: Cypress Semiconductor, Product Qualification Report QTP 99325: *5V Synchronous FIFOs, R42HDHA Technology, Fab 4*, January, 2000;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507133537/https://www.cypress.com/file/94266/download>
[^qtp-099503]: Cypress Semiconductor, Product Qualification Report QTP 99503: *4 Meg Synchronous Cache RAM, R52D-3 Technology at Fab 4*, December, 2002;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210422145212/https://www.cypress.com/file/94336/download>
[^qtp-102101]: Cypress Semiconductor, Product Qualification Report QTP 102101: *Synchronous/Asynchronous Dual Port SRAM (3.3V and 5V), R42HD Technology, Fab 4 Qualification*, July 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-102101-synchronous-asynchronous-dual-port-sram-3.3v-and-5v-r42hd-technology-fab-4-qualification-productqualificationreport-en.pdf>
[^qtp-110605]: Cypress Semiconductor, Product Qualification Report QTP 110605: *Zero Delay Buffer, L28 Technology, TSMC-2A*, March 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-110605-zero-delay-buffer-l28-technology-tsmc-2a-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714b37f41005>
[^qtp-113005]: Cypress Semiconductor, Product Qualification Report QTP 113005: *64K Serial Non-Volatile SRAM Product Family, S8 Technology, CMI (Fab 4)*, January 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^qtp-151005]: Cypress Semiconductor, Product Qualification Report QTP 151005: *PSoC RADON Device Family, S4AD-5 Technology, HHGrace FAB5*, October 2015.
    <https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-151005-psoc24x94-hhgrace-productqualificationreport-en.pdf>
[^qtp-g990003]: Cypress Semiconductor, Product Qualification Report QTP G990003: *WaferTech 0.35um*, May, 2001;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20200810011117/https://www.cypress.com/file/94381/download>
[^qtp-i000005]: Cypress Semiconductor, Product Qualification Report QTP I000005: *0.35um Technology, CSM Fab 2*, October 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-i000005-0.35um-technology-csm-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152d1a52016>
