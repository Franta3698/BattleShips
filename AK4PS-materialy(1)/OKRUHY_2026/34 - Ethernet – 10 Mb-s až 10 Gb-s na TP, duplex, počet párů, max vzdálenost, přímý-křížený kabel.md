---
cislo: 34
nazev: Ethernet – 10 Mb/s až 10 Gb/s na TP, duplex, počet párů, max vzdálenost, přímý/křížený kabel
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 34) Ethernet – 10 Mb/s až 10 Gb/s na TP, duplex, počet párů, max vzdálenost, přímý/křížený kabel

### Tabulka standardů Ethernetu na kroucené dvojlince
| Norma | Rychlost | Pásmo | Páry vodičů | Duplex | Max segment | Min. Cat |
|---|---|---|---|---|---|---|
| **10BASE-T** | 10 Mb/s | baseband | **2 páry** (1,2 + 3,6) | poloduplex / plný | **100 m** | Cat 3 |
| **100BASE-TX** | 100 Mb/s | baseband | **2 páry** (1,2 + 3,6) | poloduplex / plný | **100 m** | Cat 5 |
| **1000BASE-T (1GBASE-T)** | 1 Gb/s | baseband | **4 páry** (všechny 4) | **plný duplex** | **100 m** | Cat 5E |
| **2,5GBASE-T** | 2,5 Gb/s | baseband | 4 páry | plný duplex | 100 m | Cat 5E |
| **5GBASE-T** | 5 Gb/s | baseband | 4 páry | plný duplex | 100 m | Cat 6 |
| **10GBASE-T** | 10 Gb/s | baseband | **4 páry** | **plný duplex** | **100 m** (Cat 6A), 55 m (Cat 6) | Cat 6A |

### Duplex
- **10 Mb/s a 100 Mb/s**: poloduplex i plný duplex (s autonegotiation).
- **1 Gb/s a vyšší**: **vždy plný duplex** (CSMA/CD ztrácí smysl).

### Páry kabelu pro signál
| Norma | Páry pro signál | Páry pro řízení/rezervu |
|---|---|---|
| 10BASE-T | 2 (TX + RX) | 2 nepoužité |
| 100BASE-TX | 2 (TX + RX) | 2 nepoužité |
| 1000BASE-T | **4 (vše duplex)** | – |
| 10GBASE-T | **4 (vše duplex)** | – |

### Přímý a křížený kabel
**Přímý kabel (straight-through)** – vodiče zapojeny **1:1** na obou koncích (T568A↔T568A nebo T568B↔T568B).

**Křížený kabel (crossover)** – TX se kříží s RX na druhém konci.

#### Kdy použít přímý vs křížený (bez autodetekce/Auto-MDIX)
**Stejná skupina zařízení = křížený, různá = přímý.**

#### Skupiny zařízení
| Skupina | Zařízení |
|---|---|
| **A (DTE)** | PC, server, **router** (z hlediska kabeláže patří router do PC skupiny – „end stations") |
| **B (DCE)** | **hub**, **switch** |

> Pozor: **router je formálně DTE** (jako PC) – kříží se s PC.

#### Pravidla zapojení
| Spojení | Kabel |
|---|---|
| PC ↔ switch | **přímý** (A↔B) |
| PC ↔ hub | **přímý** (A↔B) |
| switch ↔ router | **přímý** (B↔A) |
| hub ↔ router | **přímý** (B↔A) |
| **switch ↔ switch** | **křížený** (B↔B) |
| **hub ↔ hub** | **křížený** (B↔B) |
| **switch ↔ hub** | **křížený** (B↔B) |
| **PC ↔ PC** | **křížený** (A↔A) |
| **PC ↔ router** | **křížený** (A↔A) |
| **router ↔ router** | **křížený** (A↔A) |

### Křížení vodičů (T568A vs T568B)
Standardní zapojení barev v RJ-45 podle T568B (běžnější):
| Pin | T568B | T568A |
|---|---|---|
| 1 | Oranžovo-bílá | Zeleno-bílá |
| 2 | Oranžová | Zelená |
| 3 | Zeleno-bílá | Oranžovo-bílá |
| 4 | Modrá | Modrá |
| 5 | Modro-bílá | Modro-bílá |
| 6 | Zelená | Oranžová |
| 7 | Hnědo-bílá | Hnědo-bílá |
| 8 | Hnědá | Hnědá |

**Křížený kabel** = jeden konec T568B, druhý konec T568A.

### Auto-MDIX
Moderní switche/karty mají **Auto-MDIX** – samy detekují, zda je kabel přímý nebo křížený, a přepnou se. **Dnes nemusí řešit, ale ke zkoušce ANO!**

### Vzorová odpověď
Ethernet na kroucené dvojlince používá vždy max 100 m segment. 10BASE-T a 100BASE-TX používají 2 páry a podporují polo i plný duplex, Cat 3 resp. Cat 5 a vyšší. Od 1 Gb/s (1000BASE-T) se používají všechny 4 páry a vždy plný duplex (CSMA/CD ztrácí smysl); 1 Gb/s vyžaduje Cat 5E, 10 Gb/s pak Cat 6A. Kabel je buď přímý (1:1) nebo křížený (TX↔RX přehozené). Pravidlo: stejná skupina zařízení (PC↔PC, switch↔switch) potřebuje křížený, různé skupiny (PC↔switch, switch↔router) potřebují přímý. Router patří kabeláží do PC skupiny (DTE). Moderní zařízení mají Auto-MDIX a poznají kabel samy.

---
