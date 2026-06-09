---
cislo: 7
nazev: Komunikace vzduchem – WLAN, IEEE 802.11, Wi-Fi, pásma, standardy
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 7) Komunikace vzduchem – WLAN, IEEE 802.11, Wi-Fi, pásma, standardy

### WLAN, Wi-Fi, IEEE 802.11
- **WLAN** = obecně bezdrátová lokální síť.
- **IEEE 802.11** = standard pro bezdrátové LAN (od IEEE).
- **Wi-Fi** = **pouze značka/nálepka** pro zařízení, která splňují 802.11 + vzájemnou kompatibilitu.
- Nálepku Wi-Fi uděluje **Wi-Fi Alliance** (sdružení výrobců, certifikační autorita).
- Označení „bezdrátový Ethernet" je **NESPRÁVNÉ** (Ethernet má 802.3, Wi-Fi 802.11; jiný standard, jiné rámce).

### Licencovaná a bezlicenční pásma
| Typ | Pásma | Použití |
|---|---|---|
| **Licencovaná** | 3,5; 26; 28 GHz (+ 4, 6, 7, 8, 11, 13, 15, 18, 23 GHz) | mikrovlnné spoje, mobilní operátoři |
| **Bezlicenční** | 2,4; 5; 6; 10,5 GHz | Wi-Fi, Bluetooth, IoT |

- **Licencovaná pásma**: vyžadují přidělení od ČTÚ za poplatek; uživatel má garantovanou ochranu před rušením.
- **Bezlicenční pásma**: volně využitelná v rámci tzv. **generální licence** ČTÚ.

### Generální licence (ČR)
Souhrnný dokument ČTÚ povolující používat bezlicenční pásma za stanovených podmínek (max. vyzářený výkon, EIRP, povolené modulace, šířka kanálu…). Pro 2,4 GHz Wi-Fi: **max 100 mW EIRP** (20 dBm).

### Standardy IEEE 802.11 a rychlosti
| Standard | Pásmo | Max. teor. rychlost | Označení |
|---|---|---|---|
| **802.11a** | 5 GHz | 54 Mb/s | – |
| **802.11b** | 2,4 GHz | 11 Mb/s | – |
| **802.11g** | 2,4 GHz | 54 Mb/s | – |
| **802.11n** | 2,4 + 5 GHz | 600 Mb/s | Wi-Fi 4 |
| **802.11ac** | 5 GHz | 6,77 Gb/s | Wi-Fi 5 |
| **802.11ax** | 2,4 + 5 + 6 GHz | 9,6 Gb/s | **Wi-Fi 6 / 6E** |
| **802.11be** | 2,4 + 5 + 6 GHz | 46 Gb/s | **Wi-Fi 7** |

### Kompatibilita
- **802.11g** je zpětně kompatibilní s **802.11b**.
- **802.11n** funguje v 2,4 i 5 GHz – kompatibilita s a/b/g podle pásma.

### Pásmo 2,4 GHz v ČR
- Rozděleno na **13 kanálů** šířky 20 MHz.
- **Nepřekrývající se kanály v ČR: 1, 7, 13** (v USA bývají 1, 6, 11).
- **Maximální počet vzájemně se nerušících sítí: 3** (na 1, 7 a 13).
- **Max vyzářený výkon**: **20 dBm = 100 mW**.

### Pásmo 5 GHz
- Rozděleno na **19 subpásem**.
- V subpásmu 5,470–5,725 GHz: **11 nepřekrývajících se kanálů**.
- **Min. přenos antény**: 1000 mW (1 W).

### Pásmo 6 GHz
- **59 kanálů**.
- Využívá ho 802.11ax (Wi-Fi 6E) a 802.11be (Wi-Fi 7).

### Vzorová odpověď
WLAN je obecná bezdrátová síť, standardizovaná jako IEEE 802.11. Wi-Fi je jen certifikační značka, kterou uděluje Wi-Fi Alliance. Pásma jsou licencovaná (3,5/26/28 GHz a další – pro mikrovlnné spoje, mobilní operátory) a bezlicenční (2,4/5/6/10,5 GHz – Wi-Fi). Bezlicenční využití kryje generální licence ČTÚ s omezením výkonu (max 100 mW v 2,4 GHz). Standardy 802.11 a-g pracují do 54 Mb/s, novější n/ac/ax/be jdou až do desítek Gb/s a využívají i 6 GHz pásmo. V 2,4 GHz jsou v ČR nepřekrývající se kanály 1, 7, 13.

---
