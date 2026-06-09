---
cislo: 31
nazev: Ethernet – zasílání unicast, multicast, broadcast a vývoj
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 31) Ethernet – zasílání unicast, multicast, broadcast a vývoj

### Tři typy doručování rámců
Podle cílové MAC adresy se zpráva doručí jinak:

#### 1) Unicast – jednomu konkrétnímu příjemci
- Cílová MAC = MAC konkrétní stanice.
- Switch ji **doručí jen na port, kde cílová stanice je** (díky MAC tabulce).
- Pokud switch MAC nezná → **flooduje** (pošle na všechny porty kromě příchozího).
- **Standardní doručování** většiny rámců.

#### 2) Multicast – skupině přihlášených příjemců
- Cílová MAC: **01-00-5E-XX-XX-XX** (IPv4 multicast mapped) nebo **33-33-XX-XX-XX-XX** (IPv6 multicast mapped).
- Switch ji default **flooduje na všechny porty** (ne plnohodnotné multicast routing).
- **IGMP snooping** umožňuje switchi sledovat IGMP zprávy a posílat multicast jen na porty, kde jsou členové skupiny.

#### 3) Broadcast – všem ve stejné broadcastové doméně
- Cílová MAC: **FF-FF-FF-FF-FF-FF**.
- Switch **flooduje na všechny porty** kromě příchozího.
- **Nepřejde přes router**.
- Použití: ARP, DHCP discover, IPv4 omezený broadcast.

### Vývoj Ethernetu (historicky)
| Generace | Rychlost | Médium | Rok | Standard |
|---|---|---|---|---|
| Experimental Ethernet | 2,94 Mb/s | koax | 1973 | – (Xerox) |
| **Ethernet I (DIX)** | **10 Mb/s** | koax | 1980 | DIX |
| **IEEE 802.3** | **10 Mb/s** | koax | 1983 | IEEE 802.3 |
| **10BASE-T** | 10 Mb/s | TP | 1990 | IEEE 802.3i |
| **Fast Ethernet (100BASE-TX)** | **100 Mb/s** | TP / FO | 1995 | IEEE 802.3u |
| **Gigabit Ethernet (1000BASE-T)** | **1 Gb/s** | TP / FO | 1999 | IEEE 802.3ab |
| **10 Gigabit Ethernet** | **10 Gb/s** | TP / FO | 2002+ | IEEE 802.3ae |
| **2,5/5 GBASE-T** | 2,5 / 5 Gb/s | TP (Cat 5e/6) | 2016 | IEEE 802.3bz |
| **25/40/100/400 GbE** | 25–400 Gb/s | FO | 2010+ | různé |

### Vlastnosti vývoje
- **Rychlost narostla 10 000×** (z 10 Mb/s na 100 Gb/s a víc).
- **Médium se mění**: koax → TP → FO.
- **Topologie**: sběrnice → hvězda/strom.
- **Duplex**: poloduplex (CSMA/CD) → plný duplex (switch).

### Kódování podle rychlosti
| Rychlost | Kódování |
|---|---|
| 10 Mb/s | **Manchester (fázové NRZ)** |
| 100 Mb/s | **4B/5B + MLT-3** nebo NRZI |
| 1 Gb/s | **PAM5** (Cat 5e+) nebo **8B/10B** (FO) |
| 10 Gb/s | různé (např. 64B/66B) |

### Doba odvysílání 1 bitu
| Rychlost | Čas 1 bitu |
|---|---|
| 10 Mb/s | **100 ns** |
| 100 Mb/s | **10 ns** |
| 1 Gb/s | **1 ns** |
| 10 Gb/s | **0,1 ns** |

### Vzorová odpověď
Ethernet zasílá tři typy rámců. Unicast míří jednomu příjemci, switch ho podle MAC tabulky doručí jen na správný port (neznámou MAC flooduje). Multicast má adresu 01-00-5E-..., switch ho běžně flooduje, ale s IGMP snoopingem ho posílá jen členům skupiny. Broadcast (FF-FF-FF-FF-FF-FF) jde všem v broadcastové doméně – switch ho flooduje, router nepropustí. Vývoj Ethernetu šel z 10 Mb/s na koaxu (1980, DIX) přes Fast Ethernet 100 Mb/s (1995), Gigabit Ethernet (1999) až dnes po 400 GbE. Změna média koax → TP → FO, topologie sběrnice → hvězda, poloduplex → plný duplex se switchem.

---
