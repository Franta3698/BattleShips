---
cislo: 14
nazev: Model OSI
predmet: AK4PS
tags:
  - okruh
  - ak4ps
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
