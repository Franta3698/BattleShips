---
cislo: 1
nazev: Základní terminologie
predmet: AK4PS
tags:
  - okruh
  - ak4ps
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
