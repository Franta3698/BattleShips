---
cislo: 6
nazev: Optický kabel
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 6) Optický kabel

### Konstrukce optického vlákna
```
        ┌───────────────────────────────────┐
        │  Obal (neprůhledný plast)         │
        │  ┌─────────────────────────────┐  │
        │  │  Plášť (světlovod, n₂)      │  │
        │  │  ┌───────────────────────┐  │  │
        │  │  │  Jádro (n₁ > n₂)      │  │  │
        │  │  └───────────────────────┘  │  │
        │  └─────────────────────────────┘  │
        └───────────────────────────────────┘
```
- **Jádro** – sklo nebo plast (sklo má lepší přenosové vlastnosti).
- **Plášť** – sklo nebo plast, s **nižším indexem lomu** než jádro.
- **Obal** – neprůhledný barevný plast (mechanická ochrana, identifikace).

### Princip přenosu – totální odraz
Paprsek vstoupí do jádra pod úhlem, který je **menší nebo roven kritickému úhlu** → paprsek se totálně odráží od pláště a šíří se jádrem. Větší úhel = paprsek opustí jádro do pláště → ztráta.

### Index lomu
- **n = c / v** (rychlost ve vakuu / rychlost v materiálu).
- **Numerická apertura NA = n·sin(φ)** – míra schopnosti vlákna „chytit" světlo.

### Typy vláken
| Typ | Označení | Jádro | Zdroj | Vzdálenost |
|---|---|---|---|---|
| **Single-mode (jednovidové)** | **9/125** μm | malé | laserová dioda | velké, **přes 100 km** |
| **Multi-mode (mnohovidové)** | **62,5/125** μm (nebo 50/125) | velké | LED s clonou | krátké |

### Skoková vs průběžná změna indexu lomu
- **Skoková (step-index)**: index lomu mezi jádrem a pláštěm se mění skokem. Lze u single-mode i multi-mode.
- **Průběžná / gradient (graded-index)**: index lomu se v jádře plynule mění – paprsky uprostřed jdou pomaleji, paprsky u kraje rychleji → menší vidová disperze. **Pouze u multi-mode**, **lepší vlastnosti** než step-index multi-mode.

![[Pasted image 20260523193131.png]]
![[Pasted image 20260523193142.png]]
![[Pasted image 20260523193233.png]]

### Vlnové délky
Používané: **850 nm, 1300 nm, 1310 nm, 1550 nm**.

### Útlum
- **Nejkvalitnější single-mode FO**: **0,2 dB/km**.
- **Vidová disperze** – rozdíl mezi rychlostí různých světelných paprsků (rozšíření pulzu). Jednotka: **ns/km**.
- **Útlum vlivem nečistot v jádře**: rozptyl, absorpce.
- **Útlum vlivem mechaniky**: mikro-ohyby, makro-ohyby.

### Spojování FO
- **Svařením** – nejlepší (nejnižší ztráty).
- Slepením.
- Mechanickými spojkami.
- Spoj **lepený NENÍ lepší** než svařený (častá chytácká otázka).

### WDM/DWDM
**WDM (Wavelength Division Multiplex)** – na jednom vláknu více vlnových délek současně → každá nese samostatný signál.
- **WDM umožňuje**: plně-duplexní provoz, více vlnových délek, simplexní provoz.
- **DWDM** (Dense WDM) – max **160 vlnových délek** na vlákno.
- **Max rychlost na 1 vlákně na 1 vlnové délce**: **100 Gb/s**.
- **U FO se běžně používá plný duplex** (1 vlákno tam, 1 vlákno zpět; nebo WDM na 1 vlákně).

### Konektory FO
**Patří sem**: FC, ST, SC, E2000, MTRJ.
**NEpatří sem**: RJ-45, RJ-11, BNC (to jsou metalické konektory).

### Přijímač FO
**Fotodetektor → zesilovač → procesor**.

### Odolnost vůči rušení
**FO je IMUNNÍ vůči EMS** (pozor na otočenou otázku „náchylné na EMS" = NEPRAVDA). FO má největší odolnost vůči EMI/EMS ze všech médií.

### Vzorová odpověď
Optický kabel má jádro (větší index lomu n₁), plášť (n₂ < n₁) a ochranný obal. Funguje na principu totálního odrazu. Single-mode (9/125 μm) je s laserovou diodou, pro velké vzdálenosti přes 100 km; multi-mode (62,5/125 μm) je s LED, pro krátké vzdálenosti. Multi-mode existuje ve dvou variantách – step-index a graded-index (gradient je lepší, méně vidové disperze). Používají se vlnové délky 850, 1300, 1310 a 1550 nm. Vlákna se nejlépe spojují svařením. WDM umožňuje více vlnových délek na jednom vlákně, DWDM až 160. FO je imunní vůči EMS.

---
