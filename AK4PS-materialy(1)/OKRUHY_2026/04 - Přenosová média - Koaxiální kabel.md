---
cislo: 4
nazev: Přenosová média. Koaxiální kabel
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 4) Přenosová média. Koaxiální kabel

### Druhy přenosových médií
| Druh                     | Příklad                     | Signál            |
| ------------------------ | --------------------------- | ----------------- |
| **Metalické (drátové)**  | koaxiál, kroucená dvojlinka | elektrický        |
| **Optické**              | optické vlákno              | optický (světlo)  |
| **Vzdušné (bezdrátové)** | Wi-Fi, mikrovlnný spoj      | elektromagnetický |

### Koaxiální kabel – konstrukce (zevnitř)
```
┌──────────────────────────────────────┐
│  Plášť (izolační)                    │
│  ┌────────────────────────────────┐  │
│  │  Stínění (vodivý oplet/fólie)  │  │
│  │  ┌──────────────────────────┐  │  │
│  │  │  Dielektrikum (izolant)  │  │  │
│  │  │  ┌────────────────────┐  │  │  │
│  │  │  │  Vnitřní vodič     │  │  │  │
│  │  │  └────────────────────┘  │  │  │
│  │  └──────────────────────────┘  │  │
│  └────────────────────────────────┘  │
└──────────────────────────────────────┘
```
Pořadí: **vnitřní vodič → dielektrikum → vodivý oplet/stínění → plášť**.

### Parametry
- **Dobré přenosové vlastnosti do**: ~**1 GHz**.
- **V základním pásmu** přenáší: **pouze 1 signál**.
- **Impedance pro TV**: **75 Ω**.
- **Impedance pro Ethernet a Wi-Fi**: **50 Ω**.
- **Jednotka impedance**: **ohm (Ω)**.

### Stínění
- Vodivý oplet, hliníková fólie, nebo kombinace.
- Lze **uzemnit** – ochrana proti EMI/EMS.
- **EMI** = vyzařování rušení (Electromagnetic Interference).
- **EMS** = odolnost vůči rušení (Electromagnetic Susceptibility).

#### EMI vs EMS — dva směry stejného problému 📡

> **EMI = co kabel ZAŘVE do okolí** (kolik ven vyzařuje)
> **EMS = co kabel SNESE od okolí** (jak je odolný proti rušení zvenku)

| Zkratka | Anglicky | Česky | Co měří |
|---|---|---|---|
| **EMI** | Electro**M**agnetic **I**nterference | Elektromagnetické **rušení** (vyzařování) | Kolik kabel **vysílá ven** a ruší ostatní (rádio, TV, jiné kabely) |
| **EMS** | Electro**M**agnetic **S**usceptibility | Elektromagnetická **odolnost / náchylnost** | Kolik rušení kabel **snese zvenku**, aniž by signál zkresloval |

**Mnemo:**
- **EM**I = **I** jako **„Issue"** → problém, co posílám ven do světa
- **EM**S = **S** jako **„Snesu"** → kolik snesu zvenku

**Praktický příklad — stínění zlepšuje OBOJÍ:**
- Stínění drží signál uvnitř → **nižší EMI** (kabel neruší okolí)
- Stínění odráží vnější rušení → **vyšší EMS** (kabel je odolnější)
- Proto v průmyslových halách (motory, frekvenční měniče) **musí být STP/S/FTP**, ne UTP.

**Pozor na chyták:** Optické vlákno (FO) je **IMUNNÍ vůči EMI/EMS** — světlo se elektromagneticky nedá rušit. Otázka „FO je náchylné na EMS" = NEPRAVDA.

### VF technika
- **Vodiče se postřibřují** ve VF technice → snížení oxidace, lepší vodivost, menší impedance.
- **Skin efekt** – při vyšších frekvencích proud teče po povrchu vodiče.

### Vzorová odpověď
Přenosová média jsou metalická, optická a vzdušná. Koaxiální kabel má 4 vrstvy (vnitřní vodič – dielektrikum – stínění – plášť), funguje dobře do 1 GHz, v základním pásmu nese jen 1 signál. Impedance pro TV je 75 Ω, pro datové sítě (Ethernet 10BASE2/5) 50 Ω. Stínění chrání před EMI/EMS, dá se uzemnit. Dnes se v LAN nepoužívá, vytlačila ho kroucená dvojlinka.

---
