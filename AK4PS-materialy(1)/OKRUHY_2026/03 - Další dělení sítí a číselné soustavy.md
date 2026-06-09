---
cislo: 3
nazev: Další dělení sítí a číselné soustavy
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---
## 3) Další dělení sítí a číselné soustavy

### Dělení podle rozsahu (od nejmenší)
**PAN < LAN < CAN < MAN < WAN < GAN**

| Zkratka  | Význam          | Rozsah                                 |
| -------- | --------------- | -------------------------------------- |
| **PAN**  | Personal AN     | jednotky metrů (Bluetooth, USB)        |
| **LAN**  | Local AN        | desítky až stovky metrů (jedna budova) |
| **CAN**  | Campus AN       | stovky m až jednotky km (univerzita)   |
| **MAN**  | Metropolitan AN | jednotky až desítky km (město)         |
| **WAN**  | Wide AN         | desítky km a víc (stát)                |
| **GAN**  | Global AN       | celosvětová                            |
| **SAN**  | Storage AN      | speciální – pro úložiště               |
| **WLAN** | Wireless LAN    | bezdrátová LAN (Wi-Fi)                 |

### Soustředěná vs rozlehlá
- **Soustředěná síť (LAN)**: v daný okamžik se v ní šíří **1 paket**.
- **Rozlehlá síť (WAN)**: v daný okamžik se šíří **více paketů** (víc kanálů, větvení).

### Internet / intranet / extranet
- **Internet** (s velkým I) – celosvětová.
- **internet** (malé i) – libovolné propojení sítí.
- **Intranet** – služby uvnitř organizace.
- **Extranet** – služby pro externí (partneři, dodavatelé).

### VLAN / VPN
- **VLAN** = virtuální lokální síť (logické oddělení v rámci switche).
- **VPN** = virtuální privátní síť (zabezpečený tunel přes Internet).

### Síť s přepojováním paketů
Pakety putují z uzlu na uzel, pokud je volný kanál. Použito v Internetu a propojených LAN.
![[Pasted image 20260523164611.png|677]]
### Číselné soustavy
| Soustava | Označení | Číslice |
|---|---|---|
| Dvojková (binární) | B | 0, 1 |
| Osmičková (oktalová) | O | 0–7 |
| Desítková | – / D | 0–9 |
| Šestnáctková (hex) | H | 0–9, A–F |

**Binární předpony IEC** (mocniny 2): KiB = 1024 B, MiB, GiB.

### Metodika převodu (POZOR – chytácká oblast!)

#### B ↔ O (binární ↔ oktalová)
- **Po trojicích zprava.** Nejvýznamnější bit(y) se doplní zleva **nulami** na trojici.
- Příklad: `1011111000 B` → `001 011 111 000` → `1 3 7 0` → `1370 O`.

#### B ↔ H (binární ↔ hexadecimální)
- **Po čtveřicích zprava.** Nejvýznamnější bity se doplní zleva **nulami** na čtveřici.
- Příklad: `1011111000 B` → `0010 1111 1000` → `2 F 8` → `2F8 H`.
- Zpětně: místo hex číslice napíšu binární čtveřici, **nevýznamné nuly zleva nepíšu**.

#### POZOR – BCD kód (Binary Coded Decimal)
**Když převedeš dekadické číslo pomocí binárních čtveřic, NENÍ to jeho dvojková hodnota, ale BCD kód!**
- Příklad: `245 D`:
  - Jako BCD = `0010 0100 0101` (každá dekadická číslice samostatně do 4 bitů).
  - Jako binární hodnota = `11110101` (skutečná hodnota 245₁₀).
- Otázka typu „převeď 245 do binární pomocí čtveřic" je **chyták** – odpovědí je BCD, ne binární hodnota.

### Převody (procvičovací)
- 11111110₂ = **254**
- 11100000₂ = **224**
- 11000000₂ = **192**
- 11110000₂ = **240**
- 10000000₂ = **128**
- 11111000₂ = **248**
- 183₁₀ = **10110111**₂ (pozor: typo v starém taháku)
- 1101110₂ = **156**₈
- 10010110₂ = **96**₁₆
- 777₈ = **111111111**₂
- AA₁₆ = **10101010**₂
- FF₁₆ = **255**₁₀

### Vzorová odpověď
Sítě dělíme podle rozsahu PAN < LAN < CAN < MAN < WAN < GAN. V LAN se v daném okamžiku šíří jen 1 paket, v WAN více. Důležité jsou taky pojmy intranet (vnitřní) a extranet (pro partnery), a virtualizace VLAN/VPN. Síť pracuje s číselnými soustavami – binární (B), oktalová (O), dekadická, hex (H); binární je základ pro masky a adresy IPv4.


---
