---
cislo: 28
nazev: Propojování sítí – kolizní doména, broadcastová doména, repeater, hub, bridge, switch
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 28) Propojování sítí – kolizní doména, broadcastová doména, repeater, hub, bridge, switch

### Kolizní doména
**Kolizní doména** = část sítě, ve které se mohou **kolize na médiu navzájem ovlivnit**. Tj. když 2 stanice v této doméně vysílají současně, nastane kolize.
- V plně-duplexním režimu (switch) **neexistují kolize** → každý port switche je vlastní kolizní doména s rozměrem 1 zařízení.
- V polo-duplexním režimu (hub, koaxiál) je celý segment 1 kolizní doména.

### Broadcastová doména
**Broadcastová doména** = část sítě, ve které se rozšíří **broadcast (FF:FF:FF:FF:FF:FF)**.
- Broadcast přechází switche, ale **ne routery**.
- VLAN dělí broadcastovou doménu logicky.

### Repeater (L1 – fyzická vrstva)
**Funkce**: zesiluje a regeneruje signál na médiu (proti útlumu).

#### Vlastnosti
- **2 porty** (in / out).
- **Nepracuje s přístupovými metodami** – nezná rámce.
- **Nedělí kolizní doménu** ani broadcastovou.
- Prodlužuje dosah segmentu.

```
[PC]────[REPEATER]────────[PC]
       (vše = 1 kolizní + 1 broadcast doména)
```

### Hub (L1 – fyzická vrstva)
**Funkce**: víceportový repeater. Co přijde na 1 port, vyšle na **všechny ostatní porty**.

#### Vlastnosti
- Více portů (4, 8, 16, 24…).
- Pracuje v **polo-duplexu** (poslouchá při vysílání kvůli CSMA/CD).
- **Nedělí kolizní doménu** – všichni připojení jsou v 1 kolizní doméně.
- **Nedělí broadcastovou doménu**.
- Dnes již nepoužívá se, vytlačil ho switch.

```
       [HUB]
       /│ │ \
    PC1 PC2 PC3 PC4
   (vše 1 kolizní + 1 broadcast doména)
```

### Bridge (L2 – linková vrstva)
**Funkce**: spojuje 2 (nebo víc) segmenty na L2; **odděluje kolizní domény** mezi segmenty, ale broadcastovou ne.

#### Vlastnosti
- Pracuje s **MAC adresami**.
- Učí se MAC adresy na portech (MAC tabulka).
- **Dělí kolizní doménu** – každý port = vlastní kolizní doména.
- **Nedělí broadcastovou doménu** – broadcast přechází.
- Dnes je v podstatě nahrazený switchem (bridge = 2portový switch).

### Switch (L2 – linková vrstva)
**Funkce**: vícebodový bridge – víceportové zařízení, které **přepíná rámce mezi porty** podle MAC.

#### Vlastnosti
- Více portů (typicky 8, 16, 24, 48).
- **Dělí kolizní doménu**: každý port = vlastní kolizní doména (typ. 1 zařízení).
- **Nedělí broadcastovou doménu**: broadcast jde na všechny porty.
- Plný duplex – bez kolizí.
- Pracuje s **MAC tabulkou** (přiřazení MAC ↔ port).
- VLAN umožňuje logické dělení broadcastové domény.

```
          [SWITCH]
       /│ │ │ │ \
    PC1 PC2 PC3 PC4
    
    Kolizní domény: PC1, PC2, PC3, PC4 – KAŽDÝ ZVLÁŠŤ (4 domény).
    Broadcastová doména: VŠICHNI dohromady (1 doména).
```

### Souhrnná tabulka
| Zařízení | OSI vrstva | Dělí kolizní doménu? | Dělí broadcastovou doménu? |
|---|---|---|---|
| Repeater | 1 | NE | NE |
| Hub | 1 | NE | NE |
| Bridge | 2 | ANO | NE |
| Switch | 2 | ANO | NE |
| **Router** | **3** | **ANO** | **ANO** |

### Spanning Tree (STP)
V přepínané síti **nesmí vzniknout kruh** (smyčka) – jinak broadcast bouře. Redundantní cesty se vypínají pomocí **STP (IEEE 802.1D)**, dnes RSTP/MSTP.

### Kaskáda u 10BASE-T – pravidlo 5-4-3
**Klíčové pravidlo pro Ethernet 10BASE-T/2/5 s opakovači (huby):**

| Číslo | Co znamená |
|---|---|
| **5** | **max 5 segmentů** mezi dvěma nejvzdálenějšími stanicemi |
| **4** | **max 4 opakovače (huby)** mezi nimi |
| **3** | **max 3 segmenty smí být „osídlené"** (s koncovými stanicemi) – zbylé 2 jsou jen propojovací (link segments) |

```
[PC]─seg1─[HUB]─seg2─[HUB]─seg3─[HUB]─seg4─[HUB]─seg5─[PC]
   ↑osídl.   link        osídl.       link       ↑osídl.
   (3 osídlené segmenty, 2 propojovací, 4 huby celkem, 5 segmentů)
```

- **Max počet switchů** v kaskádě: **~4** (logická hranice kvůli STP convergence + latency).
- Pozor: pravidlo 5-4-3 platí jen pro **CSMA/CD s opakovači** (huby). Switche pravidlo neřeší (full duplex, bez kolizí).

### Vzorová odpověď
Kolizní doména je část sítě, kde se kolize navzájem ovlivňují; broadcastová doména je část, kde se rozšíří broadcastový rámec. Repeater a hub jsou L1 zařízení – jen regenerují signál, nedělí kolizní ani broadcastovou doménu. Bridge a switch jsou L2 – pracují s MAC adresami, dělí kolizní doménu (každý port = vlastní), ale ne broadcastovou. Switch je vícebodový bridge s plným duplexem. STP zabraňuje smyčkám v přepínané síti.

---
