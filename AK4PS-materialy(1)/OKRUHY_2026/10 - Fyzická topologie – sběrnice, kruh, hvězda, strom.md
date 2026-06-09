---
cislo: 10
nazev: Fyzická topologie – sběrnice, kruh, hvězda, strom
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 10) Fyzická topologie – sběrnice, kruh, hvězda, strom

### Definice
**Fyzická topologie** = způsob fyzického propojení uzlů kabely / médii. **Logická topologie** = způsob, jakým spolu uzly logicky komunikují (může se lišit od fyzické).

### Sběrnice (Bus)
![[Pasted image 20260523193809.png]]

- Všechny uzly visí na **společném kabelu**.
- **Musí být zakončena odpory** (terminátory) na obou koncích – jinak odraz signálu.
- **Přerušení kabelu = výpadek celé sítě**.
- Zpráva se šíří **ke všem stanicím**.
- Historicky: **10BASE2, 10BASE5** (koaxiál).
- Dnes prakticky **nepoužívaná** v Ethernetu, ale **logická topologie Ethernetu je stále sběrnice**.

### Kruh (Ring)
![[Pasted image 20260523193912.png]]

- Každý PC propojen s **následujícím a předchozím** (typicky jednosměrný tok).
- Každý uzel **regeneruje signál** (aktivní role).
- Pokud přijatá data nejsou určena tomuto PC, pošle dál.
- **Výpadek 1 PC = výpadek celé sítě** (lze obejít dvojitým kruhem – Token Ring, FDDI).
- Historicky: Token Ring, FDDI.

### Hvězda (Star)
![[Pasted image 20260523193956.png]]
- Všechny uzly k jednomu **centrálnímu prvku** (hub nebo switch).
- **Výpadek stanice neovlivní síť** (jen ona je odpojená).
- **Výpadek centrálního prvku = pád sítě**.
- Nejstarší typ topologie (terminály k mainframe).
- **Typický dnes**: Ethernet na TP se switchem.

### Strom (Tree)
![[Pasted image 20260523194016.png]]
- **Hierarchie hvězd** – kořen + uzly, ze kterých vychází další hvězdy.
- **Havárie kořene → celá síť padá**.
- **Výpadek větve → ostatní fungují**.
- Typické pro **strukturovanou kabeláž** v budově (páteřní switch → patrové switche).

### Vzorová odpověď
Fyzická topologie je dána fyzickým propojením kabelů. Sběrnice má společný kabel se zakončovacími odpory, libovolné přerušení shodí síť, šíří ke všem – dnes prakticky nepoužitá. Kruh propojuje uzly do okruhu, každý regeneruje signál a posílá dál – historicky Token Ring, FDDI. Hvězda má centrální prvek (hub/switch), výpadek stanice síti nevadí ale výpadek centra ano – dnes nejtypičtější. Strom je hierarchie hvězd, používá se ve strukturované kabeláži, padá kořen = padá síť.

---
