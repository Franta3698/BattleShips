---
cislo: 24
nazev: IPv6 – přidělování Link-local a Globální unicast adresy hostu
predmet: AK4PS
tags:
  - okruh
  - ak4ps
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
