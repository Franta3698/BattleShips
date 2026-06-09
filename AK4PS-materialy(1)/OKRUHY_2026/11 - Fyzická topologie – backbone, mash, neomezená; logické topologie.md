---
cislo: 11
nazev: Fyzická topologie – backbone, mash, neomezená; logické topologie
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 11) Fyzická topologie – backbone, mash, neomezená; logické topologie

### Backbone (páteř)
![[Pasted image 20260523194044.png]]
**Páteřní topologie** = vysokorychlostní linka spojující více menších sítí (LAN, MAN).
```
        ┌─[LAN1]──┐
        │         │
   ═══[BACKBONE]══════[BACKBONE]═══   (rychlá optická páteř)
        │                   │
        └─[LAN2]──┐    ┌──[LAN3]
                  │    │
                  [LAN4]
```
- Vysoká rychlost (obvykle optická).
- V ČR příklad: **CESNET2** (akademická páteřní síť).
- Spojuje LAN/CAN/MAN/WAN.

### Mash (mesh)
![[Pasted image 20260523194103.png]]
- Každý uzel propojen **s více ostatními** (částečný mesh) nebo **se všemi** (full mesh).
- **Vysoká redundance** → odolnost vůči výpadkům.
- Při výpadku spoje má paket alternativní cestu.
- Použití: WAN páteřní sítě, mesh Wi-Fi (pokrytí budov).

### Neomezená topologie (libovolná, irregular)
![[Pasted image 20260523194118.png]]
- **Nejčastěji pro WAN** – Internet, světová síť.
- Topologie není pravidelná, vzniká postupně připojováním dalších sítí.
- Není striktně řízena, propojení podle dohody mezi ISP.

### Logická topologie
**Definice**: dána způsobem, jakým spolu uzly **logicky komunikují** – nezávisí na tom, jak je síť fyzicky zapojena.

#### Tři logické topologie
1. **Logická sběrnice** – všechny uzly vysílají do jednoho společného „bus", ostatní poslouchají. **Ethernet má logickou topologii sběrnici**, i když fyzicky je hvězda.
2. **Logický kruh** – data putují od uzlu k uzlu v kruhu (token předávaný dál). Token Ring fyzicky byl hvězda kolem MAU, ale logicky kruh.
3. **Logický dvojbodový spoj (point-to-point)** – přímé spojení dvou uzlů (modem, dedikovaná linka).

### Vzorová odpověď
Backbone je páteřní topologie – vysokorychlostní linka spojující menší sítě, v ČR příklad CESNET2. Mesh propojuje uzly mezi sebou s vysokou redundancí, paket má alternativní cesty. Neomezená (libovolná) topologie je typická pro WAN a Internet – vzniká postupně, není pravidelná. Logická topologie je nezávislá na fyzické: Ethernet má fyzicky hvězdu, ale logicky sběrnici. Logické topologie jsou tři: sběrnice, kruh a dvojbodový spoj.

---
