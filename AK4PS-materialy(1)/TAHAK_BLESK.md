# ⚡ Tahák BLESK – poslední opakování před zkouškou

> Pro arbitrární čísla a fakta, která se NEDAJÍ odvodit. K plnému teoretickému taháku viz [[TAHAK_CISTY]].

---

## 🧩 IEEE 802.X – které číslo je co

| Číslo      | Co je                                               |
| ---------- | --------------------------------------------------- |
| **802.1**  | rozhraní k vyšším vrstvám, adresace                 |
| **802.2**  | **LLC** (Logical Link Control) – nezávislé na médiu |
| **802.3**  | **Ethernet (CSMA/CD)**                              |
| **802.4**  | Token Bus                                           |
| **802.5**  | Token Ring                                          |
| **802.6**  | **MAN** (DQDB)                                      |
| **802.7**  | Broadband (přeložen)                                |
| **802.11** | **Wi-Fi**                                           |
| **802.15** | **Bluetooth, WPAN**                                 |
| **802.16** | **WiMax (WMAN)**                                    |

🧠 **Trik:** 1=interface, 2=LLC, 3=Ethernet (vždy první 3 jdou logicky). **11=Wi-Fi**, **15=BT**, **16=WiMax** zkus jako trojici „radio: 11/15/16".

---

## 📶 Wi-Fi varianty 802.11

| Standard | Pásmo | Max rychlost |
|---|---|---|
| **a** | 5 GHz | 54 Mb/s |
| **b** | 2,4 GHz | 11 Mb/s |
| **g** | 2,4 GHz | 54 Mb/s |
| **n** | 2,4 + 5 | 600 Mb/s |
| **ac** | 5 GHz | 6,77 Gb/s |
| **ax** | 2,4 + 5 + 6 | 9,6 Gb/s (Wi-Fi 6) |
| **be** | 2,4 + 5 + 6 | 46 Gb/s (Wi-Fi 7) |

🧠 **Trik:** `b` je **B**ída (11 Mb), `a` byl 5 GHz hned od začátku, `g` = jako b ale rychlejší, `n` = první multi-pásmo. **`g` zpětně kompatibilní s `b`** (oba 2,4 GHz).

---

## 📻 Pásma a kanály

- **2,4 GHz v ČR**: **13 kanálů** šířky 20 MHz
- **Nepřekrývající se kanály ČR**: **1, 7, 13** (USA: 1, 6, 11)
- **Max nerušené sítě v 2,4 GHz**: **3**
- **Max výkon 2,4 GHz v ČR**: **20 dBm = 100 mW**
- **5 GHz**: **19 subpásem**
- **5,470–5,725 GHz**: **11 nepřekrývajících kanálů**
- **5 GHz min. výkon antény**: **1000 mW (1 W)**
- **6 GHz**: 59 kanálů
- **Bezlicenční pásma**: 2,4 / 5 / 6 / 10,5 GHz
- **Licencované**: 3,5 / 26 / 28 GHz

---

## 🔐 Šifrování Wi-Fi (vzestupně)

**WEP < WPA < WPA2 < WPA3**
- ✅ Nejúčinnější: **WPA3**
- ❌ Slabé dnes: **WEP**
- Ad-hoc obvykle: WEP

---

## 💡 Optická vlákna – vlnové délky

**850, 1300, 1310, 1550 nm**

🧠 **Trik:** pamatuj „**8-13-15**" (× ~100 dá nm). 850 nm pro krátké, 1550 nm pro dlouhé.

- Útlum nejkvalitnějšího jednovidu: **0,2 dB/km**
- **9/125** = jednovidové (laser, dlouhé)
- **62,5/125** = mnohovidové (LED, krátké)
- Max rychlost na 1 vlákně / 1 vlnové délce: **100 Gb/s**
- DWDM max vlnových délek na 1 vláknu: **160**
- Vidová disperze v: **ns/km**
- Bez retranslace jednovidem až: **přes 100 km**

🧠 **Konektory FO** (NEPATŘÍ RJ-45, RJ-11, BNC): FC, ST, SC, E2000, MTRJ

---

## 🔌 Porty (well-known)

| Port | Protokol |
|---|---|
| 20, 21 | **FTP** (data, řízení) |
| 22 | SSH |
| 23 | Telnet |
| **25** | **SMTP** |
| 53 | DNS |
| **80** | **HTTP** |
| **110** | **POP3** |
| 143 | IMAP4 |
| 443 | HTTPS |

🧠 **Rozsahy**: 0–1023 = známé, 1024–49151 = registrované, 49152–65535 = dynamické.

---

## 📅 Roky (historie)

| Rok | Co |
|---|---|
| **1969** | ARPANET |
| **1977** | start vývoje TCP/IP |
| **1983** | TCP/IP zaveden do ARPANETu |
| **1984** | DNS zaveden |
| 1986 | NSF financování |
| **1989** | WWW (Berners-Lee) |
| 1990 | pevná linka ČSFR |
| 1991 | pokus o připojení ČSFR |
| **1992** | komerční Internet v ČSFR |
| 1993 | doména **.cz** |
| 1995 | cz místo cs |

🧠 **Trik:** ARPANET **1969** (jako přistání na Měsíci). Pak +14 = TCP/IP 1983, +6 = WWW 1989, +3 = ČSFR 1992.

První sítě obecně: **začátek 70. let**.

---

## 📦 Ethernet – tabulkové memory

### Nejkratší rámec (v bitech)
| Rychlost | Bity |
|---|---|
| 10 Mb/s | **512** |
| 100 Mb/s | **512** |
| **1 Gb/s** | **4096** |
| 10 Gb/s | – (nepoužívá se) |

### Doba odvysílání 1 bitu
| Rychlost | Doba |
|---|---|
| 10 Mb/s | 100 ns |
| 100 Mb/s | 10 ns |
| 1 Gb/s | 1 ns |
| 10 Gb/s | 0,1 ns |

🧠 **Vzorec:** `1 / rychlost`. 10 Mb = 10⁷ b/s, 1 b = 10⁻⁷ s = 100 ns. Každá ×10 rychlost = ÷10 doba.

### Mezirámcová mezera (IFG): **96 bitů**
### Max pokusů CSMA/CD: **16**, max `k` pro backoff: **10** (2¹⁰=1024)

### Kategorie TP
| Cat | Pro |
|---|---|
| 3 | 10 Mb |
| 5 | 100 Mb |
| **5e** | **1 Gb** |
| 6 | 5 Gb |
| **6a** | **10 Gb** |
| 8 | 40 Gb |

### Kódování
| Rychlost | Kódování |
|---|---|
| 10 Mb | Manchester (fázové NRZ) |
| 100 Mb | 4B/5B + MLT-3 / NRZI |
| 1 Gb | PAM5 nebo 8B/10B |

---

## 🌐 IP adresy – rozsahy 1. byte (musíš znát!)

| Třída | 1. byte | K čemu |
|---|---|---|
| A | **1–127** | unicast |
| B | **128–191** | unicast |
| C | **192–223** | unicast |
| D | **224–239** | multicast |
| E | **240–255** | rezerva |

🧠 **Mnemotechnika:** 127 → 128 → 192 → 224 → 240 (pohybuje se po mocninách dvou: +1, +64, +32, +16)

### Default masky
- A = /8 = `255.0.0.0`
- B = /16 = `255.255.0.0`
- C = /24 = `255.255.255.0`

### Použitelné adresy – **vzorec**: `2^(32-prefix) - 2`
- /23 → 510, /24 → 254, /25 → 126, /26 → 62, /27 → 30, /28 → 14, /29 → 6, /30 → 2

### Privátní (NAT)
- **10.x.x.x** (třída A)
- **172.16–31.x.x** (třída B)
- **192.168.x.x** (třída C)

### Vyhrazené
- `0.0.0.0` = nemá adresu
- `127.x.x.x` = loopback
- `255.255.255.255` = omezený broadcast
- `169.254.x.x` = APIPA (link-local)

### IPv4 = **4 byte = 32 bitů**, IPv6 = **16 byte = 128 bitů**

---

## 📐 Antény a výkon

- **dBi vs dBd**: dBi je o **2,15 dB** větší než dBd
- **dBm**: `10 · log(P[W] / 0,001)`
- **20 dBm = 100 mW** (10 dB = 10×; každých +10 dBm = ×10)
- **0 dBm = 1 mW**, **30 dBm = 1 W**
- Snížení **výkonu** na 25 % = **−6 dB**
- Snížení **napětí** na 50 % = **−6 dB**, na 25 % = **−12 dB**
- Fresnelova zóna = **paraboloid**, signál uvnitř

### MIMO technologie
- **SIMO** = 1 vysílá, víc přijímá
- **MISO** = víc vysílá, 1 přijímá
- **MIMO** = víc / víc

🧠 **Trik:** **I**nput = strana vysílače (do kanálu), **O**utput = strana přijímače. Single/Multiple v tom pořadí.

---

## ⚙️ Důležitá samostatná čísla

- **ALOHA propustnost**: základní **18 %**, taktovaná **36 %** (taktovaná je 2× lepší)
- **Repeater**: **2 porty**
- **Coax dobrý do**: **~1 GHz**
- **Coax pro TV**: 75 Ω, **pro Wi-Fi/Ethernet**: 50 Ω
- **TP pro LAN**: 100 Ω, **8 vodičů** (4 páry)
- **Konektor RJ-45**: 8 kontaktů, RJ-11/12=6, RJ-10=4, RJ-48=10
- **Bezdrátový kanál 802.11ac**: max 4
- **Frekvence k 1 b/s**: 0,5 Hz (1 Hz = **2** b/s)
- **VLAN ID**: 12 bitů (1–4096), tag 4B
- **Preamble**: **56 bitů**, SFD: **8 bitů**
- **Data v 802.3+802.2**: **46–1500 byte** (MTU 1500)

---

## ❗ Nejčastější chytáky

1. **DNS protokol** – v OSI je vrstva **5** (relační), v TCP/IP modelu **aplikační (7)**. Záleží na otázce!
2. **IPX** = vrstva **3** (síťová, jako IP). **SPX** = vrstva **4**.
3. **NetBIOS** = vrstva **5**. **NetBEUI** = vrstvy 3+4. **Nerouturovatelné** oba.
4. **Adresa 0.0.125.131 v třídě B** = **nepatří tam** (B začíná 128, ne 0).
5. **Adresa 196.265.148.63** = neplatná (265 > 255).
6. **WPA3** = nejlepší. WPA2 byla starší verze otázky.
7. **Doména musí mít alespoň 1 DNS server** (typicky 2).
8. **Která média Ethernet NEpoužívá**: **rádiové vlny** (to je Wi-Fi).
9. **CSMA/CD smysl ztrácí se switchem** v plném duplexu.
10. **Lepený spoj FO LEPŠÍ než svařený**: **NEPRAVDA** (svařený je nejlepší).
11. **Průběžná změna indexu lomu**: **jen u mnohovidu**.

---

## 🗓️ Pořadí sítí podle velikosti

**PAN < LAN < CAN < MAN < WAN < GAN**

| Zkratka | Rozsah |
|---|---|
| PAN | metry |
| LAN | desítky–stovky m |
| CAN | stovky m – jednotky km |
| MAN | jednotky–desítky km |
| WAN | desítky km+ |
| GAN | celosvět. |

🧠 **Trik:** PLČMWG → **P**oslušné **L**ámání **C**hleba **M**ezi **W**ánoční **G**alou. (Nebo si vymysli vlastní 🙂)

---

## 🚦 Vrstvy aktivních prvků

| Zařízení | Vrstva |
|---|---|
| Repeater, Hub | **1** |
| Bridge, Switch | **2** |
| Router | **3** |
| Gateway | **7** |

---

## Co fakt ignorovat / nestresovat

Tyhle věci se asi neptat nebudou, a kdyby ano – ber zdravý odhad:

- Detailní typy potvrzování (skupinové vs nesamostatné) – samotná zkouška s tím má taky problém
- Přesné rozdíly mezi historickými variantami IPX adresování
- Konkrétní procentní rychlosti backoffu po pokusu N
- Přesné rozdíly NetBEUI vs NetBIOS detaily

---

> **Strategie u zkoušky:** Když nevíš a otázka je „kolik byte" → tipuj **mocninu dvou nebo násobek 4** (typicky 4, 6, 8, 16). Když „kolik vrstev" → **7** (OSI) nebo **5** (TCP/IP). Roky → 1969 / 1989 / 1992. Standard 802 → 11 = Wi-Fi, 3 = Ethernet.
