---
cislo: 5
nazev: Kroucená dvojlinka a strukturovaná kabeláž
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 5) Kroucená dvojlinka a strukturovaná kabeláž

### Co to je
**Kroucená dvojlinka (Twisted Pair, TP)** – pár (nebo více párů) vodičů zkroucených dohromady; standardní médium pro Ethernet v LAN.

### Klíčové parametry
- **Kabel pro LAN má 8 vodičů** uspořádaných do **4 párů**.
- **Impedance**: **100 Ω**.
- **Konektor**: **RJ-45** (8 kontaktů).
- **Maximální rychlost**: **10 Gb/s** (Cat 6a/7), Cat 8 pak až 40 Gb/s.
- **Maximální délka segmentu**: **100 m**.

### Proč jsou páry kroucené
1. **Minimalizují přeslechy** mezi páry (crosstalk).
2. **Zvyšují odolnost proti EMS** (vnější rušení).
3. **Snižují ztráty** z kapacitního odporu.

### Typy TP podle stínění
| Označení | Stínění |
|---|---|
| **UTP** | Unshielded – nestíněný |
| **FTP / F/UTP** | Foiled – celkové stínění fólií |
| **STP / U/FTP** | každý pár stíněn fólií |
| **S/FTP** | každý pár fólie + celek opletení/fólie |

- **UTP** – ohebnější, levnější, hůře odolný EMS.
- **STP/S/FTP** – odolnější vůči EMI/EMS, méně ohebné, dražší.

### Konektory RJ-x
| Konektor | Počet kontaktů | Použití |
|---|---|---|
| RJ-10 | 4 | sluchátka |
| RJ-11 | 6 | telefon (2-pin) |
| RJ-12 | 6 | telefon (6-pin) |
| **RJ-45** | **8** | **Ethernet LAN** |
| RJ-48 | 10 | T1 linky |

### Strukturovaná kabeláž
**Strukturovaná kabeláž** = jednotná univerzální kabeláž v budově sloužící současně pro LAN, telefonii i další služby.

#### Součásti
- **RACK (datový rozvaděč)** – skříň, kde jsou switche, patch panely.
- **Patch panel (rozvodný panel)** – přepojovací panel mezi pevnou kabeláží a aktivními prvky.
- **Patch kabel** – krátký kabel switch ↔ patch panel.
- **Pracovní zásuvka** – v místnosti, kam se připojuje PC.
- **Narážecí nástroj** – nástroj pro adjustáž (uchycení) vodičů do patch panelu.

#### Schéma
```
[ PC ]──patch──[ zásuvka ]──pevný kabel──[ patch panel ]──patch──[ SWITCH ]
                                              │
                                          (v RACKu)
```

### Kategorie TP podle rychlosti
| Rychlost | Min. kategorie |
|---|---|
| 10 Mb/s | Cat 3+ |
| 100 Mb/s | Cat 5+ |
| 1 Gb/s | **Cat 5E+** |
| 2,5 / 5 Gb/s | Cat 5E / 6+ |
| 10 Gb/s | **Cat 6A+** |
| 40 Gb/s | Cat 8 |

### Vzorová odpověď
Kroucená dvojlinka má 4 páry (8 vodičů), impedanci 100 Ω, konektor RJ-45 a maximální segment 100 m. Páry se kroutí kvůli přeslechům a EMS. Podle stínění rozlišujeme UTP, FTP, STP, S/FTP. Strukturovaná kabeláž je jednotný kabelový systém v budově – pevné rozvody jdou do patch panelu v RACKu, odkud se patch kabely zapojují do switche. Kategorie kabelu určuje max. rychlost (Cat 5E pro 1 Gb/s, Cat 6A pro 10 Gb/s).

### Zkreslení signálu PŘENOSOVÝM KANÁLEM u metaliky ⚠️ (chyták v písemce)

> **Pozor na záměnu!** Otázka se NEPTÁ na vnější rušení (EMI, přeslechy, teplota, rádio).
> Ptá se na **parazitní vlastnosti samotného kabelu** jako fyzikálního objektu.

Reálný metalický kabel není dokonalý vodič. Chová se jako kombinace 4 jevů:

| Veličina | Co to fyzikálně je | Důsledek na signál |
|---|---|---|
| **O — Odpor vodičů (sériový)** | Měď klade odpor protékajícímu proudu | **Útlum** — signál slábne s délkou |
| **K — Kapacita mezi vodiči** | 2 paralelní dráty + izolant mezi nimi = kondenzátor | Rozmazává rychlé hrany signálu |
| **I — Indukčnost vodičů** | Tekoucí proud vytváří magnetické pole, které se brání změnám proudu | Zkresluje vysoké frekvence |
| **S — Svod v izolaci** | Izolace není dokonalá, prosakuje proud mezi vodiči | Další ztráty energie |

**Mnemotechnika: O-K-I-S** (Odpor, Kapacita, Indukčnost, Svod).
V elektrotechnice se značí **R, C, L, G** — tzv. „primární parametry vedení" (model RLCG).

#### Vnější vs vnitřní vlivy — rozlišuj!

| Když otázka říká... | Správná odpověď |
|---|---|
| „rušení signálu", „okolní vlivy" | EMI, přeslechy, teplota, rádiové vlny |
| **„zkreslení PŘENOSOVÝM KANÁLEM"** | **O-K-I-S (odpor, kapacita, indukčnost, svod)** |

#### Analogie: zahradní hadice
- **O = odpor** = úzká hadice (voda špatně teče)
- **K = kapacita** = pružný balónek na cestě (pohlcuje rychlé tlakové změny)
- **I = indukčnost** = setrvačnost vody (brání rychlému start/stop)
- **S = svod** = děravá hadice (voda kape ven)

---
