# Zkušební okruhy – Počítačové sítě (AK4PS) – LS 2025/2026

> Zpracování všech **35 okruhů** z `PS zkušební okruhy 04.05.26.pdf`.
> Zdroj: `Počítačové sítě 14.05.26.pdf` (Matýsek, UTB Zlín) + `Počítačové sítě rozšiřující prezentace 26.03.19.pdf` + existující [[TAHAK_CISTY]].
> Formát na otázku: **definice → klíčová fakta → analogie/diagram → tabulka/příklad → vzorová odpověď u zkoušky**.
> Otázky kde si nejsem 100% jistý označuji **[?]** – ověř proti přednášce.

---

## 1) Základní terminologie

### Definice
**Počítačová síť** = soustava propojených autonomních počítačů a dalších zařízení (tiskárny, servery…) sdílejících prostředky pomocí komunikačních pravidel (protokolů).
  >Vrstva = úroveň, na které se něco děje (jako patro v paneláku).
  >Protokol = pravidla, jak se to na té vrstvě dělá.

### Klíčové pojmy
- **Uzel (node)** = aktivní zařízení v síti (PC, server, switch, router…).
- **Médium** = fyzický prostředek pro přenos (kabel metalický/optický, vzduch).
- **Protokol** = sada pravidel pro výměnu dat (TCP/IP, IPX/SPX, NetBEUI…).
- **PDU (Protocol Data Unit)** = blok dat na dané vrstvě:
  - rámec (L2) – paket (L3) – segment/datagram (L4) – zpráva (L5–L7).
- **Zpráva** = obecně balík dat přenášený sítí.
- **Paket** = balík dat pevné délky.
- **Datagram** = paket, který se může po síti pohybovat samostatně (L3).
- **Rámec** = paket + linkové info (MAC adresy, CRC).
- **Segment** = balík pevné délky z transportní vrstvy.

### Architektury
| Architektura | Popis |
|---|---|
| **Client-server** | vyhraněné role, server poskytuje, klient žádá |
| **Peer-to-peer (P2P)** | každý PC je klient i jednoduchý server, role nevyhraněné |

### Homogenní vs nehomogenní síť
- **Homogenní** – stejný OS, stejný protokol, stejný HW na všech PC.
- **Nehomogenní** – různé OS / různé protokoly → potřeba **gateway** na propojení.

### Síťový protokol
Soubor pravidel umožňujících výměnu dat přes síť. Bez společného protokolu si dva uzly „nerozumí".

### Historické alternativy k TCP/IP (z rozšiřující prezentace)

#### IPX/SPX (Xerox / Novell)
Alternativa k TCP/IP, **původně XEROX**, později rozšířeno Novell NetWare. **V LAN rychlejší než TCP/IP.** Pokrývá SW 2.–7. vrstvu OSI (u L2 jen podvrstvu LLC).

- **IPX (Internetwork Packet eXchange)** = L3, **nespojovaná nepotvrzovaná** služba (analog **datagramové služby TCP/IP**, tj. ekvivalent UDP/IP).
  - Výhody: nezatěžuje síť řídicími/potvrzovacími pakety, lze poslat skupině nebo všem.
  - Nevýhoda: není zaručeno bezchybné doručení.
- **SPX (Sequenced Packet eXchange)** = L4, **spojovaná potvrzovaná** služba (analog **TCP**).
  - Výhoda: bezchybné doručení.
  - Nevýhody: nelze multicast/broadcast, režie ~15 %.

**Složená síťová adresa IPX/SPX v Ethernetu:**
- **32 b adresa sítě** – default `00000000H`, u sítí s routerem přiděluje správce.
- **48 b adresa uzlu** – = **MAC adresa NIC** (v síti bez routeru tedy není třeba nic nastavovat).
- Příklad: `000000F5:FF005C8911CB`.

**Další protokoly v zásobníku Novell**: RIPX (routing), BCAST, DIAG, SER, WDOG, SAP (Service Advertising Protocol), NetBIOS, BMP, NCP (NetWare Core Protocol), NDS (NetWare Directory Services), NLSP.

#### NetBIOS / NetBEUI (IBM, dnes Microsoft)
- **NetBIOS (Network Basic I/O System)** = nejstarší síťový protokol pro LAN, IBM pro DOS, rozšiřuje BIOS o LAN funkce. Pod IPX/SPX nebo TCP/IP je **emulován na relační vrstvě (L5)**.
- **NetBEUI (NetBIOS Extended User Interface)** = nadstavba nad NetBIOS, **realizována na L3 + L4**. V Microsoft Windows společně se **SMB** (Server Message Block – aplikační, sdílení disků/tiskáren). SMB pod TCP/IP je emulován.
- Vyžaduje jednoznačnost jmen (jméno PC + workgroup/doména, max 16 znaků).
- **Není routovatelný** (adresa neobsahuje adresu sítě, jen uzel).
- **Rychlejší v LAN do 10 PC** než IPX/SPX a TCP/IP, pro větší zpomaluje.

### Symboly síťových zařízení (Cisco standard)
![[2.7 Symboly sitovych zarizeni.png]]

Standardní piktogramy, které prezentace používá: **Router** (kruh se 4 šipkami), **Switch** (kvádr se 4 šipkami), **Hub** (kvádr s vodorovnými čárkami), **Bridge**, **Repeater**, **Firewall** (cihla), **Wireless AP / Wireless Router** (s anténami), **Server**, koncová zařízení (PC, laptop, IP phone, tiskárna). Linky: **LAN** = rovná, **WAN** = klikatá, **Wireless** = vlnovka.

### Vzorová odpověď
Počítačová síť je propojení autonomních zařízení sdílejících prostředky podle pravidel = protokolů. PDU (blok dat na dané vrstvě) jsou na různých vrstvách jiné (rámec/paket/segment/zpráva). Architektura buď client-server (vyhraněné role) nebo peer-to-peer. Síť může být homogenní (stejný OS/protokol) nebo nehomogenní – pak se potřebuje gateway. Historické alternativy k TCP/IP: IPX/SPX od Xerox/Novell (IPX = L3 nespojovaná jako UDP, SPX = L4 spojovaná jako TCP, adresa 32b síť + 48b uzel = MAC) a NetBIOS/NetBEUI od IBM (NetBIOS na L5 jako emulace, NetBEUI na L3+L4, není routovatelný, rychlý v LAN ≤10 PC).

---

## 2) Historie počítačových sítí

### Klíčové letopočty
| Rok                 | Událost                                                                  |
| ------------------- | ------------------------------------------------------------------------ |
| **počátek 70. let** | vznik prvních počítačových sítí                                          |
| **1969**            | **ARPANET** – první uzel, projekt americké armády (DARPA)                |
| **1970**            | vývoj v DARPA pokračuje                                                  |
| **1977**            | zahájen vývoj **TCP/IP**                                                 |
| **1983**            | zavedení **TCP/IP do ARPANETu** (přechod z NCP)                          |
| **1984**            | zavedení **DNS** do ARPANETu                                             |
| **1986**            | financování **NSF** (NSFNET)                                             |
| **1989**            | vznik **WWW** stránek (Tim Berners-Lee, CERN)                            |
| **1990**            | pevná linka v ČSFR                                                       |
| **1991**            | pokus o připojení ČSFR k Internetu                                       |
| **1992**            | **ČSFR připojeno k Internetu (komerční provoz)** – 13. 2. 1992 přes ČVUT |
| **1993**            | registrována doména **.cs**                                              |
| **1995**            | doména **.cs** nahrazena doménou **.cz** (rozpad ČSFR)                   |

### Souvislosti
- ARPANET vznikl z obavy o odolnost komunikační infrastruktury během studené války.
- Předchůdce TCP/IP byl protokol **NCP**.
- Internet (s velkým I) = celosvětová síť postavená nad TCP/IP.
- internet (malé i) = libovolná soustava propojených sítí.

### Vývoj topologie sítí (slidy 25–30 prezentace)

#### 3.1 Počátky počítačových sítí 
- V počátku 70. let vznikaly **první izolované počítačové sítě** různých výrobců.
- Později vznikají sítě s **polygonální strukturou** → vznikají první **přepojovací uzly**.

#### 3.2 Síť bez přepojovacích uzlů 
![[Pasted image 20260523142218.png]]
- **U = uzel**: sálový počítač s OS Unix.
- Sálové počítače propojené **přímo navzájem** (polygonální propojení).
- Velmi nepraktické: počet spojů roste kvadraticky s počtem uzlů.

#### 3.3 Síť s přepojovacími uzly  
![[Pasted image 20260523142237.png]]
- **P = přepojovací uzel**: OS Unix + přepojovací SW (předchůdce dnešního routeru).
- Pakety putují **uzel → přepojovací uzel → cílový uzel**.

#### 3.4 Alternativní cesty 
![[Pasted image 20260523142247.png]]
- Mezi dvěma uzly **existuje víc cest** přes různé přepojovací uzly.
- Při výpadku jedné cesty paket jde jinou → základ odolnosti ARPANETu.

#### 3.5 Nadbytečná propojení (slide 29)
![[Pasted image 20260523142529.png]]
- Některá přímá U↔U propojení **zbytečně duplikují** trasy, které jsou už dostupné přes P.
- Lze je odstranit bez ztráty konektivity.

#### 3.6 Nezbytně nutná propojení (slide 30)
![[Pasted image 20260523142549.png]]
- Po odstranění nadbytečností zůstane **hvězdicová struktura kolem přepojovacích uzlů P**.
- Každý U je připojen jen k P, P jsou propojeny mezi sebou → základ dnešní hierarchické topologie LAN/WAN.

### Vzorová odpověď
Počítačové sítě vznikly na začátku 70. let. Klíčový mezník je ARPANET (1969), na něm se v 70. letech vyvíjel TCP/IP, který se prosadil v roce 1983. DNS přišel 1984, WWW v roce 1989. ČSFR byla připojena 1992, doména .cz nahradila .cs v roce 1995. Topologicky se vývoj posunul ze sítí bez přepojovacích uzlů (polygonální propojení U-U) přes sítě s přepojovacími uzly (P mezi U) k dnešní struktuře s alternativními cestami a odstraněním nadbytečných propojení – výsledkem jsou „nezbytně nutná propojení" tvořící hvězdy kolem přepojovacích uzlů.

---

## 3) Další dělení sítí a číselné soustavy

### Dělení podle rozsahu (od nejmenší)
**PAN < LAN < CAN < MAN < WAN < GAN**

| Zkratka | Význam | Rozsah |
|---|---|---|
| **PAN** | Personal AN | jednotky metrů (Bluetooth, USB) |
| **LAN** | Local AN | desítky až stovky metrů (jedna budova) |
| **CAN** | Campus AN | stovky m až jednotky km (univerzita) |
| **MAN** | Metropolitan AN | jednotky až desítky km (město) |
| **WAN** | Wide AN | desítky km a víc (stát) |
| **GAN** | Global AN | celosvětová |
| **SAN** | Storage AN | speciální – pro úložiště |
| **WLAN** | Wireless LAN | bezdrátová LAN (Wi-Fi) |

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

## 7) Komunikace vzduchem – WLAN, IEEE 802.11, Wi-Fi, pásma, standardy

### WLAN, Wi-Fi, IEEE 802.11
- **WLAN** = obecně bezdrátová lokální síť.
- **IEEE 802.11** = standard pro bezdrátové LAN (od IEEE).
- **Wi-Fi** = **pouze značka/nálepka** pro zařízení, která splňují 802.11 + vzájemnou kompatibilitu.
- Nálepku Wi-Fi uděluje **Wi-Fi Alliance** (sdružení výrobců, certifikační autorita).
- Označení „bezdrátový Ethernet" je **NESPRÁVNÉ** (Ethernet má 802.3, Wi-Fi 802.11; jiný standard, jiné rámce).

### Licencovaná a bezlicenční pásma
| Typ | Pásma | Použití |
|---|---|---|
| **Licencovaná** | 3,5; 26; 28 GHz (+ 4, 6, 7, 8, 11, 13, 15, 18, 23 GHz) | mikrovlnné spoje, mobilní operátoři |
| **Bezlicenční** | 2,4; 5; 6; 10,5 GHz | Wi-Fi, Bluetooth, IoT |

- **Licencovaná pásma**: vyžadují přidělení od ČTÚ za poplatek; uživatel má garantovanou ochranu před rušením.
- **Bezlicenční pásma**: volně využitelná v rámci tzv. **generální licence** ČTÚ.

### Generální licence (ČR)
Souhrnný dokument ČTÚ povolující používat bezlicenční pásma za stanovených podmínek (max. vyzářený výkon, EIRP, povolené modulace, šířka kanálu…). Pro 2,4 GHz Wi-Fi: **max 100 mW EIRP** (20 dBm).

### Standardy IEEE 802.11 a rychlosti
| Standard | Pásmo | Max. teor. rychlost | Označení |
|---|---|---|---|
| **802.11a** | 5 GHz | 54 Mb/s | – |
| **802.11b** | 2,4 GHz | 11 Mb/s | – |
| **802.11g** | 2,4 GHz | 54 Mb/s | – |
| **802.11n** | 2,4 + 5 GHz | 600 Mb/s | Wi-Fi 4 |
| **802.11ac** | 5 GHz | 6,77 Gb/s | Wi-Fi 5 |
| **802.11ax** | 2,4 + 5 + 6 GHz | 9,6 Gb/s | **Wi-Fi 6 / 6E** |
| **802.11be** | 2,4 + 5 + 6 GHz | 46 Gb/s | **Wi-Fi 7** |

### Kompatibilita
- **802.11g** je zpětně kompatibilní s **802.11b**.
- **802.11n** funguje v 2,4 i 5 GHz – kompatibilita s a/b/g podle pásma.

### Pásmo 2,4 GHz v ČR
- Rozděleno na **13 kanálů** šířky 20 MHz.
- **Nepřekrývající se kanály v ČR: 1, 7, 13** (v USA bývají 1, 6, 11).
- **Maximální počet vzájemně se nerušících sítí: 3** (na 1, 7 a 13).
- **Max vyzářený výkon**: **20 dBm = 100 mW**.

### Pásmo 5 GHz
- Rozděleno na **19 subpásem**.
- V subpásmu 5,470–5,725 GHz: **11 nepřekrývajících se kanálů**.
- **Min. přenos antény**: 1000 mW (1 W).

### Pásmo 6 GHz
- **59 kanálů**.
- Využívá ho 802.11ax (Wi-Fi 6E) a 802.11be (Wi-Fi 7).

### Vzorová odpověď
WLAN je obecná bezdrátová síť, standardizovaná jako IEEE 802.11. Wi-Fi je jen certifikační značka, kterou uděluje Wi-Fi Alliance. Pásma jsou licencovaná (3,5/26/28 GHz a další – pro mikrovlnné spoje, mobilní operátory) a bezlicenční (2,4/5/6/10,5 GHz – Wi-Fi). Bezlicenční využití kryje generální licence ČTÚ s omezením výkonu (max 100 mW v 2,4 GHz). Standardy 802.11 a-g pracují do 54 Mb/s, novější n/ac/ax/be jdou až do desítek Gb/s a využívají i 6 GHz pásmo. V 2,4 GHz jsou v ČR nepřekrývající se kanály 1, 7, 13.

---

## 8) Komunikace vzduchem – bezpečnost, architektura, mikrovlnné spoje, antény, Fresnelova zóna, skrytý uzel

### Bezpečnost Wi-Fi
Šifrování vzestupně podle síly:
**WEP < WPA < WPA2 < WPA3**
- **WEP** – dnes prolomený, **nedostatečný**, používá se jen u ad-hoc historicky.
- **WPA** – přechodný standard.
- **WPA2** – dlouhá léta standard, AES.
- **WPA3** – **aktuálně nejúčinnější**, odolnost proti slovníkovým útokům.

### Architektura WLAN
Dva základní režimy:

#### 1) Ad-hoc (IBSS – Independent BSS)
Bez přístupového bodu; klienti komunikují přímo.
```
[ PC1 ]──────[ PC2 ]
   \          /
    \        /
     [ PC3 ]
```

#### 2) Infrastructure (BSS / ESS)
S přístupovým bodem (AP – Access Point).
```
        [ AP ]
       /  │   \
   [PC1] [PC2] [PC3]
```
- **BSS** (Basic Service Set) = 1 AP + klienti.
- **ESS** (Extended Service Set) = více AP propojených páteří (roaming).
- **SSID** – identifikátor sítě.

### Mikrovlnné spoje
- **Bod-bod přenos** mezi 2 anténami na přímou viditelnost (LOS – Line of Sight).
- Používá licencovaná pásma 3,5–80 GHz pro páteřové spoje (operátoři, ISP).
- Velmi citlivé na déšť (dešťový útlum) ve vyšších pásmech.

### Antény – typy a parametry
| Typ antény | Vyzařovací charakteristika |
|---|---|
| **Izotropní** | (teoretická) vyzařuje stejně do všech směrů |
| **Všesměrová (omni)** | kruhová horizontálně (anténa pro AP) |
| **Sektorová** | určitý úhel (např. 60°/90°/120°) – pro WISP |
| **Směrová (parabolická, Yagi)** | úzký svazek – bod-bod spoje |

#### Zisk antény
- **dBi** – zisk vůči izotropní anténě.
- **dBd** – zisk vůči dipólu.
- **dBi je o 2,15 dB větší než dBd** (izotropní je horší referenční bod).
- **dBm** = decibel milliwatt = výkon vůči 1 mW. 20 dBm = 100 mW.

### Fresnelova zóna
![[8 Fresnelova zona.png]]

**Fresnelova zóna** = oblast kolem přímé spojnice antén ve tvaru **paraboloidu (rotačního elipsoidu)**, ve které se šíří podstatná část energie radiového signálu.

```
       ────────────                 ────────────
       \           \               /           /
         \    F1    \    Pevný    /     F2    /
   ANT1   \─────────────signál───────────────/  ANT2
         /                                  \
       /          (paraboloid)               \
       ────────────                ────────────
```

- **Předměty v Fresnelově zóně zeslabují signál** (i když je přímá viditelnost zachována).
- 1. Fresnelova zóna by měla být **alespoň z 60 % volná**.
- Velikost zóny závisí na frekvenci a vzdálenosti antén.

### Problém skrytého uzlu (hidden node)
**Situace**: dvě stanice A a C jsou v dosahu AP, ale **nevidí navzájem** (např. zdi, vzdálenost). Obě začnou vysílat současně → na AP **kolize**, ale CSMA/CA to neumí detekovat (každá stanice „slyší" jen sebe).

```
   [A] ─── slyší ──→ [AP] ←── slyší ── [C]
   [A] ✗ NEslyší ✗ [C]
```

**Řešení: RTS/CTS** (Request to Send / Clear to Send)
1. **A** chce vysílat → pošle krátký rámec **RTS** s časem trvání přenosu.
2. **AP** odpoví **CTS** broadcastem – obsahuje stejný čas.
3. **C** sice neslyší A, ale **slyší CTS od AP** a ví, že má mlčet po danou dobu.
4. A vysílá, C čeká.

```
A: ──RTS──>           AP: ──CTS──> (broadcast, slyší ho i C)
                       │
A vysílá data...       │
                       │
A: ──ACK potvrzení──>  │
```

### Pasivní vs aktivní retranslace
- **Pasivní** – odraz, přesměrování (zrcadlo, parabola).
- **Aktivní centralizovaná** – 1 prvek (AP).
- **Aktivní distribuovaná** – víc aktivních prvků (mesh, repeatery).

### MIMO technologie
Více antén pro vyšší propustnost.
| Vysílání / Příjem | Označení |
|---|---|
| 1 / 1 | SISO |
| 1 / více | **SIMO** |
| Více / 1 | **MISO** |
| Více / Více | **MIMO** |

### Vzorová odpověď
Bezpečnost Wi-Fi prochází vývojem WEP → WPA → WPA2 → WPA3 (nejúčinnější). Architektura má dva režimy: ad-hoc (peer-to-peer) a infrastructure s přístupovým bodem (BSS, ESS pro roaming). Mikrovlnné spoje slouží pro bod-bod přenos v licencovaných pásmech. Antény mají různé vyzařovací charakteristiky (izotropní teoretická, všesměrová, směrová), zisk se udává v dBi (vůči izotropní) nebo dBd (vůči dipólu, o 2,15 dB méně). Fresnelova zóna je paraboloid kolem přímky mezi anténami, ve kterém se šíří signál – předměty v něm signál zeslabují. Problém skrytého uzlu vzniká když dva klienti nevidí navzájem, ale oba vidí AP – řeší ho mechanismus RTS/CTS.

---

## 9) Přenos signálu v základním a přeloženém pásmu

### Definice
- **Základní pásmo (Baseband)** = přenos signálu přímo na médiu **bez přesunu na nosnou frekvenci**. Signál zabírá celé spektrum média.
- **Přeložené pásmo (Broadband)** = signál je **modulován na nosnou vlnu** a přesunut do jiného frekvenčního rozsahu. Na médiu lze vést **víc signálů současně** v různých pásmech.

### Vlastnosti
| Charakteristika | Základní (Baseband) | Přeložené (Broadband) |
|---|---|---|
| Počet signálů na médiu | **1** | **více** (FDM) |
| Modulace | bez nosné | s nosnou (AM/FM/PM) |
| Šíře pásma | celá | jen alokovaný subkanál |
| Příklad | klasický Ethernet (BaseT) | kabelová TV, ADSL, mobilní sítě |

### Modulace v přeloženém pásmu
Tři základní druhy:
- **Amplitudová modulace (AM)** – mění se velikost amplitudy nosné.
- **Frekvenční modulace (FM)** – mění se frekvence nosné.
- **Fázová modulace (PM)** – mění se fáze nosné.
- **QAM** (kvadraturní amplitudově-fázová) – kombinace AM + PM, dnes nejpoužívanější (kabelovky, Wi-Fi, LTE).

### Kódování v základním pásmu
| Kód | Princip | Použití |
|---|---|---|
| **NRZ bipolární** | 0 = nižší úroveň, 1 = vyšší úroveň | COM port |
| **NRZI bipolární** | 0 = beze změny, 1 = změna úrovně | 100BASE-FX |
| **Fázové NRZ (Manchester)** | 1 = sestupná, 0 = vzestupná hrana | **10BASE-T Ethernet** |
| **MLT-3** | tři úrovně, změna při 1 | 100BASE-TX |
| **PAM5** | 5 úrovní amplitudy | 1000BASE-T |
| **4B/5B, 8B/10B** | kódování 4/8 bitů do 5/10 (eliminace DC) | 100BASE-TX, 1000BASE-X |

### Důležitá pravidla
- Přenášený signál by **neměl mít stejnosměrnou složku** (DC) – proto kódování jako Manchester, 8B/10B.
- **Šířka pásma digitálního signálu** se uvádí v **b/s** (bps).
- **Modulační rychlost** v **Baud (Bd)** = počet změn za sekundu = Hz.
- **Přenosová rychlost** v **b/s**.
- **1 Hz teoreticky převede 2 bity/s** (Nyquist).
- **Frekvence pro 1 b/s** = **0,5 Hz**.

### COM port (RS-232)
- Používá **bipolární NRZ**.
- Log. 0 = **+3 až +15 V**.
- Log. 1 = **−3 až −15 V**.

### Druhy přenosu podle směru
| Typ | Popis |
|---|---|
| **Simplex** | jen jedním směrem (vysílač → přijímač) |
| **Poloduplex (Half-duplex)** | oběma směry, ale ne současně |
| **Plný duplex (Full-duplex)** | oběma směry současně |

### Throughput vs goodput
**Kde měříme přenosovou rychlost:**
- **Throughput** = rychlost **na přenosovém médiu** (hrubá – včetně všech hlaviček, ACK, signalizace).
- **Goodput** = rychlost **na úrovni síťové aplikace** (čistá užitečná data).
- **Goodput = throughput − provozní režie** (zřízení relace, potvrzování, zapouzdření hlaviček L2/L3/L4).
- Goodput je vždy **menší než throughput**. U TCP přes Ethernet typicky 90–95 % throughputu.

### Útlum
- Uvádí se v **dB**.
- **dB napětí**: 20·log₁₀(U₂/U₁).
- **dB výkonu**: 10·log₁₀(P₂/P₁).
- **dBm**: 10·log(P [W] / 0,001).
- **Snížení napětí na 50 % = −6 dB**.
- **Snížení napětí na 25 % = −12 dB**.
- **Snížení výkonu na 25 % = −6 dB**.
- **Přeslech (NEXT/FEXT)** = 10·log₁₀(P₁/P₂), uvádí se v dB.

### Vzorová odpověď
V základním pásmu (baseband) přenáším signál přímo, bez modulace, médium nese jen 1 signál – tak funguje Ethernet (10/100 BaseT). V přeloženém pásmu (broadband) signál moduluji na nosnou vlnu a na médium se vejde víc signálů paralelně (FDM) – kabelovka, ADSL, mobilní sítě. Modulace jsou amplitudová, frekvenční a fázová (resp. jejich kombinace QAM). V základním pásmu se používají kódování jako NRZ, NRZI, Manchester (10BASE-T), MLT-3 (100BASE-TX), PAM5 (1GBASE-T) – cíl je odstranit stejnosměrnou složku a umožnit synchronizaci.

---

## 10) Fyzická topologie – sběrnice, kruh, hvězda, strom

### Definice
**Fyzická topologie** = způsob fyzického propojení uzlů kabely / médii. **Logická topologie** = způsob, jakým spolu uzly logicky komunikují (může se lišit od fyzické).

### Sběrnice (Bus)
![[Pasted image 20260523193809.png]]

- Všechny uzly visí na **společném kabelu**.
- **Musí být zakončena odpory** (terminátory) na obou koncích – jinak odraz signálu.
- **Přerušení kabelu = výpadek celé sítě**.
- Zpráva se šíří **ke všem stanicím**.
- Historicky: **10BASE2, 10BASE5** (koaxiál).
- Dnes prakticky **nepoužívaná** v Ethernetu, ale **logická topologie Ethernetu je stále sběrnice**.

### Kruh (Ring)
![[Pasted image 20260523193912.png]]

- Každý PC propojen s **následujícím a předchozím** (typicky jednosměrný tok).
- Každý uzel **regeneruje signál** (aktivní role).
- Pokud přijatá data nejsou určena tomuto PC, pošle dál.
- **Výpadek 1 PC = výpadek celé sítě** (lze obejít dvojitým kruhem – Token Ring, FDDI).
- Historicky: Token Ring, FDDI.

### Hvězda (Star)
![[Pasted image 20260523193956.png]]
- Všechny uzly k jednomu **centrálnímu prvku** (hub nebo switch).
- **Výpadek stanice neovlivní síť** (jen ona je odpojená).
- **Výpadek centrálního prvku = pád sítě**.
- Nejstarší typ topologie (terminály k mainframe).
- **Typický dnes**: Ethernet na TP se switchem.

### Strom (Tree)
![[Pasted image 20260523194016.png]]
- **Hierarchie hvězd** – kořen + uzly, ze kterých vychází další hvězdy.
- **Havárie kořene → celá síť padá**.
- **Výpadek větve → ostatní fungují**.
- Typické pro **strukturovanou kabeláž** v budově (páteřní switch → patrové switche).

### Vzorová odpověď
Fyzická topologie je dána fyzickým propojením kabelů. Sběrnice má společný kabel se zakončovacími odpory, libovolné přerušení shodí síť, šíří ke všem – dnes prakticky nepoužitá. Kruh propojuje uzly do okruhu, každý regeneruje signál a posílá dál – historicky Token Ring, FDDI. Hvězda má centrální prvek (hub/switch), výpadek stanice síti nevadí ale výpadek centra ano – dnes nejtypičtější. Strom je hierarchie hvězd, používá se ve strukturované kabeláži, padá kořen = padá síť.

---

## 11) Fyzická topologie – backbone, mash, neomezená; logické topologie

### Backbone (páteř)
![[Pasted image 20260523194044.png]]
**Páteřní topologie** = vysokorychlostní linka spojující více menších sítí (LAN, MAN).
```
        ┌─[LAN1]──┐
        │         │
   ═══[BACKBONE]══════[BACKBONE]═══   (rychlá optická páteř)
        │                   │
        └─[LAN2]──┐    ┌──[LAN3]
                  │    │
                  [LAN4]
```
- Vysoká rychlost (obvykle optická).
- V ČR příklad: **CESNET2** (akademická páteřní síť).
- Spojuje LAN/CAN/MAN/WAN.

### Mash (mesh)
![[Pasted image 20260523194103.png]]
- Každý uzel propojen **s více ostatními** (částečný mesh) nebo **se všemi** (full mesh).
- **Vysoká redundance** → odolnost vůči výpadkům.
- Při výpadku spoje má paket alternativní cestu.
- Použití: WAN páteřní sítě, mesh Wi-Fi (pokrytí budov).

### Neomezená topologie (libovolná, irregular)
![[Pasted image 20260523194118.png]]
- **Nejčastěji pro WAN** – Internet, světová síť.
- Topologie není pravidelná, vzniká postupně připojováním dalších sítí.
- Není striktně řízena, propojení podle dohody mezi ISP.

### Logická topologie
**Definice**: dána způsobem, jakým spolu uzly **logicky komunikují** – nezávisí na tom, jak je síť fyzicky zapojena.

#### Tři logické topologie
1. **Logická sběrnice** – všechny uzly vysílají do jednoho společného „bus", ostatní poslouchají. **Ethernet má logickou topologii sběrnici**, i když fyzicky je hvězda.
2. **Logický kruh** – data putují od uzlu k uzlu v kruhu (token předávaný dál). Token Ring fyzicky byl hvězda kolem MAU, ale logicky kruh.
3. **Logický dvojbodový spoj (point-to-point)** – přímé spojení dvou uzlů (modem, dedikovaná linka).

### Vzorová odpověď
Backbone je páteřní topologie – vysokorychlostní linka spojující menší sítě, v ČR příklad CESNET2. Mesh propojuje uzly mezi sebou s vysokou redundancí, paket má alternativní cesty. Neomezená (libovolná) topologie je typická pro WAN a Internet – vzniká postupně, není pravidelná. Logická topologie je nezávislá na fyzické: Ethernet má fyzicky hvězdu, ale logicky sběrnici. Logické topologie jsou tři: sběrnice, kruh a dvojbodový spoj.

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

## 14) Model OSI

### Co to je
**ISO/OSI (Open Systems Interconnection)** = referenční model definovaný ISO; rozděluje komunikaci do **7 vrstev**. Není to implementace, ale **referenční rámec**.

### 7 vrstev (zdola)
![[Pasted image 20260524002828.png]]

| #     | Vrstva                | Anglicky     | PDU                    | Co dělá                                                          |
| ----- | --------------------- | ------------ | ---------------------- | ---------------------------------------------------------------- |
| **7** | **Aplikační**         | Application  | data/zpráva            | rozhraní pro aplikace (HTTP, FTP, SMTP, DNS)                     |
| **6** | **Prezentační**       | Presentation | data/zpráva            | formát dat, šifrování, komprese (ASCII, JPEG, TLS)               |
| **5** | **Relační**           | Session      | data/zpráva            | navazování/řízení relací (NetBIOS, RPC, SQL session)             |
| **4** | **Transportní**       | Transport    | **segment / datagram** | end-to-end přenos, spolehlivost (TCP, UDP)                       |
| **3** | **Síťová**            | Network      | **paket / datagram**   | logická adresace, směrování (IP, IPX, ICMP)                      |
| **2** | **Linková (spojová)** | Data Link    | **rámec**              | MAC adresy, řízení přístupu k médiu, rámcování (Ethernet, Wi-Fi) |
| **1** | **Fyzická**           | Physical     | **bity**               | přenos sériového toku bitů, médium, konektory                    |

### Mnemoshrnutí (česky zdola): **F**y**L**a**S**í**T**ra**R**e**P**re**A**p
„Fyzická Linková Síťová Transportní Relační Prezentační Aplikační"

### Co je v hlavičce
| Vrstva | PDU | Adresy / identifikátory |
|---|---|---|
| 2 | rámec | **MAC adresy** (zdroj + cíl), FCS |
| 3 | paket | **logické adresy** (IP, IPX) |
| 4 | segment | **čísla portů** (TCP/UDP) |

### Typické otázky
- **Kterou vrstvou se přenáší sériová posloupnost bitů?** Fyzická.
- **Která vrstva pracuje s pakety?** Síťová (3).
- **Které vrstvy pracují se zprávami?** Aplikační, prezentační, relační.
- **Nejvyšší vrstva OSI?** Aplikační (7).
- **Která vrstva pracuje s MAC adresami?** Linková (2).
- **Na kterých vrstvách jsou síťové protokoly nezávislé na cestě?** Vrstvy **4, 5, 6, 7** (end-to-end). Vrstvy 1–3 pracují hop-by-hop a starají se o cestu.
- **Která vrstva směruje?** Síťová (3) – routery.

### Vstupní body SAP (Service Access Point)
**SAP = brána mezi dvěma sousedními vrstvami OSI.** Vyšší vrstva přes SAP žádá nižší vrstvu o její službu.

#### Analogie: budova s patry a dveřmi
- Vrstva = patro
- SAP = dveře mezi patry, **každé patro má víc dveří** → každé dveře vedou k jiné konkrétní službě.
- Bez SAPu by mohla jednu vrstvu používat jen jedna aplikace naráz; díky SAPu běží paralelně web, mail i SSH.

#### Konkrétní názvy SAPů
| Mezi vrstvami | Název SAP | Konkrétní příklad |
|---|---|---|
| 5 ↔ 4 | **TSAP** (Transport SAP) | **port TCP/UDP** (80, 25, 443…) |
| 4 ↔ 3 | NSAP (Network SAP) | – |
| 3 ↔ 2 | **LSAP** (Link SAP) | **DSAP / SSAP** v hlavičce 802.2 LLC |

#### Důležitý praktický příklad
V IEEE 802.3 + 802.2 najdeš pole **„cílová SAP" (DSAP)** – říká linkové vrstvě, kterému síťovému protokolu (IP, IPX) předat data nahoru. Bez SAPu by linkovka nevěděla, kam paket „přepnout".

#### Otázka
**Vstupní body SAP umožňují**: paralelní poskytování nezávislých služeb několika uživatelům současně.

### Každá vrstva
- má přidělenou činnost, sadu protokolů a **dvě rozhraní** (k vyšší a nižší vrstvě).

### Vzorová odpověď
Model OSI je referenční model od ISO se 7 vrstvami (fyzická, linková, síťová, transportní, relační, prezentační, aplikační). Vrstvy 1–3 pracují hop-by-hop, vrstvy 4–7 end-to-end. PDU se mění: bity (L1), rámec (L2, MAC adresy), paket (L3, IP), segment (L4, porty), zpráva (L5–7). SAPy jsou „dveře" mezi vrstvami – umožňují paralelní obsluhu více uživatelů; konkrétně TSAP = port, LSAP = DSAP/SSAP v 802.2.

---

## 15) Standardy IEEE 802

### Co to je
**IEEE 802** = rodina standardů Institute of Electrical and Electronics Engineers pro **LAN, MAN a WLAN**. Standardy definují fyzickou a linkovou vrstvu.

### Architektura IEEE 802 a vztah k OSI
IEEE 802 dělí **linkovou vrstvu (L2)** na dvě podvrstvy:
```
   OSI vrstva 2 (Linková)
   ┌────────────────────────┐
   │   LLC – 802.2          │ ← logické řízení (společné všem)
   ├────────────────────────┤
   │   MAC – 802.3, 802.11, │ ← přístup k médiu (specifické)
   │         802.5, …       │
   └────────────────────────┘
   OSI vrstva 1 (Fyzická)
```

### Klíčové standardy
| Standard | Co řeší |
|---|---|
| **IEEE 802.1** | architektura, mosty (bridging), VLAN (802.1Q), spanning tree (802.1D) |
| **IEEE 802.2** | **LLC** – logické řízení linky (společné pro všechny MAC) |
| **IEEE 802.3** | **Ethernet** (CSMA/CD) |
| 802.4 | Token Bus (historicky) |
| **802.5** | **Token Ring** (IBM) |
| 802.6 | DQDB – MAN (historicky) |
| 802.7 | broadband (historicky) |
| 802.8 | optická vlákna (historicky) |
| 802.9 | integrovaný hlas + data |
| 802.10 | bezpečnost |
| **802.11** | **Wi-Fi / WLAN** |
| **802.15** | **WPAN** – Bluetooth (802.15.1), ZigBee (802.15.4) |
| **802.16** | **WiMAX** (WMAN) |
| 802.17 | Resilient Packet Ring |

### Klíčová fakta pro zkoušku
- **IEEE 802.3 = Ethernet** (standard CSMA/CD na 1 Gb/s a méně).
- **IEEE 802.11 = Wi-Fi** (CSMA/CA).
- **IEEE 802.2 = LLC** (společná horní podvrstva linkovky).
- **Předložen standard Ethernetu**: **802.3**.
- **Standard popisující LAN s CSMA/CD**: **802.3**.
- **Standard pro bezdrátové sítě**: **802.11**.
- **Standard pro Bluetooth**: **802.15.1**.

### Vzorová odpověď
IEEE 802 je rodina standardů od IEEE pro LAN/MAN/WLAN. Pokrývá fyzickou a linkovou vrstvu OSI a linkovou rozděluje na dvě podvrstvy: LLC (802.2 – logické řízení, společné) a MAC (specifické: 802.3 Ethernet, 802.11 Wi-Fi, 802.15 Bluetooth/ZigBee, 802.16 WiMAX). Klíčové k zapamatování: 802.3 = Ethernet (CSMA/CD), 802.11 = Wi-Fi (CSMA/CA), 802.2 = LLC.

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

## 17) Potvrzování PDU včetně potvrzování TCP

### Proč se potvrzuje
Pokud chce odesílatel **mít jistotu, že paket dorazil**, příjemce musí potvrdit. Typy potvrzování se liší dle „kdy" a „jak" potvrzuje.

### Typy potvrzování PDU
| Typ                          | Princip                                                         | Příklad               |
| ---------------------------- | --------------------------------------------------------------- | --------------------- |
| **Pozitivní (ACK)**          | příjemce potvrzuje doručené PDU                                 | TCP                   |
| **Negativní (NAK)**          | příjemce potvrzuje **až chybu** (nedoručené/poškozené)          | některé sériové linky |
| **Kombinované**              | ACK + NAK podle situace                                         | –                     |
| **Skupinové**                | jedno potvrzení pokrývá celé skupiny PDU (např. ACK na N rámců) | sliding window        |
| **Nesamostatné (piggyback)** | potvrzení „svezeno" v datovém PDU jdoucím opačným směrem        | TCP duplex            |

### Ke ztrátě potvrzení – chování
| Typ                            | Co se stane při ztrátě ACK                     |
| ------------------------------ | ---------------------------------------------- |
| Pozitivní                      | odesílatel **opakovaně vysílá data** (timeout) |
| Negativní                      | nic se nestane (pokud nepřišlo NAK, vše OK)    |
| **Skupinové bez číslování**    | **zdvojení dat** (příjemce dostane podruhé)    |
| **Nesamostatné bez číslování** | **zdvojení dat**                               |

> Klíč: **pozitivní → opakované vysílání**; **skupinové a nesamostatné bez číslování → zdvojení PDU**. (Číslování v hlavičce tomu zabrání – příjemce duplikát detekuje a zahodí.)

### Potvrzování v TCP
TCP používá **pozitivní potvrzování s posuvným oknem (sliding window)** a **kumulativní ACK**.

#### TCP segment hlavička (klíčová pole)
| Pole | Význam |
|---|---|
| **Sequence Number** | pořadí prvního bajtu v segmentu |
| **Acknowledgment Number** | pořadí dalšího očekávaného bajtu (kumulativní ACK) |
| **Window Size** | kolik bajtů ještě může příjemce přijmout |
| Flags | SYN, ACK, FIN, RST, PSH, URG |
| Checksum | kontrolní součet |

#### Třícestný handshake (navázání spojení)
```
Klient                              Server
  │ ──── SYN, seq=x ─────────────→ │
  │ ←─── SYN+ACK, seq=y, ack=x+1 ─│
  │ ──── ACK, ack=y+1 ───────────→│
   spojení navázáno
```

#### Posuvné okno (sliding window)
- Odesílatel pošle několik segmentů **bez čekání** na ACK (do velikosti okna).
- Příjemce posílá ACK s **„očekávaným dalším bajtem"** – kumulativní.
- Pokud chybí segment uprostřed → příjemce posílá **duplikátní ACK** (selektivní opakování přes SACK).

#### Příklad
```
Seq=1:  data 1-1000   →
Seq=1001: data 1001-2000 →
Seq=2001: data 2001-3000 →
                            ← ACK=3001  (vše do 3001 OK, čekám další)
```

#### Ztráta segmentu a opakování
- Po vypršení **retransmission timeout (RTO)** → opakuje neACKnuté segmenty.
- **Fast retransmit**: 3 duplikátní ACK → ihned opakuj, nečekej RTO.

#### Uzavření spojení (4-way)
```
Klient                          Server
  │ ──── FIN ──────────────→  │
  │ ←─── ACK ─────────────────│
  │ ←─── FIN ─────────────────│
  │ ──── ACK ──────────────→  │
```

### Vzorová odpověď
Potvrzování PDU má pět typů: pozitivní (ACK – potvrzení doručení), negativní (NAK – jen při chybě), kombinované, skupinové (1 ACK za víc PDU) a nesamostatné (piggyback – ACK svezený s daty). Při ztrátě ACK u pozitivního dojde k opakovanému vysílání; u skupinového a nesamostatného bez číslování v hlavičce dojde ke zdvojení. TCP používá pozitivní potvrzování s posuvným oknem a kumulativním ACK (Acknowledgment Number = pořadí dalšího očekávaného bajtu). Spojení se navazuje 3-way handshakem (SYN, SYN+ACK, ACK) a uzavírá 4-way (FIN, ACK, FIN, ACK). Při ztrátě segmentu se po RTO opakuje, případně fast retransmit při 3 duplikátech ACK.

---

## 18) Síťové protokoly – TCP/IP historie, struktura, MTU, TTL

### Historie TCP/IP
- **1970** – DARPA začíná vývoj sítí; používal se protokol NCP v ARPANETu.
- **1977** – zahájen vývoj **TCP/IP** (Vint Cerf, Bob Kahn).
- **1983** – **TCP/IP nahrazuje NCP** v ARPANETu (flag day 1. 1. 1983).
- **1984** – DNS přidán.

### Struktura – TCP/IP model (5-vrstvý)
| # | TCP/IP vrstva | Odpovídá OSI | Příklady protokolů |
|---|---|---|---|
| 5 | **Aplikační** | 5, 6, 7 | HTTP, FTP, SMTP, DNS, Telnet, SSH |
| 4 | **Transportní** | 4 | **TCP, UDP** |
| 3 | **Síťová (Internetová)** | 3 | **IP**, ICMP, ARP, IGMP |
| 2 | **Linková** | 2 | Ethernet, Wi-Fi, PPP |
| 1 | **Fyzická** | 1 | TP, FO, vzduch |

> **Aplikační vrstva TCP/IP** = OSI 5 + 6 + 7 sloučeno do jedné.

### Klíčové součásti (rodina TCP/IP)
| Protokol | Vrstva | Funkce |
|---|---|---|
| **IP** (IPv4/IPv6) | 3 | datagramová, nespojovaná, nepotvrzovaná služba |
| **ICMP** | 3 | chybové a řídicí zprávy (ping, traceroute) |
| **ARP** | 3 | převod IP → MAC |
| **RARP** | 3 | převod MAC → IP (historické) |
| **IGMP** | 3 | správa multicast skupin |
| **DHCP / BootP** | 3 (z hlediska funkce) | přidělování IP adres a parametrů |
| **TCP** | 4 | spojovaný, spolehlivý, ACK |
| **UDP** | 4 | nespojovaný, nespolehlivý, rychlý |
| **HTTP/HTTPS** | 5 | web |
| **DNS** | 5 (relační v OSI) | doménová jména ↔ IP |
| **SMTP/POP3/IMAP** | 5 | pošta |
| **FTP/TFTP** | 5 | přenos souborů |
| **SSH/Telnet** | 5 | vzdálené terminály |
| **SNMP** | 5 | správa síťových prostředků |
| **NTP** | 5 | synchronizace času |
| **LDAP** | 5 | adresářové služby |

### MTU (Maximum Transmission Unit)
**MTU** = maximální délka **paketu/PDU** v dané části sítě (typicky v bajtech).
- **Ethernet MTU** = **1500 B** (data v rámci 802.3 jsou 46–1500 B).
- Wi-Fi MTU = 2304 B (v praxi 1500 B).
- PPPoE = 1492 B.

#### Fragmentace
Když paket je **větší než MTU** další linky:
1. Router (zařízení na L3) **fragmentuje** paket na menší kousky.
2. Každý fragment dostane vlastní IP hlavičku s **fragment offset**.
3. **Sestavení zpět** dělá **cílové zařízení na síťové vrstvě** (ne mezilehlé routery!).
4. IPv6 nefragmentuje na cestě – buď jde celý, nebo se vrací ICMP zpráva „Packet too big".

### TTL (Time To Live)
**TTL** = pole v hlavičce **3. vrstvy (IP)**, určuje **kolik routerů (hopů) paket ještě smí projít**.

#### Co router udělá
1. Při průchodu routerem: **TTL = TTL − 1**.
2. **Pokud TTL = 0** → router **paket zahodí** a pošle ICMP „Time Exceeded" zpět odesílateli.

#### K čemu to slouží
- **Ochrana proti smyčkám** – paket nemůže nekonečně kolovat.
- **Traceroute** funguje tak, že posílá pakety s rostoucím TTL (1, 2, 3…) a sbírá ICMP odpovědi.

#### Typické iniciální hodnoty
- Linux: 64
- Windows: 128
- Cisco: 255

### Vzorová odpověď
TCP/IP vznikl v 70. letech, vývoj 1977, do ARPANETu nasazen 1983. Model TCP/IP má 5 vrstev: fyzická, linková, síťová (IP), transportní (TCP/UDP), aplikační (sloučení OSI 5-7). Hlavní součásti: IP (L3 – datagramová), TCP (L4 – spojovaná, spolehlivá), UDP (L4 – nespolehlivá), ARP (IP→MAC), ICMP (chyby), DNS, DHCP. MTU je maximální velikost paketu na lince (Ethernet 1500 B) – větší pakety router fragmentuje, sestavuje cílový uzel na L3. TTL je pole v IP hlavičce, každý router ho dekrementuje o 1; při TTL=0 paket zahodí a pošle ICMP Time Exceeded – chrání před smyčkami a slouží traceroute.

---

## 19) IPv4 – původní a současná koncepce

### Adresa
- **IPv4 adresa = 32 bitů = 4 byte**.
- Zápis: **dekadicky po bajtech**, oddělené tečkami: `192.168.1.42`.
- Každý oktet: **0–255**.

### Původní koncepce – třídy adres (1981, Classful)
| Třída | 1. byte | Bity sítě / hosta | Výchozí maska | Síť/host |
|---|---|---|---|---|
| **A** | 1–127 | 8 / 24 | 255.0.0.0 (/8) | 128 sítí / 16 777 214 hostů |
| **B** | 128–191 | 16 / 16 | 255.255.0.0 (/16) | 16 384 sítí / 65 534 hostů |
| **C** | 192–223 | 24 / 8 | 255.255.255.0 (/24) | ≈2 mil. sítí / 254 hostů |
| **D** | 224–239 | – (multicast) | – | skupinové adresování |
| **E** | 240–255 | – (rezerva) | – | experimentální, nepoužívá se |

#### Bity prvního bytu
- A: `0xxxxxxx` (0 na začátku)
- B: `10xxxxxx`
- C: `110xxxxx`
- D: `1110xxxx`
- E: `1111xxxx`

#### Využití tříd
- **A, B, C** = unicast (jednotlivé počítače).
- **D** = multicast (skupinové).
- **E** = rezerva, experimenty.

#### Problém původní koncepce
Velké třídy plýtvaly adresami: kdo dostal třídu A, měl 16 milionů adres, ale využil jich pár tisíc. **Adresy IPv4 by došly velmi rychle.**

### Současná koncepce – CIDR (Classless Inter-Domain Routing, 1993)
**CIDR = beztřídové směrování.** Místo pevných tříd se používá **prefix /n** – kolik bitů zleva tvoří síťovou část. Třídy A/B/C **stále existují**, ale jen jako orientační (např. defaultní masky), reálně se dělí libovolně.

#### Zápis CIDR
- `192.168.1.0/24` – 24 bitů sítě, 8 bitů hosta.
- `10.0.0.0/8` – třída A, ale CIDR umožňuje libovolně dělit.
- `200.10.10.0/26` – třída C rozdělená na subsítě po 64 adresách.

#### Výhody CIDR
- Efektivnější využití adresního prostoru.
- **Agregace tras** (supernetting) – jeden záznam v routing tabulce pokryje víc sítí.

### NAT (Network Address Translation)
Další způsob šetření – **privátní adresy** uvnitř LAN, jedna **veřejná** vůči Internetu.
- 1 veřejná IP → mnoho privátních počítačů.
- NAT překládá adresy a porty (PAT/Overload).

### IPv6
Dlouhodobé řešení nedostatku adres: **128 bitů** místo 32. Viz okruh 23.

### Vzorová odpověď
IPv4 adresa je 32 bitů zapsaná dekadicky po bajtech (4 oktety 0-255). Původní koncepce (1981) dělila adresy do tříd A, B, C podle prvního bajtu – třídy měly pevně danou síťovou masku 8/16/24 bitů. Třída D je multicast, E rezerva. Tahle koncepce plýtvala adresami, proto v 1993 přišlo CIDR – beztřídové dělení s prefixem /n. Místo tříd se masky dají libovolně. Druhou nouzovou cestou bylo NAT – privátní adresy schované za jednu veřejnou. Dlouhodobé řešení je ale IPv6 (128 bitů).

---

## 20) IPv4 – speciální vyhrazené a privátní adresy

### Speciální vyhrazené adresy
| Adresa / rozsah | Význam |
|---|---|
| **0.0.0.0** | zařízení **nezná svou adresu** (před DHCP); v routing tabulce = defaultní cesta |
| **0.0.0.0/8** | „this network" – rezervováno |
| **127.0.0.0/8** | **loopback** (typicky 127.0.0.1 = localhost) |
| 127.255.255.254 | loopback (rezerva) |
| **169.254.0.0/16** | **APIPA / link-local** (Auto-IP když selže DHCP) |
| **224.0.0.0/4** | **multicast** (třída D) |
| **240.0.0.0/4** | rezerva (třída E) |
| **255.255.255.255** | **omezený broadcast** (limited broadcast) – zůstává v lokální síti |
| `x.x.x.0` (adresa sítě/subsítě) | první adresa v podsíti, **nepoužitelná pro hosta** |
| `x.x.x.255` (broadcast subsítě) | poslední adresa, broadcast subsítě – **nepoužitelná pro hosta** |

### Privátní (neveřejné) adresy
Definované RFC 1918 – **nesměrují se přes Internet**, jen v lokálních sítích, **používají se za NAT**.

| Třída | Rozsah | Prefix |
|---|---|---|
| **A** | **10.0.0.0 – 10.255.255.255** | /8 |
| **B** | **172.16.0.0 – 172.31.255.255** | /12 |
| **C** | **192.168.0.0 – 192.168.255.255** | /16 |

#### Příklady
| Adresa | Typ |
|---|---|
| 10.5.16.131 | privátní třídy A (za NAT) |
| 172.20.18.131 | privátní třídy B (za NAT) |
| 192.168.16.131 | privátní třídy C (za NAT/proxy) |
| 195.178.90.15 | **veřejná** (není vyhrazená) |
| 0.0.0.0 | zařízení nezná adresu |
| 255.255.255.255 | omezený broadcast |
| 169.254.5.10 | APIPA (DHCP selhal) |

### Loopback
- **127.0.0.0/8** – celá síť pro loopback, typicky **127.0.0.1** = localhost.
- Pakety se nedostanou na drát, vrací se zpět do TCP/IP stacku.
- Slouží k testování síťových aplikací bez fyzické sítě.

### APIPA (Automatic Private IP Addressing)
- Pokud klient **neúspěšně dotazuje DHCP**, Windows mu přidělí adresu z **169.254.0.0/16**.
- Slouží k provizorní komunikaci v LAN bez DHCP.
- Nemá výchozí bránu → nelze ven z LAN.

### Multicast (třída D)
- **224.0.0.0/4** (224.0.0.0 – 239.255.255.255).
- Vybrané vyhrazené:
  - **224.0.0.1** = all hosts in subnet.
  - **224.0.0.2** = all routers in subnet.
  - **224.0.0.5/6** = OSPF routery.
- IGMP řídí členství ve skupinách.

### Vzorová odpověď
IPv4 má řadu speciálních a vyhrazených adres. 0.0.0.0 znamená „neznám svou adresu" (DHCP request) nebo defaultní cesta. 127.0.0.0/8 je loopback (127.0.0.1 = localhost). 169.254.0.0/16 je APIPA – přiřadí se klientovi, když selhal DHCP. 224.0.0.0/4 je multicast (třída D), 240.0.0.0/4 rezerva (třída E). 255.255.255.255 je omezený broadcast. Privátní (neveřejné) adresy podle RFC 1918 nelze směrovat přes Internet, používají se za NAT: 10.0.0.0/8 (třída A), 172.16-31.0.0/12 (třída B), 192.168.0.0/16 (třída C).

---

## 21) IPv4 – síťová a subsíťová maska. Dělení na subsítě

### Síťová maska (Subnet Mask)
**Maska** říká, **kolik bitů z IP adresy tvoří síť** a kolik tvoří hosta.
- Binárně: jedničky zleva (síť), pak nuly (host).
- Dekadicky: 4 byty po tečkách jako IP adresa.
- **Prefix /n** = počet jedniček v masce zleva.

| Prefix | Maska dekadicky |
|---|---|
| /8 | 255.0.0.0 |
| /16 | 255.255.0.0 |
| /24 | 255.255.255.0 |
| /25 | 255.255.255.128 |
| /26 | 255.255.255.192 |
| /27 | 255.255.255.224 |
| /28 | 255.255.255.240 |
| /29 | 255.255.255.248 |
| /30 | 255.255.255.252 |

#### Hodnoty bajtu masky
| Poslední byte | Binárně | Půjčených bitů |
|---|---|---|
| 128 | 10000000 | 1 |
| 192 | 11000000 | 2 |
| 224 | 11100000 | 3 |
| 240 | 11110000 | 4 |
| 248 | 11111000 | 5 |
| 252 | 11111100 | 6 |
| 254 | 11111110 | 7 |
| 255 | 11111111 | 8 |

### Výpočet adresy sítě
**Adresa sítě** = IP **AND** maska (po bitech).

#### Příklad
```
IP:      192.168.10.130    11000000.10101000.00001010.10000010
Maska:   255.255.255.192   11111111.11111111.11111111.11000000
AND ─────────────────────────────────────────────────────────────
Síť:     192.168.10.128    11000000.10101000.00001010.10000000
```

### Dělení sítí na subsítě (subnetting)
**Subnetting** = ze sítě vytvořím **více menších podsítí** tím, že **„půjčím" bity z hostitelské části** do síťové.

#### Vzorec
- **Počet subsítí = 2ⁿ**, kde n = počet půjčených bitů.
- **Počet hostů na subsíť = 2^(bitů hosta) − 2** (odečítáme adresu sítě a broadcast).

#### Příklad: dělení třídy C (192.168.10.0/24) na subsítě po /26
- Půjčíme 2 bity → 4 subsítě.
- Každá má 32 − 26 = 6 bitů hosta → 2⁶ − 2 = **62 použitelných hostů**.

| # | Síť | První host | Poslední host | Broadcast |
|---|---|---|---|---|
| 1 | 192.168.10.0/26 | .1 | .62 | .63 |
| 2 | 192.168.10.64/26 | .65 | .126 | .127 |
| 3 | 192.168.10.128/26 | .129 | .190 | .191 |
| 4 | 192.168.10.192/26 | .193 | .254 | .255 |

#### Tabulka výsledných hostů
| Prefix | Bitů hosta | 2ⁿ | Použitelné (−2) |
|---|---|---|---|
| /23 | 9 | 512 | **510** |
| /24 | 8 | 256 | **254** |
| /25 | 7 | 128 | **126** |
| /26 | 6 | 64 | **62** |
| /27 | 5 | 32 | **30** |
| /28 | 4 | 16 | **14** |
| /29 | 3 | 8 | **6** |
| /30 | 2 | 4 | **2** |

### Typické otázky
- **Délka prefixu pro dělení třídy B na čtvrtiny**: **/18** (B má /16, 2 půjčené bity = 4 subsítě).
- **Hodnota 2. bajtu při půlení třídy A**: **128** (A má /8, 1 půjčený bit = bit 128 v 2. bajtu).
- **Maska SSM IPv4 má kolik byte**: **4**.
- **První adresa v síti/subsíti**: adresa sítě / subsítě (nepoužitelná pro hosta).
- **Maximum subsítí třídy C, aby zbyly volné adresy pro PC**: **64** (/30 → 2 hosti).

### Vzorová odpověď
Subsíťová maska je 32-bitové číslo s jedničkami zleva (síťová část) a nulami (hostitelská část). Prefix /n udává počet jedniček. Adresu sítě získám logickým AND mezi IP a maskou. Subnetting znamená rozdělení sítě na menší podsítě půjčením bitů z hostitelské části – počet subsítí = 2ⁿ (kde n = počet půjčených bitů), použitelných hostů = 2^bitů_hosta − 2 (mínus síť a broadcast). Třídu C dokážu rozdělit prefixem /26 na 4 subsítě po 62 hostech, prefixem /30 na 64 subsítí po 2 hostech.

---

## 22) IPv4 – šíření paketů s všeobecnou adresou (broadcast)

### Co je broadcast
**Broadcast** = paket adresovaný **všem stanicím** v dané síti / subsíti.

### Dva typy broadcastu
#### 1) Omezený broadcast (limited broadcast)
- Adresa: **255.255.255.255**.
- Šíří se **pouze v aktuální subsíti** (NEpřechází přes router).
- Používá se před DHCP, kdy stanice ještě nezná svou adresu ani adresu sítě.

#### 2) Směrovaný / všesměrový broadcast (directed broadcast)
- Adresa: **adresa sítě s hostitelskou částí samé 1**, např. `192.168.10.255` pro /24, nebo `200.10.10.63` pro /26.
- Mířená na konkrétní subsíť.
- Historicky se mohl šířit přes routery do cílové subsítě, **dnes routery ve výchozím nastavení nepropouštějí** (ochrana proti smurf útokům – RFC 2644).

### Šíření přes různá zařízení
| Zařízení | Broadcast (255.255.255.255) propustí? |
|---|---|
| **Hub / repeater (L1)** | ANO (vidí jen bity, neumí adresy) |
| **Bridge / switch (L2)** | ANO – šíří se v celé **broadcastové doméně** |
| **Router (L3)** | **NE** – broadcastovou doménu ohraničuje router |
| **Routing switch (L3)** | NE – jako router |

> **Router rozděluje broadcastovou doménu.** Hub ani switch ne.

### Broadcastová doména
**Broadcastová doména** = část sítě, kam se rozšíří rámec s **broadcastovou MAC adresou FF:FF:FF:FF:FF:FF**.
- Switch tvoří jednu broadcastovou doménu (na 1 VLAN).
- Router ji ohraničuje – broadcast se na druhou stranu nepropustí.
- VLAN dělí broadcastovou doménu logicky.

### Příklad: PC v 192.168.10.0/24 vyšle 192.168.10.255
```
[PC] ──broadcast──→ [SWITCH] ──→ [PC2, PC3, …všechny v subsíti]
                          │
                          └──→ [ROUTER] ──X── nepropustí dál
```

### Příklad: omezený broadcast 255.255.255.255
- Šíří se **jen v aktuální subsíti** (i kdyby paket měl správnou IP, router nepropustí).

### Multicast (pro srovnání)
Multicast (224.0.0.0/4) = posílám jen vybrané skupině uzlů (kteří se přihlásili přes IGMP). Není všem, je jen těm, co chtějí poslouchat. Šetří kapacitu oproti broadcastu.

### IPv6 nemá broadcast
Důležitá změna: **IPv6 nepoužívá broadcast vůbec**, místo něj **multicast** (např. all-nodes = FF02::1, all-routers = FF02::2).

### Vzorová odpověď
Broadcast je paket adresovaný všem stanicím v síti. IPv4 zná dva typy: omezený broadcast 255.255.255.255 (šíří se jen v aktuální subsíti, používá ho DHCP klient před přidělením adresy) a směrovaný broadcast (adresa subsítě s hostitelskými bity samé 1, např. 192.168.10.255 pro /24). Hub, bridge a switch broadcast propustí v celé broadcastové doméně, ale router ji ohraničuje – přes router se broadcast standardně nešíří. Routery proto definují broadcastové domény, na rozdíl od switchů (které ohraničují jen kolizní doménu). IPv6 broadcast zrušil a nahradil multicastem.

---

## 23) IPv6 – typy adres

### Základní vlastnosti
- **Délka adresy: 128 bitů = 16 byte**.
- **Zápis**: 8 skupin po 4 hex číslicích oddělené dvojtečkou.
  - `2001:0db8:0000:0000:0000:ff00:0042:8329`
- **Zkrácení**: jedna sekvence nul lze nahradit `::` (jen jednou v adrese).
  - `2001:db8::ff00:42:8329`
- Vedoucí nuly v každé skupině lze vypustit.
- **IPv6 nemá broadcast** – nahradil ho multicast.

### POZOR – chyták na existující verze IP
| Verze | Existuje? | Délka |
|---|---|---|
| **IPv4** | ANO | **4 byte = 32 bit** |
| IPv5 | NE (rezervováno pro experimentální ST/ST2 protokol, **nikdy nenasazeno**) | – |
| **IPv6** | ANO | **16 byte = 128 bit** |
| **IPv7, IPv8, IPv9** | **NEEXISTUJÍ** jako standardy | – |

> Tahák může mít otázku „Z kolika byte je složena IP adresa verze 8?" – **správná odpověď: IPv8 neexistuje / žádná**. Stejně pro IPv5, IPv7, IPv9. Reálně se používají jen IPv4 a IPv6.

### Tři základní typy adres
| Typ | Princip |
|---|---|
| **Unicast** | jeden konkrétní příjemce |
| **Multicast** | skupina příjemců (kdo se přihlásí) |
| **Anycast** | nejbližší z dané skupiny (záleží na směrování) |

> Pozor: **broadcast v IPv6 NEexistuje**.

### Konkrétní rozsahy adres
| Typ adresy | Prefix | Význam |
|---|---|---|
| **Globální unicast (GUA)** | **2000::/3** | „veřejná" IPv6 adresa (analog veřejné IPv4) |
| **Link-local (LLA)** | **FE80::/10** | unikátní jen v segmentu (1 link), automaticky |
| **Unique local (ULA)** | **FC00::/7** (FC.. nebo FD..) | privátní v rámci organizace (analog 10.x v IPv4) |
| **Multicast** | **FF00::/8** | skupinové adresování |
| **All-nodes link-local** | **FF02::1** | všichni v segmentu (jako broadcast) |
| **All-routers link-local** | **FF02::2** | všechny routery v segmentu |
| **Solicited-node multicast** | FF02::1:FFXX:XXXX | adresa pro DAD a Neighbor Discovery |
| **Loopback** | **::1/128** | localhost (analog 127.0.0.1) |
| **Neznámá adresa** | **::/128** | „nemám adresu" (jako 0.0.0.0) |
| **IPv4-mapped** | ::FFFF:0:0/96 | IPv4 adresa zapsaná v IPv6 |

### Struktura globální unicast adresy
```
| 48 bitů GRP (Global Routing Prefix) | 16 bitů Subnet ID | 64 bitů Interface ID |
|             (od ISP/RIR)            |   (správce sítě)   |   (identifikuje hosta) |
```
- Hostitelská část je vždy **64 bitů**.
- Síťová část = 48 + 16 = 64 bitů.

### Link-local (LLA)
- Každé rozhraní má **automaticky** přidělenou LLA hned po zapnutí.
- Prefix **FE80::/10**, ale dalších 54 bitů je 0 → praktický prefix **FE80::/64**.
- Slouží **pro komunikaci v rámci jednoho linku** – Neighbor Discovery (NDP), DHCPv6, OSPF…
- **Nenajdu LLA v Internetu** – nesměrují se.

### Multicast v IPv6
- Nahrazuje broadcast.
- Klíčové skupiny:
  - **FF02::1** – all nodes (broadcast ekvivalent)
  - **FF02::2** – all routers
  - **FF02::1:FFXX:XXXX** – solicited-node (pro DAD)

### Vzorová odpověď
IPv6 adresa má 128 bitů, zapisuje se hex po 16 bitech oddělených dvojtečkou, jednu sekvenci nul lze zkrátit dvojtečkami ::. Existují tři typy: unicast (1 příjemce), multicast (skupina), anycast (nejbližší z více). Broadcast IPv6 nemá. Klíčové prefixy: globální unicast 2000::/3 (veřejná), link-local FE80::/10 (jen v linku, automaticky), unique local FC00::/7 (privátní), multicast FF00::/8. Speciální adresy: ::1 loopback, ::/128 neznámá, FF02::1 all-nodes, FF02::2 all-routers. Hostitelská část GUA je vždy 64 bitů.

---

## 24) IPv6 – přidělování Link-local a Globální unicast adresy hostu

### Krok 1: Link-local (LLA) – vždy první
Hned po zapnutí rozhraní si host **automaticky** vygeneruje LLA:

```
Prefix: FE80::/64
Interface ID (64 bitů): generován z MAC přes EUI-64 nebo náhodný generátor
```

#### Konstrukce LLA s EUI-64
1. Vezmu 48-bit MAC adresu: `AA:BB:CC:DD:EE:FF`
2. Rozdělím na dvě 24-bit poloviny: `AABBCC` | `DDEEFF`
3. Vložím doprostřed `FFFE`: `AABBCC` **FFFE** `DDEEFF`
4. **Invertuju 7. bit prvního bytu** (Universal/Local bit): `AA` (1010 1010) → `A8` (1010 1000)
5. Výsledný Interface ID: `A8BB:CCFF:FEDD:EEFF`
6. LLA = `FE80::A8BB:CCFF:FEDD:EEFF`

#### Konstrukce LLA s náhodným generátorem (privacy extensions)
- Moderní OS (Windows, macOS, Linux) preferují **náhodně generovaný Interface ID** – kvůli soukromí (MAC adresa neprozradí výrobce ani sledování pohybu).
- Náhodné Interface ID se může pravidelně měnit.

### Krok 2: Verifikace adresy přes DAD
Před použitím každé adresy (LLA i GUA) host provede **Duplicate Address Detection** (viz okruh 25). Pokud zjistí konflikt, adresu nepoužije.

### Krok 3: Globální unicast (GUA)
Pro komunikaci s Internetem host potřebuje **globální unicast adresu**. Tři varianty (viz okruh 26):

#### a) SLAAC (Stateless Address Autoconfiguration)
1. Host pošle **Router Solicitation (RS)** na `FF02::2` (all-routers).
2. Router odpoví **Router Advertisement (RA)** s **prefixem sítě** (typicky /64) a defaultní bránou.
3. Host si **sám sestaví GUA** = prefix + Interface ID (EUI-64 nebo náhodný).
4. Provede DAD.
5. **Bez serveru, bez state.**

#### b) Stateful DHCPv6
1. Host pošle DHCPv6 Solicit na multicast `FF02::1:2`.
2. DHCPv6 server odpoví s **konkrétní GUA** + dalšími parametry.
3. Host adresu použije po DAD.

#### c) Stateless DHCPv6
- SLAAC + DHCPv6 jen pro **další parametry** (DNS servery, NTP).
- Host adresu sestaví sám (jako SLAAC), DHCPv6 dodá metadata.

### Speciální stavy
- **`::/128`** – host „nemá adresu" (před přidělením, jako 0.0.0.0 v IPv4).
- LLA má každý host **vždy**, nezávisle na ostatních.

### Vzorová odpověď
Host si nejdřív po zapnutí rozhraní automaticky vyrobí Link-local adresu (LLA) – prefix FE80::/64 + Interface ID. Interface ID se generuje buď algoritmem EUI-64 z MAC adresy (vloží FFFE doprostřed a invertuje 7. bit prvního bajtu) nebo náhodným generátorem (privacy extensions). LLA slouží jen pro komunikaci v rámci linku (Neighbor Discovery, DHCPv6 init). Pro komunikaci ven host potřebuje globální unicast (GUA) – tři způsoby získání: SLAAC (host si sám sestaví prefix + Interface ID z Router Advertisementu), stateful DHCPv6 (server přidělí konkrétní adresu), nebo stateless DHCPv6 (SLAAC + DHCPv6 jen pro DNS/NTP). Před použitím každé adresy host provede DAD.

---

## 25) IPv6 – EUI-64, generátor náhodných čísel, DAD

### Algoritmus EUI-64
**Cíl**: vytvořit 64-bit **Interface Identifier** z 48-bit **MAC adresy**.

#### Postup
1. **Vezmu MAC**: `AABBCC-DDEEFF` (3+3 byte, ale obvykle se píše s pomlčkami/dvojtečkami).
2. **Rozdělím** na **OUI** (3 byte = vendor) a **NIC** (3 byte = id karty).
3. **Vložím `FFFE` mezi OUI a NIC**: `AABBCC` + **FFFE** + `DDEEFF` → 8 byte = 64 bit.
4. **Invertuju 7. bit prvního bajtu** (U/L bit = Universal/Local).
   - Pokud byl 0 (Universal, globálně unikátní), bude 1 (Local).
   - Funguje jako přepínač interpretace adresy.

#### Příklad
```
MAC:       0050:56C0:0008
Rozdělím:  0050:56  C0:0008
Vložím FFFE: 0050:56FF:FEC0:0008
Invertuj 7. bit prvního bajtu:
  0x00 = 00000000  →  invert bit 7 (z LSB) = 00000010 = 0x02
Výsledný IID: 0250:56FF:FEC0:0008
LLA:        FE80::250:56FF:FEC0:0008
```

#### Proč invertovat U/L bit?
V MAC formátu: 0 = globálně unikátní adresa, 1 = lokálně administrovaná.
V EUI-64: význam je obrácený, takže invertujeme.

### Generátor náhodných čísel (Privacy Extensions, RFC 4941/8981)
**Problém EUI-64**: Interface ID je odvozený z MAC → unikátní identifikátor zařízení putuje s ním po Internetu. **Hrozba sledování.**

**Řešení**: Interface ID se generuje **náhodně** (kryptografická hashová funkce + náhodné semínko), pravidelně se mění (typ. 1× denně), staré adresy se zachovají do vypršení.

#### Vlastnosti
- Náhodný 64-bit IID.
- Lze používat současně s EUI-64 adresou.
- **Výchozí ve Windows, macOS, novějších Linuxech.**
- U/L bit se nastavuje na 0 (lokální).

### DAD – Duplicate Address Detection
**Účel**: před použitím nově sestavené adresy si **ověřit, že ji nemá nikdo jiný** v segmentu.

#### Algoritmus DAD
1. Host **dočasně** přidělí adresu rozhraní s příznakem **tentative**.
2. Pošle **Neighbor Solicitation (NS)** na **solicited-node multicast** adresy `FF02::1:FFXX:XXXX` (kde XXXX je posledních 24 bitů adresy).
3. Cílová adresa NS = ověřovaná adresa. Zdrojová adresa = `::` (neznámá).
4. **Čeká** určitý čas (RetransTimer, výchozí 1 s).
5. **Pokud odpověď NS od jiného hosta** = adresa je obsazená → host adresu **NEPOUŽIJE** (oznámí konflikt).
6. **Pokud neodpoví nikdo** = adresa je volná → host ji nastaví jako **preferred** a začne používat.

#### Vizualizace
```
Host A chce použít FE80::A8BB:CCFF:FEDD:EEFF
   │
   ├──→ NS (target: FE80::A8BB:CCFF:FEDD:EEFF) na FF02::1:FFDD:EEFF
   │    src: ::, dst: solicited-node multicast
   │
   ├──→ čeká
   │
   ▼
 Žádná odpověď → adresa volná → použiju
 Odpověď NA → adresa zabraná → konflikt!
```

#### Co se kontroluje
- **Každou** unicast adresu (LLA, GUA, ULA).
- Probíhá vždy při **prvním přidělení**.
- IPv6 standard to **vyžaduje** (RFC 4862).

### Vzorová odpověď
EUI-64 je algoritmus pro odvození 64-bitového Interface ID z 48-bit MAC: rozdělím MAC na dvě poloviny, vložím doprostřed FFFE a invertuju 7. bit prvního bajtu (U/L bit). Výsledek se připojí k prefixu (FE80::/64 pro LLA, nebo prefix z RA pro GUA). Místo EUI-64 se dnes preferuje náhodný generátor (Privacy Extensions, RFC 4941/8981) – odstraňuje sledovatelnost přes MAC, IID se pravidelně mění. Před použitím každé adresy host provede DAD (Duplicate Address Detection): pošle Neighbor Solicitation na solicited-node multicast s ověřovanou adresou jako cílem. Pokud někdo odpoví, adresa je obsazená a host ji nepoužije; pokud nikdo, adresa je volná.

---

## 26) IPv6 – tři varianty dynamického přidělování adres

### Přehled
Pro získání **globální unicast adresy (GUA)** IPv6 host má tři možnosti:

| Varianta | State | Adresa | Další parametry |
|---|---|---|---|
| **SLAAC** | bez state | host si sestaví sám | z RA |
| **Stateless DHCPv6** | bez state | host si sestaví sám (SLAAC) | z DHCPv6 |
| **Stateful DHCPv6** | se state | server přidělí | z DHCPv6 |

### 1) SLAAC (Stateless Address Autoconfiguration)
**Bez serveru, bez evidence.** Host komunikuje pouze s routerem.

#### Postup
```
1. Host po zapnutí má LLA (FE80::...).
2. Host pošle Router Solicitation (RS) na FF02::2 (all-routers).
3. Router odpoví Router Advertisement (RA), obsahuje:
   - Prefix sítě (typ. /64)
   - Defaultní bránu (= LLA routeru)
   - Flag M (Managed) = 0
   - Flag O (Other) = 0
4. Host složí GUA: prefix + Interface ID (EUI-64 nebo random).
5. Provede DAD.
6. Adresu začne používat.
```

#### Výhody
- Bez DHCP serveru – jednodušší infrastruktura.
- Vhodné pro malé sítě a domácnosti.

#### Nevýhody
- **Bez DNS** – pokud nepřijde RA s DNS volbou (RDNSS).
- Bez evidence kdo má jakou adresu.

### 2) Stateful DHCPv6
**Plnohodnotný DHCP** pro IPv6 – server **přiděluje a eviduje** adresy.

#### Postup
```
1. RA má flag M (Managed) = 1.
   → Host ví, že má použít DHCPv6.
2. Host pošle DHCPv6 Solicit na FF02::1:2 (all DHCP servers).
3. DHCPv6 server odpoví Advertise.
4. Host pošle Request.
5. Server pošle Reply s konkrétní GUA + DNS + lease.
6. Host provede DAD a adresu použije.
```

#### Výhody
- **Centrální evidence** přidělených adres.
- Plná kontrola síťového administrátora.
- Dodávky DNS, NTP, dalších parametrů.

#### Nevýhody
- Vyžaduje DHCPv6 server (složitější infrastruktura).
- Defaultní bránu **stále poskytuje router přes RA** (DHCPv6 neumí předat default gateway!).

### 3) Stateless DHCPv6
**Hybrid**: SLAAC pro adresu + DHCPv6 jen pro **metadata**.

#### Postup
```
1. RA má flag M = 0, O = 1 (Other config).
   → Host ví, že má adresu z SLAAC, ale o DNS si má říct DHCPv6.
2. Host složí GUA podle SLAAC.
3. Host kontaktuje DHCPv6 server jen pro DNS, NTP, doménové jméno.
4. DHCPv6 server odpoví Information Reply (bez adresy).
```

#### Výhody
- Adresa bez DHCP state (SLAAC).
- Doplňkové parametry (DNS) z centrálního zdroje.
- Kompromis mezi SLAAC a Stateful DHCPv6.

### Srovnání
| Vlastnost | SLAAC | Stateless DHCPv6 | Stateful DHCPv6 |
|---|---|---|---|
| Adresa | host sám | host sám | server |
| DNS | (RDNSS v RA) | DHCPv6 | DHCPv6 |
| Default GW | router (RA) | router (RA) | router (RA) |
| Evidence | NE | NE | ANO |
| Flag M v RA | 0 | 0 | 1 |
| Flag O v RA | 0 | 1 | (typ. 1) |

### Vzorová odpověď
IPv6 host má tři způsoby dynamického získání globální unicast adresy. **SLAAC** je bezstavová autokonfigurace – host pošle Router Solicitation, dostane Router Advertisement s prefixem a defaultní bránou, sám sestaví adresu (prefix + Interface ID z EUI-64 nebo random). **Stateful DHCPv6** funguje jako klasické DHCP – server přiděluje konkrétní adresu a vede o ní evidenci; aktivuje se flagem M=1 v RA. **Stateless DHCPv6** je hybrid: adresu si host sestaví sám (SLAAC), ale DNS a další parametry dostane z DHCPv6; aktivuje se flagem O=1. Defaultní bránu vždy dodává router přes RA (DHCPv6 to neumí).

---

## 27) TCP/IP port a socket. Dělení portů. Demultiplexování

### Port
**Port** = 16-bitové číslo (**0–65535**), identifikuje **konkrétní službu/aplikaci** na hostiteli. Bez portu by transportní vrstva nevěděla, které aplikaci data předat.

> Port je **TSAP** (Transport Service Access Point) v terminologii OSI.

### Dělení portů (IANA)
| Rozsah | Název | Použití |
|---|---|---|
| **0 – 1023** | **Well-known (všeobecné)** | systémové služby, vyhrazené (HTTP, FTP, DNS…) |
| **1024 – 49151** | **Registrované** | aplikace registrované u IANA (SQL Server 1433, RDP 3389…) |
| **49152 – 65535** | **Dynamické / soukromé** | klientské porty, NAT, efemérní |

### Důležité porty (well-known)
| Port | Protokol | Služba |
|---|---|---|
| 20 | TCP | FTP – data |
| **21** | TCP | **FTP – řízení** |
| **22** | TCP | **SSH** |
| 23 | TCP | Telnet |
| **25** | TCP | **SMTP** |
| 53 | TCP/UDP | **DNS** |
| 67/68 | UDP | DHCP server / klient |
| 69 | UDP | TFTP |
| **80** | TCP | **HTTP** |
| **110** | TCP | **POP3** |
| **143** | TCP | **IMAP4** |
| 161/162 | UDP | SNMP / SNMP-trap |
| **443** | TCP | **HTTPS** |
| 3389 | TCP | RDP |

### Socket
**Socket** = **kombinace IP adresy + portu + protokolu**. Identifikuje **konec spojení** (endpoint).
- Zápis: `IP:port` (např. `192.168.1.5:80`).
- **Síťové spojení (TCP)** = pár socketů: `(client_IP:client_port, server_IP:server_port)`.

#### Příklad
```
Klient 192.168.1.5 chce HTTPS na google.com (216.58.214.78):
- Socket klienta: 192.168.1.5:49432   (klient si vybral náhodný port z dynamického rozsahu)
- Socket serveru: 216.58.214.78:443
- Spojení = (192.168.1.5:49432 ↔ 216.58.214.78:443)
```

#### Vlastnosti socketu
- **Aplikace si socket otevře** (Berkeley sockets API: socket, bind, listen, accept, connect, send, recv).
- **OS udržuje tabulku** otevřených socketů a směřuje příchozí pakety ke správné aplikaci.

### Demultiplexování
**Demultiplexování** = proces, kterým přijatý paket „prochází vrstvami" a nakonec dorazí ke **správné aplikaci**. Na každé vrstvě se použije identifikátor v hlavičce k rozhodnutí, **kam paket předat výš**.

#### Řetězec demultiplexace
```
[Bity z drátu]
   │
   ▼ L2 (Linková)
[Rámec] – načtu MAC adresu; je moje? Pokud ne, zahodím.
   ↓ Type (Ethernet) nebo DSAP (802.2) → určuje L3 protokol
   │
   ▼ L3 (Síťová)
[Paket] – načtu IP adresu; je moje? Pokud ne, případně přesměruji nebo zahodím.
   ↓ Číslo IP protokolu (např. 6=TCP, 17=UDP, 1=ICMP) → určuje L4
   │
   ▼ L4 (Transportní)
[Segment / Datagram] – načtu cílový port
   ↓ Port → určuje aplikaci (socket)
   │
   ▼ L5–7
[Aplikace] – HTTP server / FTP klient / DNS resolver…
```

#### Klíčová pole pro demultiplexaci
| Vrstva | Pole | Příklad hodnoty |
|---|---|---|
| L2 (Ethernet II) | **Type** | 0x0800 = IPv4, 0x86DD = IPv6, 0x0806 = ARP |
| L2 (802.3 + 802.2 LLC) | **DSAP** | 0x06 = IP, 0xE0 = IPX |
| L3 (IPv4/IPv6) | **Protocol** (IPv4) / **Next Header** (IPv6) | 6 = TCP, 17 = UDP, 1 = ICMP |
| L4 (TCP/UDP) | **Destination Port** | 80 = HTTP, 25 = SMTP |

> Otázka: **Demultiplexace podle**: typu rámce (Ethernet type), čísla IP protokolu, čísla portu – **všechny tři postupně**.

### Vzorová odpověď
Port je 16-bitové číslo identifikující službu na hostiteli (TSAP v OSI terminologii). Porty dělíme na všeobecné (0-1023, např. HTTP 80, SMTP 25, FTP 21), registrované (1024-49151) a dynamické (49152-65535, klientské/efemérní). Socket je IP+port+protokol – identifikuje endpoint spojení; TCP spojení tvoří pár socketů (klient + server). Demultiplexování je proces směrování příchozího paketu vrstvami ke správné aplikaci: na L2 podle Ethernet type určím L3 protokol (IP), na L3 podle čísla IP protokolu určím L4 (TCP/UDP), na L4 podle cílového portu určím aplikaci.

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

## 29) Propojování sítí – router, routing switch L3/L4, gateway, model OSI

### Router (L3 – síťová vrstva)
**Funkce**: směruje pakety mezi sítěmi na základě **IP adres**.

#### Vlastnosti
- Pracuje s **logickými adresami (IP, IPX)** a **routovací tabulkou**.
- **Dělí kolizní doménu**.
- **Dělí broadcastovou doménu** – tady je klíčový rozdíl proti switchi.
- Při průchodu **dekrementuje TTL** o 1 (při TTL=0 paket zahodí).
- Může **fragmentovat** paket (pokud je větší než MTU další linky).
- **Může paket zahodit** (TTL=0, neznámá síť, ACL).
- Provádí směrování podle **routovacích protokolů**:
  - **RIP** – Distance Vector (počet hopů, max 15).
  - **OSPF** – Link State.
  - **EIGRP** – Cisco hybrid.
  - **BGP** – Path Vector, mezi AS (Internet).
- **K rozdělení broadcastové domény slouží router**.

### Routing switch (L3 switch)
**Funkce**: switch + funkce routeru ve stejné krabici. **Přepíná na L3** (podle IP adresy), ale velmi rychle pomocí hardwarového ASIC/FPGA.

#### Vlastnosti
- Hardwarově urychlené směrování – mnohem rychlejší než klasický router.
- Spojuje VLAN, mezi-VLAN routing (Inter-VLAN routing).
- Některá rozhodnutí přesouvá až na **L4 (Routing switch L4)** – směrování podle portů.

### Routing switch L4
**Funkce**: routing switch, který umí rozhodovat i podle **portu (TCP/UDP)**.

#### Vlastnosti
- Filtruje na úrovni portů.
- Umožňuje load balancing podle aplikace (HTTP na jiný server, FTP na jiný).
- Typické v datacentrech, **server load balancing**.

### Gateway (L7 – aplikační vrstva)
**Funkce**: překládá mezi **neslučitelnými systémy** – různé protokoly, různé formáty dat, různé poštovní systémy.

#### Vlastnosti
- Pracuje až na **aplikační vrstvě (L7)**.
- **Plně překládá protokoly i data**.
- Příklad: brána mezi **různými poštovními systémy** (X.400 ↔ SMTP), VoIP ↔ ISDN brána, SIP ↔ H.323.

#### Kdy použít gateway
- Sítě s **nekompatibilními protokoly**.
- Sítě s **nekompatibilními formáty dat** (např. různé poštovní systémy, různé znakové sady).
- Pokud router stačí, používáme router. Gateway je nasazena tam, kde **nestačí pouhé přesměrování paketu** – musí se obsah přeložit.

### Souhrn (rozšířená tabulka z OSI)
| Zařízení | Vrstva OSI | Adresy | Funkce |
|---|---|---|---|
| Repeater, Hub | 1 (fyzická) | – | regenerace signálu |
| Bridge, Switch | 2 (linková) | MAC | přepínání rámců |
| **Router** | **3 (síťová)** | **IP** | **směrování paketů, dělí broadcast** |
| Routing switch L3 | 3 | IP | HW-urychlené směrování |
| Routing switch L4 | 4 | IP + porty | směrování + port-based filtrování |
| **Gateway** | **7 (aplikační)** | aplikační info | překlad protokolů a dat |

### Vzorová odpověď
Router pracuje na 3. vrstvě OSI, směruje pakety podle IP adres, dělí kolizní i broadcastovou doménu, dekrementuje TTL a fragmentuje pakety větší než MTU. Routing switch L3 je hardwarově urychlený router – spojuje funkčnost switche a routeru, používá ASIC/FPGA. Routing switch L4 přidává schopnost rozhodovat podle portů (TCP/UDP) – využívá se pro load balancing. Gateway je až na 7. vrstvě a překládá mezi neslučitelnými protokoly / formáty dat (např. brána mezi různými poštovními systémy nebo VoIP ↔ ISDN). Jak L3 switch tak gateway jsou „nadstavby" – router pro rychlost, gateway pro nesourodost protokolů.

---

## 30) Ethernet – základní parametry

### Co je Ethernet
**Ethernet** = nejrozšířenější standard LAN. Definuje **fyzickou a linkovou vrstvu**.
- Vyvinul **Xerox PARC** (Bob Metcalfe) v 70. letech.
- Standardizován jako **IEEE 802.3** (1983).
- Dnes prakticky synonymum pro drátový LAN.

### Klíčové parametry
| Parametr | Hodnota |
|---|---|
| **Standard** | **IEEE 802.3** |
| **Přístupová metoda** | **CSMA/CD** (do 1 Gb/s; pak full-duplex) |
| **Logická topologie** | **sběrnice** (BUS) |
| **Fyzická topologie dnes** | **hvězda, strom** |
| **Adresování** | **MAC adresy 48 bitů** |
| **Médium** | TP (BaseT), FO (BaseS/L/F/E), historicky koax |
| **Rychlosti** | 10 Mb/s, 100 Mb/s, 1 / 2,5 / 5 / 10 / 25 / 40 / 100 / 400 Gb/s |

### MAC adresa
- **Délka: 6 byte = 48 bit**.
- Zápis: hex po bytech, oddělené dvojtečkami nebo pomlčkami: `00:1A:2B:3C:4D:5E`.
- **Prvních 3 byte** = **OUI** (Organizationally Unique Identifier) – výrobce NIC.
- **Posledních 3 byte** = sériové číslo NIC od daného výrobce.
- **Globálně unikátní** (přiřazuje IEEE).
- **Broadcast MAC**: `FF-FF-FF-FF-FF-FF`.
- **Multicast MAC**: `01-00-5E-XX-XX-XX` (pro IPv4 multicast).
- **U/L bit** (Universal/Local) – druhý nejméně významný bit prvního bajtu.
- **I/G bit** (Individual/Group) – nejméně významný bit prvního bajtu (0 = unicast, 1 = multi/broadcast).

### Označení Ethernetu (např. 100BASE-TX)
```
   100 BASE - TX
    │   │     │
    │   │     └── Médium: T = Twisted pair, F = Fiber, S = Short FO,
    │   │                 L = Long FO, E = Extended FO, B = Bidirectional
    │   └── Pásmo: BASE = baseband, BROAD = broadband
    └── Rychlost v Mb/s
```

| Označení | Médium | Rychlost |
|---|---|---|
| **BaseT** | kroucená dvojlinka (TP) | – |
| **BaseS** | short-range FO | – |
| **BaseL** | long-range FO | – |
| **BaseF, BaseE** | FO | – |
| **BaseBX** | bidirectional FO (1 vlákno) | – |

### Rychlé krátké odpovědi (časté otázky v taháku)
| Otázka | Odpověď |
|---|---|
| **Jak je označen Ethernet s kroucenou dvojlinkou?** | **BaseT** (např. 10BASE-T, 100BASE-TX, 1000BASE-T) |
| **Jak je označen Ethernet s optickými vlákny?** | **BaseF, BaseS, BaseL, BaseE, BaseBX** (např. 100BASE-FX, 1000BASE-SX, 10GBASE-LR) |
| **Co znamená písmeno T v 10BASE-T?** | Twisted pair (kroucená dvojlinka) |
| **Co znamená písmeno F v 10BASE-F?** | Fiber (optické vlákno) |
| **Co znamená písmeno S v 1000BASE-SX?** | Short wavelength (krátkovlnný FO, typ. 850 nm multi-mode) |
| **Co znamená písmeno L v 1000BASE-LX?** | Long wavelength (dlouhovlnný FO, typ. 1310 nm single-mode) |
| **Co znamená BASE?** | Baseband (základní pásmo, bez modulace na nosnou) |

### Vývoj Ethernetu
**Posloupnost**: Ethernet (DIX) → IEEE 802.3 → Ethernet II → upravený IEEE 802.3 (s 802.2 LLC).
- **Ethernet II** a **IEEE 802.3** se liší **formátem rámce** (Type vs Length).
- **Dnes preferovaný formát**: kombinovaný **IEEE 802.3 + 802.2 LLC** nebo Ethernet II.

### Média, která Ethernet NEpoužívá
**Rádiové vlny** (to je Wi-Fi). Ethernet je drátový (nebo přes FO).

### Rychlost, kterou Ethernet NEpoužívá
**1 Mb/s** – nikdy nebyla v Ethernetu standardizována.

### Vzorová odpověď
Ethernet je nejrozšířenější LAN standard, definovaný IEEE 802.3. Vyvinul ho Xerox v 70. letech. Používá přístupovou metodu CSMA/CD do 1 Gb/s (nad to plný duplex), logickou topologii sběrnici (i když fyzicky je dnes hvězda nebo strom). MAC adresa má 48 bitů – první 3 byte identifikují výrobce (OUI). Broadcast je FF:FF:FF:FF:FF:FF. Standardní označení např. 100BASE-TX: 100 Mb/s, baseband, kroucená dvojlinka. Ethernet má dva rámce: Ethernet II (s Type) a IEEE 802.3 (s Length + 802.2 LLC).

---

## 31) Ethernet – zasílání unicast, multicast, broadcast a vývoj

### Tři typy doručování rámců
Podle cílové MAC adresy se zpráva doručí jinak:

#### 1) Unicast – jednomu konkrétnímu příjemci
- Cílová MAC = MAC konkrétní stanice.
- Switch ji **doručí jen na port, kde cílová stanice je** (díky MAC tabulce).
- Pokud switch MAC nezná → **flooduje** (pošle na všechny porty kromě příchozího).
- **Standardní doručování** většiny rámců.

#### 2) Multicast – skupině přihlášených příjemců
- Cílová MAC: **01-00-5E-XX-XX-XX** (IPv4 multicast mapped) nebo **33-33-XX-XX-XX-XX** (IPv6 multicast mapped).
- Switch ji default **flooduje na všechny porty** (ne plnohodnotné multicast routing).
- **IGMP snooping** umožňuje switchi sledovat IGMP zprávy a posílat multicast jen na porty, kde jsou členové skupiny.

#### 3) Broadcast – všem ve stejné broadcastové doméně
- Cílová MAC: **FF-FF-FF-FF-FF-FF**.
- Switch **flooduje na všechny porty** kromě příchozího.
- **Nepřejde přes router**.
- Použití: ARP, DHCP discover, IPv4 omezený broadcast.

### Vývoj Ethernetu (historicky)
| Generace | Rychlost | Médium | Rok | Standard |
|---|---|---|---|---|
| Experimental Ethernet | 2,94 Mb/s | koax | 1973 | – (Xerox) |
| **Ethernet I (DIX)** | **10 Mb/s** | koax | 1980 | DIX |
| **IEEE 802.3** | **10 Mb/s** | koax | 1983 | IEEE 802.3 |
| **10BASE-T** | 10 Mb/s | TP | 1990 | IEEE 802.3i |
| **Fast Ethernet (100BASE-TX)** | **100 Mb/s** | TP / FO | 1995 | IEEE 802.3u |
| **Gigabit Ethernet (1000BASE-T)** | **1 Gb/s** | TP / FO | 1999 | IEEE 802.3ab |
| **10 Gigabit Ethernet** | **10 Gb/s** | TP / FO | 2002+ | IEEE 802.3ae |
| **2,5/5 GBASE-T** | 2,5 / 5 Gb/s | TP (Cat 5e/6) | 2016 | IEEE 802.3bz |
| **25/40/100/400 GbE** | 25–400 Gb/s | FO | 2010+ | různé |

### Vlastnosti vývoje
- **Rychlost narostla 10 000×** (z 10 Mb/s na 100 Gb/s a víc).
- **Médium se mění**: koax → TP → FO.
- **Topologie**: sběrnice → hvězda/strom.
- **Duplex**: poloduplex (CSMA/CD) → plný duplex (switch).

### Kódování podle rychlosti
| Rychlost | Kódování |
|---|---|
| 10 Mb/s | **Manchester (fázové NRZ)** |
| 100 Mb/s | **4B/5B + MLT-3** nebo NRZI |
| 1 Gb/s | **PAM5** (Cat 5e+) nebo **8B/10B** (FO) |
| 10 Gb/s | různé (např. 64B/66B) |

### Doba odvysílání 1 bitu
| Rychlost | Čas 1 bitu |
|---|---|
| 10 Mb/s | **100 ns** |
| 100 Mb/s | **10 ns** |
| 1 Gb/s | **1 ns** |
| 10 Gb/s | **0,1 ns** |

### Vzorová odpověď
Ethernet zasílá tři typy rámců. Unicast míří jednomu příjemci, switch ho podle MAC tabulky doručí jen na správný port (neznámou MAC flooduje). Multicast má adresu 01-00-5E-..., switch ho běžně flooduje, ale s IGMP snoopingem ho posílá jen členům skupiny. Broadcast (FF-FF-FF-FF-FF-FF) jde všem v broadcastové doméně – switch ho flooduje, router nepropustí. Vývoj Ethernetu šel z 10 Mb/s na koaxu (1980, DIX) přes Fast Ethernet 100 Mb/s (1995), Gigabit Ethernet (1999) až dnes po 400 GbE. Změna média koax → TP → FO, topologie sběrnice → hvězda, poloduplex → plný duplex se switchem.

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

## 34) Ethernet – 10 Mb/s až 10 Gb/s na TP, duplex, počet párů, max vzdálenost, přímý/křížený kabel

### Tabulka standardů Ethernetu na kroucené dvojlince
| Norma | Rychlost | Pásmo | Páry vodičů | Duplex | Max segment | Min. Cat |
|---|---|---|---|---|---|---|
| **10BASE-T** | 10 Mb/s | baseband | **2 páry** (1,2 + 3,6) | poloduplex / plný | **100 m** | Cat 3 |
| **100BASE-TX** | 100 Mb/s | baseband | **2 páry** (1,2 + 3,6) | poloduplex / plný | **100 m** | Cat 5 |
| **1000BASE-T (1GBASE-T)** | 1 Gb/s | baseband | **4 páry** (všechny 4) | **plný duplex** | **100 m** | Cat 5E |
| **2,5GBASE-T** | 2,5 Gb/s | baseband | 4 páry | plný duplex | 100 m | Cat 5E |
| **5GBASE-T** | 5 Gb/s | baseband | 4 páry | plný duplex | 100 m | Cat 6 |
| **10GBASE-T** | 10 Gb/s | baseband | **4 páry** | **plný duplex** | **100 m** (Cat 6A), 55 m (Cat 6) | Cat 6A |

### Duplex
- **10 Mb/s a 100 Mb/s**: poloduplex i plný duplex (s autonegotiation).
- **1 Gb/s a vyšší**: **vždy plný duplex** (CSMA/CD ztrácí smysl).

### Páry kabelu pro signál
| Norma | Páry pro signál | Páry pro řízení/rezervu |
|---|---|---|
| 10BASE-T | 2 (TX + RX) | 2 nepoužité |
| 100BASE-TX | 2 (TX + RX) | 2 nepoužité |
| 1000BASE-T | **4 (vše duplex)** | – |
| 10GBASE-T | **4 (vše duplex)** | – |

### Přímý a křížený kabel
**Přímý kabel (straight-through)** – vodiče zapojeny **1:1** na obou koncích (T568A↔T568A nebo T568B↔T568B).

**Křížený kabel (crossover)** – TX se kříží s RX na druhém konci.

#### Kdy použít přímý vs křížený (bez autodetekce/Auto-MDIX)
**Stejná skupina zařízení = křížený, různá = přímý.**

#### Skupiny zařízení
| Skupina | Zařízení |
|---|---|
| **A (DTE)** | PC, server, **router** (z hlediska kabeláže patří router do PC skupiny – „end stations") |
| **B (DCE)** | **hub**, **switch** |

> Pozor: **router je formálně DTE** (jako PC) – kříží se s PC.

#### Pravidla zapojení
| Spojení | Kabel |
|---|---|
| PC ↔ switch | **přímý** (A↔B) |
| PC ↔ hub | **přímý** (A↔B) |
| switch ↔ router | **přímý** (B↔A) |
| hub ↔ router | **přímý** (B↔A) |
| **switch ↔ switch** | **křížený** (B↔B) |
| **hub ↔ hub** | **křížený** (B↔B) |
| **switch ↔ hub** | **křížený** (B↔B) |
| **PC ↔ PC** | **křížený** (A↔A) |
| **PC ↔ router** | **křížený** (A↔A) |
| **router ↔ router** | **křížený** (A↔A) |

### Křížení vodičů (T568A vs T568B)
Standardní zapojení barev v RJ-45 podle T568B (běžnější):
| Pin | T568B | T568A |
|---|---|---|
| 1 | Oranžovo-bílá | Zeleno-bílá |
| 2 | Oranžová | Zelená |
| 3 | Zeleno-bílá | Oranžovo-bílá |
| 4 | Modrá | Modrá |
| 5 | Modro-bílá | Modro-bílá |
| 6 | Zelená | Oranžová |
| 7 | Hnědo-bílá | Hnědo-bílá |
| 8 | Hnědá | Hnědá |

**Křížený kabel** = jeden konec T568B, druhý konec T568A.

### Auto-MDIX
Moderní switche/karty mají **Auto-MDIX** – samy detekují, zda je kabel přímý nebo křížený, a přepnou se. **Dnes nemusí řešit, ale ke zkoušce ANO!**

### Vzorová odpověď
Ethernet na kroucené dvojlince používá vždy max 100 m segment. 10BASE-T a 100BASE-TX používají 2 páry a podporují polo i plný duplex, Cat 3 resp. Cat 5 a vyšší. Od 1 Gb/s (1000BASE-T) se používají všechny 4 páry a vždy plný duplex (CSMA/CD ztrácí smysl); 1 Gb/s vyžaduje Cat 5E, 10 Gb/s pak Cat 6A. Kabel je buď přímý (1:1) nebo křížený (TX↔RX přehozené). Pravidlo: stejná skupina zařízení (PC↔PC, switch↔switch) potřebuje křížený, různé skupiny (PC↔switch, switch↔router) potřebují přímý. Router patří kabeláží do PC skupiny (DTE). Moderní zařízení mají Auto-MDIX a poznají kabel samy.

---

## 35) Internet – historie a adresace (DNS)

### Historie Internetu
| Rok      | Událost                                                                  |
| -------- | ------------------------------------------------------------------------ |
| **1969** | **ARPANET** spuštěn (4 uzly: UCLA, Stanford, UC Santa Barbara, Utah)     |
| 1971     | první e-mail (Ray Tomlinson, použití `@`)                                |
| **1977** | start vývoje **TCP/IP**                                                  |
| 1980     | testovací nasazení TCP/IP                                                |
| **1983** | **TCP/IP nahradil NCP** v ARPANETu (1. ledna) – „flag day"               |
| **1984** | **DNS** zavedeno                                                         |
| 1986     | **NSFNET** (National Science Foundation) – první vědecká páteř           |
| **1989** | **WWW** – Tim Berners-Lee v CERN navrhl WorldWideWeb                     |
| 1990     | ARPANET ukončen, NSFNET pokračuje                                        |
| 1991     | WWW veřejně dostupné; **ČSFR pokus o připojení**                         |
| **1992** | **ČSFR připojeno k Internetu** (komerční provoz) – 13. 2. 1992 přes ČVUT |
| 1993     | Mosaic – první grafický prohlížeč; doména **.cs**                        |
| **1995** | doména **.cz** nahrazuje .cs (po rozpadu ČSFR)                           |
| 1995+    | komercializace Internetu, ISP, .com boom                                 |

### DNS – Domain Name System
**DNS** = hierarchický distribuovaný systém pro **překlad doménových jmen ↔ IP adres**.

#### Proč potřebujeme DNS
Lidé si zapamatují `google.com`, ne `142.250.190.46`. DNS překládá lidsky-přátelská jména na IP adresy.

#### Komponenty DNS
DNS systém má **3 části**:
1. **DNS resolvery** – komponenty na klientech, které posílají dotazy DNS serverům.
2. **DNS servery** – odpovídají na dotazy resolverů.
3. **DNS cache paměti** – ukládají odpovědi pro rychlejší následné dotazy.

#### Hierarchie domén
```
                    .   (kořenová doména – tečka)
                    │
        ┌───────────┼───────────┐
       cz         com         org      ← TLD (Top Level Domain)
        │           │
      utb         google      ← SLD (Second Level Domain)
        │           │
       fai        mail        ← další úrovně
```

- **Kořenová doména** = **tečka (.)** na konci úplného jména (FQDN).
  - `www.utb.cz.` (s tečkou) je FQDN.
- **TLD (Top Level Domain)** = `.cz, .com, .org, .gov, .edu, …`
  - **Doména `.cz` je TLD**.
- **SLD (Second Level Domain)** = `utb.cz, google.com`.
- **Subdomény** = `mail.google.com, www.fai.utb.cz`.
- **Oddělovač úrovní** = **tečka**.

#### Druhy DNS dotazů
- **Rekurzivní** – klient: „dej mi finální odpověď". Server doptá ostatní serverů.
- **Iterativní** – server: „neznám, ale zkus se zeptat tady".

#### Postup překladu `www.utb.cz`
```
Klient → DNS resolver: "kde je www.utb.cz?"
Resolver → cache: "máš v paměti?"  → NE
Resolver → root DNS: "kde je www.utb.cz?"
Root → "neznám, .cz spravuje tenhle server"
Resolver → .cz DNS: "kde je www.utb.cz?"
.cz DNS → "neznám, utb.cz spravuje tenhle server"
Resolver → utb.cz DNS: "kde je www.utb.cz?"
utb.cz DNS → "IP je 195.178.92.140"
Resolver → klient: 195.178.92.140
```

#### DNS server vs resolver vs cache
- **DNS server** **obsahuje** jak server, tak resolver (může se ptát dalších serverů → rekurze).
- **Pracovní stanice** **obsahuje** jen **DNS resolver**.
- **Cache** drží nedávno přeložené odpovědi (TTL záznamu určuje, jak dlouho jsou platné).

#### Klíčové fakty
- **DNS protokol v OSI**: **5. vrstva (relační)**.
- **DNS protokol v TCP/IP modelu**: aplikační.
- **Port DNS**: **53** (UDP pro dotazy, TCP pro zone transfer).
- **Každá doména v Internetu má alespoň 1 DNS server** (typicky 2 z bezpečnostních důvodů – primární + sekundární).
- **DNS slouží k překladu**: doménové jméno → IP **A NAOPAK** (reverzní DNS, PTR záznam).

#### Typy DNS záznamů
| Záznam    | Význam                        |
| --------- | ----------------------------- |
| **A**     | název → IPv4 adresa           |
| **AAAA**  | název → IPv6 adresa           |
| **CNAME** | alias (kanonické jméno)       |
| **MX**    | mailový server domény         |
| **NS**    | DNS server domény             |
| **PTR**   | reverzní (IP → název)         |
| **TXT**   | textový záznam (SPF, DKIM, …) |
| **SOA**   | autoritativní info o doméně   |

### Internet vs internet vs intranet vs extranet
| Pojem | Význam |
|---|---|
| **Internet** (velké I) | celosvětová síť postavená na TCP/IP |
| **internet** (malé i) | libovolné propojení sítí |
| **Intranet** | služby uvnitř organizace |
| **Extranet** | služby pro externí partnery |

### Adresace v Internetu
- **IPv4** – 32 bit, 4 byte, klasická adresace (viz okruh 19-22).
- **IPv6** – 128 bit, 16 byte, moderní adresace (viz okruh 23-26).
- **DNS** – lidsky-čitelné jméno místo IP.
- **NAT** – privátní IP za jednou veřejnou.

### Vzorová odpověď
Internet vznikl jako ARPANET v roce 1969 (DARPA), TCP/IP se začal vyvíjet 1977 a v roce 1983 nahradil NCP. DNS přibyl v 1984, WWW vymyslel Tim Berners-Lee v CERN v roce 1989. ČSFR byla připojena 13. 2. 1992 přes ČVUT, doména .cs byla 1995 nahrazena .cz po rozpadu federace. Internet adresuje na třech úrovních: MAC (L2), IP (L3 – IPv4 32 bit, IPv6 128 bit), a DNS (lidská jména). DNS je hierarchický systém složený z resolverů, serverů a cache; pracuje na 5. vrstvě OSI a portu 53. Hierarchie: kořen (tečka) → TLD (.cz, .com) → SLD (utb.cz) → subdomény. Každá doména má alespoň 1 DNS server (typicky 2). DNS překládá název na IP (záznam A pro IPv4, AAAA pro IPv6) i obráceně (PTR).

---

## Reference

- Hlavní zdroj: `Počítačové sítě 14.05.26.pdf` (Matýsek, UTB Zlín)
- Rozšiřující: `Počítačové sítě rozšiřující prezentace 26.03.19.pdf`
- Existující taháky:
  - [[TAHAK_CISTY]] – kompletní vyčištěný tahák s vysvětleními
  - [[TAHAK_BLESK]] – krátký memorizační tahák
  - [[CHYTAKY_DEKODER]] – dekodér chytáků (17 typů pastí)

## Otevřené body k osobnímu ověření

1. **Otázka 17 – TCP potvrzování**: detaily TCP handshake jsou z mé znalosti, ne přímo z prezentace. Ověř, zda přednáška chce na otázku konkrétně 3-way handshake nebo se spokojí s obecnou „pozitivní s ACK + sliding window".

2. **Otázka 22 – broadcast**: přechody přes zařízení odpovídají standardu, ale konkrétní formulace „směrovaný broadcast" může být v prezentaci pojmenovaná jinak. Stojí za to projít slidy o IPv4 broadcast.

3. **Otázka 26 – tři varianty DHCPv6**: rozlišení SLAAC / Stateless DHCPv6 / Stateful DHCPv6 podle flagů M, O v RA je standardní, ověř že prezentace tohle dělí stejně (mohou být jen 2 varianty: SLAAC vs DHCPv6).

4. **Otázka 29 – Gateway na vrstvě 7**: některé prezentace uvádějí gateway jako obecný pojem (přes všechny vrstvy 4-7), Matýsek ji ale typicky řadí na L7. Ověř formulaci.

5. **Otázka 34 – skupiny zařízení**: pravidlo „stejná skupina = křížený" je standardní. Pozor na speciální zapojení (např. server-to-server). Router je v praxi řazen jak do DTE (PC) skupiny, tak může mít speciální chování – ověř, jak to prezentace popisuje.



antény, pěkné obrázky ale žádný popisek k nim ![[Pasted image 20260526003555.png]]