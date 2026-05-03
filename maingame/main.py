"""
Hlavní modul aplikace - CLI rozhraní hry Námořní bitva.

Tento modul zajišťuje interaktivní logiku hry pro dva hráče.
Obsahuje fázi rozestavění lodí na herní pole a následnou fázi
střídavé střelby na soupeřovy lodě až do vítězství jednoho z hráčů.

Spuštění
--------
Aplikaci spustíte příkazem::
    python -m main

Průběh hry
----------
1. Zadání jmen obou hráčů.
2. Rozestavení 4 typů lodí (velikosti 5, 4, 3, 3) na pole 8x8.
3. Střídavá střelba: při zásahu hráč střílí znovu.
4. Konec hry nastává při snížení HP soupeře na 0.
"""

import os
from . import playerLogic


def main():
    """
    Hlavní smyčka hry (MainLoop).

    Zajišťuje inicializaci hráčů, volání metod pro položení lodí
    a řízení střídavých tahů v ShootLoop. Po skončení hry nabízí
    možnost opakování (Rematch).
    """
    while True:
        turn = 0
        players = []
        for i in range(2):
            os.system('cls' if os.name == 'nt' else 'clear')
            name = input(f"Zadejte název {i + 1}. hráče:")
            players.append(playerLogic.Player(name))
            while False in players[i].placed:
                print("Vyberte loď kterou chcete položit:")
                if not players[i].placed[0]:
                    print("1. Battle Ship (Velikost 5)")
                if not players[i].placed[1]:
                    print("2. Cruiser (Velikost 4)")
                if not players[i].placed[2]:
                    print("3. Submarine (Velikost 3)")
                if not players[i].placed[3]:
                    print("4. Destroyer (Velikost 3)")
                try:
                    ans = int(input("Zadejte číslo (1-4): "))
                    if ans < 1 or ans > 4 or players[i].placed[ans - 1]:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                except ValueError:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

                os.system('cls' if os.name == 'nt' else 'clear')
                players[i].print_board()
                print("Zadejte pozici nejvíce levé horní části lodě.")
                try:
                    cord_x = int(input("Zadejte řádek: "))
                    cord_y = int(input("Zadejte sloupec: "))
                except ValueError:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

                msg = "Zadejte orientaci lode (V - vyska, S - Sirka): "
                ori = input(msg).upper() == 'S'

                match ans:
                    case 1:
                        players[i].place_battleship(cord_x, cord_y, ori)
                    case 2:
                        players[i].place_cruiser(cord_x, cord_y, ori)
                    case 3:
                        players[i].place_submarine(cord_x, cord_y, ori)
                    case 4:
                        players[i].place_destroyer(cord_x, cord_y, ori)
                os.system('cls' if os.name == 'nt' else 'clear')
                players[i].print_board()
                if False not in players[i].placed:
                    input("Pro začátek hry protihráče zmáčkněte enter")
                else:
                    input("Pro polozeni dalsi lode zmacknete enter")
                os.system('cls' if os.name == 'nt' else 'clear')

        while True:
            p_idx = turn % 2
            e_idx = (turn + 1) % 2
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Na tahu je hráč {players[p_idx].name}")
            players[p_idx].print_shoot_board()
            success = True

            while success:
                print(f"Hráč {players[p_idx].name} střílí:")
                try:
                    cord_x = int(input("Zadejte řádek: "))
                    cord_y = int(input("Zadejte sloupec: "))
                    success = players[p_idx].shoot(
                        players[e_idx].board, cord_x, cord_y
                    )
                    os.system('cls' if os.name == 'nt' else 'clear')
                    players[p_idx].print_shoot_board()
                except (ValueError, IndexError):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    players[p_idx].print_shoot_board()
                    print("Zadejte platné číselné hodnoty (0-7)")
                    continue

                if success:
                    if success != "Repeat":
                        players[e_idx].hp -= 1
                        msg = f"Zásah! Životy hráče {players[e_idx].name}: "
                        print(f"{msg}{players[e_idx].hp}")
                if players[e_idx].hp <= 0:
                    break

            if players[e_idx].hp <= 0:
                break
            print("Vedle")
            input("Pro začátek střelby protihráče zmáčkněte enter")
            turn += 1

        print(f"Hráč {players[p_idx].name} vyhrál!")
        again = input("Chcete hrát znova? (Y/n): ").strip().upper()
        if again != 'Y':
            break


if __name__ == "__main__":
    main()
