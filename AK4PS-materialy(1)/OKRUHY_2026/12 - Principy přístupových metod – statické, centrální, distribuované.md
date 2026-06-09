---
cislo: 12
nazev: Principy přístupových metod – statické, centrální, distribuované
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 12) Principy přístupových metod – statické, centrální, distribuované

### Co je přístupová metoda
**Přístupová metoda (MAC – Medium Access Control)** = pravidla, podle kterých stanice **získává přístup ke sdílenému médiu** (kabel, kanál). Bez nich by stanice vysílaly přes sebe.

### Dělení
```
                 ┌──── Statické (TDM, FDM)
PŘÍSTUPOVÉ ─────┼──── Centrální (Polling: na výzvu / na žádost)
   METODY       ├──── Distribuované (Token Ring / Newhall)
                 └──── Náhodné (ALOHA, CSMA/CD, CSMA/CA)
```

### 1) Statické přidělování
Kanál je **pevně rozdělen** mezi všechny účastníky – každý má vyhrazenou část kapacity, **ať vysílá nebo ne**.
- **TDM (Time Division Multiplex)** – časové úseky.
- **FDM (Frequency Division Multiplex)** – frekvenční pásma.
- **Výhoda**: bez kolizí, garantovaná kapacita.
- **Nevýhoda**: nevyužitá kapacita když stanice nevysílá (plýtvání).

### 2) Centrální přidělování (Polling)
Jedna **centrální stanice (master)** rozhoduje, kdo bude vysílat.

#### a) Na výzvu (polling)
```
Master ──"Stanice 1, máš data?"──> Stanice 1
              ↑
        Stanice 1 odpoví NE
              ↓
Master ──"Stanice 2, máš data?"──> Stanice 2
              ↑
        Stanice 2 odpoví ANO, vysílá
```
- Master se **periodicky ptá** všech stanic.
- Stanice vysílá jen na vyzvání.

#### b) Na žádost
- Každá stanice má **vyhrazenou malou část kanálu** (žádací slot), kterou žádá master o přidělení vysílacího času.
- Master pak alokuje hlavní část kanálu žadatelům.

#### Vlastnosti centrálního přidělování
- **Bez centrály síť nefunguje** (single point of failure).
- **Kapacitu kanálu přiděluje centrální stanice**.
- Hodí se kde je hierarchie (mainframe + terminály).

### 3) Distribuované přidělování
**Bezkonfliktní současné** přidělování bez centrály. Stanice **kolektivně** rozhodují o přístupu.
![[Pasted image 20260524002452.png]]
#### Newhallův kruh / Token Ring
```
   Pešek (token):  ─[T]─→  [PC1] ─→ [PC2] ─→ [PC3] ─→  zpět [PC1]
```
1. V síti **stále koluje 1 rámec** – buď **token (pešek)** nebo data.
2. PC chce vysílat → počká, až mu přijde token.
3. **Změní příznak peška na data**, rozpojí kruh, odvysílá rámec do kruhu.
4. Cíl rámec přečte, potvrdí (změna příznaku v rámci).
5. Vysílající rámec po obejití kruhu odejme a **vyšle volný pešek dál**.
- Posuvný registr nemusí mít velikost celého rámce.

#### Aktivní retranslace u Wi-Fi
- **Centralizovaná** – 1 prvek (AP) řídí přístup.
- **Distribuovaná** – víc aktivních prvků (mesh).

### Vzorová odpověď
Přístupové metody řídí, jak stanice získávají přístup ke sdílenému médiu. Statické přidělování (TDM, FDM) dá každé stanici pevnou část kapacity – bez kolizí, ale plýtvá. Centrální přidělování má master, který se ptá (polling na výzvu) nebo přiděluje na žádost stanic – bez mastera síť nefunguje. Distribuované přidělování pracuje bez centrály – nejznámější je Newhallův kruh / Token Ring, kde po kruhu cirkuluje token a jen jeho držitel smí vysílat.

---
