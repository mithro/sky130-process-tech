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

### 0.65 µm

| Code | Fab as printed | Metal layers | Gate oxide | Report |
|---|---|---|---|---|
| L28 | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 145 A | QTP 011503[^qtp-011503] |
| L28 | TSMC-2A, Taiwan | 2 | SiO2 / 125 Å | QTP 080608[^qtp-080608] |
| L28 | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 145 A | QTP 98333[^qtp-098333] |
| L28 | TSMC-2A, Taiwan | 2 | SiO2 / 125 Å | QTP 110605[^qtp-110605] |
| L28EPD | Cypress Semiconductor – Round Rock, Texas | 2 | SiO2 / 145 Å | QTP 99034[^qtp-099034] |
| P26 | Cypress Semiconductor - Round Rock, TX (Fab2) | 2 | SiO2 / 165A | QTP 96411[^qtp-096411] |
| R28 | Cypress Semiconductor, Bloomington, MN | 2 | SiO2 / 165 A | QTP 96091[^qtp-096091] |
| R28 | Cypress Semiconductor, Bloomington, MN | 2 | SiO2 / 165 A | QTP 96182[^qtp-096182] |
| R28 | Cypress Semiconductor -- Round Rock, TX | 2 | SiO2 / 165 Å | QTP 97476[^qtp-097476] |
| R28 | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 165 Å | QTP 98393[^qtp-098393] |

### 0.5 µm

| Code | Fab as printed | Metal layers | Gate oxide | Report |
|---|---|---|---|---|
| 0.5um TLM | Hyundai / Cheong Ju, Korea | 3 | SiO2 / 95 A | QTP 001004[^qtp-001004] |
| R32 | Cypress Semiconductor - Bloomington, MN | 1 | SiO2 / 145Å | QTP 97132[^qtp-097132] |
| R32D | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 145Å | QTP 98021[^qtp-098021] |
| S4AD-5 | Cypress Semiconductor -- CTI Round Rock, TX | 2 | SiO2 / 110Å | QTP 021507[^qtp-021507] |

### 0.42 µm and 0.35 µm

| Code | Fab as printed | Metal layers | Gate oxide | Report |
|---|---|---|---|---|
| CSM 0.35um | Chartered Semiconductor Singapore | 3 | SiO2 / 65Å | QTP I000005[^qtp-i000005] |
| R42HD | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 110Å | QTP 98368[^qtp-098368] |
| R42HD | Fab 4 / CMI - Bloomington, MN | 2 | SiO2 / 110Å | QTP 102101[^qtp-102101] |
| R42LDHA | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 70Å | QTP 003907[^qtp-003907] |
| RAM42HHA | Cypress Semiconductor -- Bloomington, MN | 1 | SiO2 /110A | QTP 030206[^qtp-030206] |
| RAM42HNHA | Grace Semiconductor, Shanghai, China | 1 | SiO2 /110A | QTP 091302[^qtp-091302] |
| S4AD-5 | GSMC/Shanghai-China | 2 | SiO2 / 110A | QTP 062509[^qtp-062509] |
| S4AD-5 | HHGrace /Shanghai-China | 2 | SiO2 / 110A | QTP 151005[^qtp-151005] |
| S4AD-5CTI | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 110A | QTP 051005[^qtp-051005] |
| S4ADLatch | Cypress Semiconductor - Round Rock, TX | 2 | SiO2 / 7A | QTP 042806[^qtp-042806] |

### 0.25 µm

| Code | Fab as printed | Metal layers | Gate oxide | Report |
|---|---|---|---|---|
| B53D-3RF | Cypress Minnesota, Fab4 | 2 | SiO2 / 55Å | QTP 032005[^qtp-032005] |
| R52D-3 | Cypress Semiconductor - Bloomington, MN | 2 | SiO2 / 50 Å | QTP 99202[^qtp-099202] |
| R52FFD-3 | Cypress Semiconductor – Bloomington, MN | 2 | SiO2 55Å | QTP 012705[^qtp-012705] |
| R52LD-3 | Cypress Semiconductor – Bloomington Minnesota | 2 | 55Å | QTP 062201[^qtp-062201] |
| R52T-3 | Cypress Semiconductor - Bloomington, MN | 3 | SiO2, 55Å | QTP 082506[^qtp-082506] |

### 0.21 µm to 0.15 µm

| Code | Fab as printed | Metal layers | Gate oxide | Report |
|---|---|---|---|---|
| B55SGT | Cypress Semiconductor – Bloomington, MN (CMI) | 3 | SiO2, 45Å | QTP 051101[^qtp-051101] |
| PowerChip 0.165um | Powerchip Semiconductor Corp, HsinChu, Taiwan | 2 | SiO2 / 72A | QTP 051501[^qtp-051501] |
| R7FD | Cypress Semiconductor -- Bloomington, MN | 2 | SiO2, 32Å | QTP 011908[^qtp-011908] |
| R7FT-3R | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2, 32Å | QTP 014807[^qtp-014807] |
| R7FTW-3R | Cypress Semiconductor -- Bloomington Minnesota | 3 | SiO2 32Å | QTP 023101[^qtp-023101] |
| R7LD-1.8 | Cypress Semiconductor -- Bloomington, MN | 2 | SiO2, 32Å | QTP 012801[^qtp-012801] |
| S17 | Promos (Taiwan) | 2 | SiO2, 62Å | QTP 032301[^qtp-032301] |

### 0.13 µm

| Code | Fab as printed | Metal layers | Gate oxide | Report |
|---|---|---|---|---|
| C8Q-3R | CMI/Bloomington MN | 4 | SiO2 DGOX 32/55A | QTP 043004[^qtp-043004] |
| L8C-3R | CMI / Bloomington MN | 4 | SiO2 DGOX 32/55A | QTP 053301[^qtp-053301] |
| RAM8NLD-1.8 | Cypress Semiconductor -- Bloomington, MN | 2 | 26Å | QTP 024110[^qtp-024110] |
| S8 | Cypress Semiconductor -- Bloomington, MN | 3 | SiO2 /110A & SiO2/32A | QTP 113005[^qtp-113005] |

### 90 nm

| Code | Fab as printed | Metal layers | Gate oxide | Report |
|---|---|---|---|---|
| C9FD-3R | Cypress Semiconductor -- Bloomington, MN | 2 | 23Å | QTP 063807[^qtp-063807] |
| R95LD-3R | Cypress Semiconductor -- Bloomington, MN | 2 | 28Å | QTP 061806[^qtp-061806] |
| R95LD-3R | Cypress Semiconductor -- Bloomington, MN | 2 | 28Å | QTP 072002[^qtp-072002] |
| R9Q-3R | Cypress Semiconductor - Bloomington, MN | 4 | Nitridized SiO2, 22Å | QTP 051207[^qtp-051207] |
| R9T-3R | Cypress Semiconductor -- Bloomington, MN | 3 | Nitridized SiO2, Thin GOX 22A, Thick GOx | QTP 032003[^qtp-032003] |

## Film by film

Each table gives one report's metal layers and passivation, with its design rule and the earliest dated row of its qualification history.

### QTP 011503: Fab2/L28

*Spread Spectrum Timing Solution for Serverworks Chipset, L28 Technology, Fab 2.* Design rule: CMOS, Single Poly, Double Metal /0.65 µm. Earliest dated history row: Apr 98 (QTP 97403).[^qtp-011503]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/1,200A TiW/6,000A Al/1,200A TiW | 0.890 µm |
| Metal 2 | 1,500A TiW/10,000A Al/150A Ti | 1.165 µm |
| Passivation | 3,000A TEOS + 15,000A Si2N4 | — |

### QTP 080608: TSMC-2A/L28 TSMC

*High Accuracy EPROM Programmable Device Family, L28 Technology, TSMC-2A.* Design rule: CMOS, Single Poly, Double Metal/0.65um. Earliest dated history row: May 2003 (QTP 99285).[^qtp-080608]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 400Å Ti / 1,000Å TiN/ 4,700Å AlSiCu/ 375Å TiN | 0.648 µm |
| Metal 2 | 1,500 Å Ti / 8,000Å AlSiCu / 375Å TiN | 0.988 µm |
| Passivation | 3,000Å SiN / 3,150Å SOG, 1,200Å SiN | — |

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

### QTP 96411: Fab 2/ P26

*256K/512K PROM - P26 Technology.* Design rule: CMOS, Double Metal / 0.65µm. Earliest dated history row: no history table.[^qtp-096411]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 6K Al, 1200A TiW | 0.720 µm |
| Metal 2 | 1,500A TiW, 9K Al, 320A TiW | 1.082 µm |
| Passivation | Oxynitride | — |

### QTP 97476: Fab2/R28

*256K STATIC RAM "CY7C194/CY7195/CY7C199" R28 PROCESS, FAB 2 QUALIFICATION.* Design rule: CMOS, Double Poly, Double Metal /0.65 m. Earliest dated history row: Nov. 1997 (QTP 97476).[^qtp-097476]

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

### QTP 97132: Fab4/R32

*32K x 8 Low Power SRAM, R32 Technology, Fab4.* Design rule: CMOS, Double Poly, Single Metal /0.5 µm. Earliest dated history row: Jun 03 (QTP 97132).[^qtp-097132]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | TiW/Al, 500Å/8,000Å | 0.850 µm |
| Passivation | Silicon Dioxide 7,000Å + Silicon Nitride 6,000Å | — |

### QTP 98021: Fab4/R32D

*1 Meg SRAM (5% Shrink), R32D Technology, Fab 4 -- Military Devices.* Design rule: CMOS, Single Local Interconnect, Double Metal /0.5 µm. Earliest dated history row: no history table.[^qtp-098021]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | Al-Cu/TiW | — |
| Metal 2 | TiW/Al-Cu/TiW | — |
| Passivation | Silicon Dioxide 7,000Å + Silicon Nitride 6,000Å | — |

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

### QTP 98368: Fab4/R42HD

*SYNCHRONOUS/ASYNCHRONOUS DUAL PORT SRAM (3.3V AND 5V), R42HD TECHNOLOGY, FAB 4.* Design rule: CMOS, Double Metal /0.42 m. Earliest dated history row: the history table gives no dates.[^qtp-098368]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6000Å Al -5%Cu/1200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW/8000Å Al -5%Cu/300Å TiW | 0.880 µm |
| Passivation | 7000Å SiO2 + 6000Å Si3N4 | — |

### QTP 102101: R42HD

*Synchronous/Asynchronous Dual Port SRAM (3.3V and 5V), R42HD Technology, Fab 4 Qualification.* Design rule: CMOS, Double Metal /0.42 µm. Earliest dated history row: Nov 97 (QTP 98064).[^qtp-102101]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6000Å Al -5%Cu/1200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW/8000Å Al -5%Cu/300Å TiW | 0.880 µm |
| Passivation | 7000Å SiO2 + 6000Å Si3N4 | — |

### QTP 003907: Fab4/R42D (with Hot AL)

*High Frequency Programmable PECL Clock Generator R42LDHA Technology, Fab 4.* Design rule: CMOS, Double Metal /0.35 m. Earliest dated history row: Sep 98 (QTP 98357).[^qtp-003907]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6000Å Al -5%Cu/1200Å TiW | 0.770 µm |
| Metal 2 | 500Å TiW/8000Å Al -5%Cu/300Å TiW | 0.880 µm |
| Passivation | 3,000Å SiO2 + 6000Å Si3N4 | — |

### QTP 042806: Fab2, S4AD-5

*S4ADLATCH Technology, Fab 2.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Apr 01 (QTP 010702).[^qtp-042806]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/6,000A Al 0.5% Cu /1,200A TiW | 0.770 µm |
| Metal 2 | 500A Ti/8,000A Al 0.5% Cu/300A TiW | 0.880 µm |
| Passivation | 3,000A TeOs / 6,000A Si3N4 | — |

### QTP 051005: Fab2, S4AD-5CTI SONOS

*Automotive PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2.* Design rule: Single Poly, Double Metal, 0.35 um. Earliest dated history row: Nov 04 (QTP 042702).[^qtp-051005]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500A Ti/6000A Al 0.5% Cu /1200A TiW | 0.770 µm |
| Metal 2 | 500A Ti/8000A Al 0.5% Cu/300A TiW | 0.880 µm |
| Passivation | 3,000A TeOs / 6000A Si3N4 | — |

### QTP 062509: S4AD-5 GSMC SONOS

*Neutron Device Family, S4AD-5 Technology, GSMC.* Design rule: Single Poly, Double Metal, 0.35 µm. Earliest dated history row: Aug 06 (QTP 060605).[^qtp-062509]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 250A TiN/5,800A Al/700A TiN | 0.675 µm |
| Metal 2 | 500A TiN/8,000A Al/250A TiN | 0.875 µm |
| Passivation | 7,000A TeOs /6,000A Si3N4 | — |

### QTP 151005: S4AD-5

*PSoC RADON Device Family, S4AD-5 Technology, HHGrace FAB5.* Design rule: Single Poly, Double Metal, 0.35 µm (the report prints µ with a non-standard font glyph). Earliest dated history row: Aug 06 (QTP 060605).[^qtp-151005]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 250A TiN/5,800A Al/700A TiN | 0.675 µm |
| Metal 2 | 500A TiN/8,000A Al/250A TiN | 0.875 µm |
| Passivation | 7,000A TeOs /6,000A Si3N4 | — |

### QTP I000005: 2L313-698-CBB/CRA

*0.35um Technology, CSM Fab 2.* Design rule: CMOS, Triple Metal /0.35 µm. Earliest dated history row: 2000 (QTP I000005).[^qtp-i000005]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100Å IMPTi/300Å TiN/.5KAlCu/350Å Tin ARC | 0.125 µm |
| Metal 2 | 100Å IMPTi/300Å TiN/.5KAlCu/350Å Tin ARC | 0.125 µm |
| Metal 3 | 300Å IMPTi /300Å TiN/.8K AlCu/350Å TiN ARC | 0.175 µm |
| Passivation | 350Å TiN/2K PSG/7K Si3N4 | — |

### QTP 012705: Fab4/R52FFD-3

*1MEG SRAM Fast Asynchronous Family, R52FFD-3 Technology, Fab 4.* Design rule: CMOS, Double Metal, 0.25 m (the µ is not printed in the report). Earliest dated history row: Oct 00 (QTP 000505).[^qtp-012705]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500Å TiW/6,000Å Al-0.5%Cu/300Å TiW | 0.680 µm |
| Metal 2 | 300Å Ti/8,000Å Al-0.5%Cu/300Å TiW | 0.860 µm |
| Passivation | 1,000Å Oxide / 9,000 Å Nitride | — |

### QTP 032005: Fab4 / B53D-3

*WirelessUSB Device Family, B53D-3RF Technology, Fab 4.* Design rule: CMOS, 0.25 µm. Earliest dated history row: Aug 00 (QTP 99256).[^qtp-032005]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500/6000/300 [Å] | — |
| Metal 2 | 500/6000/300 [Å] | — |
| Passivation | 1,000A TEOS + 9,000A Si2N4 | — |

### QTP 062201: 7C02638A

*MoBL ADM Dual Port Static RAM Family, R52LD-3 Technology, Fab4.* Design rule: R52 TDR (01-30065), 0.25um Technology. Earliest dated history row: Apr 99 (QTP 99075).[^qtp-062201]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 500 Å-TiW/6000 Å Al-Cu/500 Å TiW | 0.700 µm |
| Metal 2 | 300 Å-Ti/8000 Å Al-Cu/300 Å TiW | 0.860 µm |
| Passivation | 1,000A TEOS + 9,000A SiN | — |

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

### QTP 051101: Fab 4/ B55SGT

*FastEdge Series, B55SGT Technology, Fab 4.* Design rule: CMOS (0.21 – 0.35 µm), SiGe Bipolar. Earliest dated history row: May 03 (QTP 015104).[^qtp-051101]

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
| Metal 1 | TiN/Ti (18/8.5nm) | — |
| Metal 2 | TiN/Alcu/TiN (23/800/28nm) | — |
| Passivation | Si3N4 & Polyimide | — |

### QTP 011908: Fab4/R7FD-3R

*Fast Asynchronous SRAM Technology Derivative R7FD, Fab 4 Qualification.* Design rule: CMOS, Double Metal /0.15 um. Earliest dated history row: Dec 01 (QTP 011305).[^qtp-011908]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti / 4,200Å Al / 300Å TiW | 0.465 µm |
| Metal 2 | 300Å Ti /8,000 Å Al / 300Å TiW | 0.860 µm |
| Passivation | 1000Å TEOS / 9000Å PECVD Nitride | — |

### QTP 024110: Fab4/RAM8NLD-1.8V

*1 MEG (3.0V) MOBL DEVICES RAM8NLD-1.8V TECHNOLOGY, FAB4.* Design rule: 0.13 m. Earliest dated history row: Mar 03 (QTP 031102).[^qtp-024110]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150 Å Ti / 300 Å Al / 300 Å Cu | 0.075 µm (implausibly thin; probably misprinted) |
| Metal 2 | 300 Å Ti / 8000 Å Al | 0.830 µm |
| Passivation | 1000Å TEOS / 9000Å Si3N4 | — |

### QTP 043004: Fab4, C8Q-3R

*DDR2-PLL Device Family, C8Q-3R, Fab 4.* Design rule: CMOS, 0.13 µm. Earliest dated history row: Jan 05 (QTP 042106).[^qtp-043004]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100A Ti/3,200A Al 0.5% Cu /300A TiW | 0.360 µm |
| Metal 2 | 150A Ti/4,230A Al 0.5% Cu/300A TiW | 0.468 µm |
| Metal 3 | 150A Ti/4,230A Al 0.5% Cu/300A TiW | 0.468 µm |
| Metal 4 | 150A Ti/8,000A Al 0.5% Cu/300A TiW | 0.845 µm |
| Passivation | 1,000A TEOs / 9,000A Si3N4 | — |

### QTP 053301: Fab4, L8C-3R

*L8C-3R Technology, Fab 4.* Design rule: CMOS, 0.13 µm. Earliest dated history row: Jan 05 (QTP 042106).[^qtp-053301]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100A Ti/3,200A Al 0.5% Cu /300A TiW | 0.360 µm |
| Metal 2 | 150A Ti/4,230A Al 0.5% Cu/300A TiW | 0.468 µm |
| Metal 3 | 150A Ti/4,230A Al 0.5% Cu/300A TiW | 0.468 µm |
| Metal 4 | 150A Ti/8,000A Al 0.5% Cu/300A TiW | 0.845 µm |
| Passivation | 1,000A TeOs / 9,000A Si3N4 | — |

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

### QTP 051207: Fab4/R9Q-3R

*18 MEG QDR SYNCHRONOUS SRAM FAMILY, R9Q-3R TECHNOLOGY, FAB4.* Design rule: CMOS, Triple Metal, 90 nm. Earliest dated history row: Sep 04 (QTP 033302).[^qtp-051207]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 150Å Ti /3200Å Al / 300Å TiW | 0.365 µm |
| Metal 2 | 150Å Ti /6000 Å Al / 300Å TiW | 0.645 µm |
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

### QTP 072002: Fab4/R95LD-3R

*2 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4.* Design rule: CMOS, Double Metal, 0.09μm. Earliest dated history row: Mar 07 (QTP 071103).[^qtp-072002]

| Layer | Films as printed | Layer total (our arithmetic) |
|---|---|---|
| Metal 1 | 100Å Ti / 3200Å Al / 300Å TiW | 0.360 µm |
| Metal 2 | 150Å Ti / 8000Å Al / 300Å TiW | 0.845 µm |
| Passivation | 1000Å Oxide TEOS / 9000Å Nitride | — |

## References

### Cross-check

* {ref}`history-fabs` — which fab ran each process, from annual reports and the press.

### Deep dive

* [Cypress, QTP 001004](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-001004-productqualificationreport-en.pdf>) — 0.5um TLM Technology, Fab HME, Dual Port SRAM with PCI Bus Controller.[^qtp-001004]
* [Cypress, QTP 003907](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-003907-high-frequency-programmable-pecl-clock-generator-r42ldha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714957940a14>) — High Frequency Programmable PECL Clock Generator R42LDHA Technology, Fab 4.[^qtp-003907]
* [Cypress, QTP 011503](<https://web.archive.org/web/20201205124212/https://www.cypress.com/file/91641/download>) — Spread Spectrum Timing Solution for Serverworks Chipset, L28 Technology, Fab 2.[^qtp-011503]
* [Cypress, QTP 011908](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-011908-fast-asynchronous-sram-technology-derivative-r7fd-fab-4-qualification-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7150e6271aff>) — Fast Asynchronous SRAM Technology Derivative R7FD, Fab 4 Qualification.[^qtp-011908]
* [Cypress, QTP 012705](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-012705-1meg-sram-fast-asynchronous-family-r52ffd-3-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148db7c0893>) — 1MEG SRAM Fast Asynchronous Family, R52FFD-3 Technology, Fab 4.[^qtp-012705]
* [Cypress, QTP 012801](<https://web.archive.org/web/20210302225236/https://www.cypress.com/file/91706/download>) — 4 Meg SRAM Device R7LD-1.8 Technology, Fab4.[^qtp-012801]
* [Cypress, QTP 014807](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>) — Technology Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM CY7C085xV / CY7C083xV.[^qtp-014807]
* [Cypress, QTP 021507](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>) — Failsafe Device Family & Options S4AD-5 SONOS Technology, Fab 2.[^qtp-021507]
* [Cypress, QTP 023101](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-023101-rev2.0-sync-dual-port-family-productqualificationreport-en.pdf>) — Synchronous Dual Port RAM Family CY7C083xV / CY7C085xV, R7FTW-3R Technology Fab4.[^qtp-023101]
* [Cypress, QTP 024110](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-024110-1-meg-3.0v-mobl-devices-ram8nld-1.8v-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152a1d61fde>) — 1 MEG (3.0V) MOBL DEVICES RAM8NLD-1.8V TECHNOLOGY, FAB4.[^qtp-024110]
* [Cypress, QTP 030206](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030206-256k-static-ram-automotive-devices-ram42hha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71491e3d0986>) — 256K Static RAM Automotive Devices, RAM42HHA Technology, Fab 4.[^qtp-030206]
* [Cypress, QTP 032003](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-032003-36-meg-synchronous-sram-family-technology-r9t-3r-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714983cb0ac5>) — 36 Meg Synchronous SRAM Family, Technology R9T-3R, Fab4.[^qtp-032003]
* [Cypress, QTP 032005](<https://web.archive.org/web/20211206184334/https://www.cypress.com/file/92296/download>) — WirelessUSB Device Family, B53D-3RF Technology, Fab 4.[^qtp-032005]
* [Cypress, QTP 032301](<https://web.archive.org/web/20201204235131/https://www.cypress.com/file/92311/download>) — 16 MEG A/D MUX SRAM, S17 Technology, Promos Fab in Taiwan.[^qtp-032301]
* [Cypress, QTP 042806](<https://web.archive.org/web/20211025144943/https://www.cypress.com/file/92521/download>) — S4ADLATCH Technology, Fab 2.[^qtp-042806]
* [Cypress, QTP 043004](<https://web.archive.org/web/20201205122906/https://www.cypress.com/file/92151/download>) — DDR2-PLL Device Family, C8Q-3R, Fab 4.[^qtp-043004]
* [Cypress, QTP 051005](<https://web.archive.org/web/20211130190834/https://www.cypress.com/file/92671/download>) — Automotive PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2.[^qtp-051005]
* [Cypress, QTP 051101](<https://web.archive.org/web/20201028052046/https://www.cypress.com/file/92676/download>) — FastEdge Series, B55SGT Technology, Fab 4.[^qtp-051101]
* [Cypress, QTP 051207](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-051207-18-meg-qdr-synchronous-sram--cy7c1313d-product-family--r9q-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148e37b08a2>) — 18 MEG QDR SYNCHRONOUS SRAM FAMILY, R9Q-3R TECHNOLOGY, FAB4.[^qtp-051207]
* [Cypress, QTP 051501](<https://web.archive.org/web/20201028052812/https://www.cypress.com/file/92636/download>) — Cypress Minnesota (CMI) Sort Site Qualification -- 2 Meg, 3V PSRAM Device, PowerChip 0.165µm.[^qtp-051501]
* [Cypress, QTP 053301](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-053301-l8c-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149c4a70b8f>) — L8C-3R Technology, Fab 4.[^qtp-053301]
* [Cypress, QTP 061806](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-061806-4-meg-mobl-sram-automotive-devices-r95ld-3r-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714fdec718db>) — 4 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4.[^qtp-061806]
* [Cypress, QTP 062201](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-062201-mobl-adm-dual-port-static-ram-family-r52ld-3-technology-fab4-productqualificationreport-en.pdf>) — MoBL ADM Dual Port Static RAM Family, R52LD-3 Technology, Fab4.[^qtp-062201]
* [Cypress, QTP 062509](<https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-062509-psoc21x34-95xx-gsmc-productqualificationreport-en.pdf>) — Neutron Device Family, S4AD-5 Technology, GSMC.[^qtp-062509]
* [Cypress, QTP 063807](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-063807-1-meg-fast-asynchronous-sram-family-c9fd-3r-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149f5380c45>) — 1 Meg Fast Asynchronous SRAM Family, C9FD-3R Technology, Fab4.[^qtp-063807]
* [Cypress, QTP 072002](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-072002-2-meg-mobl-sram-cy62136-7fv30-r95ld-3rfab4-aec-q100-productqualificationreport-en.pdf>) — 2 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4.[^qtp-072002]
* [Cypress, QTP 080608](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-080608-high-accuracy-eprom-programmable-device-family-l28-technology-tsmc-2a-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714a27090cd2>) — High Accuracy EPROM Programmable Device Family, L28 Technology, TSMC-2A.[^qtp-080608]
* [Cypress, QTP 082506](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-082506-pci-e-clock-family-r52t-3-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714a4cbb0d39>) — PCI-E Clock Family, R52T-3 Technology, Fab 4.[^qtp-082506]
* [Cypress, QTP 091302](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-091302-mobl-asynchronous-sram-product-family-cy62256-ram42hnha-technology-fab5-gsmc-productqualificationreport-en.pdf?fileId=8ac78c8c93dda25b01953e8470a271d4>) — MoBL Asynchronous SRAM Product Family, RAM42HNHA Technology, Fab5 GSMC.[^qtp-091302]
* [Cypress, QTP 96091](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-96091-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148ab080847>) — Dual Port SRAM - R28 Technology, 6% Shrink.[^qtp-096091]
* [Cypress, QTP 96182](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-96182-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148acf9084a>) — Dual Port SRAM - R28 Technology.[^qtp-096182]
* [Cypress, QTP 96411](<https://web.archive.org/web/20201026124735/https://www.cypress.com/file/93566/download>) — 256K/512K PROM - P26 Technology.[^qtp-096411]
* [Cypress, QTP 97132](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97132-32k-x-8-low-power-sram-r32-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714947ff09f5>) — 32K x 8 Low Power SRAM, R32 Technology, Fab4.[^qtp-097132]
* [Cypress, QTP 97476](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97476-256k-static-ram-r28-process-fab-2-qualification-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7150d8bb1af5>) — 256K STATIC RAM "CY7C194/CY7195/CY7C199" R28 PROCESS, FAB 2 QUALIFICATION.[^qtp-097476]
* [Cypress, QTP 98021](<https://web.archive.org/web/20210507141403/https://www.cypress.com/file/93501/download>) — 1 Meg SRAM (5% Shrink), R32D Technology, Fab 4 -- Military Devices.[^qtp-098021]
* [Cypress, QTP 98333](<https://web.archive.org/web/20201205131229/https://www.cypress.com/file/94086/download>) — 100-MHz Spread Spectrum Clock Synthesizer/Driver, USB, Hublink and SDRAM Support (CY2287PVC), Fab2, L28 Technology.[^qtp-098333]
* [Cypress, QTP 98368](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-98368-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152cc652012>) — SYNCHRONOUS/ASYNCHRONOUS DUAL PORT SRAM (3.3V AND 5V), R42HD TECHNOLOGY, FAB 4.[^qtp-098368]
* [Cypress, QTP 98393](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-98393-productqualificationreport-en.pdf>) — Dual Port SRAM - R28 Technology - Fab 2.[^qtp-098393]
* [Cypress, QTP 99034](<https://web.archive.org/web/20210507224233/https://www.cypress.com/file/94156/download>) — 5V, 8/10 Bit FCT-T, L28EPD Technology, Fab 2.[^qtp-099034]
* [Cypress, QTP 99202](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-99202-low-voltage-synchronous-asynchronous-ram-r52d-3-technology-at-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71491c270982>) — Low Voltage Synchronous/Asynchronous RAM, R52D-3 Technology at Fab 4.[^qtp-099202]
* [Cypress, QTP 102101](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-102101-synchronous-asynchronous-dual-port-sram-3.3v-and-5v-r42hd-technology-fab-4-qualification-productqualificationreport-en.pdf>) — Synchronous/Asynchronous Dual Port SRAM (3.3V and 5V), R42HD Technology, Fab 4 Qualification.[^qtp-102101]
* [Cypress, QTP 110605](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-110605-zero-delay-buffer-l28-technology-tsmc-2a-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714b37f41005>) — Zero Delay Buffer, L28 Technology, TSMC-2A.[^qtp-110605]
* [Cypress, QTP 113005](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>) — 64K Serial Non-Volatile SRAM Product Family, S8 Technology, CMI (Fab 4).[^qtp-113005]
* [Cypress, QTP 151005](<https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-151005-psoc24x94-hhgrace-productqualificationreport-en.pdf>) — PSoC RADON Device Family, S4AD-5 Technology, HHGrace FAB5.[^qtp-151005]
* [Cypress, QTP I000005](<https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-i000005-0.35um-technology-csm-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152d1a52016>) — 0.35um Technology, CSM Fab 2.[^qtp-i000005]

<!-- footnotes -->

[^qtp-001004]: Cypress Semiconductor, Product Qualification Report QTP 001004: *0.5um TLM Technology, Fab HME, Dual Port SRAM with PCI Bus Controller*, January 2001.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-001004-productqualificationreport-en.pdf>
[^qtp-003907]: Cypress Semiconductor, Product Qualification Report QTP 003907: *High Frequency Programmable PECL Clock Generator R42LDHA Technology, Fab 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-003907-high-frequency-programmable-pecl-clock-generator-r42ldha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714957940a14>
[^qtp-011503]: Cypress Semiconductor, Product Qualification Report QTP 011503: *Spread Spectrum Timing Solution for Serverworks Chipset, L28 Technology, Fab 2*, December 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205124212/https://www.cypress.com/file/91641/download>
[^qtp-011908]: Cypress Semiconductor, Product Qualification Report QTP 011908: *Fast Asynchronous SRAM Technology Derivative R7FD, Fab 4 Qualification*, August 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-011908-fast-asynchronous-sram-technology-derivative-r7fd-fab-4-qualification-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7150e6271aff>
[^qtp-012705]: Cypress Semiconductor, Product Qualification Report QTP 012705: *1MEG SRAM Fast Asynchronous Family, R52FFD-3 Technology, Fab 4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-012705-1meg-sram-fast-asynchronous-family-r52ffd-3-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148db7c0893>
[^qtp-012801]: Cypress Semiconductor, Product Qualification Report QTP 012801: *4 Meg SRAM Device R7LD-1.8 Technology, Fab4*, October 2004;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210302225236/https://www.cypress.com/file/91706/download>
[^qtp-014807]: Cypress Semiconductor, Product Qualification Report QTP 014807: *Technology Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM CY7C085xV / CY7C083xV*, June 2005.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
[^qtp-021507]: Cypress Semiconductor, Product Qualification Report QTP 021507: *Failsafe Device Family & Options S4AD-5 SONOS Technology, Fab 2*, December 2015.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-021507-failsafe-device-family--options-s4ad-5-sonos-technology-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714961a70a2b>
[^qtp-023101]: Cypress Semiconductor, Product Qualification Report QTP 023101: *Synchronous Dual Port RAM Family CY7C083xV / CY7C085xV, R7FTW-3R Technology Fab4*, June 2005.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-023101-rev2.0-sync-dual-port-family-productqualificationreport-en.pdf>
[^qtp-024110]: Cypress Semiconductor, Product Qualification Report QTP 024110: *1 MEG (3.0V) MOBL DEVICES RAM8NLD-1.8V TECHNOLOGY, FAB4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-024110-1-meg-3.0v-mobl-devices-ram8nld-1.8v-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152a1d61fde>
[^qtp-030206]: Cypress Semiconductor, Product Qualification Report QTP 030206: *256K Static RAM Automotive Devices, RAM42HHA Technology, Fab 4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-030206-256k-static-ram-automotive-devices-ram42hha-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71491e3d0986>
[^qtp-032003]: Cypress Semiconductor, Product Qualification Report QTP 032003: *36 Meg Synchronous SRAM Family, Technology R9T-3R, Fab4*, August 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-032003-36-meg-synchronous-sram-family-technology-r9t-3r-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714983cb0ac5>
[^qtp-032005]: Cypress Semiconductor, Product Qualification Report QTP 032005: *WirelessUSB Device Family, B53D-3RF Technology, Fab 4*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211206184334/https://www.cypress.com/file/92296/download>
[^qtp-032301]: Cypress Semiconductor, Product Qualification Report QTP 032301: *16 MEG A/D MUX SRAM, S17 Technology, Promos Fab in Taiwan*, May 2004;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201204235131/https://www.cypress.com/file/92311/download>
[^qtp-042806]: Cypress Semiconductor, Product Qualification Report QTP 042806: *S4ADLATCH Technology, Fab 2*, January 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211025144943/https://www.cypress.com/file/92521/download>
[^qtp-043004]: Cypress Semiconductor, Product Qualification Report QTP 043004: *DDR2-PLL Device Family, C8Q-3R, Fab 4*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205122906/https://www.cypress.com/file/92151/download>
[^qtp-051005]: Cypress Semiconductor, Product Qualification Report QTP 051005: *Automotive PSoC Mixed Signal Array Family, S4AD-5CTI Technology, Fab 2*, March 2007;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20211130190834/https://www.cypress.com/file/92671/download>
[^qtp-051101]: Cypress Semiconductor, Product Qualification Report QTP 051101: *FastEdge Series, B55SGT Technology, Fab 4*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201028052046/https://www.cypress.com/file/92676/download>
[^qtp-051207]: Cypress Semiconductor, Product Qualification Report QTP 051207: *18 MEG QDR SYNCHRONOUS SRAM FAMILY, R9Q-3R TECHNOLOGY, FAB4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-051207-18-meg-qdr-synchronous-sram--cy7c1313d-product-family--r9q-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148e37b08a2>
[^qtp-051501]: Cypress Semiconductor, Product Qualification Report QTP 051501: *Cypress Minnesota (CMI) Sort Site Qualification -- 2 Meg, 3V PSRAM Device, PowerChip 0.165µm*, May 2005;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201028052812/https://www.cypress.com/file/92636/download>
[^qtp-053301]: Cypress Semiconductor, Product Qualification Report QTP 053301: *L8C-3R Technology, Fab 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-053301-l8c-3r-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149c4a70b8f>
[^qtp-061806]: Cypress Semiconductor, Product Qualification Report QTP 061806: *4 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4*, March 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-061806-4-meg-mobl-sram-automotive-devices-r95ld-3r-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714fdec718db>
[^qtp-062201]: Cypress Semiconductor, Product Qualification Report QTP 062201: *MoBL ADM Dual Port Static RAM Family, R52LD-3 Technology, Fab4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-062201-mobl-adm-dual-port-static-ram-family-r52ld-3-technology-fab4-productqualificationreport-en.pdf>
[^qtp-062509]: Cypress Semiconductor, Product Qualification Report QTP 062509: *Neutron Device Family, S4AD-5 Technology, GSMC*, July 2014.
    <https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-062509-psoc21x34-95xx-gsmc-productqualificationreport-en.pdf>
[^qtp-063807]: Cypress Semiconductor, Product Qualification Report QTP 063807: *1 Meg Fast Asynchronous SRAM Family, C9FD-3R Technology, Fab4*, Jan 2024.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-063807-1-meg-fast-asynchronous-sram-family-c9fd-3r-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7149f5380c45>
[^qtp-072002]: Cypress Semiconductor, Product Qualification Report QTP 072002: *2 Meg MoBL SRAM Automotive Devices, R95LD-3R, Fab 4*, March 2025 rev*B.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-072002-2-meg-mobl-sram-cy62136-7fv30-r95ld-3rfab4-aec-q100-productqualificationreport-en.pdf>
[^qtp-080608]: Cypress Semiconductor, Product Qualification Report QTP 080608: *High Accuracy EPROM Programmable Device Family, L28 Technology, TSMC-2A*, May 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-080608-high-accuracy-eprom-programmable-device-family-l28-technology-tsmc-2a-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714a27090cd2>
[^qtp-082506]: Cypress Semiconductor, Product Qualification Report QTP 082506: *PCI-E Clock Family, R52T-3 Technology, Fab 4*, September 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-082506-pci-e-clock-family-r52t-3-technology-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714a4cbb0d39>
[^qtp-091302]: Cypress Semiconductor, Product Qualification Report QTP 091302: *MoBL Asynchronous SRAM Product Family, RAM42HNHA Technology, Fab5 GSMC*, February 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-091302-mobl-asynchronous-sram-product-family-cy62256-ram42hnha-technology-fab5-gsmc-productqualificationreport-en.pdf?fileId=8ac78c8c93dda25b01953e8470a271d4>
[^qtp-096091]: Cypress Semiconductor, Product Qualification Report QTP 96091: *Dual Port SRAM - R28 Technology, 6% Shrink*, September 1996.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-96091-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148ab080847>
[^qtp-096182]: Cypress Semiconductor, Product Qualification Report QTP 96182: *Dual Port SRAM - R28 Technology*, September 1996.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-96182-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7148acf9084a>
[^qtp-096411]: Cypress Semiconductor, Product Qualification Report QTP 96411: *256K/512K PROM - P26 Technology*, May 1997;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201026124735/https://www.cypress.com/file/93566/download>
[^qtp-097132]: Cypress Semiconductor, Product Qualification Report QTP 97132: *32K x 8 Low Power SRAM, R32 Technology, Fab4*, June 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97132-32k-x-8-low-power-sram-r32-technology-fab4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714947ff09f5>
[^qtp-097476]: Cypress Semiconductor, Product Qualification Report QTP 97476: *256K STATIC RAM "CY7C194/CY7195/CY7C199" R28 PROCESS, FAB 2 QUALIFICATION*, August 2016.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-97476-256k-static-ram-r28-process-fab-2-qualification-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7150d8bb1af5>
[^qtp-098021]: Cypress Semiconductor, Product Qualification Report QTP 98021: *1 Meg SRAM (5% Shrink), R32D Technology, Fab 4 -- Military Devices*, July 1998;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507141403/https://www.cypress.com/file/93501/download>
[^qtp-098333]: Cypress Semiconductor, Product Qualification Report QTP 98333: *100-MHz Spread Spectrum Clock Synthesizer/Driver, USB, Hublink and SDRAM Support (CY2287PVC), Fab2, L28 Technology*, August 2003;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20201205131229/https://www.cypress.com/file/94086/download>
[^qtp-098368]: Cypress Semiconductor, Product Qualification Report QTP 98368: *SYNCHRONOUS/ASYNCHRONOUS DUAL PORT SRAM (3.3V AND 5V), R42HD TECHNOLOGY, FAB 4*, June 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-98368-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152cc652012>
[^qtp-098393]: Cypress Semiconductor, Product Qualification Report QTP 98393: *Dual Port SRAM - R28 Technology - Fab 2*, March 1999.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-98393-productqualificationreport-en.pdf>
[^qtp-099034]: Cypress Semiconductor, Product Qualification Report QTP 99034: *5V, 8/10 Bit FCT-T, L28EPD Technology, Fab 2*, March 1999;
    Wayback Machine copy of the cypress.com download.
    <https://web.archive.org/web/20210507224233/https://www.cypress.com/file/94156/download>
[^qtp-099202]: Cypress Semiconductor, Product Qualification Report QTP 99202: *Low Voltage Synchronous/Asynchronous RAM, R52D-3 Technology at Fab 4*, May 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-99202-low-voltage-synchronous-asynchronous-ram-r52d-3-technology-at-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71491c270982>
[^qtp-102101]: Cypress Semiconductor, Product Qualification Report QTP 102101: *Synchronous/Asynchronous Dual Port SRAM (3.3V and 5V), R42HD Technology, Fab 4 Qualification*, July 2014.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-102101-synchronous-asynchronous-dual-port-sram-3.3v-and-5v-r42hd-technology-fab-4-qualification-productqualificationreport-en.pdf>
[^qtp-110605]: Cypress Semiconductor, Product Qualification Report QTP 110605: *Zero Delay Buffer, L28 Technology, TSMC-2A*, March 2025.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-110605-zero-delay-buffer-l28-technology-tsmc-2a-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714b37f41005>
[^qtp-113005]: Cypress Semiconductor, Product Qualification Report QTP 113005: *64K Serial Non-Volatile SRAM Product Family, S8 Technology, CMI (Fab 4)*, January 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^qtp-151005]: Cypress Semiconductor, Product Qualification Report QTP 151005: *PSoC RADON Device Family, S4AD-5 Technology, HHGrace FAB5*, October 2015.
    <https://www.infineon.com/assets/row/public/documents/30/316/infineon-qtp-151005-psoc24x94-hhgrace-productqualificationreport-en.pdf>
[^qtp-i000005]: Cypress Semiconductor, Product Qualification Report QTP I000005: *0.35um Technology, CSM Fab 2*, October 2013.
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-i000005-0.35um-technology-csm-fab-2-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d7152d1a52016>
