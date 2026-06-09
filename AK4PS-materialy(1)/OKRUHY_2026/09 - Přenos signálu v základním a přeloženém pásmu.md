---
cislo: 9
nazev: Přenos signálu v základním a přeloženém pásmu
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 9) Přenos signálu v základním a přeloženém pásmu

### Definice
- **Základní pásmo (Baseband)** = přenos signálu přímo na médiu **bez přesunu na nosnou frekvenci**. Signál zabírá celé spektrum média.
- **Přeložené pásmo (Broadband)** = signál je **modulován na nosnou vlnu** a přesunut do jiného frekvenčního rozsahu. Na médiu lze vést **víc signálů současně** v různých pásmech.

### Vlastnosti
| Charakteristika | Základní (Baseband) | Přeložené (Broadband) |
|---|---|---|
| Počet signálů na médiu | **1** | **více** (FDM) |
| Modulace | bez nosné | s nosnou (AM/FM/PM) |
| Šíře pásma | celá | jen alokovaný subkanál |
| Příklad | klasický Ethernet (BaseT) | kabelová TV, ADSL, mobilní sítě |

### Modulace v přeloženém pásmu
Tři základní druhy:
- **Amplitudová modulace (AM)** – mění se velikost amplitudy nosné.
- **Frekvenční modulace (FM)** – mění se frekvence nosné.
- **Fázová modulace (PM)** – mění se fáze nosné.
- **QAM** (kvadraturní amplitudově-fázová) – kombinace AM + PM, dnes nejpoužívanější (kabelovky, Wi-Fi, LTE).

### Kódování v základním pásmu
| Kód | Princip | Použití |
|---|---|---|
| **NRZ bipolární** | 0 = nižší úroveň, 1 = vyšší úroveň | COM port |
| **NRZI bipolární** | 0 = beze změny, 1 = změna úrovně | 100BASE-FX |
| **Fázové NRZ (Manchester)** | 1 = sestupná, 0 = vzestupná hrana | **10BASE-T Ethernet** |
| **MLT-3** | tři úrovně, změna při 1 | 100BASE-TX |
| **PAM5** | 5 úrovní amplitudy | 1000BASE-T |
| **4B/5B, 8B/10B** | kódování 4/8 bitů do 5/10 (eliminace DC) | 100BASE-TX, 1000BASE-X |

### Důležitá pravidla
- Přenášený signál by **neměl mít stejnosměrnou složku** (DC) – proto kódování jako Manchester, 8B/10B.
- **Šířka pásma digitálního signálu** se uvádí v **b/s** (bps).
- **Modulační rychlost** v **Baud (Bd)** = počet změn za sekundu = Hz.
- **Přenosová rychlost** v **b/s**.
- **1 Hz teoreticky převede 2 bity/s** (Nyquist).
- **Frekvence pro 1 b/s** = **0,5 Hz**.

### COM port (RS-232)
- Používá **bipolární NRZ**.
- Log. 0 = **+3 až +15 V**.
- Log. 1 = **−3 až −15 V**.

### Druhy přenosu podle směru
| Typ | Popis |
|---|---|
| **Simplex** | jen jedním směrem (vysílač → přijímač) |
| **Poloduplex (Half-duplex)** | oběma směry, ale ne současně |
| **Plný duplex (Full-duplex)** | oběma směry současně |

### Throughput vs goodput
**Kde měříme přenosovou rychlost:**
- **Throughput** = rychlost **na přenosovém médiu** (hrubá – včetně všech hlaviček, ACK, signalizace).
- **Goodput** = rychlost **na úrovni síťové aplikace** (čistá užitečná data).
- **Goodput = throughput − provozní režie** (zřízení relace, potvrzování, zapouzdření hlaviček L2/L3/L4).
- Goodput je vždy **menší než throughput**. U TCP přes Ethernet typicky 90–95 % throughputu.

### Útlum
- Uvádí se v **dB**.
- **dB napětí**: 20·log₁₀(U₂/U₁).
- **dB výkonu**: 10·log₁₀(P₂/P₁).
- **dBm**: 10·log(P [W] / 0,001).
- **Snížení napětí na 50 % = −6 dB**.
- **Snížení napětí na 25 % = −12 dB**.
- **Snížení výkonu na 25 % = −6 dB**.
- **Přeslech (NEXT/FEXT)** = 10·log₁₀(P₁/P₂), uvádí se v dB.

### Vzorová odpověď
V základním pásmu (baseband) přenáším signál přímo, bez modulace, médium nese jen 1 signál – tak funguje Ethernet (10/100 BaseT). V přeloženém pásmu (broadband) signál moduluji na nosnou vlnu a na médium se vejde víc signálů paralelně (FDM) – kabelovka, ADSL, mobilní sítě. Modulace jsou amplitudová, frekvenční a fázová (resp. jejich kombinace QAM). V základním pásmu se používají kódování jako NRZ, NRZI, Manchester (10BASE-T), MLT-3 (100BASE-TX), PAM5 (1GBASE-T) – cíl je odstranit stejnosměrnou složku a umožnit synchronizaci.

---
