---
cislo: 2
nazev: Historie počítačových sítí
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 2) Historie počítačových sítí

### Klíčové letopočty
| Rok                 | Událost                                                                  |
| ------------------- | ------------------------------------------------------------------------ |
| **počátek 70. let** | vznik prvních počítačových sítí                                          |
| **1969**            | **ARPANET** – první uzel, projekt americké armády (DARPA)                |
| **1970**            | vývoj v DARPA pokračuje                                                  |
| **1977**            | zahájen vývoj **TCP/IP**                                                 |
| **1983**            | zavedení **TCP/IP do ARPANETu** (přechod z NCP)                          |
| **1984**            | zavedení **DNS** do ARPANETu                                             |
| **1986**            | financování **NSF** (NSFNET)                                             |
| **1989**            | vznik **WWW** stránek (Tim Berners-Lee, CERN)                            |
| **1990**            | pevná linka v ČSFR                                                       |
| **1991**            | pokus o připojení ČSFR k Internetu                                       |
| **1992**            | **ČSFR připojeno k Internetu (komerční provoz)** – 13. 2. 1992 přes ČVUT |
| **1993**            | registrována doména **.cs**                                              |
| **1995**            | doména **.cs** nahrazena doménou **.cz** (rozpad ČSFR)                   |

### Souvislosti
- ARPANET vznikl z obavy o odolnost komunikační infrastruktury během studené války.
- Předchůdce TCP/IP byl protokol **NCP**.
- Internet (s velkým I) = celosvětová síť postavená nad TCP/IP.
- internet (malé i) = libovolná soustava propojených sítí.

### Vývoj topologie sítí (slidy 25–30 prezentace)

#### 3.1 Počátky počítačových sítí 
- V počátku 70. let vznikaly **první izolované počítačové sítě** různých výrobců.
- Později vznikají sítě s **polygonální strukturou** → vznikají první **přepojovací uzly**.

#### 3.2 Síť bez přepojovacích uzlů 
![[Pasted image 20260523142218.png]]
- **U = uzel**: sálový počítač s OS Unix.
- Sálové počítače propojené **přímo navzájem** (polygonální propojení).
- Velmi nepraktické: počet spojů roste kvadraticky s počtem uzlů.

#### 3.3 Síť s přepojovacími uzly  
![[Pasted image 20260523142237.png]]
- **P = přepojovací uzel**: OS Unix + přepojovací SW (předchůdce dnešního routeru).
- Pakety putují **uzel → přepojovací uzel → cílový uzel**.

#### 3.4 Alternativní cesty 
![[Pasted image 20260523142247.png]]
- Mezi dvěma uzly **existuje víc cest** přes různé přepojovací uzly.
- Při výpadku jedné cesty paket jde jinou → základ odolnosti ARPANETu.

#### 3.5 Nadbytečná propojení (slide 29)
![[Pasted image 20260523142529.png]]
- Některá přímá U↔U propojení **zbytečně duplikují** trasy, které jsou už dostupné přes P.
- Lze je odstranit bez ztráty konektivity.

#### 3.6 Nezbytně nutná propojení (slide 30)
![[Pasted image 20260523142549.png]]
- Po odstranění nadbytečností zůstane **hvězdicová struktura kolem přepojovacích uzlů P**.
- Každý U je připojen jen k P, P jsou propojeny mezi sebou → základ dnešní hierarchické topologie LAN/WAN.

### Vzorová odpověď
Počítačové sítě vznikly na začátku 70. let. Klíčový mezník je ARPANET (1969), na něm se v 70. letech vyvíjel TCP/IP, který se prosadil v roce 1983. DNS přišel 1984, WWW v roce 1989. ČSFR byla připojena 1992, doména .cz nahradila .cs v roce 1995. Topologicky se vývoj posunul ze sítí bez přepojovacích uzlů (polygonální propojení U-U) přes sítě s přepojovacími uzly (P mezi U) k dnešní struktuře s alternativními cestami a odstraněním nadbytečných propojení – výsledkem jsou „nezbytně nutná propojení" tvořící hvězdy kolem přepojovacích uzlů.

---
