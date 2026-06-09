---
cislo: 16
nazev: Datagramová služba a virtuální spoj
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 16) Datagramová služba a virtuální spoj

### Dva základní způsoby přepojování paketů na L3
Když chceme přenést delší zprávu, rozdělíme ji na **pakety**. Jak se pakety dostanou do cíle? Dvě filozofie:

### 1) Datagramová služba (nespojovaná)
**Každý paket = samostatný datagram** s úplnou cílovou adresou; směruje se nezávisle.

```
    Zpráva: [A][B][C][D]
    A pošlu jednou cestou
    B pošlu jinou cestou (mezitím se cesta změnila)
    C může dorazit dřív než B
    → cíl musí přeskládat
```

#### Vlastnosti
- **Bez navazování spojení** – jen pošlu a uvidíme.
- Každý paket má **cílovou + zdrojovou adresu** a další pomocné info.
- Pakety mohou jít **různými cestami** (dynamické směrování).
- Pakety mohou dorazit **v jiném pořadí** než byly odeslány.
- Pakety se mohou ztratit – odesílatel se to nedozví, pokud na to nedohlíží vyšší vrstva.

#### Výhody
- **Síť se nezatěžuje servisními pakety** (žádné navazování, žádné ACK na L3).
- **Robustní** – při výpadku linky se pakety přesměrují.
- Flexibilní – dynamické směrování.

#### Nevýhody
- **Bez garance pořadí**.
- Bez garance doručení.
- Vyšší vrstva (TCP) musí dohlédnout.

#### Příklad
- **IP** v Internetu.
- **IPX** v Novell NetWare.
- **UDP** taky nespojovaná (i když na L4).

### 2) Virtuální spoj (spojovaná služba)
**Nejdřív se naváže virtuální okruh** mezi zdrojem a cílem, **všechny pakety jdou stejnou cestou**.

```
1. SETUP: A vyjedná cestu A → R1 → R2 → R3 → B, dostane VC ID = 42
2. Data: pakety nesou jen [VC=42][data], žádné adresy
   R1 ví: VC 42 → další uzel R2
   R2 ví: VC 42 → další uzel R3
   ...
3. RELEASE: po skončení se virtuální spoj uvolní.
```

#### Vlastnosti
- Před přenosem se naváže virtuální spoj (cesta).
- Paket je opatřen pouze **identifikátorem virtuálního spoje (VCI)**, ne plnou adresou.
- Všechny pakety jdou **stejnou cestou**.
- Po skončení se spoj **uvolní**.

#### Výhody
- **Data dorazí ve správném pořadí** (jdou jednou cestou FIFO).
- Menší hlavičky paketů (jen VCI místo plné adresy).
- Lze garantovat QoS (rezervace zdrojů na cestě).

#### Nevýhody
- Zátěž navázáním a uvolněním spoje.
- Při výpadku linky → spoj padá, nutno znovu navázat.

#### Příklad
- **ATM** (Asynchronous Transfer Mode).
- **Frame Relay**, X.25.
- **MPLS** (label switching, koncepčně VC).
- **TCP** (logicky spojovaný i když běží přes IP datagramy).

### Srovnání
| Vlastnost | Datagramová | Virtuální spoj |
|---|---|---|
| Navázání spojení | NE | ANO |
| Adresa v paketu | plná cílová | VCI |
| Cesta paketů | různá | stejná |
| Pořadí v cíli | nezaručené | zaručené |
| Servisní pakety | minimální | setup + release |
| Reakce na výpadek | přesměruje | padá, nový setup |

### Vzorová odpověď
Na síťové vrstvě se přepojuje dvojím způsobem. Datagramová služba pakety posílá nezávisle (každý má plnou adresu, může jít jinou cestou, dorazit v jiném pořadí) – nepotřebuje navazování, je robustní, ale bez garancí; tak funguje IP. Virtuální spoj nejdřív navazuje cestu, pak pakety nesou jen identifikátor VCI a jdou stejnou cestou ve správném pořadí – nutný setup/release; tak fungovalo X.25, ATM, dnes MPLS.

---
