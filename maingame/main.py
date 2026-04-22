import playerLogic

def main():
    
    while True:
        players = []
        turn = 0
        #setup
        for i in range(2):
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
                print("Zadejte Souřadnici nejvíce levé horní pozice lodě a orientaci loďe")
                cordX = int(input("pozice X:"))
                cordY = int(input("pozice Y:"))

                match ans:
                    case 1 : players[i].placeBattleship(cordX, cordY)
                    case 2 : players[i].placeCruiser(cordX, cordY)
                    case 3 : players[i].placeSubmarine(cordX, cordY)
                    case 4 : players[i].placeDestroyer(cordX, cordY)
                players[i].printBoard()

        
        

        again = input("Chcete hrát znova?(Y,n), default n").strip().upper()
        if again != 'Y':
            break
if __name__ == "__main__":
    main()
