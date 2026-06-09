---
cislo: 30
nazev: Ethernet – základní parametry
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 30) Ethernet – základní parametry

### Co je Ethernet
**Ethernet** = nejrozšířenější standard LAN. Definuje **fyzickou a linkovou vrstvu**.
- Vyvinul **Xerox PARC** (Bob Metcalfe) v 70. letech.
- Standardizován jako **IEEE 802.3** (1983).
- Dnes prakticky synonymum pro drátový LAN.

### Klíčové parametry
| Parametr | Hodnota |
|---|---|
| **Standard** | **IEEE 802.3** |
| **Přístupová metoda** | **CSMA/CD** (do 1 Gb/s; pak full-duplex) |
| **Logická topologie** | **sběrnice** (BUS) |
| **Fyzická topologie dnes** | **hvězda, strom** |
| **Adresování** | **MAC adresy 48 bitů** |
| **Médium** | TP (BaseT), FO (BaseS/L/F/E), historicky koax |
| **Rychlosti** | 10 Mb/s, 100 Mb/s, 1 / 2,5 / 5 / 10 / 25 / 40 / 100 / 400 Gb/s |

### MAC adresa
- **Délka: 6 byte = 48 bit**.
- Zápis: hex po bytech, oddělené dvojtečkami nebo pomlčkami: `00:1A:2B:3C:4D:5E`.
- **Prvních 3 byte** = **OUI** (Organizationally Unique Identifier) – výrobce NIC.
- **Posledních 3 byte** = sériové číslo NIC od daného výrobce.
- **Globálně unikátní** (přiřazuje IEEE).
- **Broadcast MAC**: `FF-FF-FF-FF-FF-FF`.
- **Multicast MAC**: `01-00-5E-XX-XX-XX` (pro IPv4 multicast).
- **U/L bit** (Universal/Local) – druhý nejméně významný bit prvního bajtu.
- **I/G bit** (Individual/Group) – nejméně významný bit prvního bajtu (0 = unicast, 1 = multi/broadcast).

### Označení Ethernetu (např. 100BASE-TX)
```
   100 BASE - TX
    │   │     │
    │   │     └── Médium: T = Twisted pair, F = Fiber, S = Short FO,
    │   │                 L = Long FO, E = Extended FO, B = Bidirectional
    │   └── Pásmo: BASE = baseband, BROAD = broadband
    └── Rychlost v Mb/s
```

| Označení | Médium | Rychlost |
|---|---|---|
| **BaseT** | kroucená dvojlinka (TP) | – |
| **BaseS** | short-range FO | – |
| **BaseL** | long-range FO | – |
| **BaseF, BaseE** | FO | – |
| **BaseBX** | bidirectional FO (1 vlákno) | – |

### Rychlé krátké odpovědi (časté otázky v taháku)
| Otázka | Odpověď |
|---|---|
| **Jak je označen Ethernet s kroucenou dvojlinkou?** | **BaseT** (např. 10BASE-T, 100BASE-TX, 1000BASE-T) |
| **Jak je označen Ethernet s optickými vlákny?** | **BaseF, BaseS, BaseL, BaseE, BaseBX** (např. 100BASE-FX, 1000BASE-SX, 10GBASE-LR) |
| **Co znamená písmeno T v 10BASE-T?** | Twisted pair (kroucená dvojlinka) |
| **Co znamená písmeno F v 10BASE-F?** | Fiber (optické vlákno) |
| **Co znamená písmeno S v 1000BASE-SX?** | Short wavelength (krátkovlnný FO, typ. 850 nm multi-mode) |
| **Co znamená písmeno L v 1000BASE-LX?** | Long wavelength (dlouhovlnný FO, typ. 1310 nm single-mode) |
| **Co znamená BASE?** | Baseband (základní pásmo, bez modulace na nosnou) |

### Vývoj Ethernetu
**Posloupnost**: Ethernet (DIX) → IEEE 802.3 → Ethernet II → upravený IEEE 802.3 (s 802.2 LLC).
- **Ethernet II** a **IEEE 802.3** se liší **formátem rámce** (Type vs Length).
- **Dnes preferovaný formát**: kombinovaný **IEEE 802.3 + 802.2 LLC** nebo Ethernet II.

### Média, která Ethernet NEpoužívá
**Rádiové vlny** (to je Wi-Fi). Ethernet je drátový (nebo přes FO).

### Rychlost, kterou Ethernet NEpoužívá
**1 Mb/s** – nikdy nebyla v Ethernetu standardizována.

### Vzorová odpověď
Ethernet je nejrozšířenější LAN standard, definovaný IEEE 802.3. Vyvinul ho Xerox v 70. letech. Používá přístupovou metodu CSMA/CD do 1 Gb/s (nad to plný duplex), logickou topologii sběrnici (i když fyzicky je dnes hvězda nebo strom). MAC adresa má 48 bitů – první 3 byte identifikují výrobce (OUI). Broadcast je FF:FF:FF:FF:FF:FF. Standardní označení např. 100BASE-TX: 100 Mb/s, baseband, kroucená dvojlinka. Ethernet má dva rámce: Ethernet II (s Type) a IEEE 802.3 (s Length + 802.2 LLC).

---
