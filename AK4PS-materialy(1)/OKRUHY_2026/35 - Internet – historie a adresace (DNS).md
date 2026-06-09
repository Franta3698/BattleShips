---
cislo: 35
nazev: Internet – historie a adresace (DNS)
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 35) Internet – historie a adresace (DNS)

### Historie Internetu
| Rok      | Událost                                                                  |
| -------- | ------------------------------------------------------------------------ |
| **1969** | **ARPANET** spuštěn (4 uzly: UCLA, Stanford, UC Santa Barbara, Utah)     |
| 1971     | první e-mail (Ray Tomlinson, použití `@`)                                |
| **1977** | start vývoje **TCP/IP**                                                  |
| 1980     | testovací nasazení TCP/IP                                                |
| **1983** | **TCP/IP nahradil NCP** v ARPANETu (1. ledna) – „flag day"               |
| **1984** | **DNS** zavedeno                                                         |
| 1986     | **NSFNET** (National Science Foundation) – první vědecká páteř           |
| **1989** | **WWW** – Tim Berners-Lee v CERN navrhl WorldWideWeb                     |
| 1990     | ARPANET ukončen, NSFNET pokračuje                                        |
| 1991     | WWW veřejně dostupné; **ČSFR pokus o připojení**                         |
| **1992** | **ČSFR připojeno k Internetu** (komerční provoz) – 13. 2. 1992 přes ČVUT |
| 1993     | Mosaic – první grafický prohlížeč; doména **.cs**                        |
| **1995** | doména **.cz** nahrazuje .cs (po rozpadu ČSFR)                           |
| 1995+    | komercializace Internetu, ISP, .com boom                                 |

### DNS – Domain Name System
**DNS** = hierarchický distribuovaný systém pro **překlad doménových jmen ↔ IP adres**.

#### Proč potřebujeme DNS
Lidé si zapamatují `google.com`, ne `142.250.190.46`. DNS překládá lidsky-přátelská jména na IP adresy.

#### Komponenty DNS
DNS systém má **3 části**:
1. **DNS resolvery** – komponenty na klientech, které posílají dotazy DNS serverům.
2. **DNS servery** – odpovídají na dotazy resolverů.
3. **DNS cache paměti** – ukládají odpovědi pro rychlejší následné dotazy.

#### Hierarchie domén
```
                    .   (kořenová doména – tečka)
                    │
        ┌───────────┼───────────┐
       cz         com         org      ← TLD (Top Level Domain)
        │           │
      utb         google      ← SLD (Second Level Domain)
        │           │
       fai        mail        ← další úrovně
```

- **Kořenová doména** = **tečka (.)** na konci úplného jména (FQDN).
  - `www.utb.cz.` (s tečkou) je FQDN.
- **TLD (Top Level Domain)** = `.cz, .com, .org, .gov, .edu, …`
  - **Doména `.cz` je TLD**.
- **SLD (Second Level Domain)** = `utb.cz, google.com`.
- **Subdomény** = `mail.google.com, www.fai.utb.cz`.
- **Oddělovač úrovní** = **tečka**.

#### Druhy DNS dotazů
- **Rekurzivní** – klient: „dej mi finální odpověď". Server doptá ostatní serverů.
- **Iterativní** – server: „neznám, ale zkus se zeptat tady".

#### Postup překladu `www.utb.cz`
```
Klient → DNS resolver: "kde je www.utb.cz?"
Resolver → cache: "máš v paměti?"  → NE
Resolver → root DNS: "kde je www.utb.cz?"
Root → "neznám, .cz spravuje tenhle server"
Resolver → .cz DNS: "kde je www.utb.cz?"
.cz DNS → "neznám, utb.cz spravuje tenhle server"
Resolver → utb.cz DNS: "kde je www.utb.cz?"
utb.cz DNS → "IP je 195.178.92.140"
Resolver → klient: 195.178.92.140
```

#### DNS server vs resolver vs cache
- **DNS server** **obsahuje** jak server, tak resolver (může se ptát dalších serverů → rekurze).
- **Pracovní stanice** **obsahuje** jen **DNS resolver**.
- **Cache** drží nedávno přeložené odpovědi (TTL záznamu určuje, jak dlouho jsou platné).

#### Klíčové fakty
- **DNS protokol v OSI**: **5. vrstva (relační)**.
- **DNS protokol v TCP/IP modelu**: aplikační.
- **Port DNS**: **53** (UDP pro dotazy, TCP pro zone transfer).
- **Každá doména v Internetu má alespoň 1 DNS server** (typicky 2 z bezpečnostních důvodů – primární + sekundární).
- **DNS slouží k překladu**: doménové jméno → IP **A NAOPAK** (reverzní DNS, PTR záznam).

#### Typy DNS záznamů
| Záznam    | Význam                        |
| --------- | ----------------------------- |
| **A**     | název → IPv4 adresa           |
| **AAAA**  | název → IPv6 adresa           |
| **CNAME** | alias (kanonické jméno)       |
| **MX**    | mailový server domény         |
| **NS**    | DNS server domény             |
| **PTR**   | reverzní (IP → název)         |
| **TXT**   | textový záznam (SPF, DKIM, …) |
| **SOA**   | autoritativní info o doméně   |

### Internet vs internet vs intranet vs extranet
| Pojem | Význam |
|---|---|
| **Internet** (velké I) | celosvětová síť postavená na TCP/IP |
| **internet** (malé i) | libovolné propojení sítí |
| **Intranet** | služby uvnitř organizace |
| **Extranet** | služby pro externí partnery |

### Adresace v Internetu
- **IPv4** – 32 bit, 4 byte, klasická adresace (viz okruh 19-22).
- **IPv6** – 128 bit, 16 byte, moderní adresace (viz okruh 23-26).
- **DNS** – lidsky-čitelné jméno místo IP.
- **NAT** – privátní IP za jednou veřejnou.

### Vzorová odpověď
Internet vznikl jako ARPANET v roce 1969 (DARPA), TCP/IP se začal vyvíjet 1977 a v roce 1983 nahradil NCP. DNS přibyl v 1984, WWW vymyslel Tim Berners-Lee v CERN v roce 1989. ČSFR byla připojena 13. 2. 1992 přes ČVUT, doména .cs byla 1995 nahrazena .cz po rozpadu federace. Internet adresuje na třech úrovních: MAC (L2), IP (L3 – IPv4 32 bit, IPv6 128 bit), a DNS (lidská jména). DNS je hierarchický systém složený z resolverů, serverů a cache; pracuje na 5. vrstvě OSI a portu 53. Hierarchie: kořen (tečka) → TLD (.cz, .com) → SLD (utb.cz) → subdomény. Každá doména má alespoň 1 DNS server (typicky 2). DNS překládá název na IP (záznam A pro IPv4, AAAA pro IPv6) i obráceně (PTR).

---

## Reference

- Hlavní zdroj: `Počítačové sítě 14.05.26.pdf` (Matýsek, UTB Zlín)
- Rozšiřující: `Počítačové sítě rozšiřující prezentace 26.03.19.pdf`
- Existující taháky:
  - [[TAHAK_CISTY]] – kompletní vyčištěný tahák s vysvětleními
  - [[TAHAK_BLESK]] – krátký memorizační tahák
  - [[CHYTAKY_DEKODER]] – dekodér chytáků (17 typů pastí)

## Otevřené body k osobnímu ověření

1. **Otázka 17 – TCP potvrzování**: detaily TCP handshake jsou z mé znalosti, ne přímo z prezentace. Ověř, zda přednáška chce na otázku konkrétně 3-way handshake nebo se spokojí s obecnou „pozitivní s ACK + sliding window".

2. **Otázka 22 – broadcast**: přechody přes zařízení odpovídají standardu, ale konkrétní formulace „směrovaný broadcast" může být v prezentaci pojmenovaná jinak. Stojí za to projít slidy o IPv4 broadcast.

3. **Otázka 26 – tři varianty DHCPv6**: rozlišení SLAAC / Stateless DHCPv6 / Stateful DHCPv6 podle flagů M, O v RA je standardní, ověř že prezentace tohle dělí stejně (mohou být jen 2 varianty: SLAAC vs DHCPv6).

4. **Otázka 29 – Gateway na vrstvě 7**: některé prezentace uvádějí gateway jako obecný pojem (přes všechny vrstvy 4-7), Matýsek ji ale typicky řadí na L7. Ověř formulaci.

5. **Otázka 34 – skupiny zařízení**: pravidlo „stejná skupina = křížený" je standardní. Pozor na speciální zapojení (např. server-to-server). Router je v praxi řazen jak do DTE (PC) skupiny, tak může mít speciální chování – ověř, jak to prezentace popisuje.
