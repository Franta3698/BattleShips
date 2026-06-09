---
cislo: 25
nazev: IPv6 – EUI-64, generátor náhodných čísel, DAD
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 25) IPv6 – EUI-64, generátor náhodných čísel, DAD

### Algoritmus EUI-64
**Cíl**: vytvořit 64-bit **Interface Identifier** z 48-bit **MAC adresy**.

#### Postup
1. **Vezmu MAC**: `AABBCC-DDEEFF` (3+3 byte, ale obvykle se píše s pomlčkami/dvojtečkami).
2. **Rozdělím** na **OUI** (3 byte = vendor) a **NIC** (3 byte = id karty).
3. **Vložím `FFFE` mezi OUI a NIC**: `AABBCC` + **FFFE** + `DDEEFF` → 8 byte = 64 bit.
4. **Invertuju 7. bit prvního bajtu** (U/L bit = Universal/Local).
   - Pokud byl 0 (Universal, globálně unikátní), bude 1 (Local).
   - Funguje jako přepínač interpretace adresy.

#### Příklad
```
MAC:       0050:56C0:0008
Rozdělím:  0050:56  C0:0008
Vložím FFFE: 0050:56FF:FEC0:0008
Invertuj 7. bit prvního bajtu:
  0x00 = 00000000  →  invert bit 7 (z LSB) = 00000010 = 0x02
Výsledný IID: 0250:56FF:FEC0:0008
LLA:        FE80::250:56FF:FEC0:0008
```

#### Proč invertovat U/L bit?
V MAC formátu: 0 = globálně unikátní adresa, 1 = lokálně administrovaná.
V EUI-64: význam je obrácený, takže invertujeme.

### Generátor náhodných čísel (Privacy Extensions, RFC 4941/8981)
**Problém EUI-64**: Interface ID je odvozený z MAC → unikátní identifikátor zařízení putuje s ním po Internetu. **Hrozba sledování.**

**Řešení**: Interface ID se generuje **náhodně** (kryptografická hashová funkce + náhodné semínko), pravidelně se mění (typ. 1× denně), staré adresy se zachovají do vypršení.

#### Vlastnosti
- Náhodný 64-bit IID.
- Lze používat současně s EUI-64 adresou.
- **Výchozí ve Windows, macOS, novějších Linuxech.**
- U/L bit se nastavuje na 0 (lokální).

### DAD – Duplicate Address Detection
**Účel**: před použitím nově sestavené adresy si **ověřit, že ji nemá nikdo jiný** v segmentu.

#### Algoritmus DAD
1. Host **dočasně** přidělí adresu rozhraní s příznakem **tentative**.
2. Pošle **Neighbor Solicitation (NS)** na **solicited-node multicast** adresy `FF02::1:FFXX:XXXX` (kde XXXX je posledních 24 bitů adresy).
3. Cílová adresa NS = ověřovaná adresa. Zdrojová adresa = `::` (neznámá).
4. **Čeká** určitý čas (RetransTimer, výchozí 1 s).
5. **Pokud odpověď NS od jiného hosta** = adresa je obsazená → host adresu **NEPOUŽIJE** (oznámí konflikt).
6. **Pokud neodpoví nikdo** = adresa je volná → host ji nastaví jako **preferred** a začne používat.

#### Vizualizace
```
Host A chce použít FE80::A8BB:CCFF:FEDD:EEFF
   │
   ├──→ NS (target: FE80::A8BB:CCFF:FEDD:EEFF) na FF02::1:FFDD:EEFF
   │    src: ::, dst: solicited-node multicast
   │
   ├──→ čeká
   │
   ▼
 Žádná odpověď → adresa volná → použiju
 Odpověď NA → adresa zabraná → konflikt!
```

#### Co se kontroluje
- **Každou** unicast adresu (LLA, GUA, ULA).
- Probíhá vždy při **prvním přidělení**.
- IPv6 standard to **vyžaduje** (RFC 4862).

### Vzorová odpověď
EUI-64 je algoritmus pro odvození 64-bitového Interface ID z 48-bit MAC: rozdělím MAC na dvě poloviny, vložím doprostřed FFFE a invertuju 7. bit prvního bajtu (U/L bit). Výsledek se připojí k prefixu (FE80::/64 pro LLA, nebo prefix z RA pro GUA). Místo EUI-64 se dnes preferuje náhodný generátor (Privacy Extensions, RFC 4941/8981) – odstraňuje sledovatelnost přes MAC, IID se pravidelně mění. Před použitím každé adresy host provede DAD (Duplicate Address Detection): pošle Neighbor Solicitation na solicited-node multicast s ověřovanou adresou jako cílem. Pokud někdo odpoví, adresa je obsazená a host ji nepoužije; pokud nikdo, adresa je volná.

---
