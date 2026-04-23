class Player:
    def __init__(self, Name):
        self.Name = Name
        self.Hp = 12
        self.Board = [['~' for _ in range(8)] for _ in range(8)]
        self.ShootBoard = [['~' for _ in range(8)] for _ in range(8)]
        self.Placed = [False for _ in range(4)]

    def placeBattleship(self, cordX, cordY, orientation = False): #4
        shipLength = 5

        if sonar(self.Board, cordX, cordY, shipLength, orientation):
            if orientation:
                for i in range(shipLength):
                    self.Board[cordX][cordY + i] = '■'
            else:
                for i in range(shipLength):
                    self.Board[cordX + i][cordY] = '■'
            self.Placed[0] = True
        else:
            print("Lodička se nepoložila :(")
    def placeCruiser(self, cordX, cordY, orientation = False): #3
        shipLength = 4
        if sonar(self.Board, cordX, cordY, shipLength, orientation):
            if orientation:
                for i in range(shipLength):
                    self.Board[cordX][cordY + i] = '■'
            else:
                for i in range(shipLength):
                    self.Board[cordX + i][cordY] = '■'
            self.Placed[1] = True
        else:
            print("Lodička se nepoložila :(")
    def placeSubmarine(self, cordX, cordY, orientation = False): #3
        shipLength = 3
        if sonar(self.Board, cordX, cordY, shipLength, orientation):
            if orientation:
                for i in range(shipLength):
                    self.Board[cordX][cordY + i] = '■'
            else:
                for i in range(shipLength):
                    self.Board[cordX + i][cordY] = '■'
            self.Placed[2] = True
        else:
            print("Lodička se nepoložila :(")
    def placeDestroyer(self, cordX, cordY, orientation = False): #2
        shipLength = 3
        if sonar(self.Board, cordX, cordY, shipLength, orientation):
            if orientation:
                for i in range(shipLength):
                    self.Board[cordX][cordY + i] = '■'
            else:
                for i in range(shipLength):
                    self.Board[cordX + i][cordY] = '■'
            self.Placed[3] = True
        else:
            print("Lodička se nepoložila :(")


    def shoot(self, enemyBoard, cordX, cordY):
        if enemyBoard[cordX][cordY] == 'X' or enemyBoard[cordX][cordY] == 'O':
            print("Zadejte pole na které jste ještě nestřílel")
            return True
        if enemyBoard[cordX][cordY] == '■':
            self.ShootBoard[cordX][cordY] = 'X'
            for row in self.ShootBoard:
                print(' '.join(row))

            return True
        else:
            self.ShootBoard[cordX][cordY] = 'O'
            for row in self.ShootBoard:
                print(' '.join(row))
            return False
        


    def printBoard(self):
        print("TABULKA VAŠICH LODÍ")
        print("  0 1 2 3 4 5 6 7")
        i = 0
        for row in self.Board:
            print(str(i) + " " + str(' '.join(row)))
            i += 1

    def printShootBoard(self):
        print("TABULKA ZÁSAHŮ LODÍ")
        print("  0 1 2 3 4 5 6 7")
        i = 0
        for row in self.ShootBoard:
            print(str(i) + " " + str(' '.join(row)))
            i += 1
        
        


def sonar(board, cordX, cordY, shipLenght, orientation = False):
    if (cordX > 7 or cordX < 0 ) or (cordY > 7 or cordY < 0):
        return False
    if orientation:
        if cordY + shipLenght-1 > 7:
            return False
        for i in range(shipLenght):
            if board[cordX][cordY + i] == '■':
                return False
    else:
        if cordX + shipLenght-1 > 7:
                return
        for i in range(shipLenght):
                if board[cordX + i][cordY] == '■':
                    return False
    return True


