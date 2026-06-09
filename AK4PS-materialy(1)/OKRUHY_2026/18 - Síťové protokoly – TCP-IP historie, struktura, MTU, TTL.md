---
cislo: 18
nazev: Síťové protokoly – TCP/IP historie, struktura, MTU, TTL
predmet: AK4PS
tags:
  - okruh
  - ak4ps
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
