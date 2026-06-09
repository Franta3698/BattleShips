---
cislo: 27
nazev: TCP/IP port a socket. Dělení portů. Demultiplexování
predmet: AK4PS
tags:
  - okruh
  - ak4ps
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
