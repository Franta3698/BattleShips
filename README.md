

<h1 align="center">Námořní bitva (Battleships)</h1>


> **Autor:** František Hradil  
> **Předmět:** AP2PN  
> **Akademický rok:** 2025/2026  

Konzolová hra pro dva hráče inspirovaná klasickou hrou Námořní bitva.  
Aplikace umožňuje strategické rozmístění lodí na herní pole a následnou simulaci střelby s automatickým vyhodnocováním zásahů a vítězství.

---

## 📋 Obsah

- [✨ Funkce](#-funkce)
- [📋 Požadavky](#-požadavky)
- [🔧 Instalace](#-instalace)
- [▶️ Spuštění](#️-spuštění)
- [🧪 Testování](#-testování)
- [📁 Struktura projektu](#-struktura-projektu)
- [🔄 CI/CD Pipeline](#-cicd-pipeline)
- [📖 Generování dokumentace](#-generování-dokumentace)
- [📝 Licence](#-licence)

---

## ✨ Funkce

- **Správa hráčů:** Inicializace hráčů a sledování jejich stavu (HP, herní pole)
- **Validace sonar:** Kontrola kolizí a přetečení při umisťování lodí
- **Herní logika:** Střídavý systém tahů s bonusovým výstřelem při zásahu
- **CLI rozhraní:** Zobrazení herního pole přímo v terminálu

---

## 📋 Požadavky

- Python 3.10+
- pip

---

## 🔧 Instalace

1. **Naklonování repozitáře**
```bash
git clone https://gitlab.utb.cz/vase-username/nazev-projektu.git
cd nazev-projektu
```

2. **Virtuální prostředí (doporučeno)**
```bash
python -m venv venv

# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. **Instalace závislostí**
```bash
pip install -r requirements.txt
```

---

## ▶️ Spuštění

```bash
python -m maingame.main
```

---

## 🧪 Testování

### Spuštění testů
```bash
python -m pytest
```

### Coverage report
```bash
python -m pytest --cov=maingame --cov-report=term-missing
```

### Linting (PEP 8)
```bash
python -m flake8 maingame/ tests/
```

---

## 📁 Struktura projektu

```text
projekt/
├── maingame/
│   ├── __init__.py
│   ├── main.py
│   └── playerLogic.py
├── tests/
│   ├── __init__.py
│   └── testPlayer.py
├── docs/
├── .gitlab-ci.yml
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🔄 CI/CD Pipeline

Projekt využívá GitLab CI/CD:

| Stage | Nástroj | Popis |
|------|--------|------|
| lint | flake8 | Kontrola stylu kódu |
| test | pytest | Spouštění unit testů |
| docs | pdoc | Generování dokumentace |

---

## 📖 Generování dokumentace

```bash
pdoc maingame tests -o docs --docformat numpy
```

---

## 📝 Licence

Tento projekt byl vytvořen jako závěrečný projekt na UTB ve Zlíně.
