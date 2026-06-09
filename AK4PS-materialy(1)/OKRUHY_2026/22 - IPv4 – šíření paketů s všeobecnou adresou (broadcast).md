---
cislo: 22
nazev: IPv4 – šíření paketů s všeobecnou adresou (broadcast)
predmet: AK4PS
tags:
  - okruh
  - ak4ps
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
