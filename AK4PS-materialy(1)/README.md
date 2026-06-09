# 📚 AK4PS – Počítačové sítě (UTB Zlín) – Návod pro budoucí studenty

> **Autor:** Pranav Vajgl
> **Složeno:** 2026-05-26, známka **D**
> **Vyučující:** Matýsek (LS 2025/2026)

Tento adresář obsahuje **kompletní studijní materiály**, které ti pomůžou složit AK4PS bez stresu. Níže je strategie, která fungovala mně, a kde co najít.

---

## 🎯 Realistický popis kurzu (čti první!)

- **Forma:** Písemný test z 35 okruhů. Hodně **trik-otázek** na přesné formulace (typu „IPv8 existuje?" → ne; „zkreslení přenosovým kanálem" → R-L-C-G, ne EMI).
- **Materiály vyučujícího:** PDF prezentace ~387 stran, **nehledatelná** (scan). Velmi detailní, často biflování konkrétních čísel.
- **Praktická využitelnost:** Nízká. V práci se 99 % řeší přes reference manuály, ne paměť. Po zkoušce klidně **konkrétní čísla zapomeň** a drž si **koncepty** (OSI, TCP/UDP, IP).
- **Strategie:** Učit se z **taháku** + procvičovat **trik-otázky**, ne číst prezentaci od začátku do konce.

---

## 📁 Co je v této složce

| Soubor / složka | K čemu slouží |
|---|---|
| **OKRUHY_2026.md** | 35 okruhů v jednom souboru. **Primární studijní zdroj.** Pokrývá ~90 % obsahu testu. |
| **OKRUHY_2026/** (složka) | Stejných 35 okruhů, ale **každý zvlášť** — pro fokusované učení okruh po okruhu. |
| **TAHAK_BLESK.md** | 🔑 **Tahák pro poslední den.** Všechna arbitrární čísla a fakta na jedné stránce (802.x, Wi-Fi, optika, porty, roky, IP třídy, dBm…). |
| **FULL_TAHAK.md** | Sbírka reálných otázek z předchozích testů. Slouží k trénování trik-otázek. |

---

## 🗺️ Doporučená strategie učení (3 fáze)

### Fáze 1 — Pochopení (čas: ~3 dny)
1. Pročti **OKRUHY_2026** od začátku do konce. Cíl: pochopit logiku, ne memorovat.
2. Když narazíš na něco nejasného, hledej v prezentaci. **Není potřeba číst celou.**
3. Skip rote-memorovací úseky (přesná čísla GHz/dB) — k tomu se vrátíš.

### Fáze 2 — Active recall (čas: ~3 dny)
1. Projeď **TAHAK_BLESK** sekci po sekci. **Zakryj odpověď, řekni z hlavy, odkryj.**
2. Co neumíš → poznámka, do dalšího kola.
3. Opakuj, dokud neumíš celý TAHAK_BLESK bez podívání.

### Fáze 3 — Trik-otázky (čas: 1 den před zkouškou)
1. Projdi **CHYTAKY_DEKODER** + **FULL_TAHAK**.
2. Naučí tě **rozeznat past** podle klíčových slov v zadání (např. „přenosovým kanálem" = R-L-C-G, ne EMI).
3. **Den před zkouškou: jen TAHAK_BLESK rychle**, žádné nové učivo.

---

## ⚠️ TOP chytáky, na kterých se nejvíc padá

Tyto byly v testu a/nebo v reálných taháku. **Stojí za podrobné nastudování:**

| # | Past | Správně |
|---|---|---|
| 1 | „Zkreslení signálu **přenosovým kanálem** u metaliky" | **R-L-C-G** (Odpor, Indukčnost, Kapacita, Svod) → mnemo **OKIS**. NE EMI/přeslechy! |
| 2 | IPv5, IPv7, IPv8 existují? | **NE.** Existuje jen IPv4 a IPv6 |
| 3 | „Fyzická topologie hvězda" + hub | Fyzicky hvězda, **logicky sběrnice** |
| 4 | DNS na které OSI vrstvě? | **L5 relační** (v OSI) NEBO **L7 aplikační** (v TCP/IP). Záleží na otázce! |
| 5 | Wi-Fi proč CSMA/**CA** místo CSMA/CD? | Vzduch = poloduplex + **skrytý uzel** (hidden node) |
| 6 | EMI vs EMS | **EMI = vyzařování** ven; **EMS = odolnost** zvenku |
| 7 | Plášť optického vlákna vede světlo? | **NE!** Vede ho **jádro**. Plášť je zrcadlo (totální odraz). |
| 8 | Adresa typu `0.0.125.131` v třídě B | **NEPATŘÍ** (B začíná 128) |
| 9 | Lepený FO spoj lepší než svařený? | **NEPRAVDA.** Svařený je nejlepší |
| 10 | „NetBIOS/NetBEUI routovatelné?" | **NE.** Oba nerouturovatelné |
| 11 | „Pravidlo 5-4-3" u 10BASE-T | 5 segmentů, 4 repeatery, 3 osazené segmenty |
| 12 | BCD kód = binární zápis? | **NE.** BCD = každá dekadická cifra zvlášť v 4 bitech |

---

## 🧠 Mnemonika, která fungovala

| Téma | Mnemo |
|---|---|
| **R-L-C-G** primární parametry vedení | **OKIS** (Odpor, Kapacita, Indukčnost, Svod) |
| **EMI vs EMS** | **I**ssue (ven) vs **S**nesu (dovnitř) |
| **PAN < LAN < CAN < MAN < WAN < GAN** | „**P**oslušné **L**ámání **C**hleba **M**ezi **W**ánoční **G**alou" |
| **OSI 7 vrstev zdola** | „Fyzická-Linková-Síťová-Transportní-Relační-Prezentační-Aplikační" |
| **PDU zdola nahoru** | **B**ity → **R**ámec → **P**aket → **S**egment (B-R-P-S) |
| **Optika SM vs MM** | SM = **L**aser + **L**ong; MM = **L**ED + **L**ocal |
| **Roky historie** | ARPANET **1969** (Měsíc), TCP/IP **1983** (+14), ČSFR **1992** (+9) |
| **Wi-Fi nepřekrývající kanály** | ČR: **1, 7, 13** (po 6); USA: **1, 6, 11** (po 5) |
| **Nej-pravidlo TCP/IP vrstev** | TCP/UDP = transportní; IP/ICMP/ARP = internet; Ethernet/Wi-Fi = síťové rozhraní; **cokoli jiného = aplikační** |

---

## 💡 Praktické tipy do testu

1. **Čti zadání 2×.** Trik je často v jednom slově („přenosovým kanálem", „omezený", „samostatný").
2. **Když nevíš:**
   - „Kolik bytů" → tipuj mocninu dvou (4, 8, 16) nebo násobek 4
   - „Kolik vrstev" → 7 (OSI) nebo 4 (TCP/IP)
   - „Rok" → 1969 / 1983 / 1989 / 1992
   - Standard 802 → 11 = Wi-Fi, 3 = Ethernet
3. **„Identifikuje které tvrzení je SPRÁVNÉ/NESPRÁVNÉ"** — projdi všechny varianty a hledej tu jednu, co zní očividně blbě nebo naopak.
4. **Nestresuj nad detaily, kterým nerozumíš.** V kurzu je víc faktů, než zvládneš. Lépe znát 80 % dobře než 100 % chaoticky.

---

## 🙅 Co IGNOROVAT (nebudou se ptát / nedá se to naučit)

- Detaily skupinového potvrzování
- Přesné rozdíly NetBEUI vs NetBIOS detaily
- Konkrétní procentní rychlosti backoffu po pokusu N
- Historické varianty IPX adresování
- Hluboké detaily ATM/ISDN (zmiňováno, ale málo)

---

## 📞 Kontakt / Doplnění

Pokud najdeš chyby nebo přidáš něco užitečného (např. po své zkoušce), **uprav tento README**. Cílem je, ať budoucí studenti **nemusí trpět** jako my.

**Hodně štěstí. 🍀 Ty to dáš.**

— Pranav, ročník 2026
