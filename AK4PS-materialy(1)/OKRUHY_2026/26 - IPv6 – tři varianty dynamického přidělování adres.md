---
cislo: 26
nazev: IPv6 – tři varianty dynamického přidělování adres
predmet: AK4PS
tags:
  - okruh
  - ak4ps
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
