---
cislo: 19
nazev: IPv4 – původní a současná koncepce
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 19) IPv4 – původní a současná koncepce

### Adresa
- **IPv4 adresa = 32 bitů = 4 byte**.
- Zápis: **dekadicky po bajtech**, oddělené tečkami: `192.168.1.42`.
- Každý oktet: **0–255**.

### Původní koncepce – třídy adres (1981, Classful)
| Třída | 1. byte | Bity sítě / hosta | Výchozí maska | Síť/host |
|---|---|---|---|---|
| **A** | 1–127 | 8 / 24 | 255.0.0.0 (/8) | 128 sítí / 16 777 214 hostů |
| **B** | 128–191 | 16 / 16 | 255.255.0.0 (/16) | 16 384 sítí / 65 534 hostů |
| **C** | 192–223 | 24 / 8 | 255.255.255.0 (/24) | ≈2 mil. sítí / 254 hostů |
| **D** | 224–239 | – (multicast) | – | skupinové adresování |
| **E** | 240–255 | – (rezerva) | – | experimentální, nepoužívá se |

#### Bity prvního bytu
- A: `0xxxxxxx` (0 na začátku)
- B: `10xxxxxx`
- C: `110xxxxx`
- D: `1110xxxx`
- E: `1111xxxx`

#### Využití tříd
- **A, B, C** = unicast (jednotlivé počítače).
- **D** = multicast (skupinové).
- **E** = rezerva, experimenty.

#### Problém původní koncepce
Velké třídy plýtvaly adresami: kdo dostal třídu A, měl 16 milionů adres, ale využil jich pár tisíc. **Adresy IPv4 by došly velmi rychle.**

### Současná koncepce – CIDR (Classless Inter-Domain Routing, 1993)
**CIDR = beztřídové směrování.** Místo pevných tříd se používá **prefix /n** – kolik bitů zleva tvoří síťovou část. Třídy A/B/C **stále existují**, ale jen jako orientační (např. defaultní masky), reálně se dělí libovolně.

#### Zápis CIDR
- `192.168.1.0/24` – 24 bitů sítě, 8 bitů hosta.
- `10.0.0.0/8` – třída A, ale CIDR umožňuje libovolně dělit.
- `200.10.10.0/26` – třída C rozdělená na subsítě po 64 adresách.

#### Výhody CIDR
- Efektivnější využití adresního prostoru.
- **Agregace tras** (supernetting) – jeden záznam v routing tabulce pokryje víc sítí.

### NAT (Network Address Translation)
Další způsob šetření – **privátní adresy** uvnitř LAN, jedna **veřejná** vůči Internetu.
- 1 veřejná IP → mnoho privátních počítačů.
- NAT překládá adresy a porty (PAT/Overload).

### IPv6
Dlouhodobé řešení nedostatku adres: **128 bitů** místo 32. Viz okruh 23.

### Vzorová odpověď
IPv4 adresa je 32 bitů zapsaná dekadicky po bajtech (4 oktety 0-255). Původní koncepce (1981) dělila adresy do tříd A, B, C podle prvního bajtu – třídy měly pevně danou síťovou masku 8/16/24 bitů. Třída D je multicast, E rezerva. Tahle koncepce plýtvala adresami, proto v 1993 přišlo CIDR – beztřídové dělení s prefixem /n. Místo tříd se masky dají libovolně. Druhou nouzovou cestou bylo NAT – privátní adresy schované za jednu veřejnou. Dlouhodobé řešení je ale IPv6 (128 bitů).

---
