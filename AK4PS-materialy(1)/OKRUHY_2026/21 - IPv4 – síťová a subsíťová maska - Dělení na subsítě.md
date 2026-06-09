---
cislo: 21
nazev: IPv4 – síťová a subsíťová maska. Dělení na subsítě
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 21) IPv4 – síťová a subsíťová maska. Dělení na subsítě

### Síťová maska (Subnet Mask)
**Maska** říká, **kolik bitů z IP adresy tvoří síť** a kolik tvoří hosta.
- Binárně: jedničky zleva (síť), pak nuly (host).
- Dekadicky: 4 byty po tečkách jako IP adresa.
- **Prefix /n** = počet jedniček v masce zleva.

| Prefix | Maska dekadicky |
|---|---|
| /8 | 255.0.0.0 |
| /16 | 255.255.0.0 |
| /24 | 255.255.255.0 |
| /25 | 255.255.255.128 |
| /26 | 255.255.255.192 |
| /27 | 255.255.255.224 |
| /28 | 255.255.255.240 |
| /29 | 255.255.255.248 |
| /30 | 255.255.255.252 |

#### Hodnoty bajtu masky
| Poslední byte | Binárně | Půjčených bitů |
|---|---|---|
| 128 | 10000000 | 1 |
| 192 | 11000000 | 2 |
| 224 | 11100000 | 3 |
| 240 | 11110000 | 4 |
| 248 | 11111000 | 5 |
| 252 | 11111100 | 6 |
| 254 | 11111110 | 7 |
| 255 | 11111111 | 8 |

### Výpočet adresy sítě
**Adresa sítě** = IP **AND** maska (po bitech).

#### Příklad
```
IP:      192.168.10.130    11000000.10101000.00001010.10000010
Maska:   255.255.255.192   11111111.11111111.11111111.11000000
AND ─────────────────────────────────────────────────────────────
Síť:     192.168.10.128    11000000.10101000.00001010.10000000
```

### Dělení sítí na subsítě (subnetting)
**Subnetting** = ze sítě vytvořím **více menších podsítí** tím, že **„půjčím" bity z hostitelské části** do síťové.

#### Vzorec
- **Počet subsítí = 2ⁿ**, kde n = počet půjčených bitů.
- **Počet hostů na subsíť = 2^(bitů hosta) − 2** (odečítáme adresu sítě a broadcast).

#### Příklad: dělení třídy C (192.168.10.0/24) na subsítě po /26
- Půjčíme 2 bity → 4 subsítě.
- Každá má 32 − 26 = 6 bitů hosta → 2⁶ − 2 = **62 použitelných hostů**.

| # | Síť | První host | Poslední host | Broadcast |
|---|---|---|---|---|
| 1 | 192.168.10.0/26 | .1 | .62 | .63 |
| 2 | 192.168.10.64/26 | .65 | .126 | .127 |
| 3 | 192.168.10.128/26 | .129 | .190 | .191 |
| 4 | 192.168.10.192/26 | .193 | .254 | .255 |

#### Tabulka výsledných hostů
| Prefix | Bitů hosta | 2ⁿ | Použitelné (−2) |
|---|---|---|---|
| /23 | 9 | 512 | **510** |
| /24 | 8 | 256 | **254** |
| /25 | 7 | 128 | **126** |
| /26 | 6 | 64 | **62** |
| /27 | 5 | 32 | **30** |
| /28 | 4 | 16 | **14** |
| /29 | 3 | 8 | **6** |
| /30 | 2 | 4 | **2** |

### Typické otázky
- **Délka prefixu pro dělení třídy B na čtvrtiny**: **/18** (B má /16, 2 půjčené bity = 4 subsítě).
- **Hodnota 2. bajtu při půlení třídy A**: **128** (A má /8, 1 půjčený bit = bit 128 v 2. bajtu).
- **Maska SSM IPv4 má kolik byte**: **4**.
- **První adresa v síti/subsíti**: adresa sítě / subsítě (nepoužitelná pro hosta).
- **Maximum subsítí třídy C, aby zbyly volné adresy pro PC**: **64** (/30 → 2 hosti).

### Vzorová odpověď
Subsíťová maska je 32-bitové číslo s jedničkami zleva (síťová část) a nulami (hostitelská část). Prefix /n udává počet jedniček. Adresu sítě získám logickým AND mezi IP a maskou. Subnetting znamená rozdělení sítě na menší podsítě půjčením bitů z hostitelské části – počet subsítí = 2ⁿ (kde n = počet půjčených bitů), použitelných hostů = 2^bitů_hosta − 2 (mínus síť a broadcast). Třídu C dokážu rozdělit prefixem /26 na 4 subsítě po 62 hostech, prefixem /30 na 64 subsítí po 2 hostech.

---
