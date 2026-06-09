---
cislo: 32
nazev: Ethernet – rámce a kolize
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 32) Ethernet – rámce a kolize

### Rámec Ethernetu – struktura
Existují dvě varianty: **Ethernet II (DIX)** a **IEEE 802.3 + 802.2 LLC**. Liší se polem Type/Length.

#### Společná část
```
| Preamble | SFD | DST MAC | SRC MAC | Type/Length | Data | FCS |
|  7 byte  | 1 B |  6 byte |  6 byte |   2 byte    |46-1500| 4 B|
```

- **Preamble** = 7 byte (56 bitů) synchronizační posloupnost (`10101010` x 7).
- **SFD** (Start Frame Delimiter) = 1 byte (`10101011`) – signál „za chvíli data".
- **DST MAC** – cílová MAC adresa (6 byte).
- **SRC MAC** – zdrojová MAC adresa (6 byte).
- **Type / Length** – 2 byte:
  - **Type > 1536 (0x0600)** → **Ethernet II** (např. 0x0800 = IPv4, 0x86DD = IPv6).
  - **Length ≤ 1500** → **IEEE 802.3**; po něm následuje **802.2 LLC** hlavička (DSAP, SSAP, Control).
- **Data** – 46–1500 byte (data + případně padding).
- **FCS** (Frame Check Sequence) – 4 byte CRC, kontrolní součet. **Nezahrnuje Preamble a SFD.**

#### Volitelně: VLAN tag (802.1Q)
- 4 byte vkládaný za SRC MAC.
- 12 bitů pro **VLAN ID** (rozsah 1–4096).
- Mění rámec na **„tagged"**.

### Velikosti
| Parametr | Hodnota |
|---|---|
| Min. délka dat | **46 byte** |
| Max. délka dat | **1500 byte** (= MTU) |
| Min. délka celého rámce (bez Preamble/SFD) | **64 byte** |
| Max. délka rámce | **1518 byte** (s VLAN tagem 1522 B) |
| **IFG** (Inter-Frame Gap) | **96 bitů** |

### Délka nejkratšího rámce v bitech
| Rychlost | Délka v bitech |
|---|---|
| 10 Mb/s | **512** |
| 100 Mb/s | **512** |
| **1 Gb/s** | **4096** |
| 10 Gb/s | neaplikuje se (full-duplex, bez kolizí) |

> Důvod: musí být **delší než round-trip čas k nejvzdálenější stanici**, aby stanice stihla detekovat kolizi ještě během vysílání. U 1 Gb/s by 512 bitů trvalo jen 512 ns, což je málo na max segment 100 m.

### Kolize
**Kolize** = situace, kdy 2+ stanice vysílají ve stejnou dobu na stejném médiu → signály se prolnou, výsledek je nečitelný.

#### Detekce a chování (CSMA/CD)
1. Stanice **při vysílání poslouchá** médium.
2. Pokud signál na médiu neodpovídá vlastnímu vysílanému → kolize.
3. Vyšle **JAM signál** (32 bitů, zaručí všem ostatním, že kolize nastala).
4. Stanice přestane vysílat.
5. Počká **náhodnou dobu** z intervalu `<0, 2^k>` slot-times (binary exponential backoff).
6. Zkusí znovu. Max **16 pokusů**.

#### Pravidla
- **JAM vyšlou pouze stanice, které právě vysílají a detekovaly kolizi**.
- **Max k = 10** (interval `<0, 1024>`).
- **Max pokusů = 16**, pak chyba.
- Doba vysílání **nejkratšího rámce musí být delší než round-trip k nejvzdálenější stanici**.

#### Kdy ke kolizi dochází
- Pouze v **polo-duplexním** režimu na sdíleném médiu (koaxiál, hub).
- Ve **switchi s plným duplexem** kolize **NEexistují** – CSMA/CD ztrácí smysl.

### Vzorová odpověď
Ethernet rámec má pevnou strukturu: Preamble (7 B) + SFD (1 B) + cílová MAC (6 B) + zdrojová MAC (6 B) + Type/Length (2 B) + Data (46-1500 B) + FCS (4 B). Pokud Type > 1536, je to Ethernet II (s číslem L3 protokolu), pokud Length ≤ 1500, je to IEEE 802.3 s 802.2 LLC hlavičkou. IFG mezi rámci je 96 bitů. Minimální délka rámce je 64 byte, u 1 Gb/s ale musí být 4096 bitů (jinak by stanice nestihla detekovat kolizi). Kolize vznikají v polo-duplexu na sdíleném médiu; CSMA/CD je detekuje, stanice pošle JAM, čeká náhodný backoff (max k=10), po 16 pokusech chyba. Plný duplex se switchem kolize odstraňuje.

---
