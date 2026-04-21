import playerLogic

def main():
    
    while True:
        players = []
        turn = 0
        for i in range(2):
            name = input(f"Zadejte název {i + 1}. hráče:")
            players.append(playerLogic.Player(name))
        for player in players:
            print(player.Name)

        again = input("Chcete hrát znova?(Y,n), default n").strip().upper()
        if again != 'Y':
            break
if __name__ == "__main__":
    main()
