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

Příklad použití
---------------
Po spuštění aplikace vás program provede nastavením::
    Zadejte název 1. hráče: Martin
    Vyberte loď kterou chcete položit:
    1. Battle Ship 5
    řádek: 0
    sloupec: 0
    Zadejte orientaci lode (V - vyska, S - Sirka): S
"""


from . import playerLogic
import os

def main():
    """
    Hlavní smyčka hry (MainLoop).
    
    Zajišťuje inicializaci hráčů, volání metod pro položení lodí
    a řízení střídavých tahů v ShootLoop. Po skončení hry nabízí 
    možnost opakování (Rematch).

    Raises
    ------
    ValueError
        Při zadání nečíselných souřadnic je chyba zachycena 
        a uživatel vyzván k novému zadání.
    """

    while True: #MainLoop
        turn = 0
        players = []
        for i in range(2): #SetupLoop
            name = input(f"Zadejte název {i + 1}. hráče:")
            players.append(playerLogic.Player(name))
            while False in players[i].Placed:
                print("Vyberte loď kterou chcete položit:")
                if players[i].Placed[0] == False:
                    print("1. Battle Ship 5")
                if players[i].Placed[1] == False:
                    print("2. Cruiser 4")
                if players[i].Placed[2] == False:
                    print("3. Submarine 3")
                if players[i].Placed[3] == False:
                    print("4. Destroyer 3")
                try:
                    ans = int(input("Zadejte číslo"))
                except ValueError:
                    continue
                if (ans - 1 > 4) or (players[i].Placed[int(ans) - 1]) == True:
                    continue
                players[i].printBoard()
                print("Zadejte Souřadnici nejvíce levé horní pozice lodě a orientaci loďe")
                try:
                    cordX = int(input("řádek:"))
                    cordY = int(input("sloupec:"))
                except ValueError:
                    print("Zadejte číselné hodnoty")
                    continue

                orientation = input("Zadejte orientaci lode (V - vyska, S - Sirka)") == 'S'

                match ans:
                    case 1 : players[i].placeBattleship(cordX, cordY, orientation)
                    case 2 : players[i].placeCruiser(cordX, cordY, orientation)
                    case 3 : players[i].placeSubmarine(cordX, cordY, orientation)
                    case 4 : players[i].placeDestroyer(cordX, cordY, orientation)
                players[i].printBoard()
                input("Pro polozeni dalsi lode zmacknete enter")
                os.system('Cls')


        while True: #ShootLoop
            playerTurn = turn % 2
            print(f"Na tahu je hráč {players[playerTurn].Name}")
            success = True

            while success:

                print(f"Hráč {players[playerTurn].Name} střílí:")
                try:
                    cordX = int(input("řádek:"))
                    cordY = int(input("sloupec:"))
                except ValueError:
                    print("Zadejte číselné hodnoty")
                    continue
                
                success = players[playerTurn].shoot(players[(playerTurn + 1)%2].Board, cordX, cordY)
                if success:
                    if success != "Repeat":
                        players[(playerTurn + 1)%2].Hp -= 1
                        print(f"Zásah životy hráče {players[(playerTurn + 1)%2].Name}: {players[(playerTurn + 1)%2].Hp}")
                if players[(playerTurn + 1)%2].Hp <= 0:
                    break

            if players[(playerTurn + 1)%2].Hp <= 0:
                        break
            turn += 1


        
        
        print(f"Hráč {players[playerTurn].Name} vyhrál:")
        again = input("Chcete hrát znova?(Y,n), default n").strip().upper()
        if again != 'Y':
            break
        
if __name__ == "__main__":
    main()
