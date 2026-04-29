import playerLogic
import os

def main():

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
                ans = int(input("Zadejte číslo"))
                if (ans - 1 > 4) or (players[i].Placed[int(ans) - 1]) == True:
                    continue
                players[i].printBoard()
                print("Zadejte Souřadnici nejvíce levé horní pozice lodě a orientaci loďe")
                cordX = int(input("řádek:"))
                cordY = int(input("sloupec:"))
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
                cordX = int(input("řádek:"))
                cordY = int(input("sloupec:"))
                
                success = players[playerTurn].shoot(players[(playerTurn + 1)%2].Board, cordX, cordY)
                if success:
                    players[(playerTurn + 1)%2].Hp -= 1
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
