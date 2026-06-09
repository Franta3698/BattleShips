---
cislo: 15
nazev: Standardy IEEE 802
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 15) Standardy IEEE 802

### Co to je
**IEEE 802** = rodina standardů Institute of Electrical and Electronics Engineers pro **LAN, MAN a WLAN**. Standardy definují fyzickou a linkovou vrstvu.

### Architektura IEEE 802 a vztah k OSI
IEEE 802 dělí **linkovou vrstvu (L2)** na dvě podvrstvy:
```
   OSI vrstva 2 (Linková)
   ┌────────────────────────┐
   │   LLC – 802.2          │ ← logické řízení (společné všem)
   ├────────────────────────┤
   │   MAC – 802.3, 802.11, │ ← přístup k médiu (specifické)
   │         802.5, …       │
   └────────────────────────┘
   OSI vrstva 1 (Fyzická)
```

### Klíčové standardy
| Standard | Co řeší |
|---|---|
| **IEEE 802.1** | architektura, mosty (bridging), VLAN (802.1Q), spanning tree (802.1D) |
| **IEEE 802.2** | **LLC** – logické řízení linky (společné pro všechny MAC) |
| **IEEE 802.3** | **Ethernet** (CSMA/CD) |
| 802.4 | Token Bus (historicky) |
| **802.5** | **Token Ring** (IBM) |
| 802.6 | DQDB – MAN (historicky) |
| 802.7 | broadband (historicky) |
| 802.8 | optická vlákna (historicky) |
| 802.9 | integrovaný hlas + data |
| 802.10 | bezpečnost |
| **802.11** | **Wi-Fi / WLAN** |
| **802.15** | **WPAN** – Bluetooth (802.15.1), ZigBee (802.15.4) |
| **802.16** | **WiMAX** (WMAN) |
| 802.17 | Resilient Packet Ring |

### Klíčová fakta pro zkoušku
- **IEEE 802.3 = Ethernet** (standard CSMA/CD na 1 Gb/s a méně).
- **IEEE 802.11 = Wi-Fi** (CSMA/CA).
- **IEEE 802.2 = LLC** (společná horní podvrstva linkovky).
- **Předložen standard Ethernetu**: **802.3**.
- **Standard popisující LAN s CSMA/CD**: **802.3**.
- **Standard pro bezdrátové sítě**: **802.11**.
- **Standard pro Bluetooth**: **802.15.1**.

### Vzorová odpověď
IEEE 802 je rodina standardů od IEEE pro LAN/MAN/WLAN. Pokrývá fyzickou a linkovou vrstvu OSI a linkovou rozděluje na dvě podvrstvy: LLC (802.2 – logické řízení, společné) a MAC (specifické: 802.3 Ethernet, 802.11 Wi-Fi, 802.15 Bluetooth/ZigBee, 802.16 WiMAX). Klíčové k zapamatování: 802.3 = Ethernet (CSMA/CD), 802.11 = Wi-Fi (CSMA/CA), 802.2 = LLC.

---
