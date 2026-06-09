---
cislo: 8
nazev: Komunikace vzduchem – bezpečnost, architektura, mikrovlnné spoje, antény, Fresnelova zóna, skrytý uzel
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 8) Komunikace vzduchem – bezpečnost, architektura, mikrovlnné spoje, antény, Fresnelova zóna, skrytý uzel

### Bezpečnost Wi-Fi
Šifrování vzestupně podle síly:
**WEP < WPA < WPA2 < WPA3**
- **WEP** – dnes prolomený, **nedostatečný**, používá se jen u ad-hoc historicky.
- **WPA** – přechodný standard.
- **WPA2** – dlouhá léta standard, AES.
- **WPA3** – **aktuálně nejúčinnější**, odolnost proti slovníkovým útokům.

### Architektura WLAN
Dva základní režimy:

#### 1) Ad-hoc (IBSS – Independent BSS)
Bez přístupového bodu; klienti komunikují přímo.
```
[ PC1 ]──────[ PC2 ]
   \          /
    \        /
     [ PC3 ]
```

#### 2) Infrastructure (BSS / ESS)
S přístupovým bodem (AP – Access Point).
```
        [ AP ]
       /  │   \
   [PC1] [PC2] [PC3]
```
- **BSS** (Basic Service Set) = 1 AP + klienti.
- **ESS** (Extended Service Set) = více AP propojených páteří (roaming).
- **SSID** – identifikátor sítě.

### Mikrovlnné spoje
- **Bod-bod přenos** mezi 2 anténami na přímou viditelnost (LOS – Line of Sight).
- Používá licencovaná pásma 3,5–80 GHz pro páteřové spoje (operátoři, ISP).
- Velmi citlivé na déšť (dešťový útlum) ve vyšších pásmech.

### Antény – typy a parametry
| Typ antény | Vyzařovací charakteristika |
|---|---|
| **Izotropní** | (teoretická) vyzařuje stejně do všech směrů |
| **Všesměrová (omni)** | kruhová horizontálně (anténa pro AP) |
| **Sektorová** | určitý úhel (např. 60°/90°/120°) – pro WISP |
| **Směrová (parabolická, Yagi)** | úzký svazek – bod-bod spoje |

#### Zisk antény
- **dBi** – zisk vůči izotropní anténě.
- **dBd** – zisk vůči dipólu.
- **dBi je o 2,15 dB větší než dBd** (izotropní je horší referenční bod).
- **dBm** = decibel milliwatt = výkon vůči 1 mW. 20 dBm = 100 mW.

### Fresnelova zóna
![[8 Fresnelova zona.png]]

**Fresnelova zóna** = oblast kolem přímé spojnice antén ve tvaru **paraboloidu (rotačního elipsoidu)**, ve které se šíří podstatná část energie radiového signálu.

```
       ────────────                 ────────────
       \           \               /           /
         \    F1    \    Pevný    /     F2    /
   ANT1   \─────────────signál───────────────/  ANT2
         /                                  \
       /          (paraboloid)               \
       ────────────                ────────────
```

- **Předměty v Fresnelově zóně zeslabují signál** (i když je přímá viditelnost zachována).
- 1. Fresnelova zóna by měla být **alespoň z 60 % volná**.
- Velikost zóny závisí na frekvenci a vzdálenosti antén.

### Problém skrytého uzlu (hidden node)
**Situace**: dvě stanice A a C jsou v dosahu AP, ale **nevidí navzájem** (např. zdi, vzdálenost). Obě začnou vysílat současně → na AP **kolize**, ale CSMA/CA to neumí detekovat (každá stanice „slyší" jen sebe).

```
   [A] ─── slyší ──→ [AP] ←── slyší ── [C]
   [A] ✗ NEslyší ✗ [C]
```

**Řešení: RTS/CTS** (Request to Send / Clear to Send)
1. **A** chce vysílat → pošle krátký rámec **RTS** s časem trvání přenosu.
2. **AP** odpoví **CTS** broadcastem – obsahuje stejný čas.
3. **C** sice neslyší A, ale **slyší CTS od AP** a ví, že má mlčet po danou dobu.
4. A vysílá, C čeká.

```
A: ──RTS──>           AP: ──CTS──> (broadcast, slyší ho i C)
                       │
A vysílá data...       │
                       │
A: ──ACK potvrzení──>  │
```

### Pasivní vs aktivní retranslace
- **Pasivní** – odraz, přesměrování (zrcadlo, parabola).
- **Aktivní centralizovaná** – 1 prvek (AP).
- **Aktivní distribuovaná** – víc aktivních prvků (mesh, repeatery).

### MIMO technologie
Více antén pro vyšší propustnost.
| Vysílání / Příjem | Označení |
|---|---|
| 1 / 1 | SISO |
| 1 / více | **SIMO** |
| Více / 1 | **MISO** |
| Více / Více | **MIMO** |

### Vzorová odpověď
Bezpečnost Wi-Fi prochází vývojem WEP → WPA → WPA2 → WPA3 (nejúčinnější). Architektura má dva režimy: ad-hoc (peer-to-peer) a infrastructure s přístupovým bodem (BSS, ESS pro roaming). Mikrovlnné spoje slouží pro bod-bod přenos v licencovaných pásmech. Antény mají různé vyzařovací charakteristiky (izotropní teoretická, všesměrová, směrová), zisk se udává v dBi (vůči izotropní) nebo dBd (vůči dipólu, o 2,15 dB méně). Fresnelova zóna je paraboloid kolem přímky mezi anténami, ve kterém se šíří signál – předměty v něm signál zeslabují. Problém skrytého uzlu vzniká když dva klienti nevidí navzájem, ale oba vidí AP – řeší ho mechanismus RTS/CTS.

---
