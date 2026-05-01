<p align="center">
  <img src="icon.svg" alt="Battleships Logo" width="80">
  <h1 align="center">Námořní bitva (Battleships)</h1>
</p>

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pipeline](https://img.shields.io/badge/CI%2FCD-GitLab-orange.svg)

> **Autor:** [František Hradil]
> **Předmět:** [AP2PN]
> **Akademický rok:** 2025/2026

Konzolová hra pro dva hráče inspirovaná klasickou hrou Námořní bitva. Aplikace umožňuje strategické rozmístění lodí na herní pole a následnou simulaci střelby s automatickým vyhodnocováním zásahů a vítězství.

---

## 📋 Obsah

- [📋 Obsah](#-obsah)
- [✨ Funkce](#-funkce)
- [📋 Požadavky](#-požadavky)
- [🔧 Instalace](#-instalace)
- [▶️ Spuštění](#️-spuštění)
- [🧪 Testování](#-testování)
  - [Spuštění testů](#spuštění-testů)
  - [Spuštění testů s coverage reportem](#spuštění-testů-s-coverage-reportem)
  - [Statická analýza kódu (linting)](#statická-analýza-kódu-linting)
- [📁 Struktura projektu](#-struktura-projektu)
- [🔄 CI/CD Pipeline](#-cicd-pipeline)
- [📖 Generování dokumentace](#-generování-dokumentace)
- [📝 Licence](#-licence)

---

## ✨ Funkce

- **Správa hráčů:** Inicializace hráčů a sledování jejich stavu (HP, herní pole).
- **Validace sonar:** Inteligentní systém kontroly kolizí a přetečení při umisťování lodí.
- **Herní logika:** Střídavý systém tahů s bonusovým výstřelem při úspěšném zásahu.
- **CLI rozhraní:** Interaktivní grafické zobrazení herního pole přímo v terminálu.

---

## 📋 Požadavky

- Python 3.10+
- pip (správce balíčků)

---

## 🔧 Instalace

1. **Naklonujte repozitář:**
   ```Bash
   git clone [https://gitlab.utb.cz/vase-username/nazev-projektu.git](https://gitlab.utb.cz/vase-username/nazev-projektu.git)
   cd nazev-projektu


2. **Vytvořte virtuální prostředí (doporučeno):**
    ```Bash

    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # nebo
    venv\Scripts\activate     # Windows
3. **Nainstalujte závislosti**
pip install -r requirements.txt

## ▶️ Spuštění
Aplikaci spustíte jako modul z kořenového adresáře:
    ```Bash
    python -m maingame.main
    python -m pytest
## 🧪 Testování

**Spuštění testů**
Používá framework pytest pro ověření logiky lodi a sonaru.
    ```Bash
    python -m pytest
**Spuštění testů s coverage reportem**
Zjistí, kolik procent kódu je pokryto testy.
    ```Bash
    python -m pytest --cov=maingame --cov-report=term-missing
**Statická analýza kódu (linting)**
Kontrola dodržování stylu PEP 8.
    ```Bash
    python -m flake8 maingame/ tests/

## 📁 Struktura projektu


projekt/
├── maingame/               # Zdrojový kód aplikace
│   ├── __init__.py         # Metadata a dokumentace balíčku
│   ├── main.py             # Vstupní bod aplikace (Herní smyčka)
│   └── playerLogic.py      # Logika hráčů a herní desky
├── tests/                  # Unit testy
│   ├── __init__.py
│   └── testPlayer.py       # Testy pro třídu Player a sonar
├── docs/                   # Automaticky generovaná dokumentace (HTML)
├── .gitlab-ci.yml          # CI/CD pipeline konfigurace
├── requirements.txt        # Python závislosti (pdoc, pytest, flake8)
├── pytest.ini              # Konfigurace testovacího prostředí
└── README.md               # Dokumentace projektu


## 🔄 CI/CD Pipeline
Projekt využívá GitLab CI/CD pro automatizaci kvality kódu:

Stage,Nástroj,Popis
lint,flake8,Kontrola formátování a stylu kódu.
test,pytest,Automatické spouštění unit testů.
docs,pdoc,Generování HTML dokumentace z docstringů.

## 📖 Generování dokumentace

Dokumentace je psána v NumPy stylu a generována nástrojem pdoc.
    Bash
    pdoc maingame tests -o docs --docformat numpy

## 📝 Licence
Tento projekt byl vytvořen jako závěrečný projekt na UTB ve Zlíně.