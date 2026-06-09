---
cislo: 33
nazev: Ethernet – součásti sítě, zapojení kabeláže se switchem a hubem
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 33) Ethernet – součásti sítě, zapojení kabeláže se switchem a hubem

### Aktivní prvky
| Prvek | Vrstva OSI | Funkce |
|---|---|---|
| **NIC (Network Interface Card)** | 1+2 | rozhraní PC – síť, má MAC adresu |
| **Repeater** | 1 | zesílení signálu |
| **Hub** | 1 | víceportový repeater |
| **Bridge** | 2 | spojení 2 segmentů na L2 |
| **Switch** | 2 | víceportový bridge |
| **Router** | 3 | směrování mezi sítěmi |
| **Gateway** | 7 | překlad mezi neslučitelnými systémy |

### Pasivní prvky
- **Kabely** – TP, FO, koax.
- **Konektory** – RJ-45, FC/ST/SC (FO), BNC (koax).
- **Patch panel** – přepojovací bod v RACKu.
- **Zásuvky** – v místnosti pro zapojení PC.
- **RACK** – datový rozvaděč.
- **Spojky, prodlužky**.

### Zapojení se switchem
```
[ PC1 ]──TP──┐
[ PC2 ]──TP──┼──[ SWITCH ]──TP──[ ROUTER ]──→ Internet
[ PC3 ]──TP──┘
```

#### Vlastnosti
- **Hvězdicová topologie**.
- Každé PC má **vlastní spoj** se switchem.
- **Plný duplex**: PC i switch posílají současně.
- Switch **udržuje MAC tabulku** a přepíná rámce jen na cílový port (unicast).
- **Bez kolizí** – každý port = vlastní kolizní doména.
- **Broadcast** se rozšíří na všechny porty.

### Zapojení s hubem
```
[ PC1 ]──TP──┐
[ PC2 ]──TP──┼──[ HUB ]──TP──[ ROUTER ]──→ Internet
[ PC3 ]──TP──┘
```

#### Vlastnosti
- **Hvězdicová topologie fyzicky**, ale **sběrnicová logicky**.
- Hub vysílá příchozí rámec na **všechny porty**.
- **Polo-duplex** – PC i hub se musí střídat.
- **Kolize** – všichni v 1 kolizní doméně.
- **CSMA/CD** se uplatňuje.
- **Stejná propustnost se dělí** mezi všechny stanice.

### Rozdíl switch vs hub
| Vlastnost | Hub | Switch |
|---|---|---|
| OSI vrstva | 1 | 2 |
| Adresace | – | MAC |
| Duplex | polo | plný |
| Kolize | ANO | NE |
| Šíření rámce | všem | jen cílovému portu |
| Kolizních domén | 1 | tolik, kolik portů |
| Broadcastových domén | 1 | 1 (pokud bez VLAN) |

### Strukturovaná kabeláž v budově
```
   [Páteřní switch v hlavním RACKu]
              │ (FO uplink)
              │
   [Patrový switch (RACK na patře)]
              │ (TP do patch panelu)
              │
   [Patch panel] ──pevný kabel── [zásuvka v místnosti] ──patch── [PC]
```

### Vzorová odpověď
Ethernet síť se skládá z aktivních prvků (NIC, hub, switch, router) a pasivních (kabely, patch panel, RACK, zásuvky, konektory). Se switchem je topologie hvězdicová, plně-duplexní, bez kolizí – switch podle MAC tabulky přepíná rámec jen na cílový port. S hubem je topologie fyzicky hvězda, ale logicky sběrnice – hub flooduje na všechny porty, polo-duplex, kolize, uplatňuje se CSMA/CD. Switch nahradil hub kvůli rychlosti a absenci kolizí. Ve strukturované kabeláži vede pevný kabel od patch panelu v RACKu do zásuvky v místnosti, PC se připojí patch kabelem.

---
