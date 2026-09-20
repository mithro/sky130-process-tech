(steps-index)=
# Process steps

The SKY130 flow is documented here as 171 numbered steps, in the
order in which a wafer experiences them. Each step has its own page.
The step numbers and codes are those of the public
*S8 / SKY130 Process Steps* sheet, and the names follow its
descriptions,[^steps-sheet] lightly edited for 20 steps: typing slips
are corrected ("Low Vt NOMOS mask" becomes "Low Vt NMOS mask"),
abbreviations are spelt out, and step 82, which the sheet describes only
by its code "PSDI", is named "P+ source drain implant".

## Starting material, isolation and deep N-well

| Step | Code | Name | Category |
|---:|---|---|---|
| 1 | {ref}`SMAT <step-001>` | Starting material | {ref}`Substrate <category-substrate>` |
| 2 | {ref}`BOX <step-002>` | Base oxidation | {ref}`Oxidation <category-oxidation>` |
| 3 | {ref}`ISONIT <step-003>` | Iso nitride deposition | {ref}`Deposition <category-deposition>` |
| 4 | {ref}`FOM <step-004>` | Field oxide mask | {ref}`Litho <category-lithography>` |
| 5 | {ref}`STINITE <step-005>` | Shallow trench nitride etch | {ref}`Etch <category-etch>` |
| 6 | {ref}`STIE <step-006>` | Shallow trench etch | {ref}`Etch <category-etch>` |
| 7 | {ref}`DNM <step-007>` | Deep N-well mask | {ref}`Litho <category-lithography>` |
| 8 | {ref}`DNI <step-008>` | Deep N+ implant | {ref}`Implant <category-implant>` |
| 9 | {ref}`DNIS <step-009>` | High V deep N-well implant strip | {ref}`Strip/clean <category-strip>` |
| 10 | {ref}`LINOX <step-010>` | LINOX oxidation | {ref}`Oxidation <category-oxidation>` |
| 11 | {ref}`FILOX <step-011>` | Fill oxide deposition | {ref}`Deposition <category-deposition>` |
| 12 | {ref}`CMPNIT <step-012>` | CMP over nitride | {ref}`CMP <category-cmp>` |
| 13 | {ref}`NS19 <step-013>` | Nitride strip | {ref}`Strip/clean <category-strip>` |

| Step | Code | Machine class | Mask |
|---:|---|---|---|
| 1 | {ref}`SMAT <step-001>` | {ref}`Starting material <machine-starting-material>` | — |
| 2 | {ref}`BOX <step-002>` | {ref}`Vertical batch furnace <machine-vertical-furnace-oxidation>` | — |
| 3 | {ref}`ISONIT <step-003>` | {ref}`Vertical batch furnace <machine-vertical-furnace-lpcvd>` | — |
| 4 | {ref}`FOM <step-004>` | {ref}`DUV (KrF, 248 nm) stepper or scanner <machine-duv-krf-stepper>` | {ref}`FOM <mask-fom>` |
| 5 | {ref}`STINITE <step-005>` | {ref}`Plasma etcher: dielectric and nitride <machine-plasma-etcher-dielectric>` | {ref}`FOM <mask-fom>` |
| 6 | {ref}`STIE <step-006>` | {ref}`Plasma etcher: silicon and polysilicon <machine-plasma-etcher-silicon>` | {ref}`FOM <mask-fom>` |
| 7 | {ref}`DNM <step-007>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`DNM <mask-dnm>` |
| 8 | {ref}`DNI <step-008>` | {ref}`High-energy ion implanter <machine-high-energy-implanter>` | {ref}`DNM <mask-dnm>` |
| 9 | {ref}`DNIS <step-009>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`DNM <mask-dnm>` |
| 10 | {ref}`LINOX <step-010>` | {ref}`Vertical batch furnace <machine-vertical-furnace-oxidation>` | — |
| 11 | {ref}`FILOX <step-011>` | {ref}`HDP-CVD <machine-hdp-cvd>` | — |
| 12 | {ref}`CMPNIT <step-012>` | {ref}`CMP polisher <machine-cmp-polisher>` | — |
| 13 | {ref}`NS19 <step-013>` | {ref}`Wet bench and spray processor <machine-wet-bench>` | — |

## Wells and threshold implants

| Step | Code | Name | Category |
|---:|---|---|---|
| 14 | {ref}`LVTNM <step-014>` | Low Vt NMOS mask | {ref}`Litho <category-lithography>` |
| 15 | {ref}`LVTNI <step-015>` | Low Vt NMOS implantation | {ref}`Implant <category-implant>` |
| 16 | {ref}`LVTNIS <step-016>` | Low Vt NMOS implant strip | {ref}`Strip/clean <category-strip>` |
| 17 | {ref}`NWM <step-017>` | N-well mask | {ref}`Litho <category-lithography>` |
| 18 | {ref}`NWI <step-018>` | N-well implant | {ref}`Implant <category-implant>` |
| 19 | {ref}`NWI2 <step-019>` | NWI2 implant | {ref}`Implant <category-implant>` |
| 20 | {ref}`LVTPI <step-020>` | Low V P-channel implant | {ref}`Implant <category-implant>` |
| 21 | {ref}`LVTPIS <step-021>` | P-channel implant strip | {ref}`Strip/clean <category-strip>` |
| 22 | {ref}`HVTPM <step-022>` | High V P-channel implant mask | {ref}`Litho <category-lithography>` |
| 23 | {ref}`PCHI <step-023>` | P-channel implant | {ref}`Implant <category-implant>` |
| 24 | {ref}`PNCHI <step-024>` | P-channel BF2 implant | {ref}`Implant <category-implant>` |
| 25 | {ref}`PCHIS <step-025>` | P-channel BF2 implant strip | {ref}`Strip/clean <category-strip>` |
| 26 | {ref}`PWBM <step-026>` | P-well block mask | {ref}`Litho <category-lithography>` |
| 27 | {ref}`PWI <step-027>` | P-well implant | {ref}`Implant <category-implant>` |
| 28 | {ref}`PWI2 <step-028>` | PWI2 implant | {ref}`Implant <category-implant>` |
| 29 | {ref}`PWIS <step-029>` | P-well implant strip | {ref}`Strip/clean <category-strip>` |
| 30 | {ref}`PWDEM <step-030>` | P-well drain extended mask | {ref}`Litho <category-lithography>` |
| 31 | {ref}`PWDEI1 <step-031>` | PWDEI1 implant | {ref}`Implant <category-implant>` |
| 32 | {ref}`PWDEI2 <step-032>` | PWDEI2 implant | {ref}`Implant <category-implant>` |
| 33 | {ref}`PWDEIS <step-033>` | PWDEIS implant strip | {ref}`Strip/clean <category-strip>` |
| 34 | {ref}`RTAI <step-034>` | Pre-gate oxide anneal | {ref}`Anneal <category-anneal>` |

| Step | Code | Machine class | Mask |
|---:|---|---|---|
| 14 | {ref}`LVTNM <step-014>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`LVTNM <mask-lvtnm>` |
| 15 | {ref}`LVTNI <step-015>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`LVTNM <mask-lvtnm>` |
| 16 | {ref}`LVTNIS <step-016>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`LVTNM <mask-lvtnm>` |
| 17 | {ref}`NWM <step-017>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`NWM <mask-nwm>` |
| 18 | {ref}`NWI <step-018>` | {ref}`High-energy ion implanter <machine-high-energy-implanter>` | {ref}`NWM <mask-nwm>` |
| 19 | {ref}`NWI2 <step-019>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`NWM <mask-nwm>` |
| 20 | {ref}`LVTPI <step-020>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`NWM <mask-nwm>` |
| 21 | {ref}`LVTPIS <step-021>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`NWM <mask-nwm>` |
| 22 | {ref}`HVTPM <step-022>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`HVTPM <mask-hvtpm>` |
| 23 | {ref}`PCHI <step-023>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`HVTPM <mask-hvtpm>` |
| 24 | {ref}`PNCHI <step-024>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`HVTPM <mask-hvtpm>` |
| 25 | {ref}`PCHIS <step-025>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`HVTPM <mask-hvtpm>` |
| 26 | {ref}`PWBM <step-026>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`PWBM <mask-pwbm>` |
| 27 | {ref}`PWI <step-027>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`PWBM <mask-pwbm>` |
| 28 | {ref}`PWI2 <step-028>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`PWBM <mask-pwbm>` |
| 29 | {ref}`PWIS <step-029>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`PWBM <mask-pwbm>` |
| 30 | {ref}`PWDEM <step-030>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`PWDEM <mask-pwdem>` |
| 31 | {ref}`PWDEI1 <step-031>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`PWDEM <mask-pwdem>` |
| 32 | {ref}`PWDEI2 <step-032>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`PWDEM <mask-pwdem>` |
| 33 | {ref}`PWDEIS <step-033>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`PWDEM <mask-pwdem>` |
| 34 | {ref}`RTAI <step-034>` | {ref}`Rapid thermal processor <machine-rapid-thermal-processor>` | — |

## SONOS tunnel window and ONO stack

| Step | Code | Name | Category |
|---:|---|---|---|
| 35 | {ref}`TUNM <step-035>` | Tunnel mask | {ref}`Litho <category-lithography>` |
| 36 | {ref}`TUNARCE <step-036>` | Tunnel mask ARC etch | {ref}`Etch <category-etch>` |
| 37 | {ref}`PTSI <step-037>` | Punch-through stop implant | {ref}`Implant <category-implant>` |
| 38 | {ref}`DEPI <step-038>` | Depletion implant | {ref}`Implant <category-implant>` |
| 39 | {ref}`TUNME <step-039>` | Tunnel mask etch | {ref}`Etch <category-etch>` |
| 40 | {ref}`ONO <step-040>` | ONO stack oxidation | {ref}`Oxidation <category-oxidation>` |
| 41 | {ref}`ONOM <step-041>` | ONO mask | {ref}`Litho <category-lithography>` |
| 42 | {ref}`ONOME <step-042>` | ONO mask etch | {ref}`Etch <category-etch>` |

| Step | Code | Machine class | Mask |
|---:|---|---|---|
| 35 | {ref}`TUNM <step-035>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`TUNM <mask-tunm>` |
| 36 | {ref}`TUNARCE <step-036>` | {ref}`Plasma etcher: silicon and polysilicon <machine-plasma-etcher-silicon>` | {ref}`TUNM <mask-tunm>` |
| 37 | {ref}`PTSI <step-037>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`TUNM <mask-tunm>` |
| 38 | {ref}`DEPI <step-038>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`TUNM <mask-tunm>` |
| 39 | {ref}`TUNME <step-039>` | {ref}`Wet bench and spray processor <machine-wet-bench>` | {ref}`TUNM <mask-tunm>` |
| 40 | {ref}`ONO <step-040>` | {ref}`Vertical batch furnace <machine-vertical-furnace-oxidation>` | — |
| 41 | {ref}`ONOM <step-041>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`ONOM <mask-onom>` |
| 42 | {ref}`ONOME <step-042>` | {ref}`Plasma etcher: silicon and polysilicon <machine-plasma-etcher-silicon>` | {ref}`ONOM <mask-onom>` |

## Gate oxides

| Step | Code | Name | Category |
|---:|---|---|---|
| 43 | {ref}`GOX100 <step-043>` | Gate oxidation | {ref}`Oxidation <category-oxidation>` |
| 44 | {ref}`LVOM <step-044>` | Low voltage oxide mask | {ref}`Litho <category-lithography>` |
| 45 | {ref}`NCHI <step-045>` | N-channel implant | {ref}`Implant <category-implant>` |
| 46 | {ref}`GOXETCH <step-046>` | Low V gate oxide etch | {ref}`Etch <category-etch>` |
| 47 | {ref}`LVGOX <step-047>` | Gate oxidation | {ref}`Oxidation <category-oxidation>` |

| Step | Code | Machine class | Mask |
|---:|---|---|---|
| 43 | {ref}`GOX100 <step-043>` | {ref}`Vertical batch furnace <machine-vertical-furnace-oxidation>` | — |
| 44 | {ref}`LVOM <step-044>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`LVOM <mask-lvom>` |
| 45 | {ref}`NCHI <step-045>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`LVOM <mask-lvom>` |
| 46 | {ref}`GOXETCH <step-046>` | {ref}`Wet bench and spray processor <machine-wet-bench>` | {ref}`LVOM <mask-lvom>` |
| 47 | {ref}`LVGOX <step-047>` | {ref}`Vertical batch furnace <machine-vertical-furnace-oxidation>` | — |

## Poly gate and poly resistors

| Step | Code | Name | Category |
|---:|---|---|---|
| 48 | {ref}`SAGD <step-048>` | Single a-Si gate deposition | {ref}`Deposition <category-deposition>` |
| 49 | {ref}`RPM <step-049>` | Resistor protect mask | {ref}`Litho <category-lithography>` |
| 50 | {ref}`P1I <step-050>` | Poly1 implant | {ref}`Implant <category-implant>` |
| 51 | {ref}`P1IS <step-051>` | P1IS implant resist strip | {ref}`Strip/clean <category-strip>` |
| 52 | {ref}`RRPM <step-052>` | Rev resistor protect mask | {ref}`Litho <category-lithography>` |
| 53 | {ref}`PRI <step-053>` | PRI implant splits | {ref}`Implant <category-implant>` |
| 54 | {ref}`PRIS <step-054>` | PRI implant resist strip | {ref}`Strip/clean <category-strip>` |
| 55 | {ref}`URPM <step-055>` | Ultra-high resistor poly mask | {ref}`Litho <category-lithography>` |
| 56 | {ref}`UPRI <step-056>` | UPRI implant | {ref}`Implant <category-implant>` |
| 57 | {ref}`UPRIS <step-057>` | UPRIS implant resist strip | {ref}`Strip/clean <category-strip>` |
| 58 | {ref}`GATENIT <step-058>` | Gate poly nitride deposition | {ref}`Deposition <category-deposition>` |
| 59 | {ref}`POC <step-059>` | Protective oxide cap | {ref}`Deposition <category-deposition>` |
| 60 | {ref}`BFR <step-060>` | Backside film removal | {ref}`Etch <category-etch>` |
| 61 | {ref}`P1M <step-061>` | Poly mask | {ref}`Litho <category-lithography>` |
| 62 | {ref}`P1ME <step-062>` | Poly mask poly etch | {ref}`Etch <category-etch>` |
| 63 | {ref}`IOX45 <step-063>` | Implant oxidation | {ref}`Oxidation <category-oxidation>` |

| Step | Code | Machine class | Mask |
|---:|---|---|---|
| 48 | {ref}`SAGD <step-048>` | {ref}`Vertical batch furnace <machine-vertical-furnace-lpcvd>` | — |
| 49 | {ref}`RPM <step-049>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`RPM <mask-rpm>` |
| 50 | {ref}`P1I <step-050>` | {ref}`High-current ion implanter <machine-high-current-implanter>` | {ref}`RPM <mask-rpm>` |
| 51 | {ref}`P1IS <step-051>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`RPM <mask-rpm>` |
| 52 | {ref}`RRPM <step-052>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`RRPM <mask-rrpm>` |
| 53 | {ref}`PRI <step-053>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`RRPM <mask-rrpm>` |
| 54 | {ref}`PRIS <step-054>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`RRPM <mask-rrpm>` |
| 55 | {ref}`URPM <step-055>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`URPM <mask-urpm>` |
| 56 | {ref}`UPRI <step-056>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`URPM <mask-urpm>` |
| 57 | {ref}`UPRIS <step-057>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`URPM <mask-urpm>` |
| 58 | {ref}`GATENIT <step-058>` | {ref}`Vertical batch furnace <machine-vertical-furnace-lpcvd>` | — |
| 59 | {ref}`POC <step-059>` | {ref}`Vertical batch furnace <machine-vertical-furnace-lpcvd>` | — |
| 60 | {ref}`BFR <step-060>` | {ref}`Single-wafer spin processor <machine-single-wafer-spin-processor>` | — |
| 61 | {ref}`P1M <step-061>` | {ref}`DUV (KrF, 248 nm) stepper or scanner <machine-duv-krf-stepper>` | {ref}`P1M <mask-p1m>` |
| 62 | {ref}`P1ME <step-062>` | {ref}`Plasma etcher: silicon and polysilicon <machine-plasma-etcher-silicon>` | {ref}`P1M <mask-p1m>` |
| 63 | {ref}`IOX45 <step-063>` | {ref}`Vertical batch furnace <machine-vertical-furnace-oxidation>` | — |

## Tips and halos

| Step | Code | Name | Category |
|---:|---|---|---|
| 64 | {ref}`NTM <step-064>` | NTM mask (tip formation) | {ref}`Litho <category-lithography>` |
| 65 | {ref}`ASTI <step-065>` | As tip implant | {ref}`Implant <category-implant>` |
| 66 | {ref}`BHI <step-066>` | B halo implant | {ref}`Implant <category-implant>` |
| 67 | {ref}`ASTIS <step-067>` | As tip implant strip | {ref}`Strip/clean <category-strip>` |
| 68 | {ref}`HVNTM <step-068>` | HV N-tip mask formation | {ref}`Litho <category-lithography>` |
| 69 | {ref}`HVASTI <step-069>` | HV As N-tip implant | {ref}`Implant <category-implant>` |
| 70 | {ref}`HVASTIS <step-070>` | HV As N-tip implant strip | {ref}`Strip/clean <category-strip>` |
| 71 | {ref}`LDNTM <step-071>` | LD tip layer mask | {ref}`Litho <category-lithography>` |
| 72 | {ref}`LDASTI <step-072>` | LD ASTI implant | {ref}`Implant <category-implant>` |
| 73 | {ref}`LDBHI <step-073>` | LD B halo implant | {ref}`Implant <category-implant>` |
| 74 | {ref}`LDASTIS <step-074>` | LD ASTI implant strip | {ref}`Strip/clean <category-strip>` |
| 75 | {ref}`TIPRTAD <step-075>` | RTA tip activation | {ref}`Anneal <category-anneal>` |

| Step | Code | Machine class | Mask |
|---:|---|---|---|
| 64 | {ref}`NTM <step-064>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`NTM <mask-ntm>` |
| 65 | {ref}`ASTI <step-065>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`NTM <mask-ntm>` |
| 66 | {ref}`BHI <step-066>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`NTM <mask-ntm>` |
| 67 | {ref}`ASTIS <step-067>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`NTM <mask-ntm>` |
| 68 | {ref}`HVNTM <step-068>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`HVNTM <mask-hvntm>` |
| 69 | {ref}`HVASTI <step-069>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`HVNTM <mask-hvntm>` |
| 70 | {ref}`HVASTIS <step-070>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`HVNTM <mask-hvntm>` |
| 71 | {ref}`LDNTM <step-071>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`LDNTM <mask-ldntm>` |
| 72 | {ref}`LDASTI <step-072>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`LDNTM <mask-ldntm>` |
| 73 | {ref}`LDBHI <step-073>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`LDNTM <mask-ldntm>` |
| 74 | {ref}`LDASTIS <step-074>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`LDNTM <mask-ldntm>` |
| 75 | {ref}`TIPRTAD <step-075>` | {ref}`Rapid thermal processor <machine-rapid-thermal-processor>` | — |

## Spacers and source/drain

| Step | Code | Name | Category |
|---:|---|---|---|
| 76 | {ref}`SPNIT <step-076>` | Spacer nitride deposition | {ref}`Deposition <category-deposition>` |
| 77 | {ref}`SPE <step-077>` | Spacer nitride etch | {ref}`Etch <category-etch>` |
| 78 | {ref}`NPCM <step-078>` | Nitride poly cut mask | {ref}`Litho <category-lithography>` |
| 79 | {ref}`NPCME <step-079>` | Nitride poly cut mask etch | {ref}`Etch <category-etch>` |
| 80 | {ref}`SPOX <step-080>` | Spacer oxide deposition | {ref}`Deposition <category-deposition>` |
| 81 | {ref}`PSDM <step-081>` | P+ source drain implant mask | {ref}`Litho <category-lithography>` |
| 82 | {ref}`PSDI <step-082>` | P+ source drain implant | {ref}`Implant <category-implant>` |
| 83 | {ref}`2PSDI <step-083>` | 2nd P+ source drain implant | {ref}`Implant <category-implant>` |
| 84 | {ref}`PDIS <step-084>` | P+ source drain implant strip | {ref}`Strip/clean <category-strip>` |
| 85 | {ref}`NSDM <step-085>` | N+ source drain implant mask | {ref}`Litho <category-lithography>` |
| 86 | {ref}`NSDI <step-086>` | N+ source drain implant | {ref}`Implant <category-implant>` |
| 87 | {ref}`NSDIS <step-087>` | N+ source drain implant strip | {ref}`Strip/clean <category-strip>` |
| 88 | {ref}`RTAD <step-088>` | RTA source drain implant anneal | {ref}`Anneal <category-anneal>` |

| Step | Code | Machine class | Mask |
|---:|---|---|---|
| 76 | {ref}`SPNIT <step-076>` | {ref}`Vertical batch furnace <machine-vertical-furnace-lpcvd>` | — |
| 77 | {ref}`SPE <step-077>` | {ref}`Plasma etcher: dielectric and nitride <machine-plasma-etcher-dielectric>` | — |
| 78 | {ref}`NPCM <step-078>` | {ref}`DUV (KrF, 248 nm) stepper or scanner <machine-duv-krf-stepper>` | {ref}`NPCM <mask-npcm>` |
| 79 | {ref}`NPCME <step-079>` | {ref}`Plasma etcher: dielectric and nitride <machine-plasma-etcher-dielectric>` | {ref}`NPCM <mask-npcm>` |
| 80 | {ref}`SPOX <step-080>` | {ref}`PECVD <machine-pecvd>` | — |
| 81 | {ref}`PSDM <step-081>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`PSDM <mask-psdm>` |
| 82 | {ref}`PSDI <step-082>` | {ref}`High-current ion implanter <machine-high-current-implanter>` | {ref}`PSDM <mask-psdm>` |
| 83 | {ref}`2PSDI <step-083>` | {ref}`Medium-current ion implanter <machine-medium-current-implanter>` | {ref}`PSDM <mask-psdm>` |
| 84 | {ref}`PDIS <step-084>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`PSDM <mask-psdm>` |
| 85 | {ref}`NSDM <step-085>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`NSDM <mask-nsdm>` |
| 86 | {ref}`NSDI <step-086>` | {ref}`High-current ion implanter <machine-high-current-implanter>` | {ref}`NSDM <mask-nsdm>` |
| 87 | {ref}`NSDIS <step-087>` | {ref}`Downstream plasma asher <machine-downstream-plasma-asher>` | {ref}`NSDM <mask-nsdm>` |
| 88 | {ref}`RTAD <step-088>` | {ref}`Rapid thermal processor <machine-rapid-thermal-processor>` | — |

## Pre-metal dielectric, contact silicide and local interconnect

| Step | Code | Name | Category |
|---:|---|---|---|
| 89 | {ref}`PSG <step-089>` | Sacrificial PSG deposition | {ref}`Deposition <category-deposition>` |
| 90 | {ref}`CMPP <step-090>` | CMP over poly | {ref}`CMP <category-cmp>` |
| 91 | {ref}`NCAPOX <step-091>` | Cap oxide deposition | {ref}`Deposition <category-deposition>` |
| 92 | {ref}`RTAD2 <step-092>` | RTA source drain anneal | {ref}`Anneal <category-anneal>` |
| 93 | {ref}`LICM1 <step-093>` | Local interconnect contact mask | {ref}`Litho <category-lithography>` |
| 94 | {ref}`LICM1E <step-094>` | Local interconnect contact mask etch | {ref}`Etch <category-etch>` |
| 95 | {ref}`SACETCH <step-095>` | Sacrificial etch | {ref}`Etch <category-etch>` |
| 96 | {ref}`ALLY1 <step-096>` | Alloy 1 | {ref}`Anneal <category-anneal>` |
| 97 | {ref}`TI/TIN1 <step-097>` | IMP Ti/TiN deposition | {ref}`Deposition <category-deposition>` |
| 98 | {ref}`CSIL <step-098>` | Contact silicidation | {ref}`Anneal <category-anneal>` |
| 99 | {ref}`WDEP <step-099>` | Blanket CVD W deposition | {ref}`Deposition <category-deposition>` |
| 100 | {ref}`WCMPLI <step-100>` | W CMP for local interconnect | {ref}`CMP <category-cmp>` |
| 101 | {ref}`LITIN <step-101>` | TiN deposition | {ref}`Deposition <category-deposition>` |
| 102 | {ref}`LI1M <step-102>` | Local interconnect 1 mask | {ref}`Litho <category-lithography>` |
| 103 | {ref}`LI1ME <step-103>` | Local interconnect 1 mask etch | {ref}`Etch <category-etch>` |
| 104 | {ref}`LINIT <step-104>` | Nitride cap deposition | {ref}`Deposition <category-deposition>` |
| 105 | {ref}`NILD2 <step-105>` | ILD oxide deposition | {ref}`Deposition <category-deposition>` |
| 106 | {ref}`CMPL <step-106>` | CMP polish over local interconnect | {ref}`CMP <category-cmp>` |

| Step | Code | Machine class | Mask |
|---:|---|---|---|
| 89 | {ref}`PSG <step-089>` | {ref}`PECVD <machine-pecvd>` | — |
| 90 | {ref}`CMPP <step-090>` | {ref}`CMP polisher <machine-cmp-polisher>` | — |
| 91 | {ref}`NCAPOX <step-091>` | {ref}`PECVD <machine-pecvd>` | — |
| 92 | {ref}`RTAD2 <step-092>` | {ref}`Rapid thermal processor <machine-rapid-thermal-processor>` | — |
| 93 | {ref}`LICM1 <step-093>` | {ref}`DUV (KrF, 248 nm) stepper or scanner <machine-duv-krf-stepper>` | {ref}`LICM1 <mask-licm1>` |
| 94 | {ref}`LICM1E <step-094>` | {ref}`Plasma etcher: dielectric and nitride <machine-plasma-etcher-dielectric>` | {ref}`LICM1 <mask-licm1>` |
| 95 | {ref}`SACETCH <step-095>` | {ref}`Wet bench and spray processor <machine-wet-bench>` | {ref}`LICM1 <mask-licm1>` |
| 96 | {ref}`ALLY1 <step-096>` | {ref}`Vertical batch furnace <machine-vertical-furnace-anneal>` | — |
| 97 | {ref}`TI/TIN1 <step-097>` | {ref}`PVD (sputtering) cluster tool <machine-pvd-cluster-tool>` | — |
| 98 | {ref}`CSIL <step-098>` | {ref}`Rapid thermal processor <machine-rapid-thermal-processor>` | — |
| 99 | {ref}`WDEP <step-099>` | {ref}`Tungsten CVD <machine-tungsten-cvd>` | — |
| 100 | {ref}`WCMPLI <step-100>` | {ref}`CMP polisher <machine-cmp-polisher>` | — |
| 101 | {ref}`LITIN <step-101>` | {ref}`PVD (sputtering) cluster tool <machine-pvd-cluster-tool>` | — |
| 102 | {ref}`LI1M <step-102>` | {ref}`DUV (KrF, 248 nm) stepper or scanner <machine-duv-krf-stepper>` | {ref}`LI1M <mask-li1m>` |
| 103 | {ref}`LI1ME <step-103>` | {ref}`Plasma etcher: metal <machine-plasma-etcher-metal>` | {ref}`LI1M <mask-li1m>` |
| 104 | {ref}`LINIT <step-104>` | {ref}`PECVD <machine-pecvd>` | — |
| 105 | {ref}`NILD2 <step-105>` | {ref}`PECVD <machine-pecvd>` | — |
| 106 | {ref}`CMPL <step-106>` | {ref}`CMP polisher <machine-cmp-polisher>` | — |

## Metal contact and metal 1

| Step | Code | Name | Category |
|---:|---|---|---|
| 107 | {ref}`CTM1 <step-107>` | Metal contact mask | {ref}`Litho <category-lithography>` |
| 108 | {ref}`CTME <step-108>` | Metal contact mask etch | {ref}`Etch <category-etch>` |
| 109 | {ref}`TIN2 <step-109>` | IMP TiN deposition | {ref}`Deposition <category-deposition>` |
| 110 | {ref}`WDEP2 <step-110>` | Blanket CVD W deposition | {ref}`Deposition <category-deposition>` |
| 111 | {ref}`WCMP2 <step-111>` | W CMP for metal contact | {ref}`CMP <category-cmp>` |
| 112 | {ref}`TIAL6 <step-112>` | CoTi/AlCu/TiW deposition | {ref}`Deposition <category-deposition>` |
| 113 | {ref}`MM1 <step-113>` | Metal1 mask | {ref}`Litho <category-lithography>` |
| 114 | {ref}`MM1E <step-114>` | Metal1 mask etch | {ref}`Etch <category-etch>` |
| 115 | {ref}`NILD3 <step-115>` | ILD oxide deposition | {ref}`Deposition <category-deposition>` |
| 116 | {ref}`CMPM <step-116>` | CMP over metal1 | {ref}`CMP <category-cmp>` |
| 117 | {ref}`NCAPOX3 <step-117>` | CAPOX deposition | {ref}`Deposition <category-deposition>` |

| Step | Code | Machine class | Mask |
|---:|---|---|---|
| 107 | {ref}`CTM1 <step-107>` | {ref}`DUV (KrF, 248 nm) stepper or scanner <machine-duv-krf-stepper>` | {ref}`CTM1 <mask-ctm1>` |
| 108 | {ref}`CTME <step-108>` | {ref}`Plasma etcher: dielectric and nitride <machine-plasma-etcher-dielectric>` | {ref}`CTM1 <mask-ctm1>` |
| 109 | {ref}`TIN2 <step-109>` | {ref}`PVD (sputtering) cluster tool <machine-pvd-cluster-tool>` | — |
| 110 | {ref}`WDEP2 <step-110>` | {ref}`Tungsten CVD <machine-tungsten-cvd>` | — |
| 111 | {ref}`WCMP2 <step-111>` | {ref}`CMP polisher <machine-cmp-polisher>` | — |
| 112 | {ref}`TIAL6 <step-112>` | {ref}`PVD (sputtering) cluster tool <machine-pvd-cluster-tool>` | — |
| 113 | {ref}`MM1 <step-113>` | {ref}`DUV (KrF, 248 nm) stepper or scanner <machine-duv-krf-stepper>` | {ref}`MM1 <mask-mm1>` |
| 114 | {ref}`MM1E <step-114>` | {ref}`Plasma etcher: metal <machine-plasma-etcher-metal>` | {ref}`MM1 <mask-mm1>` |
| 115 | {ref}`NILD3 <step-115>` | {ref}`PECVD <machine-pecvd>` | — |
| 116 | {ref}`CMPM <step-116>` | {ref}`CMP polisher <machine-cmp-polisher>` | — |
| 117 | {ref}`NCAPOX3 <step-117>` | {ref}`PECVD <machine-pecvd>` | — |

## Via 1, metal 2 and via 2

| Step | Code | Name | Category |
|---:|---|---|---|
| 118 | {ref}`VIM <step-118>` | Via1 mask | {ref}`Litho <category-lithography>` |
| 119 | {ref}`VIME <step-119>` | Via1 mask etch | {ref}`Etch <category-etch>` |
| 120 | {ref}`TIN3 <step-120>` | IMP TiN deposition | {ref}`Deposition <category-deposition>` |
| 121 | {ref}`WDEP3 <step-121>` | Blanket CVD W deposition | {ref}`Deposition <category-deposition>` |
| 122 | {ref}`WCMP3 <step-122>` | W CMP for via1 | {ref}`CMP <category-cmp>` |
| 123 | {ref}`TIAL12 <step-123>` | AlCu 2/TiW deposition | {ref}`Deposition <category-deposition>` |
| 124 | {ref}`MM2 <step-124>` | Metal2 mask | {ref}`Litho <category-lithography>` |
| 125 | {ref}`MM2E <step-125>` | Metal2 mask etch | {ref}`Etch <category-etch>` |
| 126 | {ref}`NILD4 <step-126>` | ILD oxide deposition | {ref}`Deposition <category-deposition>` |
| 127 | {ref}`CMPM2 <step-127>` | CMP over metal2 | {ref}`CMP <category-cmp>` |
| 128 | {ref}`NCAPOX4 <step-128>` | CAPOX deposition | {ref}`Deposition <category-deposition>` |
| 129 | {ref}`VIM2 <step-129>` | Via2 mask | {ref}`Litho <category-lithography>` |
| 130 | {ref}`VIM2E <step-130>` | Via2 mask etch | {ref}`Etch <category-etch>` |
| 131 | {ref}`TIN4 <step-131>` | IMP TiN deposition | {ref}`Deposition <category-deposition>` |
| 132 | {ref}`WDEP4 <step-132>` | Blanket CVD W deposition | {ref}`Deposition <category-deposition>` |
| 133 | {ref}`WCMP4 <step-133>` | W CMP for via2 | {ref}`CMP <category-cmp>` |
| 134 | {ref}`WTIAL3 <step-134>` | AlCu 2/TiW deposition | {ref}`Deposition <category-deposition>` |

| Step | Code | Machine class | Mask |
|---:|---|---|---|
| 118 | {ref}`VIM <step-118>` | {ref}`DUV (KrF, 248 nm) stepper or scanner <machine-duv-krf-stepper>` | {ref}`VIM <mask-vim>` |
| 119 | {ref}`VIME <step-119>` | {ref}`Plasma etcher: dielectric and nitride <machine-plasma-etcher-dielectric>` | {ref}`VIM <mask-vim>` |
| 120 | {ref}`TIN3 <step-120>` | {ref}`PVD (sputtering) cluster tool <machine-pvd-cluster-tool>` | — |
| 121 | {ref}`WDEP3 <step-121>` | {ref}`Tungsten CVD <machine-tungsten-cvd>` | — |
| 122 | {ref}`WCMP3 <step-122>` | {ref}`CMP polisher <machine-cmp-polisher>` | — |
| 123 | {ref}`TIAL12 <step-123>` | {ref}`PVD (sputtering) cluster tool <machine-pvd-cluster-tool>` | — |
| 124 | {ref}`MM2 <step-124>` | {ref}`DUV (KrF, 248 nm) stepper or scanner <machine-duv-krf-stepper>` | {ref}`MM2 <mask-mm2>` |
| 125 | {ref}`MM2E <step-125>` | {ref}`Plasma etcher: metal <machine-plasma-etcher-metal>` | {ref}`MM2 <mask-mm2>` |
| 126 | {ref}`NILD4 <step-126>` | {ref}`PECVD <machine-pecvd>` | — |
| 127 | {ref}`CMPM2 <step-127>` | {ref}`CMP polisher <machine-cmp-polisher>` | — |
| 128 | {ref}`NCAPOX4 <step-128>` | {ref}`PECVD <machine-pecvd>` | — |
| 129 | {ref}`VIM2 <step-129>` | {ref}`DUV (KrF, 248 nm) stepper or scanner <machine-duv-krf-stepper>` | {ref}`VIM2 <mask-vim2>` |
| 130 | {ref}`VIM2E <step-130>` | {ref}`Plasma etcher: dielectric and nitride <machine-plasma-etcher-dielectric>` | {ref}`VIM2 <mask-vim2>` |
| 131 | {ref}`TIN4 <step-131>` | {ref}`PVD (sputtering) cluster tool <machine-pvd-cluster-tool>` | — |
| 132 | {ref}`WDEP4 <step-132>` | {ref}`Tungsten CVD <machine-tungsten-cvd>` | — |
| 133 | {ref}`WCMP4 <step-133>` | {ref}`CMP polisher <machine-cmp-polisher>` | — |
| 134 | {ref}`WTIAL3 <step-134>` | {ref}`PVD (sputtering) cluster tool <machine-pvd-cluster-tool>` | — |

## First MiM capacitor, metal 3 and via 3

| Step | Code | Name | Category |
|---:|---|---|---|
| 135 | {ref}`CAPILD <step-135>` | Capacitor ILD oxynitride deposition | {ref}`Deposition <category-deposition>` |
| 136 | {ref}`CAPTIW1 <step-136>` | Capacitor TiW deposition | {ref}`Deposition <category-deposition>` |
| 137 | {ref}`CAPM <step-137>` | Capacitor mask | {ref}`Litho <category-lithography>` |
| 138 | {ref}`CAPME <step-138>` | Capacitor mask etch | {ref}`Etch <category-etch>` |
| 139 | {ref}`MM3 <step-139>` | Metal3 mask | {ref}`Litho <category-lithography>` |
| 140 | {ref}`MM3E <step-140>` | Metal3 mask etch | {ref}`Etch <category-etch>` |
| 141 | {ref}`NILD5 <step-141>` | ILD oxide deposition | {ref}`Deposition <category-deposition>` |
| 142 | {ref}`CMPM3 <step-142>` | CMP over metal3 | {ref}`CMP <category-cmp>` |
| 143 | {ref}`NCAPOX5 <step-143>` | CAPOX deposition | {ref}`Deposition <category-deposition>` |
| 144 | {ref}`VIM3 <step-144>` | Via3 mask | {ref}`Litho <category-lithography>` |
| 145 | {ref}`VIM3E <step-145>` | Via3 mask etch | {ref}`Etch <category-etch>` |
| 146 | {ref}`TIN5 <step-146>` | IMP TiN deposition | {ref}`Deposition <category-deposition>` |
| 147 | {ref}`WDEP5 <step-147>` | Blanket CVD W deposition | {ref}`Deposition <category-deposition>` |
| 148 | {ref}`WCMP5 <step-148>` | W CMP for via3 | {ref}`CMP <category-cmp>` |

| Step | Code | Machine class | Mask |
|---:|---|---|---|
| 135 | {ref}`CAPILD <step-135>` | {ref}`PECVD <machine-pecvd>` | — |
| 136 | {ref}`CAPTIW1 <step-136>` | {ref}`PVD (sputtering) cluster tool <machine-pvd-cluster-tool>` | — |
| 137 | {ref}`CAPM <step-137>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`CAPM <mask-capm>` |
| 138 | {ref}`CAPME <step-138>` | {ref}`Plasma etcher: metal <machine-plasma-etcher-metal>` | {ref}`CAPM <mask-capm>` |
| 139 | {ref}`MM3 <step-139>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`MM3 <mask-mm3>` |
| 140 | {ref}`MM3E <step-140>` | {ref}`Plasma etcher: metal <machine-plasma-etcher-metal>` | {ref}`MM3 <mask-mm3>` |
| 141 | {ref}`NILD5 <step-141>` | {ref}`PECVD <machine-pecvd>` | — |
| 142 | {ref}`CMPM3 <step-142>` | {ref}`CMP polisher <machine-cmp-polisher>` | — |
| 143 | {ref}`NCAPOX5 <step-143>` | {ref}`PECVD <machine-pecvd>` | — |
| 144 | {ref}`VIM3 <step-144>` | {ref}`DUV (KrF, 248 nm) stepper or scanner <machine-duv-krf-stepper>` | {ref}`VIM3 <mask-vim3>` |
| 145 | {ref}`VIM3E <step-145>` | {ref}`Plasma etcher: dielectric and nitride <machine-plasma-etcher-dielectric>` | {ref}`VIM3 <mask-vim3>` |
| 146 | {ref}`TIN5 <step-146>` | {ref}`PVD (sputtering) cluster tool <machine-pvd-cluster-tool>` | — |
| 147 | {ref}`WDEP5 <step-147>` | {ref}`Tungsten CVD <machine-tungsten-cvd>` | — |
| 148 | {ref}`WCMP5 <step-148>` | {ref}`CMP polisher <machine-cmp-polisher>` | — |

## Metal 4, second MiM capacitor, via 4 and metal 5

| Step | Code | Name | Category |
|---:|---|---|---|
| 149 | {ref}`WTIAL4 <step-149>` | AlCu 2/TiW deposition | {ref}`Deposition <category-deposition>` |
| 150 | {ref}`CAPILD2 <step-150>` | Capacitor ILD oxynitride deposition | {ref}`Deposition <category-deposition>` |
| 151 | {ref}`CAPTIW2 <step-151>` | Capacitor TiW deposition | {ref}`Deposition <category-deposition>` |
| 152 | {ref}`CAP2M <step-152>` | Capacitor 2 mask | {ref}`Litho <category-lithography>` |
| 153 | {ref}`CAP2ME <step-153>` | Capacitor 2 mask etch | {ref}`Etch <category-etch>` |
| 154 | {ref}`MM4 <step-154>` | Metal4 mask | {ref}`Litho <category-lithography>` |
| 155 | {ref}`MM4E <step-155>` | Metal4 mask etch | {ref}`Etch <category-etch>` |
| 156 | {ref}`NILD6 <step-156>` | ILD oxide deposition | {ref}`Deposition <category-deposition>` |
| 157 | {ref}`CMPM4 <step-157>` | CMP over metal4 | {ref}`CMP <category-cmp>` |
| 158 | {ref}`NCAPOX6 <step-158>` | CAPOX deposition | {ref}`Deposition <category-deposition>` |
| 159 | {ref}`VIM4 <step-159>` | Via4 (pad via) mask | {ref}`Litho <category-lithography>` |
| 160 | {ref}`VIM4E <step-160>` | Via4 (pad via) mask etch | {ref}`Etch <category-etch>` |
| 161 | {ref}`WTIAL5 <step-161>` | AlCu 2/TiW deposition | {ref}`Deposition <category-deposition>` |
| 162 | {ref}`MM5 <step-162>` | Metal5 mask | {ref}`Litho <category-lithography>` |
| 163 | {ref}`MM5E <step-163>` | Metal5 mask etch | {ref}`Etch <category-etch>` |

| Step | Code | Machine class | Mask |
|---:|---|---|---|
| 149 | {ref}`WTIAL4 <step-149>` | {ref}`PVD (sputtering) cluster tool <machine-pvd-cluster-tool>` | — |
| 150 | {ref}`CAPILD2 <step-150>` | {ref}`PECVD <machine-pecvd>` | — |
| 151 | {ref}`CAPTIW2 <step-151>` | {ref}`PVD (sputtering) cluster tool <machine-pvd-cluster-tool>` | — |
| 152 | {ref}`CAP2M <step-152>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`CAP2M <mask-cap2m>` |
| 153 | {ref}`CAP2ME <step-153>` | {ref}`Plasma etcher: metal <machine-plasma-etcher-metal>` | {ref}`CAP2M <mask-cap2m>` |
| 154 | {ref}`MM4 <step-154>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`MM4 <mask-mm4>` |
| 155 | {ref}`MM4E <step-155>` | {ref}`Plasma etcher: metal <machine-plasma-etcher-metal>` | {ref}`MM4 <mask-mm4>` |
| 156 | {ref}`NILD6 <step-156>` | {ref}`PECVD <machine-pecvd>` | — |
| 157 | {ref}`CMPM4 <step-157>` | {ref}`CMP polisher <machine-cmp-polisher>` | — |
| 158 | {ref}`NCAPOX6 <step-158>` | {ref}`PECVD <machine-pecvd>` | — |
| 159 | {ref}`VIM4 <step-159>` | {ref}`DUV (KrF, 248 nm) stepper or scanner <machine-duv-krf-stepper>` | {ref}`VIM4 <mask-vim4>` |
| 160 | {ref}`VIM4E <step-160>` | {ref}`Plasma etcher: dielectric and nitride <machine-plasma-etcher-dielectric>` | {ref}`VIM4 <mask-vim4>` |
| 161 | {ref}`WTIAL5 <step-161>` | {ref}`PVD (sputtering) cluster tool <machine-pvd-cluster-tool>` | — |
| 162 | {ref}`MM5 <step-162>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`MM5 <mask-mm5>` |
| 163 | {ref}`MM5E <step-163>` | {ref}`Plasma etcher: metal <machine-plasma-etcher-metal>` | {ref}`MM5 <mask-mm5>` |

## Passivation, pads, alloy and test

| Step | Code | Name | Category |
|---:|---|---|---|
| 164 | {ref}`NFUSOX <step-164>` | Fuse oxide deposition | {ref}`Deposition <category-deposition>` |
| 165 | {ref}`NSM <step-165>` | Nitride seal mask | {ref}`Litho <category-lithography>` |
| 166 | {ref}`NSME <step-166>` | Nitride seal mask etch | {ref}`Etch <category-etch>` |
| 167 | {ref}`NTSD <step-167>` | Nitride topside deposition | {ref}`Deposition <category-deposition>` |
| 168 | {ref}`PDM <step-168>` | Pad mask | {ref}`Litho <category-lithography>` |
| 169 | {ref}`PDME <step-169>` | Pad mask etch | {ref}`Etch <category-etch>` |
| 170 | {ref}`ALLY <step-170>` | Alloy | {ref}`Anneal <category-anneal>` |
| 171 | {ref}`HPETEST <step-171>` | Electrical test | {ref}`Test <category-test>` |

| Step | Code | Machine class | Mask |
|---:|---|---|---|
| 164 | {ref}`NFUSOX <step-164>` | {ref}`PECVD <machine-pecvd>` | — |
| 165 | {ref}`NSM <step-165>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`NSM <mask-nsm>` |
| 166 | {ref}`NSME <step-166>` | {ref}`Plasma etcher: dielectric and nitride <machine-plasma-etcher-dielectric>` | {ref}`NSM <mask-nsm>` |
| 167 | {ref}`NTSD <step-167>` | {ref}`PECVD <machine-pecvd>` | — |
| 168 | {ref}`PDM <step-168>` | {ref}`i-line stepper or scanner <machine-i-line-stepper>` | {ref}`PDM <mask-pdm>` |
| 169 | {ref}`PDME <step-169>` | {ref}`Plasma etcher: dielectric and nitride <machine-plasma-etcher-dielectric>` | {ref}`PDM <mask-pdm>` |
| 170 | {ref}`ALLY <step-170>` | {ref}`Vertical batch furnace <machine-vertical-furnace-anneal>` | — |
| 171 | {ref}`HPETEST <step-171>` | {ref}`Parametric tester and prober <machine-parametric-tester>` | — |

```{toctree}
:maxdepth: 1
:hidden:

001 SMAT — Starting material <001-smat>
002 BOX — Base oxidation <002-box>
003 ISONIT — Iso nitride deposition <003-isonit>
004 FOM — Field oxide mask <004-fom>
005 STINITE — Shallow trench nitride etch <005-stinite>
006 STIE — Shallow trench etch <006-stie>
007 DNM — Deep N-well mask <007-dnm>
008 DNI — Deep N+ implant <008-dni>
009 DNIS — High V deep N-well implant strip <009-dnis>
010 LINOX — LINOX oxidation <010-linox>
011 FILOX — Fill oxide deposition <011-filox>
012 CMPNIT — CMP over nitride <012-cmpnit>
013 NS19 — Nitride strip <013-ns19>
014 LVTNM — Low Vt NMOS mask <014-lvtnm>
015 LVTNI — Low Vt NMOS implantation <015-lvtni>
016 LVTNIS — Low Vt NMOS implant strip <016-lvtnis>
017 NWM — N-well mask <017-nwm>
018 NWI — N-well implant <018-nwi>
019 NWI2 — NWI2 implant <019-nwi2>
020 LVTPI — Low V P-channel implant <020-lvtpi>
021 LVTPIS — P-channel implant strip <021-lvtpis>
022 HVTPM — High V P-channel implant mask <022-hvtpm>
023 PCHI — P-channel implant <023-pchi>
024 PNCHI — P-channel BF2 implant <024-pnchi>
025 PCHIS — P-channel BF2 implant strip <025-pchis>
026 PWBM — P-well block mask <026-pwbm>
027 PWI — P-well implant <027-pwi>
028 PWI2 — PWI2 implant <028-pwi2>
029 PWIS — P-well implant strip <029-pwis>
030 PWDEM — P-well drain extended mask <030-pwdem>
031 PWDEI1 — PWDEI1 implant <031-pwdei1>
032 PWDEI2 — PWDEI2 implant <032-pwdei2>
033 PWDEIS — PWDEIS implant strip <033-pwdeis>
034 RTAI — Pre-gate oxide anneal <034-rtai>
035 TUNM — Tunnel mask <035-tunm>
036 TUNARCE — Tunnel mask ARC etch <036-tunarce>
037 PTSI — Punch-through stop implant <037-ptsi>
038 DEPI — Depletion implant <038-depi>
039 TUNME — Tunnel mask etch <039-tunme>
040 ONO — ONO stack oxidation <040-ono>
041 ONOM — ONO mask <041-onom>
042 ONOME — ONO mask etch <042-onome>
043 GOX100 — Gate oxidation <043-gox100>
044 LVOM — Low voltage oxide mask <044-lvom>
045 NCHI — N-channel implant <045-nchi>
046 GOXETCH — Low V gate oxide etch <046-goxetch>
047 LVGOX — Gate oxidation <047-lvgox>
048 SAGD — Single a-Si gate deposition <048-sagd>
049 RPM — Resistor protect mask <049-rpm>
050 P1I — Poly1 implant <050-p1i>
051 P1IS — P1IS implant resist strip <051-p1is>
052 RRPM — Rev resistor protect mask <052-rrpm>
053 PRI — PRI implant splits <053-pri>
054 PRIS — PRI implant resist strip <054-pris>
055 URPM — Ultra-high resistor poly mask <055-urpm>
056 UPRI — UPRI implant <056-upri>
057 UPRIS — UPRIS implant resist strip <057-upris>
058 GATENIT — Gate poly nitride deposition <058-gatenit>
059 POC — Protective oxide cap <059-poc>
060 BFR — Backside film removal <060-bfr>
061 P1M — Poly mask <061-p1m>
062 P1ME — Poly mask poly etch <062-p1me>
063 IOX45 — Implant oxidation <063-iox45>
064 NTM — NTM mask (tip formation) <064-ntm>
065 ASTI — As tip implant <065-asti>
066 BHI — B halo implant <066-bhi>
067 ASTIS — As tip implant strip <067-astis>
068 HVNTM — HV N-tip mask formation <068-hvntm>
069 HVASTI — HV As N-tip implant <069-hvasti>
070 HVASTIS — HV As N-tip implant strip <070-hvastis>
071 LDNTM — LD tip layer mask <071-ldntm>
072 LDASTI — LD ASTI implant <072-ldasti>
073 LDBHI — LD B halo implant <073-ldbhi>
074 LDASTIS — LD ASTI implant strip <074-ldastis>
075 TIPRTAD — RTA tip activation <075-tiprtad>
076 SPNIT — Spacer nitride deposition <076-spnit>
077 SPE — Spacer nitride etch <077-spe>
078 NPCM — Nitride poly cut mask <078-npcm>
079 NPCME — Nitride poly cut mask etch <079-npcme>
080 SPOX — Spacer oxide deposition <080-spox>
081 PSDM — P+ source drain implant mask <081-psdm>
082 PSDI — P+ source drain implant <082-psdi>
083 2PSDI — 2nd P+ source drain implant <083-2psdi>
084 PDIS — P+ source drain implant strip <084-pdis>
085 NSDM — N+ source drain implant mask <085-nsdm>
086 NSDI — N+ source drain implant <086-nsdi>
087 NSDIS — N+ source drain implant strip <087-nsdis>
088 RTAD — RTA source drain implant anneal <088-rtad>
089 PSG — Sacrificial PSG deposition <089-psg>
090 CMPP — CMP over poly <090-cmpp>
091 NCAPOX — Cap oxide deposition <091-ncapox>
092 RTAD2 — RTA source drain anneal <092-rtad2>
093 LICM1 — Local interconnect contact mask <093-licm1>
094 LICM1E — Local interconnect contact mask etch <094-licm1e>
095 SACETCH — Sacrificial etch <095-sacetch>
096 ALLY1 — Alloy 1 <096-ally1>
097 TI/TIN1 — IMP Ti/TiN deposition <097-ti-tin1>
098 CSIL — Contact silicidation <098-csil>
099 WDEP — Blanket CVD W deposition <099-wdep>
100 WCMPLI — W CMP for local interconnect <100-wcmpli>
101 LITIN — TiN deposition <101-litin>
102 LI1M — Local interconnect 1 mask <102-li1m>
103 LI1ME — Local interconnect 1 mask etch <103-li1me>
104 LINIT — Nitride cap deposition <104-linit>
105 NILD2 — ILD oxide deposition <105-nild2>
106 CMPL — CMP polish over local interconnect <106-cmpl>
107 CTM1 — Metal contact mask <107-ctm1>
108 CTME — Metal contact mask etch <108-ctme>
109 TIN2 — IMP TiN deposition <109-tin2>
110 WDEP2 — Blanket CVD W deposition <110-wdep2>
111 WCMP2 — W CMP for metal contact <111-wcmp2>
112 TIAL6 — CoTi/AlCu/TiW deposition <112-tial6>
113 MM1 — Metal1 mask <113-mm1>
114 MM1E — Metal1 mask etch <114-mm1e>
115 NILD3 — ILD oxide deposition <115-nild3>
116 CMPM — CMP over metal1 <116-cmpm>
117 NCAPOX3 — CAPOX deposition <117-ncapox3>
118 VIM — Via1 mask <118-vim>
119 VIME — Via1 mask etch <119-vime>
120 TIN3 — IMP TiN deposition <120-tin3>
121 WDEP3 — Blanket CVD W deposition <121-wdep3>
122 WCMP3 — W CMP for via1 <122-wcmp3>
123 TIAL12 — AlCu 2/TiW deposition <123-tial12>
124 MM2 — Metal2 mask <124-mm2>
125 MM2E — Metal2 mask etch <125-mm2e>
126 NILD4 — ILD oxide deposition <126-nild4>
127 CMPM2 — CMP over metal2 <127-cmpm2>
128 NCAPOX4 — CAPOX deposition <128-ncapox4>
129 VIM2 — Via2 mask <129-vim2>
130 VIM2E — Via2 mask etch <130-vim2e>
131 TIN4 — IMP TiN deposition <131-tin4>
132 WDEP4 — Blanket CVD W deposition <132-wdep4>
133 WCMP4 — W CMP for via2 <133-wcmp4>
134 WTIAL3 — AlCu 2/TiW deposition <134-wtial3>
135 CAPILD — Capacitor ILD oxynitride deposition <135-capild>
136 CAPTIW1 — Capacitor TiW deposition <136-captiw1>
137 CAPM — Capacitor mask <137-capm>
138 CAPME — Capacitor mask etch <138-capme>
139 MM3 — Metal3 mask <139-mm3>
140 MM3E — Metal3 mask etch <140-mm3e>
141 NILD5 — ILD oxide deposition <141-nild5>
142 CMPM3 — CMP over metal3 <142-cmpm3>
143 NCAPOX5 — CAPOX deposition <143-ncapox5>
144 VIM3 — Via3 mask <144-vim3>
145 VIM3E — Via3 mask etch <145-vim3e>
146 TIN5 — IMP TiN deposition <146-tin5>
147 WDEP5 — Blanket CVD W deposition <147-wdep5>
148 WCMP5 — W CMP for via3 <148-wcmp5>
149 WTIAL4 — AlCu 2/TiW deposition <149-wtial4>
150 CAPILD2 — Capacitor ILD oxynitride deposition <150-capild2>
151 CAPTIW2 — Capacitor TiW deposition <151-captiw2>
152 CAP2M — Capacitor 2 mask <152-cap2m>
153 CAP2ME — Capacitor 2 mask etch <153-cap2me>
154 MM4 — Metal4 mask <154-mm4>
155 MM4E — Metal4 mask etch <155-mm4e>
156 NILD6 — ILD oxide deposition <156-nild6>
157 CMPM4 — CMP over metal4 <157-cmpm4>
158 NCAPOX6 — CAPOX deposition <158-ncapox6>
159 VIM4 — Via4 (pad via) mask <159-vim4>
160 VIM4E — Via4 (pad via) mask etch <160-vim4e>
161 WTIAL5 — AlCu 2/TiW deposition <161-wtial5>
162 MM5 — Metal5 mask <162-mm5>
163 MM5E — Metal5 mask etch <163-mm5e>
164 NFUSOX — Fuse oxide deposition <164-nfusox>
165 NSM — Nitride seal mask <165-nsm>
166 NSME — Nitride seal mask etch <166-nsme>
167 NTSD — Nitride topside deposition <167-ntsd>
168 PDM — Pad mask <168-pdm>
169 PDME — Pad mask etch <169-pdme>
170 ALLY — Alloy <170-ally>
171 HPETEST — Electrical test <171-hpetest>
```

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    retrieved 2026-09-14; tab "Sheet1" lists the 171 steps (number, code and
    description). <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
