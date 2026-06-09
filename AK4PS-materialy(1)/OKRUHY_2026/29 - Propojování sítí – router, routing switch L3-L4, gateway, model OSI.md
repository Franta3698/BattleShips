---
cislo: 29
nazev: Propojování sítí – router, routing switch L3/L4, gateway, model OSI
predmet: AK4PS
tags:
  - okruh
  - ak4ps
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
