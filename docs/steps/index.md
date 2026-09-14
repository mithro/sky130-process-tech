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

| # | Code | Step | Category |
|---|------|------|----------|
| 1 | {ref}`SMAT <step-001>` | Starting material | {ref}`Substrate / starting material <category-substrate>` |
| 2 | {ref}`BOX <step-002>` | Base oxidation | {ref}`Thermal oxidation <category-oxidation>` |
| 3 | {ref}`ISONIT <step-003>` | Iso nitride deposition | {ref}`Thin-film deposition <category-deposition>` |
| 4 | {ref}`FOM <step-004>` | Field oxide mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 5 | {ref}`STINITE <step-005>` | Shallow trench nitride etch | {ref}`Etch <category-etch>` |
| 6 | {ref}`STIE <step-006>` | Shallow trench etch | {ref}`Etch <category-etch>` |
| 7 | {ref}`DNM <step-007>` | Deep N-well mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 8 | {ref}`DNI <step-008>` | Deep N+ implant | {ref}`Ion implantation <category-implant>` |
| 9 | {ref}`DNIS <step-009>` | High V deep N-well implant strip | {ref}`Resist strip / clean <category-strip>` |
| 10 | {ref}`LINOX <step-010>` | LINOX oxidation | {ref}`Thermal oxidation <category-oxidation>` |
| 11 | {ref}`FILOX <step-011>` | Fill oxide deposition | {ref}`Thin-film deposition <category-deposition>` |
| 12 | {ref}`CMPNIT <step-012>` | CMP over nitride | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| 13 | {ref}`NS19 <step-013>` | Nitride strip | {ref}`Resist strip / clean <category-strip>` |
| 14 | {ref}`LVTNM <step-014>` | Low Vt NMOS mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 15 | {ref}`LVTNI <step-015>` | Low Vt NMOS implantation | {ref}`Ion implantation <category-implant>` |
| 16 | {ref}`LVTNIS <step-016>` | Low Vt NMOS implant strip | {ref}`Resist strip / clean <category-strip>` |
| 17 | {ref}`NWM <step-017>` | N-well mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 18 | {ref}`NWI <step-018>` | N-well implant | {ref}`Ion implantation <category-implant>` |
| 19 | {ref}`NWI2 <step-019>` | NWI2 implant | {ref}`Ion implantation <category-implant>` |
| 20 | {ref}`LVTPI <step-020>` | Low V P-channel implant | {ref}`Ion implantation <category-implant>` |
| 21 | {ref}`LVTPIS <step-021>` | P-channel implant strip | {ref}`Resist strip / clean <category-strip>` |
| 22 | {ref}`HVTPM <step-022>` | High V P-channel implant mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 23 | {ref}`PCHI <step-023>` | P-channel implant | {ref}`Ion implantation <category-implant>` |
| 24 | {ref}`PNCHI <step-024>` | P-channel BF2 implant | {ref}`Ion implantation <category-implant>` |
| 25 | {ref}`PCHIS <step-025>` | P-channel BF2 implant strip | {ref}`Resist strip / clean <category-strip>` |
| 26 | {ref}`PWBM <step-026>` | P-well block mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 27 | {ref}`PWI <step-027>` | P-well implant | {ref}`Ion implantation <category-implant>` |
| 28 | {ref}`PWI2 <step-028>` | PWI2 implant | {ref}`Ion implantation <category-implant>` |
| 29 | {ref}`PWIS <step-029>` | P-well implant strip | {ref}`Resist strip / clean <category-strip>` |
| 30 | {ref}`PWDEM <step-030>` | P-well drain extended mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 31 | {ref}`PWDEI1 <step-031>` | PWDEI1 implant | {ref}`Ion implantation <category-implant>` |
| 32 | {ref}`PWDEI2 <step-032>` | PWDEI2 implant | {ref}`Ion implantation <category-implant>` |
| 33 | {ref}`PWDEIS <step-033>` | PWDEIS implant strip | {ref}`Resist strip / clean <category-strip>` |
| 34 | {ref}`RTAI <step-034>` | Pre-gate oxide anneal | {ref}`Anneal / thermal processing <category-anneal>` |
| 35 | {ref}`TUNM <step-035>` | Tunnel mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 36 | {ref}`TUNARCE <step-036>` | Tunnel mask ARC etch | {ref}`Etch <category-etch>` |
| 37 | {ref}`PTSI <step-037>` | Punch-through stop implant | {ref}`Ion implantation <category-implant>` |
| 38 | {ref}`DEPI <step-038>` | Depletion implant | {ref}`Ion implantation <category-implant>` |
| 39 | {ref}`TUNME <step-039>` | Tunnel mask etch | {ref}`Etch <category-etch>` |
| 40 | {ref}`ONO <step-040>` | ONO stack oxidation | {ref}`Thermal oxidation <category-oxidation>` |
| 41 | {ref}`ONOM <step-041>` | ONO mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 42 | {ref}`ONOME <step-042>` | ONO mask etch | {ref}`Etch <category-etch>` |
| 43 | {ref}`GOX100 <step-043>` | Gate oxidation | {ref}`Thermal oxidation <category-oxidation>` |
| 44 | {ref}`LVOM <step-044>` | Low voltage oxide mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 45 | {ref}`NCHI <step-045>` | N-channel implant | {ref}`Ion implantation <category-implant>` |
| 46 | {ref}`GOXETCH <step-046>` | Low V gate oxide etch | {ref}`Etch <category-etch>` |
| 47 | {ref}`LVGOX <step-047>` | Gate oxidation | {ref}`Thermal oxidation <category-oxidation>` |
| 48 | {ref}`SAGD <step-048>` | Single a-Si gate deposition | {ref}`Thin-film deposition <category-deposition>` |
| 49 | {ref}`RPM <step-049>` | Resistor protect mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 50 | {ref}`P1I <step-050>` | Poly1 implant | {ref}`Ion implantation <category-implant>` |
| 51 | {ref}`P1IS <step-051>` | P1IS implant resist strip | {ref}`Resist strip / clean <category-strip>` |
| 52 | {ref}`RRPM <step-052>` | Rev resistor protect mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 53 | {ref}`PRI <step-053>` | PRI implant splits | {ref}`Ion implantation <category-implant>` |
| 54 | {ref}`PRIS <step-054>` | PRI implant resist strip | {ref}`Resist strip / clean <category-strip>` |
| 55 | {ref}`URPM <step-055>` | Ultra-high resistor poly mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 56 | {ref}`UPRI <step-056>` | UPRI implant | {ref}`Ion implantation <category-implant>` |
| 57 | {ref}`UPRIS <step-057>` | UPRIS implant resist strip | {ref}`Resist strip / clean <category-strip>` |
| 58 | {ref}`GATENIT <step-058>` | Gate poly nitride deposition | {ref}`Thin-film deposition <category-deposition>` |
| 59 | {ref}`POC <step-059>` | Protective oxide cap | {ref}`Thin-film deposition <category-deposition>` |
| 60 | {ref}`BFR <step-060>` | Backside film removal | {ref}`Etch <category-etch>` |
| 61 | {ref}`P1M <step-061>` | Poly mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 62 | {ref}`P1ME <step-062>` | Poly mask poly etch | {ref}`Etch <category-etch>` |
| 63 | {ref}`IOX45 <step-063>` | Implant oxidation | {ref}`Thermal oxidation <category-oxidation>` |
| 64 | {ref}`NTM <step-064>` | NTM mask (tip formation) | {ref}`Photolithography (mask step) <category-lithography>` |
| 65 | {ref}`ASTI <step-065>` | As tip implant | {ref}`Ion implantation <category-implant>` |
| 66 | {ref}`BHI <step-066>` | B halo implant | {ref}`Ion implantation <category-implant>` |
| 67 | {ref}`ASTIS <step-067>` | As tip implant strip | {ref}`Resist strip / clean <category-strip>` |
| 68 | {ref}`HVNTM <step-068>` | HV N-tip mask formation | {ref}`Photolithography (mask step) <category-lithography>` |
| 69 | {ref}`HVASTI <step-069>` | HV As N-tip implant | {ref}`Ion implantation <category-implant>` |
| 70 | {ref}`HVASTIS <step-070>` | HV As N-tip implant strip | {ref}`Resist strip / clean <category-strip>` |
| 71 | {ref}`LDNTM <step-071>` | LD tip layer mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 72 | {ref}`LDASTI <step-072>` | LD ASTI implant | {ref}`Ion implantation <category-implant>` |
| 73 | {ref}`LDBHI <step-073>` | LD B halo implant | {ref}`Ion implantation <category-implant>` |
| 74 | {ref}`LDASTIS <step-074>` | LD ASTI implant strip | {ref}`Resist strip / clean <category-strip>` |
| 75 | {ref}`TIPRTAD <step-075>` | RTA tip activation | {ref}`Anneal / thermal processing <category-anneal>` |
| 76 | {ref}`SPNIT <step-076>` | Spacer nitride deposition | {ref}`Thin-film deposition <category-deposition>` |
| 77 | {ref}`SPE <step-077>` | Spacer nitride etch | {ref}`Etch <category-etch>` |
| 78 | {ref}`NPCM <step-078>` | Nitride poly cut mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 79 | {ref}`NPCME <step-079>` | Nitride poly cut mask etch | {ref}`Etch <category-etch>` |
| 80 | {ref}`SPOX <step-080>` | Spacer oxide deposition | {ref}`Thin-film deposition <category-deposition>` |
| 81 | {ref}`PSDM <step-081>` | P+ source drain implant mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 82 | {ref}`PSDI <step-082>` | P+ source drain implant | {ref}`Ion implantation <category-implant>` |
| 83 | {ref}`2PSDI <step-083>` | 2nd P+ source drain implant | {ref}`Ion implantation <category-implant>` |
| 84 | {ref}`PDIS <step-084>` | P+ source drain implant strip | {ref}`Resist strip / clean <category-strip>` |
| 85 | {ref}`NSDM <step-085>` | N+ source drain implant mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 86 | {ref}`NSDI <step-086>` | N+ source drain implant | {ref}`Ion implantation <category-implant>` |
| 87 | {ref}`NSDIS <step-087>` | N+ source drain implant strip | {ref}`Resist strip / clean <category-strip>` |
| 88 | {ref}`RTAD <step-088>` | RTA source drain implant anneal | {ref}`Anneal / thermal processing <category-anneal>` |
| 89 | {ref}`PSG <step-089>` | Sacrificial PSG deposition | {ref}`Thin-film deposition <category-deposition>` |
| 90 | {ref}`CMPP <step-090>` | CMP over poly | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| 91 | {ref}`NCAPOX <step-091>` | Cap oxide deposition | {ref}`Thin-film deposition <category-deposition>` |
| 92 | {ref}`RTAD2 <step-092>` | RTA source drain anneal | {ref}`Anneal / thermal processing <category-anneal>` |
| 93 | {ref}`LICM1 <step-093>` | Local interconnect contact mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 94 | {ref}`LICM1E <step-094>` | Local interconnect contact mask etch | {ref}`Etch <category-etch>` |
| 95 | {ref}`SACETCH <step-095>` | Sacrificial etch | {ref}`Etch <category-etch>` |
| 96 | {ref}`ALLY1 <step-096>` | Alloy 1 | {ref}`Anneal / thermal processing <category-anneal>` |
| 97 | {ref}`TI/TIN1 <step-097>` | IMP Ti/TiN deposition | {ref}`Thin-film deposition <category-deposition>` |
| 98 | {ref}`CSIL <step-098>` | Contact silicidation | {ref}`Anneal / thermal processing <category-anneal>` |
| 99 | {ref}`WDEP <step-099>` | Blanket CVD W deposition | {ref}`Thin-film deposition <category-deposition>` |
| 100 | {ref}`WCMPLI <step-100>` | W CMP for local interconnect | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| 101 | {ref}`LITIN <step-101>` | TiN deposition | {ref}`Thin-film deposition <category-deposition>` |
| 102 | {ref}`LI1M <step-102>` | Local interconnect 1 mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 103 | {ref}`LI1ME <step-103>` | Local interconnect 1 mask etch | {ref}`Etch <category-etch>` |
| 104 | {ref}`LINIT <step-104>` | Nitride cap deposition | {ref}`Thin-film deposition <category-deposition>` |
| 105 | {ref}`NILD2 <step-105>` | ILD oxide deposition | {ref}`Thin-film deposition <category-deposition>` |
| 106 | {ref}`CMPL <step-106>` | CMP polish over local interconnect | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| 107 | {ref}`CTM1 <step-107>` | Metal contact mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 108 | {ref}`CTME <step-108>` | Metal contact mask etch | {ref}`Etch <category-etch>` |
| 109 | {ref}`TIN2 <step-109>` | IMP TiN deposition | {ref}`Thin-film deposition <category-deposition>` |
| 110 | {ref}`WDEP2 <step-110>` | Blanket CVD W deposition | {ref}`Thin-film deposition <category-deposition>` |
| 111 | {ref}`WCMP2 <step-111>` | W CMP for metal contact | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| 112 | {ref}`TIAL6 <step-112>` | CoTi/AlCu/TiW deposition | {ref}`Thin-film deposition <category-deposition>` |
| 113 | {ref}`MM1 <step-113>` | Metal1 mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 114 | {ref}`MM1E <step-114>` | Metal1 mask etch | {ref}`Etch <category-etch>` |
| 115 | {ref}`NILD3 <step-115>` | ILD oxide deposition | {ref}`Thin-film deposition <category-deposition>` |
| 116 | {ref}`CMPM <step-116>` | CMP over metal1 | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| 117 | {ref}`NCAPOX3 <step-117>` | CAPOX deposition | {ref}`Thin-film deposition <category-deposition>` |
| 118 | {ref}`VIM <step-118>` | Via1 mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 119 | {ref}`VIME <step-119>` | Via1 mask etch | {ref}`Etch <category-etch>` |
| 120 | {ref}`TIN3 <step-120>` | IMP TiN deposition | {ref}`Thin-film deposition <category-deposition>` |
| 121 | {ref}`WDEP3 <step-121>` | Blanket CVD W deposition | {ref}`Thin-film deposition <category-deposition>` |
| 122 | {ref}`WCMP3 <step-122>` | W CMP for via1 | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| 123 | {ref}`TIAL12 <step-123>` | AlCu 2/TiW deposition | {ref}`Thin-film deposition <category-deposition>` |
| 124 | {ref}`MM2 <step-124>` | Metal2 mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 125 | {ref}`MM2E <step-125>` | Metal2 mask etch | {ref}`Etch <category-etch>` |
| 126 | {ref}`NILD4 <step-126>` | ILD oxide deposition | {ref}`Thin-film deposition <category-deposition>` |
| 127 | {ref}`CMPM2 <step-127>` | CMP over metal2 | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| 128 | {ref}`NCAPOX4 <step-128>` | CAPOX deposition | {ref}`Thin-film deposition <category-deposition>` |
| 129 | {ref}`VIM2 <step-129>` | Via2 mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 130 | {ref}`VIM2E <step-130>` | Via2 mask etch | {ref}`Etch <category-etch>` |
| 131 | {ref}`TIN4 <step-131>` | IMP TiN deposition | {ref}`Thin-film deposition <category-deposition>` |
| 132 | {ref}`WDEP4 <step-132>` | Blanket CVD W deposition | {ref}`Thin-film deposition <category-deposition>` |
| 133 | {ref}`WCMP4 <step-133>` | W CMP for via2 | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| 134 | {ref}`WTIAL3 <step-134>` | AlCu 2/TiW deposition | {ref}`Thin-film deposition <category-deposition>` |
| 135 | {ref}`CAPILD <step-135>` | Capacitor ILD oxynitride deposition | {ref}`Thin-film deposition <category-deposition>` |
| 136 | {ref}`CAPTIW1 <step-136>` | Capacitor TiW deposition | {ref}`Thin-film deposition <category-deposition>` |
| 137 | {ref}`CAPM <step-137>` | Capacitor mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 138 | {ref}`CAPME <step-138>` | Capacitor mask etch | {ref}`Etch <category-etch>` |
| 139 | {ref}`MM3 <step-139>` | Metal3 mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 140 | {ref}`MM3E <step-140>` | Metal3 mask etch | {ref}`Etch <category-etch>` |
| 141 | {ref}`NILD5 <step-141>` | ILD oxide deposition | {ref}`Thin-film deposition <category-deposition>` |
| 142 | {ref}`CMPM3 <step-142>` | CMP over metal3 | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| 143 | {ref}`NCAPOX5 <step-143>` | CAPOX deposition | {ref}`Thin-film deposition <category-deposition>` |
| 144 | {ref}`VIM3 <step-144>` | Via3 mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 145 | {ref}`VIM3E <step-145>` | Via3 mask etch | {ref}`Etch <category-etch>` |
| 146 | {ref}`TIN5 <step-146>` | IMP TiN deposition | {ref}`Thin-film deposition <category-deposition>` |
| 147 | {ref}`WDEP5 <step-147>` | Blanket CVD W deposition | {ref}`Thin-film deposition <category-deposition>` |
| 148 | {ref}`WCMP5 <step-148>` | W CMP for via3 | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| 149 | {ref}`WTIAL4 <step-149>` | AlCu 2/TiW deposition | {ref}`Thin-film deposition <category-deposition>` |
| 150 | {ref}`CAPILD2 <step-150>` | Capacitor ILD oxynitride deposition | {ref}`Thin-film deposition <category-deposition>` |
| 151 | {ref}`CAPTIW2 <step-151>` | Capacitor TiW deposition | {ref}`Thin-film deposition <category-deposition>` |
| 152 | {ref}`CAP2M <step-152>` | Capacitor 2 mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 153 | {ref}`CAP2ME <step-153>` | Capacitor 2 mask etch | {ref}`Etch <category-etch>` |
| 154 | {ref}`MM4 <step-154>` | Metal4 mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 155 | {ref}`MM4E <step-155>` | Metal4 mask etch | {ref}`Etch <category-etch>` |
| 156 | {ref}`NILD6 <step-156>` | ILD oxide deposition | {ref}`Thin-film deposition <category-deposition>` |
| 157 | {ref}`CMPM4 <step-157>` | CMP over metal4 | {ref}`Chemical-mechanical planarisation <category-cmp>` |
| 158 | {ref}`NCAPOX6 <step-158>` | CAPOX deposition | {ref}`Thin-film deposition <category-deposition>` |
| 159 | {ref}`VIM4 <step-159>` | Via4 (pad via) mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 160 | {ref}`VIM4E <step-160>` | Via4 (pad via) mask etch | {ref}`Etch <category-etch>` |
| 161 | {ref}`WTIAL5 <step-161>` | AlCu 2/TiW deposition | {ref}`Thin-film deposition <category-deposition>` |
| 162 | {ref}`MM5 <step-162>` | Metal5 mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 163 | {ref}`MM5E <step-163>` | Metal5 mask etch | {ref}`Etch <category-etch>` |
| 164 | {ref}`NFUSOX <step-164>` | Fuse oxide deposition | {ref}`Thin-film deposition <category-deposition>` |
| 165 | {ref}`NSM <step-165>` | Nitride seal mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 166 | {ref}`NSME <step-166>` | Nitride seal mask etch | {ref}`Etch <category-etch>` |
| 167 | {ref}`NTSD <step-167>` | Nitride topside deposition | {ref}`Thin-film deposition <category-deposition>` |
| 168 | {ref}`PDM <step-168>` | Pad mask | {ref}`Photolithography (mask step) <category-lithography>` |
| 169 | {ref}`PDME <step-169>` | Pad mask etch | {ref}`Etch <category-etch>` |
| 170 | {ref}`ALLY <step-170>` | Alloy | {ref}`Anneal / thermal processing <category-anneal>` |
| 171 | {ref}`HPETEST <step-171>` | Electrical test | {ref}`Electrical test / metrology <category-test>` |

```{toctree}
:maxdepth: 1
:hidden:

001-smat
002-box
003-isonit
004-fom
005-stinite
006-stie
007-dnm
008-dni
009-dnis
010-linox
011-filox
012-cmpnit
013-ns19
014-lvtnm
015-lvtni
016-lvtnis
017-nwm
018-nwi
019-nwi2
020-lvtpi
021-lvtpis
022-hvtpm
023-pchi
024-pnchi
025-pchis
026-pwbm
027-pwi
028-pwi2
029-pwis
030-pwdem
031-pwdei1
032-pwdei2
033-pwdeis
034-rtai
035-tunm
036-tunarce
037-ptsi
038-depi
039-tunme
040-ono
041-onom
042-onome
043-gox100
044-lvom
045-nchi
046-goxetch
047-lvgox
048-sagd
049-rpm
050-p1i
051-p1is
052-rrpm
053-pri
054-pris
055-urpm
056-upri
057-upris
058-gatenit
059-poc
060-bfr
061-p1m
062-p1me
063-iox45
064-ntm
065-asti
066-bhi
067-astis
068-hvntm
069-hvasti
070-hvastis
071-ldntm
072-ldasti
073-ldbhi
074-ldastis
075-tiprtad
076-spnit
077-spe
078-npcm
079-npcme
080-spox
081-psdm
082-psdi
083-2psdi
084-pdis
085-nsdm
086-nsdi
087-nsdis
088-rtad
089-psg
090-cmpp
091-ncapox
092-rtad2
093-licm1
094-licm1e
095-sacetch
096-ally1
097-ti-tin1
098-csil
099-wdep
100-wcmpli
101-litin
102-li1m
103-li1me
104-linit
105-nild2
106-cmpl
107-ctm1
108-ctme
109-tin2
110-wdep2
111-wcmp2
112-tial6
113-mm1
114-mm1e
115-nild3
116-cmpm
117-ncapox3
118-vim
119-vime
120-tin3
121-wdep3
122-wcmp3
123-tial12
124-mm2
125-mm2e
126-nild4
127-cmpm2
128-ncapox4
129-vim2
130-vim2e
131-tin4
132-wdep4
133-wcmp4
134-wtial3
135-capild
136-captiw1
137-capm
138-capme
139-mm3
140-mm3e
141-nild5
142-cmpm3
143-ncapox5
144-vim3
145-vim3e
146-tin5
147-wdep5
148-wcmp5
149-wtial4
150-capild2
151-captiw2
152-cap2m
153-cap2me
154-mm4
155-mm4e
156-nild6
157-cmpm4
158-ncapox6
159-vim4
160-vim4e
161-wtial5
162-mm5
163-mm5e
164-nfusox
165-nsm
166-nsme
167-ntsd
168-pdm
169-pdme
170-ally
171-hpetest
```

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    retrieved 2026-09-13; tab "Sheet1" lists the 171 steps (number, code and
    description). <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
