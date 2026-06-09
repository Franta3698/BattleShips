---
cislo: 17
nazev: Potvrzování PDU včetně potvrzování TCP
predmet: AK4PS
tags:
  - okruh
  - ak4ps
---

## 17) Potvrzování PDU včetně potvrzování TCP

### Proč se potvrzuje
Pokud chce odesílatel **mít jistotu, že paket dorazil**, příjemce musí potvrdit. Typy potvrzování se liší dle „kdy" a „jak" potvrzuje.

### Typy potvrzování PDU
| Typ                          | Princip                                                         | Příklad               |
| ---------------------------- | --------------------------------------------------------------- | --------------------- |
| **Pozitivní (ACK)**          | příjemce potvrzuje doručené PDU                                 | TCP                   |
| **Negativní (NAK)**          | příjemce potvrzuje **až chybu** (nedoručené/poškozené)          | některé sériové linky |
| **Kombinované**              | ACK + NAK podle situace                                         | –                     |
| **Skupinové**                | jedno potvrzení pokrývá celé skupiny PDU (např. ACK na N rámců) | sliding window        |
| **Nesamostatné (piggyback)** | potvrzení „svezeno" v datovém PDU jdoucím opačným směrem        | TCP duplex            |

### Ke ztrátě potvrzení – chování
| Typ                            | Co se stane při ztrátě ACK                     |
| ------------------------------ | ---------------------------------------------- |
| Pozitivní                      | odesílatel **opakovaně vysílá data** (timeout) |
| Negativní                      | nic se nestane (pokud nepřišlo NAK, vše OK)    |
| **Skupinové bez číslování**    | **zdvojení dat** (příjemce dostane podruhé)    |
| **Nesamostatné bez číslování** | **zdvojení dat**                               |

> Klíč: **pozitivní → opakované vysílání**; **skupinové a nesamostatné bez číslování → zdvojení PDU**. (Číslování v hlavičce tomu zabrání – příjemce duplikát detekuje a zahodí.)

### Potvrzování v TCP
TCP používá **pozitivní potvrzování s posuvným oknem (sliding window)** a **kumulativní ACK**.

#### TCP segment hlavička (klíčová pole)
| Pole | Význam |
|---|---|
| **Sequence Number** | pořadí prvního bajtu v segmentu |
| **Acknowledgment Number** | pořadí dalšího očekávaného bajtu (kumulativní ACK) |
| **Window Size** | kolik bajtů ještě může příjemce přijmout |
| Flags | SYN, ACK, FIN, RST, PSH, URG |
| Checksum | kontrolní součet |

#### Třícestný handshake (navázání spojení)
```
Klient                              Server
  │ ──── SYN, seq=x ─────────────→ │
  │ ←─── SYN+ACK, seq=y, ack=x+1 ─│
  │ ──── ACK, ack=y+1 ───────────→│
   spojení navázáno
```

#### Posuvné okno (sliding window)
- Odesílatel pošle několik segmentů **bez čekání** na ACK (do velikosti okna).
- Příjemce posílá ACK s **„očekávaným dalším bajtem"** – kumulativní.
- Pokud chybí segment uprostřed → příjemce posílá **duplikátní ACK** (selektivní opakování přes SACK).

#### Příklad
```
Seq=1:  data 1-1000   →
Seq=1001: data 1001-2000 →
Seq=2001: data 2001-3000 →
                            ← ACK=3001  (vše do 3001 OK, čekám další)
```

#### Ztráta segmentu a opakování
- Po vypršení **retransmission timeout (RTO)** → opakuje neACKnuté segmenty.
- **Fast retransmit**: 3 duplikátní ACK → ihned opakuj, nečekej RTO.

#### Uzavření spojení (4-way)
```
Klient                          Server
  │ ──── FIN ──────────────→  │
  │ ←─── ACK ─────────────────│
  │ ←─── FIN ─────────────────│
  │ ──── ACK ──────────────→  │
```

### Vzorová odpověď
Potvrzování PDU má pět typů: pozitivní (ACK – potvrzení doručení), negativní (NAK – jen při chybě), kombinované, skupinové (1 ACK za víc PDU) a nesamostatné (piggyback – ACK svezený s daty). Při ztrátě ACK u pozitivního dojde k opakovanému vysílání; u skupinového a nesamostatného bez číslování v hlavičce dojde ke zdvojení. TCP používá pozitivní potvrzování s posuvným oknem a kumulativním ACK (Acknowledgment Number = pořadí dalšího očekávaného bajtu). Spojení se navazuje 3-way handshakem (SYN, SYN+ACK, ACK) a uzavírá 4-way (FIN, ACK, FIN, ACK). Při ztrátě segmentu se po RTO opakuje, případně fast retransmit při 3 duplikátech ACK.

---
