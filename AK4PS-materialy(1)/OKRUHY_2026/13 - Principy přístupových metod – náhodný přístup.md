---
cislo: 13
nazev: Principy přístupových metod – náhodný přístup
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 13) Principy přístupových metod – náhodný přístup

### Definice
**Náhodný přístup** = stanice **mohou vysílat kdykoli**, bez nutnosti centrály nebo tokenu. Rozhodují samy, ale riskují **kolizi** s jinou vysílající stanicí.

### Patří sem
- **ALOHA** (původní i taktovaná)
- **Příposlech nosné (Carrier Sense)**:
  - **CSMA/CD** – Carrier Sense Multiple Access with Collision **Detection**
  - **CSMA/CA** – Carrier Sense Multiple Access with Collision **Avoidance**

### ALOHA (1971, Havaj)
- Stanice vysílá **kdykoli** chce, neřeší obsazenost.
- Po vysílání čeká na ACK; pokud nepřišel → kolize → čeká náhodnou dobu a vysílá znovu.
- **Propustnost: max ~18 %**.

#### Taktovaná (Slotted) ALOHA
- Vysílá se jen na **začátku časových slotů** → kolize buď nastane úplně, nebo vůbec.
- **Propustnost: ~36 %** (2× lepší než základní ALOHA).

### CSMA – příposlech nosné
Stanice **nejprve poslouchá**, jestli někdo vysílá. Pokud ano → čeká. Pokud ne → vysílá.

### CSMA/CD (Ethernet do 1 Gb/s)
**Collision Detection** – stanice **při vysílání zároveň poslouchá** a porovnává odeslaný a slyšený signál.

#### Algoritmus
```
1. Posloucháš médium.
2. Volné? → vysíláš (s krátkým posloucháním po startu).
3. Kolize zjištěna? → vyšleš JAM signál (kolizní signál) a přestaneš.
4. Počkáš náhodnou dobu z intervalu <0, 2^k>·slot_time (binary exponential backoff).
5. Goto 1.
6. Po 16 pokusech (k_max = 10) ohlásíš chybu.
```

#### Pravidla
- **JAM signál** vyšlou **pouze stanice, které vysílají a detekovaly kolizi**.
- **Max počet pokusů = 16**, pak chyba.
- **Max k = 10** (interval `<0, 2¹⁰>` = až 1024 slotů).
- **Slot time** musí být **delší než round-trip k nejvzdálenější stanici** (jinak by stanice neviděla kolizi).
- **CSMA/CD se používá do 1 Gb/s**. Nad to (10 Gb/s) ztrácí smysl, protože plný duplex = bez kolizí.
- **Se switchem v plně-duplexním režimu CSMA/CD ztrácí smysl**.

### CSMA/CA (Wi-Fi)
**Collision Avoidance** – kolize se **dopředu vyhýbáme**, protože ve Wi-Fi nelze detekovat kolizi vysílání (poloduplex, slabý vlastní signál vs silný cizí).

#### Algoritmus
```
1. Posloucháš médium.
2. Volné? Počkáš DIFS interval (Distributed Inter-Frame Space).
3. Stále volné po DIFS? Vysíláš.
4. Obsazené? Odmlčíš se na náhodný backoff slot a znovu testuješ.
5. (Volitelně RTS/CTS proti skrytým uzlům.)
6. Po úspěšném přijetí cíl odpovídá ACK po SIFS intervalu.
```
- **DIFS** = delší interval, normální vysílání.
- **SIFS** = kratší interval, pro ACK (přednost odpovědi).
- **Bez ACK = vysílám znovu**.

### Proč Wi-Fi NEMŮŽE detekovat kolize jako Ethernet 🎯

Klíčová otázka: **Proč CD funguje na drátě a ve Wi-Fi musíme dělat CA?**

#### Na drátě (CSMA/CD) — detekce JDE
```
Drát:   ═══●═════════●═══
            ▲         ▲
           PC1       PC2
```
Když PC1 a PC2 vyšlou současně:
- napětí na drátě se **SEČTE** (zdvojnásobí se)
- PC1 i PC2 svůj vlastní signál **slyší** na drátě
- vidí, že napětí je vyšší, než by mělo → **„KOLIZE!"** → JAM signál → backoff

> **Na drátě slyšíš sebe i ostatní současně.** Anomálii v napětí poznáš real-time.

#### Ve vzduchu (CSMA/CA) — detekce NEJDE, 2 fyzikální důvody

**Důvod 1: Vlastní signál tě OHLUŠÍ**
```
PC1 ))))) ((((( PC2     ✖ kolize ✖

PC1 vysílá → vlastní vysílač řve do antény
           → vlastní signál je MILIONKRÁT silnější
             než cokoli zvenku
           → PC1 NESLYŠÍ, že PC2 vysílá taky
```
Wi-Fi karta nedokáže současně vysílat a poslouchat na stejné frekvenci. To je **half-duplex** = poloduplex.

**Důvod 2: SKRYTÝ UZEL (Hidden Node Problem) ⚠️**
```
       PC1         AP (router)         PC2
        ●─────────►●◄─────────●
       (dosah PC1)    (dosah PC2)

      ❌ PC1 a PC2 SE NAVZÁJEM NESLYŠÍ ❌
      (jsou za zdí, mimo dosah)
      ALE OBA SLYŠÍ AP UPROSTŘED
```
- PC1 poslouchá → ticho → vysílá k AP
- PC2 poslouchá → ticho → vysílá k AP
- **OBA vysílají na AP současně → kolize NA AP**
- Ani jeden z nich kolizi nezpozoruje (neslyší toho druhého)

> **Skrytý uzel = stanice mimo váš dosah, ale dosáhne na společný cíl.**

#### Tabulka rozdílů CD vs CA

| | **CSMA/CD** | **CSMA/CA** |
|---|---|---|
| Médium | **Drát** (Ethernet) | **Vzduch** (Wi-Fi) |
| Princip | **Detekce** kolize (až nastane) | **Avoidance** — vyhnutí (předem) |
| Jak řeší kolizi | Pozná ze zvýšeného napětí | **Nepozná** — usuzuje z chybějícího ACK |
| Hidden node problem | **Neexistuje** (všichni na drátě se slyší) | **EXISTUJE** — řeší se RTS/CTS |
| Efektivita | **Vyšší** (kolize hned vyřešena) | **Nižší** (čekání, ACK, backoff) |

### Demultiplexace u CSMA/CD
Když rámec dorazí na NIC, postupně se „odbalí":
- **Typ rámce (Ethernet type)** → určuje protokol L3 (IP, IPX, ARP…).
- **Číslo IP protokolu** v IP hlavičce → určuje L4 protokol (TCP=6, UDP=17, ICMP=1).
- **Číslo portu** v TCP/UDP hlavičce → určuje aplikaci (port 80 = HTTP atd.).

### Vzorová odpověď
Náhodný přístup dovolí stanicím vysílat kdykoli, ale za cenu kolizí. Patří sem ALOHA (max propustnost 18 %, taktovaná 36 %) a metody příposlechu nosné: CSMA/CD (Ethernet do 1 Gb/s – detekuje kolize, vyšle JAM, čeká náhodný backoff, max 16 pokusů, k_max = 10) a CSMA/CA (Wi-Fi – kolizím se vyhýbá, čeká DIFS interval, případně RTS/CTS proti skrytým uzlům). Se switchem v plném duplexu CSMA/CD ztrácí smysl.

---
