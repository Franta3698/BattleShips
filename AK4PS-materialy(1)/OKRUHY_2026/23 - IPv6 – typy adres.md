---
cislo: 23
nazev: IPv6 – typy adres
predmet: AK4PS
tags:
  - okruh
  - ak4ps
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
