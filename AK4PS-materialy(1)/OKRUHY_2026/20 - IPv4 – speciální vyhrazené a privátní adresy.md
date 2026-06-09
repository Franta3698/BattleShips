---
cislo: 20
nazev: IPv4 – speciální vyhrazené a privátní adresy
predmet: AK4PS
tags:
  - okruh
  - ak4ps
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
